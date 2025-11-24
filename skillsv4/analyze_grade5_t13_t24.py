#!/usr/bin/env python3
"""
Analyze Grade 5 skills in Topics T13-T24 for cross-topic dependency issues.
"""

import json
import re
from collections import defaultdict

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def parse_skill_id(skill_id):
    """Parse skill_id like T14.G5.01 into components."""
    match = re.match(r'T(\d+)\.G([KX\d]+)\.(\d+)', skill_id)
    if match:
        return {
            'topic': int(match.group(1)),
            'grade': match.group(2),
            'number': int(match.group(3)),
            'topic_str': f"T{match.group(1)}",
            'grade_str': f"G{match.group(2)}"
        }
    return None

def get_grade_level(grade_str):
    """Convert grade string to numeric level for comparison."""
    if grade_str == 'GK': return 0
    if grade_str == 'GX': return 10  # Advanced
    return int(grade_str[1:])

def analyze_grade5_t13_t24():
    # Load data
    print("Loading data files...")
    grade5_data = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade5_skills_data.json')
    all_skill_ids = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/all_skill_ids.json')

    # Extract Grade 5 skills in T13-T24
    target_topics = [f"T{i:02d}" for i in range(13, 25)]  # T13 to T24
    g5_skills_t13_t24 = []

    # grade5_data is a dict with topics as keys
    for topic_key, skills_list in grade5_data.items():
        if topic_key in target_topics:
            if isinstance(skills_list, list):
                g5_skills_t13_t24.extend(skills_list)

    print(f"Found {len(g5_skills_t13_t24)} Grade 5 skills in T13-T24")

    # Topic definitions and expected foundational dependencies
    topic_foundations = {
        13: {  # Debugging
            'name': 'Debugging',
            'expected': ['T06', 'T07', 'T08'],  # Events, Loops, Conditionals
            'description': 'Finding and fixing errors requires understanding of events, loops, conditionals'
        },
        14: {  # Games
            'name': 'Games',
            'expected': ['T06', 'T07', 'T08', 'T09'],  # Events, Loops, Conditionals, Variables
            'description': 'Game mechanics require events, loops, conditionals, variables'
        },
        15: {  # Storytelling
            'name': 'Storytelling',
            'expected': ['T06', 'T07', 'T10'],  # Events, Loops, Lists (for dialogue)
            'description': 'Narratives require events, loops for sequences, lists for dialogue'
        },
        16: {  # User Interface
            'name': 'User Interface',
            'expected': ['T06', 'T08', 'T09'],  # Events, Conditionals, Variables
            'description': 'UI requires events for interaction, conditionals for state, variables'
        },
        17: {  # Physics/Motion
            'name': 'Physics/Motion',
            'expected': ['T07', 'T08', 'T09'],  # Loops, Conditionals, Variables
            'description': 'Physics simulations require loops, conditionals, variables'
        },
        18: {  # 3D Worlds
            'name': '3D Worlds',
            'expected': ['T06', 'T07', 'T09'],  # Events, Loops, Variables
            'description': '3D scenes require events, loops for animation, variables for state'
        },
        19: {  # Multiplayer
            'name': 'Multiplayer',
            'expected': ['T06', 'T09', 'T10'],  # Events, Variables, Lists
            'description': 'Networking requires events, variables for state, lists for players'
        },
        20: {  # Generative Art
            'name': 'Generative Art',
            'expected': ['T07', 'T09', 'T10'],  # Loops, Variables, Lists
            'description': 'Procedural art requires loops, variables, lists for patterns'
        },
        21: {  # AI Text (ChatGPT)
            'name': 'AI Text',
            'expected': ['T06', 'T09', 'T29'],  # Events, Variables, Text handling
            'description': 'AI text requires events, variables, text manipulation'
        },
        22: {  # AI Voice
            'name': 'AI Voice',
            'expected': ['T06', 'T09', 'T29'],  # Events, Variables, Text
            'description': 'Voice AI requires events, variables, text for prompts'
        },
        23: {  # AI Vision
            'name': 'AI Vision',
            'expected': ['T06', 'T09'],  # Events, Variables
            'description': 'Vision AI requires events for camera, variables for results'
        },
        24: {  # XO Assistant
            'name': 'XO Assistant',
            'expected': ['T06', 'T09'],  # Events, Variables
            'description': 'AI assistant requires events, variables for interaction'
        }
    }

    # Results
    dependencies_to_add = []
    dependencies_to_remove = []
    violations = []

    # Analyze each skill
    for skill in g5_skills_t13_t24:
        skill_id = skill['id']
        title = skill.get('skill', '')
        description = skill.get('description', '')
        dependencies = skill.get('dependencies', [])

        parsed = parse_skill_id(skill_id)
        if not parsed:
            continue

        topic_num = parsed['topic']
        topic_info = topic_foundations.get(topic_num, {})

        # Check X-2 rule violations (G5 should only depend on G3, G4, G5)
        for dep in dependencies:
            dep_parsed = parse_skill_id(dep)
            if dep_parsed:
                dep_grade_level = get_grade_level(dep_parsed['grade_str'])
                if dep_grade_level < 3:  # Depends on GK, G1, or G2
                    violations.append({
                        'skill_id': skill_id,
                        'issue': f"Depends on {dep} which is below G3 (violates X-2 rule for G5)"
                    })
                elif dep_grade_level > 5:  # Depends on G6+
                    violations.append({
                        'skill_id': skill_id,
                        'issue': f"Depends on {dep} which is G6+ (violates X-2 rule for G5)"
                    })

        # Check for missing foundational dependencies
        expected_topics = topic_info.get('expected', [])

        # Extract topics from current dependencies
        current_dep_topics = set()
        for dep in dependencies:
            dep_parsed = parse_skill_id(dep)
            if dep_parsed:
                current_dep_topics.add(dep_parsed['topic_str'])

        # Check each expected topic
        for expected_topic in expected_topics:
            if expected_topic not in current_dep_topics:
                # Find appropriate skill from G3 or G4 in that topic
                # Look for foundational skills
                topic_num_expected = int(expected_topic[1:])

                # Find suitable dependency from G3 or G4
                candidate_deps = []
                for valid_id in all_skill_ids:
                    valid_parsed = parse_skill_id(valid_id)
                    if valid_parsed and valid_parsed['topic'] == topic_num_expected:
                        grade_level = get_grade_level(valid_parsed['grade_str'])
                        if grade_level in [3, 4]:
                            candidate_deps.append((valid_id, grade_level))

                # Prefer G3 skills as they're more foundational
                candidate_deps.sort(key=lambda x: (x[1], x[0]))

                if candidate_deps:
                    suggested_dep = candidate_deps[0][0]

                    # Determine reason based on topic and skill content
                    reason = f"{topic_info['name']} skill requires {expected_topic} foundation"

                    # Make reason more specific based on skill content
                    title_lower = title.lower()
                    desc_lower = description.lower()

                    if expected_topic == 'T06' and ('event' in title_lower or 'trigger' in title_lower or 'click' in desc_lower):
                        reason = f"Requires event handling foundation from {expected_topic}"
                    elif expected_topic == 'T07' and ('loop' in title_lower or 'repeat' in title_lower or 'iterate' in desc_lower):
                        reason = f"Requires loop foundation from {expected_topic}"
                    elif expected_topic == 'T08' and ('condition' in title_lower or 'if' in desc_lower or 'check' in desc_lower):
                        reason = f"Requires conditional logic foundation from {expected_topic}"
                    elif expected_topic == 'T09' and ('variable' in title_lower or 'store' in desc_lower or 'value' in desc_lower):
                        reason = f"Requires variable handling foundation from {expected_topic}"
                    elif expected_topic == 'T10' and ('list' in title_lower or 'array' in desc_lower or 'collection' in desc_lower):
                        reason = f"Requires list/data structure foundation from {expected_topic}"
                    elif expected_topic == 'T29' and ('text' in title_lower or 'string' in desc_lower or 'prompt' in desc_lower):
                        reason = f"Requires text manipulation foundation from {expected_topic}"

                    dependencies_to_add.append({
                        'skill_id': skill_id,
                        'add_dep': suggested_dep,
                        'reason': reason
                    })

    # Check for potentially redundant dependencies
    # (Conservative - only flag truly obvious redundancies)
    for skill in g5_skills_t13_t24:
        skill_id = skill['id']
        dependencies = skill.get('dependencies', [])

        # Check for same-topic dependencies that might be redundant
        parsed = parse_skill_id(skill_id)
        if parsed:
            same_topic_deps = []
            for dep in dependencies:
                dep_parsed = parse_skill_id(dep)
                if dep_parsed and dep_parsed['topic'] == parsed['topic']:
                    same_topic_deps.append(dep)

            # If there are 3+ same-topic dependencies, might have redundancy
            if len(same_topic_deps) >= 3:
                # This is conservative - we'd need to look at actual skill progression
                # For now, just note but don't auto-remove
                pass

    # Create output
    output = {
        'dependencies_to_add': dependencies_to_add,
        'dependencies_to_remove': dependencies_to_remove,
        'violations': violations,
        'summary': {
            'total_skills_analyzed': len(g5_skills_t13_t24),
            'dependencies_to_add_count': len(dependencies_to_add),
            'dependencies_to_remove_count': len(dependencies_to_remove),
            'violations_count': len(violations)
        }
    }

    # Save output
    output_path = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade5_t13_t24_analysis.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)

    print(f"\nAnalysis complete!")
    print(f"Total skills analyzed: {len(g5_skills_t13_t24)}")
    print(f"Dependencies to add: {len(dependencies_to_add)}")
    print(f"Dependencies to remove: {len(dependencies_to_remove)}")
    print(f"Violations found: {len(violations)}")
    print(f"\nOutput saved to: {output_path}")

    # Print sample findings
    if dependencies_to_add:
        print("\nSample dependencies to add:")
        for item in dependencies_to_add[:5]:
            print(f"  {item['skill_id']} <- {item['add_dep']}: {item['reason']}")

    if violations:
        print("\nViolations found:")
        for item in violations[:5]:
            print(f"  {item['skill_id']}: {item['issue']}")

if __name__ == '__main__':
    analyze_grade5_t13_t24()
