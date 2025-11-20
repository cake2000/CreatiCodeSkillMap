#!/usr/bin/env python3
"""Comprehensive analysis of all G1 skills"""

import re
from collections import defaultdict

def extract_g1_skills(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match skill blocks
    pattern = r'ID: (T\d+\.G1\.\d+)\n(.*?)(?=\nID: T\d+\.G\d+\.\d+|\n# T\d+:|$)'

    skills = []
    for match in re.finditer(pattern, content, re.DOTALL):
        skill_id = match.group(1)
        skill_content = match.group(2)

        # Extract topic
        topic_match = re.search(r'Topic: (.+)', skill_content)
        topic = topic_match.group(1) if topic_match else "NO TOPIC"

        # Extract skill title
        skill_match = re.search(r'Skill: (.+)', skill_content)
        title = skill_match.group(1) if skill_match else "NO TITLE"

        # Extract dependencies - they're listed as bullet points
        deps_section = re.search(r'Dependencies:\s*\n((?:\* .*\n)*)', skill_content)
        dependencies = []
        dep_details = []
        if deps_section:
            deps_text = deps_section.group(1)
            # Extract skill IDs from dependency lines
            for dep_line in deps_text.split('\n'):
                if dep_line.strip():
                    dep_match = re.search(r'(T\d+\.(?:GK|G\d+)\.\d+): (.+)', dep_line)
                    if dep_match:
                        dependencies.append(dep_match.group(1))
                        dep_details.append({
                            'id': dep_match.group(1),
                            'title': dep_match.group(2)
                        })

        skills.append({
            'id': skill_id,
            'topic': topic,
            'title': title,
            'dependencies': dependencies,
            'dep_details': dep_details
        })

    return skills

def analyze_dependencies(skills):
    """Analyze all dependency issues"""

    issues = {
        'high': [],  # Critical issues
        'medium': [],  # Should fix
        'low': []  # Optional improvements
    }

    # Build skill lookup
    skill_map = {s['id']: s for s in skills}

    # Build all skills map (we need to check if dependencies exist)
    all_skill_ids = set(skill_map.keys())

    for skill in skills:
        skill_id = skill['id']
        topic = skill['id'].split('.')[0]  # Extract topic (T01, T02, etc.)
        grade = 'G1'

        # Check each dependency
        for dep_id in skill['dependencies']:
            dep_grade = dep_id.split('.')[1]  # Extract grade (GK, G1, G2, etc.)
            dep_topic = dep_id.split('.')[0]

            # Issue 1: Out of order - G1 depending on G2+
            if dep_grade.startswith('G') and dep_grade not in ['GK', 'G1']:
                grade_num = int(dep_grade[1:])
                issues['high'].append({
                    'skill': skill_id,
                    'title': skill['title'],
                    'issue': 'OUT_OF_ORDER',
                    'detail': f"G1 skill depends on {dep_grade} skill: {dep_id}",
                    'dependency': dep_id
                })

            # Issue 2: Dependencies should be from G1 or GK only
            if dep_grade not in ['GK', 'G1']:
                issues['high'].append({
                    'skill': skill_id,
                    'title': skill['title'],
                    'issue': 'INVALID_GRADE',
                    'detail': f"G1 skill should only depend on GK or G1, not {dep_grade}: {dep_id}",
                    'dependency': dep_id
                })

        # Check if skill is too broad (heuristic: very generic titles)
        broad_keywords = ['understand', 'learn', 'know', 'explore', 'introduction']
        if any(keyword in skill['title'].lower() for keyword in broad_keywords):
            issues['medium'].append({
                'skill': skill_id,
                'title': skill['title'],
                'issue': 'POSSIBLY_TOO_BROAD',
                'detail': f"Skill title contains generic keywords that may indicate it's too broad"
            })

        # Check for dependencies within same topic/grade (might be transitive)
        same_topic_deps = [d for d in skill['dependencies'] if d.startswith(topic) and '.G1.' in d]
        if len(same_topic_deps) > 0:
            # Get the skill numbers
            skill_num = int(skill_id.split('.')[-1])
            for dep in same_topic_deps:
                dep_num = int(dep.split('.')[-1])
                # If depending on earlier skill in same topic, it might be unnecessary
                if skill_num - dep_num > 1:
                    issues['low'].append({
                        'skill': skill_id,
                        'title': skill['title'],
                        'issue': 'POSSIBLE_TRANSITIVE',
                        'detail': f"Depends on {dep} which is 2+ skills earlier in same topic - may be transitive",
                        'dependency': dep
                    })

    return issues

def generate_report(skills, issues):
    """Generate comprehensive report"""

    print("="*80)
    print("COMPREHENSIVE G1 SKILLS ANALYSIS REPORT")
    print("="*80)
    print()

    print(f"Total G1 Skills Found: {len(skills)}")
    print()

    # Group skills by topic
    by_topic = defaultdict(list)
    for skill in skills:
        topic = skill['topic']
        by_topic[topic].append(skill)

    print(f"Topics Covered: {len(by_topic)}")
    for topic in sorted(by_topic.keys()):
        print(f"  - {topic}: {len(by_topic[topic])} skills")
    print()

    print("="*80)
    print("SECTION 1: ALL G1 SKILLS WITH DEPENDENCIES")
    print("="*80)
    print()

    for skill in sorted(skills, key=lambda x: x['id']):
        print(f"{skill['id']}: {skill['title']}")
        print(f"  Topic: {skill['topic']}")
        if skill['dependencies']:
            print(f"  Dependencies:")
            for dep_detail in skill['dep_details']:
                print(f"    - {dep_detail['id']}: {dep_detail['title']}")
        else:
            print(f"  Dependencies: None")
        print()

    print("="*80)
    print("SECTION 2: HIGH PRIORITY ISSUES (MUST FIX)")
    print("="*80)
    print()

    if issues['high']:
        print(f"Found {len(issues['high'])} high priority issues:\n")
        for i, issue in enumerate(issues['high'], 1):
            print(f"{i}. {issue['skill']}: {issue['title']}")
            print(f"   Issue Type: {issue['issue']}")
            print(f"   Detail: {issue['detail']}")
            if 'dependency' in issue:
                print(f"   Problematic Dependency: {issue['dependency']}")
            print()
    else:
        print("No high priority issues found!")
        print()

    print("="*80)
    print("SECTION 3: MEDIUM PRIORITY ISSUES (SHOULD FIX)")
    print("="*80)
    print()

    if issues['medium']:
        print(f"Found {len(issues['medium'])} medium priority issues:\n")
        for i, issue in enumerate(issues['medium'], 1):
            print(f"{i}. {issue['skill']}: {issue['title']}")
            print(f"   Issue Type: {issue['issue']}")
            print(f"   Detail: {issue['detail']}")
            print()
    else:
        print("No medium priority issues found!")
        print()

    print("="*80)
    print("SECTION 4: LOW PRIORITY ISSUES (OPTIONAL)")
    print("="*80)
    print()

    if issues['low']:
        print(f"Found {len(issues['low'])} low priority issues:\n")
        for i, issue in enumerate(issues['low'], 1):
            print(f"{i}. {issue['skill']}: {issue['title']}")
            print(f"   Issue Type: {issue['issue']}")
            print(f"   Detail: {issue['detail']}")
            if 'dependency' in issue:
                print(f"   Dependency: {issue['dependency']}")
            print()
    else:
        print("No low priority issues found!")
        print()

    print("="*80)
    print("SECTION 5: SKILLS REQUIRING CLARIFICATION")
    print("="*80)
    print()

    # Check for skills with no dependencies at all
    no_deps = [s for s in skills if not s['dependencies']]
    print(f"Skills with NO dependencies: {len(no_deps)}")
    print("(These are entry-level G1 skills - verify they truly need no prerequisites)")
    print()

    # Group by topic
    no_deps_by_topic = defaultdict(list)
    for skill in no_deps:
        no_deps_by_topic[skill['topic']].append(skill)

    for topic in sorted(no_deps_by_topic.keys()):
        print(f"\n{topic}:")
        for skill in no_deps_by_topic[topic]:
            print(f"  - {skill['id']}: {skill['title']}")

    print()
    print("="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total Skills: {len(skills)}")
    print(f"High Priority Issues: {len(issues['high'])}")
    print(f"Medium Priority Issues: {len(issues['medium'])}")
    print(f"Low Priority Issues: {len(issues['low'])}")
    print(f"Skills with no dependencies: {len(no_deps)}")
    print()

if __name__ == '__main__':
    skills = extract_g1_skills('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    issues = analyze_dependencies(skills)
    generate_report(skills, issues)
