#!/usr/bin/env python3
"""
Integrate K-2 picture-based skills with G3-8 coding skills
to create the complete K-8 CreatiCode Skill Map
"""

import json
from collections import defaultdict, Counter
from typing import Dict, List, Set, Tuple

def load_json(filepath: str) -> List[Dict]:
    """Load JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath: str, indent=2):
    """Save data to JSON file"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)
    print(f"Saved: {filepath}")

def is_k2_grade(grade) -> bool:
    """Check if grade is K, 1, or 2"""
    # Handle both string and integer grades
    if isinstance(grade, str):
        return grade in ['K', '1', '2']
    elif isinstance(grade, int):
        return grade in [0, 1, 2]  # K=0, 1=1, 2=2
    return False

def is_g3_plus_grade(grade) -> bool:
    """Check if grade is 3-8"""
    # Handle both string and integer grades
    if isinstance(grade, str):
        return grade in ['3', '4', '5', '6', '7', '8']
    elif isinstance(grade, int):
        return grade in [3, 4, 5, 6, 7, 8]
    return False

def get_skill_id(skill: Dict) -> str:
    """Get skill ID from skill object"""
    return skill.get('id', skill.get('skill_id', ''))

def get_dependencies(skill: Dict) -> List[str]:
    """Get dependencies from skill, handling different formats"""
    deps = skill.get('dependencies', [])
    if isinstance(deps, list):
        return deps
    return []

def remove_old_k2_skills(all_skills: List[Dict]) -> Tuple[List[Dict], int]:
    """Remove Grade K, 1, and 2 skills from the list"""
    g3_plus_skills = [s for s in all_skills if is_g3_plus_grade(s.get('grade', ''))]
    removed_count = len(all_skills) - len(g3_plus_skills)
    print(f"Removed {removed_count} old K-2 skills")
    print(f"Retained {len(g3_plus_skills)} Grade 3-8 skills")
    return g3_plus_skills, removed_count

def merge_skills(k2_skills: List[Dict], g3_plus_skills: List[Dict]) -> List[Dict]:
    """Merge K-2 and G3+ skills and sort properly"""
    all_skills = k2_skills + g3_plus_skills

    # Sort by topic_id, then grade, then skill_id
    def sort_key(skill):
        topic = skill.get('topic_id', 'T00')
        grade = skill.get('grade', 'K')
        # Convert grade to sortable format (handle both string and int)
        if grade == 'K':
            grade_num = 0
        elif isinstance(grade, int):
            grade_num = grade
        elif isinstance(grade, str):
            grade_num = int(grade)
        else:
            grade_num = 0
        skill_id = skill.get('skill_id', '')
        return (topic, grade_num, skill_id)

    all_skills.sort(key=sort_key)
    print(f"Merged and sorted {len(all_skills)} total skills")
    return all_skills

def validate_skill_structure(skill: Dict, is_k2: bool) -> List[str]:
    """Validate skill has required fields"""
    issues = []
    # Use 'id' as the primary ID field
    required_base = ['id', 'topic_id', 'grade']

    for field in required_base:
        if field not in skill:
            issues.append(f"Missing required field: {field}")

    # Check for description (different field names)
    if not (skill.get('description') or skill.get('description_teacher') or skill.get('student_prompt')):
        issues.append("Missing description field")

    if is_k2:
        # K-2 specific fields
        k2_required = ['skill_type', 'activity_type']
        for field in k2_required:
            if field not in skill:
                issues.append(f"Missing K-2 field: {field}")

        # K-2 should NOT have coding
        if skill.get('skill_type') == 'coding':
            issues.append("K-2 skill has coding type")

    return issues

def find_k3_dependencies_on_k2(all_skills: List[Dict]) -> Dict:
    """Find all Grade 3 skills that depend on K-2 skills"""
    # Build skill index (skip skills without id)
    skill_index = {}
    for s in all_skills:
        skill_id = get_skill_id(s)
        if skill_id:
            skill_index[skill_id] = s

    g3_with_k2_deps = []

    for skill in all_skills:
        skill_id = get_skill_id(skill)
        if not skill_id:
            continue
        grade = skill.get('grade')
        # Handle both string '3' and int 3
        if not (grade == '3' or grade == 3):
            continue

        deps = get_dependencies(skill)
        k2_deps = []

        for dep_id in deps:
            dep_skill = skill_index.get(dep_id)
            if dep_skill and is_k2_grade(dep_skill.get('grade', '')):
                k2_deps.append({
                    'dep_id': dep_id,
                    'dep_grade': dep_skill.get('grade'),
                    'dep_topic': dep_skill.get('topic_id'),
                    'exists': True
                })
            elif not dep_skill:
                k2_deps.append({
                    'dep_id': dep_id,
                    'exists': False,
                    'issue': 'Dependency not found'
                })

        if k2_deps:
            desc = skill.get('description') or skill.get('description_teacher') or skill.get('student_prompt') or ''
            g3_with_k2_deps.append({
                'skill_id': skill_id,
                'topic_id': skill.get('topic_id'),
                'description': desc[:100],
                'k2_dependencies': k2_deps,
                'total_deps': len(deps),
                'k2_dep_count': len(k2_deps)
            })

    return {
        'total_g3_skills_with_k2_deps': len(g3_with_k2_deps),
        'skills': g3_with_k2_deps,
        'analysis': {
            'most_common_k2_topics': _analyze_k2_topics(g3_with_k2_deps),
            'by_grade': _analyze_by_grade(g3_with_k2_deps)
        }
    }

def _analyze_k2_topics(g3_deps: List[Dict]) -> Dict:
    """Analyze which K-2 topics are most referenced by G3"""
    topic_counts = Counter()
    for item in g3_deps:
        for dep in item['k2_dependencies']:
            if dep.get('exists'):
                topic_counts[dep['dep_topic']] += 1
    return dict(topic_counts.most_common(10))

def _analyze_by_grade(g3_deps: List[Dict]) -> Dict:
    """Analyze K-2 dependencies by grade"""
    grade_counts = Counter()
    for item in g3_deps:
        for dep in item['k2_dependencies']:
            if dep.get('exists'):
                grade_counts[dep['dep_grade']] += 1
    return dict(grade_counts)

def calculate_statistics(all_skills: List[Dict]) -> Dict:
    """Calculate comprehensive statistics"""
    stats = {
        'total_skills': len(all_skills),
        'by_grade': {},
        'by_topic': {},
        'by_domain': {},
        'dependencies': {
            'total_dependencies': 0,
            'by_grade': {},
            'gateway_skills': [],
            'capstone_skills': []
        },
        'k2_specific': {},
        'transition_analysis': {}
    }

    # Count by grade (normalize to string format)
    for skill in all_skills:
        grade = skill.get('grade', 'Unknown')
        # Normalize grade to string
        if isinstance(grade, int):
            grade = str(grade)
        stats['by_grade'][grade] = stats['by_grade'].get(grade, 0) + 1

    # Count by topic
    for skill in all_skills:
        topic = skill.get('topic_id', 'Unknown')
        stats['by_topic'][topic] = stats['by_topic'].get(topic, 0) + 1

    # Count by domain (from topic_id)
    domain_map = {
        'T01-T05': 'D1_Algorithms_Programming',
        'T06-T13': 'D2_Programming_Development',
        'T14-T24': 'D3_Applications_AI',
        'T25-T29': 'D4_Data_Analysis',
        'T30-T36': 'D5_Computing_Systems_Society'
    }

    for skill in all_skills:
        topic = skill.get('topic_id', 'T00')
        topic_num = int(topic[1:]) if topic.startswith('T') else 0

        if 1 <= topic_num <= 5:
            domain = 'D1_Algorithms_Programming'
        elif 6 <= topic_num <= 13:
            domain = 'D2_Programming_Development'
        elif 14 <= topic_num <= 24:
            domain = 'D3_Applications_AI'
        elif 25 <= topic_num <= 29:
            domain = 'D4_Data_Analysis'
        elif 30 <= topic_num <= 36:
            domain = 'D5_Computing_Systems_Society'
        else:
            domain = 'Unknown'

        stats['by_domain'][domain] = stats['by_domain'].get(domain, 0) + 1

    # Dependency statistics
    dep_counts = {}
    dependent_counts = defaultdict(int)

    for skill in all_skills:
        skill_id = get_skill_id(skill)
        if not skill_id:
            continue
        deps = get_dependencies(skill)
        dep_counts[skill_id] = len(deps)
        stats['dependencies']['total_dependencies'] += len(deps)

        # Count how many skills depend on each skill
        for dep_id in deps:
            dependent_counts[dep_id] += 1

    # Average dependencies by grade
    grade_dep_totals = defaultdict(int)
    grade_skill_counts = defaultdict(int)

    for skill in all_skills:
        grade = skill.get('grade', 'Unknown')
        deps = get_dependencies(skill)
        grade_dep_totals[grade] += len(deps)
        grade_skill_counts[grade] += 1

    for grade in grade_dep_totals:
        if grade_skill_counts[grade] > 0:
            stats['dependencies']['by_grade'][grade] = {
                'total_deps': grade_dep_totals[grade],
                'avg_deps': round(grade_dep_totals[grade] / grade_skill_counts[grade], 2)
            }

    # Gateway skills (most dependents)
    gateway = sorted(dependent_counts.items(), key=lambda x: x[1], reverse=True)[:20]
    stats['dependencies']['gateway_skills'] = [
        {'skill_id': sid, 'dependent_count': count} for sid, count in gateway
    ]

    # Capstone skills (most dependencies)
    capstone = sorted(dep_counts.items(), key=lambda x: x[1], reverse=True)[:20]
    stats['dependencies']['capstone_skills'] = [
        {'skill_id': sid, 'dependency_count': count} for sid, count in capstone
    ]

    # K-2 specific statistics
    k2_skills = [s for s in all_skills if is_k2_grade(s.get('grade', ''))]
    stats['k2_specific']['total_k2_skills'] = len(k2_skills)

    # Activity type distribution
    activity_types = Counter()
    for skill in k2_skills:
        activity_types[skill.get('activity_type', 'unknown')] += 1
    stats['k2_specific']['activity_type_distribution'] = dict(activity_types)

    # Skill type distribution
    skill_types = Counter()
    for skill in k2_skills:
        skill_types[skill.get('skill_type', 'unknown')] += 1
    stats['k2_specific']['skill_type_distribution'] = dict(skill_types)

    # Topics with K-2 content
    k2_topics = set(s.get('topic_id') for s in k2_skills)
    stats['k2_specific']['topics_with_k2_content'] = sorted(list(k2_topics))
    stats['k2_specific']['k2_topic_count'] = len(k2_topics)

    # All topics (T01-T36)
    all_topics = set(f'T{i:02d}' for i in range(1, 37))
    deferred_topics = sorted(list(all_topics - k2_topics))
    stats['k2_specific']['deferred_topics'] = deferred_topics
    stats['k2_specific']['deferred_topic_count'] = len(deferred_topics)

    return stats

def validate_complete_map(all_skills: List[Dict]) -> Dict:
    """Run comprehensive validation checks"""
    results = {
        'data_integrity': {},
        'dependency_integrity': {},
        'k2_quality': {},
        'g3_plus_quality': {},
        'overall_status': 'PASS'
    }

    # Data integrity checks
    skill_ids = [get_skill_id(s) for s in all_skills if get_skill_id(s)]
    unique_ids = set(skill_ids)

    # Check required fields
    required_check = []
    for s in all_skills:
        has_id = bool(get_skill_id(s))
        has_topic = bool(s.get('topic_id'))
        has_grade = s.get('grade') is not None
        has_desc = bool(s.get('description') or s.get('description_teacher') or s.get('student_prompt'))
        required_check.append(has_id and has_topic and has_grade and has_desc)
    results['data_integrity']['all_have_required_fields'] = all(required_check)
    results['data_integrity']['all_ids_unique'] = len(skill_ids) == len(unique_ids)
    results['data_integrity']['no_duplicates'] = len(skill_ids) == len(unique_ids)

    # Validate grades (handle both string and int)
    valid_grade_check = []
    for s in all_skills:
        grade = s.get('grade')
        if isinstance(grade, str):
            valid_grade_check.append(grade in ['K', '1', '2', '3', '4', '5', '6', '7', '8'])
        elif isinstance(grade, int):
            valid_grade_check.append(grade in [0, 1, 2, 3, 4, 5, 6, 7, 8])
        else:
            valid_grade_check.append(False)
    results['data_integrity']['valid_grades'] = all(valid_grade_check)
    results['data_integrity']['valid_topics'] = all(
        s.get('topic_id', '').startswith('T') and 1 <= int(s.get('topic_id', 'T00')[1:]) <= 36
        for s in all_skills if s.get('topic_id', '').startswith('T')
    )

    # Dependency integrity checks
    skill_id_set = set(skill_ids)
    all_deps = []
    for s in all_skills:
        all_deps.extend(get_dependencies(s))

    self_refs = sum(1 for s in all_skills if get_skill_id(s) and get_skill_id(s) in get_dependencies(s))
    results['dependency_integrity']['no_self_references'] = self_refs == 0

    # Check all dependencies exist
    missing_deps = [d for d in all_deps if d not in skill_id_set]
    results['dependency_integrity']['all_deps_exist'] = len(missing_deps) == 0
    if missing_deps:
        results['dependency_integrity']['missing_deps_sample'] = missing_deps[:10]

    # K-2 quality checks
    k2_skills = [s for s in all_skills if is_k2_grade(s.get('grade', ''))]
    results['k2_quality']['all_picture_based'] = all(
        s.get('skill_type') != 'coding' for s in k2_skills
    )
    results['k2_quality']['all_have_activity_type'] = all(
        s.get('activity_type') for s in k2_skills
    )
    results['k2_quality']['no_coding_required'] = all(
        s.get('skill_type') != 'coding' for s in k2_skills
    )

    # G3+ quality checks
    g3_plus_skills = [s for s in all_skills if is_g3_plus_grade(s.get('grade', ''))]

    # Check if all G3+ dependencies reference existing skills
    g3_missing_deps = []
    for skill in g3_plus_skills:
        skill_id = get_skill_id(skill)
        if not skill_id:
            continue
        for dep_id in get_dependencies(skill):
            if dep_id not in skill_id_set:
                g3_missing_deps.append({'skill': skill_id, 'missing_dep': dep_id})

    results['g3_plus_quality']['no_broken_dependencies'] = len(g3_missing_deps) == 0
    if g3_missing_deps:
        results['g3_plus_quality']['broken_deps_sample'] = g3_missing_deps[:10]

    # Overall status
    all_checks = []
    for category in ['data_integrity', 'dependency_integrity', 'k2_quality', 'g3_plus_quality']:
        for check, passed in results[category].items():
            if isinstance(passed, bool):
                all_checks.append(passed)

    if all(all_checks):
        results['overall_status'] = 'PASS'
    else:
        results['overall_status'] = 'FAIL'
        failed_checks = sum(1 for c in all_checks if not c)
        results['failed_check_count'] = failed_checks

    return results

def main():
    print("=" * 80)
    print("CREATICODE K-8 SKILL MAP INTEGRATION")
    print("=" * 80)

    # Load files
    print("\n[1] Loading skill files...")
    k2_skills = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_k2_with_dependencies.json')
    all_skills_original = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_final_enriched.json')

    print(f"Loaded {len(k2_skills)} K-2 picture-based skills")
    print(f"Loaded {len(all_skills_original)} original K-8 skills")

    # Remove old K-2 skills
    print("\n[2] Removing old K-2 skills...")
    g3_plus_skills, removed_count = remove_old_k2_skills(all_skills_original)

    # Merge new K-2 with G3-8
    print("\n[3] Merging new K-2 with Grade 3-8 skills...")
    complete_skills = merge_skills(k2_skills, g3_plus_skills)

    # Save complete K-8 map
    print("\n[4] Saving complete K-8 skill map...")
    save_json(complete_skills, '/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_complete_k8.json')

    # Validate K-3 transition
    print("\n[5] Validating Grade 2→3 transition...")
    k3_validation = find_k3_dependencies_on_k2(complete_skills)
    save_json(k3_validation, '/media/binyu/USB2/dev/CreatiCodeSkillMap/k3_transition_validation.json')
    print(f"Found {k3_validation['total_g3_skills_with_k2_deps']} Grade 3 skills with K-2 dependencies")

    # Calculate statistics
    print("\n[6] Calculating comprehensive statistics...")
    statistics = calculate_statistics(complete_skills)
    save_json(statistics, '/media/binyu/USB2/dev/CreatiCodeSkillMap/k8_complete_statistics.json')

    # Run validation
    print("\n[7] Running comprehensive validation...")
    validation = validate_complete_map(complete_skills)
    save_json(validation, '/media/binyu/USB2/dev/CreatiCodeSkillMap/k8_validation_report.json')
    print(f"Validation Status: {validation['overall_status']}")

    # Print summary
    print("\n" + "=" * 80)
    print("INTEGRATION COMPLETE")
    print("=" * 80)
    print(f"\nTotal Skills: {statistics['total_skills']}")
    print(f"  - K-2 Skills: {statistics['k2_specific']['total_k2_skills']}")
    print(f"  - Grade 3-8 Skills: {statistics['total_skills'] - statistics['k2_specific']['total_k2_skills']}")
    print(f"\nBy Grade:")
    for grade in ['K', '1', '2', '3', '4', '5', '6', '7', '8']:
        count = statistics['by_grade'].get(grade, 0)
        print(f"  Grade {grade}: {count}")
    print(f"\nBy Domain:")
    for domain, count in sorted(statistics['by_domain'].items()):
        print(f"  {domain}: {count}")
    print(f"\nK-2 Topics: {statistics['k2_specific']['k2_topic_count']}/36")
    print(f"Deferred Topics: {statistics['k2_specific']['deferred_topic_count']}")
    print(f"\nTotal Dependencies: {statistics['dependencies']['total_dependencies']}")
    print(f"Grade 3 Skills with K-2 deps: {k3_validation['total_g3_skills_with_k2_deps']}")
    print(f"\nValidation: {validation['overall_status']}")

    print("\n✅ All files generated successfully!")

if __name__ == '__main__':
    main()
