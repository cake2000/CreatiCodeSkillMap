# T18 Implementation Checklist

**Start Date**: _____________
**Target Completion**: _____________
**Current Status**: Not Started

---

## HOW TO USE THIS CHECKLIST

1. Mark items with `[✓]` when completed
2. Add completion date next to each item
3. Note any issues or deviations in the Notes column
4. Update Current Status at top when phases complete

---

## PHASE 1: CRITICAL FIXES (Week 1)

**Target**: All skills follow ONE-BLOCK rule, correct block names
**Priority**: 🚨 CRITICAL

| Item | Task | File Location | Status | Date | Notes |
|------|------|---------------|--------|------|-------|
| 1.1 | Split T18.G4.01.02 into capsule + torus (2 skills) | allskills.md line ~14544 | [ ] | | |
| 1.2 | Renumber old T18.G4.01.03 → T18.G4.01.04 | allskills.md line ~14555 | [ ] | | |
| 1.3 | Update all references to T18.G4.01.03 → T18.G4.01.04 | Search entire file | [ ] | | |
| 1.4 | Split T18.G7.01.03 into 4 skills (cone, tube, rect tube, stairs) | allskills.md line ~15055 | [ ] | | |
| 1.5 | Renumber all G7 skills after +3 positions | allskills.md G7 section | [ ] | | |
| 1.6 | Update all references to renumbered G7 skills | Search entire file | [ ] | | |
| 1.7 | Fix T18.G3.05 description ("move to" not "go to") | allskills.md line ~14479 | [ ] | | |
| 1.8 | Fix T18.G3.06.01 description ("update color diffusion") | allskills.md line ~14490 | [ ] | | |
| 1.9 | Fix T18.G3.06.02 description (clarify parameters) | allskills.md line ~14501 | [ ] | | |
| 1.10 | Decide fate of T18.G4.01.03 (old - composite skill) | allskills.md line ~14555 | [ ] | | Delete or move to G6+ |
| 1.11 | Clarify T18.G4.06 as non-physics collision | allskills.md line ~14673 | [ ] | | Add note about physics vs non-physics |

**Phase 1 Completion**: [ ] All items above completed
**Completion Date**: _____________

---

## PHASE 2: HIGH-PRIORITY MISSING SKILLS (Week 2)

**Target**: Add 10 most-needed missing skills
**Priority**: ⚡ HIGH

| Item | Task | Insert After | Status | Date | Notes |
|------|------|-------------|--------|------|-------|
| 2.1 | Add: Distance between objects (G4) | T18.G3.05 or T18.G4.XX | [ ] | | See ACTIONABLE_FIXES.md |
| 2.2 | Add: Set object speed (G4) | T18.G3.07 or T18.G4.XX | [ ] | | See ACTIONABLE_FIXES.md |
| 2.3 | Add: Copy position from camera (G5) | T18.G4.03.01 or T18.G5.XX | [ ] | | See ACTIONABLE_FIXES.md |
| 2.4 | Add: Copy direction from camera (G5) | T18.G5.XX | [ ] | | See ACTIONABLE_FIXES.md |
| 2.5 | Add: Remove object named (G4) | T18.G3.04.01 or T18.G4.XX | [ ] | | See ACTIONABLE_FIXES.md |
| 2.6 | Add: Remove all objects (G4) | After remove object named | [ ] | | See ACTIONABLE_FIXES.md |
| 2.7 | Add: Remove light named (G5) | T18.G4.02.01 or T18.G5.XX | [ ] | | See ACTIONABLE_FIXES.md |
| 2.8 | Add: Remove all lights (G5) | After remove light named | [ ] | | See ACTIONABLE_FIXES.md |
| 2.9 | Add: Set scene background color (G3) | T18.G3.03 or nearby | [ ] | | See ACTIONABLE_FIXES.md |
| 2.10 | Add: Show 3D axis (G4) | T18.G3.01 or T18.G4.XX | [ ] | | See ACTIONABLE_FIXES.md |

**Phase 2 Completion**: [ ] All items above completed
**Completion Date**: _____________
**Coverage After Phase 2**: ____% (target: 30%)

---

## PHASE 3: DEPENDENCY CLEANUP (Week 3)

**Target**: Remove unnecessary dependencies, fix wrong dependencies
**Priority**: 🧹 MEDIUM

### Remove Unnecessary Cross-Topic Dependencies

| Item | Skill | Remove Dependency | Status | Date | Notes |
|------|-------|------------------|--------|------|-------|
| 3.1 | T18.G3.03 | Remove T09.G3.01 (variables) | [ ] | | Scene init doesn't need variables |
| 3.2 | T18.G3.03 | Remove T07.G3.02 (loops) | [ ] | | Scene init doesn't need loops |
| 3.3 | T18.G3.03 | Remove T03.G3.03 (storyboard) | [ ] | | Not needed for basic init |
| 3.4 | T18.G3.04.01 | Remove T08.G3.01 (conditionals) | [ ] | | Adding box doesn't need if |
| 3.5 | T18.G4.05.01 | Remove T07.G3.01 (loops) | [ ] | | Playing animation doesn't need loops |
| 3.6 | T18.G3.02 | Remove T07.G3.01 (loops) | [ ] | | Camera matching is observation |

### Fix Wrong Intra-Topic Dependencies

| Item | Skill | Change From | Change To | Status | Date | Notes |
|------|-------|-------------|-----------|--------|------|-------|
| 3.7 | T18.G4.03.01 | T18.G4.02.03 (lights) | T18.G3.03 (scene init) | [ ] | | Orbit camera needs scene, not lights |
| 3.8 | T18.G4.03.01 | Also remove T07.G2.01 | (remove completely) | [ ] | | Not needed |
| 3.9 | T18.G4.04.01 | T18.G4.03.02 (camera) | T18.G3.03 (scene init) | [ ] | | Models need scene, not cameras |
| 3.10 | T18.G4.04.01 | Also remove T07.G2.01 | (remove completely) | [ ] | | Not needed |

**Phase 3 Completion**: [ ] All items above completed
**Completion Date**: _____________

---

## PHASE 4: GRADE LEVEL ADJUSTMENTS (Week 3-4)

**Target**: Move skills to appropriate grade levels
**Priority**: 🧹 MEDIUM

| Item | Skill | Current Grade | New Grade | Reason | Status | Date | Notes |
|------|-------|---------------|-----------|--------|--------|------|-------|
| 4.1 | T18.G3.07 | G3 | G4 | Too complex for G3 | [ ] | | Keyboard + movement + loops |
| 4.2 | T18.G3.08 | G3 | G4 | Too abstract for G3 | [ ] | | Script tracing |
| 4.3 | T18.G6.05.01 | G6 | G4 (as T18.G4.02.04) | Same complexity as point lights | [ ] | | Spot lights |
| 4.4 | T18.G5.04.01 | G5 | G6 | Nested loops are G6 concept | [ ] | | Wait for nested loop skills |
| 4.5 | Update all dependency references | (various) | (various) | After moves complete | [ ] | | Check all deps still valid |

**Phase 4 Completion**: [ ] All items above completed
**Completion Date**: _____________

---

## PHASE 5: SYSTEMATIC GAP FILLING (Weeks 4-6)

**Target**: Add remaining ~60 skills to reach 80% coverage
**Priority**: 📈 ONGOING

### Category 1: 3D Action (Worst Coverage - 16%)

**Target**: 30 new skills

| Priority | Block/Feature | Grade | Status | Date | Notes |
|----------|---------------|-------|--------|------|-------|
| High | Rotate to angle around axis | G4 | [ ] | | |
| High | Rotate to direction xyz | G4 | [ ] | | |
| High | Turn degrees around axis | G4 | [ ] | | |
| High | Move along current direction | G4 | [ ] | | |
| High | Point to position xyz | G4 | [ ] | | |
| High | Copy position from object | G5 | [ ] | | |
| High | Copy direction from object | G5 | [ ] | | |
| High | Select sprite object by name | G5 | [ ] | | |
| High | Sprite object name (reporter) | G5 | [ ] | | |
| High | Update bone (skeletal animation) | G6 | [ ] | | |
| High | Attach to body part | G6 | [ ] | | |
| High | Detach from body | G6 | [ ] | | |
| High | Turn on collision | G5 | [ ] | | |
| High | Broadcast on collision | G5 | [ ] | | |
| High | Update collider dimension | G5 | [ ] | | |
| High | Sprite object blocked (reporter) | G5 | [ ] | | |
| High | Broadcast when overlap | G5 | [ ] | | |
| High | Broadcast when distance | G5 | [ ] | | |
| High | Set distance sensor (6 directions) | G5 | [ ] | | |
| High | Name of nearest obstacle | G5 | [ ] | | |
| High | Distance to nearest obstacle | G5 | [ ] | | |
| Med | Turn on hovering | G6 | [ ] | | |
| Med | Turn off hovering | G6 | [ ] | | |
| Med | Hovered object name | G6 | [ ] | | |
| Med | Hovered point x/y/z pos (3 blocks) | G6 | [ ] | | |
| Med | Turn off picking | G6 | [ ] | | |
| Med | When object is picked (event) | G6 | [ ] | | |
| Med | Set dragging limits | G6 | [ ] | | |
| Med | Set dragging mode | G6 | [ ] | | |
| Med | Dragged object name | G6 | [ ] | | |
| Med | Dragging events (3 event blocks) | G6 | [ ] | | |
| Low | Map screen XY to XYZ position | G7 | [ ] | | |

**Category 1 Progress**: [ ] 0/30 completed

---

### Category 2: 3D Tools (Worst Coverage - 16%)

**Target**: 15 new skills

| Priority | Block/Feature | Grade | Status | Date | Notes |
|----------|---------------|-------|--------|------|-------|
| High | Update scale xyz | G4 | [ ] | | |
| High | Update size xyz | G4 | [ ] | | |
| High | Get color of object (reporter) | G5 | [ ] | | |
| High | Add texture with shared file | G5 | [ ] | | |
| High | Objects are overlapping (reporter) | G5 | [ ] | | |
| High | Bake current transformations | G6 | [ ] | | |
| High | Copy object (with sharing option) | G6 | [ ] | | |
| Med | Apply grid material | G6 | [ ] | | |
| Med | Material setting (wireframe, backface, etc.) | G6 | [ ] | | |
| Med | Convert to flat shading | G6 | [ ] | | |
| Med | Set camera facing mode | G6 | [ ] | | |
| Med | Set rendering layer | G6 | [ ] | | |
| Med | For each 3D object (loop) | G6 | [ ] | | |
| Med | Update vertices | G7 | [ ] | | |
| Med | Subdivide faces | G7 | [ ] | | |
| Low | Show bounding box | G7 | [ ] | | |
| Low | Show edges | G7 | [ ] | | |
| Low | Show skeleton | G7 | [ ] | | |
| Low | Remove all reflections | G7 | [ ] | | |
| Low | Reflect in mirror | G7 | [ ] | | |
| Low | Copy to mirror position | G7 | [ ] | | |
| Low | Copy by matrix from center | G7 | [ ] | | |

**Category 2 Progress**: [ ] 0/15 completed

---

### Category 3: 3D Object (Missing Basics - 20%)

**Target**: 20 new skills

| Priority | Block/Feature | Grade | Status | Date | Notes |
|----------|---------------|-------|--------|------|-------|
| High | Add 6-colored box | G4 | [ ] | | Different color per face |
| High | Add tube (hollow cylinder) | G5 | [ ] | | |
| High | Add rectangle tube | G7 | [ ] | | Moved from split T18.G7.01.03 |
| High | Add 3D thick text | G7 | [ ] | | With thickness/depth |
| High | Add plane from equation | G7 | [ ] | | From abcd coefficients |
| High | Add public object at URL | G6 | [ ] | | |
| High | Add community model | G6 | [ ] | | |
| High | Add voxel | G6 | [ ] | | |
| High | Extrude costume | G6 | [ ] | | 2D → 3D |
| High | Add avatar for user | G5 | [ ] | | Different signature |
| High | Add user avatar | G5 | [ ] | | Current user |
| Med | Add line | G5 | [ ] | | |
| Med | Add dotted line | G5 | [ ] | | |
| Med | Add curve from list | G6 | [ ] | | |
| Med | Generate arc points | G6 | [ ] | | Helper for curves |
| Med | Add moving line between objects | G6 | [ ] | | Dynamic line |
| Low | Add transformer | G7 | [ ] | | |
| Low | Set object from sprite as parent | G6 | [ ] | | |
| Low | Unlink all children | G6 | [ ] | | |
| Low | Unlink parent | G6 | [ ] | | |
| Low | Set camera as parent | G6 | [ ] | | |
| Low | Show local axis | G5 | [ ] | | |
| Low | Object exists (reporter) | G5 | [ ] | | |
| Low | Convert to SPS | G7 | [ ] | | Solid Particle System |
| Low | Add to SPS | G7 | [ ] | | |
| Low | Property get/set (generic) | G7 | [ ] | | 3 blocks |

**Category 3 Progress**: [ ] 0/20 completed

---

### Category 4: 3D Effect (Missing Configs - 17%)

**Target**: 10 new skills

| Priority | Block/Feature | Grade | Status | Date | Notes |
|----------|---------------|-------|--------|------|-------|
| High | Add particle emitter (custom) | G6 | [ ] | | vs prebuilt |
| Med | Configure box emitter | G6 | [ ] | | |
| Med | Configure cone emitter | G6 | [ ] | | |
| Med | Configure cylinder emitter | G6 | [ ] | | |
| Med | Configure hemispheric emitter | G6 | [ ] | | |
| Med | Configure mesh emitter | G7 | [ ] | | |
| Med | Configure sphere emitter | G6 | [ ] | | |
| Med | Configure emitter blend mode | G6 | [ ] | | |
| Med | Configure emitter initial rotation | G6 | [ ] | | |
| Med | Configure emitter movement | G6 | [ ] | | |
| Med | Configure emitter rotation speed | G6 | [ ] | | |
| Med | Configure emitter scale | G6 | [ ] | | |
| Low | Emitter action (start/stop/pause) | G6 | [ ] | | |
| Low | Start emitter with rate | G6 | [ ] | | |

**Category 4 Progress**: [ ] 0/10 completed

---

### Category 5: 3D Scene (Polish - 32%)

**Target**: 10 new skills

| Priority | Block/Feature | Grade | Status | Date | Notes |
|----------|---------------|-------|--------|------|-------|
| High | Show 3D scene | G3 | [ ] | | Already added in Phase 2? |
| Med | When 3D scene is initialized (event) | G3 | [ ] | | |
| Med | Remove sky | G5 | [ ] | | |
| Med | Set clipping plane | G7 | [ ] | | |
| Med | Remove clipping plane | G7 | [ ] | | |
| Med | Remove pipeline | G8 | [ ] | | |
| Low | Lock pointer | G6 | [ ] | | |
| Low | Turn webcam background | G7 | [ ] | | |
| Low | Switch to full screen | G6 | [ ] | | |
| Low | GPU Available (reporter) | G8 | [ ] | | |
| Low | Set camera target xyz | G5 | [ ] | | |
| Low | Set camera target object | G5 | [ ] | | |
| Low | Set display region (multi-camera) | G8 | [ ] | | |
| Low | Set camera distance/angles | G6 | [ ] | | |
| Low | Configure camera (limits) | G6 | [ ] | | |
| Low | Camera property (reporter) | G5 | [ ] | | |
| Low | Get camera direction (reporter) | G5 | [ ] | | |
| Low | Get camera view position (reporter) | G6 | [ ] | | |
| Low | Receives shadow | G6 | [ ] | | |
| Low | Switch light on/off | G5 | [ ] | | |
| Low | Exclude object from light | G6 | [ ] | | |
| Low | Remove from glow layer | G6 | [ ] | | |
| Low | Remove from highlight layer | G6 | [ ] | | |
| Low | Joystick property (reporter) | G6 | [ ] | | |
| Low | Remove all joysticks | G6 | [ ] | | |
| Low | Set [OBJECT] as parent of camera | G6 | [ ] | | |

**Category 5 Progress**: [ ] 0/10 completed

---

### Category 6: 3D Physics (Fair Coverage - 42%, but gaps remain)

**Target**: 10 new skills

| Priority | Block/Feature | Grade | Status | Date | Notes |
|----------|---------------|-------|--------|------|-------|
| High | Update gravity | G5 | [ ] | | |
| High | Set physics frame rate | G6 | [ ] | | |
| High | Get physics frame rate (reporter) | G6 | [ ] | | |
| High | Remove physics body | G5 | [ ] | | |
| High | Get physics body property (reporter) | G5 | [ ] | | |
| Med | Freeze all physics bodies | G6 | [ ] | | |
| Med | Add physics bodies into compound | G7 | [ ] | | |
| Med | Set physics body speed (5 variants) | G6 | [ ] | | 5 separate skills |
| Med | Lock physics body speed | G6 | [ ] | | |
| Med | Set physics body damping | G6 | [ ] | | |
| Med | Set rotation speed limit | G6 | [ ] | | |
| Med | Set movement speed limit | G6 | [ ] | | |
| Med | Set limits for hinge | G7 | [ ] | | |
| Med | Set speed for hinge (motor) | G7 | [ ] | | |
| Med | Remove constraint | G7 | [ ] | | |
| Med | Names of physics bodies in contact (reporter) | G6 | [ ] | | |
| Low | Set car engine force | G8 | [ ] | | |
| Low | Set car wheel angle | G8 | [ ] | | |
| Low | Steer car to angle | G8 | [ ] | | |
| Low | Set car wheel engine force (individual) | G8 | [ ] | | |

**Category 6 Progress**: [ ] 0/10 completed

---

### Category 7: Advanced/Specialized (Lower Priority)

**Target**: 5 new skills

| Priority | Block/Feature | Grade | Status | Date | Notes |
|----------|---------------|-------|--------|------|-------|
| Low | Geometry: add point | G7 | [ ] | | |
| Low | Geometry: add point between | G7 | [ ] | | |
| Low | Geometry: add line | G7 | [ ] | | |
| Low | Geometry: add triangle | G7 | [ ] | | |
| Low | Geometry: add frame box | G7 | [ ] | | |
| Low | Geometry: add angle mark | G7 | [ ] | | |
| Low | Chemistry: add atom | G7 | [ ] | | |
| Low | Chemistry: add custom atom | G7 | [ ] | | |
| Low | Convert to transparent occlusion (AR) | G8 | [ ] | | |
| Low | Show inspector (AR) | G8 | [ ] | | |
| Low | Add animations (list) | G6 | [ ] | | |
| Low | Start animation (custom) | G6 | [ ] | | |

**Category 7 Progress**: [ ] 0/5 completed

---

**Phase 5 Overall Progress**: [ ] 0/~60 completed
**Phase 5 Completion Date**: _____________
**Final Coverage**: ____% (target: 80%)

---

## FINAL VALIDATION (Week 7)

**Target**: Verify all changes are correct and consistent

| Item | Task | Status | Date | Notes |
|------|------|--------|------|-------|
| V.1 | Verify all skill IDs are sequential | [ ] | | No gaps in numbering |
| V.2 | Verify all dependencies reference valid skill IDs | [ ] | | No broken refs |
| V.3 | Verify all block names match CreatiCode reference | [ ] | | Check against CREATICODE_3D_BLOCKS_REFERENCE.md |
| V.4 | Verify grade progression makes sense | [ ] | | Skills build on each other |
| V.5 | Test sample learning paths (K→G8) | [ ] | | Pick 3 paths, trace dependencies |
| V.6 | Check for duplicate skills | [ ] | | Same block covered twice |
| V.7 | Verify X-2 rule compliance | [ ] | | Deps at X, X-1, or X-2 only |
| V.8 | Spell check all descriptions | [ ] | | Professional presentation |
| V.9 | Verify coverage percentage | [ ] | | Should be 75-80% |
| V.10 | Document remaining gaps | [ ] | | List blocks still uncovered |

**Final Validation Complete**: [ ]
**Completion Date**: _____________

---

## ROLLOUT (Week 8)

| Item | Task | Status | Date | Notes |
|------|------|--------|------|-------|
| R.1 | Backup original allskills.md | [ ] | | Just in case |
| R.2 | Commit changes to version control | [ ] | | With detailed commit message |
| R.3 | Update any external documentation | [ ] | | References to T18 |
| R.4 | Notify team of changes | [ ] | | Email/Slack/meeting |
| R.5 | Update skill map visualizations | [ ] | | If any diagrams exist |
| R.6 | Train educators on new skills | [ ] | | If needed |
| R.7 | Monitor for issues | [ ] | | First 2 weeks |

**Rollout Complete**: [ ]
**Completion Date**: _____________

---

## METRICS TRACKING

### Coverage Progress

| Checkpoint | Date | Coverage % | Skills Added | Notes |
|------------|------|-----------|--------------|-------|
| Initial | | 25% | 82 | Baseline |
| Phase 1 Complete | | 25% | ~85 | Fixed multi-block issues |
| Phase 2 Complete | | 30% | ~95 | Added high-priority skills |
| Phase 3 Complete | | 30% | ~95 | Cleaned dependencies |
| Phase 4 Complete | | 80% | ~157 | Filled gaps systematically |
| Final | | __% | ____ | |

### Quality Metrics

| Metric | Initial | Target | Final | Notes |
|--------|---------|--------|-------|-------|
| ONE-BLOCK compliance | 96% | 100% | __% | |
| Dependency cleanliness | 82% | 95% | __% | |
| Grade appropriateness | 94% | 100% | __% | |
| Block name accuracy | 96% | 100% | __% | |
| Coverage | 25% | 80% | __% | |

---

## ISSUES LOG

| Date | Issue | Resolution | Status |
|------|-------|-----------|--------|
| | | | |
| | | | |
| | | | |

---

## NOTES & LESSONS LEARNED

_Use this space to document challenges, decisions, and insights for future reference_

---

**Checklist Created**: 2025-11-25
**Last Updated**: _____________
**Maintained By**: _____________
