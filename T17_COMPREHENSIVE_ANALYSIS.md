# Topic T17 (2D Motion & Physics) - Comprehensive Analysis Report

**Analysis Date:** 2025-11-22
**Analyst:** Claude Code Agent
**Project:** CreatiCode Skill Map Optimization - Phase 2

---

## EXECUTIVE SUMMARY

Topic T17 (2D Motion & Physics) contains **60 skills** spanning grades G3-G8, covering both manual velocity-based physics and CreatiCode's Rapier-based 2D physics engine. The topic is **well-structured overall** with a thoughtful pedagogical progression from observational skills through manual implementation to engine-based physics. However, analysis reveals **8 HIGH priority issues**, **12 MEDIUM priority issues**, and **7 LOW priority issues** that should be addressed.

### Key Findings:
- ✅ **Strong pedagogical design**: Dual-track approach (manual G5.02-G5.04 + engine G5.05-G5.11) builds deep understanding
- ✅ **Comprehensive coverage**: 46 physics blocks → 60 skills (good coverage ratio)
- ❌ **Missing K-2 grades**: No foundational motion concepts for early learners
- ❌ **Terminology inconsistency**: Skill T17.G5.06.01 references shapes that don't exist in blockdes8
- ❌ **Coverage gaps**: Missing blocks for `set speed in moving direction`, `remove from collision group`, `enable collision with group`
- ⚠️ **Dependency issues**: T17.G5.06.02 has circular dependency (requires G6.04 while in G5)

---

## 1. CURRENT T17 STRUCTURE

### 1.1 Grade Distribution

| Grade | Skill Count | Percentage | Focus Area |
|-------|-------------|------------|------------|
| G3 | 2 | 3.3% | Basic motion observation (no physics engine) |
| G4 | 2 | 3.3% | Conceptual understanding of speed/falling |
| G5 | 18 | 30.0% | Manual physics + Engine basics + Body setup |
| G6 | 16 | 26.7% | Collision detection, friction, restitution, filtering |
| G7 | 13 | 21.7% | Forces, projectiles, drag, torque, reporters |
| G8 | 9 | 15.0% | Joints, optimization, regression testing |
| **TOTAL** | **60** | **100%** | |

### 1.2 Missing Grades
- **K-2**: NO SKILLS - Major gap for picture-based learning
  - K-2 students should have skills like:
    - "Observe how sprites move when motion blocks run" (picture-based)
    - "Match sprite positions to motion block sequences" (picture-based)
    - "Identify fast vs slow motion" (visual comparison)

### 1.3 Topic Progression Architecture

```
T17 Structure (Well-designed dual track):

G3-G4: Conceptual Foundation
├─ G3.01: Observe position changes
├─ G3.02: Predict direction/distance
├─ G4.01: Simulate falling (loop-based)
└─ G4.02: Explain speed as position change

G5: DUAL TRACK (Manual + Engine)
├─ Manual Track (G5.02-G5.04):
│  ├─ G5.02: Track gravity with velocity variables
│  ├─ G5.03: Use horizontal speed and friction variables
│  └─ G5.04: Code manual bounce with energy loss
│
├─ Engine Track (G5.05-G5.11):
│  ├─ G5.05: Initialize physics world
│  ├─ G5.06+: Attach bodies, shapes, sensors, compound shapes
│  ├─ G5.07: Fixed boundaries
│  ├─ G5.08+: Impulses (center + off-center)
│  ├─ G5.09: Configure density
│  └─ G5.10-G5.12: Tracing, debugging, choosing approach
│
└─ Integration:
   └─ G5.12: Choose manual vs engine-based physics (synthesis skill)

G6: Physics Properties & Collisions
├─ Material properties (friction, restitution)
├─ Velocity control & body types (dynamic/movable)
├─ Collision detection & filtering
└─ Debugging & blending

G7: Advanced Forces & Data
├─ Projectiles, combined forces
├─ Drag simulation & damping
├─ Torque & rotation
└─ Velocity/mass reporters & graphing

G8: Integration & Optimization
├─ Joints (fixed, revolute, prismatic)
├─ Performance optimization
├─ Regression testing
└─ Game design & tuning
```

---

## 2. CREATICODE 2D PHYSICS BLOCKS INVENTORY

### 2.1 Complete Block List (46 blocks)

**World Setup (2 blocks):**
1. `physics_enablephysics` → `initialize 2D physics world with gravity x [X] y [Y]`
2. `physics_settimespeed` → `set physics time speed (SPEED) %`

**Body Creation & Management (4 blocks):**
3. `physics_setphysicsbody` → `behave as a [TYPE] [SENSORTYPE] shape [SHAPETYPE] debug [DODEBUG]`
   - TYPE: fixed, dynamic, movable
   - SENSORTYPE: object, sensor
   - **SHAPETYPE: Circle, Box, Capsule, Convex Hull** ⚠️ NOTE: No "ConvexHull" (it's "Convex Hull" with space)
4. `physics_setphysicsbody2` → `behave as a [TYPE] [SENSORTYPE] in compound shape with curve tolerance [TOLERANCE] point distance [DISTANCE] debug [DODEBUG]`
5. `physics_removecollider` → `remove physics-based behavior`
6. `physics_updatephysicsbody` → `update density (DENSITY) friction (FRICTION)% restitution (RESTITUTION)%`

**Velocity Control (5 blocks):**
7. `physics_setvelocityx` → `set x speed (SPEED)`
8. `physics_setvelocityy` → `set y speed (SPEED)`
9. `physics_setvelocitydir` → `set speed (SPEED) in direction (DIR)`
10. `physics_setvelocitymovingdir` → `set speed (SPEED) in moving direction` ⚠️ MISSING SKILL
11. `physics_setrotationspeed` → `set rotation speed (SPEED)`

**Direction Control (1 block):**
12. `physics_setdirbyvelocity` → `point in direction of speed`

**Forces (4 blocks):**
13. `physics_addforce` → `add force (FORCE) in direction (DIR)`
14. `physics_addforce2` → `add force (FORCE) in direction (DIR) at position x (XPOS) y (YPOS)`
15. `physics_clearforce` → `remove all forces`
16. `physics_addtorque` → `add torque (TORQUE)`
17. `physics_cleartorque` → `remove all torques`

**Impulses (3 blocks):**
18. `physics_applyimpulse` → `apply impulse (FORCE) in direction (DIR)`
19. `physics_applyimpulse2` → `apply impulse (FORCE) in direction (DIR) at position x (POSX) y (POSY)`
20. `physics_applytorqueimpulse` → `apply torque impulse (TORQUE)`

**Constraints (2 blocks):**
21. `physics_lockmovement` → `prevent body movement from forces [DOPREVENT]`
22. `physics_lockrotation` → `prevent body rotation from forces [DOPREVENT]`

**Damping (1 block):**
23. `physics_setdampingfactor` → `set damping factor for movement (MOVEMENTDAMPING) % rotation (ROTATIONDAMPING) %`

**Collision Events (2 blocks):**
24. `physics_broadcastcollisioneventmessage` → `broadcast [MESSAGE] when colliding with [SPRITENAME v]`
25. `physics_broadcastcollisioneventmessage2` → `broadcast [MESSAGE] when finish colliding with [SPRITENAME v]`

**Collision Groups (4 blocks):**
26. `physics_addtocollisiongroup` → `add to collision group [G]`
27. `physics_removefromcollisiongroup` → `remove from collision group [G]` ⚠️ MISSING SKILL
28. `physics_addcollisionfilter` → `enable collision with group [G]` ⚠️ MISSING SKILL
29. `physics_removecollisionfilter` → `disable collision with group [G]`

**Advanced Physics (4 blocks):**
30. `physics_setdominancegroup` → `set dominance group to (G)`
31. `physics_setccd` → `enable collision detection as a fast object [ISFAST]`
32. `physics_setgravityscale` → `set gravity scale (SCALE) %`
33. `physics_turnoncollisiondetection` → `turn on ground detection within distance (DISTANCE) debug [DODEBUG]`

**Joints (6 blocks):**
34. `physics_addfixedjoint` → `fix relative position to [SPRITENAME v]`
35. `physics_removefixedjoint` → `remove relative position constraint`
36. `physics_addrevoltejoint` → `set [SPRITENAME v] as rotation axis with offset x (OFFSETX) y (OFFSETY)`
37. `physics_removerevoltejoint` → `remove rotation axis`
38. `physics_setrotationaxisspeed` → `set rotation axis speed (SPEED) damping factor (DAMPINGFACTOR) %`
39. `physics_addprismaticjoint` → `allow [DIRECTION] sliding relative to [SPRITENAME v] range from (MINDISTANCE) and (MAXDISTANCE)`

**World Border (2 blocks):**
40. `physics_setedgecollider` → `set world border collider friction (FRICTION)% restitution (RESTITUTION)%`
41. `physics_setedgecollisiongroup` → `set world border collision group [COLLISIONGROUP] colliding with group [TARGETGROUP]`

**Reporters (6 blocks):**
42. `physics_getvelocityx` → `(x speed)`
43. `physics_getvelocityy` → `(y speed)`
44. `physics_getMass` → `(mass)`
45. `physics_getangularvelocity` → `(angular speed)`
46. `physics_getcollidingbottom` → `<in collision below>`
47. `physics_getgroundslope` → `(ground slope)`

### 2.2 Block-to-Skill Coverage Analysis

| Block Category | Blocks | Skills Covering | Coverage Status |
|----------------|--------|-----------------|-----------------|
| World Setup | 2 | 2 (G5.05, G8.05) | ✅ Complete |
| Body Creation | 4 | 6 (G5.06, G5.06.01-03, G5.10.01) | ✅ Complete |
| Velocity Control | 5 | 3 (G6.02.01 covers 3 blocks) | ⚠️ Missing `set speed in moving direction` |
| Direction | 1 | 1 (G7.01.01) | ✅ Complete |
| Forces | 5 | 4 (G5.08.01, G7.02, G7.02.01-02) | ✅ Complete |
| Impulses | 3 | 3 (G5.08, G5.08.01-02) | ✅ Complete |
| Constraints | 2 | 1 (G6.06.01) | ✅ Complete |
| Damping | 1 | 1 (G7.03.01) | ✅ Complete |
| Collision Events | 2 | 2 (G6.04, G6.04.01) | ✅ Complete |
| Collision Groups | 4 | 2 (G6.05, G6.05.01) | ❌ Missing 2 skills |
| Advanced Physics | 4 | 4 (G6.04.02, G8.04.01, G8.05) | ✅ Complete |
| Joints | 6 | 3 (G8.02, G8.02.01-02) | ✅ Complete (all covered) |
| World Border | 2 | 1 (G6.07.01) | ⚠️ Partial (collision group setting missing) |
| Reporters | 6 | 2 (G7.05, G7.05.01) | ✅ Complete |

**Coverage Rate: 42/46 blocks directly taught = 91.3%**

---

## 3. ISSUES IDENTIFIED

### 3.1 HIGH PRIORITY ISSUES (8)

#### H1. Missing K-2 Grades (Critical Gap)
**Issue:** T17 has NO skills for K-2 students
**Impact:** Early learners cannot engage with motion concepts
**Expected Skills:**
- K.01: Observe sprite position changes when motion blocks run (picture-based)
- K.02: Match sprite to position after motion sequence (picture-based)
- G1.01: Identify fast vs slow motion from animations
- G2.01: Predict sprite direction from motion blocks (picture choices)

**Priority:** HIGH
**Recommendation:** Add 4-6 K-2 skills focused on visual/picture-based motion observation

---

#### H2. Incorrect Shape Type Names (T17.G5.06.01)
**Issue:** Dependency text says "Select appropriate body shapes (Box, Circle, ConvexHull, Capsule)" but blockdes8 shows the shape is "Convex Hull" (with space), not "ConvexHull"
**Location:** Line 8771 of allskills.md
**Actual Block Parameter:** `SHAPETYPE: Circle, Box, Capsule, Convex Hull`
**Impact:** Terminology mismatch could confuse curriculum developers

**Priority:** HIGH
**Recommendation:** Update dependency to: "Select appropriate body shapes (Box, Circle, Capsule, Convex Hull)"

---

#### H3. Missing Skill: Set Speed in Moving Direction
**Issue:** Block `physics_setvelocitymovingdir` → `set speed (SPEED) in moving direction` has no dedicated skill
**Current Coverage:** Skill G6.02.01 covers three blocks (`set x speed`, `set y speed`, `set speed in direction`) but NOT this one
**Use Case:** Maintaining constant speed while preserving direction (e.g., platformer character speed regulation)

**Priority:** HIGH
**Recommendation:** Add new skill:
```
ID: T17.G6.02.01.01
Skill: Maintain constant speed in current direction
Description: Students use `set speed [value] in moving direction` to regulate an object's speed without changing its trajectory. This is useful for maintaining constant character movement speed or limiting maximum velocity while preserving physics-driven direction changes.
Dependencies: T17.G6.02.01
```

---

#### H4. Missing Skill: Remove from Collision Group
**Issue:** Block `physics_removefromcollisiongroup` → `remove from collision group [G]` has no skill
**Current Coverage:** G6.05 teaches adding to collision groups and disabling collisions, but not removal
**Use Case:** Dynamic collision group management (e.g., player becomes invincible temporarily)

**Priority:** HIGH
**Recommendation:** Expand T17.G6.05 description to include removal, OR add sub-skill:
```
ID: T17.G6.05.02
Skill: Dynamically modify collision group membership
Description: Students use `add to collision group [G]` and `remove from collision group [G]` to change which groups an object belongs to during gameplay. Use cases: temporary invincibility, phasing through walls, dynamic object state changes.
Dependencies: T17.G6.05
```

---

#### H5. Missing Skill: Enable Collision with Group
**Issue:** Block `physics_addcollisionfilter` → `enable collision with group [G]` has no skill
**Current Coverage:** G6.05 teaches `disable collision with group [G]` but not the opposite
**Impact:** Incomplete understanding of collision filtering (only teaches disabling, not re-enabling)

**Priority:** HIGH
**Recommendation:** Update T17.G6.05 description to explicitly mention BOTH enabling and disabling:
```
Updated Description for T17.G6.05:
Students use `add to collision group [0-15]`, `disable collision with group [G]`, and `enable collision with group [G]` to control selective collisions. They configure which groups each object collides with, allowing players to pass through collectibles while still hitting hazards.
```

---

#### H6. Circular Dependency: T17.G5.06.02 → T17.G6.04
**Issue:** Skill T17.G5.06.02 (G5, "Create sensor bodies") depends on T17.G6.04 (G6, "Detect collisions")
**Location:** Line 8762 of allskills.md
**Problem:** Forward dependency within same topic violates scaffolding
**Impact:** Students must jump ahead one grade to learn collision detection before learning sensors

**Priority:** HIGH
**Recommendation:** REMOVE the T17.G6.04 dependency from T17.G5.06.02. Sensors can be taught as "bodies that don't collide physically" without needing collision event detection. The collision detection skill can use sensors as an application later.

**Revised Dependency for T17.G5.06.02:**
```
Dependencies:
* T17.G5.06.01: Select Box and Circle body shapes
(REMOVE: T17.G6.04)
```

---

#### H7. Missing World Border Collision Group Skill
**Issue:** Block `physics_setedgecollisiongroup` is only partially covered in T17.G6.07.01
**Current:** G6.07.01 teaches friction/restitution but description doesn't mention `set world border collision group`
**Impact:** Students don't learn how to make borders selectively collide with certain groups

**Priority:** HIGH
**Recommendation:** Update T17.G6.07.01 description:
```
Updated Description for T17.G6.07.01:
Students use `set world border collider friction [value]% restitution [value]%` and `set world border collision group [COLLISIONGROUP] colliding with group [TARGETGROUP]` to customize how objects interact with the automatic stage boundaries. They create bouncy walls, configure selective border collisions for different object types, or remove border collisions for objects that should wrap around.
```

---

#### H8. Skill T17.G5.06.01 Title vs Description Mismatch
**Issue:** Skill title is "Select Box and Circle body shapes" but description says "Box works well for rectangular objects and Circle for round objects"
**Problem:** Title mentions only 2 shapes, but the actual block supports 4: Box, Circle, Capsule, Convex Hull
**Location:** Lines 8746-8752 of allskills.md

**Priority:** HIGH
**Recommendation:** Update skill title and description:
```
Updated Skill T17.G5.06.01:
Skill: Select basic body shapes (Box, Circle, Capsule)
Description: Students practice choosing between Box, Circle, and Capsule collision shapes for different sprites. They understand that Box works well for rectangular objects, Circle for round objects, and Capsule for elongated objects. They observe how shape choice affects collision behavior and learn to select the simplest shape that matches their sprite.
```

---

### 3.2 MEDIUM PRIORITY ISSUES (12)

#### M1. Terminology: "Movable" vs "Kinematic"
**Issue:** Skill T17.G6.02.02 uses "movable (kinematic)" and T17.G6.03 uses "movable" in title
**blockdes8 terminology:** `TYPE can be 'fixed', 'dynamic' or 'movable'`
**Industry terminology:** Typically called "kinematic" bodies in physics engines
**Current approach:** Skills correctly use CreatiCode terminology "movable" with "(kinematic)" parenthetical

**Priority:** MEDIUM
**Recommendation:** Keep current approach (using CreatiCode's "movable" term with industry term in parentheses for clarity)

---

#### M2. G5 Overload (18 skills)
**Issue:** Grade 5 contains 30% of all T17 skills (18/60)
**Reason:** Dual-track design (manual + engine) both start in G5
**Impact:** May be overwhelming for 5th graders

**Priority:** MEDIUM
**Recommendation:** Consider this acceptable given that:
1. Manual track (G5.02-G5.04) is only 3 skills
2. Engine track is well-scaffolded with progressive sub-skills
3. The dual-track approach is pedagogically sound
4. Alternative would be to move manual track to G4, but G4 students may not be ready for variables

**Suggested Action:** Keep as-is but monitor in pilot testing

---

#### M3. Missing "Convex Hull" Shape Introduction
**Issue:** Skill T17.G5.06.01 teaches Box, Circle, and should teach Capsule, but "Convex Hull" shape is never explicitly introduced
**Current Coverage:** Mentioned in passing in G5.06.03 (compound shapes) dependency text, but students never practice choosing it

**Priority:** MEDIUM
**Recommendation:** Update T17.G5.06.01 to include all 4 simple shapes:
```
Updated Description:
Students practice choosing between Box, Circle, Capsule, and Convex Hull collision shapes for different sprites. They understand that Box works for rectangular objects, Circle for round objects, Capsule for elongated objects, and Convex Hull for automatic shape-fitting. They observe how shape choice affects collision accuracy and performance.
```

---

#### M4. Rotation Axis Speed Block Placement
**Issue:** Block `physics_setrotationaxisspeed` is introduced in G8.02.01 (revolute joints) but it's a configuration detail
**Current Approach:** Correctly bundled with revolute joint skill since it's only meaningful after creating rotation axis

**Priority:** MEDIUM
**Recommendation:** Keep as-is (correct placement)

---

#### M5. Missing Joint Removal Skills
**Issue:** Blocks `physics_removefixedjoint` and `physics_removerevoltejoint` are not explicitly taught
**Current Coverage:** Implicit in joint creation skills (G8.02, G8.02.01)

**Priority:** MEDIUM
**Recommendation:** Update descriptions of G8.02 and G8.02.01 to explicitly mention removal:
```
Updated T17.G8.02:
Students use `fix relative position to [sprite]` to weld sprites together and `remove relative position constraint` to break the connection. Examples: compound objects, multi-part characters, towed vehicles that can be detached.

Updated T17.G8.02.01:
Students use `set [sprite] as rotation axis with offset x [X] y [Y]` to create hinged objects like doors, seesaws, and pendulums, configure rotation with `set rotation axis speed [S] damping factor [D]%`, and use `remove rotation axis` to disconnect. Examples: breakable hinges, detachable rotating parts.
```

---

#### M6. No Prismatic Joint Removal Skill
**Issue:** No removal block exists for prismatic joints in blockdes8 (only creation block)
**Implication:** Prismatic joints are permanent (cannot be dynamically removed)

**Priority:** MEDIUM
**Recommendation:** Document this limitation in T17.G8.02.02 description:
```
Updated Description:
Students use `allow [Horizontal/Vertical] sliding relative to [sprite] range from [min] to [max]` to create pistons, sliding doors, and spring-loaded platforms with configurable movement limits. Note: Prismatic joints are permanent once created; plan constraint usage during design phase.
```

---

#### M7. Ground Slope Reporter Not Explicitly Taught
**Issue:** Block `physics_getgroundslope` → `(ground slope)` mentioned in ground detection block description but never gets dedicated skill attention
**Current Coverage:** T17.G6.04.02 teaches ground detection but doesn't emphasize slope reporter

**Priority:** MEDIUM
**Recommendation:** Update T17.G6.04.02 description:
```
Updated Description:
Students enable `turn on ground detection within distance [value] debug [Yes]` and use the `<in collision below>` boolean reporter to allow jumping only when grounded. They also use the `(ground slope)` reporter to detect inclined surfaces. They configure detection distance and debug detection issues.
```

---

#### M8. Dependency Gap: T17.G6.05 Depends on T08.G4.01
**Issue:** Skill T17.G6.05 (G6) depends on T08.G4.01 (G4: "Write a condition that uses and/or")
**Problem:** 2-grade gap, but it's cross-topic
**Note:** Comment on line 8860 acknowledges X-2 violations are acceptable for cross-topic dependencies

**Priority:** MEDIUM
**Recommendation:** Keep as-is (cross-topic dependencies are Phase 2 concern, acknowledged in comment)

---

#### M9. Missing CCD Explanation Context
**Issue:** Skill T17.G8.04.01 introduces CCD but term "tunneling" may be unfamiliar
**Current Description:** "fast-moving objects that might tunnel through thin walls at normal update rates"

**Priority:** MEDIUM
**Recommendation:** Expand description slightly:
```
Updated Description:
Students use `enable collision detection as a fast object [Yes]` (Continuous Collision Detection / CCD) for bullets, fast balls, or other high-speed objects. CCD prevents "tunneling" - when objects move so fast they skip past thin walls between physics updates, passing through without colliding.
```

---

#### M10. Reporter Skills Could Be More Granular
**Issue:** Skill T17.G7.05 teaches ALL reporter blocks at once (x speed, y speed, mass, angular speed, ground slope)
**Current Approach:** Single skill covers all 6 reporters
**Alternative:** Could split into velocity reporters vs mass vs ground detection

**Priority:** MEDIUM
**Recommendation:** Keep current approach (all reporters have similar usage pattern: "read and display data"). The follow-up skill G7.05.01 (graphing) provides practice opportunity.

---

#### M11. Physics World Not Required for G3-G4 Skills
**Issue:** Skills T17.G3.01, G3.02, G4.01, G4.02 teach motion concepts but don't use physics engine
**These use:** Basic Scratch motion blocks (move, glide) and loops
**Clarification needed:** Do these belong in T17 (physics topic) or should they be in a "Motion" topic?

**Priority:** MEDIUM
**Recommendation:** Keep in T17 as designed. These skills provide conceptual foundation for physics understanding. The progression from "observe motion" → "explain speed" → "manual implementation" → "engine-based" is pedagogically sound.

---

#### M12. Skill T17.G5.12 Uniqueness
**Issue:** Skill T17.G5.12 "Choose manual vs engine-based physics" is a meta-cognitive decision-making skill
**Type:** Synthesis/analysis skill rather than implementation skill
**Dependencies:** Requires experience with BOTH manual (G5.02-G5.04) AND engine (G5.05-G5.11) approaches

**Priority:** MEDIUM
**Recommendation:** This is actually a STRENGTH. Keep as-is. This synthesis skill is excellent pedagogy - students compare approaches and make informed tool choices. Consider adding similar meta-cognitive skills to other topics.

---

### 3.3 LOW PRIORITY ISSUES (7)

#### L1. No Explicit "Getting Started" Skill for G3
**Issue:** T17.G3.01 jumps into "observe position changes" without an intro skill
**Comparison:** Some topics have explicit "intro to category" skills

**Priority:** LOW
**Recommendation:** Optional - could add T17.G3.00 "Recognize that sprites can move on the stage" but current G3.01 is sufficient

---

#### L2. Damping Factor Terminology
**Issue:** Term "damping factor" in `set damping factor for movement (M)% rotation (R)%` may be unfamiliar
**Current Coverage:** Skill T17.G7.03.01 introduces it as "alternative to manual drag"
**Pedagogical Note:** Skill T17.G7.03 teaches manual drag first, then G7.03.01 introduces damping as easier alternative (good scaffolding)

**Priority:** LOW
**Recommendation:** Keep current approach (manual first, then built-in)

---

#### L3. No "Reset Physics World" Skill
**Issue:** No skill teaches how to completely reset/reinitialize physics world mid-game
**Workaround:** Students can call `initialize 2D physics world` again

**Priority:** LOW
**Recommendation:** Add note to T17.G5.05 description that re-running initialization resets the world

---

#### L4. Collision Group Numbers (0-15) Not Explained
**Issue:** Skills mention collision groups 0-15 but don't explain why 16 groups or how to organize them
**Current Coverage:** G6.04.03 "Identify collision management needs" plans strategy, G6.05 implements

**Priority:** LOW
**Recommendation:** Acceptable as-is. 16 groups is an implementation detail. Students learn through practice.

---

#### L5. No Performance Profiling Skill
**Issue:** Skill T17.G8.04 "Optimize a physics scene for performance" mentions profiling but doesn't teach HOW to measure performance
**Platform Limitation:** CreatiCode may not have built-in profiling tools

**Priority:** LOW
**Recommendation:** Update description to clarify measurement approach:
```
Updated Description:
Students identify performance bottlenecks in a busy physics scene by observing frame rate and lag. They implement optimizations: using simpler collision shapes (Box instead of Convex Hull), reducing active object count, using compound shapes sparingly, disabling unnecessary collision groups, and hiding debug overlays. They verify improvements through playtesting.
```

---

#### L6. Dominance Group Range Not Justified
**Issue:** Skill T17.G6.05.01 mentions dominance group range (-127 to 127) but doesn't explain why this range
**Technical Detail:** Likely signed byte integer (-128 to 127, or -127 to 127 avoiding -128 edge case)

**Priority:** LOW
**Recommendation:** Keep as-is. Range is a technical detail. Students just need to know "higher number = more dominant"

---

#### L7. No Explicit "Remove All Physics Bodies" Skill
**Issue:** No skill teaches mass cleanup of physics bodies (e.g., level transition)
**Workaround:** Students can use `remove physics-based behavior` on each sprite or reinitialize world

**Priority:** LOW
**Recommendation:** Optional - could add to T17.G5.10.01 or create new cleanup skill, but current coverage is adequate

---

## 4. GRADE APPROPRIATENESS ANALYSIS

### 4.1 K-2 Assessment: FAIL ❌
**Issue:** NO K-2 skills exist
**Expected:** Picture-based motion observation and prediction
**Impact:** Early learners excluded from motion concepts

### 4.2 G3-G4 Assessment: GOOD ✅
**Skills:** Observational and conceptual (no coding complexity)
**Appropriate for grade level:** Yes
- G3: Observe and predict (concrete operations)
- G4: Explain speed concept (developing abstract thinking)

### 4.3 G5 Assessment: ACCEPTABLE ⚠️
**Skills:** Mix of manual implementation and engine usage
**Concern:** 18 skills (30% of topic)
**Mitigation:** Well-scaffolded progression, optional paths (manual vs engine)
**Recommendation:** Monitor in pilot testing

### 4.4 G6-G8 Assessment: EXCELLENT ✅
**Progression:** Material properties → Forces → Joints → Optimization
**Cognitive level:** Appropriate advancement through grades
**Real-world connection:** Strong (G7.06 models real phenomena, G8.06 uses analytics)

---

## 5. DEPENDENCY ANALYSIS (WITHIN T17 ONLY)

### 5.1 Dependency Validation Rules
1. ✅ Skills can depend on earlier grades (backward dependencies OK)
2. ❌ Skills CANNOT depend on later grades within same topic (forward dependencies forbidden)
3. ⚠️ Skills CAN depend on later grades in OTHER topics (cross-topic gaps addressed in Phase 2)
4. ✅ X-2 rule: Within-topic dependencies should not skip more than 2 grades

### 5.2 Within-Topic Forward Dependencies: 1 VIOLATION

| Skill | Grade | Depends On | Violation Type |
|-------|-------|------------|----------------|
| T17.G5.06.02 | G5 | T17.G6.04 (G6) | ❌ FORWARD (1 grade ahead) |

**Action Required:** Remove T17.G6.04 dependency from T17.G5.06.02

### 5.3 Within-Topic X-2 Violations: NONE ✅
All within-topic dependencies respect the X-2 rule (no skill depends on a within-topic skill more than 2 grades earlier).

### 5.4 Cross-Topic Dependency Gaps (Acknowledged)
**Note:** Comment on line 8860 acknowledges several G6-G7 skills depend on T07/T08/T09.G3 skills (3-4 grade gaps). These are cross-topic dependencies and will be addressed in Phase 2.

Examples:
- T17.G6.01 (G6) depends on T08.G3.01 (G3) - 3 grade gap ✅ (cross-topic, acceptable per comment)
- T17.G6.05 (G6) depends on T08.G4.01 (G4) - 2 grade gap ✅ (cross-topic, acceptable)

---

## 6. DUPLICATE & OVERLAP ANALYSIS

### 6.1 Duplicate Skills: NONE ✅
No duplicate skills found. Each skill teaches a distinct concept or block.

### 6.2 Overlapping Skills: MINIMAL ✅

**Acceptable Overlaps (Progressive Refinement):**
1. **T17.G5.06 → G5.06.A → G5.06.01**
   - G5.06: Attach ONE dynamic body
   - G5.06.A: Practice with MULTIPLE bodies
   - G5.06.01: Practice SHAPE SELECTION
   - **Status:** ✅ Good scaffolding (progressive refinement)

2. **T17.G5.08 → G5.08.01 → G5.08.02**
   - G5.08: Apply impulse at center
   - G5.08.01: Distinguish forces vs impulses
   - G5.08.02: Apply impulse at position (creates rotation)
   - **Status:** ✅ Good scaffolding (concept then variation)

3. **T17.G6.02.01 vs G6.02.02**
   - G6.02.01: Set velocity directly (3 blocks)
   - G6.02.02: Compare body types (dynamic vs movable)
   - **Status:** ✅ Related but distinct (implementation vs conceptual comparison)

### 6.3 Potential Merge Candidates: NONE
No skills should be merged. Granularity is appropriate.

---

## 7. SKILLS TOO BROAD / TOO NARROW

### 7.1 Skills That Are Too Broad: 1

**T17.G6.02.01: Set velocity directly for physics bodies**
- **Issue:** Teaches THREE different blocks in one skill:
  1. `set x speed [value]`
  2. `set y speed [value]`
  3. `set speed [value] in direction [angle]`
- **Why it's a problem:** Each block has distinct use cases
- **Recommendation:** Consider splitting:
  ```
  T17.G6.02.01: Set velocity by component (x/y speeds)
  Description: Students use `set x speed [value]` and `set y speed [value]` to control physics body velocity separately in each axis. Use for independent horizontal/vertical control like platformer jumping.

  T17.G6.02.01.01: Set velocity by direction and magnitude
  Description: Students use `set speed [value] in direction [angle]` to control velocity using polar coordinates. Use for projectiles, steering, or any motion with a clear direction.
  ```

**Priority:** MEDIUM (current approach is acceptable but could be improved)

### 7.2 Skills That Are Too Narrow: NONE ✅
No skills are overly granular. The topic has good balance between atomic skills and synthesis skills.

---

## 8. MISSING SKILLS (COMPREHENSIVE)

### 8.1 Missing K-2 Foundation Skills (4-6 skills needed)
Already covered in section 3.1 (H1)

### 8.2 Missing Block Coverage (3 skills)
1. **`set speed in moving direction`** - Covered in H3
2. **`remove from collision group [G]`** - Covered in H4
3. **`enable collision with group [G]`** - Covered in H5

### 8.3 Missing Conceptual Skills (Optional)

**Optional Additions:**
1. **"Understanding Body Types" (could go in G5)**
   - Concept: fixed vs dynamic vs movable (currently scattered across skills)
   - **Recommendation:** LOW PRIORITY - Current scattered approach works

2. **"Physics Coordinate System" (could go in G3)**
   - Concept: Y-axis points up (not down like in Scratch 2D)
   - **Recommendation:** MEDIUM PRIORITY - Could add to G3.01 description

3. **"Collision vs Sensor Bodies" (could go in G5)**
   - Concept: object vs sensor behavior
   - **Current Coverage:** G5.06.02 teaches sensors
   - **Recommendation:** Keep as-is

---

## 9. RECOMMENDATIONS SUMMARY

### 9.1 MUST FIX (High Priority - 8 issues)

1. **Add K-2 skills** (4-6 picture-based motion skills)
2. **Fix shape terminology** in T17.G5.06.01 dependency ("Convex Hull" not "ConvexHull")
3. **Add skill for `set speed in moving direction`** (new T17.G6.02.01.01)
4. **Add skill for collision group removal** (expand G6.05 or add G6.05.02)
5. **Add skill for enable collision filter** (update G6.05 description)
6. **Remove circular dependency** in T17.G5.06.02 (remove G6.04 dependency)
7. **Update T17.G6.07.01** to cover world border collision groups
8. **Fix T17.G5.06.01 title and description** to include all basic shapes

### 9.2 SHOULD FIX (Medium Priority - 12 issues)

1. Consider G5 skill count (18 skills) - monitor in pilot testing
2. Update T17.G5.06.01 to include Convex Hull shape
3. Update joint skills (G8.02, G8.02.01) to mention removal blocks
4. Document prismatic joint limitation in G8.02.02
5. Update G6.04.02 to emphasize ground slope reporter
6. Expand CCD description in G8.04.01 to explain tunneling
7. Add note to G5.05 that re-initialization resets world
8. Update G8.04 to clarify performance measurement approach
9. Keep current terminology ("movable" with kinematic note)
10. Keep reporter consolidation in G7.05 (don't split)
11. Keep G3-G4 non-engine motion skills in T17
12. Keep G5.12 meta-cognitive synthesis skill (it's a strength)

### 9.3 OPTIONAL IMPROVEMENTS (Low Priority - 7 issues)

1. Consider T17.G3.00 intro skill (low value)
2. Keep damping factor approach (manual then built-in)
3. Explain collision group organization (16 groups)
4. Justify dominance group range (technical detail)
5. Consider mass cleanup skill (low value)
6. Consider splitting G6.02.01 into two skills (moderate value)
7. Add physics coordinate system note to G3.01 (moderate value)

---

## 10. FINAL ASSESSMENT

### 10.1 Overall Quality: EXCELLENT ⭐⭐⭐⭐ (4/5 stars)

**Strengths:**
- ✅ Dual-track pedagogy (manual + engine) builds deep understanding
- ✅ Excellent scaffolding and progressive refinement
- ✅ High block coverage (91.3% of 46 blocks)
- ✅ Strong real-world connections (G7.06 modeling, G8.06 analytics)
- ✅ Meta-cognitive synthesis skills (G5.12, G8.01)
- ✅ Well-structured grade progression (G3-G8)

**Weaknesses:**
- ❌ No K-2 skills (critical gap)
- ❌ Terminology inconsistencies (shape names)
- ❌ Minor block coverage gaps (3 blocks)
- ❌ One circular dependency (G5→G6)
- ⚠️ G5 potentially overloaded (18 skills, but well-scaffolded)

### 10.2 Readiness for Implementation
**Status:** READY after HIGH priority fixes (8 issues)

**Estimated Effort:**
- HIGH priority fixes: 4-6 hours (add K-2 skills, fix terminology, add 3 skills, update descriptions)
- MEDIUM priority fixes: 2-3 hours (update descriptions, add notes)
- LOW priority fixes: 1 hour (optional improvements)

**TOTAL ESTIMATED EFFORT:** 7-10 hours

---

## 11. BLOCK MAPPING REFERENCE

### 11.1 Blocks WITH Skills (43/46)

| Block ID | Syntax | Skill(s) |
|----------|--------|----------|
| physics_enablephysics | initialize 2D physics world | T17.G5.05 |
| physics_setphysicsbody | behave as [TYPE] [SENSOR] shape [SHAPE] | T17.G5.06, G5.06.01 |
| physics_setphysicsbody2 | compound shape | T17.G5.06.03 |
| physics_removecollider | remove physics-based behavior | T17.G5.10.01 |
| physics_updatephysicsbody | update density friction restitution | T17.G5.09, G6.01, G6.02 |
| physics_setvelocityx | set x speed | T17.G6.02.01 |
| physics_setvelocityy | set y speed | T17.G6.02.01 |
| physics_setvelocitydir | set speed in direction | T17.G6.02.01 |
| physics_setrotationspeed | set rotation speed | T17.G7.04.01 |
| physics_setdirbyvelocity | point in direction of speed | T17.G7.01.01 |
| physics_addforce | add force in direction | T17.G5.08.01, G7.02 |
| physics_addforce2 | add force at position | T17.G7.02.02 |
| physics_clearforce | remove all forces | T17.G7.02.01 |
| physics_addtorque | add torque | T17.G7.04.01 |
| physics_cleartorque | remove all torques | T17.G7.02.01 |
| physics_applyimpulse | apply impulse | T17.G5.08 |
| physics_applyimpulse2 | apply impulse at position | T17.G5.08.02 |
| physics_applytorqueimpulse | apply torque impulse | T17.G7.04.01 |
| physics_lockmovement | prevent body movement | T17.G6.06.01 |
| physics_lockrotation | prevent body rotation | T17.G6.06.01 |
| physics_setdampingfactor | set damping factor | T17.G7.03.01 |
| physics_broadcastcollisioneventmessage | broadcast when colliding | T17.G6.04 |
| physics_broadcastcollisioneventmessage2 | broadcast when finish colliding | T17.G6.04.01 |
| physics_addtocollisiongroup | add to collision group | T17.G6.05 |
| physics_removecollisionfilter | disable collision with group | T17.G6.05 |
| physics_setdominancegroup | set dominance group | T17.G6.05.01 |
| physics_setccd | enable CCD for fast objects | T17.G8.04.01 |
| physics_setgravityscale | set gravity scale | T17.G8.05 |
| physics_settimespeed | set physics time speed | T17.G8.05 |
| physics_addfixedjoint | fix relative position | T17.G8.02 |
| physics_removefixedjoint | remove relative position constraint | T17.G8.02 (implicit) |
| physics_addrevoltejoint | set as rotation axis | T17.G8.02.01 |
| physics_removerevoltejoint | remove rotation axis | T17.G8.02.01 (implicit) |
| physics_setrotationaxisspeed | set rotation axis speed | T17.G8.02.01 |
| physics_setedgecollider | set world border collider | T17.G6.07.01 |
| physics_setedgecollisiongroup | set world border collision group | T17.G6.07.01 (partial) |
| physics_addprismaticjoint | allow sliding | T17.G8.02.02 |
| physics_turnoncollisiondetection | turn on ground detection | T17.G6.04.02 |
| physics_getvelocityx | (x speed) | T17.G7.05 |
| physics_getvelocityy | (y speed) | T17.G7.05 |
| physics_getMass | (mass) | T17.G7.05 |
| physics_getangularvelocity | (angular speed) | T17.G7.05 |
| physics_getcollidingbottom | <in collision below> | T17.G6.04.02 |
| physics_getgroundslope | (ground slope) | T17.G6.04.02 (partial) |

### 11.2 Blocks WITHOUT Skills (3/46) ⚠️

| Block ID | Syntax | Missing Skill |
|----------|--------|---------------|
| physics_setvelocitymovingdir | set speed in moving direction | NEW: T17.G6.02.01.01 needed |
| physics_removefromcollisiongroup | remove from collision group | NEW: T17.G6.05.02 OR expand G6.05 |
| physics_addcollisionfilter | enable collision with group | UPDATE: Expand G6.05 description |

---

## APPENDIX A: COMPLETE SKILL LIST BY GRADE

### Grade 3 (2 skills)
- T17.G3.01: Observe position changes from motion blocks
- T17.G3.02: Predict direction and distance of sprite motion

### Grade 4 (2 skills)
- T17.G4.01: Simulate falling with repeated motion
- T17.G4.02: Explain speed as position change over time

### Grade 5 (18 skills)
**Manual Physics Track:**
- T17.G5.02: Track gravity with velocity variables
- T17.G5.03: Use horizontal speed and friction variables
- T17.G5.04: Code a manual bounce with energy loss

**Engine Physics Track:**
- T17.G5.05: Initialize a 2D physics world
- T17.G5.06: Attach a dynamic body to a sprite
- T17.G5.06.A: Practice creating multiple dynamic bodies
- T17.G5.06.01: Select Box and Circle body shapes
- T17.G5.06.02: Create sensor bodies for trigger zones
- T17.G5.06.03: Create compound shapes for complex sprites
- T17.G5.07: Build fixed boundaries for floors and walls
- T17.G5.08: Apply an impulse to jump or push
- T17.G5.08.01: Distinguish forces from impulses
- T17.G5.08.02: Apply impulse at a position for rotation
- T17.G5.09: Configure density for mass control
- T17.G5.10: Trace simple 2D physics motion
- T17.G5.10.01: Remove physics body from a sprite
- T17.G5.11: Debug missing physics setup
- T17.G5.12: Choose manual vs engine-based physics

### Grade 6 (16 skills)
- T17.G6.01: Configure surface friction parameters
- T17.G6.02: Control restitution (bounce) parameters
- T17.G6.02.01: Set velocity directly for physics bodies
- T17.G6.02.02: Compare dynamic vs movable body types
- T17.G6.03: Build a movable (kinematic) moving platform
- T17.G6.04: Detect collisions for scoring or triggers
- T17.G6.04.01: Detect collision end events
- T17.G6.04.02: Use ground detection for platformer jumping
- T17.G6.04.03: Identify collision management needs
- T17.G6.05: Use collision groups to filter interactions
- T17.G6.05.01: Use dominance groups for one-way interactions
- T17.G6.06: Blend manual and engine sprites in a level
- T17.G6.06.01: Lock movement or rotation of physics bodies
- T17.G6.07: Debug unstable physics behavior
- T17.G6.07.01: Configure world border properties
- T17.G6.08: Compare simulations to real-world motion

### Grade 7 (13 skills)
- T17.G7.01: Launch a configurable projectile
- T17.G7.01.01: Point sprite in movement direction
- T17.G7.02: Combine multiple forces simultaneously
- T17.G7.02.01: Clear forces and torques from physics bodies
- T17.G7.02.02: Apply force at a position for continuous rotation
- T17.G7.03: Simulate drag with manual force calculations
- T17.G7.03.01: Use built-in damping as alternative to manual drag
- T17.G7.04: Build chains or stacks of physics objects
- T17.G7.04.01: Use rotation speed and torque
- T17.G7.05: Read velocity and mass reporters
- T17.G7.05.01: Instrument and graph motion data
- T17.G7.06: Model a real-world physics scenario
- T17.G7.07: Evaluate whether a simulation meets requirements

### Grade 8 (9 skills)
- T17.G8.01: Design and balance a physics-based arcade game
- T17.G8.02: Implement fixed joints for connected objects
- T17.G8.02.01: Implement revolute joints for hinges
- T17.G8.02.02: Implement prismatic joints for sliding
- T17.G8.03: Build automated physics regression tests
- T17.G8.04: Optimize a physics scene for performance
- T17.G8.04.01: Enable CCD for fast-moving objects
- T17.G8.05: Control gravity scale and time speed
- T17.G8.06: Use instrumentation data to tune difficulty

---

**END OF REPORT**
