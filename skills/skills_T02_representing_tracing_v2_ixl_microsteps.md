# T02 – Representing & Tracing Algorithms: K–8 Skill List (v2, IXL‑Style Microsteps)

Topic reference: `T02 Representing & Tracing Algorithms` in `domains_topics_overview.md`  
Domain: Algorithms & Design (D1) · Primary CSTA focus: ALG‑AF (with links to ALG‑PS, ALG‑HD)

This v2 version upgrades the original draft (`skills_T02_representing_tracing.md`) to an **IXL‑style microstep design**, aligned with the principles in `docs/TOPIC_IXL_MICROSTEP_GUIDE.md` and the v6 design for T01.

- **Role of T02:** Focused on *representations* of algorithms (pictures, boxes, flowcharts, pseudocode, code) and *tracing* them (following, predicting, debugging), not on inventing new real‑world tasks (T01) or core programming constructs (T06–T13).  
- **Microsteps:** Each skill targets a single, narrow role (read/trace, represent/convert, debug/fix, compare/choose). Larger v1 skills that bundled roles are split here.  
- **Uneven density:** More skills in **grades 3–6** where formal representations and tracing are first developed; lighter but still meaningful coverage in K–2 and 7–8.  
- **Dependencies:** T02 skills assume core construct knowledge comes from other topics (e.g., T01 for everyday algorithms, T06–T08 for events/loops/conditionals). Dependencies should primarily reference those gateway skills plus earlier T02 microsteps.
- **Implementability:** All skills can be implemented using CreatiCode’s picture‑based K–2 activities, block‑based coding environment, and simple UI widgets (for flowchart‑like diagrams, pseudocode entry, or multi‑choice/drag‑drop tasks).

IDs follow `T02.G<grade>.<nn>`. Existing v1 IDs are preserved with tightened scopes where needed; additional microsteps use higher `<nn>` values and will need to be added to the JSON skill maps in a later data pass.

---

## Grade K (PreK–K) – Seeing Routines as Algorithms

Strands: **K‑A Recognize sequences**, **K‑B Describe & fix**

### K‑A: Recognize sequences

**T02.GK.01 – Recognize picture steps for a task**  
Students look at 3–4 pictures that show steps in a familiar routine (e.g., brushing teeth) and identify that the ordered pictures are “the steps to do it” (an algorithm).  
_Format:_ Multiple‑choice with 2–3 picture sequences; choose which one shows the steps in a sensible order. · _CSTA:_ EK‑ALG‑AF‑01.

**T02.GK.02 – Order 3–4 pictures to make a story**  
Students drag 3–4 scrambled pictures into first‑next‑last order to make a simple routine.  
_Format:_ Drag‑drop sequence (3–4 items). · _CSTA:_ EK‑ALG‑AF‑01.

### K‑B: Describe & fix

**T02.GK.03 – Use first/next/last to describe a sequence**  
Students see 3 ordered pictures and complete sentence frames like “First we ___, next we ___, last we ___” by choosing words or icons that match.  
_Format:_ Picture‑supported sentence completion with audio. · _CSTA:_ EK‑ALG‑AF‑01.

**T02.GK.04 – Fix one picture that is out of order**  
Students see a 3‑picture routine where one picture is clearly in the wrong place and drag it into the correct slot.  
_Format:_ Drag one “wrong” card to the right position; auto‑graded by final order. · _CSTA:_ EK‑ALG‑AF‑01, EK‑ALG‑PS‑03.

---

## Grade 1 – Creating, Tracing, and Debugging Picture Algorithms

Strands: **1‑A Build picture algorithms**, **1‑B Trace & predict**, **1‑C Debug & compare**

### 1‑A: Build picture algorithms

**T02.G1.01 – Make a 3–4 step picture algorithm**  
Students are given a simple task (e.g., “how to feed the class pet”) and assemble 3–4 pictures into a sensible sequence that solves it.  
_Format:_ Drag‑drop cards into numbered slots; auto‑graded by order. · _CSTA:_ E1‑ALG‑AF‑01.

**T02.G1.02 – Add a missing step to a picture algorithm**  
Students see a 3‑step picture algorithm with one missing middle step and choose the correct picture to fill the gap.  
_Format:_ MCQ picture choice for the missing step. · _CSTA:_ E1‑ALG‑AF‑01, E1‑ALG‑PS‑03.

### 1‑B: Trace & predict

**T02.G1.03 – Trace a picture algorithm and tell the outcome**  
Students follow a 3–4 picture sequence (e.g., recipe) and choose what the final picture or outcome should be.  
_Format:_ Picture sequence + outcome MCQ; auto‑graded by outcome. · _CSTA:_ EK‑ALG‑AF‑01.

### 1‑C: Debug & compare

**T02.G1.04 – Find a broken picture algorithm**  
Students compare two 3–4 picture algorithms for the same task: one is correct, one has an obvious missing or wrong step. They pick which one is broken.  
_Format:_ Two sequences side by side; choose the broken one. · _CSTA:_ E1‑ALG‑AF‑01, E1‑ALG‑PS‑03.

**T02.G1.05 – Fix one wrong step in a picture algorithm**  
Students see a sequence with one clearly wrong picture (e.g., “eat sandwich” before “make sandwich”) and replace just that picture with the correct one.  
_Format:_ Click the wrong picture, then choose a replacement from 2–3 options. · _CSTA:_ E1‑ALG‑AF‑01, E1‑ALG‑PS‑03.

---

## Grade 2 – First Formal Representations & Block Tracing

Strands: **2‑A Boxes as step diagrams**, **2‑B Trace simple scripts**, **2‑C Match & debug**

### 2‑A: Boxes as step diagrams

**T02.G2.01 – Turn a picture routine into labeled boxes**  
Students see a 3–4 picture routine and build a horizontal row of labeled boxes (“Step 1,” “Step 2,” “Step 3”) that describe each step in simple words or icons.  
_Format:_ Drag icons into blank boxes and type or choose short labels; auto‑graded by order and coverage. · _CSTA:_ E2‑ALG‑AF‑01.

**T02.G2.02 – Read a box diagram and choose the matching pictures**  
Students are given a 3–4 box “algorithm diagram” and must choose which picture sequence matches it.  
_Format:_ Box diagram + 2–3 picture sequences; MCQ. · _CSTA:_ E2‑ALG‑AF‑01.

### 2‑B: Trace simple scripts

**T02.G2.03 – Trace a simple sequence‑only block script**  
Students see a short CreatiCode script with 3–6 blocks using only sequence (no loops or conditionals) and predict the sprite’s final position or message.  
_Format:_ Code‑reading MCQ; correctness checked via simulation. · _CSTA:_ E2‑ALG‑AF‑01.

**T02.G2.04 – Step through a script and mark intermediate states**  
Students click a “step” button to run one block at a time and mark where the sprite is after each step (e.g., on a number line or grid).  
_Format:_ Interactive trace with step button + checkpoints; auto‑graded by intermediate and final positions. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

### 2‑C: Match & debug

**T02.G2.05 – Match a box diagram to a script**  
Students match a simple 3–4 step box diagram to one of several scripts that implements it.  
_Format:_ Diagram + 3 scripts; MCQ; auto‑graded by behavior equivalence. · _CSTA:_ E2‑ALG‑AF‑01.

**T02.G2.06 – Fix a sequencing error in a script**  
Students are given a short script whose blocks are out of order and reorder them to match a target picture or box diagram.  
_Format:_ Drag‑to‑reorder; auto‑graded by final script and simulation. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

---

## Grade 3 – Flowchart Basics & Tracing Simple Code

Strands: **3‑A Flowchart basics**, **3‑B Trace code with choices & loops**, **3‑C Match flowcharts and code**

### 3‑A: Flowchart basics

**T02.G3.01 – Identify start, action, and end symbols**  
Students look at small flowcharts and identify which shapes mark “start,” “action,” and “end.”  
_Format:_ Click‑select shapes or match labels to shapes. · _CSTA:_ E3‑ALG‑AF‑01.

**T02.G3.02 – Turn a 3‑step routine into a basic flowchart**  
Students create a flowchart using start, action, and end symbols for a simple everyday process (no decisions yet).  
_Format:_ Drag symbols onto canvas, connect arrows, label actions; auto‑graded for structure. · _CSTA:_ E3‑ALG‑AF‑01.

### 3‑B: Trace code with choices & loops

**T02.G3.03 – Trace code with a single if/else**  
Students trace a script with one simple `if/else` block and a given condition (“key pressed” or not) to predict which branch runs and what happens.  
_Format:_ Code‑reading MCQ; checked against simulation. · _CSTA:_ E3‑ALG‑AF‑01.

**T02.G3.04 – Trace a repeat loop and count iterations**  
Students trace a script with a `repeat N` loop and answer questions like “How many times does this happen?” or “How far does the sprite move?”  
_Format:_ Code‑reading with numeric answer; auto‑graded by simulation. · _CSTA:_ E3‑ALG‑AF‑01.

### 3‑C: Match flowcharts and code

**T02.G3.05 – Match a simple flowchart to a script**  
Students choose which of several scripts matches a small flowchart with only actions (no decisions).  
_Format:_ Flowchart + 3 short scripts; MCQ. · _CSTA:_ E3‑ALG‑AF‑01.

**T02.G3.06 – Match a decision flowchart to if/else code**  
Students match a flowchart containing one decision diamond to a script that uses an `if/else` block.  
_Format:_ Flowchart + 3 scripts; MCQ; auto‑graded by logical equivalence. · _CSTA:_ E3‑ALG‑AF‑01.

---

## Grade 4 – Flowcharts with Loops & Multi‑Step Tracing

Strands: **4‑A Flowcharts with loops & decisions**, **4‑B Trace multi‑branch code**, **4‑C Pseudocode bridges**

### 4‑A: Flowcharts with loops & decisions

**T02.G4.01 – Add a loop to an existing flowchart**  
Students are shown a straight‑line flowchart and a description that includes repetition (e.g., “do this 5 times”) and must add a loop back arrow in the correct place.  
_Format:_ Edit an existing flowchart; auto‑graded by placement and labels. · _CSTA:_ E4‑ALG‑AF‑01.

**T02.G4.02 – Design a flowchart for a task with repetition**  
Students design a flowchart from scratch for a simple task that repeats (e.g., “Count from 1 to 5”), correctly showing the loop structure.  
_Format:_ Constructive flowchart activity; auto‑graded for loop correctness. · _CSTA:_ E4‑ALG‑AF‑01.

### 4‑B: Trace multi‑branch code

**T02.G4.03 – Trace code with a sequence of if/else blocks**  
Students trace code with 2–3 sequential `if/else` blocks and predict the final output for a given set of conditions.  
_Format:_ Code‑reading + prediction; auto‑graded via simulation. · _CSTA:_ E4‑ALG‑AF‑01.

**T02.G4.04 – Trace code that combines a loop and a condition**  
Students trace a script with a loop that contains an `if` block (e.g., bouncing off edges) to predict behavior after several iterations.  
_Format:_ Code‑reading or step‑through; auto‑graded by final state. · _CSTA:_ E4‑ALG‑AF‑01, E4‑ALG‑PS‑03.

### 4‑C: Pseudocode bridges

**T02.G4.05 – Convert a story description into simple pseudocode**  
Students turn a short natural‑language description or picture routine into ordered pseudocode lines like “Step 1: …; Step 2: …”.  
_Format:_ Text entry or card ordering; auto‑graded by order and coverage. · _CSTA:_ E4‑ALG‑AF‑01.

**T02.G4.06 – Match pseudocode to a flowchart**  
Students match a simple pseudocode listing to one of several flowcharts.  
_Format:_ Pseudocode + 2–3 candidate flowcharts; MCQ. · _CSTA:_ E4‑ALG‑AF‑01.

---

## Grade 5 – Detailed Flowcharts, Variables in Traces, and Efficiency

Strands: **5‑A Complex flowcharts**, **5‑B Trace variables & counters**, **5‑C Pseudocode & efficiency**

### 5‑A: Complex flowcharts

**T02.G5.01 – Read a multi‑branch flowchart and trace a path**  
Students are given a flowchart with several decision diamonds and must trace the path for a specific input (e.g., “It is rainy and cold”).  
_Format:_ Highlight path or choose final outcome; auto‑graded by selected path/outcome. · _CSTA:_ E5‑ALG‑AF‑01.

**T02.G5.02 – Design a multi‑branch flowchart for a decision task**  
Students design a flowchart with multiple decision points (e.g., “choose a game based on time and number of players”).  
_Format:_ Constructive flowchart tool; auto‑graded by structure and coverage of cases. · _CSTA:_ E5‑ALG‑AF‑01.

### 5‑B: Trace variables & counters

**T02.G5.03 – Trace a counter variable in a loop**  
Students trace a script where a variable starts at a value and changes inside a loop, predicting its final value.  
_Format:_ Code‑reading with table or MCQ; checked by simulation. · _CSTA:_ E5‑ALG‑AF‑01.

**T02.G5.04 – Trace an accumulator that sums values**  
Students trace code that adds values to a running total and determine the final sum.  
_Format:_ Code‑reading + numeric answer; auto‑graded. · _CSTA:_ E5‑ALG‑AF‑01, E5‑ALG‑PS‑03.

### 5‑C: Pseudocode & efficiency

**T02.G5.05 – Write pseudocode for a loop‑based algorithm**  
Students write structured pseudocode for a multi‑step algorithm that includes a loop and conditional, using clear indentation and step labels.  
_Format:_ Guided text entry or block‑pseudocode; auto‑graded for structure and logic. · _CSTA:_ E5‑ALG‑AF‑01.

**T02.G5.06 – Compare two algorithms for the same task**  
Students are given two short algorithms (flowcharts or pseudocode) solving the same problem and choose which uses fewer steps or is clearer, explaining why.  
_Format:_ MCQ + short justification; auto‑graded by selected option and key phrases. · _CSTA:_ E5‑ALG‑PS‑03.

---

## Grade 6 – Multi‑Representation Mastery & Nested Tracing

Strands: **6‑A Game/decision flowcharts**, **6‑B Nested tracing**, **6‑C Representation conversions**

### 6‑A: Game/decision flowcharts

**T02.G6.01 – Design a flowchart for a simple guessing game**  
Students design a flowchart for a higher/lower guessing game with loops and decisions, showing start, repeated guesses, and end when guessed correctly.  
_Format:_ Constructive flowchart; auto‑graded by structure and handling of end condition. · _CSTA:_ MS‑ALG‑AF‑01.

### 6‑B: Nested tracing

**T02.G6.02 – Trace nested loops with a table of values**  
Students trace code with nested loops and track changes to one or two variables in a table, predicting final values or patterns.  
_Format:_ Code‑reading + table fill‑in; auto‑graded by final row(s). · _CSTA:_ MS‑ALG‑AF‑01.

**T02.G6.03 – Trace nested loops that fill a grid pattern**  
Students trace nested loops that draw or fill a 2D grid (e.g., checkerboard), predicting how many cells are filled or what pattern appears.  
_Format:_ Code‑reading + grid visualization; auto‑graded by predicted pattern. · _CSTA:_ MS‑ALG‑AF‑01, MS‑ALG‑PS‑05.

### 6‑C: Representation conversions

**T02.G6.04 – Convert a flowchart to pseudocode**  
Students are given a small flowchart (with loops and decisions) and write equivalent pseudocode.  
_Format:_ Text entry or block‑pseudocode; auto‑graded by structure and logic. · _CSTA:_ MS‑ALG‑AF‑01.

**T02.G6.05 – Match pseudocode to code with loops and conditions**  
Students match a short pseudocode description to one of several code snippets that implement it.  
_Format:_ Pseudocode + 3 code options; MCQ. · _CSTA:_ MS‑ALG‑AF‑01.

---

## Grade 7 – Complex Algorithms, Simulation Traces, and Efficiency

Strands: **7‑A Trace simulations**, **7‑B Flowcharts for classic algorithms**, **7‑C Efficiency & bugs**

### 7‑A: Trace simulations

**T02.G7.01 – Trace a step‑by‑step simulation algorithm**  
Students trace code that simulates a process over several timesteps (e.g., a counter stepping up, an object moving with friction) and predict state after N steps.  
_Format:_ Code‑reading + table or MCQ; auto‑graded by predicted state. · _CSTA:_ MS‑ALG‑PS‑05.

**T02.G7.02 – Extend a simulation trace and predict future behavior**  
Students are shown a partially filled trace table for a simulation algorithm and must extend it a few rows to predict future behavior.  
_Format:_ Table completion; auto‑graded by continuation. · _CSTA:_ MS‑ALG‑PS‑05.

### 7‑B: Flowcharts for classic algorithms

**T02.G7.03 – Create a flowchart for linear search or “find max”**  
Students design a flowchart for a simple search algorithm (e.g., scan a list to find the largest value).  
_Format:_ Constructive flowchart; auto‑graded by correct loop and comparison logic. · _CSTA:_ MS‑ALG‑AF‑01.

**T02.G7.04 – Read a flowchart for a simple sort and trace one pass**  
Students read a flowchart for one pass of a simple sort (e.g., bubble sort) and trace how a short list changes after that pass.  
_Format:_ Flowchart + list; students show resulting list; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑01, MS‑ALG‑PS‑05.

### 7‑C: Efficiency & bugs

**T02.G7.05 – Count steps for two algorithms on small inputs**  
Students compare two algorithms that solve the same problem, counting actual steps for small input sizes and deciding which is more efficient for those inputs.  
_Format:_ Code/flowcharts + small inputs; numeric counts + MCQ. · _CSTA:_ MS‑ALG‑PS‑05.

**T02.G7.06 – Trace an algorithm to find a bug or edge case**  
Students trace an algorithm with a specific input where it fails (e.g., empty list, single element) and explain the failure in terms of a missed case or incorrect condition.  
_Format:_ Code‑reading + short answer or MCQ; auto‑graded by identified case/cause. · _CSTA:_ MS‑ALG‑PS‑05.

---

## Grade 8 – Pseudocode Design, Representation Quality, and Determinism

Strands: **8‑A Design & test pseudocode**, **8‑B Representation quality & human‑centered thinking**, **8‑C Deterministic vs probabilistic**

### 8‑A: Design & test pseudocode

**T02.G8.01 – Write pseudocode for a non‑trivial algorithm**  
Students write pseudocode for a moderately complex algorithm (e.g., check if a number is prime, find the median of 5 numbers) using clear structure, loops, and conditionals.  
_Format:_ Guided pseudocode editor; auto‑graded by structural and logical checks. · _CSTA:_ MS‑ALG‑AF‑02.

**T02.G8.02 – Trace your pseudocode with multiple test cases**  
Students are given pseudocode (their own or provided) and a set of test cases; they trace each case and record outputs, checking for correctness.  
_Format:_ Table of inputs/outputs; auto‑graded by predicted outputs. · _CSTA:_ MS‑ALG‑PS‑05.

### 8‑B: Representation quality & human‑centered thinking

**T02.G8.03 – Refactor an algorithm’s representation for clarity**  
Students are given an overly verbose or confusing flowchart/pseudocode and must simplify or restructure it while preserving behavior (e.g., merging repeated steps, improving names).  
_Format:_ Edit representation + short explanation; auto‑graded by structural patterns and key phrases. · _CSTA:_ MS‑ALG‑AF‑01.

**T02.G8.04 – Design a flowchart for a real‑world decision with user needs in mind**  
Students create a flowchart for a real‑world decision process (e.g., “How to choose a help resource online”) that is clear and easy to follow for a target user.  
_Format:_ Constructive flowchart + prompt about audience; auto‑graded for coverage of key cases and structure. · _CSTA:_ MS‑ALG‑HD‑03.

### 8‑C: Deterministic vs probabilistic

**T02.G8.05 – Trace and compare deterministic and probabilistic algorithms**  
Students trace two versions of an algorithm—one deterministic, one with randomness—and compare their outputs and when each type might be appropriate.  
_Format:_ Code/pseudocode pairs + tracing questions; auto‑graded by predicted outputs and selected use‑case reasons. · _CSTA:_ MS‑ALG‑AF‑02.

---

### Notes on Dependencies and Alignment

- K–2 T02 skills should depend primarily on T01 K–2 (everyday algorithms) and earlier skills within T02.  
- G3–5 T02 tracing skills should depend on the **Grade 3 gateway constructs** in T06–T09 (events, loops, conditionals, variables) plus corresponding T01 algorithm skills.  
- G6–8 T02 analysis skills should depend on earlier T02 representation/tracing skills and on relevant programming topics (T06–T13) but should **not** be prerequisites for core coding constructs themselves.  
- This design aligns with CSTA ALG‑AF and ALG‑PS progressions while keeping each skill small, auto‑gradable, and implementable on the CreatiCode playground.

