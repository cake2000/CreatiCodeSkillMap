#!/usr/bin/env python3
"""
Clean up transitive dependencies in Grade 5 skills.
A dependency is transitive if it's already implied through another dependency.
"""

import re
from collections import defaultdict
from typing import Dict, Set, List, Tuple

def parse_skills_file(filepath: str) -> Tuple[Dict[str, Dict], Dict[str, Set[str]]]:
    """Parse the skills file and return skill data and dependency graph."""
    skills = {}
    dependencies = defaultdict(set)

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_id = None
    current_skill = None
    in_dependencies = False

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Check for ID line
        if line.startswith('ID: '):
            if current_id and current_skill:
                skills[current_id] = current_skill

            current_id = line[4:].strip()
            current_skill = {
                'id': current_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': [],
                'start_line': i
            }
            in_dependencies = False

        elif current_id:
            if line.startswith('Topic: '):
                current_skill['topic'] = line[7:].strip()
            elif line.startswith('Skill: '):
                current_skill['skill'] = line[7:].strip()
            elif line.startswith('Description: '):
                current_skill['description'] = line[13:].strip()
            elif line.startswith('Dependencies:'):
                in_dependencies = True
            elif in_dependencies and line.startswith('* '):
                # Parse dependency: "* T01.GK.01: Description"
                dep_match = re.match(r'\* ([^:]+):', line)
                if dep_match:
                    dep_id = dep_match.group(1).strip()
                    current_skill['dependencies'].append({
                        'id': dep_id,
                        'line': line
                    })
                    dependencies[current_id].add(dep_id)
            elif in_dependencies and not line:
                in_dependencies = False

        i += 1

    # Don't forget the last skill
    if current_id and current_skill:
        skills[current_id] = current_skill

    return skills, dict(dependencies)


def get_all_transitive_deps(skill_id: str, dependencies: Dict[str, Set[str]],
                            visited: Set[str] = None) -> Set[str]:
    """Get all transitive dependencies for a skill (recursively)."""
    if visited is None:
        visited = set()

    if skill_id in visited:
        return set()

    visited.add(skill_id)
    all_deps = set()

    # Get direct dependencies
    direct_deps = dependencies.get(skill_id, set())

    # For each direct dependency, get its transitive dependencies
    for dep in direct_deps:
        all_deps.add(dep)
        # Recursively get dependencies of this dependency
        all_deps.update(get_all_transitive_deps(dep, dependencies, visited.copy()))

    return all_deps


def find_transitive_dependencies(skill_id: str, direct_deps: Set[str],
                                 dependencies: Dict[str, Set[str]]) -> Set[str]:
    """Find which direct dependencies are transitive (redundant)."""
    transitive = set()

    # For each direct dependency
    for dep in direct_deps:
        # Check if this dependency is implied by any other direct dependency
        other_deps = direct_deps - {dep}

        for other_dep in other_deps:
            # Get all transitive dependencies of other_dep
            other_dep_transitives = get_all_transitive_deps(other_dep, dependencies)

            # If dep is in other_dep's transitive dependencies, it's redundant
            if dep in other_dep_transitives:
                transitive.add(dep)
                break

    return transitive


def clean_grade5_transitive_deps(filepath: str, output_filepath: str = None):
    """Remove transitive dependencies from Grade 5 skills."""
    if output_filepath is None:
        output_filepath = filepath

    print("Parsing skills file...")
    skills, dependencies = parse_skills_file(filepath)

    print(f"Total skills parsed: {len(skills)}")

    # Find Grade 5 skills
    grade5_skills = {k: v for k, v in skills.items() if '.G5.' in k}
    print(f"Grade 5 skills found: {len(grade5_skills)}")

    # Track changes
    changes = []
    total_removed = 0

    # For each Grade 5 skill
    for skill_id, skill_data in sorted(grade5_skills.items()):
        if not skill_data['dependencies']:
            continue

        direct_deps = dependencies.get(skill_id, set())
        if not direct_deps:
            continue

        # Find transitive dependencies
        transitive = find_transitive_dependencies(skill_id, direct_deps, dependencies)

        if transitive:
            removed_deps = []
            kept_deps = []

            for dep_info in skill_data['dependencies']:
                if dep_info['id'] in transitive:
                    removed_deps.append(dep_info['id'])
                else:
                    kept_deps.append(dep_info)

            if removed_deps:
                changes.append({
                    'skill_id': skill_id,
                    'skill_name': skill_data['skill'],
                    'removed': removed_deps,
                    'kept': [d['id'] for d in kept_deps]
                })

                # Update the skill data
                skill_data['dependencies'] = kept_deps
                dependencies[skill_id] = {d['id'] for d in kept_deps}
                total_removed += len(removed_deps)

    # Write the updated file
    print("\nWriting updated file...")
    write_updated_file(filepath, skills, output_filepath)

    # Report changes
    print(f"\n{'='*80}")
    print(f"TRANSITIVE DEPENDENCY CLEANUP COMPLETE")
    print(f"{'='*80}")
    print(f"\nTotal transitive dependencies removed: {total_removed}")
    print(f"Grade 5 skills modified: {len(changes)}")

    if changes:
        print("\n" + "="*80)
        print("EXAMPLES OF CHANGES MADE:")
        print("="*80)

        # Show first 5 examples
        for i, change in enumerate(changes[:5], 1):
            print(f"\n{i}. {change['skill_id']}: {change['skill_name']}")
            print(f"   Removed (transitive): {', '.join(change['removed'])}")
            print(f"   Kept (direct): {', '.join(change['kept']) if change['kept'] else 'None'}")

        if len(changes) > 5:
            print(f"\n   ... and {len(changes) - 5} more skills modified")

    # Verify all Grade 5 skills still have valid dependencies or none
    print("\n" + "="*80)
    print("VERIFICATION:")
    print("="*80)
    orphaned = []
    for skill_id in sorted(grade5_skills.keys()):
        deps = dependencies.get(skill_id, set())
        if not deps:
            # Check if this skill originally had dependencies
            if any(c['skill_id'] == skill_id for c in changes):
                # It was modified, check if all were removed
                change = next(c for c in changes if c['skill_id'] == skill_id)
                if not change['kept']:
                    orphaned.append(skill_id)

    if orphaned:
        print(f"WARNING: {len(orphaned)} skills have NO dependencies after cleanup:")
        for skill_id in orphaned[:10]:
            print(f"  - {skill_id}")
    else:
        print("All Grade 5 skills have valid dependency chains!")

    print(f"\nOutput written to: {output_filepath}")

    return changes, total_removed


def write_updated_file(original_filepath: str, skills: Dict, output_filepath: str):
    """Write the updated skills back to file, preserving formatting."""
    with open(original_filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Build a map of skill_id -> updated dependencies text
    updated_deps = {}
    for skill_id, skill_data in skills.items():
        if skill_data['dependencies']:
            deps_lines = ['Dependencies:\n']
            for dep_info in skill_data['dependencies']:
                deps_lines.append(dep_info['line'] + '\n')
            updated_deps[skill_id] = deps_lines
        else:
            updated_deps[skill_id] = []

    # Process the file
    new_lines = []
    i = 0
    current_id = None
    in_dependencies = False
    skip_until_blank = False

    while i < len(lines):
        line = lines[i]

        # Check for ID line
        if line.strip().startswith('ID: '):
            current_id = line.strip()[4:].strip()
            in_dependencies = False
            skip_until_blank = False
            new_lines.append(line)

        elif line.strip().startswith('Dependencies:'):
            # We're entering a dependencies section
            in_dependencies = True
            skip_until_blank = True

            # Replace with updated dependencies for this skill
            if current_id in updated_deps:
                new_lines.extend(updated_deps[current_id])
            # If no updated deps, skip this entire section

        elif skip_until_blank:
            # Skip old dependency lines until we hit a blank line
            if not line.strip():
                skip_until_blank = False
                new_lines.append(line)

        else:
            new_lines.append(line)

        i += 1

    # Write the new file
    with open(output_filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)


if __name__ == '__main__':
    import sys

    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    if len(sys.argv) > 1:
        output_filepath = sys.argv[1]
    else:
        output_filepath = filepath

    clean_grade5_transitive_deps(filepath, output_filepath)
