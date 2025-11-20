#!/usr/bin/env python3
"""
Apply fixes to Grade 7 skills based on the fix plan.
Replaces low-grade dependencies with G5/G6/G7 equivalents.
"""

import re
import json
from datetime import datetime
from collections import defaultdict

def parse_skills_file(filepath):
    """Parse the allskills.md file and extract all skills with their full text."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}

    # Split content by skill blocks
    skill_blocks = re.split(r'\n(?=ID: T\d+\.G)', content)

    # Track positions
    current_pos = 0
    for block in skill_blocks:
        if not block.strip():
            continue

        # Find position in original content
        start_pos = content.find(block, current_pos)
        if start_pos == -1:
            continue

        end_pos = start_pos + len(block)
        current_pos = end_pos

        # Extract skill ID
        id_match = re.search(r'ID:\s*(T\d+\.G\d+\.\d+)', block)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        skills[skill_id] = {
            'id': skill_id,
            'full_text': block,
            'start': start_pos,
            'end': end_pos
        }

    return skills, content

def get_grade(skill_id):
    """Extract grade number from skill ID."""
    match = re.search(r'\.G(\d+)\.', skill_id)
    return int(match.group(1)) if match else 0

def apply_dependency_fix(skill_text, replacement_map):
    """Apply dependency replacements to a skill's text."""
    # Find the dependencies section (format: Dependencies:\n* ...)
    dep_match = re.search(r'(Dependencies:\s*\n)((?:\*.*\n)*)', skill_text)

    if not dep_match:
        return skill_text, []

    prefix = dep_match.group(1)
    dep_section = dep_match.group(2)

    # Track changes
    changes_made = []

    # Replace each dependency
    new_dep_section = dep_section
    for old_dep, new_dep in replacement_map.items():
        if new_dep:  # Only replace if we have a replacement
            # Replace the dependency ID
            pattern = r'\b' + re.escape(old_dep) + r'\b'
            if re.search(pattern, new_dep_section):
                new_dep_section = re.sub(pattern, new_dep, new_dep_section)
                changes_made.append(f"{old_dep} → {new_dep}")

    # Remove duplicates from dependency list
    deps_found = re.findall(r'T\d+\.G\d+\.\d+', new_dep_section)
    unique_deps = []
    seen = set()
    for dep in deps_found:
        if dep not in seen:
            unique_deps.append(dep)
            seen.add(dep)

    # If we have duplicates, rebuild the dependency section
    if len(deps_found) != len(unique_deps):
        # Rebuild with * prefix for each line
        dep_lines = []
        for dep_id in unique_deps:
            # Find the original line to preserve the description
            for line in dep_section.split('\n'):
                if dep_id in line:
                    dep_lines.append(line)
                    break
        new_dep_section = '\n'.join(dep_lines) + '\n'
        changes_made.append(f"Removed {len(deps_found) - len(unique_deps)} duplicate dependencies")

    # Reconstruct the skill text
    before_deps = skill_text[:dep_match.start()]
    after_deps = skill_text[dep_match.end():]

    new_skill_text = before_deps + prefix + new_dep_section + after_deps

    return new_skill_text, changes_made

def remove_transitive_dependencies(skill_text, all_skills):
    """Remove transitive dependencies from a skill."""
    # Extract current dependencies (format: Dependencies:\n* ...)
    dep_match = re.search(r'Dependencies:\s*\n((?:\*.*\n)*)', skill_text)

    if not dep_match:
        return skill_text, 0

    dep_section = dep_match.group(1)
    current_deps = re.findall(r'T\d+\.G\d+\.\d+', dep_section)

    if len(current_deps) <= 1:
        return skill_text, 0

    # Build transitive closure
    transitive = set()
    for dep_id in current_deps:
        if dep_id in all_skills:
            dep_skill_text = all_skills[dep_id]['full_text']
            sub_dep_match = re.search(r'Dependencies:\s*\n((?:\*.*\n)*)', dep_skill_text)
            if sub_dep_match:
                sub_deps = re.findall(r'T\d+\.G\d+\.\d+', sub_dep_match.group(1))
                transitive.update(sub_deps)

    # Remove transitive dependencies
    minimal_deps = [dep for dep in current_deps if dep not in transitive]

    if len(minimal_deps) < len(current_deps):
        # Rebuild dependency section preserving original format
        dep_lines = []
        for dep_id in minimal_deps:
            # Find the original line to preserve the description
            for line in dep_section.split('\n'):
                if dep_id in line:
                    dep_lines.append(line)
                    break

        new_dep_section = '\n'.join(dep_lines) + '\n'

        # Reconstruct skill text
        before_deps = skill_text[:dep_match.start()]
        after_deps = skill_text[dep_match.end():]

        new_skill_text = before_deps + 'Dependencies:\n' + new_dep_section + after_deps

        return new_skill_text, len(current_deps) - len(minimal_deps)

    return skill_text, 0

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    fix_plan_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G7_FIX_PLAN.json'

    print("=" * 80)
    print("G7 FIXES APPLICATOR")
    print("=" * 80)
    print()

    # Load fix plan
    print("Loading fix plan...")
    with open(fix_plan_file, 'r', encoding='utf-8') as f:
        fix_data = json.load(f)

    fix_plan = fix_data['fix_plan']
    print(f"Fix plan loaded: {len(fix_plan)} skills to fix")
    print()

    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'{filepath}.backup_g7_{timestamp}'
    print(f"Creating backup: {backup_file}")

    with open(filepath, 'r', encoding='utf-8') as f:
        original_content = f.read()

    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(original_content)

    print("Backup created successfully")
    print()

    # Parse skills
    print("Parsing skills file...")
    skills, content = parse_skills_file(filepath)
    print(f"Total skills parsed: {len(skills)}")
    print()

    # Apply fixes
    print("Applying fixes...")
    print("=" * 80)

    modified_skills = {}
    stats = {
        'skills_modified': 0,
        'dependencies_upgraded': 0,
        'transitive_removed': 0,
        'g3_to_g5': 0,
        'g3_to_g6': 0,
        'g3_to_g7': 0,
        'g2_to_g5': 0,
        'g2_to_g6': 0,
        'g2_to_g7': 0,
        'g1_to_g5': 0,
        'g1_to_g6': 0,
        'g1_to_g7': 0
    }

    detailed_changes = []

    for skill_id, plan in fix_plan.items():
        if skill_id not in skills:
            print(f"WARNING: Skill {skill_id} not found in file")
            continue

        original_text = skills[skill_id]['full_text']
        modified_text = original_text

        # Apply dependency replacements
        replacement_map = plan['replacement_map']

        # Only process if we have valid replacements
        valid_replacements = {k: v for k, v in replacement_map.items() if v}

        if valid_replacements:
            modified_text, changes = apply_dependency_fix(modified_text, valid_replacements)

            if changes:
                stats['skills_modified'] += 1

                for old_dep, new_dep in valid_replacements.items():
                    stats['dependencies_upgraded'] += 1

                    old_grade = get_grade(old_dep)
                    new_grade = get_grade(new_dep)

                    if old_grade == 3 and new_grade == 5:
                        stats['g3_to_g5'] += 1
                    elif old_grade == 3 and new_grade == 6:
                        stats['g3_to_g6'] += 1
                    elif old_grade == 3 and new_grade == 7:
                        stats['g3_to_g7'] += 1
                    elif old_grade == 2 and new_grade == 5:
                        stats['g2_to_g5'] += 1
                    elif old_grade == 2 and new_grade == 6:
                        stats['g2_to_g6'] += 1
                    elif old_grade == 2 and new_grade == 7:
                        stats['g2_to_g7'] += 1
                    elif old_grade == 1 and new_grade == 5:
                        stats['g1_to_g5'] += 1
                    elif old_grade == 1 and new_grade == 6:
                        stats['g1_to_g6'] += 1
                    elif old_grade == 1 and new_grade == 7:
                        stats['g1_to_g7'] += 1

                detailed_changes.append({
                    'skill_id': skill_id,
                    'title': plan['title'],
                    'changes': changes
                })

                print(f"✓ {skill_id}: {len(changes)} changes")
                for change in changes:
                    print(f"    {change}")

        # Remove transitive dependencies
        modified_text, transitive_count = remove_transitive_dependencies(modified_text, skills)
        if transitive_count > 0:
            stats['transitive_removed'] += transitive_count
            print(f"  Removed {transitive_count} transitive dependencies")

        if modified_text != original_text:
            modified_skills[skill_id] = modified_text

    print()
    print(f"Total skills modified: {stats['skills_modified']}")
    print()

    # Reconstruct the file
    print("Reconstructing allskills.md...")

    new_content = content
    # Sort by position (reverse) to avoid offset issues
    sorted_skills = sorted(skills.items(), key=lambda x: x[1]['start'], reverse=True)

    for skill_id, skill_data in sorted_skills:
        if skill_id in modified_skills:
            new_content = (
                new_content[:skill_data['start']] +
                modified_skills[skill_id] +
                new_content[skill_data['end']:]
            )

    # Write the updated file
    print("Writing updated file...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("File updated successfully")
    print()

    # Generate detailed report
    report_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G7_FIXES_APPLIED_REPORT.md'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Grade 7 Fixes Applied Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("## Summary Statistics\n\n")
        f.write(f"- **Total skills modified:** {stats['skills_modified']}\n")
        f.write(f"- **Total dependencies upgraded:** {stats['dependencies_upgraded']}\n")
        f.write(f"- **Total transitive dependencies removed:** {stats['transitive_removed']}\n\n")

        f.write("## Dependency Upgrade Breakdown\n\n")
        f.write(f"- **G3 → G5:** {stats['g3_to_g5']}\n")
        f.write(f"- **G3 → G6:** {stats['g3_to_g6']}\n")
        f.write(f"- **G3 → G7:** {stats['g3_to_g7']}\n")
        f.write(f"- **G2 → G5:** {stats['g2_to_g5']}\n")
        f.write(f"- **G2 → G6:** {stats['g2_to_g6']}\n")
        f.write(f"- **G2 → G7:** {stats['g2_to_g7']}\n")
        f.write(f"- **G1 → G5:** {stats['g1_to_g5']}\n")
        f.write(f"- **G1 → G6:** {stats['g1_to_g6']}\n")
        f.write(f"- **G1 → G7:** {stats['g1_to_g7']}\n\n")

        f.write("## Detailed Changes\n\n")

        for change in detailed_changes:
            f.write(f"### {change['skill_id']}: {change['title']}\n\n")
            for c in change['changes']:
                f.write(f"- {c}\n")
            f.write("\n")

    print(f"Detailed report saved to: {report_file}")
    print()

    # Print final statistics
    print("=" * 80)
    print("FINAL STATISTICS")
    print("=" * 80)
    print(f"Skills modified: {stats['skills_modified']}")
    print(f"Dependencies upgraded: {stats['dependencies_upgraded']}")
    print(f"  G3 → G5: {stats['g3_to_g5']}")
    print(f"  G3 → G6: {stats['g3_to_g6']}")
    print(f"  G3 → G7: {stats['g3_to_g7']}")
    print(f"  G2 → G5: {stats['g2_to_g5']}")
    print(f"  G2 → G6: {stats['g2_to_g6']}")
    print(f"  G2 → G7: {stats['g2_to_g7']}")
    print(f"  G1 → G5: {stats['g1_to_g5']}")
    print(f"  G1 → G6: {stats['g1_to_g6']}")
    print(f"  G1 → G7: {stats['g1_to_g7']}")
    print(f"Transitive dependencies removed: {stats['transitive_removed']}")
    print()
    print("=" * 80)
    print("COMPLETE - All fixes applied successfully!")
    print("=" * 80)

if __name__ == '__main__':
    main()
