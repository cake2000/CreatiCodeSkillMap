#!/usr/bin/env python3
"""
Analyze Grade 5 T01-T12 skills for cross-topic dependency issues.
"""

import json
import re

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def parse_skill_id(skill_id):
    """Parse skill ID into topic, grade, skill number."""
    match = re.match(r'T(\d+)\.G([K\d]+)\.(\d+)', skill_id)
    if match:
        topic = int(match.group(1))
        grade = match.group(2)
        skill_num = int(match.group(3))
        return topic, grade, skill_num
    return None, None, None

def get_grade_level(grade_str):
    """Convert grade string to numeric for comparison (K=0)."""
    if grade_str == 'K':
        return 0
    return int(grade_str)

def analyze_skill_content(skill):
    """Analyze skill content to identify what programming concepts it uses."""
    skill_id = skill['id']
    title = skill.get('title', '').lower()
    description = skill.get('description', '').lower()
    examples = ' '.join(skill.get('examples', [])).lower()
    full_text = f"{title} {description} {examples}"

    concepts = {
        'loops': False,
        'conditionals': False,
        'variables': False,
        'lists': False,
        'functions': False,
        'events': False,
        'patterns': False,
        'debugging': False
    }

    # Detect loops
    loop_keywords = ['loop', 'repeat', 'forever', 'iteration', 'iterate', 'nested loop']
    if any(kw in full_text for kw in loop_keywords):
        concepts['loops'] = True

    # Detect conditionals
    cond_keywords = ['if', 'else', 'condition', 'conditional', 'boolean', 'true/false', 'comparison']
    if any(kw in full_text for kw in cond_keywords):
        concepts['conditionals'] = True

    # Detect variables
    var_keywords = ['variable', 'store value', 'counter', 'accumulator', 'update', 'increment', 'decrement']
    if any(kw in full_text for kw in var_keywords):
        concepts['variables'] = True

    # Detect lists
    list_keywords = ['list', 'array', 'collection', 'item in list', 'add to list', 'delete from list']
    if any(kw in full_text for kw in list_keywords):
        concepts['lists'] = True

    # Detect functions
    func_keywords = ['function', 'custom block', 'procedure', 'parameter', 'return', 'define']
    if any(kw in full_text for kw in func_keywords):
        concepts['functions'] = True

    # Detect events
    event_keywords = ['event', 'green flag', 'key press', 'mouse click', 'broadcast', 'when']
    if any(kw in full_text for kw in event_keywords):
        concepts['events'] = True

    # Detect patterns
    pattern_keywords = ['pattern', 'counter', 'accumulator', 'filter', 'search', 'recognize pattern']
    if any(kw in full_text for kw in pattern_keywords):
        concepts['patterns'] = True

    # Detect debugging
    debug_keywords = ['debug', 'error', 'bug', 'trace', 'fix', 'troubleshoot', 'test']
    if any(kw in full_text for kw in debug_keywords):
        concepts['debugging'] = True

    return concepts

def check_cross_topic_deps(skill, all_skills_by_id, all_skill_ids):
    """Check if skill has appropriate cross-topic dependencies."""
    skill_id = skill['id']
    topic, grade, skill_num = parse_skill_id(skill_id)

    if topic is None or topic > 12:
        return None  # Only analyze T01-T12

    if grade != '5':
        return None  # Only analyze Grade 5

    current_deps = set(skill.get('dependencies', []))
    concepts = analyze_skill_content(skill)

    suggestions = {
        'add': [],
        'remove': [],
        'violations': []
    }

    # Check for X-2 rule violations (G5 can only depend on G3+)
    for dep_id in current_deps:
        _, dep_grade, _ = parse_skill_id(dep_id)
        if dep_grade and get_grade_level(dep_grade) < 3:
            suggestions['violations'].append({
                'dep_id': dep_id,
                'issue': f'G5 depends on G{dep_grade} which violates X-2 rule (should be G3+)'
            })

    # Check for missing cross-topic dependencies

    # T06: Events
    if concepts['events'] and topic != 6:
        has_t06_dep = any(d.startswith('T06.') for d in current_deps)
        if not has_t06_dep:
            # Look for appropriate T06 G3-G5 skills
            for cand_id in all_skill_ids:
                if cand_id.startswith('T06.') and (cand_id.startswith('T06.G3.') or
                                                     cand_id.startswith('T06.G4.') or
                                                     cand_id.startswith('T06.G5.')):
                    if cand_id in all_skills_by_id:
                        cand_title = all_skills_by_id[cand_id].get('title', '').lower()
                        if 'event' in cand_title or 'green flag' in cand_title:
                            suggestions['add'].append({
                                'dep_id': cand_id,
                                'reason': 'Skill involves events'
                            })
                            break

    # T07: Loops
    if concepts['loops'] and topic != 7:
        has_t07_dep = any(d.startswith('T07.') for d in current_deps)
        if not has_t07_dep:
            # Look for appropriate T07 G3-G5 skills
            for cand_id in all_skill_ids:
                if cand_id.startswith('T07.') and (cand_id.startswith('T07.G3.') or
                                                     cand_id.startswith('T07.G4.') or
                                                     cand_id.startswith('T07.G5.')):
                    if cand_id in all_skills_by_id:
                        cand_title = all_skills_by_id[cand_id].get('title', '').lower()
                        if 'loop' in cand_title or 'repeat' in cand_title:
                            suggestions['add'].append({
                                'dep_id': cand_id,
                                'reason': 'Skill involves loops'
                            })
                            break

    # T08: Conditionals
    if concepts['conditionals'] and topic != 8:
        has_t08_dep = any(d.startswith('T08.') for d in current_deps)
        if not has_t08_dep:
            # Look for appropriate T08 G3-G5 skills
            for cand_id in all_skill_ids:
                if cand_id.startswith('T08.') and (cand_id.startswith('T08.G3.') or
                                                     cand_id.startswith('T08.G4.') or
                                                     cand_id.startswith('T08.G5.')):
                    if cand_id in all_skills_by_id:
                        cand_title = all_skills_by_id[cand_id].get('title', '').lower()
                        if 'if' in cand_title or 'condition' in cand_title:
                            suggestions['add'].append({
                                'dep_id': cand_id,
                                'reason': 'Skill involves conditionals'
                            })
                            break

    # T09: Variables
    if concepts['variables'] and topic != 9:
        has_t09_dep = any(d.startswith('T09.') for d in current_deps)
        if not has_t09_dep:
            # Look for appropriate T09 G3-G5 skills
            for cand_id in all_skill_ids:
                if cand_id.startswith('T09.') and (cand_id.startswith('T09.G3.') or
                                                     cand_id.startswith('T09.G4.') or
                                                     cand_id.startswith('T09.G5.')):
                    if cand_id in all_skills_by_id:
                        cand_title = all_skills_by_id[cand_id].get('title', '').lower()
                        if 'variable' in cand_title:
                            suggestions['add'].append({
                                'dep_id': cand_id,
                                'reason': 'Skill involves variables'
                            })
                            break

    # T10: Lists
    if concepts['lists'] and topic != 10:
        has_t10_dep = any(d.startswith('T10.') for d in current_deps)
        if not has_t10_dep:
            # Look for appropriate T10 G3-G5 skills
            for cand_id in all_skill_ids:
                if cand_id.startswith('T10.') and (cand_id.startswith('T10.G3.') or
                                                     cand_id.startswith('T10.G4.') or
                                                     cand_id.startswith('T10.G5.')):
                    if cand_id in all_skills_by_id:
                        cand_title = all_skills_by_id[cand_id].get('title', '').lower()
                        if 'list' in cand_title:
                            suggestions['add'].append({
                                'dep_id': cand_id,
                                'reason': 'Skill involves lists'
                            })
                            break

    # T11: Functions
    if concepts['functions'] and topic != 11:
        has_t11_dep = any(d.startswith('T11.') for d in current_deps)
        if not has_t11_dep:
            # Look for appropriate T11 G3-G5 skills
            for cand_id in all_skill_ids:
                if cand_id.startswith('T11.') and (cand_id.startswith('T11.G3.') or
                                                     cand_id.startswith('T11.G4.') or
                                                     cand_id.startswith('T11.G5.')):
                    if cand_id in all_skills_by_id:
                        cand_title = all_skills_by_id[cand_id].get('title', '').lower()
                        if 'function' in cand_title or 'custom block' in cand_title:
                            suggestions['add'].append({
                                'dep_id': cand_id,
                                'reason': 'Skill involves functions'
                            })
                            break

    # T04: Patterns
    if concepts['patterns'] and topic != 4:
        has_t04_dep = any(d.startswith('T04.') for d in current_deps)
        if not has_t04_dep:
            # Look for appropriate T04 G3-G5 skills
            for cand_id in all_skill_ids:
                if cand_id.startswith('T04.') and (cand_id.startswith('T04.G3.') or
                                                     cand_id.startswith('T04.G4.') or
                                                     cand_id.startswith('T04.G5.')):
                    if cand_id in all_skills_by_id:
                        cand_title = all_skills_by_id[cand_id].get('title', '').lower()
                        if 'pattern' in cand_title or 'counter' in cand_title or 'accumulator' in cand_title:
                            suggestions['add'].append({
                                'dep_id': cand_id,
                                'reason': 'Skill involves patterns'
                            })
                            break

    return suggestions if (suggestions['add'] or suggestions['remove'] or suggestions['violations']) else None

def main():
    print("Loading data files...")
    grade5_data_by_topic = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade5_skills_data.json')
    all_skill_ids = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/all_skill_ids.json')

    # Flatten and build lookup dict
    all_skills = []
    for topic_key, skills in grade5_data_by_topic.items():
        if isinstance(skills, list):
            all_skills.extend(skills)

    all_skills_by_id = {skill['id']: skill for skill in all_skills}

    print(f"Loaded {len(all_skills)} Grade 5 skills")
    print(f"Total skill IDs available: {len(all_skill_ids)}")

    # Analyze each G5 T01-T12 skill
    results = {
        'dependencies_to_add': [],
        'dependencies_to_remove': [],
        'violations': []
    }

    skills_analyzed = 0
    for skill in all_skills:
        skill_id = skill['id']
        topic, grade, _ = parse_skill_id(skill_id)

        if topic and 1 <= topic <= 12 and grade == '5':
            skills_analyzed += 1
            suggestions = check_cross_topic_deps(skill, all_skills_by_id, all_skill_ids)

            if suggestions:
                if suggestions['add']:
                    for item in suggestions['add']:
                        results['dependencies_to_add'].append({
                            'skill_id': skill_id,
                            'add_dep': item['dep_id'],
                            'reason': item['reason']
                        })

                if suggestions['remove']:
                    for item in suggestions['remove']:
                        results['dependencies_to_remove'].append({
                            'skill_id': skill_id,
                            'remove_dep': item['dep_id'],
                            'reason': item['reason']
                        })

                if suggestions['violations']:
                    for item in suggestions['violations']:
                        results['violations'].append({
                            'skill_id': skill_id,
                            'issue': item['issue']
                        })

    print(f"\nAnalyzed {skills_analyzed} Grade 5 T01-T12 skills")
    print(f"Dependencies to add: {len(results['dependencies_to_add'])}")
    print(f"Dependencies to remove: {len(results['dependencies_to_remove'])}")
    print(f"Violations found: {len(results['violations'])}")

    # Save results
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE5_T01_T12_ANALYSIS.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {output_file}")

    # Print summary
    print("\n=== SUMMARY ===")
    if results['dependencies_to_add']:
        print("\nDependencies to Add:")
        for item in results['dependencies_to_add'][:10]:  # Show first 10
            print(f"  {item['skill_id']} -> {item['add_dep']} ({item['reason']})")
        if len(results['dependencies_to_add']) > 10:
            print(f"  ... and {len(results['dependencies_to_add']) - 10} more")

    if results['violations']:
        print("\nX-2 Rule Violations:")
        for item in results['violations'][:10]:
            print(f"  {item['skill_id']}: {item['issue']}")
        if len(results['violations']) > 10:
            print(f"  ... and {len(results['violations']) - 10} more")

if __name__ == '__main__':
    main()
