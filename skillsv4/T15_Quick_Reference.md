# T15 (Stories & Animation) - Quick Reference Guide

## Critical Issues Summary

### Block Syntax Errors (FIX IMMEDIATELY)
1. **T15.G3.10**: Wrong syntax for styled say blocks → See Implementation doc for correct syntax
2. **T15.G3.05.01**: Wrong syntax for styled think blocks → See Implementation doc for correct syntax

### Major Gaps (ADD SKILLS)
1. **Text-to-Speech**: Missing foundational TTS skill before G6 → Add T15.G5.12
2. **Speech Recognition**: Missing basic skill before G6 → Add T15.G6.05, renumber G6.05→G6.06
3. **Programmatic Drawing**: Confusion between paint editor and draw blocks → Modify G5.09, G5.10, add G5.11
4. **Broadcast and Wait**: Referenced but never taught → Add T15.G5.02.01
5. **Glide Blocks**: Mentioned but not explicitly taught → Add T15.G3.01.01

### Medium Priority
- Widget enhancements (styling, dropdowns, rich text, sliders) - 4 new skills
- Scene manager improvements (widget visibility) - modify T15.G7.01
- String parsing scaffolding (split text) - add T15.G7.03.01
- Save/load details (cloud variables) - modify T15.G8.03, T15.G8.03.01

---

## Platform Features Verified

### Speech/Dialogue Blocks ✓
- `say [TEXT] for (T) seconds text size (FONTSIZE) [FONTCOLOR] background [BACKGROUNDCOLOR] edge [EDGECOLOR]`
- `think [TEXT] for (T) seconds text size (FONTSIZE) [FONTCOLOR] background [BACKGROUNDCOLOR] edge [EDGECOLOR]`

### Text-to-Speech ✓
- `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]`
- 30+ languages, 8 voice types (Male, Female, Male2, Female2, Male3, Female3, Boy, Girl)

### Speech Recognition ✓
- `start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]` (Azure)
- `OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]` (Whisper)
- `end speech recognition`
- `(text from speech)` reporter

### Print Text ✓
- `print [TEXT] at x (XPOS) y (YPOS) width (W) height (H) color [FONTCOLOR]`
- `print [TEXT] at x (XPOS) y (YPOS) width (W) height (H) color [FONTCOLOR] for (T) seconds`
- `clear all my prints`
- `clear all prints`

### Drawing Blocks ✓
- `draw rectangle at x (XPOS) y (YPOS) width (W) height (H) fill [FILLCOLOR] border [BORDERCOLOR] width (BORDERWIDTH) corner radius (CORNERRADIUS) rotation (N)`
- `draw oval at x (XPOS) y (YPOS) width (W) height (H) fill [FILLCOLOR] border [BORDERCOLOR] width (BORDERWIDTH) rotation (N)`
- `draw line in [LINECOLOR] from x (FROMX) y (FROMY) to x (TOX) y (TOY) thickness (THICKNESS)`
- `draw curve in [LINECOLOR] from x (FROMX) y (FROMY) to x (TOX) y (TOY) control 1 x (CONTROLX1) y (CONTROLY1) control 2 x (CONTROLX2) y (CONTROLY2) thickness (THICKNESS)`

### Widgets ✓
- Labels: `add label at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (P) as [NAME]`
- Buttons: `add button at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (P) as [NAME]`
- Textboxes: `add textbox at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (P) line [single/multiple v] scroll [scroll/no scroll v] mode [read only/input v] as [NAME]`
- Rich textboxes: `add rich textbox at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (P) mode [read only/input v] as [NAME]`
- Dropdown menus: `add dropdown menu at X (X) Y (Y) width (WIDTH) height (HEIGHT) from list [LISTNAME v] as [NAME]`
- Sliders: `add slider at X (X) Y (Y) width (WIDTH) min (MIN) max (MAX) as [NAME]`
- Camera: `add camera widget at X (X) Y (Y) width (WIDTH) height (HEIGHT) from [front/back v] mode [normal/flipped v] as [NAME]`
- `(value of widget [WIDGETNAME v])` reporter
- `set value to [V] for widget [WIDGETNAME v]`
- `when widget [NAME v] clicked` hat block
- `when widget [NAME v] changes` hat block
- Widget styling: `set widget background color [BACKGROUNDCOLOR] border color [BORDERCOLOR] border width (BORDERWIDTH) border radius (BORDERRADIUS) for [WIDGETNAME v]`
- Text styling: `set text style [FONTSTYLE v] font size (FONTSIZE) text color [TEXTCOLOR] boldness [BOLDNESS v] text alignment [TEXTALIGNMENT v] for [WIDGETNAME v]`

### 3D Speech Bubbles ✓
- `show speech bubble [TEXT] offset xyz (X) (Y) (Z) max width (W) text font [FONTNAME v] size (FONTSIZE) color [FONTCOLOR] background [BGCOLOR] for [T] seconds camera facing [ISCAMERAFACING v] ID [BUBBLEID v]`

### Movement ✓
- `glide (T) secs to x: (XPOS) y: (YPOS)`
- `go to x: (XPOS) y: (YPOS)`

---

## New Skills to Add (15-17 total)

### Grade 3
1. **T15.G3.01.01**: Smooth movement with glide

### Grade 5
1. **T15.G5.11**: Clear programmatic drawings
2. **T15.G5.12**: Basic text-to-speech narration ⭐ CRITICAL
3. **T15.G5.13**: Style widgets for stories
4. **T15.G5.14**: Dropdown menus for story choices
5. **T15.G5.15**: Calculate animation timing
6. **T15.G5.02.01**: Sequential actions with broadcast and wait

### Grade 6
1. **T15.G6.05**: Basic speech recognition input ⭐ CRITICAL (renumber current G6.05→G6.06)
2. **T15.G6.07**: Rich text story displays
3. **T15.G6.08**: Visual stat tracking with sliders

### Grade 7
1. **T15.G7.03.01**: Split text at delimiter
2. **T15.G7.04**: Generate backgrounds with AI (IF PLATFORM SUPPORTS - verify first)

### Grade 8
1. **T15.G8.04**: 3D speech bubbles in space
2. **T15.G8.05**: Interactive camera stories

---

## Skills to Modify (11 total)

### Grade 3
1. **T15.G3.00.03**: Clarify paint editor vs blocks ⭐ HIGH
2. **T15.G3.05.01**: Fix think block syntax ⭐ CRITICAL
3. **T15.G3.10**: Fix say block syntax ⭐ CRITICAL
4. **T15.G3.11**: Clarify persistent labels
5. **T15.G3.12**: Add clear prints, clarify temporary vs persistent

### Grade 5
1. **T15.G5.04**: Add text layering explanation
2. **T15.G5.09**: Change to programmatic drawing blocks ⭐ HIGH
3. **T15.G5.10**: Change to lines/curves (was "draw text") ⭐ HIGH

### Grade 6
1. **T15.G6.03**: Add broadcast-and-wait dependency
2. **T15.G6.04**: Expand multi-language TTS details ⭐ HIGH

### Grade 7
1. **T15.G7.01**: Add widget hide/show
2. **T15.G7.03**: Add string parsing details or prerequisite

### Grade 8
1. **T15.G8.03**: Specify save location (cloud variables)
2. **T15.G8.03.01**: Specify load source

---

## Skills to Reorder (2 skills)

Move in G3:
- **T15.G3.10** (Enhanced say) → AFTER T15.G3.08 (Click to talk)
- **T15.G3.05.01** (Style think) → AFTER new T15.G3.10 position

**Reason**: Students should practice basic dialogue before learning advanced styling.

New G3 order:
1. G3.04: Say something
2. G3.05: Think bubble
3. G3.06: Sequence dialogue
4. G3.07: Wait between actions
5. G3.08: Click to talk
6. G3.09: Key press animation
7. **G3.10: Enhanced say with styling** ⬅️ MOVED
8. **G3.11: Style think bubbles** ⬅️ MOVED (was G3.05.01)
9. G3.12: Display labels (was G3.11)
10. G3.13: Print text at positions (was G3.12)

---

## Dependencies to Verify

Check these skills exist in other topics before referencing:

### T09 (Variables)
- [ ] **T09.G7.01**: Cloud variables - needed by T15.G8.03

### T12 (Text/Strings)
- [ ] **T12.G4.01** or **T12.G5.01**: Letter operations, string extraction - needed by T15.G5.06, T15.G7.03.01

### T14 (AI & Data)
- [ ] **T14.G5.01**: Understanding AI services - should be dependency for T15.G5.12, T15.G6.05
- [ ] **T14.G6.01**: AI creative generation - needed by T15.G7.04 (if that feature exists)

### T16 (User Interfaces)
- [ ] **T16.G4.03**: Hide and show widgets - needed by T15.G7.01
- [ ] **T16.G5.05**: Rich textboxes - needed by T15.G6.07
- [ ] **T16.G6.01**: Camera widgets - needed by T15.G8.05

### T17 (3D Graphics)
- [ ] **T17.G7.01**: 3D sprite basics - needed by T15.G8.04

**Action**: If any are missing, either:
1. Add them to the respective topic first, OR
2. Remove the dependency and adjust T15 skill description

---

## Implementation Phases

### PHASE 1 (DO FIRST) - Critical Fixes
Priority: ⭐⭐⭐⭐⭐ HIGH
Estimated time: 2-3 hours

- [ ] Fix T15.G3.10 block syntax
- [ ] Fix T15.G3.05.01 block syntax
- [ ] Add T15.G5.12 (basic TTS)
- [ ] Modify T15.G6.04 (multi-language TTS)
- [ ] Add T15.G6.05 (basic speech recognition)
- [ ] Renumber current T15.G6.05 to T15.G6.06
- [ ] Clarify T15.G3.00.03 (paint editor)
- [ ] Modify T15.G5.09 (programmatic drawing)
- [ ] Modify T15.G5.10 (lines/curves)

**Impact**: Fixes incorrect documentation that would confuse students

---

### PHASE 2 - Scaffolding
Priority: ⭐⭐⭐⭐ MEDIUM-HIGH
Estimated time: 2 hours

- [ ] Add T15.G3.01.01 (glide)
- [ ] Add T15.G5.02.01 (broadcast and wait)
- [ ] Add T15.G5.11 (clear prints)
- [ ] Modify T15.G6.03 (add dependency)
- [ ] Reorder T15.G3.10 and T15.G3.05.01
- [ ] Modify T15.G3.11 (clarify labels)
- [ ] Modify T15.G3.12 (clarify prints)
- [ ] Modify T15.G5.04 (layering)

**Impact**: Fills critical gaps in learning progression

---

### PHASE 3 - Widget Enhancements
Priority: ⭐⭐⭐ MEDIUM
Estimated time: 2-3 hours

- [ ] Add T15.G5.13 (widget styling)
- [ ] Add T15.G5.14 (dropdown menus)
- [ ] Add T15.G6.07 (rich textboxes)
- [ ] Add T15.G6.08 (sliders)
- [ ] Modify T15.G7.01 (scene manager with widgets)

**Impact**: Leverages underutilized platform features

---

### PHASE 4 - Advanced Features
Priority: ⭐⭐ LOW-MEDIUM
Estimated time: 2-3 hours

- [ ] Add T15.G5.15 (animation timing)
- [ ] Add T15.G7.03.01 (split text)
- [ ] Modify T15.G7.03 (dialogue parsing)
- [ ] Modify T15.G8.03 (save with details)
- [ ] Modify T15.G8.03.01 (load with details)
- [ ] Add T15.G8.04 (3D speech bubbles)
- [ ] Add T15.G8.05 (camera stories)
- [ ] Add T15.G7.04 (AI backgrounds - IF SUPPORTED)

**Impact**: Enables advanced storytelling techniques

---

## Testing Checklist

After implementation, verify:

### Syntax Accuracy
- [ ] All block syntax matches blockdes8.txt exactly
- [ ] Parameter names are correct
- [ ] Dropdown options are accurate

### Scaffolding
- [ ] Each new skill has clear prerequisites
- [ ] No jumps in complexity without intermediate steps
- [ ] Dependencies follow X-2 rule

### Platform Features
- [ ] All mentioned blocks exist in CreatiCode
- [ ] No references to non-existent features
- [ ] Widget types match actual platform

### Progression
- [ ] K-2 skills are picture-based (no coding)
- [ ] G3+ skills involve block coding
- [ ] Complexity increases gradually

### Cross-Topic Dependencies
- [ ] All referenced T09, T12, T14, T16, T17 skills exist
- [ ] Or alternative dependencies provided

---

## Quick Stats

**Before optimization:**
- Total skills: 61
- K-2: 9 (picture-based) ✓
- G3-8: 52 (block coding)

**After optimization:**
- Total skills: ~76-78
- K-2: 9 (unchanged)
- G3: 17 (+1)
- G4: 8 (unchanged)
- G5: 15 (+5)
- G6: 9 (+4)
- G7: 5 (+2)
- G8: 11 (+5)

**Changes:**
- Skills added: 15-17
- Skills modified: 11
- Skills removed: 0
- Skills reordered: 2

**Expansion**: ~25% (reasonable given underutilized features)

---

## File Locations

1. **Full Analysis**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T15_Analysis_Report.md`
   - Detailed issue breakdown
   - Platform capability verification
   - Dependency analysis

2. **Implementation Guide**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T15_Implementation_Solutions.md`
   - Exact skill definitions ready to copy
   - Before/after comparisons
   - Dependency specifications

3. **Quick Reference**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T15_Quick_Reference.md` (this file)
   - Summary of changes
   - Implementation phases
   - Testing checklist

---

## Contact / Questions

If you encounter issues during implementation:

1. **Block syntax questions**: Reference `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`
2. **Dependency questions**: Check the dependency graph tool
3. **Platform features**: Test in CreatiCode editor to confirm existence
4. **Progression questions**: Review similar topics (T16 UI, T14 AI) for patterns

---

End of Quick Reference
