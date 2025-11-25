#!/usr/bin/env python3
"""Create JSON export of Grade 7 skills for easier data analysis"""

import json
import re
from collections import defaultdict

def extract_grade7_skills(filename):
    """Extract all Grade 7 skills with their complete information"""

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = []
    current_skill = None
    in_g7_skill = False

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.startswith('ID: ') and '.G7.' in line:
            if current_skill:
                skills.append(current_skill)

            current_skill = {'id': line.replace('ID: ', '').strip(), 'raw_lines': [line]}
            in_g7_skill = True
            i += 1
            continue

        if in_g7_skill:
            if line.startswith('ID: ') and '.G7.' not in line:
                if current_skill:
                    skills.append(current_skill)
                current_skill = None
                in_g7_skill = False
            elif line.startswith('## ') or line.startswith('---'):
                if current_skill:
                    skills.append(current_skill)
                current_skill = None
                in_g7_skill = False
            else:
                if current_skill:
                    current_skill['raw_lines'].append(line)

        i += 1

    if current_skill and in_g7_skill:
        skills.append(current_skill)

    parsed_skills = []
    for skill in skills:
        parsed = parse_skill_details(skill)
        if parsed:
            parsed_skills.append(parsed)

    return parsed_skills

def parse_skill_details(skill):
    """Parse skill details from raw lines"""

    parsed = {'id': skill['id']}
    raw_text = '\n'.join(skill['raw_lines'])

    topic_match = re.search(r'^Topic:\s*(.+)$', raw_text, re.MULTILINE)
    if topic_match:
        parsed['topic'] = topic_match.group(1).strip()

    skill_match = re.search(r'^Skill:\s*(.+)$', raw_text, re.MULTILINE)
    if skill_match:
        parsed['skill'] = skill_match.group(1).strip()

    desc_match = re.search(r'^Description:\s*(.+?)(?=\n\n|\nDependencies:|\nAlternative|\nGrade:|\Z)',
                           raw_text, re.MULTILINE | re.DOTALL)
    if desc_match:
        parsed['description'] = desc_match.group(1).strip()

    deps_match = re.search(r'^Dependencies:\s*\n((?:\*.+\n?)+)', raw_text, re.MULTILINE)
    if deps_match:
        deps_text = deps_match.group(1)
        deps = re.findall(r'^\*\s*(.+)$', deps_text, re.MULTILINE)
        parsed['dependencies'] = [d.strip() for d in deps]
    else:
        if 'Dependencies: None' in raw_text or 'Dependencies:\nNone' in raw_text:
            parsed['dependencies'] = []
        else:
            parsed['dependencies'] = []

    grade_match = re.search(r'^Grade:\s*(\d+)$', raw_text, re.MULTILINE)
    if grade_match:
        parsed['grade'] = grade_match.group(1)
    else:
        parsed['grade'] = '7'

    return parsed

def main():
    input_file = 'allskills.md'
    output_json = 'GRADE7_SKILLS.json'

    print(f"Extracting Grade 7 skills from {input_file}...")
    skills = extract_grade7_skills(input_file)

    # Group by topic
    by_topic = defaultdict(list)
    for skill in skills:
        topic = skill.get('topic', 'Unknown')
        by_topic[topic].append(skill)

    # Create output structure
    output = {
        'metadata': {
            'total_skills': len(skills),
            'total_topics': len(by_topic),
            'grade': 7,
            'source': 'allskills.md'
        },
        'summary': {
            'skills_by_topic': {topic: len(skills_list) for topic, skills_list in by_topic.items()}
        },
        'skills': sorted(skills, key=lambda x: x['id']),
        'by_topic': {topic: sorted(skills_list, key=lambda x: x['id'])
                     for topic, skills_list in by_topic.items()}
    }

    print(f"Writing {len(skills)} skills to {output_json}...")
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"JSON export complete!")
    print(f"  Total skills: {len(skills)}")
    print(f"  Topics: {len(by_topic)}")

if __name__ == '__main__':
    main()
