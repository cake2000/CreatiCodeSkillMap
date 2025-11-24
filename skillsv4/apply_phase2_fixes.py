#!/usr/bin/env python3
"""
Apply Phase 2 validated dependency fixes to Grade K skills.
Conservative approach - only add high-confidence cross-topic dependencies.
"""

import re
from typing import Dict, List, Tuple, Set

def read_skill_file(filepath: str) -> str:
    """Read the entire skills file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_skill_file(filepath: str, content: str):
    """Write the skills file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

def parse_skills(content: str) -> Dict[str, Dict]:
    """Parse skills from content."""
    skills = {}
    skill_pattern = r'ID: (T\d+\.GK\.\d+)\s*\nTopic: ([^\n]+)\s*\nSkill: ([^\n]+)\s*\nDescription: ([^\n]+(?:\n(?!ID:|Topic:|Skill:|Description:|Dependencies:)[^\n]+)*)'
    dep_pattern = r'Dependencies:\s*\n((?:\* [^\n]+\n?)*)'

    for match in re.finditer(skill_pattern, content):
        skill_id = match.group(1)
        topic = match.group(2)
        skill_name = match.group(3)
        description = match.group(4).strip()

        # Find dependencies
        deps = []
        end_pos = match.end()
        remaining = content[end_pos:end_pos+2000]
        dep_match = re.match(r'\s*\nDependencies:\s*\n((?:\* [^\n]+\n?)*)', remaining)
        if dep_match:
            dep_text = dep_match.group(1)
            for dep_line in dep_text.strip().split('\n'):
                if dep_line.startswith('* '):
                    dep_id = dep_line.split(':')[0].replace('* ', '').strip()
                    deps.append(dep_id)

        skills[skill_id] = {
            'topic': topic,
            'name': skill_name,
            'description': description,
            'dependencies': deps,
            'match_obj': match
        }

    return skills

def get_high_confidence_additions() -> Dict[str, List[str]]:
    """
    Return only HIGH-CONFIDENCE cross-topic dependencies to add.
    Focus on clear pedagogical connections.
    """
    additions = {}

    # HIGH-CONFIDENCE: Counting skill should depend on basic counting
    # T01.GK.08 explicitly asks students to count
    additions['T01.GK.08'] = ['T09.GK.01']  # Recognize that a label can hold a number

    # HIGH-CONFIDENCE: Sequencing skills with motion should depend on basic motion
    # These explicitly involve character/sprite movement
    additions['T13.GK.01'] = ['T02.GK.01']  # Spot missing action - needs motion concepts
    additions['T14.GK.01'] = ['T02.GK.01']  # Match controls to character actions - needs motion

    # HIGH-CONFIDENCE: Interactive game skills needing foundational skills
    # T08.GK.02 involves making choices based on conditions
    additions['T08.GK.02'] = ['T06.GK.01']  # Needs event sequence understanding

    # HIGH-CONFIDENCE: Counting/comparison skills need basic counting
    additions['T10.GK.03'] = ['T09.GK.01']  # Find which group has more - needs counting
    additions['T27.GK.02'] = ['T09.GK.01']  # Compare which group has more - needs counting

    # HIGH-CONFIDENCE: Pattern recognition with counting
    additions['T26.GK.02'] = ['T09.GK.01']  # Log repeated events - needs counting concept

    return additions

def get_redundant_removals() -> Dict[str, List[str]]:
    """
    Return dependencies to remove (only truly redundant ones).
    BE VERY CONSERVATIVE - only 2 identified in analysis.
    """
    removals = {}

    # From analysis: T13.GK.02 potentially redundant on T01.GK.05 (already via T13.GK.01)
    # DECISION: Keep it - adds semantic clarity that fixing requires sequencing knowledge

    # From analysis: T13.GK.03 potentially redundant on T01.GK.03 (already via T13.GK.01)
    # DECISION: Keep it - adds semantic clarity that fixing requires finding first/last

    # NO REMOVALS - all dependencies add semantic value
    return removals

def apply_dependency_changes(content: str, additions: Dict[str, List[str]],
                            removals: Dict[str, List[str]]) -> Tuple[str, List[Dict]]:
    """Apply dependency changes to content."""
    changes_log = []

    # Parse skills
    skills = parse_skills(content)

    # Process additions
    for skill_id, new_deps in additions.items():
        if skill_id not in skills:
            print(f"WARNING: Skill {skill_id} not found")
            continue

        current_deps = skills[skill_id]['dependencies']

        for new_dep in new_deps:
            if new_dep not in skills:
                print(f"WARNING: Dependency {new_dep} does not exist")
                continue

            if new_dep in current_deps:
                print(f"INFO: {skill_id} already has {new_dep}")
                continue

            # Find the skill in content
            skill_match = skills[skill_id]['match_obj']
            skill_start = skill_match.start()
            skill_end = skill_match.end()

            # Find where to insert dependency
            next_skill_pattern = r'\n\nID: T\d+'
            next_match = re.search(next_skill_pattern, content[skill_end:skill_end+3000])

            if next_match:
                section_end = skill_end + next_match.start()
            else:
                section_end = len(content)

            skill_section = content[skill_start:section_end]

            # Check if Dependencies section exists
            if '\nDependencies:\n' in skill_section:
                # Add to existing dependencies
                dep_match = re.search(r'(Dependencies:\s*\n(?:\* [^\n]+\n)*)', skill_section)
                if dep_match:
                    dep_end_pos = skill_start + dep_match.end()
                    dep_text = skills[new_dep]['name']
                    new_line = f"* {new_dep}: {dep_text}\n"
                    content = content[:dep_end_pos] + new_line + content[dep_end_pos:]

                    changes_log.append({
                        'skill_id': skill_id,
                        'skill_name': skills[skill_id]['name'],
                        'change_type': 'ADD',
                        'dependency_id': new_dep,
                        'dependency_name': dep_text,
                        'reason': get_addition_reason(skill_id, new_dep)
                    })

                    # Update skills dict
                    skills[skill_id]['dependencies'].append(new_dep)
            else:
                # Create Dependencies section
                desc_end = skill_match.end()
                dep_text = skills[new_dep]['name']
                new_section = f"\n\nDependencies:\n* {new_dep}: {dep_text}\n"
                content = content[:desc_end] + new_section + content[desc_end:]

                changes_log.append({
                    'skill_id': skill_id,
                    'skill_name': skills[skill_id]['name'],
                    'change_type': 'ADD',
                    'dependency_id': new_dep,
                    'dependency_name': dep_text,
                    'reason': get_addition_reason(skill_id, new_dep)
                })

                # Update skills dict
                skills[skill_id]['dependencies'].append(new_dep)

    return content, changes_log

def get_addition_reason(skill_id: str, dep_id: str) -> str:
    """Get reason for adding dependency."""
    reasons = {
        ('T01.GK.08', 'T09.GK.01'): 'Skill explicitly asks students to count, requires understanding that numbers can be stored/tracked',
        ('T13.GK.01', 'T02.GK.01'): 'Spotting missing actions in animations requires understanding basic character movement',
        ('T14.GK.01', 'T02.GK.01'): 'Matching controls to character actions requires understanding basic character movement',
        ('T08.GK.02', 'T06.GK.01'): 'Making yes/no choices requires understanding event sequences',
        ('T10.GK.03', 'T09.GK.01'): 'Comparing group sizes requires basic counting and number understanding',
        ('T27.GK.02', 'T09.GK.01'): 'Comparing which group has more requires basic counting and number understanding',
        ('T26.GK.02', 'T09.GK.01'): 'Logging repeated events requires understanding how to track counts',
    }
    return reasons.get((skill_id, dep_id), 'Cross-topic prerequisite')

def validate_changes(content: str) -> Tuple[bool, List[str]]:
    """Validate no circular dependencies or X-2 violations introduced."""
    errors = []

    skills = parse_skills(content)

    # Check for circular dependencies (simple check)
    for skill_id, skill_data in skills.items():
        for dep_id in skill_data['dependencies']:
            if dep_id not in skills:
                errors.append(f"ERROR: {skill_id} depends on non-existent skill {dep_id}")
                continue

            # Check if dependency depends back on this skill (simple cycle)
            if skill_id in skills[dep_id]['dependencies']:
                errors.append(f"ERROR: Circular dependency between {skill_id} and {dep_id}")

    # Check X-2 rule for Grade K skills
    grade_k_skills = {sid: data for sid, data in skills.items() if '.GK.' in sid}

    for skill_id, skill_data in grade_k_skills.items():
        for dep_id in skill_data['dependencies']:
            if dep_id not in skills:
                continue

            # Check grade of dependency
            if '.GK.' in dep_id:
                continue  # Same grade, OK
            elif '.G1.' in dep_id:
                errors.append(f"ERROR: Grade K skill {skill_id} depends on Grade 1 skill {dep_id}")
            elif '.G2.' in dep_id:
                errors.append(f"ERROR: Grade K skill {skill_id} depends on Grade 2 skill {dep_id}")
            elif '.G3.' in dep_id:
                errors.append(f"ERROR: Grade K skill {skill_id} depends on Grade 3+ skill {dep_id}")

    return len(errors) == 0, errors

def generate_change_report(changes_log: List[Dict], output_file: str):
    """Generate detailed change report."""
    report = []
    report.append("# Grade K Phase 2: Applied Changes Report\n")
    report.append(f"**Date:** 2025-11-24\n")
    report.append(f"**Total Changes:** {len(changes_log)}\n\n")

    report.append("## Summary\n\n")
    additions = [c for c in changes_log if c['change_type'] == 'ADD']
    removals = [c for c in changes_log if c['change_type'] == 'REMOVE']

    report.append(f"- **Dependencies Added:** {len(additions)}\n")
    report.append(f"- **Dependencies Removed:** {len(removals)}\n")
    report.append(f"- **Skills Modified:** {len(set(c['skill_id'] for c in changes_log))}\n\n")

    if additions:
        report.append("## Dependencies Added\n\n")
        for change in additions:
            report.append(f"### {change['skill_id']}: {change['skill_name']}\n\n")
            report.append(f"**Added Dependency:** {change['dependency_id']} - {change['dependency_name']}\n\n")
            report.append(f"**Reasoning:** {change['reason']}\n\n")

    if removals:
        report.append("## Dependencies Removed\n\n")
        for change in removals:
            report.append(f"### {change['skill_id']}: {change['skill_name']}\n\n")
            report.append(f"**Removed Dependency:** {change['dependency_id']} - {change['dependency_name']}\n\n")
            report.append(f"**Reasoning:** {change['reason']}\n\n")

    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(report)

def main():
    input_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    report_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade_k_phase2_changes_applied.md'

    print("Reading skills file...")
    content = read_skill_file(input_file)

    print("Getting high-confidence changes...")
    additions = get_high_confidence_additions()
    removals = get_redundant_removals()

    print(f"Planned additions: {sum(len(deps) for deps in additions.values())}")
    print(f"Planned removals: {sum(len(deps) for deps in removals.values())}")

    print("\nApplying changes...")
    modified_content, changes_log = apply_dependency_changes(content, additions, removals)

    print("\nValidating changes...")
    valid, errors = validate_changes(modified_content)

    if not valid:
        print("VALIDATION ERRORS:")
        for error in errors:
            print(f"  {error}")
        return False

    print("Validation passed!")

    print("\nWriting modified file...")
    write_skill_file(output_file, modified_content)

    print("Generating change report...")
    generate_change_report(changes_log, report_file)

    print("\n=== SUMMARY ===")
    print(f"Total dependencies added: {len([c for c in changes_log if c['change_type'] == 'ADD'])}")
    print(f"Total dependencies removed: {len([c for c in changes_log if c['change_type'] == 'REMOVE'])}")
    print(f"Skills modified: {len(set(c['skill_id'] for c in changes_log))}")
    print(f"All validations passed: {valid}")

    return True

if __name__ == '__main__':
    success = main()
    exit(0 if success else 1)
