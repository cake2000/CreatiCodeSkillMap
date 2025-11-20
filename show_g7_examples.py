#!/usr/bin/env python3
"""Show before/after examples of G7 fixes."""

import re

BACKUP_PATH = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md.backup_g7_20251120_124024"
FIXED_PATH = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"

def parse_skills(content):
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
                'skill': '',
                'dependencies': []
            }
            skills[skill_id] = current_skill
        elif current_skill and line.startswith('Skill: '):
            current_skill['skill'] = line[7:].strip()
        elif current_skill and line.startswith('Dependencies:'):
            i += 1
            while i < len(lines) and lines[i].startswith('* '):
                match = re.match(r'\* ([^:]+):', lines[i])
                if match:
                    current_skill['dependencies'].append(match.group(1))
                i += 1
            continue

        i += 1

    return skills

with open(BACKUP_PATH) as f:
    backup_skills = parse_skills(f.read())

with open(FIXED_PATH) as f:
    fixed_skills = parse_skills(f.read())

# Examples to show
examples = [
    'T01.G7.01',  # Big reduction
    'T02.G7.02',  # Add + remove
    'T19.G7.01',  # Network topic
    'T31.G7.02',  # Complex changes
]

print("=" * 80)
print("G7 FIXES - BEFORE/AFTER EXAMPLES")
print("=" * 80)
print()

for skill_id in examples:
    if skill_id not in backup_skills or skill_id not in fixed_skills:
        continue

    before = backup_skills[skill_id]
    after = fixed_skills[skill_id]

    before_deps = set(before['dependencies'])
    after_deps = set(after['dependencies'])

    removed = before_deps - after_deps
    added = after_deps - before_deps

    print(f"SKILL: {skill_id}")
    print(f"TITLE: {before['skill']}")
    print()
    print(f"BEFORE ({len(before_deps)} dependencies):")
    for dep in sorted(before_deps):
        marker = "  ❌" if dep in removed else "    "
        print(f"{marker} {dep}")
    print()
    print(f"AFTER ({len(after_deps)} dependencies):")
    for dep in sorted(after_deps):
        marker = "  ✓" if dep in added else "   "
        print(f"{marker} {dep}")
    print()

    if removed:
        print(f"REMOVED ({len(removed)}): {', '.join(sorted(removed))}")
    if added:
        print(f"ADDED ({len(added)}): {', '.join(sorted(added))}")

    print(f"CHANGE: {len(before_deps)} → {len(after_deps)} dependencies")
    print("=" * 80)
    print()

