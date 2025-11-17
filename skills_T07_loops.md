# T07 – Loops & Repetition: K–8 Skill List (Draft v1)

Topic reference: `T07 Loops & Repetition` in `domains_topics_overview.md`  
Domain: Programming (D2) · CSTA focus: PRO‑PF, ALG‑AF (with links to PRO‑TR, DAA‑DF/DP, DAA‑DI)

Each skill below has:

- a stable **ID** (`T07.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Loops are treated as an intuitive idea of “doing something again” and recognizing repeating patterns, not yet as code blocks.

### T07.GK.01 – Spot a repeating pattern (pictures)

- **Short name:** Identify simple repeating patterns (pictures)  
- **Description:** Students recognize visually repeating patterns (e.g., ABAB, AABB) in rows of shapes or sprite poses and distinguish them from non‑patterns or broken sequences. This builds the concept of repetition as “the same thing again and again” in a concrete, age‑appropriate way.  
- **Challenge format:** Concept, multiple choice. Show 3–4 rows of picture tiles; only one is a clean repeating pattern. Students select the repeating row. Variants use sprite poses (walk, walk, jump, walk, walk, jump) to gently bridge toward animation.  
- **CSTA:** EK‑ALG‑AF‑01 (Identify algorithms in daily activities – early pattern awareness).

### T07.GK.02 – Count repeated actions in a story

- **Short name:** Count how many times it repeats  
- **Description:** Students watch or step through a short story animation where a character repeats an action (e.g., jumps, claps) several times. They count and report how many times the action repeats, connecting repetition to counting and iteration.  
- **Challenge format:** Concept, interactive animation. A CreatiCode project plays a short animation with a clearly repeated action; the system then asks “How many times did the cat jump?” and offers picture‑based answer choices (e.g., 2/3/4 icons). Auto‑grading checks the numeric answer.  
- **CSTA:** EK‑ALG‑AF‑01.

### T07.GK.03 – Describe “do it again” in words

- **Short name:** Tell the robot to do it again  
- **Description:** Students use natural language to indicate that an action repeats (e.g., “jump 3 times” instead of listing “jump, jump, jump”), preparing them to later map this idea onto loop blocks.  
- **Challenge format:** Concept, guided input. A picture shows a robot taking the same action several times. Students either choose a sentence (“Jump 3 times” vs “Jump, run, jump”) or drag a “repeat” icon next to a single action picture. Auto‑grading uses the selected sentence/icon.  
- **CSTA:** EK‑ALG‑AF‑01.

---

## Grade 1

Grade 1 focuses on recognizing repetition in code and behavior, still without requiring students to construct loop blocks.

### T07.G1.01 – Find repeated code in a script

- **Short name:** Spot repeated blocks in code  
- **Description:** Students identify sequences of identical or very similar blocks that repeat within a short script (e.g., four `move 10 steps` blocks in a row). This builds awareness of redundant code and prepares the ground for later replacing it with loops.  
- **Challenge format:** Concept, multiple choice or highlighting. A script is shown; students click on or choose which part “does the same thing again and again.” Auto‑grading checks selected block region.  
- **CSTA:** E1‑ALG‑AF‑01, E1‑PRO‑PF‑01.

### T07.G1.02 – Predict how far repetition moves a sprite

- **Short name:** How far does the cat walk?  
- **Description:** Given a script with repeated motion blocks (e.g., five `move 10 steps` in sequence), students predict the total movement or final position qualitatively (e.g., “farther/shorter”) or quantitatively (simple totals) to connect counting with repeated actions.  
- **Challenge format:** Concept, interactive trace. The editor shows a script and a number line or grid; students choose the correct final picture/position or numeric distance. Auto‑grading compares the chosen outcome to the simulated result.  
- **CSTA:** E1‑PRO‑PF‑01.

### T07.G1.03 – Match a repeating picture story to code

- **Short name:** Match repeated actions to code  
- **Description:** Students match a short picture story (e.g., jump, jump, jump) to one of several simple scripts that replicate the same repeated action (e.g., three `jump` blocks). This strengthens mapping between informal descriptions and repeated code.  
- **Challenge format:** Concept, multiple choice. Show a 3‑panel picture story and three tiny scripts; only one script uses the same sequence of actions. Students pick the script.  
- **CSTA:** E1‑ALG‑AF‑01, E1‑PRO‑PF‑01.

### T07.G1.04 – Build a simple repeating script (no loops)

- **Short name:** Repeat an action by copying blocks  
- **Description:** Students build a short script where a sprite repeats a simple action a given number of times (e.g., clap 3 times) by duplicating blocks, but without using loop blocks. This solidifies repetition as repeating code.  
- **Challenge format:** Coding, starter project. Provided: a sprite with one action block (e.g., `say "Hi!" for 1 sec`). Prompt: “Make the sprite say ‘Hi!’ 3 times.” Auto‑grading checks the final script for the correct count and order of repeated blocks.  
- **CSTA:** E1‑PRO‑PF‑01.

---

## Grade 2

Grade 2 is the first year where iteration (loop blocks) is expected in CSTA; students replace repeated code with counted loops.

### T07.G2.01 – Replace repeated moves with a loop

- **Short name:** Use a repeat loop for steps  
- **Description:** Students refactor a script that contains repeated `move 10 steps` blocks into an equivalent script that uses a `repeat` loop, maintaining the same total distance. They must choose a correct repeat count and move block.  
- **Challenge format:** Coding, refactor in CreatiCode. Starter script uses 5–8 repeated movement blocks. Students must modify it to use exactly one `repeat` loop with one movement block inside. Auto‑grading checks for (1) correct presence of a `repeat` loop with the right count, (2) removal of the extra duplicated moves, and (3) correct final position when the green flag is clicked.  
- **CSTA:** E2‑PRO‑PF‑01, E2‑ALG‑AF‑01.

### T07.G2.02 – Loop a simple dance pattern

- **Short name:** Loop a dance move pattern  
- **Description:** Students create a short dance sequence (e.g., step left, step right, spin) and wrap it in a `repeat` block so that the sprite performs the pattern several times when the green flag is clicked.  
- **Challenge format:** Coding, guided construction. Starter project includes a sprite and example blocks for the dance steps. Prompt specifies the pattern and number of repeats (e.g., “Do this pattern 3 times”). Auto‑grading checks that (1) the pattern sequence inside the loop is correct, (2) the repeat count matches the instructions, and (3) no redundant copies exist outside the loop.  
- **CSTA:** E2‑PRO‑PF‑01.

### T07.G2.03 – Loop for a blinking or walking animation

- **Short name:** Use a loop for simple animation  
- **Description:** Students use a `repeat` loop to alternate costumes (or move a sprite back and forth) for a fixed number of times, creating a blinking or walking effect rather than placing many separate `next costume` or move blocks.  
- **Challenge format:** Coding, starter project. A sprite has two costumes and a basic script. Students insert a `repeat` loop around `next costume` and a `wait` block to blink 5 times. Auto‑grading checks (1) loop structure, (2) correct repeat count, and (3) that the sprite alternates costumes the required number of times when run.  
- **CSTA:** E2‑PRO‑PF‑01.

### T07.G2.04 – Predict how many times a loop runs

- **Short name:** Count loop repeats from code  
- **Description:** Students read a simple script with a `repeat` block (e.g., `repeat 4 { move 10 }`) and determine how many times the action inside happens, or what the final distance will be. This develops a mental model of loop count.  
- **Challenge format:** Concept, code‑reading item. CreatiCode shows a short script and ask “How many times does the cat move?” or “How far does the cat move?” with choices. Auto‑grading compares to simulation.  
- **CSTA:** E2‑PRO‑PF‑01.

---

## Grade 3

Grade 3 introduces loops combined with events, conditions, and simple nested structures.

### T07.G3.01 – Use repeat‑until to reach a goal

- **Short name:** Repeat until you reach the flag  
- **Description:** Students use a `repeat until <touching goal>` loop to move a sprite towards a target (e.g., a flag or color stripe), so that the sprite stops exactly when the condition becomes true rather than after a fixed number of steps.  
- **Challenge format:** Coding, starter project. Provided: sprite, goal object, and partial script with a move block. Students wrap the move in a `repeat until` loop with the appropriate condition. Auto‑grading checks (1) correct loop type, (2) appropriate condition, and (3) that the sprite stops on the goal across multiple starting positions.  
- **CSTA:** E3‑PRO‑PF‑01.

### T07.G3.02 – Create a forever game loop for controls

- **Short name:** Forever loop for player controls  
- **Description:** Students implement a `forever` loop that continuously checks keyboard input and moves the sprite accordingly, instead of responding only once. This is often the first exposure to a persistent game loop.  
- **Challenge format:** Coding, starter project. Provided: a sprite and `if key pressed` blocks outside any loop. Students put these inside a `forever` loop triggered by `when green flag clicked`. Auto‑grading runs the project and checks that holding or repeatedly pressing keys moves the sprite smoothly and that no duplicate code exists outside the loop.  
- **CSTA:** E3‑PRO‑PF‑01.

### T07.G3.03 – Nested loops for rows or simple grids

- **Short name:** Use nested loops for patterns  
- **Description:** Students use a loop inside a loop to make patterns such as a row of stamps repeated multiple times (e.g., a 3×4 grid). They learn that nested loops multiply the number of repetitions.  
- **Challenge format:** Coding, starter project with pen or stamping. Prompt: “Make 3 rows of 4 stars each.” Students implement an outer loop for rows and an inner loop for stars in a row, including movement resets. Auto‑grading inspects the code structure (two loops with correct counts) and checks the final stage pattern.  
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑AF‑01.

### T07.G3.04 – Trace a script with nested loops

- **Short name:** Trace nested loops and count actions  
- **Description:** Students read a short script with nested loops and predict how many times an action (like stamping) occurs or how many items appear. This reinforces multiplicative reasoning with loops.  
- **Challenge format:** Concept, code‑reading item. Show nested loops such as `repeat 3 { repeat 2 { stamp } }` and ask “How many stamps will you see?” Auto‑grading compares answer to the product of the loop counts or to simulation.  
- **CSTA:** E3‑ALG‑AF‑01, E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 deepens loop usage with more complex conditions, counters, and refinement of existing loop code.

### T07.G4.01 – Loop with a condition inside

- **Short name:** Loop with checks inside  
- **Description:** Students write a loop where each repeated step also contains a conditional, such as moving and bouncing off edges or adding to a score only when touching a coin.  
- **Challenge format:** Coding, starter project. Example: a ball moves across the screen; students wrap movement in a `repeat` or `forever` loop and add an `if on edge, bounce` or `if touching coin then change score`. Auto‑grading checks that (1) movement loop is present, (2) the condition is inside the loop, and (3) behavior (bouncing or scoring) occurs multiple times as appropriate.  
- **CSTA:** E4‑PRO‑PF‑01.

### T07.G4.02 – Use a loop counter variable

- **Short name:** Use a counter inside a loop  
- **Description:** Students maintain a numeric counter variable that increments on each loop iteration (e.g., to show “Step 1, Step 2, …” or to track how many loops have run), introducing a “for loop” pattern using Scratch‑style blocks.  
- **Challenge format:** Coding, starter project. Students create a variable (e.g., `step`) and initialize it, then inside a `repeat` loop they change `step by 1` and display it (`say step`). Auto‑grading ensures (1) variable initialization, (2) update inside the loop, and (3) correct final value after execution.  
- **CSTA:** E4‑PRO‑PF‑01, E4‑ALG‑AF‑01.

### T07.G4.03 – Convert repeated blocks with conditions into loops

- **Short name:** Refactor repeated code with a loop  
- **Description:** Students are given a longer script with repeated groups of blocks (including conditionals) and asked to rewrite it using a loop to reduce duplication, preserving behavior. This builds code quality and abstraction skills.  
- **Challenge format:** Coding, refactor challenge. Starter script might contain 4 identical “move 10, if touching star change score by 1” sequences. Students rewrite using a `repeat` loop. Auto‑grading checks code structure (loop present, one copy of the body) and behavior equivalence (same final score for a fixed setup).  
- **CSTA:** E4‑PRO‑PF‑01, PRO‑TR.

### T07.G4.04 – Analyze and fix a loop bug

- **Short name:** Find the bug in a loop  
- **Description:** Students examine a script where a loop runs too many or too few times, or the counter/condition is incorrect, and modify it to match the intended behavior. They practice reasoning about loop boundaries and conditions.  
- **Challenge format:** Coding, debugging. A starter project shows expected behavior (e.g., character should jump exactly 3 times), but the given loop makes it jump 4 times or 2 times. Students adjust the loop count or condition. Auto‑grading compares final behavior to a reference solution.  
- **CSTA:** E4‑PRO‑TR‑01 (testing and refining).

---

## Grade 5

Grade 5 uses loops for simulations, data collection, and more complex patterns.

### T07.G5.01 – Simulate repeated experiments with a loop

- **Short name:** Run an experiment many times with a loop  
- **Description:** Students simulate a simple chance experiment (e.g., rolling a die, flipping a coin) repeatedly in code using a loop, and count outcomes to observe frequencies. This connects loops to data and probability.  
- **Challenge format:** Coding, starter project. Provided: a `pick random` block and a `when green flag clicked` script stub. Students add a `repeat` loop (e.g., 20 trials), update counts in variables, and optionally report results. Auto‑grading checks that the loop runs the correct number of iterations and that the count variables update correctly.  
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DP/DI.

### T07.G5.02 – Build a list with a loop

- **Short name:** Fill a list using a loop  
- **Description:** Students write a loop that populates a list with a sequence of values (e.g., the numbers 1 to 10) or with repeated samples from user input or sensors.  
- **Challenge format:** Coding, starter project with an empty list. Students initialize a variable, use a `repeat` or `repeat until` loop, and `add` values to the list each iteration. Auto‑grading checks list content after execution and that there’s no manual duplication.  
- **CSTA:** E5‑PRO‑PF‑01, PRO‑DH, DAA‑DF.

### T07.G5.03 – Use loops to compute aggregates

- **Short name:** Use a loop to total scores  
- **Description:** Students loop over items in a list (or through repeated events) to compute a total or average (e.g., total points from several rounds), using an accumulator variable.  
- **Challenge format:** Coding, starter project with a list of numbers. Students initialize a `total` variable, loop and `change total by item`, then display `total`. Auto‑grading checks the accumulator pattern and final value.  
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DP.

### T07.G5.04 – Nested loops for advanced patterns or tilings

- **Short name:** Nested loops for complex patterns  
- **Description:** Students design or reproduce more complex tilings or repeating art (checkerboards, stripes, simple mosaics) using nested loops and coordinate changes, reinforcing multiplicative reasoning and spatial thinking.  
- **Challenge format:** Coding, creative challenge with auto‑check. The system provides a target pattern; students implement nested loops to approximate it. Auto‑grading uses image similarity and/or code structure checks (two nested loops with appropriate counts).  
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DI.

---

## Grade 6

In middle school, loops become part of analyzing and designing general algorithms; students both trace and construct more abstract loop patterns.

### T07.G6.01 – Trace nested loops with variables

- **Short name:** Trace nested loops and variables  
- **Description:** Students analyze code with nested loops and variable updates (e.g., counters or sums), predicting final variable values and number of iterations.  
- **Challenge format:** Concept, code‑reading item. Show code with two nested loops updating variables; students answer questions like “What is the final value of `sum`?” Auto‑grading uses static analysis or simulation.  
- **CSTA:** MS‑PRO‑PF‑01.

### T07.G6.02 – Refactor repeated code into loops

- **Short name:** Turn repeated code into a loop  
- **Description:** Students are given longer scripts with clearly repeated segments and asked to refactor them into loops—possibly with a loop counter variable—while preserving behavior. This develops generalization and refactoring skills important for competitions.  
- **Challenge format:** Coding, refactor challenge. Projects include repeated movement, drawing, or text output sequences. Auto‑grading compares behavior and checks that repetition is handled by loop blocks rather than by copy‑paste.  
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T07.G6.03 – Loop‑based search in a list

- **Short name:** Search a list using a loop  
- **Description:** Students implement a simple linear search using a loop to find the first item in a list that matches a target (e.g., find the first score above 90), and then respond (e.g., report the position).  
- **Challenge format:** Coding, starter project with a list and a target value. Students write a `repeat until` or `repeat` loop with an index variable or for‑each pattern. Auto‑grading seeds the list with test cases and checks for correct results and use of a loop.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP.

### T07.G6.04 – Avoid and fix infinite loops

- **Short name:** Find and fix infinite loops  
- **Description:** Students identify scripts that never stop because of improper use of `forever` or `repeat until` with a condition that never becomes true. They modify the code to add a stopping condition or break behavior appropriately.  
- **Challenge format:** Coding and concept, debugging. Starter projects include one or two scripts that hang. Students adjust conditions or add a `stop this script` or equivalent structure. Auto‑grading checks that the script terminates or behaves as specified under test inputs.  
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

---

## Grade 7

Grade 7 emphasizes loop patterns that underpin standard algorithms and simulations.

### T07.G7.01 – Use loops to simulate motion over time

- **Short name:** Loop for step‑by‑step simulation  
- **Description:** Students implement a loop that repeatedly updates position (and optionally velocity) to simulate motion, such as an object sliding or falling with a simple rule each step.  
- **Challenge format:** Coding, starter project. Provided variables `x`, `v`, etc.; students create a loop that updates them each tick and animate a sprite accordingly. Auto‑grading checks for correct update pattern and plausible behavior over time.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T07.G7.02 – Nested loops for 2D grids and tile maps

- **Short name:** Nested loops for grid processing  
- **Description:** Students use two loops to process a conceptual 2D grid (e.g., rows and columns of tiles), even if represented as positions or a 1D list plus indices, introducing matrix‑like reasoning.  
- **Challenge format:** Coding, starter project with grid layout. Students implement nested loops to place tiles or check conditions across the grid. Auto‑grading checks the pattern of positions visited and any computed counts.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP.

### T07.G7.03 – Compare loop algorithms by counting steps

- **Short name:** Compare two loop solutions  
- **Description:** Students compare two loop‑based solutions that both solve the same problem but use different numbers of iterations (e.g., repeated subtraction vs direct arithmetic) and reason about which is more efficient for larger inputs.  
- **Challenge format:** Concept, multiple choice/explanation. Present two code snippets; ask which will take more/fewer iterations in given cases and why. Auto‑grading checks selected choices and short structured responses.  
- **CSTA:** MS‑ALG‑AF‑02, MS‑PRO‑PF‑01.

### T07.G7.04 – Loop patterns for counting and accumulation

- **Short name:** Recognize loop accumulator patterns  
- **Description:** Students identify and/or construct loops that follow common accumulator patterns (counting, summing, tracking min/max), distinguishing them from unrelated code.  
- **Challenge format:** Mixed concept and coding. Items may ask students to choose which of several loops correctly tracks a maximum value, or to add the missing update step. Auto‑grading checks selected option or presence/placement of the accumulator update.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP.

---

## Grade 8

Grade 8 builds toward high school expectations by using loops in more complex logic and data‑heavy contexts.

### T07.G8.01 – Monte Carlo simulations with loops

- **Short name:** Estimate probabilities using loops  
- **Description:** Students design loop‑based simulations that approximate probabilities (e.g., estimate chance of rolling a sum ≥ 9 with two dice) and interpret the results in terms of experimental vs theoretical probability.  
- **Challenge format:** Coding, starter project. Students build a loop that runs many trials, tracks successes, and reports frequencies. Auto‑grading checks loop count, correct condition for success, and the consistency of results across runs (within a range).  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T07.G8.02 – Implement iterative algorithms with loops

- **Short name:** Implement iterative algorithms (e.g., GCD)  
- **Description:** Students implement simple iterative algorithms that rely on loops and repeated updates, such as computing the greatest common divisor by repeated subtraction or checking if a number is prime by trying divisors.  
- **Challenge format:** Coding, algorithmic challenge. Starter project includes input variables and output display blocks; students fill in the loop logic. Auto‑grading runs test cases (pairs of numbers, candidate primes) and compares outputs to reference answers.  
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑02.

### T07.G8.03 – Process structured data with nested loops

- **Short name:** Nested loops over 2D data  
- **Description:** Students use nested loops to process 2D‑structured data (e.g., a list encoding grid values, or two parallel lists) and compute statistics like row/column sums or counts of certain cells.  
- **Challenge format:** Coding, starter project with data representation explained. Students implement nested loops to traverse the structure and compute requested metrics. Auto‑grading checks code structure and final numeric results on multiple test datasets.  
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP/DI.

### T07.G8.04 – Analyze and justify loop designs

- **Short name:** Explain loop choices for a task  
- **Description:** Students analyze given loop‑based solutions (e.g., using `repeat until` vs a counted `repeat` with a condition inside) and justify which structure is more appropriate or reliable for a given task. They articulate reasons using input ranges, stopping conditions, and readability.  
- **Challenge format:** Concept, explanation plus selection. Items present two loop implementations for the same scenario; students choose the better one and explain their reasoning using sentence stems or structured responses. Auto‑grading scores the choice and key reasoning phrases.  
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑02.

