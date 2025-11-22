#!/usr/bin/env python3
"""
Verify T20 intra-topic dependencies in allskills.md
"""

import re
from collections import defaultdict

def parse_grade(skill_id):
    """Extract grade from skill ID (e.g., T20.G3.01 -> 3)"""
    match = re.match(r'T\d+\.G([KK0-9]+)', skill_id)
    if match:
        grade_str = match.group(1)
        if grade_str == 'K':
            return 0
        return int(grade_str)
    return None

def parse_skill_number(skill_id):
    """Extract skill number for ordering (e.g., T20.G3.01 -> 1, T20.G3.05.01 -> 5.01)"""
    parts = skill_id.split('.')
    if len(parts) >= 3:
        # Handle both T20.G3.01 and T20.G3.05.01
        skill_parts = parts[2:]
        try:
            return float('.'.join(skill_parts))
        except ValueError:
            # Handle non-numeric parts (like T04.G2.04a)
            # Just use the first numeric part
            try:
                return float(skill_parts[0])
            except:
                return 0
    return 0

def read_skills(filename):
    """Parse all T20 skills from allskills.md"""
    all_skills = {}
    current_skill = None
    in_dependencies = False
    in_t20_section = False

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()

            # Check for any skill ID
            id_match = re.match(r'^ID:\s+(T\d+\.\S+)', line)
            if id_match:
                skill_id = id_match.group(1)

                # Track if we're in T20 section
                if skill_id.startswith('T20.'):
                    in_t20_section = True
                elif skill_id.startswith('T21.'):
                    # End of T20 section
                    in_t20_section = False

                current_skill = {
                    'id': skill_id,
                    'grade': parse_grade(skill_id),
                    'skill_number': parse_skill_number(skill_id),
                    'skill_name': '',
                    'dependencies': []
                }
                all_skills[skill_id] = current_skill
                in_dependencies = False
                continue

            # Check for skill name
            if current_skill and line.startswith('Skill:'):
                current_skill['skill_name'] = line.replace('Skill:', '').strip()
                continue

            # Check for dependencies section
            if line.startswith('Dependencies:'):
                in_dependencies = True
                continue

            # Parse dependency lines
            if in_dependencies and current_skill:
                if line.startswith('* '):
                    # Extract dependency ID - updated pattern to include letters (G, K, etc.)
                    dep_match = re.match(r'\*\s+([T0-9.GKa-z]+):', line)
                    if dep_match:
                        dep_id = dep_match.group(1)
                        current_skill['dependencies'].append(dep_id)
                elif line.strip() == '':
                    # Empty line might end dependencies
                    continue
                elif line.startswith('ID:'):
                    # New skill ID ends dependencies
                    in_dependencies = False

    return all_skills

def check_x_minus_2_rule(skill_id, dep_id, skills):
    """Check if dependency follows X-2 rule"""
    skill_grade = skills[skill_id]['grade']
    dep_grade = parse_grade(dep_id)

    if dep_grade is None:
        return True, f"Cannot parse grade from {dep_id}"

    grade_diff = skill_grade - dep_grade

    if grade_diff < 0:
        return False, f"Forward grade dependency: Grade {skill_grade} depends on Grade {dep_grade}"
    if grade_diff > 2:
        return False, f"Violates X-2 rule: Grade {skill_grade} depends on Grade {dep_grade} (difference: {grade_diff})"

    return True, "OK"

def check_forward_dependency(skill_id, dep_id, skills):
    """Check if dependency is a forward reference within same topic and grade"""
    # Extract topic and grade
    skill_topic = skill_id.split('.')[0]
    dep_topic = dep_id.split('.')[0]

    skill_grade = skills[skill_id]['grade']
    dep_grade = parse_grade(dep_id)

    # Only check within same topic and same grade
    if skill_topic == dep_topic and skill_grade == dep_grade:
        skill_num = skills[skill_id]['skill_number']
        dep_num = parse_skill_number(dep_id)

        if dep_num > skill_num:
            return False, f"Forward dependency: {skill_id} (#{skill_num}) depends on {dep_id} (#{dep_num})"

    return True, "OK"

def main():
    filename = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = read_skills(filename)

    # Filter T20 skills
    t20_skills = {k: v for k, v in skills.items() if k.startswith('T20.')}

    print("=" * 80)
    print("T20 DEPENDENCY VALIDATION REPORT")
    print("=" * 80)
    print()

    print(f"Total T20 skills found: {len(t20_skills)}")
    print()

    # Group by grade
    by_grade = defaultdict(list)
    for skill_id, skill in t20_skills.items():
        by_grade[skill['grade']].append(skill_id)

    print("Skills by grade:")
    for grade in sorted(by_grade.keys()):
        grade_label = f"GK" if grade == 0 else f"G{grade}"
        print(f"  {grade_label}: {len(by_grade[grade])} skills")
    print()

    # Track all issues
    x2_violations = []
    forward_deps = []
    t20_deps = []

    # Check each skill
    print("=" * 80)
    print("DETAILED ANALYSIS")
    print("=" * 80)
    print()

    for grade in sorted(by_grade.keys()):
        grade_label = f"GK" if grade == 0 else f"G{grade}"
        print(f"\n{'='*80}")
        print(f"GRADE {grade_label}")
        print(f"{'='*80}\n")

        grade_skills = sorted(by_grade[grade], key=lambda x: t20_skills[x]['skill_number'])

        for skill_id in grade_skills:
            skill = t20_skills[skill_id]
            print(f"{skill_id}: {skill['skill_name']}")

            if not skill['dependencies']:
                print("  No dependencies")
            else:
                print(f"  Dependencies ({len(skill['dependencies'])}):")

                for dep_id in skill['dependencies']:
                    # Check if it's a T20 dependency
                    is_t20 = dep_id.startswith('T20.')

                    if is_t20:
                        t20_deps.append((skill_id, dep_id))

                        # Check X-2 rule
                        valid_x2, x2_msg = check_x_minus_2_rule(skill_id, dep_id, t20_skills)

                        # Check forward dependency
                        valid_fwd, fwd_msg = check_forward_dependency(skill_id, dep_id, t20_skills)

                        status = "✓"
                        issues = []

                        if not valid_x2:
                            status = "✗"
                            issues.append(x2_msg)
                            x2_violations.append((skill_id, dep_id, x2_msg))

                        if not valid_fwd:
                            status = "✗"
                            issues.append(fwd_msg)
                            forward_deps.append((skill_id, dep_id, fwd_msg))

                        if issues:
                            print(f"    {status} {dep_id} - ISSUES:")
                            for issue in issues:
                                print(f"       {issue}")
                        else:
                            print(f"    {status} {dep_id}")
                    else:
                        # Cross-topic dependency (not checked)
                        print(f"    ○ {dep_id} (cross-topic)")

            print()

    # Summary
    print("\n" + "=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print()

    print(f"Total T20 skills: {len(t20_skills)}")
    print(f"Total T20 intra-topic dependencies: {len(t20_deps)}")
    print()

    if x2_violations:
        print(f"❌ X-2 RULE VIOLATIONS: {len(x2_violations)}")
        for skill_id, dep_id, msg in x2_violations:
            print(f"   {skill_id} -> {dep_id}")
            print(f"      {msg}")
        print()
    else:
        print("✓ No X-2 rule violations")
        print()

    if forward_deps:
        print(f"❌ FORWARD DEPENDENCY VIOLATIONS: {len(forward_deps)}")
        for skill_id, dep_id, msg in forward_deps:
            print(f"   {skill_id} -> {dep_id}")
            print(f"      {msg}")
        print()
    else:
        print("✓ No forward dependencies")
        print()

    # Check the 8 newly added skills
    print("=" * 80)
    print("NEW SKILLS CHECK (8 skills)")
    print("=" * 80)
    print()

    new_skills = [
        'T20.G3.05.01',
        'T20.G4.05.01',
        'T20.G5.01.01',
        'T20.G5.04.01',
        'T20.G6.05.01',
        'T20.G6.05.02',
        'T20.G6.05.03',
        'T20.G7.04.01',
    ]

    # Also check the 3 additional new skills
    additional_new = [
        'T20.G7.05.01',
        'T20.G7.05.02',
        'T20.G7.05.03',
        'T20.G8.05.01'
    ]

    print("Original 8 new skills:")
    for skill_id in new_skills:
        if skill_id in t20_skills:
            skill = t20_skills[skill_id]
            print(f"\n{skill_id}: {skill['skill_name']}")
            if skill['dependencies']:
                print(f"  Dependencies: {len(skill['dependencies'])}")
                for dep_id in skill['dependencies']:
                    is_t20 = dep_id.startswith('T20.')
                    if is_t20:
                        valid_x2, _ = check_x_minus_2_rule(skill_id, dep_id, t20_skills)
                        valid_fwd, _ = check_forward_dependency(skill_id, dep_id, t20_skills)
                        status = "✓" if (valid_x2 and valid_fwd) else "✗"
                        print(f"    {status} {dep_id}")
                    else:
                        print(f"    ○ {dep_id} (cross-topic)")
            else:
                print("  No dependencies")
        else:
            print(f"\n{skill_id}: NOT FOUND")

    print("\n\nAdditional new skills:")
    for skill_id in additional_new:
        if skill_id in t20_skills:
            skill = t20_skills[skill_id]
            print(f"\n{skill_id}: {skill['skill_name']}")
            if skill['dependencies']:
                print(f"  Dependencies: {len(skill['dependencies'])}")
                for dep_id in skill['dependencies']:
                    is_t20 = dep_id.startswith('T20.')
                    if is_t20:
                        valid_x2, _ = check_x_minus_2_rule(skill_id, dep_id, t20_skills)
                        valid_fwd, _ = check_forward_dependency(skill_id, dep_id, t20_skills)
                        status = "✓" if (valid_x2 and valid_fwd) else "✗"
                        print(f"    {status} {dep_id}")
                    else:
                        print(f"    ○ {dep_id} (cross-topic)")
            else:
                print("  No dependencies")
        else:
            print(f"\n{skill_id}: NOT FOUND")

    print("\n" + "=" * 80)
    if not x2_violations and not forward_deps:
        print("✅ ALL T20 DEPENDENCIES ARE VALID!")
    else:
        print("❌ ISSUES FOUND - SEE ABOVE FOR DETAILS")
    print("=" * 80)

if __name__ == '__main__':
    main()
