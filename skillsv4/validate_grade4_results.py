#!/usr/bin/env python3
"""
Export detailed validation results to JSON for automated processing.
"""

import json
from validate_grade4_final import extract_all_skills, validate_grade4_skills, analyze_cross_topic_patterns, get_topic_stats

def main():
    skills_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE4_VALIDATION_RESULTS.json'

    print("Extracting and validating Grade 4 skills...")
    skills = extract_all_skills(skills_file)
    validation_results, g4_skills = validate_grade4_skills(skills)
    topic_pairs = analyze_cross_topic_patterns(g4_skills)
    topic_stats = get_topic_stats(g4_skills)

    # Convert Counter to dict for JSON serialization
    dep_grade_dist = dict(validation_results['dep_grade_distribution'])
    topic_pairs_dict = {f"{t1}-{t2}": count for (t1, t2), count in topic_pairs.items()}

    # Prepare JSON output
    results = {
        "metadata": {
            "generated": "2025-11-24",
            "source_file": skills_file,
            "grade": "G4"
        },
        "summary": {
            "total_skills": validation_results['total_g4_skills'],
            "avg_dependencies_per_skill": round(validation_results['avg_deps_per_skill'], 2),
            "total_dependencies": sum(validation_results['dep_grade_distribution'].values()),
            "cross_topic_dependencies": len(validation_results['cross_topic_deps']),
            "cross_topic_percentage": round(len(validation_results['cross_topic_deps']) * 100 / sum(validation_results['dep_grade_distribution'].values()), 1) if sum(validation_results['dep_grade_distribution'].values()) > 0 else 0
        },
        "dependency_grade_distribution": dep_grade_dist,
        "validation_status": {
            "x2_violations": len(validation_results['x2_violations']),
            "invalid_dependency_ids": len(validation_results['invalid_dep_ids']),
            "circular_dependencies": len(validation_results['circular_deps']),
            "skills_without_dependencies": len(validation_results['skills_without_deps'])
        },
        "issues": {
            "x2_violations": validation_results['x2_violations'],
            "invalid_dependency_ids": validation_results['invalid_dep_ids'],
            "circular_dependencies": validation_results['circular_deps'],
            "skills_without_dependencies": validation_results['skills_without_deps']
        },
        "topic_statistics": {
            topic: {
                "total_skills": stats['count'],
                "skills_with_dependencies": stats['with_deps'],
                "total_dependencies": stats['total_deps'],
                "avg_dependencies_per_skill": round(stats['total_deps'] / stats['count'], 2) if stats['count'] > 0 else 0
            }
            for topic, stats in topic_stats.items()
        },
        "cross_topic_pairs": topic_pairs_dict
    }

    # Write to JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Validation results exported to: {output_file}")
    print(f"Total size: {len(json.dumps(results, indent=2))} bytes")

if __name__ == '__main__':
    main()
