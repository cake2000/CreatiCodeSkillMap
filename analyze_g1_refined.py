#!/usr/bin/env python3
"""
Refined Grade 1 cross-topic dependency analysis.
Distinguishes between true dependencies and false positives.
Focuses on actual programming/Scratch block dependencies.
"""

import re
from collections import defaultdict

def parse_skills(filepath):
    """Extract all skills with their full information."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    current_skill = None
    in_dependencies = False

    lines = content.split('\n')
    for line in lines:
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
    match = re.search(r'\.G([K12])\.', skill_id)
    return match.group(1) if match else None

def extract_topic(skill_id):
    match = re.match(r'T(\d+)\.', skill_id)
    return int(match.group(1)) if match else None

def is_unplugged(skill):
    """Check if skill is unplugged (no Scratch blocks)."""
    desc = skill['description'].lower()
    name = skill['skill'].lower()

    unplugged_indicators = [
        'unplugged',
        'picture cards',
        'picture-based',
        'paper',
        'drag cards',
        'drag-drop',
        'cut out',
        'mcq',
        'multiple choice',
        'match',
        'sort cards',
        'role-play',
        'illustrated',
        'picture matching'
    ]

    return any(indicator in desc or indicator in name for indicator in unplugged_indicators)

def requires_scratch_blocks(skill):
    """Check if skill requires actual Scratch blocks."""
    desc = skill['description'].lower()

    scratch_indicators = [
        'scratch',
        'block',
        'sprite',
        'costume',
        'backdrop',
        'code',
        'program',
        'script'
    ]

    return any(indicator in desc for indicator in scratch_indicators)

def check_genuine_cross_topic_needs(skill, skills):
    """Identify genuine cross-topic dependencies based on actual programming needs."""
    issues = []
    skill_id = skill['id']
    topic = extract_topic(skill_id)
    deps = skill['dependencies']
    dep_topics = set(extract_topic(d) for d in deps if d in skills)

    desc = skill['description'].lower()
    name = skill['skill'].lower()

    # Skip unplugged activities - they don't need programming dependencies
    if is_unplugged(skill):
        return issues

    # Only check skills that involve actual Scratch/programming
    if not requires_scratch_blocks(skill):
        return issues

    # Now check for genuine cross-topic needs

    # 1. Interactive elements need Events
    if topic != 6:
        needs_events = (
            'click' in desc or
            'when' in desc and ('when flag' in desc or 'when key' in desc or 'when space' in desc) or
            'start' in desc and 'green flag' in desc or
            'press' in desc or
            'trigger' in desc
        )
        if needs_events and 6 not in dep_topics:
            issues.append({
                'type': 'MISSING_EVENTS',
                'skill': skill_id,
                'reason': 'Interactive Scratch activity needs Events',
                'suggestion': 'Add T06.GK.03 or T06.G1.01'
            })

    # 2. Repeated block sequences need Loops
    if topic != 7:
        needs_loops = (
            'repeat' in desc and 'block' in desc or
            'loop' in desc or
            'repeat n' in desc or
            'repeat 10' in desc or
            'multiple times' in desc and 'sprite' in desc
        )
        if needs_loops and 7 not in dep_topics:
            issues.append({
                'type': 'MISSING_LOOPS',
                'skill': skill_id,
                'reason': 'Repeated Scratch blocks need Loops',
                'suggestion': 'Add T07.K.01 or T07.G1.01'
            })

    # 3. Scoring/counting in games needs Variables
    if topic != 9:
        needs_variables = (
            'score' in desc and ('game' in desc or 'point' in desc) or
            'variable' in desc or
            'counter' in desc and 'sprite' in desc or
            'track' in desc and ('score' in desc or 'count' in desc)
        )
        if needs_variables and 9 not in dep_topics:
            issues.append({
                'type': 'MISSING_VARIABLES',
                'skill': skill_id,
                'reason': 'Score tracking needs Variables',
                'suggestion': 'Add T09.GK.02 or T09.G1.01'
            })

    # 4. Pen drawing in Scratch
    if topic >= 16 and topic != 21:
        needs_pen = (
            'pen down' in desc or
            'pen up' in desc or
            'stamp' in desc and 'sprite' in desc or
            'draw' in desc and ('pen' in desc or 'trail' in desc or 'line' in desc) and 'sprite' in desc
        )
        if needs_pen and 21 not in dep_topics:
            issues.append({
                'type': 'MISSING_PEN',
                'skill': skill_id,
                'reason': 'Pen drawing in Scratch needs Pen blocks',
                'suggestion': 'Add T21.GK.01 or T21.G1.01'
            })

    # 5. Motion blocks for sprite movement
    if topic >= 16 and topic != 14:
        needs_motion = (
            'move' in desc and ('sprite' in desc or 'blocks' in desc) or
            'glide' in desc or
            'go to' in desc or
            'change x' in desc or
            'change y' in desc
        )
        if needs_motion and 14 not in dep_topics:
            issues.append({
                'type': 'MISSING_MOTION',
                'skill': skill_id,
                'reason': 'Sprite movement needs Motion blocks',
                'suggestion': 'Add T14.GK.01'
            })

    return issues

def check_x_minus_2_violations(skill, skills):
    """Check X-2 rule: Grade 1 cannot depend on Grade 2."""
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
                'severity': 'CRITICAL'
            })

    return issues

def check_transitive_redundancy(skill, skills):
    """Check for transitive redundant dependencies - only flag true redundancy."""
    issues = []
    skill_id = skill['id']
    deps = skill['dependencies']

    if len(deps) <= 1:
        return issues

    # Check each pair of dependencies
    for i, dep1 in enumerate(deps):
        if dep1 not in skills:
            continue

        for dep2 in deps[i+1:]:
            if dep2 not in skills:
                continue

            # Check if dep1 is a direct dependency of dep2
            if dep1 in skills[dep2]['dependencies']:
                # This is transitive - dep1 is reachable through dep2
                # Only flag if there's no good pedagogical reason to keep both
                dep1_topic = extract_topic(dep1)
                dep2_topic = extract_topic(dep2)

                # If they're from the same topic, likely truly redundant
                if dep1_topic == dep2_topic:
                    issues.append({
                        'type': 'TRANSITIVE_REDUNDANT',
                        'skill': skill_id,
                        'redundant_dep': dep1,
                        'kept_dep': dep2,
                        'reason': f'{dep1} is direct dep of {dep2} (same topic)',
                        'severity': 'MEDIUM'
                    })

            # Check reverse
            elif dep2 in skills[dep1]['dependencies']:
                dep1_topic = extract_topic(dep1)
                dep2_topic = extract_topic(dep2)

                if dep1_topic == dep2_topic:
                    issues.append({
                        'type': 'TRANSITIVE_REDUNDANT',
                        'skill': skill_id,
                        'redundant_dep': dep2,
                        'kept_dep': dep1,
                        'reason': f'{dep2} is direct dep of {dep1} (same topic)',
                        'severity': 'MEDIUM'
                    })

    return issues

def check_game_foundations(skill, skills):
    """Check if game-related skills have proper foundations."""
    issues = []
    skill_id = skill['id']
    topic = extract_topic(skill_id)
    deps = skill['dependencies']
    dep_topics = set(extract_topic(d) for d in deps if d in skills)

    desc = skill['description'].lower()
    name = skill['skill'].lower()

    # Game topics: T14 (2D Games), T16 (UI), T29 (Advanced Games)
    is_game_skill = (
        topic in [14, 16, 29] or
        'game' in name or
        'game' in desc and ('play' in desc or 'player' in desc or 'win' in desc)
    )

    if not is_game_skill:
        return issues

    # Games with interactive elements need Events
    if 'click' in desc or 'press' in desc or 'control' in desc:
        if 6 not in dep_topics:
            issues.append({
                'type': 'GAME_NEEDS_EVENTS',
                'skill': skill_id,
                'reason': 'Interactive game needs Events (T6)',
                'severity': 'HIGH'
            })

    # Games with scoring need Variables
    if 'score' in desc or 'point' in desc or 'counter' in desc:
        if 9 not in dep_topics:
            issues.append({
                'type': 'GAME_NEEDS_VARIABLES',
                'skill': skill_id,
                'reason': 'Game with scoring needs Variables (T9)',
                'severity': 'HIGH'
            })

    return issues

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills...")
    skills = parse_skills(filepath)

    g1_skills = {k: v for k, v in skills.items() if extract_grade(k) == '1'}
    print(f"Found {len(g1_skills)} Grade 1 skills\n")

    # Analyze
    all_issues = []

    print("Running refined analysis...")
    for skill_id, skill in sorted(g1_skills.items()):
        # Critical: X-2 violations
        all_issues.extend(check_x_minus_2_violations(skill, skills))

        # Important: Missing cross-topic dependencies
        all_issues.extend(check_genuine_cross_topic_needs(skill, skills))

        # Important: Game foundations
        all_issues.extend(check_game_foundations(skill, skills))

        # Medium: Transitive redundancy
        all_issues.extend(check_transitive_redundancy(skill, skills))

    # Group by type and severity
    by_type = defaultdict(list)
    by_severity = defaultdict(list)

    for issue in all_issues:
        by_type[issue['type']].append(issue)
        severity = issue.get('severity', 'LOW')
        by_severity[severity].append(issue)

    # Print summary
    print("\n" + "="*100)
    print("REFINED GRADE 1 CROSS-TOPIC DEPENDENCY ANALYSIS")
    print("="*100)
    print(f"\nTotal Grade 1 skills: {len(g1_skills)}")
    print(f"Total genuine issues: {len(all_issues)}\n")

    print("By Severity:")
    for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        if severity in by_severity:
            print(f"  {severity}: {len(by_severity[severity])} issues")

    print("\nBy Type:")
    for issue_type in sorted(by_type.keys()):
        print(f"  {issue_type}: {len(by_type[issue_type])} issues")

    # Save detailed report
    output = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G1_REFINED_DEPENDENCY_FIXES.md'
    with open(output, 'w') as f:
        f.write("# Grade 1 Cross-Topic Dependency Analysis - Actionable Fixes\n\n")
        f.write(f"**Analysis Date:** 2024-11-24\n\n")
        f.write(f"**Total Grade 1 Skills:** {len(g1_skills)}\n\n")
        f.write(f"**Total Issues Found:** {len(all_issues)}\n\n")

        f.write("## Issue Summary\n\n")
        f.write("| Severity | Count |\n")
        f.write("|----------|-------|\n")
        for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            count = len(by_severity.get(severity, []))
            if count > 0:
                f.write(f"| {severity} | {count} |\n")

        f.write("\n## Issues by Type\n\n")
        for issue_type in sorted(by_type.keys()):
            count = len(by_type[issue_type])
            f.write(f"- **{issue_type}**: {count} issues\n")

        # Detailed issues by severity
        for severity in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            if severity not in by_severity:
                continue

            issues = by_severity[severity]
            f.write(f"\n---\n\n## {severity} Priority Issues ({len(issues)})\n\n")

            for idx, issue in enumerate(issues, 1):
                skill_id = issue.get('skill', 'N/A')
                f.write(f"### {idx}. {skill_id}\n\n")

                if skill_id in skills:
                    skill_info = skills[skill_id]
                    f.write(f"**Topic:** {skill_info['topic']}\n\n")
                    f.write(f"**Skill:** {skill_info['skill']}\n\n")
                    f.write(f"**Description:** {skill_info['description'][:300]}...\n\n")
                    f.write(f"**Current Dependencies:** {', '.join(skill_info['dependencies']) or 'None'}\n\n")

                f.write(f"**Issue Type:** {issue['type']}\n\n")

                if 'dependency' in issue:
                    f.write(f"**Violates X-2 Rule:** Depends on Grade 2 skill `{issue['dependency']}`\n\n")
                    f.write(f"**Bad Dependency Name:** {issue.get('dep_name', 'N/A')}\n\n")

                if 'reason' in issue:
                    f.write(f"**Reason:** {issue['reason']}\n\n")

                if 'redundant_dep' in issue:
                    f.write(f"**Redundant Dependency:** `{issue['redundant_dep']}`\n\n")
                    f.write(f"**Keep Instead:** `{issue.get('kept_dep', 'N/A')}`\n\n")

                if 'suggestion' in issue:
                    f.write(f"**Fix:** {issue['suggestion']}\n\n")

                f.write("\n")

    print(f"\n\nDetailed report saved to:\n{output}\n")

    # Print actionable summary
    print("\n" + "="*100)
    print("CRITICAL & HIGH PRIORITY FIXES")
    print("="*100 + "\n")

    critical_high = by_severity.get('CRITICAL', []) + by_severity.get('HIGH', [])
    if critical_high:
        print(f"Total critical/high priority: {len(critical_high)}\n")
        for issue in critical_high[:15]:
            skill_id = issue.get('skill')
            print(f"{skill_id}")
            print(f"  {skills[skill_id]['skill']}")
            print(f"  Issue: {issue['type']}")
            print(f"  Fix: {issue.get('suggestion', issue.get('reason', 'See report'))}")
            print()
    else:
        print("No critical or high priority issues found!")

if __name__ == '__main__':
    main()
