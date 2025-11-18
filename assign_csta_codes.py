#!/usr/bin/env python3
"""
Assign CSTA codes to all 1,119 skills using the mapping rules.
This creates SKILL_CSTA_ASSIGNMENTS.json with comprehensive assignments.
"""
import json
from collections import defaultdict

# Load skills
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/skills_k8_ai_complete.json', 'r') as f:
    skills = json.load(f)

# Load mapping rules
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/TOPIC_TO_CSTA_MAPPING_RULES.json', 'r') as f:
    mapping_rules = json.load(f)

# Grade name mapping
grade_map = {
    'K': 'K',
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8'
}

# Track statistics
stats = {
    'total_skills': len(skills),
    'skills_assigned': 0,
    'skills_with_existing': 0,
    'skills_kept_existing': 0,
    'skills_auto_assigned': 0,
    'skills_needing_review': 0,
    'by_topic': {},
    'by_grade': defaultdict(lambda: {'total': 0, 'assigned': 0})
}

assignments = []

for skill in skills:
    skill_id = skill['id']
    topic_id = skill['topic_id']
    grade = skill['grade']

    # Convert grade to string key
    grade_key = str(grade) if grade != 'K' else 'K'

    # Track by grade
    stats['by_grade'][grade_key]['total'] += 1

    # Check if skill already has valid CSTA code
    existing_csta = skill.get('csta_code', '')
    has_valid_existing = existing_csta and existing_csta not in ['', 'Unknown', None]

    if has_valid_existing:
        stats['skills_with_existing'] += 1

    # Get mapping rule for this topic and grade
    topic_mapping = mapping_rules['topic_mappings'].get(topic_id, {})
    grade_mappings = topic_mapping.get('grade_mappings', {})
    suggested_codes = grade_mappings.get(grade_key, [])

    # Determine assignment strategy
    if has_valid_existing:
        # Keep existing if it's valid
        assigned_codes = [existing_csta]
        assignment_method = 'existing'
        confidence = 'high'
        stats['skills_kept_existing'] += 1
    elif suggested_codes:
        # Use rule-based assignment
        assigned_codes = suggested_codes
        assignment_method = 'rule_based'
        confidence = 'high' if len(suggested_codes) <= 2 else 'medium'
        stats['skills_auto_assigned'] += 1
    else:
        # No mapping available - needs manual review
        assigned_codes = []
        assignment_method = 'needs_review'
        confidence = 'low'
        stats['skills_needing_review'] += 1

    if assigned_codes:
        stats['skills_assigned'] += 1
        stats['by_grade'][grade_key]['assigned'] += 1

    # Track by topic
    if topic_id not in stats['by_topic']:
        stats['by_topic'][topic_id] = {
            'total': 0,
            'assigned': 0,
            'existing': 0,
            'auto': 0,
            'review': 0
        }

    stats['by_topic'][topic_id]['total'] += 1
    if assigned_codes:
        stats['by_topic'][topic_id]['assigned'] += 1
    if assignment_method == 'existing':
        stats['by_topic'][topic_id]['existing'] += 1
    elif assignment_method == 'rule_based':
        stats['by_topic'][topic_id]['auto'] += 1
    else:
        stats['by_topic'][topic_id]['review'] += 1

    # Create assignment record
    assignment = {
        'skill_id': skill_id,
        'topic_id': topic_id,
        'topic_name': topic_mapping.get('name', ''),
        'grade': grade,
        'title': skill['title'],
        'skill_type': skill.get('skill_type', ''),
        'existing_csta_code': existing_csta if has_valid_existing else None,
        'assigned_csta_codes': assigned_codes,
        'primary_csta_area': topic_mapping.get('primary_csta_area', ''),
        'secondary_csta_areas': topic_mapping.get('secondary_csta_areas', []),
        'assignment_method': assignment_method,
        'confidence': confidence,
        'notes': ''
    }

    # Add notes for manual review cases
    if assignment_method == 'needs_review':
        if not topic_mapping:
            assignment['notes'] = f'No mapping rule found for topic {topic_id}'
        else:
            assignment['notes'] = f'No grade-specific mapping for {topic_id} grade {grade}. Check if topic is appropriate for this grade.'

    assignments.append(assignment)

# Create output structure
output = {
    'metadata': {
        'version': '1.0',
        'created': '2025-11-17',
        'description': 'CSTA code assignments for all CreatiCode K-8 skills',
        'total_skills': stats['total_skills'],
        'skills_assigned': stats['skills_assigned'],
        'coverage_percentage': round(stats['skills_assigned'] / stats['total_skills'] * 100, 1)
    },
    'statistics': stats,
    'assignments': assignments
}

# Save to file
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/SKILL_CSTA_ASSIGNMENTS.json', 'w') as f:
    json.dump(output, f, indent=2)

print("Created SKILL_CSTA_ASSIGNMENTS.json")
print(f"\n=== Assignment Statistics ===")
print(f"Total skills: {stats['total_skills']}")
print(f"Skills assigned CSTA codes: {stats['skills_assigned']} ({stats['skills_assigned']/stats['total_skills']*100:.1f}%)")
print(f"  - Kept existing: {stats['skills_kept_existing']}")
print(f"  - Auto-assigned by rules: {stats['skills_auto_assigned']}")
print(f"  - Needs manual review: {stats['skills_needing_review']}")

print(f"\n=== Coverage by Grade ===")
for grade in ['K', '1', '2', '3', '4', '5', '6', '7', '8']:
    data = stats['by_grade'][grade]
    if data['total'] > 0:
        pct = data['assigned'] / data['total'] * 100
        print(f"Grade {grade}: {data['assigned']}/{data['total']} ({pct:.1f}%)")

print(f"\n=== Coverage by Topic (Top 10 Lowest) ===")
topic_coverage = []
for topic_id, data in stats['by_topic'].items():
    pct = data['assigned'] / data['total'] * 100 if data['total'] > 0 else 0
    topic_coverage.append((topic_id, data['assigned'], data['total'], pct))

topic_coverage.sort(key=lambda x: x[3])  # Sort by percentage
for topic_id, assigned, total, pct in topic_coverage[:10]:
    topic_name = mapping_rules['topic_mappings'].get(topic_id, {}).get('name', '')
    print(f"{topic_id} ({topic_name[:30]}): {assigned}/{total} ({pct:.1f}%)")

print(f"\n=== Skills Needing Manual Review ===")
print(f"Total: {stats['skills_needing_review']}")
review_by_topic = defaultdict(int)
for assignment in assignments:
    if assignment['assignment_method'] == 'needs_review':
        review_by_topic[assignment['topic_id']] += 1

print("\nBy topic:")
for topic_id, count in sorted(review_by_topic.items(), key=lambda x: x[1], reverse=True)[:10]:
    topic_name = mapping_rules['topic_mappings'].get(topic_id, {}).get('name', '')
    print(f"  {topic_id} ({topic_name[:30]}): {count} skills")

print(f"\n✓ Assignment file created successfully!")
print(f"✓ Automated coverage: {(stats['skills_auto_assigned']+stats['skills_kept_existing'])/stats['total_skills']*100:.1f}%")
