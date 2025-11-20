#!/usr/bin/env python3
"""
Generate comprehensive fix plan for Grade 6 skills.
Removes dependencies on G3, G2, G1, GK and transitive dependencies.
"""

import re
import json
from collections import defaultdict

def parse_skills_file(filepath):
    """Parse the allskills.md file and extract all skills with dependencies."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries
    skill_pattern = r'ID: (T\d+\.[A-Z0-9]+\.\d+)\n'
    skills = {}
    skill_blocks = re.split(skill_pattern, content)

    # Process pairs of (skill_id, skill_content)
    for i in range(1, len(skill_blocks), 2):
        if i + 1 < len(skill_blocks):
            skill_id = skill_blocks[i]
            skill_content = skill_blocks[i + 1]

            # Extract topic
            topic_match = re.search(r'Topic: (.+)', skill_content)
            topic = topic_match.group(1) if topic_match else ""

            # Extract skill name
            skill_match = re.search(r'Skill: (.+)', skill_content)
            skill_name = skill_match.group(1) if skill_match else ""

            # Extract dependencies
            deps = []
            dep_section = re.search(r'Dependencies:\n((?:\* .+\n?)+)', skill_content)
            if dep_section:
                dep_lines = dep_section.group(1).strip().split('\n')
                for line in dep_lines:
                    # Extract skill ID from dependency line
                    dep_match = re.search(r'\* (T\d+\.[A-Z0-9]+\.\d+):', line)
                    if dep_match:
                        deps.append(dep_match.group(1))

            skills[skill_id] = {
                'topic': topic,
                'name': skill_name,
                'dependencies': deps
            }

    return skills

def get_grade_level(skill_id):
    """Extract grade level from skill ID (e.g., T01.G6.01 -> G6)."""
    match = re.search(r'\.([A-Z0-9]+)\.\d+$', skill_id)
    return match.group(1) if match else None

def get_topic_number(skill_id):
    """Extract topic number from skill ID (e.g., T01.G6.01 -> T01)."""
    match = re.search(r'^(T\d+)\.', skill_id)
    return match.group(1) if match else None

def get_skill_number(skill_id):
    """Extract skill number from skill ID (e.g., T01.G6.01 -> 01)."""
    match = re.search(r'\.(\d+)$', skill_id)
    return int(match.group(1)) if match else 0

def is_lower_grade(dep_grade):
    """Check if dependency is on a lower grade (G3, G2, G1, GK)."""
    return dep_grade in ['G3', 'G2', 'G1', 'GK']

def find_transitive_dependencies(skill_id, all_skills, visited=None):
    """Find all transitive dependencies for a skill."""
    if visited is None:
        visited = set()

    if skill_id in visited or skill_id not in all_skills:
        return set()

    visited.add(skill_id)
    transitive = set()

    # Get direct dependencies
    direct_deps = all_skills[skill_id]['dependencies']

    # For each direct dependency, get its dependencies (transitive)
    for dep in direct_deps:
        if dep in all_skills:
            # Add all dependencies of this dependency
            dep_deps = all_skills[dep]['dependencies']
            transitive.update(dep_deps)
            # Recursively find transitive dependencies
            transitive.update(find_transitive_dependencies(dep, all_skills, visited.copy()))

    return transitive

def is_sequential_in_same_topic(skill_id, dep_id):
    """
    Check if dependency is a sequential skill in the same topic/grade.
    These are assumed to be sequential and don't need explicit dependency.
    """
    skill_topic = get_topic_number(skill_id)
    skill_grade = get_grade_level(skill_id)
    skill_num = get_skill_number(skill_id)

    dep_topic = get_topic_number(dep_id)
    dep_grade = get_grade_level(dep_id)
    dep_num = get_skill_number(dep_id)

    # If same topic, same grade, and earlier in sequence
    if skill_topic == dep_topic and skill_grade == dep_grade and dep_num < skill_num:
        return True

    return False

def generate_fix_plan(all_skills):
    """Generate fix plan for all G6 skills."""
    fix_plan = {}

    # Filter G6 skills only
    g6_skills = {sid: sdata for sid, sdata in all_skills.items()
                 if get_grade_level(sid) == 'G6'}

    print(f"Processing {len(g6_skills)} Grade 6 skills...")

    for skill_id, skill_data in g6_skills.items():
        old_deps = skill_data['dependencies'].copy()
        new_deps = []
        issues_fixed = []

        # Find all transitive dependencies
        transitive_deps = find_transitive_dependencies(skill_id, all_skills)

        # Process each dependency
        for dep_id in old_deps:
            dep_grade = get_grade_level(dep_id)

            # Issue 1: Dependency on lower grades (G3, G2, G1, GK)
            if is_lower_grade(dep_grade):
                issues_fixed.append(f"REMOVED lower grade dependency on {dep_id} ({dep_grade})")
                continue

            # Issue 2: Transitive dependency
            if dep_id in transitive_deps:
                issues_fixed.append(f"REMOVED transitive dependency on {dep_id}")
                continue

            # Issue 3: Sequential skill in same topic/grade
            if is_sequential_in_same_topic(skill_id, dep_id):
                issues_fixed.append(f"REMOVED sequential dependency on {dep_id} (same topic/grade, earlier skill)")
                continue

            # Keep this dependency
            new_deps.append(dep_id)

        # Only add to fix plan if there are changes
        if old_deps != new_deps or issues_fixed:
            fix_plan[skill_id] = {
                'skill_name': skill_data['name'],
                'topic': skill_data['topic'],
                'old_dependencies': old_deps,
                'new_dependencies': new_deps,
                'issues_fixed': issues_fixed
            }

    return fix_plan

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G6_FIX_PLAN.json'

    print("Parsing skills file...")
    all_skills = parse_skills_file(filepath)
    print(f"Found {len(all_skills)} total skills")

    # Count skills by grade
    grade_counts = defaultdict(int)
    for sid in all_skills:
        grade = get_grade_level(sid)
        grade_counts[grade] += 1

    print("\nSkills by grade:")
    for grade in sorted(grade_counts.keys()):
        print(f"  {grade}: {grade_counts[grade]}")

    print("\nGenerating fix plan for G6 skills...")
    fix_plan = generate_fix_plan(all_skills)

    # Calculate statistics
    total_g6_with_changes = len(fix_plan)
    total_old_deps = sum(len(v['old_dependencies']) for v in fix_plan.values())
    total_new_deps = sum(len(v['new_dependencies']) for v in fix_plan.values())
    total_removed = total_old_deps - total_new_deps

    # Count issue types
    lower_grade_fixes = sum(1 for v in fix_plan.values()
                           for issue in v['issues_fixed']
                           if 'lower grade' in issue)
    transitive_fixes = sum(1 for v in fix_plan.values()
                          for issue in v['issues_fixed']
                          if 'transitive' in issue)
    sequential_fixes = sum(1 for v in fix_plan.values()
                          for issue in v['issues_fixed']
                          if 'sequential' in issue)

    print(f"\n=== Fix Plan Statistics ===")
    print(f"G6 skills with changes: {total_g6_with_changes}")
    print(f"Total dependencies removed: {total_removed}")
    print(f"  - Lower grade (G3/G2/G1/GK): {lower_grade_fixes}")
    print(f"  - Transitive dependencies: {transitive_fixes}")
    print(f"  - Sequential in same topic: {sequential_fixes}")
    print(f"Old total dependencies: {total_old_deps}")
    print(f"New total dependencies: {total_new_deps}")

    # Save fix plan
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(fix_plan, f, indent=2, ensure_ascii=False)

    print(f"\nFix plan saved to: {output_file}")

    # Show some examples
    print("\n=== Example Fixes (first 5 skills with changes) ===")
    for i, (skill_id, data) in enumerate(list(fix_plan.items())[:5]):
        print(f"\n{skill_id}: {data['skill_name']}")
        print(f"  Old deps ({len(data['old_dependencies'])}): {data['old_dependencies']}")
        print(f"  New deps ({len(data['new_dependencies'])}): {data['new_dependencies']}")
        print(f"  Issues fixed:")
        for issue in data['issues_fixed']:
            print(f"    - {issue}")

if __name__ == '__main__':
    main()
