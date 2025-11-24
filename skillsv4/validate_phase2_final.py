#!/usr/bin/env python3
"""
Validate Phase 2 fixes for Grade K skills
"""

import re
from collections import defaultdict

def parse_skills_file(filepath: str):
    """Parse the allskills.md file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    skill_blocks = re.split(r'\n(?=ID: T\d+\.G[K\d]\.)', content)

    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID:'):
            continue

        lines = block.strip().split('\n')
        id_match = re.match(r'ID: (T\d+\.G[K\d]\.\d+)', lines[0])
        if not id_match:
            continue

        skill_id = id_match.group(1)
        dependencies = []

        for i, line in enumerate(lines):
            if line.startswith('Dependencies:'):
                j = i + 1
                while j < len(lines) and lines[j].startswith('*'):
                    dep_match = re.search(r'(T\d+\.G[K\d]\.\d+)', lines[j])
                    if dep_match:
                        dependencies.append(dep_match.group(1))
                    j += 1
                break

        grade_match = re.search(r'\.G([K\d])\.', skill_id)
        grade = grade_match.group(1) if grade_match else None

        skills[skill_id] = {
            'id': skill_id,
            'grade': grade,
            'dependencies': dependencies
        }

    return skills

def validate_grade_k(skills):
    """Validate Grade K skills"""
    grade_k_skills = {sid: s for sid, s in skills.items() if s['grade'] == 'K'}

    print(f"Total Grade K skills: {len(grade_k_skills)}")

    # Check X-2 violations
    x2_violations = []
    for skill_id, skill in grade_k_skills.items():
        for dep_id in skill['dependencies']:
            if dep_id in skills:
                dep_grade = skills[dep_id]['grade']
                if dep_grade != 'K':
                    x2_violations.append((skill_id, dep_id, dep_grade))

    # Check for circular dependencies
    def has_cycle(skill_id, visited, path):
        if skill_id in visited:
            if skill_id in path:
                return path[path.index(skill_id):] + [skill_id]
            return []
        visited.add(skill_id)
        path.append(skill_id)
        if skill_id in grade_k_skills:
            for dep_id in grade_k_skills[skill_id]['dependencies']:
                if dep_id in grade_k_skills:
                    cycle = has_cycle(dep_id, visited.copy(), path.copy())
                    if cycle:
                        return cycle
        return []

    circular_deps = []
    checked = set()
    for skill_id in grade_k_skills:
        if skill_id not in checked:
            cycle = has_cycle(skill_id, set(), [])
            if cycle:
                circular_deps.append(cycle)
                checked.update(cycle)

    # Report
    print("\n" + "="*70)
    print("VALIDATION RESULTS")
    print("="*70)

    if x2_violations:
        print(f"\nX-2 VIOLATIONS FOUND: {len(x2_violations)}")
        for skill_id, dep_id, dep_grade in x2_violations:
            print(f"  {skill_id} depends on {dep_id} (Grade {dep_grade})")
    else:
        print("\nX-2 RULE: PASSED - All Grade K skills only depend on Grade K skills")

    if circular_deps:
        print(f"\nCIRCULAR DEPENDENCIES FOUND: {len(circular_deps)}")
        for cycle in circular_deps:
            print(f"  {' -> '.join(cycle)}")
    else:
        print("\nCIRCULAR DEPENDENCIES: PASSED - No circular dependencies found")

    # Count dependencies
    total_deps = sum(len(s['dependencies']) for s in grade_k_skills.values())
    avg_deps = total_deps / len(grade_k_skills) if grade_k_skills else 0

    print(f"\nDEPENDENCY STATISTICS:")
    print(f"- Total dependencies: {total_deps}")
    print(f"- Average dependencies per skill: {avg_deps:.2f}")

    # Find skills with no dependencies
    no_deps = [sid for sid, s in grade_k_skills.items() if not s['dependencies']]
    print(f"- Skills with no dependencies: {len(no_deps)}")

    # Find skills with most dependencies
    max_deps = max(len(s['dependencies']) for s in grade_k_skills.values()) if grade_k_skills else 0
    skills_max_deps = [sid for sid, s in grade_k_skills.items() if len(s['dependencies']) == max_deps]
    print(f"- Maximum dependencies for a single skill: {max_deps}")
    if skills_max_deps:
        print(f"  Skills: {', '.join(skills_max_deps)}")

    print("\n" + "="*70)
    if not x2_violations and not circular_deps:
        print("ALL VALIDATIONS PASSED!")
    else:
        print("VALIDATION FAILED - Issues found above")
    print("="*70)

if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = parse_skills_file(filepath)
    validate_grade_k(skills)
