# G2 Skills Dependency Fix Plan - Executive Summary

**Date:** 2025-11-20
**Scope:** Grade 2 (G2) skills in /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Total Fixes Required:** 30 skills

---

## Problem Statement

Analysis of G2 skill dependencies revealed three major categories of issues:

1. **Broken References (4 skills):** Dependencies referencing non-existent or misnamed skills
2. **Missing G1 Bridges (17 skills):** G2 skills jumping directly to GK (Kindergarten) level, skipping G1
3. **Transitive Redundancies (9 skills):** Dependencies already covered through other dependency paths

**Total Impact:** 30 skills (approximately 30% of all G2 skills) require dependency corrections.

---

## Critical Issues (Must Fix)

### 1. Broken Dependency References

| Skill ID | Broken Reference | Actual Skill |
|----------|-----------------|--------------|
| T13.G2.03 | References: "Spot what doesn't belong in a pattern" | T13.G2.01 is actually: "Fix steps that use the wrong signal" |
| T13.G2.04 | References: "Fix the wrong step in a simple task" | T13.G2.03 is actually: "Fix repeated step (wrong count)" |
| T20.G2.03 | References: "Identify win and lose in a simple game" | T20.G2.01 is actually: "Use repeat cards in an art recipe" |
| T23.G2.02 | References: "Match a color to a feeling" | T23.G2.01 is actually: "Pick the right sensor for a job" |

**Impact:** These cause immediate confusion and break learning progressions.
**Priority:** CRITICAL - Fix first

---

### 2. G2→GK Dependencies (Skipping G1 Bridge)

**Problem:** 17 G2 skills depend directly on Kindergarten (GK) skills, skipping the Grade 1 (G1) bridge level.

**Most Common Offenders:**
- **T01.GK.07** "Find the pattern that repeats" - referenced by 10 G2 skills
- **T01.GK.08** "Count how many times" - referenced by 9 G2 skills
- **T01.GK.05** "Move the picture that's in the wrong place" - referenced by 2 skills
- **T04.GK.01** "Spot a simple repeating pattern" - referenced by 1 skill

**Solution:** Replace with appropriate G1 bridge skills:
- T04.G1.03: "Find repeated steps in an instruction list" (bridges T01.GK.07)
- T12.G1.02: "Give a clear title to a set of steps" (bridges organization skills)
- T01.G1.06: "Fix a routine with one wrong step" (bridges debugging skills)
- T23.G1.03: "Choose what a sensor can notice" (bridges sensor skills)
- Topic-specific G1 skills for data/analysis topics (T25-T28)

**Impact:** Improves learning progression, ensures proper skill scaffolding.
**Priority:** HIGH - Fix after broken references

---

### 3. Transitive Redundancies

**Problem:** 9 G2 skills list dependencies that are already covered through other dependency paths.

**Example:**
```
T03.G2.02 currently depends on:
  - T03.G2.01 (direct prerequisite)
  - T03.G1.03 (redundant - already covered through T03.G2.01 → T03.G1.03)
```

**Solution:** Remove the redundant dependency, keep only the direct path.

**Impact:** Cleaner dependency graphs, easier to understand learning paths.
**Priority:** MEDIUM - Fix after bridge corrections

---

## Fix Summary by Category

### High Priority (21 skills)

**Broken References (4 skills):**
- T13.G2.03, T13.G2.04, T20.G2.03, T23.G2.02

**Pattern/Sequencing Bridges (8 skills):**
- T01.G2.01, T01.G2.02, T01.G2.08
- T04.G2.02, T04.G2.04
- T12.G2.02, T13.G2.01, T23.G2.01

**Data Skills Bridges (9 skills):**
- T25: T25.G2.02, T25.G2.03, T25.G2.04
- T26: T26.G2.02, T26.G2.04
- T27: T27.G2.02, T27.G2.04
- T28: T28.G2.02, T28.G2.04

### Medium Priority (9 skills)

**Transitive Redundancies:**
- T03.G2.02, T05.G2.02
- T14.G2.02, T14.G2.04
- T20.G2.04

---

## Expected Outcomes

### Before Fixes
- ❌ 4 broken references causing confusion
- ❌ 17 G2→GK jumps skipping G1 level
- ❌ 9 redundant dependencies cluttering graphs
- ❌ Cross-topic dependencies (e.g., data skills depending on pattern skills)

### After Fixes
- ✅ All skill references valid and accurate
- ✅ Clean GK→G1→G2 progression for all skills
- ✅ Minimal, essential-only dependencies
- ✅ Topic-consistent dependencies (data skills depend on data foundations)

### Benefits
1. **Clearer Learning Progressions:** Students advance through proper skill levels
2. **Better Topic Coherence:** Skills build on relevant foundations within their topic
3. **Easier Maintenance:** Dependency graphs are simpler and more logical
4. **Foundation for Higher Grades:** Sets precedent for clean G3-G8 dependencies

---

## Implementation Plan

### Phase 1: Critical (30 minutes)
Fix 4 broken references:
- T13.G2.03, T13.G2.04, T20.G2.03, T23.G2.02

### Phase 2: High Priority (2-3 hours)
Fix 17 G2→GK bridge issues:
- Pattern/sequencing skills (8 skills)
- Data/analysis skills (9 skills)

### Phase 3: Medium Priority (1 hour)
Remove 9 transitive redundancies

### Phase 4: Validation (30 minutes)
Run validation queries to ensure:
- No broken references
- No G2→GK jumps
- All new G1 bridges in place
- No circular dependencies

**Total Time Estimate:** 4-5 hours

---

## Key Metrics

| Metric | Value |
|--------|-------|
| Total G2 skills requiring fixes | 30 |
| Broken references to fix | 4 |
| GK dependencies to replace | 17 |
| Transitive redundancies to remove | 9 |
| New G1 bridge skills introduced | 12 unique |
| Estimated implementation time | 4-5 hours |

---

## Validation Criteria

Fix plan is complete when:

1. ✅ Zero G2 skills with broken dependency references
2. ✅ Zero or minimal G2→GK direct dependencies (all properly bridged through G1)
3. ✅ All transitive redundancies removed
4. ✅ Validation queries pass with 0 errors
5. ✅ Dependency graphs show logical progressions

---

## Documentation Suite

Complete documentation available in 5 files:

1. **G2_FIX_PLAN_README.md** - Guide to all documentation (you are here)
2. **G2_FIX_PLAN.md** - Full detailed plan with rationales (25KB)
3. **G2_FIX_SUMMARY_TABLE.md** - Quick reference tables (7.6KB)
4. **G2_IMPLEMENTATION_CHECKLIST.md** - Step-by-step checklist (9.7KB)
5. **G2_DEPENDENCY_CHAINS_VISUAL.md** - Visual before/after comparisons (14KB)

---

## Recommended Next Steps

1. **Immediate:** Review and approve this fix plan
2. **Phase 1:** Implement critical broken reference fixes (30 min)
3. **Phase 2:** Implement high-priority bridge fixes (2-3 hours)
4. **Phase 3:** Implement medium-priority redundancy removals (1 hour)
5. **Phase 4:** Validate all fixes (30 min)
6. **Follow-up:** Apply same methodology to G3-G8 skills

---

## Risk Assessment

**Low Risk:**
- All proposed changes are well-documented
- Each change has clear rationale
- Changes follow consistent patterns
- Validation queries will catch errors

**Mitigation:**
- Use implementation checklist for systematic approach
- Validate after each phase
- Keep backup of original file
- Test dependency analysis tools after each phase

---

## Approval & Sign-off

**Prepared by:** Claude Code Analysis
**Date:** 2025-11-20
**Review Status:** Ready for implementation

**Recommended Approvers:**
- [ ] Curriculum Lead
- [ ] Technical Lead
- [ ] Quality Assurance

**Implementation Authorization:**
- [ ] Approved to proceed with Phase 1 (Critical)
- [ ] Approved to proceed with Phase 2 (High Priority)
- [ ] Approved to proceed with Phase 3 (Medium Priority)

---

## Quick Links

- **Full Plan:** G2_FIX_PLAN.md
- **Quick Reference:** G2_FIX_SUMMARY_TABLE.md
- **Implementation Guide:** G2_IMPLEMENTATION_CHECKLIST.md
- **Visual Guide:** G2_DEPENDENCY_CHAINS_VISUAL.md
- **Documentation Index:** G2_FIX_PLAN_README.md

---

**Questions?** Refer to G2_FIX_PLAN_README.md for complete documentation guide.

---

**END OF EXECUTIVE SUMMARY**
