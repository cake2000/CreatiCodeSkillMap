#!/usr/bin/env python3
"""
Add dependencies to K-2 skills in allskills.md
"""

import re
from typing import List, Dict, Tuple

def parse_skills(filepath: str) -> List[Dict]:
    """Parse all skills from the markdown file."""
    skills = []
    current_skill = {}

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.rstrip('\n')

        if line.startswith('ID: '):
            # Save previous skill if exists
            if current_skill:
                skills.append(current_skill)

            # Start new skill
            skill_id = line.replace('ID: ', '').strip()
            current_skill = {
                'id': skill_id,
                'line_num': i,
                'lines': [line]
            }
        elif current_skill:
            current_skill['lines'].append(line)

            # Extract fields
            if line.startswith('Topic: '):
                current_skill['topic'] = line.replace('Topic: ', '').strip()
            elif line.startswith('Skill: '):
                current_skill['skill'] = line.replace('Skill: ', '').strip()
            elif line.startswith('Description: '):
                current_skill['description'] = line.replace('Description: ', '').strip()

    # Don't forget the last skill
    if current_skill:
        skills.append(current_skill)

    return skills

def get_grade_topic(skill_id: str) -> Tuple[str, str]:
    """Extract grade and topic from skill ID like T01.GK.01"""
    match = re.match(r'T(\d+)\.(G[K\d])\.(\d+)', skill_id)
    if match:
        topic = f"T{match.group(1)}"
        grade = match.group(2)
        return grade, topic
    return None, None

def add_dependencies_to_k2_skills(skills: List[Dict]) -> List[Dict]:
    """
    Add dependencies to K-2 skills following pedagogical principles.

    Key patterns:
    - GK: Average 0.62 dependencies (mostly 0-1)
    - G1: Average 0.91 dependencies (mostly 0-2)
    - G2: Average 1.45 dependencies (mostly 1-2)
    - Algorithm skills (T01) may depend on pattern recognition (T04)
    - Pattern skills (T04) may depend on basic sequencing (T01)
    - Debugging skills (T13) depend on understanding what correct looks like
    - Data skills (T25-T28) may depend on counting and sorting abilities
    """

    # Create lookup dictionaries
    skills_by_id = {s['id']: s for s in skills}
    skills_by_grade_topic = {}

    for skill in skills:
        grade, topic = get_grade_topic(skill['id'])
        if grade and topic:
            key = f"{grade}_{topic}"
            if key not in skills_by_grade_topic:
                skills_by_grade_topic[key] = []
            skills_by_grade_topic[key].append(skill)

    # Process each K-2 skill
    for skill in skills:
        grade, topic = get_grade_topic(skill['id'])

        if grade not in ['GK', 'G1', 'G2']:
            continue

        dependencies = []
        skill_id = skill['id']
        skill_name = skill.get('skill', '')
        desc = skill.get('description', '').lower()

        # GRADE K DEPENDENCIES (average 0.62)
        if grade == 'GK':
            # Most GK skills have no dependencies
            # Only add if there's a clear foundational need

            if topic == 'T01':  # Algorithms
                # T01.GK.07 (find repeating pattern) depends on sequencing
                if 'pattern' in skill_name.lower() and 'repeat' in skill_name.lower():
                    dependencies.append(('T01.GK.03', 'Find the first and last pictures'))
                # T01.GK.08 (counting) is foundational
                pass

            elif topic == 'T04':  # Patterns
                # Pattern recognition may benefit from basic sequencing
                if 'AB' in skill_name or 'complete' in skill_name.lower():
                    dependencies.append(('T01.GK.03', 'Find the first and last pictures'))

            elif topic == 'T13':  # Debugging
                # Debugging requires understanding correct sequences
                if 'wrong' in desc or 'mistake' in desc or 'fix' in desc:
                    dependencies.append(('T01.GK.03', 'Find the first and last pictures'))

        # GRADE 1 DEPENDENCIES (average 0.91)
        elif grade == 'G1':
            if topic == 'T01':  # Algorithms
                # More complex sequencing may depend on GK basics
                if 'order' in skill_name.lower():
                    # Check if it's more than 4 items
                    if '5' in desc or 'five' in desc:
                        dependencies.append(('T01.GK.02', 'Put pictures in order for coming to class'))

                # Repeating patterns depend on GK pattern recognition
                if 'repeat' in skill_name.lower() or 'pattern' in skill_name.lower():
                    dependencies.append(('T01.GK.07', 'Find the pattern that repeats'))

                # Counting actions
                if 'count' in skill_name.lower() or 'how many' in skill_name.lower():
                    dependencies.append(('T01.GK.08', 'Count how many times'))

            elif topic == 'T04':  # Patterns
                # Build on GK pattern skills
                if 'AAB' in skill_name or 'ABB' in skill_name:
                    dependencies.append(('T04.GK.02', 'Complete an AB pattern'))
                elif 'ABC' in skill_name:
                    dependencies.append(('T04.GK.02', 'Complete an AB pattern'))
                elif 'pattern' in skill_name.lower() and 'next' in skill_name.lower():
                    dependencies.append(('T04.GK.03', 'What comes next in a pattern?'))

            elif topic == 'T13':  # Debugging
                # Debugging requires understanding correct sequences
                dependencies.append(('T01.GK.04', 'Pick the pictures that make sense'))

            elif topic in ['T25', 'T26', 'T27', 'T28']:  # Data topics
                # Data skills may need counting
                if 'count' in skill_name.lower() or 'how many' in desc:
                    dependencies.append(('T01.GK.08', 'Count how many times'))

        # GRADE 2 DEPENDENCIES (average 1.45)
        elif grade == 'G2':
            if topic == 'T01':  # Algorithms
                # Complex sequencing
                if 'order' in skill_name.lower() and ('6' in desc or 'six' in desc or '7' in desc):
                    dependencies.append(('T01.G1.02', 'Put pictures in order to make breakfast'))

                # Repeating patterns with counting
                if 'repeat' in skill_name.lower():
                    dependencies.append(('T01.G1.07', 'Find the repeating pattern'))
                    if 'count' in skill_name.lower() or 'how many' in desc:
                        dependencies.append(('T01.G1.09', 'Count repeats in a pattern'))

                # Decision-making and conditionals
                if 'choose' in skill_name.lower() or 'pick' in skill_name.lower() or 'decision' in skill_name.lower():
                    dependencies.append(('T01.G1.04', 'Pick the best order'))

                # More complex counting
                if 'count' in skill_name.lower() and 'different' in skill_name.lower():
                    dependencies.append(('T01.G1.09', 'Count repeats in a pattern'))

            elif topic == 'T04':  # Patterns
                # More complex patterns
                if 'growing' in skill_name.lower() or 'changing' in skill_name.lower():
                    dependencies.append(('T04.G1.03', 'What comes next in an AAB or ABB pattern?'))
                elif 'create' in skill_name.lower() or 'make' in skill_name.lower():
                    dependencies.append(('T04.G1.04', 'Make your own ABC pattern'))

            elif topic == 'T13':  # Debugging
                # Debugging more complex sequences
                dependencies.append(('T13.G1.01', 'Find the picture that does not belong'))
                if 'fix' in skill_name.lower() or 'mistake' in skill_name.lower():
                    dependencies.append(('T01.G1.05', 'Find the missing step'))

            elif topic in ['T25', 'T26', 'T27', 'T28']:  # Data topics
                # Sorting and organizing data
                if 'sort' in skill_name.lower() or 'order' in skill_name.lower():
                    dependencies.append(('T01.G1.01', 'Put pictures in order to plant a seed'))
                if 'count' in skill_name.lower() or 'how many' in desc:
                    dependencies.append(('T01.G1.09', 'Count repeats in a pattern'))
                # Comparing and analyzing
                if 'compare' in skill_name.lower() or 'more' in skill_name.lower() or 'less' in skill_name.lower():
                    dependencies.append(('T25.G1.01', 'Count items in a group'))

        # Add dependency section to the skill
        if dependencies:
            skill['dependencies'] = dependencies

    return skills

def write_updated_skills(filepath: str, skills: List[Dict], output_filepath: str):
    """Write updated skills with dependencies back to file."""

    output_lines = []

    for skill in skills:
        grade, topic = get_grade_topic(skill['id'])

        # Only process K-2 skills
        if grade not in ['GK', 'G1', 'G2']:
            continue

        # Write ID, Topic, Skill lines
        for line in skill['lines']:
            output_lines.append(line)

            # After Description, add Dependencies if they exist
            if line.startswith('Description: '):
                if 'dependencies' in skill:
                    output_lines.append('Dependencies:')
                    for dep_id, dep_name in skill['dependencies']:
                        output_lines.append(f'* {dep_id}: {dep_name}')

                # Add blank line after skill block
                output_lines.append('')
                break

    # Write to output file
    with open(output_filepath, 'w', encoding='utf-8') as f:
        for line in output_lines:
            f.write(line + '\n')

    print(f"Wrote updated skills to: {output_filepath}")
    print(f"Total skills processed: {len([s for s in skills if get_grade_topic(s['id'])[0] in ['GK', 'G1', 'G2']])}")

def main():
    input_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/k2_skills_with_dependencies.md'

    print("Parsing skills...")
    skills = parse_skills(input_file)
    print(f"Total skills found: {len(skills)}")

    print("\nAdding dependencies to K-2 skills...")
    skills = add_dependencies_to_k2_skills(skills)

    print("\nWriting output...")
    write_updated_skills(input_file, skills, output_file)

    # Print statistics
    k_count = len([s for s in skills if get_grade_topic(s['id'])[0] == 'GK' and 'dependencies' in s])
    g1_count = len([s for s in skills if get_grade_topic(s['id'])[0] == 'G1' and 'dependencies' in s])
    g2_count = len([s for s in skills if get_grade_topic(s['id'])[0] == 'G2' and 'dependencies' in s])

    k_total = len([s for s in skills if get_grade_topic(s['id'])[0] == 'GK'])
    g1_total = len([s for s in skills if get_grade_topic(s['id'])[0] == 'G1'])
    g2_total = len([s for s in skills if get_grade_topic(s['id'])[0] == 'G2'])

    print(f"\nGK: {k_count}/{k_total} skills with dependencies")
    print(f"G1: {g1_count}/{g1_total} skills with dependencies")
    print(f"G2: {g2_count}/{g2_total} skills with dependencies")

if __name__ == '__main__':
    main()
