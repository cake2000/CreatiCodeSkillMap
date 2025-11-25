# T16 Skills - Complete Revised Skill Definitions
**Ready for Copy-Paste into allskills.md**

This document contains all NEW and REVISED skill definitions that result from the T16 optimization.
These are ready to be copied directly into allskills.md.

---

## NEW SKILLS (6 new skill definitions)

### T16.G4.07.A - Add and use checkbox widgets

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

---

### T16.G4.07.B - Add and use radio button widgets

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

---

### T16.G5.06.01 - Add a chat window widget (REPLACES OLD VERSION)

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

---

### T16.G5.06.02 - Append messages to chat window

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

---

### T16.G5.06.03 - Update streaming chat messages

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

---

### T16.G6.06.01 - Add menu groups and items to menu bar

```
ID: T16.G6.06.01
Topic: T16 – User Interfaces
Skill: Add menu groups and items to menu bar
Description: After creating a menu bar, use "add menu group [GROUPNAME] to menu bar [MENUBARNAME v]" block to add menu groups (File, Edit, View, Help). Each group appears as a clickable label on the menu bar. Then use "add menu item [ITEMNAME] to group [GROUPNAME] in menu bar [MENUBARNAME v]" block to add items within each group. When users click a group name, a dropdown appears showing all items in that group. Organize related commands into logical groups (File: New, Open, Save; Edit: Cut, Copy, Paste; View: Zoom In, Zoom Out). Menu groups and items create a hierarchical navigation structure. To respond to menu selections, use skill T16.G6.06.02.

Dependencies:
* T16.G6.06: Add a menu bar widget
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
```

---

## REVISED SKILLS (3 skill revisions)

### T16.G5.05 - Add a video widget to the stage (REVISED)

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

---

### T16.G6.06 - Add a menu bar widget (REVISED)

```
ID: T16.G6.06
Topic: T16 – User Interfaces
Skill: Add a menu bar widget
Description: Use "add menu bar at X (X) Y (Y) width (WIDTH) height (HEIGHT) as [NAME]" block to create an empty application-style menu bar. The menu bar widget provides a horizontal bar at the specified position where you can add menu groups (like File, Edit, View, Help). The menu bar is initially empty and displays no menus until you add menu groups using skill T16.G6.06.01. Menu bars are common in desktop applications and provide organized access to commands and features. Position the menu bar at the top of your interface (Y around 170) for a traditional application layout.

Dependencies:
* T16.G5.01: Create a multi‑screen app with a navigation interface
* T16.G4.03: Add a dropdown menu widget
```

---

### T16.G6.06.02 - Handle menu item click events (RENUMBERED + REVISED)

**NOTE: This was previously T16.G6.06.01**

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

## SKILLS WITH DEPENDENCY UPDATES ONLY (4 skills)

These skills only need their dependency lists updated. The skill name and description remain unchanged.

### T16.G4.07.01 - Add and use tabs widget for organizing content

**CHANGE REQUIRED:** Update dependency from T16.G4.07 to T16.G4.07.B

**Find this line in dependencies:**
```
* T16.G4.07: Add checkbox and radio button widgets
```

**Replace with:**
```
* T16.G4.07.B: Add and use radio button widgets
```

**Full dependency list after change:**
```
Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T16.G3.07: Show and hide widgets
* T16.G4.07.B: Add and use radio button widgets
```

---

### T16.G4.08 - Build a simple settings panel

**CHANGE REQUIRED:** Update dependency from T16.G4.07 to T16.G4.07.A

**Find this line in dependencies:**
```
* T16.G4.07: Add checkbox and radio button widgets
```

**Replace with:**
```
* T16.G4.07.A: Add and use checkbox widgets
```

**Full dependency list after change:**
```
Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T16.G4.06: Read and respond to slider value changes
* T16.G4.07.A: Add and use checkbox widgets
```

---

### T16.G5.02 - Design a form with multiple inputs and validation

**CHANGE REQUIRED:** Update dependency from T16.G4.07 to T16.G4.07.A

**Find this line in dependencies:**
```
* T16.G4.07: Add checkbox and radio button widgets
```

**Replace with:**
```
* T16.G4.07.A: Add and use checkbox widgets
```

**Full dependency list after change:**
```
Dependencies:
* T16.G4.07.A: Add and use checkbox widgets
* T08.G3.05: Fix a condition that uses the wrong operator
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.01.01: Create a new variable with a descriptive name
```

---

### T16.G6.06.02 - Navigate to other projects

**NOTE:** This skill ID is unchanged, but verify it doesn't conflict with the renumbered menu skill.
If there's a conflict, this skill may need to be renumbered to T16.G6.06.03 or T16.G6.07.

**No changes required for this skill** - but verify its placement in the file.

---

## DELETION LIST

These skills should be completely removed from allskills.md:

1. **T16.G4.07** - Add checkbox and radio button widgets (split into .A and .B)
2. **OLD T16.G5.06.01** - Create a chat window widget for messaging (replaced by new version)

---

## INSERTION ORDER IN ALLSKILLS.MD

When inserting these skills into allskills.md, follow this order to maintain proper skill ID sequencing:

### In G4 section (after T16.G4.06):
1. Insert **T16.G4.07.A** (checkboxes)
2. Insert **T16.G4.07.B** (radio buttons)
3. Keep **T16.G4.07.01** (tabs) with updated dependency
4. Keep **T16.G4.08** with updated dependency
5. Continue with rest of G4 skills...

### In G5 section:
1. Keep T16.G5.01, T16.G5.02 (update dependencies), T16.G5.03, T16.G5.04
2. Keep T16.G5.04.01, T16.G5.04.02
3. Replace **T16.G5.05** with revised version
4. Keep T16.G5.05.01, T16.G5.05.02 (no changes)
5. Keep T16.G5.06 (rich textbox)
6. Replace **T16.G5.06.01** with new version (add chat window)
7. Insert **T16.G5.06.02** (append messages)
8. Insert **T16.G5.06.03** (update streaming)
9. Continue with T16.G5.07, T16.G5.08...

### In G6 section:
1. Keep T16.G6.01 through T16.G6.05
2. Replace **T16.G6.06** with revised version
3. Insert **T16.G6.06.01** (add menu groups and items)
4. Renumber old T16.G6.06.01 to **T16.G6.06.02** (handle menu events)
5. Check if old T16.G6.06.02 needs renumbering to T16.G6.06.03 or T16.G6.07

---

## VALIDATION CHECKLIST

After making all changes:

- [ ] Total T16 skills = 68
- [ ] All skill IDs are unique
- [ ] No gaps in skill numbering (or gaps are intentional)
- [ ] All dependency references point to existing skills
- [ ] No skills reference deleted T16.G4.07 or old T16.G5.06.01
- [ ] T16.G4.07.A and T16.G4.07.B both exist
- [ ] T16.G5.06.01, .02, .03 all exist
- [ ] T16.G6.06, T16.G6.06.01, T16.G6.06.02 all exist
- [ ] Skill progression is logical (dependencies come before dependent skills)

---

## SUMMARY OF CHANGES

**Deletions:** 2 skills
- T16.G4.07 (split)
- Old T16.G5.06.01 (split)

**Additions:** 6 new skills
- T16.G4.07.A (checkboxes)
- T16.G4.07.B (radio buttons)
- T16.G5.06.01 (add chat window - new version)
- T16.G5.06.02 (append messages)
- T16.G5.06.03 (update streaming)
- T16.G6.06.01 (add menu groups and items)

**Revisions:** 3 skills
- T16.G5.05 (video widget - simplified)
- T16.G6.06 (menu bar - simplified)
- T16.G6.06.02 (menu events - renumbered from .01)

**Dependency Updates:** 4 skills
- T16.G4.07.01 (tabs)
- T16.G4.08 (settings panel)
- T16.G5.02 (form validation)
- T16.G6.06.02 (old skill, may need renumbering)

**Net Result:** 63 → 68 skills (+5 skills)
