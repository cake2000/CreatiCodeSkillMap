
with open('t09_content.txt', 'a') as f:
    f.write(r'''ID: T09.G5.01
Topic: T09 – Variables & Expressions
Skill: Use multiple variables together in a single expression
Description: **Student task:** Students write expressions that reference 2-3 different variables in one calculation, such as "set area to width * height" or "set total to price * quantity". The focus is on using multiple named variables (not just literals) to compute a result, understanding that variables can reference each other.

Dependencies:
* T09.G4.06: Combine two arithmetic operators in a single expression
* T09.G4.17: Debug wrong variable or update frequency errors

ID: T09.G5.02
Topic: T09 – Variables & Expressions
Skill: Create and use string variables
Description: **Student task:** Students create variables that hold text instead of numbers (e.g., name, message, status). They set string values using "set [myName] to [Alice]" and display them using say blocks or labels.

Dependencies:
* T06.G5.01: Identify standard event patterns in a small game
* T09.G4.07: Store and use user input in a variable

ID: T09.G5.03
Topic: T09 – Variables & Expressions
Skill: Create and use boolean variables with true/false values
Description: **Student task:** Students create variables that hold boolean (true/false) values instead of numbers or text. They set boolean values using logic blocks and use them in conditionals to control program flow. Examples: "set isJumping to true", "if isJumping = true then...". This is more intuitive than using 0/1 for flags.

Dependencies:
* T08.G5.01: Draw decision tree flowchart
* T09.G4.13: Use a flag variable to track state (0/1 or true/false)

ID: T09.G5.04
Topic: T09 – Variables & Expressions
Skill: Identify and choose appropriate variable types for data
Description: **Student task:** Students identify the three main variable types (number, string, boolean) and explain what each can store. They predict what happens when mixing types (e.g., adding a number to a string produces concatenation, not arithmetic). Given a scenario, they choose the appropriate variable type: "score" → number for calculations, "playerName" → string for text, "gameOver" → boolean for true/false state. This skill is essential for avoiding type-related bugs.

Dependencies:
* T09.G5.02: Create and use string variables
* T09.G5.03: Create and use boolean variables with true/false values

ID: T09.G5.05
Topic: T09 – Variables & Expressions
Skill: Join strings using concatenation
Description: **Student task:** Students use the `join` block to combine multiple text values into one string, such as "join [Hello ] [name]" to create personalized messages. They understand that join combines text end-to-end without spaces unless explicitly added.

Dependencies:
* T06.G5.01: Identify standard event patterns in a small game
* T09.G5.02: Create and use string variables

ID: T09.G5.06
Topic: T09 – Variables & Expressions
Skill: Use multi-input join with separator
Description: **Student task:** Students use the advanced join block `join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]` to combine multiple strings with a separator between them. They apply this for creating CSV data, formatted lists, or comma-separated values. Example: join names with ", " to create "Alice, Bob, Carol".

Dependencies:
* T09.G5.05: Join strings using concatenation

ID: T09.G5.07
Topic: T09 – Variables & Expressions
Skill: Use variables as settings to control program behavior
Description: **Student task:** Students create variables that control game or program settings (e.g., player_speed, enemy_count, difficulty_level) and use them throughout the code so changing one value updates the entire program's behavior. This demonstrates the power of variables as configurable parameters.

Dependencies:
* T09.G4.17: Debug wrong variable or update frequency errors
* T11.G5.01: Decompose a problem into logical custom block boundaries

ID: T09.G5.08
Topic: T09 – Variables & Expressions
Skill: Use the accumulator pattern to compute running totals
Description: **Student task:** Students implement the accumulator pattern: initialize a variable to 0, then add values to it repeatedly (in a loop or across events) to compute totals. They understand this pattern is essential for sums, averages, and statistics. Example: "set total to 0", then in loop: "change total by (item value)".

Dependencies:
* T04.G5.01: Identify and classify counter update patterns in code
* T06.G5.01: Identify standard event patterns in a small game
* T07.G5.01: Simulate repeated experiments with a loop
* T09.G4.08: Use a variable as a loop counter
* T09.G4.17: Debug wrong variable or update frequency errors

ID: T09.G5.09
Topic: T09 – Variables & Expressions
Skill: Trace a counter through loop iterations to predict final value
Description: **Student task:** Students trace a script where a counter variable starts at a value and changes inside a repeat loop, tracking its value at each iteration and predicting the final value. Example: "set i to 0, repeat 5 times: change i by 2" results in i = 10. This extends G3.07 tracing to multi-iteration contexts.

Dependencies:
* T02.G5.01: Trace a script with nested loops using debug print
* T04.G5.01: Identify and classify counter update patterns in code
* T07.G5.01: Simulate repeated experiments with a loop
* T09.G4.08: Use a variable as a loop counter

ID: T09.G5.10
Topic: T09 – Variables & Expressions
Skill: Trace code with multiple interacting variables
Description: **Student task:** Students trace code involving 2-3 variables that interact through expressions, recording each variable's value at each step. Focus on understanding how assignment order affects results (e.g., "set a to b" before vs after "set b to 5").

Dependencies:
* T02.G5.01: Trace a script with nested loops using debug print
* T09.G5.01: Use multiple variables together in a single expression
* T09.G5.09: Trace a counter through loop iterations to predict final value

ID: T09.G5.11
Topic: T09 – Variables & Expressions
Skill: Track high score using variable comparison
Description: **Student task:** Students implement a high score system: compare current score to high_score variable, and if current is greater, update high_score. This combines accumulator tracking with conditional updates and persists the "best so far" value.

Dependencies:
* T04.G5.01: Identify and classify counter update patterns in code
* T08.G5.01: Draw decision tree flowchart
* T09.G4.11: Use not equal (≠) and inclusive comparison (≥, ≤) operators
* T09.G5.08: Use the accumulator pattern to compute running totals

ID: T09.G5.12
Topic: T09 – Variables & Expressions
Skill: Apply basic text formatting using string operations
Description: **Student task:** Students combine string variables and join operations to create formatted output messages. They build messages like "Player: [name] - Score: [score]" by joining text literals with variable values. This prepares them for more advanced string operations in Grade 6 by practicing composition of text from multiple parts.

Dependencies:
* T09.G5.06: Use multi-input join with separator
* T09.G5.10: Trace code with multiple interacting variables

ID: T09.G5.13
Topic: T09 – Variables & Expressions
Skill: Use variables for animation state machines
Description: **Student task:** Students create a state variable (e.g., "animation_state" with values like "idle", "walking", "jumping") to control which animation plays and what behaviors are active. They use conditionals to check the state and switch between states based on events. Example: "if animation_state = walking then switch costume to walk1, else if animation_state = jumping then switch costume to jump1". This pattern is essential for character controllers and game entities.

Dependencies:
* T09.G4.13: Use a flag variable to track state (0/1 or true/false)
* T09.G5.02: Create and use string variables
* T09.G5.04: Identify and choose appropriate variable types for data

ID: T09.G5.14
Topic: T09 – Variables & Expressions
Skill: Swap two variable values using a temporary variable
Description: **Student task:** Students implement the classic swap algorithm: create a temporary variable, copy one value to temp, copy second value to first variable, copy temp to second variable. Example: to swap a=3 and b=5, use "set temp to a, set a to b, set b to temp". They understand why a direct swap fails ("set a to b, set b to a" loses the original value of a). This fundamental algorithm pattern is essential for sorting, shuffling, and many other algorithms.

Dependencies:
* T09.G3.08: Copy one variable's value to another variable
* T09.G5.10: Trace code with multiple interacting variables

ID: T09.G5.15
Topic: T09 – Variables & Expressions
Skill: Define and use constant variables for configuration
Description: **Student task:** Students create variables intended to be set once and never changed during program execution (constants). They use ALL_CAPS naming convention to indicate constants (e.g., MAX_LIVES, GRAVITY, SCREEN_WIDTH) and set them at program start. They understand constants make code more maintainable—changing one constant updates all places it's used. Example: "set JUMP_HEIGHT to 50" used throughout the code; changing it once changes all jumps. Students contrast constants with variables that change during execution.

Dependencies:
* T09.G5.07: Use variables as settings to control program behavior
* T09.G5.10: Trace code with multiple interacting variables

ID: T09.G5.16
Topic: T09 – Variables & Expressions
Skill: Refactor repeated literal values into named variables
Description: **Student task:** Students identify code where the same literal value appears multiple times (e.g., "move 50 steps" appears in 5 places) and refactor by creating a named variable (e.g., "set moveDistance to 50") and replacing all occurrences with the variable. They understand benefits: (1) changing the value in one place updates everywhere, (2) the name documents what the value means, (3) reduces chance of inconsistent updates. This "Don't Repeat Yourself" (DRY) principle is fundamental to maintainable code.

Dependencies:
* T09.G5.07: Use variables as settings to control program behavior
* T09.G5.15: Define and use constant variables for configuration

ID: T09.G5.17
Topic: T09 – Variables & Expressions
Skill: Design variable update rules for game mechanics
Description: **Student task:** Students design the variable logic for common game mechanics by specifying: (1) what variables are needed, (2) their initial values, (3) when and how they change, and (4) what conditions check them. Examples: health system (health starts at 100, decreases when hit, can't go below 0 or above max, game over when 0), scoring system (score starts at 0, increases on collect, displays on stage), or power-up system (hasPowerUp starts false, becomes true on collect, enables special ability, expires after timer). This design-before-code approach builds planning skills.

Dependencies:
* T09.G5.13: Use variables for animation state machines
* T09.G5.15: Define and use constant variables for configuration
* T09.G4.22: Implement boundary checking with min and max guards

ID: T09.G5.18
Topic: T09 – Variables & Expressions
Skill: Debug variables in loops using step-by-step console tracing
Description: **Student task:** Students debug loop-based variable bugs by adding console output inside loops to trace values at each iteration. They identify: (1) initialization errors (wrong starting value), (2) update errors (wrong increment), (3) off-by-one errors (loop runs wrong number of times). Example: "repeat 5: change counter by 2, console log [counter]" helps verify counter increases correctly. This extends G3.12 console debugging to loops.

Dependencies:
* T09.G3.12: Use console output to inspect variable values during execution
* T09.G5.09: Trace a counter through loop iterations to predict final value

ID: T09.G5.19
Topic: T09 – Variables & Expressions
Skill: Integrate table variables with regular variables for structured data
Description: **Student task:** Students use table variables (from T10 Lists & Tables) to store collections of related data, then extract values into regular variables for processing. Example: store player stats in a table (name, score, level columns), then "set playerName to item 1 of row 1 of statsTable" to extract a specific player's name. They understand when to use tables (for collections) vs regular variables (for single values), and how to move data between them.

Dependencies:
* T09.G5.07: Use variables as settings to control program behavior
* T09.G5.10: Trace code with multiple interacting variables

ID: T09.G5.20
Topic: T09 – Variables & Expressions
Skill: Critique variable naming in given code and improve it
Description: **Student task:** Students review code with poor variable names and suggest improvements. Given code with names like "x", "temp1", "data", "thing", they identify which names are unclear and propose better alternatives. They explain WHY each suggestion is better: "x should be playerX because it stores the player's horizontal position." This skill develops code review abilities and reinforces naming best practices by analyzing others' code, not just writing their own.

Dependencies:
* T09.G3.11: Explain why descriptive variable names improve code readability
* T09.G5.15: Define and use constant variables for configuration

ID: T09.G5.21
Topic: T09 – Variables & Expressions
Skill: Order expression evaluation steps explicitly
Description: **Student task:** Students are given a complex expression and must number the evaluation steps in correct order. Example: "set result to (a + b) * (c - d)" with a=2, b=3, c=10, d=4. Steps to order: (A) Compute a+b=5, (B) Compute c-d=6, (C) Multiply results=30, (D) Store in result. Correct order: A and B can be in either order (both first), then C, then D. This explicit ordering builds deep understanding of expression evaluation, especially recognizing that independent subexpressions can evaluate in any order.

Dependencies:
* T09.G4.27: Predict result of nested operator blocks visually
* T09.G5.10: Trace code with multiple interacting variables

ID: T09.G5.22
Topic: T09 – Variables & Expressions
Skill: Design variable schema for a mini-project before coding
Description: **Student task:** Students plan all variables needed for a small project (5-10 variables) BEFORE writing any code. They create a specification document listing: (1) variable name, (2) what it stores, (3) initial value, (4) when/how it changes, (5) where it's used. Example: For a "Catch the Falling Objects" game, plan variables for score, lives, speed, gameOver flag, highScore. They review and refine their schema, then implement the code. This design-first approach reduces bugs and teaches professional planning practices.

Dependencies:
* T09.G4.24: Plan variable lifecycle before coding
* T09.G5.17: Design variable update rules for game mechanics

ID: T09.G5.23
Topic: T09 – Variables & Expressions
Skill: Build compound expressions step-by-step from requirements
Description: **Student task:** Students translate multi-part requirements into compound expressions by building them incrementally. Example requirement: "Score is base points (10) times multiplier, plus bonus if bonus is active, minus penalty if penalty is active." Students identify the parts, build each subexpression, then combine: "set score to (10 * multiplier) + (if bonusActive then bonus else 0) - (if penaltyActive then penalty else 0)". They verify their expression handles all cases correctly. This skill bridges the gap between requirements and implementation.

Dependencies:
* T09.G5.01: Use multiple variables together in a single expression
* T09.G5.21: Order expression evaluation steps explicitly

ID: T09.G5.24
Topic: T09 – Variables & Expressions
Skill: Identify variable invariants that must always be true
Description: **Student task:** Students identify conditions that should ALWAYS be true about their variables (invariants) and explain why. Examples: "score is always >= 0" (score can't be negative), "lives is always between 0 and maxLives", "currentLevel <= totalLevels". They practice: (1) Stating invariants for given code, (2) Checking if code maintains invariants, (3) Finding code that BREAKS invariants. This introduces formal reasoning about program correctness - a key skill for writing bug-free code. Example: Given health system code, identify the invariant "0 <= health <= maxHealth" and check if all update operations maintain it.

Dependencies:
* T09.G4.22: Implement boundary checking with min and max guards
* T09.G5.17: Design variable update rules for game mechanics

ID: T09.G5.25
Topic: T09 – Variables & Expressions
Skill: Rewrite expressions for clarity vs efficiency
Description: **Student task:** Students compare equivalent expressions and discuss trade-offs between clarity and efficiency. Example: "distance = sqrt(dx*dx + dy*dy)" is efficient but "dxSquared = dx*dx; dySquared = dy*dy; sumSquares = dxSquared + dySquared; distance = sqrt(sumSquares)" is clearer for debugging. They practice: (1) Rewriting compact expressions into step-by-step versions for clarity, (2) Combining step-by-step code into compact expressions for efficiency, (3) Deciding when each style is appropriate (prototyping vs production, simple vs complex logic). This meta-skill helps students make informed coding style decisions.

Dependencies:
* T09.G4.28: Write multi-step calculations as intermediate variable assignments
* T09.G5.21: Order expression evaluation steps explicitly

ID: T09.G5.26
Topic: T09 – Variables & Expressions
Skill: Create minimal reproducible examples for variable bugs
Description: **Student task:** Students learn to isolate variable bugs by creating minimal reproducible examples (MREs). Given a complex program with a bug, they: (1) Identify which variables are involved, (2) Remove unrelated code while preserving the bug, (3) Create the smallest program that still shows the problem, (4) Document exact steps to reproduce. Example: "My score doesn't update correctly" gets reduced to 5-10 blocks showing just the scoring logic with the bug. This professional debugging skill helps students get better help and understand bugs more deeply.

Dependencies:
* T09.G5.18: Debug variables in loops using step-by-step console tracing
* T09.G5.22: Design variable schema for a mini-project before coding

ID: T09.G5.27
Topic: T09 – Variables & Expressions
Skill: Trace counter through complex branching logic
Description: **Student task:** Students trace counter variables through code with nested conditionals and multiple branches. Given code like: "if touching enemy then (if hasShield then change shield by -1, else change health by -1)", they trace all possible paths and predict counter values for each scenario. They create trace tables with columns for each variable and rows for each execution path. This extends G5.09 loop tracing to conditional branching contexts.

Dependencies:
* T09.G4.30: Implement count-up and count-down patterns with conditionals
* T09.G5.09: Trace a counter through loop iterations to predict final value
* T09.G5.10: Trace code with multiple interacting variables

ID: T09.G5.28
Topic: T09 – Variables & Expressions
Skill: Debug wrong operand order errors in expressions
Description: **Student task:** Students identify and fix bugs where operands are in the wrong order. Given "set change to payment - price" (should be "price - payment" if calculating what customer owes, or correct if calculating change given), they analyze the context to determine correct operand order. They practice: (1) Subtraction order bugs (a-b vs b-a gives different results), (2) Division order bugs (a/b vs b/a), (3) Understanding that order matters for - and / but not for + and *. This precision skill prevents subtle calculation errors.

Dependencies:
* T09.G4.31: Debug wrong operator errors in expressions
* T09.G5.01: Use multiple variables together in a single expression

ID: T09.G5.29
Topic: T09 – Variables & Expressions
Skill: React to variable changes with when-variable-changed event
Description: **Student task:** Students use CreatiCode's `when variable [name] changed` event block to trigger scripts automatically whenever a specific variable's value changes. This enables reactive programming patterns where scripts respond to state changes without polling. Examples: update a UI label when score changes, play sound when health drops, trigger animation when level increases. Students compare this approach to a "forever loop checking if variable changed" and understand the efficiency benefits.

Dependencies:
* T09.G5.07: Use variables as settings to control program behavior
* T09.G5.17: Design variable update rules for game mechanics

ID: T09.G5.30
Topic: T09 – Variables & Expressions
Skill: Control 3D object properties with variables
Description: **Student task:** Students use variables to control 3D object properties dynamically. They link a variable (e.g., "scaleFactor", "rotationX") to 3D blocks like `set size to [scaleFactor]` or `turn x by [rotationX]`. They use loops to update the variable, creating dynamic 3D animations like a pulsing sphere or rotating cube. This connects variables to the 3D world.

Dependencies:
* T09.G5.07: Use variables as settings to control program behavior
* T09.G5.13: Use variables for animation state machines

ID: T09.G6.01
Topic: T09 – Variables & Expressions
Skill: Model real-world quantities using variables and formulas
Description: **Student task:** Students create variables representing real-world quantities (e.g., distance, time, money, temperature) and update them using formulas. Examples: total_cost = price × quantity, distance = speed × time. This connects math formulas to programming.

Dependencies:
* T09.G5.08: Use the accumulator pattern to compute running totals
* T09.G5.10: Trace code with multiple interacting variables

ID: T09.G6.02
Topic: T09 – Variables & Expressions
Skill: Apply operator precedence rules (PEMDAS) in expressions
Description: **Student task:** Students write and evaluate expressions mixing addition/subtraction with multiplication/division, understanding that * and / are evaluated before + and -. They learn to read and predict evaluation order in expressions like "a + b * c" (multiply first, then add). This focuses on understanding the default order of operations.

Dependencies:
* T09.G5.10: Trace code with multiple interacting variables

ID: T09.G6.03
Topic: T09 – Variables & Expressions
Skill: Use parentheses to override operator precedence
Description: **Student task:** Students use parentheses to control evaluation order in expressions, overriding default PEMDAS precedence. They predict and explain different results from "(a + b) * c" vs "a + b * c". This enables them to write expressions that match their intended calculation order.

Dependencies:
* T09.G6.02: Apply operator precedence rules (PEMDAS) in expressions

ID: T09.G6.04
Topic: T09 – Variables & Expressions
Skill: Use exponents (^) and modulo (%) operators
Description: **Student task:** Students use the power operator (^) to compute squares, cubes, and other powers (e.g., "set area to side ^ 2"), and the modulo operator (% or mod) to find remainders from division. They apply modulo to practical tasks like determining odd/even numbers (n mod 2), cycling through values, or creating repeating patterns. Example: "if score mod 10 = 0" to trigger events every 10 points.

Dependencies:
* T09.G6.03: Use parentheses to override operator precedence

ID: T09.G6.05
Topic: T09 – Variables & Expressions
Skill: Use string length and join operations
Description: **Student task:** Students use `length of [string]` to get the character count of text and combine it with join operations for validation and formatting. They apply this to validate input (e.g., check password length) and create formatted output. Example: "if length of [name] > 10".

Dependencies:
* T09.G5.05: Join strings using concatenation

ID: T09.G6.06
Topic: T09 – Variables & Expressions
Skill: Extract characters with letter-of operator
Description: **Student task:** Students use the `letter (position) of [text]` block to extract a single character from a specific position in a string. They apply this for character-by-character text processing, validation, or creating acronyms. Example: "letter 1 of [name]" to get first initial.

Dependencies:
* T09.G6.05: Use string length and join operations

ID: T09.G6.07
Topic: T09 – Variables & Expressions
Skill: Find and extract text with position and substring operators
Description: **Student task:** Students use `position of [search] in [text]` to find where a substring appears (returns position number, or 0 if not found), and `substring of [text] from position (start) to (end)` to extract parts of strings. They apply this for text searching, parsing, and extracting portions like initials or file extensions. Example: check if email contains "@", extract first name from full name.

Dependencies:
* T09.G6.06: Extract characters with letter-of operator

ID: T09.G6.08
Topic: T09 – Variables & Expressions
Skill: Transform text with replace, split, and case operators
Description: **Student task:** Students use `replace [old] with [new] in [text]` to substitute text, `split [text] by [delimiter]` to break strings into lists, and `[CASE v] of text [T]` for uppercase/lowercase conversion. They apply these for text normalization, parsing CSV data, formatting output, and case-insensitive comparisons. Example: replace all spaces with underscores, split "apple,banana,cherry" by ",", convert to uppercase for shouting effects.

Dependencies:
* T09.G6.07: Find and extract text with position and substring operators

ID: T09.G6.09
Topic: T09 – Variables & Expressions
Skill: Use temporary variables for multi-step calculations
Description: **Student task:** Students create temporary variables to hold intermediate results in multi-step calculations. For example, when calculating average: first compute total, then count, then divide total by count. This improves code readability and enables debugging by inspecting intermediate states.

Dependencies:
* T09.G5.08: Use the accumulator pattern to compute running totals
* T09.G6.03: Use parentheses to override operator precedence

ID: T09.G6.10
Topic: T09 – Variables & Expressions
Skill: Trace variable values across multiple event handlers
Description: **Student task:** Students trace how variables maintain their values across different event handlers and broadcasts. They predict the value of a variable after a sequence of events: one script sets a variable and broadcasts a message, another script receiving that broadcast reads the updated value. This demonstrates coordination between different parts of a program through shared variable state.

Dependencies:
* T09.G5.07: Use variables as settings to control program behavior

ID: T09.G6.11
Topic: T09 – Variables & Expressions
Skill: Debug off-by-one and comparison operator errors
Description: **Student task:** Students debug scripts where variables control program flow through conditionals and loops. Common bugs include: wrong comparison operator (using > instead of >=), off-by-one errors in loop conditions, or variables not being reset. This extends G4.17 by focusing on control-flow bugs.

Dependencies:
* T09.G4.17: Debug wrong variable or update frequency errors
* T09.G5.10: Trace code with multiple interacting variables

ID: T09.G6.12
Topic: T09 – Variables & Expressions
Skill: Use variables to parameterize AI prompts dynamically
Description: **Student task:** Students create variables to store user preferences, settings, or context information, then use these variables to construct dynamic AI prompts. Examples: "set style to [answer]", then "ask AI to draw [subject] in [style] style", or "set difficulty to [hard]", then "ask AI to generate [difficulty] math problem". This demonstrates how variables enable personalized and adaptive AI interactions.

Dependencies:
* T09.G5.07: Use variables as settings to control program behavior
* T09.G5.12: Apply basic text formatting using string operations

ID: T09.G6.13
Topic: T09 – Variables & Expressions
Skill: Use the expression calculator block for complex formulas
Description: **Student task:** Students use CreatiCode's `calculate expression [text]` block to evaluate mathematical expressions written as text strings. This allows for dynamic formula evaluation where the expression itself can be constructed or modified at runtime. Examples: "calculate expression [(1 + 1) * (2^4)]" returns 32, or building a formula string from user input like "calculate expression [join [price] [* 1.08]]" for tax calculation. Students understand when to use this vs regular operator blocks.

Dependencies:
* T09.G5.12: Apply basic text formatting using string operations
* T09.G6.04: Use exponents (^) and modulo (%) operators

ID: T09.G6.14
Topic: T09 – Variables & Expressions
Skill: Build dynamic UI with widget-bound variables
Description: **Student task:** Students connect variables to CreatiCode UI widgets (labels, text inputs, sliders) to create interactive interfaces. They use variables to display values in label widgets, read user input from text fields into variables, and bind slider widgets to control variable values. Example: create a "Speed: [speed]" label that updates automatically, or use a slider widget to let users adjust difficulty level stored in a variable. This pattern is essential for building user-friendly applications.

Dependencies:
* T09.G5.07: Use variables as settings to control program behavior
* T09.G6.10: Trace variable values across multiple event handlers

ID: T09.G6.15
Topic: T09 – Variables & Expressions
Skill: Convert between data types explicitly
Description: **Student task:** Students explicitly convert between data types: number to string using join (e.g., "join [] [score]" converts score to text), string to number using arithmetic (e.g., "set num to [textValue] + 0" or explicit conversion blocks), and understand implicit type coercion. They predict and debug type-related errors such as comparing "5" (string) with 5 (number) or concatenating numbers unintentionally. Example: converting user input from text to number before doing calculations.

Dependencies:
* T09.G5.04: Identify and choose appropriate variable types for data
* T09.G6.05: Use string length and join operations

ID: T09.G6.16
Topic: T09 – Variables & Expressions
Skill: Validate text patterns with includes/starts/ends operators
Description: **Student task:** Students use CreatiCode's text validation operators to check string patterns: `[text] includes [search]` to check if text contains a substring, `[text] starts with [prefix]` to check beginning, and `[text] ends with [suffix]` to check ending. They apply these for input validation and filtering. Examples: check if email includes "@", check if filename ends with ".png", check if command starts with "/". These operators support case-insensitive matching with the ignore case option.

Dependencies:
* T09.G5.05: Join strings using concatenation
* T09.G6.07: Find and extract text with position and substring operators

ID: T09.G6.17
Topic: T09 – Variables & Expressions
Skill: Implement undo functionality using variable history
Description: **Student task:** Students implement a simple undo feature by storing the previous value of a variable before changing it. Pattern: "set previousValue to currentValue" before "set currentValue to newValue", then undo restores with "set currentValue to previousValue". They extend this to store multiple previous values in a list for multi-level undo. Example: in a drawing app, store previous x,y positions to undo the last move; in a game editor, store previous object positions. This introduces the concept of state history for reversible actions.

Dependencies:
* T09.G5.14: Swap two variable values using a temporary variable
* T09.G6.09: Use temporary variables for multi-step calculations

ID: T09.G6.18
Topic: T09 – Variables & Expressions
Skill: Trace variables through nested conditional branches
Description: **Student task:** Students trace code with nested if/else structures (2-3 levels deep) to predict variable values. They create a trace table showing the variable's value at each decision point and through each branch. Example: if score > 100 { if hasBonus { multiplier = 3 } else { multiplier = 2 } } else { multiplier = 1 } - trace what multiplier becomes for different score and hasBonus values. This prepares for debugging complex conditional logic.

Dependencies:
* T09.G5.10: Trace code with multiple interacting variables
* T09.G6.11: Debug off-by-one and comparison operator errors

ID: T09.G6.19
Topic: T09 – Variables & Expressions
Skill: Model complex real-world systems with multiple variable types
Description: **Student task:** Students design variable structures for complex scenarios requiring numbers, strings, and booleans together. Examples: weather system (temperature:number, condition:string, isRaining:boolean), character RPG stats (name:string, health:number, level:number, isAlive:boolean). They justify their type choices and explain relationships between variables. This synthesis skill demonstrates mastery of variable types working together.

Dependencies:
* T09.G5.04: Identify and choose appropriate variable types for data
* T09.G6.01: Model real-world quantities using variables and formulas
* T09.G6.15: Convert between data types explicitly

ID: T09.G6.20
Topic: T09 – Variables & Expressions
Skill: Trace AI prompt variables to debug unexpected AI outputs
Description: **Student task:** Students debug AI interactions where variables in prompts cause unexpected outputs. They trace how variable values are inserted into AI prompt strings and identify problems: (1) variable contains unexpected value, (2) variable is undefined/empty, (3) variable formatting creates invalid prompts. Example: "Generate a story about [character]" gives weird results because character variable = "undefined". They add console logging to inspect variable values before sending to AI. This combines variable debugging with AI integration skills.

Dependencies:
* T09.G5.18: Debug variables in loops using step-by-step console tracing
* T09.G6.12: Use variables to parameterize AI prompts dynamically

ID: T09.G6.21
Topic: T09 – Variables & Expressions
Skill: Debug expressions with type coercion errors
Description: **Student task:** Students identify and fix bugs caused by implicit type conversion in expressions. Examples: "5" + "3" = "53" (string concatenation, not 8), comparing "10" < "9" (string comparison, true because "1" < "9" lexicographically). They trace expression evaluation to identify where type coercion causes unexpected behavior, then apply explicit conversions to fix. This skill is essential for robust code that handles user input and mixed data sources.

Dependencies:
* T09.G6.05: Use string length and join operations
* T09.G6.15: Convert between data types explicitly

ID: T09.G6.22
Topic: T09 – Variables & Expressions
Skill: Review and improve variable design in existing code
Description: **Student task:** Students perform code review focused on variable usage in a 20-50 block program. They identify issues: (1) poor naming, (2) missing initialization, (3) unused variables, (4) variables that could be constants, (5) scope problems, (6) unclear purpose. They document findings and suggest specific improvements with reasoning. Example: "The variable 'x' on line 5 should be renamed 'enemySpawnX' because it stores where enemies appear." This professional skill prepares students for collaborative development and code maintenance.

Dependencies:
* T09.G5.20: Critique variable naming in given code and improve it
* T09.G6.11: Debug off-by-one and comparison operator errors

ID: T09.G6.23
Topic: T09 – Variables & Expressions
Skill: Simplify complex expressions using algebraic properties
Description: **Student task:** Students recognize and apply algebraic simplifications to expressions: "x + x + x" → "x * 3", "x * 1" → "x", "x + 0" → "x", "x * 0" → "0", "x - x" → "0". They identify expressions in code that can be simplified and explain the mathematical property used. Example: "set speed to baseSpeed + 0" should be "set speed to baseSpeed". This skill builds mathematical reasoning and code optimization awareness.

Dependencies:
* T09.G6.02: Apply operator precedence rules (PEMDAS) in expressions
* T09.G6.04: Use exponents (^) and modulo (%) operators

ID: T09.G6.24
Topic: T09 – Variables & Expressions
Skill: Use variables to implement stateful UI behavior
Description: **Student task:** Students use variables to track UI state and create responsive interfaces. Examples: toggle buttons (isMenuOpen), radio button selection (selectedOption), multi-step forms (currentStep), input validation state (isEmailValid). They implement complete UI patterns where user interactions update state variables, which in turn control what's displayed. This connects variable management to practical application development.

Dependencies:
* T09.G6.10: Trace variable values across multiple event handlers
* T09.G6.14: Build dynamic UI with widget-bound variables

ID: T09.G6.25
Topic: T09 – Variables & Expressions
Skill: Write preconditions and postconditions for variable updates
Description: **Student task:** Students formalize what must be true BEFORE (precondition) and AFTER (postcondition) variable operations. Examples: For "change health by -damage", precondition: "damage >= 0", postcondition: "health decreased by damage amount". They practice: (1) Writing preconditions for functions that update variables, (2) Writing postconditions that describe the effect, (3) Identifying when preconditions are violated (causing bugs). This formal thinking prevents bugs by making assumptions explicit. Example: "setLevel(newLevel)" has precondition "newLevel > 0 AND newLevel <= maxLevels" and postcondition "currentLevel == newLevel".

Dependencies:
* T09.G5.24: Identify variable invariants that must always be true
* T09.G6.11: Debug off-by-one and comparison operator errors

ID: T09.G6.26
Topic: T09 – Variables & Expressions
Skill: Refactor global variables into structured data
Description: **Student task:** Students identify when multiple related global variables should be grouped into structured data. Given scattered variables like "player_x, player_y, player_health, player_score, player_name", they recognize these belong together and refactor using naming conventions (player_*) or table variables. They practice: (1) Identifying variable clusters that represent one entity, (2) Planning how to group them (naming prefix, table row), (3) Refactoring existing code to use the grouped structure. This professional refactoring skill reduces bugs from inconsistent updates and prepares for object-oriented thinking.

Dependencies:
* T09.G5.19: Integrate table variables with regular variables for structured data
* T09.G6.22: Review and improve variable design in existing code

ID: T09.G6.27
Topic: T09 – Variables & Expressions
Skill: Analyze expression complexity and suggest simplifications
Description: **Student task:** Students analyze expressions for unnecessary complexity and suggest simplifications. They identify: (1) Redundant operations (x * 1, x + 0), (2) Repeated subexpressions that could be stored in a variable, (3) Overly complex expressions that could be split, (4) Mathematical simplifications (x * 2 + x * 3 = x * 5). Given complex expression code, they propose specific simplifications with reasoning. Example: "set result to (a * b) + (a * b) + (a * b)" simplifies to "set temp to a * b; set result to temp * 3". This optimization skill builds mathematical reasoning and code efficiency awareness.

Dependencies:
* T09.G5.25: Rewrite expressions for clarity vs efficiency
* T09.G6.23: Simplify complex expressions using algebraic properties

ID: T09.G6.28
Topic: T09 – Variables & Expressions
Skill: Debug type mismatch errors in expressions
Description: **Student task:** Students identify and fix bugs caused by mixing incompatible types in expressions. Given code where a string variable is used in arithmetic ("set result to playerName + 10") or a number is treated as a string, they trace the problem and apply fixes. They practice: (1) Recognizing type error symptoms (unexpected concatenation, NaN results), (2) Adding explicit type conversions, (3) Validating data types before operations. This extends G6.21 type coercion debugging to cover explicit type mismatches that cause expression failures.

Dependencies:
* T09.G5.28: Debug wrong operand order errors in expressions
* T09.G6.15: Convert between data types explicitly
* T09.G6.21: Debug expressions with type coercion errors

ID: T09.G6.29
Topic: T09 – Variables & Expressions
Skill: Store and validate AI-generated numeric outputs
Description: **Student task:** Students capture numeric outputs from AI blocks (ChatGPT, speech recognition, sensors) in variables and validate them before use. They implement patterns: (1) Parse AI text response to extract numbers using string operations, (2) Check if value is within expected range (e.g., 0-100 for percentage), (3) Handle invalid outputs gracefully (set default, ask again, show error). Example: Ask AI "pick a number 1-10", store response, validate it's actually a number in range before using. This prepares for robust AI integration.

Dependencies:
* T09.G6.12: Use variables to parameterize AI prompts dynamically
* T09.G6.15: Convert between data types explicitly
* T09.G6.28: Debug type mismatch errors in expressions

ID: T09.G6.30
Topic: T09 – Variables & Expressions
Skill: Use variables to store Speech Recognition results
Description: **Student task:** Students use the `text from speech` reporter block and store its value in a variable for processing. They create scripts that listen for speech, save the result to a "userCommand" variable, and then use string matching to decide what to do. Example: "if userCommand = 'jump' then...". This connects AI input (speech) to variable storage and control flow.

Dependencies:
* T09.G6.05: Use string length and join operations
* T09.G6.16: Validate text patterns with includes/starts/ends operators

''')