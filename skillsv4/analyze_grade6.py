#!/usr/bin/env python3
"""
Comprehensive Grade 6 Skills Analysis
Analyzes all Grade 6 skills for:
- X-2 rule violations
- Missing cross-topic dependencies
- Circular dependencies
- Redundant transitive dependencies
- Cross-topic relationships
"""

import re
import json
from collections import defaultdict, deque
from typing import Dict, List, Set, Tuple

def parse_skill_id(skill_id: str) -> Tuple[str, str, str]:
    """Parse skill ID into topic, grade, and number"""
    match = re.match(r'(T\d{2})\.([^.]+)\.(.+)', skill_id)
    if match:
        return match.groups()
    return None, None, None

def extract_grade(skill_id: str) -> str:
    """Extract grade from skill ID"""
    _, grade, _ = parse_skill_id(skill_id)
    return grade

def extract_topic(skill_id: str) -> str:
    """Extract topic from skill ID"""
    topic, _, _ = parse_skill_id(skill_id)
    return topic

def parse_allskills_file(filepath: str) -> Dict:
    """Parse the allskills.md file and extract all Grade 6 skills"""

    skills = {}
    current_skill = None
    in_dependencies = False

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()

            # Check for skill ID
            if line.startswith('ID: '):
                skill_id = line[4:].strip()
                if '.G6.' in skill_id:
                    current_skill = skill_id
                    skills[skill_id] = {
                        'id': skill_id,
                        'topic': None,
                        'skill_name': None,
                        'description': None,
                        'dependencies': [],
                        'topic_code': extract_topic(skill_id),
                        'grade': 'G6'
                    }
                    in_dependencies = False
                else:
                    current_skill = None
                    in_dependencies = False

            elif current_skill:
                if line.startswith('Topic: '):
                    skills[current_skill]['topic'] = line[7:].strip()

                elif line.startswith('Skill: '):
                    skills[current_skill]['skill_name'] = line[7:].strip()

                elif line.startswith('Description: '):
                    skills[current_skill]['description'] = line[13:].strip()

                elif line.startswith('Dependencies:'):
                    in_dependencies = True

                elif in_dependencies:
                    if line.startswith('* '):
                        # Extract dependency ID
                        dep_match = re.search(r'(T\d{2}\.[^:]+)', line)
                        if dep_match:
                            dep_id = dep_match.group(1).strip()
                            skills[current_skill]['dependencies'].append(dep_id)
                    elif line == '' or line.startswith('ID: '):
                        in_dependencies = False

    return skills

def analyze_x_minus_2_violations(skills: Dict) -> List[Dict]:
    """Find dependencies that violate X-2 rule for Grade 6 (only G4, G5, G6 allowed)"""
    violations = []
    allowed_grades = {'GK', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6'}

    for skill_id, skill_data in skills.items():
        for dep_id in skill_data['dependencies']:
            dep_grade = extract_grade(dep_id)
            if dep_grade and dep_grade not in allowed_grades:
                violations.append({
                    'skill_id': skill_id,
                    'skill_name': skill_data['skill_name'],
                    'dependency_id': dep_id,
                    'dependency_grade': dep_grade,
                    'issue': f'Grade 6 skill depends on {dep_grade} (violates X-2 rule)'
                })

    return violations

def build_dependency_graph(skills: Dict) -> Dict[str, Set[str]]:
    """Build a dependency graph for all skills"""
    graph = defaultdict(set)
    for skill_id, skill_data in skills.items():
        for dep_id in skill_data['dependencies']:
            graph[skill_id].add(dep_id)
    return graph

def find_circular_dependencies(graph: Dict[str, Set[str]], grade6_skills: Set[str]) -> List[Dict]:
    """Find circular dependencies involving Grade 6 skills"""
    circles = []

    def dfs_find_cycle(node, path, visited_in_path):
        if node in visited_in_path:
            # Found a cycle
            cycle_start = path.index(node)
            cycle = path[cycle_start:]
            # Only report if it involves a Grade 6 skill
            if any(skill in grade6_skills for skill in cycle):
                return [cycle]
            return []

        if node not in graph:
            return []

        visited_in_path.add(node)
        path.append(node)

        cycles = []
        for neighbor in graph[node]:
            cycles.extend(dfs_find_cycle(neighbor, path[:], visited_in_path.copy()))

        return cycles

    found_cycles = set()
    for skill in grade6_skills:
        cycles = dfs_find_cycle(skill, [], set())
        for cycle in cycles:
            cycle_key = tuple(sorted(cycle))
            if cycle_key not in found_cycles:
                found_cycles.add(cycle_key)
                circles.append({
                    'cycle': cycle,
                    'description': ' -> '.join(cycle) + ' -> ' + cycle[0]
                })

    return circles

def find_redundant_transitive_deps(skills: Dict) -> List[Dict]:
    """Find truly redundant transitive dependencies"""
    redundant = []

    for skill_id, skill_data in skills.items():
        direct_deps = set(skill_data['dependencies'])

        # For each direct dependency, find all its transitive dependencies
        for dep in direct_deps:
            # Get all dependencies reachable from this direct dep
            reachable = set()
            queue = deque([dep])
            visited = {dep}

            while queue:
                current = queue.popleft()
                # Find current in all skills (may be from different grade)
                for s_id, s_data in skills.items():
                    if s_id == current:
                        for next_dep in s_data['dependencies']:
                            if next_dep not in visited:
                                visited.add(next_dep)
                                reachable.add(next_dep)
                                queue.append(next_dep)
                        break

            # Check if any other direct dep is in reachable set
            for other_dep in direct_deps:
                if other_dep != dep and other_dep in reachable:
                    redundant.append({
                        'skill_id': skill_id,
                        'skill_name': skill_data['skill_name'],
                        'redundant_dep': other_dep,
                        'reachable_via': dep,
                        'explanation': f'{skill_id} directly depends on {other_dep}, but {other_dep} is already reachable via {dep}'
                    })

    return redundant

# Topic descriptions for cross-topic analysis
TOPIC_CATEGORIES = {
    'T01': 'Algorithms',
    'T02': 'Flowcharts',
    'T03': 'Debugging',
    'T04': 'Code Organization',
    'T05': 'Variables',
    'T06': 'Operators',
    'T07': 'Conditionals',
    'T08': 'Lists',
    'T09': 'Loops',
    'T10': 'Events',
    'T11': 'Motion',
    'T12': 'Looks',
    'T13': 'Pen',
    'T14': 'Sound',
    'T15': 'Sensing',
    'T16': 'Control Flow',
    'T17': 'Functions',
    'T18': 'UI',
    'T19': 'Multiplayer',
    'T20': 'Graphics',
    'T21': 'Animation',
    'T22': 'Game',
    'T23': 'Physics',
    'T24': 'Data',
    'T25': 'AI',
    'T26': 'Image',
    'T27': 'Sound/Music',
    'T28': 'Math',
    'T29': '3D',
    'T30': 'AR',
    'T31': 'Devices',
    'T32': 'Security',
    'T33': 'Social',
    'T34': 'Environment',
    'T35': 'ML',
    'T36': 'Data Science',
}

# Expected cross-topic dependencies for different skill types
EXPECTED_CROSS_TOPIC_DEPS = {
    'T22': ['T05', 'T07', 'T09', 'T11', 'T10', 'T15', 'T06'],  # Game needs variables, conditionals, loops, motion, events, sensing, operators
    'T21': ['T11', 'T12', 'T09', 'T05', 'T10'],  # Animation needs motion, looks, loops, variables, events
    'T24': ['T05', 'T08', 'T06', 'T18'],  # Data needs variables, lists, operators, UI
    'T23': ['T11', 'T06', 'T15', 'T05', 'T09'],  # Physics needs motion, operators, sensing, variables, loops
    'T25': ['T24', 'T05', 'T08', 'T18', 'T06'],  # AI needs data, variables, lists, UI, operators
    'T19': ['T05', 'T10', 'T18', 'T08'],  # Multiplayer needs variables, events, UI, lists
    'T20': ['T13', 'T11', 'T12', 'T06'],  # Graphics needs pen, motion, looks, operators
    'T29': ['T11', 'T15', 'T06', 'T05'],  # 3D needs motion, sensing, operators, variables
    'T30': ['T15', 'T26', 'T11', 'T05'],  # AR needs sensing, image, motion, variables
    'T35': ['T24', 'T25', 'T08', 'T05', 'T06'],  # ML needs data, AI, lists, variables, operators
    'T36': ['T24', 'T08', 'T05', 'T06', 'T18'],  # Data Science needs data, lists, variables, operators, UI
}

def analyze_cross_topic_dependencies(skills: Dict) -> Dict:
    """Analyze cross-topic dependencies"""

    cross_topic_analysis = {
        'existing_cross_topic_deps': [],
        'missing_cross_topic_deps': [],
        'cross_topic_summary': defaultdict(lambda: {'has': set(), 'missing': set()})
    }

    for skill_id, skill_data in skills.items():
        skill_topic = skill_data['topic_code']

        # Analyze existing cross-topic dependencies
        cross_topic_deps = []
        for dep_id in skill_data['dependencies']:
            dep_topic = extract_topic(dep_id)
            if dep_topic and dep_topic != skill_topic:
                cross_topic_deps.append({
                    'from_topic': skill_topic,
                    'to_topic': dep_topic,
                    'dep_id': dep_id
                })
                cross_topic_analysis['cross_topic_summary'][skill_topic]['has'].add(dep_topic)

        if cross_topic_deps:
            cross_topic_analysis['existing_cross_topic_deps'].append({
                'skill_id': skill_id,
                'skill_name': skill_data['skill_name'],
                'topic': skill_topic,
                'cross_topic_deps': cross_topic_deps
            })

        # Check for missing expected dependencies
        if skill_topic in EXPECTED_CROSS_TOPIC_DEPS:
            expected_topics = EXPECTED_CROSS_TOPIC_DEPS[skill_topic]
            current_dep_topics = set(extract_topic(dep) for dep in skill_data['dependencies'])

            missing_topics = []
            for expected_topic in expected_topics:
                if expected_topic not in current_dep_topics:
                    missing_topics.append(expected_topic)
                    cross_topic_analysis['cross_topic_summary'][skill_topic]['missing'].add(expected_topic)

            if missing_topics:
                cross_topic_analysis['missing_cross_topic_deps'].append({
                    'skill_id': skill_id,
                    'skill_name': skill_data['skill_name'],
                    'topic': skill_topic,
                    'missing_from_topics': missing_topics,
                    'suggestion': f'Consider adding dependencies from: {", ".join(TOPIC_CATEGORIES[t] for t in missing_topics if t in TOPIC_CATEGORIES)}'
                })

    # Convert sets to lists for JSON serialization
    for topic in cross_topic_analysis['cross_topic_summary']:
        cross_topic_analysis['cross_topic_summary'][topic]['has'] = list(cross_topic_analysis['cross_topic_summary'][topic]['has'])
        cross_topic_analysis['cross_topic_summary'][topic]['missing'] = list(cross_topic_analysis['cross_topic_summary'][topic]['missing'])

    return cross_topic_analysis

def main():
    print("Loading and parsing allskills.md...")
    skills = parse_allskills_file('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')

    print(f"Found {len(skills)} Grade 6 skills")

    # Organize by topic
    skills_by_topic = defaultdict(list)
    for skill_id, skill_data in skills.items():
        skills_by_topic[skill_data['topic_code']].append(skill_id)

    print("\n=== ANALYZING X-2 RULE VIOLATIONS ===")
    violations = analyze_x_minus_2_violations(skills)
    print(f"Found {len(violations)} X-2 rule violations")

    print("\n=== BUILDING DEPENDENCY GRAPH ===")
    graph = build_dependency_graph(skills)

    print("\n=== FINDING CIRCULAR DEPENDENCIES ===")
    grade6_skill_ids = set(skills.keys())
    circles = find_circular_dependencies(graph, grade6_skill_ids)
    print(f"Found {len(circles)} circular dependency chains")

    print("\n=== FINDING REDUNDANT TRANSITIVE DEPENDENCIES ===")
    redundant = find_redundant_transitive_deps(skills)
    print(f"Found {len(redundant)} potentially redundant dependencies")

    print("\n=== ANALYZING CROSS-TOPIC DEPENDENCIES ===")
    cross_topic = analyze_cross_topic_dependencies(skills)
    print(f"Found {len(cross_topic['existing_cross_topic_deps'])} skills with cross-topic deps")
    print(f"Found {len(cross_topic['missing_cross_topic_deps'])} skills with potentially missing cross-topic deps")

    # Build comprehensive report
    report = {
        'summary': {
            'total_grade6_skills': len(skills),
            'topics_with_grade6': len(skills_by_topic),
            'x_minus_2_violations': len(violations),
            'circular_dependencies': len(circles),
            'redundant_dependencies': len(redundant),
            'skills_with_cross_topic_deps': len(cross_topic['existing_cross_topic_deps']),
            'skills_missing_cross_topic_deps': len(cross_topic['missing_cross_topic_deps'])
        },
        'skills_by_topic': {topic: sorted(skill_list) for topic, skill_list in skills_by_topic.items()},
        'all_skills': {k: {**v, 'dependencies': list(v['dependencies'])} for k, v in skills.items()},
        'violations': {
            'x_minus_2_rule': violations,
            'circular_dependencies': circles,
            'redundant_transitive_deps': redundant[:50]  # Limit to top 50
        },
        'cross_topic_analysis': {
            'existing_cross_topic_deps': cross_topic['existing_cross_topic_deps'][:100],
            'missing_cross_topic_deps': cross_topic['missing_cross_topic_deps'],
            'summary_by_topic': dict(cross_topic['cross_topic_summary'])
        },
        'recommendations': []
    }

    # Add recommendations
    if violations:
        report['recommendations'].append({
            'category': 'X-2 Rule Violations',
            'severity': 'HIGH',
            'count': len(violations),
            'action': 'Review and fix dependencies that violate the X-2 rule (Grade 6 should only depend on G4, G5, G6)'
        })

    if circles:
        report['recommendations'].append({
            'category': 'Circular Dependencies',
            'severity': 'HIGH',
            'count': len(circles),
            'action': 'Break circular dependency chains to ensure proper skill progression'
        })

    if cross_topic['missing_cross_topic_deps']:
        report['recommendations'].append({
            'category': 'Missing Cross-Topic Dependencies',
            'severity': 'MEDIUM',
            'count': len(cross_topic['missing_cross_topic_deps']),
            'action': 'Review skills that may need dependencies from foundational topics (variables, loops, conditionals, etc.)'
        })

    if redundant:
        report['recommendations'].append({
            'category': 'Redundant Dependencies',
            'severity': 'LOW',
            'count': len(redundant),
            'action': 'Consider removing redundant transitive dependencies to simplify the skill graph'
        })

    # Save report
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE6_ANALYSIS_REPORT.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"\n=== REPORT SAVED TO {output_file} ===")
    print("\nSUMMARY:")
    print(f"  Total Grade 6 Skills: {report['summary']['total_grade6_skills']}")
    print(f"  Topics with Grade 6: {report['summary']['topics_with_grade6']}")
    print(f"  X-2 Violations: {report['summary']['x_minus_2_violations']}")
    print(f"  Circular Dependencies: {report['summary']['circular_dependencies']}")
    print(f"  Redundant Dependencies: {report['summary']['redundant_dependencies']}")
    print(f"  Cross-Topic Dependencies: {report['summary']['skills_with_cross_topic_deps']}")
    print(f"  Missing Cross-Topic Deps: {report['summary']['skills_missing_cross_topic_deps']}")

    return report

if __name__ == '__main__':
    main()
