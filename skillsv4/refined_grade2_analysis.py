#!/usr/bin/env python3
"""
Refined analysis of Grade 2 skills in topics T12-T20 for missing cross-topic dependencies.
This version checks existing dependencies more carefully to avoid redundant suggestions.
"""

import re

def parse_skills(filename):
    """Parse the allskills.md file and extract all skills with their dependencies."""
    skills = {}
    current_skill = None

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith('ID: '):
            skill_id = line[4:].strip()
            current_skill = {
                'id': skill_id,
                'topic': '',
                'skill': '',
                'description': '',
                'dependencies': []
            }
            skills[skill_id] = current_skill
            i += 1
            continue

        if current_skill:
            if line.startswith('Topic: '):
                current_skill['topic'] = line[7:].strip()
            elif line.startswith('Skill: '):
                current_skill['skill'] = line[7:].strip()
            elif line.startswith('Description: '):
                current_skill['description'] = line[13:].strip()
            elif line.startswith('Dependencies:'):
                i += 1
                while i < len(lines):
                    dep_line = lines[i].strip()
                    if dep_line.startswith('* '):
                        dep_match = re.match(r'\* ([A-Z0-9.]+):', dep_line)
                        if dep_match:
                            current_skill['dependencies'].append(dep_match.group(1))
                    elif dep_line == '' or dep_line.startswith('ID: '):
                        i -= 1
                        break
                    i += 1

        i += 1

    return skills

def has_topic_dependency(skill, topic_prefix, all_skills):
    """Check if skill has any dependency from a specific topic (e.g., 'T08')."""
    for dep_id in skill['dependencies']:
        if dep_id.startswith(topic_prefix + '.'):
            return True
    return False

def has_conditional_thinking(skill, all_skills):
    """Check if skill already has conditional thinking through T01.G1.10 or T08."""
    if 'T01.G1.10' in skill['dependencies'] or 'T01.GK.06' in skill['dependencies']:
        return True
    if has_topic_dependency(skill, 'T08', all_skills):
        return True
    return False

def analyze_refined(skills):
    """Refined analysis with better dependency checking."""
    target_topics = ['T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T20']
    recommendations = []

    for skill_id, skill in skills.items():
        match = re.match(r'(T\d+)\.G2\.', skill_id)
        if not match:
            continue

        topic = match.group(1)
        if topic not in target_topics:
            continue

        desc = skill['description'].lower()

        # T12.G2.02 - Fix confusing labels
        if skill_id == 'T12.G2.02':
            if not has_topic_dependency(skill, 'T01', skills):
                recommendations.append(f"{skill_id}: Add dependency T01.G1.01 - Reason: Understanding sequences is needed before labeling sections of a plan")

        # T13.G2.01 - Fix wrong signal (already has T01.G1.06, which implies some error fixing)
        # Being conservative - T01.G1.06 is "Fix a routine with one wrong step" which is similar

        # T13.G2.04 - Add checks (like assertions/debugging)
        elif skill_id == 'T13.G2.04':
            if not has_conditional_thinking(skill, skills):
                recommendations.append(f"{skill_id}: Add dependency T08.G1.01 - Reason: Adding checks requires conditional thinking (if goal reached then show success)")

        # T14.G2.02 - Track lives
        elif skill_id == 'T14.G2.02':
            if not has_topic_dependency(skill, 'T02', skills):
                recommendations.append(f"{skill_id}: Add dependency T02.G1.01 - Reason: Tracking lives requires understanding of counting and data tracking")

        # T14.G2.03 - Level progression (already has T01.G1.01 for sequencing, needs conditional)
        elif skill_id == 'T14.G2.03':
            if not has_conditional_thinking(skill, skills):
                recommendations.append(f"{skill_id}: Add dependency T08.G1.01 - Reason: Level progression requires conditional logic (if goal touched then next level)")

        # T15.G2.01 - Fast vs slow animation
        elif skill_id == 'T15.G2.01':
            if not has_topic_dependency(skill, 'T04', skills):
                recommendations.append(f"{skill_id}: Add dependency T04.G1.01 - Reason: Comparing animation speeds requires recognizing patterns in movement sequences")

        # T15.G2.02 - Scene transitions (already has T01.G1.10 which is if/then)
        # Being conservative here

        # T15.G2.03 - Loop patterns in animation
        elif skill_id == 'T15.G2.03':
            needs_pattern = not has_topic_dependency(skill, 'T04', skills)
            needs_loop = not has_topic_dependency(skill, 'T07', skills)
            if needs_pattern:
                recommendations.append(f"{skill_id}: Add dependency T04.G2.01 - Reason: Identifying repeating animation patterns requires pattern recognition skills")
            if needs_loop:
                recommendations.append(f"{skill_id}: Add dependency T07.G1.01 - Reason: Understanding loops in animation requires loop concept understanding")

        # T16.G2.01 - Interface interactions (cause/effect)
        elif skill_id == 'T16.G2.01':
            if not has_conditional_thinking(skill, skills):
                recommendations.append(f"{skill_id}: Add dependency T08.G1.01 - Reason: UI interactions are conditional (if button pressed then action happens)")

        # T16.G2.02 - Design interface
        elif skill_id == 'T16.G2.02':
            if not has_topic_dependency(skill, 'T03', skills) and not has_topic_dependency(skill, 'T05', skills):
                recommendations.append(f"{skill_id}: Add dependency T03.G1.02 - Reason: Designing interfaces requires organizing related elements into groups")

        # T18.G2.01 - 3D views
        elif skill_id == 'T18.G2.01':
            if not has_topic_dependency(skill, 'T17', skills):
                recommendations.append(f"{skill_id}: Add dependency T17.G1.01 - Reason: Understanding 3D viewpoints builds on 2D motion and direction concepts")

        # T20.G2.01 - Repeat cards in art
        elif skill_id == 'T20.G2.01':
            if not has_topic_dependency(skill, 'T04', skills):
                recommendations.append(f"{skill_id}: Add dependency T04.G1.01 - Reason: Using repeat in art requires understanding of pattern recognition")

        # T20.G2.02 - Mirrored mosaics
        elif skill_id == 'T20.G2.02':
            if not has_topic_dependency(skill, 'T04', skills):
                recommendations.append(f"{skill_id}: Add dependency T04.G1.02 - Reason: Creating symmetrical patterns requires understanding of pattern structures")

        # T20.G2.03 - Layered patterns
        elif skill_id == 'T20.G2.03':
            if not has_topic_dependency(skill, 'T04', skills):
                recommendations.append(f"{skill_id}: Add dependency T04.G2.02 - Reason: Layering patterns requires recognizing repeated sequences in algorithms")

        # T20.G2.04 - Explain changes (cause/effect) - being conservative, already has T01.G1.04

    return recommendations

def main():
    filename = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills...")
    skills = parse_skills(filename)
    print(f"Found {len(skills)} total skills")

    print("\n" + "="*80)
    print("REFINED ANALYSIS: GRADE 2 SKILLS IN TOPICS T12-T20")
    print("="*80)

    recommendations = analyze_refined(skills)

    print("\n" + "="*80)
    print("RECOMMENDED DEPENDENCY ADDITIONS (Conservative)")
    print("="*80)
    print()

    if recommendations:
        for rec in recommendations:
            print(rec)
        print(f"\nTotal recommendations: {len(recommendations)}")
    else:
        print("No additional dependencies recommended.")

    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade2_t12_t20_refined_recommendations.txt'
    with open(output_file, 'w') as f:
        f.write("GRADE 2 CROSS-TOPIC DEPENDENCY RECOMMENDATIONS (T12-T20)\n")
        f.write("REFINED CONSERVATIVE ANALYSIS\n")
        f.write("="*80 + "\n\n")
        for rec in recommendations:
            f.write(rec + "\n")
        f.write(f"\nTotal recommendations: {len(recommendations)}\n")

    print(f"\nRecommendations saved to: {output_file}")

if __name__ == '__main__':
    main()
