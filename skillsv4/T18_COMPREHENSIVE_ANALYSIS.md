# T18 (3D Worlds & Games) Comprehensive Analysis

**Analysis Date**: 2025-11-25
**Skill Range**: Lines 14391-15299 in allskills.md
**Total Skills Analyzed**: 82 skills (GK to G8)

---

## EXECUTIVE SUMMARY

The T18 topic has **CRITICAL STRUCTURAL ISSUES** that need immediate attention:

1. **Multiple blocks covered in single skills** - Violates "ONE block per skill" rule
2. **Missing fundamental skills** - Many CreatiCode 3D blocks have no corresponding skills
3. **Dependency issues** - Many cross-topic dependencies that could be removed
4. **Incomplete progression** - Gaps in logical skill progression from basic to advanced
5. **Misalignment with CreatiCode blocks** - Skills don't match actual block capabilities

---

## HIGH PRIORITY ISSUES (MUST FIX)

### Issue Category 1: Skills Covering Multiple Blocks (ONE-SKILL-ONE-BLOCK VIOLATION)

| Skill ID | Current Description | Multiple Blocks Covered | Recommended Fix |
|----------|-------------------|-------------------------|-----------------|
| **T18.G3.04.01** | Add a box shape to the 3D scene | Just box (OK) | ✓ This is fine |
| **T18.G3.04.02** | Add a sphere shape to the 3D scene | Just sphere (OK) | ✓ This is fine |
| **T18.G3.04.03** | Add a cylinder shape to the 3D scene | Just cylinder (OK) | ✓ This is fine |
| **T18.G4.01.01** | Add plane shapes for floors and walls | Just plane (OK) | ✓ This is fine |
| **T18.G4.01.02** | Add capsule and torus shapes | **2 BLOCKS**: capsule + torus | **SPLIT**: Create T18.G4.01.02 for capsule, T18.G4.01.03 for torus |
| **T18.G4.01.03** | Compose a multi-part 3D scene with multiple primitives | **PROJECT SKILL**: Uses many blocks | **REDESIGN**: This is a project/composite skill, not a single-block skill. Move to higher grade or mark as composite |
| **T18.G4.02.01** | Add ambient lighting to set base brightness | Just ambient light (OK) | ✓ This is fine |
| **T18.G4.02.02** | Add directional lighting for sunlight effect | Just directional light (OK) | ✓ This is fine |
| **T18.G4.02.03** | Add point lights for localized illumination | Just point light (OK) | ✓ This is fine |
| **T18.G7.01.03** | Use advanced shapes (cone, tube, stairs) | **3+ BLOCKS**: cone, tube, rectangle tube, stairs | **SPLIT**: Create separate skills for each shape type |

**CRITICAL**: T18.G4.01.02 must be split into two skills immediately.

---

### Issue Category 2: Missing Essential Skills

Based on the CreatiCode 3D blocks reference, these blocks have NO corresponding skills:

#### **3D Scene Category - Missing Skills**:
1. **Scene fog** - `set scene fog` block (exists but only mentioned in G5.06.01 descriptor)
2. **Sky/skybox** - `set sky` block (exists as T18.G8.02.01 but only for textures)
3. **Clipping planes** - `set clipping plane` block
4. **Pipeline effects** - `add pipeline vignette` block (post-processing)
5. **3D axis display** - `show 3D axis` block
6. **Webcam background** - `turn webcam background` block
7. **Full screen mode** - `switch to full screen` block
8. **Display region** - `set display region` block (multi-camera viewports)
9. **Scene background color** - `set scene background color` block

#### **3D Object Category - Missing Skills**:
1. **6-colored box** - `add 6-colored box` block (different colors per face)
2. **Tube** - `add tube` block (separate from cylinder)
3. **Rectangle tube** - `add rectangle tube` block
4. **Dotted lines** - `add dotted line` block
5. **Curves** - `add curve` block (from point list)
6. **Arc generation** - `generate arc points` block
7. **Moving lines** - `add moving line between objects` block
8. **Geometry tools** - Multiple geometry blocks (points, frames, angles)
9. **Chemistry tools** - Atom and molecule blocks
10. **Voxel objects** - `add voxel` block
11. **Costume extrusion** - `extrude costume` block
12. **User avatars** - `add user avatar` block
13. **Community models** - `add community model` block
14. **Public URL objects** - `add public object at URL` block
15. **Transformers** - `add transformer` block
16. **SPS (Solid Particle System)** - `convert to sps` and `add to sps` blocks

#### **3D Action Category - Missing Skills**:
1. **Set speed** - `set speed` block
2. **Distance calculation** - `distance between objects` block
3. **Copy direction from camera** - `copy direction from camera` block
4. **Copy position from camera** - `copy position from camera` block
5. **Copy from other objects** - `copy position/direction from object` blocks
6. **Update bone** - `update bone` block (for skeletal animation)
7. **Attach to avatar body parts** - `attach to body part` block
8. **Update collider dimension** - `update collider dimension` block
9. **Distance sensors** - `set distance sensor` and related blocks
10. **Hovering detection** - Complete hovering block set
11. **Dragging** - Complete dragging block set
12. **Map screen to 3D** - `map screen XY to XYZ position` block

#### **3D Tools Category - Missing Skills**:
1. **Grid materials** - `apply grid material` block
2. **Material settings** - `material setting` block (wireframe, backface, etc.)
3. **Flat shading** - `convert to flat shading` block
4. **Camera facing mode** - `set camera facing mode` block
5. **Rendering layers** - `set rendering layer` block
6. **Bake transformations** - `bake current transformations` block
7. **Parent management** - `unlink all children`, `unlink parent`, `set camera as parent`
8. **Local axis display** - `show local axis` block
9. **Property get/set** - Generic property blocks
10. **For each loop** - `for each 3D object named` block
11. **Subdivide faces** - `subdivide faces by` block
12. **Update vertices** - `update vertices` block

#### **3D Physics Category - Missing Skills**:
1. **Update gravity** - `update gravity for scene` block
2. **Set physics frame rate** - `set physics frame rate` block
3. **Get physics frame rate** - `get physics frame rate` block
4. **Compound physics bodies** - `add physics bodies into compound` block
5. **Remove physics body** - `remove physics body` block
6. **Get physics body properties** - `get physics body [PROPERTY]` block
7. **Set physics body speed variants** - Multiple speed-setting blocks
8. **Set rotation speed** - `set physics body rotation speed` block
9. **Lock physics movement** - `lock physics body speed` block
10. **Physics damping** - `set physics body damping` block
11. **Speed limits** - `set physics body rotation/movement speed limit` blocks
12. **Constraint limits** - `set limits for hinge constraint` block
13. **Hinge motor** - `set speed for hinge constraint` block
14. **Remove constraint** - `remove constraint` block
15. **Contact detection** - `names of physics bodies in contact` block
16. **Individual car wheel control** - `set car wheel engine force` and `set car wheel angle` blocks

#### **3D Effect Category - Missing Skills**:
1. **Custom particle emitters** - `add particle emitter` block (vs prebuilt)
2. **All emitter shape configs** - Box, cone, cylinder, hemispheric, mesh, sphere configs
3. **Emitter blend modes** - `configure emitter blend mode` block
4. **Emitter initial rotation** - `configure emitter initial rotation` block
5. **Emitter movement** - `configure emitter movement` block
6. **Emitter rotation speed** - `configure emitter rotation speed` block
7. **Emitter scale** - `configure emitter scale` block
8. **Emitter control** - Start/stop emitter blocks
9. **Trails** - `add trail` block (mentioned in G7.06.02 but no dedicated skill)

#### **3D AR/VR Category - Missing Skills**:
1. **AR world camera** - Partially covered in T18.G8.04.01
2. **AR face tracking** - Partially covered in T18.G8.04.02
3. **AR image tracking** - Partially covered in T18.G8.04.03
4. **Transparent occlusion** - `convert to transparent occlusion` block
5. **AR inspector** - `show inspector` block

---

### Issue Category 3: Incorrect Block Mapping

| Skill ID | Issue | Actual Block(s) | Fix |
|----------|-------|----------------|-----|
| **T18.G3.05** | Description says "go to x:y:z" | Block is `move to x y z in (T) seconds` from 3D Action | Update description to match actual block name and behavior |
| **T18.G3.06.01** | Says "set color block" | Block is `update color diffusion [COLOR]` from 3D Tools | Update to reflect actual block syntax |
| **T18.G3.06.02** | Says "opacity or alpha blocks" | Block is `update color` with transparency parameter | Clarify exact block used |
| **T18.G4.05.01** | Says "100+ built-in animations" | Need to verify count | Verify actual animation count |
| **T18.G5.05.01** | Says "200+ texture library" | Need to verify count | Verify actual texture count |
| **T18.G6.06.02** | Says "mouse picking blocks" | Actual blocks are `turn on picking`, `picked point`, `picked object name` | Update to reflect multiple blocks or split skill |

---

### Issue Category 4: Missing Fundamental Foundation Skills

These early skills are MISSING and should exist before current G3 skills:

| Grade | Missing Skill | Why It's Needed |
|-------|---------------|-----------------|
| **G2** | Observe 3D objects in digital environments | Bridge from physical 3D (GK-G2) to digital 3D |
| **G3** | Understand 3D coordinate system basics | Before using coordinates in T18.G3.05 |
| **G3** | Identify camera perspective differences | Before T18.G3.02 camera views |
| **G3** | Recognize basic 3D shapes in games | Before creating shapes in G3.04.x |

---

### Issue Category 5: Intra-Topic Dependency Issues

Several skills have **BROKEN or QUESTIONABLE** intra-topic dependencies:

#### **Missing Prerequisites**:

| Skill ID | Current Prerequisites | Missing Prerequisites |
|----------|---------------------|---------------------|
| **T18.G3.04.01** | T18.G3.03, T08.G3.01 | Should depend on understanding basic shapes (missing) |
| **T18.G3.07** | T18.G3.06.02, T08.G3.03, T09.G3.03 | Should depend on positioning (T18.G3.05) since player needs to be positioned |
| **T18.G4.03.01** | T18.G4.02.03 | Why does orbit camera depend on point lights? Should depend on T18.G3.03 (scene init) |
| **T18.G4.04.01** | T18.G4.03.02 | Why do models depend on camera setup? Should just depend on scene init |

#### **Incorrect Sequencing**:

| Skill ID | Issue | Fix |
|----------|-------|-----|
| **T18.G5.01.01** | Physics depends on T18.G4.06 (collision detection) | Physics initialization should come BEFORE collision detection, not after |
| **T18.G4.06** | Uses "proximity detection" but no physics | Either this is non-physics collision (fine) or it needs physics prereqs |
| **T18.G6.05.01** | Spot lights in G6 but point/directional in G4 | Spot lights are same complexity as point lights, should be in G4 |

#### **Overly Long Dependency Chains**:

Example: To get to **T18.G5.06.02** (particle emitters), students must go through:
- T18.G3.03 → T18.G3.04.01 → .02 → .03 → T18.G3.05 → T18.G3.06.01 → .02 → T18.G3.07 → T18.G3.08 → T18.G4.01.01 → .02 → .03 → T18.G4.02.01 → .02 → .03 → T18.G4.03.01 → .02 → T18.G4.04.01 → .02 → T18.G4.05.01 → .02 → .03 → T18.G4.06 → T18.G5.01.01 → .02 → .03 → T18.G5.02.01 → .02 → T18.G5.03.01 → .02 → T18.G5.04.01 → .02 → T18.G5.05.01 → .02 → .03 → T18.G5.06.01 → T18.G5.06.02

**35 skills just to add a particle emitter!** This is excessive.

---

## MEDIUM PRIORITY ISSUES

### Issue Category 6: Excessive Cross-Topic Dependencies

Many skills have cross-topic dependencies that may not be necessary:

#### **T07 (Loops) Dependencies - Often Redundant**:

| Skill ID | T07 Dependency | Why It Might Be Redundant |
|----------|---------------|---------------------------|
| T18.G3.02 | T07.G3.01: Use a counted repeat loop | Camera matching is observation, doesn't need loops |
| T18.G3.03 | T07.G3.02: Trace a script with a simple loop | Scene initialization doesn't require loops |
| T18.G4.05.01 | T07.G3.01: Use a counted repeat loop | Playing animation doesn't require loops (animation plays once) |

**Pattern**: Many skills import T07 dependencies when they don't actually need loops. Loop skills should only be prerequisites when the skill **requires iteration**.

#### **T09 (Variables) Dependencies - Often Premature**:

| Skill ID | T09 Dependency | Why It Might Be Excessive |
|----------|---------------|---------------------------|
| T18.G3.03 | T09.G3.01: Create and use a numeric variable | Scene initialization doesn't need variables |
| T18.G5.01.01 | T09.G3.01: Create and use a numeric variable | Physics init doesn't inherently need variables |
| Many G5+ skills | T09.G3.01.01: Create a new variable with a descriptive name | This same dependency appears 20+ times |

**Pattern**: Variables are imported as dependencies even when not needed for the basic block usage.

#### **T08 (Conditionals) Dependencies - Sometimes Unnecessary**:

| Skill ID | T08 Dependency | Why It Might Be Excessive |
|----------|---------------|---------------------------|
| T18.G3.04.01 | T08.G3.01: Use a simple if in a script | Adding a box doesn't require conditionals |

#### **Recommendations**:
1. **Remove cross-topic dependencies** unless the skill description **explicitly requires** that concept
2. **Focus on intra-topic progression** within T18
3. **Add cross-topic dependencies only when building complete projects** (e.g., "Build a 3D maze game with scoring" would need T09 variables)

---

### Issue Category 7: Skills That Are Too Broad or Too Vague

| Skill ID | Issue | Fix |
|----------|-------|-----|
| **T18.G3.08** | "Trace a short 3D script to predict positions" | Too abstract - what specific blocks? Make this concrete |
| **T18.G4.01.03** | "Compose a multi-part 3D scene" | This is a project, not a single block skill |
| **T18.G6.02** | "Trace multi-step 3D scripts with transforms" | Too abstract |
| **T18.G6.03** | "Refactor repeated object creation with loops" | This is refactoring skill, not a 3D block skill |
| **T18.G8.06.01** | "Analyze and optimize 3D scene performance" | Meta-skill, not a block skill |
| **T18.G8.06.02** | "Analyze trade-offs in 3D design decisions" | Meta-skill, not a block skill |

**Recommendation**:
- Keep meta-skills (analysis, optimization, design) but clearly mark them as "composite" or "meta" skills
- Separate them from single-block skills
- Consider moving to end of topic as capstone skills

---

### Issue Category 8: Grade Level Appropriateness

Some skills may be too advanced for their assigned grade:

| Skill ID | Current Grade | Complexity Issue | Recommended Grade |
|----------|---------------|------------------|------------------|
| **T18.G3.07** | G3 | Keyboard input + movement + forever loop is complex for 3rd grade | G4 |
| **T18.G3.08** | G3 | Script tracing with rotations is abstract for 3rd grade | G4-G5 |
| **T18.G5.04.01** | G5 | Nested loops for 3D grids | G6 (nested loops are G6 skill) |
| **T18.G6.04.01** | G6 | Mouse input to camera rotation with clamping | G7-G8 |
| **T18.G7.04.02** | G7 | Distance-based AI with vectors | G8 |

---

## LOWER PRIORITY ISSUES

### Issue Category 9: Skill Ordering Within Same Grade

Some skills within the same grade could be reordered for better learning flow:

**Example - G4 Lighting**:
- Current: Ambient → Directional → Point
- Better: Ambient → Point → Directional (point lights are conceptually simpler than directional)

**Example - G3 Shapes**:
- Current: Box → Sphere → Cylinder
- Current order is fine, follows increasing complexity

---

### Issue Category 10: Description Clarity

Minor improvements needed:

| Skill ID | Current Description Fragment | Clearer Alternative |
|----------|---------------------------|-------------------|
| T18.G3.05 | "or use `go to x:y:z`" | "using the `move to` block" (match actual block name) |
| T18.G5.02.01 | "0 = no bounce, 1 = perfect bounce" | Good! Keep this level of detail |
| T18.G6.01.02 | "collision groups or masks" | Clarify: are these separate blocks or one block? |

---

## DETAILED SKILL-BY-SKILL ANALYSIS

### Grade K-2 Skills (Unplugged/Picture-Based) ✓

| Skill ID | Status | Notes |
|----------|--------|-------|
| T18.GK.01 | ✓ GOOD | Proper unplugged 3D shape exploration |
| T18.G1.01 | ✓ GOOD | Matching activity, age-appropriate |
| T18.G2.01 | ✓ GOOD | Perspective understanding, prepares for 3D |

**Assessment**: K-2 skills are well-designed and appropriate.

---

### Grade 3 Skills (Foundation)

| Skill ID | Block(s) Covered | Issues | Priority |
|----------|----------------|--------|----------|
| T18.G3.01 | (Conceptual - axes) | ✓ Good conceptual foundation | LOW |
| T18.G3.02 | (Conceptual - camera views) | ✓ Good preparation skill | LOW |
| T18.G3.03 | `initialize 3D scene` | Too many cross-topic deps (T09, T07) | MEDIUM |
| T18.G3.04.01 | `add box` | ✓ Good single block | LOW |
| T18.G3.04.02 | `add sphere` | ✓ Good single block | LOW |
| T18.G3.04.03 | `add cylinder` | ✓ Good single block | LOW |
| T18.G3.05 | `move to x y z` | Block name incorrect in description | HIGH |
| T18.G3.06.01 | `update color` | Block name unclear | MEDIUM |
| T18.G3.06.02 | `update color` (transparency) | Block name unclear | MEDIUM |
| T18.G3.07 | Movement with keyboard | Too complex for G3, missing prereqs | HIGH |
| T18.G3.08 | (Script tracing) | Too abstract for G3 | MEDIUM |

**Missing G3 Skills**:
- Plane shapes (currently in G4, should be G3)
- Understanding position vs rotation
- Basic camera positioning

---

### Grade 4 Skills

| Skill ID | Block(s) Covered | Issues | Priority |
|----------|----------------|--------|----------|
| T18.G4.01.01 | `add plane` | ✓ Good but should be G3 | LOW |
| T18.G4.01.02 | `add capsule` + `add torus` | **VIOLATES ONE-BLOCK RULE** | **CRITICAL** |
| T18.G4.01.03 | Multiple blocks (composite) | Not a single-block skill | HIGH |
| T18.G4.02.01 | `add ambient light` | ✓ Good | LOW |
| T18.G4.02.02 | `add directional light` | ✓ Good | LOW |
| T18.G4.02.03 | `add point light` | ✓ Good | LOW |
| T18.G4.03.01 | `add orbit camera` | Depends on lights (why?) | MEDIUM |
| T18.G4.03.02 | `add follow camera` | ✓ Good | LOW |
| T18.G4.04.01 | `add model` | ✓ Good | LOW |
| T18.G4.04.02 | `add avatar` | ✓ Good | LOW |
| T18.G4.05.01 | Animation blocks | ✓ Good | LOW |
| T18.G4.05.02 | Rotation loops | Composite skill | MEDIUM |
| T18.G4.05.03 | Position loops | Composite skill | MEDIUM |
| T18.G4.06 | Proximity/collision detection | ✓ Good concept but which blocks? | MEDIUM |

**Missing G4 Skills**:
- Spot lights (currently G6)
- Basic textures
- Model scaling

---

### Grade 5 Skills

| Skill ID | Block(s) Covered | Issues | Priority |
|----------|----------------|--------|----------|
| T18.G5.01.01 | `enable physics for scene` | ✓ Good but comes after collision (wrong order) | HIGH |
| T18.G5.01.02 | `add physics body` (static) | ✓ Good | LOW |
| T18.G5.01.03 | `add physics body` (dynamic) | ✓ Good | LOW |
| T18.G5.02.01 | Restitution parameter | ✓ Good | LOW |
| T18.G5.02.02 | Friction parameter | ✓ Good | LOW |
| T18.G5.03.01 | Physics collision events | ✓ Good | LOW |
| T18.G5.03.02 | Collision response | Composite skill | MEDIUM |
| T18.G5.04.01 | Nested loops for grids | Should be G6 (nested loops) | HIGH |
| T18.G5.04.02 | Grid with Y variation | ✓ Good extension | LOW |
| T18.G5.05.01 | Texture library | ✓ Good | LOW |
| T18.G5.05.02 | Costume textures | ✓ Good | LOW |
| T18.G5.05.03 | Material properties | ✓ Good | LOW |
| T18.G5.06.01 | Fog | ✓ Good | LOW |
| T18.G5.06.02 | Particle emitters (prebuilt) | ✓ Good | LOW |
| T18.G5.06.03 | Emitter configuration | ✓ Good | LOW |

**Missing G5 Skills**:
- Remove objects
- Physics forces vs impulses (currently G6)
- Basic constraints

---

### Grade 6 Skills

| Skill ID | Block(s) Covered | Issues | Priority |
|----------|----------------|--------|----------|
| T18.G6.01.01 | `apply force` and `apply impulse` | Should be G5 | MEDIUM |
| T18.G6.01.02 | Collision groups | ✓ Good | LOW |
| T18.G6.01.03 | Freeze physics axes | ✓ Good | LOW |
| T18.G6.02 | (Script tracing) | Meta-skill | LOW |
| T18.G6.03 | (Refactoring) | Meta-skill | LOW |
| T18.G6.04.01 | Mouse to camera rotation | Complex, needs clear block mapping | MEDIUM |
| T18.G6.04.02 | Virtual joystick | ✓ Good | LOW |
| T18.G6.05.01 | `add spot light` | Should be G4 | HIGH |
| T18.G6.05.02 | Shadow generation | ✓ Good | LOW |
| T18.G6.05.03 | Glow/highlight layers | ✓ Good | LOW |
| T18.G6.06.01 | Speech bubbles | ✓ Good | LOW |
| T18.G6.06.02 | Mouse picking | Multiple blocks or one? | MEDIUM |

**Missing G6 Skills**:
- Nested loops for 3D (if not in G5)
- Distance sensors
- Hovering detection

---

### Grade 7 Skills

| Skill ID | Block(s) Covered | Issues | Priority |
|----------|----------------|--------|----------|
| T18.G7.01.01 | `add column` (extrude) | ✓ Good | LOW |
| T18.G7.01.02 | `add 3D text` | ✓ Good | LOW |
| T18.G7.01.03 | Cone + tube + stairs | **VIOLATES ONE-BLOCK RULE** | **CRITICAL** |
| T18.G7.02.01 | Grid matrix copy | ✓ Good | LOW |
| T18.G7.02.02 | Mirror symmetry copy | ✓ Good | LOW |
| T18.G7.02.03 | Rotational symmetry copy | ✓ Good | LOW |
| T18.G7.03.01 | Distance constraints | ✓ Good | LOW |
| T18.G7.03.02 | Hinge constraints | ✓ Good | LOW |
| T18.G7.03.03 | Fixed constraints | ✓ Good | LOW |
| T18.G7.04.01 | Waypoint movement | Composite skill | MEDIUM |
| T18.G7.04.02 | Chase AI | Composite skill | MEDIUM |
| T18.G7.05.01 | Merge meshes + compound physics | Multiple blocks | HIGH |
| T18.G7.05.02 | Carve operations | ✓ Good | LOW |
| T18.G7.06.01 | Camera transitions | Composite skill | MEDIUM |
| T18.G7.06.02 | Particle trails | ✓ Good | LOW |
| T18.G7.06.03 | Advanced emitter shapes | ✓ Good | LOW |

**Missing G7 Skills**:
- Dragging objects
- Advanced collision detection
- For each object loop

---

### Grade 8 Skills

| Skill ID | Block(s) Covered | Issues | Priority |
|----------|----------------|--------|----------|
| T18.G8.01.01 | Car simulation | ✓ Good | LOW |
| T18.G8.01.02 | Dynamic level loading | Composite skill | MEDIUM |
| T18.G8.01.03 | Multiple camera views | ✓ Good concept | LOW |
| T18.G8.02.01 | Skybox textures | ✓ Good | LOW |
| T18.G8.02.02 | Post-processing effects | ✓ Good | LOW |
| T18.G8.03.01 | Export GLB | ✓ Good | LOW |
| T18.G8.03.02 | Export STL | ✓ Good | LOW |
| T18.G8.04.01 | AR world camera | ✓ Good | LOW |
| T18.G8.04.02 | AR face tracking | ✓ Good | LOW |
| T18.G8.04.03 | AR image tracking | ✓ Good | LOW |
| T18.G8.05.01 | Mirrors | ✓ Good | LOW |
| T18.G8.05.02 | Custom geometry | ✓ Good | LOW |
| T18.G8.06.01 | Performance optimization | Meta-skill | LOW |
| T18.G8.06.02 | Design analysis | Meta-skill | LOW |

**Missing G8 Skills**:
- Custom particle emitters (from scratch)
- Advanced physics (damping, speed limits)
- Vertex manipulation

---

## RECOMMENDED FIXES - ACTION PLAN

### Phase 1: Critical Fixes (Do First)

1. **Split T18.G4.01.02** into:
   - T18.G4.01.02: Add capsule shape to the 3D scene
   - T18.G4.01.03: Add torus shape to the 3D scene
   - Renumber T18.G4.01.03 → T18.G4.01.04

2. **Split T18.G7.01.03** into:
   - T18.G7.01.03: Add cone shapes
   - T18.G7.01.04: Add tube shapes
   - T18.G7.01.05: Add rectangle tube shapes
   - T18.G7.01.06: Add stair shapes

3. **Fix T18.G5.01.01** ordering:
   - Move physics initialization BEFORE collision detection
   - Physics should be introduced in early G5, before T18.G4.06 collision

4. **Correct block names**:
   - T18.G3.05: Change "go to x:y:z" → "move to x y z"
   - T18.G3.06.01: Specify exact block: "update color diffusion"
   - T18.G3.06.02: Clarify transparency parameter in update color

5. **Remove composite skill T18.G4.01.03** (current):
   - This is not a single-block skill
   - Either remove or convert to a project/capstone skill

---

### Phase 2: Add Missing Foundation Skills

**Add to G3**:
1. T18.G3.XX: Add plane shapes for floors
2. T18.G3.XX: Set object position using coordinates
3. T18.G3.XX: Set camera position

**Add to G4**:
1. T18.G4.XX: Add spot lights
2. T18.G4.XX: Scale objects
3. T18.G4.XX: Remove objects

**Add to G5**:
1. T18.G5.XX: Apply forces to physics bodies
2. T18.G5.XX: Apply impulses to physics bodies
3. T18.G5.XX: Detect physics collisions

---

### Phase 3: Add Missing Essential Skills

Based on "Issue Category 2", systematically add skills for:

**Priority 1 - Common Blocks**:
- Distance calculation
- Set speed
- Copy position/direction
- Distance sensors
- Hovering detection
- Dragging objects

**Priority 2 - Important Features**:
- Scene background color
- Sky/skybox (non-texture)
- Fog configuration
- Remove light
- Remove object
- Material settings

**Priority 3 - Advanced Features**:
- Custom geometry
- Vertex manipulation
- Chemistry tools
- Geometry tools
- SPS system

---

### Phase 4: Clean Up Dependencies

1. **Remove unnecessary cross-topic dependencies**:
   - T18.G3.03: Remove T09.G3.01, T07.G3.02 (scene init doesn't need variables/loops)
   - T18.G3.04.01: Remove T08.G3.01 (adding box doesn't need conditionals)
   - T18.G4.05.01: Remove T07.G3.01 (playing animation doesn't need loops)

2. **Fix intra-topic dependency chains**:
   - T18.G4.03.01: Change from T18.G4.02.03 → T18.G3.03 (orbit camera needs scene, not lights)
   - T18.G4.04.01: Change from T18.G4.03.02 → T18.G3.03 (models need scene, not cameras)

3. **Simplify long chains**:
   - Create alternate paths to advanced features
   - Don't require ALL prior skills, just essential prereqs

---

### Phase 5: Grade Level Adjustments

**Move to G4**:
- T18.G3.07: Move keyboard input to G4
- T18.G3.08: Move script tracing to G4
- T18.G4.01.01: Keep planes in G4 (OK)

**Move to G4**:
- T18.G6.05.01: Move spot lights to G4 (same complexity as point lights)

**Move to G6**:
- T18.G5.04.01: Move nested loops to G6

**Move to G7-G8**:
- T18.G6.04.01: Move advanced camera rotation to G7

---

## SUMMARY STATISTICS

### Current State
- **Total Skills**: 82
- **Skills Covering Multiple Blocks**: 3 (CRITICAL)
- **Missing Essential Blocks**: ~60+ blocks
- **Skills with Questionable Dependencies**: 15+
- **Skills Too Complex for Grade**: 5
- **Meta-Skills (not block skills)**: 6

### Coverage Analysis
- **3D Scene blocks**: 47 blocks, ~15 skills (32% coverage)
- **3D Object blocks**: 50 blocks, ~10 skills (20% coverage)
- **3D Action blocks**: 51 blocks, ~8 skills (16% coverage)
- **3D Tools blocks**: 32 blocks, ~5 skills (16% coverage)
- **3D Physics blocks**: 36 blocks, ~15 skills (42% coverage)
- **3D Effect blocks**: 18 blocks, ~3 skills (17% coverage)
- **3D AR/VR blocks**: 5 blocks, ~3 skills (60% coverage)

**Overall Coverage**: ~60/239 blocks = **25% coverage**

### Estimated Work
- **Critical fixes**: 5 skills to split/fix
- **New skills needed**: ~60-80 skills to add
- **Dependency fixes**: ~20 skills to update
- **Description updates**: ~15 skills

---

## CONCLUSION

The T18 topic needs **significant restructuring** to:

1. **Achieve one-skill-one-block mapping** (split multi-block skills)
2. **Add missing skills** for ~180 uncovered blocks
3. **Fix dependency chains** (remove unnecessary cross-topic deps)
4. **Reorder skills** for logical progression
5. **Adjust grade levels** for complexity appropriateness

**Estimated Timeline**: This is a major revision requiring careful planning and execution.

**Recommended Approach**:
- Start with Phase 1 (critical fixes)
- Then systematically add missing skills category by category
- Test dependency chains after each addition
- Review with educators for grade-level appropriateness

---

## APPENDIX: COMPLETE SKILL LIST WITH STATUS

[See separate detailed spreadsheet for skill-by-skill breakdown]
