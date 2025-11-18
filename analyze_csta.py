#!/usr/bin/env python3
import json
from collections import defaultdict

# Load skills
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_k8_ai_complete.json', 'r') as f:
    skills = json.load(f)

print(f"Total skills: {len(skills)}")

# Count skills with valid CSTA codes
valid_csta = [s for s in skills if s.get('csta_code') and s['csta_code'] not in ['', 'Unknown', None]]
print(f"Skills with valid CSTA codes: {len(valid_csta)} ({len(valid_csta)/len(skills)*100:.1f}%)")

# Analyze by topic
by_topic = defaultdict(lambda: {'total': 0, 'with_csta': 0, 'samples': []})
for skill in skills:
    topic = skill['topic_id']
    by_topic[topic]['total'] += 1
    if skill.get('csta_code') and skill['csta_code'] not in ['', 'Unknown', None]:
        by_topic[topic]['with_csta'] += 1
        if len(by_topic[topic]['samples']) < 3:
            by_topic[topic]['samples'].append({
                'id': skill['id'],
                'grade': skill['grade'],
                'csta': skill['csta_code'],
                'title': skill['title'][:50]
            })

print("\n=== Coverage by Topic ===")
for topic in sorted(by_topic.keys()):
    data = by_topic[topic]
    pct = data['with_csta'] / data['total'] * 100 if data['total'] > 0 else 0
    print(f"{topic}: {data['with_csta']}/{data['total']} ({pct:.1f}%)")
    for sample in data['samples']:
        print(f"  {sample['id']} (G{sample['grade']}): {sample['csta']} - {sample['title']}")

# Analyze CSTA code patterns
print("\n=== CSTA Code Patterns ===")
csta_codes = defaultdict(list)
for skill in valid_csta:
    csta_codes[skill['csta_code']].append({
        'id': skill['id'],
        'topic': skill['topic_id'],
        'grade': skill['grade']
    })

print(f"Unique CSTA codes used: {len(csta_codes)}")
print("\nMost common CSTA codes:")
for code, skills_list in sorted(csta_codes.items(), key=lambda x: len(x[1]), reverse=True)[:10]:
    print(f"  {code}: {len(skills_list)} skills")
    for s in skills_list[:2]:
        print(f"    {s['id']} ({s['topic']}, G{s['grade']})")
