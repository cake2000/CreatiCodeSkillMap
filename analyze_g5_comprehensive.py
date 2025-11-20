#!/usr/bin/env python3
"""
Comprehensive analysis of Grade 5 skills for dependency issues.
"""

import re
from typing import Dict, List, Set, Tuple
from collections import defaultdict

def parse_skills_file(filepath: str) -> Dict[str, dict]:
    """Parse the allskills.md file and extract all skills with their dependencies."""
    skills = {}
    current_skill = None
    current_deps = []

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Check for skill ID
        if line.startswith('ID: '):
            # Save previous skill if exists
            if current_skill:
                skills[current_skill['id']] = current_skill

            skill_id = line[4:].strip()
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': []
            }
            current_deps = []

        elif current_skill:
            if line.startswith('Topic: '):
                current_skill['topic'] = line[7:].strip()
            elif line.startswith('Skill: '):
                current_skill['skill'] = line[7:].strip()
            elif line.startswith('Description: '):
                current_skill['description'] = line[13:].strip()
            elif line.startswith('Dependencies:'):
                # Read dependency lines
                j = i + 1
                while j < len(lines):
                    dep_line = lines[j].strip()
                    if dep_line.startswith('* '):
                        # Extract dependency ID
                        dep_match = re.match(r'\* ([^:]+):', dep_line)
                        if dep_match:
                            current_deps.append(dep_match.group(1).strip())
                        j += 1
                    elif dep_line == '':
                        j += 1
                    else:
                        break
                current_skill['dependencies'] = current_deps
                i = j - 1

        i += 1

    # Save last skill
    if current_skill:
        skills[current_skill['id']] = current_skill

    return skills

def get_grade_from_id(skill_id: str) -> str:
    """Extract grade from skill ID (e.g., 'T01.G5.01' -> 'G5')."""
    parts = skill_id.split('.')
    if len(parts) >= 2:
        return parts[1]
    return ''

def get_topic_from_id(skill_id: str) -> str:
    """Extract topic from skill ID (e.g., 'T01.G5.01' -> 'T01')."""
    parts = skill_id.split('.')
    if len(parts) >= 1:
        return parts[0]
    return ''

def get_transitive_deps(skill_id: str, skills: Dict[str, dict], visited: Set[str] = None) -> Set[str]:
    """Get all transitive dependencies of a skill."""
    if visited is None:
        visited = set()

    if skill_id in visited or skill_id not in skills:
        return set()

    visited.add(skill_id)
    all_deps = set()

    for dep in skills[skill_id]['dependencies']:
        if dep in skills:
            all_deps.add(dep)
            all_deps.update(get_transitive_deps(dep, skills, visited.copy()))

    return all_deps

def detect_circular_dependencies(skill_id: str, skills: Dict[str, dict], path: List[str] = None) -> List[List[str]]:
    """Detect circular dependencies starting from a skill."""
    if path is None:
        path = []

    cycles = []

    if skill_id in path:
        # Found a cycle
        cycle_start = path.index(skill_id)
        cycles.append(path[cycle_start:] + [skill_id])
        return cycles

    if skill_id not in skills:
        return cycles

    new_path = path + [skill_id]

    for dep in skills[skill_id]['dependencies']:
        cycles.extend(detect_circular_dependencies(dep, skills, new_path))

    return cycles

def analyze_g5_skills(skills: Dict[str, dict]) -> Dict[str, List[dict]]:
    """Analyze all G5 skills for issues."""
    issues = {
        'HIGH': [],
        'MEDIUM': [],
        'LOW': []
    }

    # Get all G5 skills
    g5_skills = {sid: s for sid, s in skills.items() if get_grade_from_id(sid) == 'G5'}

    print(f"Found {len(g5_skills)} Grade 5 skills to analyze")

    for skill_id, skill in g5_skills.items():
        topic = get_topic_from_id(skill_id)

        # Rule 1: Check dependencies on G1/G2 (HIGH priority)
        for dep_id in skill['dependencies']:
            dep_grade = get_grade_from_id(dep_id)
            if dep_grade in ['G1', 'G2']:
                issues['HIGH'].append({
                    'skill_id': skill_id,
                    'skill_name': skill['skill'],
                    'issue_type': 'Invalid grade dependency',
                    'priority': 'HIGH',
                    'current_state': f"Depends on {dep_id} (Grade {dep_grade})",
                    'recommended_fix': f"Remove dependency on {dep_id} or find appropriate G3/G4/G5 alternative",
                    'explanation': f"G5 skills should not depend on G1 or G2 skills. This creates an inappropriate grade-level gap."
                })

        # Rule 2: Check for dependencies on higher grades (HIGH priority)
        for dep_id in skill['dependencies']:
            if dep_id not in skills:
                continue
            dep_grade = get_grade_from_id(dep_id)
            if dep_grade in ['G6', 'G7', 'G8', 'MS', 'HS']:
                issues['HIGH'].append({
                    'skill_id': skill_id,
                    'skill_name': skill['skill'],
                    'issue_type': 'Out of order dependency',
                    'priority': 'HIGH',
                    'current_state': f"Depends on {dep_id} (Grade {dep_grade})",
                    'recommended_fix': f"Remove dependency on {dep_id} - it's from a higher grade",
                    'explanation': f"A G5 skill cannot depend on a {dep_grade} skill (out of order)."
                })

        # Rule 3: Check for circular dependencies (HIGH priority)
        cycles = detect_circular_dependencies(skill_id, skills)
        if cycles:
            for cycle in cycles:
                # Only report if this skill is the first in the alphabetically sorted cycle
                # to avoid duplicate reports
                if skill_id == min(cycle):
                    issues['HIGH'].append({
                        'skill_id': skill_id,
                        'skill_name': skill['skill'],
                        'issue_type': 'Circular dependency',
                        'priority': 'HIGH',
                        'current_state': f"Circular chain: {' -> '.join(cycle)}",
                        'recommended_fix': "Break the circular dependency by removing one of the links in the chain",
                        'explanation': "Circular dependencies create logical impossibilities in the learning sequence."
                    })

        # Rule 4: Check for transitive dependencies (MEDIUM priority)
        if len(skill['dependencies']) > 1:
            direct_deps = set(skill['dependencies'])
            for dep_id in skill['dependencies']:
                if dep_id not in skills:
                    continue
                # Get transitive deps of this dependency
                trans_deps = get_transitive_deps(dep_id, skills)
                # Check if any other direct dependency is actually a transitive one
                redundant = direct_deps.intersection(trans_deps)
                for red_dep in redundant:
                    issues['MEDIUM'].append({
                        'skill_id': skill_id,
                        'skill_name': skill['skill'],
                        'issue_type': 'Transitive dependency',
                        'priority': 'MEDIUM',
                        'current_state': f"Directly depends on both {dep_id} and {red_dep}, but {dep_id} already depends on {red_dep}",
                        'recommended_fix': f"Remove direct dependency on {red_dep} (it's already transitively included via {dep_id})",
                        'explanation': "Redundant direct dependency that's already covered transitively."
                    })

        # Rule 5: Check for same-topic, same-grade dependencies (MEDIUM priority)
        for dep_id in skill['dependencies']:
            if dep_id not in skills:
                continue
            dep_grade = get_grade_from_id(dep_id)
            dep_topic = get_topic_from_id(dep_id)

            if dep_grade == 'G5' and dep_topic == topic:
                issues['MEDIUM'].append({
                    'skill_id': skill_id,
                    'skill_name': skill['skill'],
                    'issue_type': 'Same-topic same-grade dependency',
                    'priority': 'MEDIUM',
                    'current_state': f"Depends on {dep_id} (same topic {topic}, same grade G5)",
                    'recommended_fix': f"Remove dependency on {dep_id} - skills in the same topic and grade are learned sequentially",
                    'explanation': "Skills within the same topic and grade level are assumed to be learned in sequence order and should not have explicit dependencies on each other."
                })

        # Rule 6: Check for missing dependencies (MEDIUM priority)
        # This is more heuristic - check if description mentions concepts not in dependencies
        # For now, we'll skip this as it requires semantic analysis

        # Rule 7: Check for overly broad skills (LOW priority)
        # Check if description is very long or mentions many different concepts
        desc = skill['description'].lower()
        if len(desc) > 500 or desc.count(' and ') > 5:
            issues['LOW'].append({
                'skill_id': skill_id,
                'skill_name': skill['skill'],
                'issue_type': 'Possibly overly broad skill',
                'priority': 'LOW',
                'current_state': f"Description length: {len(desc)} chars, contains {desc.count(' and ')} 'and' conjunctions",
                'recommended_fix': "Consider breaking into multiple smaller, more focused skills",
                'explanation': "Very long or complex descriptions may indicate a skill that's trying to cover too much."
            })

    return issues

def generate_report(issues: Dict[str, List[dict]]) -> str:
    """Generate a comprehensive report of all issues."""
    report = []
    report.append("=" * 80)
    report.append("GRADE 5 SKILLS - COMPREHENSIVE DEPENDENCY ANALYSIS REPORT")
    report.append("=" * 80)
    report.append("")

    # Summary
    total_high = len(issues['HIGH'])
    total_medium = len(issues['MEDIUM'])
    total_low = len(issues['LOW'])
    total = total_high + total_medium + total_low

    report.append("EXECUTIVE SUMMARY")
    report.append("-" * 80)
    report.append(f"Total issues found: {total}")
    report.append(f"  HIGH priority:   {total_high}")
    report.append(f"  MEDIUM priority: {total_medium}")
    report.append(f"  LOW priority:    {total_low}")
    report.append("")

    # Detailed issues by priority
    for priority in ['HIGH', 'MEDIUM', 'LOW']:
        if issues[priority]:
            report.append("")
            report.append("=" * 80)
            report.append(f"{priority} PRIORITY ISSUES ({len(issues[priority])} issues)")
            report.append("=" * 80)
            report.append("")

            # Group by issue type
            by_type = defaultdict(list)
            for issue in issues[priority]:
                by_type[issue['issue_type']].append(issue)

            for issue_type, type_issues in sorted(by_type.items()):
                report.append(f"\n{issue_type} ({len(type_issues)} issues)")
                report.append("-" * 80)

                for i, issue in enumerate(type_issues, 1):
                    report.append(f"\nIssue #{i}:")
                    report.append(f"  Skill ID: {issue['skill_id']}")
                    report.append(f"  Skill Name: {issue['skill_name']}")
                    report.append(f"  Current State: {issue['current_state']}")
                    report.append(f"  Recommended Fix: {issue['recommended_fix']}")
                    report.append(f"  Explanation: {issue['explanation']}")

    return '\n'.join(report)

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills file...")
    skills = parse_skills_file(filepath)
    print(f"Parsed {len(skills)} total skills")

    print("\nAnalyzing G5 skills...")
    issues = analyze_g5_skills(skills)

    print("\nGenerating report...")
    report = generate_report(issues)

    # Save to file
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G5_COMPREHENSIVE_ANALYSIS_REPORT.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport saved to: {output_file}")
    print("\n" + "=" * 80)
    print(report)

if __name__ == '__main__':
    main()
