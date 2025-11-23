# T08 - READY TO PASTE (Updated Skills Only)

## Instructions:
Replace the corresponding skills in allskills.md with these updated versions.
Insert the NEW skill (T08.G3.03b) between T08.G3.03 and T08.G3.04.

---

## T08.G3.02 (UPDATED - Description Change)

```markdown
ID: T08.G3.02
Topic: T08 – Conditions & Logic
Skill: Decide when a single if is enough
Description: Students identify simple scenarios where an action should happen only when one condition is true (e.g., "move when space key is pressed" or "say 'Good!' when touching star"). This builds conceptual understanding of when to use a simple if block through concrete, visual examples. Students practice recognizing single-condition situations in game and animation contexts.

Dependencies:
* T08.G3.01: Use a simple if in a script

CSTA: E3-ALG-AF-01
```

---

## T08.G3.03b (NEW SKILL - Insert after T08.G3.03)

```markdown
ID: T08.G3.03b
Topic: T08 – Conditions & Logic
Skill: Build a simple if/else block
Description: Students add their first `if/else` block to handle two distinct outcomes (e.g., "if touching goal, say 'You win!', else say 'Keep going!'"). This introduces the two-branch conditional structure where both paths execute different actions. Use scenarios with clear either/or outcomes that require different responses for each branch.

Dependencies:
* T08.G3.03: Pick the right conditional block for a scenario
* T07.G3.02: Trace a script with a simple loop

CSTA: E3-ALG-AF-01, E3-PRO-PF-01
```

---

## T08.G3.04 (UPDATED - Dependencies Change)

```markdown
ID: T08.G3.04
Topic: T08 – Conditions & Logic
Skill: Trace code with a single if/else
Description: Students trace a short script with one simple `if/else` block and a given condition to predict which branch runs and what happens. This develops code reading and prediction skills by following the execution path through a two-branch conditional structure.

Dependencies:
* T08.G3.03b: Build a simple if/else block
* T07.G3.03: Build a forever loop for simple animation

CSTA: E3-ALG-AF-01, E3-PRO-PF-01
```

---

## T08.G4.01 (UPDATED - Dependencies Change)

```markdown
ID: T08.G4.01
Topic: T08 – Conditions & Logic
Skill: Combine two conditions with AND
Description: Students use a compound condition (AND) to check if two things are true at the same time before acting (e.g., "if key pressed AND touching goal, then complete level"). This is their first time writing boolean logic operators in code, introducing logical conjunction.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.05: Fix a condition that uses the wrong comparison operator

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

---

## T08.G4.02 (UPDATED - Dependencies Change)

```markdown
ID: T08.G4.02
Topic: T08 – Conditions & Logic
Skill: Combine two conditions with OR
Description: Students use OR to check if at least one of two conditions is true (e.g., "if score > 100 OR lives == 0, then end game"). This introduces logical disjunction and helps students understand when to use OR vs AND in compound conditions.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G4.01: Combine two conditions with AND
* T09.G3.01.04: Display variable value on stage using the variable monitor

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

---

## T08.G4.03 (UPDATED - Description Change)

```markdown
ID: T08.G4.03
Topic: T08 – Conditions & Logic
Skill: Trace code with compound conditionals
Description: Students read code with compound expressions (AND and/or OR) and predict which branch runs for given inputs, building comfort with compound logic before debugging or refactoring. This skill develops the ability to mentally evaluate complex boolean expressions combining multiple conditions.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G4.01: Combine two conditions with AND

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

---

## T08.G4.04 (UPDATED - Dependencies Change)

```markdown
ID: T08.G4.04
Topic: T08 – Conditions & Logic
Skill: Nest if/else statements
Description: Students write nested if/else blocks where an else branch contains another if (e.g., checking weather type, then checking temperature). This models multi-step decision-making and introduces hierarchical conditional structures.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G4.01: Combine two conditions with AND

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

---

## T08.G4.09 (UPDATED - Dependencies Change)

```markdown
ID: T08.G4.09
Topic: T08 – Conditions & Logic
Skill: Trace code with a sequence of if/else blocks
Description: Students trace code with 2-3 sequential `if/else` blocks and predict the final output for a given set of conditions. This develops the ability to track program state through multiple consecutive decision points.

Dependencies:
* T08.G3.04: Trace code with a single if/else

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

---

## T08.G5.05 (UPDATED - Dependencies Change)

```markdown
ID: T08.G5.05
Topic: T08 – Conditions & Logic
Skill: Use inline if-then-else expressions to compute conditional values
Description: Students use CreatiCode's inline conditional expression reporter block (`if <condition> then [value1] else [value2]`) to compute values conditionally without using full if/else control blocks. This is useful for setting variables or parameters based on a condition in a single expression (e.g., `set speed to (if fast mode then 10 else 5)`). This introduces the ternary operator concept and promotes more concise code.

Dependencies:
* T08.G5.01: Design multi-branch decision logic

CSTA: E5-ALG-AF-01, E5-PRO-PF-01
```

---

## CHANGE SUMMARY

### Total Skills Modified: 10
- 1 NEW skill added (T08.G3.03b)
- 2 Description changes (T08.G3.02, T08.G4.03)
- 6 Dependency changes (T08.G3.04, T08.G4.01, T08.G4.02, T08.G4.04, T08.G4.09, T08.G5.05)

### Insertion Point:
Insert T08.G3.03b after this block:
```
ID: T08.G3.03
Topic: T08 – Conditions & Logic
Skill: Pick the right conditional block for a scenario
...
CSTA: E3-ALG-AF-01, E3-PRO-PF-01


```

And before this block:
```
ID: T08.G3.04
Topic: T08 – Conditions & Logic
Skill: Trace code with a single if/else
...
```

---

## VALIDATION AFTER PASTING

Run these checks:
1. ✓ T08.G3.03b exists between T08.G3.03 and T08.G3.04
2. ✓ T08.G3.02 no longer mentions "AND" in description
3. ✓ T08.G4.01 only has 2 dependencies (not 3)
4. ✓ T08.G4.02 depends on T08.G4.01 (not T08.G3.05)
5. ✓ T08.G4.04 depends on T08.G4.01 (not T08.G3.05)
6. ✓ T08.G4.09 has only 1 dependency (T08.G3.04)
7. ✓ T08.G5.05 has only 1 dependency (T08.G5.01)
8. ✓ Total T08 skills count = 36 (was 35)

---

## FILES TO BACKUP BEFORE CHANGES

- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

Recommended: Create backup with timestamp:
```bash
cp allskills.md allskills_backup_$(date +%Y%m%d_%H%M%S).md
```
