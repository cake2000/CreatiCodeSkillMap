#!/usr/bin/env python3
"""
Apply all fixes from G5_FIX_PLAN.json to allskills.md
"""

import json
import re
import shutil
from datetime import datetime

# File paths
FIX_PLAN_PATH = "/media/binyu/USB2/dev/CreatiCodeSkillMap/G5_FIX_PLAN.json"
ALLSKILLS_PATH = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"
BACKUP_PATH = f"/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md.backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
REPORT_PATH = "/media/binyu/USB2/dev/CreatiCodeSkillMap/G5_FIXES_APPLIED_REPORT.md"

def load_fix_plan():
    """Load the fix plan JSON"""
    with open(FIX_PLAN_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def backup_file():
    """Create a backup of the original file"""
    print(f"Creating backup: {BACKUP_PATH}")
    shutil.copy2(ALLSKILLS_PATH, BACKUP_PATH)
    return BACKUP_PATH

def find_skill_section(content, skill_id):
    """Find the start and end positions of a skill section"""
    # Pattern to match skill ID like "ID: T03.G5.01"
    pattern = rf'^ID: {re.escape(skill_id)}$'

    lines = content.split('\n')
    start_idx = None

    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start_idx = i
            break

    if start_idx is None:
        return None, None, None

    # Find the end of this skill section (next "ID:" or end of file)
    end_idx = len(lines)
    for i in range(start_idx + 1, len(lines)):
        if lines[i].startswith('ID: '):
            end_idx = i
            break

    return start_idx, end_idx, lines

def update_dependencies_line(lines, start_idx, end_idx, new_deps):
    """Update the dependencies section in a skill section"""
    # Find the dependencies header line
    deps_header_idx = None
    for i in range(start_idx, end_idx):
        if lines[i].strip() == 'Dependencies:':
            deps_header_idx = i
            break

    if deps_header_idx is None:
        print(f"  WARNING: Dependencies header not found in section")
        return False

    # Find the end of the dependencies section (next non-bullet line or empty line after bullets)
    deps_end_idx = deps_header_idx + 1
    for i in range(deps_header_idx + 1, end_idx):
        line = lines[i].strip()
        if line.startswith('* '):
            deps_end_idx = i + 1
        elif line == '':
            # Empty line might be separator or part of deps
            if deps_end_idx > deps_header_idx + 1:
                # We had some bullets, this is the end
                break
        else:
            # Non-bullet, non-empty line - end of deps
            break

    # Capture old dependencies
    old_deps_lines = lines[deps_header_idx:deps_end_idx]

    # Build new dependencies lines
    new_deps_lines = ['Dependencies:']
    if new_deps:
        # Need to get skill names for each dependency
        # For now, just use the ID. We'll need to look them up in the file
        sorted_deps = sorted(new_deps)
        for dep_id in sorted_deps:
            # Find the skill name for this dependency
            skill_name = get_skill_name(lines, dep_id)
            new_deps_lines.append(f'* {dep_id}: {skill_name}')
    else:
        # No dependencies - just leave it as "Dependencies:" with empty lines after
        pass

    # Replace the old dependencies with new ones
    lines[deps_header_idx:deps_end_idx] = new_deps_lines

    old_text = '\n'.join(old_deps_lines)
    new_text = '\n'.join(new_deps_lines)

    return True, old_text, new_text

def get_skill_name(lines, skill_id):
    """Find the skill name for a given skill ID"""
    # Search for the skill ID in the lines
    for i, line in enumerate(lines):
        if line.strip() == f'ID: {skill_id}':
            # Found the skill, now get the name from the "Skill:" line
            for j in range(i + 1, min(i + 10, len(lines))):
                if lines[j].startswith('Skill: '):
                    return lines[j][7:].strip()
    return "Unknown skill"

def apply_fixes():
    """Apply all fixes from the fix plan"""
    print("Loading fix plan...")
    fix_plan = load_fix_plan()

    print(f"Found {len(fix_plan)} skills to fix")

    print("\nBacking up original file...")
    backup_path = backup_file()

    print("\nReading allskills.md...")
    with open(ALLSKILLS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    changes = []
    errors = []

    print("\nApplying fixes...")
    for skill_id, fix_data in fix_plan.items():
        print(f"\nProcessing {skill_id}...")

        start_idx, end_idx, lines = find_skill_section(content, skill_id)

        if start_idx is None:
            error_msg = f"Skill {skill_id} not found in allskills.md"
            print(f"  ERROR: {error_msg}")
            errors.append({
                'skill_id': skill_id,
                'error': error_msg
            })
            continue

        # Get current and proposed dependencies
        current_deps = fix_data.get('current_dependencies', [])
        proposed_deps = fix_data.get('proposed_dependencies', [])

        # Update the dependencies line
        result = update_dependencies_line(lines, start_idx, end_idx, proposed_deps)

        if isinstance(result, tuple):
            success, old_line, new_line = result
            if success:
                print(f"  OLD: {old_line}")
                print(f"  NEW: {new_line}")

                # Reconstruct content
                content = '\n'.join(lines)

                changes.append({
                    'skill_id': skill_id,
                    'skill_name': fix_data.get('skill_name', ''),
                    'old_deps': current_deps,
                    'new_deps': proposed_deps,
                    'old_line': old_line,
                    'new_line': new_line,
                    'rationale': fix_data.get('rationale', [])
                })
            else:
                errors.append({
                    'skill_id': skill_id,
                    'error': 'Failed to update dependencies line'
                })
        else:
            errors.append({
                'skill_id': skill_id,
                'error': 'Unknown error during update'
            })

    print("\nWriting updated allskills.md...")
    with open(ALLSKILLS_PATH, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\nGenerating report...")
    generate_report(changes, errors, backup_path, fix_plan)

    return changes, errors

def generate_report(changes, errors, backup_path, fix_plan):
    """Generate a detailed report of all changes"""
    report = []

    report.append("# G5 Fixes Applied Report")
    report.append(f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"\nBackup created: `{backup_path}`")

    report.append("\n## Summary")
    report.append(f"\n- Total skills in fix plan: {len(fix_plan)}")
    report.append(f"- Successfully updated: {len(changes)}")
    report.append(f"- Errors encountered: {len(errors)}")

    if changes:
        report.append("\n## Changes Applied")
        report.append("\n| Skill ID | Skill Name | Old Dependencies | New Dependencies | Changes |")
        report.append("|----------|------------|------------------|------------------|---------|")

        for change in changes:
            old_deps = ', '.join(change['old_deps']) if change['old_deps'] else 'None'
            new_deps = ', '.join(change['new_deps']) if change['new_deps'] else 'None'

            # Calculate what changed
            old_set = set(change['old_deps'])
            new_set = set(change['new_deps'])
            added = new_set - old_set
            removed = old_set - new_set

            changes_desc = []
            if added:
                changes_desc.append(f"+{', '.join(sorted(added))}")
            if removed:
                changes_desc.append(f"-{', '.join(sorted(removed))}")
            changes_text = '; '.join(changes_desc)

            report.append(f"| {change['skill_id']} | {change['skill_name']} | {old_deps} | {new_deps} | {changes_text} |")

    if changes:
        report.append("\n## Detailed Changes")
        for i, change in enumerate(changes, 1):
            report.append(f"\n### {i}. {change['skill_id']} - {change['skill_name']}")
            report.append(f"\n**Old Dependencies:** {', '.join(change['old_deps']) if change['old_deps'] else 'None'}")
            report.append(f"\n**New Dependencies:** {', '.join(change['new_deps']) if change['new_deps'] else 'None'}")

            if change['rationale']:
                report.append("\n**Rationale:**")
                for rationale in change['rationale']:
                    report.append(f"- {rationale}")

            old_set = set(change['old_deps'])
            new_set = set(change['new_deps'])
            added = new_set - old_set
            removed = old_set - new_set

            if added:
                report.append(f"\n**Added:** {', '.join(sorted(added))}")
            if removed:
                report.append(f"\n**Removed:** {', '.join(sorted(removed))}")

    if errors:
        report.append("\n## Errors Encountered")
        for error in errors:
            report.append(f"\n- **{error['skill_id']}**: {error['error']}")

    report.append("\n## Verification")
    report.append("\nTo verify the changes:")
    report.append("1. Check that all 28 skills were processed")
    report.append("2. Review the dependencies changes in the table above")
    report.append("3. Run validation script to ensure no circular dependencies")
    report.append(f"4. If needed, restore from backup: `{backup_path}`")

    report_text = '\n'.join(report)

    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report_text)

    print(f"\nReport saved to: {REPORT_PATH}")

if __name__ == '__main__':
    print("=" * 80)
    print("Applying G5 Fixes to allskills.md")
    print("=" * 80)

    try:
        changes, errors = apply_fixes()

        print("\n" + "=" * 80)
        print("COMPLETED")
        print("=" * 80)
        print(f"Successfully updated: {len(changes)} skills")
        print(f"Errors: {len(errors)}")
        print(f"\nReport: {REPORT_PATH}")

    except Exception as e:
        print(f"\nFATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
