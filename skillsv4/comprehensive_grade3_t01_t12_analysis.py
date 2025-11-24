#!/usr/bin/env python3
"""
Comprehensive analysis of ALL Grade 3 skills in T01-T12.
Identifies missing cross-topic dependencies following X-2 rule.
"""

import re

def parse_all_skills(filepath):
    """Parse all skills from allskills.md."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skill_pattern = re.compile(r'^ID: (T\d+\.G\d+\.\d+(?:\.\d+)?)$', re.MULTILINE)
    skills = {}

    parts = skill_pattern.split(content)
    for i in range(1, len(parts), 2):
        skill_id = parts[i]
        skill_content = parts[i+1] if i+1 < len(parts) else ""

        # Extract topic and grade
        topic_match = re.match(r'T(\d+)\.G([KGE0-9]+)\.', skill_id)
        if not topic_match:
            continue

        # Extract skill name
        name_match = re.search(r'^Skill: (.+)$', skill_content, re.MULTILINE)
        skill_name = name_match.group(1) if name_match else ""

        # Extract description
        desc_match = re.search(r'^Description: (.+?)(?=\n\n|\nDependencies:|\nCSTA:|\Z)', skill_content, re.MULTILINE | re.DOTALL)
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

def has_transitive_dependency(skill_id, target_topic, skills, visited=None):
    """Check if skill has direct or transitive dependency on target topic."""
    if visited is None:
        visited = set()

    if skill_id in visited or skill_id not in skills:
        return False
    visited.add(skill_id)

    for dep in skills[skill_id]['dependencies']:
        if dep.startswith(target_topic + '.'):
            return True
        if has_transitive_dependency(dep, target_topic, skills, visited):
            return True

    return False

def analyze_grade3_skills(skills):
    """Analyze Grade 3 skills from T01-T12 for missing dependencies."""
    recommendations = []

    # Extract only Grade 3 skills from T01-T12
    grade3_skills = {sid: data for sid, data in skills.items()
                     if re.match(r'T(0[1-9]|1[0-2])\.G3\.', sid)}

    print(f"Analyzing {len(grade3_skills)} Grade 3 skills from T01-T12...\n")

    for skill_id in sorted(grade3_skills.keys()):
        skill = grade3_skills[skill_id]
        name = skill['name']
        desc = skill['description'].lower()
        deps = skill['dependencies']
        topic = skill_id.split('.')[0]

        missing = []

        # Check 1: Skills using loops should depend on T07
        if not skill_id.startswith('T07.'):
            loop_keywords = ['repeat', 'loop', 'forever', 'iterate', 'for each']
            if any(kw in desc for kw in loop_keywords):
                if not has_transitive_dependency(skill_id, 'T07', skills):
                    # Determine which loop skill to recommend
                    if 'for each' in desc or 'iterate' in desc:
                        dep_id = 'T07.G3.01'
                    elif 'forever' in desc:
                        dep_id = 'T07.G3.01'
                    else:
                        dep_id = 'T07.G3.01'

                    missing.append({
                        'dep_id': dep_id,
                        'dep_name': 'Use a counted repeat loop',
                        'reason': f'Description mentions loops/repeat: "{[kw for kw in loop_keywords if kw in desc]}"'
                    })

        # Check 2: Skills using conditionals should depend on T08
        if not skill_id.startswith('T08.'):
            cond_keywords = ['if ', 'else', 'condition', 'when ', 'decision']
            if any(kw in desc for kw in cond_keywords):
                if not has_transitive_dependency(skill_id, 'T08', skills):
                    missing.append({
                        'dep_id': 'T08.G3.01',
                        'dep_name': 'Use a simple if in a script',
                        'reason': f'Description mentions conditionals: "{[kw for kw in cond_keywords if kw in desc]}"'
                    })

        # Check 3: Skills using variables should depend on T09
        if not skill_id.startswith('T09.'):
            var_keywords = ['variable', 'counter', 'score', 'parameter']
            if any(kw in desc for kw in var_keywords):
                if not has_transitive_dependency(skill_id, 'T09', skills):
                    missing.append({
                        'dep_id': 'T09.G3.01.01',
                        'dep_name': 'Create a variable and set it',
                        'reason': f'Description mentions variables: "{[kw for kw in var_keywords if kw in desc]}"'
                    })

        # Check 4: Skills using events should depend on T06
        if not skill_id.startswith('T06.'):
            event_keywords = ['green flag', 'event', 'broadcast', 'when clicked', 'program start']
            if any(kw in desc for kw in event_keywords):
                if not has_transitive_dependency(skill_id, 'T06', skills):
                    missing.append({
                        'dep_id': 'T06.G3.01',
                        'dep_name': 'Build a green-flag script that runs a 3-5 block sequence',
                        'reason': f'Description mentions events: "{[kw for kw in event_keywords if kw in desc]}"'
                    })

        # Add to recommendations
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

    print("Parsing all skills...")
    all_skills = parse_all_skills(filepath)
    print(f"Found {len(all_skills)} total skills\n")

    recommendations = analyze_grade3_skills(all_skills)

    # Output
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE3_T01_T12_COMPREHENSIVE_ANALYSIS.txt'
    with open(output_file, 'w') as f:
        f.write("# GRADE 3 CROSS-TOPIC DEPENDENCY ANALYSIS (T01-T12)\n")
        f.write("# Comprehensive automated analysis with transitive dependency checking\n\n")

        if recommendations:
            for rec in recommendations:
                f.write(f"{rec['skill_id']}: {rec['skill_name']}\n")
                f.write(f"ADD DEPENDENCY: {rec['dep_id']}: {rec['dep_name']}\n")
                f.write(f"REASON: {rec['reason']}\n\n")
        else:
            f.write("No missing dependencies found.\n")

        f.write(f"\nTotal recommendations: {len(recommendations)}\n")

    print(f"Analysis complete. Found {len(recommendations)} potential missing dependencies.")
    print(f"Results written to: {output_file}\n")

    if recommendations:
        print("=== POTENTIAL MISSING DEPENDENCIES ===\n")
        for rec in recommendations[:20]:  # Show first 20
            print(f"{rec['skill_id']}: {rec['skill_name']}")
            print(f"ADD DEPENDENCY: {rec['dep_id']}: {rec['dep_name']}")
            print(f"REASON: {rec['reason']}\n")
        if len(recommendations) > 20:
            print(f"... and {len(recommendations) - 20} more. See file for complete list.")

if __name__ == '__main__':
    main()
