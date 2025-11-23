# T18 Skills - Before/After Comparison

**Analysis Date:** 2025-11-23

This document shows the current skill structure vs. recommended structure after Phase 1 fixes.

---

## CURRENT STRUCTURE (Before Fixes)

### Early Grades: GK-G2 (3 skills) - SPARSE
```
GK.01: Explore 3D shapes in real world (unplugged)
G1.01: Match 3D shapes to names (unplugged)
G2.01: Identify front/top/side views (unplugged)
```

### Grade 3: Fundamentals (8 skills)
```
G3.01: Interpret 3D axis directions
G3.02: Match camera views to layouts
G3.03: Initialize 3D scene ← TOO SIMPLE (1 block)
G3.04: Add primitives ← TOO BROAD (11 shape types)
  G3.04.01: Rotate objects
G3.05: Position shapes with x/y/z
G3.06: Change colors or textures ← TOO BROAD (colors + textures + PBR)
G3.07: Move player with keyboard ← BLOCKED by G3.06
G3.08: Trace 3D script ← VAGUE ("short script" undefined)
```
**Issues:** 5 HIGH (H1, H13, H14, H23, H24), 2 MEDIUM (M1, M9)

### Grade 4: Building Scenes (9 skills)
```
G4.01: Compose multi-part scene
G4.02: Configure lighting ← TOO BROAD (3 light types)
  G4.02.01: Manage lights dynamically
  G4.02.02: Add point lights
G4.03: Create following/orbiting camera ← OVER-CONSTRAINED
G4.04: Place imported models ← TOO BROAD (library + URL)
  G4.04.01: Scale and resize
G4.05: Animate scenery with loops ← MISSING prerequisite (no basic animation)
  G4.05.01: Use distance sensors ← BLOCKED by movement chain
  G4.05.02: Understand collision types ← TOO BROAD (3 types)
G4.06: Trigger collision events ← BEFORE understanding types
G4.07: Control model animations
  G4.07.01: Add avatar animations
G4.08: Add 3D text
```
**Issues:** 10 HIGH (H2-H5, H15, H16, H19-H22), 4 MEDIUM (M3, M4)

### Grade 5: Physics & Effects (14 skills) - OVERCROWDED
```
G5.01: Initialize physics world
G5.02: Attach static/dynamic bodies
  G5.02.01: Pick 3D objects ← MISCATEGORIZED (not physics)
  G5.02.02: Drag 3D objects ← MISCATEGORIZED (not physics)
G5.03: Detect physics collisions
G5.04: Nested loops for grids ← MISSING scaffolding
  G5.04.01: Copy by matrix
  G5.04.02: Mirror/rotation copy
G5.05: Apply detailed textures
G5.06: Add fog effects
  G5.06.01: Enable shadows ← INCORRECT dependency on physics
  G5.06.02: Change sky background
G5.07: Add particle emitters ← TOO BROAD (prebuilt + custom)
G5.08: Apply forces/impulses
  G5.08.01: Remove objects ← INCORRECT dependency on physics
G5.09: Adjust camera dynamically
G5.10: Add joystick controls
```
**Issues:** 5 HIGH (H6-H8, H17), 3 MEDIUM (M5, M6), 3 LOW (L4-L6)

### Grade 6: Mixed Topics (7 skills) - INCOHERENT THEME
```
G6.01: Set up collision groups
G6.02: Debug 3D scene ← VAGUE process, BLOCKED by nested loops
G6.03: Refactor into loops/functions ← MISSING basic version
G6.04: Implement mouse look camera
G6.05: Trigger advanced visual effects
G6.06: Use constraints ← TOO BROAD (2 types)
  G6.06.01: Create parent-child hierarchies
```
**Issues:** 4 HIGH (H9, H10, H18, H26), 1 MEDIUM (M13)

### Grade 7: Gameplay Mechanics (6 skills)
```
G7.01: Waypoint NPC movement ← MISSING movement prerequisites
G7.02: Design collision response
G7.03: Use 3D distance calculations
G7.04: Implement physics puzzle
G7.05: Script camera cutscenes
G7.06: Control avatar animations ← DUPLICATE of G4.07.01?
```
**Issues:** 1 HIGH (H11), 2 MEDIUM (M7, M14)

### Grade 8: Systems & Optimization (5 skills)
```
G8.01: Load level layouts ← INCORRECT dependency on physics
G8.02: Multiple cameras split-screen ← OVER-CONSTRAINED
G8.03: Optimize 3D game performance
G8.04: Analyze quality/performance trade-offs ← VAGUE criteria
G8.05: Use car physics
```
**Issues:** 2 HIGH (H12, H25), 2 MEDIUM (M8, M14, M15)

---

## RECOMMENDED STRUCTURE (After Fixes)

### Early Grades: GK-G2 (6-9 skills) - EXPANDED
```
GK.01: Explore 3D shapes in real world ✓
GK.02: Identify shapes in 3D models [NEW]
GK.03: Match objects to silhouettes [NEW]

G1.01: Match 3D shapes to names ✓
G1.02: Build shape from multiple views [NEW]
G1.03: Count visible faces [NEW]

G2.01: Identify front/top/side views ✓
G2.02: Draw missing view from object [NEW]
G2.03: Predict view from rotation [NEW]
```
**Changes:** +6 skills for better early scaffolding

### Grade 3: Fundamentals (10-11 skills) - FOCUSED
```
G3.01: Interpret 3D axis directions ✓ (make fully unplugged OR coding)
G3.02: Match camera views to layouts ✓ (make fully unplugged OR coding)
G3.03: Initialize 3D scene & basic setup [EXPANDED]
  - Initialize scene + show axis + set background color
G3.04: Add basic primitives [FOCUSED]
  - Box, sphere, cylinder ONLY (3 shapes)
  G3.04.01: Rotate objects around axes ✓
G3.05: Position shapes with x/y/z ✓
G3.06: Change object colors [FOCUSED - colors only, remove textures]
G3.07: Move player with keyboard [MOVED EARLIER - before G3.06]
G3.08: Trace 3D script [CLARIFIED]
  - "3-5 blocks using move/rotate/turn, predict final position"
G3.09: Understand collision detection types [NEW - conceptual]
  - Raycast (blocking), overlap (triggers), physics (realistic)
```
**Changes:** Renumbered, split G3.04, split G3.06, moved G3.07, clarified G3.08, added G3.09

### Grade 4: Building Scenes (16-18 skills) - WELL-SCAFFOLDED
```
G4.01: Understand camera basics [NEW]
  - Camera as viewpoint, show axis, simple orbit camera
G4.02: Compose multi-part scene ✓ (was G4.01, renumbered)
G4.03: Add ambient light [SPLIT from old G4.02]
  G4.03.01: Manage lights dynamically ✓ (was G4.02.01)
  G4.03.02: Add point lights ✓ (was G4.02.02)
G4.04: Add directional light [SPLIT from old G4.02]
G4.05: Add spot light [SPLIT from old G4.02]
G4.06: Add specialized primitives [SPLIT from G3.04]
  - Plane, cone, capsule, tube, torus, stairs
G4.07: Apply textures to objects [NEW - split from G3.06]
G4.08: Detect when objects overlap [NEW - simple collision]
G4.09: Create multiple objects with loops [NEW - loop application]
G4.10: Animate a 3D object [NEW - single move/rotate with timing]
G4.11: Animate scenery with loops ✓ (was G4.05)
G4.12: Create following/orbiting camera [SIMPLIFIED]
  - Depend only on G4.01, not player movement
G4.13: Use CreatiCode prebuilt models [SPLIT from old G4.04]
  G4.13.01: Scale and resize objects ✓ (was G4.04.01, now for all objects)
G4.14: Trigger raycast collision events [REVISED from G4.06]
  - Implement after understanding types (G3.09)
G4.15: Control model animations ✓ (was G4.07)
  G4.15.01: Add and control avatar animations ✓ (was G4.07.01)
G4.16: Add 3D text for labels ✓ (was G4.08)
G4.17: Pick 3D objects with mouse/touch [MOVED from G5.02.01]
G4.18: Drag 3D objects [MOVED from G5.02.02]
G4.19: Add fog effects [MOVED from G5.06]
G4.20: Change sky background [MOVED from G5.06.02]
G4.21: Add joystick controls [MOVED from G5.10]
G4.22: Debug simple 3D scripts [NEW]
  - Show axis, bounding box, trace with say blocks
```
**Changes:** +13 skills, better scaffolding, clear progression

### Grade 5: Physics & Effects (10-12 skills) - FOCUSED ON PHYSICS
```
G5.01: Initialize 3D physics world ✓
G5.02: Attach static/dynamic physics bodies ✓
G5.03: Detect physics collisions for collectibles [CLARIFIED]
  - Physics collision type (not raycast/overlap)
G5.04: Use nested loops to arrange objects ✓ [ADD inter-topic dependencies]
  G5.04.01: Copy by matrix ✓
  G5.04.02: Mirror/rotation copy ✓
G5.05: Apply detailed textures and PBR materials ✓
G5.06: Import external 3D models from URLs [MOVED from G4.04]
G5.07: Add prebuilt particle emitters [SPLIT]
  - Fire, smoke, rain, snow only
G5.08: Apply forces and impulses ✓
  G5.08.01: Remove objects and reset scenes ✓ [FIX dependencies]
G5.09: Adjust camera distance/angles dynamically ✓
G5.10: Enable shadows from lights [FIX dependencies - remove physics]
G5.11: Use distance sensors [MOVED from G4.05.01, FIX dependencies]
```
**Changes:** -2 skills (moved to G4), focused on physics, split particles

### Grade 6: Advanced Interaction (10-12 skills) - COHERENT THEME
```
G6.01: Set up collision groups ✓
G6.02: Add fixed constraints [SPLIT from old G6.06]
  G6.02.01: Create parent-child hierarchies ✓ (was G6.06.01)
G6.03: Create custom particle emitters [SPLIT from G5.07]
  - Advanced configuration with 6+ parameters
G6.04: Implement mouse look camera ✓
G6.05: Trigger advanced visual effects ✓
G6.06: Refactor simple object creation [NEW - basic version]
  - Repeated add object → repeat loop
G6.07: Refactor complex scripts [REVISED from old G6.03]
  - Nested loops, custom blocks
G6.08: Debug complex 3D scenes ✓ [CLARIFIED process]
  - Identify bug → hypothesis → tools → trace → fix → verify
G6.09: Add hinge constraints with motors [SPLIT from old G6.06]
G6.10: Understand when to use physics vs animation [NEW - transition]
```
**Changes:** Theme = "Advanced Interaction & Effects", better coherence

### Grade 7: Gameplay Mechanics (7-8 skills) - FOCUSED
```
G7.01: Implement waypoint NPC movement ✓ [FIX dependencies - add movement prereq]
G7.02: Design collision response (bounce/slide) ✓
G7.03: Use 3D distance calculations ✓
G7.04: Implement physics-based puzzle ✓
G7.05: Script camera transitions/cutscenes ✓
G7.06: Build avatar state machine [REVISED - differentiate from G4.15.01]
  - Switch animations based on state (walk→run→jump→idle)
G7.07: Add spatial audio positioning [NEW - if space allows]
```
**Changes:** Clarified theme = "Gameplay Mechanics (AI, puzzles, cutscenes)"

### Grade 8: Systems & Optimization (5-6 skills) - FOCUSED
```
G8.01: Load level layouts from data ✓ [FIX dependencies - remove physics]
G8.02: Multiple cameras for split-screen ✓ [FIX dependencies - simplify]
G8.03: Optimize 3D game performance ✓
G8.04: Analyze quality/performance trade-offs ✓ [CLARIFIED criteria]
  - "Identify 3+ design choices, explain trade-off for each"
G8.05: Use car physics for vehicles [KEEP or move to G7]
G8.06: Advanced optimization techniques [NEW - if needed]
  - LOD, occlusion, instancing, GPU particles
```
**Changes:** Clarified theme = "Systems & Optimization", clear criteria

---

## SKILLS COUNT COMPARISON

| Grade | Before | After | Change | Notes |
|-------|--------|-------|--------|-------|
| GK    | 1      | 3      | +2     | Added shape identification activities |
| G1    | 1      | 3      | +2     | Added view construction activities |
| G2    | 1      | 3      | +2     | Added view drawing/prediction |
| G3    | 8      | 10-11  | +2-3   | Split complex, added collision understanding |
| G4    | 9      | 16-22  | +7-13  | Major expansion with fundamentals from G5 |
| G5    | 14     | 10-12  | -2-4   | Focused on physics, moved basics to G4 |
| G6    | 7      | 10-12  | +3-5   | Coherent interaction theme, split skills |
| G7    | 6      | 7-8    | +1-2   | Gameplay mechanics focused |
| G8    | 5      | 5-6    | +0-1   | Systems & optimization focused |
| **TOTAL** | **61** | **73-86** | **+12-25** | Better scaffolding, clearer progression |

**Note:** Final count depends on how many new skills are added vs. existing skills split.

---

## DEPENDENCY CHAIN EXAMPLES

### BEFORE: Complex Camera Chain (5 steps)
```
G3.06 (textures) ← has T07.G3.03 (loops) dependency
  ↓
G3.07 (player movement) ← blocked
  ↓
G4.03 (following camera) ← requires movement
  ↓
G5.09 (dynamic camera) ← requires following
  ↓
G7.05 (cutscenes) ← requires dynamic
```
**Problem:** Can't learn cameras until mastering textures, loops, movement

### AFTER: Simplified Camera Progression (3 steps)
```
G4.01 (camera basics) ← independent
  ↓
G4.12 (following camera) ← simplified, no player movement needed
  ↓
G5.09 (dynamic camera) ← smooth adjustment
  ↓
G7.05 (cutscenes) ← choreography
```
**Improvement:** Clean progression, no unrelated prerequisites

### BEFORE: Collision Confusion (All at once)
```
G4.05.02 (understand 3 collision types)
  ↓ (same grade)
G4.06 (implement raycast collision)
```
**Problem:** Understanding and implementation simultaneous, no hands-on before theory

### AFTER: Collision Scaffolding (Step by step)
```
G3.09 (understand 3 types - conceptual)
  ↓
G4.08 (detect overlap - simple hands-on)
  ↓
G4.14 (implement raycast - practical)
  ↓
G5.03 (use physics collision - with physics engine)
```
**Improvement:** Concept → simple practice → advanced implementation → physics integration

---

## SKILL COMPLEXITY DISTRIBUTION

### BEFORE (blocks per skill)
```
G3.03: 1 block    ← TOO SIMPLE
G3.04: 11 blocks  ← TOO COMPLEX
G3.06: 2 blocks with 13 params total ← TOO COMPLEX
G4.02: 3 blocks with 20+ params total ← TOO COMPLEX
G4.04: 2 blocks very different ← TOO BROAD
G5.07: 7 blocks ← TOO COMPLEX
Average: 1-11 blocks (high variance)
```

### AFTER (blocks per skill)
```
G3.03: 3 blocks (scene + axis + background) ← FOCUSED
G3.04: 3 blocks (box, sphere, cylinder) ← FOCUSED
G3.06: 1 block (color only) ← FOCUSED
G4.03: 1 block (ambient light only) ← FOCUSED
G4.13: 1 block (prebuilt models only) ← FOCUSED
G5.07: 1 block (prebuilt emitters only) ← FOCUSED
Average: 1-3 blocks (low variance)
```
**Improvement:** Consistent complexity, single-focused skills

---

## KEY IMPROVEMENTS SUMMARY

### ✅ Fixed Dependency Violations
- No more X-2 rule violations (was 12)
- Camera progression simplified
- Collision understanding before implementation
- Basic UI independent of physics

### ✅ Proper Scaffolding
- Added 5+ fundamental skills (camera basics, simple collision, basic animation, textures, colors)
- Early grades expanded (3→9 skills)
- G4 strengthened as foundation (9→16+ skills)
- G5 focused on physics (14→10-12 skills)

### ✅ Single-Focused Skills
- Split 6 overly complex skills
- Each skill teaches 1-3 blocks
- Clear learning objective per skill

### ✅ Assessable Descriptions
- Concrete criteria added
- "Short script" = 3-5 blocks
- "Explain trade-offs" = identify 3+ choices
- Debugging process specified

### ✅ Coherent Themes
- G3: Fundamentals (shapes, position, rotation, movement)
- G4: Scene Building (cameras, lights, models, collision, interaction)
- G5: Physics & Effects (physics engine, particles, advanced rendering)
- G6: Advanced Interaction (constraints, hierarchies, custom effects, optimization)
- G7: Gameplay Mechanics (AI, puzzles, cutscenes)
- G8: Systems & Optimization (data-driven, performance, complex simulation)

---

## VALIDATION CHECKLIST

After implementing fixes, verify:

- [ ] No skill depends on skills >2 positions later (X-2 rule)
- [ ] Each skill focuses on 1-3 related blocks
- [ ] All descriptions have concrete, assessable criteria
- [ ] All dependencies are justified and necessary
- [ ] Each grade has coherent theme
- [ ] Progression from simple → complex within each grade
- [ ] Inter-topic dependencies documented
- [ ] Early grades (GK-G2) have sufficient unplugged activities
- [ ] G3-G4 provide solid coding fundamentals
- [ ] G5-G8 progress through advanced topics logically

---

**Comparison Document Created:** 2025-11-23
**Ready for implementation:** Yes ✓

_This comparison shows current structure with issues vs. recommended structure addressing all Phase 1 optimization criteria._
