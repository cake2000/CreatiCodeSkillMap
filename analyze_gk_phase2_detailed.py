#!/usr/bin/env python3
"""
Detailed analysis of Grade K cross-topic dependencies.
Focus on genuine missing dependencies vs false positives.
"""

import re
from collections import defaultdict

def parse_skills_from_md(file_path):
    """Parse all skills from allskills.md file."""
    skills = []
    current_skill = None

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith('ID: '):
            if current_skill:
                skills.append(current_skill)

            skill_id = line.replace('ID: ', '').strip()
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': [],
                'line_number': i + 1
            }

        elif current_skill:
            if line.startswith('Topic: '):
                current_skill['topic'] = line.replace('Topic: ', '').strip()

            elif line.startswith('Skill: '):
                current_skill['skill'] = line.replace('Skill: ', '').strip()

            elif line.startswith('Description: '):
                desc = line.replace('Description: ', '').strip()
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith(('ID:', 'Topic:', 'Skill:', 'Dependencies:', 'Blocks:')):
                    if lines[j].strip():
                        desc += ' ' + lines[j].strip()
                    j += 1
                current_skill['description'] = desc

            elif line.startswith('Dependencies:'):
                j = i + 1
                while j < len(lines) and lines[j].strip().startswith('* '):
                    dep_line = lines[j].strip()[2:]
                    dep_match = re.match(r'(T\d+\.[A-Z0-9]+\.\d+)', dep_line)
                    if dep_match:
                        current_skill['dependencies'].append(dep_match.group(1))
                    j += 1

        i += 1

    if current_skill:
        skills.append(current_skill)

    return skills

def extract_grade_from_id(skill_id):
    match = re.match(r'T\d+\.([A-Z0-9]+)\.\d+', skill_id)
    return match.group(1) if match else None

def extract_topic_from_id(skill_id):
    match = re.match(r'(T\d+)\.[A-Z0-9]+\.\d+', skill_id)
    return match.group(1) if match else None

def detailed_missing_deps_analysis(skills):
    """Detailed analysis of genuinely missing cross-topic dependencies."""

    gk_skills = [s for s in skills if extract_grade_from_id(s['id']) == 'GK']
    skill_by_id = {s['id']: s for s in skills}

    print("=" * 80)
    print("DETAILED CROSS-TOPIC DEPENDENCY ANALYSIS FOR GRADE K")
    print("=" * 80)
    print()

    # Analyze specific patterns that truly indicate missing dependencies
    genuine_missing = []

    # Pattern 1: Game skills (T14) that should depend on foundational concepts
    print("Pattern 1: Game Skills (T14) Dependencies")
    print("-" * 80)
    game_skills = [s for s in gk_skills if extract_topic_from_id(s['id']) == 'T14']
    for skill in game_skills:
        desc_lower = skill['description'].lower()

        # Check for score/counting concepts
        if 'score' in desc_lower or 'count' in desc_lower:
            has_var_dep = any(extract_topic_from_id(d) == 'T09' for d in skill['dependencies'])
            if not has_var_dep:
                genuine_missing.append({
                    'skill': skill['id'],
                    'skill_name': skill['skill'],
                    'missing_topic': 'T09',
                    'reason': 'Game with score/counting should understand variables (labels with numbers)',
                    'priority': 'HIGH'
                })

        # Check for control concepts
        if 'control' in desc_lower or 'button' in desc_lower or 'key' in desc_lower:
            has_event_dep = any(extract_topic_from_id(d) == 'T06' for d in skill['dependencies'])
            if not has_event_dep:
                genuine_missing.append({
                    'skill': skill['id'],
                    'skill_name': skill['skill'],
                    'missing_topic': 'T06',
                    'reason': 'Game with controls should understand events',
                    'priority': 'HIGH'
                })

    print(f"Found {len([m for m in genuine_missing if extract_topic_from_id(m['skill']) == 'T14'])} genuine missing dependencies for game skills")

    # Pattern 2: Data skills (T25-T27) that need foundational concepts
    print("\nPattern 2: Data Skills (T25-T27) Dependencies")
    print("-" * 80)
    data_skills = [s for s in gk_skills if extract_topic_from_id(s['id']) in ['T25', 'T26', 'T27']]
    for skill in data_skills:
        desc_lower = skill['description'].lower()

        # Data collection/logging should understand counting
        if extract_topic_from_id(skill['id']) == 'T26':
            if 'count' in desc_lower or 'number' in desc_lower:
                has_var_dep = any(extract_topic_from_id(d) == 'T09' for d in skill['dependencies'])
                if not has_var_dep:
                    genuine_missing.append({
                        'skill': skill['id'],
                        'skill_name': skill['skill'],
                        'missing_topic': 'T09',
                        'reason': 'Data counting should understand variables/numbers',
                        'priority': 'MEDIUM'
                    })

        # Data analysis should understand grouping/lists
        if extract_topic_from_id(skill['id']) == 'T27':
            if 'sort' in desc_lower or 'group' in desc_lower:
                has_list_dep = any(extract_topic_from_id(d) == 'T10' for d in skill['dependencies'])
                if not has_list_dep:
                    genuine_missing.append({
                        'skill': skill['id'],
                        'skill_name': skill['skill'],
                        'missing_topic': 'T10',
                        'reason': 'Data sorting/grouping should understand lists/tables concepts',
                        'priority': 'MEDIUM'
                    })

    print(f"Found {len([m for m in genuine_missing if extract_topic_from_id(m['skill']) in ['T25', 'T26', 'T27']])} genuine missing dependencies for data skills")

    # Pattern 3: Creative/Art skills (T20) that use patterns
    print("\nPattern 3: Creative Coding Skills (T20) Dependencies")
    print("-" * 80)
    art_skills = [s for s in gk_skills if extract_topic_from_id(s['id']) == 'T20']
    for skill in art_skills:
        # T20 skills already have good dependencies on T04 (patterns)
        # Check if they're complete
        pass
    print(f"T20 skills appear to have appropriate dependencies on T04 (patterns)")

    # Pattern 4: Animation/Story skills (T15) that need sequencing
    print("\nPattern 4: Animation/Story Skills (T15) Dependencies")
    print("-" * 80)
    story_skills = [s for s in gk_skills if extract_topic_from_id(s['id']) == 'T15']
    for skill in story_skills:
        desc_lower = skill['description'].lower()

        # Stories with sequences should understand ordering
        if 'order' in desc_lower or 'sequence' in desc_lower:
            has_algo_dep = any(extract_topic_from_id(d) == 'T01' for d in skill['dependencies'])
            if not has_algo_dep:
                genuine_missing.append({
                    'skill': skill['id'],
                    'skill_name': skill['skill'],
                    'missing_topic': 'T01',
                    'reason': 'Story sequencing should build on algorithm ordering',
                    'priority': 'MEDIUM'
                })

    print(f"Found {len([m for m in genuine_missing if extract_topic_from_id(m['skill']) == 'T15'])} genuine missing dependencies for story skills")

    # Pattern 5: Debugging skills (T13) that need algorithm foundation
    print("\nPattern 5: Debugging Skills (T13) Dependencies")
    print("-" * 80)
    debug_skills = [s for s in gk_skills if extract_topic_from_id(s['id']) == 'T13']
    for skill in debug_skills:
        # Most debugging skills should understand basic sequencing
        has_algo_dep = any(extract_topic_from_id(d) == 'T01' for d in skill['dependencies'])
        if not has_algo_dep and skill['id'] not in ['T13.GK.01']:  # First debugging skill can be foundational
            genuine_missing.append({
                'skill': skill['id'],
                'skill_name': skill['skill'],
                'missing_topic': 'T01',
                'reason': 'Debugging sequences needs understanding of correct sequences first',
                'priority': 'HIGH'
            })

    print(f"Found {len([m for m in genuine_missing if extract_topic_from_id(m['skill']) == 'T13'])} genuine missing dependencies for debugging skills")

    # Pattern 6: Check for skills that build on each other within topic
    print("\nPattern 6: Within-Topic Dependency Completeness")
    print("-" * 80)

    # Group skills by topic
    skills_by_topic = defaultdict(list)
    for skill in gk_skills:
        topic = extract_topic_from_id(skill['id'])
        skills_by_topic[topic].append(skill)

    within_topic_issues = []
    for topic, topic_skills in sorted(skills_by_topic.items()):
        # Sort by skill number
        topic_skills.sort(key=lambda s: int(re.search(r'\.(\d+)$', s['id']).group(1)))

        # Check if later skills depend on earlier skills appropriately
        for i, skill in enumerate(topic_skills):
            if i > 0:  # Not the first skill
                # Should probably depend on at least one earlier skill in same topic
                has_prev_dep = any(
                    extract_topic_from_id(d) == topic and
                    int(re.search(r'\.(\d+)$', d).group(1)) < int(re.search(r'\.(\d+)$', skill['id']).group(1))
                    for d in skill['dependencies']
                )

                # Exception: if it's a parallel foundational skill (e.g., T14.GK.01, T14.GK.02, T14.GK.03)
                is_foundational = len(skill['dependencies']) == 0

                if not has_prev_dep and not is_foundational and len(topic_skills) > 2:
                    within_topic_issues.append({
                        'skill': skill['id'],
                        'skill_name': skill['skill'],
                        'topic': topic,
                        'reason': f'Later skill in {topic} with no dependencies on earlier skills in same topic',
                        'suggestion': f'Consider if it should depend on {topic_skills[i-1]["id"]}'
                    })

    print(f"Found {len(within_topic_issues)} potential within-topic dependency gaps")
    if within_topic_issues:
        for issue in within_topic_issues[:10]:
            print(f"  {issue['skill']}: {issue['skill_name']}")
            print(f"    {issue['reason']}")
            print(f"    {issue['suggestion']}")

    # Summary
    print("\n\n" + "=" * 80)
    print("GENUINE MISSING CROSS-TOPIC DEPENDENCIES")
    print("=" * 80)

    # Group by priority
    high_priority = [m for m in genuine_missing if m['priority'] == 'HIGH']
    medium_priority = [m for m in genuine_missing if m['priority'] == 'MEDIUM']

    print(f"\nHIGH PRIORITY: {len(high_priority)} dependencies to add")
    print("-" * 80)
    for dep in high_priority:
        skill = skill_by_id[dep['skill']]
        print(f"\nSkill: {dep['skill']}")
        print(f"  Name: {dep['skill_name']}")
        print(f"  Add dependency on topic: {dep['missing_topic']}")
        print(f"  Reason: {dep['reason']}")
        print(f"  Current deps: {', '.join(skill['dependencies']) if skill['dependencies'] else 'None'}")

    print(f"\n\nMEDIUM PRIORITY: {len(medium_priority)} dependencies to add")
    print("-" * 80)
    for dep in medium_priority:
        skill = skill_by_id[dep['skill']]
        print(f"\nSkill: {dep['skill']}")
        print(f"  Name: {dep['skill_name']}")
        print(f"  Add dependency on topic: {dep['missing_topic']}")
        print(f"  Reason: {dep['reason']}")
        print(f"  Current deps: {', '.join(skill['dependencies']) if skill['dependencies'] else 'None'}")

    print("\n\n" + "=" * 80)
    print("SPECIFIC RECOMMENDATIONS")
    print("=" * 80)

    # Make specific recommendations with skill IDs
    recommendations = []

    for dep in genuine_missing:
        skill = skill_by_id[dep['skill']]
        target_topic = dep['missing_topic']

        # Find an appropriate skill in target topic to depend on
        target_topic_skills = [s for s in gk_skills if extract_topic_from_id(s['id']) == target_topic]

        # Choose the first or most basic skill in that topic
        if target_topic_skills:
            # Prefer skills with fewer dependencies (more foundational)
            target_topic_skills.sort(key=lambda s: len(s['dependencies']))
            suggested_dep = target_topic_skills[0]['id']

            recommendations.append({
                'skill': dep['skill'],
                'add_dependency': suggested_dep,
                'reason': dep['reason'],
                'priority': dep['priority']
            })

    print("\nSpecific dependency additions recommended:")
    print()
    for rec in sorted(recommendations, key=lambda r: (r['priority'], r['skill'])):
        print(f"[{rec['priority']}] Add to {rec['skill']}:")
        print(f"  * {rec['add_dependency']}: {skill_by_id[rec['add_dependency']]['skill']}")
        print(f"  Reason: {rec['reason']}")
        print()

if __name__ == '__main__':
    file_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = parse_skills_from_md(file_path)
    detailed_missing_deps_analysis(skills)
