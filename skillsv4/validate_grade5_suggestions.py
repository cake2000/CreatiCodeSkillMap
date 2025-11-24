#!/usr/bin/env python3
"""
Validate and refine Grade 5 T01-T12 dependency suggestions.
"""

import json

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def main():
    print("Loading data...")
    grade5_data = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/grade5_skills_data.json')
    suggestions = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE5_T01_T12_DETAILED_ANALYSIS.json')

    # Build skill lookup
    all_skills = {}
    for topic_key, skills in grade5_data.items():
        if isinstance(skills, list):
            for skill in skills:
                all_skills[skill['id']] = skill

    # Validate each suggestion
    validated = {
        'dependencies_to_add': [],
        'dependencies_to_remove': [],
        'violations': suggestions['violations']  # Keep all violations
    }

    print(f"Validating {len(suggestions['dependencies_to_add'])} suggestions...")

    for sugg in suggestions['dependencies_to_add']:
        skill_id = sugg['skill_id']
        add_dep = sugg['add_dep']
        reason = sugg['reason']

        if skill_id not in all_skills:
            continue

        skill = all_skills[skill_id]
        desc = skill.get('description', '').lower()
        skill_text = skill.get('skill', '').lower()
        full_text = f"{skill_text} {desc}"

        # Check for explicit exclusions
        exclude = False

        if reason == "Skill uses loops":
            if "no loop" in full_text or "without loop" in full_text or "no iteration" in full_text:
                exclude = True

        if reason == "Skill uses conditionals":
            if "no conditional" in full_text or "without conditional" in full_text or \
               "no if" in full_text or "sequential" in desc:
                exclude = True

        # Keep suggestion if not excluded
        if not exclude:
            validated['dependencies_to_add'].append(sugg)
        else:
            print(f"  EXCLUDED: {skill_id} -> {add_dep} ({reason})")
            print(f"    Reason: Found exclusion in description")

    print(f"\nValidation complete:")
    print(f"  Original suggestions: {len(suggestions['dependencies_to_add'])}")
    print(f"  Validated suggestions: {len(validated['dependencies_to_add'])}")
    print(f"  Excluded: {len(suggestions['dependencies_to_add']) - len(validated['dependencies_to_add'])}")

    # Save validated results
    output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE5_T01_T12_FINAL.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(validated, f, indent=2)

    print(f"\nValidated results saved to: {output_file}")

    # Print summary by category
    print("\n=== SUMMARY BY CATEGORY ===")

    by_reason = {}
    for sugg in validated['dependencies_to_add']:
        reason = sugg['reason']
        if reason not in by_reason:
            by_reason[reason] = []
        by_reason[reason].append(sugg)

    for reason, items in sorted(by_reason.items()):
        print(f"\n{reason}: {len(items)} dependencies")
        for item in items[:5]:  # Show first 5
            print(f"  {item['skill_id']} -> {item['add_dep']}")
        if len(items) > 5:
            print(f"  ... and {len(items) - 5} more")

if __name__ == '__main__':
    main()
