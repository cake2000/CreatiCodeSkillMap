# T07 (Loops) Comprehensive Analysis
**Date**: 2025-11-22
**Total Skills Analyzed**: 36 (G3: 5, G4: 8, G5: 4, G6: 8, G7: 4, G8: 7)

---

## HIGH PRIORITY ISSUES

### H1: K-2 Coverage Gap (CRITICAL)
**Severity**: High
**Skill IDs Affected**: None (that's the problem!)
**Issue**: T07 has ZERO K-2 skills. Per spec, K-2 should have picture-based foundational skills.

**Analysis**:
- Current progression starts at G3.01 with `repeat N` loops
- K-2 students miss foundational pattern recognition that supports loop concepts
- Other topics (T04, T01) have K-2 skills that reference patterns, but T07 doesn't establish its own foundation

**Recommended Fix**:
Add 3-4 picture-based K-2 skills:
1. **T07.K.01**: Identify repeating patterns in pictures (AB, ABB patterns)
2. **T07.K.02**: Complete a visual pattern by adding the missing repeated unit
3. **T07.G1.01**: Count how many times a pattern repeats in a sequence
4. **T07.G2.01**: Recognize "do this 3 times" instruction patterns in picture sequences

**Justification**:
- Creates natural progression from visual pattern recognition (K-2) → simple loops (G3)
- Aligns with T04.K.01, T04.G1.01, T04.G2.01 which already cover pattern matching
- Provides pre-coding foundation for loop concepts
- Current G3.01 dependencies include T04.G1.01 and T04.G2.01 (pattern skills), suggesting K-2 pattern foundation is intended

---

### H2: Block Accuracy - "break" and "continue" Blocks
**Severity**: High
**Skill IDs Affected**: T07.G6.08
**Issue**: Skill references `break out of loop` and `continue to next iteration` blocks - need verification these exact blocks exist in CreatiCode.

**Description from skill**:
"Students use CreatiCode's `break out of loop` block to exit a loop early... and use the `continue to next iteration` block to skip the rest of the current iteration"

**Recommended Action**:
1. Verify exact block names in CreatiCode (may be "stop this script" or different phrasing)
2. Update skill description to match actual block names
3. If blocks don't exist, revise T07.G6.08 to use alternative approaches (flag variables + if/then)

---

### H3: Duplicate/Overlap - Nested Loop Tracing Skills
**Severity**: High
**Skill IDs Affected**: T07.G6.05, T07.G6.06
**Issue**: Significant overlap between two nested loop tracing skills at same grade level.

**T07.G6.05**: "Trace nested loops using a trace table"
- Focus: Systematic trace table technique for tracking variables
- Method: Create table with columns for variables, rows for iterations

**T07.G6.06**: "Trace nested loops that generate visual patterns"
- Focus: Predict visual output from nested loops
- Method: Understanding row/column counters control position

**Analysis**:
Both are tracing skills at G6, both use nested loops, both depend on T07.G5.03 and T07.G5.04. The distinction is trace TABLE methodology vs visual OUTPUT prediction, but in practice these overlap heavily.

**Recommended Fix**:
Consider consolidating or making the distinction clearer:
- **Option A**: Merge into single skill "Trace nested loops using systematic methods (trace tables, visual prediction)"
- **Option B**: Keep separate but clarify: G6.05 focuses on METHOD (trace table as a tool), G6.06 focuses on APPLICATION (specific use case: visual patterns)
- **Preferred**: Option B with clearer descriptions emphasizing G6.05 = general technique, G6.06 = specific pattern application

---

### H4: Unclear Description - T07.G8.02
**Severity**: High
**Skill IDs Affected**: T07.G8.02
**Issue**: Description is too broad and vague for an IXL-style assessable skill.

**Current Description**:
"Students learn the general pattern of iterative algorithms - using loops to repeatedly update values until a condition is met. They identify and apply this pattern to solve various problems that require repeated calculation or testing."

**Problems**:
- "Learn the general pattern" is not assessable
- "Various problems" is not specific
- Too meta-cognitive for a single skill
- Has 3 sub-skills (T07.G8.02.01, .02, .03) that are MORE specific than the parent

**Analysis**:
The sub-skills are well-defined:
- T07.G8.02.01: GCD using repeated subtraction
- T07.G8.02.02: Prime checking with trial division
- T07.G8.02.03: Fibonacci iterative calculation

**Recommended Fix**:
Rewrite T07.G8.02 to be more specific and assessable:
"Identify when a problem requires an iterative algorithm (repeated updates until a condition is met) and select the appropriate loop structure (repeat-until, for loop, or forever with break). Given a word problem or scenario, determine if iteration is needed and what should update each loop iteration."

---

### H5: Missing Skill - for-each iteration blocks
**Severity**: High
**Skill IDs Affected**: None (missing)
**Issue**: CreatiCode has `for each item [var] in [list]` and `for each index [var] in [list]` blocks, but no skill explicitly teaches these important iteration patterns.

**Evidence**:
- Available blocks include: "for each item [var] in [list]", "for each index [var] in [list]", "for each 3D object named [var]"
- T07.G5.02 "Build a list with a loop" and T07.G6.03 "Loop-based search in a list" use loops with lists
- But no skill teaches the for-each iteration pattern specifically

**Recommended Fix**:
Add new skill **T07.G6.09** (or adjust numbering):
"Use for-each loops to iterate through lists"
- Description: Students use CreatiCode's `for each item [var] in [list]` block to process all items in a list without manually tracking an index counter. They also learn `for each index [var] in [list]` when they need both the index and the value. This pattern is cleaner than using a counter variable with `item [i] of [list]`.
- Dependencies: T07.G5.02 (Build a list with a loop), T07.G6.03 (Loop-based search in a list)
- Grade: G6 (after students understand lists and searching)

---

## MEDIUM PRIORITY ISSUES

### M1: Intra-Topic Dependency - Potential Circular Reference
**Severity**: Medium
**Skill IDs Affected**: T07.G4.07, T07.G4.03
**Issue**: T07.G4.07 depends on T07.G4.03, but the dependency path may create unnecessary coupling.

**T07.G4.03**: "Use a loop counter variable and for loops"
- G4 skill teaching counter variables and for loops

**T07.G4.07**: "Trace simple nested loops with fixed bounds"
- Depends on T07.G4.03
- But description says "fixed bounds" (constant numbers, not variables)

**Analysis**:
If T07.G4.07 uses fixed bounds (e.g., "repeat 3, repeat 2"), why does it depend on T07.G4.03 which is about VARIABLE counters? The dependency makes sense if students need to understand loop mechanics, but it may be overspecified.

**Recommended Fix**:
- **Option A**: Remove T07.G4.03 dependency if fixed-bound nested loops don't need counter variable knowledge
- **Option B**: Keep dependency but clarify in description that understanding loop counters helps trace nested loops
- **Preferred**: Option B - keep dependency, add note: "While this skill uses fixed bounds, understanding loop counter mechanics from T07.G4.03 helps students mentally track which iteration they're on in each loop."

---

### M2: Intra-Topic Dependency - Forward Reference
**Severity**: Medium
**Skill IDs Affected**: T07.G3.01
**Issue**: T07.G3.01 is the gateway skill but has dependencies on T04 pattern skills that should logically follow from T07 K-2 skills (which don't exist).

**T07.G3.01 Dependencies**:
- T06.G3.01: Build a green-flag script (makes sense)
- T04.G1.01: Match a picture pattern to a movement pattern
- T04.G2.01: Identify the repeating unit in a longer pattern
- T01.G2.05: Complete a simple if/then algorithm

**Analysis**:
Dependencies on T04.G1.01 and T04.G2.01 are pattern skills that properly prepare for loops. However, T07 should have its own K-2 foundation (see H1) that would make these T04 dependencies supplementary rather than primary.

**Recommended Fix**:
Once K-2 skills are added (per H1):
1. Add T07.K.01 or T07.G1.01 as primary dependencies to T07.G3.01
2. Keep T04 pattern dependencies as they provide complementary perspective
3. This creates multi-topic support rather than over-reliance on T04

---

### M3: Same-Grade Dependency Chain in G4
**Severity**: Medium
**Skill IDs Affected**: T07.G4.01, T07.G4.02, T07.G4.04, T07.G4.05, T07.G4.06
**Issue**: Multiple G4 skills depend on other G4 skills, creating a long same-grade dependency chain that may limit flexibility.

**Dependency Chain**:
```
T07.G4.01 ← T07.G3.05, T07.G3.03
T07.G4.02 ← T07.G3.04, T07.G3.01
T07.G4.03 ← T07.G3.05, T07.G3.01
T07.G4.04 ← T07.G3.04, T07.G3.01
T07.G4.05 ← T07.G3.04, T07.G3.01 (complex debugging)
T07.G4.06 ← T07.G3.04, T07.G3.01 (tracing)
T07.G4.07 ← T07.G4.03, T07.G4.06 (SAME GRADE CHAIN)
T07.G4.08 ← T07.G4.01, T07.G3.01
```

**Analysis**:
T07.G4.07 depends on two other G4 skills (T07.G4.03 and T07.G4.06), which is valid per X-2 rule but creates ordering constraints within G4. This is acceptable but worth noting for curriculum sequencing.

**Recommended Action**:
- No change needed (follows X-2 rule)
- Document for instructors: G4 skills should be taught in this order:
  1. T07.G4.01, .02, .03, .04, .05, .06, .08 (can be somewhat parallel)
  2. T07.G4.07 (requires .03 and .06 first)

---

### M4: Grade Progression - G5 Light on Content
**Severity**: Medium
**Skill IDs Affected**: G5 skills (T07.G5.01-04)
**Issue**: G5 has only 4 skills compared to G4's 8 and G6's 8, suggesting possible gap in progression.

**G5 Skills**:
1. T07.G5.01: Simulate repeated experiments with a loop (probability)
2. T07.G5.02: Build a list with a loop (data structures)
3. T07.G5.03: Use loops to compute aggregates (math/statistics)
4. T07.G5.04: Nested loops for advanced patterns or tilings (visual/spatial)

**Analysis**:
G5 skills are high-quality and cover diverse applications (probability, data, computation, visual). The smaller number may be intentional as G5 focuses on APPLICATIONS rather than new loop mechanics. However, other grades have more skills.

**Recommended Fix**:
Consider adding 1-2 skills:
- **Potential T07.G5.05**: "Use a loop with user input to build interactive sequences" (combines loops with T10 input skills)
- **Potential T07.G5.06**: "Trace loops that modify list items" (bridge between G5.02 list building and G6.03 list searching)

**Justification**:
- Not critical (current G5 skills are solid)
- But would create smoother progression from G4 (8 skills) → G5 (4→6) → G6 (8)

---

### M5: Skill Granularity - T07.G4.03 Too Broad
**Severity**: Medium
**Skill IDs Affected**: T07.G4.03
**Issue**: Skill teaches TWO distinct concepts: manual counter variables AND for-loops with built-in counters.

**Current T07.G4.03**:
"Students create and use a counter variable that increments on each loop iteration... They also learn to use CreatiCode's `for [variable] from (START) to (LIMIT) at step (S)` block..."

**Analysis**:
This is really two skills:
1. Manual counter pattern: Create variable, set to 0, increment in loop
2. For-loop block: Use built-in counter with start/limit/step

These are related but distinct enough to warrant separate skills for better assessment granularity.

**Recommended Fix**:
Split into:
- **T07.G4.03**: "Use a loop counter variable to track iterations"
  - Focus: Manual counter pattern (create, initialize, increment)
  - Example: Track "Step 1, Step 2, Step 3" displays

- **T07.G4.03.01**: "Use for-loops with start, limit, and step values"
  - Focus: CreatiCode's for-loop block with parameters
  - Example: Count by 2s, count down, use different ranges
  - Dependencies: T07.G4.03 (understand counter concept first)

---

### M6: Grade Progression - Jump from G6.08 to G7.01
**Severity**: Medium
**Skill IDs Affected**: T07.G7.01
**Issue**: G7.01 introduces "motion simulation" which is a significant conceptual leap from G6's topics.

**T07.G6.08**: "Use break and continue to control loop flow" (control flow)
**T07.G7.01**: "Use loops to simulate motion over time" (physics simulation)

**Analysis**:
G6 ends with advanced loop control (break/continue), then G7 suddenly introduces physics simulation. While dependencies are valid (G7.01 depends on G6.05, G6.06, G6.07), the thematic shift is abrupt.

**Recommended Fix**:
- Add bridging context in T07.G7.01 description
- Updated description: "Students implement a loop that repeatedly updates position (and optionally velocity) to simulate motion, such as an object sliding or falling with a simple rule each step. This applies the iterative update pattern from T07.G6.07 to a physics context, where each loop iteration represents one time step."

---

### M7: Missing Skill - Loop Efficiency Concepts
**Severity**: Medium
**Skill IDs Affected**: None (missing)
**Issue**: T07.G7.03 compares loop algorithms by counting steps, but there's no skill about choosing efficient loop bounds or avoiding unnecessary iterations.

**Current Related Skills**:
- T07.G7.03: Compare loop algorithms by counting steps (compares algorithms)
- T07.G8.04: Analyze and justify loop design choices (compares structures)

**Gap**:
No skill teaches students to minimize iterations within a single loop (e.g., "only loop to sqrt(n) for prime checking" or "use break to stop early when found").

**Recommended Fix**:
Add **T07.G7.05**: "Optimize loop bounds to reduce unnecessary iterations"
- Description: Students identify when a loop performs unnecessary iterations and tighten the bounds (e.g., checking divisors up to √n instead of n-1 for primality, or stopping a search loop with break once the item is found). They compare the iteration counts before and after optimization.
- Dependencies: T07.G6.08 (break/continue), T07.G7.03 (counting steps)
- Note: This is partially covered by T07.G8.02.02 (prime checking) but should be explicit

---

### M8: Dependency Concern - T07.G8.02 sub-skills
**Severity**: Medium
**Skill IDs Affected**: T07.G8.02.01, T07.G8.02.02, T07.G8.02.03
**Issue**: All three sub-skills depend ONLY on T07.G8.02, creating tight coupling. If T07.G8.02 is revised (per H4), sub-skills may need adjustment.

**Current Sub-skills**:
- T07.G8.02.01: GCD (Euclidean algorithm) - only depends on T07.G8.02
- T07.G8.02.02: Prime checking - depends on T07.G8.02 + T08.G6.01
- T07.G8.02.03: Fibonacci - depends on T07.G8.02 + T09.G6.01

**Analysis**:
If T07.G8.02's scope is narrowed (per H4 recommendation), these sub-skills might need additional dependencies or clearer connection to the revised parent skill.

**Recommended Fix**:
After revising T07.G8.02 (per H4):
1. Verify each sub-skill still aligns with parent's revised scope
2. Consider adding T07.G7.04 (loop patterns for accumulation) as dependency for sub-skills
3. Ensure sub-skills can stand alone if parent skill becomes more abstract

---

## SUMMARY OF FINDINGS

### High Priority Issues (5):
1. **H1**: Add K-2 foundational skills (CRITICAL)
2. **H2**: Verify break/continue block names
3. **H3**: Clarify nested loop tracing skill distinction (G6.05 vs G6.06)
4. **H4**: Rewrite T07.G8.02 to be more specific/assessable
5. **H5**: Add for-each iteration skill (G6.09)

### Medium Priority Issues (8):
1. **M1**: Review G4.07 dependency on G4.03
2. **M2**: Update G3.01 dependencies once K-2 skills added
3. **M3**: Document G4 skill sequencing (no changes needed)
4. **M4**: Consider adding 1-2 more G5 skills
5. **M5**: Split G4.03 into two skills (manual counter vs for-loop)
6. **M6**: Add bridging context to G7.01 description
7. **M7**: Add loop efficiency/optimization skill at G7
8. **M8**: Verify sub-skill dependencies after G8.02 revision

### Skills With No Issues Identified (18):
T07.G3.02, T07.G3.03, T07.G3.04, T07.G3.05, T07.G4.01, T07.G4.02, T07.G4.04, T07.G4.05, T07.G4.06, T07.G4.08, T07.G5.01, T07.G5.02, T07.G5.03, T07.G5.04, T07.G6.01, T07.G6.02, T07.G6.03, T07.G6.04

### Overall Assessment:
T07 has a **strong G3-G8 progression** with well-defined skills that align with CreatiCode blocks. The main gaps are:
1. Missing K-2 foundation (critical)
2. Missing for-each iteration pattern (important)
3. Some skills need description clarification for better assessment
4. Opportunity to add 2-3 more skills at G5/G7 for smoother progression

**Total Recommended Additions**: 4-6 K-2 skills + 1 G6 skill + 2-3 optional G5/G7 skills = 7-10 new skills
**Total Recommended Revisions**: 5 description updates
**Total Recommended Splits**: 1 skill (G4.03 → G4.03 + G4.03.01)
