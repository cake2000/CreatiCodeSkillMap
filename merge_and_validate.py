import json
import sys
from collections import defaultdict, deque
from datetime import datetime

# Phase 1: Merge dependency data
print("=" * 80)
print("PHASE 1: MERGING DEPENDENCY DATA")
print("=" * 80)

# Read skills_enriched.json
print("\nReading skills_enriched.json...")
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_enriched.json', 'r') as f:
    skills_base = json.load(f)
print(f"Loaded {len(skills_base)} skills")

# Create a map for quick lookup
skills_map = {skill['id']: skill for skill in skills_base}

# Read all dependency files
dep_files = [
    '/media/binyu/USB2/dev/CreatiCodeSkillMap/dependencies_T01_T05.json',
    '/media/binyu/USB2/dev/CreatiCodeSkillMap/dependencies_T06_T13.json',
    '/media/binyu/USB2/dev/CreatiCodeSkillMap/dependencies_T14_T24.json',
    '/media/binyu/USB2/dev/CreatiCodeSkillMap/dependencies_T25_T29.json',
    '/media/binyu/USB2/dev/CreatiCodeSkillMap/dependencies_T30_T36.json'
]

all_dependencies = {}
for dep_file in dep_files:
    print(f"Reading {dep_file.split('/')[-1]}...")
    with open(dep_file, 'r') as f:
        dep_data = json.load(f)
    for item in dep_data:
        all_dependencies[item['id']] = item.get('dependencies', [])
    print(f"  -> Added {len(dep_data)} skills")

print(f"\nTotal dependency entries: {len(all_dependencies)}")

# Merge dependencies into skills
print("\nMerging dependencies into skills...")
merged_count = 0
missing_deps = 0
for skill in skills_base:
    skill_id = skill['id']
    if skill_id in all_dependencies:
        skill['dependencies'] = all_dependencies[skill_id]
        skill['dependency_count'] = len(skill['dependencies'])
        merged_count += 1
    else:
        skill['dependencies'] = []
        skill['dependency_count'] = 0
        missing_deps += 1

print(f"Merged {merged_count} skills with dependencies")
print(f"Skills without dependency data: {missing_deps}")

# Save merged file
output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_with_dependencies.json'
with open(output_file, 'w') as f:
    json.dump(skills_base, f, indent=2)
print(f"\nSaved: {output_file}")

# Phase 2: Global Validation
print("\n" + "=" * 80)
print("PHASE 2: GLOBAL VALIDATION")
print("=" * 80)

validation_results = {
    'timestamp': datetime.now().isoformat(),
    'checks': {},
    'errors': [],
    'warnings': []
}

# Check 1: Grade-level consistency
print("\n1. Checking grade-level consistency...")
grade_issues = []
for skill in skills_base:
    skill_id = skill['id']
    skill_grade = skill.get('grade', -1)
    for dep_id in skill.get('dependencies', []):
        if dep_id in skills_map:
            dep_grade = skills_map[dep_id].get('grade', -1)
            if dep_grade > skill_grade:
                grade_issues.append({
                    'skill': skill_id,
                    'grade': skill_grade,
                    'dependency': dep_id,
                    'dep_grade': dep_grade
                })

validation_results['checks']['grade_level_consistency'] = {
    'passed': len(grade_issues) == 0,
    'issues_found': len(grade_issues),
    'issues': grade_issues[:10]  # Show first 10
}
print(f"Grade issues found: {len(grade_issues)}")
if grade_issues:
    print(f"Example: {grade_issues[0]}")

# Check 2: Circular dependencies (using DFS)
print("\n2. Checking for circular dependencies...")
def has_cycle(skills_dict):
    visited = set()
    rec_stack = set()
    cycles = []
    
    def dfs(node, path):
        visited.add(node)
        rec_stack.add(node)
        
        if node in skills_dict and 'dependencies' in skills_dict[node]:
            for dep in skills_dict[node]['dependencies']:
                if dep not in visited:
                    if dfs(dep, path + [dep]):
                        return True
                elif dep in rec_stack:
                    cycles.append(path + [dep])
                    return True
        
        rec_stack.remove(node)
        return False
    
    for skill_id in skills_dict:
        if skill_id not in visited:
            dfs(skill_id, [skill_id])
    
    return len(cycles) == 0, cycles

no_cycles, cycles = has_cycle(skills_map)
validation_results['checks']['circular_dependencies'] = {
    'passed': no_cycles,
    'cycles_found': len(cycles),
    'cycles': cycles[:5]
}
print(f"Circular dependencies found: {len(cycles)}")

# Check 3: Orphan references
print("\n3. Checking for orphan references...")
orphan_refs = []
for skill in skills_base:
    for dep_id in skill.get('dependencies', []):
        if dep_id not in skills_map:
            orphan_refs.append({
                'skill': skill['id'],
                'missing_dep': dep_id
            })

validation_results['checks']['orphan_references'] = {
    'passed': len(orphan_refs) == 0,
    'orphans_found': len(orphan_refs),
    'examples': orphan_refs[:10]
}
print(f"Orphan references found: {len(orphan_refs)}")

# Check 4: Missing dependencies
print("\n4. Checking for missing dependency data...")
missing_dep_data = []
for skill in skills_base:
    if skill['id'] not in all_dependencies:
        missing_dep_data.append(skill['id'])

validation_results['checks']['missing_dependency_data'] = {
    'passed': len(missing_dep_data) == 0,
    'missing_count': len(missing_dep_data),
    'missing_skills': missing_dep_data[:20]
}
print(f"Skills missing dependency data: {len(missing_dep_data)}")

# Check 5: Dependency statistics
print("\n5. Calculating dependency statistics...")
dep_counts = [skill.get('dependency_count', 0) for skill in skills_base]
orphan_skills = [skill['id'] for skill in skills_base if skill.get('dependency_count', 0) == 0]

# Count reverse dependencies (how many skills depend on each skill)
reverse_deps = defaultdict(list)
for skill in skills_base:
    for dep_id in skill.get('dependencies', []):
        reverse_deps[dep_id].append(skill['id'])

gateway_candidates = sorted([(skill_id, len(dependents)) for skill_id, dependents in reverse_deps.items()], 
                            key=lambda x: x[1], reverse=True)

validation_results['checks']['dependency_statistics'] = {
    'total_skills': len(skills_base),
    'total_dependencies': sum(dep_counts),
    'avg_dependencies': sum(dep_counts) / len(skills_base),
    'max_dependencies': max(dep_counts) if dep_counts else 0,
    'min_dependencies': min(dep_counts) if dep_counts else 0,
    'orphan_skills_count': len(orphan_skills),
    'top_gateway_skills': gateway_candidates[:20]
}

print(f"Total dependencies: {sum(dep_counts)}")
print(f"Avg dependencies per skill: {sum(dep_counts) / len(skills_base):.2f}")
print(f"Skills with 0 dependencies: {len(orphan_skills)}")

# Phase 3: Calculate gateway and capstone skills
print("\n" + "=" * 80)
print("PHASE 3: IDENTIFYING GATEWAY AND CAPSTONE SKILLS")
print("=" * 80)

print("\nMarking gateway and capstone skills...")
gateway_threshold = 5  # Skills that 5+ skills depend on
capstone_threshold = 5  # Skills with 5+ dependencies

for skill in skills_base:
    skill_id = skill['id']
    # Gateway: many skills depend on this one
    skill['is_gateway'] = len(reverse_deps.get(skill_id, [])) >= gateway_threshold
    # Capstone: this skill depends on 5+ others
    skill['is_capstone'] = skill.get('dependency_count', 0) >= capstone_threshold

gateway_count = sum(1 for skill in skills_base if skill.get('is_gateway', False))
capstone_count = sum(1 for skill in skills_base if skill.get('is_capstone', False))

print(f"Gateway skills identified: {gateway_count}")
print(f"Capstone skills identified: {capstone_count}")

# Save final skill map
final_output = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_final.json'
with open(final_output, 'w') as f:
    json.dump(skills_base, f, indent=2)
print(f"\nSaved: {final_output}")

# Save validation report
validation_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/validation_report.json'
with open(validation_file, 'w') as f:
    json.dump(validation_results, f, indent=2)
print(f"Saved: {validation_file}")

print("\n" + "=" * 80)
print("VALIDATION SUMMARY")
print("=" * 80)
for check_name, result in validation_results['checks'].items():
    if isinstance(result, dict) and 'passed' in result:
        status = "PASS" if result['passed'] else "FAIL"
        print(f"{check_name}: {status}")
    else:
        print(f"{check_name}: COMPUTED")

print("\nPhases 1-3 complete!")
print("skill_with_dependencies.json created")
print("skills_final.json created")
print("validation_report.json created")

