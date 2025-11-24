#!/usr/bin/env python3
"""
Analyze Grade 1 skills to identify missing cross-topic dependencies.
Focus on conceptual relationships and skill reuse across different topics.
"""

import re
from collections import defaultdict

def parse_skills(filename):
    """Parse the allskills.md file and extract Grade 1 skills with their dependencies."""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    current_skill = None
    current_deps = []

    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Check for skill ID
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
                # Read all dependencies
                j = i + 1
                while j < len(lines) and lines[j].startswith('* '):
                    dep_line = lines[j].strip()[2:]  # Remove '* '
                    if ':' in dep_line:
                        dep_id = dep_line.split(':')[0].strip()
                        current_deps.append(dep_id)
                    j += 1
                current_skill['dependencies'] = current_deps
                i = j - 1

        i += 1

    # Add last skill
    if current_skill:
        skills[current_skill['id']] = current_skill

    return skills

def get_topic_from_id(skill_id):
    """Extract topic code from skill ID (e.g., T01 from T01.G1.01)"""
    match = re.match(r'(T\d+)\.', skill_id)
    return match.group(1) if match else None

def get_grade_from_id(skill_id):
    """Extract grade from skill ID (e.g., G1 from T01.G1.01)"""
    match = re.match(r'T\d+\.(GK|G[0-9]+)\.', skill_id)
    return match.group(1) if match else None

def analyze_cross_topic_dependencies(skills):
    """Identify missing cross-topic dependencies for Grade 1 skills."""

    # Filter for Grade 1 skills only
    g1_skills = {k: v for k, v in skills.items() if get_grade_from_id(k) == 'G1'}

    # Organize by topic
    by_topic = defaultdict(list)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)
        if topic:
            by_topic[topic].append((skill_id, skill))

    print(f"Found {len(g1_skills)} Grade 1 skills across {len(by_topic)} topics")
    print()

    recommendations = []

    # Rule 1: Debugging skills should depend on algorithm design skills
    # T13 (Debugging) should depend on T02 (Algorithm Design) and T01 (Everyday Algorithms)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T13':  # Debugging
            # Should have dependencies on algorithm understanding
            has_algo_dep = any(get_topic_from_id(d) in ['T01', 'T02'] for d in skill['dependencies'])
            if not has_algo_dep:
                # Find appropriate algorithm skill
                if 'error' in skill['skill'].lower() or 'mistake' in skill['skill'].lower():
                    recommendations.append((skill_id, 'T01.G1.06',
                        "Debugging requires understanding algorithm steps (fixing wrong steps)"))
                if 'trace' in skill['skill'].lower() or 'step' in skill['description'].lower():
                    recommendations.append((skill_id, 'T02.G1.02',
                        "Tracing for debugging requires basic algorithm tracing skills"))

    # Rule 2: Loop-related skills should depend on pattern recognition
    # T07 (Loops) should depend on T04 (Pattern Recognition)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T07':  # Loops
            has_pattern_dep = any(get_topic_from_id(d) == 'T04' for d in skill['dependencies'])
            if not has_pattern_dep:
                recommendations.append((skill_id, 'T04.G1.01',
                    "Understanding loops requires recognizing repeating patterns"))

    # Rule 3: Game Design with rules should depend on conditionals
    # T14 (Game Design) with "rules" should depend on T08 (Conditionals)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T14':  # Game Design
            if 'rule' in skill['skill'].lower() or 'rule' in skill['description'].lower():
                has_cond_dep = any(get_topic_from_id(d) == 'T08' for d in skill['dependencies'])
                if not has_cond_dep:
                    recommendations.append((skill_id, 'T08.G1.01',
                        "Game rules often use if-then logic (conditionals)"))

    # Rule 4: Data visualization should depend on data structures
    # T27 (Data Visualization) should depend on T10 (Data Structures) or T25 (Data Representation)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T27':  # Data Visualization
            has_data_dep = any(get_topic_from_id(d) in ['T10', 'T25'] for d in skill['dependencies'])
            if not has_data_dep:
                if 'pictograph' in skill['description'].lower() or 'table' in skill['description'].lower():
                    recommendations.append((skill_id, 'T25.G1.02',
                        "Visualizing data requires understanding data representation (tables)"))

    # Rule 5: Data collection should use data structures
    # T26 (Data Collection) should depend on T10 or T25
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T26':  # Data Collection
            has_data_dep = any(get_topic_from_id(d) in ['T10', 'T25'] for d in skill['dependencies'])
            if not has_data_dep:
                if 'tally' in skill['description'].lower():
                    recommendations.append((skill_id, 'T25.G1.01',
                        "Collecting with tallies requires understanding tally marks"))
                elif 'checklist' in skill['description'].lower() or 'log' in skill['description'].lower():
                    recommendations.append((skill_id, 'T10.G1.01',
                        "Using checklists/logs requires understanding organized data"))

    # Rule 6: Creative computing with patterns should depend on pattern recognition
    # T20 (Creative Computing) should depend on T04 (Pattern Recognition)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T20':  # Creative Computing
            if 'pattern' in skill['skill'].lower() or 'pattern' in skill['description'].lower():
                has_pattern_dep = any(get_topic_from_id(d) == 'T04' for d in skill['dependencies'])
                if not has_pattern_dep:
                    recommendations.append((skill_id, 'T04.G1.03',
                        "Creating art patterns requires pattern recognition skills"))

    # Rule 7: Storytelling with sequences should depend on algorithms
    # T15 (Storytelling) should depend on T01 (Everyday Algorithms)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T15':  # Storytelling
            if 'sequence' in skill['description'].lower() or 'order' in skill['description'].lower():
                has_algo_dep = any(get_topic_from_id(d) == 'T01' for d in skill['dependencies'])
                if not has_algo_dep:
                    recommendations.append((skill_id, 'T01.G1.04',
                        "Story sequencing uses same skills as predicting algorithm steps"))

    # Rule 8: Variables used for counting should relate to loops
    # T09 (Variables) with counting should depend on T07 (Loops) or pattern recognition
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T09':  # Variables
            if 'count' in skill['skill'].lower():
                has_loop_dep = any(get_topic_from_id(d) in ['T07', 'T01'] for d in skill['dependencies'])
                if not has_loop_dep:
                    recommendations.append((skill_id, 'T01.GK.08',
                        "Counting actions relates to recognizing repetitions"))

    # Rule 9: Text processing with sorting should depend on data structures
    # T29 (Text Processing) with sorting should depend on T10 (Data Structures)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T29':  # Text Processing
            if 'sort' in skill['skill'].lower() or 'categor' in skill['skill'].lower():
                has_data_dep = any(get_topic_from_id(d) == 'T10' for d in skill['dependencies'])
                if not has_data_dep:
                    recommendations.append((skill_id, 'T10.G1.01',
                        "Sorting/categorizing requires understanding data organization"))

    # Rule 10: Conditionals for sorting should depend on algorithms
    # T08 (Conditionals) with sorting should depend on T01 or T02
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T08':  # Conditionals
            if 'sort' in skill['skill'].lower():
                has_algo_dep = any(get_topic_from_id(d) == 'T01' for d in skill['dependencies'])
                if not has_algo_dep:
                    recommendations.append((skill_id, 'T01.G1.10',
                        "Sorting with if-then rules builds on matching if/then concepts"))

    # Rule 11: Algorithm design should depend on decomposition
    # T02 (Algorithm Design) should depend on T03 (Decomposition)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T02':  # Algorithm Design
            if 'make' in skill['skill'].lower() or 'create' in skill['skill'].lower():
                has_decomp_dep = any(get_topic_from_id(d) == 'T03' for d in skill['dependencies'])
                if not has_decomp_dep:
                    recommendations.append((skill_id, 'T03.G1.01',
                        "Creating algorithms requires breaking tasks into parts"))

    # Rule 12: Abstraction with grouping should depend on pattern recognition
    # T12 (Abstraction) should depend on T04 (Pattern Recognition)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T12':  # Abstraction
            if 'group' in skill['skill'].lower() or 'similar' in skill['description'].lower():
                has_pattern_dep = any(get_topic_from_id(d) == 'T04' for d in skill['dependencies'])
                if not has_pattern_dep:
                    recommendations.append((skill_id, 'T04.G1.02',
                        "Grouping similar things requires recognizing patterns/similarities"))

    # Rule 13: Design thinking should use decomposition
    # T05 (Design Thinking) should depend on T03 (Decomposition)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T05':  # Design Thinking
            if 'solution' in skill['description'].lower() or 'design' in skill['skill'].lower():
                has_decomp_dep = any(get_topic_from_id(d) == 'T03' for d in skill['dependencies'])
                if not has_decomp_dep:
                    recommendations.append((skill_id, 'T03.G1.02',
                        "Designing solutions requires breaking problems into steps"))

    # Rule 14: Events triggering actions should relate to conditionals
    # T06 (Events) should relate to T08 (Conditionals)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T06':  # Events
            if 'trigger' in skill['description'].lower() or 'cause' in skill['description'].lower():
                has_cond_dep = any(get_topic_from_id(d) == 'T08' for d in skill['dependencies'])
                if not has_cond_dep:
                    recommendations.append((skill_id, 'T01.G1.10',
                        "Events causing actions is similar to if-then rules"))

    # Rule 15: AI chatbots asking questions relates to data collection
    # T22 (AI Chatbots) should relate to T26 (Data Collection) for question asking
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T22':  # AI Chatbots
            if 'question' in skill['skill'].lower():
                has_data_dep = any(get_topic_from_id(d) == 'T26' for d in skill['dependencies'])
                if not has_data_dep:
                    recommendations.append((skill_id, 'T26.GK.01',
                        "Asking good questions relates to collecting information"))

    # Rule 16: Sensors detecting changes relates to events
    # T23 (Sensors) should relate to T06 (Events)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T23':  # Sensors
            if 'detect' in skill['description'].lower() or 'sense' in skill['description'].lower():
                has_event_dep = any(get_topic_from_id(d) == 'T06' for d in skill['dependencies'])
                if not has_event_dep:
                    recommendations.append((skill_id, 'T06.GK.01',
                        "Sensors detecting triggers relate to events causing actions"))

    # Rule 17: Interface design with buttons relates to events
    # T16 (Interface Design) should relate to T06 (Events)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T16':  # Interface Design
            if 'button' in skill['description'].lower() or 'click' in skill['description'].lower():
                has_event_dep = any(get_topic_from_id(d) == 'T06' for d in skill['dependencies'])
                if not has_event_dep:
                    recommendations.append((skill_id, 'T06.G1.01',
                        "Interface buttons are events that trigger actions"))

    # Rule 18: Computing systems with sensors relates to sensor topic
    # T30 (Computing Systems) should relate to T23 (Sensors)
    for skill_id, skill in g1_skills.items():
        topic = get_topic_from_id(skill_id)

        if topic == 'T30':  # Computing Systems
            if 'sensor' in skill['description'].lower():
                has_sensor_dep = any(get_topic_from_id(d) == 'T23' for d in skill['dependencies'])
                if not has_sensor_dep:
                    recommendations.append((skill_id, 'T23.G1.01',
                        "Understanding computing system sensors requires sensor concepts"))

    return recommendations

def main():
    skills = parse_skills('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    recommendations = analyze_cross_topic_dependencies(skills)

    print("=" * 80)
    print("RECOMMENDED NEW CROSS-TOPIC DEPENDENCIES FOR GRADE 1")
    print("=" * 80)
    print()

    # Group by source skill
    by_source = defaultdict(list)
    for skill_id, dep_id, reason in recommendations:
        by_source[skill_id].append((dep_id, reason))

    for skill_id in sorted(by_source.keys()):
        skill = skills.get(skill_id)
        if skill:
            print(f"SKILL: {skill_id} - {skill['skill']}")
            for dep_id, reason in by_source[skill_id]:
                dep_skill = skills.get(dep_id)
                if dep_skill:
                    print(f"  -> {dep_id}: {reason}")
                    print(f"     (Dependency: {dep_skill['skill']})")
                else:
                    print(f"  -> {dep_id}: {reason}")
            print()

    print("=" * 80)
    print(f"Total: {len(recommendations)} new cross-topic dependencies recommended")
    print("=" * 80)

if __name__ == '__main__':
    main()
