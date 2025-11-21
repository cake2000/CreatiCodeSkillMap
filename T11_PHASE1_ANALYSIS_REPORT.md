# T11 (Functions & Procedures) - Phase 1 Optimization Analysis

**Analysis Date:** 2025-11-20
**Topic:** T11 - Functions & Procedures
**Grade Range:** G3-G8 (26 skills total)
**Focus:** Internal optimization only - no cross-topic modifications

---

## EXECUTIVE SUMMARY

Topic T11 demonstrates a generally well-structured progression from basic custom block concepts in G3 to advanced modular design in G8. However, several critical issues exist:

1. **HIGH PRIORITY:** Multiple X-2 rule violations (dependencies spanning 4+ grades)
2. **HIGH PRIORITY:** Missing critical prerequisite skill (G4.01) from many G4-G5 skills
3. **MEDIUM PRIORITY:** Inconsistent skill descriptions and unclear terminology
4. **MEDIUM PRIORITY:** Suboptimal dependency structure creating unnecessary complexity
5. **LOW PRIORITY:** Minor wording improvements for clarity

---

## COMPLETE T11 SKILL INVENTORY

### Grade 3 (4 skills - Foundation)
1. **T11.G3.01** - Understand when to use custom blocks vs loops
2. **T11.G3.02** - Use a pre-made helper block with parameters
3. **T11.G3.03** - Identify parts of a script that could be helpers
4. **T11.G3.04** - Understand the concept of return values

### Grade 4 (5 skills - Creation & Understanding)
5. **T11.G4.01** - Define and call a simple helper (no parameters)
6. **T11.G4.02** - Distinguish action blocks from reporter functions
7. **T11.G4.03** - Use a block's result in a calculation
8. **T11.G4.04** - Describe what each helper does in a script
9. **T11.G4.05** - Trace through a script with helpers and reporters

### Grade 5 (4 skills - Parameterization & Analysis)
10. **T11.G5.01** - Identify subproblems that deserve their own helper
11. **T11.G5.02** - Define a simple helper with one parameter
12. **T11.G5.03** - Decide between a parameter and a call to a separate block
13. **T11.G5.04** - Analyze a modular program structure

### Grade 6 (4 skills - Design & Refactoring)
14. **T11.G6.01** - Design blocks with clear, predictable interfaces
15. **T11.G6.02** - Create modular programs with multiple custom blocks
16. **T11.G6.03** - Refactor spaghetti code into organized blocks
17. **T11.G6.04** - Analyze and improve block abstraction

### Grade 7 (4 skills - Advanced Techniques)
18. **T11.G7.01** - Use custom blocks to implement algorithms
19. **T11.G7.02** - Design a set of related blocks for a subsystem
20. **T11.G7.03** - Understand encapsulation and data hiding
21. **T11.G7.04** - Trace and debug complex block hierarchies

### Grade 8 (4 skills - Architecture & Trade-offs)
22. **T11.G8.01** - Design blocks for a game or simulation framework
23. **T11.G8.02** - Refactor a complex program into a well-organized block hierarchy
24. **T11.G8.03** - Use custom blocks with complex data (lists, objects)
25. **T11.G8.04** - Analyze trade-offs in modular vs. monolithic design

---

## CROSS-TOPIC DEPENDENCIES (PRESERVED)

The following skills from OTHER topics depend on T11 skills. These dependencies are PRESERVED and will NOT be modified:

1. **T14.G3.07** (2D Games - Switch to game mode) → depends on T11.G3.01
2. **T14.G3.10** (2D Games - Visual effects on interaction) → depends on T11.G3.02
3. **T15.G3.07** (Stories & Animation - Wait between actions) → depends on T11.G3.01
4. **T15.G3.09** (Stories & Animation - Key press animation) → depends on T11.G3.02
5. **T18.G3.08** (3D Worlds - Trace a short 3D script) → depends on T11.G3.01

**Analysis:** These cross-topic dependencies are appropriate. They correctly reference foundational T11 skills at grade 3, which aligns with the X-2 rule for G3 skills in other topics.

---

## HIGH PRIORITY ISSUES

### ISSUE H1: Critical X-2 Rule Violations

**Severity:** HIGH - Violates fundamental skill map design principle
**Impact:** 8 skills affected

#### H1.1: T11.G7.03 depends on T11.G5.01 (2 grades back, violates X-2)

**Current:**
```
T11.G7.03: Understand encapsulation and data hiding
Dependencies:
* T09.G5.01: Create and use a numeric variable for score or count
* T11.G5.01: Understand when to use custom blocks vs loops  ← PROBLEM
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
```

**Issue:** T11.G5.01 is 2 grades below G7, violating X-2 rule (should only depend on G7, G6, or G5).

**Additional Issue:** The dependency name "T11.G5.01: Understand when to use custom blocks vs loops" appears to be a COPY ERROR. The actual T11.G5.01 skill is "Identify subproblems that deserve their own helper." The referenced skill is actually T11.G3.01.

**Fix:**
- Remove T11.G5.01 dependency (or if it's meant to reference T11.G3.01, that's even worse - 4 grades back)
- T11.G6.03 and T11.G6.04 already provide sufficient coverage
- Encapsulation concepts are introduced through refactoring experience

#### H1.2: T11.G6.01 depends on skills that are too low-level

**Current:**
```
T11.G6.01: Design blocks with clear, predictable interfaces
Dependencies:
* T08.G3.01: Use a simple if in a script  ← 3 grades back
* T09.G3.01: Create and use a numeric variable for score or count  ← 3 grades back
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
```

**Issue:** Dependencies on G3 skills from G6 violate X-2 rule.

**Fix:**
- Remove T08.G3.01 and T09.G3.01
- These are too fundamental and should be transitively covered by G5 skills
- T11.G5.03 and T11.G5.04 are sufficient prerequisites

#### H1.3: T11.G6.02 depends on T11.G3.01 (3 grades back)

**Current:**
```
T11.G6.02: Create modular programs with multiple custom blocks
Dependencies:
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T11.G3.01: Understand when to use custom blocks vs loops  ← PROBLEM
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
```

**Issue:** T11.G3.01 is 3 grades below G6.

**Fix:**
- Remove T11.G3.01 dependency
- T11.G5.03 and T11.G5.04 already ensure students understand custom block organization

#### H1.4: All G6 skills depend on T06.G3.01 (3 grades back)

**Current:** T11.G6.02, T11.G6.03, T11.G6.04 all depend on T06.G3.01

**Issue:** This basic sequencing skill from G3 is too far back for G6.

**Fix:**
- Remove T06.G3.01 from all G6 skills
- Replace with more appropriate G5 dependencies where needed
- Basic scripting is assumed by G6

#### H1.5: T11.G7.01 depends on T01.G5.01 (2 grades back but wrong topic)

**Current:**
```
T11.G7.01: Use custom blocks to implement algorithms
Dependencies:
* T01.G5.01: Complete a simple script with missing blocks  ← 2 grades back
* T09.G5.01: Create and use a numeric variable for score or count
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
```

**Issue:** T01.G5.01 is a basic algorithm concept from 2 grades back. While not technically violating X-2, it's unnecessarily low-level for G7.

**Fix:**
- Consider removing T01.G5.01 as G6 skills should cover this
- Or replace with a more advanced algorithm skill if one exists at G6-G7

#### H1.6: G8 skills depend on G6 skills but skip G7 skills

**Current:** All G8 skills (T11.G8.01-G8.04) depend on:
```
* T11.G6.01: Design blocks with clear, predictable interfaces
* T11.G7.03: Understand encapsulation and data hiding
* T11.G7.04: Trace and debug complex block hierarchies
```

**Issue:** They depend on T11.G6.01 (2 grades back) but not on more relevant G7 skills like T11.G7.01 or T11.G7.02.

**Fix:**
- This is ACCEPTABLE under X-2 rule but suboptimal
- Consider whether T11.G7.01 or T11.G7.02 would be more appropriate than T11.G6.01

---

### ISSUE H2: Missing Critical Prerequisite (T11.G4.01)

**Severity:** HIGH - Logical progression gap
**Impact:** 10 skills affected

**Problem:** T11.G4.01 "Define and call a simple helper (no parameters)" is the FIRST skill where students actually CREATE a custom block. However, many subsequent skills do not depend on it, even though they require this foundational ability.

#### H2.1: T11.G4.02 should depend on T11.G4.01

**Current:**
```
T11.G4.02: Distinguish action blocks from reporter functions
Dependencies:
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T08.G3.01: Use a simple if in a script
* T09.G3.01: Create and use a numeric variable for score or count
* T11.G3.03: Identify parts of a script that could be helpers
```

**Issue:** Student needs to have created custom blocks (T11.G4.01) before distinguishing types.

**Fix:** Add T11.G4.01 as a dependency.

#### H2.2: T11.G5.02 should depend on T11.G4.01

**Current:**
```
T11.G5.02: Define a simple helper with one parameter
Dependencies:
* T11.G4.04: Describe what each helper does in a script
* T11.G4.05: Trace through a script with helpers and reporters
```

**Issue:** Students need to know how to create a basic custom block (T11.G4.01) before adding parameters.

**Fix:** Add T11.G4.01 as a dependency. This is critical - you can't define a helper with parameters if you haven't defined one without parameters first.

#### H2.3: T11.G6.02, G6.03, G6.04 should depend on creation skills

**Issue:** These skills involve creating and modifying custom blocks but don't explicitly require T11.G4.01 or T11.G5.02.

**Fix:** Ensure dependency chain includes creation skills, not just analysis skills.

---

### ISSUE H3: Incorrect Skill Reference in Dependencies

**Severity:** HIGH - Data integrity error
**Impact:** 1 skill

**Problem:** T11.G7.03 lists a dependency as "T11.G5.01: Understand when to use custom blocks vs loops" but the actual T11.G5.01 skill is "Identify subproblems that deserve their own helper."

**Analysis:** This is either:
1. A copy-paste error where the skill name is wrong, OR
2. The dependency ID is wrong and should reference T11.G3.01

**Fix:** Verify the correct dependency and update either the ID or the name to match.

---

## MEDIUM PRIORITY ISSUES

### ISSUE M1: Inconsistent Terminology

**Severity:** MEDIUM - Affects clarity
**Impact:** Multiple skills

#### M1.1: "Helper" vs "Custom Block" vs "Procedure" vs "Function"

**Observation:** The skills use multiple terms somewhat inconsistently:
- "Helper block" (most common)
- "Custom block" (also common)
- "Procedure" (used in topic name but rarely in skills)
- "Function" (used interchangeably with reporter)
- "Reporter function" (used to distinguish from procedures)

**Current Pattern:**
- G3: "helper block"
- G4: Mix of "helper" and "custom block"
- G5-G6: More use of "custom block"
- G7-G8: "Custom blocks" dominates

**Recommendation:**
- Standardize on "custom block" as the primary term (aligns with Scratch terminology)
- Use "helper" as a casual synonym but not in skill names
- Reserve "procedure" for G7+ when discussing procedural abstraction formally
- Use "reporter" or "reporter function" consistently for value-returning blocks

#### M1.2: Unclear distinction between "action" and "procedure"

**In T11.G4.02:** "action blocks" vs "reporter functions"

**Issue:** "Action blocks" is not standard Scratch terminology. The correct term is "stack blocks" or "command blocks" in Scratch, though "procedure" is the CS concept.

**Recommendation:** Update to "command blocks (procedures)" for clarity.

---

### ISSUE M2: Skill Descriptions Need Clarification

**Severity:** MEDIUM - Affects implementation
**Impact:** 5 skills

#### M2.1: T11.G3.01 - Too conceptual without clear deliverable

**Current:**
```
Skill: Understand when to use custom blocks vs loops
Description: Students differentiate between using a loop (for repeating the exact
same action a fixed number of times) and a custom block (for grouping a complex
or varied sequence and reusing it). Both organize code, but for different purposes.
This conceptual gateway skill builds organizational thinking without requiring
students to define functions yet.
```

**Issue:**
- How do we assess "understand"?
- The description focuses on DIFFERENCES but doesn't give clear scenarios
- The loop description is limited ("fixed number of times") - what about repeat-until?

**Recommendation:**
```
Description: Students identify scenarios where a custom block is more appropriate
than a loop. They recognize that loops repeat the SAME action multiple times,
while custom blocks group a SEQUENCE of different actions for reuse. Given example
scripts, they choose the better organizational approach and explain why.

Assessment: Present 3-4 scenarios (e.g., "draw a house," "move 10 steps 5 times,"
"reset game state," "count to 10"). Students label each as better solved with a
loop or a custom block and explain their reasoning.
```

#### M2.2: T11.G3.03 - "Highlight" is vague

**Current:**
```
Skill: Identify parts of a script that could be helpers
Description: Students look at a longer script and highlight groups of blocks that
represent a meaningful behavior (e.g., "reset player," "check win," "show game over"),
even though they do not yet define new custom blocks.
```

**Issue:** "Highlight" is vague. Do they literally use a highlighter? Circle? Label?

**Recommendation:**
```
Description: Students examine a longer script (15-30 blocks) and identify groups
of blocks that represent distinct behaviors by drawing boxes around them and
labeling each group with a descriptive name (e.g., "reset player," "check win
condition," "show game over message"). This builds the habit of recognizing
natural helper block boundaries before creating them.
```

#### M2.3: T11.G4.04 vs T11.G4.05 - Too similar

**Current:**
```
T11.G4.04: Describe what each helper does in a script
T11.G4.05: Trace through a script with helpers and reporters
```

**Issue:** These feel like they could be the same skill. Both involve understanding what helpers do.

**Analysis:**
- G4.04 is about HIGH-LEVEL description (what is the purpose)
- G4.05 is about LOW-LEVEL tracing (step-by-step execution)

**Recommendation:** Make the distinction clearer in descriptions:

```
T11.G4.04 Description: Students read a script that uses several custom blocks
and write a one-sentence description of each block's PURPOSE (e.g., "This block
resets the player to the starting position and clears the score"). They focus
on WHAT each block does, not HOW.

T11.G4.05 Description: Students trace a script that calls custom blocks
step-by-step, predicting the order of execution and the values returned by
reporter blocks. They show the flow of control and data through the program,
reinforcing their mental model of procedure calls and returns.
```

#### M2.4: T11.G6.01 - "Interface-first thinking" undefined

**Current:**
```
Description: Students design custom blocks where the purpose, parameters, and
return value (if any) are clear and well-named, making the blocks easy to use
and reuse without reading internal details. This is "interface-first" thinking.
```

**Issue:** "Interface-first thinking" is jargon that needs explanation for K-8.

**Recommendation:**
```
Description: Students design custom blocks by first deciding what the block should
do, what inputs it needs, and what it should return (if anything) BEFORE writing
the code inside. They choose clear, descriptive names for the block and its
parameters so that other programmers (or their future selves) can use the block
without reading its internal code. This "design the interface first" approach
promotes reusable, maintainable code.
```

#### M2.5: T11.G7.03 - "Encapsulation" and "data hiding" need K-8 friendly language

**Current:**
```
Skill: Understand encapsulation and data hiding
Description: Students learn that a well-designed custom block hides its
implementation details from the user; the caller only needs to know the interface
(parameters and return value), not how it works inside. This is a step toward
object-oriented thinking.
```

**Issue:** While appropriate for G7, could be more concrete.

**Recommendation:**
```
Description: Students understand that a well-designed custom block acts like a
"black box": users only need to know WHAT it does (its inputs and outputs), not
HOW it does it (the code inside). They compare examples of blocks with clear
interfaces versus blocks that require understanding internal variables or logic.
This "hiding the complexity" principle makes code easier to use and change.
This is a foundational idea in object-oriented programming.
```

---

### ISSUE M3: Missing Intermediate Skills

**Severity:** MEDIUM - Learning gap
**Impact:** G5-G6 transition

#### M3.1: Jump from one parameter (G5) to multiple parameters/blocks (G6)

**Current Progression:**
- G5.02: Define a simple helper with one parameter
- G6.01: Design blocks with clear, predictable interfaces (implies multiple parameters)
- G6.02: Create modular programs with multiple custom blocks

**Issue:** No explicit skill for "define a helper with 2-3 parameters" between G5 and G6.

**Recommendation:** Consider adding a skill at early G6 like:
```
T11.G6.0X: Define a custom block with multiple parameters
Description: Students create custom blocks that accept 2-3 parameters of
different types (numbers, text, booleans) and use them appropriately inside the
block. They understand how parameter order and naming affect usability.
Dependencies: T11.G5.02, T11.G5.03
```

However, this may be implicitly covered by G6.01. If so, make it explicit in G6.01's description.

---

### ISSUE M4: Dependency Redundancy

**Severity:** MEDIUM - Complexity
**Impact:** Multiple skills

#### M4.1: All G5 skills depend on both G4.04 AND G4.05

**Current:**
```
T11.G5.02, G5.03, G5.04 all depend on:
* T11.G4.04: Describe what each helper does in a script
* T11.G4.05: Trace through a script with helpers and reporters
```

**Analysis:**
- G4.05 likely subsumes G4.04 (tracing requires understanding what each block does)
- Having both is redundant

**Recommendation:**
- Keep only T11.G4.05 as the dependency for G5 skills
- OR clarify that G4.04 is about high-level purpose while G4.05 is about low-level execution

---

## LOW PRIORITY SUGGESTIONS

### ISSUE L1: Wording Improvements

#### L1.1: T11.G3.04 - "Introduced to the idea" is passive

**Current:** "Students are introduced to the idea that..."

**Suggestion:** "Students learn that a custom block can return a value..."

#### L1.2: T11.G4.03 - Example could be clearer

**Current:** `set x to [random 1 to 10] + 5`

**Suggestion:** Use a more obviously "function-like" example:
```
set [score] to (calculate total points) + 100
if <(distance to [Player]) < 50> then...
```

#### L1.3: T11.G8.03 - "Objects" may not exist in Scratch

**Current:** "lists of objects with multiple attributes"

**Issue:** Scratch doesn't have objects in the traditional sense.

**Suggestion:** "lists of sprites, or lists representing structured data (e.g., a list of player records where each record includes name, score, and level)"

---

### ISSUE L2: Grade Distribution

**Observation:** T11 has exactly 4 skills per grade (G5-G8) and slightly uneven in G3-G4.
- G3: 4 skills
- G4: 5 skills
- G5-G8: 4 skills each

**Analysis:** This is actually well-balanced. G4 having 5 skills makes sense as it's the transition from understanding to creation.

**Recommendation:** No change needed.

---

### ISSUE L3: CreatiCode-Specific Features

**Observation:** Most skills are generic to Scratch/block-based programming. Only a few mention CreatiCode-specific features.

**Examples:**
- T11.G3.04 mentions "Distance to [sprite] function in CreatiCode"
- T11.G8.03 mentions "lists of sprites, lists of objects"

**Recommendation:**
- Verify that CreatiCode supports custom blocks with parameters (it should, as it's based on Scratch)
- Verify reporter blocks work as described
- Add more CreatiCode-specific examples if relevant (e.g., server-side custom functions)

**Action:** This should be verified against the actual CreatiCode codebase, but is low priority for Phase 1.

---

## RECOMMENDED CHANGES SUMMARY

### High Priority Fixes (Must Do)

1. **Fix X-2 violations:**
   - T11.G7.03: Remove T11.G5.01 dependency (or fix if it's a wrong reference)
   - T11.G6.01: Remove T08.G3.01 and T09.G3.01 dependencies
   - T11.G6.02: Remove T11.G3.01 dependency
   - T11.G6.02, G6.03, G6.04: Remove T06.G3.01 dependencies
   - T11.G7.01: Consider removing T01.G5.01 dependency

2. **Add missing T11.G4.01 dependencies:**
   - Add to T11.G4.02
   - Add to T11.G5.02 (CRITICAL)
   - Verify G6+ skills have proper creation skill dependencies

3. **Fix data integrity error:**
   - T11.G7.03: Correct the skill name/ID mismatch for the dependency

### Medium Priority Improvements (Should Do)

4. **Standardize terminology:**
   - Use "custom block" consistently in skill names
   - Use "command blocks (procedures)" instead of "action blocks"
   - Reserve "reporter" for value-returning blocks

5. **Clarify skill descriptions:**
   - T11.G3.01: Add concrete assessment criteria
   - T11.G3.03: Clarify "highlight" means
   - T11.G4.04 vs G4.05: Emphasize high-level vs low-level distinction
   - T11.G6.01: Explain "interface-first thinking"
   - T11.G7.03: Use K-8 friendly language for encapsulation

6. **Simplify dependencies:**
   - Consider consolidating G4.04 and G4.05 dependencies in G5 skills

### Low Priority Enhancements (Could Do)

7. **Polish descriptions:**
   - Make language more active
   - Update examples to be more clear
   - Ensure Scratch/CreatiCode alignment

---

## VERIFICATION CHECKLIST

Before finalizing changes, verify:

- [ ] No T11 skill has been deleted
- [ ] All cross-topic dependencies (T14, T15, T18) are preserved
- [ ] All within-T11 dependencies follow X-2 rule (max 2 grades back)
- [ ] All skills that involve CREATING custom blocks depend on T11.G4.01
- [ ] All skills that involve PARAMETERS depend on T11.G5.02
- [ ] Skill descriptions use consistent terminology
- [ ] Each skill has a clear, assessable learning objective
- [ ] Grade progression is logical (G3 foundation → G8 advanced)

---

## IMPLEMENTATION NOTES

**Phase 1 Scope:** This analysis focuses ONLY on T11 internal structure and dependencies. No changes to other topics will be made in Phase 1.

**Phase 2 Considerations:** After T11 is optimized, Phase 2 should:
- Review whether other topics should depend on improved T11 skills
- Consider whether T11 should depend on more advanced skills from other topics
- Validate learning progression across all topics

**Testing Recommendations:**
- Have students attempt skills in order to verify progression
- Ensure assessments align with skill descriptions
- Validate that CreatiCode features support all described blocks/functions

---

## APPENDIX A: COMPLETE DEPENDENCY GRAPH

### Within-T11 Dependencies

```
G3 Skills (Foundation - no T11 dependencies):
  T11.G3.01 ← [cross-topic only]
  T11.G3.02 ← T11.G3.01
  T11.G3.03 ← T11.G3.02
  T11.G3.04 ← T11.G3.03

G4 Skills (Creation & Understanding):
  T11.G4.01 ← T11.G3.04
  T11.G4.02 ← T11.G3.03
  T11.G4.03 ← T11.G3.04
  T11.G4.04 ← T11.G3.04
  T11.G4.05 ← T11.G3.03, T11.G3.04

G5 Skills (Parameterization):
  T11.G5.01 ← T11.G4.05
  T11.G5.02 ← T11.G4.04, T11.G4.05
  T11.G5.03 ← T11.G4.04, T11.G4.05
  T11.G5.04 ← T11.G4.04, T11.G4.05

G6 Skills (Design):
  T11.G6.01 ← T11.G5.03, T11.G5.04
  T11.G6.02 ← T11.G3.01, T11.G5.03, T11.G5.04  [G3.01 violates X-2]
  T11.G6.03 ← T11.G5.03, T11.G5.04
  T11.G6.04 ← T11.G5.03, T11.G5.04

G7 Skills (Advanced):
  T11.G7.01 ← T11.G6.03, T11.G6.04
  T11.G7.02 ← T11.G6.03, T11.G6.04
  T11.G7.03 ← T11.G5.01, T11.G6.03, T11.G6.04  [G5.01 violates X-2 + name error]
  T11.G7.04 ← T11.G6.03, T11.G6.04

G8 Skills (Architecture):
  T11.G8.01 ← T11.G6.01, T11.G7.03, T11.G7.04
  T11.G8.02 ← T11.G6.01, T11.G7.03, T11.G7.04
  T11.G8.03 ← T11.G6.01, T11.G7.03, T11.G7.04
  T11.G8.04 ← T11.G6.01, T11.G7.03, T11.G7.04
```

### Cross-Topic Dependencies (FROM other topics TO T11)

```
T14.G3.07 → T11.G3.01
T14.G3.10 → T11.G3.02
T15.G3.07 → T11.G3.01
T15.G3.09 → T11.G3.02
T18.G3.08 → T11.G3.01
```

---

## APPENDIX B: PROPOSED NEW DEPENDENCY STRUCTURE

### High-Priority Fixed Skills

**T11.G4.02** (ADD T11.G4.01):
```
Dependencies:
* T11.G4.01: Define and call a simple helper (no parameters)  [NEW]
* T11.G3.03: Identify parts of a script that could be helpers
* T09.G3.01: Create and use a numeric variable for score or count
```

**T11.G5.02** (ADD T11.G4.01):
```
Dependencies:
* T11.G4.01: Define and call a simple helper (no parameters)  [NEW - CRITICAL]
* T11.G4.05: Trace through a script with helpers and reporters
```

**T11.G6.01** (REMOVE G3 skills):
```
Dependencies:
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
[REMOVED: T08.G3.01, T09.G3.01]
```

**T11.G6.02** (REMOVE T11.G3.01):
```
Dependencies:
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
[REMOVED: T06.G3.01, T11.G3.01]
```

**T11.G6.03** (REMOVE T06.G3.01):
```
Dependencies:
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
[REMOVED: T06.G3.01]
```

**T11.G6.04** (REMOVE T06.G3.01, T09.G3.01):
```
Dependencies:
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
[REMOVED: T06.G3.01, T09.G3.01]
```

**T11.G7.01** (REMOVE T01.G5.01):
```
Dependencies:
* T09.G5.01: Create and use a numeric variable for score or count
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
[REMOVED: T01.G5.01]
```

**T11.G7.02** (REMOVE T06.G3.01, T09.G5.01):
```
Dependencies:
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
[REMOVED: T06.G3.01, T09.G5.01]
```

**T11.G7.03** (FIX wrong skill reference + REMOVE violating dependency):
```
Dependencies:
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
[REMOVED: T09.G5.01, T11.G5.01 (wrong skill name/ID)]
```

**T11.G7.04** (REMOVE T06.G3.01, T08.G5.01):
```
Dependencies:
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
[REMOVED: T06.G3.01, T08.G5.01]
```

---

## APPENDIX C: SKILLS WITHOUT T11 DEPENDENCIES (FOUNDATION)

These G3 skills are the entry points to T11 and only depend on other topics:

**T11.G3.01:**
```
Dependencies:
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T07.G3.02: Trace a script with a simple loop
* T01.G3.12: Predict the final state of a simple algorithm
```

All other T11 skills depend (directly or transitively) on T11.G3.01.

---

## CONCLUSION

Topic T11 is well-conceived and generally well-structured, but requires targeted fixes to:
1. Eliminate X-2 rule violations
2. Add missing prerequisite dependencies (especially T11.G4.01)
3. Fix data integrity errors
4. Clarify skill descriptions and terminology

These changes will strengthen the internal consistency of T11 and ensure a logical, teachable progression from Grade 3 to Grade 8.

**Estimated Impact:**
- 8 skills will have dependencies removed (X-2 fixes)
- 2 skills will have dependencies added (T11.G4.01)
- 5 skill descriptions will be clarified
- 1 data integrity error will be fixed

**No skills will be deleted. All cross-topic dependencies will be preserved.**
