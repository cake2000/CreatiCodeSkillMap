#!/usr/bin/env python3
"""
Apply transitive dependency fixes from G3_TRANSITIVE_FIXES.json to allskills.md
"""

import json
import re

def load_json_fixes(json_path):
    """Load the fixes from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def load_markdown_file(md_path):
    """Load the markdown file"""
    with open(md_path, 'r') as f:
        return f.read()

def apply_fixes(content, fixes):
    """Apply all fixes to the content"""
    stats = {
        'total_fixes': len(fixes),
        'successful': 0,
        'failed': [],
        'changes': []
    }

    for fix in fixes:
        skill_id = fix['skill_id']
        remove_deps = fix['remove_deps']
        final_deps = fix['final_deps']

        # Find the skill section starting with "ID: SKILL_ID"
        # Look for Dependencies section that follows
        skill_pattern = rf'ID: {re.escape(skill_id)}\n.*?\nDependencies:\n((?:\* [^\n]+\n)+)'

        match = re.search(skill_pattern, content, re.DOTALL)

        if not match:
            stats['failed'].append({
                'skill_id': skill_id,
                'reason': 'Skill or dependencies section not found'
            })
            continue

        # Extract the dependencies block
        deps_block = match.group(1)

        # Parse each dependency line (format: "* T01.G2.01: Description")
        dep_lines = deps_block.strip().split('\n')
        current_deps_map = {}  # Maps skill_id to full line

        for line in dep_lines:
            if line.startswith('* '):
                # Extract the skill ID from the line
                dep_id_match = re.match(r'\* ([^:]+):', line)
                if dep_id_match:
                    dep_id = dep_id_match.group(1)
                    current_deps_map[dep_id] = line

        # Build new dependencies block
        new_dep_lines = []
        for dep_id in final_deps:
            if dep_id in current_deps_map:
                new_dep_lines.append(current_deps_map[dep_id])
            else:
                stats['failed'].append({
                    'skill_id': skill_id,
                    'reason': f'Dependency {dep_id} not found in original'
                })
                break
        else:
            # All dependencies found, build new block
            if new_dep_lines:
                new_deps_block = '\n'.join(new_dep_lines) + '\n'
            else:
                new_deps_block = ''

            # Replace the dependencies block
            old_full = match.group(0)
            new_full = old_full.replace(deps_block, new_deps_block)

            content = content.replace(old_full, new_full)

            stats['successful'] += 1
            stats['changes'].append({
                'skill_id': skill_id,
                'removed': remove_deps,
                'final': final_deps
            })

    return content, stats

def save_markdown_file(md_path, content):
    """Save the markdown file"""
    with open(md_path, 'w') as f:
        f.write(content)

def print_report(stats):
    """Print the detailed report"""
    print("\n" + "="*80)
    print("G3 TRANSITIVE FIXES APPLICATION REPORT")
    print("="*80)

    print(f"\nTotal fixes to apply: {stats['total_fixes']}")
    print(f"Successfully updated: {stats['successful']}")
    print(f"Failed: {len(stats['failed'])}")

    if stats['failed']:
        print("\nFailed updates:")
        for failure in stats['failed']:
            print(f"  - {failure['skill_id']}: {failure['reason']}")

    print("\nSuccessfully updated skills:")
    for change in stats['changes']:
        print(f"  - {change['skill_id']}")
        print(f"    Removed: {', '.join(change['removed'])}")
        print(f"    Final: {', '.join(change['final'])}")

    print("\n" + "="*80)
    print(f"File updated successfully with {stats['successful']} changes")
    print("="*80 + "\n")

def main():
    json_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G3_TRANSITIVE_FIXES.json'
    md_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Loading fixes from JSON...")
    fixes = load_json_fixes(json_path)

    print(f"Loading allskills.md...")
    content = load_markdown_file(md_path)

    print(f"Applying {len(fixes)} fixes...")
    new_content, stats = apply_fixes(content, fixes)

    print("Saving updated file...")
    save_markdown_file(md_path, new_content)

    print_report(stats)

if __name__ == '__main__':
    main()
