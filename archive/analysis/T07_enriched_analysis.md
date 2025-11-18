# T07 – Loops & Repetition: Dependency Analysis

## Age-Appropriateness Framework for This Topic

**K-2 (Ages 5-8)**: Recognizing "again and again". Counting repetitions. Manual duplication before loops.

**3-5 (Ages 8-11)**: Loop blocks (repeat, forever, repeat-until). Nested loops. Loop counters.

**6-8 (Ages 11-14)**: Loop efficiency analysis. Advanced patterns (accumulators). Loop-based algorithms.

---

## ⚠️ OVERLAP ANALYSIS WITH T04 (Patterns)

Before analyzing skills, documenting known overlaps from T04 analysis:

| T07 Skill | T04 Equivalent | Resolution |
|-----------|----------------|------------|
| T07.GK.01 | T04.GK.01 | **KEEP T07.GK.01** (same skill, keep in loops topic) |
| T07.G1.01 | T04.G1.01 | **KEEP T07.G1.01**, T04 should reference |
| T07.G1.04 | T04.G1.04 | **KEEP T07.G1.04**, T04 duplicates |
| T07.G2.01 | T04.G2.02 | **KEEP T07.G2.01** (primary implementation) |
| T07.G3.03 | T04.G3.02 | **KEEP T07.G3.03**, T04 should reference |
| T07.G3.04 | T04.G3.04 | **KEEP T07.G3.04**, T04 should reference |

**Resolution Strategy**: T07 keeps all loop *implementation* skills. T04 should *reference* these and focus on pattern *recognition*.

---

## Skill Review & Dependencies

### Grade K (PreK–K) - Ages 5-6

#### T07.GK.01 – Identify simple repeating patterns (pictures)
- **Size**: ✓ Appropriate (ABAB patterns)
- **Age-appropriateness**: ✓ Perfect for K - visual, concrete
- **Dependencies**: []
- **Notes**: **DUPLICATE** of T04.GK.01
- **Resolution**: **KEEP HERE** - this is foundational for loops
- **T04 Action**: T04.GK.01 should be SAME skill or reference this

#### T07.GK.02 – Count how many times it repeats
- **Size**: ✓ Appropriate (counting iterations)
- **Age-appropriateness**: ✓ Excellent - connects repetition to counting
- **Dependencies**: [T07.GK.01]
- **Notes**: **UNIQUE** to T07 - counting focus vs pattern recognition

#### T07.GK.03 – Tell the robot to do it again
- **Size**: ✓ Appropriate (verbal repetition commands)
- **Age-appropriateness**: ✓ Good for K - natural language
- **Dependencies**: [T07.GK.01]
- **Notes**: **UNIQUE** - prepares for loop blocks

---

### Grade 1 (Ages 6-7)

#### T07.G1.01 – Spot repeated blocks in code
- **Size**: ✓ Appropriate (identifying code repetition)
- **Age-appropriateness**: ✓ Good for G1 - first code pattern recognition
- **Dependencies**: [T07.GK.01, T06.G1.01]
  - T06.G1.01: Build short script with green flag
- **Notes**: **DUPLICATE** of T04.G1.01
- **Resolution**: **KEEP HERE** as primary skill
- **T04 Action**: T04.G1.01 should reference T07.G1.01
- **Grade-level check**: ✓ T06.G1.01 is G1

#### T07.G1.02 – How far does the cat walk?
- **Size**: ✓ Appropriate (cumulative effect of repetition)
- **Age-appropriateness**: ✓ Good - quantitative reasoning
- **Dependencies**: [T07.G1.01, T06.G1.02]
  - T06.G1.02: Trace code to find result
- **Notes**: **UNIQUE** - cumulative reasoning
- **Grade-level check**: ✓ T06.G1.02 is G1

#### T07.G1.03 – Match repeated actions to code
- **Size**: ✓ Appropriate (visual-code mapping)
- **Age-appropriateness**: ✓ Good for G1 - concrete matching
- **Dependencies**: [T07.G1.01, T01.G1.02]
  - T01.G1.02: Trace and predict outcome
- **Notes**: Similar to T04.G1.02 but loop-focused
- **Grade-level check**: ✓ T01.G1.02 is G1

#### T07.G1.04 – Repeat an action by copying blocks
- **Size**: ✓ Appropriate (manual repetition)
- **Age-appropriateness**: ✓ **PERFECT** - doing it "wrong" before learning loops
- **Dependencies**: [T07.G1.01, T06.G1.01]
- **Notes**: **DUPLICATE** of T04.G1.04
- **Resolution**: **KEEP HERE** - pedagogically important pre-loop skill
- **T04 Action**: T04.G1.04 should be REMOVED (duplicate)
- **Grade-level check**: ✓ T06.G1.01 is G1

---

### Grade 2 (Ages 7-8) - FIRST LOOP BLOCKS

#### T07.G2.01 – Use a repeat loop for steps
- **Size**: ✓ Appropriate (first loop refactoring)
- **Age-appropriateness**: ✓ **EXCELLENT** for G2 - first loop implementation
- **Dependencies**: [T07.G1.04, T07.G1.01, T06.G2.01]
  - T06.G2.01: Key events (for triggering loops)
- **Notes**: **DUPLICATE** of T04.G2.02
- **Resolution**: **KEEP HERE** - this is THE primary loop introduction
- **T04 Action**: T04.G2.02 should REFERENCE T07.G2.01, not duplicate
- **Grade-level check**: ✓ T06.G2.01 is G2

#### T07.G2.02 – Loop a dance move pattern
- **Size**: ✓ Appropriate (looping sequences)
- **Age-appropriateness**: ✓ Perfect - creative, motivating
- **Dependencies**: [T07.G2.01]
- **Notes**: **UNIQUE** - applying loops to patterns

#### T07.G2.03 – Use a loop for simple animation
- **Size**: ✓ Appropriate (costume-change loops)
- **Age-appropriateness**: ✓ Good for G2 - visual feedback
- **Dependencies**: [T07.G2.01, T15.G2.01]
  - T15.G2.01: Stories/animation - costume changes
- **Notes**: **UNIQUE** - loops for animation
- **Grade-level check**: ✓ T15.G2.01 is G2

#### T07.G2.04 – Count loop repeats from code
- **Size**: ✓ Appropriate (reading loop count)
- **Age-appropriateness**: ✓ Good - code reading
- **Dependencies**: [T07.G2.01, T02.G2.02]
  - T02.G2.02: Follow block program
- **Notes**: Similar to T04.G2.04 - **BOTH VALID** (trace vs predict)
- **Grade-level check**: ✓ T02.G2.02 is G2

---

### Grade 3 (Ages 8-9)

#### T07.G3.01 – Repeat until you reach the flag
- **Size**: ✓ Appropriate (repeat-until introduction)
- **Age-appropriateness**: ✓ Good for G3 - condition-based loops
- **Dependencies**: [T07.G2.01, T08.G2.01]
  - T08.G2.01: If/else basics
- **Notes**: **UNIQUE** - conditional loops
- **Grade-level check**: ✓ T08.G2.01 is G2

#### T07.G3.02 – Forever loop for player controls
- **Size**: ✓ Appropriate (forever loop, game context)
- **Age-appropriateness**: ✓ **EXCELLENT** - game loops highly motivating
- **Dependencies**: [T07.G2.01, T06.G2.04, T08.G2.03]
  - T06.G2.04: Game controls
  - T08.G2.03: If touching detection
- **Notes**: **CRITICAL** game programming skill
- **Grade-level check**: ✓ Both G2

#### T07.G3.03 – Use nested loops for patterns
- **Size**: ✓ Appropriate (nested loops, grids)
- **Age-appropriateness**: ✓ Good for G3 - 2D thinking
- **Dependencies**: [T07.G2.01, T07.G2.02]
- **Notes**: **DUPLICATE** of T04.G3.02
- **Resolution**: **KEEP HERE** - primary nested loop implementation
- **T04 Action**: T04.G3.02 should REFERENCE T07.G3.03

#### T07.G3.04 – Trace nested loops and count actions
- **Size**: ✓ Appropriate (multiplicative reasoning)
- **Age-appropriateness**: ✓ Good - math connection
- **Dependencies**: [T07.G3.03, T02.G3.02]
  - T02.G3.02: Trace code with condition
- **Notes**: **DUPLICATE** of T04.G3.04
- **Resolution**: **KEEP HERE** - tracing nested loops
- **T04 Action**: T04.G3.04 should REFERENCE T07.G3.04
- **Grade-level check**: ✓ T02.G3.02 is G3

---

### Grade 4 (Ages 9-10)

#### T07.G4.01 – Loop with checks inside
- **Size**: ✓ Appropriate (loops + conditionals)
- **Age-appropriateness**: ✓ Good for G4 - integration
- **Dependencies**: [T07.G3.02, T08.G3.01]
  - T08.G3.01: If/else in game loops
- **Notes**: **UNIQUE** - loop-conditional integration
- **Grade-level check**: ✓ T08.G3.01 is G3

#### T07.G4.02 – Use a counter inside a loop
- **Size**: ✓ Appropriate (loop counter variables)
- **Age-appropriateness**: ✓ Perfect for G4 - for-loop pattern
- **Dependencies**: [T07.G2.01, T09.G3.01]
  - T09.G3.01: Variables in programs
- **Notes**: **UNIQUE** - counter pattern (critical!)
- **Grade-level check**: ✓ T09.G3.01 is G3

#### T07.G4.03 – Refactor repeated code with a loop
- **Size**: ✓ Appropriate (code quality refactoring)
- **Age-appropriateness**: ✓ Good - can understand "better" code
- **Dependencies**: [T07.G2.01, T07.G4.01]
- **Notes**: Similar to T04.G4.03 but loop-focused - acceptable

#### T07.G4.04 – Find the bug in a loop
- **Size**: ✓ Appropriate (loop debugging)
- **Age-appropriateness**: ✓ Good for G4 - error analysis
- **Dependencies**: [T07.G2.01, T13.G3.01]
  - T13.G3.01: Testing/debugging basics
- **Notes**: **UNIQUE** - loop-specific debugging
- **Grade-level check**: ✓ T13.G3.01 is G3

---

### Grade 5 (Ages 10-11)

#### T07.G5.01 – Run an experiment many times with a loop
- **Size**: ✓ Appropriate (simulation/data collection)
- **Age-appropriateness**: ✓ **EXCELLENT** for G5 - scientific thinking
- **Dependencies**: [T07.G2.01, T09.G4.01, T28.G4.01]
  - T09.G4.01: Variables with loops
  - T28.G4.01: Chance/probability basics
- **Notes**: **UNIQUE** - loops for data/science
- **Grade-level check**: ✓ Both G4

#### T07.G5.02 – Fill a list using a loop
- **Size**: ✓ Appropriate (loops + lists)
- **Age-appropriateness**: ✓ Good for G5 - data structures
- **Dependencies**: [T07.G2.01, T10.G4.01, T07.G4.02]
  - T10.G4.01: Lists basics
- **Notes**: **UNIQUE** - list population pattern
- **Grade-level check**: ✓ T10.G4.01 is G4

#### T07.G5.03 – Use a loop to total scores
- **Size**: ✓ Appropriate (accumulator pattern)
- **Age-appropriateness**: ✓ Perfect - practical application
- **Dependencies**: [T07.G5.02, T10.G4.01, T09.G4.01]
- **Notes**: **CRITICAL** accumulator pattern
- **Grade-level check**: ✓ Both G4

#### T07.G5.04 – Nested loops for complex patterns
- **Size**: ✓ Appropriate (advanced nested loops)
- **Age-appropriateness**: ✓ Good for G5 - creative patterns
- **Dependencies**: [T07.G3.03, T07.G4.02]
- **Notes**: Similar to T04.G5.04 - acceptable (implementation vs design)

---

### Grade 6 (Ages 11-12)

#### T07.G6.01 – Trace nested loops with variables
- **Size**: ✓ Appropriate (complex tracing)
- **Age-appropriateness**: ✓ Good for G6 - abstract reasoning
- **Dependencies**: [T07.G5.04, T07.G4.02, T09.G5.01]
  - T09.G5.01: Advanced variables
- **Notes**: **UNIQUE** - complex loop analysis
- **Grade-level check**: ✓ T09.G5.01 is G5

#### T07.G6.02 – Turn repeated code into a loop
- **Size**: ✓ Appropriate (advanced refactoring)
- **Age-appropriateness**: ✓ Good - code quality focus
- **Dependencies**: [T07.G4.03, T12.G5.01]
  - T12.G5.01: Code organization
- **Notes**: Advanced version of G4.03
- **Grade-level check**: ✓ T12.G5.01 is G5

#### T07.G6.03 – Search a list using a loop
- **Size**: ✓ Appropriate (linear search)
- **Age-appropriateness**: ✓ Perfect for G6 - algorithm pattern
- **Dependencies**: [T07.G5.02, T10.G5.01, T08.G5.02]
  - T10.G5.01: List processing
  - T08.G5.02: Filter data with conditions
- **Notes**: **CRITICAL** search algorithm
- **Grade-level check**: ✓ Both G5

#### T07.G6.04 – Find and fix infinite loops
- **Size**: ✓ Appropriate (infinite loop debugging)
- **Age-appropriateness**: ✓ Good for G6 - understanding termination
- **Dependencies**: [T07.G3.01, T07.G3.02, T13.G5.02]
  - T13.G5.02: Testing edge cases
- **Notes**: **UNIQUE** - critical debugging skill
- **Grade-level check**: ✓ T13.G5.02 is G5

---

### Grade 7 (Ages 12-13)

#### T07.G7.01 – Loop for step-by-step simulation
- **Size**: ✓ Appropriate (simulation loops)
- **Age-appropriateness**: ✓ Perfect for G7 - physics/science simulations
- **Dependencies**: [T07.G5.01, T05.G7.04, T09.G6.01]
  - T05.G7.04: Simulation design
  - T09.G6.01: Advanced variable usage
- **Notes**: **UNIQUE** - simulation tick loops
- **Grade-level check**: ✓ Both G6-G7

#### T07.G7.02 – Nested loops for grid processing
- **Size**: ✓ Appropriate (2D data processing)
- **Age-appropriateness**: ✓ Good for G7 - matrix thinking
- **Dependencies**: [T07.G5.04, T10.G6.01, T25.G6.01]
  - T10.G6.01: 2D list structures
  - T25.G6.01: Data representation
- **Notes**: **UNIQUE** - 2D loop patterns
- **Grade-level check**: ✓ Both G6

#### T07.G7.03 – Compare two loop solutions
- **Size**: ✓ Appropriate (efficiency comparison)
- **Age-appropriateness**: ✓ Good - analytical thinking
- **Dependencies**: [T07.G6.02, T01.G7.02]
  - T01.G7.02: Choose right algorithm
- **Notes**: **UNIQUE** - loop efficiency analysis
- **Grade-level check**: ✓ T01.G7.02 is G7

#### T07.G7.04 – Recognize loop accumulator patterns
- **Size**: ✓ Appropriate (pattern recognition)
- **Age-appropriateness**: ✓ Perfect for G7 - meta-cognitive
- **Dependencies**: [T07.G5.03, T07.G6.03, T04.G7.01]
  - T04.G7.01: Spot loop patterns (recognition vs implementation)
- **Notes**: Meta-pattern skill - complements T04
- **Grade-level check**: ✓ T04.G7.01 is G7

---

### Grade 8 (Ages 13-14)

#### T07.G8.01 – Estimate probabilities using loops
- **Size**: ✓ Appropriate (Monte Carlo simulations)
- **Age-appropriateness**: ✓ **EXCELLENT** for G8 - advanced statistics
- **Dependencies**: [T07.G5.01, T28.G7.01, T27.G7.01]
  - T28.G7.01: Statistical sampling
  - T27.G7.01: Data analysis
- **Notes**: **UNIQUE** - Monte Carlo methods
- **Grade-level check**: ✓ Both G7

#### T07.G8.02 – Implement iterative algorithms (e.g., GCD)
- **Size**: ✓ Appropriate (classic algorithms)
- **Age-appropriateness**: ✓ Good for G8 - mathematical algorithms
- **Dependencies**: [T07.G7.03, T01.G7.01]
  - T01.G7.01: Identify algorithm patterns
- **Notes**: **UNIQUE** - iterative algorithm implementation
- **Grade-level check**: ✓ T01.G7.01 is G7

#### T07.G8.03 – Nested loops over 2D data
- **Size**: ✓ Appropriate (complex 2D processing)
- **Age-appropriateness**: ✓ Good - advanced data structures
- **Dependencies**: [T07.G7.02, T10.G7.01, T25.G7.01]
  - T10.G7.01: Advanced lists
  - T25.G7.01: Complex data representation
- **Notes**: **UNIQUE** - 2D data algorithms
- **Grade-level check**: ✓ Both G7

#### T07.G8.04 – Explain loop choices for a task
- **Size**: ✓ Appropriate (design justification)
- **Age-appropriateness**: ✓ Perfect - articulating reasoning
- **Dependencies**: [T07.G7.03, T01.G7.02]
- **Notes**: **UNIQUE** - loop design reasoning
- **Grade-level check**: ✓ T01.G7.02 is G7

---

## Summary

**Total Skills**: 35
**Granularity**: ✓ All appropriately sized
**Age-Appropriateness**: ✓ Excellent progression

**OVERLAP RESOLUTION**:

### Duplicates with T04 (ACTION REQUIRED):
1. **T07.GK.01** = T04.GK.01 → **KEEP T07**, coordinate with T04
2. **T07.G1.01** = T04.G1.01 → **KEEP T07**, T04 should reference
3. **T07.G1.04** = T04.G1.04 → **KEEP T07**, REMOVE from T04
4. **T07.G2.01** = T04.G2.02 → **KEEP T07**, T04 should reference
5. **T07.G3.03** = T04.G3.02 → **KEEP T07**, T04 should reference
6. **T07.G3.04** = T04.G3.04 → **KEEP T07**, T04 should reference

**Issues Found**: None - all dependencies properly ordered

**Cross-Topic Dependencies**:
- **T01** (Algorithms): Loop concepts from repetition
- **T02** (Representing): Loop tracing
- **T04** (Patterns): **OVERLAP** - T04 should reference T07 for implementation
- **T06** (Events): Loops inside events
- **T08** (Conditionals): Loops with conditions
- **T09** (Variables): Loop counters, accumulators
- **T10** (Lists): Loop over lists
- **T13** (Testing): Loop debugging
- **T25-T28** (Data): Loops for data processing
- **T05** (Simulation): Simulation loops

**Critical Loop Patterns Introduced**:
- G2: Basic repeat loop
- G3: Forever, repeat-until, nested loops
- G4: Loop counters
- G5: Accumulators, list population
- G6: Search patterns
- G7: 2D loops, efficiency
- G8: Monte Carlo, iterative algorithms

**Recommendation**:
- **NO CHANGES** to T07
- **UPDATE T04** to reference T07 skills instead of duplicating
- T07 is the **authoritative source** for loop implementation skills
