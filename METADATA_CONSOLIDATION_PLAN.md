# CreatiCode Skill Map: Metadata Consolidation Plan

**Date:** 2025-11-17
**Purpose:** Step-by-step plan to enrich canonical skill file with all missing metadata

---

## Overview

This plan details the process to take **skills_k8_ai_complete.json** as the base and enrich it with:

1. Missing skills from **skills_final_enriched.json**
2. Domain IDs and domain names
3. Topic names
4. CSTA standards codes
5. AI4K12 categories
6. Competition tags
7. Difficulty tracks
8. Gateway and capstone flags
9. Dependency counts

**Target Output:** CANONICAL_SKILLS.json with 1,234+ fully enriched skills

---

## Phase 1: Skill Merge and Deduplication

### Step 1.1: Load Source Files

```python
import json

# Load primary source (base)
with open('skills_k8_ai_complete.json', 'r') as f:
    k8_ai_skills = json.load(f)

# Load secondary source (for missing skills)
with open('skills_final_enriched.json', 'r') as f:
    final_enriched_skills = json.load(f)

print(f"K8 AI Complete: {len(k8_ai_skills)} skills")
print(f"Final Enriched: {len(final_enriched_skills)} skills")
```

**Expected Output:**
```
K8 AI Complete: 1119 skills
Final Enriched: 1155 skills
```

---

### Step 1.2: Identify Unique Skills

```python
# Create ID sets
k8_ai_ids = set(skill['id'] for skill in k8_ai_skills)
final_enriched_ids = set(skill['id'] for skill in final_enriched_skills)

# Find unique skills
only_in_k8_ai = k8_ai_ids - final_enriched_ids
only_in_final = final_enriched_ids - k8_ai_ids
common_skills = k8_ai_ids & final_enriched_ids

print(f"Only in k8_ai_complete: {len(only_in_k8_ai)}")
print(f"Only in final_enriched: {len(only_in_final)}")
print(f"Common to both: {len(common_skills)}")

# Analyze unique skills by grade
for skill_id in sorted(only_in_k8_ai):
    skill = next(s for s in k8_ai_skills if s['id'] == skill_id)
    print(f"  {skill_id} (Grade {skill['grade']}): {skill['title'][:50]}...")

for skill_id in sorted(only_in_final):
    skill = next(s for s in final_enriched_skills if s['id'] == skill_id)
    print(f"  {skill_id} (Grade {skill['grade']}): {skill['title'][:50]}...")
```

**Expected Results:**
- only_in_k8_ai: ~61 (Kindergarten skills) + ~18 (Grade 3-8 AI skills)
- only_in_final: ~115 (Grade 1-2 skills)
- Common: ~1,040 skills

---

### Step 1.3: Merge Unique Skills from final_enriched

```python
# Start with k8_ai_complete as base
canonical_skills = k8_ai_skills.copy()

# Add unique skills from final_enriched
for skill_id in only_in_final:
    skill = next(s for s in final_enriched_skills if s['id'] == skill_id)

    # Convert final_enriched skill to k8_ai_complete format
    merged_skill = {
        'id': skill['id'],
        'title': skill['title'],
        'short_name': skill['short_name'],
        'topic_id': skill['topic_id'],
        'grade': skill['grade'],
        'description': skill['description'],
        'csta_code': skill['csta_code'],
        'dependencies': skill['dependencies'],

        # Add k8_ai-specific fields with defaults
        'description_teacher': skill['description'],  # Use same as description
        'student_prompt': None,
        'student_prompt_audio': None,
        'skill_type': 'coding_task',  # Default for G1-2
        'activity_type': 'guided_coding',  # Default
        'interaction_details': None,
        'auto_grade_rules': None,
        'accessibility': None,
        'notes_redesign': f"Merged from skills_final_enriched.json"
    }

    canonical_skills.append(merged_skill)

print(f"Merged canonical skills: {len(canonical_skills)}")

# Sort by ID
canonical_skills.sort(key=lambda s: s['id'])
```

**Expected Output:**
```
Merged canonical skills: 1234
```

---

### Step 1.4: Normalize Grade Format

```python
# Normalize grades to consistent format
for skill in canonical_skills:
    grade = skill['grade']

    # Convert to consistent format
    if grade == 'K' or grade == 'k':
        skill['grade'] = 'K'
    elif isinstance(grade, str) and grade.isdigit():
        skill['grade'] = int(grade)
    elif isinstance(grade, int):
        # Already correct
        pass
    else:
        print(f"WARNING: Unexpected grade format in {skill['id']}: {grade}")

# Validate grade distribution
from collections import Counter
grade_counts = Counter(skill['grade'] for skill in canonical_skills)
print("Grade distribution:", dict(grade_counts))
```

**Expected Output:**
```
Grade distribution: {'K': 61, 1: 202, 2: 233, 3: 143, 4: 146, 5: 149, 6: 148, 7: 145, 8: 149}
```

---

## Phase 2: Add Domain and Topic Metadata

### Step 2.1: Load Domain Mapping

```python
# Load domain mapping
with open('domain_mapping.json', 'r') as f:
    domain_mapping = json.load(f)

# Load topic names from domains_topics.yaml
import yaml
with open('domains_topics.yaml', 'r') as f:
    domains_topics = yaml.safe_load(f)

# Create topic_id -> topic_name mapping
topic_names = {
    topic['id']: topic['name']
    for topic in domains_topics['topics']
}

print(f"Loaded {len(domain_mapping)} domain mappings")
print(f"Loaded {len(topic_names)} topic names")
```

---

### Step 2.2: Apply Domain and Topic Metadata

```python
# Add domain_id, domain_name, and topic_name to all skills
for skill in canonical_skills:
    topic_id = skill['topic_id']

    # Add domain metadata
    if topic_id in domain_mapping:
        skill['domain_id'] = domain_mapping[topic_id]['domain_id']
        skill['domain_name'] = domain_mapping[topic_id]['domain_name']
    else:
        print(f"WARNING: No domain mapping for {topic_id} in skill {skill['id']}")
        skill['domain_id'] = 'Unknown'
        skill['domain_name'] = 'Unknown'

    # Add topic name
    if topic_id in topic_names:
        skill['topic_name'] = topic_names[topic_id]
    else:
        print(f"WARNING: No topic name for {topic_id} in skill {skill['id']}")
        skill['topic_name'] = 'Unknown'

# Validate
domains_used = set(skill['domain_id'] for skill in canonical_skills)
print(f"Domains used: {sorted(domains_used)}")

topics_used = set(skill['topic_id'] for skill in canonical_skills)
print(f"Topics covered: {len(topics_used)} of 36")
```

**Expected Output:**
```
Domains used: ['D1', 'D2', 'D3', 'D4', 'D5']
Topics covered: 36 of 36
```

---

## Phase 3: Add CSTA Standards Codes

### Step 3.1: Parse Existing CSTA Codes

```python
from collections import defaultdict

# Analyze existing CSTA codes
csta_by_topic_grade = defaultdict(list)

for skill in canonical_skills:
    if skill['csta_code'] and skill['csta_code'] != '':
        key = (skill['topic_id'], skill['grade'])
        csta_by_topic_grade[key].append({
            'id': skill['id'],
            'csta_code': skill['csta_code'],
            'title': skill['short_name']
        })

print(f"Skills with CSTA codes: {sum(1 for s in canonical_skills if s['csta_code'])}")
print("\nCoverage by topic:")
for topic_id in sorted(set(s['topic_id'] for s in canonical_skills)):
    topic_skills = [s for s in canonical_skills if s['topic_id'] == topic_id]
    with_csta = [s for s in topic_skills if s['csta_code']]
    print(f"  {topic_id}: {len(with_csta)}/{len(topic_skills)} ({100*len(with_csta)/len(topic_skills):.0f}%)")
```

---

### Step 3.2: Create CSTA Mapping Rules

```python
# Define CSTA mapping rules based on existing patterns and cstastandard.md

csta_mapping_rules = {
    # Domain D1: Algorithms and Design
    'T01': {  # Everyday Algorithms
        'K': '1A-AP-08',  # Model daily processes
        1: '1A-AP-08',
        2: '1A-AP-08',
        3: '1B-AP-08',  # Algorithms include sequences
        4: '1B-AP-08',
        5: '1B-AP-11',  # Decompose problems
        6: '2-AP-10',   # Algorithms in problem solving
        7: '2-AP-10',
        8: '2-AP-10'
    },
    'T02': {  # Representing & Tracing
        'K': '1A-AP-09',  # Model sequences
        1: '1A-AP-09',
        2: '1A-AP-09',
        3: '1B-AP-09',  # Create programs with sequences
        4: '1B-AP-09',
        5: '1B-AP-11',
        6: '2-AP-10',
        7: '2-AP-10',
        8: '2-AP-10'
    },
    'T03': {  # Decomposition
        3: '1B-AP-11',  # Decompose problems
        4: '1B-AP-11',
        5: '1B-AP-11',
        6: '2-AP-10',
        7: '2-AP-10',
        8: '2-AP-13'  # Decompose and define sub-problems
    },
    'T04': {  # Patterns
        3: '1B-AP-10',  # Pattern recognition
        4: '1B-AP-10',
        5: '1B-AP-10',
        6: '2-AP-11',  # Abstraction
        7: '2-AP-11',
        8: '2-AP-11'
    },
    'T05': {  # Human-Centered Design
        3: '1B-AP-12',  # Iterative design
        4: '1B-AP-12',
        5: '1B-AP-12',
        6: '2-AP-15',  # Design and iteratively develop
        7: '2-AP-15',
        8: '2-AP-15'
    },

    # Domain D2: Programming
    'T06': {  # Events & Sequencing
        1: '1A-AP-10',  # Programs with sequences and simple loops
        2: '1A-AP-10',
        3: '1B-AP-08',
        4: '1B-AP-08',
        5: '1B-AP-08',
        6: '2-AP-12',  # Programs with sequences, events
        7: '2-AP-12',
        8: '2-AP-12'
    },
    'T07': {  # Loops
        2: '1A-AP-10',  # Simple loops
        3: '1B-AP-09',  # Loops in programs
        4: '1B-AP-09',
        5: '1B-AP-12',  # Control structures
        6: '2-AP-12',
        7: '2-AP-13',
        8: '2-AP-13'
    },
    'T08': {  # Conditionals
        3: '1B-AP-09',  # Conditionals
        4: '1B-AP-09',
        5: '1B-AP-12',
        6: '2-AP-12',
        7: '2-AP-13',
        8: '2-AP-13'
    },
    'T09': {  # Variables
        3: '1B-AP-09',  # Variables
        4: '1B-AP-09',
        5: '2-AP-11',
        6: '2-AP-11',
        7: '2-AP-13',
        8: '2-AP-13'
    },
    'T10': {  # Lists & Tables
        4: '1B-AP-09',
        5: '2-AP-14',  # Data structures
        6: '2-AP-14',
        7: '2-AP-14',
        8: '2-AP-14'
    },
    'T11': {  # Functions
        4: '1B-AP-11',  # Decompose
        5: '2-AP-13',  # Modularization
        6: '2-AP-13',
        7: '2-AP-13',
        8: '2-AP-13'
    },
    'T12': {  # Program Organization
        4: '1B-AP-15',  # Code readability
        5: '2-AP-17',
        6: '2-AP-17',
        7: '2-AP-17',
        8: '2-AP-17'
    },
    'T13': {  # Testing & Debugging
        3: '1B-AP-13',  # Test and debug
        4: '1B-AP-13',
        5: '1B-AP-14',  # Troubleshooting
        6: '2-AP-17',
        7: '2-AP-17',
        8: '2-AP-17'
    },

    # Applications (T14-T24) - mostly programming domain
    'T14': {  # Games
        3: '1B-AP-09',
        4: '1B-AP-12',
        5: '2-AP-15',
        6: '2-AP-15',
        7: '2-AP-16',
        8: '2-AP-16'
    },
    'T15': {  # Stories & Animation
        2: '1A-AP-10',
        3: '1B-AP-09',
        4: '1B-AP-12',
        5: '2-AP-15',
        6: '2-AP-15',
        7: '2-AP-16',
        8: '2-AP-16'
    },

    # Domain D3: Data and Analysis
    'T25': {  # Data Representation
        'K': '1A-DA-06',  # Simple data
        1: '1A-DA-06',
        2: '1A-DA-06',
        3: '1B-DA-06',  # Store, access, manipulate data
        4: '1B-DA-06',
        5: '2-DA-07',
        6: '2-DA-07',
        7: '2-DA-08',
        8: '2-DA-08'
    },
    'T26': {  # Data Collection
        'K': '1A-DA-07',  # Collect and present data
        1: '1A-DA-07',
        2: '1A-DA-07',
        3: '1B-DA-07',
        4: '1B-DA-07',
        5: '2-DA-08',
        6: '2-DA-08',
        7: '2-DA-08',
        8: '2-DA-08'
    },
    'T27': {  # Data Analysis
        'K': '1A-DA-07',
        1: '1A-DA-07',
        2: '1A-DA-07',
        3: '1B-DA-07',
        4: '1B-DA-07',
        5: '2-DA-09',  # Refine computational models
        6: '2-DA-09',
        7: '2-DA-09',
        8: '2-DA-09'
    },

    # Domain D4: Systems and Security
    'T30': {  # Hardware
        'K': '1A-CS-01',  # Devices, hardware, software
        1: '1A-CS-01',
        2: '1A-CS-01',
        3: '1B-CS-01',
        4: '1B-CS-01',
        5: '2-CS-01',
        6: '2-CS-01',
        7: '2-CS-02',
        8: '2-CS-02'
    },
    'T31': {  # Internet & Networks
        1: '1A-NI-04',  # Networks and internet
        2: '1A-NI-04',
        3: '1B-NI-04',
        4: '1B-NI-04',
        5: '2-NI-04',
        6: '2-NI-05',
        7: '2-NI-05',
        8: '2-NI-05'
    },
    'T32': {  # Cybersecurity
        'K': '1A-NI-04',
        1: '1A-NI-04',
        2: '1A-NI-04',
        3: '1B-NI-05',  # Cybersecurity
        4: '1B-NI-05',
        5: '2-NI-06',
        6: '2-NI-06',
        7: '2-NI-06',
        8: '2-NI-06'
    },

    # Domain D5: Computing and Society
    'T34': {  # History
        3: '1B-IC-18',  # Computing history
        4: '1B-IC-18',
        5: '2-IC-20',
        6: '2-IC-20',
        7: '2-IC-20',
        8: '2-IC-20'
    },
    'T35': {  # Impacts
        'K': '1A-IC-16',  # Computing impacts
        1: '1A-IC-16',
        2: '1A-IC-17',
        3: '1B-IC-18',
        4: '1B-IC-18',
        5: '2-IC-20',
        6: '2-IC-20',
        7: '2-IC-20',
        8: '2-IC-20'
    },
    'T36': {  # Ethics & Careers
        'K': '1A-IC-18',  # Collaboration
        1: '1A-IC-18',
        2: '1A-IC-18',
        3: '1B-IC-19',  # Collaboration and communication
        4: '1B-IC-19',
        5: '2-IC-21',
        6: '2-IC-21',
        7: '2-IC-23',
        8: '2-IC-23'
    }
}

# Note: This is a simplified mapping. Real implementation should:
# 1. Parse cstastandard.md for complete standard descriptions
# 2. Review each skill individually for best CSTA match
# 3. Allow multiple CSTA codes per skill where appropriate
```

---

### Step 3.3: Apply CSTA Codes

```python
# Apply CSTA codes based on mapping rules
csta_applied = 0
csta_preserved = 0
csta_missing = 0

for skill in canonical_skills:
    topic_id = skill['topic_id']
    grade = skill['grade']

    # Preserve existing non-empty CSTA codes
    if skill.get('csta_code') and skill['csta_code'] != '':
        csta_preserved += 1
        continue

    # Apply mapping rule if available
    if topic_id in csta_mapping_rules:
        topic_rules = csta_mapping_rules[topic_id]
        if grade in topic_rules:
            skill['csta_code'] = topic_rules[grade]
            csta_applied += 1
        else:
            skill['csta_code'] = ''
            csta_missing += 1
    else:
        skill['csta_code'] = ''
        csta_missing += 1

print(f"CSTA codes preserved: {csta_preserved}")
print(f"CSTA codes applied: {csta_applied}")
print(f"CSTA codes still missing: {csta_missing}")
print(f"Total coverage: {100*(csta_preserved + csta_applied)/len(canonical_skills):.1f}%")
```

**Expected Output:**
```
CSTA codes preserved: 240
CSTA codes applied: ~700
CSTA codes still missing: ~294
Total coverage: 76.2%
```

---

## Phase 4: Add AI4K12 Categories

### Step 4.1: Load AI4K12 Mappings

```python
# Load AI4K12 mapping
with open('AI4K12_MAPPING.json', 'r') as f:
    ai4k12_data = json.load(f)

# Extract topic-level AI4K12 categories
topic_ai4k12_mapping = {}

for topic_key, topic_data in ai4k12_data['current_coverage'].items():
    if 'ai4k12_categories' in topic_data:
        # Extract topic ID from key (e.g., "T21_ai_media" -> "T21")
        topic_id = topic_key.split('_')[0]

        # Convert category descriptions to structured format
        categories = []
        for cat_desc in topic_data['ai4k12_categories']:
            # Parse format like "3_machine_learning (data, building_and_using_ai_models)"
            # Convert to ["3_machine_learning:data", "3_machine_learning:building_and_using_ai_models"]
            if '(' in cat_desc:
                main_cat = cat_desc.split('(')[0].strip()
                subcats = cat_desc.split('(')[1].split(')')[0].split(',')
                for subcat in subcats:
                    categories.append(f"{main_cat}:{subcat.strip()}")
            else:
                categories.append(cat_desc.strip())

        topic_ai4k12_mapping[topic_id] = categories

print(f"AI4K12 mappings for topics: {sorted(topic_ai4k12_mapping.keys())}")
```

---

### Step 4.2: Apply AI4K12 Categories

```python
# Apply AI4K12 categories to relevant skills
ai4k12_applied = 0

for skill in canonical_skills:
    topic_id = skill['topic_id']

    # Initialize field
    if 'ai4k12_categories' not in skill:
        skill['ai4k12_categories'] = []

    # Apply if topic has AI4K12 mapping
    if topic_id in topic_ai4k12_mapping:
        skill['ai4k12_categories'] = topic_ai4k12_mapping[topic_id].copy()
        ai4k12_applied += 1

print(f"Skills with AI4K12 categories: {ai4k12_applied}")

# Breakdown by topic
for topic_id in sorted(topic_ai4k12_mapping.keys()):
    count = sum(1 for s in canonical_skills if s['topic_id'] == topic_id)
    print(f"  {topic_id}: {count} skills")
```

**Expected Output:**
```
Skills with AI4K12 categories: ~166
  T21: ~25 skills
  T22: ~24 skills
  T23: ~24 skills
  T24: ~22 skills
  T35: ~36 skills
  T36: ~35 skills
```

---

## Phase 5: Add Competition Tags

### Step 5.1: Parse Competition Paths

```python
# Parse competition_paths.md to extract skill-to-competition mappings
# This is a manual process - create mapping based on document

competition_mapping_rules = {
    # Topic-based rules
    'topic_rules': {
        'T01': {
            (3, 4, 5): ['ACSL Elementary', 'NOC Elementary'],
            (6, 7, 8): ['ACSL Junior', 'NOC Junior']
        },
        'T02': {
            (3, 4, 5): ['ACSL Elementary'],
            (6, 7, 8): ['ACSL Junior', 'NOC Junior']
        },
        'T04': {
            (4, 5, 6): ['Lanqiao Scratch Junior'],
            (6, 7, 8): ['ACSL Junior', 'Lanqiao Scratch Senior', 'NOC Junior']
        },
        'T07': {
            (2, 3): ['Scratch Olympiad Elementary'],
            (4, 5): ['Scratch Olympiad Junior', 'Lanqiao Scratch Junior'],
            (6, 7, 8): ['ACSL Junior', 'Lanqiao Scratch Senior']
        },
        'T08': {
            (3, 4, 5): ['ACSL Elementary', 'Scratch Olympiad Junior'],
            (6, 7, 8): ['ACSL Junior']
        },
        'T09': {
            (3, 4, 5): ['ACSL Elementary'],
            (4, 5, 6): ['Scratch Olympiad Junior', 'Lanqiao Scratch Junior'],
            (6, 7, 8): ['ACSL Junior', 'Lanqiao Scratch Senior']
        },
        'T10': {
            (6, 7, 8): ['ACSL Junior']
        },
        'T11': {
            (4, 5, 6): ['Scratch Olympiad Junior'],
            (6, 7, 8): ['ACSL Junior', 'Lanqiao Scratch Senior', 'NOC Junior']
        },
        'T13': {
            (3, 4, 5): ['ACSL Elementary'],
            (6, 7, 8): ['ACSL Junior']
        },
        'T14': {
            (3, 4, 5): ['Scratch Olympiad Elementary', 'NOC Elementary'],
            (4, 5, 6): ['Scratch Olympiad Junior', 'Games for Change'],
            (6, 7, 8): ['NOC Junior', 'Games for Change']
        },
        'T15': {
            (2, 3, 4, 5): ['Scratch Olympiad Elementary'],
            (4, 5, 6): ['Scratch Olympiad Junior'],
            (4, 5, 6, 7, 8): ['Games for Change']
        },
        'T20': {
            (6, 7, 8): ['NOC Junior', 'ICode Global Hackathon']
        },
        'T21': {
            (4, 5, 6, 7, 8): ['CreatiCode XO Challenge']
        },
        'T22': {
            (4, 5, 6, 7, 8): ['CreatiCode XO Challenge']
        },
        'T23': {
            (4, 5, 6, 7, 8): ['CreatiCode XO Challenge']
        },
        'T24': {
            (4, 5, 6, 7, 8): ['CreatiCode XO Challenge']
        },
        'T25': {
            (6, 7, 8): ['ACSL Junior']
        },
        'T26': {
            (6, 7, 8): ['Congressional App Challenge']
        },
        'T27': {
            (6, 7, 8): ['ACSL Junior']
        },
        'T31': {
            (6, 7, 8): ['Congressional App Challenge', 'ICode Global Hackathon']
        },
        'T32': {
            (6, 7, 8): ['Congressional App Challenge']
        },
        'T36': {
            (4, 5, 6, 7, 8): ['Games for Change', 'Congressional App Challenge', 'ICode Global Hackathon']
        }
    }
}

def get_competition_tags(topic_id, grade):
    """Get competition tags for a skill based on topic and grade"""
    tags = []

    if topic_id not in competition_mapping_rules['topic_rules']:
        return tags

    topic_rules = competition_mapping_rules['topic_rules'][topic_id]

    for grade_tuple, competitions in topic_rules.items():
        if grade in grade_tuple:
            tags.extend(competitions)

    return list(set(tags))  # Remove duplicates
```

---

### Step 5.2: Apply Competition Tags

```python
# Apply competition tags
competition_applied = 0

for skill in canonical_skills:
    topic_id = skill['topic_id']
    grade = skill['grade']

    # Skip kindergarten
    if grade == 'K':
        skill['competition_tags'] = []
        continue

    # Get applicable competitions
    tags = get_competition_tags(topic_id, grade)
    skill['competition_tags'] = tags

    if tags:
        competition_applied += 1

print(f"Skills with competition tags: {competition_applied}")

# Summary by competition
from collections import Counter
all_tags = [tag for s in canonical_skills for tag in s.get('competition_tags', [])]
tag_counts = Counter(all_tags)
print("\nCompetition tag counts:")
for tag, count in sorted(tag_counts.items()):
    print(f"  {tag}: {count} skills")
```

**Expected Output:**
```
Skills with competition tags: ~600
Competition tag counts:
  ACSL Elementary: ~120 skills
  ACSL Junior: ~180 skills
  Congressional App Challenge: ~50 skills
  CreatiCode XO Challenge: ~80 skills
  Games for Change: ~60 skills
  ICode Global Hackathon: ~40 skills
  Lanqiao Scratch Junior: ~70 skills
  Lanqiao Scratch Senior: ~50 skills
  NOC Elementary: ~60 skills
  NOC Junior: ~80 skills
  Scratch Olympiad Elementary: ~80 skills
  Scratch Olympiad Junior: ~90 skills
```

---

## Phase 6: Add Difficulty Tracks

### Step 6.1: Load Track Categorization

```python
# Load difficulty track data
with open('SKILL_TRACK_CATEGORIZATION.json', 'r') as f:
    track_data = json.load(f)

# Build skill ID to track mapping
skill_track_mapping = {}

# Competition track
for skill_entry in track_data['track_assignments']['competition_track']:
    skill_track_mapping[skill_entry['id']] = 'competition'

# Enrichment track (advanced but appropriate)
for skill_entry in track_data['track_assignments']['enrichment_track_advanced_but_appropriate']:
    skill_track_mapping[skill_entry['id']] = 'enrichment'

# Too advanced for standard -> enrichment
for skill_entry in track_data['track_assignments']['too_advanced_for_standard']:
    if skill_entry['track'] == 'enrichment':
        skill_track_mapping[skill_entry['id']] = 'enrichment'

print(f"Loaded track assignments for {len(skill_track_mapping)} skills")
```

---

### Step 6.2: Apply Difficulty Tracks

```python
# Apply difficulty tracks
track_counts = {'standard': 0, 'enrichment': 0, 'competition': 0}

for skill in canonical_skills:
    skill_id = skill['id']

    # Check if explicitly categorized
    if skill_id in skill_track_mapping:
        skill['difficulty_track'] = skill_track_mapping[skill_id]
        track_counts[skill_track_mapping[skill_id]] += 1
    else:
        # Default to standard
        skill['difficulty_track'] = 'standard'
        track_counts['standard'] += 1

print("Difficulty track distribution:")
for track, count in track_counts.items():
    print(f"  {track}: {count} ({100*count/len(canonical_skills):.1f}%)")
```

**Expected Output:**
```
Difficulty track distribution:
  standard: ~1200 (97.2%)
  enrichment: ~25 (2.0%)
  competition: ~9 (0.8%)
```

---

## Phase 7: Calculate Dependency Metadata

### Step 7.1: Calculate Dependency Counts

```python
# Calculate dependency counts
for skill in canonical_skills:
    deps = skill.get('dependencies', [])
    skill['dependency_count'] = len(deps)

# Validate
avg_deps = sum(s['dependency_count'] for s in canonical_skills) / len(canonical_skills)
max_deps = max(s['dependency_count'] for s in canonical_skills)
skill_max_deps = next(s for s in canonical_skills if s['dependency_count'] == max_deps)

print(f"Average dependencies per skill: {avg_deps:.2f}")
print(f"Max dependencies: {max_deps} (skill {skill_max_deps['id']})")
```

---

### Step 7.2: Identify Gateway Skills

```python
# Gateway skills: 5+ dependencies within same topic
for skill in canonical_skills:
    deps = skill.get('dependencies', [])
    topic_id = skill['topic_id']

    # Count dependencies from same topic
    same_topic_deps = [d for d in deps if d.startswith(topic_id + '.')]

    skill['is_gateway'] = len(same_topic_deps) >= 5

gateway_count = sum(1 for s in canonical_skills if s['is_gateway'])
print(f"Gateway skills identified: {gateway_count}")

# Show examples
gateway_skills = [s for s in canonical_skills if s['is_gateway']][:5]
for skill in gateway_skills:
    same_topic = [d for d in skill['dependencies'] if d.startswith(skill['topic_id'] + '.')]
    print(f"  {skill['id']}: {skill['short_name']} ({len(same_topic)} same-topic deps)")
```

---

### Step 7.3: Identify Capstone Skills

```python
# Capstone skills: depended on by 5+ other skills
from collections import Counter

# Count how many times each skill appears in dependencies
skill_dependency_counts = Counter()

for skill in canonical_skills:
    for dep in skill.get('dependencies', []):
        skill_dependency_counts[dep] += 1

# Mark capstones
for skill in canonical_skills:
    skill_id = skill['id']
    skill['is_capstone'] = skill_dependency_counts[skill_id] >= 5

capstone_count = sum(1 for s in canonical_skills if s['is_capstone'])
print(f"Capstone skills identified: {capstone_count}")

# Show top capstones
capstones = sorted(
    [(s['id'], s['short_name'], skill_dependency_counts[s['id']])
     for s in canonical_skills if s['is_capstone']],
    key=lambda x: x[2],
    reverse=True
)[:10]

print("\nTop capstone skills:")
for skill_id, name, count in capstones:
    print(f"  {skill_id}: {name} (depended on by {count} skills)")
```

---

## Phase 8: Validation and Quality Checks

### Step 8.1: Validate Required Fields

```python
required_fields = [
    'id', 'title', 'short_name', 'topic_id', 'topic_name',
    'domain_id', 'domain_name', 'grade', 'description',
    'csta_code', 'ai4k12_categories', 'difficulty_track',
    'competition_tags', 'dependencies', 'dependency_count',
    'is_gateway', 'is_capstone'
]

validation_errors = []

for skill in canonical_skills:
    for field in required_fields:
        if field not in skill:
            validation_errors.append(f"Missing field '{field}' in skill {skill.get('id', 'UNKNOWN')}")

if validation_errors:
    print(f"VALIDATION ERRORS: {len(validation_errors)}")
    for error in validation_errors[:10]:
        print(f"  - {error}")
else:
    print("All required fields present!")
```

---

### Step 8.2: Validate Dependencies

```python
# Check for broken dependency references
all_skill_ids = set(s['id'] for s in canonical_skills)
broken_deps = []

for skill in canonical_skills:
    for dep in skill.get('dependencies', []):
        if dep not in all_skill_ids:
            broken_deps.append({
                'skill': skill['id'],
                'broken_dep': dep
            })

if broken_deps:
    print(f"WARNING: {len(broken_deps)} broken dependencies found")
    for item in broken_deps[:10]:
        print(f"  {item['skill']} -> {item['broken_dep']}")
else:
    print("All dependencies valid!")
```

---

### Step 8.3: Validate Data Types

```python
# Check data types
type_errors = []

for skill in canonical_skills:
    # Grade should be string 'K' or integer 1-8
    if not (skill['grade'] == 'K' or (isinstance(skill['grade'], int) and 1 <= skill['grade'] <= 8)):
        type_errors.append(f"{skill['id']}: Invalid grade {skill['grade']}")

    # Arrays should be arrays
    if not isinstance(skill.get('dependencies', []), list):
        type_errors.append(f"{skill['id']}: dependencies not a list")

    if not isinstance(skill.get('ai4k12_categories', []), list):
        type_errors.append(f"{skill['id']}: ai4k12_categories not a list")

    if not isinstance(skill.get('competition_tags', []), list):
        type_errors.append(f"{skill['id']}: competition_tags not a list")

    # Booleans should be booleans
    if not isinstance(skill.get('is_gateway', False), bool):
        type_errors.append(f"{skill['id']}: is_gateway not a boolean")

    if not isinstance(skill.get('is_capstone', False), bool):
        type_errors.append(f"{skill['id']}: is_capstone not a boolean")

if type_errors:
    print(f"TYPE ERRORS: {len(type_errors)}")
    for error in type_errors[:10]:
        print(f"  - {error}")
else:
    print("All data types valid!")
```

---

## Phase 9: Generate Final Output

### Step 9.1: Save Canonical Skills File

```python
# Save to CANONICAL_SKILLS.json
with open('CANONICAL_SKILLS.json', 'w') as f:
    json.dump(canonical_skills, f, indent=2, ensure_ascii=False)

print(f"Saved {len(canonical_skills)} skills to CANONICAL_SKILLS.json")
print(f"File size: {os.path.getsize('CANONICAL_SKILLS.json') / 1024 / 1024:.2f} MB")
```

---

### Step 9.2: Generate Statistics Report

```python
# Generate comprehensive statistics
stats = {
    'total_skills': len(canonical_skills),
    'by_grade': dict(Counter(s['grade'] for s in canonical_skills)),
    'by_domain': dict(Counter(s['domain_id'] for s in canonical_skills)),
    'by_topic': dict(Counter(s['topic_id'] for s in canonical_skills)),
    'by_difficulty_track': dict(Counter(s['difficulty_track'] for s in canonical_skills)),
    'metadata_coverage': {
        'csta_codes': sum(1 for s in canonical_skills if s.get('csta_code', '') != ''),
        'ai4k12_categories': sum(1 for s in canonical_skills if s.get('ai4k12_categories', [])),
        'competition_tags': sum(1 for s in canonical_skills if s.get('competition_tags', [])),
        'dependencies': sum(1 for s in canonical_skills if s.get('dependencies', [])),
    },
    'dependency_stats': {
        'avg_dependencies': sum(s['dependency_count'] for s in canonical_skills) / len(canonical_skills),
        'max_dependencies': max(s['dependency_count'] for s in canonical_skills),
        'gateway_skills': sum(1 for s in canonical_skills if s['is_gateway']),
        'capstone_skills': sum(1 for s in canonical_skills if s['is_capstone']),
    }
}

# Save statistics
with open('CANONICAL_SKILLS_STATISTICS.json', 'w') as f:
    json.dump(stats, f, indent=2)

print("\nCanonical Skills Statistics:")
print(f"  Total skills: {stats['total_skills']}")
print(f"  CSTA coverage: {100*stats['metadata_coverage']['csta_codes']/stats['total_skills']:.1f}%")
print(f"  AI4K12 coverage: {stats['metadata_coverage']['ai4k12_categories']} skills")
print(f"  Competition tags: {stats['metadata_coverage']['competition_tags']} skills")
print(f"  Gateway skills: {stats['dependency_stats']['gateway_skills']}")
print(f"  Capstone skills: {stats['dependency_stats']['capstone_skills']}")
```

---

## Success Metrics

Upon completion, the canonical file should have:

- **1,234+ skills** (K-8 complete coverage)
- **100% domain/topic metadata** (all skills have domain_id, domain_name, topic_name)
- **75%+ CSTA coverage** (meaningful CSTA codes for most skills)
- **~166 skills with AI4K12 categories** (T21-T24, T35-T36)
- **~600 skills with competition tags** (competition-relevant skills tagged)
- **All skills with difficulty_track** (standard/enrichment/competition)
- **All skills with valid dependency metadata** (dependency_count, is_gateway, is_capstone)
- **No broken dependencies** (all referenced skill IDs exist)
- **Consistent data types** (grades normalized, arrays are arrays, booleans are booleans)

---

## Next Steps After Consolidation

1. **Archive old skill files** per FILE_DEPRECATION_PLAN.md
2. **Update all documentation** to reference CANONICAL_SKILLS.json
3. **Update build scripts** to use CANONICAL_SKILLS.json
4. **Create visualizations** of skill map structure
5. **Generate teacher documentation** from canonical data
6. **Implement skill map UI** using canonical schema

---

**End of Consolidation Plan**
