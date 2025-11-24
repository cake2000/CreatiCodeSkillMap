#!/usr/bin/env python3
"""
Final refined analysis of Grade 3 cross-topic dependencies for Topics T01-T12.
Manually verified based on actual skill descriptions.
"""

import re

def parse_skills(filepath):
    """Parse the allskills.md file and extract ALL skills with dependencies."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skill_pattern = re.compile(r'^ID: (T\d+\.G\d+\.\d+(?:\.\d+)?)$', re.MULTILINE)
    skills = {}

    parts = skill_pattern.split(content)
    for i in range(1, len(parts), 2):
        skill_id = parts[i]
        skill_content = parts[i+1] if i+1 < len(parts) else ""

        # Extract skill name
        name_match = re.search(r'^Skill: (.+)$', skill_content, re.MULTILINE)
        skill_name = name_match.group(1) if name_match else ""

        # Extract dependencies
        deps = []
        deps_section = re.search(r'Dependencies:\n((?:\* .+\n?)+)', skill_content, re.MULTILINE)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.match(r'\* ([^:]+):', line)
                if dep_match:
                    deps.append(dep_match.group(1))

        skills[skill_id] = {
            'name': skill_name,
            'dependencies': deps
        }

    return skills

def has_transitive_dependency(skill_id, target_topic, skills, visited=None):
    """Check if skill has a transitive dependency on target_topic."""
    if visited is None:
        visited = set()

    if skill_id in visited:
        return False
    visited.add(skill_id)

    if skill_id not in skills:
        return False

    for dep in skills[skill_id]['dependencies']:
        if dep.startswith(target_topic + '.'):
            return True
        if has_transitive_dependency(dep, target_topic, skills, visited):
            return True

    return False

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing all skills...")
    all_skills = parse_skills(filepath)
    print(f"Found {len(all_skills)} total skills\n")

    # Manually verified recommendations based on actual descriptions
    recommendations = []

    # T01.G3.12: "possibly with a loop" - should depend on loop tracing
    if not has_transitive_dependency('T01.G3.12', 'T07', all_skills):
        recommendations.append({
            'skill_id': 'T01.G3.12',
            'skill_name': 'Predict the final state of a simple algorithm',
            'dep_id': 'T07.G3.02',
            'dep_name': 'Trace a script with a simple loop',
            'reason': 'Description says "possibly with a loop" - needs loop tracing skills'
        })

    # T01.G3.16: Mentions "checking if a key is pressed" - involves conditionals
    if not has_transitive_dependency('T01.G3.16', 'T08', all_skills):
        recommendations.append({
            'skill_id': 'T01.G3.16',
            'skill_name': "Identify when to use 'repeat forever' vs 'repeat N times'",
            'dep_id': 'T08.G3.01',
            'dep_name': 'Use a simple if in a script',
            'reason': 'Example mentions "checking if a key is pressed" which uses conditionals'
        })

    # T02.G3.03: Just a simple sequence, doesn't actually need if/else
    # SKIP - description doesn't mention if/else

    # T02.G3.04: "Trace a block sequence with an if/else decision" - NEEDS if/else
    if not has_transitive_dependency('T02.G3.04', 'T08', all_skills):
        recommendations.append({
            'skill_id': 'T02.G3.04',
            'skill_name': 'Trace a block sequence with an if/else decision',
            'dep_id': 'T08.G3.01',
            'dep_name': 'Use a simple if in a script',
            'reason': 'Skill explicitly traces scripts with if/else blocks'
        })

    # T02.G3.05: "Create a block script with one if/else decision"
    if not has_transitive_dependency('T02.G3.05', 'T08', all_skills):
        recommendations.append({
            'skill_id': 'T02.G3.05',
            'skill_name': 'Create a block script with one if/else decision',
            'dep_id': 'T08.G3.01',
            'dep_name': 'Use a simple if in a script',
            'reason': 'Skill explicitly creates scripts with if/else blocks'
        })

    # T02.G3.06: Compare two block sequences - may include if/else but not explicitly stated
    # SKIP for now

    # T04.G3.04.02: "using parameters or variables as placeholders"
    if not has_transitive_dependency('T04.G3.04.02', 'T09', all_skills):
        recommendations.append({
            'skill_id': 'T04.G3.04.02',
            'skill_name': 'Create a custom block (template) for repeated code patterns',
            'dep_id': 'T09.G3.01.01',
            'dep_name': 'Create a variable and set it',
            'reason': 'Uses parameters/variables as placeholders in custom blocks'
        })

    # T04.G3.08: "count how many times" suggests counter pattern with variables
    if not has_transitive_dependency('T04.G3.08', 'T09', all_skills):
        recommendations.append({
            'skill_id': 'T04.G3.08',
            'skill_name': 'Match algorithm descriptions to code pattern shapes',
            'dep_id': 'T09.G3.01.01',
            'dep_name': 'Create a variable and set it',
            'reason': 'Matches patterns like "count how many times" which use counter variables'
        })

    # T08.G3.01: Conditionals need scripts/events to run in
    if not has_transitive_dependency('T08.G3.01', 'T06', all_skills):
        recommendations.append({
            'skill_id': 'T08.G3.01',
            'skill_name': 'Use a simple if in a script',
            'dep_id': 'T06.G3.01',
            'dep_name': 'Build a green-flag script that runs a 3-5 block sequence',
            'reason': 'Conditionals need to be placed in event-triggered scripts'
        })

    # T08.G3.05: "Fix a condition that uses the wrong comparison operator"
    if not has_transitive_dependency('T08.G3.05', 'T09', all_skills):
        recommendations.append({
            'skill_id': 'T08.G3.05',
            'skill_name': 'Fix a condition that uses the wrong comparison operator',
            'dep_id': 'T09.G3.01.01',
            'dep_name': 'Create a variable and set it',
            'reason': 'Comparison operators typically compare variables or values'
        })

    # T09.G3.01.02: "Set a variable to an initial value at program start"
    if not has_transitive_dependency('T09.G3.01.02', 'T06', all_skills):
        recommendations.append({
            'skill_id': 'T09.G3.01.02',
            'skill_name': 'Set a variable to an initial value at program start',
            'dep_id': 'T06.G3.01',
            'dep_name': 'Build a green-flag script that runs a 3-5 block sequence',
            'reason': 'Setting initial values at "program start" requires green flag event'
        })

    # T09.G3.01.03: "Change a variable value" - happens in scripts
    if not has_transitive_dependency('T09.G3.01.03', 'T06', all_skills):
        recommendations.append({
            'skill_id': 'T09.G3.01.03',
            'skill_name': 'Change a variable value by 1 using the change block',
            'dep_id': 'T06.G3.01',
            'dep_name': 'Build a green-flag script that runs a 3-5 block sequence',
            'reason': 'Variable changes occur within event-triggered scripts'
        })

    # T10.G3.07: Already has T10.G3.05 which has T07.G3.01, so transitive dep exists
    # SKIP - has transitive dependency through T10.G3.05

    # T12.G3.03.01: "Use clearer variable names"
    if not has_transitive_dependency('T12.G3.03.01', 'T09', all_skills):
        recommendations.append({
            'skill_id': 'T12.G3.03.01',
            'skill_name': 'Use clearer variable names to improve readability',
            'dep_id': 'T09.G3.01.01',
            'dep_name': 'Create a variable and set it',
            'reason': 'Renaming variables requires understanding of variables'
        })

    # T12.G3.03.03: "Split complex scripts into separate event-driven scripts"
    if not has_transitive_dependency('T12.G3.03.03', 'T06', all_skills):
        recommendations.append({
            'skill_id': 'T12.G3.03.03',
            'skill_name': 'Split complex scripts into separate event-driven scripts',
            'dep_id': 'T06.G3.01',
            'dep_name': 'Build a green-flag script that runs a 3-5 block sequence',
            'reason': 'Splitting into event-driven scripts requires event understanding'
        })

    # Output recommendations
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE3_T01_T12_MISSING_DEPS_FINAL.txt'
    with open(output_file, 'w') as f:
        f.write("# GRADE 3 CROSS-TOPIC DEPENDENCY RECOMMENDATIONS (T01-T12)\n")
        f.write("# FINAL ANALYSIS - Manually verified against actual skill descriptions\n")
        f.write("# Only includes MISSING dependencies that should be ADDED\n\n")

        if recommendations:
            for rec in recommendations:
                f.write(f"{rec['skill_id']}: {rec['skill_name']}\n")
                f.write(f"ADD DEPENDENCY: {rec['dep_id']}: {rec['dep_name']}\n")
                f.write(f"REASON: {rec['reason']}\n\n")
        else:
            f.write("No missing dependencies found.\n")

        f.write(f"\nTotal recommendations: {len(recommendations)}\n")

    print(f"Final analysis complete. Found {len(recommendations)} validated missing dependencies.")
    print(f"Results written to: {output_file}\n")

    # Print to console
    if recommendations:
        print("=== FINAL VALIDATED MISSING DEPENDENCIES ===\n")
        for rec in recommendations:
            print(f"{rec['skill_id']}: {rec['skill_name']}")
            print(f"ADD DEPENDENCY: {rec['dep_id']}: {rec['dep_name']}")
            print(f"REASON: {rec['reason']}\n")

if __name__ == '__main__':
    main()
