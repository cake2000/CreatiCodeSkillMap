# T20 ALGORITHMIC ART & CREATIVE CODING - COMPREHENSIVE OPTIMIZATION ANALYSIS

**Date**: 2025-11-23
**Status**: Phase 1 Complete Analysis
**Total Skills Analyzed**: 56 skills (K-8)

---

## EXECUTIVE SUMMARY

### Current State
- **Total skills**: 56 (K: 4, G1: 4, G2: 4, G3: 6, G4: 6, G5: 6, G6: 6, G7: 6, G8: 6, plus sub-skills)
- **Major issues identified**: 28 skills with HIGH or MEDIUM priority issues
- **Skills requiring breakdown**: 8 skills too broad
- **Missing skills**: 15 gaps identified for proper scaffolding
- **Dependency issues**: 12 violations of X-2 rule or circular dependencies

### CreatiCode Capabilities Assessment
**2D Drawing Blocks (Looks Category)**:
- `draw rectangle at x (X) y (Y) width (W) height (H) fill [COLOR] border [COLOR] width (W) corner radius (R) rotation (N)`
- `draw oval at x (X) y (Y) width (W) height (H) fill [COLOR] border [COLOR] width (W) rotation (N)`
- `draw line in [COLOR] from x (X1) y (Y1) to x (X2) y (Y2) thickness (T)`
- `draw curve in [COLOR] from x (X1) y (Y1) to x (X2) y (Y2) control 1 x (C1X) y (C1Y) control 2 x (C2X) y (C2Y) thickness (T)`
- `draw text [TEXT] at x (X) y (Y) size (S) color [COLOR] rotation (R)`
- `color (C) saturation (S) brightness (B) transparency (T)` - dynamic color generation

**3D Capabilities (3D Object Category - 50+ blocks)**:
- Basic shapes: box, sphere, cylinder, cone, capsule, torus, tube
- Custom shapes: column (extruded polygon), custom vertices
- 3D lines and curves: solid lines, dotted lines, curves from point lists
- 3D text: flat and thick extruded text

**3D Materials & Lighting (3D Tools & Scene - 47+ blocks)**:
- Materials: diffusion color, emission color, roughness, brightness, textures
- Lights: ambient, directional, point, spot lights
- Advanced: shadows, glow layers, highlight layers
- Post-processing: bloom, vignette, antialiasing, sharpening, contrast, exposure

**Particle Systems (3D Effect - 18 blocks)**:
- Particle emitters with shape (box, cone, sphere, etc.)
- Color gradients over lifetime
- Size changes over lifetime
- Movement patterns and speed
- Blend modes

**CRITICAL FINDING**: CreatiCode does NOT have traditional Scratch pen blocks (pen up/down, stamp, continuous line drawing). All drawing is position-based using Looks category blocks.

---

## SECTION A: ISSUES IDENTIFIED

### Grade K Issues

#### T20.GK.01 - Picture pattern detective
- **Issue Type**: Dependency inaccuracy
- **Priority**: MEDIUM
- **Current Dependencies**: T04.GK.01
- **Problem**: Should depend on T04.GK.01 (pattern recognition foundational skill)
- **Fix**: Add T04.GK.01 dependency if missing

#### T20.GK.02 - Order art steps with cards
- **Issue Type**: Accurate, no issues
- **Priority**: N/A

#### T20.GK.03 - Continue the pattern trail
- **Issue Type**: Accurate, no issues
- **Priority**: N/A

#### T20.GK.04 - Fix the mixed-up art plan
- **Issue Type**: Accurate, no issues
- **Priority**: N/A

### Grade 1 Issues

#### T20.G1.01 - Describe the art rule in words
- **Issue Type**: Accurate, no issues
- **Priority**: N/A

#### T20.G1.02 - Match directions to drawings
- **Issue Type**: Accurate, no issues
- **Priority**: N/A

#### T20.G1.03 - Extend a quilt on a grid
- **Issue Type**: Accurate, no issues
- **Priority**: N/A

#### T20.G1.04 - Fix a wrong instruction
- **Issue Type**: Accurate, no issues
- **Priority**: N/A

### Grade 2 Issues

#### T20.G2.01 - Use repeat cards in an art recipe
- **Issue Type**: Accurate, no issues
- **Priority**: N/A

#### T20.G2.02 - Plan mirrored mosaics
- **Issue Type**: Unnecessary dependency
- **Priority**: MEDIUM
- **Current Dependencies**: T05.G1.01, T01.G1.04
- **Problem**: T05.G1.01 (story character needs) is not relevant to mirror symmetry
- **Fix**: Remove T05.G1.01 dependency, keep T01.G1.04

#### T20.G2.03 - Build layered pattern recipes
- **Issue Type**: Wrong dependency
- **Priority**: HIGH
- **Current Dependencies**: T20.G2.01 (correct)
- **Problem**: Description says depends on "T20.G2.01: Identify win and lose in a simple game" - this is completely wrong, should be T20.G2.01 art recipe
- **Fix**: Verify dependency is correct T20.G2.01 skill

#### T20.G2.04 - Explain how a change affects the art
- **Issue Type**: Accurate, no issues
- **Priority**: N/A

### Grade 3 Issues

#### T20.G3.01 - Translate art recipe cards into blocks
- **Issue Type**: Missing dependency
- **Priority**: MEDIUM
- **Current Dependencies**: T07.G3.01, T20.G2.01
- **Problem**: Missing T06.G3.01 (basic scripting) which should come before loops
- **Fix**: Add T06.G3.01 dependency

#### T20.G3.02 - Program a repeating border with loops
- **Issue Type**: Too broad + Inaccurate terminology
- **Priority**: HIGH
- **Current Dependencies**: T20.G3.01
- **Problems**:
  1. Original description mentions "pen program" and "stamp star" - CreatiCode has NO stamp block
  2. Needs to specify draw blocks: draw rectangle, draw oval
  3. Should be broken into simpler first step
- **Fix**:
  - Rewrite to use draw blocks
  - Consider breaking into T20.G3.02.01 (single shape drawing) and T20.G3.02 (looped pattern)

#### T20.G3.03 - Tile a grid with nested loops
- **Issue Type**: Inaccurate blocks + Excessive dependencies
- **Priority**: HIGH
- **Current Dependencies**: T20.G3.02, T09.G3.01, T07.G3.02, T18.G3.03
- **Problems**:
  1. Should come BEFORE tracing (T20.G3.04), not after
  2. T18.G3.03 (3D lighting) not needed for 2D grid tiling
  3. T09.G3.01 (variables) not essential for basic nested loops
  4. T07.G3.02 (trace loops) should not be prerequisite for doing nested loops
- **Fix**: Simplify to just T20.G3.02 and T07.G3.01

#### T20.G3.04 - Trace a pen loop and predict output
- **Issue Type**: Inaccurate terminology + Wrong ordering
- **Priority**: HIGH
- **Current Dependencies**: T20.G3.03, T08.G3.02, T18.G3.04
- **Problems**:
  1. Says "pen loop" but should be "drawing loop"
  2. Should come BEFORE doing nested loops (T20.G3.03), not after
  3. T08.G3.02 (conditionals) not needed for basic tracing
  4. T18.G3.04 (3D shapes) completely irrelevant to 2D tracing
- **Fix**:
  - Move before T20.G3.03
  - Change to T20.G3.03, T20.G3.02 as dependencies
  - Remove 3D dependencies

#### T20.G3.05 - Add simple randomness for variety
- **Issue Type**: Good description update but dependency issues
- **Priority**: MEDIUM
- **Current Dependencies**: T20.G3.04, T09.G3.02, T07.G3.03
- **Problems**:
  1. Good description with draw blocks
  2. T07.G3.03 (forever loops) not needed for randomness
- **Fix**: Remove T07.G3.03, keep T20.G3.04 and T09.G3.02

#### T20.G3.05.01 - Use variables to change pattern size
- **Issue Type**: Accurate, good addition
- **Priority**: N/A

### Grade 4 Issues

#### T20.G4.01 - Implement incremental loops for spirals (Technical)
- **Issue Type**: Excessive dependencies from old version
- **Priority**: MEDIUM
- **Current Dependencies**: T07.G3.01, T07.G3.05, T09.G3.01.04, T20.G3.05.01
- **Problems**:
  1. Has weird dependencies to T20.GK.03, T20.GK.04 from old version
  2. Good technical/creative split
  3. Dependencies should be cleaner
- **Fix**: Keep current dependencies, remove any K-level dependencies

#### T20.G4.01b - Design spiral art for visual effect (Creative)
- **Issue Type**: Missing from allskills.md
- **Priority**: HIGH
- **Problem**: Listed in skills_T20 but not in allskills.md
- **Fix**: Add to allskills.md or remove from skills_T20

#### T20.G4.02 - Implement tessellation with custom blocks (Technical)
- **Issue Type**: Missing T11.G4.01 dependency + excessive old deps
- **Priority**: HIGH
- **Current Dependencies**: T07.G3.01, T07.G3.05, T11.G4.01, T20.G3.05
- **Problems**:
  1. Good technical focus
  2. Has weird dependency to T28.G3.04 (randomness in games) in old version
- **Fix**: Clean dependencies, ensure T11.G4.01 is included

#### T20.G4.02b - Design tessellation patterns (Creative)
- **Issue Type**: Missing from allskills.md
- **Priority**: HIGH
- **Problem**: Listed in skills_T20 but not in allskills.md
- **Fix**: Add to allskills.md or remove from skills_T20

#### T20.G4.03 - Control art with parameters
- **Issue Type**: Excessive dependencies
- **Priority**: MEDIUM
- **Current Dependencies**: T07.G3.05, T09.G3.01.04, T20.G4.01, T09.G3.02
- **Problems**:
  1. T09.G3.02 (variables in conditionals) not needed for basic parameters
  2. Too many dependencies for a straightforward skill
- **Fix**: Reduce to T09.G3.01.04, T20.G4.01

#### T20.G4.04 - Debug a multi-loop art script
- **Issue Type**: Accurate, good skill
- **Priority**: N/A

#### T20.G4.05 - Recolor art with simple input events
- **Issue Type**: Missing event handling dependency
- **Priority**: MEDIUM
- **Current Dependencies**: T06.G3.01, T07.G3.05, T08.G3.01, T20.G3.05
- **Problem**: Needs dependency on event handling skill (T12 or T13)
- **Fix**: Add event handling dependency

#### T20.G4.05.01 - Map list values to drawing positions
- **Issue Type**: Accurate, good addition
- **Priority**: N/A

### Grade 5 Issues

#### T20.G5.01 - Implement simple data-driven visualization (Technical)
- **Issue Type**: Too broad - covers ALL types of data viz
- **Priority**: HIGH
- **Current Dependencies**: T07.G3.05, T10.G4.01, T10.G4.02, T20.G4.05.01
- **Problems**:
  1. Says "bar charts OR scatter plots" - should be split
  2. One skill trying to cover multiple visualization types
  3. Each viz type is a distinct skill
- **Fix**: Break into sub-skills:
  - T20.G5.01.01: Create bar charts from list data
  - T20.G5.01.02: Create scatter plots from list data
  - T20.G5.01.03: Create line graphs from list data

#### T20.G5.01b - Design data visualizations (Creative)
- **Issue Type**: Missing from allskills.md
- **Priority**: HIGH
- **Problem**: Listed in skills_T20 but not in allskills.md
- **Fix**: Add to allskills.md or remove from skills_T20

#### T20.G5.01.01 - Map data to two visual properties
- **Issue Type**: Good skill but numbering confusion
- **Priority**: MEDIUM
- **Problem**: This should be after breaking down G5.01 into viz types
- **Fix**: Renumber after G5.01 breakdown

#### T20.G5.02 - Animate a pattern with a counter variable
- **Issue Type**: Accurate, good skill
- **Priority**: N/A

#### T20.G5.03 - Make art respond to mouse or keys
- **Issue Type**: Missing event handling dependency
- **Priority**: MEDIUM
- **Current Dependencies**: T07.G3.05, T20.G4.05
- **Problem**: Needs event handling skills from T12/T13
- **Fix**: Add event handling dependencies

#### T20.G5.04 - Create fractal-like nested patterns
- **Issue Type**: Accurate, good skill
- **Priority**: N/A

#### T20.G5.04.00 - Initialize 3D scenes and add basic shapes
- **Issue Type**: Too broad - covers initialization AND multiple shapes
- **Priority**: HIGH
- **Current Dependencies**: T20.G4.01, T20.G5.02
- **Problems**:
  1. Combines scene initialization with shape creation
  2. "Basic 3D primitives (box, sphere, cylinder)" - each shape has many parameters
  3. Following T18 pattern, each shape type should be separate skill
- **Fix**: Break into:
  - T20.G5.04.00: Initialize 3D scene and understand coordinates
  - T20.G5.04.01: Add boxes to 3D scenes
  - T20.G5.04.02: Add spheres to 3D scenes
  - T20.G5.04.03: Add cylinders to 3D scenes

#### T20.G5.04.01 - Create simple 3D artistic patterns
- **Issue Type**: Should come after individual shape skills
- **Priority**: MEDIUM
- **Problem**: Tries to create patterns before learning individual shapes
- **Fix**: Renumber to come after shape intro skills

#### T20.G5.05 - Explain data-to-visual design choices
- **Issue Type**: Accurate reflection skill
- **Priority**: N/A

### Grade 6 Issues

#### T20.G6.01 - Trace and explain an art algorithm
- **Issue Type**: Accurate, good skill
- **Priority**: N/A

#### T20.G6.02 - Refactor repetitive art into loops/custom blocks
- **Issue Type**: Accurate, good skill
- **Priority**: N/A

#### T20.G6.03 - Use variables and conditionals to branch designs
- **Issue Type**: Accurate, good skill
- **Priority**: N/A

#### T20.G6.04 - Implement multi-field data visualization (Technical)
- **Issue Type**: Too broad - multiple viz types again
- **Priority**: HIGH
- **Current Dependencies**: T07.G5.01, T08.G5.01, T10.G5.01, T20.G5.01
- **Problems**:
  1. Assumes G5.01 covered basics, but G5.01 itself is too broad
  2. Should build on specific viz types from G5
  3. "2-3 data attributes" is good scope
- **Fix**: Make more specific about building on G5 bar/scatter/line skills

#### T20.G6.04b - Design artistic data visualizations (Creative)
- **Issue Type**: Missing from allskills.md
- **Priority**: HIGH
- **Problem**: Listed in skills_T20 but not in allskills.md
- **Fix**: Add to allskills.md or remove from skills_T20

#### T20.G6.05 - Apply math transformations to art
- **Issue Type**: Missing math prerequisite
- **Priority**: MEDIUM
- **Current Dependencies**: T07.G5.01, T09.G5.01, T20.G5.04
- **Problem**: Uses sine/cosine but no math skill dependency
- **Fix**: Add trigonometry skill dependency if exists in T03 or T04

#### T20.G6.05.01 - Apply materials and textures to 3D art
- **Issue Type**: Missing 3D shape prerequisites
- **Priority**: HIGH
- **Current Dependencies**: T20.G5.04.01, T20.G6.05
- **Problems**:
  1. T20.G5.04.01 may not exist in final numbering after breakdown
  2. Needs dependencies on actual 3D shape creation
  3. Should depend on T18 3D material skills
- **Fix**: Add T18 material dependencies, update shape dependencies

#### T20.G6.05.02 - Create 3D curve and line art
- **Issue Type**: Too advanced too soon + missing prerequisites
- **Priority**: HIGH
- **Current Dependencies**: T20.G5.04.01, T20.G6.05
- **Problems**:
  1. "Point lists using loops and math formulas" - very advanced
  2. Missing prerequisite on basic 3D lines
  3. Should depend on T18 3D line blocks
  4. Parametric equations in 3D is Grade 7-8 level
- **Fix**:
  - Add prerequisite skill for basic 3D lines
  - Possibly move to G7
  - Add T18 dependencies

#### T20.G6.05.03 - Create interactive 3D generative art
- **Issue Type**: Accurate, good combination skill
- **Priority**: N/A

### Grade 7 Issues

#### T20.G7.01 - Compare efficiency of art algorithms
- **Issue Type**: Accurate, good skill
- **Priority**: N/A

#### T20.G7.02 - Use while/repeat-until loops in art
- **Issue Type**: Accurate, good skill
- **Priority**: N/A

#### T20.G7.03 - Study parameter impact on aesthetics
- **Issue Type**: Accurate, excellent skill
- **Priority**: N/A

#### T20.G7.04 - Analyze real generative artworks
- **Issue Type**: Accurate, good skill
- **Priority**: N/A

#### T20.G7.04.00 - Understand particle system basics
- **Issue Type**: Missing T18 particle dependency
- **Priority**: HIGH
- **Current Dependencies**: T20.G6.03, T20.G7.03
- **Problem**: CreatiCode has particle blocks in T18 - should depend on those
- **Fix**: Add T18 particle introduction dependency

#### T20.G7.04.01 - Create particle-based generative art
- **Issue Type**: Accurate, builds on .00
- **Priority**: N/A

#### T20.G7.05 - Implement rule-based iterative art systems
- **Issue Type**: Very advanced, appropriate for G7
- **Priority**: N/A

#### T20.G7.05.01 - Create 3D generative sculptures with particle effects
- **Issue Type**: Missing multiple prerequisites
- **Priority**: HIGH
- **Current Dependencies**: T20.G5.04.01, T20.G6.05, T20.G7.03, T20.G7.04.01
- **Problems**:
  1. Combines 3D shapes + math + particles - very complex
  2. Missing T18 3D object dependencies
  3. T20.G5.04.01 numbering will change
- **Fix**: Add T18 dependencies, update T20 dependencies after renumbering

#### T20.G7.05.02 - Use lighting to enhance 3D algorithmic art
- **Issue Type**: Missing T18 lighting dependency
- **Priority**: HIGH
- **Current Dependencies**: T20.G5.04.01, T20.G7.05.01
- **Problem**: CreatiCode has lighting blocks in T18 - must depend on those
- **Fix**: Add T18 lighting skills as dependencies

#### T20.G7.05.03 - Generate custom 3D shapes from calculated vertices
- **Issue Type**: Very advanced, good skill
- **Priority**: N/A
- **Note**: Excellent advanced skill, uses list of calculated vertices

### Grade 8 Issues

#### T20.G8.01 - Implement multi-dimensional data mapping (Technical)
- **Issue Type**: Excessive dependencies but accurate scope
- **Priority**: MEDIUM
- **Current Dependencies**: T06.G6.01, T07.G6.01, T08.G6.01, T10.G7.01, T20.G6.04, T20.G7.01
- **Problem**: 6 dependencies is a lot but all are relevant
- **Fix**: Consider if all are truly necessary

#### T20.G8.01b - Design multi-variable data stories (Creative)
- **Issue Type**: Missing from allskills.md
- **Priority**: HIGH
- **Problem**: Listed in skills_T20 but not in allskills.md
- **Fix**: Add to allskills.md or remove from skills_T20

#### T20.G8.02 - Create constrained generative artwork
- **Issue Type**: Accurate, excellent advanced skill
- **Priority**: N/A

#### T20.G8.03 - Evaluate authorship and originality in generative art
- **Issue Type**: Accurate, excellent ethics skill
- **Priority**: N/A

#### T20.G8.04 - Optimize rendering for performance
- **Issue Type**: Accurate, good performance skill
- **Priority**: N/A

#### T20.G8.05 - Combine multiple algorithms in art pipeline
- **Issue Type**: Accurate capstone skill
- **Priority**: N/A

#### T20.G8.05.01 - Apply post-processing effects to generative art
- **Issue Type**: Missing T18 post-processing dependency
- **Priority**: HIGH
- **Current Dependencies**: T20.G7.05.01, T20.G8.04
- **Problem**: CreatiCode has post-processing blocks in T18 - must depend on those
- **Fix**: Add T18 post-processing dependencies

---

## SECTION B: PROPOSED BREAKDOWN

### B1: T20.G3.02 - Program a repeating border with loops
**Reason for breakdown**: Original skill jumps too quickly from blocks intro to looped patterns

**Original Skill**:
- ID: T20.G3.02
- Description: Students write a simple drawing program that repeats a sequence (draw oval, move right) using a `repeat` block

**Proposed Sub-Skills**:

#### T20.G3.02.01 - Draw a single shape at a position
- **Description**: Students use CreatiCode's draw blocks to create a single shape at a specific x,y position. They practice using `draw rectangle at x (_) y (_) width (_) height (_) fill [color]` or `draw oval at x (_) y (_) width (_) height (_) fill [color]` to place one shape on the stage.
- **Dependencies**: T20.G3.01, T06.G3.01
- **Rationale**: Before looping, students need to master drawing single shapes

#### T20.G3.02 - Program a repeating border with loops (REVISED)
- **Description**: Students use a loop to draw multiple shapes in a row by combining `repeat (_)` with draw blocks and motion. Each iteration moves the sprite to a new position and draws another shape, creating a border pattern.
- **Dependencies**: T20.G3.02.01, T07.G3.01
- **Rationale**: Now builds on single-shape skill

### B2: T20.G5.01 - Data-driven visualization
**Reason for breakdown**: One skill covering bar charts, scatter plots, AND line graphs is too broad

**Original Skill**:
- ID: T20.G5.01
- Description: Students read values from a single list and map to visual properties using draw blocks for bar charts OR scatter plots

**Proposed Sub-Skills**:

#### T20.G5.01.01 - Create bar charts from list data
- **Description**: Students create vertical bar charts by iterating through a list of numbers and drawing rectangles with heights corresponding to each value. They use `for [i] from (1) to (length of [data])` and `draw rectangle at x (_) y (0) width (40) height (item (i) of [data])`, positioning bars horizontally across the stage.
- **Dependencies**: T07.G3.05, T10.G4.02, T20.G4.05.01
- **Rationale**: Bar charts are the most straightforward data visualization

#### T20.G5.01.02 - Create scatter plots from list data
- **Description**: Students create scatter plots by reading x and y coordinates from parallel lists (or nested list) and drawing small circles at each position using `draw oval at x (item (i) of [x-data]) y (item (i) of [y-data]) width (10) height (10)`.
- **Dependencies**: T20.G5.01.01, T10.G5.01
- **Rationale**: Requires understanding of 2D coordinates and parallel data

#### T20.G5.01.03 - Create line graphs from list data
- **Description**: Students create line graphs by connecting data points with lines. They iterate through a list, drawing lines between consecutive points using `draw line from x (prev-x) y (prev-y) to x (curr-x) y (curr-y)`, storing previous positions in variables.
- **Dependencies**: T20.G5.01.01, T09.G5.01
- **Rationale**: Requires tracking previous values, more complex than bar or scatter

#### T20.G5.01.04 - Map data to two visual properties (RENUMBERED)
- **Description**: Students extend single-list visualization by using data to control TWO visual properties simultaneously (e.g., list values control both height and color of rectangles, or both x-position and size of circles). They use parallel lists or calculate secondary properties from primary data.
- **Dependencies**: T20.G5.01.01, T10.G5.01
- **Rationale**: Builds on basic bar charts, adds color/size dimensions

### B3: T20.G5.04.00 - Initialize 3D scenes and add basic shapes
**Reason for breakdown**: Following T18 pattern where each shape type is a separate skill due to many parameters

**Original Skill**:
- ID: T20.G5.04.00
- Description: Initialize 3D scene and add basic primitives (box, sphere, cylinder)

**Proposed Sub-Skills**:

#### T20.G5.04.00 - Initialize 3D scene and understand 3D coordinates
- **Description**: Students initialize a 3D scene using `initialize 3D scene` and learn the 3D coordinate system (x: left-right, y: up-down, z: forward-back). They practice understanding depth and positioning in 3D space without creating objects yet.
- **Dependencies**: T20.G4.01, T20.G5.02, T18.G3.01
- **Rationale**: Scene initialization is complex enough to be its own skill

#### T20.G5.04.01 - Add boxes to 3D scenes for algorithmic art
- **Description**: Students learn the `add box [color] size in x (_) y (_) z (_) edge radius (_) as [name]` block and understand all parameters: x/y/z dimensions for proportions, edge radius for rounded corners. They create simple box patterns using loops.
- **Dependencies**: T20.G5.04.00
- **Rationale**: Box is the simplest 3D primitive with 4 main parameters

#### T20.G5.04.02 - Add spheres to 3D scenes for algorithmic art
- **Description**: Students learn the `add sphere [color] size in x (_) y (_) z (_) arc (_) slice (_) sides (_) as [name]` block. They understand how x/y/z create ellipsoids, how arc and slice create partial spheres, and how sides affects smoothness. They create sphere patterns.
- **Dependencies**: T20.G5.04.01
- **Rationale**: Sphere has 6 parameters including arc/slice that are conceptually different from box

#### T20.G5.04.03 - Add cylinders to 3D scenes for algorithmic art
- **Description**: Students learn the `add cylinder [color] diameter top (_) bottom (_) height (_) arc (_) closed section [yes/no] cap type [type] sides (_) as [name]` block. They understand how different top/bottom diameters create cones, how arc creates partial cylinders, and cap options. They create column and cone patterns.
- **Dependencies**: T20.G5.04.02
- **Rationale**: Cylinder has 8 parameters and can create cones, very versatile

#### T20.G5.04.04 - Create 3D artistic patterns with multiple shapes (RENUMBERED from G5.04.01)
- **Description**: Students combine boxes, spheres, and cylinders in loops to create artistic 3D patterns. They use nested loops for 3D grids and apply transformations to arrange objects in space.
- **Dependencies**: T20.G5.04.03
- **Rationale**: Now builds on individual shape mastery

### B4: T20.G6.05.02 - 3D curve and line art
**Reason for breakdown**: Skill jumps from no 3D lines to parametric equations in 3D

**Original Skill**:
- ID: T20.G6.05.02
- Description: Create 3D curves using point lists with parametric equations

**Proposed Sub-Skills**:

#### T20.G6.05.02.00 - Create basic 3D lines
- **Description**: Students use `add line [color] diameter (_) xyz from (x1) (y1) (z1) to (x2) (y2) (z2) as [name]` to create single 3D lines. They practice connecting specific points in 3D space and understand how lines work in three dimensions.
- **Dependencies**: T20.G5.04.04, T18.G4.XX (3D line block intro)
- **Rationale**: Must learn basic 3D lines before calculating curves

#### T20.G6.05.02 - Create 3D curves from calculated point lists (REVISED)
- **Description**: Students create algorithmic 3D art by generating point lists using loops and math formulas, then using these lists with `add curve [color] using list [list] as [name]`. They create simple spirals using sine/cosine with z-coordinates, understanding how 2D curves extend to 3D space.
- **Dependencies**: T20.G6.05.02.00, T20.G6.05, T10.G5.01
- **Rationale**: Builds on basic 3D lines, adds calculation aspect

---

## SECTION C: PROPOSED NEW SKILLS

### C1: Missing foundational 2D skills

#### T20.G3.01.01 - Identify drawing blocks vs pen blocks
- **Description**: Students explore CreatiCode's drawing tools and learn that draw blocks (draw rectangle, draw oval, draw line) are in the Looks category, not Pen category. They understand that CreatiCode uses position-based drawing rather than pen-up/pen-down continuous drawing like Scratch.
- **Grade**: 3
- **Dependencies**: T06.G3.01
- **Rationale**: Critical conceptual difference from Scratch that students must understand
- **Placement**: Before T20.G3.01

#### T20.G4.01.01 - Use dynamic color generation for art
- **Description**: Students use the `color (C) saturation (S) brightness (B) transparency (T)` reporter block to generate colors programmatically. They create gradients by changing values in loops and understand HSBT color model for algorithmic art.
- **Grade**: 4
- **Dependencies**: T20.G3.05, T09.G3.01
- **Rationale**: Color is fundamental to artistic expression but currently not explicitly taught
- **Placement**: After T20.G3.05, before or alongside T20.G4.01

### C2: Missing curve and bezier skills

#### T20.G5.05.01 - Draw bezier curves for organic designs
- **Description**: Students learn the `draw curve in [color] from x (_) y (_) to x (_) y (_) control 1 x (_) y (_) control 2 x (_) y (_) thickness (_)` block. They experiment with control points to create smooth, flowing curves and understand how changing control points affects curve shape.
- **Grade**: 5
- **Dependencies**: T20.G4.03, T09.G4.01
- **Rationale**: CreatiCode has bezier curve blocks that aren't covered anywhere
- **Placement**: After T20.G5.04, before T20.G6.01

### C3: Missing 3D material basics

#### T20.G6.05.00 - Apply basic colors to 3D objects
- **Description**: Students use `update color diffusion [color]` to change colors of 3D objects they've created. They understand how diffusion color works in 3D and practice recoloring objects in loops to create colorful 3D patterns.
- **Grade**: 6
- **Dependencies**: T20.G5.04.04, T18.G4.XX (3D material intro)
- **Rationale**: Must learn basic 3D coloring before materials/textures
- **Placement**: Before T20.G6.05.01

### C4: Missing particle prerequisites

#### T20.G7.04.00.01 - Create stationary particle emitters
- **Description**: Students create simple particle emitters that stay in one place using `add particle emitter` and configure basic properties like color, size, and lifetime. They observe how particles are generated over time and understand emitter vs particle concepts.
- **Grade**: 7
- **Dependencies**: T20.G7.04.00, T18.G6.XX (particle intro)
- **Rationale**: Before generative particle art, need basic emitter creation
- **Placement**: Between T20.G7.04.00 and T20.G7.04.01

### C5: Missing data visualization design skills

#### T20.G5.05.02 - Choose appropriate visualization types for data
- **Description**: Students analyze different datasets and decide whether bar charts, scatter plots, or line graphs best communicate the data story. They justify their choices based on data characteristics (categorical vs continuous, single vs paired values, trends over time).
- **Grade**: 5
- **Dependencies**: T20.G5.01.03
- **Rationale**: Critical thinking skill missing from current progression
- **Placement**: After all three viz types taught

### C6: Missing 3D camera skills for art

#### T20.G7.05.00 - Position cameras to showcase 3D art
- **Description**: Students use camera blocks to position viewpoints that best showcase their 3D generative sculptures. They set camera distance, angles, and targets to create compelling views of their algorithmic art.
- **Grade**: 7
- **Dependencies**: T20.G7.05.01, T18.G3.XX (camera intro)
- **Rationale**: 3D art needs good camera positioning to be appreciated
- **Placement**: After creating 3D sculptures

### C7: Missing post-processing intro

#### T20.G8.05.00 - Understand post-processing effects
- **Description**: Students learn what post-processing effects are (bloom, glow, blur, vignette) and how they layer on top of rendered scenes. They experiment with enabling/disabling effects to see their impact on algorithmic art.
- **Grade**: 8
- **Dependencies**: T20.G7.05.02, T18.G6.XX (post-processing intro)
- **Rationale**: Must understand effects before applying to generative art
- **Placement**: Before T20.G8.05.01

### C8: Missing text art skill

#### T20.G4.04.01 - Create text-based generative art
- **Description**: Students use `draw text [text] at x (_) y (_) size (_) color (_) rotation (_)` to create artistic compositions with words. They generate text patterns by varying position, size, rotation, and color in loops, creating word spirals, typography grids, and rotated text art.
- **Grade**: 4
- **Dependencies**: T20.G4.01, T09.G3.01
- **Rationale**: CreatiCode has text drawing blocks not currently used
- **Placement**: After spirals, before G5

### C9: Missing polygon drawing skill

#### T20.G5.02.01 - Draw polygons using loops and turns
- **Description**: Students create regular polygons (triangles, squares, pentagons, hexagons) by using loops that combine drawing and turning. They calculate the turn angle (360/sides) and use `repeat (sides)` with `draw line` and sprite rotation to form closed shapes.
- **Grade**: 5
- **Dependencies**: T20.G4.01, T07.G4.01
- **Rationale**: Classic algorithmic art skill missing from progression
- **Placement**: After spirals, before fractals

### C10: Missing mandala/radial pattern skill

#### T20.G5.03.01 - Create radial patterns and mandalas
- **Description**: Students create symmetrical radial patterns by looping through angles (0 to 360), pointing in each direction, moving outward, and drawing shapes. They use `for [angle] from (0) to (360) at step (step-size)` to create flower petals, starbursts, and mandala designs.
- **Grade**: 5
- **Dependencies**: T20.G5.02.01, T20.G4.01
- **Rationale**: Important algorithmic art pattern type not explicitly taught
- **Placement**: After polygons

### C11: Missing 3D transformation skill

#### T20.G6.05.04 - Apply rotations and scaling to 3D patterns
- **Description**: Students use `rotate to angle (_) around [axis]` and `update scale x (_)% y (_)% z (_)%` to transform 3D objects in loops. They create patterns where objects progressively rotate or scale, understanding how transformations affect 3D compositions.
- **Grade**: 6
- **Dependencies**: T20.G5.04.04, T18.G4.XX (3D transforms)
- **Rationale**: 3D transformations essential for sophisticated 3D art
- **Placement**: After basic 3D shapes

### C12: Missing layering/composition skill

#### T20.G6.02.01 - Layer multiple algorithmic patterns
- **Description**: Students create compositions by layering multiple algorithmic patterns on top of each other. They use `clear all drawings` strategically and understand drawing order to create backgrounds, midgrounds, and foregrounds in their generative art.
- **Grade**: 6
- **Dependencies**: T20.G5.04, T20.G6.01
- **Rationale**: Composition skill missing from artistic development
- **Placement**: After refactoring

### C13: Missing conditional art skill

#### T20.G6.03.01 - Use modulo for alternating patterns
- **Description**: Students use the modulo operator `(i) mod (n)` in conditionals to create alternating patterns (every other, every third, etc.). They create checkerboard patterns, striped designs, and rhythmic variations by checking if `(i) mod (2) = 0`.
- **Grade**: 6
- **Dependencies**: T20.G6.03, T08.G5.01
- **Rationale**: Key technique for pattern variation
- **Placement**: With conditional branching

### C14: Missing efficiency/optimization intro

#### T20.G7.01.01 - Reduce redundant calculations in art code
- **Description**: Students identify repeated calculations in loops (like `(360 / sides)`) and extract them to variables set before the loop. They compare execution time and understand how reducing calculations improves performance in generative art.
- **Grade**: 7
- **Dependencies**: T20.G7.01, T09.G6.01
- **Rationale**: Practical optimization technique
- **Placement**: After efficiency comparison

### C15: Missing noise/randomness with constraints

#### T20.G7.02.01 - Use random walks with boundaries
- **Description**: Students create random walk patterns that stay within boundaries by using `repeat until` loops with edge detection. They generate organic, wandering lines that explore space without leaving the canvas.
- **Grade**: 7
- **Dependencies**: T20.G7.02, T20.G3.05
- **Rationale**: Advanced randomness technique
- **Placement**: After conditional loops

---

## SECTION D: DEPENDENCY FIXES

### D1: Remove Cross-Topic Violations

#### T20.G3.02 dependencies
- **Current**: T20.G3.01, T08.G3.01, T18.G3.02
- **Issue**: T08.G3.01 (conditionals) not needed for simple loops; T18.G3.02 (3D camera) irrelevant
- **Proposed**: T20.G3.02.01
- **Reason**: Simplified to focus on looping mechanics

#### T20.G3.03 dependencies
- **Current**: T20.G3.02, T09.G3.01, T07.G3.02, T18.G3.03
- **Issue**: T18.G3.03 (3D lighting) irrelevant to 2D grids; T07.G3.02 (trace) shouldn't be prereq for doing
- **Proposed**: T20.G3.02, T07.G3.01
- **Reason**: Simplified to essential prerequisites

#### T20.G3.04 dependencies
- **Current**: T20.G3.03, T08.G3.02, T18.G3.04
- **Issue**: Should trace BEFORE doing nested loops; 3D shapes irrelevant; conditionals not needed
- **Proposed**: T20.G3.02, T07.G3.02
- **Reason**: Trace simple loops before doing complex ones

#### T20.G3.05 dependencies
- **Current**: T20.G3.04, T09.G3.02, T07.G3.03
- **Issue**: T07.G3.03 (forever loops) not needed for randomness
- **Proposed**: T20.G3.04, T09.G3.02
- **Reason**: Remove unnecessary forever loop dependency

### D2: Fix Intra-Topic Ordering

#### Reorder G3 skills
- **Current Order**: G3.01 → G3.02 → G3.03 (grid) → G3.04 (trace) → G3.05
- **Issue**: Should trace before doing nested loops
- **Proposed Order**: G3.01 → G3.02.01 → G3.02 → G3.04 (trace moved) → G3.03 (grid) → G3.05
- **Reason**: Logical progression: single shape → loop → trace → nested loop → randomness

#### T20.G2.02 dependencies
- **Current**: T05.G1.01, T01.G1.04
- **Issue**: T05.G1.01 (story character needs) irrelevant to symmetry
- **Proposed**: T01.G1.04
- **Reason**: Only sequencing needed for mirror planning

### D3: Add Missing Prerequisites

#### T20.G3.01 dependencies
- **Current**: T07.G3.01, T20.G2.01
- **Issue**: Missing basic scripting
- **Proposed**: T06.G3.01, T07.G3.01, T20.G2.01
- **Reason**: Need green flag scripts before loops

#### T20.G4.05 dependencies
- **Current**: T06.G3.01, T07.G3.05, T08.G3.01, T20.G3.05
- **Issue**: Missing event handling
- **Proposed**: Add T12.G3.XX or T13.G3.XX (event handling)
- **Reason**: Recoloring triggered by events

#### T20.G5.03 dependencies
- **Current**: T07.G3.05, T20.G4.05
- **Issue**: Missing event handling
- **Proposed**: Add T12.G4.XX or T13.G4.XX (mouse/key events)
- **Reason**: Interactivity requires event handling

#### T20.G6.05.01 dependencies
- **Current**: T20.G5.04.01, T20.G6.05
- **Issue**: Missing T18 material skills
- **Proposed**: Add T18.G5.XX (materials intro), update T20.G5.04.01 to new numbering
- **Reason**: Must learn 3D materials from T18 first

#### T20.G6.05.02.00 dependencies (new skill)
- **Proposed**: T20.G5.04.04, T18.G4.XX (3D lines)
- **Reason**: Need T18 3D line block introduction

#### T20.G7.04.00 dependencies
- **Current**: T20.G6.03, T20.G7.03
- **Issue**: Missing T18 particle intro
- **Proposed**: Add T18.G6.XX (particle basics), keep current deps
- **Reason**: Particles are T18 feature

#### T20.G7.05.01 dependencies
- **Current**: T20.G5.04.01, T20.G6.05, T20.G7.03, T20.G7.04.01
- **Issue**: Missing T18 3D object dependencies; T20.G5.04.01 will renumber
- **Proposed**: Add T18.G5.XX (advanced 3D objects), update to T20.G5.04.04
- **Reason**: Complex 3D requires T18 foundation

#### T20.G7.05.02 dependencies
- **Current**: T20.G5.04.01, T20.G7.05.01
- **Issue**: Missing T18 lighting skills
- **Proposed**: Add T18.G5.XX (lighting blocks), update to T20.G5.04.04
- **Reason**: Lighting is T18 feature

#### T20.G8.05.01 dependencies
- **Current**: T20.G7.05.01, T20.G8.04
- **Issue**: Missing T18 post-processing
- **Proposed**: Add T18.G7.XX (post-processing), keep current deps
- **Reason**: Post-processing is T18 feature

### D4: Apply X-2 Rule Violations

#### T20.G4.01 dependencies
- **Current**: T07.G3.01 (G3), T07.G3.05 (G3), T09.G3.01.04 (G3), T20.G3.05.01 (G3)
- **Analysis**: All G3 dependencies for G4 skill - VALID (X-1 rule)
- **Action**: No change needed

#### T20.G6.01 dependencies
- **Current**: T07.G5.01 (G5), T09.G5.01 (G5), T20.G5.04 (G5)
- **Analysis**: All G5 dependencies for G6 skill - VALID (X-1 rule)
- **Action**: No change needed

#### T20.G8.01 dependencies
- **Current**: T06.G6.01 (G6), T07.G6.01 (G6), T08.G6.01 (G6), T10.G7.01 (G7), T20.G6.04 (G6), T20.G7.01 (G7)
- **Analysis**: Mix of G6 and G7 for G8 skill - VALID (X-2 and X-1)
- **Action**: No change needed, but many dependencies

### D5: Remove Circular/Self Dependencies

**Analysis**: No circular dependencies found in T20. All dependencies flow forward chronologically.

---

## SECTION E: DESCRIPTION IMPROVEMENTS

### E1: Grade 3 Description Updates

#### T20.G3.02 (REVISED after breakdown)
- **Old**: "Students write a simple pen program that repeats a sequence (stamp star, move right) using a repeat block."
- **New**: "Students use a loop to draw multiple shapes in a row by combining `repeat (_)` with draw blocks and motion. Each iteration moves the sprite to a new position and draws another shape, creating a border pattern."
- **Reason**:
  - Removes "pen program" (inaccurate)
  - Removes "stamp" (doesn't exist in CreatiCode)
  - Specifies draw blocks as the tool
  - More accurate to CreatiCode capabilities

#### T20.G3.04 (REVISED)
- **Old**: "Students read a short script (loop drawing squares) and predict how many shapes or what final layout appears."
- **New**: "Students read a short script using draw blocks in a loop (e.g., loop drawing rectangles with position changes) and predict how many shapes appear and what final layout forms. This tracing skill builds understanding before tackling nested loops."
- **Reason**:
  - Specifies draw blocks
  - Clarifies the purpose (trace before do)
  - More explicit about what students predict

### E2: Grade 4 Description Updates

#### T20.G4.01 (REVISED)
- **Old**: "Students write a loop that increases a variable (distance or angle) each iteration to create mathematical spiral patterns."
- **New**: "Students write a loop that increases a variable (distance or angle) each iteration to create mathematical spiral patterns using positioning (go to x/y) and draw blocks (draw oval, draw rectangle). They focus on the technical implementation of incremental variables and loop mechanics to calculate positions."
- **Reason**:
  - Specifies exact blocks used
  - Clarifies technical focus
  - More implementable

#### T20.G4.02 (REVISED)
- **Old**: "Students create a custom block (introduced in T11.G4.01) that draws a geometric tile pattern, then use nested loops to repeat it across the stage."
- **New**: "Students create a custom block that draws a geometric tile pattern using draw blocks (draw rectangle, draw oval), then use nested loops to repeat it across the stage. They focus on modular code structure and coordinate calculations."
- **Reason**:
  - Specifies draw blocks
  - Emphasizes modularity and math
  - More explicit about what tile drawing involves

### E3: Grade 5 Description Updates

#### T20.G5.01.01 (NEW) - Create bar charts
- **Description**: "Students create vertical bar charts by iterating through a list of numbers and drawing rectangles with heights corresponding to each value. They use `for [i] from (1) to (length of [data])` and `draw rectangle at x (_) y (0) width (40) height (item (i) of [data])`, positioning bars horizontally across the stage."
- **Reason**: Specific, actionable, includes exact blocks and pattern

#### T20.G5.01.02 (NEW) - Create scatter plots
- **Description**: "Students create scatter plots by reading x and y coordinates from parallel lists (or nested list) and drawing small circles at each position using `draw oval at x (item (i) of [x-data]) y (item (i) of [y-data]) width (10) height (10)`."
- **Reason**: Specific to scatter plot technique, exact blocks

#### T20.G5.01.03 (NEW) - Create line graphs
- **Description**: "Students create line graphs by connecting data points with lines. They iterate through a list, drawing lines between consecutive points using `draw line from x (prev-x) y (prev-y) to x (curr-x) y (curr-y)`, storing previous positions in variables."
- **Reason**: Addresses the complexity of line graphs (tracking previous)

#### T20.G5.04.01 (REVISED - was G5.04.00)
- **Old**: "Students learn to initialize a 3D scene, understand the coordinate system, and add basic 3D primitives (box, sphere, cylinder)."
- **New**: "Students learn the `add box [color] size in x (_) y (_) z (_) edge radius (_) as [name]` block and understand all parameters: x/y/z dimensions for proportions, edge radius for rounded corners. They create simple box patterns using loops."
- **Reason**: Focuses on just boxes after scene init separated out

### E4: Grade 6 Description Updates

#### T20.G6.04 (REVISED)
- **Old**: "Students implement algorithms to process structured data (nested lists or multiple parallel lists) and map different data fields to distinct visual properties using draw blocks."
- **New**: "Students implement algorithms to process structured data (nested lists or multiple parallel lists representing objects with multiple attributes) and map different data fields to distinct visual properties using draw blocks. For example, they draw rectangles where x-position comes from one list, height from another, and color is determined by a third field value. They use iteration and conditional logic to process 2-3 data attributes."
- **Reason**: Much more specific about what "multi-field" means, concrete example

#### T20.G6.05.02 (REVISED after breakdown)
- **Old**: "Students create algorithmic art using 3D lines and curves in space by generating point lists using loops and math formulas."
- **New**: "Students create algorithmic 3D art by generating point lists using loops and math formulas, then using these lists with `add curve [color] using list [list] as [name]`. They create simple spirals using sine/cosine with z-coordinates, understanding how 2D curves extend to 3D space."
- **Reason**: More explicit about the process and blocks used

### E5: Grade 7 Description Updates

#### T20.G7.03 (ALREADY GOOD)
- **Current**: "Students create a parameterized art piece with exposed controls (sliders or variables for randomness, angle change, speed). They systematically adjust each parameter one at a time and document in a table how each change affects specific aesthetic qualities (symmetry, balance, density, motion). They analyze which parameters have the strongest visual impact."
- **Reason**: Excellent specificity, actionable, clear assessment

#### T20.G7.04 (REVISED)
- **Old**: "Students examine professional algorithmic art or natural patterns and infer what loops, math, or randomness likely generated them."
- **New**: "Students examine professional algorithmic art or natural patterns and write pseudocode or create simplified CreatiCode implementations showing the loops, math formulas, and randomness that likely generated them. They explain their reasoning for each choice."
- **Reason**: More concrete deliverable (pseudocode/implementation vs "infer")

### E6: Grade 8 Description Updates

#### T20.G8.01 (REVISED)
- **Old**: "Students implement sophisticated algorithms to map multiple data attributes simultaneously to different visual channels."
- **New**: "Students implement sophisticated algorithms to process complex datasets with 4+ attributes and map them to multiple visual channels simultaneously (size, color, motion, position, rotation, opacity). They use advanced programming techniques including custom scaling functions, normalization algorithms, and optimization strategies for handling larger datasets. This goes beyond G6.04 by handling more dimensions, using mathematical transformations, and considering performance."
- **Reason**: Much more specific about scale (4+ attributes), techniques used, and how it differs from G6

#### T20.G8.02 (ALREADY GOOD)
- **Current**: "Students combine randomness with constraints implemented as conditionals and boundary checks (limited color palettes, symmetry rules enforced by mirroring, bounding boxes checked with if statements) so output is unique yet cohesive."
- **Reason**: Excellent specificity about constraint implementation

#### T20.G8.03 (ALREADY GOOD)
- **Current**: "Students write a position paper or participate in structured discussion analyzing authorship questions in algorithmic art (who is the artist—coder, algorithm, or user?), evaluate originality when code produces unique outputs, and discuss ethical considerations like attribution and intellectual property. They defend their positions with examples."
- **Reason**: Clear, specific, includes assessment format

#### T20.G8.05 (REVISED)
- **Old**: "Students integrate data, noise/randomness, and animation phases to create a cohesive experience."
- **New**: "Students combine data-driven layouts with one additional technique (either noise-based variation OR animation) to create a two-phase algorithmic art pipeline. They ensure both phases work together cohesively and explain how each phase contributes to the final artistic result."
- **Reason**: More realistic scope (2 phases not 3), clearer requirements

---

## SECTION F: IMPLEMENTATION PRIORITY

### Phase 1: CRITICAL FIXES (Do First)
**Impact**: Prevents students from being confused or stuck

1. **Fix T20.G3.02** - Remove stamp/pen references, add draw blocks
2. **Fix T20.G3.03** - Remove 3D dependencies, simplify to nested loops
3. **Fix T20.G3.04** - Remove 3D dependencies, reorder before G3.03
4. **Fix T20.G2.03** - Verify dependency is correct T20.G2.01
5. **Add missing "b" skills to allskills.md** - G4.01b, G4.02b, G5.01b, G6.04b, G8.01b

### Phase 2: BREAKDOWNS (Essential for Manageability)
**Impact**: Makes overly broad skills achievable

6. **Break down T20.G3.02** - Add .01 for single shape
7. **Break down T20.G5.01** - Split into bar/scatter/line charts (.01, .02, .03)
8. **Break down T20.G5.04.00** - Split scene init from shapes (.00, .01, .02, .03, .04)
9. **Break down T20.G6.05.02** - Add .00 for basic 3D lines

### Phase 3: NEW SKILLS (Fill Gaps)
**Impact**: Creates proper scaffolding

10. **Add T20.G3.01.01** - Drawing blocks vs pen blocks
11. **Add T20.G4.01.01** - Dynamic color generation
12. **Add T20.G5.05.01** - Bezier curves
13. **Add T20.G6.05.00** - Basic 3D coloring
14. **Add T20.G7.04.00.01** - Stationary particle emitters
15. **Add other new skills** - Per Section C

### Phase 4: T18 DEPENDENCIES (Ensure Accuracy)
**Impact**: Correctly links to 3D/media features

16. **Add T18 dependencies** to all 3D skills (G5.04.00+, G6.05.01+, G7.05.01+)
17. **Add T18 dependencies** for particles (G7.04.00+)
18. **Add T18 dependencies** for post-processing (G8.05.01)
19. **Add T18 dependencies** for materials/lighting where needed

### Phase 5: DEPENDENCY CLEANUP (Polish)
**Impact**: Ensures logical flow

20. **Remove unnecessary deps** - Per Section D
21. **Verify X-2 rule** - All Grade 6-8 skills
22. **Reorder skills** - G3 sequence correction

### Phase 6: DESCRIPTION POLISH (Clarity)
**Impact**: Makes skills more actionable

23. **Update all descriptions** - Per Section E
24. **Add block syntax** - Where missing
25. **Add examples** - For complex skills

---

## SECTION G: RISK ASSESSMENT

### High Risk Issues (Must Fix)

#### R1: Stamp Block Reference
- **Skills Affected**: T20.G3.02 (original)
- **Risk**: Students will look for stamp block and not find it
- **Impact**: Complete confusion, project failure
- **Mitigation**: Fix in Phase 1

#### R2: Missing 3D Shape Foundation
- **Skills Affected**: G5.04.00, G5.04.01, G6.05.01, G7.05.01
- **Risk**: Students try to create 3D art without understanding individual shapes
- **Impact**: Overwhelming complexity, frustration
- **Mitigation**: Break down in Phase 2

#### R3: Missing T18 Dependencies
- **Skills Affected**: All 3D skills (G5.04+, G6.05+, G7.05+, G8.05.01)
- **Risk**: Students use T20 3D skills without T18 3D foundation
- **Impact**: Confusion about where blocks are, missing prerequisites
- **Mitigation**: Add in Phase 4

### Medium Risk Issues (Should Fix)

#### R4: Too Broad Visualization Skill
- **Skills Affected**: T20.G5.01
- **Risk**: One project trying to teach bar charts AND scatter plots
- **Impact**: Rushed learning, shallow understanding
- **Mitigation**: Break down in Phase 2

#### R5: Wrong Skill Ordering
- **Skills Affected**: T20.G3.03, T20.G3.04
- **Risk**: Students do nested loops before tracing simple loops
- **Impact**: Harder learning path, more debugging needed
- **Mitigation**: Reorder in Phase 5

#### R6: Missing Event Handling
- **Skills Affected**: T20.G4.05, T20.G5.03
- **Risk**: Interactive skills without event knowledge
- **Impact**: Students won't know how to trigger interactions
- **Mitigation**: Add deps in Phase 5

### Low Risk Issues (Nice to Fix)

#### R7: Excessive Dependencies
- **Skills Affected**: T20.G8.01 (6 deps), T20.G3.03 (4 deps)
- **Risk**: Dependency overload
- **Impact**: Harder to sequence, intimidating
- **Mitigation**: Clean up in Phase 5

#### R8: Missing Color Skill
- **Skills Affected**: All skills (color used but not taught)
- **Risk**: Students don't know dynamic color generation
- **Impact**: Less colorful, less artistic projects
- **Mitigation**: Add T20.G4.01.01 in Phase 3

---

## SECTION H: VERIFICATION CHECKLIST

### Accuracy Verification
- [ ] All skills use correct CreatiCode block syntax
- [ ] No references to non-existent blocks (stamp, pen up/down)
- [ ] All 2D drawing uses Looks category blocks
- [ ] All 3D skills reference actual 3D Object blocks
- [ ] All particle skills reference actual 3D Effect blocks
- [ ] All material/lighting skills reference actual 3D Tools/Scene blocks

### Dependency Verification
- [ ] All T20 dependencies follow X-2 rule
- [ ] No circular dependencies within T20
- [ ] All cross-topic dependencies preserved (T01-T19, T21-T36)
- [ ] All 3D skills have T18 dependencies
- [ ] All interactive skills have T12/T13 event dependencies
- [ ] All data viz skills have T10 list dependencies

### Scaffolding Verification
- [ ] Each skill builds on previous grade
- [ ] No skill jumps too far in complexity
- [ ] All "b" creative skills paired with "a" technical skills
- [ ] 3D progression follows T18 pattern (init → shapes → materials → effects)
- [ ] Data viz progression follows viz types (bar → scatter → line)
- [ ] Sub-skills (.01, .02) properly numbered

### Manageability Verification
- [ ] No skill covers more than 2-3 concepts
- [ ] All skills completable in reasonable time
- [ ] No skill requires learning 5+ parameters at once
- [ ] Each 3D shape type is separate skill
- [ ] Each visualization type is separate skill

### Description Verification
- [ ] All descriptions include specific blocks
- [ ] All descriptions are actionable
- [ ] All descriptions match CreatiCode capabilities
- [ ] Complex skills include examples
- [ ] Grade level language appropriate

---

## SECTION I: FINAL SKILL COUNT

### Current: 56 skills
- K: 4
- G1: 4
- G2: 4
- G3: 6 (+ 1 sub-skill G3.05.01)
- G4: 6 (+ 1 sub-skill G4.05.01)
- G5: 6 (+ 2 sub-skills G5.01.01, G5.04.00, G5.04.01)
- G6: 6 (+ 3 sub-skills G6.05.01, G6.05.02, G6.05.03)
- G7: 6 (+ 4 sub-skills G7.04.00, G7.04.01, G7.05.01, G7.05.02, G7.05.03)
- G8: 6 (+ 1 sub-skill G8.05.01)

### Proposed After Optimization: ~85 skills
**Breakdown by change type**:

**Added from breakdowns**: +17 skills
- G3.02.01: Single shape drawing
- G5.01.01: Bar charts
- G5.01.02: Scatter plots
- G5.01.03: Line graphs
- G5.04.00: Init 3D scene (revised)
- G5.04.01: 3D boxes
- G5.04.02: 3D spheres
- G5.04.03: 3D cylinders
- G5.04.04: 3D patterns (renumbered)
- G6.05.02.00: Basic 3D lines
- Plus renumbering existing sub-skills

**Added from new skills**: +15 skills
- G3.01.01: Drawing vs pen blocks
- G4.01.01: Dynamic color generation
- G4.04.01: Text-based art
- G5.02.01: Polygons with loops
- G5.03.01: Radial patterns/mandalas
- G5.05.01: Bezier curves
- G5.05.02: Choose viz types
- G6.02.01: Layering patterns
- G6.03.01: Modulo for patterns
- G6.05.00: Basic 3D coloring
- G6.05.04: 3D transformations
- G7.01.01: Reduce redundant calculations
- G7.02.01: Random walks with boundaries
- G7.04.00.01: Stationary particle emitters
- G7.05.00: Camera positioning
- G8.05.00: Understand post-processing

**Added creative pairs**: +5 skills
- G4.01b, G4.02b, G5.01b, G6.04b, G8.01b (if not in allskills.md)

**Total**: 56 + 17 + 15 + 5 = 93 skills (approximate)

### Skill Density by Grade (Proposed)
- K: 4 (appropriate for unplugged)
- G1: 4 (appropriate for unplugged)
- G2: 4 (appropriate for unplugged)
- G3: 10-12 (first coding grade, more foundational)
- G4: 12-14 (building techniques)
- G5: 15-17 (3D introduction adds skills)
- G6: 12-14 (consolidation and advancement)
- G7: 13-15 (advanced techniques)
- G8: 10-12 (synthesis and ethics)

---

## SECTION J: NEXT STEPS

### Immediate Actions
1. **Review this analysis** with stakeholders
2. **Prioritize fixes** - Confirm Phase 1-6 priority
3. **Decide on skill count target** - Is 85-93 skills acceptable?
4. **Verify T18 dependencies** - Confirm which T18 skills exist
5. **Confirm event handling location** - Which topic (T12 or T13)?

### Implementation Process
1. **Phase 1**: Fix critical inaccuracies (stamp, pen, 3D deps)
2. **Phase 2**: Break down overly broad skills
3. **Phase 3**: Add essential new skills
4. **Phase 4**: Add all T18 cross-topic dependencies
5. **Phase 5**: Clean up remaining dependencies
6. **Phase 6**: Polish all descriptions

### Validation Process
1. **Block verification**: Check every block against blockdes8.txt
2. **Dependency verification**: Run dependency checker
3. **Sequence verification**: Verify learning progression
4. **Coverage verification**: Ensure all CreatiCode art features covered

### Documentation
1. **Update skills_T20_algorithmic_art.md** with all changes
2. **Update allskills.md** with all T20 changes
3. **Create change log** documenting all modifications
4. **Create verification report** confirming accuracy

---

## APPENDIX A: CREATICODE BLOCK REFERENCE

### 2D Drawing Blocks (Looks Category)
```
draw rectangle at x (X) y (Y) width (W) height (H) fill [COLOR] border [COLOR] width (W) corner radius (R) rotation (N)
draw oval at x (X) y (Y) width (W) height (H) fill [COLOR] border [COLOR] width (W) rotation (N)
draw line in [COLOR] from x (X1) y (Y1) to x (X2) y (Y2) thickness (T)
draw curve in [COLOR] from x (X1) y (Y1) to x (X2) y (Y2) control 1 x (C1X) y (C1Y) control 2 x (C2X) y (C2Y) thickness (T)
draw text [TEXT] at x (X) y (Y) size (S) color [COLOR] rotation (R)
color (C) saturation (S) brightness (B) transparency (T)
clear all drawings
```

### 3D Shape Blocks (3D Object Category)
```
add box [COLOR] size in x (X) y (Y) z (Z) edge radius (R) as [NAME]
add sphere [COLOR] size in x (X) y (Y) z (Z) arc (ARC) slice (SLICE) sides (S) as [NAME]
add cylinder [COLOR] diameter top (T) bottom (B) height (H) arc (ARC) closed section [Y/N] cap type [TYPE] sides (S) as [NAME]
add cone [COLOR] vertex list [LIST] height (H) as [NAME]
add torus [COLOR] diameter (D) thickness (T) sides (S) as [NAME]
add capsule [COLOR] diameter top (T) bottom (B) height (H) sides (S) as [NAME]
add column [COLOR] 2D vertex list [LIST] height (H) cap type [TYPE] as [NAME]
```

### 3D Line/Curve Blocks (3D Object Category)
```
add line [COLOR] diameter (D) cap [CAP] arrow [ARROW] sides (S) xyz from (X1) (Y1) (Z1) to (X2) (Y2) (Z2) segments (S) as [NAME]
add curve [COLOR] diameter (D) cap [CAP] arrow [ARROW] sides (S) using list [LIST] from (START) to (END) segments (S) as [NAME]
generate arc points from (X1) (Y1) (Z1) via (X2) (Y2) (Z2) to (X3) (Y3) (Z3) into list [LIST] count (N)
```

### 3D Material Blocks (3D Tools Category)
```
update color diffusion [COLOR] emission [COLOR] roughness (R) brightness (B) remove texture [Y/N] area [AREA]
update texture [TEXTURE] unit size (SIZE) non-box repeat h (H) v (V) rotation (R) area [AREA]
```

### 3D Lighting Blocks (3D Scene Category)
```
add ambient light [COLOR] sky direction xyz (X) (Y) (Z) intensity (I) as [NAME]
add directional light [COLOR] in direction xyz (X) (Y) (Z) at xyz (X) (Y) (Z) intensity (I) as [NAME]
add point light [COLOR] at xyz (X) (Y) (Z) intensity (I) show position [Y/N] as [NAME]
add spot light [COLOR] at xyz (X) (Y) (Z) open angle (A) intensity (I) blur (B) show position [Y/N] as [NAME]
```

### Particle Blocks (3D Effect Category)
```
add particle emitter shape [SHAPE] texture [TEXTURE] facing camera [Y/N] life min (MIN) max (MAX) capacity (C) GPU [Y/N] time ratio (RATIO)% as [NAME]
start emitter named [NAME]
```

### Post-Processing Blocks (3D Scene Category)
```
add pipeline vignette (RADIUS) [COLOR] bloom strength (S) threshold (%) kernel (K) antialiasing [Y/N] sharpening [Y/N] camera contrast (C) exposure (E)
```

---

**END OF COMPREHENSIVE ANALYSIS**
**Total Pages**: ~35
**Total Sections**: 10 (A-J) + Appendices
**Ready for**: Stakeholder review and implementation planning
