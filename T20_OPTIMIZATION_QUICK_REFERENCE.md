# T20 OPTIMIZATION - QUICK REFERENCE GUIDE

**Date**: 2025-11-23
**Full Analysis**: See T20_COMPREHENSIVE_OPTIMIZATION_ANALYSIS.md

---

## AT A GLANCE

**Total Issues Found**: 28 skills with HIGH or MEDIUM priority issues
**Skills to Break Down**: 8 skills too broad
**New Skills Needed**: 15 gaps for scaffolding
**Dependency Fixes**: 12 violations

**Estimated Final Skill Count**: 85-93 skills (from current 56)

---

## CRITICAL FIXES (DO FIRST)

### 1. T20.G3.02 - Remove Non-Existent Blocks
**Issue**: References "stamp star" and "pen program"
**Fix**: Use `draw rectangle` and `draw oval` blocks instead
**Priority**: CRITICAL - students will be confused

### 2. T20.G3.03 & T20.G3.04 - Remove 3D Dependencies
**Issue**: 2D grid skills depend on T18 3D skills (lighting, shapes)
**Fix**: Remove T18.G3.03, T18.G3.04 dependencies
**Priority**: HIGH - wrong topic entirely

### 3. T20.G3.04 - Reorder Before G3.03
**Issue**: Should trace simple loops BEFORE doing nested loops
**Fix**: Move G3.04 before G3.03 in sequence
**Priority**: HIGH - pedagogical order wrong

### 4. Add Missing "b" Creative Skills to allskills.md
**Issue**: T20.G4.01b, G4.02b, G5.01b, G6.04b, G8.01b listed in skills_T20 but not in allskills.md
**Fix**: Add all "b" creative pair skills or remove from skills_T20
**Priority**: HIGH - inconsistency between files

---

## SKILLS TO BREAK DOWN

### 1. T20.G3.02 → Split into .01 + main
- **.01**: Draw single shape at position
- **Main**: Loop to draw multiple shapes

### 2. T20.G5.01 → Split into 3 visualization types
- **.01**: Create bar charts from list data
- **.02**: Create scatter plots from list data
- **.03**: Create line graphs from list data

### 3. T20.G5.04.00 → Split 3D init from shapes
- **.00**: Initialize 3D scene and understand coordinates
- **.01**: Add boxes to 3D scenes
- **.02**: Add spheres to 3D scenes
- **.03**: Add cylinders to 3D scenes
- **.04**: Create 3D patterns with multiple shapes (renumbered from .01)

### 4. T20.G6.05.02 → Add basic 3D lines first
- **.00**: Create basic 3D lines
- **Main**: Create 3D curves from calculated point lists

---

## TOP 15 NEW SKILLS TO ADD

**Foundational (G3-G4)**:
1. G3.01.01 - Identify drawing blocks vs pen blocks (CreatiCode difference)
2. G4.01.01 - Use dynamic color generation (`color (C) saturation (S) brightness (B) transparency (T)`)
3. G4.04.01 - Create text-based generative art

**Intermediate (G5)**:
4. G5.02.01 - Draw polygons using loops and turns
5. G5.03.01 - Create radial patterns and mandalas
6. G5.05.01 - Draw bezier curves for organic designs
7. G5.05.02 - Choose appropriate visualization types for data

**Advanced 3D (G6-G7)**:
8. G6.05.00 - Apply basic colors to 3D objects
9. G6.05.04 - Apply rotations and scaling to 3D patterns
10. G6.02.01 - Layer multiple algorithmic patterns
11. G6.03.01 - Use modulo for alternating patterns
12. G7.04.00.01 - Create stationary particle emitters
13. G7.05.00 - Position cameras to showcase 3D art

**Capstone (G8)**:
14. G8.05.00 - Understand post-processing effects
15. G7.01.01 - Reduce redundant calculations in art code

---

## KEY DEPENDENCY FIXES

### Remove Unnecessary Dependencies
- **T20.G2.02**: Remove T05.G1.01 (story needs - irrelevant)
- **T20.G3.03**: Remove T18.G3.03 (3D lighting), T07.G3.02 (trace), T09.G3.01 (variables)
- **T20.G3.04**: Remove T18.G3.04 (3D shapes), T08.G3.02 (conditionals)
- **T20.G3.05**: Remove T07.G3.03 (forever loops)

### Add Missing Dependencies
- **T20.G3.01**: Add T06.G3.01 (green flag scripts)
- **T20.G4.05**: Add T12/T13 event handling
- **T20.G5.03**: Add T12/T13 mouse/key events
- **All 3D skills (G5.04+)**: Add corresponding T18 dependencies
- **T20.G7.04.00**: Add T18 particle introduction
- **T20.G7.05.02**: Add T18 lighting blocks
- **T20.G8.05.01**: Add T18 post-processing blocks

---

## CREATICODE BLOCKS CHEAT SHEET

### What CreatiCode HAS:
✅ `draw rectangle at x (_) y (_) width (_) height (_) fill [color] border [color] width (_) corner radius (_) rotation (_)`
✅ `draw oval at x (_) y (_) width (_) height (_) fill [color] border [color] width (_) rotation (_)`
✅ `draw line in [color] from x (_) y (_) to x (_) y (_) thickness (_)`
✅ `draw curve in [color] from x (_) y (_) to x (_) y (_) control 1 x (_) y (_) control 2 x (_) y (_) thickness (_)`
✅ `draw text [text] at x (_) y (_) size (_) color [color] rotation (_)`
✅ `color (C) saturation (S) brightness (B) transparency (T)` - dynamic color generator
✅ 50+ 3D shape blocks (box, sphere, cylinder, cone, torus, etc.)
✅ 18 particle system blocks
✅ 47 lighting/material/post-processing blocks

### What CreatiCode DOES NOT HAVE:
❌ `pen up` / `pen down`
❌ `set pen color to (_)`
❌ `set pen size to (_)`
❌ `stamp` (create copy of sprite)
❌ Traditional pen drawing while sprite moves

**CRITICAL**: CreatiCode uses POSITION-BASED drawing (Looks category), NOT continuous pen drawing like Scratch!

---

## DESCRIPTION IMPROVEMENT PATTERNS

### Before (Vague):
"Students create spirals using loops"

### After (Specific):
"Students write a loop that increases a variable each iteration using `for [i] from (1) to (360)`, position sprite with `go to x (i * cos(i)) y (i * sin(i))`, and draw with `draw oval at x (x position) y (y position) width (20) height (20) fill [color]`"

### Key Elements to Include:
1. **Specific blocks** with syntax
2. **Mathematical concepts** (angles, increments, coordinates)
3. **Loop structure** type
4. **What students control** (variables, parameters)
5. **Expected output** description

---

## IMPLEMENTATION PHASES

### Phase 1: CRITICAL (Week 1)
- Fix stamp/pen references
- Remove 3D dependencies from 2D skills
- Reorder G3.03 and G3.04
- Add missing "b" skills

### Phase 2: BREAKDOWNS (Week 2)
- Break down G3.02 (single + loop)
- Break down G5.01 (bar/scatter/line)
- Break down G5.04.00 (init + shapes)
- Break down G6.05.02 (basic + calculated lines)

### Phase 3: NEW SKILLS (Week 3)
- Add 15 new foundational skills
- Add color generation skill
- Add text art skill
- Add polygon/mandala skills

### Phase 4: T18 LINKS (Week 4)
- Add T18 dependencies to all 3D skills
- Add T18 particle dependencies
- Add T18 material dependencies
- Add T18 post-processing dependencies

### Phase 5: CLEANUP (Week 5)
- Remove unnecessary dependencies
- Verify X-2 rule throughout
- Check all grade progressions
- Final dependency validation

### Phase 6: POLISH (Week 6)
- Update all descriptions
- Add block syntax throughout
- Add examples where needed
- Final review and validation

---

## VALIDATION CHECKLIST

**Block Accuracy**:
- [ ] No references to stamp, pen up/down, set pen color
- [ ] All 2D drawing uses Looks blocks (draw rectangle/oval/line/curve/text)
- [ ] All 3D references match actual 3D Object blocks
- [ ] All particle references match actual 3D Effect blocks

**Dependencies**:
- [ ] All T20 internal deps follow X-2 rule
- [ ] No circular dependencies
- [ ] All 3D skills have T18 dependencies
- [ ] All interactive skills have event dependencies
- [ ] All data viz skills have list dependencies

**Scaffolding**:
- [ ] Single shapes before loops
- [ ] Simple loops before nested loops
- [ ] Trace before do
- [ ] Each 3D shape type separate
- [ ] Each viz type separate
- [ ] Scene init before shape creation

**Manageability**:
- [ ] No skill covers 5+ concepts
- [ ] Each skill completable in reasonable time
- [ ] No skill requires mastering 8+ parameters at once

---

## RISK MITIGATION

### HIGH RISK: Stamp Block Reference
**Where**: T20.G3.02
**Impact**: Students will search for non-existent block
**Fix**: Replace with draw blocks immediately

### HIGH RISK: Missing 3D Prerequisites
**Where**: G5.04.00 combines init + all shapes
**Impact**: Overwhelming complexity
**Fix**: Break into 5 separate skills

### HIGH RISK: Missing T18 Dependencies
**Where**: All 3D skills (G5.04+, G6.05+, G7.05+)
**Impact**: Students don't know where 3D blocks are
**Fix**: Add T18 deps in Phase 4

### MEDIUM RISK: Visualization Too Broad
**Where**: T20.G5.01 tries to teach 3 viz types
**Impact**: Shallow learning, rushed projects
**Fix**: Split into .01 (bar), .02 (scatter), .03 (line)

---

## SUCCESS METRICS

**Accuracy**:
- 100% of skills use existing CreatiCode blocks
- 0 references to non-existent blocks
- All 3D skills linked to T18

**Scaffolding**:
- Every skill builds on max 3-4 prerequisites
- No jumps > 2 grade levels in dependencies
- Clear progression within each grade

**Manageability**:
- Average skill completion time: 30-45 minutes
- Max concepts per skill: 3
- Max new parameters per skill: 5

**Coverage**:
- All CreatiCode artistic blocks covered
- 2D drawing: rectangles, ovals, lines, curves, text ✓
- 3D shapes: box, sphere, cylinder, cone, torus ✓
- 3D effects: materials, lighting, particles, post-processing ✓
- Data viz: bar, scatter, line graphs ✓

---

## QUESTIONS FOR STAKEHOLDERS

1. **Skill count**: Is 85-93 skills acceptable for T20? (vs current 56)
2. **T18 dependencies**: Which specific T18 skills exist for 3D intro, materials, particles, post-processing?
3. **Event handling**: Where are mouse/key event skills - T12 or T13?
4. **Creative pairs**: Should all technical skills have creative pair "b" skills?
5. **Grade distribution**: Is 15-17 skills in G5 (3D intro) acceptable?

---

## FILES CREATED

1. **T20_COMPREHENSIVE_OPTIMIZATION_ANALYSIS.md** (35 pages)
   - Complete analysis of all 56 skills
   - Section A: All issues identified
   - Section B: Proposed breakdowns
   - Section C: Proposed new skills
   - Section D: Dependency fixes
   - Section E: Description improvements
   - Full implementation plan

2. **T20_OPTIMIZATION_QUICK_REFERENCE.md** (this file)
   - Executive summary
   - Critical fixes only
   - Top priorities
   - Validation checklist

---

**NEXT STEP**: Review with stakeholders → Approve phases → Begin implementation

**CONTACT**: See T20_COMPREHENSIVE_OPTIMIZATION_ANALYSIS.md Section J for detailed next steps
