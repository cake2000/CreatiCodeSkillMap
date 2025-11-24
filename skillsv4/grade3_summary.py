#!/usr/bin/env python3
"""Generate a summary of Grade 3 skills by topic"""

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

    # Organize by topic
    by_topic = defaultdict(list)
    for skill in skills:
        topic_id = skill['id'].split('.')[0]  # e.g., T01
        by_topic[topic_id].append(skill)

    print("="*80)
    print("GRADE 3 SKILLS SUMMARY")
    print("="*80)
    print()

    # Create summary table
    print(f"{'Topic':<8} {'Topic Name':<50} {'G3 Skills':<10}")
    print("-"*80)

    total_skills = 0
    topics_with_g3 = []

    for topic_id in sorted(by_topic.keys(), key=lambda x: int(x[1:])):
        skills_in_topic = by_topic[topic_id]
        topic_name = skills_in_topic[0]['topic']
        # Truncate long topic names
        if len(topic_name) > 48:
            topic_name = topic_name[:45] + "..."

        count = len(skills_in_topic)
        total_skills += count
        topics_with_g3.append((topic_id, topic_name, count))

        print(f"{topic_id:<8} {topic_name:<50} {count:<10}")

    print("-"*80)
    print(f"{'TOTAL':<8} {'':<50} {total_skills:<10}")
    print("="*80)
    print()

    # Additional statistics
    print("STATISTICS:")
    print(f"  Total Grade 3 skills: {total_skills}")
    print(f"  Number of topics with G3 skills: {len(topics_with_g3)}")
    print(f"  Average skills per topic: {total_skills/len(topics_with_g3):.1f}")
    print()

    # Find topics with most/least skills
    sorted_by_count = sorted(topics_with_g3, key=lambda x: x[2], reverse=True)
    print(f"  Topic with most G3 skills: {sorted_by_count[0][0]} ({sorted_by_count[0][2]} skills)")
    print(f"  Topic with fewest G3 skills: {sorted_by_count[-1][0]} ({sorted_by_count[-1][2]} skills)")
    print()

    # Topics without G3 skills
    all_topics = set(f"T{i:02d}" for i in range(1, 37))
    topics_with_skills = set(by_topic.keys())
    topics_without = sorted(all_topics - topics_with_skills, key=lambda x: int(x[1:]))

    if topics_without:
        print(f"  Topics WITHOUT Grade 3 skills ({len(topics_without)}):")
        print(f"    {', '.join(topics_without)}")
    else:
        print("  All topics have Grade 3 skills!")
    print()

if __name__ == '__main__':
    main()
