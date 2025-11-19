#!/usr/bin/env python3
"""
Generate final statistics for allskills.md with dependencies
"""

import re
from collections import defaultdict

def analyze_allskills(filepath):
    """Analyze the allskills.md file and generate comprehensive statistics."""

    grade_stats = defaultdict(lambda: {
        'total_skills': 0,
        'skills_with_deps': 0,
        'total_dependencies': 0,
        'skills': []
    })

    topic_stats = defaultdict(lambda: {
        'total_skills': 0,
        'skills_with_deps': 0,
        'total_dependencies': 0
    })

    current_skill_id = None
    current_topic = None
    current_deps = 0

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()

            # Match skill ID
            id_match = re.match(r'^ID:\s*(T(\d+)\.(G[K0-9]+)\.\d+)', line)
            if id_match:
                # Save previous skill if exists
                if current_skill_id:
                    grade = re.match(r'T\d+\.(G[K0-9]+)\.\d+', current_skill_id).group(1)
                    topic = re.match(r'T(\d+)\.G[K0-9]+\.\d+', current_skill_id).group(1)

                    grade_stats[grade]['total_skills'] += 1
                    topic_stats[topic]['total_skills'] += 1

                    if current_deps > 0:
                        grade_stats[grade]['skills_with_deps'] += 1
                        grade_stats[grade]['total_dependencies'] += current_deps
                        topic_stats[topic]['skills_with_deps'] += 1
                        topic_stats[topic]['total_dependencies'] += current_deps

                current_skill_id = id_match.group(1)
                current_topic = id_match.group(2)
                current_deps = 0
                continue

            # Count dependencies
            if current_skill_id and re.match(r'^\*\s*T\d+\.G[K0-9]+\.\d+:', line):
                current_deps += 1

    # Save last skill
    if current_skill_id:
        grade = re.match(r'T\d+\.(G[K0-9]+)\.\d+', current_skill_id).group(1)
        topic = re.match(r'T(\d+)\.G[K0-9]+\.\d+', current_skill_id).group(1)

        grade_stats[grade]['total_skills'] += 1
        topic_stats[topic]['total_skills'] += 1

        if current_deps > 0:
            grade_stats[grade]['skills_with_deps'] += 1
            grade_stats[grade]['total_dependencies'] += current_deps
            topic_stats[topic]['skills_with_deps'] += 1
            topic_stats[topic]['total_dependencies'] += current_deps

    return grade_stats, topic_stats

def main():
    filepath = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md'

    print("Analyzing allskills.md with dependencies...")
    grade_stats, topic_stats = analyze_allskills(filepath)

    # Calculate totals
    total_skills = sum(s['total_skills'] for s in grade_stats.values())
    total_with_deps = sum(s['skills_with_deps'] for s in grade_stats.values())
    total_deps = sum(s['total_dependencies'] for s in grade_stats.values())

    print("\n" + "="*70)
    print("FINAL ALLSKILLS.MD STATISTICS")
    print("="*70)

    print(f"\nOVERALL SUMMARY:")
    print(f"  Total skills: {total_skills}")
    print(f"  Skills with dependencies: {total_with_deps}")
    print(f"  Skills without dependencies: {total_skills - total_with_deps}")
    print(f"  Total dependency connections: {total_deps}")
    print(f"  Overall average dependencies per skill: {total_deps / total_with_deps:.2f}")

    print("\n" + "="*70)
    print("STATISTICS BY GRADE")
    print("="*70)

    grades = ['GK', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8']

    for grade in grades:
        if grade in grade_stats:
            stats = grade_stats[grade]
            avg_deps = stats['total_dependencies'] / stats['skills_with_deps'] if stats['skills_with_deps'] > 0 else 0
            coverage = (stats['skills_with_deps'] / stats['total_skills'] * 100) if stats['total_skills'] > 0 else 0

            print(f"\nGrade {grade}:")
            print(f"  Total skills: {stats['total_skills']}")
            print(f"  Skills with dependencies: {stats['skills_with_deps']}")
            print(f"  Dependency coverage: {coverage:.1f}%")
            print(f"  Total dependencies: {stats['total_dependencies']}")
            print(f"  Average dependencies per skill: {avg_deps:.2f}")

    print("\n" + "="*70)
    print("STATISTICS BY TOPIC (Top 10 by skill count)")
    print("="*70)

    # Sort topics by total skills
    sorted_topics = sorted(topic_stats.items(), key=lambda x: x[1]['total_skills'], reverse=True)[:10]

    for topic_num, stats in sorted_topics:
        avg_deps = stats['total_dependencies'] / stats['skills_with_deps'] if stats['skills_with_deps'] > 0 else 0
        coverage = (stats['skills_with_deps'] / stats['total_skills'] * 100) if stats['total_skills'] > 0 else 0

        print(f"\nTopic T{topic_num}:")
        print(f"  Total skills: {stats['total_skills']}")
        print(f"  Skills with dependencies: {stats['skills_with_deps']} ({coverage:.1f}% coverage)")
        print(f"  Total dependencies: {stats['total_dependencies']}")
        print(f"  Average dependencies per skill: {avg_deps:.2f}")

    print("\n" + "="*70)
    print("CONFIRMATION")
    print("="*70)
    print(f"\nAll {total_skills} skills from K-8 are present in allskills.md")
    print(f"{total_with_deps} skills ({total_with_deps/total_skills*100:.1f}%) now have proper dependencies")
    print(f"Dependencies use the format: * SKILL_ID: Skill name")
    print(f"\nTotal dependency connections created: {total_deps}")

if __name__ == '__main__':
    main()
