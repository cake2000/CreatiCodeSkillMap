#!/usr/bin/env python3
"""Analyze G5 skills dependencies"""

import re
from collections import defaultdict

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

def analyze_dependencies(skills):
    """Analyze dependency patterns in G5 skills"""

    # Statistics
    total_deps = sum(len(skill['dependencies']) for skill in skills)
    skills_with_deps = sum(1 for skill in skills if skill['dependencies'])
    skills_without_deps = len(skills) - skills_with_deps

    # Dependency by grade
    dep_by_grade = defaultdict(int)
    dep_by_topic = defaultdict(int)

    for skill in skills:
        for dep in skill['dependencies']:
            dep_id = dep['id']
            # Extract grade (e.g., GK, G1, G2, etc.)
            grade_match = re.search(r'\.(G[K0-9]+)\.', dep_id)
            if grade_match:
                grade = grade_match.group(1)
                dep_by_grade[grade] += 1

            # Extract topic
            topic = dep_id.split('.')[0]
            dep_by_topic[topic] += 1

    # Most common dependencies
    dep_counts = defaultdict(int)
    for skill in skills:
        for dep in skill['dependencies']:
            dep_counts[dep['id']] += 1

    report = []
    report.append("=" * 80)
    report.append("GRADE 5 SKILLS DEPENDENCY ANALYSIS")
    report.append("=" * 80)
    report.append("")

    # Basic statistics
    report.append("BASIC STATISTICS")
    report.append("-" * 80)
    report.append(f"Total G5 Skills: {len(skills)}")
    report.append(f"Total Dependencies: {total_deps}")
    report.append(f"Average Dependencies per Skill: {total_deps / len(skills):.2f}")
    report.append(f"Skills with Dependencies: {skills_with_deps} ({100*skills_with_deps/len(skills):.1f}%)")
    report.append(f"Skills without Dependencies: {skills_without_deps} ({100*skills_without_deps/len(skills):.1f}%)")
    report.append("")

    # Dependencies by grade
    report.append("DEPENDENCIES BY GRADE")
    report.append("-" * 80)
    for grade in sorted(dep_by_grade.keys()):
        report.append(f"{grade}: {dep_by_grade[grade]} dependencies")
    report.append("")

    # Dependencies by topic
    report.append("DEPENDENCIES BY TOPIC (Top 20)")
    report.append("-" * 80)
    sorted_topics = sorted(dep_by_topic.items(), key=lambda x: x[1], reverse=True)[:20]
    for topic, count in sorted_topics:
        report.append(f"{topic}: {count} dependencies")
    report.append("")

    # Most referenced skills
    report.append("MOST REFERENCED SKILLS (Top 30)")
    report.append("-" * 80)
    sorted_deps = sorted(dep_counts.items(), key=lambda x: x[1], reverse=True)[:30]
    for dep_id, count in sorted_deps:
        report.append(f"{dep_id}: referenced {count} times")
    report.append("")

    # Skills by dependency count
    report.append("G5 SKILLS BY DEPENDENCY COUNT")
    report.append("-" * 80)
    skills_by_dep_count = defaultdict(list)
    for skill in skills:
        count = len(skill['dependencies'])
        skills_by_dep_count[count].append(skill)

    for count in sorted(skills_by_dep_count.keys(), reverse=True):
        report.append(f"\n{count} Dependencies ({len(skills_by_dep_count[count])} skills):")
        for skill in sorted(skills_by_dep_count[count], key=lambda x: x['id']):
            report.append(f"  - {skill['id']}: {skill['skill']}")

    return '\n'.join(report)

if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Extracting G5 skills...")
    skills = extract_g5_skills(filepath)

    print(f"Found {len(skills)} G5 skills")

    # Analyze dependencies
    analysis = analyze_dependencies(skills)

    # Save to file
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G5_DEPENDENCY_ANALYSIS.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(analysis)

    print(f"Analysis saved to: {output_file}")
    print("\n" + analysis)
