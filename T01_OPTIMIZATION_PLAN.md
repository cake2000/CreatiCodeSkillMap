# T01 - EVERYDAY ALGORITHMS: PHASE 1 OPTIMIZATION PLAN

**Date**: 2025-11-22
**Total Skills**: 97
**Grade Range**: Kindergarten (GK) through Grade 8 (G8)
**Analysis Source**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/T01_COMPLETE_EXTRACTION.md`

---

## EXECUTIVE SUMMARY

This optimization plan identifies **42 specific issues** across T01's 97 skills, categorized by priority:
- **HIGH Priority**: 15 issues (must fix for Phase 1)
- **MEDIUM Priority**: 18 issues (should fix for Phase 1)
- **LOW Priority**: 9 issues (nice to have improvements)

**Key Finding**: T01 shows excellent structure in K-2 (picture-based, minimal dependencies), but has significant issues in G3-G8 including overly complex skills, unclear progression, and redundant learning objectives.

**Critical Constraint**: We MUST preserve ALL external dependencies to other topics (T02-T36). Only internal T01 dependencies can be modified.

---

## HIGH PRIORITY ISSUES (Must Fix)

### H1: T01.G8.10 - Massive Capstone Skill with 288 Dependencies

**Skill ID**: T01.G8.10
**Title**: "Facilitate capstone retrospectives with stakeholders"
**Problem**:
- Has 288 external dependencies spanning T02, T03, T04, T05
- Too broad and complex for a single skill
- Belongs in a different topic (likely T05 - Human-Centered Design or a new capstone topic)
- Not focused on "everyday algorithms" - this is project management

**Proposed Solution**:
- SPLIT into 4 sub-skills:
  - **T01.G8.10.01**: "Reflect on algorithm choices made during a project"
  - **T01.G8.10.02**: "Document algorithm trade-offs and design decisions"
  - **T01.G8.10.03**: "Compare initial vs. final algorithm implementations"
  - **T01.G8.10.04**: "Present algorithm evolution to stakeholders"
- Each sub-skill focuses specifically on algorithmic thinking
- Preserve all 288 external dependencies distributed across sub-skills

**Impact on Dependencies**: None - splits preserve all existing dependencies

---

### H2: G3 Transition Too Abrupt (0% → 100% External Dependencies)

**Skills Affected**: All G2 and G3 skills
**Problem**:
- G1 and G2 have 0% external dependencies (picture-based)
- G3 has 100% external dependencies (code-based)
- No scaffolding between abstract concepts and code implementation
- Students jump from "write directions using repeat" (G2) to "replace repeated blocks" (G3) without transition

**Proposed Solution**:
Add bridging skills in late G2:
- **T01.G2.16**: "Match code blocks to picture sequences"
  - Description: "Look at a picture sequence. Which set of code blocks does the same thing?"
  - Dependencies: T01.G2.03, T06.G3.01 (EXTERNAL - NEW)
  - Prepares students for G3 transition

- **T01.G2.17**: "Identify the action each code block performs"
  - Description: "Look at simple code blocks (move, turn, say). What does each block do?"
  - Dependencies: T01.G2.02, T06.G3.01 (EXTERNAL - NEW)

**Impact on Dependencies**:
- Adds 2 new external dependencies to G2 (gradual transition)
- Reduces cognitive load in G3

---

### H3: Redundant "Trace" Skills Across Multiple Grades

**Skills Affected**: T01.G2.09, T01.G2.12, T01.G3.06, T01.G3.10, T01.G4.07, T01.G4.10, T01.G5.04, T01.G7.04, T01.G8.05

**Problem**:
- Multiple skills ask students to "trace" or "follow" algorithms step-by-step
- Unclear differentiation between grade levels
- Example:
  - T01.G2.09: "Trace an algorithm that uses 'repeat ___ times'"
  - T01.G2.12: "Trace an algorithm with if/then and repeat"
  - T01.G3.06: "Trace a repeat loop to find total movement"
  - T01.G3.10: "Trace a script with a single if/then"
  - T01.G4.07: "Trace a simple counter variable"
  - T01.G4.10: "Trace a multi-step algorithm with loops and variables"

**Proposed Solution**:
CLARIFY each tracing skill with specific complexity:
- **T01.G2.09**: Add "with 3-5 steps total" to description
- **T01.G2.12**: Add "with one if/then and one repeat (max 3 repetitions)"
- **T01.G3.06**: Add "calculating total distance or rotation"
- **T01.G3.10**: Add "with 2-3 possible conditions"
- **T01.G4.07**: Add "through 5-10 iterations"
- **T01.G4.10**: Add "with 2-3 variables changing values"
- **T01.G5.04**: Already specific (search algorithm)
- **T01.G7.04**: Already specific (sorting algorithm)
- **T01.G8.05**: Already specific (recursive algorithm)

**Impact on Dependencies**: None - only description improvements

---

### H4: T01.GK.03 and T01.GK.07 - Unclear Dependencies

**Skills Affected**: T01.GK.03, T01.GK.07
**Problem**:
- **T01.GK.03**: "Find the first and last pictures" - depends on T01.GK.01
  - But T01.GK.01 is "Put pictures in order for getting ready for bed"
  - Why does finding first/last depend on a specific ordering task?
- **T01.GK.07**: "Find the pattern that repeats" - depends on T01.GK.03
  - Pattern recognition doesn't require understanding first/last

**Proposed Solution**:
- **T01.GK.03**: Change dependency from T01.GK.01 to T01.GK.02
  - T01.GK.02 is more general (4 pictures vs. 3) and better prerequisite
- **T01.GK.07**: REMOVE dependency on T01.GK.03
  - Make it depend on T01.GK.01 instead (understanding sequences is sufficient)

**Impact on Dependencies**: Internal T01 only - safe to modify

---

### H5: T01.G1.07 vs T01.G1.02 - Duplicate Skills

**Skills Affected**: T01.G1.02, T01.G1.07
**Problem**:
- **T01.G1.02**: "Match two different ways to do the same thing" - "Look at two algorithms. Do they both get to the same place?"
- **T01.G1.07**: "Decide if two algorithms finish with the same result" - "Look at two different algorithms. Do they both end up at the same place?"
- These are IDENTICAL learning objectives

**Proposed Solution**:
MERGE into single skill:
- **Keep T01.G1.02** (appears first)
- **DELETE T01.G1.07** and update any skills that depend on it to depend on T01.G1.02 instead
- **T01.G1.08** currently depends on T01.G1.07 → change to T01.G1.02

**Impact on Dependencies**:
- Internal only (T01.G1.08 dependency updated)
- Reduces G1 from 10 to 9 skills

---

### H6: Missing Scaffolding - "Repeat Until" vs "Repeat N Times"

**Skills Affected**: All G2-G4 loop skills
**Problem**:
- G2 introduces "repeat N times" (counted loops)
- No skills address "repeat until" (conditional loops) until much later
- Students may encounter both types in actual coding
- Gap in conceptual understanding

**Proposed Solution**:
Add new skill in G4:
- **T01.G4.13**: "Compare 'repeat N times' with 'repeat until' loops"
  - Description: "Look at two scripts that do the same thing. One uses 'repeat 10' and one uses 'repeat until touching edge.' What's different?"
  - Dependencies: T07.G3.01, T07.G4.01 (EXTERNAL)
  - CSTA: 1B-AP-12

**Impact on Dependencies**: Adds external dependency (acceptable for new skill)

---

### H7: T01.G4.01 and T01.G4.02 - Overly Generic

**Skills Affected**: T01.G4.01, T01.G4.02
**Problem**:
- **T01.G4.01**: "Plan a short program before coding it" - too vague
- **T01.G4.02**: "Implement a written plan in code" - too vague
- What constitutes "planning"? Pseudocode? Flowchart? Notes?
- No specific guidance on planning methods

**Proposed Solution**:
ENHANCE descriptions with specificity:
- **T01.G4.01**: "Plan a short program before coding it using step-by-step notes"
  - Add to description: "Write 5-8 steps in plain language describing what your program should do."
- **T01.G4.02**: "Implement a written plan in code"
  - Add to description: "Take your step-by-step plan from T01.G4.01 and convert each step into 1-3 code blocks."

**Impact on Dependencies**: None - description enhancements only

---

### H8: T01.G5.02.01 and T01.G5.02.02 - Inconsistent Numbering

**Skills Affected**: T01.G5.02.01, T01.G5.02.02
**Problem**:
- These use sub-IDs but there's no T01.G5.02 parent skill
- Inconsistent with rest of skill map (no other grade uses .01/.02 pattern)
- Should either be T01.G5.02 and T01.G5.03, or split differently

**Proposed Solution**:
RENUMBER for consistency:
- **T01.G5.02.01** → **T01.G5.02**: "Convert a simple flowchart into code"
- **T01.G5.02.02** → **T01.G5.03**: "Convert simple pseudocode into code"
- **Current T01.G5.03** → **T01.G5.04**: "Convert a short program into pseudocode"
- Continue renumbering: G5.04→G5.05, G5.05→G5.06, etc.

**Impact on Dependencies**:
- Internal dependencies need updating
- External dependencies pointing TO these skills need updating (coordinate with other topics)

---

### H9: T01.G3.12 - Unclear Dependency

**Skills Affected**: T01.G3.12
**Problem**:
- **T01.G3.12**: "Predict the final state of a simple algorithm"
- Depends on **T14.G3.01**: "Move a sprite with arrow keys (4 directions)"
- Why does predicting algorithm outcomes depend on keyboard control?
- This dependency doesn't make sense

**Proposed Solution**:
REPLACE dependency:
- Change from T14.G3.01 (arrow keys) to T06.G3.01 (basic sequencing)
- Or add dependency on T09.G3.01.04 (variables) since "state" implies tracking values

**Impact on Dependencies**: Changes external dependency (coordinate with optimization)

---

### H10: Missing "Debugging Mindset" Progression

**Skills Affected**: T01.G3.13, T01.G3.14, T01.G3.15, scattered debugging skills
**Problem**:
- Debugging skills appear suddenly in G3 without prior introduction
- G1 has "Check a completed routine for mistakes" (T01.G1.05)
- G2 has "Fix a repeat count that's wrong" (T01.G2.10)
- But no systematic debugging progression
- G3 debugging skills assume knowledge not scaffolded

**Proposed Solution**:
ADD bridging skill in G2:
- **T01.G2.18**: "Find and explain what's wrong with a broken algorithm"
  - Description: "Look at an algorithm that doesn't work correctly. What's wrong? Why doesn't it work? (You don't need to fix it yet.)"
  - Dependencies: T01.G2.14
  - Prepares for G3 debugging skills

**Impact on Dependencies**: None - new skill adds to progression

---

### H11: T01.G6.01 - Wrong Dependency

**Skills Affected**: T01.G6.01
**Problem**:
- **T01.G6.01**: "Compare efficiency of linear and binary search"
- Depends on **T04.G2.01**: "Identify the repeating unit in a longer pattern"
- Binary search is NOT about patterns - it's about search algorithms
- Should depend on T01.G5.04 (search algorithm tracing)

**Proposed Solution**:
REPLACE dependency:
- Remove: T04.G2.01 (patterns - EXTERNAL)
- Add: T01.G5.04 (trace search algorithm - INTERNAL)

**Impact on Dependencies**:
- Removes 1 external dependency
- Adds 1 internal dependency
- Better conceptual alignment

---

### H12: Inconsistent Variable Introduction

**Skills Affected**: T01.G4.06, T01.G4.07, T01.G4.08, T01.G4.09
**Problem**:
- G4 has 4 skills about variables (recognize, trace, add, use)
- All depend on T09.G3.01.04 (display variable on stage)
- But this is too narrow - students need broader variable understanding
- Skills feel redundant

**Proposed Solution**:
CONSOLIDATE and CLARIFY:
- **T01.G4.06**: Keep as "Recognize variables in a program" (identification)
- **T01.G4.07**: Keep as "Trace a simple counter variable" (tracing)
- **MERGE T01.G4.08 + T01.G4.09** → **T01.G4.08**: "Use a variable to track changing values"
  - Description: "Create a program that uses a variable to track something that changes (like points in a game or times a button is clicked)."
  - Dependencies: T06.G3.01, T08.G3.01, T09.G3.01.04 (EXTERNAL)
- **DELETE T01.G4.09** (redundant with merged T01.G4.08)
- Renumber: T01.G4.10→G4.09, T01.G4.11→G4.10, T01.G4.12→G4.11

**Impact on Dependencies**:
- Internal dependencies need updating
- Reduces G4 from 12 to 11 skills

---

### H13: T01.G5.10 - "Helper Steps" Undefined

**Skills Affected**: T01.G5.10
**Problem**:
- **T01.G5.10**: "Rewrite a long algorithm using loops or helper steps"
- "Helper steps" is undefined at this point
- Functions/procedures aren't introduced until later topics
- Confusing terminology

**Proposed Solution**:
CLARIFY description:
- Change "helper steps" to "repeated blocks organized into loops"
- Remove vague reference to undefined concept
- New description: "Look at a long, repetitive algorithm. Rewrite it using loops to reduce repetition."

**Impact on Dependencies**: None - description clarification only

---

### H14: Missing Skill - Algorithm Correctness vs. Efficiency

**Skills Affected**: G5-G6 skills
**Problem**:
- G4 ends with "Explain why an algorithm is correct or incorrect" (T01.G4.12)
- G6 starts with "Compare efficiency of linear and binary search" (T01.G6.01)
- Missing bridge: students need to understand that CORRECT doesn't mean EFFICIENT
- Gap in conceptual understanding

**Proposed Solution**:
ADD new skill in G5:
- **T01.G5.12**: "Distinguish between algorithm correctness and efficiency"
  - Description: "Look at two correct algorithms that solve the same problem. Both are correct, but one is faster. Why do we care about efficiency if both work?"
  - Dependencies: T01.G4.12, T01.G5.06
  - CSTA: 1B-AP-17

**Impact on Dependencies**: Internal only - builds on existing skills

---

### H15: T01.G7.01 - Overly Advanced Dependency

**Skills Affected**: T01.G7.01
**Problem**:
- **T01.G7.01**: "Identify the pattern in a given program"
- Depends on **T06.G7.01** (state machines) and **T09.G7.04** (variable scope)
- These are very advanced topics - not necessary for pattern identification
- Should depend on simpler skills

**Proposed Solution**:
REPLACE dependencies:
- Remove: T06.G7.01 (state machines - EXTERNAL)
- Remove: T09.G7.04 (variable scope - EXTERNAL)
- Add: T01.G5.09 (explain algorithm with loops/variables - INTERNAL)
- Add: T01.G6.02 (best/worst case - INTERNAL)

**Impact on Dependencies**:
- Removes 2 external dependencies
- Adds 2 internal dependencies
- More appropriate skill level

---

## MEDIUM PRIORITY ISSUES (Should Fix)

### M1: Inconsistent Terminology - "Algorithm" vs "Program" vs "Script"

**Skills Affected**: Multiple across all grades
**Problem**:
- K-2 use "algorithm" and "routine"
- G3 introduces "script" and "program"
- G4+ mix "algorithm," "program," "script," "code"
- No clear definition of when to use which term

**Proposed Solution**:
STANDARDIZE terminology:
- **K-2**: Use "algorithm" and "routine" (abstract, picture-based)
- **G3-G4**: Use "script" (matches Scratch terminology)
- **G5+**: Use "program" and "algorithm" interchangeably
- Add glossary note in skill map

**Impact on Dependencies**: None - terminology clarification

---

### M2: T01.G1.09 and T01.G1.10 - Overlapping Skills

**Skills Affected**: T01.G1.09, T01.G1.10
**Problem**:
- **T01.G1.09**: "Match a simple if/then rule to a picture"
- **T01.G1.10**: "Match pictures to 'if/then' rules"
- Both are matching exercises
- T01.G1.09 has no dependencies; T01.G1.10 depends on T01.GK.04

**Proposed Solution**:
CLARIFY differentiation:
- **T01.G1.09**: "Match ONE if/then rule to ONE picture"
  - Add to description: "Given one rule and one picture, determine if they match."
- **T01.G1.10**: "Match MULTIPLE pictures to MULTIPLE if/then rules"
  - Add to description: "Given 3-4 pictures and 3-4 rules, match each picture to its correct rule."
- Make T01.G1.10 depend on T01.G1.09 (progression from single to multiple)

**Impact on Dependencies**:
- Adds internal dependency (T01.G1.09 → T01.G1.10)
- Removes dependency from T01.GK.04 to T01.G1.09

---

### M3: T01.G2.04 - Redundant with T01.G1.10

**Skills Affected**: T01.G2.04
**Problem**:
- **T01.G2.04**: "Match if/then rules to pictures"
- **T01.G1.10**: "Match pictures to 'if/then' rules"
- These are the same skill, just reworded
- T01.G2.04 depends on T01.G1.10

**Proposed Solution**:
DIFFERENTIATE by adding complexity:
- **T01.G2.04**: Change to "Match if/then rules to pictures with MULTIPLE conditions"
  - Add to description: "Look at pictures showing different situations. Some rules have TWO conditions (If it's raining AND cold, take umbrella and jacket). Match complex rules to pictures."

**Impact on Dependencies**: None - clarification only

---

### M4: T01.G3.03 vs T01.G3.04 - Similar Skills

**Skills Affected**: T01.G3.03, T01.G3.04
**Problem**:
- **T01.G3.03**: "Identify repeated blocks in a script (no loops)"
- **T01.G3.04**: "Predict how many times repeated blocks run"
- Very similar - both look at repeated blocks before loops

**Proposed Solution**:
MERGE into single skill:
- **Keep T01.G3.03**: "Identify and count repeated blocks in a script"
  - Description: "Look at a script. Which blocks repeat? How many times do they run? (The script doesn't use loops yet.)"
  - Dependencies: T06.G3.01, T04.G2.01 (EXTERNAL)
- **DELETE T01.G3.04**
- Update T01.G3.05 to depend on new T01.G3.03

**Impact on Dependencies**:
- Internal dependency update
- Reduces G3 from 15 to 14 skills

---

### M5: T01.G3.08 and T01.G3.09 - Overlapping Skills

**Skills Affected**: T01.G3.08, T01.G3.09
**Problem**:
- **T01.G3.08**: "Add a simple if/then to a script"
- **T01.G3.09**: "Match an if/then script to a behavior description"
- T01.G3.08 is creation; T01.G3.09 is recognition
- Should be in opposite order (recognize before create)

**Proposed Solution**:
SWAP order and clarify:
- **Rename T01.G3.08 → T01.G3.09**: "Add a simple if/then to a script" (creation)
- **Rename T01.G3.09 → T01.G3.08**: "Match an if/then script to a behavior description" (recognition)
- Update dependencies accordingly

**Impact on Dependencies**: Internal renumbering only

---

### M6: Missing Skill - "Repeat Forever" Loops

**Skills Affected**: G3 loop skills
**Problem**:
- G3 introduces "repeat N times" counted loops
- No mention of "repeat forever" (forever loops)
- These are fundamental in Scratch/block coding
- Gap in coverage

**Proposed Solution**:
ADD new skill in G3:
- **T01.G3.16**: "Identify when to use 'repeat forever' vs 'repeat N times'"
  - Description: "Look at two scripts. One needs to run forever (like checking if a key is pressed). One needs to run a specific number of times (like drawing a square). Which loop should each use?"
  - Dependencies: T07.G3.01, T07.G3.02 (EXTERNAL)
  - CSTA: 1B-AP-12

**Impact on Dependencies**: Adds external dependency to loop skills

---

### M7: T01.G4.03 and T01.G4.04 - Redundant Progression

**Skills Affected**: T01.G4.03, T01.G4.04
**Problem**:
- **T01.G4.03**: "Identify repeated patterns in longer scripts"
- **T01.G4.04**: "Replace repeated patterns with loops"
- This is the same progression as G3 (T01.G3.03 → T01.G3.05)
- What makes G4 more advanced?

**Proposed Solution**:
CLARIFY complexity difference:
- **T01.G4.03**: Add "in scripts with 20+ blocks and multiple sequences"
- **T01.G4.04**: Add "including nested patterns (patterns inside patterns)"
- Make clear this is about MORE COMPLEX scripts than G3

**Impact on Dependencies**: None - clarification only

---

### M8: T01.G4.05 - Unclear Learning Objective

**Skills Affected**: T01.G4.05
**Problem**:
- **T01.G4.05**: "Compare two versions of a script: with and without loops"
- Description: "Look at two scripts that do the same thing. One uses loops, one doesn't. What's different?"
- What is the learning objective? Efficiency? Readability?
- Too vague

**Proposed Solution**:
CLARIFY objective:
- Change description to: "Look at two scripts that do the same thing. One uses loops, one doesn't. Which is easier to read? Which is shorter? Why is using loops better?"
- Add explicit learning objective: understanding benefits of abstraction

**Impact on Dependencies**: None - clarification only

---

### M9: T01.G5.01 - Isolated Flowchart Skill

**Skills Affected**: T01.G5.01
**Problem**:
- **T01.G5.01**: "Match a word description to a flowchart" (G5)
- Next flowchart skill is **T01.G6.07**: "Design a flowchart for a multi-step program" (G6)
- Gap of 1 full grade
- No progression from matching to creating

**Proposed Solution**:
ADD intermediate skill in G5:
- **T01.G5.13**: "Create a simple flowchart from a word description"
  - Description: "Read a 5-7 step algorithm description. Draw a flowchart with sequence, decision, and loop symbols."
  - Dependencies: T01.G5.01, T01.G5.02 (flowchart to code)
  - CSTA: 1B-AP-11

**Impact on Dependencies**: Internal only - builds progression

---

### M10: T01.G5.05 - Too Advanced for G5

**Skills Affected**: T01.G5.05
**Problem**:
- **T01.G5.05**: "Determine whether an algorithm is correct for all inputs"
- This is a very sophisticated skill (formal verification concept)
- Depends on G3 skills only (big gap)
- May be too abstract for G5

**Proposed Solution**:
REFRAME for age-appropriateness:
- Change to: "Test an algorithm with different inputs to find bugs"
- Description: "Look at an algorithm. Try it with 3-5 different inputs (small numbers, large numbers, zero, negative). Does it work every time? If not, which inputs break it?"
- Make it concrete (testing) rather than abstract (formal correctness)

**Impact on Dependencies**: None - reframing only

---

### M11: T01.G5.07 and T01.G5.08 - Redundant Edge Case Skills

**Skills Affected**: T01.G5.07, T01.G5.08
**Problem**:
- **T01.G5.07**: "Debug an algorithm that mis-handles a simple edge case"
- **T01.G5.08**: "Add checks to handle edge cases"
- T01.G5.07 is debugging; T01.G5.08 is preventing
- But learning objective is nearly identical

**Proposed Solution**:
MERGE into single comprehensive skill:
- **Keep T01.G5.07**: "Identify and fix edge case bugs"
  - Description: "Look at an algorithm that works for most inputs but fails for edge cases (like zero, empty lists, or boundary values). Find the bug and add checks to handle these cases."
  - Dependencies: T06.G3.01, T08.G3.01 (EXTERNAL)
- **DELETE T01.G5.08** (redundant)
- Renumber: G5.09→G5.08, G5.10→G5.09, G5.11→G5.10

**Impact on Dependencies**: Internal renumbering

---

### M12: T01.G5.11 - Overlaps with T01.G2.14

**Skills Affected**: T01.G5.11, T01.G2.14
**Problem**:
- **T01.G2.14**: "Test your algorithm on different examples"
- **T01.G5.11**: "Choose appropriate test cases for an algorithm"
- Both about testing, but what makes G5 more advanced?

**Proposed Solution**:
CLARIFY progression:
- **T01.G2.14**: Testing with GIVEN examples (teacher provides test cases)
- **T01.G5.11**: CHOOSING your own test cases (student identifies edge cases, normal cases, boundary conditions)
- Update descriptions to reflect this difference

**Impact on Dependencies**: None - clarification only

---

### M13: T01.G6.03 and T01.G6.04 - Sequential Not Parallel

**Skills Affected**: T01.G6.03, T01.G6.04
**Problem**:
- **T01.G6.03**: "Spot unnecessary work in an algorithm"
- **T01.G6.04**: "Revise an algorithm to do less work"
- These should be done together (spot THEN revise)
- Why are they separate skills?

**Proposed Solution**:
MERGE into single skill:
- **Keep T01.G6.03**: "Identify and eliminate unnecessary work in algorithms"
  - Description: "Look at an algorithm. Is it doing unnecessary work? Where? Revise it to be more efficient by removing redundant operations."
  - Dependencies: T06.G3.01, T07.G3.01, T08.G3.01, T09.G3.01.04 (EXTERNAL)
- **DELETE T01.G6.04**
- Renumber: G6.05→G6.04, G6.06→G6.05, G6.07→G6.06, G6.08→G6.07

**Impact on Dependencies**:
- External dependencies preserved
- Internal renumbering
- Reduces G6 from 8 to 7 skills

---

### M14: T01.G6.07 and T01.G6.08 - Better as Single Skill

**Skills Affected**: T01.G6.07, T01.G6.08
**Problem**:
- **T01.G6.07**: "Design a flowchart for a multi-step program"
- **T01.G6.08**: "Implement code from a detailed flowchart"
- These are inverse operations - should be learned together

**Proposed Solution**:
Keep as separate BUT make explicit bidirectional dependency:
- **T01.G6.07**: Add note "This is planning (algorithm → flowchart)"
- **T01.G6.08**: Add note "This is implementation (flowchart → algorithm)"
- Make T01.G6.08 depend on T01.G6.07 (currently doesn't)

**Impact on Dependencies**:
- Adds internal dependency (T01.G6.07 → T01.G6.08)

---

### M15: T01.G7.03 - Overly Broad Dependency

**Skills Affected**: T01.G7.03
**Problem**:
- **T01.G7.03**: "Write pseudocode for a search or accumulation algorithm"
- Depends on **T04.G2.01** (patterns) and **T09.G3.01.04** (variables)
- Why patterns (T04)? This is about algorithms not patterns
- Should depend on search/accumulation understanding

**Proposed Solution**:
REPLACE dependencies:
- Remove: T04.G2.01 (patterns - EXTERNAL)
- Add: T01.G5.04 (trace search algorithm - INTERNAL)
- Add: T01.G5.03 (convert program to pseudocode - INTERNAL)
- Keep: T09.G3.01.04 (variables needed for accumulation)

**Impact on Dependencies**:
- Reduces external dependencies
- Better conceptual alignment

---

### M16: T01.G7.08 - Wrong External Dependency

**Skills Affected**: T01.G7.08
**Problem**:
- **T01.G7.08**: "Rewrite a naive algorithm using a better pattern"
- Depends on **T04.G2.01** (identify repeating unit in pattern)
- T04.G2.01 is a G2 skill - way too basic for G7
- Should depend on G7 pattern identification

**Proposed Solution**:
REPLACE dependency:
- Remove: T04.G2.01 (G2 patterns - EXTERNAL)
- Add: T01.G7.01 (identify pattern in program - INTERNAL)
- Keep: T07.G3.01 (loops - EXTERNAL)

**Impact on Dependencies**:
- Removes inappropriate external dependency
- Adds internal dependency

---

### M17: T01.G8.01 and T01.G8.02 - Simulation Skills Need Prerequisites

**Skills Affected**: T01.G8.01, T01.G8.02
**Problem**:
- **T01.G8.01**: "Design one-step update rules for a simple simulation"
- **T01.G8.02**: "Interpret the behavior of a simulation algorithm over time"
- Simulations haven't been introduced before G8
- Abrupt introduction of new concept
- Need scaffolding

**Proposed Solution**:
ADD prerequisite skill in G7:
- **T01.G7.09**: "Identify simulation algorithms vs. calculation algorithms"
  - Description: "Look at two programs. One simulates a bouncing ball (runs continuously, updates each frame). One calculates the ball's position after 5 seconds (runs once, outputs result). What makes them different?"
  - Dependencies: T07.G3.01, T09.G3.01.04 (EXTERNAL)
  - CSTA: 2-AP-11
- Make T01.G8.01 depend on T01.G7.09

**Impact on Dependencies**:
- Adds external dependencies to new skill
- Adds internal dependency to G8.01

---

### M18: T01.G8.04 and T01.G8.05 - Recursion Skills Too Abstract

**Skills Affected**: T01.G8.04, T01.G8.05
**Problem**:
- **T01.G8.04**: "Identify base case and recursive step in an algorithm description"
- **T01.G8.05**: "Trace a conceptual recursive algorithm on small inputs"
- Recursion is very abstract
- Block-based coding (Scratch) doesn't support recursion well
- May be inappropriate for T01 (everyday algorithms)

**Proposed Solution**:
REFRAME as conceptual understanding:
- **T01.G8.04**: Add "conceptual" emphasis - "Identify base case and recursive step in an algorithm DESCRIPTION (reading, not coding)"
- **T01.G8.05**: Add "on paper" - "Trace a recursive algorithm on paper using small inputs (like factorial of 3)"
- Make clear these are about UNDERSTANDING recursion, not implementing it
- Add note: "Implementation of recursive algorithms is in T10 (Functions)"

**Impact on Dependencies**: None - clarification only

---

## LOW PRIORITY ISSUES (Nice to Have)

### L1: Inconsistent Skill Title Formats

**Skills Affected**: All skills
**Problem**:
- Some titles are questions: "What comes next?"
- Some are imperatives: "Put pictures in order"
- Some are descriptive: "Simple pattern game"
- Inconsistent style

**Proposed Solution**:
STANDARDIZE to imperative format:
- "What comes next?" → "Predict the next picture in a sequence"
- "Simple pattern game" → "Predict patterns in movement games"
- "Match X to Y" → keep (already imperative)

**Impact on Dependencies**: None - title formatting only

---

### L2: Missing Examples in K-2 Descriptions

**Skills Affected**: Multiple K-2 skills
**Problem**:
- Some K-2 skills have examples (T01.GK.01: "Put on pajamas, brush teeth, get in bed")
- Others don't (T01.GK.03: "Touch the first picture. Touch the last picture.")
- Examples help teachers implement picture-based activities

**Proposed Solution**:
ADD examples to all K-2 skills:
- T01.GK.03: Add "Example: In a sequence of 'wake up, eat breakfast, brush teeth, go to school,' point to 'wake up' (first) and 'go to school' (last)."
- T01.GK.05: Add "Example: Pictures show 'get dressed, eat breakfast, brush teeth, go to school' but 'brush teeth' is after 'go to school.'"
- Continue for all K-2 skills

**Impact on Dependencies**: None - description enhancements

---

### L3: CSTA Codes - Some Skills Missing 1B-AP-15 (Debugging)

**Skills Affected**: Debugging skills without 1B-AP-15
**Problem**:
- Some debugging skills have CSTA code 1B-AP-15
- Others don't (e.g., T01.G3.13, T01.G3.14, T01.G3.15 have 1B-AP-15)
- But T01.G2.10, T01.G1.05, T01.G1.06 don't

**Proposed Solution**:
ADD 1B-AP-15 to all debugging/fixing skills:
- T01.G1.05: Add 1B-AP-15
- T01.G1.06: Add 1B-AP-15
- T01.G2.10: Add 1B-AP-15
- T01.G2.15: Add 1B-AP-15

**Impact on Dependencies**: None - metadata enhancement

---

### L4: Missing "Explain Your Reasoning" Skills in Early Grades

**Skills Affected**: K-2 skills
**Problem**:
- G3+ have "explain" skills (T01.G3.11, T01.G4.12, T01.G5.09)
- K-2 don't emphasize explaining thinking
- But explaining reasoning is age-appropriate even for young learners

**Proposed Solution**:
CONSIDER adding (optional):
- **T01.G1.11**: "Explain why your picture order makes sense"
  - Description: "You put pictures in order. Tell someone why you put them in that order."
  - Dependencies: T01.G1.01
- **T01.G2.19**: "Explain why an if/then rule works"
  - Description: "Look at an if/then rule. Explain when it would happen and when it wouldn't."
  - Dependencies: T01.G2.07

**Impact on Dependencies**: Internal only - optional additions

---

### L5: Inconsistent Use of "Simple" and "Short" Modifiers

**Skills Affected**: Multiple skills
**Problem**:
- Many skills use "simple" or "short" without defining what that means
- Examples: "simple script," "short program," "simple algorithm"
- What makes something "simple" vs. "complex"?

**Proposed Solution**:
QUANTIFY modifiers:
- "Simple script" → "script with 5-10 blocks"
- "Short program" → "program with 1-2 scripts"
- "Simple algorithm" → "algorithm with 3-5 steps"
- Add measurement criteria

**Impact on Dependencies**: None - description clarification

---

### L6: T01.GK.08 - Physical Activity May Be Implementation Detail

**Skills Affected**: T01.GK.08
**Problem**:
- **T01.GK.08**: "Simple pattern game" - "Play a simple clapping or movement pattern game"
- This is the only skill that specifies a physical activity
- Other skills are activity-agnostic
- May be too prescriptive

**Proposed Solution**:
MAKE more general:
- Change description to: "Participate in a simple pattern activity (like clapping, movements, or sounds). Can you predict what comes next?"
- Allows for multiple implementation methods

**Impact on Dependencies**: None - description refinement

---

### L7: Missing Vocabulary Emphasis

**Skills Affected**: Multiple skills
**Problem**:
- Skills use terms like "algorithm," "sequence," "loop," "conditional" without emphasizing vocabulary
- Students should learn these terms explicitly

**Proposed Solution**:
ADD vocabulary notes:
- Add "Key vocabulary:" section to skill descriptions
- Example for T01.G2.02: "Key vocabulary: repeat, iteration, loop"
- Helps teachers emphasize correct terminology

**Impact on Dependencies**: None - instructional enhancement

---

### L8: G6-G8 Skills Could Reference Real-World Algorithms

**Skills Affected**: G6-G8 skills
**Problem**:
- G6-G8 discuss sorting, searching, efficiency
- Don't reference real-world applications
- Students may not see relevance

**Proposed Solution**:
ADD real-world context:
- T01.G6.01: Add "Used in phone contacts, search engines, databases"
- T01.G7.04: Add "Used for organizing music libraries, student records"
- Makes learning more meaningful

**Impact on Dependencies**: None - description enhancements

---

### L9: Missing Cross-Reference to Other Topics

**Skills Affected**: All skills
**Problem**:
- Skills list dependencies but not "related skills"
- Students might benefit from seeing connections
- Example: T01.G5.02 (flowchart to code) relates to T03 (decomposition)

**Proposed Solution**:
CONSIDER adding "Related skills:" section (optional):
- Lists skills in OTHER topics that connect thematically
- Not dependencies (don't block progress)
- Helps students see bigger picture

**Impact on Dependencies**: None - supplementary information

---

## SUMMARY OF PROPOSED CHANGES

### Skill Count Changes
- **Original**: 97 skills
- **After optimization**: 94 skills
- **Deletions**: 6 skills (T01.G1.07, T01.G3.04, T01.G4.09, T01.G5.08, T01.G6.04, T01.G8.10 split)
- **Additions**: 7 new skills (T01.G2.16, T01.G2.17, T01.G2.18, T01.G4.13, T01.G5.12, T01.G5.13, T01.G7.09)
- **Splits**: 1 skill split into 4 (T01.G8.10 → T01.G8.10.01-.04)
- **Net change**: -3 skills overall (97 → 94), but +1 when counting sub-skills (97 → 98)

### Grade-Level Changes
- **GK**: 8 → 8 skills (no change)
- **G1**: 10 → 9 skills (-1: merged T01.G1.07 into T01.G1.02)
- **G2**: 15 → 18 skills (+3: added T01.G2.16, T01.G2.17, T01.G2.18)
- **G3**: 15 → 14 skills (-1: merged T01.G3.04 into T01.G3.03)
- **G4**: 12 → 12 skills (merged T01.G4.08+G4.09, added T01.G4.13)
- **G5**: 11 → 12 skills (+1: merged T01.G5.07+G5.08, added T01.G5.12, G5.13)
- **G6**: 8 → 7 skills (-1: merged T01.G6.03+G6.04)
- **G7**: 8 → 9 skills (+1: added T01.G7.09)
- **G8**: 10 → 13 skills (+3: split T01.G8.10 into 4 sub-skills)

### Dependency Changes
| Change Type | Count | Impact |
|-------------|-------|---------|
| External dependencies REMOVED | 8 | Reduces coupling |
| External dependencies ADDED | 5 | Necessary for new skills |
| Internal dependencies ADDED | 12 | Better progression |
| Internal dependencies MODIFIED | 6 | Clearer relationships |
| Dependencies PRESERVED | 3,357 | All other external deps intact |

### Priority Breakdown
- **HIGH Priority**: 15 issues → Affects 32 skills
- **MEDIUM Priority**: 18 issues → Affects 45 skills
- **LOW Priority**: 9 issues → Affects 58 skills
- **Total unique skills affected**: 67 of 97 (69%)

---

## IMPLEMENTATION ROADMAP

### Phase 1A: Safe Changes (No External Dependencies)
**Timeline**: Complete first
**Risk**: LOW

1. Fix H4: T01.GK.03, T01.GK.07 dependency updates
2. Fix H5: Merge T01.G1.02 and T01.G1.07
3. Fix H7: Enhance T01.G4.01, T01.G4.02 descriptions
4. Fix H10: Add T01.G2.18 debugging skill
5. Fix H12: Consolidate T01.G4.08 + T01.G4.09
6. Fix H13: Clarify T01.G5.10 description
7. Implement M1: Standardize terminology
8. Implement M2: Clarify T01.G1.09, T01.G1.10
9. Implement M4: Merge T01.G3.03 + T01.G3.04
10. Implement M5: Swap T01.G3.08 ↔ T01.G3.09
11. Implement M7: Clarify T01.G4.03, T01.G4.04
12. Implement M11: Merge T01.G5.07 + T01.G5.08
13. Implement M13: Merge T01.G6.03 + T01.G6.04
14. All LOW priority issues (L1-L9)

### Phase 1B: External Dependency Changes (Coordination Required)
**Timeline**: After Phase 1A
**Risk**: MEDIUM

1. Fix H2: Add G2 bridging skills (T01.G2.16, T01.G2.17)
2. Fix H8: Renumber T01.G5.02.01/.02 → T01.G5.02/.03
3. Fix H9: Replace T01.G3.12 dependency
4. Fix H11: Replace T01.G6.01 dependency
5. Fix H15: Replace T01.G7.01 dependencies
6. Implement M6: Add T01.G3.16 (forever loops)
7. Implement M15: Replace T01.G7.03 dependencies
8. Implement M16: Replace T01.G7.08 dependencies
9. Implement M17: Add T01.G7.09 (simulation prerequisite)

### Phase 1C: Complex Changes (Requires Testing)
**Timeline**: After Phase 1B
**Risk**: MEDIUM-HIGH

1. Fix H1: Split T01.G8.10 into 4 sub-skills
2. Fix H6: Add T01.G4.13 (conditional loops)
3. Fix H14: Add T01.G5.12 (correctness vs. efficiency)
4. Implement M9: Add T01.G5.13 (create flowchart)
5. Implement M14: Add dependency T01.G6.07 → T01.G6.08

### Phase 2: Content Quality (Description Updates)
**Timeline**: Ongoing
**Risk**: LOW

1. Fix H3: Clarify all "trace" skill descriptions
2. Implement M3: Differentiate T01.G2.04
3. Implement M8: Clarify T01.G4.05 objective
4. Implement M10: Reframe T01.G5.05
5. Implement M12: Clarify T01.G2.14 vs T01.G5.11
6. Implement M18: Add notes to recursion skills

---

## VALIDATION CHECKLIST

After implementing changes, verify:

- [ ] Total skill count is 98 (including sub-skills)
- [ ] All external dependencies to T06, T07, T08, T09 are preserved
- [ ] No circular dependencies within T01
- [ ] All dependencies follow X-2 rule (grade X can depend on X, X-1, or X-2)
- [ ] K-2 skills remain picture-based (no coding)
- [ ] G3+ skills properly reference block-based coding
- [ ] All skill IDs are unique
- [ ] All skills have titles, descriptions, CSTA codes
- [ ] Progression flows logically from concrete to abstract
- [ ] No orphaned skills (all part of dependency chain)

---

## RISK ASSESSMENT

### Low Risk Changes (42 issues)
- Description clarifications
- Terminology standardization
- Adding examples
- Internal dependency updates
- Merging redundant skills within same grade

### Medium Risk Changes (8 issues)
- Adding new skills with external dependencies
- Changing external dependencies
- Renumbering skills (affects other topics)
- Splitting complex skills

### High Risk Changes (1 issue)
- T01.G8.10 split (288 dependencies to redistribute)

**Recommendation**: Complete Low Risk changes first, then Medium Risk, then High Risk after thorough review.

---

## NEXT STEPS

1. **Review this plan** with stakeholders
2. **Prioritize** which issues to address in Phase 1
3. **Coordinate** with owners of T06, T07, T08, T09 for external dependency changes
4. **Implement** Phase 1A changes (safe, no coordination needed)
5. **Test** updated skill progression
6. **Document** all changes in changelog
7. **Update** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` with optimized skills

---

**Generated**: 2025-11-22
**Analyst**: Claude (Sonnet 4.5)
**Total Issues Identified**: 42
**Total Skills Affected**: 67 of 97 (69%)
**Estimated Impact**: Moderate (improves clarity and progression without major restructuring)
