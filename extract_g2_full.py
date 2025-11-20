#!/usr/bin/env python3
"""Extract all G2 skills with complete sections."""

import re

def extract_g2_skills_full(filepath):
    """Extract all G2 skills with their complete sections."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by ID: markers to separate skills
    skill_blocks = re.split(r'\n(?=ID: )', content)

    g2_skills = []

    for block in skill_blocks:
        if not block.strip():
            continue

        # Check if this is a G2 skill
        id_match = re.search(r'^ID:\s*([TG]\d+\.G2\.\d+)', block, re.MULTILINE)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic
        topic_match = re.search(r'^Topic:\s*(.+?)$', block, re.MULTILINE)
        topic = topic_match.group(1).strip() if topic_match else 'Unknown'

        # Extract skill title
        skill_match = re.search(r'^Skill:\s*(.+?)$', block, re.MULTILINE)
        title = skill_match.group(1).strip() if skill_match else 'Unknown'

        # Extract description
        desc_match = re.search(r'^Description:\s*(.+?)(?=\n(?:Dependencies:|ID:|\Z))', block, re.MULTILINE | re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ''

        # Extract dependencies
        dependencies = []
        deps_match = re.search(r'^Dependencies:\s*\n((?:\*\s*.+?\n)*)', block, re.MULTILINE)
        if deps_match:
            dep_text = deps_match.group(1)
            dep_items = re.findall(r'\*\s*([TG]\d+\.G[K\d]+\.\d+):\s*(.+)', dep_text)
            dependencies = [{'id': dep[0], 'title': dep[1].strip()} for dep in dep_items]

        g2_skills.append({
            'topic': topic,
            'skill_id': skill_id,
            'title': title,
            'description': description,
            'dependencies': dependencies,
            'full_content': block.strip()
        })

    return g2_skills

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    g2_skills = extract_g2_skills_full(filepath)

    # Group by topic
    topics = {}
    for skill in g2_skills:
        topic = skill['topic'] or 'Unknown Topic'
        if topic not in topics:
            topics[topic] = []
        topics[topic].append(skill)

    # Save to file
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/g2_skills_complete.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Grade 2 (G2) Skills - Complete Extraction\n\n")
        f.write(f"**Total G2 Skills Found:** {len(g2_skills)}\n\n")
        f.write(f"**Extraction Date:** 2025-11-20\n\n")
        f.write("---\n\n")

        # Table of contents
        f.write("## Table of Contents\n\n")
        for topic_name in sorted(topics.keys()):
            skills_in_topic = len(topics[topic_name])
            f.write(f"- [{topic_name}](#{topic_name.lower().replace(' ', '-')}) ({skills_in_topic} skills)\n")
        f.write("\n---\n\n")

        # Full content by topic
        for topic_name in sorted(topics.keys()):
            skills = topics[topic_name]
            f.write(f"## {topic_name}\n\n")
            f.write(f"**Number of G2 skills:** {len(skills)}\n\n")

            for skill in sorted(skills, key=lambda x: x['skill_id']):
                f.write(f"{skill['full_content']}\n")
                f.write("\n" + "="*80 + "\n\n")

        # Summary table at the end
        f.write("\n\n# Summary Table of All G2 Skills\n\n")
        f.write("| Skill ID | Topic | Title | # Deps |\n")
        f.write("|----------|-------|-------|--------|\n")

        for skill in sorted(g2_skills, key=lambda x: x['skill_id']):
            deps_count = len(skill['dependencies'])
            topic_short = skill['topic'][:30] + '...' if len(skill['topic']) > 30 else skill['topic']
            title_short = skill['title'][:50] + '...' if len(skill['title']) > 50 else skill['title']
            f.write(f"| {skill['skill_id']} | {topic_short} | {title_short} | {deps_count} |\n")

        # Dependency analysis
        f.write("\n\n# Dependency Analysis\n\n")
        f.write("## Skills with Dependencies\n\n")

        for skill in sorted(g2_skills, key=lambda x: x['skill_id']):
            if skill['dependencies']:
                f.write(f"\n### {skill['skill_id']}: {skill['title']}\n\n")
                f.write("**Dependencies:**\n\n")
                for dep in skill['dependencies']:
                    # Check if dependency is appropriate
                    dep_grade = re.search(r'\.G(\d+|K)\.', dep['id'])
                    if dep_grade:
                        grade = dep_grade.group(1)
                        warning = ""
                        if grade not in ['K', '1', '2']:
                            warning = " ⚠️ **ISSUE: Depends on higher grade!**"
                        f.write(f"- {dep['id']}: {dep['title']}{warning}\n")
                f.write("\n")

    print(f"Extraction complete!")
    print(f"Total G2 skills found: {len(g2_skills)}")
    print(f"\nSkills by topic:")
    for topic_name in sorted(topics.keys()):
        print(f"  - {topic_name}: {len(topics[topic_name])} skills")
    print(f"\nOutput saved to: {output_file}")

if __name__ == '__main__':
    main()
