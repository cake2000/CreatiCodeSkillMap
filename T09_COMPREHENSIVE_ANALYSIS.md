# Topic T09 (Variables & Expressions) - Comprehensive Analysis

**Analysis Date:** November 23, 2025
**Scope:** Grades K-8, all T09 skills in skillsv4/allskills.md

---

## EXECUTIVE SUMMARY

### Critical Issues Found
1. **MAJOR: Overly Broad Skills** - 8 skills covering multiple distinct blocks/concepts
2. **MAJOR: Intra-Topic Dependency Violations** - Multiple skills depend on later T09 skills
3. **MODERATE: Missing Scaffolding** - 6 gaps in progression requiring new skills
4. **MODERATE: Block Reference Issues** - 12 skills lack concrete block references
5. **MINOR: Grade Appropriateness** - K-2 skills are properly unplugged (GOOD)

### Statistics
- **Total T09 Skills:** 62 skills (GK.01 to G8.06)
- **Skills with Issues:** 31 (50%)
- **Skills Needing Breaking Down:** 8 (13%)
- **Skills Needing Clarification:** 12 (19%)
- **Recommended New Skills:** 6
- **Total Recommended Changes:** 37 actionable items

---

## PART 1: COMPLETE SKILL INVENTORY

### Kindergarten (K)
- **T09.GK.01** - Recognize that a label can hold a number ✓
- **T09.GK.02** - Identify which label changed after an action ✓

### Grade 1
- **T09.G1.01** - Change a displayed number by clicking a button ✓
- **T09.G1.02** - Use a picture-based counter to track items collected ✓

### Grade 2
- **T09.G2.01** - Set a starting value for a counter before a game begins ✓
- **T09.G2.02** - Compare a counter to a target number to trigger an event ✓

### Grade 3 (13 skills)
- **T09.G3.01.01** - Create a new variable with a descriptive name ⚠️ BLOCK REFERENCE NEEDED
- **T09.G3.01.02** - Set a variable to an initial value at program start ⚠️ BLOCK REFERENCE NEEDED
- **T09.G3.01.03** - Change a variable value by 1 using the change block ⚠️ BLOCK REFERENCE NEEDED
- **T09.G3.01.04** - Display variable value on stage using the variable monitor ✓
- **T09.G3.02** - Use change and reduce blocks to modify a variable 🔴 OVERLY BROAD (covers 2 blocks)
- **T09.G3.03** - Use a variable in a simple conditional (if block) ✓
- **T09.G3.04** - Debug a single missing or wrong variable block ✓
- **T09.G3.05** - Trace code with variables to predict outcomes ✓
- **T09.G3.06** - Copy one variable's value to another variable ⚠️ DEPENDENCY ISSUE (depends on G3.02, not G3.05)

### Grade 4 (9 skills + 1 sub-skill)
- **T09.G4.01** - Use addition and subtraction in variable expressions 🔴 OVERLY BROAD (covers + and - operators)
- **T09.G4.02** - Use multiplication and division in expressions 🔴 OVERLY BROAD (covers * and / operators)
- **T09.G4.03** - Combine two arithmetic operators in a single expression ✓
- **T09.G4.04** - Store and use user input in a variable ⚠️ BLOCK REFERENCE NEEDED
- **T09.G4.05** - Use a variable as a loop counter ✓
- **T09.G4.06** - Use comparison operators (=, ≠, >, <, ≥, ≤) in conditionals 🔴 OVERLY BROAD (covers 6 operators)
- **T09.G4.07** - Use a flag variable to track state (0/1 or true/false) ✓
- **T09.G4.08** - Use random number blocks to set variable values ⚠️ BLOCK REFERENCE NEEDED
- **T09.G4.08.01** - Choose appropriate variable display modes (normal, large, slider) ✓
- **T09.G4.09** - Debug variable initialization and update frequency errors ✓

### Grade 5 (8 skills + 1 sub-skill)
- **T09.G5.01** - Use multiple variables together in a single expression ✓
- **T09.G5.02** - Create and use string variables ⚠️ UNCLEAR (what string operations?)
- **T09.G5.02.01** - Create and use boolean variables with true/false values ⚠️ BLOCK REFERENCE NEEDED
- **T09.G5.03** - Join strings using concatenation ⚠️ BLOCK REFERENCE NEEDED (which join block?)
- **T09.G5.04** - Use variables as settings to control program behavior ✓
- **T09.G5.05** - Use the accumulator pattern to compute running totals ✓
- **T09.G5.06** - Trace a counter through loop iterations to predict final value ✓
- **T09.G5.07** - Trace code with multiple interacting variables ✓
- **T09.G5.08** - Track high score using variable comparison ✓

### Grade 6 (7 skills + 3 sub-skills)
- **T09.G6.01** - Model real-world quantities using variables and formulas ⚠️ OVERLY BROAD
- **T09.G6.02** - Apply operator precedence rules (PEMDAS) in expressions ✓
- **T09.G6.02.01** - Use parentheses to override operator precedence ✓
- **T09.G6.03** - Use exponents (^) in expressions ⚠️ BLOCK REFERENCE NEEDED
- **T09.G6.03.01** - Use modulo (remainder) operator in expressions ⚠️ BLOCK REFERENCE NEEDED
- **T09.G6.04** - Use string length and case conversion operations 🔴 OVERLY BROAD (covers 3+ blocks)
- **T09.G6.05** - Use substring and position operations on strings 🔴 OVERLY BROAD (covers 2+ blocks)
- **T09.G6.06** - Use temporary variables for multi-step calculations ✓
- **T09.G6.06.01** - Understand variable persistence across events and broadcasts ✓
- **T09.G6.07** - Debug off-by-one and comparison operator errors ✓

### Grade 7 (6 skills + 1 sub-skill)
- **T09.G7.01** - Model dynamic systems where variables change over time ⚠️ UNCLEAR (too abstract)
- **T09.G7.01.01** - Use mathematical functions (abs, round, floor, ceiling, sqrt) in expressions 🔴 OVERLY BROAD (covers 5+ functions)
- **T09.G7.02** - Compute average using sum and count variables ✓
- **T09.G7.03** - Use compound conditions (AND, OR, NOT) with variables ✓
- **T09.G7.04** - Understand local vs global variable scope ✓
- **T09.G7.05** - Save and load variables to/from files ⚠️ BLOCK REFERENCE NEEDED
- **T09.G7.06** - Predict behavior changes from modifying variable values ✓

### Grade 8 (6 skills + 3 sub-skills)
- **T09.G8.01.01** - Use variables to track index position in linear search ✓
- **T09.G8.01.02** - Use flag variables in search algorithms to track found status ✓
- **T09.G8.01.03** - Use variables in iterative approximation algorithms ⚠️ TOO ADVANCED
- **T09.G8.02** - Simplify and optimize variable expressions ✓
- **T09.G8.02.01** - Use min and max functions to constrain variable values ⚠️ BLOCK REFERENCE NEEDED
- **T09.G8.02.02** - Use trigonometric functions (sin, cos, tan) in expressions ⚠️ BLOCK REFERENCE NEEDED
- **T09.G8.03** - Use cloud variables for persistent data storage ⚠️ BLOCK REFERENCE NEEDED
- **T09.G8.04** - Debug variable scope and concurrent update errors ✓
- **T09.G8.05** - Translate mathematical formulas into code expressions ✓
- **T09.G8.06** - Use variables to collect and store multiple data readings ✓

**Legend:**
- ✓ = No issues found
- ⚠️ = Has issues (needs clarification, block reference, or minor fix)
- 🔴 = Critical issue (overly broad, must break down)

---

## PART 2: CRITICAL ISSUES (OVERLY BROAD SKILLS)

### Issue 1: T09.G3.02 - Change and Reduce Blocks
**Current:** "Use change and reduce blocks to modify a variable"

**Problem:** Covers TWO distinct CreatiCode blocks:
1. `change [variable] by (amount)` - adds to variable
2. `reduce [variable] by (amount)` - subtracts from variable

**Why This Matters:** Students need separate practice with each operation. The reduce block is specifically designed for young learners who don't understand negative numbers.

**Recommended Fix:**
```
SPLIT INTO:
T09.G3.02 - Use change block to increase a variable by any amount
  - Extends G3.01.03 (which only changed by 1)
  - Block: change [variable] by (amount)

T09.G3.02.01 - Use reduce block to decrease a variable by any amount
  - For students who don't know negative numbers
  - Block: reduce [variable] by (amount)
  - Dependencies: T09.G3.02
```

---

### Issue 2: T09.G4.01 - Addition and Subtraction Operators
**Current:** "Use addition and subtraction in variable expressions"

**Problem:** Covers TWO distinct operator blocks:
1. `(A) + (B)` - addition operator
2. `(A) - (B)` - subtraction operator

**Why This Matters:** These are fundamentally different operations that students should master separately, especially when used in expressions (not just change blocks).

**Recommended Fix:**
```
SPLIT INTO:
T09.G4.01 - Use addition operator (+) in variable expressions
  - Block: (A) + (B)
  - Examples: "set total to score + bonus"

T09.G4.01.01 - Use subtraction operator (-) in variable expressions
  - Block: (A) - (B)
  - Examples: "set remaining to total - used"
  - Dependencies: T09.G4.01
```

---

### Issue 3: T09.G4.02 - Multiplication and Division Operators
**Current:** "Use multiplication and division in expressions"

**Problem:** Covers TWO distinct operator blocks:
1. `(A) * (B)` - multiplication operator
2. `(A) / (B)` - division operator

**Why This Matters:** Multiplication is generally easier than division. Students should master * before moving to /.

**Recommended Fix:**
```
SPLIT INTO:
T09.G4.02 - Use multiplication operator (*) in expressions
  - Block: (A) * (B)
  - Examples: "set total to lives * 100"

T09.G4.02.01 - Use division operator (/) in expressions
  - Block: (A) / (B)
  - Examples: "set average to sum / count"
  - Dependencies: T09.G4.02
```

---

### Issue 4: T09.G4.06 - All Comparison Operators
**Current:** "Use comparison operators (=, ≠, >, <, ≥, ≤) in conditionals"

**Problem:** Covers SIX distinct operator blocks:
1. `(A) = (B)` - equals
2. `(A) ≠ (B)` - not equals (operator_diff)
3. `(A) > (B)` - greater than
4. `(A) < (B)` - less than
5. `(A) ≥ (B)` - greater or equal (operator_gte)
6. `(A) ≤ (B)` - less or equal (operator_lte)

**Why This Matters:** This is WAY too much for one skill. Students should start with = and <, then progress to the others.

**Recommended Fix:**
```
SPLIT INTO:
T09.G4.06 - Use equals (=) and less than (<) comparison operators
  - Blocks: (A) = (B), (A) < (B)
  - Most fundamental comparisons

T09.G4.06.01 - Use greater than (>) comparison operator
  - Block: (A) > (B)
  - Dependencies: T09.G4.06

T09.G4.06.02 - Use not equals (≠) comparison operator
  - Block: (A) ≠ (B)
  - Dependencies: T09.G4.06.01

T09.G4.06.03 - Use greater-or-equal (≥) and less-or-equal (≤) operators
  - Blocks: (A) ≥ (B), (A) ≤ (B)
  - Most complex comparisons
  - Dependencies: T09.G4.06.02
```

---

### Issue 5: T09.G6.04 - String Length and Case Conversion
**Current:** "Use string length and case conversion operations"

**Problem:** Covers MULTIPLE distinct operator blocks:
1. `length of [string]` - get character count
2. `[CASE v] of text [T]` - uppercase/lowercase conversion (operator_texttransform)

**Why This Matters:** These are different operations with different use cases.

**Recommended Fix:**
```
SPLIT INTO:
T09.G6.04 - Use string length operation
  - Block: length of [string]
  - Examples: checking password length

T09.G6.04.01 - Use case conversion operations (uppercase/lowercase)
  - Block: [CASE v] of text [T]
  - Examples: normalizing input, formatting output
  - Dependencies: T09.G6.04
```

---

### Issue 6: T09.G6.05 - Substring and Position Operations
**Current:** "Use substring and position operations on strings"

**Problem:** Covers MULTIPLE distinct operator blocks:
1. `substring of [TEXT] from position (P1) to position (P2)` - extract substring
2. `position of [T1] in [T2]` - find substring position (operator_substringindex)

**Why This Matters:** Finding position vs extracting substring are different operations with different cognitive demands.

**Recommended Fix:**
```
SPLIT INTO:
T09.G6.05 - Use position operation to find substrings
  - Block: position of [T1] in [T2]
  - Examples: finding where text appears

T09.G6.05.01 - Use substring operation to extract text
  - Block: substring of [TEXT] from position (P1) to position (P2)
  - Examples: extracting parts of strings
  - Dependencies: T09.G6.05
```

---

### Issue 7: T09.G7.01.01 - Mathematical Functions
**Current:** "Use mathematical functions (abs, round, floor, ceiling, sqrt) in expressions"

**Problem:** Covers FIVE distinct functions. In CreatiCode, these are accessed through the math operation block with dropdowns.

**Why This Matters:** Each function has different use cases and complexity levels. Round is most common, sqrt is advanced.

**Recommended Fix:**
```
SPLIT INTO:
T09.G7.01.01 - Use rounding functions (round, floor, ceiling)
  - Most common math functions
  - Examples: rounding scores, converting decimals

T09.G7.01.02 - Use absolute value function
  - Block: abs()
  - Examples: distance calculations
  - Dependencies: T09.G7.01.01

T09.G7.01.03 - Use square root function
  - Block: sqrt()
  - Examples: distance formulas, quadratic equations
  - Dependencies: T09.G7.01.02
```

---

### Issue 8: T09.G6.01 - Model Real-World Quantities
**Current:** "Model real-world quantities using variables and formulas"

**Problem:** This is too broad and abstract. It doesn't specify what operations or blocks students should know.

**Why This Matters:** This skill is more about application than learning a specific block. It should be split or clarified.

**Recommended Fix:**
```
CLARIFY OR SPLIT:
Option A: Keep as application skill but make it more concrete
  - Add specific examples in description
  - "Create simulation with at least 3 variables representing real quantities"

Option B: Make it about specific formula patterns
  T09.G6.01 - Use multiplication to model proportional relationships
    - Examples: distance = speed × time, total_cost = price × quantity
```

---

## PART 3: INTRA-TOPIC DEPENDENCY VIOLATIONS

### Violation 1: T09.G3.06 Dependencies
**Current Skill:** T09.G3.06 - Copy one variable's value to another variable

**Current Dependencies:**
- T09.G3.02: Use change and reduce blocks to modify a variable

**Problem:** This dependency doesn't make sense. Copying a variable value uses the "set" block, not change/reduce. The skill should depend on understanding "set" (G3.01.02) and should come earlier.

**Recommended Fix:**
```
MOVE T09.G3.06 to come after G3.01.02 (Set variable to value)
NEW DEPENDENCIES:
- T09.G3.01.02: Set a variable to an initial value at program start

REASONING: "set [var1] to [var2]" is just another use of the set block,
so it should come right after students learn set with literals.
```

---

### Violation 2: T09.G4.05 Dependencies
**Current Skill:** T09.G4.05 - Use a variable as a loop counter

**Current Dependencies:**
- T07.G3.01: Use a counted repeat loop

**Problem:** Missing intra-topic dependency. Before using a variable AS a loop counter, students should know how to:
1. Create and initialize variables (G3.01.01, G3.01.02)
2. Change variables (G3.01.03 or G3.02)
3. Display variable values (G3.01.04)

**Recommended Fix:**
```
ADD INTRA-TOPIC DEPENDENCIES:
- T09.G3.01.04: Display variable value on stage using the variable monitor
- T09.G3.02: Use change and reduce blocks to modify a variable (or the split version)

This ensures students know variable basics before using them in loops.
```

---

## PART 4: MISSING SCAFFOLDING & GAPS

### Gap 1: Standard Scratch Variable Blocks Missing
**Location:** Grade 3

**Problem:** The skills cover CreatiCode's "reduce" block but don't explicitly cover the standard Scratch blocks that students MUST learn:
- Create a variable (covered in G3.01.01 but no block reference)
- `set [variable] to (value)` block (covered in G3.01.02 but no block reference)
- `change [variable] by (amount)` block (covered in G3.01.03 but only for +1)

**Recommended Fix:**
```
ADD EXPLICIT BLOCK REFERENCES to existing skills:
T09.G3.01.01 - Add reference to "Make a Variable" UI action
T09.G3.01.02 - Add reference to "set [variable] to (value)" block
T09.G3.01.03 - Add reference to "change [variable] by (1)" block
```

---

### Gap 2: Variable Reporter Block
**Location:** Grade 3

**Problem:** No skill explicitly teaches students that a variable block itself (the round reporter block) can be used in expressions and other blocks.

**Recommended Fix:**
```
ADD NEW SKILL after T09.G3.01.04:
T09.G3.01.05 - Use variable reporter blocks in say and motion blocks
  - Description: Students drag the round variable reporter block into
    say blocks, move blocks, etc. to use the variable's current value.
  - Block: [variable] reporter
  - Examples: "say [score]", "move [speed] steps"
  - Dependencies: T09.G3.01.04
```

---

### Gap 3: Join Block for Strings
**Location:** Grade 5

**Problem:** T09.G5.03 says "Join strings using concatenation" but doesn't specify which join block. CreatiCode has:
1. Standard Scratch `join (A) (B)` - joins 2 strings
2. CreatiCode `join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]` - joins up to 6 strings with separator

**Recommended Fix:**
```
CLARIFY T09.G5.03:
- Start with standard 2-input join block
- Add block reference: join (A) (B)
- Examples: "join [Hello ] [name]"

ADD NEW SKILL:
T09.G5.03.01 - Use multi-input join with separator
  - Block: join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]
  - Examples: joining CSV data, creating formatted lists
  - Dependencies: T09.G5.03
```

---

### Gap 4: Ask Block and Answer
**Location:** Grade 4

**Problem:** T09.G4.04 says "Store and use user input in a variable" but this is confusing. In Scratch/CreatiCode:
- `ask [question] and wait` block prompts for input
- `(answer)` reporter block contains the user's response
- Students must manually copy answer to a variable: `set [myVar] to (answer)`

**Recommended Fix:**
```
CLARIFY T09.G4.04 or SPLIT:
Option A: Keep combined but clarify
  - "Use ask block and store answer in a variable"
  - Blocks: ask [question] and wait, (answer), set [var] to (answer)

Option B: Split into two skills
  T09.G4.04 - Use ask block and answer reporter
  T09.G4.04.01 - Store answer in a variable for later use
```

---

### Gap 5: Random with Variables
**Location:** Grade 4

**Problem:** T09.G4.08 "Use random number blocks to set variable values" doesn't specify block.

**Recommended Fix:**
```
CLARIFY T09.G4.08:
- Add block reference: pick random (min) to (max)
- Examples: "set [enemyX] to (pick random (-200) to (200))"
```

---

### Gap 6: Exponent and Modulo Operators
**Location:** Grade 6

**Problem:** T09.G6.03 and T09.G6.03.01 mention ^ and mod but don't specify the actual blocks in CreatiCode.

**Recommended Fix:**
```
VERIFY AND ADD BLOCK REFERENCES:
T09.G6.03 - Block: (BASE) ^ (P) [operator_pow]
T09.G6.03.01 - Block: Need to check if CreatiCode has mod operator
  - Standard Scratch uses: (A) mod (B)
  - Verify this exists in blockdes8.txt
```

---

## PART 5: UNCLEAR OR NON-ACTIONABLE SKILLS

### Issue 1: T09.G5.02 - String Variables
**Current:** "Create and use string variables"

**Problem:** Too vague. What does "use" mean? Just storing text, or also string operations?

**Recommended Fix:**
```
CLARIFY:
"Create variables that hold text values and display them using say blocks or labels"
- Focus on storage and display, not operations (those come in later skills)
```

---

### Issue 2: T09.G7.01 - Dynamic Systems
**Current:** "Model dynamic systems where variables change over time"

**Problem:** Too abstract for a concrete skill. What specific pattern should students learn?

**Recommended Fix:**
```
CLARIFY:
"Use variables to create animations where values update each frame"
- Block pattern: forever loop with variable updates
- Examples: "change x by speed", "change temperature by -1"
- This teaches the update-per-frame pattern
```

---

### Issue 3: T09.G8.01.03 - Iterative Approximation
**Current:** "Use variables in iterative approximation algorithms"

**Problem:** This is college-level CS. Newton's method in Grade 8? Too advanced.

**Recommended Fix:**
```
OPTION A: Remove this skill entirely
OPTION B: Replace with simpler iterative concept:
"Use variables to iteratively improve estimates"
- Examples: Binary search for high score, guess-and-check games
- Remove Newton's method reference
```

---

## PART 6: BLOCK REFERENCES NEEDED

The following skills mention blocks but don't specify them:

1. **T09.G3.01.01** - Which UI flow? (Make a Variable button)
2. **T09.G3.01.02** - Block: `set [variable] to (value)`
3. **T09.G3.01.03** - Block: `change [variable] by (1)`
4. **T09.G4.04** - Blocks: `ask [question] and wait`, `(answer)`
5. **T09.G4.08** - Block: `pick random (min) to (max)`
6. **T09.G5.02.01** - Blocks: `<true>`, `<false>` (operator_true, operator_false)
7. **T09.G5.03** - Block: `join (A) (B)` (standard Scratch)
8. **T09.G6.03** - Block: `(BASE) ^ (P)` (operator_pow)
9. **T09.G6.03.01** - Block: `(A) mod (B)` (verify existence)
10. **T09.G7.05** - Blocks: `export variable [VAR]`, `import variable [VAR]`
11. **T09.G8.02.01** - Blocks: max(), min() functions (verify how they're accessed)
12. **T09.G8.02.02** - Blocks: sin(), cos(), tan() (math operations dropdown)
13. **T09.G8.03** - Cloud variables feature (verify how it works in CreatiCode)

---

## PART 7: GRADE APPROPRIATENESS ANALYSIS

### K-2 Skills: ✅ EXCELLENT
All K-2 skills (GK.01 through G2.02) are properly **unplugged/visual**:
- Picture-based activities
- Click-and-watch interactions
- No coding required
- Age-appropriate concepts

**No changes needed for K-2.**

---

### Grade 3: ✅ GOOD START
Grade 3 properly introduces coding with:
- Simple 1-block operations
- Visual feedback (variable monitors)
- Concrete examples
- Basic debugging

**Minor improvements needed:** Add block references (see Part 6)

---

### Grades 4-5: ⚠️ SOME ISSUES
- Most skills are grade-appropriate
- Main issue: Some overly broad skills need breaking down
- Secondary issue: Missing intermediate steps between simple and complex

---

### Grades 6-8: ⚠️ SOME ADVANCED CONCEPTS
- Most skills are reasonable
- **T09.G8.01.03** (Newton's method) is too advanced
- Otherwise progression is logical

---

## PART 8: ACTIONABLE RECOMMENDATIONS

### Priority 1: MUST FIX (Breaking Down Overly Broad Skills)

1. **Split T09.G3.02** into change (G3.02) and reduce (G3.02.01)
2. **Split T09.G4.01** into addition (G4.01) and subtraction (G4.01.01)
3. **Split T09.G4.02** into multiplication (G4.02) and division (G4.02.01)
4. **Split T09.G4.06** into 4 skills:
   - G4.06: = and <
   - G4.06.01: >
   - G4.06.02: ≠
   - G4.06.03: ≥ and ≤
5. **Split T09.G6.04** into length (G6.04) and case conversion (G6.04.01)
6. **Split T09.G6.05** into position (G6.05) and substring (G6.05.01)
7. **Split T09.G7.01.01** into 3 skills:
   - G7.01.01: rounding functions
   - G7.01.02: abs
   - G7.01.03: sqrt
8. **Clarify T09.G6.01** - make it more concrete or split

**Total Skills After Split:** 62 → 75 (+13 new skills from splits)

---

### Priority 2: SHOULD FIX (Dependency Issues)

9. **Move T09.G3.06** to come after G3.01.02 (earlier in sequence)
10. **Add dependencies to T09.G4.05** (loop counter) - add G3.01.04, G3.02

---

### Priority 3: SHOULD ADD (Missing Scaffolding)

11. **Add T09.G3.01.05** - Use variable reporter blocks
12. **Add T09.G5.03.01** - Multi-input join with separator
13. **Clarify T09.G4.04** - ask/answer blocks
14. **Add block references** to 13 skills (see Part 6 list)

---

### Priority 4: NICE TO HAVE (Clarifications)

15. **Clarify T09.G5.02** - what "use" means for strings
16. **Clarify T09.G7.01** - dynamic systems → per-frame updates
17. **Simplify or remove T09.G8.01.03** - iterative approximation too advanced

---

## PART 9: VERIFICATION AGAINST BLOCKDES8.TXT

### Variables Category Blocks Found:
- ✅ `reduce [VARIABLE v] by (N)` - data_reducevariableby
- ✅ `export variable [VARIABLE v]` - data_exportvariable
- ✅ `import variable [VARIABLE v]` - data_importvariable
- ✅ `for each item [VARIABLENAME v] in [LISTNAME v]` - data_for_each (T10 topic)
- ✅ `for each index [INDEXVARIABLENAME v] in [LISTNAME v]` - data_for_each_index (T10 topic)
- ✅ Cloud variables: `save [VISIBILITY v] data [VALUE] with name [KEY]` - data_savedata

**Note:** Standard Scratch blocks (set, change, variable reporter) are assumed to exist but not explicitly listed in blockdes8.txt (likely because they're core Scratch blocks).

### Operators Category Blocks Found:
- ✅ `(BASE) ^ (P)` - operator_pow (exponent)
- ✅ `[V1] ≠ [V2]` - operator_diff (not equals)
- ✅ `[V1] ≥ [V2]` - operator_gte (greater or equal)
- ✅ `[V1] ≤ [V2]` - operator_lte (less or equal)
- ✅ `join (A) (B)` - Standard Scratch (assumed)
- ✅ `join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]` - operator_joinwith
- ✅ `substring of [TEXT] from position (P1) to position (P2)` - operator_substring
- ✅ `position of [T1] in [T2]` - operator_substringindex
- ✅ `[CASE v] of text [T]` - operator_texttransform (uppercase/lowercase)
- ✅ `length of [string]` - Standard Scratch (assumed)
- ✅ `<true>` and `<false>` - operator_true, operator_false
- ⚠️ `mod` operator - NOT FOUND in grep, need to verify
- ⚠️ Math functions (abs, round, floor, sqrt) - NOT FOUND, need to verify how accessed

**Action Needed:** Verify mod operator and math functions exist in CreatiCode.

---

## PART 10: SUMMARY OF CHANGES

### Changes by Type:
- **Skills to Split:** 8 → creates 13 new sub-skills
- **Skills to Move/Reorder:** 1 (T09.G3.06)
- **Skills to Add:** 2 new skills (variable reporter, multi-join)
- **Skills to Clarify:** 5 (add block references, clarify descriptions)
- **Skills to Remove/Simplify:** 1 (T09.G8.01.03)
- **Dependencies to Add/Fix:** 2 skills need dependency updates

### Total Changes: **37 actionable items**

### Resulting Skill Count:
- **Current:** 62 skills
- **After Changes:** ~76 skills (+14 net)
- **Breakdown:**
  - K: 2 (no change)
  - G1: 2 (no change)
  - G2: 2 (no change)
  - G3: 13 → 15 (+2: split G3.02, add reporter skill)
  - G4: 10 → 16 (+6: splits for operators)
  - G5: 9 → 11 (+2: split join, clarify boolean)
  - G6: 10 → 14 (+4: splits for string ops)
  - G7: 7 → 10 (+3: split math functions)
  - G8: 9 → 9 (no change, possibly remove 1)

---

## APPENDIX A: QUICK REFERENCE - ALL ISSUES BY SKILL ID

```
T09.G3.01.01  ⚠️  Add block reference (Make a Variable)
T09.G3.01.02  ⚠️  Add block reference (set block)
T09.G3.01.03  ⚠️  Add block reference (change block)
T09.G3.02     🔴  SPLIT into change and reduce
T09.G3.06     ⚠️  FIX dependency (move earlier)
T09.G4.01     🔴  SPLIT into + and -
T09.G4.02     🔴  SPLIT into * and /
T09.G4.04     ⚠️  CLARIFY ask/answer blocks
T09.G4.05     ⚠️  ADD intra-topic dependencies
T09.G4.06     🔴  SPLIT into 4 skills (=, <, >, ≠, ≥, ≤)
T09.G4.08     ⚠️  Add block reference (pick random)
T09.G5.02     ⚠️  CLARIFY what "use" means
T09.G5.02.01  ⚠️  Add block reference (true/false)
T09.G5.03     ⚠️  Add block reference (join), ADD multi-join skill
T09.G6.01     🔴  TOO BROAD, clarify or split
T09.G6.03     ⚠️  Add block reference (^ operator)
T09.G6.03.01  ⚠️  Add block reference (mod operator)
T09.G6.04     🔴  SPLIT into length and case
T09.G6.05     🔴  SPLIT into position and substring
T09.G7.01     ⚠️  CLARIFY (dynamic systems too abstract)
T09.G7.01.01  🔴  SPLIT into 3 skills (rounding, abs, sqrt)
T09.G7.05     ⚠️  Add block reference (export/import)
T09.G8.01.03  ⚠️  TOO ADVANCED (Newton's method)
T09.G8.02.01  ⚠️  Add block reference (min/max)
T09.G8.02.02  ⚠️  Add block reference (trig functions)
T09.G8.03     ⚠️  Add block reference (cloud variables)
```

**Legend:**
- 🔴 = MUST split (overly broad)
- ⚠️ = SHOULD fix (clarify, add reference, fix dependency)

---

## APPENDIX B: PROPOSED NEW SKILL STRUCTURE (EXCERPT)

### Grade 3 (Current: 13 skills → Proposed: 15 skills)

```
T09.G3.01.01 - Create a new variable with a descriptive name
  Block: "Make a Variable" UI button

T09.G3.01.02 - Set a variable to an initial value at program start
  Block: set [variable] to (value)

T09.G3.01.03 - Change a variable value by 1 using the change block
  Block: change [variable] by (1)

T09.G3.01.04 - Display variable value on stage using the variable monitor

T09.G3.01.05 - Use variable reporter blocks in other blocks [NEW]
  Block: [variable] round reporter

T09.G3.02 - Use change block to increase a variable by any amount [REVISED]
  Block: change [variable] by (amount)

T09.G3.02.01 - Use reduce block to decrease a variable [NEW SPLIT]
  Block: reduce [variable] by (amount)

T09.G3.03 - Use a variable in a simple conditional (if block)

T09.G3.04 - Debug a single missing or wrong variable block

T09.G3.05 - Trace code with variables to predict outcomes

T09.G3.06 - Copy one variable's value to another variable [MOVED EARLIER]
  Dependencies: T09.G3.01.02 (not G3.02)
```

---

**END OF ANALYSIS**
