#!/usr/bin/env python3
"""
Analyze Grade 3 cross-topic dependencies for Topics T13-T24
Identify MISSING dependencies that should be added
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

def analyze_skill_for_missing_deps(skill, all_skills):
    """Analyze a single skill to find missing cross-topic dependencies"""
    recommendations = []

    skill_id = skill['id']
    skill_name = skill['skill']
    description = skill['description'].lower()
    current_deps = set(skill['dependencies'])

    # Get current skill's grade and topic
    skill_grade = extract_grade_from_id(skill_id)
    skill_topic = extract_topic_from_id(skill_id)

    if skill_grade != '3':
        return []

    # Skip if not in T13-T24
    if skill_topic < 13 or skill_topic > 24:
        return []

    # Helper to check if dependency is already present
    def has_dep(dep_id):
        return dep_id in current_deps

    # Helper to check if any dependency from a topic is present
    def has_any_dep_from_topic(topic_num):
        topic_prefix = f'T{topic_num:02d}.'
        return any(dep.startswith(topic_prefix) for dep in current_deps)

    # Check for loop usage (T07 dependencies)
    loop_keywords = ['repeat', 'loop', 'forever', 'times', 'until', 'while', 'iteration']
    if any(keyword in description for keyword in loop_keywords):
        if not has_any_dep_from_topic(7):
            # Find appropriate T07 dependency based on grade
            for dep_id in all_skills:
                if dep_id.startswith('T07.') and extract_grade_from_id(dep_id) in ['K', '1', '2', '3']:
                    dep_skill = all_skills[dep_id]
                    if 'repeat' in dep_skill['skill'].lower() or 'loop' in dep_skill['skill'].lower():
                        if not has_dep(dep_id):
                            recommendations.append({
                                'skill_id': skill_id,
                                'skill_name': skill_name,
                                'add_dep': dep_id,
                                'add_dep_name': dep_skill['skill'],
                                'reason': f'Uses loops/repetition concept'
                            })
                            break

    # Check for conditional usage (T08 dependencies)
    conditional_keywords = ['if', 'when', 'condition', 'check', 'compare', 'else', 'whether']
    if any(keyword in description for keyword in conditional_keywords):
        if not has_any_dep_from_topic(8):
            # Find appropriate T08 dependency
            for dep_id in all_skills:
                if dep_id.startswith('T08.') and extract_grade_from_id(dep_id) in ['K', '1', '2', '3']:
                    dep_skill = all_skills[dep_id]
                    if 'if' in dep_skill['skill'].lower() or 'condition' in dep_skill['skill'].lower():
                        if not has_dep(dep_id):
                            recommendations.append({
                                'skill_id': skill_id,
                                'skill_name': skill_name,
                                'add_dep': dep_id,
                                'add_dep_name': dep_skill['skill'],
                                'reason': f'Uses conditionals/branching'
                            })
                            break

    # Check for variable usage (T09 dependencies)
    variable_keywords = ['variable', 'store', 'save', 'remember', 'count', 'score', 'value', 'number']
    if any(keyword in description for keyword in variable_keywords):
        if not has_any_dep_from_topic(9):
            # Find appropriate T09 dependency
            for dep_id in all_skills:
                if dep_id.startswith('T09.') and extract_grade_from_id(dep_id) in ['K', '1', '2', '3']:
                    dep_skill = all_skills[dep_id]
                    if 'variable' in dep_skill['skill'].lower():
                        if not has_dep(dep_id):
                            recommendations.append({
                                'skill_id': skill_id,
                                'skill_name': skill_name,
                                'add_dep': dep_id,
                                'add_dep_name': dep_skill['skill'],
                                'reason': f'Uses variables to store data'
                            })
                            break

    # Check for event usage (T06 dependencies)
    event_keywords = ['event', 'click', 'press', 'key', 'button', 'when', 'start', 'trigger', 'broadcast', 'message']
    if any(keyword in description for keyword in event_keywords):
        if not has_any_dep_from_topic(6):
            # Find appropriate T06 dependency
            for dep_id in all_skills:
                if dep_id.startswith('T06.') and extract_grade_from_id(dep_id) in ['K', '1', '2', '3']:
                    dep_skill = all_skills[dep_id]
                    if 'event' in dep_skill['skill'].lower() or 'click' in dep_skill['skill'].lower():
                        if not has_dep(dep_id):
                            recommendations.append({
                                'skill_id': skill_id,
                                'skill_name': skill_name,
                                'add_dep': dep_id,
                                'add_dep_name': dep_skill['skill'],
                                'reason': f'Uses events for interaction'
                            })
                            break

    # Check for text/string usage (T10 dependencies)
    text_keywords = ['text', 'string', 'message', 'say', 'ask', 'answer', 'input', 'output']
    if any(keyword in description for keyword in text_keywords):
        if not has_any_dep_from_topic(10):
            # Find appropriate T10 dependency
            for dep_id in all_skills:
                if dep_id.startswith('T10.') and extract_grade_from_id(dep_id) in ['K', '1', '2', '3']:
                    dep_skill = all_skills[dep_id]
                    if 'text' in dep_skill['skill'].lower() or 'string' in dep_skill['skill'].lower():
                        if not has_dep(dep_id):
                            recommendations.append({
                                'skill_id': skill_id,
                                'skill_name': skill_name,
                                'add_dep': dep_id,
                                'add_dep_name': dep_skill['skill'],
                                'reason': f'Uses text/strings'
                            })
                            break

    # Topic-specific checks

    # T14 (Games) should use loops, conditionals, variables
    if skill_topic == 14:
        game_keywords = ['game', 'player', 'win', 'lose', 'collision', 'hit', 'catch']
        if any(keyword in description for keyword in game_keywords):
            # Likely needs variables for scoring/state
            if not has_any_dep_from_topic(9):
                for dep_id in all_skills:
                    if dep_id.startswith('T09.') and extract_grade_from_id(dep_id) in ['K', '1', '2']:
                        dep_skill = all_skills[dep_id]
                        if not has_dep(dep_id):
                            recommendations.append({
                                'skill_id': skill_id,
                                'skill_name': skill_name,
                                'add_dep': dep_id,
                                'add_dep_name': dep_skill['skill'],
                                'reason': f'Games typically need variables for state/scoring'
                            })
                            break

    # T15 (Stories/Animation) should use events, loops
    if skill_topic == 15:
        animation_keywords = ['animate', 'story', 'character', 'scene', 'move', 'transition']
        if any(keyword in description for keyword in animation_keywords):
            # Likely needs events
            if not has_any_dep_from_topic(6):
                for dep_id in all_skills:
                    if dep_id.startswith('T06.') and extract_grade_from_id(dep_id) in ['K', '1', '2']:
                        dep_skill = all_skills[dep_id]
                        if not has_dep(dep_id):
                            recommendations.append({
                                'skill_id': skill_id,
                                'skill_name': skill_name,
                                'add_dep': dep_id,
                                'add_dep_name': dep_skill['skill'],
                                'reason': f'Animations/stories need events for sequencing'
                            })
                            break

    # T16 (UI/widgets) should use events
    if skill_topic == 16:
        ui_keywords = ['button', 'widget', 'input', 'output', 'display', 'interface']
        if any(keyword in description for keyword in ui_keywords):
            if not has_any_dep_from_topic(6):
                for dep_id in all_skills:
                    if dep_id.startswith('T06.') and extract_grade_from_id(dep_id) in ['K', '1', '2']:
                        dep_skill = all_skills[dep_id]
                        if not has_dep(dep_id):
                            recommendations.append({
                                'skill_id': skill_id,
                                'skill_name': skill_name,
                                'add_dep': dep_id,
                                'add_dep_name': dep_skill['skill'],
                                'reason': f'UI widgets need event handling'
                            })
                            break

    # T18 (3D) should use variables, conditionals, loops
    if skill_topic == 18:
        if not has_any_dep_from_topic(9):
            for dep_id in all_skills:
                if dep_id.startswith('T09.') and extract_grade_from_id(dep_id) in ['K', '1', '2']:
                    dep_skill = all_skills[dep_id]
                    if not has_dep(dep_id):
                        recommendations.append({
                            'skill_id': skill_id,
                            'skill_name': skill_name,
                            'add_dep': dep_id,
                            'add_dep_name': dep_skill['skill'],
                            'reason': f'3D projects often need variables for positions/states'
                        })
                        break

    # AI topics (T21-T24) should use variables, conditionals, text
    if skill_topic >= 21 and skill_topic <= 24:
        if not has_any_dep_from_topic(10):
            for dep_id in all_skills:
                if dep_id.startswith('T10.') and extract_grade_from_id(dep_id) in ['K', '1', '2']:
                    dep_skill = all_skills[dep_id]
                    if not has_dep(dep_id):
                        recommendations.append({
                            'skill_id': skill_id,
                            'skill_name': skill_name,
                            'add_dep': dep_id,
                            'add_dep_name': dep_skill['skill'],
                            'reason': f'AI skills typically work with text/prompts'
                        })
                        break

    return recommendations

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing allskills.md...")
    all_skills = parse_allskills(filepath)
    print(f"Found {len(all_skills)} total skills")

    # Find all Grade 3 skills in T13-T24
    grade3_skills_t13_t24 = []
    for skill_id, skill in all_skills.items():
        grade = extract_grade_from_id(skill_id)
        topic = extract_topic_from_id(skill_id)
        if grade == '3' and topic and 13 <= topic <= 24:
            grade3_skills_t13_t24.append(skill)

    print(f"Found {len(grade3_skills_t13_t24)} Grade 3 skills in Topics T13-T24")
    print("\nAnalyzing for missing cross-topic dependencies...\n")

    all_recommendations = []
    for skill in grade3_skills_t13_t24:
        recs = analyze_skill_for_missing_deps(skill, all_skills)
        all_recommendations.extend(recs)

    # Output recommendations
    print(f"FOUND {len(all_recommendations)} MISSING DEPENDENCIES\n")
    print("=" * 80)
    print("RECOMMENDED NEW DEPENDENCIES TO ADD")
    print("=" * 80)
    print()

    for rec in all_recommendations:
        print(f"SKILL_ID: {rec['skill_id']}: {rec['skill_name']}")
        print(f"ADD DEPENDENCY: {rec['add_dep']}: {rec['add_dep_name']}")
        print(f"REASON: {rec['reason']}")
        print()

    # Save to file
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade3_t13_t24_missing_deps.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"GRADE 3 TOPICS T13-T24 MISSING DEPENDENCIES\n")
        f.write(f"Total: {len(all_recommendations)} missing dependencies found\n")
        f.write("=" * 80 + "\n\n")

        for rec in all_recommendations:
            f.write(f"SKILL_ID: {rec['skill_id']}: {rec['skill_name']}\n")
            f.write(f"ADD DEPENDENCY: {rec['add_dep']}: {rec['add_dep_name']}\n")
            f.write(f"REASON: {rec['reason']}\n")
            f.write("\n")

    print(f"\nResults saved to: {output_file}")

if __name__ == '__main__':
    main()
