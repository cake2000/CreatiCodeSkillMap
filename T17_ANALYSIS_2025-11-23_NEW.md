# T17 (2D Motion & Physics) - Comprehensive Analysis Report
Date: 2025-11-23

## Executive Summary

This report analyzes the T17 (2D Motion & Physics) topic in the CreatiCode K-8 skill map. The analysis covers:
- CreatiCode's 2D Physics capabilities (47 physics blocks available)
- Current state of T17 skills (77 skills across K-8)
- Issues identified (HIGH and MEDIUM priority)
- Detailed recommendations for optimization

**Key Findings:**
- Skills are well-scaffolded from manual motion (K-G5) to physics engine (G5-G8)
- Some overly broad skills need to be broken down
- Strong coverage of physics blocks, but some blocks missing skill coverage
- Generally good adherence to picture-based (K-2) and block-based (3+) rules
- Minor dependency issues within topic (mostly acceptable cross-topic dependencies)

---

## 1. CreatiCode's 2D Physics Capabilities

### Summary
CreatiCode provides a comprehensive 2D physics engine based on **Rapier**, with 47 dedicated physics blocks covering:

### 1.1 Core Physics Setup (2 blocks)
- **physics_enablephysics**: Initialize 2D physics world with gravity x/y
  - Creates 4 invisible border walls automatically
  - Defines the physics world for all objects

- **physics_removecollider**: Remove physics-based behavior
  - Detaches sprite from physics engine

### 1.2 Physics Body Creation (2 blocks)
- **physics_setphysicsbody**: Create simple convex shape body
  - Types: fixed, dynamic, movable
  - Sensor types: object, sensor
  - Shapes: Circle, Box, Capsule, Convex Hull
  - Debug mode available

- **physics_setphysicsbody2**: Create compound shape body (complex/concave)
  - Same types and sensor options
  - Additional parameters: curve tolerance, point distance
  - More accurate for complex sprites but slower performance

### 1.3 Body Properties (1 block)
- **physics_updatephysicsbody**: Update density, friction, restitution
  - Density: controls mass (density × area = mass)
  - Friction: 0-100%, prevents relative movement
  - Restitution: 0-100%, controls bounciness

### 1.4 Velocity Control (4 blocks)
- **physics_setvelocityx**: Set x speed
- **physics_setvelocityy**: Set y speed
- **physics_setvelocitydir**: Set speed in direction (angle)
- **physics_setvelocitymovingdir**: Set speed in current moving direction
  - Useful for maintaining constant speed without changing direction

### 1.5 Rotation Control (2 blocks)
- **physics_setrotationspeed**: Set rotation speed (degrees/second)
- **physics_setdirbyvelocity**: Point in direction of speed
  - Auto-rotate sprite to face movement direction

### 1.6 Forces (4 blocks)
- **physics_addforce**: Add continuous force at center
- **physics_addforce2**: Add continuous force at position (creates torque if off-center)
- **physics_clearforce**: Remove all forces
- **physics_addtorque**: Add continuous rotational force
- **physics_cleartorque**: Remove all torques

### 1.7 Impulses (3 blocks)
- **physics_applyimpulse**: Apply one-time impulse at center
- **physics_applyimpulse2**: Apply one-time impulse at position
- **physics_applytorqueimpulse**: Apply one-time torque impulse

### 1.8 Movement Constraints (2 blocks)
- **physics_lockmovement**: Prevent body movement from forces (Yes/No)
  - Useful for static objects like walls
- **physics_lockrotation**: Prevent body rotation from forces (Yes/No)
  - Keep objects upright

### 1.9 Damping (1 block)
- **physics_setdampingfactor**: Set movement and rotation damping percentages
  - Simulates air resistance or water friction

### 1.10 Collision Detection & Events (2 blocks)
- **physics_broadcastcollisioneventmessage**: Broadcast when collision starts
- **physics_broadcastcollisioneventmessage2**: Broadcast when collision ends

### 1.11 Collision Groups & Filtering (6 blocks)
- **physics_addtocollisiongroup**: Add to collision group (0-15)
- **physics_removefromcollisiongroup**: Remove from collision group
- **physics_addcollisionfilter**: Enable collision with group
- **physics_removecollisionfilter**: Disable collision with group
- **physics_setdominancegroup**: Set dominance group (-127 to 127)
  - Higher dominance objects don't get pushed by lower dominance
- **physics_setccd**: Enable CCD for fast objects
  - Prevents tunneling through walls

### 1.12 World Properties (2 blocks)
- **physics_setgravityscale**: Set gravity scale for individual sprite (percentage)
  - Create floaty zones or reverse gravity
- **physics_settimespeed**: Set physics time speed (percentage)
  - Slow-motion or fast-forward effects

### 1.13 Joints/Constraints (8 blocks)
- **physics_addfixedjoint**: Fix relative position to sprite (weld together)
- **physics_removefixedjoint**: Remove relative position constraint
- **physics_addrevoltejoint**: Set sprite as rotation axis (hinge)
- **physics_removerevoltejoint**: Remove rotation axis
- **physics_setrotationaxisspeed**: Set rotation axis speed and damping
- **physics_addprismaticjoint**: Allow horizontal/vertical sliding with range limits
  - Note: Prismatic joints are permanent once created
- No remove block for prismatic joint (limitation)

### 1.14 World Border Control (2 blocks)
- **physics_setedgecollider**: Set world border friction and restitution
- **physics_setedgecollisiongroup**: Set world border collision groups

### 1.15 Ground Detection (1 block)
- **physics_turnoncollisiondetection**: Turn on raycast ground detection
  - Maximum distance parameter
  - Debug mode to visualize ray
  - Used with reporters: <in collision below> and (ground slope)

### 1.16 Reporter Blocks (6 blocks)
- **physics_getvelocityx**: Get x speed
- **physics_getvelocityy**: Get y speed
- **physics_getMass**: Get mass
- **physics_getangularvelocity**: Get angular speed
- **physics_getcollidingbottom**: Check if in collision below (boolean)
- **physics_getgroundslope**: Get ground slope

---

## 2. Current State of T17 Skills

### 2.1 Skill Distribution by Grade

| Grade | Count | Focus Area |
|-------|-------|------------|
| K | 2 | Picture-based observation |
| G1 | 1 | Picture-based speed comparison |
| G2 | 1 | Picture-based direction prediction |
| G3 | 2 | Basic motion blocks, position/direction |
| G4 | 2 | Manual gravity simulation, speed concepts |
| G5 | 22 | Manual motion + Physics engine introduction |
| G6 | 21 | Advanced physics properties, collision detection |
| G7 | 15 | Complex forces, joints, simulation |
| G8 | 11 | Game design, optimization, testing |
| **TOTAL** | **77** | |

### 2.2 Pedagogical Approach

The T17 topic follows a well-designed progression:

**Phase 1: Conceptual Foundation (K-G4)**
- K-G2: Picture-based observation and prediction
- G3-G4: Manual motion using basic blocks
- G4: Introduction to gravity simulation using loops and variables

**Phase 2: Manual Physics (G5.02-G5.04)**
- G5.02: Track gravity with velocity variables
- G5.03: Use horizontal speed and friction variables
- G5.04: Code manual bounce with energy loss
- This mirrors classic Scratch physics tutorials
- Builds deep understanding before using engine

**Phase 3: Physics Engine Introduction (G5.05-G5.12)**
- G5.05: Initialize physics world
- G5.06+: Create physics bodies (dynamic, fixed, movable)
- Body shapes, sensors, compound shapes
- Forces, impulses, density
- Basic debugging

**Phase 4: Advanced Physics (G6-G7)**
- Surface properties (friction, restitution)
- Collision detection and events
- Collision groups and filtering
- Velocity control, body types
- Ground detection
- Forces vs impulses
- Damping, torque, reporters

**Phase 5: Complex Systems (G8)**
- Joints (fixed, revolute, prismatic)
- Game design and balancing
- Performance optimization
- Regression testing
- Gravity scale and time speed

### 2.3 Strengths

1. **Excellent scaffolding** from concrete (pictures) to abstract (physics engine)
2. **Manual physics first** approach builds deeper understanding
3. **Good coverage** of most physics blocks
4. **Picture-based K-2** appropriately focused on observation
5. **Block-based G3+** with hands-on coding
6. **Clear progression** from simple to complex

---

## 3. Issues Identified

### 3.1 HIGH PRIORITY Issues

#### Issue H1: Overly Broad Skill - T17.G5.06
**Skill:** T17.G5.06: Attach a dynamic body to a sprite
**Problem:** This skill tries to cover the entire physics_setphysicsbody block, which has multiple parameters:
- Body type (fixed, dynamic, movable)
- Sensor type (object, sensor)
- Shape (Box, Circle, Capsule, Convex Hull)
- Debug mode

Currently, the skill description only focuses on "dynamic" bodies, but the skill ID is referenced as a dependency for many other skills that should logically come BEFORE learning about shapes.

**Current Structure:**
- T17.G5.06: Attach a dynamic body to a sprite (Box shape, basic introduction)
- T17.G5.06.A: Practice creating multiple dynamic bodies (already exists - good!)
- T17.G5.06.01: Choose Box vs Circle collision shapes (already exists)
- T17.G5.06.01.01: Use Capsule shapes (already exists)
- T17.G5.06.01.02: Use Convex Hull (already exists)
- T17.G5.06.02: Create sensor bodies (already exists)
- T17.G5.06.03: Create compound shapes (already exists)

**Issue:** The skill tree is already well-broken down! But the descriptions need to be verified for accuracy.

**Severity:** MEDIUM (structure is good, just need to verify content)

#### Issue H2: Missing Skill - Debug Mode for Physics Bodies
**Block:** physics_setphysicsbody and physics_setphysicsbody2 both have a debug parameter
**Problem:** No explicit skill teaches students to use debug mode to visualize collision shapes
**Current Coverage:** Debug is mentioned in descriptions but not as a dedicated learning outcome

**Recommendation:** Add new skill:
- **T17.G5.06.A.01: Use debug mode to visualize collision shapes**
  - Description: Students enable debug mode when creating physics bodies to see the actual collision shape outline overlaid on sprites. They use this to verify that collision shapes match sprite visuals appropriately and troubleshoot collision detection issues.
  - Dependencies: T17.G5.06.A
  - Place before T17.G5.06.01 (choosing shapes)

**Severity:** HIGH - Debug visualization is critical for learning

#### Issue H3: Missing Skill - Remove Prismatic Joint
**Block:** physics_addprismaticjoint exists but there's no remove block
**Problem:** T17.G8.02.02 teaches prismatic joints but doesn't mention they are permanent
**Current Coverage:** Description mentions "Note: Prismatic joints are permanent once created" but this is a limitation that should be more prominent

**Recommendation:** Update T17.G8.02.02 description to emphasize:
- Prismatic joints cannot be removed once created
- Plan constraint usage during design phase
- Compare with fixed and revolute joints which CAN be removed

**Severity:** MEDIUM - Important limitation to understand

#### Issue H4: Incomplete Coverage - World Border Blocks
**Blocks:**
- physics_setedgecollider (set border friction/restitution)
- physics_setedgecollisiongroup (set border collision groups)

**Current Coverage:**
- T17.G6.07.01: Configure world border properties (covers friction/restitution)
- T17.G6.07.02: Configure world borders for wrap-around (covers collision groups)

**Problem:** T17.G6.07.01 description mentions collision groups but that's actually a separate block

**Recommendation:** Split into two focused skills:
- **T17.G6.07.01: Configure world border friction and restitution**
  - Focus only on physics_setedgecollider
  - Description: Students use set world border collider friction [value]% restitution [value]% to customize how objects interact with the automatic stage boundaries. They create bouncy walls for pinball effects, sticky borders to slow objects down, or completely non-bouncy edges.
  - Dependencies: T17.G5.05, T17.G6.01

- **T17.G6.07.02: Configure world border collision groups for selective interactions**
  - Focus only on physics_setedgecollisiongroup
  - Description: Students use set world border collision group [COLLISIONGROUP] colliding with group [TARGETGROUP] to make borders selectively collide with different object types. Examples: players bounce off borders but bullets pass through, or create one-way borders that only stop objects from certain groups.
  - Dependencies: T17.G6.05, T17.G6.07.01

**Severity:** HIGH - Current description is confusing

### 3.2 MEDIUM PRIORITY Issues

#### Issue M1: Skill Ordering - Ground Detection
**Skills:**
- T17.G6.04.02: Enable ground detection for jump control (G6)
- T17.G5.10.01: Remove physics body from a sprite (G5)

**Problem:** Ground detection is taught in G6, but it's a relatively simple concept that could be introduced earlier. However, it depends on understanding collision detection, so G6 placement may be appropriate.

**Recommendation:** Keep as-is. The progression makes sense:
- G5: Basic physics setup and bodies
- G6: Collision detection then Ground detection is a specialized form

**Severity:** LOW - Current placement is acceptable

#### Issue M2: Missing Application Skill - Collision End Events
**Block:** physics_broadcastcollisioneventmessage2 (collision end)
**Current Coverage:** T17.G6.04.01: Detect collision end events

**Problem:** The skill description is very generic. It doesn't provide concrete examples of when collision END is more useful than collision START.

**Recommendation:** Enhance T17.G6.04.01 description:
- Current: "Students use broadcast [message] when finish colliding with [sprite] to trigger actions when objects stop touching. They use collision end events for exit zones, releasing grabbed objects, or state transitions."
- Better: Add specific example: "For example, in a platformer, collision START with lava damages the player, but collision END with lava stops the damage-over-time effect. In a puzzle game, collision END with a button releases it after being pressed."

**Severity:** LOW - Current description is acceptable but could be improved

#### Issue M3: Dependency Chain Verification - Manual Physics
**Skills:**
- T17.G5.03.01: Build top-down vehicle (depends on G5.03)
- T17.G5.04.01: Create simple platformer (depends on G5.04)

**Problem:** These are application skills that depend on manual physics. However, students who go straight to the physics engine (G5.05+) won't have these manual physics dependencies.

**Current Setup:** The dependency tree allows students to either:
- Path A: Learn manual physics (G5.02-G5.04) then Application projects (G5.03.01, G5.04.01)
- Path B: Skip manual physics, go to engine (G5.05+)
- Path C: Do both, then compare (G5.12)

**Recommendation:** This is actually GOOD design! The dependency structure allows flexibility. Keep as-is.

**Severity:** NOT AN ISSUE - This is a feature, not a bug

#### Issue M4: Missing Cross-Reference - Velocity Reporters
**Skills:**
- T17.G7.05: Read velocity and mass reporters
- T17.G6.02.01: Set velocity directly for physics bodies

**Problem:** Students learn to SET velocity in G6.02.01 but don't learn to READ velocity reporters until G7.05. This is a 1-grade gap.

**Current Dependencies:**
- T17.G7.05 depends on: T17.G6.07 (Debug unstable), T17.G6.08 (Compare simulations)

**Recommendation:** Consider adding an earlier introduction to velocity reporters:
- Option A: Add T17.G6.02.01.02: Read velocity values after setting them
  - Dependencies: T17.G6.02.01
  - Description: Students use (x speed) and (y speed) reporter blocks to verify that velocity was set correctly. They display velocity values on screen and check that they match expected values after using set velocity blocks.

- Option B: Keep as-is, since reading reporters is more naturally needed for debugging (G7)

**Recommendation:** Add Option A skill for better immediate feedback

**Severity:** MEDIUM - Gap exists but not critical

#### Issue M5: Advanced Skills Without Prerequisites - Rotation Speed and Torque
**Skill:** T17.G7.04.01: Use rotation speed and torque
**Current Dependencies:** T17.G7.04 (Build chains or stacks)

**Problem:** This skill covers THREE different blocks:
- set rotation speed [value] (direct control)
- add torque [value] (continuous force)
- apply torque impulse [value] (one-time force)

These are three different concepts that should be scaffolded separately.

**Current Coverage:**
- physics_setrotationspeed: Covered in T17.G7.04.01
- physics_addtorque: Covered in T17.G7.04.01
- physics_applytorqueimpulse: Covered in T17.G7.04.01

**Recommendation:** Break down T17.G7.04.01:
- **T17.G6.02.01.03: Set rotation speed directly** (parallel to velocity setting in G6.02.01)
  - Dependencies: T17.G6.02.01
  - Description: Students use set rotation speed [value] to directly control how fast a physics body rotates. They compare direct rotation speed setting to using rotation impulses and understand when each approach is appropriate.

- **T17.G7.04.01: Use continuous torque for sustained rotation**
  - Dependencies: T17.G7.02 (Combine multiple forces)
  - Description: Students use add torque [value] to apply continuous rotational force to physics bodies. They build spinning platforms, rotating obstacles, and objects that continuously accelerate their rotation.

- **T17.G7.04.01.01: Apply torque impulse for instant rotation**
  - Dependencies: T17.G7.04.01, T17.G5.08.02 (Apply impulse at position)
  - Description: Students use apply torque impulse [value] to create instant rotational velocity changes. Examples: hitting a spinning wheel to change its rotation, applying sudden spin to objects, creating rotation without sustained force.

**Severity:** HIGH - Three different concepts bundled together

### 3.3 LOW PRIORITY Issues

#### Issue L1: Terminology Consistency
**Problem:** Some skills use "2D physics body" while others just say "physics body"

**Recommendation:** Standardize to "physics body" since T17 is explicitly about 2D physics (3D physics is in a different topic). The "2D" qualifier is redundant in context.

**Severity:** LOW - Cosmetic issue

#### Issue L2: Missing Real-World Connection - CCD
**Skill:** T17.G7.01.02: Enable CCD for fast projectiles
**Current Description:** "Enable Continuous Collision Detection (CCD) for fast-moving projectiles to prevent tunneling through walls"

**Problem:** Very technical description without explaining WHEN students would notice they need CCD.

**Recommendation:** Enhance description:
- "Students observe a problem where fast-moving projectiles (like bullets) pass through walls instead of colliding. They learn this is called 'tunneling' and happens when objects move too far in a single physics update. They use enable collision detection as a fast object [Yes] to enable CCD (Continuous Collision Detection), which uses a higher update frequency to catch collisions that would otherwise be missed."

**Severity:** LOW - Current description is functional but could be more pedagogical

#### Issue L3: Missing Skill - Collision Group Explanation
**Current Coverage:**
- T17.G6.04.03: Identify collision management needs (planning)
- T17.G6.05: Set up static collision groups for filtering (implementation)

**Problem:** The jump from planning (G6.04.03) to implementation (G6.05) is steep. The concept of collision groups (0-15) and how filtering works is complex.

**Current Description (T17.G6.05):** "Set up collision groups to filter which objects can interact with each other"

**Problem:** This doesn't explain the mental model:
1. Add object to group (e.g., player to group 1, enemies to group 2)
2. Enable collision filter (player enables collision with group 2)
3. Bidirectional setup needed (enemies also enable collision with group 1)

**Recommendation:** Enhance T17.G6.05 description with detailed explanation:
- "Students use collision groups to control which objects can collide with each other. They learn the three-step process: (1) Add objects to groups (0-15) using add to collision group, (2) Enable which groups each object can collide with using enable collision with group, and (3) Understand that collision filters must be bidirectional - if player (group 1) should collide with enemies (group 2), then player must enable collision with group 2 AND enemies must enable collision with group 1. Examples: bullets pass through teammates but hit enemies, ghosts phase through walls, power-up shields make player ignore hazards."

**Severity:** MEDIUM - Complex concept needs better explanation

---

## 4. Missing Block Coverage

### 4.1 Blocks WITH Skill Coverage - All 47 blocks covered

All 47 physics blocks have at least some coverage in the skill tree.

#### Fully Covered Blocks (Dedicated Skills):
All blocks are covered. See section 1 for complete mapping.

---

## 5. Dependency Analysis (X-2 Rule Violations)

### 5.1 Within-Topic Dependencies (T17 to T17)

**Analysis:** All T17 to T17 dependencies follow proper scaffolding. No violations found.

### 5.2 Cross-Topic Dependencies

As noted in the file comment at line 11043-11046:
```
Several G6-G7 skills have cross-topic dependencies on T07/T08/T09.G3 skills,
creating 3-4 grade gaps. This is acceptable since they are cross-topic dependencies
and will be addressed in Phase 2 cross-topic dependency optimization.
```

**Examples:**
- T17.G6.05 depends on T08.G4.01 (3-grade gap)
- T17.G7.01 depends on T08.G5.01, T09.G3.01.04 (4-grade gap)

**Recommendation:** These are acceptable and will be addressed in Phase 2. The T17 internal scaffolding is correct.

---

## 6. Picture-Based vs Block-Based Verification

### 6.1 K-2 Skills (Should be Picture-Based)

| ID | Title | Status |
|----|-------|--------|
| T17.K.01 | Observe sprite position changes (picture-based) | CORRECT |
| T17.K.02 | Match sprite to position after motion (picture-based) | CORRECT |
| T17.G1.01 | Identify fast vs slow motion (picture-based) | CORRECT |
| T17.G2.01 | Predict sprite direction from motion blocks (picture choices) | CORRECT |

**All K-2 skills are properly picture-based!**

### 6.2 Grade 3+ Skills (Should be Block-Based)

All G3+ skills involve hands-on coding with blocks. CORRECT

---

## 7. Detailed Recommendations

### 7.1 IMMEDIATE FIXES (Before Any Other Work)

#### Fix 1: Add Debug Mode Skill
Insert after T17.G5.06.A (line approximately 10911):

```
ID: T17.G5.06.A.01
Topic: T17 – 2D Motion & Physics
Skill: Use debug mode to visualize collision shapes
Description: Students enable debug mode when creating physics bodies (debug [Yes]) to see the actual collision shape outline overlaid on sprites. They use this to verify that collision shapes match sprite visuals appropriately, identify why collisions aren't working as expected, and understand the difference between the visible sprite and its collision boundary.

Dependencies:
* T17.G5.06.A: Practice creating multiple dynamic bodies
```

Update T17.G5.06.01 dependency from T17.G5.06.A to T17.G5.06.A.01

#### Fix 2: Split World Border Skills
Replace T17.G6.07.01 (current line approximately 11221):

```
ID: T17.G6.07.01
Topic: T17 – 2D Motion & Physics
Skill: Configure world border friction and restitution
Description: Students use set world border collider friction [value]% restitution [value]% to customize the physical properties of the automatic stage boundaries. They create bouncy walls for pinball effects (high restitution), sticky borders to slow objects down (high friction, low restitution), or completely non-bouncy edges (0% restitution) for realistic simulations.

Dependencies:
* T17.G5.05: Initialize a 2D physics world
* T17.G6.01: Configure surface friction parameters
```

Replace T17.G6.07.02 (current line approximately 11231):

```
ID: T17.G6.07.02
Topic: T17 – 2D Motion & Physics
Skill: Configure world border collision groups for selective interactions
Description: Students use set world border collision group [COLLISIONGROUP] colliding with group [TARGETGROUP] to make stage boundaries selectively collide with different object types. Examples: players bounce off borders but bullets pass through, enemies are contained but power-ups can float off-screen, or create wrap-around effects by disabling border collisions for specific groups.

Dependencies:
* T17.G6.05: Set up static collision groups for filtering
* T17.G6.07.01: Configure world border friction and restitution
```

#### Fix 3: Break Down Rotation Skills
Insert after T17.G6.02.01.01 (line approximately 11084):

```
ID: T17.G6.02.01.02
Topic: T17 – 2D Motion & Physics
Skill: Read velocity reporters for verification
Description: Students use (x speed) and (y speed) reporter blocks to verify that velocity was set correctly after using velocity control blocks. They display velocity values on screen, compare them to expected values, and use this feedback to debug motion problems and understand how forces and damping affect velocity over time.

Dependencies:
* T17.G6.02.01: Set velocity directly for physics bodies
```

```
ID: T17.G6.02.01.03
Topic: T17 – 2D Motion & Physics
Skill: Set rotation speed directly
Description: Students use set rotation speed [value] to directly control how fast a physics body rotates (degrees per second). They compare direct rotation speed setting to using torque and torque impulses, understanding when direct control (moving platforms, controlled rotation) vs. physics-driven rotation (tumbling objects, realistic impacts) is appropriate.

Dependencies:
* T17.G6.02.01: Set velocity directly for physics bodies
```

Replace T17.G7.04.01 (current line approximately 11337):

```
ID: T17.G7.04.01
Topic: T17 – 2D Motion & Physics
Skill: Use continuous torque for sustained rotation
Description: Students use add torque [value] to apply continuous rotational force to physics bodies. They build spinning platforms, rotating obstacles, and objects that continuously accelerate their rotation. They observe how torque creates angular acceleration (increasing rotation speed) while direct rotation speed setting maintains constant rotation.

Dependencies:
* T17.G6.02.01.03: Set rotation speed directly
* T17.G7.02: Combine multiple forces simultaneously
```

Insert after T17.G7.04.01:

```
ID: T17.G7.04.01.01
Topic: T17 – 2D Motion & Physics
Skill: Apply torque impulse for instant rotation
Description: Students use apply torque impulse [value] to create instant rotational velocity changes without sustained force. They compare torque (continuous rotational force) with torque impulse (one-time rotational kick) and build examples: hitting a spinning wheel to change its rotation, applying sudden spin to objects on impact, creating rotation effects without ongoing torque.

Dependencies:
* T17.G5.08.02: Apply impulse at a position for rotation
* T17.G7.04.01: Use continuous torque for sustained rotation
```

#### Fix 4: Enhance Collision Group Description
Update T17.G6.05 description:

```
Description: Students use collision groups (0-15) to control which objects can collide with each other. They learn the three-step process: (1) Add objects to groups using add to collision group [G], (2) Enable which groups each object can collide with using enable collision with group [G], and (3) Understand that collision filters must be bidirectional - if player (group 1) should collide with enemies (group 2), then player must enable collision with group 2 AND enemies must enable collision with group 1. Important: Objects not in any group collide with everything; once added to a group, must explicitly enable collision with other groups. Examples: bullets pass through teammates but hit enemies, ghosts phase through walls, power-up shields make player ignore hazards temporarily.
```

#### Fix 5: Enhance CCD Description
Update T17.G7.01.02 description:

```
Description: Students observe a problem where fast-moving projectiles (like bullets or arrows) pass through walls instead of colliding. They learn this is called 'tunneling' and happens when objects move so far in a single physics update that they "jump" from one side of a wall to the other without ever touching it. They use enable collision detection as a fast object [Yes] to enable CCD (Continuous Collision Detection), which uses a higher update frequency to catch collisions that would otherwise be missed. They test with and without CCD to see the difference.
```

#### Fix 6: Enhance Collision End Events Description
Update T17.G6.04.01 description:

```
Description: Students use broadcast [message] when finish colliding with [sprite] to trigger actions when objects stop touching. They understand when collision END is more useful than collision START: damage-over-time effects that stop when objects separate, buttons that release after being pressed, grabbed objects that are released, entering and exiting zones (START = enter zone, END = exit zone), or state transitions that need both contact and separation events. Example: lava damages player on contact (START) and stops damage when player escapes (END).
```

### 7.2 MEDIUM PRIORITY IMPROVEMENTS

#### Improvement 1: Update Prismatic Joint Warning
Update T17.G8.02.02 description:

Add prominent warning at the beginning:
"IMPORTANT: Prismatic joints are PERMANENT once created and cannot be removed. Plan constraint usage during the design phase before implementing."

#### Improvement 2: Standardize Terminology
Perform global find/replace:
- "2D physics body" to "physics body" (in T17 context)
- "2D physics engine" to "physics engine" (in T17 context)

#### Improvement 3: Add Cross-References
Add notes to relevant skills mentioning related concepts:
- T17.G5.08.01 (forces) - mention T17.G7.04.01 (torque)
- T17.G6.02.01 (set velocity) - mention T17.G7.05 (read velocity)

---

## 8. Summary of All Physics Blocks

### Quick Reference Chart

| Block ID | Block Name | Grade Introduced | Skill ID(s) |
|----------|-----------|------------------|-------------|
| physics_enablephysics | initialize physics world | G5 | T17.G5.05 |
| physics_setphysicsbody | behave as body (simple) | G5 | T17.G5.06 |
| physics_setphysicsbody2 | behave as body (compound) | G5 | T17.G5.06.03 |
| physics_removecollider | remove physics behavior | G5 | T17.G5.10.01 |
| physics_updatephysicsbody | update density/friction/restitution | G5 | T17.G5.09, T17.G6.01, T17.G6.02 |
| physics_setvelocityx | set x speed | G6 | T17.G6.02.01 |
| physics_setvelocityy | set y speed | G6 | T17.G6.02.01 |
| physics_setvelocitydir | set speed in direction | G6 | T17.G6.02.01 |
| physics_setvelocitymovingdir | set speed in moving direction | G6 | T17.G6.02.01.01 |
| physics_setrotationspeed | set rotation speed | G6 | T17.G6.02.01.03 (NEW) |
| physics_setdirbyvelocity | point in direction of speed | G7 | T17.G7.01.01 |
| physics_addforce | add force (center) | G7 | T17.G7.02 |
| physics_addforce2 | add force at position | G7 | T17.G7.02.02 |
| physics_clearforce | remove all forces | G7 | T17.G7.02.01 |
| physics_addtorque | add torque | G7 | T17.G7.04.01 (UPDATED) |
| physics_cleartorque | remove all torques | G7 | T17.G7.02.01 |
| physics_applyimpulse | apply impulse (center) | G5 | T17.G5.08, T17.G7.01 |
| physics_applyimpulse2 | apply impulse at position | G5 | T17.G5.08.02 |
| physics_applytorqueimpulse | apply torque impulse | G7 | T17.G7.04.01.01 (NEW) |
| physics_lockmovement | prevent body movement | G6 | T17.G6.06.01 |
| physics_lockrotation | prevent body rotation | G6 | T17.G6.06.01 |
| physics_setdampingfactor | set damping factor | G7 | T17.G7.03.01 |
| physics_broadcastcollisioneventmessage | broadcast on collision start | G6 | T17.G6.04 |
| physics_broadcastcollisioneventmessage2 | broadcast on collision end | G6 | T17.G6.04.01 (UPDATED) |
| physics_addtocollisiongroup | add to collision group | G6 | T17.G6.05 (UPDATED) |
| physics_removefromcollisiongroup | remove from collision group | G6 | T17.G6.05.01 |
| physics_addcollisionfilter | enable collision with group | G6 | T17.G6.05 |
| physics_removecollisionfilter | disable collision with group | G6 | T17.G6.05 |
| physics_setdominancegroup | set dominance group | G6 | T17.G6.05.02 |
| physics_setccd | enable CCD for fast objects | G7 | T17.G7.01.02 (UPDATED) |
| physics_setgravityscale | set gravity scale | G8 | T17.G8.05 |
| physics_settimespeed | set physics time speed | G8 | T17.G8.05 |
| physics_addfixedjoint | fix relative position | G8 | T17.G8.02 |
| physics_removefixedjoint | remove position constraint | G8 | T17.G8.02 |
| physics_addrevoltejoint | set rotation axis | G8 | T17.G8.02.01 |
| physics_removerevoltejoint | remove rotation axis | G8 | T17.G8.02.01 |
| physics_setrotationaxisspeed | set rotation axis speed | G8 | T17.G8.02.01.01 |
| physics_addprismaticjoint | allow sliding | G8 | T17.G8.02.02 (UPDATED) |
| physics_setedgecollider | set border friction/restitution | G6 | T17.G6.07.01 (UPDATED) |
| physics_setedgecollisiongroup | set border collision group | G6 | T17.G6.07.02 (UPDATED) |
| physics_turnoncollisiondetection | turn on ground detection | G6 | T17.G6.04.02 |
| physics_getvelocityx | (x speed) reporter | G6 | T17.G6.02.01.02 (NEW) |
| physics_getvelocityy | (y speed) reporter | G6 | T17.G6.02.01.02 (NEW) |
| physics_getMass | (mass) reporter | G7 | T17.G7.05 |
| physics_getangularvelocity | (angular speed) reporter | G7 | T17.G7.05 |
| physics_getcollidingbottom | (in collision below) reporter | G6 | T17.G6.04.02 |
| physics_getgroundslope | (ground slope) reporter | G6 | T17.G6.04.02.01 |

---

## 9. Action Items Summary

### HIGH Priority (Fix Before Launch)
1. Add T17.G5.06.A.01: Use debug mode to visualize collision shapes
2. Split T17.G6.07.01 into separate friction/restitution skill
3. Split T17.G6.07.02 into separate collision group skill
4. Break down T17.G7.04.01 into three rotation skills (set speed, torque, torque impulse)
5. Add T17.G6.02.01.02: Read velocity reporters for verification
6. Enhance T17.G6.05 description with detailed collision group explanation

### MEDIUM Priority (Important Improvements)
7. Enhance T17.G7.01.02 CCD description with tunneling explanation
8. Enhance T17.G6.04.01 collision end events with specific examples
9. Update T17.G8.02.02 with prominent prismatic joint warning
10. Consider standardizing "2D physics" to "physics" terminology

### LOW Priority (Polish)
11. Add cross-references between related skills
12. Consider adding more application project skills
13. Consider adding comparison skills

---

## 10. Conclusion

The T17 (2D Motion & Physics) skill map is **well-designed** with excellent scaffolding from K through Grade 8. The progression from picture-based observation to manual physics to physics engine is pedagogically sound.

**Strengths:**
- Comprehensive coverage of all 47 physics blocks
- Excellent K-2 picture-based foundation
- Strong manual physics foundation (G5.02-G5.04) before engine introduction
- Well-structured dependency tree
- Good balance of conceptual and application skills

**Areas for Improvement:**
- Some overly broad skills need to be broken down (rotation, world borders)
- A few missing intermediate skills (debug mode, velocity reporters in G6)
- Some descriptions need enhancement for clarity (collision groups, CCD, collision end)

**Overall Assessment:** 8.5/10 - Very strong topic with minor improvements needed.

**Estimated Work Required:**
- Add 4 new skills
- Update 6 skill descriptions
- Update dependencies for affected skills
- Estimated time: 3-4 hours

---

End of Report
