#!/usr/bin/env python3
"""
Merge dependencies from K-2, G3, and G4-8 files into allskills.md
"""

import re
from collections import defaultdict

def build_skill_name_map(base_filepath):
    """Build a comprehensive map of all skill IDs to names from the base file."""
    skill_names = {}
    with open(base_filepath, 'r', encoding='utf-8') as f:
        current_id = None
        for line in f:
            line = line.rstrip()
            id_match = re.match(r'^ID:\s*(T\d+\.G[K0-9]+\.\d+)', line)
            if id_match:
                current_id = id_match.group(1)
            elif current_id and line.startswith('Skill:'):
                skill_name = line.replace('Skill:', '').strip()
                skill_names[current_id] = skill_name
    return skill_names

def parse_skill_file(filepath, skill_name_map):
    """Parse a skill file and extract skills with their dependencies."""
    skills = {}
    current_skill = None
    current_deps = []

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()

            # Match skill ID
            id_match = re.match(r'^ID:\s*(T\d+\.G[K0-9]+\.\d+)', line)
            if id_match:
                # Save previous skill if exists
                if current_skill:
                    skills[current_skill] = current_deps

                current_skill = id_match.group(1)
                current_deps = []
                continue

            # Match dependency or dependencies header
            if current_skill:
                if line.startswith('Dependencies:') or line.startswith('Dependency:'):
                    continue

                # Match dependency line with description: * SKILL_ID: Description
                dep_match = re.match(r'^\*\s*(T\d+\.G[K0-9]+\.\d+):\s*(.+)', line)
                if dep_match:
                    current_deps.append((dep_match.group(1), dep_match.group(2)))
                    continue

                # Match dependency line without description: * SKILL_ID
                dep_match_no_desc = re.match(r'^\*\s*(T\d+\.G[K0-9]+\.\d+)\s*$', line)
                if dep_match_no_desc:
                    dep_id = dep_match_no_desc.group(1)
                    # Look up the skill name from comprehensive map
                    dep_name = skill_name_map.get(dep_id, "Unknown skill")
                    current_deps.append((dep_id, dep_name))

        # Save last skill
        if current_skill:
            skills[current_skill] = current_deps

    return skills

def parse_base_file(filepath):
    """Parse the base allskills.md file and return list of skill blocks."""
    skills = []
    current_skill = []
    current_id = None

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()

            # Match skill ID
            id_match = re.match(r'^ID:\s*(T\d+\.G[K0-9]+\.\d+)', line)
            if id_match:
                # Save previous skill if exists
                if current_skill:
                    skills.append({
                        'id': current_id,
                        'lines': current_skill
                    })

                current_id = id_match.group(1)
                current_skill = [line]
                continue

            if current_skill:
                current_skill.append(line)

        # Save last skill
        if current_skill:
            skills.append({
                'id': current_id,
                'lines': current_skill
            })

    return skills

def main():
    # Build comprehensive skill name map from base file
    print("Building skill name map from base file...")
    skill_name_map = build_skill_name_map('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    print(f"Found {len(skill_name_map)} skill names")

    # Parse all dependency files
    print("\nParsing K-2 dependencies...")
    k2_deps = parse_skill_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/k2_skills_with_dependencies.md', skill_name_map)
    print(f"Found {len(k2_deps)} K-2 skills with dependencies")

    print("Parsing G3 dependencies...")
    g3_deps = parse_skill_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g3_skills_with_dependencies.md', skill_name_map)
    print(f"Found {len(g3_deps)} G3 skills with dependencies")

    print("Parsing G4-8 dependencies...")
    g48_deps = parse_skill_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g4-8_skills_with_dependencies.md', skill_name_map)
    print(f"Found {len(g48_deps)} G4-8 skills with dependencies")

    # Merge all dependencies
    all_deps = {}
    all_deps.update(k2_deps)
    all_deps.update(g3_deps)
    all_deps.update(g48_deps)

    print(f"\nTotal unique skills with dependencies: {len(all_deps)}")

    # Parse base file
    print("\nParsing base allskills.md...")
    base_skills = parse_base_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    print(f"Found {len(base_skills)} skills in base file")

    # Generate merged output
    print("\nGenerating merged file...")
    output_lines = []
    skills_with_deps = 0
    skills_without_deps = 0

    for skill in base_skills:
        skill_id = skill['id']
        skill_lines = skill['lines']

        # Remove any existing Dependencies/Dependency lines from base
        filtered_lines = []
        skip_deps = False
        for line in skill_lines:
            if line.startswith('Dependencies:') or line.startswith('Dependency:'):
                skip_deps = True
                continue
            if skip_deps and line.startswith('* '):
                continue
            skip_deps = False
            filtered_lines.append(line)

        # Add skill ID and other lines
        output_lines.extend(filtered_lines)

        # Add dependencies if they exist
        if skill_id in all_deps and all_deps[skill_id]:
            deps = all_deps[skill_id]
            output_lines.append('Dependencies:')
            for dep_id, dep_desc in deps:
                output_lines.append(f'* {dep_id}: {dep_desc}')
            skills_with_deps += 1
        else:
            skills_without_deps += 1

        # Add blank line separator
        output_lines.append('')
        output_lines.append('')

    # Write output file
    output_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills_merged.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))

    print(f"\nMerged file written to: {output_path}")
    print(f"Skills with dependencies: {skills_with_deps}")
    print(f"Skills without dependencies: {skills_without_deps}")
    print(f"Total skills: {len(base_skills)}")

    # Calculate statistics by grade
    grade_stats = defaultdict(lambda: {'total': 0, 'with_deps': 0, 'dep_count': 0})

    for skill_id, deps in all_deps.items():
        # Extract grade from skill ID (e.g., T01.GK.01 -> GK)
        match = re.match(r'T\d+\.(G[K0-9]+)\.\d+', skill_id)
        if match:
            grade = match.group(1)
            grade_stats[grade]['total'] += 1
            if deps:
                grade_stats[grade]['with_deps'] += 1
                grade_stats[grade]['dep_count'] += len(deps)

    print("\n" + "="*60)
    print("STATISTICS BY GRADE")
    print("="*60)

    for grade in sorted(grade_stats.keys()):
        stats = grade_stats[grade]
        avg_deps = stats['dep_count'] / stats['with_deps'] if stats['with_deps'] > 0 else 0
        print(f"\nGrade {grade}:")
        print(f"  Total skills with dependencies: {stats['with_deps']}")
        print(f"  Total dependencies: {stats['dep_count']}")
        print(f"  Average dependencies per skill: {avg_deps:.2f}")

if __name__ == '__main__':
    main()
