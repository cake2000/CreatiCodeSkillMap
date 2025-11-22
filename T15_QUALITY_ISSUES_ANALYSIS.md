# T15 (Stories & Animation) - Quality Issues Analysis
**Date:** 2025-11-22
**Topic:** T15 - Stories & Animation
**Total Skills:** 47 skills (K-8)
**Analysis Focus:** CreatiCode feature accuracy, skill quality, scaffolding, dependencies, grade appropriateness

---

## EXECUTIVE SUMMARY

### Overall Assessment
T15 skills have **CRITICAL ACCURACY ISSUES** due to fundamental misalignment with CreatiCode's platform capabilities. The topic extensively references standard Scratch blocks that DO NOT EXIST in CreatiCode.

### Critical Findings:
- **11 HIGH PRIORITY ISSUES** - Skills reference non-existent blocks (costume/backdrop switching, graphic effects)
- **8 MEDIUM PRIORITY ISSUES** - Missing skills for CreatiCode-unique features, skill quality problems
- **6 LOW PRIORITY ISSUES** - Dependency and scaffolding concerns
- **Platform Misalignment:** ~40% of Grade 3-5 skills reference unavailable features

### Required Actions:
1. **REMOVE or REPLACE** all skills referencing non-existent blocks
2. **ADD NEW SKILLS** for CreatiCode's unique animation features (styled say/think, fade gradually, widgets, TTS)
3. **FIX DEPENDENCIES** to remove references to deleted skills
4. **ENHANCE SCAFFOLDING** for story-building progression

---

## CATEGORY 1: PLATFORM ACCURACY ISSUES (CRITICAL)

### ISSUE-ACC-001: NON-EXISTENT COSTUME SWITCHING BLOCKS
**Priority:** HIGH (CRITICAL)
**Skills Affected:** T15.G3.01, T15.G3.02, T15.G4.01, T15.G4.02

**Problem:**
CreatiCode **DOES NOT HAVE** these standard Scratch blocks:
- ❌ `switch costume to [Costume B]`
- ❌ `next costume`
- ❌ `costume number`
- ❌ `switch costume to (1)` (by number)

**Current State - T15.G3.01:**
```yaml
Description: "Use `switch costume to [Costume B]` to change a sprite's appearance."
Challenge: "when clicked -> switch costume to [Happy]"
```

**Current State - T15.G3.02:**
```yaml
Description: "Use `next costume` inside a `repeat` loop to create a simple animation cycle."
Challenge: "repeat (10) -> next costume, wait (0.1) secs"
```

**Current State - T15.G4.02:**
```yaml
Description: "Use costume numbers to switch costumes (e.g., `switch costume to (1)`)"
```

**CreatiCode Reality:**
CreatiCode provides:
- ✅ `add costume from URL [URL] name [NAME]` - Add costumes dynamically
- ✅ No built-in costume switching blocks
- ✅ Students must manage costume display through other means (hiding/showing sprites, using different sprites per costume)

**Recommended Action:**
```
ACTION: DELETE T15.G3.01, T15.G3.02, T15.G4.02 entirely
REASON: Core functionality does not exist in CreatiCode
REPLACEMENT: Add new skills for CreatiCode's actual costume management
```

**Replacement Skills Needed:**
```yaml
T15.G4.NEW1 - Add costume from URL:
  description: "Students add costumes to sprites dynamically using 'add costume from URL [URL] name [NAME]'. They learn to import images from the web to create character variations."
  challenge: "Build: add costume from URL [https://...] name [happy_face]"
  CSTA: 1B-AP-10
  dependencies: [T06.G3.01, T14.G3.03]

T15.G5.NEW2 - Multi-sprite character states:
  description: "Students create character state changes by using multiple sprites with hide/show, rather than costume switching. Each 'costume' becomes a separate sprite that appears/disappears."
  challenge: "Debug: Character states overlap. Fix visibility logic."
  CSTA: 1B-AP-10
  dependencies: [T15.G4.04, T06.G3.08]
```

**Impact:** CRITICAL - Affects progression of entire animation strand

---

### ISSUE-ACC-002: NON-EXISTENT BACKDROP SWITCHING BLOCKS
**Priority:** HIGH (CRITICAL)
**Skills Affected:** T15.G4.03, T15.G4.04

**Problem:**
CreatiCode **DOES NOT HAVE** these standard Scratch blocks:
- ❌ `switch backdrop to [Next Scene]`
- ❌ `next backdrop`
- ❌ `when backdrop switches to [Scene 2]`

**Current State - T15.G4.03:**
```yaml
Description: "Use `switch backdrop to [Next Scene]` to change the setting."
Challenge: "say [Let's go outside], switch backdrop to [Outdoors]"
```

**Current State - T15.G4.04:**
```yaml
Description: "Use `hide` and `show` to control which characters appear in which scene."
Challenge: "when backdrop switches to [Scene 2] -> show"
```

**CreatiCode Reality:**
CreatiCode provides:
- ✅ Drawing blocks: `draw rectangle`, `draw oval`, `draw text` on stage
- ✅ Image widgets: Can add background images via widgets
- ✅ Stage mode control: `set stage mode to [MODE]` (fullscreen, presentation, etc.)
- ❌ No backdrop switching system

**Recommended Action:**
```
ACTION: DELETE T15.G4.03 entirely, MODIFY T15.G4.04
REASON: Backdrop switching does not exist; hide/show works but needs different trigger
```

**Replacement Skills Needed:**
```yaml
T15.G4.NEW3 - Scene changes with broadcasts:
  description: "Students create scene changes using broadcasts to hide/show sprites and redraw backgrounds using drawing blocks. They coordinate multiple sprites to create scene transitions."
  challenge: "Build: broadcast [Scene2] -> all sprites respond by hiding/showing/moving"
  CSTA: 1B-AP-15
  dependencies: [T06.G3.01, T15.G4.04-MODIFIED]

T15.G4.04-MODIFIED - Hide and Show characters (revised):
  old_description: "Use `hide` and `show` to control which characters appear in which scene."
  new_description: "Use `hide` and `show` to control sprite visibility. Students learn to make characters appear and disappear using event triggers like broadcasts or green flag."
  old_challenge: "when backdrop switches to [Scene 2] -> show"
  new_challenge: "when I receive [enter scene] -> show, when I receive [exit scene] -> hide"
  CSTA: 1B-AP-10
```

**Impact:** CRITICAL - Affects scene management system

---

### ISSUE-ACC-003: NON-EXISTENT GRAPHIC EFFECTS BLOCKS
**Priority:** HIGH (CRITICAL)
**Skills Affected:** T15.G4.01

**Problem:**
CreatiCode **DOES NOT HAVE** standard Scratch graphic effects:
- ❌ `change [ghost] effect by (10)`
- ❌ `set [ghost] effect to (50)`
- ❌ `change [color] effect by (25)`
- ❌ `clear graphic effects`

**Current State - T15.G4.01:**
```yaml
Description: "Use `change [ghost] effect` or `change size` to animate appearance (e.g., fading out, growing)."
Challenge: "repeat (10) -> change [ghost] effect by (10)"
```

**CreatiCode Reality:**
CreatiCode provides:
- ✅ `[fade/reveal v] sprite gradually in (T) seconds` - Gradual fade/reveal effect
- ✅ `change size by (N)` - Size changes (this works!)
- ✅ No ghost/color/fisheye/whirl/pixelate/mosaic/brightness effects

**Recommended Action:**
```
ACTION: REPLACE T15.G4.01 with CreatiCode's gradual effects
REASON: Ghost effect doesn't exist, but fade gradually does
```

**Replacement Skill:**
```yaml
T15.G4.01-REVISED - Animate with gradual effects:
  old_description: "Use `change [ghost] effect` or `change size` to animate appearance (e.g., fading out, growing)."
  new_description: "Use `[fade/reveal] sprite gradually in (T) seconds` or `change size by (N)` to animate appearance. Students create smooth transitions by fading sprites in/out or changing their size."
  old_challenge: "repeat (10) -> change [ghost] effect by (10)"
  new_challenge: "fade sprite gradually in (2) seconds OR repeat (10) -> change size by (10), wait (0.1) secs"
  block_syntax: "[ACTION v] sprite gradually in (T) seconds where ACTION = fade or reveal"
  CSTA: 1B-AP-10
```

**Impact:** HIGH - Affects one skill, easy to fix with correct block

---

### ISSUE-ACC-004: MISSING CREATICODE-UNIQUE STYLED SAY/THINK BLOCKS
**Priority:** MEDIUM
**Skills Affected:** T15.G3.04, T15.G3.05 (missing enhancement)

**Problem:**
Current skills teach basic say/think but **IGNORE** CreatiCode's powerful styling features.

**Current State - T15.G3.04:**
```yaml
Description: "Use the `say [Hello] for (2) seconds` block to display text."
Challenge: "say [Welcome!] for (2) secs"
```

**CreatiCode Reality:**
```
Block ID: looks_sayforsecs_withstyle
Syntax: say [TEXT] for (T) seconds text size (FONTSIZE) [FONTCOLOR] background [BACKGROUNDCOLOR] edge [EDGECOLOR]
Usage: say [Hi] for (3) seconds text size (16) [#FFFFFFFF] background [#000000FF] edge [#FFFFFFFF]

Block ID: looks_thinkforsecs_withstyle
Syntax: think [TEXT] for (T) seconds text size (FONTSIZE) [FONTCOLOR] background [BACKGROUNDCOLOR] edge [EDGECOLOR]
```

**Key Features:**
- Customizable font size, text color, background color, edge color
- If T is empty or 0, bubble stays visible indefinitely
- More powerful than standard Scratch

**Recommended Action:**
```
ACTION: KEEP existing basic skills, ADD new advanced styling skills
REASON: Progressive scaffolding - basic first, styling later
```

**New Skills Needed:**
```yaml
T15.G5.NEW3 - Style speech bubbles:
  description: "Students customize speech bubbles using CreatiCode's styled say block with text size, colors, and backgrounds. They make dialogue visually distinct for different characters."
  challenge: "Build: say [Hi!] for (2) seconds text size (20) [#FF0000] background [#FFFF00] edge [#000000]"
  syntax: "say [TEXT] for (T) seconds text size (SIZE) [TEXTCOLOR] background [BGCOLOR] edge [EDGECOLOR]"
  CSTA: 1B-AP-10
  dependencies: [T15.G3.04, T15.G3.05]

T15.G5.NEW4 - Persistent bubbles:
  description: "Students create speech or thought bubbles that stay visible indefinitely by leaving the time parameter empty. They learn when to use timed vs. persistent dialogue."
  challenge: "Modify: Change timed dialogue to persistent, add clear mechanism"
  CSTA: 1B-AP-10
  dependencies: [T15.G3.04, T15.G3.05]
```

**Impact:** MEDIUM - Misses opportunity to teach CreatiCode-unique features

---

### ISSUE-ACC-005: NO INFINITE SAY/THINK BLOCKS IN STANDARD SCRATCH SENSE
**Priority:** LOW
**Skills Affected:** None directly, but context important

**CreatiCode Reality:**
- Standard Scratch has: `say [Hello]` (infinite) and `say [Hello] for (2) secs` (timed)
- CreatiCode has: `say [TEXT] for (T) seconds ...` where T=0 or empty means infinite
- This is actually BETTER - one block, dual purpose

**Recommended Action:**
```
ACTION: Document this difference in skill descriptions
REASON: Helps educators understand CreatiCode's streamlined approach
```

**Impact:** LOW - Documentation/clarification only

---

### ISSUE-ACC-006: MISSING TEXT-TO-SPEECH INTEGRATION
**Priority:** MEDIUM
**Skills Affected:** T15.G8.02 (accessibility), entire topic missing TTS

**Problem:**
T15 completely ignores CreatiCode's powerful AI text-to-speech capabilities for storytelling.

**Current State - T15.G8.02:**
```yaml
Description: "Implement features like text-to-speech (for blind users) or subtitles (for sound) to make stories accessible."
Challenge: "Modify. Add TTS blocks to existing text."
```

**CreatiCode Reality:**
```
Block ID: ai_speakinlanguage
Syntax: say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]
API: Microsoft Azure Text-to-Speech
Languages: 50+ languages
Voice Types: Male, Female, Male2, Female2, Male3, Female3, Boy, Girl
Customization: Speed, pitch, volume percentages
```

**Current Gap:**
- No skills teach TTS for character voices
- No skills teach multi-language storytelling
- No skills teach voice customization (pitch, speed)
- T15.G8.02 mentions TTS but provides no scaffolding

**Recommended Action:**
```
ACTION: ADD comprehensive TTS skill progression
REASON: TTS is perfect for storytelling and accessibility
```

**New Skills Needed:**
```yaml
T15.G5.NEW5 - Basic text-to-speech:
  description: "Students use AI text-to-speech to give characters voices. They learn to convert dialogue text to spoken audio using say [TEXT] in [LANGUAGE] as [VOICETYPE]."
  challenge: "Build: say [Hello, I am a robot!] in [English (United States)] as [Male]"
  CSTA: 1B-AP-10
  dependencies: [T15.G3.04, T06.G4.01]

T15.G6.NEW6 - Customize character voices:
  description: "Students customize character voices using speed, pitch, and volume parameters. Different characters get distinct voice personalities (fast/high for excited, slow/low for serious)."
  challenge: "Build: Create 2 characters with contrasting voices (speed/pitch)"
  syntax: "say [TEXT] in [LANG v] as [VOICE v] speed (SPEED) pitch (PITCH) volume (VOL)"
  CSTA: 2-AP-10
  dependencies: [T15.G5.NEW5]

T15.G7.NEW7 - Multi-language stories:
  description: "Students create stories that speak in multiple languages using TTS language parameter. They explore accessibility and global storytelling."
  challenge: "Build: Story with dialogue in 3+ languages"
  CSTA: 2-AP-13
  dependencies: [T15.G6.NEW6]

T15.G8.02-REVISED - Accessibility in Media (enhanced):
  old_description: "Implement features like text-to-speech (for blind users) or subtitles (for sound) to make stories accessible."
  new_description: "Students implement comprehensive accessibility: (1) AI text-to-speech for spoken dialogue, (2) visual speech bubbles for deaf users, (3) multi-language support, (4) adjustable text sizes and colors for visual impairment. They evaluate their story against WCAG principles."
  old_challenge: "Modify. Add TTS blocks to existing text."
  new_challenge: "Refactor: Take existing story and add full accessibility suite (TTS + visual + multi-lang)"
  CSTA: 2-AP-14
  dependencies: [T15.G7.NEW7, T15.G5.NEW3]
```

**Impact:** MEDIUM - Significant missed opportunity for storytelling innovation

---

### ISSUE-ACC-007: MISSING WIDGET INTEGRATION FOR INTERACTIVE STORIES
**Priority:** MEDIUM
**Skills Affected:** T15.G4.05, T15.G4.06 (could be enhanced with widgets)

**Problem:**
T15 uses only `ask [question] and wait` for interaction, completely missing CreatiCode's rich widget system.

**Current State - T15.G4.05:**
```yaml
Description: "Use `ask [What is your name?] and wait` and use the `answer` block in a response."
Challenge: "ask [Name?], say (join [Hello ] (answer))"
```

**CreatiCode Widget Reality:**
CreatiCode has extensive widget blocks:
- `add textbox [NAME] at x (X) y (Y) width (W) height (H)`
- `add button [NAME] at x (X) y (Y) width (W) height (H) text [TEXT]`
- `add label [NAME] at x (X) y (Y) width (W) height (H) text [TEXT]`
- `create chat window [NAME] at x (X) y (Y) width (W) height (H)`
- `add tabs [NAME] at x (X) y (Y) width (W) height (H)`
- `when widget [NAME] clicked`
- `value from widget [NAME]`

**Opportunity:**
Interactive stories could use:
1. Textboxes for name input (prettier than ask block)
2. Buttons for choice-based narratives
3. Labels for persistent UI elements
4. Chat windows for dialogue history
5. Tabs for different story chapters/scenes

**Recommended Action:**
```
ACTION: ADD widget-based interactive story skills at higher grades
REASON: Widgets enable more sophisticated interactive narratives
```

**New Skills Needed:**
```yaml
T15.G6.NEW8 - Widget-based input:
  description: "Students create interactive stories using textbox widgets for player input, replacing the basic ask block. They learn to position widgets and retrieve values."
  challenge: "Build: add textbox [nameInput], add button [submit], when widget [submit] clicked -> say (join [Hello ] (value from widget [nameInput]))"
  CSTA: 2-AP-10
  dependencies: [T15.G4.05]

T15.G7.NEW9 - Button-based choices:
  description: "Students create choice-based narratives using button widgets. Each choice button triggers different story branches using broadcasts."
  challenge: "Build: Present 3 button choices, each broadcasts different scene"
  CSTA: 2-AP-13
  dependencies: [T15.G5.01, T15.G6.NEW8]

T15.G7.NEW10 - Chat window stories:
  description: "Students create dialogue-driven stories using chat window widgets. Messages appear in a scrollable history, creating a conversation-style narrative."
  challenge: "Build: Multi-character dialogue using chat window with distinct speakers"
  syntax: "create chat window [NAME], append chat message [NAME] sender [SENDER] message [TEXT]"
  CSTA: 2-AP-13
  dependencies: [T15.G6.NEW8]

T15.G8.NEW11 - Tabbed story chapters:
  description: "Students organize complex stories into chapters using tab widgets. Each tab contains a different scene/chapter with its own sprites and logic."
  challenge: "Build: 5-chapter story with tab navigation"
  CSTA: 2-AP-14
  dependencies: [T15.G7.NEW9, T15.G7.NEW10]
```

**Impact:** MEDIUM - Widgets enable much richer interactive storytelling

---

### ISSUE-ACC-008: MISSING DRAWING BLOCKS FOR SCENE CREATION
**Priority:** LOW
**Skills Affected:** None currently, but opportunity exists

**Problem:**
Since backdrops can't be switched, students need alternative ways to create scenes.

**CreatiCode Drawing Blocks:**
```
looks_draw_rectangle: draw rectangle x (X) y (Y) width (W) height (H) color [COLOR] filled (FILLED)
looks_draw_oval: draw oval x (X) y (Y) width (W) height (H) color [COLOR] filled (FILLED)
looks_draw_text: draw text [TEXT] at x (X) y (Y) text size (SIZE) [COLOR]
looks_draw_line: draw line from x (X1) y (Y1) to x (X2) y (Y2) color [COLOR] width (W)
looks_clear_drawing: clear all drawings
```

**Opportunity:**
Students could programmatically draw scenes/backgrounds instead of importing images.

**Recommended Action:**
```
ACTION: ADD drawing-based scene creation skills (OPTIONAL)
REASON: Alternative to backdrop switching, teaches generative graphics
```

**New Skills Needed:**
```yaml
T15.G6.NEW12 - Draw simple scenes:
  description: "Students create scene backgrounds using drawing blocks. They draw rectangles for ground/sky, ovals for sun/moon, and text for labels."
  challenge: "Build: Draw daytime scene with sky, ground, sun using drawing blocks"
  CSTA: 2-AP-10
  dependencies: [T06.G3.01]

T15.G7.NEW13 - Programmatic scene transitions:
  description: "Students create scene transitions by clearing drawings and redrawing new scenes. They use broadcasts to coordinate scene changes."
  challenge: "Build: Transition from day to night scene using clear and redraw"
  CSTA: 2-AP-13
  dependencies: [T15.G6.NEW12, T15.G5.01]
```

**Impact:** LOW - Nice-to-have, but not essential

---

## CATEGORY 2: SKILL QUALITY ISSUES

### ISSUE-QUAL-001: OVERLY COMPLEX EARLY DEPENDENCIES
**Priority:** MEDIUM
**Skills Affected:** T15.G3.04, T15.G3.05, T15.G3.06

**Problem:**
Early Grade 3 skills have unnecessary complex dependencies from other topics.

**Example - T15.G3.04:**
```yaml
Dependencies:
  - T15.G3.03: Reset appearance (reasonable)
  - T09.G3.01: Create and use a numeric variable (WHY?)
  - T14.G3.03: Keep sprite on screen (somewhat relevant)
  - T07.G3.02: Trace a script with a simple loop (WHY?)
```

**Analysis:**
- Saying "Hello" doesn't require variables (T09.G3.01)
- Saying "Hello" doesn't require loop tracing (T07.G3.02)
- These dependencies artificially delay a fundamental storytelling skill

**Similar Issues:**
- T15.G3.05 (Think bubble) depends on T08.G3.02, T07.G3.03 (unnecessary)
- T15.G3.06 (Sequence dialogue) depends on T09.G3.02, T10.G3.01 (list processing?!)
- T15.G3.07 (Wait) depends on T11.G3.01, T12.G3.01 (custom blocks and comments?!)

**Recommended Action:**
```
ACTION: SIMPLIFY dependencies to only essential prerequisites
REASON: Enable earlier access to fundamental storytelling features
```

**Revised Dependencies:**
```yaml
T15.G3.04 - Say something (REVISED):
  old_dependencies: [T15.G3.03, T09.G3.01, T14.G3.03, T07.G3.02]
  new_dependencies: [T06.G3.01] # Only need basic scripting
  rationale: "Saying text is foundational and doesn't need variables, loops, or boundary logic"

T15.G3.05 - Think bubble (REVISED):
  old_dependencies: [T15.G3.04, T08.G3.02, T07.G3.03]
  new_dependencies: [T15.G3.04] # Only need say block first
  rationale: "Think is parallel to say, no loops or conditionals needed"

T15.G3.06 - Sequence dialogue (REVISED):
  old_dependencies: [T15.G3.05, T09.G3.02, T10.G3.01]
  new_dependencies: [T15.G3.05] # Only need individual bubbles first
  rationale: "Sequencing say blocks doesn't require variables or lists"

T15.G3.07 - Wait between actions (REVISED):
  old_dependencies: [T15.G3.06, T11.G3.01, T12.G3.01]
  new_dependencies: [T15.G3.06] # Only need dialogue sequencing
  rationale: "Wait block is simple timing, doesn't need custom blocks or comments"
```

**Impact:** MEDIUM - Improves accessibility of storytelling strand

---

### ISSUE-QUAL-002: VAGUE "SIMPLE ANIMATION" WITHOUT COSTUME BLOCKS
**Priority:** HIGH
**Skills Affected:** T15.G3.02, T15.G3.03

**Problem:**
T15.G3.02 and T15.G3.03 are labeled "Simple animation loop" and "Reset appearance" but reference costume blocks that don't exist.

**Current State - T15.G3.02:**
```yaml
Description: "Use `next costume` inside a `repeat` loop to create a simple animation cycle."
```

**Without costume blocks, what IS animation in CreatiCode?**
Options:
1. Movement animation (glide, change x/y in loops)
2. Size animation (change size in loops)
3. Rotation animation (turn degrees in loops)
4. Fade/reveal animation (gradual effects)
5. Multi-sprite choreography (different sprites appearing in sequence)

**Recommended Action:**
```
ACTION: DELETE or completely REWRITE animation skills
REASON: Foundation (costumes) doesn't exist
```

**Replacement Skills:**
```yaml
T15.G3.NEW13 - Movement animation:
  description: "Students create animation using movement in a loop. They make sprites glide, hop, or slide across the stage by repeating motion blocks."
  challenge: "Build: repeat (10) -> change x by (10), wait (0.1) secs"
  CSTA: 1B-AP-10
  dependencies: [T06.G3.01, T07.G3.01]

T15.G3.NEW14 - Size animation:
  description: "Students create growing/shrinking animations using change size in a loop. They make objects pulse, grow, or shrink rhythmically."
  challenge: "Build: repeat (10) -> change size by (10), wait (0.1) secs"
  CSTA: 1B-AP-10
  dependencies: [T15.G3.NEW13]

T15.G3.NEW15 - Reset animation state:
  description: "Students ensure sprites return to starting position, size, and visibility when green flag is clicked. They debug animations that don't restart properly."
  challenge: "Debug: Sprite stays big/moved after restart. Fix initialization."
  CSTA: 1B-AP-10
  dependencies: [T15.G3.NEW14]
```

**Impact:** HIGH - Foundational skills need complete redesign

---

### ISSUE-QUAL-003: MISSING SCAFFOLDING FOR NARRATIVE STRUCTURE
**Priority:** MEDIUM
**Skills Affected:** Entire topic (structural)

**Problem:**
T15 teaches mechanics (say, hide, broadcast) but lacks explicit skills for:
- Story arc (beginning, middle, end)
- Character development
- Conflict and resolution
- Pacing and timing for emotional impact

**Current Approach:**
- Grade 3-4: Mechanical skills (say, hide, wait)
- Grade 5-6: Technical skills (broadcasts, variables)
- Grade 7-8: System design (managers, engines)

**Missing Layer:**
Storytelling **craft** - how to use these tools to tell compelling stories.

**Recommended Action:**
```
ACTION: ADD narrative craft skills at each grade level
REASON: Bridge technical skills to storytelling outcomes
```

**New Skills Needed:**
```yaml
T15.G4.NEW14 - Three-part story structure:
  description: "Students organize a story into beginning (setup), middle (conflict), and end (resolution) using broadcasts to mark transitions. They learn narrative arc fundamentals."
  challenge: "Build: Story with clear broadcast [Beginning], [Conflict], [Resolution] markers"
  CSTA: 1B-AP-10
  dependencies: [T15.G3.06, T15.G3.07]

T15.G5.NEW15 - Pacing with wait blocks:
  description: "Students control story pacing using strategic wait blocks. Fast pacing (short waits) for action, slow pacing (long waits) for suspense/emotion."
  challenge: "Modify: Add waits to create suspense before reveal"
  CSTA: 1B-AP-10
  dependencies: [T15.G3.07, T15.G4.NEW14]

T15.G6.NEW16 - Character consistency:
  description: "Students maintain character traits across scenes using variables. A character's personality (brave, shy) determines their dialogue choices throughout the story."
  challenge: "Build: Character with personality variable influencing multiple dialogue choices"
  CSTA: 2-AP-10
  dependencies: [T15.G5.07, T15.G4.NEW14]

T15.G7.NEW17 - Emotional arc mapping:
  description: "Students map emotional intensity across story using a variable that changes scene-by-scene. They visualize story arc as a curve (rising action, climax, falling action)."
  challenge: "Build: 5-scene story with emotion variable graphing story arc"
  CSTA: 2-AP-13
  dependencies: [T15.G6.NEW16]
```

**Impact:** MEDIUM - Elevates T15 from mechanics to craft

---

### ISSUE-QUAL-004: DUPLICATE/OVERLAPPING SKILLS
**Priority:** LOW
**Skills Affected:** T15.G3.04 vs T15.G3.05

**Problem:**
Say and Think skills are nearly identical, could be combined or better differentiated.

**Current State:**
```yaml
T15.G3.04 - Say something: "Use the say block"
T15.G3.05 - Think bubble: "Use the think block"
```

**Analysis:**
- Both use same syntax (just different blocks)
- Both have same duration parameter
- Think is just "say but with thought bubble visual"
- Having two separate skills for this is weak

**Options:**
1. Combine into one skill "Speech and thought bubbles"
2. Differentiate by purpose (say = dialogue, think = internal monologue)
3. Keep separate but make think skill about WHEN to use think vs say

**Recommended Action:**
```
ACTION: DIFFERENTIATE by teaching when to use each
REASON: Turn mechanical distinction into conceptual one
```

**Revised Skills:**
```yaml
T15.G3.04-REVISED - Say something (unchanged):
  description: "Use the say block to display dialogue."

T15.G3.05-REVISED - Think bubble for internal monologue:
  old_description: "Use the `think [Hmm...]` block to show internal monologue."
  new_description: "Use the think block to show a character's internal thoughts that other characters can't hear. Students learn the difference between dialogue (say - heard by others) and internal monologue (think - character's private thoughts)."
  old_challenge: "Modify. Change say to think."
  new_challenge: "Build: Character says hello to friend, then thinks 'I wonder if they like me' (demonstrating both external and internal)"
  rationale: "Teaches narrative concept, not just mechanical block swap"
```

**Impact:** LOW - Minor quality improvement

---

### ISSUE-QUAL-005: T15.G5.03 "SIMULATED CAMERA PAN" TOO COMPLEX
**Priority:** MEDIUM
**Skills Affected:** T15.G5.03

**Problem:**
Camera pan requires moving ALL sprites in opposite direction - very complex for Grade 5.

**Current State:**
```yaml
Description: "Move all sprites in the opposite direction to simulate a camera panning."
Challenge: "change x by (-10) (on all world sprites)"
```

**Issues:**
1. Requires broadcast to all sprites or duplicated code
2. Difficult to coordinate without proper sprite categorization
3. Easy to forget sprites, creating broken effect
4. Viewport blocks exist but aren't mentioned

**CreatiCode Viewport Blocks:**
```
motion_move_viewport: move viewport to x (XPOS) y (YPOS)
motion_lock_viewport_to_sprite: lock viewport to sprite [SPRITENAME v]
motion_attachtoviewport: attach to viewport at x (XPOS) y (YPOS)
motion_detachfromviewport: detach from viewport
```

**Recommended Action:**
```
ACTION: REPLACE with viewport blocks (easier and more powerful)
REASON: CreatiCode has native viewport system
```

**Revised Skill:**
```yaml
T15.G5.03-REVISED - Viewport control:
  old_description: "Move all sprites in the opposite direction to simulate a camera panning."
  new_description: "Students control the viewport (camera) using 'move viewport to x (X) y (Y)' and 'lock viewport to sprite [NAME]'. They create camera pan effects and camera-following characters for scrolling stories."
  old_challenge: "change x by (-10) (on all world sprites)"
  new_challenge: "Build: lock viewport to sprite [Player], create world larger than stage"
  block_syntax: "move viewport to x (X) y (Y), lock viewport to sprite [NAME v]"
  CSTA: 1B-AP-10
  dependencies: [T06.G3.01, T14.G3.03]
```

**Impact:** MEDIUM - Teaches correct CreatiCode pattern

---

## CATEGORY 3: DEPENDENCY ISSUES (INTRA-TOPIC)

### ISSUE-DEP-001: KINDERGARTEN SKILLS WITH T01/T03 DEPENDENCIES
**Priority:** LOW
**Skills Affected:** T15.GK.02, T15.GK.03

**Problem:**
T15.GK.02 depends on T03.GK.01 (Identify parts of a whole)
T15.GK.03 depends on T01.GK.03 (Find first and last pictures)

**Analysis:**
These dependencies make sense conceptually:
- Identifying emotions (facial parts = parts of whole) ✓
- Speech bubbles (sequence understanding) ✓

**However:**
- Creates cross-topic complexity at Kindergarten level
- Delays storytelling introduction
- May not be necessary (emotions/speech could be taught standalone)

**Recommended Action:**
```
ACTION: OPTIONAL - Remove dependencies if they cause scheduling issues
REASON: K skills should be maximally independent for flexibility
```

**Impact:** LOW - Acceptable as-is, but could be simplified

---

### ISSUE-DEP-002: GRADE 4 SKILLS ALL DEPEND ON SAME 4 SKILLS
**Priority:** LOW
**Skills Affected:** T15.G4.01-G4.08 (all 8 skills)

**Problem:**
All 8 Grade 4 skills share identical dependencies:
```yaml
dependencies:
  - T06.G3.01: Build a green-flag script
  - T06.G3.08: Fix a behavior that runs at the wrong time
  - T07.G3.05: Fix a loop that runs too many or too few times
  - T15.GK.03: Identify speech bubbles (OR T15.GK.02, or T08.G3.01)
```

**Issues:**
1. Copy-paste error - no way all 8 skills need identical prerequisites
2. Some skills need more specific dependencies (e.g., broadcasting needs broadcast intro)
3. Kindergarten skill (T15.GK.03) as prereq for Grade 4 seems odd
4. Too generic - doesn't reflect actual skill content

**Recommended Action:**
```
ACTION: CUSTOMIZE dependencies per skill after fixing platform issues
REASON: Dependencies should reflect actual prerequisite knowledge
```

**Example Revisions:**
```yaml
T15.G4.05-REVISED - Ask and Answer:
  old_dependencies: [T06.G3.01, T06.G3.08, T07.G3.05, T15.GK.03]
  new_dependencies: [T15.G3.06, T09.G3.01] # Need dialogue + variables for join
  rationale: "Ask/answer builds on dialogue sequencing and string joining"

T15.G4.07-REVISED - Coordinate two sprites:
  old_dependencies: [T06.G3.01, T06.G3.08, T07.G3.05, T15.GK.03]
  new_dependencies: [T15.G3.07, T06.G3.01] # Need wait timing + parallel scripts
  rationale: "Coordination requires understanding wait and parallel execution"
```

**Impact:** LOW - Cleanup issue, not blocking

---

### ISSUE-DEP-003: SKILLS DEPENDING ON DELETED SKILLS
**Priority:** HIGH (after deletions)
**Skills Affected:** Any skill depending on T15.G3.01, T15.G3.02, T15.G4.02, T15.G4.03

**Problem:**
Once we delete costume/backdrop skills, dependencies will break.

**Current Dependencies on To-Be-Deleted Skills:**
- T15.G3.03 depends on T15.G3.02 (simple animation loop) - WILL BE DELETED
- T15.G3.04+ depend on T15.G3.03 (reset appearance) - NEEDS UPDATE

**Recommended Action:**
```
ACTION: UPDATE dependency chains after deletions
REASON: Prevent broken dependency references
```

**Revised Dependency Chain:**
```yaml
# After deleting T15.G3.01, T15.G3.02, T15.G3.03:

T15.G3.04-REVISED - Say something:
  old_dependencies: [T15.G3.03, ...]
  new_dependencies: [T06.G3.01] # Just basic scripting

T15.G3.NEW15 - Reset animation state (replaces T15.G3.03):
  dependencies: [T15.G3.NEW14] # Depends on new size animation skill

# All downstream skills update to depend on T15.G3.NEW15 instead of T15.G3.03
```

**Impact:** HIGH - Must coordinate with deletions

---

## CATEGORY 4: GRADE APPROPRIATENESS

### ISSUE-GRADE-001: K-2 SKILLS ARE WELL-DESIGNED
**Priority:** N/A (Positive finding)
**Skills Affected:** T15.GK.01-03, T15.G1.01-03, T15.G2.01-03

**Assessment:**
✅ All K-2 skills are appropriately unplugged/concept-based
✅ Good progression: pictures → story parts → timing concepts
✅ No coding required (correct for K-2)
✅ Scaffolding is sound

**No action needed** - K-2 skills are good as-is.

---

### ISSUE-GRADE-002: GRADE 3 GATEWAY SKILLS TOO DELAYED
**Priority:** MEDIUM
**Skills Affected:** T15.G3.01-G3.09

**Problem:**
Due to costume block issues and over-dependencies, Grade 3 storytelling is artificially delayed.

**Current Situation:**
- T15.G3.01 references non-existent blocks (DELETE)
- T15.G3.04 (say) blocked by 4 dependencies including variables
- Students can't start storytelling until mid-Grade 3

**Ideal Situation:**
- Say/think available early Grade 3 (just need basic scripting)
- Simple stories (dialogue + timing) before complex features
- Progressive enhancement (basic → styled → interactive)

**Recommended Action:**
```
ACTION: SIMPLIFY Grade 3 to enable early storytelling
REASON: Storytelling motivates learners, should be accessible early
```

**Revised Grade 3 Progression:**
```yaml
# Early Grade 3 (immediately after basic scripting):
T15.G3.04-REVISED - Say something [depends only on T06.G3.01]
T15.G3.05-REVISED - Think bubble [depends only on T15.G3.04]
T15.G3.06-REVISED - Sequence dialogue [depends only on T15.G3.05]
T15.G3.07-REVISED - Wait between actions [depends only on T15.G3.06]

# Mid Grade 3 (after events):
T15.G3.08-REVISED - Click to talk [depends on T15.G3.07 + events]
T15.G3.09-REVISED - Key press animation [depends on T15.G3.08]

# Late Grade 3 (after motion):
T15.G3.NEW13 - Movement animation
T15.G3.NEW14 - Size animation
T15.G3.NEW15 - Reset animation state
```

**Impact:** MEDIUM - Improves learner motivation and engagement

---

### ISSUE-GRADE-003: MIDDLE SCHOOL SKILLS APPROPRIATE BUT NEED UPDATING
**Priority:** LOW
**Skills Affected:** T15.G6.01-G8.02

**Assessment:**
Grade 6-8 skills appropriately target:
- System design (state machines, managers)
- Efficiency (list-based dialogue)
- Advanced techniques (lip sync)
- Engine architecture (branching narrative engine)

**However:**
After platform fixes, these need minor updates:
- T15.G6.01: State machine for animation states (not costumes, but size/position/visibility states)
- T15.G7.02: Lip sync logic is fine (uses loudness)
- T15.G8.01: Branching narrative engine is fine (generic)
- T15.G8.02: Accessibility needs TTS scaffolding added earlier

**Recommended Action:**
```
ACTION: MINOR updates after platform fixes complete
REASON: Concepts are sound, just need syntax alignment
```

**Impact:** LOW - Mostly good as-is

---

## SUMMARY OF RECOMMENDED ACTIONS

### IMMEDIATE (HIGH PRIORITY):

1. **DELETE NON-EXISTENT BLOCK SKILLS:**
   - T15.G3.01 (switch costume) - DELETE
   - T15.G3.02 (next costume) - DELETE
   - T15.G3.03 (reset costume) - DELETE or REPLACE
   - T15.G4.02 (costume number) - DELETE
   - T15.G4.03 (switch backdrop) - DELETE

2. **REPLACE GRAPHIC EFFECTS:**
   - T15.G4.01 - REPLACE with gradual fade/reveal effects

3. **UPDATE BACKDROP/SCENE SKILLS:**
   - T15.G4.04 - MODIFY to use broadcasts instead of backdrop events

4. **ADD REPLACEMENT SKILLS:**
   - T15.G3.NEW13-15: Movement/size animation and reset
   - T15.G4.NEW1-3: Costume management via URL, scene changes via broadcasts

### MEDIUM PRIORITY:

5. **ADD CREATICODE-UNIQUE FEATURES:**
   - T15.G5.NEW3-5: Styled say/think, persistent bubbles, basic TTS
   - T15.G6.NEW6-8: Voice customization, widget input
   - T15.G7.NEW7-10: Multi-language, button choices, chat windows

6. **SIMPLIFY DEPENDENCIES:**
   - Remove unnecessary cross-topic dependencies from G3 skills
   - Customize G4 dependencies (currently all identical)

7. **ENHANCE WITH NARRATIVE CRAFT:**
   - T15.G4.NEW14: Three-part story structure
   - T15.G5.NEW15: Pacing with waits
   - T15.G6.NEW16: Character consistency
   - T15.G7.NEW17: Emotional arc mapping

### LOW PRIORITY:

8. **OPTIONAL ENHANCEMENTS:**
   - T15.G6.NEW12-13: Drawing-based scenes (alternative to backdrops)
   - T15.G8.NEW11: Tabbed story chapters
   - Viewport skills: Replace camera pan simulation with viewport blocks
   - K-2 dependency simplification

### DOCUMENTATION:

9. **ENHANCED T15.G8.02:**
   - Add comprehensive accessibility skill with proper scaffolding
   - Reference TTS skills built earlier in progression

10. **DEPENDENCY CLEANUP:**
    - Update all dependencies after skill deletions
    - Ensure no broken references

---

## PLATFORM COMPARISON: SCRATCH VS CREATICODE

| Feature | Standard Scratch | CreatiCode | Impact on T15 |
|---------|-----------------|------------|---------------|
| **Costume Switching** | ✅ switch costume to<br>✅ next costume | ❌ None<br>✅ add costume from URL | **CRITICAL** - 5 skills invalid |
| **Backdrop Switching** | ✅ switch backdrop to<br>✅ next backdrop<br>✅ when backdrop switches | ❌ None | **CRITICAL** - 2 skills invalid |
| **Graphic Effects** | ✅ change [ghost] effect<br>✅ change [color] effect<br>✅ 7 effect types | ❌ None<br>✅ fade/reveal gradually | **HIGH** - 1 skill needs replacement |
| **Say/Think Blocks** | ✅ say [text]<br>✅ say [text] for (t) secs<br>❌ No styling | ✅ Styled say/think<br>✅ Colors, sizes, backgrounds<br>✅ Persistent via T=0 | **MEDIUM** - Missing skills for unique features |
| **Text-to-Speech** | ❌ Extension only<br>❌ Limited voices | ✅ AI TTS built-in<br>✅ 50+ languages<br>✅ 8 voice types<br>✅ Pitch/speed/volume | **MEDIUM** - Huge missed opportunity |
| **Widgets** | ❌ None<br>✅ ask block only | ✅ Textboxes<br>✅ Buttons<br>✅ Labels<br>✅ Chat windows<br>✅ Tabs | **MEDIUM** - Could enhance interactivity |
| **Drawing Blocks** | ✅ Pen extension | ✅ Built-in drawing<br>✅ Rectangles, ovals, text | **LOW** - Alternative to backdrops |
| **Viewport Control** | ❌ None | ✅ move viewport<br>✅ lock to sprite<br>✅ attach to viewport | **MEDIUM** - Better than sprite-moving hack |
| **Speech Recognition** | ❌ None | ✅ Azure + Whisper<br>✅ Continuous recognition | **LOW** - Advanced feature |

---

## METRICS

### Skills Status After Analysis:
- **DELETE:** 5 skills (T15.G3.01, G3.02, G3.03, G4.02, G4.03)
- **MAJOR REVISION:** 6 skills (T15.G4.01, G4.04, G5.03, G8.02, G3.04-G3.07 dependencies)
- **MINOR REVISION:** 8 skills (G4 dependencies, G3.05 conceptual)
- **NEW SKILLS NEEDED:** 17+ skills (animation alternatives, TTS, widgets, narrative craft)
- **KEEP AS-IS:** 9 skills (K-2 unplugged, most MS skills)

### Coverage Gaps:
- **Styled say/think:** 0 skills → Need 2-3
- **Text-to-speech:** 1 vague skill → Need 4-5 scaffolded
- **Widgets for stories:** 0 skills → Need 4
- **Drawing scenes:** 0 skills → Need 2 (optional)
- **Viewport control:** 0 skills → Need 1
- **Narrative craft:** 0 skills → Need 4

### Dependency Health:
- **Broken after deletions:** 5+ skills need updates
- **Over-constrained:** 8 skills (G3.04-G3.09, all G4)
- **Well-designed:** K-2, most G5+

### Grade Appropriateness:
- **K-2:** ✅ Excellent (9/9 appropriate)
- **Grade 3:** ⚠️ Needs simplification (over-dependencies)
- **Grade 4-5:** ❌ Critical platform issues
- **Grade 6-8:** ✅ Good concepts, minor updates needed

---

## CONCLUSION

Topic T15 requires **substantial revision** due to fundamental platform misalignment. Approximately 40% of Grade 3-5 skills reference features that don't exist in CreatiCode (costume/backdrop switching, graphic effects). However, CreatiCode offers powerful unique features (styled say/think, AI TTS, widgets, viewport control) that are completely unused.

**Recommended Strategy:**
1. **Phase 1:** Delete/replace non-existent block skills (HIGH priority)
2. **Phase 2:** Add CreatiCode-unique features (MEDIUM priority)
3. **Phase 3:** Enhance with narrative craft skills (MEDIUM priority)
4. **Phase 4:** Polish dependencies and scaffolding (LOW priority)

The revised T15 will be **shorter initially** (42 skills → ~37 after deletions) but **richer and more accurate** to CreatiCode's actual capabilities. Adding new skills for TTS, widgets, and narrative craft will bring the total back to ~50 skills, with **100% platform accuracy** and significantly improved storytelling power.
