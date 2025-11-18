# CreatiCode Skill Files Organization

**Last Updated:** 2025-11-17
**Status:** Production Ready

## File Structure

```
CreatiCodeSkillMap/
├── skills_k8_ai_complete_FINAL.json          [PRODUCTION - 1,150 skills]
├── FOUNDATIONAL_41_SKILLS.json               [Reference subset]
├── WEEK2_NEW_SKILLS.json                     [Reference subset]
├── CREATIVE_SKILLS_3.json                    [Reference subset]
├── WEEK2_SKILLS_QUICK_REFERENCE.json         [Quick reference]
├── CANONICAL_SKILL_SCHEMA.json               [Schema documentation]
├── k2_skill_format_spec.json                 [K-2 format spec]
├── FINAL_SKILL_MAP_STATISTICS.json           [Statistics]
└── archive/
    ├── skills_final.json                     [Pre-AI redesign version]
    ├── skills_k8_ai_complete_WEEK2.json      [Week 2 snapshot]
    └── skills_k8_ai_complete.BACKUP.json     [Backup version]
```

---

## Production File

### skills_k8_ai_complete_FINAL.json
- **Purpose:** The canonical, production-ready skill map
- **Content:** 1,150 skills across 36 topics (T01-T36) for grades K-8
- **Last Updated:** 2025-11-17 19:48
- **Size:** 1.15 MB
- **Use For:**
  - Production deployment
  - Generating skill reports
  - Creating topic extractions
  - All skill queries and analysis

**Topic Coverage:**
- T01 (Getting Started): 36 skills
- T02 (Intro Sprite): 47 skills
- T03 (Pixel Editor): 35 skills
- T04 (Programming): 39 skills
- ... (through T36)

---

## Reference Subsets

### FOUNDATIONAL_41_SKILLS.json
- **Purpose:** Core foundational skills across all topics
- **Content:** 41 carefully selected skills that form the foundation
- **Use For:** Testing, sample data, teaching core concepts

### WEEK2_NEW_SKILLS.json
- **Purpose:** Skills added during Week 2 development
- **Content:** 20 new skills
- **Use For:** Changelog generation, understanding recent additions

### CREATIVE_SKILLS_3.json
- **Purpose:** Creative-focused skills
- **Content:** 3 skills emphasizing creative expression
- **Use For:** Creative track curriculum planning

### WEEK2_SKILLS_QUICK_REFERENCE.json
- **Purpose:** Quick reference guide for Week 2 additions
- **Content:** Summary of 20 Week 2 skills
- **Use For:** Quick lookup, documentation

---

## Schema & Documentation

### CANONICAL_SKILL_SCHEMA.json
- **Purpose:** Defines the skill data structure
- **Content:** Field definitions, validation rules, examples
- **Use For:** Understanding skill format, validation, new skill creation

### k2_skill_format_spec.json
- **Purpose:** K-2 specific format specification
- **Content:** Age-appropriate formatting rules for K-2 skills
- **Use For:** Creating/editing K-2 skills, understanding design decisions

### FINAL_SKILL_MAP_STATISTICS.json
- **Purpose:** Statistical summary of the skill map
- **Content:** Counts by grade, topic, skill type, etc.
- **Use For:** Reporting, validation, understanding distribution

---

## Archived Files

### archive/skills_final.json
- **Purpose:** Pre-AI redesign version (Version 1)
- **Content:** 1,155 skills (pre-redesign)
- **Use For:** Historical comparison, rollback reference
- **Note:** Contains 126 skills that were redesigned in FINAL version

### archive/skills_k8_ai_complete_WEEK2.json
- **Purpose:** Week 2 development snapshot
- **Content:** 1,140 skills (10 fewer than FINAL)
- **Use For:** Understanding Week 2 development, rollback point

### archive/skills_k8_ai_complete.BACKUP.json
- **Purpose:** Explicit backup before final changes
- **Content:** 1,119 skills
- **Use For:** Emergency rollback

---

## Usage Guide

### Extract Skills by Topic
```bash
# Extract all skills for topic T14
jq 'map(select(.topic_id == "T14"))' skills_k8_ai_complete_FINAL.json > skills_T14.json
```

### Extract Skills by Grade
```bash
# Extract all Kindergarten skills
jq 'map(select(.grade == "K"))' skills_k8_ai_complete_FINAL.json > skills_K.json
```

### Count Skills
```bash
# Total skills
jq '. | length' skills_k8_ai_complete_FINAL.json

# Skills by topic
jq 'group_by(.topic_id) | map({topic: .[0].topic_id, count: length})' skills_k8_ai_complete_FINAL.json
```

### Validate Skills
```bash
# Check for missing required fields
jq 'map(select(.id == null or .title == null or .grade == null))' skills_k8_ai_complete_FINAL.json
```

---

## Maintenance

### Adding New Skills
1. Use `CANONICAL_SKILL_SCHEMA.json` for field definitions
2. For K-2 skills, follow `k2_skill_format_spec.json`
3. Add to `skills_k8_ai_complete_FINAL.json`
4. Update `FINAL_SKILL_MAP_STATISTICS.json`
5. If creating new reference subsets, document purpose

### Creating Backups
```bash
# Before major changes
cp skills_k8_ai_complete_FINAL.json "skills_k8_ai_complete_FINAL.$(date +%Y%m%d).backup.json"
```

### File Naming Conventions
- **Production files:** Use descriptive names ending in `.json`
- **Backups:** Use `.BACKUP.json` or date suffix
- **Temporary/working:** Prefix with `temp_` or `working_`
- **Reference subsets:** Use ALL_CAPS prefix for visibility

---

## Version History

### Version 2 (Current - AI Enhanced)
- **File:** skills_k8_ai_complete_FINAL.json
- **Skills:** 1,150
- **Date:** 2025-11-17
- **Changes:** AI-enhanced redesign with improved K-2 coverage

### Version 1 (Archived)
- **File:** archive/skills_final.json
- **Skills:** 1,155
- **Date:** 2025-11-17 (pre-AI)
- **Changes:** Initial complete skill map

---

## Questions?

For questions about:
- **File usage:** See Usage Guide above
- **Skill schema:** See CANONICAL_SKILL_SCHEMA.json
- **K-2 formatting:** See k2_skill_format_spec.json
- **Version differences:** See UNIQUE_CONTENT_REPORT.md
- **Cleanup rationale:** See CLEANUP_PLAN.md

