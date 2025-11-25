# T09 (Variables & Expressions) Skills Analysis Report

## Executive Summary

Analysis of T09 skills (lines 6163-6982 in allskills.md) reveals **45 total skills** with significant structural issues. Based on CreatiCode's actual block inventory:
- **Variables Category**: 59 blocks (basic operations + tables + lists + cloud storage)
- **Operators Category**: 30 blocks (string ops, regex, math, geometric, comparison)

## Key Findings

### 1. SKILLS THAT ARE TOO BROAD (Need Breakdown)

#### **T09.G3.03** - "Use a variable in a simple conditional"
- **Issue**: Combines variable usage + conditional logic + comparison operators in one skill
- **Should be**: Already covered by separate skills (T09.G4.06 covers comparisons in conditionals)
- **Recommendation**: Remove redundancy or clarify this is about the FIRST usage pattern

#### **T09.G3.04** - "Debug a single missing or wrong variable block"
- **Issue**: Covers 3 different bug types: missing initialization, missing update, wrong number
- **Should be**: Split into 3 separate debugging skills (one per bug type)

#### **T09.G3.05** - "Trace code with variables to predict outcomes"
- **Issue**: Generic tracing without specific focus
- **Should be**: More specific about what kind of variable operations are being traced

#### **T09.G4.03** - "Combine two arithmetic operators in a single expression"
- **Issue**: Description says "same type of operation" (a+b+c or x*y*z) but doesn't address mixing operators
- **Should be**: Either rename to "Chain same operators" or expand to truly mixing operators

#### **T09.G4.04** - "Store and use user input in a variable"
- **Issue**: Combines input capture + storage + usage in one skill
- **Should be**: Each aspect should be separate (already partially covered elsewhere)

#### **T09.G4.09** - "Debug variable initialization and update frequency errors"
- **Issue**: Covers 3+ error types (initialization, wrong variable, update frequency)
- **Should be**: Split into separate debugging skills per error category

#### **T09.G5.08** - "Track high score using variable comparison"
- **Issue**: Combines comparison + conditional update + persistence pattern
- **Should be**: This is actually a good integration skill, but relies on earlier skills

#### **T09.G7.05** - "Save and load variables to/from files"
- **Issue**: Combines save + load operations (two different blocks)
- **Should be**: Split into G7.05 (save) and G7.05.01 (load)

---

### 2. MISSING SKILLS (CreatiCode Features Not Covered)

#### **String Operations Missing**:
- **letter # of [string]** - Extract single character by position
- **replace [old] with [new] in [string]** - String replacement
- **split [string] by [delimiter]** - Split string into array/list
- **split [string] by empty** - Split into character array
- **word # of [string]** - Extract word by position
- **diff string [A] [B]** - String difference/comparison
- **word to number [text]** - Convert word to numeric value

#### **Regex Operations Missing** (5 blocks - ENTIRE CATEGORY):
- **regex test [pattern] [text]** - Test if pattern matches
- **regex match [pattern] [text]** - Find matches
- **regex replace [pattern] [new] in [text]** - Replace using regex
- **regex split [text] by [pattern]** - Split using regex
- **regex search [pattern] in [text]** - Search for pattern

#### **Math Functions Missing**:
- **power [base] ^ [exponent]** - Currently only mentions ^ operator in G6.03, needs explicit power block skill
- **moving average** - CreatiCode-specific statistical function
- **solve equation for [variable]** - CreatiCode's equation solver
- **calculate [expression]** - Expression evaluator block

#### **Advanced Math Functions Missing**:
- **e^[x]** - Natural exponential
- **10^[x]** - Base-10 exponential
- **ln [x]** - Natural logarithm
- **log [x]** - Base-10 logarithm
- **asin, acos, atan** - Inverse trigonometric functions (only sin/cos/tan covered in G8.02.02)

#### **Geometric Operations Missing** (3 blocks - ENTIRE CATEGORY):
- **distance 2D [x1,y1] to [x2,y2]** - 2D distance calculation
- **distance 3D [x1,y1,z1] to [x2,y2,z2]** - 3D distance calculation
- **direction from [x1,y1] to [x2,y2]** - Angle calculation

#### **CreatiCode-Specific Missing**:
- **reduce [variable] by [amount]** - COVERED in T09.G3.02.01 ✓ (Good!)
- **Cloud storage blocks** - Partially covered in T09.G8.03 but needs more detail on all 4 cloud blocks

---

### 3. INTRA-TOPIC DEPENDENCY ISSUES (X-2 Rule Violations)

#### **Critical Violations**:

**T09.G4.01** (Use addition in expressions):
- Depends on: T09.G3.05, T09.G3.06 (only 2 skills back) ✓ OK
- BUT also depends on: T04.G2.01, T04.G2.02, T04.G2.03, T07.G2.01 (cross-topic)
- **Issue**: These loop/pattern dependencies appear in EVERY G4+ skill unnecessarily

**T09.G5.06** (Trace counter through loop iterations):
- Lists dependencies: T09.G4.05, T10.G3.05, T10.G4.18
- **Issue**: T10.G3.05 and T10.G4.18 are from NEXT TOPIC (Tables), violates forward dependency rule
- **Critical Error**: Cannot depend on skills from T10 within T09!

**T09.G4.08.01** (Choose variable display modes):
- Depends on: T13.G3.01 (Testing topic)
- **Issue**: Cross-topic dependency that may be too far ahead

**Excessive Repetitive Cross-Topic Dependencies**:
Every skill from G4.01 onwards lists the same 4 dependencies:
- T04.G2.01, T04.G2.02, T04.G2.03, T07.G2.01
- **Issue**: These are overly broad and not specifically relevant to most variable skills
- **Recommendation**: Remove these boilerplate dependencies, keep only truly necessary ones

#### **Progression Issues**:

**T09.G3.01.05** → **T09.G3.02** dependency problem:
- G3.01.05: "Use variable reporter blocks in other blocks" depends on G3.01.04
- G3.02: "Use change block to increase a variable" depends on G3.01.04
- **Issue**: G3.02 should come BEFORE G3.01.05 (using reporter in blocks is more advanced)
- **Actual sequence violation**: G3.02 is listed after G3.01.05 but both depend on G3.01.04

**T09.G3.06** placement issue:
- Listed after G3.05 but only depends on G3.01.02
- **Issue**: This should come much earlier (right after G3.01.02), not after tracing skills

---

### 4. DESCRIPTION CLARITY ISSUES

#### **Vague Descriptions**:

**T09.G3.01.01** - "Create a new variable with a descriptive name":
- Missing: How to access "Make a Variable" button
- Missing: Variable naming conventions/restrictions
- Missing: What happens after creation

**T09.G3.01.04** - "Display variable value on stage":
- Says "check the checkbox" but doesn't explain WHERE the checkbox is
- Missing: Mention of different display modes (comes much later in G4.08.01)

**T09.G3.02** vs **T09.G3.01.03**:
- G3.01.03: "Change a variable value by 1"
- G3.02: "Use change block to increase a variable"
- **Issue**: These overlap significantly, description needs to clarify G3.02 is about arbitrary amounts

**T09.G3.03** - "Use a variable in a simple conditional":
- Says "very simple comparisons" but doesn't define what makes it simple
- **Conflict**: T09.G4.06 covers comparison operators in conditionals - these overlap

**T09.G4.03** - "Combine two arithmetic operators":
- Description says "same type of operation (a+b+c or x*y*z)"
- **Issue**: This isn't really "combining two operators" - it's chaining the same operator

**T09.G5.03.01** - "Use multi-input join with separator":
- Shows block syntax but doesn't explain when/why to use this vs basic join
- Missing: Examples of CSV, formatted lists mentioned in description

**T09.G6.02.01** - "Use parentheses to override precedence":
- Good description but missing: In Scratch/CreatiCode, parentheses are implicit through block nesting

**T09.G7.04** - "Understand local vs global variable scope":
- **Critical Issue**: CreatiCode/Scratch only have "for this sprite only" vs "for all sprites" variables
- Description uses "local" and "global" which are traditional programming terms
- **Needs clarification**: How this maps to CreatiCode's actual variable scoping system

**T09.G8.06** - "Use variables to collect and store multiple data readings":
- **Issue**: Description mentions "sensor readings" but CreatiCode doesn't have traditional sensors
- **Issue**: No dependencies listed (appears to be cut off)
- Missing: Connection to lists/arrays for storing multiple values

#### **Misleading Descriptions**:

**T09.G4.02.01** (Division operator):
- Listed AFTER G4.02 (multiplication) but has same dependencies as multiplication
- Dependencies include T04.G2.01, T07.G2.01 which don't relate to division
- **Should be**: Parallel to multiplication, not sequential

---

### 5. GRADE-LEVEL APPROPRIATENESS ISSUES

#### **K-2 Skills (Generally Good)**:

**T09.GK.01-02, T09.G1.01-02, T09.G2.01-02**: ✓ Appropriate
- Picture-based, no coding required
- Focus on recognition and observation
- Good progression

#### **Grade 3 Transition Issues**:

**T09.G3.01.01 through T09.G3.01.05**:
- **Issue**: Numbered as G3.01.01, G3.01.02, etc. (sub-sub-level)
- **Pattern**: These are the 5 fundamental variable operations broken down step-by-step
- **Appropriate for G3**: Yes, but the numbering is unusual
- **Recommendation**: Consider renumbering as T09.G3.01 through T09.G3.05

**T09.G3.02** vs **T09.G3.02.01**:
- G3.02: Use change block (increase)
- G3.02.01: Use reduce block (decrease)
- **Good**: Introduces CreatiCode-specific "reduce" block
- **Appropriate**: Yes for G3

#### **Grade 4 Complexity Jump**:

**T09.G4.01** onwards:
- Suddenly introduces all 4 basic arithmetic operators in sequence
- Each has dependencies on T04.G2.01, T04.G2.02, T04.G2.03, T07.G2.01
- **Issue**: Why do arithmetic operators need loop/pattern dependencies?
- **Recommendation**: These dependencies seem copy-pasted, not carefully considered

**T09.G4.05** - "Use a variable as a loop counter":
- **Good skill** for G4
- **Issue**: Very heavy dependency list (9 dependencies)
- **Question**: Are all these dependencies truly necessary?

#### **Grade 5-8 Skills (Generally Appropriate)**:

Most G5-G8 skills show good progression in complexity
- G5: Multiple variables, strings, patterns
- G6: Operator precedence, string operations, formulas
- G7: Dynamic systems, scope, file I/O
- G8: Algorithms, optimization, cloud variables

**Exception - T09.G8.06**:
- Mentions "sensor readings" which isn't standard CreatiCode
- Unclear if this refers to user inputs, data generation, or something else

---

### 6. STRUCTURAL ISSUES

#### **Numbering Inconsistencies**:

**T09.G3.01.XX pattern**:
- T09.G3.01.01, T09.G3.01.02, T09.G3.01.03, T09.G3.01.04, T09.G3.01.05
- Then jumps to T09.G3.02
- **Issue**: Unusual to have 5 sub-skills under one skill number
- **Recommendation**: Consider flattening to T09.G3.01-05

**T09.G4.01, T09.G4.01.01, T09.G4.02, T09.G4.02.01**:
- Addition (G4.01) → Subtraction (G4.01.01) → Multiplication (G4.02) → Division (G4.02.01)
- **Issue**: Why is subtraction a sub-skill of addition? They're parallel operations
- **Recommendation**: All 4 basic operators should be parallel: G4.01, G4.02, G4.03, G4.04

**T09.G6.04 string operations**:
- G6.04: length
- G6.04.01: case conversion
- G6.05: position (find substring)
- G6.05.01: substring extraction
- **Issue**: Position and substring are closely related, but case conversion inserted between length and position
- **Recommendation**: Group logically: length/case together, then position/substring together

#### **Missing Block-to-Skill Mapping**:

Based on CreatiCode's blocks:

**String Category (15 blocks)**:
- join ✓ (G5.03)
- join with separator ✓ (G5.03.01)
- length ✓ (G6.04)
- letter of ✗ MISSING
- position of ✓ (G6.05)
- substring ✓ (G6.05.01)
- replace ✗ MISSING
- split ✗ MISSING
- split with empty ✗ MISSING
- to upper case ✓ (G6.04.01)
- to lower case ✓ (G6.04.01)
- word to number ✗ MISSING
- word of ✗ MISSING
- diff string ✗ MISSING

**Regex Category (5 blocks)**:
- ALL 5 BLOCKS MISSING from skills

**Math Category (advanced functions)**:
- round ✓ (G7.01.01)
- floor ✓ (G7.01.01)
- ceiling ✓ (G7.01.01)
- abs ✓ (G7.01.02)
- sqrt ✓ (G7.01.03)
- sin/cos/tan ✓ (G8.02.02)
- asin/acos/atan ✗ MISSING
- ln/log ✗ MISSING
- e^x, 10^x ✗ MISSING
- power ✓ (G6.03 as operator)
- mod ✓ (G6.03.01)
- moving average ✗ MISSING
- calculate ✗ MISSING
- solve equation ✗ MISSING

**Geometric Category (3 blocks)**:
- distance 2D ✗ MISSING
- distance 3D ✗ MISSING
- direction ✗ MISSING

---

### 7. DEPENDENCY GRAPH ISSUES

#### **Circular or Confusing Dependencies**:

**T09.G3.03** depends on:
- T09.G3.02: "Use change and reduce blocks"
- BUT: G3.02 description only mentions "change" block
- AND: T09.G3.02.01 is the "reduce" block skill
- **Issue**: Should depend on G3.02.01, not G3.02

**T09.G4.05** (loop counter) depends on:
- T09.G3.01.04: Display variable on stage ✓
- T09.G3.02: Use change block ✓
- **But also**: T01.G2.01, T02.G2.01, T02.G2.02, T04.G2.01, T04.G2.02, T07.G2.01, T07.G3.01
- **Issue**: 9 dependencies for a single skill about loop counters seems excessive

**T09.G5.05** (accumulator pattern) depends on:
- T09.G4.05: Loop counter ✓
- T09.G4.09: Debug variable errors ✓
- T06.G5.01, T07.G5.01: Event patterns, simulate experiments ✓
- **T10.G5.01**: Understand table structure
- **Issue**: Depends on T10 (next topic) - should not!

**T09.G5.06** (trace counter through loop):
- **CRITICAL ERROR**: Lists dependencies T10.G3.05, T10.G4.18
- **Cannot depend on future topic T10**

#### **Missing Critical Dependencies**:

**T09.G5.02** (string variables):
- Depends on: T09.G4.04 (user input), T06.G5.01 (event patterns)
- **Missing**: Should depend on basic variable creation (T09.G3.01.01)

**T09.G6.04.01** (case conversion):
- Only depends on: T09.G6.04 (string length)
- **Missing**: Should also depend on T09.G5.02 (string variables)

**T09.G7.03** (compound conditions AND/OR/NOT):
- Depends on: T09.G5.08, T09.G6.07
- **Missing**: Should depend on T09.G4.06.xx (comparison operators)
- **Note**: AND/OR/NOT are actually in T08 (Conditionals), not T09

---

## Priority Recommendations

### HIGH PRIORITY:

1. **Fix T10 forward dependencies in T09.G5.05, T09.G5.06** - CRITICAL ERROR
2. **Add missing regex skills** (entire 5-block category)
3. **Add missing geometric operations** (3 blocks)
4. **Split overly broad debugging skills** (G3.04, G4.09)
5. **Fix operator numbering** (make +, -, *, / parallel, not hierarchical)
6. **Remove excessive boilerplate cross-topic dependencies** from G4+ skills

### MEDIUM PRIORITY:

7. **Add missing string operations** (letter of, replace, split, word of, diff string, word to number)
8. **Add missing advanced math** (inverse trig, logarithms, exponentials)
9. **Add missing math utilities** (moving average, calculate, solve equation)
10. **Clarify variable scope description** (local/global vs sprite-specific/all-sprites)
11. **Move T09.G3.06 earlier** in the progression (right after G3.01.02)
12. **Renumber G3.01.XX** to flatten structure (G3.01-05 instead of G3.01.01-05)

### LOW PRIORITY:

13. **Clean up description clarity** for confusing skills
14. **Standardize dependency lists** (remove copy-paste dependencies)
15. **Add implementation notes** for picture-based vs block-based activities
16. **Clarify "sensor readings"** in T09.G8.06 (what this means in CreatiCode context)

---

## Coverage Statistics

**Current T09 Skills**: 45 total
- Grade K: 2 skills
- Grade 1: 2 skills
- Grade 2: 2 skills
- Grade 3: 11 skills (including sub-numbered)
- Grade 4: 9 skills
- Grade 5: 8 skills
- Grade 6: 7 skills
- Grade 7: 6 skills
- Grade 8: 6 skills (last one appears incomplete)

**CreatiCode Blocks Relevant to T09**:
- Variables: ~25 blocks (excluding tables/lists which go to T10)
- Operators: 30 blocks (string + regex + math + geometric + comparison)
- **Total**: ~55 blocks

**Missing Coverage**:
- Regex: 5 blocks (0% coverage)
- Geometric: 3 blocks (0% coverage)
- String operations: 7 blocks missing (~50% coverage)
- Advanced math: 8 blocks missing (~70% coverage)
- **Estimated missing skills needed**: ~15-20 new skills

---

## Conclusion

T09 has a solid foundation for basic variable operations but needs significant expansion to cover CreatiCode's full operator and expression capabilities. The most critical issues are:

1. Forward dependencies to T10 (tables)
2. Missing entire categories (regex, geometric)
3. Overly broad skills that need splitting
4. Excessive boilerplate dependencies
5. Numbering inconsistencies

The skill progression from K-8 is generally appropriate, but Grade 4+ needs dependency cleanup and missing block coverage.
