#!/usr/bin/env python3
"""
Validate that G8 fixes were applied correctly.

Checks:
1. No G8 skills depend on G5 or lower
2. No self-references in G1 skills
3. No transitive dependencies in target skills
4. All dependency IDs still exist
"""

import re
import json
from collections import defaultdict

def parse_skills(filepath):
    """Parse all skills from allskills.md."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}

    # Find all skills
    pattern = r'ID: (T\d+\.G\d+\.\d+).*?(?=\n\nID: T\d+\.G|\Z)'
    matches = re.finditer(pattern, content, re.DOTALL)

    for match in matches:
        block = match.group(0)
        skill_id = match.group(1)

        # Extract dependencies
        deps_match = re.search(r'Dependencies:\s*\n((?:\*.*\n)*)', block)
        if deps_match:
            dependencies = re.findall(r'T\d+\.G\d+\.\d+', deps_match.group(1))
        else:
            dependencies = []

        # Extract title
        title_match = re.search(r'Skill:\s*(.+?)(?:\n|$)', block)
        title = title_match.group(1).strip() if title_match else "Unknown"

        skills[skill_id] = {
            'id': skill_id,
            'title': title,
            'dependencies': dependencies
        }

    return skills

def get_grade(skill_id):
    """Extract grade from skill ID."""
    match = re.search(r'\.G(\d+)\.', skill_id)
    return int(match.group(1)) if match else 0

def get_topic(skill_id):
    """Extract topic from skill ID."""
    match = re.search(r'^(T\d+)\.', skill_id)
    return match.group(1) if match else None

def check_g8_grade_constraints(skills):
    """Check that G8 skills only depend on G6+."""
    violations = []

    g8_skills = [k for k in skills.keys() if get_grade(k) == 8]

    for skill_id in g8_skills:
        skill = skills[skill_id]
        for dep in skill['dependencies']:
            if dep not in skills:
                violations.append({
                    'type': 'missing_dependency',
                    'skill_id': skill_id,
                    'dependency': dep,
                    'message': f"{skill_id} depends on non-existent {dep}"
                })
                continue

            dep_grade = get_grade(dep)
            if dep_grade < 6:
                violations.append({
                    'type': 'low_grade_dependency',
                    'skill_id': skill_id,
                    'dependency': dep,
                    'dep_grade': dep_grade,
                    'message': f"{skill_id} depends on {dep} (G{dep_grade})"
                })

    return violations

def check_self_references(skills):
    """Check for self-referencing dependencies."""
    violations = []

    for skill_id, skill in skills.items():
        if skill_id in skill['dependencies']:
            violations.append({
                'type': 'self_reference',
                'skill_id': skill_id,
                'message': f"{skill_id} has self-reference in dependencies"
            })

    return violations

def check_transitive_dependencies(skills, target_skills=None):
    """Check for transitive dependencies."""
    if target_skills is None:
        target_skills = skills.keys()

    violations = []

    for skill_id in target_skills:
        if skill_id not in skills:
            continue

        skill = skills[skill_id]
        direct_deps = set(skill['dependencies'])

        if len(direct_deps) <= 1:
            continue

        # Build transitive set
        indirect_deps = set()
        for dep in direct_deps:
            if dep in skills:
                indirect_deps.update(skills[dep]['dependencies'])

        # Find redundant
        redundant = direct_deps & indirect_deps

        if redundant:
            violations.append({
                'type': 'transitive_dependency',
                'skill_id': skill_id,
                'redundant_deps': list(redundant),
                'message': f"{skill_id} has transitive dependencies: {', '.join(redundant)}"
            })

    return violations

def check_circular_dependencies(skills):
    """Check for circular dependency chains."""
    violations = []

    def has_cycle(skill_id, visited=None, stack=None):
        if visited is None:
            visited = set()
            stack = set()

        if skill_id in stack:
            return [skill_id]

        if skill_id in visited:
            return []

        if skill_id not in skills:
            return []

        visited.add(skill_id)
        stack.add(skill_id)

        for dep in skills[skill_id]['dependencies']:
            cycle = has_cycle(dep, visited, stack)
            if cycle:
                return [skill_id] + cycle

        stack.remove(skill_id)
        return []

    checked = set()
    for skill_id in skills.keys():
        if skill_id in checked:
            continue

        cycle = has_cycle(skill_id)
        if cycle:
            violations.append({
                'type': 'circular_dependency',
                'cycle': cycle,
                'message': f"Circular dependency: {' → '.join(cycle)}"
            })
            checked.update(cycle)

    return violations

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("=" * 80)
    print("G8 FIXES VALIDATION")
    print("=" * 80)
    print()

    print("Parsing skills file...")
    skills = parse_skills(filepath)
    print(f"Total skills parsed: {len(skills)}")
    print()

    # Count by grade
    grade_counts = defaultdict(int)
    for skill_id in skills.keys():
        grade = get_grade(skill_id)
        grade_counts[grade] += 1

    print("Skills by grade:")
    for grade in sorted(grade_counts.keys()):
        if grade == 0:
            print(f"  GK: {grade_counts[grade]}")
        else:
            print(f"  G{grade}: {grade_counts[grade]}")
    print()

    # Run validation checks
    all_violations = []

    print("CHECK 1: G8 grade constraints (should only depend on G6+)")
    print("-" * 80)
    violations = check_g8_grade_constraints(skills)
    if violations:
        print(f"❌ FAILED: {len(violations)} violations found")
        for v in violations[:10]:
            print(f"  - {v['message']}")
        if len(violations) > 10:
            print(f"  ... and {len(violations) - 10} more")
        all_violations.extend(violations)
    else:
        print("✓ PASSED: All G8 skills depend only on G6+")
    print()

    print("CHECK 2: Self-references")
    print("-" * 80)
    violations = check_self_references(skills)
    if violations:
        print(f"❌ FAILED: {len(violations)} self-references found")
        for v in violations[:10]:
            print(f"  - {v['message']}")
        all_violations.extend(violations)
    else:
        print("✓ PASSED: No self-references found")
    print()

    print("CHECK 3: Circular dependencies")
    print("-" * 80)
    violations = check_circular_dependencies(skills)
    if violations:
        print(f"❌ FAILED: {len(violations)} circular dependency chains found")
        for v in violations[:10]:
            print(f"  - {v['message']}")
        all_violations.extend(violations)
    else:
        print("✓ PASSED: No circular dependencies found")
    print()

    print("CHECK 4: Transitive dependencies (target G8 skills)")
    print("-" * 80)
    target_skills = [
        'T25.G8.02', 'T25.G8.04',
        'T34.G8.01', 'T34.G8.03',
        'T35.G8.02', 'T35.G8.03', 'T35.G8.04',
        'T36.G8.04'
    ]
    violations = check_transitive_dependencies(skills, target_skills)
    if violations:
        print(f"❌ FAILED: {len(violations)} transitive dependencies found")
        for v in violations[:10]:
            print(f"  - {v['message']}")
        all_violations.extend(violations)
    else:
        print("✓ PASSED: No transitive dependencies in target skills")
    print()

    # Summary
    print("=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)

    if all_violations:
        print(f"❌ VALIDATION FAILED: {len(all_violations)} total violations")
        print()
        print("Violations by type:")
        violation_types = defaultdict(int)
        for v in all_violations:
            violation_types[v['type']] += 1
        for vtype, count in sorted(violation_types.items()):
            print(f"  {vtype}: {count}")
    else:
        print("✓ VALIDATION PASSED: All checks successful!")
        print()
        print("G8 fixes have been applied correctly:")
        print("  - No G8 skills depend on G5 or lower")
        print("  - No self-references in any skills")
        print("  - No circular dependencies")
        print("  - No transitive dependencies in target skills")

    print()
    print("=" * 80)

    # Save validation report
    if all_violations:
        report_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G8_VALIDATION_FAILURES.json'
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump({
                'total_violations': len(all_violations),
                'violations_by_type': dict(violation_types),
                'violations': all_violations
            }, f, indent=2)
        print(f"Validation failures saved to: {report_file}")
    else:
        report_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G8_VALIDATION_SUCCESS.txt'
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write("G8 VALIDATION: PASSED\n")
            f.write(f"All {len(skills)} skills validated successfully\n")
            f.write("No violations found\n")
        print(f"Validation success saved to: {report_file}")

if __name__ == '__main__':
    main()
