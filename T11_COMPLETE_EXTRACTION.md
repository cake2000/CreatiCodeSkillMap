# Topic T11 – Functions & Procedures: Complete Skill Extraction

**Extraction Date:** 2025-11-22
**Source File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Total T11 Skills:** 31 (Grades 3-8 only)

---

## Summary Statistics

- **Grade 3 (G3):** 5 skills (T11.G3.01 - T11.G3.05)
- **Grade 4 (G4):** 6 skills (T11.G4.01 - T11.G4.06)
- **Grade 5 (G5):** 8 skills (T11.G5.01 - T11.G5.08)
- **Grade 6 (G6):** 4 skills (T11.G6.01 - T11.G6.04)
- **Grade 7 (G7):** 4 skills (T11.G7.01 - T11.G7.04)
- **Grade 8 (G8):** 4 skills (T11.G8.01 - T11.G8.04)
- **Kindergarten-Grade 2:** 0 skills

---

## Grade 3 Skills (5 skills)

### T11.G3.01
**Topic:** T11 – Functions & Procedures
**Skill:** Understand when to use custom blocks vs loops
**Description:** Students identify scenarios where a custom block (called "My Block" in CreatiCode) is more appropriate than a loop. They recognize that loops repeat the SAME action multiple times, while custom blocks group a SEQUENCE of different actions for reuse. Given example scripts or problems, they choose the better organizational approach and explain their reasoning. This conceptual gateway skill builds organizational thinking without requiring students to define custom blocks yet.

**Assessment example:** Present 3-4 scenarios (e.g., "draw a house," "move 10 steps 5 times," "reset game state," "count to 10"). Students label each as better solved with a loop or a custom block and explain why.

**Dependencies:**
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.02: Trace a script with a simple loop
* T01.G3.12: Predict the final state of a simple algorithm

---

### T11.G3.02
**Topic:** T11 – Functions & Procedures
**Skill:** Use a pre-made custom block with parameters
**Description:** Students use an existing custom block (e.g., "DrawRectangle [width] [height]" or "MoveSprite [x] [y]") provided in a starter project, and experiment with different parameter values to see how the block's behavior changes. They learn that parameters let one block handle many situations.

**Dependencies:**
* T11.G3.01: Understand when to use custom blocks vs loops
* T08.G3.02: Decide when a single if is enough
* T09.G3.01.04: Display variable value on stage using the variable monitor

---

### T11.G3.03
**Topic:** T11 – Functions & Procedures
**Skill:** Identify repeated or grouped actions that could become custom blocks
**Description:** Students examine a longer script (15-30 blocks) and identify groups of blocks that appear multiple times OR represent distinct behaviors. They draw boxes around these groups and label each with a descriptive name (e.g., "reset player," "check win condition"). This builds the habit of recognizing natural custom block boundaries before actually creating them.

**Dependencies:**
* T11.G3.02: Use a pre-made custom block with parameters
* T09.G3.02: Use a variable in a conditional (if block)
* T08.G3.03: Pick the right conditional block for a scenario

---

### T11.G3.04
**Topic:** T11 – Functions & Procedures
**Skill:** Understand the concept of return values
**Description:** Students learn that some blocks **report** (return) a value instead of just doing an action. In CreatiCode, reporter blocks have rounded shapes and fit inside input slots. Examples include built-in reporters like "random 1 to 10" or "distance to [sprite]". Students identify which blocks return values vs. which blocks perform actions.

**Dependencies:**
* T11.G3.03: Identify repeated or grouped actions that could become custom blocks
* T09.G3.04: Debug a single missing or wrong variable block
* T07.G3.04: Use repeat‑until to reach a simple goal

---

### T11.G3.05
**Topic:** T11 – Functions & Procedures
**Skill:** Explore the "Make a Block" interface in CreatiCode
**Description:** Students open CreatiCode's "My Blocks" category, click "Make a Block," and explore the interface options: typing a block name, adding text labels, adding number/text input parameters using parentheses notation like `(width)`. They preview how block definitions work without completing a full custom block yet. This hands-on exploration prepares them for creating their own blocks in Grade 4.

**Dependencies:**
* T11.G3.04: Understand the concept of return values

---

## Grade 4 Skills (6 skills)

### T11.G4.01
**Topic:** T11 – Functions & Procedures
**Skill:** Define and call a simple custom block (no parameters)
**Description:** Students create a custom block with no inputs (e.g., `define (ResetPlayer)`) using CreatiCode's "Make a Block" button. They define the block with 3–5 blocks inside, then use `call ResetPlayer` from a main script. They compare the before/after organization to see how custom blocks improve readability.

**Dependencies:**
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T11.G3.05: Explore the "Make a Block" interface in CreatiCode

---

### T11.G4.02
**Topic:** T11 – Functions & Procedures
**Skill:** Distinguish command blocks from reporter blocks
**Description:** Students learn to recognize which blocks **do something** (command/stack blocks that perform actions) and which blocks **return a value** (reporter blocks with rounded shapes). In CreatiCode, command blocks stack vertically in scripts, while reporter blocks fit inside input slots. Students categorize a set of blocks and predict where each type can be used.

**Dependencies:**
* T11.G4.01: Define and call a simple custom block (no parameters)
* T11.G3.04: Understand the concept of return values
* T09.G3.01.04: Display variable value on stage using the variable monitor

---

### T11.G4.03
**Topic:** T11 – Functions & Procedures
**Skill:** Use a reporter block's result in a calculation or condition
**Description:** Students call built-in reporter blocks and use their returned values directly in conditions or arithmetic (e.g., `if <distance to [sprite] < 50>`, `set x to [random 1 to 10] + 5`). They chain multiple reporters together in expressions.

**Dependencies:**
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T11.G3.04: Understand the concept of return values
* T11.G4.02: Distinguish command blocks from reporter blocks

---

### T11.G4.04
**Topic:** T11 – Functions & Procedures
**Skill:** Describe the purpose of each custom block in a script
**Description:** Students read a script that uses several custom blocks and write a one-sentence description of each block's PURPOSE (e.g., "This block resets the player to the starting position and clears the score"). They focus on WHAT each block does (its goal), not HOW it does it (implementation details). They also identify how blocks fit together in the program's overall structure (e.g., setup, game loop, scoring, ending).

**Dependencies:**
* T11.G4.01: Define and call a simple custom block (no parameters)
* T11.G4.02: Distinguish command blocks from reporter blocks

---

### T11.G4.05
**Topic:** T11 – Functions & Procedures
**Skill:** Trace execution through a script with custom blocks
**Description:** Students trace step-by-step through a script that calls custom blocks, predicting the order of execution and the values returned by reporter blocks at each step. They show the flow of control and data through the program, reinforcing their mental model of procedure calls, returns, and the call stack. This is LOW-LEVEL tracing (execution order) as opposed to G4.04's HIGH-LEVEL understanding (purpose).

**Dependencies:**
* T11.G4.01: Define and call a simple custom block (no parameters)
* T11.G3.04: Understand the concept of return values
* T11.G4.02: Distinguish command blocks from reporter blocks

---

### T11.G4.06
**Topic:** T11 – Functions & Procedures
**Skill:** Understand the argument block for accessing parameters
**Description:** Students learn that inside a custom block definition, the `argument (name)` reporter block retrieves the value passed in when the block is called. They trace through examples showing how `argument (size)` in a definition like `define (DrawSquare (size))` receives the value `50` when called with `call DrawSquare [50]`. This conceptual understanding prepares them for creating parameterized blocks in Grade 5.

**Dependencies:**
* T11.G4.01: Define and call a simple custom block (no parameters)
* T11.G4.02: Distinguish command blocks from reporter blocks
* T11.G3.02: Use a pre-made custom block with parameters

---

## Grade 5 Skills (8 skills)

### T11.G5.01
**Topic:** T11 – Functions & Procedures
**Skill:** Decompose a problem into logical custom block boundaries
**Description:** Given a larger problem description (e.g., "make a quiz game"), students break it into distinct responsibilities that would each make a good custom block (e.g., "show question," "check answer," "update score," "show results"). This is problem decomposition BEFORE coding, focusing on design thinking rather than identifying blocks in existing code.

**Dependencies:**
* T11.G4.04: Describe the purpose of each custom block in a script
* T11.G4.05: Trace execution through a script with custom blocks

---

### T11.G5.02
**Topic:** T11 – Functions & Procedures
**Skill:** Define a custom block with one parameter
**Description:** Students create a custom block that takes one input parameter using `define (DrawSquare (size))` syntax. Inside the definition, they access the parameter using the `argument (size)` reporter block, replacing hard-coded values. They call the block with different arguments like `call DrawSquare [50]` to demonstrate reuse.

**Dependencies:**
* T11.G4.05: Trace execution through a script with custom blocks
* T11.G4.06: Understand the argument block for accessing parameters

---

### T11.G5.03
**Topic:** T11 – Functions & Procedures
**Skill:** Choose between adding a parameter vs. creating a separate block
**Description:** Students analyze scenarios and decide whether to add a parameter to an existing custom block OR create a separate block. For example: should "DrawRectangle" have a color parameter, or should there be separate "DrawRedRectangle" and "DrawBlueRectangle" blocks? They justify their design choice based on reusability and clarity.

**Dependencies:**
* T11.G5.01: Decompose a problem into logical custom block boundaries
* T11.G5.02: Define a custom block with one parameter

---

### T11.G5.04
**Topic:** T11 – Functions & Procedures
**Skill:** Analyze a modular program structure
**Description:** Students examine a larger project (game, animation, simulation) and identify how it uses custom blocks to organize functionality. They explain how this modular design makes the code easier to understand, modify, and debug compared to a non-modular version.

**Dependencies:**
* T11.G4.04: Describe the purpose of each custom block in a script
* T11.G4.05: Trace execution through a script with custom blocks

---

### T11.G5.05
**Topic:** T11 – Functions & Procedures
**Skill:** Define a custom block with two or more parameters
**Description:** Students create a custom block with multiple parameters using `define (DrawRectangle (width) (height))` syntax. Inside the definition, they access each parameter using the `argument` block (e.g., `argument (width)`, `argument (height)`). They practice ordering parameters logically and using clear parameter names, calling the block with various argument combinations like `call DrawRectangle [100] [50]`.

**Dependencies:**
* T11.G5.02: Define a custom block with one parameter
* T11.G5.03: Choose between adding a parameter vs. creating a separate block

---

### T11.G5.06
**Topic:** T11 – Functions & Procedures
**Skill:** Define a custom reporter block that returns a value
**Description:** Students create a custom block that returns a value using CreatiCode's `return [value]` block inside the definition. For example, `define (Average (a) (b))` with a `return` block that computes the average. To use the return value, they call the block with `report Average [10] [20]` instead of `call`, allowing the result to be used in expressions or conditions.

**Dependencies:**
* T11.G5.02: Define a custom block with one parameter
* T11.G4.03: Use a reporter block's result in a calculation or condition

---

### T11.G5.07
**Topic:** T11 – Functions & Procedures
**Skill:** Debug a script with incorrect custom block calls
**Description:** Students examine a script that uses custom blocks incorrectly (e.g., wrong argument values, missing calls, arguments in wrong order, using `call` when `report` is needed or vice versa). They identify and fix 2-3 bugs related to custom block usage.

**Dependencies:**
* T11.G5.02: Define a custom block with one parameter
* T11.G4.05: Trace execution through a script with custom blocks

---

### T11.G5.08
**Topic:** T11 – Functions & Procedures
**Skill:** Use comments to document custom block purpose
**Description:** Students use CreatiCode's `// [comment]` block to add comments inside and above custom block definitions, documenting what the block does, what each parameter represents, and what value it returns (if any). This practice makes code more readable for others and for their future selves.

**Dependencies:**
* T11.G5.02: Define a custom block with one parameter
* T11.G5.06: Define a custom reporter block that returns a value

---

## Grade 6 Skills (4 skills)

### T11.G6.01
**Topic:** T11 – Functions & Procedures
**Skill:** Design custom blocks with clear, predictable interfaces
**Description:** Students design custom blocks by first deciding what the block should do, what inputs (parameters) it needs, and what it should return (if anything) BEFORE writing the code inside. They choose clear, descriptive names for the block and its parameters so that other programmers (or their future selves) can use the block without reading its internal code. This "design the interface first" approach promotes reusable, maintainable code.

**Dependencies:**
* T11.G5.03: Choose between adding a parameter vs. creating a separate block
* T11.G5.04: Analyze a modular program structure
* T11.G5.05: Define a custom block with two or more parameters

---

### T11.G6.02
**Topic:** T11 – Functions & Procedures
**Skill:** Create modular programs with multiple custom blocks
**Description:** Students design and implement a moderately complex program (e.g., a game with setup, gameplay, and end screen) structured as a set of custom blocks, each handling a distinct responsibility. They demonstrate that changing one block doesn't break other parts of the program.

**Dependencies:**
* T11.G5.04: Analyze a modular program structure
* T11.G5.05: Define a custom block with two or more parameters
* T11.G6.01: Design custom blocks with clear, predictable interfaces

---

### T11.G6.03
**Topic:** T11 – Functions & Procedures
**Skill:** Refactor spaghetti code into organized custom blocks
**Description:** Students take a messy, unorganized script (20-30 blocks) and improve it by identifying and extracting logical units into custom blocks, improving readability without changing behavior. They verify the refactored code produces the same output.

**Dependencies:**
* T11.G5.04: Analyze a modular program structure
* T11.G6.01: Design custom blocks with clear, predictable interfaces

---

### T11.G6.04
**Topic:** T11 – Functions & Procedures
**Skill:** Evaluate and critique custom block designs
**Description:** Students look at examples of custom block designs (some good, some poor) and critique them based on clarity, reusability, naming conventions, and appropriate parameter/return choices. They suggest specific improvements and explain why those changes would help.

**Dependencies:**
* T11.G5.03: Choose between adding a parameter vs. creating a separate block
* T11.G6.01: Design custom blocks with clear, predictable interfaces

---

## Grade 7 Skills (4 skills)

### T11.G7.01
**Topic:** T11 – Functions & Procedures
**Skill:** Implement algorithms as reusable custom blocks
**Description:** Students implement standard algorithms (e.g., linear search, bubble sort, greatest common divisor) as custom blocks with clear parameters and return values. They demonstrate that a complex algorithm can be encapsulated in a reusable block that hides its implementation details.

**Dependencies:**
* T11.G6.03: Refactor spaghetti code into organized custom blocks
* T11.G6.04: Evaluate and critique custom block designs
* T11.G5.06: Define a custom reporter block that returns a value

---

### T11.G7.02
**Topic:** T11 – Functions & Procedures
**Skill:** Design a set of related custom blocks for a subsystem
**Description:** Students design a cohesive set of custom blocks that work together to implement a feature or subsystem, such as a "Sprite Physics" system with blocks for velocity, acceleration, and collision, or a "Dialogue System" with blocks for NPC interaction. The blocks should have consistent naming and work well together.

**Dependencies:**
* T11.G6.02: Create modular programs with multiple custom blocks
* T11.G6.03: Refactor spaghetti code into organized custom blocks
* T11.G6.04: Evaluate and critique custom block designs

---

### T11.G7.03
**Topic:** T11 – Functions & Procedures
**Skill:** Understand encapsulation and information hiding
**Description:** Students understand that a well-designed custom block acts like a "black box": users only need to know WHAT it does (its inputs and outputs), not HOW it does it (the code inside). They compare examples of blocks with clear interfaces versus blocks that expose internal details. This "hiding the complexity" principle makes code easier to use and change.

**Dependencies:**
* T11.G6.01: Design custom blocks with clear, predictable interfaces
* T11.G6.03: Refactor spaghetti code into organized custom blocks
* T11.G6.04: Evaluate and critique custom block designs

---

### T11.G7.04
**Topic:** T11 – Functions & Procedures
**Skill:** Trace and debug multi-level custom block calls
**Description:** Students trace through the execution of a script that calls custom blocks, which in turn call other custom blocks (2-3 levels deep). They predict outputs, track variable values, and identify bugs in the call hierarchy. This reinforces understanding of the call stack.

**Dependencies:**
* T11.G5.07: Debug a script with incorrect custom block calls
* T11.G6.03: Refactor spaghetti code into organized custom blocks
* T11.G6.04: Evaluate and critique custom block designs

---

## Grade 8 Skills (4 skills)

### T11.G8.01
**Topic:** T11 – Functions & Procedures
**Skill:** Design a reusable library of custom blocks for games
**Description:** Students design a small library of custom blocks that could be reused across multiple games or projects, such as "CheckCollision [sprite1] [sprite2]", "DrawHUD [score] [lives]", and "HandleGameState [state]". They demonstrate reusability by using the same blocks in two different game projects.

**Dependencies:**
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T11.G7.02: Design a set of related custom blocks for a subsystem
* T11.G7.03: Understand encapsulation and information hiding

---

### T11.G8.02
**Topic:** T11 – Functions & Procedures
**Skill:** Refactor a large program into a hierarchical block structure
**Description:** Students take a large, unorganized program (30+ blocks) and reorganize it using a thoughtful hierarchy of custom blocks—top-level blocks that call mid-level blocks, which call low-level utility blocks—improving clarity and maintainability. They document the hierarchy.

**Dependencies:**
* T11.G7.02: Design a set of related custom blocks for a subsystem
* T11.G7.03: Understand encapsulation and information hiding
* T11.G7.04: Trace and debug multi-level custom block calls

---

### T11.G8.03
**Topic:** T11 – Functions & Procedures
**Skill:** Create custom blocks that work with lists and complex data
**Description:** Students create custom blocks that accept and return lists or structured data (e.g., a "FilterList [list] [condition]" block, or blocks that manage inventory items stored as formatted strings). These blocks enable powerful abstractions for managing collections of game entities, high scores, or other complex data.

**Dependencies:**
* T10.G7.01: Use lists of lists (2D lists) to store tabular data
* T11.G7.02: Design a set of related custom blocks for a subsystem
* T11.G7.03: Understand encapsulation and information hiding

---

### T11.G8.04
**Topic:** T11 – Functions & Procedures
**Skill:** Analyze trade-offs between modular and inline code
**Description:** Students examine two versions of a program: one organized into many custom blocks, one written mostly inline. They discuss trade-offs in readability, maintainability, code reuse, and cognitive load, developing critical thinking about when and how much to modularize.

**Dependencies:**
* T11.G7.03: Understand encapsulation and information hiding
* T11.G7.04: Trace and debug multi-level custom block calls
* T11.G8.02: Refactor a large program into a hierarchical block structure

---

## Observations and Analysis

### 1. Structure and Organization
- **Well-organized progression:** The skills follow a clear learning trajectory from understanding the concept (G3) to implementation (G4-G5) to advanced design and analysis (G6-G8)
- **No early-grade introduction:** T11 starts at Grade 3, which is appropriate since functions/procedures require understanding of basic programming constructs first
- **Consistent format:** All skills follow the standard format with ID, Topic, Skill, Description, and Dependencies

### 2. Skill Progression Pattern
- **Grade 3:** Conceptual understanding (when to use, identifying opportunities, understanding return values)
- **Grade 4:** Basic implementation (defining/calling, distinguishing types, tracing execution)
- **Grade 5:** Parameter handling and practical application (1 param, 2+ params, reporter blocks, debugging)
- **Grade 6:** Design principles (interfaces, modular programs, refactoring, critique)
- **Grade 7:** Advanced concepts (algorithms as blocks, subsystems, encapsulation, multi-level debugging)
- **Grade 8:** Expert-level application (libraries, hierarchical structures, complex data, trade-off analysis)

### 3. Key Conceptual Milestones
- **T11.G3.01:** Gateway skill - distinguishes custom blocks from loops
- **T11.G3.04:** Introduces return values concept (foundational for reporter blocks)
- **T11.G4.01:** First hands-on creation of custom blocks
- **T11.G5.02:** Parameters introduced (single parameter first)
- **T11.G5.06:** Custom reporter blocks (combining parameters + return values)
- **T11.G6.01:** Shift to design-first thinking
- **T11.G7.03:** Encapsulation and information hiding (CS principle)
- **T11.G8.01:** Library design (code reuse across projects)

### 4. Dependencies Analysis
- **Most connected skills:**
  - T11.G6.01 (Design custom blocks) - appears in 5 dependency lists
  - T11.G6.03 (Refactor spaghetti code) - appears in 5 dependency lists
  - T11.G6.04 (Evaluate and critique) - appears in 5 dependency lists
- **Cross-topic dependencies:** T11 skills depend heavily on:
  - T06 (Events) - for script structure understanding
  - T07 (Loops) - for understanding when NOT to use loops
  - T08 (Conditionals) - for using blocks in conditions
  - T09 (Variables) - for understanding data flow
  - T10 (Lists) - only in G8 for complex data structures

### 5. CreatiCode-Specific Features
- Uses CreatiCode terminology: "My Blocks" instead of generic "functions"
- Specific syntax notation: `define (BlockName (param))` and `argument (param)`
- Distinguishes `call` vs `report` for command vs reporter blocks
- Uses `return [value]` block for reporter blocks
- Comment syntax: `// [comment]` block

### 6. Assessment and Learning Activities
- Only T11.G3.01 includes an explicit assessment example
- Most skills describe hands-on activities (create, trace, debug, analyze)
- Strong emphasis on both creating and analyzing/critiquing code

### 7. No Issues Found
- **No duplicate IDs detected**
- **No missing dependencies** (all referenced skills exist in other topics)
- **No gaps in grade progression** (skills build logically)
- **No CSTA codes** (consistent with mid-to-upper grades in this curriculum)
- **Consistent formatting** throughout all 31 skills

### 8. Pedagogical Strengths
- **Scaffolded learning:** Each grade builds on previous grades with clear prerequisites
- **Balance of skills:** Good mix of conceptual understanding, practical implementation, and design thinking
- **Real-world application:** Skills reference practical scenarios (games, simulations, quizzes)
- **Debugging emphasis:** Multiple skills focus on debugging and tracing (G4.05, G5.07, G7.04)
- **Design thinking:** Strong emphasis on design-first approach (G6.01, G6.04, G7.02, G8.01)

### 9. Potential Enhancement Opportunities
- **Assessment examples:** Only G3.01 has an explicit assessment example; others could benefit from similar guidance
- **Recursion:** No mention of recursive custom blocks (may be intentional for K-8 scope)
- **Variable scope:** No explicit discussion of local vs global variables in custom blocks
- **Error handling:** No skills about handling errors or edge cases within custom blocks

---

## Quick Reference: Grade-by-Grade Skill Counts

| Grade | Skill IDs | Count | Focus Area |
|-------|-----------|-------|------------|
| K | None | 0 | N/A |
| 1 | None | 0 | N/A |
| 2 | None | 0 | N/A |
| 3 | T11.G3.01 - T11.G3.05 | 5 | Conceptual understanding |
| 4 | T11.G4.01 - T11.G4.06 | 6 | Basic implementation |
| 5 | T11.G5.01 - T11.G5.08 | 8 | Parameters & practical use |
| 6 | T11.G6.01 - T11.G6.04 | 4 | Design & refactoring |
| 7 | T11.G7.01 - T11.G7.04 | 4 | Advanced concepts |
| 8 | T11.G8.01 - T11.G8.04 | 4 | Expert application |

---

**End of T11 Extraction Report**
