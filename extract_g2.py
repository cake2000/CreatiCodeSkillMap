#!/usr/bin/env python3
"""Extract and analyze G2 skills from allskills.md"""

import re
from collections import defaultdict

def parse_allskills(filepath):
    """Parse the allskills.md file and extract G2 skills with their dependencies."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries
    skills = []
    current_skill = {}
    lines = content.split('\n')

    i = 0
    while i < len(lines):
        line = lines[i]

        # Start of a new skill
        if line.startswith('ID: '):
            if current_skill and current_skill.get('id', '').find('.G2.') != -1:
                skills.append(current_skill)

            skill_id = line.replace('ID: ', '').strip()
            current_skill = {
                'id': skill_id,
                'topic': '',
                'title': '',
                'description': '',
                'dependencies': []
            }

        elif line.startswith('Topic: ') and current_skill:
            current_skill['topic'] = line.replace('Topic: ', '').strip()

        elif line.startswith('Skill: ') and current_skill:
            current_skill['title'] = line.replace('Skill: ', '').strip()

        elif line.startswith('Description: ') and current_skill:
            current_skill['description'] = line.replace('Description: ', '').strip()

        elif line.startswith('Dependencies:') and current_skill:
            # Read all dependencies
            i += 1
            while i < len(lines) and lines[i].startswith('* '):
                dep_line = lines[i].strip('* ').strip()
                if ':' in dep_line:
                    dep_id = dep_line.split(':')[0].strip()
                    dep_title = ':'.join(dep_line.split(':')[1:]).strip()
                    current_skill['dependencies'].append({
                        'id': dep_id,
                        'title': dep_title
                    })
                i += 1
            continue

        i += 1

    # Don't forget the last skill
    if current_skill and current_skill.get('id', '').find('.G2.') != -1:
        skills.append(current_skill)

    return skills

def analyze_dependencies(skills):
    """Analyze dependency issues for G2 skills."""
    issues = defaultdict(list)

    for skill in skills:
        skill_id = skill['id']

        # Extract grade from skill ID
        match = re.search(r'\.(G\d+|GK)\.', skill_id)
        if not match:
            continue

        skill_grade = match.group(1)

        for dep in skill['dependencies']:
            dep_id = dep['id']

            # Extract grade from dependency ID
            dep_match = re.search(r'\.(G\d+|GK)\.', dep_id)
            if not dep_match:
                issues[skill_id].append(f"Invalid dependency format: {dep_id}")
                continue

            dep_grade = dep_match.group(1)

            # Check if G2 skill depends on G3+ skills
            if skill_grade == 'G2':
                if dep_grade.startswith('G') and dep_grade not in ['GK', 'G1', 'G2']:
                    dep_num = int(dep_grade[1:])
                    if dep_num >= 3:
                        issues[skill_id].append(
                            f"INVALID: G2 skill depends on {dep_grade} skill ({dep_id})"
                        )

                # Check if G2 depends on GK (more than 2 grades lower)
                if dep_grade == 'GK':
                    issues[skill_id].append(
                        f"WARNING: G2 skill depends on K skill ({dep_id}) - may skip G1 bridge"
                    )

    return issues

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Extracting G2 skills...")
    skills = parse_allskills(filepath)

    print(f"\nFound {len(skills)} G2 skills\n")

    # Group by topic
    by_topic = defaultdict(list)
    for skill in skills:
        topic = skill['topic']
        by_topic[topic].append(skill)

    # Analyze dependencies
    issues = analyze_dependencies(skills)

    # Output results
    print("=" * 80)
    print("G2 SKILLS BY TOPIC")
    print("=" * 80)

    for topic in sorted(by_topic.keys()):
        print(f"\n### {topic}")
        print("-" * 80)

        for skill in by_topic[topic]:
            print(f"\nID: {skill['id']}")
            print(f"Title: {skill['title']}")

            if skill['dependencies']:
                print("Dependencies:")
                for dep in skill['dependencies']:
                    print(f"  - {dep['id']}: {dep['title']}")
            else:
                print("Dependencies: None")

            # Show issues if any
            if skill['id'] in issues:
                print("\nISSUES:")
                for issue in issues[skill['id']]:
                    print(f"  ! {issue}")

    # Summary of issues
    print("\n" + "=" * 80)
    print("DEPENDENCY ISSUES SUMMARY")
    print("=" * 80)

    if issues:
        for skill_id in sorted(issues.keys()):
            print(f"\n{skill_id}:")
            for issue in issues[skill_id]:
                print(f"  - {issue}")
    else:
        print("\nNo dependency issues found!")

    print(f"\nTotal G2 skills analyzed: {len(skills)}")
    print(f"Skills with issues: {len(issues)}")

if __name__ == '__main__':
    main()
