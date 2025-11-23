# T23 AI Perception - Implementation Guide
**Date:** 2025-11-23
**Status:** ✅ READY FOR IMPLEMENTATION

---

## EXECUTIVE SUMMARY

This guide provides step-by-step instructions to replace the current T23 (AI Perception) section in allskills.md with the completely rewritten version that incorporates ALL fixes from the comprehensive analysis.

**What You're Getting:**
- ✅ 58 total skills (up from 49)
- ✅ 6 NEW skills to fill scaffolding gaps
- ✅ Complete technical specifications for all detection tables
- ✅ All intra-T23 dependencies fixed
- ✅ All cross-topic dependencies preserved
- ✅ Better skill progression and learning paths
- ✅ Production-ready quality

---

## PRE-IMPLEMENTATION CHECKLIST

Before proceeding, ensure you have:

- [ ] Backup of current allskills.md
- [ ] Read T23_REWRITE_SUMMARY.md (understand what's changing)
- [ ] Read T23_VISUAL_CHANGES.md (see visual progression improvements)
- [ ] Verified T23_COMPLETE_REWRITE.md exists and is complete

---

## STEP-BY-STEP IMPLEMENTATION

### Step 1: Create Backup

```bash
cd /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4
cp allskills.md allskills_backup_before_t23_rewrite_$(date +%Y%m%d_%H%M%S).md
```

**Verification:**
```bash
ls -lh allskills_backup_before_t23_rewrite_*.md
```

Expected: Backup file created with timestamp

---

### Step 2: Locate Current T23 Section

**Current T23 Location:**
- **Start Line:** 13579 (ID: T23.GK.01)
- **End Line:** 14167 (last T23 skill before T24.GK.01)
- **Total Lines:** ~589 lines

**Verify location:**
```bash
sed -n '13579p' allskills.md  # Should show: ID: T23.GK.01
sed -n '14167p' allskills.md  # Should show last T23 skill
sed -n '14168p' allskills.md  # Should show: ID: T24.GK.01 or similar
```

---

### Step 3: Replace T23 Section

#### Option A: Using sed (Automated)

```bash
# Save new T23 content to temporary file
cp /media/binyu/USB2/dev/CreatiCodeSkillMap/T23_COMPLETE_REWRITE.md /tmp/t23_new.txt

# Remove header lines from new content (first 3 lines are comments)
sed -i '1,3d' /tmp/t23_new.txt

# Replace lines 13579-14167 with new content
sed -i '13579,14167d' allskills.md
sed -i '13578r /tmp/t23_new.txt' allskills.md

# Cleanup
rm /tmp/t23_new.txt
```

#### Option B: Manual Replacement (Safer)

1. Open `allskills.md` in your editor
2. Navigate to line 13579
3. Select from line 13579 to line 14167 (inclusive)
4. Delete selected lines
5. Open `T23_COMPLETE_REWRITE.md`
6. Copy everything EXCEPT the first 3 header/comment lines
7. Paste at line 13579 in `allskills.md`
8. Save file

---

### Step 4: Verify Replacement

Run these verification commands:

```bash
# 1. Count total T23 skills (should be 58)
grep "^ID: T23\." allskills.md | wc -l

# 2. Verify G6.10 no longer exists
grep "^ID: T23\.G6\.10" allskills.md
# Expected: No output (empty)

# 3. Verify G6.08.03 now exists
grep "^ID: T23\.G6\.08\.03" allskills.md
# Expected: ID: T23.G6.08.03

# 4. Verify all 6 new skills exist
grep "^ID: T23\.G5\.06\|^ID: T23\.G6\.04\.04\|^ID: T23\.G6\.06B\|^ID: T23\.G7\.01B\|^ID: T23\.G7\.06B\|^ID: T23\.G8\.01A" allskills.md
# Expected: 6 lines showing all new skill IDs

# 5. Verify T24 still follows T23
grep -A 2 "^ID: T23\.G8\.05" allskills.md | tail -1
# Expected: Should show ID: T24.GK.01 or blank lines before it

# 6. Count total skills in file (should increase by 7)
grep "^ID: T" allskills.md | wc -l
```

**Expected Results:**
- ✅ 58 T23 skills
- ✅ No T23.G6.10
- ✅ T23.G6.08.03 exists
- ✅ All 6 new skills present
- ✅ T24 section intact
- ✅ Total file skill count increased by 7

---

### Step 5: Verify Specific Enhancements

Check that enhanced descriptions are present:

```bash
# Check hand detection table structure (47 rows)
grep -A 2 "47 rows per detected hand" allskills.md

# Check body pose keypoints (all 17 listed)
grep -A 2 "all 17 keypoints" allskills.md

# Check face detection table (13 rows)
grep -A 2 "13 rows per detected face" allskills.md

# Check speech recognition timing
grep "1-3 seconds" allskills.md

# Check TTS parameters
grep "default 100, range 50-200" allskills.md
```

**Expected:** All searches return content with enhanced technical details

---

### Step 6: Verify Dependencies

Check critical dependency fixes:

```bash
# G6.02 should depend on G6.02.01
grep -A 6 "^ID: T23.G6.02$" allskills.md | grep "G6.02.01"

# G6.05 should depend on G6.04.04
grep -A 6 "^ID: T23.G6.05$" allskills.md | grep "G6.04.04"

# G6.06 should depend on G6.04.02
grep -A 8 "^ID: T23.G6.06$" allskills.md | grep "G6.04.02"

# G7.01 should depend on G6.04.04
grep -A 8 "^ID: T23.G7.01$" allskills.md | grep "G6.04.04"

# G7.02 should depend on G7.01
grep -A 8 "^ID: T23.G7.02$" allskills.md | grep "G7.01"
```

**Expected:** All dependency searches return matching lines

---

### Step 7: Verify Cross-Topic Dependencies Preserved

Ensure dependencies to other topics remain intact:

```bash
# Should still have T01 dependencies
grep "T01\." allskills.md | grep "T23" | head -5

# Should still have T22 dependencies
grep "T22\.G6\.01" allskills.md | grep "T23"

# Should still have T10 dependencies
grep "T10\.G5\.04\|T10\.G6\.02" allskills.md | grep -A 2 "T23"
```

**Expected:** Cross-topic dependencies still exist and unchanged

---

### Step 8: Validate File Integrity

```bash
# Check for syntax issues
# 1. Every skill should have an ID
awk '/^ID:/ {count++} END {print "Total IDs:", count}' allskills.md

# 2. No duplicate IDs
awk '/^ID: T23\./ {print $2}' allskills.md | sort | uniq -d
# Expected: No output (no duplicates)

# 3. Check for incomplete skills (ID without Topic)
awk '/^ID: T23\./ {id=$0; getline; if ($0 !~ /^Topic:/) print "Missing Topic after:", id}' allskills.md
# Expected: No output

# 4. Verify grade markers
grep "^Grade: [0-9K]" allskills.md | grep -c "Grade:"
# Expected: Number of grade markers (should have some for G5, G6, G7, G8)
```

---

## POST-IMPLEMENTATION TESTS

### Test 1: Skill Sequence Check

Verify skills are in proper order:

```bash
# Extract all T23 skill IDs in order
grep "^ID: T23\." allskills.md | awk '{print $2}' > /tmp/t23_order.txt

# Check order makes sense
cat /tmp/t23_order.txt
```

**Expected Order:**
```
T23.GK.01, T23.GK.02, T23.GK.03
T23.G1.01, T23.G1.02, T23.G1.03
T23.G2.01, T23.G2.02, T23.G2.03
T23.G3.01, T23.G3.02, T23.G3.03
T23.G4.01, T23.G4.02, T23.G4.03
T23.G5.01, T23.G5.02, T23.G5.03, T23.G5.04, T23.G5.05, T23.G5.06
T23.G6.01.01, T23.G6.01.02, T23.G6.01B
T23.G6.02.01, T23.G6.02
T23.G6.03A, T23.G6.03B
T23.G6.04.01, T23.G6.04.02, T23.G6.04.03, T23.G6.04.04
T23.G6.05, T23.G6.06, T23.G6.06B
T23.G6.07
T23.G6.08.01, T23.G6.08.02, T23.G6.08.03
T23.G6.09.01, T23.G6.09.02
T23.G7.00A, T23.G7.01, T23.G7.01B, T23.G7.02, T23.G7.03, T23.G7.04, T23.G7.05, T23.G7.06, T23.G7.06B
T23.G8.00A, T23.G8.01, T23.G8.01A, T23.G8.02, T23.G8.02B, T23.G8.03, T23.G8.04, T23.G8.05
```

---

### Test 2: Dependency Chain Validation

Verify no broken dependencies:

```bash
# Extract all T23 dependencies
grep -A 10 "^ID: T23\." allskills.md | grep "^\* T23\." | awk '{print $2}' | sort | uniq > /tmp/t23_deps.txt

# Check each dependency exists as a skill
while read dep; do
  dep_clean=$(echo "$dep" | sed 's/:$//')
  if ! grep -q "^ID: $dep_clean\$" allskills.md; then
    echo "BROKEN DEPENDENCY: $dep_clean not found"
  fi
done < /tmp/t23_deps.txt
```

**Expected:** No output (no broken dependencies)

---

### Test 3: Grade Distribution Check

```bash
# Count skills per grade
echo "K: $(grep -A 20 "^ID: T23.GK" allskills.md | grep -c "^ID: T23.GK")"
echo "1: $(grep -A 20 "^ID: T23.G1" allskills.md | grep -c "^ID: T23.G1")"
echo "2: $(grep -A 20 "^ID: T23.G2" allskills.md | grep -c "^ID: T23.G2")"
echo "3: $(grep -A 20 "^ID: T23.G3" allskills.md | grep -c "^ID: T23.G3")"
echo "4: $(grep -A 20 "^ID: T23.G4" allskills.md | grep -c "^ID: T23.G4")"
echo "5: $(grep "^ID: T23.G5" allskills.md | wc -l)"
echo "6: $(grep "^ID: T23.G6" allskills.md | wc -l)"
echo "7: $(grep "^ID: T23.G7" allskills.md | wc -l)"
echo "8: $(grep "^ID: T23.G8" allskills.md | wc -l)"
```

**Expected:**
```
K: 3
1: 3
2: 3
3: 3
4: 3
5: 7  (was 6, added G5.06)
6: 20 (was 17, added G6.04.04, G6.06B, renumbered G6.10→G6.08.03)
7: 9  (was 7, added G7.01B, G7.06B)
8: 7  (was 6, added G8.01A)
```

---

## TROUBLESHOOTING

### Issue: Skill Count Wrong

**Symptom:** `grep "^ID: T23\." allskills.md | wc -l` returns something other than 58

**Solutions:**
1. Check if replacement captured all skills from T23_COMPLETE_REWRITE.md
2. Verify header lines (first 3 comment lines) weren't included
3. Restore from backup and retry

---

### Issue: G6.10 Still Exists

**Symptom:** `grep "^ID: T23\.G6\.10" allskills.md` returns results

**Solutions:**
1. Old content wasn't fully replaced
2. Restore from backup and retry with correct line range
3. Manually search and remove T23.G6.10

---

### Issue: New Skills Missing

**Symptom:** One or more new skills (G5.06, G6.04.04, etc.) not found

**Solutions:**
1. Verify T23_COMPLETE_REWRITE.md is complete
2. Check if content was truncated during copy/paste
3. Restore from backup and retry

---

### Issue: Broken Dependencies

**Symptom:** Dependency validation finds broken links

**Solutions:**
1. Compare dependencies in T23_COMPLETE_REWRITE.md vs allskills.md
2. Manually fix broken links
3. Or restore from backup and retry implementation

---

## ROLLBACK PROCEDURE

If issues occur and you need to revert:

```bash
# Find your backup
ls -lh allskills_backup_before_t23_rewrite_*.md

# Restore (replace TIMESTAMP with actual timestamp)
cp allskills_backup_before_t23_rewrite_TIMESTAMP.md allskills.md

# Verify restoration
grep "^ID: T23\." allskills.md | wc -l  # Should be original count (49 or 51)
```

---

## SUCCESS CRITERIA

✅ **IMPLEMENTATION SUCCESSFUL IF:**

1. ✅ Total T23 skills = 58
2. ✅ No T23.G6.10 exists
3. ✅ T23.G6.08.03 exists (3D pose moved earlier)
4. ✅ All 6 new skills exist (G5.06, G6.04.04, G6.06B, G7.01B, G7.06B, G8.01A)
5. ✅ Enhanced descriptions present (47-row table, 17 keypoints, 13-row face table)
6. ✅ All dependency fixes applied (G6.02→G6.02.01, G6.06→G6.04.02, etc.)
7. ✅ Cross-topic dependencies preserved (T01, T06, T08, T09, T10, T11, T16, T22)
8. ✅ No broken dependencies
9. ✅ T24 section still intact after T23
10. ✅ File syntax valid (no incomplete skills)

---

## FINAL VALIDATION SCRIPT

Run this comprehensive validation:

```bash
#!/bin/bash
echo "=== T23 REWRITE VALIDATION ==="
echo ""

# Test 1: Skill count
total=$(grep "^ID: T23\." allskills.md | wc -l)
echo "1. Total T23 skills: $total (expected: 58)"
[ "$total" -eq 58 ] && echo "   ✅ PASS" || echo "   ❌ FAIL"

# Test 2: G6.10 removed
old_skill=$(grep "^ID: T23\.G6\.10" allskills.md | wc -l)
echo "2. T23.G6.10 removed: $([ "$old_skill" -eq 0 ] && echo "Yes" || echo "No")"
[ "$old_skill" -eq 0 ] && echo "   ✅ PASS" || echo "   ❌ FAIL"

# Test 3: G6.08.03 exists
new_skill=$(grep "^ID: T23\.G6\.08\.03" allskills.md | wc -l)
echo "3. T23.G6.08.03 exists: $([ "$new_skill" -eq 1 ] && echo "Yes" || echo "No")"
[ "$new_skill" -eq 1 ] && echo "   ✅ PASS" || echo "   ❌ FAIL"

# Test 4: New skills
new_count=$(grep "^ID: T23\.G5\.06\|^ID: T23\.G6\.04\.04\|^ID: T23\.G6\.06B\|^ID: T23\.G7\.01B\|^ID: T23\.G7\.06B\|^ID: T23\.G8\.01A" allskills.md | wc -l)
echo "4. New skills added: $new_count / 6"
[ "$new_count" -eq 6 ] && echo "   ✅ PASS" || echo "   ❌ FAIL"

# Test 5: Enhanced descriptions
enhanced=$(grep "47 rows per detected hand\|all 17 keypoints\|13 rows per detected face" allskills.md | wc -l)
echo "5. Enhanced descriptions: $enhanced / 3"
[ "$enhanced" -eq 3 ] && echo "   ✅ PASS" || echo "   ❌ FAIL"

echo ""
echo "=== VALIDATION COMPLETE ==="
```

Save as `validate_t23.sh`, make executable, and run:
```bash
chmod +x validate_t23.sh
./validate_t23.sh
```

---

## COMPLETION CHECKLIST

After implementation, mark completed items:

- [ ] Backup created
- [ ] T23 section replaced (lines 13579-14167)
- [ ] Skill count = 58
- [ ] G6.10 removed, G6.08.03 exists
- [ ] All 6 new skills present
- [ ] Enhanced descriptions verified
- [ ] Dependencies fixed
- [ ] Cross-topic dependencies preserved
- [ ] No broken dependencies found
- [ ] T24 section intact
- [ ] Validation script passes all tests
- [ ] Git commit created (if using version control)

---

## NEXT STEPS

After successful implementation:

1. **Test in Practice:**
   - Review skills with educators
   - Test learning progressions with students
   - Verify block syntax with CreatiCode platform

2. **Monitor Issues:**
   - Track any new gaps or inconsistencies
   - Gather feedback from users
   - Document any adjustments needed

3. **Version Control:**
   ```bash
   git add skillsv4/allskills.md
   git commit -m "T23 AI Perception: Complete rewrite with 6 new skills

   - Added G5.06 (API workflow), G6.04.04 (gesture practice), G6.06B (patterns)
   - Added G7.01B (OR logic), G7.06B (optimization), G8.01A (KNN practice)
   - Renumbered G6.10 → G6.08.03 for better progression
   - Enhanced all detection table specifications (hand: 47 rows, body: 17 keypoints, face: 13 rows)
   - Fixed all intra-T23 dependencies
   - Total: 58 skills (was 49)

   Based on T23_COMPREHENSIVE_ISSUES_ANALYSIS.md"
   ```

---

**Document Version:** 1.0
**Created:** 2025-11-23
**Status:** ✅ READY FOR USE
