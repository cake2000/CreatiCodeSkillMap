#!/usr/bin/env python3
"""
Grade 7 Skills Cross-Topic Dependency Analysis (Phase 2)
Analyzes all Grade 7 skills for cross-topic dependency issues
"""

import json
import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def parse_allskills_file(filepath: str) -> Dict[str, dict]:
    """Parse allskills.md and extract all skill information"""
    skills = {}
    current_skill = None

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries
    skill_blocks = re.split(r'\n(?=ID: T\d+\.)', content)

    for block in skill_blocks:
        if not block.strip():
            continue

        lines = block.strip().split('\n')
        skill_data = {
            'id': None,
            'topic': None,
            'skill': None,
            'description': None,
            'dependencies': []
        }

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if line.startswith('ID:'):
                skill_data['id'] = line.replace('ID:', '').strip()
            elif line.startswith('Topic:'):
                skill_data['topic'] = line.replace('Topic:', '').strip()
            elif line.startswith('Skill:'):
                skill_data['skill'] = line.replace('Skill:', '').strip()
            elif line.startswith('Description:'):
                skill_data['description'] = line.replace('Description:', '').strip()
            elif line.startswith('Dependencies:'):
                # Collect all dependency lines
                i += 1
                while i < len(lines) and lines[i].strip().startswith('*'):
                    dep_line = lines[i].strip()
                    match = re.match(r'\* (T\d+\.[A-Z0-9]+\.\d+(?:\.\d+)*)', dep_line)
                    if match:
                        skill_data['dependencies'].append(match.group(1))
                    i += 1
                i -= 1

            i += 1

        if skill_data['id']:
            skills[skill_data['id']] = skill_data

    return skills

def extract_grade_from_id(skill_id: str) -> str:
    """Extract grade from skill ID (e.g., T01.G7.01 -> G7)"""
    match = re.match(r'T\d+\.(GK|G[0-9]+)', skill_id)
    if match:
        return match.group(1)
    return None

def extract_topic_from_id(skill_id: str) -> str:
    """Extract topic from skill ID (e.g., T01.G7.01 -> T01)"""
    match = re.match(r'(T\d+)\.', skill_id)
    if match:
        return match.group(1)
    return None

def grade_to_number(grade: str) -> int:
    """Convert grade string to number (GK=0, G1=1, etc.)"""
    if grade == 'GK':
        return 0
    match = re.match(r'G(\d+)', grade)
    if match:
        return int(match.group(1))
    return -1

def is_cross_topic_dependency(skill_id: str, dep_id: str) -> bool:
    """Check if dependency is from a different topic"""
    skill_topic = extract_topic_from_id(skill_id)
    dep_topic = extract_topic_from_id(dep_id)
    return skill_topic != dep_topic

def check_x2_rule(skill_grade_num: int, dep_grade_num: int) -> bool:
    """Check if dependency follows X-2 rule (can depend on X-2 to X)"""
    return dep_grade_num >= skill_grade_num - 2 and dep_grade_num <= skill_grade_num

def get_topic_name(topic_code: str) -> str:
    """Map topic code to name"""
    topic_map = {
        'T01': 'Everyday Algorithms',
        'T02': 'Programs & Debugging',
        'T03': 'Sequencing',
        'T04': 'Loops',
        'T05': 'Events',
        'T06': 'Conditionals',
        'T07': 'Variables',
        'T08': 'Functions',
        'T09': 'Operators',
        'T10': 'Data Structures',
        'T11': 'Cloning',
        'T12': 'Custom Blocks',
        'T13': 'Animation',
        'T14': 'Game Design',
        'T15': 'Game Mechanics',
        'T16': 'UI Design',
        'T17': 'Drawing',
        'T18': 'Pen Effects',
        'T19': 'Sound',
        'T20': 'Music',
        'T21': 'Text',
        'T22': 'Multimedia',
        'T23': 'Interactions',
        'T24': 'Simulation',
        'T25': 'Math',
        'T26': 'Data Analysis',
        'T27': 'AI',
        'T28': 'Sensors',
        'T29': 'Robotics',
        'T30': 'Electronics',
        'T31': 'Networks',
        'T32': 'Cybersecurity',
        'T33': 'Web',
        'T34': 'Databases',
        'T35': 'Computer Systems',
        'T36': 'Ethics'
    }
    return topic_map.get(topic_code, topic_code)

def analyze_grade7_skills(skills: Dict[str, dict]) -> dict:
    """Analyze all Grade 7 skills for cross-topic dependency issues"""

    # Filter Grade 7 skills
    grade7_skills = {
        skill_id: skill_data
        for skill_id, skill_data in skills.items()
        if extract_grade_from_id(skill_id) == 'G7'
    }

    print(f"Found {len(grade7_skills)} Grade 7 skills")

    # Count skills by topic
    skills_by_topic = defaultdict(int)
    for skill_id in grade7_skills.keys():
        topic = extract_topic_from_id(skill_id)
        skills_by_topic[topic] += 1

    print(f"Skills across {len(skills_by_topic)} topics")

    # Analyze each skill for issues
    dependency_issues = []

    for skill_id, skill_data in grade7_skills.items():
        skill_grade_num = 7  # Grade 7
        skill_topic = extract_topic_from_id(skill_id)

        # Check each dependency
        current_deps = skill_data['dependencies']
        cross_topic_deps = []
        same_topic_deps = []

        for dep_id in current_deps:
            if is_cross_topic_dependency(skill_id, dep_id):
                cross_topic_deps.append(dep_id)
            else:
                same_topic_deps.append(dep_id)

            # Check X-2 rule
            dep_grade = extract_grade_from_id(dep_id)
            if dep_grade:
                dep_grade_num = grade_to_number(dep_grade)
                if not check_x2_rule(skill_grade_num, dep_grade_num):
                    dependency_issues.append({
                        'skill_id': skill_id,
                        'skill_name': skill_data['skill'],
                        'topic': get_topic_name(skill_topic),
                        'issue_type': 'x2_violation',
                        'current_dependencies': current_deps,
                        'violating_dependency': dep_id,
                        'violating_grade': dep_grade,
                        'recommended_action': 'remove',
                        'recommended_dependencies': [d for d in current_deps if d != dep_id],
                        'rationale': f"Grade 7 skill depends on {dep_grade} (grade {dep_grade_num}), which violates X-2 rule (must be >= grade 5)"
                    })

        # Analyze for missing cross-topic dependencies based on skill content
        skill_text = (skill_data.get('skill', '') + ' ' + skill_data.get('description', '')).lower()

        # Check for common patterns that need cross-topic dependencies
        missing_deps = analyze_missing_dependencies(
            skill_id, skill_text, skill_topic, current_deps, skills, grade7_skills
        )

        for missing_dep in missing_deps:
            dependency_issues.append(missing_dep)

    # Identify cross-topic patterns
    cross_topic_patterns = identify_cross_topic_patterns(grade7_skills, skills)

    # Build final report
    report = {
        'grade7_analysis': {
            'total_skills': len(grade7_skills),
            'skills_by_topic': {get_topic_name(t): c for t, c in sorted(skills_by_topic.items())},
            'dependency_issues': dependency_issues,
            'cross_topic_patterns': cross_topic_patterns,
            'summary': {
                'total_issues': len(dependency_issues),
                'x2_violations': len([i for i in dependency_issues if i['issue_type'] == 'x2_violation']),
                'missing_cross_topic': len([i for i in dependency_issues if i['issue_type'] == 'missing_cross_topic']),
                'transitive_redundant': len([i for i in dependency_issues if i['issue_type'] == 'transitive_redundant'])
            }
        }
    }

    return report

def analyze_missing_dependencies(
    skill_id: str,
    skill_text: str,
    skill_topic: str,
    current_deps: List[str],
    all_skills: Dict[str, dict],
    grade7_skills: Dict[str, dict]
) -> List[dict]:
    """Analyze if a skill is missing cross-topic dependencies - CONSERVATIVE approach"""
    issues = []
    current_dep_topics = {extract_topic_from_id(d) for d in current_deps}

    # Only flag truly essential dependencies based on topic
    # Be very conservative - only topics that CLEARLY need foundational concepts

    # Game Design (T14) and Game Mechanics (T15) MUST have programming fundamentals
    if skill_topic in ['T14', 'T15']:
        skill_desc = all_skills[skill_id].get('description', '').lower()

        # Need loops for any game with movement, enemies, or continuous action
        if 'T04' not in current_dep_topics:
            if any(word in skill_text for word in ['move', 'enemy', 'chase', 'follow', 'patrol', 'continuous', 'forever', 'game loop']):
                issues.append({
                    'skill_id': skill_id,
                    'skill_name': all_skills[skill_id]['skill'],
                    'topic': get_topic_name(skill_topic),
                    'issue_type': 'missing_cross_topic',
                    'current_dependencies': current_deps,
                    'recommended_action': 'add',
                    'recommended_dependencies': ['T04.G5.01'],  # Basic loop understanding
                    'rationale': f"Game with movement/enemies requires loop knowledge for game mechanics"
                })

        # Need variables for score, health, lives, timers
        if 'T07' not in current_dep_topics:
            if any(word in skill_text for word in ['score', 'health', 'lives', 'timer', 'points', 'counter', 'track']):
                issues.append({
                    'skill_id': skill_id,
                    'skill_name': all_skills[skill_id]['skill'],
                    'topic': get_topic_name(skill_topic),
                    'issue_type': 'missing_cross_topic',
                    'current_dependencies': current_deps,
                    'recommended_action': 'add',
                    'recommended_dependencies': ['T07.G5.01'],  # Basic variables
                    'rationale': f"Game state tracking (score/health/timer) requires variable knowledge"
                })

        # Need conditionals for collision detection, win/lose conditions
        if 'T06' not in current_dep_topics:
            if any(word in skill_text for word in ['collision', 'touching', 'detect', 'hit', 'win', 'lose', 'game over', 'if']):
                issues.append({
                    'skill_id': skill_id,
                    'skill_name': all_skills[skill_id]['skill'],
                    'topic': get_topic_name(skill_topic),
                    'issue_type': 'missing_cross_topic',
                    'current_dependencies': current_deps,
                    'recommended_action': 'add',
                    'recommended_dependencies': ['T06.G5.01'],  # Basic conditionals
                    'rationale': f"Game logic (collision/win-lose) requires conditional knowledge"
                })

    # Animation (T13) needs loops for continuous animation
    if skill_topic == 'T13':
        if 'T04' not in current_dep_topics:
            if any(word in skill_text for word in ['continuous', 'repeat', 'forever', 'loop', 'animate', 'smooth']):
                issues.append({
                    'skill_id': skill_id,
                    'skill_name': all_skills[skill_id]['skill'],
                    'topic': get_topic_name(skill_topic),
                    'issue_type': 'missing_cross_topic',
                    'current_dependencies': current_deps,
                    'recommended_action': 'add',
                    'recommended_dependencies': ['T04.G5.01'],
                    'rationale': f"Continuous animation requires loop knowledge"
                })

    # Data Analysis (T26) needs data structures
    if skill_topic == 'T26':
        if 'T10' not in current_dep_topics:
            if any(word in skill_text for word in ['dataset', 'list', 'data', 'collection', 'table']):
                issues.append({
                    'skill_id': skill_id,
                    'skill_name': all_skills[skill_id]['skill'],
                    'topic': get_topic_name(skill_topic),
                    'issue_type': 'missing_cross_topic',
                    'current_dependencies': current_deps,
                    'recommended_action': 'add',
                    'recommended_dependencies': ['T10.G5.01'],
                    'rationale': f"Data analysis requires data structure knowledge"
                })

    # Simulation (T24) needs programming fundamentals
    if skill_topic == 'T24':
        skill_desc = all_skills[skill_id].get('description', '').lower()

        # Complex simulations need variables
        if 'T07' not in current_dep_topics:
            if any(word in skill_text for word in ['variable', 'parameter', 'state', 'track', 'measure']):
                issues.append({
                    'skill_id': skill_id,
                    'skill_name': all_skills[skill_id]['skill'],
                    'topic': get_topic_name(skill_topic),
                    'issue_type': 'missing_cross_topic',
                    'current_dependencies': current_deps,
                    'recommended_action': 'add',
                    'recommended_dependencies': ['T07.G5.01'],
                    'rationale': f"Simulation state tracking requires variable knowledge"
                })

    return issues

def find_appropriate_dependencies(topic: str, grades: List[str], all_skills: Dict[str, dict]) -> List[str]:
    """Find appropriate dependency skills from a given topic and grades"""
    candidates = []

    for skill_id, skill_data in all_skills.items():
        skill_grade = extract_grade_from_id(skill_id)
        skill_topic = extract_topic_from_id(skill_id)

        if skill_topic == topic and skill_grade in grades:
            # Prefer foundational skills (lower IDs typically)
            candidates.append(skill_id)

    # Sort to prefer earlier/foundational skills
    candidates.sort()
    return candidates[:3]  # Return up to 3 candidates

def identify_cross_topic_patterns(grade7_skills: Dict[str, dict], all_skills: Dict[str, dict]) -> List[dict]:
    """Identify common cross-topic dependency patterns"""
    patterns = []

    # Pattern 1: Game skills (T14, T15) should depend on loops (T04), variables (T07), conditionals (T06)
    game_topics = ['T14', 'T15']
    game_skills = [sid for sid in grade7_skills.keys() if extract_topic_from_id(sid) in game_topics]
    game_missing_loops = []
    game_missing_vars = []
    game_missing_conds = []

    for skill_id in game_skills:
        deps = grade7_skills[skill_id]['dependencies']
        dep_topics = {extract_topic_from_id(d) for d in deps}

        if 'T04' not in dep_topics:
            game_missing_loops.append(skill_id)
        if 'T07' not in dep_topics:
            game_missing_vars.append(skill_id)
        if 'T06' not in dep_topics:
            game_missing_conds.append(skill_id)

    if game_missing_loops:
        patterns.append({
            'pattern': 'Game skills missing loop dependencies',
            'affected_skills': game_missing_loops,
            'recommendation': 'Add dependencies on T04 (Loops) G5/G6 skills for game mechanics'
        })

    if game_missing_vars:
        patterns.append({
            'pattern': 'Game skills missing variable dependencies',
            'affected_skills': game_missing_vars,
            'recommendation': 'Add dependencies on T07 (Variables) G5/G6 skills for score/state tracking'
        })

    if game_missing_conds:
        patterns.append({
            'pattern': 'Game skills missing conditional dependencies',
            'affected_skills': game_missing_conds,
            'recommendation': 'Add dependencies on T06 (Conditionals) G5/G6 skills for game logic'
        })

    # Pattern 2: Animation skills (T13) should depend on loops (T04) and events (T05)
    anim_skills = [sid for sid in grade7_skills.keys() if extract_topic_from_id(sid) == 'T13']
    anim_missing_loops = []

    for skill_id in anim_skills:
        deps = grade7_skills[skill_id]['dependencies']
        dep_topics = {extract_topic_from_id(d) for d in deps}

        if 'T04' not in dep_topics:
            anim_missing_loops.append(skill_id)

    if anim_missing_loops:
        patterns.append({
            'pattern': 'Animation skills missing loop dependencies',
            'affected_skills': anim_missing_loops,
            'recommendation': 'Add dependencies on T04 (Loops) for continuous animation'
        })

    # Pattern 3: Data analysis (T26) should depend on data structures (T10)
    data_skills = [sid for sid in grade7_skills.keys() if extract_topic_from_id(sid) == 'T26']
    data_missing_ds = []

    for skill_id in data_skills:
        deps = grade7_skills[skill_id]['dependencies']
        dep_topics = {extract_topic_from_id(d) for d in deps}

        if 'T10' not in dep_topics:
            data_missing_ds.append(skill_id)

    if data_missing_ds:
        patterns.append({
            'pattern': 'Data analysis skills missing data structure dependencies',
            'affected_skills': data_missing_ds,
            'recommendation': 'Add dependencies on T10 (Data Structures) for working with datasets'
        })

    return patterns

def main():
    print("=== Grade 7 Skills Analysis (Phase 2) ===\n")

    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    print(f"Reading skills from: {filepath}")

    skills = parse_allskills_file(filepath)
    print(f"Total skills parsed: {len(skills)}\n")

    report = analyze_grade7_skills(skills)

    # Print summary
    summary = report['grade7_analysis']['summary']
    print(f"\n=== Analysis Summary ===")
    print(f"Total Grade 7 skills: {report['grade7_analysis']['total_skills']}")
    print(f"Total issues found: {summary['total_issues']}")
    print(f"  - X-2 rule violations: {summary['x2_violations']}")
    print(f"  - Missing cross-topic dependencies: {summary['missing_cross_topic']}")
    print(f"  - Transitive redundant: {summary['transitive_redundant']}")
    print(f"\nCross-topic patterns identified: {len(report['grade7_analysis']['cross_topic_patterns'])}")

    # Save report
    output_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE7_ANALYSIS_REPORT.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    print(f"\nFull report saved to: {output_path}")

if __name__ == '__main__':
    main()
