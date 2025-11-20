# G7 Skills - Sample Fixes

This document shows specific examples of how to fix the most common issues found in G7 skills.

---

## Example 1: Removing Transitive Dependencies

### BEFORE: T01.G7.01
```
ID: T01.G7.01
Topic: T01 – Everyday Algorithms
Skill: Identify the pattern in a given program
Description: Students categorize code as search, sort, accumulation, or simulation.

Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed
* T01.GK.07: Find the pattern that repeats
* T01.GK.08: Count how many times
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.01: Create and use a numeric variable for score or count
```

**Issue:** T01.GK.08 already depends on T01.GK.07, so the dependency on T01.GK.07 is redundant.

### AFTER: T01.G7.01
```
ID: T01.G7.01
Topic: T01 – Everyday Algorithms
Skill: Identify the pattern in a given program
Description: Students categorize code as search, sort, accumulation, or simulation.

Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed
* T01.GK.08: Count how many times
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.01: Create and use a numeric variable for score or count
```

**Change:** Removed `T01.GK.07` (still accessible through T01.GK.08)

---

## Example 2: Adding Missing Dependencies

### BEFORE: T02.G7.03
```
ID: T02.G7.03
Topic: T02 – Algorithm Diagrams
Skill: Create a flowchart for linear search or "find max"
Description: Students design a flowchart in the Diagrams tab for a simple search algorithm (e.g., scan a list to find the largest value).

Dependencies:
* T01.G3.01: Complete a simple script with missing blocks
* T01.G3.02: Match a story description to a code sequence
* T02.GK.01: Recognize picture steps for a task
* T02.GK.03: Use first/next/last to describe a sequence
* T02.GK.04: Fix one picture that is out of order
```

**Issue:** Description mentions "scan a list" but no T10 (Lists & Tables) dependency.

### AFTER: T02.G7.03
```
ID: T02.G7.03
Topic: T02 – Algorithm Diagrams
Skill: Create a flowchart for linear search or "find max"
Description: Students design a flowchart in the Diagrams tab for a simple search algorithm (e.g., scan a list to find the largest value).

Dependencies:
* T01.G3.01: Complete a simple script with missing blocks
* T01.G3.02: Match a story description to a code sequence
* T02.GK.01: Recognize picture steps for a task
* T02.GK.04: Fix one picture that is out of order
* T10.G3.01: Loop through and process each item in a list
```

**Changes:**
1. Removed `T02.GK.03` (implied by T02.GK.04)
2. Added `T10.G3.01` (needed for list operations)

---

## Example 3: Fixing Multiple Issues in One Skill

### BEFORE: T01.G7.08
```
ID: T01.G7.08
Topic: T01 – Everyday Algorithms
Skill: Rewrite a naive algorithm using a better pattern
Description: Students replace repeated naive logic with a cleaner pattern (single loop, flag, etc.).

Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed
* T01.GK.07: Find the pattern that repeats
* T01.GK.08: Count how many times
* T04.G2.01: Identify the repeating unit in a longer pattern
* T07.G3.01: Use a counted repeat loop
```

**Issues:**
1. T01.GK.08 implies T01.GK.07 (transitive)
2. T07.G3.01 implies T04.G2.01 (transitive)

### AFTER: T01.G7.08
```
ID: T01.G7.08
Topic: T01 – Everyday Algorithms
Skill: Rewrite a naive algorithm using a better pattern
Description: Students replace repeated naive logic with a cleaner pattern (single loop, flag, etc.).

Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed
* T01.GK.08: Count how many times
* T07.G3.01: Use a counted repeat loop
```

**Changes:**
1. Removed `T01.GK.07` (implied by T01.GK.08)
2. Removed `T04.G2.01` (implied by T07.G3.01)

---

## Example 4: Complex Transitive Dependency Chain

### BEFORE: T19.G7.01
```
ID: T19.G7.01
Topic: T19 – Multiplayer Games
Skill: Balance starting conditions and scoring
Description: Students design and test balanced rules for multiplayer gameplay.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.01: Use a simple if in a script
* T09.G3.01: Create and use a numeric variable for score or count
* T19.G6.05: Use server lists to track game state
* T31.G5.01: Understand data flow: send → server → broadcast
```

**Issue:** T19.G6.05 already depends on T31.G5.01

### AFTER: T19.G7.01
```
ID: T19.G7.01
Topic: T19 – Multiplayer Games
Skill: Balance starting conditions and scoring
Description: Students design and test balanced rules for multiplayer gameplay.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.01: Use a simple if in a script
* T09.G3.01: Create and use a numeric variable for score or count
* T19.G6.05: Use server lists to track game state
```

**Change:** Removed `T31.G5.01` (implied by T19.G6.05)

---

## Example 5: Clarifying Overly Broad Skill

### BEFORE: T02.G7.01
```
ID: T02.G7.01
Topic: T02 – Algorithm Diagrams
Skill: Trace a step‑by‑step simulation algorithm
Description: Students trace code that simulates a process over several timesteps (e.g., a counter stepping up, an object moving with friction) and predict state after N steps.
```

**Issue:** "several timesteps" is vague

### AFTER: T02.G7.01
```
ID: T02.G7.01
Topic: T02 – Algorithm Diagrams
Skill: Trace a step‑by‑step simulation algorithm
Description: Students trace code that simulates a process over 3-5 timesteps (e.g., a counter stepping up, an object moving with friction) and predict state after N steps.
```

**Change:** Changed "several" to "3-5" for specificity

---

## Example 6: Fixing Pattern Across Multiple Skills

Many T02.G7.* skills share the same transitive dependency pattern:

### Pattern to Apply:
For skills T02.G7.01 through T02.G7.06:

**Remove:** `T02.GK.03` (always implied by `T02.GK.04`)

This is a consistent pattern that can be applied mechanically across 6 skills.

---

## Example 7: Multiple Changes + Missing Dependency

### BEFORE: T02.G7.02
```
ID: T02.G7.02
Topic: T02 – Algorithm Diagrams
Skill: Extend a simulation trace and predict future behavior
Description: Students are shown a partially filled trace table for a simulation algorithm and must extend it a few rows to predict future behavior.

Dependencies:
* T01.G3.01: Complete a simple script with missing blocks
* T01.G3.02: Match a story description to a code sequence
* T02.GK.01: Recognize picture steps for a task
* T02.GK.03: Use first/next/last to describe a sequence
* T02.GK.04: Fix one picture that is out of order
```

**Issues:**
1. T02.GK.04 implies T02.GK.03 (transitive)
2. Description mentions "trace table" but no T10 dependency

### AFTER: T02.G7.02
```
ID: T02.G7.02
Topic: T02 – Algorithm Diagrams
Skill: Extend a simulation trace and predict future behavior
Description: Students are shown a partially filled trace table for a simulation algorithm and must extend it a few rows to predict future behavior.

Dependencies:
* T01.G3.01: Complete a simple script with missing blocks
* T01.G3.02: Match a story description to a code sequence
* T02.GK.01: Recognize picture steps for a task
* T02.GK.04: Fix one picture that is out of order
* T10.G3.01: Loop through and process each item in a list
```

**Changes:**
1. Removed `T02.GK.03` (transitive)
2. Added `T10.G3.01` (for table operations)

---

## Summary of Fix Patterns

### Pattern 1: GK Transitive Dependencies
- If skill has both `T0X.GK.0Y` and `T0X.GK.0Z` where Y < Z
- Check if `.0Z` depends on `.0Y`
- If yes, remove `.0Y`

### Pattern 2: G6→G5 Transitive Dependencies
- If skill has both `T0X.G6.0Y` and `T0X.G5.0Z`
- Check if the G6 skill depends on the G5 skill
- If yes, remove the G5 dependency

### Pattern 3: Loop→Pattern Transitive Dependencies
- If skill has both `T07.G3.01` (loops) and `T04.G2.01` (patterns)
- Loop skill already requires pattern skill
- Remove `T04.G2.01`

### Pattern 4: Missing List Dependencies
- If description mentions: "list", "table", "data", "scan", "search", "find max"
- Add: `T10.G3.01` or higher T10 skill as appropriate

### Pattern 5: Missing Loop Dependencies
- If description mentions: "loop", "repeat", "iterate", "each"
- Add: `T07.G3.01` or higher T07 skill as appropriate

---

## Validation After Fixes

After applying fixes, verify:

1. **Skill still makes sense:** Dependencies support the skill description
2. **No missing prerequisites:** All concepts mentioned are covered by dependencies
3. **No over-specification:** Not listing every possible transitive dependency
4. **Consistent with peers:** Similar skills in same topic have similar dependency patterns

---

## Tools for Verification

Re-run the analysis script after fixes:
```bash
python3 analyze_g7_comprehensive.py
```

Expected results after fixes:
- Transitive dependency issues: 0 (down from 116)
- Missing dependency issues: ~5-10 (down from 31, after validating which are real)
- Total issues: <20 (down from 150)

