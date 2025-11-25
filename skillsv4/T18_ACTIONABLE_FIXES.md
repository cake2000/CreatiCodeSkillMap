# T18 Actionable Fixes - Step-by-Step Guide

**Date**: 2025-11-25

This document provides exact fixes for T18 issues, ready to copy-paste into allskills.md.

---

## PHASE 1: CRITICAL FIXES (Do First)

### Fix 1: Split T18.G4.01.02 (Capsule + Torus)

**Current (WRONG)**:
```
ID: T18.G4.01.02
Topic: T18 – 3D Worlds & Games
Skill: Add capsule and torus shapes
Description: Students add capsule shapes (for character bodies, pillars) and torus shapes (for rings, wheels) to expand their shape vocabulary beyond basic primitives.

Dependencies:
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T18.G4.01.01: Add plane shapes for floors and walls
```

**Replace With**:

```
ID: T18.G4.01.02
Topic: T18 – 3D Worlds & Games
Skill: Add capsule shapes to the 3D scene
Description: Students use the `add capsule` block to create capsule shapes (for character bodies, pillars, posts) by setting diameter top, diameter bottom, height, and sides parameters.

Dependencies:
* T18.G4.01.01: Add plane shapes for floors and walls


ID: T18.G4.01.03
Topic: T18 – 3D Worlds & Games
Skill: Add torus shapes to the 3D scene
Description: Students use the `add torus` block to create torus shapes (for rings, wheels, donuts) by setting diameter, thickness, and sides parameters.

Dependencies:
* T18.G4.01.02: Add capsule shapes to the 3D scene
```

**Then renumber**: T18.G4.01.03 (old "Compose multi-part") → T18.G4.01.04

---

### Fix 2: Split T18.G7.01.03 (Cone + Tube + Stairs)

**Current (WRONG)**:
```
ID: T18.G7.01.03
Topic: T18 – 3D Worlds & Games
Skill: Use advanced shapes (cone, tube, stairs)
Description: Students add cone, tube, rectangle tube, and stair shapes to expand their building vocabulary for more complex architecture and level design.

Dependencies:
* T18.G7.01.02: Create 3D text objects
```

**Replace With**:

```
ID: T18.G7.01.03
Topic: T18 – 3D Worlds & Games
Skill: Add cone shapes from vertex lists
Description: Students use the `add cone` block to create cone shapes from a 2D vertex list, setting height to create custom conical structures for roofs, towers, or projectiles.

Dependencies:
* T18.G7.01.02: Create 3D text objects


ID: T18.G7.01.04
Topic: T18 – 3D Worlds & Games
Skill: Add tube shapes to the 3D scene
Description: Students use the `add tube` block to create hollow tube shapes, adjusting diameter (top and bottom), height, arc, closed section, cap type, sides, and thickness for pipes, tunnels, or architectural elements.

Dependencies:
* T18.G7.01.03: Add cone shapes from vertex lists


ID: T18.G7.01.05
Topic: T18 – 3D Worlds & Games
Skill: Add rectangle tube shapes
Description: Students use the `add rectangle tube` block to create hollow rectangular tubes by setting size in X, Y, height, cap type, thickness, and sides for ducts, channels, or frames.

Dependencies:
* T18.G7.01.04: Add tube shapes to the 3D scene


ID: T18.G7.01.06
Topic: T18 – 3D Worlds & Games
Skill: Add stair shapes to the 3D scene
Description: Students use the `add stairs` block to create staircase structures by setting width, depth, height, count, thickness, and type for platformers or architectural scenes.

Dependencies:
* T18.G7.01.05: Add rectangle tube shapes
```

**Then renumber**: All subsequent G7 skills +3

---

### Fix 3: Fix Block Names in Descriptions

**T18.G3.05 - Current**:
```
Description: Students set `x`, `y`, and `z` values (or use `go to x:y:z`) to move an object to a target location, connecting coordinate plans from earlier math/diagram skills (T02/T25) to actual blocks.
```

**T18.G3.05 - Fixed**:
```
Description: Students use the `move to x y z in (T) seconds` block to position an object at target coordinates, connecting coordinate understanding from earlier math skills to actual 3D positioning.
```

---

**T18.G3.06.01 - Current**:
```
Description: Students use the `set color` block to apply a solid color to 3D objects, learning how to differentiate objects visually (e.g., making the ground green, a player red).
```

**T18.G3.06.01 - Fixed**:
```
Description: Students use the `update color diffusion` block to apply a solid diffusion color to 3D objects, learning how to differentiate objects visually (e.g., making the ground green, a player red).
```

---

**T18.G3.06.02 - Current**:
```
Description: Students use opacity or alpha blocks to make objects partially or fully transparent, useful for windows, water, or ghost effects.
```

**T18.G3.06.02 - Fixed**:
```
Description: Students adjust the roughness and brightness parameters in the `update color` block to make objects partially or fully transparent, useful for windows, water, or ghost effects.
```

---

### Fix 4: Remove Composite Skill T18.G4.01.03 (old numbering)

**Current (DELETE or MOVE)**:
```
ID: T18.G4.01.03
Topic: T18 – 3D Worlds & Games
Skill: Compose a multi-part 3D scene with multiple primitives
Description: Students create a complex environment using multiple primitive types (boxes, spheres, cylinders, planes, etc.), aligning them precisely to build a room, park, or racetrack.
```

**Options**:
1. **DELETE** - This is not a single-block skill
2. **MOVE** to G6+ as a project/capstone skill with updated description:
   ```
   ID: T18.G6.XX
   Topic: T18 – 3D Worlds & Games
   Skill: Design and build a multi-part 3D environment project
   Description: Students design and implement a complete 3D environment (room, park, racetrack, etc.) using multiple primitive shapes, positioning them precisely and applying appropriate colors and materials. This is a composite project skill demonstrating mastery of object creation and positioning.

   Dependencies:
   * T18.G5.XX: (appropriate foundation skills)

   Note: This is a composite/project skill, not a single-block skill.
   ```

**Recommended**: DELETE (not a block skill)

---

### Fix 5: Reorder Physics Skills

**Problem**: Physics initialization (T18.G5.01.01) comes AFTER collision detection (T18.G4.06)

**Solution**: Move physics initialization earlier OR move collision detection later

**Option A**: Move T18.G5.01.01-03 to G4 (after scene/object basics)

**Option B**: Change T18.G4.06 to be non-physics collision (use collision detection blocks from 3D Action, not physics)

**Recommended Option B**: Clarify T18.G4.06 as non-physics collision

**T18.G4.06 - Rewrite**:
```
ID: T18.G4.06
Topic: T18 – 3D Worlds & Games
Skill: Detect when 3D objects are close using distance checking
Description: Students use distance-checking blocks or overlap detection to detect when the player gets near collectibles, NPCs, or hazards, then respond with sounds, score changes, or dialog. This uses non-physics collision detection suitable for simple games.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.01: Use a simple if in a script
* T18.G4.05.03: Animate scenery with position changes

Note: This skill uses distance checking, not physics collision. For physics-based collision, see T18.G5.03.01.
```

---

## PHASE 2: ADD MISSING HIGH-PRIORITY SKILLS

### New Skill: Distance Between Objects (G4)

```
ID: T18.G4.XX
Topic: T18 – 3D Worlds & Games
Skill: Calculate distance between two 3D objects
Description: Students use the `distance between objects [OBJECT1] and [OBJECT2]` block to calculate the 3D distance between two objects, useful for proximity detection, chase AI, or scoring.

Dependencies:
* T18.G3.05: Position shapes using x/y/z coordinates
```

---

### New Skill: Set Object Speed (G4)

```
ID: T18.G4.XX
Topic: T18 – 3D Worlds & Games
Skill: Set movement speed for 3D objects
Description: Students use the `set speed` block to control how fast an object moves when using motion blocks, useful for creating different character movement speeds.

Dependencies:
* T18.G3.07: Move a 3D player with keyboard input
```

---

### New Skill: Copy Position from Camera (G5)

```
ID: T18.G5.XX
Topic: T18 – 3D Worlds & Games
Skill: Copy object position from camera
Description: Students use the `copy position from camera` block to instantly position an object at the camera's location, useful for first-person spawning or camera-relative placement.

Dependencies:
* T18.G4.03.01: Set up an orbit camera to view a target
```

---

### New Skill: Copy Direction from Camera (G5)

```
ID: T18.G5.XX
Topic: T18 – 3D Worlds & Games
Skill: Copy object direction from camera
Description: Students use the `copy direction from camera` block to orient an object to face the same direction as the camera, useful for projectile launching or first-person mechanics.

Dependencies:
* T18.G4.03.01: Set up an orbit camera to view a target
```

---

### New Skill: Remove 3D Objects (G4)

```
ID: T18.G4.XX
Topic: T18 – 3D Worlds & Games
Skill: Remove 3D objects from the scene
Description: Students use the `remove object named [NAME]` block to delete objects from the scene, useful for collecting items, removing enemies, or cleaning up the scene.

Dependencies:
* T18.G3.04.01: Add a box shape to the 3D scene
```

---

### New Skill: Remove All 3D Objects (G4)

```
ID: T18.G4.XX
Topic: T18 – 3D Worlds & Games
Skill: Remove all 3D objects at once
Description: Students use the `remove all objects` block to clear the entire scene, useful for resetting levels or transitioning between scenes.

Dependencies:
* T18.G4.XX: Remove 3D objects from the scene
```

---

### New Skill: Remove Light (G5)

```
ID: T18.G5.XX
Topic: T18 – 3D Worlds & Games
Skill: Remove individual lights from the scene
Description: Students use the `remove light named [NAME]` block to delete specific lights, useful for dynamic lighting effects or optimizing performance.

Dependencies:
* T18.G4.02.01: Add ambient lighting to set base brightness
```

---

### New Skill: Remove All Lights (G5)

```
ID: T18.G5.XX
Topic: T18 – 3D Worlds & Games
Skill: Remove all lights from the scene
Description: Students use the `remove all lights` block to clear all lighting, useful for dramatic transitions or resetting lighting setup.

Dependencies:
* T18.G5.XX: Remove individual lights from the scene
```

---

### New Skill: Set Scene Background Color (G3)

```
ID: T18.G3.XX
Topic: T18 – 3D Worlds & Games
Skill: Set scene background color
Description: Students use the `set scene background color [COLOR]` block to change the background color of the 3D scene, creating different moods or environments.

Dependencies:
* T18.G3.03: Initialize a 3D scene with a specific environment
```

---

### New Skill: Show 3D Axis (G4)

```
ID: T18.G4.XX
Topic: T18 – 3D Worlds & Games
Skill: Show 3D axis helper for debugging
Description: Students use the `show 3D axis [SHOW v] length (LENGTH)` block to display the world coordinate axes (X, Y, Z) for debugging and understanding object positions.

Dependencies:
* T18.G3.01: Interpret 3D axis directions
```

---

## PHASE 3: CLEAN UP DEPENDENCIES

### T18.G3.03 - Remove Unnecessary Dependencies

**Current**:
```
Dependencies:
* T18.G3.02: Match camera views to 3D layouts
* T09.G3.01: Create and use a numeric variable for score or count
* T07.G3.02: Trace a script with a simple loop
* T03.G3.03: Create a 3‑panel storyboard for a project
```

**Fixed**:
```
Dependencies:
* T18.G3.02: Match camera views to 3D layouts
```

**Removed**: T09.G3.01 (variables not needed), T07.G3.02 (loops not needed), T03.G3.03 (storyboard not needed for basic init)

---

### T18.G3.04.01 - Remove Conditional Dependency

**Current**:
```
Dependencies:
* T18.G3.03: Initialize a 3D scene with a specific environment
* T08.G3.01: Use a simple if in a script
```

**Fixed**:
```
Dependencies:
* T18.G3.03: Initialize a 3D scene with a specific environment
```

**Removed**: T08.G3.01 (conditionals not needed to add a box)

---

### T18.G4.05.01 - Remove Loop Dependency

**Current**:
```
Dependencies:
* T18.G4.04.02: Add avatar models to the scene
* T07.G3.01: Use a counted repeat loop
```

**Fixed**:
```
Dependencies:
* T18.G4.04.02: Add avatar models to the scene
```

**Removed**: T07.G3.01 (loops not needed to play one animation)

---

### T18.G3.02 - Remove Loop Dependency

**Current**:
```
Dependencies:
* T18.G3.01: Interpret 3D axis directions
* T07.G3.01: Use a counted repeat loop
```

**Fixed**:
```
Dependencies:
* T18.G3.01: Interpret 3D axis directions
```

**Removed**: T07.G3.01 (loops not needed for observation)

---

### T18.G4.03.01 - Fix Wrong Dependency

**Current**:
```
Dependencies:
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T18.G4.02.03: Add point lights for localized illumination
```

**Fixed**:
```
Dependencies:
* T18.G3.03: Initialize a 3D scene with a specific environment
```

**Removed**: T18.G4.02.03 (orbit camera doesn't depend on lights)
**Removed**: T07.G2.01 (not needed)

---

### T18.G4.04.01 - Fix Wrong Dependency

**Current**:
```
Dependencies:
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T18.G4.03.02: Set up a follow camera to track a moving object
```

**Fixed**:
```
Dependencies:
* T18.G3.03: Initialize a 3D scene with a specific environment
```

**Removed**: T18.G4.03.02 (models don't depend on cameras)
**Removed**: T07.G2.01 (not needed)

---

## PHASE 4: GRADE LEVEL ADJUSTMENTS

### Move T18.G3.07 to G4

**Current**: T18.G3.07 (Grade 3)
**Move to**: T18.G4.XX

**Reasoning**: Keyboard input + movement + forever loop is too complex for G3

---

### Move T18.G3.08 to G4

**Current**: T18.G3.08 (Grade 3)
**Move to**: T18.G4.XX

**Reasoning**: Script tracing with rotations is too abstract for G3

---

### Move T18.G6.05.01 to G4

**Current**: T18.G6.05.01 (Grade 6)
**Move to**: T18.G4.XX (after T18.G4.02.03)

**New ID**: T18.G4.02.04

**Reasoning**: Spot lights have same complexity as point lights

**Updated Skill**:
```
ID: T18.G4.02.04
Topic: T18 – 3D Worlds & Games
Skill: Add spot lights for focused illumination
Description: Students add spot lights (like flashlights or stage lights) with configurable direction, cone angle, and intensity for dramatic focused lighting.

Dependencies:
* T18.G4.02.03: Add point lights for localized illumination
```

---

### Move T18.G5.04.01 to G6

**Current**: T18.G5.04.01 (Grade 5)
**Move to**: T18.G6.XX

**Reasoning**: Nested loops are a G6 concept (T10.G6.XX)

---

## SUMMARY OF CHANGES

### Critical Fixes (5 items)
- ✓ Split T18.G4.01.02 → 2 skills
- ✓ Split T18.G7.01.03 → 4 skills
- ✓ Fix 3 block name descriptions
- ✓ Remove/relocate composite skill T18.G4.01.03
- ✓ Clarify T18.G4.06 as non-physics collision

### New Skills Added (9 items)
- ✓ Distance between objects
- ✓ Set speed
- ✓ Copy position from camera
- ✓ Copy direction from camera
- ✓ Remove object
- ✓ Remove all objects
- ✓ Remove light
- ✓ Remove all lights
- ✓ Set background color
- ✓ Show 3D axis

### Dependencies Cleaned (6 skills)
- ✓ T18.G3.03 (removed 3 deps)
- ✓ T18.G3.04.01 (removed 1 dep)
- ✓ T18.G4.05.01 (removed 1 dep)
- ✓ T18.G3.02 (removed 1 dep)
- ✓ T18.G4.03.01 (fixed deps)
- ✓ T18.G4.04.01 (fixed deps)

### Grade Adjustments (4 skills)
- ✓ T18.G3.07 → G4
- ✓ T18.G3.08 → G4
- ✓ T18.G6.05.01 → G4 (as T18.G4.02.04)
- ✓ T18.G5.04.01 → G6

---

## NEXT STEPS

After completing these fixes:

1. **Renumber affected skills** - Many skills will need new IDs due to insertions
2. **Verify all dependency references** - Make sure renumbered skills update their dependencies
3. **Add remaining missing skills** - Systematically add ~70 more skills for uncovered blocks
4. **Test progression** - Verify skills flow logically from simple to complex
5. **Review with educators** - Confirm grade-level appropriateness

---

**Files Created**:
- T18_COMPREHENSIVE_ANALYSIS.md (full analysis)
- T18_QUICK_SUMMARY.md (executive summary)
- T18_ACTIONABLE_FIXES.md (this file - ready-to-apply fixes)
