#!/usr/bin/env python3
"""
Grade K Phase 2 Cross-Topic Dependency Analysis (IMPROVED)
Focuses on DIRECT dependencies only for clearer analysis
"""

import re
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def parse_skills_file(filepath: str) -> Dict[str, dict]:
    """Parse allskills.md and extract all Grade K skills with their DIRECT dependencies."""
    skills = {}
    current_skill = None

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

        # Parse topic
        elif line.startswith('Topic:') and current_skill:
            skills[current_skill]['topic'] = line.split(':', 1)[1].strip()

        # Parse skill name
        elif line.startswith('Skill:') and current_skill:
            skills[current_skill]['skill'] = line.split(':', 1)[1].strip()

        # Parse description
        elif line.startswith('Description:') and current_skill:
            skills[current_skill]['description'] = line.split(':', 1)[1].strip()

        # Parse dependencies
        elif line.startswith('Dependencies:') and current_skill:
            # Read dependency lines
            j = i + 1
            while j < len(lines):
                dep_line = lines[j].strip()
                if dep_line.startswith('*'):
                    # Extract dependency ID
                    match = re.search(r'(T\d+\.[A-Z0-9]+\.\d+)', dep_line)
                    if match:
                        skills[current_skill]['dependencies'].append(match.group(1))
                elif dep_line.startswith('ID:'):
                    # Hit next skill
                    break
                elif dep_line == '':
                    # Empty line - dependencies section might be continuing or ending
                    # Check if next non-empty line is a dependency or new section
                    k = j + 1
                    while k < len(lines) and lines[k].strip() == '':
                        k += 1
                    if k < len(lines):
                        next_line = lines[k].strip()
                        if not next_line.startswith('*'):
                            # Not a dependency, end here
                            break
                    # Otherwise continue (blank lines within dependencies)
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

def analyze_dependencies(skills: Dict[str, dict]) -> Dict[str, List]:
    """Analyze dependencies for issues - DIRECT dependencies only."""
    issues = {
        'grade_violations': [],
        'circular_dependencies': [],
        'redundant_dependencies': [],
        'missing_cross_topic': [],
        'missing_foundational': []
    }

    # Group skills by topic
    skills_by_topic = defaultdict(list)
    for skill_id in skills:
        topic = extract_topic_number(skill_id)
        skills_by_topic[topic].append(skill_id)

    # Check each skill
    for skill_id, skill_data in skills.items():
        skill_topic = extract_topic_number(skill_id)
        skill_name = skill_data['skill'].lower()
        skill_desc = skill_data['description'].lower()
        deps = skill_data['dependencies']

        # 1. Check for DIRECT grade violations (X-2 rule)
        for dep_id in deps:
            dep_grade = extract_grade(dep_id)
            if dep_grade != 'GK':
                issues['grade_violations'].append({
                    'skill': skill_id,
                    'skill_name': skill_data['skill'],
                    'dependency': dep_id,
                    'dep_grade': dep_grade,
                    'reason': f'Grade K skill depends on {dep_grade} skill (X-2 violation)'
                })

        # 2. Check for circular dependencies
        for dep_id in deps:
            if dep_id in skills:
                if skill_id in skills[dep_id]['dependencies']:
                    # Avoid duplicate pairs
                    pair_key = tuple(sorted([skill_id, dep_id]))
                    if not any(tuple(sorted([d['skill1'], d['skill2']])) == pair_key
                             for d in issues['circular_dependencies']):
                        issues['circular_dependencies'].append({
                            'skill1': skill_id,
                            'skill1_name': skill_data['skill'],
                            'skill2': dep_id,
                            'skill2_name': skills[dep_id]['skill']
                        })

        # 3. Check for redundant dependencies (transitive)
        if len(deps) > 1:
            for i, dep_id in enumerate(deps):
                if dep_id in skills:
                    for j, other_dep in enumerate(deps):
                        if i != j and other_dep in skills:
                            # Check if dep_id is in other_dep's transitive closure
                            if is_transitive_dep(dep_id, other_dep, skills):
                                issues['redundant_dependencies'].append({
                                    'skill': skill_id,
                                    'skill_name': skill_data['skill'],
                                    'redundant_dep': dep_id,
                                    'via': other_dep,
                                    'reason': f'{dep_id} is transitively included via {other_dep}'
                                })

        # 4. Look for missing cross-topic dependencies
        cross_topic_suggestions = get_cross_topic_suggestions(
            skill_id, skill_name, skill_desc, skill_topic, deps, skills_by_topic
        )
        issues['missing_cross_topic'].extend(cross_topic_suggestions)

        # 5. Check for missing foundational skills
        if is_complex_skill(skill_name, skill_desc) and len(deps) == 0:
            issues['missing_foundational'].append({
                'skill': skill_id,
                'skill_name': skill_data['skill'],
                'reason': 'Complex skill with no dependencies'
            })

    return issues

def is_transitive_dep(target: str, start: str, skills: Dict, visited: Set = None) -> bool:
    """Check if target is a transitive dependency of start."""
    if visited is None:
        visited = set()

    if start in visited or start not in skills:
        return False

    visited.add(start)

    for dep in skills[start]['dependencies']:
        if dep == target:
            return True
        if is_transitive_dep(target, dep, skills, visited):
            return True

    return False

def get_cross_topic_suggestions(skill_id, skill_name, skill_desc, skill_topic, deps, skills_by_topic):
    """Generate cross-topic dependency suggestions."""
    suggestions = []

    # Pattern recognition → T04
    if skill_topic != 'T04' and 'T04' in skills_by_topic:
        if any(kw in skill_name or kw in skill_desc for kw in
               ['pattern', 'repeat', 'sequence', 'color pattern', 'shape pattern', 'over and over']):
            has_t04 = any(extract_topic_number(d) == 'T04' for d in deps)
            if not has_t04:
                suggestions.append({
                    'skill': skill_id,
                    'suggested_topic': 'T04',
                    'reason': 'Involves patterns/repetition',
                    'keywords': ['pattern', 'repeat', 'sequence']
                })

    # Counting/numbers → T09
    if skill_topic != 'T09' and 'T09' in skills_by_topic:
        if any(kw in skill_name or kw in skill_desc for kw in
               ['count', 'number', 'how many', 'more', 'less', 'most', 'least', 'tally', 'score']):
            has_t09 = any(extract_topic_number(d) == 'T09' for d in deps)
            if not has_t09:
                suggestions.append({
                    'skill': skill_id,
                    'suggested_topic': 'T09',
                    'reason': 'Involves counting/numbers',
                    'keywords': ['count', 'number', 'quantity']
                })

    # Sorting/ordering → T09
    if skill_topic != 'T09' and 'T09' in skills_by_topic:
        if any(kw in skill_name or kw in skill_desc for kw in
               ['sort', 'order by', 'arrange', 'organize by', 'group by']):
            has_t09 = any(extract_topic_number(d) == 'T09' for d in deps)
            if not has_t09:
                suggestions.append({
                    'skill': skill_id,
                    'suggested_topic': 'T09',
                    'reason': 'Involves sorting/ordering',
                    'keywords': ['sort', 'order', 'arrange']
                })

    # Drawing/shapes → T05
    if skill_topic != 'T05' and 'T05' in skills_by_topic:
        if any(kw in skill_name or kw in skill_desc for kw in
               ['draw', 'line', 'shape', 'circle', 'square', 'triangle', 'rectangle', 'pen']):
            has_t05 = any(extract_topic_number(d) == 'T05' for d in deps)
            if not has_t05:
                suggestions.append({
                    'skill': skill_id,
                    'suggested_topic': 'T05',
                    'reason': 'Involves drawing/shapes',
                    'keywords': ['draw', 'line', 'shape']
                })

    # Events/triggers → T06
    if skill_topic != 'T06' and 'T06' in skills_by_topic:
        if any(kw in skill_name or kw in skill_desc for kw in
               ['when clicked', 'when touch', 'when tap', 'when press', 'when start', 'trigger', 'event']):
            has_t06 = any(extract_topic_number(d) == 'T06' for d in deps)
            if not has_t06:
                suggestions.append({
                    'skill': skill_id,
                    'suggested_topic': 'T06',
                    'reason': 'Involves events/triggers',
                    'keywords': ['when', 'click', 'touch', 'trigger']
                })

    # Motion/movement → T02
    if skill_topic != 'T02' and 'T02' in skills_by_topic:
        if any(kw in skill_name or kw in skill_desc for kw in
               ['move sprite', 'walk', 'run', 'jump', 'fly', 'glide', 'slide', 'step']):
            has_t02 = any(extract_topic_number(d) == 'T02' for d in deps)
            if not has_t02:
                suggestions.append({
                    'skill': skill_id,
                    'suggested_topic': 'T02',
                    'reason': 'Involves motion/movement',
                    'keywords': ['move', 'walk', 'jump']
                })

    # Sound/music → T03
    if skill_topic != 'T03' and 'T03' in skills_by_topic:
        if any(kw in skill_name or kw in skill_desc for kw in
               ['sound', 'music', 'play sound', 'note', 'beat', 'instrument', 'song', 'melody']):
            has_t03 = any(extract_topic_number(d) == 'T03' for d in deps)
            if not has_t03:
                suggestions.append({
                    'skill': skill_id,
                    'suggested_topic': 'T03',
                    'reason': 'Involves sound/music',
                    'keywords': ['sound', 'music', 'play']
                })

    return suggestions

def is_complex_skill(skill_name, skill_desc):
    """Determine if skill is complex enough to need dependencies."""
    action_words = ['move', 'turn', 'draw', 'play', 'count', 'sort', 'create', 'build', 'combine']
    action_count = sum(1 for w in action_words if w in skill_desc.lower())
    return action_count >= 2 or len(skill_desc) > 200

def generate_report(skills: Dict[str, dict], issues: Dict[str, List], output_file: str):
    """Generate comprehensive analysis report."""

    # Count skills by topic
    skills_by_topic = defaultdict(int)
    for skill_id in skills:
        topic = extract_topic_number(skill_id)
        skills_by_topic[topic] += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Grade K Phase 2: Cross-Topic Dependency Analysis\n\n")
        f.write("## Executive Summary\n\n")
        f.write(f"**Total Grade K Skills Analyzed:** {len(skills)}\n\n")

        # Summary of issues (unique counts)
        unique_violations = len(set((i['skill'], i['dependency']) for i in issues['grade_violations']))
        unique_circular = len(issues['circular_dependencies'])
        unique_redundant = len(set((i['skill'], i['redundant_dep']) for i in issues['redundant_dependencies']))
        unique_cross_topic = len(issues['missing_cross_topic'])
        unique_foundational = len(issues['missing_foundational'])

        f.write("### Issues Found (DIRECT Dependencies Only):\n\n")
        f.write(f"- **Missing Cross-Topic Dependencies:** {unique_cross_topic}\n")
        f.write(f"- **Grade Violation Issues (X-2 rule):** {unique_violations}\n")
        f.write(f"- **Circular Dependencies:** {unique_circular}\n")
        f.write(f"- **Potentially Redundant Dependencies:** {unique_redundant}\n")
        f.write(f"- **Missing Foundational Skills:** {unique_foundational}\n\n")

        # Skills by topic
        f.write("## Grade K Skills by Topic\n\n")
        for topic in sorted(skills_by_topic.keys()):
            f.write(f"- **{topic}:** {skills_by_topic[topic]} skills\n")
        f.write("\n")

        # === CRITICAL ISSUES ===
        f.write("## CRITICAL ISSUES (Must Fix)\n\n")

        # Grade violations
        f.write("### 1. Grade Violations (X-2 Rule)\n\n")
        if issues['grade_violations']:
            f.write(f"**{unique_violations} Grade K skills have direct dependencies on non-Grade K skills.**\n\n")
            f.write("This violates the X-2 rule: Grade K can ONLY depend on Grade K.\n\n")

            # Group by skill
            by_skill = defaultdict(list)
            for issue in issues['grade_violations']:
                by_skill[issue['skill']].append(issue)

            for skill_id in sorted(by_skill.keys()):
                skill_issues = by_skill[skill_id]
                f.write(f"**{skill_id}:** {skill_issues[0]['skill_name']}\n")
                f.write(f"Invalid dependencies ({len(skill_issues)}):\n")
                for issue in skill_issues:
                    f.write(f"  - {issue['dependency']} (Grade {issue['dep_grade']})\n")
                f.write("**ACTION:** Remove these dependencies or replace with Grade K equivalents\n\n")
        else:
            f.write("✓ No grade violations found.\n\n")

        # Circular dependencies
        f.write("### 2. Circular Dependencies\n\n")
        if issues['circular_dependencies']:
            f.write(f"**{unique_circular} circular dependency pairs found.**\n\n")
            for issue in issues['circular_dependencies']:
                f.write(f"**{issue['skill1']}** ⟷ **{issue['skill2']}**\n")
                f.write(f"- {issue['skill1_name']}\n")
                f.write(f"- {issue['skill2_name']}\n")
                f.write("**ACTION:** Break the circular dependency by removing one direction\n\n")
        else:
            f.write("✓ No circular dependencies found.\n\n")

        # === RECOMMENDED ADDITIONS ===
        f.write("## RECOMMENDED ADDITIONS (Cross-Topic Dependencies)\n\n")

        if issues['missing_cross_topic']:
            f.write(f"**{unique_cross_topic} skills should have cross-topic dependencies.**\n\n")

            # Group by suggested topic
            by_topic = defaultdict(list)
            for issue in issues['missing_cross_topic']:
                by_topic[issue['suggested_topic']].append(issue)

            for suggested_topic in sorted(by_topic.keys()):
                topic_issues = by_topic[suggested_topic]
                f.write(f"### Skills needing {suggested_topic} dependencies ({len(topic_issues)} skills):\n\n")
                for issue in topic_issues:
                    skill_data = skills[issue['skill']]
                    f.write(f"**{issue['skill']}:** {skill_data['skill']}\n")
                    f.write(f"- Reason: {issue['reason']}\n")
                    f.write(f"- Suggested: Add foundational {suggested_topic}.GK.XX dependency\n\n")
        else:
            f.write("✓ No missing cross-topic dependencies identified.\n\n")

        # === OPTIONAL REVIEWS ===
        f.write("## OPTIONAL REVIEWS\n\n")

        # Redundant dependencies
        f.write("### Potentially Redundant Dependencies\n\n")
        if issues['redundant_dependencies']:
            f.write(f"**{unique_redundant} potentially redundant dependencies found.**\n\n")
            f.write("**NOTE:** Only remove if genuinely redundant and doesn't add semantic clarity.\n\n")

            seen = set()
            for issue in issues['redundant_dependencies']:
                key = (issue['skill'], issue['redundant_dep'])
                if key not in seen:
                    seen.add(key)
                    f.write(f"**{issue['skill']}:** {issue['skill_name']}\n")
                    f.write(f"- Potentially redundant: {issue['redundant_dep']}\n")
                    f.write(f"- Already via: {issue['via']}\n")
                    f.write("**REVIEW:** Check if adds semantic value\n\n")
        else:
            f.write("✓ No redundant dependencies found.\n\n")

        # Missing foundational
        f.write("### Missing Foundational Skills\n\n")
        if issues['missing_foundational']:
            f.write(f"**{unique_foundational} complex skills without dependencies.**\n\n")
            for issue in issues['missing_foundational']:
                f.write(f"**{issue['skill']}:** {issue['skill_name']}\n")
                f.write(f"- Reason: {issue['reason']}\n")
                f.write("**REVIEW:** Consider adding foundational dependencies\n\n")
        else:
            f.write("✓ No complex skills missing foundational dependencies.\n\n")

        # === SUMMARY ===
        f.write("## Action Summary\n\n")
        f.write("### Must Fix:\n")
        if unique_violations > 0:
            f.write(f"- [ ] Fix {unique_violations} grade violations\n")
        if unique_circular > 0:
            f.write(f"- [ ] Break {unique_circular} circular dependencies\n")

        f.write("\n### Should Add:\n")
        if unique_cross_topic > 0:
            f.write(f"- [ ] Add {unique_cross_topic} cross-topic dependencies\n")

        f.write("\n### Optional Review:\n")
        if unique_redundant > 0:
            f.write(f"- [ ] Review {unique_redundant} potentially redundant dependencies\n")
        if unique_foundational > 0:
            f.write(f"- [ ] Review {unique_foundational} complex skills for foundational deps\n")

def main():
    input_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade_k_phase2_analysis.md'

    print("=" * 70)
    print("Grade K Phase 2: Cross-Topic Dependency Analysis")
    print("=" * 70)

    # Parse skills
    print("\n[1/3] Parsing Grade K skills...")
    skills = parse_skills_file(input_file)
    print(f"      Found {len(skills)} Grade K skills")

    # Analyze issues
    print("\n[2/3] Analyzing dependencies...")
    issues = analyze_dependencies(skills)

    unique_violations = len(set((i['skill'], i['dependency']) for i in issues['grade_violations']))
    unique_circular = len(issues['circular_dependencies'])
    unique_redundant = len(set((i['skill'], i['redundant_dep']) for i in issues['redundant_dependencies']))
    unique_cross_topic = len(issues['missing_cross_topic'])
    unique_foundational = len(issues['missing_foundational'])

    print(f"\n      Issues found:")
    print(f"      - Missing cross-topic dependencies: {unique_cross_topic}")
    print(f"      - Grade violations (X-2 rule): {unique_violations}")
    print(f"      - Circular dependencies: {unique_circular}")
    print(f"      - Potentially redundant: {unique_redundant}")
    print(f"      - Missing foundational: {unique_foundational}")

    # Generate report
    print("\n[3/3] Generating report...")
    generate_report(skills, issues, output_file)
    print(f"      Report saved to: {output_file}")

    print("\n" + "=" * 70)
    print("Analysis complete!")
    print("=" * 70)

if __name__ == "__main__":
    main()
