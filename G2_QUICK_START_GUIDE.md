# G2 Fix Plan - Quick Start Guide

**5-Minute Overview | Action-Oriented | Get Started Fast**

---

## What You Need to Know

**Problem:** 30 G2 skills have dependency issues (broken references, missing bridges, redundancies)

**Solution:** This fix plan provides everything needed to correct all 30 issues

**Time:** 4-5 hours total implementation

**Files:** You'll work in `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

---

## Start Here

### If you have 5 minutes:
→ Read this document (you are here)

### If you have 15 minutes:
→ Read: **G2_EXECUTIVE_SUMMARY.md**

### If you have 30 minutes:
→ Read: Executive Summary + browse **G2_FIX_SUMMARY_TABLE.md**

### If you're ready to implement:
→ Use: **G2_IMPLEMENTATION_CHECKLIST.md** (work through items 1-30)

### If you need to understand WHY:
→ Study: **G2_FIX_PLAN.md** (full rationales for each fix)

### If you want visuals:
→ See: **G2_DEPENDENCY_CHAINS_VISUAL.md** (before/after diagrams)

---

## The 4 Critical Fixes (Do These First)

**Time: 30 minutes | Priority: CRITICAL**

These are BROKEN references that must be fixed immediately:

### 1. T13.G2.03
```diff
- * T13.G2.01: Spot what doesn't belong in a pattern  ❌ WRONG
+ * T04.G2.01: Identify the repeating unit in a longer pattern
+ * T01.G2.01: Find actions that repeat in everyday tasks
```

### 2. T13.G2.04
```diff
- * T13.G2.03: Fix the wrong step in a simple task  ❌ WRONG
+ * T01.G1.09: Match an algorithm to its goal
  * T03.G1.03: List steps for a simple classroom routine  ✓ KEEP
```

### 3. T20.G2.03
```diff
- * T20.G2.01: Identify win and lose in a simple game  ❌ WRONG
+ * T20.G2.01: Use repeat cards in an art recipe
+ * T01.G2.02: Use "repeat" to make directions shorter
```

### 4. T23.G2.02
```diff
- * T23.G2.01: Match a color to a feeling  ❌ WRONG
+ * T23.G2.01: Pick the right sensor for a job  ✓ CORRECT
```

**After these 4:** Validate with:
```bash
grep -E "Spot what doesn't belong|Fix the wrong step|win and lose|color to a feeling" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
```
Should return: **0 results**

---

## The Pattern (For Next 17 Fixes)

**Problem:** G2 skills jump directly to GK (Kindergarten), skipping G1

**Solution:** Replace GK dependency with G1 bridge skill

**Example:**
```diff
Current (BAD):
  T01.G2.01: Find actions that repeat
  └─ T01.GK.07: Find the pattern that repeats  ⚠️ SKIPS G1

Fixed (GOOD):
  T01.G2.01: Find actions that repeat
  └─ T04.G1.03: Find repeated steps in instruction list  ✓ G1 BRIDGE
      └─ T01.GK.07: Find the pattern that repeats (transitively)
```

---

## Common Replacements

| Remove This GK | Replace With G1 Bridge | Topic |
|----------------|------------------------|-------|
| T01.GK.07: Find pattern | T04.G1.03: Find repeated steps | Patterns |
| T01.GK.08: Count times | T25/26/27.G1.XX (varies) | Data |
| T01.GK.05: Move picture | T12.G1.02 or T01.G1.06 | Org/Debug |
| T04.GK.01: Spot pattern | T23.G1.03: Choose sensor | Sensors |

---

## File Locations

**Target file to edit:**
```
/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
```

**Documentation:**
```
/media/binyu/USB2/dev/CreatiCodeSkillMap/
├── G2_EXECUTIVE_SUMMARY.md           ← Overview & metrics
├── G2_FIX_PLAN.md                    ← Full detailed plan
├── G2_FIX_SUMMARY_TABLE.md           ← Quick lookup tables
├── G2_IMPLEMENTATION_CHECKLIST.md    ← Step-by-step (USE THIS)
├── G2_DEPENDENCY_CHAINS_VISUAL.md    ← Visual diagrams
├── G2_FIX_PLAN_README.md             ← Documentation guide
└── G2_QUICK_START_GUIDE.md           ← This file
```

---

## Workflow

### Step 1: Open files
```bash
cd /media/binyu/USB2/dev/CreatiCodeSkillMap

# Open checklist in editor
nano G2_IMPLEMENTATION_CHECKLIST.md

# Open target file in another terminal/editor
nano skillsv4/allskills.md
```

### Step 2: Find skill
```bash
# Example: Find T13.G2.03
grep -A 10 "^ID: T13.G2.03" skillsv4/allskills.md
```

### Step 3: Make change
- Locate "Dependencies:" section
- Replace old text with new text (from checklist)
- Save file

### Step 4: Check off in checklist
Mark item as complete: `[x]`

### Step 5: Validate periodically
After every 5-10 fixes, run validation queries

### Step 6: Final validation
After all 30 fixes, run complete validation suite

---

## Validation Queries

**Quick check during implementation:**
```bash
cd /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4

# Count remaining G2→GK.07 dependencies (should decrease)
grep -B 5 "T01.GK.07" allskills.md | grep "^ID: .*\.G2\." | wc -l

# Count remaining G2→GK.08 dependencies (should decrease)
grep -B 5 "T01.GK.08" allskills.md | grep "^ID: .*\.G2\." | wc -l
```

**Full validation (at end):**
See Phase 4 in G2_IMPLEMENTATION_CHECKLIST.md

---

## Tips & Tricks

### Finding a skill quickly
```bash
# By ID
grep -A 10 "^ID: T13.G2.03" allskills.md

# By name (partial)
grep -B 2 "Fix a repeated step" allskills.md
```

### Seeing current dependencies
```bash
# Show skill + dependencies
grep -A 15 "^ID: T13.G2.03" allskills.md | grep -E "^ID:|^Dependencies:|^\\*"
```

### Checking your work
```bash
# After editing T13.G2.03, verify:
grep -A 12 "^ID: T13.G2.03" allskills.md
```

### Before/after comparison
```bash
# Make a backup first
cp skillsv4/allskills.md skillsv4/allskills.md.backup

# After fixes, compare
diff skillsv4/allskills.md.backup skillsv4/allskills.md
```

---

## Estimated Time per Phase

| Phase | Fixes | Time | Priority |
|-------|-------|------|----------|
| 1: Broken References | 4 | 30 min | CRITICAL |
| 2: GK Bridges | 17 | 2-3 hrs | HIGH |
| 3: Redundancies | 9 | 1 hr | MEDIUM |
| 4: Validation | - | 30 min | CRITICAL |
| **TOTAL** | **30** | **4-5 hrs** | - |

---

## Success Looks Like

**Before (problems):**
```
T01.G2.01: Find actions that repeat
├─ T01.G1.10: Match "if/then" rules  ❌ Unrelated
└─ T01.GK.07: Find pattern           ⚠️ Skips G1
```

**After (fixed):**
```
T01.G2.01: Find actions that repeat
└─ T04.G1.03: Find repeated steps    ✓ Proper G1 bridge
    └─ T01.GK.07: Find pattern       ✓ Transitively included
```

---

## When You're Stuck

**Q: Can't find the skill in allskills.md?**
```bash
grep -n "T13.G2.03" allskills.md  # Shows line number
```

**Q: Current dependencies don't match checklist?**
- File may have been updated
- Check actual current state
- Adapt fix accordingly
- Note in checklist

**Q: Proposed bridge skill doesn't exist?**
- Search to confirm: `grep "T04.G1.03" allskills.md`
- If missing, check G2_FIX_PLAN.md for alternatives
- Document substitution

**Q: Breaking something?**
- You have a backup: `allskills.md.backup`
- Restore: `cp allskills.md.backup allskills.md`
- Try again

---

## Three Ways to Use This Plan

### 1. Quick Fix (1 hour)
- Fix only the 4 broken references (Phase 1)
- Validates clean
- Stops the bleeding

### 2. High Priority (3 hours)
- Fix broken references (Phase 1)
- Fix GK bridges (Phase 2)
- Significantly improves structure

### 3. Complete (5 hours)
- All phases
- All 30 skills fixed
- Clean, optimal state

**Recommendation:** Go for Complete (5 hours)
- It's only 2 more hours than High Priority
- Sets foundation for G3-G8 fixes
- One-and-done for G2

---

## Phase Order (Recommended)

1. **Critical** (30 min): Items 1-4 in checklist
2. **BREAK** (5 min): Validate Phase 1
3. **High-A** (1 hr): Items 5-12 (pattern/sequencing)
4. **BREAK** (5 min): Quick validation
5. **High-B** (1.5 hrs): Items 13-21 (data skills)
6. **BREAK** (5 min): Quick validation
7. **Medium** (1 hr): Items 22-26 (redundancies)
8. **Final** (30 min): Complete validation

Total: 4.5 hours + 20 min breaks = ~5 hours

---

## Your Action Plan (Right Now)

### Next 10 minutes:
1. [ ] Read this Quick Start Guide (done!)
2. [ ] Skim G2_EXECUTIVE_SUMMARY.md
3. [ ] Open G2_IMPLEMENTATION_CHECKLIST.md

### Next 30 minutes:
4. [ ] Make backup: `cp skillsv4/allskills.md skillsv4/allskills.md.backup`
5. [ ] Fix items 1-4 (broken references)
6. [ ] Validate Phase 1

### Next 3 hours:
7. [ ] Fix items 5-21 (GK bridges)
8. [ ] Validate periodically

### Final 1.5 hours:
9. [ ] Fix items 22-26 (redundancies)
10. [ ] Run complete validation
11. [ ] Celebrate!

---

## Ready to Start?

**Go to:** G2_IMPLEMENTATION_CHECKLIST.md

**Start with:** Item 1 (T13.G2.03)

**Remember:**
- Make a backup first
- Work systematically through checklist
- Validate periodically
- Take breaks
- You've got this!

---

**Good luck!**

Need more detail on any fix? See G2_FIX_PLAN.md for full rationales.

---

**END OF QUICK START GUIDE**
