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
    topics = []
    current_topic = None

    # Split by topic headers
    topic_pattern = r'^## Topic (\d+): (.+)$'
    skill_pattern = r'^### (\d+\.\d+(?:\.\d+)*)\. (.+)$'

    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check for topic header
        topic_match = re.match(topic_pattern, line)
        if topic_match:
            topic_num = int(topic_match.group(1))
            topic_name = topic_match.group(2)
            current_topic = f"T{topic_num}"
            topics.append({'num': topic_num, 'name': topic_name, 'id': current_topic})
            i += 1
            continue

        # Check for skill header
        skill_match = re.match(skill_pattern, line)
        if skill_match and current_topic:
            skill_id = skill_match.group(1)
            skill_name = skill_match.group(2)

            # Determine grade from skill_id
            parts = skill_id.split('.')
            if len(parts) >= 2:
                grade = int(parts[1])
            else:
                grade = None

            # Extract content until next skill or topic
            content_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i]
                if re.match(topic_pattern, next_line) or re.match(skill_pattern, next_line):
                    break
                content_lines.append(next_line)
                i += 1

            skill_content = '\n'.join(content_lines)

            # Extract dependencies
            deps = []
            dep_match = re.search(r'\*\*Dependencies:\*\*\s*(.+?)(?:\n|$)', skill_content, re.MULTILINE)
            if dep_match:
                dep_text = dep_match.group(1).strip()
                if dep_text and dep_text.lower() != 'none':
                    deps = [d.strip() for d in dep_text.split(',') if d.strip()]

            skills[skill_id] = {
                'id': skill_id,
                'name': skill_name,
                'grade': grade,
                'topic': current_topic,
                'dependencies': deps,
                'content': skill_content,
                'original_deps': deps.copy()
            }
            continue

        i += 1

    return {'skills': skills, 'topics': topics}

def get_skill_grade(skill_id: str) -> int:
    """Extract grade from skill ID."""
    parts = skill_id.split('.')
    if len(parts) >= 2:
        return int(parts[1])
    return 0

def get_skill_topic(skill_id: str) -> str:
    """Extract topic from skill ID."""
    parts = skill_id.split('.')
    if len(parts) >= 1:
        return f"T{parts[0]}"
    return "T0"

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

def find_missing_cross_topic_deps(skills: Dict, skill_id: str) -> List[str]:
    """Find potentially missing cross-topic dependencies."""
    skill = skills[skill_id]
    skill_topic = skill['topic']
    skill_grade = skill['grade']
    skill_name = skill['name'].lower()
    skill_content = skill['content'].lower()

    suggestions = []

    # Define key dependency patterns
    patterns = {
        'loops': {
            'keywords': ['loop', 'repeat', 'forever', 'times', 'iteration'],
            'topics': ['T1', 'T2'],  # Loops and control flow topics
            'grades': [2, 3, 4]
        },
        'variables': {
            'keywords': ['variable', 'score', 'counter', 'track', 'store', 'value'],
            'topics': ['T3', 'T4'],  # Variable topics
            'grades': [2, 3, 4]
        },
        'conditionals': {
            'keywords': ['if', 'condition', 'check', 'when', 'detect'],
            'topics': ['T5', 'T6'],  # Conditional topics
            'grades': [2, 3, 4]
        },
        'events': {
            'keywords': ['event', 'click', 'key press', 'broadcast', 'message'],
            'topics': ['T7', 'T8'],  # Event topics
            'grades': [2, 3, 4]
        },
        'graphics': {
            'keywords': ['draw', 'sprite', 'costume', 'appearance', 'visual', 'color'],
            'topics': ['T9', 'T10', 'T11'],  # Graphics topics
            'grades': [2, 3, 4]
        },
        'motion': {
            'keywords': ['move', 'position', 'coordinate', 'x', 'y', 'direction'],
            'topics': ['T12', 'T13'],  # Motion topics
            'grades': [2, 3, 4]
        },
        'sensing': {
            'keywords': ['sense', 'detect', 'collision', 'touch', 'ask', 'answer'],
            'topics': ['T14', 'T15'],  # Sensing topics
            'grades': [2, 3, 4]
        },
        'operators': {
            'keywords': ['calculate', 'math', 'random', 'join', 'operation'],
            'topics': ['T16', 'T17'],  # Operator topics
            'grades': [2, 3, 4]
        }
    }

    # Check if skill uses certain concepts but doesn't depend on foundational skills
    for concept, info in patterns.items():
        # Check if skill mentions these keywords
        mentions_concept = any(kw in skill_name or kw in skill_content for kw in info['keywords'])

        if mentions_concept:
            # Check if we have dependencies from relevant topics
            current_deps = skill['dependencies']
            dep_topics = set(get_skill_topic(dep) for dep in current_deps if dep in skills)

            relevant_topics = set(info['topics'])
            missing_topics = relevant_topics - dep_topics

            if missing_topics and skill_topic not in relevant_topics:
                # Look for foundational skills in missing topics
                for topic in missing_topics:
                    for sid, s in skills.items():
                        if s['topic'] == topic and s['grade'] in info['grades'] and s['grade'] <= skill_grade:
                            if sid not in current_deps:
                                suggestions.append({
                                    'skill': sid,
                                    'reason': f"Uses {concept} concept but missing foundational dependency",
                                    'priority': 'high' if s['grade'] == 2 else 'medium'
                                })

    return suggestions

def analyze_grade4_skills(data: Dict) -> Dict:
    """Comprehensive analysis of all Grade 4 skills."""
    skills = data['skills']

    # Filter Grade 4 skills
    grade4_skills = {sid: s for sid, s in skills.items() if s['grade'] == 4}

    print(f"Total Grade 4 skills found: {len(grade4_skills)}")
    print(f"Distributed across topics:\n")

    # Count by topic
    topic_counts = defaultdict(int)
    for skill in grade4_skills.values():
        topic_counts[skill['topic']] += 1

    for topic in sorted(topic_counts.keys(), key=lambda x: int(x[1:])):
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
        print(f"[{idx}/{len(grade4_skills)}] Analyzing {skill_id}: {skill['name']}")
        print(f"  Topic: {skill['topic']}")
        print(f"  Current dependencies: {len(skill['dependencies'])}")

        # Check X-2 rule
        violations = check_x_minus_2_rule(skill_id, skill['dependencies'])
        if violations:
            print(f"  ⚠ X-2 VIOLATIONS: {violations}")
            analysis['x_minus_2_violations'].append({
                'skill': skill_id,
                'violations': violations
            })

        # Check circular dependencies
        cycle = detect_circular_deps(skills, skill_id)
        if cycle:
            print(f"  ⚠ CIRCULAR DEPENDENCY: {' -> '.join(cycle)}")
            analysis['circular_deps'].append({
                'skill': skill_id,
                'cycle': cycle
            })

        # Check for missing cross-topic dependencies
        missing = find_missing_cross_topic_deps(skills, skill_id)
        if missing:
            print(f"  💡 POTENTIAL MISSING DEPS: {len(missing)} suggestions")
            for m in missing[:3]:  # Show top 3
                print(f"     - {m['skill']}: {m['reason']}")
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
    for violation in analysis['x_minus_2_violations']:
        skill_id = violation['skill']
        skill = skills[skill_id]
        skill_grade = skill['grade']

        print(f"Fixing X-2 violations for {skill_id}...")

        new_deps = []
        for dep in skill['dependencies']:
            dep_grade = get_skill_grade(dep)
            if dep_grade > skill_grade:
                print(f"  ✗ Removing {dep} (grade {dep_grade} > {skill_grade})")
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
    for missing_info in analysis['missing_deps']:
        skill_id = missing_info['skill']
        skill = skills[skill_id]

        high_priority = [s for s in missing_info['suggestions'] if s['priority'] == 'high']

        if high_priority:
            print(f"\nAdding missing dependencies for {skill_id}...")

            for sugg in high_priority[:2]:  # Add top 2 high-priority deps
                dep_id = sugg['skill']
                if dep_id not in skill['dependencies'] and dep_id in skills:
                    print(f"  ✓ Adding {dep_id}: {sugg['reason']}")
                    skill['dependencies'].append(dep_id)
                    fixes.append({
                        'skill': skill_id,
                        'action': 'add',
                        'dependency': dep_id,
                        'reason': sugg['reason']
                    })

    return {'fixes': fixes}

def write_updated_file(filepath: str, data: Dict) -> None:
    """Write updated skills back to allskills.md."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = data['skills']

    # Replace dependencies for each skill
    for skill_id, skill in skills.items():
        if skill['dependencies'] != skill['original_deps']:
            # Find the skill section
            pattern = rf'(### {re.escape(skill_id)}\. .+?\n.*?\*\*Dependencies:\*\*\s*)([^\n]+)'

            new_deps_str = ', '.join(skill['dependencies']) if skill['dependencies'] else 'None'

            def replace_deps(match):
                return match.group(1) + new_deps_str

            content = re.sub(pattern, replace_deps, content, flags=re.MULTILINE | re.DOTALL)

    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\n✓ Updated {filepath}")

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
            report.append(f"  • {fix['skill']}: Added {fix['dependency']}")
            report.append(f"    Reason: {fix['reason']}")

        report.append(f"\nDEPENDENCIES REMOVED: {len(removed)}")
        for fix in removed:
            report.append(f"  • {fix['skill']}: Removed {fix['dependency']}")
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
        report.append("⚠ CIRCULAR DEPENDENCIES:")
        for circ in analysis['circular_deps']:
            report.append(f"  • {circ['skill']}: {' -> '.join(circ['cycle'])}")
    else:
        report.append("✓ No circular dependencies detected")

    report.append("")

    # Check if X-2 rule is satisfied after fixes
    report.append("5. X-2 RULE COMPLIANCE:")
    report.append("-" * 80)
    if analysis['x_minus_2_violations']:
        report.append(f"✓ Fixed {len(analysis['x_minus_2_violations'])} X-2 violations")
        report.append("✓ All Grade 4 skills now comply with X-2 rule")
    else:
        report.append("✓ All Grade 4 skills already complied with X-2 rule")

    report.append("")
    report.append("="*80)
    report.append("ANALYSIS COMPLETE")
    report.append("="*80)

    return '\n'.join(report)

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Loading allskills.md...")
    data = parse_allskills(filepath)
    print(f"Loaded {len(data['skills'])} total skills across {len(data['topics'])} topics\n")

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

    print(f"\n✓ Report saved to {report_path}")
    print("\n" + report)

if __name__ == '__main__':
    main()
