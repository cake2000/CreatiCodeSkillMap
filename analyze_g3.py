#!/usr/bin/env python3
"""
Extract and analyze all Grade 3 skills from allskills.md
"""

import re
from collections import defaultdict

def parse_skills(filepath):
    """Parse the markdown file and extract all skills with their metadata."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill headers (lines starting with "ID: ")
    skill_blocks = re.split(r'\n(?=ID: )', content)

    skills = []
    for block in skill_blocks:
        if not block.strip():
            continue

        # Extract ID
        id_match = re.search(r'^ID: (.+)$', block, re.MULTILINE)
        if not id_match:
            continue
        skill_id = id_match.group(1).strip()

        # Extract Title
        title_match = re.search(r'^Title: (.+)$', block, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else ""

        # Extract Description
        desc_match = re.search(r'^Description: (.+?)(?=\n\n|\nDependencies:|\Z)', block, re.MULTILINE | re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract Dependencies
        deps = []
        deps_section = re.search(r'Dependencies:\s*\n((?:\* .+\n?)+)', block, re.MULTILINE)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'\* ([A-Z0-9.]+):', line)
                if dep_match:
                    deps.append(dep_match.group(1))

        skills.append({
            'id': skill_id,
            'title': title,
            'description': description,
            'dependencies': deps,
            'raw_block': block
        })

    return skills

def extract_grade(skill_id):
    """Extract grade from skill ID (e.g., 'G3' from 'T01.G3.01')."""
    match = re.search(r'\.(G\d+|K)\.', skill_id)
    return match.group(1) if match else None

def grade_to_num(grade):
    """Convert grade string to number for comparison."""
    if grade == 'K':
        return 0
    match = re.match(r'G(\d+)', grade)
    return int(match.group(1)) if match else -1

def analyze_dependencies(skill, all_skills_dict):
    """Analyze dependencies for a single skill."""
    issues = []
    skill_id = skill['id']
    skill_grade = extract_grade(skill_id)
    skill_grade_num = grade_to_num(skill_grade)

    # Get topic from skill ID (e.g., 'T01' from 'T01.G3.01')
    topic_match = re.search(r'^([A-Z0-9]+)\.', skill_id)
    topic = topic_match.group(1) if topic_match else None

    for dep_id in skill['dependencies']:
        dep_grade = extract_grade(dep_id)
        dep_grade_num = grade_to_num(dep_grade)

        # Get dependency topic
        dep_topic_match = re.search(r'^([A-Z0-9]+)\.', dep_id)
        dep_topic = dep_topic_match.group(1) if dep_topic_match else None

        # Rule 1: Dependencies should be at grade X, X-1, or X-2
        if dep_grade_num > skill_grade_num:
            issues.append({
                'priority': 'HIGH',
                'type': 'OUT_OF_ORDER',
                'skill_id': skill_id,
                'title': skill['title'],
                'problem': f"Depends on {dep_id} which is grade {dep_grade} (higher than {skill_grade})",
                'recommendation': f"Remove dependency on {dep_id} or move this skill to a higher grade"
            })
        elif skill_grade_num - dep_grade_num > 2:
            issues.append({
                'priority': 'MEDIUM',
                'type': 'TOO_EARLY_GRADE',
                'skill_id': skill_id,
                'title': skill['title'],
                'problem': f"Depends on {dep_id} (grade {dep_grade}), which is more than 2 grades below {skill_grade}",
                'recommendation': f"Consider if {dep_id} is really needed or if there's an intermediate skill"
            })

        # Rule 2: Check for same topic, same grade dependencies (unnecessary)
        if topic == dep_topic and dep_grade == skill_grade:
            issues.append({
                'priority': 'LOW',
                'type': 'SAME_TOPIC_GRADE',
                'skill_id': skill_id,
                'title': skill['title'],
                'problem': f"Depends on {dep_id} which is same topic and same grade (assumed to be learned in order)",
                'recommendation': f"Consider removing {dep_id} dependency as it's assumed"
            })

    # Check for transitive dependencies
    direct_deps = set(skill['dependencies'])
    for dep_id in skill['dependencies']:
        if dep_id in all_skills_dict:
            dep_skill = all_skills_dict[dep_id]
            second_level_deps = set(dep_skill['dependencies'])

            # Find common dependencies (potential transitive)
            transitive = direct_deps.intersection(second_level_deps)
            for trans_id in transitive:
                issues.append({
                    'priority': 'MEDIUM',
                    'type': 'TRANSITIVE',
                    'skill_id': skill_id,
                    'title': skill['title'],
                    'problem': f"Depends on both {trans_id} and {dep_id}, but {dep_id} already depends on {trans_id}",
                    'recommendation': f"Remove direct dependency on {trans_id} (transitive through {dep_id})"
                })

    return issues

def detect_circular_dependencies(skills):
    """Detect circular dependencies using DFS."""
    issues = []
    skills_dict = {s['id']: s for s in skills}

    def has_path(start, end, visited=None):
        """Check if there's a path from start to end."""
        if visited is None:
            visited = set()
        if start == end:
            return True
        if start in visited or start not in skills_dict:
            return False
        visited.add(start)
        for dep in skills_dict[start]['dependencies']:
            if has_path(dep, end, visited):
                return True
        return False

    for skill in skills:
        skill_id = skill['id']
        for dep_id in skill['dependencies']:
            # Check if dep also depends on this skill (circular)
            if has_path(dep_id, skill_id):
                issues.append({
                    'priority': 'HIGH',
                    'type': 'CIRCULAR',
                    'skill_id': skill_id,
                    'title': skill['title'],
                    'problem': f"Circular dependency with {dep_id}",
                    'recommendation': f"Break the circular dependency between {skill_id} and {dep_id}"
                })

    return issues

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills file...")
    all_skills = parse_skills(filepath)

    # Filter G3 skills
    g3_skills = [s for s in all_skills if extract_grade(s['id']) == 'G3']
    print(f"Found {len(g3_skills)} Grade 3 skills")

    # Create lookup dict for all skills
    all_skills_dict = {s['id']: s for s in all_skills}

    # Analyze each G3 skill
    all_issues = []
    for skill in g3_skills:
        issues = analyze_dependencies(skill, all_skills_dict)
        all_issues.extend(issues)

    # Check for circular dependencies
    circular_issues = detect_circular_dependencies(g3_skills)
    all_issues.extend(circular_issues)

    # Sort issues by priority
    priority_order = {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2}
    all_issues.sort(key=lambda x: (priority_order[x['priority']], x['skill_id']))

    # Generate report
    print("\n" + "="*80)
    print("GRADE 3 SKILLS ANALYSIS REPORT")
    print("="*80)
    print(f"\nTotal G3 Skills: {len(g3_skills)}")
    print(f"Total Issues Found: {len(all_issues)}")
    print(f"  HIGH Priority: {len([i for i in all_issues if i['priority'] == 'HIGH'])}")
    print(f"  MEDIUM Priority: {len([i for i in all_issues if i['priority'] == 'MEDIUM'])}")
    print(f"  LOW Priority: {len([i for i in all_issues if i['priority'] == 'LOW'])}")

    # Group by priority
    for priority in ['HIGH', 'MEDIUM', 'LOW']:
        priority_issues = [i for i in all_issues if i['priority'] == priority]
        if not priority_issues:
            continue

        print(f"\n{'='*80}")
        print(f"{priority} PRIORITY ISSUES ({len(priority_issues)})")
        print('='*80)

        # Group by type
        issues_by_type = defaultdict(list)
        for issue in priority_issues:
            issues_by_type[issue['type']].append(issue)

        for issue_type, issues in sorted(issues_by_type.items()):
            print(f"\n{issue_type} ({len(issues)} issues):")
            print('-'*80)
            for issue in issues:
                print(f"\nSkill: {issue['skill_id']}")
                print(f"Title: {issue['title']}")
                print(f"Problem: {issue['problem']}")
                print(f"Fix: {issue['recommendation']}")

    # Save detailed report
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/G3_ANALYSIS_REPORT.md', 'w') as f:
        f.write("# Grade 3 Skills Analysis Report\n\n")
        f.write(f"**Analysis Date:** 2025-11-20\n\n")
        f.write(f"**Total G3 Skills:** {len(g3_skills)}\n\n")
        f.write(f"**Total Issues Found:** {len(all_issues)}\n\n")
        f.write(f"- HIGH Priority: {len([i for i in all_issues if i['priority'] == 'HIGH'])}\n")
        f.write(f"- MEDIUM Priority: {len([i for i in all_issues if i['priority'] == 'MEDIUM'])}\n")
        f.write(f"- LOW Priority: {len([i for i in all_issues if i['priority'] == 'LOW'])}\n\n")

        for priority in ['HIGH', 'MEDIUM', 'LOW']:
            priority_issues = [i for i in all_issues if i['priority'] == priority]
            if not priority_issues:
                continue

            f.write(f"\n## {priority} PRIORITY ISSUES ({len(priority_issues)})\n\n")

            issues_by_type = defaultdict(list)
            for issue in priority_issues:
                issues_by_type[issue['type']].append(issue)

            for issue_type, issues in sorted(issues_by_type.items()):
                f.write(f"\n### {issue_type} ({len(issues)} issues)\n\n")
                for issue in issues:
                    f.write(f"**Skill:** {issue['skill_id']}\n\n")
                    f.write(f"**Title:** {issue['title']}\n\n")
                    f.write(f"**Problem:** {issue['problem']}\n\n")
                    f.write(f"**Recommendation:** {issue['recommendation']}\n\n")
                    f.write("---\n\n")

        # Add summary of all G3 skills
        f.write("\n## All Grade 3 Skills Summary\n\n")
        for skill in sorted(g3_skills, key=lambda x: x['id']):
            f.write(f"### {skill['id']}: {skill['title']}\n\n")
            if skill['dependencies']:
                f.write("**Dependencies:**\n")
                for dep in skill['dependencies']:
                    dep_grade = extract_grade(dep)
                    f.write(f"- {dep} (Grade {dep_grade})\n")
            else:
                f.write("**Dependencies:** None\n")
            f.write("\n")

    print("\n" + "="*80)
    print("Full report saved to: G3_ANALYSIS_REPORT.md")
    print("="*80)

if __name__ == '__main__':
    main()
