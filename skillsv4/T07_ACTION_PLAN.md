# T07 (Loops) Action Plan for Fixes
**Based on**: T07_COMPREHENSIVE_ANALYSIS.md
**Date**: 2025-11-22

---

## PHASE 1: HIGH PRIORITY FIXES (Required)

### Action H1: Add K-2 Foundational Skills
**Priority**: CRITICAL
**Estimated New Skills**: 4

#### New Skill: T07.K.01
```
ID: T07.K.01
Topic: T07 – Loops
Skill: Identify repeating patterns in picture sequences
Description: Students look at a sequence of pictures and identify which pattern repeats (e.g., "red circle, blue square, red circle, blue square" is AB pattern). They recognize when the same group of items appears over and over. Use simple 2-3 element patterns with clear visual differences.

Dependencies:
* T04.K.01: Match same/different in simple patterns
```

#### New Skill: T07.G1.01
```
ID: T07.G1.01
Topic: T07 – Loops
Skill: Complete a visual pattern by adding the repeated unit
Description: Students are shown a pattern with missing elements and add the correct repeated unit to continue it. For example, if shown "star-moon-star-moon-star-[?]", they select "moon" to complete the pattern. This builds on pattern recognition by requiring active construction of the repetition.

Dependencies:
* T07.K.01: Identify repeating patterns in picture sequences
* T04.G1.01: Match a picture pattern to a movement pattern
```

#### New Skill: T07.G1.02
```
ID: T07.G1.02
Topic: T07 – Loops
Skill: Count how many times a pattern unit repeats
Description: Students count the number of times a pattern unit appears in a sequence. For example, in "AB-AB-AB-AB" they count 4 repetitions of the AB unit. This introduces the concept of counting iterations, preparing for "repeat N" loops in G3.

Dependencies:
* T07.G1.01: Complete a visual pattern by adding the repeated unit
```

#### New Skill: T07.G2.01
```
ID: T07.G2.01
Topic: T07 – Loops
Skill: Match "do this N times" instructions to picture sequences
Description: Students match written instructions like "Draw a star 3 times" to picture sequences showing the action repeated the correct number of times. They distinguish between "do once", "do twice", "do three times" by counting the repetitions in the pictures. This directly prepares for understanding repeat blocks in coding.

Dependencies:
* T07.G1.02: Count how many times a pattern unit repeats
* T04.G2.01: Identify the repeating unit in a longer pattern
```

#### Action Items:
1. Insert these 4 skills at the beginning of T07 topic
2. Update T07.G3.01 dependencies to include T07.G2.01
3. Verify cross-references with T04 pattern skills remain complementary

---

### Action H2: Verify and Fix Block Names for T07.G6.08
**Priority**: HIGH
**Affected Skill**: T07.G6.08

#### Investigation Required:
1. Check CreatiCode documentation for exact block names:
   - Break block: Is it "break out of loop" or "stop this script" or other?
   - Continue block: Is it "continue to next iteration" or other?

#### Possible Revisions:

**If blocks exist with different names:**
Update description to match exact block names.

**If break/continue blocks don't exist:**
Revise skill entirely:
```
ID: T07.G6.08
Topic: T07 – Loops
Skill: Exit loops early using flag variables and conditionals
Description: Students use a flag variable combined with repeat-until or if-statements to exit a loop when a condition is met (e.g., "found = true" to stop searching once an item is found). While CreatiCode doesn't have explicit break/continue blocks, this pattern achieves the same goal: stopping iteration early or skipping certain iterations based on conditions.

Dependencies:
* T07.G5.02: Build a list with a loop
* T07.G6.03: Loop-based search in a list
* T07.G6.04: Avoid and fix infinite loops
* T09.G4.01: Use variables to store and update game state
```

#### Action Items:
1. **VERIFY** exact block names in CreatiCode
2. **UPDATE** skill description based on findings
3. **TEST** that skill is implementable with available blocks

---

### Action H3: Clarify Distinction Between G6.05 and G6.06
**Priority**: HIGH
**Affected Skills**: T07.G6.05, T07.G6.06

#### Recommended Revision:

**T07.G6.05** (Keep focused on METHODOLOGY):
```
ID: T07.G6.05
Topic: T07 – Loops
Skill: Trace nested loops using a trace table
Description: Students learn the trace table technique as a systematic method for tracking variable changes through nested loops. They create a table with columns for each variable (outer counter, inner counter, accumulator, etc.) and rows for each iteration, filling in values step-by-step. This methodical approach works for any nested loop - whether computing sums, generating patterns, or processing data. Trace tables are particularly useful for competition problems where mental tracing is error-prone.

Dependencies:
* T07.G5.03: Use loops to compute aggregates
* T07.G5.04: Nested loops for advanced patterns or tilings
* T09.G4.01: Use variables to store and update game state
```

**T07.G6.06** (Keep focused on VISUAL APPLICATION):
```
ID: T07.G6.06
Topic: T07 – Loops
Skill: Trace nested loops that generate visual patterns
Description: Students trace nested loops that produce visual output (e.g., drawing a checkerboard, creating a grid of stamps, or generating star patterns) to predict what the final image will look like. They understand how row and column counters control position, and may use the trace table technique from G6.05 to help track values. This skill focuses on spatial reasoning and connecting abstract loop logic to concrete visual results.

Dependencies:
* T07.G5.03: Use loops to compute aggregates
* T07.G5.04: Nested loops for advanced patterns or tilings
* T07.G6.05: Trace nested loops using a trace table
* T08.G3.01: Use a simple if in a script
```

#### Key Changes:
- G6.05: Emphasize it's a GENERAL TECHNIQUE for any nested loop
- G6.06: Emphasize VISUAL application and add G6.05 as dependency
- G6.06: Note that trace table from G6.05 can be USED in this context
- Clear progression: Learn technique (G6.05) → Apply to visual patterns (G6.06)

#### Action Items:
1. **UPDATE** both skill descriptions as shown above
2. **ADD** T07.G6.05 dependency to T07.G6.06
3. **VERIFY** this creates appropriate progression

---

### Action H4: Rewrite T07.G8.02 for Specificity
**Priority**: HIGH
**Affected Skill**: T07.G8.02

#### Current (Too Vague):
"Students learn the general pattern of iterative algorithms - using loops to repeatedly update values until a condition is met..."

#### Revised (Specific and Assessable):
```
ID: T07.G8.02
Topic: T07 – Loops
Skill: Design iterative algorithms with loops
Description: Students analyze word problems or scenarios to determine if an iterative algorithm is needed - situations where values must be repeatedly updated until a condition is met, and a direct formula won't work. They identify three key components: (1) initial state, (2) update rule for each iteration, and (3) stopping condition. Then they select the appropriate loop structure (repeat-until, for-loop, or forever with break) and implement the algorithm. Examples include: repeated subtraction for GCD, trial division for prime checking, or iterative calculation of Fibonacci numbers.

Dependencies:
* T01.G6.01: Count comparisons in linear and binary search
* T07.G6.01: Trace nested loops with variable bounds
* T07.G7.03: Compare loop algorithms by counting steps
* T07.G7.04: Loop patterns for counting and accumulation
* T08.G6.01: Use conditionals to control simulation steps
```

#### Key Improvements:
- Specific cognitive task: "analyze to determine if iteration is needed"
- Clear three-component framework for assessment
- Concrete examples that connect to sub-skills
- Maintains broad applicability while being assessable

#### Action Items:
1. **REPLACE** description with revised version
2. **VERIFY** sub-skills (G8.02.01, .02, .03) still align
3. **TEST** that description supports assessment creation

---

### Action H5: Add For-Each Iteration Skill
**Priority**: HIGH
**Estimated New Skills**: 1

#### New Skill: T07.G6.09
```
ID: T07.G6.09
Topic: T07 – Loops
Skill: Use for-each loops to iterate through lists
Description: Students use CreatiCode's `for each item [var] in [list]` block to process all items in a list without manually tracking an index counter. They learn that this pattern is cleaner and less error-prone than using a counter variable with `item [i] of [list]`. Students also learn `for each index [var] in [list]` when they need to know both the position and the value. This iteration pattern is especially useful for processing lists where the number of items may vary.

Dependencies:
* T07.G5.02: Build a list with a loop
* T07.G6.03: Loop-based search in a list
* T09.G4.01: Use variables to store and update game state
```

#### Rationale:
- Fills gap: CreatiCode has for-each blocks but no skill teaches them
- Natural progression after learning manual list iteration
- Common pattern in modern programming
- Reduces errors from off-by-one mistakes with manual indexing

#### Action Items:
1. **INSERT** skill as T07.G6.09
2. **UPDATE** any later skills that could reference this pattern
3. **VERIFY** placement between G6 list skills and G7 advanced topics

---

## PHASE 2: MEDIUM PRIORITY FIXES (Recommended)

### Action M1: Review T07.G4.07 Dependency
**Priority**: MEDIUM
**Affected Skill**: T07.G4.07

#### Current Situation:
T07.G4.07 depends on T07.G4.03 (loop counter variables), but uses "fixed bounds" (constants, not variables).

#### Recommended Action:
**Keep dependency, clarify description**:
```
ID: T07.G4.07
Topic: T07 – Loops
Skill: Trace simple nested loops with fixed bounds
Description: Students trace a simple script with two nested loops using fixed repeat counts (e.g., outer loop repeats 3 times, inner loop repeats 2 times) to predict total iterations and final outcomes. Use small iteration counts (2-3 each) and concrete visual actions like drawing or stamping. The loop bounds are constant numbers, not variables. Understanding loop counter mechanics from T07.G4.03 helps students mentally track which iteration they're on in each nested level, even when the bounds themselves are fixed. This prepares students for building nested loops in Grade 5.

Dependencies:
* T07.G4.03: Use a loop counter variable and for loops
* T07.G4.06: Trace code that combines a loop and a condition
```

#### Action Items:
1. **ADD** clarifying sentence about why G4.03 dependency helps
2. **NO STRUCTURAL CHANGES** needed

---

### Action M2: Update T07.G3.01 Dependencies (After K-2 Added)
**Priority**: MEDIUM (depends on H1 completion)
**Affected Skill**: T07.G3.01

#### Current Dependencies:
```
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T04.G1.01: Match a picture pattern to a movement pattern
* T04.G2.01: Identify the repeating unit in a longer pattern
* T01.G2.05: Complete a simple if/then algorithm
```

#### Revised Dependencies (After K-2 Added):
```
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Match "do this N times" instructions to picture sequences
* T04.G1.01: Match a picture pattern to a movement pattern
* T04.G2.01: Identify the repeating unit in a longer pattern
* T01.G2.05: Complete a simple if/then algorithm
```

#### Key Change:
- **ADD** T07.G2.01 as primary pattern/repetition foundation
- **KEEP** T04 dependencies for complementary perspective

#### Action Items:
1. **COMPLETE** H1 first (add K-2 skills)
2. **UPDATE** dependencies to include T07.G2.01
3. **VERIFY** no circular dependencies created

---

### Action M3: Document G4 Skill Sequencing
**Priority**: MEDIUM
**Affected Skills**: All G4 skills

#### Recommended Sequencing Guide:
Create instructor documentation showing G4 skill dependencies:

```
GRADE 4 LOOP SKILLS - RECOMMENDED TEACHING ORDER

Tier 1 (Can be taught in parallel after G3 completion):
- T07.G4.01: Forever game loop
- T07.G4.02: If inside a loop
- T07.G4.03: Loop counter variables and for loops
- T07.G4.04: Convert repeated code to loops
- T07.G4.05: Debug complex loop conditions
- T07.G4.06: Trace loop + condition
- T07.G4.08: Timed repeat for animations

Tier 2 (Requires Tier 1 completion):
- T07.G4.07: Trace nested loops (needs G4.03 + G4.06)

NOTE: While all G4 skills are valid per X-2 rule, T07.G4.07 creates
intra-grade dependency. Plan curriculum to cover Tier 1 skills before
introducing nested loop tracing.
```

#### Action Items:
1. **CREATE** instructor guide document
2. **NO CHANGES** to skill definitions (structure is valid)
3. **COMMUNICATE** sequencing in teacher materials

---

### Action M4: Expand G5 Skills
**Priority**: MEDIUM
**Estimated New Skills**: 2 (optional)

#### Potential New Skill: T07.G5.05
```
ID: T07.G5.05
Topic: T07 – Loops
Skill: Use loops with user input to build interactive sequences
Description: Students create loops that repeatedly ask for user input and process each response, building lists or updating displays based on the input. For example, repeatedly asking "Enter a number (or -1 to stop)" and calculating the sum of all entered numbers. This combines loop control with input handling, requiring students to design both the loop termination condition and the processing logic.

Dependencies:
* T07.G4.05: Debug complex loop conditions and boundaries
* T07.G5.02: Build a list with a loop
* T10.G4.01: Use ask-and-wait to get user text input
```

#### Potential New Skill: T07.G5.06
```
ID: T07.G5.06
Topic: T07 – Loops
Skill: Trace loops that modify list items
Description: Students trace loops that change values inside a list (e.g., doubling every number, adding 10 to each score, or capitalizing each name). They predict the final state of the list after all iterations. This bridges list-building (G5.02) and list-searching (G6.03) by focusing on in-place modifications.

Dependencies:
* T07.G5.02: Build a list with a loop
* T07.G5.03: Use loops to compute aggregates
* T09.G4.01: Use variables to store and update game state
```

#### Rationale:
- Smooths progression: G4 (8) → G5 (4→6) → G6 (8)
- Adds important patterns: input loops and list modification
- Creates bridge to G6 list-processing skills

#### Action Items:
1. **DECIDE** if G5 expansion is needed (not critical)
2. **INSERT** skills if approved
3. **VERIFY** dependencies align with other topics (T10 for input)

---

### Action M5: Split T07.G4.03 Into Two Skills
**Priority**: MEDIUM
**Affected Skill**: T07.G4.03

#### Current Skill (Too Broad):
Teaches both manual counter variables AND for-loop blocks in one skill.

#### Proposed Split:

**T07.G4.03** (Manual counter pattern):
```
ID: T07.G4.03
Topic: T07 – Loops
Skill: Use a loop counter variable to track iterations
Description: Students create a counter variable that tracks how many times a loop has run. They initialize it to 0 or 1 before the loop, then increment it by 1 (using `change [counter] by 1`) inside the loop body. This allows them to display step numbers ("Step 1", "Step 2"...), make decisions based on iteration count, or track progress. Unlike the built-in for-loop counter, students manage this variable themselves, giving them full control and deeper understanding of the counter pattern.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.01: Use a counted repeat loop
* T07.G3.05: Fix a simple repeat loop count
* T09.G3.01: Create and use a numeric variable for score or count
```

**T07.G4.03.01** (For-loop blocks):
```
ID: T07.G4.03.01
Topic: T07 – Loops
Skill: Use for-loops with start, limit, and step parameters
Description: Students use CreatiCode's `for [variable] from (START) to (LIMIT) at step (S)` block, which provides a built-in loop counter that automatically updates. They practice with different configurations: counting from 1 to 10 (step 1), counting by 2s for even numbers (step 2), counting backwards (step -1), or starting from non-zero values. This block combines the counter pattern from T07.G4.03 with automatic management, making certain loops cleaner and less error-prone.

Dependencies:
* T07.G4.03: Use a loop counter variable to track iterations
* T09.G3.01: Create and use a numeric variable for score or count
```

#### Benefits:
- Better granularity for assessment
- Clearer learning progression: manual → automated
- Allows focusing on one pattern at a time

#### Impact Analysis:
Skills that depend on current T07.G4.03 would depend on the split skills:
- Skills needing manual counter: depend on T07.G4.03
- Skills needing for-loop: depend on T07.G4.03.01
- Skills needing counter concept generally: depend on T07.G4.03

#### Action Items:
1. **SPLIT** skill as shown above
2. **REVIEW** all skills that depend on T07.G4.03 (G4.07, G6.01, G6.02, G7.04)
3. **UPDATE** dependencies based on which counter type each needs
4. **ADJUST** skill numbering if needed

---

### Action M6: Add Context to T07.G7.01 Description
**Priority**: MEDIUM
**Affected Skill**: T07.G7.01

#### Current Description:
"Students implement a loop that repeatedly updates position (and optionally velocity) to simulate motion, such as an object sliding or falling with a simple rule each step."

#### Enhanced Description:
```
Description: Students implement a loop that repeatedly updates position (and optionally velocity) to simulate motion, such as an object sliding or falling with a simple rule each step. This applies the iterative update pattern from T07.G6.07 (updating values based on previous values) to a physics context, where each loop iteration represents one time step. For example, a sliding object might reduce its speed by 10% each frame, or a falling object might increase downward velocity by a constant acceleration. This bridges abstract iteration concepts to concrete motion simulation.

Dependencies: [unchanged]
* T07.G6.05: Trace nested loops using a trace table
* T07.G6.06: Trace nested loops that generate visual patterns
* T07.G6.07: Use loops to update values iteratively
```

#### Key Addition:
- Explicit connection to G6.07 (iterative updates)
- Explains time-step concept
- Concrete examples of motion rules

#### Action Items:
1. **UPDATE** description with enhanced version
2. **VERIFY** dependencies already include G6.07 (they do)

---

### Action M7: Add Loop Efficiency Skill
**Priority**: MEDIUM
**Estimated New Skills**: 1 (optional)

#### New Skill: T07.G7.05
```
ID: T07.G7.05
Topic: T07 – Loops
Skill: Optimize loop bounds to reduce unnecessary iterations
Description: Students identify when a loop performs unnecessary iterations and tighten the bounds to improve efficiency. For example, when checking if a number N is prime, they recognize that testing divisors up to √N is sufficient instead of testing all numbers up to N-1. They compare iteration counts before and after optimization and explain why the optimized version produces the same result. This skill develops algorithmic thinking about efficiency without requiring formal Big-O notation.

Dependencies:
* T07.G6.08: Use break and continue to control loop flow
* T07.G7.03: Compare loop algorithms by counting steps
* T07.G7.04: Loop patterns for counting and accumulation
```

#### Rationale:
- Fills gap in efficiency reasoning
- Complements T07.G7.03 (compares algorithms) and T07.G8.04 (compares structures)
- Practical skill for competitions and real-world coding
- Partially covered in T07.G8.02.02 but should be explicit

#### Action Items:
1. **DECIDE** if efficiency skill is needed at G7
2. **INSERT** as T07.G7.05 if approved
3. **UPDATE** T07.G8.02.02 to reference this skill as prerequisite

---

### Action M8: Verify Sub-Skill Dependencies After G8.02 Revision
**Priority**: MEDIUM
**Affected Skills**: T07.G8.02.01, T07.G8.02.02, T07.G8.02.03
**Depends On**: Completion of H4

#### Current Dependencies:
All three sub-skills depend primarily on parent T07.G8.02.

#### After H4 Revision:
Verify each sub-skill aligns with revised T07.G8.02 focus:

**T07.G8.02.01** (GCD using repeated subtraction):
- Requires: identifying iterative algorithm, update rule (subtract smaller from larger), stopping condition (both equal)
- ✓ Aligns with revised G8.02

**T07.G8.02.02** (Prime checking with trial division):
- Requires: identifying iterative algorithm, update rule (test next divisor), stopping condition (found divisor or reached √N)
- ✓ Aligns with revised G8.02
- Consider adding T07.G7.05 (optimize bounds) if that skill is added

**T07.G8.02.03** (Fibonacci iterative):
- Requires: identifying iterative algorithm, update rule (add previous two), stopping condition (reached target count)
- ✓ Aligns with revised G8.02

#### Potential Enhancement:
Consider adding T07.G7.04 (loop patterns for accumulation) as common dependency:
```
All three sub-skills could add:
* T07.G7.04: Loop patterns for counting and accumulation
```

Rationale: GCD, prime checking, and Fibonacci all use accumulator patterns (tracking state across iterations), which G7.04 explicitly teaches.

#### Action Items:
1. **COMPLETE** H4 revision first
2. **VERIFY** all sub-skills still align with parent
3. **CONSIDER** adding G7.04 as shared dependency
4. **UPDATE** dependencies if needed

---

## PHASE 3: OPTIONAL ENHANCEMENTS

### Optional 1: Add Specific 3D Loop Iteration Skill
**Estimated New Skills**: 1

CreatiCode has `for each 3D object named [var]` block. If 3D programming is significant in curriculum:

```
ID: T07.G7.06
Topic: T07 – Loops
Skill: Use for-each loops to process 3D objects
Description: Students use CreatiCode's `for each 3D object named [var]` block to iterate through all 3D objects in a scene and apply operations to each (e.g., rotate all cubes, change all spheres' colors, or detect collisions with all obstacles). This extends the for-each pattern from lists to 3D scene objects.

Dependencies:
* T07.G6.09: Use for-each loops to iterate through lists
* [3D programming dependency from relevant topic]
```

---

### Optional 2: Add Parallel Loop Skill
**Estimated New Skills**: 1

If CreatiCode supports concurrent loops (multiple forever loops running simultaneously):

```
ID: T07.G6.10
Topic: T07 – Loops
Skill: Coordinate multiple concurrent loops
Description: Students create projects where multiple forever loops run simultaneously on different sprites (e.g., one sprite's loop handles player movement, another sprite's loop handles enemy AI, a third loop handles score display). They understand that each loop runs independently but may interact through shared variables or broadcasts.

Dependencies:
* T07.G4.01: Create a forever game loop for controls
* T06.G4.01: Use broadcast to trigger behaviors across sprites
* T09.G4.01: Use variables to store and update game state
```

---

## IMPLEMENTATION CHECKLIST

### Phase 1 (Required - High Priority):
- [ ] H1: Add 4 K-2 skills (T07.K.01, G1.01, G1.02, G2.01)
- [ ] H2: Verify break/continue block names, update T07.G6.08
- [ ] H3: Clarify G6.05/G6.06 distinction, add dependency
- [ ] H4: Rewrite T07.G8.02 description
- [ ] H5: Add T07.G6.09 (for-each loops)

### Phase 2 (Recommended - Medium Priority):
- [ ] M1: Clarify T07.G4.07 description
- [ ] M2: Update T07.G3.01 dependencies (after H1)
- [ ] M3: Create G4 sequencing guide for instructors
- [ ] M4: Consider adding 2 G5 skills (T07.G5.05, G5.06)
- [ ] M5: Split T07.G4.03 into two skills
- [ ] M6: Enhance T07.G7.01 description
- [ ] M7: Consider adding T07.G7.05 (loop efficiency)
- [ ] M8: Verify sub-skill dependencies (after H4)

### Phase 3 (Optional - Enhancements):
- [ ] Consider T07.G7.06 (3D object iteration)
- [ ] Consider T07.G6.10 (parallel/concurrent loops)

---

## ESTIMATED IMPACT

### Skill Count Changes:
- **Current**: 36 skills (K: 0, G1: 0, G2: 0, G3: 5, G4: 8, G5: 4, G6: 8, G7: 4, G8: 7)
- **After Phase 1**: 41 skills (K: 1, G1: 2, G2: 1, G3: 5, G4: 8, G5: 4, G6: 9, G7: 4, G8: 7)
- **After Phase 2 (all optional additions)**: 46+ skills

### Description Changes:
- **Phase 1**: 5 major rewrites
- **Phase 2**: 3 minor clarifications

### Dependency Updates:
- **Phase 1**: ~5-10 skills need dependency updates
- **Phase 2**: ~3-5 skills need dependency updates

### Timeline Estimate:
- **Phase 1**: 3-4 hours (critical fixes)
- **Phase 2**: 2-3 hours (improvements)
- **Phase 3**: 1-2 hours (if desired)
- **Total**: 6-9 hours for complete implementation
