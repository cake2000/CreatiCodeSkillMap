#!/usr/bin/env python3
"""
Apply cross-topic dependency additions to Grade 3 skills in allskills.md
"""

import re

# Define all dependencies to add
DEPENDENCIES_TO_ADD = [
    # Topics T01-T12
    ("T04.G3.04.02", "T09.G3.01.01", "Create a new variable with a descriptive name"),
    ("T04.G3.08", "T09.G3.01.01", "Create a new variable with a descriptive name"),
    ("T12.G3.03.01", "T09.G3.01.01", "Create a new variable with a descriptive name"),
    ("T12.G3.03.04", "T09.G3.01.01", "Create a new variable with a descriptive name"),
    ("T02.G3.04", "T08.G3.01", "Use a simple if in a script"),
    ("T02.G3.05", "T08.G3.01", "Use a simple if in a script"),
    ("T01.G3.16", "T08.G3.01", "Use a simple if in a script"),

    # Topics T13-T24 (KEY additions)
    ("T14.G3.01.01", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T14.G3.01.02", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T14.G3.03", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T14.G3.04.01", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T14.G3.05", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T14.G3.06", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T14.G3.07", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T14.G3.08", "T09.G2.02", "Compare a counter to a target number to trigger an event"),
    ("T14.G3.09", "T09.G2.02", "Compare a counter to a target number to trigger an event"),
    ("T14.G3.10", "T09.G2.02", "Compare a counter to a target number to trigger an event"),
    ("T14.G3.11", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T15.G3.02", "T07.G2.01", "Identify when to use \"repeat\" vs \"do once\""),
    ("T15.G3.09", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T15.G3.11.02", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T15.G3.12", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T15.G3.12.01", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T16.G3.02.01", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T16.G3.04", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T16.G3.04.01", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T16.G3.05", "T09.G2.02", "Compare a counter to a target number to trigger an event"),
    ("T16.G3.06", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T16.G3.07", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T16.G3.07.01", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T16.G3.08", "T09.G2.02", "Compare a counter to a target number to trigger an event"),
    ("T18.G3.03", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T18.G3.05", "T06.G2.03", "Design a simple \"if-then\" game rule"),
    ("T18.G3.07", "T07.G2.01", "Identify when to use \"repeat\" vs \"do once\""),
    ("T18.G3.08", "T09.G2.02", "Compare a counter to a target number to trigger an event"),
    ("T20.G3.02", "T07.G2.01", "Identify when to use \"repeat\" vs \"do once\""),
    ("T20.G3.05.01", "T07.G2.01", "Identify when to use \"repeat\" vs \"do once\""),
    ("T22.G3.02", "T10.G2.01", "Read and write data to a simple table"),
    ("T23.G3.03", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T24.G3.00", "T10.G2.01", "Read and write data to a simple table"),
    ("T24.G3.01", "T10.G2.01", "Read and write data to a simple table"),
    ("T24.G3.02", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T24.G3.03", "T10.G2.01", "Read and write data to a simple table"),

    # Topics T25-T36 (KEY additions)
    ("T25.G3.02.01", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T25.G3.05", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T26.G3.04.02", "T07.G2.01", "Identify when to use \"repeat\" vs \"do once\""),
    ("T27.G3.01c", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T27.G3.05", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T28.G3.02", "T09.G2.02", "Compare a counter to a target number to trigger an event"),
    ("T28.G3.03", "T07.G2.01", "Identify when to use \"repeat\" vs \"do once\""),
    ("T28.G3.04", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T28.G3.07", "T07.G2.01", "Identify when to use \"repeat\" vs \"do once\""),
    ("T29.G3.02", "T07.G2.01", "Identify when to use \"repeat\" vs \"do once\""),
    ("T29.G3.04", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T29.G3.05", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T30.G3.02", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T30.G3.03", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T30.G3.05", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T30.G3.06", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T32.G3.02", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T32.G3.04", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T32.G3.05", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T35.G3.04", "T08.G2.03", "Identify which rule applies in a situation"),
    ("T36.G3.02", "T08.G2.03", "Identify which rule applies in a situation"),
]


def parse_skills(content):
    """Parse the markdown file and extract skills as blocks"""
    # Split by skill ID pattern
    skill_pattern = r'\n(ID: T\d+\.G\d+\.\d+(?:\.\d+)?[a-z]?)\n'
    parts = re.split(skill_pattern, content)

    # Reconstruct skills
    skills = {}
    if parts[0].strip():  # Header before first skill
        header = parts[0]
    else:
        header = ""

    for i in range(1, len(parts), 2):
        if i + 1 < len(parts):
            skill_id_line = parts[i]
            skill_id = skill_id_line.replace("ID: ", "").strip()
            skill_content = parts[i + 1]
            skills[skill_id] = {
                'id_line': skill_id_line,
                'content': skill_content,
                'full_text': skill_id_line + "\n" + skill_content
            }

    return header, skills


def add_dependency_to_skill(skill_content, dep_id, dep_name):
    """Add a dependency to a skill's content"""
    # Check if dependency already exists
    dep_line = f"* {dep_id}: {dep_name}"
    if dep_line in skill_content:
        return skill_content, False, "already_exists"

    # Find the Dependencies section
    deps_match = re.search(r'\nDependencies:\n', skill_content)

    if deps_match:
        # Dependencies section exists, find where to insert
        deps_start = deps_match.end()

        # Find the next section (starts with a capital letter after newline, or end of content)
        next_section = re.search(r'\n\n[A-Z]', skill_content[deps_start:])
        if next_section:
            deps_end = deps_start + next_section.start()
            insertion_point = deps_end
        else:
            # No next section, add at end
            insertion_point = len(skill_content)

        # Insert the new dependency
        new_content = (skill_content[:insertion_point] +
                      f"* {dep_id}: {dep_name}\n" +
                      skill_content[insertion_point:])
        return new_content, True, "added"
    else:
        # No Dependencies section, need to create one
        # Find where to insert (after Description section)
        desc_match = re.search(r'Description:.*?\n\n', skill_content, re.DOTALL)
        if desc_match:
            insertion_point = desc_match.end()
            new_content = (skill_content[:insertion_point] +
                          f"Dependencies:\n* {dep_id}: {dep_name}\n\n" +
                          skill_content[insertion_point:])
            return new_content, True, "added_new_section"
        else:
            # Just add at the end before any double newlines
            insertion_point = len(skill_content.rstrip())
            new_content = (skill_content[:insertion_point] +
                          f"\n\nDependencies:\n* {dep_id}: {dep_name}\n" +
                          skill_content[insertion_point:])
            return new_content, True, "added_new_section_end"


def apply_dependencies(file_path):
    """Apply all dependencies to the file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    header, skills = parse_skills(content)

    results = {
        'modified': 0,
        'already_exists': 0,
        'not_found': 0,
        'details': []
    }

    for skill_id, dep_id, dep_name in DEPENDENCIES_TO_ADD:
        if skill_id in skills:
            new_content, modified, status = add_dependency_to_skill(
                skills[skill_id]['content'], dep_id, dep_name
            )

            if modified:
                skills[skill_id]['content'] = new_content
                skills[skill_id]['full_text'] = skills[skill_id]['id_line'] + "\n" + new_content
                results['modified'] += 1
                results['details'].append(f"✓ {skill_id} -> {dep_id} ({status})")
            else:
                results['already_exists'] += 1
                results['details'].append(f"○ {skill_id} -> {dep_id} (already exists)")
        else:
            results['not_found'] += 1
            results['details'].append(f"✗ {skill_id} NOT FOUND")

    # Reconstruct the file
    new_content = header
    for skill_id in sorted(skills.keys()):
        new_content += "\n" + skills[skill_id]['full_text']

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return results


if __name__ == "__main__":
    file_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"

    print("Applying Grade 3 cross-topic dependencies...")
    print(f"Total dependencies to add: {len(DEPENDENCIES_TO_ADD)}")
    print()

    results = apply_dependencies(file_path)

    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    print(f"Skills modified: {results['modified']}")
    print(f"Dependencies already existed: {results['already_exists']}")
    print(f"Skills not found: {results['not_found']}")
    print()

    print("\n" + "="*70)
    print("DETAILED RESULTS")
    print("="*70)
    for detail in results['details']:
        print(detail)

    print("\n" + "="*70)
    print("DONE")
    print("="*70)
