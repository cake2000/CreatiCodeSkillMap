#!/usr/bin/env python3
"""
Validate that all G7 skills now only depend on G5, G6, or G7 skills.
"""

import re
from collections import defaultdict

def parse_skills_file(filepath):
    """Parse the allskills.md file and extract all skills."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    skill_blocks = re.split(r'\n(?=ID: T\d+\.G)', content)

    for block in skill_blocks:
        if not block.strip():
            continue

        id_match = re.search(r'ID:\s*(T\d+\.G\d+\.\d+)', block)
        if not id_match:
            continue

        skill_id = id_match.group(1)
        skill_match = re.search(r'Skill:\s*(.+)', block)
        title = skill_match.group(1).strip() if skill_match else ''

        deps = []
        dep_section = re.search(r'Dependencies:\s*\n((?:\*.*\n)*)', block)
        if dep_section:
            dep_text = dep_section.group(1)
            deps = re.findall(r'T\d+\.G\d+\.\d+', dep_text)

        skills[skill_id] = {
            'id': skill_id,
            'title': title,
            'dependencies': deps
        }

    return skills

def get_grade(skill_id):
    """Extract grade number from skill ID."""
    match = re.search(r'\.G(\d+)\.', skill_id)
    return int(match.group(1)) if match else 0

def validate_g7_skills(skills):
    """Validate that G7 skills only depend on G5, G6, or G7."""
    g7_skills = {sid: s for sid, s in skills.items() if get_grade(sid) == 7}

    print(f"Total G7 skills found: {len(g7_skills)}")
    print()

    violations = []
    low_grade_deps = defaultdict(list)

    for skill_id, skill in g7_skills.items():
        for dep in skill['dependencies']:
            dep_grade = get_grade(dep)

            if dep_grade < 5:
                violations.append({
                    'skill_id': skill_id,
                    'skill_title': skill['title'],
                    'dep_id': dep,
                    'dep_grade': dep_grade
                })
                low_grade_deps[dep_grade].append(skill_id)

    return violations, low_grade_deps, g7_skills

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("=" * 80)
    print("G7 VALIDATION")
    print("=" * 80)
    print()

    print("Parsing skills file...")
    skills = parse_skills_file(filepath)
    print(f"Total skills parsed: {len(skills)}")
    print()

    print("Validating G7 skills...")
    violations, low_grade_deps, g7_skills = validate_g7_skills(skills)
    print()

    print("=" * 80)
    print("VALIDATION RESULTS")
    print("=" * 80)
    print()

    if not violations:
        print("SUCCESS! All G7 skills only depend on G5, G6, or G7 skills.")
        print()
        print(f"Total G7 skills validated: {len(g7_skills)}")
        print()

        dep_counts = defaultdict(int)
        for skill in g7_skills.values():
            for dep in skill['dependencies']:
                dep_grade = get_grade(dep)
                dep_counts[dep_grade] += 1

        print("Dependency distribution:")
        for grade in sorted(dep_counts.keys()):
            if grade >= 5:
                print(f"  G{grade}: {dep_counts[grade]} dependencies")
        print()

        print("=" * 80)
        print("VALIDATION PASSED")
        print("=" * 80)
    else:
        print(f"FAILED! Found {len(violations)} violations:")
        print()

        print("Low-grade dependencies by grade:")
        for grade in sorted(low_grade_deps.keys()):
            print(f"  G{grade}: {len(low_grade_deps[grade])} skills affected")
        print()

        print("First 10 violations:")
        for i, v in enumerate(violations[:10], 1):
            print(f"{i}. {v['skill_id']} depends on {v['dep_id']} (G{v['dep_grade']})")

        if len(violations) > 10:
            print(f"... and {len(violations) - 10} more")

        print()
        print("=" * 80)
        print("VALIDATION FAILED")
        print("=" * 80)

if __name__ == '__main__':
    main()
