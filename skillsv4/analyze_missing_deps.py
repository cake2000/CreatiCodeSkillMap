#!/usr/bin/env python3
"""
Analyze Grade K skills and suggest missing cross-topic dependencies
"""

import re
from collections import defaultdict

def parse_allskills(filepath):
    """Parse allskills.md and extract all Grade K skills"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    sections = content.split('\nID: ')

    for section in sections:
        if not section.strip():
            continue

        if not section.startswith('ID:'):
            section = 'ID: ' + section

        id_match = re.search(r'ID: (T\d+\.GK\.\d+)', section)
        if not id_match:
            continue

        skill_id = id_match.group(1)
        topic_match = re.search(r'Topic: ([^\n]+)', section)
        topic = topic_match.group(1).strip() if topic_match else ''
        skill_match = re.search(r'Skill: ([^\n]+)', section)
        skill_name = skill_match.group(1).strip() if skill_match else ''
        desc_match = re.search(r'Description: ([^\n]+(?:\n(?!Dependencies:|ID:)[^\n]+)*)', section, re.MULTILINE)
        description = desc_match.group(1).strip() if desc_match else ''

        deps = []
        dep_match = re.search(r'Dependencies:\s*\n((?:\* [^\n]+\n?)*)', section, re.MULTILINE)
        if dep_match:
            dep_text = dep_match.group(1)
            for line in dep_text.split('\n'):
                line = line.strip()
                if line.startswith('*'):
                    dep_id_match = re.search(r'(T\d+\.[A-Z0-9]+\.\d+)', line)
                    if dep_id_match:
                        deps.append(dep_id_match.group(1))

        skills[skill_id] = {
            'topic': topic,
            'skill': skill_name,
            'description': description,
            'dependencies': deps,
        }

    return skills

def suggest_dependencies(skill_id, skill_data, all_skills):
    """Suggest missing cross-topic dependencies based on skill content"""
    suggestions = []
    topic_num = skill_id.split('.')[0]
    skill_lower = skill_data['skill'].lower()
    desc_lower = skill_data['description'].lower()
    combined = skill_lower + ' ' + desc_lower

    # Rule 1: Sequencing/ordering → T01 (Everyday Algorithms)
    if topic_num != 'T01' and any(word in combined for word in [
        'order', 'sequence', 'first', 'next', 'last', 'step', 'routine',
        'arrange', 'put in order', 'chronological'
    ]):
        # Should depend on T01.GK.01 (basic ordering)
        if 'T01.GK.01' not in skill_data['dependencies']:
            suggestions.append({
                'dep': 'T01.GK.01',
                'reason': 'Involves sequencing/ordering concepts',
                'confidence': 'high'
            })

    # Rule 2: Patterns → T04 (Algorithm Patterns)
    if topic_num != 'T04' and any(word in combined for word in [
        'pattern', 'repeat', 'repeating', 'over and over', 'again and again'
    ]):
        if 'T04.GK.01' not in skill_data['dependencies']:
            suggestions.append({
                'dep': 'T04.GK.01',
                'reason': 'Involves pattern recognition',
                'confidence': 'high'
            })

    # Rule 3: Sorting/grouping → T10 (Lists & Tables)
    if topic_num != 'T10' and any(word in combined for word in [
        'sort', 'group', 'categor', 'classify', 'organize', 'collection'
    ]):
        if 'T10.GK.01' not in skill_data['dependencies']:
            suggestions.append({
                'dep': 'T10.GK.01',
                'reason': 'Involves sorting/grouping concepts',
                'confidence': 'medium'
            })

    # Rule 4: Problem-solving/decomposition → T03
    if topic_num != 'T03' and any(word in combined for word in [
        'break down', 'part', 'whole', 'component', 'decompose'
    ]):
        if 'T03.GK.01' not in skill_data['dependencies']:
            suggestions.append({
                'dep': 'T03.GK.01',
                'reason': 'Involves problem decomposition',
                'confidence': 'medium'
            })

    # Rule 5: Cause-and-effect → T02/T06 (Events)
    if topic_num not in ['T02', 'T06'] and any(word in combined for word in [
        'cause', 'effect', 'result', 'happens', 'leads to', 'triggers'
    ]):
        if 'T06.GK.01' not in skill_data['dependencies']:
            suggestions.append({
                'dep': 'T06.GK.01',
                'reason': 'Involves cause-and-effect/event concepts',
                'confidence': 'low'
            })

    # Rule 6: Counting/numbers → T09 (Variables)
    if topic_num != 'T09' and any(word in combined for word in [
        'count', 'number', 'score', 'quantity', 'how many'
    ]):
        if 'T09.GK.01' not in skill_data['dependencies']:
            suggestions.append({
                'dep': 'T09.GK.01',
                'reason': 'Involves counting/numerical concepts',
                'confidence': 'medium'
            })

    # Rule 7: Testing/debugging → T13
    if topic_num != 'T13' and any(word in combined for word in [
        'fix', 'wrong', 'error', 'mistake', 'debug', 'correct', 'broken'
    ]):
        if 'T13.GK.01' not in skill_data['dependencies']:
            suggestions.append({
                'dep': 'T13.GK.01',
                'reason': 'Involves error detection/debugging',
                'confidence': 'low'
            })

    # Rule 8: Creative/storytelling → T15
    if topic_num not in ['T14', 'T15', 'T20'] and any(word in combined for word in [
        'story', 'narrat', 'character', 'emotion', 'creative'
    ]):
        if 'T15.GK.01' not in skill_data['dependencies']:
            suggestions.append({
                'dep': 'T15.GK.01',
                'reason': 'Involves storytelling/narrative concepts',
                'confidence': 'low'
            })

    # Rule 9: Data/information → T25/T26
    if topic_num not in ['T25', 'T26', 'T27'] and any(word in combined for word in [
        'data', 'information', 'collect', 'record', 'log'
    ]):
        if 'T25.GK.01' not in skill_data['dependencies']:
            suggestions.append({
                'dep': 'T25.GK.01',
                'reason': 'Involves data/information concepts',
                'confidence': 'low'
            })

    # Rule 10: Devices/technology → T30
    if topic_num not in ['T30', 'T34'] and any(word in combined for word in [
        'device', 'computer', 'tablet', 'technology', 'hardware'
    ]):
        if 'T30.GK.01' not in skill_data['dependencies']:
            suggestions.append({
                'dep': 'T30.GK.01',
                'reason': 'Involves devices/technology',
                'confidence': 'low'
            })

    return suggestions

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = parse_allskills(filepath)

    print("="*80)
    print("MISSING CROSS-TOPIC DEPENDENCY ANALYSIS")
    print("="*80)

    all_suggestions = defaultdict(list)
    stats = {'high': 0, 'medium': 0, 'low': 0}

    for skill_id, skill_data in sorted(skills.items()):
        suggestions = suggest_dependencies(skill_id, skill_data, skills)

        if suggestions:
            all_suggestions[skill_id] = suggestions
            for sugg in suggestions:
                stats[sugg['confidence']] += 1

    print(f"\nTotal skills analyzed: {len(skills)}")
    print(f"Skills with suggestions: {len(all_suggestions)}")
    print(f"High confidence: {stats['high']}")
    print(f"Medium confidence: {stats['medium']}")
    print(f"Low confidence: {stats['low']}")

    print("\n" + "="*80)
    print("DETAILED SUGGESTIONS (High & Medium Confidence)")
    print("="*80)

    for skill_id, suggestions in sorted(all_suggestions.items()):
        skill_data = skills[skill_id]
        high_med = [s for s in suggestions if s['confidence'] in ['high', 'medium']]

        if high_med:
            print(f"\n{skill_id}: {skill_data['skill']}")
            print(f"  Topic: {skill_data['topic']}")
            print(f"  Current deps: {skill_data['dependencies']}")
            print(f"  Suggestions:")
            for sugg in high_med:
                conf_marker = "★★★" if sugg['confidence'] == 'high' else "★★"
                print(f"    {conf_marker} Add {sugg['dep']} - {sugg['reason']}")

    # Save to file for review
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/dependency_suggestions.txt'
    with open(output_file, 'w') as f:
        f.write("GRADE K CROSS-TOPIC DEPENDENCY SUGGESTIONS\n")
        f.write("="*80 + "\n\n")

        for skill_id, suggestions in sorted(all_suggestions.items()):
            skill_data = skills[skill_id]
            f.write(f"\n{skill_id}: {skill_data['skill']}\n")
            f.write(f"Topic: {skill_data['topic']}\n")
            f.write(f"Current dependencies: {', '.join(skill_data['dependencies']) if skill_data['dependencies'] else 'None'}\n")
            f.write(f"Suggestions:\n")
            for sugg in suggestions:
                f.write(f"  [{sugg['confidence']}] {sugg['dep']} - {sugg['reason']}\n")

    print(f"\n\nFull suggestions saved to: {output_file}")

if __name__ == '__main__':
    main()
