#!/usr/bin/env python3
"""
Refined analysis of Grade 2 skills (T21-T36) for missing cross-topic dependencies.
This version does deeper content analysis and follows conservative dependency addition.
"""

import re
from collections import defaultdict

def parse_skills(filepath):
    """Parse the allskills.md file and extract skills with their dependencies."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by ID: markers
    skill_blocks = re.split(r'\n(?=ID: )', content)

    skills = []
    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID:'):
            continue

        # Extract skill ID
        id_match = re.search(r'ID:\s*(\S+)', block)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic
        topic_match = re.search(r'Topic:\s*([^\n]+)', block)
        topic = topic_match.group(1).strip() if topic_match else ""

        # Extract skill name
        skill_match = re.search(r'Skill:\s*([^\n]+)', block)
        skill_name = skill_match.group(1).strip() if skill_match else ""

        # Extract description
        desc_match = re.search(r'Description:\s*(.*?)(?=\n(?:Activity Type:|Estimated Time:|CSTA:|Dependencies:|ID:|$))', block, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        deps = []
        deps_section = re.search(r'Dependencies:(.*?)(?=\n\n|\Z)', block, re.DOTALL)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'\*\s*([^:]+):', line)
                if dep_match:
                    deps.append(dep_match.group(1).strip())

        skills.append({
            'id': skill_id,
            'topic': topic,
            'skill': skill_name,
            'description': description,
            'dependencies': deps,
            'block': block
        })

    return skills

def extract_grade(skill_id):
    """Extract grade from skill ID (e.g., T01.G2.01 -> 2)"""
    match = re.search(r'\.G(\d+|K)\.', skill_id)
    if match:
        grade = match.group(1)
        return 0 if grade == 'K' else int(grade)
    return None

def extract_topic(skill_id):
    """Extract topic from skill ID (e.g., T01.G2.01 -> T01)"""
    match = re.match(r'(T\d+)', skill_id)
    return match.group(1) if match else None

def find_prerequisite_skill(target_topic, max_grade, all_skills_by_topic, keywords=None):
    """Find a suitable prerequisite skill from target_topic with grade <= max_grade."""
    candidates = all_skills_by_topic.get(target_topic, [])

    for skill in candidates:
        grade = extract_grade(skill['id'])
        if grade is not None and grade <= max_grade:
            if keywords:
                desc_lower = (skill['skill'] + ' ' + skill['description']).lower()
                if any(kw in desc_lower for kw in keywords):
                    return skill['id']
            else:
                return skill['id']

    # If no keyword match, return first skill of appropriate grade
    for skill in candidates:
        grade = extract_grade(skill['id'])
        if grade is not None and grade <= max_grade:
            return skill['id']

    return None

def analyze_grade2_skills_manually(all_skills, skills_by_id, skills_by_topic):
    """Manual analysis of specific Grade 2 skills that need cross-topic dependencies."""

    recommendations = []

    # Helper function to add recommendation
    def add_rec(skill_id, dep_id, reason):
        if dep_id and skill_id in skills_by_id:
            skill = skills_by_id[skill_id]
            if dep_id not in skill['dependencies']:
                recommendations.append({
                    'skill_id': skill_id,
                    'add_dep': dep_id,
                    'reason': reason
                })

    # T21.G2.02 - Checking AI outputs requires ethics understanding
    dep = find_prerequisite_skill('T35', 1, skills_by_topic, ['safe', 'kind', 'right'])
    add_rec('T21.G2.02', dep, 'Understanding why AI needs checking requires ethical awareness about safety and appropriateness')

    # T22.G2.02 - Privacy in chatbots requires security basics
    dep = find_prerequisite_skill('T32', 1, skills_by_topic, ['private', 'personal', 'safe'])
    add_rec('T22.G2.02', dep, 'Recognizing private information requires foundational security/privacy concepts')

    # T23 (Sensors) skills need hardware understanding
    # T23.G2.01, T23.G2.02, T23.G2.03 all involve physical sensors/devices
    hardware_dep = find_prerequisite_skill('T30', 1, skills_by_topic, ['device', 'computer', 'hardware'])
    add_rec('T23.G2.01', hardware_dep, 'Understanding sensors requires basic hardware/device concepts')
    add_rec('T23.G2.02', hardware_dep, 'Understanding sensor limitations requires hardware knowledge')
    add_rec('T23.G2.03', hardware_dep, 'Distinguishing sensor input from commands requires hardware understanding')

    # T24.G2.01 - AI text-to-speech involves programming concepts
    prog_dep = find_prerequisite_skill('T01', 1, skills_by_topic, ['sequence', 'step', 'order'])
    add_rec('T24.G2.01', prog_dep, 'Understanding AI demonstrations with multiple steps requires sequencing concepts')

    # T24.G2.02 - AI capabilities and limitations relates to ethics
    ethics_dep = find_prerequisite_skill('T35', 1, skills_by_topic, ['safe', 'kind'])
    add_rec('T24.G2.02', ethics_dep, 'Understanding what AI can/cannot do includes ethical considerations')

    # T26 (Data Collection) skills need data representation
    data_rep_dep = find_prerequisite_skill('T25', 1, skills_by_topic, ['data', 'information', 'organize'])
    add_rec('T26.G2.01', data_rep_dep, 'Distinguishing data types requires understanding data representation')
    add_rec('T26.G2.03', data_rep_dep, 'Collecting duration data requires understanding how data is represented')
    add_rec('T26.G2.05', data_rep_dep, 'Conducting surveys requires understanding how to structure data')

    # T27 (Data Visualization) skills need data collection AND representation
    data_col_dep = find_prerequisite_skill('T26', 1, skills_by_topic, ['collect', 'data'])
    data_rep_dep2 = find_prerequisite_skill('T25', 1, skills_by_topic, ['data', 'organize'])

    add_rec('T27.G2.01', data_col_dep, 'Creating charts requires understanding data collection')
    add_rec('T27.G2.01', data_rep_dep2, 'Creating charts requires understanding data representation')
    add_rec('T27.G2.04', data_col_dep, 'Analyzing if data answers questions requires understanding data collection')

    # T28.G2.04 - Predicting outcomes uses data/patterns
    add_rec('T28.G2.04', data_col_dep, 'Making predictions requires understanding how data is collected and used')

    # T29.G2.04 - Find/replace is a programming operation
    add_rec('T29.G2.04', prog_dep, 'Find and replace operations require understanding of sequential processing')

    # T31.G2.01 - Internet requires hardware understanding
    add_rec('T31.G2.01', hardware_dep, 'Understanding internet connections requires knowing about computers/devices')

    # T32 (Security) skills need hardware AND ethics
    security_ethics = find_prerequisite_skill('T35', 1, skills_by_topic, ['safe', 'right', 'kind'])

    add_rec('T32.G2.01', hardware_dep, 'Creating passwords requires understanding devices that use them')
    add_rec('T32.G2.01', security_ethics, 'Password security connects to ethical use and safety')

    add_rec('T32.G2.04', hardware_dep, 'Device care requires understanding what devices are')
    add_rec('T32.G2.04', security_ethics, 'Caring for devices responsibly is an ethical practice')

    add_rec('T32.G2.05', hardware_dep, 'Understanding links requires device/internet knowledge')
    add_rec('T32.G2.05', security_ethics, 'Recognizing dangers requires ethical judgment about safety')

    add_rec('T32.G2.06', hardware_dep, 'Understanding authentication requires device knowledge')

    # T33.G2.01 - Connectivity requires network understanding
    network_dep = find_prerequisite_skill('T31', 1, skills_by_topic, ['internet', 'connect', 'network'])
    add_rec('T33.G2.01', network_dep, 'Understanding app connectivity requires network/internet basics')

    # T34.G2.01 - History of computing requires hardware awareness
    add_rec('T34.G2.01', hardware_dep, 'Comparing past/present technology requires hardware understanding')

    # T36.G2.04 - Career awareness includes ethical dimension
    add_rec('T36.G2.04', security_ethics, 'Understanding digital creation careers includes ethical responsibilities')

    return recommendations

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills...")
    all_skills = parse_skills(filepath)

    # Index skills by ID and topic
    skills_by_id = {s['id']: s for s in all_skills}
    skills_by_topic = defaultdict(list)
    for skill in all_skills:
        topic = extract_topic(skill['id'])
        if topic:
            skills_by_topic[topic].append(skill)

    # Filter Grade 2 skills from T21-T36
    target_topics = [f'T{i:02d}' for i in range(21, 37)]
    grade2_skills = []

    for skill in all_skills:
        skill_topic = extract_topic(skill['id'])
        skill_grade = extract_grade(skill['id'])

        if skill_topic in target_topics and skill_grade == 2:
            grade2_skills.append(skill)

    print(f"\nFound {len(grade2_skills)} Grade 2 skills in T21-T36")

    # Perform manual analysis
    recommendations = analyze_grade2_skills_manually(all_skills, skills_by_id, skills_by_topic)

    # Print recommendations
    print("\n" + "=" * 80)
    print("MISSING CROSS-TOPIC DEPENDENCY RECOMMENDATIONS FOR GRADE 2 (T21-T36)")
    print("=" * 80)
    print()

    if not recommendations:
        print("No missing cross-topic dependencies identified.")
    else:
        # Group by skill
        recs_by_skill = defaultdict(list)
        for rec in recommendations:
            recs_by_skill[rec['skill_id']].append(rec)

        for skill_id in sorted(recs_by_skill.keys()):
            skill = skills_by_id.get(skill_id)
            if not skill:
                continue

            print(f"\n{skill_id}: {skill['skill']}")
            print(f"Current deps: {', '.join(skill['dependencies']) if skill['dependencies'] else 'None'}")

            for rec in recs_by_skill[skill_id]:
                dep_skill = skills_by_id.get(rec['add_dep'])
                if dep_skill:
                    print(f"  → Add {rec['add_dep']}: {dep_skill['skill']}")
                    print(f"     Reason: {rec['reason']}")

    print()
    print("=" * 80)
    print(f"Total recommendations: {len(recommendations)}")
    print("=" * 80)

    # Save to file
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade2_t21_t36_refined_deps.txt'
    with open(output_file, 'w') as f:
        f.write("REFINED MISSING CROSS-TOPIC DEPENDENCIES FOR GRADE 2 (T21-T36)\n")
        f.write("=" * 80 + "\n\n")

        recs_by_skill = defaultdict(list)
        for rec in recommendations:
            recs_by_skill[rec['skill_id']].append(rec)

        for skill_id in sorted(recs_by_skill.keys()):
            skill = skills_by_id.get(skill_id)
            if not skill:
                continue

            f.write(f"\n{skill_id}: {skill['skill']}\n")
            f.write(f"Current deps: {', '.join(skill['dependencies']) if skill['dependencies'] else 'None'}\n")

            for rec in recs_by_skill[skill_id]:
                dep_skill = skills_by_id.get(rec['add_dep'])
                if dep_skill:
                    f.write(f"  → Add {rec['add_dep']}: {dep_skill['skill']}\n")
                    f.write(f"     Reason: {rec['reason']}\n")

        f.write(f"\n\nTotal recommendations: {len(recommendations)}\n")

    print(f"\nRecommendations saved to: {output_file}")

if __name__ == '__main__':
    main()
