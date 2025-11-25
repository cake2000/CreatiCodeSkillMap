#!/usr/bin/env python3
"""
Generate comprehensive Grade 8 analysis report
"""

import json
import re
from collections import defaultdict

def load_changes():
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g8_changes_log.json', 'r') as f:
        return json.load(f)

def parse_skills(content: str):
    """Parse all skills from the markdown content."""
    skills = {}
    skill_blocks = re.split(r'\n(?=ID: )', content)

    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID: '):
            continue

        lines = block.strip().split('\n')
        skill_id = None
        dependencies = []

        in_deps = False

        for line in lines:
            if line.startswith('ID: '):
                skill_id = line.replace('ID: ', '').strip()
            elif line.startswith('Dependencies:'):
                in_deps = True
            elif in_deps and line.startswith('* '):
                dep_match = re.match(r'\* ([^:]+): (.+)', line)
                if dep_match:
                    dep_id = dep_match.group(1).strip()
                    dep_name = dep_match.group(2).strip()
                    dependencies.append({'id': dep_id, 'name': dep_name})
            elif in_deps and line.strip() == '':
                in_deps = False

        if skill_id:
            skills[skill_id] = {
                'id': skill_id,
                'dependencies': dependencies
            }

    return skills

def get_grade(skill_id: str) -> str:
    match = re.search(r'\.(G\d+|GK)\.', skill_id)
    if match:
        return match.group(1)
    return None

def get_topic(skill_id: str) -> str:
    match = re.match(r'(T\d+)\.', skill_id)
    if match:
        return match.group(1)
    return None

def main():
    print("Loading changes log...")
    data = load_changes()

    print("Reading updated allskills.md...")
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r', encoding='utf-8') as f:
        content = f.read()

    skills = parse_skills(content)
    g8_skills = {sid: skill for sid, skill in skills.items() if get_grade(sid) == 'G8'}

    # Generate comprehensive report
    report = []
    report.append("=" * 80)
    report.append("GRADE 8 DEPENDENCY ANALYSIS - PHASE 2 COMPLETE REPORT")
    report.append("=" * 80)
    report.append("")

    # 1. Overview statistics
    report.append("## OVERVIEW STATISTICS")
    report.append(f"Total Grade 8 skills analyzed: {len(g8_skills)}")
    report.append(f"Total skills with cross-topic dependencies added: {len(data['skill_changes'])}")
    report.append("")

    # 2. X-2 Rule Violations
    report.append("## X-2 RULE VIOLATIONS FOUND")
    report.append(f"Total skills with violations: {len(data['summary']['x2_violations'])}")
    report.append("")
    report.append("Skills requiring scaffolding (dependencies > 2 grades below):")
    for v in data['summary']['x2_violations']:
        report.append(f"  - {v['skill_id']}: {len(v['violations'])} violations")
        for vid in v['violations'][:3]:
            report.append(f"    * {vid}")
    report.append("")

    # 3. Cross-topic dependencies added
    report.append("## CROSS-TOPIC DEPENDENCIES ADDED")
    report.append(f"Total cross-topic dependencies added: {len(data['summary']['cross_topic_adds'])}")
    report.append("")

    # Count by topic
    topic_counts = defaultdict(int)
    for change in data['summary']['cross_topic_adds']:
        skill_id = change['skill_id']
        topic = get_topic(skill_id)
        topic_counts[topic] += 1

    report.append("Dependencies added by topic:")
    for topic in sorted(topic_counts.keys()):
        report.append(f"  {topic}: {topic_counts[topic]} additions")
    report.append("")

    # 4. Top 20 most significant changes
    report.append("## TOP 20 MOST SIGNIFICANT CHANGES")
    report.append("")

    # Calculate significance (number of changes)
    skill_significance = []
    for skill_id, changes in data['skill_changes'].items():
        num_adds = len(changes['adds'])
        num_removes = len(changes['removes'])
        total = num_adds + num_removes
        if total > 0:
            skill_significance.append({
                'skill_id': skill_id,
                'adds': num_adds,
                'removes': num_removes,
                'total': total,
                'reasons': changes['reasons']
            })

    skill_significance.sort(key=lambda x: x['total'], reverse=True)

    for i, change in enumerate(skill_significance[:20], 1):
        report.append(f"{i}. Skill ID: {change['skill_id']}")
        report.append(f"   Topic: {get_topic(change['skill_id'])}")
        report.append(f"   Changes: +{change['adds']} dependencies added, -{change['removes']} removed")
        report.append(f"   Reasons:")
        for reason in change['reasons'][:5]:
            report.append(f"     - {reason}")
        report.append("")

    # 5. Circular dependencies
    report.append("## CIRCULAR DEPENDENCIES")
    if data['summary']['circular_fixes']:
        report.append(f"Found {len(data['summary']['circular_fixes'])} potential circular dependency chains")
        for cycle in data['summary']['circular_fixes'][:10]:
            report.append(f"  - {cycle}")
    else:
        report.append("No circular dependencies detected!")
    report.append("")

    # 6. Transitive redundancy
    report.append("## TRANSITIVE REDUNDANCY ANALYSIS")
    report.append(f"Skills with potential redundant dependencies: {len(data['summary']['redundancy_removes'])}")
    report.append("(Flagged for review - NOT auto-removed due to conservative approach)")
    report.append("")

    # 7. Skills still needing attention
    report.append("## SKILLS REQUIRING MANUAL REVIEW")
    report.append("")

    needs_review = set()

    # Add X-2 violators
    for v in data['summary']['x2_violations']:
        needs_review.add(v['skill_id'])

    # Add skills with many changes
    for change in skill_significance[:10]:
        if change['total'] >= 3:
            needs_review.add(change['skill_id'])

    report.append(f"Total skills needing manual review: {len(needs_review)}")
    report.append("")
    report.append("Priority review list:")
    for skill_id in sorted(needs_review)[:20]:
        report.append(f"  - {skill_id}")
    report.append("")

    # 8. Summary by change category
    report.append("## SUMMARY BY CHANGE CATEGORY")
    report.append("")
    report.append(f"X-2 Rule Violations Flagged: {len(data['summary']['x2_violations'])}")
    report.append(f"Cross-Topic Dependencies Added: {len(data['summary']['cross_topic_adds'])}")
    report.append(f"Circular Dependencies Found: {len(data['summary']['circular_fixes'])}")
    report.append(f"Transitive Redundancies Flagged: {len(data['summary']['redundancy_removes'])}")
    report.append(f"Total Issues Identified: {data['summary']['total_changes']}")
    report.append("")

    # 9. Current state analysis
    report.append("## CURRENT STATE ANALYSIS")
    report.append("")

    # Count dependencies per skill
    dep_counts = []
    for skill_id, skill in g8_skills.items():
        dep_counts.append(len(skill['dependencies']))

    avg_deps = sum(dep_counts) / len(dep_counts) if dep_counts else 0
    max_deps = max(dep_counts) if dep_counts else 0

    report.append(f"Average dependencies per Grade 8 skill: {avg_deps:.2f}")
    report.append(f"Maximum dependencies in a single skill: {max_deps}")
    report.append("")

    # Cross-topic dependency analysis
    cross_topic_count = 0
    for skill_id, skill in g8_skills.items():
        skill_topic = get_topic(skill_id)
        for dep in skill['dependencies']:
            dep_topic = get_topic(dep['id'])
            if dep_topic and dep_topic != skill_topic:
                cross_topic_count += 1
                break

    report.append(f"Skills with cross-topic dependencies: {cross_topic_count}/{len(g8_skills)}")
    report.append("")

    # 10. Recommendations
    report.append("## RECOMMENDATIONS")
    report.append("")
    report.append("1. IMMEDIATE ACTIONS:")
    report.append(f"   - Review {len(data['summary']['x2_violations'])} skills with X-2 violations")
    report.append("   - Add scaffolding skills for Grade 6-8 where dependencies skip too many grades")
    report.append("")
    report.append("2. VALIDATION:")
    report.append(f"   - Verify {len(data['summary']['cross_topic_adds'])} cross-topic dependencies added")
    report.append("   - Ensure they align with actual skill requirements")
    report.append("")
    report.append("3. CONSERVATIVE CHANGES:")
    report.append(f"   - {len(data['summary']['redundancy_removes'])} potential redundancies were FLAGGED but NOT removed")
    report.append("   - Review these to determine if they're truly redundant or needed for direct teaching")
    report.append("")

    # Save report
    report_text = "\n".join(report)
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/G8_PHASE2_COMPLETE_REPORT.md', 'w') as f:
        f.write(report_text)

    print(report_text)
    print("\n" + "=" * 80)
    print("Report saved to: G8_PHASE2_COMPLETE_REPORT.md")

if __name__ == '__main__':
    main()
