# T04 – Patterns & Reusable Solutions: K–8 Skill List (Draft v1)

Topic reference: `T04 Patterns & Reusable Solutions` in `domains_topics_overview.md`
Domain: Algorithms & Design (D1) · CSTA focus: ALG‑AF, ALG‑PS (with links to PRO‑PF, ALG‑HD, ALG‑IM)

Each skill below has:

- a stable **ID** (`T04.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

In Kindergarten, pattern recognition begins with visual observation of repeating sequences in everyday objects and pictures, laying the foundation for understanding repetition and reuse in later coding contexts.

### T04.GK.01 – Spot a repeating pattern (pictures)

- **Short name:** Identify simple repeating patterns (pictures)
- **Description:** Students recognize visually repeating patterns (e.g., ABAB, AABB) in rows of shapes or colored tiles and distinguish them from non‑patterns or broken sequences. This builds the concept of repetition as "the same thing again and again" in a concrete, age‑appropriate way.
- **Challenge format:** Concept, multiple choice. Show 3–4 rows of picture tiles; only one is a clean repeating pattern. Students select the repeating row. Variants use sprite colors or shapes (red, red, blue, red, red, blue) to gently bridge toward coding ideas.
- **CSTA:** EK‑ALG‑AF‑01 (Identify algorithms in daily activities – early pattern awareness).

### T04.GK.02 – Continue a repeating pattern

- **Short name:** Extend the pattern with the next item
- **Description:** Students see a partial repeating pattern (e.g., ABABAB…) and predict or select what comes next, building the mental model of "this repeats the same way" and strengthening sequence reasoning.
- **Challenge format:** Concept, multiple choice or drag‑and‑drop. Show a 5–6 item pattern with the last item missing; students click or drag the correct next tile from options. Auto‑grading checks the selected tile.
- **CSTA:** EK‑ALG‑AF‑01.

### T04.GK.03 – Describe a pattern in simple words

- **Short name:** Tell the pattern rule
- **Description:** Students use natural language (e.g., "red, blue, red, blue" or "happy, sad, happy, sad") to describe what repeats in a given pattern, preparing them to recognize repeating code blocks later.
- **Challenge format:** Concept, guided input or multiple choice. A picture shows a visual pattern. Students either complete a sentence ("The pattern is _____ and _____") or choose the correct description from options. Auto‑grading uses text matching (with fuzzy matching for variation).
- **CSTA:** EK‑ALG‑AF‑01.

---

## Grade 1

Grade 1 extends pattern recognition to include spotting repeated code sequences and understanding how repeated actions can be simplified by identifying the pattern.

### T04.G1.01 – Find repeated blocks in a script

- **Short name:** Spot repeated blocks in code
- **Description:** Students identify sequences of identical or very similar blocks that repeat within a short script (e.g., four `move 10 steps` blocks in a row). This builds awareness of redundant code and prepares the ground for later replacing it with loops or custom blocks.
- **Challenge format:** Concept, multiple choice or highlighting. A script is shown with several repeated blocks; students click on or choose which part "does the same thing again and again." Auto‑grading checks the selected block region or counts matches.
- **CSTA:** E1‑ALG‑AF‑01, E1‑ALG‑PS‑03.

### T04.G1.02 – Match a repeated picture story to code

- **Short name:** Match repeated actions to code
- **Description:** Students match a short picture story showing repeated actions (e.g., jump, jump, jump) to one of several simple scripts that replicate the same repeated action (e.g., three `jump` blocks). This strengthens mapping between informal descriptions and repeated code.
- **Challenge format:** Concept, multiple choice. Show a 3‑panel picture story and three tiny scripts; only one script uses the same sequence of repeated actions. Students pick the script.
- **CSTA:** E1‑ALG‑AF‑01, E1‑ALG‑PS‑03.

### T04.G1.03 – Recognize a template structure in sprite code

- **Short name:** Spot a repeating template in code
- **Description:** Students examine a provided starter script (template) where a single sprite sequence repeats (e.g., "step, pause, step, pause" happening twice), and they describe or identify the core repeated unit, building readiness to use and modify templates.
- **Challenge format:** Concept, short answer or multiple choice. Show a complete short script with an obvious repeated section. Ask "What is the thing that repeats?" or "Which blocks show the pattern?" Auto‑grading checks recognition of the repeating segment.
- **CSTA:** E1‑ALG‑AF‑01.

### T04.G1.04 – Build a simple repeating script (no loops)

- **Short name:** Repeat an action by copying blocks
- **Description:** Students build a short script where a sprite repeats a simple action a given number of times (e.g., clap 3 times) by duplicating blocks, but without using loop blocks. This solidifies repetition as repeating code and the idea of copy‑and‑paste solutions.
- **Challenge format:** Coding, starter project. Provided: a sprite with one action block (e.g., `say "Hi!" for 1 sec`). Prompt: "Make the sprite say 'Hi!' 3 times." Auto‑grading checks the final script for the correct count and order of repeated blocks.
- **CSTA:** E1‑ALG‑PS‑03, E1‑PRO‑PF‑01.

---

## Grade 2

Grade 2 focuses on identifying patterns and repetition in algorithms and replacing redundancy with loops. Students also begin using and modifying template projects to understand code reuse.

### T04.G2.01 – Identify repeating sections in longer scripts

- **Short name:** Find repeated sequences in code
- **Description:** Students examine longer scripts (10‑15 blocks) and identify sections that repeat, even if scattered or with small variations. They learn to spot inefficiency and understand the value of consolidation.
- **Challenge format:** Concept, code‑reading item. Show a longer script; ask students to count how many times a specific sequence (e.g., move, turn) appears, or highlight all instances. Auto‑grading uses code analysis or simulation count.
- **CSTA:** E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

### T04.G2.02 – Replace repeated code with a loop

- **Short name:** Use a repeat loop instead of copy‑paste
- **Description:** Students refactor a script that contains repeated blocks (e.g., five `move 10 steps`) into an equivalent script that uses a `repeat` loop, understanding that loops reduce duplication and make code easier to change.
- **Challenge format:** Coding, refactor in CreatiCode. Starter script uses 5–8 repeated movement blocks. Students must modify it to use exactly one `repeat` loop. Auto‑grading checks for (1) correct loop presence and count, (2) removal of extra duplicates, and (3) equivalent final behavior.
- **CSTA:** E2‑ALG‑PS‑03, E2‑PRO‑PF‑01.

### T04.G2.03 – Use a template project and customize it

- **Short name:** Start from a template and modify it
- **Description:** Students are given a template CreatiCode project (e.g., a simple animation or interactive scene) and make small targeted changes (e.g., change colors, add a sprite, adjust timing). They learn that templates are starting points and can be reused with customization.
- **Challenge format:** Coding, guided modification of a starter project. Provided: a working template project with clear spots to modify (e.g., "Change the background here," "Add a new line of dialogue"). Students make 2–3 specified changes. Auto‑grading checks presence and correctness of changes while verifying the template structure remains intact.
- **CSTA:** E2‑ALG‑PS‑03.

### T04.G2.04 – Predict what a simple repeated pattern produces

- **Short name:** Trace repeated actions and predict the result
- **Description:** Students read or trace a script with repeated blocks (e.g., four `move 10 steps`) and predict the final outcome qualitatively (e.g., "far to the right") or quantitatively (e.g., "40 steps total"), connecting repetition to cumulative effect.
- **Challenge format:** Concept, interactive trace or multiple choice. The editor shows a script with repeated actions and a grid or picture; students choose the correct final position or state. Auto‑grading compares to simulation.
- **CSTA:** E2‑ALG‑AF‑01.

---

## Grade 3

Grade 3 deepens pattern recognition by analyzing nested and conditional patterns, and introducing the idea of custom blocks as reusable code units.

### T04.G3.01 – Decompose a pattern into repeating units

- **Short name:** Break a pattern into smaller pieces
- **Description:** Students analyze a visual or behavioral pattern (e.g., a row of stamps repeated multiple times to form a grid) and identify both the core unit that repeats and how many times it repeats, practicing decomposition.
- **Challenge format:** Concept, multiple choice or labeling. Show a complex pattern (e.g., a 3×4 grid of stars); ask students to identify the core unit and the number of repetitions. Choices might be "1 unit repeated 12 times" vs "3 units repeated 4 times." Auto‑grading checks both the unit identification and the count.
- **CSTA:** E3‑ALG‑PS‑03 (Decompose a problem or task into smaller components).

### T04.G3.02 – Create a nested loop pattern

- **Short name:** Use nested loops for patterns
- **Description:** Students use a loop inside a loop to make patterns such as a row of stamps repeated multiple times (e.g., a 3×4 grid). They learn that nested loops multiply repetitions and allow compact expression of complex patterns.
- **Challenge format:** Coding, starter project with pen or stamping. Prompt: "Make 3 rows of 4 stars each." Students implement an outer loop for rows and an inner loop for stars in a row, including movement resets. Auto‑grading inspects the code structure (two loops with correct counts) and checks the final pattern.
- **CSTA:** E3‑ALG‑PS‑03, E3‑PRO‑PF‑01.

### T04.G3.03 – Recognize a reusable behavior and create a custom block

- **Short name:** Build a custom block for a repeated action
- **Description:** Students identify a repeating behavior in a script (e.g., "turn 90 degrees and move 20 steps" happening multiple times) and create a custom block (procedure) to encapsulate it, learning that custom blocks reduce duplication and improve readability.
- **Challenge format:** Coding, guided construction or refactoring. Starter project has a script with repeated multi‑block sequences. Prompt: "Create a custom block called 'turn_and_move' that combines these three blocks." Students define the block and replace repetitions with calls to it. Auto‑grading checks (1) custom block definition, (2) correct parameters if any, and (3) that the script uses the block instead of duplicating code.
- **CSTA:** E3‑ALG‑PS‑03 (Decompose a problem into smaller components).

### T04.G3.04 – Trace a nested pattern and count outcomes

- **Short name:** Predict outcomes of nested patterns
- **Description:** Students read a script with nested loops (e.g., `repeat 3 { repeat 2 { stamp } }`) and predict how many times an action occurs or how many items appear, reinforcing multiplicative reasoning with patterns.
- **Challenge format:** Concept, code‑reading item. Show nested loops and ask "How many stamps will appear?" or "How many times does the sprite move?" with numeric choices. Auto‑grading compares answer to the product of loop counts or to simulation.
- **CSTA:** E3‑ALG‑AF‑01, E3‑ALG‑PS‑03.

---

## Grade 4

Grade 4 emphasizes pattern analysis in algorithms, generalizing repeated code into reusable procedures, and optimizing code by recognizing and eliminating redundancy.

### T04.G4.01 – Analyze repeated code for abstraction opportunities

- **Short name:** Find code to turn into a procedure
- **Description:** Students examine a longer script with several repeated multi‑block sequences (possibly with small parameter variations, like different move amounts) and identify which parts are reusable, considering how to parameterize them if needed.
- **Challenge format:** Concept, code analysis. Show a script with repeated patterns (e.g., "move X, turn 90" where X varies). Ask students to identify opportunities to create a custom block with a parameter, or multiple choice: which section is most reusable? Auto‑grading checks understanding of parameterization and reusability.
- **CSTA:** E4‑ALG‑PS‑03.

### T04.G4.02 – Convert repeated blocks into a parameterized custom block

- **Short name:** Create a custom block with parameters
- **Description:** Students refactor repeated code into a single custom block with parameters (e.g., `draw_polygon(sides, size)`). They learn that parameters allow one block to handle multiple similar tasks, achieving even greater code reuse than loops alone.
- **Challenge format:** Coding, refactor challenge. Starter script contains code like "move 10, turn 36" repeated 10 times, then "move 20, turn 45" repeated 8 times. Students create a custom block `move_and_turn(amount, angle)` and replace both sequences with calls to it. Auto‑grading checks parameter definitions, block calls with correct arguments, and equivalent behavior.
- **CSTA:** E4‑ALG‑PS‑03, E4‑PRO‑PF‑01.

### T04.G4.03 – Refactor repeated code to use loops and custom blocks

- **Short name:** Clean up code by combining loops and custom blocks
- **Description:** Students are given a script with both redundant copy‑paste code and opportunities to nest or parameterize. They refactor to use both loops (for iteration within a pattern) and custom blocks (for abstraction), learning when to apply each technique.
- **Challenge format:** Coding, advanced refactor. Starter script might repeatedly call a "draw star" sequence, each with different rotation or color. Students create a custom block `draw_star(color)`, then use a loop to call it multiple times with different colors. Auto‑grading checks code structure (custom block + loop), parameter passing, and behavior equivalence on test runs.
- **CSTA:** E4‑ALG‑PS‑03, E4‑PRO‑PF‑01.

### T04.G4.04 – Assess effectiveness of a pattern recognition strategy

- **Short name:** Evaluate how well a pattern is abstracted
- **Description:** Students compare two solutions to the same problem: one using repeated code and one using loops/custom blocks. They discuss or analyze which is more maintainable, clearer, and easier to modify, developing critical thinking about code quality.
- **Challenge format:** Concept, explanation or multiple choice. Present two scripts side‑by‑side (one with copy‑paste, one with loops/blocks). Ask which is easier to modify if you need to change a value, or which is shorter. Students select and explain, or score multiple choice. Auto‑grading checks selection and key reasoning phrases (e.g., "fewer blocks," "easier to change").
- **CSTA:** E4‑ALG‑PS‑03, E4‑ALG‑AF‑01.

---

## Grade 5

Grade 5 applies pattern recognition and code reuse to simulations, data structures, and algorithms, learning that many computational solutions rely on recognizing and exploiting patterns.

### T04.G5.01 – Identify patterns in data and represent them with variables

- **Short name:** Spot patterns in data with variables
- **Description:** Students examine a sequence of data values (e.g., scores increasing by 5 each round, or alternating values) and recognize the underlying pattern, then use variables and loops to generate or process similar data efficiently.
- **Challenge format:** Coding, starter project with data. Provided: a loop and a pattern description (e.g., "Each round, score increases by 5. Start at 10."). Students initialize a variable and update it in the loop to match the pattern. Auto‑grading checks loop structure and final values.
- **CSTA:** E5‑ALG‑AF‑01, E5‑ALG‑PS‑03.

### T04.G5.02 – Create a reusable library of custom blocks

- **Short name:** Build and use a custom block library
- **Description:** Students create several related custom blocks (e.g., `draw_polygon(sides, size)`, `draw_triangle`, `draw_square`) and recognize that this library of blocks encodes common patterns and can be applied in multiple projects, introducing the idea of code libraries and modularity.
- **Challenge format:** Coding, mini‑project. Prompt: "Create three custom blocks for drawing shapes: triangle, square, pentagon. Then use them to draw a scene." Students build the blocks with appropriate logic and call them in a main script. Auto‑grading checks (1) all three blocks are defined correctly, (2) all are called at least once, and (3) the scene is drawn correctly.
- **CSTA:** E5‑ALG‑PS‑03, E5‑PRO‑PF‑01.

### T04.G5.03 – Generalize a pattern into an algorithm

- **Short name:** Turn a pattern into a reusable algorithm
- **Description:** Students take a specific repeating pattern (e.g., "draw a checkerboard") and generalize it into a parameterized algorithm (nested loops with dynamic sizing), so that changing one parameter produces the entire family of similar patterns.
- **Challenge format:** Coding, algorithmic design. Prompt: "Create a custom block `checkerboard(size)` that draws a checkerboard of any size." Students implement nested loops with parameters. Auto‑grading tests the block with multiple size inputs and checks that output scales correctly.
- **CSTA:** E5‑ALG‑PS‑03, E5‑ALG‑AF‑01.

### T04.G5.04 – Refactor a complex pattern into smaller, composable blocks

- **Short name:** Decompose a big pattern into smaller reusable parts
- **Description:** Students take a complex visual pattern or animation (e.g., a fancy border made of repeated sections) and break it into smaller custom blocks that can be reused independently, understanding that patterns themselves can be built from simpler patterns.
- **Challenge format:** Coding, creative refactoring challenge. Provided: a script that draws a complex decorative pattern using many repeated blocks. Prompt: "Break this into smaller custom blocks so that each block is short and reusable." Students create 2–3 intermediate blocks and recompose the original pattern from them. Auto‑grading checks that (1) intermediate blocks are defined, (2) the main script calls them correctly, and (3) the output is visually equivalent to the original.
- **CSTA:** E5‑ALG‑PS‑03.

---

## Grade 6

In middle school, pattern recognition becomes more abstract and is applied to algorithm design, data processing, and optimization. Students analyze patterns in code structure and behavior.

### T04.G6.01 – Recognize structural patterns in algorithms

- **Short name:** Spot common algorithm patterns
- **Description:** Students analyze code and identify common structural patterns (e.g., counter increments, accumulator updates, conditional nesting) that appear across different programs, learning that algorithms often follow recognizable templates.
- **Challenge format:** Concept, code‑reading or matching. Show several short code snippets; ask students to group them by pattern (e.g., all the "counter" patterns together) or identify which pattern a given snippet follows. Auto‑grading checks correct grouping or selection.
- **CSTA:** MS‑ALG‑AF‑02, MS‑ALG‑PS‑05.

### T04.G6.02 – Refactor repeated code into modular custom blocks

- **Short name:** Turn repeated code into reusable procedures
- **Description:** Students are given longer projects with clearly repeated segments and asked to refactor them into well‑named custom blocks with appropriate parameters, improving code clarity and maintainability.
- **Challenge format:** Coding, refactor challenge. Project includes repeated movement, drawing, or text output sequences. Students create custom blocks and replace repetitions. Auto‑grading compares behavior and checks that repetition is handled by block calls rather than copy‑paste, while verifying parameter count and types.
- **CSTA:** MS‑ALG‑PS‑05, MS‑PRO‑PF‑01.

### T04.G6.03 – Analyze template projects and customize them systematically

- **Short name:** Modify template projects for custom needs
- **Description:** Students examine a template project, understand its structure and key decision points, then make systematic modifications to adapt it for a different purpose (e.g., change a quiz template to use different questions, or adapt a game template with new rules), learning strategic reuse.
- **Challenge format:** Coding, guided modification or mini‑project. Provided: a template (e.g., a simple quiz or game). Prompt: "Adapt this for [new context]" (e.g., "a math quiz" or "a space shooter"). Students identify key customization points and make changes. Auto‑grading checks that template structure remains, custom elements are correct, and the project runs without errors.
- **CSTA:** MS‑ALG‑PS‑05.

### T04.G6.04 – Compare efficiency of different pattern solutions

- **Short name:** Evaluate which pattern approach is best
- **Description:** Students compare two solutions using different pattern techniques (e.g., nested loops vs list iteration, or custom blocks vs inline code) and reason about which is more efficient, readable, or maintainable for a given context.
- **Challenge format:** Concept, explanation plus selection. Present two code snippets solving the same problem differently; ask which is easier to understand, which is shorter, which would be easier to modify. Students choose and explain. Auto‑grading scores selection and reasoning quality.
- **CSTA:** MS‑ALG‑AF‑02, MS‑ALG‑PS‑05.

---

## Grade 7

Grade 7 uses pattern recognition as a foundation for designing algorithms and understanding data structures. Students recognize that many algorithms are built by combining patterns.

### T04.G7.01 – Recognize iteration patterns in different contexts

- **Short name:** Spot loop patterns in simulations and games
- **Description:** Students identify the iteration patterns underlying common game and simulation behaviors (e.g., "update physics every frame," "process each sprite," "check all collisions"), understanding that iteration is a fundamental building block.
- **Challenge format:** Concept, code analysis or explanation. Show snippets from a game or simulation; ask students to identify the loop structure and what it does on each iteration. Or: present a game loop description and ask which snippets belong inside the loop. Auto‑grading checks correct identification of loop scope and purpose.
- **CSTA:** MS‑ALG‑AF‑02, MS‑ALG‑PS‑06.

### T04.G7.02 – Design composite algorithms using smaller algorithmic patterns

- **Short name:** Build algorithms from smaller patterns
- **Description:** Students design a solution to a complex problem by recognizing that it can be decomposed into smaller, standard algorithmic patterns (e.g., a search pattern + an accumulator pattern) and combining them.
- **Challenge format:** Coding or concept, mixed. Prompt: "Design an algorithm that finds all even numbers in a list and sums them." Students outline or code a solution, explicitly using both a filtering pattern and an accumulation pattern. Auto‑grading checks that both patterns are present and correctly applied.
- **CSTA:** MS‑ALG‑PS‑05, MS‑ALG‑PS‑06.

### T04.G7.03 – Optimize code by eliminating redundant patterns

- **Short name:** Simplify code by removing repeated patterns
- **Description:** Students examine an existing project with redundant patterns and systematically refactor it, combining loops, nesting, and custom blocks to minimize duplication and improve clarity.
- **Challenge format:** Coding, optimization challenge. Provided: a working project with obvious redundancy (e.g., three nearly identical sprites, each with similar code). Prompt: "Refactor this to use custom blocks and loops instead of repetition." Auto‑grading checks that redundancy is reduced while behavior is preserved.
- **CSTA:** MS‑ALG‑PS‑05, MS‑PRO‑PF‑01.

### T04.G7.04 – Explain how pattern recognition leads to better algorithm design

- **Short name:** Justify pattern‑based design choices
- **Description:** Students articulate how recognizing patterns in a problem (or in existing solutions) leads to better algorithm design, including improved efficiency, readability, and generalizability.
- **Challenge format:** Concept, explanation with selection. Present a problem and two design approaches; ask students to explain why the pattern‑based approach is better, using sentences stems like "By recognizing the ___ pattern, we can avoid repeating ___." Auto‑grading checks for key concepts (efficiency, clarity, reusability).
- **CSTA:** MS‑ALG‑PS‑05, MS‑ALG‑PS‑06.

---

## Grade 8

Grade 8 builds toward high school by treating pattern recognition and code reuse as essential skills for solving complex, data‑heavy problems and designing robust, maintainable systems.

### T04.G8.01 – Recognize and leverage common algorithmic patterns

- **Short name:** Use standard algorithm patterns in solutions
- **Description:** Students identify standard algorithmic patterns (e.g., linear search, accumulation, two‑pointer, divide‑and‑conquer) in problem descriptions and apply them effectively to solve problems, understanding that many problems can be solved by pattern matching to known solutions.
- **Challenge format:** Coding, algorithmic challenge. Prompt: "Find the two numbers in a list that add up to a target sum." Students recognize this as a pattern match problem (or two‑pointer / hash pattern) and implement a solution. Auto‑grading runs test cases and compares outputs to reference answers.
- **CSTA:** MS‑ALG‑AF‑02, MS‑ALG‑PS‑05.

### T04.G8.02 – Design modular, reusable custom blocks for a project

- **Short name:** Build a library of procedures for a project
- **Description:** Students design and build a suite of well‑named, well‑documented custom blocks (procedures) for a project, recognizing that good abstractions make code easier to reason about, test, and reuse across multiple scenes or game states.
- **Challenge format:** Coding, project design. Prompt: "Build a game or interactive app with at least 5 custom blocks, each handling a distinct behavior (e.g., update_player, check_collision, draw_ui)." Students design the blocks with appropriate parameters and use them throughout the project. Auto‑grading checks that (1) each block is defined, (2) blocks are called appropriately, (3) each has a clear, single responsibility, and (4) the overall project works correctly.
- **CSTA:** MS‑ALG‑PS‑05, MS‑PRO‑PF‑01.

### T04.G8.03 – Generalize a specific solution into a parameterized template

- **Short name:** Turn a solution into a template others can reuse
- **Description:** Students take a working solution to a specific problem (e.g., a quiz with five questions) and generalize it into a reusable template with parameters (e.g., `make_quiz(num_questions, question_list)`) that others can adapt for different inputs, learning that good design anticipates reuse.
- **Challenge format:** Coding, design challenge. Provided: a working, specific solution. Prompt: "Refactor this into a reusable template that others could customize." Students parameterize key customization points (e.g., questions, colors, difficulty). Auto‑grading checks that the template can be used with different inputs and produces correct results.
- **CSTA:** MS‑ALG‑PS‑05, MS‑ALG‑PS‑07.

### T04.G8.04 – Analyze and justify choices in pattern‑based design

- **Short name:** Explain trade‑offs in abstraction and reuse
- **Description:** Students examine a project and argue about design choices (e.g., "Should this be a custom block or inline code?" "Is this parameter necessary?"). They weigh factors like code length, clarity, flexibility, and performance in the context of the problem.
- **Challenge format:** Concept, explanation plus selection. Provide a code snippet with a custom block that could alternatively be inline, or a parameterized block that might not need all its parameters in this context. Ask students to decide: keep it abstracted or simplify? Justify with reasoning about readability, reusability, and clarity. Auto‑grading scores the choice and quality of reasoning.
- **CSTA:** MS‑ALG‑AF‑02, MS‑ALG‑PS‑05.

---

## Implementation Notes

**Overlap with T07 (Loops & Repetition):**
T04 and T07 are closely related. T07 focuses on loops as a control structure for iteration; T04 focuses on *recognizing* when repetition is needed (pattern identification) and *abstracting* it into reusable components (custom blocks, templates). Teachers may introduce T07 and T04 concurrently or in tandem, with T04 perhaps starting one step earlier (pattern spotting in Grade K–1 before loop block syntax in Grade 2).

**CreatiCode‑Specific Affordances:**
- **Templates:** CreatiCode's template projects allow students to experience code reuse without building from scratch.
- **Custom blocks (procedures):** CreatiCode's custom block interface naturally supports the progression from spotting repetition to building and using reusable procedures.
- **Pen/stamping:** Drawing and stamping tools support visual pattern creation and nested loop demonstration.
- **Project sharing:** The platform's ability to share projects makes the template and reuse mindset practical.

**Assessment Considerations:**
- Early grades (K–2): Assess through visual pattern recognition and identification of repeated code blocks.
- Middle grades (3–5): Assess through refactoring challenges where students replace repetition with loops and custom blocks.
- Upper grades (6–8): Assess through design decisions, code optimization, and meta‑analysis of pattern‑based approaches.

**Connection to Other Topics:**
- **T01 (Everyday Algorithms):** Understanding steps and sequences prepares for recognizing repeating patterns.
- **T02 (Representing & Tracing):** Flowcharts and tracing help visualize how patterns unfold.
- **T03 (Problem Decomposition):** Breaking problems into parts goes hand in hand with identifying reusable components.
- **T07 (Loops & Repetition):** Loops are the primary coding tool for implementing pattern-based solutions.
- **T11 (Functions & Modularization):** Custom blocks are the key abstraction mechanism for reuse.
- **T12 (Program Organization):** Good naming and structure support pattern recognition and code clarity.
