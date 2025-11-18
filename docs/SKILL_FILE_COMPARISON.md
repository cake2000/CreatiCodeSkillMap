# CreatiCode Skill Map: Detailed File Comparison

**Date:** 2025-11-17
**Purpose:** Side-by-side comparison of all candidate skill files

---

## Quick Reference Table

| Metric | skills_k8_ai_complete.json | skills_final_enriched.json | skills_complete_k8.json | Canonical Target |
|--------|---------------------------|---------------------------|------------------------|------------------|
| **Total Skills** | 1,119 | 1,155 | 1,086 | **1,234+** |
| **File Size** | 1.1M | 864K | 1.1M | ~1.3M |
| **Last Modified** | 2025-11-17 11:05 | 2025-11-17 08:04 | 2025-11-17 10:17 | TBD |
| | | | | |
| **Grade Coverage** | | | | |
| Kindergarten | ✅ 61 | ❌ 0 | Unknown | **✅ 61** |
| Grade 1 | 69 | 133 | Unknown | **✅ 202** |
| Grade 2 | 91 | 142 | Unknown | **✅ 233** |
| Grade 3 | 146 | 143 | Unknown | **✅ 146** |
| Grade 4 | 149 | 146 | Unknown | **✅ 149** |
| Grade 5 | 152 | 149 | Unknown | **✅ 152** |
| Grade 6 | 151 | 148 | Unknown | **✅ 151** |
| Grade 7 | 148 | 145 | Unknown | **✅ 148** |
| Grade 8 | 152 | 149 | Unknown | **✅ 152** |
| | | | | |
| **Metadata Fields** | | | | |
| id, title, short_name | ✅ | ✅ | ✅ | **✅** |
| topic_id | ✅ | ✅ | ✅ | **✅** |
| topic_name | ❌ | ✅ | Unknown | **✅** |
| domain_id | ❌ | ⚠️ Unknown | Unknown | **✅** |
| domain_name | ❌ | ⚠️ Unknown | Unknown | **✅** |
| grade | ✅ | ✅ | ✅ | **✅** |
| description | ✅ | ✅ | ✅ | **✅** |
| description_teacher | ✅ | ❌ | Unknown | **✅** |
| student_prompt | ✅ | ❌ | Unknown | **✅** |
| student_prompt_audio | ✅ | ❌ | Unknown | **✅** |
| skill_type | ✅ | ❌ | Unknown | **✅** |
| activity_type | ✅ | ❌ | Unknown | **✅** |
| interaction_details | ✅ | ❌ | Unknown | **✅** |
| auto_grade_rules | ✅ | ❌ | Unknown | **✅** |
| accessibility | ✅ | ❌ | Unknown | **✅** |
| csta_code | ✅ 240 | ✅ 2 | Unknown | **✅ 940+** |
| ai4k12_categories | ❌ | ❌ | Unknown | **✅** |
| difficulty_track | ❌ | ❌ | Unknown | **✅** |
| competition_tags | ❌ | ❌ | Unknown | **✅** |
| dependencies | ✅ | ✅ | ✅ | **✅** |
| dependency_count | ❌ | ✅ | Unknown | **✅** |
| is_gateway | ❌ | ✅ | Unknown | **✅** |
| is_capstone | ❌ | ✅ | Unknown | **✅** |
| notes_redesign | ✅ | ❌ | Unknown | **✅** |
| | | | | |
| **Content Completeness** | | | | |
| CSTA Codes Populated | 21% (240) | 0.2% (2) | Unknown | **75%+ (940+)** |
| AI4K12 Categories | 0% | 0% | Unknown | **13% (166)** |
| Competition Tags | 0% | 0% | Unknown | **49% (600)** |
| Difficulty Tracks | 0% | 0% | Unknown | **100% (1,234)** |

---

## Field-by-Field Analysis

### Core Identification (All Files)

```json
// Present in all files
{
  "id": "T07.G4.02",
  "title": "Use a loop with a condition...",
  "short_name": "Repeat until loop...",
  "topic_id": "T07",
  "grade": 4
}
```

✅ No issues - all files consistent

---

### Taxonomy Classification

#### skills_k8_ai_complete.json
```json
{
  "topic_id": "T07",
  // topic_name: MISSING
  // domain_id: MISSING
  // domain_name: MISSING
}
```
❌ Missing taxonomy fields

#### skills_final_enriched.json
```json
{
  "topic_id": "T07",
  "topic_name": "Loops & Repetition",
  "domain": null,
  "domain_id": "Unknown",    // ⚠️ Placeholder
  "domain_name": "Unknown"   // ⚠️ Placeholder
}
```
⚠️ Has fields but values are "Unknown"

#### Canonical Target
```json
{
  "topic_id": "T07",
  "topic_name": "Loops & Repetition",
  "domain_id": "D2",
  "domain_name": "Programming"
}
```
✅ Complete and accurate

**Source:** domain_mapping.json + domains_topics.yaml

---

### Content Description

#### skills_k8_ai_complete.json (K-2 Skills)
```json
{
  "description": "Students practice sequencing...",
  "description_teacher": "Students practice sequencing...",  // ✅ Present
  "student_prompt": "Put the pictures in order...",          // ✅ Present
  "student_prompt_audio": {                                  // ✅ Present
    "tts_text": "Put the pictures in order...",
    "voice_settings": {...}
  }
}
```
✅ Rich content for K-2

#### skills_final_enriched.json (All Grades)
```json
{
  "description": "Students create a sequence...",
  // description_teacher: MISSING
  // student_prompt: MISSING
  // student_prompt_audio: MISSING
}
```
❌ Missing student-facing content

---

### Activity Design

#### skills_k8_ai_complete.json
```json
{
  "skill_type": "picture_based_digital",          // ✅ Present
  "activity_type": "drag_drop_sequence",          // ✅ Present
  "interaction_details": {                        // ✅ Present
    "item_count": 3,
    "items": [...],
    "interaction_mode": "drag_to_slots",
    "visual_theme": "animals_pets",
    "estimated_time_minutes": 2,
    "randomization": {...}
  },
  "auto_grade_rules": {                           // ✅ Present
    "type": "sequence_order",
    "correct_answer": [...],
    "feedback": {...},
    "retry_logic": {...}
  },
  "accessibility": {                               // ✅ Present
    "audio_support": true,
    "keyboard_navigable": true,
    ...
  }
}
```
✅ Complete activity design metadata (K-2 primarily)

#### skills_final_enriched.json
```json
{
  // skill_type: MISSING
  // activity_type: MISSING
  // interaction_details: MISSING
  // auto_grade_rules: MISSING
  // accessibility: MISSING
}
```
❌ No activity design metadata

---

### Standards Alignment

#### skills_k8_ai_complete.json
```json
{
  "csta_code": "1A-AP-08"  // ✅ 240 skills (21%)
  // ai4k12_categories: MISSING
}
```
✅ Better CSTA coverage
❌ No AI4K12

#### skills_final_enriched.json
```json
{
  "csta_code": ""  // ⚠️ 2 skills only (0.2%)
  // ai4k12_categories: MISSING
}
```
❌ Almost no CSTA
❌ No AI4K12

#### Canonical Target
```json
{
  "csta_code": "1A-AP-08",              // ✅ 75%+ coverage
  "ai4k12_categories": [                // ✅ For AI topics
    "3_machine_learning:data",
    "4_ethical_ai:ethical_evaluation"
  ]
}
```
✅ Complete standards coverage

---

### Difficulty and Competition

#### Both Current Files
```json
{
  // difficulty_track: MISSING
  // competition_tags: MISSING
}
```
❌ No difficulty or competition metadata in any current file

#### Canonical Target
```json
{
  "difficulty_track": "standard",       // ✅ All skills
  "competition_tags": [                 // ✅ Relevant skills
    "ACSL Elementary",
    "Scratch Olympiad Junior"
  ]
}
```
✅ Complete difficulty and competition metadata

**Sources:**
- difficulty_track: SKILL_TRACK_CATEGORIZATION.json
- competition_tags: competition_paths.md

---

### Dependencies and Structure

#### skills_k8_ai_complete.json
```json
{
  "dependencies": ["T07.G3.01", "T06.G3.01"]  // ✅ Present
  // dependency_count: MISSING
  // is_gateway: MISSING
  // is_capstone: MISSING
}
```
✅ Has dependencies
❌ Missing calculated fields

#### skills_final_enriched.json
```json
{
  "dependencies": ["T07.G3.01", "T06.G3.01"],  // ✅ Present
  "dependency_count": 2,                        // ✅ Present
  "is_gateway": false,                          // ✅ Present
  "is_capstone": false                          // ✅ Present
}
```
✅ Complete dependency metadata

#### Canonical Target
```json
{
  "dependencies": ["T07.G3.01", "T06.G3.01"],
  "dependency_count": 2,
  "is_gateway": false,
  "is_capstone": true
}
```
✅ All dependency fields + recalculated flags

---

## Unique Strengths by File

### skills_k8_ai_complete.json (Chosen as Base)

**Unique Strengths:**
1. ✅ **Only file with Kindergarten** (61 skills)
2. ✅ **Rich K-2 activity design** (interaction_details, auto_grade_rules, accessibility)
3. ✅ **Better CSTA coverage** (240 vs 2 skills)
4. ✅ **AI topic skills included** (110 skills in T21-T24)
5. ✅ **Student-facing content** (prompts, audio)
6. ✅ **Teacher-facing content** (description_teacher)

**Weaknesses:**
1. ❌ Missing 115 Grade 1-2 skills present in final_enriched
2. ❌ No domain_id/domain_name
3. ❌ No topic_name
4. ❌ No dependency_count
5. ❌ No is_gateway/is_capstone

**Why Chosen:** Kindergarten coverage and rich instructional metadata are irreplaceable; weaknesses are easily fixed by merging and enrichment.

---

### skills_final_enriched.json (Secondary Source)

**Unique Strengths:**
1. ✅ **More Grade 1-2 skills** (133 + 142 = 275 vs 160)
2. ✅ **Has topic_name**
3. ✅ **Has domain_id/domain_name fields** (though set to "Unknown")
4. ✅ **Complete dependency metadata** (dependency_count, is_gateway, is_capstone)

**Weaknesses:**
1. ❌ No Kindergarten (0 skills)
2. ❌ No K-2 activity design metadata
3. ❌ Almost no CSTA codes (2 skills)
4. ❌ No student-facing content
5. ❌ No teacher-specific descriptions

**Role:** Source for missing Grade 1-2 skills and dependency calculation reference.

---

## Grade Distribution Comparison

| Grade | k8_ai_complete | final_enriched | Difference | Canonical Target |
|-------|----------------|----------------|------------|------------------|
| **K** | 61 | 0 | +61 k8_ai | **61** (from k8_ai) |
| **1** | 69 | 133 | +64 final | **202** (merge both) |
| **2** | 91 | 142 | +51 final | **233** (merge both) |
| **3** | 146 | 143 | +3 k8_ai | **146** (favor k8_ai) |
| **4** | 149 | 146 | +3 k8_ai | **149** (favor k8_ai) |
| **5** | 152 | 149 | +3 k8_ai | **152** (favor k8_ai) |
| **6** | 151 | 148 | +3 k8_ai | **151** (favor k8_ai) |
| **7** | 148 | 145 | +3 k8_ai | **148** (favor k8_ai) |
| **8** | 152 | 149 | +3 k8_ai | **152** (favor k8_ai) |
| **Total** | 1,119 | 1,155 | -36 | **1,234** |

**Analysis:**
- K: Only in k8_ai_complete → keep all
- 1-2: More in final_enriched → merge unique skills
- 3-8: Slightly more in k8_ai_complete → likely AI skills (T21-T24)

**Strategy:** Merge approach captures all skills from both files.

---

## CSTA Code Coverage Comparison

### skills_k8_ai_complete.json (240 skills)

**Sample Codes Present:**
```
1A-AP-08, 1A-AP-09, 1A-AP-10, 1A-AP-11, 1A-AP-12, 1A-AP-14,
1A-CS-01, 1A-CS-02, 1A-DA-05, 1A-DA-06, 1A-DA-07,
1A-IC-16, 1A-IC-17, 1A-IC-18, 1A-NI-04,
1B-AP-11, 1B-DA-07, 1B-IC-18
```

**Coverage:** 240/1,119 = **21.4%**

---

### skills_final_enriched.json (2 skills)

**Coverage:** 2/1,155 = **0.2%**

---

### Canonical Target (940+ skills)

**Strategy:**
1. Preserve existing 240 codes from k8_ai_complete
2. Apply mapping rules for remaining ~700 skills
3. Leave ~200 skills for manual review

**Coverage:** 940/1,234 = **76.2%**

---

## AI4K12 Category Coverage

### Current (All Files): 0 skills

No file currently has ai4k12_categories field.

---

### Canonical Target: 166 skills

**Topics with AI4K12 Alignment:**
- T21: AI Media Tools (25 skills) → machine_learning, ethical_ai
- T22: Chatbots (24 skills) → representation_and_reasoning, machine_learning
- T23: Multimodal AI (24 skills) → machine_learning, representation_and_reasoning
- T24: XO & AI Coding (22 skills) → humans_and_ai, ethical_ai
- T35: Impacts (36 skills) → societal_impacts
- T36: Ethics (35 skills) → societal_impacts, ethical_ai

**Total:** 166 skills (~13% of all skills)

---

## Summary Recommendations

### ✅ Use skills_k8_ai_complete.json as Base

**Rationale:**
1. Only source for Kindergarten (irreplaceable)
2. Rich instructional metadata (K-2 especially)
3. Better CSTA coverage
4. AI topic skills included

---

### ✅ Merge Missing Skills from skills_final_enriched.json

**What to Merge:**
- ~115 unique Grade 1-2 skills
- Any unique Grade 3-8 skills not in k8_ai_complete

**How to Merge:**
- Add k8_ai_complete-specific fields with defaults
- Preserve existing final_enriched data where available

---

### ✅ Enrich with Complete Metadata

**Add to ALL skills:**
1. domain_id, domain_name (from domain_mapping.json)
2. topic_name (from domains_topics.yaml)
3. CSTA codes (from mapping rules + cstastandard.md)
4. difficulty_track (from SKILL_TRACK_CATEGORIZATION.json)
5. dependency_count, is_gateway, is_capstone (calculated)

**Add to RELEVANT skills:**
1. ai4k12_categories (T21-T24, T35-T36 only)
2. competition_tags (grades 2-8, relevant topics)

---

## Conclusion

**Clear Winner:** skills_k8_ai_complete.json

**With:** Merge strategy for complete coverage + metadata enrichment

**Result:** 1,234+ fully enriched skills covering K-8 with complete metadata

---

**End of Comparison**
