#!/usr/bin/env python3
"""
Validate Grade K skills after applying 6 dependency fixes.
Checks:
1. X-2 Rule: Grade K skills only depend on Grade K skills
2. Circular Dependencies
3. Invalid References
4. Applied Changes verification
5. Grade-Level Coherence
"""

import re
import json
from collections import defaultdict, deque

def parse_allskills(filepath):
    """Parse allskills.md and extract all skills."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    # Split by "ID:" to get each skill block
    skill_blocks = re.split(r'\n(?=ID:\s+)', content)

    for block in skill_blocks:
        # Extract skill ID (handles GK, K, and G1-G8 formats)
        id_match = re.match(r'ID:\s+([A-Z]\d+\.[A-Z]+\d*\.\d+)', block)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract skill title (the "Skill:" line)
        skill_match = re.search(r'Skill:\s+([^\n]+)', block)
        title = skill_match.group(1).strip() if skill_match else "Unknown"

        # Extract dependencies
        dependencies = []
        deps_section = re.search(r'Dependencies:\s*\n((?:\*\s+[^\n]+\n?)+)', block)
        if deps_section:
            deps_text = deps_section.group(1)
            # Extract all skill IDs from dependency lines (handles GK, K, and G1-G8 formats)
            dep_ids = re.findall(r'([A-Z]\d+\.[A-Z]+\d*\.\d+)', deps_text)
            dependencies = dep_ids

        # Extract grade (e.g., T01.GK.01 -> GK, T01.G1.01 -> G1)
        grade_match = re.search(r'\.([A-Z]+\d*)\.', skill_id)
        grade = grade_match.group(1) if grade_match else "Unknown"

        skills[skill_id] = {
            'id': skill_id,
            'title': title,
            'grade': grade,
            'dependencies': dependencies,
            'content': block
        }

    return skills

def check_x_minus_2_rule(skills):
    """Check that Grade K skills only depend on Grade K skills."""
    violations = []
    grade_k_skills = {sid: s for sid, s in skills.items() if s['grade'] == 'GK'}

    for skill_id, skill in grade_k_skills.items():
        for dep in skill['dependencies']:
            # Extract grade from dependency ID (e.g., T01.GK.01 -> GK)
            dep_grade_match = re.search(r'\.([A-Z]+\d*)\.', dep)
            if dep_grade_match:
                dep_grade_code = dep_grade_match.group(1)
                if dep_grade_code != 'GK':
                    violations.append({
                        'skill': skill_id,
                        'title': skill['title'],
                        'invalid_dep': dep,
                        'dep_grade': dep_grade_code
                    })

    return violations

def check_circular_dependencies(skills):
    """Check for circular dependencies."""
    def has_cycle(skill_id, visited, rec_stack, skills):
        visited.add(skill_id)
        rec_stack.add(skill_id)

        if skill_id in skills:
            for dep in skills[skill_id]['dependencies']:
                if dep not in visited:
                    cycle = has_cycle(dep, visited, rec_stack, skills)
                    if cycle:
                        return [skill_id] + cycle
                elif dep in rec_stack:
                    return [skill_id, dep]

        rec_stack.remove(skill_id)
        return None

    grade_k_skills = {sid: s for sid, s in skills.items() if s['grade'] == 'GK'}
    cycles = []
    visited = set()

    for skill_id in grade_k_skills:
        if skill_id not in visited:
            cycle = has_cycle(skill_id, visited, set(), skills)
            if cycle:
                cycles.append(cycle)

    return cycles

def check_invalid_references(skills):
    """Check that all dependency IDs exist as valid skills."""
    grade_k_skills = {sid: s for sid, s in skills.items() if s['grade'] == 'GK'}
    all_skill_ids = set(skills.keys())
    invalid_refs = []

    for skill_id, skill in grade_k_skills.items():
        for dep in skill['dependencies']:
            if dep not in all_skill_ids:
                invalid_refs.append({
                    'skill': skill_id,
                    'title': skill['title'],
                    'invalid_dep': dep
                })

    return invalid_refs

def verify_applied_changes(skills):
    """Verify the 6 specific fixes were applied correctly."""
    expected_changes = [
        ('T14.GK.01', 'T06.GK.01'),
        ('T14.GK.02', 'T09.GK.01'),
        ('T13.GK.02', 'T01.GK.01'),
        ('T26.GK.01', 'T09.GK.01'),
        ('T26.GK.02', 'T09.GK.01'),
        ('T27.GK.01', 'T10.GK.01'),
    ]

    results = []
    for skill_id, expected_dep in expected_changes:
        if skill_id in skills:
            actual_deps = skills[skill_id]['dependencies']
            has_dep = expected_dep in actual_deps
            results.append({
                'skill': skill_id,
                'expected_dep': expected_dep,
                'actual_deps': actual_deps,
                'passed': has_dep
            })
        else:
            results.append({
                'skill': skill_id,
                'expected_dep': expected_dep,
                'actual_deps': [],
                'passed': False,
                'error': 'Skill not found'
            })

    return results

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("=" * 80)
    print("GRADE K SKILLS VALIDATION REPORT")
    print("=" * 80)
    print()

    # Parse skills
    print("Parsing allskills.md...")
    skills = parse_allskills(filepath)
    grade_k_skills = {sid: s for sid, s in skills.items() if s['grade'] == 'GK'}

    print(f"Total skills parsed: {len(skills)}")
    print(f"Total Grade K skills: {len(grade_k_skills)}")
    print()

    # Check 1: X-2 Rule
    print("-" * 80)
    print("CHECK 1: X-2 RULE (Grade K skills only depend on Grade K skills)")
    print("-" * 80)
    violations = check_x_minus_2_rule(skills)

    if not violations:
        print("STATUS: PASS")
        print("All Grade K skills only depend on Grade K skills.")
    else:
        print(f"STATUS: FAIL")
        print(f"Found {len(violations)} violation(s):")
        for v in violations:
            print(f"  - {v['skill']} ({v['title']})")
            print(f"    Invalid dependency: {v['invalid_dep']} (Grade {v['dep_grade']})")
    print()

    # Check 2: Circular Dependencies
    print("-" * 80)
    print("CHECK 2: CIRCULAR DEPENDENCIES")
    print("-" * 80)
    cycles = check_circular_dependencies(skills)

    if not cycles:
        print("STATUS: PASS")
        print("No circular dependencies found.")
    else:
        print(f"STATUS: FAIL")
        print(f"Found {len(cycles)} circular dependency chain(s):")
        for i, cycle in enumerate(cycles, 1):
            print(f"  Cycle {i}: {' -> '.join(cycle)}")
    print()

    # Check 3: Invalid References
    print("-" * 80)
    print("CHECK 3: INVALID REFERENCES")
    print("-" * 80)
    invalid_refs = check_invalid_references(skills)

    if not invalid_refs:
        print("STATUS: PASS")
        print("All dependency IDs are valid.")
    else:
        print(f"STATUS: FAIL")
        print(f"Found {len(invalid_refs)} invalid reference(s):")
        for ref in invalid_refs:
            print(f"  - {ref['skill']} ({ref['title']})")
            print(f"    Invalid dependency: {ref['invalid_dep']}")
    print()

    # Check 4: Applied Changes Verification
    print("-" * 80)
    print("CHECK 4: APPLIED CHANGES VERIFICATION")
    print("-" * 80)
    change_results = verify_applied_changes(skills)

    all_passed = all(r['passed'] for r in change_results)
    if all_passed:
        print("STATUS: PASS")
        print("All 6 fixes were correctly applied:")
    else:
        print("STATUS: FAIL")
        print("Applied changes verification:")

    for i, result in enumerate(change_results, 1):
        status = "✓" if result['passed'] else "✗"
        print(f"  {status} {result['skill']} should have {result['expected_dep']}")
        if not result['passed']:
            if 'error' in result:
                print(f"     ERROR: {result['error']}")
            else:
                print(f"     Actual dependencies: {', '.join(result['actual_deps']) if result['actual_deps'] else 'None'}")
    print()

    # Check 5: Grade-Level Coherence (Sample Check)
    print("-" * 80)
    print("CHECK 5: GRADE-LEVEL COHERENCE (Sample)")
    print("-" * 80)
    # Sample some skills to check they're properly connected
    sample_skills = ['T01.GK.01', 'T09.GK.01', 'T10.GK.01', 'T06.GK.01']
    coherence_issues = []

    for skill_id in sample_skills:
        if skill_id in skills:
            skill = skills[skill_id]
            print(f"{skill_id}: {skill['title']}")
            if skill['dependencies']:
                print(f"  Dependencies: {', '.join(skill['dependencies'])}")
            else:
                print(f"  Dependencies: None")
        else:
            coherence_issues.append(f"Sample skill {skill_id} not found")
            print(f"{skill_id}: NOT FOUND")

    if not coherence_issues:
        print("\nSTATUS: PASS")
        print("Sample skills are properly defined.")
    else:
        print("\nSTATUS: FAIL")
        for issue in coherence_issues:
            print(f"  - {issue}")
    print()

    # Final Summary
    print("=" * 80)
    print("FINAL VALIDATION STATUS")
    print("=" * 80)

    all_checks_passed = (
        not violations and
        not cycles and
        not invalid_refs and
        all_passed and
        not coherence_issues
    )

    if all_checks_passed:
        print("RESULT: PASS")
        print(f"\nAll {len(grade_k_skills)} Grade K skills validated successfully.")
        print("All dependency fixes have been correctly applied.")
        print("No violations found.")
    else:
        print("RESULT: FAIL")
        print("\nValidation failed. Issues found:")
        if violations:
            print(f"  - X-2 Rule violations: {len(violations)}")
        if cycles:
            print(f"  - Circular dependencies: {len(cycles)}")
        if invalid_refs:
            print(f"  - Invalid references: {len(invalid_refs)}")
        if not all_passed:
            failed_changes = sum(1 for r in change_results if not r['passed'])
            print(f"  - Applied changes not verified: {failed_changes}/6")
        if coherence_issues:
            print(f"  - Coherence issues: {len(coherence_issues)}")

    print()

if __name__ == '__main__':
    main()
