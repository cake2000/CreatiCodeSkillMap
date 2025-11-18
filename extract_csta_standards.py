#!/usr/bin/env python3
"""
Extract all K-8 CSTA standards from the cstastandard.md file
and organize them by domain and grade level.
"""
import json
import re

# Read the CSTA standards markdown file
with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/cstastandard.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Define standard code patterns for K-8
# Elementary: EK, E1, E2, E3, E4, E5
# Middle School: MS
# Not included: HS (high school), S1/S2 (specialty)

standards = []

# Extract all EK through E5 and MS standards
# Pattern: E[K12345]-[A-Z]{3}-[A-Z]{2}-\d{2}
elementary_pattern = r'(E[K12345]-[A-Z]{3}-[A-Z]{2}-\d{2})\.\s+([^\n]+)'
ms_pattern = r'(MS-[A-Z]{3}-[A-Z]{2}-\d{2})\.\s+([^\n]+)'

# Find all elementary standards
for match in re.finditer(elementary_pattern, content):
    code = match.group(1)
    description = match.group(2).strip()

    # Parse code parts
    parts = code.split('-')
    grade = parts[0]  # EK, E1, E2, etc.
    topic_area = parts[1]  # ALG, PRO, DAA, SAS, CAS
    subtopic = parts[2]  # AF, PF, etc.

    standards.append({
        'code': code,
        'grade_band': 'Elementary',
        'grade': grade,
        'topic_area': topic_area,
        'subtopic': subtopic,
        'description': description
    })

# Find all middle school standards
for match in re.finditer(ms_pattern, content):
    code = match.group(1)
    description = match.group(2).strip()

    # Parse code parts
    parts = code.split('-')
    topic_area = parts[1]  # ALG, PRO, DAA, SAS, CAS
    subtopic = parts[2]  # AF, PF, etc.

    standards.append({
        'code': code,
        'grade_band': 'Middle School',
        'grade': 'MS',
        'topic_area': topic_area,
        'subtopic': subtopic,
        'description': description
    })

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

# Add full names to standards
for std in standards:
    std['topic_area_name'] = topic_areas[std['topic_area']]['name']
    std['subtopic_name'] = topic_areas[std['topic_area']]['subtopics'][std['subtopic']]

print(f"Extracted {len(standards)} K-8 CSTA standards")

# Organize by topic area and grade
by_topic = {}
for topic_code, topic_info in topic_areas.items():
    by_topic[topic_code] = {
        'name': topic_info['name'],
        'standards': {}
    }
    for grade in ['EK', 'E1', 'E2', 'E3', 'E4', 'E5', 'MS']:
        by_topic[topic_code]['standards'][grade] = []

for std in standards:
    by_topic[std['topic_area']]['standards'][std['grade']].append(std)

# Print summary
print("\n=== Standards by Topic Area and Grade ===")
for topic_code in ['ALG', 'PRO', 'DAA', 'SAS', 'CAS']:
    print(f"\n{topic_code}: {by_topic[topic_code]['name']}")
    for grade in ['EK', 'E1', 'E2', 'E3', 'E4', 'E5', 'MS']:
        count = len(by_topic[topic_code]['standards'][grade])
        if count > 0:
            print(f"  {grade}: {count} standards")

# Save to JSON for use by other scripts
output = {
    'topic_areas': topic_areas,
    'standards': standards,
    'by_topic': by_topic
}

with open('/media/binyu/USB2/dev/CreatiCodeSkillMap/csta_standards_extracted.json', 'w') as f:
    json.dump(output, f, indent=2)

print(f"\nSaved to csta_standards_extracted.json")
