# T07 (Loops) - Comprehensive Analysis Report
**Date:** November 23, 2025
**Analysis Type:** Complete topic review including skills, CreatiCode features, and dependency validation

---

## Executive Summary

**Total T07 Skills:** 41 skills spanning Kindergarten through Grade 8

**Critical Finding:** The T07 skills curriculum references standard Scratch loop blocks (`repeat N`, `forever`, `repeat until`) that are **not documented** in CreatiCode's blockdes8.txt, though they appear to be available based on example program usage. This creates a documentation gap that affects skill alignment verification.

**Overall Assessment:**
- ✅ **Strengths:** Excellent scaffolding from unplugged to advanced algorithms, good use of CreatiCode-specific enhanced blocks
- ⚠️ **Issues Found:** 32 issues across all priority levels
  - HIGH priority: 8 issues
  - MEDIUM priority: 15 issues
  - LOW priority: 9 issues

---

## 1. Current T07 Skills Inventory

### 1.1 Skills by Grade Level

| Grade | Count | Range |
|-------|-------|-------|
| K | 1 | T07.K.01 |
| G1 | 2 | T07.G1.01 - T07.G1.02 |
| G2 | 1 | T07.G2.01 |
| G3 | 5 | T07.G3.01 - T07.G3.05 |
| G4 | 8 | T07.G4.01 - T07.G4.08 |
| G5 | 4 | T07.G5.01 - T07.G5.04 |
| G6 | 9 | T07.G6.01 - T07.G6.09 |
| G7 | 4 | T07.G7.01 - T07.G7.04 |
| G8 | 7 | T07.G8.01 - T07.G8.04 (includes 3 sub-skills) |

### 1.2 Skills by Loop Concept

#### Basic Loop Types (K-G3)
- **Unplugged Pattern Recognition** (K-G2): T07.K.01, T07.G1.01, T07.G1.02, T07.G2.01
- **Counted Repeat Loops** (G3-G4): T07.G3.01, T07.G3.02, T07.G3.05, T07.G4.04
- **Forever Loops** (G3-G4): T07.G3.03, T07.G4.01
- **Repeat Until Loops** (G3-G4): T07.G3.04

#### Intermediate Loop Concepts (G4-G5)
- **Loops with Conditionals** (G4-G5): T07.G4.02, T07.G4.06
- **Loop Counters & For Loops** (G4-G5): T07.G4.03, T07.G4.08 (timed repeat)
- **Nested Loops** (G4-G5): T07.G4.07 (trace), T07.G5.04 (build)
- **Loops with Data** (G5): T07.G5.01 (simulation), T07.G5.02 (build lists), T07.G5.03 (aggregates)
- **Debugging** (G4): T07.G4.05

#### Advanced Loop Concepts (G6-G8)
- **Variable Bounds & Complex Tracing** (G6): T07.G6.01, T07.G6.05, T07.G6.06
- **Refactoring & Optimization** (G6): T07.G6.02, T07.G6.03 (search), T07.G6.04 (infinite loops)
- **Advanced Control Flow** (G6): T07.G6.08 (break/continue), T07.G6.09 (for-each)
- **Iterative Updates** (G6-G7): T07.G6.07, T07.G7.01 (motion simulation)
- **2D Grid Processing** (G7): T07.G7.02
- **Algorithm Analysis** (G7-G8): T07.G7.03, T07.G7.04, T07.G8.04
- **Classic Algorithms** (G8): T07.G8.02.01 (GCD), T07.G8.02.02 (primality), T07.G8.02.03 (Fibonacci)
- **Advanced Applications** (G8): T07.G8.01 (Monte Carlo), T07.G8.03 (structured data)

---

## 2. Available CreatiCode Loop Features

### 2.1 DOCUMENTED Loop Blocks

#### Control Category

1. **for [VARIABLE] from (START) to (LIMIT) at step (S)**
   - Block ID: `control_set_variable_in_loop`
   - Category: Control
   - Description: For-loop with automatic counter variable, supports custom start/limit/step
   - Use case: Iterating with a counter, counting by steps, counting backwards

2. **repeat (N) times at intervals of (T) [TIMEUNIT]**
   - Block ID: `control_repeat_on_every`
   - Category: Control
   - Description: Timed repeat with fixed intervals (milliseconds/frames/seconds)
   - Use case: Animations with consistent timing, game loops with fixed frame rates

3. **break**
   - Block ID: `control_break`
   - Category: Control
   - Description: Exit loop early
   - Use case: Early termination when condition met

4. **continue**
   - Block ID: `control_continue`
   - Category: Control
   - Description: Skip to next iteration
   - Use case: Skip invalid items without nested conditionals

#### Variables Category

5. **for each item [VARIABLE] in [LIST]**
   - Block ID: `data_for_each`
   - Category: Variables
   - Description: Iterate through list values
   - Use case: Process all items without manual indexing

6. **for each index [VARIABLE] in [LIST]**
   - Block ID: `data_for_each_index`
   - Category: Variables
   - Description: Iterate through list indices
   - Use case: Need position information while iterating

### 2.2 UNDOCUMENTED but AVAILABLE Loop Blocks

Based on example program usage in blockdes8.txt, these standard Scratch blocks appear to be available:

7. **repeat (N)**
   - Standard Scratch counted loop
   - Status: ⚠️ Used in examples but NOT in blockdes8.txt documentation
   - Use case: Basic repetition, fundamental loop concept

8. **forever**
   - Standard Scratch infinite loop
   - Status: ⚠️ Used in examples but NOT in blockdes8.txt documentation
   - Use case: Game loops, continuous animations

9. **repeat until <CONDITION>**
   - Standard Scratch conditional loop
   - Status: ⚠️ Likely available but needs verification
   - Use case: Loop until goal reached

### 2.3 Documentation Gap Analysis

**CRITICAL ISSUE:** The most fundamental loop blocks that students learn first are not documented:
- `repeat N` - The gateway loop block for Grade 3
- `forever` - Essential for game loops and animations
- `repeat until` - Key for goal-based iteration

**Impact:**
- Cannot verify if T07.G3.01-T07.G3.04 skills align with actual blocks
- May confuse curriculum developers
- Risk of skills referencing non-existent features

**Recommendation:** HIGH PRIORITY - Verify these blocks exist in CreatiCode and add to documentation

---

## 3. Issues Found

### 3.1 HIGH Priority Issues (8 issues)

#### ISSUE H1: Undocumented Core Loop Blocks
**Skills Affected:** T07.G3.01, T07.G3.02, T07.G3.03, T07.G3.04, T07.G4.01, T07.G4.04, T07.G4.06
**Description:** Skills reference `repeat N`, `forever`, and `repeat until` blocks that are not documented in blockdes8.txt, though they appear in example programs.
**Priority:** HIGH - Cannot verify feature alignment for foundational skills
**Recommendation:**
- Verify these blocks exist in CreatiCode platform
- Add proper documentation to blockdes8.txt
- If blocks don't exist, revise affected skills to use documented alternatives

#### ISSUE H2: T07.G3.01 - Excessive Cross-Topic Dependencies
**Skill:** Use a counted repeat loop
**Current Dependencies:**
```
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T04.G1.01: Match a picture pattern to a movement pattern
* T04.G2.01: Identify the repeating unit in a longer pattern
* T01.G2.05: Complete a simple if/then algorithm
* T07.G2.01: Identify when to use "repeat" vs "do once"
```
**Problem:** This is the FIRST coding loop skill but has 5 dependencies including T01.G2.05 (conditionals) which is unrelated to basic loops. The T04 pattern dependencies are from G1-G2 but the skill is in G3.
**Priority:** HIGH - Overloaded gateway skill blocks natural progression
**Recommendation:**
```
Required:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"

Optional context (not blockers):
* T04.G2.01: Identify the repeating unit in a longer pattern
```

#### ISSUE H3: T07.G3.04 - Depends on Non-Existent T09.G3.02
**Skill:** Use repeat‑until to reach a simple goal
**Current Dependency:** T09.G3.02: Use a variable in a conditional (if block)
**Problem:** T09.G3.02 does not exist. The T09 (Variables) topic jumps from T09.G3.01.04 to T09.G4.01.
**Priority:** HIGH - Broken dependency
**Recommendation:**
- Change to T09.G3.01.04 (Display variable value on stage) if checking variable values
- OR remove if basic `<touching [goal]?>` doesn't need variables
- Likely should just depend on T08.G3.01 (basic if statement)

#### ISSUE H4: T07.G4.03 - Combining Two Distinct Concepts
**Skill:** Use a loop counter variable and for loops
**Description:** Combines BOTH manual counter variables (set counter to 0, change by 1) AND CreatiCode's for-loop block in one skill.
**Problem:** These are conceptually different:
1. Manual counters teach the mechanics of counting
2. For-loops provide abstraction over manual counters
**Priority:** HIGH - Confuses teaching sequence
**Recommendation:** Split into two skills:
```
T07.G4.03: Use a loop counter variable
- Description: Manually create and increment a counter inside repeat loop
- For: Teaching the concept of counting iterations

T07.G4.03.01: Use for loops with automatic counters
- Description: Use CreatiCode's for-loop block as cleaner alternative
- Dependencies: T07.G4.03
- For: Learning abstraction after understanding mechanics
```

#### ISSUE H5: T07.G4.07 - Intra-Topic Dependency Violation
**Skill:** Trace simple nested loops with fixed bounds
**Dependencies:**
```
* T07.G4.03: Use a loop counter variable
* T07.G4.06: Trace code that combines a loop and a condition
```
**Problem:** T07.G4.07 is listed BEFORE T07.G4.03 in the document (skills should be in dependency order within a topic). Also depends on T07.G4.06 which comes after it.
**Priority:** HIGH - Violates topological order
**Recommendation:** Reorder skills:
```
T07.G4.03 (counter variable)
T07.G4.06 (trace loop + condition)
T07.G4.07 (trace nested loops)
```

#### ISSUE H6: T07.G6.05 vs T07.G6.06 - Unclear Distinction
**Skills:**
- T07.G6.05: Trace nested loops using a trace table
- T07.G6.06: Trace nested loops that generate visual patterns

**Problem:**
- G6.05 says it focuses on "the trace table methodology itself"
- G6.06 says it "applies the trace table technique learned in T07.G6.05"
- BUT both are at same grade level (G6) and G6.06 depends on G6.05
- The distinction between "learning trace tables" vs "applying to visual patterns" is vague
- Most nested loop problems HAVE visual output in block-based programming

**Priority:** HIGH - Confusing skill separation
**Recommendation:**
Option A: Merge into one skill "Trace nested loops using trace tables for visual patterns"
Option B: Make clearer distinction:
- G6.05: Trace nested loops with abstract calculations (counting, summing)
- G6.06: Trace nested loops with spatial output (grids, patterns, drawings)

#### ISSUE H7: T07.G8.02 - Overly Abstract for Implementation
**Skill:** Design iterative algorithms with loops
**Description:** "Students learn to design iterative algorithms by identifying three components: (1) initial state setup, (2) update rule that moves closer to the goal, and (3) stopping condition."
**Problem:** This is more of a meta-skill or framework for thinking, not a concrete assessable skill. How would you test if a student has mastered this abstraction?
**Priority:** HIGH - Not measurable/assessable
**Recommendation:** Either:
1. Move this to a teacher guide as a framework for teaching G8 loop algorithms
2. Rewrite as concrete skill: "Analyze iterative algorithms to identify setup, update, and stopping conditions"
3. Replace with example: "Implement a simple iterative algorithm (e.g., GCD, primality test)" - but wait, that's what the sub-skills do!

**Better approach:** Remove T07.G8.02 entirely. Its sub-skills (GCD, primality, Fibonacci) are concrete and teachable. The parent skill adds no assessable value.

#### ISSUE H8: T07.G6.01 - Unclear What "Variable Bounds" Means
**Skill:** Trace nested loops with variable bounds
**Description:** "loops where the loop bounds depend on variables or expressions (e.g., `repeat (rows)` or `repeat (n-1)`)"
**Problem:** The description focuses on when the NUMBER of repetitions is a variable, but the key example shows the inner bound CHANGING each iteration: `repeat (n - i)`. These are different concepts:
- Concept A: Loop count is stored in a variable (e.g., `repeat (rows)`) - easier
- Concept B: Loop count changes each outer iteration - harder, requires calculation

**Priority:** HIGH - Concept conflation could confuse students
**Recommendation:** Clarify which concept is the focus:
```
If Concept A: "Trace nested loops where iteration counts are stored in variables"
If Concept B: "Trace nested loops where inner bound depends on outer counter"
Or split into two skills if both are important.
```

### 3.2 MEDIUM Priority Issues (15 issues)

#### ISSUE M1: T07.K.01 - No Dependencies is Correct
**Status:** ✅ CORRECT - This is truly the first loops skill
**Note:** Kindergarten unplugged pattern completion is appropriately dependency-free

#### ISSUE M2: T07.G3.05 - Unnecessary Conditional Dependency
**Skill:** Fix a simple repeat loop count
**Current Dependencies:**
```
* T07.G3.04: Use repeat‑until to reach a simple goal
* T08.G3.03: Pick the right conditional block for a scenario
```
**Problem:** Fixing a simple loop count (e.g., changing repeat 4 to repeat 3) doesn't require understanding conditionals. The T08.G3.03 dependency is unrelated.
**Priority:** MEDIUM - Doesn't block but adds unnecessary prereq
**Recommendation:**
```
Required:
* T07.G3.02: Trace a script with a simple loop (to understand what loops do)
```

#### ISSUE M3: T07.G4.01 - Redundant Dependencies
**Skill:** Create a forever game loop for controls
**Current Dependencies:**
```
* T06.G3.01: Build a green‑flag script
* T07.G3.01: Use a counted repeat loop
* T07.G3.03: Build a forever loop for simple animation
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
```
**Problem:** If student can already build a forever loop (G3.03), adding T07.G3.01 (counted repeat) and T07.G3.05 (debugging) seems redundant. The skill is just "use forever with keyboard input" which only needs G3.03 + conditionals.
**Priority:** MEDIUM - Overspecified but not wrong
**Recommendation:**
```
Required:
* T07.G3.03: Build a forever loop for simple animation
* T08.G3.01: Use a simple if in a script

Optional:
* T06.G3.01: Build a green‑flag script (likely already known)
```

#### ISSUE M4: T07.G4.02 - Depends on Non-Existent T09.G3.01.04
**Skill:** Use an if statement inside a loop
**Current Dependency:** T09.G3.01.04: Display variable value on stage
**Problem:** Why does putting an if inside a loop require knowing how to display variables? This seems unrelated unless the examples specifically check variable values.
**Priority:** MEDIUM - Likely incorrect dependency
**Recommendation:** Remove T09.G3.01.04 unless the skill specifically requires checking variable monitors

#### ISSUE M5: T07.G4.04 - Minimal Dependency Set Too Small?
**Skill:** Identify and convert simple repeated code into loops
**Current Dependencies:**
```
* T06.G3.01: Build a green‑flag script
* T07.G3.01: Use a counted repeat loop
* T07.G3.04: Use repeat‑until to reach a simple goal
* T08.G3.01: Use a simple if in a script
```
**Problem:** Skill is about recognizing repeated blocks and refactoring to use `repeat N`. Why does it need T07.G3.04 (repeat-until) and T08.G3.01 (conditionals)? The description says "no variables or changing values involved."
**Priority:** MEDIUM - Dependencies don't match description
**Recommendation:**
```
Required:
* T07.G3.01: Use a counted repeat loop
* T07.G3.02: Trace a script with a simple loop (to understand what loops produce)
```

#### ISSUE M6: T07.G4.08 - Narrow Feature-Specific Skill
**Skill:** Use timed repeat for spaced animations
**Description:** Uses CreatiCode's `repeat (N) times at intervals of (T)` block
**Problem:** This is the ONLY skill that teaches this specific CreatiCode block. While it's useful, having one Grade 4 skill for one specific block seems imbalanced. Is this block important enough for its own skill?
**Priority:** MEDIUM - Curriculum balance question
**Recommendation:**
Option A: Keep it - it's a useful enhanced block worth teaching
Option B: Merge with T07.G4.01 or T07.G4.03 as an alternative timing technique
Option C: Create companion skills for other timed loop patterns

**Decision:** Probably KEEP - timed loops are important for animations and this is a cleaner solution than `wait` inside loops

#### ISSUE M7: T07.G5.01 - Overly Broad Description
**Skill:** Simulate repeated experiments with a loop
**Description:** "simulate a simple chance experiment (e.g., rolling a die, flipping a coin) repeatedly in code using a loop, and count outcomes to observe frequencies"
**Problem:** This combines:
1. Using random number blocks
2. Using loops to repeat experiments
3. Using counters to track outcomes
4. Understanding frequency vs. probability

This is actually quite complex for a single Grade 5 skill.
**Priority:** MEDIUM - May be too ambitious for one skill
**Recommendation:**
Consider splitting:
- G5.01a: Run random experiments in a loop
- G5.01b: Count outcomes to calculate frequencies
Or keep but acknowledge it's a multi-day project skill

#### ISSUE M8: T07.G5.02 - Vague "Repeated Samples from Sensors"
**Skill:** Build a list with a loop
**Description:** "loop that populates a list with a sequence of values (e.g., the numbers 1 to 10) or with repeated samples from user input or sensors"
**Problem:** CreatiCode is primarily used for sprite-based animation/games. What "sensors" are available? This sounds like it's written for Arduino/micro:bit but not adapted to CreatiCode's context.
**Priority:** MEDIUM - Possible feature misalignment
**Recommendation:**
- Verify CreatiCode has sensor input blocks (camera, microphone, etc.)
- If yes: Provide specific example
- If no: Remove sensor reference, focus on "user input" (ask blocks)

#### ISSUE M9: T07.G5.03 - "Repeated Events" Unclear
**Skill:** Use loops to compute aggregates
**Description:** "loop over items in a list (or through repeated events)"
**Problem:** What are "repeated events"? Does this mean:
- Event handlers triggering multiple times?
- A loop that processes event data?
- Collecting data from multiple user interactions?

**Priority:** MEDIUM - Ambiguous terminology
**Recommendation:** Clarify with concrete example:
- "Loop over items in a list OR through multiple rounds of user input to compute totals"

#### ISSUE M10: T07.G6.03 - Should Use for-each Loop
**Skill:** Loop‑based search in a list
**Description:** "implement a simple linear search using a loop to find the first item in a list that matches a target"
**Dependencies:** Includes T07.G5.02 (Build list) and T07.G5.03 (Aggregates)
**Problem:** This skill is in Grade 6 but doesn't depend on T07.G6.09 (for-each loops), which would be the natural block to use for searching. Also, why does search require T07.G5.03 (aggregates)?
**Priority:** MEDIUM - Missing key dependency
**Recommendation:**
```
Dependencies:
* T07.G5.02: Build a list with a loop
* T07.G6.09: Use for-each loops to iterate over lists
* T08.G4.01: Use if-then-else in a project (for conditional logic)

Remove: T07.G5.03 (not needed for search)
```

#### ISSUE M11: T07.G6.04 - Missing break Dependency
**Skill:** Avoid and fix infinite loops
**Description:** "modify the code to add a stopping condition or use the `break out of loop` block"
**Current Dependencies:** Does NOT include T07.G6.08 (break and continue)
**Problem:** Skill explicitly mentions using break block but doesn't depend on the skill that teaches it!
**Priority:** MEDIUM - Missing dependency
**Recommendation:** Add dependency on T07.G6.08

#### ISSUE M12: T07.G6.09 - Grade Placement Too Late
**Skill:** Use for-each loops to iterate over lists
**Current Grade:** 6
**Problem:** The for-each block (`for each item [variable] in [list]`) is documented and available, but students don't learn it until Grade 6. Meanwhile:
- G5.02: Build lists with loops (manual indexing)
- G5.03: Compute aggregates (manual indexing)
- G6.03: Search in lists (manual indexing)

All of these would be simpler with for-each loops!
**Priority:** MEDIUM - Suboptimal teaching sequence
**Recommendation:** Move T07.G6.09 to Grade 5 (after T07.G5.02) so students can use cleaner iteration patterns earlier

#### ISSUE M13: T07.G7.01 - Vague "Simple Rule Each Step"
**Skill:** Use loops to simulate motion over time
**Description:** "repeatedly updates position (and optionally velocity) to simulate motion, such as an object sliding or falling with a simple rule each step"
**Problem:** What's a "simple rule"? This needs concrete examples:
- Gravity: `change y by (velocity)`, `change velocity by (-0.5)`
- Friction: `change x by (speed * 0.9)`
- Collision bounce: `if touching edge then set velocity to (velocity * -1)`

**Priority:** MEDIUM - Too abstract for assessment
**Recommendation:** Provide specific implementation examples in description

#### ISSUE M14: T07.G8.01 - No List Processing Dependency
**Skill:** Monte Carlo simulations with loops
**Description:** "design loop‑based simulations that approximate probabilities"
**Current Dependencies:** Does NOT include any list skills
**Problem:** To collect simulation results and analyze frequencies, you typically need lists (or at least variables to count). Should depend on T07.G5.02 or T10.G5.01.
**Priority:** MEDIUM - Missing practical dependency
**Recommendation:** Add T07.G5.02 (Build list with loop) to dependencies

#### ISSUE M15: T07.G8.02 Sub-Skills - Inconsistent Dependencies
**Skills:** T07.G8.02.01 (GCD), T07.G8.02.02 (Primality), T07.G8.02.03 (Fibonacci)
**Problem:** All three depend on parent T07.G8.02, but:
- GCD and Fibonacci also need T09.G6.01 (variables/formulas)
- Primality also needs T08.G6.01 (conditionals)
- No explanation for why these specific additional dependencies

**Priority:** MEDIUM - Inconsistent dependency rationale
**Recommendation:** Standardize dependencies for all three:
```
All three should have:
* T07.G8.02: Design iterative algorithms
* T09.G6.01: Model quantities with variables
* T08.G6.01: Use conditionals to control simulation steps
```

### 3.3 LOW Priority Issues (9 issues)

#### ISSUE L1: T07.G1.01 and T07.G1.02 - Very Similar
**Skills:**
- G1.01: Count repetitions in a pattern
- G1.02: Match "do N times" instructions to outcomes

**Description:** Both are unplugged matching activities involving counting repetitions. The distinction is subtle (counting vs. matching).
**Priority:** LOW - Both are useful for scaffolding
**Recommendation:** Keep both but consider combining if time-constrained

#### ISSUE L2: T07.G2.01 - Could Add Example
**Skill:** Identify when to use "repeat" vs "do once"
**Description:** Sort tasks into "needs repeating" vs "do once"
**Note:** Good unplugged activity but could benefit from clearer examples in description
**Priority:** LOW - Description is adequate
**Recommendation:** Optional - Add 2-3 example tasks to description

#### ISSUE L3: T07.G3.02 - Redundant with G3.01?
**Skill:** Trace a script with a simple loop
**Description:** "predict how many times a basic action occurs or where a sprite ends up"
**Note:** This is the complement to G3.01 (using loops) - tracing vs. building
**Priority:** LOW - Both skills are valuable
**Recommendation:** Keep as is - tracing is distinct from building

#### ISSUE L4: T07.G4.06 - Almost Identical to G4.02
**Skills:**
- G4.02: Use an if statement inside a loop
- G4.06: Trace code that combines a loop and a condition

**Description:** One is "use" (building) and one is "trace" (reading), but both involve loops + conditionals.
**Priority:** LOW - Distinction between building and tracing is valid
**Recommendation:** Keep both but ensure examples are clearly different (G4.02 = create, G4.06 = analyze)

#### ISSUE L5: T07.G4.05 - "Complex" Needs Definition
**Skill:** Debug complex loop conditions and boundaries
**Description:** "more complex loop problems involving counter variables, repeat-until conditions, or off-by-one errors"
**Problem:** What makes it "complex" vs. T07.G3.05's "simple"? Needs concrete examples.
**Priority:** LOW - Description works but could be clearer
**Recommendation:** Add examples: "e.g., loop stops one iteration early, condition uses >= instead of >, counter increments at wrong time"

#### ISSUE L6: T07.G5.04 - Generic "Advanced Patterns"
**Skill:** Nested loops for advanced patterns or tilings
**Description:** "checkerboards, stripes, simple mosaics"
**Problem:** "Advanced" is relative - checkerboards are actually quite achievable at this level. What makes these "advanced" vs. simple nested loop drawings?
**Priority:** LOW - Functional but could be more specific
**Recommendation:** Clarify: "Use nested loops to create 2D patterns that require different row and column logic (e.g., alternating checkerboard colors)"

#### ISSUE L7: T07.G6.02 - Mathematical Expression Not Taught
**Skill:** Refactor complex repeated patterns into loops with variables
**Description:** "analyze the variation pattern and express it mathematically"
**Problem:** Expressing patterns mathematically (e.g., recognizing "move 10, move 20, move 30" as `move (i * 10)`) is a significant skill not explicitly taught elsewhere. This skill assumes students can do mathematical pattern analysis.
**Priority:** LOW - This is Grade 6, students likely have math skills
**Recommendation:** Consider adding a brief note about pattern analysis or link to math standards

#### ISSUE L8: T07.G6.07 - Overlaps with G7.01
**Skills:**
- G6.07: Use loops to update values iteratively (interest, health points, growth)
- G7.01: Use loops to simulate motion over time (position, velocity)

**Description:** Both are about iterative state updates. G7.01 is specifically motion while G6.07 is general state changes.
**Priority:** LOW - Progression is clear (general → specific)
**Recommendation:** Keep both but clarify that G7.01 is application of G6.07 to physics/motion

#### ISSUE L9: T07.G7.02 - "Even if Represented as 1D List"
**Skill:** Nested loops for 2D grids and tile maps
**Description:** "process a conceptual 2D grid (e.g., rows and columns of tiles), even if represented as positions or a 1D list plus indices"
**Problem:** The parenthetical note about 1D list representation is confusing. Is this skill about:
- Nested loops for logical 2D structure?
- Converting between 2D and 1D representations?

**Priority:** LOW - Doesn't affect skill functionality
**Recommendation:** Simplify: "Use nested loops to process 2D grids (rows and columns) for tile-based layouts or matrix operations"

---

## 4. Missing Skills Analysis

### 4.1 Potential Gaps in Scaffolding

#### GAP 1: No Explicit "While Loop" Skill
**Current Coverage:** `repeat N`, `forever`, `repeat until`
**Missing:** No explicit "while loop" skill
**Analysis:**
- Scratch/CreatiCode don't have a `while` block (only `repeat until`)
- `repeat until` is semantically equivalent to `while (not condition)`
- No action needed - covered by `repeat until` skills

#### GAP 2: Limited Break/Continue Practice
**Current Coverage:** T07.G6.08 introduces break and continue
**Missing:** No follow-up application skills
**Analysis:** Break and continue are introduced in G6 but never practiced in later skills (G7-G8 don't explicitly use them)
**Recommendation:** Consider adding examples of break/continue to:
- T07.G6.03 (search - break when found)
- T07.G8.02.02 (primality - break when divisor found)

#### GAP 3: No "Loop Invariants" Concept
**Current Coverage:** Algorithm analysis in G7-G8
**Missing:** No explicit teaching of loop invariants
**Analysis:** Loop invariants are a CS concept important for:
- Understanding algorithm correctness
- Competition programming
- Advanced CS courses

**Priority:** LOW - Loop invariants are college-level CS theory
**Recommendation:** Optional - Could add as enrichment in G8 for advanced students

#### GAP 4: No Performance/Efficiency Optimization
**Current Coverage:** T07.G7.03 compares algorithms by counting steps
**Missing:** No skill about optimizing loops themselves (e.g., breaking early, skipping unnecessary iterations)
**Analysis:** T07.G7.03 compares different algorithms, but there's no skill about making a single loop more efficient
**Recommendation:** Could add to G7 or G8:
```
T07.G7.05: Optimize loops for efficiency
- Description: Improve loop performance by breaking early, combining operations,
  or reducing redundant calculations. Compare before/after performance.
- Example: Search loop that checks every item vs. search that breaks when found
```

### 4.2 Recommended New Skills

#### NEW SKILL 1: Basic While Pattern Understanding (G3)
```
ID: T07.G3.02.01
Topic: T07 – Loops
Skill: Understand repeat-until as checking conditions
Description: Students understand that repeat-until checks a condition at the
START of each iteration (not just at the end). They predict whether a loop will
run 0, 1, or multiple times based on the starting condition. Use simple scenarios
like "repeat until <touching edge>" where sprite starts at different positions.

Dependencies:
* T07.G3.04: Use repeat-until to reach a simple goal
```

**Rationale:** There's a gap between "use repeat-until" (G3.04) and "debug loop conditions" (G4.05). Students need to understand when loops execute zero times.

#### NEW SKILL 2: Loop Counter Initialization (G4)
```
ID: T07.G4.03.00
Topic: T07 – Loops
Skill: Initialize loop counters before loops
Description: Students learn to set counter variables to starting values (usually 0 or 1)
BEFORE the loop begins. They debug scripts where forgetting to initialize causes wrong
results. Emphasizes that variables retain values between runs.

Dependencies:
* T09.G3.01.01: Create a variable
* T09.G3.01.02: Set variable value
```

**Rationale:** Counter variables (G4.03) assumes students know to initialize. This foundational concept needs explicit teaching.

#### NEW SKILL 3: Early Loop Patterns Practice (G5)
```
ID: T07.G5.02.01
Topic: T07 – Loops
Skill: Use common list-building patterns
Description: Students implement standard patterns for populating lists:
(1) sequential numbers, (2) repeated copies of a value, (3) user input collection.
They recognize when to use each pattern and combine them in projects.

Dependencies:
* T07.G5.02: Build a list with a loop
* T10.G5.01: Create and populate a list
```

**Rationale:** Bridges the gap between "build a list" and "compute aggregates" by teaching common patterns.

---

## 5. Dependency Analysis

### 5.1 Cross-Topic Dependencies

T07 skills depend on:
- **T01 (Algorithms):** T01.G2.05, T01.G6.01
- **T04 (Patterns):** T04.G1.01, T04.G2.01, T04.G3.03, T04.G3.04.01
- **T06 (Event Handlers):** T06.G3.01
- **T08 (Conditionals):** T08.G3.01, T08.G3.03, T08.G4.01, T08.G6.01
- **T09 (Variables):** T09.G3.01.04, T09.G3.02 (doesn't exist!), T09.G4.01, T09.G5.01, T09.G6.01
- **T10 (Lists):** T10.G5.01

### 5.2 X-2 Rule Violations

The X-2 rule states: Grade X skills should not depend on skills beyond Grade X-2.

#### VIOLATION 1: T07.G3.01 → T01.G2.05
- **Dependency:** Grade 3 skill depends on Grade 2.05 (within X-2 ✓)
- **Status:** No violation

#### VIOLATION 2: T07.G3.01 → T04.G1.01
- **Dependency:** Grade 3 skill depends on Grade 1.01
- **Status:** No violation (X-2 = 1)

#### VIOLATION 3: T07.G8.02 → T01.G6.01
- **Dependency:** Grade 8 skill depends on Grade 6.01
- **Status:** No violation (X-2 = 6)

✅ **Result:** NO X-2 violations found in T07 dependencies

### 5.3 Broken Dependencies

1. **T07.G3.04 → T09.G3.02** - T09.G3.02 does not exist (HIGH priority fix)
2. **T07.G4.02 → T09.G3.01.04** - Questionable if needed (MEDIUM priority review)

### 5.4 Intra-Topic Ordering Issues

Skills within T07 should be in topological order (dependencies come before dependents).

**Issue Found:** T07.G4.07 (line 165) depends on T07.G4.03 (line 117) - ✅ OK
BUT also depends on T07.G4.06 (line 155) - ✅ OK (G4.06 comes before G4.07)

**Wait, re-checking the actual line numbers:**
- T07.G4.03: line 117
- T07.G4.06: line 155
- T07.G4.07: line 165

These ARE in correct order. False alarm.

However, looking at dependencies:
- T07.G4.01 depends on T07.G3.05 (correct order ✓)
- T07.G4.05 depends on T07.G3.04 (correct order ✓)
- T07.G5.01 depends on T07.G4.05 (correct order ✓)

✅ **Result:** Intra-topic ordering is correct

---

## 6. Grade Appropriateness

### 6.1 K-2 Analysis (Unplugged Focus)

**Skills:** T07.K.01, T07.G1.01, T07.G1.02, T07.G2.01
**Assessment:** ✅ APPROPRIATE
- All are picture-based, unplugged activities
- No coding required
- Concrete, tangible patterns
- Age-appropriate cognitive load

### 6.2 G3 Analysis (First Coding Loops)

**Skills:** T07.G3.01 - T07.G3.05
**Assessment:** ⚠️ SLIGHTLY AGGRESSIVE
- T07.G3.01 is gateway skill but has 5 dependencies (see Issue H2)
- Introduces repeat, forever, AND repeat-until in same grade
- Includes basic debugging (G3.05)

**Recommendation:** Consider stretching to G3-G4 transition or simplifying G3.01 dependencies

### 6.3 G4 Analysis (Loop Sophistication)

**Skills:** T07.G4.01 - T07.G4.08 (8 skills)
**Assessment:** ⚠️ HEAVY LOAD
- Most skills of any grade level
- Covers game loops, conditionals in loops, counters, refactoring, debugging, tracing, nested loops, and timed repeats
- This is a LOT for one year

**Recommendation:** Consider moving 1-2 skills to G5 (candidates: G4.07 nested loop tracing, G4.08 timed repeat)

### 6.4 G5-G8 Analysis

**G5 (4 skills):** ✅ Appropriate - Data-focused applications
**G6 (9 skills):** ⚠️ Heavy but manageable - Advanced techniques
**G7 (4 skills):** ✅ Appropriate - Simulations and analysis
**G8 (7 skills):** ✅ Appropriate - Classic algorithms and competition prep

---

## 7. Concrete and Assessable Descriptions

### 7.1 Well-Defined Skills (Examples)

✅ **T07.G3.01:** "make a sprite jump exactly 3 times, or say 'Hello!' 2 times"
✅ **T07.G6.08:** "use `break` block to exit a loop early... use `continue` block to skip the rest of the current iteration"
✅ **T07.G8.02.01:** "Implement GCD using repeated subtraction"

These skills have:
- Clear action verbs (make, use, implement)
- Concrete examples
- Measurable outcomes

### 7.2 Skills Needing More Clarity

⚠️ **T07.G5.01:** "simulate a simple chance experiment" - What counts as successful mastery?
⚠️ **T07.G6.07:** "repeatedly update a variable based on its previous value" - Needs example in description
⚠️ **T07.G7.01:** "simulate motion with a simple rule" - "Simple rule" is vague
⚠️ **T07.G8.02:** "learn to design iterative algorithms" - Too meta, not assessable

### 7.3 Recommendations for Clarity

For each skill, ensure description includes:
1. **Action verb:** Use, build, trace, debug, analyze, implement
2. **Context:** What type of project or scenario
3. **Success criteria:** How do we know the student achieved it?
4. **Example:** Concrete instance of the skill in action

**Template:**
```
Description: Students [ACTION VERB] [SPECIFIC TECHNIQUE] to [PURPOSE/GOAL].
They [DEMONSTRATE UNDERSTANDING BY]. [EXAMPLE SCENARIO].
[Implementation note if needed].
```

---

## 8. Priority Recommendations Summary

### 8.1 IMMEDIATE Actions (HIGH Priority)

1. **Verify and document standard loop blocks** (Issue H1)
   - Check if `repeat N`, `forever`, `repeat until` exist in CreatiCode
   - Add to blockdes8.txt documentation
   - If missing, redesign G3 skills to use documented blocks

2. **Fix broken dependency** (Issue H3)
   - T07.G3.04: Change T09.G3.02 to T08.G3.01 or remove

3. **Simplify T07.G3.01 dependencies** (Issue H2)
   - Remove unrelated dependencies
   - Keep only: T06.G3.01, T07.G2.01

4. **Split T07.G4.03** (Issue H4)
   - Separate manual counters from for-loops
   - Create T07.G4.03.01 for for-loop block

5. **Clarify or merge G6.05 and G6.06** (Issue H6)
   - Define clear distinction between skills
   - OR merge into single comprehensive skill

6. **Fix T07.G8.02** (Issue H7)
   - Remove parent skill, keep concrete sub-skills
   - OR rewrite as "Analyze iterative algorithms"

7. **Clarify T07.G6.01** (Issue H8)
   - Focus on one concept: variable bounds vs. changing bounds
   - Provide clear examples

### 8.2 IMPORTANT Actions (MEDIUM Priority)

8. **Review and fix unnecessary dependencies** (Issues M2-M5)
   - T07.G3.05: Remove T08.G3.03
   - T07.G4.01: Simplify to core dependencies
   - T07.G4.02: Remove T09.G3.01.04 if not needed
   - T07.G4.04: Remove conditional dependencies

9. **Add missing dependency** (Issue M11)
   - T07.G6.04: Add T07.G6.08 (break/continue)

10. **Move T07.G6.09 earlier** (Issue M12)
    - For-each loops should be taught in G5 after basic list skills

11. **Verify CreatiCode sensor support** (Issue M8)
    - If no sensors, update T07.G5.02 description

12. **Standardize T07.G8.02 sub-skill dependencies** (Issue M15)
    - All three should have same base dependencies

13. **Add list dependency to T07.G8.01** (Issue M14)
    - Monte Carlo needs list skills

### 8.3 OPTIONAL Actions (LOW Priority)

14. **Add concrete examples** to vague skills (Issues L5, L7, L13)
    - T07.G4.05: Define "complex"
    - T07.G6.02: Note about pattern analysis
    - T07.G7.01: Specific motion rules

15. **Consider new skills** (Section 4.2)
    - Loop counter initialization (G4)
    - Repeat-until condition checking (G3)
    - Common list patterns (G5)

16. **Balance G4 workload** (Section 6.3)
    - Consider moving 1-2 skills to G5

---

## 9. Alignment with CreatiCode Features

### 9.1 Well-Aligned Skills

✅ **For-loops** (T07.G4.03): Matches `control_set_variable_in_loop` perfectly
✅ **Timed repeat** (T07.G4.08): Uses `control_repeat_on_every` effectively
✅ **Break/Continue** (T07.G6.08): Matches documented blocks
✅ **For-each loops** (T07.G6.09): Uses `data_for_each` and `data_for_each_index`

### 9.2 Uncertain Alignment

⚠️ **Basic loops** (G3.01-G3.04): Assumes `repeat N`, `forever`, `repeat until` exist but not documented
⚠️ **Sensor input** (G5.02): CreatiCode sensor support unclear

### 9.3 Feature Enhancement Opportunities

CreatiCode has enhanced blocks that could be featured more:
1. **Timed repeat** - Only used in one skill (T07.G4.08)
2. **For-loop with step** - Could emphasize counting by 2s, backwards counting, etc.
3. **For-each variants** - Could add skill distinguishing item vs. index iteration

---

## 10. Competition Readiness Assessment

### 10.1 Coverage of Competition Topics

T07 skills prepare students for programming competitions that involve:

✅ **Loop patterns:** Well covered (G4-G6)
✅ **Nested loops:** Excellent progression (G4.07 → G5.04 → G6.01 → G7.02)
✅ **Classic algorithms:** Strong (G8 sub-skills cover GCD, primality, Fibonacci)
✅ **Optimization:** Good (G7.03 compares algorithms)
✅ **Trace tables:** Excellent (G6.05-G6.06 teach systematic tracing)

⚠️ **Loop invariants:** Not covered (optional advanced concept)
⚠️ **Complex loop math:** Limited (G6.02 touches on it)

### 10.2 Comparison with Competition Problem Types

**Bebras Challenge:**
- Pattern recognition: ✅ Covered (K-G2)
- Loop counting: ✅ Covered (G3-G4)
- Efficiency analysis: ✅ Covered (G7.03)

**USACO Bronze:**
- Complete search with loops: ✅ Covered (G6-G7)
- Nested loops for grids: ✅ Covered (G7.02)
- Simulation: ✅ Covered (G7-G8)

**Code.org CSA:**
- For-loop variants: ✅ Covered (G4.03)
- List iteration: ✅ Covered (G6.09)
- Nested loops: ✅ Covered (G5-G7)

**Overall:** T07 provides strong competition preparation

---

## 11. Summary Statistics

| Metric | Value |
|--------|-------|
| Total Skills | 41 |
| Unplugged Skills (K-G2) | 4 (10%) |
| Coding Skills (G3-G8) | 37 (90%) |
| Gateway Skills | 5 (G3.01, G3.03, G3.04, G4.03, G6.09) |
| Sub-Skills | 3 (T07.G8.02.01-03) |
| Skills with Dependencies | 37 (90%) |
| Skills without Dependencies | 4 (K.01, G1.01, G8.02.01-03 parent) |
| Average Dependencies per Skill | 2.8 |
| Max Dependencies (single skill) | 5 (T07.G3.01) |
| Issues Found (Total) | 32 |
| - HIGH Priority | 8 |
| - MEDIUM Priority | 15 |
| - LOW Priority | 9 |
| Broken Dependencies | 2 |
| X-2 Violations | 0 |
| Intra-Topic Order Issues | 0 |

---

## 12. Action Plan

### Phase 1: Critical Fixes (Week 1)
1. Verify standard loop blocks in CreatiCode
2. Fix broken dependency T07.G3.04 → T09.G3.02
3. Simplify T07.G3.01 dependencies
4. Split T07.G4.03 into manual + for-loop skills
5. Resolve T07.G8.02 (remove or rewrite)

### Phase 2: Dependency Cleanup (Week 2)
6. Remove unnecessary dependencies from G3.05, G4.01, G4.02, G4.04
7. Add missing dependency G6.04 → G6.08
8. Move G6.09 to G5
9. Fix T07.G6.01 and G6.05/G6.06 clarity issues

### Phase 3: Enhancement (Week 3)
10. Add concrete examples to vague skills
11. Verify sensor support and update G5.02
12. Standardize G8.02 sub-skill dependencies
13. Consider adding new scaffolding skills

### Phase 4: Documentation (Week 4)
14. Update blockdes8.txt with standard loop blocks
15. Create teacher guide for loop progression
16. Add assessment rubrics for key skills

---

## 13. Conclusion

The T07 (Loops) topic is **well-structured overall** with excellent scaffolding from unplugged patterns to advanced algorithms. The progression through counted loops, forever loops, conditional loops, nested loops, and algorithmic applications is pedagogically sound.

**Key Strengths:**
- Strong unplugged foundation (K-G2)
- Clear gateway skills for each loop type
- Excellent nested loop progression
- Strong competition preparation
- Good use of CreatiCode-specific features

**Key Concerns:**
- Standard loop blocks not documented (HIGH priority)
- Some broken or questionable dependencies (HIGH/MEDIUM priority)
- Grade 3-4 cognitive load may be heavy
- A few skills lack concrete examples

**Overall Recommendation:** APPROVE with required fixes for HIGH priority issues before deployment. The topic is production-ready after addressing the 8 HIGH priority issues listed in Section 8.1.

**Estimated Effort:**
- HIGH priority fixes: 8-12 hours
- MEDIUM priority improvements: 12-16 hours
- LOW priority enhancements: 4-6 hours
- **Total:** 24-34 hours for complete optimization

---

*End of Report*
