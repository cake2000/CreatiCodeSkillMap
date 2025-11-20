#!/usr/bin/env python3
"""
Generate fix recommendations for G4 skills
"""

import re
from collections import defaultdict

def parse_allskills(filepath):
    """Parse the allskills.md file and extract all skills."""
    skills = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    entries = re.split(r'\n(?=ID: )', content)

    for entry in entries:
        if not entry.strip():
            continue

        id_match = re.search(r'^ID:\s*(\S+)', entry, re.MULTILINE)
        if not id_match:
            continue

        skill_id = id_match.group(1)
        topic_match = re.search(r'^Topic:\s*(.+)$', entry, re.MULTILINE)
        topic = topic_match.group(1).strip() if topic_match else "Unknown"
        skill_match = re.search(r'^Skill:\s*(.+)$', entry, re.MULTILINE)
        skill_name = skill_match.group(1).strip() if skill_match else "Unknown"

        dependencies = []
        deps_match = re.search(r'^Dependencies:\s*(.+?)(?=^ID:|$)', entry, re.MULTILINE | re.DOTALL)
        if deps_match:
            deps_text = deps_match.group(1)
            dep_ids = re.findall(r'\*\s*(\S+):', deps_text)
            dependencies = dep_ids

        skills[skill_id] = {
            'id': skill_id,
            'topic': topic,
            'skill': skill_name,
            'dependencies': dependencies
        }

    return skills

def get_grade_from_id(skill_id):
    match = re.search(r'\.(G\d+|GK)\.', skill_id)
    if match:
        return match.group(1)
    return None

def get_grade_number(grade):
    if grade == 'GK':
        return 0
    match = re.match(r'G(\d+)', grade)
    if match:
        return int(match.group(1))
    return -1

def get_topic_from_id(skill_id):
    match = re.match(r'(T\d+)\.', skill_id)
    if match:
        return match.group(1)
    return None

def find_intermediate_skills(skill_id, dep_id, skills):
    """Find potential intermediate skills between skill and dependency."""
    skill_topic = get_topic_from_id(skill_id)
    dep_topic = get_topic_from_id(dep_id)
    dep_grade_num = get_grade_number(get_grade_from_id(dep_id))

    intermediates = []

    # Look for skills in same topic with grades between dep and current (G4)
    for sid, s in skills.items():
        s_topic = get_topic_from_id(sid)
        s_grade = get_grade_from_id(sid)

        if s_topic == skill_topic and s_grade:
            s_grade_num = get_grade_number(s_grade)
            # Find skills in G2 or G3 from same topic
            if dep_grade_num < s_grade_num < 4:
                intermediates.append((sid, s_grade))

    return intermediates

def generate_fixes(skills):
    """Generate fix recommendations for G4 skills."""

    g4_skills = {sid: s for sid, s in skills.items() if get_grade_from_id(sid) == 'G4'}

    print("=" * 80)
    print("G4 SKILLS FIX RECOMMENDATIONS")
    print("=" * 80)
    print(f"\nTotal G4 skills: {len(g4_skills)}\n")

    by_topic = defaultdict(list)
    for skill_id, skill in g4_skills.items():
        by_topic[skill['topic']].append(skill)

    fix_count = 0
    no_fix_count = 0

    for topic in sorted(by_topic.keys()):
        topic_skills = sorted(by_topic[topic], key=lambda x: x['id'])

        has_issues = False
        for skill in topic_skills:
            # Check for issues
            has_range_violation = False
            has_other_issues = False

            for dep_id in skill['dependencies']:
                dep_grade = get_grade_from_id(dep_id)
                if dep_grade:
                    dep_grade_num = get_grade_number(dep_grade)
                    if dep_grade_num < 2 and dep_grade_num >= 0:
                        has_range_violation = True
                    elif dep_grade_num > 4:
                        has_other_issues = True

            if has_range_violation or has_other_issues:
                has_issues = True
                break

        if not has_issues:
            continue

        print(f"\n{'=' * 80}")
        print(f"TOPIC: {topic}")
        print('=' * 80)

        for skill in topic_skills:
            range_violations = []
            forward_refs = []

            for dep_id in skill['dependencies']:
                dep_grade = get_grade_from_id(dep_id)
                if dep_grade:
                    dep_grade_num = get_grade_number(dep_grade)
                    if dep_grade_num < 2 and dep_grade_num >= 0:
                        range_violations.append((dep_id, dep_grade))
                    elif dep_grade_num > 4:
                        forward_refs.append((dep_id, dep_grade))

            if not range_violations and not forward_refs:
                continue

            print(f"\n--- {skill['id']}: {skill['skill']}")
            print(f"Current dependencies: {', '.join(skill['dependencies'])}")

            if forward_refs:
                print("\nFORWARD REFERENCES (HIGH PRIORITY):")
                for dep_id, dep_grade in forward_refs:
                    print(f"  - {dep_id} ({dep_grade})")
                print("  FIX: Remove these dependencies or restructure the skill")

            if range_violations:
                print("\nRANGE VIOLATIONS (MEDIUM PRIORITY):")
                for dep_id, dep_grade in range_violations:
                    print(f"  - {dep_id} ({dep_grade}) is too far back")

                    # Find intermediate skills
                    intermediates = find_intermediate_skills(skill['id'], dep_id, skills)

                    if intermediates:
                        print(f"    SUGGESTED FIX: Replace with one of these intermediate skills:")
                        for inter_id, inter_grade in intermediates[:3]:  # Show top 3
                            inter_skill = skills[inter_id]
                            print(f"      - {inter_id} ({inter_grade}): {inter_skill['skill']}")
                    else:
                        print(f"    SUGGESTED FIX: Remove {dep_id} or add intermediate G2/G3 skills from same topic")

            print(f"\nRECOMMENDED NEW DEPENDENCIES:")
            # Build recommended deps
            new_deps = []
            for dep_id in skill['dependencies']:
                dep_grade = get_grade_from_id(dep_id)
                if dep_grade:
                    dep_grade_num = get_grade_number(dep_grade)
                    # Keep deps that are G2, G3, or G4
                    if 2 <= dep_grade_num <= 4:
                        new_deps.append(dep_id)

            if new_deps:
                print(f"  Keep: {', '.join(new_deps)}")
            else:
                print("  (Review needed - need to add appropriate G2-G4 prerequisites)")

            fix_count += 1

    print("\n\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"\nG4 skills requiring fixes: {fix_count}")
    print(f"G4 skills without issues: {len(g4_skills) - fix_count}")

    print("\n" + "=" * 80)
    print("NEXT STEPS")
    print("=" * 80)
    print("\n1. Review all FORWARD REFERENCES (HIGH priority) - these are critical errors")
    print("2. Fix RANGE VIOLATIONS by:")
    print("   - Replacing GK/G1 dependencies with intermediate G2/G3 skills from same topic")
    print("   - Or adding the intermediate skills as dependencies")
    print("3. Verify that all G4 skills have appropriate prerequisites")
    print("4. Consider creating intermediate skills if gaps exist in the progression")

    print("\n" + "=" * 80)
    print("END OF FIX RECOMMENDATIONS")
    print("=" * 80)

if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = parse_allskills(filepath)
    generate_fixes(skills)
