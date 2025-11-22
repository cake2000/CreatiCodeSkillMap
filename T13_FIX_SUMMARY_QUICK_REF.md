# T13 Fix Plan - Quick Reference

## Overview
**Total Skills**: 44 → 48 (+4 new)
**Critical Fixes**: 5
**Improvements**: 12
**New Skills**: 4

---

## Critical Fixes (DO IMMEDIATELY)

### 1. T13.G5.05 - Fix Dependency Title
**Change**: Update dependency from "Debug a loop containing a conditional" to "Debug complex two-level nested structures"

### 2. T13.G3.01b → T13.G3.01.02
**Change**: Rename for consistency with decimal notation
**Cascade**: Update T13.G3.05 dependency reference

### 3. Move T13.G4.07 → T13.G5.06
**Reason**: Rebalance Grade 4 (9→8 skills) and Grade 5 (5→9 skills)
**Cascade**:
- Renumber T13.G4.08 → T13.G4.07
- Renumber T13.G4.09 → T13.G4.08
- Update T13.G5.05 dependency

### 4. Add T13.G5.09 - Error Message Interpretation
**Gap**: No skill teaches reading error indicators
**Placement**: Grade 5 (bridges logging and systematic debugging)

### 5. CreatiCode Accuracy Check
**Status**: ✅ Current skills correctly reference actual features
- say blocks ✅
- variable monitors ✅
- widget labels ✅
**Not Referenced** (correctly): Debug Mode, 3D inspector, breakpoints

---

## Skill Count by Grade (After Fixes)

| Grade | Before | After | Change |
|-------|--------|-------|--------|
| K     | 3      | 3     | -      |
| 1     | 4      | 4     | -      |
| 2     | 4      | 4     | -      |
| 3     | 6      | 6     | -      |
| **4** | **9**  | **8** | **-1** (moved to G5) |
| **5** | **5**  | **9** | **+4** (1 moved from G4, 3 new) |
| 6     | 4      | 5     | +1 (new) |
| 7     | 5      | 6     | +1 (new) |
| 8     | 4      | 5     | +1 (new) |
| **Total** | **44** | **48** | **+4** |

---

## New Skills Summary

### T13.G5.09 - Read and interpret error indicators
**Why**: Students need to recognize error signals before debugging
**Teaches**: Red/orange blocks, unexpected behavior, frozen scripts

### T13.G5.10 - Debug with limited changes allowed
**Why**: Develops precision and minimal fixes
**Teaches**: Fix by changing only numbers OR only reordering

### T13.G6.05 - Debug a peer's program
**Why**: Collaborative debugging missing from progression
**Teaches**: Systematic observation, hypothesis sharing, guiding peers

### T13.G7.06 - Context-dependent bugs
**Why**: Important for multiplayer and state-dependent issues
**Teaches**: Different starting positions, player counts, initial values

### T13.G8.05 - Error propagation through custom blocks
**Why**: Understanding call stacks and error flow
**Teaches**: Tracing errors through nested custom blocks

---

## Key Improvements

### Made More Specific:
- **T13.G3.01**: Added "written expectation" for comparison
- **T13.G4.02**: Concrete edge case examples (x=240, y=180, timer=0)
- **T13.G4.05.01**: 3-column test template specified
- **T13.G5.03**: 8-10 test cases across 3 categories (vs G4's 3-5 total)

### Made More Systematic:
- **T13.G6.02**: 4-step debugging process numbered
- **T13.G6.03**: Test matrix with 5 values per variable
- **T13.G7.01**: 10-15 test cases with coverage percentage
- **T13.G8.04**: 4-question review framework

### Made More Accurate (CreatiCode):
- **T13.G5.01**: Explicitly lists say blocks, monitors, widgets
- **T13.G7.05**: 5 defensive patterns with examples

---

## Renumbering Map

```
OLD ID        → NEW ID        Reason
─────────────────────────────────────────
T13.G3.01b    → T13.G3.01.02  Consistency
T13.G4.07     → T13.G5.06     Rebalance
T13.G4.08     → T13.G4.07     Shift up
T13.G4.09     → T13.G4.08     Shift up
              → T13.G5.09     NEW
              → T13.G5.10     NEW
              → T13.G6.05     NEW
              → T13.G7.06     NEW
              → T13.G8.05     NEW
```

---

## Dependency Updates Required

1. **T13.G3.05**: Change `T13.G3.01b` → `T13.G3.01.02`
2. **T13.G5.05**: Change dependency title to match actual skill
3. **T13.G5.05**: Change `T13.G4.07` → `T13.G5.06`
4. **All references to T13.G4.08**: Update to `T13.G4.07`
5. **All references to T13.G4.09**: Update to `T13.G4.08`

---

## Validation Checklist

- [x] T08.G5.01 exists (verified - multiple G7 skills depend on it)
- [x] All cross-topic dependencies preserved (T01, T03, T04, T06, T07, T08, T09)
- [x] X-2 rule compliance (only grades X, X-1, X-2)
- [x] No circular dependencies
- [x] K-2 unplugged, G3+ block coding
- [x] IXL-style specificity and assessability
- [x] CreatiCode feature accuracy

---

## Implementation Priority

### Phase 1 (Critical - Do First):
1. Fix T13.G5.05 dependency
2. Renumber T13.G3.01b → T13.G3.01.02
3. Move T13.G4.07 → T13.G5.06 and cascade renumbering
4. Add T13.G5.09

### Phase 2 (Important - Do Second):
5. Update 12 skill descriptions for clarity
6. Verify all dependency references updated

### Phase 3 (Enhancement - Do Third):
7. Add remaining 3 new skills (G5.10, G6.05, G7.06, G8.05)
8. Final validation pass

---

## Key Design Decisions

**Why move G4.07 to G5?**
- G4 had 9 skills (overloaded)
- Complex two-level nesting is more advanced than simple conditional-in-loop (G4.01)
- Creates better progression: G4.01 (simple) → G5.06 (complex two-level) → G5.05 (three+ levels)

**Why add error message skill at G5?**
- Bridges logging/tracing (G5.01) and systematic debugging (G6.02)
- Essential prerequisite for hypothesis-driven debugging
- Students can't debug what they can't recognize as errors

**Why keep test plan skills together in G4?**
- T13.G4.05.01 and .02 form coherent unit (plan → execute)
- Moving them splits related concepts
- G5.03 differentiates by adding categories and more test cases

**Why use decimal notation for sub-skills?**
- Professional and consistent
- Scales better (can have .01, .02, .03... vs limited to a, b, c)
- Matches industry practice

---

## Files to Update

1. **/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/skills_T13_testing.md** (if exists)
2. **/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md** (master file)
3. **/media/binyu/USB2/dev/CreatiCodeSkillMap/T13_COMPLETE_EXTRACTION.md** (regenerate)

---

## Expected Outcomes

After implementing all fixes:
- ✅ More balanced skill distribution across grades
- ✅ No dependency errors
- ✅ Platform-accurate debugging techniques
- ✅ More specific, assessable skills (IXL-style)
- ✅ Smoother scaffolding with filled gaps
- ✅ Professional, consistent numbering
- ✅ Complete progression K-8

**Quality Increase**: From "good foundation" to "production-ready, comprehensive"
