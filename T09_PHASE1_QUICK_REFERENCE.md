# T09 Phase 1 Optimization - Quick Reference

## AT A GLANCE

**Status:** 🟢 GOOD - Minor fixes needed
**Total Skills:** 59 (K:2, G1:2, G2:2, G3:6, G4:10, G5:9, G6:10, G7:7, G8:9)
**Issues Found:** 12 total (3 HIGH, 5 MEDIUM, 4 LOW)
**Estimated Fix Time:** 2-3 hours for all high-priority issues

---

## 🔴 HIGH PRIORITY FIXES (Must Do)

| ID | Issue | Fix Required | Impact |
|---|---|---|---|
| **H1** | G3.01.03 & G3.02 overlap | Merge or clarify distinction | Reduces redundancy |
| **H2** | G5.06 redundant dependency | Remove G3.05 from dependencies | Cleaner graph |
| **H3** | Missing variable-to-variable pattern | Add new G3.06 skill | Fills scaffolding gap |

**Action:** Fix these before production release

---

## 🟡 MEDIUM PRIORITY FIXES (Should Do)

| ID | Issue | Fix Required | Complexity |
|---|---|---|---|
| **M1** | G4.08 isolated from progression | Add G4.01 dependency | Simple |
| **M2** | G5.04 description vague | Rewrite description | Simple |
| **M3** | G6.02 redundant dependency | Remove G5.01 from deps | Simple |
| **M4** | G7.03 possible T08 overlap | Verify T08, rewrite/relocate | **Requires T08 review** |
| **M5** | G6 has 10 skills | Consider moving 1-2 to G7 | Optional |

**Action:** Address after high-priority fixes, before final review

---

## 🔵 LOW PRIORITY ENHANCEMENTS (Nice to Have)

| ID | Issue | Type | Notes |
|---|---|---|---|
| **L1** | G3.01.01-04 naming | Observation | No fix needed |
| **L2** | List/variable integration | Coverage check | **Requires T10 coordination** |
| **L3** | G6.06.01 assessability | Description quality | Optional enhancement |
| **L4** | G8.05 has 3 dependencies | Review necessity | May be justified |

**Action:** Consider during quality review phase

---

## SPECIFIC FIXES DETAIL

### H1: G3.01.03 / G3.02 Overlap
**Current State:**
- G3.01.03: "Change a variable value by 1 using the change block"
- G3.02: "Use change and reduce blocks to modify a variable"

**Recommended Fix:**
```
DELETE: T09.G3.01.03
MERGE INTO: T09.G3.01.04 (rename to "Change and display variable value")
UPDATE: T09.G3.02 description to emphasize "any amount" and "reduce"
```

### H2: G5.06 Redundant Dependency
**Current State:**
```
T09.G5.06 depends on:
- T09.G3.05 ← REMOVE THIS
- T09.G4.05 ← KEEP THIS
```

**Fix:** Remove T09.G3.05 (redundant through G4.05)

### H3: Missing Variable-to-Variable Assignment
**Add New Skill:**
```
ID: T09.G3.06
Skill: Copy a value from one variable to another
Description: Students use "set [var1] to (var2)" to copy values.
Dependencies: T09.G3.01.04
Insert After: T09.G3.05
Update: Add as dependency to T09.G5.08
```

---

## COORDINATION CHECKLIST

- [ ] **Verify T08 coverage** of AND/OR/NOT operators (affects M4)
- [ ] **Review T10** for list indexing with variables (affects L2)
- [ ] **Check cross-references** if G3.01.03 is deleted (affects H1)
- [ ] **Update skill count** in documentation after fixes

---

## DEPENDENCY CHANGES SUMMARY

### Changes to Make:
1. T09.G5.06: Remove T09.G3.05 dependency
2. T09.G4.08: Add T09.G4.01 dependency
3. T09.G6.02: Remove T09.G5.01 dependency
4. T09.G5.08: Add T09.G3.06 dependency (after creating new skill)
5. T09.G8.05: Consider removing T09.G7.03 dependency

### Affected by H1 (if G3.01.03 deleted):
- All dependencies pointing to T09.G3.01.03 must redirect to T09.G3.01.04
- Check: T09.G3.01.04, T09.G3.02 (and any cross-topic references)

---

## SKILL QUALITY CHECKLIST

✅ K-2 picture-based (no coding)
✅ G3+ block-based coding
✅ No X-2 violations
✅ No forward dependencies
✅ Clear progression K-8
⚠️ Minor overlap (H1)
⚠️ Some redundant deps (H2, M3)
⚠️ One scaffolding gap (H3)

---

## IMPLEMENTATION ORDER

### Step 1: Analysis Phase (Complete)
- [x] Review all 59 skills
- [x] Check dependencies
- [x] Verify K-2 compliance
- [x] Identify issues

### Step 2: High Priority Fixes
- [ ] H1: Resolve G3.01.03/G3.02 overlap
- [ ] H2: Clean up G5.06 dependencies
- [ ] H3: Add G3.06 variable-to-variable skill

### Step 3: Medium Priority Fixes
- [ ] M1: Fix G4.08 dependencies
- [ ] M2: Rewrite G5.04 description
- [ ] M3: Clean up G6.02 dependencies
- [ ] M4: Coordinate with T08 (verify overlap)
- [ ] M5: Review G6 skill density

### Step 4: Low Priority (Optional)
- [ ] L2: Coordinate with T10
- [ ] L3: Enhance G6.06.01 description
- [ ] L4: Review G8.05 dependencies

### Step 5: Validation
- [ ] Verify all dependency changes
- [ ] Check cross-topic references
- [ ] Update skill counts
- [ ] Generate final summary

---

## NOTES

- **Previous Work:** T09 already optimized from 35→59 skills (major work done)
- **Current Status:** Refinement phase, not major restructuring
- **Risk Level:** LOW - changes are incremental improvements
- **Breaking Changes:** Only if H1 deletes G3.01.03 (check references)

---

## QUICK DECISION GUIDE

**Should I fix this now?**
- HIGH (H1-H3): YES - required for quality
- MEDIUM (M1-M5): DEPENDS - coordinate with other topics first
- LOW (L1-L4): NO - enhancement only

**Can I release without fixing?**
- HIGH issues: NO - fix first
- MEDIUM issues: MAYBE - with workarounds
- LOW issues: YES - nice-to-have only

**What needs coordination?**
- M4: Requires T08 analysis
- L2: Requires T10 analysis
- All others: Self-contained within T09

---

## SUCCESS CRITERIA

T09 optimization is COMPLETE when:
- ✅ All HIGH priority issues resolved (H1-H3)
- ✅ No X-2 violations
- ✅ No forward dependencies
- ✅ K-2 skills picture-based
- ✅ Comprehensive CreatiCode coverage
- ⚠️ MEDIUM/LOW issues documented for future work

**Target:** Production-ready after HIGH fixes, excellent after MEDIUM fixes
