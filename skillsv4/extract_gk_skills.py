#!/usr/bin/env python3
"""
Extract all Grade K skills from allskills.md and analyze dependencies
"""

import re
from collections import defaultdict

def parse_allskills(filepath):
    """Parse allskills.md and extract all Grade K skills"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match skill blocks
    skill_pattern = r'ID: (T\d+\.GK\.\d+)\s*\nTopic: ([^\n]+)\s*\nSkill: ([^\n]+)\s*\nDescription: ([^\n]+(?:\n(?!ID:|Dependencies:)[^\n]+)*)'
    dep_pattern = r'Dependencies:\s*\n((?:\* [^\n]+\n)*)'

    skills = {}
    current_id = None

    # Split content by ID markers
    sections = content.split('\nID: ')

    for section in sections:
        if not section.strip():
            continue

        # Add back the ID: prefix
        if not section.startswith('ID:'):
            section = 'ID: ' + section

        # Extract skill ID
        id_match = re.search(r'ID: (T\d+\.GK\.\d+)', section)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic
        topic_match = re.search(r'Topic: ([^\n]+)', section)
        topic = topic_match.group(1).strip() if topic_match else ''

        # Extract skill name
        skill_match = re.search(r'Skill: ([^\n]+)', section)
        skill_name = skill_match.group(1).strip() if skill_match else ''

        # Extract description
        desc_match = re.search(r'Description: ([^\n]+(?:\n(?!Dependencies:|ID:)[^\n]+)*)', section, re.MULTILINE)
        description = desc_match.group(1).strip() if desc_match else ''

        # Extract dependencies
        deps = []
        dep_match = re.search(r'Dependencies:\s*\n((?:\* [^\n]+\n?)*)', section, re.MULTILINE)
        if dep_match:
            dep_text = dep_match.group(1)
            for line in dep_text.split('\n'):
                line = line.strip()
                if line.startswith('*'):
                    # Extract dependency ID
                    dep_id_match = re.search(r'(T\d+\.[A-Z0-9]+\.\d+)', line)
                    if dep_id_match:
                        deps.append(dep_id_match.group(1))

        skills[skill_id] = {
            'topic': topic,
            'skill': skill_name,
            'description': description,
            'dependencies': deps,
            'raw_section': section[:500]  # Store first 500 chars for debugging
        }

    return skills

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    skills = parse_allskills(filepath)

    print(f"Total Grade K skills found: {len(skills)}")
    print("\nTopics covered:")

    topics = defaultdict(list)
    for skill_id, skill_data in sorted(skills.items()):
        topic_num = skill_id.split('.')[0]
        topics[topic_num].append(skill_id)

    for topic, skill_ids in sorted(topics.items()):
        print(f"  {topic}: {len(skill_ids)} skills")

    print("\n" + "="*80)
    print("DEPENDENCY ANALYSIS")
    print("="*80)

    # Analyze dependencies
    invalid_deps = []
    cross_topic_deps = defaultdict(list)

    for skill_id, skill_data in sorted(skills.items()):
        topic_num = skill_id.split('.')[0]

        if skill_data['dependencies']:
            print(f"\n{skill_id}: {skill_data['skill']}")
            print(f"  Dependencies: {len(skill_data['dependencies'])}")

            for dep in skill_data['dependencies']:
                dep_topic = dep.split('.')[0]

                # Check if dependency exists
                if dep not in skills:
                    print(f"    ⚠ INVALID: {dep} (not a GK skill)")
                    invalid_deps.append((skill_id, dep))
                # Check cross-topic
                elif dep_topic != topic_num:
                    print(f"    ✓ Cross-topic: {dep} ({dep_topic})")
                    cross_topic_deps[skill_id].append(dep)
                else:
                    print(f"    ✓ Intra-topic: {dep}")

    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total skills: {len(skills)}")
    print(f"Skills with dependencies: {sum(1 for s in skills.values() if s['dependencies'])}")
    print(f"Invalid dependencies found: {len(invalid_deps)}")
    print(f"Skills with cross-topic deps: {len(cross_topic_deps)}")

    if invalid_deps:
        print("\nINVALID DEPENDENCIES TO FIX:")
        for skill_id, dep in invalid_deps:
            print(f"  {skill_id} → {dep}")

if __name__ == '__main__':
    main()
