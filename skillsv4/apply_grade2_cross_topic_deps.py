#!/usr/bin/env python3
"""
Apply cross-topic dependency fixes to Grade 2 skills in allskills.md
"""

import re
from collections import defaultdict

# All dependencies to add - compiled from comprehensive analysis
DEPENDENCIES_TO_ADD = [
    # T01-T10 Dependencies
    ("T01.G2.01", "T07.G1.02", "Understanding repeat counting is foundational for identifying repeated actions"),
    ("T01.G2.04", "T08.G1.03", "Conditional logic needed for if/then rules"),
    ("T01.G2.08", "T07.G1.02", "Tracing repeats requires repeat counting understanding"),
    ("T01.G2.11", "T01.G1.01", "Basic sequencing needed before tracing maze directions"),
    ("T02.G2.03", "T01.G1.09", "Tracing sequences builds on algorithm tracing"),
    ("T02.G2.06", "T01.G1.06", "Fixing sequencing errors builds on earlier debugging"),
    ("T03.G2.03", "T02.G1.01", "Understanding sequential diagrams helps order subtasks"),
    ("T04.G2.02", "T01.G1.09", "Understanding algorithms helps spot repeated steps"),
    ("T04.G2.05", "T02.G1.02", "Box diagram understanding needed for repeat boxes"),
    ("T05.G2.04", "T03.G1.03", "Decomposition skills needed for simulations"),
    ("T06.G2.01", "T01.G1.09", "Algorithm tracing foundational for cause-effect chains"),
    ("T06.G2.03", "T08.G1.03", "Conditional logic needed for if-then game rules"),
    ("T07.G2.01", "T04.G1.03", "Pattern recognition helps identify when repetition is needed"),
    ("T10.G2.05", "T08.G1.02", "Rule matching needed for finding matching rows"),

    # T12-T20 Dependencies
    ("T12.G2.02", "T01.G1.01", "Understanding sequences needed before labeling sections"),
    ("T13.G2.04", "T08.G1.01", "Adding checks requires conditional thinking"),
    ("T14.G2.02", "T02.G1.01", "Tracking lives requires counting/data tracking"),
    ("T14.G2.03", "T08.G1.01", "Level progression requires conditional logic"),
    ("T15.G2.01", "T04.G1.01", "Comparing animation speeds requires pattern recognition"),
    ("T15.G2.03", "T04.G2.01", "Identifying repeating animation patterns requires pattern skills"),
    ("T15.G2.03", "T07.G1.01", "Loop understanding needed for animation loops"),
    ("T16.G2.01", "T08.G1.01", "UI interactions are conditional"),
    ("T16.G2.02", "T03.G1.02", "Interface design requires organizing elements"),
    ("T18.G2.01", "T17.G1.01", "3D viewpoints build on 2D motion concepts"),
    ("T20.G2.01", "T04.G1.01", "Using repeat in art requires pattern recognition"),
    ("T20.G2.02", "T04.G1.02", "Creating symmetrical patterns requires pattern understanding"),
    ("T20.G2.03", "T04.G2.02", "Layering patterns requires recognizing repeated sequences"),

    # T21-T36 Dependencies
    ("T21.G2.02", "T35.GK.04", "AI checking requires safe sharing awareness"),
    ("T22.G2.02", "T32.GK.01", "Private info in chat requires privacy concepts"),
    ("T23.G2.01", "T30.GK.01", "Understanding sensors requires device knowledge"),
    ("T23.G2.02", "T30.GK.01", "Sensor limitations requires hardware knowledge"),
    ("T23.G2.03", "T30.GK.01", "Distinguishing sensor input requires hardware understanding"),
    ("T24.G2.01", "T01.GK.02", "Multi-step AI demos require sequencing concepts"),
    ("T26.G2.01", "T25.GK.01", "Distinguishing data types requires data representation"),
    ("T26.G2.03", "T25.GK.01", "Collecting duration data requires data representation"),
    ("T26.G2.05", "T25.GK.01", "Surveys require understanding data structure"),
    ("T27.G2.01", "T26.GK.01", "Creating charts requires data collection understanding"),
    ("T27.G2.01", "T25.GK.01", "Creating charts requires data representation"),
    ("T27.G2.04", "T26.GK.01", "Analyzing data requires data collection understanding"),
    ("T28.G2.04", "T26.GK.01", "Making predictions requires data collection"),
    ("T29.G2.04", "T01.GK.02", "Find/replace requires sequential processing"),
    ("T31.G2.01", "T30.GK.01", "Internet connections require device understanding"),
    ("T32.G2.01", "T30.GK.01", "Creating passwords requires device understanding"),
    ("T32.G2.01", "T35.GK.04", "Password security connects to safe sharing"),
    ("T32.G2.04", "T30.GK.01", "Device care requires device understanding"),
    ("T32.G2.05", "T30.GK.01", "Suspicious links require device/internet knowledge"),
    ("T32.G2.05", "T35.GK.04", "Recognizing dangers requires safe sharing judgment"),
    ("T32.G2.06", "T30.GK.01", "Authentication requires device knowledge"),
    ("T33.G2.01", "T31.GK.01", "App connectivity requires network basics"),
    ("T34.G2.01", "T30.GK.01", "Comparing technology requires hardware understanding"),
    ("T36.G2.04", "T35.GK.01", "Digital creation careers require tech impact awareness"),
]


def read_file(filepath):
    """Read the entire file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath, content):
    """Write content to file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def extract_skill_name(content, skill_id):
    """Extract the skill name for a given skill ID"""
    pattern = rf'^ID: {re.escape(skill_id)}\s*$\n^Topic: .+$\n^Skill: (.+?)$'
    match = re.search(pattern, content, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return None


def find_skill_section(content, skill_id):
    """Find the start and end positions of a skill section"""
    # Find the skill ID line
    pattern = rf'^ID: {re.escape(skill_id)}\s*$'
    match = re.search(pattern, content, re.MULTILINE)

    if not match:
        return None, None

    start = match.start()

    # Find the next skill ID (or end of file)
    next_pattern = r'^ID: [A-Z0-9]+\.G[0-9K]+\.[0-9]+\s*$'
    next_match = re.search(next_pattern, content[match.end():], re.MULTILINE)

    if next_match:
        end = match.end() + next_match.start()
    else:
        end = len(content)

    return start, end


def get_dependencies_section(skill_content):
    """Extract the Dependencies section from skill content"""
    pattern = r'^Dependencies:\s*\n((?:\* .+\n)*)'
    match = re.search(pattern, skill_content, re.MULTILINE)

    if match:
        deps_start = match.start()
        deps_end = match.end()
        deps_text = match.group(1)
        return deps_start, deps_end, deps_text

    return None, None, None


def parse_existing_dependencies(deps_text):
    """Parse existing dependencies into a set of skill IDs"""
    deps = set()
    if deps_text:
        for line in deps_text.strip().split('\n'):
            match = re.match(r'\* ([A-Z0-9]+\.G[0-9K]+\.[0-9]+):', line.strip())
            if match:
                deps.add(match.group(1))
    return deps


def apply_dependencies(filepath):
    """Apply all dependencies to the file"""
    print(f"Reading file: {filepath}")
    content = read_file(filepath)

    # Group dependencies by target skill
    deps_by_skill = defaultdict(list)
    for target_skill, dep_skill, reason in DEPENDENCIES_TO_ADD:
        deps_by_skill[target_skill].append((dep_skill, reason))

    print(f"\nTotal dependencies to add: {len(DEPENDENCIES_TO_ADD)}")
    print(f"Skills to modify: {len(deps_by_skill)}")

    # Track changes
    modified_skills = []
    failed_skills = []
    total_deps_added = 0

    # Process each target skill
    for target_skill in sorted(deps_by_skill.keys()):
        print(f"\n--- Processing {target_skill} ---")

        # Find the skill section
        start, end = find_skill_section(content, target_skill)
        if start is None:
            print(f"ERROR: Could not find skill {target_skill}")
            failed_skills.append((target_skill, "Skill not found in file"))
            continue

        skill_content = content[start:end]

        # Get Dependencies section
        deps_start, deps_end, deps_text = get_dependencies_section(skill_content)

        # Parse existing dependencies
        existing_deps = parse_existing_dependencies(deps_text) if deps_text else set()
        print(f"Existing dependencies: {existing_deps}")

        # Prepare new dependencies to add
        new_deps_to_add = []
        for dep_skill, reason in deps_by_skill[target_skill]:
            # Verify the dependency skill exists
            dep_name = extract_skill_name(content, dep_skill)
            if not dep_name:
                print(f"WARNING: Dependency skill {dep_skill} not found in file, skipping")
                failed_skills.append((target_skill, f"Dependency {dep_skill} not found"))
                continue

            # Check if already exists
            if dep_skill in existing_deps:
                print(f"Dependency {dep_skill} already exists, skipping")
                continue

            new_deps_to_add.append((dep_skill, dep_name))
            print(f"Will add: {dep_skill}: {dep_name}")

        if not new_deps_to_add:
            print(f"No new dependencies to add for {target_skill}")
            continue

        # Modify the skill section
        if deps_start is not None:
            # Dependencies section exists, append to it
            new_deps_lines = []
            for dep_skill, dep_name in new_deps_to_add:
                new_deps_lines.append(f"* {dep_skill}: {dep_name}\n")

            # Insert new dependencies at the end of existing ones
            new_skill_content = (
                skill_content[:deps_end] +
                ''.join(new_deps_lines) +
                skill_content[deps_end:]
            )
        else:
            # No Dependencies section, need to add one
            # Find where to insert (after Description: line)
            desc_pattern = r'^Description: .+$'
            desc_match = re.search(desc_pattern, skill_content, re.MULTILINE)

            if not desc_match:
                print(f"ERROR: Could not find Description field for {target_skill}")
                failed_skills.append((target_skill, "Could not find Description field"))
                continue

            insert_pos = desc_match.end()

            # Build Dependencies section
            deps_section = "\n\nDependencies:\n"
            for dep_skill, dep_name in new_deps_to_add:
                deps_section += f"* {dep_skill}: {dep_name}\n"

            new_skill_content = (
                skill_content[:insert_pos] +
                deps_section +
                skill_content[insert_pos:]
            )

        # Update the content
        content = content[:start] + new_skill_content + content[end:]

        # Track changes
        modified_skills.append(target_skill)
        total_deps_added += len(new_deps_to_add)
        print(f"Added {len(new_deps_to_add)} dependencies to {target_skill}")

    # Write back to file
    print(f"\n\nWriting changes to file...")
    write_file(filepath, content)

    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total dependencies added: {total_deps_added}")
    print(f"Skills modified: {len(modified_skills)}")
    print(f"\nModified skills:")
    for skill in modified_skills:
        print(f"  - {skill}")

    if failed_skills:
        print(f"\n\nSkills with issues: {len(failed_skills)}")
        for skill, reason in failed_skills:
            print(f"  - {skill}: {reason}")

    return {
        'total_deps_added': total_deps_added,
        'modified_skills': modified_skills,
        'failed_skills': failed_skills
    }


if __name__ == "__main__":
    filepath = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"
    results = apply_dependencies(filepath)

    print("\n\nDone!")
