# Skill Files Cleanup Plan

**Project:** CreatiCode K-8 Skill Map
**Date:** 2025-11-17

## Overview

This plan will reduce 36 skill-related JSON files to 8 essential files, removing 28 redundant/intermediate files and saving ~4.36 MB of disk space.

---

## KEEP IN ROOT DIRECTORY (8 files - 1.26 MB)

### Production File (1 file)
✅ **skills_k8_ai_complete_FINAL.json** (1.15 MB)
   - The canonical, production-ready file
   - 1,150 skills across all 36 topics (T01-T36)
   - Most recent (2025-11-17 19:48)

### Reference/Subset Files (4 files)
✅ **FOUNDATIONAL_41_SKILLS.json** (0.04 MB)
   - Core foundational skills reference
   - Used for testing and documentation

✅ **WEEK2_NEW_SKILLS.json** (0.03 MB)
   - Documents the 20 skills added in Week 2
   - Important for changelog/version tracking

✅ **CREATIVE_SKILLS_3.json** (0.02 MB)
   - Creative skills subset
   - Reference for specific skill type

✅ **WEEK2_SKILLS_QUICK_REFERENCE.json** (0.00 MB)
   - Quick reference guide for Week 2 additions

### Schema/Documentation Files (3 files)
✅ **CANONICAL_SKILL_SCHEMA.json** (0.02 MB)
   - Defines the skill data structure
   - Essential documentation

✅ **k2_skill_format_spec.json** (0.02 MB)
   - K-2 specific format specification
   - Important for understanding K-2 design decisions

✅ **FINAL_SKILL_MAP_STATISTICS.json** (0.00 MB)
   - Statistical summary of final skill map
   - Key metrics and validation

---

## ARCHIVE (Move to archive/ directory - 3 files - 2.88 MB)

Create an `archive/` subdirectory for historical reference:

📦 **skills_final.json** (0.79 MB)
   - Pre-AI redesign version (Version 1)
   - Contains 126 skills that were redesigned
   - Keep one copy for historical comparison

📦 **skills_k8_ai_complete_WEEK2.json** (1.12 MB)
   - Week 2 snapshot (before final 10 skills added)
   - Useful for understanding Week 2 development

📦 **skills_k8_ai_complete.BACKUP.json** (1.09 MB)
   - Explicit backup before final changes
   - Insurance against accidental data loss

**Rationale:** These files provide version history and rollback capability without cluttering the main directory.

---

## DELETE (Remove completely - 25 files - 4.36 MB)

### Group 1: Pre-AI Redesign Duplicates (5 files)
🗑️ skills.json (0.76 MB) - Duplicate of skills_final.json
🗑️ skills_enriched.json (0.65 MB) - Duplicate of skills_final.json
🗑️ skills_final_enriched.json (0.84 MB) - Duplicate of skills_final.json
🗑️ extracted_skills_raw.json (0.59 MB) - Duplicate of skills_final.json
🗑️ skills_with_dependencies.json (0.73 MB) - Old format, superseded

**Rationale:** These are all duplicates or minor variations of skills_final.json (which we're archiving). No unique content.

### Group 2: Intermediate Development Files (2 files)
🗑️ skills_k8_ai_complete.json (1.09 MB) - Superseded by FINAL
🗑️ skills_k8_ai_complete_REVISED.json (1.09 MB) - Superseded by WEEK2 and FINAL
🗑️ skills_complete_k8.json (1.04 MB) - Incomplete version
🗑️ skills_enriched_partial.json (0.01 MB) - Partial test file

**Rationale:** These are intermediate checkpoints. We're keeping BACKUP and WEEK2 for history; don't need 4 versions.

### Group 3: K-2 Working Files (10 files)
🗑️ skills_k2_complete_all.json (0.38 MB)
🗑️ skills_k2_with_dependencies.json (0.38 MB)
🗑️ skills_k2_redesigned.json (0.20 MB)
🗑️ skills_k2_all_remaining_topics.json (0.18 MB)
🗑️ skills_k2_batch_comprehensive.json (0.06 MB)
🗑️ skills_k2_redesigned_partial.json (0.05 MB)
🗑️ skills_k2_additional_topics.json (0.02 MB)
🗑️ skills_k2_new_batch.json (0.02 MB)

**Rationale:** These are working files from the K-2 redesign process. All content merged into FINAL. No unique content remains.

### Group 4: Temporary Extractions (3 files)
🗑️ skills_T14_T24_extracted.json (0.19 MB) - Temporary extraction
🗑️ grade_7_8_skills_for_analysis.json (0.19 MB) - Analysis working file
🗑️ grade_7_8_skills_extracted.json (0.25 MB) - Malformed/empty
🗑️ t01_t05_skills.json (0.09 MB) - Temporary extraction

**Rationale:** These were created for specific analysis tasks. Content is in canonical file. Can be regenerated if needed.

---

## Verification Before Deletion

Before executing the cleanup, verify:

### ✅ Checklist
1. [ ] Confirmed skills_k8_ai_complete_FINAL.json has 1,150 skills
2. [ ] Confirmed FINAL file has all 36 topics (T01-T36)
3. [ ] Verified no unique skill IDs in files marked for deletion
4. [ ] Created archive/ directory
5. [ ] Backed up entire project (git commit or external backup)

### Unique Content Check
Based on comparison analysis:
- ✅ All skills in BACKUP, REVISED, and .json versions are subsets of FINAL
- ✅ Pre-AI files (skills.json, etc.) contain 126 OLD skills that were intentionally redesigned
- ✅ No unique content will be lost by deleting the listed files

---

## Impact Summary

### Before Cleanup
- 36 skill-related JSON files
- ~8.5 MB total
- Confusing file organization
- Unclear which file is canonical

### After Cleanup
- 8 skill-related JSON files in root
- 3 archived files in archive/
- ~4.26 MB total
- Clear file organization
- Obvious canonical file

### Benefits
- **51% disk space reduction** (4.36 MB saved)
- **Clear file purpose** - every file has a documented reason to exist
- **Easier maintenance** - fewer files to manage
- **Preserved history** - key versions archived
- **Better onboarding** - new developers can quickly identify the production file

---

## Execution Plan

The cleanup will be performed by the `cleanup_skill_files.sh` script with these steps:

1. Create `archive/` directory
2. Move 3 files to archive
3. Delete 25 redundant files
4. Generate `FILE_ORGANIZATION.md` documenting final structure
5. Display summary of actions taken

---

## Rollback Plan

If cleanup needs to be reversed:

1. Files are in git history (commit before cleanup)
2. Archive files can be restored from `archive/`
3. Script creates `cleanup_log.txt` with all actions for manual reversal

---

## Questions & Answers

**Q: What about skills_T01.json through skills_T36.json?**
**A:** These files do not exist. The canonical file contains all topics in one file.

**Q: Is it safe to delete the pre-AI files (skills.json, skills_enriched.json)?**
**A:** Yes. We're archiving `skills_final.json` which contains the same content. The 126 "unique" skills in these files were intentionally redesigned, not lost.

**Q: What if we need to regenerate extractions like skills_T14_T24_extracted.json?**
**A:** They can be easily recreated from the canonical file using a simple jq or Python filter.

**Q: Why keep WEEK2_NEW_SKILLS.json if it's in the canonical file?**
**A:** It serves as documentation of what was added in Week 2, making changelog generation and version tracking easier.

---

## Approval Required

Before executing `cleanup_skill_files.sh`, please confirm:

- [ ] I have reviewed the cleanup plan
- [ ] I understand which files will be deleted
- [ ] I have verified no unique content will be lost
- [ ] I have committed current state to git or created external backup
- [ ] I approve the cleanup execution

**Once approved, run:** `bash cleanup_skill_files.sh`
