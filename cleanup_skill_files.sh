#!/bin/bash

##############################################################################
# CreatiCode Skill Files Cleanup Script
#
# Purpose: Clean up redundant skill JSON files, keeping only essential files
# Date: 2025-11-17
#
# Actions:
#   - Keep 8 essential files in root
#   - Archive 3 historical versions
#   - Delete 25 redundant files
#
# IMPORTANT: Review CLEANUP_PLAN.md before running this script!
##############################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Base directory
BASE_DIR="/media/binyu/USB2/dev/CreatiCodeSkillMap"
ARCHIVE_DIR="${BASE_DIR}/archive"
LOG_FILE="${BASE_DIR}/cleanup_log.txt"

# Initialize log
echo "==============================================================================" > "$LOG_FILE"
echo "CreatiCode Skill Files Cleanup Log" >> "$LOG_FILE"
echo "Date: $(date)" >> "$LOG_FILE"
echo "==============================================================================" >> "$LOG_FILE"
echo "" >> "$LOG_FILE"

##############################################################################
# Functions
##############################################################################

log() {
    echo "$1" | tee -a "$LOG_FILE"
}

log_action() {
    echo "$1" >> "$LOG_FILE"
}

print_header() {
    echo -e "${BLUE}==============================================================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}==============================================================================${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

##############################################################################
# Pre-flight Checks
##############################################################################

print_header "Pre-flight Checks"

# Check if we're in the right directory
if [ ! -f "${BASE_DIR}/skills_k8_ai_complete_FINAL.json" ]; then
    print_error "Cannot find canonical file: skills_k8_ai_complete_FINAL.json"
    print_error "Are you in the correct directory?"
    exit 1
fi
print_success "Found canonical file: skills_k8_ai_complete_FINAL.json"

# Verify canonical file has 1150 skills
SKILL_COUNT=$(jq '. | length' "${BASE_DIR}/skills_k8_ai_complete_FINAL.json")
if [ "$SKILL_COUNT" -eq 1150 ]; then
    print_success "Canonical file verified: 1150 skills"
else
    print_error "Canonical file has $SKILL_COUNT skills, expected 1150"
    exit 1
fi

# Count files before cleanup
BEFORE_COUNT=$(ls -1 "${BASE_DIR}"/*.json 2>/dev/null | wc -l)
BEFORE_SIZE=$(du -sh "${BASE_DIR}"/*.json 2>/dev/null | tail -1 | awk '{print $1}' || echo "0")
log "Files before cleanup: $BEFORE_COUNT"
log "Total size before: $BEFORE_SIZE"
echo ""

##############################################################################
# User Confirmation
##############################################################################

print_header "Cleanup Plan Summary"
echo ""
echo "This script will:"
echo "  - Keep 8 essential files in root directory"
echo "  - Move 3 files to archive/ directory"
echo "  - Delete 25 redundant files"
echo ""
echo "Expected outcome:"
echo "  - Files in root: 36 → 8 skill files"
echo "  - Space saved: ~4.36 MB"
echo ""
print_warning "This action cannot be easily undone (except via git)!"
echo ""
read -p "Do you want to proceed? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    print_warning "Cleanup cancelled by user"
    exit 0
fi

##############################################################################
# Step 1: Create Archive Directory
##############################################################################

print_header "Step 1: Creating Archive Directory"

if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir -p "$ARCHIVE_DIR"
    print_success "Created archive directory: $ARCHIVE_DIR"
    log_action "mkdir $ARCHIVE_DIR"
else
    print_success "Archive directory already exists"
fi
echo ""

##############################################################################
# Step 2: Archive Historical Files
##############################################################################

print_header "Step 2: Archiving Historical Files"

ARCHIVE_FILES=(
    "skills_final.json"
    "skills_k8_ai_complete_WEEK2.json"
    "skills_k8_ai_complete.BACKUP.json"
)

for file in "${ARCHIVE_FILES[@]}"; do
    if [ -f "${BASE_DIR}/${file}" ]; then
        mv "${BASE_DIR}/${file}" "${ARCHIVE_DIR}/"
        print_success "Archived: $file"
        log_action "mv ${BASE_DIR}/${file} ${ARCHIVE_DIR}/"
    else
        print_warning "File not found, skipping: $file"
    fi
done
echo ""

##############################################################################
# Step 3: Delete Redundant Files
##############################################################################

print_header "Step 3: Deleting Redundant Files"

# Group 1: Pre-AI Redesign Duplicates
DELETE_FILES=(
    # Pre-AI duplicates
    "skills.json"
    "skills_enriched.json"
    "skills_final_enriched.json"
    "extracted_skills_raw.json"
    "skills_with_dependencies.json"

    # Intermediate versions
    "skills_k8_ai_complete.json"
    "skills_k8_ai_complete_REVISED.json"
    "skills_complete_k8.json"
    "skills_enriched_partial.json"

    # K-2 working files
    "skills_k2_complete_all.json"
    "skills_k2_with_dependencies.json"
    "skills_k2_redesigned.json"
    "skills_k2_all_remaining_topics.json"
    "skills_k2_batch_comprehensive.json"
    "skills_k2_redesigned_partial.json"
    "skills_k2_additional_topics.json"
    "skills_k2_new_batch.json"

    # Extraction/analysis files
    "skills_T14_T24_extracted.json"
    "grade_7_8_skills_for_analysis.json"
    "grade_7_8_skills_extracted.json"
    "t01_t05_skills.json"
)

DELETED_COUNT=0
DELETED_SIZE=0

for file in "${DELETE_FILES[@]}"; do
    if [ -f "${BASE_DIR}/${file}" ]; then
        # Get file size before deletion
        FILE_SIZE=$(stat -c%s "${BASE_DIR}/${file}" 2>/dev/null || echo 0)
        DELETED_SIZE=$((DELETED_SIZE + FILE_SIZE))

        rm "${BASE_DIR}/${file}"
        print_success "Deleted: $file"
        log_action "rm ${BASE_DIR}/${file}"
        DELETED_COUNT=$((DELETED_COUNT + 1))
    else
        print_warning "File not found, skipping: $file"
    fi
done

# Convert bytes to MB
DELETED_SIZE_MB=$(echo "scale=2; $DELETED_SIZE / 1024 / 1024" | bc)

echo ""
print_success "Deleted $DELETED_COUNT files (~${DELETED_SIZE_MB} MB)"
echo ""

##############################################################################
# Step 4: Verify Final State
##############################################################################

print_header "Step 4: Verification"

# Files that should remain
KEEP_FILES=(
    "skills_k8_ai_complete_FINAL.json"
    "FOUNDATIONAL_41_SKILLS.json"
    "WEEK2_NEW_SKILLS.json"
    "CREATIVE_SKILLS_3.json"
    "WEEK2_SKILLS_QUICK_REFERENCE.json"
    "CANONICAL_SKILL_SCHEMA.json"
    "k2_skill_format_spec.json"
    "FINAL_SKILL_MAP_STATISTICS.json"
)

echo "Verifying essential files..."
ALL_PRESENT=true
for file in "${KEEP_FILES[@]}"; do
    if [ -f "${BASE_DIR}/${file}" ]; then
        print_success "$file"
    else
        print_error "MISSING: $file"
        ALL_PRESENT=false
    fi
done

if [ "$ALL_PRESENT" = false ]; then
    print_error "Some essential files are missing!"
    exit 1
fi

echo ""

# Verify archive
echo "Verifying archived files..."
ARCHIVE_PRESENT=true
for file in "${ARCHIVE_FILES[@]}"; do
    if [ -f "${ARCHIVE_DIR}/${file}" ]; then
        print_success "$file (in archive/)"
    else
        print_warning "NOT ARCHIVED: $file"
        ARCHIVE_PRESENT=false
    fi
done

echo ""

##############################################################################
# Step 5: Generate Summary
##############################################################################

print_header "Cleanup Summary"

AFTER_COUNT=$(ls -1 "${BASE_DIR}"/*skill*.json 2>/dev/null | wc -l || echo 0)
AFTER_SIZE=$(du -sh "${BASE_DIR}"/*skill*.json 2>/dev/null | tail -1 | awk '{print $1}' || echo "0")

echo "Files before:     $BEFORE_COUNT skill JSON files"
echo "Files after:      $AFTER_COUNT skill JSON files in root"
echo "Files archived:   ${#ARCHIVE_FILES[@]} files"
echo "Files deleted:    $DELETED_COUNT files"
echo ""
echo "Space saved:      ~${DELETED_SIZE_MB} MB"
echo ""

log ""
log "=============================================================================="
log "Summary"
log "=============================================================================="
log "Files before:     $BEFORE_COUNT"
log "Files after:      $AFTER_COUNT in root + ${#ARCHIVE_FILES[@]} in archive"
log "Files deleted:    $DELETED_COUNT"
log "Space saved:      ~${DELETED_SIZE_MB} MB"
log ""

##############################################################################
# Step 6: Create FILE_ORGANIZATION.md
##############################################################################

print_header "Step 6: Creating Documentation"

cat > "${BASE_DIR}/FILE_ORGANIZATION.md" << 'EOF'
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

EOF

print_success "Created FILE_ORGANIZATION.md"
log_action "Created FILE_ORGANIZATION.md"

echo ""

##############################################################################
# Done
##############################################################################

print_header "Cleanup Complete!"

echo ""
echo "Next steps:"
echo "  1. Review FILE_ORGANIZATION.md for file structure"
echo "  2. Commit changes to git:"
echo "     git add ."
echo "     git commit -m 'Clean up redundant skill files, keep only essential files'"
echo "  3. Review cleanup_log.txt for detailed actions"
echo ""

print_success "All done! Skill files are now organized."
echo ""
