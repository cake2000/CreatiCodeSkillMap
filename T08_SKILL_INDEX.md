# T08 (Conditions & Logic) - Complete Skill Index

## Overview
- **Topic:** T08 – Conditions & Logic
- **Total Skills:** 36 (after Phase 1 optimization)
- **Grade Range:** K through G8
- **Phase 1 Status:** Complete - Ready for Implementation

---

## Quick Navigation

- [Kindergarten (K)](#kindergarten-skills-2-skills)
- [Grade 1](#grade-1-skills-3-skills)
- [Grade 2](#grade-2-skills-3-skills)
- [Grade 3](#grade-3-skills-6-skills-1-new)
- [Grade 4](#grade-4-skills-9-skills)
- [Grade 5](#grade-5-skills-6-skills)
- [Grade 6](#grade-6-skills-3-skills)
- [Grade 7](#grade-7-skills-2-skills)
- [Grade 8](#grade-8-skills-2-skills)

---

## Kindergarten Skills (2 skills)

### T08.GK.01 - Match pictures to "if it rains" rules
**Type:** Picture-based matching
**Format:** Drag-and-drop activity
**Status:** ✓ Unchanged

### T08.GK.02 - Choose what happens next based on yes/no
**Type:** Picture-based decision
**Format:** Multiple-choice with 2 picture choices
**Dependencies:** T08.GK.01
**Status:** ✓ Unchanged

---

## Grade 1 Skills (3 skills)

### T08.G1.01 - Sort cards by if-then rules
**Type:** Picture-based sorting
**Format:** Drag-and-drop to 2 labeled bins
**Dependencies:** T08.GK.02
**Status:** ✓ Unchanged

### T08.G1.02 - Predict the outcome of an if-then rule
**Type:** Picture-based prediction
**Format:** Multiple-choice prediction activity
**Dependencies:** T08.G1.01
**Status:** ✓ Unchanged

### T08.G1.03 - Choose between two actions based on a condition
**Type:** Picture-based decision
**Format:** Multiple-choice with picture choices
**Dependencies:** T08.G1.02
**Status:** ✓ Unchanged

---

## Grade 2 Skills (3 skills)

### T08.G2.01 - Follow branching paths based on yes/no questions
**Type:** Picture-based flowchart
**Format:** Interactive flowchart with 2-3 decision points
**Dependencies:** T08.G1.03
**Status:** ✓ Unchanged

### T08.G2.02 - Create a simple if-then-else rule for a scenario
**Type:** Picture-based construction
**Format:** Fill-in-the-blank with word/picture bank
**Dependencies:** T08.G2.01
**Status:** ✓ Unchanged

### T08.G2.03 - Identify which rule applies in a situation
**Type:** Picture-based rule selection
**Format:** Multiple-choice rule matching
**Dependencies:** T08.G2.02
**Status:** ✓ Unchanged

---

## Grade 3 Skills (6 skills, 1 NEW)

### T08.G3.01 - Use a simple if in a script
**Type:** Code - Basic conditional
**Concept:** First `if <condition> then ...` block
**Dependencies:** T07.G3.01, T08.G2.03
**Status:** ✓ Unchanged

### T08.G3.02 - Decide when a single if is enough
**Type:** Code - Conceptual understanding
**Concept:** Recognizing single-condition scenarios
**Dependencies:** T08.G3.01
**Status:** ⚠️ UPDATED (description rewritten - removed compound condition references)

### T08.G3.03 - Pick the right conditional block for a scenario
**Type:** Code - Block selection
**Concept:** Choose between `if` and `if/else`
**Dependencies:** T08.G3.02, T07.G3.02
**Status:** ✓ Unchanged

### T08.G3.03b - Build a simple if/else block
**Type:** Code - Implementation
**Concept:** First two-branch conditional
**Dependencies:** T08.G3.03, T07.G3.02
**Status:** ✨ NEW SKILL (fills scaffolding gap)

### T08.G3.04 - Trace code with a single if/else
**Type:** Code - Tracing/Reading
**Concept:** Predict execution path
**Dependencies:** T08.G3.03b, T07.G3.03
**Status:** ⚠️ UPDATED (dependencies changed - now depends on G3.03b)

### T08.G3.05 - Fix a condition that uses the wrong comparison operator
**Type:** Code - Debugging
**Concept:** Comparison operators (<, >, =, ≤, ≥, ≠)
**Dependencies:** T08.G3.04
**Status:** ✓ Unchanged

---

## Grade 4 Skills (9 skills)

### T08.G4.01 - Combine two conditions with AND
**Type:** Code - Boolean logic
**Concept:** Logical conjunction
**Dependencies:** T06.G3.01, T08.G3.05
**Status:** ⚠️ UPDATED (removed redundant T08.G3.01 dependency)

### T08.G4.02 - Combine two conditions with OR
**Type:** Code - Boolean logic
**Concept:** Logical disjunction
**Dependencies:** T06.G3.01, T08.G4.01, T09.G3.01.04
**Status:** ⚠️ UPDATED (now depends on G4.01 to ensure AND before OR)

### T08.G4.03 - Trace code with compound conditionals
**Type:** Code - Tracing/Reading
**Concept:** Evaluate complex boolean expressions
**Dependencies:** T06.G3.01, T08.G4.01
**Status:** ⚠️ UPDATED (description clarified - "AND and/or OR")

### T08.G4.04 - Nest if/else statements
**Type:** Code - Hierarchical structure
**Concept:** Multi-level decision-making
**Dependencies:** T06.G3.01, T08.G4.01
**Status:** ⚠️ UPDATED (now depends on G4.01 to learn compound before nesting)

### T08.G4.05 - Use else-if for multiple exclusive conditions
**Type:** Code - Chained conditionals
**Concept:** Multi-way selection
**Dependencies:** T08.G4.03, T08.G4.04
**Status:** ✓ Unchanged

### T08.G4.06 - Convert nested if to cleaner logic
**Type:** Code - Refactoring
**Concept:** Code quality and maintainability
**Dependencies:** T08.G4.01, T08.G4.02, T08.G4.05
**Status:** ✓ Unchanged

### T08.G4.07 - Use if to control state changes
**Type:** Code - Application
**Concept:** Game/animation state management
**Dependencies:** T06.G3.02, T08.G3.05, T09.G3.01.04
**Status:** ✓ Unchanged

### T08.G4.08 - Analyze and fix a compound logic bug
**Type:** Code - Debugging
**Concept:** Debug AND/OR/NOT errors
**Dependencies:** T08.G4.01, T08.G4.02, T08.G4.03
**Status:** ✓ Unchanged

### T08.G4.09 - Trace code with a sequence of if/else blocks
**Type:** Code - Tracing/Reading
**Concept:** Track state through multiple decision points
**Dependencies:** T08.G3.04
**Status:** ⚠️ UPDATED (removed G4.05 dependency - sequential ≠ exclusive)

---

## Grade 5 Skills (6 skills)

### T08.G5.01 - Design multi-branch decision logic
**Type:** Code - Design/Planning
**Concept:** Algorithmic thinking
**Dependencies:** T08.G4.05, T08.G4.06, T08.G4.09
**Status:** ✓ Unchanged

### T08.G5.02 - Use NOT to invert conditions
**Type:** Code - Boolean logic
**Concept:** Logical negation
**Dependencies:** T08.G4.01, T08.G4.02, T08.G4.03
**Status:** ✓ Unchanged

### T08.G5.03 - Combine three or more conditions
**Type:** Code - Complex logic
**Concept:** Multi-condition expressions
**Dependencies:** T08.G5.02, T08.G4.08
**Status:** ✓ Unchanged

### T08.G5.04 - Trace complex decision logic
**Type:** Code - Tracing/Reading
**Concept:** Analyze decision trees
**Dependencies:** T08.G5.01, T08.G5.03
**Status:** ✓ Unchanged

### T08.G5.05 - Use inline if-then-else expressions to compute conditional values
**Type:** Code - Advanced feature (CreatiCode)
**Concept:** Ternary operator / inline conditionals
**Dependencies:** T08.G5.01
**Status:** ⚠️ UPDATED (removed redundant G4.06 dependency)

### T08.G5.06 - Use condition-triggered events to respond to state changes
**Type:** Code - Advanced feature (CreatiCode)
**Concept:** `when <condition>` hat block / event-driven patterns
**Dependencies:** T08.G5.01, T08.G4.07, T06.G4.01
**Status:** ✓ Unchanged

---

## Grade 6 Skills (3 skills)

### T08.G6.01 - Use conditionals to control simulation steps
**Type:** Code - Application (Science/Math)
**Concept:** Simulation control logic
**Dependencies:** T08.G5.03, T08.G5.04
**Status:** ✓ Unchanged

### T08.G6.02 - Implement simple state machines using conditionals
**Type:** Code - Design pattern
**Concept:** Formal state machine concepts
**Dependencies:** T08.G5.03, T08.G5.04, T08.G4.07
**Status:** ✓ Unchanged

### T08.G6.03 - Debug multi-condition logic
**Type:** Code - Debugging
**Concept:** Complex boolean debugging, operator precedence
**Dependencies:** T08.G5.03, T08.G5.04, T08.G4.08
**Status:** ✓ Unchanged

---

## Grade 7 Skills (2 skills)

### T08.G7.01 - Reason about fairness using conditions
**Type:** Code - Critical thinking / Ethics
**Concept:** Algorithmic bias and fairness
**Dependencies:** T08.G5.01, T08.G5.02, T08.G6.02, T08.G6.03
**Status:** ✓ Unchanged

### T08.G7.02 - Design tests for condition-heavy code
**Type:** Code - Testing methodology
**Concept:** Branch coverage, systematic testing
**Dependencies:** T08.G5.01, T08.G6.02, T08.G6.03
**Status:** ✓ Unchanged

---

## Grade 8 Skills (2 skills)

### T08.G8.01 - Analyze logical equivalence of conditionals
**Type:** Code - Formal logic
**Concept:** De Morgan's law, logical transformations
**Dependencies:** T04.G6.01, T08.G6.01, T08.G7.01, T08.G7.02
**Status:** ✓ Unchanged (T04 dependency flagged for review)

### T08.G8.02 - Use logic to design robust input validation
**Type:** Code - Security/Data validation
**Concept:** Defensive programming
**Dependencies:** T06.G6.01, T08.G6.01, T08.G7.01, T08.G7.02
**Status:** ✓ Unchanged

---

## Skill Type Distribution

### By Activity Type:
- **Picture-based (K-2):** 8 skills
- **Code - Basic conditionals (G3):** 6 skills
- **Code - Compound logic (G4):** 9 skills
- **Code - Complex logic (G5):** 6 skills
- **Code - Applications (G6-G8):** 7 skills

### By Learning Mode:
- **Conceptual understanding:** 6 skills (K-2 picture-based + G3.02)
- **Implementation/Building:** 15 skills
- **Tracing/Reading:** 5 skills
- **Debugging:** 4 skills
- **Design/Planning:** 3 skills
- **Testing/Ethics:** 3 skills

### By Skill Complexity:
- **Foundational (K-2):** 8 skills
- **Basic (G3):** 6 skills
- **Intermediate (G4):** 9 skills
- **Advanced (G5-G6):** 9 skills
- **Expert (G7-G8):** 4 skills

---

## Key Concepts Coverage

### Core Conditional Structures:
- ✓ Simple `if` (G3.01)
- ✓ `if/else` (G3.03b, G3.04)
- ✓ `else-if` chains (G4.05)
- ✓ Nested conditionals (G4.04)

### Boolean Operators:
- ✓ AND (G4.01)
- ✓ OR (G4.02)
- ✓ NOT (G5.02)
- ✓ Compound expressions (G4.03, G5.03)

### Comparison Operators:
- ✓ =, <, >, ≤, ≥, ≠ (G3.05)

### Advanced Features (CreatiCode-specific):
- ✓ Inline `if-then-else` reporter (G5.05)
- ✓ `when <condition>` hat block (G5.06)

### Cross-Cutting Skills:
- ✓ Tracing/prediction (G3.04, G4.03, G4.09, G5.04)
- ✓ Debugging (G3.05, G4.08, G6.03)
- ✓ Refactoring (G4.06)
- ✓ Design (G5.01)
- ✓ Testing (G7.02)
- ✓ Ethics (G7.01)
- ✓ Formal logic (G8.01)

---

## Dependency Patterns

### Intra-Topic (T08 → T08):
- Clean linear progression K → G1 → G2 → G3
- Branching in G4 (AND/OR, nesting, else-if as parallel tracks)
- Convergence in G5 (synthesis of G4 concepts)
- Application in G6-G8

### Cross-Topic Dependencies:
- **T06 (Events & Scripts):** 5 dependencies
  - T06.G3.01 (green-flag scripts) → used in G4 compound logic
  - T06.G3.02 (key-press scripts) → used in G4.07 state management
  - T06.G4.01 (event types) → used in G5.06 conditional events
  - T06.G6.01 (event execution) → used in G8.02 input validation

- **T07 (Loops):** 3 dependencies
  - T07.G3.01 (counted repeat) → prerequisite for G3.01 basic if
  - T07.G3.02 (trace loop) → prerequisite for G3.03/G3.03b
  - T07.G3.03 (forever loop) → prerequisite for G3.04

- **T09 (Variables):** 2 dependencies
  - T09.G3.01.04 (variable monitor) → used in G4.02 OR, G4.07 state

- **T04 (Pattern Recognition):** 1 dependency
  - T04.G6.01 (algorithm patterns) → used in G8.01 logical equivalence

- **T03 (Problem Decomposition):** 0 direct dependencies
  - (May have indirect through other topics)

---

## Phase 1 Optimization Summary

### Changes Made:
- **Added:** 1 new skill (T08.G3.03b)
- **Updated descriptions:** 2 skills (G3.02, G4.03)
- **Updated dependencies:** 6 skills (G3.04, G4.01, G4.02, G4.04, G4.09, G5.05)
- **Total affected:** 10 skills out of 36

### Issues Resolved:
- ✓ Scaffolding gap filled (build if/else before tracing)
- ✓ Forward reference eliminated (G4.09 → G4.05)
- ✓ Concept clarity improved (G3.02 no longer references future concepts)
- ✓ Dependency optimization (removed redundancies)
- ✓ Pedagogical sequencing (AND before OR, compound before nesting)

### Quality Metrics:
- **K-2 Format Compliance:** 100% (8/8 picture-based)
- **No Duplicates:** Confirmed
- **X-2 Rule Compliance:** 100%
- **Forward References:** 0 (all eliminated)
- **Pedagogical Flow:** Excellent (smooth progression K-G8)

---

## Related Documentation

1. **T08_PHASE1_OPTIMIZATION_ANALYSIS.md** - Comprehensive issue analysis
2. **T08_EXACT_CHANGES.md** - Exact text for all changes
3. **T08_READY_TO_PASTE.md** - Ready-to-implement skill blocks
4. **T08_VERIFICATION_CHECKLIST.md** - Implementation validation checklist
5. **T08_PHASE1_COMPLETE.md** - Executive summary
6. **T08_SKILL_INDEX.md** - This document

---

## Next Steps

### Immediate:
1. Review all documentation
2. Implement changes using T08_READY_TO_PASTE.md
3. Validate using T08_VERIFICATION_CHECKLIST.md

### Phase 2 (Future):
1. Cross-topic dependency analysis
2. Integration with T06, T07, T09
3. Assessment alignment
4. Platform capability verification

---

**Document Created:** 2025-11-22
**Last Updated:** 2025-11-22
**Status:** Complete and Ready for Implementation
**Total T08 Skills:** 36 (35 original + 1 new)
