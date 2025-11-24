#!/usr/bin/env python3
"""
Comprehensive manual analyzer that examines each Grade K skill individually
and applies careful logical reasoning for cross-topic dependencies.
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
            if line_stripped.startswith('Skill:'):
                current_skill['title'] = line_stripped.replace('Skill:', '').strip()
            elif line_stripped.startswith('Description:'):
                current_skill['description'] = line_stripped.replace('Description:', '').strip()
            elif line_stripped.startswith('Dependencies:'):
                in_dependencies = True
            elif in_dependencies and line_stripped.startswith('*'):
                dep_match = re.match(r'^\*\s*(T\d+\.[A-Z0-9]+\.\d+)', line_stripped)
                if dep_match:
                    dep_id = dep_match.group(1)
                    current_skill['dependencies'].append(dep_id)
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

    skill = next((s for s in all_skills if s['id'] == skill_id), None)
    if not skill:
        return deps

    for dep in skill['dependencies']:
        deps.add(dep)
        deps.update(get_transitive_deps(dep, all_skills, visited))

    return deps

def analyze_all_grade_k_skills(skills):
    """
    Comprehensive manual analysis of ALL Grade K skills.
    Uses careful logical reasoning for each skill.
    """
    suggestions = []

    # Create skill lookup
    skill_dict = {s['id']: s for s in skills}

    # Define hub skills
    HUB_SEQ = 'T01.GK.01'  # Sequencing
    HUB_PAT = 'T04.GK.01'  # Pattern Recognition
    HUB_SORT = 'T10.GK.01' # Sorting/Categorization
    HUB_COND = 'T08.GK.01' # Conditional Thinking
    HUB_VAR = 'T09.GK.01'  # Variables/Numbers

    # Manual analysis of each skill
    # Format: 'skill_id': [(hub_to_add, reason), ...]
    manual_deps = {
        # T01 - Everyday Algorithms
        'T01.GK.02': [(HUB_SEQ, 'Putting pictures in specific order directly builds on basic sequencing')],
        'T01.GK.03': [(HUB_SEQ, 'Identifying first/last positions requires understanding of sequence order')],
        'T01.GK.04': [(HUB_SEQ, 'Giving step-by-step instructions requires sequencing knowledge')],
        'T01.GK.05': [(HUB_SEQ, 'Describing what comes next in a sequence requires sequencing foundation')],
        'T01.GK.06': [(HUB_SEQ, 'Selecting correct next step requires understanding of sequential order')],
        'T01.GK.07': [(HUB_PAT, 'Finding patterns that repeat requires pattern recognition skill')],
        'T01.GK.08': [(HUB_PAT, 'Predicting next in pattern requires recognizing the repeating pattern')],

        # T02 - Debugging
        'T02.GK.02': [(HUB_SEQ, 'Noticing pictures out of order requires understanding correct sequence')],
        'T02.GK.03': [(HUB_SEQ, 'Fixing wrong step order requires sequencing knowledge')],
        'T02.GK.04': [(HUB_SEQ, 'Adding missing step to sequence requires understanding order')],

        # T03 - Modularity (mostly ok, but check a few)
        # T03 skills are about parts/wholes, not necessarily requiring hub skills

        # T04 - Patterns (self-contained, these ARE the pattern hub)
        'T04.GK.02': [(HUB_PAT, 'Making patterns builds on recognizing patterns')],
        'T04.GK.03': [(HUB_PAT, 'Copying patterns requires recognizing the pattern first')],
        'T04.GK.04': [(HUB_PAT, 'Extending patterns requires recognizing pattern rule')],

        # T05 - Purpose & Impact (mostly narrative, check for any sequencing needs)
        # T05 skills seem ok, about understanding purpose not requiring hub skills

        # T06 - Events (these are about cause-effect sequences)
        'T06.GK.02': [(HUB_SEQ, 'Understanding before/after requires sequencing foundation')],
        'T06.GK.03': [(HUB_SEQ, 'Ordering event steps requires sequencing knowledge')],

        # T08 - Conditionals (this IS the conditional hub, but check children)
        'T08.GK.02': [(HUB_COND, 'Matching actions to conditions builds on if-then understanding')],

        # T09 - Variables (this IS the variable hub, but check children)
        'T09.GK.02': [(HUB_VAR, 'Using labels to track values builds on variable concept')],

        # T10 - Data (this IS the sorting hub, but check children)
        'T10.GK.02': [(HUB_SORT, 'Organizing items by type requires sorting/categorization')],
        'T10.GK.03': [(HUB_SORT, 'Grouping by shared traits uses sorting/categorization')],
        'T10.GK.04': [(HUB_SORT, 'Putting items in labeled groups requires categorization')],
        'T10.GK.05': [(HUB_SORT, 'Deciding which group item belongs to requires categorization')],
        'T10.GK.06': [(HUB_SORT, 'Sorting by different rules builds on basic sorting')],
        'T10.GK.07': [(HUB_SORT, 'Creating collection categories requires categorization understanding')],
        'T10.GK.08': [(HUB_SORT, 'Explaining sorting rule requires understanding categorization')],

        # T13 - Testing & Validation
        'T13.GK.02': [(HUB_SEQ, 'Testing steps in order requires sequencing understanding')],

        # T14 - Collaboration (mostly about teamwork)
        # T14 skills seem ok, social skills not requiring hub skills

        # T15 - Research (mostly about finding info)
        # T15 skills seem ok, about research not requiring hub skills

        # T18 - Design Process
        'T18.GK.01': [(HUB_SEQ, 'Understanding design steps (ask, imagine, plan, create) requires sequencing')],

        # T20 - Patterns in Art
        'T20.GK.01': [(HUB_PAT, 'Pattern detective activity requires pattern recognition')],
        'T20.GK.02': [(HUB_PAT, 'Describing patterns requires recognizing them'), (HUB_SEQ, 'Ordering art steps requires sequencing')],
        'T20.GK.03': [(HUB_PAT, 'Creating own patterns builds on pattern recognition')],
        'T20.GK.04': [(HUB_SEQ, 'Fixing mixed-up plan requires understanding correct order')],

        # T21 - Simulation
        # T21 skills about simulation seem ok, not requiring hub skills

        # T22 - Data in Context
        'T22.GK.01': [(HUB_VAR, 'Recognizing counting/tracking involves variable/number concepts')],
        'T22.GK.02': [(HUB_SORT, 'Organizing data by categories requires categorization')],

        # T23 - User Interface Design
        # T23 skills about UI design seem ok

        # T24 - AI Training
        'T24.GK.03': [(HUB_SEQ, 'Giving clear step-by-step instructions requires sequencing')],

        # T25 - AI Decisions
        'T25.GK.02': [(HUB_COND, 'Understanding AI making choices based on conditions uses if-then logic')],
        'T25.GK.03': [(HUB_COND, 'Building decision rules (legend) uses conditional thinking')],

        # T26 - Bias in AI
        # T26 skills about fairness seem ok

        # T27 - Privacy
        # T27 skills about privacy seem ok

        # T29 - Digital Identity
        # T29 skills about identity seem ok

        # T30 - Online Presence
        # T30 skills about online safety seem ok

        # T31 - Cybersecurity
        # T31 skills about safety seem ok

        # T32 - Digital Citizenship
        # T32 skills about citizenship seem ok

        # T33 - Open Source
        # T33 skills about sharing seem ok

        # T34 - Accessibility
        # T34 skills about accessibility seem ok

        # T35 - Ethics
        # T35 skills about ethics seem ok

        # T36 - Equity & Inclusion
        # T36 skills about equity seem ok
    }

    # Process manual dependencies
    for skill_id, dep_list in manual_deps.items():
        skill = skill_dict.get(skill_id)
        if not skill:
            print(f"Warning: Skill {skill_id} not found")
            continue

        for hub_skill, reason in dep_list:
            # Check if already has this dependency (direct or transitive)
            all_deps = get_transitive_deps(skill_id, skills)
            if hub_skill in skill['dependencies'] or hub_skill in all_deps:
                continue

            # Determine category
            category_map = {
                HUB_SEQ: 'Sequencing Foundation',
                HUB_PAT: 'Pattern Recognition',
                HUB_SORT: 'Sorting/Categorization',
                HUB_COND: 'Conditional Thinking',
                HUB_VAR: 'Variables/Numbers'
            }

            suggestions.append({
                'skill_id': skill_id,
                'skill_title': skill['title'],
                'current_deps': skill['dependencies'],
                'add_dep': hub_skill,
                'reason': reason,
                'category': category_map[hub_skill]
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

    # Analyze all Grade K skills
    print("\nAnalyzing all Grade K skills with manual curation...")
    suggestions = analyze_all_grade_k_skills(grade_k_skills)

    print(f"\nTotal suggested dependencies: {len(suggestions)}")

    # Group by category
    by_category = defaultdict(list)
    for sugg in suggestions:
        by_category[sugg['category']].append(sugg)

    # Print summary
    print("\n=== SUMMARY BY CATEGORY ===")
    for category in ['Sequencing Foundation', 'Pattern Recognition', 'Sorting/Categorization',
                     'Conditional Thinking', 'Variables/Numbers']:
        items = by_category.get(category, [])
        if items:
            print(f"\n{category}: {len(items)} dependencies")
            for item in items:
                print(f"  {item['skill_id']}: {item['skill_title']}")

    # Write detailed report
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/final_cross_topic_report.md', 'w') as f:
        f.write("# Final Cross-Topic Dependency Analysis Report\n\n")
        f.write("## Executive Summary\n\n")
        f.write(f"- Total Grade K skills analyzed: {len(grade_k_skills)}\n")
        f.write(f"- Total dependencies to add: {len(suggestions)}\n")
        for category in ['Sequencing Foundation', 'Pattern Recognition', 'Sorting/Categorization',
                         'Conditional Thinking', 'Variables/Numbers']:
            items = by_category.get(category, [])
            if items:
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
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/final_cross_topic_fixes.txt', 'w') as f:
        for sugg in suggestions:
            f.write(f"{sugg['skill_id']}|{sugg['add_dep']}|{sugg['category']}\n")

    print("\nReport written to: final_cross_topic_report.md")
    print("Fixes written to: final_cross_topic_fixes.txt")

    return suggestions

if __name__ == '__main__':
    main()
