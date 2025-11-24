#!/usr/bin/env python3
"""
Create JSON export of Grade 1 skills with all details
"""

import re
import json

def parse_allskills():
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into skills by looking for "ID:" markers
    skill_blocks = re.split(r'\n\n+(?=ID:)', content)

    grade_k_skills = {}
    grade_1_skills = {}

    for block in skill_blocks:
        # Extract skill ID
        id_match = re.search(r'^ID:\s*(T\d+\.(?:GK|K|G1|G2)\.\d+)', block, re.MULTILINE)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract title/skill name
        skill_match = re.search(r'^Skill:\s*(.+?)$', block, re.MULTILINE)
        title = skill_match.group(1).strip() if skill_match else "Unknown"

        # Extract description
        desc_match = re.search(r'^Description:\s*(.+?)(?=^(?:Dependencies:|ID:|\Z))', block, re.MULTILINE | re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        dependencies = []
        deps_section = re.search(r'^Dependencies:\s*\n((?:\*\s+.+\n?)+)', block, re.MULTILINE)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'(T\d+\.(?:GK|K|G1|G2)\.\d+):\s*(.+?)$', line)
                if dep_match:
                    dep_id = dep_match.group(1)
                    dep_title = dep_match.group(2).strip()
                    dependencies.append({
                        'id': dep_id,
                        'title': dep_title
                    })

        skill_info = {
            'id': skill_id,
            'title': title,
            'description': description,
            'dependencies': dependencies,
            'topic': skill_id.split('.')[0],
            'grade': 'K' if ('.GK.' in skill_id or '.K.' in skill_id) else skill_id.split('.')[1]
        }

        if '.GK.' in skill_id or re.match(r'T\d+\.K\.\d+', skill_id):
            grade_k_skills[skill_id] = skill_info
        elif '.G1.' in skill_id:
            grade_1_skills[skill_id] = skill_info

    return grade_k_skills, grade_1_skills

def main():
    print("Parsing allskills.md...")
    grade_k_skills, grade_1_skills = parse_allskills()

    print(f"Found {len(grade_k_skills)} Grade K skills")
    print(f"Found {len(grade_1_skills)} Grade 1 skills")

    # Classify dependencies for each G1 skill
    for skill_id, skill in grade_1_skills.items():
        skill['dependency_analysis'] = {
            'same_topic_gk': [],
            'same_topic_g1': [],
            'cross_topic_gk': [],
            'cross_topic_g1': [],
            'invalid': []
        }

        for dep in skill['dependencies']:
            dep_id = dep['id']
            dep_topic = dep_id.split('.')[0]
            is_same_topic = (dep_topic == skill['topic'])

            if '.GK.' in dep_id or re.match(r'T\d+\.K\.\d+', dep_id):
                if dep_id in grade_k_skills:
                    if is_same_topic:
                        skill['dependency_analysis']['same_topic_gk'].append(dep_id)
                    else:
                        skill['dependency_analysis']['cross_topic_gk'].append(dep_id)
                else:
                    skill['dependency_analysis']['invalid'].append(dep_id)
            elif '.G1.' in dep_id:
                if dep_id in grade_1_skills:
                    if is_same_topic:
                        skill['dependency_analysis']['same_topic_g1'].append(dep_id)
                    else:
                        skill['dependency_analysis']['cross_topic_g1'].append(dep_id)
                else:
                    skill['dependency_analysis']['invalid'].append(dep_id)
            else:
                skill['dependency_analysis']['invalid'].append(dep_id)

    # Create export structure
    export_data = {
        'metadata': {
            'total_grade_k_skills': len(grade_k_skills),
            'total_grade_1_skills': len(grade_1_skills),
            'topics': sorted(list(set([s['topic'] for s in grade_1_skills.values()])))
        },
        'grade_k_skills': grade_k_skills,
        'grade_1_skills': grade_1_skills
    }

    # Save JSON
    json_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade_1_skills_complete.json'
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(export_data, f, indent=2, ensure_ascii=False)

    print(f"\nJSON export saved to: {json_file}")

    # Print summary
    print("\n" + "=" * 80)
    print("GRADE 1 SKILLS SUMMARY")
    print("=" * 80)

    total_deps = sum(len(s['dependencies']) for s in grade_1_skills.values())
    same_topic_gk = sum(len(s['dependency_analysis']['same_topic_gk']) for s in grade_1_skills.values())
    same_topic_g1 = sum(len(s['dependency_analysis']['same_topic_g1']) for s in grade_1_skills.values())
    cross_topic_gk = sum(len(s['dependency_analysis']['cross_topic_gk']) for s in grade_1_skills.values())
    cross_topic_g1 = sum(len(s['dependency_analysis']['cross_topic_g1']) for s in grade_1_skills.values())

    print(f"\nTotal Grade 1 skills: {len(grade_1_skills)}")
    print(f"Total dependencies: {total_deps}")
    print(f"  - Same topic Grade K: {same_topic_gk}")
    print(f"  - Same topic Grade 1: {same_topic_g1}")
    print(f"  - Cross-topic Grade K: {cross_topic_gk}")
    print(f"  - Cross-topic Grade 1: {cross_topic_g1}")

    # Most common cross-topic dependencies
    print("\n" + "=" * 80)
    print("MOST COMMON CROSS-TOPIC DEPENDENCIES")
    print("=" * 80)

    cross_topic_counts = {}
    for skill in grade_1_skills.values():
        for dep_id in skill['dependency_analysis']['cross_topic_gk']:
            cross_topic_counts[dep_id] = cross_topic_counts.get(dep_id, 0) + 1

    for dep_id, count in sorted(cross_topic_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
        dep_title = grade_k_skills[dep_id]['title'] if dep_id in grade_k_skills else "Unknown"
        print(f"  {dep_id}: {dep_title} ({count} times)")

if __name__ == '__main__':
    main()
