# T16 – User Interfaces: K–8 Skill List (Draft v1)

Topic reference: `T16 User Interfaces` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, ALG‑HD (with links to PRO‑PM, PRO‑DH)

Each skill below has:

- a stable **ID** (`T16.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

In Kindergarten, students encounter UI elements in everyday apps and games but do not build interfaces themselves. Focus is on recognizing buttons, menus, and simple interactions.

### T16.GK.01 – Spot buttons and menus in a picture

- **Short name:** Identify buttons in an interface (pictures)
- **Description:** Students recognize familiar UI elements—buttons, menus, text labels—in simple pictures of apps or games. They distinguish a button from non-interactive elements (e.g., decorative icons, plain text) and describe what each element does (e.g., "This button makes the sound go louder").
- **Challenge format:** Concept, multiple choice with images. Show a simple screenshot or drawing of an app interface; students select which element is the "play button" or "menu" or "volume slider" from choices. Auto‑grading checks the selected element.
- **CSTA:** EK‑ALG‑HD‑02 (Identify ways that technology might help others – recognizing interface design).

### T16.GK.02 – Follow on‑screen buttons in a story

- **Short name:** Click buttons to play a story
- **Description:** Students interact with a simple CreatiCode project where buttons trigger story animations or sounds. They learn that clicking a button causes something to happen and understand the cause‑effect relationship in an interactive interface.
- **Challenge format:** Concept, interactive experience. A CreatiCode project plays a short story and offers 2–3 large, clearly labeled buttons (e.g., "Next Scene," "Play Sound," "Restart"). Students click to advance. Auto‑grading tracks button clicks and story progression.
- **CSTA:** EK‑PRO‑PF‑02 (Create programs that include a sequence to complete a task).

### T16.GK.03 – Describe what a label tells you

- **Short name:** Read labels in a game or app
- **Description:** Students look at text labels, icons, and simple labels in an interface and understand what information they convey (e.g., a "Score: 5" label tells you how many points you have; a "Lives: 3" label tells you how many chances you have left).
- **Challenge format:** Concept, multiple choice or matching. Show a screenshot with labeled elements; ask "What does this label tell you?" or match labels to what they represent. Auto‑grading checks answers.
- **CSTA:** EK‑ALG‑HD‑02.

---

## Grade 1

Grade 1 students begin creating simple interfaces with buttons and labels in CreatiCode projects. They learn that buttons can be placed on screen and connected to scripts.

### T16.G1.01 – Add a button to a sprite project

- **Short name:** Place a button on the stage
- **Description:** Students use CreatiCode's button widget block to add a button to the stage. They specify the button's label (text) and position. This is an early step toward understanding widgets as distinct from sprites.
- **Challenge format:** Coding, starter project. Provided: a sprite and an empty stage. Prompt: "Add a button that says 'Jump' near the bottom left." Students use the "add button" block and adjust position using the positioning tool. Auto‑grading checks for the presence of a button with the correct label in approximately the right location.
- **CSTA:** E1‑PRO‑PF‑01.

### T16.G1.02 – Connect a button to a simple action

- **Short name:** Make a button do something
- **Description:** Students create a script where clicking a button triggers a simple action (e.g., sprite jumps, plays a sound, changes color). They use a "when button clicked" event block linked to one or more action blocks.
- **Challenge format:** Coding, starter project. Provided: a sprite and a button already placed. Prompt: "When the button is clicked, make the sprite say 'Hello!'." Students connect a "when [button] clicked" event to "say [Hello!] for 2 seconds." Auto‑grading verifies the event block and at least one action block are connected correctly.
- **CSTA:** E1‑PRO‑PF‑01.

### T16.G1.03 – Match buttons to their effects in code

- **Short name:** Choose the button event for an action
- **Description:** Students read a short script with an action (e.g., "say 'Good job!'") and select which event block (button clicked vs key pressed vs green flag) would trigger it based on a scenario (e.g., "I want it to happen when the user clicks the button").
- **Challenge format:** Concept, multiple choice. Present a script with an action block visible and three event block options; students choose the correct event. Auto‑grading compares selection to the correct answer.
- **CSTA:** E1‑PRO‑PF‑01, E1‑ALG‑HD‑02.

### T16.G1.04 – Design a simple menu with labels

- **Short name:** Create a label that gives instructions
- **Description:** Students add a label widget to the stage to display instructions or information (e.g., "Click a button to pick a color" or "Score: 0"). This reinforces that labels are used to communicate with the user.
- **Challenge format:** Coding, starter project. Prompt: "Add a label that says 'Choose a level:' above three buttons." Students use the "add label" block and position it. Auto‑grading checks for a label with the correct text in an appropriate location above buttons.
- **CSTA:** E1‑PRO‑PF‑01, E1‑ALG‑HD‑02.

---

## Grade 2

Grade 2 students build interactive projects with multiple buttons and labels, and learn to update label text dynamically.

### T16.G2.01 – Create a two‑button game control interface

- **Short name:** Add left and right buttons for movement
- **Description:** Students place two buttons on the stage (e.g., "Move Left" and "Move Right") and write scripts so that clicking each button moves a sprite in the corresponding direction. This combines button events with movement logic.
- **Challenge format:** Coding, starter project. Provided: a sprite in the center of the stage and a template with two empty button placeholders. Students create two buttons and connect each to a movement block. Auto‑grading checks for two distinct buttons and correct movement direction when each is clicked.
- **CSTA:** E2‑PRO‑PF‑01.

### T16.G2.02 – Update a score label when an event happens

- **Short name:** Change a label's text with a variable
- **Description:** Students create a variable (e.g., `score`) and use blocks to change the label's text to display the variable's current value. For example, when a sprite touches a coin, the score increases and the label updates to show "Score: 5."
- **Challenge format:** Coding, starter project with a label and a variable. Prompt: "When the sprite touches a coin, increase the score and update the label to show the new score." Students add a "set [label] text to" block inside an "if touching" condition and reference the score variable. Auto‑grading simulates touches and checks that the label text updates correctly.
- **CSTA:** E2‑PRO‑PF‑01, E2‑PRO‑DH‑02.

### T16.G2.03 – Position buttons without overlapping

- **Short name:** Arrange multiple buttons on screen
- **Description:** Students place three or more buttons on the stage in a logical layout (e.g., a row at the bottom, or a column on the right) without overlapping each other or the main game/sprite area. They use the positioning tool to fine‑tune placement.
- **Challenge format:** Coding, starter project. Prompt: "Add three buttons labeled 'Red,' 'Green,' and 'Blue' in a row at the bottom of the screen. Make sure they don't overlap." Students use the positioning tool to place and resize buttons. Auto‑grading checks that buttons are placed below a certain Y position and do not overlap (by checking bounding boxes).
- **CSTA:** E2‑ALG‑HD‑02.

### T16.G2.04 – Create an instructions label that hides when play starts

- **Short name:** Show and hide UI elements
- **Description:** Students place an instructions label at the start of the project and learn to hide it (or show it) using "hide [widget]" and "show [widget]" blocks. For example, showing instructions before play and hiding them once the game begins.
- **Challenge format:** Coding, starter project. Provided: an instructions label. Prompt: "Hide the instructions label when the green flag is clicked, then show it again if the user clicks a 'Help' button." Students add "hide [label]" in the green flag script and "show [label]" in the help button's event. Auto‑grading checks that the label is hidden after green flag and shown after clicking help.
- **CSTA:** E2‑PRO‑PF‑01.

---

## Grade 3

Grade 3 students create more complex interfaces with multiple widgets and logic, including responding to button clicks with conditionals and state changes.

### T16.G3.01 – Create a start/stop button interface

- **Short name:** Button to start and stop a game
- **Description:** Students design a simple state machine where clicking a "Start" button begins a game loop (sprite moves, score counts) and clicking a "Stop" button ends it. They learn to use a variable to track game state.
- **Challenge format:** Coding, starter project. Provided: a sprite and two button placeholders. Students create a "game\_running" variable (true/false), and set up button event handlers to toggle it. Auto‑grading verifies that the game starts/stops when buttons are clicked and the variable toggles correctly.
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑HD‑02.

### T16.G3.02 – Use a label to display changing information

- **Short name:** Display timer or status on a label
- **Description:** Students create a label that continuously updates to show dynamic information (e.g., a timer counting down, the current level, or the player's name input). The label text changes based on a variable or computation.
- **Challenge format:** Coding, starter project with a timer variable. Prompt: "Display the countdown timer on a label. Each second, decrease the timer and update the label." Students use a loop with a "set [label] text to [timer]" block. Auto‑grading simulates the timer and checks that the label updates with the correct values.
- **CSTA:** E3‑PRO‑PF‑01.

### T16.G3.03 – Add a button to reset or restart the game

- **Short name:** Reset button that clears the game state
- **Description:** Students add a "Reset" button that, when clicked, clears variables (e.g., sets score to 0, returns sprite to start position), updates all relevant labels, and prepares the game to be played again.
- **Challenge format:** Coding, refactor challenge. Provided: a simple game with score and sprites. Students add a reset button and write the event handler to reset all variables and labels. Auto‑grading clicks the reset button and checks that score is 0, sprite is at the starting position, and labels show initial values.
- **CSTA:** E3‑PRO‑PF‑01.

### T16.G3.04 – Create a menu with button options

- **Short name:** Build a main menu with multiple choices
- **Description:** Students design a menu screen with multiple buttons (e.g., "Play Game," "Instructions," "Quit") and labels, and connect each button to a different scene or action. This introduces the concept of navigation in an interface.
- **Challenge format:** Coding, creative project. Prompt: "Create a start menu with at least three buttons. When 'Play' is clicked, start the game. When 'Instructions' is clicked, show instructions on a label." Students build the menu and implement navigation. Auto‑grading checks that buttons are labeled correctly and that clicking them triggers the expected actions (or scene changes).
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑HD‑02.

---

## Grade 4

Grade 4 students design more sophisticated interfaces with multiple states, input validation, and user feedback through widgets.

### T16.G4.01 – Add a text input widget and use the entered text

- **Short name:** Get player name from a text box
- **Description:** Students add a text input widget (also called a text box or input field) and use blocks to read the text the user types. For example, "Ask the player for their name and then display 'Welcome, [name]!' on a label."
- **Challenge format:** Coding, starter project. Provided: a text input widget placeholder and a label. Prompt: "Add a text input so the user can type their name. When they click 'Submit,' display a welcome message with their name." Students read from the text input using a reporter block (e.g., `[text input] text`). Auto‑grading simulates text entry and checks that the label displays the correct personalized message.
- **CSTA:** E4‑PRO‑PF‑01, E4‑PRO‑DH‑02.

### T16.G4.02 – Validate input and provide feedback

- **Short name:** Check that input is valid and show an error
- **Description:** Students use conditionals to validate user input (e.g., "Check if the name field is empty; if so, show an error message") and provide user feedback via a label. This builds understanding of error handling in user interfaces.
- **Challenge format:** Coding, starter project with a text input and a feedback label. Prompt: "If the name field is empty, display 'Please enter a name' in red. If the name is valid, display 'Good!' in green." Students add an `if`/`else` block to check input and update a label's text and color. Auto‑grading tests empty input and valid input scenarios.
- **CSTA:** E4‑PRO‑PF‑01, E4‑PRO‑TR‑03.

### T16.G4.03 – Create a dropdown menu widget

- **Short name:** Use a dropdown to select from options
- **Description:** Students add a dropdown widget that displays a list of choices (e.g., "Easy," "Medium," "Hard") and use a block to read the selected option. They might use the selection to set a game difficulty or change colors.
- **Challenge format:** Coding, starter project. Prompt: "Add a dropdown with three difficulty levels. When the player selects a level and clicks 'Start,' display the selected level on a label." Students add a dropdown, read its value using a reporter, and display it. Auto‑grading selects different options and verifies that the label displays the correct choice.
- **CSTA:** E4‑PRO‑PF‑01, E4‑PRO‑DH‑02.

### T16.G4.04 – Build a settings panel with multiple controls

- **Short name:** Design a settings menu with buttons and sliders
- **Description:** Students create a settings or options screen with multiple widgets (buttons, labels, sliders, dropdowns) to control game features (e.g., volume, difficulty, graphics quality). They learn to organize widgets logically and respond to changes.
- **Challenge format:** Coding, creative project. Prompt: "Create a settings screen with a volume slider, a difficulty dropdown, and an 'Apply' button. When Apply is clicked, update the game's settings." Students lay out multiple widgets and implement handlers for each. Auto‑grading checks widget placement, responsiveness to interaction, and variable updates.
- **CSTA:** E4‑PRO‑PF‑01, E4‑ALG‑HD‑02.

---

## Grade 5

Grade 5 students design complete interfaces for apps and games with multiple screens, persistent data in labels, and thoughtful UX design.

### T16.G5.01 – Create a multi‑screen app with a navigation interface

- **Short name:** Switch between screens using buttons
- **Description:** Students build an app with multiple screens (e.g., home screen, game screen, results screen) and use buttons and labels to navigate between them. They manage widget visibility to show/hide different screens.
- **Challenge format:** Coding, creative project. Prompt: "Build a three-screen app: a home menu, a game, and a results screen. Use buttons to navigate between them. Only show the widgets for the current screen." Students organize widgets into groups (e.g., home buttons, game buttons, result labels) and toggle visibility. Auto‑grading verifies that clicking buttons switches screens correctly and only the current screen's widgets are visible.
- **CSTA:** E5‑PRO‑PF‑01, E5‑ALG‑HD‑02.

### T16.G5.02 – Design a form with multiple inputs and validation

- **Short name:** Build a form with error checking
- **Description:** Students create a form interface with multiple text input fields, dropdowns, or checkboxes, validate all inputs for completeness and correctness, and display a summary or confirmation message. This teaches form design and validation patterns.
- **Challenge format:** Coding, guided project. Prompt: "Create a registration form with fields for name, age, and email. Check that name is not empty, age is a number, and email contains an '@'. If all valid, show a confirmation message." Students add multiple input widgets, validation logic, and a confirmation label. Auto‑grading tests valid and invalid input scenarios.
- **CSTA:** E5‑PRO‑PF‑01, E5‑PRO‑DH‑02.

### T16.G5.03 – Build a leaderboard or high‑score display

- **Short name:** Display a sorted list of high scores
- **Description:** Students create a label or series of labels that display high scores or player rankings. They use lists or variables to store scores and update the display dynamically. This introduces the concept of showing structured data in a UI.
- **Challenge format:** Coding, starter project with a list of scores. Prompt: "Display the top 3 high scores on the screen in a nice format (e.g., '1st: 500 points' on separate labels). Update them when the game ends with a new high score." Students loop through a score list, format the display, and update labels. Auto‑grading checks that scores are displayed correctly after each game round.
- **CSTA:** E5‑PRO‑PF‑01, E5‑PRO‑DH‑02.

### T16.G5.04 – Implement a responsive HUD that reacts to game state

- **Short name:** Create a heads-up display (HUD) that changes with the game
- **Description:** Students design a "heads-up display" (HUD)—on-screen UI elements that show real-time game information (health bar, ammo count, mini-map indicator, status text). The HUD updates dynamically as game variables change.
- **Challenge format:** Coding, creative project. Prompt: "Build a game HUD with labels for health (0–100), ammo (0–30), and a 'WARNING' label that appears when health drops below 20. Update all values in real time as the player plays." Students add labels and conditionally show/hide or update them based on variables. Auto‑grading simulates game events and checks that the HUD displays and updates correctly.
- **CSTA:** E5‑PRO‑PF‑01, E5‑ALG‑HD‑02.

---

## Grade 6

In middle school, students apply human-centered design principles to interface design and think critically about usability, accessibility, and user experience.

### T16.G6.01 – Evaluate an interface for usability

- **Short name:** Analyze a UI for clarity and accessibility
- **Description:** Students examine an existing interface (a simple app screenshot) and identify issues or strengths: Are buttons clearly labeled? Is the layout intuitive? Are colors accessible for colorblind users? They learn to think like a UX designer and consider diverse users.
- **Challenge format:** Concept, analysis and short response. Show a screenshot of a simple game or app interface; students answer questions: "What does this button do?" "Is the layout clear?" "How could you make this more accessible?" Auto‑grading uses keyword matching or rubric scoring for responses.
- **CSTA:** MS‑ALG‑HD‑03 (Design algorithms using human-centered design principles like empathy and accessibility), MS‑PRO‑TR‑12 (Modify a program to improve usability and accessibility).

### T16.G6.02 – Design an interface based on user feedback

- **Short name:** Improve an interface using user testing
- **Description:** Students design an initial interface (buttons, labels, layout), ask peers or a teacher to try it, gather feedback on usability, and then modify the design to address the feedback. This introduces the iterative design process.
- **Challenge format:** Coding, iterative design project. Students first build a simple game or app interface, then conduct a brief user test with one or two peers (e.g., "Can you find the play button?" "Is the score easy to read?"), document feedback, and refine the interface. Auto‑grading evaluates the refinement based on a rubric that includes evidence of feedback incorporation.
- **CSTA:** MS‑ALG‑HD‑04 (Refine algorithms iteratively through user feedback to improve usability and accessibility).

### T16.G6.03 – Use color and contrast to improve readability

- **Short name:** Choose colors that are easy to read
- **Description:** Students apply color theory to interface design: choosing high-contrast text and backgrounds for readability, avoiding color combinations that are difficult for colorblind users, and using color to highlight important elements (e.g., a red button for "Stop").
- **Challenge format:** Coding, design challenge. Prompt: "Create a game interface where the score label uses high-contrast colors (e.g., white text on dark background). Make sure a 'Stop' button is red and stands out." Students add labels and buttons with specific color properties. Auto‑grading checks color properties (background and text colors) for sufficient contrast using a contrast ratio calculation.
- **CSTA:** MS‑ALG‑HD‑03, MS‑PRO‑TR‑12.

### T16.G6.04 – Create an interface that works on different screen sizes

- **Short name:** Design a responsive UI layout
- **Description:** Students learn that interfaces may be viewed on different devices (tablets, phones, computers) and adjust their layouts to be flexible. They position buttons and labels using percentages or relative sizing rather than fixed positions.
- **Challenge format:** Coding, design and testing project. Students design an interface using relative positioning or percentage-based sizing. The system then simulates the layout on different screen dimensions (e.g., 800x600, 1920x1080, mobile). Auto‑grading checks that widgets remain visible and well-positioned across simulated screen sizes.
- **CSTA:** MS‑ALG‑HD‑03, MS‑PRO‑TR‑12.

---

## Grade 7

Grade 7 students design complex interfaces for applications, including data input/output, dynamic content, and user-centered refinement.

### T16.G7.01 – Build a data collection interface (survey or questionnaire)

- **Short name:** Create a survey form with multiple input types
- **Description:** Students design an interface for a survey or questionnaire with text inputs, dropdowns, checkboxes, or radio buttons; validate responses; and collect the data. They learn how interfaces are used to gather information.
- **Challenge format:** Coding, creative project. Prompt: "Create a survey about favorite sports with text input for name, dropdowns for age range, checkboxes for sports interests, and a submit button. When submitted, display a summary of responses." Students design the form, implement validation, and show a result. Auto‑grading tests that all input types work and data is collected correctly.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑HD‑03.

### T16.G7.02 – Implement a search or filter interface

- **Short name:** Search or filter a list using a text input
- **Description:** Students create a text input field where users can type a query, and the interface filters or searches a list of items (e.g., a player inventory, a menu of options) to show only matching results. This is a real-world UI pattern.
- **Challenge format:** Coding, starter project with a list of items (stored in a variable or list). Prompt: "Add a search box. As the user types, filter the list to show only items that contain the search text. Update labels or sprites to display results." Students use string matching and conditional logic. Auto‑grading simulates typing and checks that the correct items are displayed.
- **CSTA:** MS‑PRO‑PF‑01.

### T16.G7.03 – Design an accessible interface for users with different abilities

- **Short name:** Make a UI accessible for all players
- **Description:** Students consider accessibility needs (e.g., text size for low vision, keyboard controls for mobility challenges, colorblind-friendly palettes) and redesign an interface to accommodate multiple ability types. They learn to design inclusively from the start.
- **Challenge format:** Coding and concept, design challenge. Prompt: "Redesign your game interface to be accessible to a player with low vision: make buttons larger, use high-contrast colors, and make button text bigger. Also, add keyboard shortcuts as an alternative to mouse clicks." Students modify widget sizes, colors, and add keyboard event handlers. Auto‑grading checks property values and the presence of alternative input methods.
- **CSTA:** MS‑ALG‑HD‑03, MS‑PRO‑TR‑12.

### T16.G7.04 – Create a help or tutorial interface

- **Short name:** Build an in-game help system
- **Description:** Students design a help or tutorial interface within a game, including explanatory labels, step-by-step instructions, images/animations, and a "Next" button to guide the player through mechanics or controls.
- **Challenge format:** Coding, creative project. Prompt: "Create a tutorial screen that teaches the player how to play your game. Use labels for explanations, images for diagrams, and 'Next' / 'Back' buttons to move through steps." Students build a multi-step tutorial interface. Auto‑grading verifies that buttons navigate correctly and information is displayed clearly.
- **CSTA:** MS‑ALG‑HD‑03.

---

## Grade 8

Grade 8 students apply advanced UI design patterns, think about scalability and maintainability, and integrate UX with broader algorithmic and data design.

### T16.G8.01 – Design a wizard or step-by-step interface

- **Short name:** Create a multi-step wizard interface
- **Description:** Students build a "wizard" interface that guides users through a multi-step process (e.g., character creation, game setup, checkout) with Previous/Next buttons, progress indicators, and validation at each step. They manage state across multiple screens.
- **Challenge format:** Coding, creative project. Prompt: "Create a character creation wizard with 3 steps: choose name, choose class, choose starting items. Show a progress indicator ('Step 1 of 3'), and validate each step before allowing the user to proceed." Students implement state management (a 'current_step' variable) and conditional visibility of screens. Auto‑grading simulates user navigation and checks state transitions and validation.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑HD‑03.

### T16.G8.02 – Implement dynamic content loading in a UI

- **Short name:** Load and display content based on user choices
- **Description:** Students design an interface where selecting an option dynamically loads and displays related content (e.g., clicking a character name displays their stats, clicking a level number shows the level preview). Content is retrieved from lists or variables.
- **Challenge format:** Coding, starter project with data structures (e.g., a list of character names, a parallel list of stats). Prompt: "When the user clicks a character button, display that character's stats (health, attack, defense) in labels on the right. Update the labels when a different character is clicked." Students use conditionals or list indexing to match choices to data. Auto‑grading simulates multiple clicks and verifies that the correct data is displayed.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑DH‑04.

### T16.G8.03 – Analyze UI design patterns and their effectiveness

- **Short name:** Compare two UI designs for a task
- **Description:** Students examine two different interface designs for the same task (e.g., two layouts for a settings menu, two ways to input a number) and evaluate which is more effective based on clarity, ease of use, and aesthetics. They write a brief analysis.
- **Challenge format:** Concept, analysis and comparison. Present two CreatiCode projects or screenshots with different UI designs for the same task; students select the better design and explain their reasoning using vocabulary like "clarity," "efficiency," "accessibility," and "visual hierarchy." Auto‑grading uses rubric scoring for written explanations.
- **CSTA:** MS‑ALG‑HD‑03.

### T16.G8.04 – Document and refine a UI design based on usability testing

- **Short name:** Test UI with users and iterate
- **Description:** Students conduct user testing of their interface (having peers try to complete a task using their interface, noting where they struggle), document observations, and refactor the interface to resolve usability issues. This reinforces the human-centered design cycle.
- **Challenge format:** Coding and documentation, iterative design project. Students build an interface, conduct a user test with 2–3 peers (e.g., "Can you find the pause button?" "How would you exit to the menu?"), document what was difficult, and then refine the interface. They submit a brief report of issues found and changes made. Auto‑grading evaluates the report and the quality of refinements using a rubric.
- **CSTA:** MS‑ALG‑HD‑04, MS‑PRO‑PM‑16 (Document a program, including complex logic).
