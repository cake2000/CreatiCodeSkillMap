# T01 – Everyday Algorithms: K–8 Skill List (v6, IXL‑Style Microsteps)

Topic reference: `T01 Everyday Algorithms` in `domains_topics_overview.md`  
Domain: Algorithms & Design (D1) · Primary CSTA focus: ALG‑AF, with links to ALG‑PS, ALG‑IM, PRO‑PF, PRO‑TR

This v6 version is designed to feel like **IXL for algorithms**, with:

- **No big jumps**: each new skill is a tiny step from the previous one (read → trace → write → debug → compare).  
- **Uneven skill density on purpose**:
  - K–2: fewer, playful, picture‑based skills for concrete routines and patterns.  
  - G3–5: the **densest years** (most skills) because coding and algorithm patterns begin here.  
  - G6–8: focused, higher‑order skills on efficiency, fairness, simulations, recursion, and refactoring.
- **Loops and variables treated as big ideas**:
  - Many micro‑skills around identifying, tracing, adding, tuning, comparing, and debugging loops and variables in algorithms.
- A mix of **concept‑only**, **read/trace**, **write/refactor**, and **debug/compare** skills for each idea.
- K–2 skills that remain **picture‑based and enjoyable**, per `docs/K2_QUALITY_GUIDELINES.md`.
- **Interplay with T02 – Algorithm Diagrams:**
  - T02 is the main home for learning *how to read and convert* algorithm representations (strips, box diagrams, flowcharts, pseudocode, trace tables, and code tracing).  
  - T01 occasionally uses these representations, but always in service of **choosing, improving, or explaining algorithms for real tasks** (mazes, games, simulations, fairness scenarios).  
  - Representation‑heavy T01 skills (especially in Grades 5–6) should list the relevant T02 microsteps as prerequisites and assume students are already comfortable with the notation itself.
- **Interplay with T04 – Algorithm Patterns:**
  - T04 is where students first **name and recognize standard patterns** (visual repeats, loop shapes, counters, accumulators, search, “bounce on edge,” etc.).  
  - T01 reuses these patterns inside concrete algorithms and projects (e.g., maze solvers, games, simulations) without re‑teaching the pattern mechanics; it focuses on when and why to apply them for a particular task.  
  - Loop‑ and if/then‑heavy T01 skills (especially in Grades 3–5) should list the relevant T04 pattern microsteps as prerequisites so students meet the pattern concept before they use it in full algorithms.

## Teacher Guidance & Sequencing

- **K–2 (concept‑only):** Use T01 K–2 alongside picture‑based work in T02–T05. Keep student language to “steps,” “rules,” and “routines” rather than “algorithms” or “code,” so tasks stay unplugged and concrete.  
- **Grade 3 gateway:** Treat `T01.G1.01` (everyday algorithms) and `T01.G3.01` (first event‑driven sequence) as *gateway skills* that deserve extra practice and teacher‑led examples before students move into heavier loop and conditional work in T06–T09.  
- **Within a grade:** Move in this order: concept/read skills → write/build skills → debug/compare skills. For example, in Grade 3 use `T01.G3.02`, `T01.G3.03–G3.04`, and `T01.G3.09–G3.10` before tackling debugging (`T01.G3.13–G3.15`).  
- **Cross‑topic:** Pair T01 with:
  - **T02** when you want to emphasize diagrams, flowcharts, and tracing.  
  - **T03** when turning everyday tasks and project ideas into plans.  
  - **T04** when highlighting named patterns like “repeat,” counters, or search that reappear across projects.  
  - **T06–T09** when you are ready for focused construct practice (events, loops, conditionals, variables) after students understand the underlying algorithm ideas here.

Skills are grouped by grade and within each grade by **strands**. IDs follow `T01.G<grade>.<nn>`. This file supersedes earlier v4/v5 drafts as the **current, high‑granularity design** for T01.

---

## Grade K (PreK–K) – Everyday Sequences & Patterns

Strands: **K‑A Simple routines**, **K‑B Story order & sense‑making**, **K‑C Repeating actions**

### K‑A: Simple routines

**T01.GK.01 – Sequence a 3‑step daily routine**  
Students arrange 3 pictures (e.g., “put on pajamas,” “brush teeth,” “get in bed”) into first‑next‑last order.  
_Format:_ Drag‑drop sequence (3 items). · _CSTA:_ EK‑ALG‑AF‑01.

**T01.GK.02 – Sequence a 4‑step daily routine**  
Students order 4 pictures for a classroom routine (e.g., arrive, hang backpack, sit, listen).  
_Format:_ Drag‑drop 4 items. · _CSTA:_ EK‑ALG‑AF‑01.

**T01.GK.03 – Identify the first and last steps**  
Given an ordered 3–4 step routine, students tap which picture is first and which is last.  
_Format:_ Click first/last pictures. · _CSTA:_ EK‑ALG‑AF‑01.

### K‑B: Story order & sense‑making

**T01.GK.04 – Decide if a sequence makes sense**  
Students compare two short sequences and pick which one shows a sensible order (e.g., “wash → dry → eat” vs “eat → wash → dry”).  
_Format:_ Two sequences, choose one. · _CSTA:_ EK‑ALG‑AF‑01, EK‑ALG‑IM‑04.

**T01.GK.05 – Fix one step that is out of order**  
Students see a routine where one picture is in the wrong place and drag it into the right slot.  
_Format:_ Drag the “wrong” card into correct position. · _CSTA:_ EK‑ALG‑AF‑01, EK‑ALG‑PS‑03.

**T01.GK.06 – Predict the last step from the first two**  
Students see the first two pictures of a 3‑step routine and choose the correct last step from options.  
_Format:_ MCQ, choose final picture. · _CSTA:_ EK‑ALG‑AF‑01.

### K‑C: Repeating actions

**T01.GK.07 – Spot a repeating action pattern**  
Students watch short patterns (hop–clap–hop–clap) and pick the pair that shows the repeating unit.  
_Format:_ Visual pattern MCQ. · _CSTA:_ EK‑ALG‑AF‑01, EK‑ALG‑PS‑03.

**T01.GK.08 – Count how many times an action repeats**  
Students watch a character repeat an action and choose how many times it happened.  
_Format:_ Short animation + picture‑based count choices. · _CSTA:_ EK‑ALG‑AF‑01.

---

## Grade 1 – Creating, Predicting, and Comparing Algorithms

Strands: **1‑A Build multi‑step instructions**, **1‑B Predict/debug**, **1‑C Compare & choose**

### 1‑A: Build multi‑step instructions

**T01.G1.01 – Create a 4‑step everyday algorithm**  
Students arrange 4 pictures or phrases into a sensible order for a task like “plant a seed.”  
_Format:_ Drag‑drop (4 items). · _CSTA:_ E1‑ALG‑AF‑01.

**T01.G1.02 – Create a 5‑step everyday algorithm**  
Students extend to 5‑step routines (e.g., “get bowl, pour cereal, pour milk, eat, wash bowl”).  
_Format:_ Drag‑drop (5 items). · _CSTA:_ E1‑ALG‑AF‑01.

**T01.G1.03 – Add a missing last step to a routine**  
Students see a 3‑step routine and choose the correct 4th step.  
_Format:_ MCQ picture choice. · _CSTA:_ E1‑ALG‑AF‑01.

### 1‑B: Predict & debug

**T01.G1.04 – Predict the next step in a story sequence**  
Students see 3 ordered panels and choose what happens next.  
_Format:_ MCQ visuals. · _CSTA:_ E1‑ALG‑AF‑01, E1‑ALG‑PS‑03.

**T01.G1.05 – Find the missing step in an algorithm**  
Students see a 4‑step sequence with one blank and choose which picture fills the gap.  
_Format:_ Click‑select from options. · _CSTA:_ E1‑ALG‑AF‑01, E1‑ALG‑PS‑03.

**T01.G1.06 – Fix a routine with one wrong step**  
Students identify a clearly wrong step (e.g., “eat” before “cook”) and replace it with a correct picture.  
_Format:_ Select wrong step, then replacement. · _CSTA:_ E1‑ALG‑AF‑01.

### 1‑C: Compare & choose

**T01.G1.07 – Decide if two algorithms finish with the same result**  
Students compare two routines and decide whether both achieve the same goal.  
_Format:_ Side‑by‑side sequences with Yes/No or “Which work?” question. · _CSTA:_ E1‑ALG‑AF‑01, E1‑ALG‑PS‑03.

**T01.G1.08 – Choose the algorithm that uses fewer steps**  
Students pick between two correct routines that differ in length; they choose the shorter correct one.  
_Format:_ Choose shorter correct sequence. · _CSTA:_ E1‑ALG‑IM‑04.

**T01.G1.09 – Match an algorithm to its goal**  
Students match short routines to labels like “clean desk,” “feed pet,” “get ready for recess.”  
_Format:_ Matching lines between sequences and goals. · _CSTA:_ E1‑ALG‑AF‑01.

**T01.G1.10 – Recognize simple everyday if/then rules**  
Students match pictures to natural‑language if/then rules (“If it rains, then use an umbrella.”).  
_Format:_ MCQ match picture ↔ sentence. · _CSTA:_ E1‑ALG‑AF‑01 (conceptual branching).

---

## Grade 2 – Everyday Algorithms with Choices and Repeats

Strands: **2‑A Repeat/“do again”**, **2‑B If/then choices**, **2‑C Trace & debug**, **2‑D Mazes**

### 2‑A: Repeat / “do again”

**T01.G2.01 – Identify repeated actions in a routine**  
Students find which action happens over and over in a picture‑based routine, building on the pattern sense from T04 K–1 but tying it to a whole everyday task.  
_Format:_ Highlight or MCQ. · _CSTA:_ E2‑ALG‑AF‑01.

**T01.G2.02 – Use “repeat” to describe repeated actions**  
Students choose the shorter description of repeated steps that uses “repeat ___ times” to describe a full routine, applying compressed‑description ideas from T04.G2.x to concrete classroom or home scenarios.  
_Format:_ MCQ (long explicit vs “repeat” version). · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

**T01.G2.03 – Replace repeated steps with a repeat instruction**  
Students rewrite a long list of repeated steps for a real‑world routine as one step with “repeat ___ times,” treating “repeat” as a tool for clearer everyday algorithms rather than just an abstract pattern puzzle.  
_Format:_ Choose or assemble compressed description with “repeat.” · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

### 2‑B: If/then choices

**T01.G2.04 – Match if/then rules to pictures**  
Students match simple “If it is ___, then do ___” rules to images (rainy/sunny, door open/closed).  
_Format:_ Visual MCQ. · _CSTA:_ E2‑ALG‑AF‑01.

**T01.G2.05 – Complete a simple if/then algorithm**  
Students fill in missing condition or action in an if/then pair for a daily scenario.  
_Format:_ Fill‑in with picture or word cards. · _CSTA:_ E2‑ALG‑AF‑01.

**T01.G2.06 – Choose the best if/then rule for a situation**  
Students choose which of several if/then statements fits a picture story.  
_Format:_ MCQ; auto‑graded. · _CSTA:_ E2‑ALG‑AF‑01.

### 2‑C: Trace & debug

**T01.G2.07 – Trace an algorithm that uses an if/then choice**  
Students follow short number/picture algorithms with if/then and identify the final result.  
_Format:_ Tracing + MCQ result. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

**T01.G2.08 – Trace an algorithm that uses “repeat ___ times”**  
Students compute total actions or final position for routines with “repeat 3 times.”  
_Format:_ Tracing + MCQ. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

**T01.G2.09 – Fix a wrong repeat count in an algorithm**  
Students adjust a repeat count that causes too many or too few repetitions.  
_Format:_ Increase/decrease repeat number; auto‑graded via final outcome. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

**T01.G2.10 – Fix a wrong or missing if/then branch**  
Students correct an if/then rule that doesn’t match a picture situation.  
_Format:_ MCQ or card swap. · _CSTA:_ E2‑ALG‑AF‑01.

### 2‑D: Mazes and navigation

**T01.G2.11 – Trace maze directions on a simple grid**  
Students see a character on a small grid and a sequence of “forward/left/right” arrows, then choose where the character ends up.  
_Format:_ Path tracing with MCQ final position; auto‑graded by ending cell. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

**T01.G2.12 – Choose directions that reach the goal**  
Students see a start and goal on a grid and pick which of several arrow sequences reaches the goal without hitting a wall.  
_Format:_ MCQ (choose arrow sequence); auto‑graded via simulation. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

**T01.G2.13 – Write directions to navigate a simple grid**  
Students create “forward/left/right” instructions that move a character from start to finish.  
_Format:_ Drag arrow cards; auto‑graded via simulation. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

**T01.G2.14 – Fix maze directions that miss the goal**  
Students correct a set of directions that doesn’t reach the goal or hits a wall.  
_Format:_ Edit arrow sequence; auto‑graded via new simulation. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

---

## Grade 3 – First Algorithms in Code (Loops & Choices in Microsteps)

Strands: **3‑A Build simple coded algorithms**, **3‑B Loops as repeated steps**, **3‑C If/then in code**, **3‑D Read & debug**

### 3‑A: Build simple coded algorithms

**T01.G3.01 – Build a simple event‑driven sequence**  
Students complete a partially built script that is triggered by an event by adding 1–2 missing blocks so it runs a clear 3–5 block sequence, starting from a highly scaffolded starter project.  
_Format:_ Guided coding in a starter project (mostly pre‑built); auto‑graded via final behavior. · _CSTA:_ E3‑ALG‑AF‑01, E3‑PRO‑PF‑01.

**T01.G3.02 – Match a story description to a code sequence**  
Students choose which of several scripts matches a natural‑language description.  
_Format:_ MCQ, code snippets. · _CSTA:_ E3‑ALG‑AF‑01, E3‑ALG‑PS‑03.

### 3‑B: Loops as repeated steps (baby steps)

**T01.G3.03 – Identify repeated blocks in a script (no loops)**  
Students highlight which part of a script repeats the same action several times in a *specific project script*, applying the loop‑pattern recognition they developed in T04.G1–G3 to a real algorithm context.  
_Format:_ Highlight or click region in code. · _CSTA:_ E3‑ALG‑AF‑01.

**T01.G3.04 – Predict how many times repeated blocks run**  
Students count how many times an action happens based on repeated blocks (e.g., 4× `move 10`) in a concrete behavior (like a character walking), connecting T04’s abstract repeat units to meaningful movement or actions.  
_Format:_ MCQ; auto‑graded. · _CSTA:_ E3‑ALG‑AF‑01.

**T01.G3.05 – Replace repeated blocks with a repeat loop**  
Students refactor repeated blocks into a `repeat` loop with the correct count in a small project script, using loop patterns first explored in T04.G3.01–G3.02 to improve a real algorithm.  
_Format:_ Coding refactor; auto‑graded by structure + behavior. · _CSTA:_ E3‑ALG‑AF‑01, E3‑PRO‑PF‑01.

**T01.G3.06 – Trace a repeat loop to find total movement**  
Students trace a script with a `repeat` loop to determine how far a sprite moves or how many actions occur.  
_Format:_ Tracing + MCQ. · _CSTA:_ E3‑ALG‑AF‑01.

**T01.G3.07 – Adjust a repeat count to match a pattern**  
Students change the repeat number so a pattern (e.g., a square, a full spin) completes exactly.  
_Format:_ Edit loop count; auto‑graded via final orientation/pattern. · _CSTA:_ E3‑ALG‑AF‑01, E3‑PRO‑PF‑01.

### 3‑C: If/then in code

**T01.G3.08 – Add a simple if/then to a script**  
Students insert an `if touching [color/sprite]` block to trigger an action.  
_Format:_ Coding, scaffolded; auto‑graded by behavior. · _CSTA:_ E3‑ALG‑AF‑01, E3‑PRO‑PF‑01.

**T01.G3.09 – Match an if/then script to a behavior description**  
Students pick which script with if/then matches a described behavior (“When you touch the goal, say ‘Yay!’.”).  
_Format:_ MCQ; auto‑graded. · _CSTA:_ E3‑ALG‑AF‑01.

**T01.G3.10 – Trace a script with a single if/then**  
Students predict whether the if/then block will run in a given situation.  
_Format:_ Tracing scenario + MCQ. · _CSTA:_ E3‑ALG‑AF‑01, E3‑ALG‑PS‑03.

### 3‑D: Read & debug

**T01.G3.11 – Explain in words what a short program does**  
Students select or write a one‑sentence description of a short script’s algorithm.  
_Format:_ Code‑reading MCQ/short answer. · _CSTA:_ E3‑ALG‑AF‑01, E3‑ALG‑PS‑03.

**T01.G3.12 – Predict the final state of a simple algorithm**  
Students trace a script (possibly with a loop) to predict final position or direction.  
_Format:_ Grid/orientation MCQ. · _CSTA:_ E3‑ALG‑AF‑01.

**T01.G3.13 – Debug a program with steps in the wrong order**  
Students rearrange blocks in a sequence script to match a given intended behavior.  
_Format:_ Coding re‑order; auto‑graded via behavior. · _CSTA:_ E3‑ALG‑AF‑01, E3‑PRO‑TR‑03.

**T01.G3.14 – Debug a loop that repeats the wrong number of times**  
Students fix a `repeat` loop that runs too many or too few times by adjusting the loop count so the behavior matches the description.  
_Format:_ Coding edit (loop count); auto‑graded via final behavior. · _CSTA:_ E3‑ALG‑AF‑01, E3‑PRO‑TR‑03.

**T01.G3.15 – Debug an if/then that doesn’t trigger when it should**  
Students fix a simple if/then condition so an action (like saying “Yay!” at the goal) happens at the right time.  
_Format:_ Coding edits; auto‑graded with multiple tests. · _CSTA:_ E3‑ALG‑AF‑01, E3‑PRO‑TR‑03.

---

## Grade 4 – Loops & Variables as Algorithm Tools (Microsteps)

Strands: **4‑A Plan & implement**, **4‑B Loops for efficiency**, **4‑C Variables as counters & trackers**, **4‑D Trace, compare, debug**

### 4‑A: Plan & implement

**T01.G4.01 – Plan steps for a coded maze or goal‑reach task**  
Students write numbered steps in words for “reach the flag without touching red walls.”  
_Format:_ Arrange/choose steps. · _CSTA:_ E4‑ALG‑AF‑01.

**T01.G4.02 – Implement a written plan in code**  
Students turn a given plan into a CreatiCode script and test it.  
_Format:_ Coding; auto‑grading checks match between plan and behavior. · _CSTA:_ E4‑ALG‑AF‑01, E4‑PRO‑PF‑01.

### 4‑B: Loops for efficiency (microsteps)

**T01.G4.03 – Identify repeated patterns in longer scripts**  
Students highlight repeated sequences (not just single blocks) in longer scripts.  
_Format:_ Highlight blocks; auto‑grading checks region. · _CSTA:_ E4‑ALG‑AF‑01.

**T01.G4.04 – Replace repeated patterns with loops**  
Students refactor repeated patterns into loops that contain multiple blocks.  
_Format:_ Coding refactor; auto‑graded by behavior & fewer blocks. · _CSTA:_ E4‑ALG‑AF‑01, E4‑ALG‑PS‑03.

**T01.G4.05 – Compare two versions of a script: with and without loops**  
Students compare a long “no loops” script and a shorter “with loops” version and choose which is better and why.  
_Format:_ Side‑by‑side code comparison with MCQ explanation. · _CSTA:_ E4‑ALG‑IM‑04.

### 4‑C: Variables as counters & trackers (microsteps)

**T01.G4.06 – Recognize variables in a program**  
Students identify which names in a script are variables and what they store.  
_Format:_ Code‑reading MCQ/highlight. · _CSTA:_ E4‑PRO‑DH‑02.

**T01.G4.07 – Trace a simple counter variable**  
Students follow a script that initializes a variable and increments it in a loop, then predict its final value.  
_Format:_ Tracing + MCQ. · _CSTA:_ E4‑ALG‑AF‑01, E4‑PRO‑DH‑02.

**T01.G4.08 – Add a variable to count events in a program**  
Students add a variable (e.g., `steps`, `coins`) and increment it at the right place in an existing script.  
_Format:_ Coding; auto‑grading checks updates and display. · _CSTA:_ E4‑ALG‑AF‑01, E4‑PRO‑DH‑02.

**T01.G4.09 – Use a variable to track a simple game state (lives or points)**  
Students extend a game to use a variable for lives or points, decreasing or increasing it based on events.  
_Format:_ Coding; auto‑graded on correct updates. · _CSTA:_ E4‑ALG‑AF‑01, E4‑PRO‑DH‑02.

### 4‑D: Trace, compare, debug

**T01.G4.10 – Trace a multi‑step algorithm with loops and variables**  
Students trace code with a loop and variable updates to find final values or positions.  
_Format:_ Code‑reading + MCQ. · _CSTA:_ E4‑ALG‑AF‑01, E4‑ALG‑PS‑03.

**T01.G4.11 – Debug an off‑by‑one counting bug**  
Students fix a counter that ends too high or too low by adjusting initialization or loop bounds.  
_Format:_ Coding edits; auto‑graded with multiple tests. · _CSTA:_ E4‑ALG‑AF‑01, E4‑PRO‑TR‑03.

**T01.G4.12 – Explain why one algorithm solution is better than another**  
Students compare two working algorithms and explain which they prefer (fewer steps, easier to read) and why.  
_Format:_ MCQ + short explanation. · _CSTA:_ E4‑ALG‑IM‑04.

---

## Grade 5 – Representing, Comparing, and Proving Algorithms

Strands: **5‑A Representations ↔ code**, **5‑B Correctness & efficiency**, **5‑C Edge cases & refinement**

### 5‑A: Representations ↔ code

**T01.G5.01 – Match a word description to a flowchart**  
Students match everyday‑language descriptions of algorithms to flowcharts, applying the flowchart symbols and reading skills introduced in T02 (Grades 3–4) to real‑world tasks.  
_Format:_ MCQ matching, using familiar contexts (games, classroom routines). · _CSTA:_ E5‑ALG‑AF‑01.

**T01.G5.02 – Convert a flowchart or pseudocode into code**  
Students implement simple flowcharts/pseudocode (that follow patterns already practiced in T02.G4.x–T02.G5.x) as block‑based code for small CreatiCode projects.  
_Format:_ Coding; auto‑graded on behavior and basic correspondence between diagram/pseudocode and code. · _CSTA:_ E5‑ALG‑AF‑01, E5‑PRO‑PF‑01.

**T01.G5.03 – Convert a short program into pseudocode**  
Students rewrite a short program as structured pseudocode showing loops, if/then, and variables, using the pseudocode conventions introduced in T02 and focusing on clarity for a human reader who is thinking about the real task.  
_Format:_ Guided pseudocode; rubric/auto‑grading focused on structure and faithfulness to behavior. · _CSTA:_ E5‑ALG‑AF‑01, E5‑ALG‑PS‑03.

### 5‑B: Correctness & efficiency (using loops & variables)

**T01.G5.04 – Trace a search algorithm using loops and variables**  
Students trace a simple “find the largest” or “count matches” algorithm and track how a variable changes.  
_Format:_ Tracing table; auto‑graded. · _CSTA:_ E5‑ALG‑PS‑03, E5‑PRO‑DH‑02.

**T01.G5.05 – Determine whether an algorithm is correct for all inputs**  
Students apply test cases to decide if an algorithm always gives the right answer.  
_Format:_ Choose “always works” vs “fails sometimes” with evidence. · _CSTA:_ E5‑ALG‑PS‑03.

**T01.G5.06 – Compare two algorithms for step counts (efficiency)**  
Students estimate or count loop iterations and compare efficiency.  
_Format:_ Tables + MCQ; auto‑graded. · _CSTA:_ E5‑ALG‑PS‑03, E5‑ALG‑IM‑04.

### 5‑C: Edge cases & refinement

**T01.G5.07 – Debug an algorithm that mis‑handles a simple edge case**  
Students fix a bug where an algorithm fails on empty input or a special case.  
_Format:_ Coding edits; auto‑graded tests. · _CSTA:_ E5‑ALG‑PS‑03, E5‑PRO‑TR‑03.

**T01.G5.08 – Add checks to handle edge cases**  
Students extend an algorithm to include extra if/then checks for invalid or special inputs.  
_Format:_ Coding; test both regular and edge cases. · _CSTA:_ E5‑ALG‑PS‑03.

**T01.G5.09 – Explain why an algorithm is correct using loops and variables**  
Students explain why a loop + variable algorithm (e.g., max, count) is guaranteed to work.  
_Format:_ Structured explanation; auto‑graded patterns. · _CSTA:_ E5‑ALG‑PS‑03.

**T01.G5.10 – Rewrite a long algorithm using loops or helper steps**  
Students reduce a long algorithm to a shorter one using loops or helper steps without changing behavior.  
_Format:_ Pseudocode/code refactor; rubric/auto‑graded. · _CSTA:_ E5‑ALG‑AF‑01, E5‑ALG‑PS‑03.

---

## Grade 6 – Efficiency & Fairness in Algorithms

Strands: **6‑A Efficiency & scaling**, **6‑B Algorithm impacts**, **6‑C Flowchart↔code**

**T01.G6.01 – Count comparisons in linear and binary search**  
Students fill in how many comparisons each algorithm uses for given list sizes.  
_Format:_ Table; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑02.

**T01.G6.02 – Compare how step counts grow with input size**  
Students interpret tables/graphs to see which algorithm scales better.  
_Format:_ MCQ + explanation. · _CSTA:_ MS‑ALG‑AF‑02, MS‑ALG‑PS‑05.

**T01.G6.03 – Spot unnecessary work in an algorithm**  
Students highlight lines where an algorithm keeps working after the result is found.  
_Format:_ Code highlight; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑01.

**T01.G6.04 – Revise an algorithm to do less work**  
Students remove redundant checks/loops without changing output.  
_Format:_ Pseudocode/coding edit; auto‑graded on correctness + fewer steps. · _CSTA:_ MS‑ALG‑AF‑01, MS‑ALG‑PS‑05.

**T01.G6.05 – Identify who is favored or harmed by a decision algorithm**  
Students analyze a simple decision algorithm for fairness across groups.  
_Format:_ Scenario MCQ + short explanation. · _CSTA:_ MS‑ALG‑IM‑08.

**T01.G6.06 – Suggest a change to make a decision algorithm more fair**  
Students propose specific changes to reduce bias or harm.  
_Format:_ Structured response; auto‑graded by alignment with identified issue. · _CSTA:_ MS‑ALG‑IM‑09.

**T01.G6.07 – Design a flowchart for a multi‑step program**  
Students design a flowchart for a game turn (ask, check, update score, continue/stop), building on the flowchart symbols, loops, and decisions practiced in T02 up through Grade 6.  
_Format:_ Flowchart design tied to a concrete game scenario; rubric. · _CSTA:_ MS‑ALG‑AF‑01.

**T01.G6.08 – Implement code from a detailed flowchart**  
Students map each shape in a detailed, multi‑step flowchart to code constructs in a CreatiCode project, focusing on correctness and readability rather than learning new notation.  
_Format:_ Coding; auto‑graded structure + tests, assumes prior diagram‑to‑code practice from T02.G6.05. · _CSTA:_ MS‑ALG‑AF‑01, MS‑PRO‑PF‑01.

---

## Grade 7 – Algorithm Patterns, Choice, and Testing

Strands: **7‑A Recognize & apply patterns**, **7‑B Choose algorithms**, **7‑C Edge cases & improvement**

**T01.G7.01 – Identify the pattern in a given program**  
Students categorize code as search, sort, accumulation, or simulation.  
_Format:_ MCQ; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑01.

**T01.G7.02 – Choose a pattern to solve a problem**  
Students pick which algorithm pattern is best for a described task.  
_Format:_ MCQ; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑01, MS‑ALG‑PS‑06.

**T01.G7.03 – Write pseudocode for a search or accumulation algorithm**  
Students write structured pseudocode for “find max” or “count items that match.”  
_Format:_ Guided pseudocode; auto‑graded structure. · _CSTA:_ MS‑ALG‑AF‑01, MS‑PRO‑PF‑02.

**T01.G7.04 – Compare efficiency of two algorithms qualitatively**  
Students reason which algorithm scales better as inputs grow.  
_Format:_ Scenario + MCQ + explanation. · _CSTA:_ MS‑ALG‑AF‑02, MS‑ALG‑PS‑05.

**T01.G7.05 – Design a set of edge‑case tests for an algorithm**  
Students pick tests (including edge cases) that give high confidence the algorithm works.  
_Format:_ Choose tests from list; auto‑graded for coverage. · _CSTA:_ MS‑ALG‑PS‑05, MS‑PRO‑TR‑11.

**T01.G7.06 – Run an algorithm on edge cases and find failures**  
Students test algorithms on tricky inputs and flag those that fail.  
_Format:_ MCQ/interactive; auto‑graded. · _CSTA:_ MS‑ALG‑PS‑05.

**T01.G7.07 – Explain why an algorithm fails on a specific edge case**  
Students explain which step causes the failure and why.  
_Format:_ Structured explanation; auto‑graded patterns. · _CSTA:_ MS‑ALG‑PS‑05, MS‑PRO‑TR‑11.

**T01.G7.08 – Rewrite a naive algorithm using a better pattern**  
Students replace repeated naive logic with a cleaner pattern (single loop, flag, etc.).  
_Format:_ Pseudocode/coding refactor; rubric. · _CSTA:_ MS‑ALG‑AF‑01, MS‑ALG‑PS‑06.

---

## Grade 8 – Simulations, Recursion, Impacts, and Refactoring

Strands: **8‑A Simulations & update rules**, **8‑B Recursive thinking**, **8‑C Impacts & refactoring**

**T01.G8.01 – Design one‑step update rules for a simple simulation**  
Students specify how state variables change in one timestep of a simulation.  
_Format:_ Code/pseudocode blanks; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑01, DAA‑DI.

**T01.G8.02 – Interpret the behavior of a simulation algorithm over time**  
Students explain what happens to variables after several steps.  
_Format:_ Code + graph reading; MCQ/short answer. · _CSTA:_ MS‑ALG‑AF‑02, DAA‑DI.

**T01.G8.03 – Compare two simulations with slightly different rules**  
Students explain how changed rules affect outcomes.  
_Format:_ Side‑by‑side comparison + explanation. · _CSTA:_ MS‑ALG‑AF‑02, DAA‑DI.

**T01.G8.04 – Identify base case and recursive step in an algorithm description**  
Students highlight base case and recursive step in natural‑language recursion.  
_Format:_ MCQ/highlight; auto‑graded. · _CSTA:_ MS‑ALG‑PS‑07.

**T01.G8.05 – Trace a conceptual recursive algorithm on small inputs**  
Students step through recursion (e.g., factorial, sum of list) for small inputs.  
_Format:_ Tracing table; auto‑graded. · _CSTA:_ MS‑ALG‑PS‑07.

**T01.G8.06 – Analyze who is helped or harmed by a real‑world algorithm**  
Students identify stakeholders and impacts of a real‑world algorithm.  
_Format:_ Scenario with MCQ + short answers. · _CSTA:_ MS‑ALG‑IM‑08.

**T01.G8.07 – Propose changes to make a real‑world algorithm more fair**  
Students propose specific mitigations based on identified harms.  
_Format:_ Structured responses; auto‑graded alignment. · _CSTA:_ MS‑ALG‑IM‑09.

**T01.G8.08 – Refactor a medium‑sized program for clarity**  
Students reorganize code into helper blocks, remove duplication, and add meaningful names.  
_Format:_ Coding refactor; auto‑graded via behavior + structure. · _CSTA:_ MS‑PRO‑TR‑11.

**T01.G8.09 – Refactor a medium‑sized program for efficiency**  
Students make local changes (e.g., break loops early, avoid unnecessary recomputation) to reduce work.  
_Format:_ Coding edits; auto‑graded for unchanged outputs and fewer steps. · _CSTA:_ MS‑ALG‑PS‑05, MS‑PRO‑TR‑11.

**T01.G8.10 – Use logging/probes to understand algorithm behavior**  
Students insert logs or display statements at key points and use them to answer questions about an algorithm’s internal behavior.  
_Format:_ Coding + reading logs; auto‑graded. · _CSTA:_ MS‑ALG‑PS‑07, MS‑PRO‑TR‑11.

---

## Summary of Granularity & Loops/Variables Coverage

- **K–2:** ~8–12 playful, picture‑based skills per grade focusing on everyday sequences, if/then ideas, repeats, and maze‑style tracing, with no text entry required.
- **G3–5:** highest density with many micro‑skills for:
  - **Loops:** find repeated blocks → count → replace with loops → trace loops → tune loop counts → apply loops in search/accumulation → compare loop vs no‑loop algorithms.  
  - **Variables:** recognize variables → trace counters → add counters to scripts → track game state → trace loop+variable algorithms → debug miscounts → use them in correctness explanations.
- **G6–8:** focused skills on:
  - Efficiency and scaling (step counts, unnecessary work, improved patterns),  
  - Fairness and societal impacts of algorithms,  
  - Simulation update rules and high‑level recursive thinking,  
  - Refactoring mid‑sized programs for clarity and efficiency, plus logging to “peek inside” algorithms.

Every skill is designed as a **small, enjoyable step** that can be implemented as a short CreatiCode activity, mirroring IXL’s “painfully small” but highly effective incremental style.

### Notes on Dependencies and Alignment

- **Standards:** Skills map primarily to CSTA ALG‑AF with links to ALG‑PS/ALG‑IM and PRO‑PF/PRO‑TR. Fairness‑ and impact‑oriented skills in Grades 6–8 should also carry AI4K12 tags in implementation (e.g., categories D/E for ethical design and societal impacts).  
- **K–2 foundations:** T01 K–2 should be prerequisites for Grade 3 gateway construct topics (T06–T09), but K–2 activities themselves remain picture‑based, unplugged, and device‑agnostic.  
- **Grade 3 gateway:** Grade 3 T01 skills depend on K–2 T01–T05 foundations and then support, rather than gate, the core construct topics (T06–T09). In data files, avoid making T01.G3.x a prerequisite for students’ *first* exposure to loops/events/conditionals; instead, treat them as parallel practice and application.  
- **Inter‑topic dependencies:** Representation‑heavy T01 skills (especially Grades 5–6) should depend on T02 flowchart/pseudocode microsteps; loop and variable usage skills should depend on pattern skills in T04 and core construct skills in T07–T09.  
- **Classroom use:** Teachers can select short “ladders” within each grade (e.g., G3 read → build → debug) as mini‑units, or sprinkle individual skills across game, data, and AI projects to reinforce algorithm ideas without needing long, standalone algorithm lessons.
