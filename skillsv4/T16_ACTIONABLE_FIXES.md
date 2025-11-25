# T16 Skills - Actionable Fix List
**Quick Reference for Making Changes**

---

## DELETIONS (2 skills)

### 1. DELETE: T16.G4.07
**Reason:** Split into T16.G4.07.A (checkboxes) and T16.G4.07.B (radio buttons)

### 2. DELETE: Old T16.G5.06.01
**Reason:** Split into three skills (T16.G5.06.01, .02, .03)

---

## ADDITIONS (7 skills)

### 1. ADD: T16.G4.07.A
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

### 2. ADD: T16.G4.07.B
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

### 3. REPLACE: T16.G5.06.01 (new version)
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

### 4. ADD: T16.G5.06.02
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

### 5. ADD: T16.G5.06.03
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

### 6. ADD: T16.G6.06.01
```
ID: T16.G6.06.01
Topic: T16 – User Interfaces
Skill: Add menu groups and items to menu bar
Description: After creating a menu bar, use "add menu group [GROUPNAME] to menu bar [MENUBARNAME v]" block to add menu groups (File, Edit, View, Help). Each group appears as a clickable label on the menu bar. Then use "add menu item [ITEMNAME] to group [GROUPNAME] in menu bar [MENUBARNAME v]" block to add items within each group. When users click a group name, a dropdown appears showing all items in that group. Organize related commands into logical groups (File: New, Open, Save; Edit: Cut, Copy, Paste; View: Zoom In, Zoom Out). Menu groups and items create a hierarchical navigation structure. To respond to menu selections, use skill T16.G6.06.02.

Dependencies:
* T16.G6.06: Add a menu bar widget
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
```

### 7. RENUMBER: T16.G6.06.01 → T16.G6.06.02 (handle menu events)
**Note:** This is the existing T16.G6.06.01 being renumbered, not a new skill.

---

## REVISIONS (3 skills)

### 1. REVISE: T16.G5.05
**Old Skill Name:** Embed and control a video widget
**New Skill Name:** Add a video widget to the stage

**Old Description:**
```
Use "add youtube video [URL] at X (X) Y (Y) width (WIDTH) height (HEIGHT) named [NAME] in [foreground/background v]" block to embed a YouTube video. Set the video's URL, position, size, name, and layer. Use foreground layer for interactive videos users can click to play/pause. Use background layer for non-interactive videos that play automatically. Video widgets are useful for tutorials, cutscenes, educational content, or entertainment.
```

**New Description:**
```
Use "add youtube video [URL] at X (X) Y (Y) width (WIDTH) height (HEIGHT) named [NAME] in [foreground/background v]" block to embed a YouTube video. Set the video's URL, position, size, name, and layer. Use foreground layer for interactive videos users can click to play/pause. Use background layer for non-interactive videos that play automatically. The video widget displays the YouTube video within your project. Video widgets are useful for tutorials, cutscenes, educational content, or entertainment. For controlling video playback programmatically (pause, seek, volume, speed), see skill T16.G5.05.01. For responding to video events, see skill T16.G5.05.02.
```

**Dependencies:** (no change)

---

### 2. REVISE: T16.G6.06
**Old Skill Name:** Create a menu bar with groups and items
**New Skill Name:** Add a menu bar widget

**Old Description:**
```
Use "add menu bar at X (X) Y (Y) width (WIDTH) height (HEIGHT) as [NAME]" block to create application-style menus. Use "add menu group" to add menu groups (File, Edit, View). Use "add menu item" to add items within each group. Organize related commands into logical groups.
```

**New Description:**
```
Use "add menu bar at X (X) Y (Y) width (WIDTH) height (HEIGHT) as [NAME]" block to create an empty application-style menu bar. The menu bar widget provides a horizontal bar at the specified position where you can add menu groups (like File, Edit, View, Help). The menu bar is initially empty and displays no menus until you add menu groups using skill T16.G6.06.01. Menu bars are common in desktop applications and provide organized access to commands and features. Position the menu bar at the top of your interface (Y around 170) for a traditional application layout.
```

**Dependencies:** (no change)

---

### 3. REVISE: T16.G6.06.02 (was T16.G6.06.01)
**This is a RENUMBER + DESCRIPTION UPDATE**

**New Description:**
```
Use "when menu item [ITEMNAME] from group [GROUPNAME] clicked" event block to respond when users select menu items. Connect menu selections to actions (show/hide widgets, change settings, trigger functions, broadcast messages). For example, "when menu item [Save] from group [File] clicked" can save project data to a list. Compare menu bars to other navigation patterns: menu bars are best for many organized commands (like desktop apps), dropdowns are best for selecting one option from a list, tabs are best for switching between different views, and buttons are best for 2-4 primary actions.
```

**New Dependencies:**
```
* T16.G6.06.01: Add menu groups and items to menu bar
* T06.G3.02: Build a key‑press script that controls a sprite
```

---

## DEPENDENCY UPDATES (4 skills need dependency changes)

### 1. UPDATE: T16.G4.07.01 (tabs widget)
**Change:** T16.G4.07 → T16.G4.07.B
**Find in dependencies:**
```
* T16.G4.07: Add checkbox and radio button widgets
```
**Replace with:**
```
* T16.G4.07.B: Add and use radio button widgets
```

### 2. UPDATE: T16.G4.08 (settings panel)
**Change:** T16.G4.07 → T16.G4.07.A
**Find in dependencies:**
```
* T16.G4.07: Add checkbox and radio button widgets
```
**Replace with:**
```
* T16.G4.07.A: Add and use checkbox widgets
```

### 3. UPDATE: T16.G5.02 (form validation)
**Change:** T16.G4.07 → T16.G4.07.A
**Find in dependencies:**
```
* T16.G4.07: Add checkbox and radio button widgets
```
**Replace with:**
```
* T16.G4.07.A: Add and use checkbox widgets
```

### 4. UPDATE: T16.G6.06.02 (menu item events)
**Change:** T16.G6.06 → T16.G6.06.01
**Old dependencies:**
```
* T16.G6.06: Create a menu bar with groups and items
```
**New dependencies:**
```
* T16.G6.06.01: Add menu groups and items to menu bar
* T06.G3.02: Build a key‑press script that controls a sprite
```

---

## CHECKLIST FOR IMPLEMENTATION

### Phase 1: Checkbox and Radio Button Split
- [ ] Add T16.G4.07.A (checkboxes)
- [ ] Add T16.G4.07.B (radio buttons)
- [ ] Delete T16.G4.07
- [ ] Update T16.G4.07.01 dependencies (G4.07 → G4.07.B)
- [ ] Update T16.G4.08 dependencies (G4.07 → G4.07.A)
- [ ] Update T16.G5.02 dependencies (G4.07 → G4.07.A)

### Phase 2: Video Widget Simplification
- [ ] Revise T16.G5.05 description and skill name
- [ ] Verify T16.G5.05.01 is unchanged
- [ ] Verify T16.G5.05.02 is unchanged

### Phase 3: Chat Window Split
- [ ] Delete old T16.G5.06.01
- [ ] Add new T16.G5.06.01 (add chat window)
- [ ] Add T16.G5.06.02 (append messages)
- [ ] Add T16.G5.06.03 (update streaming)

### Phase 4: Menu Bar Split
- [ ] Revise T16.G6.06 description and skill name
- [ ] Add T16.G6.06.01 (add groups and items)
- [ ] Renumber old T16.G6.06.01 to T16.G6.06.02
- [ ] Revise T16.G6.06.02 description
- [ ] Update T16.G6.06.02 dependencies

### Phase 5: Verification
- [ ] Count total T16 skills (should be 68)
- [ ] Verify no broken dependency references
- [ ] Check skill numbering is sequential
- [ ] Validate all new skill descriptions
- [ ] Test dependency chain integrity

---

## QUICK STATS

**Before:**
- Total skills: 63
- Skills with issues: 4

**After:**
- Total skills: 68
- Deletions: 2
- Additions: 7 (includes 1 renumber)
- Revisions: 3
- Dependency updates: 4

**Net change:** +5 skills
