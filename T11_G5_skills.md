ID: T11.G5.01
Topic: T11 – Functions & Organization
Skill: Use the return block to send a value from a custom block
Description: Students learn the `return [VALUE]` block in CreatiCode's My Blocks category to create custom reporter blocks that send values back to the caller. They understand that `return` ends block execution immediately and sends the specified value to wherever the block was called. For example, in `define (DoubleIt [num])`, they add `return [((argument (num)) * 2)]` to send back the doubled value. They recognize that any blocks after `return` will not execute, making `return` a control flow statement as well as a value-passing mechanism. Students test their reporter blocks by using them in expressions and verifying the returned values are correct.

Assessment example: Students create `define (CalculateArea [width] [height])` containing `return [((argument (width)) * (argument (height)))]` and verify that `set [area] to (report CalculateArea [5] [3])` sets area to 15.

Dependencies:
* T11.G4.05: Organize a project with 3-4 custom blocks
* T10.G5.01: Calculate with arithmetic expressions (nested operators)
* T11.G3.19: Explain how custom blocks improve code clarity

---

ID: T11.G5.01.01
Topic: T11 – Functions & Organization
Skill: Call a custom reporter block using report syntax
Description: Students learn to call custom reporter blocks using CreatiCode's `report` syntax to retrieve returned values. Unlike command blocks called with `call BlockName [args]`, reporter blocks must be called with `report BlockName [args]` which evaluates to the returned value. They practice using reporter calls in various contexts: inside variable assignments `set [result] to (report CalculateScore [10] [2])`, within expressions `((total) + (report GetBonus))`, and in conditionals `if <(report IsReady) = [true]>`. Students understand that `report` invocations are reporter blocks themselves (rounded shape) and can be nested inside any block that accepts values. They compare this to built-in reporter blocks like `(pick random 1 to 10)` to reinforce the concept.

Assessment example: Students use `report CalculateScore [hits] [multiplier]` in three different contexts: in a variable assignment, inside an arithmetic expression with operators, and within an if condition.

Dependencies:
* T11.G5.01: Use the return block to send a value from a custom block
* T11.G4.10: Call one custom block from inside another

---

ID: T11.G5.01.02
Topic: T11 – Functions & Organization
Skill: Compare call vs report syntax side-by-side
Description: Students explicitly compare and contrast CreatiCode's two ways of invoking custom blocks: `call BlockName [args]` for command blocks that perform actions, and `report BlockName [args]` for reporter blocks that return values. They examine side-by-side examples showing when each syntax is appropriate and the errors that occur from mixing them up. For instance, they see that `call DrawSquare [50]` is correct for drawing but `call CalculateScore [10]` cannot be used in `set [score] to (call CalculateScore [10])` because `call` doesn't return a value. They practice identifying incorrect syntax in code samples (e.g., using `report` on a command block or `call` on a reporter block) and fixing them. This explicit comparison helps prevent the common confusion between the two invocation styles.

Assessment example: Given 8-10 custom block invocations, students identify which use correct syntax and fix incorrect ones, explaining why each fix is needed (e.g., "Changed `call GetDistance [x]` to `report GetDistance [x]` because the result needs to be used in a comparison").

Dependencies:
* T11.G5.01.01: Call a custom reporter block using report syntax
* T11.G3.08: Explain when to use custom blocks vs inline code

---

ID: T11.G5.02
Topic: T11 – Functions & Organization
Skill: Distinguish when to use reporter vs command custom blocks
Description: Students develop decision-making skills for choosing whether new custom blocks should be reporters (return a value) or commands (perform an action with side effects). They learn that reporters are appropriate when the primary purpose is to compute or retrieve information without changing program state, while commands are for performing actions that modify sprite properties, variables, or other state. Given various scenarios, they categorize each as better suited to a reporter or command and explain their reasoning. For example, "CalculateDistance [x1] [y1] [x2] [y2]" should be a reporter because it only computes a value, while "MoveTo [x] [y]" should be a command because it changes sprite position. Students recognize that some operations could be implemented either way but identify best practices (e.g., prefer reporters for calculations, commands for state changes).

Assessment example: Given 8-10 block descriptions (e.g., "Get player's current level", "Show game over screen", "Check if inventory is full", "Reset score to zero"), students categorize each as reporter or command and explain their reasoning with reference to whether the block computes/retrieves information vs changes state.

Dependencies:
* T11.G5.01: Use the return block to send a value from a custom block
* T11.G4.21: Review and refactor custom block organization

---

ID: T11.G5.03
Topic: T11 – Functions & Organization
Skill: Use custom reporter blocks in expressions
Description: Students compose custom reporter blocks they created with operators and other reporters to build complex expressions. They understand that custom reporters work exactly like built-in reporters (rounded blocks) and can be combined freely. For example, they create expressions like `set [finalScore] to (((report CalculateBaseScore [hits]) * (report GetMultiplier [level])) + (report GetTimeBonus [seconds]))` that combine multiple custom reporters with arithmetic operators. They nest custom reporters inside other blocks: `move ((report GetSpeed [powerups]) * 2) steps` or `wait ((report CalculatePause [difficulty]) / 10) seconds`. Students recognize that this composability makes custom reporters powerful building blocks for complex calculations.

Assessment example: Students create an expression that combines at least two custom reporter blocks with at least two arithmetic operators and one built-in reporter block (e.g., pick random or distance), then test it with different values.

Dependencies:
* T11.G5.01: Use the return block to send a value from a custom block
* T10.G5.01: Calculate with arithmetic expressions (nested operators)

---

ID: T11.G5.04
Topic: T11 – Functions & Organization
Skill: Use custom reporter blocks in conditionals
Description: Students use custom reporter blocks in if conditions, repeat-until loops, and wait-until blocks to create readable, maintainable conditional logic. Instead of writing complex inline conditions, they encapsulate logic in reporter blocks: `if <(report IsPlayerNearEnemy [50])>` instead of `if <(distance to [enemy]) < [50]>`, or `repeat until <(report HasWonLevel)>` instead of embedding all winning conditions inline. They understand that boolean reporter blocks make conditionals self-documenting and easier to modify. Students practice both numeric reporters used in comparisons `if <(report GetPlayerHealth) < [20]>` and boolean reporters used directly `if <(report IsGameOver)>`. They learn to choose reporter names that read naturally in conditions.

Assessment example: Students create at least three control structures (if/if-else/repeat-until/wait-until) that use custom reporter blocks in their conditions, demonstrating both numeric reporters with comparisons and boolean reporters used directly.

Dependencies:
* T11.G5.01: Use the return block to send a value from a custom block
* T08.G5.02: Nest if statements for multi-level decisions

---

ID: T11.G5.05
Topic: T11 – Functions & Organization
Skill: Create boolean custom reporter blocks
Description: Students create custom reporter blocks specifically designed to return true/false values for use in conditionals. They understand that boolean reporters encapsulate complex conditions into readable, reusable, testable blocks. For example, `define (IsScoreHigh [score])` contains `return <(argument (score)) > [100]>`, or `define (CanPlayerJump)` contains `return <((touching [ground]?) and ((yVelocity) = 0))>`. Students practice creating boolean reporters that combine multiple conditions with AND/OR operators, making complex logic manageable. They name boolean reporters as questions that return yes/no answers: "IsWinning", "CanMove", "HasPowerup", "ShouldSpawnEnemy". They test their boolean reporters with various inputs to verify they return correct true/false values.

Assessment example: Students create 2-3 boolean reporter blocks with descriptive question-form names, each combining at least two conditions with AND or OR, and demonstrate using them in if statements or loops to control program flow.

Dependencies:
* T11.G5.01: Use the return block to send a value from a custom block
* T08.G5.03: Combine multiple conditions with OR

---

ID: T11.G5.06
Topic: T11 – Functions & Organization
Skill: Validate parameter values at block start
Description: Students implement defensive programming by adding validation code at the beginning of custom blocks to check that parameter values are reasonable before using them. They learn common validation patterns: checking for negative values `if <(argument (size)) < [1]> then set [size] to [1]`, checking for empty strings `if <(argument (name)) = []> then set [name] to [Player]`, and checking ranges `if <(argument (speed)) > [100]> then set [speed] to [100]`. Students understand that validation prevents errors, makes blocks more robust, and provides sensible defaults for edge cases. They add validation to blocks that could receive problematic inputs and test with intentionally bad inputs to verify validation works. They document what validations are in place and why they're needed.

Assessment example: Students add parameter validation to 2-3 custom blocks to handle edge cases (negative numbers, zero, empty values, out-of-range values), test each block with invalid inputs to verify validation works correctly, and document the validation rules in comments.

Dependencies:
* T11.G4.16: Test custom blocks independently before integration
* T08.G5.04: Chain if-else for 3+ exclusive options

---

ID: T11.G5.07
Topic: T11 – Functions & Organization
Skill: Use default values for optional parameters
Description: Students implement optional parameters by checking if a parameter is empty or unspecified and using a default value when necessary. In CreatiCode, they check if a parameter is empty `if <(argument (color)) = []> then set [color] to [blue]` or use conditional logic to provide defaults. For example, `define (DrawCircle [radius] [color])` might default color to red if not specified: `if <(argument (color)) = []> then set [color] to [#FF0000]`. Students understand that optional parameters make blocks more flexible and easier to use: callers who want the default behavior don't need to specify every parameter. They document which parameters are optional and what their default values are. They test calling blocks both with and without optional parameters.

Assessment example: Students create a custom block with 2-3 parameters where at least one has a default value, clearly document which parameters are optional and their defaults, and demonstrate calling the block in multiple ways: with all parameters, with only required parameters, and with some optional parameters.

Dependencies:
* T11.G4.05: Organize a project with 3-4 custom blocks
* T08.G5.04: Chain if-else for 3+ exclusive options

---

ID: T11.G5.08
Topic: T11 – Functions & Organization
Skill: Create custom blocks with 3+ parameters
Description: Students create custom blocks with three or more parameters, managing the increased complexity through clear naming, logical ordering, and thorough documentation. For example, `define (DrawRectangle [x] [y] [width] [height] [color])` requires tracking five pieces of information. They learn to keep parameter lists manageable (typically 3-5 parameters; more suggests the block might be doing too much) and organize parameters logically. Students use the `(argument (PARAMNAME))` block to access each parameter inside the definition and verify they're using the correct parameter in each context. They test multi-parameter blocks with diverse combinations of values to ensure all parameters work correctly.

Assessment example: Students create a custom block with 4-5 parameters, implement it completely using all parameters, document what each parameter controls, and demonstrate calling it with at least three different combinations of arguments.

Dependencies:
* T11.G4.05: Organize a project with 3-4 custom blocks
* T11.G4.19: Use text parameters for custom blocks

---

ID: T11.G5.08.01
Topic: T11 – Functions & Organization
Skill: Order parameters logically in multi-parameter blocks
Description: Students learn and apply principles for ordering parameters in blocks with 3+ parameters to maximize usability and clarity. Key principles include: (1) required parameters before optional ones, (2) most important/frequently-changed parameters first, (3) related parameters grouped together (e.g., x and y coordinates adjacent), (4) parameters following a natural sequence (e.g., start before end, width before height). For example, `define (DrawRectangle [x] [y] [width] [height] [color])` groups position parameters (x, y) before size parameters (width, height), with the less frequently changed color last. Students review existing blocks with poor parameter ordering and refactor them, explaining how the new order improves usability.

Assessment example: Given 3-4 custom blocks with poorly ordered parameters (e.g., `define (MoveSprite [speed] [x] [direction] [y])`), students reorder parameters following best practices, explain the principles applied, and demonstrate that the reordered version is easier to understand and use.

Dependencies:
* T11.G5.08: Create custom blocks with 3+ parameters
* T11.G4.19: Use text parameters for custom blocks

---

ID: T11.G5.09
Topic: T11 – Functions & Organization
Skill: Choose between local variables and parameters
Description: Students develop decision-making skills for determining when values should be parameters (passed from caller) versus local variables (created inside the block). They understand that parameters make blocks flexible and reusable by letting callers control behavior, while local variables keep internal calculations encapsulated and avoid cluttering the block interface with implementation details. For example, in `define (DrawPolygon [sides] [size])`, `sides` and `size` should be parameters because callers need to control them, but `angle` should be a local variable calculated as `360 / sides` because it's an internal implementation detail. Students analyze scenarios and make appropriate choices, explaining trade-offs between flexibility (more parameters) and simplicity (fewer parameters, more local variables).

Assessment example: Given 4-6 custom block scenarios with lists of values the block uses, students identify which values should be parameters and which should be local variables, explaining their reasoning in terms of caller control vs internal implementation.

Dependencies:
* T11.G5.08: Create custom blocks with 3+ parameters
* T09.G5.01: Use variables with limited scope in projects

---

ID: T11.G5.10
Topic: T11 – Functions & Organization
Skill: Create and use nested custom reporter blocks
Description: Students create custom reporter blocks that call other custom reporter blocks in their implementation, building hierarchical calculations and demonstrating the composability of reporters. For example, `define (CalculateFinalScore)` might call `return [(((report CalculateBaseScore [hits]) * (report GetDifficultyMultiplier [level])) + (report GetTimeBonus [elapsedTime]))]`, composing three reporter blocks into a final calculation. Students understand that nested reporters enable building complex calculations from simpler, tested components. They create reporter hierarchies where low-level reporters perform basic calculations, mid-level reporters combine those, and high-level reporters produce final results. They trace values through the hierarchy to understand how results are computed and debug when results are unexpected.

Assessment example: Students create 3-4 custom reporter blocks where at least two call other custom reporters in their implementation, creating a calculation hierarchy (e.g., TotalScore calls BaseScore and BonusScore; BonusScore calls TimeBonus and ComboBonus), and demonstrate the hierarchy working correctly.

Dependencies:
* T11.G5.03: Use custom reporter blocks in expressions
* T11.G4.09: Identify custom blocks that share similar code

---

ID: T11.G5.11
Topic: T11 – Functions & Organization
Skill: Trace return values through nested reporter calls
Description: Students debug custom reporter blocks by systematically tracing return values through multiple levels of nested calls. When `report CalculateFinalScore` calls `report GetBaseScore [hits]` and `report GetMultiplier [level]`, they trace each intermediate return value back through the chain to understand how the final result is computed. They add temporary `log` statements at each return point to visualize value flow: `log [join [BaseScore returning: ] [(report GetBaseScore [hits])]]`. Students create trace diagrams showing the call hierarchy and returned values at each level. They use this tracing skill to identify where unexpected values originate in nested reporter chains and fix calculation errors.

Assessment example: Given a nested reporter calculation that returns an unexpected result (e.g., `report FinalScore` that uses `report BaseScore [hits]` and `report Multiplier [level]`), students add logging to trace all intermediate return values, create a diagram showing the call hierarchy and values, and identify which reporter is returning an incorrect value.

Dependencies:
* T11.G5.10: Create and use nested custom reporter blocks
* T11.G4.09.01: Trace execution through nested custom block calls

---

ID: T11.G5.12
Topic: T11 – Functions & Organization
Skill: Debug custom blocks using console logging
Description: Students add temporary `log [message]` blocks inside custom block definitions to trace execution flow and inspect variable and parameter values during debugging. They learn strategic logging placement: (1) at block entry to log parameters `log [join [DrawSquare called with size: ] [(argument (size))]]`, (2) at key calculation points to log intermediate values `log [join [Calculated angle: ] [angle]]`, (3) at conditional branches to log which path was taken `log [Size was negative, using default]`, (4) before return statements to log return values `log [join [Returning: ] [result]]`. After debugging, students remove or comment out logging statements. They understand that logging helps them "see inside" block execution when blocks don't behave as expected.

Assessment example: Students debug a faulty custom block by adding 4-6 log statements that show: entry with parameter values, intermediate calculations, conditional branch taken, and return value (for reporters). They use the console output to identify and fix the bug, then remove/comment the logging.

Dependencies:
* T11.G5.10: Create and use nested custom reporter blocks
* T12.G5.05: Use log blocks to trace variable values

---

ID: T11.G5.13
Topic: T11 – Functions & Organization
Skill: Design custom block interfaces for a project before coding
Description: Students practice design-first development by planning all custom blocks for a project BEFORE writing implementation code. They create a design document listing each block's name, parameters (with types and purposes), return value (for reporters), and brief description of what the block does. They specify how blocks will call each other and which blocks depend on which. This upfront planning helps them think through the architecture, identify missing functionality, spot duplicate functionality, and organize the project logically before getting lost in implementation details. They understand that good design makes implementation smoother and results in better-organized code. After implementing, they reflect on how the design helped and what they would change.

Assessment example: Students write a design document for a game or animation project specifying 6-8 custom blocks with complete signatures (name, parameters with types, return type for reporters), purpose descriptions, and a diagram or list showing which blocks call which. Then they implement the project following the design and reflect on how the design helped or what they learned.

Dependencies:
* T11.G4.18: Design a custom block interface before implementation
* T11.G4.26: Use custom blocks to organize complex projects

---

ID: T11.G5.13.01
Topic: T11 – Functions & Organization
Skill: Decompose project requirements into custom block responsibilities
Description: Students analyze written project requirements or user stories and systematically identify what custom blocks are needed, what each should do, and how they work together. This is requirements analysis translated into code organization. For example, given "Create a game where the player collects coins, avoids enemies, and progresses through levels with increasing difficulty," students identify blocks like `SetupLevel [levelNum]`, `SpawnCoin [x] [y]`, `SpawnEnemy [speed] [pattern]`, `CheckCoinCollision`, `CheckEnemyCollision`, `UpdateDifficulty [levelNum]`, `ShowLevelComplete`, etc. They categorize blocks by responsibility (initialization, game loop, collision detection, difficulty management, UI) and identify dependencies between blocks.

Assessment example: Given a 3-4 paragraph project description with multiple features and requirements, students create a list of 8-12 custom blocks with names, parameters, brief purpose statements, and categories (initialization/main/helper), showing they've decomposed requirements into implementable blocks.

Dependencies:
* T11.G5.13: Design custom block interfaces for a project before coding
* T11.G4.18: Design a custom block interface before implementation

---

ID: T11.G5.14
Topic: T11 – Functions & Organization
Skill: Refactor a long script into well-named custom blocks
Description: Students take a long (40-60 block) monolithic script and refactor it into 4-6 well-named, focused custom blocks, improving readability and maintainability. They identify logical sections in the long script (initialization, main loop, helper operations), extract each section into a custom block with a descriptive name, replace the original code with calls to the new blocks, and verify the refactored version works identically. For example, a long game loop might be refactored into `SetupGame`, `GameLoop`, `HandleInput`, `UpdatePhysics`, `CheckCollisions`, `UpdateUI`. Students understand that refactoring improves code organization without changing behavior. They practice choosing good block names that describe what each block does.

Assessment example: Given a long script (40-60 blocks) that implements complete functionality in one place, students refactor it into 4-6 custom blocks with clear names and responsibilities, document each block, and verify the refactored version produces identical behavior to the original.

Dependencies:
* T11.G4.15: Extract repeated code into a helper custom block
* T11.G4.26: Use custom blocks to organize complex projects

---

ID: T11.G5.15
Topic: T11 – Functions & Organization
Skill: Design custom blocks for single responsibility
Description: Students apply the Single Responsibility Principle (SRP) to custom blocks: each block should do one thing well and have one reason to change. They learn to recognize blocks that do too much (violate SRP) and split them into focused blocks. For example, a block named `UpdateGameState` that updates score, checks win conditions, spawns enemies, and updates UI does too much and should be split into `UpdateScore`, `CheckWinCondition`, `SpawnEnemies`, and `UpdateUI`. Students understand that single-responsibility blocks are easier to name, test, debug, reuse, and modify. They review existing blocks, identify SRP violations, and refactor them into well-focused blocks.

Assessment example: Given 2-3 custom blocks that do multiple unrelated things (e.g., one block that updates score, plays sound, changes costume, and spawns items), students identify the multiple responsibilities, split each into 2-3 focused blocks, and explain the benefits in terms of testing, debugging, and reusability.

Dependencies:
* T11.G5.14: Refactor a long script into well-named custom blocks
* T11.G4.22: Debug custom blocks with wrong parameter values

---

ID: T11.G5.16
Topic: T11 – Functions & Organization
Skill: Organize blocks into initialization, main, and helper categories
Description: Students categorize all custom blocks in a project into three architectural categories: (1) initialization blocks that run at program start to set up initial state, (2) main blocks that implement core functionality and game loop logic, and (3) helper blocks that are called by other blocks to perform specific tasks. They use naming conventions to mark categories (e.g., `Setup_Level`, `Main_GameLoop`, `Helper_CalculateScore`) or organize blocks into commented sections in the block palette. This architectural thinking helps them understand code structure at a higher level and see how blocks work together. They create diagrams or documentation showing which category each block belongs to and how blocks in different categories interact.

Assessment example: Students categorize 10-15 custom blocks from a project into initialization, main, and helper groups, use naming prefixes or comments to mark categories, and create a diagram showing how blocks in different categories call each other.

Dependencies:
* T11.G4.13: Decide when to create a new custom block vs add to existing
* T11.G5.13: Design custom block interfaces for a project before coding

---

ID: T11.G5.17
Topic: T11 – Functions & Organization
Skill: Document block preconditions and postconditions
Description: Students add comments specifying what must be true before calling a block (preconditions) and what will be true after it executes (postconditions), introducing formal specification thinking. Preconditions describe assumptions the block makes about parameter values, variable states, or sprite positions. Postconditions describe what the block guarantees when it completes. For example: `// PRECONDITION: lives > 0, gameState = 'playing' // POSTCONDITION: score updated by points, lives may decrease, gameState may change to 'gameOver'`. Students understand that documenting preconditions and postconditions helps callers use blocks correctly, helps them design better blocks, and aids in debugging when assumptions are violated. They verify through testing that documented conditions actually hold.

Assessment example: Students add precondition and postcondition documentation to 3-4 custom blocks using a consistent comment format, test that preconditions are actually required, and verify through testing that postconditions are guaranteed.

Dependencies:
* T11.G4.16: Test custom blocks independently before integration
* T11.G5.06: Validate parameter values at block start

---

ID: T11.G5.18
Topic: T11 – Functions & Organization
Skill: Document custom blocks with purpose comments
Description: Students systematically add comprehensive purpose comments to all custom blocks following a consistent format that includes: (1) what the block does, (2) what each parameter means with expected types and ranges, (3) what the block returns (for reporters) with type and possible values, (4) any important side effects or state changes, (5) any preconditions or special requirements. For example: `// DrawRectangle: Draws a filled rectangle at the specified position // Parameters: x (number) - left edge x-coordinate, y (number) - top edge y-coordinate, width (number) - rectangle width in pixels (must be > 0), height (number) - rectangle height in pixels (must be > 0), color (color) - fill color // Side effects: Changes pen color, draws on stage // Precondition: pen must be up before calling`. Students understand that comprehensive documentation helps others (and their future selves) understand and use blocks correctly.

Assessment example: Students document 5-7 custom blocks with complete, well-formatted purpose comments following a consistent template, and explain how documentation helps others (and themselves) use the blocks correctly.

Dependencies:
* T11.G5.17: Document block preconditions and postconditions
* T11.G4.16: Test custom blocks independently before integration

---

ID: T11.G5.19
Topic: T11 – Functions & Organization
Skill: Use comments to mark TODO items and known issues
Description: Students use comments to explicitly mark incomplete work, known bugs, and planned improvements in their code, adopting professional development practices. They learn standard comment markers: `// TODO: Add validation for negative scores` for planned work, `// BUG: Sometimes jumps too high when velocity > 20, investigate` for known issues, `// FIXME: This collision detection doesn't work for rotated sprites` for bugs that need fixing, and `// HACK: Temporary workaround until proper save system implemented` for temporary solutions. Students understand that marking issues in code ensures they're not forgotten and helps others understand what's in progress. They review their projects, identify incomplete or problematic areas, and mark them with appropriate comments. They prioritize TODO items and systematically address them.

Assessment example: Students review a project in progress, add TODO, BUG, FIXME, or HACK comments for 4-6 known problems or planned improvements, prioritize them by importance, and address at least 2 of the marked items.

Dependencies:
* T11.G5.18: Document custom blocks with purpose comments
* T11.G3.11: Experiment with pre-made custom blocks to observe parameter effects

---

ID: T11.G5.20
Topic: T11 – Functions & Organization
Skill: Use consistent commenting style across a project
Description: Students establish and consistently follow a commenting style guide throughout a project, including formats for block headers, inline comments, TODO markers, parameter documentation, and section separators. They create a simple style guide (3-5 rules) for their project, such as: (1) all custom blocks start with a purpose comment in this format: `// BlockName: description`, (2) parameters documented in separate comments: `// PARAM name: description`, (3) TODO items use `// TODO: description`, (4) inline comments start with lowercase, (5) section separators use `// ========== SECTION NAME ==========`. They review their code for consistency and update comments to match the style guide. Students understand that consistency makes code more professional and easier to read.

Assessment example: Students create a simple commenting style guide for their project (4-6 rules), apply it consistently to all custom blocks and major scripts (8-12 blocks/scripts total), and explain how consistency improves code readability.

Dependencies:
* T11.G5.18: Document custom blocks with purpose comments
* T11.G5.19: Use comments to mark TODO items and known issues

---

ID: T11.G5.21
Topic: T11 – Functions & Organization
Skill: Balance block granularity (not too small, not too large)
Description: Students develop judgment about appropriate block granularity, understanding that blocks should be neither too small (2-3 blocks doing trivial things, creating clutter) nor too large (50+ blocks doing many different things, hard to understand). They learn to evaluate block size: blocks with 1-3 trivial actions might be too small and should be inlined or combined with related logic; blocks with 40+ blocks doing multiple different things are too large and should be split into focused sub-blocks. Students examine blocks of various sizes, categorize each as too small/just right/too large, and refactor blocks that are poorly sized. They understand that "just right" depends on context: a block is the right size when it has a clear, focused purpose and is neither overwhelming nor pointless.

Assessment example: Given 6-8 custom blocks of varying sizes (some with 2-3 blocks, some with 50+ blocks, some appropriately sized), students categorize each as too small/just right/too large, explain their reasoning, and refactor at least two blocks (merging small ones or splitting large ones).

Dependencies:
* T11.G5.15: Design custom blocks for single responsibility
* T11.G5.14: Refactor a long script into well-named custom blocks

---

ID: T11.G5.22
Topic: T11 – Functions & Organization
Skill: Identify and eliminate duplicate custom blocks
Description: Students review projects with multiple custom blocks to identify blocks that are identical or nearly identical and consolidate duplicates into single, parameterized blocks, applying the DRY (Don't Repeat Yourself) principle. They learn to spot duplication patterns: blocks with identical logic but different hard-coded values can be merged with parameters; blocks with identical structure but minor variations can often be unified with conditional parameters. For example, two blocks `DrawSmallCircle` and `DrawLargeCircle` can be consolidated into one `DrawCircle [size]`. Students refactor duplicates, test that the consolidated version works for all previous use cases, and update all call sites. They understand that eliminating duplication reduces maintenance burden and the risk of inconsistent updates.

Assessment example: Given a project with 3-4 pairs of very similar custom blocks, students identify the similarities, consolidate each pair into a single parameterized block, update all calls to use the new unified blocks, and verify the project still works correctly.

Dependencies:
* T11.G4.14: Extract repeated code into a helper custom block
* T11.G5.14: Refactor a long script into well-named custom blocks

---

ID: T11.G5.23
Topic: T11 – Functions & Organization
Skill: Call custom blocks from multiple sprites
Description: Students create custom blocks that are invoked by multiple sprites in a project, understanding sprite-local vs potentially shared block organization. In CreatiCode, custom blocks are sprite-local (each sprite has its own block definitions), so they learn when to duplicate similar blocks across sprites and when duplication indicates a need for better organization (like using messages or shared variables instead). For example, if three sprites all need `RespondToClick`, they create the block in each sprite but consider whether behavior should be identical or sprite-specific. Students coordinate multi-sprite projects where different sprites call their own versions of similarly-named blocks and verify each sprite's version works correctly.

Assessment example: Students create a project with 3 sprites where at least one custom block concept appears in multiple sprites (e.g., all three sprites have a "Reset" block), and explain when block duplication across sprites is appropriate vs when alternative approaches (messaging, shared variables) would be better.

Dependencies:
* T11.G4.11: Customize block behavior for different sprite types
* T05.G5.01: Coordinate two sprites for a simple interaction

---

ID: T11.G5.24
Topic: T11 – Functions & Organization
Skill: Create custom blocks that modify sprite properties
Description: Students create custom blocks that encapsulate common sprite property changes, bundling related property modifications into reusable, well-named blocks. For example, `define (ResetPlayer)` sets the sprite's position to `(0, 0)`, size to `100%`, rotation to `0`, shows the sprite, and switches to costume `idle`. They understand that grouping related property changes into blocks makes code more readable (the block name explains intent) and more maintainable (changing initialization means editing one block, not many scripts). Students create blocks for common state changes like reset, power-up mode, damage state, victory pose, etc., and use them consistently throughout their project instead of repeating property-change sequences.

Assessment example: Students create 2-3 custom blocks that each modify 3-5 sprite properties (position, size, costume, visibility, rotation, color effects, etc.), document what properties each block changes and why they're grouped together, and use the blocks in at least two different contexts.

Dependencies:
* T11.G4.11: Customize block behavior for different sprite types
* T05.G5.02: Use variables to control sprite behavior

---

ID: T11.G5.25
Topic: T11 – Functions & Organization
Skill: Test custom blocks with edge case parameters
Description: Students systematically test custom blocks with edge cases and boundary values to verify robust behavior: zero, negative numbers, very large numbers, empty strings, boundary values (min/max), and combinations of extreme values. They create test plans listing edge cases for each parameter, run tests with those values, and document expected vs actual behavior. When edge cases cause errors or unexpected results, they add validation to handle them gracefully. For example, testing `DrawPolygon [sides] [size]` with sides=0, sides=1, sides=2, sides=100, size=0, size=negative, size=1000. Students understand that edge case testing finds bugs that normal testing misses and makes blocks more robust and reliable.

Assessment example: Students test 3 custom blocks with at least 3 edge cases each (chosen from: zero, negative, very large, empty, boundary values), document expected behavior for each edge case, identify any bugs found, and add validation or fix bugs as needed.

Dependencies:
* T11.G5.06: Validate parameter values at block start
* T11.G4.20: Combine number and text parameters in one block

---

ID: T11.G5.26
Topic: T11 – Functions & Organization
Skill: Evaluate custom block naming quality
Description: Students review custom block names for clarity, descriptiveness, and consistency, applying naming best practices. Good names: (1) start with verbs for command blocks (DrawSquare, UpdateScore, CheckCollision), (2) are questions for boolean reporters (IsGameOver, CanJump, HasPowerup), (3) are noun phrases for non-boolean reporters (PlayerSpeed, DistanceToEnemy, CurrentLevel), (4) avoid abbreviations unless very common, (5) accurately describe what the block does, (6) follow consistent naming conventions (camelCase or snake_case). Students evaluate existing block names as excellent/good/needs improvement, explain what makes names good or bad, and rename poorly named blocks. They understand that good names make code self-documenting.

Assessment example: Given 8-10 custom blocks with varying name quality (some clear, some vague or misleading), students evaluate each name as excellent/good/needs improvement, explain their reasoning, and provide better names for blocks that need improvement.

Dependencies:
* T11.G4.12: Organize related custom blocks into logical groups
* T11.G5.15: Design custom blocks for single responsibility

---

ID: T11.G5.27
Topic: T11 – Functions & Organization
Skill: Read and explain unfamiliar custom blocks written by others
Description: Students examine custom blocks created by another person and reverse-engineer their purpose, parameters, and implementation, practicing code reading and comprehension. Given blocks with minimal or no comments, they analyze the block's name, parameters, internal logic, and usage to determine what the block does, what each parameter controls, what it returns (for reporters), and any preconditions or side effects. They trace through the code, identify key logic sections, and explain how the block works in their own words. Students document their understanding by writing explanatory comments for the blocks. This skill is essential for collaboration, code review, using shared code, and learning from examples.

Assessment example: Given a project with 3-4 undocumented custom blocks created by someone else (with moderately complex implementations), students analyze each block and write comprehensive explanations: what it does, what parameters mean, what it returns, how it works internally, and any requirements or assumptions they identify from the code.

Dependencies:
* T11.G4.24: Read others' custom blocks and identify improvements
* T11.G5.01.02: Compare call vs report syntax side-by-side
* T11.G4.16: Test custom blocks independently before integration

---

ID: T11.G5.28
Topic: T11 – Functions & Organization
Skill: Create reusable utility blocks for common operations
Description: Students identify common operations they use repeatedly across projects and create reusable utility custom blocks that solve those problems generically. Examples include: `Clamp [value] [min] [max]` (returns value constrained to range), `RandomInRange [min] [max]` (returns random number in range), `DistanceBetween [x1] [y1] [x2] [y2]` (returns distance between points), `FormatTime [seconds]` (returns formatted time string), `IsInRange [value] [min] [max]` (returns true if value is between min and max). Students design these utility blocks to be generic enough to use in multiple contexts, document them thoroughly with examples, and build a personal library of utilities. They understand that building reusable utilities saves time and creates better, more tested code.

Assessment example: Students create 3-4 utility custom reporter blocks for operations they use frequently, document each with purpose, parameters, return value, and usage examples, and demonstrate using them in at least two different contexts within a project.

Dependencies:
* T11.G5.01.01: Call a custom reporter block using report syntax
* T11.G5.15: Design custom blocks for single responsibility

---
