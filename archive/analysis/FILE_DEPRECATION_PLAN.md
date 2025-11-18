# CreatiCode Skill Map: File Deprecation and Management Plan

**Date:** 2025-11-17
**Purpose:** Define which files to keep, archive, or delete after consolidation

---

## Overview

After creating the canonical CANONICAL_SKILLS.json file, this plan specifies how to manage the 48 JSON files currently in the repository to maintain a clean, organized codebase.

---

## File Categories

### Category 1: CANONICAL (Keep - Production)

These files become the single source of truth for the skill map.

| File | Purpose | Status |
|------|---------|--------|
| **CANONICAL_SKILLS.json** | Single source of truth for all K-8 skills | TO BE CREATED |
| **CANONICAL_SKILLS_STATISTICS.json** | Metadata about canonical file | TO BE CREATED |

**Location:** Root directory
**Backup:** Daily automated backups
**Version Control:** Primary branch, protected

---

## Category 2: REFERENCE DATA (Keep - Required)

These files provide essential reference data used to generate and validate canonical skills.

| File | Purpose | Size | Notes |
|------|---------|------|-------|
| domains_topics.yaml | Domain and topic structure (D1-D5, T01-T36) | N/A | Source of truth for taxonomy |
| domain_mapping.json | Topic ID → Domain ID lookup | 2.7K | Generated from domains_topics.yaml |
| competition_paths.md | Competition mapping documentation | N/A | Human-readable reference |
| AI4K12_MAPPING.json | AI4K12 framework alignment | 15K | AI standards reference |
| SKILL_TRACK_CATEGORIZATION.json | Difficulty track assignments | 16K | Standard/enrichment/competition |
| cstastandard.md | CSTA standards documentation | N/A | CSTA reference document |

**Location:** `/reference/` subdirectory (create)
**Backup:** Version controlled
**Updates:** Manual, with documentation

---

## Category 3: VALIDATION & REPORTS (Keep - Quality Assurance)

These files document validation, analysis, and quality metrics.

| File | Purpose | Size | Notes |
|------|---------|------|-------|
| validation_report.json | Skill validation results | 2.4K | Latest validation run |
| k8_validation_report.json | K-8 complete validation | 477 bytes | Post-K-2 integration |
| ai_enhanced_validation_report.json | AI skill validation | 1.5K | AI topics validation |
| enrichment_stats.json | Enrichment process metrics | 2.6K | Metadata enrichment stats |
| k8_complete_statistics.json | K-8 statistics | 6.0K | Coverage analysis |
| ai_enhanced_statistics.json | AI enhancement stats | 1.7K | AI integration metrics |
| age_appropriateness_analysis.json | Developmental review | 90K | Age-appropriateness analysis |
| comprehensive_age_review.json | Full age review | 13K | Detailed age analysis |
| well_designed_examples.json | Best practice examples | 4.4K | Model skills reference |
| k3_transition_validation.json | K-3 transition analysis | 40K | Early grades validation |
| removed_dependencies_report.json | Dependency cleanup log | 3.2K | Dependency refactoring |

**Location:** `/reports/` subdirectory (create)
**Backup:** Version controlled
**Retention:** Indefinite (historical record)

---

## Category 4: DEPENDENCY DATA (Keep - Graph Structure)

These files contain detailed dependency relationships.

| File | Purpose | Size | Notes |
|------|---------|------|-------|
| dependencies_T01_T05.json | D1 domain dependencies | 45K | Algorithms & Design |
| dependencies_T01_T05_summary.json | D1 summary | 449 bytes | Quick reference |
| dependencies_T06_T13.json | D2 core programming dependencies | 74K | Programming fundamentals |
| dependencies_T14_T24.json | D2 applications dependencies | 166K | Programming applications |
| dependencies_T25_T29.json | D3 data dependencies | 54K | Data & Analysis |
| dependencies_T30_T36.json | D4/D5 systems dependencies | 85K | Systems & Society |

**Location:** `/dependencies/` subdirectory (create)
**Backup:** Version controlled
**Purpose:** Detailed dependency analysis per domain/topic cluster
**Note:** Canonical file includes consolidated dependencies; these provide detailed analysis

---

## Category 5: ARCHIVE (Move to /archive/)

These files represent important historical versions but are superseded by CANONICAL_SKILLS.json.

| File | Purpose | Size | Reason for Archive |
|------|---------|------|-------------------|
| skills_k8_ai_complete.json | K-8 with AI integration | 1.1M | **Primary source for canonical merge** |
| skills_final_enriched.json | Grades 1-8 enriched | 864K | **Secondary source for canonical merge** |
| skills_complete_k8.json | Earlier K-8 version | 1.1M | Superseded by k8_ai_complete |
| skills_final.json | Pre-enrichment final | 807K | Superseded by final_enriched |
| skills_with_dependencies.json | With dependencies | 750K | Earlier dependency version |
| skills_enriched.json | Partial enrichment | 666K | Intermediate processing |
| skills.json | Base version | 778K | Early version |

**Location:** `/archive/skill_versions/` subdirectory (create)
**Backup:** Version controlled, compressed
**Retention:** 2 years minimum
**Purpose:** Historical reference, rollback capability

---

## Category 6: DEVELOPMENT ARTIFACTS (Archive or Delete)

### 6a. K-2 Development Iterations (Archive)

These document the K-2 skill design process.

| File | Purpose | Size | Action |
|------|---------|------|--------|
| skills_k2_complete_all.json | Final K-2 compilation | 386K | **Archive** - final K-2 design |
| skills_k2_with_dependencies.json | K-2 with dependencies | 390K | **Archive** - dependency validation |
| k2_skill_format_spec.json | K-2 format specification | 18K | **Keep in /reference/** - design spec |
| k2_activity_templates.json | K-2 activity templates | 29K | **Keep in /reference/** - template library |
| k2_autograding_rules.json | K-2 autograding spec | 25K | **Keep in /reference/** - grading rules |
| k2_visual_themes.json | K-2 visual themes | 25K | **Keep in /reference/** - design system |
| k2_current_analysis.json | K-2 analysis | 27K | **Archive** - process documentation |

**Action:** Move final K-2 compilation to archive; move specs to reference

### 6b. K-2 Intermediate Files (Delete)

| File | Size | Reason for Deletion |
|------|------|-------------------|
| skills_k2_redesigned_partial.json | 53K | Partial/incomplete |
| skills_k2_new_batch.json | 25K | Batch processing artifact |
| skills_k2_redesigned.json | 200K | Intermediate version |
| skills_k2_additional_topics.json | 19K | Partial batch |
| skills_k2_batch_comprehensive.json | 64K | Intermediate batch |
| skills_k2_all_remaining_topics.json | 186K | Superseded by complete_all |

**Action:** DELETE after confirming all K-2 skills in canonical file

---

### 6c. AI Skill Development (Archive)

| File | Purpose | Size | Action |
|------|---------|------|--------|
| ai_skills_new_phase1.json | AI skill generation phase 1 | 32K | **Archive** - AI development history |
| ai_skills_new_phase2.json | AI skill generation phase 2 | 20K | **Archive** - AI development history |

**Action:** Archive in `/archive/ai_development/`

---

### 6d. Topic Extraction Files (Delete)

| File | Size | Reason for Deletion |
|------|------|-------------------|
| extracted_skills_raw.json | 601K | Raw extraction, superseded |
| t01_t05_skills.json | 95K | Subset extracted during development |
| skills_T14_T24_extracted.json | 197K | Topic subset extraction |
| grade_7_8_skills_extracted.json | 256K | Grade subset for analysis |
| grade_7_8_skills_for_analysis.json | 190K | Analysis subset |

**Action:** DELETE - all data incorporated into canonical file

---

### 6e. Partial/Incomplete Files (Delete)

| File | Size | Reason for Deletion |
|------|------|-------------------|
| skills_enriched_partial.json | 15K | Incomplete processing |

**Action:** DELETE - superseded

---

## Directory Structure (Proposed)

```
CreatiCodeSkillMap/
│
├── CANONICAL_SKILLS.json                    # PRODUCTION
├── CANONICAL_SKILLS_STATISTICS.json         # PRODUCTION
│
├── reference/                                # REFERENCE DATA
│   ├── domains_topics.yaml
│   ├── domain_mapping.json
│   ├── competition_paths.md
│   ├── AI4K12_MAPPING.json
│   ├── SKILL_TRACK_CATEGORIZATION.json
│   ├── cstastandard.md
│   ├── k2_skill_format_spec.json           # K-2 design specs
│   ├── k2_activity_templates.json
│   ├── k2_autograding_rules.json
│   └── k2_visual_themes.json
│
├── dependencies/                            # DEPENDENCY GRAPHS
│   ├── dependencies_T01_T05.json
│   ├── dependencies_T01_T05_summary.json
│   ├── dependencies_T06_T13.json
│   ├── dependencies_T14_T24.json
│   ├── dependencies_T25_T29.json
│   └── dependencies_T30_T36.json
│
├── reports/                                 # VALIDATION & QA
│   ├── validation_report.json
│   ├── k8_validation_report.json
│   ├── ai_enhanced_validation_report.json
│   ├── enrichment_stats.json
│   ├── k8_complete_statistics.json
│   ├── ai_enhanced_statistics.json
│   ├── age_appropriateness_analysis.json
│   ├── comprehensive_age_review.json
│   ├── well_designed_examples.json
│   ├── k3_transition_validation.json
│   └── removed_dependencies_report.json
│
├── archive/                                 # HISTORICAL VERSIONS
│   ├── skill_versions/                     # Major skill file versions
│   │   ├── skills_k8_ai_complete.json      # Source for canonical
│   │   ├── skills_final_enriched.json      # Source for canonical
│   │   ├── skills_complete_k8.json
│   │   ├── skills_final.json
│   │   ├── skills_with_dependencies.json
│   │   ├── skills_enriched.json
│   │   └── skills.json
│   │
│   ├── k2_development/                     # K-2 design process
│   │   ├── skills_k2_complete_all.json
│   │   ├── skills_k2_with_dependencies.json
│   │   └── k2_current_analysis.json
│   │
│   └── ai_development/                     # AI skill generation
│       ├── ai_skills_new_phase1.json
│       └── ai_skills_new_phase2.json
│
└── docs/                                    # DOCUMENTATION
    ├── DATA_CONSOLIDATION_ANALYSIS.md
    ├── CANONICAL_SKILL_SCHEMA.json
    ├── METADATA_CONSOLIDATION_PLAN.md
    ├── FILE_DEPRECATION_PLAN.md            # This file
    ├── spec.md
    ├── creaticode.md
    ├── domains_topics_overview.md
    ├── topic_grade_matrix.md
    ├── skill_dependency_workflow.md
    └── [all other .md documentation files]
```

---

## Migration Script

### Step 1: Create Directories

```bash
#!/bin/bash

# Create new directory structure
mkdir -p reference
mkdir -p dependencies
mkdir -p reports
mkdir -p archive/skill_versions
mkdir -p archive/k2_development
mkdir -p archive/ai_development
mkdir -p docs
```

---

### Step 2: Move Reference Files

```bash
# Move reference data
mv domains_topics.yaml reference/
mv domain_mapping.json reference/
mv competition_paths.md reference/
mv AI4K12_MAPPING.json reference/
mv SKILL_TRACK_CATEGORIZATION.json reference/
mv cstastandard.md reference/

# Move K-2 specs to reference
mv k2_skill_format_spec.json reference/
mv k2_activity_templates.json reference/
mv k2_autograding_rules.json reference/
mv k2_visual_themes.json reference/
```

---

### Step 3: Move Dependency Files

```bash
# Move dependency data
mv dependencies_T01_T05.json dependencies/
mv dependencies_T01_T05_summary.json dependencies/
mv dependencies_T06_T13.json dependencies/
mv dependencies_T14_T24.json dependencies/
mv dependencies_T25_T29.json dependencies/
mv dependencies_T30_T36.json dependencies/
```

---

### Step 4: Move Reports

```bash
# Move validation and reports
mv validation_report.json reports/
mv k8_validation_report.json reports/
mv ai_enhanced_validation_report.json reports/
mv enrichment_stats.json reports/
mv k8_complete_statistics.json reports/
mv ai_enhanced_statistics.json reports/
mv age_appropriateness_analysis.json reports/
mv comprehensive_age_review.json reports/
mv well_designed_examples.json reports/
mv k3_transition_validation.json reports/
mv removed_dependencies_report.json reports/
```

---

### Step 5: Archive Skill Versions

```bash
# Archive major skill file versions
mv skills_k8_ai_complete.json archive/skill_versions/
mv skills_final_enriched.json archive/skill_versions/
mv skills_complete_k8.json archive/skill_versions/
mv skills_final.json archive/skill_versions/
mv skills_with_dependencies.json archive/skill_versions/
mv skills_enriched.json archive/skill_versions/
mv skills.json archive/skill_versions/
```

---

### Step 6: Archive Development Files

```bash
# Archive K-2 development
mv skills_k2_complete_all.json archive/k2_development/
mv skills_k2_with_dependencies.json archive/k2_development/
mv k2_current_analysis.json archive/k2_development/

# Archive AI development
mv ai_skills_new_phase1.json archive/ai_development/
mv ai_skills_new_phase2.json archive/ai_development/
```

---

### Step 7: Delete Temporary Files

```bash
# Delete K-2 intermediate files
rm skills_k2_redesigned_partial.json
rm skills_k2_new_batch.json
rm skills_k2_redesigned.json
rm skills_k2_additional_topics.json
rm skills_k2_batch_comprehensive.json
rm skills_k2_all_remaining_topics.json

# Delete extraction/subset files
rm extracted_skills_raw.json
rm t01_t05_skills.json
rm skills_T14_T24_extracted.json
rm grade_7_8_skills_extracted.json
rm grade_7_8_skills_for_analysis.json

# Delete partial files
rm skills_enriched_partial.json
```

---

### Step 8: Move Documentation

```bash
# Move markdown documentation to docs/
mv *.md docs/
mv DATA_CONSOLIDATION_ANALYSIS.md docs/
mv CANONICAL_SKILL_SCHEMA.json docs/
mv METADATA_CONSOLIDATION_PLAN.md docs/
mv FILE_DEPRECATION_PLAN.md docs/
```

---

## Rollback Plan

In case issues are discovered with CANONICAL_SKILLS.json:

### Immediate Rollback (Within 7 Days)

1. Files are in `/archive/skill_versions/` - not deleted
2. Restore either:
   - `skills_k8_ai_complete.json` (has K, has AI)
   - `skills_final_enriched.json` (more 1-2 skills)
3. Revert documentation references
4. Debug canonical generation process

### Long-term Rollback (After 7 Days)

1. Use git history to restore state
2. Archived files remain available
3. Regenerate canonical file from sources

---

## Backup Strategy

### Git Version Control
- All files tracked in git
- Protected main branch
- Tag releases: `v1.0-canonical`, `v1.1-canonical`, etc.

### External Backups
- Daily: `CANONICAL_SKILLS.json`
- Weekly: Full repository backup
- Monthly: Archive snapshot

### Backup Locations
- Primary: GitHub repository
- Secondary: Cloud storage (Google Drive/Dropbox)
- Tertiary: Local backup drive

---

## Access Control

### Production Files (CANONICAL_SKILLS.json)
- **Read:** All team members
- **Write:** Build scripts only (automated)
- **Manual Edit:** Requires approval + PR review

### Reference Files
- **Read:** All team members
- **Write:** Data team + documentation team
- **Changes:** Documented in changelog

### Archive Files
- **Read:** All team members
- **Write:** None (read-only)
- **Deletion:** Project lead approval only

---

## Update Procedures

### When CANONICAL_SKILLS.json Changes

1. Generate from source data (never edit directly)
2. Run validation suite
3. Generate new statistics report
4. Update documentation if schema changes
5. Tag new version in git
6. Archive previous version with timestamp

### When Reference Data Changes

1. Update source file (e.g., domains_topics.yaml)
2. Document change in CHANGELOG.md
3. Regenerate CANONICAL_SKILLS.json
4. Validate all dependencies still resolve
5. Update affected reports

---

## File Retention Policy

| Category | Retention Period | Storage Location |
|----------|------------------|------------------|
| Canonical (current) | Indefinite | Root + backups |
| Reference data | Indefinite | /reference/ |
| Reports (current year) | Indefinite | /reports/ |
| Archive (skill versions) | 2 years | /archive/ |
| Development artifacts | 1 year | /archive/ |
| Deleted files (git history) | Git retention policy | Git only |

---

## Checklist for Deprecation

Before executing deprecation plan:

- [ ] CANONICAL_SKILLS.json successfully generated
- [ ] All 1,234+ skills present in canonical file
- [ ] Validation suite passes (100% required fields)
- [ ] Dependency validation passes (no broken references)
- [ ] Statistics report generated
- [ ] Spot-check random skills for data quality
- [ ] Backup current state to external storage
- [ ] Git tag current state as `pre-deprecation`
- [ ] Create new directories (reference/, dependencies/, reports/, archive/)
- [ ] Execute migration script
- [ ] Verify all moved files accessible in new locations
- [ ] Update all documentation references to new paths
- [ ] Update build scripts to use CANONICAL_SKILLS.json
- [ ] Test build process with new file structure
- [ ] Confirm git tracks all new file locations
- [ ] Create git tag `post-deprecation`
- [ ] Update README.md with new file structure
- [ ] Notify team of file structure changes

---

## Contact for Questions

- **File structure questions:** Project lead
- **Data questions:** Data team
- **Archive access:** Repository admin
- **Backup restore:** DevOps team

---

**End of Deprecation Plan**
