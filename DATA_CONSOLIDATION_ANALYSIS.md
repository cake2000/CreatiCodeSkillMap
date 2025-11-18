# CreatiCode Skill Map: Data Consolidation Analysis

**Date:** 2025-11-17
**Analysis Focus:** Identify canonical skill data source and consolidation requirements

---

## Executive Summary

Multiple "final" skill files exist with inconsistent data coverage and metadata completeness. This analysis identifies **skills_k8_ai_complete.json** as the recommended canonical source and outlines the consolidation plan.

### Critical Findings

1. **Three competing "complete" files** with different skill counts and metadata
2. **Missing Kindergarten coverage** in most recent files
3. **Inconsistent CSTA code coverage** (21% vs 0.2% populated)
4. **No competition tags** in any file
5. **No difficulty tracks** integrated
6. **Incomplete domain metadata** in most files

---

## File Inventory and Comparison

### Primary Skill Files (Potential Canonical Sources)

| File | Skills | K | 1 | 2 | 3-8 | Has AI4K12 | CSTA Codes | Domain IDs | Size |
|------|--------|---|---|---|-----|------------|------------|------------|------|
| **skills_k8_ai_complete.json** | 1,119 | 61 | 69 | 91 | 898 | Partial | 240 (21%) | Missing | 1.1M |
| **skills_final_enriched.json** | 1,155 | 0 | 133 | 142 | 880 | No | 2 (0.2%) | "Unknown" | 864K |
| **skills_complete_k8.json** | 1,086 | Unknown | - | - | - | Unknown | Unknown | Unknown | 1.1M |
| **skills_final.json** | 1,155 | 0 | 133 | 142 | 880 | No | 0? | No | 807K |

### Field Comparison by File

#### skills_k8_ai_complete.json Fields:
```
accessibility, activity_type, auto_grade_rules, csta_code, dependencies,
description_teacher, grade, id, interaction_details, notes_redesign,
short_name, skill_type, student_prompt, student_prompt_audio, title, topic_id
```

**Strengths:**
- Has Kindergarten skills (61 skills)
- Rich activity design metadata (activity_type, interaction_details, auto_grade_rules)
- Accessibility specifications
- Student-facing content (student_prompt, audio)
- Some CSTA codes (240 populated)

**Weaknesses:**
- Missing domain_id, domain_name
- Missing topic_name
- No AI4K12 category field
- No competition tags
- No difficulty track
- No is_gateway, is_capstone flags
- Inconsistent grade format (K vs "K", 1 vs "1")

#### skills_final_enriched.json Fields:
```
csta_code, dependencies, dependency_count, description, domain, domain_id,
domain_name, grade, id, is_capstone, is_gateway, short_name, title,
topic_id, topic_name
```

**Strengths:**
- Has topic_name
- Has domain_id, domain_name (though marked "Unknown")
- Has is_gateway, is_capstone flags
- Has dependency_count
- Consistent grade format (integers)

**Weaknesses:**
- Missing Kindergarten (0 skills)
- Almost no CSTA codes (2 total)
- Missing all K-2 content design metadata
- No AI4K12 categories
- No competition tags
- No difficulty track

---

## Skill Count Analysis

### By Grade Distribution

**skills_k8_ai_complete.json:**
- K: 61 (5.5%)
- 1: 69 (6.2%)
- 2: 91 (8.1%)
- 3: 146 (13.0%)
- 4: 149 (13.3%)
- 5: 152 (13.6%)
- 6: 151 (13.5%)
- 7: 148 (13.2%)
- 8: 152 (13.6%)
- **Total: 1,119**

**skills_final_enriched.json:**
- K: 0 (0%)
- 1: 133 (11.5%)
- 2: 142 (12.3%)
- 3: 143 (12.4%)
- 4: 146 (12.6%)
- 5: 149 (12.9%)
- 6: 148 (12.8%)
- 7: 145 (12.6%)
- 8: 149 (12.9%)
- **Total: 1,155**

### Discrepancy Analysis

**Missing from skills_k8_ai_complete.json:**
- 36 fewer skills overall (1,119 vs 1,155)
- 0 Kindergarten in final_enriched
- Grade 1-2: 64 fewer vs 133, 91 vs 142
- Grades 3-8: Roughly equal distribution

**Hypothesis:** skills_final_enriched includes more Grade 1-2 coding skills but lacks the special Kindergarten picture-based activities that exist only in skills_k8_ai_complete.json.

---

## Missing Metadata Analysis

### 1. CSTA Standards Codes

**Current Coverage:**
- skills_k8_ai_complete.json: 240/1,119 = 21.4% populated
- skills_final_enriched.json: 2/1,155 = 0.2% populated

**Available CSTA codes in k8_ai_complete:**
```
1A-AP-08, 1A-AP-09, 1A-AP-10, 1A-AP-11, 1A-AP-12, 1A-AP-14,
1A-CS-01, 1A-CS-02, 1A-DA-05, 1A-DA-06, 1A-DA-07,
1A-IC-16, 1A-IC-17, 1A-IC-18, 1A-NI-04,
1B-AP-11, 1B-DA-07, 1B-IC-18
```

**Gap:** 879 skills in k8_ai_complete have empty CSTA codes.

**Source for CSTA mapping:** cstastandard.md contains CSTA 2.0 Draft standards documentation.

**Action Required:**
1. Parse CSTA standards from cstastandard.md
2. Create topic-to-CSTA mapping rules
3. Apply CSTA codes to all 1,119 skills
4. Validate against existing 240 codes

---

### 2. Domain IDs and Names

**Current Coverage:**
- skills_k8_ai_complete.json: Missing both domain_id and domain_name fields
- skills_final_enriched.json: Has fields but set to "Unknown" for all skills

**Available Source:** domains_topics.yaml

**Mapping Structure:**
```yaml
domains:
  - id: D1
    name: Algorithms and Design
  - id: D2
    name: Programming
  - id: D3
    name: Data and Analysis
  - id: D4
    name: Systems and Security
  - id: D5
    name: Computing and Society

topics:
  - id: T01
    domain_id: D1
    domain_name: Algorithms and Design
  - id: T06
    domain_id: D2
    domain_name: Programming
  [...]
```

**Action Required:**
1. Load domain_mapping.json (already contains topic_id → domain_id mapping)
2. Join skills by topic_id to add domain_id and domain_name

---

### 3. AI4K12 Categories

**Current Coverage:**
- No skill file has ai4k12_category field
- AI4K12_MAPPING.json contains gap analysis and topic-level mappings

**Available Data in AI4K12_MAPPING.json:**
```json
"T21_ai_media": {
  "ai4k12_categories": [
    "3_machine_learning (data, building_and_using_ai_models)",
    "4_ethical_ai (ethical_design_criteria, ethical_evaluation)",
    "1_humans_and_ai (nature_of_humans_and_ai, choice_to_use_ai)"
  ]
}
```

**Topics with AI4K12 relevance:**
- T21: AI Media Tools & Creative Assets
- T22: AI Chatbots & Information Apps
- T23: AI Voice, Vision & Gesture Interfaces
- T24: XO & AI-Supported Coding Practices
- T35: Impacts of Computing, Games & AI (societal impacts)
- T36: Ethics, Careers (ethical evaluation)

**Action Required:**
1. Parse topic-level AI4K12 categories from AI4K12_MAPPING.json
2. Apply to all skills in T21-T24, T35-T36 topics
3. Add ai4k12_category field (array of strings)

---

### 4. Competition Tags

**Current Coverage:**
- No file has competition tags

**Available Source:** competition_paths.md

**Competition Types Identified:**
1. ACSL (Elementary Grades 3-5, Junior Grades 6-8)
2. Scratch Olympiad (Elementary 2-5, Junior 4-6)
3. NOC (Chinese, Elementary 3-5, Junior 6-8)
4. Lanqiao Scratch (Junior 4-6, Senior 6-8)
5. Games for Change (Grades 4+)
6. Congressional App Challenge (Grades 6-8)
7. ICode Global Hackathon (Grades 5-8)
8. Codeavour (Grades 3-8, tiered)

**Mapping Strategy:**
- Topic + Grade → Competition tags
- Example: T01.G3.01 → ["ACSL Elementary", "NOC Elementary"]

**Action Required:**
1. Parse competition_paths.md
2. Create topic-grade-competition mapping table
3. Add competition_tags field (array of strings)

---

### 5. Difficulty Tracks

**Current Coverage:**
- No file has difficulty track field

**Available Source:** SKILL_TRACK_CATEGORIZATION.json

**Track Types:**
- **standard**: Core skills all students should master
- **enrichment**: Advanced but age-appropriate stretch goals
- **competition**: Skills targeting competitive programming or requiring AP-level knowledge

**Categorized Skills (Grades 7-8 only):**
```json
"competition_track": [
  "T10.G8.02", // Sorting algorithms
  "T01.G8.02", // Recursion (enrichment)
  "T02.G7.03", // Algorithm complexity
  "T02.G8.04"  // Probabilistic algorithms
]

"too_advanced_for_standard": [
  "T27.G8.02", // Causal relationships
  "T35.G7.01", // Systemic impacts
  "T35.G8.02"  // Policy analysis
]
```

**Default Assumptions:**
- K-6: All "standard" unless explicitly marked
- 7-8: Use SKILL_TRACK_CATEGORIZATION.json assignments

**Action Required:**
1. Load categorizations from SKILL_TRACK_CATEGORIZATION.json
2. Add difficulty_track field (string: "standard" | "enrichment" | "competition")
3. Apply to Grade 7-8 skills first
4. Default all K-6 to "standard"

---

### 6. Other Missing Fields

**From skills_final_enriched.json (missing in k8_ai_complete):**
- topic_name
- dependency_count
- is_gateway
- is_capstone

**From skills_k8_ai_complete.json (missing in final_enriched):**
- activity_type
- skill_type
- interaction_details
- auto_grade_rules
- accessibility
- student_prompt
- student_prompt_audio
- description_teacher (vs generic "description")

---

## Recommended Canonical Source

### Winner: **skills_k8_ai_complete.json**

**Rationale:**

1. **Has Kindergarten skills (61 skills)** - Critical coverage missing in all other files
2. **Rich instructional design metadata** - Activity types, interaction details, autograding rules, accessibility
3. **Student-facing content** - Prompts and audio for actual implementation
4. **Better CSTA coverage** - 21% vs 0.2%
5. **AI topic skills included** - 110 skills in T21-T24

**Trade-offs:**
- 36 fewer total skills (1,119 vs 1,155)
- Missing some Grade 1-2 skills present in final_enriched
- Lacks domain_id/domain_name fields (easy to add)
- Lacks is_gateway/is_capstone flags (can derive from dependencies)

**Decision:** Use skills_k8_ai_complete.json as the base and merge missing skills from skills_final_enriched.json.

---

## Data Sources for Metadata Enrichment

| Metadata Field | Source File | Mapping Strategy |
|----------------|-------------|------------------|
| domain_id, domain_name | domain_mapping.json | Join by topic_id |
| topic_name | domains_topics.yaml | Join by topic_id |
| CSTA codes | cstastandard.md + existing codes | Parse standards, map by topic/grade, validate |
| AI4K12 categories | AI4K12_MAPPING.json | Apply to T21-T24, T35-T36 by topic_id |
| competition_tags | competition_paths.md | Parse and map by topic_id + grade |
| difficulty_track | SKILL_TRACK_CATEGORIZATION.json | Apply to G7-G8, default K-6 to "standard" |
| is_gateway | Calculate from dependencies | Skills with dependency_count >= 5 in same topic |
| is_capstone | Calculate from dependencies | Skills depended on by >= 5 other skills |
| dependency_count | Calculate from dependencies array | length of dependencies array |

---

## Skill Discrepancy Resolution Plan

### Gap Analysis

1. **Kindergarten Gap (61 skills):**
   - Present ONLY in skills_k8_ai_complete.json
   - **Action:** Keep all K skills from k8_ai_complete

2. **Grade 1-2 Gap:**
   - k8_ai_complete: 69 + 91 = 160 skills
   - final_enriched: 133 + 142 = 275 skills
   - **Delta:** 115 more skills in final_enriched
   - **Action:** Merge missing Grade 1-2 skills from final_enriched into k8_ai_complete

3. **Grades 3-8 Gap:**
   - k8_ai_complete: 898 skills
   - final_enriched: 880 skills
   - **Delta:** 18 more skills in k8_ai_complete
   - **Action:** Investigate which 18 are unique to k8_ai_complete (likely AI skills)

### Merge Strategy

**Phase 1:** Identify unique skills
```python
k8_ai_ids = set([skill['id'] for skill in k8_ai_complete])
final_enriched_ids = set([skill['id'] for skill in final_enriched])

only_in_k8_ai = k8_ai_ids - final_enriched_ids  # Expected: ~61 K skills + AI skills
only_in_final = final_enriched_ids - k8_ai_ids  # Expected: ~115 G1-2 skills
```

**Phase 2:** Merge unique skills from final_enriched into k8_ai_complete
- Add skills from only_in_final to canonical file
- Preserve all k8_ai_complete fields for existing skills
- For merged skills, add k8_ai_complete-specific fields with defaults

**Expected Final Count:** 1,119 + 115 = **~1,234 skills** (accounting for overlap)

---

## File Deprecation Recommendations

### Files to KEEP

| File | Purpose | Status |
|------|---------|--------|
| **CANONICAL_SKILLS.json** (new) | Single source of truth | TO BE CREATED |
| domains_topics.yaml | Domain/topic structure | Reference |
| domain_mapping.json | Topic-to-domain lookup | Reference |
| competition_paths.md | Competition mappings | Reference |
| AI4K12_MAPPING.json | AI standards alignment | Reference |
| SKILL_TRACK_CATEGORIZATION.json | Difficulty tracks | Reference |
| cstastandard.md | CSTA standards reference | Reference |

### Files to ARCHIVE (for historical reference)

| File | Reason |
|------|--------|
| skills_k8_ai_complete.json | Source for canonical merge |
| skills_final_enriched.json | Source for canonical merge |
| skills_complete_k8.json | Earlier version |
| skills_final.json | Earlier version |
| skills_with_dependencies.json | Earlier version |
| skills_enriched.json | Earlier version |
| skills.json | Earlier version |

### Files to DELETE (intermediate/temporary)

| File | Reason |
|------|--------|
| extracted_skills_raw.json | Raw extraction, superseded |
| skills_enriched_partial.json | Partial processing |
| t01_t05_skills.json | Subset of data |
| skills_T14_T24_extracted.json | Subset of data |
| skills_k2_*.json | All K2 development iterations |
| ai_skills_new_phase1.json | Intermediate AI skill generation |
| ai_skills_new_phase2.json | Intermediate AI skill generation |
| grade_7_8_skills_extracted.json | Subset for analysis |
| grade_7_8_skills_for_analysis.json | Subset for analysis |

### Files to KEEP (reports/validation)

| File | Purpose |
|------|---------|
| validation_report.json | Quality assurance |
| enrichment_stats.json | Process metrics |
| k8_complete_statistics.json | Coverage metrics |
| ai_enhanced_validation_report.json | AI skill validation |
| age_appropriateness_analysis.json | Developmental validation |
| comprehensive_age_review.json | Developmental validation |
| well_designed_examples.json | Best practice reference |

---

## Next Steps

1. **Create DATA_CONSOLIDATION_PLAN.md** - Step-by-step merge procedure
2. **Create CANONICAL_SKILL_SCHEMA.json** - Complete field reference
3. **Create METADATA_CONSOLIDATION_PLAN.md** - Enrichment procedures
4. **Create FILE_DEPRECATION_PLAN.md** - File management strategy
5. **Execute consolidation script** - Generate CANONICAL_SKILLS.json

---

## Success Criteria

A successful consolidation will produce:

1. **Single canonical file** with 1,234+ skills (K-8 complete coverage)
2. **100% metadata coverage** for core fields:
   - domain_id, domain_name (1,234/1,234)
   - topic_id, topic_name (1,234/1,234)
   - difficulty_track (1,234/1,234)
   - CSTA codes (goal: 80%+ meaningful coverage)
   - competition_tags (relevant skills only)
   - AI4K12 categories (T21-T24, T35-T36 only)
3. **Consistent data types** across all skills
4. **Valid dependencies** (no broken skill ID references)
5. **Validated gateway/capstone flags** based on dependency analysis

---

**End of Analysis**
