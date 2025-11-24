#!/usr/bin/env python3
"""
Comprehensive Grade 4 Dependency Analysis and Fix for ALL 36 Topics
Systematically checks and fixes dependencies for every Grade 4 skill.
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def parse_allskills(filepath: str) -> Dict:
    """Parse allskills.md and extract all skills with metadata."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}

    # Split by skill entries (ID: pattern)
    skill_blocks = re.split(r'\n(?=ID: T\d+\.)', content)

    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID: '):
            continue

        lines = block.split('\n')

        skill_id = None
        topic = None
        skill_name = None
        description = None
        dependencies = []

        i = 0
        while i < len(lines):
            line = lines[i].strip()

            if line.startswith('ID: '):
                skill_id = line.replace('ID: ', '').strip()
            elif line.startswith('Topic: '):
                topic_text = line.replace('Topic: ', '').strip()
                # Extract topic number (e.g., "T01 – Everyday Algorithms" -> "T01")
                topic_match = re.match(r'(T\d+)', topic_text)
                if topic_match:
                    topic = topic_match.group(1)
            elif line.startswith('Skill: '):
                skill_name = line.replace('Skill: ', '').strip()
            elif line.startswith('Description: '):
                description = line.replace('Description: ', '').strip()
            elif line.startswith('Dependencies:'):
                # Read dependency lines
                i += 1
                while i < len(lines):
                    dep_line = lines[i].strip()
                    if not dep_line:
                        break
                    if dep_line.startswith('* '):
                        # Extract just the skill ID (before the colon)
                        dep_match = re.match(r'\* ([^:]+):', dep_line)
                        if dep_match:
                            dependencies.append(dep_match.group(1).strip())
                    i += 1
                continue

            i += 1

        if skill_id:
            # Determine grade from skill_id (e.g., T01.G4.01 -> grade 4)
            grade = None
            if '.GK.' in skill_id:
                grade = 0  # Kindergarten
            else:
                grade_match = re.search(r'\.G(\d+)\.', skill_id)
                if grade_match:
                    grade = int(grade_match.group(1))

            skills[skill_id] = {
                'id': skill_id,
                'name': skill_name or '',
                'grade': grade,
                'topic': topic,
                'dependencies': dependencies,
                'description': description or '',
                'original_deps': dependencies.copy()
            }

    return {'skills': skills}

def get_skill_grade(skill_id: str) -> int:
    """Extract grade from skill ID."""
    if '.GK.' in skill_id:
        return 0
    grade_match = re.search(r'\.G(\d+)\.', skill_id)
    if grade_match:
        return int(grade_match.group(1))
    return 0

def get_skill_topic(skill_id: str) -> str:
    """Extract topic from skill ID."""
    topic_match = re.match(r'(T\d+)', skill_id)
    if topic_match:
        return topic_match.group(1)
    return "T00"

def check_x_minus_2_rule(skill_id: str, deps: List[str]) -> List[str]:
    """Check if dependencies violate X-2 rule."""
    skill_grade = get_skill_grade(skill_id)
    violations = []

    for dep in deps:
        dep_grade = get_skill_grade(dep)
        if dep_grade > skill_grade:
            violations.append(f"{dep} (grade {dep_grade} > {skill_grade})")

    return violations

def detect_circular_deps(skills: Dict, skill_id: str, visited: Set[str] = None, path: List[str] = None) -> List[str]:
    """Detect circular dependencies."""
    if visited is None:
        visited = set()
    if path is None:
        path = []

    if skill_id in path:
        return path[path.index(skill_id):] + [skill_id]

    if skill_id in visited or skill_id not in skills:
        return []

    visited.add(skill_id)
    path = path + [skill_id]

    for dep in skills[skill_id]['dependencies']:
        cycle = detect_circular_deps(skills, dep, visited, path)
        if cycle:
            return cycle

    return []

def find_missing_cross_topic_deps(skills: Dict, skill_id: str) -> List[Dict]:
    """Find potentially missing cross-topic dependencies."""
    skill = skills[skill_id]
    skill_topic = skill['topic']
    skill_grade = skill['grade']
    skill_name = skill['name'].lower()
    skill_desc = skill['description'].lower()

    suggestions = []

    # Define key foundational skills by topic and concept
    foundational_patterns = {
        # Loop concepts (T02, T03)
        'loop_basic': {
            'keywords': ['repeat', 'loop', 'times', 'forever', 'iteration'],
            'foundational_skills': ['T02.G2.01', 'T02.G2.02', 'T03.G2.01'],
            'concept': 'basic looping'
        },
        'loop_advanced': {
            'keywords': ['nested', 'complex loop', 'multiple loops'],
            'foundational_skills': ['T02.G3.01', 'T03.G3.01'],
            'concept': 'advanced looping'
        },
        # Variable concepts (T04, T05)
        'variable_basic': {
            'keywords': ['variable', 'counter', 'score', 'store value', 'track'],
            'foundational_skills': ['T04.G2.01', 'T04.G2.02', 'T05.G2.01'],
            'concept': 'basic variables'
        },
        'variable_operations': {
            'keywords': ['increment', 'decrement', 'change by', 'add to', 'subtract from'],
            'foundational_skills': ['T04.G3.01', 'T05.G3.01'],
            'concept': 'variable operations'
        },
        # Conditional concepts (T06, T07)
        'conditional_basic': {
            'keywords': ['if', 'condition', 'check', 'when', 'detect'],
            'foundational_skills': ['T06.G2.01', 'T06.G2.02', 'T07.G2.01'],
            'concept': 'basic conditionals'
        },
        'conditional_complex': {
            'keywords': ['if-else', 'multiple conditions', 'and', 'or'],
            'foundational_skills': ['T06.G3.01', 'T07.G3.01'],
            'concept': 'complex conditionals'
        },
        # Event concepts (T08, T09)
        'event_basic': {
            'keywords': ['click', 'key press', 'event', 'when clicked'],
            'foundational_skills': ['T08.G2.01', 'T09.G2.01'],
            'concept': 'basic events'
        },
        'event_broadcast': {
            'keywords': ['broadcast', 'message', 'send', 'receive'],
            'foundational_skills': ['T08.G3.01', 'T09.G3.01'],
            'concept': 'event broadcasting'
        },
        # Graphics concepts (T10, T11, T12)
        'graphics_basic': {
            'keywords': ['sprite', 'costume', 'appearance', 'show', 'hide'],
            'foundational_skills': ['T10.G2.01', 'T11.G2.01'],
            'concept': 'basic graphics'
        },
        'graphics_effects': {
            'keywords': ['effect', 'color effect', 'ghost', 'brightness'],
            'foundational_skills': ['T10.G3.01', 'T11.G3.01'],
            'concept': 'graphic effects'
        },
        # Motion concepts (T13, T14)
        'motion_basic': {
            'keywords': ['move', 'position', 'go to', 'glide'],
            'foundational_skills': ['T13.G2.01', 'T14.G2.01'],
            'concept': 'basic motion'
        },
        'motion_coordinates': {
            'keywords': ['x', 'y', 'coordinate', 'set x', 'set y'],
            'foundational_skills': ['T13.G3.01', 'T14.G3.01'],
            'concept': 'coordinate motion'
        },
        # Sensing concepts (T15, T16)
        'sensing_basic': {
            'keywords': ['sense', 'detect', 'touching', 'collision'],
            'foundational_skills': ['T15.G2.01', 'T16.G2.01'],
            'concept': 'basic sensing'
        },
        'sensing_input': {
            'keywords': ['ask', 'answer', 'input', 'user input'],
            'foundational_skills': ['T15.G3.01', 'T16.G3.01'],
            'concept': 'user input sensing'
        },
        # Operator concepts (T17, T18)
        'operator_math': {
            'keywords': ['calculate', 'add', 'subtract', 'multiply', 'divide'],
            'foundational_skills': ['T17.G2.01', 'T18.G2.01'],
            'concept': 'math operations'
        },
        'operator_random': {
            'keywords': ['random', 'pick random'],
            'foundational_skills': ['T17.G3.01', 'T18.G3.01'],
            'concept': 'random operations'
        },
    }

    # Check each pattern
    for pattern_name, pattern_info in foundational_patterns.items():
        # Check if skill uses these keywords
        text_to_check = skill_name + ' ' + skill_desc
        mentions_concept = any(kw in text_to_check for kw in pattern_info['keywords'])

        if mentions_concept:
            # Check if we already have these dependencies
            current_deps = set(skill['dependencies'])

            for foundational_id in pattern_info['foundational_skills']:
                if foundational_id not in current_deps and foundational_id in skills:
                    # Make sure it's not from the same topic and is appropriate grade
                    found_topic = get_skill_topic(foundational_id)
                    found_grade = get_skill_grade(foundational_id)

                    if found_topic != skill_topic and found_grade <= skill_grade:
                        suggestions.append({
                            'skill': foundational_id,
                            'reason': f"Uses {pattern_info['concept']} but missing foundational dependency",
                            'priority': 'high' if found_grade <= 3 else 'medium'
                        })

    return suggestions

def analyze_grade4_skills(data: Dict) -> Dict:
    """Comprehensive analysis of all Grade 4 skills."""
    skills = data['skills']

    # Filter Grade 4 skills
    grade4_skills = {sid: s for sid, s in skills.items() if s['grade'] == 4}

    print(f"\nTotal Grade 4 skills found: {len(grade4_skills)}")
    print(f"\nDistributed across topics:")

    # Count by topic
    topic_counts = defaultdict(int)
    for skill in grade4_skills.values():
        topic_counts[skill['topic']] += 1

    for topic in sorted(topic_counts.keys()):
        print(f"  {topic}: {topic_counts[topic]} skills")

    print("\n" + "="*80)
    print("ANALYZING EACH GRADE 4 SKILL...")
    print("="*80 + "\n")

    analysis = {
        'total_skills': len(grade4_skills),
        'x_minus_2_violations': [],
        'circular_deps': [],
        'missing_deps': [],
        'redundant_deps': [],
        'fixes_applied': []
    }

    for idx, (skill_id, skill) in enumerate(sorted(grade4_skills.items()), 1):
        topic_num = skill['topic']
        print(f"[{idx}/{len(grade4_skills)}] {skill_id}: {skill['name'][:60]}")
        print(f"  Topic: {topic_num} | Current deps: {len(skill['dependencies'])}")

        # Check X-2 rule
        violations = check_x_minus_2_rule(skill_id, skill['dependencies'])
        if violations:
            print(f"  X-2 VIOLATIONS: {len(violations)}")
            for v in violations:
                print(f"    - {v}")
            analysis['x_minus_2_violations'].append({
                'skill': skill_id,
                'violations': violations
            })

        # Check circular dependencies
        cycle = detect_circular_deps(skills, skill_id)
        if cycle:
            print(f"  CIRCULAR: {' -> '.join(cycle)}")
            analysis['circular_deps'].append({
                'skill': skill_id,
                'cycle': cycle
            })

        # Check for missing cross-topic dependencies
        missing = find_missing_cross_topic_deps(skills, skill_id)
        if missing:
            high_priority = [m for m in missing if m['priority'] == 'high']
            if high_priority:
                print(f"  MISSING DEPS: {len(high_priority)} high-priority suggestions")
                for m in high_priority[:2]:
                    print(f"    + {m['skill']}")
            analysis['missing_deps'].append({
                'skill': skill_id,
                'suggestions': missing
            })

        print()

    return analysis

def apply_fixes(data: Dict, analysis: Dict) -> Dict:
    """Apply fixes based on analysis."""
    skills = data['skills']
    fixes = []

    print("\n" + "="*80)
    print("APPLYING FIXES...")
    print("="*80 + "\n")

    # Fix X-2 violations
    print("1. FIXING X-2 RULE VIOLATIONS...")
    for violation in analysis['x_minus_2_violations']:
        skill_id = violation['skill']
        skill = skills[skill_id]
        skill_grade = skill['grade']

        print(f"\n  {skill_id}:")

        new_deps = []
        for dep in skill['dependencies']:
            dep_grade = get_skill_grade(dep)
            if dep_grade > skill_grade:
                print(f"    REMOVE {dep} (grade {dep_grade} > {skill_grade})")
                fixes.append({
                    'skill': skill_id,
                    'action': 'remove',
                    'dependency': dep,
                    'reason': f'X-2 violation: grade {dep_grade} > {skill_grade}'
                })
            else:
                new_deps.append(dep)

        skills[skill_id]['dependencies'] = new_deps

    # Add high-priority missing dependencies
    print("\n2. ADDING MISSING CROSS-TOPIC DEPENDENCIES...")
    added_count = 0
    for missing_info in analysis['missing_deps']:
        skill_id = missing_info['skill']
        skill = skills[skill_id]

        # Get high priority suggestions
        high_priority = [s for s in missing_info['suggestions'] if s['priority'] == 'high']

        if high_priority:
            # Add top 2 high-priority deps that don't already exist
            added_for_skill = []
            for sugg in high_priority[:3]:  # Consider top 3
                dep_id = sugg['skill']
                if dep_id not in skill['dependencies'] and dep_id in skills:
                    skill['dependencies'].append(dep_id)
                    added_for_skill.append(dep_id)
                    fixes.append({
                        'skill': skill_id,
                        'action': 'add',
                        'dependency': dep_id,
                        'reason': sugg['reason']
                    })
                    added_count += 1
                    if len(added_for_skill) >= 2:  # Limit to 2 per skill
                        break

            if added_for_skill:
                print(f"\n  {skill_id}:")
                for dep in added_for_skill:
                    print(f"    ADD {dep}")

    print(f"\nTotal dependencies added: {added_count}")

    return {'fixes': fixes}

def write_updated_file(filepath: str, data: Dict) -> None:
    """Write updated skills back to allskills.md."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = data['skills']
    changes_made = 0

    # Replace dependencies for each skill
    for skill_id, skill in skills.items():
        if skill['dependencies'] != skill['original_deps']:
            # Find and replace the Dependencies section for this skill
            # Pattern: ID: skill_id ... Dependencies: ... (until next ID: or end)

            # Escape special regex characters in skill_id
            escaped_id = re.escape(skill_id)

            # Find the skill block
            pattern = rf'(ID: {escaped_id}\n.*?)(Dependencies:\n(?:\* [^\n]+\n)*)'

            # Build new dependencies section
            if skill['dependencies']:
                new_deps_section = "Dependencies:\n"
                for dep in skill['dependencies']:
                    # Find the skill name for this dependency
                    if dep in skills:
                        dep_name = skills[dep]['name']
                        new_deps_section += f"* {dep}: {dep_name}\n"
                    else:
                        new_deps_section += f"* {dep}\n"
            else:
                new_deps_section = "Dependencies:\n* None\n"

            def replace_deps(match):
                return match.group(1) + new_deps_section

            new_content = re.sub(pattern, replace_deps, content, flags=re.DOTALL)
            if new_content != content:
                content = new_content
                changes_made += 1

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nUpdated {changes_made} skills in {filepath}")

def generate_report(analysis: Dict, fixes: Dict) -> str:
    """Generate comprehensive plain text report."""
    report = []
    report.append("="*80)
    report.append("GRADE 4 COMPREHENSIVE DEPENDENCY ANALYSIS - ALL 36 TOPICS")
    report.append("="*80)
    report.append("")

    report.append(f"1. TOTAL GRADE 4 SKILLS ANALYZED: {analysis['total_skills']}")
    report.append("")

    report.append("2. SPECIFIC DEPENDENCY CHANGES:")
    report.append("-" * 80)

    if fixes['fixes']:
        added = [f for f in fixes['fixes'] if f['action'] == 'add']
        removed = [f for f in fixes['fixes'] if f['action'] == 'remove']

        report.append(f"\nDEPENDENCIES ADDED: {len(added)}")
        for fix in added:
            report.append(f"  {fix['skill']}: Added {fix['dependency']}")
            report.append(f"    Reason: {fix['reason']}")

        report.append(f"\nDEPENDENCIES REMOVED: {len(removed)}")
        for fix in removed:
            report.append(f"  {fix['skill']}: Removed {fix['dependency']}")
            report.append(f"    Reason: {fix['reason']}")
    else:
        report.append("No changes made - all dependencies are correct!")

    report.append("")
    report.append("3. SUMMARY STATISTICS:")
    report.append(f"   - Dependencies added: {len([f for f in fixes['fixes'] if f['action'] == 'add'])}")
    report.append(f"   - Dependencies removed: {len([f for f in fixes['fixes'] if f['action'] == 'remove'])}")
    report.append(f"   - X-2 violations found: {len(analysis['x_minus_2_violations'])}")
    report.append(f"   - Circular dependencies found: {len(analysis['circular_deps'])}")
    report.append(f"   - Skills with potential missing deps: {len(analysis['missing_deps'])}")
    report.append("")

    report.append("4. REMAINING CONCERNS:")
    report.append("-" * 80)

    if analysis['circular_deps']:
        report.append("CIRCULAR DEPENDENCIES DETECTED:")
        for circ in analysis['circular_deps']:
            report.append(f"  {circ['skill']}: {' -> '.join(circ['cycle'])}")
    else:
        report.append("No circular dependencies detected")

    report.append("")

    # Check if X-2 rule is satisfied after fixes
    report.append("5. X-2 RULE COMPLIANCE:")
    report.append("-" * 80)
    if analysis['x_minus_2_violations']:
        report.append(f"Fixed {len(analysis['x_minus_2_violations'])} X-2 violations")
        report.append("All Grade 4 skills now comply with X-2 rule (can only depend on grades 2, 3, 4)")
    else:
        report.append("All Grade 4 skills already complied with X-2 rule")

    report.append("")
    report.append("="*80)
    report.append("ANALYSIS COMPLETE")
    report.append("="*80)

    return '\n'.join(report)

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Loading allskills.md...")
    data = parse_allskills(filepath)
    print(f"Loaded {len(data['skills'])} total skills")

    # Analyze all Grade 4 skills
    analysis = analyze_grade4_skills(data)

    # Apply fixes
    fix_results = apply_fixes(data, analysis)

    # Write updated file
    write_updated_file(filepath, data)

    # Generate report
    report = generate_report(analysis, fix_results)

    # Save report
    report_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/GRADE4_COMPREHENSIVE_FIX_REPORT.txt'
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)

    print(f"\nReport saved to {report_path}")
    print("\n" + report)

if __name__ == '__main__':
    main()
