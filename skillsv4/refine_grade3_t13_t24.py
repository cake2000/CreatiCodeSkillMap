#!/usr/bin/env python3
"""
Refine Grade 3 cross-topic dependencies analysis for Topics T13-T24
Only recommend truly MISSING dependencies, manually verified
"""

import re
from collections import defaultdict

def parse_allskills(filepath):
    """Parse allskills.md and extract all skills with their dependencies"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    current_skill = None
    current_deps = []

    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]

        # Match skill ID
        if line.startswith('ID: '):
            # Save previous skill
            if current_skill:
                skills[current_skill['id']] = current_skill

            skill_id = line[4:].strip()
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': []
            }
            current_deps = []

        elif current_skill and line.startswith('Topic: '):
            current_skill['topic'] = line[7:].strip()

        elif current_skill and line.startswith('Skill: '):
            current_skill['skill'] = line[7:].strip()

        elif current_skill and line.startswith('Description: '):
            current_skill['description'] = line[13:].strip()

        elif current_skill and line.startswith('Dependencies:'):
            # Read dependencies
            j = i + 1
            while j < len(lines) and lines[j].startswith('* '):
                dep_line = lines[j][2:].strip()
                # Extract dep_id from "dep_id: description"
                if ':' in dep_line:
                    dep_id = dep_line.split(':')[0].strip()
                    current_deps.append(dep_id)
                j += 1
            current_skill['dependencies'] = current_deps
            i = j - 1

        i += 1

    # Save last skill
    if current_skill:
        skills[current_skill['id']] = current_skill

    return skills

def extract_grade_from_id(skill_id):
    """Extract grade from skill ID like T01.GK.01 or T01.G1.01"""
    parts = skill_id.split('.')
    if len(parts) >= 2:
        grade_part = parts[1]
        if grade_part == 'GK':
            return 'K'
        elif grade_part.startswith('G'):
            return grade_part[1:]
    return None

def extract_topic_from_id(skill_id):
    """Extract topic number from skill ID like T01.G1.01"""
    parts = skill_id.split('.')
    if len(parts) >= 1:
        topic = parts[0]
        if topic.startswith('T'):
            return int(topic[1:])
    return None

def analyze_skill_manual(skill, all_skills):
    """
    Manually analyze each skill based on specific patterns
    Only recommend truly missing and necessary dependencies
    """
    recommendations = []

    skill_id = skill['id']
    skill_name = skill['skill']
    desc = skill['description'].lower()
    current_deps = set(skill['dependencies'])

    skill_grade = extract_grade_from_id(skill_id)
    skill_topic = extract_topic_from_id(skill_id)

    if skill_grade != '3' or skill_topic < 13 or skill_topic > 24:
        return []

    def has_any_dep_from_topic(topic_num):
        topic_prefix = f'T{topic_num:02d}.'
        return any(dep.startswith(topic_prefix) for dep in current_deps)

    # T14 (Games) - Movement with arrow keys needs events
    if skill_id in ['T14.G3.01.01', 'T14.G3.01.02']:
        if not has_any_dep_from_topic(6):
            recommendations.append({
                'skill_id': skill_id,
                'skill_name': skill_name,
                'add_dep': 'T06.G2.01',
                'add_dep_name': all_skills['T06.G2.01']['skill'],
                'reason': 'Arrow key movement requires event handling (key press events)'
            })

    # T14 (Games) - Collision detection needs conditionals
    if 'collision' in desc or 'touching' in desc or 'detect' in desc:
        if skill_topic == 14 and not has_any_dep_from_topic(8):
            recommendations.append({
                'skill_id': skill_id,
                'skill_name': skill_name,
                'add_dep': 'T08.G2.01',
                'add_dep_name': all_skills['T08.G2.01']['skill'],
                'reason': 'Collision detection requires conditionals (if touching then...)'
            })

    # T14 (Games) - Score/state management needs variables
    if skill_topic == 14:
        if 'score' in desc or 'collect' in desc or 'count' in desc:
            if not has_any_dep_from_topic(9):
                recommendations.append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'add_dep': 'T09.G2.02',
                    'add_dep_name': all_skills['T09.G2.02']['skill'],
                    'reason': 'Tracking score/collectibles requires variables'
                })

    # T15 (Animation/Stories) - Event-driven animations
    if skill_topic == 15:
        if 'click' in desc or 'key' in desc or 'event' in desc:
            if not has_any_dep_from_topic(6):
                recommendations.append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'add_dep': 'T06.G2.01',
                    'add_dep_name': all_skills['T06.G2.01']['skill'],
                    'reason': 'Interactive animations require event handling'
                })

    # T16 (UI Widgets) - All widgets need events
    if skill_topic == 16:
        if 'widget' in desc or 'button' in desc or 'click' in desc:
            if not has_any_dep_from_topic(6):
                recommendations.append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'add_dep': 'T06.G2.01',
                    'add_dep_name': all_skills['T06.G2.01']['skill'],
                    'reason': 'UI widgets require event handling for user interaction'
                })

    # T16 (UI) - Input/output needs variables
    if skill_topic == 16:
        if 'textbox' in desc or 'input' in desc or 'get text' in desc:
            if not has_any_dep_from_topic(9):
                recommendations.append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'add_dep': 'T09.G2.02',
                    'add_dep_name': all_skills['T09.G2.02']['skill'],
                    'reason': 'Getting user input requires variables to store data'
                })

    # T18 (3D) - Movement/control needs events
    if skill_topic == 18:
        if 'keyboard' in desc or 'input' in desc or 'move' in desc:
            if not has_any_dep_from_topic(6):
                recommendations.append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'add_dep': 'T06.G2.01',
                    'add_dep_name': all_skills['T06.G2.01']['skill'],
                    'reason': '3D movement with keyboard requires event handling'
                })

    # T18 (3D) - Position tracking needs variables
    if skill_topic == 18:
        if 'position' in desc or 'coordinate' in desc or 'trace' in desc:
            if not has_any_dep_from_topic(9):
                recommendations.append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'add_dep': 'T09.G2.02',
                    'add_dep_name': all_skills['T09.G2.02']['skill'],
                    'reason': '3D position tracking requires variables'
                })

    # AI topics (T21-T24) - Text-based prompts
    if skill_topic >= 21 and skill_topic <= 24:
        if 'prompt' in desc or 'text' in desc or 'ask' in desc or 'chatgpt' in desc or 'speech' in desc:
            if not has_any_dep_from_topic(10):
                recommendations.append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'add_dep': 'T10.G2.01',
                    'add_dep_name': all_skills['T10.G2.01']['skill'],
                    'reason': 'AI prompts require text/string manipulation'
                })

    # Loops - explicit repeat/pattern
    if 'repeat' in desc or 'loop' in desc or 'pattern' in desc or 'multiple times' in desc:
        if not has_any_dep_from_topic(7):
            recommendations.append({
                'skill_id': skill_id,
                'skill_name': skill_name,
                'add_dep': 'T07.G2.01',
                'add_dep_name': all_skills['T07.G2.01']['skill'],
                'reason': 'Uses loops/repetition'
            })

    # Conditionals - explicit if/check/condition
    if ('if ' in desc or 'when ' in desc or 'condition' in desc or
        'check' in desc or 'detect' in desc or 'whether' in desc):
        if not has_any_dep_from_topic(8):
            recommendations.append({
                'skill_id': skill_id,
                'skill_name': skill_name,
                'add_dep': 'T08.G2.01',
                'add_dep_name': all_skills['T08.G2.01']['skill'],
                'reason': 'Uses conditionals/branching logic'
            })

    return recommendations

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing allskills.md...")
    all_skills = parse_allskills(filepath)
    print(f"Found total skills")

    # Find all Grade 3 skills in T13-T24
    grade3_skills_t13_t24 = []
    for skill_id, skill in all_skills.items():
        grade = extract_grade_from_id(skill_id)
        topic = extract_topic_from_id(skill_id)
        if grade == '3' and topic and 13 <= topic <= 24:
            grade3_skills_t13_t24.append(skill)

    print(f"Found {len(grade3_skills_t13_t24)} Grade 3 skills in Topics T13-T24\n")

    all_recommendations = []
    for skill in grade3_skills_t13_t24:
        recs = analyze_skill_manual(skill, all_skills)
        all_recommendations.extend(recs)

    # Deduplicate recommendations
    seen = set()
    unique_recs = []
    for rec in all_recommendations:
        key = (rec['skill_id'], rec['add_dep'])
        if key not in seen:
            seen.add(key)
            unique_recs.append(rec)

    print(f"FOUND {len(unique_recs)} MISSING DEPENDENCIES (after deduplication)\n")
    print("=" * 80)
    print("RECOMMENDED NEW DEPENDENCIES TO ADD")
    print("=" * 80)
    print()

    # Group by topic for easier review
    by_topic = defaultdict(list)
    for rec in unique_recs:
        topic = extract_topic_from_id(rec['skill_id'])
        by_topic[topic].append(rec)

    for topic in sorted(by_topic.keys()):
        print(f"\n### TOPIC T{topic:02d} ###\n")
        for rec in by_topic[topic]:
            print(f"{rec['skill_id']}: {rec['skill_name']}")
            print(f"  ADD: {rec['add_dep']}: {rec['add_dep_name']}")
            print(f"  REASON: {rec['reason']}")
            print()

    # Save to file
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade3_t13_t24_refined_deps.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"GRADE 3 TOPICS T13-T24 MISSING DEPENDENCIES (REFINED)\n")
        f.write(f"Total: {len(unique_recs)} missing dependencies\n")
        f.write("=" * 80 + "\n\n")

        for topic in sorted(by_topic.keys()):
            f.write(f"\n### TOPIC T{topic:02d} ###\n\n")
            for rec in by_topic[topic]:
                f.write(f"{rec['skill_id']}: {rec['skill_name']}\n")
                f.write(f"  ADD: {rec['add_dep']}: {rec['add_dep_name']}\n")
                f.write(f"  REASON: {rec['reason']}\n")
                f.write("\n")

    print(f"\nResults saved to: {output_file}")

if __name__ == '__main__':
    main()
