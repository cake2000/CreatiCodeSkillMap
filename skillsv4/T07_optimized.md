ID: T07.K.01
Topic: T07 – Loops
Skill: Complete a repeating pattern
Description: Students drag pictures to fill in missing items in a simple repeating pattern (AB, AAB, or ABC patterns). For example, given "dog-cat-dog-cat-dog-?" they select "cat" from 3 choices. This picture-based activity builds foundational understanding of repetition without coding. Use 3-4 repetitions of the pattern with 1-2 missing items. Visual themes include animals, shapes, or everyday objects.

Dependencies:


ID: T07.G1.01
Topic: T07 – Loops
Skill: Count repetitions in a pattern
Description: Students count how many times a unit repeats in a given pattern and select the correct number. For example, shown a visual sequence of "jump-clap, jump-clap, jump-clap" they count 3 repetitions. Present 2-5 repetitions and use concrete, observable actions or objects. This develops the concept of "how many times" which is essential for understanding loop counts.

Dependencies:
* T07.K.01: Complete a repeating pattern


ID: T07.G1.02
Topic: T07 – Loops
Skill: Match "do N times" instructions to outcomes
Description: Students match a simple "do something N times" instruction to the correct visual outcome. For example, given "clap 4 times" they select the picture showing 4 claps (not 3 or 5). Use familiar actions like clapping, jumping, or stacking blocks. This connects the abstract concept of "repeat N times" to concrete results, preparing for the `repeat N` block in Grade 3.

Dependencies:
* T07.G1.01: Count repetitions in a pattern


ID: T07.G2.01
Topic: T07 – Loops
Skill: Identify when to use "repeat" vs "do once"
Description: Students sort simple task cards into two categories: "needs repeating" (like brushing all teeth, coloring all stars) vs "do only once" (like putting on a hat, opening a door). This picture-based classification develops the judgment of when repetition is needed, a key prerequisite for choosing between loops and sequential code. Use 6-8 task cards with clear yes/no answers.

Dependencies:
* T07.G1.02: Match "do N times" instructions to outcomes


ID: T07.G3.01
Topic: T07 – Loops
Skill: Use a counted repeat loop
Description: Students use their first `repeat N` loop to run a very simple sequence a small number of times (e.g., make a sprite jump exactly 3 times, or say "Hello!" 2 times). This gateway skill introduces the fundamental concept of repetition in programming by replacing obvious copy-pasted blocks. Start with 2-3 repetitions to keep cognitive load manageable.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"


ID: T07.G3.02
Topic: T07 – Loops
Skill: Trace a script with a simple loop
Description: Students read a very simple script with a single `repeat N` loop (N = 2-4) and predict how many times a basic action occurs or where a sprite ends up. Use concrete, visual actions like moving, stamping, or saying something. Focus on "this will happen 3 times" understanding rather than complex calculations.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T04.G3.03: Match a "repeat N" loop to repeated behavior


ID: T07.G3.03
Topic: T07 – Loops
Skill: Build a forever loop for simple animation
Description: Students create their first `forever` loop with a very simple action inside (e.g., turn 15 degrees, or next costume) to create basic continuous animation. Introduce "forever" as "repeat until you stop the program."

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T04.G3.04.01: Identify repeated code segments that could be simplified with templates


ID: T07.G3.04
Topic: T07 – Loops
Skill: Use repeat‑until to reach a simple goal
Description: Students use a very simple `repeat until <touching [goal]>` loop with a basic movement block to move a sprite towards a clearly visible target. The goal should be directly in the sprite's path to minimize complexity. Introduce this as "keep doing something until something else happens."

Dependencies:
* T07.G3.03: Build a forever loop for simple animation
* T08.G3.01: Use a simple if in a script


ID: T07.G3.04.01
Topic: T07 – Loops
Skill: Trace a repeat‑until loop step by step
Description: Students trace a simple `repeat until` loop by predicting the outcome of each iteration and determining when the stopping condition becomes true. For example, tracing a sprite moving step by step until it touches a target, or counting up until a variable reaches a certain value. This builds understanding of conditional loops before advancing to more complex uses. Use concrete examples with 3-5 iterations and clear stopping conditions.

Dependencies:
* T07.G3.04: Use repeat‑until to reach a simple goal


ID: T07.G3.05
Topic: T07 – Loops
Skill: Fix a simple repeat loop count
Description: Students inspect a simple script where a `repeat` loop has the wrong number (e.g., repeat 4 instead of repeat 3). The error is obvious and the fix is straightforward - just change the number in the repeat block. Focus is on recognizing that the loop count is wrong, not complex debugging.

Dependencies:
* T07.G3.02: Trace a script with a simple loop


ID: T07.G4.01
Topic: T07 – Loops
Skill: Create a forever game loop for controls
Description: Students implement a `forever` loop that continuously checks keyboard input and moves the sprite accordingly, instead of responding only once. This is the first time they build a persistent game loop after tracing one in Grade 3.

Dependencies:
* T07.G3.03: Build a forever loop for simple animation
* T08.G3.01: Use a simple if in a script


ID: T07.G4.02
Topic: T07 – Loops
Skill: Use an if statement inside a loop
Description: Students write a loop (repeat or forever) that contains an if block inside it, combining iteration with conditional logic. Examples include checking for collisions each frame, or processing items differently based on their values.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T08.G3.01: Use a simple if in a script


ID: T07.G4.03
Topic: T07 – Loops
Skill: Use a manual loop counter variable
Description: Students create and use a counter variable that they manually increment on each loop iteration (e.g., to show "Step 1, Step 2, …" or to track how many loops have run). They initialize the counter before the loop (set counter to 0), then use a `change counter by 1` block inside a repeat loop. This teaches the fundamental mechanics of counting iterations and prepares students for understanding for-loops as an abstraction of this pattern.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T09.G3.01.01: Create a new variable with a descriptive name
* T09.G3.01.02: Set a variable to an initial value at program start


ID: T07.G4.03.01
Topic: T07 – Loops
Skill: Use a basic for-loop with start, limit, and step
Description: Students use CreatiCode's `for [variable] from (START) to (LIMIT) at step (S)` block to create loops with automatic counters. They learn that for-loops provide a built-in loop variable that automatically increments, eliminating the need to manually initialize and increment counters. Start with simple cases using step 1 and various start/limit values (e.g., from 1 to 10, from 0 to 5). Students understand this as a cleaner alternative to manual counter variables.

Dependencies:
* T07.G4.03: Use a manual loop counter variable


ID: T07.G4.03.02
Topic: T07 – Loops
Skill: Use for-loops to count by different step sizes
Description: Students practice using for-loops with different step sizes to count by 2s, 5s, 10s, or other increments. For example: loop from 0 to 20 step 2 to get even numbers, or from 5 to 50 step 5 to count by fives. They apply this to create patterns, animations with varying spacing, or generate sequences for calculations. This reinforces understanding of the step parameter and multiplication patterns.

Dependencies:
* T07.G4.03.01: Use a basic for-loop with start, limit, and step


ID: T07.G4.03.03
Topic: T07 – Loops
Skill: Use for-loops to count backwards
Description: Students use negative step values in for-loops to count backwards (e.g., from 10 to 1 step -1 for a countdown, or from 100 to 0 step -5). They understand that when step is negative, the start value should be larger than the limit value. Common applications include countdown timers, reverse animations, or processing items in reverse order. This completes their understanding of for-loop flexibility.

Dependencies:
* T07.G4.03.01: Use a basic for-loop with start, limit, and step


ID: T07.G4.04
Topic: T07 – Loops
Skill: Identify and convert simple repeated code into loops
Description: Students recognize when a script contains the same sequence of blocks repeated multiple times (e.g., move-turn-stamp copied 4 times) and rewrite it using a simple `repeat N` loop where N equals the number of repetitions. The repeated blocks are identical—no variables or changing values involved. Students verify the refactored code produces identical behavior.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T07.G3.02: Trace a script with a simple loop


ID: T07.G4.05
Topic: T07 – Loops
Skill: Debug complex loop conditions and boundaries
Description: Students debug more complex loop problems involving counter variables, repeat-until conditions, or off-by-one errors. Unlike G3.05's simple count fix, this requires analyzing how the loop condition interacts with variables and understanding boundary cases.

Dependencies:
* T07.G3.04: Use repeat‑until to reach a simple goal
* T07.G4.03: Use a manual loop counter variable
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T13.G3.01: Test and trace simple block-based scripts


ID: T07.G4.06
Topic: T07 – Loops
Skill: Trace code that combines a loop and a condition
Description: Students trace a script with a loop that contains an `if` block (e.g., bouncing off edges) to predict behavior after several iterations.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T07.G3.04: Use repeat‑until to reach a simple goal
* T08.G3.01: Use a simple if in a script
* T13.G3.01: Test and trace simple block-based scripts


ID: T07.G4.07
Topic: T07 – Loops
Skill: Trace simple nested loops with fixed bounds
Description: Students trace a simple script with two nested loops using fixed repeat counts (e.g., outer loop repeats 3 times, inner loop repeats 2 times) to predict total iterations and final outcomes. Use small iteration counts (2-3 each) and concrete visual actions like drawing or stamping. The loop bounds are constant numbers, not variables. This prepares students for building nested loops in Grade 5.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T07.G4.03: Use a manual loop counter variable
* T07.G4.06: Trace code that combines a loop and a condition
* T13.G3.01: Test and trace simple block-based scripts


ID: T07.G4.08
Topic: T07 – Loops
Skill: Use timed repeat for spaced animations
Description: Students use CreatiCode's `repeat (N) times at intervals of (T)` block to create animations where actions happen with visible pauses between them (e.g., a countdown timer showing 3...2...1, a character blinking every 0.5 seconds, or a sprite moving in discrete steps). This block automatically handles timing without needing a `wait` block inside the loop, making code cleaner and timing more precise.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T07.G4.01: Create a forever game loop for controls


ID: T07.G5.01
Topic: T07 – Loops
Skill: Simulate repeated experiments with a loop
Description: Students simulate a simple chance experiment repeatedly in code using a loop, and use counter variables to track outcomes and observe frequencies. For example: roll a die 100 times and count how many times each number appears; flip a coin 50 times and track heads vs. tails; or spin a spinner repeatedly to see if outcomes match expected probabilities. Students initialize counters to 0, use a repeat loop, generate random outcomes, increment the appropriate counter, and display results. This connects loops to data collection and probability.

Dependencies:
* T07.G4.03: Use a manual loop counter variable
* T07.G4.06: Trace code that combines a loop and a condition
* T10.G3.05: Use random values in code
* T10.G4.18: Use random numbers to model chance or variety
* T09.G5.01: Use multiple variables together in a single expression
* T04.G5.01: Recognize a counter update pattern


ID: T07.G5.02
Topic: T07 – Loops
Skill: Build a list with a loop
Description: Students write a loop that populates a list with a sequence of values or with repeated samples from user input. Common patterns include: (1) sequential numbers (loop from 1 to 10, add each to list), (2) user input collection (repeat N times, ask for name/score and add to list), or (3) calculated values (loop through numbers and add their squares to a list). Students practice initializing an empty list, using add-to-list blocks inside loops, and verifying the final list contents.

Dependencies:
* T07.G4.03: Use a manual loop counter variable
* T10.G5.01: Create and populate a list with items
* T10.G3.05: Use random values in code
* T10.G4.18: Use random numbers to model chance or variety
* T09.G5.01: Use multiple variables together in a single expression
* T04.G5.01: Recognize a counter update pattern


ID: T07.G5.03
Topic: T07 – Loops
Skill: Use loops to compute aggregates
Description: Students loop over items in a list (or through repeated events) to compute a total or average (e.g., total points from several rounds), using an accumulator variable.

Dependencies:
* T07.G4.03: Use a manual loop counter variable
* T07.G4.06: Trace code that combines a loop and a condition
* T10.G3.05: Use random values in code
* T10.G4.18: Use random numbers to model chance or variety
* T06.G5.01: Identify standard event patterns in a small game
* T09.G5.01: Use multiple variables together in a single expression
* T04.G5.01: Recognize a counter update pattern


ID: T07.G5.04
Topic: T07 – Loops
Skill: Nested loops for advanced patterns or tilings
Description: Students design or reproduce more complex tilings or repeating art (checkerboards, stripes, simple mosaics) using nested loops and coordinate changes, reinforcing multiplicative reasoning and spatial thinking.

Dependencies:
* T07.G4.05: Debug complex loop conditions and boundaries
* T07.G4.07: Trace simple nested loops with fixed bounds
* T10.G3.05: Use random values in code
* T10.G4.18: Use random numbers to model chance or variety
* T04.G5.01: Recognize a counter update pattern


ID: T07.G5.04.01
Topic: T07 – Loops
Skill: Build simple nested loops
Description: Students write their first nested loop structure by placing one loop inside another. Start with concrete tasks like creating a simple grid pattern (e.g., 3 rows of 4 stamps each) or repeating a short sequence multiple times. The outer loop controls how many groups, the inner loop controls repetitions within each group. Use small fixed counts (2-4 iterations each) and visual feedback to make the nested structure clear. This scaffolding skill prepares students for analyzing variable bounds in nested loops.

Dependencies:
* T07.G4.07: Trace simple nested loops with fixed bounds


ID: T07.G6.01
Topic: T07 – Loops
Skill: Trace nested loops with variable bounds
Description: Students analyze code with nested loops where the inner loop bound depends on the outer loop counter (e.g., `for i from 1 to n` outer, `repeat (n - i)` inner). The key challenge is understanding that the inner loop executes a different number of times for each outer iteration, requiring calculation to predict total iterations. Unlike G4.07's constant bounds, students must reason about changing iteration counts and track how the loop variable affects inner bounds.

Dependencies:
* T07.G4.03.01: Use a basic for-loop with start, limit, and step
* T07.G5.03: Use loops to compute aggregates
* T07.G5.04: Nested loops for advanced patterns or tilings
* T07.G5.04.01: Build simple nested loops
* T09.G4.01: Use variables to store and update game state


ID: T07.G6.02
Topic: T07 – Loops
Skill: Refactor complex repeated patterns into loops with variables
Description: Students refactor longer scripts where the repeated segments have slight variations (e.g., "move 10, move 20, move 30" becomes a loop with a changing variable). Unlike G4.04's identical repetitions, this requires using a for-loop to handle the pattern. Students analyze the variation pattern and express it mathematically (e.g., recognizing that "10, 20, 30" follows the pattern `i * 10` where i goes from 1 to 3). This develops competition-level generalization skills.

Dependencies:
* T07.G4.03.01: Use a basic for-loop with start, limit, and step
* T07.G4.04: Identify and convert simple repeated code into loops
* T07.G5.04: Nested loops for advanced patterns or tilings


ID: T07.G6.03
Topic: T07 – Loops
Skill: Loop‑based search in a list
Description: Students implement a simple linear search using a for-each loop to find the first item in a list that matches a target (e.g., find the first score above 90), and then respond (e.g., report the position or value). They use conditional logic inside the loop to check each item and a flag or result variable to track whether the target was found.

Dependencies:
* T07.G5.02: Build a list with a loop
* T07.G6.09.01: Use for-each item to iterate over list values
* T08.G4.01: Use if-then-else in a project


ID: T07.G6.04
Topic: T07 – Loops
Skill: Avoid and fix infinite loops
Description: Students identify scripts that never stop because of improper use of `forever` or `repeat until` with a condition that never becomes true. They modify the code to add a stopping condition or use the `break out of loop` block appropriately.

Dependencies:
* T07.G4.05: Debug complex loop conditions and boundaries
* T07.G6.08.01: Use break to exit a loop early


ID: T07.G6.05
Topic: T07 – Loops
Skill: Trace nested loops with abstract calculations using trace tables
Description: Students use trace tables to systematically track variable values through nested loops that perform abstract calculations (e.g., computing sums, products, or counts). They create a table with columns for each variable (outer counter, inner counter, accumulator) and rows for each iteration, filling in values step-by-step. Focus is on loops where the output is numerical rather than spatial. Examples include: calculating factorial with nested loops, summing products of row/column indices, or counting items that meet complex conditions. This methodical approach is essential for debugging complex loop logic and succeeding in programming competitions.

Dependencies:
* T07.G5.03: Use loops to compute aggregates
* T07.G5.04: Nested loops for advanced patterns or tilings
* T09.G4.01: Use variables to store and update game state


ID: T07.G6.06
Topic: T07 – Loops
Skill: Trace nested loops that generate spatial patterns
Description: Students trace nested loops that produce visual/spatial output where row and column counters control position (e.g., drawing a checkerboard, creating a grid of stamps, or generating triangle patterns). They predict the visual result by understanding how loop iteration numbers map to spatial coordinates (x, y positions). Unlike G6.05's focus on abstract calculations, this skill connects loop tracing to concrete spatial reasoning. Students may use trace tables but the emphasis is on visualizing the 2D output pattern, not just tracking numerical values.

Dependencies:
* T07.G6.05: Trace nested loops with abstract calculations using trace tables
* T07.G5.04: Nested loops for advanced patterns or tilings


ID: T07.G6.07
Topic: T07 – Loops
Skill: Use loops to update values iteratively
Description: Students implement loops that repeatedly update a variable based on its previous value (e.g., adding interest each year, reducing health points each turn, or growing/shrinking a value by a percentage). This bridges statistical simulations to physics-based motion by focusing on the concept of iterative state change.

Dependencies:
* T07.G5.01: Simulate repeated experiments with a loop
* T07.G5.03: Use loops to compute aggregates
* T07.G6.05: Trace nested loops with abstract calculations using trace tables


ID: T07.G6.08.01
Topic: T07 – Loops
Skill: Use break to exit a loop early
Description: Students use CreatiCode's `break` block to exit a loop immediately when a specific condition is met, without completing all planned iterations. Common applications include: stopping a search loop once the target item is found, exiting a game loop when a win/lose condition occurs, or terminating input collection when a sentinel value is entered. Students learn that break makes code more efficient by avoiding unnecessary iterations and clearer than complex nested conditionals.

Dependencies:
* T07.G5.02: Build a list with a loop
* T07.G6.03: Loop‑based search in a list


ID: T07.G6.08.02
Topic: T07 – Loops
Skill: Use continue to skip loop iterations
Description: Students use CreatiCode's `continue` block to skip the rest of the current iteration and immediately start the next one. This is useful for filtering or conditional processing, such as: skipping invalid items in a list without processing them, ignoring even numbers when processing odds, or bypassing error cases without stopping the loop. Students understand that continue is clearer than wrapping the entire loop body in an if statement.

Dependencies:
* T07.G5.02: Build a list with a loop
* T07.G6.08.01: Use break to exit a loop early


ID: T07.G6.09.01
Topic: T07 – Loops
Skill: Use for-each item to iterate over list values
Description: Students use CreatiCode's `for each item [variable] in [list]` block to process all items in a list sequentially, with the loop variable taking on each value. For example: say each word in a sentence list, draw each number from a score list, or check each name for a match. Students learn when for-each loops are clearer than manually indexed loops because they focus on values rather than positions. This is especially useful when the item's value matters but its position doesn't.

Dependencies:
* T07.G5.02: Build a list with a loop
* T10.G5.01: Create and populate a list with items


ID: T07.G6.09.02
Topic: T07 – Loops
Skill: Use for-each index to iterate over list positions
Description: Students use CreatiCode's `for each index [variable] in [list]` block to iterate over list positions (indices) rather than values. This variant is useful when: you need both the position and value (access via "item [index] of [list]"), you want to modify list items in place, or you need to work with corresponding positions in multiple lists. Students compare when to use for-each item (value-focused) vs for-each index (position-focused).

Dependencies:
* T07.G6.09.01: Use for-each item to iterate over list values


ID: T07.G7.01
Topic: T07 – Loops
Skill: Use loops to simulate motion over time
Description: Students implement a loop that repeatedly updates position (and optionally velocity) to simulate motion with physics-like rules. Examples include: (1) gravity simulation - each frame, change y by velocity, then change velocity by -0.5 to simulate falling; (2) friction/sliding - each frame, change x by speed, then multiply speed by 0.9 to slow down; (3) bouncing - update position, check for edge collision, reverse velocity if touching edge. Students use forever loops or repeat loops with iterative state updates to create realistic motion effects.

Dependencies:
* T07.G6.05: Trace nested loops with abstract calculations using trace tables
* T07.G6.06: Trace nested loops that generate spatial patterns
* T07.G6.07: Use loops to update values iteratively


ID: T07.G7.02
Topic: T07 – Loops
Skill: Nested loops for 2D grids and tile maps
Description: Students use two loops to process a conceptual 2D grid (e.g., rows and columns of tiles), even if represented as positions or a 1D list plus indices, introducing matrix‑like reasoning.

Dependencies:
* T07.G6.05: Trace nested loops with abstract calculations using trace tables
* T07.G6.06: Trace nested loops that generate spatial patterns
* T08.G6.01: Use conditionals to control simulation steps


ID: T07.G7.03
Topic: T07 – Loops
Skill: Compare loop algorithms by counting steps
Description: Students compare two loop‑based solutions that both solve the same problem but use different numbers of iterations (e.g., repeated subtraction vs direct arithmetic) and reason about which is more efficient for larger inputs.

Dependencies:
* T07.G6.05: Trace nested loops with abstract calculations using trace tables
* T07.G6.07: Use loops to update values iteratively
* T08.G6.01: Use conditionals to control simulation steps


ID: T07.G7.04
Topic: T07 – Loops
Skill: Loop patterns for counting and accumulation
Description: Students identify and/or construct loops that follow common accumulator patterns (counting, summing, tracking min/max), distinguishing them from unrelated code.

Dependencies:
* T07.G6.05: Trace nested loops with abstract calculations using trace tables
* T07.G6.07: Use loops to update values iteratively
* T08.G6.01: Use conditionals to control simulation steps


ID: T07.G8.01
Topic: T07 – Loops
Skill: Monte Carlo simulations with loops
Description: Students design loop‑based simulations that approximate probabilities (e.g., estimate chance of rolling a sum ≥ 9 with two dice) and interpret the results in terms of experimental vs theoretical probability.

Dependencies:
* T07.G6.01: Trace nested loops with variable bounds
* T07.G7.03: Compare loop algorithms by counting steps
* T07.G7.04: Loop patterns for counting and accumulation


ID: T07.G8.02
Topic: T07 – Loops
Skill: Analyze iterative algorithms to identify components
Description: Students analyze existing iterative algorithms (like GCD, primality testing, Fibonacci) to identify three key components: (1) initial state setup (variable initialization), (2) update rule that moves closer to the goal (how values change each iteration), and (3) stopping condition (when the loop exits). This analytical skill helps students understand algorithm structure and prepares them for algorithm design competitions and advanced CS courses. Students practice by examining code and labeling which parts serve each purpose.

Dependencies:
* T01.G6.01: Count comparisons in linear and binary search
* T07.G6.01: Trace nested loops with variable bounds
* T07.G7.03: Compare loop algorithms by counting steps


ID: T07.G8.02.01
Topic: T07 – Loops
Skill: Implement GCD using repeated subtraction in a loop
Description: Students implement the Euclidean algorithm for finding the greatest common divisor by repeatedly subtracting the smaller number from the larger until they are equal. This introduces the concept of iterative reduction. They initialize two variables with input values, use a repeat-until loop that continues while the values differ, and update by subtracting the smaller from the larger each iteration.

Dependencies:
* T07.G8.02: Analyze iterative algorithms to identify components
* T09.G6.01: Model real-world quantities using variables and formulas
* T08.G6.01: Use conditionals to control simulation steps


ID: T07.G8.02.02
Topic: T07 – Loops
Skill: Check if a number is prime using trial division
Description: Students write a loop that tests whether a number is prime by checking divisibility from 2 up to the square root of the number. They initialize a flag variable to track whether any divisor was found, loop through potential divisors, and use a conditional to check remainder. Students learn to optimize by breaking early when a divisor is found.

Dependencies:
* T07.G8.02: Analyze iterative algorithms to identify components
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas


ID: T07.G8.02.03
Topic: T07 – Loops
Skill: Find Fibonacci numbers using iterative calculation
Description: Students implement an iterative algorithm to generate Fibonacci numbers, maintaining two variables (previous and current) that are repeatedly updated in a loop. They initialize the first two values, use a counted loop for the desired position, and update both variables each iteration (current becomes previous, sum becomes new current). This demonstrates state management in iterative algorithms.

Dependencies:
* T07.G8.02: Analyze iterative algorithms to identify components
* T09.G6.01: Model real-world quantities using variables and formulas
* T08.G6.01: Use conditionals to control simulation steps


ID: T07.G8.03
Topic: T07 – Loops
Skill: Process structured data with nested loops
Description: Students use nested loops to process 2D‑structured data (e.g., a list encoding grid values, or two parallel lists) and compute statistics like row/column sums or counts of certain cells.

Dependencies:
* T07.G6.01: Trace nested loops with variable bounds
* T07.G7.03: Compare loop algorithms by counting steps
* T07.G7.04: Loop patterns for counting and accumulation


ID: T07.G8.04
Topic: T07 – Loops
Skill: Analyze and justify loop design choices
Description: Students compare different loop structures for the same problem (e.g., `repeat until` vs counted `repeat` with inner condition, or `forever` with break vs bounded loop) and justify which is more appropriate. They consider factors like: guaranteed termination, handling edge cases, readability, and efficiency for different input sizes.

Dependencies:
* T07.G6.01: Trace nested loops with variable bounds
* T07.G7.03: Compare loop algorithms by counting steps
* T07.G7.04: Loop patterns for counting and accumulation
