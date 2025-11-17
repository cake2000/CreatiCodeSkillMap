import json
from collections import defaultdict

# Load data
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/validation_report.json', 'r') as f:
    report = json.load(f)

with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_final.json', 'r') as f:
    skills_base = json.load(f)

skills_map = {skill['id']: skill for skill in skills_base}

print("=" * 80)
print("INVESTIGATING ISSUES")
print("=" * 80)

# Issue 1: Circular dependencies
print("\n1. CIRCULAR DEPENDENCIES (23 found)")
print("-" * 80)

def find_all_cycles():
    def dfs(node, visited, rec_stack, path, all_cycles):
        visited.add(node)
        rec_stack.add(node)
        
        if node in skills_map and 'dependencies' in skills_map[node]:
            for dep in skills_map[node]['dependencies']:
                if dep not in visited:
                    dfs(dep, visited, rec_stack, path + [dep], all_cycles)
                elif dep in rec_stack:
                    cycle_start = path.index(dep) if dep in path else 0
                    cycle = path[cycle_start:] + [dep]
                    all_cycles.append(cycle)
        
        rec_stack.remove(node)
    
    visited = set()
    all_cycles = []
    for skill_id in skills_map:
        if skill_id not in visited:
            dfs(skill_id, visited, set(), [skill_id], all_cycles)
    return all_cycles

cycles = find_all_cycles()
print(f"Total cycles detected: {len(cycles)}")
if cycles:
    print("\nFirst 5 cycles:")
    for i, cycle in enumerate(cycles[:5], 1):
        print(f"  Cycle {i}: {' -> '.join(cycle[:5])}")

# Issue 2: Orphan references
print("\n2. ORPHAN REFERENCES (2 found)")
print("-" * 80)

orphan_refs = report['checks']['orphan_references']['examples']
print(f"Orphan references:")
for ref in orphan_refs:
    print(f"  {ref['skill']} -> depends on missing {ref['missing_dep']}")

# Let's find them all
all_orphans = defaultdict(list)
for skill in skills_base:
    for dep_id in skill.get('dependencies', []):
        if dep_id not in skills_map:
            all_orphans[skill['id']].append(dep_id)

print(f"\nAll missing dependencies:")
for skill_id, missing_deps in all_orphans.items():
    for missing_dep in missing_deps:
        print(f"  {skill_id} depends on missing: {missing_dep}")

# Suggest fixes
print("\n" + "=" * 80)
print("RECOMMENDED FIXES")
print("=" * 80)

print("\n1. For orphan references (2 skills):")
print("   Option A: Remove the broken dependency links")
print("   Option B: Identify the correct skill ID (typo?)")
for skill_id, missing_deps in all_orphans.items():
    skill = skills_map[skill_id]
    print(f"\n   Skill: {skill_id} ({skill['title']})")
    print(f"   Grade: {skill.get('grade')}, Topic: {skill.get('topic_name')}")
    for missing_dep in missing_deps:
        print(f"   References missing: {missing_dep}")

print("\n2. For circular dependencies (23 cycles):")
print("   These may be legitimate cross-references or design patterns.")
print("   Manual review needed to determine:")
print("   - Are they bidirectional (mutual dependencies)?")
print("   - Should one direction be removed?")
print("   - Are they indicators of misclassified grade levels?")

# Analyze cycle patterns
print("\n3. Cycle Analysis:")
cycle_edges = set()
for cycle in cycles:
    for i in range(len(cycle) - 1):
        cycle_edges.add((cycle[i], cycle[i+1]))

print(f"   Unique edges in cycles: {len(cycle_edges)}")
print(f"   First 10 edge pairs:")
for i, (a, b) in enumerate(sorted(list(cycle_edges))[:10], 1):
    if a in skills_map and b in skills_map:
        print(f"   {i}. {a} -> {b}")

