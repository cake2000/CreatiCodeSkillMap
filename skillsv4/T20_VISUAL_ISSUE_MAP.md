# T20 VISUAL ISSUE MAP
## Grade-by-Grade Issue Breakdown

---

## LEGEND

| Symbol | Meaning |
|--------|---------|
| ✓ | Skill is good |
| ⚠️ | Minor issue (unclear description, dependency fix) |
| 🔧 | Major issue (needs rewrite) |
| ❌ | Must delete (duplicates T18) |
| ➕ | Missing skill (should be added) |

---

## GRADE K (4 skills) - ✓ EXCELLENT

```
✓ T20.GK.01: Picture pattern detective
✓ T20.GK.02: Order art steps with cards
✓ T20.GK.03: Continue the pattern trail
✓ T20.GK.04: Fix the mixed-up art plan

Issues: NONE
Status: Production ready
```

---

## GRADE 1 (4 skills) - ✓ EXCELLENT

```
✓ T20.G1.01: Describe the art rule in words
✓ T20.G1.02: Match directions to drawings
✓ T20.G1.03: Extend a quilt on a grid
✓ T20.G1.04: Fix a wrong instruction

Issues: NONE
Status: Production ready
```

---

## GRADE 2 (4 skills) - ✓ EXCELLENT

```
✓ T20.G2.01: Use repeat cards in an art recipe
✓ T20.G2.02: Plan mirrored mosaics
✓ T20.G2.03: Build layered pattern recipes
✓ T20.G2.04: Explain how a change affects the art

Issues: NONE
Status: Production ready
```

---

## GRADE 3 (6 skills) - ⚠️ MINOR ISSUES

```
✓ T20.G3.01: Translate art recipe cards into blocks
✓ T20.G3.01.01: Explain CreatiCode drawing model
✓ T20.G3.01.02: Use basic pen blocks
✓ T20.G3.02: Program a repeating border with loops
✓ T20.G3.03: Trace a drawing loop and predict output
✓ T20.G3.04: Tile a grid with nested loops
⚠️ T20.G3.05: Add simple randomness for variety
   └─ Issue: "Simple" undefined - needs concrete examples
✓ T20.G3.05.01: Use variables to change pattern size

Issues: 1 minor
Fixes needed:
  - Clarify T20.G3.05 description (provide example ranges)
```

---

## GRADE 4 (8 skills) - ⚠️ MODERATE ISSUES

```
⚠️ T20.G4.01: Implement incremental loops for spirals [Technical]
   └─ Issue: 11 dependencies (should be 3-4)
⚠️ T20.G4.02: Implement tessellation with custom blocks [Technical]
   └─ Issue: "Tessellation" concept not explained
✓ T20.G4.03: Control art with parameters
⚠️ T20.G4.03.01: Create smooth animations
   └─ Issue 1: Should be main skill, not sub-skill
   └─ Issue 2: Depends on T03.G4.03 (team roles - irrelevant!)
⚠️ T20.G4.03.02: Design and apply color palettes
   └─ Issue 1: Should be main skill, not sub-skill
   └─ Issue 2: Depends on user interview skills (irrelevant!)
✓ T20.G4.04: Debug a multi-loop art script
✓ T20.G4.05: Recolor art with simple input events
✓ T20.G4.05.01: Map list values to drawing positions
✓ T20.G4.05.02: Use color reporter for dynamic palettes

Issues: 4 moderate
Fixes needed:
  - Reduce T20.G4.01 dependencies to 3-4 core skills
  - Add tessellation explanation to T20.G4.02
  - Promote T20.G4.03.01 to main skill (renumber as G4.04)
  - Promote T20.G4.03.02 to main skill (renumber as G4.05)
  - Fix irrelevant dependencies
  - Renumber existing G4.04-05 to G4.06-07
```

---

## GRADE 5 (11 skills) - 🚨 CRITICAL ISSUES

```
✓ T20.G5.01: Implement simple data-driven visualization [Technical]
✓ T20.G5.01.01: Map data to two visual properties
➕ MISSING: T20.G5.01.02: Handle text/category data
   └─ Gap in data viz progression
✓ T20.G5.02: Animate a pattern with a counter variable
✓ T20.G5.03: Make art respond to mouse or keys
✓ T20.G5.04: Create fractal-like nested patterns
❌ T20.G5.04.00: Initialize 3D scenes
   └─ DUPLICATE: T18.G4.01.01 covers this
   └─ ID ERROR: .00 suffix when .04 exists
✓ T20.G5.05: Explain data-to-visual design choices
   └─ NOTE: Out of order in file (after G5.10)
➕ MISSING: T20.G5.04.01: Apply color theory
   └─ Gap between color reporter (G4) and application
❌ T20.G5.06: Add box shapes to 3D scenes
   └─ DUPLICATE: T18.G4.01.02 teaches same block
❌ T20.G5.07: Add sphere shapes to 3D scenes
   └─ DUPLICATE: T18.G4.01.03 teaches same block
❌ T20.G5.08: Add cylinder shapes to 3D scenes
   └─ DUPLICATE: T18.G4.01.04 teaches same block
❌ T20.G5.09: Create patterns with 3D shapes
   └─ DUPLICATE: Just combines previous 3 duplicates
🔧 T20.G5.10: Create simple 3D artistic patterns
   └─ KEEP but rewrite to assume T18 background
   └─ Rename to "Create 3D algorithmic art"

Issues: 5 deletions, 2 additions, 1 rewrite, 1 reorder
Fixes needed:
  - DELETE: G5.04.00, G5.06, G5.07, G5.08, G5.09 (duplicates)
  - REWRITE: G5.10 (assume T18, focus on algorithms)
  - ADD: G5.01.02 (text/category data)
  - ADD: G5.04.01 (color theory)
  - RENUMBER: All remaining skills sequentially
  - FIX ORDER: Move G5.05 to correct position

After fixes: 11 skills → 8 skills
```

---

## GRADE 6 (8 skills) - 🚨 MODERATE-HIGH ISSUES

```
✓ T20.G6.01: Trace and explain an art algorithm
✓ T20.G6.02: Refactor repetitive art into loops/custom blocks
✓ T20.G6.03: Use variables and conditionals to branch designs
✓ T20.G6.04: Implement multi-field data visualization [Technical]
➕ MISSING: T20.G6.04.01: Create interactive data viz
   └─ Gap: No hover/click/filter interactivity
✓ T20.G6.05: Apply math transformations to art
❌ T20.G6.05.01: Apply materials and textures to 3D art
   └─ DUPLICATE: T18.G5.04-05 cover materials comprehensively
⚠️ T20.G6.05.02: Create 3D curve and line art
   └─ KEEP (unique to algorithmic art)
   └─ Issue: Missing dependencies (needs list iteration)
✓ T20.G6.05.03: Create interactive 3D generative art
   └─ KEEP (unique combination of T18 + algorithmic)
➕ MISSING: T20.G6.06: Document and export algorithmic art
   └─ Gap: No skill for saving/sharing work
➕ MISSING: T20.G6.07: Debug mathematical/visual errors
   └─ Gap: G4.04 only covers loop debugging

Issues: 1 deletion, 3 additions, 1 dependency fix
Fixes needed:
  - DELETE: G6.05.01 (materials duplicate)
  - ADD: G6.04.01 (interactive viz)
  - ADD: G6.06 (documentation)
  - ADD: G6.07 (math debugging)
  - FIX: G6.05.02 dependencies (add T10.G5.01, T10.G4.02)
  - RENUMBER: After changes

After fixes: 8 skills → 10 skills
```

---

## GRADE 7 (10 skills) - 🚨 CRITICAL ISSUES

```
✓ T20.G7.01: Compare efficiency of art algorithms
✓ T20.G7.02: Use while/repeat-until loops in art
✓ T20.G7.03: Study parameter impact on aesthetics
✓ T20.G7.04: Analyze real generative artworks
❌ T20.G7.04.00: Understand particle system basics
   └─ DUPLICATE: T18.G5.06.01-02 cover particle basics
   └─ ID ERROR: Unrelated to parent T20.G7.04
❌ T20.G7.04.01: Create particle-based generative art
   └─ DUPLICATE: T18.G5.06.03-05 cover particle configuration
   └─ ID ERROR: Unrelated to parent T20.G7.04
🔧 T20.G7.05: Generate fractal patterns using L-system rules
   └─ Issue 1: Description just repeats title
   └─ Issue 2: L-systems too advanced (college CS topic)
   └─ Issue 3: No explanation of what L-systems are
   └─ Fix: Simplify to "rule-based pattern generation"
🔧 T20.G7.05.01: Implement cellular automata
   └─ Issue 1: No description of mechanics
   └─ Issue 2: Should be parallel to G7.05, not sub-skill
   └─ Issue 3: 2D automata too complex for Grade 7
   └─ Fix: Simplify to 1D automata, make parallel skill
✓ T20.G7.05.02: Combine L-systems and cellular automata
   └─ NOTE: Will need rewrite after parent skills simplified
🔧 T20.G7.06: Create 3D generative sculptures with particles
   └─ Issue: References deleted particle skills
   └─ Fix: Merge particle content into this skill, assume T18
❌ T20.G7.07: Use lighting to enhance 3D algorithmic art
   └─ DUPLICATE: T18.G6.04.01-04 cover all lighting comprehensively
✓ T20.G7.08: Generate custom 3D shapes from vertices
   └─ KEEP (advanced, unique to algorithmic art)
   └─ NOTE: Will be renumbered to G7.07

Issues: 3 deletions, 4 rewrites
Fixes needed:
  - DELETE: G7.04.00, G7.04.01, G7.07 (duplicates)
  - REWRITE: G7.05 (simplify L-systems)
  - REWRITE: G7.05.01 (simplify automata, make parallel)
  - REWRITE: G7.05.02 (after parent rewrites)
  - REWRITE: G7.06 (merge particle content)
  - RENUMBER: All skills after deletions

After fixes: 10 skills → 7 skills
```

---

## GRADE 8 (6 skills) - ⚠️ MODERATE ISSUES

```
⚠️ T20.G8.01: Implement multi-dimensional data mapping [Technical]
   └─ Issue: Mentions "normalization algorithms" without guidance
   └─ Fix: Add concrete examples of scaling techniques
✓ T20.G8.02: Create constrained generative artwork
✓ T20.G8.03: Evaluate authorship/originality in generative art
✓ T20.G8.04: Optimize rendering for performance
🔧 T20.G8.05: Implement advanced 3D artistic effects
   └─ CRITICAL: Claims "custom shaders" - NOT IN CREATICODE
   └─ CRITICAL: Claims "procedural materials" - NOT IN CREATICODE
   └─ Fix: Rewrite to use actual available features
⚠️ T20.G8.05.01: Apply post-processing effects
   └─ Issue: May duplicate T18 post-processing
   └─ Action: Verify T18 coverage, delete if duplicate

Issues: 1 critical rewrite, 2 moderate fixes
Fixes needed:
  - REWRITE: G8.05 (remove non-existent features)
  - CLARIFY: G8.01 (add scaling examples)
  - VERIFY: G8.05.01 (check T18 for duplication)

After fixes: 6 skills (possibly 5 if G8.05.01 deleted)
```

---

## SUMMARY BY GRADE

| Grade | Total Skills | ✓ Good | ⚠️ Minor | 🔧 Major | ❌ Delete | ➕ Add | Net Change |
|-------|-------------|--------|----------|----------|-----------|---------|------------|
| K     | 4           | 4      | 0        | 0        | 0         | 0       | 0          |
| 1     | 4           | 4      | 0        | 0        | 0         | 0       | 0          |
| 2     | 4           | 4      | 0        | 0        | 0         | 0       | 0          |
| 3     | 6           | 5      | 1        | 0        | 0         | 0       | 0          |
| 4     | 8           | 4      | 4        | 0        | 0         | 0       | 0          |
| 5     | 11          | 4      | 0        | 1        | 5         | 2       | -3         |
| 6     | 8           | 5      | 1        | 0        | 1         | 3       | +2         |
| 7     | 10          | 3      | 0        | 4        | 3         | 0       | -3         |
| 8     | 6           | 3      | 2        | 1        | 0         | 0       | 0          |
| **TOTAL** | **61** | **36** | **8** | **6** | **9** | **5** | **-4** |

**Status Breakdown:**
- ✓ Good: 36 skills (59%)
- ⚠️ Minor Issues: 8 skills (13%)
- 🔧 Major Issues: 6 skills (10%)
- ❌ Must Delete: 9 skills (15%)
- ➕ Must Add: 5 skills (8%)

---

## ISSUE CATEGORIES VISUAL

### Duplication with T18 (9 skills)
```
Grade 5: ████████████████████ (5 skills)
Grade 6: ████ (1 skill)
Grade 7: ████████████ (3 skills)
         ├─ All basic 3D shapes
         ├─ Materials/textures
         ├─ Particle systems
         └─ Lighting
```

### ID System Problems (3 skills)
```
T20.G5.04.00  ← .00 suffix error
T20.G7.04.00  ← Unrelated to parent
T20.G7.04.01  ← Unrelated to parent
```

### Platform Misalignment (1 skill)
```
T20.G8.05 ← Claims shaders/procedural materials
```

### Unclear Descriptions (5 skills)
```
T20.G3.05     ← "Simple" undefined
T20.G4.02     ← Tessellation not explained
T20.G7.05     ← L-systems not explained
T20.G7.05.01  ← Automata not explained
T20.G8.05     ← (Also has platform issues)
```

### Dependency Problems (4 skills)
```
T20.G4.01     ← 11 deps (excessive)
T20.G4.03.01  ← Team roles (irrelevant)
T20.G4.03.02  ← User interviews (irrelevant)
T20.G6.05.02  ← Missing list deps
```

### Missing Skills (5 gaps)
```
Grade 5: Text/category data viz
Grade 5: Color theory application
Grade 6: Interactive data viz
Grade 6: Documentation/export
Grade 6: Math debugging
```

---

## VISUAL DEPENDENCY MAP (ISSUES)

### Current Problematic Structure
```
T20.G4.03: Control with parameters
    ├─ T20.G4.03.01: Animations ⚠️ (should be main skill)
    └─ T20.G4.03.02: Palettes ⚠️ (should be main skill)

T20.G5.04: Fractal patterns (2D)
    └─ T20.G5.04.00: 3D init ❌ (unrelated duplicate)

T20.G7.04: Analyze real artworks
    ├─ T20.G7.04.00: Particle basics ❌ (unrelated duplicate)
    └─ T20.G7.04.01: Particle art ❌ (unrelated duplicate)

T20.G7.05: L-systems
    ├─ T20.G7.05.01: Automata ⚠️ (should be parallel)
    └─ T20.G7.05.02: Combined (depends on both)
```

### Correct Structure (After Fixes)
```
T20.G4.03: Control with parameters
T20.G4.04: Create animations (promoted)
T20.G4.05: Design palettes (promoted)

T20.G5.04: Fractal patterns (2D only)
T20.G5.06: Create 3D algorithmic art (assumes T18)

T20.G7.04: Analyze real artworks
T20.G7.05: Rule-based patterns (simplified L-systems)
T20.G7.06: Grid-based evolution (simplified automata, parallel)
T20.G7.07: Combined generative techniques
T20.G7.08: 3D generative sculptures (merged particles)
T20.G7.09: Custom 3D vertices (renumbered from G7.08)
```

---

## COVERAGE ANALYSIS

### 2D Drawing Blocks: ✓ EXCELLENT
- Pen blocks (down/up, color, size) ✓
- Draw rectangle/oval on stage ✓
- Draw rectangle/oval/line/curve on costume ✓
- Draw text ✓

### 3D Shapes: ❌ DUPLICATE (covered in T18)
- Basic shapes (box, sphere, cylinder) ← T18.G4
- Advanced shapes (tube, capsule, torus, etc.) ← Not covered
- Custom shapes from vertices ✓ (T20.G7.08 unique)

### Materials/Textures: ❌ DUPLICATE (covered in T18)
- Color diffusion/emission ← T18.G5
- Textures ← T18.G5
- Roughness ← T18.G5
- Metallic properties ← Not explicitly covered

### Lighting: ❌ DUPLICATE (covered in T18)
- Point light ← T18.G6
- Directional light ← T18.G6
- Ambient light ← T18.G6
- Spotlight ← T18.G6

### Particles: ❌ DUPLICATE (covered in T18)
- Prebuilt emitters ← T18.G5
- Custom emitters ← T18.G5
- Color/size configuration ← T18.G5

### Post-Processing: ⚠️ UNCLEAR
- Bloom ← T20.G8.05.01 (verify T18)
- Glow ← T20.G8.05.01 (verify T18)
- Blur ← T20.G8.05.01 (verify T18)

### Data Visualization: ✓ GOOD
- Single-list charts ✓
- Multi-field viz ✓
- Multi-dimensional mapping ✓
- **Missing:** Text/category data
- **Missing:** Interactive viz

### Color System: ✓ GOOD
- HSV color reporter ✓
- Dynamic palettes ✓
- **Missing:** Color theory application

---

## FILES CREATED

1. ✓ **T20_COMPREHENSIVE_ISSUE_ANALYSIS.md** - Full detailed analysis
2. ✓ **T20_ISSUES_QUICK_REFERENCE.md** - Action plan
3. ✓ **T20_VISUAL_ISSUE_MAP.md** - This file (visual breakdown)

**Next:** Implementation phase (delete/modify/add skills)

---

**Summary:** T20 has significant structural issues requiring 14+ hours of work. Grades K-3 are excellent, but Grades 5-7 have critical duplication with T18 (22% of all skills). The ID system is broken, and several skills claim features not in the platform.
