#!/usr/bin/env python3
"""
Apply Grade 1 validated dependencies to allskills.md
"""

import re
from collections import defaultdict

def parse_allskills(filepath):
    """Parse allskills.md and extract skill info"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Build map of skill ID -> title
    skill_titles = {}
    skill_pattern = r'ID:\s+(T\d+\.G[K\d]+\.\d+)\s+Topic:[^\n]+\s+Skill:\s+([^\n]+)'

    for match in re.finditer(skill_pattern, content):
        skill_id = match.group(1)
        title = match.group(2)
        skill_titles[skill_id] = title

    print(f"Found {len(skill_titles)} skills in allskills.md")
    return content, skill_titles

def parse_dependencies_file(filepath):
    """Parse the validated dependencies file"""
    deps_to_add = defaultdict(list)

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            parts = line.split()
            if len(parts) == 3 and parts[1] == 'ADD_DEP':
                skill_id = parts[0]
                dep_id = parts[2]
                deps_to_add[skill_id].append(dep_id)

    total_deps = sum(len(deps) for deps in deps_to_add.values())
    print(f"Parsed {total_deps} dependencies for {len(deps_to_add)} skills")
    return deps_to_add

def find_skill_section(content, skill_id):
    """Find the start and end positions of a skill section"""
    # Pattern to match skill ID line
    pattern = rf'^ID:\s+{re.escape(skill_id)}\s*$'

    match = re.search(pattern, content, re.MULTILINE)
    if not match:
        return None, None

    start = match.start()

    # Find the next skill (next ID: line) or end of file
    next_skill = re.search(r'^ID:\s+T\d+\.G[K\d]+\.\d+\s*$', content[start + len(match.group(0)):], re.MULTILINE)
    if next_skill:
        end = start + len(match.group(0)) + next_skill.start()
    else:
        end = len(content)

    return start, end

def get_existing_dependencies(skill_section):
    """Extract existing dependency IDs from a skill section"""
    deps = set()
    # Pattern: * T01.GK.02: Title
    dep_pattern = r'^\*\s+(T\d+\.G[K\d]+\.\d+):'

    for line in skill_section.split('\n'):
        match = re.match(dep_pattern, line.strip())
        if match:
            deps.add(match.group(1))

    return deps

def apply_dependencies(content, skill_titles, deps_to_add):
    """Apply dependencies to the content"""
    stats = {
        'skills_modified': 0,
        'deps_added': 0,
        'skills_not_found': [],
        'deps_missing_title': [],
        'deps_already_exist': 0
    }

    # Process each skill that needs dependencies added
    for skill_id in sorted(deps_to_add.keys()):
        new_deps = deps_to_add[skill_id]

        # Find the skill section
        start, end = find_skill_section(content, skill_id)
        if start is None:
            print(f"WARNING: Skill {skill_id} not found")
            stats['skills_not_found'].append(skill_id)
            continue

        skill_section = content[start:end]

        # Check existing dependencies
        existing_deps = get_existing_dependencies(skill_section)

        # Filter out dependencies that already exist
        deps_to_actually_add = [dep for dep in new_deps if dep not in existing_deps]

        if len(deps_to_actually_add) < len(new_deps):
            stats['deps_already_exist'] += len(new_deps) - len(deps_to_actually_add)

        if not deps_to_actually_add:
            continue

        # Find or create Dependencies section
        deps_section_match = re.search(r'\nDependencies:\s*\n', skill_section)

        new_dep_lines = []
        for dep_id in deps_to_actually_add:
            if dep_id not in skill_titles:
                print(f"WARNING: No title found for dependency {dep_id}")
                stats['deps_missing_title'].append(dep_id)
                continue

            dep_title = skill_titles[dep_id]
            new_dep_lines.append(f"* {dep_id}: {dep_title}")

        if not new_dep_lines:
            continue

        if deps_section_match:
            # Insert after "Dependencies:\n"
            insert_pos = start + deps_section_match.end()

            # Find where to insert (after existing deps or at the beginning)
            deps_start = deps_section_match.end()

            # Find the end of existing dependencies (blank line or next section)
            remaining = skill_section[deps_start:]
            blank_line = re.search(r'\n\s*\n', remaining)

            if existing_deps:
                # Insert after existing dependencies
                last_dep_line = None
                for line_match in re.finditer(r'^\*[^\n]+\n', remaining, re.MULTILINE):
                    last_dep_line = line_match

                if last_dep_line:
                    insert_offset = deps_start + last_dep_line.end()
                else:
                    insert_offset = deps_start
            else:
                insert_offset = deps_start

            insert_pos = start + insert_offset
            new_content = '\n'.join(new_dep_lines) + '\n'
            content = content[:insert_pos] + new_content + content[insert_pos:]

        else:
            # Add Dependencies section after Description line
            desc_match = re.search(r'\nDescription:[^\n]+\n', skill_section)
            if desc_match:
                insert_pos = start + desc_match.end()
                new_content = '\nDependencies:\n' + '\n'.join(new_dep_lines) + '\n'
                content = content[:insert_pos] + new_content + content[insert_pos:]
            else:
                print(f"WARNING: Could not find Description line for {skill_id}")
                continue

        stats['skills_modified'] += 1
        stats['deps_added'] += len(new_dep_lines)
        print(f"Added {len(new_dep_lines)} dependencies to {skill_id}")

    return content, stats

def main():
    allskills_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    deps_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE1_VALIDATED_NEW_DEPS.txt'
    output_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Step 1: Parsing allskills.md...")
    content, skill_titles = parse_allskills(allskills_path)

    print("\nStep 2: Parsing dependencies file...")
    deps_to_add = parse_dependencies_file(deps_path)

    print("\nStep 3: Applying dependencies...")
    new_content, stats = apply_dependencies(content, skill_titles, deps_to_add)

    print("\nStep 4: Writing updated file...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Skills modified: {stats['skills_modified']}")
    print(f"New dependencies added: {stats['deps_added']}")
    print(f"Dependencies already existed: {stats['deps_already_exist']}")
    print(f"Skills not found: {len(stats['skills_not_found'])}")
    print(f"Dependencies missing titles: {len(stats['deps_missing_title'])}")

    if stats['skills_not_found']:
        print("\nSkills not found:")
        for skill_id in stats['skills_not_found']:
            print(f"  - {skill_id}")

    if stats['deps_missing_title']:
        print("\nDependencies missing titles:")
        for dep_id in stats['deps_missing_title']:
            print(f"  - {dep_id}")

    print("\nDone!")

if __name__ == '__main__':
    main()
