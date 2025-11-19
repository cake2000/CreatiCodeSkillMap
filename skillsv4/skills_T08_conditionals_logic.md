# T08 – Conditions & Logic: K–8 Skill List (Draft v1)

Topic reference: `T08 Conditions & Logic` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, ALG‑AF (with links to PRO‑TR, DAA‑DI)

Each skill below has:

- a stable **ID** (`T08.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Scope in v3:** Conditions and logic as programming constructs (if/else blocks, compound conditions) are treated as a **Grade 3–8** topic here. K–2 if/then ideas and simple classifications live in T01 (everyday if/then), T04 (conditional patterns), and T25 (categorical data); T08 assumes those foundations and begins when students start block‑based coding.

---

## Grade 3

Grade 3 introduces if/else blocks with **single conditions only** plus choosing when combined conditions are needed, without yet writing AND/OR logic from scratch.

### T08.G3.01 – Use a simple if in a script

- **Short name:** Add an if to control behavior  
- **Description:** Students add their first single `if <condition> then ...` block to a very simple script so that an action only happens when an obvious condition is true (e.g., "if touching the green flag, say 'Yay!'"). This gateway skill introduces the fundamental concept of conditional execution. Start with highly visual, binary conditions that are easy to test.  
- **Challenge format:** Coding, highly scaffolded starter project with step-by-step guidance. Provided: a sprite and a simple script that always performs an action. Prompt: "Only do this when touching the goal" with clear visual guidance. Students wrap the action in an `if` block with a pre-selected condition. Auto‑grading checks that the `if` is present, that the condition is correct, and that behavior changes correctly.  
- **CSTA:** E3‑PRO‑PF‑01. ⭐ Gateway

### T08.G3.02 – Decide when a single if is enough

- **Short name:** Choose simple vs combined checks  
- **Description:** Students read very simple scenarios (e.g., "move only when the space key is pressed" vs "jump only if touching the ground AND space is pressed") and identify whether a single condition is enough or multiple conditions are needed. This builds conceptual understanding without requiring students to write complex logic yet. Use concrete, visual examples.  
- **Challenge format:** Concept, multiple choice with visual scenarios. Learners read simple prompts with pictures and sort them into "single condition" or "needs two conditions" with guided examples. Auto‑grading checks correct grouping.  
- **CSTA:** E3‑PRO‑PF‑01.

### T08.G3.03 – Pick the right conditional block for a scenario

- **Short name:** Match behaviors to if vs if/else  
- **Description:** Students choose between a simple `if` and an `if/else` block for very basic scenarios (e.g., "if touching star, say 'Good!' but don't do anything else" vs "if touching red, say 'Stop!', otherwise say 'Go!'"). Use clear either/or vs. one-way scenarios. Focus on recognizing the difference, not writing complex logic.  
- **Challenge format:** Multiple choice with visual scenarios and pre-built block options. Given simple stories and block diagrams, students pick which block type fits best. Auto‑grading checks selections.  
- **CSTA:** E3‑PRO‑PF‑01.

### T08.G3.04 – Trace code with a single if/else

- **Short name:** Trace simple if/else code  
- **Description:** Students trace a short script with one simple `if/else` block and a given condition to predict which branch runs and what happens.  
- **Challenge format:** Code‑reading MCQ or trace‑table; checked against simulation.  
- **CSTA:** E3‑ALG‑AF‑01, E3‑PRO‑PF‑01.

### T08.G3.05 – Fix a condition that uses the wrong operator

- **Short name:** Debug wrong comparison operator  
- **Description:** Students fix a simple script where a condition uses an obviously wrong comparison operator (e.g., score > 10 when it should be score < 10, with very clear wrong behavior). This contextualized debugging skill teaches debugging as a natural part of learning conditionals. The error should be obvious and the fix straightforward.  
- **Challenge format:** Coding, scaffolded debugging. Starter project shows clear expected behavior vs. actual behavior; students identify and change only the comparison operator with guided options. Auto‑grading checks final behavior.  
- **CSTA:** E3‑PRO‑TR‑01, E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 introduces AND/OR coding, includes both trace and build paths, and then moves into state management and refactoring.

### T08.G4.01 – Combine two conditions with AND

- **Short name:** Use AND to combine conditions  
- **Description:** Students use a compound condition (AND) to check if two things are true at the same time before acting (e.g., "if key pressed AND touching goal, then complete level"). This is their first time writing boolean logic operators in code.  
- **Challenge format:** Coding, starter project. Provided: blocks for two separate conditions. Prompt: "Complete this challenge only if you touch the goal AND collect all coins." Students combine the conditions with AND. Auto‑grading checks correct use of AND operator and behavior.  
- **CSTA:** E4‑PRO‑PF‑01, E4‑ALG‑AF‑01.

### T08.G4.02 – Combine two conditions with OR

- **Short name:** Use OR to combine conditions  
- **Description:** Students use OR to check if at least one of two conditions is true (e.g., "if score > 100 OR lives == 0, then end game").  
- **Challenge format:** Coding, starter project. Prompt: "End the game if the score is high enough OR if lives run out." Students write or complete an if statement with OR. Auto‑grading verifies correct OR logic and behavior in test cases.  
- **CSTA:** E4‑PRO‑PF‑01, E4‑ALG‑AF‑01.

### T08.G4.03 – Trace code with compound conditionals

- **Short name:** Trace AND/OR branches  
- **Description:** Students read code with AND/OR expressions and predict which branch runs for given inputs, building comfort before debugging or refactoring.  
- **Challenge format:** Concept, code‑tracing item. Show code with AND/OR; give input values; ask "Which message will be displayed?" Auto‑grading checks via simulation.  
- **CSTA:** E4‑ALG‑AF‑01, E4‑PRO‑PF‑01.

### T08.G4.04 – Nest if/else statements

- **Short name:** Use nested if/else for layered decisions  
- **Description:** Students write nested if/else blocks where an else branch contains another if (e.g., checking weapon type, then checking ammo level). This models multi-step decision-making.  
- **Challenge format:** Coding, starter project. Prompt: "If the player presses a button, check what weapon they have. If it's a gun, check if there's ammo. If yes, shoot; if no, say 'no ammo'." Students build the nested structure. Auto‑grading verifies correct nesting and behavior across scenarios.  
- **CSTA:** E4‑PRO‑PF‑01.

### T08.G4.05 – Convert nested if to cleaner logic

- **Short name:** Simplify nested if/else  
- **Description:** Students are given deeply nested or redundant if/else code and refactor it using AND, OR, or else-if to make it cleaner and more readable.  
- **Challenge format:** Coding, refactor challenge. Starter project contains nested if statements (e.g., 3+ levels). Students rewrite using compound conditions or else-if chains. Auto‑grading checks code structure (cleaner/flatter) and behavior equivalence.  
- **CSTA:** E4‑PRO‑PF‑01, PRO‑TR.

### T08.G4.06 – Use if to control state changes

- **Short name:** Use conditions to manage state  
- **Description:** Students use conditional logic to manage game states (e.g., "if game over then don't allow movement") or animation states (e.g., "if jumping then use jump costume"). This applies conditionals to tracking program state.  
- **Challenge format:** Coding, starter project. Provided: a game or animation with a state variable (e.g., `is_jumping`, `game_over`). Students add if checks to prevent or trigger actions based on state. Auto‑grading verifies state management via behavior tests.  
- **CSTA:** E4‑PRO‑PF‑01.

### T08.G4.07 – Analyze and fix a logic bug

- **Short name:** Find and fix conditional bugs  
- **Description:** Students debug a script where a condition is incorrect or inverted (e.g., `if score < 10` instead of `if score >= 10`), causing unexpected behavior. They identify and fix the logic error.  
- **Challenge format:** Coding, debugging. A starter project shows expected behavior (e.g., "when score reaches 10, win the game"), but the conditional is wrong. Students adjust the condition or operator. Auto‑grading checks behavior against the expected outcome.  
- **CSTA:** E4‑PRO‑TR‑01.

### T08.G4.08 – Trace code with a sequence of if/else blocks

- **Short name:** Trace sequential if/else  
- **Description:** Students trace code with 2–3 sequential `if/else` blocks and predict the final output for a given set of conditions.  
- **Challenge format:** Code‑reading + prediction; auto‑graded via simulation.  
- **CSTA:** E4‑ALG‑AF‑01.

---

## Grade 5

Grade 5 uses logic for more complex decision trees, scoring systems, and simple AI-like behaviors.

### T08.G5.01 – Design multi-branch decision logic

- **Short name:** Multi-branch decisions  
- **Description:** Students design multi-branch logic (e.g., grading scales, game difficulty tiers) using nested or chained if/else statements.  
- **Challenge format:** Coding, starter project. Prompt: "Given a score, display 'bronze', 'silver', or 'gold' based on ranges." Students implement the logic. Auto‑grading checks that each range maps to the correct label.  
- **CSTA:** E5‑PRO‑PF‑01.

### T08.G5.02 – Use NOT to invert conditions

- **Short name:** Use NOT in conditions  
- **Description:** Students use NOT to invert conditions (e.g., "if NOT touching ground, then falling") and reason about when inversion is clearer than checking the opposite directly.  
- **Challenge format:** Coding, starter project. Prompt: "If the player is NOT on the ground, play the falling animation." Students implement NOT logic. Auto‑grading checks behavior in both states.  
- **CSTA:** E5‑PRO‑PF‑01.

### T08.G5.03 – Combine three or more conditions

- **Short name:** Combine many conditions  
- **Description:** Students write compound conditions that combine three or more tests using AND/OR, such as "if score > 100 AND lives > 0 AND has_key then ..."  
- **Challenge format:** Coding, starter project. Prompt: "Only open the treasure if the player has the key AND at least 3 stars AND is not poisoned." Auto‑grading tests multiple input combinations.  
- **CSTA:** E5‑PRO‑PF‑01, E5‑ALG‑AF‑01.

### T08.G5.04 – Trace complex decision logic

- **Short name:** Trace multi-branch logic  
- **Description:** Students trace a decision tree implemented with nested/compound conditionals and determine which path is taken for various inputs.  
- **Challenge format:** Concept, code-tracing with scenarios. Show code and ask "For input X, which message is shown?" Auto‑grading compares to simulation.  
- **CSTA:** E5‑ALG‑AF‑01.

---

## Grade 6

In middle school, logic is used to implement more sophisticated behaviors and simple AI-like patterns.

### T08.G6.01 – Use conditionals to control simulation steps

- **Short name:** Conditions in simulations  
- **Description:** Students write conditionals that control when a simulation stops, when events trigger, or when entities change behavior (e.g., "if population exceeds limit, reduce births").  
- **Challenge format:** Coding, simulation project. Prompt: "Stop the simulation if the population exceeds 100, or if time reaches 50 steps." Auto‑grading checks stopping conditions.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T08.G6.02 – Implement simple state machines using conditionals

- **Short name:** Use conditions for state machines  
- **Description:** Students use variables and conditionals to implement simple state machines (e.g., idle → walking → jumping based on inputs and timers).  
- **Challenge format:** Coding, starter project. Prompt: "Implement three states for a character: idle, walking, jumping." Auto‑grading checks transitions based on inputs.  
- **CSTA:** MS‑PRO‑PF‑01.

### T08.G6.03 – Debug multi-condition logic

- **Short name:** Fix bugs in complex conditions  
- **Description:** Students debug scripts where multi-part conditions (AND/OR/NOT) are wrong or mis-parenthesized, leading to incorrect behavior.  
- **Challenge format:** Coding, debugging challenge. Starter code has faulty compound conditions; students fix them. Auto‑grading checks corrected behavior.  
- **CSTA:** MS‑PRO‑TR‑11.

---

## Grade 7

Grade 7 emphasizes logical reasoning about fairness, algorithms, and decision impacts.

### T08.G7.01 – Reason about fairness using conditions

- **Short name:** Use conditions to reason about fairness  
- **Description:** Students analyze conditional rules (e.g., eligibility rules in a game or system) and decide whether they treat different groups fairly.  
- **Challenge format:** Concept, scenario analysis. Show if/else rules and ask students to identify who is included/excluded and whether that seems fair. Auto‑grading checks key reasoning.  
- **CSTA:** MS‑ALG‑AF‑01, links to impacts/ethics topics.

### T08.G7.02 – Design tests for condition-heavy code

- **Short name:** Test cases for conditionals  
- **Description:** Students design a set of test inputs that exercise all branches of a condition-heavy script (e.g., all paths through a grading or login system).  
- **Challenge format:** Concept/coding hybrid. Present code; students choose or list test inputs that hit each branch. Auto‑grading checks branch coverage.  
- **CSTA:** MS‑PRO‑TR‑11.

---

## Grade 8

Grade 8 prepares students for high school and more formal reasoning about logic and algorithms.

### T08.G8.01 – Analyze logical equivalence of conditionals

- **Short name:** Compare logically equivalent conditions  
- **Description:** Students compare two conditional expressions and decide whether they are logically equivalent (e.g., De Morgan’s law patterns like NOT(A OR B) vs NOT A AND NOT B).  
- **Challenge format:** Concept, multiple choice and explanation. Show two conditions and ask if they are equivalent for all inputs; students justify. Auto‑grading checks equivalence and key reasoning phrases.  
- **CSTA:** MS‑ALG‑AF‑02.

### T08.G8.02 – Use logic to design robust input validation

- **Short name:** Design input validation logic  
- **Description:** Students use compound conditions to validate user input (e.g., "age between 13 and 18," "password long enough and contains a number") and prevent invalid states.  
- **Challenge format:** Coding, starter project. Prompt: "Only accept a username if it is 3–10 characters and contains no spaces." Auto‑grading checks validation behavior.  
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑TR‑11.

---

### Notes on Dependencies and Alignment

**Editor Notes:**
- K–2 foundations: Conceptual work on everyday if/then rules and simple classifications lives in T01, T04, and T25 and is picture‑based/non‑coding. T08 assumes these foundations.
- G3–5: T08 is a gateway programming topic that follows the progression: simple if → choose if vs if/else → trace → compound conditions (AND/OR) → nested conditions → debug. Single conditions are mastered before combining.
- G6–8: T08 skills assume solid use of conditional logic and focus on state machines, complex decision trees, and logical reasoning.
- This design effectively manages G3 cognitive load and serves as a model for other gateway topics, aligning with CSTA PRO‑PF expectations while keeping skills small, progressive, and CreatiCode‑implementable.
