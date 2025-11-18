#!/usr/bin/env python3
import json
from pathlib import Path
from collections import defaultdict

def load_skills(file_path):
    """Load skills from a JSON file and return set of skill IDs."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)

        if isinstance(data, list):
            skills = data
        elif isinstance(data, dict) and 'skills' in data:
            skills = data['skills']
        else:
            return None, None

        skill_ids = {skill['id'] for skill in skills if 'id' in skill}
        return skills, skill_ids
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None, None

def compare_with_canonical():
    base_path = Path('/media/binyu/USB2/dev/CreatiCodeSkillMap')

    # The canonical file
    canonical_file = base_path / 'skills_k8_ai_complete_FINAL.json'
    print(f"Loading canonical file: {canonical_file.name}")
    canonical_skills, canonical_ids = load_skills(canonical_file)

    if canonical_ids is None:
        print("ERROR: Could not load canonical file!")
        return

    print(f"Canonical file has {len(canonical_ids)} skills\n")

    # Files to compare
    compare_files = [
        'skills_k8_ai_complete_WEEK2.json',
        'skills_k8_ai_complete_REVISED.json',
        'skills_k8_ai_complete.json',
        'skills_k8_ai_complete.BACKUP.json',
        'skills_complete_k8.json',
        'skills_final_enriched.json',
        'skills_final.json',
        'skills.json',
        'skills_enriched.json',
        'extracted_skills_raw.json',
        'FOUNDATIONAL_41_SKILLS.json',
        'CREATIVE_SKILLS_3.json',
        'WEEK2_NEW_SKILLS.json',
    ]

    results = {
        'canonical_count': len(canonical_ids),
        'comparisons': []
    }

    for filename in compare_files:
        file_path = base_path / filename
        if not file_path.exists():
            continue

        skills, skill_ids = load_skills(file_path)
        if skill_ids is None:
            continue

        # Find differences
        unique_in_file = skill_ids - canonical_ids
        unique_in_canonical = canonical_ids - skill_ids
        common = skill_ids & canonical_ids

        comparison = {
            'filename': filename,
            'total_skills': len(skill_ids),
            'common_with_canonical': len(common),
            'unique_in_this_file': len(unique_in_file),
            'missing_from_this_file': len(unique_in_canonical),
            'unique_ids': sorted(list(unique_in_file))[:10] if unique_in_file else []
        }

        results['comparisons'].append(comparison)

        print(f"{filename:50} | Total: {len(skill_ids):4} | Common: {len(common):4} | Unique: {len(unique_in_file):4} | Missing: {len(unique_in_canonical):4}")
        if unique_in_file:
            print(f"  └─ Sample unique IDs: {', '.join(sorted(list(unique_in_file))[:5])}")

    # Save results
    output_file = base_path / 'skill_comparison_report.json'
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n\nDetailed comparison saved to: {output_file}")

if __name__ == '__main__':
    compare_with_canonical()
