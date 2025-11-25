#!/usr/bin/env python3
"""Extract and analyze all Grade 7 skills from allskills.md"""

import re
from collections import defaultdict

def extract_grade7_skills(filename):
    """Extract all Grade 7 skills with their complete information"""

    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries
    # A skill starts with "ID: " and continues until the next "ID: " or major section
    skills = []
    current_skill = None
    in_g7_skill = False

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this is a Grade 7 skill ID
        if line.startswith('ID: ') and '.G7.' in line:
            # Save previous skill if exists
            if current_skill:
                skills.append(current_skill)

            # Start new skill
            current_skill = {'id': line.replace('ID: ', '').strip(), 'raw_lines': [line]}
            in_g7_skill = True
            i += 1
            continue

        # If we're in a G7 skill, keep collecting lines
        if in_g7_skill:
            # Stop conditions
            if line.startswith('ID: ') and '.G7.' not in line:
                # Next skill is not G7, save current and stop
                if current_skill:
                    skills.append(current_skill)
                current_skill = None
                in_g7_skill = False
            elif line.startswith('## ') or line.startswith('---'):
                # Section boundary
                if current_skill:
                    skills.append(current_skill)
                current_skill = None
                in_g7_skill = False
            else:
                # Add line to current skill
                if current_skill:
                    current_skill['raw_lines'].append(line)

        i += 1

    # Don't forget last skill
    if current_skill and in_g7_skill:
        skills.append(current_skill)

    # Parse each skill's details
    parsed_skills = []
    for skill in skills:
        parsed = parse_skill_details(skill)
        if parsed:
            parsed_skills.append(parsed)

    return parsed_skills

def parse_skill_details(skill):
    """Parse skill details from raw lines"""

    parsed = {'id': skill['id']}
    raw_text = '\n'.join(skill['raw_lines'])

    # Extract Topic
    topic_match = re.search(r'^Topic:\s*(.+)$', raw_text, re.MULTILINE)
    if topic_match:
        parsed['topic'] = topic_match.group(1).strip()

    # Extract Skill name
    skill_match = re.search(r'^Skill:\s*(.+)$', raw_text, re.MULTILINE)
    if skill_match:
        parsed['skill'] = skill_match.group(1).strip()

    # Extract Description
    desc_match = re.search(r'^Description:\s*(.+?)(?=\n\n|\nDependencies:|\nAlternative|\nGrade:|\Z)',
                           raw_text, re.MULTILINE | re.DOTALL)
    if desc_match:
        parsed['description'] = desc_match.group(1).strip()

    # Extract Dependencies
    deps_match = re.search(r'^Dependencies:\s*\n((?:\*.+\n?)+)', raw_text, re.MULTILINE)
    if deps_match:
        deps_text = deps_match.group(1)
        deps = re.findall(r'^\*\s*(.+)$', deps_text, re.MULTILINE)
        parsed['dependencies'] = [d.strip() for d in deps]
    else:
        # Check for "Dependencies: None" or similar
        if 'Dependencies: None' in raw_text or 'Dependencies:\nNone' in raw_text:
            parsed['dependencies'] = []
        else:
            parsed['dependencies'] = []

    # Extract Grade if present
    grade_match = re.search(r'^Grade:\s*(\d+)$', raw_text, re.MULTILINE)
    if grade_match:
        parsed['grade'] = grade_match.group(1)
    else:
        parsed['grade'] = '7'  # Default to 7 for G7 skills

    return parsed

def analyze_skills(skills):
    """Analyze and group skills by topic"""

    by_topic = defaultdict(list)
    all_deps = set()

    for skill in skills:
        topic = skill.get('topic', 'Unknown')
        by_topic[topic].append(skill)

        # Collect all dependencies
        for dep in skill.get('dependencies', []):
            all_deps.add(dep)

    return by_topic, all_deps

def write_analysis(skills, output_file):
    """Write comprehensive analysis to file"""

    by_topic, all_deps = analyze_skills(skills)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# GRADE 7 SKILLS COMPREHENSIVE ANALYSIS\n")
        f.write(f"# Generated from allskills.md\n")
        f.write(f"# Total Grade 7 Skills: {len(skills)}\n\n")

        f.write("=" * 80 + "\n")
        f.write("SUMMARY STATISTICS\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"Total Grade 7 Skills: {len(skills)}\n")
        f.write(f"Number of Topics: {len(by_topic)}\n")
        f.write(f"Total Unique Dependencies: {len(all_deps)}\n\n")

        f.write("Skills by Topic:\n")
        for topic in sorted(by_topic.keys()):
            f.write(f"  {topic}: {len(by_topic[topic])} skills\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("SKILLS BY TOPIC (DETAILED)\n")
        f.write("=" * 80 + "\n\n")

        for topic in sorted(by_topic.keys()):
            f.write(f"\n{'#' * 80}\n")
            f.write(f"# TOPIC: {topic}\n")
            f.write(f"# Count: {len(by_topic[topic])} skills\n")
            f.write(f"{'#' * 80}\n\n")

            for skill in sorted(by_topic[topic], key=lambda x: x['id']):
                f.write(f"ID: {skill['id']}\n")
                f.write(f"Topic: {skill.get('topic', 'N/A')}\n")
                f.write(f"Skill: {skill.get('skill', 'N/A')}\n")
                f.write(f"Description: {skill.get('description', 'N/A')}\n")

                if skill.get('dependencies'):
                    f.write(f"\nDependencies ({len(skill['dependencies'])}):\n")
                    for dep in skill['dependencies']:
                        f.write(f"  * {dep}\n")
                else:
                    f.write(f"\nDependencies: None\n")

                f.write("\n" + "-" * 80 + "\n\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("ALL GRADE 7 SKILL IDs (Sorted)\n")
        f.write("=" * 80 + "\n\n")

        for skill in sorted(skills, key=lambda x: x['id']):
            f.write(f"{skill['id']}: {skill.get('skill', 'N/A')}\n")

        f.write("\n" + "=" * 80 + "\n")
        f.write("DEPENDENCY ANALYSIS\n")
        f.write("=" * 80 + "\n\n")

        # Count dependencies per skill
        dep_counts = defaultdict(int)
        for skill in skills:
            dep_counts[len(skill.get('dependencies', []))] += 1

        f.write("Dependency Count Distribution:\n")
        for count in sorted(dep_counts.keys()):
            f.write(f"  {count} dependencies: {dep_counts[count]} skills\n")

        f.write("\n\nSkills with NO dependencies:\n")
        for skill in sorted(skills, key=lambda x: x['id']):
            if not skill.get('dependencies'):
                f.write(f"  {skill['id']}: {skill.get('skill', 'N/A')}\n")

        f.write("\n\nSkills with MOST dependencies (top 10):\n")
        sorted_by_deps = sorted(skills, key=lambda x: len(x.get('dependencies', [])), reverse=True)
        for skill in sorted_by_deps[:10]:
            dep_count = len(skill.get('dependencies', []))
            f.write(f"  {skill['id']}: {dep_count} deps - {skill.get('skill', 'N/A')}\n")

if __name__ == '__main__':
    input_file = 'allskills.md'
    output_file = 'GRADE7_COMPLETE_ANALYSIS.md'

    print(f"Extracting Grade 7 skills from {input_file}...")
    skills = extract_grade7_skills(input_file)

    print(f"Found {len(skills)} Grade 7 skills")
    print(f"Writing analysis to {output_file}...")

    write_analysis(skills, output_file)

    print(f"Analysis complete! See {output_file}")
