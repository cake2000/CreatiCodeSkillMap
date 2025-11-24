#!/usr/bin/env python3
"""
Extract all Grade 2 skills from allskills.md
"""

import re
import json

def extract_grade2_skills(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into sections by skill ID
    skill_pattern = re.compile(r'^ID: (T\d+\.G\d+\.\d+(?:\.\d+)?)\s*$', re.MULTILINE)

    skills = []
    matches = list(skill_pattern.finditer(content))

    for i, match in enumerate(matches):
        skill_id = match.group(1)

        # Only process Grade 2 skills
        if '.G2.' not in skill_id:
            continue

        # Extract the section for this skill
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        section = content[start:end]

        # Extract topic from ID (T##)
        topic_match = re.match(r'T(\d+)', skill_id)
        topic = f"T{topic_match.group(1)}" if topic_match else "Unknown"

        # Extract skill name (usually the line after "Skill name:")
        name_match = re.search(r'Skill name:\s*(.+?)(?:\n|$)', section)
        skill_name = name_match.group(1).strip() if name_match else "N/A"

        # Extract description
        desc_match = re.search(r'Description:\s*(.+?)(?:\n\n|\nGrade level:|\nSkill type:)', section, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else "N/A"
        description = ' '.join(description.split())  # Normalize whitespace

        # Extract dependencies
        deps = []
        deps_section = re.search(r'Dependencies:\s*\n((?:\s*\*\s*T\d+\.G\d+\.\d+(?:\.\d+)?:.*\n?)+)', section)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.match(r'\s*\*\s*(T\d+\.G\d+\.\d+(?:\.\d+)?)', line)
                if dep_match:
                    deps.append(dep_match.group(1))

        skills.append({
            'id': skill_id,
            'topic': topic,
            'name': skill_name,
            'description': description,
            'dependencies': deps
        })

    return skills

def main():
    filename = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = extract_grade2_skills(filename)

    # Group by topic
    topics = {}
    for skill in skills:
        topic = skill['topic']
        if topic not in topics:
            topics[topic] = []
        topics[topic].append(skill)

    # Sort topics
    sorted_topics = sorted(topics.keys(), key=lambda x: int(x[1:]))

    # Print results
    print("=" * 80)
    print(f"GRADE 2 SKILLS EXTRACTION REPORT")
    print(f"Total Grade 2 Skills Found: {len(skills)}")
    print("=" * 80)
    print()

    for topic in sorted_topics:
        topic_skills = topics[topic]
        print(f"\n{'=' * 80}")
        print(f"TOPIC {topic} ({len(topic_skills)} Grade 2 skills)")
        print(f"{'=' * 80}")

        for skill in topic_skills:
            print(f"\nSkill ID: {skill['id']}")
            print(f"Name: {skill['name']}")
            print(f"Description: {skill['description'][:200]}{'...' if len(skill['description']) > 200 else ''}")
            print(f"Dependencies ({len(skill['dependencies'])}):")
            if skill['dependencies']:
                for dep in skill['dependencies']:
                    print(f"  - {dep}")
            else:
                print("  (none)")

    # Save to JSON
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade_2_skills_complete.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'total_count': len(skills),
            'topics': {topic: topics[topic] for topic in sorted_topics},
            'skills': skills
        }, f, indent=2)

    print(f"\n{'=' * 80}")
    print(f"JSON output saved to: {output_file}")
    print(f"{'=' * 80}")

if __name__ == '__main__':
    main()
