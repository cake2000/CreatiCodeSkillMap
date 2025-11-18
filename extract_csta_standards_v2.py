#!/usr/bin/env python3
"""
Extract all K-8 CSTA standards from the cstastandard.md file.
Standards are embedded in HTML tables.
"""
import json
import re

# Read the CSTA standards markdown file
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/cstastandard.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Topic area mapping
topic_areas = {
    'ALG': {'name': 'Algorithms and Design', 'subtopics': {
        'AF': 'Algorithm Fundamentals',
        'HD': 'Human-Centered Design',
        'PS': 'Problem Solving',
        'IM': 'Impacts of Algorithms'
    }},
    'PRO': {'name': 'Programming', 'subtopics': {
        'PF': 'Programming Fundamentals',
        'DH': 'Data Handling',
        'PD': 'Program Development',
        'TR': 'Testing and Refining Code',
        'PM': 'Project Management'
    }},
    'DAA': {'name': 'Data and Analysis', 'subtopics': {
        'DF': 'Data Fundamentals',
        'DP': 'Data Processing',
        'DI': 'Data Investigations',
        'IM': 'Impacts of Data Science'
    }},
    'SAS': {'name': 'Systems and Security', 'subtopics': {
        'HW': 'Hardware and Software',
        'NW': 'Networks',
        'SC': 'Security',
        'IM': 'Impacts of Computing Systems'
    }},
    'CAS': {'name': 'Computing and Society', 'subtopics': {
        'HC': 'History of Computing',
        'ET': 'Emerging Technologies',
        'CE': 'Career Exploration'
    }}
}

standards = []

# Extract all K-8 standard codes and descriptions
# Pattern matches: E[K12345]-XXX-YY-NN or MS-XXX-YY-NN followed by description
pattern = r'(E[K12345]|MS)-([A-Z]{3})-([A-Z]{2})-(\d{2})\.\s+([^\n<]+?)(?:\n|<|$)'

for match in re.finditer(pattern, content, re.MULTILINE):
    grade_prefix = match.group(1)
    topic_area = match.group(2)
    subtopic = match.group(3)
    number = match.group(4)
    description = match.group(5).strip()

    code = f"{grade_prefix}-{topic_area}-{subtopic}-{number}"

    # Skip if not a K-8 topic area
    if topic_area not in topic_areas:
        continue

    # Determine grade band
    if grade_prefix == 'MS':
        grade_band = 'Middle School'
        grade = 'MS'
        grade_level = '6-8'
    else:
        grade_band = 'Elementary'
        grade = grade_prefix
        # Map to actual grade
        grade_map = {'EK': 'K', 'E1': '1', 'E2': '2', 'E3': '3', 'E4': '4', 'E5': '5'}
        grade_level = grade_map.get(grade_prefix, grade_prefix)

    standards.append({
        'code': code,
        'grade_band': grade_band,
        'grade': grade,
        'grade_level': grade_level,
        'topic_area': topic_area,
        'topic_area_name': topic_areas[topic_area]['name'],
        'subtopic': subtopic,
        'subtopic_name': topic_areas[topic_area]['subtopics'].get(subtopic, subtopic),
        'number': number,
        'description': description
    })

# Remove duplicates (same code)
seen_codes = set()
unique_standards = []
for std in standards:
    if std['code'] not in seen_codes:
        seen_codes.add(std['code'])
        unique_standards.append(std)

standards = unique_standards

print(f"Extracted {len(standards)} unique K-8 CSTA standards")

# Organize by topic area and grade
by_topic_grade = {}
for topic_code in topic_areas.keys():
    by_topic_grade[topic_code] = {}
    for grade in ['EK', 'E1', 'E2', 'E3', 'E4', 'E5', 'MS']:
        by_topic_grade[topic_code][grade] = []

for std in standards:
    by_topic_grade[std['topic_area']][std['grade']].append(std)

# Print summary
print("\n=== Standards by Topic Area and Grade ===")
for topic_code in ['ALG', 'PRO', 'DAA', 'SAS', 'CAS']:
    print(f"\n{topic_code}: {topic_areas[topic_code]['name']}")
    total = 0
    for grade in ['EK', 'E1', 'E2', 'E3', 'E4', 'E5', 'MS']:
        count = len(by_topic_grade[topic_code][grade])
        total += count
        if count > 0:
            print(f"  {grade}: {count} standards")
    print(f"  TOTAL: {total}")

# Organize by subtopic for easier reference
by_subtopic = {}
for std in standards:
    key = f"{std['topic_area']}-{std['subtopic']}"
    if key not in by_subtopic:
        by_subtopic[key] = {
            'topic_area': std['topic_area'],
            'topic_area_name': std['topic_area_name'],
            'subtopic': std['subtopic'],
            'subtopic_name': std['subtopic_name'],
            'standards': []
        }
    by_subtopic[key]['standards'].append(std)

# Save to JSON for use by other scripts
output = {
    'topic_areas': topic_areas,
    'standards': standards,
    'by_topic_grade': by_topic_grade,
    'by_subtopic': by_subtopic,
    'total_count': len(standards)
}

with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/csta_standards_extracted.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"\nSaved {len(standards)} standards to csta_standards_extracted.json")

# Show some examples
print("\n=== Sample Standards ===")
for i, std in enumerate(standards[:5]):
    print(f"{std['code']}: {std['description'][:80]}...")
