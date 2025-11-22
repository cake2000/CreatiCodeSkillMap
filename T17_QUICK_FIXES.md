# T17 Quick Fixes - Action Items

## CRITICAL FIXES (Must Do Before Implementation)

### 1. Add K-2 Skills (4-6 skills needed)
**Problem:** NO K-2 skills exist in T17
**Impact:** Early learners excluded from motion concepts

**Add these skills:**

```
ID: T17.K.01
Topic: T17 – 2D Motion & Physics
Skill: Observe sprite position changes (picture-based)
Description: Students watch animations of sprites moving and identify which sprite moved, matching before/after pictures. They recognize that "motion" means a sprite's position changes on the stage.
Dependencies: None

ID: T17.K.02
Topic: T17 – 2D Motion & Physics
Skill: Match sprite to position after motion (picture-based)
Description: Students see a motion block sequence and choose which picture shows where the sprite will end up. They develop spatial reasoning by predicting final positions from simple motion sequences.
Dependencies: T17.K.01

ID: T17.G1.01
Topic: T17 – 2D Motion & Physics
Skill: Identify fast vs slow motion
Description: Students watch two sprite animations and identify which sprite moves faster. They compare motion speeds visually and describe motion using "fast" and "slow" vocabulary.
Dependencies: T17.K.02

ID: T17.G2.01
Topic: T17 – 2D Motion & Physics
Skill: Predict sprite direction from motion blocks (picture choices)
Description: Students look at motion blocks (move 10 steps, turn right, move 10 steps) and choose from picture options showing which direction the sprite will move. They build directional intuition before coding.
Dependencies: T17.G1.01
```

---

### 2. Fix T17.G5.06.01 Shape Terminology
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Line:** 8746-8752

**CURRENT (WRONG):**
```
Dependencies:
* T17.G5.06.01: Select appropriate body shapes (Box, Circle, ConvexHull, Capsule)
```

**CHANGE TO:**
```
Skill: Select basic body shapes (Box, Circle, Capsule)
Description: Students practice choosing between Box, Circle, and Capsule collision shapes for different sprites. They understand that Box works well for rectangular objects, Circle for round objects, and Capsule for elongated objects. They observe how shape choice affects collision behavior and learn to select the simplest shape that matches their sprite. Advanced: Convex Hull automatically fits the sprite outline but may impact performance.

Dependencies:
* T17.G5.06.A: Practice creating multiple dynamic bodies
```

**ALSO UPDATE LINE 8771:**
```
Dependencies:
* T17.G5.06.01: Select basic body shapes (Box, Circle, Capsule)
```

---

### 3. Remove Circular Dependency: T17.G5.06.02
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Line:** 8762

**CURRENT (WRONG):**
```
Dependencies:
* T17.G5.06.01: Select Box and Circle body shapes
* T17.G6.04: Detect collisions for scoring or triggers
```

**CHANGE TO:**
```
Dependencies:
* T17.G5.06.01: Select basic body shapes (Box, Circle, Capsule)
```

**REASON:** G5 skill cannot depend on G6 skill (forward dependency violation)

---

### 4. Add Missing Skill: Set Speed in Moving Direction
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Insert after:** T17.G6.02.01

```
ID: T17.G6.02.01.01
Topic: T17 – 2D Motion & Physics
Skill: Maintain constant speed in current direction
Description: Students use `set speed [value] in moving direction` to regulate an object's speed without changing its trajectory. This is useful for maintaining constant character movement speed, limiting maximum velocity, or normalizing physics-driven velocities while preserving direction changes from collisions or forces.

Dependencies:
* T17.G6.02.01: Set velocity directly for physics bodies
```

---

### 5. Fix Collision Group Coverage
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Line:** 8953-8961

**CURRENT:**
```
ID: T17.G6.05
Skill: Use collision groups to filter interactions
Description: Students use `add to collision group [0-15]` and `disable collision with group [G]` so the player can pass through certain objects (collectibles) while still hitting others (hazards). They reason about selective interactions.
```

**CHANGE TO:**
```
ID: T17.G6.05
Skill: Use collision groups to filter interactions
Description: Students use `add to collision group [0-15]`, `remove from collision group [G]`, `enable collision with group [G]`, and `disable collision with group [G]` to control selective collisions. They configure which groups each object belongs to and which groups it collides with, allowing players to pass through collectibles while still hitting hazards. They dynamically modify group membership for effects like temporary invincibility or phasing through walls.
```

---

### 6. Fix World Border Collision Groups
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Line:** 9001-9009

**CURRENT:**
```
ID: T17.G6.07.01
Skill: Configure world border properties
Description: Students use `set world border collider friction [value]% restitution [value]%` and `set world border collision group` to customize how objects interact with the automatic stage boundaries. They create bouncy walls or remove border collisions for objects that should wrap around.
```

**CHANGE TO:**
```
ID: T17.G6.07.01
Skill: Configure world border properties
Description: Students use `set world border collider friction [value]% restitution [value]%` and `set world border collision group [COLLISIONGROUP] colliding with group [TARGETGROUP]` to customize how objects interact with the automatic stage boundaries. They create bouncy walls, configure selective border collisions for different object types (e.g., players hit borders but bullets pass through), or remove border collisions for objects that should wrap around.
```

---

### 7. Update Ground Detection Skill (Add Slope Reporter)
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Line:** 8935-8942

**CURRENT:**
```
Description: Students enable `turn on ground detection within distance [value] debug [Yes]` and use the `<in collision below>` reporter to allow jumping only when grounded. They configure detection distance and debug detection issues.
```

**CHANGE TO:**
```
Description: Students enable `turn on ground detection within distance [value] debug [Yes]` and use the `<in collision below>` boolean reporter to allow jumping only when grounded. They also use the `(ground slope)` reporter to detect inclined surfaces and adjust character behavior on slopes. They configure detection distance and debug detection issues.
```

---

### 8. Update Joint Removal Documentation
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md

**Line 9162-9170 (T17.G8.02):**
**CURRENT:**
```
Description: Students use `fix relative position to [sprite]` to weld sprites together so they move as a single rigid unit. Examples: compound objects, multi-part characters, towed vehicles.
```

**CHANGE TO:**
```
Description: Students use `fix relative position to [sprite]` to weld sprites together so they move as a single rigid unit, and `remove relative position constraint` to break the connection. Examples: compound objects, multi-part characters, towed vehicles that can be detached.
```

**Line 9172-9180 (T17.G8.02.01):**
**CURRENT:**
```
Description: Students use `set [sprite] as rotation axis with offset x [X] y [Y]` to create hinged objects like doors, seesaws, and pendulums. They configure rotation behavior with `set rotation axis speed [S] damping factor [D]%`.
```

**CHANGE TO:**
```
Description: Students use `set [sprite] as rotation axis with offset x [X] y [Y]` to create hinged objects like doors, seesaws, and pendulums. They configure rotation behavior with `set rotation axis speed [S] damping factor [D]%`, and use `remove rotation axis` to disconnect hinges. Examples: breakable doors, detachable rotating parts.
```

**Line 9182-9189 (T17.G8.02.02):**
**CURRENT:**
```
Description: Students use `allow [Horizontal/Vertical] sliding relative to [sprite] range from [min] to [max]` to create pistons, sliding doors, and spring-loaded platforms with configurable movement limits.
```

**CHANGE TO:**
```
Description: Students use `allow [Horizontal/Vertical] sliding relative to [sprite] range from [min] to [max]` to create pistons, sliding doors, and spring-loaded platforms with configurable movement limits. Note: Prismatic joints are permanent once created; plan constraint usage during the design phase.
```

---

## MEDIUM PRIORITY (Should Fix)

### 9. Add CCD Tunneling Explanation
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Line:** 9211-9218

**CURRENT:**
```
Description: Students use `enable collision detection as a fast object [Yes]` (Continuous Collision Detection) for bullets, fast balls, or other high-speed objects that might tunnel through thin walls at normal update rates.
```

**CHANGE TO:**
```
Description: Students use `enable collision detection as a fast object [Yes]` (Continuous Collision Detection / CCD) for bullets, fast balls, or other high-speed objects. CCD prevents "tunneling" - when objects move so fast they skip past thin walls between physics updates, passing through without colliding. Essential for projectiles and high-velocity objects.
```

---

### 10. Document Physics World Re-initialization
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Line:** 8718-8726

**CURRENT:**
```
Description: Students add the `initialize 2D physics world with gravity x [0] y [-100]` block, set appropriate gravity values, and confirm the debug overlay shows the world running. They understand that no physics behavior occurs until this block executes.
```

**CHANGE TO:**
```
Description: Students add the `initialize 2D physics world with gravity x [0] y [-100]` block, set appropriate gravity values, and confirm the debug overlay shows the world running. They understand that no physics behavior occurs until this block executes. Note: Running this block again resets the entire physics world, useful for level transitions or game resets.
```

---

### 11. Clarify Performance Measurement
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Line:** 9200-9209

**CURRENT:**
```
Description: Students profile a busy physics scene and implement optimizations: using simpler collision shapes (Box instead of Convex Hull), reducing active object count, using compound shapes sparingly, disabling unnecessary collision groups, and hiding debug overlays.
```

**CHANGE TO:**
```
Description: Students identify performance bottlenecks in a busy physics scene by observing frame rate and lag during playtesting. They implement optimizations: using simpler collision shapes (Box instead of Convex Hull), reducing active object count, using compound shapes sparingly, disabling unnecessary collision groups, and hiding debug overlays. They verify improvements through repeated playtesting.
```

---

## SUMMARY CHECKLIST

- [ ] Add 4 K-2 skills (K.01, K.02, G1.01, G2.01)
- [ ] Fix T17.G5.06.01 shape terminology (line 8746-8752, 8771)
- [ ] Remove circular dependency in T17.G5.06.02 (line 8762)
- [ ] Add T17.G6.02.01.01 (set speed in moving direction)
- [ ] Update T17.G6.05 for collision group coverage (line 8953-8961)
- [ ] Update T17.G6.07.01 for border collision groups (line 9001-9009)
- [ ] Update T17.G6.04.02 for ground slope reporter (line 8935-8942)
- [ ] Update T17.G8.02 joint removal docs (line 9162-9189)
- [ ] Update T17.G8.04.01 CCD explanation (line 9211-9218)
- [ ] Update T17.G5.05 re-initialization note (line 8718-8726)
- [ ] Update T17.G8.04 performance measurement (line 9200-9209)

**ESTIMATED TIME:** 7-10 hours total
- Critical fixes: 4-6 hours
- Medium priority: 2-3 hours
- Testing/validation: 1 hour
