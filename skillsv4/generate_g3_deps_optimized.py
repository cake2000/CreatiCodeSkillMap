#!/usr/bin/env python3
"""
Generate G3 skills with dependencies targeting exactly 3.12 average
Total: 145 skills
Target: 452 total dependencies (145 * 3.12)
Distribution: 127 skills with 3 deps, 18 skills with 4+ deps
"""

import re

# Skills that get 4+ dependencies (18 total):
FOUR_DEP_SKILLS = {
    # Gateway skills (4)
    'T06.G3.01', 'T07.G3.01', 'T08.G3.01', 'T09.G3.01',
    # Key integration points (14 more)
    'T01.G3.05',  # First loop usage in algorithms
    'T01.G3.10',  # First conditional in algorithms
    'T01.G3.12',  # Decomposition start
    'T10.G3.01',  # Messages (multi-sprite)
    'T11.G3.01',  # Custom blocks
    'T12.G3.01',  # Clones
    'T14.G3.01',  # Debugging start
    'T15.G3.04',  # Design with all concepts
    'T18.G3.03',  # Variables in coordinates
    'T20.G3.03',  # Variables in motion
    'T07.G3.03',  # Complex loops
    'T08.G3.03',  # Complex conditionals
    'T09.G3.02',  # Variable operations
    'T03.G3.03',  # Variables with numeric data
}

def get_dependencies(skill_id):
    """Return dependency list (3 deps for most, 4 for critical skills)"""
    topic = skill_id.split('.')[0]
    skill_num = skill_id.split('.')[-1]
    
    # Check if this gets 4 dependencies
    allow_four = skill_id in FOUR_DEP_SKILLS
    
    # === GATEWAY SKILLS ===
    if skill_id == 'T06.G3.01':
        return ['T01.K.01', 'T01.G1.01', 'T01.G2.01', 'T01.G2.02']
    elif skill_id == 'T07.G3.01':
        return ['T06.G3.01', 'T04.G1.01', 'T04.G2.01', 'T01.G2.05']
    elif skill_id == 'T08.G3.01':
        return ['T06.G3.01', 'T07.G3.01', 'T05.G1.02', 'T05.G2.02']
    elif skill_id == 'T09.G3.01':
        return ['T06.G3.01', 'T07.G3.01', 'T08.G3.01', 'T03.G2.01']
    
    # === T01: EVERYDAY ALGORITHMS ===
    elif topic == 'T01':
        if skill_num in ['01', '02']:
            return ['T06.G3.01', 'T01.G2.01', 'T01.G2.02']
        elif skill_num in ['03', '04']:
            return ['T06.G3.01', 'T04.G2.01', 'T01.G2.03']
        elif skill_id == 'T01.G3.05':  # 4 deps
            return ['T06.G3.01', 'T07.G3.01', 'T04.G3.01', 'T01.G3.04']
        elif skill_num in ['06', '07']:
            return ['T07.G3.01', 'T01.G3.05', 'T04.G3.02']
        elif skill_num in ['08', '09']:
            return ['T07.G3.01', 'T01.G3.06', 'T01.G3.07']
        elif skill_id == 'T01.G3.10':  # 4 deps
            return ['T06.G3.01', 'T07.G3.01', 'T08.G3.01', 'T01.G3.09']
        elif skill_num == '11':
            return ['T08.G3.01', 'T01.G3.10', 'T07.G3.02']
        elif skill_id == 'T01.G3.12':  # 4 deps
            return ['T07.G3.01', 'T08.G3.01', 'T01.G3.11', 'T14.G3.01']
        else:  # 13-15
            return ['T08.G3.01', 'T09.G3.01', 'T01.G3.12']
    
    # === T02: DATA COLLECTION ===
    elif topic == 'T02':
        if skill_num == '01':
            return ['T02.G2.01', 'T02.G2.02', 'T03.G2.01']
        elif skill_num == '02':
            return ['T02.G3.01', 'T03.G2.02', 'T05.G2.01']
        elif skill_num == '03':
            return ['T02.G3.02', 'T03.G2.03', 'T05.G2.02']
        elif skill_num == '04':
            return ['T02.G3.03', 'T05.G2.03', 'T03.G3.01']
        elif skill_num == '05':
            return ['T02.G3.04', 'T03.G3.01', 'T05.G3.01']
        else:  # 06
            return ['T02.G3.05', 'T05.G3.02', 'T08.G3.01']
    
    # === T03: NUMERIC DATA ===
    elif topic == 'T03':
        if skill_num == '01':
            return ['T03.G2.01', 'T03.G2.02', 'T06.G3.01']
        elif skill_num == '02':
            return ['T03.G3.01', 'T07.G3.01', 'T03.G2.03']
        elif skill_id == 'T03.G3.03':  # 4 deps
            return ['T03.G3.02', 'T09.G3.01', 'T07.G3.01', 'T03.G2.04']
        elif skill_num == '04':
            return ['T03.G3.03', 'T09.G3.01', 'T07.G3.02']
        elif skill_num == '05':
            return ['T03.G3.04', 'T09.G3.01', 'T08.G3.01']
        else:  # 06
            return ['T03.G3.05', 'T09.G3.02', 'T02.G3.05']
    
    # === T04: PATTERNS ===
    elif topic == 'T04':
        if skill_num == '01':
            return ['T04.G2.01', 'T04.G2.02', 'T07.G3.01']
        elif skill_num == '02':
            return ['T04.G3.01', 'T07.G3.01', 'T04.G2.03']
        elif skill_num == '03':
            return ['T04.G3.02', 'T07.G3.02', 'T03.G3.02']
        elif skill_num == '04':
            return ['T04.G3.03', 'T07.G3.02', 'T09.G3.01']
        elif skill_num == '05':
            return ['T04.G3.04', 'T08.G3.01', 'T07.G3.02']
        else:  # 06
            return ['T04.G3.05', 'T09.G3.01', 'T07.G3.03']
    
    # === T05: SORTING & LOGIC ===
    elif topic == 'T05':
        if skill_num == '01':
            return ['T05.G2.01', 'T05.G2.02', 'T08.G3.01']
        elif skill_num == '02':
            return ['T05.G3.01', 'T08.G3.01', 'T05.G2.03']
        elif skill_num == '03':
            return ['T05.G3.02', 'T08.G3.02', 'T07.G3.01']
        elif skill_num == '04':
            return ['T05.G3.03', 'T08.G3.02', 'T09.G3.01']
        else:  # 05
            return ['T05.G3.04', 'T08.G3.03', 'T07.G3.02']
    
    # === T06: EVENTS ===
    elif topic == 'T06':
        if skill_num == '02':
            return ['T06.G3.01', 'T06.G2.02', 'T07.G3.01']
        elif skill_num == '03':
            return ['T06.G3.02', 'T06.G2.03', 'T07.G3.01']
        elif skill_num == '04':
            return ['T06.G3.03', 'T08.G3.01', 'T06.G2.04']
        elif skill_num == '05':
            return ['T06.G3.04', 'T07.G3.02', 'T08.G3.01']
        elif skill_num == '06':
            return ['T06.G3.05', 'T08.G3.02', 'T09.G3.01']
        elif skill_num == '07':
            return ['T06.G3.06', 'T09.G3.01', 'T07.G3.02']
        else:  # 08
            return ['T06.G3.07', 'T08.G3.02', 'T09.G3.02']
    
    # === T07: LOOPS ===
    elif topic == 'T07':
        if skill_num == '02':
            return ['T07.G3.01', 'T04.G3.02', 'T07.G2.02']
        elif skill_id == 'T07.G3.03':  # 4 deps
            return ['T07.G3.02', 'T08.G3.01', 'T09.G3.01', 'T04.G3.03']
        elif skill_num == '04':
            return ['T07.G3.03', 'T08.G3.02', 'T09.G3.02']
        else:  # 05
            return ['T07.G3.04', 'T08.G3.03', 'T09.G3.02']
    
    # === T08: CONDITIONALS ===
    elif topic == 'T08':
        if skill_num == '02':
            return ['T08.G3.01', 'T05.G3.02', 'T08.G2.02']
        elif skill_id == 'T08.G3.03':  # 4 deps
            return ['T08.G3.02', 'T07.G3.02', 'T09.G3.01', 'T05.G3.03']
        elif skill_num == '04':
            return ['T08.G3.03', 'T07.G3.03', 'T09.G3.02']
        else:  # 05
            return ['T08.G3.04', 'T09.G3.02', 'T07.G3.03']
    
    # === T09: VARIABLES ===
    elif topic == 'T09':
        if skill_id == 'T09.G3.02':  # 4 deps
            return ['T09.G3.01', 'T03.G3.03', 'T07.G3.02', 'T08.G3.02']
        elif skill_num == '03':
            return ['T09.G3.02', 'T07.G3.03', 'T08.G3.03']
        else:  # 04
            return ['T09.G3.03', 'T07.G3.04', 'T08.G3.04']
    
    # === T10: MESSAGES ===
    elif topic == 'T10':
        if skill_id == 'T10.G3.01':  # 4 deps
            return ['T06.G3.03', 'T07.G3.01', 'T10.G2.01', 'T06.G3.04']
        elif skill_num == '02':
            return ['T10.G3.01', 'T08.G3.01', 'T07.G3.02']
        else:  # 03
            return ['T10.G3.02', 'T09.G3.01', 'T08.G3.02']
    
    # === T11: CUSTOM BLOCKS ===
    elif topic == 'T11':
        if skill_id == 'T11.G3.01':  # 4 deps
            return ['T06.G3.01', 'T07.G3.02', 'T01.G3.12', 'T11.G2.01']
        elif skill_num == '02':
            return ['T11.G3.01', 'T08.G3.02', 'T09.G3.01']
        elif skill_num == '03':
            return ['T11.G3.02', 'T09.G3.02', 'T08.G3.03']
        else:  # 04
            return ['T11.G3.03', 'T09.G3.03', 'T07.G3.04']
    
    # === T12: CLONES ===
    elif topic == 'T12':
        if skill_id == 'T12.G3.01':  # 4 deps
            return ['T06.G3.01', 'T07.G3.02', 'T09.G3.01', 'T12.G2.01']
        elif skill_num == '02':
            return ['T12.G3.01', 'T08.G3.02', 'T09.G3.02']
        elif skill_num == '03':
            return ['T12.G3.02', 'T07.G3.03', 'T09.G3.02']
        else:  # 04
            return ['T12.G3.03', 'T08.G3.03', 'T10.G3.02']
    
    # === T14: DEBUGGING ===
    elif topic == 'T14':
        if skill_id == 'T14.G3.01':  # 4 deps
            return ['T06.G3.01', 'T07.G3.01', 'T14.G2.01', 'T01.G3.05']
        elif skill_num == '02':
            return ['T14.G3.01', 'T07.G3.02', 'T14.G2.02']
        elif skill_num == '03':
            return ['T14.G3.02', 'T08.G3.01', 'T14.G2.03']
        elif skill_num == '04':
            return ['T14.G3.03', 'T09.G3.01', 'T14.G2.04']
        elif skill_num == '05':
            return ['T14.G3.04', 'T07.G3.03', 'T08.G3.02']
        elif skill_num == '06':
            return ['T14.G3.05', 'T09.G3.02', 'T06.G3.05']
        elif skill_num == '07':
            return ['T14.G3.06', 'T10.G3.01', 'T11.G3.01']
        elif skill_num == '08':
            return ['T14.G3.07', 'T12.G3.01', 'T08.G3.03']
        elif skill_num == '09':
            return ['T14.G3.08', 'T09.G3.03', 'T07.G3.04']
        else:  # 10
            return ['T14.G3.09', 'T11.G3.02', 'T08.G3.04']
    
    # === T15: DESIGN & PLANNING ===
    elif topic == 'T15':
        if skill_num == '01':
            return ['T06.G3.01', 'T01.G3.01', 'T15.G2.01']
        elif skill_num == '02':
            return ['T15.G3.01', 'T07.G3.01', 'T01.G3.05']
        elif skill_num == '03':
            return ['T15.G3.02', 'T08.G3.01', 'T01.G3.10']
        elif skill_id == 'T15.G3.04':  # 4 deps
            return ['T15.G3.03', 'T09.G3.01', 'T14.G3.03', 'T07.G3.02']
        elif skill_num == '05':
            return ['T15.G3.04', 'T08.G3.02', 'T07.G3.03']
        elif skill_num == '06':
            return ['T15.G3.05', 'T09.G3.02', 'T10.G3.01']
        elif skill_num == '07':
            return ['T15.G3.06', 'T11.G3.01', 'T12.G3.01']
        elif skill_num == '08':
            return ['T15.G3.07', 'T14.G3.05', 'T09.G3.03']
        else:  # 09
            return ['T15.G3.08', 'T11.G3.02', 'T08.G3.04']
    
    # === T18: COORDINATE SYSTEMS ===
    elif topic == 'T18':
        if skill_num == '01':
            return ['T06.G3.01', 'T18.G2.01', 'T03.G2.01']
        elif skill_num == '02':
            return ['T18.G3.01', 'T07.G3.01', 'T18.G2.02']
        elif skill_id == 'T18.G3.03':  # 4 deps
            return ['T18.G3.02', 'T09.G3.01', 'T07.G3.02', 'T03.G3.03']
        elif skill_num == '04':
            return ['T18.G3.03', 'T08.G3.01', 'T18.G2.04']
        elif skill_num == '05':
            return ['T18.G3.04', 'T09.G3.02', 'T08.G3.02']
        elif skill_num == '06':
            return ['T18.G3.05', 'T07.G3.03', 'T03.G3.04']
        elif skill_num == '07':
            return ['T18.G3.06', 'T08.G3.03', 'T09.G3.03']
        else:  # 08
            return ['T18.G3.07', 'T11.G3.01', 'T07.G3.04']
    
    # === T20: MOTION & DIRECTION ===
    elif topic == 'T20':
        if skill_num == '01':
            return ['T06.G3.01', 'T07.G3.01', 'T20.G2.01']
        elif skill_num == '02':
            return ['T20.G3.01', 'T08.G3.01', 'T18.G3.02']
        elif skill_id == 'T20.G3.03':  # 4 deps
            return ['T20.G3.02', 'T09.G3.01', 'T07.G3.02', 'T18.G3.03']
        elif skill_num == '04':
            return ['T20.G3.03', 'T08.G3.02', 'T18.G3.04']
        else:  # 05
            return ['T20.G3.04', 'T09.G3.02', 'T07.G3.03']
    
    # === T21: DRAWING ===
    elif topic == 'T21':
        return ['T06.G3.01', 'T07.G3.01', 'T20.G3.01']
    
    # === T22: LOOKS & EFFECTS ===
    elif topic == 'T22':
        return ['T06.G3.01', 'T07.G3.01', 'T08.G3.01']
    
    # === T23: SOUND & MUSIC ===
    elif topic == 'T23':
        if skill_num == '01':
            return ['T06.G3.01', 'T07.G3.01', 'T23.G2.01']
        elif skill_num == '02':
            return ['T23.G3.01', 'T08.G3.01', 'T06.G3.04']
        else:  # 03
            return ['T23.G3.02', 'T09.G3.01', 'T07.G3.02']
    
    # === T25: SENSING & INPUT ===
    elif topic == 'T25':
        if skill_num == '01':
            return ['T06.G3.01', 'T08.G3.01', 'T25.G2.01']
        elif skill_num == '02':
            return ['T25.G3.01', 'T09.G3.01', 'T08.G3.02']
        elif skill_num == '03':
            return ['T25.G3.02', 'T08.G3.03', 'T10.G3.01']
        else:  # 04
            return ['T25.G3.03', 'T09.G3.02', 'T07.G3.03']
    
    # === T26-T36: ADVANCED TOPICS ===
    elif topic in ['T26', 'T27', 'T28', 'T29', 'T30', 'T32', 'T34', 'T35', 'T36']:
        g2_id = skill_id.replace('.G3.', '.G2.')
        if skill_num == '01':
            return [g2_id, 'T06.G3.01', 'T07.G3.01']
        else:
            prev_num = str(int(skill_num) - 1).zfill(2)
            prev_id = f"{topic}.G3.{prev_num}"
            return [prev_id, 'T08.G3.01', 'T09.G3.01']
    
    # Fallback
    return ['T06.G3.01', 'T07.G3.01', 'T08.G3.01']


# Main processing
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r') as f:
    lines = f.readlines()

# Extract G3 skills
g3_skills = []
i = 0
while i < len(lines):
    if lines[i].startswith('ID: ') and '.G3.' in lines[i]:
        skill_id = lines[i].strip().replace('ID: ', '')
        topic = lines[i+1].strip().replace('Topic: ', '') if i+1 < len(lines) else ''
        skill_name = lines[i+2].strip().replace('Skill: ', '') if i+2 < len(lines) else ''
        desc = lines[i+3].strip().replace('Description: ', '') if i+3 < len(lines) else ''
        
        g3_skills.append({
            'id': skill_id,
            'topic': topic,
            'skill_name': skill_name,
            'description': desc
        })
        i += 4
    else:
        i += 1

print(f"Extracted {len(g3_skills)} G3 skills")

# Generate output
output_lines = []
total_deps = 0
dep_counts = []

for skill in g3_skills:
    deps = get_dependencies(skill['id'])
    total_deps += len(deps)
    dep_counts.append(len(deps))
    
    output_lines.append(f"ID: {skill['id']}\n")
    output_lines.append(f"Topic: {skill['topic']}\n")
    output_lines.append(f"Skill: {skill['skill_name']}\n")
    output_lines.append(f"Description: {skill['description']}\n")
    output_lines.append("Dependency:\n")
    for dep in deps:
        output_lines.append(f"* {dep}\n")
    output_lines.append("\n")

# Write output
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g3_skills_with_dependencies.md', 'w') as f:
    f.writelines(output_lines)

avg_deps = total_deps / len(g3_skills) if g3_skills else 0

# Statistics
from collections import Counter
dist = Counter(dep_counts)

print(f"\n=== RESULTS ===")
print(f"Total skills: {len(g3_skills)}")
print(f"Total dependencies: {total_deps}")
print(f"Average dependencies per skill: {avg_deps:.2f}")
print(f"Target: 3.12")
print(f"Difference: {avg_deps - 3.12:+.2f}")
print(f"\nDistribution:")
for count in sorted(dist.keys()):
    print(f"  {count} deps: {dist[count]} skills")
print(f"\nOutput: /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g3_skills_with_dependencies.md")
