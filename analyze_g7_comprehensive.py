#!/usr/bin/env python3
"""
Comprehensive analysis of all G7 skills from allskills.md
Checks for:
1. Dependency grade constraints (only G5, G6, G7 + foundational GK-G3)
2. Missing dependencies
3. Circular dependencies
4. Transitive dependencies
5. Same-grade forward dependencies
6. Skill clarity issues
7. Out of order skills
"""

import re
from collections import defaultdict, deque

def parse_skill_block(lines, start_idx):
    """Parse a single skill block starting at start_idx"""
    skill = {}
    i = start_idx

    # Parse ID line
    if i < len(lines) and lines[i].startswith('ID:'):
        skill['id'] = lines[i].split(':', 1)[1].strip()
        i += 1
    else:
        return None, i

    # Parse Topic
    if i < len(lines) and lines[i].startswith('Topic:'):
        skill['topic'] = lines[i].split(':', 1)[1].strip()
        i += 1

    # Parse Skill name
    if i < len(lines) and lines[i].startswith('Skill:'):
        skill['skill'] = lines[i].split(':', 1)[1].strip()
        i += 1

    # Parse Description
    if i < len(lines) and lines[i].startswith('Description:'):
        desc_lines = []
        desc_lines.append(lines[i].split(':', 1)[1].strip())
        i += 1
        # Continue reading description if it spans multiple lines
        while i < len(lines) and not lines[i].strip() == '' and not lines[i].startswith('Dependencies:'):
            desc_lines.append(lines[i].strip())
            i += 1
        skill['description'] = ' '.join(desc_lines)

    # Skip blank line
    if i < len(lines) and lines[i].strip() == '':
        i += 1

    # Parse Dependencies
    skill['dependencies'] = []
    if i < len(lines) and lines[i].startswith('Dependencies:'):
        i += 1
        while i < len(lines) and lines[i].startswith('*'):
            dep = lines[i].strip().lstrip('*').strip()
            # Extract just the skill ID
            match = re.match(r'(T\d+\.G[KG0-9]+\.\d+)', dep)
            if match:
                skill['dependencies'].append(match.group(1))
            i += 1

    return skill, i

def extract_all_skills(filepath):
    """Extract all skills from the markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    skills = []
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith('ID:'):
            skill, i = parse_skill_block(lines, i)
            if skill:
                skills.append(skill)
        else:
            i += 1

    return skills

def extract_grade_from_id(skill_id):
    """Extract grade from skill ID like T01.G7.01 -> G7"""
    match = re.search(r'\.(G[KG0-9]+)\.', skill_id)
    if match:
        return match.group(1)
    return None

def extract_topic_and_number(skill_id):
    """Extract topic and skill number from ID like T01.G7.01 -> ('T01', '01')"""
    match = re.match(r'(T\d+)\.G[KG0-9]+\.(\d+)', skill_id)
    if match:
        return match.group(1), int(match.group(2))
    return None, None

def check_circular_dependencies(skill_id, all_skills_dict, visited, rec_stack):
    """Check for circular dependencies using DFS"""
    visited.add(skill_id)
    rec_stack.add(skill_id)

    if skill_id in all_skills_dict:
        for dep in all_skills_dict[skill_id].get('dependencies', []):
            if dep not in visited:
                cycle = check_circular_dependencies(dep, all_skills_dict, visited, rec_stack)
                if cycle:
                    return cycle
            elif dep in rec_stack:
                # Found a cycle
                return [dep, skill_id]

    rec_stack.remove(skill_id)
    return None

def grade_to_number(grade):
    """Convert grade string to number for comparison. GK=0, G1=1, etc."""
    if grade == 'GK':
        return 0
    elif grade.startswith('G'):
        try:
            return int(grade[1:])
        except:
            return -1
    return -1

def analyze_g7_comprehensive(g7_skills, all_skills_dict):
    """Comprehensive analysis of G7 skills"""
    issues = {
        'HIGH': [],
        'MEDIUM': [],
        'LOW': []
    }

    for skill in g7_skills:
        skill_id = skill['id']
        skill_name = skill['skill']
        skill_topic, skill_num = extract_topic_and_number(skill_id)
        deps = skill['dependencies']
        description = skill.get('description', '')

        # 1. Check dependency grade constraints
        for dep_id in deps:
            dep_grade = extract_grade_from_id(dep_id)
            dep_num = grade_to_number(dep_grade) if dep_grade else -1

            # HIGH: Dependencies on G4 or lower (except foundational GK-G3)
            if dep_num >= 4 and dep_num < 5:
                issues['HIGH'].append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'issue_type': 'Invalid dependency grade',
                    'issue': f'Dependency on {dep_grade} ({dep_id}) - too low for G7 (should be G5-G7 only)',
                    'dependency': dep_id,
                    'fix': f'Replace {dep_id} with equivalent G5 or G6 skill, or remove if not essential'
                })

            # HIGH: Dependencies on G8 or higher (forward dependencies)
            if dep_num >= 8:
                issues['HIGH'].append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'issue_type': 'Forward dependency',
                    'issue': f'Forward dependency on {dep_grade} ({dep_id}) - cannot depend on future grades',
                    'dependency': dep_id,
                    'fix': f'Remove dependency on {dep_id} (future grade)'
                })

        # 2. Check for transitive dependencies
        for i, dep1 in enumerate(deps):
            if dep1 in all_skills_dict:
                dep1_deps = all_skills_dict[dep1].get('dependencies', [])
                for dep2 in deps:
                    if dep2 != dep1 and dep2 in dep1_deps:
                        issues['MEDIUM'].append({
                            'skill_id': skill_id,
                            'skill_name': skill_name,
                            'issue_type': 'Transitive dependency',
                            'issue': f'Depends on both {dep1} and {dep2}, but {dep1} already depends on {dep2}',
                            'dependency': dep2,
                            'fix': f'Remove {dep2} from dependencies (already implied by {dep1})'
                        })

        # 3. Check for same-grade forward dependencies (same topic)
        for dep_id in deps:
            dep_grade = extract_grade_from_id(dep_id)
            dep_topic, dep_num = extract_topic_and_number(dep_id)

            if dep_grade == 'G7' and dep_topic == skill_topic and dep_num is not None and skill_num is not None:
                if dep_num > skill_num:
                    issues['HIGH'].append({
                        'skill_id': skill_id,
                        'skill_name': skill_name,
                        'issue_type': 'Same-grade forward dependency',
                        'issue': f'Depends on later skill in same topic/grade: {dep_id} (num {dep_num} > {skill_num})',
                        'dependency': dep_id,
                        'fix': f'Remove or reorder: {skill_id} cannot depend on {dep_id} which comes after it'
                    })

        # 4. Check skill clarity - overly broad or vague
        vague_words = ['various', 'several', 'multiple complex', 'comprehensive', 'advanced']
        for word in vague_words:
            if word in skill_name.lower() or word in description.lower():
                issues['MEDIUM'].append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'issue_type': 'Potentially too broad',
                    'issue': f'Contains vague term "{word}" - may be too broad or unclear',
                    'fix': 'Consider breaking into more specific skills or clarifying scope'
                })
                break

        # 5. Check for missing obvious dependencies based on description
        # If description mentions loops but no loop dependency
        if ('loop' in description.lower() or 'repeat' in description.lower()) and \
           not any('T07.' in dep for dep in deps):
            issues['MEDIUM'].append({
                'skill_id': skill_id,
                'skill_name': skill_name,
                'issue_type': 'Missing dependency',
                'issue': 'Description mentions loops but no T07 (Loops) dependency found',
                'fix': 'Add appropriate T07 loop skill dependency'
            })

        # If description mentions variables but no variable dependency
        if ('variable' in description.lower() or 'state' in description.lower()) and \
           not any('T09.' in dep for dep in deps):
            issues['MEDIUM'].append({
                'skill_id': skill_id,
                'skill_name': skill_name,
                'issue_type': 'Missing dependency',
                'issue': 'Description mentions variables/state but no T09 (Variables) dependency found',
                'fix': 'Add appropriate T09 variable skill dependency'
            })

        # If description mentions conditions/if but no condition dependency
        if ('condition' in description.lower() or 'if ' in description.lower()) and \
           not any('T08.' in dep for dep in deps):
            issues['MEDIUM'].append({
                'skill_id': skill_id,
                'skill_name': skill_name,
                'issue_type': 'Missing dependency',
                'issue': 'Description mentions conditions but no T08 (Conditions) dependency found',
                'fix': 'Add appropriate T08 condition skill dependency'
            })

        # If description mentions lists/tables but no list dependency
        if ('list' in description.lower() or 'table' in description.lower()) and \
           not any('T10.' in dep for dep in deps):
            issues['MEDIUM'].append({
                'skill_id': skill_id,
                'skill_name': skill_name,
                'issue_type': 'Missing dependency',
                'issue': 'Description mentions lists/tables but no T10 (Lists & Tables) dependency found',
                'fix': 'Add appropriate T10 list skill dependency'
            })

    # 6. Check for circular dependencies
    visited = set()
    for skill in g7_skills:
        if skill['id'] not in visited:
            rec_stack = set()
            cycle = check_circular_dependencies(skill['id'], all_skills_dict, visited, rec_stack)
            if cycle:
                issues['HIGH'].append({
                    'skill_id': skill['id'],
                    'skill_name': skill['skill'],
                    'issue_type': 'Circular dependency',
                    'issue': f'Circular dependency detected: {" -> ".join(cycle)}',
                    'fix': 'Break the circular dependency by removing one of the dependencies'
                })

    return issues

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Extracting all skills...")
    all_skills = extract_all_skills(filepath)
    print(f"Found {len(all_skills)} total skills")

    # Create dictionary for quick lookup
    all_skills_dict = {s['id']: s for s in all_skills}

    # Filter G7 skills
    g7_skills = [s for s in all_skills if '.G7.' in s['id']]
    print(f"Found {len(g7_skills)} G7 skills")

    # Group by topic
    g7_by_topic = defaultdict(list)
    for skill in g7_skills:
        topic = skill['id'].split('.')[0]
        g7_by_topic[topic].append(skill)

    print(f"Across {len(g7_by_topic)} topics")

    # Analyze dependencies
    print("\nAnalyzing dependencies...")
    issues = analyze_g7_comprehensive(g7_skills, all_skills_dict)

    # Remove duplicates
    for priority in ['HIGH', 'MEDIUM', 'LOW']:
        seen = set()
        unique_issues = []
        for issue in issues[priority]:
            key = (issue['skill_id'], issue.get('issue_type', ''), issue.get('dependency', ''))
            if key not in seen:
                seen.add(key)
                unique_issues.append(issue)
        issues[priority] = unique_issues

    # Print summary
    print(f"\nISSUE SUMMARY:")
    print(f"  HIGH priority: {len(issues['HIGH'])}")
    print(f"  MEDIUM priority: {len(issues['MEDIUM'])}")
    print(f"  LOW priority: {len(issues['LOW'])}")

    # Group issues by type
    issue_types = defaultdict(lambda: {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0})
    for priority in ['HIGH', 'MEDIUM', 'LOW']:
        for issue in issues[priority]:
            issue_type = issue.get('issue_type', 'Other')
            issue_types[issue_type][priority] += 1

    print(f"\nISSUES BY TYPE:")
    for issue_type, counts in sorted(issue_types.items()):
        total = counts['HIGH'] + counts['MEDIUM'] + counts['LOW']
        print(f"  {issue_type}: {total} (H:{counts['HIGH']}, M:{counts['MEDIUM']}, L:{counts['LOW']})")

    # Save detailed report
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/G7_COMPREHENSIVE_ANALYSIS.txt', 'w') as f:
        f.write("="*80 + "\n")
        f.write("G7 SKILLS COMPREHENSIVE DEPENDENCY ANALYSIS\n")
        f.write("="*80 + "\n\n")
        f.write(f"Total G7 skills analyzed: {len(g7_skills)}\n")
        f.write(f"Across {len(g7_by_topic)} topics\n\n")

        f.write("ISSUE SUMMARY:\n")
        f.write(f"  HIGH priority: {len(issues['HIGH'])}\n")
        f.write(f"  MEDIUM priority: {len(issues['MEDIUM'])}\n")
        f.write(f"  LOW priority: {len(issues['LOW'])}\n\n")

        f.write("ISSUES BY TYPE:\n")
        for issue_type, counts in sorted(issue_types.items()):
            total = counts['HIGH'] + counts['MEDIUM'] + counts['LOW']
            f.write(f"  {issue_type}: {total} (HIGH:{counts['HIGH']}, MED:{counts['MEDIUM']}, LOW:{counts['LOW']})\n")
        f.write("\n")

        for priority in ['HIGH', 'MEDIUM', 'LOW']:
            if issues[priority]:
                f.write(f"\n{'='*80}\n")
                f.write(f"{priority} PRIORITY ISSUES ({len(issues[priority])})\n")
                f.write(f"{'='*80}\n\n")

                # Group by skill
                by_skill = defaultdict(list)
                for issue in issues[priority]:
                    by_skill[issue['skill_id']].append(issue)

                for skill_id in sorted(by_skill.keys()):
                    skill_issues = by_skill[skill_id]
                    first_issue = skill_issues[0]

                    f.write(f"SKILL: {skill_id}\n")
                    f.write(f"TITLE: {first_issue['skill_name']}\n")
                    if skill_id in all_skills_dict:
                        deps = all_skills_dict[skill_id].get('dependencies', [])
                        f.write(f"DEPENDENCIES ({len(deps)}): {', '.join(deps)}\n")
                    f.write(f"\n")

                    for i, issue in enumerate(skill_issues, 1):
                        f.write(f"  Issue #{i}: [{issue['issue_type']}]\n")
                        f.write(f"    Problem: {issue['issue']}\n")
                        f.write(f"    Fix: {issue['fix']}\n")
                        f.write(f"\n")

                    f.write("-"*80 + "\n\n")

    print("\nComprehensive analysis saved to G7_COMPREHENSIVE_ANALYSIS.txt")

    # Save summary by topic
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/G7_SUMMARY_BY_TOPIC.txt', 'w') as f:
        f.write("="*80 + "\n")
        f.write("G7 SKILLS BY TOPIC\n")
        f.write("="*80 + "\n\n")

        for topic in sorted(g7_by_topic.keys()):
            skills = g7_by_topic[topic]
            f.write(f"\n{topic}: {skills[0]['topic']}\n")
            f.write(f"Total G7 skills: {len(skills)}\n")
            f.write("-"*80 + "\n")
            for skill in sorted(skills, key=lambda s: s['id']):
                f.write(f"\n{skill['id']}: {skill['skill']}\n")
                f.write(f"  Deps ({len(skill['dependencies'])}): ")
                if skill['dependencies']:
                    f.write(', '.join(skill['dependencies']))
                else:
                    f.write("None")
                f.write("\n")

    print("Topic summary saved to G7_SUMMARY_BY_TOPIC.txt")

if __name__ == '__main__':
    main()
