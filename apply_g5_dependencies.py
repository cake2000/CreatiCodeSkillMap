#!/usr/bin/env python3
"""
Apply Grade 5 dependency fixes from GRADE5_DEPENDENCY_REPORT.md to allskills.md
"""

import re
from collections import defaultdict

# Complete mapping of all recommended dependency additions from the report
DEPENDENCY_ADDITIONS = {
    'T01.G5.02': ['T09.G3.03', 'T10.G3.05', 'T10.G4.18'],
    'T01.G5.09': ['T10.G3.05', 'T10.G4.18'],
    'T01.G5.10': ['T10.G3.05', 'T10.G4.18'],
    'T02.G5.01': ['T10.G3.05', 'T10.G4.18'],
    'T02.G5.02': ['T10.G3.05', 'T10.G4.18'],
    'T03.G5.03': ['T09.G3.03'],
    'T03.G5.04': ['T09.G3.03'],
    'T03.G5.06': ['T09.G3.03'],
    'T04.G5.03': ['T09.G3.03'],
    'T04.G5.06': ['T09.G3.03'],
    'T05.G5.03': ['T09.G3.03'],
    'T05.G5.05': ['T09.G3.03'],
    'T06.G5.01': ['T09.G3.03'],
    'T06.G5.07': ['T09.G3.03'],
    'T06.G5.08': ['T12.G3.05', 'T12.G4.05'],
    'T06.G5.10': ['T09.G3.03'],
    'T07.G5.01': ['T10.G3.05', 'T10.G4.18'],
    'T07.G5.02': ['T10.G3.05', 'T10.G4.18'],
    'T07.G5.03': ['T10.G3.05', 'T10.G4.18'],
    'T07.G5.04': ['T10.G3.05', 'T10.G4.18'],
    'T08.G5.03': ['T09.G3.03'],
    'T08.G5.05': ['T09.G3.03'],
    'T08.G5.06': ['T09.G3.03'],
    'T09.G5.06': ['T10.G3.05', 'T10.G4.18'],
    'T10.G5.09': ['T09.G3.03'],
    'T10.G5.11': ['T09.G3.03'],
    'T10.G5.13': ['T09.G3.03'],
    'T11.G5.01': ['T12.G3.05', 'T12.G4.05'],
    'T11.G5.02': ['T12.G3.05', 'T12.G4.05'],
    'T11.G5.03': ['T12.G3.05', 'T12.G4.05'],
    'T11.G5.04': ['T12.G3.05', 'T12.G4.05'],
    'T11.G5.06': ['T12.G3.05', 'T12.G4.05'],
    'T11.G5.07': ['T12.G3.05', 'T12.G4.05'],
    'T11.G5.08': ['T12.G3.05', 'T12.G4.05'],
    'T11.G5.09': ['T12.G3.05', 'T12.G4.05'],
    'T11.G5.10': ['T12.G3.05', 'T12.G4.05'],
    'T11.G5.11': ['T12.G3.05', 'T12.G4.05'],
    'T13.G5.05': ['T10.G3.05', 'T10.G4.18'],
    'T13.G5.06': ['T10.G3.05', 'T10.G4.18'],
    'T13.G5.09': ['T09.G3.03'],
    'T14.G5.01': ['T12.G3.05', 'T12.G4.05'],
    'T15.G5.02': ['T09.G3.03'],
    'T15.G5.08': ['T09.G3.03'],
    'T18.G5.04': ['T10.G3.05', 'T10.G4.18'],
    'T20.G5.04': ['T10.G3.05', 'T10.G4.18'],
    'T21.G5.03': ['T09.G3.03', 'T12.G3.05', 'T12.G4.05'],
    'T21.G5.07': ['T12.G3.05', 'T12.G4.05'],
    'T22.G5.05': ['T12.G3.05', 'T09.G3.03', 'T12.G4.05'],
    'T23.G5.04': ['T09.G3.03'],
    'T23.G5.05': ['T09.G3.03'],
    'T24.G5.07': ['T12.G3.05', 'T12.G4.05'],
    'T24.G5.12': ['T09.G3.03'],
    'T25.G5.01': ['T12.G3.05', 'T12.G4.05'],
    'T25.G5.02': ['T09.G3.03'],
    'T28.G5.02': ['T09.G3.03'],
    'T30.G5.01': ['T09.G3.03'],
    'T30.G5.02': ['T12.G3.05', 'T12.G4.05'],
    'T30.G5.03': ['T09.G3.03'],
    'T30.G5.06': ['T09.G3.03'],
    'T32.G5.04': ['T09.G3.03'],
    'T35.G5.03': ['T09.G3.03'],
}

def parse_skill_block(lines, start_idx):
    """
    Parse a skill block starting at start_idx.
    Returns (skill_id, end_idx, skill_lines, depends_on_list)
    """
    # Find skill ID from the "ID: " line
    skill_id = None
    id_line = lines[start_idx].strip()
    if id_line.startswith('ID:'):
        skill_id = id_line.replace('ID:', '').strip()

    # Find the end of this skill block (next "ID:" line or end of file)
    end_idx = start_idx + 1
    while end_idx < len(lines):
        if lines[end_idx].strip().startswith('ID:'):
            break
        end_idx += 1

    skill_lines = lines[start_idx:end_idx]

    # Extract current depends_on list (now called "Dependencies:")
    depends_on = []
    in_depends = False
    for line in skill_lines:
        if line.strip().startswith('Dependencies:'):
            in_depends = True
            # Check if it's inline format (not used in this file format)
            continue
        elif in_depends:
            if line.strip().startswith('*'):
                # Extract dependency ID from "* T10.G4.02: Description" format
                dep_match = re.match(r'^\*\s+([^:]+):', line.strip())
                if dep_match:
                    dep = dep_match.group(1).strip()
                    depends_on.append(dep)
            elif line.strip() and not line.startswith('*') and not line.strip().startswith('#'):
                # Next section started
                in_depends = False

    return skill_id, end_idx, skill_lines, depends_on

def update_depends_on(skill_lines, current_deps, new_deps):
    """
    Update the Dependencies field in skill_lines.
    Returns updated skill_lines.
    """
    # Combine current and new dependencies, removing duplicates while preserving order
    all_deps = list(dict.fromkeys(current_deps + new_deps))

    # Find the Dependencies line
    depends_line_idx = None
    for i, line in enumerate(skill_lines):
        if line.strip().startswith('Dependencies:'):
            depends_line_idx = i
            break

    if depends_line_idx is None:
        # No Dependencies field exists - need to add one
        # Find where to insert (after Description, before blank line at end)
        insert_idx = len(skill_lines) - 1  # Before the final blank line
        for i in range(len(skill_lines) - 1, -1, -1):
            if skill_lines[i].strip().startswith('Description:'):
                # Skip to end of description (multiline)
                j = i + 1
                while j < len(skill_lines) and (skill_lines[j].startswith('  ') or not skill_lines[j].strip()):
                    if skill_lines[j].strip():  # Non-blank line
                        insert_idx = j + 1
                    j += 1
                insert_idx = j
                break

        # Insert Dependencies field in format "* T10.G4.02: Description"
        skill_lines.insert(insert_idx, '\n')
        skill_lines.insert(insert_idx + 1, 'Dependencies:\n')
        for dep in all_deps:
            # Add dependency without description (we don't have descriptions in our mapping)
            skill_lines.insert(insert_idx + 2, f'* {dep}\n')
            insert_idx += 1
        skill_lines.insert(insert_idx + 2, '\n')
    else:
        # Update existing Dependencies
        # Find all existing dependency lines and remove them
        i = depends_line_idx + 1
        while i < len(skill_lines) and (skill_lines[i].strip().startswith('*') or (skill_lines[i].strip() == '' and i < len(skill_lines) - 1 and skill_lines[i+1].strip().startswith('*'))):
            skill_lines.pop(i)

        # Add all dependencies (merged list)
        for j, dep in enumerate(all_deps):
            skill_lines.insert(depends_line_idx + 1 + j, f'* {dep}\n')

    return skill_lines

def apply_dependency_fixes(input_file, output_file):
    """
    Read allskills.md, apply dependency fixes, and write back.
    """
    # Read the file
    print(f"Reading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print(f"Total lines: {len(lines)}")

    # Track changes
    changes_by_topic = defaultdict(list)
    skills_processed = []
    skills_not_found = []

    # Process the file
    new_lines = []
    i = 0
    while i < len(lines):
        if lines[i].strip().startswith('ID:'):
            # Found a skill block
            skill_id, end_idx, skill_lines, current_deps = parse_skill_block(lines, i)

            # Check if this skill or its parent needs updating
            # For sub-skills like T01.G5.02.01.01, check if T01.G5.02 is in DEPENDENCY_ADDITIONS
            needs_update = False
            new_deps = []
            matching_parent = None

            if skill_id in DEPENDENCY_ADDITIONS:
                needs_update = True
                new_deps = DEPENDENCY_ADDITIONS[skill_id]
                matching_parent = skill_id
            else:
                # Check if any parent skill needs these dependencies
                # For T01.G5.02.01.01, check T01.G5.02
                parts = skill_id.split('.')
                if len(parts) > 3:  # Has sub-skill parts
                    parent_id = '.'.join(parts[:3])  # e.g., T01.G5.02
                    if parent_id in DEPENDENCY_ADDITIONS:
                        needs_update = True
                        new_deps = DEPENDENCY_ADDITIONS[parent_id]
                        matching_parent = parent_id

            if needs_update:
                # Filter out dependencies that already exist
                deps_to_add = [d for d in new_deps if d not in current_deps]

                if deps_to_add:
                    print(f"\nUpdating {skill_id} (from {matching_parent}):")
                    print(f"  Current deps: {current_deps}")
                    print(f"  Adding: {deps_to_add}")

                    # Update the skill block
                    updated_lines = update_depends_on(skill_lines, current_deps, new_deps)
                    new_lines.extend(updated_lines)

                    # Track the change
                    topic = skill_id.split('.')[0]
                    changes_by_topic[topic].append({
                        'skill_id': skill_id,
                        'parent': matching_parent,
                        'added': deps_to_add
                    })
                    if matching_parent not in skills_processed:
                        skills_processed.append(matching_parent)
                else:
                    print(f"\n{skill_id}: All dependencies already present")
                    new_lines.extend(skill_lines)
                    if matching_parent not in skills_processed:
                        skills_processed.append(matching_parent)
            else:
                # No changes needed for this skill
                new_lines.extend(skill_lines)

            i = end_idx
        else:
            new_lines.append(lines[i])
            i += 1

    # Check for skills in DEPENDENCY_ADDITIONS that weren't found
    for skill_id in DEPENDENCY_ADDITIONS:
        if skill_id not in skills_processed:
            skills_not_found.append(skill_id)

    # Write the output file
    print(f"\nWriting to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    # Print summary
    print("\n" + "="*70)
    print("SUMMARY OF CHANGES")
    print("="*70)

    total_skills_updated = len(skills_processed)
    total_deps_added = sum(len(change['added']) for changes in changes_by_topic.values() for change in changes)

    print(f"\nTotal Grade 5 skills updated: {total_skills_updated}")
    print(f"Total dependencies added: {total_deps_added}")
    print(f"\nChanges by topic:")

    for topic in sorted(changes_by_topic.keys()):
        changes = changes_by_topic[topic]
        print(f"\n{topic}:")
        for change in changes:
            parent_info = f" (from {change['parent']})" if 'parent' in change and change['parent'] != change['skill_id'] else ""
            print(f"  {change['skill_id']}{parent_info}: added {len(change['added'])} dependencies")
            for dep in change['added']:
                print(f"    + {dep}")

    if skills_not_found:
        print(f"\nWARNING: The following skills were not found in the file:")
        for skill_id in skills_not_found:
            print(f"  - {skill_id}")

    print("\n" + "="*70)
    print(f"Updated file saved to: {output_file}")
    print("="*70)

    return {
        'total_skills_updated': total_skills_updated,
        'total_deps_added': total_deps_added,
        'changes_by_topic': dict(changes_by_topic),
        'skills_not_found': skills_not_found
    }

if __name__ == '__main__':
    input_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    result = apply_dependency_fixes(input_file, output_file)

    # Print final status
    print("\nFINAL STATUS: SUCCESS")
    print(f"File updated: {output_file}")
