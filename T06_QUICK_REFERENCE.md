# T06 Optimization Quick Reference

**Date**: 2025-11-23

---

## CRITICAL FIXES (Must Do)

### Fix 1: T06.G7.07 Broken Dependency
**Line**: 3894
**Change**: `T06.G4.04A` → `T06.G4.04.01`

### Fix 2: T06.G8.06 Broken Dependency
**Line**: 3963
**Change**: `T06.G7.05` → `T06.G7.05.01`

---

## MAJOR CHANGES

### 1. Split T06.G6.03 (Refactoring) → 3 Skills
- **T06.G6.03.01**: Group related event handlers
- **T06.G6.03.02**: Extract to custom blocks
- **T06.G6.03.03**: Simplify event logic

**Update downstream**: T06.G7.01, G7.02, G7.03, G7.04 → depend on G6.03.01

---

### 2. Split T06.G8.06 (3D Events) → 5 Skills
- **T06.G8.06.01**: 3D collision events
- **T06.G8.06.02**: 3D picking events
- **T06.G8.06.03**: 3D dragging events
- **T06.G8.06.04**: 3D distance/overlap events
- **T06.G8.06.05**: 3D scene initialization

---

## NEW SKILLS TO ADD (14 New)

### G4 Additions (1)
- **T06.G4.10.01**: Variable-based key events (after G4.10)

### G5 Additions (1)
- **T06.G5.10.01**: 2D physics collision events (after G5.10)

### G6 Additions (5)
- **T06.G6.05.01**: Widget change events
- **T06.G6.05.02**: Video widget events
- **T06.G6.05.03**: Pointer enter/leave (hover) events
- **T06.G6.05.04**: Tab selection events
- **T06.G6.05.05**: Any-button-named events

### G8 Additions (already counted in split)
- Part of T06.G8.06 split

---

## DEPENDENCY UPDATES

### Strengthen Existing Skills
1. **T06.G5.07**: Add `T06.G4.01` dependency
2. **T06.G6.01**: Add `T06.G3.06` dependency

### Update After G6.03 Split
All skills depending on old `T06.G6.03` should depend on `T06.G6.03.01`:
- T06.G7.01
- T06.G7.02
- T06.G7.03
- T06.G7.04

---

## STATISTICS

### Before Optimization
- **Total T06 Skills**: 60
- **G6 Skills**: 11
- **G8 Skills**: 6
- **CreatiCode Coverage**: ~75%

### After Optimization
- **Total T06 Skills**: 77 (+17, +28%)
- **G6 Skills**: 19 (+8)
- **G8 Skills**: 11 (+5)
- **CreatiCode Coverage**: 96%

---

## VALIDATION CHECKLIST

Before implementation:
- [ ] Verify T16 widget skills exist (G4.01, G5.01, G5.02, G5.03)
- [ ] Verify T17 physics skills exist (G5.01)
- [ ] Verify T18 3D skills exist (G6.01, G6.02)
- [ ] Verify T12.G5.01 exists (custom blocks)
- [ ] Backup allskills.md
- [ ] Run dependency validator after changes

---

## IMPLEMENTATION ORDER

1. **Phase 1**: Fix broken references (5 minutes)
   - T06.G7.07 dependency
   - T06.G8.06 dependency

2. **Phase 2**: Break down broad skills (30 minutes)
   - Split T06.G6.03 → .01, .02, .03
   - Split T06.G8.06 → .01, .02, .03, .04, .05
   - Update downstream dependencies

3. **Phase 3**: Add new skills (60 minutes)
   - Add 14 new skills with proper dependencies
   - Verify cross-topic dependencies exist

4. **Phase 4**: Strengthen scaffolding (15 minutes)
   - Update T06.G5.07
   - Update T06.G6.01

5. **Phase 5**: Validate (30 minutes)
   - Run dependency checker
   - Test sample skills
   - Update skills_T06_events.md

---

## KEY DECISIONS

### Why Split T06.G6.03?
- Combined 4 activities → Now 3 focused microsteps
- Better scaffolding: group → extract → simplify

### Why Split T06.G8.06?
- Combined 5 3D event types → Now 5 focused skills
- Each 3D interaction is complex enough for dedicated practice

### Why Add Widget Skills?
- CreatiCode has 10 widget event blocks
- Original coverage: only clicks (1 skill)
- New coverage: clicks, changes, hover, video, tabs, any-button (6 skills)

### Why Add Physics/3D Skills?
- CreatiCode-specific features underrepresented
- Physics events have different timing than regular collision
- 3D events are specialized and deserve granular coverage

---

## CROSS-TOPIC IMPACT

### New Dependencies on T16 (Widgets)
- 5 new skills depend on T16.G4-G5
- **Action**: Verify T16 has required foundation skills

### New Dependencies on T17 (Physics)
- 1 new skill depends on T17.G5
- **Action**: Verify T17.G5.01 exists (2D physics bodies)

### New Dependencies on T18 (3D)
- 5 new skills depend on T18.G6
- **Action**: Verify T18 has 3D scene and object skills

### No Changes to T07, T08, T09
- Core gateway dependencies remain stable
- G3 event skills unchanged (still gate loops/conditionals)

---

## RISK ASSESSMENT

### Low Risk
- Fixing broken references (Phase 1)
- Adding new leaf skills with valid dependencies (Phase 3)

### Medium Risk
- Breaking down skills (Phase 2) - requires careful downstream updates
- Cross-topic dependencies - need validation that target skills exist

### High Risk
- None identified

---

## SUCCESS CRITERIA

After implementation:
1. ✓ No broken dependency references
2. ✓ All new skills have valid dependencies
3. ✓ No duplicate IDs
4. ✓ Dependency checker passes
5. ✓ CreatiCode event coverage >= 95%
6. ✓ All G6-G8 skills are focused microsteps
7. ✓ Downstream skills updated correctly after splits

---

## QUESTIONS FOR REVIEW

1. Are T16 widget foundation skills (G4.01, G5.01-03) defined?
2. Does T17.G5.01 exist for 2D physics bodies?
3. Do T18.G6.01-02 exist for 3D scenes and objects?
4. Is G6 with 19 skills acceptable, or should some move to G7?
5. Should multiplayer events be addressed here or in T19?

---

## CONTACT & NOTES

- See full plan: `T06_OPTIMIZATION_PLAN.md`
- Estimated implementation time: 3-4 hours
- Recommended: Start with Phase 1 (fixes only) for quick win
- Consider implementing in branches for safe rollback
