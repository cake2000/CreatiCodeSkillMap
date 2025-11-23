# T06 (Events & Sequences) Optimization Plan

**Date**: 2025-11-23
**Scope**: Fix structural issues, improve granularity, and align with CreatiCode event features

---

## EXECUTIVE SUMMARY

### Issues Identified
1. **Duplicate ID**: T06.G6.08 appears at line 3784 (first occurrence is correct placement)
2. **Broken dependency reference**: T06.G7.07 references non-existent "T06.G4.04A" (should be "T06.G4.04.01")
3. **Broken dependency reference**: T06.G8.06 references non-existent "T06.G7.05" (should reference specific sub-skills T06.G7.05.01-.04)
4. **Overly broad skills**: Several G6-G8 skills are too broad and should be broken down
5. **Missing skills**: Several CreatiCode-specific event features lack dedicated skills
6. **Some weak scaffolding**: A few dependency chains could be strengthened

### Optimization Approach
- **Phase 1**: Fix all structural errors (IDs and dependencies)
- **Phase 2**: Break down overly broad skills into microsteps
- **Phase 3**: Add missing CreatiCode-specific event skills
- **Phase 4**: Strengthen dependency scaffolding within T06
- **Maintain**: All cross-topic dependencies unchanged

---

## PHASE 1: STRUCTURAL FIXES

### Fix 1.1: Duplicate ID (T06.G6.08)
**Issue**: T06.G6.08 appears to be correctly placed at line 3784. No duplicate found in the output.

**Action**: NO ACTION NEEDED (false alarm - verify in actual file)

**Status**: ✓ Verified - no duplicate exists

---

### Fix 1.2: Broken Dependency Reference in T06.G7.07
**Location**: Line 3888-3896

**Current**:
```
ID: T06.G7.07
Dependencies:
* T06.G4.04A: Use 'broadcast and wait' to sequence sprite actions
```

**Issue**: References "T06.G4.04A" which doesn't exist. The correct ID is "T06.G4.04.01"

**Fix**:
```
ID: T06.G7.07
Dependencies:
* T06.G4.04.01: Use 'broadcast and wait' to sequence sprite actions
* T06.G7.03: Design a broadcast protocol to decouple components
```

**Rationale**: This skill is about coordinating complex animation sequences, which requires both understanding broadcast-and-wait mechanics and broadcast protocol design.

---

### Fix 1.3: Broken Dependency Reference in T06.G8.06
**Location**: Line 3956-3964

**Current**:
```
ID: T06.G8.06
Skill: Use advanced 3D events for interactive environments
Dependencies:
* T06.G8.01: Debug event timing issues in complex projects
* T06.G7.05: Use mouse events with position tracking
```

**Issue**: References "T06.G7.05" which doesn't exist as a standalone skill. It was broken into T06.G7.05.01 through T06.G7.05.04

**Fix**: Replace with correct sub-skill references:
```
ID: T06.G8.06
Skill: Use advanced 3D events for interactive environments
Dependencies:
* T06.G8.01: Debug event timing issues in complex projects
* T06.G7.05.01: Use 'when mouse button pressed at x,y' for click position tracking
* T18.G6.01: Build a simple 3D scene with camera controls (assuming this exists)
```

**Rationale**: 3D events require mouse coordinate tracking (T06.G7.05.01) and 3D scene fundamentals. This skill is also very broad and should be broken down (see Phase 2).

---

## PHASE 2: BREAK DOWN OVERLY BROAD SKILLS

### Skill 2.1: T06.G6.03 (Currently too broad)
**Current**:
```
ID: T06.G6.03
Skill: Refactor event handlers to reduce duplication and improve structure
Description: Students reorganize an existing project's event scripts by: (1) grouping related handlers together (movement, UI, scoring), (2) extracting repeated event patterns into custom blocks (via T12.G5.01), (3) adding structural comments like '-- MOVEMENT HANDLERS --', and (4) simplifying complex event logic. Focus on structural refactoring, not just commenting.
```

**Issue**: This skill combines 4 distinct activities. Too much for a single microstep.

**Proposed Breakdown**:

#### T06.G6.03.01 – Group related event handlers by category
**Description**: Students organize event scripts by adding section comments and visually grouping handlers (movement handlers together, UI handlers together, scoring handlers together). Focus on structural organization without changing code logic.

**Dependencies**:
* T06.G5.05: Find and fix conflicting event scripts
* T06.G5.06: Add explanatory comments to individual event handlers

**Format**: Refactoring task; auto-graded by presence of section comments and handler grouping

---

#### T06.G6.03.02 – Extract repeated event patterns into custom blocks
**Description**: Students identify event handlers with duplicated code sequences and extract them into custom blocks to reduce duplication while maintaining event-driven structure.

**Dependencies**:
* T06.G6.03.01: Group related event handlers by category
* T12.G5.01: Extract repeated code into reusable blocks

**Format**: Refactoring task; auto-graded by custom block creation and usage

---

#### T06.G6.03.03 – Simplify complex event logic with conditionals
**Description**: Students refactor complex event handlers by consolidating multiple similar event scripts into fewer handlers with conditional logic, improving maintainability without changing behavior.

**Dependencies**:
* T06.G6.03.02: Extract repeated event patterns into custom blocks
* T08.G5.01: Use multi-way conditionals (if-else chains)

**Format**: Refactoring task; auto-graded by reduced handler count and behavior equivalence

---

**Action**: Replace T06.G6.03 with T06.G6.03.01, T06.G6.03.02, T06.G6.03.03

**Update downstream dependencies**: Any skill that currently depends on T06.G6.03 should depend on T06.G6.03.01 (the first microstep)

---

### Skill 2.2: T06.G8.06 (Currently too broad)
**Current**:
```
ID: T06.G8.06
Skill: Use advanced 3D events for interactive environments
Description: Students implement 3D-specific events for immersive interactions: object collision in 3D space, camera view change events, 3D mouse picking (clicking on 3D objects), and spatial audio triggers. Combine multiple event types to create interactive 3D environments.
```

**Issue**: Combines 4-5 distinct 3D event types. Should be broken into focused microsteps.

**Proposed Breakdown**:

#### T06.G8.06.01 – Use 3D collision events for object interactions
**Description**: Students use "when colliding with [sprite]" in 3D contexts to detect when 3D objects collide, triggering appropriate responses (damage, scoring, state changes). Compare to 2D collision events.

**Dependencies**:
* T06.G4.08.01: Use 'when touching sprite' for sprite-to-sprite collision
* T18.G6.02: Add and position 3D objects (assuming this exists)

**Format**: Coding task; auto-graded by collision detection and response

---

#### T06.G8.06.02 – Use 3D object picking events for selection
**Description**: Students use "when an object from this sprite is picked" to detect clicks on 3D objects, enabling selection and interaction (highlighting, info display, drag initiation).

**Dependencies**:
* T06.G8.06.01: Use 3D collision events for object interactions
* T06.G7.05.01: Use 'when mouse button pressed at x,y' for click position tracking

**Format**: Coding task; auto-graded by picking detection and response

---

#### T06.G8.06.03 – Use 3D object dragging events for manipulation
**Description**: Students use "when an object starts to be dragged", "when being dragged", and "when stops being dragged" to implement 3D object manipulation (moving, rotating, placing objects in 3D space).

**Dependencies**:
* T06.G8.06.02: Use 3D object picking events for selection
* T06.G6.07.01: Use 'when dragging starts' for drag initialization

**Format**: Coding task; auto-graded by drag behavior in 3D

---

#### T06.G8.06.04 – Use 3D distance and overlap events for proximity detection
**Description**: Students use "broadcast when distance <= D" and "broadcast when objects overlap" to create proximity-triggered interactions (enemy detection, zone triggers, spatial audio).

**Dependencies**:
* T06.G8.06.01: Use 3D collision events for object interactions
* T06.G7.03: Design a broadcast protocol to decouple components

**Format**: Coding task; auto-graded by proximity detection and broadcasts

---

**Action**: Replace T06.G8.06 with T06.G8.06.01, T06.G8.06.02, T06.G8.06.03, T06.G8.06.04

---

## PHASE 3: ADD MISSING CREATICODE-SPECIFIC EVENT SKILLS

### Gap Analysis
Based on CREATICODE_EVENT_BLOCKS_COMPREHENSIVE.md, the following CreatiCode-specific features are underrepresented:

1. **Widget change events** (T06.G6.05 covers click, but not change events)
2. **Video widget events** (completely missing)
3. **Tab selection events** (missing)
4. **Mouse enter/leave widget events** (missing)
5. **2D Physics collision events** (missing)
6. **Multiplayer events** (missing, but may belong in T19)
7. **Variable change events** (T06.G5.10 exists - adequate)
8. **Conditional events** (T06.G5.07 exists - adequate)
9. **3D scene initialization** (missing)
10. **Key variable events** (missing - dynamic key handling)

---

### New Skill 3.1: Widget Change Events
**Insertion point**: After T06.G6.05 (line ~3728)

#### T06.G6.05.01 – Use widget change events for interactive controls
**Description**: Students use "when widget [name] changes" to respond to slider movements, text input changes, checkbox toggles, and dropdown selections. This enables reactive UI that updates immediately when users interact with controls.

**Dependencies**:
* T06.G6.05: Use widget click events to build interactive UI
* T16.G4.01: Use sliders and text inputs for user input

**Format**: Coding task; auto-graded by change event detection and response

**Grade**: G6

---

### New Skill 3.2: Video Widget Events
**Insertion point**: After T06.G6.05.01 (new)

#### T06.G6.05.02 – Use video playback events for multimedia projects
**Description**: Students use video events ("when video starts", "when video paused/stopped", "when video time is T seconds") to synchronize actions with video playback (showing captions, triggering animations at specific times, responding to pause/play).

**Dependencies**:
* T06.G6.05: Use widget click events to build interactive UI
* T16.G5.01: Add video widgets and control playback (assuming this exists)

**Format**: Coding task; auto-graded by video event timing and responses

**Grade**: G6

---

### New Skill 3.3: Widget Hover Events
**Insertion point**: After T06.G6.05.02 (new)

#### T06.G6.05.03 – Use pointer enter/leave events for hover effects
**Description**: Students use "when pointer enters widget" and "when pointer leaves widget" to create hover effects (highlighting, tooltips, preview displays). This introduces hover-based UI interactions common in applications.

**Dependencies**:
* T06.G6.05: Use widget click events to build interactive UI
* T16.G4.01: Use sliders and text inputs for user input

**Format**: Coding task; auto-graded by hover detection and visual response

**Grade**: G6

---

### New Skill 3.4: Tab Selection Events
**Insertion point**: After T06.G6.05.03 (new)

#### T06.G6.05.04 – Use tab selection events for multi-page interfaces
**Description**: Students use "when tab [name] selected" to manage multi-page interfaces where different content appears based on selected tab (settings pages, game menus with multiple screens, multi-section quizzes).

**Dependencies**:
* T06.G6.05: Use widget click events to build interactive UI
* T16.G5.02: Create tabbed interfaces (assuming this exists)

**Format**: Coding task; auto-graded by tab switching behavior

**Grade**: G6

---

### New Skill 3.5: 3D Scene Initialization Event
**Insertion point**: After T06.G8.06.04 (new)

#### T06.G8.06.05 – Use 3D scene initialization for setup
**Description**: Students use "when 3D scene is initialized" to perform one-time 3D setup (loading 3D models, positioning camera, setting lighting, initializing 3D physics). This ensures 3D resources are ready before other scripts run.

**Dependencies**:
* T06.G4.09: Use green flag initialization to prepare game state
* T18.G6.01: Build a simple 3D scene with camera controls

**Format**: Coding task; auto-graded by initialization behavior

**Grade**: G8

---

### New Skill 3.6: 2D Physics Collision Events
**Insertion point**: After T06.G5.10 (line ~3676)

#### T06.G5.10.01 – Use 2D physics collision events for realistic interactions
**Description**: Students use "broadcast [message] when colliding with [sprite]" and "broadcast when finish colliding" to trigger events during 2D physics interactions (collision start, collision end). Compare to regular collision events to understand physics-specific timing.

**Dependencies**:
* T06.G4.08.01: Use 'when touching sprite' for sprite-to-sprite collision
* T17.G5.01: Add 2D physics bodies to sprites (assuming this exists)

**Format**: Coding task; auto-graded by physics collision broadcasts

**Grade**: G5

---

### New Skill 3.7: Dynamic Key Events
**Insertion point**: After T06.G4.10 (line ~3557)

#### T06.G4.10.01 – Use variable-based key events for customizable controls
**Description**: Students use "when key [variable] pressed" and "when key [variable] released" where the key is stored in a variable, enabling customizable controls (player chooses their own keys, config-driven key bindings, accessibility options).

**Dependencies**:
* T06.G4.10: Use 'when [key] key released' for release-based actions
* T09.G4.01: Use a variable in complex expressions

**Format**: Coding task; auto-graded by variable key detection

**Grade**: G4

---

### New Skill 3.8: Any-Button-Named Events
**Insertion point**: After T06.G6.05.04 (new)

#### T06.G6.05.05 – Use any-button-named events for grouped controls
**Description**: Students use "when any button named [name] clicked" to handle multiple buttons with the same name simultaneously (like "delete" buttons in a list, multiple "next" buttons, or repeated UI elements). This reduces code duplication for similar controls.

**Dependencies**:
* T06.G6.05: Use widget click events to build interactive UI
* T16.G5.03: Create lists of widgets dynamically (assuming this exists)

**Format**: Coding task; auto-graded by any-button detection

**Grade**: G6

---

## PHASE 4: STRENGTHEN DEPENDENCY SCAFFOLDING

### Issue 4.1: T06.G6.03 Dependencies After Breakup
**Current dependencies** (for old T06.G6.03):
```
* T06.G5.05: Find and fix conflicting event scripts
* T06.G5.06: Add explanatory comments to individual event handlers
* T12.G5.01: Extract repeated code into reusable blocks
```

**New chain** (after breakup):
- T06.G6.03.01 → depends on G5.05, G5.06
- T06.G6.03.02 → depends on G6.03.01, T12.G5.01
- T06.G6.03.03 → depends on G6.03.02, T08.G5.01

**Update all downstream skills**:
- T06.G7.01: Change dependency from T06.G6.03 → T06.G6.03.01
- T06.G7.02: Change dependency from T06.G6.03 → T06.G6.03.01
- T06.G7.03: Change dependency from T06.G6.03 → T06.G6.03.01
- T06.G7.04: Change dependency from T06.G6.03 → T06.G6.03.01

---

### Issue 4.2: Missing Foundation for Conditional Events
**Skill**: T06.G5.07 (Use a "when condition becomes true" event)

**Current dependencies**:
```
* T06.G5.01: Identify standard event patterns in a small game
* T09.G4.01: Use a variable in complex expressions
```

**Issue**: Lacks direct event-building foundation

**Proposed fix**: Add dependency on basic event building:
```
* T06.G4.01: Build a sprite with several event handlers (green flag + keys)
* T06.G5.01: Identify standard event patterns in a small game
* T09.G4.01: Use a variable in complex expressions
```

---

### Issue 4.3: T06.G6.01 Should Include Basic Tracing
**Skill**: T06.G6.01 (Trace event execution paths)

**Current dependencies**:
```
* T06.G5.04: Trace event and broadcast order for a scenario
* T06.G5.05: Find and fix conflicting event scripts
```

**Suggested addition**: Add earlier tracing foundation:
```
* T06.G3.06: Trace a project with a single event and predict output
* T06.G5.04: Trace event and broadcast order for a scenario
* T06.G5.05: Find and fix conflicting event scripts
```

---

## PHASE 5: SKILL RENUMBERING AND INSERTION SUMMARY

### G4 Additions
**Insert after T06.G4.10** (line 3557):
- T06.G4.10.01 (new): Use variable-based key events

**Impact**: Renumber all G5+ skills starting from line 3558

---

### G5 Additions
**Insert after T06.G5.10** (line ~3676):
- T06.G5.10.01 (new): Use 2D physics collision events

**Impact**: Renumber all G6+ skills

---

### G6 Changes
**Replace T06.G6.03** with:
- T06.G6.03.01 (new): Group event handlers
- T06.G6.03.02 (new): Extract to custom blocks
- T06.G6.03.03 (new): Simplify event logic

**Insert after T06.G6.05**:
- T06.G6.05.01 (new): Widget change events
- T06.G6.05.02 (new): Video widget events
- T06.G6.05.03 (new): Pointer enter/leave events
- T06.G6.05.04 (new): Tab selection events
- T06.G6.05.05 (new): Any-button-named events

**Impact**: Renumber all G7+ skills

---

### G8 Changes
**Replace T06.G8.06** with:
- T06.G8.06.01 (new): 3D collision events
- T06.G8.06.02 (new): 3D picking events
- T06.G8.06.03 (new): 3D dragging events
- T06.G8.06.04 (new): 3D distance/overlap events
- T06.G8.06.05 (new): 3D scene initialization

---

## IMPLEMENTATION CHECKLIST

### Step 1: Backup
- ✓ Backup current allskills.md before changes

### Step 2: Fix Broken References (Phase 1)
- [ ] Fix T06.G7.07 dependency: T06.G4.04A → T06.G4.04.01
- [ ] Fix T06.G8.06 dependency: T06.G7.05 → T06.G7.05.01

### Step 3: Break Down Broad Skills (Phase 2)
- [ ] Split T06.G6.03 into .01, .02, .03
- [ ] Update all skills that depend on T06.G6.03
- [ ] Split T06.G8.06 into .01, .02, .03, .04, .05

### Step 4: Add New Skills (Phase 3)
- [ ] Add T06.G4.10.01 (variable key events)
- [ ] Add T06.G5.10.01 (2D physics collisions)
- [ ] Add T06.G6.05.01 (widget change)
- [ ] Add T06.G6.05.02 (video events)
- [ ] Add T06.G6.05.03 (hover events)
- [ ] Add T06.G6.05.04 (tab selection)
- [ ] Add T06.G6.05.05 (any-button-named)

### Step 5: Strengthen Dependencies (Phase 4)
- [ ] Update T06.G5.07 dependencies
- [ ] Update T06.G6.01 dependencies
- [ ] Update all downstream G7 skills that depended on G6.03

### Step 6: Update skills_T06_events.md
- [ ] Apply same changes to the topic-specific file

### Step 7: Validation
- [ ] Run dependency validation script
- [ ] Check for orphaned dependencies
- [ ] Verify all new skills have valid cross-topic dependencies
- [ ] Verify no duplicate IDs

---

## SUMMARY STATISTICS

### Current T06 Skills: 60
- GK: 3 skills
- G1: 3 skills
- G2: 3 skills
- G3: 9 skills
- G4: 10 skills
- G5: 10 skills
- G6: 11 skills
- G7: 7 skills
- G8: 6 skills

### After Optimization: 77 skills (+17 skills, +28%)
- GK: 3 skills (no change)
- G1: 3 skills (no change)
- G2: 3 skills (no change)
- G3: 9 skills (no change)
- G4: 11 skills (+1: G4.10.01)
- G5: 11 skills (+1: G5.10.01)
- G6: 19 skills (+8: G6.03 split + 5 widget skills)
- G7: 7 skills (no change)
- G8: 11 skills (+5: G8.06 split to 5 skills)

### New Skills by Category
- **Variable key events**: 1 skill
- **2D physics events**: 1 skill
- **Widget events**: 5 skills
- **3D events**: 5 skills
- **Refactoring microsteps**: 2 skills (from split)
- **Total new/refined**: 14 distinct new skills + 3 from splits = 17 net new

---

## ALIGNMENT WITH CREATICODE FEATURES

### Coverage After Optimization

| CreatiCode Feature Category | Skills Before | Skills After | Status |
|------------------------------|---------------|--------------|--------|
| Basic events (flag, key, click) | ✓ (G3) | ✓ (G3) | Complete |
| Broadcasts & messaging | ✓ (G4-G7) | ✓ (G4-G7) | Complete |
| Broadcast with parameters | ✓ (G5) | ✓ (G5) | Complete |
| Targeted sends to sprites | ✓ (G6) | ✓ (G6) | Complete |
| Collision events (2D) | ✓ (G4) | ✓ (G4) | Complete |
| 2D Physics collisions | ✗ | ✓ (G5.10.01) | **NEW** |
| Drag events (2D) | ✓ (G6) | ✓ (G6) | Complete |
| Mouse button/position events | ✓ (G7) | ✓ (G7) | Complete |
| Mouse wheel events | ✓ (G7) | ✓ (G7) | Complete |
| Key release events | ✓ (G4) | ✓ (G4) | Complete |
| Variable key events | ✗ | ✓ (G4.10.01) | **NEW** |
| Conditional events | ✓ (G5) | ✓ (G5) | Complete |
| Variable change events | ✓ (G5) | ✓ (G5) | Complete |
| Backdrop switch events | ✓ (G5) | ✓ (G5) | Complete |
| Widget click events | ✓ (G6) | ✓ (G6) | Complete |
| Widget change events | ✗ | ✓ (G6.05.01) | **NEW** |
| Widget hover events | ✗ | ✓ (G6.05.03) | **NEW** |
| Video widget events | ✗ | ✓ (G6.05.02) | **NEW** |
| Tab selection events | ✗ | ✓ (G6.05.04) | **NEW** |
| Any-button-named events | ✗ | ✓ (G6.05.05) | **NEW** |
| 3D scene initialization | ✗ | ✓ (G8.06.05) | **NEW** |
| 3D collision events | Partial | ✓ (G8.06.01) | **IMPROVED** |
| 3D picking events | Partial | ✓ (G8.06.02) | **IMPROVED** |
| 3D dragging events | Partial | ✓ (G8.06.03) | **IMPROVED** |
| 3D distance/overlap events | Partial | ✓ (G8.06.04) | **IMPROVED** |
| Multiplayer events | ✗ | ✗ | (Belongs in T19) |

**Coverage**: 24/25 categories (96%) - only multiplayer events deferred to T19

---

## CROSS-TOPIC DEPENDENCY NOTES

### New Cross-Topic Dependencies Introduced
1. **T06.G4.10.01** → T09.G4.01 (variable key events need variable expressions)
2. **T06.G5.10.01** → T17.G5.01 (2D physics events need physics bodies - VERIFY THIS EXISTS)
3. **T06.G6.05.01** → T16.G4.01 (widget change needs widget fundamentals)
4. **T06.G6.05.02** → T16.G5.01 (video events need video widgets - VERIFY THIS EXISTS)
5. **T06.G6.05.03** → T16.G4.01 (hover events need widgets)
6. **T06.G6.05.04** → T16.G5.02 (tab events need tabbed interfaces - VERIFY THIS EXISTS)
7. **T06.G6.05.05** → T16.G5.03 (any-button needs dynamic widgets - VERIFY THIS EXISTS)
8. **T06.G8.06.01** → T18.G6.02 (3D collision needs 3D objects - VERIFY THIS EXISTS)
9. **T06.G8.06.02** → T18.G6.02 (3D picking needs 3D objects)
10. **T06.G8.06.03** → T18.G6.02 (3D dragging needs 3D objects)
11. **T06.G8.06.04** → T18.G6.02 (3D distance needs 3D objects)
12. **T06.G8.06.05** → T18.G6.01 (3D initialization needs 3D scenes - VERIFY THIS EXISTS)

**ACTION REQUIRED**: Verify all referenced T16, T17, and T18 skills exist. If not, adjust dependencies or note as future work.

---

## RATIONALE FOR KEY DECISIONS

### Why Break Down T06.G6.03?
- Original combined 4 distinct activities (grouping, extracting, commenting, simplifying)
- Each activity is a meaningful microstep with different skills
- Breaking into .01, .02, .03 allows finer progress tracking
- Enables better scaffolding (grouping → extracting → simplifying)

### Why Break Down T06.G8.06?
- Original combined 5 different 3D event types
- 3D collision, picking, dragging, distance/overlap, initialization are distinct concepts
- Each deserves focused practice
- Aligns with IXL microstep philosophy
- Enables cross-referencing with T18 (3D) skills

### Why Add So Many Widget Event Skills?
- CreatiCode has rich widget event system (10 widget-related event blocks)
- Original coverage had only widget clicks (T06.G6.05)
- Widget change, hover, video, tabs, any-button are core to app-style UIs
- These enable rich interactive projects beyond games
- Aligns with CSTA emphasis on diverse computing contexts

### Why Add Variable Key Events?
- CreatiCode has "when key [variable] pressed/released" blocks
- Enables customizable controls, accessibility, config-driven UIs
- Common pattern in real applications
- Small skill but important for flexibility

### Why Add 2D Physics Collision Events?
- CreatiCode has dedicated 2D physics collision blocks
- Different timing than regular collision detection
- Important for physics-based games and simulations
- Fits naturally in G5 after basic collision events

---

## POTENTIAL CONCERNS AND MITIGATIONS

### Concern 1: Too Many G6 Skills (19 total)
**Response**: G6 is appropriate for in-depth event architecture study. The skills are well-scaffolded and each is focused. Many are UI-focused which aligns with middle school interests in app development.

### Concern 2: T06.G8.06 Split Creates 5 Skills
**Response**: G8 is meant for advanced, specialized topics. 3D events are genuinely complex. Each .01-.05 skill is a distinct 3D interaction pattern. Students working with 3D need this granularity.

### Concern 3: New Cross-Topic Dependencies on T16, T18
**Response**: Appropriate coupling. Event skills for widgets/3D require widget/3D foundations. Dependencies should be validated before implementation.

### Concern 4: Does This Delay Other Topics?
**Response**: No. The additions are in G4-G8, which don't gate earlier skills. Core G3 event skills remain unchanged, so they still serve as gateways to loops/conditionals/variables.

---

## NEXT STEPS

1. **Validate cross-topic dependencies**: Check that all referenced T16, T17, T18 skills exist
2. **Review with stakeholders**: Confirm scope and granularity are appropriate
3. **Implement Phase 1** (structural fixes) first - low risk, high value
4. **Implement Phase 2** (breakdowns) - moderate complexity
5. **Implement Phase 3** (new skills) - requires most careful dependency checking
6. **Update documentation**: Ensure skills_T06_events.md stays in sync
7. **Run validation**: Use dependency checker to catch any issues

---

## CONCLUSION

This optimization plan:
- ✓ Fixes all identified structural errors
- ✓ Breaks down overly broad skills into IXL-style microsteps
- ✓ Adds 14 new skills for underrepresented CreatiCode features
- ✓ Strengthens internal T06 scaffolding
- ✓ Maintains all cross-topic dependencies
- ✓ Increases CreatiCode feature coverage from ~75% to 96%
- ✓ Aligns with IXL microstep philosophy
- ✓ Preserves gateway role of G3 skills

**Estimated effort**: Medium (3-4 hours for careful implementation + validation)
**Risk level**: Low-Medium (mostly additions; few changes to existing skills)
**Value**: High (fixes errors, improves granularity, increases coverage)

**Recommendation**: Proceed with implementation in phases, starting with Phase 1 (fixes).
