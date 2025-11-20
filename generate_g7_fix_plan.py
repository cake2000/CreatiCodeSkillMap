#!/usr/bin/env python3
"""
Generate fix plan for Grade 7 skills with low-grade dependencies.
Identifies G7 skills that depend on G3/G2/G1 and finds G5/G6/G7 replacements.
"""

import re
import json
from collections import defaultdict

def parse_skills_file(filepath):
    """Parse the allskills.md file and extract all skills."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}

    # Split by ID: pattern
    skill_blocks = re.split(r'\n(?=ID: T\d+\.G)', content)

    for block in skill_blocks:
        if not block.strip():
            continue

        # Extract skill ID
        id_match = re.search(r'ID:\s*(T\d+\.G\d+\.\d+)', block)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract skill name
        skill_match = re.search(r'Skill:\s*(.+)', block)
        title = skill_match.group(1).strip() if skill_match else ''

        # Extract dependencies
        deps = []
        dep_section = re.search(r'Dependencies:\s*\n((?:\*.*\n)*)', block)
        if dep_section:
            dep_text = dep_section.group(1)
            deps = re.findall(r'T\d+\.G\d+\.\d+', dep_text)

        skills[skill_id] = {
            'id': skill_id,
            'title': title,
            'body': block,
            'dependencies': deps,
            'full_text': block
        }

    return skills

def get_grade(skill_id):
    """Extract grade number from skill ID."""
    match = re.search(r'\.G(\d+)\.', skill_id)
    return int(match.group(1)) if match else 0

def get_topic(skill_id):
    """Extract topic from skill ID."""
    match = re.search(r'(T\d+)\.', skill_id)
    return match.group(1) if match else ''

def find_replacement(dep_id, skills, allowed_grades=[5, 6, 7]):
    """Find a suitable replacement for a low-grade dependency."""
    topic = get_topic(dep_id)
    dep_grade = get_grade(dep_id)

    # Get the skill number
    match = re.search(r'\.G\d+\.(\d+)', dep_id)
    skill_num = match.group(1) if match else '01'

    # Find candidates in the same topic with allowed grades
    candidates = []
    for allowed_grade in sorted(allowed_grades):
        candidate_id = f"{topic}.G{allowed_grade}.{skill_num}"
        if candidate_id in skills:
            candidates.append(candidate_id)

    # If no exact match, find any skill in same topic with allowed grade
    if not candidates:
        for skill_id in skills:
            if get_topic(skill_id) == topic and get_grade(skill_id) in allowed_grades:
                candidates.append(skill_id)

    # Return the closest grade match
    return candidates[0] if candidates else None

def analyze_g7_skills(skills):
    """Analyze G7 skills and create fix plan."""
    g7_skills = {sid: s for sid, s in skills.items() if get_grade(sid) == 7}

    print(f"Total G7 skills: {len(g7_skills)}")

    issues = []
    fix_plan = {}
    stats = {
        'total_g7_skills': len(g7_skills),
        'skills_with_low_deps': 0,
        'low_deps_found': 0,
        'g3_deps': 0,
        'g2_deps': 0,
        'g1_deps': 0,
        'replacements_found': 0,
        'replacements_missing': 0
    }

    for skill_id, skill in g7_skills.items():
        low_grade_deps = []
        replacement_map = {}

        for dep in skill['dependencies']:
            dep_grade = get_grade(dep)

            if dep_grade in [1, 2, 3]:
                low_grade_deps.append(dep)
                stats['low_deps_found'] += 1

                if dep_grade == 1:
                    stats['g1_deps'] += 1
                elif dep_grade == 2:
                    stats['g2_deps'] += 1
                elif dep_grade == 3:
                    stats['g3_deps'] += 1

                # Find replacement
                replacement = find_replacement(dep, skills, [5, 6, 7])

                if replacement:
                    replacement_map[dep] = replacement
                    stats['replacements_found'] += 1
                else:
                    replacement_map[dep] = None
                    stats['replacements_missing'] += 1

                issues.append({
                    'skill_id': skill_id,
                    'skill_title': skill['title'],
                    'low_grade_dep': dep,
                    'dep_grade': dep_grade,
                    'replacement': replacement
                })

        if low_grade_deps:
            stats['skills_with_low_deps'] += 1
            fix_plan[skill_id] = {
                'title': skill['title'],
                'original_deps': skill['dependencies'],
                'low_grade_deps': low_grade_deps,
                'replacement_map': replacement_map
            }

    return fix_plan, issues, stats

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("=" * 80)
    print("G7 FIX PLAN GENERATOR")
    print("=" * 80)
    print()

    # Parse skills
    print("Parsing skills file...")
    skills = parse_skills_file(filepath)
    print(f"Total skills parsed: {len(skills)}")
    print()

    # Analyze G7 skills
    print("Analyzing G7 skills for low-grade dependencies...")
    fix_plan, issues, stats = analyze_g7_skills(skills)
    print()

    # Print statistics
    print("=" * 80)
    print("STATISTICS")
    print("=" * 80)
    print(f"Total G7 skills: {stats['total_g7_skills']}")
    print(f"G7 skills with low-grade dependencies: {stats['skills_with_low_deps']}")
    print(f"Total low-grade dependencies found: {stats['low_deps_found']}")
    print(f"  - G1 dependencies: {stats['g1_deps']}")
    print(f"  - G2 dependencies: {stats['g2_deps']}")
    print(f"  - G3 dependencies: {stats['g3_deps']}")
    print(f"Replacements found: {stats['replacements_found']}")
    print(f"Replacements missing: {stats['replacements_missing']}")
    print()

    # Save fix plan
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G7_FIX_PLAN.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump({
            'fix_plan': fix_plan,
            'issues': issues,
            'statistics': stats
        }, f, indent=2)

    print(f"Fix plan saved to: {output_file}")
    print()

    # Generate summary report
    report_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G7_FIX_PLAN_SUMMARY.md'
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("# Grade 7 Fix Plan Summary\n\n")
        f.write(f"**Generated:** {stats['total_g7_skills']} G7 skills analyzed\n\n")

        f.write("## Overview\n\n")
        f.write(f"- **Total G7 skills:** {stats['total_g7_skills']}\n")
        f.write(f"- **Skills requiring fixes:** {stats['skills_with_low_deps']}\n")
        f.write(f"- **Total low-grade dependencies:** {stats['low_deps_found']}\n")
        f.write(f"  - G1: {stats['g1_deps']}\n")
        f.write(f"  - G2: {stats['g2_deps']}\n")
        f.write(f"  - G3: {stats['g3_deps']}\n")
        f.write(f"- **Replacements found:** {stats['replacements_found']}\n")
        f.write(f"- **Replacements missing:** {stats['replacements_missing']}\n\n")

        f.write("## Skills Requiring Fixes\n\n")

        for skill_id, plan in sorted(fix_plan.items()):
            f.write(f"### {skill_id}: {plan['title']}\n\n")
            f.write(f"**Original dependencies:** {', '.join(plan['original_deps'])}\n\n")
            f.write(f"**Low-grade dependencies to replace:**\n\n")

            for old_dep, new_dep in plan['replacement_map'].items():
                if new_dep:
                    f.write(f"- {old_dep} → {new_dep}\n")
                else:
                    f.write(f"- {old_dep} → ⚠️ NO REPLACEMENT FOUND\n")

            f.write("\n")

        f.write("## Replacement Details\n\n")
        f.write("| G7 Skill | Low-Grade Dep | Grade | Replacement | Status |\n")
        f.write("|----------|---------------|-------|-------------|--------|\n")

        for issue in issues:
            status = "✓" if issue['replacement'] else "✗"
            replacement = issue['replacement'] if issue['replacement'] else "NOT FOUND"
            f.write(f"| {issue['skill_id']} | {issue['low_grade_dep']} | G{issue['dep_grade']} | {replacement} | {status} |\n")

    print(f"Summary report saved to: {report_file}")
    print()

    # Print sample of issues
    print("=" * 80)
    print("SAMPLE ISSUES (first 10)")
    print("=" * 80)
    for i, issue in enumerate(issues[:10], 1):
        replacement = issue['replacement'] if issue['replacement'] else "NOT FOUND"
        print(f"{i}. {issue['skill_id']} - {issue['low_grade_dep']} (G{issue['dep_grade']}) → {replacement}")

    if len(issues) > 10:
        print(f"... and {len(issues) - 10} more")

    print()
    print("=" * 80)
    print("COMPLETE - Fix plan generated successfully!")
    print("=" * 80)

if __name__ == '__main__':
    main()
