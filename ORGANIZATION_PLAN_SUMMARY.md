# CreatiCode Project File Organization Plan

## Executive Summary

This document outlines the complete file organization plan for the CreatiCode K-8 Skill Map project. The project currently contains 304 files in the root directory. This plan reorganizes them into a clean, maintainable structure with clear separation of concerns.

## Current State
- **Total Files**: 304 in root directory
- **Problem**: Difficult to navigate; mix of production data, temporary analysis, documentation, and utilities
- **Solution**: Organize into logical directories with clear purposes

## Proposed Structure

```
CreatiCodeSkillMap/
├── skills/                          # Production skill data and schemas
│   ├── README.md                    # Skills directory guide
│   ├── skills_k8_ai_complete_FINAL.json  # MAIN PRODUCTION FILE
│   ├── FOUNDATIONAL_41_SKILLS.json
│   ├── WEEK2_NEW_SKILLS.json
│   ├── CREATIVE_SKILLS_3.json
│   ├── CANONICAL_SKILL_SCHEMA.json
│   ├── k2_skill_format_spec.json
│   ├── domains_topics.yaml
│   └── [22 more skill-related files]
│
├── archive/analysis/                # Temporary analysis & historical files
│   ├── README.md                    # Archive guide
│   ├── WEEK1_*.md                   # Week 1 analysis
│   ├── WEEK2_*.md                   # Week 2 analysis
│   ├── DEPENDENCIES_*.md            # Dependency analyses
│   ├── INTEGRATION_*.md             # Integration reports
│   ├── K2_*.md                      # K-2 specific analyses
│   ├── ACSL_*.md                    # ACSL content analysis
│   ├── AI_*.md                      # AI enhancement analysis
│   └── [166 more temporary files]
│
├── docs/                            # Reference documentation
│   ├── README.md                    # Documentation guide
│   └── (future: curated docs)
│
├── [Core Documentation in Root]
│   ├── README.md                    # Main project readme
│   ├── spec.md                      # Project specification
│   ├── spec_v2_updated.md           # Spec v2
│   ├── QUICK_START_GUIDE.md
│   ├── IMPLEMENTATION_GUIDE.md
│   ├── CSTA_STANDARDS_REFERENCE.md
│   └── [Additional core docs]
│
├── [Utility Scripts in Root]
│   ├── analyze_csta.py
│   ├── create_mapping_rules.py
│   ├── generate_reports.py
│   └── [14 more utility scripts]
│
└── [Topic-based Skill Files in Root]
    ├── skills_T01_everyday_algorithms.md
    ├── skills_T02_representing_tracing.md
    └── [34 more topic skill files]
```

## File Categorization

### Category 1: Skills Data (26 files) → skills/

**Main Production File:**
- `skills_k8_ai_complete_FINAL.json` - Contains 1,150 complete K-8 skills with AI integration

**Supporting Data Files:**
- FOUNDATIONAL_41_SKILLS.json
- WEEK2_NEW_SKILLS.json
- CREATIVE_SKILLS_3.json
- WEEK2_SKILLS_QUICK_REFERENCE.json

**Schema & Format Definitions:**
- CANONICAL_SKILL_SCHEMA.json
- k2_skill_format_spec.json
- k2_activity_templates.json
- k2_autograding_rules.json
- k2_visual_themes.json

**Domain & Topic Files:**
- domains_topics.yaml
- domain_mapping.json

**Statistics & Validation:**
- FINAL_SKILL_MAP_STATISTICS.json
- k8_complete_statistics.json
- enrichment_stats.json
- k8_validation_report.json
- well_designed_examples.json
- foundational_blocks_detailed_analysis.json
- k2_current_analysis.json
- skill_file_analysis.json
- skill_comparison_report.json
- removed_dependencies_report.json

**CSTA Reference Data:**
- csta_standards_extracted.json
- SKILL_CSTA_ASSIGNMENTS.json
- SKILL_TRACK_CATEGORIZATION.json
- k3_transition_validation.json

### Category 2: Temporary Analysis Files (172 files) → archive/analysis/

**WEEK1 Analysis (20 files):**
- WEEK1_CHANGES_REPORT.md
- FOUNDATIONAL_BLOCKS_ANALYSIS.md
- FOUNDATIONAL_SKILLS_WEEK*.md
- And 16 more foundational skills analysis files

**WEEK2 Analysis (13 files):**
- WEEK2_CREATIVITY_ANALYSIS.md
- WEEK2_INTEGRATION_COMPLETE.md
- WEEK2_DEPENDENCY_ANALYSIS.md
- And 10 more Week 2 specific files

**Dependency Analysis (21 files):**
- DEPENDENCIES_T01_T05_REPORT.md
- DEPENDENCIES_T06_T13_REPORT.md
- DEPENDENCIES_T14_T24_REPORT.md
- DEPENDENCIES_T25_T29_REPORT.md
- DEPENDENCIES_T30_T36_REPORT.md
- dependencies_*.json for each topic range
- DEPENDENCY_MAP files
- Cross domain dependencies

**Topic-specific Analysis (30 files):**
- T01_enriched_analysis.md through T09_enriched_analysis.md
- T10-T13_streamlined_analysis.md
- T14-T24_applications_analysis.md
- T25-T29_data_analysis.md
- T30-T36_systems_society_analysis.md

**AI Enhancement & Integration (13 files):**
- AI_ENHANCEMENT_REPORT.md
- AI_INTEGRATION_PLAN.md
- AI_SKILLS_CREATION_REPORT.md
- AI4K12_ANALYSIS_SUMMARY.md
- CURRENT_AI_COVERAGE_ANALYSIS.md
- And 8 more AI-related analysis files

**ACSL Analysis (5 files):**
- ACSL_ANALYSIS_RAW.json
- ACSL_CLEANUP_REPORT.md
- ACSL_CONTENT_EXCLUSION.md
- ACSL_DEPENDENCY_FIXES.json

**K-2 Analysis (8 files):**
- K2_REDESIGN_REPORT.md
- K2_COMPLETE_TOPIC_COVERAGE.md
- K2_REMAINING_SKILLS_REPORT.md
- And 5 more K-2 specific files

**Project Pathways (7 files):**
- CRITICAL_PATHS_T06_T13.md
- CAPSTONE_SKILLS_T14_T24.md
- CREATIVE_PROJECT_PATHWAY.md
- DATA_LITERACY_PATHWAY.md
- RESPONSIBLE_COMPUTING_PATHWAY.md
- TRACK_MIGRATION_PLAN.md
- GATEWAY_AND_CAPSTONE_SKILLS.md

**Integration & Validation (15 files):**
- INTEGRATION_COMPLETE_CHECKLIST.md
- FINAL_INTEGRATION_REPORT.md
- VALIDATION_REPORT_COMPLETE.md
- FINAL_VALIDATION_REPORT.md
- And 11 more integration/validation files

**Project Completion (11 files):**
- FINAL_PROJECT_SUMMARY_AI_COMPLETE.md
- PROJECT_COMPLETE_FINAL_SUMMARY.md
- EXECUTIVE_SUMMARY_FINAL.md
- K8_AI_COMPLETE_SUMMARY.md
- And 7 more summary files

**Data Consolidation & Management (7 files):**
- DATA_CONSOLIDATION_ANALYSIS.md
- METADATA_CONSOLIDATION_PLAN.md
- DATA_AI_BRIDGES.md
- FILE_DEPRECATION_PLAN.md
- FILE_MANIFEST.md
- FILES_GENERATED.txt
- CLEANUP_SUMMARY.md

### Category 3: Core Documentation & Utilities (106 files) → Keep in Root

**Essential Documentation (12 files):**
- README.md
- spec.md
- spec_v2_updated.md
- 00-START-HERE.md
- QUICK_START_GUIDE.md
- QUICK_REFERENCE.md
- IMPLEMENTATION_GUIDE.md
- CSTA_STANDARDS_REFERENCE.md
- creaticode.md
- reviews.md
- INDEX.md
- 00_DATA_CONSOLIDATION_INDEX.md

**Reference Documents (7 files):**
- cstastandard.md
- CRITICAL_PATHWAYS.md
- HOW_TO_USE_DEPENDENCIES.md
- dependency_framework.md
- CSTA_BACKFILL_PLAN.md
- CSTA_BACKFILL_SUMMARY.md
- AI-Priorities-for-All-K-12-Students-Report-from-CSTA-AI4K12.md

**Structural Reference (5 files):**
- domains_topics_overview.md
- topic_grade_matrix.md
- TOPIC_TO_CSTA_MAPPING_RULES.json
- competition_paths.md
- BLOCK_COVERAGE_MATRIX.md

**K-2 Implementation Guides (7 files):**
- K2_FRAMEWORK_SUMMARY.md
- K2_IMPLEMENTATION_EXAMPLES.md
- K2_QUALITY_GUIDELINES.md
- K2_DEPENDENCY_EXAMPLES.md
- K2_DEPENDENCIES_README.md
- SYNTHESIS_SKILLS.md
- subagent_instructions.md

**Python Utility Scripts (29 files):**
- analyze_csta.py
- analyze_dependencies_T01_T05.py
- analyze_differences.py
- analyze_skills.py
- analyze_T06_T13.py
- apply_week1_fixes.py
- assign_csta_codes.py
- compare_skills.py
- create_backfill_plan.py
- create_csta_reference.py
- create_mapping_rules.py
- enrich_dependencies.py
- extract_csta_standards.py
- extract_csta_standards_v2.py
- final_verification.py
- fix_dependencies.py
- fix_issues.py
- generate_all_remaining_topics_k2.py
- generate_k2_skills.py
- generate_remaining_k2_skills.py
- generate_reports.py
- integrate_ai_skills.py
- integrate_all_changes.py
- integrate_k8_skills.py
- investigate_issues.py
- merge_and_validate.py
- validate_only.py
- cleanup_skill_files.sh
- analyze_dependencies_agent.js
- generate_reports.js

**Topic-based Skill Files (36 files):**
- skills_T01_everyday_algorithms.md through skills_T36_ethics_careers.md
(Complete set of topic-based skill definitions)

**Miscellaneous Reference (3 files):**
- skill_dependency_workflow.md
- SKILL_FILE_COMPARISON.md
- analysis_block_coverage.json
- subagent_T06_T13_instructions.md

## How to Use This Plan

### Step 1: Review the Plan
Before executing any file movements:
1. Open and review `FILES_TO_MOVE.txt` - Lists all 26 files going to skills/
2. Open and review `FILES_TO_ARCHIVE.txt` - Lists all 172 analysis files
3. Open and review `FILES_TO_KEEP.txt` - Lists all 106 files staying in root

### Step 2: Create Backups (Recommended)
```bash
# Optional: Create backup before organizing
cp -r . ../CreatiCodeSkillMap_backup
```

### Step 3: Execute Organization Script
```bash
bash organize_files.sh
```

This will:
- Create directories (skills/, archive/analysis/, docs/)
- Move 26 skill files to skills/
- Move 172 temporary analysis files to archive/analysis/
- Create README.md files in each new directory
- Display a summary of changes

### Step 4: Verify Organization
```bash
# Check new structure
ls -la
ls -la skills/
ls -la archive/analysis/

# Verify important files are in correct locations
ls skills/skills_k8_ai_complete_FINAL.json
ls README.md
```

### Step 5: Commit to Git
```bash
git add skills/ archive/
git commit -m "Organize project files: move skills data and analysis files to dedicated directories"
git status
```

## Benefits of This Organization

1. **Clarity**: Clear separation between production data, temporary analysis, and documentation
2. **Maintainability**: Easy to find files and understand their purpose
3. **Navigation**: Reduces root directory clutter from 304 files to ~106 files
4. **Scalability**: Growth of analysis files won't clutter the main directory
5. **Archiving**: Temporary files are grouped and can be easily archived or deleted later
6. **Production**: Skills data is isolated in a single, organized location

## File Location Reference

| Purpose | Location | Count |
|---------|----------|-------|
| Production Skill Data | `skills/` | 26 |
| Schema & Specifications | `skills/` | 5 |
| Domain & Topics | `skills/` | 2 |
| Statistics & Validation | `skills/` | 8 |
| CSTA Reference | `skills/` | 4 |
| Temporary Analysis | `archive/analysis/` | 172 |
| Core Documentation | Root | 19 |
| Reference Docs | Root | 5 |
| Implementation Guides | Root | 7 |
| Utility Scripts | Root | 29 |
| Topic Skill Files | Root | 36 |
| Miscellaneous | Root | 5 |
| **TOTAL** | **Various** | **304** |

## FAQ

**Q: Will this affect the existing Python scripts and their file paths?**
A: Most scripts should continue to work since they look for files in specific locations. However, you may need to update any script imports if they have hardcoded paths. The `skills/` directory contains data files that scripts reference.

**Q: Can I undo this if something goes wrong?**
A: Yes. Each `mv` command in the script includes error handling. If needed, you can manually move files back to the root directory.

**Q: Should I delete the archive/analysis files?**
A: Not immediately. Keep them for at least one development cycle to ensure no important information is lost. After that, they can be archived to a separate backup or deleted.

**Q: What about new files generated during development?**
A: Place new files according to their purpose:
- New skill JSON files → `skills/`
- Analysis/report files → `archive/analysis/`
- Documentation → root or `docs/`
- Utility scripts → root

**Q: Do I need to update Git?**
A: Yes. After running the script, commit the directory changes:
```bash
git add skills/ archive/
git commit -m "Organize files: separate skills, analysis, and docs"
```

## Next Steps

1. Review the three file lists (FILES_TO_MOVE.txt, FILES_TO_ARCHIVE.txt, FILES_TO_KEEP.txt)
2. Ensure you have a backup (if desired)
3. Execute: `bash organize_files.sh`
4. Verify the new structure
5. Commit changes to Git
6. Update any documentation that references file paths
7. Monitor new file generation to follow the new organization

---

**Document Version**: 1.0
**Created**: 2025-11-17
**Status**: Ready for Implementation
