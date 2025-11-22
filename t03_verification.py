#!/usr/bin/env python3
"""
T03 Skills Verification Script
Extracts all T03 skills and verifies dependencies against X-2 rule and other issues.
"""

import re
from collections import defaultdict

# Read the allskills.md file
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Split into sections by skill ID
skill_pattern = re.compile(r'^ID: (T\d+\.G[K\d]+\.\d+)', re.MULTILINE)
skill_positions = [(m.group(1), m.start()) for m in skill_pattern.finditer(content)]

# Extract T03 skills
t03_skills = {}
for i, (skill_id, start_pos) in enumerate(skill_positions):
    if not skill_id.startswith('T03.'):
        continue

    # Find end position (next skill or end of file)
    end_pos = skill_positions[i + 1][1] if i + 1 < len(skill_positions) else len(content)
    skill_text = content[start_pos:end_pos]

    # Extract skill title
    title_match = re.search(r'^Skill: (.+)$', skill_text, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "UNKNOWN"

    # Extract dependencies
    deps = []
    in_deps = False
    for line in skill_text.split('\n'):
        if line.strip() == 'Dependencies:':
            in_deps = True
            continue
        if in_deps:
            if line.strip() == '' or line.startswith('ID:') or line.startswith('Topic:'):
                break
            dep_match = re.match(r'\* (T\d+\.G[K\d]+\.\d+(?:\.\d+)?): (.+)', line)
            if dep_match:
                deps.append((dep_match.group(1), dep_match.group(2)))

    t03_skills[skill_id] = {
        'title': title,
        'dependencies': deps
    }

# Helper functions
def get_grade_level(skill_id):
    """Extract grade level from skill ID"""
    match = re.match(r'T\d+\.(G[K\d]+)', skill_id)
    if not match:
        return None
    grade = match.group(1)
    if grade == 'GK':
        return 0
    return int(grade[1:])

def check_x_minus_2_violation(skill_id, dep_id):
    """Check if dependency violates X-2 rule"""
    skill_grade = get_grade_level(skill_id)
    dep_grade = get_grade_level(dep_id)

    if skill_grade is None or dep_grade is None:
        return None

    # X-2 rule: Grade X skill cannot depend on Grade (X-3) or earlier
    # Grade 3+ cannot have GK deps
    # Grade 4+ cannot have G1 deps
    # Grade 5+ cannot have G2 deps

    violations = []
    if skill_grade >= 3 and dep_grade == 0:
        violations.append(f"Grade {skill_grade} skill has Kindergarten dependency")
    if skill_grade >= 4 and dep_grade == 1:
        violations.append(f"Grade {skill_grade} skill has Grade 1 dependency")
    if skill_grade >= 5 and dep_grade == 2:
        violations.append(f"Grade {skill_grade} skill has Grade 2 dependency")

    return violations if violations else None

# Analysis
print("=" * 80)
print("T03 SKILLS VERIFICATION REPORT")
print("=" * 80)
print(f"\nTotal T03 skills found: {len(t03_skills)}")
print("\n" + "=" * 80)

# List all skills
print("\nALL T03 SKILLS:")
print("-" * 80)
for skill_id in sorted(t03_skills.keys()):
    skill = t03_skills[skill_id]
    grade = get_grade_level(skill_id)
    grade_str = f"GK" if grade == 0 else f"G{grade}"
    print(f"{skill_id} [{grade_str}]: {skill['title']}")
    if skill['dependencies']:
        for dep_id, dep_title in skill['dependencies']:
            dep_grade = get_grade_level(dep_id)
            dep_grade_str = f"GK" if dep_grade == 0 else f"G{dep_grade}" if dep_grade is not None else "??"
            print(f"  -> {dep_id} [{dep_grade_str}]: {dep_title}")
    else:
        print(f"  -> (no dependencies)")

# Check for X-2 violations
print("\n" + "=" * 80)
print("X-2 RULE VIOLATIONS:")
print("-" * 80)

violations_found = []
for skill_id in sorted(t03_skills.keys()):
    skill = t03_skills[skill_id]
    skill_grade = get_grade_level(skill_id)

    for dep_id, dep_title in skill['dependencies']:
        violations = check_x_minus_2_violation(skill_id, dep_id)
        if violations:
            for violation in violations:
                violations_found.append((skill_id, dep_id, violation, skill['title'], dep_title))

if violations_found:
    for skill_id, dep_id, violation, skill_title, dep_title in violations_found:
        print(f"\n{skill_id}: {skill_title}")
        print(f"  -> VIOLATION: {violation}")
        print(f"  -> Problematic dependency: {dep_id}: {dep_title}")
else:
    print("\nNo X-2 rule violations found!")

# Check for cross-topic dependencies that might be illogical
print("\n" + "=" * 80)
print("CROSS-TOPIC DEPENDENCY ANALYSIS:")
print("-" * 80)

cross_topic_deps = defaultdict(list)
for skill_id in sorted(t03_skills.keys()):
    skill = t03_skills[skill_id]
    for dep_id, dep_title in skill['dependencies']:
        dep_topic = dep_id.split('.')[0]
        if dep_topic != 'T03':
            cross_topic_deps[dep_topic].append((skill_id, dep_id, skill['title'], dep_title))

if cross_topic_deps:
    for topic in sorted(cross_topic_deps.keys()):
        print(f"\nDependencies on {topic}:")
        for skill_id, dep_id, skill_title, dep_title in cross_topic_deps[topic]:
            print(f"  {skill_id}: {skill_title}")
            print(f"    -> {dep_id}: {dep_title}")
else:
    print("\nAll dependencies are within T03 topic.")

# Check for potential circular dependencies
print("\n" + "=" * 80)
print("POTENTIAL CIRCULAR DEPENDENCY CHECK:")
print("-" * 80)

def has_circular_dependency(skill_id, dep_id, visited=None):
    """Check if there's a circular dependency path"""
    if visited is None:
        visited = set()

    if skill_id == dep_id:
        return True

    if dep_id in visited:
        return False

    visited.add(dep_id)

    if dep_id in t03_skills:
        for next_dep_id, _ in t03_skills[dep_id]['dependencies']:
            if has_circular_dependency(skill_id, next_dep_id, visited.copy()):
                return True

    return False

circular_found = []
for skill_id in sorted(t03_skills.keys()):
    skill = t03_skills[skill_id]
    for dep_id, dep_title in skill['dependencies']:
        if dep_id.startswith('T03.') and has_circular_dependency(skill_id, dep_id):
            circular_found.append((skill_id, dep_id, skill['title'], dep_title))

if circular_found:
    for skill_id, dep_id, skill_title, dep_title in circular_found:
        print(f"\nPossible circular dependency:")
        print(f"  {skill_id}: {skill_title}")
        print(f"  -> {dep_id}: {dep_title}")
else:
    print("\nNo circular dependencies detected.")

# Summary of skills by status
print("\n" + "=" * 80)
print("SKILLS STATUS SUMMARY:")
print("-" * 80)

violation_skill_ids = set(v[0] for v in violations_found)
perfect_skills = [sid for sid in sorted(t03_skills.keys()) if sid not in violation_skill_ids]

print(f"\nSkills in PERFECT condition ({len(perfect_skills)}):")
for skill_id in perfect_skills:
    print(f"  {skill_id}: {t03_skills[skill_id]['title']}")

if violation_skill_ids:
    print(f"\nSkills needing FIXES ({len(violation_skill_ids)}):")
    for skill_id in sorted(violation_skill_ids):
        print(f"  {skill_id}: {t03_skills[skill_id]['title']}")

# Final summary
print("\n" + "=" * 80)
print("FINAL SUMMARY:")
print("-" * 80)
print(f"Total T03 skills verified: {len(t03_skills)}")
print(f"Skills in perfect condition: {len(perfect_skills)}")
print(f"Skills needing fixes: {len(violation_skill_ids)}")
print(f"X-2 rule violations: {len(violations_found)}")
print(f"Circular dependencies: {len(circular_found)}")
print("=" * 80)
