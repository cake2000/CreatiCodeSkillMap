#!/usr/bin/env python3
"""
Deep analysis of G3 dependency chains to verify pedagogical soundness.
"""

import re
from collections import defaultdict, Counter

def parse_markdown_skills(file_path):
    """Parse the markdown file and extract all skills."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    skill_blocks = re.split(r'\n\n(?=ID: )', content)

    skills = []
    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID:'):
            continue

        id_match = re.search(r'ID:\s+([^\n]+)', block)
        if not id_match:
            continue
        skill_id = id_match.group(1).strip()

        grade_match = re.search(r'\.G(\d+|K)\.', skill_id)
        if not grade_match:
            continue

        grade_str = grade_match.group(1)
        if grade_str == 'K':
            grade = 0
        else:
            grade = int(grade_str)

        topic_match = re.search(r'Topic:\s+([^\n]+)', block)
        topic = topic_match.group(1).strip() if topic_match else ""

        skill_match = re.search(r'Skill:\s+([^\n]+)', block)
        title = skill_match.group(1).strip() if skill_match else ""

        desc_match = re.search(r'Description:\s+(.+?)(?=\n\nDependencies:|$)', block, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        dependencies = []
        deps_section = re.search(r'Dependencies:\s*\n((?:\*[^\n]+\n?)+)', block, re.DOTALL)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'\*\s+([^:]+):', line)
                if dep_match:
                    dependencies.append(dep_match.group(1).strip())

        skills.append({
            'id': skill_id,
            'title': title,
            'topic': topic,
            'grade': grade,
            'dependencies': dependencies,
            'description': description
        })

    return skills

def analyze_dependency_chains(skills):
    """Analyze dependency chains for G3 skills."""

    skill_map = {s['id']: s for s in skills}
    g3_skills = [s for s in skills if s['grade'] == 3]

    print("=" * 80)
    print("GRADE 3 DEPENDENCY CHAIN ANALYSIS")
    print("=" * 80)
    print()

    # Analyze by topic
    print("-" * 80)
    print("DEPENDENCY ANALYSIS BY TOPIC")
    print("-" * 80)

    topic_stats = defaultdict(lambda: {'count': 0, 'total_deps': 0, 'skills': []})

    for skill in g3_skills:
        topic = skill['topic']
        topic_stats[topic]['count'] += 1
        topic_stats[topic]['total_deps'] += len(skill['dependencies'])
        topic_stats[topic]['skills'].append(skill)

    for topic in sorted(topic_stats.keys()):
        stats = topic_stats[topic]
        avg_deps = stats['total_deps'] / stats['count'] if stats['count'] > 0 else 0
        print(f"\n{topic}")
        print(f"  Skills: {stats['count']}")
        print(f"  Avg dependencies: {avg_deps:.2f}")

        # Show dependency distribution for this topic
        dep_counts = Counter([len(s['dependencies']) for s in stats['skills']])
        print(f"  Distribution: ", end="")
        for count in sorted(dep_counts.keys()):
            print(f"{count}deps:{dep_counts[count]} ", end="")
        print()

    print()

    # Analyze dependency patterns
    print("-" * 80)
    print("DEPENDENCY PATTERN ANALYSIS")
    print("-" * 80)

    # What grades are G3 skills depending on?
    grade_dependencies = Counter()
    for skill in g3_skills:
        for dep in skill['dependencies']:
            if dep in skill_map:
                grade_dependencies[skill_map[dep]['grade']] += 1

    print("\nG3 skills depend on:")
    total_deps = sum(grade_dependencies.values())
    for grade in sorted(grade_dependencies.keys()):
        count = grade_dependencies[grade]
        pct = (count / total_deps * 100) if total_deps > 0 else 0
        print(f"  Grade {grade if grade > 0 else 'K'}: {count} dependencies ({pct:.1f}%)")

    print()

    # Find longest dependency chains
    print("-" * 80)
    print("DEPENDENCY CHAIN DEPTH ANALYSIS")
    print("-" * 80)

    def get_max_depth(skill_id, skill_map, visited=None):
        """Get the maximum depth of dependency chain."""
        if visited is None:
            visited = set()

        if skill_id in visited or skill_id not in skill_map:
            return 0

        visited.add(skill_id)
        skill = skill_map[skill_id]

        if not skill['dependencies']:
            return 0

        max_depth = 0
        for dep in skill['dependencies']:
            depth = get_max_depth(dep, skill_map, visited.copy())
            max_depth = max(max_depth, depth)

        return max_depth + 1

    chain_depths = []
    for skill in g3_skills:
        depth = get_max_depth(skill['id'], skill_map)
        chain_depths.append((skill['id'], skill['title'], depth))

    chain_depths.sort(key=lambda x: x[2], reverse=True)

    print("\nTop 10 longest dependency chains:")
    for skill_id, title, depth in chain_depths[:10]:
        print(f"  {skill_id}: depth {depth} - {title[:50]}...")

    depth_dist = Counter([d for _, _, d in chain_depths])
    print("\nChain depth distribution:")
    for depth in sorted(depth_dist.keys()):
        bar = '#' * (depth_dist[depth] // 2)
        print(f"  Depth {depth}: {depth_dist[depth]} skills {bar}")

    print()

    # Cross-topic dependencies
    print("-" * 80)
    print("CROSS-TOPIC DEPENDENCY ANALYSIS")
    print("-" * 80)

    cross_topic_count = 0
    same_topic_count = 0

    for skill in g3_skills:
        skill_topic = skill['topic']
        for dep in skill['dependencies']:
            if dep in skill_map:
                dep_topic = skill_map[dep]['topic']
                if dep_topic != skill_topic:
                    cross_topic_count += 1
                else:
                    same_topic_count += 1

    total = cross_topic_count + same_topic_count
    print(f"\nSame-topic dependencies: {same_topic_count} ({same_topic_count/total*100:.1f}%)")
    print(f"Cross-topic dependencies: {cross_topic_count} ({cross_topic_count/total*100:.1f}%)")
    print()
    print("Cross-topic dependencies indicate integration between topics.")

    print()

    # Most referenced prerequisites
    print("-" * 80)
    print("MOST REFERENCED PREREQUISITES")
    print("-" * 80)

    dep_frequency = Counter()
    for skill in g3_skills:
        for dep in skill['dependencies']:
            dep_frequency[dep] += 1

    print("\nTop 15 most-referenced prerequisite skills:")
    for i, (dep_id, count) in enumerate(dep_frequency.most_common(15), 1):
        if dep_id in skill_map:
            dep_skill = skill_map[dep_id]
            print(f"  {i:2d}. {dep_id} (G{dep_skill['grade']}): {count} times")
            print(f"      {dep_skill['title'][:70]}...")

    print()

    # Skills that are never prerequisites
    print("-" * 80)
    print("TERMINAL SKILLS (Not prerequisites for other G3 skills)")
    print("-" * 80)

    all_g3_deps = set()
    for skill in g3_skills:
        all_g3_deps.update(skill['dependencies'])

    g3_ids = set(s['id'] for s in g3_skills)
    terminal_skills = g3_ids - (all_g3_deps & g3_ids)

    print(f"\nTotal terminal skills (not used as prereqs): {len(terminal_skills)}")
    print(f"Percentage: {len(terminal_skills)/len(g3_skills)*100:.1f}%")
    print("\nThese are advanced/specialized skills in G3:")
    for i, skill_id in enumerate(sorted(terminal_skills)[:10], 1):
        skill = skill_map[skill_id]
        print(f"  {i:2d}. {skill_id}: {skill['title'][:60]}...")

    print()

    # Foundation skills (no deps or very few)
    print("-" * 80)
    print("FOUNDATION SKILLS (1 dependency)")
    print("-" * 80)

    foundation = [s for s in g3_skills if len(s['dependencies']) == 1]
    print(f"\nTotal foundation skills: {len(foundation)}")
    print("\nThese build on a single key prerequisite:")

    # Group by the prerequisite they depend on
    by_prereq = defaultdict(list)
    for skill in foundation:
        prereq = skill['dependencies'][0]
        by_prereq[prereq].append(skill)

    print(f"\nGrouped by prerequisite (showing top 10):")
    sorted_prereqs = sorted(by_prereq.items(), key=lambda x: len(x[1]), reverse=True)
    for prereq, skills in sorted_prereqs[:10]:
        if prereq in skill_map:
            prereq_skill = skill_map[prereq]
            print(f"\n  {prereq} (G{prereq_skill['grade']}): {len(skills)} skills depend on this")
            print(f"  Prereq: {prereq_skill['title'][:60]}...")
            for s in skills[:3]:
                print(f"    - {s['id']}: {s['title'][:50]}...")

    print()
    print("=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    file_path = "/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md"

    print("Parsing skills file...")
    skills = parse_markdown_skills(file_path)
    print(f"Parsed {len(skills)} skills total\n")

    analyze_dependency_chains(skills)
