# T04 – Algorithm Patterns: K–8 Skill List (v2, IXL‑Style Microsteps)

Topic reference: `T04 Algorithm Patterns` in `domains_topics_overview.md`  
Domain: Algorithms & Design (D1) · Primary CSTA focus: ALG‑AF, ALG‑PS (with links to PRO‑PF, ALG‑HD, ALG‑IM)

This v2 version refines the original draft (`skills_T04_patterns.md`) into an **IXL‑style microstep design**:

- **Role of T04:** Focused on *identifying algorithmic patterns* (repetition, structure, behavior) and *reusing solutions* (templates, loops, custom blocks, idioms) across problems. T04 assumes that students can already describe everyday algorithms (T01), read/trace diagrams and code (T02), and break projects into tasks (T03), and then gives them a vocabulary of “standard solutions” they can spot and apply.  
- **Microsteps:** Each skill handles one narrow pattern role (spot pattern, extend, describe rule, recognize repeated code, replace repetition with loops/blocks, adapt templates, compare pattern choices) instead of bundling multiple constructs. Within a strand, IXL‑style microsteps move from “see a pattern” → “name it” → “use/modify it” → “compare/debug it,” with no big jumps.  
- **Uneven density:** Richer in **grades 3–6**, where loops, lists, custom blocks, and template reuse take off; lighter but still meaningful foundations in K–2 and higher‑order analysis and tradeoffs in 7–8.  
- **Implementability:** Designed for CreatiCode using picture‑based K–2 tasks, code snippets, starter templates, and small refactor or comparison exercises.

IDs follow `T04.G<grade>.<nn>`. v1 IDs are preserved conceptually; new microsteps use higher `<nn>` values.

---

## Grade K (PreK–K) – Visual Repeating Patterns

Strands: **K‑A Spot & extend patterns**, **K‑B Describe & fix**

### K‑A: Spot & extend patterns

**T04.GK.01 – Spot a simple repeating pattern**  
Students look at rows of pictures or tiles and pick the row that shows a clear repeating pattern (ABAB, AABB, ABCABC), distinguishing it from broken or random rows.  
_Format:_ MCQ visual rows; auto‑graded by correct row. · _CSTA:_ EK‑ALG‑AF‑01.

**T04.GK.02 – Extend a repeating pattern by one tile**

_Dependency:_
  * T04.GK.01: Spot a simple repeating pattern

Students see a short pattern (e.g., red, blue, red, blue, ?) and choose or drag the next picture.  
_Format:_ Drag‑drop or MCQ; auto‑graded. · _CSTA:_ EK‑ALG‑AF‑01.

### K‑B: Describe & fix

**T04.GK.03 – Describe a pattern using simple words**

_Dependency:_
  * T01.GK.03: Find the first and last pictures

Students see a pattern and choose the matching description (e.g., “circle, square, circle, square”).  
_Format:_ MCQ with picture‑supported phrases; auto‑graded. · _CSTA:_ EK‑ALG‑AF‑01.

**T04.GK.04 – Fix a broken pattern by replacing one tile**

_Dependency:_
  * T04.GK.02: Extend a repeating pattern by one tile

Students see a pattern row with one wrong picture and replace just that tile to restore the repeating pattern.  
_Format:_ Click wrong tile → pick replacement; auto‑graded. · _CSTA:_ EK‑ALG‑AF‑01, EK‑ALG‑PS‑03.

---

## Grade 1 – From Picture Patterns to Repeated Instructions

Strands: **1‑A Picture patterns to actions**, **1‑B Spot repetition in step sequences**

### 1‑A: Picture patterns to actions

**T04.G1.01 – Match a picture pattern to a movement pattern**

_Dependency:_
  * T04.GK.02: Extend a repeating pattern by one tile

Students match a picture pattern (e.g., hop, clap, hop, clap) to a character’s actions in a short story or animation.  
_Format:_ MCQ or drag matching; auto‑graded. · _CSTA:_ E1‑ALG‑AF‑01.

**T04.G1.02 – Plan a short repeating animation pattern**

_Dependency:_
  * T04.G1.01: Match a picture pattern to a movement pattern

Students choose a 3‑panel picture pattern (e.g., spin, jump, spin) and arrange action cards to create a matching “dance” plan.  
_Format:_ Drag action cards; auto‑graded by pattern unit. · _CSTA:_ E1‑ALG‑AF‑01, E1‑ALG‑PS‑03.

### 1‑B: Spot repetition in step sequences

**T04.G1.03 – Find repeated steps in an instruction list**

_Dependency:_
  * T01.GK.07: Find the pattern that repeats

Students examine a short list of picture‑based steps (or action cards laid out in a row) and click or highlight the part that repeats (e.g., three identical “move forward” cards in a row).  
_Format:_ Highlight region in the step list; auto‑graded by range. · _CSTA:_ E1‑ALG‑AF‑01, E1‑ALG‑PS‑03.

**T04.G1.04 – Match a repeated picture story to a repeated step list**

_Dependency:_
  * T04.G1.03: Find repeated steps in an instruction list

Students match a picture story showing repeated actions with a simple list of steps that repeats the same action sequence.  
_Format:_ Picture story + 2–3 step lists; MCQ. · _CSTA:_ E1‑ALG‑AF‑01.

---

## Grade 2 – Repetition as a Strategy

Strands: **2‑A Recognize repeating structure**, **2‑B Compare repeated vs non‑repeated solutions**

### 2‑A: Recognize repeating structure

**T04.G2.01 – Identify the repeating unit in a longer pattern**

_Dependency:_
  * T04.G1.03: Find repeated steps in an instruction list

Students see a longer pattern like ABCABCABC and choose the “unit” that repeats.  
_Format:_ MCQ; auto‑graded. · _CSTA:_ E2‑ALG‑AF‑01.

**T04.G2.02 – Spot repeated step sequences in everyday algorithms**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T01.GK.07: Find the pattern that repeats

Students read or see an everyday algorithm (e.g., “brush, rinse” repeated three times) and highlight the part that repeats, focusing on the *pattern unit* rather than the full routine.  
_Format:_ Highlight text/cards; auto‑graded. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

### 2‑B: Compare repeated vs non‑repeated solutions

**T04.G2.03 – Compare a long explicit description vs a compressed “repeat” description**

_Dependency:_
  * T01.G2.02: Use "repeat" to make directions shorter

Students choose which of two algorithm descriptions is shorter/clearer: one with all steps written out vs one with “repeat 3 times,” treating both as *generic pattern descriptions* rather than complete plans for a specific task.  
_Format:_ MCQ with two descriptions; auto‑graded. · _CSTA:_ E2‑ALG‑AF‑01, E2‑ALG‑PS‑03.

**T04.G2.04 – Replace repeated steps with a “repeat ___ times” phrase**

_Dependency:_
  * T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
  * T01.GK.07: Find the pattern that repeats

Students rewrite a long description by choosing a version that uses “repeat ___ times” correctly, focusing on the *mechanics* of compression that will later be applied to whole routines in T01.  
_Format:_ MCQ or drag phrase; auto‑graded. · _CSTA:_ E2‑ALG‑AF‑01.

---

## Grade 3 – First Coding Patterns (Loops & Templates)

Strands: **3‑A Loop patterns**, **3‑B Starter templates & reuse**, **3‑C Debugging simple patterns**

### 3‑A: Loop patterns

**T04.G3.01 – Identify where a loop could replace repeated blocks**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.G2.02: Spot repeated step sequences in everyday algorithms
  * T07.G3.01: Use a counted repeat loop

Students see a small, context‑free script with copy‑pasted blocks and choose which part can be replaced by a loop, focusing on the *loop pattern shape* without yet worrying about a particular game or project.  
_Format:_ Highlight repeated segment; auto‑graded. · _CSTA:_ E3‑ALG‑AF‑01, E3‑PRO‑PF‑01.

**T04.G3.02 – Match a “repeat N” loop to repeated behavior**

_Dependency:_
  * T04.G3.01: Identify where a loop could replace repeated blocks
  * T07.G3.01: Use a counted repeat loop
  * T04.G2.03: Compare a long explicit description vs a compressed “repeat” description

Students match a `repeat N` loop script (e.g., `repeat 4 { move 10 }`) to an animation or path with the same repeated behavior, treating it as a generic “N‑times pattern” that will later appear inside real T01/T07 projects.  
_Format:_ Code + 2–3 behaviors; MCQ. · _CSTA:_ E3‑ALG‑AF‑01.

### 3‑B: Starter templates & reuse

**T04.G3.03 – Recognize a simple project template**

_Dependency:_
  * T04.G3.02: Match a “repeat N” loop to repeated behavior
  * T07.G3.02: Trace a script with a simple loop
  * T03.G3.02: Group features into “must‑have” vs “nice‑to‑have”

Students inspect two tiny projects and identify which is written as a clearly reusable template (e.g., with placeholders or comments).  
_Format:_ Side‑by‑side comparison; MCQ. · _CSTA:_ E3‑ALG‑PS‑03.

**T04.G3.04 – Customize a template by changing repeated elements**

_Dependency:_
  * T04.G3.03: Recognize a simple project template
  * T07.G3.02: Trace a script with a simple loop
  * T09.G3.01: Create and use a numeric variable for score or count

Students modify a simple template (e.g., pattern of colors or sounds in a loop) by adjusting blocks while preserving the structure.  
_Format:_ Coding in CreatiCode starter; auto‑graded by behavior pattern. · _CSTA:_ E3‑PRO‑PF‑01.

### 3‑C: Debugging simple patterns

**T04.G3.05 – Fix a loop that repeats too many or too few times**

_Dependency:_
  * T04.G3.04: Customize a template by changing repeated elements
  * T08.G3.01: Use a simple if in a script
  * T07.G3.02: Trace a script with a simple loop

Students adjust the `repeat` count to match a target pattern or path in a small, self‑contained example, so they can later use the same adjustment skill inside larger T01 algorithms.  
_Format:_ Change loop count; auto‑graded via simulation. · _CSTA:_ E3‑ALG‑PS‑03.

**T04.G3.06 – Fix a pattern where one step is wrong**

_Dependency:_
  * T04.G3.05: Fix a loop that repeats too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T07.G3.03: Build a forever loop for simple animation

Students repair a loop or repeated sequence where one action is different from the rest.  
_Format:_ Edit one block; auto‑graded by final behavior. · _CSTA:_ E3‑ALG‑PS‑03.

---

## Grade 4 – Richer Patterns: Nested Repetition and Conditionals

Strands: **4‑A Patterned loops & grids**, **4‑B Conditional patterns**, **4‑C Recognize reusable solutions**

### 4‑A: Patterned loops & grids

**T04.G4.01 – Trace a loop that creates a visual pattern**

_Dependency:_
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence

Students trace code that draws shapes or patterns and match it to one of several images.  
_Format:_ Code‑reading + image MCQ; auto‑graded. · _CSTA:_ E4‑ALG‑AF‑01.

**T04.G4.02 – Identify nested pattern structure (outer vs inner loop)**

_Dependency:_
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T07.G3.01: Use a counted repeat loop

Students see nested loops and choose which part controls rows vs columns in a grid pattern.  
_Format:_ Highlight outer/inner loop roles; auto‑graded. · _CSTA:_ E4‑ALG‑AF‑01, E4‑ALG‑PS‑03.

### 4‑B: Conditional patterns

**T04.G4.03 – Recognize “if” patterns that handle special cases**

_Dependency:_
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T08.G3.01: Use a simple if in a script

Students identify code patterns like “bounce on edge” or “wrap around screen” as standard conditional patterns.  
_Format:_ Match behavior description to code snippet; auto‑graded. · _CSTA:_ E4‑ALG‑AF‑01.

**T04.G4.04 – Match multiple code snippets that share the same pattern**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile

Students group snippets that all implement the same conditional pattern (e.g., “check boundary then adjust position”).  
_Format:_ Grouping exercise; auto‑graded by group membership. · _CSTA:_ E4‑ALG‑PS‑03.

### 4‑C: Recognize reusable solutions

**T04.G4.05 – Identify when a known pattern can solve a new problem**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T09.G3.01: Create and use a numeric variable for score or count

Students see a new problem description and choose which known pattern (e.g., loop over list, counter pattern) would help.  
_Format:_ MCQ; auto‑graded. · _CSTA:_ E4‑ALG‑PS‑03.

**T04.G4.06 – Explain how reusing a pattern saves time**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile

Students answer conceptual questions about why reusing patterns/templates is beneficial in coding.  
_Format:_ MCQ + short explanation; auto‑graded by key phrases. · _CSTA:_ E4‑ALG‑IM‑04.

---

## Grade 5 – Canonical Patterns: Counters, Accumulators, Search

Strands: **5‑A Counter & accumulator patterns**, **5‑B Search & filter patterns**, **5‑C Compare implementations**

### 5‑A: Counter & accumulator patterns

**T04.G5.01 – Recognize a counter update pattern**

_Dependency:_
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count

Students identify code where a variable counts events (`set count to 0; change count by 1`) across different contexts.  
_Format:_ Code classification; auto‑graded. · _CSTA:_ E5‑ALG‑AF‑01.

**T04.G5.02 – Recognize an accumulator (sum/concatenate) pattern**

_Dependency:_
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count

Students identify code where a variable accumulates totals or builds strings.  
_Format:_ Code classification; auto‑graded. · _CSTA:_ E5‑ALG‑AF‑01, E5‑ALG‑PS‑03.

### 5‑B: Search & filter patterns

**T04.G5.03 – Recognize a linear search pattern**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T08.G3.01: Use a simple if in a script

Students identify the “look at each item and compare” pattern in code that searches for a match.  
_Format:_ Code‑reading; MCQ. · _CSTA:_ E5‑ALG‑PS‑03.

**T04.G5.04 – Recognize a filter‑and‑collect pattern**

_Dependency:_
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script

Students identify code that loops, tests a condition, and adds matching items to a list.  
_Format:_ Code classification; auto‑graded. · _CSTA:_ E5‑ALG‑PS‑03.

### 5‑C: Compare implementations

**T04.G5.05 – Compare solutions that use a pattern vs those that don’t**

_Dependency:_
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count

Students compare two snippets solving the same task, one using a standard pattern (loop + counter) and one using ad‑hoc code, and choose which is better and why.  
_Format:_ MCQ + explanation; auto‑graded by key reasoning. · _CSTA:_ E5‑ALG‑PS‑03, E5‑ALG‑IM‑04.

---

## Grade 6 – Reusable Blocks, Templates, and Efficiency

Strands: **6‑A Recognize common algorithm patterns**, **6‑B Refactor to reusable blocks**, **6‑C Template adaptation & efficiency**

### 6‑A: Recognize common algorithm patterns

**T04.G6.01 – Group snippets by underlying algorithm pattern**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T09.G3.01: Create and use a numeric variable for score or count

Students group code snippets that all implement the same pattern (counter, accumulator, search, filter).  
_Format:_ Drag snippets into labeled groups; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑02, MS‑ALG‑PS‑05.

**T04.G6.02 – Spot pattern variants that look different but behave the same**

_Dependency:_
  * T04.G1.01: Match a picture pattern to a movement pattern
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile

Students identify snippets that are structurally different but implement the same pattern (e.g., counting with `repeat` vs `for each`).  
_Format:_ MCQ/grouping; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑02.

### 6‑B: Refactor to reusable blocks

**T04.G6.03 – Turn repeated code into a custom block**

_Dependency:_
  * T01.G3.01: Complete a simple script with missing blocks
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T07.G3.01: Use a counted repeat loop

Students refactor repeated sequences into a custom block and replace occurrences with calls.  
_Format:_ Coding refactor challenge; auto‑graded by checking calls vs repetition. · _CSTA:_ MS‑PRO‑PF‑01, MS‑ALG‑PS‑05.

**T04.G6.04 – Add parameters to make a custom block more reusable**

_Dependency:_
  * T01.G3.01: Complete a simple script with missing blocks
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T08.G3.01: Use a simple if in a script

Students modify a custom block to accept parameters (e.g., number of steps, color) and adjust calls accordingly.  
_Format:_ Coding + small tests; auto‑graded by parameter use. · _CSTA:_ MS‑PRO‑PF‑01.

### 6‑C: Template adaptation & efficiency

**T04.G6.05 – Analyze a template project and identify customization points**

_Dependency:_
  * T04.G1.01: Match a picture pattern to a movement pattern
  * T04.G1.02: Plan a short repeating animation pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile

Students inspect a template (quiz, platformer, etc.) and mark which parts are meant to change vs stay the same.  
_Format:_ Highlight or label code areas; auto‑graded. · _CSTA:_ MS‑ALG‑PS‑05.

**T04.G6.06 – Compare two pattern‑based solutions for efficiency and clarity**

_Dependency:_
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script

Students compare two different pattern choices (e.g., nested loops vs one loop + formula) and select which is better for given constraints.  
_Format:_ MCQ + explanation; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑02, MS‑ALG‑PS‑05.

---

## Grade 7 – Pattern Composition and Optimization

Strands: **7‑A Patterns in simulations and games**, **7‑B Compose patterns**, **7‑C Optimize by removing redundancy**

### 7‑A: Patterns in simulations and games

**T04.G7.01 – Identify the main loop patterns in a simulation or game**

_Dependency:_
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script

Students analyze a game/simulation and identify loops like “update each frame,” “process each object,” “check each pair.”  
_Format:_ Code analysis MCQ; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑02, MS‑ALG‑PS‑06.

**T04.G7.02 – Identify data structure patterns (lists, grids) in use**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T08.G3.01: Use a simple if in a script

Students recognize when code uses a list or grid pattern (e.g., iterating over a list of enemies or cells).  
_Format:_ Code‑reading; MCQ. · _CSTA:_ MS‑ALG‑PS‑06.

### 7‑B: Compose patterns

**T04.G7.03 – Design a solution by combining two known patterns**

_Dependency:_
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count

Students design or outline code that combines, for example, a filter pattern + accumulator pattern to solve a task.  
_Format:_ Structured outline or code; auto‑graded by presence of both patterns. · _CSTA:_ MS‑ALG‑PS‑05, MS‑ALG‑PS‑06.

**T04.G7.04 – Trace a composite pattern and explain each part’s role**

_Dependency:_
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count

Students trace code that uses multiple patterns together and annotate what each pattern is doing.  
_Format:_ Code annotation; auto‑graded by keywords. · _CSTA:_ MS‑ALG‑AF‑02.

### 7‑C: Optimize by removing redundancy

**T04.G7.05 – Simplify code by merging repeated patterns**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T07.G3.01: Use a counted repeat loop

Students refactor code that has repeated pattern blocks into a more compact form (e.g., use a function applied twice).  
_Format:_ Coding refactor; auto‑graded by structure and behavior. · _CSTA:_ MS‑ALG‑PS‑05.

**T04.G7.06 – Compare pattern‑based implementations for maintainability**

_Dependency:_
  * T04.G1.01: Match a picture pattern to a movement pattern
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile

Students compare two implementations and decide which will be easier to modify later, explaining in terms of patterns and reuse.  
_Format:_ MCQ + explanation; auto‑graded. · _CSTA:_ MS‑ALG‑PS‑05, MS‑ALG‑IM‑04.

---

## Grade 8 – Idioms, Libraries, and Pattern Literacy

Strands: **8‑A Code idioms & libraries**, **8‑B Evaluate and choose patterns**, **8‑C Document and communicate patterns**

### 8‑A: Code idioms & libraries

**T04.G8.01 – Recognize common code idioms in a library**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count

Students inspect a small library of utility blocks and identify familiar patterns (e.g., clamp value, random choice, state machine tick).  
_Format:_ Code‑reading and classification; auto‑graded. · _CSTA:_ MS‑ALG‑AF‑02.

**T04.G8.02 – Adapt a library function to a new context**

_Dependency:_
  * T04.G1.01: Match a picture pattern to a movement pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count

Students take an existing utility block and adapt parameters or logic to a new but related use.  
_Format:_ Coding adaptation; auto‑graded by tests. · _CSTA:_ MS‑ALG‑PS‑05.

### 8‑B: Evaluate and choose patterns

**T04.G8.03 – Choose between alternative patterns for a problem**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop

Students evaluate several candidate approaches (e.g., polling vs event‑driven; nested loops vs index lists) and choose which pattern fits given constraints.  
_Format:_ Scenario + MCQ + justification; auto‑graded. · _CSTA:_ MS‑ALG‑PS‑05, MS‑ALG‑IM‑04.

**T04.G8.04 – Analyze tradeoffs in using a standard pattern vs custom code**

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count

Students reason about pros/cons of relying on a standard pattern or library vs writing one‑off code.  
_Format:_ MCQ + explanation; auto‑graded by key ideas. · _CSTA:_ MS‑ALG‑IM‑04.

### 8‑C: Document and communicate patterns

**T04.G8.05 – Write a short “pattern card” describing a reusable solution**

_Dependency:_
  * T04.G1.01: Match a picture pattern to a movement pattern
  * T04.G1.02: Plan a short repeating animation pattern
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile

Students document a pattern in a standard format: name, problem it solves, solution sketch, and when to use it.  
_Format:_ Template completion; auto‑graded by sections. · _CSTA:_ MS‑ALG‑HD‑03, MS‑ALG‑IM‑04.

**T04.G8.06 – Explain to a peer how to reuse a pattern in their project**

_Dependency:_
  * T04.G1.01: Match a picture pattern to a movement pattern
  * T04.G1.02: Plan a short repeating animation pattern
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T04.GK.03: Describe a pattern using simple words
  * T04.GK.04: Fix a broken pattern by replacing one tile

Students draft brief guidance (written or in‑app notes) on how someone else can use a particular pattern.  
_Format:_ Short written guidance; auto‑graded via key phrases. · _CSTA:_ MS‑ALG‑HD‑03.

---

### Notes on Dependencies and Alignment

- K–2: T04 builds on T01 (everyday sequences) and T02 K–2 (basic sequence diagrams) by focusing on *repetition as a recognizable structure* (picture patterns, repeated actions) that later connects to loops. Early T04 skills are small pattern‑spotting microsteps, not new planning or representation work.  
- G3–5: T04 patterns are closely tied to loops, conditionals, variables, and lists (T06–T10); dependencies should point to the relevant construct topics plus earlier T04 pattern recognitions. Within a grade, strands move in small steps from spotting repetition in code → mapping to `repeat`/counter/search patterns → applying and comparing those patterns in simple problems. Canonical counter/accumulator/search/filter patterns in Grade 5 should be treated as gateway skills for later data (T25–T27) and AI topics (T21–T24).  
- G6–8: T04 emphasizes algorithmic patterns, reuse, and efficiency across projects; skills depend on prior programming topics, T02 diagram/tracing fluency, and T03 decomposition habits, but should not gate access to core constructs. They help students recognize, compose, and optimize common patterns rather than learn constructs from scratch. Pattern‑comparison and optimization skills can be tagged to CSTA efficiency/impacts standards and, when used in AI contexts, to AI4K12 ethical design and impacts categories.  
- This design aligns with CSTA ALG‑AF/ALG‑PS and ALG‑IM expectations while making each step small, auto‑gradable, and CreatiCode‑friendly and keeping roles of T01 (everyday algorithms), T02 (algorithm diagrams & tracing), T03 (planning/decomposition), and T04 (patterns & reusable solutions) complementary with no major duplication.
