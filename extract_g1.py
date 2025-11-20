#!/usr/bin/env python3
"""Extract all G1 skills from allskills.md"""

import re

def extract_g1_skills(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match skill blocks
    # Each skill starts with "ID: " and ends before the next "ID: " or topic header
    pattern = r'ID: (T\d+\.G1\.\d+)\n(.*?)(?=\nID: T\d+\.G\d+\.\d+|\n# T\d+:|$)'

    skills = []
    for match in re.finditer(pattern, content, re.DOTALL):
        skill_id = match.group(1)
        skill_content = match.group(2)

        # Extract topic
        topic_match = re.search(r'Topic: (.+)', skill_content)
        topic = topic_match.group(1) if topic_match else "NO TOPIC"

        # Extract skill title
        skill_match = re.search(r'Skill: (.+)', skill_content)
        title = skill_match.group(1) if skill_match else "NO TITLE"

        # Extract dependencies - they're listed as bullet points
        deps_section = re.search(r'Dependencies:\s*\n((?:\* .*\n)*)', skill_content)
        dependencies = []
        if deps_section:
            deps_text = deps_section.group(1)
            # Extract skill IDs from dependency lines
            for dep_line in deps_text.split('\n'):
                if dep_line.strip():
                    dep_match = re.search(r'(T\d+\.[KG]\d+\.\d+)', dep_line)
                    if dep_match:
                        dependencies.append(dep_match.group(1))

        skills.append({
            'id': skill_id,
            'topic': topic,
            'title': title,
            'dependencies': dependencies,
            'full_content': skill_content
        })

    return skills

if __name__ == '__main__':
    skills = extract_g1_skills('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')

    print(f"Found {len(skills)} G1 skills\n")
    print("="*80)

    for skill in sorted(skills, key=lambda x: x['id']):
        print(f"\n{skill['id']}: {skill['title']}")
        print(f"Topic: {skill['topic']}")
        if skill['dependencies']:
            print(f"Dependencies: {', '.join(skill['dependencies'])}")
        else:
            print("Dependencies: None")
        print("-"*80)
