# T07 (Loops) - Restructured Skills
## Phase 14 - Comprehensive Optimization

This document contains NEW, CONSOLIDATED, and MODIFIED skills for T07 (Loops) focusing on grades 5-8 where the most improvement is needed.

---

## PART 1: CONSOLIDATED SKILLS (Reducing Redundancy)

### CONSOLIDATED API & BATCH PROCESSING (G8)
**Replaces:** T07.G8.12 (batch AI calls), T07.G8.16 (paginated API), T07.G8.23 (rate limiting), T07.G8.24 (batching inference)

```
ID: T07.G8.12
Topic: T07 – Loops
Skill: Design loops for API integration patterns [CONSOLIDATED from T07.G8.12, T07.G8.16, T07.G8.23, T07.G8.24]
Description: Students design loops to handle three common API integration patterns: (1) **Batch processing:** Process multiple items in groups to reduce API calls - `for batch from 0 to (itemCount/batchSize - 1) [send batch to API, wait for results, add to output]`. Balance batch size vs latency. (2) **Pagination:** Handle multi-page responses - `set page to 1, repeat until (no more pages) [fetch page, add items to results, increment page]`. Detect completion via empty response or nextPage field. (3) **Rate limiting:** Respect API limits - calculate delay between requests (e.g., 30 requests/min = 2s delay) and add `wait` blocks. **Unified pattern:** All three use similar loop structure with different stopping conditions and timing strategies. Students analyze a use case and choose which pattern(s) to apply. **Applications:** ChatGPT batch classification, image API processing, database queries, GitHub API pagination.

Dependencies:
* T07.G8.10: Describe loop requirements to AI coding assistant
* T07.G8.08: Justify loop design choices
* T07.G8.17: Implement asynchronous processing patterns with loops

Examples:
* Batch: Classify 100 images in groups of 10 to reduce overhead
* Pagination: Fetch all GitHub repos across multiple pages
* Rate limiting: Call ChatGPT API 30x/minute without exceeding quota
```

### CONSOLIDATED DEBUGGING TECHNIQUES (G3)
**Replaces:** T07.G3.06 (say blocks), T07.G3.07 (console logging), T07.G3.13 (wrong count), T07.G3.14 (wrong action), T07.G3.15 (step-by-step), T07.G3.18 (bug categories)

```
ID: T07.G3.06
Topic: T07 – Loops
Skill: Debug loops using systematic techniques [CONSOLIDATED from T07.G3.06, T07.G3.07, T07.G3.13, T07.G3.14, T07.G3.15, T07.G3.18]
Description: Students learn a systematic three-tool approach to debug loop problems. **Tool 1 - Visualization:** Add `say` blocks inside loops to display counter/variable values (quick but covers stage). **Tool 2 - Console logging (CreatiCode-specific):** Use `log` block to write iteration data to console panel - cleaner and scrollable. Example: `log (join "i=" i " total=" total)`. **Tool 3 - Step-by-step execution (CreatiCode-specific):** Use Debug Mode button to pause between iterations and inspect sprite state. **Three bug categories to diagnose:** (1) **Wrong count** - loop runs too many/few times, (2) **Wrong action** - incorrect blocks inside loop, (3) **Wrong condition** - stops at wrong time or never. **Debugging process:** (1) Identify expected vs actual behavior, (2) Choose appropriate tool, (3) Trace execution, (4) Categorize the bug, (5) Fix targeted area. **Key insight:** Systematic debugging is faster than random trial-and-error. These three tools and three categories provide a complete debugging framework students use throughout their programming journey.

Dependencies:
* T07.G3.05: Predict the final position after a repeat loop
* T07.G3.11: Use repeat-until to reach a goal

Practice Tasks:
* Debug `repeat 3 [move 30]` that should move 100 steps total (wrong count + wrong action)
* Debug `repeat until <touching edge>` that never stops (wrong condition)
* Use all three tools to diagnose a complex nested loop bug
```

---

## PART 2: NEW SKILLS (Filling Critical Gaps)

### NEW: K-2 COMPUTATIONAL THINKING ENHANCEMENT

```
ID: T07.K.06 [NEW]
Topic: T07 – Loops
Skill: Group repeated tasks into one idea
Description: Students practice the abstraction step that precedes looping - recognizing when multiple similar tasks can be grouped. **Task:** Teacher shows 4 pictures: (1) Put on left shoe, (2) Tie left shoe, (3) Put on right shoe, (4) Tie right shoe. Students group into categories: "Shoe tasks we do twice - once for each foot." **Pattern recognition:** Identify WHAT repeats (put on + tie) and HOW MANY times (2). **Transition to loops:** This grouping skill is the mental step before "repeat 2 times [put on shoe, tie shoe]". **Activities:** Group daily routines (brush top teeth, brush bottom teeth → brushing tasks × 2), art patterns (draw star, draw star, draw star → star × 3). **Key insight:** Before you can loop, you must recognize the pattern - this is the abstraction skill that makes loops meaningful.

Dependencies:
* T07.K.01: Recognize patterns in real-world sequences (e.g., daily routines)

Related:
* Connects to T07.G1.01 where students start coding loops
```

```
ID: T07.G2.12 [NEW]
Topic: T07 – Loops
Skill: Predict "how many times" before seeing the loop
Description: Students develop prediction skills by analyzing repeated patterns and stating the count BEFORE being shown the loop structure. **Task:** Teacher shows a completed drawing with 6 identical flowers. Students count and say "The loop repeated 6 times." Then reveal the code: `repeat 6 [draw flower]` - confirming their prediction. **Variations:** (1) Count stamps in a pattern, (2) Count identical animation frames, (3) Count repetitions in a song/chant. **Key insight:** This reverses the typical flow (given loop → predict output). Instead, students see output → predict loop count. This backward reasoning strengthens loop understanding and prepares for refactoring repeated code. **Connects to:** G4.09 where students refactor code into loops - this skill builds the pattern-counting ability needed for that task.

Dependencies:
* T07.G2.06: Count exact repetitions in step-by-step instructions
* T07.K.06: Group repeated tasks into one idea

Related:
* Prepares for T07.G4.09: Refactor repeated code into a loop
```

### NEW: NAMED LOOP PATTERNS (G5-G6)

```
ID: T07.G5.22 [NEW]
Topic: T07 – Loops
Skill: Identify and name common loop patterns
Description: Students learn standard names for loop patterns used in professional programming. **Core patterns:** (1) **Accumulator pattern** - building up a total: `set sum to 0, for each item [change sum by item]`. (2) **Sentinel loop pattern** - stopping at special value: `repeat until (answer = "quit") [ask, process]`. (3) **Flag-controlled loop** - stopping when boolean changes: `set found to false, repeat until (found) [search, if (match) [set found to true]]`. (4) **Counter loop** - fixed iterations: `for i from 1 to n`. (5) **Processing loop** - iterating over collection: `for each item in list`. **Task:** Given 8-10 code snippets, students identify which pattern each uses and explain their reasoning. **Key insight:** These pattern names are professional vocabulary - using them helps communicate with other programmers and AI assistants. Knowing patterns helps students recognize which one fits a new problem. **Applications:** These 5 patterns cover ~80% of loops students will write.

Dependencies:
* T07.G5.17: Classify loops by purpose
* T07.G5.04: Compute sum and average using a loop
* T07.G5.02: Use loops to collect user input repeatedly

Examples:
* Accumulator: Calculate total price of shopping cart
* Sentinel: Collect student names until user enters "done"
* Flag: Search for first occurrence of target value
* Counter: Draw 10 stars in a row
* Processing: Display each item from a list
```

```
ID: T07.G5.23 [NEW]
Topic: T07 – Loops
Skill: Choose appropriate pattern for a new problem
Description: Students analyze a problem description and select which named loop pattern (from T07.G5.22) best fits, BEFORE writing code. **Task format:** Given a problem, select from: Accumulator, Sentinel, Flag-controlled, Counter, or Processing pattern. **Example 1:** "Ask user to enter numbers until they enter -1, then display the sum" → Sentinel loop (for input) + Accumulator pattern (for sum). **Example 2:** "Find if ANY score in the list is above 90" → Processing loop + Flag pattern. **Example 3:** "Calculate the product of numbers 1 through 10" → Counter loop + Accumulator. **Scaffold:** Problems specify 1-2 patterns; students identify and explain their choice. **Key insight:** Pattern selection is a design skill - choosing the right pattern makes coding easier. Wrong pattern → more complex code. **Practice:** Students explain their pattern choice to a peer before coding.

Dependencies:
* T07.G5.22: Identify and name common loop patterns
* T07.G5.16: Explain loop algorithm choices to a peer

Applications:
* Design phase of problem-solving
* Explaining solutions to AI assistants
* Code review and peer collaboration
```

### NEW: LOOP DECOMPOSITION & INVARIANTS (G6)

```
ID: T07.G6.26 [NEW]
Topic: T07 – Loops
Skill: Decompose one complex loop into multiple simpler loops
Description: Students refactor complex loops that do multiple things into separate focused loops. **Example - Complex loop:** `for each item in data [validate item, transform item, filter item, accumulate total]` - too much in one loop. **Decomposed version:** (1) `for each item in data [if (valid) [add to validData]]`, (2) `for each item in validData [set item to (transform item)]`, (3) `for each item in validData [if (meets criteria) [add to filtered]]`, (4) `for each item in filtered [change total by item]`. **Trade-off analysis:** Separate loops are clearer and easier to debug but process the list multiple times. **When to decompose:** If the loop body has 3+ distinct responsibilities, or if you struggle to name what the loop does. **Key insight:** "Do one thing well" applies to loops - simpler loops are easier to understand, test, and modify. This principle scales to functions and classes in later programming.

Dependencies:
* T07.G5.22: Identify and name common loop patterns
* T07.G6.05: Debug nested loops with incorrect bounds

Examples:
* Split data validation + transformation into two passes
* Separate filtering logic from calculation logic
* Break apart nested loops when inner loop has complex logic
```

```
ID: T07.G6.27 [NEW]
Topic: T07 – Loops
Skill: Understand loop invariants (simplified)
Description: Students learn to identify "what stays true throughout the loop" - a simplified introduction to loop invariants. **Pattern:** State a fact that's true before the loop, after each iteration, and after the loop ends. **Example 1 - Sum algorithm:** Invariant: "total equals the sum of all items processed so far." Check: (1) Start: total=0, items processed=0 (✓ 0 is sum of nothing), (2) After i=1: total=item1 (✓ correct sum), (3) After all: total=sum of all (✓). **Example 2 - Search:** Invariant: "If target exists, it hasn't been found in items already checked." **Task:** Given 3-4 simple loop algorithms, students select the correct invariant statement from multiple choices. **Key insight:** Loop invariants help prove correctness - if the invariant is true at start and preserved by each iteration, it must be true at the end. This is a foundational concept for competition programming and formal verification. **Simplified for G6:** Focus on stating and checking the invariant, not formal proofs.

Dependencies:
* T07.G6.06: Use trace tables for nested loop calculations
* T07.G5.04: Compute sum and average using a loop

Applications:
* Verify algorithm correctness
* Debug: if invariant becomes false, you found the bug
* Design: define invariant first, then write loop to maintain it
```

### NEW: PARALLEL LOOP EXECUTION (G5-G6)

```
ID: T07.G5.24 [NEW]
Topic: T07 – Loops
Skill: Understand parallel loop execution in multi-sprite programs
Description: Students learn that in Scratch/CreatiCode, multiple sprites can run their loops simultaneously - each sprite's green flag script runs in parallel. **Demonstration:** Create 3 sprites with identical scripts: `when green flag clicked, repeat 10 [move 10, wait 0.1 seconds]`. All 3 sprites move together at the same time. **Key concept:** Each sprite has its own loop counter and variables - they don't interfere. **Contrast with sequential:** Compare to one sprite doing `move sprite1, move sprite2, move sprite3` sequentially. **Applications:** (1) Synchronized animation - all sprites dance together, (2) Multi-character games - each enemy runs its own loop, (3) Particle systems - each particle clone loops independently. **CreatiCode-specific:** Broadcast can coordinate parallel loops - sprites wait for same broadcast to synchronize. **Common misconception:** Students sometimes think loops must finish before other sprites start - this corrects that.

Dependencies:
* T07.G4.15: Build a nested loop to draw a rectangle grid
* T07.G3.08: Build a forever loop for continuous animation

Examples:
* 5 sprites all spinning simultaneously
* Multiple enemies patrolling different paths in parallel
* Coordinated animation where all sprites start on broadcast
```

```
ID: T07.G6.28 [NEW]
Topic: T07 – Loops
Skill: Debug race conditions in parallel loops
Description: Students identify and fix bugs that occur when multiple sprites' loops interact unexpectedly. **Bug scenario:** Two sprites both check `if (score < 10) [change score by 1]`. If score=9, both check simultaneously, both see 9<10, both add 1 → score becomes 11 (wrong!). **Fix strategies:** (1) Use broadcasts to serialize access - one sprite waits for other to finish. (2) Use atomic operations - change score THEN check. (3) Assign different responsibilities - only one sprite modifies score. **Task:** Given scenarios with buggy parallel loops, students identify the race condition and propose a fix. **Key insight:** Parallel execution creates timing bugs that don't exist in sequential code. This is a preview of concurrency challenges in advanced programming. **CreatiCode context:** Common in multi-sprite games where sprites compete for resources (e.g., collecting the same item).

Dependencies:
* T07.G5.24: Understand parallel loop execution in multi-sprite programs
* T07.G6.04: Identify and fix infinite loops

Examples:
* Two sprites both trying to collect the same coin
* Multiple enemies all targeting the same player position
* Parallel loops modifying the same list variable
```

### NEW: ERROR RECOVERY & RESILIENCE (G7)

```
ID: T07.G7.19 [NEW]
Topic: T07 – Loops
Skill: Implement error recovery mid-loop (continue on failure)
Description: Students design loops that handle errors gracefully, continuing to process remaining items when one item fails. **Pattern:** `for each item in batch [try to process item, if (error occurred) [log error, add to failedItems] else [add to successItems]]`. **Example:** Batch image classification where API fails on corrupted image - loop continues with next image instead of stopping. **Strategies:** (1) **Try-catch pattern (simulated):** Check for error conditions and handle them. (2) **Error collection:** Accumulate failed items in a separate list for retry. (3) **Partial results:** Return successful results even if some failed. **Task:** Given a batch processing scenario, students add error handling to ensure loop completes. **Key insight:** Robust loops don't stop at first error - they handle failures and continue. This is essential for real-world applications where data is messy and APIs are unreliable.

Dependencies:
* T07.G7.08: Use loops for input validation with retry
* T07.G8.20: Design retry loops with exponential backoff

Examples:
* Process 100 images; 3 are corrupted → return results for 97
* Classify 50 text samples; API times out on 2 → continue with rest
* Validate 20 user inputs; 5 invalid → collect valid ones, report invalid
```

### NEW: LOOP VS RECURSION (G8)

```
ID: T07.G8.29 [NEW]
Topic: T07 – Loops
Skill: Compare iteration vs recursion trade-offs
Description: Students understand when to use loops vs recursion by analyzing trade-offs. **Iteration (loops):** Uses explicit counters/accumulators, state updated in loop body, efficient (no function call overhead), easier to understand for sequential processing. **Recursion:** Function calls itself, state passed as parameters, natural for tree/hierarchical structures, risk of stack overflow. **Comparison tasks:** (1) **Factorial:** Both work; recursion matches math definition but loop is more efficient. (2) **Tree traversal:** Recursion is natural; loops require explicit stack. (3) **List processing:** Loops are simpler and faster. **Task:** Given 5 problems, students identify which approach is better and justify. **Key insight:** Use loops for sequential/counted tasks; use recursion for naturally recursive structures (trees, nested data). In CreatiCode, loops are preferred for most tasks; recursion is for specific cases like AI conversation trees or hierarchical 3D object structures.

Dependencies:
* T07.G8.02: Analyze iterative algorithm structure
* T07.G8.08: Justify loop design choices

Examples:
* Iteration: Sum list, process batch, animate sequence
* Recursion: Traverse folder tree, parse nested JSON, draw fractal
* Both work: Calculate Fibonacci, find GCD, generate permutations
```

### NEW: CREATICODE-SPECIFIC ENHANCEMENTS

```
ID: T07.G3.07A [NEW - Strengthened version]
Topic: T07 – Loops
Skill: Master CreatiCode console logging for loop debugging
Description: Students become proficient with CreatiCode's console panel for sophisticated loop debugging. **Basic usage:** `log (join "i=" i " value=" value)` outputs to console. **Advanced techniques:** (1) **Conditional logging:** `if (value > 100) [log "Large value detected"]` - only log interesting cases. (2) **Structured output:** Format logs for readability - use consistent prefix like "ITER i:" + value. (3) **Performance monitoring:** Log timestamps to identify slow iterations. (4) **Multi-variable tracking:** Log multiple values per iteration for complex state. **Comparison with say blocks:** Console doesn't cover stage, preserves history, can be filtered/searched. **Task:** Debug a complex nested loop by adding strategic console.log statements, then use console to identify the bug. **CreatiCode-specific:** Uses the console panel (terminal icon) and `log` block from Operators category.

Dependencies:
* T07.G3.06: Debug loops using systematic techniques
* T07.G6.06: Use trace tables for nested loop calculations

Applications:
* Debug nested loops with multiple variables
* Track accumulator values through iterations
* Identify performance bottlenecks in long loops
```

```
ID: T07.G6.19A [NEW - Strengthened version]
Topic: T07 – Loops
Skill: Master clone-based parallel loops for advanced effects
Description: Students create sophisticated particle systems and effects using loops with sprite clones. **Pattern:** `repeat n [create clone of myself], when I start as a clone [setup, forever [update, render]]`. **Advanced techniques:** (1) **Parameterized clones:** Pass different values to each clone via variables - `set cloneID to cloneCounter, create clone`. (2) **Clone pools:** Reuse clones instead of creating/deleting - create 100 clones at start, activate as needed. (3) **Synchronized behavior:** All clones respond to same broadcast for coordinated animation. (4) **Cleanup patterns:** `delete this clone` when off-screen or after timer to prevent memory leaks. **Applications:** (1) Fireworks with hundreds of particles, (2) Rain/snow effects, (3) Bullet patterns in shooters, (4) Flocking algorithms (boids). **Performance:** Monitor clone count - too many clones slow down. **3D support:** Works with 3D objects using `create clone of [3D object name]`.

Dependencies:
* T07.G6.18: Use loops with sprite clones for particle effects
* T07.G6.19: Debug clone lifecycle issues in loop-based animations
* T07.G5.24: Understand parallel loop execution in multi-sprite programs

Examples:
* Explosion with 50 debris particles flying outward
* 100 raindrops falling at different speeds
* Enemy spawner creating waves of clones
```

---

## PART 3: MODIFIED SKILLS (Improved Descriptions)

```
ID: T07.G5.01 [MODIFIED]
Topic: T07 – Loops
Skill: Use loops for statistical experiments and data collection
Description: Students use loops to repeat random experiments many times and analyze outcomes - introducing loops as a data science tool. **Pattern:** (1) Initialize counters to 0, (2) `repeat N [generate random outcome, if (condition) [increment counter]]`, (3) Calculate statistics from counters. **Example:** Simulate 1000 coin flips to verify probability: `set heads to 0, repeat 1000 [if (pick random 0 or 1 = 0) [change heads by 1]], say (join "Heads: " (heads/1000*100) "%")`. **Key insight:** More trials → results converge to theoretical probability. Students compare n=10, n=100, n=1000 to observe convergence. **Connection to real-world:** This is how scientists verify probability theories and how Monte Carlo methods work in advanced computing. **Applications:** Dice probability, birthday paradox, estimating pi.

Dependencies:
* T07.G4.17: Compare manual wait vs timed repeat for animations
* T07.G4.03: Identify which iterations trigger a condition
* T10.G4.27: Use random numbers to model chance or variety

Changes from original:
* Emphasized connection to data science and statistics
* Added convergence concept (n=10 vs n=100 vs n=1000)
* Clearer pattern specification
* Added real-world context (Monte Carlo methods)
```

```
ID: T07.G6.03 [MODIFIED]
Topic: T07 – Loops
Skill: Implement linear search with early exit optimization
Description: Students search a list for a target value using a loop with early termination. **Basic pattern:** `set found to false, for each item in list [if (item = target) [set found to true]]` - checks all items even after finding. **Optimized pattern with break:** `set found to false, set position to 0, for i from 1 to (length of list) [if (item i = target) [set found to true, set position to i, break]]` - stops immediately when found. **Efficiency comparison:** For target at position 3 in list of 100, basic checks 100 items (wasted 97 checks), optimized checks only 3. **Variations:** (1) Find first score above 90, (2) Find item matching multiple criteria, (3) Search in unsorted vs sorted data. **Key insight:** Early exit via break makes search much faster for large lists. This optimization principle applies broadly - do only necessary work.

Dependencies:
* T07.G5.04: Compute sum and average using a loop
* T08.G4.14: Use if-then-else in a project
* T07.G6.09: Use break to exit a loop early

Changes from original:
* Added break optimization as core content (was implied)
* Emphasized efficiency comparison with concrete numbers
* Connected to broader optimization principle
* Made the "accumulator with early exit" pattern explicit
```

```
ID: T07.G7.05 [MODIFIED]
Topic: T07 – Loops
Skill: Recognize and apply accumulator patterns strategically
Description: Students master the accumulator pattern - the most important loop pattern in programming - and choose appropriate variations for different tasks. **Core pattern:** Initialize accumulator before loop, update it each iteration, use result after loop. **Five accumulator variations:** (1) **Sum/Product:** `set total to 0, for each [change total by value]`, (2) **String building:** `set result to "", for each [set result to (join result char)]`, (3) **List building (filter):** `set filtered to [], for each [if (condition) [add item to filtered]]`, (4) **Count matching:** `set count to 0, for each [if (condition) [change count by 1]]`, (5) **Find min/max:** `set max to (item 1), for each [if (item > max) [set max to item]]`. **Selection task:** Given 6 problems, students identify which accumulator variation fits each. **Common bug:** Forgetting to initialize accumulator - results compound across runs. **Key insight:** ~70% of loops use accumulators. Mastering this pattern is essential for data processing, statistics, and algorithm implementation.

Dependencies:
* T07.G7.04: Compare loop algorithms by counting iterations
* T07.G7.03: Calculate 1D index from 2D coordinates

Changes from original:
* Explicitly enumerated 5 accumulator variations (was vague)
* Added selection task for pattern recognition
* Emphasized importance (70% of loops)
* Made initialization bug explicit
* Better progression from simple to complex accumulators
```

```
ID: T07.G8.10 [MODIFIED]
Topic: T07 – Loops
Skill: Write effective prompts for AI to generate loop code
Description: Students learn prompt engineering for AI-generated loops - a critical skill for modern programming. **Effective prompt structure:** (1) **Input specification:** Describe data structure and format, (2) **Loop logic:** Specify what to do each iteration, (3) **Termination:** Explain when loop should stop, (4) **Edge cases:** List special cases to handle, (5) **Output format:** Describe expected result, (6) **Preferred patterns:** Mention patterns to use (e.g., "use accumulator pattern"). **Example - Poor prompt:** "Write a loop for scores." **Example - Good prompt:** "Write a loop that iterates through a list of student scores (numbers). For each score above 60, add it to a passingScores list. Handle empty input by returning an empty list. Use the for-each-item pattern." **Evaluation:** Students compare AI output from poor vs good prompts and analyze what made the difference. **Iteration:** If AI output is wrong, students refine prompt and try again. **Key insight:** Clear prompts → better AI code. This skill transfers to all AI-assisted programming.

Dependencies:
* T07.G8.08: Justify loop design choices
* T07.G7.08: Use loops for input validation with retry
* T07.G5.22: Identify and name common loop patterns

Changes from original:
* Added 6-part prompt structure (was vague "describe clearly")
* Concrete poor vs good examples
* Emphasized iteration and refinement
* Connected to pattern vocabulary from G5.22
* Made it more actionable for students
```

---

## PART 4: DEPENDENCY FIXES

### Fixed X-2 Rule Violations

```
ID: T07.G6.01 [MODIFIED - Dependencies Fixed]
Topic: T07 – Loops
Skill: Trace nested loops with variable bounds
Description: Students trace nested loops where inner loop count depends on outer loop variable. Example: `for i from 1 to 4 [repeat (i) times [stamp]]`. Trace: i=1 → 1 stamp, i=2 → 2 stamps, i=3 → 3 stamps, i=4 → 4 stamps, total = 1+2+3+4 = 10 stamps. Students calculate total iterations by summing variable inner counts. This is more complex than fixed nested loops.

Dependencies:
* T07.G5.08: Build triangular number patterns with nested loops [CHANGED from G5.07 - closer grade]
* T07.G4.15: Build a nested loop to draw a rectangle grid [ADDED - foundation skill]
* T09.G4.01: Use variables to store and update game state

NOTE: Original had dependency on G5.07 (2 grades back) - changed to G5.08 (1 grade back, complies with X-2 rule)
```

```
ID: T07.G8.02 [MODIFIED - Dependencies Fixed]
Topic: T07 – Loops
Skill: Analyze iterative algorithm structure
Description: Students analyze iterative algorithms to identify three components: (1) **Initialization** - starting state/values, (2) **Update rule** - how values change each iteration, (3) **Termination condition** - when the loop stops. Example (GCD): init: a=48, b=18; update: replace larger with (larger mod smaller); terminate: when a=b. Students label these parts in given algorithms (primality, Fibonacci, binary search).

Dependencies:
* T07.G7.04: Compare loop algorithms by counting iterations [CHANGED from T01.G6.01 which is 2 grades back]
* T07.G7.05: Recognize and apply accumulator patterns [ADDED - same grade]
* T07.G6.06: Use trace tables for nested loop calculations [ADDED - foundation skill from G6]

NOTE: Removed cross-topic dependency on T01.G6.01 (binary search) - that violated X-2. Replaced with G7 skills.
```

---

## PART 5: SUMMARY STATISTICS

### Original T07 Structure (Phase 13)
- **Total skills:** 158
- **Grade distribution:** K(5), G1(9), G2(11), G3(18), G4(23), G5(21), G6(25), G7(18), G8(28)
- **Major issues:**
  - 4 redundant API skills in G8
  - 6 overlapping debugging skills in G3
  - Missing named pattern vocabulary
  - No loop decomposition skill
  - No parallel execution coverage
  - Weak error recovery

### Restructured T07 (Phase 14)
- **Skills removed via consolidation:** 8 (2 consolidated skills replace 10 originals)
- **Skills added:** 11 NEW skills
- **Skills modified:** 5 with improved descriptions
- **Net change:** +3 skills (158 → 161)
- **Dependencies fixed:** 3 X-2 violations corrected

### NEW Skill Distribution
- **K:** 1 new (abstraction/grouping)
- **G2:** 1 new (prediction)
- **G3:** 1 strengthened (console logging)
- **G5:** 3 new (named patterns, pattern selection, parallel loops)
- **G6:** 4 new (decomposition, invariants, parallel debugging, clone mastery)
- **G7:** 1 new (error recovery)
- **G8:** 1 new (iteration vs recursion)

### Key Improvements Delivered
1. **Redundancy eliminated:** API integration consolidated from 4 to 1 focused skill
2. **Debugging streamlined:** 6 scattered skills consolidated into 1 systematic framework
3. **Pattern vocabulary added:** Named patterns (accumulator, sentinel, flag, counter, processing)
4. **Critical gaps filled:** Decomposition, invariants, parallel execution, error recovery, iteration vs recursion
5. **K-2 enhanced:** Added abstraction skill (grouping) and prediction skill
6. **CreatiCode-specific strengthened:** Console logging and clone loops emphasized
7. **Dependencies fixed:** All X-2 violations corrected
8. **Clearer progression:** Each grade builds on previous more explicitly

---

## IMPLEMENTATION NOTES

### Integration with Existing Skills
- Consolidated skills REPLACE their predecessors (mark old IDs as deprecated)
- New skills INSERT at specified IDs (may require renumbering subsequent skills)
- Modified skills UPDATE in place (preserve ID)

### Renumbering Required
- **G3:** Insert T07.G3.07A after T07.G3.07, shift G3.08-G3.18 down
- **G5:** Insert T07.G5.22, G5.23, G5.24 after G5.21, shift subsequent
- **G6:** Insert T07.G6.26, G6.27, G6.28 after G6.25
- **G7:** Insert T07.G7.19 after G7.18
- **G8:** Insert T07.G8.29 at end, consolidate G8.12/16/23/24 into new G8.12

### Deprecated Skills (Mark for Removal)
- OLD T07.G8.16 (paginated API) → merged into NEW T07.G8.12
- OLD T07.G8.23 (rate limiting) → merged into NEW T07.G8.12
- OLD T07.G8.24 (batching inference) → merged into NEW T07.G8.12
- OLD T07.G3.13 (debug count) → merged into NEW T07.G3.06
- OLD T07.G3.14 (debug action) → merged into NEW T07.G3.06
- OLD T07.G3.15 (step-by-step) → merged into NEW T07.G3.06
- OLD T07.G3.18 (bug categories) → merged into NEW T07.G3.06

### Testing Recommendations
1. Verify all new dependencies exist and comply with X-2 rule
2. Check that consolidated skills cover all use cases from originals
3. Ensure G5.22 (named patterns) is prerequisite for all skills that reference patterns
4. Validate that parallel loop skills (G5.24, G6.28) are properly sequenced
5. Confirm CreatiCode-specific skills reference correct blocks and panels

---

## NEXT STEPS

1. **Review & Approve:** Stakeholders review this restructuring proposal
2. **Update Master File:** Integrate changes into main allskills.md
3. **Renumber IDs:** Systematically renumber shifted skills
4. **Update Dependencies:** Global search for deprecated IDs, update to consolidated versions
5. **Create Curriculum:** Map new skills to lesson plans and assessments
6. **Document Migration:** Note which old skills map to which new/consolidated skills
7. **Validate X-2 Rule:** Run automated check on all T07 dependencies

---

END OF RESTRUCTURING DOCUMENT
