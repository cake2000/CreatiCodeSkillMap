#!/usr/bin/env python3
"""
Extract and analyze all Grade 4 (G4) skills from allskills.md
"""

import re
from collections import defaultdict

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

def analyze_g4_skills(skills):
    """Analyze all G4 skills for dependency issues."""

    g4_skills = {sid: s for sid, s in skills.items() if get_grade_from_id(sid) == 'G4'}

    print("=" * 80)
    print("GRADE 4 (G4) SKILLS ANALYSIS REPORT")
    print("=" * 80)
    print(f"\nTotal G4 skills found: {len(g4_skills)}\n")

    # Group by topic
    by_topic = defaultdict(list)
    for skill_id, skill in g4_skills.items():
        by_topic[skill['topic']].append(skill)

    # Sort topics
    sorted_topics = sorted(by_topic.keys())

    all_issues = []

    for topic in sorted_topics:
        topic_skills = sorted(by_topic[topic], key=lambda x: x['id'])

        print("\n" + "=" * 80)
        print(f"TOPIC: {topic}")
        print("=" * 80)

        for skill in topic_skills:
            print(f"\n--- Skill ID: {skill['id']} ---")
            print(f"Title: {skill['skill']}")
            print(f"Dependencies ({len(skill['dependencies'])}): {', '.join(skill['dependencies']) if skill['dependencies'] else 'NONE'}")

            issues = []

            # Check 1: Out of order dependencies (G4 depending on G5+)
            for dep_id in skill['dependencies']:
                dep_grade = get_grade_from_id(dep_id)
                if dep_grade:
                    dep_grade_num = get_grade_number(dep_grade)
                    if dep_grade_num > 4:
                        issues.append({
                            'type': 'OUT_OF_ORDER',
                            'priority': 'HIGH',
                            'message': f"Depends on {dep_id} ({dep_grade}) - forward reference to higher grade"
                        })

            # Check 2: Dependency range violations (should be G4, G3, or G2 only)
            for dep_id in skill['dependencies']:
                dep_grade = get_grade_from_id(dep_id)
                if dep_grade:
                    dep_grade_num = get_grade_number(dep_grade)
                    if dep_grade_num < 2 and dep_grade_num >= 0:  # GK, G1
                        issues.append({
                            'type': 'RANGE_VIOLATION',
                            'priority': 'MEDIUM',
                            'message': f"Depends on {dep_id} ({dep_grade}) - too far back (should be G2-G4 only)"
                        })

            # Check 3: Same-topic same-grade dependencies
            same_topic_same_grade = []
            for dep_id in skill['dependencies']:
                if dep_id in skills:
                    dep_skill = skills[dep_id]
                    if dep_skill['topic'] == skill['topic'] and get_grade_from_id(dep_id) == 'G4':
                        same_topic_same_grade.append(dep_id)

            if same_topic_same_grade:
                issues.append({
                    'type': 'SAME_TOPIC_SAME_GRADE',
                    'priority': 'LOW',
                    'message': f"Lists same-topic same-grade dependencies: {', '.join(same_topic_same_grade)} (may be implicit)"
                })

            # Check 4: Transitive dependencies
            transitive_deps = []
            for dep_id in skill['dependencies']:
                if dep_id in skills:
                    dep_skill = skills[dep_id]
                    for indirect_dep in dep_skill['dependencies']:
                        if indirect_dep in skill['dependencies']:
                            transitive_deps.append(f"{dep_id} -> {indirect_dep}")

            if transitive_deps:
                issues.append({
                    'type': 'TRANSITIVE',
                    'priority': 'LOW',
                    'message': f"Possible transitive dependencies: {', '.join(transitive_deps)}"
                })

            # Check 5: Missing dependencies (basic check)
            if not skill['dependencies']:
                # Check if this is truly a foundational skill or should have deps
                # Look at skill name for clues
                skill_lower = skill['skill'].lower()
                if any(word in skill_lower for word in ['advanced', 'complex', 'combine', 'debug', 'optimize', 'refactor']):
                    issues.append({
                        'type': 'MISSING_DEPS',
                        'priority': 'MEDIUM',
                        'message': "Skill appears advanced but has no dependencies listed"
                    })

            # Check 6: Overly broad skills (heuristic check)
            skill_lower = skill['skill'].lower()
            if any(phrase in skill_lower for phrase in ['and', ' & ', 'multiple', 'various', 'all', 'everything']):
                if len(skill['skill']) > 80:
                    issues.append({
                        'type': 'OVERLY_BROAD',
                        'priority': 'LOW',
                        'message': "Skill title is very long and may cover too much"
                    })

            # Print issues
            if issues:
                print("\nISSUES FOUND:")
                for issue in issues:
                    print(f"  [{issue['priority']}] {issue['type']}: {issue['message']}")
                all_issues.append({'skill': skill, 'issues': issues})
            else:
                print("\nISSUES FOUND: None")

            # Recommendations
            if issues:
                print("\nRECOMMENDATIONS:")
                for issue in issues:
                    if issue['type'] == 'OUT_OF_ORDER':
                        print(f"  - CRITICAL: Remove forward reference or restructure skill to not depend on higher grades")
                    elif issue['type'] == 'RANGE_VIOLATION':
                        print(f"  - Remove dependency on {issue['message'].split()[2]} or add intermediate skills")
                    elif issue['type'] == 'SAME_TOPIC_SAME_GRADE':
                        print(f"  - Consider removing explicit same-topic same-grade deps (may be implicit)")
                    elif issue['type'] == 'TRANSITIVE':
                        print(f"  - Remove transitive dependencies to simplify")
                    elif issue['type'] == 'MISSING_DEPS':
                        print(f"  - Add prerequisite skills from G2-G3 as dependencies")
                    elif issue['type'] == 'OVERLY_BROAD':
                        print(f"  - Consider breaking down into multiple focused skills")

    # Summary statistics
    print("\n\n" + "=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)

    issue_counts = defaultdict(int)
    priority_counts = defaultdict(int)

    for item in all_issues:
        for issue in item['issues']:
            issue_counts[issue['type']] += 1
            priority_counts[issue['priority']] += 1

    print(f"\nTotal skills with issues: {len(all_issues)} out of {len(g4_skills)}")
    print(f"\nIssues by type:")
    for issue_type, count in sorted(issue_counts.items()):
        print(f"  {issue_type}: {count}")

    print(f"\nIssues by priority:")
    for priority, count in sorted(priority_counts.items(), reverse=True):
        print(f"  {priority}: {count}")

    # Critical issues
    critical_skills = []
    for item in all_issues:
        has_high = any(i['priority'] == 'HIGH' for i in item['issues'])
        if has_high:
            critical_skills.append(item['skill']['id'])

    if critical_skills:
        print(f"\n\nCRITICAL: {len(critical_skills)} skills with HIGH priority issues:")
        for skill_id in critical_skills:
            print(f"  - {skill_id}")

    print("\n" + "=" * 80)
    print("END OF REPORT")
    print("=" * 80)

if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = parse_allskills(filepath)
    print(f"Total skills parsed: {len(skills)}")
    analyze_g4_skills(skills)
