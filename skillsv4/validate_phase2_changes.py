#!/usr/bin/env python3
"""
Validate Phase 2 changes to ensure:
1. No X-2 rule violations
2. No circular dependencies
3. All dependency IDs exist
"""

import re
from typing import Dict, List, Set, Tuple

def parse_skills(filepath: str) -> Dict[str, Dict]:
    """Parse all skills from the file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}

    # Pattern to match skill blocks
    skill_pattern = r'ID: (T\d+\.(GK|G\d+)\.\d+)\s*\nTopic: ([^\n]+)\s*\nSkill: ([^\n]+)'

    for match in re.finditer(skill_pattern, content):
        skill_id = match.group(1)
        grade = match.group(2)
        topic = match.group(3)
        skill_name = match.group(4)

        # Find dependencies for this skill
        end_pos = match.end()
        remaining = content[end_pos:end_pos+2000]

        deps = []
        dep_match = re.search(r'Dependencies:\s*\n((?:\* [^\n]+\n?)+)', remaining)
        if dep_match:
            dep_text = dep_match.group(1)
            for line in dep_text.strip().split('\n'):
                if line.startswith('* '):
                    dep_id = line.split(':')[0].replace('* ', '').strip()
                    deps.append(dep_id)

        skills[skill_id] = {
            'grade': grade,
            'topic': topic,
            'name': skill_name,
            'dependencies': deps
        }

    return skills

def get_grade_level(grade_str: str) -> int:
    """Convert grade string to numeric level."""
    if grade_str == 'GK':
        return 0
    elif grade_str.startswith('G'):
        return int(grade_str[1:])
    return -1

def check_x2_rule(skills: Dict[str, Dict]) -> List[str]:
    """Check for X-2 rule violations."""
    violations = []

    for skill_id, skill_data in skills.items():
        skill_grade = get_grade_level(skill_data['grade'])

        for dep_id in skill_data['dependencies']:
            if dep_id not in skills:
                violations.append(f"ERROR: {skill_id} depends on non-existent skill {dep_id}")
                continue

            dep_grade = get_grade_level(skills[dep_id]['grade'])

            # Check X-2 rule: skill at grade X can depend on skills at grade X-2 or higher
            if dep_grade < skill_grade - 2:
                violations.append(
                    f"X-2 VIOLATION: {skill_id} (Grade {skill_data['grade']}) "
                    f"depends on {dep_id} (Grade {skills[dep_id]['grade']}) - "
                    f"grade difference is {skill_grade - dep_grade}"
                )

    return violations

def find_circular_dependencies(skills: Dict[str, Dict]) -> List[Tuple[List[str]]]:
    """Find circular dependency chains."""
    cycles = []

    def find_cycle(skill_id: str, path: List[str], visited: Set[str]) -> bool:
        """DFS to find cycles."""
        if skill_id in path:
            # Found a cycle
            cycle_start = path.index(skill_id)
            cycle = path[cycle_start:] + [skill_id]
            cycles.append(cycle)
            return True

        if skill_id in visited:
            return False

        visited.add(skill_id)
        path.append(skill_id)

        if skill_id in skills:
            for dep_id in skills[skill_id]['dependencies']:
                find_cycle(dep_id, path[:], visited)

        return False

    visited_global = set()
    for skill_id in skills:
        if skill_id not in visited_global:
            find_cycle(skill_id, [], visited_global)

    return cycles

def check_missing_dependencies(skills: Dict[str, Dict]) -> List[str]:
    """Check for dependencies that reference non-existent skills."""
    missing = []

    for skill_id, skill_data in skills.items():
        for dep_id in skill_data['dependencies']:
            if dep_id not in skills:
                missing.append(f"{skill_id} -> {dep_id} (does not exist)")

    return missing

def count_grade_k_changes(skills: Dict[str, Dict]) -> Dict:
    """Count dependencies for Grade K skills."""
    grade_k_skills = {sid: data for sid, data in skills.items() if '.GK.' in sid}

    cross_topic_deps = 0
    within_topic_deps = 0

    for skill_id, skill_data in grade_k_skills.items():
        skill_topic = skill_id.split('.')[0]

        for dep_id in skill_data['dependencies']:
            dep_topic = dep_id.split('.')[0]

            if dep_topic != skill_topic:
                cross_topic_deps += 1
            else:
                within_topic_deps += 1

    return {
        'total_grade_k_skills': len(grade_k_skills),
        'cross_topic_dependencies': cross_topic_deps,
        'within_topic_dependencies': within_topic_deps,
        'total_dependencies': cross_topic_deps + within_topic_deps
    }

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills file...")
    skills = parse_skills(filepath)
    print(f"Total skills parsed: {len(skills)}")

    print("\n=== VALIDATION RESULTS ===\n")

    # Check X-2 rule
    print("1. Checking X-2 Rule Violations...")
    x2_violations = check_x2_rule(skills)
    if x2_violations:
        print(f"   FOUND {len(x2_violations)} VIOLATIONS:")
        for violation in x2_violations:
            print(f"   - {violation}")
    else:
        print("   ✓ No X-2 rule violations found")

    # Check circular dependencies
    print("\n2. Checking Circular Dependencies...")
    cycles = find_circular_dependencies(skills)
    if cycles:
        print(f"   FOUND {len(cycles)} CYCLES:")
        for cycle in cycles:
            print(f"   - {' -> '.join(cycle)}")
    else:
        print("   ✓ No circular dependencies found")

    # Check missing dependencies
    print("\n3. Checking Missing Dependencies...")
    missing = check_missing_dependencies(skills)
    if missing:
        print(f"   FOUND {len(missing)} MISSING:")
        for m in missing:
            print(f"   - {m}")
    else:
        print("   ✓ All dependency IDs exist")

    # Count Grade K changes
    print("\n4. Grade K Dependency Statistics...")
    stats = count_grade_k_changes(skills)
    print(f"   Total Grade K Skills: {stats['total_grade_k_skills']}")
    print(f"   Cross-Topic Dependencies: {stats['cross_topic_dependencies']}")
    print(f"   Within-Topic Dependencies: {stats['within_topic_dependencies']}")
    print(f"   Total Dependencies: {stats['total_dependencies']}")

    # Overall result
    print("\n=== OVERALL VALIDATION ===")
    all_valid = (len(x2_violations) == 0 and len(cycles) == 0 and len(missing) == 0)
    if all_valid:
        print("✓ ALL VALIDATIONS PASSED")
        return True
    else:
        print("✗ VALIDATION FAILED")
        return False

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
