# T06 Optimization: Detailed Changes Table

**Date**: 2025-11-23

---

## SECTION 1: STRUCTURAL FIXES (Phase 1)

| Skill ID | Line # | Issue | Current Value | New Value | Impact |
|----------|--------|-------|---------------|-----------|--------|
| T06.G7.07 | 3894 | Broken dependency ref | `T06.G4.04A` | `T06.G4.04.01` | Fix only - no cascade |
| T06.G8.06 | 3963 | Broken dependency ref | `T06.G7.05` | `T06.G7.05.01` | Fix only - no cascade |

**Total fixes**: 2 structural errors

---

## SECTION 2: SKILL BREAKDOWNS (Phase 2)

### 2A: T06.G6.03 Breakdown

| Old Skill | Action | New Skill(s) | Description | Dependencies |
|-----------|--------|--------------|-------------|--------------|
| T06.G6.03 | REPLACE | T06.G6.03.01 | Group related event handlers by category | T06.G5.05, T06.G5.06 |
| | | T06.G6.03.02 | Extract repeated patterns into custom blocks | T06.G6.03.01, T12.G5.01 |
| | | T06.G6.03.03 | Simplify complex event logic | T06.G6.03.02, T08.G5.01 |

**Downstream updates required**:

| Affected Skill | Old Dependency | New Dependency | Rationale |
|----------------|----------------|----------------|-----------|
| T06.G7.01 | T06.G6.03 | T06.G6.03.01 | Only needs grouping foundation |
| T06.G7.02 | T06.G6.03 | T06.G6.03.01 | Only needs grouping foundation |
| T06.G7.03 | T06.G6.03 | T06.G6.03.01 | Only needs grouping foundation |
| T06.G7.04 | T06.G6.03 | T06.G6.03.01 | Only needs grouping foundation |

---

### 2B: T06.G8.06 Breakdown

| Old Skill | Action | New Skill(s) | Description | Dependencies |
|-----------|--------|--------------|-------------|--------------|
| T06.G8.06 | REPLACE | T06.G8.06.01 | Use 3D collision events | T06.G4.08.01, T18.G6.02 |
| | | T06.G8.06.02 | Use 3D picking events | T06.G8.06.01, T06.G7.05.01 |
| | | T06.G8.06.03 | Use 3D dragging events | T06.G8.06.02, T06.G6.07.01 |
| | | T06.G8.06.04 | Use 3D distance/overlap events | T06.G8.06.01, T06.G7.03 |
| | | T06.G8.06.05 | Use 3D scene initialization | T06.G4.09, T18.G6.01 |

**Downstream updates**: None identified (T06.G8.06 appears to be terminal)

---

## SECTION 3: NEW SKILLS (Phase 3)

### 3A: Grade 4 Additions

| Skill ID | Insertion Point | Skill Name | Description | Dependencies |
|----------|----------------|------------|-------------|--------------|
| T06.G4.10.01 | After T06.G4.10 (line 3557) | Use variable-based key events | Dynamic key handling with variables | T06.G4.10, T09.G4.01 |

---

### 3B: Grade 5 Additions

| Skill ID | Insertion Point | Skill Name | Description | Dependencies |
|----------|----------------|------------|-------------|--------------|
| T06.G5.10.01 | After T06.G5.10 (line ~3676) | Use 2D physics collision events | Physics-timed collision broadcasts | T06.G4.08.01, T17.G5.01 |

---

### 3C: Grade 6 Additions (Widget Events)

| Skill ID | Insertion Point | Skill Name | Description | Dependencies |
|----------|----------------|------------|-------------|--------------|
| T06.G6.05.01 | After T06.G6.05 (line ~3728) | Use widget change events | Respond to slider, input, checkbox changes | T06.G6.05, T16.G4.01 |
| T06.G6.05.02 | After T06.G6.05.01 | Use video playback events | Sync with video start/pause/time | T06.G6.05, T16.G5.01 |
| T06.G6.05.03 | After T06.G6.05.02 | Use pointer enter/leave events | Hover effects for widgets | T06.G6.05, T16.G4.01 |
| T06.G6.05.04 | After T06.G6.05.03 | Use tab selection events | Multi-page interfaces | T06.G6.05, T16.G5.02 |
| T06.G6.05.05 | After T06.G6.05.04 | Use any-button-named events | Handle grouped button controls | T06.G6.05, T16.G5.03 |

---

### 3D: Grade 8 Additions

| Skill ID | Insertion Point | Skill Name | Description | Dependencies |
|----------|----------------|------------|-------------|--------------|
| (See 2B) | (Split from G8.06) | 3D event skills | Five 3D interaction skills | (See breakdown table) |

---

## SECTION 4: DEPENDENCY STRENGTHENING (Phase 4)

| Skill ID | Change Type | Dependencies Before | Dependencies After | Rationale |
|----------|-------------|---------------------|-------------------|-----------|
| T06.G5.07 | ADD | T06.G5.01, T09.G4.01 | T06.G4.01, T06.G5.01, T09.G4.01 | Needs event building foundation |
| T06.G6.01 | ADD | T06.G5.04, T06.G5.05 | T06.G3.06, T06.G5.04, T06.G5.05 | Needs basic tracing foundation |

---

## SECTION 5: SUMMARY BY GRADE

### Kindergarten (No changes)
- 3 skills (GK.01-03)
- Status: Unchanged

### Grade 1 (No changes)
- 3 skills (G1.01-03)
- Status: Unchanged

### Grade 2 (No changes)
- 3 skills (G2.01-03)
- Status: Unchanged

### Grade 3 (No changes)
- 9 skills (G3.01-09)
- Status: Unchanged (gateway skills preserved)

### Grade 4 (1 addition)
- Before: 10 skills
- After: 11 skills
- Change: +1 new skill (G4.10.01 - variable key events)

### Grade 5 (1 addition)
- Before: 10 skills
- After: 11 skills
- Change: +1 new skill (G5.10.01 - 2D physics collision)

### Grade 6 (8 additions)
- Before: 11 skills
- After: 19 skills
- Changes:
  - G6.03 → G6.03.01, .02, .03 (+2 net)
  - G6.05 → G6.05, .01, .02, .03, .04, .05 (+5 net)
  - +2 dependency improvements
- Total: +8 net

### Grade 7 (No additions, 4 updates)
- Before: 7 skills
- After: 7 skills
- Changes: 4 dependency updates (G7.01-04 depend on new G6.03.01)

### Grade 8 (5 additions from split, 1 fix)
- Before: 6 skills
- After: 11 skills
- Changes:
  - G8.06 → G8.06.01, .02, .03, .04, .05 (+4 net)
  - G8.06 dependency fix
- Total: +5 net

---

## SECTION 6: CREATICODE FEATURE MAPPING

| CreatiCode Block Category | Before Coverage | After Coverage | Skills Added/Changed |
|---------------------------|----------------|----------------|---------------------|
| Basic events (flag, key, click) | ✓ Complete | ✓ Complete | None |
| Broadcasts (basic) | ✓ Complete | ✓ Complete | None |
| Broadcast with parameters | ✓ Complete | ✓ Complete | None |
| Send to specific sprite | ✓ Complete | ✓ Complete | None |
| 2D sprite collision | ✓ Complete | ✓ Complete | None |
| 2D physics collision | ✗ Missing | ✓ G5.10.01 | +1 |
| 2D drag events | ✓ Complete | ✓ Complete | None |
| Mouse button/position | ✓ Complete | ✓ Complete | None |
| Mouse wheel | ✓ Complete | ✓ Complete | None |
| Key press | ✓ Complete | ✓ Complete | None |
| Key release | ✓ Complete | ✓ Complete | None |
| Variable key events | ✗ Missing | ✓ G4.10.01 | +1 |
| Conditional events | ✓ Complete | ✓ Complete | None |
| Variable change events | ✓ Complete | ✓ Complete | None |
| Backdrop switch | ✓ Complete | ✓ Complete | None |
| Widget click | ✓ Complete | ✓ Complete | None |
| Widget change | ✗ Missing | ✓ G6.05.01 | +1 |
| Widget hover (enter/leave) | ✗ Missing | ✓ G6.05.03 | +1 |
| Video playback events | ✗ Missing | ✓ G6.05.02 | +1 |
| Tab selection | ✗ Missing | ✓ G6.05.04 | +1 |
| Any-button-named | ✗ Missing | ✓ G6.05.05 | +1 |
| 3D scene initialization | ✗ Missing | ✓ G8.06.05 | +1 |
| 3D collision | Partial (G8.06) | ✓ G8.06.01 | Refined |
| 3D picking | Partial (G8.06) | ✓ G8.06.02 | Refined |
| 3D dragging | Partial (G8.06) | ✓ G8.06.03 | Refined |
| 3D distance/overlap | Partial (G8.06) | ✓ G8.06.04 | Refined |
| Multiplayer events | ✗ Missing | ✗ Deferred | (T19) |

**Coverage improvement**: 18/25 (72%) → 24/25 (96%)

---

## SECTION 7: CROSS-TOPIC DEPENDENCY VALIDATION

| New Dependency | Target Topic | Target Skill | Status | Action if Missing |
|----------------|--------------|--------------|--------|-------------------|
| T08.G5.01 | Conditionals | Multi-way conditionals | ? | VERIFY EXISTS |
| T09.G4.01 | Variables | Variables in expressions | ✓ | None |
| T12.G5.01 | Custom Blocks | Extract repeated code | ? | VERIFY EXISTS |
| T16.G4.01 | Widgets | Basic widget usage | ? | VERIFY EXISTS |
| T16.G5.01 | Widgets | Video widgets | ? | VERIFY EXISTS |
| T16.G5.02 | Widgets | Tabbed interfaces | ? | VERIFY EXISTS |
| T16.G5.03 | Widgets | Dynamic widget lists | ? | VERIFY EXISTS |
| T17.G5.01 | Physics | 2D physics bodies | ? | VERIFY EXISTS |
| T18.G6.01 | 3D | 3D scene basics | ? | VERIFY EXISTS |
| T18.G6.02 | 3D | 3D object positioning | ? | VERIFY EXISTS |

**Action Required**: Run validation script to check all "?" entries

---

## SECTION 8: IMPLEMENTATION CHECKLIST

### Pre-Implementation
- [ ] Backup current allskills.md
- [ ] Backup current skills_T06_events.md
- [ ] Run cross-topic dependency validator
- [ ] Document baseline metrics (60 skills, dependencies, etc.)

### Phase 1: Structural Fixes (5 min)
- [ ] Line 3894: Change T06.G4.04A → T06.G4.04.01 in T06.G7.07
- [ ] Line 3963: Change T06.G7.05 → T06.G7.05.01 in T06.G8.06
- [ ] Verify no other broken references exist

### Phase 2: Skill Breakdowns (30 min)
- [ ] Split T06.G6.03 into .01, .02, .03
- [ ] Update T06.G7.01 dependency: G6.03 → G6.03.01
- [ ] Update T06.G7.02 dependency: G6.03 → G6.03.01
- [ ] Update T06.G7.03 dependency: G6.03 → G6.03.01
- [ ] Update T06.G7.04 dependency: G6.03 → G6.03.01
- [ ] Split T06.G8.06 into .01, .02, .03, .04, .05
- [ ] Verify all downstream skills updated

### Phase 3: New Skills (60 min)
- [ ] Add T06.G4.10.01 (variable key events)
- [ ] Add T06.G5.10.01 (2D physics collision)
- [ ] Add T06.G6.05.01 (widget change events)
- [ ] Add T06.G6.05.02 (video playback events)
- [ ] Add T06.G6.05.03 (pointer enter/leave)
- [ ] Add T06.G6.05.04 (tab selection)
- [ ] Add T06.G6.05.05 (any-button-named)
- [ ] Verify all new skills have complete descriptions
- [ ] Verify all dependencies are valid

### Phase 4: Strengthen Dependencies (15 min)
- [ ] Add T06.G4.01 to T06.G5.07 dependencies
- [ ] Add T06.G3.06 to T06.G6.01 dependencies
- [ ] Verify no circular dependencies introduced

### Phase 5: Documentation (30 min)
- [ ] Update skills_T06_events.md with all changes
- [ ] Update line numbers in documentation
- [ ] Generate new T06 statistics
- [ ] Update cross-references

### Phase 6: Validation (30 min)
- [ ] Run dependency validator
- [ ] Check for duplicate IDs
- [ ] Check for orphaned dependencies
- [ ] Verify all cross-topic deps exist
- [ ] Test sample skills for completeness
- [ ] Compare before/after metrics

### Post-Implementation
- [ ] Commit changes with detailed message
- [ ] Update changelog
- [ ] Notify stakeholders of changes
- [ ] Archive optimization plan documents

---

## SECTION 9: ROLLBACK PLAN

If issues are discovered:

### Quick Rollback (Phases 1-2 only)
- Restore from backup: `allskills_backup_before_T06_optimization_[timestamp].md`
- Estimated time: 2 minutes

### Partial Rollback
- Phases 1-2: Keep (fixes and breakdowns are low-risk)
- Phases 3-4: Revert (new skills and dependencies)
- Estimated time: 15 minutes

### Full Rollback
- Restore complete backup
- Document lessons learned
- Revise plan before retry
- Estimated time: 5 minutes

---

## SECTION 10: SUCCESS METRICS

### Quantitative
- **Before**: 60 T06 skills
- **After**: 77 T06 skills
- **Growth**: +28%

### Quality
- **Broken references**: 2 → 0
- **Overly broad skills**: 2 → 0
- **CreatiCode coverage**: 72% → 96%
- **Microstep compliance**: Good → Excellent

### Validation
- **Dependency errors**: 0 expected
- **Circular dependencies**: 0 expected
- **Orphaned skills**: 0 expected
- **Coverage gaps**: 1 (multiplayer, deferred)

---

## SECTION 11: NOTES AND CAVEATS

### Assumptions
1. T16 (Widgets) has foundation skills at G4-G5 levels
2. T17 (Physics) has 2D physics body creation at G5
3. T18 (3D) has scene and object skills at G6
4. T12 (Custom Blocks) has extraction skill at G5
5. T08 (Conditionals) has multi-way conditionals at G5

### Risks
- **Medium**: Cross-topic dependencies may not exist → Need validation
- **Low**: Skill breakdowns may affect learning paths → Well-scaffolded
- **Low**: G6 may be too dense (19 skills) → Appropriate for depth

### Mitigations
- Validate all cross-topic dependencies before finalizing
- Use backup/rollback plan if issues arise
- Phase implementation allows early issue detection
- Maintain sync between allskills.md and skills_T06_events.md

### Future Work
- Consider multiplayer events in T19 optimization
- Monitor if G6.05.01-.05 should be split further
- Evaluate if 3D physics events need separate skills (T17 or T18)
- Consider adding "when condition becomes false" as complement to G5.07

---

## APPENDIX: FILE LOCATIONS

- **Main plan**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/T06_OPTIMIZATION_PLAN.md`
- **Quick reference**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/T06_QUICK_REFERENCE.md`
- **This file**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/T06_DETAILED_CHANGES_TABLE.md`
- **Target files**:
  - `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`
  - `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/skills_T06_events.md`
- **Reference**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/CREATICODE_EVENT_BLOCKS_COMPREHENSIVE.md`

---

**END OF DETAILED CHANGES TABLE**
