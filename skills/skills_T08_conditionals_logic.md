# T08 – Conditionals & Logic: K–8 Skill List (Draft v1)

Topic reference: `T08 Conditionals & Logic` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, ALG‑AF (with links to PRO‑TR, DAA‑DI)

Each skill below has:

- a stable **ID** (`T08.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Conditional logic is introduced as an intuitive idea of "if something is true, then do this" using everyday language and pictures, not yet as formal code blocks.

### T08.GK.01 – Recognize if/then in daily routines

- **Short name:** Spot "if then" in real life
- **Description:** Students recognize simple if/then patterns in their daily environment (e.g., "if it rains, then use an umbrella"; "if you're hungry, then eat lunch"). This builds the concept of a condition leading to an action in a concrete, age‑appropriate way.
- **Challenge format:** Concept, multiple choice. Show 3–4 picture scenarios; students identify which one shows a clear cause-and-effect or if/then pattern. Auto‑grading checks the selected scenario.
- **CSTA:** EK‑ALG‑AF‑01 (Identify algorithms in daily activities).

### T08.GK.02 – Classify objects by a simple property

- **Short name:** Sort by one property
- **Description:** Students sort or classify objects (shapes, colors, sizes) by a single property (e.g., "red vs not red", "big vs small"). This teaches the idea of a condition (a yes/no property) without using code.
- **Challenge format:** Concept, interactive sorting. Provide 8–10 picture tiles; students drag them into two piles based on a single criterion (e.g., "has 4 sides" vs "does not have 4 sides"). Auto‑grading checks correct classification.
- **CSTA:** EK‑ALG‑AF‑01.

### T08.GK.03 – Match picture story to if/then statement

- **Short name:** Match story to "if then"
- **Description:** Students match a short picture story (e.g., a child sees rain, puts on a coat) to one of several simple if/then sentences, strengthening the connection between everyday events and conditional logic.
- **Challenge format:** Concept, multiple choice. Show a 2–3 panel picture story and 3 sentence choices (e.g., "If it's sunny, then …" vs "If it rains, then …"). Students pick the matching sentence.
- **CSTA:** EK‑ALG‑AF‑01.

---

## Grade 1

Grade 1 focuses on recognizing conditions and simple if/then logic in code, still without requiring students to construct conditional blocks.

### T08.G1.01 – Find a condition in code

- **Short name:** Spot conditions in a script
- **Description:** Students identify parts of a script that test a condition (e.g., blocks saying "touching color?", "key pressed?") and understand that they check whether something is true.
- **Challenge format:** Concept, multiple choice or highlighting. A simple script with one or two conditions is shown; students click on or choose which block "asks if something is true". Auto‑grading checks the selected block.
- **CSTA:** E1‑PRO‑PF‑01.

### T08.G1.02 – Predict the outcome of a simple if statement

- **Short name:** What happens if the condition is true?
- **Description:** Given a simple if statement and a scenario (e.g., "if key pressed, say 'Hello'"), students predict whether the action will happen. This builds understanding of how conditions control behavior.
- **Challenge format:** Concept, multiple choice or true/false. A script shows an `if key pressed then say 'hello'` block; students are told "The user presses the key" or "The user does not press the key" and choose what happens next. Auto‑grading checks the prediction.
- **CSTA:** E1‑PRO‑PF‑01.

### T08.G1.03 – Match a decision picture to code

- **Short name:** Match decision picture to code
- **Description:** Students match a simple picture showing a choice or decision (e.g., "Is it raining? Yes go inside / No go outside") to a code snippet with an if structure.
- **Challenge format:** Concept, multiple choice. Show a decision picture and three tiny code snippets; only one uses an `if` statement that matches the picture logic. Students pick the correct code.
- **CSTA:** E1‑ALG‑AF‑01, E1‑PRO‑PF‑01.

### T08.G1.04 – Build a simple if statement (no events yet)

- **Short name:** Create an if block script
- **Description:** Students build a short script using a basic `if` block that checks a condition and performs an action if true, without nesting or events. This solidifies the if structure as "check, then do".
- **Challenge format:** Coding, starter project. Provided: a sprite and a condition block (e.g., `if <touching color?>`). Prompt: "If the sprite touches red, make it say 'Ouch!'" Students place an action block inside the if statement. Auto‑grading checks structure and behavior.
- **CSTA:** E1‑PRO‑PF‑01.

---

## Grade 2

Grade 2 is when students are first expected to write code with if/else blocks and begin understanding simple conditional logic in programs.

### T08.G2.01 – Refactor duplicate code into if/else

- **Short name:** Use if/else instead of repeated scripts
- **Description:** Students take a script with two separate sequential actions and refactor it into one if/else block, reducing duplication. For example, changing "if key A then move left; if key B then move right" into "if key A then move left else move right".
- **Challenge format:** Coding, refactor in CreatiCode. Starter script has two separate branches; students replace them with a single if/else. Auto‑grading checks (1) correct if/else structure, (2) removal of duplicate code, and (3) behavior equivalence.
- **CSTA:** E2‑PRO‑PF‑01, E2‑ALG‑AF‑01.

### T08.G2.02 – Use if to respond to keyboard input

- **Short name:** Make sprite respond to a key press
- **Description:** Students create a script where pressing a specific key triggers an action (e.g., "if key up-arrow pressed, move up"). This combines if with event-driven logic in a game-like context.
- **Challenge format:** Coding, guided construction. Starter project includes a sprite and empty `if <key pressed?>` blocks. Prompt specifies which key and action (e.g., "If space is pressed, make the sprite jump"). Auto‑grading checks (1) correct condition, (2) correct key, and (3) action happens only when key is pressed.
- **CSTA:** E2‑PRO‑PF‑01.

### T08.G2.03 – Use if to detect sprite touching color or sprite

- **Short name:** If sprite touches something, do an action
- **Description:** Students write an if statement that checks whether a sprite is touching a color or another sprite, and respond accordingly (e.g., "if touching coin, change score"). This extends conditional logic to spatial/collision awareness.
- **Challenge format:** Coding, starter project. Provided: a moving sprite and a target (coin, wall, or colored area). Students add an `if <touching?>` block to detect collision and respond (change costume, disappear, add score, or bounce). Auto‑grading checks condition type and action behavior.
- **CSTA:** E2‑PRO‑PF‑01.

### T08.G2.04 – Predict outcome of if/else from code

- **Short name:** Read if/else code and predict result
- **Description:** Students read a simple if/else block and determine what action will happen given a specific condition state (true or false). This develops code-reading and logical reasoning skills.
- **Challenge format:** Concept, code‑reading item. Show simple if/else code (e.g., `if <score > 10> then say 'win' else say 'try again'`) and state whether the condition is true or false; students choose the correct output or action. Auto‑grading compares to simulation.
- **CSTA:** E2‑PRO‑PF‑01.

---

## Grade 3

Grade 3 introduces compound conditions, nested conditionals, and more complex logic patterns.

### T08.G3.01 – Use if/else in a game or interaction loop

- **Short name:** if/else for game logic
- **Description:** Students use if/else blocks inside a `forever` loop to check conditions repeatedly (e.g., "forever: if key pressed move, if touching wall bounce"). This combines loops and conditionals in a game context.
- **Challenge format:** Coding, starter project. Provided: a sprite and a partial loop with one if/else inside. Students complete the logic for a simple game (e.g., "move if key pressed, bounce if touching edge"). Auto‑grading checks loop structure, condition accuracy, and behavior over multiple iterations.
- **CSTA:** E3‑PRO‑PF‑01.

### T08.G3.02 – Combine two conditions with AND

- **Short name:** Use AND to combine conditions
- **Description:** Students use a compound condition (AND) to check if two things are true at the same time before acting (e.g., "if key pressed AND touching goal, then complete level"). This introduces boolean logic operators.
- **Challenge format:** Coding, starter project. Provided: blocks for two separate conditions. Prompt: "Complete this challenge only if you touch the goal AND collect all coins." Students combine the conditions with AND. Auto‑grading checks correct use of AND operator and behavior.
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑AF‑01.

### T08.G3.03 – Combine two conditions with OR

- **Short name:** Use OR to combine conditions
- **Description:** Students use OR to check if at least one of two conditions is true (e.g., "if score > 100 OR lives == 0, then end game"). This teaches alternative logic pathways.
- **Challenge format:** Coding, starter project. Prompt: "End the game if the score is high enough OR if lives run out." Students write or complete an if statement with OR. Auto‑grading verifies correct OR logic and behavior in test cases.
- **CSTA:** E3‑PRO‑PF‑01.

### T08.G3.04 – Trace code with conditionals and predict result

- **Short name:** Trace if/else/AND/OR code
- **Description:** Students read code with one or more if/else blocks (including compound conditions) and trace the execution path to predict the final outcome or which branch is taken.
- **Challenge format:** Concept, code‑tracing item. Show code with if/else, possibly including AND/OR; give input values; ask "Which message will be displayed?" or "What is the final value?" Auto‑grading checks correctness via simulation.
- **CSTA:** E3‑ALG‑AF‑01, E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 deepens conditional logic with nested if/else, more complex boolean expressions, and conditional refactoring.

### T08.G4.01 – Nest if/else statements

- **Short name:** Use nested if/else for layered decisions
- **Description:** Students write nested if/else blocks where an else branch contains another if (e.g., checking weapon type, then checking ammo level). This models multi-step decision-making.
- **Challenge format:** Coding, starter project. Prompt: "If the player presses a button, check what weapon they have. If it's a gun, check if there's ammo. If yes, shoot; if no, say 'no ammo'." Students build the nested structure. Auto‑grading verifies correct nesting and behavior across scenarios.
- **CSTA:** E4‑PRO‑PF‑01.

### T08.G4.02 – Convert nested if to cleaner logic

- **Short name:** Simplify nested if/else
- **Description:** Students are given deeply nested or redundant if/else code and refactor it using AND, OR, or else-if to make it cleaner and more readable.
- **Challenge format:** Coding, refactor challenge. Starter project contains nested if statements (e.g., 3+ levels). Students rewrite using compound conditions or else-if chains. Auto‑grading checks code structure (cleaner/flatter) and behavior equivalence.
- **CSTA:** E4‑PRO‑PF‑01, PRO‑TR.

### T08.G4.03 – Use if to control state changes

- **Short name:** Use conditions to manage state
- **Description:** Students use conditional logic to manage game states (e.g., "if game over then don't allow movement") or animation states (e.g., "if jumping then use jump costume"). This applies conditionals to tracking program state.
- **Challenge format:** Coding, starter project. Provided: a game or animation with a state variable (e.g., `is_jumping`, `game_over`). Students add if checks to prevent or trigger actions based on state. Auto‑grading verifies state management via behavior tests.
- **CSTA:** E4‑PRO‑PF‑01.

### T08.G4.04 – Analyze and fix a logic bug

- **Short name:** Find and fix conditional bugs
- **Description:** Students debug a script where a condition is incorrect or inverted (e.g., `if score < 10` instead of `if score >= 10`), causing unexpected behavior. They identify and fix the logic error.
- **Challenge format:** Coding, debugging. A starter project shows expected behavior (e.g., "when score reaches 10, win the game"), but the conditional is wrong. Students adjust the condition or operator. Auto‑grading checks behavior against the expected outcome.
- **CSTA:** E4‑PRO‑TR‑01.

---

## Grade 5

Grade 5 uses conditional logic in data-driven and algorithmic contexts, including simple pattern matching and data-based decisions.

### T08.G5.01 – Write conditionals for a simple game with multiple rules

- **Short name:** Multi-rule game logic
- **Description:** Students implement a game with several interrelated conditional rules (e.g., "if score > 50 and lives > 0, keep playing; if lives == 0, game over; if score > 100, win"). This combines multiple conditions in a cohesive system.
- **Challenge format:** Coding, starter project. Provided: game infrastructure (score, lives tracking). Prompt specifies 3–4 rules; students code the if/else-if chains or compound conditions. Auto‑grading runs scenarios and checks all rule outcomes.
- **CSTA:** E5‑PRO‑PF‑01.

### T08.G5.02 – Use conditionals to filter or categorize data in a list

- **Short name:** Filter data with conditions
- **Description:** Students use if statements in a loop to go through a list and select or act on items matching a condition (e.g., "for each score in scores, if score > 90, add to high_scores").
- **Challenge format:** Coding, starter project with a list of data (scores, names, colors). Prompt: "Find all scores above 85" or "Find the first player named 'Alex'." Students write a loop with an if condition inside. Auto‑grading checks the filtered result set.
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DP.

### T08.G5.03 – Implement conditional logic in a simulation or interactive story

- **Short name:** Conditionals for branching story or simulation
- **Description:** Students use if/else to create branching paths in a story or to control simulation behavior based on parameters (e.g., "if temperature > 80, speed up animation", "if player chooses door A, show scene A").
- **Challenge format:** Coding, creative project with auto‑checks. Provided: a story or simulation template; students add if/else blocks that respond to choices, variables, or conditions. Auto‑grading verifies reachable branches and correct behavior paths.
- **CSTA:** E5‑PRO‑PF‑01, ALG‑AF.

### T08.G5.04 – Write NOT (negation) conditions and evaluate complex boolean expressions

- **Short name:** Use NOT and complex boolean logic
- **Description:** Students use the NOT operator to invert conditions (e.g., "if NOT touching goal") and write more sophisticated boolean expressions combining AND, OR, and NOT to express nuanced logic.
- **Challenge format:** Coding, mixed concept and coding. Items ask students to write or choose conditions such as "if NOT (lives == 0)" or "if (speed > 5) AND (NOT on ground)" from word descriptions. Auto‑grading checks correctness of boolean expression and behavior.
- **CSTA:** E5‑PRO‑PF‑01, ALG‑AF.

---

## Grade 6

In middle school, conditional logic is used for algorithm design and analyzing more complex code; students reason about truthiness and decision paths.

### T08.G6.01 – Trace complex conditionals with variables and operators

- **Short name:** Trace conditionals with variables
- **Description:** Students analyze code with multiple if/else blocks, compound conditions (AND, OR, NOT), and variable updates, predicting final states and which branch executes.
- **Challenge format:** Concept, code‑reading item. Show code with several if/else branches that depend on variables (e.g., age, score, time); give starting values; ask "Which message prints?" or "What is the final state?" Auto‑grading uses static analysis or simulation.
- **CSTA:** MS‑PRO‑PF‑01.

### T08.G6.02 – Refactor long if/else chains into cleaner structures

- **Short name:** Clean up long if/else chains
- **Description:** Students are given code with many sequential if statements (or deeply nested else-if) and refactor it using compound conditions or lookup tables to improve readability and maintainability.
- **Challenge format:** Coding, refactor challenge. Starter code has 5+ if/else branches checking similar conditions. Students rewrite using AND, OR, or a switch-like structure. Auto‑grading checks structure (reduced duplication, clearer logic) and behavior.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T08.G6.03 – Use conditionals in a search or decision algorithm

- **Short name:** Conditionals in search/decision algorithms
- **Description:** Students implement a simple algorithm (e.g., linear search, finding max/min, classification) that relies on if statements to compare values and make decisions based on data.
- **Challenge format:** Coding, starter project with a list or dataset. Prompt: "Find the first score > 90" or "Classify each number as even or odd." Students write loops with conditionals to solve. Auto‑grading checks correctness on multiple test cases.
- **CSTA:** MS‑PRO‑PF‑01, ALG‑AF.

### T08.G6.04 – Explain and justify conditional choices for a task

- **Short name:** Justify conditional design decisions
- **Description:** Students analyze given conditional logic (several possible implementations) and explain which is better and why, using criteria like clarity, efficiency, and correctness.
- **Challenge format:** Concept, explanation plus selection. Items present two implementations of the same logic (e.g., using nested if vs compound conditions); students choose the better one and explain via sentence stems or structured responses. Auto‑grading scores choice and key reasoning phrases.
- **CSTA:** MS‑ALG‑AF‑02, MS‑PRO‑PF‑01.

---

## Grade 7

Grade 7 emphasizes conditional logic in algorithm design, state machines, and handling edge cases.

### T08.G7.01 – Use conditionals to implement a state machine

- **Short name:** Conditionals for state transitions
- **Description:** Students use if/else blocks to track and transition between program states (e.g., menu → playing → game over → restart). They understand how conditionals drive state changes.
- **Challenge format:** Coding, starter project with a state variable. Prompt: "When the game starts, set state to 'playing'. If score reaches the goal, set state to 'won'. If lives == 0, set state to 'lost'." Students implement state transitions with conditionals. Auto‑grading checks state variable updates and transitions.
- **CSTA:** MS‑PRO‑PF‑01, ALG‑AF.

### T08.G7.02 – Handle edge cases and boundary conditions

- **Short name:** Test and handle boundary cases
- **Description:** Students write conditionals that handle boundary and edge cases (e.g., "if score == 0", "if x < 0 or x > screen_width"), preventing bugs or unexpected behavior.
- **Challenge format:** Coding, debugging and design. Starter project has a game or simulation that fails at boundaries. Students add if conditions to prevent wrapping, division by zero, or out-of-bounds issues. Auto‑grading tests edge cases and confirms the fix.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T08.G7.03 – Write conditionals for pattern recognition or rule-checking

- **Short name:** Conditionals for pattern matching
- **Description:** Students use if statements to detect patterns or check membership (e.g., "if this word is in my list of banned words", "if the sequence is ascending"). This applies conditionals to data validation and pattern detection.
- **Challenge format:** Coding, starter project with a list or sequence. Prompt: "Detect if the input matches a known pattern" or "Check if a word is misspelled by comparing to a word list." Students write conditionals to identify or classify. Auto‑grading checks detection accuracy on diverse inputs.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T08.G7.04 – Analyze and compare conditional logic approaches

- **Short name:** Compare conditional implementations
- **Description:** Students compare two different conditional implementations of the same algorithm (e.g., using nested if vs a switch-like structure) and reason about clarity, efficiency, and maintainability.
- **Challenge format:** Concept, multiple choice with explanation. Present two implementations and ask "Which is clearer for future maintainers?" or "Which is less error-prone?" Students choose and justify using computational thinking language. Auto‑grading scores correctness and reasoning quality.
- **CSTA:** MS‑ALG‑AF‑02, MS‑PRO‑PF‑01.

---

## Grade 8

Grade 8 builds toward high school by using conditional logic in complex simulations, games, and data-driven decision-making.

### T08.G8.01 – Implement multi-stage game or simulation logic

- **Short name:** Complex game state and rules
- **Description:** Students design conditional logic for a multi-stage game or simulation (e.g., tutorial → levels 1-3 → boss battle → game over, each with different rule sets). They manage transitions and state-specific behavior.
- **Challenge format:** Coding, substantial starter project. Provided: a game structure with multiple states and scene transitions. Students implement conditionals for stage progression, win/loss conditions, and difficulty changes. Auto‑grading runs through scenarios and verifies all state transitions and rules.
- **CSTA:** MS‑PRO‑PF‑01, ALG‑AF.

### T08.G8.02 – Use conditionals to validate and sanitize input data

- **Short name:** Input validation with conditionals
- **Description:** Students write if statements that validate user input (e.g., "if the input is not a number, show error message"; "if the age is < 0 or > 150, reject and ask again"). This applies conditional logic to data integrity.
- **Challenge format:** Coding, starter project with user input blocks. Prompt: "Write a program that asks for the user's age and only accepts valid numbers between 0 and 120." Students implement conditional checks. Auto‑grading tests a range of valid and invalid inputs.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T08.G8.03 – Process and make decisions on structured data with nested conditionals

- **Short name:** Conditional decision trees for data
- **Description:** Students use nested or chained conditionals to traverse a decision tree or make hierarchical decisions on data (e.g., categorizing users by age and spending, or classifying items by multiple attributes).
- **Challenge format:** Coding, starter project with a dataset (list of records). Prompt: "Classify each person as a 'kid', 'teen', or 'adult' based on age. Then, within each group, mark 'high spender' or 'low spender' based on spending." Students write nested or chained conditionals. Auto‑grading checks classification accuracy on test records.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP.

### T08.G8.04 – Analyze and document the logic of conditional algorithms

- **Short name:** Document and explain conditional logic
- **Description:** Students analyze a conditional algorithm, document its decision logic (often via a flowchart or comment), and justify why specific conditions are needed.
- **Challenge format:** Concept and documentation. Items present a complex conditional algorithm; students either fill in missing comments explaining each branch, or write a short explanation of the decision tree logic, or create a flowchart representing the conditional flow. Auto‑grading checks completeness and accuracy of documentation.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑02, PRO‑PM.

