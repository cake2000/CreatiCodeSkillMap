#!/usr/bin/env python3
"""
Comprehensive Grade 7 Cross-Topic Dependency Analysis
Analyzes all dependency issues including X-2 violations, circular deps, missing deps, etc.
"""

import json
import sys
from collections import defaultdict, deque
from typing import Set, List, Dict, Tuple

def load_grade7_skills(filepath):
    """Load Grade 7 skills from JSON file"""
    with open(filepath, 'r') as f:
        data = json.load(f)
        return data.get('skills', [])

def extract_grade_from_id(skill_id):
    """Extract grade number from skill ID (e.g., 'T01.G7.01' -> 7)"""
    # Handle new format: T01.G7.01
    if '.G' in skill_id:
        parts = skill_id.split('.G')
        if len(parts) > 1:
            grade_str = parts[1].split('.')[0]
            return int(grade_str) if grade_str.isdigit() else None

    # Handle old format: g7t1s1
    if skill_id.startswith('g') and len(skill_id) > 1:
        grade_str = ''
        for c in skill_id[1:]:
            if c.isdigit():
                grade_str += c
            else:
                break
        return int(grade_str) if grade_str else None
    return None

def extract_topic_from_id(skill_id):
    """Extract topic number from skill ID (e.g., 'T01.G7.01' -> 1 or 'g7t1s1' -> 1)"""
    # Handle new format: T01.G7.01
    if skill_id.startswith('T') and '.' in skill_id:
        topic_str = skill_id.split('.')[0][1:]  # Remove 'T' prefix
        return int(topic_str) if topic_str.isdigit() else None

    # Handle old format: g7t1s1
    if 't' in skill_id:
        topic_str = ''
        start = False
        for c in skill_id:
            if c == 't':
                start = True
            elif start and c.isdigit():
                topic_str += c
            elif start:
                break
        return int(topic_str) if topic_str else None
    return None

def extract_dep_id(dep_string):
    """Extract skill ID from dependency string (e.g., 'T01.G5.09: Description' -> 'T01.G5.09')"""
    if ':' in dep_string:
        return dep_string.split(':')[0].strip()
    return dep_string.strip()

def check_x2_violations(skills):
    """Find skills with dependencies outside grades 5-7 (X-2 rule violations)"""
    violations = []

    for skill in skills:
        skill_id = skill['id']
        skill_grade = extract_grade_from_id(skill_id)

        if skill_grade != 7:
            continue

        deps = skill.get('dependencies', [])

        for dep_string in deps:
            dep = extract_dep_id(dep_string)
            dep_grade = extract_grade_from_id(dep)

            if dep_grade is not None and dep_grade not in [5, 6, 7]:
                violations.append({
                    'skill_id': skill_id,
                    'skill_name': skill.get('skill', 'Unknown'),
                    'dependency': dep,
                    'dep_grade': dep_grade,
                    'problem': f'Depends on grade {dep_grade} (outside 5-7 range)'
                })

    return violations

def find_circular_dependencies(skills):
    """Detect circular dependency chains"""
    # Build adjacency list
    graph = defaultdict(list)
    skill_map = {}

    for skill in skills:
        skill_id = skill['id']
        skill_map[skill_id] = skill
        deps = skill.get('dependencies', [])
        for dep_string in deps:
            dep = extract_dep_id(dep_string)
            graph[skill_id].append(dep)

    # DFS to detect cycles
    def dfs(node, visited, rec_stack, path):
        visited.add(node)
        rec_stack.add(node)
        path.append(node)

        cycles = []

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                cycles.extend(dfs(neighbor, visited, rec_stack, path[:]))
            elif neighbor in rec_stack:
                # Found a cycle
                cycle_start = path.index(neighbor)
                cycle = path[cycle_start:] + [neighbor]
                cycles.append(cycle)

        rec_stack.remove(node)
        return cycles

    all_cycles = []
    visited = set()

    for skill in skills:
        skill_id = skill['id']
        if skill_id not in visited:
            cycles = dfs(skill_id, visited, set(), [])
            all_cycles.extend(cycles)

    # Remove duplicate cycles
    unique_cycles = []
    seen = set()
    for cycle in all_cycles:
        cycle_key = tuple(sorted(cycle))
        if cycle_key not in seen:
            seen.add(cycle_key)
            unique_cycles.append(cycle)

    return unique_cycles

def find_transitive_dependencies(skills):
    """Find redundant transitive dependencies"""
    skill_map = {s['id']: s for s in skills}
    redundant = []

    def get_all_indirect_deps(skill_id, exclude_direct=True):
        """Get all dependencies reachable through other dependencies"""
        visited = set()
        queue = deque()

        direct_deps = set()
        for dep_string in skill_map.get(skill_id, {}).get('dependencies', []):
            direct_deps.add(extract_dep_id(dep_string))

        # Start from direct dependencies
        for dep in direct_deps:
            queue.append(dep)

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            # Add dependencies of current
            for dep_string in skill_map.get(current, {}).get('dependencies', []):
                dep = extract_dep_id(dep_string)
                if dep not in visited:
                    queue.append(dep)

        # Return indirect deps (excluding direct)
        if exclude_direct:
            return visited - direct_deps
        return visited

    for skill in skills:
        skill_id = skill['id']
        direct_deps = set()
        for dep_string in skill.get('dependencies', []):
            direct_deps.add(extract_dep_id(dep_string))

        if len(direct_deps) <= 1:
            continue

        # Check each direct dependency
        for dep in direct_deps:
            # Get all deps reachable from OTHER direct dependencies
            other_direct = direct_deps - {dep}
            indirect_from_others = set()

            for other in other_direct:
                indirect_from_others.update(get_all_indirect_deps(other, exclude_direct=True))

            # If this dep is reachable through others, it's redundant
            if dep in indirect_from_others:
                redundant.append({
                    'skill_id': skill_id,
                    'skill_name': skill.get('skill', 'Unknown'),
                    'redundant_dep': dep,
                    'problem': f'Redundant - reachable through other dependencies'
                })

    return redundant

def analyze_topic_distribution(skills):
    """Analyze cross-topic dependencies and identify patterns"""
    topic_stats = defaultdict(lambda: {
        'total_skills': 0,
        'skills_with_cross_topic_deps': 0,
        'cross_topic_dep_count': 0,
        'same_topic_dep_count': 0
    })

    cross_topic_pairs = defaultdict(int)

    for skill in skills:
        skill_id = skill['id']
        skill_grade = extract_grade_from_id(skill_id)

        if skill_grade != 7:
            continue

        skill_topic = extract_topic_from_id(skill_id)
        topic_stats[skill_topic]['total_skills'] += 1

        deps = skill.get('dependencies', [])
        has_cross_topic = False

        for dep_string in deps:
            dep = extract_dep_id(dep_string)
            dep_topic = extract_topic_from_id(dep)

            if dep_topic == skill_topic:
                topic_stats[skill_topic]['same_topic_dep_count'] += 1
            else:
                topic_stats[skill_topic]['cross_topic_dep_count'] += 1
                has_cross_topic = True
                cross_topic_pairs[(skill_topic, dep_topic)] += 1

        if has_cross_topic:
            topic_stats[skill_topic]['skills_with_cross_topic_deps'] += 1

    return topic_stats, cross_topic_pairs

def find_gateway_skills(skills):
    """Identify skills that many others depend on"""
    dependency_count = defaultdict(int)
    skill_map = {s['id']: s for s in skills}

    for skill in skills:
        for dep_string in skill.get('dependencies', []):
            dep = extract_dep_id(dep_string)
            dependency_count[dep] += 1

    # Sort by dependency count
    gateway_skills = []
    for skill_id, count in sorted(dependency_count.items(), key=lambda x: x[1], reverse=True):
        if count >= 3:  # Threshold for "gateway" status
            skill = skill_map.get(skill_id)
            if skill:
                gateway_skills.append({
                    'skill_id': skill_id,
                    'skill_name': skill.get('skill', 'Unknown'),
                    'dependent_count': count,
                    'grade': extract_grade_from_id(skill_id),
                    'topic': extract_topic_from_id(skill_id)
                })

    return gateway_skills

def identify_isolated_skills(skills):
    """Find skills with no dependencies and no dependents"""
    skill_ids = {s['id'] for s in skills if extract_grade_from_id(s['id']) == 7}
    has_deps = set()
    is_dep = set()

    for skill in skills:
        skill_id = skill['id']
        skill_grade = extract_grade_from_id(skill_id)

        if skill_grade == 7:
            deps = skill.get('dependencies', [])
            if deps:
                has_deps.add(skill_id)

            for dep_string in deps:
                dep = extract_dep_id(dep_string)
                is_dep.add(dep)

    isolated = []
    for skill in skills:
        skill_id = skill['id']
        if extract_grade_from_id(skill_id) == 7:
            if skill_id not in has_deps and skill_id not in is_dep:
                isolated.append({
                    'skill_id': skill_id,
                    'skill_name': skill.get('skill', 'Unknown'),
                    'topic': extract_topic_from_id(skill_id)
                })

    return isolated

def find_topic_overlap(skills):
    """Identify skills that appear similar across topics"""
    # Group by name similarity
    name_groups = defaultdict(list)

    for skill in skills:
        if extract_grade_from_id(skill['id']) == 7:
            name = skill.get('skill', '').lower()
            # Create a simplified key
            key_words = set(name.split())
            for other_skill in skills:
                if extract_grade_from_id(other_skill['id']) == 7:
                    if skill['id'] != other_skill['id']:
                        other_name = other_skill.get('skill', '').lower()
                        other_words = set(other_name.split())

                        # Check for significant overlap
                        overlap = key_words & other_words
                        if len(overlap) >= 2:  # At least 2 common words
                            pair = tuple(sorted([skill['id'], other_skill['id']]))
                            if pair not in name_groups:
                                name_groups[tuple(sorted([skill['skill'], other_skill['skill']]))] = pair

    overlaps = []
    for names, (id1, id2) in name_groups.items():
        topic1 = extract_topic_from_id(id1)
        topic2 = extract_topic_from_id(id2)
        if topic1 != topic2:
            overlaps.append({
                'skill1_id': id1,
                'skill2_id': id2,
                'topic1': topic1,
                'topic2': topic2,
                'names': names
            })

    return overlaps

def generate_report(skills, output_file):
    """Generate comprehensive dependency analysis report"""

    print("Analyzing X-2 violations...")
    x2_violations = check_x2_violations(skills)

    print("Finding circular dependencies...")
    circular_deps = find_circular_dependencies(skills)

    print("Finding transitive dependencies...")
    transitive_deps = find_transitive_dependencies(skills)

    print("Analyzing topic distribution...")
    topic_stats, cross_topic_pairs = analyze_topic_distribution(skills)

    print("Identifying gateway skills...")
    gateway_skills = find_gateway_skills(skills)

    print("Finding isolated skills...")
    isolated_skills = identify_isolated_skills(skills)

    print("Checking topic overlap...")
    topic_overlaps = find_topic_overlap(skills)

    # Generate report
    with open(output_file, 'w') as f:
        f.write("# Grade 7 Comprehensive Dependency Analysis\n\n")
        f.write("## Executive Summary\n\n")

        f.write(f"- **Total Grade 7 Skills Analyzed**: {len([s for s in skills if extract_grade_from_id(s['id']) == 7])}\n")
        f.write(f"- **X-2 Rule Violations**: {len(x2_violations)}\n")
        f.write(f"- **Circular Dependencies**: {len(circular_deps)} cycles detected\n")
        f.write(f"- **Redundant Dependencies**: {len(transitive_deps)}\n")
        f.write(f"- **Gateway Skills**: {len(gateway_skills)} (depended on by 3+ skills)\n")
        f.write(f"- **Isolated Skills**: {len(isolated_skills)} (no deps, no dependents)\n")
        f.write(f"- **Topic Overlaps**: {len(topic_overlaps)} potential duplicates\n\n")

        # X-2 Violations
        f.write("## 1. X-2 Rule Violations\n\n")
        f.write("Grade 7 skills should only depend on grades 5-7.\n\n")

        if x2_violations:
            f.write(f"**Found {len(x2_violations)} violations:**\n\n")
            for v in x2_violations:
                f.write(f"### {v['skill_id']}: {v['skill_name']}\n")
                f.write(f"- **Problem**: {v['problem']}\n")
                f.write(f"- **Violating Dependency**: {v['dependency']} (Grade {v['dep_grade']})\n")
                f.write(f"- **Recommended Fix**: Remove dependency or replace with appropriate grade 5-7 skill\n\n")
        else:
            f.write("No X-2 violations found.\n\n")

        # Circular Dependencies
        f.write("## 2. Circular Dependencies\n\n")
        f.write("Circular dependencies create logical inconsistencies in the skill graph.\n\n")

        if circular_deps:
            f.write(f"**Found {len(circular_deps)} circular dependency chains:**\n\n")
            for i, cycle in enumerate(circular_deps, 1):
                f.write(f"### Cycle {i}\n")
                f.write(f"- **Chain**: {' -> '.join(cycle)}\n")
                f.write(f"- **Recommended Fix**: Break cycle by removing weakest dependency link\n\n")
        else:
            f.write("No circular dependencies detected.\n\n")

        # Redundant Dependencies
        f.write("## 3. Redundant Transitive Dependencies\n\n")
        f.write("Dependencies that are already reachable through other dependencies.\n\n")

        if transitive_deps:
            f.write(f"**Found {len(transitive_deps)} redundant dependencies:**\n\n")
            for rd in transitive_deps:
                f.write(f"### {rd['skill_id']}: {rd['skill_name']}\n")
                f.write(f"- **Redundant Dependency**: {rd['redundant_dep']}\n")
                f.write(f"- **Problem**: {rd['problem']}\n")
                f.write(f"- **Recommended Fix**: Remove redundant dependency\n\n")
        else:
            f.write("No redundant dependencies found.\n\n")

        # Topic Statistics
        f.write("## 4. Cross-Topic Dependency Analysis\n\n")

        f.write("### Topic Statistics\n\n")
        f.write("| Topic | Total Skills | Skills with Cross-Topic Deps | Same-Topic Deps | Cross-Topic Deps |\n")
        f.write("|-------|-------------|------------------------------|-----------------|------------------|\n")
        for topic in sorted(topic_stats.keys()):
            stats = topic_stats[topic]
            f.write(f"| Topic {topic} | {stats['total_skills']} | {stats['skills_with_cross_topic_deps']} | ")
            f.write(f"{stats['same_topic_dep_count']} | {stats['cross_topic_dep_count']} |\n")
        f.write("\n")

        f.write("### Cross-Topic Dependency Pairs\n\n")
        f.write("| From Topic | To Topic | Count |\n")
        f.write("|------------|----------|-------|\n")
        for (from_topic, to_topic), count in sorted(cross_topic_pairs.items(), key=lambda x: x[1], reverse=True):
            f.write(f"| Topic {from_topic} | Topic {to_topic} | {count} |\n")
        f.write("\n")

        # Gateway Skills
        f.write("## 5. Gateway Skills\n\n")
        f.write("Critical skills that many others depend on.\n\n")

        if gateway_skills:
            f.write(f"**Found {len(gateway_skills)} gateway skills:**\n\n")
            f.write("| Skill ID | Skill Name | Grade | Topic | Dependent Count |\n")
            f.write("|----------|------------|-------|-------|----------------|\n")
            for gs in gateway_skills[:20]:  # Top 20
                f.write(f"| {gs['skill_id']} | {gs['skill_name']} | {gs['grade']} | {gs['topic']} | {gs['dependent_count']} |\n")
            f.write("\n")

        # Isolated Skills
        f.write("## 6. Isolated Skills\n\n")
        f.write("Skills with no dependencies and no dependents - may need connection to skill graph.\n\n")

        if isolated_skills:
            f.write(f"**Found {len(isolated_skills)} isolated skills:**\n\n")
            for iso in isolated_skills:
                f.write(f"- **{iso['skill_id']}**: {iso['skill_name']} (Topic {iso['topic']})\n")
            f.write("\n")
        else:
            f.write("No isolated skills found.\n\n")

        # Topic Overlaps
        f.write("## 7. Potential Topic Overlaps\n\n")
        f.write("Skills with similar names across different topics.\n\n")

        if topic_overlaps:
            f.write(f"**Found {len(topic_overlaps)} potential overlaps:**\n\n")
            for overlap in topic_overlaps[:20]:  # Top 20
                f.write(f"- **{overlap['skill1_id']}** (Topic {overlap['topic1']}) vs **{overlap['skill2_id']}** (Topic {overlap['topic2']})\n")
            f.write("\n")

        # Recommendations
        f.write("## 8. Priority Recommendations\n\n")

        f.write("### High Priority\n\n")
        if x2_violations:
            f.write(f"1. **Fix X-2 Violations**: {len(x2_violations)} skills violate grade dependency rules\n")
        if circular_deps:
            f.write(f"2. **Break Circular Dependencies**: {len(circular_deps)} cycles detected\n")

        f.write("\n### Medium Priority\n\n")
        if transitive_deps:
            f.write(f"1. **Remove Redundant Dependencies**: {len(transitive_deps)} redundant deps found\n")
        if isolated_skills:
            f.write(f"2. **Connect Isolated Skills**: {len(isolated_skills)} skills need integration\n")

        f.write("\n### Low Priority\n\n")
        if topic_overlaps:
            f.write(f"1. **Review Topic Overlaps**: {len(topic_overlaps)} potential duplicates\n")

        f.write("\n## Conclusion\n\n")
        f.write("This analysis provides a comprehensive view of Grade 7 skill dependencies.\n")
        f.write("Focus on high-priority issues first, particularly X-2 violations and circular dependencies.\n")

    print(f"\nReport generated: {output_file}")

def main():
    input_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE7_SKILLS.json'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE7_DEPENDENCY_ANALYSIS.md'

    print(f"Loading skills from {input_file}...")
    skills = load_grade7_skills(input_file)
    print(f"Loaded {len(skills)} skills")

    print("\nPerforming comprehensive dependency analysis...")
    generate_report(skills, output_file)

    print("\nAnalysis complete!")

if __name__ == '__main__':
    main()
