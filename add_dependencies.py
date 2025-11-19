#!/usr/bin/env python3
"""
Add dependencies to G4-G8 skills in allskills.md
Target averages:
- G4: 3.64 dependencies per skill
- G5: 4.04 dependencies per skill
- G6: 4.32 dependencies per skill
- G7: 4.57 dependencies per skill
- G8: 4.88 dependencies per skill
"""

import re
from typing import List, Dict, Tuple

# Target averages
TARGETS = {
    'G4': 3.64,
    'G5': 4.04,
    'G6': 4.32,
    'G7': 4.57,
    'G8': 4.88
}

# Core G3 gateway skills that all G4+ coding skills depend on
G3_GATEWAY = [
    'T06.G3.01',  # Events
    'T07.G3.01',  # Loops
    'T08.G3.01',  # Conditionals
    'T09.G3.01'   # Variables
]

def get_dependencies_for_skill(skill_id: str, topic: str, skill_name: str, grade: str) -> List[str]:
    """Generate appropriate dependencies for a skill based on its topic, grade, and content."""
    deps = []

    # Parse skill ID
    match = re.match(r'T(\d+)\.G(\d+)\.(\d+)', skill_id)
    if not match:
        return deps

    topic_num = int(match.group(1))
    grade_num = int(match.group(2))
    skill_num = int(match.group(3))

    # For coding topics (T06+), add G3 gateway skills selectively
    # Reduce base gateway dependencies to meet lower target averages
    if topic_num >= 6:
        # Core programming topics - selective gateways
        if topic_num == 6:  # Events
            deps.extend(['T06.G3.01'])  # Only Events gateway
        elif topic_num == 7:  # Loops
            deps.extend(['T07.G3.01', 'T06.G3.01'])  # Loops + Events
        elif topic_num == 8:  # Conditionals
            deps.extend(['T08.G3.01', 'T07.G3.01'])  # Conditionals + Loops
        elif topic_num == 9:  # Variables
            deps.extend(['T09.G3.01', 'T08.G3.01'])  # Variables + Conditionals
        # Advanced topics get 2-3 selective gateways based on relevance
        elif topic_num in [10, 11, 12]:  # Text, Lists, Functions
            deps.extend(['T09.G3.01', 'T08.G3.01'])  # 2 gateways
        elif topic_num in [13, 14, 15, 16, 20]:  # Clones, 2D, Input, Sensing, Sound
            deps.extend(['T06.G3.01', 'T09.G3.01'])  # 2 gateways
        elif topic_num >= 17:  # Advanced topics (3D, AI, Data, etc)
            deps.extend(['T09.G3.01', 'T08.G3.01'])  # 2 gateways

    # Add topic-specific dependencies based on topic number

    # T01: Everyday Algorithms - foundational, minimal dependencies beyond G3
    if topic_num == 1:
        if grade_num >= 4:
            deps.append('T01.G3.01')  # G3 algorithm understanding
        if grade_num >= 5:
            deps.append(f'T01.G{grade_num-1}.01')

    # T02: Using Instructions - depends on algorithms
    elif topic_num == 2:
        deps.append('T01.G3.01')
        if grade_num >= 5:
            deps.append(f'T02.G{grade_num-1}.01')

    # T03: Debugging - depends on algorithms and instructions
    elif topic_num == 3:
        deps.extend(['T01.G3.01', 'T02.G3.01'])
        if grade_num >= 5:
            deps.append(f'T03.G{grade_num-1}.01')

    # T04: Computer Basics - mostly independent
    elif topic_num == 4:
        if grade_num >= 4:
            deps.append('T01.G3.01')  # Basic algorithm understanding
        if grade_num >= 5:
            deps.append(f'T04.G{grade_num-1}.01')

    # T05: Block Coding Basics - depends on algorithms
    elif topic_num == 5:
        deps.extend(['T01.G3.01', 'T02.G3.01'])
        if grade_num >= 5:
            deps.append(f'T05.G{grade_num-1}.01')

    # T06: Events - core programming (already has T06.G3.01)
    elif topic_num == 6:
        deps.append('T01.G3.01')  # Algorithm understanding
        if skill_num > 1:
            deps.append(f'T06.G{grade_num}.01')
        if grade_num >= 5:
            deps.append('T05.G3.01')  # Block coding basics

    # T07: Loops - core programming (already has T07.G3.01, T06.G3.01)
    elif topic_num == 7:
        deps.append('T01.G3.01')  # Algorithm understanding
        if skill_num > 1:
            deps.append(f'T07.G{grade_num}.01')

    # T08: Conditionals - core programming (already has T08.G3.01, T07.G3.01)
    elif topic_num == 8:
        deps.append('T01.G3.01')  # Algorithm understanding
        if skill_num > 1:
            deps.append(f'T08.G{grade_num}.01')

    # T09: Variables - core programming (already has T09.G3.01, T08.G3.01)
    elif topic_num == 9:
        deps.append('T01.G3.01')  # Algorithm understanding
        if skill_num > 1:
            deps.append(f'T09.G{grade_num}.01')

    # T10: Text Processing (already has T09.G3.01, T08.G3.01)
    elif topic_num == 10:
        if skill_num > 1:
            deps.append(f'T10.G{grade_num}.01')
        if grade_num >= 5:
            deps.append(f'T10.G{grade_num-1}.01')

    # T11: Lists (already has T09.G3.01, T08.G3.01)
    elif topic_num == 11:
        deps.append('T07.G3.01')  # Lists often used with loops
        if skill_num > 1:
            deps.append(f'T11.G{grade_num}.01')

    # T12: Functions (already has T09.G3.01, T08.G3.01)
    elif topic_num == 12:
        deps.append('T07.G3.01')
        if skill_num > 1:
            deps.append(f'T12.G{grade_num}.01')

    # T13: Clones (already has T06.G3.01, T09.G3.01)
    elif topic_num == 13:
        deps.append('T07.G3.01')  # Loops for multiple clones
        if grade_num >= 5:
            deps.append(f'T13.G{grade_num-1}.01')

    # T14: 2D Graphics (already has T06.G3.01, T09.G3.01)
    elif topic_num == 14:
        deps.append('T07.G3.01')  # Loops for drawing
        if skill_num > 1:
            deps.append(f'T14.G{grade_num}.01')

    # T15: Keyboard/Mouse (already has T06.G3.01, T09.G3.01)
    elif topic_num == 15:
        deps.append('T08.G3.01')  # Conditionals for input handling
        if skill_num > 1:
            deps.append(f'T15.G{grade_num}.01')

    # T16: Sensing (already has T06.G3.01, T09.G3.01)
    elif topic_num == 16:
        deps.append('T08.G3.01')  # Conditionals for sensing
        if grade_num >= 5:
            deps.append(f'T16.G{grade_num-1}.01')

    # T17: Multiplayer (already has T09.G3.01, T08.G3.01)
    elif topic_num == 17:
        deps.extend(['T06.G3.01', 'T11.G4.01'])  # Events and lists
        if skill_num > 1:
            deps.append(f'T17.G{grade_num}.01')

    # T18: 3D Modeling (already has T09.G3.01, T08.G3.01)
    elif topic_num == 18:
        deps.extend(['T14.G4.01', 'T07.G3.01'])  # 2D graphics and loops
        if skill_num > 1:
            deps.append(f'T18.G{grade_num}.01')

    # T19: 3D Physics (already has T09.G3.01, T08.G3.01)
    elif topic_num == 19:
        deps.extend(['T18.G5.01', 'T06.G3.01'])  # 3D modeling and events
        if skill_num > 1:
            deps.append(f'T19.G{grade_num}.01')

    # T20: Sound (already has T06.G3.01, T09.G3.01)
    elif topic_num == 20:
        if grade_num >= 5:
            deps.append(f'T20.G{grade_num-1}.01')

    # T21: Image AI (already has T09.G3.01, T08.G3.01)
    elif topic_num == 21:
        deps.extend(['T11.G4.01', 'T06.G3.01'])  # Lists and events
        if skill_num > 1:
            deps.append(f'T21.G{grade_num}.01')

    # T22: Text AI (already has T09.G3.01, T08.G3.01)
    elif topic_num == 22:
        deps.extend(['T10.G4.01', 'T11.G4.01'])  # Text processing and lists
        if skill_num > 1:
            deps.append(f'T22.G{grade_num}.01')

    # T23: Speech AI (already has T09.G3.01, T08.G3.01)
    elif topic_num == 23:
        deps.extend(['T22.G5.01', 'T10.G4.01'])  # Text AI and text processing
        if skill_num > 1:
            deps.append(f'T23.G{grade_num}.01')

    # T24: Pose/Hand AI (already has T09.G3.01, T08.G3.01)
    elif topic_num == 24:
        deps.extend(['T06.G3.01', 'T11.G5.01'])  # Events and lists
        if skill_num > 1:
            deps.append(f'T24.G{grade_num}.01')

    # T25: Charts (already has T09.G3.01, T08.G3.01)
    elif topic_num == 25:
        deps.extend(['T11.G4.01', 'T07.G3.01'])  # Lists and loops
        if skill_num > 1:
            deps.append(f'T25.G{grade_num}.01')

    # T26: Data Analysis (already has T09.G3.01, T08.G3.01)
    elif topic_num == 26:
        deps.extend(['T11.G5.01', 'T25.G5.01'])  # Lists and charts
        if skill_num > 1:
            deps.append(f'T26.G{grade_num}.01')

    # T27: Databases (already has T09.G3.01, T08.G3.01)
    elif topic_num == 27:
        deps.extend(['T11.G5.01', 'T10.G5.01'])  # Lists and text
        if skill_num > 1:
            deps.append(f'T27.G{grade_num}.01')

    # T28: Web Scraping (already has T09.G3.01, T08.G3.01)
    elif topic_num == 28:
        deps.extend(['T10.G5.01', 'T11.G5.01'])  # Text and lists
        if grade_num >= 7:
            deps.append(f'T28.G{grade_num-1}.01')

    # T29: APIs (already has T09.G3.01, T08.G3.01)
    elif topic_num == 29:
        deps.extend(['T10.G6.01', 'T11.G6.01'])  # Text and lists
        if skill_num > 1:
            deps.append(f'T29.G{grade_num}.01')

    # T30: Cybersecurity (already has T09.G3.01, T08.G3.01)
    elif topic_num == 30:
        deps.append('T10.G5.01')  # Text processing
        if grade_num >= 7:
            deps.append(f'T30.G{grade_num-1}.01')

    # T31: Blockchain (already has T09.G3.01, T08.G3.01)
    elif topic_num == 31:
        deps.extend(['T11.G6.01', 'T10.G6.01'])  # Lists and text
        if grade_num >= 8:
            deps.append(f'T31.G{grade_num-1}.01')

    # Trim or pad dependencies to approximate target averages
    # We'll use a strategy that varies by skill number to create natural variation
    target_base = int(TARGETS[f'G{grade_num}'])

    # Create variation: some skills have more/fewer deps than target
    # Use skill_num to create predictable but varied pattern
    # Adjust based on grade to hit specific targets
    if grade_num == 4:
        # Target 3.64 - need more 4s
        if skill_num % 3 == 0:
            target_count = 3
        elif skill_num % 5 == 0:
            target_count = 5
        else:
            target_count = 4
    elif grade_num == 5:
        # Target 4.04 - current 4.05 is perfect!
        if skill_num % 3 == 0:
            target_count = 5
        elif skill_num % 7 == 0:
            target_count = 3
        else:
            target_count = 4
    elif grade_num == 6:
        # Target 4.32 - need more 4-5 mix
        if skill_num % 2 == 0:
            target_count = 4
        elif skill_num % 7 == 0:
            target_count = 6
        else:
            target_count = 5
    elif grade_num == 7:
        # Target 4.57 - need more 5s
        if skill_num % 3 == 0:
            target_count = 4
        elif skill_num % 5 == 0:
            target_count = 6
        else:
            target_count = 5
    else:  # G8
        # Target 4.88 - need more 5s and 6s
        if skill_num % 4 == 0:
            target_count = 4
        elif skill_num % 3 == 0:
            target_count = 6
        else:
            target_count = 5

    # Ensure minimum of 2 dependencies for G4+
    target_count = max(2, target_count)

    # If we have too many dependencies, trim less critical ones
    if len(deps) > target_count + 1:
        # Keep G3 gateways and first few topic-specific deps
        critical_deps = []
        for dep in deps:
            if 'G3.01' in dep or dep.endswith('.01'):
                critical_deps.append(dep)
            elif len(critical_deps) < target_count:
                critical_deps.append(dep)
        deps = critical_deps

    # If we need more dependencies, add progressive prerequisites
    elif len(deps) < target_count:
        # Add previous grade same topic if exists and not already added
        if grade_num > 4:
            prev_grade_skill = f'T{topic_num:02d}.G{grade_num-1}.01'
            if prev_grade_skill not in deps:
                deps.append(prev_grade_skill)

        # Add related topic dependencies based on grade level
        if len(deps) < target_count:
            # Build list of potential additional dependencies
            additional = []

            # Foundational skills for all grades
            if topic_num >= 6 and 'T01.G3.01' not in deps:
                additional.append('T01.G3.01')

            # Grade 4+ enhancements
            if grade_num >= 4:
                if topic_num >= 10 and f'T09.G3.01' not in deps:
                    additional.append('T09.G3.01')
                if topic_num >= 14 and 'T07.G3.01' not in deps:
                    additional.append('T07.G3.01')

            # Grade 5+ enhancements
            if grade_num >= 5:
                if topic_num >= 14 and 'T09.G4.01' not in deps:  # Graphics needs advanced variables
                    additional.append('T09.G4.01')
                if topic_num >= 17 and 'T10.G4.01' not in deps:  # Advanced topics need text
                    additional.append('T10.G4.01')

            # Grade 6+ enhancements
            if grade_num >= 6:
                if topic_num >= 18 and 'T14.G5.01' not in deps:  # 3D needs advanced 2D
                    additional.append('T14.G5.01')
                if topic_num >= 21 and 'T11.G5.01' not in deps:  # AI needs advanced lists
                    additional.append('T11.G5.01')

            # Grade 7+ enhancements
            if grade_num >= 7:
                if topic_num >= 25 and 'T11.G6.01' not in deps:  # Data science needs advanced lists
                    additional.append('T11.G6.01')

            # Grade 8+ enhancements
            if grade_num >= 8:
                if topic_num >= 20 and 'T14.G6.01' not in deps:  # Advanced topics need advanced 2D
                    additional.append('T14.G6.01')
                if topic_num >= 25 and 'T22.G6.01' not in deps:  # Advanced data needs AI
                    additional.append('T22.G6.01')

            # Add from additional list until we reach target
            for dep in additional:
                if dep not in deps and len(deps) < target_count:
                    deps.append(dep)

    # Remove duplicates while preserving order
    seen = set()
    unique_deps = []
    for dep in deps:
        if dep not in seen and dep != skill_id:  # Don't depend on self
            seen.add(dep)
            unique_deps.append(dep)

    return unique_deps


def read_file(filepath: str) -> List[str]:
    """Read file and return lines."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.readlines()


def write_file(filepath: str, lines: List[str]):
    """Write lines to file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(lines)


def process_skills(filepath: str):
    """Process the allskills.md file and add dependencies."""
    lines = read_file(filepath)
    new_lines = []

    i = 0
    while i < len(lines):
        line = lines[i]
        new_lines.append(line)

        # Check if this is a G4-G8 skill ID
        match = re.match(r'^ID: (T\d+\.G[4-8]\.\d+)', line)
        if match:
            skill_id = match.group(1)

            # Read next lines to get Topic and Skill name
            topic = ""
            skill_name = ""
            description = ""

            j = i + 1
            while j < len(lines) and j < i + 10:
                if lines[j].startswith('Topic: '):
                    topic = lines[j].replace('Topic: ', '').strip()
                elif lines[j].startswith('Skill: '):
                    skill_name = lines[j].replace('Skill: ', '').strip()
                elif lines[j].startswith('Description: '):
                    description = lines[j].replace('Description: ', '').strip()
                    # Add remaining lines to new_lines up to description
                    for k in range(i + 1, j + 1):
                        new_lines.append(lines[k])

                    # Check if next line is already a dependency section
                    next_idx = j + 1
                    if next_idx < len(lines) and lines[next_idx].startswith('Dependency:'):
                        # Skip existing dependency section
                        while next_idx < len(lines) and (lines[next_idx].startswith('Dependency:') or lines[next_idx].startswith('* ')):
                            next_idx += 1
                        i = next_idx - 1
                    else:
                        # Generate and add dependencies
                        grade = skill_id.split('.')[1]
                        deps = get_dependencies_for_skill(skill_id, topic, skill_name, grade)

                        if deps:
                            new_lines.append('Dependency:\n')
                            for dep in deps:
                                # Find skill name for dependency
                                dep_name = find_skill_name(lines, dep)
                                new_lines.append(f'* {dep}: {dep_name}\n')

                        i = j
                    break
                j += 1

        i += 1

    write_file(filepath, new_lines)

    # Calculate and print statistics
    print_statistics(new_lines)


def find_skill_name(lines: List[str], skill_id: str) -> str:
    """Find the skill name for a given skill ID."""
    for i, line in enumerate(lines):
        if line.strip() == f'ID: {skill_id}':
            # Look for Skill: line in next few lines
            for j in range(i + 1, min(i + 5, len(lines))):
                if lines[j].startswith('Skill: '):
                    return lines[j].replace('Skill: ', '').strip()
    return 'Unknown skill'


def print_statistics(lines: List[str]):
    """Print dependency statistics by grade."""
    stats = {'G4': [], 'G5': [], 'G6': [], 'G7': [], 'G8': []}

    i = 0
    while i < len(lines):
        match = re.match(r'^ID: T\d+\.(G[4-8])\.\d+', lines[i])
        if match:
            grade = match.group(1)
            # Count dependencies
            dep_count = 0
            j = i + 1
            while j < len(lines) and j < i + 20:
                if lines[j].startswith('* '):
                    dep_count += 1
                elif lines[j].startswith('ID: '):
                    break
                j += 1
            stats[grade].append(dep_count)
        i += 1

    print("\nDependency Statistics:")
    print("-" * 50)
    for grade in ['G4', 'G5', 'G6', 'G7', 'G8']:
        if stats[grade]:
            avg = sum(stats[grade]) / len(stats[grade])
            target = TARGETS[grade]
            print(f"{grade}: {len(stats[grade])} skills, avg {avg:.2f} deps (target: {target:.2f})")
    print("-" * 50)


if __name__ == '__main__':
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    print("Adding dependencies to G4-G8 skills...")
    process_skills(filepath)
    print("Done!")
