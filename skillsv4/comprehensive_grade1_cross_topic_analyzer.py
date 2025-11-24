#!/usr/bin/env python3
"""
Comprehensive analysis of Grade 1 cross-topic dependencies.
Uses liberal dependency identification across all topics.
"""

import re
from collections import defaultdict

def parse_skills(filename):
    """Parse the allskills.md file and extract skills with their dependencies."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    current_skill = None
    current_deps = []

    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith('ID: '):
            if current_skill:
                skills[current_skill['id']] = current_skill

            skill_id = line.replace('ID: ', '').strip()
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': []
            }
            current_deps = []

        elif current_skill:
            if line.startswith('Topic: '):
                current_skill['topic'] = line.replace('Topic: ', '').strip()
            elif line.startswith('Skill: '):
                current_skill['skill'] = line.replace('Skill: ', '').strip()
            elif line.startswith('Description: '):
                current_skill['description'] = line.replace('Description: ', '').strip()
            elif line.startswith('Dependencies:'):
                j = i + 1
                while j < len(lines) and lines[j].startswith('* '):
                    dep_line = lines[j].strip()[2:]
                    if ':' in dep_line:
                        dep_id = dep_line.split(':')[0].strip()
                        current_deps.append(dep_id)
                    j += 1
                current_skill['dependencies'] = current_deps
                i = j - 1

        i += 1

    if current_skill:
        skills[current_skill['id']] = current_skill

    return skills

def get_topic_from_id(skill_id):
    """Extract topic code from skill ID"""
    match = re.match(r'(T\d+)\.', skill_id)
    return match.group(1) if match else None

def get_grade_from_id(skill_id):
    """Extract grade from skill ID"""
    match = re.match(r'T\d+\.(GK|G[0-9]+)\.', skill_id)
    return match.group(1) if match else None

def has_cross_topic_dep(skill, target_topic):
    """Check if skill already has a dependency from target topic"""
    return any(get_topic_from_id(d) == target_topic for d in skill['dependencies'])

def find_best_dep_in_topic(skills, topic, grade_limit, keywords=None):
    """Find the best dependency skill in a topic based on keywords"""
    candidates = []
    for skill_id, skill in skills.items():
        if get_topic_from_id(skill_id) != topic:
            continue
        grade = get_grade_from_id(skill_id)
        if grade not in ['GK', grade_limit]:
            continue

        score = 0
        text = (skill['skill'] + ' ' + skill['description']).lower()

        if keywords:
            for kw in keywords:
                if kw in text:
                    score += 1

        candidates.append((skill_id, score))

    candidates.sort(key=lambda x: (-x[1], x[0]))  # Sort by score desc, then ID
    return candidates[0][0] if candidates else None

def comprehensive_analysis(skills):
    """Perform comprehensive cross-topic dependency analysis"""

    g1_skills = {k: v for k, v in skills.items() if get_grade_from_id(k) == 'G1'}
    gk_skills = {k: v for k, v in skills.items() if get_grade_from_id(k) == 'GK'}
    all_available = {**gk_skills, **g1_skills}

    recommendations = []

    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)
        text = (skill['skill'] + ' ' + skill['description']).lower()

        # === ALGORITHMIC THINKING DEPENDENCIES ===

        # Any skill involving "steps", "sequence", "order" needs T01 (Everyday Algorithms)
        if any(kw in text for kw in ['step', 'sequence', 'order', 'routine', 'process']):
            if not has_cross_topic_dep(skill, 'T01') and topic != 'T01':
                dep = find_best_dep_in_topic(all_available, 'T01', 'G1', ['order', 'sequence', 'step'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Requires understanding sequential steps"))

        # "Algorithm", "instruction", "direction" skills need T02 (Algorithm Design)
        if any(kw in text for kw in ['algorithm', 'instruction', 'direction', 'procedure']):
            if not has_cross_topic_dep(skill, 'T02') and topic not in ['T01', 'T02']:
                dep = find_best_dep_in_topic(all_available, 'T02', 'G1', ['algorithm', 'instruction'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Requires understanding how algorithms work"))

        # === DECOMPOSITION DEPENDENCIES ===

        # "Break down", "parts", "divide", "component" needs T03 (Decomposition)
        if any(kw in text for kw in ['break', 'part', 'divide', 'component', 'separate', 'piece']):
            if not has_cross_topic_dep(skill, 'T03') and topic != 'T03':
                dep = find_best_dep_in_topic(all_available, 'T03', 'G1', ['part', 'break', 'group'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Requires understanding breaking tasks into parts"))

        # === PATTERN RECOGNITION DEPENDENCIES ===

        # "Pattern", "repeat", "same", "similar" needs T04 (Pattern Recognition)
        if any(kw in text for kw in ['pattern', 'repeat', 'repeating', 'similar', 'same']):
            if not has_cross_topic_dep(skill, 'T04') and topic != 'T04':
                dep = find_best_dep_in_topic(all_available, 'T04', 'G1', ['pattern', 'repeat'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Requires recognizing patterns and repetition"))

        # === DESIGN THINKING DEPENDENCIES ===

        # "Design", "create", "make", "plan" needs T05 (Design Thinking)
        if any(kw in text for kw in ['design', 'create', 'plan', 'solution', 'need', 'user']):
            if not has_cross_topic_dep(skill, 'T05') and topic != 'T05':
                if 'user' in text or 'need' in text or 'solution' in text:
                    dep = find_best_dep_in_topic(all_available, 'T05', 'G1', ['need', 'design', 'user'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Requires design thinking approach"))

        # === EVENT DEPENDENCIES ===

        # "Event", "trigger", "when", "cause" needs T06 (Events)
        if any(kw in text for kw in ['event', 'trigger', 'when', 'cause', 'happen', 'start']):
            if not has_cross_topic_dep(skill, 'T06') and topic != 'T06':
                dep = find_best_dep_in_topic(all_available, 'T06', 'G1', ['trigger', 'action', 'when'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Requires understanding events and triggers"))

        # === LOOP DEPENDENCIES ===

        # "Loop", "repeat X times", "again", "multiple" needs T07 (Loops)
        if any(kw in text for kw in ['loop', 'times', 'again', 'multiple', 'repetition']):
            if not has_cross_topic_dep(skill, 'T07') and topic != 'T07':
                if 'times' in text or 'repeat' in text:
                    dep = find_best_dep_in_topic(all_available, 'T07', 'G1', ['repeat', 'times', 'count'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Requires understanding loops and repetition counting"))

        # === CONDITIONAL DEPENDENCIES ===

        # "If", "then", "condition", "rule", "sort", "filter" needs T08 (Conditionals)
        if any(kw in text for kw in ['if', 'then', 'condition', 'rule', 'sort', 'filter', 'when']):
            if not has_cross_topic_dep(skill, 'T08') and topic != 'T08':
                if ('if' in text and 'then' in text) or 'rule' in text:
                    dep = find_best_dep_in_topic(all_available, 'T08', 'G1', ['if', 'then', 'rule', 'sort'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Requires understanding conditional logic"))

        # === VARIABLE DEPENDENCIES ===

        # "Count", "track", "store", "remember", "score" needs T09 (Variables)
        if any(kw in text for kw in ['count', 'track', 'store', 'remember', 'score', 'number']):
            if not has_cross_topic_dep(skill, 'T09') and topic != 'T09':
                if 'count' in text or 'track' in text or 'score' in text:
                    dep = find_best_dep_in_topic(all_available, 'T09', 'G1', ['count', 'track'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Requires understanding counting/tracking"))

        # === DATA STRUCTURE DEPENDENCIES ===

        # "Table", "list", "organize", "sort", "group" needs T10 (Data Structures)
        if any(kw in text for kw in ['table', 'list', 'organize', 'sort', 'group', 'category']):
            if not has_cross_topic_dep(skill, 'T10') and topic != 'T10':
                if 'sort' in text or 'table' in text or 'list' in text:
                    dep = find_best_dep_in_topic(all_available, 'T10', 'G1', ['sort', 'table', 'organize'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Requires understanding data organization"))

        # === ABSTRACTION DEPENDENCIES ===

        # "Abstract", "generalize", "simplify", "represent" needs T12 (Abstraction)
        if any(kw in text for kw in ['abstract', 'general', 'simplify', 'represent', 'symbol']):
            if not has_cross_topic_dep(skill, 'T12') and topic != 'T12':
                dep = find_best_dep_in_topic(all_available, 'T12', 'G1', ['group', 'similar', 'represent'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Requires understanding abstraction"))

        # === DEBUGGING DEPENDENCIES ===

        # "Debug", "error", "fix", "mistake", "wrong" needs T13 (Debugging)
        if any(kw in text for kw in ['debug', 'error', 'fix', 'mistake', 'wrong', 'correct']):
            if not has_cross_topic_dep(skill, 'T13') and topic != 'T13':
                # Also needs algorithm understanding
                if not has_cross_topic_dep(skill, 'T01'):
                    dep = find_best_dep_in_topic(all_available, 'T01', 'G1', ['fix', 'wrong', 'mistake'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Debugging requires understanding algorithms"))

        # === GAME DESIGN DEPENDENCIES ===

        # Games with "rules", "goal", "win" need T14 (Game Design)
        if topic == 'T14':
            # Game design should depend on conditionals for rules
            if 'rule' in text and not has_cross_topic_dep(skill, 'T08'):
                dep = find_best_dep_in_topic(all_available, 'T08', 'G1', ['rule', 'if', 'sort'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Game rules use conditional logic"))
            # Game design should depend on variables for scoring
            if 'score' in text or 'point' in text:
                if not has_cross_topic_dep(skill, 'T09'):
                    dep = find_best_dep_in_topic(all_available, 'T09', 'G1', ['count', 'track'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Scoring requires tracking/counting"))

        # === STORYTELLING DEPENDENCIES ===

        # Stories with sequence need T01 (Algorithms)
        if topic == 'T15':
            if 'sequence' in text or 'order' in text:
                if not has_cross_topic_dep(skill, 'T01'):
                    dep = find_best_dep_in_topic(all_available, 'T01', 'G1', ['sequence', 'order', 'story'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Story sequencing uses algorithmic thinking"))
            # Stories with consequences need conditionals
            if 'consequence' in text or 'result' in text:
                if not has_cross_topic_dep(skill, 'T08'):
                    dep = find_best_dep_in_topic(all_available, 'T08', 'G1', ['if', 'then'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Story consequences use if-then logic"))

        # === INTERFACE DESIGN DEPENDENCIES ===

        # Interfaces need events
        if topic == 'T16':
            if not has_cross_topic_dep(skill, 'T06'):
                dep = find_best_dep_in_topic(all_available, 'T06', 'G1', ['trigger', 'action'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Interface elements trigger actions (events)"))

        # === CREATIVE COMPUTING DEPENDENCIES ===

        # Art with patterns needs T04
        if topic == 'T20':
            if 'pattern' in text and not has_cross_topic_dep(skill, 'T04'):
                dep = find_best_dep_in_topic(all_available, 'T04', 'G1', ['pattern'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Creating patterns requires pattern recognition"))
            # Art with algorithms needs T01
            if 'instruction' in text or 'direction' in text:
                if not has_cross_topic_dep(skill, 'T01'):
                    dep = find_best_dep_in_topic(all_available, 'T01', 'G1', ['instruction', 'direction'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Following art instructions uses algorithmic thinking"))

        # === AI & DATA DEPENDENCIES ===

        # Data collection needs data representation
        if topic == 'T26':
            if not has_cross_topic_dep(skill, 'T25'):
                dep = find_best_dep_in_topic(all_available, 'T25', 'G1', ['tally', 'table', 'data'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Data collection requires understanding data representation"))

        # Data visualization needs data representation
        if topic == 'T27':
            if not has_cross_topic_dep(skill, 'T25'):
                dep = find_best_dep_in_topic(all_available, 'T25', 'G1', ['table', 'data'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Visualizing data requires understanding data representation"))

        # Text processing with categorization needs T10
        if topic == 'T29':
            if 'category' in text or 'sort' in text or 'group' in text:
                if not has_cross_topic_dep(skill, 'T10'):
                    dep = find_best_dep_in_topic(all_available, 'T10', 'G1', ['sort', 'organize'])
                    if dep:
                        recommendations.append((skill_id, dep,
                            "Text categorization requires data organization skills"))

        # === COMPUTING SYSTEMS DEPENDENCIES ===

        # Computing systems with sensors need T23
        if topic == 'T30':
            if 'sensor' in text and not has_cross_topic_dep(skill, 'T23'):
                dep = find_best_dep_in_topic(all_available, 'T23', 'G1', ['sensor'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Understanding sensors in systems requires sensor concepts"))

        # Sensors trigger events
        if topic == 'T23':
            if not has_cross_topic_dep(skill, 'T06'):
                dep = find_best_dep_in_topic(all_available, 'T06', 'GK', ['trigger', 'action', 'event'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Sensors detecting changes trigger actions (events)"))

        # === AI LITERACY DEPENDENCIES ===

        # AI chatbots asking questions relates to data collection
        if topic == 'T22':
            if 'question' in text and not has_cross_topic_dep(skill, 'T26'):
                dep = find_best_dep_in_topic(all_available, 'T26', 'GK', ['question', 'information'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "Asking questions relates to information gathering"))

        # AI following instructions needs algorithm understanding
        if topic == 'T24':
            if 'instruction' in text and not has_cross_topic_dep(skill, 'T01'):
                dep = find_best_dep_in_topic(all_available, 'T01', 'G1', ['instruction', 'direction'])
                if dep:
                    recommendations.append((skill_id, dep,
                        "AI instructions follow algorithmic patterns"))

    return recommendations

def main():
    skills = parse_skills('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    recommendations = comprehensive_analysis(skills)

    print("=" * 80)
    print("COMPREHENSIVE CROSS-TOPIC DEPENDENCIES FOR GRADE 1")
    print("=" * 80)
    print()

    # Remove duplicates
    unique_recs = {}
    for skill_id, dep_id, reason in recommendations:
        key = (skill_id, dep_id)
        if key not in unique_recs:
            unique_recs[key] = reason

    # Group by source skill
    by_source = defaultdict(list)
    for (skill_id, dep_id), reason in unique_recs.items():
        by_source[skill_id].append((dep_id, reason))

    for skill_id in sorted(by_source.keys()):
        skill = skills.get(skill_id)
        if skill:
            print(f"SKILL: {skill_id} - {skill['skill']}")
            print(f"TOPIC: {skill['topic']}")
            for dep_id, reason in by_source[skill_id]:
                dep_skill = skills.get(dep_id)
                if dep_skill:
                    print(f"  -> {dep_id}: {reason}")
                    print(f"     (Adds: {dep_skill['skill']})")
            print()

    print("=" * 80)
    print(f"Total: {len(unique_recs)} new cross-topic dependencies recommended")
    print("=" * 80)

    # Save to file
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade1_cross_topic_recommendations.txt', 'w') as f:
        for skill_id in sorted(by_source.keys()):
            skill = skills.get(skill_id)
            if skill:
                f.write(f"{skill_id} -> Dependencies:\n")
                for dep_id, reason in by_source[skill_id]:
                    f.write(f"  {dep_id}: {reason}\n")
                f.write("\n")

    print("\nRecommendations saved to grade1_cross_topic_recommendations.txt")

if __name__ == '__main__':
    main()
