#!/usr/bin/env python3
"""
Phase 2: Grade 3 Dependency Analysis and Fix Script (Conservative)
Analyzes and fixes Grade 3 skill dependencies with conservative rules
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

# Topic categorization
FOUNDATIONAL_TOPICS = ['T01', 'T02', 'T03', 'T04', 'T05']
PROGRAMMING_CORE_TOPICS = ['T06', 'T07', 'T08', 'T09', 'T10', 'T11', 'T12', 'T13']
APPLICATION_TOPICS = ['T14', 'T15', 'T16', 'T17', 'T18', 'T20', 'T21', 'T22', 'T23', 'T24']
AI_ML_TOPICS = ['T25', 'T26', 'T27', 'T28', 'T29', 'T30']
ADVANCED_TOPICS = ['T31', 'T32', 'T33', 'T34', 'T35', 'T36']

def parse_skills(file_path: str) -> Dict[str, Dict]:
    """Parse all skills from markdown file"""
    skills = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find skill blocks
    pattern = r'ID: ([\w.]+)\n(.*?)(?=\nID: |\Z)'
    matches = re.finditer(pattern, content, re.DOTALL)

    for match in matches:
        skill_id = match.group(1)
        block_text = match.group(2)

        # Extract topic
        topic_match = re.search(r'Topic: (T\d+)', block_text)
        topic = topic_match.group(1) if topic_match else None

        # Extract skill name
        skill_match = re.search(r'Skill: (.+?)(?:\n|$)', block_text)
        skill_name = skill_match.group(1).strip() if skill_match else ""

        # Extract description
        desc_match = re.search(r'Description: (.+?)(?=\n(?:Dependencies:|ID:|\n\n|$))', block_text, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        dependencies = []
        dep_section = re.search(r'Dependencies:\n((?:\* .+\n?)+)', block_text)
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
            'full_block': 'ID: ' + skill_id + '\n' + block_text
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
    """Validate a dependency"""
    # Check if dependency exists
    if dep_id not in all_skills:
        return False, f"Non-existent skill: {dep_id}"

    # Check grade progression (X-2 rule)
    skill_grade = get_grade(skill_id)
    dep_grade = get_grade(dep_id)

    if skill_grade == 'G3':
        if dep_grade not in ['GK', 'G1', 'G2', 'G3']:
            return False, f"Invalid grade: G3 cannot depend on {dep_grade}"

    return True, "Valid"

def suggest_missing_dependencies(skill_id: str, skill: Dict, all_skills: Dict) -> List[str]:
    """
    Suggest missing cross-topic dependencies for APPLICATION/AI/ADVANCED topics only
    Uses conservative keyword matching to identify truly needed dependencies
    """
    suggestions = []
    topic = get_topic(skill_id)

    # Only suggest for application, AI/ML, and advanced topics
    if topic not in APPLICATION_TOPICS + AI_ML_TOPICS + ADVANCED_TOPICS:
        return suggestions

    description = skill.get('description', '').lower()
    name = skill.get('name', '').lower()
    combined = description + ' ' + name

    current_deps = set(skill.get('dependencies', []))
    current_dep_topics = set(get_topic(dep) for dep in current_deps if get_topic(dep))

    # Conservative keyword mapping for essential programming concepts
    dependency_rules = [
        # Loops (T08) - only if explicit loop language
        {
            'keywords': ['repeat', 'forever', 'loop', 'until'],
            'topic': 'T08',
            'suggested_skills': ['T08.G3.01', 'T08.G3.02'],
            'priority': 'high'
        },
        # Conditionals (T09) - only if explicit conditional language
        {
            'keywords': ['if ', 'when ', 'condition', 'detect collision', 'touching', 'key pressed'],
            'topic': 'T09',
            'suggested_skills': ['T09.G3.01.01', 'T09.G3.02'],
            'priority': 'high'
        },
        # Variables (T10) - only if explicit variable/score/tracking language
        {
            'keywords': ['variable', 'score', 'counter', 'store value', 'track'],
            'topic': 'T10',
            'suggested_skills': ['T10.G3.01.01', 'T10.G3.02'],
            'priority': 'high'
        },
        # Events (T07) - only if explicit event language
        {
            'keywords': ['event', 'message', 'broadcast', 'receive'],
            'topic': 'T07',
            'suggested_skills': ['T07.G3.01', 'T07.G3.02'],
            'priority': 'medium'
        },
        # Sequences (T06) - only if multiple ordered actions mentioned
        {
            'keywords': ['sequence of', 'ordered steps', 'multiple actions'],
            'topic': 'T06',
            'suggested_skills': ['T06.G3.01'],
            'priority': 'low'
        },
    ]

    for rule in dependency_rules:
        # Skip if already has dependency from this topic
        if rule['topic'] in current_dep_topics:
            continue

        # Check for keyword matches
        matches = sum(1 for keyword in rule['keywords'] if keyword in combined)

        # Only add if we have strong evidence (high priority needs 1+ match, medium 2+, low 2+)
        threshold = 1 if rule['priority'] == 'high' else 2
        if matches >= threshold:
            # Find first available suggested skill
            for skill_id in rule['suggested_skills']:
                if skill_id in all_skills and skill_id not in current_deps:
                    suggestions.append(skill_id)
                    break

    return suggestions

def analyze_g3_skills(file_path: str):
    """Main analysis function"""
    print("Phase 2: Grade 3 Dependency Analysis\n")

    all_skills = parse_skills(file_path)
    print(f"Total skills parsed: {len(all_skills)}")

    g3_skills = {sid: s for sid, s in all_skills.items() if get_grade(sid) == 'G3'}
    print(f"Total G3 skills: {len(g3_skills)}\n")

    # Statistics
    stats = {
        'invalid_deps': [],
        'suggested_deps': [],
        'topic_counts': defaultdict(int)
    }

    # Analyze each G3 skill
    for skill_id, skill in g3_skills.items():
        topic = get_topic(skill_id)
        stats['topic_counts'][topic] += 1

        # Check for invalid dependencies
        for dep_id in skill.get('dependencies', []):
            is_valid, reason = validate_dependency(skill_id, dep_id, all_skills)
            if not is_valid:
                stats['invalid_deps'].append({
                    'skill': skill_id,
                    'dep': dep_id,
                    'reason': reason
                })

        # Suggest missing dependencies
        suggestions = suggest_missing_dependencies(skill_id, skill, all_skills)
        if suggestions:
            stats['suggested_deps'].append({
                'skill': skill_id,
                'name': skill.get('name', ''),
                'suggestions': suggestions
            })

    return all_skills, g3_skills, stats

def apply_fixes(file_path: str, all_skills: Dict, g3_skills: Dict, stats: Dict):
    """Apply fixes to allskills.md"""
    print("\nApplying fixes...\n")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    changes = {
        'deps_added': defaultdict(list),
        'deps_removed': defaultdict(list)
    }

    # Apply fixes for each skill
    for skill_id, skill in g3_skills.items():
        topic = get_topic(skill_id)
        current_deps = skill.get('dependencies', [])[:]
        new_deps = current_deps[:]

        # Remove invalid dependencies
        for invalid in stats['invalid_deps']:
            if invalid['skill'] == skill_id:
                dep_to_remove = invalid['dep']
                if dep_to_remove in new_deps:
                    new_deps.remove(dep_to_remove)
                    changes['deps_removed'][topic].append(f"{skill_id} -> {dep_to_remove}: {invalid['reason']}")
                    print(f"REMOVE: {skill_id} -> {dep_to_remove}")

        # Add suggested dependencies
        for sugg in stats['suggested_deps']:
            if sugg['skill'] == skill_id:
                for dep_to_add in sugg['suggestions']:
                    if dep_to_add not in new_deps:
                        new_deps.append(dep_to_add)
                        changes['deps_added'][topic].append(f"{skill_id} <- {dep_to_add}")
                        print(f"ADD: {skill_id} <- {dep_to_add}")

        # Rebuild skill block if changed
        if set(new_deps) != set(current_deps):
            old_block = skill['full_block']
            new_block = rebuild_skill_block(skill_id, skill, new_deps, all_skills)
            content = content.replace(old_block, new_block, 1)

    # Write updated file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return changes

def rebuild_skill_block(skill_id: str, skill: Dict, new_deps: List[str], all_skills: Dict) -> str:
    """Rebuild skill block with updated dependencies"""
    lines = []
    lines.append(f"ID: {skill_id}")
    lines.append(f"Topic: {skill['topic']} – {get_topic_name(skill['topic'])}")
    lines.append(f"Skill: {skill['name']}")
    lines.append(f"Description: {skill['description']}")

    if new_deps:
        lines.append("")
        lines.append("Dependencies:")
        for dep_id in new_deps:
            dep_name = all_skills.get(dep_id, {}).get('name', 'Unknown')
            lines.append(f"* {dep_id}: {dep_name}")

    lines.append("")
    lines.append("")
    return '\n'.join(lines)

def get_topic_name(topic_code: str) -> str:
    """Get topic name"""
    names = {
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
    return names.get(topic_code, 'Unknown')

def print_summary(all_skills: Dict, g3_skills: Dict, stats: Dict, changes: Dict):
    """Print comprehensive summary"""
    print("\n" + "="*60)
    print("GRADE 3 DEPENDENCY ANALYSIS SUMMARY")
    print("="*60)

    print(f"\n1. TOTAL G3 SKILLS FOUND: {len(g3_skills)}")
    print("\n   Distribution by topic:")
    for topic in sorted(stats['topic_counts'].keys()):
        print(f"   {topic}: {stats['topic_counts'][topic]} skills")

    print(f"\n2. INVALID DEPENDENCIES: {len(stats['invalid_deps'])}")
    if stats['invalid_deps']:
        for inv in stats['invalid_deps']:
            print(f"   {inv['skill']} -> {inv['dep']}: {inv['reason']}")

    print(f"\n3. CROSS-TOPIC DEPENDENCIES ADDED: {sum(len(v) for v in changes['deps_added'].values())}")
    for topic in sorted(changes['deps_added'].keys()):
        adds = changes['deps_added'][topic]
        print(f"\n   {topic}: {len(adds)} dependencies added")
        for add in adds:
            print(f"     {add}")

    print(f"\n4. DEPENDENCIES REMOVED: {sum(len(v) for v in changes['deps_removed'].values())}")
    for topic in sorted(changes['deps_removed'].keys()):
        removes = changes['deps_removed'][topic]
        print(f"\n   {topic}: {len(removes)} dependencies removed")
        for rem in removes:
            print(f"     {rem}")

    print("\n" + "="*60)
    print("KEY PATTERNS OBSERVED")
    print("="*60)

    # Analyze patterns
    app_topics = [t for t in stats['topic_counts'].keys() if t in APPLICATION_TOPICS]
    core_topics = [t for t in stats['topic_counts'].keys() if t in PROGRAMMING_CORE_TOPICS]

    print(f"\n- Programming Core topics (T06-T13): {len(core_topics)} topics, {sum(stats['topic_counts'][t] for t in core_topics)} skills")
    print(f"- Application topics (T14-T24): {len(app_topics)} topics, {sum(stats['topic_counts'][t] for t in app_topics)} skills")
    print(f"- Most application skills depend on core programming concepts")
    print(f"- Conservative approach: Only added dependencies with strong keyword evidence")

    print("\n" + "="*60)
    print("PHASE 2 COMPLETE")
    print("="*60)

if __name__ == '__main__':
    file_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    # Analyze
    all_skills, g3_skills, stats = analyze_g3_skills(file_path)

    # Show analysis
    print(f"\nFound {len(stats['invalid_deps'])} invalid dependencies")
    print(f"Found {len(stats['suggested_deps'])} skills needing cross-topic dependencies\n")

    # Apply fixes
    changes = apply_fixes(file_path, all_skills, g3_skills, stats)

    # Print summary
    print_summary(all_skills, g3_skills, stats, changes)
