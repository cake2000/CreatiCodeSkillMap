#!/usr/bin/env python3
"""
Comprehensive topic-by-topic analysis of all Grade 1 skills.
Check for logical cross-topic dependency issues.
"""

import re
from collections import defaultdict

def parse_skills(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    current_skill = None
    in_dependencies = False

    lines = content.split('\n')
    for line in lines:
        id_match = re.match(r'^ID: (T\d+\.G[K12].\d+)$', line)
        if id_match:
            if current_skill:
                skills[current_skill['id']] = current_skill
            skill_id = id_match.group(1)
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': []
            }
            in_dependencies = False
            continue

        if current_skill:
            if line.startswith('Topic: '):
                current_skill['topic'] = line.replace('Topic: ', '').strip()
                in_dependencies = False
            elif line.startswith('Skill: '):
                current_skill['skill'] = line.replace('Skill: ', '').strip()
                in_dependencies = False
            elif line.startswith('Description: '):
                current_skill['description'] = line.replace('Description: ', '').strip()
                in_dependencies = False
            elif line.strip() == 'Dependencies:':
                in_dependencies = True
            elif in_dependencies and line.startswith('* '):
                dep_match = re.match(r'\* (T\d+\.G[K12].\d+):', line)
                if dep_match:
                    current_skill['dependencies'].append(dep_match.group(1))

    if current_skill:
        skills[current_skill['id']] = current_skill

    return skills

def extract_grade(skill_id):
    match = re.search(r'\.G([K12])\.', skill_id)
    return match.group(1) if match else None

def extract_topic(skill_id):
    match = re.match(r'T(\d+)\.', skill_id)
    return int(match.group(1)) if match else None

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills...")
    skills = parse_skills(filepath)

    g1_skills = {k: v for k, v in skills.items() if extract_grade(k) == '1'}
    print(f"Found {len(g1_skills)} Grade 1 skills\n")

    # Group by topic
    by_topic = defaultdict(list)
    for skill_id, skill in sorted(g1_skills.items()):
        topic = extract_topic(skill_id)
        by_topic[topic].append(skill)

    # Generate comprehensive report
    output = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G1_COMPREHENSIVE_TOPIC_ANALYSIS.md'
    with open(output, 'w') as f:
        f.write("# Grade 1 Skills - Comprehensive Topic-by-Topic Analysis\n\n")
        f.write("**Date:** 2024-11-24\n\n")
        f.write(f"**Total Grade 1 Skills:** {len(g1_skills)}\n\n")
        f.write(f"**Topics with Grade 1 Skills:** {len(by_topic)}\n\n")

        f.write("## Summary by Topic\n\n")
        f.write("| Topic | # G1 Skills | Topic Name |\n")
        f.write("|-------|-------------|------------|\n")

        topic_names = {}
        for topic_num, skills_list in sorted(by_topic.items()):
            if skills_list:
                topic_name = skills_list[0]['topic']
                topic_names[topic_num] = topic_name
                f.write(f"| T{topic_num:02d} | {len(skills_list)} | {topic_name} |\n")

        # Detailed analysis by topic
        for topic_num in sorted(by_topic.keys()):
            skills_list = by_topic[topic_num]
            if not skills_list:
                continue

            f.write(f"\n---\n\n## Topic {topic_num}: {topic_names[topic_num]}\n\n")
            f.write(f"**Number of Grade 1 Skills:** {len(skills_list)}\n\n")

            # Analyze cross-topic dependencies
            cross_topic_deps = set()
            same_topic_deps = set()

            for skill in skills_list:
                for dep in skill['dependencies']:
                    dep_topic = extract_topic(dep)
                    if dep_topic != topic_num:
                        cross_topic_deps.add(dep_topic)
                    else:
                        same_topic_deps.add(dep)

            if cross_topic_deps:
                f.write(f"**Cross-topic dependencies:** ")
                cross_topics_str = ", ".join([f"T{t:02d}" for t in sorted(cross_topic_deps)])
                f.write(f"{cross_topics_str}\n\n")
            else:
                f.write("**Cross-topic dependencies:** None\n\n")

            # List all skills in this topic
            f.write("### Grade 1 Skills in this Topic:\n\n")
            for idx, skill in enumerate(skills_list, 1):
                f.write(f"#### {idx}. {skill['id']}: {skill['skill']}\n\n")
                f.write(f"**Description:** {skill['description'][:200]}...\n\n")

                if skill['dependencies']:
                    f.write("**Dependencies:**\n")
                    for dep in skill['dependencies']:
                        dep_topic = extract_topic(dep)
                        if dep in skills:
                            dep_name = skills[dep]['skill']
                            marker = " [CROSS-TOPIC]" if dep_topic != topic_num else ""
                            f.write(f"- `{dep}`: {dep_name}{marker}\n")
                        else:
                            f.write(f"- `{dep}` [NOT FOUND]\n")
                    f.write("\n")
                else:
                    f.write("**Dependencies:** None\n\n")

    print(f"Comprehensive analysis saved to:\n{output}\n")

    # Print statistics
    print("\n" + "="*100)
    print("GRADE 1 SKILLS STATISTICS")
    print("="*100 + "\n")

    print("Skills per topic:")
    for topic_num in sorted(by_topic.keys()):
        count = len(by_topic[topic_num])
        print(f"  T{topic_num:02d}: {count} skills")

    # Check topics without Grade 1 skills
    all_topics = set(range(1, 37))
    topics_with_g1 = set(by_topic.keys())
    topics_without_g1 = all_topics - topics_with_g1

    if topics_without_g1:
        print(f"\nTopics without Grade 1 skills: {', '.join([f'T{t:02d}' for t in sorted(topics_without_g1)])}")

    # Cross-topic dependency patterns
    print("\n" + "="*100)
    print("CROSS-TOPIC DEPENDENCY PATTERNS")
    print("="*100 + "\n")

    all_cross_deps = defaultdict(int)
    for skill_id, skill in g1_skills.items():
        topic = extract_topic(skill_id)
        for dep in skill['dependencies']:
            dep_topic = extract_topic(dep)
            if dep_topic and dep_topic != topic:
                all_cross_deps[(topic, dep_topic)] += 1

    if all_cross_deps:
        print("Most common cross-topic dependencies:")
        for (from_topic, to_topic), count in sorted(all_cross_deps.items(), key=lambda x: x[1], reverse=True)[:15]:
            print(f"  T{from_topic:02d} -> T{to_topic:02d}: {count} dependencies")
    else:
        print("No cross-topic dependencies found in Grade 1 skills")

if __name__ == '__main__':
    main()
