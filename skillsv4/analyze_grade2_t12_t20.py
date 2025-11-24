#!/usr/bin/env python3
"""
Analyze Grade 2 skills in topics T12-T20 for missing cross-topic dependencies.
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

        # Check for skill ID
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
                # Read dependency lines
                i += 1
                while i < len(lines):
                    dep_line = lines[i].strip()
                    if dep_line.startswith('* '):
                        # Extract dependency ID (before colon)
                        dep_match = re.match(r'\* ([A-Z0-9.]+):', dep_line)
                        if dep_match:
                            current_skill['dependencies'].append(dep_match.group(1))
                    elif dep_line == '' or dep_line.startswith('ID: '):
                        i -= 1  # Back up one line
                        break
                    i += 1

        i += 1

    return skills

def analyze_g2_skills(skills):
    """Analyze Grade 2 skills in T12-T20 for missing dependencies."""

    # Focus on G2 skills in topics T12-T20
    target_topics = ['T12', 'T13', 'T14', 'T15', 'T16', 'T17', 'T18', 'T20']

    recommendations = []

    for skill_id, skill in skills.items():
        # Check if this is a G2 skill in target topics
        match = re.match(r'(T\d+)\.G2\.', skill_id)
        if not match:
            continue

        topic = match.group(1)
        if topic not in target_topics:
            continue

        print(f"\nAnalyzing {skill_id}: {skill['skill']}")
        print(f"  Description: {skill['description'][:100]}...")
        print(f"  Current dependencies: {skill['dependencies']}")

        # Analyze based on topic
        if topic == 'T12':  # Documentation/Organizing Programs
            analyze_t12(skill_id, skill, skills, recommendations)
        elif topic == 'T13':  # Debugging
            analyze_t13(skill_id, skill, skills, recommendations)
        elif topic == 'T14':  # Game Mechanics
            analyze_t14(skill_id, skill, skills, recommendations)
        elif topic == 'T15':  # Animation
            analyze_t15(skill_id, skill, skills, recommendations)
        elif topic == 'T16':  # UI Design
            analyze_t16(skill_id, skill, skills, recommendations)
        elif topic == 'T17':  # Motion
            analyze_t17(skill_id, skill, skills, recommendations)
        elif topic == 'T18':  # Spatial/3D
            analyze_t18(skill_id, skill, skills, recommendations)
        elif topic == 'T20':  # Generative Art
            analyze_t20(skill_id, skill, skills, recommendations)

    return recommendations

def has_dependency(skill, dep_id):
    """Check if skill already has the dependency."""
    return dep_id in skill['dependencies']

def analyze_t12(skill_id, skill, all_skills, recommendations):
    """Analyze T12 (Documentation) skills."""
    desc = skill['description'].lower()

    if skill_id == 'T12.G2.01':
        # "Add a note to explain a section of a plan" - needs sequencing
        # Already has T01.G1.01, which is good
        pass

    elif skill_id == 'T12.G2.02':
        # "Fix confusing labels on a plan" - needs T01 sequencing
        if not has_dependency(skill, 'T01.G1.01') and not has_dependency(skill, 'T01.G1.02'):
            recommendations.append(f"{skill_id}: Add dependency T01.G1.01 - Reason: Understanding sequences is needed before labeling sections of a plan")

    elif skill_id == 'T12.G2.03':
        # "Use the same style for section titles" - good with T01.G1.01
        pass

    elif skill_id == 'T12.G2.04':
        # "Group related steps under a heading" - has T03 dependencies which is perfect
        pass

def analyze_t13(skill_id, skill, all_skills, recommendations):
    """Analyze T13 (Debugging) skills."""
    desc = skill['description'].lower()

    if skill_id == 'T13.G2.01':
        # "Fix steps that use the wrong signal" - needs conditionals understanding
        # Has T01.G1.06 which is good, but might benefit from T08 conditionals
        if not has_dependency(skill, 'T08.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T08.G1.01 - Reason: Understanding signals/events requires conditional thinking (if signal X then action Y)")

    elif skill_id == 'T13.G2.02':
        # "Trace a set of steps and predict behavior" - good dependencies
        pass

    elif skill_id == 'T13.G2.03':
        # "Fix a repeated step that happens too many or too few times"
        # Has T04.G2.01 and T01.G2.01 - should also have loop understanding
        # Check if needs T07 (loops) understanding
        pass

    elif skill_id == 'T13.G2.04':
        # "Add a simple check to see if steps worked" - this is like adding assertions/debugging
        # Has T03.G1.03 and T01.G1.09 - might need conditional understanding
        if not has_dependency(skill, 'T08.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T08.G1.01 - Reason: Adding checks requires conditional thinking (if goal reached then show success)")

def analyze_t14(skill_id, skill, all_skills, recommendations):
    """Analyze T14 (Game Mechanics) skills."""
    desc = skill['description'].lower()

    if skill_id == 'T14.G2.01':
        # "Understand turns and rounds" - has T01 and T14.G1.02, good
        pass

    elif skill_id == 'T14.G2.02':
        # "Track lives and game over conditions" - tracking implies variables/counting
        # Should have T02 (Data & Variables) understanding
        if not has_dependency(skill, 'T02.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T02.G1.01 - Reason: Tracking lives requires understanding of counting and data tracking")

    elif skill_id == 'T14.G2.03':
        # "Recognize level progression" - conditional on reaching goal
        if not has_dependency(skill, 'T08.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T08.G1.01 - Reason: Level progression requires conditional logic (if goal touched then next level)")

    elif skill_id == 'T14.G2.04':
        # "Sequence a safe route" - has good dependencies
        pass

    elif skill_id == 'T14.G2.05':
        # "Adjust game difficulty settings" - has T01.G1.10 (if/then rules), good
        pass

def analyze_t15(skill_id, skill, all_skills, recommendations):
    """Analyze T15 (Animation) skills."""
    desc = skill['description'].lower()

    if skill_id == 'T15.G2.01':
        # "Fast vs. Slow animation" - timing/speed concept
        # Has T01.G1.01 - might benefit from T04 patterns
        if not has_dependency(skill, 'T04.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T04.G1.01 - Reason: Understanding animation speed requires recognizing patterns in movement sequences")

    elif skill_id == 'T15.G2.02':
        # "Identify scene transitions" - conditional/branching concept
        # Has T01.G1.10 and T01.G1.04 - should add T08 conditionals
        if not has_dependency(skill, 'T08.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T08.G1.01 - Reason: Scene transitions are conditional changes (if location changes then new scene)")

    elif skill_id == 'T15.G2.03':
        # "Loop patterns in animation" - clearly needs T04 patterns and T07 loops
        if not has_dependency(skill, 'T04.G2.01'):
            recommendations.append(f"{skill_id}: Add dependency T04.G2.01 - Reason: Identifying repeating animation patterns requires pattern recognition skills")
        if not has_dependency(skill, 'T07.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T07.G1.01 - Reason: Understanding loops in animation requires loop concept understanding")

def analyze_t16(skill_id, skill, all_skills, recommendations):
    """Analyze T16 (UI Design) skills."""
    desc = skill['description'].lower()

    if skill_id == 'T16.G2.01':
        # "Identify what happens when you interact with interfaces" - cause/effect, conditionals
        # Has T16.G1.02 - should add T08 conditionals
        if not has_dependency(skill, 'T08.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T08.G1.01 - Reason: UI interactions are conditional (if button pressed then action happens)")

    elif skill_id == 'T16.G2.02':
        # "Design a simple interface on paper" - layout/composition
        # Has T16.G2.01 - might need T05 (composition) or T03 (decomposition)
        if not has_dependency(skill, 'T05.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T05.G1.01 - Reason: Designing interfaces requires understanding of composition and character/element needs")

def analyze_t17(skill_id, skill, all_skills, recommendations):
    """Analyze T17 (Motion) skills."""
    desc = skill['description'].lower()

    if skill_id == 'T17.G2.01':
        # "Predict sprite direction from motion blocks" - spatial reasoning
        # Has T17.G1.01 - good, this is within-topic progression
        pass

def analyze_t18(skill_id, skill, all_skills, recommendations):
    """Analyze T18 (3D/Spatial) skills."""
    desc = skill['description'].lower()

    if skill_id == 'T18.G2.01':
        # "Identify front, top, and side views of 3D objects" - spatial reasoning
        # Has T18.G1.01 - might benefit from T17 2D motion understanding as foundation
        if not has_dependency(skill, 'T17.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T17.G1.01 - Reason: Understanding 3D viewpoints builds on 2D motion and direction concepts")

def analyze_t20(skill_id, skill, all_skills, recommendations):
    """Analyze T20 (Generative Art) skills."""
    desc = skill['description'].lower()

    if skill_id == 'T20.G2.01':
        # "Use repeat cards in an art recipe" - loops/patterns
        # Has T01.G1.04 - should add T04 patterns
        if not has_dependency(skill, 'T04.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T04.G1.01 - Reason: Using repeat in art requires understanding of pattern recognition")

    elif skill_id == 'T20.G2.02':
        # "Plan mirrored mosaics" - symmetry/patterns
        # Has T05.G1.01 and T01.G1.04 - should add T04 patterns
        if not has_dependency(skill, 'T04.G1.02'):
            recommendations.append(f"{skill_id}: Add dependency T04.G1.02 - Reason: Creating symmetrical patterns requires understanding of pattern structures")

    elif skill_id == 'T20.G2.03':
        # "Build layered pattern recipes" - has T20.G2.01 and T01.G2.02, good
        # Might benefit from T04 patterns
        if not has_dependency(skill, 'T04.G2.02'):
            recommendations.append(f"{skill_id}: Add dependency T04.G2.02 - Reason: Layering patterns requires recognizing repeated sequences")

    elif skill_id == 'T20.G2.04':
        # "Explain how a change affects the art" - cause/effect
        # Has T01.G1.04 and T20.G2.03 - might benefit from T08 conditionals
        if not has_dependency(skill, 'T08.G1.01'):
            recommendations.append(f"{skill_id}: Add dependency T08.G1.01 - Reason: Predicting changes requires conditional thinking (if color changes then pattern looks different)")

def main():
    filename = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Parsing skills...")
    skills = parse_skills(filename)
    print(f"Found {len(skills)} total skills")

    print("\n" + "="*80)
    print("ANALYZING GRADE 2 SKILLS IN TOPICS T12-T20")
    print("="*80)

    recommendations = analyze_g2_skills(skills)

    print("\n" + "="*80)
    print("RECOMMENDED DEPENDENCY ADDITIONS")
    print("="*80)
    print()

    if recommendations:
        for rec in recommendations:
            print(rec)
        print(f"\nTotal recommendations: {len(recommendations)}")
    else:
        print("No additional dependencies recommended.")

    # Save to file
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade2_t12_t20_recommendations.txt'
    with open(output_file, 'w') as f:
        f.write("GRADE 2 CROSS-TOPIC DEPENDENCY RECOMMENDATIONS (T12-T20)\n")
        f.write("="*80 + "\n\n")
        for rec in recommendations:
            f.write(rec + "\n")
        f.write(f"\nTotal recommendations: {len(recommendations)}\n")

    print(f"\nRecommendations saved to: {output_file}")

if __name__ == '__main__':
    main()
