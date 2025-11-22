# T14 (2D Games) Integration Guide

**Purpose**: Step-by-step instructions for integrating the optimized T14 section into allskills.md

**Date**: 2025-11-21
**Status**: Ready for integration

---

## Pre-Integration Checklist

- [ ] Backup current `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`
- [ ] Review all four optimization documents:
  - [ ] T14_EXECUTIVE_SUMMARY.md (quick overview)
  - [ ] T14_optimization_report.md (full analysis)
  - [ ] T14_changes_summary.md (detailed changes)
  - [ ] T14_updated_section.md (new content)
- [ ] Confirm no other work in progress on allskills.md
- [ ] Verify git status is clean or changes are committed

---

## Integration Steps

### Step 1: Locate Current T14 Section

Current T14 section in allskills.md:
- **Start line**: 6016 (ID: T14.GK.01)
- **End line**: 6774 (last line of T14.G8.05)
- **Total lines**: 759 lines

To verify:
```bash
grep -n "^ID: T14\." /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | head -1
grep -n "^ID: T14\." /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | tail -1
```

### Step 2: Extract Old Section (For Backup)

```bash
cd /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/
sed -n '6016,6774p' allskills.md > T14_old_section_backup.md
```

This creates a backup of the original T14 section.

### Step 3: Replace Section in allskills.md

**Option A: Manual Replacement (Recommended for safety)**
1. Open allskills.md in your editor
2. Navigate to line 6016
3. Select lines 6016-6774 (entire T14 section)
4. Delete selected lines
5. Copy content from T14_updated_section.md (starting after "## Topic 14: 2D Games")
6. Paste at line 6016
7. Save file

**Option B: Automated Replacement (Advanced)**
```bash
cd /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/

# Create temp file with before + new T14 + after
head -n 6015 allskills.md > allskills_temp.md
cat T14_updated_section.md >> allskills_temp.md
tail -n +6775 allskills.md >> allskills_temp.md

# Backup original and replace
cp allskills.md allskills_backup_$(date +%Y%m%d_%H%M%S).md
mv allskills_temp.md allskills.md
```

### Step 4: Verify Integration

Run these checks:

**Check 1: Skill count**
```bash
grep -c "^ID: T14\." allskills.md
# Expected: 73 (was 66)
```

**Check 2: No duplicate IDs**
```bash
grep "^ID: T14\." allskills.md | sort | uniq -d
# Expected: (empty output)
```

**Check 3: New skills present**
```bash
grep "^ID: T14\.G3\.10\.01" allskills.md
grep "^ID: T14\.G4\.04\.01" allskills.md
grep "^ID: T14\.G5\.08\.01" allskills.md
grep "^ID: T14\.G6\.07" allskills.md
# Expected: All found
```

**Check 4: Old skill removed**
```bash
grep "^ID: T14\.G4\.04$" allskills.md
grep "^ID: T14\.G5\.08$" allskills.md
# Expected: Not found (these were split)
```

**Check 5: File integrity**
```bash
wc -l allskills.md
# Expected: Original line count - 759 + new T14 lines (~800) = ~similar total
```

---

## Post-Integration Tasks

### Task 1: Update Cross-References

Check if any other topics reference old T14 skill IDs:

```bash
# Search for references to split skills
grep "T14\.G4\.04[^.]" allskills.md | grep -v "^ID:"
grep "T14\.G5\.08[^.]" allskills.md | grep -v "^ID:"

# These should now reference:
# T14.G4.04 → T14.G4.04.01 or T14.G4.04.02
# T14.G5.08 → T14.G5.08.01, T14.G5.08.02, or T14.G5.08.03
```

**Action**: Update any references found in other topics to use the new sub-skill IDs.

### Task 2: Verify No Broken Dependencies

Run dependency validator (if you have one):

```bash
# Example validation script (create if needed)
python validate_dependencies.py allskills.md
```

Or manually check:
```bash
# Extract all dependencies
grep "^\* T" allskills.md | sort | uniq > all_dependencies.txt

# Extract all IDs
grep "^ID: T" allskills.md | sed 's/^ID: //' | sort > all_skills.txt

# Find dependencies that don't exist as skills
comm -23 all_dependencies.txt all_skills.txt
# Expected: Only dependencies to external resources (if any)
```

### Task 3: Git Commit

```bash
cd /media/binyu/USB2/dev/CreatiCodeSkillMap/

git add skillsv4/allskills.md
git add skillsv4/T14_*.md

git commit -m "Optimize T14 (2D Games) topic - Phase 1

- Fixed X-2 rule violation in T14.G3.07
- Added 7 new skills for better scaffolding
- Reduced avg dependencies by 26%
- Split overly broad skills (enemy movement, waves)
- Enhanced descriptions with specific block names
- Verified alignment with CreatiCode platform

Details in T14_optimization_report.md
Total skills: 66 → 73"
```

---

## Rollback Procedure (If Needed)

If something goes wrong:

```bash
cd /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/

# Restore from backup
cp allskills_backup_YYYYMMDD_HHMMSS.md allskills.md

# Or restore from git
git checkout HEAD -- allskills.md
```

---

## Validation Checklist

After integration, verify:

- [ ] File opens without errors
- [ ] All 73 T14 skills present
- [ ] No duplicate skill IDs
- [ ] New skills (T14.G3.10.01, T14.G4.04.01-02, T14.G5.08.01-03, T14.G6.07) exist
- [ ] Old skills (T14.G4.04, T14.G5.08) removed
- [ ] No broken dependencies (all referenced skills exist)
- [ ] Cross-topic dependencies preserved (T01-T13 references intact)
- [ ] File line count is reasonable (~similar to before)
- [ ] No formatting issues (check indentation, blank lines)
- [ ] Git commit successful

---

## Common Issues & Solutions

### Issue 1: "Skill ID not found" errors

**Symptom**: Dependency references a skill that doesn't exist
**Cause**: Old skill ID still referenced after split
**Solution**: Update dependency to use new sub-skill ID

Example:
```
Old: * T14.G4.04: Simple enemy movement
New: * T14.G4.04.01: Enemy patrol movement
  OR * T14.G4.04.02: Enemy bounce movement
```

### Issue 2: Duplicate skill IDs

**Symptom**: Same skill ID appears twice
**Cause**: Manual edit error during integration
**Solution**: Remove duplicate, keep the new version

### Issue 3: Line count doesn't match

**Symptom**: File has significantly different line count
**Cause**: Copy/paste error or missing section
**Solution**: Re-check that all content was copied correctly

### Issue 4: Formatting broken

**Symptom**: Skills run together or have wrong indentation
**Cause**: Copy/paste lost blank lines or tabs
**Solution**: Compare formatting with T14_updated_section.md and fix

---

## Contact & Support

If you encounter issues:

1. **Check the documentation**:
   - T14_EXECUTIVE_SUMMARY.md for quick overview
   - T14_changes_summary.md for specific changes
   - T14_dependency_visualization.md for dependency help

2. **Review backups**:
   - T14_old_section_backup.md (original section)
   - allskills_backup_*.md (timestamped backups)

3. **Verify against source**:
   - T14_updated_section.md is the authoritative new content

4. **Use git history**:
   ```bash
   git log --oneline -- skillsv4/allskills.md
   git diff HEAD~1 skillsv4/allskills.md
   ```

---

## Integration Timeline

**Recommended schedule**:

1. **Day 1**: Review optimization documents, run pre-integration checks
2. **Day 2**: Perform integration, run verification checks
3. **Day 3**: Update any cross-references, test with sample lessons
4. **Day 4**: Git commit, announce changes to team

**Estimated time**: 2-4 hours total

---

## Success Criteria

Integration is successful when:

✅ All 73 T14 skills are present in allskills.md
✅ No duplicate IDs
✅ No broken dependencies
✅ New skills can be found and used
✅ Old split skills are removed
✅ File passes validation checks
✅ Git commit is clean
✅ Backup exists in case of rollback

---

## Next Steps After Integration

1. **Notify stakeholders**: Announce T14 optimization is complete
2. **Update lesson plans**: Review any lessons using T14.G4.04 or T14.G5.08
3. **Update assessments**: Ensure tests cover new sub-skills appropriately
4. **Teacher training**: Brief teachers on new skill structure
5. **Monitor feedback**: Track any issues reported by users
6. **Plan Phase 2**: Begin cross-topic dependency review for other topics

---

## Files Reference

All files in `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/`:

| File | Purpose | Size |
|------|---------|------|
| `T14_EXECUTIVE_SUMMARY.md` | Quick overview for stakeholders | 4 KB |
| `T14_optimization_report.md` | Full analysis and recommendations | 32 KB |
| `T14_changes_summary.md` | Detailed changelog of all modifications | 18 KB |
| `T14_updated_section.md` | Complete new T14 section (MAIN FILE) | 28 KB |
| `T14_dependency_visualization.md` | Visual dependency maps and metrics | 15 KB |
| `T14_INTEGRATION_GUIDE.md` | This file - integration instructions | 7 KB |

**Total documentation**: ~104 KB (very comprehensive!)

---

## Final Notes

- This optimization focused **only on T14 internal coherence**
- All cross-topic dependencies were **preserved**
- No skills were **deleted** (only split or enhanced)
- All changes are **backward compatible** for student progression
- Platform alignment was **verified** against CreatiCode blocks

**Status**: Ready for integration ✅

---

END OF INTEGRATION GUIDE
