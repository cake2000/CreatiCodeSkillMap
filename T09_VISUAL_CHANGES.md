# T09 Variables & Expressions - Visual Changes Summary

## Before and After Comparison

### GRADE 3: Before (13 skills) → After (15 skills)

#### BEFORE:
```
T09.G3.01.01 - Create a new variable with a descriptive name
T09.G3.01.02 - Set a variable to an initial value at program start
T09.G3.01.03 - Change a variable value by 1 using the change block
T09.G3.01.04 - Display variable value on stage using the variable monitor
T09.G3.02 - Use change and reduce blocks to modify a variable ⚠️ OVERLY BROAD
T09.G3.03 - Use a variable in a simple conditional (if block)
T09.G3.04 - Debug a single missing or wrong variable block
T09.G3.05 - Trace code with variables to predict outcomes
T09.G3.06 - Copy one variable's value to another variable ⚠️ WRONG POSITION
```

#### AFTER:
```
T09.G3.01.01 - Create a new variable with a descriptive name
  └─ Block: "Make a Variable" UI button ✓ ADDED

T09.G3.01.02 - Set a variable to an initial value at program start
  └─ Block: set [variable] to (value) ✓ ADDED

T09.G3.01.03 - Change a variable value by 1 using the change block
  └─ Block: change [variable] by (1) ✓ ADDED

T09.G3.01.04 - Display variable value on stage using the variable monitor

T09.G3.01.05 - Use variable reporter blocks in other blocks ✨ NEW
  └─ Block: [variable] round reporter
  └─ Examples: say [score], move [speed] steps

T09.G3.02 - Use change block to increase a variable by any amount 🔧 REVISED
  └─ Block: change [variable] by (amount)
  └─ Extends G3.01.03 to arbitrary amounts

T09.G3.02.01 - Use reduce block to decrease a variable ✨ NEW SPLIT
  └─ Block: reduce [variable] by (amount)
  └─ For students who don't know negative numbers

T09.G3.03 - Use a variable in a simple conditional (if block)

T09.G3.04 - Debug a single missing or wrong variable block

T09.G3.05 - Trace code with variables to predict outcomes

T09.G3.06 - Copy one variable's value to another variable 🔧 MOVED
  └─ NOW depends on G3.01.02 (set block), not G3.02
  └─ Block: set [var1] to [var2]
```

**Changes:** +2 skills (split G3.02, add reporter skill), moved G3.06 earlier

---

### GRADE 4: Before (10 skills) → After (16 skills)

#### BEFORE:
```
T09.G4.01 - Use addition and subtraction in variable expressions ⚠️ OVERLY BROAD
T09.G4.02 - Use multiplication and division in expressions ⚠️ OVERLY BROAD
T09.G4.03 - Combine two arithmetic operators in a single expression
T09.G4.04 - Store and use user input in a variable ⚠️ UNCLEAR
T09.G4.05 - Use a variable as a loop counter ⚠️ MISSING DEPENDENCIES
T09.G4.06 - Use comparison operators (=, ≠, >, <, ≥, ≤) ⚠️ MASSIVELY BROAD (6 operators!)
T09.G4.07 - Use a flag variable to track state (0/1 or true/false)
T09.G4.08 - Use random number blocks to set variable values ⚠️ NO BLOCK REF
T09.G4.08.01 - Choose appropriate variable display modes
T09.G4.09 - Debug variable initialization and update frequency errors
```

#### AFTER:
```
T09.G4.01 - Use addition operator (+) in variable expressions 🔧 SPLIT
  └─ Block: (A) + (B)
  └─ Examples: set total to score + bonus

T09.G4.01.01 - Use subtraction operator (-) in variable expressions ✨ NEW
  └─ Block: (A) - (B)
  └─ Examples: set remaining to total - used

T09.G4.02 - Use multiplication operator (*) in expressions 🔧 SPLIT
  └─ Block: (A) * (B)
  └─ Examples: set total to lives * 100

T09.G4.02.01 - Use division operator (/) in expressions ✨ NEW
  └─ Block: (A) / (B)
  └─ Examples: set average to sum / count

T09.G4.03 - Combine two arithmetic operators in a single expression

T09.G4.04 - Store and use user input in a variable 🔧 CLARIFIED
  └─ Blocks: ask [question] and wait, (answer), set [var] to (answer)
  └─ Examples: ask "Your name?" then set [playerName] to (answer)

T09.G4.05 - Use a variable as a loop counter 🔧 DEPENDENCIES ADDED
  └─ NEW dependencies: G3.01.04 (display), G3.02 (change)

T09.G4.06 - Use equals (=) and less than (<) comparison operators 🔧 SPLIT
  └─ Blocks: (A) = (B), (A) < (B)
  └─ Most fundamental comparisons

T09.G4.06.01 - Use greater than (>) comparison operator ✨ NEW
  └─ Block: (A) > (B)

T09.G4.06.02 - Use not equals (≠) comparison operator ✨ NEW
  └─ Block: (A) ≠ (B)

T09.G4.06.03 - Use greater-or-equal (≥) and less-or-equal (≤) operators ✨ NEW
  └─ Blocks: (A) ≥ (B), (A) ≤ (B)
  └─ Most complex comparisons

T09.G4.07 - Use a flag variable to track state (0/1 or true/false)

T09.G4.08 - Use random number blocks to set variable values 🔧 BLOCK REF ADDED
  └─ Block: pick random (min) to (max)
  └─ Examples: set enemyX to pick random (-200) to (200)

T09.G4.08.01 - Choose appropriate variable display modes

T09.G4.09 - Debug variable initialization and update frequency errors
```

**Changes:** +6 skills (split operators into individual skills)

---

### GRADE 5: Before (9 skills) → After (11 skills)

#### BEFORE:
```
T09.G5.01 - Use multiple variables together in a single expression
T09.G5.02 - Create and use string variables ⚠️ VAGUE
T09.G5.02.01 - Create and use boolean variables
T09.G5.03 - Join strings using concatenation ⚠️ NO BLOCK REF
T09.G5.04 - Use variables as settings to control program behavior
T09.G5.05 - Use the accumulator pattern to compute running totals
T09.G5.06 - Trace a counter through loop iterations to predict final value
T09.G5.07 - Trace code with multiple interacting variables
T09.G5.08 - Track high score using variable comparison
```

#### AFTER:
```
T09.G5.01 - Use multiple variables together in a single expression

T09.G5.02 - Create and use string variables 🔧 CLARIFIED
  └─ Description now specifies: "Store text values and display them"
  └─ Focus on storage/display, not operations (those in later skills)

T09.G5.02.01 - Create and use boolean variables 🔧 BLOCK REF ADDED
  └─ Blocks: <true>, <false> (operator_true, operator_false)
  └─ Examples: set isJumping to <true>

T09.G5.03 - Join strings using concatenation 🔧 BLOCK REF ADDED
  └─ Block: join (A) (B) (standard Scratch 2-input)
  └─ Examples: join [Hello ] [name]

T09.G5.03.01 - Use multi-input join with separator ✨ NEW
  └─ Block: join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]
  └─ Examples: CSV data, formatted lists

T09.G5.04 - Use variables as settings to control program behavior

T09.G5.05 - Use the accumulator pattern to compute running totals

T09.G5.06 - Trace a counter through loop iterations to predict final value

T09.G5.07 - Trace code with multiple interacting variables

T09.G5.08 - Track high score using variable comparison
```

**Changes:** +2 skills (add multi-join, clarify existing)

---

### GRADE 6: Before (10 skills) → After (14 skills)

#### BEFORE:
```
T09.G6.01 - Model real-world quantities using variables and formulas ⚠️ TOO BROAD
T09.G6.02 - Apply operator precedence rules (PEMDAS)
T09.G6.02.01 - Use parentheses to override operator precedence
T09.G6.03 - Use exponents (^) in expressions ⚠️ NO BLOCK REF
T09.G6.03.01 - Use modulo (remainder) operator ⚠️ NO BLOCK REF
T09.G6.04 - Use string length and case conversion operations ⚠️ OVERLY BROAD
T09.G6.05 - Use substring and position operations on strings ⚠️ OVERLY BROAD
T09.G6.06 - Use temporary variables for multi-step calculations
T09.G6.06.01 - Understand variable persistence across events
T09.G6.07 - Debug off-by-one and comparison operator errors
```

#### AFTER:
```
T09.G6.01 - Model proportional relationships using multiplication 🔧 CLARIFIED
  └─ Examples: distance = speed × time, total_cost = price × quantity
  └─ OR: Create simulations with 3+ variables representing real quantities

T09.G6.02 - Apply operator precedence rules (PEMDAS)

T09.G6.02.01 - Use parentheses to override operator precedence

T09.G6.03 - Use exponents (^) in expressions 🔧 BLOCK REF ADDED
  └─ Block: (BASE) ^ (P) (operator_pow)
  └─ Examples: set area to side ^ 2

T09.G6.03.01 - Use modulo (remainder) operator 🔧 BLOCK REF ADDED
  └─ Block: (A) mod (B) ⚠️ NEEDS VERIFICATION
  └─ Examples: if score mod 10 = 0 (trigger every 10 points)

T09.G6.04 - Use string length operation 🔧 SPLIT
  └─ Block: length of [string]
  └─ Examples: checking password length, validation

T09.G6.04.01 - Use case conversion operations ✨ NEW
  └─ Block: [CASE v] of text [T] (operator_texttransform)
  └─ Examples: uppercase/lowercase for formatting

T09.G6.05 - Use position operation to find substrings 🔧 SPLIT
  └─ Block: position of [T1] in [T2] (operator_substringindex)
  └─ Examples: finding where text appears

T09.G6.05.01 - Use substring operation to extract text ✨ NEW
  └─ Block: substring of [TEXT] from position (P1) to (P2)
  └─ Examples: extracting parts of strings

T09.G6.06 - Use temporary variables for multi-step calculations

T09.G6.06.01 - Understand variable persistence across events

T09.G6.07 - Debug off-by-one and comparison operator errors
```

**Changes:** +4 skills (split string operations, clarify G6.01)

---

### GRADE 7: Before (7 skills) → After (10 skills)

#### BEFORE:
```
T09.G7.01 - Model dynamic systems where variables change over time ⚠️ TOO ABSTRACT
T09.G7.01.01 - Use mathematical functions (abs, round, floor, ceiling, sqrt) ⚠️ MASSIVELY BROAD
T09.G7.02 - Compute average using sum and count variables
T09.G7.03 - Use compound conditions (AND, OR, NOT) with variables
T09.G7.04 - Understand local vs global variable scope
T09.G7.05 - Save and load variables to/from files ⚠️ NO BLOCK REF
T09.G7.06 - Predict behavior changes from modifying variable values
```

#### AFTER:
```
T09.G7.01 - Create animations where variables update each frame 🔧 CLARIFIED
  └─ Pattern: forever loop with variable updates
  └─ Examples: change x by speed, change temperature by -1
  └─ Teaches the update-per-frame animation pattern

T09.G7.01.01 - Use rounding functions (round, floor, ceiling) 🔧 SPLIT
  └─ Blocks: round(), floor(), ceiling()
  └─ Examples: rounding scores, converting decimals
  └─ Most common math functions

T09.G7.01.02 - Use absolute value function ✨ NEW
  └─ Block: abs()
  └─ Examples: distance calculations (abs(x1 - x2))

T09.G7.01.03 - Use square root function ✨ NEW
  └─ Block: sqrt()
  └─ Examples: distance formulas, quadratic equations

T09.G7.02 - Compute average using sum and count variables

T09.G7.03 - Use compound conditions (AND, OR, NOT) with variables

T09.G7.04 - Understand local vs global variable scope

T09.G7.05 - Save and load variables to/from files 🔧 BLOCK REF ADDED
  └─ Blocks: export variable [VAR], import variable [VAR]
  └─ Examples: save game state, high scores

T09.G7.06 - Predict behavior changes from modifying variable values
```

**Changes:** +3 skills (split math functions, clarify G7.01)

---

### GRADE 8: Before (9 skills) → After (9 skills)

#### BEFORE:
```
T09.G8.01.01 - Use variables to track index position in linear search
T09.G8.01.02 - Use flag variables in search algorithms
T09.G8.01.03 - Use variables in iterative approximation algorithms ⚠️ TOO ADVANCED
T09.G8.02 - Simplify and optimize variable expressions
T09.G8.02.01 - Use min and max functions ⚠️ NO BLOCK REF
T09.G8.02.02 - Use trigonometric functions ⚠️ NO BLOCK REF
T09.G8.03 - Use cloud variables for persistent data ⚠️ NO BLOCK REF
T09.G8.04 - Debug variable scope and concurrent update errors
T09.G8.05 - Translate mathematical formulas into code
T09.G8.06 - Use variables to collect and store multiple data readings
```

#### AFTER:
```
T09.G8.01.01 - Use variables to track index position in linear search

T09.G8.01.02 - Use flag variables in search algorithms

T09.G8.01.03 - Use variables in guess-and-check algorithms 🔧 SIMPLIFIED
  └─ Removed: Newton's method (too advanced)
  └─ New examples: Binary search for high score, guess-and-check games
  └─ OR: REMOVE this skill entirely

T09.G8.02 - Simplify and optimize variable expressions

T09.G8.02.01 - Use min and max functions to constrain values 🔧 BLOCK REF ADDED
  └─ Blocks: min(), max() ⚠️ NEEDS VERIFICATION how accessed
  └─ Examples: set x to max(0, min(480, x)) to keep in bounds

T09.G8.02.02 - Use trigonometric functions 🔧 BLOCK REF ADDED
  └─ Blocks: sin(), cos(), tan() ⚠️ NEEDS VERIFICATION
  └─ Examples: circular motion, trajectory angles

T09.G8.03 - Use cloud variables for persistent data 🔧 BLOCK REF ADDED
  └─ Block: save [VISIBILITY v] data [VALUE] with name [KEY]
  └─ Examples: high scores, user preferences, multiplayer

T09.G8.04 - Debug variable scope and concurrent update errors

T09.G8.05 - Translate mathematical formulas into code

T09.G8.06 - Use variables to collect and store multiple data readings
```

**Changes:** 0 net skills (simplify G8.01.03, add block refs)

---

## Summary Statistics

| Grade | Before | After | Change | Major Changes |
|-------|--------|-------|--------|---------------|
| K | 2 | 2 | 0 | None needed (already excellent) |
| 1 | 2 | 2 | 0 | None needed (already excellent) |
| 2 | 2 | 2 | 0 | None needed (already excellent) |
| 3 | 13 | 15 | +2 | Split G3.02, add reporter skill, move G3.06 |
| 4 | 10 | 16 | +6 | Split 4 operator skills (arithmetic + comparison) |
| 5 | 9 | 11 | +2 | Add multi-join, clarify string skills |
| 6 | 10 | 14 | +4 | Split string operations, clarify G6.01 |
| 7 | 7 | 10 | +3 | Split math functions, clarify G7.01 |
| 8 | 9 | 9 | 0 | Simplify G8.01.03, add block refs |
| **TOTAL** | **62** | **76** | **+14** | **22% increase in granularity** |

---

## Visual: Most Impactful Changes

### 🔴 CRITICAL: T09.G4.06 Split (6 operators → 4 skills)
```
BEFORE:                                AFTER:
┌─────────────────────────────┐       ┌─────────────────────────────┐
│ T09.G4.06                   │       │ T09.G4.06                   │
│ Use 6 comparison operators: │  →→→  │ Use = and <                 │
│ =, ≠, >, <, ≥, ≤           │       ├─────────────────────────────┤
│                             │       │ T09.G4.06.01: Use >        │
└─────────────────────────────┘       ├─────────────────────────────┤
                                      │ T09.G4.06.02: Use ≠        │
                                      ├─────────────────────────────┤
                                      │ T09.G4.06.03: Use ≥ and ≤  │
                                      └─────────────────────────────┘
```

### 🔴 CRITICAL: T09.G7.01.01 Split (5 functions → 3 skills)
```
BEFORE:                                AFTER:
┌─────────────────────────────┐       ┌─────────────────────────────┐
│ T09.G7.01.01                │       │ T09.G7.01.01                │
│ Use 5 math functions:       │  →→→  │ Use rounding (3 functions)  │
│ abs, round, floor,          │       ├─────────────────────────────┤
│ ceiling, sqrt               │       │ T09.G7.01.02: Use abs      │
│                             │       ├─────────────────────────────┤
└─────────────────────────────┘       │ T09.G7.01.03: Use sqrt     │
                                      └─────────────────────────────┘
```

### 🟡 HIGH IMPACT: Arithmetic Operators (4 operators → 4 skills)
```
BEFORE:                                AFTER:
┌─────────────────────────────┐       ┌─────────────────────────────┐
│ T09.G4.01: Use + and -      │  →→   │ T09.G4.01: Use +           │
│                             │       │ T09.G4.01.01: Use -        │
├─────────────────────────────┤       ├─────────────────────────────┤
│ T09.G4.02: Use * and /      │  →→   │ T09.G4.02: Use *           │
│                             │       │ T09.G4.02.01: Use /        │
└─────────────────────────────┘       └─────────────────────────────┘
```

---

## Block Verification Needed

Before finalizing changes, verify these blocks exist in CreatiCode:

1. ⚠️ `(A) mod (B)` - modulo operator (standard in Scratch)
2. ⚠️ `abs()`, `round()`, `floor()`, `ceiling()`, `sqrt()` - how accessed?
3. ⚠️ `min()`, `max()` - functions for constraining values
4. ⚠️ `sin()`, `cos()`, `tan()` - trigonometric functions
5. ✅ `save data`, `export/import variable` - CONFIRMED in blockdes8.txt
6. ✅ `<true>`, `<false>` - CONFIRMED (operator_true, operator_false)
7. ✅ All string operators - CONFIRMED in blockdes8.txt

---

## Next Steps

1. **Verify blocks** (list above)
2. **Implement splits** starting with Grade 4 (highest impact)
3. **Add block references** to all skills
4. **Test progression** for logical flow
5. **Update dependencies** (G3.06 move, G4.05 additions)
6. **Review with stakeholders**

---

**Full Analysis:** See `T09_COMPREHENSIVE_ANALYSIS.md`
**Quick Reference:** See `T09_QUICK_REFERENCE.md`
