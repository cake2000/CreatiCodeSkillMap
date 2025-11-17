#!/usr/bin/env python3
"""
Fix invalid dependencies in the complete K-8 skill map
Remove dependencies on non-existent G1-G2 bridge skills from deferred topics
"""

import json

def load_json(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath: str):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():
    print("Loading complete K-8 skills...")
    skills = load_json('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_complete_k8.json')

    # Build skill ID set
    skill_ids = set(s.get('id', '') for s in skills if s.get('id'))

    # Find and remove invalid dependencies
    fixed_count = 0
    removed_deps = []

    for skill in skills:
        deps = skill.get('dependencies', [])
        if not deps:
            continue

        # Filter out missing dependencies
        valid_deps = []
        for dep in deps:
            if dep in skill_ids:
                valid_deps.append(dep)
            else:
                removed_deps.append({
                    'skill': skill.get('id'),
                    'missing_dep': dep
                })

        if len(valid_deps) < len(deps):
            skill['dependencies'] = valid_deps
            skill['dependency_count'] = len(valid_deps)
            fixed_count += 1

    print(f"Fixed {fixed_count} skills")
    print(f"Removed {len(removed_deps)} invalid dependencies")

    # Show what was removed
    from collections import Counter
    missing_counter = Counter(d['missing_dep'] for d in removed_deps)
    print("\nRemoved dependencies:")
    for dep, count in missing_counter.most_common():
        print(f"  {dep}: {count} times")

    # Save fixed skills
    save_json(skills, '/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_complete_k8.json')
    print("\nSaved fixed skills to skills_complete_k8.json")

    # Save removed dependencies report
    save_json({
        'total_removed': len(removed_deps),
        'unique_missing_deps': len(set(d['missing_dep'] for d in removed_deps)),
        'removed_dependencies': removed_deps,
        'summary': dict(missing_counter)
    }, '/media/binyu/USB2/dev/CreatiCodeSkillMap/removed_dependencies_report.json')
    print("Saved removal report to removed_dependencies_report.json")

if __name__ == '__main__':
    main()
