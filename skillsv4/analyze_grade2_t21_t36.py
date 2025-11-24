#!/usr/bin/env python3
"""
Analyze Grade 2 skills in topics T21-T36 for missing cross-topic dependencies.
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
        desc_match = re.search(r'Description:\s*([^\n]+(?:\n(?!Dependencies:|ID:)[^\n]+)*)', block)
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

def analyze_skill_for_missing_deps(skill, all_skills_by_id, all_skills_by_topic):
    """Analyze a single Grade 2 skill for missing cross-topic dependencies."""
    recommendations = []

    skill_id = skill['id']
    skill_topic = extract_topic(skill_id)
    description = skill['description'].lower()
    existing_deps = set(skill['dependencies'])

    # Get topics from existing dependencies
    existing_dep_topics = set()
    for dep_id in existing_deps:
        dep_topic = extract_topic(dep_id)
        if dep_topic:
            existing_dep_topics.add(dep_topic)

    # Topic-specific analysis based on content keywords

    # T21 (AI Media) - check for AI basics, ethics
    if skill_topic == 'T21':
        if any(word in description for word in ['ethical', 'bias', 'fair', 'right', 'wrong', 'privacy']):
            if 'T35' not in existing_dep_topics:
                # Find appropriate T35 skills
                for t35_skill in all_skills_by_topic.get('T35', []):
                    if extract_grade(t35_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t35_skill['id'],
                            'reason': 'Ethical concepts require foundational ethics understanding'
                        })
                        break

        if any(word in description for word in ['ai generate', 'ai create', 'machine learning', 'algorithm']):
            if 'T24' not in existing_dep_topics:
                # Find appropriate T24 skills
                for t24_skill in all_skills_by_topic.get('T24', []):
                    if extract_grade(t24_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t24_skill['id'],
                            'reason': 'Understanding AI generation requires AI basics'
                        })
                        break

    # T22 (AI Chat) - check for AI Media, AI basics, security
    elif skill_topic == 'T22':
        if any(word in description for word in ['personal information', 'safe', 'privacy', 'secret', 'password']):
            if 'T32' not in existing_dep_topics:
                for t32_skill in all_skills_by_topic.get('T32', []):
                    if extract_grade(t32_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t32_skill['id'],
                            'reason': 'Privacy and safety concepts require security foundations'
                        })
                        break

        if any(word in description for word in ['ai respond', 'ai answer', 'chatbot']):
            if 'T24' not in existing_dep_topics:
                for t24_skill in all_skills_by_topic.get('T24', []):
                    if extract_grade(t24_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t24_skill['id'],
                            'reason': 'Understanding AI responses requires AI basics'
                        })
                        break

    # T23 (Sensors) - check for hardware, AI
    elif skill_topic == 'T23':
        if any(word in description for word in ['sensor', 'device', 'hardware', 'physical']):
            if 'T30' not in existing_dep_topics:
                for t30_skill in all_skills_by_topic.get('T30', []):
                    if extract_grade(t30_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t30_skill['id'],
                            'reason': 'Sensor usage requires hardware understanding'
                        })
                        break

    # T24 (AI/XO) - check for programming, ethics
    elif skill_topic == 'T24':
        if any(word in description for word in ['block', 'program', 'code', 'sprite', 'costume']):
            if 'T01' not in existing_dep_topics:
                for t01_skill in all_skills_by_topic.get('T01', []):
                    if extract_grade(t01_skill['id']) in [0, 1] and 'sequence' in t01_skill['description'].lower():
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t01_skill['id'],
                            'reason': 'Programming AI features requires sequencing skills'
                        })
                        break

        if any(word in description for word in ['bias', 'fair', 'ethical']):
            if 'T35' not in existing_dep_topics:
                for t35_skill in all_skills_by_topic.get('T35', []):
                    if extract_grade(t35_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t35_skill['id'],
                            'reason': 'Understanding AI bias requires ethics foundation'
                        })
                        break

    # T25 (Data Representation) - check for programming basics
    elif skill_topic == 'T25':
        if any(word in description for word in ['organize', 'sort', 'group', 'category']):
            if 'T01' not in existing_dep_topics:
                for t01_skill in all_skills_by_topic.get('T01', []):
                    if extract_grade(t01_skill['id']) in [0, 1] and 'pattern' in t01_skill['description'].lower():
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t01_skill['id'],
                            'reason': 'Organizing data requires pattern recognition'
                        })
                        break

    # T26 (Data Collection) - check for data representation
    elif skill_topic == 'T26':
        if any(word in description for word in ['record', 'collect', 'tally', 'count']):
            if 'T25' not in existing_dep_topics:
                for t25_skill in all_skills_by_topic.get('T25', []):
                    if extract_grade(t25_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t25_skill['id'],
                            'reason': 'Collecting data requires understanding data representation'
                        })
                        break

    # T27 (Data Visualization) - check for data collection and representation
    elif skill_topic == 'T27':
        if any(word in description for word in ['chart', 'graph', 'visualize', 'display']):
            if 'T26' not in existing_dep_topics:
                for t26_skill in all_skills_by_topic.get('T26', []):
                    if extract_grade(t26_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t26_skill['id'],
                            'reason': 'Visualizing data requires data collection skills'
                        })
                        break

            if 'T25' not in existing_dep_topics:
                for t25_skill in all_skills_by_topic.get('T25', []):
                    if extract_grade(t25_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t25_skill['id'],
                            'reason': 'Visualizing data requires understanding data representation'
                        })
                        break

    # T28 (Probability) - check for data collection
    elif skill_topic == 'T28':
        if any(word in description for word in ['likely', 'unlikely', 'chance', 'predict']):
            if 'T26' not in existing_dep_topics:
                for t26_skill in all_skills_by_topic.get('T26', []):
                    if extract_grade(t26_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t26_skill['id'],
                            'reason': 'Probability analysis requires data collection understanding'
                        })
                        break

    # T29 (Text Processing) - check for algorithms, data
    elif skill_topic == 'T29':
        if any(word in description for word in ['program', 'block', 'code']):
            if 'T01' not in existing_dep_topics:
                for t01_skill in all_skills_by_topic.get('T01', []):
                    if extract_grade(t01_skill['id']) in [0, 1] and 'sequence' in t01_skill['description'].lower():
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t01_skill['id'],
                            'reason': 'Programming text processing requires sequencing'
                        })
                        break

    # T30 (Hardware) - check for algorithms
    elif skill_topic == 'T30':
        if any(word in description for word in ['use', 'operate', 'control']):
            if 'T01' not in existing_dep_topics:
                for t01_skill in all_skills_by_topic.get('T01', []):
                    if extract_grade(t01_skill['id']) in [0, 1] and 'step' in t01_skill['description'].lower():
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t01_skill['id'],
                            'reason': 'Operating hardware requires sequential thinking'
                        })
                        break

    # T31 (Networks) - check for hardware
    elif skill_topic == 'T31':
        if any(word in description for word in ['connect', 'network', 'internet', 'device']):
            if 'T30' not in existing_dep_topics:
                for t30_skill in all_skills_by_topic.get('T30', []):
                    if extract_grade(t30_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t30_skill['id'],
                            'reason': 'Understanding networks requires hardware basics'
                        })
                        break

    # T32 (Security) - check for networks, hardware, ethics
    elif skill_topic == 'T32':
        if any(word in description for word in ['password', 'safe', 'protect', 'secure']):
            if 'T30' not in existing_dep_topics:
                for t30_skill in all_skills_by_topic.get('T30', []):
                    if extract_grade(t30_skill['id']) in [0, 1] and 'device' in t30_skill['description'].lower():
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t30_skill['id'],
                            'reason': 'Device security requires hardware understanding'
                        })
                        break

            if 'T35' not in existing_dep_topics:
                for t35_skill in all_skills_by_topic.get('T35', []):
                    if extract_grade(t35_skill['id']) in [0, 1] and 'safe' in t35_skill['description'].lower():
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t35_skill['id'],
                            'reason': 'Security practices require ethical understanding'
                        })
                        break

    # T33 (Connectivity) - check for networks, hardware
    elif skill_topic == 'T33':
        if any(word in description for word in ['connect', 'wireless', 'internet']):
            if 'T31' not in existing_dep_topics:
                for t31_skill in all_skills_by_topic.get('T31', []):
                    if extract_grade(t31_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t31_skill['id'],
                            'reason': 'Understanding connectivity requires network basics'
                        })
                        break

    # T34 (History) - check for hardware
    elif skill_topic == 'T34':
        if any(word in description for word in ['computer', 'device', 'technology']):
            if 'T30' not in existing_dep_topics:
                for t30_skill in all_skills_by_topic.get('T30', []):
                    if extract_grade(t30_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t30_skill['id'],
                            'reason': 'Understanding computing history requires hardware awareness'
                        })
                        break

    # T35 (Ethics) - check for algorithms, security
    elif skill_topic == 'T35':
        if any(word in description for word in ['program', 'technology']):
            if 'T01' not in existing_dep_topics:
                for t01_skill in all_skills_by_topic.get('T01', []):
                    if extract_grade(t01_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t01_skill['id'],
                            'reason': 'Understanding technology ethics requires basic computing concepts'
                        })
                        break

    # T36 (Careers) - check for ethics, algorithms
    elif skill_topic == 'T36':
        if any(word in description for word in ['job', 'career', 'work']):
            if 'T35' not in existing_dep_topics:
                for t35_skill in all_skills_by_topic.get('T35', []):
                    if extract_grade(t35_skill['id']) in [0, 1]:
                        recommendations.append({
                            'skill_id': skill_id,
                            'add_dep': t35_skill['id'],
                            'reason': 'Understanding computing careers requires ethical awareness'
                        })
                        break

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
    print(f"Topics: {', '.join(target_topics)}\n")

    # Analyze each skill
    all_recommendations = []

    for skill in sorted(grade2_skills, key=lambda s: s['id']):
        recommendations = analyze_skill_for_missing_deps(skill, skills_by_id, skills_by_topic)
        if recommendations:
            all_recommendations.extend(recommendations)

    # Print recommendations
    print("=" * 80)
    print("MISSING CROSS-TOPIC DEPENDENCY RECOMMENDATIONS FOR GRADE 2 (T21-T36)")
    print("=" * 80)
    print()

    if not all_recommendations:
        print("No missing cross-topic dependencies identified.")
    else:
        current_skill = None
        for rec in sorted(all_recommendations, key=lambda r: r['skill_id']):
            if rec['skill_id'] != current_skill:
                if current_skill:
                    print()
                current_skill = rec['skill_id']
                skill = skills_by_id[current_skill]
                print(f"\n{current_skill}: {skill['skill']}")
                print(f"Current deps: {', '.join(skill['dependencies']) if skill['dependencies'] else 'None'}")

            print(f"  → Add dependency {rec['add_dep']} - Reason: {rec['reason']}")

    print()
    print("=" * 80)
    print(f"Total recommendations: {len(all_recommendations)}")
    print("=" * 80)

    # Save to file
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade2_t21_t36_missing_deps.txt'
    with open(output_file, 'w') as f:
        f.write("MISSING CROSS-TOPIC DEPENDENCIES FOR GRADE 2 (T21-T36)\n")
        f.write("=" * 80 + "\n\n")

        for rec in sorted(all_recommendations, key=lambda r: r['skill_id']):
            f.write(f"{rec['skill_id']}: Add dependency {rec['add_dep']} - Reason: {rec['reason']}\n")

        f.write(f"\nTotal recommendations: {len(all_recommendations)}\n")

    print(f"\nRecommendations saved to: {output_file}")

if __name__ == '__main__':
    main()
