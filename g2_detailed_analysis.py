#!/usr/bin/env python3
"""
Detailed G2 Skills Analysis - Creates comprehensive data export
"""

import re
import json
from collections import defaultdict

def parse_skills(filename):
    """Parse all skills from the markdown file"""
    skills = {}
    current_skill = None
    current_deps = []
    in_deps = False

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()

            if line.startswith('ID: '):
                if current_skill:
                    if in_deps:
                        current_skill['dependencies'] = current_deps
                    skills[current_skill['id']] = current_skill

                skill_id = line.replace('ID: ', '').strip()
                current_skill = {
                    'id': skill_id,
                    'topic': '',
                    'skill_name': '',
                    'description': '',
                    'dependencies': []
                }
                current_deps = []
                in_deps = False

            elif line.startswith('Topic: ') and current_skill:
                current_skill['topic'] = line.replace('Topic: ', '').strip()

            elif line.startswith('Skill: ') and current_skill:
                current_skill['skill_name'] = line.replace('Skill: ', '').strip()

            elif line.startswith('Description: ') and current_skill:
                current_skill['description'] = line.replace('Description: ', '').strip()

            elif line.startswith('Dependencies:'):
                in_deps = True
                current_deps = []

            elif in_deps and line.startswith('* '):
                dep_match = re.match(r'\* ([^:]+):', line)
                if dep_match:
                    dep_id = dep_match.group(1).strip()
                    current_deps.append(dep_id)

            elif in_deps and not line.startswith('*') and not line.strip() == '':
                if current_skill:
                    current_skill['dependencies'] = current_deps
                in_deps = False

        if current_skill:
            if in_deps:
                current_skill['dependencies'] = current_deps
            skills[current_skill['id']] = current_skill

    return skills

def get_grade(skill_id):
    """Extract grade from skill ID"""
    match = re.match(r'T\d+\.(GK|G[1-5])', skill_id)
    if match:
        return match.group(1)
    return None

def get_topic(skill_id):
    """Extract topic from skill ID"""
    match = re.match(r'(T\d+)', skill_id)
    if match:
        return match.group(1)
    return None

if __name__ == '__main__':
    filename = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Loading and parsing all skills...")
    skills = parse_skills(filename)

    # Filter G2 skills
    g2_skills = {sid: s for sid, s in skills.items() if get_grade(sid) == 'G2'}

    print(f"Found {len(g2_skills)} G2 skills\n")

    # Group by topic
    by_topic = defaultdict(list)
    for skill_id, skill in sorted(g2_skills.items()):
        topic = get_topic(skill_id)
        by_topic[topic].append(skill)

    # Create detailed report
    output = []
    output.append("=" * 100)
    output.append("G2 SKILLS DETAILED ANALYSIS")
    output.append("=" * 100)
    output.append("")
    output.append(f"Total G2 Skills: {len(g2_skills)}")
    output.append(f"Topics Covered: {len(by_topic)}")
    output.append("")

    # Statistics by topic
    output.append("=" * 100)
    output.append("G2 SKILLS BY TOPIC")
    output.append("=" * 100)
    output.append("")

    for topic in sorted(by_topic.keys()):
        skills_in_topic = by_topic[topic]
        output.append(f"{topic}: {len(skills_in_topic)} skills")

        # Show each skill
        for skill in skills_in_topic:
            output.append(f"  [{skill['id']}] {skill['skill_name']}")
            if skill['dependencies']:
                output.append(f"    Dependencies ({len(skill['dependencies'])}):")
                for dep in skill['dependencies']:
                    dep_grade = get_grade(dep)
                    dep_name = skills.get(dep, {}).get('skill_name', 'UNKNOWN')
                    output.append(f"      - [{dep_grade}] {dep}: {dep_name}")
            else:
                output.append(f"    No dependencies")
        output.append("")

    # Dependency statistics
    output.append("=" * 100)
    output.append("DEPENDENCY STATISTICS")
    output.append("=" * 100)
    output.append("")

    dep_counts = defaultdict(int)
    total_deps = 0

    for skill in g2_skills.values():
        num_deps = len(skill['dependencies'])
        dep_counts[num_deps] += 1
        total_deps += num_deps

    avg_deps = total_deps / len(g2_skills) if g2_skills else 0

    output.append(f"Average dependencies per G2 skill: {avg_deps:.2f}")
    output.append("")
    output.append("Distribution of dependency counts:")
    for count in sorted(dep_counts.keys()):
        output.append(f"  {count} dependencies: {dep_counts[count]} skills ({dep_counts[count]/len(g2_skills)*100:.1f}%)")
    output.append("")

    # Skills with most dependencies
    most_deps = sorted(g2_skills.items(), key=lambda x: len(x[1]['dependencies']), reverse=True)[:10]

    output.append("=" * 100)
    output.append("TOP 10 G2 SKILLS WITH MOST DEPENDENCIES")
    output.append("=" * 100)
    output.append("")

    for skill_id, skill in most_deps:
        output.append(f"[{skill_id}] {skill['skill_name']}")
        output.append(f"  Dependencies: {len(skill['dependencies'])}")
        for dep in skill['dependencies']:
            dep_grade = get_grade(dep)
            output.append(f"    - [{dep_grade}] {dep}")
        output.append("")

    # Export to text file
    report_text = "\n".join(output)

    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/g2_detailed_analysis.txt', 'w') as f:
        f.write(report_text)

    print("Detailed analysis saved to: g2_detailed_analysis.txt")

    # Also export as JSON for programmatic access
    export_data = {
        'metadata': {
            'total_g2_skills': len(g2_skills),
            'total_topics': len(by_topic),
            'average_dependencies': avg_deps,
            'total_dependencies': total_deps
        },
        'skills': {}
    }

    for skill_id, skill in g2_skills.items():
        export_data['skills'][skill_id] = {
            'skill_name': skill['skill_name'],
            'topic': skill['topic'],
            'description': skill['description'],
            'dependencies': skill['dependencies'],
            'dependency_count': len(skill['dependencies']),
            'dependency_grades': [get_grade(dep) for dep in skill['dependencies']]
        }

    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/g2_skills_export.json', 'w') as f:
        json.dump(export_data, f, indent=2)

    print("JSON export saved to: g2_skills_export.json")
    print("")
    print("Summary:")
    print(f"  Total G2 skills: {len(g2_skills)}")
    print(f"  Topics covered: {len(by_topic)}")
    print(f"  Average dependencies: {avg_deps:.2f}")
    print(f"  Total dependencies: {total_deps}")
