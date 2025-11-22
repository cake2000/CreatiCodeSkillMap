# T07 (Loops) Visual Skill Progression Map
**Date**: 2025-11-22

---

## LEGEND
- ✅ No issues found
- 🆕 NEW skill recommended
- 📝 Description needs update
- ⚠️ Needs verification
- 🔄 Dependency update needed (after K-2 added)

---

## K-2 FOUNDATION (PICTURE-BASED)

### Kindergarten
```
🆕 T07.K.01: Identify repeating patterns in picture sequences
   └─ Dependencies: T04.K.01
   └─ NEW: Critical foundation for loop concepts
```

### Grade 1
```
🆕 T07.G1.01: Complete a visual pattern by adding the repeated unit
   └─ Dependencies: T07.K.01, T04.G1.01
   └─ NEW: Active pattern construction

🆕 T07.G1.02: Count how many times a pattern unit repeats
   └─ Dependencies: T07.G1.01
   └─ NEW: Introduces counting iterations
```

### Grade 2
```
🆕 T07.G2.01: Match "do this N times" instructions to picture sequences
   └─ Dependencies: T07.G1.02, T04.G2.01
   └─ NEW: Direct preparation for repeat blocks
```

---

## GRADE 3: BASIC LOOPS (5 skills)

### Foundation Loop Blocks
```
🔄 T07.G3.01: Use a counted repeat loop
   └─ Dependencies: T06.G3.01, T04.G1.01, T04.G2.01, T01.G2.05
   └─ UPDATE: Add T07.G2.01 dependency after K-2 added
   └─ Gateway skill for all loops

✅ T07.G3.02: Trace a script with a simple loop
   └─ Dependencies: T07.G3.01, T04.G3.02
   └─ No issues

✅ T07.G3.03: Build a forever loop for simple animation
   └─ Dependencies: T07.G3.01, T04.G3.03
   └─ No issues
```

### Conditional Loops & Debugging
```
✅ T07.G3.04: Use repeat-until to reach a simple goal
   └─ Dependencies: T07.G3.03, T09.G3.02
   └─ No issues

✅ T07.G3.05: Fix a simple repeat loop count
   └─ Dependencies: T07.G3.04, T08.G3.03
   └─ No issues
```

---

## GRADE 4: LOOPS + CONTROL FLOW (8 skills)

### Game Loops & Conditionals
```
✅ T07.G4.01: Create a forever game loop for controls
   └─ Dependencies: T06.G3.01, T07.G3.01, T07.G3.03, T07.G3.05, T08.G3.01
   └─ No issues

✅ T07.G4.02: Use an if statement inside a loop
   └─ Dependencies: T06.G3.01, T07.G3.01, T07.G3.04, T08.G3.01, T09.G3.01
   └─ No issues
```

### Counter Variables & For-Loops
```
📝 T07.G4.03: Use a loop counter variable and for loops
   └─ Dependencies: T06.G3.01, T07.G3.01, T07.G3.05, T09.G3.01
   └─ RECOMMEND SPLIT into:
      ├─ T07.G4.03: Use a loop counter variable to track iterations
      └─ T07.G4.03.01: Use for-loops with start, limit, and step parameters
   └─ Two distinct concepts in one skill
```

### Refactoring & Debugging
```
✅ T07.G4.04: Identify and convert simple repeated code into loops
   └─ Dependencies: T06.G3.01, T07.G3.01, T07.G3.04, T08.G3.01
   └─ No issues

✅ T07.G4.05: Debug complex loop conditions and boundaries
   └─ Dependencies: T06.G3.01, T07.G3.01, T07.G3.04, T08.G3.01, T09.G3.01
   └─ No issues

✅ T07.G4.06: Trace code that combines a loop and a condition
   └─ Dependencies: T06.G3.01, T07.G3.01, T07.G3.04, T08.G3.01
   └─ No issues
```

### Nested Loops & Timing
```
📝 T07.G4.07: Trace simple nested loops with fixed bounds
   └─ Dependencies: T07.G4.03, T07.G4.06
   └─ UPDATE: Clarify why G4.03 dependency helps with fixed bounds
   └─ Intra-grade dependency (valid but note sequencing)

✅ T07.G4.08: Use timed repeat for spaced animations
   └─ Dependencies: T07.G3.01, T07.G4.01
   └─ No issues
```

---

## GRADE 5: LOOPS + DATA (4 skills)

### Applications: Probability, Lists, Computation
```
✅ T07.G5.01: Simulate repeated experiments with a loop
   └─ Dependencies: T07.G4.05, T07.G4.06
   └─ No issues

✅ T07.G5.02: Build a list with a loop
   └─ Dependencies: T07.G4.05, T07.G4.06
   └─ No issues

✅ T07.G5.03: Use loops to compute aggregates
   └─ Dependencies: T07.G4.03, T07.G4.06
   └─ No issues
```

### Advanced Patterns
```
✅ T07.G5.04: Nested loops for advanced patterns or tilings
   └─ Dependencies: T07.G4.05, T07.G4.07
   └─ No issues
```

### Optional G5 Expansion
```
🆕 T07.G5.05: Use loops with user input to build interactive sequences
   └─ Dependencies: T07.G4.05, T07.G5.02, T10.G4.01
   └─ OPTIONAL: Bridges loops + input

🆕 T07.G5.06: Trace loops that modify list items
   └─ Dependencies: T07.G5.02, T07.G5.03, T09.G4.01
   └─ OPTIONAL: In-place list modification
```

---

## GRADE 6: NESTED LOOPS + OPTIMIZATION (8 skills + 1 new)

### Nested Loop Mastery
```
✅ T07.G6.01: Trace nested loops with variable bounds
   └─ Dependencies: T07.G4.03, T07.G5.03, T07.G5.04, T09.G4.01
   └─ No issues

✅ T07.G6.02: Refactor complex repeated patterns into loops with variables
   └─ Dependencies: T07.G4.03, T07.G4.04, T07.G5.04
   └─ No issues
```

### List Processing
```
✅ T07.G6.03: Loop-based search in a list
   └─ Dependencies: T07.G5.02, T07.G5.03, T09.G4.01
   └─ No issues

✅ T07.G6.04: Avoid and fix infinite loops
   └─ Dependencies: T07.G4.05, T07.G5.01, T07.G5.04, T08.G3.01
   └─ No issues
```

### Tracing Techniques
```
📝 T07.G6.05: Trace nested loops using a trace table
   └─ Dependencies: T07.G5.03, T07.G5.04, T09.G4.01
   └─ UPDATE: Clarify this is GENERAL METHODOLOGY
   └─ Emphasize trace table as tool for any nested loop

📝 T07.G6.06: Trace nested loops that generate visual patterns
   └─ Dependencies: T07.G5.03, T07.G5.04, T08.G3.01
   └─ UPDATE: Clarify this is VISUAL APPLICATION
   └─ ADD: T07.G6.05 as dependency (uses trace table technique)
   └─ Distinguish from G6.05: specific use case vs general method
```

### Iterative Updates
```
✅ T07.G6.07: Use loops to update values iteratively
   └─ Dependencies: T07.G5.01, T07.G5.03, T07.G6.05
   └─ No issues
```

### Loop Control
```
⚠️ T07.G6.08: Use break and continue to control loop flow
   └─ Dependencies: T07.G5.02, T07.G6.03, T07.G6.04
   └─ VERIFY: Do "break out of loop" and "continue to next iteration" blocks exist?
   └─ If not, revise to use flag variables + conditionals
```

### NEW: For-Each Iteration
```
🆕 T07.G6.09: Use for-each loops to iterate through lists
   └─ Dependencies: T07.G5.02, T07.G6.03, T09.G4.01
   └─ NEW: Covers `for each item/index in [list]` blocks
   └─ CRITICAL: CreatiCode has these blocks but no skill teaches them
```

---

## GRADE 7: SIMULATIONS + ALGORITHMS (4 skills + 1 optional)

### Physics & Data Structures
```
📝 T07.G7.01: Use loops to simulate motion over time
   └─ Dependencies: T07.G6.05, T07.G6.06, T07.G6.07
   └─ UPDATE: Add bridging context connecting to G6.07 iterative updates
   └─ Explain time-step concept

✅ T07.G7.02: Nested loops for 2D grids and tile maps
   └─ Dependencies: T07.G6.05, T07.G6.06, T08.G6.01
   └─ No issues
```

### Algorithm Analysis
```
✅ T07.G7.03: Compare loop algorithms by counting steps
   └─ Dependencies: T07.G6.05, T07.G6.07, T08.G6.01
   └─ No issues

✅ T07.G7.04: Loop patterns for counting and accumulation
   └─ Dependencies: T07.G6.05, T07.G6.07, T08.G6.01, T09.G5.01
   └─ No issues
```

### Optional: Optimization
```
🆕 T07.G7.05: Optimize loop bounds to reduce unnecessary iterations
   └─ Dependencies: T07.G6.08, T07.G7.03, T07.G7.04
   └─ OPTIONAL: Explicit efficiency skill (partially covered in G8.02.02)
   └─ Examples: testing divisors up to √n, using break to exit early
```

---

## GRADE 8: ADVANCED ALGORITHMS (7 skills)

### Monte Carlo & Iterative Design
```
✅ T07.G8.01: Monte Carlo simulations with loops
   └─ Dependencies: T07.G6.01, T07.G7.03, T07.G7.04
   └─ No issues

📝 T07.G8.02: Design iterative algorithms with loops
   └─ Dependencies: T01.G6.01, T07.G6.01, T07.G7.03, T07.G7.04, T08.G6.01
   └─ REWRITE: Too vague - "learn the general pattern"
   └─ NEW FOCUS: Identify when iteration needed + 3-component framework
   └─ Make specific and assessable
```

### Classic Algorithms (Sub-skills)
```
✅ T07.G8.02.01: Implement GCD using repeated subtraction in a loop
   └─ Dependencies: T07.G8.02, T09.G6.01
   └─ No issues (verify alignment after G8.02 rewrite)

✅ T07.G8.02.02: Check if a number is prime using trial division
   └─ Dependencies: T07.G8.02, T08.G6.01
   └─ No issues (verify alignment after G8.02 rewrite)

✅ T07.G8.02.03: Find Fibonacci numbers using iterative calculation
   └─ Dependencies: T07.G8.02, T09.G6.01
   └─ No issues (verify alignment after G8.02 rewrite)
```

### Data Processing & Analysis
```
✅ T07.G8.03: Process structured data with nested loops
   └─ Dependencies: T07.G6.01, T07.G7.03, T07.G7.04, T09.G6.01
   └─ No issues

✅ T07.G8.04: Analyze and justify loop design choices
   └─ Dependencies: T07.G6.01, T07.G7.03, T07.G7.04, T08.G6.01, T09.G6.01
   └─ No issues
```

---

## PROGRESSION SUMMARY BY GRADE

```
K-2 FOUNDATION (RECOMMENDED: 4 skills)
├─ K: Pattern recognition (1 skill) 🆕
├─ G1: Pattern completion + counting (2 skills) 🆕
└─ G2: "Do N times" matching (1 skill) 🆕

G3-4 CORE LOOPS (13 skills)
├─ G3: Basic loops (5 skills) ✅ Strong
└─ G4: Control flow + nested (8 skills) ✅ Strong

G5-6 APPLICATIONS (12-14 skills)
├─ G5: Data + probability (4+2 optional) ⚠️ Light coverage
└─ G6: Nested + optimization (8+1 new) ✅ Strong

G7-8 ADVANCED (11-12 skills)
├─ G7: Simulations + analysis (4+1 optional) ✅ Strong
└─ G8: Algorithms + design (7 skills) ✅ Strong
```

---

## DEPENDENCY FLOW VISUALIZATION

### K-2 → G3 Bridge (CRITICAL GAP)
```
CURRENT (BROKEN):
T04.G1.01 ─┐
T04.G2.01 ─┼─→ T07.G3.01 (Uses other topic's patterns)
T01.G2.05 ─┘

RECOMMENDED (FIXED):
T07.K.01 → T07.G1.01 → T07.G1.02 → T07.G2.01 ─┐
T04.G1.01 ────────────────────────────────────┼─→ T07.G3.01
T04.G2.01 ────────────────────────────────────┤   (Own foundation
T01.G2.05 ────────────────────────────────────┘    + cross-topic)
```

### G3 → G4 Progression
```
T07.G3.01 (repeat) ──┬─→ T07.G4.01 (forever game)
                     ├─→ T07.G4.03 (counter/for-loop)
                     └─→ T07.G4.04 (refactor)

T07.G3.04 (repeat-until) ──┬─→ T07.G4.02 (if in loop)
                            └─→ T07.G4.05 (debug)

T07.G4.03 + T07.G4.06 ────→ T07.G4.07 (nested trace)
                              ↓
                            (Intra-grade dependency - note sequencing)
```

### G6 Tracing Skills (OVERLAP CONCERN)
```
CURRENT (UNCLEAR):
T07.G5.03 ──┬─→ T07.G6.05 (trace table)
T07.G5.04 ──┘

T07.G5.03 ──┬─→ T07.G6.06 (visual patterns)
T07.G5.04 ──┘
            ↓
          (Both trace nested loops - why separate?)

RECOMMENDED (CLARIFIED):
T07.G5.03 ──┬─→ T07.G6.05 (trace table METHODOLOGY)
T07.G5.04 ──┘        ↓
                     └──→ T07.G6.06 (APPLY to visual patterns)
                          (Uses technique from G6.05)
```

### Missing For-Each Pattern
```
CURRENT (GAP):
T07.G5.02 (build list) ──→ T07.G6.03 (search in list)
                           Uses manual indexing only

RECOMMENDED (FILLED):
T07.G5.02 (build list) ──→ T07.G6.09 (for-each loops) 🆕
                           ↓
T07.G6.03 (search) ────────┘
                           (Can use for-each OR manual)
```

---

## ISSUE HEAT MAP

### By Grade Level
```
K-2:  🔴🔴🔴🔴 (CRITICAL - Missing entirely)
G3:   🟡 (Minor - dependency update needed)
G4:   🟡 (Minor - split one skill, document sequencing)
G5:   🟡 (Minor - could add 2 optional skills)
G6:   🟠 (Medium - needs new skill + clarifications)
G7:   🟢 (Good - optional optimization skill)
G8:   🟠 (Medium - rewrite one skill)
```

### By Issue Type
```
Missing Skills:     🔴 K-2 foundation (4), G6 for-each (1)
Vague Descriptions: 🟠 G8.02
Block Verification: 🟠 G6.08 (break/continue)
Overlap/Duplicate:  🟡 G6.05/G6.06 distinction
Dependency Issues:  🟡 G3.01 (after K-2), G4.07 sequencing
Skill Granularity:  🟡 G4.03 (split recommended)
```

---

## RECOMMENDED IMPLEMENTATION ORDER

### Week 1: Critical K-2 Foundation
1. Create T07.K.01, G1.01, G1.02, G2.01
2. Update T07.G3.01 dependencies
3. Verify cross-references with T04 skills

### Week 2: Block Verification & Fixes
1. Verify break/continue blocks in CreatiCode
2. Fix or revise T07.G6.08
3. Add T07.G6.09 (for-each loops)

### Week 3: Description Updates
1. Rewrite T07.G8.02 (iterative algorithms)
2. Clarify T07.G6.05/G6.06 distinction
3. Enhance T07.G7.01 context
4. Update T07.G4.07 clarification

### Week 4: Optional Enhancements
1. Consider splitting T07.G4.03
2. Consider adding G5.05, G5.06, G7.05
3. Create G4 sequencing guide
4. Verify G8.02 sub-skills

---

## FILES GENERATED

1. **T07_COMPREHENSIVE_ANALYSIS.md** - Detailed issue analysis
2. **T07_ACTION_PLAN.md** - Implementation guide with skill definitions
3. **T07_EXECUTIVE_SUMMARY.md** - High-level decision maker summary
4. **T07_VISUAL_PROGRESSION.md** - This visual progression map

---

**Status**: Analysis complete. Ready for Phase 1 implementation.
