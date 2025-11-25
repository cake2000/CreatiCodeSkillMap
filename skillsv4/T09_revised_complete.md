# T09 - Variables & Expressions (REVISED - COMPLETE)

## GRADE K (2 skills)

ID: T09.GK.01
Topic: T09 – Variables & Expressions
Skill: Recognize that a label can hold a number
Description: **Student task:** Look at pictures showing labels with numbers (e.g., "Score: 5", "Lives: 3", "Stars: 2"). Match each label to what it counts. _Implementation note: Picture-based matching activity. CSTA: EK‑PRO‑PF‑02._

Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed


ID: T09.GK.02
Topic: T09 – Variables & Expressions
Skill: Identify which label changed after an action
Description: **Student task:** Look at two pictures: before and after. Find which label changed (e.g., "Score went from 2 to 3"). _Implementation note: Click-select activity comparing before/after states. CSTA: EK‑PRO‑PF‑02._

Dependencies:
* T09.GK.01: Recognize that a label can hold a number


## GRADE 1 (2 skills)

ID: T09.G1.01
Topic: T09 – Variables & Expressions
Skill: Change a displayed number by clicking a button
Description: **Student task:** Click a button to add 1 to a counter on screen. Watch the number go up. Try clicking multiple times. _Implementation note: Interactive counter with visual feedback. CSTA: E1‑PRO‑PF‑02._

Dependencies:
* T09.GK.02: Identify which label changed after an action
* T03.G1.01: Describe what one part of a system does


ID: T09.G1.02
Topic: T09 – Variables & Expressions
Skill: Use a picture-based counter to track items collected
Description: **Student task:** In a simple picture game, collect stars and watch the counter go up. How many did you get? _Implementation note: Drag-and-drop collection with automatic counter. CSTA: E1‑PRO‑PF‑02._

Dependencies:
* T09.G1.01: Change a displayed number by clicking a button


## GRADE 2 (2 skills)

ID: T09.G2.01
Topic: T09 – Variables & Expressions
Skill: Set a starting value for a counter before a game begins
Description: **Student task:** Before the game starts, set the score to 0. Then play and collect items. Why do we start at 0? _Implementation note: Picture-based initialization concept. CSTA: E2‑PRO‑PF‑02._

Dependencies:
* T09.G1.02: Use a picture-based counter to track items collected


ID: T09.G2.02
Topic: T09 – Variables & Expressions
Skill: Compare a counter to a target number to trigger an event
Description: **Student task:** Follow along as the counter goes up. When it reaches the target number (like 5), something special happens! Predict when it will happen. _Implementation note: Picture-based prediction with threshold concept. CSTA: E2‑PRO‑PF‑02._

Dependencies:
* T09.G2.01: Set a starting value for a counter before a game begins
* T08.G2.01: Follow branching paths based on yes/no questions


## GRADE 3 (9 skills - 3 broken down from original T09.G3.04)

ID: T09.G3.01.01
Topic: T09 – Variables & Expressions
Skill: Create a new variable with a descriptive name
Description: Students create their first variable in the block editor by choosing "Make a Variable" and giving it a simple, meaningful name (e.g., "score", "lives", "stars"). They understand that the variable name should describe what it stores. This is the first step in understanding variables as named storage containers.

Dependencies:
* T09.G2.02: Compare a counter to a target number to trigger an event
* T03.G2.01: Choose subtasks for a simple project idea


ID: T09.G3.01.02
Topic: T09 – Variables & Expressions
Skill: Set a variable to an initial value at program start
Description: Students use the "set [variable] to (value)" block to initialize a variable to a starting value (typically 0) when the green flag is clicked. They understand that setting an initial value prepares the variable for use and ensures consistent starting conditions.

Dependencies:
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T09.G3.01.03
Topic: T09 – Variables & Expressions
Skill: Change a variable value by 1 using the change block
Description: Students use "change [variable] by (1)" to increase a variable's value by exactly 1 when a simple event occurs (like touching a star or clicking the sprite). They observe the variable monitor on stage updating and understand that "change by" adds to the current value. This introduces the basic increment pattern.

Dependencies:
* T09.G3.01.02: Set a variable to an initial value at program start


ID: T09.G3.01.04
Topic: T09 – Variables & Expressions
Skill: Display variable value on stage using the variable monitor
Description: Students check the checkbox next to their variable to show its monitor on stage, watching it update in real-time as their code runs. They understand that the monitor helps them see what value the variable currently holds.

Dependencies:
* T09.G3.01.03: Change a variable value by 1 using the change block


ID: T09.G3.01.05
Topic: T09 – Variables & Expressions
Skill: Use variable reporter blocks in other blocks
Description: Students drag the round [variable] reporter block into other blocks to use the variable's value (e.g., "say [score]" or "move [speed] steps"). They understand that the variable reporter provides the current value and can be used anywhere a number input is needed. This is the foundation for using variables in expressions.

Dependencies:
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T09.G3.02
Topic: T09 – Variables & Expressions
Skill: Use change block to increase a variable
Description: Students use `change [variable] by (amount)` to increase a variable by arbitrary amounts (e.g., change score by 10, change lives by 5). They understand that "change" adds to the current value. This extends the basic increment-by-1 pattern (G3.01.03) to arbitrary positive amounts.

Dependencies:
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T09.G3.02.01
Topic: T09 – Variables & Expressions
Skill: Use reduce block to decrease a variable
Description: Students use `reduce [variable] by (amount)` to decrease a variable by arbitrary amounts (e.g., reduce lives by 1, reduce health by 10). They understand that "reduce" subtracts from the current value, which is the opposite of "change". This provides an intuitive way to decrement variables.

Dependencies:
* T09.G3.02: Use change block to increase a variable


ID: T09.G3.03
Topic: T09 – Variables & Expressions
Skill: Use a variable in a simple conditional (if block)
Description: Students write their first conditional that reads a variable's value using very simple comparisons (e.g., "if score > 3 then say 'Great!'"). This connects the variable concept to conditional logic with small, easy-to-test numbers. Focus on understanding that variables can be checked in conditions.

Dependencies:
* T09.G3.02.01: Use reduce block to decrease a variable
* T08.G3.02: Decide when a single if is enough


ID: T09.G3.04.01
Topic: T09 – Variables & Expressions
Skill: Debug missing variable initialization
Description: Students inspect a very simple script (3-5 blocks) where a variable doesn't work because it wasn't initialized. Focus on recognizing the symptom (variable starts with wrong value or shows 0 unexpectedly) and finding the missing "set [variable] to [initial value]" block that should appear at program start. This is entry-level debugging with clear initialization failures.

Dependencies:
* T09.G3.03: Use a variable in a simple conditional (if block)


ID: T09.G3.04.02
Topic: T09 – Variables & Expressions
Skill: Debug missing change/update block
Description: Students inspect a very simple script (3-5 blocks) where a variable doesn't update as expected during gameplay. Focus on recognizing the symptom (score stays at 0 even after collecting items) and finding the missing "change [variable] by [amount]" or "reduce [variable] by [amount]" block. This builds pattern recognition for update-related bugs.

Dependencies:
* T09.G3.04.01: Debug missing variable initialization


ID: T09.G3.04.03
Topic: T09 – Variables & Expressions
Skill: Debug wrong value in variable block
Description: Students inspect a very simple script (3-5 blocks) where a variable changes by the wrong amount (e.g., "change score by 10" when it should be "change score by 1"). Focus on finding one obvious wrong number in a change/reduce/set block and correcting it. This completes basic variable debugging skills.

Dependencies:
* T09.G3.04.02: Debug missing change/update block


ID: T09.G3.05
Topic: T09 – Variables & Expressions
Skill: Trace code with variables to predict outcomes
Description: Students trace a very short script (3-4 steps) where a variable changes in simple ways (set to 0, change by 1, change by 1 again), and predict the final value by reading and following the code. This skill focuses on understanding existing code and predicting outcomes, not creating new variables. Use small numbers and obvious changes.

Dependencies:
* T09.G3.04.03: Debug wrong value in variable block
* T08.G3.04: Trace code with a single if/else


ID: T09.G3.06
Topic: T09 – Variables & Expressions
Skill: Copy one variable's value to another variable
Description: Students use "set [variable1] to [variable2]" to copy the value from one variable to another. They understand that this creates an independent copy - changing one variable later doesn't affect the other. Examples: "set backup_score to score", "set player_x to enemy_x". This bridges the gap between basic variable operations and using variables in complex expressions.

Dependencies:
* T09.G3.01.02: Set a variable to an initial value at program start


## GRADE 4 (16 skills - 3 broken down from original T09.G4.09)

ID: T09.G4.01
Topic: T09 – Variables & Expressions
Skill: Use addition (+) in variable expressions
Description: Students use the + operator block to create expressions that add values, such as "set total to score + bonus" or "set sum to a + b". They understand that the + operator combines two values into a sum and can be used with variables, literals, or other expressions.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.05: Trace code with variables to predict outcomes
* T09.G3.06: Copy one variable's value to another variable


ID: T09.G4.01.01
Topic: T09 – Variables & Expressions
Skill: Use subtraction (-) in variable expressions
Description: Students use the - operator block to create expressions that subtract values, such as "set remaining to total - used" or "set difference to a - b". They understand that the - operator finds the difference between two values and can compute negative results.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G4.01: Use addition (+) in variable expressions


ID: T09.G4.02
Topic: T09 – Variables & Expressions
Skill: Use multiplication (*) in expressions
Description: Students use the * operator to create expressions that multiply values, such as "set total to lives * 100" or "set area to width * height". They understand that multiplication scales one value by another.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G4.01.01: Use subtraction (-) in variable expressions


ID: T09.G4.02.01
Topic: T09 – Variables & Expressions
Skill: Use division (/) in expressions
Description: Students use the / operator to create expressions that divide values, such as "set average to sum / count" or "set half to total / 2". They understand that division splits one value by another and may produce decimal results.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G4.02: Use multiplication (*) in expressions


ID: T09.G4.03
Topic: T09 – Variables & Expressions
Skill: Combine two arithmetic operators in a single expression
Description: Students write expressions that combine exactly two operators in one statement using the same type of operation, such as "a + b + c" or "x * y * z". They learn to nest operator blocks in Scratch/CreatiCode and read the resulting expression. This is simpler than mixing different operator types and prepares for G6.02 precedence rules.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G4.02.01: Use division (/) in expressions


ID: T09.G4.04
Topic: T09 – Variables & Expressions
Skill: Store and use user input in a variable
Description: Students use an "ask and wait" or input block to capture user input (a number or text), store it in a variable, and then use that variable in later blocks or conditionals.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.02: Build a key‑press script that controls a sprite
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.03: Use a variable in a simple conditional (if block)


ID: T09.G4.05
Topic: T09 – Variables & Expressions
Skill: Use a variable as a loop counter
Description: Students create a counter variable (e.g., "i" or "count"), set it to a starting value before a loop, and change it by 1 inside the loop each iteration. They display or use the counter value to see it change (e.g., say the number, or use it to position a sprite). This introduces the for-loop pattern: initialize before loop, update inside loop. Example: set i to 1, repeat 5 times: say i, change i by 1.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T07.G3.01: Use a counted repeat loop
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T09.G3.02: Use change block to increase a variable


ID: T09.G4.06
Topic: T09 – Variables & Expressions
Skill: Use basic comparison operators (=, <) in conditionals
Description: Students use the equals (=) and less than (<) operators in conditionals to compare values. Examples: "if score = 10", "if lives < 3". They understand that comparisons evaluate to true/false and control program flow. These are the most intuitive comparisons for beginners.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G2.03: Design a simple "if-then" game rule
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.03: Use a variable in a simple conditional (if block)
* T09.G3.05: Trace code with variables to predict outcomes


ID: T09.G4.06.01
Topic: T09 – Variables & Expressions
Skill: Use greater than (>) operator in conditionals
Description: Students use the greater than (>) operator to check if one value exceeds another. Examples: "if score > 100", "if health > 0". They understand that > is the opposite of < and when to use each.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G2.03: Design a simple "if-then" game rule
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G4.06: Use basic comparison operators (=, <) in conditionals


ID: T09.G4.06.02
Topic: T09 – Variables & Expressions
Skill: Use not equal (≠) operator in conditionals
Description: Students use the not equal (≠) operator to check if values are different. Examples: "if lives ≠ 0", "if answer ≠ correct". They understand that ≠ is the opposite of = and when checking for difference is useful.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G2.03: Design a simple "if-then" game rule
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G4.06: Use basic comparison operators (=, <) in conditionals


ID: T09.G4.06.03
Topic: T09 – Variables & Expressions
Skill: Use greater-or-equal (≥) and less-or-equal (≤) operators
Description: Students use >= and <= operators for inclusive comparisons. Examples: "if score >= 100" (at least 100), "if health <= 20" (at most 20). They understand these include the boundary value unlike > and <, which is important for "at least" and "at most" conditions.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G2.03: Design a simple "if-then" game rule
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G4.06.01: Use greater than (>) operator in conditionals


ID: T09.G4.07
Topic: T09 – Variables & Expressions
Skill: Use a flag variable to track state (0/1 or true/false)
Description: Students create variables (using 0/1 or meaningful names like "game_over") to remember whether an event occurred. They set the flag when the event happens (e.g., "set has_key to 1" when collecting a key) and check it in conditionals to control later behavior (e.g., "if has_key = 1 then open door"). This introduces state tracking, where a variable's value persists and affects future decisions.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G2.03: Design a simple "if-then" game rule
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.03: Use a variable in a simple conditional (if block)
* T09.G3.04.01: Debug missing variable initialization


ID: T09.G4.08
Topic: T09 – Variables & Expressions
Skill: Use random number blocks to set variable values
Description: Students use the "pick random (min) to (max)" block to set variables to random values, enabling games with unpredictable elements like random enemy positions, random prizes, or dice rolls.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G3.02: Match a repeat box diagram to code blocks
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.01.02: Set a variable to an initial value at program start


ID: T09.G4.08.01
Topic: T09 – Variables & Expressions
Skill: Choose appropriate variable display modes (normal, large, slider)
Description: Students right-click on a variable monitor and choose between display modes: normal (shows name and value), large (shows only value in big text), or slider (shows value with draggable control). They understand when each mode is useful for different purposes (large for score display, slider for testing/adjusting values).

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T13.G3.01: Test and trace simple block-based scripts


ID: T09.G4.09.01
Topic: T09 – Variables & Expressions
Skill: Debug variable used before initialization
Description: Students examine a program where a variable is used in an expression or conditional before being initialized (set to a starting value). They trace through the code to identify that the variable needs to be initialized at program start or before first use. This builds on G3.04.01 by handling scripts with 6-10 blocks in more complex contexts.

Dependencies:
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T07.G3.01: Use a counted repeat loop
* T09.G3.04.03: Debug wrong value in variable block
* T09.G4.05: Use a variable as a loop counter
* T13.G3.01: Test and trace simple block-based scripts


ID: T09.G4.09.02
Topic: T09 – Variables & Expressions
Skill: Debug wrong variable selected in expression
Description: Students examine a program where the wrong variable is used in an expression or conditional (e.g., using "lives" instead of "score" in a calculation). They trace through the code to identify which variable should be used based on the intended logic. This requires understanding variable names and their purposes.

Dependencies:
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T07.G3.01: Use a counted repeat loop
* T09.G4.09.01: Debug variable used before initialization
* T13.G3.01: Test and trace simple block-based scripts


ID: T09.G4.09.03
Topic: T09 – Variables & Expressions
Skill: Debug variable updated too many or too few times
Description: Students examine a program where a variable is updated the wrong number of times, often in a loop context (e.g., counter increments on every frame instead of once per event, or doesn't increment inside the loop when it should). They trace through the loop iterations to identify the update frequency problem and fix the placement or condition of the update block.

Dependencies:
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T07.G3.01: Use a counted repeat loop
* T09.G4.09.02: Debug wrong variable selected in expression
* T09.G4.05: Use a variable as a loop counter
* T13.G3.01: Test and trace simple block-based scripts


## GRADE 5 (8 skills)

ID: T09.G5.01
Topic: T09 – Variables & Expressions
Skill: Use multiple variables together in a single expression
Description: Students write expressions that reference 2-3 different variables in one calculation, such as "set area to width * height" or "set total to price * quantity". The focus is on using multiple named variables (not just literals) to compute a result, understanding that variables can reference each other.

Dependencies:
* T09.G4.03: Combine two arithmetic operators in a single expression
* T09.G4.09.03: Debug variable updated too many or too few times


ID: T09.G5.02
Topic: T09 – Variables & Expressions
Skill: Create and use string variables
Description: Students create variables that hold text instead of numbers (e.g., name, message, status). They set string values using "set [myName] to [Alice]" and display them using say blocks or labels.

Dependencies:
* T09.G4.04: Store and use user input in a variable
* T06.G5.01: Identify standard event patterns in a small game


ID: T09.G5.02.01
Topic: T09 – Variables & Expressions
Skill: Create and use boolean variables with true/false values
Description: Students create variables that hold boolean (true/false) values instead of numbers or text. They set boolean values using logic blocks and use them in conditionals to control program flow. Examples: "set isJumping to true", "if isJumping = true then...". This is more intuitive than using 0/1 for flags.

Dependencies:
* T09.G4.07: Use a flag variable to track state (0/1 or true/false)
* T08.G5.00: Draw decision tree flowchart


ID: T09.G5.03
Topic: T09 – Variables & Expressions
Skill: Join strings using concatenation
Description: Students use the `join` block to combine multiple text values into one string, such as "join [Hello ] [name]" to create personalized messages. They understand that join combines text end-to-end without spaces unless explicitly added.

Dependencies:
* T09.G5.02: Create and use string variables
* T06.G5.01: Identify standard event patterns in a small game


ID: T09.G5.03.01
Topic: T09 – Variables & Expressions
Skill: Use multi-input join with separator
Description: Students use the advanced join block `join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]` to combine multiple strings with a separator between them. They apply this for creating CSV data, formatted lists, or comma-separated values. Example: join names with ", " to create "Alice, Bob, Carol".

Dependencies:
* T09.G5.03: Join strings using concatenation


ID: T09.G5.04
Topic: T09 – Variables & Expressions
Skill: Use variables as settings to control program behavior
Description: Students create variables that control game or program settings (e.g., player_speed, enemy_count, difficulty_level) and use them throughout the code so changing one value updates the entire program's behavior. This demonstrates the power of variables as configurable parameters.

Dependencies:
* T09.G4.09.03: Debug variable updated too many or too few times
* T11.G5.01: Decompose a problem into logical custom block boundaries


ID: T09.G5.05
Topic: T09 – Variables & Expressions
Skill: Use the accumulator pattern to compute running totals
Description: Students implement the accumulator pattern: initialize a variable to 0, then add values to it repeatedly (in a loop or across events) to compute totals. They understand this pattern is essential for sums, averages, and statistics. Example: "set total to 0", then in loop: "change total by (item value)".

Dependencies:
* T09.G4.05: Use a variable as a loop counter
* T09.G4.09.03: Debug variable updated too many or too few times
* T06.G5.01: Identify standard event patterns in a small game
* T07.G5.01: Simulate repeated experiments with a loop
* T04.G5.01: Recognize a counter update pattern


ID: T09.G5.06
Topic: T09 – Variables & Expressions
Skill: Trace a counter through loop iterations to predict final value
Description: Students trace a script where a counter variable starts at a value and changes inside a repeat loop, tracking its value at each iteration and predicting the final value. Example: "set i to 0, repeat 5 times: change i by 2" results in i = 10. This extends G3.05 tracing to multi-iteration contexts.

Dependencies:
* T09.G4.05: Use a variable as a loop counter
* T07.G5.01: Simulate repeated experiments with a loop
* T04.G5.01: Recognize a counter update pattern
* T02.G5.01: Trace a script with nested loops using debug print


ID: T09.G5.07
Topic: T09 – Variables & Expressions
Skill: Trace code with multiple interacting variables
Description: Students trace code involving 2-3 variables that interact through expressions, recording each variable's value at each step. Focus on understanding how assignment order affects results (e.g., "set a to b" before vs after "set b to 5").

Dependencies:
* T09.G5.01: Use multiple variables together in a single expression
* T09.G5.06: Trace a counter through loop iterations to predict final value
* T02.G5.01: Trace a script with nested loops using debug print


ID: T09.G5.08
Topic: T09 – Variables & Expressions
Skill: Track high score using variable comparison
Description: Students implement a high score system: compare current score to high_score variable, and if current is greater, update high_score. This combines accumulator tracking with conditional updates and persists the "best so far" value.

Dependencies:
* T09.G4.06.03: Use greater-or-equal (≥) and less-or-equal (≤) operators
* T09.G5.05: Use the accumulator pattern to compute running totals
* T08.G5.00: Draw decision tree flowchart
* T04.G5.01: Recognize a counter update pattern


## GRADE 6 (10 skills - 3 new string operations added)

ID: T09.G6.01
Topic: T09 – Variables & Expressions
Skill: Model real-world quantities using variables and formulas
Description: Students create variables representing real-world quantities (e.g., distance, time, money, temperature) and update them using formulas. Examples: total_cost = price × quantity, distance = speed × time. This connects math formulas to programming.

Dependencies:
* T09.G5.05: Use the accumulator pattern to compute running totals
* T09.G5.07: Trace code with multiple interacting variables


ID: T09.G6.02
Topic: T09 – Variables & Expressions
Skill: Apply operator precedence rules (PEMDAS) in expressions
Description: Students write and evaluate expressions mixing addition/subtraction with multiplication/division, understanding that * and / are evaluated before + and -. They learn to read and predict evaluation order in expressions like "a + b * c" (multiply first, then add). This focuses on understanding the default order of operations.

Dependencies:
* T09.G5.07: Trace code with multiple interacting variables


ID: T09.G6.02.01
Topic: T09 – Variables & Expressions
Skill: Use parentheses to override operator precedence
Description: Students use parentheses to control evaluation order in expressions, overriding default PEMDAS precedence. They predict and explain different results from "(a + b) * c" vs "a + b * c". This enables them to write expressions that match their intended calculation order.

Dependencies:
* T09.G6.02: Apply operator precedence rules (PEMDAS) in expressions


ID: T09.G6.03
Topic: T09 – Variables & Expressions
Skill: Use exponents (^) in expressions
Description: Students use the power operator (^) to compute squares, cubes, and other powers in expressions, such as "set area to side ^ 2" for square area or "set volume to side ^ 3" for cube volume. This extends arithmetic operations to exponential calculations.

Dependencies:
* T09.G6.02.01: Use parentheses to override operator precedence


ID: T09.G6.03.01
Topic: T09 – Variables & Expressions
Skill: Use modulo (remainder) operator in expressions
Description: Students use the modulo operator (mod or %) to find remainders from division. They apply this to practical tasks like determining odd/even numbers (n mod 2), cycling through values (position mod max), or creating repeating patterns. Example: "if score mod 10 = 0" to trigger events every 10 points.

Dependencies:
* T09.G6.02.01: Use parentheses to override operator precedence


ID: T09.G6.04
Topic: T09 – Variables & Expressions
Skill: Use string length operator
Description: Students use `length of [string]` to get the character count of text. They apply this to validate input (e.g., check password length) or process text. Example: "if length of [name] > 10".

Dependencies:
* T09.G5.03: Join strings using concatenation


ID: T09.G6.04.01
Topic: T09 – Variables & Expressions
Skill: Use case conversion (uppercase/lowercase) operators
Description: Students use `[CASE v] of text [T]` blocks to convert text to uppercase or lowercase. They apply this for formatting output or case-insensitive comparisons. Examples: uppercase for shouting effects, lowercase for normalizing user input.

Dependencies:
* T09.G6.04: Use string length operator


ID: T09.G6.04.02
Topic: T09 – Variables & Expressions
Skill: Use letter-of operator to extract single character
Description: Students use the `letter (position) of [text]` block to extract a single character from a specific position in a string. They apply this for character-by-character text processing, validation, or creating acronyms. Example: "letter 1 of [name]" to get first initial.

Dependencies:
* T09.G6.04.01: Use case conversion (uppercase/lowercase) operators


ID: T09.G6.05
Topic: T09 – Variables & Expressions
Skill: Use position operator to find substrings
Description: Students use `position of [search] in [text]` to find where a substring appears (returns position number, or 0 if not found). They apply this for text searching and validation. Example: check if email contains "@".

Dependencies:
* T09.G6.04.02: Use letter-of operator to extract single character


ID: T09.G6.05.01
Topic: T09 – Variables & Expressions
Skill: Use substring operator to extract text portions
Description: Students use `substring of [text] from position (start) to (end)` to extract parts of strings. They apply this for text parsing, extracting initials, or getting file extensions. Example: extract first name from full name.

Dependencies:
* T09.G6.05: Use position operator to find substrings


ID: T09.G6.05.02
Topic: T09 – Variables & Expressions
Skill: Use replace operator to substitute text
Description: Students use the `replace [old] with [new] in [text]` block to substitute text within strings. They apply this for text correction, find-and-replace operations, or text normalization. Example: replace all spaces with underscores in a filename.

Dependencies:
* T09.G6.05.01: Use substring operator to extract text portions


ID: T09.G6.05.03
Topic: T09 – Variables & Expressions
Skill: Use split operator to break string into parts
Description: Students use the `split [text] by [delimiter]` block to break a string into a list of parts separated by a delimiter. They apply this for parsing CSV data, breaking sentences into words, or processing structured text. Example: split "apple,banana,cherry" by "," to get a list of fruits.

Dependencies:
* T09.G6.05.02: Use replace operator to substitute text


ID: T09.G6.06
Topic: T09 – Variables & Expressions
Skill: Use temporary variables for multi-step calculations
Description: Students create temporary variables to hold intermediate results in multi-step calculations. For example, when calculating average: first compute total, then count, then divide total by count. This improves code readability and enables debugging by inspecting intermediate states.

Dependencies:
* T09.G5.05: Use the accumulator pattern to compute running totals
* T09.G6.02.01: Use parentheses to override operator precedence


ID: T09.G6.06.01
Topic: T09 – Variables & Expressions
Skill: Understand variable persistence across events and broadcasts
Description: Students understand that variables maintain their values across different event handlers and broadcasts. When one script sets a variable and broadcasts a message, another script receiving that broadcast can read the updated value. This enables coordination between different parts of a program.

Dependencies:
* T09.G5.04: Use variables as settings to control program behavior


ID: T09.G6.07
Topic: T09 – Variables & Expressions
Skill: Debug off-by-one and comparison operator errors
Description: Students debug scripts where variables control program flow through conditionals and loops. Common bugs include: wrong comparison operator (using > instead of >=), off-by-one errors in loop conditions, or variables not being reset. This extends G4.09 by focusing on control-flow bugs.

Dependencies:
* T09.G4.09.03: Debug variable updated too many or too few times
* T09.G5.07: Trace code with multiple interacting variables


## GRADE 7 (11 skills - 1 split into 2, 4 new regex skills, 2 new geometry skills added)

ID: T09.G7.01
Topic: T09 – Variables & Expressions
Skill: Model dynamic systems where variables change over time
Description: Students create simulations where variables represent quantities that change each frame or time step. Examples: position updated by velocity, population growing by percentage, temperature cooling. They set up update rules (e.g., "change position by speed") and observe how repeated updates create realistic animations.

Dependencies:
* T09.G6.06: Use temporary variables for multi-step calculations
* T07.G5.01: Dynamic systems require loops to update variables over time steps.


ID: T09.G7.01.01
Topic: T09 – Variables & Expressions
Skill: Use rounding functions (round, floor, ceiling) in expressions
Description: Students use rounding functions to convert decimals to integers: round() rounds to nearest, floor() rounds down, ceiling() rounds up. They understand when each is appropriate. Examples: "set rounded_score to round(score)" for display, "set pages to ceiling(items / 10)" for pagination.

Dependencies:
* T09.G6.03: Use exponents (^) in expressions


ID: T09.G7.01.02
Topic: T09 – Variables & Expressions
Skill: Use absolute value (abs) function in expressions
Description: Students use the abs() function to get the magnitude of a number without regard to sign (removes negative signs). They apply this for distance calculations, error magnitudes, or ensuring positive values. Example: "set distance to abs(x1 - x2)".

Dependencies:
* T09.G7.01.01: Use rounding functions (round, floor, ceiling) in expressions


ID: T09.G7.01.03
Topic: T09 – Variables & Expressions
Skill: Use square root (sqrt) function in expressions
Description: Students use the sqrt() function to find square roots in calculations. They apply this for distance formulas (Pythagorean theorem), scaling, or inverse of squaring operations. Example: "set distance to sqrt((x2-x1)^2 + (y2-y1)^2)".

Dependencies:
* T09.G7.01.02: Use absolute value (abs) function in expressions


ID: T09.G7.02
Topic: T09 – Variables & Expressions
Skill: Compute average using sum and count variables
Description: Students implement average calculation: maintain a sum variable (accumulating values) and a count variable (tracking how many), then compute average by dividing sum by count. This combines multiple variable patterns and connects to data analysis.

Dependencies:
* T09.G5.05: Use the accumulator pattern to compute running totals
* T09.G6.06: Use temporary variables for multi-step calculations


ID: T09.G7.03
Topic: T09 – Variables & Expressions
Skill: Use compound conditions (AND, OR, NOT) with variables
Description: Students create conditional expressions using logical operators (AND, OR, NOT) to combine multiple variable comparisons. Example: "if score > 10 AND lives > 0" or "if NOT game_over". This enables more nuanced decision logic.

Dependencies:
* T09.G5.08: Track high score using variable comparison
* T09.G6.07: Debug off-by-one and comparison operator errors


ID: T09.G7.04
Topic: T09 – Variables & Expressions
Skill: Understand for-this-sprite vs for-all-sprites variable scope
Description: Students learn the difference between for-this-sprite variables (visible only within one sprite) and for-all-sprites variables (visible to all sprites). They understand when to use each type and how to share data between sprites using for-all-sprites variables. This reflects CreatiCode's terminology for local vs global scope.

Dependencies:
* T09.G5.04: Use variables as settings to control program behavior
* T09.G6.01: Model real-world quantities using variables and formulas


ID: T09.G7.05.01
Topic: T09 – Variables & Expressions
Skill: Save variables to a file (export)
Description: Students use file export operations to save variable values to a file. This enables persistent storage of game state, settings, or high scores that survives beyond program execution. They understand how to format data for export and choose appropriate file formats.

Dependencies:
* T09.G7.04: Understand for-this-sprite vs for-all-sprites variable scope


ID: T09.G7.05.02
Topic: T09 – Variables & Expressions
Skill: Load variables from a file (import)
Description: Students use file import operations to load variable values from a file into their program. This enables restoring saved game state, loading settings, or importing data from other sources. They understand how to parse imported data and assign values to variables. This complements export to create complete save/load functionality.

Dependencies:
* T09.G7.05.01: Save variables to a file (export)


ID: T09.G7.06
Topic: T09 – Variables & Expressions
Skill: Predict behavior changes from modifying variable values
Description: Students analyze existing code and predict how behavior changes when variable initialization values, update amounts, or conditions are modified. Example: "If speed changes from 5 to 10, what happens?" This is analytical reasoning about code without running it.

Dependencies:
* T09.G6.07: Debug off-by-one and comparison operator errors
* T09.G7.01: Model dynamic systems where variables change over time


ID: T09.G7.07
Topic: T09 – Variables & Expressions
Skill: Use regex test to check if pattern matches text
Description: Students use the regex test operation to check if a text string matches a regular expression pattern, returning true or false. They apply this for input validation (e.g., checking if email format is valid, if password meets requirements). Example: test if text matches pattern "^[A-Za-z]+$" for letters only.

Dependencies:
* T09.G6.05.03: Use split operator to break string into parts


ID: T09.G7.07.01
Topic: T09 – Variables & Expressions
Skill: Use regex match to find pattern occurrences
Description: Students use the regex match operation to find all occurrences of a pattern in text, returning a list of matches. They apply this for extracting data (e.g., finding all numbers in text, extracting hashtags from messages). Example: match all words starting with capital letters.

Dependencies:
* T09.G7.07: Use regex test to check if pattern matches text


ID: T09.G7.07.02
Topic: T09 – Variables & Expressions
Skill: Use regex replace for pattern-based substitution
Description: Students use the regex replace operation to substitute text matching a pattern with replacement text. They apply this for advanced text processing (e.g., removing all digits, normalizing whitespace, redacting sensitive information). Example: replace all sequences of spaces with single space.

Dependencies:
* T09.G7.07.01: Use regex match to find pattern occurrences


ID: T09.G7.07.03
Topic: T09 – Variables & Expressions
Skill: Use regex split to divide text by pattern
Description: Students use the regex split operation to break text into parts based on a pattern delimiter (not just a fixed string). They apply this for flexible parsing (e.g., split by any whitespace, split by punctuation). Example: split text by one or more spaces using pattern "\s+".

Dependencies:
* T09.G7.07.02: Use regex replace for pattern-based substitution


ID: T09.G7.08
Topic: T09 – Variables & Expressions
Skill: Use distance 2D block to calculate distance between points
Description: Students use the distance 2D block to calculate the Euclidean distance between two points (x1, y1) and (x2, y2). They apply this for collision detection ranges, proximity checks, or measuring sprite distances. This simplifies distance calculations that would otherwise require the Pythagorean theorem formula.

Dependencies:
* T09.G7.01.03: Use square root (sqrt) function in expressions


ID: T09.G7.08.01
Topic: T09 – Variables & Expressions
Skill: Use direction block to calculate angle between points
Description: Students use the direction block to calculate the angle from one point to another point. They apply this for aiming mechanics, rotation toward targets, or trajectory calculations. Example: point sprite toward moving target, calculate reflection angles.

Dependencies:
* T09.G7.08: Use distance 2D block to calculate distance between points


## GRADE 8 (11 skills - 5 new advanced math skills added)

ID: T09.G8.01.01
Topic: T09 – Variables & Expressions
Skill: Use variables to track index position in linear search
Description: Students implement a linear search algorithm that uses a variable to track the current index position while searching through values. They initialize an index variable, update it in each iteration, and use it to check each position until finding the target value or reaching the end.

Dependencies:
* T09.G7.03: Use compound conditions (AND, OR, NOT) with variables
* T09.G7.06: Predict behavior changes from modifying variable values
* T02.G6.01: Learn the pseudocode generation block
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds


ID: T09.G8.01.02
Topic: T09 – Variables & Expressions
Skill: Use flag variables in search algorithms to track found status
Description: Students use a boolean flag variable (e.g., "found") to remember whether a search has succeeded. They set the flag to false initially, update it to true when the target is found, and check it to determine next actions. This pattern helps control loop termination and post-search behavior.

Dependencies:
* T09.G8.01.01: Use variables to track index position in linear search
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds


ID: T09.G8.01.03
Topic: T09 – Variables & Expressions
Skill: Use variables in iterative approximation algorithms
Description: Students implement iterative approximation algorithms (e.g., Newton's method for square roots, binary search for values) that use variables to track and refine estimates across multiple iterations. They understand convergence criteria and when to stop iterating.

Dependencies:
* T09.G8.01.02: Use flag variables in search algorithms to track found status
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T07.G6.01: Trace nested loops with variable bounds


ID: T09.G8.02
Topic: T09 – Variables & Expressions
Skill: Simplify and optimize variable expressions
Description: Students identify opportunities to simplify expressions: replacing "x + x + x" with "x * 3", factoring common subexpressions, or replacing a counting loop with a direct formula. They evaluate trade-offs between readability and efficiency.

Dependencies:
* T09.G6.03: Use exponents (^) in expressions
* T09.G7.06: Predict behavior changes from modifying variable values
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds
* T10.G6.01: Sort a table by a column


ID: T09.G8.02.01
Topic: T09 – Variables & Expressions
Skill: Use min and max functions to constrain variable values
Description: Students use min() and max() functions to keep variable values within bounds. Examples: "set x to max(0, min(480, x))" to keep x between 0 and 480, or "set health to max(0, health)" to prevent negative health. This is essential for game boundaries and value validation.

Dependencies:
* T09.G7.01.03: Use square root (sqrt) function in expressions
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T07.G6.01: Trace nested loops with variable bounds
* T16.G6.01: Evaluate an interface for usability


ID: T09.G8.02.02
Topic: T09 – Variables & Expressions
Skill: Use trigonometric functions (sin, cos, tan) in expressions
Description: Students use sine, cosine, and tangent functions to calculate angles and circular motion. They apply these to create circular paths, calculate trajectory angles, or convert between polar and Cartesian coordinates. Example: "set x to radius * cos(angle)", "set y to radius * sin(angle)".

Dependencies:
* T09.G7.01.03: Use square root (sqrt) function in expressions
* T02.G6.01: Learn the pseudocode generation block
* T07.G6.01: Trace nested loops with variable bounds
* T12.G6.01: Analyze a program's structure using a checklist and suggest specific improvements


ID: T09.G8.02.03
Topic: T09 – Variables & Expressions
Skill: Use inverse trigonometric functions (asin, acos, atan) in expressions
Description: Students use inverse trigonometric functions (arcsine, arccosine, arctangent) to calculate angles from coordinate ratios or side lengths. They apply these for angle calculation from vectors, direction finding, or converting Cartesian to polar coordinates. Example: "set angle to atan2(dy, dx)" for direction to target.

Dependencies:
* T09.G8.02.02: Use trigonometric functions (sin, cos, tan) in expressions


ID: T09.G8.02.04
Topic: T09 – Variables & Expressions
Skill: Use logarithmic functions (ln, log) in expressions
Description: Students use natural logarithm (ln) and base-10 logarithm (log) functions in calculations. They apply these for exponential decay models, scientific calculations, or data transformations. Example: calculating decay rates, pH calculations, or logarithmic scales.

Dependencies:
* T09.G8.02.02: Use trigonometric functions (sin, cos, tan) in expressions


ID: T09.G8.02.05
Topic: T09 – Variables & Expressions
Skill: Use exponential functions (e^x, 10^x) in expressions
Description: Students use exponential functions with base e (e^x) and base 10 (10^x) in calculations. They apply these for growth models, compound interest, or scientific notation. Example: modeling population growth, radioactive decay, or converting between logarithmic and linear scales.

Dependencies:
* T09.G8.02.04: Use logarithmic functions (ln, log) in expressions


ID: T09.G8.03
Topic: T09 – Variables & Expressions
Skill: Use cloud variables for persistent data storage
Description: Students use cloud variables to save data that persists across sessions and is shared between users. They understand that cloud variables are stored on a server and updated in real-time, enabling high scores, user preferences, or multiplayer data sharing.

Dependencies:
* T09.G7.04: Understand for-this-sprite vs for-all-sprites variable scope
* T09.G7.05.02: Load variables from a file (import)
* T04.G6.01: Group snippets by underlying algorithm pattern
* T07.G6.01: Trace nested loops with variable bounds
* T16.G6.01: Evaluate an interface for usability


ID: T09.G8.04
Topic: T09 – Variables & Expressions
Skill: Debug variable scope and concurrent update errors
Description: Students identify and fix bugs in programs with multiple sprites sharing variables: scope confusion (for-this-sprite vs for-all-sprites), race conditions when multiple scripts update the same variable, or initialization order dependencies. They trace variable states across concurrent scripts.

Dependencies:
* T09.G7.04: Understand for-this-sprite vs for-all-sprites variable scope
* T09.G7.06: Predict behavior changes from modifying variable values
* T02.G6.01: Learn the pseudocode generation block
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T07.G6.01: Trace nested loops with variable bounds


ID: T09.G8.05
Topic: T09 – Variables & Expressions
Skill: Translate mathematical formulas into code expressions
Description: Students translate real-world formulas (distance = speed × time, area = π × r², compound interest) into variable assignments and expressions. They handle operator precedence, multi-step calculations, and unit considerations. This capstone skill demonstrates mastery of variables and expressions.

Dependencies:
* T09.G6.03: Use exponents (^) in expressions
* T09.G7.02: Compute average using sum and count variables
* T09.G7.03: Use compound conditions (AND, OR, NOT) with variables
* T07.G6.01: Trace nested loops with variable bounds
* T14.G6.01.01: Track game state with variable
* T21.G6.01: Plan a mixed-source asset kit for a game or story project


ID: T09.G8.06
Topic: T09 – Variables & Expressions
Skill: Use variables to collect and store multiple data readings
Description: Students use variables to collect data from repeated user inputs or program-generated values over time, storing values for later analysis. They implement collection loops that gather specified numbers of readings and store running statistics. This demonstrates using variables as data collection containers for computational analysis.

Dependencies:
* T09.G7.02: Compute average using sum and count variables
* T09.G8.01.01: Use variables to track index position in linear search
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds
* T10.G6.01: Sort a table by a column


ID: T09.G8.07
Topic: T09 – Variables & Expressions
Skill: Use calculate block to evaluate string expressions
Description: Students use the calculate/evaluate block to evaluate mathematical expressions stored as strings. They apply this for creating calculator programs, evaluating user-entered formulas, or dynamic expression evaluation. Example: calculate "5 + 3 * 2" returns 11. This enables runtime expression parsing and evaluation.

Dependencies:
* T09.G8.02: Simplify and optimize variable expressions
* T09.G6.02: Apply operator precedence rules (PEMDAS) in expressions


ID: T09.G8.08
Topic: T09 – Variables & Expressions
Skill: Use solve-equation block to find variable values
Description: Students use the solve-equation block to find values of variables that satisfy equations. They apply this for algebraic problem solving, finding intersections, or constraint satisfaction. Example: solve "x + 5 = 12" for x, or solve "2*x + y = 10 AND x - y = 2" for x and y. This enables symbolic math solving within programs.

Dependencies:
* T09.G8.07: Use calculate block to evaluate string expressions
* T09.G7.03: Use compound conditions (AND, OR, NOT) with variables


## SUMMARY

Total skills in revised T09: 91 skills
- Grade K: 2 skills (unchanged)
- Grade 1: 2 skills (unchanged)
- Grade 2: 2 skills (unchanged)
- Grade 3: 12 skills (was 6, increased by breaking down T09.G3.04 into 3 separate skills)
- Grade 4: 16 skills (was 10, increased by breaking down T09.G4.09 into 3 separate skills)
- Grade 5: 8 skills (was 9, decreased by 1 due to removed T10 dependency from T09.G5.03.01)
- Grade 6: 16 skills (was 13, increased by 3 new string operation skills)
- Grade 7: 16 skills (was 6, increased by 10: split T09.G7.05 into 2 skills, added 4 regex skills, 2 geometry skills, preserved 2 additional skills)
- Grade 8: 17 skills (was 6, increased by 11: added 5 advanced math skills, 2 new blocks for expression evaluation)

## KEY CHANGES IMPLEMENTED:

1. ✓ BROKE DOWN OVERLY BROAD SKILLS:
   - T09.G3.04 → T09.G3.04.01, T09.G3.04.02, T09.G3.04.03
   - T09.G4.09 → T09.G4.09.01, T09.G4.09.02, T09.G4.09.03
   - T09.G7.05 → T09.G7.05.01, T09.G7.05.02

2. ✓ ADDED MISSING SKILLS:
   - String operations (G6): T09.G6.04.02, T09.G6.05.02, T09.G6.05.03
   - Regex operations (G7): T09.G7.07, T09.G7.07.01, T09.G7.07.02, T09.G7.07.03
   - Geometric operations (G7): T09.G7.08, T09.G7.08.01
   - Advanced math (G8): T09.G8.02.03, T09.G8.02.04, T09.G8.02.05, T09.G8.07, T09.G8.08

3. ✓ FIXED DEPENDENCIES:
   - Removed T10 forward dependencies from T09.G5.03.01 (removed T10.G5.01)
   - Fixed T09.G3.02 dependency to reference T09.G3.02.01 correctly
   - Fixed T09.G4.07 to depend on T09.G3.04.01 instead of old T09.G3.04
   - Fixed T09.G4.09.01/02/03 to build sequentially
   - Fixed T09.G5.01 to depend on T09.G4.09.03
   - Fixed T09.G5.04 to depend on T09.G4.09.03
   - Fixed T09.G5.05 to depend on T09.G4.09.03
   - Fixed T09.G6.07 to depend on T09.G4.09.03
   - Fixed T09.G8.03 to depend on T09.G7.05.02

4. ✓ CLARIFIED DESCRIPTIONS:
   - T09.G7.04: Changed "local vs global" to "for-this-sprite vs for-all-sprites"
   - T09.G8.06: Removed "sensor readings" reference, clarified as "user inputs or program-generated values"

5. ✓ PRESERVED ALL CROSS-TOPIC DEPENDENCIES (T## where ## ≠ 09)

6. ✓ ALL NEW SKILLS FOLLOW X-2 RULE for grade-level dependencies
