# T15 – User Interfaces: Grades 5-6 (Optimized)

**Topic Overview:** Advanced interface design with complex widgets, multi-screen navigation, forms, responsive layouts, usability evaluation, and professional design patterns.

---

# ============ GRADE 5 (28 skills) ============

**Grade 5 Focus:** Complex widgets (video, chat, toolbox, joystick), multi-screen apps, forms, HUD, animations, and dynamic widget generation.

---

ID: T15.G5.01
Topic: T15 – User Interfaces
Skill: Build multi-screen apps with navigation
Description: Build a multi-screen application with navigation between views (home, game, settings, results). **Approach 1:** Use buttons to navigate by showing/hiding widget groups using "set widget visible" block. **Approach 2:** Use tabs widget to organize screens into panels. Track current screen in a variable. Create consistent navigation (back buttons, menu) across all screens. **Auto-grading:** Check for multiple screen states, navigation buttons, and screen-switching logic.

Dependencies:
* T15.G4.13: Build a simple settings panel
* T15.G4.12: Add and use tabs widget for organizing content

---

ID: T15.G5.02
Topic: T15 – User Interfaces
Skill: Track current screen state with variables
Description: Use a variable (e.g., "currentScreen") to track which screen is currently displayed. **Pattern:** Set variable to "home", "game", "settings", etc. when navigating. Use the variable in conditionals to determine which widgets to show/hide. **Benefits:** Centralizes navigation logic, makes it easy to check current state, enables "back" functionality by storing previous screen. This is the state management pattern used in professional app development. **Auto-grading:** Verify variable updates on navigation and is used in conditionals.

Dependencies:
* T15.G5.01: Build multi-screen apps with navigation
* T09.G3.01: Create and use a variable to store information

---

ID: T15.G5.03
Topic: T15 – User Interfaces
Skill: Design forms with validation
Description: Create a form interface with multiple text input fields, dropdowns, or checkboxes. **Form design:** Group related inputs, add clear labels, arrange logically top-to-bottom. **Validation:** Check that required fields are not empty, verify text format (e.g., no numbers in name), display error messages next to invalid fields. **Submission:** Create submit button that validates all inputs, shows confirmation message or error list. **Auto-grading:** Check for input widgets, validation conditionals, and error feedback.

Dependencies:
* T15.G4.10: Add and use checkbox widgets
* T15.G4.06: Get the selected value from a dropdown
* T08.G4.14: Use if-else to handle two different cases

---

ID: T15.G5.04
Topic: T15 – User Interfaces
Skill: Add date and color picker widgets
Description: Add specialized picker widgets for form input. **Date picker:** Use "add date picker at X (X) Y (Y) width (WIDTH) height (HEIGHT) as [NAME]" block. Get selected date with "value of widget [NAME]" (returns YYYY-MM-DD format). **Color picker:** Use "add color picker at X (X) Y (Y) size (SIZE) as [NAME]". Get color with "value of widget [NAME]" (returns #RRGGBB hex). **Use cases:** Birthday input, event scheduling (date); theme customization, drawing apps (color). **Auto-grading:** Check for picker widgets and value retrieval.

Dependencies:
* T15.G5.03: Design forms with validation

---

ID: T15.G5.05
Topic: T15 – User Interfaces
Skill: Debug form validation systematically
Description: Systematically debug form validation failures using step-by-step testing. **Process:** (1) Test each input independently with valid/invalid data, (2) Check validation conditions fire correctly, (3) Verify error messages display in right location, (4) Test edge cases (empty strings, special characters), (5) Confirm submit button enables only when all inputs valid. **Tools:** Use "say" blocks to trace which validation fails. **Mindset:** Isolate the problem - test one input at a time. **Auto-grading:** Look for test cases and debugging annotations in comments.

Dependencies:
* T15.G5.03: Design forms with validation
* T15.G4.17: Debug widgets responding to wrong events

---

ID: T15.G5.06
Topic: T15 – User Interfaces
Skill: Build leaderboard displays
Description: Create a leaderboard interface that displays ranked data. **Data structure:** Store scores in a list sorted high-to-low. **Display:** Use labels or a textbox to show rankings (e.g., "1. Alice: 500\n2. Bob: 350"). **Dynamic updates:** When new scores are added, re-sort the list and update the display. **Formatting:** Use consistent spacing, highlight top 3, show player names with scores. **Auto-grading:** Check for list data, sorting logic, and display formatting.

Dependencies:
* T15.G4.01: Style widget text properties
* T10.G3.01: Loop through and process each item in a list

---

ID: T15.G5.07
Topic: T15 – User Interfaces
Skill: Implement responsive HUD for game state
Description: Design a "heads-up display" (HUD) showing real-time game information. **Elements:** Health/progress bar, score label, lives counter, timer, status messages. **Updates:** Use "set widget value" to update labels when variables change. **Positioning:** Place HUD elements at screen edges so they don't block gameplay. **Visibility:** Show/hide elements based on game state (hide "Game Over" until game ends). **Auto-grading:** Verify HUD widgets update when game variables change.

Dependencies:
* T15.G4.09: Read and respond to slider value changes
* T15.G5.06: Build leaderboard displays

---

ID: T15.G5.08
Topic: T15 – User Interfaces
Skill: Add and update progress bars
Description: Use progress bar widget to show completion or status. **Add:** "add progress bar at X (X) Y (Y) width (WIDTH) height (HEIGHT) style [bar/circle v] as [NAME]". **Update:** "set value of widget [NAME] to (VALUE)" where VALUE is 0-100. **Styles:** bar = horizontal fill, circle = radial progress ring. **Colors:** Use "set widget [NAME] [background/foreground v] color [COLOR]" to customize appearance. **Use cases:** Loading screens, health bars, task completion, download progress. **Auto-grading:** Check for progress bar widget and value updates.

Dependencies:
* T15.G5.07: Implement responsive HUD for game state

---

ID: T15.G5.09
Topic: T15 – User Interfaces
Skill: Animate widgets for visual feedback
Description: Animate widgets to provide visual feedback and polish. **Techniques:** (1) Fade in/out by changing opacity 0-100, (2) Slide widgets by changing X/Y position incrementally, (3) Scale widgets by changing width/height, (4) Color transition by interpolating color values. **Timing:** Use "glide" or "wait" blocks for smooth transitions. **Triggers:** Animate on button click (button grows), on hover (highlight), on state change (fade in success message). **Auto-grading:** Check for widget property changes over time with wait/glide blocks.

Dependencies:
* T15.G5.08: Add and update progress bars
* T15.G4.15: Respond to hover events on widgets

---

ID: T15.G5.10
Topic: T15 – User Interfaces
Skill: Embed and control video widgets
Description: Use "add youtube video [URL] at X (X) Y (Y) width (WIDTH) height (HEIGHT) named [NAME] in [foreground/background v]" block to embed a YouTube video. **Playback controls:** "[start/pause/stop/mute/unmute v] video for [VIDEONAME v]". **Seeking:** "seek to (TIME) seconds in video named [VIDEONAME v]". **Volume:** "set volume to (VOLUME) for [VIDEONAME v]" (0-100). **Speed:** "set playback speed ratio (SPEED) for [VIDEONAME v]" (100=normal, 200=2x). **Layers:** foreground = user can click to play/pause; background = non-interactive, plays automatically. **Use cases:** Tutorial videos, game cutscenes, educational content, background ambiance. **Auto-grading:** Check for video widget and control blocks.

Dependencies:
* T15.G5.01: Build multi-screen apps with navigation
* T15.G4.04: Add an image widget to the stage

---

ID: T15.G5.11
Topic: T15 – User Interfaces
Skill: Respond to video playback events
Description: Use video event hat blocks to create interactive video experiences. **Events:** "when video [NAME] start" triggers when playback begins. "when video [NAME] paused" detects pause. "when video [NAME] stopped" triggers when video ends. "when video time is (T) seconds for [NAME]" triggers at specific timestamps. **Status reporter:** "current video time for [VIDEONAME v]" returns current position in seconds. **Applications:** Show quiz at 1:30, display subtitles, trigger animations at key moments, auto-advance to next screen when video ends. **Auto-grading:** Check for video event hat blocks and timestamp-based actions.

Dependencies:
* T15.G5.10: Embed and control video widgets
* T06.G3.02: Build a green-flag script that runs a 3-5 block sequence

---

ID: T15.G5.12
Topic: T15 – User Interfaces
Skill: Add rich textboxes for formatted content
Description: Use "add rich textbox at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (PADDING) mode [input/read-only v] as [NAME]" block to create a text area supporting formatted text. **Input mode:** Users see a toolbar to format text (bold, italic, colors). **Read-only mode:** Display pre-formatted content. **Value format:** "value of widget" returns HTML markup. **Use cases:** Note-taking apps (input), styled instructions (read-only), formatted stories. **Auto-grading:** Check for rich textbox widget and appropriate mode selection.

Dependencies:
* T15.G4.01: Style widget text properties
* T15.G3.11: Add a textbox widget for user input

---

ID: T15.G5.13
Topic: T15 – User Interfaces
Skill: Add chat window widgets
Description: Use "add chat window x (X) y (Y) width (WIDTH) height (HEIGHT) input rows (ROWS) background [BG] border [BORDERCOLOR] name [NAME]" block to create a chat interface. **Structure:** Bottom has text input + send button; top has scrollable message history. **Input rows:** 1 for single-line, 2+ for multi-line input. **Styling:** Set background and border colors (#RRGGBBAA format). Chat windows are compound widgets combining input, button, and scrollable panel for conversations. **Auto-grading:** Check for chat window widget with proper configuration.

Dependencies:
* T15.G5.12: Add rich textboxes for formatted content
* T15.G4.13: Build a simple settings panel

---

ID: T15.G5.14
Topic: T15 – User Interfaces
Skill: Append and update chat messages
Description: **Append messages:** Use "append to chat [CHATNAME v] message [MESSAGE] as [SENDER] icon [ICON v] align [ALIGN v] text size (TEXTSIZE) color [COLOR] background [BG]" block to add messages. **Parameters:** SENDER shows name, ICON can be 'ROBOT', 'USER', or costume name; ALIGN 'Left' for received, 'Right' for sent. **Auto-scroll:** Chat scrolls to newest message. **Update streaming:** Use "update last chat message to [MESSAGE] for chat [CHATNAME v]" to modify the most recent message in-place without adding a new entry. **Use cases:** Streaming AI responses (text builds word-by-word), updating "Typing..." to actual message. **Triggers:** Append on send button click or programmatically for bot responses. **Auto-grading:** Check for both append and update blocks used appropriately.

Dependencies:
* T15.G5.13: Add chat window widgets
* T06.G3.04: Build a key-press script that controls a sprite

---

ID: T15.G5.15
Topic: T15 – User Interfaces
Skill: Create toolbox widgets for item selection
Description: Use "add toolbox at x (X) y (Y) width (WIDTH) height (HEIGHT) row count (ROWCOUNT) column count (COLCOUNT) as [NAME]" to create a grid selector. **Populate:** "set icon to [COSTUME v] at row (R) column (C) for toolbox [NAME]". **Selection:** "value of widget [NAME]" returns selected cell index (1, 2, 3...). **Events:** "when widget [NAME] clicked" and "when widget [NAME] changes". **Use cases:** Game inventories, tool palettes, building block selectors, item shops. **Auto-grading:** Check for toolbox widget, icon population, and selection handling.

Dependencies:
* T15.G4.04: Add an image widget to the stage
* T15.G4.09: Read and respond to slider value changes

---

ID: T15.G5.16
Topic: T15 – User Interfaces
Skill: Create confirmation dialogs with custom buttons
Description: Use "confirm [TEXT] with buttons [BUTTON1] [BUTTON2] [BUTTON3] [BUTTON4] [BUTTON5] [BUTTON6]" reporter block to create modal dialogs. **Behavior:** Pauses execution until user clicks a button; returns clicked button's text. **Buttons:** Up to 6 (blank = hidden). **Use cases:** Save/Cancel decisions, difficulty selection (Easy/Medium/Hard), Yes/No confirmations, error messages with OK. **Auto-grading:** Check for confirm block with multiple button options and response handling.

Dependencies:
* T15.G3.06: Handle a button click event
* T15.G4.06: Get the selected value from a dropdown

---

ID: T15.G5.17
Topic: T15 – User Interfaces
Skill: Create custom modal dialogs
Description: Build custom modal/popup dialogs using widget groups. **Structure:** Create semi-transparent overlay (full-screen button, z-index=50, 50% opacity), place dialog widgets on top (z-index=100). **Content:** Title label, message text, action buttons (OK/Cancel). **Show/hide:** Set all dialog widgets visible=true to show, visible=false to hide. **Modal behavior:** Overlay blocks interaction with widgets behind it. **Benefits vs. confirm block:** Custom styling, more flexibility, can include images/forms. **Auto-grading:** Check for overlay widget, dialog widgets with higher z-index, and show/hide logic.

Dependencies:
* T15.G5.16: Create confirmation dialogs with custom buttons
* T15.G5.09: Animate widgets for visual feedback

---

ID: T15.G5.18
Topic: T15 – User Interfaces
Skill: Add virtual joysticks for touch controls
Description: Use "add joystick to [left/right v] side of screen as [NAME] outer color [OUTERCOLOR] inner color [INNERCOLOR] size [SIZE]%" block to create touch-based game controls. **Positioning:** Left side for movement, right side for camera/actions. **Sizing:** Percentage of screen width (20-40% typical). **Colors:** Customize outer ring and inner knob colors. Joysticks are essential for mobile game interfaces on tablets and phones. **Auto-grading:** Check for joystick widget with proper positioning.

Dependencies:
* T15.G5.07: Implement responsive HUD for game state
* T15.G4.03: Style widget appearance

---

ID: T15.G5.19
Topic: T15 – User Interfaces
Skill: Read joystick input values
Description: Use "joystick [NAME v] [x/y/direction/distance/pressed v]" reporter block to read joystick state. **Reporters:** x (-100 to 100 horizontal), y (-100 to 100 vertical), direction (0-360 degrees), distance (0-100 from center), pressed (true/false). **Applications:** Move sprites using x/y, rotate using direction, control speed using distance. Combine with forever loop to create continuous movement controls. **Auto-grading:** Check for joystick reporter blocks used to control sprite movement or game state.

Dependencies:
* T15.G5.18: Add virtual joysticks for touch controls
* T07.G4.01: Repeat actions for a specific count

---

ID: T15.G5.20
Topic: T15 – User Interfaces
Skill: Design thumb-friendly mobile layouts
Description: Design interfaces optimized for mobile touch interaction following thumb-zone principles. **Thumb zones:** Easy-to-reach = bottom corners and lower third of screen; hard-to-reach = top corners. **Design rules:** Place primary actions (fire button, jump) in bottom corners. Place secondary actions (pause, settings) at top. Size buttons 60×60 pixels minimum for finger taps. Add spacing between clickable elements (20+ pixels). Test on tablet/phone. **Considerations:** Left-handed vs right-handed users, landscape vs portrait orientation. **Auto-grading:** Check button placement in lower screen regions and minimum button sizes.

Dependencies:
* T15.G5.19: Read joystick input values
* T15.G5.07: Implement responsive HUD for game state

---

ID: T15.G5.21
Topic: T15 – User Interfaces
Skill: Implement observer pattern for widget updates
Description: Implement the observer pattern where multiple UI elements automatically update when a shared data value changes. **Pattern:** When "score" variable changes, both the score label AND the progress bar AND the leaderboard update automatically. **Implementation:** Use broadcasts or "when widget changes" events to notify all dependent widgets. **Benefit:** Centralizes data management - change data in one place, all displays update. This is foundational for reactive UI programming. **Auto-grading:** Check for broadcast/event-driven updates where multiple widgets respond to same data change.

Dependencies:
* T15.G5.07: Implement responsive HUD for game state
* T15.G5.06: Build leaderboard displays

---

ID: T15.G5.22
Topic: T15 – User Interfaces
Skill: Test UI behavior against specifications
Description: Write and execute test cases to verify UI behavior matches requirements. **Test structure:** (1) Setup: Create widgets in known state, (2) Action: Simulate user interaction, (3) Verify: Check widget values/visibility match expected. **Example test:** Setup: score=0, label shows "0". Action: click "+1" button. Verify: score=1, label shows "1". **Process:** List all expected behaviors, write test for each, run tests after changes. Develops systematic UI testing mindset. **Auto-grading:** Look for test procedures documented in comments or separate test scripts.

Dependencies:
* T15.G5.21: Implement observer pattern for widget updates
* T15.G4.18: Trace settings panel state changes

---

ID: T15.G5.23
Topic: T15 – User Interfaces
Skill: Document widget update dependencies
Description: Create documentation showing which widgets depend on which data and events. **Format:** Diagram or table listing: Data/Event → Widgets that update. **Example:** "score variable changes → score label, progress bar, leaderboard all update". **Benefits:** Makes system behavior clear, helps debug update issues, guides new developers. **Process:** (1) List all data sources (variables, inputs), (2) Identify all widgets that display each data source, (3) Map the connections. **Auto-grading:** Check for dependency documentation in comments or external document.

Dependencies:
* T15.G5.22: Test UI behavior against specifications
* T15.G3.16: Draw data flow diagrams for widget communication

---

ID: T15.G5.24
Topic: T15 – User Interfaces
Skill: Create transition animations between states
Description: Animate screen transitions to create polished user experience. **Techniques:** (1) Fade: new screen starts at opacity 0, glide to 100 while old screen fades to 0. (2) Slide: new screen enters from right (X=480) while old slides left (X=-480). (3) Zoom: new screen starts small (scale 0%) and grows to 100%. **Timing:** 0.3-0.5 seconds feels responsive. **Polish:** Ease-in/ease-out makes motion feel natural. **Use broadcasts:** "switching to game screen" broadcast triggers animations. **Auto-grading:** Check for opacity/position/scale changes during screen transitions.

Dependencies:
* T15.G5.09: Animate widgets for visual feedback
* T15.G5.01: Build multi-screen apps with navigation

---

ID: T15.G5.25
Topic: T15 – User Interfaces
Skill: Apply the 3-second rule for feedback
Description: Apply the "3-second rule": users must see feedback within 3 seconds of any action. **Immediate (<0.1s):** Button press acknowledgment (color change). **Short (<1s):** Form validation results, simple saves. **Long (1-3s):** Show progress bar for operations that take time. **Very long (>3s):** Provide detailed status ("Processing item 5 of 20..."). **No feedback = user thinks app is broken.** Test: Click every button and verify visible response within 3 seconds. **Auto-grading:** Check for feedback mechanisms (messages, progress bars, animations) triggered by user actions.

Dependencies:
* T15.G5.08: Add and update progress bars
* T15.G4.21: Design feedback timing for user actions

---

ID: T15.G5.26
Topic: T15 – User Interfaces
Skill: Design confirmation patterns for destructive actions
Description: Implement confirmation patterns to prevent accidental destructive actions (delete, clear, reset). **Pattern 1:** Two-step delete (click delete button → confirm dialog → execute). **Pattern 2:** Undo option (execute immediately, show "Undo" button for 5 seconds). **Pattern 3:** Soft delete (move to trash, permanent delete requires second action). **Design:** Make confirm dialog clear about consequences: "Delete all 47 items? This cannot be undone." **When to use:** Any action that loses data or is hard to reverse. **Auto-grading:** Check for confirmation dialogs or undo mechanisms before destructive actions.

Dependencies:
* T15.G5.25: Apply the 3-second rule for feedback
* T15.G5.16: Create confirmation dialogs with custom buttons
* T15.G4.22: Use constraints and defaults to guide users

---

ID: T15.G5.27
Topic: T15 – User Interfaces
Skill: Implement master-detail with editing
Description: Implement master-detail pattern with editing capability. **Master view:** List of items (e.g., contacts) where clicking one item shows its details. **Detail view:** Displays full information for selected item with "Edit" button. **Edit mode:** Form with pre-filled values, "Save" commits changes to list, "Cancel" discards. **Data flow:** Selection → Load item data into detail widgets → Edit → Validate → Update list → Refresh detail display. **Auto-grading:** Check for list selection, detail display, edit form, and save logic.

Dependencies:
* T15.G4.19: Recognize common UI patterns (list-detail)
* T15.G5.03: Design forms with validation

---

ID: T15.G5.28
Topic: T15 – User Interfaces
Skill: Give and receive design feedback constructively
Description: Practice giving and receiving constructive feedback on interface designs. **Giving feedback:** (1) Start with strengths ("The color scheme is clear"), (2) Identify specific issues ("The save button is hard to find"), (3) Suggest improvements ("Try placing save button at bottom right"). Avoid vague criticism ("This looks bad"). **Receiving feedback:** (1) Listen without defending, (2) Ask clarifying questions, (3) Decide which feedback to incorporate. **Activity:** Peer review - exchange projects, provide 3 strengths and 3 improvements each. **Auto-grading:** Provide feedback rubric and examples; assess based on specificity and constructiveness.

Dependencies:
* T15.G5.27: Implement master-detail with editing
* T15.G2.11: Design interfaces together with a partner (unplugged)

---

ID: T15.G5.29
Topic: T15 – User Interfaces
Skill: Generate widgets dynamically from list data
Description: Create widgets programmatically based on list data rather than manually placing each widget. **Pattern:** Loop through list, for each item create a button/label widget positioned at calculated Y coordinate. **Example:** List of ["Apple", "Banana", "Cherry"] → creates 3 buttons at Y=100, 150, 200. **Benefits:** Handles variable-length data, reduces manual work, enables data-driven UIs. **Code structure:** "for each item in list: add button at X=10, Y=(index×50), text=item". **Auto-grading:** Check for widget creation inside loops with position calculated from index.

Dependencies:
* T15.G5.06: Build leaderboard displays
* T10.G4.02: Access list items using index and length
* T07.G4.01: Repeat actions for a specific count

---

ID: T15.G5.30
Topic: T15 – User Interfaces
Skill: Update dynamically generated widgets when data changes
Description: Update dynamically generated widgets when underlying data changes. **Challenge:** Can't reference widgets by individual names when generated in loop. **Solution 1:** Remove all generated widgets, regenerate from updated list. **Solution 2:** Use predictable naming (button1, button2...), update by name. **Solution 3:** Track widget IDs in parallel list, update by ID. **Process:** Data changes → detect change → update/regenerate widgets → refresh display. Efficient UI updates are critical for responsive apps. **Auto-grading:** Check for widget removal/update logic when data list changes.

Dependencies:
* T15.G5.29: Generate widgets dynamically from list data
* T15.G3.18: Remove widgets from the stage

---

# ============ GRADE 6 (21 skills) ============

**Grade 6 Focus:** Usability evaluation, responsive design, camera widgets, menu bars, user research, navigation patterns, and CRUD interfaces.

---

ID: T15.G6.01
Topic: T15 – User Interfaces
Skill: Evaluate interfaces for usability
Description: Examine an existing interface (app screenshot or project) and identify usability issues and strengths. **Evaluation criteria:** Are buttons clearly labeled? Is the layout intuitive? Can users find important actions? Are colors accessible for colorblind users? Is text readable? Do interactions provide feedback? **Activity:** Write 3 strengths and 3 improvements for a given interface. Learn to think like a UX designer. **Auto-grading:** Provide evaluation rubric; assess based on specificity of observations and use of design principles.

Dependencies:
* T15.G5.06: Build leaderboard displays

---

ID: T15.G6.02
Topic: T15 – User Interfaces
Skill: Design interfaces based on user feedback
Description: Design an initial interface (buttons, labels, layout), ask peers or a teacher to try it, gather feedback on usability, and then modify the design to address the feedback. **Process:** (1) Create initial design, (2) User testing - observe users without helping, (3) Collect feedback - what was confusing? what worked well? (4) Redesign based on patterns in feedback, (5) Test again. This introduces the iterative design process. **Auto-grading:** Require documentation of initial design, feedback received, and changes made.

Dependencies:
* T15.G6.01: Evaluate interfaces for usability

---

ID: T15.G6.03
Topic: T15 – User Interfaces
Skill: Use color and contrast to improve readability
Description: Apply color theory to interface design: choosing high-contrast text and backgrounds for readability, avoiding color combinations that are difficult for colorblind users, and using color to highlight important elements. **Contrast ratios:** Text needs 4.5:1 minimum (dark text on light background). **Colorblind-friendly:** Don't rely on red/green alone; use shapes/patterns too. **Hierarchy:** Bright colors draw attention - use for primary actions. **Tools:** Test with colorblind simulators. **Auto-grading:** Check contrast ratios of text/background combinations meet accessibility standards.

Dependencies:
* T15.G5.06: Build leaderboard displays
* T15.G4.03: Style widget appearance

---

ID: T15.G6.04
Topic: T15 – User Interfaces
Skill: Control widget layering with z-index
Description: Control widget layering and stacking order using z-index. Use the "set z-index to (Z) for widget [NAME]" block to determine which widgets appear on top of others (higher z-index = appears in front). **Default z-index:** 10. **Typical values:** 1 (background elements), 10 (normal widgets), 50 (overlay), 100 (dialogs/popups). **Use cases:** Create overlays, popup messages, or modal dialogs that appear over other interface elements. **Auto-grading:** Check for z-index blocks used to layer overlays above content.

Dependencies:
* T15.G6.03: Use color and contrast to improve readability
* T15.G5.16: Create confirmation dialogs with custom buttons

---

ID: T15.G6.05
Topic: T15 – User Interfaces
Skill: Manage widget states for clear feedback
Description: Manage widget states to provide clear feedback. **Enable/disable:** Use "disable widget [NAME]" to grey out and prevent interaction. Use "enable widget [NAME]" to restore interactivity. **Focus:** Use "release focus for widget [NAME]" to deselect/unfocus widgets (remove cursor from text fields, deselect buttons). **Visibility:** Use "set widget [NAME] visible [true/false v]" to show loading indicators or success messages. **Visual states:** Change widget text colors to red for errors, green for success. Widget state management helps users understand what actions are available. **Auto-grading:** Check for enable/disable/focus blocks used to manage interactive states.

Dependencies:
* T15.G6.03: Use color and contrast to improve readability
* T08.G4.22: Trace nested conditions to predict outcomes

---

ID: T15.G6.06
Topic: T15 – User Interfaces
Skill: Create responsive layouts for different screen sizes
Description: Create interfaces that work on different screen sizes using responsive design techniques. **Percentage positioning:** Use "stage width" and "stage height" to calculate widget positions as percentages (X = stage width × 0.5 for center). **Relative sizing:** Calculate widget sizes based on screen size. **Breakpoints:** Detect screen size and choose layout: if width > 800 use two-column, else use single-column. **Test:** Try project on computer (large), tablet (medium), phone (small). **Auto-grading:** Check for stage width/height reporters used in positioning calculations.

Dependencies:
* T15.G5.01: Build multi-screen apps with navigation
* T15.G5.07: Implement responsive HUD for game state
* T15.G4.01: Style widget text properties

---

ID: T15.G6.07
Topic: T15 – User Interfaces
Skill: Test interfaces on multiple device sizes
Description: Systematically test interface layouts on multiple device sizes to verify responsive design. **Device categories:** Desktop (1920×1080), Tablet landscape (1024×768), Tablet portrait (768×1024), Phone (375×667). **Test procedure:** (1) Load project on each size, (2) Check all widgets visible and accessible, (3) Verify text is readable, (4) Confirm buttons are large enough to tap, (5) Test all interactions work. **Document issues:** "On phone, settings button overlaps title." **Auto-grading:** Require test documentation showing results for at least 3 different screen sizes.

Dependencies:
* T15.G6.06: Create responsive layouts for different screen sizes

---

ID: T15.G6.08
Topic: T15 – User Interfaces
Skill: Display camera feed in widgets
Description: Use "add camera x (X) y (Y) width (WIDTH) height (HEIGHT) name [NAME] facing [front/back v]" block to display live camera feed in a widget. **Facing:** front = selfie camera, back = rear camera. **Permissions:** Browser will ask user for camera access. **Use cases:** Video chat apps, AR effects, QR code scanners, photo booth projects. **Combine with:** Video analysis blocks to detect faces, read codes. **Privacy:** Always indicate when camera is active. **Auto-grading:** Check for camera widget and appropriate privacy indicators.

Dependencies:
* T15.G5.10: Embed and control video widgets
* T15.G4.04: Add an image widget to the stage

---

ID: T15.G6.09
Topic: T15 – User Interfaces
Skill: Add menu bar widgets
Description: Use "add menu bar at top of screen with background [COLOR] text color [TEXTCOLOR] height (HEIGHT) as [NAME]" block to create application-style menu bars. **Structure:** Horizontal bar spanning screen width, typically at top. **Styling:** Set background color, text color, and height (30-40 pixels typical). **Purpose:** Professional app navigation, organizing commands into categories (File, Edit, View, Help). **Next step:** Populate menu bar with menu groups and items. **Auto-grading:** Check for menu bar widget with proper positioning and styling.

Dependencies:
* T15.G5.01: Build multi-screen apps with navigation
* T15.G4.05: Add a dropdown menu widget

---

ID: T15.G6.10
Topic: T15 – User Interfaces
Skill: Add menu groups and items to menu bars
Description: Populate menu bars with menu groups and items. **Add group:** "add menu group [LABEL] to menu bar [NAME]" creates a top-level menu (e.g., "File"). **Add items:** "add menu item [LABEL] to group [GROUP] in menu bar [NAME]" adds options under group (e.g., "New", "Open", "Save" under "File"). **Separators:** Use "---" as item label to create visual divider. **Organization:** Group related commands together, order by frequency of use (most common first). **Auto-grading:** Check for menu groups with multiple items added in logical groupings.

Dependencies:
* T15.G6.09: Add menu bar widgets
* T06.G3.02: Build a green-flag script that runs a 3-5 block sequence

---

ID: T15.G6.11
Topic: T15 – User Interfaces
Skill: Handle menu item click events
Description: Respond to menu item selections using "when menu item [ITEM] in group [GROUP] of menu bar [NAME] clicked" hat block. **Pattern:** Each menu item has its own handler script. **Actions:** "New" → clear workspace, "Save" → store data to cloud, "Settings" → show settings screen, "Help" → open help documentation. **Feedback:** Provide confirmation after action completes ("File saved successfully"). **Auto-grading:** Check for menu item event handlers that trigger appropriate actions.

Dependencies:
* T15.G6.10: Add menu groups and items to menu bars
* T06.G3.04: Build a key-press script that controls a sprite

---

ID: T15.G6.12
Topic: T15 – User Interfaces
Skill: Navigate to other projects
Description: Use "open project [URL/ID]" block to navigate from one Scratch project to another, creating multi-project applications. **URL format:** Full project URL or project ID number. **Use cases:** Main menu project that launches game projects, tutorial series where each lesson is a separate project, portfolio project that showcases other projects. **Design consideration:** User can't return automatically - provide navigation back (or use tabs/menu pattern within single project instead). **Auto-grading:** Check for open project blocks with valid project references.

Dependencies:
* T15.G5.01: Build multi-screen apps with navigation

---

ID: T15.G6.13
Topic: T15 – User Interfaces
Skill: Recognize navigation patterns in interfaces
Description: Identify and understand common navigation patterns used in professional apps. **Tab navigation:** Persistent tabs at bottom (mobile) or top (desktop) for main sections. **Menu navigation:** Hamburger menu or menu bar for hierarchical commands. **Wizard navigation:** Step-by-step flow with Next/Previous (setup, checkout). **Breadcrumbs:** Show location in hierarchy (Home > Products > Shoes). **Study activity:** Examine 3 professional apps, identify their navigation pattern, explain why it fits the app's purpose. **Auto-grading:** Students document navigation patterns found in apps with screenshots and explanations.

Dependencies:
* T15.G6.12: Navigate to other projects
* T15.G6.11: Handle menu item click events

---

ID: T15.G6.14
Topic: T15 – User Interfaces
Skill: Trace user paths through multi-screen apps
Description: Map all possible user interaction paths through a multi-screen application. **Method:** Create flowchart showing screens as boxes, navigation actions as arrows. **Example:** Home → [Click Play] → Game → [Click Pause] → Pause Menu → [Click Resume] → Game. **Analysis:** (1) Can users reach every screen? (2) Can users always get back to home? (3) Are there dead ends? (4) Is the path to common tasks short? **Use:** Identify navigation problems before building full interface. **Auto-grading:** Check for complete navigation flowcharts with all screens and transitions documented.

Dependencies:
* T15.G5.02: Track current screen state with variables
* T15.G6.01: Evaluate interfaces for usability

---

ID: T15.G6.15
Topic: T15 – User Interfaces
Skill: Create user personas for design decisions
Description: Create user personas (fictional but realistic user profiles) to guide design decisions. **Persona components:** Name, age, background, goals, frustrations, tech skill level. **Example:** "Maria, 10, loves animals, wants to learn about habitats, frustrated by apps with too much text, comfortable with tablets." **Usage:** When making design decisions, ask "Would Maria understand this?" "Does this help Maria achieve her goal?" **Activity:** Create 2-3 personas for target users, reference them when explaining design choices. **Auto-grading:** Assess persona completeness and evidence of persona-driven design decisions.

Dependencies:
* T15.G6.02: Design interfaces based on user feedback
* T15.G6.01: Evaluate interfaces for usability

---

ID: T15.G6.16
Topic: T15 – User Interfaces
Skill: Write user stories for interface features
Description: Write user stories that describe interface features from user perspective. **Format:** "As a [USER TYPE], I want to [ACTION] so that [BENEFIT]." **Examples:** "As a student, I want to save my progress so that I can continue later." "As a teacher, I want to view student scores so that I can track learning." **Process:** (1) Identify user types, (2) List their goals, (3) Write stories for each goal, (4) Prioritize stories, (5) Design interface to support top stories. **Auto-grading:** Check for properly formatted user stories that cover key features.

Dependencies:
* T15.G6.15: Create user personas for design decisions

---

ID: T15.G6.17
Topic: T15 – User Interfaces
Skill: Build complete CRUD interfaces
Description: Build a complete CRUD (Create, Read, Update, Delete) interface for managing data. **Create:** Form to add new items with validation and "Add" button. **Read:** List or table displaying all items. **Update:** Click item to edit in form, "Save" updates the item in list. **Delete:** Delete button with confirmation ("Delete this item?"). **Data structure:** Store items in list, each edit updates list item at index. **Example app:** Contact manager, task list, inventory system. **Auto-grading:** Verify all four CRUD operations are implemented and functional.

Dependencies:
* T15.G5.27: Implement master-detail with editing
* T15.G5.16: Create confirmation dialogs with custom buttons

---

ID: T15.G6.18
Topic: T15 – User Interfaces
Skill: Write clear UI requirements as prompts
Description: Write clear, detailed UI requirements that could serve as AI prompts or developer specifications. **Format:** "Create a [WIDGET TYPE] that [BEHAVIOR] when [TRIGGER]. It should be positioned [LOCATION] and styled with [STYLE]. Example: [EXAMPLE]." **Good requirement:** "Create a save button that displays a success message when clicked. It should be positioned at bottom-right of the form and styled with green background (#00AA00) and white text. When clicked, it should validate all form fields before saving." **Bad requirement:** "Make a save button." **Auto-grading:** Assess requirements for completeness (widget type, behavior, trigger, position, style).

Dependencies:
* T15.G6.17: Build complete CRUD interfaces
* T15.G6.16: Write user stories for interface features

---

ID: T15.G6.19
Topic: T15 – User Interfaces
Skill: Reverse-engineer professional app navigation
Description: Analyze a professional mobile app or website to understand its navigation architecture. **Process:** (1) Identify all screens/pages, (2) Map how to navigate between them (buttons, menus, gestures), (3) Identify the navigation pattern used (tabs, hamburger menu, etc.), (4) Explain why this pattern fits the app. **Document:** Create navigation map showing all screens and connections. **Reflection:** What makes the navigation effective? What would you change? **Auto-grading:** Assess completeness of navigation documentation and depth of analysis.

Dependencies:
* T15.G6.13: Recognize navigation patterns in interfaces
* T15.G4.23: Identify navigation patterns in professional apps

---

ID: T15.G6.20
Topic: T15 – User Interfaces
Skill: Create widget factory functions using custom blocks
Description: Create custom blocks (widget factories) that generate and style widgets with consistent parameters. **Example:** "create styled button [TEXT] at X (X) Y (Y)" custom block that internally calls "add button", sets background color to brand color, sets text size to 16, adds shadow effect. **Benefits:** Ensures consistency across interface, makes updates easier (change factory → all widgets update), reduces repetitive code. **Parameters:** Text, position, optional style overrides. **Auto-grading:** Check for custom blocks that create widgets with consistent styling.

Dependencies:
* T15.G6.03: Use color and contrast to improve readability
* T15.G5.29: Generate widgets dynamically from list data
* T05.G5.01: Create and use custom blocks to simplify code

---

ID: T15.G6.21
Topic: T15 – User Interfaces
Skill: Build widget style configuration systems
Description: Build a centralized style configuration system using variables or lists to store style values. **Structure:** Create variables like "primaryColor", "buttonHeight", "fontSize". **Usage:** Use these variables in all "add widget" blocks instead of hardcoded values. **Benefits:** Change one variable → entire interface updates. Enables theme switching (light/dark mode). **Advanced:** Store styles in list: ["#0066CC", "16", "bold"] = [buttonColor, fontSize, fontWeight]. **Auto-grading:** Check for style variables used consistently across multiple widget creation blocks.

Dependencies:
* T15.G6.20: Create widget factory functions using custom blocks
* T09.G4.01: Use variables to store and retrieve data

---
