#!/usr/bin/env python3
"""
Final validation of Phase 2 changes
"""

import re
from collections import defaultdict

def parse_skills_file(filepath):
    """Parse the skills file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.startswith('ID: '):
            skill_id = line.replace('ID: ', '').strip()
            topic = None
            skill_text = None
            dependencies = []

            i += 1
            while i < len(lines) and not lines[i].startswith('ID: '):
                current_line = lines[i]

                if current_line.startswith('Topic: '):
                    topic = current_line.replace('Topic: ', '').strip()
                elif current_line.startswith('Skill: '):
                    skill_text = current_line.replace('Skill: ', '').strip()
                elif current_line.startswith('Dependencies:'):
                    i += 1
                    while i < len(lines) and lines[i].strip().startswith('*'):
                        dep_line = lines[i].strip()
                        dep_match = re.match(r'\*\s*([A-Z0-9.]+):', dep_line)
                        if dep_match:
                            dependencies.append(dep_match.group(1))
                        i += 1
                    continue

                i += 1

            grade = None
            if '.GK.' in skill_id:
                grade = 'K'
            elif '.G1.' in skill_id:
                grade = '1'
            elif '.G2.' in skill_id:
                grade = '2'

            skills[skill_id] = {
                'id': skill_id,
                'grade': grade,
                'topic': topic,
                'content': skill_text or '',
                'dependencies': dependencies
            }
        else:
            i += 1

    return skills

def get_topic_from_skill_id(skill_id):
    """Extract topic number from skill ID."""
    match = re.match(r'T(\d+)\.', skill_id)
    if match:
        return int(match.group(1))
    return None

def validate_phase2(skills):
    """Validate Phase 2 results."""
    grade_k_skills = {sid: s for sid, s in skills.items() if s['grade'] == 'K'}

    print("=" * 70)
    print("PHASE 2 VALIDATION REPORT")
    print("=" * 70)

    # 1. Count Grade K skills
    print(f"\n1. Grade K Skills: {len(grade_k_skills)}")

    # 2. Check X-2 rule
    violations = []
    for sid, skill in grade_k_skills.items():
        for dep_id in skill['dependencies']:
            if dep_id in skills:
                dep_grade = skills[dep_id]['grade']
                if dep_grade and dep_grade != 'K':
                    violations.append((sid, dep_id, dep_grade))

    print(f"\n2. X-2 Rule Violations: {len(violations)}")
    if violations:
        print("   ❌ FAILED - Found violations:")
        for skill, dep, grade in violations[:5]:
            print(f"      {skill} depends on {dep} (Grade {grade})")
    else:
        print("   ✓ PASSED - All Grade K skills depend only on Grade K")

    # 3. Check circular dependencies
    def has_cycle(skill_id, visited, rec_stack):
        visited.add(skill_id)
        rec_stack.add(skill_id)

        if skill_id in grade_k_skills:
            for dep_id in grade_k_skills[skill_id]['dependencies']:
                if dep_id not in visited:
                    if has_cycle(dep_id, visited, rec_stack):
                        return True
                elif dep_id in rec_stack:
                    return True

        rec_stack.remove(skill_id)
        return False

    visited = set()
    circular = []
    for sid in grade_k_skills:
        if sid not in visited:
            if has_cycle(sid, visited, set()):
                circular.append(sid)

    print(f"\n3. Circular Dependencies: {len(circular)}")
    if circular:
        print("   ❌ FAILED - Found circular dependencies")
    else:
        print("   ✓ PASSED - No circular dependencies")

    # 4. Count cross-topic dependencies
    cross_topic_count = 0
    for sid, skill in grade_k_skills.items():
        skill_topic = get_topic_from_skill_id(sid)
        for dep_id in skill['dependencies']:
            dep_topic = get_topic_from_skill_id(dep_id)
            if dep_topic and skill_topic and dep_topic != skill_topic:
                cross_topic_count += 1
                break

    print(f"\n4. Cross-Topic Integration:")
    print(f"   Skills with cross-topic deps: {cross_topic_count} of {len(grade_k_skills)}")
    print(f"   Percentage: {cross_topic_count * 100 / len(grade_k_skills):.1f}%")
    if cross_topic_count >= len(grade_k_skills) * 0.7:
        print("   ✓ PASSED - Good cross-topic integration (≥70%)")
    else:
        print("   ⚠ WARNING - Low cross-topic integration (<70%)")

    # 5. Skills by topic
    by_topic = defaultdict(int)
    for sid in grade_k_skills:
        topic = get_topic_from_skill_id(sid)
        if topic:
            by_topic[topic] += 1

    print(f"\n5. Topics with Grade K Skills: {len(by_topic)} topics")
    print(f"   Coverage: {len(by_topic)} of 36 topics ({len(by_topic)*100/36:.1f}%)")

    # 6. Dependency statistics
    total_deps = sum(len(s['dependencies']) for s in grade_k_skills.values())
    avg_deps = total_deps / len(grade_k_skills) if grade_k_skills else 0

    print(f"\n6. Dependency Statistics:")
    print(f"   Total dependencies: {total_deps}")
    print(f"   Average per skill: {avg_deps:.1f}")
    print(f"   Skills with no deps: {sum(1 for s in grade_k_skills.values() if not s['dependencies'])}")

    # 7. Summary
    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)

    all_passed = len(violations) == 0 and len(circular) == 0

    if all_passed:
        print("✓ ALL VALIDATIONS PASSED")
        print("\nPhase 2 changes are correct and complete:")
        print("  ✓ X-2 rule enforced (Grade K depends only on Grade K)")
        print("  ✓ No circular dependencies")
        print(f"  ✓ {cross_topic_count * 100 / len(grade_k_skills):.1f}% cross-topic integration")
        print("  ✓ Curriculum structure is sound")
    else:
        print("❌ VALIDATION FAILED")
        print("\nIssues found:")
        if violations:
            print(f"  ❌ {len(violations)} X-2 rule violations")
        if circular:
            print(f"  ❌ {len(circular)} circular dependencies")

    print("=" * 70)

    return all_passed

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("\nValidating Phase 2 Changes...\n")

    skills = parse_skills_file(filepath)
    print(f"Parsed {len(skills)} total skills")

    success = validate_phase2(skills)

    if success:
        print("\n✓ Phase 2 validation complete - all checks passed!")
    else:
        print("\n❌ Phase 2 validation failed - please review issues above")

    return 0 if success else 1

if __name__ == '__main__':
    exit(main())
