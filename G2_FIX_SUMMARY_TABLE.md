# G2 Skills Fix Summary Table

Quick reference for all 30 G2 skills requiring dependency fixes.

---

## HIGH PRIORITY: Broken/Incorrect References (4 skills)

| Skill ID | Skill Name | REMOVE | ADD | Reason |
|----------|-----------|--------|-----|--------|
| T13.G2.03 | Fix a repeated step that happens too many or too few times | T13.G2.01: Spot what doesn't belong in a pattern | T04.G2.01: Identify the repeating unit in a longer pattern<br>T01.G2.01: Find actions that repeat in everyday tasks | Broken reference - T13.G2.01 is not about patterns |
| T13.G2.04 | Add a simple check to see if steps worked | T13.G2.03: Fix the wrong step in a simple task | T01.G1.09: Match an algorithm to its goal | Broken reference - T13.G2.03 is not about fixing wrong steps |
| T20.G2.03 | Build layered pattern recipes | T20.G2.01: Identify win and lose in a simple game | T20.G2.01: Use repeat cards in an art recipe<br>T01.G2.02: Use "repeat" to make directions shorter | Broken reference - T20.G2.01 is not about games |
| T23.G2.02 | Spot when sensor data might be unclear | T23.G2.01: Match a color to a feeling | T23.G2.01: Pick the right sensor for a job | Broken reference - T23.G2.01 is not about colors |

---

## HIGH PRIORITY: G2→GK.07 Dependencies (8 skills)

**Pattern:** Replace T01.GK.07 with G1 bridge or remove for transitive redundancy

| Skill ID | Skill Name | REMOVE | ADD | Fix Type |
|----------|-----------|--------|-----|----------|
| T01.G2.01 | Find actions that repeat in everyday tasks | T01.G1.10: Match pictures to "if/then" rules<br>T01.GK.07: Find the pattern that repeats | T04.G1.03: Find repeated steps in an instruction list | Replace GK with G1 bridge |
| T01.G2.02 | Use "repeat" to make directions shorter | T01.GK.07: Find the pattern that repeats | (none - keep T01.G2.01 only) | Transitive redundancy |
| T01.G2.08 | Trace an algorithm that uses "repeat ___ times" | T01.GK.07: Find the pattern that repeats | (none - keep T01.G2.03 only) | Transitive redundancy |
| T04.G2.02 | Spot repeated step sequences in everyday algorithms | T01.GK.07: Find the pattern that repeats | (none - keep T04.G2.01 only) | Transitive redundancy |
| T04.G2.04 | Replace repeated steps with a "repeat ___ times" phrase | T01.GK.07: Find the pattern that repeats | (none - keep T04.G2.03 only) | Transitive redundancy |
| T12.G2.02 | Fix confusing labels on a plan | T01.GK.05: Move the picture that's in the wrong place | T12.G1.02: Give a clear title to a set of steps | Replace GK with G1 bridge |
| T13.G2.01 | Fix steps that use the wrong signal | T01.GK.05: Move the picture that's in the wrong place | T01.G1.06: Fix a routine with one wrong step | Replace GK with G1 bridge |
| T23.G2.01 | Pick the right sensor for a job | T04.GK.01: Spot a simple repeating pattern | T23.G1.03: Choose what a sensor can notice | Replace GK with G1 bridge |

---

## HIGH PRIORITY: G2→GK.08 Dependencies (9 skills)

**Pattern:** Replace T01.GK.08 with topic-appropriate G1 skills

| Skill ID | Skill Name | REMOVE | ADD | New Topic Bridge |
|----------|-----------|--------|-----|------------------|
| T25.G2.02 | Translate between timeline, table, and sentence | T01.GK.08: Count how many times | T25.G1.03: Describe the same fact in words and numbers | T25 (Data Rep) |
| T25.G2.03 | Pick the best representation for a question | T01.GK.08: Count how many times | T25.G1.02: Design a picture table<br>T25.G2.02: Translate between timeline, table, and sentence | T25 (Data Rep) |
| T25.G2.04 | Combine two data attributes | T01.G1.01: Put pictures in order to plant a seed<br>T01.GK.08: Count how many times | T25.G1.02: Design a picture table | T25 (Data Rep) |
| T26.G2.02 | Build a two-column record sheet | T01.G1.01: Put pictures in order to plant a seed<br>T01.GK.08: Count how many times | T26.G1.01: Run a three-option picture survey<br>T25.G1.02: Design a picture table | T26 (Data Collection) |
| T26.G2.04 | Explain why sample size matters | T01.G1.01: Put pictures in order to plant a seed<br>T01.GK.08: Count how many times | T26.G1.01: Run a three-option picture survey<br>T26.G2.02: Build a two-column record sheet | T26 (Data Collection) |
| T27.G2.02 | Interpret simple line plots | T01.GK.08: Count how many times | T27.G1.01: Build a pictograph from tallies | T27 (Data Analysis) |
| T27.G2.04 | Decide if data answers the question asked | T01.G1.10: Match pictures to "if/then" rules<br>T01.GK.08: Count how many times | T27.G1.03: Tell a one-sentence story with data<br>T27.G2.02: Interpret simple line plots | T27 (Data Analysis) |
| T28.G2.02 | Conduct a picture-based chance experiment | T01.G1.01: Put pictures in order to plant a seed<br>T01.GK.08: Count how many times | T26.G1.01: Run a three-option picture survey<br>T25.G1.01: Record data with tally marks | T28 (Chance) |
| T28.G2.04 | Predict and observe outcomes | T01.G1.01: Put pictures in order to plant a seed<br>T01.GK.08: Count how many times | T28.G2.02: Conduct a picture-based chance experiment<br>T01.G1.04: Predict the next step in a story sequence | T28 (Chance) |

---

## MEDIUM PRIORITY: Transitive Redundancies (5 skills)

**Pattern:** Remove dependencies already covered transitively

| Skill ID | Skill Name | REMOVE | KEEP | Transitive Path |
|----------|-----------|--------|------|-----------------|
| T03.G2.02 | Group similar subtasks together | T03.G1.03: List steps for a simple classroom routine | T03.G2.01: Choose subtasks for a simple project idea | T03.G2.01 → T03.G1.03 |
| T05.G2.02 | Identify features that make a design more accessible | T05.G1.01: Identify what a character needs in a story | T05.G1.04: Suggest one change that helps a specific user | T05.G1.04 → T05.G1.02 → T05.G1.01 |
| T14.G2.02 | Track lives and game over conditions | T01.G1.01: Put pictures in order to plant a seed | T01.G1.04: Predict the next step in a story sequence | T01.G1.04 → T01.G1.01 |
| T14.G2.04 | Sequence a safe route | T01.G1.01: Put pictures in order to plant a seed | T01.G1.04: Predict the next step in a story sequence | T01.G1.04 → T01.G1.01 |
| T20.G2.04 | Explain how a change affects the art | T01.G1.01: Put pictures in order to plant a seed | T01.G1.04: Predict the next step in a story sequence<br>T20.G2.03: Build layered pattern recipes | T01.G1.04 → T01.G1.01 |

---

## Statistics

### Total Skills to Fix: 30

**By Priority:**
- High Priority: 21 skills (70%)
- Medium Priority: 9 skills (30%)

**By Fix Type:**
- Broken/incorrect references: 4 skills
- Replace GK with G1 bridge: 17 skills
- Remove transitive redundancy: 9 skills

**GK Dependencies Removed:**
- T01.GK.07: 5 removals (+ 1 replacement)
- T01.GK.08: 9 removals
- T01.GK.05: 2 replacements
- T04.GK.01: 1 replacement

**G1 Bridge Skills Introduced:**
- T04.G1.03: 1 usage
- T12.G1.02: 1 usage
- T01.G1.06: 1 usage
- T23.G1.03: 1 usage
- T25.G1.03: 1 usage
- T25.G1.02: 3 usages
- T25.G1.01: 1 usage
- T26.G1.01: 4 usages
- T27.G1.01: 1 usage
- T27.G1.03: 1 usage
- T01.G1.09: 1 usage
- T01.G1.04: 1 new usage (was already used elsewhere)

---

## Implementation Order Recommendation

### Phase 1: Fix Broken References (Critical)
These cause confusion and must be fixed first:
1. T13.G2.03
2. T13.G2.04
3. T20.G2.03
4. T23.G2.02

### Phase 2: Fix G2→GK Bridges (High Priority)
Replace kindergarten dependencies with proper G1 bridges:
5. T01.G2.01
6. T12.G2.02
7. T13.G2.01
8. T23.G2.01
9. T25.G2.02 through T28.G2.04 (data skills)

### Phase 3: Remove Transitive Redundancies (Medium Priority)
Clean up redundant dependencies:
10. T01.G2.02, T01.G2.08, T04.G2.02, T04.G2.04
11. T03.G2.02, T05.G2.02
12. T14.G2.02, T14.G2.04, T20.G2.04

### Phase 4: Validate
Run validation queries from main fix plan.

---

**END OF SUMMARY TABLE**
