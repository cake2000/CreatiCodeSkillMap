# Grade 8 Fixes - Quick Start Guide

## TL;DR

Fix all Grade 8 issues in 3 steps:

```bash
# 1. Apply fixes
python3 apply_g8_fixes.py

# 2. Validate fixes
python3 validate_g8_fixes.py

# 3. Review report
cat G8_FIXES_APPLIED_REPORT.md
```

## What Gets Fixed

Based on `G8_ANALYSIS_REPORT_FINAL.json`, this fixes:

1. **8 circular dependencies** - G1 skills with self-references
2. **~160 grade constraint violations** - G8 skills depending on G5 or lower
3. **8 transitive dependencies** - Redundant dependency paths

## Step-by-Step

### Step 1: Apply Fixes

```bash
python3 apply_g8_fixes.py
```

**What it does:**
- Creates backup: `skillsv4/allskills.md.backup_g8_TIMESTAMP`
- Fixes G1 self-references (T25, T34, T35, T36)
- Upgrades/removes low-grade dependencies in G8 skills
- Removes transitive dependencies
- Generates `G8_FIXES_APPLIED_REPORT.md`

**Expected output:**
```
====================================================================================
GRADE 8 COMPREHENSIVE FIX APPLICATOR
====================================================================================

Loading analysis report...
Total G8 skills: 163
High priority issues: 168
Medium priority issues: 8

Creating backup: .../allskills.md.backup_g8_20251120_HHMMSS
Backup created successfully

Parsing skills file...
Total skills parsed: XXXX

PHASE 1: Fixing G1 self-references
====================================================================================
✓ T25.G1.01: Removed self-reference
✓ T34.G1.01: Removed self-reference
✓ T35.G1.01: Removed self-reference
✓ T36.G1.01: Removed self-reference

PHASE 2: Upgrading low-grade dependencies in G8 skills
====================================================================================
Processing 163 G8 skills...

✓ T01.G8.02: 1 changes
    Upgraded T01.G3.01 (G3) → T01.G6.01 (G6)
✓ T01.G8.03: 1 changes
    Removed T01.G1.01 (G1) - no suitable G6+ replacement
...

G8 skills modified: ~160

PHASE 3: Removing transitive dependencies
====================================================================================
✓ T25.G8.02: 1 transitive dependencies removed
    Removed transitive dependency: T25.G1.01
...

Reconstructing allskills.md...
Writing updated file...
File updated successfully

Detailed report saved to: G8_FIXES_APPLIED_REPORT.md

====================================================================================
FINAL STATISTICS
====================================================================================
G1 self-references fixed: 4
G8 skills modified: ~160
Dependencies upgraded: XX
  G5 → G6: XX
  G5 → G7: XX
  G4 → G6: XX
  G3 → G6: XX
  ...
Dependencies removed (no G6+ replacement): XX
Transitive dependencies removed: 8

Total skills modified: ~170

====================================================================================
COMPLETE - All G8 fixes applied successfully!
====================================================================================
```

### Step 2: Validate Fixes

```bash
python3 validate_g8_fixes.py
```

**What it checks:**
- ✓ No G8 skills depend on G5 or lower
- ✓ No self-references anywhere
- ✓ No circular dependencies
- ✓ No transitive dependencies in target skills

**Expected output (SUCCESS):**
```
====================================================================================
G8 FIXES VALIDATION
====================================================================================

Parsing skills file...
Total skills parsed: XXXX

Skills by grade:
  GK: XX
  G1: XX
  G2: XX
  ...
  G8: 163

CHECK 1: G8 grade constraints (should only depend on G6+)
--------------------------------------------------------------------------------
✓ PASSED: All G8 skills depend only on G6+

CHECK 2: Self-references
--------------------------------------------------------------------------------
✓ PASSED: No self-references found

CHECK 3: Circular dependencies
--------------------------------------------------------------------------------
✓ PASSED: No circular dependencies found

CHECK 4: Transitive dependencies (target G8 skills)
--------------------------------------------------------------------------------
✓ PASSED: No transitive dependencies in target skills

====================================================================================
VALIDATION SUMMARY
====================================================================================
✓ VALIDATION PASSED: All checks successful!

G8 fixes have been applied correctly:
  - No G8 skills depend on G5 or lower
  - No self-references in any skills
  - No circular dependencies
  - No transitive dependencies in target skills

====================================================================================
Validation success saved to: G8_VALIDATION_SUCCESS.txt
```

### Step 3: Review Changes

```bash
# View summary
head -50 G8_FIXES_APPLIED_REPORT.md

# View full detailed report
less G8_FIXES_APPLIED_REPORT.md

# Search for specific skill
grep "T01.G8.02" G8_FIXES_APPLIED_REPORT.md
```

## If Something Goes Wrong

### Restore from Backup

```bash
# Find latest backup
ls -lt skillsv4/allskills.md.backup_g8_* | head -1

# Restore it
cp skillsv4/allskills.md.backup_g8_TIMESTAMP skillsv4/allskills.md
```

### Check What Changed

```bash
# Compare with backup
diff skillsv4/allskills.md.backup_g8_TIMESTAMP skillsv4/allskills.md | less

# Count changes
diff skillsv4/allskills.md.backup_g8_TIMESTAMP skillsv4/allskills.md | grep "^<" | wc -l
```

## Understanding the Output

### Dependency Upgrade Types

- **GX → GY**: Dependency upgraded from grade X to grade Y
  - Example: `G3 → G6` means a G3 dependency was replaced with a G6 equivalent

### Change Messages

- **"Upgraded TX.GX.XX (GX) → TY.GY.YY (GY)"**
  - Found and replaced with higher-grade equivalent

- **"Removed TX.GX.XX (GX) - no suitable G6+ replacement"**
  - No G6+ skill found in same topic; dependency removed

- **"Removed transitive dependency: TX.GX.XX"**
  - Dependency was redundant (reachable through another path)

- **"Removed self-reference"**
  - Skill was depending on itself (error)

## Files Created

1. **allskills.md.backup_g8_TIMESTAMP** - Original file backup
2. **G8_FIXES_APPLIED_REPORT.md** - Detailed change report
3. **G8_VALIDATION_SUCCESS.txt** or **G8_VALIDATION_FAILURES.json** - Validation results

## Next Steps

After successful validation:

1. **Review the report** - Check that changes make sense
2. **Spot-check some skills** - Verify a few manually
3. **Run your tests** - If you have automated tests
4. **Commit changes** - Once satisfied

```bash
# Example spot check
grep -A20 "^ID: T01.G8.02" skillsv4/allskills.md

# Example commit
git add skillsv4/allskills.md
git commit -m "Fix G8 dependencies: remove circular refs and upgrade low-grade deps

- Fixed 4 G1 self-references (T25, T34, T35, T36)
- Upgraded/removed ~160 low-grade dependencies in G8 skills
- Removed 8 transitive dependencies
- All G8 skills now depend only on G6, G7, or G8

See G8_FIXES_APPLIED_REPORT.md for details"
```

## Documentation

- **G8_FIX_SCRIPT_README.md** - Detailed documentation
- **G8_ANALYSIS_REPORT_FINAL.json** - Original analysis
- **G8_FIXES_APPLIED_REPORT.md** - Changes made
- **This guide** - Quick start

## Troubleshooting

### "No suitable G6+ replacement"

This is expected for some skills. It means:
- The dependency was too low-grade (G5 or below)
- No equivalent G6+ skill exists in that topic
- The dependency was removed

**Action**: Review these cases in the report. You may need to:
- Create the missing G6+ skill
- Accept the removal (dependency was too fundamental)
- Manually add a different dependency if needed

### Validation fails

If validation shows failures after applying fixes:

1. **Check the G8_VALIDATION_FAILURES.json** file
2. **Review what failed** in the validation output
3. **Fix manually** or re-run the fix script
4. **Report the issue** if it's unexpected

### Script errors

If the script crashes:

1. **Check Python version** (needs Python 3.6+)
2. **Verify file paths** are correct
3. **Check file permissions** (needs write access)
4. **Restore from backup** if needed
5. **Run validation** to see current state

---

**Last Updated**: 2025-11-20
**Script Version**: 1.0
