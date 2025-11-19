#!/usr/bin/env python3
"""
Generate dependencies for G4-8 skills from allskills.md

TARGET AVERAGES:
- G4: 3.64 dependencies per skill (162 skills total)
- G5: 4.04 dependencies per skill (172 skills)
- G6: 4.32 dependencies per skill (166 skills)
- G7: 4.57 dependencies per skill (168 skills)
- G8: 4.88 dependencies per skill (163 skills)

KEY GATEWAY SKILLS (G3):
- T06.G3.01: Build a green-flag script (Events)
- T07.G3.01: Use a counted repeat loop (Loops)
- T08.G3.01: Use a simple if (Conditionals)
- T09.G3.01: Create/use numeric variable (Variables - MOST CRITICAL)
"""

import re
from typing import List, Dict, Set
from collections import defaultdict

# Gateway skills that coding skills should reference
GATEWAY_SKILLS = {
    'events': 'T06.G3.01',
    'loops': 'T07.G3.01',
    'conditionals': 'T08.G3.01',
    'variables': 'T09.G3.01'
}

# Topic definitions for cross-topic dependencies
TOPIC_INFO = {
    'T01': {'name': 'Everyday Algorithms', 'foundational': True},
    'T02': {'name': 'Algorithm Diagrams', 'foundational': True},
    'T03': {'name': 'Problem Decomposition', 'foundational': True},
    'T04': {'name': 'Algorithm Patterns', 'foundational': True},
    'T05': {'name': 'Human-Centered Design', 'foundational': False},
    'T06': {'name': 'Events & Sequences', 'foundational': True, 'coding': True},
    'T07': {'name': 'Loops', 'foundational': True, 'coding': True},
    'T08': {'name': 'Conditions & Logic', 'foundational': True, 'coding': True},
    'T09': {'name': 'Variables & Expressions', 'foundational': True, 'coding': True},
    'T10': {'name': 'Lists & Tables', 'foundational': True, 'coding': True},
    'T11': {'name': 'Functions & Procedures', 'foundational': True, 'coding': True},
    'T12': {'name': 'Organizing Programs', 'foundational': True, 'coding': True},
    'T13': {'name': 'Testing, Debugging & Error Handling', 'foundational': True, 'coding': True},
    'T14': {'name': '2D Games', 'foundational': False, 'coding': True, 'requires': ['T06', 'T07', 'T08', 'T09']},
    'T15': {'name': 'Stories & Animation', 'foundational': False, 'coding': True, 'requires': ['T06', 'T07']},
    'T16': {'name': 'User Interfaces', 'foundational': False, 'coding': True, 'requires': ['T06', 'T08', 'T09']},
    'T17': {'name': '2D Motion & Physics', 'foundational': False, 'coding': True, 'requires': ['T06', 'T07', 'T08', 'T09']},
    'T18': {'name': '3D Worlds & Games', 'foundational': False, 'coding': True, 'requires': ['T14', 'T07', 'T09', 'T10']},
    'T19': {'name': 'Multiplayer Apps', 'foundational': False, 'coding': True, 'requires': ['T06', 'T09', 'T10', 'T31']},
    'T20': {'name': 'Algorithmic Art & Creative Coding', 'foundational': False, 'coding': True, 'requires': ['T07', 'T09', 'T28']},
    'T21': {'name': 'AI Media', 'foundational': False, 'coding': True, 'requires': ['T09', 'T10', 'T29']},
    'T22': {'name': 'Chatbots & Prompting', 'foundational': False, 'coding': True, 'requires': ['T06', 'T09', 'T10', 'T29']},
    'T23': {'name': 'AI Perception', 'foundational': False, 'coding': True, 'requires': ['T06', 'T08', 'T09']},
    'T24': {'name': 'XO & Generative AI Practices', 'foundational': False, 'coding': True, 'requires': ['T09', 'T10']},
    'T25': {'name': 'Data Representation', 'foundational': True, 'coding': False},
    'T26': {'name': 'Data Collection & Logging', 'foundational': False, 'coding': True, 'requires': ['T09', 'T10']},
    'T27': {'name': 'Data Analysis & Storytelling', 'foundational': False, 'coding': True, 'requires': ['T09', 'T10', 'T26']},
    'T28': {'name': 'Chance & Simulations', 'foundational': False, 'coding': True, 'requires': ['T07', 'T09']},
    'T29': {'name': 'Text Data & NLP Foundations', 'foundational': False, 'coding': True, 'requires': ['T09', 'T10']},
    'T30': {'name': 'Devices & Hardware Systems', 'foundational': False, 'coding': False},
    'T31': {'name': 'Internet & Cloud', 'foundational': False, 'coding': False},
    'T32': {'name': 'Cybersecurity & Digital Safety', 'foundational': False, 'coding': False},
    'T33': {'name': 'Connected Services & Tool Wrappers', 'foundational': False, 'coding': True, 'requires': ['T09', 'T10', 'T31']},
    'T34': {'name': 'Computing History', 'foundational': False, 'coding': False},
    'T35': {'name': 'Impacts & Ethics', 'foundational': False, 'coding': False},
    'T36': {'name': 'Careers, Collaboration & Future Paths', 'foundational': False, 'coding': False}
}


class Skill:
    def __init__(self, skill_id: str, topic: str, skill_name: str, description: str):
        self.id = skill_id
        self.topic = topic
        self.skill_name = skill_name
        self.description = description
        self.dependencies: List[str] = []

        # Parse grade from ID (e.g., T01.G4.01 -> G4)
        match = re.search(r'\.(G\d|GK)\.', skill_id)
        self.grade = match.group(1) if match else None

        # Parse topic code (e.g., T01.G4.01 -> T01)
        match = re.search(r'^(T\d+)\.', skill_id)
        self.topic_code = match.group(1) if match else None

    def __repr__(self):
        return f"Skill({self.id})"


def parse_allskills(filepath: str) -> Dict[str, Skill]:
    """Parse allskills.md and return dict of skill_id -> Skill"""
    skills = {}
    current_skill = None

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith('ID: '):
            skill_id = line[4:].strip()
            topic = ""
            skill_name = ""
            description = ""

            # Read next lines for topic, skill, description
            i += 1
            if i < len(lines) and lines[i].strip().startswith('Topic: '):
                topic = lines[i].strip()[7:].strip()

            i += 1
            if i < len(lines) and lines[i].strip().startswith('Skill: '):
                skill_name = lines[i].strip()[7:].strip()

            i += 1
            if i < len(lines) and lines[i].strip().startswith('Description: '):
                description = lines[i].strip()[13:].strip()

            current_skill = Skill(skill_id, topic, skill_name, description)
            skills[skill_id] = current_skill

        i += 1

    return skills


def is_coding_skill(skill: Skill) -> bool:
    """Determine if a skill is a coding skill based on topic and description"""
    if not skill.topic_code:
        return False

    topic_info = TOPIC_INFO.get(skill.topic_code, {})

    # Explicitly coding topics
    if topic_info.get('coding', False):
        return True

    # Check description for coding keywords
    desc_lower = skill.description.lower()
    coding_keywords = ['script', 'code', 'program', 'block', 'sprite', 'loop', 'variable',
                       'if then', 'function', 'procedure', 'event', 'costume', 'sound']

    return any(keyword in desc_lower for keyword in coding_keywords)


def get_same_topic_prerequisites(skill: Skill, all_skills: Dict[str, Skill]) -> List[str]:
    """Get skills from same topic and earlier grades"""
    prereqs = []

    if not skill.grade or not skill.topic_code:
        return prereqs

    # Grade progression: GK -> G1 -> G2 -> G3 -> G4 -> G5 -> G6 -> G7 -> G8
    grade_order = ['GK', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8']

    try:
        current_grade_idx = grade_order.index(skill.grade)
    except ValueError:
        return prereqs

    # Look for skills in same topic from earlier grades
    for other_id, other_skill in all_skills.items():
        if other_skill.topic_code == skill.topic_code and other_skill.grade:
            try:
                other_grade_idx = grade_order.index(other_skill.grade)
                if other_grade_idx < current_grade_idx:
                    prereqs.append(other_id)
            except ValueError:
                continue

    return prereqs


def get_gateway_dependencies(skill: Skill) -> List[str]:
    """Get gateway skills needed based on skill type"""
    deps = []

    if not is_coding_skill(skill):
        return deps

    desc_lower = skill.description.lower()

    # Variables are critical - almost all coding skills need them
    if any(word in desc_lower for word in ['variable', 'score', 'count', 'track', 'store', 'value']):
        deps.append(GATEWAY_SKILLS['variables'])

    # Loops
    if any(word in desc_lower for word in ['loop', 'repeat', 'iteration', 'times', 'foreach']):
        if GATEWAY_SKILLS['loops'] not in deps:
            deps.append(GATEWAY_SKILLS['loops'])

    # Conditionals
    if any(word in desc_lower for word in ['if', 'condition', 'when', 'check', 'compare', 'decision']):
        if GATEWAY_SKILLS['conditionals'] not in deps:
            deps.append(GATEWAY_SKILLS['conditionals'])

    # Events (nearly all coding skills need this)
    if 'script' in desc_lower or 'program' in desc_lower or 'event' in desc_lower:
        if GATEWAY_SKILLS['events'] not in deps:
            deps.append(GATEWAY_SKILLS['events'])

    # Default: if coding skill but no specific keywords, still needs events and variables
    if not deps and is_coding_skill(skill):
        deps.append(GATEWAY_SKILLS['events'])
        if skill.grade not in ['G4']:  # G4 might not always need variables
            deps.append(GATEWAY_SKILLS['variables'])

    return deps


def get_cross_topic_dependencies(skill: Skill, all_skills: Dict[str, Skill]) -> List[str]:
    """Get dependencies from other topics based on topic requirements"""
    deps = []

    if not skill.topic_code:
        return deps

    topic_info = TOPIC_INFO.get(skill.topic_code, {})
    required_topics = topic_info.get('requires', [])

    # Grade progression for finding appropriate prereqs
    grade_order = ['GK', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8']

    try:
        current_grade_idx = grade_order.index(skill.grade)
    except (ValueError, TypeError):
        return deps

    for req_topic in required_topics:
        # Find skills from required topic at earlier or same grade
        candidates = []
        for other_id, other_skill in all_skills.items():
            if other_skill.topic_code == req_topic and other_skill.grade:
                try:
                    other_grade_idx = grade_order.index(other_skill.grade)
                    # Prefer G3 gateway skills or skills from immediately prior grade
                    if other_grade_idx == grade_order.index('G3'):
                        candidates.insert(0, other_id)  # Prioritize G3
                    elif other_grade_idx < current_grade_idx and other_grade_idx >= grade_order.index('G3'):
                        candidates.append(other_id)
                except ValueError:
                    continue

        # Add the best candidate from this topic
        if candidates and candidates[0] not in deps:
            deps.append(candidates[0])

    # Special case: 3D skills (T18) should reference 2D games (T14)
    if skill.topic_code == 'T18':
        found_t14 = False
        # First try to find T14 skills from earlier grades
        for other_id, other_skill in all_skills.items():
            if other_skill.topic_code == 'T14' and other_skill.grade:
                try:
                    other_grade_idx = grade_order.index(other_skill.grade)
                    if other_grade_idx < current_grade_idx and other_grade_idx >= grade_order.index('G3'):
                        if other_id not in deps:
                            deps.append(other_id)
                            found_t14 = True
                            break
                except ValueError:
                    continue

    # Special case: Multiplayer (T19) needs events + variables + lists
    if skill.topic_code == 'T19':
        key_topics = ['T06', 'T09', 'T10']
        for req_topic in key_topics:
            if req_topic not in required_topics:
                for other_id, other_skill in all_skills.items():
                    if other_skill.topic_code == req_topic and other_skill.grade == 'G3':
                        if other_id not in deps:
                            deps.append(other_id)
                            break

    return deps


def get_foundational_dependencies(skill: Skill, all_skills: Dict[str, Skill]) -> List[str]:
    """Get dependencies from foundational topics (T01-T05) based on skill content"""
    deps = []

    desc_lower = skill.description.lower()

    # T01 - Everyday Algorithms (algorithm thinking)
    if any(word in desc_lower for word in ['algorithm', 'steps', 'sequence', 'plan', 'trace']):
        # Find relevant G3 T01 skill
        for other_id, other_skill in all_skills.items():
            if other_skill.topic_code == 'T01' and other_skill.grade == 'G3':
                if other_id not in deps and len(deps) < 2:
                    deps.append(other_id)

    # T02 - Algorithm Diagrams
    if any(word in desc_lower for word in ['flowchart', 'diagram', 'pseudocode']):
        for other_id, other_skill in all_skills.items():
            if other_skill.topic_code == 'T02' and other_skill.grade in ['G3', 'G4']:
                if other_id not in deps:
                    deps.append(other_id)
                    break

    # T03 - Problem Decomposition
    if any(word in desc_lower for word in ['decompose', 'break down', 'sub-problem', 'helper']):
        for other_id, other_skill in all_skills.items():
            if other_skill.topic_code == 'T03' and other_skill.grade in ['G3', 'G4']:
                if other_id not in deps:
                    deps.append(other_id)
                    break

    # T04 - Algorithm Patterns
    if any(word in desc_lower for word in ['pattern', 'search', 'sort', 'find']):
        for other_id, other_skill in all_skills.items():
            if other_skill.topic_code == 'T04' and other_skill.grade in ['G2', 'G3']:
                if other_id not in deps:
                    deps.append(other_id)
                    break

    return deps


def generate_dependencies(skill: Skill, all_skills: Dict[str, Skill]) -> List[str]:
    """Generate dependencies for a single skill"""
    deps = set()

    # Skip if not G4-8
    if not skill.grade or skill.grade not in ['G4', 'G5', 'G6', 'G7', 'G8']:
        return []

    # 1. Gateway skills (for coding skills)
    gateway_deps = get_gateway_dependencies(skill)
    deps.update(gateway_deps)

    # 2. Same-topic prerequisites (immediate predecessor from same topic)
    same_topic_deps = get_same_topic_prerequisites(skill, all_skills)
    # Select 1-2 most recent from same topic
    if same_topic_deps:
        same_topic_deps.sort()
        deps.update(same_topic_deps[-2:])  # Last 2 skills from same topic

    # 3. Cross-topic dependencies
    cross_topic_deps = get_cross_topic_dependencies(skill, all_skills)
    deps.update(cross_topic_deps)

    # 4. Foundational dependencies
    foundational_deps = get_foundational_dependencies(skill, all_skills)
    deps.update(foundational_deps[:2])  # Limit foundational to 2

    # Target dependency counts to match desired averages
    # We'll use a range to allow variation
    target_ranges = {
        'G4': (3, 4),   # Target 3.64 avg
        'G5': (4, 5),   # Target 4.04 avg
        'G6': (4, 5),   # Target 4.32 avg
        'G7': (4, 5),   # Target 4.57 avg
        'G8': (5, 6)    # Target 4.88 avg
    }

    # Vary target based on skill complexity
    min_target, max_target = target_ranges.get(skill.grade, (4, 5))

    # More complex topics get more dependencies
    if skill.topic_code in ['T18', 'T19', 'T21', 'T22', 'T23', 'T24', 'T27', 'T33']:
        target = max_target
    elif skill.topic_code in ['T14', 'T15', 'T16', 'T17', 'T20', 'T26', 'T28', 'T29']:
        target = (min_target + max_target) // 2 + 1
    else:
        target = min_target

    # Ensure we don't self-reference
    deps.discard(skill.id)

    # Adjust to target count
    deps_list = list(deps)

    # If too few, add more same-topic or foundational skills
    if len(deps_list) < target:
        # Try adding more same-topic skills first
        available_same_topic = [d for d in same_topic_deps if d not in deps_list]
        for dep_id in available_same_topic[:target - len(deps_list)]:
            deps_list.append(dep_id)

        # Still need more? Add more foundational
        if len(deps_list) < target:
            available_foundational = [d for d in foundational_deps if d not in deps_list]
            for dep_id in available_foundational[:target - len(deps_list)]:
                deps_list.append(dep_id)

        # Still need more? Add more cross-topic
        if len(deps_list) < target:
            available_cross = [d for d in cross_topic_deps if d not in deps_list]
            for dep_id in available_cross[:target - len(deps_list)]:
                deps_list.append(dep_id)

    # If too many, prioritize gateway > cross-topic > same-topic > foundational
    if len(deps_list) > target:
        # Keep all gateway skills (they're essential)
        keep = [d for d in deps_list if d in gateway_deps]

        # Add most important cross-topic (from required topics)
        remaining_cross = [d for d in deps_list if d in cross_topic_deps and d not in keep]
        needed = max(0, target - len(keep))
        keep.extend(remaining_cross[:min(needed, 2)])

        # Add most recent same-topic skills
        remaining_same = [d for d in deps_list if d in same_topic_deps and d not in keep]
        remaining_same.sort()  # Sort by ID
        needed = max(0, target - len(keep))
        keep.extend(remaining_same[-needed:])  # Take most recent

        # Fill remaining with foundational if still under target
        if len(keep) < target:
            remaining_found = [d for d in deps_list if d in foundational_deps and d not in keep]
            needed = target - len(keep)
            keep.extend(remaining_found[:needed])

        deps_list = keep

    return sorted(deps_list)


def write_output(skills: Dict[str, Skill], output_path: str):
    """Write skills with dependencies to output file"""

    # Filter G4-8 skills
    g4_8_skills = {k: v for k, v in skills.items()
                   if v.grade in ['G4', 'G5', 'G6', 'G7', 'G8']}

    # Sort by ID
    sorted_skills = sorted(g4_8_skills.items(), key=lambda x: x[0])

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# G4-8 Skills with Dependencies\n\n")
        f.write("Generated from allskills.md\n\n")

        stats = defaultdict(lambda: {'count': 0, 'total_deps': 0})

        for skill_id, skill in sorted_skills:
            f.write(f"\nID: {skill.id}\n")
            f.write(f"Topic: {skill.topic}\n")
            f.write(f"Skill: {skill.skill_name}\n")
            f.write(f"Description: {skill.description}\n")

            if skill.dependencies:
                f.write("Dependencies:\n")
                for dep_id in skill.dependencies:
                    dep_skill = skills.get(dep_id)
                    if dep_skill:
                        f.write(f"* {dep_id}: {dep_skill.skill_name}\n")
                    else:
                        f.write(f"* {dep_id}\n")

                # Track stats
                stats[skill.grade]['count'] += 1
                stats[skill.grade]['total_deps'] += len(skill.dependencies)
            else:
                stats[skill.grade]['count'] += 1

        # Write statistics
        f.write("\n\n# Statistics\n\n")
        for grade in ['G4', 'G5', 'G6', 'G7', 'G8']:
            if stats[grade]['count'] > 0:
                avg = stats[grade]['total_deps'] / stats[grade]['count']
                f.write(f"{grade}: {stats[grade]['count']} skills, ")
                f.write(f"{stats[grade]['total_deps']} total dependencies, ")
                f.write(f"{avg:.2f} average dependencies per skill\n")


def balance_dependencies(skills: Dict[str, Skill], target_avgs: Dict[str, float]):
    """Second pass to balance dependencies to hit exact target averages"""

    for grade in ['G4', 'G5', 'G6', 'G7', 'G8']:
        grade_skills = [s for s in skills.values() if s.grade == grade]
        if not grade_skills:
            continue

        target_avg = target_avgs[grade]
        target_total = int(len(grade_skills) * target_avg)

        current_total = sum(len(s.dependencies) for s in grade_skills)
        diff = target_total - current_total

        print(f"  {grade}: current={current_total}, target={target_total}, diff={diff}")

        # If we need to add dependencies
        if diff > 0:
            # Find skills with fewer dependencies
            candidates = sorted(grade_skills, key=lambda s: len(s.dependencies))
            for skill in candidates[:diff]:
                # Get all available same-topic and foundational deps
                all_other = get_same_topic_prerequisites(skill, skills)
                all_other.extend(get_foundational_dependencies(skill, skills))

                # Add one more dependency
                for dep_id in all_other:
                    if dep_id not in skill.dependencies:
                        skill.dependencies.append(dep_id)
                        skill.dependencies.sort()
                        break

        # If we need to remove dependencies
        elif diff < 0:
            # Find skills with more dependencies
            candidates = sorted(grade_skills, key=lambda s: len(s.dependencies), reverse=True)
            for skill in candidates[:abs(diff)]:
                if len(skill.dependencies) > 2:  # Keep at least 2
                    # Remove least critical dependency (foundational, not gateway)
                    gateway_ids = list(GATEWAY_SKILLS.values())
                    for dep_id in reversed(skill.dependencies):
                        if dep_id not in gateway_ids:
                            skill.dependencies.remove(dep_id)
                            break


def main():
    input_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g4-8_skills_with_dependencies.md'

    print("Parsing allskills.md...")
    skills = parse_allskills(input_file)
    print(f"Parsed {len(skills)} skills")

    # Count G4-8 skills
    g4_8_count = sum(1 for s in skills.values() if s.grade in ['G4', 'G5', 'G6', 'G7', 'G8'])
    print(f"Found {g4_8_count} G4-8 skills")

    print("\nGenerating dependencies (first pass)...")
    for skill_id, skill in skills.items():
        if skill.grade in ['G4', 'G5', 'G6', 'G7', 'G8']:
            skill.dependencies = generate_dependencies(skill, skills)

    # Target averages
    target_avgs = {
        'G4': 3.64,
        'G5': 4.04,
        'G6': 4.32,
        'G7': 4.57,
        'G8': 4.88
    }

    print("\nBalancing to target averages (second pass)...")
    balance_dependencies(skills, target_avgs)

    print("\nWriting output...")
    write_output(skills, output_file)

    print(f"\nDone! Output written to: {output_file}")

    # Print summary statistics
    stats = defaultdict(lambda: {'count': 0, 'total_deps': 0})
    for skill in skills.values():
        if skill.grade in ['G4', 'G5', 'G6', 'G7', 'G8']:
            stats[skill.grade]['count'] += 1
            stats[skill.grade]['total_deps'] += len(skill.dependencies)

    print("\nFinal Summary Statistics:")
    for grade in ['G4', 'G5', 'G6', 'G7', 'G8']:
        if stats[grade]['count'] > 0:
            avg = stats[grade]['total_deps'] / stats[grade]['count']
            target = target_avgs[grade]
            print(f"{grade}: {stats[grade]['count']} skills, {avg:.2f} avg dependencies (target: {target:.2f})")


if __name__ == '__main__':
    main()
