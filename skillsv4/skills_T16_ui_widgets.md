# T16 – User Interfaces: G5–8 Skill List (Draft v2)

Topic reference: `T16 User Interfaces` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, ALG‑HD (with links to PRO‑PM, PRO‑DH)

Each skill below has:

- a stable **ID** (`T16.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** T16 focuses on **screen‑level user interfaces** in projects: visible controls (buttons, sliders, text inputs, dropdowns) and information areas (labels, HUD, forms) that connect humans to game and app behavior. Core interface ideas for K–4 (what makes a design easy to use, where to put information, who a tool helps) live in **T05 Human‑Centered Design** and application topics like **T14/T15** as picture‑based tasks. **T16 is reserved for Grades 5–8**, where students are already building full games and apps and can benefit from explicit widgets/UI patterns. T16 assumes core algorithm and planning foundations from **T01–T04**, user‑needs thinking from **T05**, and project organization skills from **T12**, and turns them into concrete UI patterns in CreatiCode projects (menus, settings panels, forms, HUDs, responsive layouts, accessible interfaces, and multi‑step wizards). T14/T15 provide the game/story content; T16 provides the UI “wrapper” and interaction patterns around that content.

---

## Grade 5

Grade 5 students design complete interfaces for apps and games with multiple screens, persistent data in labels, and thoughtful UX design. They assume prior experience with building games and stories (T14/T15) and shift toward structured **apps** that use widgets and multi‑screen flows.

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

