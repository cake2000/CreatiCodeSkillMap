#!/usr/bin/env python3
"""
Analyze Grade K (GK) skills for Phase 2 dependency optimization.
Extract all GK skills, analyze cross-topic dependencies, validate X-2 rule, check coherence.
"""

import re
from collections import defaultdict

def parse_skills_from_md(file_path):
    """Parse all skills from allskills.md file."""
    skills = []
    current_skill = None

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # New skill starts with "ID: "
        if line.startswith('ID: '):
            if current_skill:
                skills.append(current_skill)

            skill_id = line.replace('ID: ', '').strip()
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': [],
                'line_number': i + 1
            }

        elif current_skill:
            if line.startswith('Topic: '):
                current_skill['topic'] = line.replace('Topic: ', '').strip()

            elif line.startswith('Skill: '):
                current_skill['skill'] = line.replace('Skill: ', '').strip()

            elif line.startswith('Description: '):
                desc = line.replace('Description: ', '').strip()
                # Collect multi-line descriptions
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith(('ID:', 'Topic:', 'Skill:', 'Dependencies:', 'Blocks:')):
                    if lines[j].strip():
                        desc += ' ' + lines[j].strip()
                    j += 1
                current_skill['description'] = desc

            elif line.startswith('Dependencies:'):
                # Collect all dependencies
                j = i + 1
                while j < len(lines) and lines[j].strip().startswith('* '):
                    dep_line = lines[j].strip()[2:]  # Remove "* "
                    # Extract skill ID from dependency line
                    dep_match = re.match(r'(T\d+\.[A-Z0-9]+\.\d+)', dep_line)
                    if dep_match:
                        current_skill['dependencies'].append(dep_match.group(1))
                    j += 1

        i += 1

    # Add last skill
    if current_skill:
        skills.append(current_skill)

    return skills

def extract_grade_from_id(skill_id):
    """Extract grade level from skill ID (e.g., 'GK', 'G1', 'G2')."""
    match = re.match(r'T\d+\.([A-Z0-9]+)\.\d+', skill_id)
    return match.group(1) if match else None

def extract_topic_from_id(skill_id):
    """Extract topic number from skill ID (e.g., 'T01', 'T02')."""
    match = re.match(r'(T\d+)\.[A-Z0-9]+\.\d+', skill_id)
    return match.group(1) if match else None

def analyze_gk_skills(skills):
    """Analyze all GK skills for dependency issues."""

    # Filter GK skills
    gk_skills = [s for s in skills if extract_grade_from_id(s['id']) == 'GK']

    # Create skill lookup by ID
    skill_by_id = {s['id']: s for s in skills}

    print("=" * 80)
    print("GRADE K (KINDERGARTEN) SKILLS - PHASE 2 DEPENDENCY ANALYSIS")
    print("=" * 80)
    print()

    # 1. Count by topic
    print("1. GRADE K SKILLS COUNT BY TOPIC")
    print("-" * 80)
    topic_counts = defaultdict(int)
    for skill in gk_skills:
        topic = extract_topic_from_id(skill['id'])
        topic_counts[topic] += 1

    total = 0
    for topic in sorted(topic_counts.keys()):
        count = topic_counts[topic]
        total += count
        # Get topic name from first skill in that topic
        topic_name = next((s['topic'] for s in gk_skills if extract_topic_from_id(s['id']) == topic), 'Unknown')
        print(f"{topic}: {count} skills - {topic_name}")

    print(f"\nTotal Grade K skills: {total}")
    print()

    # 2. Analyze dependencies
    print("2. DEPENDENCY ANALYSIS")
    print("-" * 80)

    issues = {
        'x2_violations': [],
        'missing_cross_topic': [],
        'circular': [],
        'transitive_redundant': [],
        'invalid_references': []
    }

    # Check each GK skill
    for skill in gk_skills:
        skill_topic = extract_topic_from_id(skill['id'])

        # Check X-2 rule: GK can only depend on GK
        for dep_id in skill['dependencies']:
            if dep_id not in skill_by_id:
                issues['invalid_references'].append({
                    'skill': skill['id'],
                    'invalid_dep': dep_id,
                    'reason': 'Dependency does not exist'
                })
                continue

            dep_grade = extract_grade_from_id(dep_id)
            if dep_grade != 'GK':
                issues['x2_violations'].append({
                    'skill': skill['id'],
                    'dependency': dep_id,
                    'dep_grade': dep_grade,
                    'reason': f'GK skill depends on {dep_grade} skill (violates X-2 rule)'
                })

        # Check for circular dependencies (A→B→A)
        for dep_id in skill['dependencies']:
            if dep_id in skill_by_id:
                dep_skill = skill_by_id[dep_id]
                if skill['id'] in dep_skill['dependencies']:
                    issues['circular'].append({
                        'skill1': skill['id'],
                        'skill2': dep_id,
                        'reason': 'Direct circular dependency'
                    })

        # Check for transitive redundancy (A→B, B→C, A→C)
        for dep_id in skill['dependencies']:
            if dep_id in skill_by_id:
                dep_skill = skill_by_id[dep_id]
                for transitive_dep in dep_skill['dependencies']:
                    if transitive_dep in skill['dependencies']:
                        issues['transitive_redundant'].append({
                            'skill': skill['id'],
                            'direct_dep': transitive_dep,
                            'via_dep': dep_id,
                            'reason': f'{skill["id"]}→{dep_id}→{transitive_dep}, but also {skill["id"]}→{transitive_dep}'
                        })

    # Analyze cross-topic dependency patterns
    print("\n2a. Cross-Topic Dependency Analysis")
    print("-" * 80)

    cross_topic_deps = defaultdict(list)
    for skill in gk_skills:
        skill_topic = extract_topic_from_id(skill['id'])
        for dep_id in skill['dependencies']:
            dep_topic = extract_topic_from_id(dep_id)
            if dep_topic != skill_topic:
                cross_topic_deps[f"{skill_topic}→{dep_topic}"].append({
                    'from': skill['id'],
                    'to': dep_id
                })

    if cross_topic_deps:
        print("Existing cross-topic dependencies:")
        for pattern, deps in sorted(cross_topic_deps.items()):
            print(f"\n{pattern}: {len(deps)} dependencies")
            for dep in deps[:3]:  # Show first 3 examples
                print(f"  - {dep['from']} → {dep['to']}")
            if len(deps) > 3:
                print(f"  ... and {len(deps) - 3} more")
    else:
        print("No cross-topic dependencies found among GK skills.")

    # Report issues
    print("\n\n2b. X-2 Rule Violations")
    print("-" * 80)
    if issues['x2_violations']:
        print(f"Found {len(issues['x2_violations'])} X-2 rule violations:")
        for issue in issues['x2_violations']:
            print(f"\n  Skill: {issue['skill']}")
            print(f"  Invalid dependency: {issue['dependency']} (grade {issue['dep_grade']})")
            print(f"  Reason: {issue['reason']}")
    else:
        print("No X-2 rule violations found. All GK skills depend only on GK skills.")

    print("\n\n2c. Circular Dependencies")
    print("-" * 80)
    if issues['circular']:
        print(f"Found {len(issues['circular'])} circular dependencies:")
        for issue in issues['circular']:
            print(f"\n  {issue['skill1']} ↔ {issue['skill2']}")
            print(f"  Reason: {issue['reason']}")
    else:
        print("No circular dependencies found.")

    print("\n\n2d. Transitive Redundant Dependencies")
    print("-" * 80)
    if issues['transitive_redundant']:
        print(f"Found {len(issues['transitive_redundant'])} potentially redundant transitive dependencies:")
        for issue in issues['transitive_redundant']:
            print(f"\n  {issue['reason']}")
            print(f"  Recommendation: Consider removing direct dependency {issue['skill']}→{issue['direct_dep']}")
    else:
        print("No transitive redundant dependencies found.")

    print("\n\n2e. Invalid Dependency References")
    print("-" * 80)
    if issues['invalid_references']:
        print(f"Found {len(issues['invalid_references'])} invalid dependency references:")
        for issue in issues['invalid_references']:
            print(f"\n  Skill: {issue['skill']}")
            print(f"  Invalid reference: {issue['invalid_dep']}")
            print(f"  Reason: {issue['reason']}")
    else:
        print("No invalid dependency references found.")

    # 3. Check for missing cross-topic dependencies
    print("\n\n3. MISSING CROSS-TOPIC DEPENDENCIES ANALYSIS")
    print("-" * 80)
    print("Analyzing skill descriptions for potential missing dependencies...")

    missing_deps = []

    # Keywords that suggest dependencies on other topics
    dependency_patterns = {
        'T02': ['loop', 'repeat', 'again', 'multiple times', 'over and over'],
        'T03': ['event', 'when', 'click', 'press', 'touch', 'start'],
        'T04': ['variable', 'count', 'score', 'number', 'store'],
        'T05': ['condition', 'if', 'when', 'check'],
        'T06': ['sprite', 'character', 'move', 'position', 'costume'],
        'T07': ['sound', 'play', 'music', 'audio'],
        'T08': ['draw', 'pen', 'line', 'color', 'paint'],
        'T09': ['user', 'input', 'ask', 'answer', 'question'],
        'T10': ['data', 'list', 'collection'],
        'T26': ['game', 'player', 'score', 'level'],
    }

    for skill in gk_skills:
        skill_topic = extract_topic_from_id(skill['id'])
        desc_lower = (skill['skill'] + ' ' + skill['description']).lower()

        for dep_topic, keywords in dependency_patterns.items():
            if dep_topic == skill_topic:
                continue  # Skip same-topic

            # Check if description mentions concepts from another topic
            for keyword in keywords:
                if keyword in desc_lower:
                    # Check if already has dependency on that topic
                    has_dep = any(extract_topic_from_id(d) == dep_topic for d in skill['dependencies'])
                    if not has_dep:
                        missing_deps.append({
                            'skill': skill['id'],
                            'skill_name': skill['skill'],
                            'missing_topic': dep_topic,
                            'keyword': keyword,
                            'context': skill['description'][:100] + '...'
                        })
                    break

    if missing_deps:
        print(f"\nFound {len(missing_deps)} potential missing cross-topic dependencies:")

        # Group by missing topic
        by_topic = defaultdict(list)
        for dep in missing_deps:
            by_topic[dep['missing_topic']].append(dep)

        for topic in sorted(by_topic.keys()):
            deps = by_topic[topic]
            print(f"\n  Missing dependencies on {topic}: {len(deps)} cases")
            for dep in deps[:5]:  # Show first 5
                print(f"    - {dep['skill']}: {dep['skill_name']}")
                print(f"      Keyword: '{dep['keyword']}'")
            if len(deps) > 5:
                print(f"    ... and {len(deps) - 5} more")
    else:
        print("\nNo obvious missing cross-topic dependencies detected based on keyword analysis.")

    # 4. Grade-level coherence check
    print("\n\n4. GRADE-LEVEL COHERENCE CHECK")
    print("-" * 80)

    # Check for skills with no dependencies (foundational skills)
    foundational = [s for s in gk_skills if not s['dependencies']]
    print(f"\nFoundational skills (no dependencies): {len(foundational)}")
    if foundational:
        topic_foundation = defaultdict(list)
        for s in foundational:
            topic = extract_topic_from_id(s['id'])
            topic_foundation[topic].append(s['id'])

        for topic in sorted(topic_foundation.keys()):
            print(f"  {topic}: {len(topic_foundation[topic])} foundational skills")
            for skill_id in topic_foundation[topic][:3]:
                skill = skill_by_id[skill_id]
                print(f"    - {skill_id}: {skill['skill']}")
            if len(topic_foundation[topic]) > 3:
                print(f"    ... and {len(topic_foundation[topic]) - 3} more")

    # Check for skills with many dependencies (advanced skills)
    advanced = [s for s in gk_skills if len(s['dependencies']) >= 3]
    print(f"\nAdvanced skills (3+ dependencies): {len(advanced)}")
    if advanced:
        for s in sorted(advanced, key=lambda x: len(x['dependencies']), reverse=True)[:10]:
            print(f"  {s['id']}: {s['skill']} ({len(s['dependencies'])} deps)")

    # Check dependency depth (how many levels of dependencies)
    print(f"\nDependency depth analysis:")

    def get_max_depth(skill_id, visited=None):
        if visited is None:
            visited = set()
        if skill_id in visited:
            return 0
        visited.add(skill_id)

        if skill_id not in skill_by_id:
            return 0

        skill = skill_by_id[skill_id]
        if not skill['dependencies']:
            return 0

        return 1 + max((get_max_depth(dep, visited.copy()) for dep in skill['dependencies']), default=0)

    depths = [(s['id'], get_max_depth(s['id'])) for s in gk_skills]
    max_depth = max(d[1] for d in depths) if depths else 0

    print(f"  Maximum dependency depth: {max_depth}")
    print(f"  Depth distribution:")
    for depth in range(max_depth + 1):
        count = sum(1 for _, d in depths if d == depth)
        print(f"    Depth {depth}: {count} skills")

    # 5. Summary and recommendations
    print("\n\n5. SUMMARY AND RECOMMENDATIONS")
    print("=" * 80)

    print("\nStatistics:")
    print(f"  Total GK skills: {len(gk_skills)}")
    print(f"  Topics covered: {len(topic_counts)}")
    print(f"  X-2 violations: {len(issues['x2_violations'])}")
    print(f"  Circular dependencies: {len(issues['circular'])}")
    print(f"  Transitive redundancies: {len(issues['transitive_redundant'])}")
    print(f"  Invalid references: {len(issues['invalid_references'])}")
    print(f"  Potential missing cross-topic deps: {len(missing_deps)}")

    print("\n\nPRIORITY FIXES NEEDED:")
    print("-" * 80)

    priority = 1

    if issues['x2_violations']:
        print(f"\n{priority}. FIX X-2 RULE VIOLATIONS (CRITICAL)")
        priority += 1
        for issue in issues['x2_violations']:
            skill = skill_by_id[issue['skill']]
            print(f"\n   Skill: {issue['skill']} - {skill['skill']}")
            print(f"   Remove dependency: {issue['dependency']} (grade {issue['dep_grade']})")
            print(f"   Reason: GK skills can ONLY depend on GK skills")

    if issues['circular']:
        print(f"\n{priority}. FIX CIRCULAR DEPENDENCIES (CRITICAL)")
        priority += 1
        for issue in issues['circular']:
            print(f"\n   Break circular dependency: {issue['skill1']} ↔ {issue['skill2']}")
            print(f"   Recommendation: Analyze which direction makes pedagogical sense, remove the other")

    if issues['invalid_references']:
        print(f"\n{priority}. FIX INVALID DEPENDENCY REFERENCES (HIGH)")
        priority += 1
        for issue in issues['invalid_references']:
            print(f"\n   Skill: {issue['skill']}")
            print(f"   Remove invalid reference: {issue['invalid_dep']}")

    if issues['transitive_redundant']:
        print(f"\n{priority}. REVIEW TRANSITIVE REDUNDANCIES (MEDIUM)")
        priority += 1
        print(f"\n   Found {len(issues['transitive_redundant'])} transitive dependencies.")
        print(f"   Review each case - only remove if TRULY redundant.")
        print(f"   Be conservative: when in doubt, keep the dependency.")
        for issue in issues['transitive_redundant'][:5]:
            print(f"\n   {issue['reason']}")
            print(f"   Consider removing: {issue['skill']}→{issue['direct_dep']}")

    if missing_deps:
        print(f"\n{priority}. REVIEW POTENTIAL MISSING CROSS-TOPIC DEPENDENCIES (LOW)")
        priority += 1
        print(f"\n   Keyword analysis suggests {len(missing_deps)} potential missing dependencies.")
        print(f"   Review each case to determine if dependency should be added.")

        # Show a few examples
        for dep in missing_deps[:10]:
            skill = skill_by_id[dep['skill']]
            print(f"\n   {dep['skill']}: {skill['skill']}")
            print(f"   Possible missing dependency on {dep['missing_topic']} (keyword: '{dep['keyword']}')")

    print("\n\n" + "=" * 80)
    print("ANALYSIS COMPLETE")
    print("=" * 80)

if __name__ == '__main__':
    file_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    skills = parse_skills_from_md(file_path)
    analyze_gk_skills(skills)
