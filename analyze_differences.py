#!/usr/bin/env python3
import json
from pathlib import Path

def analyze_differences():
    base_path = Path('/media/binyu/USB2/dev/CreatiCodeSkillMap')

    # Load canonical
    with open(base_path / 'skills_k8_ai_complete_FINAL.json', 'r') as f:
        canonical = json.load(f)
    canonical_ids = {skill['id'] for skill in canonical}

    # Load skills_final.json (one of the older files with 126 unique)
    with open(base_path / 'skills_final.json', 'r') as f:
        skills_final = json.load(f)
    final_ids = {skill['id'] for skill in skills_final}

    # Find differences
    unique_in_final = final_ids - canonical_ids
    unique_in_canonical = canonical_ids - final_ids

    print("=" * 80)
    print(f"SKILLS IN skills_final.json BUT NOT IN CANONICAL ({len(unique_in_final)} skills):")
    print("=" * 80)

    for skill_id in sorted(unique_in_final):
        skill = next(s for s in skills_final if s['id'] == skill_id)
        print(f"\nID: {skill_id}")
        print(f"  Title: {skill.get('title', 'N/A')}")
        print(f"  Grade: {skill.get('grade', 'N/A')}")
        print(f"  Topic: {skill.get('topic_id', 'N/A')}")

    print("\n" + "=" * 80)
    print(f"SKILLS IN CANONICAL BUT NOT IN skills_final.json ({len(unique_in_canonical)} skills):")
    print("=" * 80)

    for skill_id in sorted(list(unique_in_canonical)[:20]):  # Show first 20
        skill = next(s for s in canonical if s['id'] == skill_id)
        print(f"\nID: {skill_id}")
        print(f"  Title: {skill.get('title', 'N/A')}")
        print(f"  Grade: {skill.get('grade', 'N/A')}")
        print(f"  Topic: {skill.get('topic_id', 'N/A')}")

    if len(unique_in_canonical) > 20:
        print(f"\n... and {len(unique_in_canonical) - 20} more")

    # Analyze what changed
    print("\n" + "=" * 80)
    print("ANALYSIS:")
    print("=" * 80)
    print(f"Skills removed from older version: {len(unique_in_final)}")
    print(f"Skills added in FINAL version: {len(unique_in_canonical)}")
    print(f"Net change: {len(unique_in_canonical) - len(unique_in_final)}")

if __name__ == '__main__':
    analyze_differences()
