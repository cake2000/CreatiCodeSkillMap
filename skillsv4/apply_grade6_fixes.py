#!/usr/bin/env python3
"""
Apply Grade 6 dependency fixes to allskills.md
- Fix 2 circular dependencies
- Add 192 missing cross-topic dependencies
"""

import json
import re
import sys
from collections import defaultdict

def load_recommendations(filepath):
    """Load the fix recommendations JSON"""
    with open(filepath, 'r') as f:
        return json.load(f)

def read_allskills(filepath):
    """Read the allskills.md file"""
    with open(filepath, 'r') as f:
        return f.read()

def write_allskills(filepath, content):
    """Write the updated allskills.md file"""
    with open(filepath, 'w') as f:
        f.write(content)

def find_skill_block(content, skill_id):
    """
    Find the entire skill block for a given skill_id.
    Returns (start_pos, end_pos, skill_block_text) or (None, None, None) if not found
    """
    # Pattern to match a skill block starting with "- id: SKILL_ID"
    pattern = rf'^(- id: {re.escape(skill_id)}\n(?:(?!^- id:).*\n)*)'
    match = re.search(pattern, content, re.MULTILINE)

    if match:
        return match.start(), match.end(), match.group(1)
    return None, None, None

def parse_depends_list(skill_block):
    """
    Extract the depends list from a skill block.
    Returns list of dependencies or None if no depends list found.
    """
    # Look for "depends:" line followed by list items
    depends_match = re.search(r'  depends:\s*\n((?:    - [^\n]+\n)*)', skill_block)
    if not depends_match:
        # Check if depends is empty list []
        if re.search(r'  depends:\s*\[\s*\]', skill_block):
            return []
        return None

    depends_text = depends_match.group(1)
    deps = []
    for line in depends_text.split('\n'):
        line = line.strip()
        if line.startswith('- '):
            deps.append(line[2:].strip())
    return deps

def format_depends_list(depends_list):
    """Format a list of dependencies as YAML list"""
    if not depends_list:
        return "  depends: []"

    formatted = "  depends:\n"
    for dep in depends_list:
        formatted += f"    - {dep}\n"
    return formatted.rstrip('\n')

def update_skill_depends(content, skill_id, new_depends):
    """
    Update the depends list for a specific skill.
    Returns updated content and whether change was made.
    """
    start_pos, end_pos, skill_block = find_skill_block(content, skill_id)

    if start_pos is None:
        print(f"  ERROR: Skill {skill_id} not found in allskills.md")
        return content, False

    # Parse current depends
    current_depends = parse_depends_list(skill_block)

    # Build updated skill block
    # Remove old depends section
    depends_pattern = r'  depends:(?:\s*\[\s*\]|\s*\n(?:    - [^\n]+\n)*)'
    updated_block = re.sub(depends_pattern, '', skill_block)

    # Add new depends section after the "id:" line
    lines = updated_block.split('\n')
    new_lines = []
    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.strip().startswith('id:') and i == 0:
            # Insert depends after id line
            new_depends_formatted = format_depends_list(new_depends)
            for dep_line in new_depends_formatted.split('\n'):
                new_lines.append(dep_line)

    updated_block = '\n'.join(new_lines)
    if not updated_block.endswith('\n'):
        updated_block += '\n'

    # Replace in content
    new_content = content[:start_pos] + updated_block + content[end_pos:]

    return new_content, True

def apply_circular_dependency_fixes(content, recommendations):
    """Apply circular dependency fixes"""
    changes = []

    print("\n=== FIXING CIRCULAR DEPENDENCIES ===")
    for fix in recommendations['fixes']['circular_dependencies']['fixes']:
        skill_id = fix['fix']['remove_from']
        dep_to_remove = fix['fix']['remove_dependency']

        print(f"\nProcessing {fix['issue_id']}: {fix['cycle']}")
        print(f"  Removing '{dep_to_remove}' from {skill_id}")

        # Find current dependencies
        start_pos, end_pos, skill_block = find_skill_block(content, skill_id)
        if start_pos is None:
            print(f"  ERROR: Skill {skill_id} not found")
            continue

        current_depends = parse_depends_list(skill_block)
        if current_depends is None:
            print(f"  ERROR: No depends list found for {skill_id}")
            continue

        if dep_to_remove not in current_depends:
            print(f"  WARNING: '{dep_to_remove}' not found in current dependencies")
            print(f"  Current deps: {current_depends}")
            continue

        # Remove the dependency
        new_depends = [d for d in current_depends if d != dep_to_remove]

        # Update content
        content, success = update_skill_depends(content, skill_id, new_depends)

        if success:
            changes.append({
                'issue_id': fix['issue_id'],
                'skill_id': skill_id,
                'action': 'REMOVE',
                'dependency': dep_to_remove,
                'before': current_depends,
                'after': new_depends,
                'rationale': fix['fix']['rationale']
            })
            print(f"  ✓ Successfully removed dependency")
        else:
            print(f"  ✗ Failed to update skill")

    return content, changes

def apply_missing_dependencies(content, recommendations):
    """Apply missing cross-topic dependency fixes"""
    changes = []

    print("\n=== ADDING MISSING CROSS-TOPIC DEPENDENCIES ===")

    fixes = recommendations['fixes']['missing_cross_topic_dependencies']['fixes']
    print(f"\nTotal fixes to apply: {len(fixes)}")

    for i, fix in enumerate(fixes, 1):
        skill_id = fix['skill_id']
        deps_to_add = fix['fix']['add_dependencies']

        if i % 20 == 0:
            print(f"\nProgress: {i}/{len(fixes)} skills processed...")

        # Find current dependencies
        start_pos, end_pos, skill_block = find_skill_block(content, skill_id)
        if start_pos is None:
            print(f"  ERROR: Skill {skill_id} not found")
            continue

        current_depends = parse_depends_list(skill_block)
        if current_depends is None:
            current_depends = []

        # Add new dependencies (avoid duplicates)
        new_depends = current_depends.copy()
        added_deps = []
        for dep in deps_to_add:
            if dep not in new_depends:
                new_depends.append(dep)
                added_deps.append(dep)

        # Sort dependencies for consistency
        new_depends.sort()

        if not added_deps:
            continue  # No new deps to add

        # Update content
        content, success = update_skill_depends(content, skill_id, new_depends)

        if success:
            changes.append({
                'issue_id': fix['issue_id'],
                'skill_id': skill_id,
                'skill_name': fix['skill_name'],
                'action': 'ADD',
                'dependencies': added_deps,
                'before': current_depends,
                'after': new_depends,
                'rationale': fix['fix']['rationale']
            })

    print(f"\nCompleted: {len(changes)} skills updated with missing dependencies")
    return content, changes

def generate_change_log(circ_changes, missing_changes, output_file):
    """Generate a detailed change log in Markdown format"""

    log = "# Grade 6 Dependency Fixes - Change Log\n\n"
    log += f"**Generated:** 2025-11-24\n\n"
    log += "## Summary\n\n"
    log += f"- **Circular dependency fixes:** {len(circ_changes)}\n"
    log += f"- **Missing cross-topic dependencies added:** {len(missing_changes)}\n"
    log += f"- **Total skills modified:** {len(circ_changes) + len(missing_changes)}\n\n"

    # Circular dependency fixes
    log += "## Part 1: Circular Dependency Fixes (CRITICAL)\n\n"
    for change in circ_changes:
        log += f"### {change['issue_id']}: {change['skill_id']}\n\n"
        log += f"**Action:** Remove circular dependency\n\n"
        log += f"**Dependency removed:** `{change['dependency']}`\n\n"
        log += f"**Rationale:** {change['rationale']}\n\n"
        log += "**Before:**\n```yaml\n"
        log += f"depends:\n"
        for dep in change['before']:
            log += f"  - {dep}\n"
        log += "```\n\n"
        log += "**After:**\n```yaml\n"
        log += f"depends:\n"
        for dep in change['after']:
            log += f"  - {dep}\n"
        log += "```\n\n"
        log += "---\n\n"

    # Missing dependencies by topic
    log += "## Part 2: Missing Cross-Topic Dependencies\n\n"

    # Group by topic
    by_topic = defaultdict(list)
    for change in missing_changes:
        topic = change['skill_id'].split('.')[0]
        by_topic[topic].append(change)

    for topic in sorted(by_topic.keys()):
        topic_changes = by_topic[topic]
        log += f"### Topic {topic} ({len(topic_changes)} skills)\n\n"

        for change in topic_changes:
            log += f"#### {change['skill_id']}: {change['skill_name']}\n\n"
            log += f"**Dependencies added:** {', '.join(f'`{d}`' for d in change['dependencies'])}\n\n"
            log += f"**Rationale:** {change['rationale']}\n\n"

            if len(change['before']) > 0:
                log += "**Dependencies before:**\n"
                log += ', '.join(f'`{d}`' for d in change['before'][:5])
                if len(change['before']) > 5:
                    log += f" ... ({len(change['before'])} total)"
                log += "\n\n"
            else:
                log += "**Dependencies before:** None\n\n"

            log += "**Dependencies after:**\n"
            log += ', '.join(f'`{d}`' for d in change['after'][:8])
            if len(change['after']) > 8:
                log += f" ... ({len(change['after'])} total)"
            log += "\n\n"

            log += "---\n\n"

    # Write to file
    with open(output_file, 'w') as f:
        f.write(log)

    print(f"\nChange log written to: {output_file}")

def main():
    base_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4'
    recommendations_file = f'{base_path}/GRADE6_FIX_RECOMMENDATIONS.json'
    allskills_file = f'{base_path}/allskills.md'
    changelog_file = f'{base_path}/GRADE6_DEPENDENCY_CHANGES.md'

    print("=" * 70)
    print("Grade 6 Dependency Fixes Application")
    print("=" * 70)

    # Load recommendations
    print("\nLoading recommendations...")
    recommendations = load_recommendations(recommendations_file)
    print(f"  ✓ Loaded {recommendations['metadata']['total_issues']} issues")

    # Read allskills.md
    print("\nReading allskills.md...")
    content = read_allskills(allskills_file)
    print(f"  ✓ Read {len(content)} characters")

    # Apply circular dependency fixes first
    content, circ_changes = apply_circular_dependency_fixes(content, recommendations)

    # Apply missing dependencies
    content, missing_changes = apply_missing_dependencies(content, recommendations)

    # Write updated content
    print("\nWriting updated allskills.md...")
    write_allskills(allskills_file, content)
    print("  ✓ File updated successfully")

    # Generate change log
    print("\nGenerating change log...")
    generate_change_log(circ_changes, missing_changes, changelog_file)

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Circular dependencies fixed: {len(circ_changes)}")
    print(f"Missing dependencies added: {len(missing_changes)}")
    print(f"Total skills modified: {len(circ_changes) + len(missing_changes)}")
    print("\nFiles updated:")
    print(f"  - {allskills_file}")
    print(f"  - {changelog_file}")
    print("\n✓ All fixes applied successfully!")

if __name__ == '__main__':
    main()
