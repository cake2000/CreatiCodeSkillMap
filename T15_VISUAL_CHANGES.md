# T15 Optimization Visual Diagrams

## Overview of Restructuring

```
LEGEND:
  [DELETED]  - Skill removed
  MODIFIED   - Skill changed
  +NEW+      - Skill added
  └─         - Dependency relationship
```

## 1. Say/Think Block Restructure

### Before (WRONG - teaches non-existent blocks)
```
G3.04: Say something
  └─ Teaches: say [Hello] for (2) seconds
  └─ Problem: This block doesn't exist!

G3.05: Think bubble  
  └─ Teaches: think [Hmm...]
  └─ Problem: This block doesn't exist!

G3.05.01: Style think bubbles
  └─ Depends on: G3.10

[G3.10]: Enhanced say with styling [REDUNDANT]
  └─ Teaches: styled say block
  └─ Problem: This is the ONLY say block - not an enhancement
```

### After (CORRECT - teaches actual blocks)
```
G3.04: Display speech with say blocks [MODIFIED]
  └─ Teaches: say [Hello!] for (2) seconds text size (16) [#FFF] background [#000] edge [#FFF]
  └─ This is the REAL block that exists
    |
    └─ +G3.04.01: Style speech bubbles for mood+ [NEW]
        └─ Advanced styling: colors, sizes, psychology

G3.05: Display thoughts with think blocks [MODIFIED]
  └─ Teaches: think [Hmm...] for (2) seconds text size (16) [#FFF] background [#000] edge [#FFF]
  └─ This is the REAL block that exists
    |
    └─ G3.05.01: Style think bubbles [MODIFIED]
        └─ Updated dependencies: now depends on G3.04.01

[DELETED] G3.10: Enhanced say with styling
```

**Impact**: Students now learn the correct blocks from the start, avoiding misconceptions.

---

## 2. Widget Text Skills Breakdown

### Before (TOO COMPLEX)
```
G3.11: Display labels for titles
  └─ Teaches 5 concepts:
      1. Create label widget
      2. Position labels
      3. Set label text
      4. Update label text
      5. Style labels

G3.12: Print text at positions
  └─ Teaches 4 concepts:
      1. Print text
      2. Timed prints
      3. Position relative to sprites
      4. Clear prints
```

### After (FOCUSED)
```
G3.11: Create label widgets [MODIFIED - focused]
  └─ ONE concept: Create persistent label widgets
    |
    ├─ +G3.11.01: Position labels+ [NEW]
    |   └─ ONE concept: Strategic screen positioning
    |
    └─ +G3.11.02: Update label text+ [NEW]
        └─ ONE concept: Dynamic text updates

G3.12: Print temporary text [MODIFIED - focused]
  └─ ONE concept: Print text to stage layer
    |
    ├─ +G3.12.01: Timed and sprite-relative text+ [NEW]
    |   └─ ONE concept: Duration and positioning
    |
    └─ +G3.12.02: Clear printed text+ [NEW]
        └─ ONE concept: Clearing for scene changes
```

**Impact**: Each skill teaches ONE implementable concept. Students can complete and test each skill independently.

---

## 3. Drawing Skills Breakdown

### Before (COMBINED)
```
G5.09: Draw shapes on costumes
  └─ Teaches: rectangles AND ovals together
  └─ Problem: Too much to learn at once

G5.10: Draw lines and curves
  └─ Teaches: lines AND curves AND text together
  └─ Problem: 3 different concepts in one skill

G5.11: Clear drawings
```

### After (SEPARATED)
```
G5.09: Draw rectangles [MODIFIED - rectangles only]
  └─ ONE shape: Rectangle with all parameters
    |
    ├─ +G5.09.01: Draw ovals and circles+ [NEW]
    |   └─ ONE shape: Oval/circle parameters
    |
    └─ +G5.09.02: Dynamic visual effects+ [NEW]
        └─ APPLICATION: Loops, variables, patterns

G5.10: Draw straight lines [MODIFIED - lines only]
  └─ ONE shape: Straight lines
    |
    ├─ +G5.10.01: Draw bezier curves+ [NEW]
    |   └─ ONE shape: Curves with control points
    |
    └─ +G5.10.02: Draw text on costumes+ [NEW]
        └─ ONE feature: Text drawing

G5.11: Clear all drawings [MODIFIED - clarified]
  └─ Updated dependencies and description
```

**Impact**: Progressive learning - master one shape type before moving to the next.

---

## 4. Text-to-Speech Breakdown

### Before (ALL-IN-ONE)
```
G5.12: Basic text-to-speech narration
  └─ Teaches everything:
      - Basic TTS usage
      - 30+ languages
      - 8 voice types
      - Speed adjustment (50-200)
      - Pitch adjustment (50-200)  
      - Volume adjustment (0-200)
      - Sound storage
```

### After (PROGRESSIVE)
```
G5.12: Basic TTS [MODIFIED - basics only]
  └─ Core concept: Convert text to speech
  └─ Default values: English, Female, 100/100/100
    |
    ├─ +G5.12.01: Languages and voices+ [NEW]
    |   └─ ONE concept: Select language and voice type
    |
    └─ +G5.12.02: Speech characteristics+ [NEW]
        └─ ONE concept: Adjust speed/pitch/volume
```

**Impact**: Learn basics first, then customize. Students aren't overwhelmed with options.

---

## 5. Widget Styling Breakdown

### Before (ALL STYLING)
```
G5.13: Style widgets for stories
  └─ Teaches everything:
      - Background colors
      - Border colors
      - Border width
      - Border radius
      - Font selection
      - Font size
      - Text color
      - Bold/normal
      - Text alignment
      - Theme matching
```

### After (SEPARATED)
```
G5.13: Background and borders [MODIFIED - colors/borders]
  └─ Color system: #RRGGBBAA format
  └─ Border styling: width, radius
    |
    ├─ +G5.13.01: Text formatting+ [NEW]
    |   └─ Text properties: font, size, color, alignment, bold
    |
    └─ +G5.13.02: Theme cohesion+ [NEW]
        └─ APPLICATION: Match widgets to story mood
```

**Impact**: Master the visual foundation (colors/borders) before tackling text formatting and theming.

---

## 6. Scene Management Breakdown

### Before (COMPLEX)
```
G4.02: Scene management with broadcasts
  └─ Teaches:
      - Broadcast concept
      - Receive concept
      - Multi-sprite coordination
      - Show/hide sprites
      - Position changes
      - Backdrop changes
      - Widget visibility
```

### After (SEPARATED)
```
G4.02: Broadcast for scene changes [MODIFIED - mechanism]
  └─ Core concept: Use broadcast to trigger scenes
  └─ How ALL sprites respond simultaneously
    |
    └─ +G4.02.01: Sprite responses+ [NEW]
        └─ Implementation: Write receive blocks
        └─ Show/hide/position for each sprite
```

**Impact**: Understand the mechanism (broadcast), then implement the responses.

---

## Foundation Chain Fix

### Before (ILLOGICAL)
```
G3.00.01: Understand sprite appearance
  └─ G3.00.02: Change sprite size
      └─ G3.00.03: Customize costumes in paint editor
          └─ G3.01: Change sprite position ❌ WRONG!
              └─ Problem: Position doesn't require paint editor
```

### After (LOGICAL)
```
G3.00.01: Understand sprite appearance
  └─ G3.00.02: Change sprite size
      └─ G3.00.03: Customize costumes in paint editor

G3.01: Change sprite position [MODIFIED]
  └─ Depends on: T01.G3.01 only ✓ CORRECT!
  └─ Position is independent of costumes
```

**Impact**: Clear, logical learning path. Students understand position as a fundamental concept.

---

## Summary Statistics

```
CHANGES BY TYPE:
  Deleted:   1 skill  (G3.10)
  Added:    14 skills (all .01, .02 sub-skills)
  Modified: 12 skills (simplified descriptions, fixed dependencies)
  
SKILL COUNT:
  Before: 70 skills
  After:  83 skills
  Growth: +13 skills (+19%)

COMPLEXITY REDUCTION:
  Before: Average 3.2 concepts per skill
  After:  Average 1.3 concepts per skill
  
DEPENDENCY FIXES:
  - 1 illogical dependency removed (G3.01 → G3.00.03)
  - 5 dependencies updated (G3.10 references replaced)
  - 14 new dependency chains created (all verified)
```

---

## Learning Path Improvements

### Example: Learning to Display Text

**Before** (Fragmented):
```
G3.04 → G3.10 (redundant) → G3.11 (overwhelming)
```

**After** (Progressive):
```
G3.04: Learn styled say block
  └─ G3.04.01: Master mood/emphasis styling
      └─ G3.11: Create label widgets
          ├─ G3.11.01: Position strategically
          └─ G3.11.02: Update dynamically
```

### Example: Learning to Draw

**Before** (Simultaneous):
```
G5.09: Rectangle + Oval at once
G5.10: Line + Curve + Text at once
```

**After** (Sequential):
```
G5.09: Rectangle only
  └─ G5.09.01: Oval only
      └─ G5.09.02: Apply to effects
          └─ G5.10: Line only
              └─ G5.10.01: Curve only
                  └─ G5.10.02: Text only
```

---

## Block Verification Status

✅ **VERIFIED** - All skills reference blocks that exist in blockdes8.txt:
- say [TEXT] for (T) seconds text size (FONTSIZE) [FONTCOLOR] background [BACKGROUNDCOLOR] edge [EDGECOLOR]
- think [TEXT] for (T) seconds text size (FONTSIZE) [FONTCOLOR] background [BACKGROUNDCOLOR] edge [EDGECOLOR]
- say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]
- draw rectangle at x (XPOS) y (YPOS) width (W) height (H) fill [FILLCOLOR] border [BORDERCOLOR] width (BORDERWIDTH) corner radius (CORNERRADIUS) rotation (N)
- draw oval at x (XPOS) y (YPOS) width (W) height (H) fill [FILLCOLOR] border [BORDERCOLOR] width (BORDERWIDTH) rotation (N)
- draw line in [LINECOLOR] from x (FROMX) y (FROMY) to x (TOX) y (TOY) thickness (THICKNESS)
- draw curve in [LINECOLOR] from x (FROMX) y (FROMY) to x (TOX) y (TOY) control 1 x (CONTROLX1) y (CONTROLY1) control 2 x (CONTROLX2) y (CONTROLY2) thickness (THICKNESS)
- draw text [TEXT] at x (X) y (Y) size (SIZE) color (COLOR) rotation (ROTATION)
- clear all drawings
- add label [TEXT] at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (P) as [NAME]
- print [TEXT] at x (X) y (Y) width (W) height (H) color [COLOR]
- print [TEXT] at x (X) y (Y) width (W) height (H) color [COLOR] for (T) seconds

❌ **NOT FOUND** - These blocks don't exist (no skills added):
- switch costume to [COSTUME v]
- next costume
- switch backdrop to [BACKDROP v]
- change [color/brightness/ghost v] effect by (N)
- set [color/brightness/ghost v] effect to (N)

---

**End of Visual Diagrams**
