ID: T11.G4.01
Topic: T11 – Functions & Organization
Skill: Create a custom block with one number parameter
Description: Students define a complete custom block with one number parameter and implement its behavior. They click "Make a Block," name it descriptively (e.g., "DrawSquare"), add an input parameter by clicking "Add an input number or text" and naming it (e.g., "size"), which creates `define (DrawSquare [size])`. Inside the definition, they access the parameter value using the `(argument (size))` reporter block in places like `move (argument (size)) steps` or `repeat (argument (size))`. They test by calling the block with different values: `call DrawSquare [50]` creates a different size square than `call DrawSquare [100]`.

Assessment example: Students create a "DrawSquare [size]" custom block that uses `(argument (size))` to control side length, and test with 3 different values (30, 60, 90) to verify it works correctly.

Dependencies:
* T11.G3.09: Distinguish custom blocks from built-in blocks
* T07.G4.03: Use a variable as the loop counter
* T09.G4.01: Initialize variables with descriptive names

---

ID: T11.G4.01.01
Topic: T11 – Functions & Organization
Skill: Use the argument block to access parameter values inside definition
Description: Students learn CreatiCode's `(argument (PARAMETERNAME))` syntax for accessing parameter values inside a custom block definition. When they create `define (Jump [height])`, they use the rounded reporter block `(argument (height))` inside the definition to get the value passed by the caller. They find this block in the "My Blocks" category, drag it into expressions like `change y by (argument (height))` or conditions like `if <(argument (height)) > [100]>`. They understand that argument blocks are reporter blocks (rounded shape) that return the parameter's current value and can be used anywhere a value is needed inside the definition.

Assessment example: Students create `define (SayTwice [message])` and use `(argument (message))` in two `say` blocks to make the sprite say the message twice. They verify that `call SayTwice [Hello]` results in saying "Hello" twice.

Dependencies:
* T11.G4.01: Create a custom block with one number parameter
* T11.G3.13: Identify reporter blocks in existing code

---

ID: T11.G4.02
Topic: T11 – Functions & Organization
Skill: Call a custom block with different parameter values
Description: Students call their parameterized custom block multiple times with different values to accomplish different tasks. For example, after creating "DrawSquare [size]", they write a script that calls `call DrawSquare [30]`, `call DrawSquare [50]`, `call DrawSquare [70]` to draw three squares of increasing size. Each call uses the `call` block from the "My Blocks" category, filling in different values in the parameter slot. This demonstrates the reusability and flexibility of parameterized blocks - one block definition can produce many different results based on the values passed to it.

Assessment example: Students create a pattern or animation by calling the same custom block 3-5 times with different parameter values, such as drawing shapes of different sizes or moving by different distances.

Dependencies:
* T11.G4.01: Create a custom block with one number parameter
* T07.G4.02: Nest one loop inside another

---

ID: T11.G4.03
Topic: T11 – Functions & Organization
Skill: Replace hard-coded values with parameters
Description: Students take an existing custom block with hard-coded values and refactor it to use parameters instead, making it more flexible. For example, they transform `define (DrawTriangle)` with `move 50 steps` and `turn 120 degrees` into `define (DrawTriangle [size])` with `move (argument (size)) steps`. They identify which values should become parameters (typically numbers that might need to vary), add parameters to the block interface, and replace the hard-coded numbers with `(argument (parametername))` blocks. They compare the original and refactored versions and explain the benefits: the new version can draw triangles of any size instead of just one size.

Assessment example: Given a custom block "DrawRectangle" with hard-coded values 60 and 40, students add parameters [width] and [height], replace the hard-coded values with `(argument (width))` and `(argument (height))`, and test with 3 different size combinations.

Dependencies:
* T11.G4.01: Create a custom block with one number parameter
* T09.G4.02: Update a variable's value based on game events

---

ID: T11.G4.04
Topic: T11 – Functions & Organization
Skill: Test parameterized custom blocks with multiple values
Description: Students systematically test their parameterized custom blocks with a range of values to verify correct behavior, including edge cases. For a "DrawPolygon [sides]" block, they test with expected values (3, 4, 6, 8), edge cases (minimum: 3 sides, maximum: 12 sides), and document what happens with each. They create a simple testing script that calls the block with different values and observe the results, noting any unexpected behavior. This introduces basic testing practices and helps students understand the valid input range for their blocks.

Assessment example: Students create a test script for their parameterized block that tries at least 5 different values, including minimum, maximum, and typical values, and document the results in comments.

Dependencies:
* T11.G4.02: Call a custom block with different parameter values

---

ID: T11.G4.05
Topic: T11 – Functions & Organization
Skill: Create a custom block with two parameters
Description: Students create custom blocks with two parameters that work together. They click "Make a Block," add two input parameters by clicking "Add an input number or text" twice, naming them descriptively (e.g., "width" and "height"), which creates a signature like `define (DrawRectangle [width] [height])`. Inside the definition, they access both parameters using `(argument (width))` and `(argument (height))` in different parts of the code. For example, in a rectangle-drawing block: `repeat (2)` → `move (argument (width)) steps`, `turn 90 degrees`, `move (argument (height)) steps`, `turn 90 degrees`. They test with various combinations: `call DrawRectangle [50] [30]`, `call DrawRectangle [100] [20]`.

Assessment example: Students create a "DrawRectangle [width] [height]" block and test it with at least 3 different combinations of width and height values, observing how both parameters affect the result.

Dependencies:
* T11.G4.01: Create a custom block with one number parameter
* T09.G4.03: Use multiple variables for different purposes

---

ID: T11.G4.06
Topic: T11 – Functions & Organization
Skill: Add a boolean parameter to control block behavior
Description: Students create a custom block with a boolean (true/false) parameter that controls conditional behavior inside the block. When adding the parameter in "Make a Block," they select the boolean input type (creates a hexagonal slot), naming it descriptively (e.g., "shouldJump"). In the definition, they use `(argument (shouldJump))` inside an if block to check the parameter: `if <(argument (shouldJump))> then [change y by 50] else [move 10 steps]`. They call the block with both true and false to see different behaviors: `call MoveFigure [true]` makes it jump, `call MoveFigure [false]` makes it walk.

Assessment example: Students create a "MoveFigure [shouldJump]" custom block with conditional logic based on the boolean parameter, and demonstrate calling it with both true and false values to show different behaviors.

Dependencies:
* T11.G4.01: Create a custom block with one number parameter
* T08.G4.22: Combine multiple conditions with AND
* T09.G4.04: Choose between number and text variables

---

ID: T11.G4.07
Topic: T11 – Functions & Organization
Skill: Use text parameters for custom blocks
Description: Students create custom blocks that accept text parameters. When adding the parameter in "Make a Block," they select text input type (creates a rectangular slot for text), naming it descriptively (e.g., "name" or "message"). Inside the definition, they use `(argument (message))` in blocks that expect text, such as `say (argument (message))` or `join [Hello ] (argument (name))`. They explore how text parameters enable flexible, data-driven block behavior. For example, `define (Greet [name])` can greet any name: `call Greet [Alice]` says "Hello Alice," `call Greet [Bob]` says "Hello Bob."

Assessment example: Students create a custom block with a text parameter (like "ShowMessage [text]" or "Greet [name]") and demonstrate calling it with 3 different text values, showing how the block behavior changes based on the text input.

Dependencies:
* T11.G4.01: Create a custom block with one number parameter
* T09.G4.04: Choose between number and text variables

---

ID: T11.G4.08
Topic: T11 – Functions & Organization
Skill: Combine number and text parameters in one block
Description: Students create custom blocks with multiple parameters of different types (numbers and text). For example, `define (ShowMessage [message] [duration])` combines a text parameter for the message with a number parameter for how long to display it. Inside the definition, they use `(argument (message))` in the say block and `(argument (duration))` in the wait block: `say (argument (message))`, `wait (argument (duration)) seconds`. They understand how mixed parameter types enable more flexible blocks and test with various combinations: `call ShowMessage [Hello] [2]`, `call ShowMessage [Goodbye] [5]`.

Assessment example: Students create a custom block with at least one text and one number parameter (like "DisplayText [message] [size]" or "PlaySound [name] [volume]"), implement it using both parameters, and test with 3 different combinations.

Dependencies:
* T11.G4.05: Create a custom block with two parameters
* T11.G4.07: Use text parameters for custom blocks

---

ID: T11.G4.09
Topic: T11 – Functions & Organization
Skill: Call one custom block from inside another
Description: Students create custom blocks that call other custom blocks, building hierarchical organization. For example, `define (DrawHouse)` might call `call DrawRectangle [100] [80]` for the walls and `call DrawTriangle [100]` for the roof, composing a house from simpler shapes. Inside the definition of DrawHouse, they drag in call blocks for other custom blocks from the "My Blocks" category. This demonstrates how complex behaviors can be built from simpler building blocks and introduces the concept of composition. Students verify that the nested calls execute in order as part of the outer block's definition.

Assessment example: Students create 3 custom blocks where at least one block (like "DrawHouse" or "SetupGame") calls another custom block in its implementation, and explain how this organization makes the code easier to understand and modify.

Dependencies:
* T11.G4.05: Create a custom block with two parameters

---

ID: T11.G4.09.01
Topic: T11 – Functions & Organization
Skill: Trace execution through nested custom block calls
Description: Students trace step-by-step through a script that calls a custom block which itself calls other custom blocks. They create an execution trace showing the order of operations: main script → first custom block → nested custom block → back to first custom block → back to main script. For example, when tracing "when green flag clicked" → "call DrawHouse" → (inside DrawHouse definition) "call DrawRectangle [100] [80]" → (inside DrawRectangle definition) all the rectangle drawing steps → back to DrawHouse → "call DrawTriangle [100]" → back to main. They number each step and identify which block definition they're inside at each point. This builds understanding of the call stack concept at an intuitive level.

Assessment example: Given a main script that calls "DrawHouse" which calls "DrawRectangle [100] [80]" and "DrawTriangle [100]", students create a numbered trace showing all blocks executed in order with annotations like "(inside DrawHouse)" or "(inside DrawRectangle)" showing the call context.

Dependencies:
* T11.G4.09: Call one custom block from inside another
* T11.G3.03: Rename vague variables to descriptive names

---

ID: T11.G4.09.02
Topic: T11 – Functions & Organization
Skill: Debug nested custom block execution order issues
Description: Students diagnose and fix bugs caused by incorrect understanding of nested custom block execution. Common issues include: (1) expecting a nested block to run after the outer block finishes when it actually runs during, (2) incorrect assumptions about sprite state when a nested block runs, (3) wrong parameter values passed to nested calls, (4) forgetting that nested blocks execute completely before the outer block continues. They trace execution order step-by-step to identify the problem and fix the sequence.

Assessment example: Given a "DrawHouse" block that calls "DrawDoor [small]" but the door appears in the wrong position, students trace execution to find that DrawDoor runs before the sprite moves to the door position. They fix it by reordering: move to door position first, then call DrawDoor.

Dependencies:
* T11.G4.09.01: Trace execution through nested custom block calls
* T11.G3.18: Debug a custom block that produces wrong results

---

ID: T11.G4.10
Topic: T11 – Functions & Organization
Skill: Compose built-in reporter blocks in expressions and conditions
Description: Students use built-in reporter blocks (rounded blocks that return values) inside other blocks, building more complex expressions. They recognize that reporter blocks like `(pick random 1 to 10)`, `(x position)`, `(distance to [sprite])`, `(answer)`, `(length of [word])` can be nested inside other blocks. For example: `move (pick random 10 to 50) steps`, `if <(distance to [sprite]) < [50]>`, `set [score] to ((score) + (pick random 1 to 10))`, `say (join [You are ] (distance to [Player]) [steps away])`. They understand that rounded blocks return values and can be used anywhere a value is needed: in motion blocks, operators, conditionals, or other reporters.

Assessment example: Students create scripts that use at least 3 different built-in reporter blocks in various contexts: in motion blocks (like `move (pick random 1 to 100) steps`), in operators (like `(round (distance to [sprite]))`), and in conditionals (like `if <(length of [name]) > [5]>`).

Dependencies:
* T11.G3.13: Identify reporter blocks in existing code
* T08.G4.18: Write if-else with two different outcomes
* T09.G4.02: Update a variable's value based on game events

---

ID: T11.G4.11
Topic: T11 – Functions & Organization
Skill: Organize a project with 3-4 custom blocks
Description: Students decompose a project into 3-4 distinct custom blocks, each with a clear responsibility. For example, a simple game might have "SetupGame" (initializes variables, positions sprites), "UpdateScore [points]" (adds points and updates display), "CheckWinCondition" (checks if score >= 100), and "ResetLevel" (restores initial state). They implement all blocks, each with a purpose comment, and coordinate them in a main script. The main script becomes more readable: "call SetupGame", "forever" loop with "call UpdateScore [10]" when sprite is clicked, "call CheckWinCondition", etc. This builds project organization skills.

Assessment example: Students create a complete project (simple game or animation) using 3-4 custom blocks, each documented with a purpose comment, and explain how the blocks work together to achieve the program's goal.

Dependencies:
* T11.G4.02: Call a custom block with different parameter values
* T09.G4.03: Use multiple variables for different purposes
* T11.G3.17: Explain why custom blocks make code easier to read

---

ID: T11.G4.12
Topic: T11 – Functions & Organization
Skill: Choose descriptive action-based names for custom blocks
Description: Students evaluate and improve custom block names, following naming conventions: use action verbs (like Draw, Move, Check, Update, Reset), be specific about what the block does, avoid vague names. For example, "DoStuff" is vague; "Draw" is too general; "DrawSquare" is better; "DrawSquare [size]" with descriptive parameter is best. They compare poor names like "Thing," "Run," "Block1," "X" with good names like "ResetGame," "DrawCircle [radius]," "CheckCollision," "UpdateScore [points]." They rename poorly-named blocks in existing code and explain why each new name better describes the block's purpose.

Assessment example: Given 5 custom blocks with poor names ("DoStuff", "Thing", "Run", "X", "Block1"), students rename them with clear action-based names (like "InitializeVariables", "DrawShape", "MovePlayer", "CheckBoundary", "PlaySound") and explain why each new name is better.

Dependencies:
* T11.G4.11: Organize a project with 3-4 custom blocks
* T11.G3.03: Rename vague variables to descriptive names

---

ID: T11.G4.13
Topic: T11 – Functions & Organization
Skill: Organize related custom blocks into logical groups
Description: Students organize multiple custom blocks by function or purpose, using naming conventions or comments to group related blocks. They use consistent prefixes or categories: all drawing blocks start with "Draw" (DrawSquare, DrawCircle, DrawHouse), all game state blocks start with "Setup" or "Reset" (SetupGame, ResetLevel), all checking blocks start with "Check" (CheckWin, CheckCollision). They might also organize blocks spatially in the blocks palette or use comment headers like "// Drawing Helpers" or "// Game Logic". This introduces namespace organization thinking and makes projects more navigable.

Assessment example: Students create 6-8 custom blocks for a project and organize them into 2-3 logical groups using consistent naming prefixes (like "Draw", "Check", "Update"), with comment headers documenting each group's purpose.

Dependencies:
* T11.G4.12: Choose descriptive action-based names for custom blocks
* T11.G4.11: Organize a project with 3-4 custom blocks

---

ID: T11.G4.14
Topic: T11 – Functions & Organization
Skill: Identify custom blocks that share similar code
Description: Students examine 2-3 related custom blocks and identify code patterns that appear in multiple blocks. For example, three different drawing blocks (DrawSquare, DrawTriangle, DrawCircle) might all start with "pen down" and "set pen color" and end with "pen up". They highlight or annotate the shared code sequences and consider whether they should be extracted into a helper block. This introduces the concept of identifying code duplication and prepares for refactoring. They analyze: Is this code identical or just similar? Does it appear in enough places to warrant extraction? Would a helper block make the code clearer?

Assessment example: Given three custom blocks for a game (StartLevel1, StartLevel2, StartLevel3), students highlight code that appears in multiple blocks (like variable initialization, sprite positioning, score reset) and explain what benefits extracting it into a "SetupLevelDefaults" helper block would provide.

Dependencies:
* T11.G4.11: Organize a project with 3-4 custom blocks
* T11.G3.10: Distinguish when to use custom blocks vs loops

---

ID: T11.G4.15
Topic: T11 – Functions & Organization
Skill: Extract repeated code into a helper custom block
Description: Students identify code that appears in multiple places and extract it into a new "helper" custom block that is called from the original locations. The process: (1) find code repeated in 2+ places, (2) create a new custom block with a descriptive name, (3) move the repeated code into the new block's definition, (4) add parameters if the code uses different values in different places, (5) replace the original repeated code with calls to the new helper block. For example, if three blocks all initialize variables with "set [score] to [0]", "set [lives] to [3]", "set [level] to [1]", they extract this into "ResetGameState" and call it from all three. They verify the program still works after refactoring.

Assessment example: Students find code repeated in 2-3 places, extract it into a new helper block (like "InitializeDefaults" or "ResetPosition"), replace the original code with calls to the helper, and verify the program behavior is unchanged.

Dependencies:
* T11.G4.14: Identify custom blocks that share similar code
* T11.G4.09: Call one custom block from inside another

---

ID: T11.G4.16
Topic: T11 – Functions & Organization
Skill: Document parameter purpose and expected values
Description: Students add comments to custom blocks that explain what each parameter is for and what values are expected or valid. The documentation format: `// BlockName [param1] [param2]: Brief purpose. param1 = expected range/type, param2 = expected range/type`. For example: `// DrawPolygon [sides] [size]: Draws a regular polygon. sides = 3 to 12, size = 10 to 200` or `// MoveTo [x] [y]: Moves sprite to coordinates. x = -240 to 240, y = -180 to 180`. This documentation helps other programmers (and future self) understand how to use the block correctly and what parameter values make sense.

Assessment example: Students document 2-3 custom blocks with parameter descriptions, including expected value ranges or types for each parameter. For example: `// Greet [name] [times]: Says hello to name, repeating times. name = any text, times = 1 to 10`.

Dependencies:
* T11.G4.01: Create a custom block with one number parameter
* T11.G3.12: Identify repeated or grouped actions that could become custom blocks

---

ID: T11.G4.17
Topic: T11 – Functions & Organization
Skill: Document a custom block with a purpose comment
Description: Students write comprehensive documentation comments for custom blocks that include: (1) what the block does (purpose), (2) what each parameter means and expected values, (3) any preconditions (what must be true before calling), (4) any side effects (what changes the block makes). For example: `// ResetGame: Initializes all game state. Sets score=0, lives=3, level=1. Moves player to start position (0,0). Clears all clones. Call this before starting a new game.` They review each other's documentation and practice explaining blocks using only the comment.

Assessment example: Students write comprehensive documentation comments for 2-3 custom blocks, including purpose, parameters (if any), preconditions, and effects. Another student reads only the comment and explains what the block does and how to use it.

Dependencies:
* T11.G4.16: Document parameter purpose and expected values

---

ID: T11.G4.18
Topic: T11 – Functions & Organization
Skill: Design a custom block interface before implementation
Description: Students practice planning custom blocks by writing the block signature (name and parameters) and a purpose comment BEFORE writing any implementation code. They use a design-first approach: (1) identify what the block should accomplish, (2) choose a descriptive name, (3) determine what parameters are needed, (4) write a documentation comment, (5) get feedback on the design, (6) then implement. For a game, they might design: `// UpdateScore [points]: Adds points to score and checks for level-up. points = positive number to add`, then create the interface `define (UpdateScore [points])`, then implement the logic.

Assessment example: Students plan 3 custom blocks for a project by writing their signatures and purpose comments first (like `// SetupLevel [number]`, `// CheckWin`, `// SpawnEnemy [speed]`), then get peer feedback on the design before implementing any code.

Dependencies:
* T11.G4.16: Document parameter purpose and expected values
* T11.G4.12: Choose descriptive action-based names for custom blocks

---

ID: T11.G4.19
Topic: T11 – Functions & Organization
Skill: Use consistent parameter ordering across related blocks
Description: Students ensure that related custom blocks use parameters in a consistent order, making the blocks more intuitive to use. For example, if "DrawRectangle [width] [height]" puts width first, then all shape-drawing blocks should follow the same pattern: "DrawOval [width] [height]", "DrawTriangle [width] [height]". Similarly, if "MoveTo [x] [y]" uses x then y, all position-related blocks should too. They review existing blocks, identify inconsistencies (like some blocks using [x] [y] and others [y] [x]), and reorder parameters for consistency. They understand that consistency reduces errors and makes code more predictable.

Assessment example: Given 3-4 related custom blocks with inconsistent parameter ordering (like "DrawRect [width] [height]", "DrawOval [height] [width]", "DrawTri [size] [color]"), students identify inconsistencies and reorder parameters to be consistent, explaining why consistency matters for usability.

Dependencies:
* T11.G4.05: Create a custom block with two parameters
* T11.G4.13: Organize related custom blocks into logical groups

---

ID: T11.G4.20
Topic: T11 – Functions & Organization
Skill: Test custom blocks independently before integration
Description: Students create simple test scripts for individual custom blocks before using them in larger projects, practicing basic unit testing. They create dedicated test scripts (often with comment headers like "// Test DrawSquare") that call the block with multiple different parameter values and verify the results visually or with variables. For example, to test "DrawSquare [size]": `call DrawSquare [30]`, `wait 1 seconds`, `call DrawSquare [60]`, `wait 1 seconds`, `call DrawSquare [90]`, checking that three squares of increasing size appear. Testing independently helps catch bugs early, before the block is used in complex interactions.

Assessment example: Students create test scripts for 2-3 custom blocks, each testing the block with multiple different parameter values (including edge cases) and documenting the expected vs actual results.

Dependencies:
* T11.G4.04: Test parameterized custom blocks with multiple values
* T11.G4.16: Document parameter purpose and expected values

---

ID: T11.G4.21
Topic: T11 – Functions & Organization
Skill: Identify side effects in custom blocks
Description: Students learn to recognize when custom blocks have "side effects" - they change things beyond their return value, like moving a sprite, changing a variable, playing a sound, changing appearance, or creating clones. They examine custom blocks and categorize them by their side effects: "DrawSquare [size]" has side effects (moves sprite, draws with pen), "GetDistance" might not (just returns a value), "ResetGame" has many side effects (changes variables, moves sprites, clears clones). They understand that some blocks are designed to change state (like "UpdateScore [points]") while others just calculate or return information. This builds awareness of how blocks affect program state.

Assessment example: Given 5-6 custom blocks, students identify what each block changes (sprite position, variables, appearance, sounds, clones) and explain whether those changes are intentional parts of the block's purpose or unintended side effects that should be documented.

Dependencies:
* T11.G4.11: Organize a project with 3-4 custom blocks
* T09.G4.02: Update a variable's value based on game events

---

ID: T11.G4.22
Topic: T11 – Functions & Organization
Skill: Decide when to create a new custom block vs add to existing
Description: Students make design decisions about whether to create a new custom block or extend an existing one. They consider factors: (1) Does this belong with existing functionality? (2) Is the existing block getting too complex? (3) Would a parameter handle this variation? (4) Are the purposes related or different? For example, if they have "DrawSquare [size]" and need to draw circles, they create a separate "DrawCircle [radius]" (different shape). But if they need squares with different colors, they add a parameter: "DrawSquare [size] [color]". They practice this decision-making with scenarios and justify their choices.

Assessment example: Given 4-5 scenarios describing new functionality to add (like "draw a filled square" when "DrawSquare" exists, or "reset just the score" when "ResetGame" exists), students decide for each whether to create a new custom block, add a parameter to existing, or modify existing, explaining their reasoning.

Dependencies:
* T11.G4.09: Call one custom block from inside another
* T11.G4.14: Identify custom blocks that share similar code

---

ID: T11.G4.23
Topic: T11 – Functions & Organization
Skill: Identify when NOT to create a custom block
Description: Students recognize situations where creating a custom block would be over-engineering or unnecessary abstraction. They apply guidelines: (1) code that only runs once in the entire program doesn't need a block, (2) trivial 1-2 block sequences are clearer inline, (3) code that differs significantly each time shouldn't be forced into one block. For example, a single `say [Hello] for 2 seconds` should NOT become a custom block. But code that appears 3+ times or groups a complex multi-step process SHOULD be a block. They evaluate scenarios and decide when blocks add value vs add unnecessary complexity.

Assessment example: Given 5 code snippets (like "say Hello", "repeat 10 [move 10 steps turn 36 degrees]", "set score to 0 set lives to 3", "move 10 steps", "initialize 5 different variables"), students categorize each as "should be a custom block" or "should stay as inline code" and explain their reasoning with reference to repetition, complexity, and clarity.

Dependencies:
* T11.G4.14: Identify custom blocks that share similar code
* T11.G3.10: Distinguish when to use custom blocks vs loops

---

ID: T11.G4.24
Topic: T11 – Functions & Organization
Skill: Read and explain custom blocks from a shared project
Description: Students open a project created by another student or provided as an example, examine the custom blocks, and explain what each block does based on: (1) the block name and parameters, (2) the documentation comments, (3) the implementation code. They practice reading code without having written it, which builds code comprehension skills. For each custom block, they identify: purpose, parameters and their meanings, what the block changes (side effects), and how it's used in the main scripts. This prepares students for collaborative programming and reading documentation.

Assessment example: Given a shared project with 3-4 custom blocks (like "SetupGame", "UpdateScore [points]", "CheckWin", "DrawLevel"), students write explanations of what each block does, what its parameters mean, and how it's used in the project, without running the code first.

Dependencies:
* T11.G4.09.01: Trace execution through nested custom block calls
* T11.G4.16: Document parameter purpose and expected values

---

ID: T11.G4.25
Topic: T11 – Functions & Organization
Skill: Debug custom blocks with wrong parameter values
Description: Students diagnose and fix bugs where custom blocks don't work as expected because of parameter issues: (1) wrong order of arguments (width/height swapped), (2) missing arguments, (3) wrong data types (text instead of number), (4) values out of expected range (negative size, sides=1). They use tracing to follow parameter values: check what value is passed in the call, verify it flows to `(argument (name))` correctly, check if it's used appropriately. For example, debugging "DrawRectangle [width] [height]" that draws squares, they trace to find both arguments are the same value.

Assessment example: Given a "DrawRectangle [width] [height]" block that's drawing squares instead of rectangles, students trace the calls to identify that the caller is passing the same value for both parameters (`call DrawRectangle [50] [50]`) and fix it to use different values.

Dependencies:
* T11.G4.05: Create a custom block with two parameters
* T12.G4.03: Test alternative implementations to find bugs

---

ID: T11.G4.26
Topic: T11 – Functions & Organization
Skill: Review and refactor custom block organization
Description: Students review a project with 5-8 custom blocks and refactor the organization for clarity and quality. They perform multiple improvements: (1) rename blocks with vague names to descriptive names, (2) reorder parameters for consistency across related blocks, (3) merge similar blocks that could be one block with parameters, (4) split overly complex blocks into smaller focused blocks, (5) extract repeated code into helper blocks, (6) improve documentation comments, (7) organize blocks into logical groups with consistent naming. This is a comprehensive organization review skill combining many previous skills.

Assessment example: Students review a provided project with poorly organized custom blocks (vague names, inconsistent parameters, duplicated code, missing documentation) and create an improved version. They document all changes made (renaming, extracting, merging, documenting) and explain why each change improves the code organization and maintainability.

Dependencies:
* T11.G4.13: Organize related custom blocks into logical groups
* T11.G4.22: Decide when to create a new custom block vs add to existing
* T11.G4.15: Extract repeated code into a helper custom block

---
