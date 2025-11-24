#!/usr/bin/env python3
"""
Apply carefully curated cross-topic dependencies based on manual review of each skill.
"""

import re

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

def get_curated_dependencies():
    """
    Return carefully curated cross-topic dependencies.
    Each entry verified by reading actual skill description.
    """
    # Format: 'skill_id': [(hub_skill, reason), ...]

    curated = {
        # Category 1: Sequencing Foundation (T01.GK.01)
        'T01.GK.02': [('T01.GK.01', 'Putting 4 pictures in order builds on basic 3-picture sequencing')],
        'T01.GK.03': [('T01.GK.01', 'Finding first/last positions requires sequencing foundation')],
        'T06.GK.02': [('T01.GK.01', 'Understanding before/after concepts requires sequencing')],
        'T06.GK.03': [('T01.GK.01', 'Ordering morning routine steps requires sequencing')],
        'T20.GK.04': [('T01.GK.01', 'Fixing mixed-up art plan requires understanding correct order')],
        'T24.GK.03': [('T01.GK.01', 'Giving step-by-step instructions requires sequencing')],

        # Category 2: Pattern Recognition (T04.GK.01)
        'T01.GK.07': [('T04.GK.01', 'Finding repeating patterns requires pattern recognition')],
        'T01.GK.08': [('T04.GK.01', 'Predicting next in pattern requires recognizing the pattern')],
        'T04.GK.02': [('T04.GK.01', 'Making patterns builds on recognizing patterns')],
        'T04.GK.03': [('T04.GK.01', 'Copying patterns requires recognizing the pattern first')],
        'T04.GK.04': [('T04.GK.01', 'Extending patterns requires recognizing pattern rule')],
        'T20.GK.01': [('T04.GK.01', 'Pattern detective activity requires pattern recognition')],
        'T20.GK.02': [('T04.GK.01', 'Describing patterns requires recognizing them')],
        'T20.GK.03': [('T04.GK.01', 'Creating own patterns builds on pattern recognition')],

        # Category 3: Sorting/Categorization (T10.GK.01)
        'T10.GK.02': [('T10.GK.01', 'Organizing toy pictures by type requires sorting')],
        'T10.GK.03': [('T10.GK.01', 'Grouping by shared traits uses categorization')],
        'T10.GK.04': [('T10.GK.01', 'Putting items in labeled groups requires categorization')],
        'T10.GK.06': [('T10.GK.01', 'Sorting by different rules builds on basic sorting')],
        'T10.GK.07': [('T10.GK.01', 'Creating collection categories requires categorization')],
        'T10.GK.08': [('T10.GK.01', 'Explaining why items are grouped requires categorization')],

        # Category 4: Conditional Thinking (T08.GK.01)
        'T08.GK.02': [('T08.GK.01', 'Matching actions to situations uses if-then logic')],

        # Category 5: Variables/Numbers (T09.GK.01)
        'T09.GK.02': [('T09.GK.01', 'Using labels to track values builds on variable concept')],
    }

    return curated

def apply_fixes(content, curated_deps, skills):
    """Apply the curated dependencies to the content."""
    lines = content.split('\n')
    modifications = []

    for skill_id, dep_list in curated_deps.items():
        skill = next((s for s in skills if s['id'] == skill_id), None)
        if not skill:
            print(f"Warning: Skill {skill_id} not found")
            continue

        for hub_skill, reason in dep_list:
            # Check if already has dependency (direct or transitive)
            all_deps = get_transitive_deps(skill_id, skills)
            if hub_skill in skill['dependencies'] or hub_skill in all_deps:
                print(f"Skipping {skill_id} -> {hub_skill}: already has transitive dependency")
                continue

            # Find the skill title for the hub skill
            hub_skill_obj = next((s for s in skills if s['id'] == hub_skill), None)
            if not hub_skill_obj:
                print(f"Warning: Hub skill {hub_skill} not found")
                continue

            # Find the dependencies section for this skill
            skill_line = skill['line_num']
            deps_line = None

            for i in range(skill_line, min(skill_line + 20, len(lines))):
                if lines[i].strip().startswith('Dependencies:'):
                    deps_line = i
                    break

            if deps_line is None:
                print(f"Warning: Could not find Dependencies section for {skill_id}")
                continue

            # Find where to insert (after Dependencies: line, or after last dependency)
            insert_line = deps_line + 1

            # Check if there are existing dependencies
            has_deps = False
            for i in range(deps_line + 1, min(deps_line + 20, len(lines))):
                if lines[i].strip().startswith('*'):
                    has_deps = True
                    insert_line = i + 1
                elif lines[i].strip() and not lines[i].strip().startswith('*'):
                    break

            # Create the new dependency line
            new_dep_line = f"* {hub_skill}: {hub_skill_obj['title']}"

            modifications.append({
                'skill_id': skill_id,
                'hub_skill': hub_skill,
                'reason': reason,
                'insert_line': insert_line,
                'new_line': new_dep_line
            })

            print(f"Will add: {skill_id} -> {hub_skill}: {reason}")

    # Apply modifications (in reverse order to maintain line numbers)
    modifications.sort(key=lambda x: x['insert_line'], reverse=True)

    for mod in modifications:
        lines.insert(mod['insert_line'], mod['new_line'])

    return '\n'.join(lines), modifications

def main():
    print("Reading allskills.md...")
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r', encoding='utf-8') as f:
        content = f.read()

    print("Parsing skills...")
    all_skills = parse_skills(content)
    grade_k_skills = [s for s in all_skills if '.GK.' in s['id']]
    print(f"Found Grade K skills: {len(grade_k_skills)}")

    # Get curated dependencies
    curated_deps = get_curated_dependencies()
    print(f"\nCurated dependencies: {len(curated_deps)} skills to update")

    # Apply fixes
    print("\nApplying fixes...")
    modified_content, modifications = apply_fixes(content, curated_deps, all_skills)

    print(f"\nActual modifications made: {len(modifications)}")

    # Write modified content
    print("\nWriting modified allskills.md...")
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'w', encoding='utf-8') as f:
        f.write(modified_content)

    # Write summary report
    print("Writing summary report...")
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/cross_topic_changes_applied.md', 'w') as f:
        f.write("# Cross-Topic Dependencies Applied\n\n")
        f.write(f"Total modifications: {len(modifications)}\n\n")

        by_category = {}
        for mod in modifications:
            # Determine category
            if mod['hub_skill'] == 'T01.GK.01':
                cat = 'Sequencing Foundation'
            elif mod['hub_skill'] == 'T04.GK.01':
                cat = 'Pattern Recognition'
            elif mod['hub_skill'] == 'T10.GK.01':
                cat = 'Sorting/Categorization'
            elif mod['hub_skill'] == 'T08.GK.01':
                cat = 'Conditional Thinking'
            elif mod['hub_skill'] == 'T09.GK.01':
                cat = 'Variables/Numbers'
            else:
                cat = 'Other'

            if cat not in by_category:
                by_category[cat] = []
            by_category[cat].append(mod)

        for category in ['Sequencing Foundation', 'Pattern Recognition', 'Sorting/Categorization',
                         'Conditional Thinking', 'Variables/Numbers', 'Other']:
            mods = by_category.get(category, [])
            if mods:
                f.write(f"## {category} ({len(mods)})\n\n")
                for mod in mods:
                    f.write(f"- **{mod['skill_id']}** now depends on **{mod['hub_skill']}**\n")
                    f.write(f"  - Reason: {mod['reason']}\n\n")

    print("\nDone! Summary written to: cross_topic_changes_applied.md")

if __name__ == '__main__':
    main()
