#!/usr/bin/env python3
"""Deep analysis of G2 skills for dependency issues"""

import re
from collections import defaultdict, deque

def parse_allskills(filepath):
    """Parse the allskills.md file and extract ALL skills with their dependencies."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    current_skill = {}
    lines = content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i]

        if line.startswith('ID: '):
            if current_skill and 'id' in current_skill:
                skills[current_skill['id']] = current_skill

            skill_id = line.replace('ID: ', '').strip()
            current_skill = {
                'id': skill_id,
                'topic': '',
                'title': '',
                'description': '',
                'dependencies': []
            }

        elif line.startswith('Topic: ') and current_skill:
            current_skill['topic'] = line.replace('Topic: ', '').strip()

        elif line.startswith('Skill: ') and current_skill:
            current_skill['title'] = line.replace('Skill: ', '').strip()

        elif line.startswith('Description: ') and current_skill:
            current_skill['description'] = line.replace('Description: ', '').strip()

        elif line.startswith('Dependencies:') and current_skill:
            i += 1
            while i < len(lines) and lines[i].startswith('* '):
                dep_line = lines[i].strip('* ').strip()
                if ':' in dep_line:
                    dep_id = dep_line.split(':')[0].strip()
                    current_skill['dependencies'].append(dep_id)
                i += 1
            continue

        i += 1

    if current_skill and 'id' in current_skill:
        skills[current_skill['id']] = current_skill

    return skills

def extract_grade(skill_id):
    """Extract grade from skill ID."""
    match = re.search(r'\.(G\d+|GK)\.', skill_id)
    if match:
        grade = match.group(1)
        if grade == 'GK':
            return 0
        else:
            return int(grade[1:])
    return None

def extract_topic(skill_id):
    """Extract topic from skill ID."""
    match = re.match(r'(T\d+)\.', skill_id)
    if match:
        return match.group(1)
    return None

def check_circular_dependencies(skills, skill_id, visited=None, path=None):
    """Check for circular dependencies using DFS."""
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if skill_id in path:
        return path + [skill_id]

    if skill_id in visited:
        return None

    visited.add(skill_id)
    path.append(skill_id)

    skill = skills.get(skill_id)
    if skill:
        for dep_id in skill['dependencies']:
            result = check_circular_dependencies(skills, dep_id, visited.copy(), path.copy())
            if result:
                return result

    return None

def get_transitive_dependencies(skills, skill_id, seen=None):
    """Get all transitive dependencies."""
    if seen is None:
        seen = set()

    if skill_id in seen or skill_id not in skills:
        return set()

    seen.add(skill_id)
    transitive = set()

    skill = skills[skill_id]
    for dep_id in skill['dependencies']:
        transitive.add(dep_id)
        transitive.update(get_transitive_dependencies(skills, dep_id, seen.copy()))

    return transitive

def check_transitive_redundancy(skills, skill_id):
    """Check if a skill has redundant direct dependencies (already covered transitively)."""
    skill = skills.get(skill_id)
    if not skill:
        return []

    direct_deps = set(skill['dependencies'])
    redundant = []

    for dep_id in direct_deps:
        # Get transitive deps through other direct dependencies
        other_deps = direct_deps - {dep_id}
        indirect = set()
        for other_dep in other_deps:
            indirect.update(get_transitive_dependencies(skills, other_dep))

        if dep_id in indirect:
            redundant.append(dep_id)

    return redundant

def check_same_topic_same_grade(skills, skill_id):
    """Check if skill depends on earlier skills in same topic/same grade."""
    skill = skills.get(skill_id)
    if not skill:
        return []

    skill_grade = extract_grade(skill_id)
    skill_topic = extract_topic(skill_id)

    # Extract sequence number
    match = re.search(r'\.(G\d+|GK)\.(\d+)$', skill_id)
    if not match:
        return []
    skill_seq = int(match.group(2))

    issues = []
    for dep_id in skill['dependencies']:
        dep_grade = extract_grade(dep_id)
        dep_topic = extract_topic(dep_id)

        if dep_topic == skill_topic and dep_grade == skill_grade:
            # Check if it's an earlier skill in sequence
            dep_match = re.search(r'\.(G\d+|GK)\.(\d+)$', dep_id)
            if dep_match:
                dep_seq = int(dep_match.group(2))
                if dep_seq < skill_seq:
                    issues.append(dep_id)

    return issues

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing all skills...")
    all_skills = parse_allskills(filepath)

    # Filter G2 skills
    g2_skills = {sid: skill for sid, skill in all_skills.items() if '.G2.' in sid}

    print(f"\nAnalyzing {len(g2_skills)} G2 skills for detailed issues...\n")

    issues_summary = defaultdict(lambda: {
        'invalid_grade': [],
        'skip_g1_bridge': [],
        'circular': [],
        'transitive_redundant': [],
        'same_topic_grade': []
    })

    for skill_id, skill in sorted(g2_skills.items()):
        skill_grade = extract_grade(skill_id)
        skill_topic = extract_topic(skill_id)

        # Check 1: Invalid grade dependencies
        for dep_id in skill['dependencies']:
            dep_grade = extract_grade(dep_id)
            if dep_grade is not None and dep_grade >= 3:
                issues_summary[skill_id]['invalid_grade'].append(dep_id)

        # Check 2: Skipping G1 bridge (G2 -> GK)
        for dep_id in skill['dependencies']:
            dep_grade = extract_grade(dep_id)
            if dep_grade == 0:  # GK
                issues_summary[skill_id]['skip_g1_bridge'].append(dep_id)

        # Check 3: Circular dependencies
        circular = check_circular_dependencies(all_skills, skill_id)
        if circular:
            issues_summary[skill_id]['circular'] = circular

        # Check 4: Transitive redundancy
        redundant = check_transitive_redundancy(all_skills, skill_id)
        if redundant:
            issues_summary[skill_id]['transitive_redundant'] = redundant

        # Check 5: Same topic/same grade dependencies
        same_topic_deps = check_same_topic_same_grade(all_skills, skill_id)
        if same_topic_deps:
            issues_summary[skill_id]['same_topic_grade'] = same_topic_deps

    # Print detailed report
    print("=" * 100)
    print("DETAILED DEPENDENCY ISSUES FOR G2 SKILLS")
    print("=" * 100)

    total_with_issues = 0
    for skill_id in sorted(issues_summary.keys()):
        has_issues = any(issues_summary[skill_id].values())
        if not has_issues:
            continue

        total_with_issues += 1
        skill = g2_skills[skill_id]

        print(f"\n{skill_id}: {skill['title']}")
        print(f"Topic: {skill['topic']}")
        print(f"Dependencies: {', '.join(skill['dependencies']) if skill['dependencies'] else 'None'}")
        print()

        if issues_summary[skill_id]['invalid_grade']:
            print("  CRITICAL: Depends on G3+ skills:")
            for dep in issues_summary[skill_id]['invalid_grade']:
                print(f"    - {dep}")

        if issues_summary[skill_id]['skip_g1_bridge']:
            print("  WARNING: Depends on K skills (may skip G1 bridge):")
            for dep in issues_summary[skill_id]['skip_g1_bridge']:
                print(f"    - {dep}")

        if issues_summary[skill_id]['circular']:
            print("  CRITICAL: Circular dependency detected:")
            print(f"    Path: {' -> '.join(issues_summary[skill_id]['circular'])}")

        if issues_summary[skill_id]['transitive_redundant']:
            print("  INFO: Transitive redundancy (already covered by other deps):")
            for dep in issues_summary[skill_id]['transitive_redundant']:
                print(f"    - {dep}")

        if issues_summary[skill_id]['same_topic_grade']:
            print("  INFO: Depends on earlier skills in same topic/grade (may be redundant):")
            for dep in issues_summary[skill_id]['same_topic_grade']:
                print(f"    - {dep}")

    # Summary statistics
    print("\n" + "=" * 100)
    print("SUMMARY")
    print("=" * 100)

    count_invalid = sum(1 for issues in issues_summary.values() if issues['invalid_grade'])
    count_skip_bridge = sum(1 for issues in issues_summary.values() if issues['skip_g1_bridge'])
    count_circular = sum(1 for issues in issues_summary.values() if issues['circular'])
    count_transitive = sum(1 for issues in issues_summary.values() if issues['transitive_redundant'])
    count_same_topic = sum(1 for issues in issues_summary.values() if issues['same_topic_grade'])

    print(f"\nTotal G2 skills: {len(g2_skills)}")
    print(f"Skills with issues: {total_with_issues}")
    print(f"\nIssue breakdown:")
    print(f"  - Invalid grade dependencies (G3+): {count_invalid}")
    print(f"  - Skip G1 bridge (G2->GK): {count_skip_bridge}")
    print(f"  - Circular dependencies: {count_circular}")
    print(f"  - Transitive redundancy: {count_transitive}")
    print(f"  - Same topic/grade dependencies: {count_same_topic}")

if __name__ == '__main__':
    main()
