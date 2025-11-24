#!/usr/bin/env python3
"""Extract all Grade 3 skills from allskills.md"""

import re
from collections import defaultdict

def extract_grade3_skills(filepath):
    """Extract all Grade 3 skills with their details"""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into individual skill blocks
    skill_blocks = re.split(r'\n(?=ID: T\d+\.G3\.\d+)', content)

    grade3_skills = []

    for block in skill_blocks:
        # Check if this is a Grade 3 skill
        id_match = re.search(r'^ID: (T\d+\.G3\.\S+)', block, re.MULTILINE)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract Topic
        topic_match = re.search(r'^Topic: (.+)$', block, re.MULTILINE)
        topic = topic_match.group(1) if topic_match else "NOT FOUND"

        # Extract Skill
        skill_match = re.search(r'^Skill: (.+)$', block, re.MULTILINE)
        skill = skill_match.group(1) if skill_match else "NOT FOUND"

        # Extract Dependencies
        deps_section = re.search(r'Dependencies:\n((?:\* .+\n)*)', block, re.MULTILINE)
        dependencies = []
        if deps_section:
            dep_text = deps_section.group(1)
            dep_lines = re.findall(r'^\* (.+)$', dep_text, re.MULTILINE)
            dependencies = dep_lines

        grade3_skills.append({
            'id': skill_id,
            'topic': topic,
            'skill': skill,
            'dependencies': dependencies
        })

    return grade3_skills

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = extract_grade3_skills(filepath)

    print(f"Total Grade 3 skills found: {len(skills)}\n")
    print("="*80)

    # Organize by topic
    by_topic = defaultdict(list)
    for skill in skills:
        topic_id = skill['id'].split('.')[0]  # e.g., T01
        by_topic[topic_id].append(skill)

    # Print organized by topic
    for topic_id in sorted(by_topic.keys(), key=lambda x: int(x[1:])):
        skills_in_topic = by_topic[topic_id]
        print(f"\n{'='*80}")
        print(f"{topic_id}: {skills_in_topic[0]['topic']}")
        print(f"Total G3 skills: {len(skills_in_topic)}")
        print('='*80)

        for skill in skills_in_topic:
            print(f"\nID: {skill['id']}")
            print(f"Skill: {skill['skill']}")

            if skill['dependencies']:
                print(f"Dependencies ({len(skill['dependencies'])}):")
                for dep in skill['dependencies']:
                    print(f"  * {dep}")
            else:
                print("Dependencies: None")

    print(f"\n\n{'='*80}")
    print(f"SUMMARY: Found {len(skills)} Grade 3 skills across {len(by_topic)} topics")
    print('='*80)

if __name__ == '__main__':
    main()
