# T09 (Variables & Expressions) - Complete Skill Index

## PURPOSE
This document provides a complete navigable index of all 59 T09 skills with their descriptions, dependencies, and status flags.

---

## GRADE K (2 skills) - Picture-Based Variable Concepts

### T09.GK.01 ✓
**Skill:** Recognize that a label can hold a number
**Type:** Picture-based matching
**Dependencies:** T01.GK.01
**Status:** ✅ Good
**Notes:** Entry point for variable concepts

### T09.GK.02 ✓
**Skill:** Identify which label changed after an action
**Type:** Before/after comparison
**Dependencies:** T09.GK.01
**Status:** ✅ Good
**Notes:** Introduces change detection

---

## GRADE 1 (2 skills) - Interactive Counter Concepts

### T09.G1.01 ✓
**Skill:** Change a displayed number by clicking a button
**Type:** Interactive counter
**Dependencies:** T09.GK.02, T03.G1.01
**Status:** ✅ Good
**Notes:** Light digital interaction, not block coding

### T09.G1.02 ✓
**Skill:** Use a picture-based counter to track items collected
**Type:** Collection tracking
**Dependencies:** T09.G1.01
**Status:** ✅ Good
**Notes:** Practical counter application

---

## GRADE 2 (2 skills) - Counter Initialization & Comparison

### T09.G2.01 ✓
**Skill:** Set a starting value for a counter before a game begins
**Type:** Initialization concept
**Dependencies:** T09.G1.02
**Status:** ✅ Good
**Notes:** Introduces starting state

### T09.G2.02 ✓
**Skill:** Compare a counter to a target number to trigger an event
**Type:** Threshold concept
**Dependencies:** T09.G2.01, T08.G2.01
**Status:** ✅ Good
**Notes:** Connects variables to conditionals

---

## GRADE 3 (6 skills) - First Block-Based Variables

### T09.G3.01.01 ✓
**Skill:** Create a new variable with a descriptive name
**Type:** Variable creation
**Dependencies:** T09.G2.02, T03.G2.01
**Status:** ✅ Good
**Notes:** First block-based variable skill

### T09.G3.01.02 ✓
**Skill:** Set a variable to an initial value at program start
**Type:** Variable initialization
**Dependencies:** T09.G3.01.01
**Status:** ✅ Good
**Notes:** Teaches "set to" block

### T09.G3.01.03 ⚠️
**Skill:** Change a variable value by 1 using the change block
**Type:** Variable modification
**Dependencies:** T09.G3.01.02
**Status:** ⚠️ **H1: Overlaps with G3.02** - Consider merging into G3.01.04
**Notes:** Teaches "change by 1"

### T09.G3.01.04 ✓
**Skill:** Display variable value on stage using the variable monitor
**Type:** Variable display
**Dependencies:** T09.G3.01.03
**Status:** ✅ Good (may merge with G3.01.03 per H1)
**Notes:** Many skills depend on this (136+ references)

### T09.G3.02 ⚠️
**Skill:** Use change and reduce blocks to modify a variable
**Type:** Variable modification
**Dependencies:** T09.G3.01.04
**Status:** ⚠️ **H1: Overlaps with G3.01.03** - Clarify distinction
**Notes:** Extends change to any amount + reduce

### T09.G3.03 ✓
**Skill:** Use a variable in a simple conditional (if block)
**Type:** Variables in conditionals
**Dependencies:** T09.G3.02, T08.G3.02
**Status:** ✅ Good
**Notes:** Connects variables to logic

### T09.G3.04 ✓
**Skill:** Debug a single missing or wrong variable block
**Type:** Debugging
**Dependencies:** T09.G3.03
**Status:** ✅ Good
**Notes:** Entry-level debugging

### T09.G3.05 ✓
**Skill:** Trace code with variables to predict outcomes
**Type:** Code tracing
**Dependencies:** T09.G3.04, T08.G3.04
**Status:** ✅ Good
**Notes:** Reading comprehension skill

### [PROPOSED] T09.G3.06 🆕
**Skill:** Copy a value from one variable to another
**Type:** Variable-to-variable assignment
**Dependencies:** T09.G3.01.04
**Status:** 🆕 **H3: NEW SKILL NEEDED** - Missing scaffolding
**Notes:** Should be added between G3.05 and G4

---

## GRADE 4 (10 skills) - Expressions & Operators

### T09.G4.01 ✓
**Skill:** Use addition and subtraction in variable expressions
**Type:** Arithmetic expressions
**Dependencies:** T09.G3.02, T09.G3.05
**Status:** ✅ Good
**Notes:** First expression skill

### T09.G4.02 ✓
**Skill:** Use multiplication and division in expressions
**Type:** Arithmetic expressions
**Dependencies:** T09.G4.01
**Status:** ✅ Good
**Notes:** Extends operators

### T09.G4.03 ✓
**Skill:** Combine two arithmetic operators in a single expression
**Type:** Compound expressions
**Dependencies:** T09.G4.02
**Status:** ✅ Good
**Notes:** Pre-cursor to precedence

### T09.G4.04 ✓
**Skill:** Store and use user input in a variable
**Type:** External input
**Dependencies:** T06.G3.02, T09.G3.03
**Status:** ✅ Good
**Notes:** Practical input handling

### T09.G4.05 ✓
**Skill:** Use a variable as a loop counter
**Type:** Loop counter pattern
**Dependencies:** T07.G3.01, T09.G3.02
**Status:** ✅ Good
**Notes:** Classic for-loop pattern

### T09.G4.06 ✓
**Skill:** Use comparison operators (=, ≠, >, <, ≥, ≤) in conditionals
**Type:** Comparison operators
**Dependencies:** T09.G3.03, T09.G3.05
**Status:** ✅ Good
**Notes:** All six comparisons

### T09.G4.07 ✓
**Skill:** Use a flag variable to track state (0/1 or true/false)
**Type:** State tracking
**Dependencies:** T09.G3.03, T09.G3.04
**Status:** ✅ Good
**Notes:** Boolean-like pattern with numbers

### T09.G4.08 ⚠️
**Skill:** Use random number blocks to set variable values
**Type:** Random values
**Dependencies:** T09.G3.01.02
**Status:** ⚠️ **M1: Disconnected from progression** - Add G4.01 dependency
**Notes:** Should integrate with expressions

### T09.G4.08.01 ✓
**Skill:** Choose appropriate variable display modes (normal, large, slider)
**Type:** UI/Display
**Dependencies:** T09.G3.01.04
**Status:** ✅ Good
**Notes:** CreatiCode-specific feature

### T09.G4.09 ✓
**Skill:** Debug variable initialization and update frequency errors
**Type:** Debugging
**Dependencies:** T07.G3.01, T09.G3.04, T09.G4.05
**Status:** ✅ Good
**Notes:** More complex debugging than G3.04

---

## GRADE 5 (9 skills) - Multiple Variables & Patterns

### T09.G5.01 ✓
**Skill:** Use multiple variables together in a single expression
**Type:** Multi-variable expressions
**Dependencies:** T09.G4.03, T09.G4.09
**Status:** ✅ Good
**Notes:** Variables referencing each other

### T09.G5.02 ✓
**Skill:** Create and use string variables
**Type:** String variables
**Dependencies:** T09.G4.04
**Status:** ✅ Good
**Notes:** First non-numeric variable type

### T09.G5.02.01 ✓
**Skill:** Create and use boolean variables with true/false values
**Type:** Boolean variables
**Dependencies:** T09.G4.07
**Status:** ✅ Good
**Notes:** True booleans vs. 0/1 flags

### T09.G5.03 ✓
**Skill:** Join strings using concatenation
**Type:** String operations
**Dependencies:** T09.G5.02
**Status:** ✅ Good
**Notes:** String manipulation

### T09.G5.04 ⚠️
**Skill:** Use variables as settings to control program behavior
**Type:** Configuration variables
**Dependencies:** T09.G4.09
**Status:** ⚠️ **M2: Description vague** - Clarify config vs. state
**Notes:** Pre-cursor to function parameters

### T09.G5.05 ✓
**Skill:** Use the accumulator pattern to compute running totals
**Type:** Accumulator pattern
**Dependencies:** T09.G4.05, T09.G4.09
**Status:** ✅ Good
**Notes:** Critical algorithmic pattern

### T09.G5.06 ⚠️
**Skill:** Trace a counter through loop iterations to predict final value
**Type:** Code tracing
**Dependencies:** T09.G3.05, T09.G4.05
**Status:** ⚠️ **H2: Redundant dependency** - Remove G3.05
**Notes:** Loop-specific tracing

### T09.G5.07 ✓
**Skill:** Trace code with multiple interacting variables
**Type:** Code tracing
**Dependencies:** T09.G5.01, T09.G5.06
**Status:** ✅ Good
**Notes:** Complex tracing skill

### T09.G5.08 ✓
**Skill:** Track high score using variable comparison
**Type:** Conditional update
**Dependencies:** T09.G4.06, T09.G5.05
**Status:** ✅ Good (add G3.06 dependency when created per H3)
**Notes:** Classic high score pattern

---

## GRADE 6 (10 skills) - Complex Math & Strings

### T09.G6.01 ✓
**Skill:** Model real-world quantities using variables and formulas
**Type:** Mathematical modeling
**Dependencies:** T09.G5.05, T09.G5.07
**Status:** ✅ Good
**Notes:** Real-world applications

### T09.G6.02 ⚠️
**Skill:** Apply operator precedence rules (PEMDAS) in expressions
**Type:** Operator precedence
**Dependencies:** T09.G5.01, T09.G5.07
**Status:** ⚠️ **M3: Redundant dependency** - Remove G5.01
**Notes:** PEMDAS / order of operations

### T09.G6.03 ✓
**Skill:** Use exponents (^) in expressions
**Type:** Arithmetic operators
**Dependencies:** T09.G6.02
**Status:** ✅ Good
**Notes:** Power operator

### T09.G6.03.01 ✓
**Skill:** Use modulo (remainder) operator in expressions
**Type:** Arithmetic operators
**Dependencies:** T09.G6.02
**Status:** ✅ Good
**Notes:** Mod for cycling, odd/even

### T09.G6.04 ✓
**Skill:** Use string length and case conversion operations
**Type:** String operations
**Dependencies:** T09.G5.03
**Status:** ✅ Good
**Notes:** String analysis

### T09.G6.05 ✓
**Skill:** Use substring and position operations on strings
**Type:** String operations
**Dependencies:** T09.G6.04
**Status:** ✅ Good
**Notes:** String parsing

### T09.G6.06 ✓
**Skill:** Use temporary variables for multi-step calculations
**Type:** Intermediate variables
**Dependencies:** T09.G5.05, T09.G6.02
**Status:** ✅ Good
**Notes:** Code organization pattern

### T09.G6.06.01 ⚠️
**Skill:** Understand variable persistence across events and broadcasts
**Type:** Variable scope/lifetime
**Dependencies:** T09.G5.04
**Status:** ⚠️ **L3: Low assessability** - Consider rewriting for actions
**Notes:** Cross-event coordination

### T09.G6.07 ✓
**Skill:** Debug off-by-one and comparison operator errors
**Type:** Debugging
**Dependencies:** T09.G4.09, T09.G5.07
**Status:** ✅ Good
**Notes:** Classic debugging patterns

---

## GRADE 7 (7 skills) - Systems & Scope

### T09.G7.01 ✓
**Skill:** Model dynamic systems where variables change over time
**Type:** Simulations
**Dependencies:** T09.G6.01, T09.G6.06
**Status:** ✅ Good
**Notes:** Animation and physics

### T09.G7.01.01 ✓
**Skill:** Use mathematical functions (abs, round, floor, ceiling, sqrt) in expressions
**Type:** Math functions
**Dependencies:** T09.G6.03
**Status:** ✅ Good
**Notes:** Built-in functions

### T09.G7.02 ✓
**Skill:** Compute average using sum and count variables
**Type:** Statistical computation
**Dependencies:** T09.G5.05, T09.G6.06
**Status:** ✅ Good
**Notes:** Data analysis pattern

### T09.G7.03 ⚠️
**Skill:** Use compound conditions (AND, OR, NOT) with variables
**Type:** Boolean logic
**Dependencies:** T09.G5.08, T09.G6.07
**Status:** ⚠️ **M4: Possible T08 overlap** - Verify with T08 analysis
**Notes:** May duplicate T08 content

### T09.G7.04 ✓
**Skill:** Understand local vs global variable scope
**Type:** Variable scope
**Dependencies:** T09.G5.04, T09.G6.01
**Status:** ✅ Good
**Notes:** Multi-sprite coordination

### T09.G7.05 ✓
**Skill:** Save and load variables to/from files
**Type:** File I/O
**Dependencies:** T09.G7.04
**Status:** ✅ Good
**Notes:** Data persistence

### T09.G7.06 ✓
**Skill:** Predict behavior changes from modifying variable values
**Type:** Analysis
**Dependencies:** T09.G6.07, T09.G7.01
**Status:** ✅ Good
**Notes:** What-if analysis

---

## GRADE 8 (9 skills) - Algorithms & Advanced Features

### T09.G8.01.01 ✓
**Skill:** Use variables to track index position in linear search
**Type:** Search algorithms
**Dependencies:** T09.G7.03, T09.G7.06
**Status:** ✅ Good
**Notes:** Classic algorithm

### T09.G8.01.02 ✓
**Skill:** Use flag variables in search algorithms to track found status
**Type:** Search algorithms
**Dependencies:** T09.G8.01.01
**Status:** ✅ Good
**Notes:** Search termination pattern

### T09.G8.01.03 ✓
**Skill:** Use variables in iterative approximation algorithms
**Type:** Approximation algorithms
**Dependencies:** T09.G8.01.02
**Status:** ✅ Good
**Notes:** Advanced algorithms

### T09.G8.02 ✓
**Skill:** Simplify and optimize variable expressions
**Type:** Code optimization
**Dependencies:** T09.G6.03, T09.G7.06
**Status:** ✅ Good
**Notes:** Refactoring skill

### T09.G8.02.01 ✓
**Skill:** Use min and max functions to constrain variable values
**Type:** Math functions
**Dependencies:** T09.G7.01.01
**Status:** ✅ Good
**Notes:** Clamping/bounds

### T09.G8.02.02 ✓
**Skill:** Use trigonometric functions (sin, cos, tan) in expressions
**Type:** Math functions
**Dependencies:** T09.G7.01.01
**Status:** ✅ Good
**Notes:** Advanced math

### T09.G8.03 ✓
**Skill:** Use cloud variables for persistent data storage
**Type:** Cloud storage
**Dependencies:** T09.G7.04, T09.G7.05
**Status:** ✅ Good
**Notes:** CreatiCode feature

### T09.G8.04 ✓
**Skill:** Debug variable scope and concurrent update errors
**Type:** Debugging
**Dependencies:** T09.G7.04, T09.G7.06
**Status:** ✅ Good
**Notes:** Advanced debugging

### T09.G8.05 ⚠️
**Skill:** Translate mathematical formulas into code expressions
**Type:** Formula translation
**Dependencies:** T09.G6.03, T09.G7.02, T09.G7.03
**Status:** ⚠️ **L4: Review 3 dependencies** - G7.03 may be unnecessary
**Notes:** Capstone skill

### T09.G8.06 ✓
**Skill:** Use variables to collect and store multiple data readings
**Type:** Data collection
**Dependencies:** T09.G7.02, T09.G8.01.01
**Status:** ✅ Good
**Notes:** Scientific data pattern

---

## STATISTICS BY CATEGORY

### By Grade Level
- K: 2 skills (3.4%)
- G1: 2 skills (3.4%)
- G2: 2 skills (3.4%)
- G3: 6 skills (10.2%)
- G4: 10 skills (16.9%)
- G5: 9 skills (15.3%)
- G6: 10 skills (16.9%)
- G7: 7 skills (11.9%)
- G8: 9 skills (15.3%)

### By Type
- Variable Creation/Basics: 8 skills
- Arithmetic Expressions: 7 skills
- String Operations: 5 skills
- Tracing/Analysis: 6 skills
- Debugging: 4 skills
- Patterns (counter, accumulator, flag): 6 skills
- Mathematical Functions: 4 skills
- Algorithms: 5 skills
- Scope/Persistence: 4 skills
- Advanced Features: 5 skills
- Other: 5 skills

### By Status
- ✅ Good: 52 skills (88.1%)
- ⚠️ Issues: 7 skills (11.9%)
- 🆕 New: 1 skill (proposed)

---

## CROSS-REFERENCES

### Skills with Cross-Topic Dependencies (Incoming from other topics)
- T09.GK.01 ← T01.GK.01
- T09.G1.01 ← T03.G1.01
- T09.G2.02 ← T08.G2.01
- T09.G3.01.01 ← T03.G2.01
- T09.G3.03 ← T08.G3.02
- T09.G3.05 ← T08.G3.04
- T09.G4.04 ← T06.G3.02
- T09.G4.05 ← T07.G3.01
- T09.G4.09 ← T07.G3.01

### Highly Referenced Skills (Many dependencies pointing to them)
- **T09.G3.01.04**: 136+ cross-topic references (gateway skill)
- T09.G3.02: Multiple G4 skills depend on it
- T09.G5.05: Referenced by G6-G7 skills (accumulator pattern)
- T09.G7.04: Referenced by G8 scope skills

---

## LEGEND

- ✅ **Good**: No issues identified
- ⚠️ **Issues**: Has identified problems (see analysis)
- 🆕 **New**: Proposed new skill
- **H#**: High priority issue
- **M#**: Medium priority issue
- **L#**: Low priority issue

---

## NAVIGATION TIPS

1. Use Ctrl+F to find specific skill IDs
2. Status symbols (✅⚠️🆕) help identify problem areas
3. Cross-references section shows topic integration points
4. Statistics provide overview of topic structure
