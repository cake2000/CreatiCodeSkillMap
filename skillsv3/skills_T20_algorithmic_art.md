# T20 – Creative Coding: K–8 Skill List (Draft v1)

Topic reference: `T20 Creative Coding` in `domains_topics_overview.md`
Domain: Programming (D2) & Data/Analysis (D3) · CSTA focus: PRO‑PF, DAA‑DI, CAS‑ET

Each skill below has:

- a stable **ID** (`T20.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

In kindergarten, algorithmic art focuses on recognizing and creating simple visual patterns using familiar tools (pen, stamps, drawing). Students do not yet program; they manipulate physical or digital pens to draw shapes and see repetition in visual form.

### T20.GK.01 – Recognize patterns in artwork

- **Short name:** Spot patterns in pictures and drawings
- **Description:** Students look at simple artwork (rows of shapes, repeated colors, alternating designs) and identify which rows follow a repeating pattern and which do not. This builds pattern awareness that is foundational for later algorithmic thinking.
- **Challenge format:** Concept, multiple choice. Show 3–4 rows of geometric shapes or colored objects; only one (or more) is a clean repeating pattern (e.g., red-blue-red-blue or square-circle-square-circle). Students select all rows that repeat. Auto‑grading checks selected rows against a key.
- **CSTA:** EK‑ALG‑AF‑01 (Identify algorithms in daily activities).

### T20.GK.02 – Draw with a digital pen tool

- **Short name:** Use a pen to draw on screen
- **Description:** Students learn to control a digital pen tool (or turtle/sprite pen) to draw lines, create simple shapes, and make marks in different colors. This is the foundation for later algorithmic drawing.
- **Challenge format:** Coding, guided drawing. CreatiCode project with a pen tool; prompt: "Draw a red line, then a blue line." Students drag pen blocks to create the drawing. Auto‑grading checks that the drawing matches expected line colors and approximate positions.
- **CSTA:** EK‑PRO‑PF‑01 (Create programs that include sequence to complete a task).

### T20.GK.03 – Create a simple repeating row of shapes

- **Short name:** Stamp shapes in a row
- **Description:** Students use a stamp or pen to place identical shapes (circles, squares, stars) in a row across the screen, with roughly equal spacing. This is early concrete experience with repetition without formal loops.
- **Challenge format:** Coding, starter project. A sprite with a stamp block; prompt: "Stamp 5 stars across the screen." Students place blocks to move and stamp; no loop blocks required, but multiple stamp blocks are placed in sequence. Auto‑grading checks the count and approximate positions of stamps.
- **CSTA:** EK‑PRO‑PF‑01.

---

## Grade 1

Grade 1 continues hands‑on drawing and pattern-making. Students recognize and describe repeating visual patterns in their own and others' artwork, and they begin connecting simple code sequences to visual outcomes.

### T20.G1.01 – Describe repeating patterns in words

- **Short name:** Tell the pattern rule
- **Description:** Students look at a row of shapes or artwork and describe the pattern in simple language (e.g., "big, small, big, small" or "red, blue, red, blue"). This builds vocabulary for describing algorithmic structure.
- **Challenge format:** Concept, written/short-answer or multiple choice. Show a repeating pattern; ask "What is the rule?" with answer choices like "square, circle, square, circle" or "2 big, 2 small, 2 big, 2 small." Auto‑grading matches student answers to correct pattern descriptions.
- **CSTA:** E1‑ALG‑AF‑01 (Create algorithms that include step‑by‑step instructions).

### T20.G1.02 – Match drawings to pen code

- **Short name:** Match code to a drawing
- **Description:** Given a simple drawing (e.g., a red square, a blue circle, a green line), students match it to one of several short pen scripts that would produce the same drawing. This bridges visual output to code logic.
- **Challenge format:** Concept, multiple choice. Show a target drawing and three short code snippets (e.g., using pen color, pen down/up, move, and stamp blocks). Students select the code that matches the drawing. Auto‑grading compares selected code to the visual output.
- **CSTA:** E1‑PRO‑PF‑01.

### T20.G1.03 – Draw a pattern by copying pen commands

- **Short name:** Copy pen moves to make a pattern
- **Description:** Students create a simple repeating pattern (e.g., two rows of alternating colors or shapes) by copy‑pasting or duplicating pen blocks, without loops. The focus is on recognizing that repeating the same command block produces repeating visual output.
- **Challenge format:** Coding, guided construction. A sprite with one set of pen blocks (move, change pen color, stamp); prompt: "Make 2 rows of this pattern." Students copy the blocks. Auto‑grading checks for duplication and correct visual output (2 rows visible).
- **CSTA:** E1‑PRO‑PF‑01.

### T20.G1.04 – Predict the result of pen code

- **Short name:** Predict what code will draw
- **Description:** Students read a short sequence of pen blocks and predict what image or pattern will appear (e.g., "move right, stamp circle, move right, stamp circle—will I see circles in a line?"). This develops code tracing and visualization skills.
- **Challenge format:** Concept, multiple choice with pictures. Show a short script (e.g., 4 blocks: move, stamp, move, stamp); ask "What will you see?" with picture choices. Auto‑grading compares answer to simulation.
- **CSTA:** E1‑PRO‑PF‑01.

---

## Grade 2

Grade 2 introduces repeat loops for drawing and pattern-making. Students replace repeated pen commands with `repeat` loops and explore how parametric changes (pen color, size) affect visual designs.

### T20.G2.01 – Use a repeat loop to draw a row

- **Short name:** Loop to draw a repeating row
- **Description:** Students replace several duplicate pen+move blocks with a single `repeat` loop, producing a row of stamped shapes or a series of lines. This is the first algorithmic art skill using loops.
- **Challenge format:** Coding, refactor in CreatiCode. Starter script has 5 duplicate stamp+move blocks. Students modify it to use one `repeat 5` loop containing stamp and move. Auto‑grading checks (1) loop structure, (2) correct count, (3) final visual output (5 shapes in a row).
- **CSTA:** E2‑PRO‑PF‑01, E2‑ALG‑AF‑01 (Model daily processes using iteration).

### T20.G2.02 – Create a geometric pattern with a loop

- **Short name:** Draw a pattern with repeated moves
- **Description:** Students use a `repeat` loop to draw a simple geometric pattern, such as a square outline (move-right, rotate-90, repeat 4 times) or a star outline (move-forward, rotate-144, repeat 5 times).
- **Challenge format:** Coding, guided construction. Starter project includes a sprite, pen, and a loop block template. Prompt: "Draw a square using a repeat loop." Students fill in the move distance, rotation angle, and repeat count. Auto‑grading checks that a closed square shape is drawn (or verified via simulation).
- **CSTA:** E2‑PRO‑PF‑01.

### T20.G2.03 – Parametrize pen properties (color, size)

- **Short name:** Change pen color or size in a drawing
- **Description:** Students modify a pen script to change color or pen size, observing how visual output changes. This introduces the concept of parametrization: the same algorithm with different parameter values produces different-looking art.
- **Challenge format:** Coding, starter project. A script draws a row of circles using a loop. Students change the pen color block or insert a pen size change. Auto‑grading checks that the color or size is different from the original and that the pattern structure remains correct.
- **CSTA:** E2‑PRO‑PF‑01, DAA‑DI.

### T20.G2.04 – Combine loops and color changes for a striped pattern

- **Short name:** Create stripes using loops
- **Description:** Students build a script that uses a loop and pen color changes to create a striped or multi-color pattern, such as alternating color rows.
- **Challenge format:** Coding, creative challenge. Prompt: "Use a repeat loop to draw horizontal stripes of different colors." Students implement an outer loop for rows and a color change inside or between rows. Auto‑grading checks the loop structure and that at least 2 colors appear in the final output.
- **CSTA:** E2‑PRO‑PF‑01, DAA‑DI.

---

## Grade 3

Grade 3 deepens loop use in art and introduces nested loops for creating grid-based patterns. Students also begin using conditionals and simple randomness to vary designs.

### T20.G3.01 – Use nested loops to draw a grid pattern

- **Short name:** Nested loops for grids
- **Description:** Students use an outer loop (rows) and an inner loop (columns) to create a grid of stamps or shapes. This is a key skill for algorithmic art, introducing two-dimensional design thinking.
- **Challenge format:** Coding, starter project with a checkerboard goal. Prompt: "Draw a 3×4 grid of shapes using nested loops." Students implement an outer `repeat 3` for rows and an inner `repeat 4` for columns, with position resets. Auto‑grading checks code structure (two loops) and the final grid pattern.
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑AF‑01 (Use nested loops for patterns).

### T20.G3.02 – Create a checkerboard with conditional stamp placement

- **Short name:** Checkerboard pattern with conditionals
- **Description:** Students use nested loops with an if statement to stamp only certain squares (e.g., only when row+column is even), creating a checkerboard effect.
- **Challenge format:** Coding, challenge project. Prompt: "Draw a checkerboard where alternating squares are filled." Students use nested loops, a counter variable, and a condition to decide when to stamp. Auto‑grading checks the code for loops and conditionals, and verifies the checkerboard pattern visually.
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑AF‑01.

### T20.G3.03 – Use randomness to create generative patterns

- **Short name:** Random colors or positions in art
- **Description:** Students add `pick random` to a loop-based drawing script to vary colors, positions, or stamp sizes. This introduces generative art: each run produces a slightly different design.
- **Challenge format:** Coding, starter project with a loop drawing shapes. Students insert a `pick random` block to vary pen color or x/y position slightly. Auto‑grading runs the project multiple times and checks that outputs differ while maintaining the overall loop structure.
- **CSTA:** E3‑PRO‑PF‑01, DAA‑DI.

### T20.G3.04 – Trace nested loops and predict output

- **Short name:** Trace nested loops in art code
- **Description:** Students read code with nested loops and predict or count how many stamps will appear or describe the final pattern structure.
- **Challenge format:** Concept, code-reading item. Show nested loops such as `repeat 2 { repeat 3 { stamp } move }` and ask "How many stamps?" or "What shape will you see?" Auto‑grading compares answer to simulation.
- **CSTA:** E3‑ALG‑AF‑01, E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 applies art skills to more complex designs: tessellations, spirals, fractals-like patterns, and art that responds to user input or variables.

### T20.G4.01 – Draw a spiral using a loop with changing distance

- **Short name:** Spiral pattern with loops
- **Description:** Students write a loop where the move distance or angle increases on each iteration, creating a spiral or expanding geometric pattern. This combines loops with variables.
- **Challenge format:** Coding, guided construction. Starter project includes a `repeat` loop and a variable for move distance. Prompt: "Change the distance a little each time to make a spiral." Students increment the distance variable inside the loop. Auto‑grading verifies the loop structure and checks that the spiral expands (distances increase).
- **CSTA:** E4‑PRO‑PF‑01, E4‑ALG‑AF‑01 (Create algorithms with variables).

### T20.G4.02 – Create a tessellation or tiling pattern

- **Short name:** Tessellation design
- **Description:** Students design a repeating tile (e.g., a hexagon or square with internal pattern) and then use nested loops to tile it across the screen, creating a seamless tessellation.
- **Challenge format:** Coding, creative challenge. Prompt: "Design a tile shape and then repeat it to cover the screen." Students create a custom block (or inline procedure) for the tile and call it in nested loops. Auto‑grading checks code modularity and verifies that the tiles repeat without gaps or severe overlaps.
- **CSTA:** E4‑PRO‑PF‑01.

### T20.G4.03 – Use variables to parametrize art (size, color, rotation)

- **Short name:** Parametrized algorithmic art
- **Description:** Students create a script where variables control the visual design (e.g., a variable for number of sides, pen size, or rotation angle). Changing the variable changes the whole design.
- **Challenge format:** Coding, starter project. A script draws a polygon using a loop; variables control sides, size, and color. Prompt: "Create a script where changing one variable creates different art." Students set initial values and ensure the code uses them. Auto‑grading checks that variables are declared and used, and that changing them changes the output.
- **CSTA:** E4‑PRO‑PF‑01, DAA‑DI.

### T20.G4.04 – Analyze and modify a complex art script

- **Short name:** Debug or improve art code
- **Description:** Students are given a script that draws a pattern but has an issue (e.g., too many loops causing clutter, wrong colors, or incorrect spacing). They modify it to fix or improve the design.
- **Challenge format:** Coding, debugging/improvement challenge. A starter script draws a pattern with a flaw (overlapping shapes, wrong color, poor spacing). Students modify loop counts, variables, or conditions to improve it. Auto‑grading checks that the code is improved and runs without errors.
- **CSTA:** E4‑PRO‑TR‑01 (Testing and refining code).

---

## Grade 5

Grade 5 emphasizes data-driven art: visualizations of simple datasets, art that reacts to sensor input or user actions, and fractal-like recursive patterns.

### T20.G5.01 – Create a bar chart or simple data visualization

- **Short name:** Draw a bar chart with loops
- **Description:** Students use loops to draw rectangles or lines of varying heights based on a list of numeric values, creating a visual representation of data. This bridges algorithmic art with data visualization.
- **Challenge format:** Coding, starter project. Provided: a list of numbers (e.g., [3, 5, 2, 4]). Prompt: "Draw bars where the height matches each number." Students use a loop that reads from the list and draws a rectangle of proportional height. Auto‑grading checks the loop structure and compares bar heights to the data values.
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DP/DI (Data investigation).

### T20.G5.02 – Animate a pattern based on a variable

- **Short name:** Animate algorithmic art
- **Description:** Students create a script that draws or modifies a pattern in response to a counter variable that changes over time (e.g., a spiral that grows with each frame, or a pattern that rotates).
- **Challenge format:** Coding, starter project with a timer or frame count. Prompt: "Make an animated pattern that changes each frame." Students use a variable to control pen angle, position, or size inside a forever loop. Auto‑grading runs the project and checks that the visual output changes smoothly over time.
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DI.

### T20.G5.03 – Create interactive art that responds to mouse or keyboard

- **Short name:** Interactive algorithmic art
- **Description:** Students build a script where user input (mouse position, key press) drives the algorithmic drawing. For example, the art style or pattern changes based on where the user clicks.
- **Challenge format:** Coding, creative challenge. Prompt: "Make art that changes when you click or press a key." Students implement event handlers (on click, on key press) that modify variables controlling the art. Auto‑grading checks for event handlers and that the visual output responds to input.
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DI.

### T20.G5.04 – Design a recursive-like pattern (fractal preview)

- **Short name:** Fractal-like patterns
- **Description:** Students create patterns where a shape is drawn, and then smaller copies of the same shape are drawn inside or around it, mimicking fractal-like structure (without full recursion, using nested loops instead).
- **Challenge format:** Coding, challenge project. Prompt: "Draw a pattern where smaller shapes repeat the same pattern inside." Students use multiple nested loops of decreasing sizes. Auto‑grading verifies the code structure and checks that the visual output shows repeated, nested patterns.
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DI.

---

## Grade 6

In middle school, students analyze and design more sophisticated algorithmic art, often connecting it to mathematics or data insights. They understand how parameters and algorithms create variety and meaning.

### T20.G6.01 – Analyze and describe an algorithmic art script

- **Short name:** Trace and explain art code
- **Description:** Students examine a script that produces an interesting pattern and explain what the loops, variables, and conditionals do and how they combine to create the visual effect.
- **Challenge format:** Concept, code analysis. Show a moderately complex art script (with nested loops, variable updates, and color changes). Ask: "Describe what each section of this code does" or "What happens if you change this variable?" Auto‑grading uses structured responses or multiple choice to check understanding.
- **CSTA:** MS‑PRO‑PF‑01 (Analyze how code segments work).

### T20.G6.02 – Refactor repetitive art code into loops and functions

- **Short name:** Organize art code with loops and custom blocks
- **Description:** Students take a lengthy, repetitive art script and refactor it to use loops and/or custom blocks, reducing duplication while maintaining the visual output.
- **Challenge format:** Coding, refactor challenge. A starter script draws multiple similar patterns with copy‑pasted code. Students replace duplication with loops or create a custom block. Auto‑grading checks code structure (presence of loops or functions) and that the output remains visually equivalent.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T20.G6.03 – Use variables and conditional logic in art

- **Short name:** Conditional design based on variables
- **Description:** Students write an algorithm where the visual design branches based on variable values or conditions (e.g., draw a different tile pattern depending on a value, or alternate colors based on a counter).
- **Challenge format:** Coding, starter project. Prompt: "Create art where the design changes based on a variable or condition." Students implement conditionals inside loops that control which shapes are drawn, what colors are used, or how angles are set. Auto‑grading checks for correct conditional structure and visual variety based on the variable.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T20.G6.04 – Create data-driven visualizations

- **Short name:** Visualize data with algorithmic art
- **Description:** Students design a script that reads data from a list or table and creates a visualization (bar chart, scatter plot, or abstract artistic representation). This connects data analysis with creative expression.
- **Challenge format:** Coding, starter project with a provided dataset. Prompt: "Create a visual representation of this data." Students implement a loop that processes each data point and draws corresponding visual elements. Auto‑grading checks the loop structure and verifies that the visualization accurately reflects the data.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP/DI.

---

## Grade 7

Grade 7 emphasizes algorithmic thinking in art: efficiency, optimization, and understanding how small changes in an algorithm cascade into large visual differences. Students also explore algorithms used in real generative art.

### T20.G7.01 – Optimize an art algorithm for efficiency

- **Short name:** Efficient art algorithms
- **Description:** Students compare two algorithms that produce similar art but differ in efficiency (e.g., one uses nested loops, another uses conditionals and single loop). They analyze which is faster and explain why.
- **Challenge format:** Concept, code comparison. Show two implementations of a pattern (e.g., one with nested loops, one with a single loop and math); ask which is more efficient or will run faster. Students explain their reasoning. Auto‑grading checks the answer and evaluates reasoning phrases.
- **CSTA:** MS‑ALG‑AF‑02, MS‑PRO‑PF‑01.

### T20.G7.02 – Use advanced control flow in art (while, repeat-until)

- **Short name:** Advanced loops in art
- **Description:** Students use a `repeat until` loop (e.g., draw until reaching screen edge) or a `while` condition in an art algorithm, introducing data-dependent looping rather than fixed-count repetition.
- **Challenge format:** Coding, starter project. Prompt: "Create a pattern that keeps repeating until the drawing reaches the edge of the screen." Students implement a condition-based loop. Auto‑grading checks loop type and that the output respects the stopping condition.
- **CSTA:** MS‑PRO‑PF‑01.

### T20.G7.03 – Understand how parameters change visual aesthetics

- **Short name:** Parameter impact on art design
- **Description:** Students investigate how varying a parameter (pen size, angle increment, randomness level) changes the visual result and explain the relationship between the mathematical parameter and the aesthetic effect.
- **Challenge format:** Concept/interactive exploration. A project with sliders or input fields controlling parameters (e.g., number of sides, size scale, rotation speed). Students adjust parameters and observe the effect. Auto‑grading may use response entries asking students to predict or explain the effect of a change.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T20.G7.04 – Recognize patterns in real-world algorithmic art and design

- **Short name:** Analyze real generative art
- **Description:** Students study examples of algorithmic art or generative design from artists or nature (fractals, Penrose tilings, algorithmic music visualizers) and identify the underlying algorithmic principles.
- **Challenge format:** Concept, analysis/discussion. Show images or videos of algorithmic art; ask: "What loops, patterns, or parameters might create this design?" Students write or verbally explain the algorithm. Auto‑grading uses open-ended response rubrics or structured explanations.
- **CSTA:** MS‑ALG‑AF‑02, CAS‑ET (Emerging technologies).

---

## Grade 8

Grade 8 synthesizes algorithmic art with broader computational concepts: efficiency, visualization of complex data, AI/ML in creative generation, and social/ethical impacts of algorithm-driven design.

### T20.G8.01 – Design and implement a complex data visualization

- **Short name:** Advanced data visualization
- **Description:** Students design a script that visualizes a larger or more complex dataset (multiple variables, time series) in an artistic way. They choose how to represent data dimensions (color, size, position, animation) and justify their choices.
- **Challenge format:** Coding, capstone project. Provided: a dataset with 3+ variables. Prompt: "Create a visualization that shows relationships in the data." Students implement loops to iterate over data, conditionals to map data to visual properties, and variables to control the design. Auto‑grading checks code structure, data accuracy, and may include peer/teacher evaluation of design choices.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP/DI.

### T20.G8.02 – Create generative or randomized art with constrained variation

- **Short name:** Constrained generative art
- **Description:** Students build an algorithm that uses randomness and loops to generate unique artwork on each run, but with constraints (e.g., a color palette, size limits, or symmetry rules) to maintain aesthetic quality.
- **Challenge format:** Coding, creative challenge. Prompt: "Create art that looks different each time but always follows certain rules (e.g., stays symmetrical, uses a color palette)." Students implement loops with constrained random values. Auto‑grading runs multiple times and checks that outputs vary while respecting constraints.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T20.G8.03 – Analyze social and creative implications of algorithms in art

- **Short name:** Algorithms and creativity
- **Description:** Students explore how algorithmic choices affect the artistic result and discuss ethical/creative questions: Does algorithmic art count as "real" art? How do algorithm parameters influence what is created? Can algorithms replicate human creativity?
- **Challenge format:** Concept, discussion/written reflection. Prompt: "Analyze an algorithmic art example. How does the algorithm shape what is created? What are the limits and possibilities?" Students write responses or participate in discussions. Auto‑grading uses rubrics to evaluate reasoning about algorithm and aesthetics.
- **CSTA:** CAS‑ET (Emerging technologies, AI creativity).

### T20.G8.04 – Optimize art rendering for performance

- **Short name:** Optimize art code for speed
- **Description:** Students profile or analyze an art script and identify bottlenecks (e.g., too many draw calls, redundant calculations). They refactor to improve performance while maintaining visual output.
- **Challenge format:** Coding, performance challenge. A starter script draws complex art but runs slowly. Students modify it (e.g., reduce loop iterations, cache calculations, or batch draw commands) to improve frame rate or responsiveness. Auto‑grading checks code changes and measures or assesses performance improvements.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

---
