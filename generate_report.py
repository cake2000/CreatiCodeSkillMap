#!/usr/bin/env python3
"""
Generate a detailed report of transitive dependency removals.
"""

import re
from collections import defaultdict

def parse_skills_file(filepath: str):
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

        if line.startswith('ID: '):
            if current_id and current_skill:
                skills[current_id] = current_skill

            current_id = line[4:].strip()
            current_skill = {
                'id': current_id,
                'skill': '',
                'dependencies': []
            }
            in_dependencies = False

        elif current_id:
            if line.startswith('Skill: '):
                current_skill['skill'] = line[7:].strip()
            elif line.startswith('Dependencies:'):
                in_dependencies = True
            elif in_dependencies and line.startswith('* '):
                dep_match = re.match(r'\* ([^:]+):', line)
                if dep_match:
                    dep_id = dep_match.group(1).strip()
                    current_skill['dependencies'].append(dep_id)
                    dependencies[current_id].add(dep_id)
            elif in_dependencies and not line:
                in_dependencies = False

        i += 1

    if current_id and current_skill:
        skills[current_id] = current_skill

    return skills, dict(dependencies)


def get_all_transitive_deps(skill_id: str, dependencies: dict, visited: set = None) -> set:
    """Get all transitive dependencies for a skill."""
    if visited is None:
        visited = set()

    if skill_id in visited:
        return set()

    visited.add(skill_id)
    all_deps = set()

    direct_deps = dependencies.get(skill_id, set())
    for dep in direct_deps:
        all_deps.add(dep)
        all_deps.update(get_all_transitive_deps(dep, dependencies, visited.copy()))

    return all_deps


def explain_why_transitive(skill_id: str, transitive_dep: str, direct_deps: set, dependencies: dict):
    """Explain why a dependency is transitive."""
    reasons = []

    for other_dep in direct_deps:
        if other_dep == transitive_dep:
            continue

        other_transitives = get_all_transitive_deps(other_dep, dependencies)
        if transitive_dep in other_transitives:
            reasons.append(f"  -> {transitive_dep} is already included via {other_dep}")

    return reasons


# Parse file
filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
skills, dependencies = parse_skills_file(filepath)

# Find Grade 5 skills
grade5_skills = {k: v for k, v in skills.items() if '.G5.' in k}

# Generate detailed report
print("DETAILED TRANSITIVE DEPENDENCY REMOVAL REPORT")
print("=" * 100)
print()

changes_with_reasons = []

for skill_id in sorted(grade5_skills.keys()):
    skill_data = skills[skill_id]
    if not skill_data['dependencies']:
        continue

    direct_deps = set(skill_data['dependencies'])

    # Find transitive dependencies
    transitive = set()
    reasons_map = {}

    for dep in direct_deps:
        other_deps = direct_deps - {dep}
        for other_dep in other_deps:
            other_transitives = get_all_transitive_deps(other_dep, dependencies)
            if dep in other_transitives:
                transitive.add(dep)
                if dep not in reasons_map:
                    reasons_map[dep] = []
                reasons_map[dep].append(other_dep)

    if transitive:
        changes_with_reasons.append({
            'skill_id': skill_id,
            'skill_name': skill_data['skill'],
            'removed': sorted(transitive),
            'kept': sorted(direct_deps - transitive),
            'reasons': reasons_map
        })

# Print summary
print(f"Total Grade 5 skills: {len(grade5_skills)}")
print(f"Skills with transitive dependencies: {len(changes_with_reasons)}")
print(f"Total transitive dependencies removed: {sum(len(c['removed']) for c in changes_with_reasons)}")
print()
print("=" * 100)
print()

# Show detailed examples (first 10)
print("DETAILED EXAMPLES (showing first 10):")
print()

for i, change in enumerate(changes_with_reasons[:10], 1):
    print(f"{i}. {change['skill_id']}: {change['skill_name']}")
    print(f"   Original dependencies: {len(change['removed']) + len(change['kept'])}")
    print(f"   After cleanup: {len(change['kept'])}")
    print()

    if change['removed']:
        print("   REMOVED (transitive):")
        for dep in change['removed']:
            print(f"     - {dep}")
            if dep in change['reasons']:
                for implied_by in change['reasons'][dep]:
                    print(f"       (already implied by: {implied_by})")
        print()

    if change['kept']:
        print("   KEPT (direct):")
        for dep in change['kept']:
            print(f"     - {dep}")
    else:
        print("   KEPT: (none - all were transitive)")

    print()
    print("-" * 100)
    print()

if len(changes_with_reasons) > 10:
    print(f"... and {len(changes_with_reasons) - 10} more skills with changes")
    print()

# Statistics by topic
print("=" * 100)
print("STATISTICS BY TOPIC:")
print()

by_topic = defaultdict(lambda: {'count': 0, 'removed': 0})
for change in changes_with_reasons:
    topic = change['skill_id'].split('.')[0]
    by_topic[topic]['count'] += 1
    by_topic[topic]['removed'] += len(change['removed'])

for topic in sorted(by_topic.keys()):
    stats = by_topic[topic]
    print(f"{topic}: {stats['count']} skills modified, {stats['removed']} dependencies removed")
