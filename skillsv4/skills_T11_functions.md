# T11 – Functions & Procedures: K–8 Skill List (Draft v1)

Topic reference: `T11 Functions & Procedures` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, ALG‑PS (with links to PRO‑PM, PRO‑PD, ALG‑AF)

Each skill below has:

- a stable **ID** (`T11.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Scope in v3:** T11 focuses on **functions and custom blocks as programming constructs** from **Grade 3–8**. K–2 ideas about grouping actions, naming routines, and splitting plans live in T01/T03/T04/T12; T11 assumes those conceptual foundations and begins only once students are working in the CreatiCode editor. Grades **3–5** focus on **reading, using, and reasoning about** helper procedures (stack custom blocks) and reporter functions (value‑returning blocks), including when they are useful and how their inputs/outputs behave. Grades **6–8** introduce and extend **defining** custom procedures and functions with parameters and return values, building block hierarchies, algorithm libraries, and subsystems. This is aligned with CSTA: elementary grades work with simple algorithms, while middle school introduces modular programs (MS‑PRO‑PD‑08). T04 provides the pattern vocabulary (e.g., search, accumulator); T03/T12 cover project planning and code organization; T11 is specifically about *encapsulating behavior in reusable procedures and functions with clear interfaces*.

---

## Grade 3

Grade 3 gently introduces the idea of helper blocks and functions by **reading and using** pre‑made ones. Students focus on when helpers are useful and how their inputs/outputs behave, without defining new blocks themselves.

### T11.G3.01 – Understand when to use custom blocks vs loops

- **Short name:** Choose between blocks and loops
- **Description:** Students differentiate between using a loop (for repeating the exact same action a fixed number of times) and a custom block (for grouping a complex or varied sequence and reusing it). Both organize code, but for different purposes.
- **Challenge format:** Concept, multiple choice. Present a scenario (e.g., "I want my sprite to do a pattern 5 times") and two approaches: a custom block inside a loop, or just a loop. Ask "Which approach would work here and why?" Auto‑grading checks the choice and reasoning.
- **CSTA:** E3‑ALG‑AF‑01 (Write algorithms including sequence, events, iteration, and selection); E3‑PRO‑PF‑01 (Develop code including these constructs).

### T11.G3.02 – Use a pre‑made helper block with parameters

- **Short name:** Call a block with inputs
- **Description:** Students use an existing helper block (e.g., "DrawRectangle [width] [height]" or "Say [text] for [seconds]") provided in a starter project, and experiment with different parameter values to see how its behavior changes.
- **Challenge format:** Coding, starter project. Provided: scripts that already include one or two helper blocks with parameters. Prompt: "Use the 'DrawRectangle [width] [height]' block three times with different widths and heights to make three different rooms." Students call the block with varied inputs. Auto‑grading checks that the helper is called the required number of times and that outputs match the chosen parameters.
- **CSTA:** E3‑PRO‑PF‑01 (Develop code using existing procedures).

### T11.G3.03 – Identify parts of a script that could be helpers

- **Short name:** Spot behaviors that could be blocks
- **Description:** Students look at a longer script and highlight groups of blocks that represent a meaningful behavior (e.g., "reset player," "check win," "show game over"), even though they do not yet define new custom blocks. This builds the habit of seeing natural helper boundaries.
- **Challenge format:** Concept + light coding. Provided: a jumbled game script. Prompt: "Highlight the blocks that handle setup vs play vs game‑over." Students select ranges or tag them with provided labels. Auto‑grading checks that the same regions are tagged consistently.
- **CSTA:** E3‑PRO‑PM‑05, E3‑ALG‑PS‑03 (Decompose a problem into smaller components).

### T11.G3.04 – Understand the concept of return values

- **Short name:** Know what a return value is
- **Description:** Students are introduced to the idea that a helper can **report** a value (as a reporter block/function) instead of just doing an action—e.g., a "Random Number Between [min] [max]" block returning a number or a "Distance to [sprite]" function in CreatiCode.
- **Challenge format:** Concept, code‑reading item. Show a script that uses a reporter block (built‑in or pre‑made CreatiCode function) inside a condition or assignment. Ask "What value is this function giving back?" and "How is that value used?" Auto‑grading checks recognition of the returned value and its use.
- **CSTA:** E3‑PRO‑PF‑01 (beginning awareness of block outputs).

---

## Grade 4

Grade 4 shifts from only reading helpers to **defining and calling simple parameterless helpers**, then classifying action vs reporter blocks and tracing how calls work.

### T11.G4.01 – Define and call a simple helper (no parameters)

- **Short name:** Make a one-click helper block  
- **Description:** Students create a custom block with no inputs (e.g., “ResetPlayer”) that wraps 3–5 blocks, define it, and call it from a main script to compare before/after organization.  
- **Challenge format:** Coding, starter project. Provided: a script with setup actions repeated twice. Students create a custom block, move the setup actions into it, and call it from both places. Auto‑grading checks that the block exists, contains the actions, and both call sites remain.  
- **CSTA:** E4‑PRO‑PF‑01, E4‑ALG‑PS‑03.

### T11.G4.02 – Distinguish action blocks from reporter functions

- **Short name:** Tell actions from value‑returning blocks
- **Description:** Students learn to recognize which blocks **do something** (procedure‑style stack blocks) and which blocks **return a value** (reporter functions) in CreatiCode, and to predict where each type belongs in a script (stack vs inside conditions/expressions).
- **Challenge format:** Concept, code‑reading and classification. Provide a mix of blocks (e.g., `move 10 steps`, `play sound [pop]`, `distance to [sprite]`, `random [1] to [10]`, and a pre‑made custom reporter). Students sort them into "action" vs "returns a value" and identify where they can be used. Auto‑grading checks classifications and placement.
- **CSTA:** E4‑PRO‑PF‑01 (Analyze code behavior), E4‑PRO‑DH‑02.

### T11.G4.03 – Use a block's result in a calculation

- **Short name:** Use a block's result in a calculation
- **Description:** Students call built‑in or pre‑made reporter functions and use their returned values directly in conditions or arithmetic (e.g., `if <distance to [sprite] < 50>`, `set x to [random 1 to 10] + 5`).
- **Challenge format:** Coding, guided construction. Provided: starter scripts with holes where a reporter should go. Prompt: "Use a reporter block to decide if the player is close to the goal" or "Use a reporter to set a variable to a random starting value." Auto‑grading checks correct reporter usage and resulting behavior.
- **CSTA:** E4‑PRO‑PF‑01, E4‑PRO‑DH‑02 (Trace how data flows through a program).

### T11.G4.04 – Describe what each helper does in a script

- **Short name:** Explain helper roles in code
- **Description:** Students read a script that uses several helpers (procedures and reporter functions) and explain, in everyday language, what each helper does and how they fit together (setup vs game loop vs scoring).
- **Challenge format:** Concept, code‑reading and explanation. Provide a small project that uses 3–4 named helpers. Students match each helper to a description ("gets player input," "checks if player won," "calculates distance") or write short sentences using scaffolds. Auto‑grading checks matches and key phrases.
- **CSTA:** E4‑PRO‑PM‑05, E4‑ALG‑PS‑03.

### T11.G4.05 – Trace through a script with helpers and reporters

- **Short name:** Follow program flow with helper calls
- **Description:** Students read a script that calls helper procedures and reporter functions and trace through the execution to predict final outputs, reinforcing a mental model of calls and returns.
- **Challenge format:** Concept, code‑reading item. Show a script with 2–3 helper calls. Ask questions like "What happens when this script runs?" or "What does the sprite say at the end?" Auto‑grading checks predicted outputs against simulation.
- **CSTA:** E4‑PRO‑PF‑01 (Analyze code flow).

---

## Grade 5

Grade 5 deepens students’ understanding of **why** helper procedures and functions are useful and introduces **defining simple parameterized helpers** while still providing scaffolds.

### T11.G5.01 – Identify subproblems that deserve their own helper

- **Short name:** Pick good helper candidates
- **Description:** Students are given a larger problem description and a long script, and they identify which repeated or conceptually distinct behaviors (e.g., "reset player," "check win condition," "update HUD") would make good helper procedures or functions, even if those helpers are already defined by the teacher or system.
- **Challenge format:** Concept + code‑reading. Provided: a game script plus a list of possible helper names. Students highlight code regions and match them to helper names that would make sense. Auto‑grading checks region/name pairings.
- **CSTA:** E5‑PRO‑PF‑01 (Develop code from student‑created algorithms), E5‑ALG‑PS‑03 (Analyze algorithms).

### T11.G5.02 – Define a simple helper with one parameter

- **Short name:** Add one input to make a helper flexible  
- **Description:** Students create or edit a custom block to take one parameter (e.g., `DrawRectangle [size]` or `SpawnEnemy [speed]`) and replace hard‑coded values with the parameter. They call it with different arguments to show reuse.  
- **Challenge format:** Coding, guided build. Starter project has a parameterless helper and repeated code. Students add one input, update the block body to use it, and call it with at least two values. Auto‑grading checks parameter definition, usage inside the block, and multiple distinct calls.  
- **CSTA:** E5‑PRO‑PF‑01, E5‑ALG‑PS‑03.

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

**3–4:** First exposure to custom blocks with parameters; recognizing when to use a block vs. a loop; introducing return values and using them in expressions; organizing small projects into named procedures.

**5–6:** Custom blocks as a core design tool for larger projects; nested blocks; designing clear interfaces; building whole programs out of well‑named blocks; refactoring messy code into modular structures.

**7:** Implementing standard algorithms as custom blocks; designing cooperating block “subsystems”; practicing encapsulation and tracing nested block calls.

**8:** Reusable game/simulation libraries; deep refactoring of large programs; blocks that operate on complex data; analyzing design trade‑offs in how much and how to modularize.

This progression builds toward the high school expectation (HS‑PRO‑PF‑01: "Convert an algorithm written in pseudocode into a program that uses sequence, selection, iteration, procedures with parameters, and lists") while grounding learning in concrete, auto-gradable challenges in CreatiCode.
