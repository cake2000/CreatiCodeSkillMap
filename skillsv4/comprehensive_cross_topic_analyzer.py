#!/usr/bin/env python3
"""
Comprehensive second-pass analyzer for missing cross-topic dependencies in Grade K skills.
Focuses on 5 key hub skills that should have broader cross-topic dependencies.
"""

import re
from collections import defaultdict

def parse_skills(content):
    """Parse all skills from markdown content."""
    skills = []
    current_skill = None
    in_dependencies = False

    lines = content.split('\n')
    for i, line in enumerate(lines):
        line_stripped = line.strip()

        # Match skill ID line like "ID: T01.GK.01"
        if line_stripped.startswith('ID:'):
            if current_skill:
                skills.append(current_skill)

            skill_id = line_stripped.replace('ID:', '').strip()
            current_skill = {
                'id': skill_id,
                'title': '',
                'description': '',
                'dependencies': [],
                'line_num': i
            }
            in_dependencies = False
            continue

        if current_skill:
            # Extract skill title
            if line_stripped.startswith('Skill:'):
                current_skill['title'] = line_stripped.replace('Skill:', '').strip()

            # Extract description
            elif line_stripped.startswith('Description:'):
                current_skill['description'] = line_stripped.replace('Description:', '').strip()

            # Extract dependencies section
            elif line_stripped.startswith('Dependencies:'):
                in_dependencies = True

            # Parse dependency items
            elif in_dependencies and line_stripped.startswith('*'):
                # Parse lines like "* T03.GK.01: Identify parts that make up a whole"
                dep_match = re.match(r'^\*\s*(T\d+\.[A-Z0-9]+\.\d+)', line_stripped)
                if dep_match:
                    dep_id = dep_match.group(1)
                    current_skill['dependencies'].append(dep_id)

            # Stop dependencies section when we hit a blank line or new section
            elif in_dependencies and (not line_stripped or line_stripped.startswith('ID:')):
                in_dependencies = False

    if current_skill:
        skills.append(current_skill)

    return skills

def get_transitive_deps(skill_id, all_skills, visited=None):
    """Get all transitive dependencies for a skill."""
    if visited is None:
        visited = set()

    if skill_id in visited:
        return set()

    visited.add(skill_id)
    deps = set()

    # Find the skill
    skill = next((s for s in all_skills if s['id'] == skill_id), None)
    if not skill:
        return deps

    # Add direct dependencies
    for dep in skill['dependencies']:
        deps.add(dep)
        # Add transitive dependencies
        deps.update(get_transitive_deps(dep, all_skills, visited))

    return deps

def analyze_sequencing_dependencies(skills):
    """Category 1: Skills that should depend on T01.GK.01 (sequencing)."""
    hub_skill = 'T01.GK.01'
    suggestions = []

    sequencing_keywords = [
        'step', 'order', 'sequence', 'first', 'second', 'third', 'next', 'then',
        'before', 'after', 'follow', 'instruction', 'algorithm', 'procedure',
        'chronological', 'consecutive', 'progression'
    ]

    for skill in skills:
        if skill['id'] == hub_skill:
            continue

        # Check if already has dependency (direct or transitive)
        all_deps = get_transitive_deps(skill['id'], skills)
        if hub_skill in skill['dependencies'] or hub_skill in all_deps:
            continue

        # Check description and title for sequencing concepts
        text = (skill['title'] + ' ' + skill['description']).lower()

        if any(keyword in text for keyword in sequencing_keywords):
            reason = f"Involves sequencing/ordering - found keywords in: {text[:100]}"
            suggestions.append({
                'skill_id': skill['id'],
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': hub_skill,
                'reason': reason,
                'category': 'Sequencing Foundation'
            })

    return suggestions

def analyze_pattern_dependencies(skills):
    """Category 2: Skills that should depend on T04.GK.01 (pattern recognition)."""
    hub_skill = 'T04.GK.01'
    suggestions = []

    pattern_keywords = [
        'pattern', 'repeat', 'repetition', 'recurring', 'cycle', 'regular',
        'predictable', 'recognize', 'identify pattern', 'same', 'similar',
        'matching', 'consistent', 'rhythm'
    ]

    for skill in skills:
        if skill['id'] == hub_skill:
            continue

        all_deps = get_transitive_deps(skill['id'], skills)
        if hub_skill in skill['dependencies'] or hub_skill in all_deps:
            continue

        text = (skill['title'] + ' ' + skill['description']).lower()

        if any(keyword in text for keyword in pattern_keywords):
            reason = f"Involves pattern recognition - found keywords in: {text[:100]}"
            suggestions.append({
                'skill_id': skill['id'],
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': hub_skill,
                'reason': reason,
                'category': 'Pattern Recognition'
            })

    return suggestions

def analyze_sorting_dependencies(skills):
    """Category 3: Skills that should depend on T10.GK.01 (sorting/categorization)."""
    hub_skill = 'T10.GK.01'
    suggestions = []

    sorting_keywords = [
        'sort', 'group', 'category', 'categorize', 'classify', 'organize',
        'separate', 'divide', 'type', 'kind', 'collection', 'set',
        'same type', 'different type', 'belongs to'
    ]

    for skill in skills:
        if skill['id'] == hub_skill:
            continue

        all_deps = get_transitive_deps(skill['id'], skills)
        if hub_skill in skill['dependencies'] or hub_skill in all_deps:
            continue

        text = (skill['title'] + ' ' + skill['description']).lower()

        if any(keyword in text for keyword in sorting_keywords):
            reason = f"Involves sorting/categorization - found keywords in: {text[:100]}"
            suggestions.append({
                'skill_id': skill['id'],
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': hub_skill,
                'reason': reason,
                'category': 'Sorting/Categorization'
            })

    return suggestions

def analyze_conditional_dependencies(skills):
    """Category 4: Skills that should depend on T08.GK.01 (conditional thinking)."""
    hub_skill = 'T08.GK.01'
    suggestions = []

    conditional_keywords = [
        'if', 'then', 'when', 'condition', 'rule', 'match', 'cause', 'effect',
        'because', 'result', 'consequence', 'decision', 'choose', 'select',
        'branch', 'option', 'depending on'
    ]

    for skill in skills:
        if skill['id'] == hub_skill:
            continue

        all_deps = get_transitive_deps(skill['id'], skills)
        if hub_skill in skill['dependencies'] or hub_skill in all_deps:
            continue

        text = (skill['title'] + ' ' + skill['description']).lower()

        if any(keyword in text for keyword in conditional_keywords):
            reason = f"Involves conditional/cause-effect thinking - found keywords in: {text[:100]}"
            suggestions.append({
                'skill_id': skill['id'],
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': hub_skill,
                'reason': reason,
                'category': 'Conditional Thinking'
            })

    return suggestions

def analyze_variable_dependencies(skills):
    """Category 5: Skills that should depend on T09.GK.01 (variables/numbers)."""
    hub_skill = 'T09.GK.01'
    suggestions = []

    variable_keywords = [
        'count', 'number', 'quantity', 'amount', 'track', 'measure',
        'value', 'score', 'total', 'many', 'few', 'more', 'less',
        'label', 'variable', 'data', 'information', 'record'
    ]

    for skill in skills:
        if skill['id'] == hub_skill:
            continue

        all_deps = get_transitive_deps(skill['id'], skills)
        if hub_skill in skill['dependencies'] or hub_skill in all_deps:
            continue

        text = (skill['title'] + ' ' + skill['description']).lower()

        if any(keyword in text for keyword in variable_keywords):
            reason = f"Involves counting/tracking/variables - found keywords in: {text[:100]}"
            suggestions.append({
                'skill_id': skill['id'],
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': hub_skill,
                'reason': reason,
                'category': 'Variables/Numbers'
            })

    return suggestions

def main():
    print("Reading allskills.md...")
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r', encoding='utf-8') as f:
        content = f.read()

    print("Parsing Grade K skills...")
    all_skills = parse_skills(content)
    grade_k_skills = [s for s in all_skills if '.GK.' in s['id']]

    print(f"Found Grade K skills: {len(grade_k_skills)}")

    # Analyze each category
    print("\n=== CATEGORY 1: SEQUENCING FOUNDATION (T01.GK.01) ===")
    seq_suggestions = analyze_sequencing_dependencies(grade_k_skills)
    print(f"Found suggestions: {len(seq_suggestions)}")

    print("\n=== CATEGORY 2: PATTERN RECOGNITION (T04.GK.01) ===")
    pattern_suggestions = analyze_pattern_dependencies(grade_k_skills)
    print(f"Found suggestions: {len(pattern_suggestions)}")

    print("\n=== CATEGORY 3: SORTING/CATEGORIZATION (T10.GK.01) ===")
    sorting_suggestions = analyze_sorting_dependencies(grade_k_skills)
    print(f"Found suggestions: {len(sorting_suggestions)}")

    print("\n=== CATEGORY 4: CONDITIONAL THINKING (T08.GK.01) ===")
    conditional_suggestions = analyze_conditional_dependencies(grade_k_skills)
    print(f"Found suggestions: {len(conditional_suggestions)}")

    print("\n=== CATEGORY 5: VARIABLES/NUMBERS (T09.GK.01) ===")
    variable_suggestions = analyze_variable_dependencies(grade_k_skills)
    print(f"Found suggestions: {len(variable_suggestions)}")

    # Combine all suggestions
    all_suggestions = (seq_suggestions + pattern_suggestions + sorting_suggestions +
                      conditional_suggestions + variable_suggestions)

    # Write detailed report
    print(f"\n\nTotal suggestions: {len(all_suggestions)}")

    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/cross_topic_dependency_report.md', 'w') as f:
        f.write("# Comprehensive Cross-Topic Dependency Analysis Report\n\n")
        f.write("## Executive Summary\n\n")
        f.write(f"- Total Grade K skills analyzed: {len(grade_k_skills)}\n")
        f.write(f"- Total missing dependencies found: {len(all_suggestions)}\n")
        f.write(f"  - Category 1 (Sequencing): {len(seq_suggestions)}\n")
        f.write(f"  - Category 2 (Pattern Recognition): {len(pattern_suggestions)}\n")
        f.write(f"  - Category 3 (Sorting/Categorization): {len(sorting_suggestions)}\n")
        f.write(f"  - Category 4 (Conditional Thinking): {len(conditional_suggestions)}\n")
        f.write(f"  - Category 5 (Variables/Numbers): {len(variable_suggestions)}\n")
        f.write("\n---\n\n")

        # Group by category
        for category_name, category_suggestions in [
            ('Category 1: Sequencing Foundation (T01.GK.01)', seq_suggestions),
            ('Category 2: Pattern Recognition (T04.GK.01)', pattern_suggestions),
            ('Category 3: Sorting/Categorization (T10.GK.01)', sorting_suggestions),
            ('Category 4: Conditional Thinking (T08.GK.01)', conditional_suggestions),
            ('Category 5: Variables/Numbers (T09.GK.01)', variable_suggestions)
        ]:
            if category_suggestions:
                f.write(f"## {category_name}\n\n")
                for i, sugg in enumerate(category_suggestions, 1):
                    f.write(f"### {i}. {sugg['skill_id']} - {sugg['skill_title']}\n\n")
                    f.write(f"**Current Dependencies:** {', '.join(sugg['current_deps']) if sugg['current_deps'] else 'None'}\n\n")
                    f.write(f"**Add Dependency:** {sugg['add_dep']}\n\n")
                    f.write(f"**Reason:** {sugg['reason']}\n\n")
                    f.write("---\n\n")

    # Generate machine-readable output for applying fixes
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/cross_topic_fixes.txt', 'w') as f:
        for sugg in all_suggestions:
            f.write(f"{sugg['skill_id']}|{sugg['add_dep']}|{sugg['category']}\n")

    print("\nReport written to: cross_topic_dependency_report.md")
    print("Fixes written to: cross_topic_fixes.txt")

    return all_suggestions

if __name__ == '__main__':
    main()
