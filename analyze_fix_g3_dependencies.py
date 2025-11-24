#!/usr/bin/env python3
"""
Phase 2: Grade 3 Dependency Analysis and Fix Script
Analyzes and fixes all Grade 3 skill dependencies in allskills.md
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

# Topic categorization
FOUNDATIONAL_TOPICS = ['T01', 'T02', 'T03', 'T04', 'T05']  # Everyday, Decompose, Pattern, Debug, Collaborate
PROGRAMMING_CORE_TOPICS = ['T06', 'T07', 'T08', 'T09', 'T10', 'T11', 'T12', 'T13']  # Sequence, Events, Loops, Conditionals, Variables, Operators, Functions, Procedures
APPLICATION_TOPICS = ['T14', 'T15', 'T16', 'T17', 'T18', 'T19', 'T20', 'T21', 'T22', 'T23', 'T24']  # Games, Stories, Art, etc.
AI_ML_TOPICS = ['T25', 'T26', 'T27', 'T28', 'T29', 'T30']  # AI/ML concepts
ADVANCED_TOPICS = ['T31', 'T32', 'T33', 'T34', 'T35', 'T36']  # Advanced programming

def parse_skills(file_path: str) -> Dict[str, Dict]:
    """Parse all skills from the markdown file"""
    skills = {}

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill ID markers
    skill_blocks = re.split(r'\n(?=ID: )', content)

    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID: '):
            continue

        # Extract skill ID
        id_match = re.match(r'ID: ([\w.]+)', block)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic
        topic_match = re.search(r'Topic: (T\d+)', block)
        topic = topic_match.group(1) if topic_match else None

        # Extract skill name
        skill_match = re.search(r'Skill: (.+?)(?:\n|$)', block)
        skill_name = skill_match.group(1).strip() if skill_match else ""

        # Extract description
        desc_match = re.search(r'Description: (.+?)(?=\n(?:Dependencies:|ID:|$))', block, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        dependencies = []
        dep_section = re.search(r'Dependencies:\n((?:\* .+\n?)+)', block)
        if dep_section:
            dep_lines = dep_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.match(r'\* ([\w.]+):', line)
                if dep_match:
                    dependencies.append(dep_match.group(1))

        skills[skill_id] = {
            'id': skill_id,
            'topic': topic,
            'name': skill_name,
            'description': description,
            'dependencies': dependencies,
            'original_block': block
        }

    return skills

def get_grade(skill_id: str) -> str:
    """Extract grade from skill ID"""
    match = re.search(r'\.(GK|G[0-9]+)\.', skill_id)
    return match.group(1) if match else None

def get_topic(skill_id: str) -> str:
    """Extract topic from skill ID"""
    match = re.match(r'(T\d+)', skill_id)
    return match.group(1) if match else None

def validate_dependency(skill_id: str, dep_id: str, all_skills: Dict) -> Tuple[bool, str]:
    """
    Validate a dependency
    Returns (is_valid, reason)
    """
    # Check if dependency exists
    if dep_id not in all_skills:
        return False, f"Non-existent skill: {dep_id}"

    # Check grade progression (X-2 rule: G3 can depend on GK, G1, G2, G3)
    skill_grade = get_grade(skill_id)
    dep_grade = get_grade(dep_id)

    if skill_grade == 'G3':
        if dep_grade not in ['GK', 'G1', 'G2', 'G3']:
            return False, f"Invalid grade progression: G3 cannot depend on {dep_grade}"

    return True, "Valid"

def find_circular_dependencies(skill_id: str, all_skills: Dict, visited: Set = None, path: List = None) -> List:
    """Find circular dependencies starting from a skill"""
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if skill_id in path:
        # Found a cycle
        cycle_start = path.index(skill_id)
        return path[cycle_start:] + [skill_id]

    if skill_id in visited:
        return []

    visited.add(skill_id)
    path.append(skill_id)

    skill = all_skills.get(skill_id, {})
    for dep_id in skill.get('dependencies', []):
        if dep_id in all_skills:
            cycle = find_circular_dependencies(dep_id, all_skills, visited, path[:])
            if cycle:
                return cycle

    return []

def is_transitive_redundant(skill_id: str, dep_id: str, all_skills: Dict) -> bool:
    """
    Check if a dependency is truly redundant (transitive)
    A->C is redundant if there exists A->B->C
    """
    skill = all_skills.get(skill_id, {})
    direct_deps = skill.get('dependencies', [])

    # Check if dep_id is reachable through another dependency
    for other_dep in direct_deps:
        if other_dep == dep_id:
            continue
        if other_dep not in all_skills:
            continue

        # Check if other_dep leads to dep_id
        indirect_deps = all_skills[other_dep].get('dependencies', [])
        if dep_id in indirect_deps:
            return True

    return False

def suggest_cross_topic_dependencies(skill_id: str, skill: Dict, all_skills: Dict) -> List[str]:
    """
    Suggest missing cross-topic dependencies for a G3 skill
    """
    suggestions = []
    topic = get_topic(skill_id)
    description = skill.get('description', '').lower()
    name = skill.get('name', '').lower()
    combined_text = description + ' ' + name

    # Only suggest for application/advanced topics
    if topic not in APPLICATION_TOPICS + AI_ML_TOPICS + ADVANCED_TOPICS:
        return suggestions

    current_deps = set(skill.get('dependencies', []))
    current_dep_topics = set(get_topic(dep) for dep in current_deps if get_topic(dep))

    # Key programming concepts to check
    concepts_to_check = [
        # Loops (T08)
        (['loop', 'repeat', 'forever', 'until', 'while', 'iterate'], 'T08', ['T08.G3.01', 'T08.G3.02', 'T08.G3.03']),
        # Conditionals (T09)
        (['if', 'when', 'condition', 'check', 'detect', 'collision', 'touch', 'press'], 'T09', ['T09.G3.01.01', 'T09.G3.02', 'T09.G3.03']),
        # Variables (T10)
        (['variable', 'score', 'count', 'store', 'value', 'change', 'track'], 'T10', ['T10.G3.01.01', 'T10.G3.02', 'T10.G3.03']),
        # Events (T07)
        (['event', 'click', 'key', 'start', 'message', 'broadcast'], 'T07', ['T07.G3.01', 'T07.G3.02', 'T07.G3.03']),
        # Sequences (T06)
        (['sequence', 'order', 'step', 'move', 'action'], 'T06', ['T06.G3.01', 'T06.G3.02']),
    ]

    for keywords, dep_topic, example_skills in concepts_to_check:
        # Skip if already has dependency from this topic
        if dep_topic in current_dep_topics:
            continue

        # Check if any keyword appears in the skill
        if any(keyword in combined_text for keyword in keywords):
            # Find appropriate skill from that topic
            for example_skill_id in example_skills:
                if example_skill_id in all_skills and example_skill_id not in current_deps:
                    suggestions.append(example_skill_id)
                    break

    return suggestions

def analyze_g3_dependencies(file_path: str):
    """Main analysis function"""
    print("=== Phase 2: Grade 3 Dependency Analysis ===\n")

    # Parse all skills
    print("Parsing skills from allskills.md...")
    all_skills = parse_skills(file_path)
    print(f"Total skills parsed: {len(all_skills)}")

    # Filter G3 skills
    g3_skills = {sid: s for sid, s in all_skills.items() if get_grade(sid) == 'G3'}
    print(f"Total G3 skills found: {len(g3_skills)}\n")

    # Statistics
    stats = {
        'total_g3_skills': len(g3_skills),
        'invalid_deps': defaultdict(list),
        'circular_deps': [],
        'redundant_deps': defaultdict(list),
        'suggested_deps': defaultdict(list),
        'deps_to_add': defaultdict(list),
        'deps_to_remove': defaultdict(list),
    }

    # Analyze each G3 skill
    print("Analyzing G3 dependencies...\n")

    for skill_id, skill in g3_skills.items():
        topic = get_topic(skill_id)
        deps = skill.get('dependencies', [])

        # Check for invalid dependencies
        for dep_id in deps:
            is_valid, reason = validate_dependency(skill_id, dep_id, all_skills)
            if not is_valid:
                stats['invalid_deps'][topic].append({
                    'skill': skill_id,
                    'dep': dep_id,
                    'reason': reason
                })

        # Check for circular dependencies
        cycle = find_circular_dependencies(skill_id, all_skills)
        if cycle:
            stats['circular_deps'].append({
                'skill': skill_id,
                'cycle': cycle
            })

        # Check for transitive redundancies (conservative)
        for dep_id in deps:
            if is_transitive_redundant(skill_id, dep_id, all_skills):
                stats['redundant_deps'][topic].append({
                    'skill': skill_id,
                    'dep': dep_id
                })

        # Suggest missing cross-topic dependencies
        suggestions = suggest_cross_topic_dependencies(skill_id, skill, all_skills)
        if suggestions:
            stats['suggested_deps'][topic].extend([{
                'skill': skill_id,
                'suggestions': suggestions
            }])

    # Print statistics
    print("=== ANALYSIS RESULTS ===\n")

    print(f"1. TOTAL G3 SKILLS: {stats['total_g3_skills']}")
    print(f"   Breakdown by topic:")
    topic_counts = defaultdict(int)
    for sid in g3_skills:
        topic_counts[get_topic(sid)] += 1
    for topic in sorted(topic_counts.keys()):
        print(f"   - {topic}: {topic_counts[topic]} skills")

    print(f"\n2. INVALID DEPENDENCIES FOUND: {sum(len(v) for v in stats['invalid_deps'].values())}")
    for topic in sorted(stats['invalid_deps'].keys()):
        issues = stats['invalid_deps'][topic]
        print(f"   {topic}: {len(issues)} issues")
        for issue in issues[:3]:  # Show first 3
            print(f"     - {issue['skill']} -> {issue['dep']}: {issue['reason']}")
        if len(issues) > 3:
            print(f"     ... and {len(issues) - 3} more")

    print(f"\n3. CIRCULAR DEPENDENCIES: {len(stats['circular_deps'])}")
    for circ in stats['circular_deps'][:5]:  # Show first 5
        print(f"   - {circ['skill']}: {' -> '.join(circ['cycle'])}")

    print(f"\n4. POTENTIALLY REDUNDANT DEPENDENCIES: {sum(len(v) for v in stats['redundant_deps'].values())}")
    for topic in sorted(stats['redundant_deps'].keys())[:5]:  # Show first 5 topics
        issues = stats['redundant_deps'][topic]
        print(f"   {topic}: {len(issues)} potentially redundant")

    print(f"\n5. SUGGESTED CROSS-TOPIC DEPENDENCIES: {sum(len(v) for v in stats['suggested_deps'].values())}")
    for topic in sorted(stats['suggested_deps'].keys()):
        suggestions = stats['suggested_deps'][topic]
        print(f"   {topic}: {len(suggestions)} skills need cross-topic deps")

    return all_skills, g3_skills, stats

def apply_fixes(file_path: str, all_skills: Dict, g3_skills: Dict, stats: Dict):
    """Apply fixes to the allskills.md file"""
    print("\n=== APPLYING FIXES ===\n")

    changes_log = {
        'deps_added': defaultdict(int),
        'deps_removed': defaultdict(int),
        'invalid_fixed': defaultdict(int)
    }

    # Read original file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Process each G3 skill that needs fixes
    for skill_id, skill in g3_skills.items():
        topic = get_topic(skill_id)
        deps = skill.get('dependencies', [])
        new_deps = deps.copy()

        # Remove invalid dependencies
        for dep_info in stats['invalid_deps'].get(topic, []):
            if dep_info['skill'] == skill_id:
                dep_to_remove = dep_info['dep']
                if dep_to_remove in new_deps:
                    new_deps.remove(dep_to_remove)
                    changes_log['invalid_fixed'][topic] += 1
                    print(f"Removing invalid dep from {skill_id}: {dep_to_remove}")

        # Add suggested dependencies
        for sugg_info in stats['suggested_deps'].get(topic, []):
            if sugg_info['skill'] == skill_id:
                for sugg_dep in sugg_info['suggestions']:
                    if sugg_dep not in new_deps:
                        new_deps.append(sugg_dep)
                        changes_log['deps_added'][topic] += 1
                        print(f"Adding suggested dep to {skill_id}: {sugg_dep}")

        # Update content if dependencies changed
        if set(new_deps) != set(deps):
            # Find and replace the skill block
            old_block = skill['original_block']
            new_block = rebuild_skill_block(skill_id, skill, new_deps, all_skills)
            content = content.replace(old_block, new_block)

    # Write updated content
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n=== FIXES APPLIED ===\n")
    return changes_log

def rebuild_skill_block(skill_id: str, skill: Dict, new_deps: List[str], all_skills: Dict) -> str:
    """Rebuild a skill block with updated dependencies"""
    lines = []
    lines.append(f"ID: {skill_id}")
    lines.append(f"Topic: {skill['topic']} – {get_topic_name(skill['topic'])}")
    lines.append(f"Skill: {skill['name']}")
    lines.append(f"Description: {skill['description']}")

    if new_deps:
        lines.append("")
        lines.append("Dependencies:")
        for dep_id in sorted(new_deps):
            dep_skill = all_skills.get(dep_id, {})
            dep_name = dep_skill.get('name', 'Unknown')
            lines.append(f"* {dep_id}: {dep_name}")

    lines.append("")
    lines.append("")

    return '\n'.join(lines)

def get_topic_name(topic_code: str) -> str:
    """Get topic name from code"""
    topic_names = {
        'T01': 'Everyday Algorithms', 'T02': 'Decompose', 'T03': 'Pattern Recognition',
        'T04': 'Debug', 'T05': 'Collaborate', 'T06': 'Sequences', 'T07': 'Events',
        'T08': 'Loops', 'T09': 'Conditionals', 'T10': 'Variables', 'T11': 'Operators',
        'T12': 'Functions', 'T13': 'Procedures', 'T14': 'Games', 'T15': 'Interactive Stories',
        'T16': 'Art & Graphics', 'T17': 'Music & Sound', 'T18': 'Simulation',
        'T20': 'Data Visualization', 'T21': 'Math', 'T22': 'Science', 'T23': 'Language Arts',
        'T24': 'Social Studies', 'T25': 'AI Concepts', 'T26': 'Pattern Recognition AI',
        'T27': 'Decision Making AI', 'T28': 'NLP', 'T29': 'Computer Vision',
        'T30': 'ML Concepts', 'T31': 'Lists', 'T32': 'Cloning', 'T33': 'Custom Blocks',
        'T34': 'Extensions', 'T35': 'Advanced Graphics', 'T36': 'Advanced Data'
    }
    return topic_names.get(topic_code, 'Unknown')

if __name__ == '__main__':
    file_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    # Analyze
    all_skills, g3_skills, stats = analyze_g3_dependencies(file_path)

    # Apply fixes
    changes_log = apply_fixes(file_path, all_skills, g3_skills, stats)

    # Final summary
    print("\n=== FINAL SUMMARY ===")
    print(f"Total G3 skills processed: {len(g3_skills)}")
    print(f"\nDependencies added by topic:")
    for topic in sorted(changes_log['deps_added'].keys()):
        print(f"  {topic}: {changes_log['deps_added'][topic]}")
    print(f"Total added: {sum(changes_log['deps_added'].values())}")

    print(f"\nDependencies removed by topic:")
    for topic in sorted(changes_log['deps_removed'].keys()):
        print(f"  {topic}: {changes_log['deps_removed'][topic]}")
    print(f"Total removed: {sum(changes_log['deps_removed'].values())}")

    print(f"\nInvalid dependencies fixed by topic:")
    for topic in sorted(changes_log['invalid_fixed'].keys()):
        print(f"  {topic}: {changes_log['invalid_fixed'][topic]}")
    print(f"Total invalid fixed: {sum(changes_log['invalid_fixed'].values())}")

    print("\n=== PHASE 2 COMPLETE ===")
