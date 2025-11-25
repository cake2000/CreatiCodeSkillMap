#!/usr/bin/env python3
"""
Apply Grade 7 fixes to allskills.md based on GRADE7_FIXES_PLAN.json
"""

import json
import re
from typing import Dict, List, Tuple

def load_json_plan(filepath: str) -> dict:
    """Load the fixes plan from JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_markdown(filepath: str) -> str:
    """Load the markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def save_markdown(filepath: str, content: str):
    """Save the markdown file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def find_skill_block(content: str, skill_id: str) -> Tuple[int, int]:
    """
    Find the start and end positions of a skill block in the content.
    Returns (start_pos, end_pos) or (-1, -1) if not found.
    """
    # Pattern to find skill ID
    pattern = rf'^ID: {re.escape(skill_id)}$'

    lines = content.split('\n')
    start_idx = -1

    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start_idx = i
            break

    if start_idx == -1:
        return (-1, -1)

    # Find the end of this skill block (next ID: or end of file)
    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if lines[i].startswith('ID:'):
            end_idx = i
            break

    # Calculate character positions
    start_pos = sum(len(line) + 1 for line in lines[:start_idx])
    end_pos = sum(len(line) + 1 for line in lines[:end_idx])

    return (start_pos, end_pos)

def find_dependencies_section(skill_block: str) -> Tuple[int, int]:
    """
    Find the Dependencies section within a skill block.
    Returns (start_offset, end_offset) relative to skill_block start.
    """
    lines = skill_block.split('\n')
    dep_start = -1
    dep_end = -1

    for i, line in enumerate(lines):
        if line.strip() == 'Dependencies:':
            dep_start = i
            # Find end of dependencies (next non-empty line that doesn't start with * or empty line followed by non-dependency)
            for j in range(i + 1, len(lines)):
                stripped = lines[j].strip()
                # End when we hit an empty line or a line that doesn't start with *
                if stripped and not stripped.startswith('*'):
                    dep_end = j
                    break
            if dep_end == -1:
                dep_end = len(lines)
            break

    if dep_start == -1:
        return (-1, -1)

    # Calculate character offsets
    start_offset = sum(len(line) + 1 for line in lines[:dep_start])
    end_offset = sum(len(line) + 1 for line in lines[:dep_end])

    return (start_offset, end_offset)

def apply_replace_dependency(content: str, skill_id: str, old_value: str, new_value: str) -> Tuple[str, bool]:
    """Replace a dependency in the skill block"""
    skill_start, skill_end = find_skill_block(content, skill_id)

    if skill_start == -1:
        return content, False

    skill_block = content[skill_start:skill_end]
    dep_start, dep_end = find_dependencies_section(skill_block)

    if dep_start == -1:
        return content, False

    # Extract dependencies section
    deps_section = skill_block[dep_start:dep_end]

    # Find and replace the dependency line
    lines = deps_section.split('\n')
    replaced = False
    new_lines = []

    for line in lines:
        if line.strip().startswith(f'* {old_value}:'):
            # Replace the skill ID but keep the description
            new_line = line.replace(f'* {old_value}:', f'* {new_value}:', 1)
            new_lines.append(new_line)
            replaced = True
        else:
            new_lines.append(line)

    if not replaced:
        return content, False

    # Rebuild the skill block
    new_deps_section = '\n'.join(new_lines)
    new_skill_block = skill_block[:dep_start] + new_deps_section + skill_block[dep_end:]

    # Rebuild the content
    new_content = content[:skill_start] + new_skill_block + content[skill_end:]

    return new_content, True

def apply_add_dependency(content: str, skill_id: str, new_value: str, justification: str) -> Tuple[str, bool]:
    """Add a new dependency to the skill block"""
    skill_start, skill_end = find_skill_block(content, skill_id)

    if skill_start == -1:
        return content, False

    skill_block = content[skill_start:skill_end]
    dep_start, dep_end = find_dependencies_section(skill_block)

    if dep_start == -1:
        return content, False

    # Extract dependencies section
    deps_section = skill_block[dep_start:dep_end]

    # Check if dependency already exists
    if f'* {new_value}:' in deps_section:
        return content, False  # Already exists, skip

    # Find the last dependency line
    lines = deps_section.split('\n')
    insert_idx = -1

    for i in range(len(lines) - 1, -1, -1):
        if lines[i].strip().startswith('* '):
            insert_idx = i + 1
            break

    if insert_idx == -1:
        # No dependencies found, insert after Dependencies:
        for i, line in enumerate(lines):
            if line.strip() == 'Dependencies:':
                insert_idx = i + 1
                break

    if insert_idx == -1:
        return content, False

    # Create the new dependency line (extract description from justification or use generic)
    new_dep_line = f'* {new_value}: {justification[:80] if justification else "Required dependency"}'

    # Insert the new line
    lines.insert(insert_idx, new_dep_line)

    # Rebuild the skill block
    new_deps_section = '\n'.join(lines)
    new_skill_block = skill_block[:dep_start] + new_deps_section + skill_block[dep_end:]

    # Rebuild the content
    new_content = content[:skill_start] + new_skill_block + content[skill_end:]

    return new_content, True

def apply_remove_dependency(content: str, skill_id: str, old_value: str) -> Tuple[str, bool]:
    """Remove a dependency from the skill block"""
    skill_start, skill_end = find_skill_block(content, skill_id)

    if skill_start == -1:
        return content, False

    skill_block = content[skill_start:skill_end]
    dep_start, dep_end = find_dependencies_section(skill_block)

    if dep_start == -1:
        return content, False

    # Extract dependencies section
    deps_section = skill_block[dep_start:dep_end]

    # Remove the dependency line
    lines = deps_section.split('\n')
    removed = False
    new_lines = []

    for line in lines:
        if line.strip().startswith(f'* {old_value}:'):
            removed = True
            continue  # Skip this line
        new_lines.append(line)

    if not removed:
        return content, False

    # Rebuild the skill block
    new_deps_section = '\n'.join(new_lines)
    new_skill_block = skill_block[:dep_start] + new_deps_section + skill_block[dep_end:]

    # Rebuild the content
    new_content = content[:skill_start] + new_skill_block + content[skill_end:]

    return new_content, True

def main():
    """Main execution function"""
    # Load files
    plan = load_json_plan('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE7_FIXES_PLAN.json')
    content = load_markdown('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')

    # Track changes
    changes_log = []
    stats = {
        'x2_fixes': 0,
        'redundant_removals': 0,
        't8_additions': 0,
        't9_additions': 0,
        't10_additions': 0,
        't7_additions': 0,
        't6_additions': 0,
        't11_additions': 0,
        'failed': 0
    }

    # Process each category
    for category_data in plan['fixes']:
        category = category_data['category']
        print(f"\nProcessing: {category}")
        print(f"Total fixes in category: {len(category_data['fixes'])}")

        for fix in category_data['fixes']:
            skill_id = fix['skill_id']
            action = fix['action']

            # Skip review actions
            if action == 'review':
                continue

            success = False

            if action == 'replace_dependency':
                old_val = fix['old_value']
                new_val = fix['new_value']
                content, success = apply_replace_dependency(content, skill_id, old_val, new_val)
                if success:
                    changes_log.append({
                        'skill_id': skill_id,
                        'action': 'replace',
                        'old': old_val,
                        'new': new_val,
                        'category': category
                    })
                    if 'X-2' in category:
                        stats['x2_fixes'] += 1
                else:
                    print(f"  FAILED: {skill_id} - replace {old_val} -> {new_val}")
                    stats['failed'] += 1

            elif action == 'add_dependency':
                new_val = fix['new_value']
                justification = fix.get('justification', '')
                content, success = apply_add_dependency(content, skill_id, new_val, justification)
                if success:
                    changes_log.append({
                        'skill_id': skill_id,
                        'action': 'add',
                        'new': new_val,
                        'category': category
                    })
                    # Track by topic
                    if 'Topic 8' in category:
                        stats['t8_additions'] += 1
                    elif 'Topic 9' in category:
                        stats['t9_additions'] += 1
                    elif 'Topic 10' in category:
                        stats['t10_additions'] += 1
                    elif 'Topic 7' in category:
                        stats['t7_additions'] += 1
                    elif 'Topic 6' in category:
                        stats['t6_additions'] += 1
                    elif 'Topic 11' in category:
                        stats['t11_additions'] += 1
                else:
                    print(f"  FAILED: {skill_id} - add {new_val}")
                    stats['failed'] += 1

            elif action == 'remove_dependency':
                old_val = fix['old_value']
                content, success = apply_remove_dependency(content, skill_id, old_val)
                if success:
                    changes_log.append({
                        'skill_id': skill_id,
                        'action': 'remove',
                        'old': old_val,
                        'category': category
                    })
                    stats['redundant_removals'] += 1
                else:
                    print(f"  FAILED: {skill_id} - remove {old_val}")
                    stats['failed'] += 1

    # Save updated file
    save_markdown('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', content)

    # Save changes log
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g7_changes_log.json', 'w') as f:
        json.dump({'changes': changes_log, 'stats': stats}, f, indent=2)

    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"X-2 Rule Fixes Applied: {stats['x2_fixes']}")
    print(f"Redundant Dependencies Removed: {stats['redundant_removals']}")
    print(f"Topic 8 (Conditions) Added: {stats['t8_additions']}")
    print(f"Topic 9 (Variables) Added: {stats['t9_additions']}")
    print(f"Topic 10 (Lists/Tables) Added: {stats['t10_additions']}")
    print(f"Topic 7 (Loops) Added: {stats['t7_additions']}")
    print(f"Topic 6 (Events) Added: {stats['t6_additions']}")
    print(f"Topic 11 (Functions) Added: {stats['t11_additions']}")
    print(f"Failed Operations: {stats['failed']}")
    print(f"Total Successful: {sum(stats.values()) - stats['failed']}")
    print("="*60)

if __name__ == '__main__':
    main()
