#!/usr/bin/env python3
"""
Analyze Grade 3 cross-topic dependencies for Topics T01-T12.
Identifies MISSING dependencies that should be added.
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
    """Analyze skills and identify missing cross-topic dependencies."""
    recommendations = []

    # Define key concept skills that others should depend on
    loop_skills = ['T07.G3.01', 'T07.G3.02', 'T07.G2.01', 'T07.G2.02', 'T07.G1.01']
    conditional_skills = ['T08.G3.01', 'T08.G2.01', 'T08.G2.02', 'T08.G1.01']
    variable_skills = ['T09.G3.01.01', 'T09.G3.01.02', 'T09.G2.01', 'T09.G2.02']
    event_skills = ['T06.G3.01', 'T06.G2.01', 'T06.G1.01']

    for skill_id, skill_data in sorted(skills.items()):
        name = skill_data['name']
        desc = skill_data['description'].lower()
        deps = skill_data['dependencies']
        topic = skill_id.split('.')[0]

        missing = []

        # Check for loop usage
        if any(keyword in desc for keyword in ['repeat', 'loop', 'forever', 'iterate']):
            has_loop_dep = any(dep.startswith('T07.') or dep.startswith('T04.G3') for dep in deps)
            if not has_loop_dep:
                # Check if it's not already a T07 skill
                if not skill_id.startswith('T07.'):
                    missing.append({
                        'dep_id': 'T07.G3.01',
                        'dep_name': 'Use a counted repeat loop',
                        'reason': 'Skill uses loops/repeat but lacks T07 loop dependency'
                    })

        # Check for conditional usage
        if any(keyword in desc for keyword in ['if', 'when', 'condition', 'touching', 'check']):
            has_conditional_dep = any(dep.startswith('T08.') for dep in deps)
            if not has_conditional_dep:
                # Check if it's not already a T08 skill
                if not skill_id.startswith('T08.'):
                    # More specific checks
                    if 'if' in desc or 'condition' in desc or 'check if' in desc:
                        missing.append({
                            'dep_id': 'T08.G3.01',
                            'dep_name': 'Use a simple if in a script',
                            'reason': 'Skill uses conditionals/if statements but lacks T08 conditional dependency'
                        })

        # Check for variable usage
        if any(keyword in desc for keyword in ['variable', 'score', 'counter', 'store', 'track']):
            has_variable_dep = any(dep.startswith('T09.') for dep in deps)
            if not has_variable_dep:
                # Check if it's not already a T09 skill
                if not skill_id.startswith('T09.'):
                    missing.append({
                        'dep_id': 'T09.G3.01.01',
                        'dep_name': 'Create a variable and set it',
                        'reason': 'Skill uses variables but lacks T09 variable dependency'
                    })

        # Check for event usage
        if any(keyword in desc for keyword in ['green flag', 'event', 'trigger', 'when clicked', 'broadcast']):
            has_event_dep = any(dep.startswith('T06.') for dep in deps)
            if not has_event_dep:
                # Check if it's not already a T06 skill
                if not skill_id.startswith('T06.'):
                    if 'green flag' in desc or 'event' in desc or 'broadcast' in desc:
                        missing.append({
                            'dep_id': 'T06.G3.01',
                            'dep_name': 'Build a green-flag script that runs a 3-5 block sequence',
                            'reason': 'Skill uses events but lacks T06 event dependency'
                        })

        # Topic-specific checks
        # T10 (Lists) should often depend on loops
        if skill_id.startswith('T10.'):
            if any(keyword in desc for keyword in ['each', 'all items', 'iterate', 'every']):
                has_loop_dep = any(dep.startswith('T07.') for dep in deps)
                if not has_loop_dep:
                    missing.append({
                        'dep_id': 'T07.G3.01',
                        'dep_name': 'Use a counted repeat loop',
                        'reason': 'List skill iterates over items but lacks loop dependency'
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

    print("Analyzing for missing cross-topic dependencies...")
    recommendations = analyze_missing_dependencies(skills)

    # Output recommendations
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade3_t01_t12_missing_deps.txt'
    with open(output_file, 'w') as f:
        f.write("# GRADE 3 CROSS-TOPIC DEPENDENCY RECOMMENDATIONS (T01-T12)\n")
        f.write("# Missing dependencies that should be ADDED\n\n")

        if recommendations:
            for rec in recommendations:
                f.write(f"{rec['skill_id']}: {rec['skill_name']}\n")
                f.write(f"ADD DEPENDENCY: {rec['dep_id']}: {rec['dep_name']}\n")
                f.write(f"REASON: {rec['reason']}\n\n")
        else:
            f.write("No missing dependencies found.\n")

        f.write(f"\nTotal recommendations: {len(recommendations)}\n")

    print(f"Analysis complete. Found {len(recommendations)} missing dependencies.")
    print(f"Results written to: {output_file}")

    # Also print to console
    if recommendations:
        print("\n=== MISSING DEPENDENCIES ===\n")
        for rec in recommendations:
            print(f"{rec['skill_id']}: {rec['skill_name']}")
            print(f"ADD DEPENDENCY: {rec['dep_id']}: {rec['dep_name']}")
            print(f"REASON: {rec['reason']}\n")

if __name__ == '__main__':
    main()
