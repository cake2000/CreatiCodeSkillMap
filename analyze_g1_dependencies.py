#!/usr/bin/env python3
"""
Analyze Grade 1 skills for cross-topic dependency issues.
Focus: X-2 rule validation and cross-topic dependency analysis.
"""

import re
from collections import defaultdict

def parse_skills(filepath):
    """Extract all skills with their dependencies."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill IDs
    skills = {}
    current_skill = None

    lines = content.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i]

        # Check for skill ID
        id_match = re.match(r'^ID: (T\d+\.G[K12].\d+)$', line)
        if id_match:
            skill_id = id_match.group(1)
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': []
            }
            skills[skill_id] = current_skill
            i += 1
            continue

        if current_skill:
            # Parse topic
            if line.startswith('Topic: '):
                current_skill['topic'] = line.replace('Topic: ', '').strip()
            # Parse skill name
            elif line.startswith('Skill: '):
                current_skill['skill'] = line.replace('Skill: ', '').strip()
            # Parse description
            elif line.startswith('Description: '):
                current_skill['description'] = line.replace('Description: ', '').strip()
            # Parse dependencies
            elif line.startswith('* '):
                dep_match = re.match(r'\* (T\d+\.G[K12].\d+):', line)
                if dep_match:
                    current_skill['dependencies'].append(dep_match.group(1))

        i += 1

    return skills

def extract_grade(skill_id):
    """Extract grade from skill ID (K, 1, or 2)."""
    match = re.search(r'\.G([K12])\.', skill_id)
    if match:
        return match.group(1)
    return None

def extract_topic(skill_id):
    """Extract topic number from skill ID."""
    match = re.match(r'T(\d+)\.', skill_id)
    if match:
        return int(match.group(1))
    return None

def check_x_minus_2_rule(skill_id, dependencies, skills):
    """
    Check if X-2 rule is satisfied:
    Grade 1 can only depend on K and 1.
    """
    issues = []
    skill_grade = extract_grade(skill_id)

    if skill_grade != '1':
        return issues

    for dep in dependencies:
        dep_grade = extract_grade(dep)
        if dep_grade == '2':
            issues.append({
                'type': 'X-2_VIOLATION',
                'skill': skill_id,
                'dependency': dep,
                'problem': f'Grade 1 skill depends on Grade 2 skill'
            })

    return issues

def find_cross_topic_issues(skills):
    """Analyze cross-topic dependencies and find missing connections."""
    issues = []

    # Get all Grade 1 skills by topic
    g1_by_topic = defaultdict(list)
    for skill_id, skill in skills.items():
        if extract_grade(skill_id) == '1':
            topic = extract_topic(skill_id)
            g1_by_topic[topic].append(skill)

    # Check each Grade 1 skill
    for skill_id, skill in skills.items():
        if extract_grade(skill_id) != '1':
            continue

        topic = extract_topic(skill_id)
        deps = skill['dependencies']

        # Check X-2 rule violations
        x2_issues = check_x_minus_2_rule(skill_id, deps, skills)
        issues.extend(x2_issues)

        # Check for potentially missing cross-topic dependencies
        skill_name = skill['skill'].lower()
        desc = skill['description'].lower()

        # Topic-specific checks based on content

        # T16+ (Advanced topics) should often depend on earlier foundational topics
        if topic >= 16:
            # Game-related skills (T16-T20) should check for:
            # - Events (T6)
            # - Loops (T7)
            # - Variables (T9)
            # - Graphics/Motion (implied from Scratch basics)

            if any(word in skill_name or word in desc for word in ['game', 'score', 'player', 'win', 'lose', 'play']):
                has_event_dep = any(extract_topic(d) == 6 for d in deps)
                has_var_dep = any(extract_topic(d) == 9 for d in deps)

                if 'score' in skill_name or 'score' in desc:
                    if not has_var_dep:
                        issues.append({
                            'type': 'MISSING_CROSS_TOPIC',
                            'skill': skill_id,
                            'problem': 'Game with score should depend on Variables (T9)',
                            'suggestion': 'Add T09.GK.02 or T09.G1.01'
                        })

                if 'click' in desc or 'event' in desc or 'when' in desc:
                    if not has_event_dep:
                        issues.append({
                            'type': 'MISSING_CROSS_TOPIC',
                            'skill': skill_id,
                            'problem': 'Interactive game should depend on Events (T6)',
                            'suggestion': 'Add T06.GK.03 or T06.G1.01'
                        })

            # Animation/motion skills should check for loops
            if any(word in skill_name or word in desc for word in ['repeat', 'animation', 'move', 'motion']):
                has_loop_dep = any(extract_topic(d) == 7 for d in deps)
                if 'repeat' in desc or 'multiple' in desc or 'several' in desc:
                    if not has_loop_dep:
                        issues.append({
                            'type': 'MISSING_CROSS_TOPIC',
                            'skill': skill_id,
                            'problem': 'Repeated actions should depend on Loops (T7)',
                            'suggestion': 'Add T07.K.01 or T07.G1.01'
                        })

        # Check for transitive dependencies (truly redundant ones)
        if len(deps) > 1:
            for i, dep1 in enumerate(deps):
                if dep1 not in skills:
                    continue
                for dep2 in deps[i+1:]:
                    if dep2 not in skills:
                        continue
                    # Check if dep2 depends on dep1 (making dep1 transitive)
                    if dep1 in skills[dep2]['dependencies']:
                        issues.append({
                            'type': 'TRANSITIVE_REDUNDANT',
                            'skill': skill_id,
                            'redundant_dep': dep1,
                            'problem': f'{dep1} is transitive through {dep2}',
                            'suggestion': f'Consider removing {dep1} if it is truly redundant'
                        })
                    # Check if dep1 depends on dep2 (making dep2 transitive)
                    elif dep2 in skills[dep1]['dependencies']:
                        issues.append({
                            'type': 'TRANSITIVE_REDUNDANT',
                            'skill': skill_id,
                            'redundant_dep': dep2,
                            'problem': f'{dep2} is transitive through {dep1}',
                            'suggestion': f'Consider removing {dep2} if it is truly redundant'
                        })

    return issues

def check_circular_dependencies(skills):
    """Check for circular dependency chains."""
    issues = []

    def find_cycle(skill_id, visited, path):
        if skill_id in path:
            cycle_start = path.index(skill_id)
            return path[cycle_start:] + [skill_id]

        if skill_id in visited:
            return None

        visited.add(skill_id)
        path.append(skill_id)

        if skill_id in skills:
            for dep in skills[skill_id]['dependencies']:
                cycle = find_cycle(dep, visited, path[:])
                if cycle:
                    return cycle

        return None

    checked = set()
    for skill_id in skills:
        if extract_grade(skill_id) == '1' and skill_id not in checked:
            visited = set()
            cycle = find_cycle(skill_id, visited, [])
            if cycle:
                issues.append({
                    'type': 'CIRCULAR_DEPENDENCY',
                    'cycle': ' -> '.join(cycle),
                    'problem': 'Circular dependency detected'
                })
                checked.update(cycle)

    return issues

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills...")
    skills = parse_skills(filepath)

    # Filter Grade 1 skills
    g1_skills = {k: v for k, v in skills.items() if extract_grade(k) == '1'}
    print(f"Found {len(g1_skills)} Grade 1 skills\n")

    # Find all issues
    print("Analyzing cross-topic dependencies...")
    issues = find_cross_topic_issues(skills)

    print("Checking for circular dependencies...")
    circular_issues = check_circular_dependencies(skills)
    issues.extend(circular_issues)

    # Group issues by type
    issues_by_type = defaultdict(list)
    for issue in issues:
        issues_by_type[issue['type']].append(issue)

    # Print summary
    print("\n" + "="*80)
    print("GRADE 1 DEPENDENCY ANALYSIS SUMMARY")
    print("="*80)
    print(f"\nTotal Grade 1 skills analyzed: {len(g1_skills)}")
    print(f"Total issues found: {len(issues)}\n")

    for issue_type, type_issues in sorted(issues_by_type.items()):
        print(f"\n{issue_type}: {len(type_issues)} issues")
        print("-" * 80)

        for issue in type_issues[:10]:  # Show first 10 of each type
            print(f"\nSkill: {issue.get('skill', 'N/A')}")
            print(f"Problem: {issue.get('problem', 'N/A')}")
            if 'dependency' in issue:
                print(f"Bad dependency: {issue['dependency']}")
            if 'redundant_dep' in issue:
                print(f"Redundant: {issue['redundant_dep']}")
            if 'suggestion' in issue:
                print(f"Suggestion: {issue['suggestion']}")
            if 'cycle' in issue:
                print(f"Cycle: {issue['cycle']}")

        if len(type_issues) > 10:
            print(f"\n... and {len(type_issues) - 10} more")

    # Save detailed report
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G1_DEPENDENCY_ANALYSIS.txt'
    with open(output_file, 'w') as f:
        f.write("COMPREHENSIVE GRADE 1 DEPENDENCY ANALYSIS\n")
        f.write("="*80 + "\n\n")
        f.write(f"Total Grade 1 skills: {len(g1_skills)}\n")
        f.write(f"Total issues found: {len(issues)}\n\n")

        for issue_type, type_issues in sorted(issues_by_type.items()):
            f.write(f"\n{issue_type}: {len(type_issues)} issues\n")
            f.write("-" * 80 + "\n")

            for issue in type_issues:
                f.write(f"\nSkill: {issue.get('skill', 'N/A')}\n")
                if issue.get('skill') and issue['skill'] in skills:
                    skill_info = skills[issue['skill']]
                    f.write(f"  Topic: {skill_info['topic']}\n")
                    f.write(f"  Name: {skill_info['skill']}\n")
                    f.write(f"  Current deps: {', '.join(skill_info['dependencies']) if skill_info['dependencies'] else 'None'}\n")

                f.write(f"Problem: {issue.get('problem', 'N/A')}\n")
                if 'dependency' in issue:
                    f.write(f"Bad dependency: {issue['dependency']}\n")
                if 'redundant_dep' in issue:
                    f.write(f"Redundant: {issue['redundant_dep']}\n")
                if 'suggestion' in issue:
                    f.write(f"Suggestion: {issue['suggestion']}\n")
                if 'cycle' in issue:
                    f.write(f"Cycle: {issue['cycle']}\n")
                f.write("\n")

    print(f"\n\nDetailed report saved to: {output_file}")

if __name__ == '__main__':
    main()
