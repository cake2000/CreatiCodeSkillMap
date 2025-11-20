# G2 Dependency Chains - Before & After Visual

This document shows the dependency chain improvements for key G2 skills, illustrating how the fixes create cleaner, more logical learning progressions.

---

## 1. BROKEN REFERENCE FIXES

### Fix 1.1: T13.G2.03 (Debugging Repeat Counts)

**BEFORE (BROKEN):**
```
T13.G2.03: Fix repeated steps (wrong count)
    └─ T13.G2.01: "Spot what doesn't belong in a pattern" ❌ DOES NOT EXIST
```

**AFTER (FIXED):**
```
T13.G2.03: Fix repeated steps (wrong count)
    ├─ T04.G2.01: Identify the repeating unit
    │   └─ T04.G1.03: Find repeated steps in instruction list
    │       └─ T01.GK.07: Find the pattern that repeats
    │
    └─ T01.G2.01: Find actions that repeat in everyday tasks
        └─ T04.G1.03: Find repeated steps in instruction list
            └─ T01.GK.07: Find the pattern that repeats
```

**Improvement:**
- Fixes broken reference
- Creates logical progression: recognize patterns → identify units → fix counts
- Both dependencies converge on pattern recognition foundation

---

### Fix 1.2: T13.G2.04 (Adding Verification Checks)

**BEFORE (BROKEN):**
```
T13.G2.04: Add a check to see if steps worked
    ├─ T13.G2.03: "Fix the wrong step in simple task" ❌ DOES NOT EXIST
    └─ T03.G1.03: List steps for classroom routine ✓
```

**AFTER (FIXED):**
```
T13.G2.04: Add a check to see if steps worked
    ├─ T03.G1.03: List steps for classroom routine
    │   └─ T03.GK.03: Order 3-4 pictures in routine
    │
    └─ T01.G1.09: Match algorithm to its goal ← NEW
        └─ T01.G1.01: Put pictures in order to plant a seed
            └─ T01.GK.02: Put pictures in order for class
```

**Improvement:**
- Fixes broken reference
- Adds goal-understanding prerequisite (essential for knowing *what* to check)
- Logical progression: understand algorithms → understand goals → add verification

---

### Fix 1.3: T20.G2.03 (Layered Pattern Recipes)

**BEFORE (BROKEN):**
```
T20.G2.03: Build layered pattern recipes
    └─ T20.G2.01: "Identify win and lose in simple game" ❌ DOES NOT EXIST
```

**AFTER (FIXED):**
```
T20.G2.03: Build layered pattern recipes (2-layer: "repeat A 3×, then B 1×")
    ├─ T20.G2.01: Use repeat cards in art recipe (single-layer)
    │   └─ T01.G1.04: Predict next step in story sequence
    │
    └─ T01.G2.02: Use "repeat" to make directions shorter
        └─ T01.G2.01: Find actions that repeat
            └─ T04.G1.03: Find repeated steps
                └─ T01.GK.07: Find pattern that repeats
```

**Improvement:**
- Fixes broken reference
- Creates natural artistic pattern progression: simple repeat → single-layer → multi-layer
- Adds foundational understanding of "repeat" notation

---

### Fix 1.4: T23.G2.02 (Sensor Limitations)

**BEFORE (BROKEN):**
```
T23.G2.02: Spot when sensor data might be unclear
    └─ T23.G2.01: "Match color to feeling" ❌ DOES NOT EXIST
```

**AFTER (FIXED):**
```
T23.G2.02: Spot when sensor data might be unclear
    └─ T23.G2.01: Pick the right sensor for a job
        └─ T23.G1.03: Choose what a sensor can notice
            └─ T23.G1.02: Match sensors to human senses
                └─ T23.G1.01: Find sensors on everyday devices
```

**Improvement:**
- Fixes broken reference (now correct skill name)
- Clean progression: identify sensors → match to senses → understand capabilities → choose sensors → understand limitations

---

## 2. G2→GK BRIDGE IMPROVEMENTS (Pattern Recognition)

### Fix 2A.1: T01.G2.01 (Find Repeating Actions)

**BEFORE (POOR BRIDGES):**
```
T01.G2.01: Find actions that repeat in everyday tasks
    ├─ T01.G1.10: Match pictures to "if/then" rules ❌ UNRELATED (if/then ≠ patterns)
    └─ T01.GK.07: Find pattern that repeats ⚠️ SKIPS G1
```

**AFTER (CLEAN BRIDGE):**
```
T01.G2.01: Find actions that repeat in everyday tasks
    └─ T04.G1.03: Find repeated steps in instruction list ← G1 BRIDGE
        └─ T01.GK.07: Find pattern that repeats
```

**Improvement:**
- Removes irrelevant if/then dependency
- Adds proper G1 bridge (T04.G1.03)
- Clean GK → G1 → G2 progression
- Single clear path instead of two confusing paths

---

### Fix 2A.6: T12.G2.02 (Fix Confusing Labels)

**BEFORE (WRONG TOPIC):**
```
T12.G2.02: Fix confusing labels on a plan
    └─ T01.GK.05: Move picture to wrong place ⚠️ WRONG TOPIC (sequencing ≠ labeling)
        └─ T01.GK.03: Find first and last pictures
```

**AFTER (CORRECT TOPIC):**
```
T12.G2.02: Fix confusing labels on a plan
    └─ T12.G1.02: Give a clear title to a set of steps ← G1 BRIDGE, SAME TOPIC
        └─ T12.G1.01: Find the main set of instructions
```

**Improvement:**
- Stays within T12 (Organizing Programs) topic
- Proper G1 bridge for labeling skills
- Logical progression: create good labels (G1) → fix bad labels (G2)

---

### Fix 2A.7: T13.G2.01 (Fix Wrong Signals)

**BEFORE (WRONG TOPIC):**
```
T13.G2.01: Fix steps that use wrong signal
    └─ T01.GK.05: Move picture to wrong place ⚠️ WRONG TOPIC (sequencing ≠ debugging)
        └─ T01.GK.03: Find first and last pictures
```

**AFTER (CORRECT TOPIC):**
```
T13.G2.01: Fix steps that use wrong signal
    └─ T01.G1.06: Fix a routine with one wrong step ← G1 BRIDGE FOR DEBUGGING
        └─ T01.GK.05: Move picture to wrong place
            └─ T01.GK.03: Find first and last pictures
```

**Improvement:**
- Adds debugging-specific G1 bridge
- Maintains sequencing foundation transitively
- Progression: fix sequencing (GK) → fix wrong steps (G1) → fix wrong signals (G2)

---

### Fix 2A.8: T23.G2.01 (Pick Right Sensor)

**BEFORE (COMPLETELY WRONG):**
```
T23.G2.01: Pick the right sensor for a job
    └─ T04.GK.01: Spot a simple repeating pattern ❌ TOTALLY UNRELATED
```

**AFTER (CORRECT TOPIC):**
```
T23.G2.01: Pick the right sensor for a job
    └─ T23.G1.03: Choose what a sensor can notice ← G1 BRIDGE, SAME TOPIC
        └─ T23.G1.02: Match sensors to human senses
            └─ T23.G1.01: Find sensors on everyday devices
```

**Improvement:**
- Completely replaces unrelated pattern dependency
- Creates clean sensor skill progression within T23 topic
- Logical: identify sensors → match to senses → understand capabilities → choose right one

---

## 3. G2→GK.08 BRIDGE IMPROVEMENTS (Data Skills)

### Fix 2B.1: T25.G2.02 (Translate Between Representations)

**BEFORE (WEAK BRIDGE):**
```
T25.G2.02: Translate between timeline, table, and sentence
    ├─ T01.G1.01: Put pictures in order ⚠️ TOO GENERIC
    └─ T01.GK.08: Count how many times ⚠️ WRONG TOPIC, SKIPS G1
        └─ T01.GK.07: Find pattern that repeats
```

**AFTER (STRONG BRIDGE):**
```
T25.G2.02: Translate between timeline, table, and sentence
    ├─ T01.G1.01: Put pictures in order (sequencing foundation)
    └─ T25.G1.03: Describe same fact in words and numbers ← G1 BRIDGE, SAME TOPIC
        └─ T25.G1.02: Design a picture table
```

**Improvement:**
- Replaces cross-topic counting with same-topic representation skill
- Perfect G1 bridge: multi-format description → multi-format translation
- Stays within T25 (Data Representation) topic

---

### Fix 2B.3: T25.G2.04 (Combine Two Attributes)

**BEFORE (UNRELATED DEPENDENCIES):**
```
T25.G2.04: Combine two data attributes (e.g., animal + habitat)
    ├─ T01.G1.01: Put pictures in order ❌ UNRELATED (sequencing ≠ data pairing)
    └─ T01.GK.08: Count how many times ❌ UNRELATED (counting ≠ combining)
        └─ T01.GK.07: Find pattern that repeats
```

**AFTER (DIRECT, RELEVANT):**
```
T25.G2.04: Combine two data attributes
    └─ T25.G1.02: Design a picture table ← PERFECT G1 BRIDGE
        └─ (foundational table understanding)
```

**Improvement:**
- Removes two unrelated T01 dependencies
- Single, highly relevant prerequisite
- Direct progression: structured tables → multi-attribute records

---

### Fix 2B.4: T26.G2.02 (Two-Column Record Sheet)

**BEFORE (CROSS-TOPIC DEPENDENCIES):**
```
T26.G2.02: Build a two-column record sheet
    ├─ T01.G1.01: Put pictures in order ❌ UNRELATED
    └─ T01.GK.08: Count how many times ❌ WRONG TOPIC
        └─ T01.GK.07: Find pattern that repeats
```

**AFTER (TOPIC-CONSISTENT):**
```
T26.G2.02: Build a two-column record sheet
    ├─ T26.G1.01: Run a three-option picture survey ← G1 DATA COLLECTION
    │   └─ T26.GK.01: Choose a three-option question
    │
    └─ T25.G1.02: Design a picture table ← G1 TABLE STRUCTURE
```

**Improvement:**
- Combines data collection (T26) + table structure (T25)
- Both prerequisites are relevant and properly bridged
- Progression: collect data + structure → record sheet

---

### Fix 2B.7: T27.G2.04 (Data Answers Question?)

**BEFORE (UNRELATED LOGIC):**
```
T27.G2.04: Decide if data answers the question asked
    ├─ T01.G1.10: Match pictures to "if/then" rules ❌ UNRELATED (logic ≠ data analysis)
    └─ T01.GK.08: Count how many times ❌ TOO NARROW
        └─ T01.GK.07: Find pattern that repeats
```

**AFTER (DATA INTERPRETATION):**
```
T27.G2.04: Decide if data answers the question asked
    ├─ T27.G1.03: Tell a one-sentence story with data ← G1 INTERPRETATION
    │   └─ T27.G1.02: Answer "how many more?" questions
    │       └─ T27.G1.01: Build pictograph from tallies
    │
    └─ T27.G2.02: Interpret simple line plots ← G2 ANALYSIS
        └─ T01.G1.01: Put pictures in order
        └─ T27.G1.01: Build pictograph from tallies
```

**Improvement:**
- Removes unrelated if/then logic dependency
- Creates natural data analysis progression
- Learn to interpret data → evaluate if it answers questions

---

### Fix 2B.8 & 2B.9: T28 Chance Experiments

**BEFORE (GENERIC SEQUENCING + COUNTING):**
```
T28.G2.02: Conduct chance experiment
    ├─ T01.G1.01: Put pictures in order ❌ TOO GENERIC
    └─ T01.GK.08: Count how many times ⚠️ PARTIALLY RELEVANT

T28.G2.04: Predict and observe outcomes
    ├─ T01.G1.01: Put pictures in order ❌ UNRELATED
    └─ T01.GK.08: Count how many times ⚠️ PARTIALLY RELEVANT
```

**AFTER (EXPERIMENT METHODOLOGY + PREDICTION):**
```
T28.G2.02: Conduct chance experiment
    ├─ T26.G1.01: Run a three-option survey ← DATA COLLECTION METHOD
    └─ T25.G1.01: Record data with tally marks ← RECORDING METHOD

T28.G2.04: Predict and observe outcomes
    ├─ T28.G2.02: Conduct chance experiment ← EXPERIMENT SKILLS
    └─ T01.G1.04: Predict next step in sequence ← PREDICTION SKILLS
```

**Improvement:**
- T28.G2.02: Gets proper data collection + recording prerequisites
- T28.G2.04: Combines experimentation + prediction skills
- Clean progression: collect data → conduct experiments → predict outcomes

---

## 4. TRANSITIVE REDUNDANCY REMOVALS

### Fix 3.1: T03.G2.02 (Group Subtasks)

**BEFORE (REDUNDANT):**
```
T03.G2.02: Group similar subtasks together
    ├─ T03.G2.01: Choose subtasks for project idea
    │   └─ T03.G1.03: List steps for classroom routine ← COVERED HERE
    │
    └─ T03.G1.03: List steps for classroom routine ⚠️ REDUNDANT
        └─ T03.GK.03: Order 3-4 pictures
```

**AFTER (CLEAN):**
```
T03.G2.02: Group similar subtasks together
    └─ T03.G2.01: Choose subtasks for project idea
        └─ T03.G1.03: List steps for classroom routine ← INCLUDED TRANSITIVELY
            └─ T03.GK.03: Order 3-4 pictures
```

**Improvement:**
- Removes direct dependency on T03.G1.03
- Maintains transitive coverage through T03.G2.01
- Cleaner single-path progression

---

### Fix 3.3 & 3.4: T14 Game Skills

**BEFORE (REDUNDANT):**
```
T14.G2.02 & T14.G2.04
    ├─ T01.G1.01: Put pictures in order ⚠️ REDUNDANT
    │   └─ T01.GK.02: Put pictures in order for class
    │
    └─ T01.G1.04: Predict next step in sequence
        └─ T01.G1.01: Put pictures in order ← COVERED HERE
            └─ T01.GK.02: Put pictures in order for class
```

**AFTER (CLEAN):**
```
T14.G2.02: Track lives and game over conditions
    └─ T01.G1.04: Predict next step in sequence
        └─ T01.G1.01: Put pictures in order ← INCLUDED TRANSITIVELY

T14.G2.04: Sequence a safe route
    └─ T01.G1.04: Predict next step in sequence
        └─ T01.G1.01: Put pictures in order ← INCLUDED TRANSITIVELY
```

**Improvement:**
- Removes redundant T01.G1.01 dependencies
- Maintains sequencing foundation transitively
- Emphasizes prediction as the more relevant skill

---

## SUMMARY OF IMPROVEMENTS

### Pattern Skills (T01, T04)
- **Before:** Multiple G2 skills jumped directly to T01.GK.07, or had unrelated dependencies
- **After:** Clean GK → G1 (T04.G1.03) → G2 progression with transitive coverage

### Organization Skills (T12, T13)
- **Before:** Cross-topic dependencies on generic sequencing
- **After:** Topic-specific G1 bridges (labeling, debugging)

### Sensor Skills (T23)
- **Before:** Completely unrelated pattern dependency + broken references
- **After:** Clean sensor-specific progression within T23

### Data Skills (T25-T28)
- **Before:** Generic T01 sequencing/counting dependencies across all data topics
- **After:** Topic-specific G1 bridges:
  - T25: Multi-format representation
  - T26: Data collection methodology
  - T27: Data interpretation
  - T28: Experiment methodology + prediction

### Overall Structure
- **Eliminated:** 17 cross-topic GK dependencies
- **Added:** 12 topic-appropriate G1 bridges
- **Removed:** 9 transitive redundancies
- **Fixed:** 4 broken/incorrect references

**Result:** Cleaner, more logical, topic-consistent learning progressions throughout G2.

---

**END OF VISUAL GUIDE**
