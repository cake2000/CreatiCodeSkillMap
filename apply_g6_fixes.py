#!/usr/bin/env python3
"""
Apply Grade 6 dependency fixes to allskills.md
"""

import json
import re
from pathlib import Path

def load_fix_plan(fix_plan_path):
    """Load the G6 fix plan JSON file."""
    with open(fix_plan_path, 'r') as f:
        return json.load(f)

def load_allskills(allskills_path):
    """Load the allskills.md file."""
    with open(allskills_path, 'r') as f:
        return f.read()

def format_dependencies(deps_list):
    """Format dependencies list as markdown bullets."""
    if not deps_list:
        return "Dependencies: none\n"

    result = "Dependencies:\n"
    for dep in deps_list:
        result += f"* {dep}\n"
    return result

def apply_fixes(content, fix_plan):
    """Apply all G6 fixes to the content."""
    changes = []

    for skill_id, fix_data in fix_plan.items():
        # Find the skill block
        # Pattern: ID: skill_id, then Topic, Skill, Description, then Dependencies section
        # Dependencies can be multiple lines starting with *

        # First, find where the skill starts
        id_pattern = rf'^ID: {re.escape(skill_id)}$'
        id_match = re.search(id_pattern, content, re.MULTILINE)

        if not id_match:
            print(f"WARNING: Could not find skill {skill_id}")
            continue

        # Now find the Dependencies section for this skill
        # Start from the ID position
        start_pos = id_match.start()

        # Find the next ID (or end of file) to know where this skill ends
        next_id_pattern = r'^ID: T\d+\.G\d+\.\d+$'
        next_id_match = re.search(next_id_pattern, content[start_pos+1:], re.MULTILINE)
        if next_id_match:
            end_pos = start_pos + 1 + next_id_match.start()
        else:
            end_pos = len(content)

        skill_block = content[start_pos:end_pos]

        # Find Dependencies section within this skill block
        deps_pattern = r'Dependencies:\n(\*[^\n]*\n)*'
        deps_match = re.search(deps_pattern, skill_block)

        if not deps_match:
            # Try simpler pattern for "Dependencies: none"
            deps_pattern = r'Dependencies:[^\n]*\n'
            deps_match = re.search(deps_pattern, skill_block)

        if not deps_match:
            print(f"WARNING: Could not find Dependencies section for {skill_id}")
            continue

        # Extract old dependencies text
        old_deps_text = deps_match.group(0)

        # Build new dependencies text
        new_deps_text = format_dependencies(fix_data['new_dependencies'])

        # Replace in the full content
        old_full_text = content[start_pos:start_pos+len(skill_block)]
        new_full_text = old_full_text.replace(old_deps_text, new_deps_text, 1)

        content = content[:start_pos] + new_full_text + content[end_pos:]

        # Track change
        old_deps_str = old_deps_text.strip()
        new_deps_str = new_deps_text.strip()

        changes.append({
            'skill_id': skill_id,
            'skill_name': fix_data['skill_name'],
            'old_deps': old_deps_str,
            'new_deps': new_deps_str,
            'issues_fixed': len(fix_data['issues_fixed'])
        })

    return content, changes

def main():
    base_path = Path('/media/binyu/USB2/dev/CreatiCodeSkillMap')
    fix_plan_path = base_path / 'G6_FIX_PLAN.json'
    allskills_path = base_path / 'skillsv4' / 'allskills.md'

    print("Loading fix plan...")
    fix_plan = load_fix_plan(fix_plan_path)
    print(f"Loaded {len(fix_plan)} G6 skills to fix")

    print("\nLoading allskills.md...")
    content = load_allskills(allskills_path)
    print(f"Loaded file with {len(content)} characters")

    print("\nApplying fixes...")
    new_content, changes = apply_fixes(content, fix_plan)

    print(f"\nSuccessfully updated {len(changes)} skills")

    # Write the updated content
    print("\nWriting updated allskills.md...")
    with open(allskills_path, 'w') as f:
        f.write(new_content)

    # Generate summary report
    print("\n" + "="*80)
    print("GRADE 6 FIXES APPLIED - SUMMARY")
    print("="*80)
    print(f"\nTotal skills updated: {len(changes)}")
    print(f"Total issues fixed: {sum(c['issues_fixed'] for c in changes)}")

    # Count how many now have no dependencies
    no_deps = sum(1 for c in changes if 'none' in c['new_deps'])
    print(f"Skills with no dependencies: {no_deps}")
    print(f"Skills with dependencies: {len(changes) - no_deps}")

    # Show first 10 examples
    print("\n" + "-"*80)
    print("FIRST 10 EXAMPLES:")
    print("-"*80)
    for i, change in enumerate(changes[:10], 1):
        print(f"\n{i}. {change['skill_id']}: {change['skill_name']}")
        print(f"   Old: {change['old_deps'][:100]}...")  # Truncate for readability
        print(f"   New: {change['new_deps'][:100]}...")
        print(f"   Issues fixed: {change['issues_fixed']}")

    # Show summary by topic
    print("\n" + "-"*80)
    print("SUMMARY BY TOPIC:")
    print("-"*80)
    topics = {}
    for change in changes:
        topic = change['skill_id'].split('.')[0]  # e.g., T01, T02
        topics[topic] = topics.get(topic, 0) + 1

    for topic in sorted(topics.keys()):
        print(f"{topic}: {topics[topic]} skills updated")

    print("\n" + "="*80)
    print("Done! All Grade 6 fixes have been applied.")
    print("="*80)

if __name__ == '__main__':
    main()
