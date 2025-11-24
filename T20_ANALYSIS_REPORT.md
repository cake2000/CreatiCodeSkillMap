# T20 (Algorithmic Art & Creative Coding) - Comprehensive Analysis Report

**Analysis Date:** 2025-11-23
**Total Skills Analyzed:** 62 skills (GK through G8)
**Focus:** Clarity, Age-Appropriateness, Progression, Dependencies, CreatiCode Feature Alignment

---

## EXECUTIVE SUMMARY

### Overall Assessment
T20 is a **well-structured topic** with mostly clear skills and good progression. However, there are several issues:

1. **Critical CreatiCode Feature Mismatch**: Multiple skills reference "stamp" blocks that don't exist in CreatiCode
2. **Dependency Issues**: Some skills have dependencies outside the X-2 rule
3. **3D Skill Chain Issues**: The 3D skill sequence has numbering problems and awkward placement
4. **Some Skills Too Broad**: A few G7-G8 skills need breaking down
5. **Missing Scaffolding**: Gaps between some skill levels

### Strengths
- Excellent unplugged foundation (GK-G2)
- Clear technical skill markers at appropriate levels
- Good integration of data visualization concepts
- Strong progression from 2D to 3D art

---

## PART 1: COMPLETE SKILL INVENTORY

### Kindergarten (4 skills)
1. **T20.GK.01** - Picture pattern detective ✓
2. **T20.GK.02** - Order art steps with cards ✓
3. **T20.GK.03** - Continue the pattern trail ✓
4. **T20.GK.04** - Fix the mixed-up art plan (picture-only) ✓

**Assessment:** All appropriate for age. Pure visual/unplugged activities.

---

### Grade 1 (4 skills)
1. **T20.G1.01** - Describe the art rule in words ✓
2. **T20.G1.02** - Match directions to drawings ✓
3. **T20.G1.03** - Extend a quilt on a grid ✓
4. **T20.G1.04** - Fix a wrong instruction (text-based) ✓

**Assessment:** Good progression from K. Adds verbal/text components appropriately.

---

### Grade 2 (4 skills)
1. **T20.G2.01** - Use repeat cards in an art recipe ✓
2. **T20.G2.02** - Plan mirrored mosaics ✓
3. **T20.G2.03** - Build layered pattern recipes ✓
4. **T20.G2.04** - Explain how a change affects the art ✓

**Assessment:** Clear and age-appropriate. Good introduction to repeat concepts.

---

### Grade 3 (7 skills)
1. **T20.G3.01** - Translate art recipe cards into blocks ✓
2. **T20.G3.01.01** - Explain CreatiCode drawing model ✓ **[IMPORTANT]**
3. **T20.G3.02** - Program a repeating border with loops ✓
4. **T20.G3.03** - Trace a drawing loop and predict output ✓
5. **T20.G3.04** - Tile a grid with nested loops ✓
6. **T20.G3.05** - Add simple randomness for variety ✓
7. **T20.G3.05.01** - Use variables to change pattern size ✓

**Assessment:** Excellent transition to code. T20.G3.01.01 correctly identifies CreatiCode's drawing model.

**Key Feature Notes:**
- ✓ Uses "draw rectangle at x y" and "draw oval at x y" (Looks category)
- ✓ Mentions pen blocks for trails
- ✓ Correctly notes NO stamp block exists

---

### Grade 4 (7 skills)
1. **T20.G4.01** - [Technical] Implement incremental loops for spirals ✓
2. **T20.G4.02** - [Technical] Implement tessellation with custom blocks ✓
3. **T20.G4.03** - Control art with parameters ✓
4. **T20.G4.04** - Debug a multi-loop art script ✓
5. **T20.G4.05** - Recolor art with simple input events ✓
6. **T20.G4.05.01** - Map list values to drawing positions ✓
7. **T20.G4.05.02** - Use color reporter for dynamic palettes ✓

**Assessment:** Good technical depth. Color reporter skill correctly references HSV system.

**Feature Verification:**
- ✓ Color reporter block exists: `color (C) saturation (S) brightness (B) transparency (T)`
- ✓ Draw blocks available for spirals and tessellation

---

### Grade 5 (12 skills)
1. **T20.G5.01** - [Technical] Implement simple data-driven visualization ✓
2. **T20.G5.01.01** - Map data to two visual properties ✓
3. **T20.G5.02** - Animate a pattern with a counter variable ✓
4. **T20.G5.03** - Make art respond to mouse or keys ✓
5. **T20.G5.04** - Create fractal-like nested patterns ✓
6. **T20.G5.04.00** - Initialize 3D scenes ✓
7. **T20.G5.04.00.01** - Add box shapes to 3D scenes ✓
8. **T20.G5.04.00.02** - Add sphere shapes to 3D scenes ✓
9. **T20.G5.04.00.03** - Add cylinder shapes to 3D scenes ✓
10. **T20.G5.04.00.04** - Create patterns with 3D shapes ✓
11. **T20.G5.04.01** - Create simple 3D artistic patterns ✓
12. **T20.G5.05** - Explain data-to-visual design choices ✓

**Assessment:** Strong data visualization foundation. 3D sequence has numbering issues.

**Issues:**
- **3D Skill Numbering:** The ".00" pattern (T20.G5.04.00, .00.01, .00.02, etc.) is unusual
- **Better Structure:** Should be T20.G5.05 through T20.G5.09 for 3D basics, then T20.G5.10 for artistic patterns

**Feature Verification:**
- ✓ `initialize 3D scene [SCENETYPE]` exists
- ✓ `add box`, `add sphere`, `add cylinder` blocks exist with correct parameters
- ✓ All referenced 3D features are available

---

### Grade 6 (9 skills)
1. **T20.G6.01** - Trace and explain an art algorithm ✓
2. **T20.G6.02** - Refactor repetitive art into loops/custom blocks ✓
3. **T20.G6.03** - Use variables and conditionals to branch designs ✓
4. **T20.G6.04** - [Technical] Implement multi-field data visualization ✓
5. **T20.G6.05** - Apply math transformations to art ✓
6. **T20.G6.05.01** - Apply materials and textures to 3D art ✓
7. **T20.G6.05.02** - Create 3D curve and line art ✓
8. **T20.G6.05.03** - Create interactive 3D generative art ✓

**Assessment:** Excellent computational thinking focus. Good math integration.

**Feature Verification:**
- ✓ Material blocks exist: `update color diffusion [COLOR] emission [COLOR] roughness (R) brightness (B)`
- ✓ Texture blocks exist: `update texture [TEXTURENAME]`
- ✓ Line/curve blocks exist: `add line`, `add curve using list`
- ✓ All 3D features properly supported

---

### Grade 7 (11 skills)
1. **T20.G7.01** - Compare efficiency of art algorithms ✓
2. **T20.G7.02** - Use while/repeat-until loops in art ✓
3. **T20.G7.03** - Study parameter impact on aesthetics ✓
4. **T20.G7.04** - Analyze real generative artworks ✓
5. **T20.G7.04.00** - Understand particle system basics ✓
6. **T20.G7.04.01** - Create particle-based generative art ✓
7. **T20.G7.05** - Implement rule-based iterative art systems ⚠️
8. **T20.G7.05.01** - Create 3D generative sculptures with particle effects ✓
9. **T20.G7.05.02** - Use lighting to enhance 3D algorithmic art ✓
10. **T20.G7.05.03** - Generate custom 3D shapes from calculated vertices ✓

**Assessment:** Advanced concepts appropriate for G7. Particle system skills well-placed.

**Issues:**
- **T20.G7.05 Too Broad:** L-systems and cellular automata in one skill is too much

**Feature Verification:**
- ✓ Particle system blocks exist: `add particle emitter`, `configure emitter`, `start emitter`
- ✓ Multiple emitter shapes available: Box, Cone, Cylinder, Sphere, Hemispheric, Mesh
- ✓ Lighting blocks exist: directional, point, spot lights with shadows
- ✓ Custom vertex shapes possible with list-based curve creation

---

### Grade 8 (6 skills)
1. **T20.G8.01** - [Technical] Implement multi-dimensional data mapping algorithms ✓
2. **T20.G8.02** - Create constrained generative artwork ✓
3. **T20.G8.03** - Evaluate authorship and originality in generative art ✓
4. **T20.G8.04** - Optimize rendering for performance ✓
5. **T20.G8.05** - Combine multiple algorithms in an art pipeline ⚠️
6. **T20.G8.05.01** - Apply post-processing effects to generative art ✓

**Assessment:** Sophisticated and appropriate for G8. Mix of technical and conceptual.

**Issues:**
- **T20.G8.05 Slightly Unclear:** "Two-phase pipeline" could be more specific

**Feature Verification:**
- ✓ Post-processing effects available through glow layers and emission colors
- ✓ Advanced 3D features support complex rendering scenarios

---

## PART 2: CRITICAL ISSUES FOUND

### Issue 1: CreatiCode Feature Alignment ✓ GOOD
**Status:** NO MAJOR ISSUES FOUND

All skills correctly reference available CreatiCode features:
- Draw blocks (rectangle, oval, line) - ✓ Exist
- 3D blocks (add box, sphere, cylinder) - ✓ Exist
- Particle system blocks - ✓ Exist
- Material/texture blocks - ✓ Exist
- Color reporter with HSV - ✓ Exists
- NO references to non-existent "stamp" block - ✓ Correct

**T20.G3.01.01 is particularly important** - it explicitly teaches that CreatiCode doesn't use stamp blocks and instead uses draw blocks at sprite position.

---

### Issue 2: Dependency Rule Violations (X-2 Rule)

**Problem Skills:**

#### T20.G4.04 - Debug a multi-loop art script
**Dependency:** T06.G3.01 (Grade 3)
**Skill Grade:** Grade 4
**Distance:** 1 grade (OK, but questionable)
**Issue:** Depends on event basics but isn't really about events

**Recommendation:** Remove T06.G3.01 dependency. The skill is about debugging loops, not events.

---

#### T20.G4.05 - Recolor art with simple input events
**Dependency:** T06.G3.01 (Grade 3)
**Skill Grade:** Grade 4
**Distance:** 1 grade (OK)

**Recommendation:** Keep, but verify this is the right event skill.

---

#### T20.G6.04 - Implement multi-field data visualization
**Dependencies include:** T07.G5.01, T08.G5.01, T10.G5.01
**Skill Grade:** Grade 6
**Distance:** 1 grade (OK)

**Assessment:** All within range.

---

#### T20.G8.01 - Implement multi-dimensional data mapping algorithms
**Dependencies include:** T06.G6.01
**Skill Grade:** Grade 8
**Distance:** 2 grades (OK)

**Assessment:** Within X-2 rule.

---

### Issue 3: Skills That Are Too Broad

#### T20.G7.05 - Implement rule-based iterative art systems
**Problem:** Mentions both L-systems AND cellular automata, which are very different
**Current Description:** "...L-systems, cellular automata lite, or simple growth rules..."

**Recommendation: SPLIT into 2-3 skills:**

```
T20.G7.05 - Implement simple substitution rule systems
Description: Students implement simple string substitution systems where each iteration
replaces symbols with patterns (e.g., F → F+F-F, starting with F). They draw the results
using forward movement and turns, creating branching patterns and fractal-like structures.

T20.G7.05.01 - Implement L-system plant structures
Description: Students implement basic L-systems to create plant-like branching structures.
They define rules for growth (e.g., A → AB, B → A), iterate the rules multiple times,
and draw the results using turtle graphics with stack-based branching.

T20.G7.05.02 - Implement simple cellular automata
Description: Students create simple 1D cellular automata (like Rule 30 or Rule 110).
They use lists to represent cell states, apply rules to update each cell based on
neighbors, and visualize the evolution over time using draw blocks to show generations.
```

---

#### T20.G8.05 - Combine multiple algorithms in an art pipeline
**Problem:** "Two-phase pipeline" is vague; "either noise-based OR animation" limits creativity

**Recommendation: REVISE:**

```
T20.G8.05 - Combine multiple algorithms in an art pipeline
Description: Students design and implement a multi-stage algorithmic art system that
combines at least two distinct techniques (e.g., data-driven layout + procedural variation,
fractal generation + color mapping, or particle systems + interactive controls). They
ensure each stage's output feeds into the next, document how stages interact, and explain
how the combination creates effects impossible with single techniques.
```

---

### Issue 4: 3D Skill Numbering Problems

**Current Structure (Grade 5):**
- T20.G5.04 - Create fractal-like nested patterns (2D)
- T20.G5.04.00 - Initialize 3D scenes ← WEIRD
- T20.G5.04.00.01 - Add box shapes to 3D scenes ← WEIRD
- T20.G5.04.00.02 - Add sphere shapes to 3D scenes ← WEIRD
- T20.G5.04.00.03 - Add cylinder shapes to 3D scenes ← WEIRD
- T20.G5.04.00.04 - Create patterns with 3D shapes ← WEIRD
- T20.G5.04.01 - Create simple 3D artistic patterns
- T20.G5.05 - Explain data-to-visual design choices

**Problems:**
1. The ".00" and ".00.01" numbering is non-standard
2. 3D basics are hidden under a 2D fractal skill
3. Hard to find and navigate

**Recommendation: RENUMBER:**

```
Grade 5 - REVISED 3D SEQUENCE:

T20.G5.04 - Create fractal-like nested patterns (2D) [KEEP AS-IS]
T20.G5.05 - Explain data-to-visual design choices [KEEP AS-IS]

T20.G5.06 - Initialize 3D scenes [WAS T20.G5.04.00]
T20.G5.06.01 - Add box shapes to 3D scenes [WAS T20.G5.04.00.01]
T20.G5.06.02 - Add sphere shapes to 3D scenes [WAS T20.G5.04.00.02]
T20.G5.06.03 - Add cylinder shapes to 3D scenes [WAS T20.G5.04.00.03]
T20.G5.06.04 - Create patterns with 3D shapes [WAS T20.G5.04.00.04]
T20.G5.07 - Create simple 3D artistic patterns [WAS T20.G5.04.01]
```

**Impact:** All skills that depend on these will need dependency updates:
- T20.G6.05.01, T20.G6.05.02, T20.G6.05.03
- T20.G7.05.01, T20.G7.05.02
- Any other 3D art skills

---

### Issue 5: Missing Scaffolding

#### Gap 1: Pen Blocks Introduction
**Problem:** T20.G3.01.01 mentions pen blocks for trails, but no explicit skill teaches pen basics

**Recommendation: ADD at G3:**

```
T20.G3.01.02 - Draw trails with pen blocks
Description: Students learn to use pen down/up blocks to draw trails as the sprite moves.
They understand the difference between pen trails (drawn on stage as sprite moves) and
draw blocks (placed at sprite position). They create simple designs by combining movement
with pen down, adjusting pen color and thickness.

Dependencies:
* T20.G3.01.01: Explain CreatiCode drawing model
```

---

#### Gap 2: Basic Animation Before Complex
**Problem:** Jump from static patterns (G3) to counter animations (G5) skips simple animation

**Recommendation: ADD at G4:**

```
T20.G4.06 - Animate art with simple motion
Description: Students add basic animation to their art using forever loops that gradually
change position, rotation, or size. They create effects like spinning patterns, bouncing
elements, or sliding designs using change blocks within loops.

Dependencies:
* T07.G3.03: Build a forever loop for simple animation
* T20.G4.03: Control art with parameters
```

---

#### Gap 3: Color Palettes Before Dynamic Color
**Problem:** Jump from random colors (G3.05) to HSV color reporter (G4.05.02) is steep

**Recommendation: ADD at G4:**

```
T20.G4.05.03 - Create color palettes with lists
Description: Students create predefined color palettes by storing color values in lists.
They select colors from their palette using list indexing or pick random from list,
ensuring consistent color schemes across their art. They understand how lists enable
controlled variety.

Dependencies:
* T10.G4.01: Create a list and add items through code
* T20.G3.05: Add simple randomness for variety
```

---

## PART 3: DUPLICATE AND OVERLAP ANALYSIS

### Within T20 Topic

#### Potential Overlap: Tracing Skills
**T20.G3.03** - Trace a drawing loop and predict output (G3)
**T20.G6.01** - Trace and explain an art algorithm (G6)

**Analysis:** NOT duplicates
- G3 version: Simple loops, visual prediction
- G6 version: Complex algorithms with comments, explain contribution
**Verdict:** ✓ Appropriate progression

---

#### Potential Overlap: Refactoring Skills
**T20.G6.02** - Refactor repetitive art into loops/custom blocks (G6)
**T20.G8.04** - Optimize rendering for performance (G8)

**Analysis:** NOT duplicates
- G6 version: Code organization, DRY principle
- G8 version: Performance profiling, frame rate targets
**Verdict:** ✓ Different focus

---

#### Potential Overlap: Parameter Skills
**T20.G4.03** - Control art with parameters (G4)
**T20.G7.03** - Study parameter impact on aesthetics (G7)

**Analysis:** NOT duplicates
- G4 version: Implementation, sliders, how to parameterize
- G7 version: Systematic analysis, documentation, aesthetic impact
**Verdict:** ✓ Appropriate progression

---

#### Potential Overlap: Data Visualization Skills
**T20.G5.01** - Implement simple data-driven visualization (G5)
**T20.G5.01.01** - Map data to two visual properties (G5)
**T20.G6.04** - Implement multi-field data visualization (G6)
**T20.G8.01** - Implement multi-dimensional data mapping algorithms (G8)

**Analysis:** Clear progression
- G5.01: One list → one property (height)
- G5.01.01: One list → two properties (height + color)
- G6.04: Multiple lists/nested lists → 2-3 properties with conditionals
- G8.01: Complex data (4+ attributes) → multiple channels with optimization

**Verdict:** ✓ Excellent scaffolding

---

### No True Duplicates Found Within T20

All apparent overlaps represent intentional skill progression with increasing sophistication.

---

## PART 4: PROGRESSION ANALYSIS

### Kindergarten → Grade 2: Unplugged Foundation
**Assessment: ✓ EXCELLENT**

Clear progression:
- K: Pure visual pattern recognition
- G1: Adding verbal descriptions
- G2: Repeat concepts, change prediction

No coding required. Builds pattern thinking and algorithmic reasoning.

---

### Grade 3: Transition to Code
**Assessment: ✓ STRONG**

Key transition skill: **T20.G3.01.01 - Explain CreatiCode drawing model**

This is CRITICAL for success because it:
- Distinguishes Looks blocks (draw at position) from pen blocks (trails)
- Explicitly notes stamp doesn't exist
- Prevents student confusion

Progression within G3:
1. Translate cards to blocks (T20.G3.01)
2. Learn drawing model (T20.G3.01.01)
3. Program borders (T20.G3.02)
4. Trace loops (T20.G3.03)
5. Nested loops (T20.G3.04)
6. Add randomness (T20.G3.05)
7. Use variables (T20.G3.05.01)

**Recommendation:** Add pen block skill as noted in Issue 5.

---

### Grades 4-5: Technical Skills + Data Foundation
**Assessment: ✓ GOOD (with issues)**

Grade 4 introduces:
- [Technical Skill] markers (spirals, tessellation)
- Custom blocks for art
- Debugging
- Events for interaction
- Lists for data

Grade 5 adds:
- Data visualization
- 3D graphics
- Animation
- Fractals

**Issue:** 3D numbering needs fixing (see Issue 4)
**Issue:** Missing animation scaffolding (see Issue 5)

---

### Grades 6-7: Advanced Concepts
**Assessment: ✓ STRONG**

Grade 6 focus:
- Algorithm analysis
- Refactoring
- Math transformations
- Advanced 3D (materials, curves)

Grade 7 adds:
- Efficiency comparison
- While loops
- Parameter studies
- Generative art analysis
- Particle systems
- L-systems/CA (needs splitting)

Good balance of computational thinking + artistic concepts.

---

### Grade 8: Sophisticated Integration
**Assessment: ✓ EXCELLENT**

Culmination with:
- Multi-dimensional data algorithms
- Constrained randomness
- Philosophical questions (authorship)
- Performance optimization
- Algorithm pipelines
- Post-processing effects

Appropriate for advanced middle school students.

---

## PART 5: FEATURE VERIFICATION SUMMARY

### Drawing Blocks - ✓ VERIFIED
**Looks Category:**
- `draw rectangle at x (X) y (Y) width (W) height (H) fill [COLOR] border [COLOR] width (W) corner radius (R) rotation (N)`
- `draw oval at x (X) y (Y) width (W) height (H) fill [COLOR] border [COLOR] width (W) rotation (N)`
- `draw line in [COLOR] from x (X1) y (Y1) to x (X2) y (Y2) thickness (T)`

**Pen Category:**
- `draw rectangle width (W) height (H) fill color [COLOR] border width (W) color [COLOR] corner radius (R) rotation (N)`
- `draw oval width (W) height (H) fill color [COLOR] border width (W) color [COLOR] rotation (N)`

**Skills correctly reference these blocks.**

---

### 3D Blocks - ✓ VERIFIED
**3D Scene:**
- `initialize 3D scene [SCENETYPE] as hidden [ISHIDDEN]` ✓

**3D Object:**
- `add box [COLOR] size in x (X) y (Y) z (Z) edge radius (R) as [NAME]` ✓
- `add sphere [COLOR] size in x (X) y (Y) z (Z) arc (A) slice (S) sides (N) as [NAME]` ✓
- `add cylinder [COLOR] diameter top (T) bottom (B) height (H) arc (A) closed section [YES/NO] cap type [TYPE] sides (N) as [NAME]` ✓
- `add line [COLOR] diameter (D) cap [TYPE] arrow [TYPE] sides (S) xyz from (X1) (Y1) (Z1) to (X2) (Y2) (Z2) segments (N) as [NAME]` ✓
- `add curve [COLOR] diameter (D) cap [TYPE] arrow [TYPE] sides (S) using list [LIST] from (START) to (END) segments (N) as [NAME]` ✓

**All skills referencing 3D blocks are accurate.**

---

### Material/Texture Blocks - ✓ VERIFIED
**3D Tools:**
- `update color diffusion [COLOR] emission [COLOR] roughness (R) brightness (B) remove texture [YES/NO] area [TYPE]` ✓
- `update texture [TEXTURENAME] unit size (S) non-box repeat h (H) v (V) rotation (R) area [TYPE]` ✓

**T20.G6.05.01 correctly references these.**

---

### Particle System Blocks - ✓ VERIFIED
**3D Effect:**
- `add particle emitter shape [SHAPETYPE] texture [TEXTURE] facing camera [YES/NO] life min (MIN) max (MAX) capacity (C) GPU [YES/NO] time ratio (R)% as [NAME]` ✓
- `configure box emitter [NAME]: min xyz (X1) (Y1) (Z1) max xyz (X2) (Y2) (Z2)` ✓
- `configure cone emitter [NAME]: radius (R) angle (A) radius range (RR) height range (HR)` ✓
- `configure emitter [NAME] color: start [C1] to [C2] end [C3] to [C4] at progress (P)% [C5] to [C6]` ✓
- `configure emitter [NAME] size: start (S1) to (S2) end (E1) to (E2) at progress (P)% (M1) to (M2)` ✓
- `start emitter [NAME] [by rate/by count] of (N)` ✓
- `[stop/dispose] emitter [NAME]` ✓

**T20.G7.04.00, T20.G7.04.01, T20.G7.05.01 accurately reference particle systems.**

---

### Color Reporter - ✓ VERIFIED
**Looks Category:**
- `color (C) saturation (S) brightness (B) transparency (T)` ✓
  - C: 0-100 (hue)
  - S: 0-100 (saturation)
  - B: 0-100 (brightness)
  - T: 0-100 (transparency)

**T20.G4.05.02 correctly describes HSV system.**

---

### Stamp Block - ✓ CORRECTLY ABSENT
**NO stamp block exists in CreatiCode.**

**T20.G3.01.01 correctly teaches this limitation.**

This is important because many Scratch-based curricula rely on stamp, but CreatiCode uses a different model.

---

## PART 6: RECOMMENDED CHANGES

### Priority 1: Fix 3D Numbering (CRITICAL)
**Renumber the entire 3D sequence in Grade 5:**

```
OLD → NEW
T20.G5.04.00 → T20.G5.06 (Initialize 3D scenes)
T20.G5.04.00.01 → T20.G5.06.01 (Add box shapes)
T20.G5.04.00.02 → T20.G5.06.02 (Add sphere shapes)
T20.G5.04.00.03 → T20.G5.06.03 (Add cylinder shapes)
T20.G5.04.00.04 → T20.G5.06.04 (Create patterns with 3D shapes)
T20.G5.04.01 → T20.G5.07 (Create simple 3D artistic patterns)
```

**Update all dependencies:**
- T20.G6.05.01: Change dep from T20.G5.04.01 → T20.G5.07
- T20.G6.05.02: Change dep from T20.G5.04.01 → T20.G5.07
- T20.G6.05.03: Change dep from T20.G5.04.01 → T20.G5.07
- T20.G7.05.01: Change dep from T20.G5.04.01 → T20.G5.07
- T20.G7.05.02: Change dep from T20.G5.04.01 → T20.G5.07

---

### Priority 2: Split L-systems Skill
**Break T20.G7.05 into 2-3 skills:**

```
T20.G7.05 - Implement simple substitution rule systems
Description: Students implement simple string substitution systems where each iteration
replaces symbols with patterns (e.g., F → F+F-F, starting with F). They draw the results
using forward movement and turns, creating branching patterns and fractal-like structures.

Dependencies:
* T07.G6.05: Fix a loop that runs too many or too few times
* T09.G6.01: Model real-world quantities using variables and formulas
* T20.G6.05: Apply math transformations to art

---

T20.G7.05.01 - Implement basic L-system patterns
Description: Students implement basic Lindenmayer systems to create plant-like branching
structures. They define multiple rules for growth (e.g., A → AB, B → A), iterate the
rules several times, and draw the results using position and direction tracking.

Dependencies:
* T20.G7.05: Implement simple substitution rule systems
* T10.G6.01: Use lists to track structured information

---

T20.G7.05.02 - Implement simple cellular automata
Description: Students create simple 1D cellular automata (like Rule 30 or Rule 110).
They use lists to represent cell states, apply rules to update each cell based on
neighbors, and visualize the evolution over time using draw blocks to show generations.

Dependencies:
* T20.G7.05: Implement simple substitution rule systems
* T10.G6.01: Use lists to track structured information
```

**THEN RENUMBER existing skills:**
```
OLD T20.G7.05.01 → T20.G7.06 (Create 3D generative sculptures with particle effects)
OLD T20.G7.05.02 → T20.G7.07 (Use lighting to enhance 3D algorithmic art)
OLD T20.G7.05.03 → T20.G7.08 (Generate custom 3D shapes from calculated vertices)
```

---

### Priority 3: Add Missing Scaffolding Skills

**Add at Grade 3:**
```
T20.G3.01.02 - Draw trails with pen blocks
Description: Students learn to use pen down/up blocks to draw trails as the sprite moves.
They understand the difference between pen trails (drawn on stage as sprite moves) and
draw blocks (placed at sprite position). They create simple designs by combining movement
with pen down, adjusting pen color and thickness.

Dependencies:
* T20.G3.01.01: Explain CreatiCode drawing model
```

**Add at Grade 4:**
```
T20.G4.06 - Animate art with simple motion
Description: Students add basic animation to their art using forever loops that gradually
change position, rotation, or size. They create effects like spinning patterns, bouncing
elements, or sliding designs using change blocks within loops.

Dependencies:
* T07.G3.03: Build a forever loop for simple animation
* T20.G4.03: Control art with parameters

---

T20.G4.07 - Create color palettes with lists
Description: Students create predefined color palettes by storing color values in lists.
They select colors from their palette using list indexing or pick random from list,
ensuring consistent color schemes across their art. They understand how lists enable
controlled variety.

Dependencies:
* T10.G4.01: Create a list and add items through code
* T20.G3.05: Add simple randomness for variety
```

---

### Priority 4: Fix Dependencies

**T20.G4.04 - Debug a multi-loop art script**
```
REMOVE: T06.G3.01 (not about events)

Keep:
* T07.G3.01: Use a counted repeat loop
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T20.G3.05: Add simple randomness for variety
```

---

### Priority 5: Clarify Broad Skills

**T20.G8.05 - Combine multiple algorithms in an art pipeline**
```
REVISED Description:
Students design and implement a multi-stage algorithmic art system that combines at least
two distinct techniques (e.g., data-driven layout + procedural variation, fractal generation +
color mapping, or particle systems + interactive controls). They ensure each stage's output
feeds into the next, document how stages interact, and explain how the combination creates
effects impossible with single techniques.

Dependencies: [Keep existing]
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds
* T09.G6.01: Model real-world quantities using variables and formulas
* T20.G7.05: Implement rule-based iterative art systems
```

---

## PART 7: SKILLS THAT ARE JUST RIGHT

These skills are excellent examples of IXL-style clarity and should be used as models:

### T20.G3.01.01 - Explain CreatiCode drawing model ⭐
**Why it's great:**
- Addresses platform-specific difference (no stamp)
- Prevents common student confusion
- Clear, specific learning outcome
- Essential foundation for all later art skills

---

### T20.G4.05.02 - Use color reporter for dynamic palettes ⭐
**Why it's great:**
- Specific block referenced
- Clear parameters (HSV 0-100)
- Concrete application (gradients in loops)
- Builds on prior skills appropriately

---

### T20.G5.06.01 through .04 - 3D Shape Sequence ⭐
**Why it's great:**
- Each skill teaches ONE shape type
- Clear progression (box → sphere → cylinder → patterns)
- Manageable chunks
- Builds to composite skill

(Note: Just needs renumbering, content is perfect)

---

### T20.G7.03 - Study parameter impact on aesthetics ⭐
**Why it's great:**
- Specific method (systematic adjustment, table documentation)
- Clear learning objective (analyze impact)
- Appropriate complexity for G7
- Connects programming to artistic concepts

---

### T20.G7.04.00 and .01 - Particle System Sequence ⭐
**Why it's great:**
- .00 teaches concepts (generation, behavior, configuration)
- .01 teaches application (color gradients, movement, standalone art)
- Clear progression from understanding to creation
- Well-matched to CreatiCode features

---

## PART 8: FINAL SKILL COUNT AFTER CHANGES

### Current: 62 skills
- GK: 4
- G1: 4
- G2: 4
- G3: 7
- G4: 7
- G5: 12
- G6: 8
- G7: 10
- G8: 6

### After Recommended Changes: 69 skills (+7)

**Grade 3:** 7 → 8 (+1 pen skill)
**Grade 4:** 7 → 9 (+2 animation and palette skills)
**Grade 7:** 10 → 14 (+4 from splitting L-systems and renumbering)
**Other grades:** No change in count (just renumbering)

---

## PART 9: CROSS-TOPIC DEPENDENCIES

### Dependencies FROM Other Topics (External to T20)

All external dependencies are appropriate and within X-2 rule. Key cross-topic connections:

**T01 (Sequencing & Algorithms):**
- Multiple skills depend on basic sequencing
- ✓ Appropriate foundation

**T04 (Patterns):**
- Early T20 skills build on pattern recognition
- ✓ Natural connection

**T07 (Loops):**
- Heavy use throughout T20
- ✓ Essential for algorithmic art

**T08 (Conditionals):**
- Used for branching designs
- ✓ Appropriate integration

**T09 (Variables):**
- Critical for parameters and animation
- ✓ Well-integrated

**T10 (Lists):**
- Essential for data viz and vertices
- ✓ Good alignment

**T11 (Custom Blocks):**
- Used for modular art functions
- ✓ Appropriate application

**No problematic external dependencies found.**

---

## PART 10: IMPLEMENTATION NOTES

### For Curriculum Designers

1. **T20.G3.01.01 is CRITICAL** - Don't skip or de-emphasize this skill. Students coming from Scratch will expect stamp blocks.

2. **3D sequence needs careful teaching** - Consider creating a unified 3D mini-unit within G5 that teaches all 3D basics together.

3. **Particle systems are advanced** - G7 placement is appropriate, but consider providing templates/examples to help students understand the complex configuration.

4. **Data visualization progression** - The G5→G6→G8 data viz progression is excellent. Make sure students master each level before advancing.

5. **Math integration** - G6-G7 skills assume comfort with sine/cosine and coordinate systems. Consider cross-referencing with math curriculum.

---

### For Assessment Designers

**Clear Success Criteria Skills (Easy to assess):**
- T20.G3.02 - Program a repeating border (does it repeat? is loop used?)
- T20.G3.04 - Tile a grid with nested loops (grid filled? nested loops present?)
- T20.G4.01 - Implement spirals (spiral present? variable increments?)
- T20.G5.01 - Data visualization (data used? visual output correct?)

**Subjective Skills (Need rubrics):**
- T20.G7.03 - Study parameter impact (rubric for documentation quality)
- T20.G7.04 - Analyze generative art (rubric for analysis depth)
- T20.G8.03 - Evaluate authorship (rubric for argument quality)

**Performance Skills (Need benchmarks):**
- T20.G8.04 - Optimize rendering (define target frame rate)

---

## PART 11: SUMMARY OF FINDINGS

### Strengths
✓ Excellent unplugged foundation (GK-G2)
✓ Clear platform-specific teaching (T20.G3.01.01)
✓ Strong data visualization progression
✓ All CreatiCode features accurately referenced
✓ Good balance of technical and artistic concepts
✓ Appropriate use of [Technical Skill] markers
✓ Strong 3D graphics integration
✓ Well-placed particle system skills
✓ No true duplicates within topic
✓ All external dependencies appropriate

### Issues Requiring Action
⚠️ 3D skill numbering (.00, .00.01) needs fixing
⚠️ L-systems skill too broad, needs splitting
⚠️ Missing pen block introduction
⚠️ Missing animation scaffolding
⚠️ Missing color palette scaffolding
⚠️ One unnecessary dependency (T20.G4.04)
⚠️ One skill description could be clearer (T20.G8.05)

### Overall Grade: A- (Excellent with minor fixes needed)

T20 is one of the stronger topics in the skill map. The issues found are mostly organizational (numbering) rather than conceptual. The progression is sound, skills are clear, and CreatiCode features are accurately represented.

---

## APPENDIX A: COMPLETE RENUMBERING MAP

### Grade 5 Changes
```
OLD ID          → NEW ID       SKILL NAME
T20.G5.04.00    → T20.G5.06    Initialize 3D scenes
T20.G5.04.00.01 → T20.G5.06.01 Add box shapes to 3D scenes
T20.G5.04.00.02 → T20.G5.06.02 Add sphere shapes to 3D scenes
T20.G5.04.00.03 → T20.G5.06.03 Add cylinder shapes to 3D scenes
T20.G5.04.00.04 → T20.G5.06.04 Create patterns with 3D shapes
T20.G5.04.01    → T20.G5.07    Create simple 3D artistic patterns
```

### Grade 7 Changes (After L-system split)
```
OLD ID          → NEW ID       SKILL NAME
T20.G7.05       → T20.G7.05    Implement simple substitution rule systems [REVISED]
[NEW]           → T20.G7.05.01 Implement basic L-system patterns [NEW]
[NEW]           → T20.G7.05.02 Implement simple cellular automata [NEW]
T20.G7.05.01    → T20.G7.06    Create 3D generative sculptures with particle effects
T20.G7.05.02    → T20.G7.07    Use lighting to enhance 3D algorithmic art
T20.G7.05.03    → T20.G7.08    Generate custom 3D shapes from calculated vertices
```

### All Dependency Updates Required
Search for and update these dependencies:
- "T20.G5.04.00" → "T20.G5.06"
- "T20.G5.04.00.01" → "T20.G5.06.01"
- "T20.G5.04.00.02" → "T20.G5.06.02"
- "T20.G5.04.00.03" → "T20.G5.06.03"
- "T20.G5.04.00.04" → "T20.G5.06.04"
- "T20.G5.04.01" → "T20.G5.07"
- "T20.G7.05.01" → "T20.G7.06"
- "T20.G7.05.02" → "T20.G7.07"
- "T20.G7.05.03" → "T20.G7.08"

---

## APPENDIX B: NEW SKILLS TO ADD

### Grade 3
```
ID: T20.G3.01.02
Topic: T20 – Algorithmic Art & Creative Coding
Skill: Draw trails with pen blocks
Description: Students learn to use pen down/up blocks to draw trails as the sprite moves.
They understand the difference between pen trails (drawn on stage as sprite moves) and
draw blocks (placed at sprite position). They create simple designs by combining movement
with pen down, adjusting pen color and thickness.

Dependencies:
* T20.G3.01.01: Explain CreatiCode drawing model
```

### Grade 4
```
ID: T20.G4.06
Topic: T20 – Algorithmic Art & Creative Coding
Skill: Animate art with simple motion
Description: Students add basic animation to their art using forever loops that gradually
change position, rotation, or size. They create effects like spinning patterns, bouncing
elements, or sliding designs using change blocks within loops.

Dependencies:
* T07.G3.03: Build a forever loop for simple animation
* T20.G4.03: Control art with parameters

---

ID: T20.G4.07
Topic: T20 – Algorithmic Art & Creative Coding
Skill: Create color palettes with lists
Description: Students create predefined color palettes by storing color values in lists.
They select colors from their palette using list indexing or pick random from list,
ensuring consistent color schemes across their art. They understand how lists enable
controlled variety.

Dependencies:
* T10.G4.01: Create a list and add items through code
* T20.G3.05: Add simple randomness for variety
```

### Grade 7
```
ID: T20.G7.05
Topic: T20 – Algorithmic Art & Creative Coding
Skill: Implement simple substitution rule systems
Description: Students implement simple string substitution systems where each iteration
replaces symbols with patterns (e.g., F → F+F-F, starting with F). They draw the results
using forward movement and turns, creating branching patterns and fractal-like structures.

Dependencies:
* T07.G6.05: Fix a loop that runs too many or too few times
* T09.G6.01: Model real-world quantities using variables and formulas
* T20.G6.05: Apply math transformations to art

---

ID: T20.G7.05.01
Topic: T20 – Algorithmic Art & Creative Coding
Skill: Implement basic L-system patterns
Description: Students implement basic Lindenmayer systems to create plant-like branching
structures. They define multiple rules for growth (e.g., A → AB, B → A), iterate the
rules several times, and draw the results using position and direction tracking.

Dependencies:
* T20.G7.05: Implement simple substitution rule systems
* T10.G6.01: Use lists to track structured information

---

ID: T20.G7.05.02
Topic: T20 – Algorithmic Art & Creative Coding
Skill: Implement simple cellular automata
Description: Students create simple 1D cellular automata (like Rule 30 or Rule 110).
They use lists to represent cell states, apply rules to update each cell based on
neighbors, and visualize the evolution over time using draw blocks to show generations.

Dependencies:
* T20.G7.05: Implement simple substitution rule systems
* T10.G6.01: Use lists to track structured information
```

---

END OF REPORT
