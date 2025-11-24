# T15 (Stories & Animation) Optimization Summary

**Date:** 2025-11-23
**Status:** Analysis Complete - Implementation Recommended

## Overview

This document provides a comprehensive optimization plan for T15 (Stories & Animation) skills based on verification of actual CreatiCode blocks in blockdes8.txt.

**Current Status:**
- Original skill count: 70
- Proposed changes: Delete 1, Add 14 new sub-skills, Modify 9 existing
- Estimated final count: 83 skills (+13 net)

## Key Findings from Block Verification

### 1. Say/Think Blocks
**Actual blocks found:**
- `say [TEXT] for (T) seconds text size (FONTSIZE) [FONTCOLOR] background [BACKGROUNDCOLOR] edge [#EDGECOLOR]`
- `think [TEXT] for (T) seconds text size (FONTSIZE) [FONTCOLOR] background [BACKGROUNDCOLOR] edge [EDGECOLOR]`

**Finding:** Only styled versions exist - there are NO basic say/think blocks without styling parameters.

**Implication:** Current G3.04 teaches "basic" say that doesn't exist. Students must learn the full styled block from the start.

### 2. Text-to-Speech
**Actual block found:**
- `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]`

**Finding:** This is a completely different block from visual say blocks - it generates audio.

**Implication:** Current G5.12 conflates too many concepts. Needs to be split into 3 focused skills.

### 3. Drawing Blocks
**Actual blocks found:**
- `draw rectangle at x (XPOS) y (YPOS) width (W) height (H) fill [FILLCOLOR] border [BORDERCOLOR] width (BORDERWIDTH) corner radius (CORNERRADIUS) rotation (N)`
- `draw oval at x (XPOS) y (YPOS) width (W) height (H) fill [FILLCOLOR] border [BORDERCOLOR] width (BORDERWIDTH) rotation (N)`
- `draw line in [LINECOLOR] from x (FROMX) y (FROMY) to x (TOX) y (TOY) thickness (THICKNESS)`
- `draw curve in [LINECOLOR] from x (FROMX) y (FROMY) to x (TOX) y (TOY) control 1 x (CONTROLX1) y (CONTROLY1) control 2 x (CONTROLX2) y (CONTROLY2) thickness (THICKNESS)`
- `draw text [TEXT] at x (X) y (Y) size (SIZE) color (COLOR) rotation (ROTATION)`
- `clear all drawings`

**Implication:** Each draw type is complex enough to warrant its own skill.

### 4. Costume/Backdrop Blocks
**Blocks NOT found:**
- switch costume to
- next costume
- switch backdrop to
- graphic effects (color, brightness, ghost, etc.)

**Finding:** These standard Scratch blocks don't exist in CreatiCode or are in different categories.

**Implication:** Don't add skills for non-existent blocks.

### 5. Widget Blocks
**Verified blocks:**
- `add label [TEXT] at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (P) as [NAME]`
- `add textbox at X (X) Y (Y) width (W) height (H) padding (P) line [LINETYPE v] scroll [SCROLLTYPE v] mode [MODETYPE v] as [NAME]`
- `add button [TEXT] at X (X) Y (Y) width (WIDTH) height (HEIGHT) tooltip [TOOLTIP] as [NAME]`
- All widget blocks exist as described in current skills

## Recommended Changes

### CRITICAL CHANGE 1: Delete T15.G3.10

**Skill to delete:**
- ID: T15.G3.10
- Skill: Enhanced say with styling
- Reason: Redundant - this is the ONLY say block that exists, so it should be taught in G3.04, not as an "enhancement"

**Dependencies to update:**
- T15.G3.11: Change dependency from G3.10 to G3.04
- T15.G3.05.01: Change dependency from G3.10 to new G3.04.01

### CRITICAL CHANGE 2: Restructure Say/Think Blocks

**Current problematic structure:**
```
G3.04: Say something (teaches non-existent basic block)
G3.05: Think bubble (teaches non-existent basic block)
G3.05.01: Style think bubbles
G3.10: Enhanced say with styling (redundant)
```

**Recommended new structure:**
```
G3.04: Display speech with say blocks
  └─ Teach the FULL styled say block from the start
  └─ Focus on basic usage with default colors

G3.04.01: Style speech bubbles for mood and emphasis (NEW)
  └─ Teach advanced styling techniques
  └─ Color psychology, text sizes for shouting/whispering

G3.05: Display thoughts with think blocks
  └─ Teach the FULL styled think block
  └─ Explain difference from say (cloud vs. tail)

G3.05.01: Style think bubbles (MODIFIED)
  └─ Update to reference G3.04.01 instead of G3.10
  └─ Teach thought-specific styling (transparency for daydreams)
```

**Skills to modify:**

**T15.G3.04:**
- Old Skill: "Say something"
- New Skill: "Display speech with say blocks"
- Old Description: "Use the `say [Hello] for (2) seconds` block to display text."
- New Description: "Use the `say [Hello!] for (2) seconds text size (16) [#FFFFFFFF] background [#000000FF] edge [#FFFFFFFF]` block to display text in speech bubbles. The parameters are: message text, duration in seconds, text size (number, e.g., 16 for normal, 24 for large), font color (hex code like #FFFFFFFF for white), background color (hex code like #FF0000FF for red), and edge/border color. Speech bubbles appear above the sprite and automatically disappear after the duration. Start with simple messages using default colors, then experiment with styling for different moods or emphasis."
- Dependencies: Keep as-is (T15.G3.01, T01.G3.01)

**NEW T15.G3.04.01:**
- Skill: "Style speech bubbles for mood and emphasis"
- Description: "Customize speech bubble appearance to convey emotions and emphasis. Use larger text size (24-32) for shouting or excitement, smaller size (12-14) for whispers. Use color psychology for backgrounds: red (#FF0000FF) for anger or alerts, blue (#0000FFFF) for calm or sad speech, yellow (#FFFF00FF) for cheerful dialogue, green (#00FF00FF) for positive affirmations, purple (#800080FF) for magical or mysterious speech. Use white text (#FFFFFFFF) on dark backgrounds for high contrast, or black text (#000000FF) on light backgrounds. Match edge color to background for subtle borders, or use contrasting edge colors for bold outlines."
- Dependencies: T15.G3.04

**T15.G3.05:**
- Old Skill: "Think bubble"
- New Skill: "Display thoughts with think blocks"
- Old Description: "Use the `think [Hmm...]` block to show internal monologue."
- New Description: "Use the `think [Hmm...] for (2) seconds text size (16) [#FFFFFFFF] background [#000000FF] edge [#FFFFFFFF]` block to show internal monologue in thought bubbles. Parameters work identically to say blocks: message text, duration, text size, font color, background color, and edge color. Think bubbles have a cloud-like appearance (vs. say bubbles which have a speech tail) to distinguish thoughts from spoken words. Use think for character reasoning, planning, or reactions that other characters should not hear."
- Dependencies: Keep as-is (T15.G3.04)

**T15.G3.05.01:**
- Keep current skill name and core description
- Update Dependencies: Remove "T15.G3.10", Add "T15.G3.04.01"
- New Dependencies: [T15.G3.05, T15.G3.04.01]

### CRITICAL CHANGE 3: Fix Foundation Chain

**Current problem:**
- T15.G3.01 (Change sprite position) depends on T15.G3.00.03 (Customize costumes in paint editor)
- This is illogical - sprite position has nothing to do with the paint editor

**Fix:**
- **T15.G3.01:** Remove dependency on T15.G3.00.03
- New Dependencies: [T01.G3.01]

**Reasoning:** Position is a fundamental concept that doesn't require paint editor knowledge.

### CRITICAL CHANGE 4: Break Down Widget Text Skills

**Current problem:**
- G3.11 and G3.12 each teach 4-5 concepts in one skill

**G3.11: Display labels for titles**
Split into:

**T15.G3.11: Create label widgets for persistent text** (MODIFIED)
- Skill: "Create label widgets for persistent text"
- Description: "Create label widgets using `add label [text] at X (0) Y (0) width (200) height (50) padding (10) as [title]` to display PERSISTENT text that stays on screen. Labels are UI widgets (not temporary like say blocks or printed text) that remain visible until explicitly hidden, removed, or the project stops. The padding parameter adds space between text and label edges (larger padding = more space). Position labels using X/Y coordinates: center of stage is (0, 0), top is positive Y, bottom is negative Y, right is positive X, left is negative X. Labels float above all sprites."
- Dependencies: Keep simplified reference to T15.G3.04

**NEW T15.G3.11.01: Position labels for titles and UI elements**
- Description: "Position labels at strategic screen locations for different purposes. Top center (X: 0, Y: 150) for main titles and headings, top left (X: -200, Y: 150) for scene identifiers or chapter numbers, top right (X: 200, Y: 150) for scores or status, bottom center (X: 0, Y: -150) for subtitles or instructions, bottom left (X: -200, Y: -150) for character name tags, bottom right (X: 200, Y: -150) for timer or level indicators. The stage typically ranges from X: -240 to 240 and Y: -180 to 180. Choose width and height that fit your text: short titles (width: 150-200), long titles (width: 300-400), single-line labels (height: 30-50), multi-line labels (height: 60-100)."
- Dependencies: [T15.G3.11]

**NEW T15.G3.11.02: Update label text for dynamic displays**
- Description: "Change label text while your project runs using `set value to [New Text] for widget [title v]`. This replaces all existing text in the label. Use this to update story titles when scenes change, display character names when speakers change, or show status messages. Combine with variables to show dynamic information: `set value to (join [Score: ] (score)) for widget [scoreLabel v]`. Update labels in response to events: `when I receive [NewScene]` → `set value to [Chapter 2] for widget [title v]`. Labels update instantly when you change their value."
- Dependencies: [T15.G3.11.01, T09.G3.01.04]

**G3.12: Print text at positions**
Split into:

**T15.G3.12: Print temporary text at positions** (MODIFIED)
- Skill: "Print temporary text at positions"
- Description: "Use `print [text] at x (0) y (0) width (300) height (100) color [#2CADE5FF]` to display TEMPORARY text directly on the stage at specific coordinates. Unlike labels (which are widgets), printed text is drawn as a layer on the stage and stays until cleared or the project stops. Printed text appears BELOW sprites and widgets in the layer order. The text wraps within the specified width and height. Use color parameter for text color (hex format #RRGGBBAA). Printed text is useful for annotations, floating labels, or temporary messages that should not be clickable UI elements."
- Dependencies: [Remove T15.G3.11]

**NEW T15.G3.12.01: Create timed and sprite-relative text**
- Description: "Use `print [text] at x (0) y (0) width (300) height (100) color [#2CADE5FF] for (2) seconds` to automatically hide text after a duration. This is useful for temporary notifications, damage numbers, or status effects. Create floating text near sprites by using sprite position variables: `print [Ouch!] at x (my x) y ((my y) + (50)) width (100) height (30) color [#FF0000FF] for (1) seconds` displays red text 50 pixels above the sprite for 1 second. The text stays at the printed position even if the sprite moves afterward (it is not attached to the sprite). Display multiple simultaneous texts at different positions for conversations or multiple events happening at once."
- Dependencies: [T15.G3.12]

**NEW T15.G3.12.02: Clear printed text for scene changes**
- Description: "Use `clear all my prints` to remove all printed text created by this sprite. This clears both timed and permanent printed text. Use this when scenes change to remove old text: `when I receive [NewScene]` → `clear all my prints`. Note that `clear all my prints` only removes text printed by the current sprite. If multiple sprites print text, each sprite must clear its own prints, or you can use a scene manager sprite that broadcasts a 'ClearAll' message that all sprites respond to by clearing their prints. Printed text is NOT automatically cleared when you hide a sprite - you must explicitly clear it."
- Dependencies: [T15.G3.12.01]

### CRITICAL CHANGE 5: Break Down Drawing Skills

**G5.09: Draw shapes on costumes with blocks**
Split into:

**T15.G5.09: Draw rectangles on vector costumes** (MODIFIED)
- Description: "Use `draw rectangle at x (0) y (0) width (200) height (100) fill [#6269F8FF] border [#20B755FF] width (1) corner radius (0) rotation (0)` to programmatically draw rectangles on the sprite's current vector costume when your code runs. Unlike the paint editor (manual design tool), this block draws shapes dynamically as scripts execute. The rectangle is positioned at (x, y) coordinates relative to the costume center. Fill color is the inside color, border color is the outline color, border width is outline thickness in pixels. Corner radius creates rounded corners (0 = sharp, 10+ = rounded). Rotation rotates the rectangle clockwise by degrees. The rectangle is drawn ON the costume (not on the stage), so it moves with the sprite."
- Dependencies: [T15.G3.00.03, T15.G5.01]

**NEW T15.G5.09.01: Draw ovals and circles on vector costumes**
- Description: "Use `draw oval at x (0) y (0) width (100) height (100) fill [#E2F9F2FF] border [#F44399FF] width (1) rotation (0)` to draw circles and ovals on vector costumes. When width equals height, you get a perfect circle. When width differs from height, you get an oval/ellipse. The position (x, y) is the center of the oval. Fill and border colors work the same as rectangles. Rotation rotates the oval clockwise by degrees (useful for tilted ovals). Combine rectangle and oval drawing in loops to create patterns: `repeat (10)` → `draw oval...` → `change x by (20)` creates a row of circles."
- Dependencies: [T15.G5.09]

**NEW T15.G5.09.02: Create dynamic visual effects with shape drawing**
- Description: "Use shape drawing in loops and with variables to create dynamic visual effects. Create health bars that change size: `draw rectangle at x (-100) y (150) width ((health) * (2)) height (20) fill [#00FF00FF]...` where health variable (0-100) controls bar length. Create status icons that appear/disappear: `if <(hasShield) = [true]>` → `draw oval at x (50) y (50) width (30) height (30) fill [#0000FFFF]...` for a shield indicator. Generate patterns in loops: `repeat (10)` with `draw rectangle at x ((i) * (30))...` creates evenly spaced rectangles. Use rotation in loops to create radial patterns: `repeat (12)` with `draw rectangle... rotation ((i) * (30))` creates a starburst."
- Dependencies: [T15.G5.09.01, T07.G3.01, T09.G3.02]

**G5.10: Draw lines and curves on costumes**
Split into:

**T15.G5.10: Draw straight lines on vector costumes** (MODIFIED)
- Description: "Use `draw line in [#386AF8FF] from x (0) y (0) to x (100) y (100) thickness (2)` to draw straight lines on vector costumes. The line goes from point (from x, from y) to point (to x, to y). Color is specified in hex format. Thickness is line width in pixels (1 = thin, 5+ = thick). Lines are useful for connecting objects, creating borders, drawing diagrams, or making custom shapes by combining multiple lines. Draw a square with 4 lines: line from (0,0) to (100,0), from (100,0) to (100,100), from (100,100) to (0,100), from (0,100) to (0,0). Draw a triangle with 3 lines connecting 3 points."
- Dependencies: [T15.G5.09]

**NEW T15.G5.10.01: Draw bezier curves on vector costumes**
- Description: "Use `draw curve in [#05DC6DFF] from x (20) y (20) to x (200) y (20) control 1 x (20) y (100) control 2 x (200) y (100) thickness (1)` to draw smooth curves using bezier math. The curve starts at (from x, from y) and ends at (to x, to y). Control points 1 and 2 shape the curve's bend - they act like invisible magnets pulling the curve toward them. To create a simple arc, place both control points above or below the line between start and end points. For S-curves, place control points on opposite sides. Experiment with control point positions to see how they affect curve shape. Curves are useful for smooth paths, decorative flourishes, or organic shapes."
- Dependencies: [T15.G5.10]

**NEW T15.G5.10.02: Draw text on vector costumes**
- Description: "Use `draw text [Hello] at x (0) y (0) size (24) color [#000000FF] rotation (0)` to draw text directly on vector costumes. Unlike `print` blocks (which display text on the stage layer), this draws text AS PART OF the costume itself. The text becomes permanent part of the costume until cleared. Position (x, y) is the text anchor point. Size is font size in pixels. Color is text color in hex format. Rotation tilts the text clockwise by degrees. Use for labeling costume elements, adding titles to procedurally generated images, or creating text-based visual effects. Draw text in loops to create repeating labels or artistic text patterns."
- Dependencies: [T15.G5.10.01]

**T15.G5.11: Clear programmatic drawings** (MODIFIED)
- Skill: "Clear all costume drawings"
- Description: "Use `clear all drawings` to remove ALL programmatic drawings (rectangles, ovals, lines, curves, text) from this sprite's current costume. This block only clears elements drawn with drawing blocks - it does NOT erase shapes manually created in the paint editor. Those paint editor shapes are permanent parts of the costume. Use `clear all drawings` at the start of scripts with `when green flag clicked` to reset costumes to their original state, or use with scene changes `when I receive [NewScene]` to clear old visual elements before drawing new ones. This allows you to create dynamic costumes that change throughout your story or animation."
- Dependencies: [T15.G5.10.02, T15.G3.12.02]

### CRITICAL CHANGE 6: Break Down Text-to-Speech

**T15.G5.12: Basic text-to-speech narration**
Split into:

**T15.G5.12: Basic text-to-speech with AI voices** (MODIFIED)
- Description: "Use `say [Hello everyone!] in [English (United States) v] as [Female v] speed (100) pitch (100) volume (100) store sound as []` to convert text to spoken audio using AI voices. This is DIFFERENT from regular say blocks - this block speaks the text aloud with synthesized speech, while regular say blocks just show text bubbles. The sprite will speak the text you provide. Leave 'store sound as' empty for now (advanced feature for saving audio). Speed, pitch, and volume are all set to 100 (normal) as a starting point. The block plays the speech and waits until it finishes before continuing to the next block in the script."
- Dependencies: [T15.G4.05, T15.G3.04]

**NEW T15.G5.12.01: Select languages and voice types for text-to-speech**
- Description: "Choose from 30+ languages including English (United States), English (United Kingdom), Spanish (Spain), Spanish (Mexico), French (France), Chinese (Mandarin, China), Japanese (Japan), German (Germany), Italian (Italy), Portuguese (Brazil), Russian (Russia), Korean (Korea), and many more. Each language has multiple voice types: Female, Male, Female2, Male2, Female3, Male3, Boy, and Girl. Not all voice types work in all languages - experiment to find available voices. Use different voices for different characters to create distinct personalities: Female for a princess, Male for a knight, Boy/Girl for children characters. Language selection allows creating bilingual or multilingual stories."
- Dependencies: [T15.G5.12]

**NEW T15.G5.12.02: Adjust speech characteristics for expression**
- Description: "Modify speed, pitch, and volume to create expressive speech. Speed (50-200): 50 is half speed (slow, careful), 100 is normal, 150 is fast (excited), 200 is very fast (rushed). Pitch (50-200): 50 is low pitch (deep voice, serious), 100 is normal, 150 is high pitch (cheerful, excited), 200 is very high (childlike, squeaky). Volume (0-200): 0 is silent, 50 is quiet (whisper), 100 is normal, 150 is loud, 200 is very loud (shouting). Combine adjustments for character personality: speed=80, pitch=70, volume=100 for a wise old character; speed=120, pitch=140, volume=110 for an energetic child. Test values to find the right expression for each character or mood."
- Dependencies: [T15.G5.12.01]

### CRITICAL CHANGE 7: Break Down Widget Styling

**T15.G5.13: Style widgets for stories**
Split into:

**T15.G5.13: Set widget background and border colors** (MODIFIED)
- Description: "Use `set widget background color [#FFFFFFFF] border color [#000000FF] border width (2) border radius (10) for [widgetName v]` to customize widget appearance. Colors use hex format #RRGGBBAA where RR=red (00-FF), GG=green (00-FF), BB=blue (00-FF), AA=alpha/transparency (FF=solid/100%, 80=50%, 00=invisible/0%). Border width is outline thickness in pixels (0=no border, 2=thin, 5=thick). Border radius creates rounded corners (0=sharp, 10=slightly rounded, 20+=very rounded). This block works on labels, buttons, textboxes, and most widgets."
- Dependencies: [T15.G4.06, T15.G3.11]

**NEW T15.G5.13.01: Format text inside widgets**
- Description: "Use `set text style [Arial v] font size (18) text color [#000000FF] boldness [bold v] text alignment [Center v] for [widgetName v]` to format text inside labels, buttons, and textboxes. Font options include Arial, Times New Roman, Courier, Georgia, Verdana, Comic Sans MS, and many more. Font size is in pixels (12=small, 18=medium, 24=large, 36+=very large). Text color uses hex format. Boldness can be [normal v] or [bold v]. Text alignment can be [Left v], [Center v], or [Right v]. Use larger fonts (24+) for titles and important buttons, smaller fonts (14-16) for descriptions, bold for emphasis, centered alignment for titles, left alignment for paragraphs."
- Dependencies: [T15.G5.13]

**NEW T15.G5.13.02: Create cohesive widget themes for story atmosphere**
- Description: "Match widget colors to story mood and create visual cohesion. For scary/dark scenes: dark background (#333333FF), red or orange text (#FF0000FF or #FFA500FF), thick red borders. For happy/bright scenes: light pastel backgrounds (#FFB6C1FF pink, #87CEEBFF sky blue), white or black text, thin borders. For fantasy/magical scenes: purple/blue backgrounds (#800080FF, #4B0082FF), gold text (#FFD700FF), glowing effects with bright borders. For nature scenes: green backgrounds (#228B22FF), brown text (#8B4513FF), organic rounded corners (border radius 15+). Apply consistent styling to all widgets in a scene so they feel unified. Change all widget styles when scenes change to reinforce the new atmosphere."
- Dependencies: [T15.G5.13.01]

### CRITICAL CHANGE 8: Break Down Scene Management

**T15.G4.02: Scene management with broadcasts**
Split into:

**T15.G4.02: Use broadcasts to trigger scene changes** (MODIFIED)
- Description: "Use `broadcast [Scene2]` to send scene change messages and `when I receive [Scene2]` to respond to them. Broadcasting is how you coordinate multiple sprites to create the illusion of changing locations or scenes. When you `broadcast [Scene2]`, ALL sprites with `when I receive [Scene2]` hat blocks will run their scripts simultaneously. This allows you to trigger many changes at once: some sprites show, some hide, some move, some change appearance. Each sprite decides how to respond to each scene. For example, Scene1 might show characters in a house, Scene2 might show them in a forest - different sprites respond by showing/hiding/moving to create each scene."
- Dependencies: [T15.G4.01, T15.G2.02]

**NEW T15.G4.02.01: Program sprite responses to scene broadcasts**
- Description: "In each sprite, add `when I receive [SceneName]` scripts that control how the sprite behaves in that scene. Use `show` to make the sprite visible in this scene, `hide` to make it invisible. Use `go to x: () y: ()` to position the sprite correctly for this scene. For example, a House sprite: `when I receive [Scene1]` → `show` + `go to x: (0) y: (-50)` (appears in Scene1), `when I receive [Scene2]` → `hide` (disappears in Scene2). A Character sprite might move between scenes: `when I receive [Scene1]` → `go to x: (-100) y: (0)` + `show`, `when I receive [Scene2]` → `go to x: (50) y: (0)` + `show`. Every sprite needs receive blocks for every scene where it appears or needs to do something."
- Dependencies: [T15.G4.02, T15.G4.03]

## Summary of Changes

### Skills to Delete
1. **T15.G3.10**: Enhanced say with styling (redundant)

### Skills to Add (14 new)
1. **T15.G3.04.01**: Style speech bubbles for mood and emphasis
2. **T15.G3.11.01**: Position labels for titles and UI elements
3. **T15.G3.11.02**: Update label text for dynamic displays
4. **T15.G3.12.01**: Create timed and sprite-relative text
5. **T15.G3.12.02**: Clear printed text for scene changes
6. **T15.G4.02.01**: Program sprite responses to scene broadcasts
7. **T15.G5.09.01**: Draw ovals and circles on vector costumes
8. **T15.G5.09.02**: Create dynamic visual effects with shape drawing
9. **T15.G5.10.01**: Draw bezier curves on vector costumes
10. **T15.G5.10.02**: Draw text on vector costumes
11. **T15.G5.12.01**: Select languages and voice types for text-to-speech
12. **T15.G5.12.02**: Adjust speech characteristics for expression
13. **T15.G5.13.01**: Format text inside widgets
14. **T15.G5.13.02**: Create cohesive widget themes for story atmosphere

### Skills to Modify (9 existing)
1. **T15.G3.01**: Remove dependency on G3.00.03
2. **T15.G3.04**: Update to teach styled say block from the start
3. **T15.G3.05**: Update to teach styled think block from the start
4. **T15.G3.05.01**: Update dependencies (remove G3.10, add G3.04.01)
5. **T15.G3.11**: Simplify to focus on widget creation
6. **T15.G3.12**: Simplify to focus on print basics
7. **T15.G4.02**: Simplify to focus on broadcast mechanism
8. **T15.G5.09**: Focus on rectangles only
9. **T15.G5.10**: Focus on straight lines only
10. **T15.G5.11**: Update dependencies and clarify
11. **T15.G5.12**: Simplify to basic TTS usage
12. **T15.G5.13**: Focus on colors and borders

### Dependency Changes
1. T15.G3.01: Remove T15.G3.00.03 dependency
2. T15.G3.05.01: Replace T15.G3.10 with T15.G3.04.01
3. T15.G3.11: Update to reference T15.G3.04 instead of T15.G3.10
4. T15.G5.11: Add T15.G5.10.02 and T15.G3.12.02 dependencies
5. All skills referencing G3.10: Update to G3.04 or G3.04.01

## Restructured Sections - Visual Diagrams

### 1. Say/Think Blocks (G3.04-G3.05.01)

```
BEFORE:
  G3.04: Say something (basic - WRONG BLOCK)
  G3.05: Think bubble (basic - WRONG BLOCK)
  G3.05.01: Style think bubbles
  G3.10: Enhanced say with styling (DELETED - redundant)

AFTER:
  G3.04: Display speech with say blocks (FULL styled block)
    └─ G3.04.01: Style speech bubbles for mood and emphasis (NEW)
  G3.05: Display thoughts with think blocks (FULL styled block)
    └─ G3.05.01: Style think bubbles (updated dependencies)
```

### 2. Widget Text Skills (G3.11-G3.12)

```
BEFORE:
  G3.11: Display labels for titles (5 concepts in 1 skill)
  G3.12: Print text at positions (4 concepts in 1 skill)

AFTER:
  G3.11: Create label widgets for persistent text
    ├─ G3.11.01: Position labels for titles and UI elements (NEW)
    └─ G3.11.02: Update label text for dynamic displays (NEW)

  G3.12: Print temporary text at positions
    ├─ G3.12.01: Create timed and sprite-relative text (NEW)
    └─ G3.12.02: Clear printed text for scene changes (NEW)
```

### 3. Drawing Skills (G5.09-G5.11)

```
BEFORE:
  G5.09: Draw shapes on costumes (rectangle + oval together)
  G5.10: Draw lines and curves (line + curve + text together)
  G5.11: Clear programmatic drawings

AFTER:
  G5.09: Draw rectangles on vector costumes
    ├─ G5.09.01: Draw ovals and circles (NEW)
    └─ G5.09.02: Create dynamic visual effects (NEW)

  G5.10: Draw straight lines on vector costumes
    ├─ G5.10.01: Draw bezier curves (NEW)
    └─ G5.10.02: Draw text on vector costumes (NEW)

  G5.11: Clear all costume drawings (updated)
```

### 4. Text-to-Speech (G5.12)

```
BEFORE:
  G5.12: Basic text-to-speech narration (all TTS features)

AFTER:
  G5.12: Basic text-to-speech with AI voices
    ├─ G5.12.01: Select languages and voice types (NEW)
    └─ G5.12.02: Adjust speech characteristics (NEW)
```

### 5. Widget Styling (G5.13)

```
BEFORE:
  G5.13: Style widgets for stories (all styling features)

AFTER:
  G5.13: Set widget background and border colors
    ├─ G5.13.01: Format text inside widgets (NEW)
    └─ G5.13.02: Create cohesive widget themes (NEW)
```

### 6. Scene Management (G4.02)

```
BEFORE:
  G4.02: Scene management with broadcasts (complex)

AFTER:
  G4.02: Use broadcasts to trigger scene changes
    └─ G4.02.01: Program sprite responses to scene broadcasts (NEW)
```

## Key Improvements

1. **Foundation Chain Fixed**: Removed illogical dependency from G3.01 (position) on G3.00.03 (paint editor)

2. **Say/Think Restructured**: Now teaches the actual blocks that exist (styled versions), eliminating the misconception that basic versions exist

3. **Progressive Complexity**: Each major skill now broken into 2-3 focused sub-skills that build on each other

4. **One Concept Per Skill**: Each skill teaches exactly one implementable concept that students can complete

5. **Clear Layer Understanding**: Better explained distinction between widgets (top), sprites (middle), printed text (below sprites)

6. **Practical Applications**: Added skills focused on using features for story purposes (mood theming, expression, atmosphere)

7. **Verified Against Actual Blocks**: All skills now reference blocks that actually exist in CreatiCode

## Verification Checklist

- [x] All skills verified against actual CreatiCode blocks in blockdes8.txt
- [x] No skills reference non-existent blocks (switch costume, graphic effects)
- [x] No circular dependencies within T15
- [x] X-2 rule followed (dependencies only at X, X-1, X-2 grades)
- [x] Cross-topic dependencies preserved (T01-T14, T16-T20)
- [x] All new skills have proper dependency chains
- [x] Removed unnecessary same-grade dependencies where possible
- [x] Each skill teaches one focused, implementable concept

## Implementation Notes

1. **Order Matters**: Implement deletions first, then modifications, then additions to avoid ID conflicts

2. **Dependency Updates**: After deleting G3.10, search for ALL references and update them:
   - G3.11 dependency
   - G3.05.01 dependency
   - Any other skills that reference G3.10

3. **Testing**: After implementation, verify that:
   - All skill IDs are unique
   - All dependencies reference existing skills
   - No orphaned skills (skills with no path from foundation)
   - Skill count matches expected (83 total)

4. **Documentation**: Update any external documentation that references deleted or modified skill IDs

## Estimated Impact

**Before Optimization:**
- 70 skills total
- Several skills teach non-existent blocks
- Some skills pack 4-5 concepts into one
- Illogical dependency chain

**After Optimization:**
- 83 skills total (+13 skills, +19%)
- All skills verified against actual blocks
- Maximum 2-3 concepts per skill family
- Logical, clean dependency chains
- Better progressive learning path

**Student Benefits:**
- Clearer learning path (one concept at a time)
- More achievable milestones (shorter skills)
- Better understanding of layer system
- Practical styling and theming skills
- Correct mental models from the start

## Next Steps

1. Review and approve this optimization plan
2. Implement changes in order: delete → modify → add
3. Update all dependency references
4. Verify no broken dependencies
5. Test sample learning paths through T15
6. Update any related documentation or curriculum materials

---

**End of Optimization Summary**
