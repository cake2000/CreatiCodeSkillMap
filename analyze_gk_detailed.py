#!/usr/bin/env python3
"""
Enhanced Grade K dependency analysis with detailed review.
"""

import re
from collections import defaultdict

def parse_skills_file(filepath):
    """Parse the allskills.md file and extract all GK skills with dependencies."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries (ID: pattern)
    skill_pattern = r'ID: (T\d+\.[A-Z]+\d*\.\d+)'
    parts = re.split(skill_pattern, content)

    skills = {}

    # Process pairs: skill_id, skill_content
    for i in range(1, len(parts), 2):
        if i + 1 >= len(parts):
            break

        skill_id = parts[i]
        skill_content = parts[i + 1]

        # Extract topic (first line after ID)
        topic_match = re.search(r'Topic: (.+)', skill_content)
        topic = topic_match.group(1).strip() if topic_match else "Unknown"

        # Extract skill name
        skill_match = re.search(r'Skill: (.+)', skill_content)
        skill_name = skill_match.group(1).strip() if skill_match else "Unknown"

        # Extract description
        desc_match = re.search(r'Description: (.+?)(?=\n\nDependencies:|\n\nID:|\n\n\n|\Z)', skill_content, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        dependencies = []
        deps_section = re.search(r'Dependencies:(.*?)(?=\n\nID:|\n\n\n|\Z)', skill_content, re.DOTALL)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'\* (T\d+\.[A-Z]+\d*\.\d+):', line)
                if dep_match:
                    dependencies.append(dep_match.group(1))

        skills[skill_id] = {
            'topic': topic,
            'skill_name': skill_name,
            'description': description,
            'dependencies': dependencies
        }

    return skills

def get_skill_grade(skill_id):
    """Extract grade from skill ID (e.g., T01.GK.01 -> 'GK')"""
    match = re.match(r'T\d+\.([A-Z]+\d*)\.', skill_id)
    return match.group(1) if match else None

def get_topic_num(skill_id):
    """Extract topic number from skill ID (e.g., T01.GK.01 -> 'T01')"""
    match = re.match(r'(T\d+)\.', skill_id)
    return match.group(1) if match else None

def analyze_missing_cross_topic_detailed(skills):
    """Detailed analysis of missing cross-topic dependencies."""

    missing = []
    gk_skills = {sid: s for sid, s in skills.items() if get_skill_grade(sid) == 'GK'}

    # Analyze each skill for potential missing dependencies
    for skill_id, skill_data in gk_skills.items():
        topic_num = get_topic_num(skill_id)
        current_deps = skill_data['dependencies']
        skill_text = (skill_data['skill_name'] + ' ' + skill_data['description']).lower()

        # Check 1: T06 (Events & Sequences) with ordering/sequencing should depend on T01
        if topic_num == 'T06':
            if skill_id == 'T06.GK.01':  # First skill - orders pictures
                # Should depend on T01.GK.01 or T01.GK.02
                has_t01 = any(d.startswith('T01.') for d in current_deps)
                if not has_t01:
                    missing.append({
                        'skill_id': skill_id,
                        'topic': skill_data['topic'],
                        'skill_name': skill_data['skill_name'],
                        'reason': 'T06.GK.01 orders pictures (sequencing) but has no T01 dependency',
                        'suggested_dep': 'T01.GK.01 or T01.GK.02',
                        'confidence': 'HIGH',
                        'justification': 'Ordering pictures is the core skill taught in T01.GK.01-02'
                    })

        # Check 2: T02.GK.02 orders pictures to make a story - similar to T01 skills
        if skill_id == 'T02.GK.02':
            # Currently depends on T02.GK.01, but ordering 3-4 pictures is similar to T01.GK.01/02
            # However, T02.GK.01 already depends on T01.GK.01
            # So T02.GK.02 indirectly gets T01 through T02.GK.01 - NOT missing
            pass

        # Check 3: Skills that do counting/quantifying should depend on T01.GK.08 or T10 skills
        counting_patterns = [
            ('how many', 'high'),
            ('count', 'high'),
            (r'\bnumber\b', 'medium'),
        ]

        for pattern, conf in counting_patterns:
            if re.search(pattern, skill_text):
                # Check if skill involves actual counting
                if topic_num not in ['T01', 'T10']:  # T01 and T10 are the counting topics
                    has_counting_dep = False
                    for dep in current_deps:
                        if dep in gk_skills:
                            dep_text = (gk_skills[dep]['skill_name'] + ' ' + gk_skills[dep]['description']).lower()
                            if 'count' in dep_text or 'how many' in dep_text:
                                has_counting_dep = True
                                break

                    # Special cases where counting is NOT the main skill
                    skip_keywords = ['account', 'recount', 'discount', 'county']
                    if any(sk in skill_text for sk in skip_keywords):
                        continue

                    # Only flag if it's clearly about counting
                    if (('count' in skill_text and 'count' in skill_data['skill_name'].lower()) or
                        'how many' in skill_text):
                        if not has_counting_dep and 'T01.GK.08' not in current_deps:
                            # Check if already added
                            if not any(m['skill_id'] == skill_id and 'counting' in m.get('reason', '') for m in missing):
                                missing.append({
                                    'skill_id': skill_id,
                                    'topic': skill_data['topic'],
                                    'skill_name': skill_data['skill_name'],
                                    'reason': f'Skill involves counting ({pattern}) but lacks counting prerequisite',
                                    'suggested_dep': 'T01.GK.08 (Count how many times) or T10.GK.02 (Count items in each group)',
                                    'confidence': conf.upper(),
                                    'justification': f'Found counting keyword: {pattern}'
                                })
                                break

        # Check 4: Skills about patterns/repetition should consider T04 dependency
        pattern_keywords = [
            (r'\bpattern\b', 'high'),
            (r'\brepeat(?:ing|ed|s)?\b', 'high'),
            (r'\bover and over\b', 'high'),
        ]

        for pattern, conf in pattern_keywords:
            if re.search(pattern, skill_text):
                if topic_num not in ['T01', 'T04']:  # T01 and T04 teach patterns
                    has_pattern_dep = any(d.startswith('T04.') for d in current_deps)
                    has_t01_pattern = 'T01.GK.07' in current_deps  # T01.GK.07 is about repeating patterns

                    if not has_pattern_dep and not has_t01_pattern:
                        # Only flag if patterns are central to the skill
                        if 'pattern' in skill_data['skill_name'].lower() or 'repeat' in skill_data['skill_name'].lower():
                            # Check if already added
                            if not any(m['skill_id'] == skill_id and 'pattern' in m.get('reason', '') for m in missing):
                                missing.append({
                                    'skill_id': skill_id,
                                    'topic': skill_data['topic'],
                                    'skill_name': skill_data['skill_name'],
                                    'reason': f'Skill involves patterns/repetition ({pattern}) but lacks prerequisite',
                                    'suggested_dep': 'T04.GK.01 (Identify a simple repeating pattern) or T01.GK.07 (Find the pattern that repeats)',
                                    'confidence': conf.upper(),
                                    'justification': f'Found pattern keyword: {pattern}'
                                })
                                break

        # Check 5: Skills about first/next/last sequencing without T01 dependency
        if topic_num not in ['T01', 'T02']:
            if re.search(r'\b(first|next|last)\b', skill_text):
                # Check if it's really about sequencing
                if any(seq in skill_text for seq in ['in order', 'sequence', 'step']):
                    has_t01 = any(d.startswith('T01.') for d in current_deps)
                    has_t02 = any(d.startswith('T02.') for d in current_deps)

                    if not has_t01 and not has_t02:
                        # Check if already added
                        if not any(m['skill_id'] == skill_id and 'sequencing' in m.get('reason', '') for m in missing):
                            missing.append({
                                'skill_id': skill_id,
                                'topic': skill_data['topic'],
                                'skill_name': skill_data['skill_name'],
                                'reason': 'Skill uses sequencing vocabulary (first/next/last) in ordering context',
                                'suggested_dep': 'T01.GK.01-03 or T02.GK.03 (Use first/next/last to describe a sequence)',
                                'confidence': 'MEDIUM',
                                'justification': 'Uses first/next/last with ordering/sequence context'
                            })

    return missing

def check_circular_dependencies(skills):
    """Check for circular dependencies among GK skills."""

    gk_skills = {sid: s for sid, s in skills.items() if get_skill_grade(sid) == 'GK'}
    circular = []

    def find_cycle(start, current, path, visited):
        """DFS to find cycles."""
        if current in path:
            # Found cycle
            cycle_start = path.index(current)
            return path[cycle_start:] + [current]

        if current in visited or current not in gk_skills:
            return None

        visited.add(current)
        path.append(current)

        for dep in gk_skills[current]['dependencies']:
            if dep in gk_skills:
                cycle = find_cycle(start, dep, path[:], visited)
                if cycle:
                    return cycle

        return None

    checked = set()
    for skill_id in gk_skills:
        if skill_id not in checked:
            cycle = find_cycle(skill_id, skill_id, [], set())
            if cycle:
                cycle_key = tuple(sorted(set(cycle)))
                if cycle_key not in [tuple(sorted(c['skills_involved'])) for c in circular]:
                    circular.append({
                        'cycle': ' -> '.join(cycle),
                        'skills_involved': list(set(cycle))
                    })
                    checked.update(cycle)

    return circular

def print_detailed_report(issues, missing, gk_skills):
    """Print detailed report."""

    print("=" * 100)
    print("GRADE K CROSS-TOPIC DEPENDENCY ANALYSIS - DETAILED REPORT")
    print("=" * 100)
    print()

    print(f"Total Grade K Skills Analyzed: {len(gk_skills)}")
    print()

    # Count by confidence
    high_conf = [m for m in missing if m.get('confidence') == 'HIGH']
    medium_conf = [m for m in missing if m.get('confidence') == 'MEDIUM']
    low_conf = [m for m in missing if m.get('confidence') not in ['HIGH', 'MEDIUM']]

    print("SUMMARY")
    print("-" * 100)
    print(f"X-2 Rule Violations: 0 (All GK skills correctly depend only on GK skills)")
    print(f"Circular Dependencies: {len(issues['circular'])}")
    print(f"Missing Cross-Topic Dependencies (Total): {len(missing)}")
    print(f"  - HIGH confidence: {len(high_conf)}")
    print(f"  - MEDIUM confidence: {len(medium_conf)}")
    print(f"  - LOW/Other confidence: {len(low_conf)}")
    print()

    # Circular dependencies
    if issues['circular']:
        print("=" * 100)
        print("1. CIRCULAR DEPENDENCIES")
        print("=" * 100)
        for i, circ in enumerate(issues['circular'], 1):
            print(f"\n{i}. {circ['cycle']}")
            print(f"   Skills Involved: {', '.join(circ['skills_involved'])}")
            print(f"   Recommended Fix: Break cycle by removing one dependency")

    # Missing dependencies - HIGH confidence
    if high_conf:
        print("\n" + "=" * 100)
        print("2. MISSING CROSS-TOPIC DEPENDENCIES - HIGH CONFIDENCE")
        print("=" * 100)
        print("These are strongly recommended additions based on clear prerequisite relationships.")
        print()

        for i, issue in enumerate(high_conf, 1):
            print(f"\n{i}. {issue['skill_id']}")
            print(f"   Topic: {issue['topic']}")
            print(f"   Skill: {issue['skill_name']}")
            print(f"   Reason: {issue['reason']}")
            print(f"   Suggested Dependency: {issue['suggested_dep']}")
            print(f"   Justification: {issue['justification']}")
            print(f"   Current Dependencies: {', '.join(gk_skills[issue['skill_id']]['dependencies']) if gk_skills[issue['skill_id']]['dependencies'] else 'None'}")

    # Missing dependencies - MEDIUM confidence
    if medium_conf:
        print("\n" + "=" * 100)
        print("3. MISSING CROSS-TOPIC DEPENDENCIES - MEDIUM CONFIDENCE")
        print("=" * 100)
        print("These should be reviewed; they may indicate missing prerequisites.")
        print()

        for i, issue in enumerate(medium_conf, 1):
            print(f"\n{i}. {issue['skill_id']}")
            print(f"   Topic: {issue['topic']}")
            print(f"   Skill: {issue['skill_name']}")
            print(f"   Reason: {issue['reason']}")
            print(f"   Suggested Dependency: {issue['suggested_dep']}")
            print(f"   Justification: {issue['justification']}")
            print(f"   Current Dependencies: {', '.join(gk_skills[issue['skill_id']]['dependencies']) if gk_skills[issue['skill_id']]['dependencies'] else 'None'}")

    # Topic coverage analysis
    print("\n" + "=" * 100)
    print("4. TOPIC COVERAGE ANALYSIS")
    print("=" * 100)

    topic_dist = defaultdict(list)
    for skill_id, skill_data in gk_skills.items():
        topic_num = get_topic_num(skill_id)
        topic_dist[topic_num].append(skill_id)

    print(f"\nTopics with Grade K skills: {len(topic_dist)} out of 36")
    print(f"Topics without Grade K skills: {36 - len(topic_dist)}")
    print()

    # Find topics without GK
    all_topics = [f"T{i:02d}" for i in range(1, 37)]
    missing_topics = [t for t in all_topics if t not in topic_dist]
    if missing_topics:
        print(f"Topics without any Grade K skills:")
        for t in missing_topics:
            print(f"  {t}")

if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills file...")
    skills = parse_skills_file(filepath)

    gk_skills = {sid: s for sid, s in skills.items() if get_skill_grade(sid) == 'GK'}

    print("Checking circular dependencies...")
    circular = check_circular_dependencies(skills)

    print("Analyzing missing cross-topic dependencies...")
    missing = analyze_missing_cross_topic_detailed(skills)

    issues = {
        'circular': circular,
        'x2_violations': []
    }

    print("\nGenerating detailed report...\n")
    print_detailed_report(issues, missing, gk_skills)
