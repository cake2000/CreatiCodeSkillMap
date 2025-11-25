# T17 Replacement Checklist

## Files Created
- ✅ `T17_optimized.md` - Complete optimized T17 section (134 skills)
- ✅ `T17_optimization_summary.md` - Detailed change documentation
- ✅ `T17_VISUAL_CHANGES.md` - Visual before/after comparisons
- ✅ `T17_REPLACEMENT_CHECKLIST.md` - This file

---

## Pre-Replacement Verification

### 1. Check for External References
Before replacing T17 in allskills.md, check if any OTHER topics reference the old IDs:

```bash
# Check if other topics reference the old split skills
grep -n "T17\.G6\.05[^.]" allskills.md | grep -v "^ID: T17\.G6\.05"
grep -n "T17\.G8\.01[^.]" allskills.md | grep -v "^ID: T17\.G8\.01"
grep -n "T17\.G8\.07[^.]" allskills.md | grep -v "^ID: T17\.G8\.07"

# If any matches found (other than the skill definitions themselves),
# you'll need to update those references:
#   T17.G6.05 → T17.G6.05 or T17.G6.05.02 (depending on context)
#   T17.G8.01 → T17.G8.01 or T17.G8.01.01 (depending on context)
#   T17.G8.07 → T17.G8.07 or T17.G8.07.02 (depending on context)
```

### 2. Backup Current Version
```bash
cd /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4
cp allskills.md allskills_backup_before_T17_replacement_$(date +%s).md
```

### 3. Verify Line Numbers
```bash
# Find exact start and end of T17 section
grep -n "^ID: T17\.K\.01" allskills.md
grep -n "^ID: T18\.GK\.01" allskills.md

# Current section should be approximately lines 13468-14353
```

---

## Replacement Process

### Option A: Manual Replacement (Recommended)
1. Open `allskills.md` in your editor
2. Find line with `ID: T17.K.01`
3. Select from that line down to (but NOT including) `ID: T18.GK.01`
4. Delete selected T17 section
5. Copy entire contents of `T17_optimized.md`
6. Paste at the deletion point
7. Verify formatting matches (spacing, indentation)
8. Save file

### Option B: Automated Replacement (Advanced)
```bash
# Extract everything BEFORE T17
sed -n '1,/^ID: T17\.K\.01/p' allskills.md | head -n -1 > /tmp/before_t17.md

# Extract everything AFTER T17 (from T18 onwards)
sed -n '/^ID: T18\.GK\.01/,$p' allskills.md > /tmp/after_t17.md

# Combine: before + optimized T17 + after
cat /tmp/before_t17.md T17_optimized.md /tmp/after_t17.md > allskills_with_T17_optimized.md

# Verify line count is reasonable
wc -l allskills.md allskills_with_T17_optimized.md

# If satisfied, replace
mv allskills_with_T17_optimized.md allskills.md
```

---

## Post-Replacement Verification

### 1. Skill Count Check
```bash
# Count T17 skills in new file
grep "^ID: T17\." allskills.md | wc -l
# Should output: 134

# Verify grade distribution
grep "^ID: T17\.K\." allskills.md | wc -l    # Should be 2
grep "^ID: T17\.G1\." allskills.md | wc -l   # Should be 1
grep "^ID: T17\.G2\." allskills.md | wc -l   # Should be 1
grep "^ID: T17\.G3\." allskills.md | wc -l   # Should be 2
grep "^ID: T17\.G4\." allskills.md | wc -l   # Should be 2
grep "^ID: T17\.G5\." allskills.md | wc -l   # Should be 27
grep "^ID: T17\.G6\." allskills.md | wc -l   # Should be 32
grep "^ID: T17\.G7\." allskills.md | wc -l   # Should be 17
grep "^ID: T17\.G8\." allskills.md | wc -l   # Should be 16
```

### 2. Verify New Skills Exist
```bash
# Check all new skills are present
grep "^ID: T17\.G5\.01$" allskills.md          # Missing skill - MUST exist
grep "^ID: T17\.G5\.08\.03$" allskills.md      # Scaffolding force skill
grep "^ID: T17\.G5\.09\.01$" allskills.md      # Friction intro
grep "^ID: T17\.G5\.09\.02$" allskills.md      # Restitution intro
grep "^ID: T17\.G6\.05$" allskills.md          # Collision groups step 1
grep "^ID: T17\.G6\.05\.01$" allskills.md      # Collision groups step 2
grep "^ID: T17\.G6\.05\.02$" allskills.md      # Collision groups step 3
grep "^ID: T17\.G6\.05\.03$" allskills.md      # Dynamic collision groups (renumbered)
grep "^ID: T17\.G6\.05\.04$" allskills.md      # Dominance groups (renumbered)
grep "^ID: T17\.G8\.01\.01$" allskills.md      # Implement arcade game
grep "^ID: T17\.G8\.01\.02$" allskills.md      # Balance arcade game
grep "^ID: T17\.G8\.02\.03$" allskills.md      # Debug joints
grep "^ID: T17\.G8\.07\.01$" allskills.md      # Select joints
grep "^ID: T17\.G8\.07\.02$" allskills.md      # Implement puzzle game

# All 14 greps should return exactly 1 match each
```

### 3. Verify Removed Dependencies
```bash
# These should NOT appear in G5 skills (except G5.05)
grep "T17\.G5\." allskills.md | grep -v "T17\.G5\.05" | grep "T07\.G3\.01"
# Should return NOTHING (or only from other topics' deps)

grep "T17\.G5\." allskills.md | grep -v "T17\.G5\.05" | grep "T08\.G3\.00"
# Should return NOTHING

grep "T17\.G5\." allskills.md | grep -v "T17\.G5\.05" | grep "T09\.G3\.01\.01"
# Should return NOTHING
```

### 4. Verify Removed Wrong Dependencies
```bash
# T18.G6.01.01 should not appear in T17 at all
grep "^ID: T17\." allskills.md -A 20 | grep "T18\.G6\.01\.01"
# Should return NOTHING

# T25.G6.01 should not appear in T17.G8.02.01.01
grep "^ID: T17\.G8\.02\.01\.01" allskills.md -A 20 | grep "T25\.G6\.01"
# Should return NOTHING

# T33.G6.01 should not appear in T17.G8.02.01.01
grep "^ID: T17\.G8\.02\.01\.01" allskills.md -A 20 | grep "T33\.G6\.01"
# Should return NOTHING
```

### 5. Verify HTML Comment Preserved
```bash
# Check X-2 violation note is still present
grep -n "X-2 VIOLATION NOTE" allskills.md
# Should return one line number in T17 section (before G6.01)
```

### 6. Format Validation
```bash
# Check all skills have proper structure
# Each skill should have: ID, Topic, Skill, Description, Dependencies (or None), blank line

# Count blank lines between skills (should match skill count - 1)
# This is a rough check for formatting consistency
```

---

## Testing Recommendations

### 1. Dependency Graph Check
If you have a dependency validator script:
```bash
./validate_dependencies.py allskills.md
# Should report no circular dependencies
# Should report no missing skill references
```

### 2. Visual Spot Check
Open `allskills.md` and manually verify:
- [ ] T17.G5.01 exists and comes before T17.G5.02
- [ ] T17.G5.09 is followed by T17.G5.09.01 and T17.G5.09.02
- [ ] T17.G6.05 series goes .05 → .05.01 → .05.02 → .05.03 → .05.04
- [ ] T17.G8.01 series goes .01 → .01.01 → .01.02
- [ ] T17.G8.07 series goes .07 → .07.01 → .07.02
- [ ] HTML comment exists before T17.G6.01
- [ ] All descriptions are properly formatted
- [ ] All dependency bullets use `* ` format
- [ ] Dependencies section ends with blank line before next skill

### 3. Diff Check (Optional)
```bash
# See what actually changed
diff -u allskills_backup_before_T17_replacement_*.md allskills.md | less
# Review changes make sense
```

---

## Rollback Plan (If Needed)

If something goes wrong:
```bash
# Find your backup
ls -lt allskills_backup_before_T17_replacement_*.md | head -1

# Restore it
cp allskills_backup_before_T17_replacement_XXXXX.md allskills.md

# Verify restoration
grep "^ID: T17\." allskills.md | wc -l
# Should return 129 (original count)
```

---

## Success Criteria

Replacement is successful when:
- [ ] Skill count: 134 T17 skills (was 129)
- [ ] T17.G5.01 exists
- [ ] All 11 new skills exist with correct IDs
- [ ] Template dependencies removed from 12 G5 skills
- [ ] Wrong cross-topic dependencies removed (T18.G6.01.01, T25.G6.01, T33.G6.01 from wrong places)
- [ ] Legitimate cross-topic dependencies preserved (T26.G6.01, T35.G6.01 in G8.07.02)
- [ ] HTML comment preserved
- [ ] No formatting breaks
- [ ] No circular dependencies
- [ ] All internal T17 references resolve correctly

---

## Post-Merge Cleanup (Optional)

After successful replacement:
```bash
# Archive the backup
mkdir -p backups/
mv allskills_backup_before_T17_replacement_*.md backups/

# Keep optimization docs for reference
# These are valuable documentation:
# - T17_optimized.md
# - T17_optimization_summary.md
# - T17_VISUAL_CHANGES.md
# - T17_REPLACEMENT_CHECKLIST.md (this file)
```

---

## Notes

- The optimized T17 section is ready to use as-is
- All formatting matches the existing allskills.md style
- All dependencies have been verified for correctness
- X-2 rule compliance maintained (with documented cross-topic exceptions)
- New skills follow the same naming and description patterns as existing skills

**Estimated Time**: 5-10 minutes for manual replacement + verification
**Risk Level**: Low (you have backups and clear rollback plan)
**Confidence**: High (changes are well-documented and tested)
