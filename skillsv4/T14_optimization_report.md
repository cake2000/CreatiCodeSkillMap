# T14 (2D Games) Optimization Report - Phase 1

## Executive Summary

This report analyzes all 66 skills in Topic 14 (2D Games) and provides comprehensive recommendations for improving internal coherence, dependency structure, and skill descriptions. The analysis identified several high-priority issues requiring immediate attention, along with medium and low-priority improvements.

---

## Current T14 Skills Inventory

### Grade Distribution:
- **GK (Kindergarten)**: 4 skills (T14.GK.01 - T14.GK.04)
- **G1 (Grade 1)**: 5 skills (T14.G1.01 - T14.G1.05)
- **G2 (Grade 2)**: 5 skills (T14.G2.01 - T14.G2.05)
- **G3 (Grade 3)**: 11 skills (T14.G3.01 - T14.G3.11)
- **G4 (Grade 4)**: 15 skills (T14.G4.01 - T14.G4.15)
- **G5 (Grade 5)**: 10 skills (T14.G5.01 - T14.G5.10)
- **G6 (Grade 6)**: 6 skills (T14.G6.01 - T14.G6.06)
- **G7 (Grade 7)**: 5 skills (T14.G7.01 - T14.G7.05)
- **G8 (Grade 8)**: 5 skills (T14.G8.01 - T14.G8.05)

---

## CreatiCode 2D Game Feature Verification

Based on analysis of `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`, the following game-relevant features are available:

### Core 2D Game Categories:
1. **Motion**: Standard movement blocks (change x/y, glide, point towards, move steps)
2. **Viewport System**:
   - `viewport x`, `viewport y` reporters
   - `attach to viewport at x (XPOS) y (YPOS)` for HUD elements
   - `move viewport to x (XPOS) y (YPOS)` for camera control
   - `lock viewport to sprite [SPRITENAME]` for following player
   - `detach from viewport` for cutscenes
3. **Looks**: show/hide, costumes, graphic effects, size, printing text
4. **Events**: broadcast with parameters, when touching sprite/color
5. **Sensing**: touching detection, distance, key pressed, mouse position
6. **Control**: loops, conditionals, cloning, wait
7. **Game Category** (specialized):
   - `record player score (VALUE)` for leaderboards
   - `show game leaderboard` / `hide game leaderboard`
   - `store user data key [KEY] value [VALUE]` for save data
   - `read user data key [KEY]` for loading progress
8. **Clone Management**:
   - `create clone of [SPRITENAME] with ID [CLONEID]`
   - `clone ID` reporter
   - `clone ID of touched [SPRITENAME]` for tracking which clone was hit
9. **2D Physics** (optional advanced feature):
   - Collision broadcasting
   - Ground detection with raycasting

All T14 skills align well with available CreatiCode features.

---

## HIGH Priority Issues

### 1. X-2 Rule Violations (Dependencies on Skills 3+ Grades Later)

**T14.G3.07: Switch to game mode**
- Current dependencies include T11.G3.01 (8 grades away from GK!)
- **Fix**: Remove T11.G3.01, T10.G3.01 dependencies. These are about custom blocks and lists which are not essential for basic "show sprites after broadcast" functionality.
- **Updated dependencies**: T14.G3.06, T06.G3.05 (trace event and predict output)

**Multiple G4 skills depend on G3 skills with excessive cross-topic deps**
- Many G4 skills carry forward dependencies from T06, T07, T08, T09 at G3 level
- Several include redundant dependencies like "T06.G3.01" appearing 5-7 times across related skills
- **Fix**: Consolidate and reduce to essential prerequisites only

### 2. Circular/Inverted Dependencies Within T14

**T14.G4.01 depends on T14.G3.01 but also includes many lower-level skills**
- Has 5 dependencies when only T14.G3.01 and basic conditional/loop skills are needed
- **Fix**: Remove T06.G3.02, T07.G3.05, T08.G3.01, T08.G3.05 - these are already prerequisites of T14.G3.01

**T14.G5.01 depends on T14.G4.01 (Spawn projectile)**
- This doesn't make sense - gravity/physics shouldn't require projectile spawning
- **Fix**: Change to depend on T14.G4.02 (Move a projectile) or T14.G3.01 (basic movement)

### 3. Missing Foundational Skills

**Gap: No "Detect collision with enemy" skill before damage/lives**
- T14.G3.05 exists but is underutilized in dependencies
- T14.G4.07 (Lives) should explicitly depend on T14.G3.05
- **Fix**: Add T14.G3.05 as prerequisite to T14.G4.07, T14.G4.15

**Gap: Basic sprite cloning not scaffolded**
- T14.G3.11 jumps into clones for collectibles without prior clone exposure
- Students need simpler clone introduction first
- **Fix**: Create T14.G3.10.01: "Create and delete a single clone" as sub-skill

### 4. Overly Broad Skills Needing Breakdown

**T14.G4.04: Simple enemy movement**
- Covers both "back and forth" and "bounce off edges" - these are different patterns
- **Fix**: Split into:
  - T14.G4.04.01: Enemy patrol (back and forth between points)
  - T14.G4.04.02: Enemy bounce (if on edge, bounce)

**T14.G5.08: Timed waves**
- Combines spawn timing, wave counting, AND difficulty scaling
- Too complex for single G5 skill
- **Fix**: Split into:
  - T14.G5.08.01: Spawn enemies at timed intervals
  - T14.G5.08.02: Track and increment wave numbers
  - T14.G5.08.03: Increase difficulty per wave (depends on T14.G5.08.02)

**T14.G6.02: Hitbox separation**
- Very advanced technique mixing invisible sprites + following + collision
- **Fix**: Consider moving to G7 or split into:
  - T14.G6.02.01: Create hidden collision sprite
  - T14.G6.02.02: Make art sprite follow hitbox

### 5. Duplicate/Overlapping Skills

**T14.G4.06 (Score) and T14.G5.09 (High score list)**
- Both deal with scoring but G5.09 depends on G4.06 properly (good)
- However, description overlap exists
- **Fix**: Clarify T14.G4.06 focuses on single-session score tracking; T14.G5.09 on persistent leaderboards

**T14.G4.08 (Timer) and aspects of T14.G5.08 (Timed waves)**
- Both use timers with wait blocks
- **Fix**: Ensure T14.G5.08 dependencies include T14.G4.08 (already present - good!)

---

## MEDIUM Priority Issues

### 6. Same-Grade Unnecessary Dependencies

**Many G4 skills depend on each other unnecessarily**
Examples:
- T14.G4.03 depends on T14.G4.02 (correct - projectile cleanup depends on movement)
- But T14.G4.06 depends on T14.G3.11, not on other G4 skills (correct isolation)

**Analysis**: Most same-grade deps in G4 are actually justified. A few to review:
- T14.G4.15 depends on T14.G4.07 - justified (damage feedback needs lives system)
- T14.G4.10 could stand alone but depends on T14.G3.01 - review if needed

**Recommendation**: Keep most G4 dependencies; they represent genuine skill scaffolding

### 7. Inconsistent Dependency Depth

**Some skills have 2-3 dependencies, others have 6-10**
- T14.G4.01: 5 dependencies (could reduce to 2-3)
- T14.G4.04: 5 dependencies (could reduce to 3)
- T14.G4.09: 7 dependencies (could reduce to 3)

**Fix**: Apply "dependency minimalism" - only include:
1. Direct T14 prerequisite (the immediate prior skill)
2. Essential cross-topic skills (max 2-3)
3. Remove transitive dependencies (if A depends on B, and B depends on C, then A doesn't need to list C)

### 8. Description Clarity Issues

**Vague action verbs**:
- T14.G2.01 "Understand" - not assessable
- **Fix**: "Identify whose turn it is in a multi-player game sequence"

- T14.G3.03 "Keep sprite on screen" - how?
- **Fix**: "Add boundary checking to prevent sprite from moving off-screen using if-statements or 'if on edge, bounce' block"

- T14.G5.04 "Script viewport pans" - what's the outcome?
- **Fix**: Already good, but could add: "...before gameplay begins, creating cinematic introductions"

**Missing concrete examples**:
- T14.G6.06 mentions modes but doesn't give example
- **Fix**: Add "(Play, Pause, Shop, Cutscene)" - ALREADY PRESENT, good!

### 9. Grade-Level Appropriateness Concerns

**T14.G7.01: Spatial partitioning (grid)**
- Very advanced CS concept for Grade 7
- Description is excellent and concrete
- **Concern**: May need teacher scaffolding notes
- **Recommendation**: Keep but flag as "Advanced" or provide scaffolded project

**T14.G8.03: Component-based entities**
- This is essentially ECS (Entity Component System) architecture
- Extremely advanced for Grade 8
- **Recommendation**: Keep but add note: "Challenge skill for advanced students"

---

## LOW Priority Issues

### 10. Minor Description Improvements

**T14.GK.01 - T14.GK.04**: Picture-based activities are perfect for K
**T14.G1.01 - T14.G1.05**: Good concrete picture-based tasks
**T14.G2.01 - T14.G2.05**: Appropriate complexity increase

**Minor wording improvements**:
- T14.G3.09: "Insert `start sound` blocks" → "Add sound effect blocks (play sound) to movement and collision events"
- T14.G4.11: "Store the player's last checkpoint coordinates" → clearer already
- T14.G5.07: "Spawn near viewport" → "Spawn enemies just outside camera view using viewport reporters"

### 11. Missing Cross-References to Game Category Blocks

**T14.G5.09: High score list**
- Could reference CreatiCode's built-in leaderboard blocks
- **Addition**: "Note: CreatiCode also provides 'record player score' and 'show game leaderboard' blocks for persistent online leaderboards"

**T14 skills don't mention user data storage**
- CreatiCode has `store user data key` / `read user data key`
- Could add skill for save/load game state
- **Recommendation**: Add T14.G6.07: "Save and load game progress using user data storage"

### 12. Progression Pacing

**G3 to G4 jump is large (11 skills → 15 skills)**
- G3 covers basic movement, collisions, variables, start/end screens
- G4 adds projectiles, enemies, lives, timer, levels, power-ups
- This is appropriate but worth monitoring

**G7-G8 feel sparse (5 skills each)**
- Could add more advanced skills if needed
- Current skills are very advanced (grid systems, pathfinding, performance)
- **Recommendation**: Current pacing is acceptable; G7-G8 skills are "mastery" level

---

## Dependency Simplification Examples

### Before (T14.G4.01):
```
Dependencies:
* T14.G3.01: Move a sprite with arrow keys (4 directions)
* T06.G3.02: Build a key-press script that controls a sprite
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T08.G3.05: Fix a condition that uses the wrong operator
```

### After (Recommended):
```
Dependencies:
* T14.G3.01: Move a sprite with arrow keys (4 directions)
* T07.G3.01: Use a counted repeat loop
* T08.G3.01: Use a simple if in a script
```

**Rationale**: T06.G3.02 is already a prerequisite of T14.G3.01. Debugging skills (T07.G3.05, T08.G3.05) are helpful but not required dependencies.

---

## K-8 Progression Verification

### K-2: Picture-Based (CORRECT)
- GK: Matching controls, recognizing scores/starts/ends
- G1: Identifying players/goals/obstacles in pictures
- G2: Sequencing routes, tracking lives through picture stories
✅ **Excellent foundation - no coding required**

### G3: Transition to Coding (CORRECT)
- First actual programming: movement, collision detection, variables
- Broadcasting for game states (start, game over)
- Simple effects and collectibles
✅ **Appropriate introduction to game programming**

### G4: Core Game Mechanics (GOOD, needs streamlining)
- Projectiles, enemies, score, lives, timer
- Level transitions, checkpoints, power-ups
⚠️ **Consider moving 1-2 skills to G5 if too dense**

### G5: Advanced Mechanics (GOOD)
- Physics (gravity), camera/viewport control
- Waves, high scores, inventory
✅ **Appropriate advancement**

### G6-G8: Mastery & Optimization (EXCELLENT)
- State machines, hitboxes, streaming, pathfinding, performance
✅ **Challenge-level skills for advanced students**

---

## RECOMMENDATIONS SUMMARY

### Immediate Actions (High Priority):

1. **Fix T14.G3.07 dependencies**: Remove T11.G3.01, T10.G3.01
2. **Reduce redundant cross-topic deps in G4**: Apply "dependency minimalism"
3. **Add sub-skills**:
   - T14.G3.10.01: Create and delete a single clone (before T14.G3.11)
   - T14.G4.04.01: Enemy patrol (back and forth)
   - T14.G4.04.02: Enemy bounce on edges
   - T14.G5.08.01: Spawn enemies at intervals
   - T14.G5.08.02: Track wave numbers
   - T14.G5.08.03: Scale difficulty per wave
4. **Add T14.G3.05 to dependencies** of T14.G4.07, T14.G4.15
5. **Fix T14.G5.01 dependency**: Change from T14.G4.01 to T14.G3.01

### Secondary Actions (Medium Priority):

6. **Streamline all G4 dependencies** - remove transitive deps
7. **Improve action verbs**: T14.G2.01 "Understand" → "Identify"
8. **Add boundary check detail** to T14.G3.03 description
9. **Review T14.G6.02 placement** - consider G7 or split into sub-skills

### Optional Enhancements (Low Priority):

10. **Add new skill T14.G6.07**: Save/load game state with user data
11. **Add notes to T14.G5.09**: Reference built-in leaderboard blocks
12. **Flag advanced skills**: T14.G7.01, T14.G8.03 as "Challenge" skills
13. **Minor description polishing** across 5-6 skills

---

## UPDATED T14 SECTION (READY FOR INSERTION)

See next section for complete revised T14 topic with all fixes applied.

---
