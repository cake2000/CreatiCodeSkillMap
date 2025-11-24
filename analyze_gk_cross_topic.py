#!/usr/bin/env python3
"""
Analyze Grade K skills across all 36 topics for cross-topic dependencies.
Focus on finding:
1. X-2 rule violations (K skills depending on non-K skills)
2. Missing cross-topic dependencies
3. Circular dependencies
4. Truly redundant transitive dependencies
5. Skills that overlap across topics
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def parse_allskills_file(filepath: str) -> Dict[str, Dict]:
    """Parse allskills.md and extract all Grade K skills with their dependencies."""

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by ID: markers to get individual skills
    skill_blocks = re.split(r'\n(?=ID: T\d+\.)', content)

    gk_skills = {}

    for block in skill_blocks:
        if not block.strip():
            continue

        # Extract skill ID
        id_match = re.search(r'^ID: (T\d+\.GK\.\d+)', block, re.MULTILINE)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic
        topic_match = re.search(r'^Topic: (.+)$', block, re.MULTILINE)
        topic = topic_match.group(1) if topic_match else ""

        # Extract skill name
        skill_match = re.search(r'^Skill: (.+)$', block, re.MULTILINE)
        skill_name = skill_match.group(1) if skill_match else ""

        # Extract description
        desc_match = re.search(r'^Description: (.+?)(?=\n\n|\nDependencies:|\Z)', block, re.MULTILINE | re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        deps = []
        deps_section = re.search(r'Dependencies:\n((?:\* .+\n?)+)', block, re.MULTILINE)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'\* (T\d+\.[A-Z]\d+\.\d+):', line)
                if dep_match:
                    deps.append(dep_match.group(1))

        gk_skills[skill_id] = {
            'topic': topic,
            'name': skill_name,
            'description': description,
            'dependencies': deps,
            'block': block
        }

    return gk_skills

def get_topic_number(skill_id: str) -> str:
    """Extract topic number from skill ID (e.g., T01.GK.01 -> T01)"""
    return skill_id.split('.')[0]

def analyze_x_minus_2_violations(gk_skills: Dict) -> List[Tuple[str, List[str]]]:
    """Find Grade K skills that depend on non-K skills (violates X-2 rule)."""
    violations = []

    for skill_id, skill_data in gk_skills.items():
        non_k_deps = [dep for dep in skill_data['dependencies'] if '.GK.' not in dep]
        if non_k_deps:
            violations.append((skill_id, non_k_deps))

    return violations

def analyze_missing_cross_topic_deps(gk_skills: Dict) -> List[Dict]:
    """Identify missing cross-topic dependencies based on skill content patterns."""

    missing_deps = []

    # Define patterns that suggest cross-topic dependencies
    patterns = {
        'loops': {
            'keywords': ['repeat', 'loop', 'again', 'over and over', 'multiple times', 'forever'],
            'should_depend_on': ['T02.GK'],  # T02 is Loops
            'description': 'Skills using loops should depend on loop basics'
        },
        'variables': {
            'keywords': ['variable', 'score', 'counter', 'points', 'lives', 'health'],
            'should_depend_on': ['T04.GK'],  # T04 is Variables
            'description': 'Skills using variables should depend on variable basics'
        },
        'conditionals': {
            'keywords': ['if', 'when', 'choice', 'condition', 'check'],
            'should_depend_on': ['T03.GK'],  # T03 is Conditionals
            'description': 'Skills using conditionals should depend on conditional basics'
        },
        'events': {
            'keywords': ['click', 'press', 'touch', 'event', 'trigger'],
            'should_depend_on': ['T05.GK', 'T06.GK'],  # Events and Input
            'description': 'Skills using events/input should depend on event basics'
        },
        'motion': {
            'keywords': ['move', 'glide', 'position', 'go to', 'point'],
            'should_depend_on': ['T07.GK', 'T08.GK'],  # Motion and Coordinates
            'description': 'Skills with motion should depend on motion basics'
        },
        'sprites': {
            'keywords': ['character', 'sprite', 'costume', 'clone'],
            'should_depend_on': ['T09.GK'],  # Sprites
            'description': 'Skills using sprites should depend on sprite basics'
        },
        'drawing': {
            'keywords': ['draw', 'pen', 'line', 'stamp', 'paint'],
            'should_depend_on': ['T11.GK'],  # Drawing
            'description': 'Skills with drawing should depend on drawing basics'
        },
        'sound': {
            'keywords': ['sound', 'play', 'music', 'audio', 'note'],
            'should_depend_on': ['T12.GK'],  # Sound
            'description': 'Skills using sound should depend on sound basics'
        }
    }

    for skill_id, skill_data in gk_skills.items():
        skill_topic = get_topic_number(skill_id)
        text_to_check = (skill_data['name'] + ' ' + skill_data['description']).lower()

        for pattern_name, pattern_info in patterns.items():
            # Check if skill uses these concepts
            uses_concept = any(keyword in text_to_check for keyword in pattern_info['keywords'])

            if uses_concept:
                # Check if it already has dependencies from the relevant topics
                relevant_topics = pattern_info['should_depend_on']
                has_dep = False

                for dep in skill_data['dependencies']:
                    dep_topic = get_topic_number(dep)
                    if any(rt in dep for rt in relevant_topics):
                        has_dep = True
                        break

                # Only flag if it's from a DIFFERENT topic (cross-topic issue)
                if not has_dep and not any(skill_topic in rt for rt in relevant_topics):
                    missing_deps.append({
                        'skill_id': skill_id,
                        'skill_name': skill_data['name'],
                        'topic': skill_topic,
                        'missing_concept': pattern_name,
                        'reason': pattern_info['description'],
                        'suggested_deps': relevant_topics
                    })

    return missing_deps

def find_circular_dependencies(gk_skills: Dict) -> List[List[str]]:
    """Find circular dependency chains."""

    def find_cycle(node, visited, rec_stack, path):
        visited.add(node)
        rec_stack.add(node)
        path.append(node)

        if node in gk_skills:
            for neighbor in gk_skills[node]['dependencies']:
                if neighbor not in gk_skills:
                    continue

                if neighbor not in visited:
                    result = find_cycle(neighbor, visited, rec_stack, path[:])
                    if result:
                        return result
                elif neighbor in rec_stack:
                    # Found a cycle
                    cycle_start = path.index(neighbor)
                    return path[cycle_start:] + [neighbor]

        rec_stack.remove(node)
        return None

    cycles = []
    visited = set()

    for skill_id in gk_skills:
        if skill_id not in visited:
            rec_stack = set()
            cycle = find_cycle(skill_id, visited, rec_stack, [])
            if cycle:
                cycles.append(cycle)

    return cycles

def find_redundant_transitive_deps(gk_skills: Dict) -> List[Dict]:
    """Find truly redundant transitive dependencies (A→B→C where A→C exists)."""

    def get_all_reachable(skill_id, exclude_direct=False):
        """Get all skills reachable from skill_id via dependencies."""
        reachable = set()
        to_visit = []

        if skill_id not in gk_skills:
            return reachable

        if exclude_direct:
            # Start from dependencies of dependencies
            for dep in gk_skills[skill_id]['dependencies']:
                if dep in gk_skills:
                    to_visit.extend(gk_skills[dep]['dependencies'])
        else:
            to_visit = gk_skills[skill_id]['dependencies'][:]

        visited = set()
        while to_visit:
            current = to_visit.pop(0)
            if current in visited or current not in gk_skills:
                continue
            visited.add(current)
            reachable.add(current)
            to_visit.extend(gk_skills[current]['dependencies'])

        return reachable

    redundant = []

    for skill_id, skill_data in gk_skills.items():
        direct_deps = skill_data['dependencies']

        for dep in direct_deps:
            # Check if dep is reachable via other direct dependencies
            other_deps = [d for d in direct_deps if d != dep]

            for other_dep in other_deps:
                reachable_from_other = get_all_reachable(other_dep, exclude_direct=False)
                if dep in reachable_from_other:
                    redundant.append({
                        'skill': skill_id,
                        'redundant_dep': dep,
                        'reachable_via': other_dep
                    })

    return redundant

def analyze_topic_overlap(gk_skills: Dict) -> List[Dict]:
    """Find skills from different topics that overlap in content."""

    # Group skills by similar keywords in their names
    keyword_groups = defaultdict(list)

    for skill_id, skill_data in gk_skills.items():
        name_lower = skill_data['name'].lower()
        words = re.findall(r'\b\w+\b', name_lower)

        # Filter out common words
        stop_words = {'a', 'an', 'the', 'is', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'and'}
        meaningful_words = [w for w in words if w not in stop_words and len(w) > 3]

        for word in meaningful_words:
            keyword_groups[word].append(skill_id)

    overlaps = []

    for keyword, skill_ids in keyword_groups.items():
        if len(skill_ids) > 1:
            # Check if they're from different topics
            topics = [get_topic_number(sid) for sid in skill_ids]
            if len(set(topics)) > 1:
                overlaps.append({
                    'keyword': keyword,
                    'skills': [(sid, gk_skills[sid]['name'], gk_skills[sid]['topic']) for sid in skill_ids]
                })

    return overlaps

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing allskills.md...")
    gk_skills = parse_allskills_file(filepath)
    print(f"Found {len(gk_skills)} Grade K skills\n")

    # Group by topic
    by_topic = defaultdict(list)
    for skill_id, skill_data in gk_skills.items():
        topic_num = get_topic_number(skill_id)
        by_topic[topic_num].append((skill_id, skill_data['name']))

    print("=" * 80)
    print("GRADE K SKILLS BY TOPIC")
    print("=" * 80)

    for topic in sorted(by_topic.keys()):
        print(f"\n{topic}:")
        for skill_id, name in sorted(by_topic[topic]):
            print(f"  {skill_id}: {name}")

    print("\n\n" + "=" * 80)
    print("X-2 RULE VIOLATIONS (K skills depending on non-K skills)")
    print("=" * 80)

    violations = analyze_x_minus_2_violations(gk_skills)
    if violations:
        for skill_id, non_k_deps in violations:
            print(f"\n{skill_id}: {gk_skills[skill_id]['name']}")
            print(f"  Topic: {gk_skills[skill_id]['topic']}")
            print(f"  Invalid dependencies:")
            for dep in non_k_deps:
                print(f"    - {dep}")
    else:
        print("\nNo violations found")

    print("\n\n" + "=" * 80)
    print("MISSING CROSS-TOPIC DEPENDENCIES")
    print("=" * 80)

    missing = analyze_missing_cross_topic_deps(gk_skills)
    if missing:
        grouped_by_topic = defaultdict(list)
        for item in missing:
            grouped_by_topic[item['topic']].append(item)

        for topic in sorted(grouped_by_topic.keys()):
            print(f"\n{topic}:")
            for item in grouped_by_topic[topic]:
                print(f"  {item['skill_id']}: {item['skill_name']}")
                print(f"    Missing: {item['missing_concept']}")
                print(f"    Reason: {item['reason']}")
                print(f"    Suggested: {', '.join(item['suggested_deps'])}")
    else:
        print("\nNo obvious missing dependencies found")

    print("\n\n" + "=" * 80)
    print("CIRCULAR DEPENDENCIES")
    print("=" * 80)

    cycles = find_circular_dependencies(gk_skills)
    if cycles:
        for i, cycle in enumerate(cycles, 1):
            print(f"\nCircle {i}: {' -> '.join(cycle)}")
    else:
        print("\nNo circular dependencies found")

    print("\n\n" + "=" * 80)
    print("REDUNDANT TRANSITIVE DEPENDENCIES")
    print("=" * 80)

    redundant = find_redundant_transitive_deps(gk_skills)
    if redundant:
        grouped = defaultdict(list)
        for item in redundant:
            grouped[item['skill']].append(item)

        for skill_id in sorted(grouped.keys()):
            print(f"\n{skill_id}: {gk_skills[skill_id]['name']}")
            for item in grouped[skill_id]:
                print(f"  {item['redundant_dep']} is redundant (reachable via {item['reachable_via']})")
    else:
        print("\nNo redundant dependencies found")

    print("\n\n" + "=" * 80)
    print("TOPIC OVERLAP (Skills with similar content across topics)")
    print("=" * 80)

    overlaps = analyze_topic_overlap(gk_skills)
    if overlaps:
        # Sort by number of skills sharing the keyword
        overlaps.sort(key=lambda x: len(x['skills']), reverse=True)

        for overlap in overlaps[:20]:  # Show top 20
            print(f"\nKeyword: '{overlap['keyword']}' appears in {len(overlap['skills'])} skills:")
            for skill_id, name, topic in overlap['skills']:
                print(f"  {skill_id} ({topic}): {name}")
    else:
        print("\nNo significant overlaps found")

    print("\n\n" + "=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)
    print(f"Total Grade K skills: {len(gk_skills)}")
    print(f"Topics with GK skills: {len(by_topic)}")
    print(f"X-2 violations: {len(violations)}")
    print(f"Missing cross-topic deps: {len(missing)}")
    print(f"Circular dependencies: {len(cycles)}")
    print(f"Redundant dependencies: {len(redundant)}")
    print(f"Keyword overlaps: {len(overlaps)}")

    # Detailed dependency analysis
    print("\n\n" + "=" * 80)
    print("CROSS-TOPIC DEPENDENCY MATRIX")
    print("=" * 80)

    # Build cross-topic dependency counts
    cross_topic_deps = defaultdict(lambda: defaultdict(int))

    for skill_id, skill_data in gk_skills.items():
        source_topic = get_topic_number(skill_id)
        for dep in skill_data['dependencies']:
            target_topic = get_topic_number(dep)
            if source_topic != target_topic:
                cross_topic_deps[source_topic][target_topic] += 1

    if cross_topic_deps:
        print("\nTopics that depend on other topics:")
        for source in sorted(cross_topic_deps.keys()):
            print(f"\n{source} depends on:")
            for target, count in sorted(cross_topic_deps[source].items()):
                print(f"  {target}: {count} dependencies")
    else:
        print("\nNo cross-topic dependencies found")

if __name__ == '__main__':
    main()
