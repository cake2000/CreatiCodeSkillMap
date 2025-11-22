# T20 Quality Issues - Quick Reference

**Total Issues Found:** 23
**High Priority:** 15 | **Medium Priority:** 8
**New Skills Needed:** 8 | **Skills to Modify:** 13

---

## CRITICAL GAPS (Do These First)

### Missing 3D Capabilities
1. **Materials/Textures** - Add T20.G6.05.01
2. **Lighting** - Add T20.G7.05.02
3. **Post-Processing** - Add T20.G8.05.01
4. **Particle Systems** - Add T20.G7.04.01 (standalone, not just with 3D)
5. **3D Curves/Lines** - Add T20.G6.05.02
6. **Interactive 3D** - Add T20.G6.05.03
7. **Custom 3D Vertices** - Add T20.G7.05.03

### Scaffolding Gaps
8. **G5→G6 Data Viz** - Add T20.G5.01.01 (2 properties before multi-field)
9. **Particles Too Late** - Move standalone particle skill before 3D+particle combo
10. **2D→3D Math** - Update G6.05.02 to bridge trigonometry to 3D space

---

## QUICK FIXES (High Impact, Low Effort)

### Grade-Inappropriate (K-G1)
- **T20.GK.02**: Simplify "dip brush, sprinkle dots" → "pick red crayon, add yellow dots"
- **T20.G1.04**: Emphasize audio over text reading

### Unclear Descriptions
- **T20.G3.05**: Clarify "position shifts" = randomizing x/y in draw blocks
- **T20.G4.04**: Specify "colors" = fill/border parameters, not global pen color
- **T20.G6.01**: Define "annotated code" = code with comments
- **T20.G7.04**: Add deliverable: write pseudocode or simple implementation
- **T20.G8.02**: Replace "guardrails" → "constraints (conditionals, boundary checks)"

### Dependency Fix
- **T20.G4.03**: Remove T28.G3.04 (ethics), not needed for art randomness

### Simplification
- **T20.G8.05**: Reduce 3-phase pipeline → 2-phase (data + one technique)

---

## ISSUE CATEGORIES

| Category | Count | Priority Split |
|----------|-------|----------------|
| Missing Essential Skills | 7 | 6 High, 1 Med |
| Unclear Descriptions | 5 | 2 High, 2 Med, 1 Low |
| Weak Scaffolding | 3 | 1 High, 2 Med |
| Inaccurate References | 4 | 0 High, 3 Med, 1 Low |
| Grade-Inappropriate | 2 | 1 High, 1 Med |
| Skills Too Broad | 2 | 1 High, 1 Med |

---

## NEW SKILLS AT A GLANCE

| Skill ID | Title | Grade | Fills Gap |
|----------|-------|-------|-----------|
| T20.G5.01.01 | Map data to TWO visual properties | G5 | Data viz scaffolding |
| T20.G6.05.01 | Apply materials/textures to 3D art | G6 | 3D materials |
| T20.G6.05.02 | Create 3D curve and line art | G6 | 3D lines, 2D→3D math |
| T20.G6.05.03 | Create interactive 3D art | G6 | 3D interactivity |
| T20.G7.04.01 | Create particle-based generative art | G7 | Standalone particles |
| T20.G7.05.02 | Use lighting for 3D art | G7 | Lighting |
| T20.G7.05.03 | Custom 3D shapes from vertices | G7 | Advanced 3D geometry |
| T20.G8.05.01 | Apply post-processing effects | G8 | Rendering effects |

---

## SKILLS NEEDING DESCRIPTION UPDATES

1. T20.GK.02 - Kindergarten simplification
2. T20.G1.04 - Audio emphasis
3. T20.G3.03 - Remove "pen loop" references (verify)
4. T20.G3.05 - Clarify position randomization
5. T20.G4.04 - Clarify color parameters
6. T20.G5.01 - Clarify visualization types
7. T20.G6.01 - Define annotations
8. T20.G7.04 - Add concrete deliverable
9. T20.G7.05 - Broaden beyond L-systems
10. T20.G8.02 - Replace "guardrails"
11. T20.G8.03 - Specify assessment format
12. T20.G8.05 - Simplify to 2 phases

---

## WHAT T20 DOES WELL

✓ **2D drawing blocks** - All references corrected to draw rectangle/oval/line/curve
✓ **Basic progression** - K-2 unplugged → G3-4 fundamentals → G5-8 advanced
✓ **Data visualization** - Good coverage of list-to-visual mapping
✓ **Mathematical art** - Spirals, fractals, parametric curves covered
✓ **Random art** - Generative composition skills present
✓ **X-2 compliance** - All dependency violations fixed previously

---

## WHAT T20 NEEDS

✗ **3D advanced features** - Materials, lighting, post-processing missing
✗ **Particle depth** - Only mentioned once, needs standalone coverage
✗ **3D scaffolding** - Jumps too quickly to complex 3D without intermediate steps
✗ **Clarity** - 11 descriptions need refinement
✗ **K-G1 appropriateness** - 2 skills too abstract/text-heavy

---

## IMPLEMENTATION EFFORT

| Phase | Tasks | Estimated Time |
|-------|-------|----------------|
| **Phase 1** | Add 8 new skills, fix 2 grade issues, 3 scaffolding gaps | 4-5 hours |
| **Phase 2** | Update 11 descriptions, fix 1 dependency | 2-3 hours |
| **Phase 3** | Verify references, add teacher notes, create rubrics | 1-2 hours |
| **TOTAL** | 21 changes (8 new + 13 modified) | **6-8 hours** |

---

## KEY INSIGHTS

### Why These Issues Matter

1. **CreatiCode's 3D strength** is underutilized - has materials, lighting, particles, but T20 barely teaches them
2. **Students hit wall at G7** - trying to make advanced 3D art without knowing materials/lighting
3. **Particle potential wasted** - 18 particle blocks available, only 1 skill mentions them
4. **2D excellent, 3D incomplete** - Topic heavily favors 2D algorithmic art over 3D

### Quick Wins
- Fix 11 description clarity issues (30 min each = 5.5 hours)
- Add missing scaffolding skills (1 hour each = 3 hours)
- Total quick wins: **8.5 hours of work** addresses most issues

### Strategic Value
T20 is where students create **portfolio-worthy art projects**. Missing 3D capabilities means:
- Less impressive final projects
- Students don't see CreatiCode's full power
- Competing platforms (p5.js, Processing) look more capable
- Teachers miss opportunities for interdisciplinary STEAM projects

---

**Bottom Line:** T20 needs **8 new skills** focused on 3D capabilities and **13 description fixes**. This transforms it from "good 2D algorithmic art" to "comprehensive generative art covering 2D, 3D, particles, materials, lighting, and effects."

---

Generated: 2025-11-22
See: T20_QUALITY_ANALYSIS.md for complete details
