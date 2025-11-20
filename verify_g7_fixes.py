#!/usr/bin/env python3
"""Verify G7 fixes by comparing before and after."""

import re

BACKUP_PATH = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md.backup_g7_20251120_124024"
FIXED_PATH = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"

def parse_skills(content):
    """Parse skills from content."""
    skills = {}
    current_skill = None
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.startswith('ID: '):
            skill_id = line[4:].strip()
            current_skill = {
                'id': skill_id,
                'dependencies': []
            }
            skills[skill_id] = current_skill
            i += 1
            continue

        if current_skill and line.startswith('Dependencies:'):
            i += 1
            while i < len(lines) and lines[i].startswith('* '):
                match = re.match(r'\* ([^:]+):', lines[i])
                if match:
                    current_skill['dependencies'].append(match.group(1))
                i += 1
            continue

        i += 1

    return skills

# Load both versions
with open(BACKUP_PATH) as f:
    backup_content = f.read()

with open(FIXED_PATH) as f:
    fixed_content = f.read()

backup_skills = parse_skills(backup_content)
fixed_skills = parse_skills(fixed_content)

# Find G7 skills
g7_ids = [sid for sid in backup_skills.keys() if '.G7.' in sid]

print("G7 FIXES VERIFICATION REPORT")
print("=" * 80)
print()

# Track changes
total_removed = 0
total_added = 0
skills_with_removals = 0
skills_with_additions = 0
unchanged_skills = 0

changes_by_type = {
    'removed': [],
    'added': [],
    'both': []
}

for skill_id in sorted(g7_ids):
    if skill_id not in backup_skills or skill_id not in fixed_skills:
        continue

    before_deps = set(backup_skills[skill_id]['dependencies'])
    after_deps = set(fixed_skills[skill_id]['dependencies'])

    removed = before_deps - after_deps
    added = after_deps - before_deps

    if removed:
        total_removed += len(removed)
        skills_with_removals += 1

    if added:
        total_added += len(added)
        skills_with_additions += 1

    if not removed and not added:
        unchanged_skills += 1

    if removed and added:
        changes_by_type['both'].append(skill_id)
    elif removed:
        changes_by_type['removed'].append(skill_id)
    elif added:
        changes_by_type['added'].append(skill_id)

print("SUMMARY STATISTICS:")
print(f"  Total G7 skills: {len(g7_ids)}")
print(f"  Skills with removed dependencies: {skills_with_removals}")
print(f"  Skills with added dependencies: {skills_with_additions}")
print(f"  Skills with both changes: {len(changes_by_type['both'])}")
print(f"  Skills with only removals: {len(changes_by_type['removed'])}")
print(f"  Skills with only additions: {len(changes_by_type['added'])}")
print(f"  Unchanged skills: {unchanged_skills}")
print()
print(f"  Total dependencies removed: {total_removed}")
print(f"  Total dependencies added: {total_added}")
print(f"  Net change: {total_added - total_removed}")
print()

# Dependency count comparison
before_total_deps = sum(len(backup_skills[sid]['dependencies']) for sid in g7_ids if sid in backup_skills)
after_total_deps = sum(len(fixed_skills[sid]['dependencies']) for sid in g7_ids if sid in fixed_skills)
avg_before = before_total_deps / len(g7_ids)
avg_after = after_total_deps / len(g7_ids)

print("DEPENDENCY COUNT ANALYSIS:")
print(f"  Before: {before_total_deps} total deps, avg {avg_before:.2f} per skill")
print(f"  After:  {after_total_deps} total deps, avg {avg_after:.2f} per skill")
print(f"  Reduction: {before_total_deps - after_total_deps} dependencies")
print()

# Most common additions
added_deps = {}
for skill_id in g7_ids:
    if skill_id not in backup_skills or skill_id not in fixed_skills:
        continue
    before_deps = set(backup_skills[skill_id]['dependencies'])
    after_deps = set(fixed_skills[skill_id]['dependencies'])
    added = after_deps - before_deps
    for dep in added:
        added_deps[dep] = added_deps.get(dep, 0) + 1

if added_deps:
    print("MOST COMMON ADDED DEPENDENCIES:")
    for dep, count in sorted(added_deps.items(), key=lambda x: -x[1])[:10]:
        print(f"  {dep}: {count} times")
    print()

# Examples of skills with both changes
if changes_by_type['both']:
    print("EXAMPLES OF SKILLS WITH BOTH ADDITIONS AND REMOVALS:")
    for skill_id in changes_by_type['both'][:5]:
        before_deps = sorted(backup_skills[skill_id]['dependencies'])
        after_deps = sorted(fixed_skills[skill_id]['dependencies'])
        removed = set(before_deps) - set(after_deps)
        added = set(after_deps) - set(before_deps)

        print(f"\n  {skill_id}:")
        print(f"    Removed: {', '.join(sorted(removed))}")
        print(f"    Added: {', '.join(sorted(added))}")
        print(f"    Before count: {len(before_deps)}, After count: {len(after_deps)}")

print()
print("=" * 80)
print("VERIFICATION COMPLETE")
print("=" * 80)
