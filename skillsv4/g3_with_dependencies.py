#!/usr/bin/env python3
"""
Extract all G3 skills and add dependencies.
Target: ~3.12 dependencies per skill (145 skills total)
"""

import re

def get_dependencies(skill_id, skill_name, description):
    """Return list of dependency IDs based on skill analysis"""
    deps = []

    # Parse skill components
    topic = skill_id.split('.')[0]
    skill_num = skill_id.split('.')[-1]

    # ===== GATEWAY SKILLS (Foundation skills that unlock everything) =====

    if skill_id == 'T06.G3.01':  # Events - First gateway skill
        deps = [
            'T01.K.01',  # Follow 2-step sequence
            'T01.K.02',  # Order 3 picture cards
            'T01.G1.01', # Complete 4-step sequence
            'T01.G2.01', # Plan 5-step sequence
        ]

    elif skill_id == 'T07.G3.01':  # Loops - Second gateway skill
        deps = [
            'T06.G3.01', # Events foundation
            'T04.K.01',  # Match identical patterns
            'T04.G1.01', # Recognize repeating pattern unit
            'T04.G2.01', # Identify pattern unit count
            'T01.G2.05', # Pattern concepts in algorithms
        ]

    elif skill_id == 'T08.G3.01':  # Conditionals - Third gateway skill
        deps = [
            'T06.G3.01', # Events foundation
            'T07.G3.01', # Loops foundation
            'T05.K.01',  # Sort by one attribute
            'T05.G1.02', # Choose path based on condition
            'T05.G2.02', # If-then reasoning
        ]

    elif skill_id == 'T09.G3.01':  # Variables - Fourth gateway skill (MOST CRITICAL)
        deps = [
            'T06.G3.01', # Events foundation
            'T07.G3.01', # Loops foundation
            'T08.G3.01', # Conditionals foundation
            'T03.K.01',  # Count objects
            'T03.G1.01', # Count to higher numbers
            'T03.G2.01', # Track changing quantities
        ]

    # ===== T01: EVERYDAY ALGORITHMS (15 skills) =====
    elif topic == 'T01':
        if skill_num in ['01', '02']:  # Early sequence skills
            deps = ['T06.G3.01', 'T01.G2.01', 'T01.G2.02']
        elif skill_num in ['03', '04']:  # Identifying repeated blocks
            deps = ['T06.G3.01', 'T04.G2.01', 'T04.G2.02', 'T01.G2.03']
        elif skill_num in ['05', '06', '07']:  # Using loops
            deps = ['T06.G3.01', 'T07.G3.01', 'T04.G3.01', 'T01.G3.04']
        elif skill_num in ['08', '09']:  # Complex sequencing
            deps = ['T06.G3.01', 'T07.G3.01', 'T01.G3.05', 'T01.G3.06']
        elif skill_num in ['10', '11']:  # Conditional algorithms
            deps = ['T06.G3.01', 'T07.G3.01', 'T08.G3.01', 'T01.G3.07']
        elif skill_num in ['12', '13']:  # Decomposition
            deps = ['T06.G3.01', 'T07.G3.01', 'T08.G3.01', 'T01.G3.09', 'T14.G3.01']
        else:  # 14, 15 - Advanced
            deps = ['T06.G3.01', 'T07.G3.01', 'T08.G3.01', 'T09.G3.01', 'T01.G3.12']

    # ===== T02: DATA COLLECTION (6 skills) =====
    elif topic == 'T02':
        if skill_num == '01':
            deps = ['T02.G2.01', 'T02.G2.02', 'T03.G2.01']
        elif skill_num == '02':
            deps = ['T02.G3.01', 'T03.G2.02', 'T05.G2.01']
        elif skill_num == '03':
            deps = ['T02.G3.01', 'T02.G3.02', 'T03.G2.03']
        elif skill_num == '04':
            deps = ['T02.G3.02', 'T02.G3.03', 'T05.G2.03']
        elif skill_num == '05':
            deps = ['T02.G3.03', 'T02.G3.04', 'T03.G3.01', 'T05.G3.01']
        else:  # 06
            deps = ['T02.G3.04', 'T02.G3.05', 'T05.G3.02', 'T08.G3.01']

    # ===== T03: NUMERIC DATA (6 skills) =====
    elif topic == 'T03':
        if skill_num == '01':
            deps = ['T03.G2.01', 'T03.G2.02', 'T06.G3.01']
        elif skill_num == '02':
            deps = ['T03.G3.01', 'T07.G3.01', 'T03.G2.03']
        elif skill_num == '03':
            deps = ['T03.G3.01', 'T03.G3.02', 'T09.G3.01']
        elif skill_num == '04':
            deps = ['T03.G3.02', 'T03.G3.03', 'T09.G3.01', 'T07.G3.01']
        elif skill_num == '05':
            deps = ['T03.G3.03', 'T03.G3.04', 'T09.G3.01', 'T08.G3.01']
        else:  # 06
            deps = ['T03.G3.04', 'T03.G3.05', 'T09.G3.01', 'T02.G3.05']

    # ===== T04: PATTERNS (6 skills) =====
    elif topic == 'T04':
        if skill_num == '01':
            deps = ['T04.G2.01', 'T04.G2.02', 'T07.G3.01']
        elif skill_num == '02':
            deps = ['T04.G3.01', 'T07.G3.01', 'T04.G2.03']
        elif skill_num == '03':
            deps = ['T04.G3.01', 'T04.G3.02', 'T07.G3.01', 'T03.G3.02']
        elif skill_num == '04':
            deps = ['T04.G3.02', 'T04.G3.03', 'T07.G3.01', 'T09.G3.01']
        elif skill_num == '05':
            deps = ['T04.G3.03', 'T04.G3.04', 'T08.G3.01', 'T07.G3.01']
        else:  # 06
            deps = ['T04.G3.04', 'T04.G3.05', 'T09.G3.01', 'T07.G3.01']

    # ===== T05: SORTING & LOGIC (5 skills) =====
    elif topic == 'T05':
        if skill_num == '01':
            deps = ['T05.G2.01', 'T05.G2.02', 'T08.G3.01']
        elif skill_num == '02':
            deps = ['T05.G3.01', 'T08.G3.01', 'T05.G2.03']
        elif skill_num == '03':
            deps = ['T05.G3.01', 'T05.G3.02', 'T08.G3.01', 'T07.G3.01']
        elif skill_num == '04':
            deps = ['T05.G3.02', 'T05.G3.03', 'T08.G3.01', 'T09.G3.01']
        else:  # 05
            deps = ['T05.G3.03', 'T05.G3.04', 'T08.G3.01', 'T07.G3.01']

    # ===== T06: EVENTS (8 skills) =====
    elif topic == 'T06':
        if skill_num == '02':
            deps = ['T06.G3.01', 'T06.G2.02', 'T07.G3.01']
        elif skill_num == '03':
            deps = ['T06.G3.01', 'T06.G3.02', 'T06.G2.03']
        elif skill_num == '04':
            deps = ['T06.G3.01', 'T06.G3.02', 'T06.G3.03', 'T08.G3.01']
        elif skill_num == '05':
            deps = ['T06.G3.01', 'T06.G3.03', 'T06.G3.04', 'T07.G3.01']
        elif skill_num == '06':
            deps = ['T06.G3.04', 'T06.G3.05', 'T08.G3.01', 'T09.G3.01']
        elif skill_num == '07':
            deps = ['T06.G3.05', 'T06.G3.06', 'T09.G3.01', 'T07.G3.01']
        else:  # 08
            deps = ['T06.G3.06', 'T06.G3.07', 'T08.G3.01', 'T09.G3.01']

    # ===== T07: LOOPS (5 skills) =====
    elif topic == 'T07':
        if skill_num == '02':
            deps = ['T07.G3.01', 'T04.G3.02', 'T07.G2.02']
        elif skill_num == '03':
            deps = ['T07.G3.01', 'T07.G3.02', 'T08.G3.01', 'T09.G3.01']
        elif skill_num == '04':
            deps = ['T07.G3.02', 'T07.G3.03', 'T08.G3.01', 'T09.G3.01']
        else:  # 05
            deps = ['T07.G3.03', 'T07.G3.04', 'T08.G3.01', 'T09.G3.01']

    # ===== T08: CONDITIONALS (5 skills) =====
    elif topic == 'T08':
        if skill_num == '02':
            deps = ['T08.G3.01', 'T05.G3.02', 'T08.G2.02']
        elif skill_num == '03':
            deps = ['T08.G3.01', 'T08.G3.02', 'T07.G3.01', 'T09.G3.01']
        elif skill_num == '04':
            deps = ['T08.G3.02', 'T08.G3.03', 'T07.G3.01', 'T09.G3.01']
        else:  # 05
            deps = ['T08.G3.03', 'T08.G3.04', 'T09.G3.01', 'T07.G3.02']

    # ===== T09: VARIABLES (4 skills) =====
    elif topic == 'T09':
        if skill_num == '02':
            deps = ['T09.G3.01', 'T03.G3.03', 'T07.G3.01', 'T08.G3.01']
        elif skill_num == '03':
            deps = ['T09.G3.01', 'T09.G3.02', 'T07.G3.02', 'T08.G3.02']
        else:  # 04
            deps = ['T09.G3.02', 'T09.G3.03', 'T07.G3.03', 'T08.G3.03']

    # ===== T10: MESSAGES (3 skills) =====
    elif topic == 'T10':
        if skill_num == '01':
            deps = ['T06.G3.01', 'T06.G3.03', 'T07.G3.01', 'T10.G2.01']
        elif skill_num == '02':
            deps = ['T10.G3.01', 'T08.G3.01', 'T07.G3.02', 'T06.G3.04']
        else:  # 03
            deps = ['T10.G3.01', 'T10.G3.02', 'T09.G3.01', 'T08.G3.02']

    # ===== T11: CUSTOM BLOCKS (4 skills) =====
    elif topic == 'T11':
        if skill_num == '01':
            deps = ['T06.G3.01', 'T07.G3.01', 'T01.G3.12', 'T11.G2.01']
        elif skill_num == '02':
            deps = ['T11.G3.01', 'T08.G3.01', 'T07.G3.02']
        elif skill_num == '03':
            deps = ['T11.G3.01', 'T11.G3.02', 'T09.G3.01', 'T08.G3.02']
        else:  # 04
            deps = ['T11.G3.02', 'T11.G3.03', 'T09.G3.02', 'T07.G3.03']

    # ===== T12: CLONES (4 skills) =====
    elif topic == 'T12':
        if skill_num == '01':
            deps = ['T06.G3.01', 'T07.G3.01', 'T09.G3.01', 'T12.G2.01']
        elif skill_num == '02':
            deps = ['T12.G3.01', 'T08.G3.01', 'T09.G3.02']
        elif skill_num == '03':
            deps = ['T12.G3.01', 'T12.G3.02', 'T07.G3.02', 'T09.G3.02']
        else:  # 04
            deps = ['T12.G3.02', 'T12.G3.03', 'T08.G3.02', 'T10.G3.01']

    # ===== T14: DEBUGGING (10 skills) =====
    elif topic == 'T14':
        if skill_num == '01':
            deps = ['T06.G3.01', 'T07.G3.01', 'T14.G2.01']
        elif skill_num == '02':
            deps = ['T14.G3.01', 'T07.G3.01', 'T14.G2.02']
        elif skill_num == '03':
            deps = ['T14.G3.01', 'T14.G3.02', 'T08.G3.01']
        elif skill_num == '04':
            deps = ['T14.G3.02', 'T14.G3.03', 'T09.G3.01']
        elif skill_num == '05':
            deps = ['T14.G3.03', 'T14.G3.04', 'T07.G3.02', 'T08.G3.02']
        elif skill_num == '06':
            deps = ['T14.G3.04', 'T14.G3.05', 'T09.G3.02', 'T06.G3.05']
        elif skill_num == '07':
            deps = ['T14.G3.05', 'T14.G3.06', 'T10.G3.01', 'T11.G3.01']
        elif skill_num == '08':
            deps = ['T14.G3.06', 'T14.G3.07', 'T12.G3.01', 'T08.G3.03']
        elif skill_num == '09':
            deps = ['T14.G3.07', 'T14.G3.08', 'T09.G3.03', 'T07.G3.03']
        else:  # 10
            deps = ['T14.G3.08', 'T14.G3.09', 'T11.G3.02', 'T08.G3.04']

    # ===== T15: DESIGN & PLANNING (9 skills) =====
    elif topic == 'T15':
        if skill_num == '01':
            deps = ['T06.G3.01', 'T01.G3.01', 'T15.G2.01']
        elif skill_num == '02':
            deps = ['T15.G3.01', 'T07.G3.01', 'T01.G3.05']
        elif skill_num == '03':
            deps = ['T15.G3.01', 'T15.G3.02', 'T08.G3.01', 'T01.G3.10']
        elif skill_num == '04':
            deps = ['T15.G3.02', 'T15.G3.03', 'T09.G3.01', 'T14.G3.03']
        elif skill_num == '05':
            deps = ['T15.G3.03', 'T15.G3.04', 'T07.G3.02', 'T08.G3.02']
        elif skill_num == '06':
            deps = ['T15.G3.04', 'T15.G3.05', 'T09.G3.02', 'T10.G3.01']
        elif skill_num == '07':
            deps = ['T15.G3.05', 'T15.G3.06', 'T11.G3.01', 'T12.G3.01']
        elif skill_num == '08':
            deps = ['T15.G3.06', 'T15.G3.07', 'T14.G3.05', 'T09.G3.03']
        else:  # 09
            deps = ['T15.G3.07', 'T15.G3.08', 'T11.G3.02', 'T08.G3.04']

    # ===== T18: COORDINATE SYSTEMS (8 skills) =====
    elif topic == 'T18':
        if skill_num == '01':
            deps = ['T06.G3.01', 'T18.G2.01', 'T03.G2.01']
        elif skill_num == '02':
            deps = ['T18.G3.01', 'T07.G3.01', 'T18.G2.02']
        elif skill_num == '03':
            deps = ['T18.G3.01', 'T18.G3.02', 'T09.G3.01']
        elif skill_num == '04':
            deps = ['T18.G3.02', 'T18.G3.03', 'T08.G3.01', 'T07.G3.01']
        elif skill_num == '05':
            deps = ['T18.G3.03', 'T18.G3.04', 'T09.G3.02', 'T08.G3.02']
        elif skill_num == '06':
            deps = ['T18.G3.04', 'T18.G3.05', 'T07.G3.02', 'T03.G3.04']
        elif skill_num == '07':
            deps = ['T18.G3.05', 'T18.G3.06', 'T08.G3.03', 'T09.G3.03']
        else:  # 08
            deps = ['T18.G3.06', 'T18.G3.07', 'T11.G3.01', 'T07.G3.03']

    # ===== T20: MOTION & DIRECTION (5 skills) =====
    elif topic == 'T20':
        if skill_num == '01':
            deps = ['T06.G3.01', 'T07.G3.01', 'T20.G2.01']
        elif skill_num == '02':
            deps = ['T20.G3.01', 'T08.G3.01', 'T18.G3.02']
        elif skill_num == '03':
            deps = ['T20.G3.01', 'T20.G3.02', 'T09.G3.01', 'T07.G3.02']
        elif skill_num == '04':
            deps = ['T20.G3.02', 'T20.G3.03', 'T08.G3.02', 'T18.G3.04']
        else:  # 05
            deps = ['T20.G3.03', 'T20.G3.04', 'T09.G3.02', 'T07.G3.03']

    # ===== T21: DRAWING (1 skill) =====
    elif topic == 'T21':
        deps = ['T06.G3.01', 'T07.G3.01', 'T20.G3.01', 'T21.G2.01']

    # ===== T22: LOOKS & EFFECTS (1 skill) =====
    elif topic == 'T22':
        deps = ['T06.G3.01', 'T07.G3.01', 'T08.G3.01', 'T22.G2.01']

    # ===== T23: SOUND & MUSIC (3 skills) =====
    elif topic == 'T23':
        if skill_num == '01':
            deps = ['T06.G3.01', 'T07.G3.01', 'T23.G2.01']
        elif skill_num == '02':
            deps = ['T23.G3.01', 'T08.G3.01', 'T06.G3.04']
        else:  # 03
            deps = ['T23.G3.01', 'T23.G3.02', 'T09.G3.01', 'T07.G3.02']

    # ===== T25: SENSING & INPUT (4 skills) =====
    elif topic == 'T25':
        if skill_num == '01':
            deps = ['T06.G3.01', 'T08.G3.01', 'T25.G2.01']
        elif skill_num == '02':
            deps = ['T25.G3.01', 'T09.G3.01', 'T07.G3.01', 'T08.G3.02']
        elif skill_num == '03':
            deps = ['T25.G3.01', 'T25.G3.02', 'T08.G3.03', 'T10.G3.01']
        else:  # 04
            deps = ['T25.G3.02', 'T25.G3.03', 'T09.G3.02', 'T07.G3.02']

    # ===== T26-T36: ADVANCED TOPICS =====
    elif topic in ['T26', 'T27', 'T28', 'T29', 'T30', 'T32', 'T34', 'T35', 'T36']:
        # All advanced topics need gateway skills plus prior work
        base_deps = ['T06.G3.01', 'T07.G3.01', 'T08.G3.01', 'T09.G3.01']

        # Sequential dependency within topic
        if skill_num != '01':
            prev_num = str(int(skill_num) - 1).zfill(2)
            prev_id = f"{topic}.G3.{prev_num}"
            base_deps.insert(0, prev_id)

        # Add G2 foundation for first skill
        if skill_num == '01':
            g2_id = skill_id.replace('.G3.', '.G2.')
            base_deps.insert(0, g2_id)

        # Limit to reasonable number
        deps = base_deps[:4] if len(base_deps) > 4 else base_deps

    # Default fallback
    if not deps:
        deps = ['T06.G3.01', 'T07.G3.01', 'T08.G3.01']

    return deps


def get_skill_name_from_deps(dep_id):
    """Lookup skill name for dependency (placeholder - would need full data)"""
    # This would ideally lookup from the full dataset
    # For now, return placeholder
    return f"Skill {dep_id}"


# Main processing
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r') as f:
    lines = f.readlines()

# Extract all G3 skills
g3_skills = []
i = 0
while i < len(lines):
    line = lines[i]

    if line.startswith('ID: ') and '.G3.' in line:
        skill_id = line.strip().replace('ID: ', '')

        # Collect the skill block
        skill_block = []
        j = i
        while j < len(lines):
            skill_block.append(lines[j])
            # Stop after blank line following description
            if j > i + 3 and lines[j].strip() == '':
                break
            j += 1

        # Parse skill info
        topic = lines[i+1].strip().replace('Topic: ', '') if i+1 < len(lines) else ''
        skill_name = lines[i+2].strip().replace('Skill: ', '') if i+2 < len(lines) else ''
        desc = lines[i+3].strip().replace('Description: ', '') if i+3 < len(lines) else ''

        g3_skills.append({
            'id': skill_id,
            'topic': topic,
            'skill_name': skill_name,
            'description': desc,
            'lines': skill_block
        })

        i = j + 1
    else:
        i += 1

print(f"Extracted {len(g3_skills)} G3 skills")

# Generate output with dependencies
output_lines = []
total_deps = 0

for skill in g3_skills:
    # Get dependencies for this skill
    deps = get_dependencies(skill['id'], skill['skill_name'], skill['description'])
    total_deps += len(deps)

    # Write ID line
    output_lines.append(f"ID: {skill['id']}\n")

    # Write Topic line
    output_lines.append(f"Topic: {skill['topic']}\n")

    # Write Skill line
    output_lines.append(f"Skill: {skill['skill_name']}\n")

    # Write Description line
    output_lines.append(f"Description: {skill['description']}\n")

    # ADD DEPENDENCY SECTION
    output_lines.append("Dependency:\n")
    for dep in deps:
        output_lines.append(f"* {dep}\n")

    # Blank line separator
    output_lines.append("\n")

# Write output
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g3_skills_with_dependencies.md', 'w') as f:
    f.writelines(output_lines)

avg_deps = total_deps / len(g3_skills) if g3_skills else 0
print(f"\nGenerated output file with {len(g3_skills)} skills")
print(f"Total dependencies: {total_deps}")
print(f"Average dependencies per skill: {avg_deps:.2f}")
print(f"Target was: 3.12")
print(f"\nOutput written to: /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g3_skills_with_dependencies.md")
