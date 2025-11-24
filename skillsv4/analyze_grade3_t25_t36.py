#!/usr/bin/env python3
"""
Analyze Grade 3 cross-topic dependencies for Topics T25-T36
Identify MISSING dependencies that should be added
"""

import re

def parse_skill(lines, start_idx):
    """Parse a single skill entry"""
    skill = {
        'id': '',
        'topic': '',
        'skill': '',
        'description': '',
        'dependencies': []
    }

    i = start_idx
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith('ID: '):
            skill['id'] = line.replace('ID: ', '').strip()
        elif line.startswith('Topic: '):
            skill['topic'] = line.replace('Topic: ', '').strip()
        elif line.startswith('Skill: '):
            skill['skill'] = line.replace('Skill: ', '').strip()
        elif line.startswith('Description: '):
            skill['description'] = line.replace('Description: ', '').strip()
        elif line.startswith('Dependencies:'):
            # Parse dependencies
            i += 1
            while i < len(lines) and lines[i].strip().startswith('* '):
                dep_line = lines[i].strip()[2:]  # Remove '* '
                if ':' in dep_line:
                    dep_id = dep_line.split(':')[0].strip()
                    skill['dependencies'].append(dep_id)
                i += 1
            continue
        elif line.startswith('ID: ') and i > start_idx:
            # Next skill
            break

        i += 1

    return skill, i

def extract_grade3_skills(filename):
    """Extract all Grade 3 skills from T25-T36"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    grade3_skills = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Look for Grade 3 skills in T25-T36
        if line.startswith('ID: ') and '.G3.' in line:
            skill_id = line.replace('ID: ', '').strip()
            # Check if it's T25-T36
            topic_num = int(skill_id.split('.')[0][1:])  # Extract topic number
            if 25 <= topic_num <= 36:
                skill, next_i = parse_skill(lines, i)
                grade3_skills.append(skill)
                i = next_i
                continue

        i += 1

    return grade3_skills

def analyze_dependencies(skills):
    """Analyze each skill and identify missing cross-topic dependencies"""
    recommendations = []

    for skill in skills:
        skill_id = skill['id']
        description = skill['description'].lower()
        current_deps = set(skill['dependencies'])

        missing = []

        # Check for loop usage
        loop_keywords = ['repeat', 'loop', 'forever', 'times', 'until', 'while']
        if any(kw in description for kw in loop_keywords):
            # Should depend on T07 (Loops)
            has_loop_dep = any(dep.startswith('T07.') for dep in current_deps)
            if not has_loop_dep:
                missing.append({
                    'type': 'T07 - Loops',
                    'reason': 'Uses loops/repetition'
                })

        # Check for conditional usage
        conditional_keywords = ['if', 'when', 'check', 'condition', 'choose', 'decide', 'compare']
        if any(kw in description for kw in conditional_keywords):
            # Should depend on T08 (Conditionals)
            has_cond_dep = any(dep.startswith('T08.') for dep in current_deps)
            if not has_cond_dep:
                missing.append({
                    'type': 'T08 - Conditionals',
                    'reason': 'Uses conditionals/decisions'
                })

        # Check for variable usage
        variable_keywords = ['variable', 'store', 'save', 'value', 'score', 'counter', 'track']
        if any(kw in description for kw in variable_keywords):
            # Should depend on T09 (Variables)
            has_var_dep = any(dep.startswith('T09.') for dep in current_deps)
            if not has_var_dep:
                missing.append({
                    'type': 'T09 - Variables',
                    'reason': 'Uses variables/storage'
                })

        # Check for list/array usage
        list_keywords = ['list', 'array', 'collection', 'dataset', 'multiple', 'items']
        if any(kw in description for kw in list_keywords):
            # Should depend on T10 (Lists)
            has_list_dep = any(dep.startswith('T10.') for dep in current_deps)
            if not has_list_dep:
                missing.append({
                    'type': 'T10 - Lists',
                    'reason': 'Uses lists/collections'
                })

        # Check for event usage
        event_keywords = ['event', 'trigger', 'when clicked', 'when pressed', 'broadcast', 'message']
        if any(kw in description for kw in event_keywords):
            # Should depend on T06 (Events)
            has_event_dep = any(dep.startswith('T06.') for dep in current_deps)
            if not has_event_dep:
                missing.append({
                    'type': 'T06 - Events',
                    'reason': 'Uses events/triggers'
                })

        # Check for random/probability
        random_keywords = ['random', 'chance', 'probability', 'pick']
        if any(kw in description for kw in random_keywords):
            # Should depend on T11 (Random)
            has_random_dep = any(dep.startswith('T11.') for dep in current_deps)
            if not has_random_dep:
                missing.append({
                    'type': 'T11 - Random',
                    'reason': 'Uses randomness'
                })

        # Check for sequence/algorithm usage
        sequence_keywords = ['sequence', 'steps', 'order', 'algorithm', 'procedure']
        if any(kw in description for kw in sequence_keywords):
            # Should depend on T01 (Algorithms)
            has_seq_dep = any(dep.startswith('T01.') for dep in current_deps)
            if not has_seq_dep:
                missing.append({
                    'type': 'T01 - Algorithms',
                    'reason': 'Uses sequences/algorithms'
                })

        # Check for user interface elements
        ui_keywords = ['button', 'click', 'input', 'user', 'interface', 'display', 'show']
        if any(kw in description for kw in ui_keywords):
            # Should depend on T04 (User Interface)
            has_ui_dep = any(dep.startswith('T04.') for dep in current_deps)
            if not has_ui_dep:
                missing.append({
                    'type': 'T04 - User Interface',
                    'reason': 'Uses UI elements'
                })

        # Check for function/procedure usage
        function_keywords = ['function', 'procedure', 'custom block', 'define', 'reuse']
        if any(kw in description for kw in function_keywords):
            # Should depend on T05 (Functions)
            has_func_dep = any(dep.startswith('T05.') for dep in current_deps)
            if not has_func_dep:
                missing.append({
                    'type': 'T05 - Functions',
                    'reason': 'Uses functions/procedures'
                })

        if missing:
            recommendations.append({
                'skill': skill,
                'missing': missing
            })

    return recommendations

def main():
    filename = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Extracting Grade 3 skills from Topics T25-T36...")
    skills = extract_grade3_skills(filename)
    print(f"Found {len(skills)} Grade 3 skills")

    print("\nAnalyzing cross-topic dependencies...")
    recommendations = analyze_dependencies(skills)

    print(f"\n{'='*80}")
    print("GRADE 3 (T25-T36) MISSING CROSS-TOPIC DEPENDENCIES")
    print(f"{'='*80}\n")

    if not recommendations:
        print("No missing dependencies found!")
    else:
        for rec in recommendations:
            skill = rec['skill']
            print(f"SKILL_ID: {skill['id']}")
            print(f"SKILL_NAME: {skill['skill']}")
            print(f"CURRENT_DEPS: {len(skill['dependencies'])} dependencies")

            for miss in rec['missing']:
                print(f"  ADD DEPENDENCY: {miss['type']}")
                print(f"  REASON: {miss['reason']}")

            print(f"  DESCRIPTION: {skill['description'][:150]}...")
            print()

    # Save to file
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade3_t25_t36_recommendations.txt'
    with open(output_file, 'w', encoding='utf-8') as f:
        for rec in recommendations:
            skill = rec['skill']
            f.write(f"SKILL_ID: {skill['id']}\n")
            f.write(f"SKILL_NAME: {skill['skill']}\n")

            for miss in rec['missing']:
                f.write(f"ADD DEPENDENCY: {miss['type']}\n")
                f.write(f"REASON: {miss['reason']}\n")

            f.write(f"\n")

    print(f"\nRecommendations saved to: {output_file}")
    print(f"\nTotal skills analyzed: {len(skills)}")
    print(f"Skills with missing dependencies: {len(recommendations)}")

if __name__ == '__main__':
    main()
