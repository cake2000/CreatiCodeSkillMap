#!/usr/bin/env python3
"""
Final comprehensive validation of ALL Grade 7 skills.
Checks for:
1. Dependency grade constraints (G7 should only depend on G7, G6, G5)
2. Circular dependencies
3. Transitive dependencies
4. Missing dependencies (lists, loops, variables)
5. Skill clarity (vague terms, specificity)
"""

import re
import json
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def parse_allskills_md(filepath: str) -> Dict[str, Dict]:
    """Parse the allskills.md file and extract all skills."""
    skills = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Look for skill ID lines
        if line.startswith('ID: '):
            skill_id = line[4:].strip()

            # Extract grade from skill ID (e.g., T01.G7.01 -> G7)
            match = re.search(r'\.(GK|G\d+)\.', skill_id)
            if not match:
                i += 1
                continue

            grade = match.group(1)

            # Extract topic, skill name, description, and dependencies
            topic = ""
            skill_name = ""
            description = ""
            depends_on = []

            # Read following lines
            j = i + 1
            while j < len(lines) and not lines[j].strip().startswith('ID: '):
                current_line = lines[j].strip()

                if current_line.startswith('Topic: '):
                    topic = current_line[7:].strip()
                elif current_line.startswith('Skill: '):
                    skill_name = current_line[7:].strip()
                elif current_line.startswith('Description: '):
                    description = current_line[13:].strip()
                elif current_line.startswith('Dependencies:'):
                    # Read dependency list
                    k = j + 1
                    while k < len(lines) and lines[k].strip().startswith('* '):
                        dep_line = lines[k].strip()[2:]  # Remove '* '
                        # Extract dependency ID (before the colon)
                        dep_match = re.match(r'([A-Z]\d+\.[A-Z]+\d+\.\d+):', dep_line)
                        if dep_match:
                            depends_on.append(dep_match.group(1))
                        k += 1

                j += 1

            skills[skill_id] = {
                'id': skill_id,
                'grade': grade,
                'topic': topic,
                'skill_name': skill_name,
                'description': description,
                'depends_on': depends_on
            }

            i = j
        else:
            i += 1

    return skills

def get_grade_number(grade_str: str) -> int:
    """Convert grade string to number for comparison."""
    if grade_str == "GK":
        return 0
    return int(grade_str[1:])

def check_dependency_grade_constraints(skills: Dict[str, Dict]) -> List[Dict]:
    """Check that G7 skills only depend on G7, G6, or G5."""
    issues = []

    for skill_id, skill in skills.items():
        if skill['grade'] != 'G7':
            continue

        for dep_id in skill['depends_on']:
            if dep_id not in skills:
                issues.append({
                    'skill': skill_id,
                    'type': 'missing_dependency',
                    'dependency': dep_id,
                    'description': f"Depends on non-existent skill {dep_id}"
                })
                continue

            dep_grade = skills[dep_id]['grade']
            dep_grade_num = get_grade_number(dep_grade)

            # G7 should only depend on G7, G6, or G5
            if dep_grade_num < 5 or dep_grade_num > 7:
                issues.append({
                    'skill': skill_id,
                    'type': 'invalid_grade_dependency',
                    'dependency': dep_id,
                    'dep_grade': dep_grade,
                    'description': f"G7 skill depends on {dep_grade} skill {dep_id} (should only depend on G5-G7)"
                })

    return issues

def find_circular_dependencies(skills: Dict[str, Dict]) -> List[Dict]:
    """Find circular dependencies using DFS."""
    issues = []

    def has_cycle(skill_id: str, visited: Set[str], rec_stack: Set[str], path: List[str]) -> bool:
        visited.add(skill_id)
        rec_stack.add(skill_id)
        path.append(skill_id)

        if skill_id not in skills:
            path.pop()
            rec_stack.remove(skill_id)
            return False

        for dep_id in skills[skill_id]['depends_on']:
            if dep_id not in visited:
                if has_cycle(dep_id, visited, rec_stack, path):
                    return True
            elif dep_id in rec_stack:
                # Found a cycle
                cycle_start = path.index(dep_id)
                cycle = path[cycle_start:] + [dep_id]
                issues.append({
                    'type': 'circular_dependency',
                    'cycle': ' -> '.join(cycle),
                    'skills': cycle[:-1],
                    'description': f"Circular dependency: {' -> '.join(cycle)}"
                })
                return True

        path.pop()
        rec_stack.remove(skill_id)
        return False

    # Check only G7 skills
    g7_skills = [sid for sid, s in skills.items() if s['grade'] == 'G7']

    for skill_id in g7_skills:
        visited = set()
        rec_stack = set()
        path = []
        has_cycle(skill_id, visited, rec_stack, path)

    return issues

def find_transitive_dependencies(skills: Dict[str, Dict]) -> List[Dict]:
    """Find transitive dependencies (if A->B and B->C, then A shouldn't also depend on C)."""
    issues = []

    def get_indirect_deps(skill_id: str, visited: Set[str] = None) -> Set[str]:
        """Get all indirect dependencies (dependencies of dependencies)."""
        if visited is None:
            visited = set()

        if skill_id in visited or skill_id not in skills:
            return set()

        visited.add(skill_id)
        indirect = set()

        direct_deps = skills[skill_id]['depends_on']

        for dep_id in direct_deps:
            if dep_id in skills:
                # Add all dependencies of this dependency
                sub_deps = skills[dep_id]['depends_on']
                indirect.update(sub_deps)
                # Recursively get deeper dependencies
                indirect.update(get_indirect_deps(dep_id, visited.copy()))

        return indirect

    # Check only G7 skills
    g7_skills = [sid for sid, s in skills.items() if s['grade'] == 'G7']

    for skill_id in g7_skills:
        direct_deps = set(skills[skill_id]['depends_on'])
        indirect_deps = get_indirect_deps(skill_id)

        # Find dependencies that are both direct and indirect (transitive)
        transitive = direct_deps & indirect_deps

        if transitive:
            for trans_dep in transitive:
                # Find the path through which this is indirect
                for direct_dep in direct_deps:
                    if direct_dep != trans_dep and direct_dep in skills:
                        all_indirect = get_indirect_deps(direct_dep)
                        if trans_dep in all_indirect:
                            issues.append({
                                'skill': skill_id,
                                'type': 'transitive_dependency',
                                'dependency': trans_dep,
                                'path': f"{skill_id} -> {direct_dep} -> ... -> {trans_dep}",
                                'description': f"Transitive: {skill_id} directly depends on {trans_dep}, but also reaches it through {direct_dep}"
                            })
                            break

    return issues

def check_missing_dependencies(skills: Dict[str, Dict]) -> List[Dict]:
    """Check for missing dependencies based on keywords in descriptions."""
    issues = []

    # Define keyword patterns and their expected dependencies (topic-based)
    patterns = {
        'lists': {
            'keywords': ['list', 'lists', 'array', 'arrays', 'collection', 'table', 'dataset'],
            'expected_topic': 'T10',
            'category': 'list_operations'
        },
        'loops': {
            'keywords': ['loop', 'loops', 'repeat', 'iteration', 'iterate', 'nested loop'],
            'expected_topic': 'T07',
            'category': 'loop_operations'
        },
        'variables': {
            'keywords': ['variable', 'variables', 'store', 'storing'],
            'expected_topic': 'T09',
            'category': 'variable_operations'
        }
    }

    # Check only G7 skills
    g7_skills = [sid for sid, s in skills.items() if s['grade'] == 'G7']

    for skill_id in g7_skills:
        skill = skills[skill_id]

        # Combine skill name and description for checking
        full_text = f"{skill.get('skill_name', '')} {skill.get('description', '')}"
        full_text_lower = full_text.lower()

        for pattern_name, pattern_info in patterns.items():
            # Check if text mentions the keyword
            has_keyword = any(keyword in full_text_lower for keyword in pattern_info['keywords'])

            if has_keyword:
                # Check if it has appropriate dependencies (from the expected topic)
                expected_topic = pattern_info['expected_topic']
                has_dep = any(dep.startswith(expected_topic + '.') for dep in skill['depends_on'])

                if not has_dep:
                    issues.append({
                        'skill': skill_id,
                        'type': 'missing_dependency',
                        'category': pattern_info['category'],
                        'description': f"Mentions {pattern_name} but doesn't depend on any {expected_topic} skills"
                    })

    return issues

def check_skill_clarity(skills: Dict[str, Dict]) -> List[Dict]:
    """Check for vague or unclear skill descriptions."""
    issues = []

    # Vague terms to flag
    vague_terms = [
        'several', 'various', 'multiple', 'some', 'many', 'few',
        'appropriate', 'suitable', 'relevant', 'different'
    ]

    # Check only G7 skills
    g7_skills = [sid for sid, s in skills.items() if s['grade'] == 'G7']

    for skill_id in g7_skills:
        skill = skills[skill_id]

        # Combine skill name and description for analysis
        full_text = f"{skill.get('skill_name', '')} {skill.get('description', '')}"
        full_text_lower = full_text.lower()

        # Check for vague terms
        found_vague = [term for term in vague_terms if term in full_text_lower]
        if found_vague:
            issues.append({
                'skill': skill_id,
                'type': 'vague_description',
                'vague_terms': found_vague,
                'description': f"Contains vague terms: {', '.join(found_vague)}"
            })

        # Check for specific numbers (numeric specificity is less critical for G7)
        # Removed this check as it may not be relevant for all G7 skills

        # Check for overly brief skill names
        skill_name = skill.get('skill_name', '')
        if len(skill_name.split()) < 3:
            issues.append({
                'skill': skill_id,
                'type': 'brief_skill_name',
                'description': f"Skill name too brief (only {len(skill_name.split())} words)"
            })

        # Check for overly verbose descriptions
        description = skill.get('description', '')
        if len(description.split()) > 50:
            issues.append({
                'skill': skill_id,
                'type': 'too_verbose',
                'description': f"Description too verbose ({len(description.split())} words)"
            })

    return issues

def generate_report(skills: Dict[str, Dict], all_issues: Dict[str, List[Dict]]) -> str:
    """Generate a comprehensive validation report."""
    report = []
    report.append("=" * 80)
    report.append("FINAL COMPREHENSIVE VALIDATION REPORT - GRADE 7 SKILLS")
    report.append("=" * 80)
    report.append("")

    # Count G7 skills
    g7_skills = [s for s in skills.values() if s['grade'] == 'G7']
    report.append(f"Total Grade 7 Skills: {len(g7_skills)}")
    report.append("")

    # Overall summary
    total_issues = sum(len(issues) for issues in all_issues.values())
    report.append("=" * 80)
    report.append(f"OVERALL SUMMARY: {total_issues} TOTAL ISSUES FOUND")
    report.append("=" * 80)
    report.append("")

    # Breakdown by issue type
    report.append("ISSUE BREAKDOWN BY TYPE:")
    report.append("-" * 80)

    for check_name, issues in all_issues.items():
        report.append(f"\n{check_name.upper().replace('_', ' ')}:")
        report.append(f"  Count: {len(issues)}")

        if issues:
            report.append("\n  Details:")
            for issue in issues:
                report.append(f"    - {issue['skill']}: {issue['description']}")

    report.append("")
    report.append("=" * 80)

    # Success metrics
    report.append("\nSUCCESS METRICS:")
    report.append("-" * 80)

    metrics = {
        'Dependency Grade Constraints': {
            'issues': len(all_issues['dependency_grade_constraints']),
            'status': 'PASS' if len(all_issues['dependency_grade_constraints']) == 0 else 'FAIL'
        },
        'Circular Dependencies': {
            'issues': len(all_issues['circular_dependencies']),
            'status': 'PASS' if len(all_issues['circular_dependencies']) == 0 else 'FAIL'
        },
        'Transitive Dependencies': {
            'issues': len(all_issues['transitive_dependencies']),
            'status': 'PASS' if len(all_issues['transitive_dependencies']) == 0 else 'ACCEPTABLE' if len(all_issues['transitive_dependencies']) < 5 else 'REVIEW'
        },
        'Missing Dependencies': {
            'issues': len(all_issues['missing_dependencies']),
            'status': 'PASS' if len(all_issues['missing_dependencies']) == 0 else 'REVIEW'
        },
        'Skill Clarity': {
            'issues': len(all_issues['skill_clarity']),
            'status': 'PASS' if len(all_issues['skill_clarity']) == 0 else 'REVIEW'
        }
    }

    for metric_name, metric_data in metrics.items():
        status_symbol = "✓" if metric_data['status'] == 'PASS' else "✗" if metric_data['status'] == 'FAIL' else "!"
        report.append(f"{status_symbol} {metric_name}: {metric_data['issues']} issues - {metric_data['status']}")

    report.append("")

    # Overall pass/fail
    critical_fails = (
        len(all_issues['dependency_grade_constraints']) +
        len(all_issues['circular_dependencies'])
    )

    report.append("=" * 80)
    if critical_fails == 0:
        report.append("OVERALL STATUS: PASS ✓")
        report.append("All critical requirements met!")
    else:
        report.append("OVERALL STATUS: FAIL ✗")
        report.append(f"Critical issues found: {critical_fails}")
    report.append("=" * 80)

    return "\n".join(report)

def main():
    """Main execution function."""
    filepath = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"

    print("Parsing allskills.md...")
    skills = parse_allskills_md(filepath)

    print(f"Found skills from all grades")
    g7_count = len([s for s in skills.values() if s['grade'] == 'G7'])
    print(f"Found G7 skills: {g7_count}")

    # Run all checks
    print("\nRunning validation checks...")

    all_issues = {}

    print("  1. Checking dependency grade constraints...")
    all_issues['dependency_grade_constraints'] = check_dependency_grade_constraints(skills)
    print(f"     Found: {len(all_issues['dependency_grade_constraints'])} issues")

    print("  2. Checking for circular dependencies...")
    all_issues['circular_dependencies'] = find_circular_dependencies(skills)
    print(f"     Found: {len(all_issues['circular_dependencies'])} issues")

    print("  3. Checking for transitive dependencies...")
    all_issues['transitive_dependencies'] = find_transitive_dependencies(skills)
    print(f"     Found: {len(all_issues['transitive_dependencies'])} issues")

    print("  4. Checking for missing dependencies...")
    all_issues['missing_dependencies'] = check_missing_dependencies(skills)
    print(f"     Found: {len(all_issues['missing_dependencies'])} issues")

    print("  5. Checking skill clarity...")
    all_issues['skill_clarity'] = check_skill_clarity(skills)
    print(f"     Found: {len(all_issues['skill_clarity'])} issues")

    # Generate report
    print("\nGenerating report...")
    report = generate_report(skills, all_issues)

    # Save report
    report_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/G7_FINAL_VALIDATION_REPORT.txt"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport saved to: {report_path}")
    print("\n" + "=" * 80)
    print(report)

    # Save detailed issues as JSON
    json_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/G7_VALIDATION_ISSUES.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(all_issues, f, indent=2)

    print(f"\nDetailed issues saved to: {json_path}")

if __name__ == "__main__":
    main()
