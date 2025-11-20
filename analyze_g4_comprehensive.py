#!/usr/bin/env python3
"""
Comprehensive G4 analysis including circular dependencies and missing dependencies
"""

import re
from collections import defaultdict, deque

def parse_allskills(filepath):
    """Parse the allskills.md file and extract all skills."""
    skills = {}
    current_skill = None

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries (looking for ID: pattern)
    entries = re.split(r'\n(?=ID: )', content)

    for entry in entries:
        if not entry.strip():
            continue

        # Extract ID
        id_match = re.search(r'^ID:\s*(\S+)', entry, re.MULTILINE)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic
        topic_match = re.search(r'^Topic:\s*(.+)$', entry, re.MULTILINE)
        topic = topic_match.group(1).strip() if topic_match else "Unknown"

        # Extract skill name
        skill_match = re.search(r'^Skill:\s*(.+)$', entry, re.MULTILINE)
        skill_name = skill_match.group(1).strip() if skill_match else "Unknown"

        # Extract description
        desc_match = re.search(r'^Description:\s*(.+?)(?=^Dependencies:|^ID:|$)', entry, re.MULTILINE | re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        dependencies = []
        deps_match = re.search(r'^Dependencies:\s*(.+?)(?=^ID:|$)', entry, re.MULTILINE | re.DOTALL)
        if deps_match:
            deps_text = deps_match.group(1)
            # Find all dependency IDs (format: * ID: skill name)
            dep_ids = re.findall(r'\*\s*(\S+):', deps_text)
            dependencies = dep_ids

        skills[skill_id] = {
            'id': skill_id,
            'topic': topic,
            'skill': skill_name,
            'description': description,
            'dependencies': dependencies
        }

    return skills

def get_grade_from_id(skill_id):
    """Extract grade from skill ID (e.g., T01.G4.01 -> G4)"""
    match = re.search(r'\.(G\d+|GK)\.', skill_id)
    if match:
        return match.group(1)
    return None

def get_grade_number(grade):
    """Convert grade to number for comparison (GK=0, G1=1, etc.)"""
    if grade == 'GK':
        return 0
    match = re.match(r'G(\d+)', grade)
    if match:
        return int(match.group(1))
    return -1

def get_topic_from_id(skill_id):
    """Extract topic code from skill ID (e.g., T01.G4.01 -> T01)"""
    match = re.match(r'(T\d+)\.', skill_id)
    if match:
        return match.group(1)
    return None

def find_circular_dependencies(skills, g4_skills):
    """Find circular dependencies among G4 skills."""
    circular_deps = []

    def has_path(start, end, visited=None):
        """Check if there's a path from start to end."""
        if visited is None:
            visited = set()
        if start == end:
            return True
        if start in visited:
            return False
        visited.add(start)

        if start not in skills:
            return False

        for dep in skills[start]['dependencies']:
            if has_path(dep, end, visited):
                return True
        return False

    for skill_id in g4_skills:
        for dep_id in skills[skill_id]['dependencies']:
            # Check if dep_id has a path back to skill_id
            if has_path(dep_id, skill_id):
                circular_deps.append((skill_id, dep_id))

    return circular_deps

def get_all_transitive_deps(skill_id, skills, visited=None):
    """Get all transitive dependencies of a skill."""
    if visited is None:
        visited = set()

    if skill_id in visited or skill_id not in skills:
        return set()

    visited.add(skill_id)
    all_deps = set(skills[skill_id]['dependencies'])

    for dep in skills[skill_id]['dependencies']:
        all_deps.update(get_all_transitive_deps(dep, skills, visited))

    return all_deps

def analyze_missing_dependencies(skill, skills, g4_skills):
    """Analyze if a skill is missing obvious dependencies."""
    issues = []

    # Check if skill depends directly on deps of deps
    for dep_id in skill['dependencies']:
        if dep_id not in skills:
            continue
        dep_skill = skills[dep_id]

        # Get topic of current skill
        skill_topic = get_topic_from_id(skill['id'])
        dep_topic = get_topic_from_id(dep_id)

        # If depending on a different topic's skill, check if we should also depend on its deps
        if skill_topic != dep_topic:
            for indirect_dep in dep_skill['dependencies']:
                indirect_topic = get_topic_from_id(indirect_dep)
                # If the indirect dep is from same topic as current skill, might be missing
                if indirect_topic == skill_topic and indirect_dep not in skill['dependencies']:
                    indirect_grade = get_grade_from_id(indirect_dep)
                    if indirect_grade and get_grade_number(indirect_grade) < 4:
                        issues.append({
                            'type': 'POSSIBLE_MISSING_DEP',
                            'priority': 'LOW',
                            'message': f"Depends on {dep_id} which depends on {indirect_dep} (same topic as this skill)"
                        })

    # Check for skills with complex names but few dependencies
    skill_lower = skill['skill'].lower()
    complexity_keywords = ['complex', 'advanced', 'multi', 'nested', 'combine', 'integrate']
    if any(kw in skill_lower for kw in complexity_keywords) and len(skill['dependencies']) < 2:
        issues.append({
            'type': 'POSSIBLY_UNDERDEFINED',
            'priority': 'LOW',
            'message': f"Skill appears complex but has only {len(skill['dependencies'])} dependency(ies)"
        })

    return issues

def analyze_g4_comprehensive(skills):
    """Comprehensive analysis of all G4 skills."""

    g4_skills = {sid: s for sid, s in skills.items() if get_grade_from_id(sid) == 'G4'}

    print("=" * 80)
    print("COMPREHENSIVE GRADE 4 ANALYSIS REPORT")
    print("=" * 80)
    print(f"\nTotal G4 skills: {len(g4_skills)}")

    # Find circular dependencies
    print("\n" + "=" * 80)
    print("CIRCULAR DEPENDENCY CHECK")
    print("=" * 80)

    circular_deps = find_circular_dependencies(skills, g4_skills.keys())
    if circular_deps:
        print(f"\nFound {len(circular_deps)} potential circular dependencies:")
        for skill_id, dep_id in circular_deps:
            print(f"  {skill_id} <-> {dep_id}")
    else:
        print("\nNo circular dependencies found among G4 skills.")

    # Group by topic for detailed analysis
    by_topic = defaultdict(list)
    for skill_id, skill in g4_skills.items():
        by_topic[skill['topic']].append(skill)

    sorted_topics = sorted(by_topic.keys())

    all_issues = []

    print("\n" + "=" * 80)
    print("DETAILED SKILL-BY-SKILL ANALYSIS")
    print("=" * 80)

    for topic in sorted_topics:
        topic_skills = sorted(by_topic[topic], key=lambda x: x['id'])

        print(f"\n{'=' * 80}")
        print(f"TOPIC: {topic}")
        print('=' * 80)

        for skill in topic_skills:
            print(f"\nSkill ID: {skill['id']}")
            print(f"Title: {skill['skill']}")
            print(f"Dependencies: {len(skill['dependencies'])}")
            if skill['dependencies']:
                for dep in skill['dependencies']:
                    dep_grade = get_grade_from_id(dep)
                    print(f"  - {dep} ({dep_grade})")
            else:
                print("  - NONE")

            issues = []

            # Check 1: Out of order (forward references)
            for dep_id in skill['dependencies']:
                dep_grade = get_grade_from_id(dep_id)
                if dep_grade:
                    dep_grade_num = get_grade_number(dep_grade)
                    if dep_grade_num > 4:
                        issues.append({
                            'type': 'OUT_OF_ORDER',
                            'priority': 'HIGH',
                            'message': f"Forward reference to {dep_id} ({dep_grade})"
                        })

            # Check 2: Range violations (too far back)
            for dep_id in skill['dependencies']:
                dep_grade = get_grade_from_id(dep_id)
                if dep_grade:
                    dep_grade_num = get_grade_number(dep_grade)
                    if dep_grade_num < 2 and dep_grade_num >= 0:
                        issues.append({
                            'type': 'RANGE_VIOLATION',
                            'priority': 'MEDIUM',
                            'message': f"Depends on {dep_id} ({dep_grade}) - should be G2-G4 only"
                        })

            # Check 3: Same topic, same grade
            skill_topic = get_topic_from_id(skill['id'])
            for dep_id in skill['dependencies']:
                dep_topic = get_topic_from_id(dep_id)
                dep_grade = get_grade_from_id(dep_id)
                if dep_topic == skill_topic and dep_grade == 'G4':
                    issues.append({
                        'type': 'SAME_TOPIC_SAME_GRADE',
                        'priority': 'LOW',
                        'message': f"Lists {dep_id} (same topic, same grade - may be implicit)"
                    })

            # Check 4: Transitive dependencies
            transitive = []
            for dep_id in skill['dependencies']:
                if dep_id not in skills:
                    continue
                for indirect in skills[dep_id]['dependencies']:
                    if indirect in skill['dependencies']:
                        transitive.append(f"{dep_id} -> {indirect}")

            if transitive:
                issues.append({
                    'type': 'TRANSITIVE',
                    'priority': 'LOW',
                    'message': f"Direct listing of transitive deps: {', '.join(transitive)}"
                })

            # Check 5: Missing dependencies
            missing_issues = analyze_missing_dependencies(skill, skills, g4_skills)
            issues.extend(missing_issues)

            # Check 6: No dependencies but advanced skill
            if not skill['dependencies']:
                skill_lower = skill['skill'].lower()
                if any(w in skill_lower for w in ['advanced', 'complex', 'debug', 'analyze', 'optimize']):
                    issues.append({
                        'type': 'MISSING_DEPS',
                        'priority': 'MEDIUM',
                        'message': "Advanced skill with no dependencies"
                    })

            if issues:
                print("\nISSUES:")
                for issue in issues:
                    print(f"  [{issue['priority']}] {issue['type']}: {issue['message']}")
                all_issues.append({'skill': skill, 'issues': issues})
            else:
                print("\nISSUES: None")

    # Summary
    print("\n\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    issue_counts = defaultdict(int)
    priority_counts = defaultdict(int)

    for item in all_issues:
        for issue in item['issues']:
            issue_counts[issue['type']] += 1
            priority_counts[issue['priority']] += 1

    print(f"\nSkills with issues: {len(all_issues)} / {len(g4_skills)}")
    print(f"Skills without issues: {len(g4_skills) - len(all_issues)}")

    print("\nIssues by type:")
    for itype in sorted(issue_counts.keys()):
        print(f"  {itype}: {issue_counts[itype]}")

    print("\nIssues by priority:")
    for priority in ['HIGH', 'MEDIUM', 'LOW']:
        if priority in priority_counts:
            print(f"  {priority}: {priority_counts[priority]}")

    # High priority issues
    high_priority_skills = []
    for item in all_issues:
        if any(i['priority'] == 'HIGH' for i in item['issues']):
            high_priority_skills.append(item['skill']['id'])

    if high_priority_skills:
        print(f"\n\nCRITICAL: {len(high_priority_skills)} skills with HIGH priority issues:")
        for sid in high_priority_skills:
            print(f"  {sid}")
    else:
        print("\n\nNo HIGH priority issues found.")

    print("\n" + "=" * 80)
    print("END OF REPORT")
    print("=" * 80)

if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = parse_allskills(filepath)
    analyze_g4_comprehensive(skills)
