#!/usr/bin/env python3
"""
Refined cross-topic analyzer that uses manual curation and logical analysis
rather than keyword matching to avoid false positives.
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

def analyze_cross_topic_dependencies(skills):
    """
    Manually curated analysis of cross-topic dependencies.
    Only suggests dependencies that are logically necessary.
    """
    suggestions = []

    # Hub skills to check
    hub_skills = {
        'T01.GK.01': 'Sequencing Foundation',
        'T04.GK.01': 'Pattern Recognition',
        'T08.GK.01': 'Conditional Thinking',
        'T09.GK.01': 'Variables/Numbers',
        'T10.GK.01': 'Sorting/Categorization'
    }

    # Manually curated rules for each skill that should have cross-topic deps
    manual_suggestions = []

    # Category 1: Sequencing dependencies (T01.GK.01)
    # Only add if skill explicitly requires understanding of ordering/sequencing
    sequencing_deps = {
        'T01.GK.02': 'Putting pictures in order requires basic sequencing skill',
        'T01.GK.03': 'Finding first/last requires understanding of sequence positions',
        'T06.GK.01': 'Event sequences build on basic ordering',
        'T06.GK.02': 'Before/after concepts require sequencing foundation',
        'T20.GK.04': 'Fixing mixed-up plans requires understanding correct order',
    }

    # Category 2: Pattern Recognition (T04.GK.01)
    # Only add if skill involves recognizing repetition or patterns
    pattern_deps = {
        'T01.GK.07': 'Finding repeating patterns requires pattern recognition',
        'T01.GK.08': 'Predicting next in pattern builds on pattern recognition',
        'T20.GK.01': 'Pattern detective explicitly uses pattern recognition',
        'T20.GK.02': 'Describing patterns requires recognizing them first',
        'T20.GK.03': 'Creating patterns builds on recognition',
    }

    # Category 3: Sorting/Categorization (T10.GK.01)
    # Only add if skill involves grouping or categorizing
    sorting_deps = {
        'T10.GK.02': 'Organizing items builds on basic sorting',
        'T10.GK.03': 'Grouping by shared traits uses sorting/categorization',
        'T22.GK.02': 'Organizing data requires categorization skills',
    }

    # Category 4: Conditional Thinking (T08.GK.01)
    # Only add if skill involves if-then logic or cause-effect
    conditional_deps = {
        'T08.GK.02': 'Matching actions to situations uses conditional logic',
        'T08.GK.03': 'Choosing correct action requires if-then thinking',
        'T25.GK.03': 'AI choices based on conditions uses if-then logic',
    }

    # Category 5: Variables/Numbers (T09.GK.01)
    # Only add if skill involves counting, tracking, or quantifying
    variable_deps = {
        'T09.GK.02': 'Using labels to track values builds on variable concept',
        'T22.GK.01': 'Counting items for data involves tracking quantities',
    }

    # Process each category
    for skill_id, reason in sequencing_deps.items():
        skill = next((s for s in skills if s['id'] == skill_id), None)
        if not skill:
            continue

        all_deps = get_transitive_deps(skill_id, skills)
        if 'T01.GK.01' not in skill['dependencies'] and 'T01.GK.01' not in all_deps:
            manual_suggestions.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': 'T01.GK.01',
                'reason': reason,
                'category': 'Sequencing Foundation'
            })

    for skill_id, reason in pattern_deps.items():
        skill = next((s for s in skills if s['id'] == skill_id), None)
        if not skill:
            continue

        all_deps = get_transitive_deps(skill_id, skills)
        if 'T04.GK.01' not in skill['dependencies'] and 'T04.GK.01' not in all_deps:
            manual_suggestions.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': 'T04.GK.01',
                'reason': reason,
                'category': 'Pattern Recognition'
            })

    for skill_id, reason in sorting_deps.items():
        skill = next((s for s in skills if s['id'] == skill_id), None)
        if not skill:
            continue

        all_deps = get_transitive_deps(skill_id, skills)
        if 'T10.GK.01' not in skill['dependencies'] and 'T10.GK.01' not in all_deps:
            manual_suggestions.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': 'T10.GK.01',
                'reason': reason,
                'category': 'Sorting/Categorization'
            })

    for skill_id, reason in conditional_deps.items():
        skill = next((s for s in skills if s['id'] == skill_id), None)
        if not skill:
            continue

        all_deps = get_transitive_deps(skill_id, skills)
        if 'T08.GK.01' not in skill['dependencies'] and 'T08.GK.01' not in all_deps:
            manual_suggestions.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': 'T08.GK.01',
                'reason': reason,
                'category': 'Conditional Thinking'
            })

    for skill_id, reason in variable_deps.items():
        skill = next((s for s in skills if s['id'] == skill_id), None)
        if not skill:
            continue

        all_deps = get_transitive_deps(skill_id, skills)
        if 'T09.GK.01' not in skill['dependencies'] and 'T09.GK.01' not in all_deps:
            manual_suggestions.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': 'T09.GK.01',
                'reason': reason,
                'category': 'Variables/Numbers'
            })

    return manual_suggestions

def main():
    print("Reading allskills.md...")
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r', encoding='utf-8') as f:
        content = f.read()

    print("Parsing Grade K skills...")
    all_skills = parse_skills(content)
    grade_k_skills = [s for s in all_skills if '.GK.' in s['id']]

    print(f"Found Grade K skills: {len(grade_k_skills)}")

    # Analyze cross-topic dependencies
    print("\nAnalyzing cross-topic dependencies...")
    suggestions = analyze_cross_topic_dependencies(grade_k_skills)

    print(f"\nTotal curated suggestions: {len(suggestions)}")

    # Group by category
    by_category = defaultdict(list)
    for sugg in suggestions:
        by_category[sugg['category']].append(sugg)

    # Write detailed report
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/refined_cross_topic_report.md', 'w') as f:
        f.write("# Refined Cross-Topic Dependency Analysis Report\n\n")
        f.write("## Executive Summary\n\n")
        f.write(f"- Total Grade K skills analyzed: {len(grade_k_skills)}\n")
        f.write(f"- Total curated dependencies to add: {len(suggestions)}\n")
        for category, items in sorted(by_category.items()):
            f.write(f"  - {category}: {len(items)}\n")
        f.write("\n---\n\n")

        # Group by category
        for category in ['Sequencing Foundation', 'Pattern Recognition', 'Sorting/Categorization',
                         'Conditional Thinking', 'Variables/Numbers']:
            category_suggestions = by_category.get(category, [])
            if category_suggestions:
                f.write(f"## {category}\n\n")
                for i, sugg in enumerate(category_suggestions, 1):
                    f.write(f"### {i}. {sugg['skill_id']} - {sugg['skill_title']}\n\n")
                    f.write(f"**Current Dependencies:** {', '.join(sugg['current_deps']) if sugg['current_deps'] else 'None'}\n\n")
                    f.write(f"**Add Dependency:** {sugg['add_dep']}\n\n")
                    f.write(f"**Reason:** {sugg['reason']}\n\n")
                    f.write("---\n\n")

    # Generate machine-readable output for applying fixes
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/refined_cross_topic_fixes.txt', 'w') as f:
        for sugg in suggestions:
            f.write(f"{sugg['skill_id']}|{sugg['add_dep']}|{sugg['category']}\n")

    print("\nReport written to: refined_cross_topic_report.md")
    print("Fixes written to: refined_cross_topic_fixes.txt")

    # Print summary by category
    print("\n=== SUMMARY BY CATEGORY ===")
    for category in ['Sequencing Foundation', 'Pattern Recognition', 'Sorting/Categorization',
                     'Conditional Thinking', 'Variables/Numbers']:
        items = by_category.get(category, [])
        print(f"\n{category}: {len(items)} dependencies")
        for item in items:
            print(f"  - {item['skill_id']}: {item['skill_title']}")

    return suggestions

if __name__ == '__main__':
    main()
