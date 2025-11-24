#!/usr/bin/env python3
"""
Analyze Grade 4 skills for missing cross-topic dependencies
"""

import json
import re
from collections import defaultdict

def load_skills(filepath):
    """Load skills from JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # Extract skills array from the data structure
        if isinstance(data, dict) and 'skills' in data:
            return data['skills']
        return data

def extract_grade_from_skill_id(skill_id):
    """Extract grade from skill ID like T01.G4.01"""
    match = re.search(r'\.G(\d+|K)\.', skill_id)
    if match:
        grade = match.group(1)
        return 0 if grade == 'K' else int(grade)
    return None

def check_x2_violations(skill_id, deps):
    """Check if any dependencies violate X-2 rule for Grade 4"""
    violations = []
    skill_grade = extract_grade_from_skill_id(skill_id)

    if skill_grade != 4:
        return violations

    for dep in deps:
        dep_grade = extract_grade_from_skill_id(dep)
        if dep_grade is not None:
            # Grade 4 can only depend on grades 2, 3, and 4
            if dep_grade < 2 or dep_grade > 4:
                violations.append({
                    'skill': skill_id,
                    'invalid_dep': dep,
                    'dep_grade': dep_grade,
                    'reason': f'Grade 4 cannot depend on Grade {dep_grade} (X-2 rule)'
                })

    return violations

def analyze_missing_dependencies(skills):
    """Analyze skills for missing cross-topic dependencies"""

    missing_deps = []
    x2_violations = []
    dep_frequency = defaultdict(int)

    # Define keyword patterns and their suggested dependencies
    patterns = {
        'variable': {
            'keywords': ['variable', 'set variable', 'value', 'counter', 'score', 'timer', 'store'],
            'suggested_deps': ['T04.G2.01', 'T04.G2.02'],  # Create variable, Display variable
            'reason': 'Uses variables'
        },
        'loop': {
            'keywords': ['loop', 'repeat', 'iterate', ' times', 'forever', 'until'],
            'suggested_deps': ['T02.G2.01', 'T02.G2.02'],  # Basic repeat, Loop with count
            'reason': 'Uses loops'
        },
        'conditional': {
            'keywords': [' if ', 'condition', 'check', 'when ', 'else'],
            'suggested_deps': ['T06.G2.01', 'T06.G2.02'],  # Basic if, If-else
            'reason': 'Uses conditionals'
        },
        'boolean': {
            'keywords': ['boolean', 'true', 'false', ' and ', ' or ', ' not '],
            'suggested_deps': ['T07.G2.01'],  # AND/OR operators
            'reason': 'Uses boolean logic'
        },
        'nested_condition': {
            'keywords': ['nested condition', 'nested if', 'multiple condition'],
            'suggested_deps': ['T06.G3.01'],  # Nested conditionals
            'reason': 'Uses nested conditionals'
        },
        'nested_loop': {
            'keywords': ['nested loop', 'loop within', 'double loop'],
            'suggested_deps': ['T07.G3.01'],  # Nested loops
            'reason': 'Uses nested loops'
        },
        'random': {
            'keywords': ['random', 'pick random'],
            'suggested_deps': ['T04.G3.02'],  # Random values
            'reason': 'Uses random values'
        },
        'list': {
            'keywords': ['list', 'array', ' item ', 'collection', 'add to list', 'delete from list'],
            'suggested_deps': ['T05.G3.01', 'T05.G3.02'],  # List basics
            'reason': 'Uses lists'
        },
        'broadcast': {
            'keywords': ['broadcast', 'message', 'event', 'signal'],
            'suggested_deps': ['T06.G3.01'],  # Events/broadcast
            'reason': 'Uses broadcast messages'
        },
        'function': {
            'keywords': ['function', 'procedure', 'custom block', 'define'],
            'suggested_deps': ['T03.G2.01', 'T03.G2.02'],  # Function basics
            'reason': 'Uses functions/custom blocks'
        },
        'clone': {
            'keywords': ['clone', 'create clone', 'spawn'],
            'suggested_deps': ['T08.G3.01'],  # Clone basics
            'reason': 'Uses clones'
        },
        'coordinate': {
            'keywords': ['coordinate', 'position', ' x ', ' y ', 'goto', 'move to'],
            'suggested_deps': ['T01.G2.01'],  # Motion/coordinate basics
            'reason': 'Uses coordinates'
        },
        'debug': {
            'keywords': ['debug', 'trace', 'test', 'error'],
            'suggested_deps': ['T13.G3.01'],  # Debugging
            'reason': 'Uses debugging techniques'
        },
        'operator': {
            'keywords': ['operator', 'arithmetic', 'calculate', 'math', 'add', 'subtract', 'multiply', 'divide'],
            'suggested_deps': ['T04.G2.03'],  # Arithmetic operators
            'reason': 'Uses arithmetic operators'
        },
        'comparison': {
            'keywords': ['compare', 'greater', 'less', 'equal', '>', '<', '='],
            'suggested_deps': ['T06.G2.03'],  # Comparison operators
            'reason': 'Uses comparison operators'
        }
    }

    # Analyze each skill
    for skill in skills:
        skill_id = skill.get('id', '')
        description = skill.get('description', '').lower()
        deps_raw = skill.get('dependencies', [])

        # Extract dependency IDs (handle both string format and object format)
        current_deps = []
        for dep in deps_raw:
            if isinstance(dep, str):
                current_deps.append(dep)
            elif isinstance(dep, dict) and 'id' in dep:
                current_deps.append(dep['id'])
            else:
                current_deps.append(str(dep))

        # Check X-2 violations
        violations = check_x2_violations(skill_id, current_deps)
        x2_violations.extend(violations)

        # Check for missing dependencies based on patterns
        for pattern_name, pattern_info in patterns.items():
            keywords = pattern_info['keywords']
            suggested_deps = pattern_info['suggested_deps']
            reason = pattern_info['reason']

            # Check if any keyword matches
            has_keyword = any(keyword in description for keyword in keywords)

            if has_keyword:
                # Check if any of the suggested deps are already present
                has_dep = any(dep in current_deps for dep in suggested_deps)

                if not has_dep:
                    # Found missing dependency
                    for suggested_dep in suggested_deps:
                        missing_deps.append({
                            'skill': skill_id,
                            'missing_dep': suggested_dep,
                            'reason': reason,
                            'description_excerpt': description[:100]
                        })
                        dep_frequency[suggested_dep] += 1

    return missing_deps, x2_violations, dep_frequency

def generate_report(missing_deps, x2_violations, dep_frequency, output_file):
    """Generate analysis report"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("GRADE 4 CROSS-TOPIC DEPENDENCY ANALYSIS\n")
        f.write("=" * 80 + "\n\n")

        # Summary statistics
        f.write("SUMMARY STATISTICS\n")
        f.write("-" * 80 + "\n")
        f.write(f"Total missing dependencies found: {len(missing_deps)}\n")
        f.write(f"Total X-2 violations found: {len(x2_violations)}\n")
        f.write(f"Unique skills with missing deps: {len(set(d['skill'] for d in missing_deps))}\n")
        f.write("\n")

        # Most common missing dependencies
        f.write("MOST COMMON MISSING DEPENDENCIES\n")
        f.write("-" * 80 + "\n")
        sorted_deps = sorted(dep_frequency.items(), key=lambda x: x[1], reverse=True)
        for dep, count in sorted_deps[:15]:
            f.write(f"{dep}: {count} skills\n")
        f.write("\n")

        # X-2 violations
        if x2_violations:
            f.write("\n")
            f.write("=" * 80 + "\n")
            f.write("X-2 RULE VIOLATIONS\n")
            f.write("=" * 80 + "\n\n")

            for violation in x2_violations:
                f.write(f"SKILL: {violation['skill']}\n")
                f.write(f"  Invalid dependency: {violation['invalid_dep']} (Grade {violation['dep_grade']})\n")
                f.write(f"  Reason: {violation['reason']}\n")
                f.write("\n")

        # Missing dependencies detail
        f.write("\n")
        f.write("=" * 80 + "\n")
        f.write("MISSING DEPENDENCIES (DETAILED)\n")
        f.write("=" * 80 + "\n\n")

        # Group by skill
        by_skill = defaultdict(list)
        for item in missing_deps:
            by_skill[item['skill']].append(item)

        for skill, items in sorted(by_skill.items()):
            f.write(f"\nSKILL: {skill}\n")
            for item in items:
                f.write(f"  NEEDS: {item['missing_dep']} - {item['reason']}\n")
            f.write(f"  Description excerpt: {items[0]['description_excerpt']}...\n")

        # List format for easy application
        f.write("\n\n")
        f.write("=" * 80 + "\n")
        f.write("DEPENDENCIES TO ADD (READY-TO-APPLY FORMAT)\n")
        f.write("=" * 80 + "\n\n")

        for skill, items in sorted(by_skill.items()):
            unique_deps = list(set(item['missing_dep'] for item in items))
            for dep in sorted(unique_deps):
                f.write(f"{skill} needs {dep}\n")

def main():
    input_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade4_skills_extracted.json'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE4_MISSING_DEPS_ANALYSIS.txt'

    print("Loading Grade 4 skills...")
    skills = load_skills(input_file)
    print(f"Loaded {len(skills)} skills")

    print("Analyzing missing dependencies...")
    missing_deps, x2_violations, dep_frequency = analyze_missing_dependencies(skills)

    print(f"Found {len(missing_deps)} missing dependencies")
    print(f"Found {len(x2_violations)} X-2 violations")

    print("Generating report...")
    generate_report(missing_deps, x2_violations, dep_frequency, output_file)

    print(f"Report saved to: {output_file}")
    print("\nTop 10 most common missing dependencies:")
    sorted_deps = sorted(dep_frequency.items(), key=lambda x: x[1], reverse=True)
    for dep, count in sorted_deps[:10]:
        print(f"  {dep}: {count} skills")

if __name__ == '__main__':
    main()
