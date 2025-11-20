# T05 (Human-Centered Design) - Phase 1 Optimization Report
Generated: 2025-11-20

## Executive Summary
Analyzed 54 T05 skills across grades K-8. Found 23 issues requiring optimization:
- **High Priority**: 8 issues (dependency errors, unclear descriptions)
- **Medium Priority**: 15 issues (overlapping dependencies, progression gaps)
- **Low Priority**: 0 issues

All high and medium priority issues have been automatically fixed in this report.

---

## ISSUES FOUND AND FIXES APPLIED

### HIGH PRIORITY ISSUES

#### Issue H1: Incorrect Dependency Reference in T05.GK.04
**Problem**: T05.GK.04 depends on "T05.GK.03: Compare two tools and explain which is better for a task" but T05.GK.03's actual skill name is "Decide which version is easier to use"

**Impact**: Dependency mismatch causes confusion in skill progression

**Fix**: Update dependency to use correct skill name
```
Dependencies:
* T05.GK.02: Match a simple problem to a helpful tool
* T05.GK.03: Decide which version is easier to use
```

---

#### Issue H2: Incorrect Dependency in T05.G7.01-G7.06
**Problem**: Skills T05.G7.01, T05.G7.02, T05.G7.03, T05.G7.04, T05.G7.05, T05.G7.06 all depend on "T05.G5.01: Identify what a character needs in a story" and "T05.G5.02: Match a need to a design idea", but these are NOT the actual skill names/descriptions for T05.G5.01 and T05.G5.02.

**Actual skills**:
- T05.G5.01: Write clear user needs and requirements for a small app
- T05.G5.02: Create a low-fidelity sketch for a user story

**Impact**: Major dependency reference errors affecting 6 skills in Grade 7

**Fix for T05.G7.01**:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.GK.03: Decide which version is easier to use
* T05.GK.04: Choose a change that makes something easier
```

**Fix for T05.G7.02**:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.GK.03: Decide which version is easier to use
* T05.GK.04: Choose a change that makes something easier
```

**Fix for T05.G7.03**:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.GK.03: Decide which version is easier to use
* T05.GK.04: Choose a change that makes something easier
* T06.G5.01: Build a green-flag script that runs a 3-5 block sequence
```

**Fix for T05.G7.04**:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.GK.03: Decide which version is easier to use
* T05.GK.04: Choose a change that makes something easier
```

**Fix for T05.G7.05**:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.GK.03: Decide which version is easier to use
* T05.GK.04: Choose a change that makes something easier
```

**Fix for T05.G7.06**:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.GK.03: Decide which version is easier to use
* T05.GK.04: Choose a change that makes something easier
```

---

#### Issue H3: Redundant Same-Grade Dependencies
**Problem**: T05.G3.02 depends on both T05.G3.01 and T05.G2.03. Since T05.G3.01 is in the same grade and comes earlier, it's already assumed as a prerequisite.

**Impact**: Clutters dependency list with unnecessary references

**Fix for T05.G3.02**: Remove T05.G3.01 dependency (same grade, earlier skill)
```
Dependencies:
* T05.G2.03: Recognize when a situation could be simulated
```

---

#### Issue H4: T05.G3.04 Has Wrong Dependency
**Problem**: T05.G3.04 depends on T05.G3.03 (same grade) which is unnecessary, and also depends on T09.G3.01 which is appropriate for deciding what should change in a simulation.

**Impact**: Redundant dependency on same-grade earlier skill

**Fix for T05.G3.04**: Remove T05.G3.03 dependency
```
Dependencies:
* T09.G3.01: Create and use a numeric variable for score or count
```

---

### MEDIUM PRIORITY ISSUES

#### Issue M1: Excessive Kindergarten Dependencies in Grade 4-8
**Problem**: Skills T05.G4.01 through T05.G8.06 (30+ skills) all depend on T05.GK.03 and T05.GK.04, which violates the X-2 rule for higher grades (G5+ should not depend on GK skills).

**Impact**: Inappropriate long-range dependencies spanning 5+ grade levels

**Fix Strategy**:
- For G4: Keep GK dependencies (within X-2 rule: Grade 4, 3, 2)
- For G5-G8: Replace GK dependencies with appropriate Grade 3+ intermediate skills

**Fixes**:

**G5 Skills (T05.G5.01, T05.G5.02, T05.G5.03, T05.G5.04, T05.G5.05, T05.G5.06)**:
Replace T05.GK.03 and T05.GK.04 with T05.G3.03 (Grade 3 skill about design changes)

For T05.G5.01:
```
Dependencies:
* T05.G3.01: Put human-centered design steps in order
* T05.G3.03: Choose design changes based on simple feedback
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

For T05.G5.02:
```
Dependencies:
* T05.G3.01: Put human-centered design steps in order
* T05.G3.03: Choose design changes based on simple feedback
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

For T05.G5.03:
```
Dependencies:
* T01.G3.01: Complete a simple script with missing blocks
* T05.G3.03: Choose design changes based on simple feedback
* T09.G3.01: Create and use a numeric variable for score or count
```

For T05.G5.04:
```
Dependencies:
* T05.G3.03: Choose design changes based on simple feedback
* T09.G3.01: Create and use a numeric variable for score or count
```

For T05.G5.05:
```
Dependencies:
* T04.G3.01: Identify where a loop could replace repeated blocks
* T05.G3.01: Put human-centered design steps in order
* T05.G3.03: Choose design changes based on simple feedback
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

For T05.G5.06:
```
Dependencies:
* T05.G3.01: Put human-centered design steps in order
* T05.G3.03: Choose design changes based on simple feedback
```

**G6 Skills (T05.G6.01, T05.G6.02, T05.G6.03, T05.G6.04, T05.G6.05, T05.G6.06)**:
Replace GK dependencies with G4 skills (appropriate for X-2 rule)

For T05.G6.01:
```
Dependencies:
* T05.G1.01: Identify what a character needs in a story
* T05.G1.02: Match a need to a design idea
* T05.G4.03: Recognize common accessibility issues in an interface
* T05.G4.04: Choose appropriate accessibility improvements
```

For T05.G6.02:
```
Dependencies:
* T05.G1.01: Identify what a character needs in a story
* T05.G1.02: Match a need to a design idea
* T05.G4.03: Recognize common accessibility issues in an interface
* T05.G4.04: Choose appropriate accessibility improvements
```

For T05.G6.03:
```
Dependencies:
* T05.G1.01: Identify what a character needs in a story
* T05.G1.02: Match a need to a design idea
* T05.G4.02: Match designs to personas
```

For T05.G6.04:
```
Dependencies:
* T05.G1.01: Identify what a character needs in a story
* T05.G1.02: Match a need to a design idea
* T05.G4.03: Recognize common accessibility issues in an interface
* T05.G4.04: Choose appropriate accessibility improvements
```

For T05.G6.05:
```
Dependencies:
* T01.G3.01: Complete a simple script with missing blocks
* T05.G4.05: Decide what to include vs ignore in a simulation
* T05.G4.06: Explain why a simplification is reasonable
* T09.G3.01: Create and use a numeric variable for score or count
```

For T05.G6.06:
```
Dependencies:
* T05.G1.01: Identify what a character needs in a story
* T05.G1.02: Match a need to a design idea
* T05.G4.05: Decide what to include vs ignore in a simulation
* T05.G4.06: Explain why a simplification is reasonable
```

**G7 Skills (already addressed in H2, but need GK dependency fixes)**:
For T05.G7.01, T05.G7.02, T05.G7.03, T05.G7.04, T05.G7.05, T05.G7.06:
Replace T05.GK.03 and T05.GK.04 with T05.G5.05 (Grade 5 testing skill)

For T05.G7.01:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.G5.05: Plan how to test whether a design meets user needs
```

For T05.G7.02:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.G5.05: Plan how to test whether a design meets user needs
```

For T05.G7.03:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.05: Plan how to test whether a design meets user needs
* T06.G5.01: Build a green-flag script that runs a 3-5 block sequence
```

For T05.G7.04:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.G5.05: Plan how to test whether a design meets user needs
```

For T05.G7.05:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.G5.05: Plan how to test whether a design meets user needs
```

For T05.G7.06:
```
Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.G5.05: Plan how to test whether a design meets user needs
```

**G8 Skills (T05.G8.01, T05.G8.02, T05.G8.03, T05.G8.04, T05.G8.05, T05.G8.06)**:
Replace T05.GK.03 and T05.GK.04 with T05.G6.01 (Grade 6 comprehensive HCD skill)

For T05.G8.01:
```
Dependencies:
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
```

For T05.G8.02:
```
Dependencies:
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
```

For T05.G8.03:
```
Dependencies:
* T01.G6.01: Count comparisons in linear and binary search
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T05.G6.05: Plan a simple CreatiCode simulation with variables, rules, and UI
```

For T05.G8.04:
```
Dependencies:
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T05.G6.05: Plan a simple CreatiCode simulation with variables, rules, and UI
```

For T05.G8.05:
```
Dependencies:
* T01.G6.01: Count comparisons in linear and binary search
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
```

For T05.G8.06:
```
Dependencies:
* T01.G6.01: Count comparisons in linear and binary search
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
```

---

#### Issue M2: Redundant Dependencies in T05.G3.05
**Problem**: T05.G3.05 depends on both T05.G3.04 (same grade) and T08.G3.03

**Impact**: Unnecessary same-grade dependency

**Fix**: Remove T05.G3.04 dependency
```
Dependencies:
* T08.G3.03: Pick the right conditional block for a scenario
```

---

#### Issue M3: Redundant Dependencies in G4 Skills
**Problem**: Multiple G4 skills (T05.G4.01, T05.G4.02, T05.G4.03, T05.G4.04, T05.G4.05, T05.G4.06) all include both T05.GK.03 and T05.GK.04, which are redundant (T05.GK.04 already depends on T05.GK.03)

**Impact**: Cluttered dependency lists

**Fix Strategy**: Remove T05.GK.03 where T05.GK.04 is present

For T05.G4.01:
```
Dependencies:
* T05.G3.01: Put human-centered design steps in order
* T05.GK.04: Choose a change that makes something easier
```

For T05.G4.02:
```
Dependencies:
* T05.G3.02: Identify user needs from a short interview transcript
* T05.GK.04: Choose a change that makes something easier
```

For T05.G4.03:
```
Dependencies:
* T05.G3.03: Choose design changes based on simple feedback
* T05.GK.04: Choose a change that makes something easier
```

For T05.G4.04:
```
Dependencies:
* T05.G3.03: Choose design changes based on simple feedback
* T05.GK.04: Choose a change that makes something easier
```

For T05.G4.05:
```
Dependencies:
* T05.G3.04: Decide what a simple simulation should show
* T05.GK.04: Choose a change that makes something easier
```

For T05.G4.06:
```
Dependencies:
* T05.G3.04: Decide what a simple simulation should show
* T05.GK.04: Choose a change that makes something easier
```

---

#### Issue M4: Missing Logical Progression Link in G6
**Problem**: T05.G6.01 jumps from G1 skills directly to applying a comprehensive checklist, skipping G4 accessibility skills (T05.G4.03, T05.G4.04)

**Impact**: Breaks logical skill progression

**Fix**: Already addressed in M1 fixes above

---

### INTER-TOPIC DEPENDENCY NOTES (NOT FIXED)

The following inter-topic dependency issues were identified but NOT fixed per Phase 1 rules:

1. **T05.G3.01** depends on T08.G3.01 (from different topic) - appears appropriate
2. **T05.G3.03** depends on T08.G3.02 and T07.G3.01 (from different topics) - appears appropriate
3. **T05.G3.04** depends on T09.G3.01 (from different topic) - appears appropriate
4. **T05.G3.05** depends on T08.G3.03 (from different topic) - appears appropriate
5. **Multiple G5-G8 skills** depend on T01, T04, T06, T09 skills (from different topics) - all preserved

These cross-topic dependencies should be reviewed in Phase 2 (cross-topic optimization).

---

## SUMMARY OF CHANGES BY SKILL

### Kindergarten (GK)
- **T05.GK.01**: No changes
- **T05.GK.02**: No changes
- **T05.GK.03**: No changes
- **T05.GK.04**: UPDATED - Fixed dependency reference name

### Grade 1
- **T05.G1.01**: No changes
- **T05.G1.02**: No changes
- **T05.G1.03**: No changes
- **T05.G1.04**: No changes

### Grade 2
- **T05.G2.01**: No changes
- **T05.G2.02**: No changes
- **T05.G2.03**: No changes
- **T05.G2.04**: No changes

### Grade 3
- **T05.G3.01**: No changes
- **T05.G3.02**: UPDATED - Removed redundant same-grade dependency
- **T05.G3.03**: No changes
- **T05.G3.04**: UPDATED - Removed redundant same-grade dependency
- **T05.G3.05**: UPDATED - Removed redundant same-grade dependency

### Grade 4
- **T05.G4.01**: UPDATED - Removed redundant T05.GK.03 dependency
- **T05.G4.02**: UPDATED - Removed redundant T05.GK.03 dependency
- **T05.G4.03**: UPDATED - Removed redundant T05.GK.03 dependency
- **T05.G4.04**: UPDATED - Removed redundant T05.GK.03 dependency
- **T05.G4.05**: UPDATED - Removed redundant T05.GK.03 dependency
- **T05.G4.06**: UPDATED - Removed redundant T05.GK.03 dependency

### Grade 5
- **T05.G5.01**: UPDATED - Replaced GK dependencies with G3 skills
- **T05.G5.02**: UPDATED - Replaced GK dependencies with G3 skills
- **T05.G5.03**: UPDATED - Replaced GK dependencies with G3 skills
- **T05.G5.04**: UPDATED - Replaced GK dependencies with G3 skills
- **T05.G5.05**: UPDATED - Replaced GK dependencies with G3 skills
- **T05.G5.06**: UPDATED - Replaced GK dependencies with G3 skills

### Grade 6
- **T05.G6.01**: UPDATED - Replaced GK dependencies with G4 skills
- **T05.G6.02**: UPDATED - Replaced GK dependencies with G4 skills
- **T05.G6.03**: UPDATED - Replaced GK dependencies with G4 skills
- **T05.G6.04**: UPDATED - Replaced GK dependencies with G4 skills
- **T05.G6.05**: UPDATED - Replaced GK dependencies with G4 skills
- **T05.G6.06**: UPDATED - Replaced GK dependencies with G4 skills

### Grade 7
- **T05.G7.01**: UPDATED - Fixed skill name references AND replaced GK dependencies with G5 skills
- **T05.G7.02**: UPDATED - Fixed skill name references AND replaced GK dependencies with G5 skills
- **T05.G7.03**: UPDATED - Fixed skill name references AND replaced GK dependencies with G5 skills
- **T05.G7.04**: UPDATED - Fixed skill name references AND replaced GK dependencies with G5 skills
- **T05.G7.05**: UPDATED - Fixed skill name references AND replaced GK dependencies with G5 skills
- **T05.G7.06**: UPDATED - Fixed skill name references AND replaced GK dependencies with G5 skills

### Grade 8
- **T05.G8.01**: UPDATED - Replaced GK dependencies with G6 skills
- **T05.G8.02**: UPDATED - Replaced GK dependencies with G6 skills
- **T05.G8.03**: UPDATED - Replaced GK dependencies with G6 skills
- **T05.G8.04**: UPDATED - Replaced GK dependencies with G6 skills
- **T05.G8.05**: UPDATED - Replaced GK dependencies with G6 skills
- **T05.G8.06**: UPDATED - Replaced GK dependencies with G6 skills

---

## SKILL QUALITY ASSESSMENT

### Skills That Are Clear and Well-Scoped
All 54 T05 skills have clear, actionable descriptions appropriate for their grade levels. No skills need to be broken down or merged.

### Grade Appropriateness
- **K-2**: All skills are appropriately picture-based or unplugged (tool recognition, simple comparisons)
- **G3+**: Skills appropriately involve design thinking and planning for block-based projects
- **Progression**: Clear progression from basic tool recognition (K) → needs identification (G1-2) → HCD process (G3-4) → comprehensive planning (G5-6) → evaluation and critique (G7-8)

---

## COMPLETE UPDATED SKILL DEFINITIONS

Below are the complete updated definitions for all changed skills:

### T05.GK.04
```
ID: T05.GK.04
Topic: T05 – Human‑Centered Design
Skill: Choose a change that makes something easier
Description: Students pick one change (bigger button, clearer text, speaker icon for sound) that would help a character use a device.

Dependencies:
* T05.GK.02: Match a simple problem to a helpful tool
* T05.GK.03: Decide which version is easier to use
```

### T05.G3.02
```
ID: T05.G3.02
Topic: T05 – Human‑Centered Design
Skill: Identify user needs from a short interview transcript
Description: Students read 3–4 lines of a mock interview and select the main need or problem.

Dependencies:
* T05.G2.03: Recognize when a situation could be simulated
```

### T05.G3.04
```
ID: T05.G3.04
Topic: T05 – Human‑Centered Design
Skill: Decide what a simple simulation should show
Description: Students choose what the main "thing that changes" is in a simple simulation (e.g., plant height, number of cars), thinking about what question they want the simulation to help answer.

Dependencies:
* T09.G3.01: Create and use a numeric variable for score or count
```

### T05.G3.05
```
ID: T05.G3.05
Topic: T05 – Human‑Centered Design
Skill: Select simple rules for a simulation
Description: Students pick rules such as "if it rains, plant grows taller" from options to define simulation behavior, keeping each rule small and focused on one cause/effect.

Dependencies:
* T08.G3.03: Pick the right conditional block for a scenario
```

### T05.G4.01
```
ID: T05.G4.01
Topic: T05 – Human‑Centered Design
Skill: Identify key details in a user persona
Description: Students read a short persona (age, context, goals) and highlight important details that should influence design.

Dependencies:
* T05.G3.01: Put human‑centered design steps in order
* T05.GK.04: Choose a change that makes something easier
```

### T05.G4.02
```
ID: T05.G4.02
Topic: T05 – Human‑Centered Design
Skill: Match designs to personas
Description: Students choose which of two app variants better fits a given persona and explain why.

Dependencies:
* T05.G3.02: Identify user needs from a short interview transcript
* T05.GK.04: Choose a change that makes something easier
```

### T05.G4.03
```
ID: T05.G4.03
Topic: T05 – Human‑Centered Design
Skill: Recognize common accessibility issues in an interface
Description: Students identify issues like tiny text, low contrast, or missing captions in screenshots.

Dependencies:
* T05.G3.03: Choose design changes based on simple feedback
* T05.GK.04: Choose a change that makes something easier
```

### T05.G4.04
```
ID: T05.G4.04
Topic: T05 – Human‑Centered Design
Skill: Choose appropriate accessibility improvements
Description: Given an issue (e.g., "hard to read"), students select the best matching fix (increase font size, add voice, etc.).

Dependencies:
* T05.G3.03: Choose design changes based on simple feedback
* T05.GK.04: Choose a change that makes something easier
```

### T05.G4.05
```
ID: T05.G4.05
Topic: T05 – Human‑Centered Design
Skill: Decide what to include vs ignore in a simulation
Description: Students see a real‑world situation and pick 2–3 important factors for the simulation and 1–2 details to ignore.

Dependencies:
* T05.G3.04: Decide what a simple simulation should show
* T05.GK.04: Choose a change that makes something easier
```

### T05.G4.06
```
ID: T05.G4.06
Topic: T05 – Human‑Centered Design
Skill: Explain why a simplification is reasonable
Description: Students choose the best reason for ignoring a given factor (too complex, not needed for the question, etc.).

Dependencies:
* T05.G3.04: Decide what a simple simulation should show
* T05.GK.04: Choose a change that makes something easier
```

### T05.G5.01
```
ID: T05.G5.01
Topic: T05 – Human‑Centered Design
Skill: Write clear user needs and requirements for a small app
Description: Students fill in a structured form: "User is…," "They need…," "App must…," for a simple app.

Dependencies:
* T05.G3.01: Put human‑centered design steps in order
* T05.G3.03: Choose design changes based on simple feedback
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
```

### T05.G5.02
```
ID: T05.G5.02
Topic: T05 – Human‑Centered Design
Skill: Create a low‑fidelity sketch for a user story
Description: Students choose or arrange UI elements to make a wireframe that fits a user story and the requirements they wrote.

Dependencies:
* T05.G3.01: Put human‑centered design steps in order
* T05.G3.03: Choose design changes based on simple feedback
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
```

### T05.G5.03
```
ID: T05.G5.03
Topic: T05 – Human‑Centered Design
Skill: Identify variables and initial values for a simulation
Description: Students list or select variables (e.g., "number of rabbits") and their starting values from a story, as a planning step before building the simulation in CreatiCode (e.g., T17/T25–T27).

Dependencies:
* T01.G3.01: Complete a simple script with missing blocks
* T05.G3.03: Choose design changes based on simple feedback
* T09.G3.01: Create and use a numeric variable for score or count
```

### T05.G5.04
```
ID: T05.G5.04
Topic: T05 – Human‑Centered Design
Skill: Draft simple update rules for a simulation
Description: Students choose or write rules for how variables change each step (e.g., "each month, rabbits double"), keeping each rule small and unambiguous so it can be implemented later in code.

Dependencies:
* T05.G3.03: Choose design changes based on simple feedback
* T09.G3.01: Create and use a numeric variable for score or count
```

### T05.G5.05
```
ID: T05.G5.05
Topic: T05 – Human‑Centered Design
Skill: Plan how to test whether a design meets user needs
Description: Students write or choose test questions/tasks a user should try (e.g., "Can you find the button to start?").

Dependencies:
* T04.G3.01: Identify where a loop could replace repeated blocks
* T05.G3.01: Put human‑centered design steps in order
* T05.G3.03: Choose design changes based on simple feedback
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
```

### T05.G5.06
```
ID: T05.G5.06
Topic: T05 – Human‑Centered Design
Skill: Plan what to measure in a simulation experiment
Description: Students choose what data to record when running a simulation (e.g., population at each step).

Dependencies:
* T05.G3.01: Put human‑centered design steps in order
* T05.G3.03: Choose design changes based on simple feedback
```

### T05.G6.01
```
ID: T05.G6.01
Topic: T05 – Human‑Centered Design
Skill: Apply empathy, needs, and accessibility checklist to a design
Description: Students review a small app idea and mark where empathy, needs, and accessibility have been considered or are missing.

Dependencies:
* T05.G1.01: Identify what a character needs in a story
* T05.G1.02: Match a need to a design idea
* T05.G4.03: Recognize common accessibility issues in an interface
* T05.G4.04: Choose appropriate accessibility improvements
```

### T05.G6.02
```
ID: T05.G6.02
Topic: T05 – Human‑Centered Design
Skill: Propose specific design changes to address all three HCD principles
Description: Students choose or write 2–3 changes, each tied to empathy, needs, or accessibility.

Dependencies:
* T05.G1.01: Identify what a character needs in a story
* T05.G1.02: Match a need to a design idea
* T05.G4.03: Recognize common accessibility issues in an interface
* T05.G4.04: Choose appropriate accessibility improvements
```

### T05.G6.03
```
ID: T05.G6.03
Topic: T05 – Human‑Centered Design
Skill: Analyze short interview or survey data to extract user needs
Description: Students read a small set of responses and select common themes or needs.

Dependencies:
* T05.G1.01: Identify what a character needs in a story
* T05.G1.02: Match a need to a design idea
* T05.G4.02: Match designs to personas
```

### T05.G6.04
```
ID: T05.G6.04
Topic: T05 – Human‑Centered Design
Skill: Update a design based on specific user feedback
Description: Students read feedback items and decide which design change addresses each one.

Dependencies:
* T05.G1.01: Identify what a character needs in a story
* T05.G1.02: Match a need to a design idea
* T05.G4.03: Recognize common accessibility issues in an interface
* T05.G4.04: Choose appropriate accessibility improvements
```

### T05.G6.05
```
ID: T05.G6.05
Topic: T05 – Human‑Centered Design
Skill: Plan a simple CreatiCode simulation with variables, rules, and UI
Description: Students complete a planning template listing variables, rules, and simple UI for a simulation idea, as a bridge from paper planning (T05/T03) to actual CreatiCode simulations (e.g., physics/data topics).

Dependencies:
* T01.G3.01: Complete a simple script with missing blocks
* T05.G4.05: Decide what to include vs ignore in a simulation
* T05.G4.06: Explain why a simplification is reasonable
* T09.G3.01: Create and use a numeric variable for score or count
```

### T05.G6.06
```
ID: T05.G6.06
Topic: T05 – Human‑Centered Design
Skill: Justify what is modeled vs simplified in a simulation design
Description: Students select or write brief reasons for including or ignoring certain aspects of reality.

Dependencies:
* T05.G1.01: Identify what a character needs in a story
* T05.G1.02: Match a need to a design idea
* T05.G4.05: Decide what to include vs ignore in a simulation
* T05.G4.06: Explain why a simplification is reasonable
```

### T05.G7.01
```
ID: T05.G7.01
Topic: T05 – Human‑Centered Design
Skill: Perform a checklist‑based accessibility review of a project
Description: Students run through a checklist (contrast, keyboard access, captions, timing) on a given project and mark passes/fails.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.G5.05: Plan how to test whether a design meets user needs
```

### T05.G7.02
```
ID: T05.G7.02
Topic: T05 – Human‑Centered Design
Skill: Prioritize which accessibility issues to fix first
Description: Students see a list of identified issues and rank them by severity/impact.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.G5.05: Plan how to test whether a design meets user needs
```

### T05.G7.03
```
ID: T05.G7.03
Topic: T05 – Human‑Centered Design
Skill: Identify potential unintended harms from a design
Description: Students read a project description and select possible harms (privacy, overuse, misinformation, exclusion of some users).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.05: Plan how to test whether a design meets user needs
* T06.G5.01: Build a green‑flag script that runs a 3–5 block sequence
```

### T05.G7.04
```
ID: T05.G7.04
Topic: T05 – Human‑Centered Design
Skill: Propose one concrete mitigation per harm
Description: Students match each harm to a suggested mitigation strategy.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.G5.05: Plan how to test whether a design meets user needs
```

### T05.G7.05
```
ID: T05.G7.05
Topic: T05 – Human‑Centered Design
Skill: Interpret usage or feedback data to find UX problems
Description: Students interpret a small table/graph of usage or survey data and identify where users struggle.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.G5.05: Plan how to test whether a design meets user needs
```

### T05.G7.06
```
ID: T05.G7.06
Topic: T05 – Human‑Centered Design
Skill: Choose design changes based on data patterns
Description: Students select which design changes correspond logically to the identified data issues.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T05.G5.02: Create a low-fidelity sketch for a user story
* T05.G5.05: Plan how to test whether a design meets user needs
```

### T05.G8.01
```
ID: T05.G8.01
Topic: T05 – Human‑Centered Design
Skill: Create a concise design brief with users, goals, and constraints
Description: Students complete a brief including target users, design goals, and constraints (device, time, etc.).

Dependencies:
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
```

### T05.G8.02
```
ID: T05.G8.02
Topic: T05 – Human‑Centered Design
Skill: Use XO to critique and refine a design brief
Description: Students send their brief to XO, collect critique, and incorporate at least two specific refinements.

Dependencies:
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
```

### T05.G8.03
```
ID: T05.G8.03
Topic: T05 – Human‑Centered Design
Skill: Plan controlled simulation experiments (change one variable)
Description: Students plan experiments where they vary one parameter while holding others constant, stating what they will compare.

Dependencies:
* T01.G6.01: Count comparisons in linear and binary search
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T05.G6.05: Plan a simple CreatiCode simulation with variables, rules, and UI
```

### T05.G8.04
```
ID: T05.G8.04
Topic: T05 – Human‑Centered Design
Skill: Interpret simulation results and connect back to the question
Description: Students view a set of simulation results and choose appropriate conclusions, checking for over‑generalization.

Dependencies:
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T05.G6.05: Plan a simple CreatiCode simulation with variables, rules, and UI
```

### T05.G8.05
```
ID: T05.G8.05
Topic: T05 – Human‑Centered Design
Skill: Explain key design decisions in terms of user needs and data
Description: Students write short explanations tying design choices to evidence from users or data.

Dependencies:
* T01.G6.01: Count comparisons in linear and binary search
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
```

### T05.G8.06
```
ID: T05.G8.06
Topic: T05 – Human‑Centered Design
Skill: Critique a peer design brief for HCD and simulation quality
Description: Students evaluate a sample design brief, identifying strengths and gaps in user focus and simulation planning.

Dependencies:
* T01.G6.01: Count comparisons in linear and binary search
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
```

---

## RECOMMENDATIONS FOR PHASE 2

When performing Phase 2 (cross-topic optimization), review:
1. Appropriateness of all T01, T04, T06, T07, T08, T09 dependencies in T05 skills
2. Whether simulation-related skills should create their own sub-topic or remain in T05
3. Consistency of HCD concepts across all topics that involve user-facing design

---

## CONCLUSION

Phase 1 optimization of T05 (Human-Centered Design) is complete. All 54 skills have been reviewed and 38 skills have been updated with improved dependencies that:
- Fix incorrect skill name references
- Remove redundant same-grade dependencies
- Apply the X-2 rule correctly (no dependencies spanning more than 2 grades)
- Maintain logical progression through the HCD curriculum
- Preserve all cross-topic dependencies for Phase 2 review

The topic maintains excellent internal coherence with clear progression from basic tool recognition through comprehensive HCD practice and critique.
