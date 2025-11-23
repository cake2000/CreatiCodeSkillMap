# T28 Quick Fix Reference

## Critical Fixes Required

### 1. Forward Reference (H1)
**T28.G3.05** currently depends on **T28.G3.06** (comes after it)
```
REMOVE: T28.G3.06 from G3.05 dependencies
KEEP: T28.G3.01
```

### 2. Duplicate Skills (H2)
**T28.G3.07** and **T28.G4.01** are very similar
```
SOLUTION: Modify G4.01 description to emphasize if-statements:
"Build a random generator that uses if-statements to interpret random numbers
(e.g., pick random 1-4, then use if-statements to convert to color names)"
```

### 3. Misplaced Skill (H3)
**T28.G5.08** "Track position and state for a single sprite"
```
RECOMMENDATION: Move to T05 (Modeling) or T09 (Variables)
ALTERNATIVE: Reframe as "Track agent state for probabilistic simulation"
```

### 4. Fix Incorrect Dependency (H5)
**T08.G5.01** is referenced but likely doesn't exist (duplicate of T08.G3.01)
```
AFFECTED: T28.G6.05, T28.G6.07
FIX: Change T08.G5.01 → T08.G3.01
```

### 5. X-2 Rule Violations (H4)
Multiple violations - recommend accepting X-1 for foundational skills:
- T28.G3.01 depends on T07.G3.01 (same grade) - ACCEPT for loops
- T28.G4.01 depends on T08.G3.01 (X-1) - ACCEPT for conditionals
- T28.G4.02.01 depends on T07.G3.01 (X-1) - ACCEPT for loops
- T28.G5.03 depends on T08.G4.01 (X-1) - ACCEPT for conditionals
- T28.G6.05, G6.07 depend on T08.G5.01 (X-1) - FIX with #4 above
- T28.G7.01 depends on G6.08, G6.09 (X-1) - ACCEPT for scaffolding

---

## Medium Priority Fixes

### 6. Seeded Random Limitation (M2b)
**T28.G6.02** "Use random seeds for reproducibility"
```
UPDATE DESCRIPTION:
"Students populate a list with seeded random numbers using
'set [list] to (N) random numbers with seed (SEED)',
then draw values from this list sequentially to create
reproducible random sequences."
```

### 7. Unnecessary Dependency (M5a)
**T28.G5.07** doesn't need median/mode for frequency distributions
```
REMOVE: T27.G4.02c from dependencies
KEEP: T28.G5.01.02
```

### 8. Redundant Dependencies (M5b, M5c)
**T28.G6.01.01** and **T28.G6.02** have redundant dependencies
```
G6.01.01 - REMOVE: T09.G4.04 (redundant with T09.G5.01)
G6.02 - SIMPLIFY TO: T28.G5.04, T09.G5.01, T07.G5.01
```

### 9. Add List Iteration Dependency (M3c)
**T28.G4.02.02** "Count frequencies" needs list iteration
```
ADD: Dependency on T10 skill for list iteration
OR: Add dependency on T07 skill for "repeat with item in list"
```

---

## Low Priority Improvements

### 10. Make Non-Coding Skill More Specific (L1d)
**T28.G4.06** "Interpret probabilities as fractions and percentages"
```
ADD TO DESCRIPTION:
"Students create variables to convert between representations
(e.g., variable 'fraction' = 1/4, variable 'percent' = fraction * 100)"
```

### 11. CreatiCode Terminology (L1e)
**T28.G5.02** mentions "function" but CreatiCode uses "scripts"
```
CHANGE: "write a function" → "write a script"
```

### 12. Clarify Recording Method (L1b)
**T28.G3.03** "copy the generated table into their notebook"
```
ADD: "by taking a screenshot, transcribing by hand,
or copying to a document"
```

### 13. Add Success Criteria (L2a)
**T28.G3.02** "explain what 'pick random' does"
```
ADD: "Explanation must include: (1) the range of possible values
and (2) that each value has equal likelihood"
```

---

## Terminology Standardization (L3)

### Use Consistent Terms:
- **G2-G4**: "experiment" (simpler)
- **G5-G8**: "simulation" (more technical)
- **Always**: "script" (not "code" or "function")
- **Physical activities**: "picture-based" or "hands-on"

---

## Skills to Verify Dependencies Exist

Check these dependencies exist in other topics:
- T07.G3.01 (counted repeat loop) ✓ assumed to exist
- T08.G3.01 (simple if statement) ✓ assumed to exist
- T08.G4.01 (conditionals with input) ✓ assumed to exist
- T08.G5.01 (likely error - should be G3.01) ✗ NEEDS FIX
- T09.G4.04 (use variables for state) ✓ assumed to exist
- T09.G5.01 (modify variables) ✓ assumed to exist
- T10.G3.03 (add/remove list items) ✓ assumed to exist
- T27.G3.04 (side-by-side bar charts) ✓ assumed to exist
- T27.G4.02c (median/mode in code) ✓ assumed to exist

---

## Change Order

1. Fix H5 (T08.G5.01 → T08.G3.01) in affected skills
2. Fix H1 (remove forward reference)
3. Fix H2 (update G4.01 description)
4. Fix M2b (update G6.02 description)
5. Fix M5a, M5b, M5c (remove redundant dependencies)
6. Fix L1e (function → script)
7. Add L2a success criteria
8. Decide on H3 (move G5.08 or reframe)
9. Decide on H4 (accept X-1 violations or adjust grades)
10. Add L3 terminology updates

---

## Quick Stats

- Total T28 skills: 56 (across G2-G8)
- Skills with issues: 29
- Skills correct as-is: 27
- Critical fixes needed: 5
- X-2 violations: 7 (recommend accept 6, fix 1)
- Forward references: 1
- Duplicate/overlapping: 2
- Misplaced skills: 1
