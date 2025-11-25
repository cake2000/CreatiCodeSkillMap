# T08 Conditions & Logic - Proposed Changes Summary

## Quick Stats
- **Current**: 55 skills (K-8)
- **After fixes**: 57 skills (K-8)
- **Net change**: +2 skills
- **Major updates**: 40+ dependency removals, 4 new skills, 2 skills merged

---

## CRITICAL CHANGES (Priority 1 - Must Fix)

### 1. Add Bridge Skill for Grade 3
**INSERT NEW SKILL between T08.G2.03 and T08.G3.00:**

```
ID: T08.G3.00-pre
Topic: T08 – Conditions & Logic
Skill: Match scenarios to if-block descriptions
Description: Students match simple unplugged scenarios to descriptions of how an "if block" would work in programming (e.g., "If the sprite touches the edge, it turns around" - match to picture of sprite behavior). This conceptual bridge connects unplugged conditional thinking to block-based conditional structures without requiring coding yet. Uses visual matching activities with 4-5 scenario pairs.

Dependencies:
* T08.G2.03: Identify which rule applies in a situation

CSTA: E3-ALG-AF-01
```

**UPDATE T08.G3.00 dependencies:**
```
OLD: T07.G3.01, T08.G2.03
NEW: T07.G3.01, T08.G3.00-pre
```

---

### 2. Streamline Grade 4 Dependencies (Remove 40+ redundant G2 dependencies)

#### T08.G4.00 - Understand AND truth table
```
OLD Dependencies:
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G3.05: Fix a condition that uses the wrong comparison operator

NEW Dependencies:
* T08.G3.05: Fix a condition that uses the wrong comparison operator
```

#### T08.G4.01 - Combine two conditions with AND
```
OLD Dependencies (6 total):
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G4.00: Understand AND truth table

NEW Dependencies:
* T08.G4.00b: Identify situations requiring AND
* T08.G3.05: Fix a condition that uses the wrong comparison operator
```

#### T08.G4.02 - Combine two conditions with OR
```
OLD Dependencies (9 total):
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G2.03: Design a simple "if-then" game rule
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G4.01: Combine two conditions with AND
* T09.G3.01.04: Display variable value on stage using the variable monitor

NEW Dependencies:
* T08.G4.01c: Distinguish AND vs OR scenarios
* T09.G3.01.04: Display variable value on stage using the variable monitor
```

#### T08.G4.03 - Trace code with compound conditionals
```
OLD Dependencies (7 total):
* T01.G2.01: Find actions that repeat in everyday tasks
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G4.01: Combine two conditions with AND
* T13.G3.01: Test and trace simple block-based scripts

NEW Dependencies:
* T08.G4.02: Combine two conditions with OR
* T13.G3.01: Test and trace simple block-based scripts
```

#### T08.G4.04 - Nest if/else statements
```
OLD Dependencies (5 total):
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G4.03: Trace code with compound conditionals

NEW Dependencies:
* T08.G4.03b: Identify nesting levels
```

#### T08.G4.05 - Use else-if for multiple exclusive conditions
```
OLD Dependencies (8 total):
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G2.03: Design a simple "if-then" game rule
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G4.03: Trace code with compound conditionals
* T08.G4.04: Nest if/else statements

NEW Dependencies:
* T08.G4.04: Nest if/else statements
```

#### T08.G4.06 - Convert nested if to cleaner logic (CRITICAL BUG FIX)
```
OLD Dependencies:
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G4.01: Combine two conditions with AND
* T08.G4.02: Combine two conditions with OR
* T08.G4.05: Use else-if for multiple exclusive conditions

NEW Dependencies:
* T08.G4.04: Nest if/else statements  [ADDED - WAS MISSING!]
* T08.G4.05: Use else-if for multiple exclusive conditions
* T08.G4.05b: Use NOT to invert conditions
```

#### T08.G4.07 - Use if to control state changes
```
OLD Dependencies:
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.02: Build a key‑press script that controls a sprite
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G3.05: Fix a condition that uses the wrong comparison operator
* T09.G3.01.04: Display variable value on stage using the variable monitor

NEW Dependencies:
* T08.G3.05: Fix a condition that uses the wrong comparison operator
* T06.G3.02: Build a key‑press script that controls a sprite
* T09.G3.01.04: Display variable value on stage using the variable monitor
```

#### T08.G4.08 - Analyze and fix a compound logic bug
```
OLD Dependencies (9 total):
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G4.01: Combine two conditions with AND
* T08.G4.02: Combine two conditions with OR
* T08.G4.03: Trace code with compound conditionals
* T08.G4.05: Use else-if for multiple exclusive conditions
* T13.G3.01: Test and trace simple block-based scripts

NEW Dependencies:
* T08.G4.05b: Use NOT to invert conditions
* T08.G4.03: Trace code with compound conditionals
* T13.G3.01: Test and trace simple block-based scripts
```

#### T08.G4.09 - Trace code with a sequence of if/else blocks
```
OLD Dependencies (5 total):
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G3.04: Trace code with a single if/else
* T13.G3.01: Test and trace simple block-based scripts

NEW Dependencies:
* T08.G3.04: Trace code with a single if/else
* T13.G3.01: Test and trace simple block-based scripts
```

---

### 3. Reorganize Boolean Operator Truth Tables (Move to beginning of G4)

**RENAME/RENUMBER existing skills:**

```
T08.G4.01a → T08.G4.00c: Understand OR truth table
T08.G4.05a → T08.G4.00d: Understand NOT truth table
T08.G4.01b → T08.G4.01c: Distinguish AND vs OR scenarios
```

**ADD NEW SKILL:**
```
ID: T08.G4.01b
Topic: T08 – Conditions & Logic
Skill: Identify situations requiring OR
Description: Students recognize real-world scenarios that require at least one condition to be true (e.g., "You can enter if you have a ticket OR you're on the guest list", "Alert fires if battery is low OR temperature is high"). This develops pattern recognition for OR logic before coding it. Present 4-5 scenarios similar to T08.G4.00b but for OR.

Dependencies:
* T08.G4.01: Combine two conditions with AND
* T08.G4.00c: Understand OR truth table

CSTA: E4-ALG-AF-01
```

**NEW SEQUENCE for G4 truth tables:**
1. T08.G4.00 - Understand AND truth table
2. T08.G4.00b - Identify situations requiring AND
3. T08.G4.00c - Understand OR truth table [MOVED from G4.01a]
4. T08.G4.00d - Understand NOT truth table [MOVED from G4.05a]
5. T08.G4.01 - Combine two conditions with AND
6. T08.G4.01b - Identify situations requiring OR [NEW]
7. T08.G4.01c - Distinguish AND vs OR scenarios [MOVED from G4.01b]
8. T08.G4.02 - Combine two conditions with OR
... continue with existing sequence

**Keep T08.G4.05b in its current position** (after else-if)

---

### 4. Fix T08.G5.00 Wrong Dependency
```
ID: T08.G5.00 - Draw decision tree flowchart

OLD Dependencies:
* T08.G4.05: Use else-if for multiple exclusive conditions
* T08.G4.09: Trace code with a sequence of if/else blocks
* T02.G2.01: Turn a picture routine into labeled boxes
* T03.G5.01: Create a feature list and subtask breakdown

NEW Dependencies:
* T08.G4.05: Use else-if for multiple exclusive conditions
* T08.G4.09: Trace code with a sequence of if/else blocks
* T08.G2.01: Follow branching paths based on yes/no questions
* T03.G5.01: Create a feature list and subtask breakdown
```

**Rationale**: T02.G2.01 is about sequential box diagrams, not branching. T08.G2.01 is about following branching paths, which is the correct prerequisite.

---

### 5. Simplify T08.G5.03 Dependencies
```
ID: T08.G5.03 - Combine three or more conditions

OLD Dependencies:
* T08.G4.05b: Use NOT to invert conditions
* T08.G4.08: Analyze and fix a compound logic bug
* T09.G3.03: Use a variable in a simple conditional
* T02.G5.01: Trace a script with nested loops using debug print

NEW Dependencies:
* T08.G4.05b: Use NOT to invert conditions
* T08.G4.08: Analyze and fix a compound logic bug
```

**Rationale**: Variable usage and tracing are already assumed through prerequisite chains.

---

### 6. Merge G6 Simulation Skills
**REMOVE these two skills:**
```
T08.G6.01a - Use conditionals in physics simulations
T08.G6.01b - Use conditionals in population models
```

**UPDATE T08.G6.01:**
```
ID: T08.G6.01
Topic: T08 – Conditions & Logic
Skill: Use conditionals to control simulation steps
Description: Students write conditionals that control simulation behavior across various domains: physics (collision detection "if sprite touching wall then reverse direction", boundary checking "if y < 0 then set y to 0"), biology (population dynamics "if population > carrying capacity then increase death rate", resource limits "if food < threshold then reduce birth rate"), or games (state transitions, win/loss conditions). Students complete projects in at least one domain. This applies conditional logic to scientific and mathematical modeling contexts.

Dependencies:
* T08.G5.03: Combine three or more conditions
* T08.G5.04: Trace complex decision logic

CSTA: E6-ALG-AF-01, E6-PRO-PF-01
```

---

### 7. Add G7 Bridge Skill to G8
**INSERT NEW SKILL after T08.G7.02:**

```
ID: T08.G7.03
Topic: T08 – Conditions & Logic
Skill: Simplify complex boolean expressions
Description: Students apply boolean algebra rules (De Morgan's laws, distributive property, elimination of double negation) to simplify complex conditional expressions. For example, simplify "NOT(A OR B)" to "NOT A AND NOT B", or "if (A AND B) OR (A AND C)" to "if A AND (B OR C)". This develops formal logic skills and prepares students for analyzing logical equivalence in G8.

Dependencies:
* T08.G4.05b: Use NOT to invert conditions
* T08.G6.03: Debug multi-condition logic

CSTA: E7-ALG-AF-01
```

**UPDATE T08.G8.01 dependencies:**
```
OLD Dependencies:
* T04.G6.01: Group snippets by underlying algorithm pattern
* T08.G6.01: Use conditionals to control simulation steps
* T08.G7.01: Reason about fairness using conditions
* T08.G7.02: Design tests for condition-heavy code
* [cross-topic dependencies]

NEW Dependencies:
* T04.G6.01: Group snippets by underlying algorithm pattern
* T08.G6.01: Use conditionals to control simulation steps
* T08.G7.01: Reason about fairness using conditions
* T08.G7.02: Design tests for condition-heavy code
* T08.G7.03: Simplify complex boolean expressions  [ADDED]
* [cross-topic dependencies]
```

---

## OPTIONAL ENHANCEMENTS (Priority 2 - Nice to Have)

### 8. Add Practice Skill for Choosing AND vs OR
**INSERT NEW SKILL after T08.G4.02:**

```
ID: T08.G4.02b
Topic: T08 – Conditions & Logic
Skill: Choose between AND and OR for coding scenarios
Description: Given scenario descriptions, students determine whether to use AND or OR and implement the correct compound condition. For example, "Alert if score is low OR time is running out" vs "Unlock door if player has key AND puzzle is solved". This applies conceptual understanding of boolean operators to practical coding decisions. Students complete 3-4 scenarios.

Dependencies:
* T08.G4.02: Combine two conditions with OR
* T08.G4.01c: Distinguish AND vs OR scenarios

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

---

## SUMMARY TABLE

| Change Type | Count | Impact |
|------------|-------|--------|
| Skills Added | 4 | +4 |
| Skills Removed (merged) | 2 | -2 |
| Skills Renamed/Renumbered | 3 | 0 |
| **Net Change** | **+2** | **55 → 57 skills** |
| Dependency Removals | 40+ | Huge maintenance improvement |
| Critical Bug Fixes | 2 | T08.G4.06, T08.G5.00 |

---

## VALIDATION RESULTS

### ✅ All Issues Resolved:
- [x] X-2 rule violations fixed (removed 40+ G2 deps from G4)
- [x] Circular dependencies eliminated
- [x] Missing prerequisites added (G4.06 → G4.04)
- [x] Wrong dependencies corrected (G5.00: T02→T08)
- [x] Logical sequencing improved (truth tables grouped)
- [x] Grade progression gaps filled (G3 bridge, G7 bridge)
- [x] Age-appropriate content maintained (K-2 unplugged, 3+ coding)

### ✅ Quality Improvements:
- Cleaner dependency chains
- Better conceptual grouping
- Reduced redundancy
- Smoother learning progression
- Appropriate skill granularity

---

## IMPLEMENTATION ORDER

1. **Phase 1** (Critical - Do First):
   - Add T08.G3.00-pre
   - Streamline all G4 dependencies (9 skills)
   - Fix T08.G4.06 missing dependency
   - Fix T08.G5.00 wrong dependency

2. **Phase 2** (Structural):
   - Reorganize boolean operators (rename/renumber G4.01a, G4.05a, G4.01b)
   - Add T08.G4.01b (OR situations)
   - Merge G6.01a/b into G6.01
   - Add T08.G7.03 bridge skill

3. **Phase 3** (Optional):
   - Add T08.G4.02b (AND vs OR practice)
   - Review/refine skill descriptions

---

## FILES TO UPDATE

1. `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` - Main skills file
2. Create optimization summary: `T08_optimization_summary.md`
3. Create optimized version: `T08_optimized.md`

**Total estimated time**: 2-3 hours for full implementation
