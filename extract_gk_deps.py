#!/usr/bin/env python3
"""
Extract all Grade K skills with their current dependencies to analyze cross-topic relationships.
"""

import re
from collections import defaultdict

def parse_allskills_file(filepath: str):
    """Parse allskills.md and extract all Grade K skills with their dependencies."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by ID: markers to get individual skills
    skill_blocks = re.split(r'\n(?=ID: T\d+\.)', content)

    gk_skills = {}

    for block in skill_blocks:
        if not block.strip():
            continue

        # Extract skill ID
        id_match = re.search(r'^ID: (T\d+\.GK\.\d+)', block, re.MULTILINE)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic
        topic_match = re.search(r'^Topic: (.+)$', block, re.MULTILINE)
        topic = topic_match.group(1) if topic_match else ""

        # Extract skill name
        skill_match = re.search(r'^Skill: (.+)$', block, re.MULTILINE)
        skill_name = skill_match.group(1) if skill_match else ""

        # Extract description
        desc_match = re.search(r'^Description: (.+?)(?=\n\n|\nDependencies:|\Z)', block, re.MULTILINE | re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        deps = []
        deps_section = re.search(r'Dependencies:\n((?:\* .+\n?)+)', block, re.MULTILINE)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'\* (T\d+\.[A-Z]\d+\.\d+):', line)
                if dep_match:
                    deps.append(dep_match.group(1))

        gk_skills[skill_id] = {
            'topic': topic,
            'name': skill_name,
            'description': description,
            'dependencies': deps
        }

    return gk_skills

def get_topic_number(skill_id: str) -> str:
    """Extract topic number from skill ID"""
    return skill_id.split('.')[0]

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    gk_skills = parse_allskills_file(filepath)

    # Group by topic
    by_topic = defaultdict(list)
    for skill_id, skill_data in gk_skills.items():
        topic_num = get_topic_number(skill_id)
        by_topic[topic_num].append(skill_id)

    print("GRADE K SKILLS WITH CURRENT DEPENDENCIES")
    print("=" * 80)
    print()

    for topic in sorted(by_topic.keys()):
        print(f"\n{'=' * 80}")
        print(f"TOPIC: {topic}")
        print('=' * 80)

        for skill_id in sorted(by_topic[topic]):
            skill_data = gk_skills[skill_id]
            print(f"\n{skill_id}: {skill_data['name']}")

            if skill_data['dependencies']:
                print("Current dependencies:")
                for dep in skill_data['dependencies']:
                    dep_topic = get_topic_number(dep)
                    is_cross_topic = dep_topic != topic
                    marker = " [CROSS-TOPIC]" if is_cross_topic else " [same topic]"

                    if dep in gk_skills:
                        print(f"  - {dep}: {gk_skills[dep]['name']}{marker}")
                    else:
                        print(f"  - {dep}{marker}")
            else:
                print("No dependencies")

    # Count cross-topic dependencies
    print("\n\n" + "=" * 80)
    print("CROSS-TOPIC DEPENDENCY SUMMARY")
    print("=" * 80)

    cross_topic_count = 0
    same_topic_count = 0

    for skill_id, skill_data in gk_skills.items():
        source_topic = get_topic_number(skill_id)
        for dep in skill_data['dependencies']:
            target_topic = get_topic_number(dep)
            if source_topic != target_topic:
                cross_topic_count += 1
            else:
                same_topic_count += 1

    print(f"\nTotal Grade K dependencies: {cross_topic_count + same_topic_count}")
    print(f"Cross-topic dependencies: {cross_topic_count}")
    print(f"Same-topic dependencies: {same_topic_count}")
    print(f"\nSkills with no dependencies: {sum(1 for s in gk_skills.values() if not s['dependencies'])}")
    print(f"Skills with dependencies: {sum(1 for s in gk_skills.values() if s['dependencies'])}")

if __name__ == '__main__':
    main()
