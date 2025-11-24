#!/usr/bin/env python3
"""
Apply approved cross-topic dependencies to allskills.md
"""

import re
from collections import defaultdict

# Define which dependencies to add (manually curated from suggestions)
APPROVED_ADDITIONS = {
    # T01 - Everyday Algorithms
    'T01.GK.07': ['T04.GK.01'],  # Find pattern that repeats → needs pattern foundation
    'T01.GK.08': [],  # Already has T01.GK.07 which has patterns; don't add T04.GK.01 (transitive), but add T09.GK.01 for counting

    # T02 - Algorithm Diagrams
    # T02.GK.02 already transitively gets T01.GK.01 through T02.GK.01
    # T02.GK.04 already transitively gets T01.GK.01 through T02.GK.03 → T02.GK.02 → T02.GK.01

    # T03 - Problem Decomposition
    # T03.GK.04 already gets T01.GK.01 transitively through T03.GK.03
    # T03.GK.05 already gets T01.GK.01 transitively through T03.GK.03

    # T04 - Algorithm Patterns
    'T04.GK.02': [],  # Pattern extension - doesn't need T01.GK.01 (patterns ≠ sequences)

    # T06 - Events & Sequences
    # T06.GK.02 already gets T01.GK.01 transitively through T06.GK.01
    # T06.GK.03 already gets T01.GK.01 transitively through T06.GK.02 → T06.GK.01

    # T08 - Conditions & Logic
    'T08.GK.02': [],  # Conditional doesn't need sequencing directly

    # T10 - Lists & Tables
    'T10.GK.02': ['T09.GK.01'],  # Counting items → needs counting foundation
    'T10.GK.05': [],  # Already has T01.GK.03 (transitive to T01.GK.01)
    'T10.GK.08': ['T09.GK.01'],  # Finding and counting marked items

    # T13 - Testing/Debugging
    # T13.GK.03 already gets T01.GK.01 transitively through T01.GK.03

    # T18 - 3D Worlds & Games
    'T18.GK.01': [],  # Exploring 3D shapes doesn't require counting prerequisite

    # T20 - Algorithmic Art
    'T20.GK.04': [],  # Already has T04.GK.01; sequencing is transitive if needed

    # T21 - AI Media
    'T21.GK.01': ['T04.GK.01'],  # Identifying AI pictures requires pattern recognition
    'T21.GK.03': ['T10.GK.01'],  # Picking helper that talks back = sorting/categorizing

    # T23 - AI Perception
    'T23.GK.02': ['T03.GK.01'],  # Pointing to device parts → identifying parts of whole

    # T25 - Data Representation
    'T25.GK.02': ['T09.GK.01'],  # Matching quantities to symbols → needs counting

    # T26 - Data Collection & Logging
    'T26.GK.02': ['T04.GK.01'],  # Already has T01.GK.07, add T04.GK.01 for pattern foundation

    # T27 - Data Analysis
    'T27.GK.02': ['T10.GK.02', 'T09.GK.01'],  # Comparing groups → needs counting from groups
    'T27.GK.03': ['T10.GK.06'],  # Reading chart → needs table foundation

    # T29 - Text Data & NLP
    'T29.GK.01': ['T10.GK.01'],  # Sorting text vs pictures → needs sorting foundation
    'T29.GK.02': [],  # Counting letters - maybe, but not critical

    # T30 - Devices & Hardware
    'T30.GK.03': ['T10.GK.01'],  # Sorting input vs output → needs sorting foundation

    # T31 - Internet & Cloud
    'T31.GK.01': ['T10.GK.01', 'T30.GK.01'],  # Recognizing connected devices → sorting + devices

    # T32 - Cybersecurity
    'T32.GK.01': ['T10.GK.01'],  # Sorting safe vs unsafe → needs sorting foundation
    'T32.GK.03': [],  # Password concepts don't need counting directly
    'T32.GK.04': ['T10.GK.01'],  # Sorting online vs offline → needs sorting foundation

    # T33 - Connected Services
    'T33.GK.01': ['T30.GK.01'],  # Apps connecting to internet → needs device foundation

    # T35 - Impacts & Ethics
    'T35.GK.03': ['T10.GK.01'],  # Sorting kind vs unkind → needs sorting foundation
}

def parse_skill_block(content, skill_id):
    """Extract a complete skill block from content"""
    # Find the skill block
    pattern = rf'(ID: {re.escape(skill_id)}\s*\nTopic: [^\n]+\s*\nSkill: [^\n]+\s*\nDescription: [^\n]+(?:\n(?!ID:|^# T)[^\n]+)*(?:\s*\nDependencies:\s*\n(?:\* [^\n]+\n)*)?)'

    match = re.search(pattern, content, re.MULTILINE)
    if match:
        return match.group(1), match.start(), match.end()
    return None, None, None

def add_dependency(skill_block, new_dep, all_skills):
    """Add a dependency to a skill block"""
    # Check if Dependencies section exists
    if 'Dependencies:' in skill_block:
        # Find the Dependencies section
        deps_match = re.search(r'(Dependencies:\s*\n)((?:\* [^\n]+\n)*)', skill_block, re.MULTILINE)
        if deps_match:
            existing_deps = deps_match.group(2)

            # Check if dependency already exists
            if new_dep in existing_deps:
                return skill_block, False

            # Get the skill name for the new dependency
            if new_dep in all_skills:
                dep_name = all_skills[new_dep]['skill']
                new_line = f"* {new_dep}: {dep_name}\n"

                # Insert the new dependency
                updated_block = skill_block.replace(
                    deps_match.group(0),
                    deps_match.group(1) + existing_deps + new_line
                )
                return updated_block, True
    else:
        # Add Dependencies section before the end
        if new_dep in all_skills:
            dep_name = all_skills[new_dep]['skill']
            deps_section = f"\nDependencies:\n* {new_dep}: {dep_name}\n"

            # Add before the next ID or end of skill block
            updated_block = skill_block.rstrip() + "\n" + deps_section
            return updated_block, True

    return skill_block, False

def parse_allskills(filepath):
    """Parse allskills.md and extract all Grade K skills"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    sections = content.split('\nID: ')

    for section in sections:
        if not section.strip():
            continue

        if not section.startswith('ID:'):
            section = 'ID: ' + section

        id_match = re.search(r'ID: (T\d+\.GK\.\d+)', section)
        if not id_match:
            continue

        skill_id = id_match.group(1)
        skill_match = re.search(r'Skill: ([^\n]+)', section)
        skill_name = skill_match.group(1).strip() if skill_match else ''

        skills[skill_id] = {
            'skill': skill_name,
        }

    return skills

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    # Read the entire file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse all skills to get skill names
    all_skills = parse_allskills(filepath)

    print("="*80)
    print("APPLYING CROSS-TOPIC DEPENDENCIES")
    print("="*80)

    changes_made = {}
    total_additions = 0

    # Process each approved addition
    for skill_id, new_deps in sorted(APPROVED_ADDITIONS.items()):
        if not new_deps:
            continue

        print(f"\n{skill_id}:")

        for new_dep in new_deps:
            # Find the skill block in content
            skill_block, start, end = parse_skill_block(content, skill_id)

            if skill_block is None:
                print(f"  ✗ Could not find skill block")
                continue

            # Add the dependency
            updated_block, added = add_dependency(skill_block, new_dep, all_skills)

            if added:
                # Replace in content
                content = content[:start] + updated_block + content[end:]
                print(f"  ✓ Added {new_dep}")

                if skill_id not in changes_made:
                    changes_made[skill_id] = []
                changes_made[skill_id].append(new_dep)
                total_additions += 1
            else:
                print(f"  - {new_dep} (already exists)")

    # Write the updated content back
    backup_path = filepath + '.backup'
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n✓ Backup saved to: {backup_path}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Updated file: {filepath}")

    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Total skills modified: {len(changes_made)}")
    print(f"Total dependencies added: {total_additions}")

    if changes_made:
        print(f"\nDetailed changes:")
        for skill_id, deps in sorted(changes_made.items()):
            print(f"  {skill_id}: +{len(deps)} dependencies")
            for dep in deps:
                print(f"    → {dep}")

if __name__ == '__main__':
    main()
