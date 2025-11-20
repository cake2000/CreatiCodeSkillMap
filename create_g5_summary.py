#!/usr/bin/env python3
"""Create a compact summary of all G5 skills"""

import re

def extract_g5_skills(filepath):
    """Extract all G5 skills with their complete information"""

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    g5_skills = []
    current_skill = None
    in_g5_skill = False
    skill_lines = []

    for i, line in enumerate(lines):
        if line.startswith('ID: ') and '.G5.' in line:
            if current_skill and in_g5_skill:
                parse_skill_content(current_skill, skill_lines)
                g5_skills.append(current_skill)

            skill_id = line.replace('ID: ', '').strip()
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': [],
            }
            in_g5_skill = True
            skill_lines = [line]

        elif in_g5_skill:
            if line.startswith('ID: '):
                parse_skill_content(current_skill, skill_lines)
                g5_skills.append(current_skill)
                current_skill = None
                in_g5_skill = False
                skill_lines = []

                if '.G5.' in line:
                    skill_id = line.replace('ID: ', '').strip()
                    current_skill = {
                        'id': skill_id,
                        'topic': '',
                        'skill': '',
                        'description': '',
                        'dependencies': [],
                    }
                    in_g5_skill = True
                    skill_lines = [line]
            else:
                skill_lines.append(line)

    if current_skill and in_g5_skill:
        parse_skill_content(current_skill, skill_lines)
        g5_skills.append(current_skill)

    return sorted(g5_skills, key=lambda x: x['id'])

def parse_skill_content(skill, lines):
    """Parse the content of a skill from its lines"""

    content = ''.join(lines)

    topic_match = re.search(r'Topic:\s*(.+?)(?:\n|$)', content)
    if topic_match:
        skill['topic'] = topic_match.group(1).strip()

    skill_match = re.search(r'Skill:\s*(.+?)(?:\n|$)', content)
    if skill_match:
        skill['skill'] = skill_match.group(1).strip()

    desc_match = re.search(r'Description:\s*(.*?)(?=\nDependencies:|\nID:|\Z)', content, re.DOTALL)
    if desc_match:
        skill['description'] = desc_match.group(1).strip()

    deps_match = re.search(r'Dependencies:\s*\n(.*?)(?=\nID:|\Z)', content, re.DOTALL)
    if deps_match:
        deps_text = deps_match.group(1).strip()
        dep_lines = deps_text.split('\n')
        for dep_line in dep_lines:
            dep_line = dep_line.strip()
            if dep_line.startswith('*'):
                dep_match = re.match(r'\*\s+(T\d+\.G\d+\.\d+):\s*(.+)', dep_line)
                if dep_match:
                    skill['dependencies'].append({
                        'id': dep_match.group(1),
                        'description': dep_match.group(2).strip()
                    })

def create_compact_summary(skills):
    """Create compact summary organized by topic"""

    # Group by topic
    topics = {}
    for skill in skills:
        topic = skill['id'].split('.')[0]
        if topic not in topics:
            topics[topic] = []
        topics[topic].append(skill)

    summary = []
    summary.append("=" * 100)
    summary.append("GRADE 5 SKILLS - COMPACT SUMMARY")
    summary.append("=" * 100)
    summary.append("")
    summary.append(f"Total: {len(skills)} skills across {len(topics)} topics")
    summary.append("")

    for topic_id in sorted(topics.keys()):
        topic_skills = topics[topic_id]
        topic_name = topic_skills[0]['topic'] if topic_skills[0]['topic'] else topic_id

        summary.append("")
        summary.append("=" * 100)
        summary.append(f"{topic_id}: {topic_name} ({len(topic_skills)} skills)")
        summary.append("=" * 100)

        for skill in topic_skills:
            dep_count = len(skill['dependencies'])
            dep_str = f"[{dep_count} deps]" if dep_count > 0 else "[no deps]"
            summary.append(f"  {skill['id']}: {skill['skill']} {dep_str}")

    summary.append("")
    return '\n'.join(summary)

if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Extracting G5 skills...")
    skills = extract_g5_skills(filepath)

    # Create compact summary
    summary = create_compact_summary(skills)

    # Save
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G5_SKILLS_SUMMARY.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(summary)

    print(f"Compact summary saved to: {output_file}")
    print(f"\nFound {len(skills)} G5 skills")
    print(summary)
