#!/usr/bin/env python3
"""
Combine all skills from allskills.md with dependencies from K-2 and G3 files.
"""

import re
from collections import defaultdict

def parse_skills_file(filepath, parse_deps=True):
    """Parse a skills file and return a dict of skill_id -> skill_dict."""
    skills = {}
    current_skill = None
    in_dependencies = False

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')

            if line.startswith('ID: '):
                # Save previous skill if it exists
                if current_skill:
                    skills[current_skill['id']] = current_skill

                # Start new skill
                skill_id = line[4:].strip()
                current_skill = {
                    'id': skill_id,
                    'topic': '',
                    'skill': '',
                    'description': '',
                    'dependencies': []
                }
                in_dependencies = False

            elif current_skill:
                if line.startswith('Topic: '):
                    current_skill['topic'] = line[7:]
                    in_dependencies = False
                elif line.startswith('Skill: '):
                    current_skill['skill'] = line[7:]
                    in_dependencies = False
                elif line.startswith('Description: '):
                    current_skill['description'] = line[13:]
                    in_dependencies = False
                elif parse_deps and (line.startswith('Dependencies:') or line.startswith('Dependency:')):
                    # Start collecting dependencies
                    in_dependencies = True
                elif parse_deps and line.startswith('* ') and in_dependencies:
                    # Dependency line - handle both formats:
                    # "* T01.GK.01: Skill name" (K-2 format)
                    # "* T01.GK.01" (G3 format - no skill name)
                    dep_match = re.match(r'\* ([^:]+)(?:: (.+))?', line)
                    if dep_match:
                        dep_id = dep_match.group(1).strip()
                        dep_name = dep_match.group(2).strip() if dep_match.group(2) else ''
                        current_skill['dependencies'].append({
                            'id': dep_id,
                            'name': dep_name
                        })
                elif line.strip() == '':
                    # Empty line might end dependencies
                    pass
                else:
                    in_dependencies = False

        # Add the last skill
        if current_skill:
            skills[current_skill['id']] = current_skill

    return skills

def extract_grade_from_id(skill_id):
    """Extract grade level from skill ID (e.g., 'GK', 'G1', 'G2', etc.)."""
    match = re.search(r'\.([GK][0-9K]?)\.', skill_id)
    if match:
        return match.group(1)
    return None

def sort_key(skill):
    """Generate a sort key for a skill."""
    # Extract topic number (T01, T02, etc.)
    topic_match = re.match(r'T(\d+)', skill['id'])
    topic_num = int(topic_match.group(1)) if topic_match else 0

    # Extract grade
    grade = extract_grade_from_id(skill['id'])
    grade_order = {
        'GK': 0, 'G1': 1, 'G2': 2, 'G3': 3, 'G4': 4,
        'G5': 5, 'G6': 6, 'G7': 7, 'G8': 8
    }
    grade_num = grade_order.get(grade, 99)

    # Extract skill number
    skill_match = re.search(r'\.(\d+)$', skill['id'])
    skill_num = int(skill_match.group(1)) if skill_match else 0

    return (topic_num, grade_num, skill_num)

def format_skill(skill):
    """Format a skill for output."""
    lines = []
    lines.append(f"ID: {skill['id']}")
    lines.append(f"Topic: {skill['topic']}")
    lines.append(f"Skill: {skill['skill']}")
    lines.append(f"Description: {skill['description']}")

    if skill['dependencies']:
        lines.append('Dependencies:')
        for dep in skill['dependencies']:
            if dep['name']:
                lines.append(f"* {dep['id']}: {dep['name']}")
            else:
                lines.append(f"* {dep['id']}")

    lines.append('')  # Blank line
    lines.append('')  # Another blank line for spacing

    return '\n'.join(lines)

def main():
    # Read all skills from allskills.md (no dependencies)
    print("Reading all skills from allskills.md...")
    all_skills = parse_skills_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', parse_deps=False)
    print(f"  Found {len(all_skills)} total skills")

    # Read K-2 dependencies
    print("Reading K-2 skills with dependencies...")
    k2_deps = parse_skills_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/k2_skills_with_dependencies.md', parse_deps=True)
    print(f"  Found {len(k2_deps)} K-2 skills with dependencies")

    # Read G3 dependencies
    print("Reading G3 skills with dependencies...")
    g3_deps = parse_skills_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g3_skills_with_dependencies.md', parse_deps=True)
    print(f"  Found {len(g3_deps)} G3 skills with dependencies")

    # Merge dependencies into all_skills
    print("\nMerging dependencies...")
    for skill_id, skill_info in k2_deps.items():
        if skill_id in all_skills:
            all_skills[skill_id]['dependencies'] = skill_info['dependencies']
        else:
            print(f"  WARNING: K-2 skill {skill_id} not found in allskills.md")

    for skill_id, skill_info in g3_deps.items():
        if skill_id in all_skills:
            # For G3 deps without names, look up the name from all_skills
            deps_with_names = []
            for dep in skill_info['dependencies']:
                if not dep['name'] and dep['id'] in all_skills:
                    # Look up the skill name
                    dep['name'] = all_skills[dep['id']]['skill']
                deps_with_names.append(dep)
            all_skills[skill_id]['dependencies'] = deps_with_names
        else:
            print(f"  WARNING: G3 skill {skill_id} not found in allskills.md")

    # Convert to list and sort
    skill_list = list(all_skills.values())
    skill_list.sort(key=sort_key)

    # Count by grade
    grade_counts = defaultdict(int)
    dep_counts = defaultdict(int)
    dep_totals = defaultdict(int)

    for skill in skill_list:
        grade = extract_grade_from_id(skill['id'])
        grade_counts[grade] += 1
        dep_count = len(skill['dependencies'])
        dep_counts[grade] += dep_count
        dep_totals[grade] += dep_count

    # Write output
    print("\nWriting combined file...")
    output_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills_with_dependencies.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        for skill in skill_list:
            f.write(format_skill(skill))

    print(f"Wrote {len(skill_list)} skills to {output_path}")

    # Print statistics
    print("\n" + "="*60)
    print("STATISTICS")
    print("="*60)

    print("\nSkills by grade:")
    for grade in ['GK', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8']:
        count = grade_counts.get(grade, 0)
        print(f"  {grade}: {count:4d} skills")

    print(f"\n  Total: {sum(grade_counts.values())} skills")

    print("\nDependencies by grade:")
    for grade in ['GK', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8']:
        total_deps = dep_totals.get(grade, 0)
        skill_count = grade_counts.get(grade, 1)  # avoid division by zero
        avg = total_deps / skill_count if skill_count > 0 else 0
        print(f"  {grade}: {total_deps:4d} total dependencies, {avg:5.2f} avg per skill")

    print(f"\n  Total dependencies: {sum(dep_totals.values())}")
    overall_avg = sum(dep_totals.values()) / sum(grade_counts.values()) if sum(grade_counts.values()) > 0 else 0
    print(f"  Overall average: {overall_avg:.2f} dependencies per skill")

    print("\n" + "="*60)
    print(f"Total skill count: {len(skill_list)}")
    print("="*60)

if __name__ == '__main__':
    main()
