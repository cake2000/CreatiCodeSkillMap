#!/usr/bin/env python3
"""
Enhanced Grade K Dependency Analysis
Identifies missing cross-topic dependencies and potential issues
"""

import json
from collections import defaultdict

def analyze_cross_topic_dependencies(skills):
    """Analyze cross-topic dependency patterns"""

    analysis = {
        'skills_by_topic': defaultdict(list),
        'cross_topic_deps': [],
        'same_topic_deps': [],
        'potential_missing_deps': [],
        'isolated_skills': [],
        'hub_skills': []
    }

    # Group skills by topic
    for skill in skills:
        analysis['skills_by_topic'][skill['topic_id']].append(skill)

    # Create reverse dependency map (who depends on this skill)
    depended_on_by = defaultdict(list)

    for skill in skills:
        for dep in skill['dependencies']:
            depended_on_by[dep].append(skill['id'])

    # Analyze each skill
    for skill in skills:
        skill_topic = skill['topic_id']

        # Count hub skills (heavily depended upon)
        if len(depended_on_by[skill['id']]) >= 3:
            analysis['hub_skills'].append({
                'skill_id': skill['id'],
                'title': skill['title'],
                'topic': skill_topic,
                'depended_by_count': len(depended_on_by[skill['id']]),
                'depended_by': depended_on_by[skill['id']]
            })

        # Check if skill has no dependencies and no one depends on it
        if not skill['dependencies'] and not depended_on_by[skill['id']]:
            analysis['isolated_skills'].append({
                'skill_id': skill['id'],
                'title': skill['title'],
                'topic': skill_topic
            })

        # Analyze dependencies
        for dep in skill['dependencies']:
            # Extract topic from dependency
            dep_topic = dep.split('.')[0]

            dep_info = {
                'skill_id': skill['id'],
                'skill_title': skill['title'],
                'skill_topic': skill_topic,
                'depends_on': dep,
                'dep_topic': dep_topic
            }

            if dep_topic != skill_topic:
                analysis['cross_topic_deps'].append(dep_info)
            else:
                analysis['same_topic_deps'].append(dep_info)

    # Look for potential missing dependencies
    # Skills that use similar concepts should potentially depend on foundational skills

    # Skills that work with counting/numbers should depend on T09.GK.01
    counting_keywords = ['count', 'number', 'score', 'more', 'quantity']
    for skill in skills:
        if skill['id'] == 'T09.GK.01':
            continue
        title_lower = skill['title'].lower()
        desc_lower = skill['description'].lower()

        has_counting = any(kw in title_lower or kw in desc_lower for kw in counting_keywords)
        depends_on_t09_gk01 = 'T09.GK.01' in skill['dependencies']

        if has_counting and not depends_on_t09_gk01:
            analysis['potential_missing_deps'].append({
                'skill_id': skill['id'],
                'title': skill['title'],
                'topic': skill['topic_id'],
                'missing_dep': 'T09.GK.01',
                'reason': 'Uses counting/numbers but does not depend on T09.GK.01'
            })

    # Skills that work with sequencing should depend on T01.GK.01 or similar
    sequence_keywords = ['order', 'sequence', 'first', 'next', 'last', 'arrange']
    for skill in skills:
        if skill['id'] in ['T01.GK.01', 'T01.GK.02', 'T01.GK.03']:
            continue
        title_lower = skill['title'].lower()
        desc_lower = skill['description'].lower()

        has_sequencing = any(kw in title_lower or kw in desc_lower for kw in sequence_keywords)
        depends_on_t01 = any(dep.startswith('T01.GK') for dep in skill['dependencies'])

        if has_sequencing and not depends_on_t01:
            analysis['potential_missing_deps'].append({
                'skill_id': skill['id'],
                'title': skill['title'],
                'topic': skill['topic_id'],
                'missing_dep': 'T01.GK.01 or similar',
                'reason': 'Uses sequencing concepts but does not depend on T01 skills'
            })

    # Skills that work with sorting/grouping should depend on T10.GK.01
    sorting_keywords = ['sort', 'group', 'categorize', 'classify']
    for skill in skills:
        if skill['id'] == 'T10.GK.01':
            continue
        title_lower = skill['title'].lower()
        desc_lower = skill['description'].lower()

        has_sorting = any(kw in title_lower or kw in desc_lower for kw in sorting_keywords)
        depends_on_t10_gk01 = 'T10.GK.01' in skill['dependencies']

        if has_sorting and not depends_on_t10_gk01:
            analysis['potential_missing_deps'].append({
                'skill_id': skill['id'],
                'title': skill['title'],
                'topic': skill['topic_id'],
                'missing_dep': 'T10.GK.01',
                'reason': 'Uses sorting/grouping but does not depend on T10.GK.01'
            })

    # Skills that work with patterns should depend on T04.GK.01
    pattern_keywords = ['pattern', 'repeat']
    for skill in skills:
        if skill['id'] == 'T04.GK.01':
            continue
        title_lower = skill['title'].lower()
        desc_lower = skill['description'].lower()

        has_patterns = any(kw in title_lower or kw in desc_lower for kw in pattern_keywords)
        depends_on_t04_gk01 = 'T04.GK.01' in skill['dependencies']

        if has_patterns and not depends_on_t04_gk01:
            analysis['potential_missing_deps'].append({
                'skill_id': skill['id'],
                'title': skill['title'],
                'topic': skill['topic_id'],
                'missing_dep': 'T04.GK.01',
                'reason': 'Uses patterns/repetition but does not depend on T04.GK.01'
            })

    return analysis

def generate_enhanced_report(skills, analysis, output_file):
    """Generate enhanced analysis report"""

    report = []
    report.append("# GRADE K DEPENDENCY ANALYSIS - ENHANCED")
    report.append("\nGenerated: 2025-11-24")
    report.append("\n## Executive Summary\n")
    report.append(f"- **Total Grade K Skills:** {len(skills)}")
    report.append(f"- **Topics Covered:** {len(analysis['skills_by_topic'])}")
    report.append(f"- **Cross-Topic Dependencies:** {len(analysis['cross_topic_deps'])}")
    report.append(f"- **Same-Topic Dependencies:** {len(analysis['same_topic_deps'])}")
    report.append(f"- **Hub Skills (depended on by 3+ skills):** {len(analysis['hub_skills'])}")
    report.append(f"- **Isolated Skills (no deps in/out):** {len(analysis['isolated_skills'])}")
    report.append(f"- **Potential Missing Dependencies:** {len(analysis['potential_missing_deps'])}")

    # Hub skills
    report.append("\n## Hub Skills (High Leverage)\n")
    report.append("These skills are depended on by many other skills. Mastery is critical.\n")
    for hub in sorted(analysis['hub_skills'], key=lambda x: x['depended_by_count'], reverse=True):
        report.append(f"\n### {hub['skill_id']}: {hub['title']}")
        report.append(f"- **Topic:** {hub['topic']}")
        report.append(f"- **Depended on by {hub['depended_by_count']} skills:**")
        for dep_by in sorted(hub['depended_by']):
            report.append(f"  - {dep_by}")

    # Cross-topic dependencies
    report.append("\n## Cross-Topic Dependencies\n")
    report.append("Skills that depend on skills from other topics. These create curriculum integration points.\n")

    by_topic = defaultdict(list)
    for dep in analysis['cross_topic_deps']:
        by_topic[dep['skill_topic']].append(dep)

    for topic in sorted(by_topic.keys()):
        report.append(f"\n### Topic {topic}\n")
        for dep in sorted(by_topic[topic], key=lambda x: x['skill_id']):
            report.append(f"- **{dep['skill_id']}**: {dep['skill_title']}")
            report.append(f"  - Depends on: {dep['depends_on']} (from {dep['dep_topic']})")

    # Potential missing dependencies
    report.append("\n## Potential Missing Cross-Topic Dependencies\n")
    report.append("Skills that may benefit from additional prerequisite dependencies.\n")

    if analysis['potential_missing_deps']:
        by_topic = defaultdict(list)
        for issue in analysis['potential_missing_deps']:
            by_topic[issue['topic']].append(issue)

        for topic in sorted(by_topic.keys()):
            report.append(f"\n### Topic {topic}\n")
            for issue in sorted(by_topic[topic], key=lambda x: x['skill_id']):
                report.append(f"- **{issue['skill_id']}**: {issue['title']}")
                report.append(f"  - **Suggested dependency:** {issue['missing_dep']}")
                report.append(f"  - **Reason:** {issue['reason']}")
    else:
        report.append("\n✅ No potential missing dependencies identified.")

    # Isolated skills
    report.append("\n## Isolated Skills\n")
    report.append("Skills with no dependencies and not depended upon by any other skill.\n")
    report.append("These may be standalone concepts or may need better integration.\n")

    if analysis['isolated_skills']:
        by_topic = defaultdict(list)
        for skill in analysis['isolated_skills']:
            by_topic[skill['topic']].append(skill)

        for topic in sorted(by_topic.keys()):
            report.append(f"\n### Topic {topic}\n")
            for skill in sorted(by_topic[topic], key=lambda x: x['skill_id']):
                report.append(f"- **{skill['skill_id']}**: {skill['title']}")
    else:
        report.append("\n✅ No isolated skills found.")

    # Topic coverage summary
    report.append("\n## Topic Coverage Summary\n")
    for topic_id in sorted(analysis['skills_by_topic'].keys()):
        topic_skills = analysis['skills_by_topic'][topic_id]
        topic_name = topic_skills[0]['topic_name'] if topic_skills else "Unknown"

        with_deps = sum(1 for s in topic_skills if s['dependencies'])
        without_deps = len(topic_skills) - with_deps

        report.append(f"\n### {topic_id}: {topic_name}")
        report.append(f"- Total skills: {len(topic_skills)}")
        report.append(f"- With dependencies: {with_deps}")
        report.append(f"- Without dependencies: {without_deps}")

    # Write report
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report))

    print(f"Enhanced analysis written to: {output_file}")

def main():
    json_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade_k_skills.json'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE_K_DEPENDENCY_ANALYSIS.md'

    print("Loading Grade K skills...")
    with open(json_file, 'r', encoding='utf-8') as f:
        skills = json.load(f)

    print(f"Analyzing {len(skills)} skills...")
    analysis = analyze_cross_topic_dependencies(skills)

    print("Generating enhanced report...")
    generate_enhanced_report(skills, analysis, output_file)

    print(f"\nSummary:")
    print(f"- Hub skills: {len(analysis['hub_skills'])}")
    print(f"- Cross-topic dependencies: {len(analysis['cross_topic_deps'])}")
    print(f"- Potential missing dependencies: {len(analysis['potential_missing_deps'])}")
    print(f"- Isolated skills: {len(analysis['isolated_skills'])}")

if __name__ == '__main__':
    main()
