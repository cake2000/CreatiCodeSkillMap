#!/usr/bin/env python3
"""
Final refined analysis of Grade 2 skills (T21-T36) for missing cross-topic dependencies.
This version uses specific, targeted prerequisite skills based on actual content.
"""

import re
from collections import defaultdict

def parse_skills(filepath):
    """Parse the allskills.md file and extract skills with their dependencies."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by ID: markers
    skill_blocks = re.split(r'\n(?=ID: )', content)

    skills = []
    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID:'):
            continue

        # Extract skill ID
        id_match = re.search(r'ID:\s*(\S+)', block)
        if not id_match:
            continue

        skill_id = id_match.group(1)

        # Extract topic
        topic_match = re.search(r'Topic:\s*([^\n]+)', block)
        topic = topic_match.group(1).strip() if topic_match else ""

        # Extract skill name
        skill_match = re.search(r'Skill:\s*([^\n]+)', block)
        skill_name = skill_match.group(1).strip() if skill_match else ""

        # Extract description
        desc_match = re.search(r'Description:\s*(.*?)(?=\n(?:Activity Type:|Estimated Time:|CSTA:|Dependencies:|ID:|$))', block, re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""

        # Extract dependencies
        deps = []
        deps_section = re.search(r'Dependencies:(.*?)(?=\n\n|\Z)', block, re.DOTALL)
        if deps_section:
            dep_lines = deps_section.group(1).strip().split('\n')
            for line in dep_lines:
                dep_match = re.search(r'\*\s*([^:]+):', line)
                if dep_match:
                    deps.append(dep_match.group(1).strip())

        skills.append({
            'id': skill_id,
            'topic': topic,
            'skill': skill_name,
            'description': description,
            'dependencies': deps,
            'block': block
        })

    return skills

def extract_grade(skill_id):
    """Extract grade from skill ID (e.g., T01.G2.01 -> 2)"""
    match = re.search(r'\.G(\d+|K)\.', skill_id)
    if match:
        grade = match.group(1)
        return 0 if grade == 'K' else int(grade)
    return None

def extract_topic(skill_id):
    """Extract topic from skill ID (e.g., T01.G2.01 -> T01)"""
    match = re.match(r'(T\d+)', skill_id)
    return match.group(1) if match else None

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills...")
    all_skills = parse_skills(filepath)

    # Index skills by ID
    skills_by_id = {s['id']: s for s in all_skills}

    # Define specific recommendations based on manual analysis
    # Format: (skill_id, dependency_to_add, reason)
    manual_recommendations = [
        # T21 - AI Media
        ('T21.G2.02', 'T35.GK.04', 'Understanding why AI needs checking requires awareness of safe vs unsafe content'),

        # T22 - AI Chat
        ('T22.G2.02', 'T32.GK.01', 'Recognizing private information in chat requires foundational privacy concepts'),

        # T23 - Sensors (all need hardware basics)
        ('T23.G2.01', 'T30.GK.01', 'Understanding sensors requires knowing what devices are'),
        ('T23.G2.02', 'T30.GK.01', 'Understanding sensor limitations requires hardware knowledge'),
        ('T23.G2.03', 'T30.GK.01', 'Distinguishing sensor input from commands requires hardware understanding'),

        # T24 - AI/XO
        ('T24.G2.01', 'T01.GK.02', 'Understanding multi-step AI demonstrations requires sequencing concepts'),

        # T26 - Data Collection (needs data representation)
        ('T26.G2.01', 'T25.GK.01', 'Distinguishing data types requires understanding data representation'),
        ('T26.G2.03', 'T25.GK.01', 'Collecting duration data requires understanding how data is represented'),
        ('T26.G2.05', 'T25.GK.01', 'Conducting surveys requires understanding how to structure data'),

        # T27 - Data Visualization (needs collection + representation)
        ('T27.G2.01', 'T26.GK.01', 'Creating charts requires understanding data collection'),
        ('T27.G2.01', 'T25.GK.01', 'Creating charts requires understanding data representation'),
        ('T27.G2.04', 'T26.GK.01', 'Analyzing data requires understanding data collection'),

        # T28 - Probability
        ('T28.G2.04', 'T26.GK.01', 'Making predictions requires understanding data collection'),

        # T29 - Text Processing
        ('T29.G2.04', 'T01.GK.02', 'Find and replace operations require sequential processing understanding'),

        # T31 - Networks
        ('T31.G2.01', 'T30.GK.01', 'Understanding internet connections requires knowing about devices'),

        # T32 - Security (needs hardware + ethics)
        ('T32.G2.01', 'T30.GK.01', 'Creating passwords requires understanding devices that use them'),
        ('T32.G2.01', 'T35.GK.04', 'Password security connects to safe information sharing practices'),

        ('T32.G2.04', 'T30.GK.01', 'Device care requires understanding what devices are'),

        ('T32.G2.05', 'T30.GK.01', 'Understanding suspicious links requires device/internet knowledge'),
        ('T32.G2.05', 'T35.GK.04', 'Recognizing dangers requires judgment about safe sharing'),

        ('T32.G2.06', 'T30.GK.01', 'Understanding authentication requires device knowledge'),

        # T33 - Connectivity
        ('T33.G2.01', 'T31.GK.01', 'Understanding app connectivity requires network/internet basics'),

        # T34 - History
        ('T34.G2.01', 'T30.GK.01', 'Comparing past/present technology requires hardware understanding'),

        # T36 - Careers
        ('T36.G2.04', 'T35.GK.01', 'Understanding digital creation careers requires awareness of technology impacts'),
    ]

    # Filter to only valid recommendations (where dependency doesn't already exist)
    valid_recommendations = []
    for skill_id, dep_id, reason in manual_recommendations:
        if skill_id in skills_by_id and dep_id in skills_by_id:
            skill = skills_by_id[skill_id]
            if dep_id not in skill['dependencies']:
                valid_recommendations.append({
                    'skill_id': skill_id,
                    'add_dep': dep_id,
                    'reason': reason
                })

    # Print recommendations
    print("\n" + "=" * 80)
    print("FINAL CROSS-TOPIC DEPENDENCY RECOMMENDATIONS FOR GRADE 2 (T21-T36)")
    print("=" * 80)
    print()

    if not valid_recommendations:
        print("No missing cross-topic dependencies identified.")
    else:
        # Group by skill
        recs_by_skill = defaultdict(list)
        for rec in valid_recommendations:
            recs_by_skill[rec['skill_id']].append(rec)

        for skill_id in sorted(recs_by_skill.keys()):
            skill = skills_by_id[skill_id]

            print(f"\n{skill_id}: {skill['skill']}")
            print(f"Current deps: {', '.join(skill['dependencies']) if skill['dependencies'] else 'None'}")

            for rec in recs_by_skill[skill_id]:
                dep_skill = skills_by_id[rec['add_dep']]
                print(f"  → Add {rec['add_dep']}: {dep_skill['skill']}")
                print(f"     Reason: {rec['reason']}")

    print()
    print("=" * 80)
    print(f"Total recommendations: {len(valid_recommendations)}")
    print("=" * 80)

    # Save formatted output
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE2_T21_T36_MISSING_DEPS.txt'
    with open(output_file, 'w') as f:
        f.write("GRADE 2 (T21-T36) MISSING CROSS-TOPIC DEPENDENCIES\n")
        f.write("=" * 80 + "\n")
        f.write("Conservative recommendations following X-2 rule\n")
        f.write("Only adding clearly necessary cross-topic dependencies\n")
        f.write("=" * 80 + "\n\n")

        for rec in sorted(valid_recommendations, key=lambda r: r['skill_id']):
            f.write(f"{rec['skill_id']}: Add dependency {rec['add_dep']} - Reason: {rec['reason']}\n")

        f.write(f"\n{'=' * 80}\n")
        f.write(f"Total recommendations: {len(valid_recommendations)}\n")

    print(f"\nRecommendations saved to: {output_file}")

    # Also save detailed output
    detailed_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE2_T21_T36_DETAILED.txt'
    with open(detailed_file, 'w') as f:
        f.write("GRADE 2 (T21-T36) MISSING CROSS-TOPIC DEPENDENCIES - DETAILED\n")
        f.write("=" * 80 + "\n\n")

        recs_by_skill = defaultdict(list)
        for rec in valid_recommendations:
            recs_by_skill[rec['skill_id']].append(rec)

        for skill_id in sorted(recs_by_skill.keys()):
            skill = skills_by_id[skill_id]

            f.write(f"\n{skill_id}: {skill['skill']}\n")
            f.write(f"Topic: {skill['topic']}\n")
            f.write(f"Description: {skill['description'][:200]}...\n")
            f.write(f"Current deps: {', '.join(skill['dependencies']) if skill['dependencies'] else 'None'}\n")
            f.write("\nRecommended additions:\n")

            for rec in recs_by_skill[skill_id]:
                dep_skill = skills_by_id[rec['add_dep']]
                f.write(f"  → {rec['add_dep']}: {dep_skill['skill']}\n")
                f.write(f"     Reason: {rec['reason']}\n")

            f.write("\n" + "-" * 80 + "\n")

        f.write(f"\n{'=' * 80}\n")
        f.write(f"Total recommendations: {len(valid_recommendations)}\n")

    print(f"Detailed report saved to: {detailed_file}")

if __name__ == '__main__':
    main()
