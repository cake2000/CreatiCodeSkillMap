# T18 Phase 1 - Issue Tracking Checklist

**Date:** 2025-11-23
**Total Issues:** 49 (High:26, Medium:15, Low:8)

Use this checklist to track fix progress. Mark issues with [x] when resolved.

---

## HIGH PRIORITY (26 issues) - FIX FIRST

### CATEGORY 1: Intra-Topic Dependency Violations (12 issues)

- [ ] **H1** - G3.07 player movement blocked by G3.06 textures
  - Skill: T18.G3.07
  - Fix: Move G3.07 earlier OR simplify G3.06
  - Impact: Breaks basic movement learning flow

- [ ] **H2** - G4.03 camera depends on scene composition + player movement
  - Skill: T18.G4.03
  - Fix: Simplify camera to not require player movement
  - Impact: Can't learn cameras until mastering scenes

- [ ] **H3** - G4.05.01 distance sensors require G3.07 player movement
  - Skill: T18.G4.05.01
  - Fix: Introduce sensors with static objects first
  - Impact: Sensing gated behind movement

- [ ] **H4** - G4.05.02 teaches THREE collision types at once
  - Skill: T18.G4.05.02
  - Fix: Split into 3 skills (raycast, overlap, physics)
  - Impact: Overwhelms students with collision systems

- [ ] **H5** - G4.06 implements collision before understanding types
  - Skill: T18.G4.06
  - Fix: After splitting H4, make depend on understanding skill
  - Impact: Implementation without foundation

- [ ] **H6** - G5.02.01 picking miscategorized under physics
  - Skill: T18.G5.02.01
  - Fix: Move to G4 as independent interaction skill
  - Impact: Basic UI gated behind physics

- [ ] **H7** - G5.02.02 dragging miscategorized under physics
  - Skill: T18.G5.02.02
  - Fix: Move to G4 as G4.X+1 (after picking)
  - Impact: Basic UI gated behind physics

- [ ] **H8** - G5.04 nested loops without scaffolding
  - Skill: T18.G5.04
  - Fix: Add inter-topic dependencies on T04/T07 loops
  - Impact: Advanced pattern without programming foundation

- [ ] **H9** - G6.02 debugging requires nested loops
  - Skill: T18.G6.02
  - Fix: Add G4.X simple debugging, keep G6.02 for complex
  - Impact: Can't debug until mastering nested loops

- [ ] **H10** - G6.03 refactoring no basic version
  - Skill: T18.G6.03
  - Fix: Add G4.X refactor simple repetition, keep G6.03 for advanced
  - Impact: Missing foundational refactoring

- [ ] **H11** - G7.01 waypoint movement missing movement dependencies
  - Skill: T18.G7.01
  - Fix: Add dependency on T18.G3.07 or create G5/G6 intermediate
  - Impact: NPC movement without movement basics

- [ ] **H12** - G8.02 split-screen depends on cutscenes + level data
  - Skill: T18.G8.02
  - Fix: Depend only on camera basics (G4.03, G5.09)
  - Impact: Display technique gated behind unrelated skills

### CATEGORY 2: Skills Too Broad/Complex (6 issues)

- [ ] **H13** - G3.03 scene initialization too simple
  - Skill: T18.G3.03
  - Fix: Combine with G3.04 OR expand to include show axis + background
  - Impact: Wastes skill slot

- [ ] **H14** - G3.04 primitives covers too many shapes
  - Skill: T18.G3.04
  - Fix: Split into G3.04 (box, sphere, cylinder) + G4.X (specialized)
  - Impact: Overwhelming for G3

- [ ] **H15** - G4.02 lighting covers THREE types
  - Skill: T18.G4.02
  - Fix: Split into G4.02 (ambient), G4.02.X (directional), G4.02.Y (spot)
  - Impact: Three light systems at once

- [ ] **H16** - G4.04 import covers TWO systems
  - Skill: T18.G4.04
  - Fix: Split into G4.04 (prebuilt library) + G5.X (URL imports)
  - Impact: Library and external imports mixed

- [ ] **H17** - G5.07 particles covers prebuilt AND custom
  - Skill: T18.G5.07
  - Fix: Split into G5.07 (prebuilt) + G6.X (custom with 6 configs)
  - Impact: Simple and complex particle systems together

- [ ] **H18** - G6.06 constraints covers hinge AND fixed
  - Skill: T18.G6.06
  - Fix: Split into G6.06 (fixed) + G7.X (hinge with motors)
  - Impact: Two constraint types simultaneously

### CATEGORY 3: Missing Fundamental Skills (5 issues)

- [ ] **H19** - Missing basic camera skill in G3
  - Gap: Before G4.03 following camera
  - Fix: Add G3.X or G4.01 "Understand camera position/orientation"
  - Impact: Jump to complex cameras without basics

- [ ] **H20** - Missing basic collision skill
  - Gap: Before G4.05.02 (three types) and G4.06 (raycast)
  - Fix: Add G4.X "Detect when objects overlap" (simple)
  - Impact: No gentle collision introduction

- [ ] **H21** - Missing basic animation skill
  - Gap: Before G4.05 (loop-based animations)
  - Fix: Add G4.X "Animate a 3D object" (single move/rotate)
  - Impact: Jump to looping animations without basics

- [ ] **H22** - Missing loop application to 3D
  - Gap: Between T07.G3 loops and G4.05 complex animations
  - Fix: Add G4.X "Create multiple objects with loops" OR clarify G4.05
  - Impact: First loop use is complex animation

- [ ] **H23** - Missing basic texture skill
  - Gap: G3.06 mixes colors and textures with PBR
  - Fix: Split into G3.06 (colors only) + G4.X (textures only) + G5.05 (PBR)
  - Impact: First texture exposure is overwhelming

### CATEGORY 4: Unclear/Unassessable Descriptions (3 issues)

- [ ] **H24** - G3.08 trace script lacks concrete criteria
  - Skill: T18.G3.08
  - Fix: Specify "3-5 block script, predict position/orientation"
  - Impact: Inconsistent assessments

- [ ] **H25** - G8.04 trade-off analysis too vague
  - Skill: T18.G8.04
  - Fix: "Identify 3+ choices, explain trade-off for each"
  - Impact: Subjective without clear criteria

- [ ] **H26** - G6.02 debugging lacks process
  - Skill: T18.G6.02
  - Fix: Add concrete debugging process steps
  - Impact: Unclear what debugging means

---

## MEDIUM PRIORITY (15 issues) - FIX SECOND

### CATEGORY 5: Dependency Improvements (8 issues)

- [ ] **M1** - G3.04.01 rotation vs G3.05 position overlap
  - Skill: T18.G3.04.01
  - Fix: Clarify descriptions (rotation=orientation, position=location)
  - Impact: Minor overlap

- [ ] **M2** - G3.06 color requires loops?
  - Skill: T18.G3.06
  - Fix: Remove T07.G3.03 dependency if static color changes
  - Impact: Possibly unnecessary dependency

- [ ] **M3** - G4.01 scene composition requires variable display?
  - Skill: T18.G4.01
  - Fix: Remove T09.G3.01.04 dependency
  - Impact: Unclear connection

- [ ] **M4** - G4.04.01 scale only for imported models?
  - Skill: T18.G4.04.01
  - Fix: Depend on G3.04 (primitives) instead of G4.04 (imports)
  - Impact: Unnecessarily limiting

- [ ] **M5** - G5.06.01 shadows require physics?
  - Skill: T18.G5.06.01
  - Fix: Remove T18.G5.02 dependency, keep light dependencies
  - Impact: Incorrectly linking visuals to physics

- [ ] **M6** - G5.08.01 remove objects requires physics?
  - Skill: T18.G5.08.01
  - Fix: Depend on G4.06 or G4.01 instead of G5.03
  - Impact: Basic management gated behind physics

- [ ] **M7** - G7.06 vs G4.07.01 duplicate avatar animations
  - Skills: T18.G7.06, T18.G4.07.01
  - Fix: Remove G7.06 OR differentiate (single vs state machine)
  - Impact: Significant duplication

- [ ] **M8** - G8.01 level data requires physics puzzles?
  - Skill: T18.G8.01
  - Fix: Remove T18.G7.04 dependency, keep T10.G6.02
  - Impact: Data skill incorrectly depends on physics

### CATEGORY 6: Organization/Coherence (7 issues)

- [ ] **M9** - G3.01/G3.02 unplugged vs coding mismatch
  - Skills: T18.G3.01, T18.G3.02
  - Fix: Make fully unplugged OR convert to coding activities
  - Impact: Unclear activity type

- [ ] **M10** - Sub-skill numbering inconsistent
  - Problem: .01/.02 sub-skills scattered
  - Fix: Renumber so sub-skills appear after parent immediately
  - Impact: Confusing skill order

- [ ] **M11** - G4 to G5 abrupt physics shift
  - Gap: G4 scene building → G5 physics simulation
  - Fix: Add G4.X transition "When to use physics vs manual animation"
  - Impact: Abrupt topic shift

- [ ] **M12** - G5 skills out of order
  - Skills: G5.05 (textures), G5.06 (fog), G5.09 (camera)
  - Fix: Renumber to group: textures together, atmosphere together, camera together
  - Impact: Related skills scattered

- [ ] **M13** - G6 lacks theme
  - Problem: Mixing debugging, refactoring, interaction, effects
  - Fix: Regroup as "advanced interaction" (mouse look, constraints, hierarchies)
  - Impact: Thematic incoherence

- [ ] **M14** - G7/G8 overlapping themes
  - Problem: Both are "advanced topics"
  - Fix: G7=gameplay mechanics, G8=systems & optimization
  - Impact: Unclear grade distinction

- [ ] **M15** - G8.05 car physics disconnected
  - Skill: T18.G8.05
  - Fix: Move to G7 OR add more G8 simulation skills
  - Impact: Lone mechanic in optimization-focused grade

---

## LOW PRIORITY (8 issues) - POLISH LATER

### CATEGORY 7: Minor Description Improvements (8 issues)

- [ ] **L1** - G3.03 "as hidden" parameter detail confusing
  - Skill: T18.G3.03
  - Fix: Simplify, move advanced detail to end
  - Impact: Minor terminology confusion

- [ ] **L2** - G3.05 axis orientation camera-dependent
  - Skill: T18.G3.05
  - Fix: Clarify "in default camera view"
  - Impact: Possible confusion with camera changes

- [ ] **L3** - G4.07 vs G4.07.01 descriptions similar
  - Skills: T18.G4.07, T18.G4.07.01
  - Fix: Clarify embedded vs library animations
  - Impact: Minor conceptual overlap

- [ ] **L4** - G5.06 fog placement too early
  - Skill: T18.G5.06
  - Fix: Move to G4 OR add G4.01 dependency
  - Impact: Slightly over-graded

- [ ] **L5** - G5.06.02 sky too simple for G5
  - Skill: T18.G5.06.02
  - Fix: Move to G4 as scene customization
  - Impact: Over-graded for complexity

- [ ] **L6** - G5.10 joystick placement
  - Skill: T18.G5.10
  - Fix: Renumber as G4.X after player movement
  - Impact: Minor placement issue

- [ ] **L7** - GK/G1/G2 only 1 skill each
  - Skills: T18.GK.01, T18.G1.01, T18.G2.01
  - Fix: Add more unplugged spatial skills (2-3 per grade)
  - Impact: Sparse early progression

- [ ] **L8** - Block syntax inconsistent in descriptions
  - Problem: Some show full syntax, some just names
  - Fix: Standardize to always show key parameters
  - Impact: Minor consistency issue

---

## PROGRESS SUMMARY

**HIGH Priority:** [ ] 0/26 complete (0%)
**MEDIUM Priority:** [ ] 0/15 complete (0%)
**LOW Priority:** [ ] 0/8 complete (0%)

**OVERALL:** [ ] 0/49 complete (0%)

---

## NOTES

Add implementation notes, challenges, or decisions here as you work through fixes:

### Fix Log:
- [Date] [Issue ID] [Status] [Notes]

---

**Issue Tracker Created:** 2025-11-23
**Last Updated:** 2025-11-23
