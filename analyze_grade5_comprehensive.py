#!/usr/bin/env python3
"""
Comprehensive Grade 5 Dependency Analysis
Analyzes ALL Grade 5 skills across all 36 topics for cross-topic dependency issues.
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def parse_allskills(filepath: str) -> Dict:
    """Parse allskills.md and extract all skills by grade and topic."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split content by skill entries (ID: pattern)
    skill_entries = re.split(r'\n(?=ID: )', content)

    all_skills = defaultdict(lambda: defaultdict(list))
    skill_map = {}  # id -> skill info

    for entry in skill_entries:
        if not entry.strip() or not entry.startswith('ID:'):
            continue

        # Extract skill ID
        id_match = re.search(r'ID:\s*(T\d+\.(GK|G\d+)\.\d+)', entry)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic
        topic_match = re.search(r'Topic:\s*T(\d+)', entry)
        if not topic_match:
            continue
        topic_num = int(topic_match.group(1))

        # Extract topic name
        topic_name_match = re.search(r'Topic:\s*T\d+\s*[–-]\s*(.+?)(?:\n|$)', entry)
        topic_name = topic_name_match.group(1).strip() if topic_name_match else f"Topic {topic_num}"

        # Extract skill title
        skill_match = re.search(r'Skill:\s*(.+?)(?:\n|$)', entry)
        if not skill_match:
            continue
        title = skill_match.group(1).strip()

        # Determine grade from skill ID
        grade_match = re.search(r'\.(GK|G(\d+))\.', skill_id)
        if not grade_match:
            continue

        if grade_match.group(1) == 'GK':
            grade = 0  # Kindergarten
        else:
            grade = int(grade_match.group(2))

        # Extract dependencies
        dependencies = []
        deps_section = re.search(r'Dependencies:\s*\n((?:\*\s*.+?\n)+)', entry, re.MULTILINE)
        if deps_section:
            dep_lines = deps_section.group(1)
            # Extract all skill IDs from dependency lines
            deps = re.findall(r'(T\d+\.(GK|G\d+)\.\d+)', dep_lines)
            dependencies = [d[0] for d in deps]

        skill_info = {
            'id': skill_id,
            'title': title,
            'grade': grade,
            'topic': topic_num,
            'topic_name': topic_name,
            'dependencies': dependencies
        }

        all_skills[topic_num][grade].append(skill_info)
        skill_map[skill_id] = skill_info

    return {'by_topic': all_skills, 'skill_map': skill_map}

def get_skill_grade(skill_id: str, skill_map: Dict) -> int:
    """Get the grade of a skill by ID."""
    if skill_id in skill_map:
        return skill_map[skill_id]['grade']
    # Try to infer from ID format (T##.G#.##)
    match = re.search(r'\.(GK|G(\d+))\.', skill_id)
    if match:
        if match.group(1) == 'GK':
            return 0
        return int(match.group(2))
    return 0

def find_x2_violations(skill: Dict, skill_map: Dict) -> List[str]:
    """Find dependencies that violate X-2 rule (G5 depending on G6+)."""
    violations = []
    current_grade = skill['grade']

    for dep_id in skill['dependencies']:
        dep_grade = get_skill_grade(dep_id, skill_map)
        if dep_grade > current_grade:
            violations.append(dep_id)

    return violations

def find_missing_cross_topic_deps(skill: Dict, skill_map: Dict) -> List[Tuple[str, str]]:
    """
    Find missing cross-topic dependencies for Grade 5 skills.
    Returns list of (dep_id, reason) tuples.
    Be conservative - only suggest clear prerequisite relationships.
    """
    missing_set = set()  # Use set to avoid duplicates
    skill_id = skill['id']
    topic = skill['topic']
    title_lower = skill['title'].lower()
    current_deps = set(skill['dependencies'])

    # Helper function to add candidate if it exists and meets criteria
    def add_candidate(dep_id: str, reason: str):
        if dep_id not in current_deps and dep_id in skill_map:
            dep_skill = skill_map[dep_id]
            if dep_skill['grade'] < 5 and dep_skill['topic'] != topic:
                # Only add cross-topic dependencies
                missing_set.add((dep_id, reason))

    # Keyword-based detection for specific prerequisite concepts
    # Only suggest dependencies that are genuinely necessary

    # Variables needed for skills with "score", "variable", "data"
    if any(kw in title_lower for kw in ['score', 'variable', 'data', 'counter']):
        # Look for actual variable skills in T17
        for sid, sinfo in skill_map.items():
            if sinfo['topic'] == 17 and sinfo['grade'] in [3, 4]:
                if 'variable' in sinfo['title'].lower() or 'data' in sinfo['title'].lower():
                    add_candidate(sid, f"Variable skills from {sinfo['topic_name']}")

    # Sensing needed for interactive features
    if any(kw in title_lower for kw in ['touch', 'click', 'mouse', 'key', 'answer', 'sensing']):
        # Look for sensing skills in T13
        for sid, sinfo in skill_map.items():
            if sinfo['topic'] == 13 and sinfo['grade'] in [3, 4]:
                if any(kw in sinfo['title'].lower() for kw in ['mouse', 'key', 'sensing', 'touch']):
                    add_candidate(sid, f"Sensing skills from {sinfo['topic_name']}")

    # List/array operations
    if any(kw in title_lower for kw in ['list', 'item', 'add to list', 'delete', 'insert']):
        # Look for list skills in T17
        for sid, sinfo in skill_map.items():
            if sinfo['topic'] == 17 and sinfo['grade'] in [3, 4]:
                if 'list' in sinfo['title'].lower():
                    add_candidate(sid, f"List operations from {sinfo['topic_name']}")

    # Conditional logic
    if any(kw in title_lower for kw in ['if', 'condition', 'conditional', 'else']):
        # Look for conditional skills in T09
        for sid, sinfo in skill_map.items():
            if sinfo['topic'] == 9 and sinfo['grade'] in [3, 4]:
                if any(kw in sinfo['title'].lower() for kw in ['if', 'condition', 'compare']):
                    add_candidate(sid, f"Conditional logic from {sinfo['topic_name']}")

    # Loops
    if any(kw in title_lower for kw in ['repeat', 'loop', 'forever', 'until', 'nested']):
        # Look for loop skills in T10
        for sid, sinfo in skill_map.items():
            if sinfo['topic'] == 10 and sinfo['grade'] in [3, 4]:
                if any(kw in sinfo['title'].lower() for kw in ['repeat', 'loop', 'forever']):
                    add_candidate(sid, f"Loop structures from {sinfo['topic_name']}")

    # Broadcasting/messages
    if any(kw in title_lower for kw in ['broadcast', 'message', 'signal', 'send']):
        # Look for broadcast skills in T23
        for sid, sinfo in skill_map.items():
            if sinfo['topic'] == 23 and sinfo['grade'] in [3, 4]:
                if any(kw in sinfo['title'].lower() for kw in ['broadcast', 'message']):
                    add_candidate(sid, f"Broadcasting from {sinfo['topic_name']}")

    # Cloning
    if any(kw in title_lower for kw in ['clone', 'copy', 'duplicate']):
        # Look for clone skills in T22
        for sid, sinfo in skill_map.items():
            if sinfo['topic'] == 22 and sinfo['grade'] in [3, 4]:
                if 'clone' in sinfo['title'].lower():
                    add_candidate(sid, f"Cloning from {sinfo['topic_name']}")

    # Functions/custom blocks/procedures
    if any(kw in title_lower for kw in ['function', 'procedure', 'custom block', 'define', 'parameter']):
        # Look for procedure skills in T12
        for sid, sinfo in skill_map.items():
            if sinfo['topic'] == 12 and sinfo['grade'] in [3, 4]:
                if any(kw in sinfo['title'].lower() for kw in ['procedure', 'function', 'parameter']):
                    add_candidate(sid, f"Procedures from {sinfo['topic_name']}")

    # Events
    if any(kw in title_lower for kw in ['event', 'when', 'trigger']):
        # Look for event skills in T19/T20
        for sid, sinfo in skill_map.items():
            if sinfo['topic'] in [19, 20] and sinfo['grade'] in [3, 4]:
                if any(kw in sinfo['title'].lower() for kw in ['event', 'when', 'start']):
                    add_candidate(sid, f"Events from {sinfo['topic_name']}")

    return list(missing_set)

def find_circular_dependencies(skill: Dict, skill_map: Dict, visited: Set = None, path: Set = None) -> List[List[str]]:
    """Find circular dependencies starting from this skill."""
    if visited is None:
        visited = set()
    if path is None:
        path = set()

    cycles = []
    skill_id = skill['id']

    if skill_id in path:
        # Found a cycle
        return [[skill_id]]

    if skill_id in visited:
        return []

    visited.add(skill_id)
    path.add(skill_id)

    for dep_id in skill['dependencies']:
        if dep_id in skill_map:
            dep_cycles = find_circular_dependencies(skill_map[dep_id], skill_map, visited, path)
            for cycle in dep_cycles:
                cycle.append(skill_id)
                cycles.append(cycle)

    path.remove(skill_id)
    return cycles

def find_redundant_transitive_deps(skill: Dict, skill_map: Dict) -> List[Tuple[str, str]]:
    """
    Find truly redundant transitive dependencies.
    A dependency D is redundant if there exists another dependency P such that D is in P's dependency tree.
    Be conservative - only flag clear redundancies.
    """
    redundant = []
    skill_deps = skill['dependencies']

    if len(skill_deps) <= 1:
        return []

    # Build reachability map for each direct dependency
    reachable_from = {}
    for dep_id in skill_deps:
        reachable = set()
        if dep_id in skill_map:
            # BFS to find all reachable skills
            queue = [dep_id]
            visited = set([dep_id])
            while queue:
                current = queue.pop(0)
                if current in skill_map:
                    for next_dep in skill_map[current]['dependencies']:
                        if next_dep not in visited:
                            visited.add(next_dep)
                            reachable.add(next_dep)
                            queue.append(next_dep)
        reachable_from[dep_id] = reachable

    # Check for redundancies
    for dep_id in skill_deps:
        # Is this dependency reachable from any other direct dependency?
        for other_dep_id in skill_deps:
            if other_dep_id != dep_id and dep_id in reachable_from[other_dep_id]:
                reason = f"Reachable via {other_dep_id}"
                redundant.append((dep_id, reason))
                break

    return redundant

def analyze_grade5_comprehensive(filepath: str):
    """Main analysis function."""
    print("=" * 80)
    print("COMPREHENSIVE GRADE 5 DEPENDENCY ANALYSIS")
    print("=" * 80)
    print()

    # Parse skills
    print("Step 1: Parsing allskills.md...")
    data = parse_allskills(filepath)
    all_skills_by_topic = data['by_topic']
    skill_map = data['skill_map']

    # Collect all Grade 5 skills
    grade5_skills = []
    for topic_num in sorted(all_skills_by_topic.keys()):
        if 5 in all_skills_by_topic[topic_num]:
            grade5_skills.extend(all_skills_by_topic[topic_num][5])

    print(f"Found {len(grade5_skills)} Grade 5 skills across {len(all_skills_by_topic)} topics")
    print()

    # Analysis results
    issues = {
        'x2_violations': [],
        'missing_cross_topic': [],
        'circular_deps': [],
        'redundant_deps': []
    }

    changes_by_topic = defaultdict(list)

    print("Step 2: Analyzing dependencies for all Grade 5 skills...")
    print()

    for skill in grade5_skills:
        topic = skill['topic']
        skill_id = skill['id']

        # Check X-2 violations
        violations = find_x2_violations(skill, skill_map)
        for violation in violations:
            issues['x2_violations'].append({
                'skill': skill,
                'violation': violation
            })
            changes_by_topic[topic].append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'change_type': 'REMOVE',
                'dependency': violation,
                'rationale': f"X-2 rule violation: Grade 5 cannot depend on Grade {get_skill_grade(violation, skill_map)}"
            })

        # Check missing cross-topic dependencies
        missing = find_missing_cross_topic_deps(skill, skill_map)
        for dep_id, reason in missing:
            issues['missing_cross_topic'].append({
                'skill': skill,
                'missing_dep': dep_id,
                'reason': reason
            })
            changes_by_topic[topic].append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'change_type': 'ADD',
                'dependency': dep_id,
                'rationale': reason
            })

        # Check circular dependencies
        cycles = find_circular_dependencies(skill, skill_map)
        if cycles:
            for cycle in cycles:
                if skill_id in cycle:
                    issues['circular_deps'].append({
                        'skill': skill,
                        'cycle': cycle
                    })

        # Check redundant dependencies (be conservative)
        redundant = find_redundant_transitive_deps(skill, skill_map)
        for dep_id, reason in redundant:
            issues['redundant_deps'].append({
                'skill': skill,
                'redundant_dep': dep_id,
                'reason': reason
            })
            # Only suggest removal if truly redundant (appears multiple times in different paths)
            # For now, we'll flag but not auto-remove

    # Generate report
    print("=" * 80)
    print("ANALYSIS SUMMARY")
    print("=" * 80)
    print()
    print(f"Total Grade 5 Skills Analyzed: {len(grade5_skills)}")
    print(f"Topics Covered: {len(all_skills_by_topic)}")
    print()
    print("Issues Found:")
    print(f"  - X-2 Rule Violations: {len(issues['x2_violations'])}")
    print(f"  - Missing Cross-Topic Dependencies: {len(issues['missing_cross_topic'])}")
    print(f"  - Circular Dependencies: {len(issues['circular_deps'])}")
    print(f"  - Potentially Redundant Dependencies: {len(issues['redundant_deps'])}")
    print()

    # Detailed changes by topic
    print("=" * 80)
    print("DETAILED DEPENDENCY CHANGES BY TOPIC")
    print("=" * 80)
    print()

    total_changes = 0
    for topic_num in sorted(changes_by_topic.keys()):
        topic_name = next((s['topic_name'] for s in grade5_skills if s['topic'] == topic_num), f"Topic {topic_num}")
        changes = changes_by_topic[topic_num]

        if not changes:
            continue

        print(f"Topic {topic_num}: {topic_name}")
        print("-" * 80)

        # Group by skill
        changes_by_skill = defaultdict(list)
        for change in changes:
            changes_by_skill[change['skill_id']].append(change)

        for skill_id in sorted(changes_by_skill.keys()):
            skill_changes = changes_by_skill[skill_id]
            skill_title = skill_changes[0]['skill_title']
            print(f"\n[{skill_id}] {skill_title}")

            for change in skill_changes:
                dep_id = change['dependency']
                dep_info = ""
                if dep_id in skill_map:
                    dep_skill = skill_map[dep_id]
                    dep_info = f" ({dep_skill['title']})"

                print(f"  {change['change_type']} dependency: {dep_id}{dep_info}")
                print(f"    Rationale: {change['rationale']}")
                total_changes += 1

        print()

    print("=" * 80)
    print(f"TOTAL CHANGES RECOMMENDED: {total_changes}")
    print("=" * 80)
    print()

    # Circular dependencies detail
    if issues['circular_deps']:
        print("=" * 80)
        print("CIRCULAR DEPENDENCIES REQUIRING ATTENTION")
        print("=" * 80)
        print()
        print("The following circular dependencies were detected and require manual review:")
        print()

        for issue in issues['circular_deps']:
            skill = issue['skill']
            cycle = issue['cycle']
            print(f"[{skill['id']}] {skill['title']}")
            print(f"  Cycle: {' -> '.join(reversed(cycle))}")
            print()

    # Redundant dependencies detail
    if issues['redundant_deps']:
        print("=" * 80)
        print("POTENTIALLY REDUNDANT DEPENDENCIES")
        print("=" * 80)
        print()
        print("The following dependencies may be redundant (conservative analysis):")
        print("Review manually before removing - keeping them does no harm.")
        print()

        redundant_by_skill = defaultdict(list)
        for issue in issues['redundant_deps']:
            skill_id = issue['skill']['id']
            redundant_by_skill[skill_id].append(issue)

        for skill_id in sorted(redundant_by_skill.keys()):
            skill = redundant_by_skill[skill_id][0]['skill']
            print(f"[{skill_id}] {skill['title']}")
            for issue in redundant_by_skill[skill_id]:
                dep_id = issue['redundant_dep']
                reason = issue['reason']
                print(f"  {dep_id}: {reason}")
            print()

    print()
    print("Analysis complete!")

    # Write structured report
    write_structured_report(filepath, grade5_skills, changes_by_topic, issues, total_changes)

    return changes_by_topic, issues

def write_structured_report(filepath: str, grade5_skills: List, changes_by_topic: Dict, issues: Dict, total_changes: int):
    """Write a structured markdown report."""
    report_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/GRADE5_DEPENDENCY_REPORT.md"

    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# Grade 5 Comprehensive Dependency Analysis Report\n\n")
        f.write(f"**Analysis Date:** 2024-11-24\n\n")
        f.write(f"**Source File:** {filepath}\n\n")

        f.write("## Executive Summary\n\n")
        f.write(f"- **Total Grade 5 Skills Analyzed:** {len(grade5_skills)}\n")
        f.write(f"- **Total Dependency Changes Recommended:** {total_changes}\n")
        f.write(f"- **X-2 Rule Violations:** {len(issues['x2_violations'])}\n")
        f.write(f"- **Missing Cross-Topic Dependencies:** {len(issues['missing_cross_topic'])}\n")
        f.write(f"- **Circular Dependencies Detected:** {len(issues['circular_deps'])}\n")
        f.write(f"- **Potentially Redundant Dependencies:** {len(issues['redundant_deps'])}\n\n")

        f.write("## Changes by Topic\n\n")
        f.write("### Summary Table\n\n")
        f.write("| Topic | Topic Name | Skills Affected | Changes |\n")
        f.write("|-------|------------|-----------------|----------|\n")

        for topic_num in sorted(changes_by_topic.keys()):
            topic_name = next((s['topic_name'] for s in grade5_skills if s['topic'] == topic_num), f"Topic {topic_num}")
            changes = changes_by_topic[topic_num]
            skills_affected = len(set(c['skill_id'] for c in changes))
            num_changes = len(changes)
            f.write(f"| {topic_num:02d} | {topic_name} | {skills_affected} | {num_changes} |\n")

        f.write("\n### Detailed Changes\n\n")

        for topic_num in sorted(changes_by_topic.keys()):
            topic_name = next((s['topic_name'] for s in grade5_skills if s['topic'] == topic_num), f"Topic {topic_num}")
            changes = changes_by_topic[topic_num]

            if not changes:
                continue

            f.write(f"#### Topic {topic_num}: {topic_name}\n\n")

            # Group by skill
            changes_by_skill = defaultdict(list)
            for change in changes:
                changes_by_skill[change['skill_id']].append(change)

            for skill_id in sorted(changes_by_skill.keys()):
                skill_changes = changes_by_skill[skill_id]
                skill_title = skill_changes[0]['skill_title']
                f.write(f"**[{skill_id}] {skill_title}**\n\n")

                for change in skill_changes:
                    dep_id = change['dependency']
                    f.write(f"- **{change['change_type']}** dependency: `{dep_id}`\n")
                    f.write(f"  - Rationale: {change['rationale']}\n")

                f.write("\n")

        if issues['circular_deps']:
            f.write("## Circular Dependencies\n\n")
            f.write("The following circular dependencies require manual review:\n\n")

            seen_cycles = set()
            for issue in issues['circular_deps']:
                skill = issue['skill']
                cycle = issue['cycle']
                cycle_str = ' -> '.join(reversed(cycle))
                if cycle_str not in seen_cycles:
                    seen_cycles.add(cycle_str)
                    f.write(f"- **[{skill['id']}]** {skill['title']}\n")
                    f.write(f"  - Cycle: `{cycle_str}`\n\n")

        if issues['redundant_deps']:
            f.write("## Potentially Redundant Dependencies\n\n")
            f.write("Review these dependencies manually. Keeping them does no harm:\n\n")

            redundant_by_skill = defaultdict(list)
            for issue in issues['redundant_deps']:
                skill_id = issue['skill']['id']
                redundant_by_skill[skill_id].append(issue)

            for skill_id in sorted(redundant_by_skill.keys()):
                skill = redundant_by_skill[skill_id][0]['skill']
                f.write(f"- **[{skill_id}]** {skill['title']}\n")
                for issue in redundant_by_skill[skill_id]:
                    dep_id = issue['redundant_dep']
                    reason = issue['reason']
                    f.write(f"  - `{dep_id}`: {reason}\n")
                f.write("\n")

        f.write("## Implementation Notes\n\n")
        f.write("### Critical Rules\n\n")
        f.write("- **NEVER delete skills**\n")
        f.write("- Only remove dependencies if genuinely incorrect or truly redundant\n")
        f.write("- Be conservative - when in doubt, keep dependencies\n")
        f.write("- Add dependencies liberally for prerequisites\n")
        f.write("- Focus on cross-topic connections\n\n")

        f.write("### Next Steps\n\n")
        f.write("1. Review suggested dependency additions\n")
        f.write("2. Manually resolve circular dependencies\n")
        f.write("3. Apply changes to allskills.md\n")
        f.write("4. Validate with automated tests\n\n")

    print(f"\nStructured report written to: {report_path}")

if __name__ == "__main__":
    filepath = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"
    analyze_grade5_comprehensive(filepath)
