#!/usr/bin/env python3
"""
Validate Grade K dependencies in allskills.md
"""

import re
from collections import defaultdict, deque

def parse_allskills(filepath):
    """Parse allskills.md and extract all Grade K skills"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    sections = content.split('\nID: ')

    for section in sections:
        if not section.strip():
            continue

        if not section.startswith('ID:'):
            section = 'ID: ' + section

        id_match = re.search(r'ID: (T\d+\.GK\.\d+)', section)
        if not id_match:
            continue

        skill_id = id_match.group(1)
        topic_match = re.search(r'Topic: ([^\n]+)', section)
        topic = topic_match.group(1).strip() if topic_match else ''
        skill_match = re.search(r'Skill: ([^\n]+)', section)
        skill_name = skill_match.group(1).strip() if skill_match else ''

        deps = []
        dep_match = re.search(r'Dependencies:\s*\n((?:\* [^\n]+\n?)*)', section, re.MULTILINE)
        if dep_match:
            dep_text = dep_match.group(1)
            for line in dep_text.split('\n'):
                line = line.strip()
                if line.startswith('*'):
                    dep_id_match = re.search(r'(T\d+\.[A-Z0-9]+\.\d+)', line)
                    if dep_id_match:
                        deps.append(dep_id_match.group(1))

        skills[skill_id] = {
            'topic': topic,
            'skill': skill_name,
            'dependencies': deps,
        }

    return skills

def find_circular_dependencies(skills):
    """Find circular dependencies using DFS"""
    def has_cycle(node, visited, rec_stack, path):
        visited.add(node)
        rec_stack.add(node)
        path.append(node)

        if node in skills:
            for dep in skills[node]['dependencies']:
                if dep not in visited:
                    if has_cycle(dep, visited, rec_stack, path):
                        return True
                elif dep in rec_stack:
                    # Found a cycle
                    cycle_start = path.index(dep)
                    return path[cycle_start:] + [dep]

        path.pop()
        rec_stack.remove(node)
        return False

    cycles = []
    for skill_id in skills:
        visited = set()
        rec_stack = set()
        path = []
        result = has_cycle(skill_id, visited, rec_stack, path)
        if result and result is not True:
            cycles.append(result)

    return cycles

def find_transitive_redundancies(skills):
    """Find transitive redundancies in dependencies"""
    redundancies = []

    for skill_id, skill_data in skills.items():
        if not skill_data['dependencies']:
            continue

        # For each direct dependency
        for direct_dep in skill_data['dependencies']:
            if direct_dep not in skills:
                continue

            # Find all reachable nodes from this dependency
            reachable = set()
            queue = deque([direct_dep])
            visited = set([direct_dep])

            while queue:
                current = queue.popleft()
                if current not in skills:
                    continue

                for dep in skills[current]['dependencies']:
                    if dep not in visited:
                        visited.add(dep)
                        reachable.add(dep)
                        queue.append(dep)

            # Check if any other direct dependencies are reachable
            for other_dep in skill_data['dependencies']:
                if other_dep != direct_dep and other_dep in reachable:
                    redundancies.append({
                        'skill': skill_id,
                        'direct': other_dep,
                        'transitive_through': direct_dep,
                        'description': f"{skill_id} → {other_dep} is redundant (reachable via {direct_dep})"
                    })

    return redundancies

def validate_grade_levels(skills):
    """Check for invalid grade level dependencies"""
    invalid = []

    for skill_id, skill_data in skills.items():
        for dep in skill_data['dependencies']:
            # Check if dependency is a GK skill
            if not dep.startswith('T') or '.GK.' not in dep:
                invalid.append({
                    'skill': skill_id,
                    'invalid_dep': dep,
                    'reason': f"Grade K skill depends on non-GK skill: {dep}"
                })
            # Check if dependency exists
            elif dep not in skills:
                invalid.append({
                    'skill': skill_id,
                    'invalid_dep': dep,
                    'reason': f"Dependency not found: {dep}"
                })

    return invalid

def analyze_dependency_graph(skills):
    """Analyze dependency graph structure"""
    stats = {
        'total_skills': len(skills),
        'skills_with_deps': sum(1 for s in skills.values() if s['dependencies']),
        'skills_without_deps': sum(1 for s in skills.values() if not s['dependencies']),
        'total_dependencies': sum(len(s['dependencies']) for s in skills.values()),
        'cross_topic_deps': 0,
        'intra_topic_deps': 0,
        'max_deps': 0,
        'avg_deps': 0,
    }

    dep_counts = []
    for skill_id, skill_data in skills.items():
        topic = skill_id.split('.')[0]
        dep_count = len(skill_data['dependencies'])
        dep_counts.append(dep_count)

        if dep_count > stats['max_deps']:
            stats['max_deps'] = dep_count

        for dep in skill_data['dependencies']:
            dep_topic = dep.split('.')[0]
            if dep_topic == topic:
                stats['intra_topic_deps'] += 1
            else:
                stats['cross_topic_deps'] += 1

    if dep_counts:
        stats['avg_deps'] = sum(dep_counts) / len(dep_counts)

    # Find foundation skills (referenced by many others)
    references = defaultdict(int)
    for skill_data in skills.values():
        for dep in skill_data['dependencies']:
            references[dep] += 1

    stats['most_referenced'] = sorted(references.items(), key=lambda x: x[1], reverse=True)[:10]

    return stats

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = parse_allskills(filepath)

    print("="*80)
    print("GRADE K DEPENDENCY VALIDATION")
    print("="*80)

    # 1. Check for invalid grade levels
    print("\n1. CHECKING INVALID GRADE LEVEL DEPENDENCIES...")
    invalid = validate_grade_levels(skills)
    if invalid:
        print(f"   ⚠ Found {len(invalid)} invalid dependencies:")
        for item in invalid:
            print(f"     {item['skill']} → {item['invalid_dep']}: {item['reason']}")
    else:
        print("   ✓ All dependencies are valid Grade K skills")

    # 2. Check for circular dependencies
    print("\n2. CHECKING CIRCULAR DEPENDENCIES...")
    cycles = find_circular_dependencies(skills)
    if cycles:
        print(f"   ⚠ Found {len(cycles)} circular dependencies:")
        for cycle in cycles:
            print(f"     {' → '.join(cycle)}")
    else:
        print("   ✓ No circular dependencies found")

    # 3. Check for transitive redundancies
    print("\n3. CHECKING TRANSITIVE REDUNDANCIES...")
    redundancies = find_transitive_redundancies(skills)
    if redundancies:
        print(f"   ℹ Found {len(redundancies)} potential transitive redundancies:")
        for item in redundancies[:20]:  # Show first 20
            print(f"     {item['description']}")
        if len(redundancies) > 20:
            print(f"     ... and {len(redundancies) - 20} more")
    else:
        print("   ✓ No transitive redundancies found")

    # 4. Analyze dependency graph
    print("\n4. DEPENDENCY GRAPH ANALYSIS...")
    stats = analyze_dependency_graph(skills)
    print(f"   Total skills: {stats['total_skills']}")
    print(f"   Skills with dependencies: {stats['skills_with_deps']}")
    print(f"   Skills without dependencies: {stats['skills_without_deps']}")
    print(f"   Total dependencies: {stats['total_dependencies']}")
    print(f"   Cross-topic dependencies: {stats['cross_topic_deps']}")
    print(f"   Intra-topic dependencies: {stats['intra_topic_deps']}")
    print(f"   Max dependencies per skill: {stats['max_deps']}")
    print(f"   Average dependencies per skill: {stats['avg_deps']:.2f}")

    print(f"\n   Most referenced skills (foundation skills):")
    for skill_id, count in stats['most_referenced'][:10]:
        if skill_id in skills:
            print(f"     {skill_id}: {count} references - {skills[skill_id]['skill']}")
        else:
            print(f"     {skill_id}: {count} references")

    # 5. Summary
    print("\n" + "="*80)
    print("VALIDATION SUMMARY")
    print("="*80)

    issues = []
    if invalid:
        issues.append(f"❌ {len(invalid)} invalid grade level dependencies")
    else:
        print("✓ No invalid grade level dependencies")

    if cycles:
        issues.append(f"❌ {len(cycles)} circular dependencies")
    else:
        print("✓ No circular dependencies")

    if redundancies:
        print(f"ℹ {len(redundancies)} transitive redundancies (review recommended)")
    else:
        print("✓ No transitive redundancies")

    if issues:
        print("\nISSUES TO FIX:")
        for issue in issues:
            print(f"  {issue}")
    else:
        print("\n✓ All validations passed!")

if __name__ == '__main__':
    main()
