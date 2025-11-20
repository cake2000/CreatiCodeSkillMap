#!/usr/bin/env python3
"""Extract all Grade 5 skills from allskills.md"""

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
        # Check if this line contains a G5 skill ID
        if line.startswith('ID: ') and '.G5.' in line:
            # Save previous skill if exists
            if current_skill and in_g5_skill:
                parse_skill_content(current_skill, skill_lines)
                g5_skills.append(current_skill)

            # Start new skill
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
            # Check if we've hit the next skill (any ID line)
            if line.startswith('ID: '):
                # End current skill
                parse_skill_content(current_skill, skill_lines)
                g5_skills.append(current_skill)
                current_skill = None
                in_g5_skill = False
                skill_lines = []

                # Check if this new ID is also a G5 skill
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

    # Don't forget the last skill
    if current_skill and in_g5_skill:
        parse_skill_content(current_skill, skill_lines)
        g5_skills.append(current_skill)

    return sorted(g5_skills, key=lambda x: x['id'])

def parse_skill_content(skill, lines):
    """Parse the content of a skill from its lines"""

    content = ''.join(lines)

    # Extract topic
    topic_match = re.search(r'Topic:\s*(.+?)(?:\n|$)', content)
    if topic_match:
        skill['topic'] = topic_match.group(1).strip()

    # Extract skill name
    skill_match = re.search(r'Skill:\s*(.+?)(?:\n|$)', content)
    if skill_match:
        skill['skill'] = skill_match.group(1).strip()

    # Extract description
    desc_match = re.search(r'Description:\s*(.*?)(?=\nDependencies:|\nID:|\Z)', content, re.DOTALL)
    if desc_match:
        skill['description'] = desc_match.group(1).strip()

    # Extract dependencies
    deps_match = re.search(r'Dependencies:\s*\n(.*?)(?=\nID:|\Z)', content, re.DOTALL)
    if deps_match:
        deps_text = deps_match.group(1).strip()
        # Parse each dependency line (format: * T01.G3.02: Description)
        dep_lines = deps_text.split('\n')
        for dep_line in dep_lines:
            dep_line = dep_line.strip()
            if dep_line.startswith('*'):
                # Extract ID and description
                dep_match = re.match(r'\*\s+(T\d+\.G\d+\.\d+):\s*(.+)', dep_line)
                if dep_match:
                    skill['dependencies'].append({
                        'id': dep_match.group(1),
                        'description': dep_match.group(2).strip()
                    })

def format_report(skills):
    """Format skills into a readable report"""

    # Group by topic prefix
    topics = {}
    for skill in skills:
        topic = skill['id'].split('.')[0]  # e.g., T01
        if topic not in topics:
            topics[topic] = []
        topics[topic].append(skill)

    report = []
    report.append("=" * 80)
    report.append("GRADE 5 SKILLS EXTRACTION REPORT")
    report.append("=" * 80)
    report.append("")
    report.append(f"Total G5 Skills Found: {len(skills)}")
    report.append(f"Topics Covered: {len(topics)}")
    report.append("")

    # Summary by topic
    report.append("SUMMARY BY TOPIC")
    report.append("-" * 80)
    for topic_id in sorted(topics.keys()):
        topic_name = topics[topic_id][0]['topic'] if topics[topic_id][0]['topic'] else topic_id
        report.append(f"{topic_id}: {len(topics[topic_id])} skills - {topic_name}")
    report.append("")
    report.append("")

    # Detailed listing
    report.append("=" * 80)
    report.append("DETAILED SKILL LISTING")
    report.append("=" * 80)
    report.append("")

    for topic_id in sorted(topics.keys()):
        report.append("")
        report.append("=" * 80)
        topic_name = topics[topic_id][0]['topic'] if topics[topic_id][0]['topic'] else topic_id
        report.append(f"TOPIC {topic_id}: {topic_name}")
        report.append("=" * 80)
        report.append("")

        for skill in topics[topic_id]:
            report.append("-" * 80)
            report.append(f"Skill ID: {skill['id']}")
            report.append(f"Skill Name: {skill['skill']}")
            report.append("")
            report.append("Description:")
            report.append(skill['description'])
            report.append("")
            report.append(f"Dependencies ({len(skill['dependencies'])}):")
            if skill['dependencies']:
                for dep in skill['dependencies']:
                    report.append(f"  - {dep['id']}: {dep['description']}")
            else:
                report.append("  (None)")
            report.append("")

    return '\n'.join(report)

if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Extracting G5 skills...")
    skills = extract_g5_skills(filepath)

    print(f"Found {len(skills)} G5 skills")

    # Generate report
    report = format_report(skills)

    # Save to file
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G5_COMPLETE_REPORT.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"Report saved to: {output_file}")

    # Also print summary to console
    print("\nSUMMARY:")
    skills_by_topic = {}
    for skill in skills:
        topic = skill['id'].split('.')[0]
        if topic not in skills_by_topic:
            skills_by_topic[topic] = []
        skills_by_topic[topic].append(skill)

    for topic_id in sorted(skills_by_topic.keys()):
        print(f"{topic_id}: {len(skills_by_topic[topic_id])} skills")
