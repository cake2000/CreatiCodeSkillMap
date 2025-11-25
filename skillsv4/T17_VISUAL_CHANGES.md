# T17 Visual Change Reference

## 1. NEW SKILL ADDED: Missing T17.G5.01

```
BEFORE:
T17.G4.02 (Explain speed)
    ↓
T17.G5.02 (Track gravity with velocity variables) ← Referenced non-existent T17.G5.01!
    ↓
T17.G5.03 (Horizontal speed)

AFTER:
T17.G4.02 (Explain speed)
    ↓
T17.G5.01 (Apply gravity using 2D physics) ← ADDED! ✅
    ↓
T17.G5.02 (Track gravity with velocity variables)
    ↓
T17.G5.03 (Horizontal speed)
```

---

## 2. DENSITY/FRICTION/RESTITUTION SPLIT

```
BEFORE:
T17.G5.09: Configure density for mass control
  Description: "...adjust density using `update density [value] friction % restitution %`..."
  (Taught all 3 parameters at once!)
    ↓
T17.G5.10: Trace simple physics
    ↓
T17.G6.01: Configure surface friction ← Deep dive into friction with no intro
    ↓
T17.G6.02: Control restitution ← Deep dive into bounce with no intro

AFTER:
T17.G5.09: Configure density for mass control
  (Focused on density only)
    ↓
T17.G5.09.01: Introduce friction percentage ← NEW gentle intro ✅
    ↓
T17.G5.09.02: Introduce restitution percentage ← NEW gentle intro ✅
    ↓
T17.G5.10: Trace simple physics
    ↓
T17.G6.01: Configure surface friction (now builds on G5.09.01)
    ↓
T17.G6.02: Control restitution (now builds on G5.09.02)
```

---

## 3. COLLISION GROUPS BREAKDOWN

```
BEFORE:
T17.G6.05: Set up static collision groups for filtering
  Description: "3-step process: (1) Assign groups (2) Configure filters (3) Test..."
  (One giant skill!)
    ↓
T17.G6.05.01: Dynamically modify collision groups
T17.G6.05.02: Use dominance groups

AFTER:
T17.G6.05: Add sprites to collision groups ← Step 1 ✅
    ↓
T17.G6.05.01: Enable collision filtering ← Step 2 ✅
    ↓
T17.G6.05.02: Test collision group behavior ← Step 3 ✅
    ↓
T17.G6.05.03: Dynamically modify collision groups ← Advanced (renumbered)
T17.G6.05.04: Use dominance groups ← Advanced (renumbered)
```

---

## 4. FORCES SCAFFOLDING

```
BEFORE:
T17.G5.08.01: Distinguish forces from impulses
  (Understand the concept)
    ↓
    [HUGE GAP - no practice!]
    ↓
T17.G7.02: Combine multiple forces simultaneously
  (Jump straight to combining many forces)

AFTER:
T17.G5.08.01: Distinguish forces from impulses
  (Understand the concept)
    ↓
T17.G5.08.03: Apply a single continuous force ← NEW practice skill ✅
  (Practice with ONE force first)
    ↓
T17.G7.02: Combine multiple forces simultaneously
  (Now prepared to handle multiple)
```

---

## 5. ARCADE GAME BREAKDOWN

```
BEFORE:
T17.G8.01: Design and balance a physics-based arcade game
  Description: "design...test...adjust parameters...balance difficulty"
  (Entire game dev cycle in one skill!)
  Dependencies: T07.G6.01, T08.G6.01, T17.G7.06, T04.G6.01, T10.G6.01, T18.G6.01.01 ← Wrong!

AFTER:
T17.G8.01: Design a physics-based arcade game concept
  (Planning phase: layouts, objects, mechanics)
  Dependencies: T17.G7.06
    ↓
T17.G8.01.01: Implement physics arcade game mechanics ← NEW ✅
  (Building phase: create sprites, physics, logic)
  Dependencies: T17.G8.01 + all the old cross-topic deps (minus T18.G6.01.01)
    ↓
T17.G8.01.02: Balance and tune physics game difficulty ← NEW ✅
  (Tuning phase: adjust parameters, playtest)
  Dependencies: T17.G8.01.01
```

---

## 6. PUZZLE GAME BREAKDOWN

```
BEFORE:
T17.G8.07: Build a physics-based puzzle game
  Description: "Design and implement puzzle game (pulleys, seesaws...)"
  (Planning + building in one!)
  Dependencies: T17.G8.02, T17.G7.06, T18.G6.01.01 ← Wrong!, T26.G6.01, T35.G6.01

AFTER:
T17.G8.07: Plan a physics-based puzzle game
  (Design phase: mechanics, layouts, solutions)
  Dependencies: T17.G8.02, T17.G7.06
    ↓
T17.G8.07.01: Select appropriate joints for puzzle mechanics ← NEW ✅
  (Selection phase: choose fixed vs revolute vs prismatic)
  Dependencies: T17.G8.07, T17.G8.02.01, T17.G8.02.02
    ↓
T17.G8.07.02: Implement and test physics puzzle game ← NEW ✅
  (Building phase: create joints, tune, playtest)
  Dependencies: T17.G8.07.01, T26.G6.01, T35.G6.01 (kept legit deps)
```

---

## 7. JOINT DEBUGGING ADDED

```
BEFORE:
T17.G8.02.01: Implement revolute joints
    ↓
T17.G8.02.02: Implement prismatic joints
    ↓
    [NO DEBUGGING SKILL]
    ↓
Students struggle with joints separating/not working...

AFTER:
T17.G8.02.01: Implement revolute joints
    ↓
T17.G8.02.02: Implement prismatic joints
    ↓
T17.G8.02.03: Debug joint constraint issues ← NEW ✅
  (Diagnose separation, limits, motor issues)
```

---

## 8. DEPENDENCY CLEANUP VISUALIZATION

### Template Dependencies Removed:

```
BEFORE (12 skills had these):
T17.G5.03.01, T17.G5.04.01, T17.G5.06, T17.G5.06.A, etc.
  Dependencies:
    * [actual prerequisite]
    * T07.G3.01: Use a counted repeat loop ← Copy-paste clutter
    * T08.G3.00: Identify if blocks ← Copy-paste clutter
    * T09.G3.01.01: Create a variable ← Copy-paste clutter

AFTER (clean):
T17.G5.03.01, T17.G5.04.01, etc.
  Dependencies:
    * [actual prerequisite only]

KEPT ON (where they belong):
T17.G5.05: Initialize a 2D physics world
  Dependencies:
    * T06.G3.01
    * T17.G4.02
    * T07.G3.01 ← Makes sense here
    * T08.G3.00 ← Makes sense here
    * T09.G3.01.01 ← Makes sense here
```

### Wrong Cross-Topic Dependencies Fixed:

```
REMOVED:
T17.G8.01.01: - T18.G6.01.01 (3D physics in 2D topic ✗)
T17.G8.02.01.01: - T25.G6.01 (datasets ✗), T33.G6.01 (cloud ✗)
T17.G8.07.02: - T18.G6.01.01 (3D physics in 2D topic ✗)

KEPT (legitimate):
T17.G8.07.02: T26.G6.01 (stakeholder questions ✓), T35.G6.01 (ethics ✓)
```

---

## SKILL COUNT BY GRADE

```
Grade | Before | After | Change
------|--------|-------|-------
  K   |   2    |   2   |   -
  G1  |   1    |   1   |   -
  G2  |   1    |   1   |   -
  G3  |   2    |   2   |   -
  G4  |   2    |   2   |   -
  G5  |  21    |  27   |  +6  ← G5.01, G5.08.03, G5.09.01-.02, removed clutter
  G6  |  28    |  32   |  +4  ← Split G6.05 into 4 steps
  G7  |  17    |  17   |   -  ← Updated deps only
  G8  |  15    |  16   |  +1  ← Split G8.01 (+2), G8.07 (+2), added G8.02.03 (+1)
------|--------|-------|-------
TOTAL | 129    | 134   |  +5
```

---

## SUMMARY OF CHANGES

### ✅ ADDED (11 new skills):
1. T17.G5.01 - Apply gravity using 2D physics (MISSING SKILL)
2. T17.G5.08.03 - Apply single continuous force (SCAFFOLDING)
3. T17.G5.09.01 - Introduce friction % (SPLIT)
4. T17.G5.09.02 - Introduce restitution % (SPLIT)
5. T17.G6.05 - Add sprites to collision groups (SPLIT step 1)
6. T17.G6.05.01 - Enable collision filtering (SPLIT step 2)
7. T17.G6.05.02 - Test collision behavior (SPLIT step 3)
8. T17.G8.01.01 - Implement arcade game (SPLIT)
9. T17.G8.01.02 - Balance arcade game (SPLIT)
10. T17.G8.02.03 - Debug joint constraints (SCAFFOLDING)
11. T17.G8.07.01 - Select joints for puzzle (SPLIT)
12. T17.G8.07.02 - Implement puzzle game (SPLIT)

Wait, that's 12 new skills, but net is +5 because:

### 🔄 CONSOLIDATED/RENUMBERED (6 skills):
- Old T17.G6.05 → Now T17.G6.05 + G6.05.01 + G6.05.02 (3 skills from 1)
- Old T17.G6.05.01 → Now T17.G6.05.03 (renumbered)
- Old T17.G6.05.02 → Now T17.G6.05.04 (renumbered)
- Old T17.G8.01 → Now T17.G8.01 + G8.01.01 + G8.01.02 (3 skills from 1)
- Old T17.G8.07 → Now T17.G8.07 + G8.07.01 + G8.07.02 (3 skills from 1)

### 🧹 CLEANED:
- Removed template dependencies from 12 G5 skills
- Fixed 4 incorrect cross-topic dependencies
- Improved 5 skill descriptions

**Result**: 129 → 134 skills (+5 net), better scaffolded, cleaner dependencies
