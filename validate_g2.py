#!/usr/bin/env python3
"""
Comprehensive G2 Skills Validation Report
Validates all G2 skills for dependency rules, references, and clarity
"""

import re
from collections import defaultdict

def parse_skills(filename):
    """Parse all skills from the markdown file"""
    skills = {}
    current_skill = None
    current_deps = []
    in_deps = False

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()

            # New skill starts with ID:
            if line.startswith('ID: '):
                # Save previous skill (including dependencies)
                if current_skill:
                    if in_deps:
                        current_skill['dependencies'] = current_deps
                    skills[current_skill['id']] = current_skill

                skill_id = line.replace('ID: ', '').strip()
                current_skill = {
                    'id': skill_id,
                    'topic': '',
                    'skill_name': '',
                    'description': '',
                    'dependencies': []
                }
                current_deps = []
                in_deps = False

            elif line.startswith('Topic: ') and current_skill:
                current_skill['topic'] = line.replace('Topic: ', '').strip()

            elif line.startswith('Skill: ') and current_skill:
                current_skill['skill_name'] = line.replace('Skill: ', '').strip()

            elif line.startswith('Description: ') and current_skill:
                current_skill['description'] = line.replace('Description: ', '').strip()

            elif line.startswith('Dependencies:'):
                in_deps = True
                current_deps = []

            elif in_deps and line.startswith('* '):
                # Parse dependency: "* T01.GK.01: Description text"
                dep_match = re.match(r'\* ([^:]+):', line)
                if dep_match:
                    dep_id = dep_match.group(1).strip()
                    current_deps.append(dep_id)

            elif in_deps and not line.startswith('*') and not line.strip() == '':
                # End of dependencies section when we hit a non-asterisk, non-blank line
                if current_skill:
                    current_skill['dependencies'] = current_deps
                in_deps = False

        # Save last skill (including dependencies if we're still in deps section)
        if current_skill:
            if in_deps:
                current_skill['dependencies'] = current_deps
            skills[current_skill['id']] = current_skill

    return skills

def get_grade(skill_id):
    """Extract grade from skill ID (e.g., T01.G2.01 -> G2)"""
    match = re.match(r'T\d+\.(GK|G[1-5])', skill_id)
    if match:
        return match.group(1)
    return None

def get_grade_level(grade):
    """Convert grade to numeric level for comparison"""
    if grade == 'GK':
        return 0
    elif grade and grade.startswith('G'):
        return int(grade[1:])
    return -1

def validate_g2_skills(skills):
    """Comprehensive validation of all G2 skills"""

    print("=" * 80)
    print("G2 SKILLS VALIDATION REPORT")
    print("=" * 80)
    print()

    # Filter G2 skills
    g2_skills = {sid: s for sid, s in skills.items() if get_grade(sid) == 'G2'}

    print(f"Total G2 Skills Found: {len(g2_skills)}")
    print()

    # Validation categories
    critical_issues = []
    high_issues = []
    medium_issues = []
    low_issues = []
    broad_skills = []

    # Dependency grade statistics
    dep_grade_counts = defaultdict(int)

    # Validation checks
    for skill_id, skill in sorted(g2_skills.items()):
        skill_issues = []

        # Check 1: Forward dependencies (G3+)
        forward_deps = []
        gk_deps = []
        broken_refs = []

        for dep_id in skill['dependencies']:
            dep_grade = get_grade(dep_id)

            if dep_grade:
                dep_grade_counts[dep_grade] += 1
                dep_level = get_grade_level(dep_grade)

                # Forward dependency check
                if dep_level > 2:
                    forward_deps.append(dep_id)

                # GK dependency check
                if dep_grade == 'GK':
                    gk_deps.append(dep_id)

            # Check if dependency exists
            if dep_id not in skills:
                broken_refs.append(dep_id)

        # Categorize issues
        if forward_deps:
            critical_issues.append({
                'skill_id': skill_id,
                'skill_name': skill['skill_name'],
                'issue': f"Forward dependencies to G3+: {', '.join(forward_deps)}",
                'severity': 'CRITICAL'
            })

        if broken_refs:
            critical_issues.append({
                'skill_id': skill_id,
                'skill_name': skill['skill_name'],
                'issue': f"Broken references: {', '.join(broken_refs)}",
                'severity': 'CRITICAL'
            })

        if gk_deps:
            medium_issues.append({
                'skill_id': skill_id,
                'skill_name': skill['skill_name'],
                'issue': f"Still depends on GK skills: {', '.join(gk_deps)}",
                'severity': 'MEDIUM'
            })

        # Check 2: No dependencies
        if not skill['dependencies']:
            low_issues.append({
                'skill_id': skill_id,
                'skill_name': skill['skill_name'],
                'issue': "No dependencies defined",
                'severity': 'LOW'
            })

        # Check 3: Circular dependencies (basic check)
        for dep_id in skill['dependencies']:
            if dep_id in skills:
                dep_skill = skills[dep_id]
                if skill_id in dep_skill['dependencies']:
                    critical_issues.append({
                        'skill_id': skill_id,
                        'skill_name': skill['skill_name'],
                        'issue': f"Circular dependency with {dep_id}",
                        'severity': 'CRITICAL'
                    })

        # Check 4: Skill clarity (vague or too broad)
        skill_name_lower = skill['skill_name'].lower()
        desc_lower = skill['description'].lower()

        vague_indicators = [
            'understand', 'know', 'learn about', 'explore',
            'introduction to', 'basics of', 'overview'
        ]

        broad_indicators = [
            'multiple', 'various', 'different', 'several',
            'and/or', 'complex', 'advanced'
        ]

        is_vague = any(ind in skill_name_lower or ind in desc_lower for ind in vague_indicators)
        is_broad = any(ind in skill_name_lower or ind in desc_lower for ind in broad_indicators)

        if is_vague or is_broad:
            reason = []
            if is_vague:
                reason.append("vague terminology")
            if is_broad:
                reason.append("potentially too broad")

            broad_skills.append({
                'skill_id': skill_id,
                'skill_name': skill['skill_name'],
                'reason': ', '.join(reason),
                'description': skill['description'][:100] + '...' if len(skill['description']) > 100 else skill['description']
            })

    # Print results
    print("=" * 80)
    print("1. DEPENDENCY GRADE DISTRIBUTION")
    print("=" * 80)
    print()
    print("G2 skills depend on:")
    for grade in ['GK', 'G1', 'G2', 'G3', 'G4', 'G5']:
        count = dep_grade_counts.get(grade, 0)
        print(f"  {grade}: {count} dependencies")
    print()

    # Calculate statistics
    total_issues = len(critical_issues) + len(high_issues) + len(medium_issues) + len(low_issues)

    print("=" * 80)
    print("2. VALIDATION SUMMARY")
    print("=" * 80)
    print()
    print(f"Total Issues Found: {total_issues}")
    print(f"  Critical: {len(critical_issues)}")
    print(f"  High: {len(high_issues)}")
    print(f"  Medium: {len(medium_issues)}")
    print(f"  Low: {len(low_issues)}")
    print()
    print(f"Skills with clarity concerns: {len(broad_skills)}")
    print()

    # Critical Issues
    if critical_issues:
        print("=" * 80)
        print("3. CRITICAL ISSUES (Must Fix)")
        print("=" * 80)
        print()
        for issue in critical_issues:
            print(f"[{issue['skill_id']}] {issue['skill_name']}")
            print(f"  Issue: {issue['issue']}")
            print()
    else:
        print("=" * 80)
        print("3. CRITICAL ISSUES")
        print("=" * 80)
        print()
        print("No critical issues found!")
        print()

    # High Issues
    if high_issues:
        print("=" * 80)
        print("4. HIGH PRIORITY ISSUES")
        print("=" * 80)
        print()
        for issue in high_issues:
            print(f"[{issue['skill_id']}] {issue['skill_name']}")
            print(f"  Issue: {issue['issue']}")
            print()
    else:
        print("=" * 80)
        print("4. HIGH PRIORITY ISSUES")
        print("=" * 80)
        print()
        print("No high priority issues found!")
        print()

    # Medium Issues
    if medium_issues:
        print("=" * 80)
        print("5. MEDIUM PRIORITY ISSUES")
        print("=" * 80)
        print()
        print(f"Found {len(medium_issues)} G2 skills still depending on GK skills.")
        print("Recommendation: These should preferably depend on G1 or G2 skills instead.")
        print()
        for issue in medium_issues[:10]:  # Show first 10
            print(f"[{issue['skill_id']}] {issue['skill_name']}")
            print(f"  Issue: {issue['issue']}")
            print()
        if len(medium_issues) > 10:
            print(f"... and {len(medium_issues) - 10} more")
            print()
    else:
        print("=" * 80)
        print("5. MEDIUM PRIORITY ISSUES")
        print("=" * 80)
        print()
        print("No medium priority issues found!")
        print()

    # Low Issues
    if low_issues:
        print("=" * 80)
        print("6. LOW PRIORITY ISSUES")
        print("=" * 80)
        print()
        print(f"Found {len(low_issues)} G2 skills with no dependencies.")
        print()
        for issue in low_issues[:5]:  # Show first 5
            print(f"[{issue['skill_id']}] {issue['skill_name']}")
            print()
        if len(low_issues) > 5:
            print(f"... and {len(low_issues) - 5} more")
            print()
    else:
        print("=" * 80)
        print("6. LOW PRIORITY ISSUES")
        print("=" * 80)
        print()
        print("No low priority issues found!")
        print()

    # Clarity concerns
    if broad_skills:
        print("=" * 80)
        print("7. SKILL CLARITY CONCERNS")
        print("=" * 80)
        print()
        print(f"Found {len(broad_skills)} skills that may be too broad or vague.")
        print()
        for skill in broad_skills[:10]:  # Show first 10
            print(f"[{skill['skill_id']}] {skill['skill_name']}")
            print(f"  Reason: {skill['reason']}")
            print(f"  Description: {skill['description']}")
            print()
        if len(broad_skills) > 10:
            print(f"... and {len(broad_skills) - 10} more")
            print()
    else:
        print("=" * 80)
        print("7. SKILL CLARITY CONCERNS")
        print("=" * 80)
        print()
        print("All skills appear to have clear, specific descriptions!")
        print()

    # Overall assessment
    print("=" * 80)
    print("8. OVERALL ASSESSMENT")
    print("=" * 80)
    print()

    if len(critical_issues) == 0 and len(high_issues) == 0:
        print("Status: EXCELLENT")
        print()
        print("The G2 skill set is in excellent condition:")
        print("- No critical dependency rule violations")
        print("- No forward dependencies to G3+ skills")
        print("- No broken references")
        print("- Dependency structure follows proper hierarchy")
        print()
    elif len(critical_issues) == 0:
        print("Status: GOOD")
        print()
        print("The G2 skill set is in good condition:")
        print("- No critical issues found")
        print("- Some medium/low priority improvements possible")
        print()
    elif len(critical_issues) <= 5:
        print("Status: NEEDS ATTENTION")
        print()
        print("The G2 skill set needs some fixes:")
        print(f"- {len(critical_issues)} critical issues to address")
        print("- Review and fix critical issues first")
        print()
    else:
        print("Status: REQUIRES IMMEDIATE ATTENTION")
        print()
        print("The G2 skill set has significant issues:")
        print(f"- {len(critical_issues)} critical issues found")
        print("- Systematic review and fixing required")
        print()

    # Recommendations
    print("=" * 80)
    print("9. RECOMMENDATIONS")
    print("=" * 80)
    print()

    if critical_issues:
        print("1. Fix all critical issues immediately")
        print("   - Remove forward dependencies to G3+ skills")
        print("   - Fix broken skill references")
        print("   - Resolve circular dependencies")
        print()

    if len(medium_issues) > 0:
        print(f"2. Review {len(medium_issues)} skills still depending on GK")
        print("   - Consider updating to depend on G1 or G2 skills instead")
        print("   - This creates better learning progression")
        print()

    if len(broad_skills) > 10:
        print(f"3. Review {len(broad_skills)} skills with clarity concerns")
        print("   - Consider breaking down overly broad skills")
        print("   - Make vague descriptions more specific and actionable")
        print()

    if total_issues == 0:
        print("No immediate action required. G2 skills are well-structured!")
        print()

    print("=" * 80)
    print("END OF REPORT")
    print("=" * 80)

    return {
        'total_g2_skills': len(g2_skills),
        'critical_issues': len(critical_issues),
        'high_issues': len(high_issues),
        'medium_issues': len(medium_issues),
        'low_issues': len(low_issues),
        'clarity_concerns': len(broad_skills),
        'dependency_distribution': dict(dep_grade_counts)
    }

if __name__ == '__main__':
    filename = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills from allskills.md...")
    skills = parse_skills(filename)
    print(f"Total skills parsed: {len(skills)}")
    print()

    results = validate_g2_skills(skills)
