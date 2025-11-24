#!/usr/bin/env python3
"""
Extract all Grade 1 skills with their dependencies from allskills.md
Also extract Grade K skills for reference
"""

import re
from collections import defaultdict

def parse_allskills():
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into skills by looking for "ID:" markers
    skill_blocks = re.split(r'\n\n+(?=ID:)', content)

    grade_k_skills = {}
    grade_1_skills = {}

    for block in skill_blocks:
        # Extract skill ID
        id_match = re.search(r'^ID:\s*(T\d+\.(?:GK|K|G1|G2)\.\d+)', block, re.MULTILINE)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract title/skill name
        skill_match = re.search(r'^Skill:\s*(.+?)$', block, re.MULTILINE)
        title = skill_match.group(1).strip() if skill_match else "Unknown"

        # Extract dependencies
        dependencies = []
        deps_section = re.search(r'^Dependencies:\s*\n((?:\*\s+.+\n?)+)', block, re.MULTILINE)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'(T\d+\.(?:GK|K|G1|G2)\.\d+)', line)
                if dep_match:
                    dependencies.append(dep_match.group(1))

        skill_info = {
            'id': skill_id,
            'title': title,
            'dependencies': dependencies,
            'topic': skill_id.split('.')[0]
        }

        if '.GK.' in skill_id or re.match(r'T\d+\.K\.\d+', skill_id):
            grade_k_skills[skill_id] = skill_info
        elif '.G1.' in skill_id:
            grade_1_skills[skill_id] = skill_info

    return grade_k_skills, grade_1_skills

def analyze_dependencies(grade_k_skills, grade_1_skills):
    """Analyze dependency patterns for Grade 1 skills"""

    # Group by topic
    topics = defaultdict(list)
    for skill_id, skill in grade_1_skills.items():
        topics[skill['topic']].append(skill)

    output = []
    output.append("=" * 80)
    output.append("GRADE 1 SKILLS DEPENDENCY ANALYSIS")
    output.append("=" * 80)
    output.append("")

    # Summary statistics
    total_g1_skills = len(grade_1_skills)
    total_grade_k = len(grade_k_skills)
    output.append(f"Total Grade K skills: {total_grade_k}")
    output.append(f"Total Grade 1 skills: {total_g1_skills}")
    output.append("")

    # List all Grade K skills for reference
    output.append("=" * 80)
    output.append("AVAILABLE GRADE K SKILLS (Valid Dependencies)")
    output.append("=" * 80)
    output.append("")

    gk_by_topic = defaultdict(list)
    for skill_id, skill in sorted(grade_k_skills.items()):
        gk_by_topic[skill['topic']].append(skill)

    for topic in sorted(gk_by_topic.keys()):
        output.append(f"\n{topic} - Grade K Skills:")
        output.append("-" * 60)
        for skill in gk_by_topic[topic]:
            output.append(f"  {skill['id']}: {skill['title']}")

    output.append("")
    output.append("=" * 80)
    output.append("GRADE 1 SKILLS WITH DEPENDENCIES")
    output.append("=" * 80)
    output.append("")

    # Detailed analysis by topic
    for topic in sorted(topics.keys()):
        skills = sorted(topics[topic], key=lambda x: x['id'])
        output.append(f"\n{'=' * 80}")
        output.append(f"TOPIC {topic}")
        output.append(f"{'=' * 80}")
        output.append(f"Total Grade 1 skills in {topic}: {len(skills)}")
        output.append("")

        for skill in skills:
            output.append(f"\n{skill['id']}: {skill['title']}")
            output.append("-" * 60)

            if not skill['dependencies']:
                output.append("  Dependencies: None")
            else:
                output.append(f"  Dependencies ({len(skill['dependencies'])}):")

                same_topic_gk = []
                same_topic_g1 = []
                cross_topic_gk = []
                cross_topic_g1 = []
                invalid = []

                for dep in skill['dependencies']:
                    dep_topic = dep.split('.')[0]
                    is_same_topic = (dep_topic == skill['topic'])

                    # Check if it's Grade K or Grade 1
                    if '.GK.' in dep or re.match(r'T\d+\.K\.\d+', dep):
                        # Grade K dependency
                        if dep in grade_k_skills:
                            if is_same_topic:
                                same_topic_gk.append(dep)
                            else:
                                cross_topic_gk.append(dep)
                        else:
                            invalid.append(dep)
                    elif '.G1.' in dep:
                        # Grade 1 dependency
                        if dep in grade_1_skills:
                            if is_same_topic:
                                same_topic_g1.append(dep)
                            else:
                                cross_topic_g1.append(dep)
                        else:
                            invalid.append(dep)
                    else:
                        invalid.append(dep)

                if same_topic_gk:
                    output.append(f"    Same Topic Grade K ({len(same_topic_gk)}):")
                    for dep in same_topic_gk:
                        dep_title = grade_k_skills[dep]['title'] if dep in grade_k_skills else "Unknown"
                        output.append(f"      - {dep}: {dep_title}")

                if same_topic_g1:
                    output.append(f"    Same Topic Grade 1 ({len(same_topic_g1)}):")
                    for dep in same_topic_g1:
                        dep_title = grade_1_skills[dep]['title'] if dep in grade_1_skills else "Unknown"
                        output.append(f"      - {dep}: {dep_title}")

                if cross_topic_gk:
                    output.append(f"    Cross-Topic Grade K ({len(cross_topic_gk)}):")
                    for dep in cross_topic_gk:
                        dep_title = grade_k_skills[dep]['title'] if dep in grade_k_skills else "Unknown"
                        output.append(f"      - {dep}: {dep_title}")

                if cross_topic_g1:
                    output.append(f"    Cross-Topic Grade 1 ({len(cross_topic_g1)}):")
                    for dep in cross_topic_g1:
                        dep_title = grade_1_skills[dep]['title'] if dep in grade_1_skills else "Unknown"
                        output.append(f"      - {dep}: {dep_title}")

                if invalid:
                    output.append(f"    INVALID/MISSING ({len(invalid)}):")
                    for dep in invalid:
                        output.append(f"      - {dep}")

    # Summary statistics
    output.append("")
    output.append("=" * 80)
    output.append("SUMMARY STATISTICS")
    output.append("=" * 80)
    output.append("")

    total_deps = 0
    same_topic_gk_count = 0
    same_topic_g1_count = 0
    cross_topic_gk_count = 0
    cross_topic_g1_count = 0
    invalid_count = 0
    skills_with_no_deps = 0

    for skill_id, skill in grade_1_skills.items():
        if not skill['dependencies']:
            skills_with_no_deps += 1
            continue

        total_deps += len(skill['dependencies'])

        for dep in skill['dependencies']:
            dep_topic = dep.split('.')[0]
            is_same_topic = (dep_topic == skill['topic'])

            if '.GK.' in dep or re.match(r'T\d+\.K\.\d+', dep):
                if dep in grade_k_skills:
                    if is_same_topic:
                        same_topic_gk_count += 1
                    else:
                        cross_topic_gk_count += 1
                else:
                    invalid_count += 1
            elif '.G1.' in dep:
                if dep in grade_1_skills:
                    if is_same_topic:
                        same_topic_g1_count += 1
                    else:
                        cross_topic_g1_count += 1
                else:
                    invalid_count += 1
            else:
                invalid_count += 1

    output.append(f"Total Grade 1 skills: {total_g1_skills}")
    output.append(f"Skills with no dependencies: {skills_with_no_deps}")
    output.append(f"Skills with dependencies: {total_g1_skills - skills_with_no_deps}")
    output.append(f"Total dependencies: {total_deps}")
    output.append("")
    output.append("Dependency Breakdown:")
    output.append(f"  Same Topic Grade K: {same_topic_gk_count}")
    output.append(f"  Same Topic Grade 1: {same_topic_g1_count}")
    output.append(f"  Cross-Topic Grade K: {cross_topic_gk_count}")
    output.append(f"  Cross-Topic Grade 1: {cross_topic_g1_count}")
    output.append(f"  Invalid/Missing: {invalid_count}")

    return "\n".join(output)

def main():
    print("Parsing allskills.md...")
    grade_k_skills, grade_1_skills = parse_allskills()

    print(f"Found {len(grade_k_skills)} Grade K skills")
    print(f"Found {len(grade_1_skills)} Grade 1 skills")

    print("Analyzing dependencies...")
    report = analyze_dependencies(grade_k_skills, grade_1_skills)

    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE_1_ANALYSIS.md'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nAnalysis complete! Report saved to: {output_file}")
    print("\nPreview:")
    print("=" * 80)
    print(report[:2000])
    print("...")

if __name__ == '__main__':
    main()
