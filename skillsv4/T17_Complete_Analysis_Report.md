# T17 (2D Motion & Physics) - Complete Analysis Report

## Executive Summary

Topic T17 contains **65 skills** spanning grades K-8, covering both manual physics (velocity variables) and CreatiCode's Rapier-based 2D physics engine. The skills progression is generally well-structured but has several issues requiring attention:

- **Coverage**: Good coverage of core physics blocks, but missing some advanced features
- **Grade Appropriateness**: K-G2 skills properly use picture-based approaches
- **Dependencies**: Several X-2 rule violations, especially in G5-G6 range
- **Complexity**: Some skills try to cover too much; need breakdown
- **Gaps**: Missing skills for some available blocks and intermediate concepts

---

## Part 1: Complete T17 Skills Inventory

### Kindergarten (2 skills)
- **T17.K.01**: Observe sprite position changes (picture-based) - No deps
- **T17.K.02**: Match sprite to position after motion (picture-based) - Deps: T17.K.01

### Grade 1 (1 skill)
- **T17.G1.01**: Identify fast vs slow motion (picture-based) - Deps: T17.K.02

### Grade 2 (1 skill)
- **T17.G2.01**: Predict sprite direction from motion blocks (picture choices) - Deps: T17.G1.01

### Grade 3 (2 skills)
- **T17.G3.01**: Observe position changes from motion blocks - Deps: T06.G3.01, T17.G2.01
- **T17.G3.02**: Predict direction and distance of sprite motion - Deps: T17.G3.01

### Grade 4 (2 skills)
- **T17.G4.01**: Simulate falling with repeated motion - Deps: T07.G3.01, T17.G3.02
- **T17.G4.02**: Explain speed as position change over time - Deps: T09.G3.05, T17.G4.01

### Grade 5 (18 skills)

#### Manual Physics (G5.02-G5.04)
- **T17.G5.02**: Track gravity with velocity variables - Deps: T07.G3.05, T09.G3.05, T17.G4.02
- **T17.G5.03**: Use horizontal speed and friction variables - Deps: T09.G4.03, T17.G5.02
- **T17.G5.04**: Code a manual bounce with energy loss - Deps: T08.G3.01, T17.G5.02

#### Physics Engine Basics (G5.05-G5.11)
- **T17.G5.05**: Initialize a 2D physics world - Deps: T06.G3.01, T17.G4.02
- **T17.G5.06**: Attach a dynamic body to a sprite - Deps: T17.G5.05
- **T17.G5.06.A**: Practice creating multiple dynamic bodies - Deps: T17.G5.06
- **T17.G5.06.01**: Select basic body shapes (Box, Circle, Capsule) - Deps: T17.G5.06.A
- **T17.G5.06.02**: Create sensor bodies for trigger zones - Deps: T17.G5.06.01
- **T17.G5.06.03**: Create compound shapes for complex sprites - Deps: T17.G5.06.01
- **T17.G5.07**: Build fixed boundaries for floors and walls - Deps: T17.G5.05
- **T17.G5.08**: Apply an impulse to jump or push - Deps: T06.G4.01, T17.G5.06
- **T17.G5.08.01**: Distinguish forces from impulses - Deps: T17.G5.08
- **T17.G5.08.02**: Apply impulse at a position for rotation - Deps: T17.G5.08.01
- **T17.G5.09**: Configure density for mass control - Deps: T17.G5.06
- **T17.G5.10**: Trace simple 2D physics motion - Deps: T09.G3.05, T17.G5.06
- **T17.G5.10.01**: Remove physics body from a sprite - Deps: T17.G5.06
- **T17.G5.11**: Debug missing physics setup - Deps: T17.G5.06, T17.G5.07

#### Synthesis
- **T17.G5.12**: Choose manual vs engine-based physics - Deps: T05.G4.05, T17.G5.04, T17.G5.11

### Grade 6 (19 skills)

#### Surface Properties
- **T17.G6.01**: Configure surface friction parameters - Deps: T08.G3.01, T09.G3.05, T17.G5.10
- **T17.G6.02**: Control restitution (bounce) parameters - Deps: T09.G3.05, T17.G6.01

#### Velocity Control
- **T17.G6.02.01**: Set velocity directly for physics bodies - Deps: T17.G5.06, T17.G5.08
- **T17.G6.02.01.01**: Maintain constant speed in current direction - Deps: T17.G6.02.01
- **T17.G6.02.02**: Compare dynamic vs movable body types - Deps: T17.G5.06, T17.G6.02.01
- **T17.G6.03**: Build a movable (kinematic) moving platform - Deps: T07.G3.05, T17.G6.02.02

#### Collision Detection
- **T17.G6.04**: Detect collisions for scoring or triggers - Deps: T06.G4.01, T17.G5.10
- **T17.G6.04.01**: Detect collision end events - Deps: T17.G6.04
- **T17.G6.04.02**: Use ground detection for platformer jumping - Deps: T17.G6.04
- **T17.G6.04.03**: Identify collision management needs - Deps: T17.G6.04

#### Collision Groups
- **T17.G6.05**: Use collision groups to filter interactions - Deps: T08.G4.01, T17.G6.04.03
- **T17.G6.05.01**: Use dominance groups for one-way interactions - Deps: T17.G6.05

#### Integration & Debugging
- **T17.G6.06**: Blend manual and engine sprites in a level - Deps: T17.G5.10, T17.G5.11
- **T17.G6.06.01**: Lock movement or rotation of physics bodies - Deps: T17.G5.06
- **T17.G6.07**: Debug unstable physics behavior - Deps: T17.G6.01, T17.G6.02
- **T17.G6.07.01**: Configure world border properties - Deps: T17.G5.05, T17.G6.01
- **T17.G6.08**: Compare simulations to real-world motion - Deps: T08.G3.01, T09.G3.05, T17.G5.10

### Grade 7 (17 skills)

#### Projectile Motion & Forces
- **T17.G7.01**: Launch a configurable projectile - Deps: T08.G5.01, T09.G3.01.04, T17.G6.08
- **T17.G7.01.01**: Point sprite in movement direction - Deps: T17.G7.01
- **T17.G7.02**: Combine multiple forces simultaneously - Deps: T17.G5.08.01, T17.G6.07, T17.G6.08
- **T17.G7.02.01**: Clear forces and torques from physics bodies - Deps: T17.G7.02
- **T17.G7.02.02**: Apply force at a position for continuous rotation - Deps: T17.G5.08.02, T17.G7.02

#### Drag & Damping
- **T17.G7.03**: Simulate drag with manual force calculations - Deps: T17.G6.07, T17.G6.08
- **T17.G7.03.01**: Use built-in damping as alternative to manual drag - Deps: T17.G7.03

#### Complex Interactions
- **T17.G7.04**: Build chains or stacks of physics objects - Deps: T17.G6.07, T17.G6.08
- **T17.G7.04.01**: Use rotation speed and torque - Deps: T17.G7.04

#### Data & Analysis
- **T17.G7.05**: Read velocity and mass reporters - Deps: T17.G6.07, T17.G6.08
- **T17.G7.05.01**: Instrument and graph motion data - Deps: T10.G5.01, T17.G7.05

#### Real-World Modeling
- **T17.G7.06**: Model a real-world physics scenario - Deps: T08.G5.01, T09.G3.01.04, T17.G6.08
- **T17.G7.07**: Evaluate whether a simulation meets requirements - Deps: T17.G6.07, T17.G6.08

### Grade 8 (5 skills)

#### Advanced Projects
- **T17.G8.01**: Design and balance a physics-based arcade game - Deps: T07.G6.01, T08.G6.01, T17.G7.06

#### Joints & Constraints
- **T17.G8.02**: Implement fixed joints for connected objects - Deps: T09.G6.01, T17.G7.06
- **T17.G8.02.01**: Implement revolute joints for hinges - Deps: T17.G8.02
- **T17.G8.02.02**: Implement prismatic joints for sliding - Deps: T17.G8.02.01

#### Testing & Optimization
- **T17.G8.03**: Build automated physics regression tests - Deps: T08.G6.01, T17.G7.07
- **T17.G8.04**: Optimize a physics scene for performance - Deps: T07.G6.01, T17.G7.06, T17.G7.07
- **T17.G8.04.01**: Enable CCD for fast-moving objects - Deps: T17.G8.04
- **T17.G8.05**: Control gravity scale and time speed - Deps: T17.G7.06
- **T17.G8.06**: Use instrumentation data to tune difficulty - Deps: T09.G6.01, T17.G7.06

---

## Part 2: Available CreatiCode Blocks

### 2D Physics Blocks (46 blocks total)

#### World Initialization
1. `initialize 2D physics world with gravity x [X] y [Y]` - Setup world with gravity

#### Body Creation
2. `behave as a [TYPE] [SENSORTYPE] shape [SHAPETYPE] debug [DODEBUG]` - Simple shapes (Box, Circle, Capsule, Convex Hull)
3. `behave as a [TYPE] [SENSORTYPE] in compound shape with curve tolerance [TOLERANCE] point distance [DISTANCE] debug [DODEBUG]` - Complex shapes
4. `remove physics-based behavior` - Remove physics body

#### Properties
5. `update density (DENSITY) friction (FRICTION)% restitution (RESTITUTION)%` - Material properties

#### Velocity Control
6. `set x speed (SPEED)` - Set horizontal velocity
7. `set y speed (SPEED)` - Set vertical velocity
8. `set speed (SPEED) in direction (DIR)` - Set velocity by direction
9. `set speed (SPEED) in moving direction` - Maintain speed, preserve direction
10. `set rotation speed (SPEED)` - Set angular velocity
11. `point in direction of speed` - Align sprite with velocity

#### Forces & Impulses
12. `add force (FORCE) in direction (DIR)` - Continuous force at center
13. `add force (FORCE) in direction (DIR) at position x (XPOS) y (YPOS)` - Continuous force at position
14. `remove all forces` - Clear accumulated forces
15. `add torque (TORQUE)` - Continuous rotational force
16. `remove all torques` - Clear accumulated torques
17. `apply impulse (FORCE) in direction (DIR)` - One-time impulse at center
18. `apply impulse (FORCE) in direction (DIR) at position x (POSX) y (POSY)` - One-time impulse at position
19. `apply torque impulse (TORQUE)` - One-time rotational impulse

#### Body Constraints
20. `prevent body movement from forces [DOPREVENT]` - Lock translation
21. `prevent body rotation from forces [DOPREVENT]` - Lock rotation
22. `set damping factor for movement (MOVEMENTDAMPING) % rotation (ROTATIONDAMPING) %` - Air resistance

#### Collision Events
23. `broadcast [MESSAGE] when colliding with [SPRITENAME v]` - Collision start
24. `broadcast [MESSAGE] when finish colliding with [SPRITENAME v]` - Collision end

#### Collision Groups
25. `add to collision group [G]` - Add to group (0-15)
26. `remove from collision group [G]` - Remove from group
27. `enable collision with group [G]` - Enable collision with group
28. `disable collision with group [G]` - Disable collision with group
29. `set dominance group to (G)` - One-way pushing (-127 to 127)

#### Advanced Features
30. `enable collision detection as a fast object [ISFAST]` - CCD for fast objects
31. `set gravity scale (SCALE) %` - Per-body gravity multiplier
32. `set physics time speed (SPEED) %` - Global time scale

#### Joints/Constraints
33. `fix relative position to [SPRITENAME v]` - Fixed joint
34. `remove relative position constraint` - Remove fixed joint
35. `set [SPRITENAME v] as rotation axis with offset x (OFFSETX) y (OFFSETY)` - Revolute joint
36. `remove rotation axis` - Remove revolute joint
37. `set rotation axis speed (SPEED) damping factor (DAMPINGFACTOR) %` - Motor control
38. `allow [DIRECTION] sliding relative to [SPRITENAME v] range from (MINDISTANCE) to (MAXDISTANCE)` - Prismatic joint

#### World Borders
39. `set world border collider friction (FRICTION)% restitution (RESTITUTION)%` - Border properties
40. `set world border collision group [COLLISIONGROUP] colliding with group [TARGETGROUP]` - Border collision filtering

#### Ground Detection
41. `turn on ground detection within distance (DISTANCE) debug [DODEBUG]` - Enable raycast ground detection

#### Reporters
42. `(x speed)` - Get horizontal velocity
43. `(y speed)` - Get vertical velocity
44. `(angular speed)` - Get rotation velocity
45. `<in collision below>` - Ground touch boolean
46. `(ground slope)` - Ground angle
47. `(mass)` - Get calculated mass (density × area)

### Motion Blocks (Relevant to 2D physics understanding)

#### Basic Motion
- `move (N) steps` - Move forward
- `point in direction (DIR)` - Set direction
- `turn cw (N) degrees` / `turn ccw (N) degrees` - Rotate
- `go to x: (XPOS) y: (YPOS)` - Teleport
- `glide (T) secs to x: (XPOS) y: (YPOS)` - Smooth interpolated motion
- `change x by (N)` / `set x to (N)` - X position control
- `change y by (N)` / `set y to (N)` - Y position control

#### Reporters
- `(x position)` / `(y position)` / `(direction)` - Position/direction queries

#### Viewport (for scrolling/camera)
- `viewport x` / `viewport y` - Viewport position
- `attach to viewport at x (XPOS) y (YPOS)` - Fix to camera
- `move viewport to x (XPOS) y (YPOS)` - Move camera
- `lock viewport to sprite [SPRITENAME v]` - Follow sprite

---

## Part 3: Issues Analysis

### HIGH PRIORITY ISSUES

#### H1: X-2 Rule Violations in G5-G6 Skills

**Problem**: Several G6 skills depend on G3 skills, violating the X-2 rule.

**Specific Cases**:
- **T17.G6.01** (Configure surface friction) depends on T08.G3.01, T09.G3.05
- **T17.G6.02** (Control restitution) depends on T09.G3.05
- **T17.G6.03** (Build movable platform) depends on T07.G3.05
- **T17.G6.04** (Detect collisions) depends on T17.G5.10 (OK), but chains back to G3 skills
- **T17.G6.08** (Compare simulations) depends on T08.G3.01, T09.G3.05

**Impact**: Students may encounter skills before mastering prerequisite concepts from other topics.

**Recommendation**:
1. Move G6.01, G6.02 dependency checks to within-topic T17 skills
2. Consider creating T17.G5.x skills that combine the needed T08/T09 concepts specifically in physics context
3. OR: Accept cross-topic dependencies but ensure they're necessary (friction/restitution genuinely need conditionals and variables)

#### H2: Missing Skills for Block Coverage

**Missing blocks with no corresponding skills**:

1. **Rotation axis motor control** - `set rotation axis speed (SPEED) damping factor (DAMPINGFACTOR) %`
   - Current: T17.G8.02.01 mentions revolute joints but doesn't cover motor control
   - Needed: Skill for powered rotation (motors, spinning platforms)

2. **Fast object CCD** - `enable collision detection as a fast object [ISFAST]`
   - Current: T17.G8.04.01 exists BUT it's buried under optimization
   - Needed: Should be introduced earlier as essential for bullets/projectiles

3. **Per-body gravity scale** - `set gravity scale (SCALE) %`
   - Current: T17.G8.05 exists but very late
   - Needed: Could be useful in G7 for floaty characters, reverse gravity zones

4. **World border collision filtering** - `set world border collision group [COLLISIONGROUP] colliding with group [TARGETGROUP]`
   - Current: T17.G6.07.01 mentions it but doesn't practice it
   - Needed: Practical skill for making objects that can leave the stage

#### H3: Overly Complex Skills Needing Breakdown

**T17.G5.06.01** - "Select basic body shapes (Box, Circle, Capsule)"
- **Problem**: Covers Box, Circle, Capsule, AND mentions Convex Hull as advanced
- **Fix**: Split into:
  - T17.G5.06.01: Choose Box vs Circle collision shapes
  - T17.G5.06.01.01: Use Capsule shapes for elongated objects
  - T17.G5.06.01.02: Use Convex Hull for automatic fitting (advanced)

**T17.G6.04.02** - "Use ground detection for platformer jumping"
- **Problem**: Covers enabling ground detection, using `<in collision below>`, AND using `(ground slope)` reporter
- **Fix**: Split into:
  - T17.G6.04.02: Enable ground detection and use `<in collision below>` for jumping
  - T17.G6.04.02.01: Use `(ground slope)` reporter for slope-based behavior

**T17.G6.05** - "Use collision groups to filter interactions"
- **Problem**: Covers add/remove/enable/disable AND dynamic group changes
- **Fix**: Split into:
  - T17.G6.05: Set up static collision groups for object types
  - T17.G6.05.01: Dynamically change collision groups (invincibility, phasing)
  - T17.G6.05.02: Use dominance groups for one-way interactions

**T17.G8.04** - "Optimize a physics scene for performance"
- **Problem**: Lists 7 different optimization strategies
- **Fix**: Create sub-skills:
  - T17.G8.04: Identify physics performance bottlenecks
  - T17.G8.04.01: Optimize collision shapes for performance
  - T17.G8.04.02: Reduce active physics bodies
  - T17.G8.04.03: Enable CCD for fast-moving objects

### MEDIUM PRIORITY ISSUES

#### M1: Dependency Chain Complexity

**T17.G6.08** is a bottleneck:
- Many G7 skills depend on T17.G6.08 (Compare simulations to real-world motion)
- This creates a forced checkpoint that may not be necessary
- Example: T17.G7.01 (Launch projectile) could depend on simpler physics skills

**Recommendation**: Review if T17.G6.08 is truly prerequisite for all G7 skills, or if some could proceed with just G6.04 (collision detection) + G5 basics.

#### M2: Manual Physics Sequence (G5.02-G5.04) Isolation

**Current**: Manual physics (velocity variables) taught in G5.02-G5.04
**Issue**: Only T17.G5.12 (Choose manual vs engine) connects them to engine-based physics
**Gap**: Students don't practice manual physics with real control scenarios

**Recommendation**: Add skill(s):
- **T17.G5.03.01**: Build a top-down car game with manual friction
- **T17.G5.04.01**: Create a platformer with manual gravity and bounce

This gives context before asking them to choose (G5.12).

#### M3: Joints Introduction Timing

**Current**: All joints introduced in G8
**Issue**: Fixed joints (T17.G8.02) are relatively simple and could be useful earlier
**Benefit**: Compound objects, multi-part characters helpful for G7 projects

**Recommendation**: Consider moving fixed joints to G7, leave revolute/prismatic in G8.

#### M4: Sensor Bodies Underutilized

**T17.G5.06.02** introduces sensors but no follow-up practice
**Missing**: Skills for:
- Building trigger zones (checkpoint, level boundaries)
- Collectible detection without physics collision
- Proximity detection for AI

**Recommendation**: Add sensor practice skill in G6:
- **T17.G6.04.04**: Build trigger zones with sensor bodies

### LOW PRIORITY ISSUES

#### L1: Terminology Consistency

- Some skills say "physics body", others say "physics object"
- Some say "collision groups", others "collision filtering"

**Recommendation**: Standardize on "physics body" and "collision groups" throughout.

#### L2: Debug Mode Inconsistency

- Some skills mention `debug [Yes]` parameter, others don't
- Inconsistent emphasis on using debug overlays for learning

**Recommendation**: Add note to early skills (G5.06) about always using debug mode initially.

#### L3: Missing Real-World Connection in Early Skills

- K-G4 skills are abstract (picture matching, predicting)
- Could benefit from real-world references ("like a ball bouncing")

**Recommendation**: Enhance descriptions with relatable examples.

---

## Part 4: Specific Recommendations

### Immediate Fixes

1. **Split T17.G5.06.01** into 3 skills:
   - T17.G5.06.01: Choose Box vs Circle collision shapes
   - T17.G5.06.01.01: Use Capsule shapes for elongated objects
   - T17.G5.06.01.02: Use Convex Hull for sprite-fitted collision (advanced)

2. **Split T17.G6.04.02** into 2 skills:
   - T17.G6.04.02: Enable ground detection for jump control
   - T17.G6.04.02.01: Use ground slope reporter for inclined surfaces

3. **Reorganize T17.G6.05** collision groups:
   - T17.G6.05: Set up static collision groups for filtering
   - T17.G6.05.01: Dynamically modify collision groups at runtime
   - T17.G6.05.02: Use dominance groups for one-way pushing (MOVED FROM G6.05.01)

4. **Extract CCD from optimization**:
   - T17.G8.04.01: Enable CCD for fast-moving objects → MOVE to G7 as T17.G7.01.02
   - Rename current T17.G8.04.01 to T17.G8.04.02 or merge into parent

5. **Add motor control skill**:
   - **NEW T17.G8.02.01.01**: Control revolute joint motors with speed and damping

6. **Add sensor practice**:
   - **NEW T17.G6.04.04**: Build trigger zones and collectibles with sensor bodies

### New Skills to Fill Gaps

#### Grade 5 Additions
- **T17.G5.03.01**: Build a top-down vehicle with manual friction control
- **T17.G5.04.01**: Create a simple platformer using manual gravity

#### Grade 6 Additions
- **T17.G6.04.04**: Build trigger zones and collectibles with sensor bodies
- **T17.G6.07.02**: Configure world borders for wrap-around or open-edge levels

#### Grade 7 Additions
- **T17.G7.01.02**: Enable CCD for fast projectiles (MOVED from G8.04.01)
- **T17.G7.05.02**: Use velocity reporters for UI speedometers and HUDs

#### Grade 8 Additions
- **T17.G8.02.01.01**: Control revolute joint motors with speed and damping
- **T17.G8.07**: Build a physics-based puzzle game (pulleys, seesaws, Rube Goldberg)

### Dependency Adjustments

**Reduce X-2 violations by adjusting these skills**:

1. **T17.G6.01** (Configure friction):
   - Keep dependency on T17.G5.10 (Trace simple 2D physics)
   - ADD dependency on T17.G5.09 (Configure density) for material properties context
   - REMOVE T08.G3.01, T09.G3.05 (students will have these from other topics naturally)

2. **T17.G6.02** (Control restitution):
   - Keep T17.G6.01
   - REMOVE T09.G3.05

3. **T17.G6.08** (Compare simulations):
   - Keep T17.G5.10
   - REMOVE T08.G3.01, T09.G3.05
   - These are reasonable expectations by G6 from other topics

**Reduce T17.G6.08 as bottleneck**:
- **T17.G7.01** (Launch projectile): Change deps to T17.G5.08 (Apply impulse), T17.G6.04 (Detect collisions), T09.G3.01.04 (Display variables)
- **T17.G7.02** (Combine forces): Keep current deps (appropriate)
- **T17.G7.03** (Simulate drag): Change deps to T17.G5.08.01 (Forces vs impulses), T17.G6.07 (Debug unstable)

### Sequence Improvements

**Manual Physics Arc (G5)**:
```
T17.G5.02: Track gravity with velocity variables
├─ T17.G5.03: Use horizontal speed and friction variables
│  └─ T17.G5.03.01: [NEW] Build top-down vehicle with friction
├─ T17.G5.04: Code a manual bounce with energy loss
│  └─ T17.G5.04.01: [NEW] Create platformer with manual gravity
└─ T17.G5.12: Choose manual vs engine-based physics (synthesis)
```

**Physics Engine Body Types (G5-G6)**:
```
T17.G5.06: Attach a dynamic body to a sprite
├─ T17.G5.06.A: Practice creating multiple dynamic bodies
├─ T17.G5.06.01: Choose Box vs Circle collision shapes [SPLIT FROM OLD .01]
│  ├─ T17.G5.06.01.01: Use Capsule shapes [NEW, SPLIT FROM OLD .01]
│  └─ T17.G5.06.01.02: Use Convex Hull [NEW, SPLIT FROM OLD .01]
├─ T17.G5.06.02: Create sensor bodies for trigger zones
│  └─ T17.G6.04.04: [NEW] Build trigger zones and collectibles with sensors
└─ T17.G5.06.03: Create compound shapes for complex sprites
```

**Collision Groups (G6)**:
```
T17.G6.04.03: Identify collision management needs
└─ T17.G6.05: Set up static collision groups for filtering [UPDATED]
   ├─ T17.G6.05.01: Dynamically modify collision groups [UPDATED]
   └─ T17.G6.05.02: Use dominance groups for one-way pushing [MOVED]
```

**Ground Detection (G6)**:
```
T17.G6.04: Detect collisions for scoring or triggers
└─ T17.G6.04.02: Enable ground detection for jump control [SPLIT]
   └─ T17.G6.04.02.01: [NEW] Use ground slope for inclined surfaces
```

**Joints (G8)**:
```
T17.G8.02: Implement fixed joints for connected objects
└─ T17.G8.02.01: Implement revolute joints for hinges
   ├─ T17.G8.02.01.01: [NEW] Control revolute joint motors
   └─ T17.G8.02.02: Implement prismatic joints for sliding
```

**Optimization (G8)**:
```
T17.G8.04: Optimize a physics scene for performance
├─ T17.G8.04.01: Optimize collision shapes for performance [RENAMED]
└─ T17.G8.04.02: Reduce active bodies and disable unnecessary features [NEW]

[MOVED TO G7]
T17.G7.01.02: Enable CCD for fast projectiles
```

---

## Part 5: Coverage Gaps Summary

### Blocks with NO corresponding skill:
None - all blocks are covered at least minimally.

### Blocks with INSUFFICIENT coverage:
1. **Motor control** (`set rotation axis speed ... damping factor ...`) - Mentioned but not practiced
2. **CCD** (`enable collision detection as a fast object`) - Exists but buried/late
3. **Gravity scale** (`set gravity scale`) - Exists but could be earlier
4. **World border filtering** (`set world border collision group`) - Mentioned not practiced

### Concepts needing more scaffolding:
1. **Sensor bodies** - Introduced but no practice scenarios
2. **Manual physics context** - Need real projects before comparison
3. **Collision groups** - Setup vs dynamic changes should be separate
4. **Performance optimization** - Too many strategies in one skill

---

## Part 6: Grade-Level Appropriateness Assessment

### K-G2: ✅ EXCELLENT
- All skills are picture-based or unplugged
- Clear progression from observation → matching → prediction
- No block coding required
- Appropriate vocabulary (fast/slow, direction)

### G3-G4: ✅ GOOD
- Smooth transition to block-based coding
- G3: Observation and prediction with blocks
- G4: Simple loops, speed concepts
- Builds intuition before physics engine

### G5: ⚠️ DENSE BUT MANAGEABLE
- **18 skills** is a lot for one grade
- Two parallel tracks (manual + engine) may confuse
- Recommendation: Ensure manual physics (G5.02-04) clearly marked as "preparation" and engine physics (G5.05-11) as "main sequence"

### G6: ⚠️ COMPLEXITY JUMP
- **19 skills** with heavy cross-dependencies
- Collision groups, kinematic bodies, debugging all introduced
- Recommendation: Consider if some G6 skills could move to G7 (e.g., dominance groups)

### G7: ✅ GOOD
- **17 skills** focused on application and synthesis
- Real-world modeling, data analysis, complex interactions
- Good balance of new concepts and practice

### G8: ✅ GOOD
- **5 skills** focused on advanced topics (joints, optimization, testing)
- Project-based (arcade game, regression tests)
- Appropriate capstone complexity

---

## Part 7: Proposed Skill Changes Summary

### Skills to SPLIT:
1. **T17.G5.06.01** → 3 skills (Box/Circle, Capsule, Convex Hull)
2. **T17.G6.04.02** → 2 skills (ground detection, slope reporter)
3. **T17.G6.05** → Reorganize into static setup + dynamic changes + dominance
4. **T17.G8.04** → 2-3 skills (identify bottlenecks, shape optimization, body reduction)

### Skills to ADD (12 new skills):
1. **T17.G5.03.01**: Build top-down vehicle with manual friction
2. **T17.G5.04.01**: Create platformer with manual gravity
3. **T17.G5.06.01.01**: Use Capsule shapes
4. **T17.G5.06.01.02**: Use Convex Hull
5. **T17.G6.04.02.01**: Use ground slope reporter
6. **T17.G6.04.04**: Build trigger zones with sensors
7. **T17.G6.05.01**: Dynamically modify collision groups (REORGANIZED)
8. **T17.G6.05.02**: Use dominance groups (MOVED/RENUMBERED)
9. **T17.G6.07.02**: Configure world borders for wrap-around
10. **T17.G7.01.02**: Enable CCD for fast projectiles (MOVED from G8)
11. **T17.G7.05.02**: Use velocity reporters for UI
12. **T17.G8.02.01.01**: Control revolute joint motors
13. **T17.G8.07**: Build physics-based puzzle game

### Skills to MODIFY:
1. **T17.G5.06.01**: Reduce scope to Box vs Circle only
2. **T17.G6.04.02**: Focus only on basic ground detection, remove slope
3. **T17.G6.05**: Focus on static setup, reorganize sub-skills
4. **T17.G8.04**: Focus on identifying bottlenecks
5. **T17.G8.04.01**: Renumber and focus on shape optimization

### Dependency Changes:
- **T17.G6.01, G6.02, G6.08**: Remove unnecessary cross-topic G3 dependencies
- **T17.G7.01, G7.03**: Reduce reliance on T17.G6.08 as bottleneck
- Multiple skills: Adjust to new split skill IDs

### Expected New Total: ~77-80 skills (from 65)

---

## Part 8: Implementation Priority

### Phase 1: Critical Fixes (Do First)
1. Split T17.G5.06.01 (shape selection too broad)
2. Split T17.G6.04.02 (ground detection + slope)
3. Remove X-2 violations in G6 dependencies
4. Move CCD to G7 (T17.G7.01.02)

### Phase 2: Coverage Gaps (Do Second)
1. Add manual physics practice (T17.G5.03.01, T17.G5.04.01)
2. Add sensor practice (T17.G6.04.04)
3. Add motor control (T17.G8.02.01.01)
4. Add world border filtering practice (T17.G6.07.02)

### Phase 3: Polish (Do Third)
1. Reorganize collision groups sequence
2. Split optimization skill
3. Add UI/data visualization skills
4. Add capstone puzzle game project
5. Terminology standardization pass

---

## Conclusion

T17 is a **well-structured topic** with comprehensive coverage of CreatiCode's physics capabilities. The main issues are:

1. **Density**: 65 skills is manageable but G5-G6 are very dense
2. **Complexity**: Some skills try to cover too much and need splitting
3. **Dependencies**: A few X-2 violations need fixing
4. **Gaps**: Missing practice opportunities for sensors, motors, and manual physics context

**Recommended Actions**:
- Split 4 overly complex skills
- Add 12-15 new skills for practice and coverage
- Adjust dependencies to reduce bottlenecks and X-2 violations
- Result: ~77-80 well-scoped skills with clear progression

**Overall Grade**: B+ (Good foundation, needs refinement)

---

## Appendix: Block-to-Skill Mapping

| Block | Skill(s) Covering It | Coverage Quality |
|-------|---------------------|------------------|
| `initialize 2D physics world...` | T17.G5.05 | ✅ Good |
| `behave as a [type] shape [shape]...` | T17.G5.06, T17.G5.06.01 | ⚠️ Needs split |
| `behave as... compound shape...` | T17.G5.06.03 | ✅ Good |
| `remove physics-based behavior` | T17.G5.10.01 | ✅ Good |
| `update density friction restitution` | T17.G5.09, T17.G6.01, T17.G6.02 | ✅ Good |
| `set x speed` / `set y speed` | T17.G6.02.01 | ✅ Good |
| `set speed ... in direction` | T17.G6.02.01 | ✅ Good |
| `set speed ... in moving direction` | T17.G6.02.01.01 | ✅ Good |
| `set rotation speed` | T17.G7.04.01 | ✅ Good |
| `point in direction of speed` | T17.G7.01.01 | ✅ Good |
| `add force ... in direction` | T17.G5.08.01, T17.G7.02 | ✅ Good |
| `add force ... at position` | T17.G7.02.02 | ✅ Good |
| `remove all forces` | T17.G7.02.01 | ✅ Good |
| `add torque` | T17.G7.04.01 | ✅ Good |
| `remove all torques` | T17.G7.02.01 | ✅ Good |
| `apply impulse ... in direction` | T17.G5.08 | ✅ Good |
| `apply impulse ... at position` | T17.G5.08.02 | ✅ Good |
| `apply torque impulse` | T17.G7.04.01 | ✅ Good |
| `prevent body movement...` | T17.G6.06.01 | ✅ Good |
| `prevent body rotation...` | T17.G6.06.01 | ✅ Good |
| `set damping factor...` | T17.G7.03.01 | ✅ Good |
| `broadcast ... when colliding...` | T17.G6.04 | ✅ Good |
| `broadcast ... when finish colliding...` | T17.G6.04.01 | ✅ Good |
| `add to collision group` | T17.G6.05 | ⚠️ Needs reorganization |
| `remove from collision group` | T17.G6.05 | ⚠️ Needs reorganization |
| `enable collision with group` | T17.G6.05 | ⚠️ Needs reorganization |
| `disable collision with group` | T17.G6.05 | ⚠️ Needs reorganization |
| `set dominance group` | T17.G6.05.01 | ✅ Good (but renumber to G6.05.02) |
| `enable collision detection as fast object` | T17.G8.04.01 | ⚠️ Too late, move to G7 |
| `set gravity scale` | T17.G8.05 | ⚠️ Could be earlier |
| `set physics time speed` | T17.G8.05 | ✅ Good placement |
| `fix relative position to...` | T17.G8.02 | ✅ Good |
| `remove relative position constraint` | T17.G8.02 | ✅ Good |
| `set ... as rotation axis...` | T17.G8.02.01 | ✅ Good |
| `remove rotation axis` | T17.G8.02.01 | ✅ Good |
| `set rotation axis speed damping` | T17.G8.02.01 | ⚠️ Mentioned, needs dedicated skill |
| `set world border collider...` | T17.G6.07.01 | ⚠️ Mentioned, needs practice |
| `set world border collision group...` | T17.G6.07.01 | ⚠️ Mentioned, needs practice |
| `allow ... sliding relative to...` | T17.G8.02.02 | ✅ Good |
| `turn on ground detection...` | T17.G6.04.02 | ⚠️ Needs split |
| `(x speed)` | T17.G7.05 | ✅ Good |
| `(y speed)` | T17.G7.05 | ✅ Good |
| `(angular speed)` | T17.G7.05 | ✅ Good |
| `<in collision below>` | T17.G6.04.02 | ⚠️ Needs split |
| `(ground slope)` | T17.G6.04.02 | ⚠️ Needs separate skill |
| `(mass)` | T17.G7.05 | ✅ Good |

**Coverage Summary**:
- ✅ Good coverage: 35 blocks
- ⚠️ Needs improvement: 11 blocks
- ❌ Not covered: 0 blocks

---

**End of Report**
