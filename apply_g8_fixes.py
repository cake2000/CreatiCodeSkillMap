#!/usr/bin/env python3
"""
Apply comprehensive fixes to Grade 8 (G8) skills based on analysis report.

This script fixes:
1. Circular dependencies in G1 skills (self-references)
2. Grade constraint violations (G8 depends on G5 or lower - remove or upgrade to G6+)
3. Transitive dependencies in G8 skills

Based on G8_ANALYSIS_REPORT_FINAL.json
"""

import re
import json
from datetime import datetime
from collections import defaultdict

def parse_skills_file(filepath):
    """Parse allskills.md and extract all skills with their full text."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}

    # Split by skill blocks
    skill_blocks = re.split(r'\n(?=ID: T\d+\.G)', content)

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

        # Extract title
        title_match = re.search(r'Skill:\s*(.+?)(?:\n|$)', block)
        title = title_match.group(1).strip() if title_match else "Unknown"

        # Extract dependencies
        deps_match = re.search(r'Dependencies:\s*\n((?:\*.*\n)*)', block)
        if deps_match:
            deps_str = deps_match.group(1)
            dependencies = re.findall(r'T\d+\.G\d+\.\d+', deps_str)
        else:
            dependencies = []

        skills[skill_id] = {
            'id': skill_id,
            'title': title,
            'full_text': block,
            'dependencies': dependencies,
            'start': start_pos,
            'end': end_pos
        }

    return skills, content

def get_grade(skill_id):
    """Extract grade number from skill ID."""
    match = re.search(r'\.G(\d+)\.', skill_id)
    return int(match.group(1)) if match else 0

def get_topic(skill_id):
    """Extract topic from skill ID."""
    match = re.search(r'^(T\d+)\.', skill_id)
    return match.group(1) if match else None

def fix_self_reference(skill_text, skill_id):
    """Remove self-references from a skill's dependencies."""
    deps_match = re.search(r'(Dependencies:\s*\n)((?:\*.*\n)*)', skill_text)

    if not deps_match:
        return skill_text, False

    prefix = deps_match.group(1)
    deps_section = deps_match.group(2)

    # Find all dependencies
    dep_lines = [line for line in deps_section.split('\n') if line.strip().startswith('*')]

    # Remove lines that reference the skill itself
    cleaned_lines = []
    removed = False
    for line in dep_lines:
        if skill_id in line:
            removed = True
        else:
            cleaned_lines.append(line)

    if not removed:
        return skill_text, False

    # Reconstruct
    if cleaned_lines:
        new_deps_section = '\n'.join(cleaned_lines) + '\n'
    else:
        # Remove the entire Dependencies section if no deps left
        before_deps = skill_text[:deps_match.start()]
        after_deps = skill_text[deps_match.end():]
        return before_deps + after_deps, True

    before_deps = skill_text[:deps_match.start()]
    after_deps = skill_text[deps_match.end():]
    new_skill_text = before_deps + prefix + new_deps_section + after_deps

    return new_skill_text, True

def find_replacement_dependency(old_dep, topic, all_skills):
    """
    Find a G6+ replacement for a low-grade dependency.
    Look for skills in the same topic with similar concepts.
    """
    old_grade = get_grade(old_dep)
    old_topic = get_topic(old_dep)

    # Get the title of the old dependency for context
    old_title = all_skills.get(old_dep, {}).get('title', '').lower()

    # Try to find a G6 or G7 skill in the same topic
    candidates = []
    for skill_id, skill_data in all_skills.items():
        if get_topic(skill_id) != old_topic:
            continue

        skill_grade = get_grade(skill_id)
        if skill_grade < 6:
            continue

        # Prioritize G6, then G7
        if skill_grade in [6, 7]:
            candidates.append((skill_id, skill_grade, skill_data['title']))

    # Sort by grade (prefer G6) and return first match
    if candidates:
        candidates.sort(key=lambda x: x[1])
        return candidates[0][0]

    return None

def upgrade_low_grade_dependencies(skill_text, skill_id, all_skills):
    """
    For G8 skills, remove or upgrade dependencies on grades < G6.
    Strategy:
    - For dependencies on G5 or lower: try to find G6+ replacement in same topic
    - If no replacement found, remove the dependency (document this)
    """
    deps_match = re.search(r'(Dependencies:\s*\n)((?:\*.*\n)*)', skill_text)

    if not deps_match:
        return skill_text, []

    prefix = deps_match.group(1)
    deps_section = deps_match.group(2)

    # Parse all dependency lines
    dep_lines = [line for line in deps_section.split('\n') if line.strip().startswith('*')]

    new_dep_lines = []
    changes = []
    removed_deps = []

    for line in dep_lines:
        dep_id_match = re.search(r'(T\d+\.G\d+\.\d+)', line)
        if not dep_id_match:
            new_dep_lines.append(line)
            continue

        dep_id = dep_id_match.group(1)
        dep_grade = get_grade(dep_id)

        # If dependency is G6 or higher, keep it
        if dep_grade >= 6:
            new_dep_lines.append(line)
            continue

        # Dependency is G5 or lower - try to find replacement
        topic = get_topic(skill_id)
        replacement = find_replacement_dependency(dep_id, topic, all_skills)

        if replacement:
            # Replace dependency ID in the line
            new_line = line.replace(dep_id, replacement)
            # Update the description if it exists
            if replacement in all_skills:
                new_desc = all_skills[replacement]['title']
                # Replace description after the colon
                if ':' in new_line:
                    new_line = f"* {replacement}: {new_desc}"
            new_dep_lines.append(new_line)
            changes.append(f"Upgraded {dep_id} (G{dep_grade}) → {replacement} (G{get_grade(replacement)})")
        else:
            # No replacement found - remove this dependency
            removed_deps.append(dep_id)
            changes.append(f"Removed {dep_id} (G{dep_grade}) - no suitable G6+ replacement")

    if not changes:
        return skill_text, []

    # Remove duplicates from new_dep_lines
    seen_deps = set()
    unique_dep_lines = []
    for line in new_dep_lines:
        dep_match = re.search(r'(T\d+\.G\d+\.\d+)', line)
        if dep_match:
            dep = dep_match.group(1)
            if dep not in seen_deps:
                seen_deps.add(dep)
                unique_dep_lines.append(line)
        else:
            unique_dep_lines.append(line)

    # Reconstruct skill text
    if unique_dep_lines:
        new_deps_section = '\n'.join(unique_dep_lines) + '\n'
        before_deps = skill_text[:deps_match.start()]
        after_deps = skill_text[deps_match.end():]
        new_skill_text = before_deps + prefix + new_deps_section + after_deps
    else:
        # Remove entire Dependencies section if empty
        before_deps = skill_text[:deps_match.start()]
        after_deps = skill_text[deps_match.end():]
        new_skill_text = before_deps + after_deps

    return new_skill_text, changes

def remove_transitive_dependencies(skill_text, skill_id, all_skills):
    """Remove dependencies that are transitively reachable."""
    deps_match = re.search(r'(Dependencies:\s*\n)((?:\*.*\n)*)', skill_text)

    if not deps_match:
        return skill_text, []

    prefix = deps_match.group(1)
    deps_section = deps_match.group(2)

    # Get current direct dependencies
    current_deps = re.findall(r'T\d+\.G\d+\.\d+', deps_section)

    if len(current_deps) <= 1:
        return skill_text, []

    # Build set of indirect dependencies (dependencies of dependencies)
    indirect_deps = set()
    for dep_id in current_deps:
        if dep_id in all_skills:
            indirect_deps.update(all_skills[dep_id]['dependencies'])

    # Find redundant dependencies (direct deps that are also indirect)
    redundant = [dep for dep in current_deps if dep in indirect_deps]

    if not redundant:
        return skill_text, []

    # Remove redundant dependencies
    dep_lines = [line for line in deps_section.split('\n') if line.strip().startswith('*')]
    new_dep_lines = []

    for line in dep_lines:
        dep_match = re.search(r'(T\d+\.G\d+\.\d+)', line)
        if dep_match:
            dep_id = dep_match.group(1)
            if dep_id not in redundant:
                new_dep_lines.append(line)
        else:
            new_dep_lines.append(line)

    changes = [f"Removed transitive dependency: {dep}" for dep in redundant]

    # Reconstruct
    if new_dep_lines:
        new_deps_section = '\n'.join(new_dep_lines) + '\n'
        before_deps = skill_text[:deps_match.start()]
        after_deps = skill_text[deps_match.end():]
        new_skill_text = before_deps + prefix + new_deps_section + after_deps
    else:
        before_deps = skill_text[:deps_match.start()]
        after_deps = skill_text[deps_match.end():]
        new_skill_text = before_deps + after_deps

    return new_skill_text, changes

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    analysis_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G8_ANALYSIS_REPORT_FINAL.json'

    print("=" * 80)
    print("GRADE 8 COMPREHENSIVE FIX APPLICATOR")
    print("=" * 80)
    print()

    # Load analysis report
    print("Loading analysis report...")
    with open(analysis_file, 'r', encoding='utf-8') as f:
        analysis = json.load(f)

    print(f"Total G8 skills: {analysis['total_g8_skills']}")
    print(f"High priority issues: {analysis.get('high_priority_count', len(analysis.get('high_priority_issues', [])))}")
    print(f"Medium priority issues: {analysis.get('medium_priority_count', len(analysis.get('medium_priority_issues', [])))}")
    print()

    # Create backup
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f'{filepath}.backup_g8_{timestamp}'
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

    # Track all changes
    modified_skills = {}
    detailed_changes = []

    stats = {
        'g1_self_refs_fixed': 0,
        'g8_skills_upgraded': 0,
        'dependencies_upgraded': 0,
        'dependencies_removed': 0,
        'transitive_deps_removed': 0,
        'g5_to_g6': 0,
        'g5_to_g7': 0,
        'g4_to_g6': 0,
        'g4_to_g7': 0,
        'g3_to_g6': 0,
        'g3_to_g7': 0,
        'g2_to_g6': 0,
        'g2_to_g7': 0,
        'g1_to_g6': 0,
        'g1_to_g7': 0
    }

    # Phase 1: Fix G1 self-references
    print("PHASE 1: Fixing G1 self-references")
    print("=" * 80)

    g1_targets = ['T25.G1.01', 'T34.G1.01', 'T35.G1.01', 'T36.G1.01']

    for skill_id in g1_targets:
        if skill_id not in skills:
            print(f"WARNING: {skill_id} not found")
            continue

        original_text = skills[skill_id]['full_text']
        new_text, changed = fix_self_reference(original_text, skill_id)

        if changed:
            modified_skills[skill_id] = new_text
            skills[skill_id]['full_text'] = new_text
            stats['g1_self_refs_fixed'] += 1
            print(f"✓ {skill_id}: Removed self-reference")
            detailed_changes.append({
                'skill_id': skill_id,
                'title': skills[skill_id]['title'],
                'phase': 'G1 Self-Reference Fix',
                'changes': ['Removed self-reference from dependencies']
            })
        else:
            print(f"  {skill_id}: No self-reference found (already clean)")

    print()

    # Phase 2: Upgrade low-grade dependencies in G8 skills
    print("PHASE 2: Upgrading low-grade dependencies in G8 skills")
    print("=" * 80)

    g8_skills = [k for k in skills.keys() if get_grade(k) == 8]
    print(f"Processing {len(g8_skills)} G8 skills...")
    print()

    for skill_id in sorted(g8_skills):
        skill = skills[skill_id]
        original_text = skill['full_text']

        new_text, changes = upgrade_low_grade_dependencies(original_text, skill_id, skills)

        if changes:
            # Update skills dict for transitive dependency check
            skills[skill_id]['full_text'] = new_text
            # Parse new dependencies
            deps_match = re.search(r'Dependencies:\s*\n((?:\*.*\n)*)', new_text)
            if deps_match:
                skills[skill_id]['dependencies'] = re.findall(r'T\d+\.G\d+\.\d+', deps_match.group(1))
            else:
                skills[skill_id]['dependencies'] = []

            modified_skills[skill_id] = new_text
            stats['g8_skills_upgraded'] += 1

            # Count upgrade types
            for change in changes:
                if 'Upgraded' in change:
                    stats['dependencies_upgraded'] += 1
                    # Parse grades
                    match = re.search(r'G(\d+).*G(\d+)', change)
                    if match:
                        old_g = int(match.group(1))
                        new_g = int(match.group(2))
                        key = f'g{old_g}_to_g{new_g}'
                        if key in stats:
                            stats[key] += 1
                elif 'Removed' in change:
                    stats['dependencies_removed'] += 1

            print(f"✓ {skill_id}: {len(changes)} changes")
            for change in changes:
                print(f"    {change}")

            detailed_changes.append({
                'skill_id': skill_id,
                'title': skill['title'],
                'phase': 'G8 Dependency Upgrade',
                'changes': changes
            })

    print()
    print(f"G8 skills modified: {stats['g8_skills_upgraded']}")
    print()

    # Phase 3: Remove transitive dependencies from specific G8 skills
    print("PHASE 3: Removing transitive dependencies")
    print("=" * 80)

    transitive_targets = [
        'T25.G8.02', 'T25.G8.04',
        'T34.G8.01', 'T34.G8.03',
        'T35.G8.02', 'T35.G8.03', 'T35.G8.04',
        'T36.G8.04'
    ]

    for skill_id in transitive_targets:
        if skill_id not in skills:
            print(f"WARNING: {skill_id} not found")
            continue

        # Get the current text (might have been modified in phase 2)
        current_text = skills[skill_id]['full_text']

        new_text, changes = remove_transitive_dependencies(current_text, skill_id, skills)

        if changes:
            modified_skills[skill_id] = new_text
            skills[skill_id]['full_text'] = new_text
            stats['transitive_deps_removed'] += len(changes)

            print(f"✓ {skill_id}: {len(changes)} transitive dependencies removed")
            for change in changes:
                print(f"    {change}")

            # Add to existing detailed changes or create new entry
            existing = next((c for c in detailed_changes if c['skill_id'] == skill_id), None)
            if existing:
                existing['changes'].extend(changes)
            else:
                detailed_changes.append({
                    'skill_id': skill_id,
                    'title': skills[skill_id]['title'],
                    'phase': 'Transitive Dependency Removal',
                    'changes': changes
                })
        else:
            print(f"  {skill_id}: No transitive dependencies found")

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

    # Write updated file
    print("Writing updated file...")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("File updated successfully")
    print()

    # Generate detailed report
    report_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G8_FIXES_APPLIED_REPORT.md'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Grade 8 Fixes Applied Report\n\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write("## Summary Statistics\n\n")
        f.write(f"- **G1 self-references fixed:** {stats['g1_self_refs_fixed']}\n")
        f.write(f"- **G8 skills modified:** {stats['g8_skills_upgraded']}\n")
        f.write(f"- **Dependencies upgraded:** {stats['dependencies_upgraded']}\n")
        f.write(f"- **Dependencies removed:** {stats['dependencies_removed']}\n")
        f.write(f"- **Transitive dependencies removed:** {stats['transitive_deps_removed']}\n\n")

        f.write("## Dependency Upgrade Breakdown\n\n")
        f.write(f"- **G5 → G6:** {stats['g5_to_g6']}\n")
        f.write(f"- **G5 → G7:** {stats['g5_to_g7']}\n")
        f.write(f"- **G4 → G6:** {stats['g4_to_g6']}\n")
        f.write(f"- **G4 → G7:** {stats['g4_to_g7']}\n")
        f.write(f"- **G3 → G6:** {stats['g3_to_g6']}\n")
        f.write(f"- **G3 → G7:** {stats['g3_to_g7']}\n")
        f.write(f"- **G2 → G6:** {stats['g2_to_g6']}\n")
        f.write(f"- **G2 → G7:** {stats['g2_to_g7']}\n")
        f.write(f"- **G1 → G6:** {stats['g1_to_g6']}\n")
        f.write(f"- **G1 → G7:** {stats['g1_to_g7']}\n\n")

        f.write("## Detailed Changes by Skill\n\n")

        for change in detailed_changes:
            f.write(f"### {change['skill_id']}: {change['title']}\n\n")
            f.write(f"**Phase:** {change['phase']}\n\n")
            for c in change['changes']:
                f.write(f"- {c}\n")
            f.write("\n")

    print(f"Detailed report saved to: {report_file}")
    print()

    # Print final statistics
    print("=" * 80)
    print("FINAL STATISTICS")
    print("=" * 80)
    print(f"G1 self-references fixed: {stats['g1_self_refs_fixed']}")
    print(f"G8 skills modified: {stats['g8_skills_upgraded']}")
    print(f"Dependencies upgraded: {stats['dependencies_upgraded']}")
    print(f"  G5 → G6: {stats['g5_to_g6']}")
    print(f"  G5 → G7: {stats['g5_to_g7']}")
    print(f"  G4 → G6: {stats['g4_to_g6']}")
    print(f"  G4 → G7: {stats['g4_to_g7']}")
    print(f"  G3 → G6: {stats['g3_to_g6']}")
    print(f"  G3 → G7: {stats['g3_to_g7']}")
    print(f"  G2 → G6: {stats['g2_to_g6']}")
    print(f"  G2 → G7: {stats['g2_to_g7']}")
    print(f"  G1 → G6: {stats['g1_to_g6']}")
    print(f"  G1 → G7: {stats['g1_to_g7']}")
    print(f"Dependencies removed (no G6+ replacement): {stats['dependencies_removed']}")
    print(f"Transitive dependencies removed: {stats['transitive_deps_removed']}")
    print()
    print(f"Total skills modified: {len(modified_skills)}")
    print()
    print("=" * 80)
    print("COMPLETE - All G8 fixes applied successfully!")
    print("=" * 80)

if __name__ == '__main__':
    main()
