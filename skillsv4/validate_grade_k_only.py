#!/usr/bin/env python3
"""
Validate only Grade K skills for Phase 2 changes.
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

def validate_grade_k_skills(skills: Dict[str, Dict]) -> Dict:
    """Validate only Grade K skills."""
    grade_k_skills = {sid: data for sid, data in skills.items() if '.GK.' in sid}

    errors = []
    warnings = []

    print(f"Total Grade K Skills: {len(grade_k_skills)}")

    # Check each Grade K skill
    for skill_id, skill_data in grade_k_skills.items():
        for dep_id in skill_data['dependencies']:
            # Check if dependency exists
            if dep_id not in skills:
                errors.append(f"{skill_id} depends on non-existent skill {dep_id}")
                continue

            # Check if dependency is Grade K (allowed)
            if '.GK.' in dep_id:
                continue

            # Check if dependency is Grade 1 or higher (NOT allowed for Grade K)
            if '.G1.' in dep_id or '.G2.' in dep_id or '.G3.' in dep_id or \
               '.G4.' in dep_id or '.G5.' in dep_id or '.G6.' in dep_id or \
               '.G7.' in dep_id or '.G8.' in dep_id:
                errors.append(
                    f"X-2 VIOLATION: Grade K skill {skill_id} depends on "
                    f"{dep_id} ({skills[dep_id]['grade']})"
                )

    # Check for circular dependencies within Grade K
    def has_cycle(skill_id: str, path: Set[str]) -> bool:
        if skill_id in path:
            return True
        if skill_id not in grade_k_skills:
            return False

        path.add(skill_id)
        for dep_id in grade_k_skills[skill_id]['dependencies']:
            if has_cycle(dep_id, path.copy()):
                errors.append(f"Circular dependency involving {skill_id}")
                return True
        return False

    for skill_id in grade_k_skills:
        has_cycle(skill_id, set())

    return {
        'total_skills': len(grade_k_skills),
        'errors': errors,
        'warnings': warnings,
        'valid': len(errors) == 0
    }

def get_phase2_changes() -> Set[tuple]:
    """Return the 7 dependencies added in Phase 2."""
    return {
        ('T01.GK.08', 'T09.GK.01'),
        ('T13.GK.01', 'T02.GK.01'),
        ('T14.GK.01', 'T02.GK.01'),
        ('T08.GK.02', 'T06.GK.01'),
        ('T10.GK.03', 'T09.GK.01'),
        ('T27.GK.02', 'T09.GK.01'),
        ('T26.GK.02', 'T09.GK.01'),
    }

def verify_phase2_additions(skills: Dict[str, Dict]) -> Dict:
    """Verify all Phase 2 additions were applied."""
    expected = get_phase2_changes()
    found = []
    missing = []

    for skill_id, dep_id in expected:
        if skill_id in skills and dep_id in skills[skill_id]['dependencies']:
            found.append((skill_id, dep_id))
        else:
            missing.append((skill_id, dep_id))

    return {
        'expected': len(expected),
        'found': len(found),
        'missing': missing,
        'all_applied': len(missing) == 0
    }

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills file...")
    skills = parse_skills(filepath)
    print(f"Total skills parsed: {len(skills)}\n")

    print("=== VALIDATING GRADE K SKILLS ===\n")
    validation = validate_grade_k_skills(skills)

    print(f"Total Grade K Skills: {validation['total_skills']}")

    if validation['errors']:
        print(f"\n✗ FOUND {len(validation['errors'])} ERRORS:")
        for error in validation['errors'][:10]:  # Show first 10
            print(f"  - {error}")
        if len(validation['errors']) > 10:
            print(f"  ... and {len(validation['errors']) - 10} more")
    else:
        print("\n✓ No Grade K validation errors")

    print("\n=== VERIFYING PHASE 2 ADDITIONS ===\n")
    phase2 = verify_phase2_additions(skills)

    print(f"Expected additions: {phase2['expected']}")
    print(f"Actually applied: {phase2['found']}")

    if phase2['missing']:
        print(f"\n✗ MISSING {len(phase2['missing'])} DEPENDENCIES:")
        for skill_id, dep_id in phase2['missing']:
            print(f"  - {skill_id} -> {dep_id}")
    else:
        print("\n✓ All Phase 2 dependencies successfully applied")

    # Count Grade K dependencies
    grade_k_skills = {sid: data for sid, data in skills.items() if '.GK.' in sid}
    cross_topic = 0
    within_topic = 0

    for skill_id, skill_data in grade_k_skills.items():
        skill_topic = skill_id.split('.')[0]
        for dep_id in skill_data['dependencies']:
            dep_topic = dep_id.split('.')[0]
            if dep_topic != skill_topic:
                cross_topic += 1
            else:
                within_topic += 1

    print("\n=== GRADE K DEPENDENCY STATISTICS ===\n")
    print(f"Cross-Topic Dependencies: {cross_topic}")
    print(f"Within-Topic Dependencies: {within_topic}")
    print(f"Total Dependencies: {cross_topic + within_topic}")

    print("\n=== OVERALL RESULT ===")
    if validation['valid'] and phase2['all_applied']:
        print("✓ ALL GRADE K VALIDATIONS PASSED")
        print("✓ ALL PHASE 2 CHANGES SUCCESSFULLY APPLIED")
        return True
    else:
        print("✗ VALIDATION ISSUES FOUND")
        return False

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
