import json

print("=" * 80)
print("FINAL VERIFICATION")
print("=" * 80)

with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_final.json', 'r') as f:
    skills = json.load(f)

print(f"\n1. JSON Structure Verification")
print(f"   Total skills: {len(skills)}")
print(f"   Expected: 1,155")
assert len(skills) == 1155, "Skill count mismatch!"

print(f"\n2. Required Fields Check")
required_fields = ['id', 'title', 'topic_id', 'grade', 'dependencies', 'dependency_count']
skills_with_all_fields = 0
for skill in skills:
    if all(field in skill for field in required_fields):
        skills_with_all_fields += 1

print(f"   Skills with all required fields: {skills_with_all_fields}/1155")
assert skills_with_all_fields == 1155, "Some skills missing required fields!"

print(f"\n3. Dependency Data Verification")
total_deps = sum(len(skill['dependencies']) for skill in skills)
total_dep_counts = sum(skill['dependency_count'] for skill in skills)
print(f"   Total dependency relationships: {total_deps}")
print(f"   Sum of dependency_count fields: {total_dep_counts}")
assert total_deps == total_dep_counts, "Dependency count mismatch!"

print(f"\n4. Reference Validity Check")
skills_map = {s['id']: s for s in skills}
invalid_refs = 0
for skill in skills:
    for dep_id in skill['dependencies']:
        if dep_id not in skills_map:
            invalid_refs += 1
            print(f"   Invalid reference: {skill['id']} -> {dep_id}")

print(f"   Invalid references found: {invalid_refs}")
assert invalid_refs == 0, "Invalid references found!"

print(f"\n5. Self-Reference Check")
self_refs = 0
for skill in skills:
    if skill['id'] in skill['dependencies']:
        self_refs += 1
        print(f"   Self-reference: {skill['id']}")

print(f"   Self-references found: {self_refs}")
assert self_refs == 0, "Self-references found!"

print(f"\n6. Gateway and Capstone Skills")
gateway_count = sum(1 for s in skills if s.get('is_gateway', False))
capstone_count = sum(1 for s in skills if s.get('is_capstone', False))
print(f"   Gateway skills: {gateway_count}")
print(f"   Capstone skills: {capstone_count}")

print(f"\n7. Grade Distribution")
by_grade = {}
for skill in skills:
    grade = skill['grade']
    if grade not in by_grade:
        by_grade[grade] = 0
    by_grade[grade] += 1

for grade in sorted(by_grade.keys()):
    print(f"   Grade {grade}: {by_grade[grade]} skills")

print(f"\n8. Topic Coverage")
by_topic = {}
for skill in skills:
    topic = skill['topic_id']
    if topic not in by_topic:
        by_topic[topic] = 0
    by_topic[topic] += 1

print(f"   Total topics: {len(by_topic)}")
print(f"   Expected: 36")
assert len(by_topic) == 36, "Topic count mismatch!"

print(f"\n9. Foundational Skills (0 dependencies)")
foundational = [s for s in skills if s['dependency_count'] == 0]
print(f"   Count: {len(foundational)}")
print(f"   Examples:")
for i, skill in enumerate(foundational[:5], 1):
    print(f"      {i}. {skill['id']}: {skill['title'][:60]}")

print(f"\n" + "=" * 80)
print("FINAL VERIFICATION: ALL CHECKS PASSED ✓")
print("=" * 80)

