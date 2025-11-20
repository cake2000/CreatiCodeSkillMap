#!/usr/bin/env python3
"""
Analyze Grade 6 skills from allskills.md file.
Extract all G6 skills and check for dependency issues.
"""

import re
from collections import defaultdict

def extract_grade_from_id(skill_id):
    """Extract grade level from skill ID (e.g., 'G6' from 'T01.G6.01')"""
    match = re.search(r'\.G(\d+|K)\.', skill_id)
    if match:
        grade = match.group(1)
        if grade == 'K':
            return 0
        return int(grade)
    return None

def parse_skills_file(filepath):
    """Parse the allskills.md file and extract all skills with their dependencies"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries (ID: pattern)
    skill_entries = re.split(r'\n(?=ID: T\d+\.G)', content)

    skills = {}
    for entry in skill_entries:
        # Extract skill ID
        id_match = re.search(r'^ID: (T\d+\.G\w+\.\d+)', entry, re.MULTILINE)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic
        topic_match = re.search(r'^Topic: (.+)$', entry, re.MULTILINE)
        topic = topic_match.group(1) if topic_match else "Unknown"

        # Extract skill name
        skill_match = re.search(r'^Skill: (.+)$', entry, re.MULTILINE)
        skill_name = skill_match.group(1) if skill_match else "Unknown"

        # Extract description
        desc_match = re.search(r'^Description: (.+)$', entry, re.MULTILINE)
        description = desc_match.group(1) if desc_match else ""

        # Extract dependencies
        dependencies = []
        in_dependencies = False
        for line in entry.split('\n'):
            if line.strip() == 'Dependencies:':
                in_dependencies = True
                continue
            if in_dependencies:
                if line.strip().startswith('* '):
                    dep_match = re.search(r'\* (T\d+\.G\w+\.\d+):', line)
                    if dep_match:
                        dependencies.append(dep_match.group(1))
                elif line.strip() == '':
                    break

        skills[skill_id] = {
            'topic': topic,
            'skill': skill_name,
            'description': description,
            'dependencies': dependencies
        }

    return skills

def analyze_g6_skills(skills):
    """Analyze Grade 6 skills for issues"""

    g6_skills = {k: v for k, v in skills.items() if '.G6.' in k}

    issues = {
        'HIGH': [],
        'MEDIUM': [],
        'LOW': []
    }

    # Build dependency graph for circular dependency detection
    def has_circular_dependency(skill_id, visited, rec_stack):
        """Check for circular dependencies using DFS"""
        visited.add(skill_id)
        rec_stack.add(skill_id)

        if skill_id in skills:
            for dep in skills[skill_id]['dependencies']:
                if dep not in visited:
                    if has_circular_dependency(dep, visited, rec_stack):
                        return True
                elif dep in rec_stack:
                    return True

        rec_stack.remove(skill_id)
        return False

    # Check each G6 skill
    for skill_id, skill_data in g6_skills.items():
        skill_grade = extract_grade_from_id(skill_id)
        topic_num = re.match(r'T(\d+)\.', skill_id).group(1)

        # Check dependencies
        for dep_id in skill_data['dependencies']:
            dep_grade = extract_grade_from_id(dep_id)
            dep_topic = re.match(r'T(\d+)\.', dep_id).group(1)

            # HIGH: Dependencies on G3 or lower
            if dep_grade is not None and dep_grade <= 3:
                issues['HIGH'].append({
                    'skill': skill_id,
                    'skill_name': skill_data['skill'],
                    'issue': f'Depends on G{dep_grade} skill: {dep_id}',
                    'recommendation': f'Remove {dep_id} - it should be implicit knowledge from earlier grades',
                    'dependency': dep_id
                })

            # MEDIUM: Dependencies on same-topic earlier-grade skills (G4-G5)
            if topic_num == dep_topic and dep_grade is not None and 4 <= dep_grade < skill_grade:
                issues['MEDIUM'].append({
                    'skill': skill_id,
                    'skill_name': skill_data['skill'],
                    'issue': f'Depends on same-topic G{dep_grade} skill: {dep_id}',
                    'recommendation': f'Consider removing {dep_id} - same-topic earlier skills should be implicit',
                    'dependency': dep_id
                })

        # Check for circular dependencies
        visited = set()
        rec_stack = set()
        if has_circular_dependency(skill_id, visited, rec_stack):
            issues['HIGH'].append({
                'skill': skill_id,
                'skill_name': skill_data['skill'],
                'issue': 'Circular dependency detected',
                'recommendation': 'Review dependency chain and remove circular references',
                'dependency': 'CIRCULAR'
            })

        # Check for transitive dependencies
        if skill_id in skills:
            direct_deps = set(skill_data['dependencies'])
            transitive_deps = set()

            for dep in direct_deps:
                if dep in skills:
                    for trans_dep in skills[dep]['dependencies']:
                        transitive_deps.add(trans_dep)

            # Find dependencies that are both direct and transitive
            redundant = direct_deps & transitive_deps
            for red_dep in redundant:
                issues['MEDIUM'].append({
                    'skill': skill_id,
                    'skill_name': skill_data['skill'],
                    'issue': f'Transitive dependency: {red_dep} is already covered by another dependency',
                    'recommendation': f'Remove {red_dep} from direct dependencies - it\'s already transitive',
                    'dependency': red_dep
                })

        # Check if skill description is too broad
        broad_keywords = ['multiple', 'various', 'several', 'many', 'comprehensive', 'complete']
        if any(keyword in skill_data['skill'].lower() for keyword in broad_keywords):
            issues['LOW'].append({
                'skill': skill_id,
                'skill_name': skill_data['skill'],
                'issue': 'Skill name may be too broad',
                'recommendation': 'Consider making the skill more specific and focused',
                'dependency': 'N/A'
            })

    return g6_skills, issues

def generate_report(g6_skills, issues):
    """Generate a plain text report"""

    report = []
    report.append("=" * 80)
    report.append("GRADE 6 SKILLS ANALYSIS REPORT")
    report.append("=" * 80)
    report.append("")

    # Summary
    report.append(f"Total Grade 6 skills found: {len(g6_skills)}")
    report.append(f"HIGH priority issues: {len(issues['HIGH'])}")
    report.append(f"MEDIUM priority issues: {len(issues['MEDIUM'])}")
    report.append(f"LOW priority issues: {len(issues['LOW'])}")
    report.append("")

    # List all G6 skills by topic
    report.append("=" * 80)
    report.append("ALL GRADE 6 SKILLS")
    report.append("=" * 80)
    report.append("")

    skills_by_topic = defaultdict(list)
    for skill_id, skill_data in sorted(g6_skills.items()):
        topic = skill_data['topic']
        skills_by_topic[topic].append((skill_id, skill_data['skill']))

    for topic in sorted(skills_by_topic.keys()):
        report.append(f"\n{topic}")
        report.append("-" * len(topic))
        for skill_id, skill_name in skills_by_topic[topic]:
            report.append(f"  {skill_id}: {skill_name}")

    report.append("")

    # HIGH priority issues
    report.append("\n" + "=" * 80)
    report.append("HIGH PRIORITY ISSUES")
    report.append("=" * 80)
    report.append("")

    if issues['HIGH']:
        for issue in issues['HIGH']:
            report.append(f"Skill: {issue['skill']}")
            report.append(f"  Name: {issue['skill_name']}")
            report.append(f"  Issue: {issue['issue']}")
            report.append(f"  Recommendation: {issue['recommendation']}")
            report.append("")
    else:
        report.append("No HIGH priority issues found!")
        report.append("")

    # MEDIUM priority issues
    report.append("\n" + "=" * 80)
    report.append("MEDIUM PRIORITY ISSUES")
    report.append("=" * 80)
    report.append("")

    if issues['MEDIUM']:
        for issue in issues['MEDIUM']:
            report.append(f"Skill: {issue['skill']}")
            report.append(f"  Name: {issue['skill_name']}")
            report.append(f"  Issue: {issue['issue']}")
            report.append(f"  Recommendation: {issue['recommendation']}")
            report.append("")
    else:
        report.append("No MEDIUM priority issues found!")
        report.append("")

    # LOW priority issues
    report.append("\n" + "=" * 80)
    report.append("LOW PRIORITY ISSUES")
    report.append("=" * 80)
    report.append("")

    if issues['LOW']:
        for issue in issues['LOW']:
            report.append(f"Skill: {issue['skill']}")
            report.append(f"  Name: {issue['skill_name']}")
            report.append(f"  Issue: {issue['issue']}")
            report.append(f"  Recommendation: {issue['recommendation']}")
            report.append("")
    else:
        report.append("No LOW priority issues found!")
        report.append("")

    # Summary by skill
    report.append("\n" + "=" * 80)
    report.append("ISSUES BY SKILL")
    report.append("=" * 80)
    report.append("")

    skills_with_issues = defaultdict(list)
    for priority in ['HIGH', 'MEDIUM', 'LOW']:
        for issue in issues[priority]:
            skills_with_issues[issue['skill']].append((priority, issue))

    for skill_id in sorted(skills_with_issues.keys()):
        report.append(f"\n{skill_id}: {g6_skills[skill_id]['skill']}")
        report.append(f"  Dependencies: {', '.join(g6_skills[skill_id]['dependencies']) if g6_skills[skill_id]['dependencies'] else 'None'}")
        for priority, issue in skills_with_issues[skill_id]:
            report.append(f"  [{priority}] {issue['issue']}")
            report.append(f"    -> {issue['recommendation']}")

    return "\n".join(report)

def main():
    filepath = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"

    print("Parsing skills file...")
    skills = parse_skills_file(filepath)
    print(f"Found {len(skills)} total skills")

    print("Analyzing Grade 6 skills...")
    g6_skills, issues = analyze_g6_skills(skills)

    print("Generating report...")
    report = generate_report(g6_skills, issues)

    # Save report
    output_file = "/media/binyu/USB2/dev/CreatiCodeSkillMap/G6_ANALYSIS_REPORT.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport saved to: {output_file}")
    print(f"\nSummary:")
    print(f"  Total G6 skills: {len(g6_skills)}")
    print(f"  HIGH priority issues: {len(issues['HIGH'])}")
    print(f"  MEDIUM priority issues: {len(issues['MEDIUM'])}")
    print(f"  LOW priority issues: {len(issues['LOW'])}")

    # Also print the report
    print("\n" + report)

if __name__ == "__main__":
    main()
