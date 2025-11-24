#!/usr/bin/env python3
"""
Validate Grade 1 Cross-Topic Dependencies
- Build complete dependency graph (existing + proposed)
- Detect and remove circular dependencies
- Validate X-2 rule (Grade 1 skills can only depend on K or 1)
- Output validated new dependencies
"""

import re
from collections import defaultdict, deque
from typing import Set, Dict, List, Tuple

def parse_skill_id(skill_id: str) -> Tuple[str, str]:
    """Parse skill ID to extract topic and grade. Returns (topic, grade)"""
    # Format: T01.G1.01 or T01.GK.01
    match = re.match(r'T(\d+)\.(G[K\d]+)\.', skill_id)
    if match:
        topic = match.group(1)
        grade = match.group(2)
        return (topic, grade)
    return (None, None)

def get_grade_number(grade_str: str) -> int:
    """Convert grade string to number (GK=0, G1=1, G2=2, etc.)"""
    if grade_str == 'GK':
        return 0
    elif grade_str.startswith('G'):
        try:
            return int(grade_str[1:])
        except:
            return -1
    return -1

def load_existing_dependencies(analysis_file: str) -> Dict[str, Set[str]]:
    """Load existing dependencies from GRADE_1_COMPLETE_ANALYSIS.md"""
    deps = defaultdict(set)

    with open(analysis_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse the markdown file
    current_skill = None
    in_dependencies = False

    lines = content.split('\n')
    for i, line in enumerate(lines):
        # Look for skill headers like "#### T01.G1.01:"
        skill_match = re.match(r'####\s+(T\d+\.G[K\d]+\.\d+):', line)
        if skill_match:
            current_skill = skill_match.group(1)
            in_dependencies = False
            continue

        # Look for Dependencies section
        if current_skill and line.strip().startswith('- **Dependencies:**'):
            in_dependencies = True
            continue

        # Parse dependency lines like "  - T01.GK.02: Put pictures in order for coming to class"
        if current_skill and in_dependencies:
            dep_match = re.match(r'\s+- (T\d+\.G[K\d]+\.\d+):', line)
            if dep_match:
                dep_id = dep_match.group(1)
                deps[current_skill].add(dep_id)
            elif line.strip() and not line.strip().startswith('-'):
                # End of dependencies section
                in_dependencies = False

    return deps

def load_proposed_dependencies(proposed_file: str) -> List[Tuple[str, str, str]]:
    """Load proposed dependencies from GRADE1_DEPENDENCIES_TO_APPLY.txt"""
    deps = []

    with open(proposed_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Format: T01.G1.02 -> T03.G1.02: Requires understanding breaking tasks into parts
            match = re.match(r'(T\d+\.G[K\d]+\.\d+)\s*->\s*(T\d+\.G[K\d]+\.\d+):\s*(.+)', line)
            if match:
                skill_id = match.group(1)
                dep_id = match.group(2)
                reason = match.group(3)
                deps.append((skill_id, dep_id, reason))

    return deps

def build_adjacency_list(dependencies: Dict[str, Set[str]]) -> Dict[str, Set[str]]:
    """Build adjacency list from dependencies"""
    return {k: set(v) for k, v in dependencies.items()}

def detect_cycle_dfs(graph: Dict[str, Set[str]], start: str, visited: Set[str], rec_stack: Set[str], path: List[str]) -> List[str]:
    """Detect cycle using DFS. Returns cycle path if found, empty list otherwise."""
    visited.add(start)
    rec_stack.add(start)
    path.append(start)

    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in visited:
                cycle = detect_cycle_dfs(graph, neighbor, visited, rec_stack, path)
                if cycle:
                    return cycle
            elif neighbor in rec_stack:
                # Found cycle
                cycle_start_idx = path.index(neighbor)
                return path[cycle_start_idx:] + [neighbor]

    path.pop()
    rec_stack.remove(start)
    return []

def find_all_cycles(graph: Dict[str, Set[str]]) -> List[List[str]]:
    """Find all cycles in the graph"""
    cycles = []
    visited = set()

    for node in graph:
        if node not in visited:
            rec_stack = set()
            path = []
            cycle = detect_cycle_dfs(graph, node, visited, rec_stack, path)
            if cycle:
                cycles.append(cycle)

    return cycles

def validate_x2_rule(skill_id: str, dep_id: str) -> bool:
    """
    Validate X-2 rule: Grade 1 skills can only depend on Grade K or Grade 1 skills
    Returns True if valid, False otherwise
    """
    skill_topic, skill_grade = parse_skill_id(skill_id)
    dep_topic, dep_grade = parse_skill_id(dep_id)

    if skill_grade == 'G1':
        # Grade 1 can depend on GK or G1
        return dep_grade in ['GK', 'G1']

    return True  # Not a G1 skill, so rule doesn't apply

def is_already_existing(skill_id: str, dep_id: str, existing_deps: Dict[str, Set[str]]) -> bool:
    """Check if dependency already exists"""
    return dep_id in existing_deps.get(skill_id, set())

def remove_cycle_edge(cycle: List[str], graph: Dict[str, Set[str]], proposed_deps: Set[Tuple[str, str]]) -> Tuple[str, str]:
    """
    Remove one edge from the cycle.
    Prefer removing edges that are newly proposed.
    Returns the removed edge (from, to)
    """
    # Find edges in the cycle
    cycle_edges = []
    for i in range(len(cycle) - 1):
        from_node = cycle[i]
        to_node = cycle[i + 1]
        is_proposed = (from_node, to_node) in proposed_deps
        cycle_edges.append((from_node, to_node, is_proposed))

    # Prefer removing proposed edges over existing ones
    proposed_edges = [e for e in cycle_edges if e[2]]
    if proposed_edges:
        # Remove the first proposed edge
        from_node, to_node, _ = proposed_edges[0]
    else:
        # Remove the first edge if no proposed edges
        from_node, to_node, _ = cycle_edges[0]

    # Remove from graph
    if from_node in graph and to_node in graph[from_node]:
        graph[from_node].remove(to_node)

    return (from_node, to_node)

def main():
    analysis_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE_1_COMPLETE_ANALYSIS.md'
    proposed_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE1_DEPENDENCIES_TO_APPLY.txt'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE1_VALIDATED_NEW_DEPS.txt'

    print("Loading existing dependencies...")
    existing_deps = load_existing_dependencies(analysis_file)
    print(f"Loaded {sum(len(v) for v in existing_deps.values())} existing dependencies for {len(existing_deps)} skills")

    print("\nLoading proposed dependencies...")
    proposed_deps_list = load_proposed_dependencies(proposed_file)
    print(f"Loaded {len(proposed_deps_list)} proposed dependencies")

    # Build complete graph with both existing and proposed dependencies
    print("\nBuilding complete dependency graph...")
    complete_graph = defaultdict(set)

    # Add existing dependencies
    for skill_id, deps in existing_deps.items():
        complete_graph[skill_id].update(deps)

    # Track proposed deps for cycle removal preference
    proposed_deps_set = set()
    for skill_id, dep_id, reason in proposed_deps_list:
        proposed_deps_set.add((skill_id, dep_id))
        complete_graph[skill_id].add(dep_id)

    print(f"Complete graph has {len(complete_graph)} skills with dependencies")

    # Detect and remove cycles
    print("\nDetecting circular dependencies...")
    removed_due_to_cycles = []
    max_iterations = 1000  # Prevent infinite loop
    iteration = 0

    while iteration < max_iterations:
        cycles = find_all_cycles(complete_graph)
        if not cycles:
            break

        print(f"  Found {len(cycles)} cycle(s)")
        for cycle in cycles:
            print(f"    Cycle: {' -> '.join(cycle)}")
            from_node, to_node = remove_cycle_edge(cycle, complete_graph, proposed_deps_set)
            print(f"    Removed edge: {from_node} -> {to_node}")

            # Track if this was a proposed dependency
            if (from_node, to_node) in proposed_deps_set:
                removed_due_to_cycles.append((from_node, to_node))
                proposed_deps_set.remove((from_node, to_node))

        iteration += 1

    if iteration >= max_iterations:
        print("WARNING: Max iterations reached while removing cycles!")

    print(f"\nRemoved {len(removed_due_to_cycles)} proposed dependencies due to cycles")

    # Validate X-2 rule and filter out existing dependencies
    print("\nValidating X-2 rule and filtering...")
    validated_deps = []
    removed_x2_violations = []
    already_existing = []

    for skill_id, dep_id, reason in proposed_deps_list:
        # Skip if removed due to cycle
        if (skill_id, dep_id) in removed_due_to_cycles:
            continue

        # Check if already exists
        if is_already_existing(skill_id, dep_id, existing_deps):
            already_existing.append((skill_id, dep_id))
            continue

        # Validate X-2 rule
        if not validate_x2_rule(skill_id, dep_id):
            removed_x2_violations.append((skill_id, dep_id))
            continue

        # Valid dependency
        validated_deps.append((skill_id, dep_id, reason))

    print(f"Removed {len(removed_x2_violations)} dependencies due to X-2 rule violations")
    print(f"Filtered out {len(already_existing)} already existing dependencies")
    print(f"\nValidated {len(validated_deps)} new dependencies to add")

    # Write output
    print(f"\nWriting validated dependencies to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Grade 1 Validated New Dependencies\n")
        f.write(f"# Total: {len(validated_deps)} dependencies\n")
        f.write(f"# Removed due to cycles: {len(removed_due_to_cycles)}\n")
        f.write(f"# Removed due to X-2 violations: {len(removed_x2_violations)}\n")
        f.write(f"# Already existing: {len(already_existing)}\n")
        f.write("\n")

        if removed_due_to_cycles:
            f.write("# Dependencies removed due to cycles:\n")
            for skill_id, dep_id in removed_due_to_cycles:
                f.write(f"# CYCLE: {skill_id} -> {dep_id}\n")
            f.write("\n")

        if removed_x2_violations:
            f.write("# Dependencies removed due to X-2 rule violations:\n")
            for skill_id, dep_id in removed_x2_violations:
                f.write(f"# X-2 VIOLATION: {skill_id} -> {dep_id}\n")
            f.write("\n")

        f.write("# Format: SKILL_ID ADD_DEP DEPENDENCY_ID\n")
        f.write("\n")

        # Sort by skill_id for readability
        validated_deps.sort(key=lambda x: x[0])

        for skill_id, dep_id, reason in validated_deps:
            f.write(f"{skill_id} ADD_DEP {dep_id}\n")

    print("\n=== SUMMARY ===")
    print(f"Total proposed dependencies: {len(proposed_deps_list)}")
    print(f"Removed due to cycles: {len(removed_due_to_cycles)}")
    print(f"Removed due to X-2 violations: {len(removed_x2_violations)}")
    print(f"Already existing: {len(already_existing)}")
    print(f"Validated new dependencies: {len(validated_deps)}")
    print(f"\nOutput written to: {output_file}")

if __name__ == '__main__':
    main()
