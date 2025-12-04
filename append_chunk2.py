
with open('t09_content.txt', 'a') as f:
    f.write(r'''ID: T09.G3.06
Topic: T09 – Variables & Expressions
Skill: Debug missing change/update block
Description: **Student task:** Students inspect simple scripts (3-5 blocks) where a variable doesn't update as expected during gameplay. Focus on recognizing the symptom (score stays at 0 even after collecting items) and finding the missing "change [variable] by [amount]" block that should appear in the event handler. This builds pattern recognition for update-related bugs.

Dependencies:
* T09.G3.05: Debug missing initialization and wrong update values

ID: T09.G3.07
Topic: T09 – Variables & Expressions
Skill: Trace code with variables to predict outcomes
Description: **Student task:** Students trace a very short script (3-4 steps) where a variable changes in simple ways (set to 0, change by 1, change by 1 again), and predict the final value by reading and following the code. This skill focuses on understanding existing code and predicting outcomes, not creating new variables. Use small numbers and obvious changes.

Dependencies:
* T09.G3.06: Debug missing change/update block
* T08.G3.10: Trace code with a single if/else

ID: T09.G3.08
Topic: T09 – Variables & Expressions
Skill: Copy one variable's value to another variable
Description: **Student task:** Students use "set [variable1] to [variable2]" to copy the value from one variable to another. They understand that this creates an independent copy - changing one variable later doesn't affect the other. Examples: "set backup_score to score", "set player_x to enemy_x". This bridges the gap between basic variable operations and using variables in complex expressions.

Dependencies:
* T09.G3.01: Create, initialize, and increment a variable

ID: T09.G3.09
Topic: T09 – Variables & Expressions
Skill: Decrease a variable using negative numbers
Description: **Student task:** Students use the standard `change [variable] by (-1)` block pattern to decrease a value. They understand that adding a negative number is the same as subtraction. Examples: "change lives by -1" when hit by enemy, "change time by -1" each second. This reinforces the number line concept where adding negative moves left/down.

Dependencies:
* T09.G3.02: Change and reduce variables with display monitoring

ID: T09.G3.10
Topic: T09 – Variables & Expressions
Skill: Predict variable value changes before running code
Description: **Student task:** Students examine a short script (4-6 blocks) with variable operations and predict what value each variable will have after the code runs, WITHOUT actually running the code. They write their prediction, then run the code to verify. This develops computational thinking by mentally simulating code execution. Example: Given "set score to 5, change score by 3, change score by 2", students predict score = 10 before running. This differs from G3.07 (tracing) by requiring prediction BEFORE execution and self-verification AFTER.

Dependencies:
* T09.G3.07: Trace code with variables to predict outcomes

ID: T09.G3.11
Topic: T09 – Variables & Expressions
Skill: Explain why descriptive variable names improve code readability
Description: **Student task:** Students compare code using descriptive variable names (like "score", "playerSpeed", "livesRemaining") versus non-descriptive names (like "x", "n", "thing1"). They identify which version is easier to understand and explain WHY descriptive names help: (1) you can understand what the variable stores without reading the whole program, (2) you make fewer mistakes when updating the right variable, (3) other people (or future you) can read the code more easily. Example: comparing "set s to s + 1" vs "set score to score + 1" - both work, but one is much clearer.

Dependencies:
* T09.G3.01: Create, initialize, and increment a variable
* T09.G3.10: Predict variable value changes before running code

ID: T09.G3.12
Topic: T09 – Variables & Expressions
Skill: Use console output to inspect variable values during execution
Description: **Student task:** Students use `console log` or `say` blocks to display variable values at specific points in their code, creating a simple debugging trace. They run code and observe the console/stage output to verify that variables have expected values. Example: add "console log [score]" after each "change score by 10" to verify score increases correctly. This introduces systematic debugging using output inspection rather than just running code and hoping it works.

Dependencies:
* T09.G3.02: Change and reduce variables with display monitoring
* T09.G3.07: Trace code with variables to predict outcomes

ID: T09.G3.13
Topic: T09 – Variables & Expressions
Skill: Explain why a variable is needed for a specific problem
Description: **Student task:** Students compare two solutions to the same problem: one using a variable, one without (using fixed values or asking user repeatedly). They explain which solution is better and why. Example: "Store the player's name in a variable so we can greet them multiple times" vs "ask for their name every time we want to say hello." They articulate benefits: (1) store information once, use many times, (2) code is easier to change, (3) program remembers user input. This computational thinking communication skill builds understanding of WHY variables exist.

Dependencies:
* T09.G3.01: Create, initialize, and increment a variable
* T09.G3.11: Explain why descriptive variable names improve code readability

ID: T09.G3.14
Topic: T09 – Variables & Expressions
Skill: Trace expression evaluation step-by-step
Description: **Student task:** Students break down expression evaluation into steps, showing intermediate results. Given "set total to score + bonus" where score=5 and bonus=3, they write: "Step 1: Get score value (5), Step 2: Get bonus value (3), Step 3: Add them (5+3=8), Step 4: Store result in total (total=8)." This mental model of how expressions evaluate prepares them for debugging complex expressions in G4+.

Dependencies:
* T09.G3.07: Trace code with variables to predict outcomes
* T09.G3.08: Copy one variable's value to another variable

ID: T09.G3.15
Topic: T09 – Variables & Expressions
Skill: Compare two working solutions and explain trade-offs
Description: **Student task:** Students compare two correct implementations of the same task and explain the differences. Example: Solution A uses one variable that gets updated; Solution B uses two variables and copies the final result. Both work! Students explain: (1) Which is easier to read? (2) Which is easier to debug? (3) Which would you choose and why? This computational thinking communication skill builds the ability to evaluate and justify design choices, not just write working code.

Dependencies:
* T09.G3.10: Predict variable value changes before running code
* T09.G3.11: Explain why descriptive variable names improve code readability

ID: T09.G3.16
Topic: T09 – Variables & Expressions
Skill: Build an expression from a word problem
Description: **Student task:** Students translate word problems into variable expressions. Example: "You have some coins. You find 5 more coins. How do you write this in code?" Answer: "change coins by 5". Or: "Your score is coins times 10. How do you write this?" Answer: "set score to coins * 10". They practice recognizing keywords (total, difference, product, each) that indicate operations (+, -, *, /) and translating English descriptions into code expressions.

Dependencies:
* T09.G3.08: Copy one variable's value to another variable
* T09.G3.14: Trace expression evaluation step-by-step

ID: T09.G3.17
Topic: T09 – Variables & Expressions
Skill: Count occurrences using a counter variable
Description: **Student task:** Students implement the "counting occurrences" pattern: initialize a counter to 0, then increment it each time a specific event occurs. Examples: count how many times the player jumps, count how many enemies are defeated, count button clicks. They build scripts like: "set jumpCount to 0" (on green flag), then "change jumpCount by 1" (when space key pressed). They understand this pattern answers the question "how many times did X happen?" which is fundamental to data collection, statistics, and game mechanics.

Dependencies:
* T09.G3.01: Create, initialize, and increment a variable
* T09.G3.04: Use a variable in a simple conditional (if block)

ID: T09.G4.01
Topic: T09 – Variables & Expressions
Skill: Recognize and create arithmetic expressions with variables
Description: **Student task:** Students recognize that expressions combine variables and values using operators, and create their first expression using addition: "set total to score + bonus". They observe that the + operator combines two values into a sum and can be used with variables, literals, or other reporter blocks. They predict the result of simple expressions before running them. This establishes the foundation for all arithmetic operators.

Dependencies:
* T09.G3.07: Trace code with variables to predict outcomes
* T09.G3.08: Copy one variable's value to another variable

ID: T09.G4.02
Topic: T09 – Variables & Expressions
Skill: Use addition (+) in variable expressions
Description: **Student task:** Students use the + operator block to create expressions that add values, such as "set total to score + bonus" or "set sum to a + b". They understand that the + operator combines two values into a sum and can be used with variables, literals, or other expressions. This extends the foundation with practical addition patterns.

Dependencies:
* T09.G4.01: Recognize and create arithmetic expressions with variables

ID: T09.G4.03
Topic: T09 – Variables & Expressions
Skill: Use subtraction (-) in variable expressions
Description: **Student task:** Students use the - operator block to create expressions that subtract values, such as "set remaining to total - used" or "set difference to a - b". They understand that the - operator finds the difference between two values and can compute negative results.

Dependencies:
* T09.G4.01: Recognize and create arithmetic expressions with variables

ID: T09.G4.04
Topic: T09 – Variables & Expressions
Skill: Use multiplication (*) in expressions
Description: **Student task:** Students use the * operator to create expressions that multiply values, such as "set total to lives * 100" or "set area to width * height". They understand that multiplication scales one value by another.

Dependencies:
* T09.G4.01: Recognize and create arithmetic expressions with variables

ID: T09.G4.05
Topic: T09 – Variables & Expressions
Skill: Use division (/) in expressions
Description: **Student task:** Students use the / operator to create expressions that divide values, such as "set average to sum / count" or "set half to total / 2". They understand that division splits one value by another and may produce decimal results.

Dependencies:
* T09.G4.01: Recognize and create arithmetic expressions with variables

ID: T09.G4.06
Topic: T09 – Variables & Expressions
Skill: Combine two arithmetic operators in a single expression
Description: **Student task:** Students write expressions that combine exactly two operators in one statement using the same type of operation, such as "a + b + c" or "x * y * z". They learn to nest operator blocks in Scratch/CreatiCode and read the resulting expression. This is simpler than mixing different operator types and prepares for G6.02 precedence rules.

Dependencies:
* T09.G4.02: Use addition (+) in variable expressions
* T09.G4.03: Use subtraction (-) in variable expressions
* T09.G4.04: Use multiplication (*) in expressions
* T09.G4.05: Use division (/) in expressions

ID: T09.G4.07
Topic: T09 – Variables & Expressions
Skill: Store and use user input in a variable
Description: **Student task:** Students use an "ask and wait" or input block to capture user input (a number or text), store it in a variable, and then use that variable in later blocks or conditionals.

Dependencies:
* T06.G3.04: Build a key‑press script that controls a sprite
* T09.G3.04: Use a variable in a simple conditional (if block)

ID: T09.G4.08
Topic: T09 – Variables & Expressions
Skill: Use a variable as a loop counter
Description: **Student task:** Students create a counter variable (e.g., "i" or "count"), set it to a starting value before a loop, and change it by 1 inside the loop each iteration. They display or use the counter value to see it change (e.g., say the number, or use it to position a sprite). This introduces the for-loop pattern: initialize before loop, update inside loop. Example: set i to 1, repeat 5 times: say i, change i by 1.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T09.G3.02: Change and reduce variables with display monitoring

ID: T09.G4.09
Topic: T09 – Variables & Expressions
Skill: Use equals (=) and less than (<) comparison operators in conditionals
Description: **Student task:** Students use the equals (=) and less than (<) operators in conditionals to compare variable values. Examples: "if score = 10 then say 'You win!'", "if lives < 1 then broadcast game_over". They understand that comparisons evaluate to true/false and control which code runs. These are the foundational comparisons: = checks for exact match, < checks if left value is smaller than right.

Dependencies:
* T09.G3.04: Use a variable in a simple conditional (if block)
* T09.G3.07: Trace code with variables to predict outcomes

ID: T09.G4.10
Topic: T09 – Variables & Expressions
Skill: Use greater than (>) operator in conditionals
Description: **Student task:** Students use the greater than (>) operator to check if one value exceeds another. Examples: "if score > 100 then say 'High score!'", "if health > 0 then keep playing". They understand that > is the opposite of < and when to use each based on what they want to check.

Dependencies:
* T09.G4.09: Use equals (=) and less than (<) comparison operators in conditionals

ID: T09.G4.11
Topic: T09 – Variables & Expressions
Skill: Use not equal (≠) and inclusive comparison (≥, ≤) operators
Description: **Student task:** Students use CreatiCode's extended comparison operators: not equal (≠) to check if values are different, greater-or-equal (≥) for "at least" conditions, and less-or-equal (≤) for "at most" conditions. Examples: "if lives ≠ 0 then keep playing", "if score ≥ 100 then unlock bonus level", "if health ≤ 20 then show warning". They understand that ≥/≤ include the boundary value unlike >/< which exclude it.

Dependencies:
* T09.G4.09: Use equals (=) and less than (<) comparison operators in conditionals
* T09.G4.10: Use greater than (>) operator in conditionals

ID: T09.G4.12
Topic: T09 – Variables & Expressions
Skill: Debug expression evaluation errors
Description: **Student task:** Students identify and fix bugs where expressions produce wrong results due to: (1) wrong operator used (+ instead of *, / instead of -), (2) operands in wrong order (a - b vs b - a matters for subtraction/division), or (3) missing/extra operands. They trace expression evaluation step-by-step to find the error. Example: "set average to sum / count" should be "sum / count" not "count / sum". This introduces debugging of mathematical logic distinct from variable usage bugs.

Dependencies:
* T09.G4.06: Combine two arithmetic operators in a single expression
* T09.G4.09: Use equals (=) and less than (<) comparison operators in conditionals

ID: T09.G4.13
Topic: T09 – Variables & Expressions
Skill: Use a flag variable to track state (0/1 or true/false)
Description: **Student task:** Students create variables (using 0/1 or meaningful names like "game_over") to remember whether an event occurred. They set the flag when the event happens (e.g., "set has_key to 1" when collecting a key) and check it in conditionals to control later behavior (e.g., "if has_key = 1 then open door"). This introduces state tracking, where a variable's value persists and affects future decisions.

Dependencies:
* T06.G3.02: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.04: Use a variable in a simple conditional (if block)
* T09.G3.05: Debug missing initialization and wrong update values

ID: T09.G4.14
Topic: T09 – Variables & Expressions
Skill: Use random number blocks to set variable values
Description: **Student task:** Students use the "pick random (min) to (max)" block to set variables to random values, enabling games with unpredictable elements like random enemy positions, random prizes, or dice rolls.

Dependencies:
* T09.G3.01: Create, initialize, and increment a variable

ID: T09.G4.15
Topic: T09 – Variables & Expressions
Skill: Choose appropriate variable display modes (normal, large, slider)
Description: **Student task:** Students right-click on a variable monitor and choose between display modes: normal (shows name and value), large (shows only value in big text), or slider (shows value with draggable control). They understand when each mode is useful for different purposes (large for score display, slider for testing/adjusting values).

Dependencies:
* T09.G3.02: Change and reduce variables with display monitoring
* T12.G3.01: Test and trace simple block-based scripts

ID: T09.G4.16
Topic: T09 – Variables & Expressions
Skill: Debug variable used before initialization
Description: **Student task:** Students examine a program where a variable is used in an expression or conditional before being initialized (set to a starting value). They trace through the code to identify that the variable needs to be initialized at program start or before first use. This builds on G3.05 by handling scripts with 6-10 blocks in more complex contexts.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T09.G3.06: Debug missing change/update block
* T09.G4.08: Use a variable as a loop counter
* T12.G3.01: Test and trace simple block-based scripts

ID: T09.G4.17
Topic: T09 – Variables & Expressions
Skill: Debug wrong variable or update frequency errors
Description: **Student task:** Students examine programs where the wrong variable is used in an expression (e.g., using "lives" instead of "score") OR a variable is updated the wrong number of times (often in loops - counter increments on every frame instead of once per event). They trace through the code to identify which variable should be used based on intended logic, or trace loop iterations to identify update frequency problems. This consolidates the two common intermediate debugging patterns.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T09.G4.08: Use a variable as a loop counter
* T09.G4.16: Debug variable used before initialization
* T12.G3.01: Test and trace simple block-based scripts

ID: T09.G4.18
Topic: T09 – Variables & Expressions
Skill: Use CreatiCode's for-loop block with automatic variable
Description: **Student task:** Students use CreatiCode's `for [variable] from (start) to (limit) at step (step)` block (found in Control category) which automatically manages a loop counter variable. Examples: "for i from 1 to 10 at step 1" counts 1,2,3...10, or "for i from 0 to 100 at step 10" counts 0,10,20...100. This is more efficient than manually initializing and changing a counter inside a repeat loop. Students compare both approaches and understand when to use each.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T09.G4.08: Use a variable as a loop counter

ID: T09.G4.19
Topic: T09 – Variables & Expressions
Skill: Use variables with pen blocks for drawing patterns
Description: **Student task:** Students use variables to control pen drawing operations, creating patterns based on variable values. They use a counter variable to change pen size, color, or position during drawing. Examples: draw concentric circles where each circle's radius is determined by a counter variable, or draw a spiral where the distance moved increases by a variable amount each iteration. This connects variables to visual output and demonstrates how changing numbers create patterns.

Dependencies:
* T09.G4.08: Use a variable as a loop counter
* T09.G4.18: Use CreatiCode's for-loop block with automatic variable

ID: T09.G4.20
Topic: T09 – Variables & Expressions
Skill: Build a countdown timer using variables
Description: **Student task:** Students create a countdown timer that starts at a value (e.g., 10 seconds) and decreases to 0. They initialize a timer variable, use the `change [variable] by -1` block inside a loop with a 1-second wait, and display the countdown. They add a conditional to detect when the timer reaches 0 and trigger an action (say "Time's up!", end game). This practical application combines initialization, reduction, display, and conditionals in a common game mechanic.

Dependencies:
* T09.G3.09: Decrease a variable using negative numbers
* T09.G4.08: Use a variable as a loop counter
* T09.G4.09: Use equals (=) and less than (<) comparison operators in conditionals

ID: T09.G4.21
Topic: T09 – Variables & Expressions
Skill: Store intermediate calculation results in variables
Description: **Student task:** Students break down complex calculations into steps by storing intermediate results in variables. Instead of writing one large expression, they compute each step separately. Example: to calculate area of a border (outer - inner area), first "set outerArea to outerWidth * outerHeight", then "set innerArea to innerWidth * innerHeight", then "set borderArea to outerArea - innerArea". This pattern makes code more readable, easier to debug (can check each step), and prepares for more complex multi-step algorithms.

Dependencies:
* T09.G4.06: Combine two arithmetic operators in a single expression
* T09.G4.12: Debug expression evaluation errors

ID: T09.G4.22
Topic: T09 – Variables & Expressions
Skill: Implement boundary checking with min and max guards
Description: **Student task:** Students use conditionals to keep variable values within valid ranges. They implement patterns like: "if health > maxHealth then set health to maxHealth" and "if x < 0 then set x to 0". They understand that many games and simulations require variables to stay within bounds (health can't exceed max, position can't go off-screen, score can't be negative). This defensive programming pattern prevents bugs and ensures consistent behavior.

Dependencies:
* T09.G4.09: Use equals (=) and less than (<) comparison operators in conditionals
* T09.G4.11: Use not equal (≠) and inclusive comparison (≥, ≤) operators
* T09.G4.13: Use a flag variable to track state (0/1 or true/false)

ID: T09.G4.23
Topic: T09 – Variables & Expressions
Skill: Debug expression evaluation using console inspection
Description: **Student task:** Students debug expressions that produce wrong results by adding console log statements to inspect intermediate values. They identify where in a multi-step expression the error occurs. Example: "set result to (a + b) * c" gives wrong answer; add "console log [a]", "console log [b]", "console log [a + b]" to find which value is incorrect. This combines G3.12 console skills with G4.12 expression debugging.

Dependencies:
* T09.G3.12: Use console output to inspect variable values during execution
* T09.G4.12: Debug expression evaluation errors

ID: T09.G4.24
Topic: T09 – Variables & Expressions
Skill: Plan variable lifecycle before coding
Description: **Student task:** Students plan variable usage before writing code by answering: (1) What variables do I need? (2) What are their initial values? (3) When/where do they change? (4) When/where are they read? They create a simple variable plan table for a small project (3-5 variables). Example: for a jumping game, plan: "jumpHeight: starts at 0, increases when space pressed, decreases each frame, read by sprite y-position." This planning skill prevents common bugs and builds design thinking.

Dependencies:
* T09.G4.13: Use a flag variable to track state (0/1 or true/false)
* T09.G4.16: Debug variable used before initialization

ID: T09.G4.25
Topic: T09 – Variables & Expressions
Skill: Identify when to create a new variable vs. reuse existing
Description: **Student task:** Students analyze code scenarios and decide whether to create a new variable or reuse an existing one. They understand trade-offs: (1) reusing saves memory but may overwrite needed data, (2) creating new variables makes code clearer but uses more memory. Example: calculating "totalWithTax = total * 1.08" - should we reuse "total" or create "totalWithTax"? Answer: create new variable to preserve both values. This decision-making skill builds variable lifecycle awareness.

Dependencies:
* T09.G4.21: Store intermediate calculation results in variables
* T09.G4.24: Plan variable lifecycle before coding

ID: T09.G4.26
Topic: T09 – Variables & Expressions
Skill: Justify variable design choices to a peer
Description: **Student task:** Students explain their variable design decisions to a classmate (or in written form). They answer questions like: "Why did you name this variable 'playerHealth' instead of 'h'?", "Why did you initialize lives to 3 instead of 0?", "Why did you use a separate highScore variable instead of reusing score?" This communication skill requires articulating reasoning, not just making correct choices. Students practice receiving feedback and considering alternative designs.

Dependencies:
* T09.G4.24: Plan variable lifecycle before coding
* T09.G4.25: Identify when to create a new variable vs. reuse existing

ID: T09.G4.27
Topic: T09 – Variables & Expressions
Skill: Predict result of nested operator blocks visually
Description: **Student task:** Students examine Scratch/CreatiCode block structures where operator blocks are nested inside each other and predict the result without running. Example: a visual block showing "( (3 + 5) * 2 )" - students identify that the inner block (3+5=8) evaluates first, then the outer block (8*2=16). They read the visual nesting structure to determine evaluation order. This visual literacy skill is essential for understanding how block-based expressions work differently from text formulas.

Dependencies:
* T09.G4.06: Combine two arithmetic operators in a single expression
* T09.G4.21: Store intermediate calculation results in variables

ID: T09.G4.28
Topic: T09 – Variables & Expressions
Skill: Write multi-step calculations as intermediate variable assignments
Description: **Student task:** Students convert complex calculations into a series of simple steps, each storing a result in a named intermediate variable. Example: Calculate total price with tax and discount. Instead of: "set finalPrice to (price * quantity) * (1 - discount) * (1 + taxRate)", write: "set subtotal to price * quantity", "set afterDiscount to subtotal * (1 - discount)", "set finalPrice to afterDiscount * (1 + taxRate)". They verify each step produces expected values. This skill emphasizes clarity and debuggability over compact expressions.

Dependencies:
* T09.G4.21: Store intermediate calculation results in variables
* T09.G4.27: Predict result of nested operator blocks visually

ID: T09.G4.29
Topic: T09 – Variables & Expressions
Skill: Identify subexpressions that can be computed independently
Description: **Student task:** Students analyze complex expressions and identify which parts can be computed independently (in parallel) vs which must wait for other results. Given "(a + b) * (c - d)", they identify that "a + b" and "c - d" can be computed independently, but the multiplication must wait for both. They practice: (1) Drawing dependency diagrams showing which operations depend on others, (2) Identifying "parallel" subexpressions in nested blocks, (3) Explaining why some operations must be sequential. This computational thinking skill builds understanding of data dependencies and prepares for parallel computing concepts.

Dependencies:
* T09.G4.06: Combine two arithmetic operators in a single expression
* T09.G4.27: Predict result of nested operator blocks visually

ID: T09.G4.30
Topic: T09 – Variables & Expressions
Skill: Implement count-up and count-down patterns with conditionals
Description: **Student task:** Students build both count-up and count-down counter patterns with conditional actions at threshold values. Count-up example: "set score to 0", "change score by 10", "if score >= 100 then broadcast level_up". Count-down example: "set timeLeft to 30", "change timeLeft by -1", "if timeLeft <= 0 then broadcast game_over". They implement both patterns and explain when each is appropriate (earning points vs depleting resources). This consolidates the counter pattern with conditional triggers.

Dependencies:
* T09.G3.17: Count occurrences using a counter variable
* T09.G4.09: Use equals (=) and less than (<) comparison operators in conditionals
* T09.G4.20: Build a countdown timer using variables

ID: T09.G4.31
Topic: T09 – Variables & Expressions
Skill: Debug wrong operator errors in expressions
Description: **Student task:** Students identify and fix bugs where the wrong arithmetic operator is used. Given buggy code like "set average to total + count" (should be /), they trace the expression, identify the symptom (average is way too large), recognize the wrong operator, and fix it. They practice: (1) "+" instead of "-" bugs (score goes up when it should go down), (2) "*" instead of "/" bugs (result is huge instead of small), (3) "/" instead of "*" bugs (result is fraction instead of large). This systematic approach to operator debugging builds precision in expression writing.

Dependencies:
* T09.G4.02: Use addition (+) in variable expressions
* T09.G4.03: Use subtraction (-) in variable expressions
* T09.G4.04: Use multiplication (*) in expressions
* T09.G4.05: Use division (/) in expressions
* T09.G4.12: Debug expression evaluation errors

ID: T09.G4.32
Topic: T09 – Variables & Expressions
Skill: Display variable using a Label Widget
Description: **Student task:** Students use the `set value to [variable] for widget [labelName]` block to display a variable's value on a Label Widget, instead of using the standard stage monitor. They understand this allows for better UI design (custom fonts, colors, positioning) and multiple displays. This introduces the concept of binding data (variable) to UI (widget).

Dependencies:
* T09.G3.03: Use variable reporter blocks in other blocks
* T09.G4.15: Choose appropriate variable display modes (normal, large, slider)

''')