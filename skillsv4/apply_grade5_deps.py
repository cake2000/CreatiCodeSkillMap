#!/usr/bin/env python3
"""
Apply Grade 5 dependency fixes to allskills.md

This script:
1. Validates all suggested dependencies against all_skill_ids.json
2. Applies validated dependencies to allskills.md
3. Handles X-2 violations by removing G2 dependencies and adding G3 replacements
4. Outputs a summary JSON with statistics
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

# File paths
ALLSKILLS_PATH = Path("/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md")
ALL_SKILL_IDS_PATH = Path("/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/all_skill_ids.json")
T01_T12_PATH = Path("/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE5_T01_T12_FINAL.json")
T13_T24_PATH = Path("/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE5_T13_T24_FINAL_OUTPUT.json")
T25_T36_PATH = Path("/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE5_T25_T36_ANALYSIS.json")
SUMMARY_PATH = Path("/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE5_DEPS_APPLICATION_SUMMARY.json")


def load_json(path: Path) -> dict:
    """Load JSON file"""
    with open(path, 'r') as f:
        return json.load(f)


def save_json(path: Path, data: dict):
    """Save JSON file"""
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)


def load_all_skill_ids() -> Set[str]:
    """Load all valid skill IDs"""
    return set(load_json(ALL_SKILL_IDS_PATH))


def find_skill_title(skill_id: str, allskills_content: str) -> str:
    """Find the title of a skill from allskills.md content"""
    # Look for the skill block
    pattern = rf"## {re.escape(skill_id)}\n\nSkill: (.+?)\n"
    match = re.search(pattern, allskills_content)
    if match:
        return match.group(1)
    return skill_id  # Fallback to ID if title not found


def find_skill_block(skill_id: str, content: str) -> Tuple[int, int, str]:
    """
    Find a skill block in the content
    Returns: (start_pos, end_pos, block_content)
    """
    # Pattern to match skill block header
    pattern = rf"## {re.escape(skill_id)}\n\n"
    match = re.search(pattern, content)

    if not match:
        return (-1, -1, "")

    start_pos = match.start()

    # Find the end of this skill block (start of next ## or end of file)
    next_skill = re.search(r"\n## T\d+\.G\d+\.", content[match.end():])
    if next_skill:
        end_pos = match.end() + next_skill.start()
    else:
        end_pos = len(content)

    block_content = content[start_pos:end_pos]
    return (start_pos, end_pos, block_content)


def get_existing_dependencies(block_content: str) -> Set[str]:
    """Extract existing dependency IDs from a skill block"""
    deps = set()

    # Find Dependencies section
    deps_match = re.search(r"Dependencies:\n((?:\* \[.+?\]: .+?\n)*)", block_content)
    if deps_match:
        deps_section = deps_match.group(1)
        # Extract dependency IDs
        for line in deps_section.strip().split('\n'):
            id_match = re.match(r"\* \[(.+?)\]:", line)
            if id_match:
                deps.add(id_match.group(1))

    return deps


def add_dependency_to_block(block_content: str, dep_id: str, dep_title: str) -> str:
    """Add a dependency to a skill block"""
    # Find Dependencies section
    deps_match = re.search(r"(Dependencies:\n)((?:\* \[.+?\]: .+?\n)*)", block_content)

    if not deps_match:
        # No Dependencies section found, this is an error
        return block_content

    deps_start = deps_match.start(2)
    deps_end = deps_match.end(2)

    existing_deps_text = block_content[deps_start:deps_end]
    new_dep_line = f"* [{dep_id}]: {dep_title}\n"

    # Add the new dependency
    updated_deps_text = existing_deps_text + new_dep_line

    # Replace in block
    return block_content[:deps_start] + updated_deps_text + block_content[deps_end:]


def remove_dependency_from_block(block_content: str, dep_id: str) -> str:
    """Remove a dependency from a skill block"""
    # Find and remove the dependency line
    pattern = rf"\* \[{re.escape(dep_id)}\]: .+?\n"
    return re.sub(pattern, "", block_content)


def validate_dependency(skill_id: str, dep_id: str, valid_ids: Set[str]) -> Tuple[bool, str]:
    """
    Validate a dependency
    Returns: (is_valid, reason)
    """
    if skill_id not in valid_ids:
        return False, f"Skill ID {skill_id} not found in all_skill_ids.json"

    if dep_id not in valid_ids:
        return False, f"Dependency ID {dep_id} not found in all_skill_ids.json"

    return True, ""


def apply_grade5_fixes():
    """Main function to apply Grade 5 dependency fixes"""
    print("Loading data...")

    # Load valid skill IDs
    valid_ids = load_all_skill_ids()
    print(f"Loaded {len(valid_ids)} valid skill IDs")

    # Load dependency suggestions
    t01_t12 = load_json(T01_T12_PATH)
    t13_t24 = load_json(T13_T24_PATH)
    t25_t36 = load_json(T25_T36_PATH)

    # Combine all dependency additions and removals
    all_deps_to_add = (
        t01_t12.get("dependencies_to_add", []) +
        t13_t24.get("dependencies_to_add", []) +
        t25_t36.get("dependencies_to_add", [])
    )

    all_deps_to_remove = (
        t01_t12.get("dependencies_to_remove", []) +
        t13_t24.get("dependencies_to_remove", []) +
        t25_t36.get("dependencies_to_remove", [])
    )

    print(f"Total dependencies to add: {len(all_deps_to_add)}")
    print(f"Total dependencies to remove: {len(all_deps_to_remove)}")

    # Load allskills.md
    with open(ALLSKILLS_PATH, 'r') as f:
        content = f.read()

    # Track statistics
    stats = {
        "total_deps_added": 0,
        "total_deps_removed": 0,
        "skipped_suggestions": [],
        "by_topic": {},
        "successful_additions": [],
        "successful_removals": []
    }

    # Process removals first
    print("\nProcessing dependency removals...")
    for removal in all_deps_to_remove:
        skill_id = removal["skill_id"]
        remove_dep = removal["remove_dep"]
        reason = removal.get("reason", "")

        print(f"  Removing {remove_dep} from {skill_id}: {reason}")

        # Find skill block
        start_pos, end_pos, block_content = find_skill_block(skill_id, content)

        if start_pos == -1:
            stats["skipped_suggestions"].append({
                "skill_id": skill_id,
                "dep_id": remove_dep,
                "action": "remove",
                "reason": f"Skill block not found for {skill_id}"
            })
            continue

        # Check if dependency exists
        existing_deps = get_existing_dependencies(block_content)
        if remove_dep not in existing_deps:
            print(f"    Warning: {remove_dep} not found in {skill_id}, skipping")
            continue

        # Remove dependency
        updated_block = remove_dependency_from_block(block_content, remove_dep)
        content = content[:start_pos] + updated_block + content[end_pos:]

        stats["total_deps_removed"] += 1
        stats["successful_removals"].append({
            "skill_id": skill_id,
            "dep_id": remove_dep,
            "reason": reason
        })

    # Process additions
    print("\nProcessing dependency additions...")
    for addition in all_deps_to_add:
        skill_id = addition["skill_id"]
        add_dep = addition["add_dep"]
        reason = addition.get("reason", "")

        # Validate
        is_valid, validation_reason = validate_dependency(skill_id, add_dep, valid_ids)

        if not is_valid:
            print(f"  Skipping {skill_id} -> {add_dep}: {validation_reason}")
            stats["skipped_suggestions"].append({
                "skill_id": skill_id,
                "dep_id": add_dep,
                "action": "add",
                "reason": validation_reason
            })
            continue

        print(f"  Adding {add_dep} to {skill_id}: {reason}")

        # Find skill block
        start_pos, end_pos, block_content = find_skill_block(skill_id, content)

        if start_pos == -1:
            stats["skipped_suggestions"].append({
                "skill_id": skill_id,
                "dep_id": add_dep,
                "action": "add",
                "reason": f"Skill block not found for {skill_id}"
            })
            continue

        # Check if dependency already exists
        existing_deps = get_existing_dependencies(block_content)
        if add_dep in existing_deps:
            print(f"    Dependency {add_dep} already exists in {skill_id}, skipping")
            continue

        # Get title for the dependency
        dep_title = find_skill_title(add_dep, content)

        # Add dependency
        updated_block = add_dependency_to_block(block_content, add_dep, dep_title)
        content = content[:start_pos] + updated_block + content[end_pos:]

        # Update end_pos for next iteration (content length may have changed)
        _, end_pos, _ = find_skill_block(skill_id, content)

        stats["total_deps_added"] += 1
        stats["successful_additions"].append({
            "skill_id": skill_id,
            "dep_id": add_dep,
            "reason": reason
        })

        # Track by topic
        topic = skill_id.split('.')[0]
        if topic not in stats["by_topic"]:
            stats["by_topic"][topic] = 0
        stats["by_topic"][topic] += 1

    # Save updated allskills.md
    print(f"\nSaving updated allskills.md...")
    with open(ALLSKILLS_PATH, 'w') as f:
        f.write(content)

    # Save summary
    print(f"Saving summary to {SUMMARY_PATH}...")
    save_json(SUMMARY_PATH, stats)

    # Print summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total dependencies added: {stats['total_deps_added']}")
    print(f"Total dependencies removed: {stats['total_deps_removed']}")
    print(f"Total skipped: {len(stats['skipped_suggestions'])}")
    print(f"\nBy topic:")
    for topic, count in sorted(stats["by_topic"].items()):
        print(f"  {topic}: {count}")

    if stats["skipped_suggestions"]:
        print(f"\nSkipped suggestions ({len(stats['skipped_suggestions'])}):")
        for skip in stats["skipped_suggestions"][:10]:  # Show first 10
            print(f"  {skip['skill_id']} -> {skip['dep_id']}: {skip['reason']}")
        if len(stats["skipped_suggestions"]) > 10:
            print(f"  ... and {len(stats['skipped_suggestions']) - 10} more")

    print("\nDone!")


if __name__ == "__main__":
    apply_grade5_fixes()
