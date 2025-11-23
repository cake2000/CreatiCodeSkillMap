# T15 Implementation Solutions - Exact Skill Definitions

This document provides ready-to-implement skill definitions for all HIGH and MEDIUM priority issues identified in the T15 Analysis Report.

---

## PHASE 1: CRITICAL FIXES (Implement First)

### 1.1 FIX: T15.G3.10 - Enhanced Say with Styling

**Current (INCORRECT):**
```
ID: T15.G3.10
Skill: Enhanced say with styling
Description: Use `say [text] for (2) seconds text size (16) [#FFFFFFFF] background [#000000FF] edge [#FFFFFFFF]` to create styled dialogue with custom text size, text color, background color, and edge color. Use larger text for shouting, red backgrounds for anger, or blue for calm speech.
Dependencies: * T15.G3.04: Say something
```

**New (CORRECT):**
```
ID: T15.G3.10
Skill: Enhanced say with styling
Description: Use the styled say block: `say [Hello!] for (2) seconds text size (16) [#FFFFFFFF] background [#000000FF] edge [#FFFFFFFF]`. The parameters are: duration in seconds, text size (number, e.g., 16 for normal, 24 for large), font color (hex code like #FFFFFFFF for white), background color (hex code like #FF0000FF for red), and edge/border color. Use larger text size (24-32) for shouting or emphasis, red backgrounds (#FF0000FF) for anger, blue backgrounds (#0000FFFF) for calm speech, or yellow backgrounds (#FFFF00FF) for cheerful dialogue.
Dependencies:
* T15.G3.04: Say something
* T15.G3.06: Sequence dialogue
```

---

### 1.2 FIX: T15.G3.05.01 - Style Think Bubbles

**Current (INCORRECT):**
```
ID: T15.G3.05.01
Skill: Style think bubbles
Description: Use `think [text] for (2) seconds text size (16) [#FFFFFFFF] background [#000000FF] edge [#FFFFFFFF]` to create styled thought bubbles with custom colors and text sizes. Use lighter colors for daydreams or darker colors for worried thoughts.
Dependencies: * T15.G3.05: Think bubble
```

**New (CORRECT):**
```
ID: T15.G3.05.01
Skill: Style think bubbles
Description: Use the styled think block: `think [Hmm...] for (2) seconds text size (16) [#FFFFFFFF] background [#000000FF] edge [#FFFFFFFF]`. Parameters work identically to styled say blocks: duration, text size, font color, background color, and edge color. Use lighter background colors with transparency (#FFFFFF80 - white with 50% alpha) for daydreams or light thoughts, darker backgrounds (#000000FF - solid black) for worried or serious thoughts, and pastel colors (#FFB6C1FF - light pink) for happy daydreams.
Dependencies:
* T15.G3.05: Think bubble
* T15.G3.10: Enhanced say with styling
```

---

### 1.3 FIX: T15.G3.00.03 - Customize Costumes in Paint Editor

**Current (MISLEADING):**
```
ID: T15.G3.00.03
Skill: Draw on sprite costumes
Description: Use the paint editor to draw simple shapes and text on sprite costumes. Understand that you can customize how sprites look by editing their visual appearance.
Dependencies: * T15.G3.00.02: Change sprite size
```

**New (CLARIFIED):**
```
ID: T15.G3.00.03
Skill: Customize costumes in paint editor
Description: Use the paint editor (accessed by clicking the "Costumes" tab for a sprite) to manually draw simple shapes and text on sprite costumes before your code runs. This is a visual design tool, not block coding. You click drawing tools (brush, circle, square, text) to create or modify how sprites look. These manual edits become the sprite's permanent appearance. Later you'll learn to draw shapes programmatically with code blocks.
Dependencies:
* T15.G3.00.02: Change sprite size
```

---

### 1.4 MODIFY: T15.G5.09 - Draw Shapes on Costumes with Blocks

**Current (PAINT EDITOR FOCUSED):**
```
ID: T15.G5.09
Skill: Draw shapes on costumes
Description: Use the paint editor's drawing tools to add shapes (circles, rectangles, lines) to sprite costumes. Understand that you can create visual indicators like health bars, status icons, or decorative elements that become part of the sprite's appearance.
```

**New (PROGRAMMATIC BLOCKS):**
```
ID: T15.G5.09
Skill: Draw shapes on costumes with blocks
Description: Use drawing blocks to programmatically add shapes to vector costumes when your code runs. Use `draw rectangle at x (0) y (0) width (200) height (100) fill [#6269F8FF] border [#20B755FF] width (1) corner radius (0) rotation (0)` to draw rectangles. Use `draw oval at x (0) y (0) width (100) height (100) fill [#E2F9F2FF] border [#F44399FF] width (1) rotation (0)` to draw circles and ovals. Unlike the paint editor (manual tool), these blocks draw shapes when scripts run, allowing dynamic visual effects like health bars that change size, status icons that appear/disappear, or patterns created in loops. The shapes are drawn on the sprite's current vector costume, not on the stage.
Dependencies:
* T15.G3.00.03: Customize costumes in paint editor
* T15.G5.01: Coordinate scene changes with broadcasts
```

---

### 1.5 MODIFY: T15.G5.10 - Draw Lines and Curves on Costumes

**Current:**
```
ID: T15.G5.10
Skill: Draw text on costumes
Description: Use the paint editor's text tool to add text labels to sprite costumes. Create character name tags, dialogue indicators, or status text that appears as part of the sprite. For dynamic text that changes during the story, use the `print text [message] at x: () y: ()` blocks on the stage instead.
```

**New:**
```
ID: T15.G5.10
Skill: Draw lines and curves on costumes
Description: Use `draw line in [#386AF8FF] from x (0) y (0) to x (100) y (100) thickness (2)` to draw straight lines on vector costumes. For curved lines, use `draw curve in [#05DC6DFF] from x (20) y (20) to x (200) y (20) control 1 x (20) y (100) control 2 x (200) y (100) thickness (1)`, where control points shape the curve's bend. Combine line drawing with loops to create complex patterns programmatically, such as star bursts, connection lines between objects, or decorative borders that adapt based on variables.
Dependencies:
* T15.G5.09: Draw shapes on costumes with blocks
```

---

### 1.6 ADD NEW: T15.G5.11 - Clear Programmatic Drawings

```
ID: T15.G5.11
Topic: T15 – Stories & Animation
Skill: Clear programmatic drawings
Description: Use `clear all my prints` to remove all drawings created with `draw` blocks (rectangles, ovals, lines, curves) and `print` blocks (text) from this sprite's costume. Use `clear all prints` (without "my") to remove drawings from all sprites' costumes at once. Understand that these blocks only clear programmatically drawn elements - they do NOT erase shapes manually drawn in the paint editor. Use `clear all my prints` at the start of scenes with `when I receive [NewScene]` to reset costumes to their original state before drawing new dynamic elements.
Dependencies:
* T15.G5.10: Draw lines and curves on costumes
* T15.G3.12: Print text at positions
```

---

### 1.7 ADD NEW: T15.G5.12 - Basic Text-to-Speech Narration

```
ID: T15.G5.12
Topic: T15 – Stories & Animation
Skill: Basic text-to-speech narration
Description: Use `say [Hello everyone!] in [English (United States) v] as [Female v] speed (100) pitch (100) volume (100) store sound as []` to convert text to spoken audio using AI voices. The sprite will speak the text aloud. Language options include English, Spanish, French, Chinese, and 30+ others. Voice types include Male, Female, Male2, Female2, Male3, Female3, Boy, and Girl (not all voices work in all languages). Speed, pitch, and volume are percentages: 100 is normal, 50 is half speed/pitch/volume, 200 is double. Leave "store sound as" empty unless you want to save the audio for reuse. Use different voices for different characters to create distinct personalities.
Dependencies:
* T15.G4.05: Read widget value into variable
* T15.G3.04: Say something
```

---

### 1.8 MODIFY: T15.G6.04 - Multi-Language Text-to-Speech

**Current:**
```
ID: T15.G6.04
Skill: Multiple language narration
Description: Use `say [text] in [language v] as [voice v] speed (100) pitch (100) volume (100)` blocks to create stories in multiple languages. Store language preferences in variables (like `(playerLanguage)`) and use `if` blocks to speak dialogue in the selected language.
Dependencies:
* T15.G5.10: Draw text on costumes
* T09.G5.01: Use variables to store and display text strings
```

**New:**
```
ID: T15.G6.04
Topic: T15 – Stories & Animation
Skill: Multi-language text-to-speech storytelling
Description: Create stories that speak in multiple languages by combining text-to-speech with conditionals. Store the player's language preference in a variable: `set [playerLanguage v] to [Spanish]`. Use `if <(playerLanguage) = [Spanish]> then say [Hola!] in [Spanish (Spain) v] as [Female v]` blocks to speak different dialogue based on the selected language. Store parallel dialogue in lists: `[dialogueEnglish v]` and `[dialogueSpanish v]`, then use the appropriate list based on `(playerLanguage)`. Adjust speed (50-150) for slower/faster speech to help language learners, or change pitch (80-120) to create character variety within the same language.
Dependencies:
* T15.G5.12: Basic text-to-speech narration
* T09.G5.01: Use variables to store and display text strings
* T08.G4.01: Use if-else for branching logic
```

---

### 1.9 ADD NEW: T15.G6.05 - Basic Speech Recognition Input

```
ID: T15.G6.05
Topic: T15 – Stories & Animation
Skill: Basic speech recognition input
Description: Use speech recognition blocks to accept voice input from players. Start listening with `start recognizing speech in [English (United States) v] record as [input1]` (uses Microsoft Azure API) or `OpenAI: start recognizing speech in [English (United States) v] record as [input1]` (uses Whisper API). When ready to process the speech, use `end speech recognition` which stops recording and sends the audio to the AI service for text conversion. Read the recognized text with the reporter block `(text from speech)`. Save it to a variable: `set [playerInput v] to (text from speech)`, then respond: `say (join [You said: ] (playerInput))`. This allows hands-free story interaction.
Dependencies:
* T15.G6.04: Multi-language text-to-speech storytelling
* T09.G5.01: Use variables to store and display text strings
```

---

### 1.10 RENAME/MOVE: T15.G6.05 → T15.G6.06 - Voice-Controlled Story Choices

**Current T15.G6.05:**
```
ID: T15.G6.05
Skill: Voice control with speech recognition
Description: Use `start recognizing speech in [language v]` and `text from speech` blocks to create voice-controlled stories. Check the recognized text with `if <(text from speech) contains [keyword]>` to trigger story events based on spoken commands. Players can speak their choices aloud instead of clicking.
Dependencies: * T15.G6.04: Multiple language narration
```

**New T15.G6.06:**
```
ID: T15.G6.06
Topic: T15 – Stories & Animation
Skill: Voice-controlled story choices
Description: Combine speech recognition with conditional logic to trigger story events based on spoken keywords. After using `start recognizing speech` and `end speech recognition`, check the result: `if <(text from speech) contains [yes]> then broadcast [AcceptQuest]` or `if <(text from speech) contains [no]> then broadcast [RejectQuest]`. Use `contains` instead of `=` because speech recognition may include extra words ("yes please" should match "yes"). Check for multiple keywords to handle variations: `if <or <(text from speech) contains [yes]> <(text from speech) contains [yeah]>>`. This allows players to speak choices like "Go left", "Attack the dragon", or "Yes" instead of clicking buttons, creating more immersive voice-driven stories.
Dependencies:
* T15.G6.05: Basic speech recognition input
* T15.G4.06: Simple branching with buttons
* T08.G4.01: Use if-else for branching logic
```

---

### 1.11 MODIFY: T15.G3.12 - Print Text at Positions

**Current:**
```
ID: T15.G3.12
Skill: Print text at positions
Description: Use `print [text] at x (0) y (0) width (300) height (100) color [#2CADE5FF]` to display text at specific stage positions. This creates subtitle-like effects or multiple dialogue boxes simultaneously. Use `clear all my prints` to remove text when the scene changes.
Dependencies: * T15.G3.11: Display labels for titles
```

**New:**
```
ID: T15.G3.12
Topic: T15 – Stories & Animation
Skill: Print text at positions
Description: Use `print [Subtitle text] at x (0) y (0) width (300) height (100) color [#2CADE5FF]` to display TEMPORARY text directly on the stage at specific coordinates. Unlike labels (which are widgets), printed text is drawn as a layer on the stage and stays until cleared or the project stops. Use `print [text] at x (0) y (0) width (300) height (100) color [#2CADE5FF] for (2) seconds` to automatically hide the text after a duration. Create floating dialogue near characters by positioning text near sprite coordinates: `print [Ouch!] at x (my x) y ((my y) + (50))`. Display multiple simultaneous texts at different positions for conversations. Use `clear all my prints` to remove all printed text when scenes change: `when I receive [NewScene]` → `clear all my prints`.
Dependencies:
* T15.G3.11: Display labels for titles
```

---

## PHASE 2: SCAFFOLDING GAPS

### 2.1 ADD NEW: T15.G3.01.01 - Smooth Movement with Glide

```
ID: T15.G3.01.01
Topic: T15 – Stories & Animation
Skill: Smooth movement with glide
Description: Use `glide (1) secs to x: (100) y: (50)` to smoothly animate a sprite moving to a position over time, creating visible motion. Unlike `go to x: y:` which teleports instantly, glide creates a smooth animation from the current position to the target position. The duration parameter controls animation speed: longer durations (2-3 seconds) create slow, dramatic movement; shorter durations (0.5 seconds) create quick, snappy actions. Use glide for character walking, flying, or sliding animations. Combine multiple glide blocks in sequence to create path-following: `glide (1) secs to x: (0) y: (0)` then `glide (1) secs to x: (100) y: (100)` creates an L-shaped path.
Dependencies:
* T15.G3.01: Change sprite position
```

---

### 2.2 ADD NEW: T15.G5.02.01 - Sequential Actions with Broadcast and Wait

```
ID: T15.G5.02.01
Topic: T15 – Stories & Animation
Skill: Sequential actions with broadcast and wait
Description: Use `broadcast [Action1] and wait` to pause the current script until ALL scripts triggered by that broadcast complete their actions. This ensures animations happen in strict sequence: Character A finishes walking completely BEFORE Character B starts talking. Compare to regular `broadcast [Action1]` (without "and wait") which continues immediately, allowing parallel/simultaneous actions. Example: `broadcast [WalkToCenter] and wait` → Character moves (takes 3 seconds) → Current script pauses for those 3 seconds → `say [I made it!]` only runs after movement completes. Use "broadcast and wait" for cutscenes where timing order matters, regular "broadcast" when actions should happen at the same time.
Dependencies:
* T15.G5.02: Broadcast specific actions
```

---

### 2.3 MODIFY: T15.G6.03 - Cutscene Controller

**Current:**
```
ID: T15.G6.03
Skill: Cutscene controller
Description: Create a "Cutscene" custom block that uses `broadcast and wait` to sequence multiple character actions, ensuring each animation completes before the next begins.
Dependencies:
* T15.G6.02: List-based Dialogue
* T11.G4.01: Define and call a simple custom block (no parameters)
```

**New:**
```
ID: T15.G6.03
Topic: T15 – Stories & Animation
Skill: Cutscene controller with custom blocks
Description: Create a custom block called "Cutscene" (using "Make a Block") that orchestrates multi-step story sequences using `broadcast and wait` to ensure strict timing. Inside the custom block: `broadcast [Step1] and wait`, `broadcast [Step2] and wait`, `broadcast [Step3] and wait`. Each broadcast triggers a different character's action (walking, talking, reacting) and the "and wait" ensures the previous action finishes before the next begins. Call the custom block with `Cutscene` under `when green flag clicked`. This centralizes complex animation sequences in one reusable block, making stories easier to debug and modify. Use for intro sequences, dramatic reveals, or multi-character conversations.
Dependencies:
* T15.G6.02: List-based Dialogue
* T15.G5.02.01: Sequential actions with broadcast and wait
* T11.G4.01: Define and call a simple custom block (no parameters)
```

---

### 2.4 MODIFY: T15.G3.11 - Display Labels for Titles

**Current:**
```
ID: T15.G3.11
Skill: Display labels for titles
Description: Create label widgets using `add label [text] at X (0) Y (0) width (200) height (50) as [title]` to display story titles, scene headings, or character names. Position and style labels to enhance the story presentation.
Dependencies: * T15.G3.10: Enhanced say with styling
```

**New:**
```
ID: T15.G3.11
Topic: T15 – Stories & Animation
Skill: Display labels for titles
Description: Create label widgets using `add label at X (0) Y (0) width (200) height (50) padding (10) as [title]` to display PERSISTENT text that stays on screen. Labels are UI widgets (not temporary like printed text) that remain visible until explicitly hidden or the project stops. After creating a label, set its text with `set value to [Chapter 1: The Beginning] for widget [title v]`. Position labels at screen edges: top center (X: 0, Y: 150) for titles, top left (X: -200, Y: 150) for scene headings, bottom center (X: 0, Y: -150) for subtitles. Labels float above all sprites and can be styled with widget styling blocks. Use for story titles, chapter headings, character name tags, or score displays.
Dependencies:
* T15.G3.10: Enhanced say with styling
```

---

### 2.5 MODIFY: T15.G5.04 - Layering Sprites and Text

**Current:**
```
ID: T15.G5.04
Skill: Layering logic
Description: Use `go to [front v] layer` and `go [backward v] (1) layers` to control sprite depth. Ensure foreground characters appear in front of background elements for proper scene composition.
Dependencies: * T15.G5.01: Coordinate scene changes with broadcasts
```

**New:**
```
ID: T15.G5.04
Topic: T15 – Stories & Animation
Skill: Layering sprites and text
Description: Understand the layer order in CreatiCode projects: Background (stage backdrop - furthest back) → Printed text (`print` blocks) → Sprites (ordered back-to-front by layer number) → Widgets (labels, buttons - always on top). Use `go to [front v] layer` to bring a sprite to the front of all sprites, or `go to [back v] layer` to send it behind all sprites. Use `go [forward v] (1) layers` to move up one layer, `go [backward v] (1) layers` to move down one layer. Ensure foreground characters use `go to front layer` so they appear in front of background scenery sprites. Note: Sprites cannot layer above widgets (widgets are always topmost), and printed text always appears behind sprites. Use `clear all my prints` to remove text layers that might be covered by sprites.
Dependencies:
* T15.G5.01: Coordinate scene changes with broadcasts
* T15.G3.12: Print text at positions
```

---

### 2.6 REORDER: Move T15.G3.10 After T15.G3.08

**Reason:** Students should practice basic dialogue (G3.06, G3.08) before learning advanced styling.

**New Order:**
1. T15.G3.04: Say something (basic)
2. T15.G3.05: Think bubble (basic)
3. T15.G3.06: Sequence dialogue
4. T15.G3.07: Wait between actions
5. T15.G3.08: Click to talk
6. T15.G3.09: Key press animation (current)
7. **T15.G3.10: Enhanced say with styling** (MOVED from before G3.06)
8. **T15.G3.11: Style think bubbles** (renumbered from G3.05.01)
9. T15.G3.12: Display labels for titles (renumbered from G3.11)
10. T15.G3.13: Print text at positions (renumbered from G3.12)

---

## PHASE 3: WIDGET ENHANCEMENTS

### 3.1 ADD NEW: T15.G5.13 - Style Widgets for Stories

```
ID: T15.G5.13
Topic: T15 – Stories & Animation
Skill: Style widgets for stories
Description: Customize widget appearance to match story themes using styling blocks. Use `set widget background color [#FFFFFFFF] border color [#000000FF] border width (2) border radius (10) for [widgetName v]` to change widget colors and borders. Colors use hex format #RRGGBBAA where RR=red, GG=green, BB=blue, AA=alpha/transparency (FF=solid, 00=invisible). Use `set text style [Arial v] font size (18) text color [#000000FF] boldness [bold v] text alignment [Center v] for [widgetName v]` to format text inside labels, buttons, and textboxes. Match widget colors to story mood: dark colors (#333333FF background, #FF0000FF text) for scary scenes, bright pastels (#FFB6C1FF background, #FFFFFFFF text) for happy scenes. Use larger fonts (24+) for emphasis, bold for important choices.
Dependencies:
* T15.G4.06: Simple branching with buttons
* T15.G3.11: Display labels for titles
```

---

### 3.2 ADD NEW: T15.G5.14 - Dropdown Menus for Story Choices

```
ID: T15.G5.14
Topic: T15 – Stories & Animation
Skill: Dropdown menus for story choices
Description: Use `add dropdown menu at X (0) Y (0) width (200) height (40) from list [choices v] as [menu1]` to create a dropdown menu of story choices. The dropdown displays items from the list variable `[choices v]`, which you populate with `add [Go to forest] to [choices v]`, `add [Go to town] to [choices v]`, etc. Read the selected value with `(value of widget [menu1 v])` and use it in conditionals: `if <(value of widget [menu1 v]) = [Go to forest]> then broadcast [ForestScene]`. Use dropdown menus instead of multiple buttons when there are many choices (4+) to save screen space. Style the dropdown with widget styling blocks to match your story theme.
Dependencies:
* T15.G5.13: Style widgets for stories
* T10.G4.01: Use lists for dynamic data storage
```

---

### 3.3 ADD NEW: T15.G6.07 - Rich Text Story Displays

```
ID: T15.G6.07
Topic: T15 – Stories & Animation
Skill: Rich text story displays
Description: Use `add rich textbox at X (0) Y (0) width (400) height (300) padding (10) mode [read only v] as [storyText]` to create formatted text displays that support bold, italics, colors, and multiple paragraphs. Rich textboxes accept HTML-like formatting in the text value. Set formatted text with `set value to [<b>Chapter 1</b><br><br>Once upon a time...] for widget [storyText v]`. Use `<b>text</b>` for bold, `<i>text</i>` for italics, `<br>` for line breaks, `<font color='red'>text</font>` for colored text. Create book-like story presentations with styled text, chapter headings, and formatted dialogue. Set mode to [read only] so players can't edit the text, or [input] to let them write their own stories.
Dependencies:
* T15.G5.14: Dropdown menus for story choices
* T16.G5.05: Use rich textboxes for formatted text display (verify this exists in T16)
```

---

### 3.4 ADD NEW: T15.G6.08 - Visual Stat Tracking with Sliders

```
ID: T15.G6.08
Topic: T15 – Stories & Animation
Skill: Visual stat tracking with sliders
Description: Use `add slider at X (0) Y (0) width (200) min (0) max (100) as [healthBar]` to create visual stat displays for story variables. After creating the slider widget, link it to a variable by updating the slider whenever the variable changes: `when [health v] changes` → `set value to (health) for widget [healthBar v]`. Position sliders at screen edges to show stats like health (red slider at top right), mood (yellow slider at top left), or relationship levels (green sliders at bottom). Use widget styling to color-code stats: `set widget background color [#FF0000FF]...` for health (red), `set widget background color [#0000FFFF]...` for mana (blue), `set widget background color [#00FF00FF]...` for happiness (green). When story choices change the variable (`change [health v] by (-10)`), the slider automatically updates visually.
Dependencies:
* T15.G5.07: Track story choices
* T15.G5.13: Style widgets for stories
```

---

### 3.5 MODIFY: T15.G7.01 - Scene Manager Sprite

**Current:**
```
ID: T15.G7.01
Skill: Scene manager sprite
Description: Create a dedicated "SceneManager" sprite (hidden) that tracks the current scene in a variable, sends broadcasts to transition between scenes, and coordinates which sprites appear or hide. This centralizes story flow control in one place.
Dependencies:
* T15.G6.03: Cutscene controller
* T15.G5.01: Coordinate scene changes with broadcasts
```

**New:**
```
ID: T15.G7.01
Topic: T15 – Stories & Animation
Skill: Scene manager sprite
Description: Create a dedicated "SceneManager" sprite (use `hide` to keep it invisible) that centralizes story flow control. Store the current scene in a variable: `set [currentScene v] to [1]`. When transitioning scenes, the SceneManager broadcasts: `broadcast (join [Scene] (currentScene))` and coordinates which sprites AND widgets appear or hide. Use `when green flag clicked` → `hide widget [button1 v]` to hide widgets from previous scenes, then `when I receive [Scene2]` → `show widget [button2 v]` to reveal widgets for the new scene. The SceneManager handles all scene transitions, widget visibility, background changes (`switch backdrop to [forest v]`), and story state tracking in one place. This architecture makes complex multi-scene stories easier to debug and expand.
Dependencies:
* T15.G6.03: Cutscene controller with custom blocks
* T15.G5.01: Coordinate scene changes with broadcasts
* T16.G4.03: Hide and show widgets (verify this exists in T16)
```

---

## PHASE 4: ADVANCED FEATURES

### 4.1 ADD NEW: T15.G5.15 - Calculate Animation Timing

```
ID: T15.G5.15
Topic: T15 – Stories & Animation
Skill: Calculate animation timing
Description: Synchronize animations by matching `wait` block durations to speech and motion. If a character says text for 3 seconds (`say [Hello there!] for (3) seconds`), other sprites should `wait (3) seconds` before responding. For text-to-speech, estimate timing: approximately 2-3 seconds per 10 words at normal speed (100). Adjust for speed changes: 50% speed takes twice as long, 200% speed takes half as long. For glide animations, the duration IS the time: `glide (2) secs to x: y:` takes exactly 2 seconds. Coordinate multi-sprite scenes: Sprite A: `say [text] for (3) secs` + `glide (2) secs to x:y:`, Sprite B: `wait (5) secs` (3+2) then respond. Test your timings and adjust wait blocks if characters overlap or pause too long.
Dependencies:
* T15.G4.07: Coordinate two sprites (Wait)
* T15.G5.12: Basic text-to-speech narration
* T15.G3.01.01: Smooth movement with glide
```

---

### 4.2 ADD NEW: T15.G7.03.01 - Split Text at Delimiter

```
ID: T15.G7.03.01
Topic: T15 – Stories & Animation
Skill: Split text at delimiter
Description: Parse structured text by finding delimiter characters (like ":") and extracting the parts before and after. Use a loop to find the delimiter position: `set [position v] to (0)`, `repeat (length of [text v])` with `if <(letter (i) of (text)) = [:]> then set [position v] to (i)`. Once found, extract the parts: `set [beforeColon v] to (letter (1) to (position) of (text))` for everything before the delimiter, `set [afterColon v] to (letter ((position) + (2)) to (length of (text)) of (text))` for everything after (skip the colon itself with +2 to also skip the space). Use this to parse dialogue data like "Alice: Hello!" into speaker "Alice" and dialogue "Hello!". This prepares you for advanced dialogue systems with speaker tags.
Dependencies:
* T12.G5.01: Use text operations to extract substrings (verify this exists in T12)
* T15.G6.02: List-based Dialogue
* T07.G5.01: Use loops with exit conditions
```

---

### 4.3 MODIFY: T15.G7.03 - Dialogue System with Speaker Tags

**Current:**
```
ID: T15.G7.03
Skill: Dialogue system with speaker tags
Description: Build a dialogue system where each list item contains speaker name and text (e.g., "Alice:Hello!"). Parse the string to show the correct sprite speaking with `item () of [split]` operations.
Dependencies: * T15.G6.02: List-based Dialogue
```

**New:**
```
ID: T15.G7.03
Topic: T15 – Stories & Animation
Skill: Dialogue system with speaker tags
Description: Build a dialogue system where each list item in `[dialogueData v]` contains speaker name and text separated by a colon (e.g., "Alice: Hello there!", "Bob: Hi Alice!"). Loop through the list: `repeat (length of [dialogueData v])` with `set [currentLine v] to (item (i) of [dialogueData v])`. Parse each line using text splitting techniques from T15.G7.03.01 to extract `[speaker v]` and `[dialogue v]`. Use broadcasts to make the correct sprite speak: `broadcast (join [speak_] (speaker))`, then in each character sprite: `when I receive [speak_Alice]` → `say (dialogue)`. This creates a centralized dialogue system where you write conversations in a list ("Alice: Hi", "Bob: Hey") and the sprites automatically speak their lines. Easy to edit dialogue without changing code.
Dependencies:
* T15.G6.02: List-based Dialogue
* T15.G7.03.01: Split text at delimiter
```

---

### 4.4 MODIFY: T15.G8.03 - Encode Story State for Saving

**Current:**
```
ID: T15.G8.03
Skill: Encode story state for saving
Description: Combine the current node ID, score variables, and key story flags into a single string or list format that can be stored. Use `join` blocks to create a save string like "node3|score5|hasKey1".
Dependencies:
* T15.G8.01.02: Navigate story nodes by choice
* T09.G6.01: Model real-world quantities using variables and formulas
```

**New:**
```
ID: T15.G8.03
Topic: T15 – Stories & Animation
Skill: Encode story state for saving
Description: Combine the current node ID, score variables, and key story flags into a single string that can be saved and loaded later. Use nested `join` blocks to create a save string with "|" delimiters: `set [saveData v] to (join (currentNode) (join [|] (join (score) (join [|] (hasKey)))))` creates "node3|score5|true". Add more variables with more join operations. Save this string to a cloud variable `set [☁ SaveGame v] to (saveData)` so it persists across sessions and devices, or display it to the player: `say (join [Your save code: ] (saveData))` and let them copy it manually. Cloud variables require an account and internet connection; save codes work offline but require manual copying.
Dependencies:
* T15.G8.01.02: Navigate story nodes by choice
* T09.G6.01: Model real-world quantities using variables and formulas
* T09.G7.01: Use cloud variables for persistent data (verify this exists in T09)
```

---

### 4.5 MODIFY: T15.G8.03.01 - Load and Restore Story State

**Current:**
```
ID: T15.G8.03.01
Skill: Load and restore story state
Description: Parse a saved state string back into individual variables using string operations or list splits. Restore the current node, scores, and flags so the player can continue from where they left off.
Dependencies: * T15.G8.03: Encode story state for saving
```

**New:**
```
ID: T15.G8.03.01
Topic: T15 – Stories & Animation
Skill: Load and restore story state
Description: Parse a saved state string back into individual variables to restore game progress. If loading from cloud variable: `set [saveData v] to (☁ SaveGame)`. If loading from player input: create a textbox widget for the player to paste their save code, then `set [saveData v] to (value of widget [loadBox v])`. Split the string by "|" delimiter using the technique from T15.G7.03.01. Find each "|" position and extract the parts: first part is current node, second part is score, third part is flags. Restore each variable: `set [currentNode v] to (part 1)`, `set [score v] to (part 2)`, etc. After restoring all variables, broadcast the current node to resume the story: `broadcast (join [Node] (currentNode))`. Test your save/load system thoroughly to ensure all important variables are preserved.
Dependencies:
* T15.G8.03: Encode story state for saving
* T15.G7.03.01: Split text at delimiter
```

---

### 4.6 ADD NEW: T15.G8.04 - 3D Speech Bubbles in Space

```
ID: T15.G8.04
Topic: T15 – Stories & Animation
Skill: 3D speech bubbles in space
Description: Use `show speech bubble [Hello!] offset xyz (0) (0) (110) max width (200) text font [Arial v] size (15) color [#000000FF] background [#FFFFFFFF] for [3] seconds camera facing [Yes v] ID [1 v]` to create speech bubbles in 3D projects. Unlike 2D speech bubbles that appear above sprites, 3D speech bubbles float in 3D space at a specific XYZ offset relative to the sprite object. The offset (0, 0, 110) places the bubble 110 units above the sprite's center. Set "camera facing" to [Yes] to make the bubble automatically rotate to face the camera, ensuring text is always readable regardless of camera angle. The "max width" parameter controls text wrapping. Use different "ID" values ([1 v], [2 v]) to show multiple bubbles simultaneously from the same sprite. Combine with 3D animations for immersive storytelling in 3D environments.
Dependencies:
* T15.G7.02: AI text-to-speech narration
* T17.G7.01: Create and control 3D sprite objects (verify this exists in T17)
```

---

### 4.7 ADD NEW: T15.G8.05 - Interactive Camera Stories

```
ID: T15.G8.05
Topic: T15 – Stories & Animation
Skill: Interactive camera stories
Description: Use `add camera widget at X (0) Y (0) width (320) height (240) from [front v] mode [normal v] as [cam1]` to add live camera feeds to stories. The "from" parameter selects [front] (selfie) or [back] (outward) camera. Mode can be [normal] or [flipped] (mirror image). Use `save picture from camera [cam1 v] as costume [playerPhoto]` to capture the player's photo and incorporate it into the story. The captured costume can be used on sprites: `switch costume to [playerPhoto v]`. Create personalized stories where the player becomes a character, or use the camera for interactive choice-making (show an object to the camera to select a choice). Position the camera widget in a corner (X: -150, Y: -100) during capture, then hide it after: `hide widget [cam1 v]`. Requires camera permission from the user.
Dependencies:
* T15.G7.01: Scene manager sprite
* T16.G6.01: Add and control camera widgets (verify this exists in T16)
```

---

### 4.8 ADD NEW: T15.G7.04 - Generate Backgrounds with AI (IF PLATFORM SUPPORTS)

**Note:** Only add this if CreatiCode has AI image generation blocks. Verify first.

```
ID: T15.G7.04
Topic: T15 – Stories & Animation
Skill: Generate backgrounds with AI
Description: Use AI image generation blocks to create custom backgrounds from text descriptions (verify exact block syntax from blockdes8.txt). Describe the setting in detail (e.g., "a dark spooky haunted house at night with glowing windows and fog") and let the AI generate the backdrop image. Use `switch backdrop to [generatedImage v]` to display it. Combine with scene transitions to create diverse story locations without finding or drawing external images. Adjust your description based on results: add more details for better accuracy. Use AI-generated backgrounds for fantasy settings, unique locations, or rapid prototyping of story scenes. Generation takes 10-30 seconds depending on complexity.
Dependencies:
* T15.G5.01: Coordinate scene changes with broadcasts
* T14.G6.01: Use AI APIs for creative generation (verify this exists in T14)
```

---

## DEPENDENCIES TO VERIFY IN OTHER TOPICS

Before implementing, verify these skills exist in their respective topics:

### T09 (Variables) - Cloud Variables
- **T09.G7.01**: Use cloud variables for persistent data
  - If missing, T15.G8.03 description should remove cloud variable references and focus on save codes only

### T12 (Text/Strings) - String Operations
- **T12.G4.01** or **T12.G5.01**: Extract characters from text, string operations
  - Required by T15.G5.06 (typewriter effect) and T15.G7.03.01 (split text)
  - If missing, add to T12 or expand descriptions in T15

### T14 (AI & Data) - AI Understanding
- **T14.G5.01**: Understanding AI services
  - Should be dependency for T15.G5.12 (TTS), T15.G6.05 (speech recognition)
- **T14.G6.01**: Use AI APIs for creative generation
  - Should be dependency for T15.G7.04 (AI backgrounds) if that feature exists

### T16 (User Interfaces) - Widget Skills
- **T16.G4.03**: Hide and show widgets
  - Required by T15.G7.01 (scene manager)
  - If missing, add to T16 first
- **T16.G5.05**: Use rich textboxes for formatted text display
  - Required by T15.G6.07 (rich text story displays)
  - If missing, add to T16 first
- **T16.G6.01**: Add and control camera widgets
  - Required by T15.G8.05 (interactive camera stories)
  - If missing, add to T16 first

### T17 (3D Graphics) - 3D Sprites
- **T17.G7.01**: Create and control 3D sprite objects
  - Required by T15.G8.04 (3D speech bubbles)
  - If missing, T15.G8.04 should only be added after T17 has 3D basics

---

## RENUMBERING GUIDE

After adding new skills, renumber subsequent skills:

### G3 Renumbering (due to reordering):
- Current G3.09 → Keep as G3.09
- Current G3.10 → Move to G3.10 (after G3.09)
- Current G3.05.01 → Rename to G3.11
- Current G3.11 → Becomes G3.12
- Current G3.12 → Becomes G3.13

### G5 Renumbering (due to additions):
- Insert T15.G5.11 (clear prints)
- Insert T15.G5.12 (basic TTS)
- Insert T15.G5.13 (widget styling)
- Insert T15.G5.14 (dropdown menus)
- Insert T15.G5.15 (animation timing)
- Shift all current G5.11+ skills down by 5

### G6 Renumbering (due to additions):
- Insert T15.G6.05 (basic speech recognition)
- Renumber current G6.05 → G6.06
- Insert T15.G6.07 (rich text)
- Insert T15.G6.08 (sliders)
- Shift subsequent G6 skills

### G7 Renumbering (due to additions):
- Insert T15.G7.03.01 (split text)
- Insert T15.G7.04 (AI backgrounds, if applicable)
- Shift subsequent G7 skills

### G8 Additions:
- Insert T15.G8.04 (3D bubbles)
- Insert T15.G8.05 (camera stories)

---

## FINAL SKILL COUNT ESTIMATE

**Original**: 61 skills
**Added**: ~15-17 new skills (depending on platform verification)
**Removed**: 0 skills
**Final**: ~76-78 skills

Distribution estimate:
- K: 3 (unchanged)
- G1: 3 (unchanged)
- G2: 3 (unchanged)
- G3: 17 (was 16, +1 from split/reorder)
- G4: 8 (unchanged)
- G5: 15 (was 10, +5 new)
- G6: 9 (was 5, +4 new)
- G7: 5 (was 3, +2 new)
- G8: 11 (was 6, +5 new)

This creates better scaffolding in G5-G8 where complex storytelling features are introduced.

---

## IMPLEMENTATION CHECKLIST

- [ ] Phase 1: Fix all HIGH priority block syntax issues (8 skills)
- [ ] Phase 1: Add text-to-speech foundation (2 new skills)
- [ ] Phase 1: Add speech recognition foundation (2 new skills)
- [ ] Phase 2: Add scaffolding skills (5 new skills)
- [ ] Phase 2: Reorder G3 skills for better progression
- [ ] Phase 3: Add widget enhancement skills (4 new skills)
- [ ] Phase 3: Modify scene manager for widget control
- [ ] Phase 4: Add advanced feature skills (4-5 new skills)
- [ ] Phase 4: Modify save/load system details
- [ ] Verify dependencies to T09, T12, T14, T16, T17
- [ ] Add missing skills to other topics if needed
- [ ] Update dependency graph
- [ ] Renumber all affected skill IDs
- [ ] Test sample progression paths for scaffolding

---

End of Implementation Solutions Document
