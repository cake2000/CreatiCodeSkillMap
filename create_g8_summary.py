#!/usr/bin/env python3
"""
Create a human-readable summary of G8 analysis results
"""

import json
from collections import defaultdict

# Load the report
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/G8_ANALYSIS_REPORT.json', 'r') as f:
    report = json.load(f)

# Create summary
output_lines = []
output_lines.append("=" * 100)
output_lines.append("GRADE 8 (G8) SKILLS COMPREHENSIVE ANALYSIS REPORT")
output_lines.append("=" * 100)
output_lines.append("")
output_lines.append(f"Total G8 Skills Analyzed: {report['total_g8_skills']}")
output_lines.append(f"Total Issues Found: {report['issues_found']}")
output_lines.append(f"  - HIGH Priority:   {report['high_priority_count']}")
output_lines.append(f"  - MEDIUM Priority: {report['medium_priority_count']}")
output_lines.append(f"  - LOW Priority:    {report['low_priority_count']}")
output_lines.append("")

# Skills by topic
output_lines.append("=" * 100)
output_lines.append("G8 SKILLS BY TOPIC")
output_lines.append("=" * 100)
for topic, skills in sorted(report['skills_by_topic'].items()):
    output_lines.append(f"{topic}: {len(skills)} skills - {', '.join(skills)}")
output_lines.append("")

# HIGH PRIORITY ISSUES
output_lines.append("=" * 100)
output_lines.append(f"HIGH PRIORITY ISSUES ({report['high_priority_count']} total)")
output_lines.append("=" * 100)
output_lines.append("")

# Group by issue type
high_by_type = defaultdict(list)
for issue in report['high_priority_issues']:
    high_by_type[issue['issue_type']].append(issue)

for issue_type, issues in sorted(high_by_type.items()):
    output_lines.append(f"\n{issue_type.upper().replace('_', ' ')} ({len(issues)} issues)")
    output_lines.append("-" * 100)
    for i, issue in enumerate(issues[:20], 1):  # Show first 20 of each type
        output_lines.append(f"\n{i}. Skill: {issue['skill_id']}")
        output_lines.append(f"   Title: {issue['skill_title']}")
        output_lines.append(f"   Problem: {issue['description']}")
        if 'problematic_dependency' in issue:
            output_lines.append(f"   Problematic Dependency: {issue['problematic_dependency']}")
        output_lines.append(f"   Current Dependencies: {', '.join(issue['current_dependencies']) if issue['current_dependencies'] else 'None'}")
        output_lines.append(f"   Recommended Fix: {issue['recommended_fix']}")

    if len(issues) > 20:
        output_lines.append(f"\n   ... and {len(issues) - 20} more {issue_type} issues")
    output_lines.append("")

# MEDIUM PRIORITY ISSUES
output_lines.append("\n" + "=" * 100)
output_lines.append(f"MEDIUM PRIORITY ISSUES ({report['medium_priority_count']} total)")
output_lines.append("=" * 100)
output_lines.append("")

med_by_type = defaultdict(list)
for issue in report['medium_priority_issues']:
    med_by_type[issue['issue_type']].append(issue)

for issue_type, issues in sorted(med_by_type.items()):
    output_lines.append(f"\n{issue_type.upper().replace('_', ' ')} ({len(issues)} issues)")
    output_lines.append("-" * 100)
    for i, issue in enumerate(issues, 1):
        output_lines.append(f"\n{i}. Skill: {issue['skill_id']}")
        output_lines.append(f"   Title: {issue['skill_title']}")
        output_lines.append(f"   Problem: {issue['description']}")
        if 'problematic_dependency' in issue:
            output_lines.append(f"   Problematic Dependency: {issue['problematic_dependency']}")
        output_lines.append(f"   Current Dependencies: {', '.join(issue['current_dependencies']) if issue['current_dependencies'] else 'None'}")
        output_lines.append(f"   Recommended Fix: {issue['recommended_fix']}")
    output_lines.append("")

# Summary statistics
output_lines.append("\n" + "=" * 100)
output_lines.append("ISSUE TYPE BREAKDOWN")
output_lines.append("=" * 100)
output_lines.append("")
output_lines.append("HIGH PRIORITY:")
for issue_type, issues in sorted(high_by_type.items()):
    output_lines.append(f"  {issue_type}: {len(issues)}")

if med_by_type:
    output_lines.append("\nMEDIUM PRIORITY:")
    for issue_type, issues in sorted(med_by_type.items()):
        output_lines.append(f"  {issue_type}: {len(issues)}")

# Top problematic skills
output_lines.append("\n" + "=" * 100)
output_lines.append("SKILLS WITH MOST ISSUES")
output_lines.append("=" * 100)
output_lines.append("")

# Count issues per skill
skill_issue_count = defaultdict(lambda: {'high': 0, 'medium': 0, 'low': 0, 'title': 'Unknown'})
for issue in report['high_priority_issues']:
    skill_id = issue['skill_id']
    skill_issue_count[skill_id]['high'] += 1
    skill_issue_count[skill_id]['title'] = issue['skill_title']

for issue in report['medium_priority_issues']:
    skill_id = issue['skill_id']
    skill_issue_count[skill_id]['medium'] += 1
    skill_issue_count[skill_id]['title'] = issue['skill_title']

# Sort by total issues
sorted_skills = sorted(skill_issue_count.items(),
                       key=lambda x: x[1]['high'] * 100 + x[1]['medium'] * 10 + x[1]['low'],
                       reverse=True)

for i, (skill_id, counts) in enumerate(sorted_skills[:30], 1):
    total = counts['high'] + counts['medium'] + counts['low']
    output_lines.append(f"{i}. {skill_id}: {counts['title']}")
    output_lines.append(f"   Total Issues: {total} (High: {counts['high']}, Medium: {counts['medium']}, Low: {counts['low']})")

# Write summary
output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/G8_ANALYSIS_SUMMARY.txt'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print('\n'.join(output_lines))
print(f"\n\nSummary saved to: {output_file}")
