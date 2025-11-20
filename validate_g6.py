#!/usr/bin/env python3
"""
Validate Grade 6 fixes in allskills.md
"""

import re
import json

def extract_grade_6_skills(file_path):
    """Extract all Grade 6 skills from allskills.md"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into skill blocks
    skills = []
    current_skill = {}
    in_skill = False
    in_dependencies = False
    dep_lines = []

    for line in content.split('\n'):
        # Start of a new skill
        if line.startswith('ID:'):
            if current_skill and 'id' in current_skill:
                # Save dependencies from previous skill
                if dep_lines:
                    # Join all dependency lines and clean up
                    deps_text = ' '.join(dep_lines).strip()
                    # Remove bullet points and extra spaces
                    deps_text = deps_text.replace('*', '').strip()
                    current_skill['dependencies'] = deps_text
                skills.append(current_skill)

            skill_id = line.replace('ID:', '').strip()
            current_skill = {'id': skill_id}
            # Extract grade from ID (e.g., T01.G6.01 -> 6)
            match = re.search(r'\.G(\d+|K)\.', skill_id)
            if match:
                grade = match.group(1)
                current_skill['grade'] = grade
            in_skill = True
            in_dependencies = False
            dep_lines = []

        elif in_skill:
            if line.startswith('Dependencies:'):
                in_dependencies = True
                # Check if dependencies are on the same line
                rest = line.replace('Dependencies:', '').strip()
                if rest:
                    if rest.lower() == 'none':
                        current_skill['dependencies'] = 'none'
                        in_dependencies = False
                    else:
                        dep_lines.append(rest)
            elif in_dependencies:
                # Continue collecting dependency lines until we hit a blank line or next section
                stripped = line.strip()
                if stripped and not stripped.startswith('ID:') and not stripped.startswith('Topic:') and not stripped.startswith('Skill:') and not stripped.startswith('Description:'):
                    dep_lines.append(stripped)
                elif stripped == '' or stripped.startswith('ID:') or stripped.startswith('Topic:'):
                    in_dependencies = False

            if line.startswith('Description:'):
                current_skill['description'] = line.replace('Description:', '').strip()
                in_dependencies = False

    # Add last skill
    if current_skill and 'id' in current_skill:
        if dep_lines:
            deps_text = ' '.join(dep_lines).strip()
            deps_text = deps_text.replace('*', '').strip()
            current_skill['dependencies'] = deps_text
        skills.append(current_skill)

    # Filter for Grade 6 only
    g6_skills = [s for s in skills if s.get('grade') == '6']

    return g6_skills

def parse_dependencies(dep_string):
    """Parse dependency string into list of skill IDs"""
    if not dep_string or dep_string.lower() == 'none':
        return []

    # The format is: "T01.GK.01: Description, T01.GK.02: Description"
    # or just: "T01.GK.01, T01.GK.02"
    # We need to extract just the IDs

    deps = []
    # Split by comma or newline
    parts = dep_string.replace('\n', ',').split(',')

    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Extract skill ID pattern (e.g., T01.GK.01, T02.G5.03)
        # Take everything before the first colon (if any)
        if ':' in part:
            skill_id = part.split(':')[0].strip()
        else:
            skill_id = part.strip()

        # Validate it looks like a skill ID
        if re.match(r'T\d+\.G[K\d]+\.\d+', skill_id):
            deps.append(skill_id)

    return deps

def get_grade_from_skill_id(skill_id):
    """Extract grade level from skill ID (e.g., T01.G3.01 -> G3)"""
    match = re.search(r'\.G(\d+|K)\.', skill_id)
    if match:
        grade = match.group(1)
        return 'GK' if grade == 'K' else f'G{grade}'
    return None

def validate_grade_6_skills(g6_skills):
    """Validate Grade 6 skills for dependency issues"""

    issues = {
        'invalid_dependencies': [],  # Dependencies on GK-G3
        'circular_dependencies': [],
        'format_errors': [],
        'missing_dependencies': []
    }

    valid_count = 0
    total_deps_removed = 0

    print(f"\n{'='*80}")
    print(f"GRADE 6 SKILLS VALIDATION REPORT")
    print(f"{'='*80}\n")
    print(f"Total Grade 6 skills found: {len(g6_skills)}\n")

    for skill in g6_skills:
        skill_id = skill.get('id', 'UNKNOWN')
        dep_string = skill.get('dependencies', '')

        # Check for missing dependencies field
        if 'dependencies' not in skill:
            issues['missing_dependencies'].append(skill_id)
            continue

        # Parse dependencies
        deps = parse_dependencies(dep_string)

        # Track issues found for this skill
        skill_has_issues = False

        # Check each dependency
        invalid_deps = []
        for dep in deps:
            dep_grade = get_grade_from_skill_id(dep)
            if dep_grade in ['GK', 'G1', 'G2', 'G3']:
                invalid_deps.append((dep, dep_grade))
                skill_has_issues = True

        if invalid_deps:
            issues['invalid_dependencies'].append({
                'skill_id': skill_id,
                'invalid_deps': invalid_deps,
                'current_deps': dep_string
            })
        else:
            valid_count += 1

    # Print detailed results
    print(f"VALIDATION RESULTS:")
    print(f"  ✓ Valid skills (no GK-G3 dependencies): {valid_count}/{len(g6_skills)}")
    print(f"  ✗ Skills with invalid dependencies: {len(issues['invalid_dependencies'])}")
    print(f"  ✗ Skills with missing dependency field: {len(issues['missing_dependencies'])}")

    # Print invalid dependencies details
    if issues['invalid_dependencies']:
        print(f"\n{'='*80}")
        print(f"REMAINING ISSUES - SKILLS WITH INVALID DEPENDENCIES:")
        print(f"{'='*80}\n")

        for issue in issues['invalid_dependencies']:
            print(f"Skill: {issue['skill_id']}")
            print(f"  Current dependencies: {issue['current_deps']}")
            print(f"  Invalid dependencies found:")
            for dep, grade in issue['invalid_deps']:
                print(f"    - {dep} (grade level: {grade})")
            print()

    # Print missing dependencies
    if issues['missing_dependencies']:
        print(f"\n{'='*80}")
        print(f"SKILLS WITH MISSING DEPENDENCY FIELD:")
        print(f"{'='*80}\n")
        for skill_id in issues['missing_dependencies']:
            print(f"  - {skill_id}")

    return issues, valid_count, len(g6_skills)

def check_downstream_impact(file_path):
    """Check if G7 or G8 skills depend on G6 skills"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract all skills
    all_skills = {}
    current_skill = {}
    in_skill = False
    in_dependencies = False
    dep_lines = []

    for line in content.split('\n'):
        if line.startswith('ID:'):
            if current_skill and 'id' in current_skill:
                if dep_lines:
                    deps_text = ' '.join(dep_lines).strip()
                    deps_text = deps_text.replace('*', '').strip()
                    current_skill['dependencies'] = deps_text
                all_skills[current_skill['id']] = current_skill

            skill_id = line.replace('ID:', '').strip()
            current_skill = {'id': skill_id}
            # Extract grade from ID
            match = re.search(r'\.G(\d+|K)\.', skill_id)
            if match:
                grade = match.group(1)
                current_skill['grade'] = grade
            in_skill = True
            in_dependencies = False
            dep_lines = []

        elif in_skill:
            if line.startswith('Dependencies:'):
                in_dependencies = True
                rest = line.replace('Dependencies:', '').strip()
                if rest:
                    if rest.lower() == 'none':
                        current_skill['dependencies'] = 'none'
                        in_dependencies = False
                    else:
                        dep_lines.append(rest)
            elif in_dependencies:
                stripped = line.strip()
                if stripped and not stripped.startswith('ID:') and not stripped.startswith('Topic:') and not stripped.startswith('Skill:') and not stripped.startswith('Description:'):
                    dep_lines.append(stripped)
                elif stripped == '' or stripped.startswith('ID:') or stripped.startswith('Topic:'):
                    in_dependencies = False

    if current_skill and 'id' in current_skill:
        if dep_lines:
            deps_text = ' '.join(dep_lines).strip()
            deps_text = deps_text.replace('*', '').strip()
            current_skill['dependencies'] = deps_text
        all_skills[current_skill['id']] = current_skill

    # Find G7 and G8 skills that depend on G6
    g7_g8_depending_on_g6 = []

    for skill_id, skill in all_skills.items():
        grade = skill.get('grade')
        if grade in ['7', '8']:
            deps = parse_dependencies(skill.get('dependencies', ''))
            g6_deps = [d for d in deps if get_grade_from_skill_id(d) == 'G6']
            if g6_deps:
                g7_g8_depending_on_g6.append({
                    'skill_id': skill_id,
                    'grade': grade,
                    'g6_dependencies': g6_deps
                })

    print(f"\n{'='*80}")
    print(f"DOWNSTREAM IMPACT ANALYSIS (G7 & G8):")
    print(f"{'='*80}\n")

    if g7_g8_depending_on_g6:
        print(f"Found {len(g7_g8_depending_on_g6)} G7/G8 skills that depend on G6 skills:\n")
        for item in g7_g8_depending_on_g6:
            print(f"  {item['skill_id']} (Grade {item['grade']})")
            print(f"    Depends on G6 skills: {', '.join(item['g6_dependencies'])}")
            print()
        print("RECOMMENDATION: These skills should be reviewed after G6 validation completes.")
    else:
        print("No G7 or G8 skills depend on G6 skills.")

    return g7_g8_depending_on_g6

def generate_summary_stats(g6_skills):
    """Generate statistics about G6 skills"""
    print(f"\n{'='*80}")
    print(f"GRADE 6 DEPENDENCY STATISTICS:")
    print(f"{'='*80}\n")

    dep_counts = {
        'none': 0,
        'g4_only': 0,
        'g5_only': 0,
        'g6_only': 0,
        'g4_g5': 0,
        'g4_g6': 0,
        'g5_g6': 0,
        'g4_g5_g6': 0,
        'has_invalid': 0
    }

    for skill in g6_skills:
        deps = parse_dependencies(skill.get('dependencies', ''))

        if not deps:
            dep_counts['none'] += 1
            continue

        has_g4 = any(get_grade_from_skill_id(d) == 'G4' for d in deps)
        has_g5 = any(get_grade_from_skill_id(d) == 'G5' for d in deps)
        has_g6 = any(get_grade_from_skill_id(d) == 'G6' for d in deps)
        has_invalid = any(get_grade_from_skill_id(d) in ['GK', 'G1', 'G2', 'G3'] for d in deps)

        if has_invalid:
            dep_counts['has_invalid'] += 1
        elif has_g4 and has_g5 and has_g6:
            dep_counts['g4_g5_g6'] += 1
        elif has_g4 and has_g5:
            dep_counts['g4_g5'] += 1
        elif has_g4 and has_g6:
            dep_counts['g4_g6'] += 1
        elif has_g5 and has_g6:
            dep_counts['g5_g6'] += 1
        elif has_g4:
            dep_counts['g4_only'] += 1
        elif has_g5:
            dep_counts['g5_only'] += 1
        elif has_g6:
            dep_counts['g6_only'] += 1

    print(f"Skills with no dependencies: {dep_counts['none']}")
    print(f"Skills with G4 dependencies only: {dep_counts['g4_only']}")
    print(f"Skills with G5 dependencies only: {dep_counts['g5_only']}")
    print(f"Skills with G6 dependencies only: {dep_counts['g6_only']}")
    print(f"Skills with G4 & G5 dependencies: {dep_counts['g4_g5']}")
    print(f"Skills with G4 & G6 dependencies: {dep_counts['g4_g6']}")
    print(f"Skills with G5 & G6 dependencies: {dep_counts['g5_g6']}")
    print(f"Skills with G4, G5 & G6 dependencies: {dep_counts['g4_g5_g6']}")
    print(f"Skills with INVALID dependencies (GK-G3): {dep_counts['has_invalid']}")

def main():
    file_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("\nExtracting Grade 6 skills...")
    g6_skills = extract_grade_6_skills(file_path)

    print("\nValidating dependencies...")
    issues, valid_count, total_count = validate_grade_6_skills(g6_skills)

    # Generate statistics
    generate_summary_stats(g6_skills)

    # Check downstream impact
    downstream = check_downstream_impact(file_path)

    # Final summary
    print(f"\n{'='*80}")
    print(f"FINAL VALIDATION SUMMARY:")
    print(f"{'='*80}\n")

    if valid_count == total_count:
        print("✓ SUCCESS: All Grade 6 skills have valid dependencies!")
        print("✓ No dependencies on GK, G1, G2, or G3 remain.")
        print("✓ All HIGH priority issues have been fixed.")
    else:
        print(f"✗ ISSUES REMAINING: {total_count - valid_count} skills still have invalid dependencies")
        print(f"  These skills need to be reviewed and fixed manually.")

    print(f"\nNext Steps:")
    if valid_count == total_count:
        print("  1. ✓ Grade 6 validation complete")
        if downstream:
            print(f"  2. Review {len(downstream)} G7/G8 skills that depend on G6")
            print("  3. Proceed with Grade 7 validation if needed")
        else:
            print("  2. No downstream impact detected")
            print("  3. Grade 6 fixes are complete!")
    else:
        print("  1. Review and fix remaining Grade 6 issues")
        print("  2. Re-run validation")
        print("  3. Then proceed with G7/G8 review")

    print()

    # Save results
    results = {
        'total_g6_skills': total_count,
        'valid_skills': valid_count,
        'invalid_skills': total_count - valid_count,
        'issues': issues,
        'downstream_impact': downstream
    }

    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G6_VALIDATION_RESULTS.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Detailed results saved to: {output_file}\n")

if __name__ == '__main__':
    main()
