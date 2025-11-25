#!/usr/bin/env python3
"""
Grade 8 Dependency Analysis and Fix Script
Phase 2: Cross-topic dependencies and grade-level coherence
"""

import re
import json
from collections import defaultdict
from typing import Dict, List, Set, Tuple

def parse_skills(content: str) -> Dict[str, Dict]:
    """Parse all skills from the markdown content."""
    skills = {}

    # Split by ID: pattern
    skill_blocks = re.split(r'\n(?=ID: )', content)

    for block in skill_blocks:
        if not block.strip() or not block.startswith('ID: '):
            continue

        lines = block.strip().split('\n')
        skill_id = None
        topic = None
        skill_name = None
        description = None
        dependencies = []

        in_deps = False
        dep_lines = []

        for line in lines:
            if line.startswith('ID: '):
                skill_id = line.replace('ID: ', '').strip()
            elif line.startswith('Topic: '):
                topic = line.replace('Topic: ', '').strip()
            elif line.startswith('Skill: '):
                skill_name = line.replace('Skill: ', '').strip()
            elif line.startswith('Description: '):
                description = line.replace('Description: ', '').strip()
            elif line.startswith('Dependencies:'):
                in_deps = True
            elif in_deps and line.startswith('* '):
                # Parse dependency
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
                'topic': topic,
                'name': skill_name,
                'description': description,
                'dependencies': dependencies,
                'original_block': block
            }

    return skills

def get_grade(skill_id: str) -> str:
    """Extract grade from skill ID (e.g., 'T01.G8.01' -> 'G8')."""
    match = re.search(r'\.(G\d+|GK)\.', skill_id)
    if match:
        return match.group(1)
    return None

def get_topic(skill_id: str) -> str:
    """Extract topic from skill ID (e.g., 'T01.G8.01' -> 'T01')."""
    match = re.match(r'(T\d+)\.', skill_id)
    if match:
        return match.group(1)
    return None

def check_x2_rule(skill_grade: str, dep_grade: str) -> bool:
    """Check if dependency satisfies X-2 rule."""
    grade_order = ['GK', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8']

    if skill_grade not in grade_order or dep_grade not in grade_order:
        return True  # Can't check, assume OK

    skill_idx = grade_order.index(skill_grade)
    dep_idx = grade_order.index(dep_grade)

    # Dependency should not be more than 2 grades below
    return (skill_idx - dep_idx) <= 2

def find_circular_dependencies(skills: Dict[str, Dict]) -> List[List[str]]:
    """Find circular dependency chains."""
    def has_path(start: str, end: str, visited: Set[str]) -> bool:
        if start == end:
            return True
        if start in visited:
            return False
        visited.add(start)

        if start not in skills:
            return False

        for dep in skills[start]['dependencies']:
            if has_path(dep['id'], end, visited.copy()):
                return True
        return False

    cycles = []
    for skill_id in skills:
        for dep in skills[skill_id]['dependencies']:
            if has_path(dep['id'], skill_id, set()):
                cycles.append([skill_id, dep['id']])

    return cycles

def find_transitive_redundancy(skills: Dict[str, Dict], skill_id: str) -> List[str]:
    """Find dependencies that are redundant due to transitive relations."""
    if skill_id not in skills:
        return []

    direct_deps = {dep['id'] for dep in skills[skill_id]['dependencies']}
    if len(direct_deps) <= 1:
        return []

    # For each dependency, find all its transitive dependencies
    redundant = []
    for dep_id in direct_deps:
        if dep_id not in skills:
            continue

        # Get all transitive deps from this dependency
        transitive = set()
        to_visit = [dep_id]
        visited = set()

        while to_visit:
            current = to_visit.pop(0)
            if current in visited or current not in skills:
                continue
            visited.add(current)

            for sub_dep in skills[current]['dependencies']:
                transitive.add(sub_dep['id'])
                to_visit.append(sub_dep['id'])

        # Check if any other direct dependency is in transitive set
        for other_dep in direct_deps:
            if other_dep != dep_id and other_dep in transitive:
                redundant.append(other_dep)

    return list(set(redundant))

def get_cross_topic_suggestions(skills: Dict[str, Dict], skill_id: str) -> List[str]:
    """Suggest cross-topic dependencies based on skill content."""
    if skill_id not in skills:
        return []

    skill = skills[skill_id]
    description = (skill['description'] or '').lower()
    name = (skill['name'] or '').lower()
    current_topic = get_topic(skill_id)
    current_grade = get_grade(skill_id)

    suggestions = []

    # Topic mapping for common cross-topic dependencies
    topic_keywords = {
        'T02': ['motion', 'move', 'sprite', 'position', 'coordinate', 'direction'],
        'T03': ['look', 'appearance', 'costume', 'show', 'hide', 'size', 'effect'],
        'T04': ['sound', 'audio', 'music', 'play', 'volume'],
        'T05': ['event', 'when', 'broadcast', 'message', 'trigger'],
        'T06': ['loop', 'repeat', 'forever', 'times', 'until'],
        'T07': ['variable', 'data', 'store', 'change', 'set'],
        'T08': ['list', 'array', 'item', 'add', 'delete', 'contains'],
        'T09': ['custom block', 'procedure', 'function', 'define', 'call'],
        'T10': ['condition', 'if', 'else', 'compare', 'boolean'],
        'T11': ['sensor', 'detect', 'touch', 'edge', 'collision'],
        'T12': ['clone', 'create', 'delete', 'instance'],
        'T13': ['pen', 'draw', 'line', 'stamp', 'color'],
        'T14': ['operator', 'math', 'calculate', 'random', 'arithmetic'],
        'T15': ['string', 'text', 'letter', 'word', 'concatenate'],
        'T16': ['animation', 'sprite', 'smooth', 'tween', 'sequence'],
        'T17': ['game', 'score', 'level', 'player', 'enemy'],
        'T18': ['physics', 'gravity', 'velocity', 'force', 'collision'],
        'T19': ['camera', 'video', 'motion', 'sensing'],
        'T20': ['tts', 'speech', 'text to speech', 'voice'],
        'T21': ['translate', 'language', 'translation'],
        'T22': ['ai', 'machine learning', 'model', 'train', 'predict'],
        'T23': ['image', 'vision', 'classify', 'detect', 'recognize'],
        'T24': ['chatbot', 'conversation', 'dialog', 'response'],
        'T25': ['3d', 'three dimensional', 'rotation', 'axis', 'perspective'],
        'T26': ['ui', 'interface', 'button', 'menu', 'widget'],
        'T27': ['data viz', 'chart', 'graph', 'plot', 'visualize'],
        'T28': ['database', 'store', 'retrieve', 'query', 'record'],
        'T29': ['api', 'request', 'response', 'web service', 'endpoint'],
        'T30': ['iot', 'sensor', 'device', 'hardware', 'microcontroller'],
        'T31': ['parallel', 'concurrent', 'simultaneous', 'thread'],
        'T32': ['debug', 'test', 'error', 'fix', 'trace'],
        'T33': ['optimize', 'performance', 'efficient', 'speed'],
        'T34': ['collab', 'team', 'share', 'merge', 'version'],
        'T35': ['design', 'plan', 'prototype', 'sketch', 'wireframe'],
        'T36': ['document', 'comment', 'explain', 'readme']
    }

    # Check for keyword matches
    for topic, keywords in topic_keywords.items():
        if topic == current_topic:
            continue

        for keyword in keywords:
            if keyword in description or keyword in name:
                # Find a relevant skill from that topic at same or lower grade
                for other_id, other_skill in skills.items():
                    if get_topic(other_id) == topic:
                        other_grade = get_grade(other_id)
                        if other_grade and current_grade:
                            if check_x2_rule(current_grade, other_grade):
                                # Check if already a dependency
                                is_existing = any(d['id'] == other_id for d in skill['dependencies'])
                                if not is_existing:
                                    suggestions.append(other_id)
                                    break  # Only suggest one per topic
                break

    return suggestions[:5]  # Limit suggestions

def analyze_and_fix_g8(content: str) -> Tuple[str, Dict]:
    """Main analysis and fix function for Grade 8 skills."""
    skills = parse_skills(content)

    # Filter for Grade 8 skills
    g8_skills = {sid: skill for sid, skill in skills.items() if get_grade(sid) == 'G8'}

    print(f"Total Grade 8 skills found: {len(g8_skills)}")

    changes = {
        'x2_violations': [],
        'cross_topic_adds': [],
        'circular_fixes': [],
        'redundancy_removes': [],
        'total_changes': 0
    }

    # Track changes for each skill
    skill_changes = {}

    # 1. Fix X-2 rule violations
    print("\n=== Checking X-2 Rule Violations ===")
    for skill_id, skill in g8_skills.items():
        violations = []
        for dep in skill['dependencies']:
            dep_id = dep['id']
            dep_grade = get_grade(dep_id)
            if dep_grade and not check_x2_rule('G8', dep_grade):
                violations.append(dep_id)

        if violations:
            print(f"{skill_id}: Found {len(violations)} violations: {violations}")
            changes['x2_violations'].append({
                'skill_id': skill_id,
                'violations': violations,
                'action': 'Flag for manual review - need scaffolding skills'
            })

            if skill_id not in skill_changes:
                skill_changes[skill_id] = {'removes': [], 'adds': [], 'reasons': []}

            for v in violations:
                skill_changes[skill_id]['reasons'].append(f"X-2 violation: dependency on {v}")

    # 2. Check for cross-topic dependencies
    print("\n=== Analyzing Cross-Topic Dependencies ===")
    for skill_id, skill in g8_skills.items():
        current_topic = get_topic(skill_id)
        current_deps = {dep['id'] for dep in skill['dependencies']}

        # Check what topics are already covered
        dep_topics = {get_topic(dep_id) for dep_id in current_deps if get_topic(dep_id)}

        # Get suggestions
        suggestions = get_cross_topic_suggestions(skills, skill_id)

        if suggestions:
            print(f"{skill_id}: Suggested cross-topic deps: {suggestions[:3]}")

            if skill_id not in skill_changes:
                skill_changes[skill_id] = {'removes': [], 'adds': [], 'reasons': []}

            for sugg in suggestions[:3]:  # Limit to top 3
                if sugg not in current_deps and sugg in skills:
                    skill_changes[skill_id]['adds'].append({
                        'id': sugg,
                        'name': skills[sugg]['name']
                    })
                    skill_changes[skill_id]['reasons'].append(f"Cross-topic: Added {sugg} from {get_topic(sugg)}")
                    changes['cross_topic_adds'].append({
                        'skill_id': skill_id,
                        'added': sugg,
                        'reason': 'Content analysis suggests dependency'
                    })

    # 3. Check for circular dependencies
    print("\n=== Checking Circular Dependencies ===")
    cycles = find_circular_dependencies(g8_skills)
    if cycles:
        print(f"Found {len(cycles)} potential cycles")
        for cycle in cycles[:10]:
            print(f"  Cycle: {cycle}")
            changes['circular_fixes'].append({
                'cycle': cycle,
                'action': 'Flag for manual review'
            })

    # 4. Check for transitive redundancy (conservative)
    print("\n=== Checking Transitive Redundancy ===")
    for skill_id, skill in g8_skills.items():
        redundant = find_transitive_redundancy(skills, skill_id)
        if redundant:
            print(f"{skill_id}: Potential redundant deps: {redundant}")
            # Be VERY conservative - only flag, don't auto-remove
            changes['redundancy_removes'].append({
                'skill_id': skill_id,
                'redundant': redundant,
                'action': 'Flag for manual review - may be needed for direct teaching'
            })

    # Calculate total changes
    changes['total_changes'] = (
        len(changes['x2_violations']) +
        len(changes['cross_topic_adds']) +
        len(changes['circular_fixes']) +
        len(changes['redundancy_removes'])
    )

    # Apply changes to content
    modified_content = content
    for skill_id, modifications in skill_changes.items():
        if skill_id not in skills:
            continue

        skill = skills[skill_id]
        old_deps = skill['dependencies']
        new_deps = [d for d in old_deps if d['id'] not in [r for r in modifications['removes']]]
        new_deps.extend(modifications['adds'])

        # Rebuild dependency section
        if new_deps:
            dep_text = "Dependencies:\n" + "\n".join([f"* {d['id']}: {d['name']}" for d in new_deps])
        else:
            dep_text = ""

        # Find and replace in original block
        old_block = skill['original_block']

        # Remove old dependencies section
        lines = old_block.split('\n')
        new_lines = []
        in_deps = False

        for line in lines:
            if line.startswith('Dependencies:'):
                in_deps = True
                continue
            elif in_deps and (line.startswith('* ') or line.strip() == ''):
                if line.strip() == '':
                    in_deps = False
                    new_lines.append(line)
                continue
            else:
                new_lines.append(line)

        # Add new dependencies before the last empty lines
        while new_lines and new_lines[-1].strip() == '':
            new_lines.pop()

        if dep_text:
            new_lines.append('')
            new_lines.append(dep_text)

        new_lines.append('')
        new_lines.append('')

        new_block = '\n'.join(new_lines)

        # Replace in content
        modified_content = modified_content.replace(old_block, new_block)

    return modified_content, changes, skill_changes

def main():
    print("Reading allskills.md...")
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'r', encoding='utf-8') as f:
        content = f.read()

    print(f"File size: {len(content)} bytes")

    modified_content, changes, skill_changes = analyze_and_fix_g8(content)

    # Save modified content
    print("\nSaving modified content...")
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md', 'w', encoding='utf-8') as f:
        f.write(modified_content)

    # Save changes log
    print("Saving changes log...")
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g8_changes_log.json', 'w', encoding='utf-8') as f:
        json.dump({
            'summary': changes,
            'skill_changes': skill_changes
        }, f, indent=2)

    print("\n=== SUMMARY ===")
    print(f"Total Grade 8 skills analyzed: {len([s for s in skill_changes])}")
    print(f"X-2 violations found: {len(changes['x2_violations'])}")
    print(f"Cross-topic dependencies added: {len(changes['cross_topic_adds'])}")
    print(f"Circular dependencies found: {len(changes['circular_fixes'])}")
    print(f"Transitive redundancies found: {len(changes['redundancy_removes'])}")
    print(f"Total changes: {changes['total_changes']}")

    # Top 20 changes
    print("\n=== TOP 20 CHANGES ===")
    all_skill_changes = []
    for skill_id, mods in skill_changes.items():
        if mods['adds'] or mods['removes']:
            all_skill_changes.append({
                'skill_id': skill_id,
                'adds': len(mods['adds']),
                'removes': len(mods['removes']),
                'reasons': mods['reasons']
            })

    all_skill_changes.sort(key=lambda x: x['adds'] + x['removes'], reverse=True)

    for i, change in enumerate(all_skill_changes[:20], 1):
        print(f"\n{i}. {change['skill_id']}")
        print(f"   Adds: {change['adds']}, Removes: {change['removes']}")
        for reason in change['reasons'][:3]:
            print(f"   - {reason}")

    print("\n=== Done ===")

if __name__ == '__main__':
    main()
