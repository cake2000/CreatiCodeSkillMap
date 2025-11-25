#!/usr/bin/env python3
"""
Verify that Grade 7 fixes were applied correctly
"""

import json
import re

def load_json_plan(filepath: str) -> dict:
    """Load the fixes plan from JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_markdown(filepath: str) -> str:
    """Load the markdown file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def get_skill_dependencies(content: str, skill_id: str) -> list:
    """Extract dependencies for a specific skill"""
    pattern = rf'^ID: {re.escape(skill_id)}$'
    lines = content.split('\n')

    start_idx = -1
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start_idx = i
            break

    if start_idx == -1:
        return None

    # Find Dependencies section
    deps = []
    in_deps = False
    for i in range(start_idx, min(start_idx + 50, len(lines))):
        line = lines[i].strip()
        if line == 'Dependencies:':
            in_deps = True
            continue
        if in_deps:
            if line.startswith('* '):
                # Extract skill ID from dependency
                dep_match = re.match(r'\* ([^:]+):', line)
                if dep_match:
                    deps.append(dep_match.group(1))
            elif line and not line.startswith('*'):
                break

    return deps

def main():
    """Main verification function"""
    plan = load_json_plan('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/GRADE7_FIXES_PLAN.json')
    content = load_markdown('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md')

    results = {
        'x2_fixes': {'applied': 0, 'failed': []},
        'redundant_removals': {'applied': 0, 'failed': []},
        't8_additions': {'applied': 0, 'failed': []},
        't9_additions': {'applied': 0, 'failed': []},
        't10_additions': {'applied': 0, 'failed': []},
        't7_additions': {'applied': 0, 'failed': []},
        't6_additions': {'applied': 0, 'failed': []},
        't11_additions': {'applied': 0, 'failed': []}
    }

    for category_data in plan['fixes']:
        category = category_data['category']

        for fix in category_data['fixes']:
            if fix['action'] == 'review':
                continue

            skill_id = fix['skill_id']
            deps = get_skill_dependencies(content, skill_id)

            if deps is None:
                print(f"WARNING: Skill {skill_id} not found")
                continue

            if fix['action'] == 'replace_dependency':
                old_val = fix['old_value']
                new_val = fix['new_value']

                # Check if old value is gone and new value is present
                if old_val not in deps and new_val in deps:
                    if 'X-2' in category:
                        results['x2_fixes']['applied'] += 1
                else:
                    if 'X-2' in category:
                        results['x2_fixes']['failed'].append({
                            'skill_id': skill_id,
                            'old': old_val,
                            'new': new_val,
                            'deps': deps
                        })

            elif fix['action'] == 'add_dependency':
                new_val = fix['new_value']

                if new_val in deps:
                    if 'Topic 8' in category:
                        results['t8_additions']['applied'] += 1
                    elif 'Topic 9' in category:
                        results['t9_additions']['applied'] += 1
                    elif 'Topic 10' in category:
                        results['t10_additions']['applied'] += 1
                    elif 'Topic 7' in category:
                        results['t7_additions']['applied'] += 1
                    elif 'Topic 6' in category:
                        results['t6_additions']['applied'] += 1
                    elif 'Topic 11' in category:
                        results['t11_additions']['applied'] += 1
                else:
                    if 'Topic 8' in category:
                        results['t8_additions']['failed'].append({
                            'skill_id': skill_id,
                            'missing': new_val,
                            'deps': deps
                        })
                    elif 'Topic 9' in category:
                        results['t9_additions']['failed'].append({
                            'skill_id': skill_id,
                            'missing': new_val
                        })
                    elif 'Topic 10' in category:
                        results['t10_additions']['failed'].append({
                            'skill_id': skill_id,
                            'missing': new_val
                        })
                    elif 'Topic 7' in category:
                        results['t7_additions']['failed'].append({
                            'skill_id': skill_id,
                            'missing': new_val
                        })
                    elif 'Topic 6' in category:
                        results['t6_additions']['failed'].append({
                            'skill_id': skill_id,
                            'missing': new_val
                        })
                    elif 'Topic 11' in category:
                        results['t11_additions']['failed'].append({
                            'skill_id': skill_id,
                            'missing': new_val
                        })

            elif fix['action'] == 'remove_dependency':
                old_val = fix['old_value']

                if old_val not in deps:
                    results['redundant_removals']['applied'] += 1
                else:
                    results['redundant_removals']['failed'].append({
                        'skill_id': skill_id,
                        'still_present': old_val
                    })

    # Print summary
    print("="*60)
    print("VERIFICATION RESULTS")
    print("="*60)
    print(f"X-2 Rule Fixes Applied: {results['x2_fixes']['applied']} (failed: {len(results['x2_fixes']['failed'])})")
    print(f"Redundant Dependencies Removed: {results['redundant_removals']['applied']} (failed: {len(results['redundant_removals']['failed'])})")
    print(f"Topic 8 (Conditions) Added: {results['t8_additions']['applied']} (failed: {len(results['t8_additions']['failed'])})")
    print(f"Topic 9 (Variables) Added: {results['t9_additions']['applied']} (failed: {len(results['t9_additions']['failed'])})")
    print(f"Topic 10 (Lists/Tables) Added: {results['t10_additions']['applied']} (failed: {len(results['t10_additions']['failed'])})")
    print(f"Topic 7 (Loops) Added: {results['t7_additions']['applied']} (failed: {len(results['t7_additions']['failed'])})")
    print(f"Topic 6 (Events) Added: {results['t6_additions']['applied']} (failed: {len(results['t6_additions']['failed'])})")
    print(f"Topic 11 (Functions) Added: {results['t11_additions']['applied']} (failed: {len(results['t11_additions']['failed'])})")

    total_applied = sum(r['applied'] for r in results.values())
    total_failed = sum(len(r['failed']) for r in results.values())

    print("="*60)
    print(f"Total Applied: {total_applied}")
    print(f"Total Failed: {total_failed}")
    print(f"Success Rate: {total_applied / (total_applied + total_failed) * 100:.1f}%")
    print("="*60)

    # Save detailed results
    with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/g7_verification_results.json', 'w') as f:
        json.dump(results, f, indent=2)

    # Print some failed examples if any
    if total_failed > 0:
        print("\nFailed Fixes (first 5 from each category):")
        for key, data in results.items():
            if data['failed']:
                print(f"\n{key}:")
                for fail in data['failed'][:5]:
                    print(f"  {fail}")

if __name__ == '__main__':
    main()
