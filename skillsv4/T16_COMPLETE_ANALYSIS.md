# T16 (User Interfaces) - Complete Analysis for Optimization

## EXECUTIVE SUMMARY

**Total T16 Skills Found:** 64 skills (from K through G8)
**Total Widget Blocks Available:** 71 widget blocks in CreatiCode

This analysis provides the complete list of all T16 skills and all widget blocks from the CreatiCode platform to support optimization work.

---

## PART 1: ALL T16 SKILLS (COMPLETE LIST)

ID: T16.K.01
Topic: T16 – User Interfaces
Skill: Identify buttons in everyday interfaces (pictures)
Description: Look at pictures of interfaces (remote control, microwave, toy, tablet screen) and point to buttons. Understand that buttons are things you press to make something happen.

Dependencies:
* None


ID: T16.K.02
Topic: T16 – User Interfaces
Skill: Recognize labels and text displays (pictures)
Description: Look at pictures of interfaces and identify where text appears (TV screen showing channel number, microwave display showing time, sign on door). Understand that some parts of screens show information.

Dependencies:
* T16.K.01: Identify buttons in everyday interfaces (pictures)


ID: T16.G1.01
Topic: T16 – User Interfaces
Skill: Match interface elements to their purpose (unplugged)
Description: Given pictures of interface elements (button, slider, text box, picture) and pictures of purposes (click to start, move to change volume, type your name, look at photo), draw lines connecting each element to its purpose.

Dependencies:
* T16.K.02: Recognize labels and text displays (pictures)


ID: T16.G1.02
Topic: T16 – User Interfaces
Skill: Arrange interface elements on a screen (unplugged)
Description: Cut out paper shapes representing buttons, labels, and pictures. Arrange them on a paper "screen" to create a simple interface (e.g., game menu with title, start button, and picture).

Dependencies:
* T16.G1.01: Match interface elements to their purpose (unplugged)


ID: T16.G2.01
Topic: T16 – User Interfaces
Skill: Identify what happens when you interact with interfaces (picture-based)
Description: Look at before/after pictures showing interface interactions (button pressed → light turns on, slider moved → volume changes, text typed → letters appear). Describe what changed.

Dependencies:
* T16.G1.02: Arrange interface elements on a screen (unplugged)


ID: T16.G2.02
Topic: T16 – User Interfaces
Skill: Design a simple interface on paper (unplugged)
Description: Draw a simple interface on paper for a specific purpose (TV remote, game menu, calculator). Include buttons with labels, displays for information, and arrange them logically. Explain what each part does.

Dependencies:
* T16.G2.01: Identify what happens when you interact with interfaces (picture-based)


ID: T16.G3.01
Topic: T16 – User Interfaces
Skill: Add a button widget to the stage
Description: Use "add button [TEXT] at X (X) Y (Y) width (WIDTH) height (HEIGHT) tooltip [TOOLTIP] as [NAME]" block to create a clickable button on the stage. Specify the button's text label, position (X, Y coordinates), size (width and height in pixels), tooltip (text shown on hover), and name. Understand that widgets are UI elements that float above sprites.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T01.G3.01: Complete a simple script with missing blocks


ID: T16.G3.02
Topic: T16 – User Interfaces
Skill: Handle a button click event
Description: Use the "when widget [button1 v] clicked" hat block to detect when a specific button is clicked. The widget name must match the name you gave the button when adding it. Connect button clicks to simple actions like playing a sound, showing a sprite, or broadcasting a message.

Dependencies:
* T16.G3.01: Add a button widget to the stage
* T06.G3.02: Build a key‑press script that controls a sprite


ID: T16.G3.02.01
Topic: T16 – User Interfaces
Skill: Handle any button click with a single script
Description: Use "when any button named [variableName v] clicked" event block to detect when ANY button is clicked. The clicked button's name is automatically stored in the specified variable. This is useful when you have many similar buttons and want to handle them all with one script instead of creating separate scripts for each button. Use conditional blocks to check which button was clicked and take different actions accordingly.

Dependencies:
* T16.G3.02: Handle a button click event
* T09.G3.02: Use a variable in a conditional (if block)


ID: T16.G3.03
Topic: T16 – User Interfaces
Skill: Add a label widget to display text
Description: Use "add label [TEXT] at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (PADDING) as [NAME]" block to create a text display area on the stage. Set the label's initial text content, position, size, padding, and name. Labels are used to show information to the user (scores, messages, instructions) and cannot be edited by the user.

Dependencies:
* T16.G3.01: Add a button widget to the stage


ID: T16.G3.04
Topic: T16 – User Interfaces
Skill: Update label text dynamically
Description: Use the "set widget value" block to change a label's displayed text while the program runs. Connect label updates to events (button clicks, variable changes) to show dynamic information like scores or status messages.

Dependencies:
* T16.G3.03: Add a label widget to display text
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T16.G3.04.01
Topic: T16 – User Interfaces
Skill: Append text to labels and textboxes
Description: Use "append text [NEWTEXT] to [WIDGETNAME v] in new line [Yes/No v]" block to add text to the end of existing widget content without replacing it. Choose "Yes" to add text on a new line, or "No" to add on the same line. Understand the difference between "set value" (replaces all content) and "append text" (adds to existing content). Use appending for building logs, chat histories, or narratives that grow over time.

Dependencies:
* T16.G3.04: Update label text dynamically


ID: T16.G3.05
Topic: T16 – User Interfaces
Skill: Add a textbox widget for user input
Description: Use "add textbox at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (PADDING) line [single/multiple v] scroll [scroll/no scroll v] mode [input/read-only v] as [NAME]" block to create an input field. Set single line for short inputs (names, numbers) or multiple lines for longer text (comments, stories). Enable scrolling for long text. Use input mode to allow typing or read-only mode to display text without editing. Understand the difference between a label (display only, styled) and textbox (can accept user input or display plain text).

Dependencies:
* T16.G3.03: Add a label widget to display text


ID: T16.G3.06
Topic: T16 – User Interfaces
Skill: Get text from a textbox widget
Description: Use the "value of widget" block to retrieve the text that a user typed into a textbox. Store the input in a variable or use it directly in other blocks (e.g., display it in a label, use it in a greeting).

Dependencies:
* T16.G3.05: Add a textbox widget for user input
* T09.G3.02: Use a variable in a conditional (if block)


ID: T16.G3.07
Topic: T16 – User Interfaces
Skill: Show and hide widgets
Description: Use "set visibility [show/hide] for widget named [NAME]" block to show or hide individual widgets. Use "set visibility [show/hide] for all widgets" to show or hide all widgets at once. Create simple interactions where clicking a button shows or hides other widgets (e.g., show instructions when "Help" is clicked, hide a menu after selection).

Dependencies:
* T16.G3.02: Handle a button click event
* T08.G3.01: Use a simple if in a script


ID: T16.G3.07.01
Topic: T16 – User Interfaces
Skill: Remove widgets from the stage
Description: Use "remove widget named [NAME]" to permanently delete a widget from the stage. Use "remove all widgets" to clear all widgets at once. Understand the difference between hiding (temporary, can be shown again) and removing (permanent, widget is deleted). Use removal for screen transitions, game resets, or cleaning up widgets you no longer need.

Dependencies:
* T16.G3.07: Show and hide widgets


ID: T16.G3.08
Topic: T16 – User Interfaces
Skill: Position and resize widgets
Description: Use "move widget [NAME] to X (X) Y (Y) in (T) seconds [blocking v]" to animate widget position over time. Use "resize widget [NAME] to width (W) height (H) in (T) seconds [blocking v]" to animate size changes. Set T to 0 for instant movement, or use larger values for smooth animations. Choose "blocking" to make your script wait until the animation finishes before continuing to the next block (useful when you want things to happen one at a time). Choose "non-blocking" to continue immediately to the next block while animation happens in the background (useful when you want multiple things to animate at the same time). Arrange multiple widgets to create a simple layout (e.g., title at top, buttons below, input fields in the middle).

Dependencies:
* T16.G3.07: Show and hide widgets


ID: T16.G4.01
Topic: T16 – User Interfaces
Skill: Style widget text properties
Description: Use "set text style [FONTSTYLE v] font size (FONTSIZE) text color [TEXTCOLOR] boldness [bold/normal v] text alignment [Left/Middle/Right v] for widget [WIDGETNAME v]" block to style widget text. Choose from many font families (sans-serif for clean modern text, Arial/Helvetica for readability, Bangers/Creepster for fun themed text). Set font size in pixels, text color, bold or normal weight, and alignment. Create visually appealing labels and buttons with appropriate text formatting.

Dependencies:
* T06.G3.09: Fix a script that uses the wrong event type
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T16.G3.08: Position and resize widgets


ID: T16.G4.01.01
Topic: T16 – User Interfaces
Skill: Apply consistent styling across multiple widgets
Description: Apply consistent styling across multiple widgets to create visual cohesion. Use the same color scheme, font family, font sizes, and border styles for all widgets in your project. Style related widgets similarly (all navigation buttons with blue background, all info labels with grey text, all input fields with white background). Consistency makes interfaces look professional and helps users understand which widgets serve similar purposes.

Dependencies:
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T16.G4.01: Style widget text properties


ID: T16.G4.02
Topic: T16 – User Interfaces
Skill: Style widget appearance
Description: Use the "set widget style" block to customize widget backgrounds, borders (width, color, style), and corner radius. Set background color using #RRGGBBAA format (including transparency). Use "add image [costume] to widget named [NAME] at position X Y" or "add image at URL [URL] to widget named [NAME] at position X Y" to add decorative icons or images ON TOP OF other widgets (like adding a logo to a button). For standalone images, use the dedicated image widget skill (T16.G4.02.01). Create buttons and labels that match a visual theme or stand out for emphasis.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T16.G4.01: Style widget text properties


ID: T16.G4.02.01
Topic: T16 – User Interfaces
Skill: Add an image widget to the stage
Description: Use "add image [COSTUMENAME v] at x (X) y (Y) width (WIDTH) height (HEIGHT) aspect ratio [keep/stretch v] as [NAME]" or "add image from URL [URL] at x (X) y (Y) width (WIDTH) height (HEIGHT) aspect ratio [keep/stretch v] as [NAME]" blocks to create standalone image widgets that display pictures on the stage. Choose to keep original aspect ratio or stretch to fit dimensions. These are different from decorative images added TO other widgets. Image widgets are useful for displaying icons, backgrounds, or visual feedback that needs to be positioned precisely.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T16.G3.08: Position and resize widgets


ID: T16.G4.03
Topic: T16 – User Interfaces
Skill: Add a dropdown menu widget
Description: Use "add dropdown menu at X (X) Y (Y) width (WIDTH) height (HEIGHT) using list [LIST v] as [NAME]" block to create a selection menu. The dropdown options are populated from a list variable - the items in the list become the menu choices. Set the dropdown's position, size, and name. Understand when to use dropdowns vs buttons (dropdowns are best for many options where only one can be selected; buttons are best for 2-4 obvious choices).

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T05.G3.01: Put human‑centered design steps in order
* T05.G3.02: Identify user needs from a short interview transcript
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T10.G3.01.01: Create a list variable and add items to it
* T16.G4.02: Style widget appearance


ID: T16.G4.04
Topic: T16 – User Interfaces
Skill: Get the selected value from a dropdown
Description: Use "value of widget [NAME v]" block to retrieve which option the user selected from a dropdown menu. Use "when widget [NAME v] changes" event block to detect when the user selects a different option. The event triggers immediately when selection changes, allowing you to update other parts of the interface or take actions based on the new selection. Use the selected value in conditionals or to update other widgets.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G3.04: Trace code with a single if/else
* T16.G4.03: Add a dropdown menu widget


ID: T16.G4.05
Topic: T16 – User Interfaces
Skill: Add a slider widget for numeric input
Description: Use "add slider at X (X) Y (Y) width (WIDTH) between (MIN) and (MAX) as [NAME]" block to create a slider that users can drag to select a numeric value within a range. Set the position, width, minimum value, maximum value, and name. Sliders are useful for settings like volume, speed, or size.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T16.G4.02: Style widget appearance


ID: T16.G4.06
Topic: T16 – User Interfaces
Skill: Read and respond to slider value changes
Description: Use the "when widget value changed" event and "value of widget" block to detect when a user moves a slider and get its current value. Update other elements in real-time as the slider moves (e.g., adjust sprite size, change speed).

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.05: Trace code with variables to predict outcomes
* T16.G4.05: Add a slider widget for numeric input


ID: T16.G4.07
Topic: T16 – User Interfaces
Skill: Add checkbox and radio button widgets
Description: Use "add checkbox at X (X) Y (Y) named [NAME]" block to create toggle options that allow multiple selections. Use "add radio buttons [CHOICE1] [CHOICE2] [CHOICE3] [CHOICE4] [CHOICE5] [CHOICE6] [horizontal/vertical v] at x (X) y (Y) width (WIDTH) height (HEIGHT) named [NAME]" block to create mutually exclusive selections (only one can be selected at a time). Radio buttons support up to 6 choices with horizontal or vertical orientation. All radio buttons in a group share the same widget name. Use checkboxes for settings where multiple options can be on simultaneously (e.g., enable sound, enable music, enable vibration - all independent). Use radio buttons when only one choice is allowed (e.g., difficulty: Easy, Medium, Hard - only one can be selected). The mutual exclusivity of radio buttons is enforced automatically when they share the same group/widget name.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G3.04: Trace code with a single if/else
* T16.G4.02: Style widget appearance


ID: T16.G4.07.01
Topic: T16 – User Interfaces
Skill: Add and use tabs widget for organizing content
Description: Use "create tabs at X (X) Y (Y) width (WIDTH) height (HEIGHT) names [TAB1] [TAB2] ... [TAB8] show heading [Yes/No v]" block to create a tabbed interface with up to 8 panels. Use "set tab container [TABNAME v]" to specify which tab newly created widgets should appear in. Use "select tab [TABNAME]" to switch between tabs programmatically. Use "[show/hide/add/remove v] tab named [TABNAME]" to manage individual tabs. Use "when tab [TABNAME v] selected" event to respond to user tab changes. Tabs organize content into logical sections within a single screen.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T16.G3.07: Show and hide widgets
* T16.G4.07: Add checkbox and radio button widgets


ID: T16.G4.08
Topic: T16 – User Interfaces
Skill: Build a simple settings panel
Description: Organize multiple input widgets into a settings panel. Arrange checkboxes, sliders, dropdowns, and labels into a cohesive group. Position related settings near each other and use descriptive labels to explain each option. Create visual separation between setting groups using spacing or styling.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T16.G4.06: Read and respond to slider value changes
* T16.G4.07: Add checkbox and radio button widgets


ID: T16.G4.08.01
Topic: T16 – User Interfaces
Skill: Connect settings to program behavior
Description: Connect settings widget values to program behavior. Read values from multiple widget types (checkbox state, slider value, dropdown selection) and use them to control how the program runs. For example, use a volume slider value to control sound loudness, a difficulty dropdown to adjust game speed, or a sound on/off checkbox to enable/disable audio.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G4.01: Combine two conditions with AND
* T16.G4.08: Build a simple settings panel


ID: T16.G4.09
Topic: T16 – User Interfaces
Skill: Respond to hover events on widgets
Description: Use the "when pointer enters widget" and "when pointer leaves widget" event blocks to detect when the mouse hovers over a widget. Create hover effects like changing button colors, showing tooltips, or highlighting interactive elements when the user moves their mouse over them.

Dependencies:
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T16.G3.02: Handle a button click event
* T16.G4.02: Style widget appearance


ID: T16.G4.10
Topic: T16 – User Interfaces
Skill: Add hyperlink widgets to external resources
Description: Use "add link at X (X) Y (Y) url [URL] as [NAME]" block to create clickable hyperlinks that open external URLs in a new browser tab. The link displays the URL as text by default. Use "set value to [TEXT] for widget [NAME]" to change the displayed text to something more user-friendly (e.g., "Click here for help" instead of the full URL). Style links using "set text style" to change color and make them distinct from buttons. Use links for documentation, resources, or external content integration.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T16.G3.01: Add a button widget to the stage
* T16.G4.02: Style widget appearance


ID: T16.G5.01
Topic: T16 – User Interfaces
Skill: Create a multi‑screen app with a navigation interface
Description: Build a multi-screen application with navigation between different views (home screen, game screen, settings screen, results screen). Use buttons to navigate between screens by showing/hiding different groups of widgets, OR use the tabs widget to organize screens into separate tabs. Manage which widgets are visible on each screen using the "set widget visible" block or tab containers.

Dependencies:
* T16.G4.08: Build a simple settings panel
* T09.G3.05: Trace code with variables to predict outcomes
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code


ID: T16.G5.02
Topic: T16 – User Interfaces
Skill: Design a form with multiple inputs and validation
Description: Students create a form interface with multiple text input fields, dropdowns, or checkboxes, validate all inputs for completeness and correctness, and display a summary or confirmation message. This teaches form design and validation patterns.

Dependencies:
* T16.G4.07: Add checkbox and radio button widgets
* T08.G3.05: Fix a condition that uses the wrong operator
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G5.02.01
Topic: T16 – User Interfaces
Skill: Add specialized picker widgets for dates and colors
Description: Use the "add date picker widget" and "add color picker widget" blocks to create specialized input controls. Date pickers let users select dates from a calendar interface; color pickers let users choose colors visually. Retrieve selected values using the "value of widget" block.

Dependencies:
* T16.G5.02: Design a form with multiple inputs and validation
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G5.03
Topic: T16 – User Interfaces
Skill: Build a leaderboard or high‑score display
Description: Students create a label or series of labels that display high scores or player rankings. They use lists or variables to store scores and update the display dynamically. This introduces the concept of showing structured data in a UI.

Dependencies:
* T16.G4.01: Style widget text properties
* T10.G3.01: Loop through and process each item in a list
* T09.G3.05: Trace code with variables to predict outcomes
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code


ID: T16.G5.04
Topic: T16 – User Interfaces
Skill: Implement a responsive HUD that reacts to game state
Description: Students design a "heads-up display" (HUD)—on-screen UI elements that show real-time game information (health bar, ammo count, mini-map indicator, status text). The HUD updates dynamically as game variables change.

Dependencies:
* T16.G4.06: Read and respond to slider value changes
* T08.G3.05: Fix a condition that uses the wrong operator
* T09.G3.05: Trace code with variables to predict outcomes
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence


ID: T16.G5.04.01
Topic: T16 – User Interfaces
Skill: Add and update a progress bar widget
Description: Use the "add progress bar widget" block to create a visual indicator of progress or completion. Set the progress bar's minimum, maximum, and current values. Update the progress bar dynamically using "set widget value" to show loading progress, health levels, or task completion status.

Dependencies:
* T16.G5.04: Implement a responsive HUD that reacts to game state
* T16.G3.04: Update label text dynamically
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G5.04.02
Topic: T16 – User Interfaces
Skill: Animate widgets for visual feedback
Description: Animate widgets for visual feedback and smooth transitions. Use "move widget [NAME] to X Y in T seconds" to slide widgets in from the side. Use "set transparency for widget [NAME] to (T)% in (N) seconds [blocking v]" to create fade effects. Transparency creates fade effects (0% = fully visible, 100% = invisible but still present). This is different from "set visibility" which instantly shows or hides widgets. Use transparency for smooth fade-in/fade-out animations; use visibility for instant show/hide. Use "scale widget [NAME] to width (W)% height (H)% in (T) seconds" to grow or shrink widgets. Use "rotate widget [NAME] by (D) degrees in (T) seconds" to spin widgets for attention-grabbing effects. Combine with "when pointer enters widget" for hover effects. Animations improve user experience by making interfaces feel responsive and polished.

Dependencies:
* T16.G5.04.01: Add and update a progress bar widget
* T16.G4.09: Respond to hover events on widgets
* T07.G4.03: Use "repeat until" to control animation duration
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G5.05
Topic: T16 – User Interfaces
Skill: Embed and control a video widget
Description: Use "add youtube video [URL] at X (X) Y (Y) width (WIDTH) height (HEIGHT) named [NAME] in [foreground/background v]" block to embed a YouTube video. Set the video's URL, position, size, name, and layer. Use foreground layer for interactive videos users can click to play/pause. Use background layer for non-interactive videos that play automatically. Video widgets are useful for tutorials, cutscenes, educational content, or entertainment.

Dependencies:
* T16.G5.01: Create a multi‑screen app with a navigation interface
* T16.G4.09: Respond to hover events on widgets
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G5.05.01
Topic: T16 – User Interfaces
Skill: Control video playback with advanced features
Description: Control video playback with advanced features. Use "pause video", "seek to seconds", "set volume", and "set playback speed" blocks to precisely control video behavior. Use "current video time for [VIDEONAME v]" to get the current playback position in seconds. Use the "when video stopped" event to trigger actions when a video finishes (e.g., move to next screen, show quiz questions). Create interactive video experiences with checkpoints, progress tracking, branching choices, or programmatic control.

Dependencies:
* T16.G5.05: Embed and control a video widget
* T06.G4.03: Use broadcast and "when I receive" for communication
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G5.05.02
Topic: T16 – User Interfaces
Skill: Respond to video playback events
Description: Use video event blocks to create interactive video experiences. Use "when video [NAME] start" to trigger actions when playback begins. Use "when video [NAME] paused" to detect when user pauses the video. Use "when video time is (T) seconds for [NAME]" to trigger actions at specific timestamps (show quiz questions at 1:30, display commentary at 2:00). Combine these events with video control blocks to create interactive lessons, branching narratives, or video-based games.

Dependencies:
* T16.G5.05: Embed and control a video widget
* T06.G4.03: Use broadcast and "when I receive" for communication
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G5.06
Topic: T16 – User Interfaces
Skill: Add a rich textbox for formatted content
Description: Use "add rich textbox at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (PADDING) mode [input/read-only v] as [NAME]" block to create a text area that supports formatted text (bold, italic, font sizes, colors). In input mode, users can format text using toolbar buttons. In read-only mode, display pre-formatted content with styling. Retrieve formatted content using "value of widget" block (returns HTML markup like "&lt;b&gt;text&lt;/b&gt;"), which is useful for storing or transferring formatted content but requires HTML knowledge to parse or manipulate. Use input mode for note-taking apps or message composers; use read-only mode for styled instructions, stories, or formatted displays.

Dependencies:
* T16.G3.05: Add a textbox widget for user input
* T16.G4.01: Style widget text properties
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G5.06.01
Topic: T16 – User Interfaces
Skill: Create a chat window widget for messaging
Description: The chat window automatically creates a scrollable message history panel, a text input box, and a send button. Users can type messages in the input box and click send (or press Enter). Use "append to chat" to add messages programmatically. Customize message appearance with sender name, icon (robot icon, user icon, or custom costume), alignment (left for received messages, right for sent messages), text size, text color, and background color. Use "update last chat message" to modify the most recent message (useful for streaming AI responses or correcting errors). Chat windows combine multiple UI elements for interactive conversations.

Dependencies:
* T16.G5.06: Add a rich textbox for formatted content
* T16.G4.08: Build a simple settings panel
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G5.07
Topic: T16 – User Interfaces
Skill: Create a toolbox widget for item selection
Description: Use the "add toolbox widget" block to create a grid-based icon selector with specified rows and columns. Use "set icon to toolbox" with row number, column number, and costume name to populate cells with images. When a user clicks a cell, both "when widget [toolbox1 v] clicked" and "when widget [toolbox1 v] changes" events trigger. Use "value of widget [toolbox1 v]" to get the selected cell index (1 = first icon, 2 = second icon, etc.). Toolboxes are ideal for game inventories, building block selectors, tool palettes, or item shops.

Dependencies:
* T16.G4.02.01: Add an image widget to the stage
* T16.G4.06: Read and respond to slider value changes
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G5.08
Topic: T16 – User Interfaces
Skill: Create confirmation dialogs with custom buttons
Description: Use "confirm [TEXT] with buttons [BUTTON1] [BUTTON2] [BUTTON3] [BUTTON4] [BUTTON5] [BUTTON6]" block to create modal dialogs that pause program execution until the user clicks a button. Add up to 6 buttons (blank buttons are hidden). The block returns the text of the clicked button. Use confirmation dialogs for important decisions (Save or Cancel? Easy, Medium, or Hard? Yes or No?), error messages, or user choices.

Dependencies:
* T16.G3.02: Handle a button click event
* T08.G3.04: Trace code with a single if/else
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T16.G6.01
Topic: T16 – User Interfaces
Skill: Evaluate an interface for usability
Description: Students examine an existing interface (a simple app screenshot) and identify issues or strengths: Are buttons clearly labeled? Is the layout intuitive? Are colors accessible for colorblind users? They learn to think like a UX designer and consider diverse users.

Dependencies:
* T16.G5.03: Build a leaderboard or high‑score display


ID: T16.G6.02
Topic: T16 – User Interfaces
Skill: Design an interface based on user feedback
Description: Students design an initial interface (buttons, labels, layout), ask peers or a teacher to try it, gather feedback on usability, and then modify the design to address the feedback. This introduces the iterative design process.

Dependencies:
* T16.G6.01: Evaluate an interface for usability


ID: T16.G6.03
Topic: T16 – User Interfaces
Skill: Use color and contrast to improve readability
Description: Students apply color theory to interface design: choosing high-contrast text and backgrounds for readability, avoiding color combinations that are difficult for colorblind users, and using color to highlight important elements (e.g., a red button for "Stop").

Dependencies:
* T16.G5.03: Build a leaderboard or high‑score display
* T16.G4.02: Style widget appearance


ID: T16.G6.03.01
Topic: T16 – User Interfaces
Skill: Control widget layering with z-index
Description: Control widget layering and stacking order using z-index. Use the "set z-index" block to determine which widgets appear on top of others (higher z-index = appears in front). Create overlays, popup messages, or modal dialogs that appear over other interface elements. Understand the default z-index (10) and how to use values like 1 (background) to 100 (topmost) to organize interface layers.

Dependencies:
* T16.G6.03: Use color and contrast to improve readability
* T16.G3.07: Show and hide widgets


ID: T16.G6.03.02
Topic: T16 – User Interfaces
Skill: Manage widget states and focus for clear feedback
Description: Manage widget states to provide clear feedback. Use "disable widget" to grey out and prevent interaction. Use "enable widget" to restore interactivity. Use "release focus for widget [NAME]" to deselect/unfocus widgets (remove cursor from text fields, deselect buttons). Use "set widget visible" to show loading indicators or success messages. Change widget text colors to red for errors, green for success. Widget state management helps users understand what actions are available.

Dependencies:
* T16.G6.03: Use color and contrast to improve readability
* T08.G4.03: Trace nested conditions to predict outcomes


ID: T16.G6.04
Topic: T16 – User Interfaces
Skill: Create an interface that works on different screen sizes
Description: Create interfaces that adapt to different screen sizes using the "apply layout row" block. Define multiple rows with percentage heights summing to 100% (e.g., Row 1: 15% header, Row 2: 70% content, Row 3: 15% footer). Divide each row into cells with percentage widths (e.g., 20% 60% 20% for sidebar/content/sidebar). Widgets placed in cells automatically resize and reposition as screen size changes. The layout system eliminates manual coordinate calculations and makes your interface responsive on tablets, phones, and computers.

Dependencies:
* T16.G5.01: Create a multi‑screen app with a navigation interface
* T16.G4.01: Style widget text properties
* T16.G3.08: Position and resize widgets


ID: T16.G6.05
Topic: T16 – User Interfaces
Skill: Display camera feed in a widget
Description: Use "show [front/back v] camera in [normal/flipped v] x (X) y (Y) width (WIDTH) height (HEIGHT) as [NAME]" block to display a live camera feed. Choose front or back camera, normal or flipped (mirror) mode, and set position/size. Use "save picture from camera [CAMERANAME v] as costume [COSTUMENAME]" to capture a snapshot as a costume. Each snapshot creates a new costume in the sprite's costume list. Use "delete costume [COSTUMENAME]" to remove saved snapshots you no longer need to avoid filling up the costume list. Camera widgets enable photo-taking apps, video chat interfaces, or augmented reality features.

Dependencies:
* T16.G5.05: Embed and control a video widget
* T16.G4.02.01: Add an image widget to the stage


ID: T16.G6.06
Topic: T16 – User Interfaces
Skill: Create a menu bar with groups and items
Description: Use "add menu bar at X (X) Y (Y) width (WIDTH) height (HEIGHT) as [NAME]" block to create application-style menus. Use "add menu group" to add menu groups (File, Edit, View). Use "add menu item" to add items within each group. Organize related commands into logical groups.

Dependencies:
* T16.G5.01: Create a multi‑screen app with a navigation interface
* T16.G4.03: Add a dropdown menu widget


ID: T16.G6.06.01
Topic: T16 – User Interfaces
Skill: Handle menu item click events
Description: Use "when menu item [ITEMNAME] from group [GROUPNAME] clicked" event block to respond when users select menu items. Connect menu selections to actions (show/hide widgets, change settings, trigger functions). Compare menu bars to other navigation patterns (buttons, dropdowns, tabs).

Dependencies:
* T16.G6.06: Create a menu bar with groups and items


ID: T16.G6.06.02
Topic: T16 – User Interfaces
Skill: Navigate to other projects
Description: Use "run project [PROJECTID] in [new/this v] browser tab" block to launch another CreatiCode project. The target project auto-starts in full stage mode. Choose "new" to open in a new browser tab (keeps current project running) or "this" to replace the current project. Use "open URL [URL] in new browser tab" to open external websites. Project navigation enables creating multi-project experiences, portfolios with project menus, or educational sequences where completing one project leads to the next.

Dependencies:
* T16.G5.01: Create a multi‑screen app with a navigation interface


ID: T16.G7.01
Topic: T16 – User Interfaces
Skill: Build a data collection interface (survey or questionnaire)
Description: Students design an interface for a survey or questionnaire with text inputs, dropdowns, checkboxes, or radio buttons; validate responses; and collect the data. They learn how interfaces are used to gather information.

Dependencies:
* T16.G6.03: Use color and contrast to improve readability
* T16.G5.02: Design a form with multiple inputs and validation


ID: T16.G7.02
Topic: T16 – User Interfaces
Skill: Implement a search or filter interface
Description: Students create a text input field where users can type a query, and the interface filters or searches a list of items (e.g., a player inventory, a menu of options) to show only matching results. This is a real-world UI pattern.

Dependencies:
* T16.G6.04: Create an interface that works on different screen sizes
* T16.G5.02: Design a form with multiple inputs and validation


ID: T16.G7.03
Topic: T16 – User Interfaces
Skill: Design an accessible interface for users with different abilities
Description: Students consider accessibility needs (e.g., text size for low vision, keyboard controls for mobility challenges, colorblind-friendly palettes) and redesign an interface to accommodate multiple ability types. They learn to design inclusively from the start.

Dependencies:
* T16.G6.03: Use color and contrast to improve readability
* T16.G6.04: Create an interface that works on different screen sizes


ID: T16.G7.04
Topic: T16 – User Interfaces
Skill: Create a help or tutorial interface
Description: Students design a help or tutorial interface within a game, including explanatory labels, step-by-step instructions, images/animations, and a "Next" button to guide the player through mechanics or controls.

Dependencies:
* T16.G6.04: Create an interface that works on different screen sizes
* T16.G5.01: Create a multi‑screen app with a navigation interface


ID: T16.G7.05
Topic: T16 – User Interfaces
Skill: Display data as charts in a widget
Description: Use "draw [bar/line/pie/percentage v] chart using list [LISTNAME v] x (X) y (Y) width (WIDTH) height (HEIGHT)" or "draw chart using columns [COLUMNLIST] from table [TABLENAME v]..." blocks to create data visualizations. Use bar charts for comparisons, line charts for trends over time, pie charts for proportions, and percentage charts for part-to-whole relationships. Charts can use either list data (single series) or table data (multiple series). Charts transform raw numbers into visual representations that help users understand patterns and comparisons.

Dependencies:
* T16.G5.03: Build a leaderboard or high‑score display
* T10.G5.01: Search and sort a list


ID: T16.G8.01
Topic: T16 – User Interfaces
Skill: Design a wizard or step-by-step interface
Description: Students build a "wizard" interface that guides users through a multi-step process (e.g., character creation, game setup, checkout) with Previous/Next buttons, progress indicators, and validation at each step. They manage state across multiple screens.

Dependencies:
* T16.G7.04: Create a help or tutorial interface
* T16.G7.03: Design an accessible interface for users with different abilities
* T09.G6.01: Model real-world quantities using variables and formulas
* T07.G6.01: Trace nested loops with variable bounds
* T17.G6.01: Configure surface friction parameters
* T26.G6.01: Map stakeholder questions to data requirements


ID: T16.G8.02
Topic: T16 – User Interfaces
Skill: Implement dynamic content loading in a UI
Description: Students design an interface where selecting an option dynamically loads and displays related content (e.g., clicking a character name displays their stats, clicking a level number shows the level preview). Content is retrieved from lists or variables.

Dependencies:
* T16.G7.02: Implement a search or filter interface
* T16.G7.01: Build a data collection interface (survey or questionnaire)
* T09.G6.01: Model real-world quantities using variables and formulas
* T03.G6.01: Propose modules for a medium project
* T04.G6.01: Group snippets by underlying algorithm pattern
* T07.G6.01: Trace nested loops with variable bounds


ID: T16.G8.03
Topic: T16 – User Interfaces
Skill: Analyze UI design patterns and their effectiveness
Description: Students examine two different interface designs for the same task (e.g., two layouts for a settings menu, two ways to input a number) and evaluate which is more effective based on clarity, ease of use, and aesthetics. They write a brief analysis.

Dependencies:
* T16.G7.03: Design an accessible interface for users with different abilities
* T16.G6.02: Design an interface based on user feedback
* T03.G6.01: Propose modules for a medium project
* T07.G6.01: Trace nested loops with variable bounds
* T10.G6.01: Sort a table by a column



ID: T16.G8.04
Topic: T16 – User Interfaces
Skill: Document and refine a UI design based on usability testing
Description: Students conduct user testing of their interface (having peers try to complete a task using their interface, noting where they struggle), document observations, and refactor the interface to resolve usability issues. This reinforces the human-centered design cycle.

Dependencies:
* T16.G8.03: Analyze UI design patterns and their effectiveness
* T16.G6.02: Design an interface based on user feedback
* T18.G6.01.01: Apply forces and impulses to physics bodies
* T26.G6.01: Map stakeholder questions to data requirements
* T32.G6.01: Identify common malware types



---

## PART 2: ALL CREATICODE WIDGET BLOCKS (COMPLETE LIST)

Block ID: widget_addtextbox
Category: Widgets
Can be used for 3D: false
Syntax: add textbox at X (X) Y (Y) width (W) height (H) padding (P) line [LINETYPE v] scroll [SCROLLTYPE v] mode [MODETYPE v] as [textbox1]
Usage Example: add textbox at X (0) Y (0) width (200) height (30) padding (6) line [single v] scroll [scroll v] mode [input v] as [t1]
QuickDescription: 


Description: 
adds a textbox widget with width of W and height of H, centered at the position of (X, Y). The text inside the textbox will have a padding of P around the 4 borders. The LINETYPE can be 'single' or 'multiple', which controls whether the textbox only contain one line or multiple lines. The SCROLLTYPE can be 'scroll' or 'no scroll', which controls whether a scrollbar is shown. The MODETYPE can be 'read only' or 'input'. The last input is a name for the textbox and it can not be empty.




Block ID: widget_addrichtextbox
Category: Widgets
Can be used for 3D: false
Syntax: add rich textbox at X (X) Y (Y) width (W) height (H) padding (P) mode [MODE v] as [NAME]
Usage Example: add rich textbox at X (0) Y (0) width (480) height (360) padding (6) mode [read-only v] as [richtext1]
QuickDescription: 


Description: 
adds a rich text editor widget with width of W and height of H, centered at the position of (X, Y). This textbox can display or edit text with full formatting instead of plain text. The text inside the textbox will have a padding of P around the 4 borders. The MODETYPE can be 'read only' or 'input'. The last input is a name for the textbox and it can not be empty.




Block ID: widget_showcamera
Category: Widgets
Can be used for 3D: false
Syntax: show [SIDE v] camera in [MODE v] x (X) y (Y) width (W) height (H) as [NAME]
Usage Example: show [front v] camera in [normal v] x (0) y (0) width (480) height (360) as [camera1]
QuickDescription: 


Description: 
adds a camera window widget with width of W and height of H, centered at the position of (X, Y). It will be showing images from the 'front' or 'back' camera as specified by SIDE, and MODE can be 'normal' or 'flipped'. The last input is a name for the textbox and it can not be empty.




Block ID: widget_savepicturefromcamera
Category: Widgets
Can be used for 3D: false
Syntax: save picture from camera [CAMERAWIDGETNAME v] as costume [COSTUMENAME]
Usage Example: save picture from camera [camera1 v] as costume [picture1]
QuickDescription: 


Description: 
takes a snapshot of the camera view from the camera widget named CAMERAWIDGETNAME, and save it as a costume of this sprite with the name of COSTUMENAME.




Block ID: widget_valuefromwidget
Category: Widgets
Can be used for 3D: false
Syntax: value of widget [WIDGETNAME v]
Usage Example: value of widget [button1 v]
QuickDescription: 
a reporter block that returns the current value of the widget with the given name of WIDGETNAME.

Description: 
a reporter block that returns the current value of the widget with the given name of WIDGETNAME. Note that this block can work with a wide range of widget types. If the specified widget is a textbox, this block will return the text content of that textbox; if the widget is a button or label, this block will return the text shown on the widget; for date picker widget, this block returns the date string in YYYYMMDD format like '20210620'; for color picker widget, this block returns a color value in "#RRGGBBAA" format, like "#FF0088FF"; for slider widgets this block returns the current value of the slider; for dropdown menu widget this block returns the selected option.




Block ID: widget_settext
Category: Widgets
Can be used for 3D: false
Syntax: set value to [V] for widget [WIDGETNAME v]
Usage Example: set value to [hi] for widget [t1 v]
QuickDescription: 


Description: 
sets the value of the widget named WIDGETNAME to V. You can use this block to change the value of many widgets. For buttons and labels, this block changes the text displayed on them. For textbox, this block changes the text content of the textbox. For date picker, we can use this block to set the selected date using the YYYYMMDD format; For color picker, we can use this block sets the selected color in the format of #RRGGBBAA; for slider widgets, we can use this block to set the selected value with its range; for dropdown menu we can use this block to select an option from the dropdown.




Block ID: widget_addlabel
Category: Widgets
Can be used for 3D: false
Syntax: add label [TEXT] at X (X) Y (Y) width (WIDTH) height (HEIGHT) padding (P) as [NAME]
Usage Example: add label [Hi] at X (0) Y (0) width (100) height (30) padding (6) as [label1]
QuickDescription: 


Description: 
adds a label widget with the given WIDTH and HEIGHT, centered at the position of (X, Y). The text in the label has a padding of P around the 4 edges. The label will be given the NAME and it can not be blank. You can set the text shown on the label using the 'set value to [V] for widget [WIDGETNAME v]' block. You can read out the current text on the label using the 'value of widget [WIDGETNAME v]' block.




Block ID: widget_addbutton
Category: Widgets
Can be used for 3D: false
Syntax: add button [TEXT] at X (X) Y (Y) width (WIDTH) height (HEIGHT) tooltip [TOOLTIP] as [NAME]
Usage Example: add button [Run] at X (0) Y (0) width (100) height (30) tooltip [Hi] as [button1]
QuickDescription: 
adds a button widget

Description: 
adds a button with the given WIDTH and HEIGHT, centered at the position of (X, Y). The text shown on the button has a padding of P around the 4 edges. The button will be given the NAME and it can not be blank. To handle button click event, you can use the 'when widget [NAME v] clicked' block. You can set the text shown on the button using the 'set value to [V] for widget [WIDGETNAME v]' block. You can read out the current text on the button using the 'value of widget [WIDGETNAME v]' block.




Block ID: widget_whenwidgetclicked
Category: Widgets
Can be used for 3D: false
Syntax: when widget [NAME v] clicked
Usage Example: when widget (button1 v) clicked
QuickDescription: 


Description: 
A hat-block that is triggered whenever the widget with the given NAME is clicked. This block can be used to handle user click events for widget like button, image, radio button.




Block ID: widget_settextstyle
Category: Widgets
Can be used for 3D: false
Syntax: set text style [FONTSTYLE v] font size (FONTSIZE) text color [TEXTCOLOR] boldness [BOLDNESS v] text alignment [TEXTALIGNMENT v] for widget [WIDGETNAME v]
Usage Example: set text style [sans-serif v] font size (18) text color [#FFFFFFFF] boldness [normal v] text alignment [Middle v] for widget [button1 v]
QuickDescription: 
sets the text style for the widget named WIDGETNAME

Description: 
sets the text style for the widget named WIDGETNAME. we can set the FONTSTYLE to these values: 'Helvetica Neue', Helvetica, Arial, sans-serif', 'Arbutus', 'Bungee Shade', 'Butcherman', 'Bangers', 'Caesar Dressing', 'Creepster', 'Lilita One', 'Luckiest Guy', 'Jua', 'Nosifer', 'Potta One'). The font size is set to FONTSIZE, which is a whole number. We can also set TEXTCOLOR for the color of the text, and set BOLDNESS to control if the text is 'bold' or 'normal'. We can set alignment of the text to TEXTALIGNMENT, which can be Left/Middle/Right. This block works on all widget types that display some text, such as button, label, text box, dropdown menu, etc.




Block ID: widget_setwidgetstyle
Category: Widgets
Can be used for 3D: false
Syntax: set widget background color [BACKGROUNDCOLOR] border color [BORDERCOLOR] border width (BORDERWIDTH) border radius (BORDERRADIUS) for [WIDGETNAME v]
Usage Example: set widget background color [#7531BBBD] border color [#E6E6E6FF] border width (1) border radius (4) for [button1 v]
QuickDescription: 


Description: 
this block updates the style of the widget named WIDGETNAME.  Including the BACKGROUNDCOLOR, BORDERCOLOR, BORDERWIDTH, and BORDERRADIUS. The color parameters accept the #RRGGBBAA format, so you can set some transparency to the widget using this block as well. This block works on almost all widget types, such as button, label, text box, dropdown menu, etc.




Block ID: widget_adddatepicker
Category: Widgets
Can be used for 3D: false
Syntax: add date picker at X (X) Y (Y) as [NAME]
Usage Example: add date picker at X (0) Y (0) as [datepicker1]
QuickDescription: 


Description: 
adds a date picker widget centered at the specified position of (X, Y), and name this date picker as NAME. you can set its date value using the 'set value to [V] for widget [WIDGETNAME v]' block, such as 'set value to [20200512] for widget [datepicker1 v]'. You can read out the date selected by the user using the 'value of widget [WIDGETNAME v]' block, which will return a value like 20200512. The date picker's default size is 200 wide by 30 tall




Block ID: widget_addcolorpicker
Category: Widgets
Can be used for 3D: false
Syntax: add color picker at X (X) Y (Y) as [NAME]
Usage Example: add color picker at X (0) Y (0) as [colorpicker1]
QuickDescription: 


Description: 
adds a color picker widget centered at the specified position of (X, Y), and name this color picker as NAME. you can set its color value using the 'set value to [V] for widget [WIDGETNAME v]' block, such as 'set value to [#FF00FFFF] for widget [colorpicker1 v]'. You can read out the color selected by the user using the 'value of widget [WIDGETNAME v]' block, which will return a value like #FFFF00FF




Block ID: widget_addslider
Category: Widgets
Can be used for 3D: false
Syntax: add slider at X (X) Y (Y) width (WIDTH) between (MIN) and (MAX) as [NAME]
Usage Example: add slider at X (0) Y (0) width (200) between (0) and (100) as [slider1]
QuickDescription: 


Description: 
adds a slider widget centered at the the specified position of (X, Y) with the given WIDTH. Name this slider as NAME. Its value range is between MIN and MAX. you can set its value using the 'set value to [V] for widget [WIDGETNAME v]' block, such as 'set value to [20] for widget [slider1 v]'. You can read out the value using the 'value of widget [WIDGETNAME v]' block




Block ID: widget_addmenu
Category: Widgets
Can be used for 3D: false
Syntax: add dropdown menu at X (X) Y (Y) width (WIDTH) height (HEIGHT) using list [LIST v] as [NAME]
Usage Example: add dropdown menu at X (0) Y (0) width (200) height (30) using list [names v] as [menu1]
QuickDescription: 


Description: 
adds a dropdown menu centered at the the specified position of (X, Y) with the given WIDTH and HEIGHT. The choices of the dropdown will be defined by the items in the list LISTNAME. Name this slider as NAME. You can set its selected value using the 'set value to [V] for widget [WIDGETNAME v]' block, such as 'set value to [start] for widget [menu1 v]'. You can read out the selected choice using the 'value of widget [WIDGETNAME v]' block




Block ID: widget_whenwidgetchanges
Category: Widgets
Can be used for 3D: false
Syntax: when widget [NAME v] changes
Usage Example: when widget [textbox1 v] changes
QuickDescription: 


Description: 
A hat-block that is triggered when the widget with the given NAME changes its state or value. This block can be used to handle user actions that change the value of a widget, such as text box, dropdown menu, slider, color picker, date picker, etc.




Block ID: widget_resizewidgettowidthheight
Category: Widgets
Can be used for 3D: false
Syntax: resize widget [WIDGETNAME v] to width (WIDTH) height (HEIGHT) in (T) seconds [BLOCKINGMODE v]
Usage Example: resize widget [button1 v] to width (100) height (100) in (0) seconds [blocking v]
QuickDescription: 


Description: 
resizes the widget named WIDGETNAME to the given WIDTH and HEIGHT over T seconds. If BLOCKINGMODE is 'blocking', then this block will wait until the resizing is completed before running the next block. If 'non-blocking', the next block will start to run right away even if the resizing animation is not completed.




Block ID: widget_appendtext
Category: Widgets
Can be used for 3D: false
Syntax: append text [NEWTEXT] to [WIDGETNAME v] in new line [ISNEWLINE v]
Usage Example: append text [22] to [button1 v] in new line [No v]
QuickDescription: 


Description: 
appends the text of NEWTEXT to the specified widget named WIDGETNAME, such as a textbox or a button. If NEWLINE is 'Yes', then the NEWTEXT will appear in a new line, otherwise it will be appended to the last existing line.




Block ID: widget_removewidget
Category: Widgets
Can be used for 3D: false
Syntax: remove widget named [WIDGETNAME v]
Usage Example: remove widget named [button1 v]
QuickDescription: 


Description: 
removes the widget named WIDGETNAME from the project.




Block ID: widget_removeallwidgets
Category: Widgets
Can be used for 3D: false
Syntax: remove all widgets
Usage Example: remove all widgets
QuickDescription: 


Description: 
removes all widgets from the project.




Block ID: widget_setvisibility
Category: Widgets
Can be used for 3D: false
Syntax: set visibility [VISIBILITY v] for widget named [WIDGETNAME v]
Usage Example: set visibility [show v] for widget named [button1 v]
QuickDescription: 


Description: 
sets the visibility to VISIBILITY (show or hide) for the widget named WIDGETNAME




Block ID: widget_setvisibilityforall
Category: Widgets
Can be used for 3D: false
Syntax: set visibility [VISIBILITY v] for all widgets
Usage Example: set visibility [show v] for all widgets
QuickDescription: 


Description: 
sets the visibility to VISIBILITY (show or hide) for all widgets in the project.




Block ID: widget_setzindex
Category: Widgets
Can be used for 3D: false
Syntax: set z-index to [ZINDEX] for widget named [WIDGETNAME v]
Usage Example: set z-index to [20] for widget named [button1 v]
QuickDescription: 


Description: 
sets the z-index of the given widget. all widgets have default z-index of 10.




Block ID: widget_whenmouseenter
Category: Widgets
Can be used for 3D: false
Syntax: when pointer enters widget named [WIDGETNAME v]
Usage Example: when pointer enters widget named [button1 v]
QuickDescription: 


Description: 
A hat-block that is triggered when the pointer enters the area over the widget named WIDGETNAME.




Block ID: widget_whenmouseleave
Category: Widgets
Can be used for 3D: false
Syntax: when pointer leaves widget named [WIDGETNAME v]
Usage Example: when pointer leaves widget named [button1 v]
QuickDescription: 


Description: 
A hat-block that is triggered when the pointer leaves the area over the widget named WIDGETNAME




Block ID: widget_addvideo
Category: Widgets
Can be used for 3D: false
Syntax: add youtube video [URL] at X (X) Y (Y) width (WIDTH) height (HEIGHT) named [NAME] in [LAYER v]
Usage Example: add youtube video [https://www.youtube.com/watch?v=_-Dm2LTXC88] at X (0) Y (0) width (480) height (360) named [video1] in (foreground v)
QuickDescription: 


Description: 
adds a YouTube video player widget with the specified URL to the stage, centered at the (X, Y) position, as a rectangle of WIDTH and HEIGHT. Give the widget a name of NAME. Based on the LAYER parameter, the video can be added in the 'foreground' or 'background'. If it is in the background, users will not be able to interact with it, so it will serve as a background for the project, but it can still be controlled programatically by other blocks to play or stop the video. LAYER is 'foreground', then users can click the controls on this widget.




Block ID: widget_actionvideo
Category: Widgets
Can be used for 3D: false
Syntax: [COMMAND v] video for [VIDEONAME v]
Usage Example: [start v] video for [video1 v]
QuickDescription: 


Description: 
Run a COMMAND on the video widget named VIDEONAME: start, pause, stop, mute or unmute.




Block ID: widget_seektosecondsvideo
Category: Widgets
Can be used for 3D: false
Syntax: seek to (TIME) seconds in video named [VIDEONAME v]
Usage Example: seek to (100) seconds in video named [video1 v]
QuickDescription: 


Description: 
seeks to the time of TIME (in seconds) in the video widget named VIDEONAME.




Block ID: widget_currentvideotime
Category: Widgets
Can be used for 3D: false
Syntax: current video time for [VIDEONAME v]
Usage Example: current video time for [video1 v]
QuickDescription: 


Description: 
A reporter block for the current playing time in seconds of the youtube video named VIDEONAME.




Block ID: widget_setyoutubevolume
Category: Widgets
Can be used for 3D: false
Syntax: set volume to (VOLUME) for [VIDEONAME v]
Usage Example: set volume to (50) for [video1 v]
QuickDescription: 


Description: 
sets the sound volume to VOLUME for the youtube video named VIDEONAME. VOLUME should be a number between 0 and 100.




Block ID: widget_setyoutubeplaybackspeedratio
Category: Widgets
Can be used for 3D: false
Syntax: set playback speed ratio (SPEED) for [VIDEONAME v]
Usage Example: set playback speed ratio (125) for [video1 v]
QuickDescription: 


Description: 
sets the playback speed ratio as SPEED for the youtube video named VIDEONAME. For example, if SPEED is 100, then the video is playing at normal speed. If SPEED is 200, then the speed will be doubled.




Block ID: widget_whenvideotimeis
Category: Widgets
Can be used for 3D: false
Syntax: when video time is (T) seconds for [VIDEONAME v]
Usage Example: when video time is (10) seconds for [video1 v]
QuickDescription: 


Description: 
A hat-block that is triggered when the video widget named VIDEONAME reaches the time point of T seconds into the video.




Block ID: widget_whenvideoispaused
Category: Widgets
Can be used for 3D: false
Syntax: when video [VIDEONAME v] paused
Usage Example: when video [video1 v] paused
QuickDescription: 


Description: 
A hat-block that is triggered when the video widget named VIDEONAME is paused.




Block ID: widget_whenvideoisstopped
Category: Widgets
Can be used for 3D: false
Syntax: when video [VIDEONAME v] stopped
Usage Example: when video [video1 v] stopped
QuickDescription: 


Description: 
A hat-block that is triggered when the video widget named VIDEONAME is stopped.




Block ID: widget_whenvideostart
Category: Widgets
Can be used for 3D: false
Syntax: when video [VIDEONAME v] start
Usage Example: when video [video1 v] start
QuickDescription: 


Description: 
A hat-block that is triggered when the video widget named VIDEONAME starts playing.




Block ID: widget_addtoolbox
Category: Widgets
Can be used for 3D: false
Syntax: add toolbox at x (X) y (Y) width (WIDTH) height (HEIGHT) row count (ROWCOUNT) column count (COLCOUNT) as [NAME]
Usage Example: add toolbox at x (0) y (0) width (250) height (50) row count (1) column count (5) as [tb]
QuickDescription: 
adds a toolbox widget, which is a grid of icons. It looks similar to the toolbox in MineCraft.

Description: 
adds a toolbox widget, which is a grid of icons. It looks similar to the toolbox in MineCraft. It will be centered at the position of (X, Y), with the given WIDTH and HEIGHT. This rectangle region is divided into ROWCOUNT rows and COLUMNCOUNT columns. For example, if ROWCOUNT is 2 and COLUMNCOUNT is 3, then there will be 6 icons in this toolbox. This toolbox will be given a name of NAME. After the toolbox is added to the stage, you can use the 'set icon to [COSTUMENAME v] at row (ROW) column (COL) for toolbox [TOOLBOXNAME]' block to specify the icons shown at specific positions in the toolbox. You can set which icon is selected among all the icons in the toolbox using the 'set value to [V] for widget [WIDGETNAME v]' block. The first icon in the first row has an index of 1, and the second icon in the first row has an index 2, etc. Suppose each row has 3 icons, then the first icon in the second row has an index of 4. By default the first icon of index 1 is selected. You can read out the index of the currently selected icon in the toolbox using the 'value of widget [WIDGETNAME v]' block. Whenever the user clicks on any cell of the toolbox to select it, it will trigger the hat block 'when widget [WIDGETNAME v] clicked'.




Block ID: widget_seticontotoolbox
Category: Widgets
Can be used for 3D: false
Syntax: set icon to [COSTUMENAME v] at row (ROW) column (COLUMN) for toolbox [TOOLBOXNAME v]
Usage Example: set icon to [costume1 v] at row (1) column (1) for toolbox [tb v]
QuickDescription: 


Description: 
set the icon at the given ROW and COLUMN of the toolbox named TOOLBOXNAME to the costume image named COSTUMENAME. For example, to set the first icon in the first row, set both ROW and COLUMN to 1.




Block ID: widget_addimagefromcostumes
Category: Widgets
Can be used for 3D: false
Syntax: add image [COSTUMENAME v] at x (X) y (Y) width (WIDTH) height (HEIGHT) aspect ratio [OPTION v] as [NAME]
Usage Example: add image [costume1 v] at x (0) y (0) width (480) height (360) aspect ratio [keep v] as [image1]
QuickDescription: 


Description: 
adds the costume named COSTUMENAME as an image widget to the stage, centered at the (X, Y) position, as a rectangle in WIDTH and HEIGHT. For aspect ratio, if OPTION is 'keep', the original aspect ratio will be kept for the image, and there may be some border area outside the image; or OPTION can be 'stretch', which will scale the image to fully occupy the rectangle area. Specify a NAME for the image widget using the last input.




Block ID: widget_addimagefromurl
Category: Widgets
Can be used for 3D: false
Syntax: add image from URL [URL] at x (X) y (Y) width (WIDTH) height (HEIGHT) aspect ratio [OPTION v] as [NAME]
Usage Example: add image from URL [https://play.creaticode.com/tcode-static-files/images/newlogo200.png] at x (0) y (0) width (480) height (360) aspect ratio [keep v] as []
QuickDescription: 


Description: 
adds the image shared at URL as an image widget to the stage, centered at the (X, Y) position, as a rectangle in WIDTH and HEIGHT. For aspect ratio, if OPTION is 'keep', the original aspect ratio will be kept for the image, and there may be some border area outside the image; or OPTION can be 'stretch', which will scale the image to fully occupy the rectangle area. Specify a NAME for the image widget using the last input.




Block ID: widget_addimage
Category: Widgets
Can be used for 3D: false
Syntax: add image [COSTUMENAME v] to widget named [WIDGETNAME v] at position X (X) Y (Y)
Usage Example: add image [costume1 v] to widget named [button1 v] at position X (0) Y (0)
QuickDescription: 


Description: 
adds the costume image named COSTUMENAME to the widget named WIDGETNAME at the position of (X, Y). This block is useful if you want to add a small image icon on another widget, such as a button or a label. If you just need to add an image to the stage, it is simpler to use the 'add image [COSTUMENAME v] at x (X) y (Y) width (WIDTH) height (HEIGHT) aspect ratio [OPTION v] as [NAME]' block.




Block ID: widget_addimageurl
Category: Widgets
Can be used for 3D: false
Syntax: add image at URL [URL] to widget named [WIDGETNAME v] at position X (X) Y (Y)
Usage Example: add image at URL [https://play.creaticode.com/tcode-static-files/images/newlogo200.png] to widget named [button1 v] at position X (0) Y (0)
QuickDescription: 


Description: 
adds the image at the given URL to the widget named WIDGETNAME at the position of (X, Y). This block is useful if you want to add a small image icon on another widget, such as a button or a label. If you just need to add an image to the stage, it is simpler to use the 'add image from URL [URL] at x (X) y (Y) width (WIDTH) height (HEIGHT) aspect ratio [OPTION v] as [NAME]' block directly.




Block ID: widget_movewidgettoxy
Category: Widgets
Can be used for 3D: false
Syntax: move widget [WIDGETNAME v] to X (X) Y (Y) in (T) seconds [BLOCKINGMODE v]
Usage Example: move widget [button1 v] to X (0) Y (0) in (0) seconds [blocking v]
QuickDescription: 


Description: 
moves the widget named WIDGETNAME to the given X and Y coordinates over T seconds. If BLOCKINGMODE is 'blocking', then this block will wait until the movement is completed before running the next block. If 'non-blocking', the next block will start to run right away even if the movement animation is not completed.




Block ID: widget_scalewidgettowidthheight
Category: Widgets
Can be used for 3D: false
Syntax: scale widget [WIDGETNAME v] to width (WIDTH)% height (HEIGHT)% in (T) seconds [BLOCKINGMODE v]
Usage Example: scale widget [button1 v] to width (100)% height (100)% in (0) seconds [blocking v]
QuickDescription: 


Description: 
scales the widget named WIDGETNAME to the given WIDTH and HEIGHT percentages over T seconds. If BLOCKINGMODE is 'blocking', then this block will wait until the scaling is completed before running the next block. If 'non-blocking', the next block will start to run right away even if the scaling animation is not completed.




Block ID: widget_rotatewidgetbydegrees
Category: Widgets
Can be used for 3D: false
Syntax: rotate widget [WIDGETNAME v] by (D) degrees in (T) seconds [BLOCKINGMODE v]
Usage Example: rotate widget [button1 v] by (15) degrees in (0) seconds [blocking v]
QuickDescription: 


Description: 
rotates the widget named WIDGETNAME by D degrees clockwise over T seconds. If BLOCKINGMODE is 'blocking', then this block will wait until the rotation is completed before the next block starts. If 'non-blocking', the next block will start to run right away even if the rotation animation is not completed.




Block ID: widget_transparencytowidget
Category: Widgets
Can be used for 3D: false
Syntax: set transparency for widget [WIDGETNAME v] to (T) % in (N) seconds [BLOCKINGMODE v]
Usage Example: set transparency for widget [button1 v] to (0) % in (0) seconds [blocking v]
QuickDescription: 


Description: 
sets the transparency of the widget named WIDGETNAME to T percent over N seconds. If BLOCKINGMODE is 'blocking', then this block will wait until the transparency is completed before running the next block. If 'non-blocking', the next block will start to run right away even if the transparency animation is not completed.




Block ID: widget_addlink
Category: Widgets
Can be used for 3D: false
Syntax: add link at X (X) Y (Y) url [URL] as [NAME]
Usage Example: add link at X (0) Y (0) url [google.com] as [link1]
QuickDescription: 


Description: 
adds a hyperlink widget centered at the (X, Y) position that links to the given URL. Assign the widget a name of NAME.




Block ID: widget_addmenubar
Category: Widgets
Can be used for 3D: false
Syntax: add menu bar at X (X) Y (Y) width (WIDTH) height (HEIGHT) as [NAME]
Usage Example: add menu bar at X (0) Y (0) width (250) height (50) as [menubar1]
QuickDescription: 


Description: 
adds a menu bar widget centered at the (X,Y) position as a rectangle shape of WIDTH and HEIGHT. Name the menu bar as NAME. The menu bar will be empty, and you need to use these blocks to add menu groups and menu items: 'add menu bar at X (X) Y (Y) width (WIDTH) height (HEIGHT) as [NAME]' and 'add menu group [GROUPNAME] to menu bar named [MENUBARNAME v]'




Block ID: widget_addmenugroup
Category: Widgets
Can be used for 3D: false
Syntax: add menu group [GROUPNAME] to menu bar named [MENUBARNAME v]
Usage Example: add menu group [file] to menu bar named [menubar1 v]
QuickDescription: 


Description: 
adds a menu group named GROUPNAME to the menu bar named MENUBARNAME.




Block ID: widget_addmenuitem
Category: Widgets
Can be used for 3D: false
Syntax: add menu item [ITEMNAME] to menu group named [GROUPNAME v]
Usage Example: add menu item [load your data] to menu group named [file v]
QuickDescription: 


Description: 
adds a menu item named ITEMNAME to the menu group named GROUPNAME.




Block ID: widget_confirmtextwithbuttons
Category: Widgets
Can be used for 3D: false
Syntax: confirm [TEXT] with buttons [BUTTON1] [BUTTON2] [BUTTON3] [BUTTON4] [BUTTON5] [BUTTON6]
Usage Example: confirm [What's your choice?] with buttons [A] [B] [C] [] [] []
QuickDescription: 


Description: 
a reporter block that displays a modal confirmation dialog at the top middle of the browser page (not the stage window) with the specified TEXT and up to 6 buttons. The text on the buttons will be BUTTON1 to BUTTON6. If any input is blank, then that button will not be displayed. After the user clicks on one of the buttons, this block will return a value that is the text on that button the user has clicked. After the dialog box is shown, the program execution will pause before the user makes a selection.
Example Program:

when green flag clicked
    set [choice v] to (confirm [TEXT] with buttons [K-5] [6-8] [9-12] [ ] [BUTTON5] [ ])
    say (join [Thanks for confirming that you are a] (choice) [student.] [] [] [] with [ ])
end




Block ID: widget_whenanybuttonnamedclicked
Category: Widgets
Can be used for 3D: false
Syntax: when any button named [BUTTONNAME v] clicked
Usage Example: when any button named [bt v] clicked
QuickDescription: 


Description: 
A hat-block that is triggered when any of the buttons shown on the stage is clicked. The name of that clicked button is stored in the variable named BUTTONNAME. This block is useful when there are many buttons on the stage, such as buttons for the 26 English letters or numbers from 1 to 10, and we want to handle the button click event using the same script.




Block ID: widget_releasefocus
Category: Widgets
Can be used for 3D: false
Syntax: release focus for widget [WIDGETNAME v]
Usage Example: release focus for widget [button1 v]
QuickDescription: 


Description: 
releases the focus from the widget named WIDGETNAME, effectively deselecting it.




Block ID: widget_addradiobutton
Category: Widgets
Can be used for 3D: false
Syntax: add radio buttons [CHOICE1] [CHOICE2] [CHOICE3] [CHOICE4] [CHOICE5] [CHOICE6] [ORIENTATION v] at x (0) y (0) width (200) height (30) named [NAME]
Usage Example: add radio buttons [A] [B] [C] [D] [ ] [ ] [horizontal v] at x (X) y (Y) width (WIDTH) height (HEIGHT) named [rb1]
QuickDescription: 


Description: 
adds a group of radio buttons, centered at (X, Y), within a rectangle region of WIDTH and HEIGHT. There can be at most 6 buttons. Their text will be CHOICE1 to CHOICE6, and if any of these 6 inputs are empty, that button will not be displayed. The  ORIENTATION can be 'vertial' or 'horizontal', which controls how the radio buttons are laid out. The radio button group is named as NAME.




Block ID: widget_addcheckbox
Category: Widgets
Can be used for 3D: false
Syntax: add checkbox at X (X) Y (Y) named [NAME]
Usage Example: add checkbox at X (0) Y (0) named [checkbox1]
QuickDescription: 


Description: 
adds a checkbox at the position of (X, Y) and name it as NAME. The value of the checkbox widget will be 0 if it is unchecked and 1 if it is checked. you can set its value using the 'set value to [V] for widget [WIDGETNAME v]' block. You can read out the value using the 'value of widget [WIDGETNAME v]' block.




Block ID: widget_runproject
Category: Widgets
Can be used for 3D: false
Syntax: run project [PROJECTID] in [BROWSERTAB v] browser tab
Usage Example: run project [23423sdffd] in [new v] browser tab
QuickDescription: 


Description: 
runs the CreatiCode project with the given PROJECTID. If BROWSERTAB is 'new', then that project will be opened in a new browser tab. If it is 'this', then that project will replace the current project in this browser tab. The project will automatically start to run in full stage mode after it is loaded (so the user doesn't need to click the green flag). This block is especially useful when you have multiple related projects. For example, when a player completes level 1 of a game, you can store that information in the database, then add a button, and when the user clicks the button, it opens the project for the next level of the game




Block ID: widget_opennewtabwithurl
Category: Widgets
Can be used for 3D: false
Syntax: open URL [URL] in new browser tab
Usage Example: open URL [https://cnn.com] in new browser tab
QuickDescription: 


Description: 
opens the specified URL in a new browser tab.




Block ID: widget_applylayoutrowheightcellwidth
Category: Widgets
Can be used for 3D: false
Syntax: apply layout row named [ROWNAME] height (HEIGHT)% cell width [CELLWIDTH1]% [CELLWIDTH2]% [CELLWIDTH3]% [CELLWIDTH4]% [CELLWIDTH5]% [CELLWIDTH6]% widgets [WIDGET1] [WIDGET2] [WIDGET3] [WIDGET4] [WIDGET5] [WIDGET6] margin (MARGIN) padding (PADDING)
Usage Example: apply layout row named [row1] height (20)% cell width [20]% [80]% []% []% []% []% widgets [label1] [textbox1] [] [] [] [] margin (10) padding (5)
QuickDescription: 


Description: 
sets the dimensions and positions of one or more widgets by placing them in a virtual row. Use this block multiple times to add more virtual rows. Each virtual row has the specified height as percent of the total stage height. Each virtual row contains one or more cells, and you can specify the width of each cell and which widget to place in each cell. You can set the margins and padding of all widgets. This block is more convenient than calculating the position and dimensions of each widget one by one.
Example Program:

when green flag clicked
    // [no need to specify each button's position or size, since the 'apply layout' block will manage them for us]
    add button [Button 1] at X (0) Y (0) width (100) height (30) tooltip [ ] as [b1]
    add button [Button 2] at X (0) Y (0) width (100) height (30) tooltip [ ] as [b2]
    // [Top row with 40% of the stage height, split into 3 cells or 40:20:40 wide. Please b1 into first cell and b2 into the third cell]
    apply layout row named [r1] height (40)% cell width [40]% [20]% [40]% [ ]% [ ]% [ ]% widgets [b1] [NAME2] [b2] [ ] [ ] [ ] margin (10) padding (5)
    // [add an empty row that's 10% of stage height, with no widgets in it]
    apply layout row named [r2] height (10)% cell width [WIDTH1]% [WIDTH2]% [ ]% [ ]% [ ]% [ ]% widgets [NAME1] [NAME2] [ ] [ ] [ ] [ ] margin (10) padding [PADDING]
    add button [Button 3] at X (0) Y (0) width (100) height (30) tooltip [ ] as [b3]
    add button [Button 4] at X (0) Y (0) width (100) height (30) tooltip [ ] as [b4]
    add button [Button 5] at X (0) Y (0) width (100) height (30) tooltip [ ] as [b5]
    // [The third row takes the bottom 50% of height, split into 3 cells of 30:30:40 wide]
    apply layout row named [r3] height (50)% cell width [30]% [30]% [40]% [ ]% [ ]% [ ]% widgets [b3] [b4] [b5] [ ] [ ] [ ] margin (10) padding (5)
end




Block ID: widget_addtabs
Category: Widgets
Can be used for 3D: false
Syntax: create tabs at X (X) Y (Y) width (WIDTH) height (HEIGHT) names [TAB1] [TAB2] [TAB3] [TAB4] [TAB5] [TAB6] [TAB7] [TAB8] show heading [SHOWHEADING v]
Usage Example: create tabs at X (0) Y (0) width (480) height (360) names [t1] [t2] [] [] [] [] [] [] show heading [Yes v]
QuickDescription: 


Description: 
creates a tabs widget centered at (X, Y), with the given WIDTH and HEIGHT. You can specify up to 8 tab names of TAB1 to TAB8, and blank tab names are ignored. The SHOWHEADING option can be set to 'Yes' or 'No'.




Block ID: widget_selecttab
Category: Widgets
Can be used for 3D: false
Syntax: select tab [TABNAME]
Usage Example: select tab [t1]
QuickDescription: 


Description: 
selects the tab named TABNAME, bringing it to the foreground with all the widgets inside that tab




Block ID: widget_settabcontainer
Category: Widgets
Can be used for 3D: false
Syntax: set tab container [TABNAME v]
Usage Example: set tab container [t1 v]
QuickDescription: 


Description: 
sets the tab named TABNAME as the widget container, so all widgets added after this block will be added into this tab.




Block ID: widget_showhidetabnamed
Category: Widgets
Can be used for 3D: false
Syntax: [ACTION v] tab named [TABNAME]
Usage Example: [show v] tab named [t1]
QuickDescription: 


Description: 
Take an ACTION on the tab named TABNAME. The ACTION can be 'show' or 'hide' to change visibility of the tab, or 'add' and 'remove' to add or remove a tab.




Block ID: widget_whentabselected
Category: Widgets
Can be used for 3D: false
Syntax: when tab [TABNAME v] selected
Usage Example: when tab [t1 v] selected
QuickDescription: 


Description: 
A hat-block that is triggered when the tab named TABNAME is selected and displayed




Block ID: widget_drawchartusinglist
Category: Widgets
Can be used for 3D: false
Syntax: draw [CHARTTYPE v] chart using list [LISTNAME v] x (X) y (Y) width (WIDTH) height (HEIGHT)
Usage Example: draw [line v] chart using list [list1 v] x (0) y (0) width (100) height (100)
QuickDescription: 


Description: 
draws a chart of the selected CHARTTYPE, which can be 'line', 'bar', 'pie' or 'percentage', with the data in the list named LISTNAME. Since only a single list of data points is provided to draw the chart, the X axis of the chart will be labeld using each data point's index, starting at 1. The Y axis of the chart will be the value range of all the data points in the list. The chart will center at the (X, Y) position on the stage, with the size of WIDTH and HEIGHT.




Block ID: widget_drawchartusingcolumn
Category: Widgets
Can be used for 3D: false
Syntax: draw [CHARTTYPE v] chart using columns [COLUMNLIST] from table [TABLENAME v] x (X) y (Y) width (WIDTH) height (HEIGHT)
Usage Example: draw [line v] chart using columns [age,height] from table [k v] x (0) y (0) width (100) height (100)
QuickDescription: 
draws a chart of the selected CHARTTYPE

Description: 
draws a chart of the selected CHARTTYPE, which can be 'line', 'bar', 'pie' or 'percentage', with the data in the table named TABLENAME. The data can come from one or multiple columns in the table. The column names can be specified using COLUMNLIST as a comma-separated list. Each column of data is treated as one data series when they are plotted. The X axis of the chart will be labeld using each data point's row number, starting at 1. The Y axis of the chart will be the value range of all the data points in all the selected columns. The chart will center at the (X, Y) position on the stage, with the size of WIDTH and HEIGHT.




Block ID: widget_drawchartusingcategory
Category: Widgets
Can be used for 3D: false
Syntax: draw pie chart using category [CATEGORYCOLUMN] and value [VALUECOLUMN] from table [TABLENAME v] x (X) y (Y) width (WIDTH) height (HEIGHT)
Usage Example: draw pie chart using category [grade] and value [height] from table [student table v] x (0) y (0) width (100) height (100)
QuickDescription: 


Description: 
draws a pie chart using data from the table named TABLENAME. The data from the column named VALUECOLUMN will be used to calculate the percentage of each row, and the data from the column named CATEGORYCOLUMN will be used as labels in the pie chart for each row. The chart will center at the (X, Y) position on the stage, with the size of WIDTH and HEIGHT.




Block ID: widget_progressbar
Category: Widgets
Can be used for 3D: false
Syntax: add progress bar as (CURRENT) out of total (TOTAL) at x (X) y (Y) width (WIDTH) height (HEIGHT) color [COLOR] background [BG] border width (BORDERWIDTH) color [BORDERCOLOR] as [NAME]
Usage Example: add progress bar as (50) out of total (100) at x (0) y (0) width (200) height (20) color [#1777FFFF] background [#F0F0F0FF] border width (0) color [#F0F0F0FF] as [progressbar1]
QuickDescription: 
adds a progress bar widget

Description: 
adds a progress bar widget. Its initial value will be caluculated as a percentage of the CURRENT value divided by the TOTAL value. For example, if TOTAL is 200 and CURRENT is 50, then the progressbar will show a progress of 25%. However, when we read the value of the progress bar, we will still get 50. The progress bar will center at the (X, Y) position on the stage, with the size of WIDTH and HEIGHT. The color of the 'completed' portion of the bar will be COLOR, and the color of the remainder portion will be BG. You can customize the style of the border using BORDERCOLOR and BORDERWIDTH. The progress bar will be given the name of NAME.




Block ID: widget_createchatwindow
Category: Widgets
Can be used for 3D: false
Syntax: add chat window x (X) y (Y) width (WIDTH) height (HEIGHT) input rows (ROWS) background [BG] border [BORDERCOLOR] name [NAME]
Usage Example: add chat window x (0) y (0) width (480) height (360) input rows (1) background [#F0F0F0FF] border [#000000FF] name [chat1]
QuickDescription: 
adds a chat window widget to the stage, centered at the position (X, Y) with dimension of WIDTH and HEIGHT. The chat window has 2 parts. At the bottom is a wide input box on the left and a send button on the right. On the top is a chat history panel for displaying all previous messages in the chat.

Description: 
adds a chat window widget to the stage, centered at the position (X, Y) with dimension of WIDTH and HEIGHT. The chat window has 2 parts. At the bottom is a wide input box on the left and a send button on the right. On the top is a chat history panel for displaying all previous messages in the chat. When we use it, there is no need to add another input textbox or button separately. The ROWS input controls how many rows are allowed in the input box at the bottom. The background color of the chat windiw is controlled by BG, and its border color will be BORDERCOLOR. The chat window will have a name of NAME.

Note that when the user clicks the send button at the bottom of the chat window or press ENTER, the chat message will NOT be appended to the chat history window automatically. Instead, you will need to handle this event using the 'when widget [NAME v] clicked' block. To read the text of the user input, use the 'value of widget [WIDGETNAME v]' block. To add any message to the chat window's chat history panel, use the 'append to chat [CHATNAME v] message [MESSAGE] as [SENDER] icon [ICON v] align [ALIGN v] text size (TEXTSIZE) color [COLOR] background [BGCOLOR]' block. You can also update the content of the last message in the chat history panel using the 'update last chat message to [MESSAGE] for chat [CHATNAME v]' block, so when the message is being typed in or being generated by a chatbot, you can update the message from the chatbot continuously as they are being generated.




Block ID: widget_appendchatmessage
Category: Widgets
Can be used for 3D: false
Syntax: append to chat [CHATNAME v] message [MESSAGE] as [SENDER] icon [ICON v] align [ALIGN v] text size (TEXTSIZE) color [COLOR] background [BG]
Usage Example: append to chat [chat1 v] message [hi] as [Joe] icon [ROBOT v] align [Left v] text size (14) color [#000000FF] background [#F0F0F0FF]
QuickDescription: 
appends a new MESSAGE to the chat history panel of the chat window named CHATNAME

Description: 
appends a new MESSAGE to the chat history panel of the chat window named CHATNAME. The SENDER option specifies the name of the sender, as displayed next to the new message in the chat history panel. The ICON option specifies the icon displayed next to the new message in the chat history panel. It can be 'ROBOT', 'USER', or the name of one of the costumes in this sprite. The ALIGN parameter can be 'Left' or 'Right', and it controls whether the new message is displayed to the left or right side in the chat history panel. The text in the message can be styled using TEXTSIZE and COLOR. And the background of the message bubble will be BG.




Block ID: widget_updatelastchatmessage
Category: Widgets
Can be used for 3D: false
Syntax: update last chat message to [MESSAGE] for chat [CHATNAME v]
Usage Example: update last chat message to [good morning] for chat [chat1 v]
QuickDescription: 


Description: 
updates the last message in the chat history panel of the chat window named CHATNAME. MESSAGE will be the new content for that message. This is useful if the last message is being typed in by a remote user in a distributed chat, or it is being generated in streaming mode by a chatbot.




Block ID: widget_disablewidget
Category: Widgets
Can be used for 3D: false
Syntax: [ACTION v] widget [WIDGETNAME v]
Usage Example: [Disable v] widget [button1 v]
QuickDescription: 


Description: 
Take an action on the widget named WIDGETNAME. The ACTIOn can be 'Disable' or 'Enable'. When a widget is disabled, it will not respond to user interactions.




Block ID: widget_deletecostume
Category: Widgets
Can be used for 3D: false
Syntax: delete costume [COSTUMENAME]
Usage Example: delete costume [front]
QuickDescription: 


Description: 
deletes the costume of the given name




Block ID: mp_createmultiplayergame
Category: Multiplayer
Can be used for 3D: false
Syntax: create game named [GAMENAME] password [PASSWORD] my name [HOSTNAME] role [ROLE] server [LOCATION v] capacity (CAPACITY) world width (W) height (H)
Usage Example: create game named [game 1] password [123] my name [host] role [player 1] server [US-East v] capacity (2) world width (480) height (360)
QuickDescription: 


Description: 
creates a new multiplayer game of size W by H with the given GAMENAME on the game server at the LOCATION, and total number of players is CAAPCITY. Others will need to provide the same PASSWORD to join this game. My display name will be HOSTNAME in the game, and my role will be ROLE, which can be used to specify the team or game character.




Block ID: mp_listmultiplayergameusers
Category: Multiplayer
Can be used for 3D: false
Syntax: list players in game [GAMENAME] hosted by [HOSTNAME] from server [LOCATION v] in table [TABLE v]
Usage Example: list players in game [game 1] hosted by [host] from server [US-East v] in table [players v]
QuickDescription: 


Description: 
fetch data from the game server at the given LOCATION for the list of all players in the game named GAMENAME that is hosted by HOSTNAME, and write the data in the given table. Each row will be info about one player, which includes these columns:'Player Name' for the player's display name, and 'Role' for the role of that player.




Block ID: mp_resetmultiplayergame
Category: Multiplayer
Can be used for 3D: false
Syntax: reset game world
Usage Example: reset game world
QuickDescription: 


Description: 
clean up all objects in the game so the game can be restarted




Block ID: mp_listmultiplayergames
Category: Multiplayer
Can be used for 3D: false
Syntax: list multiplayer games in server [LOCATION v] in table [TABLE v]
Usage Example: list multiplayer games in server [US-East v] in table [games v]
QuickDescription: 


Description: 
fetch data from the game server at the given LOCATION for the list of all games running on that server, and write the data in the given table. Each row will be info about one game, and the columns are: "Host Name" (display name of the host user), "Game Name" (name of the game), "User Count" (how many players already in the game. Note that for a new player to join any of these games, he/she still needs to know the password.




Block ID: mp_joinmultiplayergame
Category: Multiplayer
Can be used for 3D: false
Syntax: join multiplayer game named [GAMENAME] by host [HOSTNAME] from server [LOCATION v] with password [PASSWORD] my name [DISPLAYNAME] role [ROLE]
Usage Example: join multiplayer game named [game 1] by host [host] from server [US-East v] with password [123] my name [player 2] role [player 2]
QuickDescription: 


Description: 
joins an existing multiplayer game with the given GAMENAME on the game server at the LOCATION, and provide the PASSWORD to get permission. My name in the game will be DISPLAYNAME, and my role will be ROLE, which can be used to specify the team or game character.




Block ID: mp_addspritetogame
Category: Multiplayer
Can be used for 3D: false
Syntax: add this sprite to game as a [MODE v] [SHAPE v]
Usage Example: add this sprite to game as a [Dynamic v] [Rectangle v]
QuickDescription: 


Description: 
adds this sprite as an object into the connected game world. MODE can be "Dynamic" or "Static", and Static objects won't move. SHAPE can be 'Rectangle' or 'Circle', which controls the collider shape for this sprite.




Block ID: mp_whenaddedtogame
Category: Multiplayer
Can be used for 3D: false
Syntax: when added to game
Usage Example: when added to game
QuickDescription: 


Description: 
When this sprite or clone receives confirmation from game server that it is registered as part of game. This block is triggered on both the client where this sprite is added to game using 'add sprite to game' block, and on all other clients where this sprite is replicated.




Block ID: mp_removespritefromgame
Category: Multiplayer
Can be used for 3D: false
Syntax: remove this sprite from game
Usage Example: remove this sprite from game
QuickDescription: 


Description: 
removes this sprite from the game world.




Block ID: mp_setsyncmovement
Category: Multiplayer
Can be used for 3D: false
Syntax: synchronously set speed x (X) y (Y)
Usage Example: synchronously set speed x (0) y (0)
QuickDescription: 


Description: 
sets the x and y speed of this sprite in the game world so this sprite and its replicates on other clients will move at the same speed.




Block ID: mp_setsyncmovement2
Category: Multiplayer
Can be used for 3D: false
Syntax: synchronously set speed (SPEED) dir (DIR)
Usage Example: synchronously set speed (200) dir (90)
QuickDescription: 


Description: 
Set this sprite to move with the given speed in the given direction in degrees. This will set the speed for the 2D representation of this sprite in the game server's simulation, which in turn sets the position of all clones of this sprite in all clients.




Block ID: mp_broadcastmessagetoall
Category: Multiplayer
Can be used for 3D: false
Syntax: broadcast [MESSAGE v] with parameter [PARAMETER] mode [MODE v]
Usage Example: broadcast [heal v] with parameter [20] mode [All Sprites v]
QuickDescription: 


Description: 
broadcast a message of the given message type to all players in the game, with an optional parameter. MODE can be 'All Sprites' if the message should be received by all sprites in all players' browser, or 'Exclude Replicate' if the message should only be received by the sprites that are original sprite (not replicate sprites that mirror remote original sprites)




Block ID: mp_broadcasttouchmessage
Category: Multiplayer
Can be used for 3D: false
Syntax: when touching [SPRITENAME v] will [STOPTYPE v] and trigger [MESSAGE v] with parameter [PARAMETER]
Usage Example: when touching [Sprite1 v] will [stop v] and trigger [message1 v] with parameter [ ]
QuickDescription: 


Description: 
this block specifies what happens when this sprite touches another sprite named SPRITENAME. STOPTYPE can be these values: 'stop' means this sprite will stop, 'stop and delete' means this sprite will stop and the touched sprite will be deleted from the game world, 'continue' means this sprite will simply continue its movement (no collision), and 'continue and delete' means this sprite will continue but the touched sprite will be deleted. we can also specify a message to be sent to this sprite and the touched sprite, with an optional parameter.




Block ID: mp_isconnectedtogame
Category: Multiplayer
Can be used for 3D: false
Syntax: connected to game
Usage Example: connected to game
QuickDescription: 


Description: 
a boolean block indicating whether we are peroperly connected to the game world




Block ID: data_rowatindexoftable
Category: Variables
Can be used for 3D: false
Syntax: row (ROWINDEX) of table [TABLENAME v] separator [SEPARATOR]
Usage Example: row (1) of table [table1 v] separator [,]
QuickDescription: 


Description: 
A reporter block that returns all the data in the given row with row index of ROWINDEX of the given table named TABLENAME. The data values will be joined into a string as separated by the specified SEPARATOR. This block is handy for reading all cells from a row




Block ID: data_rowindexwithcondition
Category: Variables
Can be used for 3D: false
Syntax: row # of [VALUE] in column [COLUMN] in table [TABLENAME v]
Usage Example: row # of [john] in column [name] in table [table1 v]
QuickDescription: 


Description: 
A reporter block that returns the row index of a the given VALUE in the column named COLUMN of the table named TABLENAME. If the value is not found, it returns -1. Note that the row index of tables starts at 1.




Block ID: data_rowindexwithcondition2
Category: Variables
Can be used for 3D: false
Syntax: row # of item containing [SUBSTRING] in column [COLUMN] in table [TABLENAME v]
Usage Example: row # of item containing [zh] in column [name] in table [table1 v]
QuickDescription: 


Description: 
A reporter block that looks through the data in the column named COLUMN in the table named TABLENAME, and returns the row index of the first item that contains the given SUBSTRING. If the value is not a substring of any item in that column, this block will returns -1.




Block ID: data_addrowtotable
Category: Variables
Can be used for 3D: false
Syntax: add to table [TABLENAME v]: [CELL1] [CELL2] [CELL3] [CELL4] [CELL5] [CELL6] [CELL7] [CELL8] [CELL9] [CELL10] [CELL11] [CELL12]
Usage Example: add to table [table1 v]: [a] [b] [] [] [] [] [] [] [] [] [] []
QuickDescription: 


Description: 
appends a new row of data to the table named TABLENAME at the bottom with values of CELL1 to CELL12. Any empty input will be ignored, and at most 12 data points can be appended using this block.




Block ID: data_removeallcolumnsfromtable
Category: Variables
Can be used for 3D: false
Syntax: delete all columns from table [TABLENAME v]
Usage Example: delete all columns from table [table1 v]
QuickDescription: 


Description: 
deletes all columns from the table named TABLENAME so it becomes empty with no columns.




Block ID: data_addcolatposition
Category: Variables
Can be used for 3D: false
Syntax: add column [COLUMNNAME] at position (POSITION) to table [TABLENAME v]
Usage Example: add column [age] at position (1) to table [table1 v]
QuickDescription: 


Description: 
adds a new column named COLUMNNAME at the column position of POSITION in the table named TABLENAME. The POSITION of the first column is 1.




Block ID: data_insertrowtotable
Category: Variables
Can be used for 3D: false
Syntax: insert at row (ROWNUM) of table [TABLENAME v]: [CELL1] [CELL2] [CELL3] [CELL4] [CELL5] [CELL6] [CELL7] [CELL8] [CELL9] [CELL10] [CELL11] [CELL12]
Usage Example: insert at row (1) of table [table1 v]: [c] [d] [] [] [] [] [] [] [] [] [] []
QuickDescription: 


Description: 
inserts a new row of data at the specified row index of ROWNUM (first row has a row index of 1) to the table named TABLENAME. The value of the data cells in this row will be CELL1 to CELL12.. Empty cell values are ignored.




Block ID: data_replacerowoftable
Category: Variables
Can be used for 3D: false
Syntax: replace row (ROWNUM) of table [TABLENAME v] with: [CELL1] [CELL2] [CELL3] [CELL4] [CELL5] [CELL6] [CELL7] [CELL8] [CELL9] [CELL10] [CELL11] [CELL12]
Usage Example: replace row (1) of table [table1 v] with: [2] [sophia] [] [] [] [] [] [] [] [] [] []
QuickDescription: 


Description: 
replaces the data in the row at the specified row index of ROWNUM (first row has a row index of 1) in the table named TABLENAME. The value of the cells in this row will be CELL1 to CELL12. Empty cell values are ignored.




Block ID: data_replaceitematrowcolumn
Category: Variables
Can be used for 3D: false
Syntax: replace item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] with [VALUE]
Usage Example: replace item at row (1) column [age] of table [table1 v] with [13]
QuickDescription: 


Description: 
replaces the item at the row index of ROWNUM and column named COLUMN in the table named TABLENAME with the new value of VALUE.




Block ID: data_reduceitematrowcolumn
Category: Variables
Can be used for 3D: false
Syntax: reduce item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)
Usage Example: reduce item at row (1) column [age] of table [table1 v] by (1)
QuickDescription: 


Description: 
reduces the value of the item at row index of ROWNUM (first row has an index of 1) and the column named COLUMN in the table named TABLENAME by the CHANGEAMOUNT.




Block ID: data_changeitematrowcolumn
Category: Variables
Can be used for 3D: false
Syntax: change item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)
Usage Example: change item at row (1) column [age] of table [table1 v] by (1)
QuickDescription: 


Description: 
change the value of the item at row index of ROWNUM (first row has an index of 1) and the column named COLUMN in the table named TABLENAME by the CHANGEAMOUNT.




Block ID: data_settabletocomputed
Category: Variables
Can be used for 3D: false
Syntax: set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2]
Usage Example: set table [table1 v] to [smallest v] of column [age] in table [table2 v] by column [grade]
QuickDescription: 


Description: 
update the value of the table named TABLENAME1 by aggregating the data from the table named TABLENAME2. The data in COLUMN2 of the table named TABLENAME2 will be grouped by the value of items in the column named COLUMN1, and the aggregation METHOD can be 'minimum', 'maximum', 'sum', 'average', 'median'. Note that this block will only be available when you have at least 2 tables defined in the project.
Example Program:

when green flag clicked
    // [delete all columns will also remove all data]
    delete all columns from table [t1 v]
    // [add 3 columns, but there are no rows yet]
    add column [name] at position (1) to table [t1 v]
    add column [gender] at position (2) to table [t1 v]
    add column [score] at position (3) to table [t1 v]
    // [add 4 rows of data]
    add to table [t1 v]: [Joe] [M] [92] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Mike] [M] [96] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Sophia] [F] [100] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Jenny] [F] [98] [] [] [] [] [] [] [] [] []
    // [generate average score for gender of M vs F, so the summary table will have 2 columns of gender and score, and the first row will be M and 94, and second row will be F and 99]
    set table [summary v] to [largest v] of column [score] in table [t1 v] by column [gender]
end




Block ID: data_reshuffletable
Category: Variables
Can be used for 3D: false
Syntax: reshuffle table [TABLENAME v] randomly
Usage Example: reshuffle table [table1 v] randomly
QuickDescription: 


Description: 
reshuffles the rows of the table named TABLENAME randomly.




Block ID: data_sorttablebycolumn
Category: Variables
Can be used for 3D: false
Syntax: sort table [TABLENAME v] by column [COLUMN] [SORTORDER v]
Usage Example: sort table [table1 v] by column [age] [SORTORDER v]
QuickDescription: 


Description: 
sorts the table named TABLENAME by the specified column named COLUMN in the order of SORTORDER, which can be 'large to small' or 'small to large'.




Block ID: data_deleterowoftable
Category: Variables
Can be used for 3D: false
Syntax: delete row (ROWNUM) of table [TABLENAME v]
Usage Example: delete row (1) of table [table1 v]
QuickDescription: 


Description: 
deletes the row at the index of ROWNUM (first row has an index of 1) from the table named TABLENAME and then shift all rows below that row up by one row.




Block ID: data_deleterowwithcondition
Category: Variables
Can be used for 3D: false
Syntax: delete rows with column [COLUMN] of value [VALUE] from table [TABLENAME v]
Usage Example: delete rows with column [x] of value [1] from table [table1 v]
QuickDescription: 


Description: 
deletes all rows from the table named TABLENAME where the column named COLUMN has the given VALUE.




Block ID: data_deleteallrowsoftable
Category: Variables
Can be used for 3D: false
Syntax: delete all rows from table [TABLENAME v]
Usage Example: delete all rows from table [table1 v]
QuickDescription: 


Description: 
deletes all rows from the table named TABLENAME but keep the columns.




Block ID: data_deletecolumnfromtable
Category: Variables
Can be used for 3D: false
Syntax: delete column [COLUMNNAME] from table [TABLENAME v]
Usage Example: delete column [age] from table [table1 v]
QuickDescription: 


Description: 
deletes the column named COLUMNNAME from the table named TABLENAME.




Block ID: data_rowcountoftable
Category: Variables
Can be used for 3D: false
Syntax: row count of table [TABLENAME v]
Usage Example: row count of table [table1 v]
QuickDescription: 


Description: 
A reporter block that returns the total number of rows in the table named TABLENAME.




Block ID: data_computetable
Category: Variables
Can be used for 3D: false
Syntax: [METHOD] of column [COLUMNNAME] in table [TABLE v]
Usage Example: [smallest v] of column [age] in table [table1 v]
QuickDescription: 


Description: 
A reporter block that aggregates all the items in the column named COLUMNNAME in the table named TABLE. You can choose from 5 aggregation methods: 'smallest', 'largest', 'sum', 'average', 'median'..




Block ID: data_itematrowcolumnoftable
Category: Variables
Can be used for 3D: false
Syntax: item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v]
Usage Example: item at row (1) column [age] of table [table1 v]
QuickDescription: 


Description: 
A reporter block that returns the content of the one item at the row index of ROWINDEX (first row has an index of 1) and the given column named COLUMNANE of the table named TABLE.




Block ID: data_copy_table_into_table
Category: Variables
Can be used for 3D: false
Syntax: copy table [TABLE1] into [TABLE2]
Usage Example: copy table [table1 v] into [table2 v]
QuickDescription: 


Description: 
copies all rows the table named TABLE1 into the table named TABLE2, which replaces any existing data in TABLE2. After this block these 2 tables will have exactly the same columns with the same content in them.




Block ID: data_append_table_into_table
Category: Variables
Can be used for 3D: false
Syntax: append table [TABLE1] to [TABLE2]
Usage Example: append table [table1 v] to [table2 v]
QuickDescription: 


Description: 
appends the rows of table named TABLE1 to the bottom of the table named TABLE2. These 2 tables should have the same columns.




Block ID: data_pivot_table_into_table
Category: Variables
Can be used for 3D: false
Syntax: pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST]
Usage Example: pivot [table1 v] into [table2 v] row groups [gender,grade] columns [age,height] methods [average,maximum]
QuickDescription: 


Description: 
creates a pivot table using data from TABLE1 and stores the pivot table data in TABLE2. This block groups the data in TABLE1 using the list of columns specified in ROWGROUPLIST. The data values of the pivot table will come from the columns VALUECOLUMNLIST, and these columns will be aggregated using the methods given in METHODLIST. Both VALUECOLUMNLIST and METHODLIST are comma-separated lists. Each item in the VALUECOLUMNLIST is the name of one column, and it will be aggregated by the corrsponding method specified in METHODLIST. The methods can be 'sum', 'maximum', 'mimimum' or 'average'.
Example Program:

when green flag clicked
    // [delete all columns will also remove all data]
    delete all columns from table [t1 v]
    // [add 3 columns, but there are no rows yet]
    add column [name] at position (1) to table [t1 v]
    add column [gender] at position (2) to table [t1 v]
    add column [score] at position (3) to table [t1 v]
    // [add 4 rows of data]
    add to table [t1 v]: [Joe] [M] [92] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Mike] [M] [96] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Sophia] [F] [100] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Jenny] [F] [98] [] [] [] [] [] [] [] [] []
    // [generate average score for gender of M vs F, so the summary table will have 2 columns of 'gender' and 'avg score', and the first row will be M and 94, and second row will be F and 99]
    pivot [t1 v] into [summary v] row groups [gender] columns [score] methods [average]
end






Block ID: data_showsnapshotoftable
Category: Variables
Can be used for 3D: false
Syntax: show snapshot of table [TABLENAME v] from row (STARTROW) to (ENDROW) with style [STYLE] [THEMECOLOR]
Usage Example: show snapshot of table [table1 v] from row (1) to (10) with style [style1 v] [#1E54B6FF]
QuickDescription: 


Description: 
shows the content of the specified table TABLENAME in a pop up window between the STARTROW and ENDROW. The STYLE is a dropdown with 4 style choices of 'style1', 'style2', 'style3' and 'style4'. You can also specify a theme color as THEMECOLOR.




Block ID: data_lookuptable
Category: Variables
Can be used for 3D: false
Syntax: item in column [RETURNCOLUMN] of [TABLENAME v] where column [SEARCHCOLUMN] equals [SEARCHTEXT]
Usage Example: item in column [age] of [table1 v] where column [name] equals [John]
QuickDescription: 


Description: 
A reporter block that returns the item in the column RETURNCOLUMN of the table named TABLENAME where another column SEARCHCOLUMN equals the value of SEARCHTEXT. This block can be used to look for an item in one column using the value in another column.




Block ID: data_exporttable
Category: Variables
Can be used for 3D: false
Syntax: export table [TABLENAME v] as [FILENAME]
Usage Example: export table [table1 v] as [datatable]
QuickDescription: 


Description: 
exports the table named TABLENAME as a csv file named FILENAME. If FILENAME is empty, then use the table name as the file name. The file extension is set to '.csv' automatically.




Block ID: data_importtable
Category: Variables
Can be used for 3D: false
Syntax: import file into table [TABLE]
Usage Example: import file into table [TABLE]
QuickDescription: 


Description: 
Display a file selection dialog window for user to pick a txt or csv file, then read the content of the select file and split it into rows and columns, and store it in the given table variable. If user does not select any file, the variable will be unchanged.




Block ID: data_savetable
Category: Variables
Can be used for 3D: false
Syntax: save table [TABLE v] to server as [DATANAME]
Usage Example: save table [tt v] to server as [info]
QuickDescription: 


Description: 
save the value of the entire table to the CreatiCode server with the given name




Block ID: data_loadtable
Category: Variables
Can be used for 3D: false
Syntax: load [DATANAME] from server into table [TABLE v]
Usage Example: load [info] from server into table [tt v]
QuickDescription: 


Description: 
read data from the CreatiCode server with the given DATANAME and write them in the given table.




Block ID: data_showtable
Category: Variables
Can be used for 3D: false
Syntax: show table [TABLENAME v]
Usage Example: show table [table1 v]
QuickDescription: 


Description: 
displays the table named TABLENAME on the stage.




Block ID: data_hidetable
Category: Variables
Can be used for 3D: false
Syntax: hide table [TABLENAME v]
Usage Example: hide table [table1 v]
QuickDescription: 


Description: 
hides the table named TABLENAME from the stage.




Block ID: data_setlisttocolumn
Category: Variables
Can be used for 3D: false
Syntax: copy list [LISTNAME v] to column [COLUMNNAME] of table [TABLENAME v]
Usage Example: copy list [i v] to column [age] of table [table1 v]
QuickDescription: 


Description: 
copies the contents of the list LISTNAME into the column COLUMNNAME of the table TABLENAME. The column must already exists in the table, and all existing data items in that column will be removed before the new data from the list is copied over. 




Block ID: p2p_fetchfromurl
Category: Cloud
Can be used for 3D: false
Syntax: fetch web page as [FORMAT] from URL [URL]
Usage Example: fetch web page as [markdown v] from URL [example.com]
QuickDescription: 


Description: 
fetch the content of the given web page as markdown




Block ID: p2p_removecolumnsfromsheet
Category: Cloud
Can be used for 3D: false
Syntax: remove columns [FROMC] to [TOC] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]
Usage Example: remove columns [H] to [Z] from sheet [sheet1] in Google Sheet at URL [example.com]
QuickDescription: 


Description: 
remove the specified columns




Block ID: p2p_removerowsfromsheet
Category: Cloud
Can be used for 3D: false
Syntax: remove rows [FROMR] to [TOR] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]
Usage Example: remove rows [10] to [15] from sheet [sheet1] in Google Sheet at URL [example.com]
QuickDescription: 


Description: 
remove the specified rows




Block ID: p2p_insertcolumnsinsheet
Category: Cloud
Can be used for 3D: false
Syntax: insert [COUNT] columns at column [STARTC] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]
Usage Example: insert [2] columns at column [B] in sheet [sheet1] in Google Sheet at URL [example.com]
QuickDescription: 


Description: 
insert some new columns to the right of the specified column




Block ID: p2p_insertrowsinsheet
Category: Cloud
Can be used for 3D: false
Syntax: insert [COUNT] rows at row [STARTR] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]
Usage Example: insert [2] rows at row [5] in sheet [sheet1] in Google Sheet at URL [example.com]
QuickDescription: 


Description: 
insert some new rows below the specified row




Block ID: p2p_clearsheet
Category: Cloud
Can be used for 3D: false
Syntax: clear sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]
Usage Example: clear sheet [sheet1] in Google Sheet at URL [example.com]
QuickDescription: 


Description: 
clear all content of the specified sheet




Block ID: p2p_readfromgooglesheet
Category: Cloud
Can be used for 3D: false
Syntax: read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]
Usage Example: read from google sheet: url [https://docs.google.com/spreadsheets/d/103DSwIyL4IZVq5te8QqatctJrEVO1mx878J2ah8fAGA/edit?usp=sharing] sheet name [Sheet1] range [B2:G11] into table [tt v]
QuickDescription: 


Description: 
reads data from a Google Sheet at the given URL. Read the data in the sheet named SHEETNAME, and the range of cells will be the given RANGE. The data will be stored in the table named TABLENAME.




Block ID: p2p_writeintogooglesheet
Category: Cloud
Can be used for 3D: false
Syntax: write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]
Usage Example: write into google sheet: url [https://docs.google.com/spreadsheets/d/103DSwIyL4IZVq5te8QqatctJrEVO1mx878J2ah8fAGA/edit?usp=sharing] sheet name [Sheet2] starting cell [B2] from table [tt v]
QuickDescription: 


Description: 
writes data from the table named TABLENAME into a Google Sheet shared at the given URL. Specify where to write the data in the google sheet using sheet name of SHEETNAME and specify the starting cell's address CELL. Specify which table will be the source data table using TABLENAME. All the data in that table, including the first row of column headers, will be written into the google sheet, starting from the cell at ADDRESS.




Block ID: p2p_listSheetsInGoogleSheet
Category: Cloud
Can be used for 3D: false
Syntax: list all sheets in google sheet at URL [SHEET_URL] into list [LIST]
Usage Example: list all sheets in google sheet at URL [https://xxx] into list [list1 v]
QuickDescription: 


Description: 
get the names of all sheets in the given google sheet and store them in the given list




Block ID: p2p_addsheet
Category: Cloud
Can be used for 3D: false
Syntax: add sheet [SHEETNAME] to google sheet at URL [URL]
Usage Example: add sheet [summary] to google sheet at URL [https://docs.google.com/spreadsheets/d/aaaa/edit?usp=sharing]
QuickDescription: 


Description: 
add a new sheet with the given name to the google sheet




Block ID: p2p_removesheet
Category: Cloud
Can be used for 3D: false
Syntax: remove sheet [SHEETNAME] from google sheet at URL [URL]
Usage Example: remove sheet [summary] from google sheet at URL [https://docs.google.com/spreadsheets/d/aaaa/edit?usp=sharing]
QuickDescription: 


Description: 
remove the sheet with the given name from the google sheet




Block ID: p2p_appendrow
Category: Cloud
Can be used for 3D: false
Syntax: append row [ROWNUMBER] from table [TABLENAME v] to sheet [SHEETNAME] in Google Sheet at URL [URL]
Usage Example: append row [2] from table [t1 v] to sheet [summary] in Google Sheet at URL [https://docs.google.com/spreadsheets/d/aaaa/edit?usp=sharing]
QuickDescription: 


Description: 
read all values in the given row of the given table, then append them to the bottom of the data in the given sheet of the google sheet




Block ID: p2p_setvalue
Category: Cloud
Can be used for 3D: false
Syntax: set value to [VALUE] at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]
Usage Example: set value to [abc] at row (2) column (3) of sheet [summary] in Google Sheet at URL [https://docs.google.com/spreadsheets/d/aaaa/edit?usp=sharing]
QuickDescription: 


Description: 
set the value at the given row and col in the given sheeet of the google sheet




Block ID: p2p_getvalue
Category: Cloud
Can be used for 3D: false
Syntax: value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]
Usage Example: value at row (2) column (3) of sheet [summary] in Google Sheet at URL [https://docs.google.com/spreadsheets/d/aaaa/edit?usp=sharing]
QuickDescription: 


Description: 
reporter block to read the value at the given row and col in the given sheeet of the google sheet




Block ID: p2p_getgooglefoldercontent
Category: Cloud
Can be used for 3D: false
Syntax: list content of Google Drive folder [URL] in table [TABLENAME v]
Usage Example: list content of Google Drive folder [https://xxx] in table [t1 v]
QuickDescription: 


Description: 
list the files and subfolders in the given Google Drive folder in the table with these columns: filename, fileid, mimetype, url




Block ID: looks_addcostumefromstagesnapshot
Category: Looks
Can be used for 3D: false
Syntax: add stage snapshot as costume named [NAME]
Usage Example: add stage snapshot as costume named [c1]
QuickDescription: 


Description: 
takes a snapshot of the stage and save it as a costume of this sprite with the given name. this block allows the LLM to "see" the stage if we attach the costume to the chat with the LLM




Block ID: looks_layernumber
Category: Looks
Can be used for 3D: false
Syntax: layer number
Usage Example: layer number
QuickDescription: 


Description: 
The display layer of this sprite




Block ID: looks_draw_text
Category: Looks
Can be used for 3D: false
Syntax: draw text [TEXT] at x (X) y (Y) size (SIZE) color (COLOR) rotation (ROTATION)
Usage Example: draw text [hi] at x (0) y (100) size (18) color (#122829FF) rotation (0)
QuickDescription: 


Description: 
Draw text at the given x and y positions in the given font size and font color. The text can be rorated by the given degrees clockwise. This block can be used to draw text directly on the sprite's current costume assuming it is in vector format, not draw on the stage.




Block ID: looks_clear_drawing
Category: Looks
Can be used for 3D: false
Syntax: clear all drawings
Usage Example: clear all drawings
QuickDescription: 


Description: 
Remove all drawings on this sprite's current costume, assuming it is in vector mode, and the drawings are done also using looks blocks, such as rectangle/oval/text/line/curve.




Block ID: data_joincloudsession
Category: Variables
Can be used for 3D: false
Syntax: join cloud session [SESSION]
Usage Example: join cloud session [1234]
QuickDescription: 


Description: 
joins an existing cloud session so updates to cloud variables are only shared within projects connected to this session. some user has to create the session with the same given name for the same project first




Block ID: data_createcloudsession
Category: Variables
Can be used for 3D: false
Syntax: create cloud session [SESSION]
Usage Example: create cloud session [1234]
QuickDescription: 


Description: 
create a new cloud session so updates to cloud variables will only be shared among projects connected to this session, and other users running this project can join this session after its creation.




Block ID: event_whenvariablechanged
Category: Event
Can be used for 3D: false
Syntax: when variable [VARIABLENAME v] changed
Usage Example: when variable [x v] changed
QuickDescription: 


Description: 
a hat block that's triggered when the value of the specified variable has changed. works for cloud variables as well.




Block ID: sensing_of2
Category: Sensing
Can be used for 3D: false
Syntax: [ATTRIBUTE v] of sprite [TARGET v] with clone ID [CLONEID]
Usage Example: [x position v] of sprite [Tree v] with clone ID [clone1]
QuickDescription: 


Description: 
get an attribute value or its private variable's value of the clone of the given sprite with the given Clone ID




Block ID: sensing_findclones
Category: Sensing
Can be used for 3D: false
Syntax: find clones of [SPRITE v] within distance of (DISTANCE) and write into table [TABLENAME v]
Usage Example: find clones of [Tree v] within distance of (200) and write into table [table1 v]
QuickDescription: 


Description: 
among all clones of the given sprite, find which ones are within the given direct-line distance from the current sprite, and write their info into the given table, sorted by increasting distance. hidden clone/sprite is excluded. original sprite is also counted as a clone with id of "originalsprite". First 4 columns in table will be cloneID, x, y, distance, and more columns for all private variables of these clones. this block is often used to scan for enemy or powerup objects near this sprite.




Block ID: sensing_searchclones
Category: Sensing
Can be used for 3D: false
Syntax: detect clones of [SPRITE v] within forward distance (DISTANCE) width (WIDTH) and write into table [TABLENAME v]
Usage Example: detect clones of [Zombie v] within forward distance (200) width (100) and write into table [table1 v]
QuickDescription: 


Description: 
among all clones of the given sprite, detect which ones are within a rectangle scanning area that is cast forward from current sprite, and write their info into the given table, sorted by increasting distance. hidden clone/sprite is excluded. original sprite is also counted as a clone with id of "originalsprite". the detection rectangle starts at the center of current sprite, look forward along this sprite's direction up to the given distance, and with given scanning width. First 4 columns in table will be cloneID, x, y, distance, and more columns for all private variables of these clones. this block is often used to check for blocking obstacles ahead of this sprite.




## PART 3: WIDGET BLOCKS ORGANIZED BY CATEGORY

### Basic Widgets (Display & Input)
1. widget_addlabel - Add label widget for displaying text
2. widget_addbutton - Add clickable button widget
3. widget_addtextbox - Add single/multi-line textbox for user input
4. widget_addrichtextbox - Add rich text editor with formatting support

### Input Controls
5. widget_addslider - Add slider for numeric input
6. widget_addmenu - Add dropdown menu widget
7. widget_addcolorpicker - Add color picker widget
8. widget_adddatepicker - Add date picker widget
9. widget_addcheckbox - Add checkbox widget
10. widget_addradiobutton - Add radio button group widget

### Value Management
11. widget_valuefromwidget - Get current value from any widget
12. widget_settext - Set value for any widget

### Event Handlers
13. widget_whenwidgetclicked - Detect widget click events
14. widget_whenwidgetchanges - Detect widget value changes
15. widget_whenmouseenter - Detect pointer entering widget area
16. widget_whenmouseleave - Detect pointer leaving widget area
17. widget_whenanybuttonnamedclicked - Handle any button click with single script

### Styling & Appearance
18. widget_settextstyle - Set font, size, color, boldness, alignment
19. widget_setwidgetstyle - Set background, border colors, width, radius

### Layout & Positioning
20. widget_movewidgettoxy - Move widget to position with animation
21. widget_resizewidgettowidthheight - Resize widget with animation
22. widget_scalewidgettowidthheight - Scale widget by percentage
23. widget_rotatewidgetbydegrees - Rotate widget
24. widget_transparencytowidget - Set widget transparency/opacity

### Visibility & Management
25. widget_setvisibility - Show/hide individual widget
26. widget_setvisibilityforall - Show/hide all widgets
27. widget_removewidget - Remove specific widget
28. widget_removeallwidgets - Remove all widgets
29. widget_setzindex - Control widget layering order

### Text Operations
30. widget_appendtext - Append text to widget content

### Media Widgets
31. widget_addvideo - Add YouTube video widget
32. widget_actionvideo - Control video playback (start/pause/stop/mute)
33. widget_seektosecondsvideo - Seek to specific time in video
34. widget_currentvideotime - Get current video playback time
35. widget_setyoutubevolume - Set video volume
36. widget_setyoutubeplaybackspeedratio - Set video playback speed
37. widget_whenvideotimeis - Event when video reaches specific time
38. widget_whenvideoispaused - Event when video is paused
39. widget_whenvideoisstopped - Event when video is stopped
40. widget_whenvideostart - Event when video starts

### Camera Widgets
41. widget_showcamera - Display camera feed widget
42. widget_savepicturefromcamera - Save camera snapshot as costume

### Image Widgets
43. widget_addimagefromcostumes - Add image widget from costume
44. widget_addimagefromurl - Add image widget from URL
45. widget_addimage - Add small image to existing widget
46. widget_addimageurl - Add image from URL to existing widget

### Advanced Widgets
47. widget_addtoolbox - Add grid-based icon selector (like Minecraft toolbox)
48. widget_seticontotoolbox - Set icon in toolbox cell
49. widget_addlink - Add clickable hyperlink widget
50. widget_addmenubar - Add application-style menu bar
51. widget_addmenugroup - Add menu group to menu bar
52. widget_addmenuitem - Add menu item to menu group
53. widget_confirmtextwithbuttons - Create modal confirmation dialog
54. widget_releasefocus - Release focus from widget

### Tab Widgets
55. widget_createtabs - Create tabbed interface
56. widget_settabcontainer - Set which tab widgets appear in
57. widget_selecttab - Switch to specific tab programmatically
58. widget_showhideaddremove - Manage individual tabs
59. widget_whentabselected - Event when user selects tab

### Chat & Communication
60. widget_addchatwindow - Add chat interface widget
61. widget_appendtochat - Add message to chat
62. widget_updatelastchatmessage - Update most recent chat message

### Layout System
63. widget_applylayoutrow - Create responsive layout with rows and cells
64. widget_clearlayout - Clear applied layout

### Progress & Status
65. widget_addprogressbar - Add progress bar widget

### Navigation
66. widget_openurl - Open URL in new browser tab
67. widget_runproject - Navigate to another CreatiCode project

### Widget State
68. widget_disablewidget - Disable widget interaction
69. widget_enablewidget - Enable widget interaction

### Charts & Visualization
70. widget_drawchart - Draw bar/line/pie/percentage charts from lists
71. widget_drawchartfromtable - Draw charts from table data

