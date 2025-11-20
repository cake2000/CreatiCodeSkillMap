#!/usr/bin/env python3
"""List G7 skills that were not changed."""

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

g7_ids = [sid for sid in backup_skills.keys() if '.G7.' in sid]

unchanged = []
for skill_id in sorted(g7_ids):
    if skill_id not in backup_skills or skill_id not in fixed_skills:
        continue

    before_deps = set(backup_skills[skill_id]['dependencies'])
    after_deps = set(fixed_skills[skill_id]['dependencies'])

    if before_deps == after_deps:
        unchanged.append(skill_id)

print("UNCHANGED G7 SKILLS (No issues found)")
print("=" * 80)
print(f"Total: {len(unchanged)} skills")
print()

for skill_id in unchanged:
    skill = backup_skills[skill_id]
    print(f"{skill_id}: {skill['skill']}")
    print(f"  Dependencies ({len(skill['dependencies'])}): {', '.join(skill['dependencies'])}")
    print()
