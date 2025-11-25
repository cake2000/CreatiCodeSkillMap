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

    Format:
    ID: TXX.GY.ZZ
    Topic: ...
    Skill: ...
    Description: ...

    Dependencies:
    * SKILL_ID: Description
    * SKILL_ID: Description


    (blank line before next ID)
    """
    # Find the skill ID line
    id_pattern = rf'^ID: {re.escape(skill_id)}$'
    id_match = re.search(id_pattern, content, re.MULTILINE)

    if not id_match:
        return None, None, None

    start_pos = id_match.start()

    # Find the end - either the next "ID:" line or end of file
    next_id_pattern = r'^ID: '
    next_match = re.search(next_id_pattern, content[id_match.end():], re.MULTILINE)

    if next_match:
        end_pos = id_match.end() + next_match.start()
    else:
        end_pos = len(content)

    skill_block = content[start_pos:end_pos]
    return start_pos, end_pos, skill_block

def parse_dependencies(skill_block):
    """
    Extract dependencies from a skill block.
    Returns list of (skill_id, description) tuples, or None if no dependencies.

    Format:
    Dependencies:
    * SKILL_ID: Description
    * SKILL_ID: Description
    """
    # Look for "Dependencies:" section
    deps_match = re.search(r'^Dependencies:\s*\n((?:\* [^\n]+\n)*)', skill_block, re.MULTILINE)

    if not deps_match:
        return None

    deps_text = deps_match.group(1)
    dependencies = []

    for line in deps_text.split('\n'):
        line = line.strip()
        if line.startswith('* '):
            # Parse "* SKILL_ID: Description" or "* SKILL_ID"
            dep_content = line[2:].strip()
            if ':' in dep_content:
                skill_id = dep_content.split(':', 1)[0].strip()
                description = dep_content.split(':', 1)[1].strip()
            else:
                skill_id = dep_content.strip()
                description = ""
            dependencies.append((skill_id, description))

    return dependencies if dependencies else None

def format_dependencies(dependencies):
    """
    Format dependencies list.
    dependencies is a list of (skill_id, description) tuples
    """
    if not dependencies:
        return ""

    formatted = "Dependencies:\n"
    for skill_id, description in dependencies:
        if description:
            formatted += f"* {skill_id}: {description}\n"
        else:
            formatted += f"* {skill_id}\n"

    return formatted

def update_skill_dependencies(content, skill_id, new_dependencies):
    """
    Update the dependencies for a specific skill.
    new_dependencies is a list of (skill_id, description) tuples
    Returns updated content and whether change was made.
    """
    start_pos, end_pos, skill_block = find_skill_block(content, skill_id)

    if start_pos is None:
        print(f"  ERROR: Skill {skill_id} not found in allskills.md")
        return content, False

    # Remove existing Dependencies section
    updated_block = re.sub(
        r'^Dependencies:\s*\n(?:\* [^\n]+\n)*\n*',
        '',
        skill_block,
        flags=re.MULTILINE
    )

    # Add new dependencies section before the blank lines at the end
    # First, strip trailing whitespace
    updated_block = updated_block.rstrip()

    # Add new dependencies
    if new_dependencies:
        updated_block += "\n\n" + format_dependencies(new_dependencies).rstrip()

    # Add trailing newlines
    updated_block += "\n\n\n"

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

        current_deps = parse_dependencies(skill_block)
        if current_deps is None:
            print(f"  ERROR: No dependencies found for {skill_id}")
            continue

        # Check if dependency exists
        dep_ids = [dep[0] for dep in current_deps]
        if dep_to_remove not in dep_ids:
            print(f"  WARNING: '{dep_to_remove}' not found in current dependencies")
            print(f"  Current deps: {dep_ids}")
            continue

        # Remove the dependency
        new_deps = [(sid, desc) for sid, desc in current_deps if sid != dep_to_remove]

        # Update content
        content, success = update_skill_dependencies(content, skill_id, new_deps)

        if success:
            changes.append({
                'issue_id': fix['issue_id'],
                'skill_id': skill_id,
                'action': 'REMOVE',
                'dependency': dep_to_remove,
                'before': [dep[0] for dep in current_deps],
                'after': [dep[0] for dep in new_deps],
                'rationale': fix['fix']['rationale']
            })
            print(f"  ✓ Successfully removed dependency")
        else:
            print(f"  ✗ Failed to update skill")

    return content, changes

def get_skill_description(content, skill_id):
    """Get the skill description for a given skill_id"""
    start_pos, end_pos, skill_block = find_skill_block(content, skill_id)
    if start_pos is None:
        return None

    # Extract the "Skill:" line
    skill_match = re.search(r'^Skill: (.+)$', skill_block, re.MULTILINE)
    if skill_match:
        return skill_match.group(1).strip()
    return None

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

        current_deps = parse_dependencies(skill_block)
        if current_deps is None:
            current_deps = []

        # Get current dependency IDs
        current_dep_ids = [dep[0] for dep in current_deps]

        # Add new dependencies (avoid duplicates)
        new_deps = current_deps.copy()
        added_deps = []

        for dep_id in deps_to_add:
            if dep_id not in current_dep_ids:
                # Get description for the new dependency
                dep_description = get_skill_description(content, dep_id)
                if dep_description:
                    new_deps.append((dep_id, dep_description))
                else:
                    new_deps.append((dep_id, ""))
                added_deps.append(dep_id)
                current_dep_ids.append(dep_id)

        if not added_deps:
            continue  # No new deps to add

        # Sort dependencies by skill ID
        new_deps.sort(key=lambda x: x[0])

        # Update content
        content, success = update_skill_dependencies(content, skill_id, new_deps)

        if success:
            changes.append({
                'issue_id': fix['issue_id'],
                'skill_id': skill_id,
                'skill_name': fix['skill_name'],
                'action': 'ADD',
                'dependencies': added_deps,
                'before': [dep[0] for dep in current_deps],
                'after': [dep[0] for dep in new_deps],
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
    if circ_changes:
        log += "## Part 1: Circular Dependency Fixes (CRITICAL)\n\n"
        for change in circ_changes:
            log += f"### {change['issue_id']}: {change['skill_id']}\n\n"
            log += f"**Action:** Remove circular dependency\n\n"
            log += f"**Dependency removed:** `{change['dependency']}`\n\n"
            log += f"**Rationale:** {change['rationale']}\n\n"
            log += "**Dependencies before:**\n"
            for dep in change['before']:
                log += f"- `{dep}`\n"
            log += "\n**Dependencies after:**\n"
            for dep in change['after']:
                log += f"- `{dep}`\n"
            log += "\n---\n\n"

    # Missing dependencies by topic
    if missing_changes:
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
                    log += "**Dependencies before:** "
                    log += ', '.join(f'`{d}`' for d in change['before'][:5])
                    if len(change['before']) > 5:
                        log += f" ... ({len(change['before'])} total)"
                    log += "\n\n"
                else:
                    log += "**Dependencies before:** None\n\n"

                log += "**Dependencies after:** "
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
