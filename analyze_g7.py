#!/usr/bin/env python3
"""
Extract and analyze all G7 skills from allskills.md
"""

import re
from collections import defaultdict

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
        skill['description'] = lines[i].split(':', 1)[1].strip()
        i += 1

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

def analyze_g7_dependencies(g7_skills, all_skills_dict):
    """Analyze G7 skill dependencies for issues"""
    issues = {
        'HIGH': [],
        'MEDIUM': [],
        'LOW': []
    }

    for skill in g7_skills:
        skill_id = skill['id']
        skill_name = skill['skill']
        deps = skill['dependencies']

        # Check each dependency
        for dep_id in deps:
            dep_grade = extract_grade_from_id(dep_id)

            # HIGH: Dependencies on G4 or lower (except GK, G1, G2)
            if dep_grade and dep_grade not in ['GK', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7']:
                issues['HIGH'].append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'issue': f'Invalid dependency grade: {dep_grade}',
                    'dependency': dep_id,
                    'fix': f'Remove or replace with appropriate G5-G7 dependency'
                })
            elif dep_grade == 'G4':
                issues['HIGH'].append({
                    'skill_id': skill_id,
                    'skill_name': skill_name,
                    'issue': 'Dependency on G4 (too low for G7)',
                    'dependency': dep_id,
                    'fix': 'Replace with G5 or G6 skill that covers the same concept'
                })

            # HIGH: Dependencies on G8 or higher
            if dep_grade and dep_grade.startswith('G') and dep_grade not in ['GK', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7']:
                try:
                    grade_num = int(dep_grade[1:])
                    if grade_num >= 8:
                        issues['HIGH'].append({
                            'skill_id': skill_id,
                            'skill_name': skill_name,
                            'issue': f'Forward dependency on {dep_grade}',
                            'dependency': dep_id,
                            'fix': f'Remove dependency on future grade {dep_grade}'
                        })
                except:
                    pass

        # Check for transitive dependencies
        # MEDIUM: Check if skill depends on both A and B where B depends on A
        for i, dep1 in enumerate(deps):
            if dep1 in all_skills_dict:
                dep1_deps = all_skills_dict[dep1].get('dependencies', [])
                for dep2 in deps[i+1:]:
                    if dep2 in dep1_deps:
                        issues['MEDIUM'].append({
                            'skill_id': skill_id,
                            'skill_name': skill_name,
                            'issue': f'Transitive dependency: depends on both {dep1} and {dep2}, but {dep1} already depends on {dep2}',
                            'dependency': dep2,
                            'fix': f'Remove {dep2} from dependencies (already covered by {dep1})'
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

    # Save G7 skills
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/g7_skills_list.txt', 'w') as f:
        for skill in g7_skills:
            f.write(f"\n{'='*80}\n")
            f.write(f"ID: {skill['id']}\n")
            f.write(f"Skill: {skill['skill']}\n")
            f.write(f"Description: {skill.get('description', 'N/A')}\n")
            f.write(f"Dependencies ({len(skill['dependencies'])}):\n")
            for dep in skill['dependencies']:
                dep_grade = extract_grade_from_id(dep)
                f.write(f"  - {dep} ({dep_grade})\n")

    print(f"\nG7 skills saved to g7_skills_list.txt")

    # Analyze dependencies
    print("\nAnalyzing dependencies...")
    issues = analyze_g7_dependencies(g7_skills, all_skills_dict)

    # Print summary
    print(f"\nISSUE SUMMARY:")
    print(f"  HIGH priority: {len(issues['HIGH'])}")
    print(f"  MEDIUM priority: {len(issues['MEDIUM'])}")
    print(f"  LOW priority: {len(issues['LOW'])}")

    # Save detailed report
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/g7_analysis_report.txt', 'w') as f:
        f.write("="*80 + "\n")
        f.write("G7 SKILLS DEPENDENCY ANALYSIS\n")
        f.write("="*80 + "\n\n")

        for priority in ['HIGH', 'MEDIUM', 'LOW']:
            if issues[priority]:
                f.write(f"\n{priority} PRIORITY ISSUES ({len(issues[priority])})\n")
                f.write("="*80 + "\n\n")

                for issue in issues[priority]:
                    f.write(f"Skill: {issue['skill_id']} - {issue['skill_name']}\n")
                    f.write(f"Issue: {issue['issue']}\n")
                    if 'dependency' in issue:
                        f.write(f"Dependency: {issue['dependency']}\n")
                    f.write(f"Fix: {issue['fix']}\n")
                    f.write("\n" + "-"*80 + "\n\n")

    print("\nDetailed analysis saved to g7_analysis_report.txt")

if __name__ == '__main__':
    main()
