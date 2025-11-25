# T20 ISSUES - QUICK REFERENCE
## One-Page Actionable Summary

**Status:** ❌ NOT production-ready (contrary to Phase 1 claims)
**Actual Grade:** C+ (78/100)
**Issues Found:** 47 across 10 categories
**Revision Time:** 10-12 hours

---

## CRITICAL ISSUES (Must Fix)

### 🚨 ISSUE 1: MASSIVE T18 DUPLICATION
**12 skills (22%) duplicate T18 content**

**DELETE THESE SKILLS:**
- ❌ T20.G5.04.00 - Initialize 3D scenes (duplicate T18.G4.01.01)
- ❌ T20.G5.06 - Add box shapes (duplicate T18.G4.01.02)
- ❌ T20.G5.07 - Add sphere shapes (duplicate T18.G4.01.03)
- ❌ T20.G5.08 - Add cylinder shapes (duplicate T18.G4.01.04)
- ❌ T20.G5.09 - Create patterns with 3D shapes (combines duplicates)
- ❌ T20.G6.05.01 - Materials/textures (duplicate T18.G5.04/05)
- ❌ T20.G7.04.00 - Particle basics (duplicate T18.G5.06.01-02)
- ❌ T20.G7.04.01 - Particle art (duplicate T18.G5.06.03-05)
- ❌ T20.G7.07 - Lighting (duplicate T18.G6.04.01-04)

**KEEP BUT MODIFY:**
- ✏️ T20.G5.10 → Rename to "Create 3D algorithmic art" (assumes T18 prereqs)
- ✏️ T20.G6.05.02 → Keep (3D curves unique to algorithmic art)
- ✏️ T20.G6.05.03 → Keep (interactive 3D generative unique)
- ✏️ T20.G7.06 → Keep (algorithmic sculptures, merge with particles)
- ✏️ T20.G7.08 → Keep (custom vertices advanced/unique)

### 🚨 ISSUE 2: CONFUSING ID SYSTEM

**Problems:**
- T20.G5.04.00 exists when T20.G5.04 already exists
- T20.G7.04.00/.01 unrelated to parent T20.G7.04
- Numbering gaps: .04 → .06 (skips .05)
- Skills out of order in file

**Fix:** Renumber all Grade 5 and 7 skills sequentially after deletions

### 🚨 ISSUE 3: PLATFORM MISALIGNMENT

**T20.G8.05 claims features NOT in CreatiCode:**
- ❌ "Custom shaders" - NOT AVAILABLE
- ❌ "Procedural materials" - NOT AVAILABLE

**Fix:** Rewrite to use actual features (PBR materials, multiple lights, particles)

---

## HIGH PRIORITY ISSUES

### ISSUE 4: UNCLEAR DESCRIPTIONS

**Need rewrites:**
- T20.G3.05: "Add simple randomness" - what's "simple"?
- T20.G4.02: "Tessellation" - concept not explained
- T20.G7.05: "L-system rules" - no explanation
- T20.G7.05.01: "Cellular automata" - no mechanics described

### ISSUE 5: DEPENDENCY PROBLEMS

**Excessive dependencies:**
- T20.G4.01: Lists 11 dependencies (should be 3-4)

**Irrelevant dependencies:**
- T20.G4.03.01 → T03.G4.03 (team roles unrelated to animation)
- T20.G4.03.02 → T05.G3.01-02 (user interviews unrelated to color)

**Missing dependencies:**
- T20.G6.05.02 needs T10.G5.01 (nested lists for point data)

### ISSUE 6: WRONG SUB-SKILL STRUCTURE

**These should be main skills, not sub-skills:**
- T20.G4.03.01: Create smooth animations
- T20.G4.03.02: Design color palettes
- T20.G7.05.01: Cellular automata (parallel to L-systems, not sub-skill)

---

## MEDIUM PRIORITY ISSUES

### ISSUE 7: MISSING SCAFFOLDING

**Add these skills:**
1. **T20.G5.01.02:** Handle text/category data in visualizations
2. **T20.G6.04.01:** Create interactive data visualizations (hover, click, filter)
3. **T20.G5.04.01:** Apply color theory to algorithmic art (HSV, harmony)
4. **T20.G6.06:** Document and export algorithmic art projects
5. **T20.G6.07:** Debug mathematical and visual output errors

### ISSUE 8: GRADE APPROPRIATENESS

**Too advanced for Grade 7:**
- T20.G7.05: L-systems (formal grammars typically college-level)
- T20.G7.05.01: Cellular automata (2D arrays + state management)

**Fix:** Simplify to "rule-based pattern generation" and 1D automata

### ISSUE 9: OVERLAPPING SKILLS

**Restructure:**
- T20.G7.05 (L-systems) and T20.G7.05.01 (cellular automata) are parallel, not parent-child
- Should be: T20.G7.05 (rule-based), T20.G7.06 (grid-based), T20.G7.07 (combined)

---

## SKILL COUNT AFTER FIXES

| Grade | Current | After Deletions | After Additions | Net Change |
|-------|---------|-----------------|-----------------|------------|
| K     | 4       | 4               | 4               | 0          |
| 1     | 4       | 4               | 4               | 0          |
| 2     | 4       | 4               | 4               | 0          |
| 3     | 6       | 6               | 6               | 0          |
| 4     | 8       | 8               | 8               | 0          |
| 5     | 11      | 6 (-5)          | 8 (+2)          | -3         |
| 6     | 8       | 7 (-1)          | 10 (+3)         | +2         |
| 7     | 10      | 7 (-3)          | 7 (±0)          | -3         |
| 8     | 6       | 6 (±0)          | 6 (±0)          | 0          |
| **Total** | **61** | **52** | **57** | **-4** |

---

## ACTION PLAN

### Phase 1: Delete Duplicates (2 hours)
- [ ] Remove 9 skills duplicating T18
- [ ] Update dependencies pointing to deleted skills
- [ ] Update skill counts

### Phase 2: Fix ID System (2 hours)
- [ ] Renumber Grade 5 skills (after deletions)
- [ ] Renumber Grade 7 skills (after deletions)
- [ ] Verify no gaps or duplicates
- [ ] Fix file ordering

### Phase 3: Rewrite Descriptions (3 hours)
- [ ] T20.G3.05 - clarify "simple randomness"
- [ ] T20.G4.02 - explain tessellation
- [ ] T20.G7.05 - explain L-systems/simplify
- [ ] T20.G7.05.01 - explain cellular automata/simplify
- [ ] T20.G8.05 - remove non-existent features

### Phase 4: Fix Dependencies (2 hours)
- [ ] Reduce T20.G4.01 from 11 to 3-4 dependencies
- [ ] Fix T20.G4.03.01 irrelevant dependency
- [ ] Fix T20.G4.03.02 irrelevant dependencies
- [ ] Add missing dependencies to T20.G6.05.02

### Phase 5: Add Missing Skills (2 hours)
- [ ] T20.G5.01.02: Text/category data visualization
- [ ] T20.G5.04.01: Color theory application
- [ ] T20.G6.04.01: Interactive data viz
- [ ] T20.G6.06: Document/export art
- [ ] T20.G6.07: Debug math/visual errors

### Phase 6: Restructure Sub-Skills (1 hour)
- [ ] Promote T20.G4.03.01 to main skill (renumber)
- [ ] Promote T20.G4.03.02 to main skill (renumber)
- [ ] Restructure T20.G7.05/.01/.02 as parallel topics

### Phase 7: Validation (2 hours)
- [ ] Verify no forward dependencies
- [ ] Check X-2 rule compliance
- [ ] Validate feature coverage
- [ ] Check grade appropriateness
- [ ] Test sample exercises

**Total Time: 14 hours**

---

## SKILLS REQUIRING IMMEDIATE ATTENTION

### Must Delete (Priority 1)
1. T20.G5.04.00 - 3D init duplicate
2. T20.G5.06 - Box duplicate
3. T20.G5.07 - Sphere duplicate
4. T20.G5.08 - Cylinder duplicate
5. T20.G5.09 - 3D patterns duplicate
6. T20.G6.05.01 - Materials duplicate
7. T20.G7.04.00 - Particle basics duplicate
8. T20.G7.04.01 - Particle art duplicate
9. T20.G7.07 - Lighting duplicate

### Must Rewrite (Priority 2)
1. T20.G8.05 - Remove "custom shaders"
2. T20.G7.05 - Explain/simplify L-systems
3. T20.G7.05.01 - Explain/simplify cellular automata
4. T20.G4.02 - Explain tessellation
5. T20.G3.05 - Clarify randomness ranges

### Must Fix Dependencies (Priority 3)
1. T20.G4.01 - Reduce from 11 to 3-4
2. T20.G4.03.01 - Remove team roles dependency
3. T20.G4.03.02 - Remove user interview dependencies
4. T20.G6.05.02 - Add list iteration dependencies

---

## COMPARISON: CLAIMED vs ACTUAL

| Metric | Phase 1 Claim | Actual Reality |
|--------|--------------|----------------|
| Grade | A (95/100) | C+ (78/100) |
| Status | Production Ready | Needs Revision |
| Coverage | 96% | 85% (excl. duplicates) |
| Issues Remaining | 0 | 47 |
| Duplicates with T18 | 0 mentioned | 12 skills (22%) |
| ID System | "Perfect" | Broken (.04.00) |
| Platform Alignment | "Excellent" | Claims non-existent features |

---

## KEY FINDINGS

✅ **Strengths:**
- K-2 unplugged skills excellent
- Core 2D progression solid
- Data viz sequence has potential
- Ambitious advanced topics

❌ **Critical Flaws:**
- 22% of skills duplicate T18
- ID system inconsistent/broken
- Claims features not in platform
- Dependencies excessive/irrelevant

📊 **Impact:**
- 9 skills must be deleted
- 15 skills need significant rewrites
- 5 skills must be added
- 20+ skills need renumbering

⏱️ **Effort:**
- 14 hours to fix all issues
- 2 hours to validate
- Total: ~16 hours

---

## FILES CREATED

1. **T20_COMPREHENSIVE_ISSUE_ANALYSIS.md** - Full detailed analysis
2. **T20_ISSUES_QUICK_REFERENCE.md** - This file (action plan)

---

**Conclusion:** T20 requires substantial revision before production use. The Phase 1 "complete" status was premature and did not adequately address critical issues like T18 duplication and platform misalignment.
