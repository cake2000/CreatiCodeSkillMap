# Grade K Cross-Topic Dependency Analysis

## Executive Summary

**Critical Finding:** ALL 97 Grade K skills currently have ZERO dependencies. This represents a major structural issue, as Grade K skills were treated as atomic "foundation" skills during Phase 1, but many of them actually build upon concepts from other topics.

### Key Statistics
- **Total Grade K skills:** 97 across 29 topics
- **Current dependencies:** 0 (!!!)
- **X-2 rule violations:** 0 (because there are no dependencies to violate)
- **Missing cross-topic dependencies:** 120+ potential additions needed
- **Circular dependencies:** 0
- **Redundant dependencies:** 0 (N/A since no deps exist)

### Topics Missing Grade K Skills
7 topics have no Grade K skills at all:
- T07 (Motion)
- T11 (Drawing)
- T12 (Sound)
- T16 (likely advanced topic)
- T17 (likely advanced topic)
- T19 (likely advanced topic)
- T28 (likely advanced topic)

## Major Issues Identified

### 1. **Grade K Skills Have No Dependencies**

This is the most significant finding. During Phase 1, we optimized intra-topic dependencies but didn't address cross-topic dependencies for Grade K. All Grade K skills were treated as "leaves" with no prerequisites.

**Problem:** Many Grade K skills implicitly assume knowledge from other topics:
- **T14.GK.02** (Recognize a score in games) should depend on **T09.GK.01** (Recognize that a label can hold a number)
- **T13.GK.01** (Spot wrong action in animation) should depend on foundational sequencing skills from T01/T02
- **T08.GK.01-02** (Conditional logic with "if") should depend on basic sequencing from T01

### 2. **Sequence/Order Skills Fragmented Across Topics**

**Skills with "order" or "sequence" in name appear in 7+ topics:**

| Skill ID | Topic | Skill Name |
|----------|-------|------------|
| T01.GK.01 | Everyday Algorithms | Put pictures in order for getting ready for bed |
| T01.GK.02 | Everyday Algorithms | Put pictures in order for coming to class |
| T02.GK.02 | Algorithm Diagrams | Order 3–4 pictures to make a story |
| T03.GK.03 | Problem Decomposition | Order 3–4 pictures to show steps in a routine |
| T06.GK.01 | Events & Sequences | Order pictures showing a morning routine |
| T15.GK.01 | Stories & Animation | Sequence story pictures |
| T20.GK.02 | Algorithmic Art | Order art steps with cards |

**Issue:** These skills all do essentially the same thing (ordering pictures) but are isolated from each other. Later topic skills (T15, T20) should logically depend on earlier foundational ordering skills (T01, T02).

**Recommendation:**
- T01.GK.01-02 remain foundational (no deps)
- T02.GK.02 → depends on T01.GK.01 or T01.GK.02
- T03.GK.03 → depends on T01.GK.02 (classroom routine builds on general routine)
- T06.GK.01 → depends on T01.GK.02 or T03.GK.03
- T15.GK.01 → depends on T02.GK.02 (story sequencing builds on general sequencing)
- T20.GK.02 → depends on T02.GK.02 or T03.GK.03

### 3. **Pattern Recognition Skills Not Connected**

**Pattern-related skills across 3 topics:**

| Skill ID | Topic | Skill Name |
|----------|-------|------------|
| T01.GK.07 | Everyday Algorithms | Find the pattern that repeats |
| T04.GK.01 | Algorithm Patterns | Identify a simple repeating pattern |
| T04.GK.02 | Algorithm Patterns | Extend a repeating pattern |
| T04.GK.03 | Algorithm Patterns | Describe a pattern |
| T04.GK.04 | Algorithm Patterns | Fix a broken pattern |
| T20.GK.01 | Algorithmic Art | Picture pattern detective |
| T20.GK.03 | Algorithmic Art | Continue the pattern trail |

**Issue:** T01.GK.07 and T04.GK.01 are nearly identical but not connected. T20 pattern skills don't depend on T04 pattern fundamentals.

**Recommendation:**
- T01.GK.07 remains foundational (recognizing patterns in everyday contexts)
- T04.GK.01 → depends on T01.GK.07 (formalizes the concept)
- T04.GK.02-04 → depend on T04.GK.01 (within same topic, already handled)
- T20.GK.01 → depends on T04.GK.01 or T04.GK.03
- T20.GK.03 → depends on T04.GK.02 (extending patterns)

### 4. **"Match" Skills Appear in 14 Different Topics**

Many skills use "match" verb but are completely disconnected:

| Topic | Count | Examples |
|-------|-------|----------|
| T03 | 1 | Match parts to whole objects |
| T05 | 1 | Match a problem to a tool |
| T06 | 1 | Match "first" and "next" words to pictures |
| T08 | 1 | Match pictures to "if it rains" rules |
| T10 | 1 | Match items that go together |
| T14 | 2 | Match controls to actions; Match rewards to goals |
| T15 | 1 | Match emotions to faces |
| T21 | 1 | Match picture to describing words |
| T23 | 1 | Match pictures of sensing |
| T25 | 1 | Match quantities to symbols |
| T30 | 1 | Match devices to actions |
| T34 | 1 | Match old vs new tech |
| T36 | 1 | Match community helpers to tools |

**Issue:** While all are "matching" activities, they represent different cognitive skills:
- **Categorical matching** (T03, T10, T30, T34, T36): Group similar things
- **Causal matching** (T05, T08, T14): Match cause to effect
- **Semantic matching** (T15, T21, T25): Match representation to meaning
- **System matching** (T23, T30): Match components to functions

**Recommendation:** These DON'T all need to depend on each other, but within each category, later skills should depend on earlier ones. For example:
- T30.GK.02 (Match devices to actions) → T05.GK.02 (Match problem to tool) [both about tool-action relationships]
- T36.GK.01 (Match helpers to tools) → T30.GK.02 [builds on device-action matching]

### 5. **Conditional Logic Skills Missing Foundation Dependencies**

**Conditional/choice skills:**

| Skill ID | Topic | Skill Name |
|----------|-------|------------|
| T08.GK.01 | Conditions & Logic | Match pictures to "if it rains" rules |
| T08.GK.02 | Conditions & Logic | Choose what happens next based on yes/no |
| T03.GK.04 | Problem Decomposition | Choose the missing middle step |
| T05.GK.03 | Human-Centered Design | Decide which version is easier |
| T05.GK.04 | Human-Centered Design | Choose a change that makes something easier |
| T23.GK.03 | AI Perception | Choose when to uncover or quiet a helper |
| T35.GK.04 | Impacts & Ethics | Choose safe sharing in role-play |

**Issue:** T08 (Conditions & Logic) skills introduce "if-then" thinking, but other topics have "choice" skills that don't reference this foundation.

**Recommendation:**
- T08.GK.01-02 should remain foundational OR depend on basic sequencing (T01.GK.02)
- T23.GK.03 (Choose when...) → T08.GK.02 (making conditional choices)
- Other "choose" skills may not need deps if they're about preference rather than logic

### 6. **Recognition/Identification Skills Across 10+ Topics**

**"Recognize" or "Identify" skills appear in many topics:**

These are often appropriately independent (recognizing different categories of things), but some build on each other:

- **T29.GK.01** (Recognize text vs pictures) is foundational
- **T29.GK.02** (Identify letters in text) → should depend on T29.GK.01
- **T30.GK.01** (Identify computing devices) is foundational
- **T31.GK.01** (Recognize internet-connected devices) → should depend on T30.GK.01

### 7. **Game-Related Skills Don't Depend on Fundamentals**

**T14 (2D Games) Grade K skills:**

| Skill ID | Skill Name | Should Depend On |
|----------|------------|------------------|
| T14.GK.01 | Match controls to character actions | T06.GK (events/input basics) |
| T14.GK.02 | Recognize a score in simple games | T09.GK.01 (labels hold numbers) |
| T14.GK.03 | Identify when a game starts and ends | T06.GK.01 or T08.GK (sequences/conditions) |
| T14.GK.04 | Match rewards to goals | T08.GK (conditional logic) |

**Issue:** Game skills involve multiple concepts (events, variables, conditions) but don't reference prerequisite knowledge.

**Recommendation:** Add cross-topic dependencies as shown above.

### 8. **Data/Counting Skills Not Connected**

**Data-related skills:**

| Skill ID | Topic | Skill Name |
|----------|-------|------------|
| T01.GK.08 | Everyday Algorithms | Count how many times |
| T10.GK.02 | Lists & Tables | Count items in each group |
| T25.GK.02 | Data Representation | Match quantities to symbols |
| T26.GK.01 | Data Collection | Identify countable things |
| T26.GK.02 | Data Collection | Use tokens to log repeated events |
| T27.GK.02 | Data Analysis | Compare which group has more |

**Issue:** Counting and quantification appear across multiple topics but aren't connected.

**Recommendation:**
- T01.GK.08 and T10.GK.02 are both basic counting (can be independent)
- T26.GK.01 → T10.GK.02 (countable things → counting groups)
- T26.GK.02 → T01.GK.08 (logging repeated events requires counting)
- T27.GK.02 → T10.GK.03 (both about comparing quantities)

### 9. **AI/Helper Skills Form a Cluster**

**AI-related skills across topics T21-24:**

| Skill ID | Topic | Skill Name |
|----------|-------|------------|
| T21.GK.01 | AI Media | Tell which pictures look like AI made them |
| T21.GK.02 | AI Media | Match picture to describing words |
| T21.GK.03 | AI Media | Pick the helper that can talk back |
| T22.GK.01 | Chatbots | Recognize a talking helper vs silent toy |
| T22.GK.02 | Chatbots | Practice asking a helper a question |
| T23.GK.01 | AI Perception | Match pictures of sensing |
| T23.GK.02 | AI Perception | Point to where device "looks" or "listens" |
| T23.GK.03 | AI Perception | Choose when to uncover/quiet a helper |
| T24.GK.01 | Gen AI | Identify AI as a computer helper |
| T24.GK.02 | Gen AI | Recognize AI-made vs human-made pictures |
| T24.GK.03 | Gen AI | Give simple instructions to AI helper |

**Issue:** These topics are sequential (T21→T22→T23→T24) but Grade K skills have no dependencies between them.

**Recommendation:**
- T21.GK.01 (identify AI-made pictures) is foundational
- T21.GK.03 (helper that can talk) is foundational
- T22.GK.01 (talking helper vs toy) → T21.GK.03 (builds on recognizing interactive helpers)
- T22.GK.02 (asking questions) → T22.GK.01 (must recognize talking helper first)
- T24.GK.01 (AI as helper) → T21.GK.03 or T22.GK.01 (formalizes "helper" concept)
- T24.GK.02 (AI vs human pictures) → T21.GK.01 (same concept, more formal)
- T24.GK.03 (giving instructions) → T22.GK.02 (both about interacting with AI)

### 10. **Computing Concepts Skills (T29-36) Lack Foundation Chain**

**Computing fundamentals topics:**

| Topic | Grade K Skills | Issue |
|-------|----------------|-------|
| T29 (Text/NLP) | 3 skills | Should build on each other |
| T30 (Devices) | 3 skills | Should connect to T31 (Internet) |
| T31 (Internet) | 1 skill | Should depend on T30.GK.01 (recognize devices) |
| T32 (Cybersecurity) | 4 skills | Should depend on T30 (devices) and T31 (internet) |
| T33 (Connected Services) | 1 skill | Should depend on T31 (internet concepts) |
| T34 (Computing History) | 3 skills | Should connect to T30 (devices) |
| T35 (Ethics) | 4 skills | Some should depend on T30/T32 |
| T36 (Careers) | 3 skills | Should depend on T30 (devices) |

**Recommendation:**
- T29.GK.02 → T29.GK.01 (letters in text requires recognizing text)
- T31.GK.01 → T30.GK.01 (internet devices requires recognizing devices)
- T32.GK.02 → T31.GK.01 (online help requires knowing what's online)
- T32.GK.04 → T31.GK.01 (online vs offline requires internet concept)
- T33.GK.01 → T31.GK.01 (apps talking to internet requires internet concept)
- T34.GK.02 → T30.GK.01 (old vs new tech requires recognizing tech)
- T36.GK.01 → T30.GK.02 (helpers with tools extends device-action matching)

## Recommended Dependency Additions

### High Priority (Clear Prerequisites)

These are unambiguous cases where one skill clearly builds on another:

1. **T29.GK.02** → T29.GK.01 (identify letters requires recognizing text)
2. **T31.GK.01** → T30.GK.01 (internet devices requires knowing devices)
3. **T32.GK.02** → T31.GK.01 (online help requires internet concept)
4. **T32.GK.04** → T31.GK.01 (online vs offline requires internet concept)
5. **T33.GK.01** → T31.GK.01 (apps & internet requires internet concept)
6. **T22.GK.01** → T21.GK.03 (talking helper builds on helper concept)
7. **T22.GK.02** → T22.GK.01 (asking questions requires recognizing talking helper)
8. **T24.GK.02** → T21.GK.01 (both identify AI-made pictures)
9. **T24.GK.03** → T22.GK.02 (giving instructions extends asking questions)
10. **T14.GK.02** → T09.GK.01 (score as variable requires label/number concept)

### Medium Priority (Logical but Not Essential)

These would improve coherence but aren't strictly required:

11. **T02.GK.02** → T01.GK.01 (story sequencing builds on routine sequencing)
12. **T03.GK.03** → T01.GK.02 (routine steps builds on picture ordering)
13. **T04.GK.01** → T01.GK.07 (formal pattern work builds on pattern recognition)
14. **T06.GK.01** → T01.GK.02 (morning routine builds on general routines)
15. **T15.GK.01** → T02.GK.02 (story pictures extends picture stories)
16. **T20.GK.01** → T04.GK.01 (pattern detective uses pattern recognition)
17. **T20.GK.03** → T04.GK.02 (continuing patterns extends extending patterns)
18. **T26.GK.01** → T10.GK.02 (countable things relates to counting)
19. **T27.GK.02** → T10.GK.03 (both compare quantities)
20. **T34.GK.02** → T30.GK.01 (old vs new tech requires recognizing tech)
21. **T36.GK.01** → T30.GK.02 (community helpers & tools extends device matching)

### Low Priority (Optional Enhancements)

These are more tenuous connections:

22. **T08.GK.02** → T01.GK.02 (conditional choices build on sequencing)
23. **T14.GK.03** → T06.GK.01 (game start/end relates to event sequences)
24. **T14.GK.04** → T08.GK.01 (rewards/goals relates to conditions)
25. **T20.GK.02** → T02.GK.02 or T03.GK.03 (art steps extends sequencing)

## False Positives to Ignore

The automated analysis flagged 120+ "missing dependencies" but most are false positives due to keyword matching. Here are categories to IGNORE:

### 1. **"Sound" False Positives**
Many skills mention "listen," "ask," "talk," or "class" which triggered "sound" keyword matches. These should NOT depend on T12 (Sound):
- T01.GK.02 (coming to class) - "class" ≠ sound
- T01.GK.03 (Find first/last) - no sound involved
- T22.GK.02 (asking questions) - about dialogue, not audio

### 2. **"Motion" False Positives**
Skills mentioning "move," "action," or "go" triggered motion matches, but many aren't about sprite movement:
- T01.GK.05 (Move picture that's wrong) - drag-drop UI, not sprite motion
- T06.GK.01 (morning routine) - "morning" triggered false match

### 3. **"Drawing" False Positives**
Many "picture" mentions triggered drawing matches:
- Most "picture" skills are about viewing/ordering images, not creating drawings

### 4. **"Events" False Positives**
"Click," "touch," "press" triggered event matches, but many are just UI interactions:
- T01.GK.03 (Find first/last) - clicking to select, not event programming

### 5. **"Conditionals" False Positives**
"If," "when," "check," "choice" triggered conditional matches, but many aren't about programming logic:
- T10.GK.02 (Count items in each group) - "each" triggered match
- T15.GK.02 (Match emotions to faces) - "match" triggered false positive

### 6. **"Loops" False Positives**
"Again," "repeat," "multiple times" triggered loop matches:
- T13.GK.02 (Retry after wrong) - "retry" isn't a loop concept at Grade K

### 7. **"Variables" False Positives**
"Score," "counter," "label" appropriately trigger variable matches, but "variable" in descriptions doesn't:
- T18.GK.01 (Explore 3D shapes) - false positive

## Skills That Should Remain Foundational (No Dependencies)

These Grade K skills should remain with zero dependencies as true entry points:

### Everyday Concepts (T01)
- T01.GK.01: Put pictures in order for getting ready for bed
- T01.GK.02: Put pictures in order for coming to class
- T01.GK.07: Find the pattern that repeats
- T01.GK.08: Count how many times

### Basic Sequencing (T02)
- T02.GK.01: Recognize picture steps for a task

### Decomposition (T03)
- T03.GK.01: Identify parts that make up a whole

### Human-Centered Design (T05)
- T05.GK.01: Name who a tool helps
- T05.GK.02: Match a problem to a helpful tool

### Lists & Tables (T10)
- T10.GK.01: Sort picture cards into groups
- T10.GK.02: Count items in each group

### Computing Basics (T30)
- T30.GK.01: Identify everyday computing devices

### AI Introduction (T21)
- T21.GK.01: Tell which pictures look like AI made them
- T21.GK.03: Pick the helper that can talk back

## Implementation Strategy

### Phase 2A: Add High-Priority Cross-Topic Dependencies (10 skills)
Focus on the 10 clearest prerequisite relationships listed above.

### Phase 2B: Add Medium-Priority Dependencies (11 skills)
Add the logical but non-essential dependencies.

### Phase 2C: Review Low-Priority Dependencies (Optional)
Evaluate whether these add value or just clutter.

### Phase 2D: Validate No Circular Dependencies
After each batch, re-run circular dependency check.

## Conclusion

The current state of Grade K skills (zero dependencies) is technically "correct" in that there are no violations of the X-2 rule, but it's pedagogically incomplete. Many Grade K skills implicitly assume prerequisite knowledge from other topics that isn't formally captured.

**Key Insight:** The X-2 rule (Grade X skills can depend on Grade X-2 and higher) doesn't prevent Grade K skills from depending on OTHER Grade K skills from different topics. We should establish these foundational connections to create a more coherent learning progression.

**Priority:** Focus on HIGH PRIORITY dependencies first (10 additions), particularly:
1. Computing concepts chain (T29→T30→T31→T32→T33)
2. AI concepts chain (T21→T22→T24)
3. Variables/scores connection (T09→T14)

These create clear conceptual progressions that align with how students actually learn these topics.
