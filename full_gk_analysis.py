#!/usr/bin/env python3
"""
Comprehensive Grade K dependency analysis.
Extracts all GK skills with full details and performs thorough dependency review.
"""

import re
import json
from collections import defaultdict

def parse_skills_file(filepath):
    """Parse the allskills.md file and extract ALL skills with dependencies."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries (ID: pattern)
    skill_pattern = r'\nID: (T\d+\.[A-Z]+\d*\.\d+)'
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

def comprehensive_dependency_analysis(skills):
    """Perform comprehensive dependency analysis."""

    gk_skills = {sid: s for sid, s in skills.items() if get_skill_grade(sid) == 'GK'}
    issues = []

    # Issue 1: Check X-2 rule
    for skill_id, skill_data in gk_skills.items():
        for dep in skill_data['dependencies']:
            dep_grade = get_skill_grade(dep)
            if dep_grade != 'GK':
                issues.append({
                    'type': 'X2_VIOLATION',
                    'skill_id': skill_id,
                    'topic': skill_data['topic'],
                    'skill_name': skill_data['skill_name'],
                    'issue': f"Depends on {dep} (Grade {dep_grade}) - violates X-2 rule",
                    'bad_dependency': dep,
                    'fix': f"Remove {dep} or replace with appropriate GK skill"
                })

    # Issue 2: T06.GK.01 orders pictures without T01 dependency
    if 'T06.GK.01' in gk_skills:
        deps = gk_skills['T06.GK.01']['dependencies']
        if not any(d.startswith('T01.') for d in deps):
            issues.append({
                'type': 'MISSING_CROSS_TOPIC',
                'skill_id': 'T06.GK.01',
                'topic': gk_skills['T06.GK.01']['topic'],
                'skill_name': gk_skills['T06.GK.01']['skill_name'],
                'issue': 'Orders pictures (sequencing) without T01 dependency',
                'suggested_addition': 'T01.GK.01 or T01.GK.02',
                'confidence': 'HIGH',
                'rationale': 'Ordering pictures is the foundational skill in T01.GK.01-02'
            })

    # Issue 3: T06.GK.02 uses first/next/last vocabulary - should it depend on T02.GK.03?
    if 'T06.GK.02' in gk_skills:
        deps = gk_skills['T06.GK.02']['dependencies']
        desc = gk_skills['T06.GK.02']['description'].lower()
        # Check if T02.GK.03 teaches this vocabulary
        if 'T02.GK.03' in gk_skills and 'first' in desc and 'next' in desc and 'last' in desc:
            # T02.GK.03 is "Use first/next/last to describe a sequence"
            if 'T02.GK.03' not in deps:
                # But check if this is really necessary - T06 builds on T01, not necessarily T02
                # T02 is about algorithm diagrams, T06 is about events
                # This might not be a true missing dependency
                pass

    # Issue 4: Skills about counting without counting prerequisite
    counting_skills = []
    for skill_id, skill_data in gk_skills.items():
        text = (skill_data['skill_name'] + ' ' + skill_data['description']).lower()
        if 'count' in skill_data['skill_name'].lower() or 'how many' in text:
            topic = get_topic_num(skill_id)
            if topic not in ['T01', 'T10']:
                # Check if has counting dependency
                has_count_dep = False
                for dep in skill_data['dependencies']:
                    if dep in gk_skills:
                        dep_text = gk_skills[dep]['skill_name'].lower()
                        if 'count' in dep_text:
                            has_count_dep = True
                            break
                    if dep == 'T01.GK.08':  # The counting skill
                        has_count_dep = True
                        break

                if not has_count_dep:
                    counting_skills.append(skill_id)
                    issues.append({
                        'type': 'MISSING_CROSS_TOPIC',
                        'skill_id': skill_id,
                        'topic': skill_data['topic'],
                        'skill_name': skill_data['skill_name'],
                        'issue': 'Involves counting without counting prerequisite',
                        'suggested_addition': 'T01.GK.08 (Count how many times) or T10.GK.02 (Count items in each group)',
                        'confidence': 'HIGH' if 'count' in skill_data['skill_name'].lower() else 'MEDIUM',
                        'rationale': 'Counting is explicitly mentioned in skill'
                    })

    # Issue 5: Skills about repeating/patterns without pattern prerequisite
    for skill_id, skill_data in gk_skills.items():
        if skill_id in ['T01.GK.07', 'T01.GK.08', 'T04.GK.01', 'T04.GK.02', 'T04.GK.03', 'T04.GK.04']:
            continue  # Skip pattern-teaching skills
        text = (skill_data['skill_name'] + ' ' + skill_data['description']).lower()
        if re.search(r'\brepeat(?:ed|ing|s)?\b', skill_data['skill_name'].lower()):
            # Check if has pattern dependency
            has_pattern_dep = any(d.startswith('T04.') or d == 'T01.GK.07' for d in skill_data['dependencies'])
            if not has_pattern_dep:
                issues.append({
                    'type': 'MISSING_CROSS_TOPIC',
                    'skill_id': skill_id,
                    'topic': skill_data['topic'],
                    'skill_name': skill_data['skill_name'],
                    'issue': 'About repetition/patterns without pattern prerequisite',
                    'suggested_addition': 'T04.GK.01 or T01.GK.07',
                    'confidence': 'HIGH',
                    'rationale': '"Repeat" in skill name indicates pattern concept'
                })

    # Issue 6: Check for truly redundant transitive dependencies
    for skill_id, skill_data in gk_skills.items():
        direct_deps = set(skill_data['dependencies'])
        if len(direct_deps) < 2:
            continue

        # For each pair of direct dependencies, check if one reaches the other
        for dep1 in direct_deps:
            for dep2 in direct_deps:
                if dep1 != dep2 and dep1 in gk_skills and dep2 in gk_skills:
                    # Check if dep1 can reach dep2 through its dependencies
                    if can_reach(dep1, dep2, gk_skills):
                        issues.append({
                            'type': 'REDUNDANT_TRANSITIVE',
                            'skill_id': skill_id,
                            'topic': skill_data['topic'],
                            'skill_name': skill_data['skill_name'],
                            'issue': f'Direct dependency on {dep2} is redundant (reachable via {dep1})',
                            'redundant_dep': dep2,
                            'via_dep': dep1,
                            'fix': f'Consider removing {dep2} as it\'s already implied by {dep1}'
                        })

    return issues, gk_skills

def can_reach(start, target, skills):
    """Check if start can reach target through dependencies."""
    if start not in skills:
        return False

    visited = set()
    to_check = [start]

    while to_check:
        current = to_check.pop(0)
        if current in visited:
            continue
        visited.add(current)

        if current not in skills:
            continue

        for dep in skills[current]['dependencies']:
            if dep == target:
                return True
            if dep in skills and dep not in visited:
                to_check.append(dep)

    return False

def generate_full_report(issues, gk_skills, all_skills):
    """Generate comprehensive report."""

    print("=" * 120)
    print("COMPREHENSIVE GRADE K DEPENDENCY ANALYSIS")
    print("=" * 120)
    print()

    print(f"Total Grade K Skills: {len(gk_skills)}")
    print(f"Total Skills in Database: {len(all_skills)}")
    print()

    # Categorize issues
    x2_violations = [i for i in issues if i['type'] == 'X2_VIOLATION']
    missing_cross = [i for i in issues if i['type'] == 'MISSING_CROSS_TOPIC']
    redundant = [i for i in issues if i['type'] == 'REDUNDANT_TRANSITIVE']
    circular = [i for i in issues if i['type'] == 'CIRCULAR']

    high_conf = [i for i in missing_cross if i.get('confidence') == 'HIGH']
    med_conf = [i for i in missing_cross if i.get('confidence') == 'MEDIUM']

    print("ISSUE SUMMARY")
    print("-" * 120)
    print(f"Total Issues Found: {len(issues)}")
    print(f"  - X-2 Rule Violations: {len(x2_violations)}")
    print(f"  - Circular Dependencies: {len(circular)}")
    print(f"  - Missing Cross-Topic Dependencies: {len(missing_cross)}")
    print(f"      * HIGH confidence: {len(high_conf)}")
    print(f"      * MEDIUM confidence: {len(med_conf)}")
    print(f"  - Redundant Transitive Dependencies: {len(redundant)}")
    print()

    # Print X-2 violations
    if x2_violations:
        print("=" * 120)
        print("X-2 RULE VIOLATIONS (GK skills depending on non-GK skills)")
        print("=" * 120)
        for i, issue in enumerate(x2_violations, 1):
            print(f"\n{i}. {issue['skill_id']} - {issue['skill_name']}")
            print(f"   Topic: {issue['topic']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Fix: {issue['fix']}")

    # Print missing cross-topic (HIGH confidence)
    if high_conf:
        print("\n" + "=" * 120)
        print("MISSING CROSS-TOPIC DEPENDENCIES (HIGH CONFIDENCE)")
        print("=" * 120)
        for i, issue in enumerate(high_conf, 1):
            print(f"\n{i}. {issue['skill_id']} - {issue['skill_name']}")
            print(f"   Topic: {issue['topic']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Suggested Addition: {issue['suggested_addition']}")
            print(f"   Rationale: {issue['rationale']}")
            print(f"   Current Dependencies: {', '.join(gk_skills[issue['skill_id']]['dependencies']) if gk_skills[issue['skill_id']]['dependencies'] else 'None'}")

    # Print missing cross-topic (MEDIUM confidence)
    if med_conf:
        print("\n" + "=" * 120)
        print("MISSING CROSS-TOPIC DEPENDENCIES (MEDIUM CONFIDENCE)")
        print("=" * 120)
        for i, issue in enumerate(med_conf, 1):
            print(f"\n{i}. {issue['skill_id']} - {issue['skill_name']}")
            print(f"   Topic: {issue['topic']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Suggested Addition: {issue['suggested_addition']}")
            print(f"   Rationale: {issue['rationale']}")
            print(f"   Current Dependencies: {', '.join(gk_skills[issue['skill_id']]['dependencies']) if gk_skills[issue['skill_id']]['dependencies'] else 'None'}")

    # Print redundant dependencies
    if redundant:
        print("\n" + "=" * 120)
        print("REDUNDANT TRANSITIVE DEPENDENCIES")
        print("=" * 120)
        for i, issue in enumerate(redundant, 1):
            print(f"\n{i}. {issue['skill_id']} - {issue['skill_name']}")
            print(f"   Topic: {issue['topic']}")
            print(f"   Issue: {issue['issue']}")
            print(f"   Fix: {issue['fix']}")

    # Detailed skill listing
    print("\n" + "=" * 120)
    print("ALL GRADE K SKILLS WITH DEPENDENCIES")
    print("=" * 120)

    by_topic = defaultdict(list)
    for sid, sdata in gk_skills.items():
        topic = get_topic_num(sid)
        by_topic[topic].append((sid, sdata))

    for topic in sorted(by_topic.keys()):
        print(f"\n{topic}: {len(by_topic[topic])} skills")
        for sid, sdata in sorted(by_topic[topic]):
            cross_topic = [d for d in sdata['dependencies'] if get_topic_num(d) != topic]
            dep_str = f"{len(sdata['dependencies'])} deps"
            if cross_topic:
                dep_str += f" ({len(cross_topic)} cross-topic: {', '.join(cross_topic)})"
            print(f"  {sid}: {sdata['skill_name'][:70]} - {dep_str}")

    # Topics without GK
    all_topics = [f"T{i:02d}" for i in range(1, 37)]
    missing_topics = [t for t in all_topics if t not in by_topic]
    if missing_topics:
        print(f"\n\nTopics without Grade K skills ({len(missing_topics)}):")
        print(f"  {', '.join(missing_topics)}")

if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing all skills...")
    all_skills = parse_skills_file(filepath)

    print("Performing comprehensive dependency analysis...")
    issues, gk_skills = comprehensive_dependency_analysis(all_skills)

    print("\nGenerating full report...\n")
    generate_full_report(issues, gk_skills, all_skills)
