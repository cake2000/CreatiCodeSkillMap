# T07 – Loops: K–8 Skill List (Draft v1)

Topic reference: `T07 Loops` in `domains_topics_overview.md`  
Domain: Programming (D2) · CSTA focus: PRO‑PF, ALG‑AF (with links to PRO‑TR, DAA‑DF/DP, DAA‑DI)

Each skill below has:

- a stable **ID** (`T07.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Scope in v3:** Loops as a programming construct are taught and assessed from **Grade 3–8** in this topic. K–2 repetition and pattern concepts are handled in T01 (everyday algorithms) and T04 (algorithm patterns); T07 assumes those foundations and begins when students start block‑based coding.

---

## Grade 3

Grade 3 introduces loops in a gentle progression: fixed-count repeat → trace simple repeat → forever for simple animation → repeat until for goals → debug count errors.

### T07.G3.01 – Use a counted repeat loop

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T04.G1.01: Match a picture pattern to a movement pattern
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T01.G2.05: Complete a simple if/then algorithm


- **Short name:** Repeat N times for a task  
- **Description:** Students use their first `repeat N` loop to run a very simple sequence a small number of times (e.g., make a sprite jump exactly 3 times, or say "Hello!" 2 times). This gateway skill introduces the fundamental concept of repetition in programming by replacing obvious copy-pasted blocks. Start with 2-3 repetitions to keep cognitive load manageable.  
- **Challenge format:** Coding, highly scaffolded starter project with step-by-step guidance. Provided: a script with 2-3 identical blocks in a row (such as `move 10` repeated exactly 3 times). Students replace the repeated blocks with a `repeat` loop that has the correct count and body, with clear visual guidance. Auto‑grading checks that a `repeat` loop is present, that the count matches the intended behavior, and that the final behavior matches a reference solution.  
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑AF‑01. ⭐ Gateway

### T07.G3.02 – Trace a script with a simple loop

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T04.G3.02: Match a “repeat N” loop to repeated behavior
  * T07.G2.02: Unknown skill


- **Short name:** Trace a repeat loop and count actions  
- **Description:** Students read a very simple script with a single `repeat N` loop (N = 2-4) and predict how many times a basic action occurs or where a sprite ends up. Use concrete, visual actions like moving, stamping, or saying something. Focus on "this will happen 3 times" understanding rather than complex calculations.  
- **Challenge format:** Concept, code‑reading item with visual support. Show a script such as `repeat 3 { move 10 steps }` or `repeat 2 { stamp }` and ask "How many stamps will you see?" or "How far will the sprite move in total?" with multiple choice answers. Auto‑grading compares answers to the loop count and simple arithmetic.  
- **CSTA:** E3‑ALG‑AF‑01, E3‑PRO‑PF‑01.

### T07.G3.03 – Build a forever loop for simple animation

_Dependency:_
  * T07.G3.02: Trace a script with a simple loop
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T04.G3.03: Recognize a simple project template


- **Short name:** Forever loop for animation  
- **Description:** Students create their first `forever` loop with a very simple action inside (e.g., turn 15 degrees, or next costume) to create basic continuous animation. Introduce "forever" as "repeat until you stop the program."  
- **Challenge format:** Coding, scaffolded starter project with clear action choices; auto‑graded by presence of forever loop and continuous behavior.  
- **CSTA:** E3‑PRO‑PF‑01.

### T07.G3.04 – Use repeat‑until to reach a simple goal

_Dependency:_
  * T07.G3.03: Build a forever loop for simple animation
  * T08.G3.02: Decide when a single if is enough
  * T09.G3.02: Use a variable in a conditional (if block)


- **Short name:** Repeat until you reach the flag  
- **Description:** Students use a very simple `repeat until <touching [goal]>` loop with a basic movement block to move a sprite towards a clearly visible target. The goal should be directly in the sprite's path to minimize complexity. Introduce this as "keep doing something until something else happens."  
- **Challenge format:** Coding, highly scaffolded starter project. Provided: sprite positioned directly facing the goal, goal object, and partial script with a simple move block. Students wrap the move in a `repeat until` loop with a pre-selected condition. Auto‑grading checks correct loop type and that the sprite stops on the goal.  
- **CSTA:** E3‑PRO‑PF‑01.

### T07.G3.05 – Fix a loop that runs too many or too few times

_Dependency:_
  * T07.G3.04: Use repeat‑until to reach a simple goal
  * T08.G3.03: Pick the right conditional block for a scenario
  * T09.G3.02: Use a variable in a conditional (if block)


- **Short name:** Debug the loop count  
- **Description:** Students inspect a simple script where a `repeat` loop makes the sprite do something obviously wrong (e.g., jumping 4 times instead of 3, clearly visible difference). This contextualized debugging skill teaches debugging as a natural part of learning loops. The error should be obvious and the fix straightforward (change one number).  
- **Challenge format:** Coding, scaffolded debugging. Starter project shows a clear expected behavior description and demo; students identify that the count is wrong and change only the loop count number. Auto‑grading checks final behavior and that a `repeat` loop remains in use.  
- **CSTA:** E3‑PRO‑TR‑01, E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 deepens loop usage with more complex conditions, counters, and refinement of existing loop code.

### T07.G4.01 – Create a forever game loop for controls

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script


- **Short name:** Forever loop for player controls  
- **Description:** Students implement a `forever` loop that continuously checks keyboard input and moves the sprite accordingly, instead of responding only once. This is the first time they build a persistent game loop after tracing one in Grade 3.  
- **Challenge format:** Coding, starter project. Provided: a sprite and `if key pressed` blocks outside any loop. Students put these inside a `forever` loop triggered by `when green flag clicked`. Auto‑grading runs the project and checks that holding or repeatedly pressing keys moves the sprite smoothly and that no duplicate code exists outside the loop.  
- **CSTA:** E4‑PRO‑PF‑01.

### T07.G4.02 – Loop with a condition inside

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.04: Use repeat‑until to reach a simple goal
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Loop with checks inside  
- **Description:** Students write a loop where each repeated step also contains a conditional, such as moving and bouncing off edges or adding to a score only when touching a coin.  
- **Challenge format:** Coding, starter project. Example: a ball moves across the screen; students wrap movement in a `repeat` or `forever` loop and add an `if on edge, bounce` or `if touching coin then change score`. Auto‑grading checks that (1) movement loop is present, (2) the condition is inside the loop, and (3) behavior (bouncing or scoring) occurs multiple times as appropriate.  
- **CSTA:** E4‑PRO‑PF‑01.

### T07.G4.03 – Use a loop counter variable

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Use a counter inside a loop  
- **Description:** Students maintain a numeric counter variable that increments on each loop iteration (e.g., to show “Step 1, Step 2, …” or to track how many loops have run), introducing a “for loop” pattern using Scratch‑style blocks.  
- **Challenge format:** Coding, starter project. Students create a variable (e.g., `step`) and initialize it, then inside a `repeat` loop they change `step by 1` and display it (`say step`). Auto‑grading ensures (1) variable initialization, (2) update inside the loop, and (3) correct final value after execution.  
- **CSTA:** E4‑PRO‑PF‑01, E4‑ALG‑AF‑01.

### T07.G4.04 – Convert repeated blocks with conditions into loops

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.04: Use repeat‑until to reach a simple goal
  * T08.G3.01: Use a simple if in a script


- **Short name:** Refactor repeated code with a loop  
- **Description:** Students are given a longer script with repeated groups of blocks (including conditionals) and asked to rewrite it using a loop to reduce duplication, preserving behavior. This builds code quality and abstraction skills.  
- **Challenge format:** Coding, refactor challenge. Starter script might contain 4 identical “move 10, if touching star change score by 1” sequences. Students rewrite using a `repeat` loop. Auto‑grading checks code structure (loop present, one copy of the body) and behavior equivalence (same final score for a fixed setup).  
- **CSTA:** E4‑PRO‑PF‑01, PRO‑TR.

### T07.G4.05 – Analyze and fix a loop bug

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.04: Use repeat‑until to reach a simple goal
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Find the bug in a loop  
- **Description:** Students examine a script where a loop runs too many or too few times, or the counter/condition is incorrect, and modify it to match the intended behavior. They practice reasoning about loop boundaries and conditions.  
- **Challenge format:** Coding, debugging. A starter project shows expected behavior (e.g., character should jump exactly 3 times), but the given loop makes it jump 4 times or 2 times. Students adjust the loop count or condition. Auto‑grading compares final behavior to a reference solution.  
- **CSTA:** E4‑PRO‑TR‑01 (testing and refining).

### T07.G4.06 – Trace code that combines a loop and a condition

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.04: Use repeat‑until to reach a simple goal
  * T08.G3.01: Use a simple if in a script


- **Short name:** Trace loop with condition  
- **Description:** Students trace a script with a loop that contains an `if` block (e.g., bouncing off edges) to predict behavior after several iterations.  
- **Challenge format:** Code‑reading or step‑through; auto‑graded by final state.  
- **CSTA:** E4‑ALG‑AF‑01, E4‑ALG‑PS‑03.

---

## Grade 5

Grade 5 uses loops for simulations, data collection, and more complex patterns.

### T07.G5.01 – Simulate repeated experiments with a loop

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G4.05: Analyze and fix a loop bug
  * T07.G4.06: Trace code that combines a loop and a condition
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Run an experiment many times with a loop  
- **Description:** Students simulate a simple chance experiment (e.g., rolling a die, flipping a coin) repeatedly in code using a loop, and count outcomes to observe frequencies. This connects loops to data and probability.  
- **Challenge format:** Coding, starter project. Provided: a `pick random` block and a `when green flag clicked` script stub. Students add a `repeat` loop (e.g., 20 trials), update counts in variables, and optionally report results. Auto‑grading checks that the loop runs the correct number of iterations and that the count variables update correctly.  
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DP/DI.

### T07.G5.02 – Build a list with a loop

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G4.05: Analyze and fix a loop bug
  * T07.G4.06: Trace code that combines a loop and a condition
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Fill a list using a loop  
- **Description:** Students write a loop that populates a list with a sequence of values (e.g., the numbers 1 to 10) or with repeated samples from user input or sensors.  
- **Challenge format:** Coding, starter project with an empty list. Students initialize a variable, use a `repeat` or `repeat until` loop, and `add` values to the list each iteration. Auto‑grading checks list content after execution and that there’s no manual duplication.  
- **CSTA:** E5‑PRO‑PF‑01, PRO‑DH, DAA‑DF.

### T07.G5.03 – Use loops to compute aggregates

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T07.G4.06: Trace code that combines a loop and a condition
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Use a loop to total scores  
- **Description:** Students loop over items in a list (or through repeated events) to compute a total or average (e.g., total points from several rounds), using an accumulator variable.  
- **Challenge format:** Coding, starter project with a list of numbers. Students initialize a `total` variable, loop and `change total by item`, then display `total`. Auto‑grading checks the accumulator pattern and final value.  
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DP.

### T07.G5.04 – Nested loops for advanced patterns or tilings

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G4.05: Analyze and fix a loop bug
  * T07.G4.06: Trace code that combines a loop and a condition
  * T08.G3.01: Use a simple if in a script


- **Short name:** Nested loops for complex patterns  
- **Description:** Students design or reproduce more complex tilings or repeating art (checkerboards, stripes, simple mosaics) using nested loops and coordinate changes, reinforcing multiplicative reasoning and spatial thinking.  
- **Challenge format:** Coding, creative challenge with auto‑check. The system provides a target pattern; students implement nested loops to approximate it. Auto‑grading uses image similarity and/or code structure checks (two nested loops with appropriate counts).  
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DI.

---

## Grade 6

In middle school, loops become part of analyzing and designing general algorithms; students both trace and construct more abstract loop patterns.

### T07.G6.01 – Trace nested loops with variables

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G5.03: Use loops to compute aggregates
  * T07.G5.04: Nested loops for advanced patterns or tilings
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Trace nested loops and variables  
- **Description:** Students analyze code with nested loops and variable updates (e.g., counters or sums), predicting final variable values and number of iterations.  
- **Challenge format:** Concept, code‑reading item. Show code with two nested loops updating variables; students answer questions like “What is the final value of `sum`?” Auto‑grading uses static analysis or simulation.  
- **CSTA:** MS‑PRO‑PF‑01.

### T07.G6.02 – Refactor repeated code into loops

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T07.G5.04: Nested loops for advanced patterns or tilings
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Turn repeated code into a loop  
- **Description:** Students are given longer scripts with clearly repeated segments and asked to refactor them into loops—possibly with a loop counter variable—while preserving behavior. This develops generalization and refactoring skills important for competitions.  
- **Challenge format:** Coding, refactor challenge. Projects include repeated movement, drawing, or text output sequences. Auto‑grading compares behavior and checks that repetition is handled by loop blocks rather than by copy‑paste.  
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T07.G6.03 – Loop‑based search in a list

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G5.03: Use loops to compute aggregates
  * T07.G5.04: Nested loops for advanced patterns or tilings
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Search a list using a loop  
- **Description:** Students implement a simple linear search using a loop to find the first item in a list that matches a target (e.g., find the first score above 90), and then respond (e.g., report the position).  
- **Challenge format:** Coding, starter project with a list and a target value. Students write a `repeat until` or `repeat` loop with an index variable or for‑each pattern. Auto‑grading seeds the list with test cases and checks for correct results and use of a loop.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP.

### T07.G6.04 – Avoid and fix infinite loops

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T07.G5.04: Nested loops for advanced patterns or tilings
  * T08.G3.01: Use a simple if in a script


- **Short name:** Find and fix infinite loops  
- **Description:** Students identify scripts that never stop because of improper use of `forever` or `repeat until` with a condition that never becomes true. They modify the code to add a stopping condition or break behavior appropriately.  
- **Challenge format:** Coding and concept, debugging. Starter projects include one or two scripts that hang. Students adjust conditions or add a `stop this script` or equivalent structure. Auto‑grading checks that the script terminates or behaves as specified under test inputs.  
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T07.G6.05 – Trace nested loops with a table of values

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G5.03: Use loops to compute aggregates
  * T07.G5.04: Nested loops for advanced patterns or tilings
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Trace nested loops and variables  
- **Description:** Students trace code with nested loops and track changes to one or two variables in a table, predicting final values or patterns.  
- **Challenge format:** Concept, code‑reading item. Show code with two nested loops updating variables; students answer questions like “What is the final value of `sum`?” Auto‑grading uses static analysis or simulation.  
- **CSTA:** MS‑PRO‑PF‑01.

### T07.G6.06 – Trace nested loops that fill a grid pattern

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G5.03: Use loops to compute aggregates
  * T07.G5.04: Nested loops for advanced patterns or tilings
  * T08.G3.01: Use a simple if in a script


- **Short name:** Trace nested loops for grids  
- **Description:** Students trace nested loops that draw or fill a 2D grid (e.g., checkerboard), predicting how many cells are filled or what pattern appears.  
- **Challenge format:** Code‑reading + grid visualization; auto‑graded by predicted pattern.  
- **CSTA:** MS‑ALG‑AF‑01, MS‑ALG‑PS‑05.

---

## Grade 7

Grade 7 emphasizes loop patterns that underpin standard algorithms and simulations.

### T07.G7.01 – Use loops to simulate motion over time

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.02: Trace a script with a simple loop
  * T07.G6.05: Trace nested loops with a table of values
  * T07.G6.06: Trace nested loops that fill a grid pattern


- **Short name:** Loop for step‑by‑step simulation  
- **Description:** Students implement a loop that repeatedly updates position (and optionally velocity) to simulate motion, such as an object sliding or falling with a simple rule each step.  
- **Challenge format:** Coding, starter project. Provided variables `x`, `v`, etc.; students create a loop that updates them each tick and animate a sprite accordingly. Auto‑grading checks for correct update pattern and plausible behavior over time.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T07.G7.02 – Nested loops for 2D grids and tile maps

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G6.05: Trace nested loops with a table of values
  * T07.G6.06: Trace nested loops that fill a grid pattern
  * T08.G3.01: Use a simple if in a script


- **Short name:** Nested loops for grid processing  
- **Description:** Students use two loops to process a conceptual 2D grid (e.g., rows and columns of tiles), even if represented as positions or a 1D list plus indices, introducing matrix‑like reasoning.  
- **Challenge format:** Coding, starter project with grid layout. Students implement nested loops to place tiles or check conditions across the grid. Auto‑grading checks the pattern of positions visited and any computed counts.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP.

### T07.G7.03 – Compare loop algorithms by counting steps

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G6.05: Trace nested loops with a table of values
  * T07.G6.06: Trace nested loops that fill a grid pattern
  * T08.G3.01: Use a simple if in a script


- **Short name:** Compare two loop solutions  
- **Description:** Students compare two loop‑based solutions that both solve the same problem but use different numbers of iterations (e.g., repeated subtraction vs direct arithmetic) and reason about which is more efficient for larger inputs.  
- **Challenge format:** Concept, multiple choice/explanation. Present two code snippets; ask which will take more/fewer iterations in given cases and why. Auto‑grading checks selected choices and short structured responses.  
- **CSTA:** MS‑ALG‑AF‑02, MS‑PRO‑PF‑01.

### T07.G7.04 – Loop patterns for counting and accumulation

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G6.06: Trace nested loops that fill a grid pattern
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Recognize loop accumulator patterns  
- **Description:** Students identify and/or construct loops that follow common accumulator patterns (counting, summing, tracking min/max), distinguishing them from unrelated code.  
- **Challenge format:** Mixed concept and coding. Items may ask students to choose which of several loops correctly tracks a maximum value, or to add the missing update step. Auto‑grading checks selected option or presence/placement of the accumulator update.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP.

---

## Grade 8

Grade 8 builds toward high school expectations by using loops in more complex logic and data‑heavy contexts.

### T07.G8.01 – Monte Carlo simulations with loops

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.02: Trace a script with a simple loop
  * T07.G3.03: Build a forever loop for simple animation
  * T07.G7.03: Compare loop algorithms by counting steps
  * T07.G7.04: Loop patterns for counting and accumulation


- **Short name:** Estimate probabilities using loops  
- **Description:** Students design loop‑based simulations that approximate probabilities (e.g., estimate chance of rolling a sum ≥ 9 with two dice) and interpret the results in terms of experimental vs theoretical probability.  
- **Challenge format:** Coding, starter project. Students build a loop that runs many trials, tracks successes, and reports frequencies. Auto‑grading checks loop count, correct condition for success, and the consistency of results across runs (within a range).  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T07.G8.02 – Implement iterative algorithms with loops

_Dependency:_
  * T01.G3.01: Complete a simple script with missing blocks
  * T07.G3.01: Use a counted repeat loop
  * T07.G7.03: Compare loop algorithms by counting steps
  * T07.G7.04: Loop patterns for counting and accumulation
  * T08.G3.01: Use a simple if in a script


- **Short name:** Implement iterative algorithms (e.g., GCD)  
- **Description:** Students implement simple iterative algorithms that rely on loops and repeated updates, such as computing the greatest common divisor by repeated subtraction or checking if a number is prime by trying divisors.  
- **Challenge format:** Coding, algorithmic challenge. Starter project includes input variables and output display blocks; students fill in the loop logic. Auto‑grading runs test cases (pairs of numbers, candidate primes) and compares outputs to reference answers.  
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑02.

### T07.G8.03 – Process structured data with nested loops

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.02: Trace a script with a simple loop
  * T07.G7.03: Compare loop algorithms by counting steps
  * T07.G7.04: Loop patterns for counting and accumulation
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Nested loops over 2D data  
- **Description:** Students use nested loops to process 2D‑structured data (e.g., a list encoding grid values, or two parallel lists) and compute statistics like row/column sums or counts of certain cells.  
- **Challenge format:** Coding, starter project with data representation explained. Students implement nested loops to traverse the structure and compute requested metrics. Auto‑grading checks code structure and final numeric results on multiple test datasets.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP/DI.

### T07.G8.04 – Analyze and justify loop designs

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G7.03: Compare loop algorithms by counting steps
  * T07.G7.04: Loop patterns for counting and accumulation
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Explain loop choices for a task  
- **Description:** Students analyze given loop‑based solutions (e.g., using `repeat until` vs a counted `repeat` with a condition inside) and justify which structure is more appropriate or reliable for a given task. They articulate reasons using input ranges, stopping conditions, and readability.  
- **Challenge format:** Concept, explanation plus selection. Items present two loop implementations for the same scenario; students choose the better one and explain their reasoning using sentence stems or structured responses. Auto‑grading scores the choice and key reasoning phrases.  
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑02.

---

### Notes on Dependencies and Alignment

**Editor Notes:**
- K–2 foundations: Conceptual work on everyday repetition and patterns lives in T01 and T04 and is picture‑based/non‑coding. T07 assumes these foundations.
- G3–5: T07 is a gateway programming topic that follows the progression: fixed-count repeat → trace → build forever → conditional repeat → debug. Each construct is introduced before being combined.
- G6–8: T07 skills assume solid use of basic loops and focus on analyzing, refactoring, and using loops in algorithms and simulations.
- This design aligns with CSTA PRO‑PF expectations while keeping skills small, progressive, and CreatiCode‑implementable.