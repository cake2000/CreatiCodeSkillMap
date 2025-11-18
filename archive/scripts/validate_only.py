#!/usr/bin/env python3
"""
Run only validation and statistics on the complete K-8 skill map
"""

import json
import sys
sys.path.insert(0, '/media/binyu/USB2/dev/CreatiCodeSkillMap')

from integrate_k8_skills import (
    load_json, save_json, find_k3_dependencies_on_k2,
    calculate_statistics, validate_complete_map
)

def main():
    print("Loading complete K-8 skills...")
    complete_skills = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_complete_k8.json')

    print(f"Loaded {len(complete_skills)} skills")

    # Validate K-3 transition
    print("\nValidating Grade 2→3 transition...")
    k3_validation = find_k3_dependencies_on_k2(complete_skills)
    save_json(k3_validation, '/media/binyu/USB2/dev/CreatiCodeSkillMap/k3_transition_validation.json')
    print(f"Found {k3_validation['total_g3_skills_with_k2_deps']} Grade 3 skills with K-2 dependencies")

    # Calculate statistics
    print("\nCalculating comprehensive statistics...")
    statistics = calculate_statistics(complete_skills)
    save_json(statistics, '/media/binyu/USB2/dev/CreatiCodeSkillMap/k8_complete_statistics.json')

    # Run validation
    print("\nRunning comprehensive validation...")
    validation = validate_complete_map(complete_skills)
    save_json(validation, '/media/binyu/USB2/dev/CreatiCodeSkillMap/k8_validation_report.json')
    print(f"Validation Status: {validation['overall_status']}")

    # Print summary
    print("\n" + "=" * 80)
    print("VALIDATION COMPLETE")
    print("=" * 80)
    print(f"\nTotal Skills: {statistics['total_skills']}")
    print(f"  - K-2 Skills: {statistics['k2_specific']['total_k2_skills']}")
    print(f"  - Grade 3-8 Skills: {statistics['total_skills'] - statistics['k2_specific']['total_k2_skills']}")
    print(f"\nBy Grade:")
    for grade in ['K', '1', '2', '3', '4', '5', '6', '7', '8']:
        count = statistics['by_grade'].get(grade, 0)
        print(f"  Grade {grade}: {count}")
    print(f"\nTotal Dependencies: {statistics['dependencies']['total_dependencies']}")
    print(f"Grade 3 Skills with K-2 deps: {k3_validation['total_g3_skills_with_k2_deps']}")
    print(f"\nValidation: {validation['overall_status']}")

    if validation['overall_status'] == 'FAIL':
        print("\n⚠️  Validation Issues:")
        for cat in ['data_integrity', 'dependency_integrity', 'k2_quality', 'g3_plus_quality']:
            for k, v in validation[cat].items():
                if isinstance(v, bool) and not v:
                    print(f"  ❌ {cat}.{k}")
    else:
        print("\n✅ All validation checks passed!")

if __name__ == '__main__':
    main()
