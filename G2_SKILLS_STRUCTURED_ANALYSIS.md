# Grade 2 (G2) Skills - Structured Analysis Report

## Executive Summary

**Total G2 Skills Analyzed:** 88 skills across 18 topics
**Skills with Dependency Issues:** 43 (49%)

### Issue Categories:
- **CRITICAL - Invalid Grade Dependencies (G3+):** 0 skills
- **WARNING - Skip G1 Bridge (G2→GK):** 17 skills
- **CRITICAL - Circular Dependencies:** 0 skills
- **INFO - Transitive Redundancy:** 9 skills
- **INFO - Same Topic/Grade Dependencies:** 26 skills

---

## G2 Skills Organized by Topic

### T01 – Everyday Algorithms (14 skills)

#### T01.G2.01: Find actions that repeat in everyday tasks
- **Dependencies:** T01.G1.10, T01.GK.07
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.07) - may skip G1 bridge

#### T01.G2.02: Use "repeat" to make directions shorter
- **Dependencies:** T01.G2.01, T01.GK.07
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.07) - may skip G1 bridge
  - 📝 Transitive redundancy: T01.GK.07 (already via T01.G2.01)
  - 📝 Depends on earlier same-topic/grade: T01.G2.01

#### T01.G2.03: Replace repeated steps with a repeat instruction
- **Dependencies:** T01.G2.02
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T01.G2.02

#### T01.G2.04: Match if/then rules to pictures
- **Dependencies:** T01.G1.10
- **Issues:** None

#### T01.G2.05: Complete a simple if/then algorithm
- **Dependencies:** T01.G2.04
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T01.G2.04

#### T01.G2.06: Choose the best if/then rule for a situation
- **Dependencies:** T01.G2.05
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T01.G2.05

#### T01.G2.07: Trace an algorithm that uses an if/then choice
- **Dependencies:** T01.G2.06
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T01.G2.06

#### T01.G2.08: Trace an algorithm that uses "repeat ___ times"
- **Dependencies:** T01.G2.03, T01.GK.07
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.07) - may skip G1 bridge
  - 📝 Transitive redundancy: T01.GK.07 (already via T01.G2.03)
  - 📝 Depends on earlier same-topic/grade: T01.G2.03

#### T01.G2.09: Fix a wrong repeat count in an algorithm
- **Dependencies:** T01.G2.08
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T01.G2.08

#### T01.G2.10: Fix a wrong or missing if/then branch
- **Dependencies:** T01.G2.07, T01.G1.06
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T01.G2.07

#### T01.G2.11: Trace maze directions on a simple grid
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T01.G2.12: Choose directions that reach the goal
- **Dependencies:** T01.G2.11
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T01.G2.11

#### T01.G2.13: Write directions to navigate a simple grid
- **Dependencies:** T01.G2.12
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T01.G2.12

#### T01.G2.14: Fix maze directions that miss the goal
- **Dependencies:** T01.G2.13
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T01.G2.13

---

### T02 – Algorithm Diagrams (6 skills)

#### T02.G2.01: Turn a picture routine into labeled boxes
- **Dependencies:** T02.G1.01
- **Issues:** None

#### T02.G2.02: Read a box diagram and choose the matching pictures
- **Dependencies:** T02.G2.01
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T02.G2.01

#### T02.G2.03: Trace a simple left‑to‑right instruction sequence
- **Dependencies:** T02.G2.02
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T02.G2.02

#### T02.G2.04: Reveal one instruction at a time and mark intermediate states
- **Dependencies:** T02.G2.03
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T02.G2.03

#### T02.G2.05: Match a box diagram to a step sequence
- **Dependencies:** T02.G2.02, T01.G1.01
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T02.G2.02

#### T02.G2.06: Fix a sequencing error in a step sequence
- **Dependencies:** T02.G2.05
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T02.G2.05

---

### T03 – Problem Decomposition (4 skills)

#### T03.G2.01: Choose subtasks for a simple project idea
- **Dependencies:** T03.G1.03
- **Issues:** None

#### T03.G2.02: Group similar subtasks together
- **Dependencies:** T03.G2.01, T03.G1.03
- **Issues:**
  - 📝 Transitive redundancy: T03.G1.03 (already via T03.G2.01)
  - 📝 Depends on earlier same-topic/grade: T03.G2.01

#### T03.G2.03: Arrange subtasks into a reasonable order
- **Dependencies:** T03.G2.02
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T03.G2.02

#### T03.G2.04: Use a checklist to track progress on a mini‑project
- **Dependencies:** T03.G2.03
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T03.G2.03

---

### T04 – Algorithm Patterns (4 skills)

#### T04.G2.01: Identify the repeating unit in a longer pattern
- **Dependencies:** T04.G1.03
- **Issues:** None

#### T04.G2.02: Spot repeated step sequences in everyday algorithms
- **Dependencies:** T04.G2.01, T01.GK.07
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.07) - may skip G1 bridge
  - 📝 Transitive redundancy: T01.GK.07 (already via T04.G2.01)
  - 📝 Depends on earlier same-topic/grade: T04.G2.01

#### T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
- **Dependencies:** T01.G2.02
- **Issues:** None

#### T04.G2.04: Replace repeated steps with a "repeat ___ times" phrase
- **Dependencies:** T04.G2.03, T01.GK.07
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.07) - may skip G1 bridge
  - 📝 Transitive redundancy: T01.GK.07 (already via T04.G2.03)
  - 📝 Depends on earlier same-topic/grade: T04.G2.03

---

### T05 – Human‑Centered Design (4 skills)

#### T05.G2.01: Match different users to different preferred designs
- **Dependencies:** T05.G1.03
- **Issues:** None

#### T05.G2.02: Identify features that make a design more accessible
- **Dependencies:** T05.G1.04, T05.G1.01
- **Issues:**
  - 📝 Transitive redundancy: T05.G1.01 (already via T05.G1.04)

#### T05.G2.03: Recognize when a situation could be simulated
- **Dependencies:** T05.G1.01
- **Issues:** None

#### T05.G2.04: Choose what to include in a very simple simulation
- **Dependencies:** T05.G2.03
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T05.G2.03

---

### T12 – Organizing Programs (4 skills)

#### T12.G2.01: Add a note to explain a section of a plan
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T12.G2.02: Fix confusing labels on a plan
- **Dependencies:** T01.GK.05
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.05) - may skip G1 bridge

#### T12.G2.03: Use the same style for section titles
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T12.G2.04: Group related steps under a heading
- **Dependencies:** T03.G1.02, T03.G1.03
- **Issues:** None

---

### T13 – Testing, Debugging & Error Handling (4 skills)

#### T13.G2.01: Fix steps that use the wrong signal
- **Dependencies:** T01.GK.05
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.05) - may skip G1 bridge

#### T13.G2.02: Trace a set of steps and predict behavior
- **Dependencies:** T01.G1.05, T03.G1.03
- **Issues:** None

#### T13.G2.03: Fix a repeated step that happens too many or too few times
- **Dependencies:** T13.G2.01
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T13.G2.01

#### T13.G2.04: Add a simple check to see if steps worked
- **Dependencies:** T13.G2.03, T03.G1.03
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T13.G2.03

---

### T14 – 2D Games (5 skills)

#### T14.G2.01: Understand turns and rounds
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T14.G2.02: Track lives and game over conditions
- **Dependencies:** T01.G1.01, T01.G1.04
- **Issues:**
  - 📝 Transitive redundancy: T01.G1.01 (already via T01.G1.04)

#### T14.G2.03: Recognize level progression
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T14.G2.04: Sequence a safe route
- **Dependencies:** T01.G1.01, T01.G1.04
- **Issues:**
  - 📝 Transitive redundancy: T01.G1.01 (already via T01.G1.04)

#### T14.G2.05: Adjust difficulty knobs
- **Dependencies:** T01.G1.10
- **Issues:** None

---

### T15 – Stories & Animation (3 skills)

#### T15.G2.01: Fast vs. Slow animation
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T15.G2.02: Identify scene transitions
- **Dependencies:** T01.G1.10, T01.G1.04
- **Issues:** None

#### T15.G2.03: Loop patterns in animation
- **Dependencies:** T01.G1.07
- **Issues:** None

---

### T20 – Algorithmic Art & Creative Coding (4 skills)

#### T20.G2.01: Use repeat cards in an art recipe
- **Dependencies:** T01.G1.04
- **Issues:** None

#### T20.G2.02: Plan mirrored mosaics
- **Dependencies:** T05.G1.01, T01.G1.04
- **Issues:** None

#### T20.G2.03: Build layered pattern recipes
- **Dependencies:** T20.G2.01
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T20.G2.01

#### T20.G2.04: Explain how a change affects the art
- **Dependencies:** T01.G1.01, T01.G1.04
- **Issues:**
  - 📝 Transitive redundancy: T01.G1.01 (already via T01.G1.04)

---

### T23 – AI Perception (3 skills)

#### T23.G2.01: Pick the right sensor for a job
- **Dependencies:** T04.GK.01
- **Issues:**
  - ⚠️ Depends on K skill (T04.GK.01) - may skip G1 bridge

#### T23.G2.02: Spot when sensor data might be unclear
- **Dependencies:** T23.G2.01
- **Issues:**
  - 📝 Depends on earlier same-topic/grade: T23.G2.01

#### T23.G2.03: Notice that devices sometimes "guess"
- **Dependencies:** T01.G1.01
- **Issues:** None

---

### T25 – Data Representation (4 skills)

#### T25.G2.01: Choose labels for a category chart
- **Dependencies:** T01.G1.10
- **Issues:** None

#### T25.G2.02: Translate between timeline, table, and sentence
- **Dependencies:** T01.G1.01, T01.GK.08
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.08) - may skip G1 bridge

#### T25.G2.03: Pick the best representation for a question
- **Dependencies:** T01.GK.08
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.08) - may skip G1 bridge

#### T25.G2.04: Combine two data attributes
- **Dependencies:** T01.G1.01, T01.GK.08
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.08) - may skip G1 bridge

---

### T26 – Data Collection & Logging (4 skills)

#### T26.G2.01: Distinguish observational vs survey data
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T26.G2.02: Build a two-column record sheet
- **Dependencies:** T01.G1.01, T01.GK.08
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.08) - may skip G1 bridge

#### T26.G2.03: Use timers to collect duration data
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T26.G2.04: Explain why sample size matters
- **Dependencies:** T01.G1.01, T01.GK.08
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.08) - may skip G1 bridge

---

### T27 – Data Analysis & Storytelling (4 skills)

#### T27.G2.01: Create bar charts with axes labels
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T27.G2.02: Interpret simple line plots
- **Dependencies:** T01.G1.01, T01.GK.08
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.08) - may skip G1 bridge

#### T27.G2.03: Identify outliers in small data sets
- **Dependencies:** T01.G1.10
- **Issues:** None

#### T27.G2.04: Decide if data answers the question asked
- **Dependencies:** T01.G1.10, T01.GK.08
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.08) - may skip G1 bridge

---

### T28 – Chance & Simulations (4 skills)

#### T28.G2.01: Sort events into certain / possible / impossible
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T28.G2.02: Conduct a picture-based chance experiment
- **Dependencies:** T01.G1.01, T01.GK.08
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.08) - may skip G1 bridge

#### T28.G2.03: Decide if a simple game is fair
- **Dependencies:** T01.G1.10
- **Issues:** None

#### T28.G2.04: Predict and observe outcomes
- **Dependencies:** T01.G1.01, T01.GK.08
- **Issues:**
  - ⚠️ Depends on K skill (T01.GK.08) - may skip G1 bridge

---

### T30 – Devices & Hardware Systems (4 skills)

#### T30.G2.01: Explain core internal components
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T30.G2.02: Trace input → process → output
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T30.G2.03: Compare wired vs wireless connections
- **Dependencies:** T01.G1.07
- **Issues:** None

#### T30.G2.04: Share best practices for caring for devices
- **Dependencies:** T01.G1.01
- **Issues:** None

---

### T32 – Cybersecurity & Digital Safety (4 skills)

#### T32.G2.01: Create a strong password recipe
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T32.G2.02: Practice logging off shared devices
- **Dependencies:** T01.G1.01, T03.G1.03
- **Issues:** None

#### T32.G2.03: Recognize safe digital citizenship behaviors
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T32.G2.04: Describe basic device care for security
- **Dependencies:** T01.G1.01, T03.G1.03
- **Issues:** None

---

### T34 – Computing History (3 skills)

#### T34.G2.01: Build "then vs now" comparison charts
- **Dependencies:** T01.G1.01
- **Issues:** None

#### T34.G2.02: Identify communities impacted by inventions
- **Dependencies:** T01.G1.10, T03.G1.03
- **Issues:** None

#### T34.G2.03: Create mini-biographies of computing helpers
- **Dependencies:** T01.G1.01
- **Issues:** None

---

### T35 – Impacts & Ethics (3 skills)

#### T35.G2.01: Compare benefits and harms of a tech tool
- **Dependencies:** T01.G1.07
- **Issues:** None

#### T35.G2.02: Plan balanced tech schedules
- **Dependencies:** T01.G1.01, T03.G1.03
- **Issues:** None

#### T35.G2.03: Practice online kindness scripts
- **Dependencies:** T01.G1.01
- **Issues:** None

---

### T36 – Careers, Collaboration & Future Paths (3 skills)

#### T36.G2.01: Identify project roles in simple terms
- **Dependencies:** T01.G1.10
- **Issues:** None

#### T36.G2.02: Plan balanced daily routines
- **Dependencies:** T01.G1.01, T03.G1.03
- **Issues:** None

#### T36.G2.03: Recognize teammates' different strengths
- **Dependencies:** T01.G1.10
- **Issues:** None

---

## Critical Issues Requiring Fixes

### 1. Skills Depending on K (Kindergarten) - May Skip G1 Bridge (17 skills)

These G2 skills depend directly on GK skills, potentially skipping necessary G1 bridge skills:

| Skill ID | Skill Title | GK Dependency | Recommendation |
|----------|------------|---------------|----------------|
| T01.G2.01 | Find actions that repeat in everyday tasks | T01.GK.07 | Check if there's a G1 bridge skill available |
| T01.G2.02 | Use "repeat" to make directions shorter | T01.GK.07 | Check if there's a G1 bridge skill available |
| T01.G2.08 | Trace an algorithm that uses "repeat ___ times" | T01.GK.07 | Check if there's a G1 bridge skill available |
| T04.G2.02 | Spot repeated step sequences | T01.GK.07 | Check if there's a G1 bridge skill available |
| T04.G2.04 | Replace repeated steps with "repeat ___ times" | T01.GK.07 | Check if there's a G1 bridge skill available |
| T12.G2.02 | Fix confusing labels on a plan | T01.GK.05 | Check if there's a G1 bridge skill available |
| T13.G2.01 | Fix steps that use the wrong signal | T01.GK.05 | Check if there's a G1 bridge skill available |
| T23.G2.01 | Pick the right sensor for a job | T04.GK.01 | Check if there's a G1 bridge skill available |
| T25.G2.02 | Translate between timeline, table, and sentence | T01.GK.08 | Check if there's a G1 bridge skill available |
| T25.G2.03 | Pick the best representation for a question | T01.GK.08 | Check if there's a G1 bridge skill available |
| T25.G2.04 | Combine two data attributes | T01.GK.08 | Check if there's a G1 bridge skill available |
| T26.G2.02 | Build a two-column record sheet | T01.GK.08 | Check if there's a G1 bridge skill available |
| T26.G2.04 | Explain why sample size matters | T01.GK.08 | Check if there's a G1 bridge skill available |
| T27.G2.02 | Interpret simple line plots | T01.GK.08 | Check if there's a G1 bridge skill available |
| T27.G2.04 | Decide if data answers the question asked | T01.GK.08 | Check if there's a G1 bridge skill available |
| T28.G2.02 | Conduct a picture-based chance experiment | T01.GK.08 | Check if there's a G1 bridge skill available |
| T28.G2.04 | Predict and observe outcomes | T01.GK.08 | Check if there's a G1 bridge skill available |

**Most Common GK Dependencies:**
- **T01.GK.08** (Count how many times) - 10 occurrences
- **T01.GK.07** (Find the pattern that repeats) - 5 occurrences
- **T01.GK.05** (Move the picture that's in the wrong place) - 2 occurrences
- **T04.GK.01** (Spot a simple repeating pattern) - 1 occurrence

---

## Informational Issues (May Not Need Fixes)

### 2. Transitive Redundancy (9 skills)

These skills have dependencies that are already covered transitively through other dependencies:

| Skill ID | Redundant Dependency | Already Covered Via |
|----------|---------------------|---------------------|
| T01.G2.02 | T01.GK.07 | T01.G2.01 |
| T01.G2.08 | T01.GK.07 | T01.G2.03 |
| T03.G2.02 | T03.G1.03 | T03.G2.01 |
| T04.G2.02 | T01.GK.07 | T04.G2.01 |
| T04.G2.04 | T01.GK.07 | T04.G2.03 |
| T05.G2.02 | T05.G1.01 | T05.G1.04 |
| T14.G2.02 | T01.G1.01 | T01.G1.04 |
| T14.G2.04 | T01.G1.01 | T01.G1.04 |
| T20.G2.04 | T01.G1.01 | T01.G1.04 |

**Note:** These can likely be simplified by removing the redundant dependency.

---

### 3. Same Topic/Grade Dependencies (26 skills)

These skills depend on earlier skills in the same topic and same grade. This may be redundant if skills within a topic/grade are assumed to be learned sequentially.

**Topics with Sequential Dependencies:**
- **T01** (Everyday Algorithms): 11 skills with sequential dependencies
- **T02** (Algorithm Diagrams): 5 skills with sequential dependencies
- **T03** (Problem Decomposition): 3 skills with sequential dependencies
- **T04** (Algorithm Patterns): 2 skills with sequential dependencies
- Others: 5 skills across various topics

---

## Positive Findings

1. **No Critical Grade Violations:** No G2 skills depend on G3+ skills
2. **No Circular Dependencies:** Dependency graph is acyclic
3. **Most Skills Are Clean:** 45 out of 88 skills (51%) have no issues at all

---

## Recommendations

### High Priority:
1. **Review GK → G2 jumps:** Identify whether G1 bridge skills exist for the 17 cases where G2 skills depend directly on GK skills
2. **Address T01.GK.07 & T01.GK.08:** These two kindergarten skills are heavily used by G2. Consider creating G1 bridge skills.

### Medium Priority:
3. **Remove transitive redundancies:** Clean up the 9 skills with redundant dependencies
4. **Document sequential assumptions:** Clarify whether same-topic/same-grade dependencies are needed or assumed

### Low Priority:
5. **Review cross-topic dependencies:** Many skills depend on T01.G1.01 (Put pictures in order to plant a seed) - verify this is the intended foundation skill

---

## Appendix: Most Referenced Dependencies

**Most Common G1 Dependencies:**
1. **T01.G1.01** - Put pictures in order to plant a seed (29 references)
2. **T01.G1.10** - Match pictures to "if/then" rules (11 references)
3. **T03.G1.03** - List steps for a simple classroom routine (8 references)
4. **T01.G1.04** - Predict the next step in a story sequence (7 references)

**Most Common GK Dependencies:**
1. **T01.GK.08** - Count how many times (10 references)
2. **T01.GK.07** - Find the pattern that repeats (5 references)
3. **T01.GK.05** - Move the picture that's in the wrong place (2 references)
