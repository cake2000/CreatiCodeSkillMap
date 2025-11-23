# T18 (3D Worlds & Games) - Phase 1 Comprehensive Analysis Report

**Date:** 2025-11-23
**Total Skills Analyzed:** 61 (GK: 1, G1: 1, G2: 1, G3: 8, G4: 9, G5: 14, G6: 7, G7: 6, G8: 5)
**3D Blocks Available:** 239 blocks across 7 categories

---

## EXECUTIVE SUMMARY

T18 is generally well-structured with good progression from unplugged spatial concepts (GK-G2) through basic 3D programming (G3-G4) to advanced physics and optimization (G5-G8). However, there are **26 HIGH PRIORITY issues** and **15 MEDIUM PRIORITY issues** that need attention.

**Key Findings:**
- **CRITICAL:** Multiple intra-topic dependency violations (X-2 rule violations)
- **HIGH:** Several skills are too broad/complex and need decomposition
- **HIGH:** Missing fundamental skills in early grades (G3-G4)
- **MEDIUM:** Some skill descriptions lack concrete assessment criteria
- **LOW:** Minor coherence issues (overlaps, organization)

---

## HIGH PRIORITY ISSUES (26 total)

### CATEGORY 1: INTRA-TOPIC DEPENDENCY VIOLATIONS (X-2 Rule)

#### Issue H1: G3.07 depends on G4+ concepts
**Skill:** T18.G3.07 - Move a 3D player with keyboard input
**Problem:** Depends on T18.G3.06 which uses advanced material/texture blocks. This skill should come earlier since basic movement is fundamental.
**Violation:** Conceptually depends on understanding not yet taught in G3.
**Fix:** Move G3.07 earlier (after G3.05 position/rotation), simplify G3.06, or remove dependency.

**Priority:** HIGH
**Impact:** Breaks logical learning flow for basic 3D movement

---

#### Issue H2: G4.03 camera depends on G4.01 scene composition
**Skill:** T18.G4.03 - Create a following or orbiting camera
**Problem:** Also depends on T18.G3.07 (player movement) which depends on G3.06. Camera following requires understanding of both scene composition AND player movement, creating a long dependency chain.
**Violation:** Camera skills should be introduced independently of complex scene composition.
**Fix:** Create simpler camera skill earlier; make G4.03 focus only on camera configuration, not player following.

**Priority:** HIGH
**Impact:** Students can't learn camera basics until they master scene composition

---

#### Issue H3: G4.05.01 distance sensors require G3.07 player movement
**Skill:** T18.G4.05.01 - Use distance sensors to detect obstacles
**Problem:** Depends on T18.G3.07 which has problematic dependencies. Distance sensors are a fundamental detection mechanism that shouldn't require mastery of player movement.
**Violation:** Sensing should be independent of movement mechanics.
**Fix:** Introduce distance sensors earlier with static objects, then apply to moving players later.

**Priority:** HIGH
**Impact:** Cannot learn fundamental detection without completing movement chain

---

#### Issue H4: G4.05.02 requires understanding THREE collision types
**Skill:** T18.G4.05.02 - Understand collision detection types
**Problem:** Depends on T18.G4.05.01 (distance sensors) but actually teaches THREE different collision systems (raycast, overlap, physics). This is conceptual understanding, not coding, yet placed late in G4.
**Violation:** Fundamental concept taught too late; should precede practical collision use.
**Fix:** Split into separate skills: (1) Understand collision types (conceptual, G3), (2) Use raycast collision (G4), (3) Use overlap detection (G4), (4) Use physics collision (G5 with physics intro).

**Priority:** HIGH
**Impact:** Students use collision without understanding when to use which type

---

#### Issue H5: G4.06 collision implementation before understanding types
**Skill:** T18.G4.06 - Trigger events when 3D objects touch (raycast collision)
**Problem:** Implements raycast collision and depends on G4.05.02 (understanding types), but also depends on G3.07 player movement and G4.05.02 which themselves have long chains.
**Violation:** Cannot implement collision properly without first understanding types.
**Fix:** After splitting G4.05.02, make G4.06 depend only on the "understand raycast collision" skill, not the movement chain.

**Priority:** HIGH
**Impact:** Students implement collision without conceptual foundation

---

#### Issue H6: G5.02.01 picking should precede physics
**Skill:** T18.G5.02.01 - Pick 3D objects with mouse or touch
**Problem:** Placed in G5 under a physics skill (G5.02) but only depends on G4.01 (scene composition). Object picking is fundamental interaction that doesn't require physics at all.
**Violation:** Mis-categorized under physics; should be G4 skill.
**Fix:** Move to G4 as independent interaction skill (G4.X - Pick 3D objects with mouse).

**Priority:** HIGH
**Impact:** Basic interaction unnecessarily gated behind physics

---

#### Issue H7: G5.02.02 dragging depends on picking
**Skill:** T18.G5.02.02 - Drag 3D objects with mouse or touch
**Problem:** Correctly depends on G5.02.01 (picking) but both are miscategorized under physics parent skill G5.02.
**Violation:** Both picking and dragging are non-physics interactions.
**Fix:** Move both G5.02.01 and G5.02.02 to G4 as G4.X and G4.X+1.

**Priority:** HIGH
**Impact:** Fundamental UI interactions blocked by physics prerequisite

---

#### Issue H8: G5.04 nested loops only depends on G4.01
**Skill:** T18.G5.04 - Use nested loops to arrange 3D objects in grids
**Problem:** Only depends on T18.G4.01 (scene composition) but this is a fundamental programming pattern that students should learn earlier. Nested loops are taught in T04/T07 at G3-G4 level.
**Violation:** Advanced programming pattern taught without proper scaffolding; missing inter-topic dependency on T04/T07 loop skills.
**Fix:** Add inter-topic dependencies on T04.G3.02 (nested loops conceptual) or T07.G4.X (nested loops practical). Consider whether this belongs in G4 instead of G5.

**Priority:** HIGH
**Impact:** Students encounter nested loops without programming foundation

---

#### Issue H9: G6.02 debugging requires G5.04 nested loops
**Skill:** T18.G6.02 - Debug a 3D scene by analyzing script flow
**Problem:** Depends on T18.G5.04 (nested loops) but debugging skills should be introduced much earlier. Students should debug simple scripts before complex nested loops.
**Violation:** Debugging gated behind advanced programming patterns.
**Fix:** Create earlier debugging skill for simple 3D scripts (G4), then advanced debugging for complex scripts (G6).

**Priority:** HIGH
**Impact:** Cannot learn debugging until mastering nested loops

---

#### Issue H10: G6.03 refactoring depends on nested loops + custom blocks
**Skill:** T18.G6.03 - Refactor repeated 3D object creation into loop/function
**Problem:** Correctly depends on T18.G5.04 (nested loops) and T11.G4.01 (custom blocks) BUT students should refactor simple repetition before complex nested loops.
**Violation:** Refactoring taught only for advanced patterns.
**Fix:** Create G4-level refactoring skill for simple repetition (repeated add object → repeat loop), then G6 for advanced (nested loops, functions).

**Priority:** HIGH
**Impact:** Missing foundational refactoring skill

---

#### Issue H11: G7.01 waypoint movement only depends on lists
**Skill:** T18.G7.01 - Implement waypoint-based NPC movement
**Problem:** Depends on T10.G5.01 (lists) but doesn't depend on any prior T18 movement skills. Students should master basic movement (G3.07) before NPC waypoints.
**Violation:** Missing intra-topic dependency on movement fundamentals.
**Fix:** Add dependency on T18.G3.07 (basic movement) or create intermediate NPC movement skill in G5-G6.

**Priority:** HIGH
**Impact:** Students implement NPC movement without movement fundamentals

---

#### Issue H12: G8.02 split-screen depends on G7.05 cutscenes + G8.01 level data
**Skill:** T18.G8.02 - Use multiple cameras for split-screen or UI views
**Problem:** Depends on T18.G7.05 (camera transitions/cutscenes) and T18.G8.01 (level data loading), creating unnecessary complexity. Split-screen is a display technique that doesn't require cutscene skills or data-driven levels.
**Violation:** Over-constrained dependency; should depend only on basic camera skills.
**Fix:** Make G8.02 depend on T18.G4.03 (camera basics) and T18.G5.09 (dynamic camera control), remove cutscene/level data dependencies.

**Priority:** HIGH
**Impact:** Cannot learn split-screen without mastering cutscenes

---

### CATEGORY 2: SKILLS TOO BROAD/COMPLEX (Need Breaking Down)

#### Issue H13: G3.03 - Initialize 3D scene is too simple
**Skill:** T18.G3.03 - Initialize a 3D scene with default lighting
**Problem:** Only teaches ONE block (`initialize 3D scene`) with two parameters. This is trivial and doesn't warrant a full skill.
**Fix:** Combine with G3.04 (add primitives) OR expand to include basic scene setup (initialize + show axis + set background color).

**Priority:** HIGH
**Impact:** Unnecessarily granular, wastes skill slot

---

#### Issue H14: G3.04 - Add primitives covers TOO MANY shapes
**Skill:** T18.G3.04 - Add primitive shapes with 3D blocks
**Problem:** Description lists box, sphere, cylinder AND mentions "plane, torus, cone, capsule, tube, stairs, and other primitives" but only shows 3 block examples. Too broad.
**Fix:** Split into:
- G3.04: Add basic primitives (box, sphere, cylinder) - the 3 shown blocks
- G4.X: Add specialized primitives (plane, cone, capsule, tube, torus, stairs)

**Priority:** HIGH
**Impact:** Overwhelming for G3 students; unclear scope

---

#### Issue H15: G4.02 - Lighting covers THREE light types
**Skill:** T18.G4.02 - Configure ambient and directional lighting
**Problem:** Description covers ambient (hemispheric), directional, AND spot lights with complex parameters. Too much for one skill.
**Fix:** Split into:
- G4.02: Add ambient light (hemispheric only)
- G4.02.X: Add directional light
- G4.02.Y: Add spot light (or move to G5)
Keep G4.02.01 (manage lights) and G4.02.02 (point lights) as-is but adjust dependencies.

**Priority:** HIGH
**Impact:** Students overwhelmed by three different light types at once

---

#### Issue H16: G4.04 - Import models covers TWO different systems
**Skill:** T18.G4.04 - Place imported or premade 3D models
**Problem:** Teaches BOTH CreatiCode prebuilt models AND external GLB/GLTF imports. These are different complexity levels.
**Fix:** Split into:
- G4.04: Use CreatiCode prebuilt models (simpler, library-based)
- G5.X: Import external 3D models from URLs (more advanced)

**Priority:** HIGH
**Impact:** Mixing library models with URL imports confuses students

---

#### Issue H17: G5.07 - Particle emitters covers prebuilt AND custom
**Skill:** T18.G5.07 - Add particle emitters for visual effects
**Problem:** Teaches BOTH prebuilt emitters (simple) AND custom emitters with 6 configuration blocks. Massive scope.
**Fix:** Split into:
- G5.07: Add prebuilt particle emitters (fire, smoke, rain, snow)
- G6.X: Create custom particle emitters (advanced configuration)

**Priority:** HIGH
**Impact:** Trying to teach simple and complex particle systems simultaneously

---

#### Issue H18: G6.06 - Constraints covers hinge AND fixed types
**Skill:** T18.G6.06 - Use constraints to connect physics bodies
**Problem:** Teaches TWO constraint types (hinge for rotation, fixed for rigid) plus hinge motor configuration. Complex topic.
**Fix:** Split into:
- G6.06: Add fixed constraints between objects (simpler)
- G7.X: Add hinge constraints with motors (more complex)

**Priority:** HIGH
**Impact:** Students must learn two different constraint systems at once

---

### CATEGORY 3: MISSING FUNDAMENTAL SKILLS

#### Issue H19: Missing basic camera skill in G3
**Gap:** No basic camera introduction before G4.03 (following/orbiting camera)
**Problem:** Students jump from no camera knowledge to complex following cameras with 7+ parameters.
**Fix:** Add G3.X or G4.01: "Understand camera position and orientation" - introduce camera as viewpoint, use `show axis` to understand camera direction, maybe add simple orbit camera with minimal parameters.

**Priority:** HIGH
**Impact:** Students lack camera fundamentals before advanced cameras

---

#### Issue H20: Missing basic collision skill in G3-G4
**Gap:** No simple collision before G4.05.02 (three collision types) and G4.06 (raycast implementation)
**Problem:** Related to H4 - students need hands-on collision experience before learning three systems.
**Fix:** Add G4.X: "Detect when objects overlap" - simple overlap detection using `broadcast when objects overlap` before teaching all three collision types.

**Priority:** HIGH
**Impact:** No gentle introduction to collision concepts

---

#### Issue H21: Missing basic animation skill
**Gap:** No 3D object animation before G4.05 (scenery animations with loops)
**Problem:** Students jump from static objects (G3-G4.04) to looping animations with complex timing.
**Fix:** Add G4.X: "Animate a 3D object" - simple position or rotation change over time (single move/rotate block with timing, no loops).

**Priority:** HIGH
**Impact:** Missing fundamental animation concept

---

#### Issue H22: Missing loop application skill
**Gap:** G4.05 jumps to "animate scenery with loops" but students haven't applied loops to 3D yet
**Problem:** Students learn loops in T07.G3 but first T18 loop application is complex scenery animation in G4.
**Fix:** Either add G3.X "Use repeat loop to create multiple objects" (simple stamping) OR clarify that G4.05 is intentionally the first loop application and ensure T07.G3 dependencies are clear.

**Priority:** HIGH
**Impact:** First loop application is complex animation, not simple repetition

---

#### Issue H23: Missing basic texture skill
**Gap:** G3.06 teaches textures but only as part of "colors or textures" with complex PBR parameters
**Problem:** `update color diffusion [COLOR] emission [COLOR] roughness (R) brightness (B) remove texture [DOREMOVE v] area [AREATYPE v]` has 6 parameters; texture block has 7 parameters. Too complex for first texture skill.
**Fix:** Split G3.06 into:
- G3.06: Change object colors (color block only)
- G4.X: Apply textures to objects (texture block only)
- G5.05 remains as "detailed textures/materials" with PBR

**Priority:** HIGH
**Impact:** First exposure to textures is overwhelming

---

### CATEGORY 4: UNCLEAR/UNASSESSABLE DESCRIPTIONS

#### Issue H24: G3.08 - "Trace a short 3D script" lacks concrete criteria
**Skill:** T18.G3.08 - Trace a short 3D script to predict positions
**Problem:** Says "short 3D script" but doesn't specify how many blocks, which blocks, or what constitutes "short."
**Fix:** Add concrete criteria: "Students read a 3-5 block script using move to x y z, rotate to angle, and turn N degrees blocks and predict final position/orientation by drawing or describing the result."

**Priority:** HIGH
**Impact:** Cannot create consistent assessments

---

#### Issue H25: G8.04 - Analysis skill too vague
**Skill:** T18.G8.04 - Analyze trade-offs between visual quality and performance
**Problem:** "Review completed project and explain design choices" - what constitutes sufficient explanation? What specific trade-offs?
**Fix:** Add concrete criteria: "Students identify at least 3 design choices (physics on/off, texture resolution, particle count, shadow quality) and explain the trade-off for each (why chosen, what was sacrificed, impact on frame rate)."

**Priority:** HIGH
**Impact:** Subjective skill without clear success criteria

---

#### Issue H26: G6.02 - Debugging description lacks process
**Skill:** T18.G6.02 - Debug a 3D scene by analyzing script flow
**Problem:** Lists debugging tools (show axis, show bounding box, debug parameters) but doesn't specify debugging process or outcomes.
**Fix:** Add concrete process: "Students identify bug, form hypothesis about cause, use debugging tools (show axis, show bounding box, physics debug) to gather evidence, trace script execution with console/say blocks, fix issue, and verify solution."

**Priority:** HIGH
**Impact:** Unclear what "debugging" means in practice

---

## MEDIUM PRIORITY ISSUES (15 total)

### CATEGORY 5: DEPENDENCY IMPROVEMENTS

#### Issue M1: G3.04.01 rotation should depend on G3.04 shapes
**Skill:** T18.G3.04.01 - Rotate objects around axes
**Current:** Depends on T18.G3.04 (add primitives) ✓
**Problem:** This is correct, but the skill description says "orient objects in 3D space" which overlaps with G3.05 "position shapes using coordinates."
**Fix:** Clarify distinction: G3.04.01 = rotation/orientation, G3.05 = position/location. Ensure descriptions are distinct.

**Priority:** MEDIUM
**Impact:** Minor overlap in descriptions

---

#### Issue M2: G3.06 requires loops but doesn't depend on T07
**Skill:** T18.G3.06 - Change shape colors or textures
**Current:** Depends on T18.G3.05 (position) and T07.G3.03 (forever loop)
**Problem:** Why does changing color require loops? This dependency seems odd unless skill includes animation.
**Fix:** If G3.06 is static color/texture changes, remove T07.G3.03 dependency. If it includes animated color changes, clarify in description.

**Priority:** MEDIUM
**Impact:** Possibly unnecessary dependency

---

#### Issue M3: G4.01 multi-part scene depends on variable display?
**Skill:** T18.G4.01 - Compose a multi-part 3D scene with primitives
**Current:** Depends on T18.G3.08 (trace scripts) and T09.G3.01.04 (display variable on stage)
**Problem:** Why does scene composition require variable display? Unclear connection.
**Fix:** Remove T09.G3.01.04 dependency unless skill requires tracking object counts/positions in variables (not mentioned in description).

**Priority:** MEDIUM
**Impact:** Unclear dependency rationale

---

#### Issue M4: G4.04.01 scale depends on import models
**Skill:** T18.G4.04.01 - Scale and resize objects
**Current:** Depends on T18.G4.04 (import models)
**Problem:** Scaling works on ALL objects (primitives, models). Why gate behind imports?
**Fix:** Make G4.04.01 depend on G3.04 (primitives) instead, so students can scale primitives before learning imports. Scaling imported models can be mentioned in description but isn't a prerequisite.

**Priority:** MEDIUM
**Impact:** Unnecessarily limiting scaling to imported models

---

#### Issue M5: G5.06.01 shadows require physics?
**Skill:** T18.G5.06.01 - Enable shadows from lights
**Current:** Depends on T18.G4.02.02 (point lights) and T18.G5.02 (physics bodies)
**Problem:** Shadows don't require physics. Any object can cast/receive shadows.
**Fix:** Remove T18.G5.02 dependency. Keep T18.G4.02.02 (point lights) and add T18.G4.02 (ambient/directional lights) since those cast shadows too.

**Priority:** MEDIUM
**Impact:** Incorrectly linking visual effects to physics

---

#### Issue M6: G5.08.01 remove objects depends on physics collision
**Skill:** T18.G5.08.01 - Remove objects and reset scenes
**Current:** Depends on T18.G5.03 (physics collision for collectibles)
**Problem:** Removing objects doesn't require physics. Students should learn `remove object` earlier.
**Fix:** Make G5.08.01 depend on G4.06 (basic collision) or G4.01 (scene composition) instead. Removing objects is fundamental, not physics-specific.

**Priority:** MEDIUM
**Impact:** Basic object management gated behind physics

---

#### Issue M7: G7.06 avatar animation control has duplicate skill
**Skill:** T18.G7.06 - Control avatar animations with user input
**Current:** Depends on T18.G4.07.01 (add and control avatar animations)
**Problem:** G4.07.01 already teaches "start animation [NAME] looping speed ratio to play animations like walking, jumping, idle, syncing with user input or game events." G7.06 description is nearly identical: "start animation based on user input or game state, syncing character movement with visual animation."
**Fix:** Either (1) remove G7.06 as duplicate, OR (2) differentiate: G4.07.01 = play single animation, G7.06 = switch between multiple animations based on state machine (walk→run→jump→idle).

**Priority:** MEDIUM
**Impact:** Significant duplication between skills

---

#### Issue M8: G8.01 level data missing data structure dependency
**Skill:** T18.G8.01 - Load level layouts from list data
**Current:** Depends on T18.G7.04 (physics puzzles) and T10.G6.02 (2D lists)
**Problem:** Why depend on physics puzzles? Level loading is data structure skill, not physics.
**Fix:** Remove T18.G7.04 dependency. Keep T10.G6.02 (2D lists) and possibly add T10.G5.01 (basic lists) or T10.G5.X (list iteration).

**Priority:** MEDIUM
**Impact:** Incorrect dependency on physics puzzles

---

### CATEGORY 6: SKILL ORGANIZATION/COHERENCE

#### Issue M9: G3.01 and G3.02 are conceptual, not coding
**Skills:** T18.G3.01 (Interpret 3D axis) and T18.G3.02 (Match camera views)
**Problem:** Both are unplugged activities (reading diagrams, matching images) yet depend on T06.G3.01 (green flag script) and T03.G2.01/G3.03 (storyboarding). Mismatch between unplugged and coding dependencies.
**Fix:** Either (1) make G3.01/G3.02 fully unplugged with no dependencies, OR (2) convert to coding activities (use show axis, position camera, take screenshots).

**Priority:** MEDIUM
**Impact:** Unclear whether activities are unplugged or coding-based

---

#### Issue M10: Sub-skill numbering inconsistent
**Problem:** Some skills use .01, .02 sub-numbering (G3.04.01, G4.02.01, G4.04.01, G5.02.01, G5.04.01, G5.06.01, G6.06.01) but placement is inconsistent. G4.05.01 and G4.05.02 come BEFORE G4.06, but G4.04.01 comes AFTER several G4.05+ skills.
**Fix:** Reorganize sub-skills to appear immediately after parent skill in sequence. Example: G4.02 → G4.02.01 → G4.02.02 → G4.03 (not G4.02 → ... → G4.02.01 later).

**Priority:** MEDIUM
**Impact:** Confusing skill order

---

#### Issue M11: Missing progression from G4 to G5
**Problem:** G4 ends with animation, text, and collision. G5 starts with physics initialization. There's a conceptual jump from "building scenes" to "physics simulation."
**Fix:** Consider adding G4.X transition skill: "Understand when to use physics vs. manual animation" (conceptual) to bridge the gap.

**Priority:** MEDIUM
**Impact:** Abrupt topic shift

---

#### Issue M12: G5.05 detailed textures comes after G5.06 fog?
**Skills:** G5.05 (Apply detailed textures), G5.06 (Add fog), G5.09 (Camera distance)
**Problem:** Numbering suggests G5.05 → G5.06 → G5.09, but G5.09 should come after G5.06 based on dependencies. Also, G5.05 relates to G3.06 textures but is separated by many skills.
**Fix:** Renumber to group related skills: textures together, atmospheric effects together, camera skills together.

**Priority:** MEDIUM
**Impact:** Related skills scattered across grade level

---

#### Issue M13: G6 mixing debugging, refactoring, interaction, and effects
**Problem:** G6 has debugging (G6.02), refactoring (G6.03), mouse look camera (G6.04), visual effects (G6.05), constraints (G6.06), hierarchies (G6.06.01). No clear theme.
**Fix:** Consider regrouping: G6 = advanced interaction (mouse look, picking/dragging moved from G5, constraints), G7 = optimization (debugging, refactoring, effects management).

**Priority:** MEDIUM
**Impact:** Thematic incoherence

---

#### Issue M14: G7/G8 have overlapping "advanced" themes
**Problem:** G7 has waypoints, collision response, distance calculations, puzzles, cutscenes, avatar control. G8 has level data, split-screen, performance optimization, trade-off analysis, car physics. Both are "advanced topics" without clear distinction.
**Fix:** Clarify themes: G7 = advanced gameplay mechanics (AI, puzzles, cutscenes), G8 = systems & optimization (level loading, performance, multi-view, complex simulation).

**Priority:** MEDIUM
**Impact:** Unclear distinction between G7 and G8

---

#### Issue M15: Car physics (G8.05) feels disconnected
**Skill:** T18.G8.05 - Use car physics for vehicle simulation
**Problem:** Only G8 skill that teaches new mechanic (car simulation). Rest of G8 is about systems/optimization. Car physics is similar complexity to G6.06 constraints or G7.02 collision response.
**Fix:** Either (1) move to G7 as advanced physics application, OR (2) add more G8 simulation skills to balance (water buoyancy, ragdolls, cloth).

**Priority:** MEDIUM
**Impact:** Lone mechanic skill in optimization-focused grade

---

## LOW PRIORITY ISSUES (8 total)

### CATEGORY 7: MINOR DESCRIPTION IMPROVEMENTS

#### Issue L1: G3.03 description mentions "as hidden" parameter
**Skill:** T18.G3.03 - Initialize a 3D scene with default lighting
**Description:** "The `as hidden` parameter controls whether the scene starts visible or off-screen."
**Problem:** This detail might confuse beginners. Most scenes should start visible.
**Fix:** Simplify: "Students initialize 3D scene with `initialize 3D scene [SCENETYPE]` block, choosing scene type like Empty, Grass Land, or City. Advanced: use 'as hidden' parameter for off-screen setup."

**Priority:** LOW
**Impact:** Minor terminology confusion

---

#### Issue L2: G3.05 says "Y controls forward-backward"
**Skill:** T18.G3.05 - Position shapes using x/y/z coordinates
**Description:** "X controls left-right, Y controls forward-backward, Z controls up-down"
**Problem:** CreatiCode 3D axis orientation can vary by camera. This is camera-dependent.
**Fix:** Clarify: "Students learn that in CreatiCode's default camera view: X = left/right, Y = forward/backward, Z = up/down. They position objects and observe how changing each coordinate affects placement."

**Priority:** LOW
**Impact:** Possible confusion with camera changes

---

#### Issue L3: G4.07 and G4.07.01 descriptions very similar
**Skills:** G4.07 (Control model animations) and G4.07.01 (Add and control avatar animations)
**Problem:** G4.07 teaches `start model animation` for GLB/GLTF models. G4.07.01 teaches `add avatar` + `add animations` + `start animation`. Descriptions overlap.
**Fix:** Clarify: G4.07 = animations embedded in imported models (already in file), G4.07.01 = avatars with animation library (load from library).

**Priority:** LOW
**Impact:** Minor conceptual overlap

---

#### Issue L4: G5.06 fog placement
**Skill:** T18.G5.06 - Add fog effects for atmosphere
**Problem:** Depends on T18.G3.03 (scene initialization) only, but placed in G5. Could be G4 skill.
**Fix:** Either move to G4 as atmospheric effect, or keep in G5 as "advanced atmospheric effects" and add dependency on G4.01 (scene composition) to ensure students have complete scenes before adding fog.

**Priority:** LOW
**Impact:** Slightly early for placement

---

#### Issue L5: G5.06.02 sky background only depends on scene init
**Skill:** T18.G5.06.02 - Change sky background
**Problem:** Placed in G5 but only depends on G3.03 (scene init). Very simple skill (`set sky [SKYTYPE]`).
**Fix:** Move to G4 as basic scene customization.

**Priority:** LOW
**Impact:** Over-graded for complexity

---

#### Issue L6: G5.10 joystick controls placement
**Skill:** T18.G5.10 - Add on-screen joystick controls
**Problem:** Depends on T18.G3.07 (player movement) but placed in G5 after physics. Joysticks don't require physics.
**Fix:** Renumber as G4.X (after player movement is fixed per H1).

**Priority:** LOW
**Impact:** Minor placement issue

---

#### Issue L7: GK, G1, G2 only have 1 skill each
**Skills:** T18.GK.01, T18.G1.01, T18.G2.01
**Problem:** Only 1 unplugged skill per grade. Seems sparse for 3 grade levels.
**Fix:** Consider adding more unplugged spatial skills:
- GK.02: Identify shapes in 3D models
- G1.02: Build shape from multiple views
- G2.02: Draw missing view from 3D object

**Priority:** LOW
**Impact:** Sparse early progression

---

#### Issue L8: Block syntax in descriptions inconsistent
**Problem:** Some descriptions show full block syntax with parameters (e.g., G3.03, G3.04), others just mention block names (e.g., G3.07 "if key pressed").
**Fix:** Standardize: always show block name with key parameters in descriptions for clarity.

**Priority:** LOW
**Impact:** Minor consistency issue

---

## SUMMARY BY ISSUE TYPE

| Issue Type | High | Medium | Low | Total |
|------------|------|--------|-----|-------|
| Intra-Topic Dependencies | 12 | 0 | 0 | 12 |
| Skills Too Broad | 6 | 0 | 0 | 6 |
| Missing Skills | 5 | 0 | 1 | 6 |
| Unclear Descriptions | 3 | 0 | 4 | 7 |
| Dependency Issues | 0 | 8 | 0 | 8 |
| Organization/Coherence | 0 | 7 | 3 | 10 |
| **TOTAL** | **26** | **15** | **8** | **49** |

---

## RECOMMENDED ACTION PLAN

### Phase 1: Fix HIGH Priority Issues (26 issues)

**Week 1: Fix Intra-Topic Dependencies (H1-H12)**
1. Reorganize G3.06-G3.07 dependency chain
2. Simplify camera progression (H2, H19)
3. Split collision skills properly (H3-H5, H20)
4. Move picking/dragging to G4 (H6-H7)
5. Add loop scaffolding (H8, H22)
6. Fix debugging dependencies (H9)
7. Add refactoring progression (H10)
8. Fix NPC movement dependencies (H11)
9. Simplify split-screen dependencies (H12)

**Week 2: Split Complex Skills (H13-H18)**
1. Combine/expand scene init (H13)
2. Split primitive shapes (H14)
3. Split lighting types (H15)
4. Split model import types (H16)
5. Split particle systems (H17)
6. Split constraint types (H18)

**Week 3: Add Missing Skills & Clarify Descriptions (H19-H26)**
1. Add basic camera skill (H19)
2. Add simple collision skill (H20)
3. Add basic animation skill (H21)
4. Clarify loop application (H22)
5. Split color/texture skills (H23)
6. Add concrete criteria to G3.08 (H24)
7. Add concrete criteria to G8.04 (H25)
8. Add debugging process to G6.02 (H26)

### Phase 2: Address MEDIUM Priority Issues (15 issues)
- Fix dependency inconsistencies (M1-M8)
- Improve organization and coherence (M9-M15)
- Renumber sub-skills consistently
- Clarify skill themes per grade

### Phase 3: Polish LOW Priority Issues (8 issues)
- Standardize descriptions
- Add more early unplugged skills
- Fine-tune skill placement

---

## VALIDATION AGAINST CREATICODE 3D BLOCKS

**Coverage Analysis:**

✅ **Well-Covered Categories:**
- 3D Scene (47 blocks): Skills cover initialization, cameras, lighting, fog, sky, joysticks ✓
- 3D Object (50 blocks): Skills cover primitives, models, avatars, text, hierarchy, removal ✓
- 3D Action (51 blocks): Skills cover movement, rotation, distance, picking, dragging, collision ✓
- 3D Physics (36 blocks): Skills cover physics init, bodies, forces, constraints, car simulation ✓
- 3D Effect (18 blocks): Skills cover particle emitters (G5.07), trails mentioned indirectly ✓

⚠️ **Partially Covered Categories:**
- 3D Tools (32 blocks):
  - Covered: textures, colors, scale, copy/matrix, mirror, rotation copy, bounding box
  - Missing: merge objects, carve objects, export GLB/STL, grid material, flat shading, convert to mirror, SPS (solid particle system), subdivide, update vertices

- 3D AR/VR (5 blocks):
  - NOT COVERED: AR world camera, AR face camera, AR image tracking, occlusion, inspector

❌ **Missing Advanced Features:**
- Advanced geometry: geometry blocks (triangles, lines, points, angle marks)
- Chemistry: atom blocks
- Advanced tools: CSG operations (merge, carve), mesh editing (subdivide, vertex manipulation)
- Export capabilities: GLB/STL export
- AR/VR: entire AR/VR category

**Recommendation:** Current T18 covers core 3D game development well (200+ blocks). Missing features (AR/VR, advanced geometry, chemistry, mesh editing) could be:
1. Added as G8 advanced skills, OR
2. Placed in separate topics (T32 AR/VR, T33 3D Modeling, T34 Chemistry Visualization), OR
3. Left as "beyond curriculum" for advanced learners

---

## CONCLUSION

T18 has a solid foundation but needs significant Phase 1 fixes to resolve:
1. **Dependency violations** that break learning progression
2. **Overly complex skills** that overwhelm students
3. **Missing fundamental skills** that leave gaps in scaffolding
4. **Unclear descriptions** that prevent consistent assessment

After Phase 1 fixes, the topic will provide a coherent, well-scaffolded progression from spatial awareness (GK-G2) through basic 3D programming (G3-G4) to advanced physics and optimization (G5-G8).

**Estimated Fix Time:** 3-4 weeks for HIGH priority issues, 1-2 weeks for MEDIUM, ongoing polish for LOW.

---

**Report Generated:** 2025-11-23
**Analyst:** Claude (Sonnet 4.5)
**Files Analyzed:**
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (lines 10245-10807, 61 skills)
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/T18_3D_Blocks_Complete_List.txt` (239 blocks)
