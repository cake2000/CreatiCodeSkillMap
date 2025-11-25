# T16 (User Interfaces) - Optimization Summary (COMPLETED)
**Date:** November 25, 2025
**Before Optimization:** 63 skills
**After Optimization:** 68 skills (+5 skills)

---

## EXECUTIVE SUMMARY

T16 (User Interfaces) has been optimized to break down complex skills into smaller, more manageable units focused on single blocks/concepts. This follows the IXL-style principle where each skill teaches ONE concept well.

**Issues Fixed:**
1. **T16.G4.07** - SPLIT: Checkbox AND radio button widgets into separate skills
2. **T16.G5.06.01** - SPLIT: Chat window creation + appending + updating into 3 skills
3. **T16.G6.06** - SPLIT: Menu bar creation + groups/items + events into 3 skills
4. Various dependency updates to reflect new skill structure

---

## HIGH PRIORITY: SKILLS TO SPLIT

### 1. T16.G4.07 - Split Checkboxes and Radio Buttons

**PROBLEM:** This skill combines TWO fundamentally different widget types:
- Checkboxes: Allow multiple independent selections
- Radio buttons: Allow only one mutually exclusive selection

These are different concepts with different use cases and should be taught separately.

**CURRENT SKILL:**
```
ID: T16.G4.07
Skill: Add checkbox and radio button widgets
Description: Use "add checkbox at X (X) Y (Y) named [NAME]" block to create toggle options that allow multiple selections. Use "add radio buttons [CHOICE1] [CHOICE2]...[CHOICE6] [horizontal/vertical v] at x (X) y (Y) width (WIDTH) height (HEIGHT) named [NAME]" block to create mutually exclusive selections (only one can be selected at a time)...
```

**RECOMMENDED SPLIT:**

**NEW T16.G4.07.A - Add and use checkbox widgets**
```
ID: T16.G4.07.A
Topic: T16 – User Interfaces
Skill: Add and use checkbox widgets
Description: Use "add checkbox at X (X) Y (Y) named [NAME]" block to create toggle options. The checkbox value is 0 when unchecked and 1 when checked. Use "value of widget [NAME v]" to read its state. Use "set value to [V] for widget [NAME v]" to check (V=1) or uncheck (V=0) it programmatically. Use "when widget [NAME v] clicked" or "when widget [NAME v] changes" to respond to user interactions. Checkboxes are used for settings where multiple options can be on simultaneously (e.g., enable sound, enable music, enable vibration - all independent). Each checkbox is an independent toggle, unlike radio buttons which are mutually exclusive.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G3.04: Trace code with a single if/else
* T16.G4.02: Style widget appearance
```

**NEW T16.G4.07.B - Add and use radio button widgets**
```
ID: T16.G4.07.B
Topic: T16 – User Interfaces
Skill: Add and use radio button widgets
Description: Use "add radio buttons [CHOICE1] [CHOICE2] [CHOICE3] [CHOICE4] [CHOICE5] [CHOICE6] [horizontal/vertical v] at x (X) y (Y) width (WIDTH) height (HEIGHT) named [NAME]" block to create mutually exclusive selections (only one can be selected at a time). Radio buttons support up to 6 choices with horizontal or vertical orientation. All radio buttons in a group share the same widget name. Use "value of widget [NAME v]" to get which option is selected. Use "set value to [TEXT] for widget [NAME v]" to programmatically select an option by its text. Use radio buttons when only one choice is allowed (e.g., difficulty: Easy, Medium, Hard - only one can be selected). The mutual exclusivity is enforced automatically when they share the same group/widget name. This is different from checkboxes which allow multiple independent selections.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G3.04: Trace code with a single if/else
* T16.G4.02: Style widget appearance
```

**UPDATE DEPENDENCIES:**
- T16.G4.07.01 (tabs widget) should now depend on **T16.G4.07.B** instead of T16.G4.07
- T16.G4.08 (settings panel) should now depend on **T16.G4.07.A** instead of T16.G4.07
- T16.G5.02 (form validation) should now depend on **T16.G4.07.A** instead of T16.G4.07

---

### 2. T16.G5.05 - Simplify Video Embedding Skill

**PROBLEM:** Current skill is too broad, covering BOTH adding a video widget AND understanding basic control concepts. The sub-skills (T16.G5.05.01 and T16.G5.05.02) cover advanced features but the base skill itself needs to focus on just adding the video.

**CURRENT SKILL:**
```
ID: T16.G5.05
Skill: Embed and control a video widget
Description: [covers adding video AND mentions controls]
```

**RECOMMENDED CHANGE:**

**REVISED T16.G5.05 - Add a video widget**
```
ID: T16.G5.05
Topic: T16 – User Interfaces
Skill: Add a video widget to the stage
Description: Use "add youtube video [URL] at X (X) Y (Y) width (WIDTH) height (HEIGHT) named [NAME] in [foreground/background v]" block to embed a YouTube video. Set the video's URL, position, size, name, and layer. Use foreground layer for interactive videos users can click to play/pause. Use background layer for non-interactive videos that play automatically. The video widget displays the YouTube video within your project. Video widgets are useful for tutorials, cutscenes, educational content, or entertainment. For controlling video playback programmatically (pause, seek, volume, speed), see skill T16.G5.05.01. For responding to video events, see skill T16.G5.05.02.

Dependencies:
* T16.G5.01: Create a multi‑screen app with a navigation interface
* T16.G4.09: Respond to hover events on widgets
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name
```

**NOTE:** T16.G5.05.01 and T16.G5.05.02 already properly break down the advanced features (controls and events). No changes needed to those sub-skills.

---

### 3. T16.G5.06.01 - Split Chat Window Operations

**PROBLEM:** This skill combines THREE distinct operations:
1. Creating a chat window widget
2. Appending messages to the chat
3. Updating the last message (for streaming)

Each of these is a separate block and concept that should be taught individually.

**CURRENT SKILL:**
```
ID: T16.G5.06.01
Skill: Create a chat window widget for messaging
Description: The chat window automatically creates a scrollable message history panel, a text input box, and a send button... Use "append to chat"... Use "update last chat message"...
```

**RECOMMENDED SPLIT:**

**NEW T16.G5.06.01 - Add a chat window widget**
```
ID: T16.G5.06.01
Topic: T16 – User Interfaces
Skill: Add a chat window widget
Description: Use "add chat window x (X) y (Y) width (WIDTH) height (HEIGHT) input rows (ROWS) background [BG] border [BORDERCOLOR] name [NAME]" block to create a chat interface. The chat window automatically creates two parts: at the bottom is a text input box on the left and a send button on the right; on the top is a scrollable chat history panel for displaying messages. The input box can have multiple rows (set ROWS to 1 for single line, 2+ for multi-line input). Style the chat window using background and border colors. Chat windows combine multiple UI elements (text input, button, scrollable panel) into a single widget for interactive conversations. Once created, you can add messages to the chat using skill T16.G5.06.02, and update streaming messages using skill T16.G5.06.03.

Dependencies:
* T16.G5.06: Add a rich textbox for formatted content
* T16.G4.08: Build a simple settings panel
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name
```

**NEW T16.G5.06.02 - Append messages to chat window**
```
ID: T16.G5.06.02
Topic: T16 – User Interfaces
Skill: Append messages to chat window
Description: Use "append to chat [CHATNAME v] message [MESSAGE] as [SENDER] icon [ICON v] align [ALIGN v] text size (TEXTSIZE) color [COLOR] background [BG]" block to add a new message to the chat history panel. Customize the message appearance with sender name, icon (robot icon, user icon, or custom costume from your sprite's costumes), alignment (left for received messages, right for sent messages), text size, text color, and background color. Each appended message appears as a new entry in the scrollable chat history. Messages can be appended when the user clicks the send button, or programmatically (e.g., for chatbot responses, system notifications, or multiplayer chat). The chat automatically scrolls to show the newest message.

Dependencies:
* T16.G5.06.01: Add a chat window widget
* T16.G3.02: Handle a button click event
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name
```

**NEW T16.G5.06.03 - Update streaming chat messages**
```
ID: T16.G5.06.03
Topic: T16 – User Interfaces
Skill: Update streaming chat messages
Description: Use "update last chat message to [MESSAGE] for chat [CHATNAME v]" block to modify the most recent message in the chat history panel. This block replaces the text of the last message with new text without adding a new message entry. This is useful for streaming AI responses (where the chatbot's message builds up word by word), correcting errors in the last message, or updating status messages (changing "Typing..." to the actual message). Unlike appending which adds a new message, updating modifies the existing last message in place. This creates a smooth typing effect for chatbots or real-time message updates.

Dependencies:
* T16.G5.06.02: Append messages to chat window
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name
```

**NOTE:** The original T16.G5.06.01 should be DELETED and replaced with these three new skills.

---

### 4. T16.G6.06 - Split Menu Bar Operations

**PROBLEM:** This skill combines THREE distinct operations:
1. Creating the menu bar widget
2. Adding menu groups (File, Edit, View)
3. Adding menu items within groups

These are separate blocks and concepts that build upon each other.

**CURRENT SKILL:**
```
ID: T16.G6.06
Skill: Create a menu bar with groups and items
Description: Use "add menu bar at X (X) Y (Y) width (WIDTH) height (HEIGHT) as [NAME]" block to create application-style menus. Use "add menu group" to add menu groups (File, Edit, View). Use "add menu item" to add items within each group...
```

**RECOMMENDED SPLIT:**

**REVISED T16.G6.06 - Add a menu bar widget**
```
ID: T16.G6.06
Topic: T16 – User Interfaces
Skill: Add a menu bar widget
Description: Use "add menu bar at X (X) Y (Y) width (WIDTH) height (HEIGHT) as [NAME]" block to create an empty application-style menu bar. The menu bar widget provides a horizontal bar at the specified position where you can add menu groups (like File, Edit, View, Help). The menu bar is initially empty and displays no menus until you add menu groups using skill T16.G6.06.01. Menu bars are common in desktop applications and provide organized access to commands and features. Position the menu bar at the top of your interface (Y around 170) for a traditional application layout.

Dependencies:
* T16.G5.01: Create a multi‑screen app with a navigation interface
* T16.G4.03: Add a dropdown menu widget
```

**NEW T16.G6.06.01 - Add menu groups and items to menu bar**
```
ID: T16.G6.06.01
Topic: T16 – User Interfaces
Skill: Add menu groups and items to menu bar
Description: After creating a menu bar, use "add menu group [GROUPNAME] to menu bar [MENUBARNAME v]" block to add menu groups (File, Edit, View, Help). Each group appears as a clickable label on the menu bar. Then use "add menu item [ITEMNAME] to group [GROUPNAME] in menu bar [MENUBARNAME v]" block to add items within each group. When users click a group name, a dropdown appears showing all items in that group. Organize related commands into logical groups (File: New, Open, Save; Edit: Cut, Copy, Paste; View: Zoom In, Zoom Out). Menu groups and items create a hierarchical navigation structure. To respond to menu selections, use skill T16.G6.06.02.

Dependencies:
* T16.G6.06: Add a menu bar widget
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
```

**REVISED T16.G6.06.02 - Handle menu item click events**
```
ID: T16.G6.06.02
Topic: T16 – User Interfaces
Skill: Handle menu item click events
Description: Use "when menu item [ITEMNAME] from group [GROUPNAME] clicked" event block to respond when users select menu items. Connect menu selections to actions (show/hide widgets, change settings, trigger functions, broadcast messages). For example, "when menu item [Save] from group [File] clicked" can save project data to a list. Compare menu bars to other navigation patterns: menu bars are best for many organized commands (like desktop apps), dropdowns are best for selecting one option from a list, tabs are best for switching between different views, and buttons are best for 2-4 primary actions.

Dependencies:
* T16.G6.06.01: Add menu groups and items to menu bar
* T06.G3.02: Build a key‑press script that controls a sprite
```

---

## MEDIUM PRIORITY: CLARIFICATIONS NEEDED

### 1. T16.G3.08 - Position and resize widgets

**ISSUE:** The description is comprehensive but could be clearer about the animation capabilities.

**RECOMMENDED CLARIFICATION:**
Update the description to mention at the end: "These blocks provide smooth widget animation capabilities. For more complex widget animations including transparency, scaling, and rotation, see skill T16.G5.04.02."

No ID change needed, just a small description update for better cross-referencing.

---

### 2. T16.G4.02 vs T16.G4.02.01 - Image confusion

**CURRENT STATE:** These skills are well-differentiated:
- T16.G4.02: Adding decorative images ON TOP OF widgets (icons on buttons)
- T16.G4.02.01: Standalone image widgets

**RECOMMENDATION:** No changes needed. The descriptions clearly distinguish between the two use cases.

---

### 3. T16.G7.05 - Display data as charts

**CURRENT STATE:** This is a comprehensive skill covering all chart types (bar, line, pie, percentage) and both data sources (lists and tables).

**ANALYSIS:** While this skill covers multiple chart types, they all use essentially the same block with different parameters. This is acceptable as a single skill because:
- The block interface is consistent across chart types
- The main concept is "visualizing data as charts"
- Students learn the general pattern once and can apply it to any chart type

**RECOMMENDATION:** No changes needed. This is appropriately scoped as a single skill.

---

## DEPENDENCY UPDATES REQUIRED

### Direct Impact from Splits:

**Skills that depend on OLD T16.G4.07:**
1. **T16.G4.07.01** (tabs) → Change to **T16.G4.07.B** (radio buttons)
2. **T16.G4.08** (settings panel) → Change to **T16.G4.07.A** (checkboxes)
3. **T16.G5.02** (form validation) → Change to **T16.G4.07.A** (checkboxes)

**Skills that depend on OLD T16.G5.06.01:**
- None found. This is a leaf skill with no dependents.

**Skills that depend on T16.G6.06:**
1. **T16.G6.06.01** (handle menu events) → BECOMES child of new T16.G6.06.01, needs renumbering
   - OLD T16.G6.06.01 → NEW T16.G6.06.02

---

## SUMMARY OF ALL CHANGES

### NEW SKILLS TO ADD (7 total):
1. **T16.G4.07.A** - Add and use checkbox widgets
2. **T16.G4.07.B** - Add and use radio button widgets
3. **T16.G5.06.01** - Add a chat window widget (replaces old T16.G5.06.01)
4. **T16.G5.06.02** - Append messages to chat window
5. **T16.G5.06.03** - Update streaming chat messages
6. **T16.G6.06.01** - Add menu groups and items to menu bar

### SKILLS TO DELETE (2 total):
1. **T16.G4.07** - Add checkbox and radio button widgets (split into .A and .B)
2. **OLD T16.G5.06.01** - Create a chat window widget for messaging (split into 3 skills)

### SKILLS TO REVISE (3 total):
1. **T16.G5.05** - Simplify to focus on adding video only
2. **T16.G6.06** - Simplify to focus on adding menu bar only
3. **T16.G6.06.02** - Update description for menu item events (was T16.G6.06.01)

### SKILLS WITH DEPENDENCY UPDATES (4 total):
1. **T16.G4.07.01** - Update dependency from T16.G4.07 to T16.G4.07.B
2. **T16.G4.08** - Update dependency from T16.G4.07 to T16.G4.07.A
3. **T16.G5.02** - Update dependency from T16.G4.07 to T16.G4.07.A
4. **T16.G6.06.02** - Update dependency from old T16.G6.06.01 to new T16.G6.06.01

### NET CHANGE:
- Starting: 63 skills
- Deletions: -2
- Additions: +7
- Net change: +5
- **Final Total: 68 skills**

---

## IMPLEMENTATION PLAN

### Phase 1: Split T16.G4.07 (Checkboxes and Radio Buttons)
1. Add T16.G4.07.A (checkboxes)
2. Add T16.G4.07.B (radio buttons)
3. Delete T16.G4.07
4. Update dependencies in T16.G4.07.01, T16.G4.08, T16.G5.02

### Phase 2: Simplify T16.G5.05 (Video Widget)
1. Revise T16.G5.05 description to focus on adding video only
2. Verify T16.G5.05.01 and T16.G5.05.02 are correct (no changes needed)

### Phase 3: Split T16.G5.06.01 (Chat Window)
1. Replace T16.G5.06.01 with new version (add chat window)
2. Add T16.G5.06.02 (append messages)
3. Add T16.G5.06.03 (update streaming messages)

### Phase 4: Split T16.G6.06 (Menu Bar)
1. Revise T16.G6.06 (add menu bar widget only)
2. Add T16.G6.06.01 (add groups and items)
3. Renumber old T16.G6.06.01 to T16.G6.06.02 (handle events)
4. Update T16.G6.06.02 description and dependencies

### Phase 5: Verification
1. Check all T16 skills for consistency
2. Verify all dependencies are valid
3. Check for any orphaned skills
4. Ensure skill progression is logical

---

## RATIONALE

These changes align T16 skills with the single-concept principle:
- **One skill = One block or one closely related concept**
- Each skill teaches exactly what students need to know to use ONE block effectively
- Complex widgets are broken down into creation → manipulation → events
- Skills build incrementally without overwhelming students

The splits ensure:
1. Clear learning objectives per skill
2. Better assessment granularity
3. More flexible curriculum sequencing
4. Reduced cognitive load per skill
5. Alignment with actual block structure in CreatiCode

---

## BLOCKS COVERED BY T16 SKILLS

### ✅ Fully Covered Widget Blocks:
- Text widgets: textbox, rich textbox, label
- Button widgets: button, checkbox, radio buttons
- Input widgets: slider, dropdown menu, date picker, color picker
- Display widgets: image (costume/URL), camera, video
- Advanced widgets: tabs, progress bar, chat window, toolbox, menu bar, link
- Charts: line, bar, pie, percentage (from lists and tables)
- Events: clicked, changes, pointer enter/leave, tab selected, video events, menu item clicked
- Styling: set text style, set widget style
- Transformation: move, resize, scale, rotate, transparency
- Management: show/hide, remove, z-index, enable/disable, release focus, value operations
- Layout: apply layout row
- Navigation: run project, open URL
- Confirmation: confirm dialog with buttons

### ✅ Missing Blocks (Intentionally Not Covered):
- **"clear layout" block** - Minor utility, not worth a dedicated skill
- **"delete costume" block** - Mentioned in T16.G6.05 context but not as main skill
- **"when any button named [pattern] clicked"** - Already covered in T16.G3.02.01

All major widget functionality is covered by current T16 skills!

---

## CONCLUSION

The recommended changes improve T16 skill structure by:
1. Separating combined widget types (checkboxes vs radio buttons)
2. Breaking complex operations into learnable steps (chat window, menu bar)
3. Focusing broad skills on core concepts (video embedding)
4. Maintaining complete coverage of CreatiCode widget blocks

These optimizations will make T16 skills easier to teach, learn, and assess while maintaining comprehensive coverage of CreatiCode's user interface capabilities.
