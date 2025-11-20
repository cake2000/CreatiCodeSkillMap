#!/usr/bin/env python3
"""
Comprehensive analysis of ALL Grade 8 (G8) skills in allskills.md
Checks for dependency issues, ordering problems, and skill quality
"""

import re
import json
from collections import defaultdict

def parse_skill(text, start_pos):
    """Parse a single skill block starting at start_pos"""
    skill = {}

    # Extract ID
    id_match = re.search(r'ID:\s*(T\d+\.G\d+\.\d+)', text[start_pos:start_pos+200])
    if not id_match:
        return None
    skill['id'] = id_match.group(1)

    # Extract title (it's on the "Skill:" line)
    title_match = re.search(r'Skill:\s*(.+?)(?:\n|$)', text[start_pos:start_pos+500])
    if title_match:
        skill['title'] = title_match.group(1).strip()
    else:
        skill['title'] = "Unknown"

    # Extract dependencies
    deps_match = re.search(r'Dependencies:\s*(.+?)(?:\n|$)', text[start_pos:start_pos+1000])
    if deps_match:
        deps_str = deps_match.group(1).strip()
        if deps_str.lower() == 'none':
            skill['dependencies'] = []
        else:
            # Parse dependencies - can be comma or semicolon separated
            deps = re.findall(r'T\d+\.G\d+\.\d+', deps_str)
            skill['dependencies'] = deps
    else:
        skill['dependencies'] = []

    # Extract description for quality check
    desc_match = re.search(r'Description:\s*(.+?)(?=\n\n|\nID:|\Z)', text[start_pos:start_pos+2000], re.DOTALL)
    if desc_match:
        skill['description'] = desc_match.group(1).strip()
    else:
        skill['description'] = ""

    return skill

def extract_all_skills(filename):
    """Extract all skills from the markdown file"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all skill IDs
    id_pattern = r'ID:\s*(T\d+\.G\d+\.\d+)'
    matches = list(re.finditer(id_pattern, content))

    skills = {}
    for match in matches:
        skill = parse_skill(content, match.start())
        if skill:
            skills[skill['id']] = skill

    return skills

def get_grade_from_id(skill_id):
    """Extract grade number from skill ID (e.g., T01.G8.01 -> 8)"""
    match = re.search(r'\.G(\d+)\.', skill_id)
    return int(match.group(1)) if match else None

def get_topic_from_id(skill_id):
    """Extract topic from skill ID (e.g., T01.G8.01 -> T01)"""
    match = re.search(r'^(T\d+)\.', skill_id)
    return match.group(1) if match else None

def check_dependency_grade_constraints(skill, all_skills):
    """Check if dependencies follow grade constraints (G8 can only depend on G8, G7, G6)"""
    issues = []
    skill_grade = get_grade_from_id(skill['id'])

    for dep in skill['dependencies']:
        if dep not in all_skills:
            issues.append({
                'type': 'missing_dependency',
                'dependency': dep,
                'message': f"Dependency {dep} does not exist"
            })
            continue

        dep_grade = get_grade_from_id(dep)
        if dep_grade is None:
            continue

        # For G8, dependencies should be from G8, G7, or G6 only
        if skill_grade == 8:
            if dep_grade < 6:
                issues.append({
                    'type': 'dependency_too_old',
                    'dependency': dep,
                    'dep_grade': dep_grade,
                    'message': f"G8 skill depends on G{dep_grade} skill (should be G6, G7, or G8 only)"
                })

    return issues

def check_circular_dependencies(skill_id, all_skills, visited=None, stack=None):
    """Check for circular dependencies using DFS"""
    if visited is None:
        visited = set()
        stack = set()

    if skill_id in stack:
        return [skill_id]  # Circular dependency found

    if skill_id in visited:
        return []

    if skill_id not in all_skills:
        return []

    visited.add(skill_id)
    stack.add(skill_id)

    for dep in all_skills[skill_id]['dependencies']:
        cycle = check_circular_dependencies(dep, all_skills, visited, stack)
        if cycle:
            return [skill_id] + cycle

    stack.remove(skill_id)
    return []

def check_transitive_dependencies(skill, all_skills):
    """Check for transitive dependencies (A->B, B->C, A->C is redundant)"""
    issues = []
    direct_deps = set(skill['dependencies'])

    # Get all indirect dependencies (dependencies of dependencies)
    indirect_deps = set()
    for dep in direct_deps:
        if dep in all_skills:
            indirect_deps.update(all_skills[dep]['dependencies'])

    # Check if any direct dependency is also an indirect dependency
    redundant = direct_deps & indirect_deps

    for dep in redundant:
        issues.append({
            'type': 'transitive_dependency',
            'dependency': dep,
            'message': f"Transitive dependency {dep} (already reachable through another dependency)"
        })

    return issues

def check_same_topic_same_grade(skill, all_skills):
    """Check if skill depends on another skill from same topic and same grade"""
    issues = []
    skill_topic = get_topic_from_id(skill['id'])
    skill_grade = get_grade_from_id(skill['id'])

    for dep in skill['dependencies']:
        if dep not in all_skills:
            continue

        dep_topic = get_topic_from_id(dep)
        dep_grade = get_grade_from_id(dep)

        if skill_topic == dep_topic and skill_grade == dep_grade:
            issues.append({
                'type': 'same_topic_same_grade',
                'dependency': dep,
                'message': f"G8 skill depends on another G8 skill from same topic {skill_topic} (assumed sequential)"
            })

    return issues

def check_skill_quality(skill):
    """Check if skill is clear, specific, and not too broad"""
    issues = []
    title = skill['title'].lower()
    description = skill['description'].lower()

    # Check for overly broad keywords
    broad_keywords = ['advanced', 'complex', 'various', 'multiple', 'general', 'comprehensive', 'all']
    for keyword in broad_keywords:
        if keyword in title:
            issues.append({
                'type': 'broad_skill',
                'message': f"Title contains broad keyword '{keyword}' - may be too general"
            })
            break

    # Check if description is too short
    if len(skill['description']) < 50:
        issues.append({
            'type': 'short_description',
            'message': "Description is very short (< 50 chars) - may lack detail"
        })

    return issues

def check_ordering(skill, all_skills):
    """Check if skill is properly ordered relative to its dependencies"""
    issues = []
    skill_id = skill['id']
    skill_topic = get_topic_from_id(skill_id)
    skill_grade = get_grade_from_id(skill_id)
    skill_num = int(re.search(r'\.(\d+)$', skill_id).group(1))

    # Check dependencies from same topic and same grade
    for dep in skill['dependencies']:
        if dep not in all_skills:
            continue

        dep_topic = get_topic_from_id(dep)
        dep_grade = get_grade_from_id(dep)
        dep_num = int(re.search(r'\.(\d+)$', dep).group(1))

        # If dependency is from same topic and same grade, it should come before
        if skill_topic == dep_topic and skill_grade == dep_grade:
            if dep_num >= skill_num:
                issues.append({
                    'type': 'out_of_order',
                    'dependency': dep,
                    'message': f"Skill {skill_id} depends on {dep} but comes before it in sequence"
                })

    return issues

def analyze_g8_skills(filename):
    """Main analysis function for all G8 skills"""
    print("Loading all skills from file...")
    all_skills = extract_all_skills(filename)
    print(f"Found total skills: {len(all_skills)}")

    # Filter G8 skills
    g8_skills = {k: v for k, v in all_skills.items() if get_grade_from_id(k) == 8}
    print(f"Found G8 skills: {len(g8_skills)}")

    # Group by topic
    skills_by_topic = defaultdict(list)
    for skill_id in sorted(g8_skills.keys()):
        topic = get_topic_from_id(skill_id)
        skills_by_topic[topic].append(skill_id)

    print(f"Topics with G8 skills: {len(skills_by_topic)}")

    # Analyze each G8 skill
    high_priority = []
    medium_priority = []
    low_priority = []

    for skill_id in sorted(g8_skills.keys()):
        skill = g8_skills[skill_id]
        print(f"Analyzing {skill_id}...")

        # Check dependency grade constraints
        grade_issues = check_dependency_grade_constraints(skill, all_skills)
        for issue in grade_issues:
            if issue['type'] == 'dependency_too_old':
                high_priority.append({
                    'skill_id': skill_id,
                    'skill_title': skill['title'],
                    'issue_type': 'dependency_too_old',
                    'description': issue['message'],
                    'current_dependencies': skill['dependencies'],
                    'problematic_dependency': issue['dependency'],
                    'recommended_fix': f"Remove dependency on {issue['dependency']} (G{issue['dep_grade']}) or replace with equivalent G6+ skill"
                })
            elif issue['type'] == 'missing_dependency':
                high_priority.append({
                    'skill_id': skill_id,
                    'skill_title': skill['title'],
                    'issue_type': 'missing_dependency',
                    'description': issue['message'],
                    'current_dependencies': skill['dependencies'],
                    'problematic_dependency': issue['dependency'],
                    'recommended_fix': f"Fix reference to {issue['dependency']} or remove from dependencies"
                })

        # Check circular dependencies
        cycle = check_circular_dependencies(skill_id, all_skills)
        if cycle:
            high_priority.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'issue_type': 'circular_dependency',
                'description': f"Circular dependency detected: {' -> '.join(cycle)}",
                'current_dependencies': skill['dependencies'],
                'recommended_fix': f"Break circular dependency chain: {' -> '.join(cycle)}"
            })

        # Check ordering
        order_issues = check_ordering(skill, all_skills)
        for issue in order_issues:
            high_priority.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'issue_type': 'out_of_order',
                'description': issue['message'],
                'current_dependencies': skill['dependencies'],
                'problematic_dependency': issue['dependency'],
                'recommended_fix': f"Either remove dependency on {issue['dependency']} or reorder skills"
            })

        # Check transitive dependencies
        trans_issues = check_transitive_dependencies(skill, all_skills)
        for issue in trans_issues:
            medium_priority.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'issue_type': 'transitive_dependency',
                'description': issue['message'],
                'current_dependencies': skill['dependencies'],
                'problematic_dependency': issue['dependency'],
                'recommended_fix': f"Remove redundant dependency on {issue['dependency']}"
            })

        # Check same-topic same-grade dependencies
        same_topic_issues = check_same_topic_same_grade(skill, all_skills)
        for issue in same_topic_issues:
            medium_priority.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'issue_type': 'same_topic_same_grade',
                'description': issue['message'],
                'current_dependencies': skill['dependencies'],
                'problematic_dependency': issue['dependency'],
                'recommended_fix': f"Remove dependency on {issue['dependency']} (same-topic same-grade dependencies are implicit)"
            })

        # Check skill quality
        quality_issues = check_skill_quality(skill)
        for issue in quality_issues:
            low_priority.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'issue_type': issue['type'],
                'description': issue['message'],
                'current_dependencies': skill['dependencies'],
                'recommended_fix': "Review and refine skill title/description for clarity and specificity"
            })

    # Create report
    report = {
        'total_g8_skills': len(g8_skills),
        'issues_found': len(high_priority) + len(medium_priority) + len(low_priority),
        'high_priority_count': len(high_priority),
        'medium_priority_count': len(medium_priority),
        'low_priority_count': len(low_priority),
        'high_priority_issues': high_priority,
        'medium_priority_issues': medium_priority,
        'low_priority_issues': low_priority,
        'skills_by_topic': {k: v for k, v in sorted(skills_by_topic.items())},
        'g8_skills_details': {
            skill_id: {
                'title': skill['title'],
                'dependencies': skill['dependencies'],
                'description': skill['description'][:200] + '...' if len(skill['description']) > 200 else skill['description']
            }
            for skill_id, skill in sorted(g8_skills.items())
        }
    }

    return report

if __name__ == '__main__':
    filename = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("=" * 80)
    print("G8 SKILLS COMPREHENSIVE ANALYSIS")
    print("=" * 80)

    report = analyze_g8_skills(filename)

    # Save JSON report
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G8_ANALYSIS_REPORT.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2)

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total G8 skills: {report['total_g8_skills']}")
    print(f"Total issues found: {report['issues_found']}")
    print(f"  - High priority: {report['high_priority_count']}")
    print(f"  - Medium priority: {report['medium_priority_count']}")
    print(f"  - Low priority: {report['low_priority_count']}")
    print(f"\nSkills by topic:")
    for topic, skills in report['skills_by_topic'].items():
        print(f"  {topic}: {len(skills)} skills")

    print(f"\n\nDetailed report saved to: {output_file}")

    # Print summary of issues
    if report['high_priority_issues']:
        print("\n" + "=" * 80)
        print("HIGH PRIORITY ISSUES")
        print("=" * 80)
        for i, issue in enumerate(report['high_priority_issues'][:10], 1):
            print(f"\n{i}. {issue['skill_id']}: {issue['skill_title']}")
            print(f"   Type: {issue['issue_type']}")
            print(f"   Description: {issue['description']}")
            print(f"   Fix: {issue['recommended_fix']}")

        if len(report['high_priority_issues']) > 10:
            print(f"\n... and {len(report['high_priority_issues']) - 10} more high priority issues")

    if report['medium_priority_issues']:
        print("\n" + "=" * 80)
        print("MEDIUM PRIORITY ISSUES (Sample)")
        print("=" * 80)
        for i, issue in enumerate(report['medium_priority_issues'][:5], 1):
            print(f"\n{i}. {issue['skill_id']}: {issue['skill_title']}")
            print(f"   Type: {issue['issue_type']}")
            print(f"   Description: {issue['description']}")
