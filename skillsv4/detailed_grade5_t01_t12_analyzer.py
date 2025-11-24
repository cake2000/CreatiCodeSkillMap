#!/usr/bin/env python3
"""
Detailed analysis of Grade 5 T01-T12 skills for missing cross-topic dependencies.
"""

import json
import re

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def parse_skill_id(skill_id):
    """Parse skill ID into topic, grade, skill number."""
    match = re.match(r'T(\d+)\.G([K\d]+)\.', skill_id)
    if match:
        topic = int(match.group(1))
        grade = match.group(2)
        return topic, grade
    return None, None

def get_grade_level(grade_str):
    """Convert grade string to numeric for comparison (K=0)."""
    if grade_str == 'K':
        return 0
    return int(grade_str)

def find_best_dependency(target_topic, min_grade, max_grade, all_skills_by_id, keywords):
    """Find the best dependency from a target topic within grade range."""
    candidates = []
    for skill_id, skill in all_skills_by_id.items():
        if skill_id.startswith(f'T{target_topic:02d}.'):
            topic, grade = parse_skill_id(skill_id)
            if grade and min_grade <= get_grade_level(grade) <= max_grade:
                skill_text = f"{skill.get('skill', '')} {skill.get('description', '')}".lower()
                # Check if any keyword matches
                if any(kw in skill_text for kw in keywords):
                    candidates.append(skill_id)

    # Return the earliest (lowest grade, then lowest skill number)
    if candidates:
        candidates.sort()
        return candidates[0]
    return None

def analyze_skill_detailed(skill, all_skills_by_id):
    """Perform detailed analysis of a single skill."""
    skill_id = skill['id']
    topic, grade = parse_skill_id(skill_id)

    if not topic or topic > 12 or grade != '5':
        return None

    skill_text = skill.get('skill', '')
    description = skill.get('description', '')
    full_text = f"{skill_text} {description}".lower()

    current_deps = set(skill.get('dependencies', []))
    suggestions = []
    violations = []

    # Check X-2 rule violations
    for dep_id in current_deps:
        _, dep_grade = parse_skill_id(dep_id)
        if dep_grade and get_grade_level(dep_grade) < 3:
            violations.append({
                'dep_id': dep_id,
                'issue': f'G5 depends on G{dep_grade} which violates X-2 rule (should be G3+)'
            })

    # Detailed cross-topic dependency checks

    # T06: Events - check for event-related terms
    if topic != 6:
        event_terms = ['when green flag', 'when key', 'when clicked', 'event', 'broadcast', 'message']
        if any(term in full_text for term in event_terms):
            has_t06 = any(d.startswith('T06.') for d in current_deps)
            if not has_t06:
                dep = find_best_dependency(6, 3, 5, all_skills_by_id, ['event', 'green flag', 'key press', 'mouse'])
                if dep:
                    suggestions.append({
                        'add_dep': dep,
                        'reason': 'Skill uses events'
                    })

    # T07: Loops
    if topic != 7:
        loop_terms = ['repeat', 'loop', 'forever', 'iteration', 'nested loop', 'multiple times']
        if any(term in full_text for term in loop_terms):
            has_t07 = any(d.startswith('T07.') for d in current_deps)
            if not has_t07:
                dep = find_best_dependency(7, 3, 5, all_skills_by_id, ['repeat', 'loop', 'forever'])
                if dep:
                    suggestions.append({
                        'add_dep': dep,
                        'reason': 'Skill uses loops'
                    })

    # T08: Conditionals
    if topic != 8:
        cond_terms = ['if', 'else', 'condition', 'when', 'boolean', 'comparison', 'true', 'false']
        # Be careful - "if" is common in regular English
        if 'if/else' in full_text or 'if-else' in full_text or 'conditional' in full_text or \
           'if block' in full_text or 'if statement' in full_text:
            has_t08 = any(d.startswith('T08.') for d in current_deps)
            if not has_t08:
                dep = find_best_dependency(8, 3, 5, all_skills_by_id, ['if', 'condition', 'boolean'])
                if dep:
                    suggestions.append({
                        'add_dep': dep,
                        'reason': 'Skill uses conditionals'
                    })

    # T09: Variables
    if topic != 9:
        var_terms = ['variable', 'store', 'counter', 'accumulator', 'score', 'update']
        if any(term in full_text for term in var_terms):
            has_t09 = any(d.startswith('T09.') for d in current_deps)
            if not has_t09:
                dep = find_best_dependency(9, 3, 5, all_skills_by_id, ['variable', 'create variable', 'set variable'])
                if dep:
                    suggestions.append({
                        'add_dep': dep,
                        'reason': 'Skill uses variables'
                    })

    # T10: Lists
    if topic != 10:
        list_terms = ['list', 'array', 'collection', 'item', 'add to list', 'delete from list']
        if any(term in full_text for term in list_terms):
            has_t10 = any(d.startswith('T10.') for d in current_deps)
            if not has_t10:
                dep = find_best_dependency(10, 3, 5, all_skills_by_id, ['list', 'create list', 'item'])
                if dep:
                    suggestions.append({
                        'add_dep': dep,
                        'reason': 'Skill uses lists'
                    })

    # T11: Functions/Custom blocks
    if topic != 11:
        func_terms = ['function', 'custom block', 'procedure', 'define', 'parameter', 'my block']
        if any(term in full_text for term in func_terms):
            has_t11 = any(d.startswith('T11.') for d in current_deps)
            if not has_t11:
                dep = find_best_dependency(11, 3, 5, all_skills_by_id, ['function', 'custom block', 'define'])
                if dep:
                    suggestions.append({
                        'add_dep': dep,
                        'reason': 'Skill uses functions'
                    })

    # T04: Patterns
    if topic != 4:
        pattern_terms = ['pattern', 'counter', 'accumulator', 'filter', 'search', 'recognize']
        if any(term in full_text for term in pattern_terms):
            has_t04 = any(d.startswith('T04.') for d in current_deps)
            if not has_t04:
                dep = find_best_dependency(4, 3, 5, all_skills_by_id, ['pattern', 'counter', 'accumulator'])
                if dep:
                    suggestions.append({
                        'add_dep': dep,
                        'reason': 'Skill involves patterns'
                    })

    # T02: Exploring/Tracing/Debugging
    if topic != 2:
        trace_terms = ['trace', 'debug', 'error', 'fix', 'test', 'compare algorithm']
        if any(term in full_text for term in trace_terms):
            has_t02 = any(d.startswith('T02.') for d in current_deps)
            if not has_t02:
                dep = find_best_dependency(2, 3, 5, all_skills_by_id, ['trace', 'debug', 'test'])
                if dep:
                    suggestions.append({
                        'add_dep': dep,
                        'reason': 'Skill involves debugging/tracing'
                    })

    # T03: Planning/Decomposition
    if topic != 3:
        plan_terms = ['decompos', 'break down', 'plan', 'organize', 'structure']
        if any(term in full_text for term in plan_terms):
            has_t03 = any(d.startswith('T03.') for d in current_deps)
            if not has_t03:
                dep = find_best_dependency(3, 3, 5, all_skills_by_id, ['decompos', 'plan', 'break'])
                if dep:
                    suggestions.append({
                        'add_dep': dep,
                        'reason': 'Skill involves decomposition/planning'
                    })

    return {'suggestions': suggestions, 'violations': violations} if (suggestions or violations) else None

def main():
    print("Loading data files...")
    grade5_data_by_topic = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade5_skills_data.json')
    all_skill_ids_list = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/all_skill_ids.json')

    # Load ALL grades to build complete lookup
    all_grades_data = {}
    for grade_file in ['gradeK_skills_data.json', 'grade1_skills_data.json', 'grade2_skills_data.json',
                       'grade3_skills_data.json', 'grade4_skills_data.json', 'grade5_skills_data.json']:
        try:
            data = load_json(f'/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/{grade_file}')
            for topic_key, skills in data.items():
                if isinstance(skills, list):
                    for skill in skills:
                        all_grades_data[skill['id']] = skill
        except:
            pass

    print(f"Loaded {len(all_grades_data)} total skills across all grades")

    # Get G5 T01-T12 skills
    g5_t01_t12_skills = []
    for topic_num in range(1, 13):
        topic_key = f'T{topic_num:02d}'
        if topic_key in grade5_data_by_topic:
            skills = grade5_data_by_topic[topic_key]
            if isinstance(skills, list):
                for skill in skills:
                    if skill['id'].startswith(f'T{topic_num:02d}.G5.'):
                        g5_t01_t12_skills.append(skill)

    print(f"Found {len(g5_t01_t12_skills)} Grade 5 skills in T01-T12")

    # Analyze each skill
    results = {
        'dependencies_to_add': [],
        'dependencies_to_remove': [],
        'violations': []
    }

    for skill in g5_t01_t12_skills:
        skill_id = skill['id']
        analysis = analyze_skill_detailed(skill, all_grades_data)

        if analysis:
            for sugg in analysis['suggestions']:
                results['dependencies_to_add'].append({
                    'skill_id': skill_id,
                    'add_dep': sugg['add_dep'],
                    'reason': sugg['reason']
                })

            for viol in analysis['violations']:
                results['violations'].append({
                    'skill_id': skill_id,
                    'issue': viol['issue']
                })

    print(f"\nAnalysis complete:")
    print(f"  Dependencies to add: {len(results['dependencies_to_add'])}")
    print(f"  Dependencies to remove: {len(results['dependencies_to_remove'])}")
    print(f"  Violations found: {len(results['violations'])}")

    # Save results
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE5_T01_T12_DETAILED_ANALYSIS.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {output_file}")

    # Print detailed summary
    print("\n=== DETAILED SUMMARY ===")

    if results['dependencies_to_add']:
        print(f"\nDependencies to Add ({len(results['dependencies_to_add'])}):")
        for item in results['dependencies_to_add']:
            print(f"  {item['skill_id']} -> {item['add_dep']}")
            print(f"    Reason: {item['reason']}")

    if results['violations']:
        print(f"\nX-2 Rule Violations ({len(results['violations'])}):")
        for item in results['violations']:
            print(f"  {item['skill_id']}: {item['issue']}")

if __name__ == '__main__':
    main()
