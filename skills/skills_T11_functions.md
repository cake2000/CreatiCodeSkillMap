# T11 – Functions & Modularization: K–8 Skill List (Draft v1)

Topic reference: `T11 Functions & Modularization` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, ALG‑PS (with links to PRO‑PM, PRO‑PD, ALG‑AF)

Each skill below has:

- a stable **ID** (`T11.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

In Kindergarten, students are introduced to the idea of reusable blocks and simple procedures as a precursor to custom blocks. No formal function definition or parameters are expected.

### T11.GK.01 – Recognize repeating code sequences

- **Short name:** Spot repeated blocks in short scripts
- **Description:** Students examine simple scripts and identify when the same group of blocks appears multiple times (e.g., "jump, spin, jump, spin" as a recognizable pattern). This plants the seed for the later idea that repeated code can be organized.
- **Challenge format:** Concept, multiple choice or highlighting. A script is shown with 3–4 repetitions of a simple sequence (move + sound). Students click on or select the repeated part. Auto‑grading checks for correct identification.
- **CSTA:** EK‑ALG‑AF‑01 (Identify algorithms in daily activities – recognizing repeated patterns).

### T11.GK.02 – Understand "do this group of actions"

- **Short name:** Bundle actions together
- **Description:** Students are introduced to the idea of grouping multiple actions as a single unit, though not yet with formal custom blocks. They use gestures, language ("jump and spin together"), or visual groupings to indicate that several actions belong together.
- **Challenge format:** Concept, guided input. Students drag action blocks into a highlighted area labeled "My Action" or similar to indicate grouping. The system accepts this and shows the grouped actions can be triggered as one unit. Auto‑grading checks that the grouping is made and logically consistent.
- **CSTA:** EK‑ALG‑PS‑03 (Identify individual parts that make up a whole).

### T11.GK.03 – Name a simple action

- **Short name:** Give a name to a repeated action
- **Description:** Students are introduced to labeling or naming a simple action (e.g., "My Dance" for a sequence of moves) in a visual or verbal way, preparing them to later define custom blocks with names.
- **Challenge format:** Concept, interactive naming exercise. A script shows a sequence of blocks. Students type or select a name for that sequence (from choices or free entry). The system then allows them to see "My Dance" used or referenced, showing that a name represents a group of actions. Auto‑grading checks that a label has been applied.
- **CSTA:** EK‑PRO‑PF‑01 (Choose code that matches an algorithm; early procedural awareness).

---

## Grade 1

Grade 1 focuses on recognizing the need to organize repeated code and introduces the idea of a custom block as a reusable unit, though parameter use is minimal.

### T11.G1.01 – Identify code that would benefit from a custom block

- **Short name:** Notice when code repeats
- **Description:** Students examine longer scripts and recognize that a particular sequence of blocks is repeated several times, and begin to understand that creating a single reusable version would reduce duplication.
- **Challenge format:** Concept, multiple choice. Show a script with 3+ copies of "move 10, turn 90, stamp." Ask "Which blocks are repeated?" and "Would you want to do them once instead of three times?" Students select the repeated sequence. Auto‑grading checks the selection.
- **CSTA:** E1‑ALG‑AF‑01 (Create algorithms including step-by-step instructions); E1‑ALG‑PS‑03 (Describe function of parts within a system).

### T11.G1.02 – Create a simple custom block (no parameters)

- **Short name:** Make your own block
- **Description:** Students define a simple custom block (in CreatiCode or similar) with a fixed sequence of actions inside (e.g., a "Dance" block containing move + turn + move). When the block is called, it runs the same sequence every time.
- **Challenge format:** Coding, starter project. Provided: a sprite and several isolated action blocks. Prompt: "Create a custom block called 'Dance' that does: move 10, turn 90, move 10." Students build the block definition, then use it in a script. Auto‑grading checks that the custom block is defined correctly and runs the right actions when called.
- **CSTA:** E1‑PRO‑PF‑01 (Create code including sequence and events).

### T11.G1.03 – Use a custom block in a script

- **Short name:** Call a custom block
- **Description:** Students use a pre-made custom block (provided by the teacher or system) in their own scripts, understanding that dragging the block into a script causes it to execute all the actions it contains.
- **Challenge format:** Coding, guided construction. Provided: a pre-built custom block "Jump 3 Times" and a blank script. Prompt: "Use the 'Jump 3 Times' block twice in a row to make the sprite jump 6 times total." Students drag the custom block into the script. Auto‑grading checks that the block is used the correct number of times and the sprite jumps as expected.
- **CSTA:** E1‑PRO‑PF‑01.

### T11.G1.04 – Explain why custom blocks reduce duplicate code

- **Short name:** Understand the benefit of custom blocks
- **Description:** Students reflect on or discuss why defining a reusable block is better than copying the same sequence many times: it's shorter, easier to modify, and less error‑prone.
- **Challenge format:** Concept, multiple choice or short answer. Present two versions of a script: one with 4 copies of "turn 90" and one with a custom block "Turn 4 Times" called once. Ask "Which is easier to change if you want to turn 45 degrees instead?" or similar. Auto‑grading checks the selection and key reasoning.
- **CSTA:** E1‑ALG‑PS‑03; E1‑PRO‑PM‑04 (Explain the function of a code segment).

---

## Grade 2

Grade 2 introduces custom blocks with simple parameters, allowing students to write more flexible reusable code.

### T11.G2.01 – Understand the purpose of a parameter

- **Short name:** Understand what a parameter does
- **Description:** Students learn that a parameter is an input to a custom block—a value that can change each time the block is called. Instead of separate "Jump 3 Times" and "Jump 5 Times" blocks, one "Jump N Times" block accepts different numbers.
- **Challenge format:** Concept, code‑reading item. Show a custom block definition with a parameter slot (e.g., "Move [distance] steps"). Ask "What can change each time you call this block?" or show two calls to the same block with different values and ask what is different. Auto‑grading checks the answer.
- **CSTA:** E2‑PRO‑PF‑01 (Create code including sequence, events, and iteration).

### T11.G2.02 – Create a custom block with one parameter

- **Short name:** Make a block with an input
- **Description:** Students design and define a custom block that accepts one parameter (e.g., "Move [steps] units" or "Say [text]"), and internally uses that parameter in place of a hardcoded value.
- **Challenge format:** Coding, starter project. Provided: empty custom block definition window. Prompt: "Create a custom block called 'Move and Turn' that takes one parameter called 'distance'. Inside, use that parameter to move the sprite that many steps, then turn 90 degrees." Students set up the parameter and blocks. Auto‑grading checks the parameter definition and that the block uses it correctly (e.g., moving different distances for different input values).
- **CSTA:** E2‑PRO‑PF‑01, E2‑PRO‑PD (Program Development – starting to modularize).

### T11.G2.03 – Call a custom block with different parameter values

- **Short name:** Use a block with different inputs
- **Description:** Students call the same custom block multiple times with different parameter values, demonstrating that the block's behavior adapts based on the input.
- **Challenge format:** Coding, guided construction. Provided: a pre-made custom block "Say Message [text]." Prompt: "Call this block three times with different messages: 'Hello', 'Hi', and 'Bye'." Students place the custom block three times, filling in different text values. Auto‑grading checks that the block is called three times and the sprite says the correct messages in order.
- **CSTA:** E2‑PRO‑PF‑01.

### T11.G2.04 – Refactor repeated blocks into a custom block with a parameter

- **Short name:** Turn repeated code into a parameterized block
- **Description:** Students take a script with repeated similar sequences (e.g., three "move X steps, turn 90" in slightly different variations) and recognize that a single custom block with a parameter could replace them.
- **Challenge format:** Coding, refactor challenge. Starter script contains: move 10, turn 90; move 20, turn 90; move 15, turn 90. Prompt: "Create a custom block 'MoveAndTurn' with a parameter 'amount', then replace the repeated code with three calls to this new block." Auto‑grading checks the custom block definition (with parameter) and that the script now calls it three times with the correct values.
- **CSTA:** E2‑PRO‑PF‑01, E2‑ALG‑PS‑03 (Modify algorithms with repeating patterns).

---

## Grade 3

Grade 3 deepens work with parameters and introduces simple return values (reporting a value from a custom block).

### T11.G3.01 – Understand when to use custom blocks vs loops

- **Short name:** Choose between blocks and loops
- **Description:** Students differentiate between using a loop (for repeating the exact same action a fixed number of times) and a custom block (for grouping a complex or varied sequence and reusing it). Both organize code, but for different purposes.
- **Challenge format:** Concept, multiple choice. Present a scenario (e.g., "I want my sprite to do a pattern 5 times") and two approaches: a custom block inside a loop, or just a loop. Ask "Which approach would work here and why?" Auto‑grading checks the choice and reasoning.
- **CSTA:** E3‑ALG‑AF‑01 (Write algorithms including sequence, events, iteration, and selection); E3‑PRO‑PF‑01 (Develop code including these constructs).

### T11.G3.02 – Create a custom block with multiple parameters

- **Short name:** Make a block with several inputs
- **Description:** Students define a custom block that accepts two or more parameters, such as "Draw a Rectangle [width] [height]" or "Say [text] for [seconds]."
- **Challenge format:** Coding, starter project. Provided: custom block definition interface. Prompt: "Create a custom block 'DrawRectangle' with parameters 'width' and 'height'. Inside, move forward by width, turn 90, move forward by height, turn 90, and repeat this twice to form a rectangle." Students define the parameters and arrange the blocks. Auto‑grading checks that both parameters are defined and used correctly in the block body.
- **CSTA:** E3‑PRO‑PF‑01.

### T11.G3.03 – Use a custom block to organize complex behavior

- **Short name:** Use blocks for organization
- **Description:** Students use custom blocks to partition a larger project into smaller, logical pieces. For example, separating setup, game loop, and end-screen logic into different custom blocks called from the main script.
- **Challenge format:** Coding, project organization. Provided: a incomplete game script with jumbled code. Prompt: "Organize this script into three custom blocks: 'Setup', 'PlayRound', and 'ShowWin'. Call them in the right order in your main script." Students identify which lines belong in each block, define the blocks, and call them appropriately. Auto‑grading checks the code structure and that the script behaves correctly when run.
- **CSTA:** E3‑PRO‑PM‑05, E3‑ALG‑PS‑03 (Decompose a problem into smaller components).

### T11.G3.04 – Understand the concept of return values

- **Short name:** Know what a return value is
- **Description:** Students are introduced to the idea that a custom block can compute a value and report it back to the caller, rather than just performing actions. For example, a "Random Number Between [min] [max]" block returns a number.
- **Challenge format:** Concept, code‑reading item. Show a custom block that "reports" or "returns" a value (e.g., a block that says "report [distance to sprite]"). Ask "What does this block give back to whoever uses it?" Auto‑grading checks the answer.
- **CSTA:** E3‑PRO‑PF‑01 (beginning awareness of block outputs).

---

## Grade 4

Grade 4 introduces custom blocks that return values and reinforces the use of modular design for larger projects.

### T11.G4.01 – Create a custom block that returns a value

- **Short name:** Make a block that reports a result
- **Description:** Students define a custom block that takes input parameter(s), performs computation or checks, and returns (reports) a single value. For example, "Distance to [sprite]" or "Is [number] even?" returning true/false.
- **Challenge format:** Coding, starter project. Provided: custom block definition interface with a "report" block available. Prompt: "Create a custom block 'IsEven' that takes a number as input and reports true if the number is even, false otherwise." Students define the parameter, add the logic, and use the "report" block. Auto‑grading tests the block with several inputs (even and odd numbers) and checks the returned values.
- **CSTA:** E4‑PRO‑PF‑01 (Develop code including all core constructs).

### T11.G4.02 – Use a reporter block in expressions

- **Short name:** Use a block's result in a calculation
- **Description:** Students call a custom block that returns a value and use that result directly in an expression, such as in a conditional or arithmetic operation. For example: `if [IsEven [number]]` or `set x to [Distance to Mouse]`.
- **Challenge format:** Coding, guided construction. Provided: a pre-made custom block "Distance to Mouse" that returns a number. Prompt: "Create a script that says 'You are close' if the distance is less than 50 and 'You are far' otherwise. Use the Distance to Mouse block in your condition." Students build the conditional using the reporter block. Auto‑grading checks that the correct condition is used and the script behaves as expected.
- **CSTA:** E4‑PRO‑PF‑01, E4‑PRO‑DH‑02 (Trace how data flows through a program).

### T11.G4.03 – Refactor code to use custom blocks for clarity

- **Short name:** Reorganize code into logical blocks
- **Description:** Students take a moderately complex script and identify natural groupings of related actions, creating custom blocks to improve readability and maintainability without changing the overall behavior.
- **Challenge format:** Coding, refactor challenge. Starter script contains about 15–20 blocks implementing a simple game or animation. Prompt: "Identify 3 logical tasks in this script (e.g., 'Setup', 'Handle Input', 'Check Win Condition') and create a custom block for each. Then rewrite the main script to call these blocks." Auto‑grading checks the code structure, verifies that custom blocks are defined and called, and runs the script to confirm behavior is preserved.
- **CSTA:** E4‑PRO‑PM‑05, E4‑ALG‑PS‑03 (Assess an algorithm's effectiveness).

### T11.G4.04 – Trace through a script with custom blocks

- **Short name:** Understand the flow of a program with blocks
- **Description:** Students read a script that calls custom blocks (with and without parameters/return values) and trace through the execution to predict the final result. This reinforces understanding of how blocks are modular units that can be called and return control to the caller.
- **Challenge format:** Concept, code‑reading item. Show a script with calls to 2–3 custom blocks. Ask questions like "What happens when this script runs?" or "What does the sprite say at the end?" Auto‑grading checks the predicted output against simulation.
- **CSTA:** E4‑PRO‑PF‑01 (Analyze code flow).

---

## Grade 5

Grade 5 solidifies the use of custom blocks as a core design tool and introduces nested custom blocks and more complex parameter combinations.

### T11.G5.01 – Design a custom block to solve a specific subproblem

- **Short name:** Create a block for a specific task
- **Description:** Students are given a larger problem and tasked to identify a logical subproblem (e.g., "check if a sprite is on a colored tile") and design a custom block with appropriate parameters and return value to solve it.
- **Challenge format:** Coding, design challenge. Prompt: "Create a custom block 'SpriteTouchingColor [color]' that takes a color name and returns true if the sprite is touching that color, false otherwise. Then use this block in a script to make the sprite say 'Found it!' when touching red." Students define the block with one parameter and a report statement, then use it in a conditional. Auto‑grading checks the block definition and tests it with multiple color scenarios.
- **CSTA:** E5‑PRO‑PF‑01 (Develop code from student-created algorithms), E5‑ALG‑PS‑03 (Analyze algorithms).

### T11.G5.02 – Use custom blocks within custom blocks (nesting)

- **Short name:** Call a custom block from another custom block
- **Description:** Students create a custom block that internally calls another custom block, building abstraction layers. For example, a "Draw House" block might call a "Draw Rectangle" block four times with different parameters.
- **Challenge format:** Coding, starter project. Provided: a pre-made "DrawRectangle" block with width and height parameters. Prompt: "Create a new custom block 'DrawHouse' that calls DrawRectangle to make the walls, then separately draws a roof using triangles. Use DrawHouse in your main script." Students create the new block, call the existing block multiple times within it, and verify the result. Auto‑grading checks the block nesting and final visual output.
- **CSTA:** E5‑PRO‑PF‑01, E5‑ALG‑PS‑03 (Analyze algorithms for efficiency).

### T11.G5.03 – Decide between a parameter and a call to a separate block

- **Short name:** Choose clean parameter design
- **Description:** Students think about when to add a parameter to a custom block vs. when to create a separate block or call another block. This reinforces interface design thinking.
- **Challenge format:** Concept, multiple choice/short answer. Scenario: "I have a 'DrawStar' block and a 'DrawMoon' block. Should I create one 'DrawShape' block with a parameter, or keep them separate?" Discuss trade‑offs. Auto‑grading checks for understanding of design decisions.
- **CSTA:** E5‑PRO‑PF‑01 (develop code), E5‑ALG‑PS‑03 (analyze).

### T11.G5.04 – Analyze a modular program structure

- **Short name:** Understand modular design in larger projects
- **Description:** Students examine a larger project (game, animation, simulation) and identify how it uses custom blocks to organize functionality, explaining how this design makes the code easier to understand and modify.
- **Challenge format:** Concept, analysis. Provided: a sample project with 5–6 custom blocks organized logically. Prompt: "Describe what each custom block does and how they work together. How would the code be different if all blocks were written inline?" Auto‑grading uses a rubric to assess understanding of modularity benefits.
- **CSTA:** E5‑PRO‑PM‑05 (Explain aspects of a program), E5‑PRO‑PF‑01 (Develop code).

---

## Grade 6

In middle school, custom blocks become a standard design tool. Grade 6 focuses on using modular design in the context of larger algorithms and introducing the idea of block "interfaces" (clear input/output contracts).

### T11.G6.01 – Design blocks with clear, predictable interfaces

- **Short name:** Create well-defined block interfaces
- **Description:** Students design custom blocks where the purpose, parameters, and return value (if any) are clear and well-named, making the blocks easy to use and reuse without reading internal details. This is "interface-first" thinking.
- **Challenge format:** Coding, design challenge. Prompt: "Create three related custom blocks: 'MoveToward [target] [speed]', 'IsWithin [distance] of [target]', and 'AngleToward [target]'. Make sure their names and parameters are clear." Students design the blocks and then use them in a pathfinding script. Auto‑grading checks parameter naming clarity and that the blocks work correctly together.
- **CSTA:** MS‑PRO‑PF‑01 (Analyze code segments and their roles), MS‑PRO‑PD‑08 (Create modular programs).

### T11.G6.02 – Create modular programs with multiple custom blocks

- **Short name:** Build a program using many blocks
- **Description:** Students design and implement a moderately complex program (e.g., a game with setup, gameplay, and end screen) structured as a set of custom blocks, each handling a distinct responsibility.
- **Challenge format:** Coding, project construction. Prompt: "Create a simple number-guessing game. Use custom blocks for: 'Start Game' (pick a number), 'GetPlayerGuess' (returns the guessed number), 'CheckGuess [target] [guess]' (returns 'too high', 'too low', or 'correct'), and 'PlayGame' (loops the guessing until correct). Then write a main script that calls these blocks to run the game." Auto‑grading checks code structure (custom blocks defined and called), parameter/return usage, and that the game behaves correctly.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑PD‑08.

### T11.G6.03 – Refactor spaghetti code into organized blocks

- **Short name:** Clean up unorganized code with blocks
- **Description:** Students take a messy, unorganized script and improve it by identifying and extracting logical units into custom blocks, improving readability without changing behavior.
- **Challenge format:** Coding, refactor challenge. Provided: a working but disorganized script (20–30 blocks, jumbled logic) implementing a simple animation or interaction. Prompt: "Refactor this script into logical custom blocks to make it clearer. Aim for 3–4 well-named blocks that work together." Auto‑grading checks that the refactored code is organized into custom blocks and behaves identically to the original.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑PM‑16 (Document a program).

### T11.G6.04 – Analyze and improve block abstraction

- **Short name:** Evaluate custom block design
- **Description:** Students look at examples of custom block designs (some good, some poor) and critique them based on clarity, reusability, and appropriate parameter/return choices. They suggest improvements.
- **Challenge format:** Concept, analysis/critique. Show 2–3 examples of custom blocks with different design choices (e.g., one with too many parameters, one with unclear naming, one well-designed). Ask students to rate them and explain why. Auto‑grading uses a rubric for design reasoning.
- **CSTA:** MS‑PRO‑PF‑01 (Analyze code), MS‑ALG‑PS‑05 (Demonstrate correctness of algorithms).

---

## Grade 7

Grade 7 emphasizes using custom blocks for algorithm implementation and introduces the relationship between custom blocks and larger software design patterns.

### T11.G7.01 – Use custom blocks to implement algorithms

- **Short name:** Code an algorithm as a custom block
- **Description:** Students implement standard or simple algorithms (e.g., linear search, bubble sort, greatest common divisor) as custom blocks with clear parameters and return values, demonstrating that a complex algorithm can be encapsulated in a reusable block.
- **Challenge format:** Coding, algorithmic challenge. Prompt: "Create a custom block 'LinearSearch [list] [target]' that searches a list for the target and returns the index (or -1 if not found). Then use this block in a script to find a number in a list." Students implement the search logic using loops and conditionals, properly parameterize it, and test it. Auto‑grading runs the block with multiple test cases (found, not found, edge cases) and checks correctness.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑02 (Describe data input/output/processing).

### T11.G7.02 – Design a set of related blocks for a subsystem

- **Short name:** Create a family of related blocks
- **Description:** Students design a cohesive set of custom blocks that work together to implement a feature or subsystem, such as a "Sprite Physics" system with blocks for velocity, acceleration, and collision, or a "Dialogue System" with blocks for NPC interaction.
- **Challenge format:** Coding, design and implementation. Prompt: "Design a simple particle system with custom blocks: 'CreateParticle [x] [y] [velocity]', 'UpdateParticle [particle]' (moves it and applies gravity), and 'DrawAllParticles' (renders active particles). Use these to create falling rain or fireworks." Students design and implement the blocks, then create a scene using them. Auto‑grading checks that the blocks are properly defined, called together coherently, and produce the expected visual effect.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑PD‑08 (Create modular programs).

### T11.G7.03 – Understand encapsulation and data hiding

- **Short name:** Hide implementation details in blocks
- **Description:** Students learn that a well-designed custom block hides its implementation details from the user; the caller only needs to know the interface (parameters and return value), not how it works inside. This is a step toward object-oriented thinking.
- **Challenge format:** Concept, code‑reading and design. Provided: a complex custom block (e.g., "MoveAlongSpline [t]" that uses internal math). Prompt: "Explain what this block does from the outside (without looking at its internals). Why is it good that the user doesn't need to understand the math inside?" Auto‑grading checks for understanding of encapsulation benefits.
- **CSTA:** MS‑PRO‑PD‑08 (Create modular programs), MS‑ALG‑PS‑05 (Demonstrate correctness).

### T11.G7.04 – Trace and debug complex block hierarchies

- **Short name:** Follow execution through nested blocks
- **Description:** Students trace through the execution of a script that calls blocks, which in turn call other blocks, predicting outputs and identifying bugs. This reinforces call stack thinking.
- **Challenge format:** Concept, code‑reading and debugging. Show a script with nested block calls (3 levels deep). Ask "What is the final output?" or "Where is the bug?" Students trace through and explain the flow. Auto‑grading checks the predicted output and/or bug identification against simulation.
- **CSTA:** MS‑PRO‑PF‑01 (Analyze code), MS‑PRO‑TR‑11 (Test, debug, and review code).

---

## Grade 8

Grade 8 extends modular design thinking to larger projects and introduces the relationship between custom blocks, data structures, and program organization in the context of competitive-style programming challenges.

### T11.G8.01 – Design blocks for a game or simulation framework

- **Short name:** Build reusable game components
- **Description:** Students design a small library of custom blocks that could be reused across multiple games or projects, such as "CheckCollision [sprite1] [sprite2]", "DrawHUD [score] [lives]", and "HandleGameState [state]". They demonstrate reusability by using the same blocks in two different game projects.
- **Challenge format:** Coding, design challenge. Prompt: "Create a set of custom blocks for a simple game engine: 'UpdateGameState', 'HandleInput', 'CheckCollisions', 'RenderScreen', 'PlaySound [sound]'. Use these blocks to build two different games (e.g., a space shooter and a platformer) that share the same block library." Students design the blocks to be general enough to work in both contexts, then implement both games. Auto‑grading checks that the block definitions are reused (same blocks in both games) and both games function correctly.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑PD‑08, MS‑PRO‑PM‑16 (Document a program).

### T11.G8.02 – Refactor a complex program into a well-organized block hierarchy

- **Short name:** Restructure a large program with blocks
- **Description:** Students take a large, unorganized program (30+ blocks) and reorganize it using a thoughtful hierarchy of custom blocks—top-level blocks that call mid-level blocks, which call low-level utility blocks—improving clarity and maintainability.
- **Challenge format:** Coding, refactor and design. Provided: a working but messy game or simulation (e.g., a Breakout clone with jumbled code). Prompt: "Reorganize this program using a 3-level block hierarchy: 'Main' calls 'GameLoop', 'Update', 'Render'; 'Update' calls 'MovePlayer', 'MoveEnemies', etc.; 'MovePlayer' calls helper blocks. Verify the program still works the same way." Students refactor the code into the hierarchy. Auto‑grading checks that the code is properly organized into custom blocks at multiple levels and behaves identically to the original.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑PD‑08, MS‑PRO‑PM‑16.

### T11.G8.03 – Use custom blocks with complex data (lists, objects)

- **Short name:** Write blocks that handle complex data types
- **Description:** Students create custom blocks that accept and return complex data structures (lists of sprites, lists of objects with multiple attributes), enabling powerful abstractions for managing game entities, inventories, or other game data.
- **Challenge format:** Coding, data structures and blocks. Prompt: "Create a custom block 'FilterSprites [list] [condition]' that takes a list of sprites and a condition (e.g., 'touching wall') and returns a new list containing only sprites matching the condition. Then use this block in a script to update only sprites in a certain area." Students implement the block with list parameters and returns. Auto‑grading tests the block with multiple lists and conditions, verifying correct filtering.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑DH‑06 (Use iteration to access and process collection elements).

### T11.G8.04 – Analyze trade-offs in modular vs. monolithic design

- **Short name:** Compare modular and inline code
- **Description:** Students examine two versions of a program: one organized into many custom blocks, one written mostly inline. They discuss trade-offs in readability, maintainability, performance, and complexity, developing critical thinking about when and how much to modularize.
- **Challenge format:** Concept, comparison and explanation. Provided: two implementations of the same feature (one modular, one monolithic). Prompt: "Compare these two approaches. Which is easier to understand? Which is easier to modify? When might you choose the monolithic approach?" Auto‑grading uses a rubric for reasoning about design trade-offs.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑02 (Describe data flow in algorithms), MS‑ALG‑PS‑07 (Hypothesize about internal processes).

---

## Summary of T11 Skill Progression

**K–1:** Introduction to the concept of reusable blocks and simple grouping of actions.

**2–3:** Custom blocks with parameters; understanding why they reduce duplication; introduction to return values.

**4–5:** Return values and using them in expressions; nested custom blocks; modular design for larger projects.

**6:** Designing blocks with clear interfaces; building entire programs from custom blocks; refactoring unorganized code.

**7:** Algorithms as custom blocks; subsystem design; encapsulation and data hiding; tracing through block hierarchies.

**8:** Reusable game/simulation libraries; complex hierarchical refactoring; custom blocks with complex data; design trade-offs and decision-making.

This progression builds toward the high school expectation (HS‑PRO‑PF‑01: "Convert an algorithm written in pseudocode into a program that uses sequence, selection, iteration, procedures with parameters, and lists") while grounding learning in concrete, auto-gradable challenges in CreatiCode.
