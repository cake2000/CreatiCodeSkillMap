#!/usr/bin/env python3
"""
Comprehensive Grade 1 cross-topic dependency analysis.
Examines specific patterns and relationships across all 36 topics.
"""

import re
from collections import defaultdict
import json

def parse_skills(filepath):
    """Extract all skills with their full information."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    current_skill = None
    in_dependencies = False

    lines = content.split('\n')
    for line in lines:
        # Check for skill ID
        id_match = re.match(r'^ID: (T\d+\.G[K12].\d+)$', line)
        if id_match:
            if current_skill:
                skills[current_skill['id']] = current_skill
            skill_id = id_match.group(1)
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': []
            }
            in_dependencies = False
            continue

        if current_skill:
            if line.startswith('Topic: '):
                current_skill['topic'] = line.replace('Topic: ', '').strip()
                in_dependencies = False
            elif line.startswith('Skill: '):
                current_skill['skill'] = line.replace('Skill: ', '').strip()
                in_dependencies = False
            elif line.startswith('Description: '):
                current_skill['description'] = line.replace('Description: ', '').strip()
                in_dependencies = False
            elif line.strip() == 'Dependencies:':
                in_dependencies = True
            elif in_dependencies and line.startswith('* '):
                dep_match = re.match(r'\* (T\d+\.G[K12].\d+):', line)
                if dep_match:
                    current_skill['dependencies'].append(dep_match.group(1))

    if current_skill:
        skills[current_skill['id']] = current_skill

    return skills

def extract_grade(skill_id):
    """Extract grade from skill ID."""
    match = re.search(r'\.G([K12])\.', skill_id)
    return match.group(1) if match else None

def extract_topic(skill_id):
    """Extract topic number from skill ID."""
    match = re.match(r'T(\d+)\.', skill_id)
    return int(match.group(1)) if match else None

def analyze_skill_content(skill):
    """Analyze skill content for keywords indicating cross-topic needs."""
    text = (skill['skill'] + ' ' + skill['description']).lower()

    indicators = {
        'events': ['click', 'when', 'event', 'trigger', 'start', 'flag', 'key press', 'space key'],
        'loops': ['repeat', 'loop', 'again', 'multiple times', 'several times', 'many times', 'over and over'],
        'conditionals': ['if', 'condition', 'check', 'when', 'choose', 'decide'],
        'variables': ['score', 'counter', 'count', 'track', 'remember', 'store', 'number', 'variable'],
        'motion': ['move', 'motion', 'position', 'location', 'go to', 'glide', 'direction'],
        'looks': ['costume', 'appearance', 'show', 'hide', 'size', 'effect', 'look'],
        'pen': ['draw', 'line', 'pen', 'trail', 'stamp'],
        'sound': ['sound', 'music', 'play', 'note', 'volume', 'audio'],
        'sensing': ['touch', 'distance', 'detect', 'sense', 'ask', 'answer'],
        'operators': ['add', 'subtract', 'calculate', 'math', 'compare', 'greater', 'less'],
        'lists': ['list', 'collection', 'items', 'group', 'sort'],
        'clone': ['clone', 'copy', 'duplicate', 'create'],
        'broadcast': ['message', 'broadcast', 'send', 'receive', 'communicate'],
    }

    found = defaultdict(list)
    for category, keywords in indicators.items():
        for keyword in keywords:
            if keyword in text:
                found[category].append(keyword)

    return found

def get_topic_mapping():
    """Map topic numbers to their primary focus."""
    return {
        1: 'algorithms',
        2: 'algorithm_diagrams',
        3: 'decomposition',
        4: 'patterns',
        5: 'design',
        6: 'events',
        7: 'loops',
        8: 'conditionals',
        9: 'variables',
        10: 'lists',
        11: 'operators',
        12: 'organizing',
        13: 'debugging',
        14: 'motion',
        15: 'looks',
        16: 'game_intro',
        17: 'interactive_stories',
        18: 'art_creative',
        19: 'music',
        20: 'art_algorithmic',
        21: 'pen',
        22: 'sensing',
        23: 'clones',
        24: 'ai',
        25: 'text',
        26: 'math',
        27: 'simulation',
        28: 'data',
        29: 'advanced_games',
        30: 'extension_intro',
        31: 'ml',
        32: 'mobile',
        33: 'multiplayer',
        34: 'custom_blocks',
        35: 'advanced',
        36: 'portfolio'
    }

def check_required_dependencies(skill, skills):
    """Check if skill has required cross-topic dependencies."""
    issues = []
    skill_id = skill['id']
    topic = extract_topic(skill_id)
    deps = skill['dependencies']
    dep_topics = set(extract_topic(d) for d in deps if d in skills)

    content_indicators = analyze_skill_content(skill)

    # Rule 1: Events indicators should have T6 dependency
    if content_indicators['events'] and topic != 6:
        has_event_dep = 6 in dep_topics
        if not has_event_dep:
            issues.append({
                'type': 'MISSING_EVENTS',
                'skill': skill_id,
                'indicators': content_indicators['events'],
                'current_deps': deps,
                'suggestion': 'Add T06.GK.03 or T06.G1.01 (Events)'
            })

    # Rule 2: Loop indicators should have T7 dependency
    if content_indicators['loops'] and topic != 7:
        has_loop_dep = 7 in dep_topics
        if not has_loop_dep:
            issues.append({
                'type': 'MISSING_LOOPS',
                'skill': skill_id,
                'indicators': content_indicators['loops'],
                'current_deps': deps,
                'suggestion': 'Add T07.K.01 or T07.G1.01 (Loops)'
            })

    # Rule 3: Variable/score/counter indicators should have T9 dependency
    if content_indicators['variables'] and topic != 9:
        has_var_dep = 9 in dep_topics
        if not has_var_dep:
            issues.append({
                'type': 'MISSING_VARIABLES',
                'skill': skill_id,
                'indicators': content_indicators['variables'],
                'current_deps': deps,
                'suggestion': 'Add T09.GK.02 or T09.G1.01 (Variables)'
            })

    # Rule 4: Motion indicators should have T14 dependency (for advanced topics)
    if content_indicators['motion'] and topic >= 16 and topic != 14:
        has_motion_dep = 14 in dep_topics
        if not has_motion_dep and 'move' in skill['description'].lower():
            issues.append({
                'type': 'MISSING_MOTION',
                'skill': skill_id,
                'indicators': content_indicators['motion'],
                'current_deps': deps,
                'suggestion': 'Add T14.GK.01 or similar (Motion blocks)'
            })

    # Rule 5: Pen/drawing indicators should have T21 dependency
    if content_indicators['pen'] and topic >= 16 and topic != 21:
        has_pen_dep = 21 in dep_topics
        if not has_pen_dep:
            issues.append({
                'type': 'MISSING_PEN',
                'skill': skill_id,
                'indicators': content_indicators['pen'],
                'current_deps': deps,
                'suggestion': 'Add T21.GK.01 or T21.G1.01 (Pen)'
            })

    # Rule 6: List indicators should have T10 dependency
    if content_indicators['lists'] and topic != 10:
        has_list_dep = 10 in dep_topics
        if not has_list_dep and 'list' in skill['description'].lower():
            issues.append({
                'type': 'MISSING_LISTS',
                'skill': skill_id,
                'indicators': content_indicators['lists'],
                'current_deps': deps,
                'suggestion': 'Add T10.GK.01 or T10.G1.01 (Lists)'
            })

    return issues

def check_x_minus_2_rule(skill, skills):
    """Check X-2 rule: Grade 1 can only depend on K and 1."""
    issues = []
    skill_id = skill['id']
    skill_grade = extract_grade(skill_id)

    if skill_grade != '1':
        return issues

    for dep in skill['dependencies']:
        if dep not in skills:
            continue
        dep_grade = extract_grade(dep)
        if dep_grade == '2':
            issues.append({
                'type': 'X-2_VIOLATION',
                'skill': skill_id,
                'dependency': dep,
                'dep_name': skills[dep]['skill'],
                'current_deps': skill['dependencies']
            })

    return issues

def check_transitive_redundancy(skill, skills):
    """Check for truly transitive redundant dependencies."""
    issues = []
    skill_id = skill['id']
    deps = skill['dependencies']

    if len(deps) <= 1:
        return issues

    # Build dependency chains
    for i, dep1 in enumerate(deps):
        if dep1 not in skills:
            continue

        for dep2 in deps[i+1:]:
            if dep2 not in skills:
                continue

            # Check if dep1 is in dep2's dependencies
            if dep1 in skills[dep2]['dependencies']:
                issues.append({
                    'type': 'TRANSITIVE_REDUNDANT',
                    'skill': skill_id,
                    'redundant_dep': dep1,
                    'kept_dep': dep2,
                    'reason': f'{dep1} is direct dependency of {dep2}'
                })

            # Check if dep2 is in dep1's dependencies
            elif dep2 in skills[dep1]['dependencies']:
                issues.append({
                    'type': 'TRANSITIVE_REDUNDANT',
                    'skill': skill_id,
                    'redundant_dep': dep2,
                    'kept_dep': dep1,
                    'reason': f'{dep2} is direct dependency of {dep1}'
                })

    return issues

def analyze_advanced_topic_dependencies(skill, skills):
    """Special analysis for advanced topics (T16+) to ensure proper foundation."""
    issues = []
    skill_id = skill['id']
    topic = extract_topic(skill_id)

    if topic < 16:
        return issues

    deps = skill['dependencies']
    dep_topics = set(extract_topic(d) for d in deps if d in skills)

    topic_map = get_topic_mapping()
    focus = topic_map.get(topic, '')

    # Game topics (T16, T29) should have core programming deps
    if focus in ['game_intro', 'advanced_games']:
        missing = []
        if 6 not in dep_topics:  # Events
            missing.append('Events (T6)')
        # Variables needed for games with scoring
        if 'score' in skill['description'].lower() or 'point' in skill['description'].lower():
            if 9 not in dep_topics:
                missing.append('Variables (T9)')

        if missing:
            issues.append({
                'type': 'INCOMPLETE_GAME_FOUNDATION',
                'skill': skill_id,
                'missing': missing,
                'current_deps': deps
            })

    # Art/Creative topics should have visual block deps
    if focus in ['art_creative', 'art_algorithmic']:
        if 'draw' in skill['description'].lower() or 'pen' in skill['description'].lower():
            if 21 not in dep_topics:
                issues.append({
                    'type': 'MISSING_VISUAL_FOUNDATION',
                    'skill': skill_id,
                    'missing': 'Pen (T21)',
                    'current_deps': deps
                })

    return issues

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing all skills...")
    skills = parse_skills(filepath)

    # Filter Grade 1 skills
    g1_skills = {k: v for k, v in skills.items() if extract_grade(k) == '1'}
    print(f"Found {len(g1_skills)} Grade 1 skills across 36 topics\n")

    # Analyze each Grade 1 skill
    all_issues = []

    print("Running comprehensive analysis...")
    for skill_id, skill in sorted(g1_skills.items()):
        # Check X-2 rule
        all_issues.extend(check_x_minus_2_rule(skill, skills))

        # Check required cross-topic dependencies
        all_issues.extend(check_required_dependencies(skill, skills))

        # Check transitive redundancy
        all_issues.extend(check_transitive_redundancy(skill, skills))

        # Check advanced topic foundations
        all_issues.extend(analyze_advanced_topic_dependencies(skill, skills))

    # Group by type
    issues_by_type = defaultdict(list)
    for issue in all_issues:
        issues_by_type[issue['type']].append(issue)

    # Print summary
    print("\n" + "="*100)
    print("COMPREHENSIVE GRADE 1 CROSS-TOPIC DEPENDENCY ANALYSIS")
    print("="*100)
    print(f"\nTotal Grade 1 skills: {len(g1_skills)}")
    print(f"Total issues found: {len(all_issues)}\n")

    for issue_type in sorted(issues_by_type.keys()):
        count = len(issues_by_type[issue_type])
        print(f"{issue_type}: {count} issues")

    # Save detailed report
    output = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G1_COMPREHENSIVE_DEPENDENCY_REPORT.txt'
    with open(output, 'w') as f:
        f.write("COMPREHENSIVE GRADE 1 CROSS-TOPIC DEPENDENCY ANALYSIS\n")
        f.write("="*100 + "\n\n")
        f.write(f"Analysis Date: 2024-11-24\n")
        f.write(f"Total Grade 1 skills analyzed: {len(g1_skills)}\n")
        f.write(f"Total issues identified: {len(all_issues)}\n\n")

        for issue_type in sorted(issues_by_type.keys()):
            type_issues = issues_by_type[issue_type]
            f.write(f"\n{'='*100}\n")
            f.write(f"{issue_type}: {len(type_issues)} ISSUES\n")
            f.write(f"{'='*100}\n\n")

            for idx, issue in enumerate(type_issues, 1):
                skill_id = issue.get('skill', 'N/A')
                f.write(f"{idx}. Skill: {skill_id}\n")

                if skill_id in skills:
                    skill_info = skills[skill_id]
                    f.write(f"   Topic: {skill_info['topic']}\n")
                    f.write(f"   Name: {skill_info['skill']}\n")
                    f.write(f"   Description: {skill_info['description'][:200]}...\n")
                    f.write(f"   Current Dependencies: {', '.join(skill_info['dependencies']) or 'None'}\n\n")

                if 'dependency' in issue:
                    f.write(f"   Problem: Violates X-2 rule - depends on Grade 2 skill\n")
                    f.write(f"   Bad Dependency: {issue['dependency']}\n")
                    if issue.get('dep_name'):
                        f.write(f"   Dependency Name: {issue['dep_name']}\n")

                if 'indicators' in issue:
                    f.write(f"   Content Indicators: {', '.join(issue['indicators'])}\n")

                if 'missing' in issue:
                    if isinstance(issue['missing'], list):
                        f.write(f"   Missing Dependencies: {', '.join(issue['missing'])}\n")
                    else:
                        f.write(f"   Missing Dependency: {issue['missing']}\n")

                if 'redundant_dep' in issue:
                    f.write(f"   Redundant Dependency: {issue['redundant_dep']}\n")
                    f.write(f"   Keep Instead: {issue.get('kept_dep', 'N/A')}\n")
                    f.write(f"   Reason: {issue.get('reason', 'N/A')}\n")

                if 'suggestion' in issue:
                    f.write(f"   FIX: {issue['suggestion']}\n")

                f.write("\n" + "-"*100 + "\n\n")

    print(f"\n\nDetailed report saved to:\n{output}\n")

    # Print actionable summary
    print("\n" + "="*100)
    print("ACTIONABLE FIXES SUMMARY")
    print("="*100 + "\n")

    fixes = defaultdict(list)
    for issue in all_issues:
        skill_id = issue.get('skill')
        if skill_id:
            fixes[skill_id].append(issue)

    print(f"Skills requiring fixes: {len(fixes)}\n")

    # Show top 20 skills needing attention
    skills_by_issue_count = sorted(fixes.items(), key=lambda x: len(x[1]), reverse=True)

    print("Top skills needing attention:\n")
    for skill_id, skill_issues in skills_by_issue_count[:20]:
        print(f"{skill_id}: {len(skill_issues)} issues")
        print(f"  {skills[skill_id]['skill']}")
        for issue in skill_issues:
            print(f"  - {issue['type']}")
        print()

if __name__ == '__main__':
    main()
