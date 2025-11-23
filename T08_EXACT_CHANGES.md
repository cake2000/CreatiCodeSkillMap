# T08 Phase 1 Optimization - EXACT CHANGES

## HIGH PRIORITY FIXES

### H1: ADD NEW SKILL T08.G3.03b

**Action:** Insert new skill between T08.G3.03 and T08.G3.04

**New Skill:**
```
ID: T08.G3.03b
Topic: T08 – Conditions & Logic
Skill: Build a simple if/else block
Description: Students add their first `if/else` block to handle two distinct outcomes (e.g., "if touching goal, say 'You win!', else say 'Keep going!'"). This introduces the two-branch conditional structure where both paths execute different actions. Use scenarios with clear either/or outcomes that require different responses for each branch.

Dependencies:
* T08.G3.03: Pick the right conditional block for a scenario
* T07.G3.02: Trace a script with a simple loop

CSTA: E3-ALG-AF-01, E3-PRO-PF-01
```

**Cascade Changes:**
- Update T08.G3.04 dependencies: Remove T08.G3.03, T07.G3.03; Add T08.G3.03b

---

### H2: FIX T08.G4.09 DEPENDENCY

**Current:**
```
Dependencies:
* T08.G3.04: Trace code with a single if/else
* T08.G4.05: Use else-if for multiple exclusive conditions
```

**Change to:**
```
Dependencies:
* T08.G3.04: Trace code with a single if/else
```

**Rationale:** Sequential if/else blocks are conceptually simpler than else-if chains. Students should learn to trace sequential blocks before exclusive conditionals.

---

### H3: REWRITE T08.G3.02 DESCRIPTION

**Current:**
```
Description: Students read very simple scenarios (e.g., "move only when the space key is pressed" vs "jump only if touching the ground AND space is pressed") and identify whether a single condition is enough or multiple conditions are needed. This builds conceptual understanding of condition complexity without requiring students to write complex logic yet. Use concrete, visual examples.
```

**Change to:**
```
Description: Students identify simple scenarios where an action should happen only when one condition is true (e.g., "move when space key is pressed" or "say 'Good!' when touching star"). This builds conceptual understanding of when to use a simple if block through concrete, visual examples. Students practice recognizing single-condition situations in game and animation contexts.
```

**Rationale:** Remove references to compound conditions (AND) which students haven't learned yet. Focus purely on understanding single-condition logic.

---

### H4: (Originally separate, now merged with H3)
**Status:** Resolved by H3 fix

---

### H5: REMOVE REDUNDANT DEPENDENCY FROM T08.G4.01

**Current:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.01: Use a simple if in a script
* T08.G3.05: Fix a condition that uses the wrong comparison operator
```

**Change to:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.05: Fix a condition that uses the wrong comparison operator
```

**Rationale:** T08.G3.01 is already implied through T08.G3.05's dependency chain.

---

### H6: FIX T08.G4.02 DEPENDENCIES

**Current:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.05: Fix a condition that uses the wrong comparison operator
* T09.G3.01.04: Display variable value on stage using the variable monitor
```

**Change to:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G4.01: Combine two conditions with AND
* T09.G3.01.04: Display variable value on stage using the variable monitor
```

**Rationale:** Students should learn AND before OR. This creates proper sequencing. T08.G3.05 becomes redundant since T08.G4.01 already depends on it.

---

### H7: ADD DEPENDENCY TO T08.G4.04

**Current:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.05: Fix a condition that uses the wrong comparison operator
```

**Change to:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G4.01: Combine two conditions with AND
```

**Rationale:** Students should understand compound conditions before learning nesting, so they can compare the two approaches. T08.G3.05 becomes redundant since T08.G4.01 already depends on it.

---

## MEDIUM PRIORITY FIXES

### M1: CLARIFY T08.G4.03 DESCRIPTION

**Current:**
```
Description: Students read code with AND/OR expressions and predict which branch runs for given inputs, building comfort with compound logic before debugging or refactoring. This skill develops the ability to mentally evaluate complex boolean expressions.
```

**Change to:**
```
Description: Students read code with compound expressions (AND and/or OR) and predict which branch runs for given inputs, building comfort with compound logic before debugging or refactoring. This skill develops the ability to mentally evaluate complex boolean expressions combining multiple conditions.
```

**Rationale:** Clarify that OR may or may not be included yet, since this skill only depends on AND.

---

### M5: REMOVE REDUNDANT DEPENDENCY FROM T08.G5.05

**Current:**
```
Dependencies:
* T08.G5.01: Design multi-branch decision logic
* T08.G4.06: Convert nested if to cleaner logic
```

**Change to:**
```
Dependencies:
* T08.G5.01: Design multi-branch decision logic
```

**Rationale:** T08.G5.01 already depends on T08.G4.06, making the second dependency redundant.

---

## LOW PRIORITY FIXES (OPTIONAL)

### L2: ENHANCE T08.G4.06 DESCRIPTION (OPTIONAL)

**Current:**
```
Description: Students are given deeply nested or redundant if/else code and refactor it using AND, OR, or else-if to make it cleaner and more readable. This skill requires understanding compound conditions and else-if patterns, developing code quality and maintainability awareness.
```

**Proposed Enhancement:**
```
Description: Students are given deeply nested or redundant if/else code and refactor it using AND, OR, or else-if to reduce nesting depth and improve readability. This skill requires understanding compound conditions and else-if patterns, developing code quality and maintainability awareness. Students learn that compound conditions and else-if patterns often simplify complex nested structures.
```

**Rationale:** Make "cleaner" more concrete by specifying "reduce nesting depth."

---

## VERIFICATION NEEDED

### V1: VERIFY T08.G8.01 DEPENDENCY ON T04.G6.01

**Current:**
```
Dependencies:
* T04.G6.01: Group snippets by underlying algorithm pattern
* T08.G6.01: Use conditionals to control simulation steps
* T08.G7.01: Reason about fairness using conditions
* T08.G7.02: Design tests for condition-heavy code
```

**Question:** Is T04.G6.01 necessary for logical equivalence? Seems tangential.

**Action:** Review whether T04.G6.01 adds value or could be removed.

---

## IMPLEMENTATION ORDER

1. **First:** Add new skill T08.G3.03b (H1)
2. **Second:** Update all dependencies (H2, H5, H6, H7, M5)
3. **Third:** Update descriptions (H3, M1)
4. **Fourth:** Optional enhancements (L2)
5. **Fifth:** Verify cross-topic dependencies (V1)

---

## AFFECTED SKILLS SUMMARY

### Skills with Changes:
1. **T08.G3.03b** - NEW SKILL (insert after T08.G3.03)
2. **T08.G3.02** - Description rewrite
3. **T08.G3.04** - Dependency change
4. **T08.G4.01** - Dependency removal
5. **T08.G4.02** - Dependency change
6. **T08.G4.03** - Description clarification
7. **T08.G4.04** - Dependency change
8. **T08.G4.09** - Dependency removal
9. **T08.G5.05** - Dependency removal
10. **(Optional) T08.G4.06** - Description enhancement

### Skills with No Changes:
- All K-2 skills (GK.01-02, G1.01-03, G2.01-03) ✓
- T08.G3.01, T08.G3.03, T08.G3.05 ✓
- T08.G4.05, T08.G4.07, T08.G4.08 ✓
- All G5 skills except T08.G5.05 ✓
- All G6 skills ✓
- All G7 skills ✓
- All G8 skills (pending V1 verification) ✓

---

## COMPLETE UPDATED SKILL LIST (AFFECTED SKILLS ONLY)

### T08.G3.02 (UPDATED DESCRIPTION)
```
ID: T08.G3.02
Topic: T08 – Conditions & Logic
Skill: Decide when a single if is enough
Description: Students identify simple scenarios where an action should happen only when one condition is true (e.g., "move when space key is pressed" or "say 'Good!' when touching star"). This builds conceptual understanding of when to use a simple if block through concrete, visual examples. Students practice recognizing single-condition situations in game and animation contexts.

Dependencies:
* T08.G3.01: Use a simple if in a script

CSTA: E3-ALG-AF-01
```

### T08.G3.03b (NEW SKILL)
```
ID: T08.G3.03b
Topic: T08 – Conditions & Logic
Skill: Build a simple if/else block
Description: Students add their first `if/else` block to handle two distinct outcomes (e.g., "if touching goal, say 'You win!', else say 'Keep going!'"). This introduces the two-branch conditional structure where both paths execute different actions. Use scenarios with clear either/or outcomes that require different responses for each branch.

Dependencies:
* T08.G3.03: Pick the right conditional block for a scenario
* T07.G3.02: Trace a script with a simple loop

CSTA: E3-ALG-AF-01, E3-PRO-PF-01
```

### T08.G3.04 (UPDATED DEPENDENCIES)
```
ID: T08.G3.04
Topic: T08 – Conditions & Logic
Skill: Trace code with a single if/else
Description: Students trace a short script with one simple `if/else` block and a given condition to predict which branch runs and what happens. This develops code reading and prediction skills by following the execution path through a two-branch conditional structure.

Dependencies:
* T08.G3.03b: Build a simple if/else block
* T07.G3.03: Build a forever loop for simple animation

CSTA: E3-ALG-AF-01, E3-PRO-PF-01
```

### T08.G4.01 (UPDATED DEPENDENCIES)
```
ID: T08.G4.01
Topic: T08 – Conditions & Logic
Skill: Combine two conditions with AND
Description: Students use a compound condition (AND) to check if two things are true at the same time before acting (e.g., "if key pressed AND touching goal, then complete level"). This is their first time writing boolean logic operators in code, introducing logical conjunction.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.05: Fix a condition that uses the wrong comparison operator

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

### T08.G4.02 (UPDATED DEPENDENCIES)
```
ID: T08.G4.02
Topic: T08 – Conditions & Logic
Skill: Combine two conditions with OR
Description: Students use OR to check if at least one of two conditions is true (e.g., "if score > 100 OR lives == 0, then end game"). This introduces logical disjunction and helps students understand when to use OR vs AND in compound conditions.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G4.01: Combine two conditions with AND
* T09.G3.01.04: Display variable value on stage using the variable monitor

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

### T08.G4.03 (UPDATED DESCRIPTION)
```
ID: T08.G4.03
Topic: T08 – Conditions & Logic
Skill: Trace code with compound conditionals
Description: Students read code with compound expressions (AND and/or OR) and predict which branch runs for given inputs, building comfort with compound logic before debugging or refactoring. This skill develops the ability to mentally evaluate complex boolean expressions combining multiple conditions.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G4.01: Combine two conditions with AND

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

### T08.G4.04 (UPDATED DEPENDENCIES)
```
ID: T08.G4.04
Topic: T08 – Conditions & Logic
Skill: Nest if/else statements
Description: Students write nested if/else blocks where an else branch contains another if (e.g., checking weather type, then checking temperature). This models multi-step decision-making and introduces hierarchical conditional structures.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G4.01: Combine two conditions with AND

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

### T08.G4.09 (UPDATED DEPENDENCIES)
```
ID: T08.G4.09
Topic: T08 – Conditions & Logic
Skill: Trace code with a sequence of if/else blocks
Description: Students trace code with 2-3 sequential `if/else` blocks and predict the final output for a given set of conditions. This develops the ability to track program state through multiple consecutive decision points.

Dependencies:
* T08.G3.04: Trace code with a single if/else

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

### T08.G5.05 (UPDATED DEPENDENCIES)
```
ID: T08.G5.05
Topic: T08 – Conditions & Logic
Skill: Use inline if-then-else expressions to compute conditional values
Description: Students use CreatiCode's inline conditional expression reporter block (`if <condition> then [value1] else [value2]`) to compute values conditionally without using full if/else control blocks. This is useful for setting variables or parameters based on a condition in a single expression (e.g., `set speed to (if fast mode then 10 else 5)`). This introduces the ternary operator concept and promotes more concise code.

Dependencies:
* T08.G5.01: Design multi-branch decision logic

CSTA: E5-ALG-AF-01, E5-PRO-PF-01
```

---

## VALIDATION CHECKLIST

After implementing changes, verify:
- [ ] T08.G3.03b inserted in correct position (after T08.G3.03, before T08.G3.04)
- [ ] All dependency changes applied correctly
- [ ] No circular dependencies created
- [ ] All skills still follow X-2 rule
- [ ] Cross-topic dependencies (T06, T07, T09) preserved
- [ ] CSTA standards preserved for all skills
- [ ] Skill IDs remain unchanged (except new T08.G3.03b)
- [ ] All descriptions maintain consistent tone and format
