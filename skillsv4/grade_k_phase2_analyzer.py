#!/usr/bin/env python3
"""
Grade K Phase 2 Cross-Topic Dependency Analysis
Analyzes all Grade K skills for dependency issues
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def parse_skills_file(filepath: str) -> Dict[str, dict]:
    """Parse allskills.md and extract all Grade K skills with their dependencies."""
    skills = {}
    current_skill = None
    current_section = None

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Check for skill ID (Grade K only)
        if line.startswith('ID:'):
            skill_id = line.split(':', 1)[1].strip()
            if '.GK.' in skill_id:
                current_skill = skill_id
                skills[skill_id] = {
                    'id': skill_id,
                    'topic': '',
                    'skill': '',
                    'description': '',
                    'dependencies': []
                }
                current_section = 'id'

        # Parse topic
        elif line.startswith('Topic:') and current_skill:
            skills[current_skill]['topic'] = line.split(':', 1)[1].strip()
            current_section = 'topic'

        # Parse skill name
        elif line.startswith('Skill:') and current_skill:
            skills[current_skill]['skill'] = line.split(':', 1)[1].strip()
            current_section = 'skill'

        # Parse description
        elif line.startswith('Description:') and current_skill:
            skills[current_skill]['description'] = line.split(':', 1)[1].strip()
            current_section = 'description'

        # Parse dependencies
        elif line.startswith('Dependencies:') and current_skill:
            current_section = 'dependencies'
            # Read dependency lines
            j = i + 1
            while j < len(lines):
                dep_line = lines[j].strip()
                if dep_line.startswith('*'):
                    # Extract dependency ID
                    match = re.search(r'(T\d+\.[A-Z0-9]+\.\d+)', dep_line)
                    if match:
                        skills[current_skill]['dependencies'].append(match.group(1))
                elif dep_line.startswith('ID:') or (dep_line and not dep_line.startswith('*')):
                    break
                j += 1
            i = j - 1

        i += 1

    return skills

def extract_topic_number(skill_id: str) -> str:
    """Extract topic number from skill ID (e.g., T01.GK.01 -> T01)"""
    match = re.match(r'(T\d+)', skill_id)
    return match.group(1) if match else ''

def extract_grade(skill_id: str) -> str:
    """Extract grade from skill ID (e.g., T01.GK.01 -> GK)"""
    match = re.search(r'\.([A-Z0-9]+)\.', skill_id)
    return match.group(1) if match else ''

def find_cross_topic_issues(skills: Dict[str, dict]) -> Dict[str, List]:
    """Find missing cross-topic dependencies and other issues."""
    issues = {
        'missing_cross_topic': [],
        'grade_violations': [],
        'circular_dependencies': [],
        'redundant_dependencies': [],
        'missing_foundational': []
    }

    # Group skills by topic
    skills_by_topic = defaultdict(list)
    for skill_id, skill_data in skills.items():
        topic = extract_topic_number(skill_id)
        skills_by_topic[topic].append(skill_id)

    # Check each skill
    for skill_id, skill_data in skills.items():
        skill_topic = extract_topic_number(skill_id)
        skill_name = skill_data['skill'].lower()
        skill_desc = skill_data['description'].lower()
        deps = skill_data['dependencies']

        # Check for grade violations (X-2 rule)
        for dep_id in deps:
            dep_grade = extract_grade(dep_id)
            if dep_grade != 'GK':
                issues['grade_violations'].append({
                    'skill': skill_id,
                    'dependency': dep_id,
                    'reason': f'Grade K skill depends on {dep_grade} skill'
                })

        # Check for circular dependencies
        for dep_id in deps:
            if dep_id in skills:
                if skill_id in skills[dep_id]['dependencies']:
                    issues['circular_dependencies'].append({
                        'skill1': skill_id,
                        'skill2': dep_id,
                        'reason': 'Direct circular dependency'
                    })

        # Check for redundant dependencies (transitive)
        if len(deps) > 1:
            redundant = []
            for dep_id in deps:
                if dep_id in skills:
                    # Check if this dep is also a dependency of another direct dep
                    for other_dep in deps:
                        if other_dep != dep_id and other_dep in skills:
                            if dep_id in get_all_transitive_deps(other_dep, skills):
                                redundant.append({
                                    'skill': skill_id,
                                    'redundant_dep': dep_id,
                                    'via': other_dep,
                                    'reason': f'{dep_id} is transitively included via {other_dep}'
                                })
            if redundant:
                issues['redundant_dependencies'].extend(redundant)

        # Look for missing cross-topic dependencies
        # Check for common patterns that suggest cross-topic dependencies

        # Pattern recognition skills should depend on T04 (Patterns)
        if skill_topic != 'T04' and any(kw in skill_name or kw in skill_desc for kw in
            ['pattern', 'repeat', 'sequence', 'color pattern', 'shape pattern']):
            # Check if has T04 dependency
            has_t04_dep = any(extract_topic_number(d) == 'T04' for d in deps)
            if not has_t04_dep:
                issues['missing_cross_topic'].append({
                    'skill': skill_id,
                    'suggested_topic': 'T04',
                    'reason': 'Skill involves patterns but has no T04 dependency',
                    'keywords': 'pattern/repeat/sequence'
                })

        # Counting skills should depend on T09 (Data & Numbers)
        if skill_topic != 'T09' and any(kw in skill_name or kw in skill_desc for kw in
            ['count', 'number', 'how many', 'more', 'less', 'most', 'least', 'tally']):
            has_t09_dep = any(extract_topic_number(d) == 'T09' for d in deps)
            if not has_t09_dep:
                issues['missing_cross_topic'].append({
                    'skill': skill_id,
                    'suggested_topic': 'T09',
                    'reason': 'Skill involves counting/numbers but has no T09 dependency',
                    'keywords': 'count/number/quantity'
                })

        # Sorting/ordering skills should depend on T09
        if skill_topic != 'T09' and any(kw in skill_name or kw in skill_desc for kw in
            ['sort', 'order', 'arrange', 'organize by', 'group by']):
            has_t09_dep = any(extract_topic_number(d) == 'T09' for d in deps)
            if not has_t09_dep:
                issues['missing_cross_topic'].append({
                    'skill': skill_id,
                    'suggested_topic': 'T09',
                    'reason': 'Skill involves sorting/ordering but has no T09 dependency',
                    'keywords': 'sort/order/arrange'
                })

        # Drawing/art skills should depend on T05 (Drawing)
        if skill_topic != 'T05' and any(kw in skill_name or kw in skill_desc for kw in
            ['draw', 'line', 'shape', 'circle', 'square', 'triangle', 'rectangle']):
            has_t05_dep = any(extract_topic_number(d) == 'T05' for d in deps)
            if not has_t05_dep:
                issues['missing_cross_topic'].append({
                    'skill': skill_id,
                    'suggested_topic': 'T05',
                    'reason': 'Skill involves drawing/shapes but has no T05 dependency',
                    'keywords': 'draw/line/shape'
                })

        # Event/trigger skills should depend on T06 (Events)
        if skill_topic != 'T06' and any(kw in skill_name or kw in skill_desc for kw in
            ['when', 'click', 'touch', 'tap', 'press', 'start', 'trigger', 'event']):
            has_t06_dep = any(extract_topic_number(d) == 'T06' for d in deps)
            if not has_t06_dep:
                issues['missing_cross_topic'].append({
                    'skill': skill_id,
                    'suggested_topic': 'T06',
                    'reason': 'Skill involves events/triggers but has no T06 dependency',
                    'keywords': 'when/click/touch/trigger'
                })

        # Animation/motion skills should depend on T02 (Motion & Movement)
        if skill_topic != 'T02' and any(kw in skill_name or kw in skill_desc for kw in
            ['move', 'walk', 'run', 'jump', 'fly', 'glide', 'slide', 'step', 'forward', 'backward']):
            has_t02_dep = any(extract_topic_number(d) == 'T02' for d in deps)
            if not has_t02_dep:
                issues['missing_cross_topic'].append({
                    'skill': skill_id,
                    'suggested_topic': 'T02',
                    'reason': 'Skill involves motion/movement but has no T02 dependency',
                    'keywords': 'move/walk/jump/motion'
                })

        # Direction/position skills should depend on T02
        if skill_topic != 'T02' and any(kw in skill_name or kw in skill_desc for kw in
            ['direction', 'left', 'right', 'up', 'down', 'position', 'location']):
            has_t02_dep = any(extract_topic_number(d) == 'T02' for d in deps)
            if not has_t02_dep:
                issues['missing_cross_topic'].append({
                    'skill': skill_id,
                    'suggested_topic': 'T02',
                    'reason': 'Skill involves direction/position but has no T02 dependency',
                    'keywords': 'direction/position/location'
                })

        # Sound/music skills should depend on T03 (Sound & Music)
        if skill_topic != 'T03' and any(kw in skill_name or kw in skill_desc for kw in
            ['sound', 'music', 'play', 'note', 'beat', 'instrument', 'song', 'melody']):
            has_t03_dep = any(extract_topic_number(d) == 'T03' for d in deps)
            if not has_t03_dep:
                issues['missing_cross_topic'].append({
                    'skill': skill_id,
                    'suggested_topic': 'T03',
                    'reason': 'Skill involves sound/music but has no T03 dependency',
                    'keywords': 'sound/music/play'
                })

        # Check for missing foundational skills
        # Complex skills (many actions) should have basic dependencies
        action_count = sum(1 for w in ['move', 'turn', 'draw', 'play', 'count', 'sort']
                          if w in skill_desc)
        if action_count >= 2 and len(deps) == 0:
            issues['missing_foundational'].append({
                'skill': skill_id,
                'reason': 'Complex skill with multiple actions but no dependencies',
                'action_count': action_count
            })

    return issues

def get_all_transitive_deps(skill_id: str, skills: Dict[str, dict], visited: Set[str] = None) -> Set[str]:
    """Get all transitive dependencies of a skill."""
    if visited is None:
        visited = set()

    if skill_id in visited or skill_id not in skills:
        return visited

    visited.add(skill_id)

    for dep_id in skills[skill_id]['dependencies']:
        get_all_transitive_deps(dep_id, skills, visited)

    return visited

def generate_report(skills: Dict[str, dict], issues: Dict[str, List], output_file: str):
    """Generate comprehensive analysis report."""

    # Count skills by topic
    skills_by_topic = defaultdict(int)
    for skill_id in skills:
        topic = extract_topic_number(skill_id)
        skills_by_topic[topic] += 1

    # Generate report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Grade K Phase 2: Cross-Topic Dependency Analysis\n\n")
        f.write("## Executive Summary\n\n")
        f.write(f"**Total Grade K Skills Analyzed:** {len(skills)}\n\n")

        # Summary of issues
        f.write("### Issues Found:\n\n")
        f.write(f"- **Missing Cross-Topic Dependencies:** {len(issues['missing_cross_topic'])}\n")
        f.write(f"- **Grade Violation Issues (X-2 rule):** {len(issues['grade_violations'])}\n")
        f.write(f"- **Circular Dependencies:** {len(issues['circular_dependencies'])}\n")
        f.write(f"- **Redundant Dependencies:** {len(issues['redundant_dependencies'])}\n")
        f.write(f"- **Missing Foundational Skills:** {len(issues['missing_foundational'])}\n\n")

        # Skills by topic
        f.write("## Grade K Skills by Topic\n\n")
        for topic in sorted(skills_by_topic.keys()):
            f.write(f"- **{topic}:** {skills_by_topic[topic]} skills\n")
        f.write("\n")

        # Detailed issues
        f.write("## Detailed Analysis\n\n")

        # Missing cross-topic dependencies
        f.write("### 1. Missing Cross-Topic Dependencies\n\n")
        if issues['missing_cross_topic']:
            f.write(f"Found {len(issues['missing_cross_topic'])} skills that should have cross-topic dependencies:\n\n")

            # Group by suggested topic
            by_topic = defaultdict(list)
            for issue in issues['missing_cross_topic']:
                by_topic[issue['suggested_topic']].append(issue)

            for suggested_topic in sorted(by_topic.keys()):
                f.write(f"#### Skills needing {suggested_topic} dependencies:\n\n")
                for issue in by_topic[suggested_topic]:
                    skill_id = issue['skill']
                    skill_data = skills[skill_id]
                    f.write(f"**{skill_id}:** {skill_data['skill']}\n")
                    f.write(f"- Reason: {issue['reason']}\n")
                    f.write(f"- Keywords found: {issue['keywords']}\n")
                    f.write(f"- Current dependencies: {len(skill_data['dependencies'])}\n")
                    if skill_data['dependencies']:
                        for dep in skill_data['dependencies']:
                            f.write(f"  - {dep}\n")
                    f.write("\n")
        else:
            f.write("No missing cross-topic dependencies found.\n\n")

        # Grade violations
        f.write("### 2. Grade Violation Issues (X-2 Rule)\n\n")
        if issues['grade_violations']:
            f.write(f"Found {len(issues['grade_violations'])} violations where Grade K skills depend on non-Grade K skills:\n\n")
            for issue in issues['grade_violations']:
                skill_id = issue['skill']
                skill_data = skills[skill_id]
                f.write(f"**{skill_id}:** {skill_data['skill']}\n")
                f.write(f"- Invalid dependency: {issue['dependency']}\n")
                f.write(f"- Reason: {issue['reason']}\n")
                f.write("- **ACTION REQUIRED:** Remove this dependency or replace with Grade K equivalent\n\n")
        else:
            f.write("No grade violations found. All Grade K skills correctly depend only on Grade K skills.\n\n")

        # Circular dependencies
        f.write("### 3. Circular Dependencies\n\n")
        if issues['circular_dependencies']:
            f.write(f"Found {len(issues['circular_dependencies'])} circular dependency pairs:\n\n")
            seen_pairs = set()
            for issue in issues['circular_dependencies']:
                pair = tuple(sorted([issue['skill1'], issue['skill2']]))
                if pair not in seen_pairs:
                    seen_pairs.add(pair)
                    f.write(f"**{issue['skill1']}** ⟷ **{issue['skill2']}**\n")
                    f.write(f"- {skills[issue['skill1']]['skill']}\n")
                    f.write(f"- {skills[issue['skill2']]['skill']}\n")
                    f.write("- **ACTION REQUIRED:** Break the circular dependency\n\n")
        else:
            f.write("No circular dependencies found.\n\n")

        # Redundant dependencies
        f.write("### 4. Potentially Redundant Dependencies\n\n")
        if issues['redundant_dependencies']:
            f.write(f"Found {len(issues['redundant_dependencies'])} potentially redundant dependencies:\n\n")
            f.write("**NOTE:** Be conservative - only remove if genuinely redundant and doesn't add semantic clarity.\n\n")
            for issue in issues['redundant_dependencies']:
                skill_id = issue['skill']
                skill_data = skills[skill_id]
                f.write(f"**{skill_id}:** {skill_data['skill']}\n")
                f.write(f"- Potentially redundant: {issue['redundant_dep']}\n")
                f.write(f"- Already included via: {issue['via']}\n")
                f.write(f"- Reason: {issue['reason']}\n")
                f.write("- **REVIEW REQUIRED:** Check if this adds semantic value\n\n")
        else:
            f.write("No redundant dependencies found.\n\n")

        # Missing foundational skills
        f.write("### 5. Missing Foundational Skills\n\n")
        if issues['missing_foundational']:
            f.write(f"Found {len(issues['missing_foundational'])} complex skills without dependencies:\n\n")
            for issue in issues['missing_foundational']:
                skill_id = issue['skill']
                skill_data = skills[skill_id]
                f.write(f"**{skill_id}:** {skill_data['skill']}\n")
                f.write(f"- Reason: {issue['reason']}\n")
                f.write(f"- Action count: {issue['action_count']}\n")
                f.write("- **ACTION REQUIRED:** Add appropriate foundational dependencies\n\n")
        else:
            f.write("No skills missing foundational dependencies.\n\n")

        # Recommendations summary
        f.write("## Recommended Actions\n\n")
        f.write("### High Priority (Must Fix):\n\n")
        if issues['grade_violations']:
            f.write(f"1. Fix {len(issues['grade_violations'])} grade violations (X-2 rule)\n")
        if issues['circular_dependencies']:
            f.write(f"2. Break {len(issues['circular_dependencies'])} circular dependencies\n")
        if issues['missing_foundational']:
            f.write(f"3. Add foundational dependencies to {len(issues['missing_foundational'])} complex skills\n")

        f.write("\n### Medium Priority (Should Add):\n\n")
        if issues['missing_cross_topic']:
            f.write(f"1. Add {len(issues['missing_cross_topic'])} missing cross-topic dependencies\n")

        f.write("\n### Low Priority (Review):\n\n")
        if issues['redundant_dependencies']:
            f.write(f"1. Review {len(issues['redundant_dependencies'])} potentially redundant dependencies\n")

        f.write("\n## Next Steps\n\n")
        f.write("1. Review each identified issue\n")
        f.write("2. Apply necessary dependency additions (cross-topic)\n")
        f.write("3. Remove invalid dependencies (grade violations)\n")
        f.write("4. Break circular dependencies\n")
        f.write("5. Review and selectively remove truly redundant dependencies\n")
        f.write("6. Re-run analysis to verify fixes\n")

def main():
    input_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade_k_phase2_analysis.md'

    print("Phase 2: Cross-Topic Dependency Analysis for Grade K")
    print("=" * 60)

    # Parse skills
    print("\nStep 1: Parsing Grade K skills...")
    skills = parse_skills_file(input_file)
    print(f"Found {len(skills)} Grade K skills")

    # Analyze for issues
    print("\nStep 2: Analyzing cross-topic dependencies and issues...")
    issues = find_cross_topic_issues(skills)

    print(f"\nIssues found:")
    print(f"  - Missing cross-topic dependencies: {len(issues['missing_cross_topic'])}")
    print(f"  - Grade violations: {len(issues['grade_violations'])}")
    print(f"  - Circular dependencies: {len(issues['circular_dependencies'])}")
    print(f"  - Redundant dependencies: {len(issues['redundant_dependencies'])}")
    print(f"  - Missing foundational: {len(issues['missing_foundational'])}")

    # Generate report
    print("\nStep 3: Generating detailed report...")
    generate_report(skills, issues, output_file)
    print(f"\nReport saved to: {output_file}")

    print("\n" + "=" * 60)
    print("Analysis complete!")

if __name__ == "__main__":
    main()
