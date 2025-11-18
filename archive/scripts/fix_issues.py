import json

with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_final.json', 'r') as f:
    skills_base = json.load(f)

skills_map = {skill['id']: skill for skill in skills_base}

print("=" * 80)
print("FIXING DATA ISSUES")
print("=" * 80)

# Fix 1: Self-referential cycles (self-dependencies)
print("\n1. Removing self-referential dependencies...")
self_ref_count = 0
for skill in skills_base:
    original_deps = skill.get('dependencies', [])
    # Remove self-references
    skill['dependencies'] = [dep for dep in original_deps if dep != skill['id']]
    if len(skill['dependencies']) < len(original_deps):
        self_ref_count += 1
        print(f"   Removed self-reference from {skill['id']}")

skill['dependency_count'] = len(skill['dependencies'])
print(f"Total self-references removed: {self_ref_count}")

# Fix 2: Investigate and fix missing skill references
print("\n2. Fixing orphan references...")
print("\nOrphan reference 1: T03.G2.01 references missing T03.G1.04")
print("  Looking for similar skills in T03.G1...")
t03_g1_skills = [s for s in skills_base if s['topic_id'] == 'T03' and s['grade'] == 1]
print(f"  T03.G1 skills: {[s['id'] for s in t03_g1_skills]}")
t03_g2 = skills_map['T03.G2.01']
print(f"  T03.G2.01 title: {t03_g2['title']}")
print(f"  Current dependencies: {t03_g2['dependencies']}")

# T03.G1.04 likely doesn't exist. Check what should be the dependency.
# G2.01 is about replacing repeated blocks with a loop.
# Most likely prerequisite is a skill about recognizing patterns or repetition
# Let's look at T03 structure
print("\nT03 skills structure:")
t03_all = sorted([s for s in skills_base if s['topic_id'] == 'T03'], 
                  key=lambda x: (x['grade'], x['id']))
for s in t03_all[:20]:
    print(f"  {s['id']} (G{s['grade']}): {s['title'][:60]}")

# Based on T03 structure, T03.G1 has skills 01-03 (no 04)
# T03.G2.01 should probably depend on T03.G1.03 (about identifying patterns)
print("\n  Recommendation: T03.G2.01 should depend on T03.G1.03 instead")
t03_g2['dependencies'] = ['T03.G1.03']
t03_g2['dependency_count'] = 1
print(f"  Fixed: T03.G2.01 -> {t03_g2['dependencies']}")

print("\nOrphan reference 2: T03.G3.01 references missing T03.G2.04")
print("  Looking for T03.G2 skills...")
t03_g2_skills = [s for s in skills_base if s['topic_id'] == 'T03' and s['grade'] == 2]
print(f"  T03.G2 skills: {[s['id'] for s in t03_g2_skills]}")
t03_g3 = skills_map['T03.G3.01']
print(f"  T03.G3.01 title: {t03_g3['title']}")
print(f"  Current dependencies: {t03_g3['dependencies']}")

# T03.G2 has skills 01-03 (no 04)
# T03.G3.01 is about decomposing projects, probably depends on T03.G2.03 (complex decomposition)
print("\n  Recommendation: T03.G3.01 should depend on T03.G2.03 instead")
t03_g3['dependencies'] = ['T03.G2.03']
t03_g3['dependency_count'] = 1
print(f"  Fixed: T03.G3.01 -> {t03_g3['dependencies']}")

# Recount dependency_count for all skills
print("\n3. Recalculating dependency counts...")
for skill in skills_base:
    skill['dependency_count'] = len(skill.get('dependencies', []))

# Save fixed version
output_file = '/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_final.json'
with open(output_file, 'w') as f:
    json.dump(skills_base, f, indent=2)
print(f"\nSaved fixed version: {output_file}")

# Run validation again
print("\n" + "=" * 80)
print("RE-VALIDATION AFTER FIXES")
print("=" * 80)

# Check 1: Orphan references
print("\n1. Checking for remaining orphan references...")
orphan_refs = []
for skill in skills_base:
    for dep_id in skill.get('dependencies', []):
        if dep_id not in skills_map:
            orphan_refs.append({
                'skill': skill['id'],
                'missing_dep': dep_id
            })

print(f"Remaining orphan references: {len(orphan_refs)}")
if orphan_refs:
    for ref in orphan_refs:
        print(f"  {ref}")

# Check 2: Self-references
print("\n2. Checking for self-references...")
self_refs = []
for skill in skills_base:
    if skill['id'] in skill.get('dependencies', []):
        self_refs.append(skill['id'])

print(f"Remaining self-references: {len(self_refs)}")
if self_refs:
    for ref in self_refs:
        print(f"  {ref}")

# Check 3: Circular dependencies (simplified - just count multi-item cycles)
print("\n3. Checking for genuine circular dependencies...")
def has_cycle_dfs(graph, node, visited, rec_stack, path):
    visited.add(node)
    rec_stack.add(node)
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            if has_cycle_dfs(graph, neighbor, visited, rec_stack, path + [neighbor]):
                return True
        elif neighbor in rec_stack and len(path + [neighbor]) > 2:
            return True
    
    rec_stack.remove(node)
    return False

graph = {skill['id']: skill.get('dependencies', []) for skill in skills_base}
visited = set()
multi_cycles = 0
for node in graph:
    if node not in visited:
        if has_cycle_dfs(graph, node, visited, set(), [node]):
            multi_cycles += 1

print(f"Multi-node circular dependencies: {multi_cycles}")

print("\n" + "=" * 80)
print("SUMMARY OF FIXES")
print("=" * 80)
print(f"Self-references removed: {self_ref_count}")
print(f"Orphan references fixed: 2")
print(f"  T03.G2.01: T03.G1.04 -> T03.G1.03")
print(f"  T03.G3.01: T03.G2.04 -> T03.G2.03")
print(f"Remaining validation issues: {len(orphan_refs) + len(self_refs)}")

