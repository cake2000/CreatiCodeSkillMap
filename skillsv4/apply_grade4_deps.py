#!/usr/bin/env python3
"""
Apply missing Grade 4 cross-topic dependencies to allskills.md
"""

import re
from collections import defaultdict

def parse_missing_deps_file(filepath):
    """Parse the GRADE4_MISSING_DEPS_ANALYSIS.txt file to extract missing dependencies."""
    missing_deps = defaultdict(list)

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the detailed section
    detailed_section = content.split("MISSING DEPENDENCIES (DETAILED)")[1] if "MISSING DEPENDENCIES (DETAILED)" in content else content

    # Pattern to match skill blocks
    skill_pattern = r'SKILL: (T\d+\.G4\.\d+(?:\.\d+)?)\s*\n((?:  NEEDS:.*\n)+)'

    for match in re.finditer(skill_pattern, detailed_section):
        skill_id = match.group(1)
        needs_lines = match.group(2)

        # Extract dependencies
        dep_pattern = r'NEEDS: (T\d+\.G\d+\.\d+(?:\.\d+)?)'
        deps = re.findall(dep_pattern, needs_lines)

        if deps:
            missing_deps[skill_id] = deps

    return missing_deps

def read_skill_section(content, skill_id):
    """Find and return a skill section from allskills.md"""
    # Escape special regex characters in skill_id
    escaped_id = re.escape(skill_id)

    # Pattern to match the skill section with ID: format and Dependencies: section
    # Look for ID: T##.G4.## followed by Dependencies: section
    # Only match Grade 4 skills
    if not re.search(r'\.G4\.', skill_id):
        return None

    pattern = rf'(ID: {escaped_id}\n.*?Dependencies:\n)((?:\* .*?\n)*)((?:\n|---))'

    match = re.search(pattern, content, re.DOTALL)
    if match:
        return {
            'prefix': match.group(1),
            'deps': match.group(2),
            'suffix': match.group(3),
            'start': match.start(),
            'end': match.end()
        }
    return None

def parse_deps_string(deps_str):
    """Parse a dependency string into a list of dependencies."""
    if not deps_str or deps_str.strip() in ['None', '']:
        return []

    # Parse bullet point format: * T##.G#.##: Description
    deps = []
    for line in deps_str.strip().split('\n'):
        line = line.strip()
        if line.startswith('* '):
            # Extract dependency ID (before the colon)
            dep_match = re.match(r'\* (T\d+\.G\d+\.\d+(?:\.\d+)?)', line)
            if dep_match:
                deps.append(dep_match.group(1))
    return deps

def format_deps_list(deps_list, skill_names):
    """Format a list of dependencies into bullet point format."""
    if not deps_list:
        return ""

    # Sort dependencies
    sorted_deps = sorted(deps_list, key=lambda x: (
        int(re.search(r'T(\d+)', x).group(1)),
        int(re.search(r'G(\d+)', x).group(1)),
        int(re.search(r'\.(\d+)', x).group(1))
    ))

    # Format with skill names
    result = []
    for dep in sorted_deps:
        name = skill_names.get(dep, "[Unknown skill]")
        result.append(f"* {dep}: {name}")

    return "\n".join(result) + "\n"

def validate_grade_rule(skill_id, dep_id):
    """Validate X-2 rule: Grade 4 can only depend on grades 2, 3, 4"""
    skill_grade = int(re.search(r'G(\d+)', skill_id).group(1))
    dep_grade = int(re.search(r'G(\d+)', dep_id).group(1))

    if skill_grade == 4:
        return dep_grade >= 2
    return True

def get_skill_names(content):
    """Extract skill names from allskills.md"""
    skill_names = {}
    pattern = r'ID: (T\d+\.G\d+\.\d+(?:\.\d+)?)\n(?:Topic: .*?\n)?Skill: (.*?)(?:\n|$)'

    for match in re.finditer(pattern, content):
        skill_id = match.group(1)
        skill_name = match.group(2).strip()
        skill_names[skill_id] = skill_name

    return skill_names

def apply_missing_deps(allskills_path, missing_deps_path, log_path):
    """Apply missing dependencies to allskills.md"""

    # Read the missing dependencies
    print("Reading missing dependencies analysis...")
    missing_deps = parse_missing_deps_file(missing_deps_path)
    print(f"Found {len(missing_deps)} skills with missing dependencies")

    # Read allskills.md
    print("\nReading allskills.md...")
    with open(allskills_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Extract skill names
    print("Extracting skill names...")
    skill_names = get_skill_names(content)
    print(f"Found {len(skill_names)} skill names")

    # Track changes
    changes_log = []
    skills_modified = 0
    deps_added = 0
    errors = []

    # Process each skill
    for skill_id in sorted(missing_deps.keys()):
        new_deps = missing_deps[skill_id]

        # Validate grade rule
        invalid_deps = [d for d in new_deps if not validate_grade_rule(skill_id, d)]
        if invalid_deps:
            error_msg = f"SKIPPED {skill_id}: Invalid dependencies (X-2 rule): {invalid_deps}"
            errors.append(error_msg)
            print(f"  {error_msg}")
            continue

        # Find skill section
        skill_section = read_skill_section(content, skill_id)

        if not skill_section:
            error_msg = f"SKIPPED {skill_id}: Skill section not found in allskills.md"
            errors.append(error_msg)
            print(f"  {error_msg}")
            continue

        # Parse existing dependencies
        existing_deps = parse_deps_string(skill_section['deps'])

        # Add new dependencies (avoiding duplicates)
        added_for_this_skill = 0
        for dep in new_deps:
            if dep not in existing_deps:
                existing_deps.append(dep)
                added_for_this_skill += 1

        if added_for_this_skill == 0:
            print(f"  {skill_id}: No new dependencies to add (all already exist)")
            continue

        # Format updated dependencies
        updated_deps_str = format_deps_list(existing_deps, skill_names)

        # Replace in content
        old_section = skill_section['prefix'] + skill_section['deps'] + skill_section['suffix']
        new_section = skill_section['prefix'] + updated_deps_str + skill_section['suffix']

        content = content.replace(old_section, new_section, 1)

        # Log change
        change_log = f"{skill_id}: Added {added_for_this_skill} dependencies: {[d for d in new_deps if d not in parse_deps_string(skill_section['deps'])]}"
        changes_log.append(change_log)
        print(f"  {change_log}")

        skills_modified += 1
        deps_added += added_for_this_skill

    # Write updated content
    if content != original_content:
        print(f"\nWriting updated allskills.md...")
        with open(allskills_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Done!")
    else:
        print("\nNo changes made to allskills.md")

    # Write log
    print(f"\nWriting changes log to {log_path}...")
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("GRADE 4 CROSS-TOPIC DEPENDENCIES APPLICATION LOG\n")
        f.write("=" * 80 + "\n\n")

        f.write(f"Total skills processed: {len(missing_deps)}\n")
        f.write(f"Skills modified: {skills_modified}\n")
        f.write(f"Dependencies added: {deps_added}\n")
        f.write(f"Errors/Skipped: {len(errors)}\n\n")

        if errors:
            f.write("=" * 80 + "\n")
            f.write("ERRORS/SKIPPED\n")
            f.write("=" * 80 + "\n")
            for error in errors:
                f.write(f"{error}\n")
            f.write("\n")

        f.write("=" * 80 + "\n")
        f.write("CHANGES APPLIED\n")
        f.write("=" * 80 + "\n")
        for change in changes_log:
            f.write(f"{change}\n")

    print("\nSummary:")
    print(f"  Skills modified: {skills_modified}")
    print(f"  Dependencies added: {deps_added}")
    print(f"  Errors/Skipped: {len(errors)}")

    return {
        'skills_modified': skills_modified,
        'deps_added': deps_added,
        'errors': len(errors)
    }

if __name__ == "__main__":
    allskills_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"
    missing_deps_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE4_MISSING_DEPS_ANALYSIS.txt"
    log_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE4_DEPS_APPLIED_LOG.txt"

    apply_missing_deps(allskills_path, missing_deps_path, log_path)
