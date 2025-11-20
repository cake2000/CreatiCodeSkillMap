#!/usr/bin/env python3
"""Deep analysis of G1 skills with comprehensive dependency checking"""

import re
from collections import defaultdict

def extract_all_skills(filepath):
    """Extract ALL skills (K and G1) to check dependencies"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match all skill blocks
    pattern = r'ID: (T\d+\.(?:GK|G\d+)\.\d+)\n(.*?)(?=\nID: T\d+\.G\d+\.\d+|\n# T\d+:|$)'

    skills = {}
    for match in re.finditer(pattern, content, re.DOTALL):
        skill_id = match.group(1)
        skill_content = match.group(2)

        # Extract topic
        topic_match = re.search(r'Topic: (.+)', skill_content)
        topic = topic_match.group(1) if topic_match else "NO TOPIC"

        # Extract skill title
        skill_match = re.search(r'Skill: (.+)', skill_content)
        title = skill_match.group(1) if skill_match else "NO TITLE"

        # Extract description for breadth analysis
        desc_match = re.search(r'Description: (.+)', skill_content)
        description = desc_match.group(1) if desc_match else ""

        # Extract dependencies
        deps_section = re.search(r'Dependencies:\s*\n((?:\* .*\n)*)', skill_content)
        dependencies = []
        dep_details = []
        if deps_section:
            deps_text = deps_section.group(1)
            for dep_line in deps_text.split('\n'):
                if dep_line.strip():
                    dep_match = re.search(r'(T\d+\.(?:GK|G\d+)\.\d+): (.+)', dep_line)
                    if dep_match:
                        dependencies.append(dep_match.group(1))
                        dep_details.append({
                            'id': dep_match.group(1),
                            'title': dep_match.group(2)
                        })

        skills[skill_id] = {
            'id': skill_id,
            'topic': topic,
            'title': title,
            'description': description,
            'dependencies': dependencies,
            'dep_details': dep_details
        }

    return skills

def deep_analyze_g1(all_skills):
    """Perform deep analysis on G1 skills"""

    issues = {
        'high': [],
        'medium': [],
        'low': []
    }

    # Get only G1 skills
    g1_skills = {k: v for k, v in all_skills.items() if '.G1.' in k}

    for skill_id, skill in g1_skills.items():
        topic_id = skill_id.split('.')[0]  # e.g., T01

        # === HIGH PRIORITY CHECKS ===

        # 1. Check for out-of-order dependencies (G1 depending on G2+)
        for dep_id in skill['dependencies']:
            dep_grade = dep_id.split('.')[1]
            if dep_grade.startswith('G') and dep_grade not in ['GK', 'G1']:
                issues['high'].append({
                    'skill': skill_id,
                    'title': skill['title'],
                    'issue': 'OUT_OF_ORDER',
                    'detail': f"G1 skill depends on {dep_grade} skill: {dep_id}",
                    'dependency': dep_id
                })

        # 2. Check for cross-topic K dependencies that seem weak
        # Pattern: Many skills from various topics all depend on same generic T01.GK skill
        k_deps = [d for d in skill['dependencies'] if '.GK.' in d]
        for k_dep in k_deps:
            k_topic = k_dep.split('.')[0]
            if k_topic != topic_id:
                # This is a cross-topic dependency
                # Check if it's one of the overused T01.GK skills
                if k_dep in ['T01.GK.01', 'T01.GK.03'] and topic_id not in ['T01', 'T02', 'T03']:
                    issues['medium'].append({
                        'skill': skill_id,
                        'title': skill['title'],
                        'issue': 'WEAK_CROSS_TOPIC_DEPENDENCY',
                        'detail': f"Topic {topic_id} skill depends on generic T01.GK skill: {k_dep} ('{all_skills.get(k_dep, {}).get('title', 'unknown')}'). Consider if there's a more relevant prerequisite from the same topic.",
                        'dependency': k_dep
                    })

        # 3. Check for skills that might be missing G1 prerequisites from same topic
        # If a skill is G1.04 or higher, it might need G1.01 or G1.02 from same topic
        skill_num = int(skill_id.split('.')[-1])
        if skill_num >= 4:
            # Check if it has ANY same-topic G1 dependency
            same_topic_g1_deps = [d for d in skill['dependencies'] if d.startswith(topic_id) and '.G1.' in d]
            if not same_topic_g1_deps:
                # This is suspicious - a later G1 skill with no earlier G1 prerequisites
                issues['medium'].append({
                    'skill': skill_id,
                    'title': skill['title'],
                    'issue': 'MISSING_SAME_TOPIC_PREREQ',
                    'detail': f"Skill G1.{skill_num:02d} has no same-topic G1 prerequisites. Should it depend on {topic_id}.G1.01 or other earlier skills in this topic?"
                })

        # 4. Check for skills that are too broad
        broad_keywords = ['understand', 'learn', 'know about', 'explore', 'introduction to']
        title_lower = skill['title'].lower()
        desc_lower = skill['description'].lower()

        for keyword in broad_keywords:
            if keyword in title_lower or keyword in desc_lower:
                issues['medium'].append({
                    'skill': skill_id,
                    'title': skill['title'],
                    'issue': 'POSSIBLY_TOO_BROAD',
                    'detail': f"Title/description contains '{keyword}' which may indicate the skill is too broad and should be broken down."
                })
                break

        # 5. Check for circular dependencies (A depends on B, B depends on A)
        for dep_id in skill['dependencies']:
            if dep_id in all_skills:
                dep_deps = all_skills[dep_id]['dependencies']
                if skill_id in dep_deps:
                    issues['high'].append({
                        'skill': skill_id,
                        'title': skill['title'],
                        'issue': 'CIRCULAR_DEPENDENCY',
                        'detail': f"Circular: {skill_id} depends on {dep_id}, and {dep_id} depends on {skill_id}",
                        'dependency': dep_id
                    })

        # 6. Check for transitive dependencies
        # If A depends on B and B depends on C, then A shouldn't also depend on C
        for dep_id in skill['dependencies']:
            if dep_id in all_skills:
                dep_deps = all_skills[dep_id]['dependencies']
                # Check if any of dep's dependencies are also in our dependencies
                transitive = set(dep_deps) & set(skill['dependencies'])
                if transitive:
                    for trans_dep in transitive:
                        issues['low'].append({
                            'skill': skill_id,
                            'title': skill['title'],
                            'issue': 'TRANSITIVE_DEPENDENCY',
                            'detail': f"{skill_id} depends on both {dep_id} and {trans_dep}, but {dep_id} already depends on {trans_dep}. Remove {trans_dep} from {skill_id}'s dependencies.",
                            'dependency': trans_dep,
                            'via': dep_id
                        })

        # 7. Check for non-existent dependencies
        for dep_id in skill['dependencies']:
            if dep_id not in all_skills:
                issues['high'].append({
                    'skill': skill_id,
                    'title': skill['title'],
                    'issue': 'MISSING_DEPENDENCY',
                    'detail': f"Depends on {dep_id} which doesn't exist in the skill map!",
                    'dependency': dep_id
                })

    return g1_skills, issues

def generate_deep_report(g1_skills, issues, all_skills):
    """Generate comprehensive report"""

    print("="*80)
    print("DEEP G1 SKILLS ANALYSIS REPORT")
    print("="*80)
    print()

    print(f"Total G1 Skills: {len(g1_skills)}")
    print(f"Total Skills in Database: {len(all_skills)}")
    print()

    # Topic breakdown
    by_topic = defaultdict(list)
    for skill in g1_skills.values():
        by_topic[skill['topic']].append(skill)

    print(f"Topics with G1 Skills: {len(by_topic)}")
    print()

    # === CRITICAL ISSUES ===
    print("="*80)
    print("CRITICAL ISSUES (MUST FIX IMMEDIATELY)")
    print("="*80)
    print()

    if issues['high']:
        print(f"Found {len(issues['high'])} critical issues:\n")

        # Group by issue type
        by_type = defaultdict(list)
        for issue in issues['high']:
            by_type[issue['issue']].append(issue)

        for issue_type, issue_list in sorted(by_type.items()):
            print(f"\n{issue_type} ({len(issue_list)} issues):")
            print("-" * 80)
            for i, issue in enumerate(issue_list, 1):
                print(f"{i}. {issue['skill']}: {issue['title']}")
                print(f"   {issue['detail']}")
                print()
    else:
        print("No critical issues found!")
        print()

    # === IMPORTANT ISSUES ===
    print("="*80)
    print("IMPORTANT ISSUES (SHOULD FIX)")
    print("="*80)
    print()

    if issues['medium']:
        print(f"Found {len(issues['medium'])} important issues:\n")

        # Group by issue type
        by_type = defaultdict(list)
        for issue in issues['medium']:
            by_type[issue['issue']].append(issue)

        for issue_type, issue_list in sorted(by_type.items()):
            print(f"\n{issue_type} ({len(issue_list)} issues):")
            print("-" * 80)
            for i, issue in enumerate(issue_list, 1):
                print(f"{i}. {issue['skill']}: {issue['title']}")
                print(f"   {issue['detail']}")
                print()
    else:
        print("No important issues found!")
        print()

    # === MINOR ISSUES ===
    print("="*80)
    print("MINOR ISSUES (OPTIONAL IMPROVEMENTS)")
    print("="*80)
    print()

    if issues['low']:
        print(f"Found {len(issues['low'])} minor issues:\n")

        # Group by issue type
        by_type = defaultdict(list)
        for issue in issues['low']:
            by_type[issue['issue']].append(issue)

        for issue_type, issue_list in sorted(by_type.items()):
            print(f"\n{issue_type} ({len(issue_list)} issues):")
            print("-" * 80)
            for i, issue in enumerate(issue_list, 1):
                print(f"{i}. {issue['skill']}: {issue['title']}")
                print(f"   {issue['detail']}")
                if 'via' in issue:
                    print(f"   (via {issue['via']})")
                print()
    else:
        print("No minor issues found!")
        print()

    # === DEPENDENCY PATTERNS ===
    print("="*80)
    print("DEPENDENCY PATTERN ANALYSIS")
    print("="*80)
    print()

    # Most referenced K dependencies
    k_dep_count = defaultdict(int)
    for skill in g1_skills.values():
        for dep in skill['dependencies']:
            if '.GK.' in dep:
                k_dep_count[dep] += 1

    print("Most frequently used K-level prerequisites:")
    print("-" * 80)
    for dep_id, count in sorted(k_dep_count.items(), key=lambda x: x[1], reverse=True)[:10]:
        dep_title = all_skills.get(dep_id, {}).get('title', 'UNKNOWN')
        print(f"{dep_id}: {dep_title}")
        print(f"  Used by {count} G1 skills")
        print()

    # Topics with most cross-topic dependencies
    print("\nCross-topic K dependencies by topic:")
    print("-" * 80)
    cross_topic = defaultdict(list)
    for skill in g1_skills.values():
        topic_id = skill['id'].split('.')[0]
        for dep in skill['dependencies']:
            if '.GK.' in dep:
                dep_topic = dep.split('.')[0]
                if dep_topic != topic_id:
                    cross_topic[topic_id].append((skill['id'], dep))

    for topic_id in sorted(cross_topic.keys()):
        deps = cross_topic[topic_id]
        print(f"{topic_id}: {len(deps)} cross-topic K dependencies")
        # Show unique dependencies
        unique_deps = set(d[1] for d in deps)
        for dep in sorted(unique_deps):
            count = sum(1 for _, d in deps if d == dep)
            dep_title = all_skills.get(dep, {}).get('title', 'UNKNOWN')
            print(f"  - {dep} ({count}x): {dep_title}")
        print()

    # === SUMMARY ===
    print("="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total G1 Skills: {len(g1_skills)}")
    print(f"Critical Issues: {len(issues['high'])}")
    print(f"Important Issues: {len(issues['medium'])}")
    print(f"Minor Issues: {len(issues['low'])}")
    print()
    print("PRIORITY RECOMMENDATIONS:")
    print("1. Fix all CRITICAL issues immediately")
    print("2. Review IMPORTANT issues - especially weak cross-topic dependencies")
    print("3. Consider MINOR issues for optimization")
    print()

if __name__ == '__main__':
    all_skills = extract_all_skills('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')
    g1_skills, issues = deep_analyze_g1(all_skills)
    generate_deep_report(g1_skills, issues, all_skills)
