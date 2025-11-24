#!/usr/bin/env python3
"""
Analyze Grade K skills for cross-topic dependency issues.
Reads allskills.md and extracts all GK skills with dependencies.
"""

import re
from collections import defaultdict

def parse_skills_file(filepath):
    """Parse the allskills.md file and extract all GK skills with dependencies."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries (ID: pattern)
    skill_pattern = r'ID: (T\d+\.GK\.\d+)'
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

        # Extract dependencies
        dependencies = []
        deps_section = re.search(r'Dependencies:(.*?)(?=\n\n|\nID:|\Z)', skill_content, re.DOTALL)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'\* (T\d+\.[A-Z]+\d*\.\d+):', line)
                if dep_match:
                    dependencies.append(dep_match.group(1))

        skills[skill_id] = {
            'topic': topic,
            'skill_name': skill_name,
            'dependencies': dependencies,
            'content': skill_content[:500]  # Keep first 500 chars for reference
        }

    return skills

def get_skill_grade(skill_id):
    """Extract grade from skill ID (e.g., T01.GK.01 -> 'GK')"""
    match = re.match(r'T\d+\.([A-Z]+\d*)\.', skill_id)
    return match.group(1) if match else None

def analyze_dependencies(skills):
    """Analyze all GK skills for dependency issues."""

    issues = {
        'x2_violations': [],
        'missing_cross_topic': [],
        'circular': [],
        'redundant_transitive': []
    }

    gk_skills = {sid: s for sid, s in skills.items() if get_skill_grade(sid) == 'GK'}

    print(f"Total Grade K skills found: {len(gk_skills)}\n")

    # Check X-2 rule violations (GK depending on non-GK)
    for skill_id, skill_data in gk_skills.items():
        for dep in skill_data['dependencies']:
            dep_grade = get_skill_grade(dep)
            if dep_grade != 'GK':
                issues['x2_violations'].append({
                    'skill_id': skill_id,
                    'topic': skill_data['topic'],
                    'skill_name': skill_data['skill_name'],
                    'bad_dependency': dep,
                    'dep_grade': dep_grade,
                    'issue': f"GK skill depends on {dep_grade} skill"
                })

    # Check for circular dependencies
    def has_circular_path(start, current, path, visited_in_path):
        if current in visited_in_path:
            return True, path + [current]
        if current not in gk_skills:
            return False, []

        visited_in_path.add(current)
        for dep in gk_skills[current]['dependencies']:
            if dep in gk_skills:
                found, circ_path = has_circular_path(start, dep, path + [current], visited_in_path.copy())
                if found and start in circ_path:
                    return True, circ_path
        return False, []

    checked_circulars = set()
    for skill_id in gk_skills:
        if skill_id not in checked_circulars:
            has_circ, circ_path = has_circular_path(skill_id, skill_id, [], set())
            if has_circ:
                circ_key = tuple(sorted(circ_path))
                if circ_key not in checked_circulars:
                    issues['circular'].append({
                        'cycle': ' -> '.join(circ_path),
                        'skills_involved': circ_path
                    })
                    checked_circulars.update(circ_path)

    # Check for redundant transitive dependencies
    for skill_id, skill_data in gk_skills.items():
        direct_deps = set(skill_data['dependencies'])

        # Find all indirect dependencies (transitive closure)
        indirect_deps = set()
        to_check = list(direct_deps)
        checked = set()

        while to_check:
            dep = to_check.pop(0)
            if dep in checked or dep not in gk_skills:
                continue
            checked.add(dep)

            for sub_dep in gk_skills[dep]['dependencies']:
                if sub_dep not in direct_deps and sub_dep in gk_skills:
                    indirect_deps.add(sub_dep)
                    if sub_dep not in checked:
                        to_check.append(sub_dep)

        # Check if any direct dependency is also reachable indirectly
        for dep in direct_deps:
            if dep in indirect_deps:
                # This is a potentially redundant dependency
                # Find which other direct dep leads to it
                for other_dep in direct_deps:
                    if other_dep != dep:
                        # Check if other_dep leads to dep
                        reachable = set()
                        to_check = [other_dep]
                        checked = set()
                        while to_check:
                            current = to_check.pop(0)
                            if current in checked or current not in gk_skills:
                                continue
                            checked.add(current)
                            if current == dep:
                                reachable.add(current)
                                break
                            for sub_dep in gk_skills[current]['dependencies']:
                                if sub_dep in gk_skills and sub_dep not in checked:
                                    to_check.append(sub_dep)

                        if dep in reachable:
                            issues['redundant_transitive'].append({
                                'skill_id': skill_id,
                                'topic': skill_data['topic'],
                                'skill_name': skill_data['skill_name'],
                                'redundant_dep': dep,
                                'via_dep': other_dep,
                                'issue': f"Direct dependency on {dep} is redundant (reachable via {other_dep})"
                            })
                            break

    return issues, gk_skills

def analyze_missing_cross_topic(skills):
    """Analyze potential missing cross-topic dependencies."""

    missing = []
    gk_skills = {sid: s for sid, s in skills.items() if get_skill_grade(sid) == 'GK'}

    # Group skills by topic
    by_topic = defaultdict(list)
    for skill_id, skill_data in gk_skills.items():
        topic_num = re.match(r'(T\d+)', skill_id).group(1)
        by_topic[topic_num].append((skill_id, skill_data))

    # Check specific patterns that might indicate missing dependencies

    # Pattern 1: Skills about sequencing should depend on T01 (Everyday Algorithms)
    sequencing_keywords = ['order', 'sequence', 'first', 'next', 'last', 'step']

    for skill_id, skill_data in gk_skills.items():
        topic_num = re.match(r'(T\d+)', skill_id).group(1)
        skill_lower = (skill_data['skill_name'] + ' ' + skill_data.get('content', '')).lower()

        # Check if skill mentions sequencing but doesn't depend on T01
        if any(kw in skill_lower for kw in sequencing_keywords):
            has_t01_dep = any(dep.startswith('T01.') for dep in skill_data['dependencies'])
            if not has_t01_dep and topic_num != 'T01':
                # Check if it's about pattern (might be T04 instead)
                if 'pattern' not in skill_lower and 'repeat' not in skill_lower:
                    missing.append({
                        'skill_id': skill_id,
                        'topic': skill_data['topic'],
                        'skill_name': skill_data['skill_name'],
                        'missing_dep_topic': 'T01',
                        'reason': 'Skill involves sequencing concepts but missing T01 dependency',
                        'keywords_found': [kw for kw in sequencing_keywords if kw in skill_lower]
                    })

    # Pattern 2: Skills about patterns should potentially depend on T04
    pattern_keywords = ['pattern', 'repeat', 'again', 'over']

    for skill_id, skill_data in gk_skills.items():
        topic_num = re.match(r'(T\d+)', skill_id).group(1)
        skill_lower = (skill_data['skill_name'] + ' ' + skill_data.get('content', '')).lower()

        if any(kw in skill_lower for kw in pattern_keywords):
            has_t04_dep = any(dep.startswith('T04.') for dep in skill_data['dependencies'])
            if not has_t04_dep and topic_num != 'T04' and topic_num != 'T01':
                missing.append({
                    'skill_id': skill_id,
                    'topic': skill_data['topic'],
                    'skill_name': skill_data['skill_name'],
                    'missing_dep_topic': 'T04',
                    'reason': 'Skill involves pattern concepts but missing T04 dependency',
                    'keywords_found': [kw for kw in pattern_keywords if kw in skill_lower]
                })

    # Pattern 3: Skills about counting should depend on basic counting
    counting_keywords = ['count', 'how many', 'number']

    for skill_id, skill_data in gk_skills.items():
        topic_num = re.match(r'(T\d+)', skill_id).group(1)
        skill_lower = (skill_data['skill_name'] + ' ' + skill_data.get('content', '')).lower()

        if any(kw in skill_lower for kw in counting_keywords):
            # Check if there are appropriate counting dependencies
            # T01.GK.08 is about counting
            if topic_num not in ['T01', 'T10']:  # T10 is lists which has counting built-in
                has_counting_dep = any('count' in gk_skills.get(dep, {}).get('skill_name', '').lower()
                                      for dep in skill_data['dependencies'] if dep in gk_skills)
                if not has_counting_dep and 'T01.GK.08' not in skill_data['dependencies']:
                    # Only flag if it's really about counting items
                    if 'count' in skill_lower or 'how many' in skill_lower:
                        missing.append({
                            'skill_id': skill_id,
                            'topic': skill_data['topic'],
                            'skill_name': skill_data['skill_name'],
                            'missing_dep': 'T01.GK.08',
                            'reason': 'Skill involves counting but missing counting dependency',
                            'keywords_found': [kw for kw in counting_keywords if kw in skill_lower]
                        })

    return missing

def print_report(issues, missing_cross_topic, gk_skills):
    """Print comprehensive report."""

    print("=" * 80)
    print("GRADE K CROSS-TOPIC DEPENDENCY ANALYSIS REPORT")
    print("=" * 80)
    print()

    print(f"Total Grade K Skills Analyzed: {len(gk_skills)}")
    print()

    # Summary
    print("SUMMARY OF ISSUES FOUND")
    print("-" * 80)
    print(f"X-2 Rule Violations (GK depending on non-GK): {len(issues['x2_violations'])}")
    print(f"Missing Cross-Topic Dependencies: {len(missing_cross_topic)}")
    print(f"Circular Dependencies: {len(issues['circular'])}")
    print(f"Redundant Transitive Dependencies: {len(issues['redundant_transitive'])}")
    print(f"TOTAL ISSUES: {len(issues['x2_violations']) + len(missing_cross_topic) + len(issues['circular']) + len(issues['redundant_transitive'])}")
    print()

    # X-2 Violations
    if issues['x2_violations']:
        print("=" * 80)
        print("1. X-2 RULE VIOLATIONS (Grade K depending on non-Grade K)")
        print("=" * 80)
        for i, issue in enumerate(issues['x2_violations'], 1):
            print(f"\n{i}. {issue['skill_id']}")
            print(f"   Topic: {issue['topic']}")
            print(f"   Skill: {issue['skill_name']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Bad Dependency: {issue['bad_dependency']} (Grade {issue['dep_grade']})")
            print(f"   Recommended Fix: Remove dependency or replace with appropriate GK skill")

    # Missing Cross-Topic Dependencies
    if missing_cross_topic:
        print("\n" + "=" * 80)
        print("2. POTENTIAL MISSING CROSS-TOPIC DEPENDENCIES")
        print("=" * 80)
        for i, issue in enumerate(missing_cross_topic, 1):
            print(f"\n{i}. {issue['skill_id']}")
            print(f"   Topic: {issue['topic']}")
            print(f"   Skill: {issue['skill_name']}")
            print(f"   Reason: {issue['reason']}")
            if 'missing_dep_topic' in issue:
                print(f"   Missing Dependency Topic: {issue['missing_dep_topic']}")
            if 'missing_dep' in issue:
                print(f"   Suggested Dependency: {issue['missing_dep']}")
            print(f"   Keywords Found: {', '.join(issue['keywords_found'])}")
            print(f"   Recommended Fix: Review and add appropriate cross-topic dependency")

    # Circular Dependencies
    if issues['circular']:
        print("\n" + "=" * 80)
        print("3. CIRCULAR DEPENDENCIES")
        print("=" * 80)
        for i, issue in enumerate(issues['circular'], 1):
            print(f"\n{i}. Circular Dependency Detected:")
            print(f"   Cycle: {issue['cycle']}")
            print(f"   Recommended Fix: Break the cycle by removing one dependency")

    # Redundant Transitive Dependencies
    if issues['redundant_transitive']:
        print("\n" + "=" * 80)
        print("4. POTENTIALLY REDUNDANT TRANSITIVE DEPENDENCIES")
        print("=" * 80)
        print("(Note: Only flagged if genuinely redundant - A→B and B→C makes A→C unnecessary)")
        for i, issue in enumerate(issues['redundant_transitive'], 1):
            print(f"\n{i}. {issue['skill_id']}")
            print(f"   Topic: {issue['topic']}")
            print(f"   Skill: {issue['skill_name']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Redundant Dependency: {issue['redundant_dep']}")
            print(f"   Already Reachable Via: {issue['via_dep']}")
            print(f"   Recommended Fix: Consider removing {issue['redundant_dep']} (already implied)")

    # Topic distribution
    print("\n" + "=" * 80)
    print("GRADE K SKILLS BY TOPIC")
    print("=" * 80)
    topic_dist = defaultdict(list)
    for skill_id, skill_data in gk_skills.items():
        topic_num = re.match(r'(T\d+)', skill_id).group(1)
        topic_dist[topic_num].append(skill_id)

    for topic in sorted(topic_dist.keys()):
        print(f"\n{topic}: {len(topic_dist[topic])} skills")
        for skill_id in sorted(topic_dist[topic]):
            deps = gk_skills[skill_id]['dependencies']
            cross_topic = [d for d in deps if not d.startswith(topic + '.')]
            if cross_topic:
                print(f"  {skill_id} - {len(deps)} deps ({len(cross_topic)} cross-topic)")
            else:
                print(f"  {skill_id} - {len(deps)} deps")

if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills file...")
    skills = parse_skills_file(filepath)

    print("Analyzing dependencies...")
    issues, gk_skills = analyze_dependencies(skills)

    print("Analyzing missing cross-topic dependencies...")
    missing_cross_topic = analyze_missing_cross_topic(skills)

    print("\nGenerating report...\n")
    print_report(issues, missing_cross_topic, gk_skills)
