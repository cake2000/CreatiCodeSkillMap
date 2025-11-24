#!/usr/bin/env python3
"""
Refined analysis of Grade 3 cross-topic dependencies for Topics T01-T12.
Carefully identifies MISSING dependencies with manual verification.
"""

import re
from collections import defaultdict

def parse_skills(filepath):
    """Parse the allskills.md file and extract Grade 3 skills from T01-T12."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by skill entries
    skill_pattern = re.compile(r'^ID: (T\d+\.G\d+\.\d+(?:\.\d+)?)$', re.MULTILINE)
    skills = {}

    parts = skill_pattern.split(content)
    for i in range(1, len(parts), 2):
        skill_id = parts[i]
        skill_content = parts[i+1] if i+1 < len(parts) else ""

        # Only process Grade 3 skills from topics T01-T12
        if not re.match(r'T(0[1-9]|1[0-2])\.G3\.', skill_id):
            continue

        # Extract skill name
        name_match = re.search(r'^Skill: (.+)$', skill_content, re.MULTILINE)
        skill_name = name_match.group(1) if name_match else ""

        # Extract description
        desc_match = re.search(r'^Description: (.+?)(?=\n\n|\nDependencies:|\Z)', skill_content, re.MULTILINE | re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

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
            'description': description,
            'dependencies': deps
        }

    return skills

def analyze_missing_dependencies(skills):
    """Carefully analyze skills and identify genuinely missing cross-topic dependencies."""
    recommendations = []

    for skill_id, skill_data in sorted(skills.items()):
        name = skill_data['name']
        desc = skill_data['description'].lower()
        deps = skill_data['dependencies']
        topic = skill_id.split('.')[0]

        missing = []

        # T01.G3.03: Identify repeated blocks - about recognizing patterns that COULD use loops
        if skill_id == 'T01.G3.03':
            # This is preparatory to loops, not using them. Current deps look OK.
            pass

        # T01.G3.04: Predict how many times repeated blocks run - counting explicit repetitions
        elif skill_id == 'T01.G3.04':
            # This is about counting repeated blocks, not loops yet. Current deps OK.
            pass

        # T01.G3.12: "possibly with a loop" suggests it might trace loops
        elif skill_id == 'T01.G3.12':
            if 'loop' in desc:
                has_loop_dep = any(dep.startswith('T07.') for dep in deps)
                if not has_loop_dep:
                    missing.append({
                        'dep_id': 'T07.G3.02',
                        'dep_name': 'Trace a script with a simple loop',
                        'reason': 'Skill traces scripts that may include loops'
                    })

        # T01.G3.16: Comparing loop types - should understand conditionals for "checking if key pressed"
        elif skill_id == 'T01.G3.16':
            # The description mentions "checking if a key is pressed" - this involves conditionals
            has_conditional_dep = any(dep.startswith('T08.') for dep in deps)
            if not has_conditional_dep:
                missing.append({
                    'dep_id': 'T08.G3.01',
                    'dep_name': 'Use a simple if in a script',
                    'reason': 'Skill discusses checking conditions (key pressed) within loops'
                })

        # T02 skills - analyzing block sequences
        # T02.G3.03, 04, 05, 06 all mention "if/else" or "decision"
        elif skill_id in ['T02.G3.03', 'T02.G3.04', 'T02.G3.05', 'T02.G3.06']:
            if 'if' in desc or 'decision' in desc:
                has_conditional_dep = any(dep.startswith('T08.') for dep in deps)
                if not has_conditional_dep:
                    missing.append({
                        'dep_id': 'T08.G3.01',
                        'dep_name': 'Use a simple if in a script',
                        'reason': 'Skill works with if/else decisions'
                    })

        # T03 skills - decomposition
        # Most T03.G3 skills are conceptual and might not need specific code dependencies
        # Skip overly general conditional suggestions for abstract analysis skills

        # T04.G3.04.02: Custom blocks might use parameters (like variables)
        elif skill_id == 'T04.G3.04.02':
            if 'parameter' in desc or 'input' in desc:
                has_var_dep = any(dep.startswith('T09.') for dep in deps)
                if not has_var_dep:
                    missing.append({
                        'dep_id': 'T09.G3.01.01',
                        'dep_name': 'Create a variable and set it',
                        'reason': 'Custom blocks with parameters build on variable concepts'
                    })

        # T04.G3.08: Matching algorithm descriptions to code patterns
        elif skill_id == 'T04.G3.08':
            # Mentions variables and conditions
            if 'variable' in desc or 'counter' in desc:
                has_var_dep = any(dep.startswith('T09.') for dep in deps)
                if not has_var_dep:
                    missing.append({
                        'dep_id': 'T09.G3.01.01',
                        'dep_name': 'Create a variable and set it',
                        'reason': 'Skill involves recognizing code patterns with variables'
                    })

        # T06 skills - already event-focused, skip most
        # T08.G3.01: Simple if - should depend on events to run
        elif skill_id == 'T08.G3.01':
            has_event_dep = any(dep.startswith('T06.') for dep in deps)
            if not has_event_dep:
                missing.append({
                    'dep_id': 'T06.G3.01',
                    'dep_name': 'Build a green-flag script that runs a 3-5 block sequence',
                    'reason': 'Conditionals need event context to execute'
                })

        # T08.G3.05: Fix comparison operator - likely involves variables
        elif skill_id == 'T08.G3.05':
            has_var_dep = any(dep.startswith('T09.') for dep in deps)
            if not has_var_dep:
                missing.append({
                    'dep_id': 'T09.G3.01.01',
                    'dep_name': 'Create a variable and set it',
                    'reason': 'Comparison operators typically compare variables'
                })

        # T09 variable skills
        # T09.G3.01.02: Set at program start - needs events
        elif skill_id == 'T09.G3.01.02':
            has_event_dep = any(dep.startswith('T06.') for dep in deps)
            if not has_event_dep:
                missing.append({
                    'dep_id': 'T06.G3.01',
                    'dep_name': 'Build a green-flag script that runs a 3-5 block sequence',
                    'reason': 'Setting initial values happens on program start (event)'
                })

        # T09.G3.01.03: Change variable - might use events
        elif skill_id == 'T09.G3.01.03':
            has_event_dep = any(dep.startswith('T06.') for dep in deps)
            if not has_event_dep:
                missing.append({
                    'dep_id': 'T06.G3.01',
                    'dep_name': 'Build a green-flag script that runs a 3-5 block sequence',
                    'reason': 'Variable changes occur in event-triggered scripts'
                })

        # T10 List skills
        # T10.G3.01.02: Add item - might iterate
        elif skill_id == 'T10.G3.01.02':
            # Adding single item doesn't require loop, skip
            pass

        # T10.G3.04.02: Clear all items - might iterate internally but not user-visible
        elif skill_id == 'T10.G3.04.02':
            # Clearing is a single operation, skip loop dep
            pass

        # T10.G3.05: Loop through each item - PRIMARY loop use case for lists
        elif skill_id == 'T10.G3.05':
            has_loop_dep = any(dep.startswith('T07.') for dep in deps)
            if not has_loop_dep:
                missing.append({
                    'dep_id': 'T07.G3.01',
                    'dep_name': 'Use a counted repeat loop',
                    'reason': 'Looping through list items requires understanding of loops'
                })

        # T10.G3.07: Count items matching condition - uses loops AND conditionals
        elif skill_id == 'T10.G3.07':
            has_loop_dep = any(dep.startswith('T07.') for dep in deps)
            has_cond_dep = any(dep.startswith('T08.') for dep in deps)
            if not has_loop_dep:
                missing.append({
                    'dep_id': 'T07.G3.01',
                    'dep_name': 'Use a counted repeat loop',
                    'reason': 'Counting items requires iterating through the list'
                })
            if not has_cond_dep:
                missing.append({
                    'dep_id': 'T08.G3.01',
                    'dep_name': 'Use a simple if in a script',
                    'reason': 'Matching condition requires conditional logic'
                })

        # T10.G3.10: Display list monitor
        elif skill_id == 'T10.G3.10':
            # Displaying is straightforward, likely doesn't need variable dep
            pass

        # T11 Custom blocks
        # T11.G3.01: Custom blocks vs loops - needs to understand both
        elif skill_id == 'T11.G3.01':
            # Already has loop deps, likely OK
            pass

        # T12 Readability/Comments
        # T12.G3.01: Add comment - if it's about commenting specific constructs
        elif skill_id == 'T12.G3.01':
            # Comments are general, don't force specific construct dependencies
            pass

        # T12.G3.03.01: Clear variable names
        elif skill_id == 'T12.G3.03.01':
            has_var_dep = any(dep.startswith('T09.') for dep in deps)
            if not has_var_dep:
                missing.append({
                    'dep_id': 'T09.G3.01.01',
                    'dep_name': 'Create a variable and set it',
                    'reason': 'Naming variables requires understanding of variables'
                })

        # T12.G3.03.03: Split into event-driven scripts
        elif skill_id == 'T12.G3.03.03':
            has_event_dep = any(dep.startswith('T06.') for dep in deps)
            if not has_event_dep:
                missing.append({
                    'dep_id': 'T06.G3.01',
                    'dep_name': 'Build a green-flag script that runs a 3-5 block sequence',
                    'reason': 'Splitting into event-driven scripts requires event understanding'
                })

        # Add recommendations
        for m in missing:
            recommendations.append({
                'skill_id': skill_id,
                'skill_name': name,
                'dep_id': m['dep_id'],
                'dep_name': m['dep_name'],
                'reason': m['reason']
            })

    return recommendations

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing Grade 3 skills from Topics T01-T12...")
    skills = parse_skills(filepath)
    print(f"Found {len(skills)} Grade 3 skills\n")

    print("Performing refined analysis for missing cross-topic dependencies...")
    recommendations = analyze_missing_dependencies(skills)

    # Output recommendations
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade3_t01_t12_refined_deps.txt'
    with open(output_file, 'w') as f:
        f.write("# GRADE 3 CROSS-TOPIC DEPENDENCY RECOMMENDATIONS (T01-T12) - REFINED\n")
        f.write("# Missing dependencies that should be ADDED\n")
        f.write("# Manually verified based on skill descriptions\n\n")

        if recommendations:
            for rec in recommendations:
                f.write(f"{rec['skill_id']}: {rec['skill_name']}\n")
                f.write(f"ADD DEPENDENCY: {rec['dep_id']}: {rec['dep_name']}\n")
                f.write(f"REASON: {rec['reason']}\n\n")
        else:
            f.write("No missing dependencies found.\n")

        f.write(f"\nTotal recommendations: {len(recommendations)}\n")

    print(f"Refined analysis complete. Found {len(recommendations)} validated missing dependencies.")
    print(f"Results written to: {output_file}")

    # Also print to console
    if recommendations:
        print("\n=== VALIDATED MISSING DEPENDENCIES ===\n")
        for rec in recommendations:
            print(f"{rec['skill_id']}: {rec['skill_name']}")
            print(f"ADD DEPENDENCY: {rec['dep_id']}: {rec['dep_name']}")
            print(f"REASON: {rec['reason']}\n")

if __name__ == '__main__':
    main()
