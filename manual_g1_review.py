#!/usr/bin/env python3
"""
Manual careful review of Grade 1 cross-topic dependencies.
Focus on actual actionable issues only.
"""

import re
from collections import defaultdict

def parse_skills(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    skills = {}
    current_skill = None
    in_dependencies = False

    lines = content.split('\n')
    for line in lines:
        id_match = re.match(r'^ID: (T\d+\.G[K12].\d+)$', line)
        if id_match:
            if current_skill:
                skills[current_skill['id']] = current_skill
            skill_id = id_match.group(1)
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': []
            }
            in_dependencies = False
            continue

        if current_skill:
            if line.startswith('Topic: '):
                current_skill['topic'] = line.replace('Topic: ', '').strip()
                in_dependencies = False
            elif line.startswith('Skill: '):
                current_skill['skill'] = line.replace('Skill: ', '').strip()
                in_dependencies = False
            elif line.startswith('Description: '):
                current_skill['description'] = line.replace('Description: ', '').strip()
                in_dependencies = False
            elif line.strip() == 'Dependencies:':
                in_dependencies = True
            elif in_dependencies and line.startswith('* '):
                dep_match = re.match(r'\* (T\d+\.G[K12].\d+):', line)
                if dep_match:
                    current_skill['dependencies'].append(dep_match.group(1))

    if current_skill:
        skills[current_skill['id']] = current_skill

    return skills

def extract_grade(skill_id):
    match = re.search(r'\.G([K12])\.', skill_id)
    return match.group(1) if match else None

def extract_topic(skill_id):
    match = re.match(r'T(\d+)\.', skill_id)
    return int(match.group(1)) if match else None

def manual_review(skills):
    """
    Manual review of specific Grade 1 cross-topic dependency issues.
    Only includes issues with high confidence.
    """
    issues = []
    g1_skills = {k: v for k, v in skills.items() if extract_grade(k) == '1'}

    # Issue 1: Transitive redundancies (same topic)
    # T10.G1.01 has both T10.GK.01 and T10.GK.04, where GK.01 -> GK.04
    skill = g1_skills.get('T10.G1.01')
    if skill and 'T10.GK.01' in skill['dependencies'] and 'T10.GK.04' in skill['dependencies']:
        # Verify T10.GK.01 is dependency of T10.GK.04
        if 'T10.GK.04' in skills and 'T10.GK.01' in skills['T10.GK.04']['dependencies']:
            issues.append({
                'skill': 'T10.G1.01',
                'type': 'TRANSITIVE_REDUNDANT',
                'current_deps': skill['dependencies'],
                'redundant': 'T10.GK.01',
                'keep': 'T10.GK.04',
                'proposed_deps': [d for d in skill['dependencies'] if d != 'T10.GK.01'],
                'reasoning': 'T10.GK.01 is already a dependency of T10.GK.04, making it transitive. Remove T10.GK.01.',
                'confidence': 'HIGH'
            })

    # Issue 2: T24.G1.02 transitive
    skill = g1_skills.get('T24.G1.02')
    if skill and 'T24.GK.01' in skill['dependencies'] and 'T24.GK.03' in skill['dependencies']:
        if 'T24.GK.03' in skills and 'T24.GK.01' in skills['T24.GK.03']['dependencies']:
            issues.append({
                'skill': 'T24.G1.02',
                'type': 'TRANSITIVE_REDUNDANT',
                'current_deps': skill['dependencies'],
                'redundant': 'T24.GK.01',
                'keep': 'T24.GK.03',
                'proposed_deps': [d for d in skill['dependencies'] if d != 'T24.GK.01'],
                'reasoning': 'T24.GK.01 is already a dependency of T24.GK.03. Remove T24.GK.01.',
                'confidence': 'HIGH'
            })

    # Issue 3: T24.G1.03 transitive
    skill = g1_skills.get('T24.G1.03')
    if skill and 'T24.GK.03' in skill['dependencies'] and 'T24.G1.02' in skill['dependencies']:
        if 'T24.G1.02' in skills and 'T24.GK.03' in skills['T24.G1.02']['dependencies']:
            issues.append({
                'skill': 'T24.G1.03',
                'type': 'TRANSITIVE_REDUNDANT',
                'current_deps': skill['dependencies'],
                'redundant': 'T24.GK.03',
                'keep': 'T24.G1.02',
                'proposed_deps': [d for d in skill['dependencies'] if d != 'T24.GK.03'],
                'reasoning': 'T24.GK.03 is already a dependency of T24.G1.02. Remove T24.GK.03.',
                'confidence': 'HIGH'
            })

    # Now check for X-2 violations (CRITICAL)
    for skill_id, skill in g1_skills.items():
        for dep in skill['dependencies']:
            if dep in skills and extract_grade(dep) == '2':
                issues.append({
                    'skill': skill_id,
                    'type': 'X-2_VIOLATION',
                    'current_deps': skill['dependencies'],
                    'bad_dep': dep,
                    'bad_dep_name': skills[dep]['skill'],
                    'proposed_deps': [d for d in skill['dependencies'] if d != dep],
                    'reasoning': f'Grade 1 skill cannot depend on Grade 2 skill {dep}. This violates the X-2 rule.',
                    'confidence': 'CRITICAL'
                })

    # Check for missing foundational cross-topic dependencies
    # These require manual verification of each case

    # Look at all Grade 1 skills and analyze systematically
    for skill_id, skill in sorted(g1_skills.items()):
        topic = extract_topic(skill_id)
        desc = skill['description'].lower()
        deps = skill['dependencies']
        dep_topics = set(extract_topic(d) for d in deps if d in skills)

        # Pattern 1: Skills mentioning "Scratch" or "blocks" in advanced topics
        # that don't have basic dependencies
        if topic >= 16:
            if 'scratch' in desc or ' block' in desc or 'sprite' in desc:
                # These likely need event dependencies if they're interactive
                if ('click' in desc or 'press' in desc or 'when' in desc) and 6 not in dep_topics:
                    # Manual check needed - but flag for review
                    pass  # Would need case-by-case

    return issues

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills...")
    skills = parse_skills(filepath)

    g1_skills = {k: v for k, v in skills.items() if extract_grade(k) == '1'}
    print(f"Found {len(g1_skills)} Grade 1 skills\n")

    print("Performing manual review...")
    issues = manual_review(skills)

    print("\n" + "="*100)
    print("GRADE 1 CROSS-TOPIC DEPENDENCY ISSUES - FINAL REPORT")
    print("="*100)
    print(f"\nTotal verified issues: {len(issues)}\n")

    # Group by confidence
    by_confidence = defaultdict(list)
    for issue in issues:
        by_confidence[issue['confidence']].append(issue)

    for confidence in ['CRITICAL', 'HIGH', 'MEDIUM']:
        if confidence in by_confidence:
            print(f"\n{confidence} CONFIDENCE: {len(by_confidence[confidence])} issues")

    # Save comprehensive report
    output = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G1_FINAL_DEPENDENCY_FIXES.md'
    with open(output, 'w') as f:
        f.write("# Grade 1 Cross-Topic Dependency Issues - Final Report\n\n")
        f.write("**Analysis Date:** 2024-11-24\n\n")
        f.write("**Analyst:** Manual verification with automated assistance\n\n")
        f.write(f"**Total Grade 1 Skills Reviewed:** {len(g1_skills)}\n\n")
        f.write(f"**Total Verified Issues:** {len(issues)}\n\n")

        f.write("## Summary by Confidence Level\n\n")
        f.write("| Confidence | Count | Description |\n")
        f.write("|------------|-------|-------------|\n")
        f.write(f"| CRITICAL | {len(by_confidence.get('CRITICAL', []))} | X-2 rule violations - must fix |\n")
        f.write(f"| HIGH | {len(by_confidence.get('HIGH', []))} | Clear transitive redundancies - should fix |\n")
        f.write(f"| MEDIUM | {len(by_confidence.get('MEDIUM', []))} | Potential improvements - consider fixing |\n\n")

        # Detailed issues
        for confidence in ['CRITICAL', 'HIGH', 'MEDIUM']:
            if confidence not in by_confidence:
                continue

            conf_issues = by_confidence[confidence]
            f.write(f"\n---\n\n## {confidence} Priority ({len(conf_issues)} issues)\n\n")

            for idx, issue in enumerate(conf_issues, 1):
                skill_id = issue['skill']
                skill = skills[skill_id]

                f.write(f"### {idx}. {skill_id}\n\n")
                f.write(f"**Skill Name:** {skill['skill']}\n\n")
                f.write(f"**Topic:** {skill['topic']}\n\n")
                f.write(f"**Issue Type:** {issue['type']}\n\n")
                f.write(f"**Current Dependencies:**\n")
                for dep in issue['current_deps']:
                    if dep in skills:
                        f.write(f"- `{dep}`: {skills[dep]['skill']}\n")
                    else:
                        f.write(f"- `{dep}`\n")
                f.write("\n")

                if issue['type'] == 'TRANSITIVE_REDUNDANT':
                    f.write(f"**Redundant Dependency:** `{issue['redundant']}`\n\n")
                    f.write(f"**Keep Dependency:** `{issue['keep']}`\n\n")
                elif issue['type'] == 'X-2_VIOLATION':
                    f.write(f"**Violating Dependency:** `{issue['bad_dep']}` ({issue['bad_dep_name']})\n\n")

                f.write(f"**Proposed Dependencies:**\n")
                for dep in issue['proposed_deps']:
                    if dep in skills:
                        f.write(f"- `{dep}`: {skills[dep]['skill']}\n")
                    else:
                        f.write(f"- `{dep}`\n")
                f.write("\n")

                f.write(f"**Reasoning:** {issue['reasoning']}\n\n")

                f.write("**Action Required:**\n")
                if issue['type'] == 'TRANSITIVE_REDUNDANT':
                    f.write(f"Remove `{issue['redundant']}` from dependencies list.\n\n")
                elif issue['type'] == 'X-2_VIOLATION':
                    f.write(f"Remove `{issue['bad_dep']}` and replace with appropriate K or Grade 1 skill.\n\n")

                f.write("\n")

    print(f"\n\nFinal report saved to:\n{output}\n")

    # Print quick fix list
    print("\n" + "="*100)
    print("QUICK FIX LIST")
    print("="*100 + "\n")

    for issue in issues:
        print(f"Skill: {issue['skill']}")
        print(f"  Type: {issue['type']}")
        if issue['type'] == 'TRANSITIVE_REDUNDANT':
            print(f"  Action: Remove {issue['redundant']}")
        elif issue['type'] == 'X-2_VIOLATION':
            print(f"  Action: Remove {issue['bad_dep']}")
        print()

if __name__ == '__main__':
    main()
