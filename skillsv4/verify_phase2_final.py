#!/usr/bin/env python3
"""
Final verification of Phase 2 changes - focus on what matters.
"""

import re
from typing import Dict, List, Set

def parse_skills(filepath: str) -> Dict[str, Dict]:
    """Parse all skills from the file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    skill_pattern = r'ID: (T\d+\.(GK|G\d+)\.\d+)\s*\nTopic: ([^\n]+)\s*\nSkill: ([^\n]+)'

    for match in re.finditer(skill_pattern, content):
        skill_id = match.group(1)
        grade = match.group(2)
        topic = match.group(3)
        skill_name = match.group(4)

        end_pos = match.end()
        remaining = content[end_pos:end_pos+2000]

        deps = []
        dep_match = re.search(r'Dependencies:\s*\n((?:\* [^\n]+\n?)+)', remaining)
        if dep_match:
            dep_text = dep_match.group(1)
            for line in dep_text.strip().split('\n'):
                if line.startswith('* '):
                    dep_id = line.split(':')[0].replace('* ', '').strip()
                    deps.append(dep_id)

        skills[skill_id] = {
            'grade': grade,
            'topic': topic,
            'name': skill_name,
            'dependencies': deps
        }

    return skills

def get_phase2_changes() -> List[tuple]:
    """Return the 7 dependencies added in Phase 2."""
    return [
        ('T01.GK.08', 'T09.GK.01', 'Count how many times', 'Recognize that a label can hold a number'),
        ('T13.GK.01', 'T02.GK.01', 'Spot a missing or wrong action in an animation', 'Recognize picture steps for a task'),
        ('T14.GK.01', 'T02.GK.01', 'Match controls to character actions', 'Recognize picture steps for a task'),
        ('T08.GK.02', 'T06.GK.01', 'Choose what happens next based on yes/no', 'Order pictures showing a morning routine (event sequence concept)'),
        ('T10.GK.03', 'T09.GK.01', 'Find which group has more', 'Recognize that a label can hold a number'),
        ('T27.GK.02', 'T09.GK.01', 'Compare which group has more', 'Recognize that a label can hold a number'),
        ('T26.GK.02', 'T09.GK.01', 'Use tokens to log repeated events', 'Recognize that a label can hold a number'),
    ]

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("=" * 70)
    print("PHASE 2 VERIFICATION REPORT")
    print("=" * 70)

    print("\nParsing skills file...")
    skills = parse_skills(filepath)
    print(f"Total skills parsed: {len(skills)}")

    grade_k_skills = {sid: data for sid, data in skills.items() if '.GK.' in sid}
    print(f"Total Grade K skills: {len(grade_k_skills)}")

    print("\n" + "=" * 70)
    print("VERIFYING PHASE 2 ADDITIONS")
    print("=" * 70)

    changes = get_phase2_changes()
    applied = []
    missing = []
    invalid = []

    for skill_id, dep_id, skill_name, dep_name in changes:
        status = "✓"
        issue = None

        # Check if skill exists
        if skill_id not in skills:
            status = "✗"
            issue = f"Skill {skill_id} not found"
            invalid.append((skill_id, dep_id, issue))
            continue

        # Check if dependency exists
        if dep_id not in skills:
            status = "✗"
            issue = f"Dependency {dep_id} not found"
            invalid.append((skill_id, dep_id, issue))
            continue

        # Check if dependency was added
        if dep_id in skills[skill_id]['dependencies']:
            applied.append((skill_id, dep_id, skill_name, dep_name))
            print(f"\n{status} {skill_id}: {skill_name}")
            print(f"   Added dependency: {dep_id} - {dep_name}")
        else:
            status = "✗"
            issue = f"Dependency {dep_id} not in {skill_id}'s dependency list"
            missing.append((skill_id, dep_id, issue))
            print(f"\n{status} {skill_id}: {skill_name}")
            print(f"   MISSING dependency: {dep_id} - {dep_name}")

    print("\n" + "=" * 70)
    print("CHECKING FOR X-2 VIOLATIONS IN PHASE 2 CHANGES")
    print("=" * 70)

    violations = []
    for skill_id, dep_id, skill_name, dep_name in applied:
        # All Phase 2 changes are Grade K -> Grade K, so no X-2 violations possible
        if '.GK.' not in dep_id:
            violations.append(f"{skill_id} -> {dep_id} (not Grade K)")

    if violations:
        print("\n✗ FOUND VIOLATIONS:")
        for v in violations:
            print(f"  - {v}")
    else:
        print("\n✓ No X-2 violations - all dependencies are Grade K -> Grade K")

    print("\n" + "=" * 70)
    print("GRADE K DEPENDENCY STATISTICS")
    print("=" * 70)

    cross_topic = 0
    within_topic = 0

    for skill_id, skill_data in grade_k_skills.items():
        skill_topic = skill_id.split('.')[0]
        for dep_id in skill_data['dependencies']:
            if dep_id not in skills:
                continue
            dep_topic = dep_id.split('.')[0]
            if dep_topic != skill_topic:
                cross_topic += 1
            else:
                within_topic += 1

    print(f"\nTotal Grade K Skills: {len(grade_k_skills)}")
    print(f"Cross-Topic Dependencies: {cross_topic}")
    print(f"Within-Topic Dependencies: {within_topic}")
    print(f"Total Dependencies: {cross_topic + within_topic}")
    print(f"Average Dependencies per Skill: {(cross_topic + within_topic) / len(grade_k_skills):.2f}")

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)

    print(f"\nPhase 2 Changes Expected: {len(changes)}")
    print(f"Successfully Applied: {len(applied)}")
    print(f"Missing: {len(missing)}")
    print(f"Invalid: {len(invalid)}")

    if len(applied) == len(changes) and len(violations) == 0:
        print("\n✓ ALL PHASE 2 CHANGES SUCCESSFULLY APPLIED")
        print("✓ NO X-2 RULE VIOLATIONS INTRODUCED")
        print("✓ ALL VALIDATIONS PASSED")
        return True
    else:
        print("\n✗ SOME ISSUES FOUND")
        return False

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
