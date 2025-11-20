# G2 Skills Dependency Fix Plan

**Generated:** 2025-11-20
**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md

---

## EXECUTIVE SUMMARY

This plan addresses 43 G2 skill dependency issues across three priority levels:
- **HIGH PRIORITY:** 21 skills (4 broken references + 17 G2→GK bridges)
- **MEDIUM PRIORITY:** 9 skills (transitive redundancies)
- **LOW PRIORITY:** 26 skills (same-topic dependencies - marked as OK, no fix needed)

---

## HIGH PRIORITY FIXES

### Category 1: Broken/Incorrect Dependency References (4 skills)

These skills reference dependencies that don't exist or point to the wrong skill.

#### FIX 1.1: T13.G2.03 - Fix a repeated step that happens too many or too few times

**Current Dependency:**
```
* T13.G2.01: Spot what doesn't belong in a pattern
```

**Issue:** T13.G2.01 is actually "Fix steps that use the wrong signal", NOT "Spot what doesn't belong in a pattern"

**Analysis:**
- T13.G2.03 is about fixing repeat counts (e.g., clap 2 times instead of 5)
- The skill needs prerequisites about:
  1. Understanding repeating patterns
  2. Recognizing when something is wrong in a pattern

**Proposed Fix:**
```
Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T01.G2.01: Find actions that repeat in everyday tasks
```

**Rationale:**
- T04.G2.01 teaches identifying the unit that repeats (critical for knowing what "should" repeat)
- T01.G2.01 teaches recognizing repeated actions (foundation for understanding repeat counts)
- These are more appropriate prerequisites than a debugging skill about wrong signals

---

#### FIX 1.2: T13.G2.04 - Add a simple check to see if steps worked

**Current Dependencies:**
```
* T13.G2.03: Fix the wrong step in a simple task
* T03.G1.03: List steps for a simple classroom routine
```

**Issue:** T13.G2.03 is actually "Fix a repeated step that happens too many or too few times", NOT "Fix the wrong step in a simple task"

**Analysis:**
- T13.G2.04 is about adding verification/check steps to algorithms
- The skill needs prerequisites about:
  1. Understanding multi-step algorithms
  2. Recognizing goals/outcomes in routines

**Proposed Fix:**
```
Dependencies:
* T03.G1.03: List steps for a simple classroom routine
* T01.G1.09: Match an algorithm to its goal
```

**Rationale:**
- Keep T03.G1.03 (valid prerequisite for understanding multi-step routines)
- Replace incorrect T13.G2.03 with T01.G1.09 (understanding goals is critical for adding verification checks)
- T01.G1.09 teaches matching algorithms to goals, which is foundational for knowing what to verify

---

#### FIX 1.3: T20.G2.03 - Build layered pattern recipes

**Current Dependency:**
```
* T20.G2.01: Identify win and lose in a simple game
```

**Issue:** T20.G2.01 is actually "Use repeat cards in an art recipe", NOT "Identify win and lose in a simple game"

**Analysis:**
- T20.G2.03 is about interpreting two-layer instructions ("repeat row A three times, then repeat row B once")
- This is clearly a more advanced version of T20.G2.01

**Proposed Fix:**
```
Dependencies:
* T20.G2.01: Use repeat cards in an art recipe
* T01.G2.02: Use "repeat" to make directions shorter
```

**Rationale:**
- T20.G2.01 is the correct prerequisite (using repeat in simple art recipes)
- T01.G2.02 provides foundation for understanding "repeat" notation
- This creates a natural progression: simple repeat → single-layer repeat → multi-layer repeat

---

#### FIX 1.4: T23.G2.02 - Spot when sensor data might be unclear

**Current Dependency:**
```
* T23.G2.01: Match a color to a feeling
```

**Issue:** T23.G2.01 is actually "Pick the right sensor for a job", NOT "Match a color to a feeling"

**Analysis:**
- T23.G2.02 is about recognizing when sensor input might be unclear (bright vs dark room)
- This clearly depends on knowing what sensors do

**Proposed Fix:**
```
Dependencies:
* T23.G2.01: Pick the right sensor for a job
```

**Rationale:**
- T23.G2.01 is the correct prerequisite
- Understanding sensor capabilities is foundational for recognizing their limitations
- No additional dependencies needed - this is a direct extension

---

### Category 2: G2→GK Dependencies Missing G1 Bridge (17 skills)

These skills jump from G2 to GK, skipping the G1 bridge level. We need to check if G1 bridges exist and use them.

#### Subcategory 2A: Dependencies on T01.GK.07 "Find the pattern that repeats" (10 skills)

**Analysis of T01.GK.07:**
- T01.GK.07: "Find the pattern that repeats" (GK level)
- T04.G1.03: "Find repeated steps in an instruction list" (G1 level) - **BRIDGES T01.GK.07**
- T04.G1.03 depends on T01.GK.07, so it's a valid G1 bridge

**Strategy:** Replace T01.GK.07 with T04.G1.03 where appropriate, OR keep both if the skill truly needs the foundational GK concept.

---

##### FIX 2A.1: T01.G2.01 - Find actions that repeat in everyday tasks

**Current Dependencies:**
```
* T01.G1.10: Match pictures to "if/then" rules
* T01.GK.07: Find the pattern that repeats
```

**Analysis:**
- T01.G1.10 is NOT relevant (it's about if/then, not patterns)
- T01.GK.07 is a direct prerequisite but skips G1

**Proposed Fix:**
```
Dependencies:
* T04.G1.03: Find repeated steps in an instruction list
```

**Rationale:**
- T04.G1.03 is the G1 bridge for T01.GK.07
- T04.G1.03 transitively includes T01.GK.07
- Remove T01.G1.10 (not relevant to finding repeating actions)
- This creates clean progression: GK pattern recognition → G1 find repeated steps → G2 apply to everyday tasks

---

##### FIX 2A.2: T01.G2.02 - Use "repeat" to make directions shorter

**Current Dependencies:**
```
* T01.G2.01: Find actions that repeat in everyday tasks
* T01.GK.07: Find the pattern that repeats
```

**Analysis:**
- T01.G2.01 is the direct prerequisite
- T01.GK.07 is redundant (covered transitively through T01.G2.01 → T04.G1.03 → T01.GK.07)

**Proposed Fix:**
```
Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
```

**Rationale:**
- Remove T01.GK.07 (transitive redundancy)
- T01.G2.01 already depends on the pattern-finding foundation via T04.G1.03
- Clean sequential progression within G2

---

##### FIX 2A.3: T01.G2.08 - Trace an algorithm that uses "repeat ___ times"

**Current Dependencies:**
```
* T01.G2.03: Replace repeated steps with a repeat instruction
* T01.GK.07: Find the pattern that repeats
```

**Analysis:**
- T01.G2.03 is the direct prerequisite
- T01.GK.07 is redundant (covered transitively)

**Proposed Fix:**
```
Dependencies:
* T01.G2.03: Replace repeated steps with a repeat instruction
```

**Rationale:**
- Remove T01.GK.07 (transitive redundancy)
- T01.G2.03 → T01.G2.01 → T04.G1.03 → T01.GK.07
- Tracing repeat algorithms logically follows from creating them

---

##### FIX 2A.4: T04.G2.02 - Spot repeated step sequences in everyday algorithms

**Current Dependencies:**
```
* T04.G2.01: Identify the repeating unit in a longer pattern
* T01.GK.07: Find the pattern that repeats
```

**Analysis:**
- T04.G2.01 is the direct prerequisite
- T01.GK.07 is redundant (T04.G2.01 → T04.G1.03 → T01.GK.07)

**Proposed Fix:**
```
Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
```

**Rationale:**
- Remove T01.GK.07 (transitive redundancy)
- Clean progression: identify unit → spot in algorithms
- Foundation already covered through T04.G2.01's dependencies

---

##### FIX 2A.5: T04.G2.04 - Replace repeated steps with a "repeat ___ times" phrase

**Current Dependencies:**
```
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T01.GK.07: Find the pattern that repeats
```

**Analysis:**
- T04.G2.03 is the direct prerequisite
- T01.GK.07 is redundant (covered transitively through T04.G2.01 → T04.G1.03 → T01.GK.07)

**Proposed Fix:**
```
Dependencies:
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
```

**Rationale:**
- Remove T01.GK.07 (transitive redundancy)
- T04.G2.03 → T04.G2.01 → T04.G1.03 → T01.GK.07
- Clear sequential progression for compression mechanics

---

##### FIX 2A.6: T12.G2.02 - Fix confusing labels on a plan

**Current Dependency:**
```
* T01.GK.05: Move the picture that's in the wrong place
```

**Analysis:**
- T01.GK.05 is about sequencing (moving pictures to correct position)
- T12.G2.02 is about labeling/organizing (replacing vague titles with clear ones)
- There IS a G1 bridge: T12.G1.02 "Give a clear title to a set of steps"

**Proposed Fix:**
```
Dependencies:
* T12.G1.02: Give a clear title to a set of steps
```

**Rationale:**
- T12.G1.02 is the direct G1 bridge (teaches giving clear titles at G1 level)
- T12.G2.02 extends this to *fixing* bad labels (a debugging/revision task)
- Much more relevant than sequencing prerequisite T01.GK.05
- Natural progression: learn to create good labels → fix bad labels

---

##### FIX 2A.7: T13.G2.01 - Fix steps that use the wrong signal

**Current Dependency:**
```
* T01.GK.05: Move the picture that's in the wrong place
```

**Analysis:**
- T01.GK.05 is about sequencing
- T13.G2.01 is about debugging signals (fixing wrong signal references)
- There IS a G1 bridge: T01.G1.06 "Fix a routine with one wrong step"

**Proposed Fix:**
```
Dependencies:
* T01.G1.06: Fix a routine with one wrong step
```

**Rationale:**
- T01.G1.06 is the G1 bridge for fixing wrong steps
- T01.G1.06 depends on T01.GK.05, so we get the sequencing foundation transitively
- Natural progression: fix wrong steps (general) → fix wrong signals (specific)
- More semantically relevant prerequisite

---

##### FIX 2A.8: T23.G2.01 - Pick the right sensor for a job

**Current Dependency:**
```
* T04.GK.01: Spot a simple repeating pattern
```

**Analysis:**
- T04.GK.01 is about pattern recognition (NOT relevant to sensors)
- This appears to be an incorrect dependency
- There IS a G1 bridge: T23.G1.03 "Choose what a sensor can notice"

**Proposed Fix:**
```
Dependencies:
* T23.G1.03: Choose what a sensor can notice
```

**Rationale:**
- T23.G1.03 is the appropriate G1 prerequisite (teaches sensor capabilities)
- Natural progression: what sensors can notice → pick the right sensor for a job
- Remove T04.GK.01 (completely unrelated to sensors)
- Clean bridge from G1 to G2 within the same topic

---

#### Subcategory 2B: Dependencies on T01.GK.08 "Count how many times" (9 skills)

**Analysis of T01.GK.08:**
- T01.GK.08: "Count how many times" (GK level)
- No direct G1 bridge exists in T01 for counting
- However, T25.G1.01, T26.G1.01, T27.G1.01 all involve counting/tallying at G1 level
- These skills are in data/analysis topics, not algorithm topics

**Strategy:** Check if counting is truly needed, or if there's a more relevant G1 prerequisite. If counting is essential and no better bridge exists, keep T01.GK.08 but flag it.

---

##### FIX 2B.1: T25.G2.02 - Translate between timeline, table, and sentence

**Current Dependencies:**
```
* T01.G1.01: Put pictures in order to plant a seed
* T01.GK.08: Count how many times
```

**Analysis:**
- T01.G1.01 is relevant (sequencing foundation for timelines)
- T01.GK.08 (counting) is not directly relevant to translation between formats
- Better bridge: T25.G1.03 "Describe the same fact in words and numbers"

**Proposed Fix:**
```
Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T25.G1.03: Describe the same fact in words and numbers
```

**Rationale:**
- T25.G1.03 is the perfect G1 bridge (teaches multi-format representation)
- More relevant than counting
- Creates topic-consistent progression: G1 describe in multiple formats → G2 translate between them

---

##### FIX 2B.2: T25.G2.03 - Pick the best representation for a question

**Current Dependency:**
```
* T01.GK.08: Count how many times
```

**Analysis:**
- Counting alone is insufficient for choosing representations
- Need understanding of multiple representation types

**Proposed Fix:**
```
Dependencies:
* T25.G1.02: Design a picture table
* T25.G2.02: Translate between timeline, table, and sentence
```

**Rationale:**
- T25.G1.02 introduces structured representations at G1
- T25.G2.02 teaches understanding different formats (prerequisite for choosing best one)
- Logical progression: understand formats → translate between them → choose the best one
- Remove T01.GK.08 (too narrow, not directly relevant)

---

##### FIX 2B.3: T25.G2.04 - Combine two data attributes

**Current Dependencies:**
```
* T01.G1.01: Put pictures in order to plant a seed
* T01.GK.08: Count how many times
```

**Analysis:**
- T01.G1.01 is not particularly relevant (sequencing ≠ data pairing)
- T01.GK.08 is not relevant (counting ≠ combining attributes)
- Better bridge: T25.G1.02 "Design a picture table" (introduces structured data)

**Proposed Fix:**
```
Dependencies:
* T25.G1.02: Design a picture table
```

**Rationale:**
- T25.G1.02 introduces organizing data in structured format (rows/columns)
- Combining attributes is a natural extension of table structure
- More relevant than sequencing or counting
- Clean topic-consistent progression

---

##### FIX 2B.4: T26.G2.02 - Build a two-column record sheet

**Current Dependencies:**
```
* T01.G1.01: Put pictures in order to plant a seed
* T01.GK.08: Count how many times
```

**Analysis:**
- T01.G1.01 is not relevant (sequencing ≠ data structure)
- T01.GK.08 is not relevant (counting ≠ record sheet design)
- Better bridge: T26.G1.01 "Run a three-option picture survey" (introduces data collection)

**Proposed Fix:**
```
Dependencies:
* T26.G1.01: Run a three-option picture survey
* T25.G1.02: Design a picture table
```

**Rationale:**
- T26.G1.01 introduces data collection at G1
- T25.G1.02 introduces table structure
- Two-column record sheet combines collection + structured storage
- Remove irrelevant T01.G1.01 and T01.GK.08

---

##### FIX 2B.5: T26.G2.04 - Explain why sample size matters

**Current Dependencies:**
```
* T01.G1.01: Put pictures in order to plant a seed
* T01.GK.08: Count how many times
```

**Analysis:**
- T01.G1.01 is not relevant (sequencing ≠ sample size)
- T01.GK.08 (counting) is somewhat relevant but indirect
- Better bridge: T26.G1.01 "Run a three-option picture survey" + T26.G2.02 (working with responses)

**Proposed Fix:**
```
Dependencies:
* T26.G1.01: Run a three-option picture survey
* T26.G2.02: Build a two-column record sheet
```

**Rationale:**
- T26.G1.01 introduces survey data collection
- T26.G2.02 teaches recording multiple responses
- Understanding sample size requires experience with collecting multiple data points
- Natural progression: collect data (G1) → record multiple responses (G2) → understand why more responses matter (G2)

---

##### FIX 2B.6: T27.G2.02 - Interpret simple line plots

**Current Dependencies:**
```
* T01.G1.01: Put pictures in order to plant a seed
* T01.GK.08: Count how many times
```

**Analysis:**
- T01.G1.01 has some relevance (time sequencing for line plots)
- T01.GK.08 is not particularly relevant
- Better bridge: T27.G1.01 "Build a pictograph from tallies" (introduces visual data representation)

**Proposed Fix:**
```
Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T27.G1.01: Build a pictograph from tallies
```

**Rationale:**
- Keep T01.G1.01 (sequencing is foundational for understanding time-series line plots)
- Replace T01.GK.08 with T27.G1.01 (progressing from pictographs to line plots)
- Natural data visualization progression: tallies → pictographs → line plots

---

##### FIX 2B.7: T27.G2.04 - Decide if data answers the question asked

**Current Dependencies:**
```
* T01.G1.10: Match pictures to "if/then" rules
* T01.GK.08: Count how many times
```

**Analysis:**
- T01.G1.10 is not particularly relevant (if/then logic ≠ data analysis)
- T01.GK.08 is not particularly relevant
- Better bridge: T27.G1.03 "Tell a one-sentence story with data" (introduces data interpretation)

**Proposed Fix:**
```
Dependencies:
* T27.G1.03: Tell a one-sentence story with data
* T27.G2.02: Interpret simple line plots
```

**Rationale:**
- T27.G1.03 teaches basic data interpretation at G1
- T27.G2.02 extends interpretation to specific chart types
- Deciding if data answers a question requires understanding what data shows
- Natural progression: tell what data shows → interpret charts → evaluate if data answers questions
- Remove irrelevant T01.G1.10 and T01.GK.08

---

##### FIX 2B.8: T28.G2.02 - Conduct a picture-based chance experiment

**Current Dependencies:**
```
* T01.G1.01: Put pictures in order to plant a seed
* T01.GK.08: Count how many times
```

**Analysis:**
- T01.G1.01 is not relevant (sequencing ≠ probability)
- T01.GK.08 (counting) is somewhat relevant (counting outcomes) but we need a better bridge
- Need prerequisite about recording observations

**Proposed Fix:**
```
Dependencies:
* T26.G1.01: Run a three-option picture survey
* T25.G1.01: Record data with tally marks
```

**Rationale:**
- T26.G1.01 introduces data collection methodology
- T25.G1.01 teaches recording repeated observations with tallies
- Chance experiments require both skills
- More relevant than generic sequencing
- Removes cross-topic GK dependency

---

##### FIX 2B.9: T28.G2.04 - Predict and observe outcomes

**Current Dependencies:**
```
* T01.G1.01: Put pictures in order to plant a seed
* T01.GK.08: Count how many times
```

**Analysis:**
- T01.G1.01 is not relevant (sequencing ≠ prediction)
- T01.GK.08 is somewhat relevant (counting correct/incorrect guesses)
- Better foundation: T28.G2.02 (conducting experiments first)

**Proposed Fix:**
```
Dependencies:
* T28.G2.02: Conduct a picture-based chance experiment
* T01.G1.04: Predict the next step in a story sequence
```

**Rationale:**
- T28.G2.02 teaches running chance experiments (prerequisite for comparing predictions)
- T01.G1.04 introduces prediction concept at G1
- Natural progression: learn to predict (G1) → conduct experiments (G2) → predict and compare outcomes (G2)
- Remove T01.G1.01 and T01.GK.08

---

## MEDIUM PRIORITY FIXES

### Category 3: Transitive Redundancies (9 skills)

These skills have dependencies that are already covered transitively through other dependencies.

---

#### FIX 3.1: T03.G2.02 - Group similar subtasks together

**Current Dependencies:**
```
* T03.G2.01: Choose subtasks for a simple project idea
* T03.G1.03: List steps for a simple classroom routine
```

**Analysis:**
- T03.G2.01 → T03.G1.03 (transitive coverage)
- T03.G1.03 is redundant

**Proposed Fix:**
```
Dependencies:
* T03.G2.01: Choose subtasks for a simple project idea
```

**Rationale:**
- Remove T03.G1.03 (transitive redundancy)
- Grouping subtasks logically follows from identifying them
- Clean sequential progression within topic

---

#### FIX 3.2: T05.G2.02 - Identify features that make a design more accessible

**Current Dependencies:**
```
* T05.G1.04: Suggest one change that helps a specific user
* T05.G1.01: Identify what a character needs in a story
```

**Analysis:**
- T05.G1.04 → T05.G1.02 → T05.G1.01 (transitive coverage)
- T05.G1.01 is redundant

**Proposed Fix:**
```
Dependencies:
* T05.G1.04: Suggest one change that helps a specific user
```

**Rationale:**
- Remove T05.G1.01 (transitive redundancy)
- T05.G1.04 already includes understanding user needs
- Clean single-path progression

---

#### FIX 3.3: T14.G2.02 - Track lives and game over conditions

**Current Dependencies:**
```
* T01.G1.01: Put pictures in order to plant a seed
* T01.G1.04: Predict the next step in a story sequence
```

**Analysis:**
- T01.G1.04 → T01.G1.01 (transitive coverage)
- T01.G1.01 is redundant

**Proposed Fix:**
```
Dependencies:
* T01.G1.04: Predict the next step in a story sequence
```

**Rationale:**
- Remove T01.G1.01 (transitive redundancy)
- Tracking game states requires prediction more than basic sequencing
- T01.G1.04 is more semantically relevant

---

#### FIX 3.4: T14.G2.04 - Sequence a safe route

**Current Dependencies:**
```
* T01.G1.01: Put pictures in order to plant a seed
* T01.G1.04: Predict the next step in a story sequence
```

**Analysis:**
- T01.G1.04 → T01.G1.01 (transitive coverage)
- T01.G1.01 is redundant

**Proposed Fix:**
```
Dependencies:
* T01.G1.04: Predict the next step in a story sequence
```

**Rationale:**
- Remove T01.G1.01 (transitive redundancy)
- Sequencing a safe route involves prediction of outcomes
- Single clear prerequisite

---

#### FIX 3.5: T20.G2.04 - Explain how a change affects the art

**Current Dependencies:**
```
* T01.G1.01: Put pictures in order to plant a seed
* T01.G1.04: Predict the next step in a story sequence
```

**Analysis:**
- T01.G1.04 → T01.G1.01 (transitive coverage)
- T01.G1.01 is redundant
- Also should depend on T20.G2.03 (understanding layered patterns first)

**Proposed Fix:**
```
Dependencies:
* T01.G1.04: Predict the next step in a story sequence
* T20.G2.03: Build layered pattern recipes
```

**Rationale:**
- Remove T01.G1.01 (transitive redundancy)
- Add T20.G2.03 (need to understand patterns before explaining changes to them)
- Logical progression: understand patterns → explain changes to them

---

## SUMMARY OF CHANGES

### By Priority Level

**HIGH PRIORITY (21 skills):**
- Category 1 (Broken References): 4 skills fixed
- Category 2A (T01.GK.07 bridges): 8 skills fixed
- Category 2B (T01.GK.08 bridges): 9 skills fixed

**MEDIUM PRIORITY (9 skills):**
- Category 3 (Transitive Redundancies): 5 skills fixed

**Total Skills to Fix: 30**

---

### By Change Type

1. **Replace incorrect/broken dependency references:** 4 skills
2. **Replace GK with G1 bridge (same topic):** 5 skills
3. **Replace GK with G1 bridge (cross-topic):** 12 skills
4. **Remove transitive redundancies:** 9 skills

---

### Bridge Skills Introduced

**New G1 bridges actively used:**
- T04.G1.03: Find repeated steps in an instruction list (replaces T01.GK.07 in 1 skill)
- T12.G1.02: Give a clear title to a set of steps (replaces T01.GK.05)
- T01.G1.06: Fix a routine with one wrong step (replaces T01.GK.05)
- T23.G1.03: Choose what a sensor can notice (replaces T04.GK.01)
- T25.G1.03: Describe the same fact in words and numbers (replaces T01.GK.08)
- T25.G1.02: Design a picture table (replaces T01.GK.08 in 3 skills)
- T25.G1.01: Record data with tally marks (replaces T01.GK.08)
- T26.G1.01: Run a three-option picture survey (replaces T01.GK.08 in 4 skills)
- T27.G1.01: Build a pictograph from tallies (replaces T01.GK.08)
- T27.G1.03: Tell a one-sentence story with data (replaces T01.GK.08)
- T01.G1.09: Match an algorithm to its goal (new dependency)
- T01.G1.04: Predict the next step in a story sequence (used in 1 new context)

---

## IMPLEMENTATION CHECKLIST

For each fix:
1. [ ] Locate skill in allskills.md
2. [ ] Verify current dependencies match this report
3. [ ] Replace dependency text exactly as specified
4. [ ] Run validation to confirm no broken references
5. [ ] Update any dependent visualization/analysis scripts

---

## VALIDATION QUERIES

After implementing fixes, run these checks:

```bash
# Check for remaining broken references
grep -E "T13.G2.01: Spot what doesn't belong" allskills.md
grep -E "T13.G2.03: Fix the wrong step" allskills.md
grep -E "T20.G2.01: Identify win and lose" allskills.md
grep -E "T23.G2.01: Match a color to a feeling" allskills.md

# Check that G2→GK bridges are reduced
grep -E "T01.GK.07" allskills.md | grep "\.G2\." | wc -l  # Should be 0
grep -E "T01.GK.08" allskills.md | grep "\.G2\." | wc -l  # Should be 0 or minimal
grep -E "T01.GK.05" allskills.md | grep "\.G2\." | wc -l  # Should be 0
grep -E "T04.GK.01" allskills.md | grep "\.G2\." | wc -l  # Should be 0

# Verify new bridge skills are in place
grep -E "T04.G1.03" allskills.md | grep "\.G2\."
grep -E "T12.G1.02" allskills.md | grep "T12.G2.02"
grep -E "T01.G1.06" allskills.md | grep "T13.G2.01"
grep -E "T23.G1.03" allskills.md | grep "T23.G2.01"
```

---

## NOTES & ASSUMPTIONS

1. **Pattern Recognition Bridge:** T04.G1.03 is the proper G1 bridge for T01.GK.07, as it teaches finding repeated steps at the G1 level and depends on T01.GK.07.

2. **Counting Skills:** T01.GK.08 does not have a direct G1 bridge in T01, but various data/analysis topics (T25, T26, T27, T28) have relevant G1 skills for counting and recording data.

3. **Transitive Redundancies:** Only removed dependencies where the transitive path is clear and direct (A→B→C means A→C is redundant).

4. **Cross-Topic Dependencies:** Many data skills (T25-T28) had generic T01 dependencies. Replaced with topic-specific prerequisites that are more pedagogically sound.

5. **Sensor Skills:** T23 had an incorrect pattern dependency. Fixed to use proper sensor progression within T23.

---

## DETAILED FIX LIST FOR IMPLEMENTATION

### Skills Requiring Edits (30 total)

1. T13.G2.03
2. T13.G2.04
3. T20.G2.03
4. T23.G2.02
5. T01.G2.01
6. T01.G2.02
7. T01.G2.08
8. T04.G2.02
9. T04.G2.04
10. T12.G2.02
11. T13.G2.01
12. T23.G2.01
13. T25.G2.02
14. T25.G2.03
15. T25.G2.04
16. T26.G2.02
17. T26.G2.04
18. T27.G2.02
19. T27.G2.04
20. T28.G2.02
21. T28.G2.04
22. T03.G2.02
23. T05.G2.02
24. T14.G2.02
25. T14.G2.04
26. T20.G2.04

---

**END OF FIX PLAN**
