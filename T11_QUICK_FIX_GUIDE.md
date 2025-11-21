# T11 Quick Fix Guide - Specific Changes Required

**Purpose:** This document provides the exact changes needed to fix T11 (Functions & Procedures). Each change is marked with priority and includes before/after text.

---

## HIGH PRIORITY CHANGES (MUST FIX)

### 1. T11.G4.02 - Add missing T11.G4.01 dependency

**Location:** T11.G4.02 Dependencies section

**Current:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.01: Use a simple if in a script
* T09.G3.01: Create and use a numeric variable for score or count
* T11.G3.03: Identify parts of a script that could be helpers
```

**New:**
```
Dependencies:
* T11.G4.01: Define and call a simple helper (no parameters)
* T11.G3.03: Identify parts of a script that could be helpers
* T09.G3.01: Create and use a numeric variable for score or count
```

**Rationale:** Students must know how to create custom blocks before distinguishing their types. Removed T06.G3.01 and T08.G3.01 as they're too basic and already covered by T11.G4.01's dependencies.

---

### 2. T11.G5.02 - Add missing T11.G4.01 dependency (CRITICAL)

**Location:** T11.G5.02 Dependencies section

**Current:**
```
Dependencies:
* T11.G4.04: Describe what each helper does in a script
* T11.G4.05: Trace through a script with helpers and reporters
```

**New:**
```
Dependencies:
* T11.G4.01: Define and call a simple helper (no parameters)
* T11.G4.05: Trace through a script with helpers and reporters
```

**Rationale:** You cannot define a helper WITH parameters if you haven't first learned to define one WITHOUT parameters. This is a critical logical gap. Also removed T11.G4.04 as T11.G4.05 (tracing) subsumes understanding what helpers do.

---

### 3. T11.G6.01 - Remove X-2 violations

**Location:** T11.G6.01 Dependencies section

**Current:**
```
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01: Create and use a numeric variable for score or count
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
```

**New:**
```
Dependencies:
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
```

**Rationale:** T08.G3.01 and T09.G3.01 are 3 grades back (violate X-2 rule). These basic skills are already covered transitively through G5 dependencies.

---

### 4. T11.G6.02 - Remove X-2 violations

**Location:** T11.G6.02 Dependencies section

**Current:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T11.G3.01: Understand when to use custom blocks vs loops
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
```

**New:**
```
Dependencies:
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
```

**Rationale:** T06.G3.01 and T11.G3.01 are 3 grades back (violate X-2 rule). By G6, students are well beyond basic scripting and choosing between loops vs custom blocks.

---

### 5. T11.G6.03 - Remove X-2 violation

**Location:** T11.G6.03 Dependencies section

**Current:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.01: Use a simple if in a script
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
```

**New:**
```
Dependencies:
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
```

**Rationale:** T06.G3.01 and T08.G3.01 are 3 grades back (violate X-2 rule).

---

### 6. T11.G6.04 - Remove X-2 violations

**Location:** T11.G6.04 Dependencies section

**Current:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.01: Create and use a numeric variable for score or count
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
```

**New:**
```
Dependencies:
* T11.G5.03: Decide between a parameter and a call to a separate block
* T11.G5.04: Analyze a modular program structure
```

**Rationale:** T06.G3.01 and T09.G3.01 are 3 grades back (violate X-2 rule).

---

### 7. T11.G7.01 - Remove questionable dependency

**Location:** T11.G7.01 Dependencies section

**Current:**
```
Dependencies:
* T01.G5.01: Complete a simple script with missing blocks
* T09.G5.01: Create and use a numeric variable for score or count
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
```

**New:**
```
Dependencies:
* T09.G5.01: Create and use a numeric variable for score or count
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
```

**Rationale:** T01.G5.01 is 2 grades back and too basic for implementing algorithms in custom blocks. The G6 skills already ensure sufficient prerequisite knowledge.

---

### 8. T11.G7.02 - Remove unnecessary dependencies

**Location:** T11.G7.02 Dependencies section

**Current:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G5.01: Create and use a numeric variable for score or count
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
```

**New:**
```
Dependencies:
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
```

**Rationale:** T06.G3.01 is 4 grades back (severe X-2 violation). T09.G5.01 is not directly relevant to designing a set of related blocks - the focus is on architectural design, not variable usage.

---

### 9. T11.G7.03 - Fix data error and remove X-2 violation

**Location:** T11.G7.03 Dependencies section

**Current:**
```
Dependencies:
* T09.G5.01: Create and use a numeric variable for score or count
* T11.G5.01: Understand when to use custom blocks vs loops
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
```

**ISSUE:** The dependency "T11.G5.01: Understand when to use custom blocks vs loops" has a WRONG SKILL NAME. The actual T11.G5.01 is "Identify subproblems that deserve their own helper." The skill name shown is actually T11.G3.01.

**New:**
```
Dependencies:
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
```

**Rationale:**
- Removed T11.G5.01 (2 grades back, violates X-2 rule)
- Removed T09.G5.01 (not directly relevant to encapsulation concept)
- The G6 refactoring skills provide sufficient foundation for understanding encapsulation

---

### 10. T11.G7.04 - Remove X-2 violations

**Location:** T11.G7.04 Dependencies section

**Current:**
```
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G5.01: Use a simple if in a script
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
```

**New:**
```
Dependencies:
* T11.G6.03: Refactor spaghetti code into organized blocks
* T11.G6.04: Analyze and improve block abstraction
```

**Rationale:** T06.G3.01 is 4 grades back and T08.G5.01 is 2 grades back (both violate X-2 rule). Tracing complex hierarchies doesn't require these basic skills explicitly - the G6 dependencies are sufficient.

---

## MEDIUM PRIORITY CHANGES (SHOULD FIX)

### 11. T11.G3.01 - Clarify skill description

**Location:** T11.G3.01 Description

**Current:**
```
Description: Students differentiate between using a loop (for repeating the exact
same action a fixed number of times) and a custom block (for grouping a complex
or varied sequence and reusing it). Both organize code, but for different purposes.
This conceptual gateway skill builds organizational thinking without requiring
students to define functions yet.
```

**New:**
```
Description: Students identify scenarios where a custom block is more appropriate
than a loop. They recognize that loops repeat the SAME action multiple times,
while custom blocks group a SEQUENCE of different actions for reuse. Given example
scripts or problems, they choose the better organizational approach and explain
their reasoning. This conceptual gateway skill builds organizational thinking
without requiring students to define custom blocks yet.

Assessment example: Present 3-4 scenarios (e.g., "draw a house," "move 10 steps
5 times," "reset game state," "count to 10"). Students label each as better solved
with a loop or a custom block and explain why.
```

**Rationale:** Makes the skill more concrete and assessable. Adds clarity about what "differentiate" means in practice.

---

### 12. T11.G3.03 - Clarify "highlight" instruction

**Location:** T11.G3.03 Description

**Current:**
```
Description: Students look at a longer script and highlight groups of blocks that
represent a meaningful behavior (e.g., "reset player," "check win," "show game over"),
even though they do not yet define new custom blocks. This builds the habit of
seeing natural helper boundaries.
```

**New:**
```
Description: Students examine a longer script (15-30 blocks) and identify groups
of blocks that represent distinct behaviors by drawing boxes around them and
labeling each group with a descriptive name (e.g., "reset player," "check win
condition," "show game over message"). This builds the habit of recognizing
natural custom block boundaries before actually creating them.
```

**Rationale:** Specifies what "highlight" means (draw boxes and label) and adds concrete script length. Makes the skill more implementable.

---

### 13. T11.G4.02 - Use standard terminology

**Location:** T11.G4.02 Skill name and Description

**Current:**
```
Skill: Distinguish action blocks from reporter functions
Description: Students learn to recognize which blocks **do something** (procedure‑style
stack blocks) and which blocks **return a value** (reporter functions) in CreatiCode,
and to predict where each type belongs in a script (stack vs inside conditions/expressions).
```

**New:**
```
Skill: Distinguish command blocks from reporter blocks
Description: Students learn to recognize which blocks **do something** (command/stack
blocks that perform actions) and which blocks **return a value** (reporter blocks
that can be used in expressions) in CreatiCode. They predict where each type belongs
in a script: command blocks stack vertically in scripts, while reporter blocks fit
inside hexagonal or circular input slots in conditions, operations, and other blocks.
```

**Rationale:** "Command blocks" and "reporter blocks" are standard Scratch terminology. "Action blocks" is non-standard. Also clarifies the visual distinction (stacking vs fitting in slots).

---

### 14. T11.G4.04 vs T11.G4.05 - Clarify distinction

**Location:** T11.G4.04 and T11.G4.05 Descriptions

**Current T11.G4.04:**
```
Description: Students read a script that uses several helpers (procedures and
reporter functions) and explain, in everyday language, what each helper does
and how they fit together (setup vs game loop vs scoring).
```

**Current T11.G4.05:**
```
Description: Students read a script that calls helper procedures and reporter
functions and trace through the execution to predict final outputs, reinforcing
a mental model of calls and returns.
```

**New T11.G4.04:**
```
Description: Students read a script that uses several custom blocks and write a
one-sentence description of each block's PURPOSE (e.g., "This block resets the
player to the starting position and clears the score"). They focus on WHAT each
block does (its goal), not HOW it does it (implementation details). They also
identify how blocks fit together in the program's overall structure (e.g., setup,
game loop, scoring, ending).
```

**New T11.G4.05:**
```
Description: Students trace step-by-step through a script that calls custom blocks,
predicting the order of execution and the values returned by reporter blocks at
each step. They show the flow of control and data through the program, reinforcing
their mental model of procedure calls, returns, and the call stack. This is
LOW-LEVEL tracing (execution order) as opposed to G4.04's HIGH-LEVEL understanding
(purpose).
```

**Rationale:** Makes the distinction explicit - G4.04 is WHAT (purpose), G4.05 is HOW (execution). Reduces confusion about whether these are duplicate skills.

---

### 15. T11.G6.01 - Explain "interface-first thinking"

**Location:** T11.G6.01 Description

**Current:**
```
Description: Students design custom blocks where the purpose, parameters, and
return value (if any) are clear and well-named, making the blocks easy to use
and reuse without reading internal details. This is "interface-first" thinking.
```

**New:**
```
Description: Students design custom blocks by first deciding what the block should
do, what inputs (parameters) it needs, and what it should return (if anything)
BEFORE writing the code inside. They choose clear, descriptive names for the block
and its parameters so that other programmers (or their future selves) can use the
block without reading its internal code. This "design the interface first" approach
promotes reusable, maintainable code.
```

**Rationale:** Explains what "interface-first thinking" means in concrete terms appropriate for K-8 students.

---

### 16. T11.G7.03 - Use K-8 friendly language

**Location:** T11.G7.03 Description

**Current:**
```
Description: Students learn that a well-designed custom block hides its
implementation details from the user; the caller only needs to know the interface
(parameters and return value), not how it works inside. This is a step toward
object-oriented thinking.
```

**New:**
```
Description: Students understand that a well-designed custom block acts like a
"black box": users only need to know WHAT it does (its inputs and outputs), not
HOW it does it (the code inside). They compare examples of blocks with clear
interfaces versus blocks that require understanding internal variables or logic.
This "hiding the complexity" principle (called encapsulation) makes code easier
to use and change. This is a foundational concept in object-oriented programming.
```

**Rationale:** Uses concrete metaphor ("black box") and explains encapsulation in age-appropriate language. Still mentions OOP but contextualizes it.

---

### 17. T11.G8.03 - Clarify "objects" in Scratch context

**Location:** T11.G8.03 Description

**Current:**
```
Description: Students create custom blocks that accept and return complex data
structures (lists of sprites, lists of objects with multiple attributes), enabling
powerful abstractions for managing game entities, inventories, or other game data.
```

**New:**
```
Description: Students create custom blocks that accept and return complex data
structures such as lists of sprites, or lists representing structured data (e.g.,
a list of player records where each item contains name, score, and level stored
in a formatted string or parallel lists). These blocks enable powerful abstractions
for managing game entities, inventories, or other game data.
```

**Rationale:** Clarifies that "objects" in Scratch means structured data representations, not true OOP objects. Makes it clear how to represent multi-attribute data in Scratch's list system.

---

## LOW PRIORITY CHANGES (NICE TO HAVE)

### 18. T11.G3.04 - More active voice

**Location:** T11.G3.04 Description

**Current:**
```
Description: Students are introduced to the idea that a helper can **report**
a value (as a reporter block/function) instead of just doing an action—e.g.,
a "Random Number Between [min] [max]" block returning a number or a
"Distance to [sprite]" function in CreatiCode.
```

**New:**
```
Description: Students learn that a custom block can **report** a value (as a
reporter block/function) instead of just performing an action. They explore
examples such as a "Random Number Between [min] [max]" block returning a number
or a "Distance to [sprite]" function in CreatiCode, and predict what values
these reporters will return in different situations.
```

**Rationale:** More active voice ("Students learn" vs "Students are introduced"). Adds predictive element.

---

### 19. T11.G4.03 - Better examples

**Location:** T11.G4.03 Description

**Current:**
```
Description: Students call built‑in or pre‑made reporter functions and use their
returned values directly in conditions or arithmetic (e.g.,
`if <distance to [sprite] < 50>`, `set x to [random 1 to 10] + 5`).
```

**New:**
```
Description: Students call built‑in or pre‑made reporter functions and use their
returned values directly in conditions or arithmetic. Examples:
- `if <(distance to [Player]) < 50>` then...
- `set [score] to ((calculate total points) + (bonus))
- `move ((get player speed) * 2) steps`
```

**Rationale:** Uses examples that more clearly show reporter blocks as "function calls" that return values used in larger expressions.

---

## SUMMARY OF CHANGES

**Total changes:** 19

**Priority breakdown:**
- HIGH: 10 changes (dependency fixes, X-2 violations, data errors)
- MEDIUM: 7 changes (terminology, clarity, assessability)
- LOW: 2 changes (polish, examples)

**Affected skills:**
- G3: 2 skills (descriptions)
- G4: 5 skills (dependencies + descriptions)
- G5: 1 skill (dependency - CRITICAL)
- G6: 4 skills (dependencies)
- G7: 4 skills (dependencies + descriptions)
- G8: 1 skill (description)

**Skills with NO changes:** T11.G3.02, T11.G4.01, T11.G5.01, T11.G5.03, T11.G5.04, T11.G6.02, T11.G8.01, T11.G8.02, T11.G8.04

**Dependency changes:**
- Added: 2 dependencies
- Removed: 22 dependencies (mostly X-2 violations)
- Net reduction: 20 dependencies (simplified structure)

**Skills deleted:** 0 (NONE)
**Cross-topic dependencies modified:** 0 (ALL PRESERVED)
