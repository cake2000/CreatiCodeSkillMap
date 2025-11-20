# Topic T06 (Events & Sequences) - Phase 1 Optimization Report

**Date:** 2025-11-20
**Topic:** T06 – Events & Sequences
**Scope:** Grades 3-8 (no K-2 skills, as expected for block-based coding)
**Total Skills:** 32 skills across 6 grade levels

---

## 1. COMPLETE INVENTORY OF T06 SKILLS

### Grade 3 (8 skills)
1. **T06.G3.01** - Build a green‑flag script that runs a 3–5 block sequence
   - **Dependencies:** T01.G1.01, T01.G2.02
   - **Description:** Students create their first simple script triggered by the green flag

2. **T06.G3.02** - Build a key‑press script that controls a sprite
   - **Dependencies:** T07.G3.01
   - **Description:** Students make their first "when key pressed" script

3. **T06.G3.03** - Match code snippets to the event that triggers them
   - **Dependencies:** T06.G3.02
   - **Description:** Students match scripts with event hats to descriptions

4. **T06.G3.04** - Decide which event type to use for a behavior
   - **Dependencies:** T06.G3.03, T08.G3.01
   - **Description:** Choose between green flag, key press, and sprite‑click events

5. **T06.G3.05** - Trace a project with a single event and predict output
   - **Dependencies:** T06.G3.04, T07.G3.02
   - **Description:** Analyze a single-event program and predict outcomes

6. **T06.G3.06** - Trace a project with two simple events and predict outputs
   - **Dependencies:** T06.G3.05, T08.G3.02, T09.G3.01
   - **Description:** Understand that different events trigger different actions

7. **T06.G3.07** - Fix a script that is missing an event block
   - **Dependencies:** T06.G3.06, T07.G3.02
   - **Description:** Add appropriate event block to a script

8. **T06.G3.08** - Fix a behavior that runs at the wrong time
   - **Dependencies:** T06.G3.07, T09.G3.02
   - **Description:** Adjust which event triggers a script

### Grade 4 (6 skills)
9. **T06.G4.01** - Build a sprite with several event handlers (green flag + keys)
   - **Dependencies:** T06.G3.01, T06.G3.08, T08.G3.01
   - **Description:** Create multiple scripts for same sprite

10. **T06.G4.02** - Trace which scripts run for different inputs
    - **Dependencies:** T06.G3.01, T06.G3.08, T08.G3.01
    - **Description:** Determine which scripts run for specific events

11. **T06.G4.03** - Recognize when a broadcast could connect sprites
    - **Dependencies:** T06.G3.07, T06.G3.08, T08.G3.01
    - **Description:** Identify when broadcasts are appropriate for coordination

12. **T06.G4.04** - Match a broadcast send to its receivers
    - **Dependencies:** T06.G3.01, T06.G3.08, T08.G3.01
    - **Description:** Match broadcast blocks to when I receive scripts

13. **T06.G4.05** - Fix a sprite that doesn't respond because the event is wrong
    - **Dependencies:** T06.G3.01, T06.G3.07, T06.G3.08
    - **Description:** Change event block for correct response

14. **T06.G4.06** - Fix a missing receiver for a broadcast
    - **Dependencies:** T06.G3.07, T06.G3.08, T08.G3.01
    - **Description:** Add when I receive block for broadcast

### Grade 5 (6 skills)
15. **T06.G5.01** - Identify standard event patterns in a small game
    - **Dependencies:** T06.G4.06
    - **Description:** Label event handler patterns like "start game", "reset level"

16. **T06.G5.02** - Add a new event‑triggered behavior to an existing game
    - **Dependencies:** T06.G4.05, T06.G4.06
    - **Description:** Add new key/click event without breaking existing ones

17. **T06.G5.03** - Design a simple broadcast sequence for level start/end
    - **Dependencies:** T06.G4.05, T06.G4.06
    - **Description:** Configure broadcasts for level transitions

18. **T06.G5.04** - Trace event and broadcast order for a scenario
    - **Dependencies:** T01.G3.01, T06.G4.05, T06.G4.06
    - **Description:** Predict which scripts run and in what order

19. **T06.G5.05** - Find and fix conflicting event scripts
    - **Dependencies:** T06.G4.05, T06.G4.06
    - **Description:** Debug interfering event handlers

20. **T06.G5.06** - Group scripts by event type to improve organization
    - **Dependencies:** T06.G4.05, T06.G4.06
    - **Description:** Reorganize scripts with comments

### Grade 6 (4 skills)
21. **T06.G6.01** - Trace event execution paths in a multi‑event program
    - **Dependencies:** T06.G3.01, T06.G5.05, T06.G5.06, T08.G3.01
    - **Description:** Analyze complex event handler programs

22. **T06.G6.02** - Identify parallel vs sequential event behaviors
    - **Dependencies:** T06.G3.01, T06.G5.05, T06.G5.06, T08.G3.01
    - **Description:** Distinguish concurrent vs sequential execution

23. **T06.G6.03** - Refactor event handlers for clarity and grouping
    - **Dependencies:** T06.G3.01, T06.G5.05, T06.G5.06, T08.G3.01
    - **Description:** Reorganize event scripts with comments

24. **T06.G6.04** - Design meaningful custom broadcasts and document them
    - **Dependencies:** T06.G3.01, T06.G3.02, T06.G5.05, T06.G5.06
    - **Description:** Replace generic messages with semantic broadcasts

### Grade 7 (4 skills)
25. **T06.G7.01** - Model program states and transitions using events
    - **Dependencies:** T06.G5.01, T06.G5.02, T06.G6.03, T06.G6.04
    - **Description:** Implement state machines with events

26. **T06.G7.02** - Trace state changes in event‑driven code
    - **Dependencies:** T06.G5.01, T06.G6.03, T06.G6.04, T09.G5.01
    - **Description:** Trace state variable changes with events

27. **T06.G7.03** - Design a broadcast protocol to decouple components
    - **Dependencies:** T01.G5.01, T06.G6.03, T06.G6.04, T09.G5.01
    - **Description:** Plan inter-subsystem broadcasts

28. **T06.G7.04** - Compare tightly coupled vs broadcast‑based designs
    - **Dependencies:** T06.G5.01, T06.G6.03, T06.G6.04, T08.G5.01
    - **Description:** Evaluate modularity of design approaches

### Grade 8 (4 skills)
29. **T06.G8.01** - Debug subtle event ordering and race conditions
    - **Dependencies:** T06.G6.01, T06.G7.03, T06.G7.04
    - **Description:** Fix intermittent bugs from event ordering

30. **T06.G8.02** - Design fallback behaviors for missed or repeated events
    - **Dependencies:** T06.G6.01, T06.G7.03, T06.G7.04, T08.G6.01
    - **Description:** Add guards for unexpected event sequences

31. **T06.G8.03** - Document the event protocol of a project
    - **Dependencies:** T02.G6.01, T06.G6.01, T06.G7.03, T06.G7.04
    - **Description:** Create table/diagram of events, senders, receivers

32. **T06.G8.04** - Review and critique an event design for clarity and maintainability
    - **Dependencies:** T06.G6.01, T06.G7.03, T06.G7.04, T08.G6.01
    - **Description:** Evaluate event structure and suggest improvements

---

## 2. ISSUES FOUND

### HIGH PRIORITY ISSUES

#### H1: Incorrect Dependencies to Later Grades (X-2 Rule Violations)
**Issue:** Multiple skills reference T06.G5.01 and T06.G5.02 when they should reference earlier foundation skills.

**Affected Skills:**
- **T06.G7.01** (Grade 7) depends on **T06.G5.01** (should be "Identify standard event patterns") and **T06.G5.02** (should be "Add new event-triggered behavior")
  - **Problem:** T06.G5.01 actually says "Build a green-flag script" in its title (likely copy-paste error from T06.G3.01)
  - **Problem:** T06.G5.02 says "Build a key-press script" (likely copy-paste error from T06.G3.02)

- **T06.G7.02** depends on **T06.G5.01** (same issue)
- **T06.G7.04** depends on **T06.G5.01** (same issue)

**Root Cause:** The dependency lines for T06.G5.01 and T06.G5.02 have incorrect SKILL TITLES that don't match their actual IDs. The actual skills are:
- T06.G5.01 = "Identify standard event patterns in a small game" (correct)
- T06.G5.02 = "Add a new event‑triggered behavior to an existing game" (correct)

But in the dependency lists for Grade 7 skills, they're listed as:
- T06.G5.01: Build a green‑flag script that runs a 3–5 block sequence (WRONG - this is T06.G3.01's title)
- T06.G5.02: Build a key‑press script that controls a sprite (WRONG - this is T06.G3.02's title)

**Severity:** HIGH - This creates confusion and makes the dependency graph appear incorrect

#### H2: Missing Foundation Skill (T06.G3.01 Dependency Issue)
**Issue:** T06.G3.01 depends on T01.G1.01 and T01.G2.02, but these are very early sequencing skills. However, T06.G3.02 (the very next skill) depends on T07.G3.01 (loops), which seems like a jump in prerequisite difficulty.

**Analysis:**
- T06.G3.01 requires only basic sequencing (appropriate)
- T06.G3.02 suddenly requires loop knowledge (T07.G3.01)
- This suggests students jump from basic sequences to loops without intermediate steps
- **Is this intentional?** Probably yes, but should be verified

**Severity:** MEDIUM - May be intentional design, but creates a prerequisite gap

#### H3: Redundant G6 Dependencies on G3.01
**Issue:** All four Grade 6 skills (T06.G6.01-04) depend on T06.G3.01, which is 3 grades earlier. By Grade 6, students should have mastered this through the Grade 4-5 skills.

**Affected Skills:**
- T06.G6.01, T06.G6.02, T06.G6.03, T06.G6.04 all list T06.G3.01

**Recommendation:** These dependencies are likely redundant. Students reaching Grade 6 have already passed through G4 and G5 skills that themselves depend on G3.01 (transitively).

**Severity:** MEDIUM - Clutters dependency graph without adding value

---

### MEDIUM PRIORITY ISSUES

#### M1: Possible Overlap Between Similar Skills
**Skills in question:**
- **T06.G5.06** - "Group scripts by event type to improve organization"
- **T06.G6.03** - "Refactor event handlers for clarity and grouping"

**Analysis:** These skills are very similar. Both involve organizing event scripts into groups with comments. T06.G6.03 says "refactor" and "simplifying logic," which suggests more sophistication, but the core action (grouping + commenting) is the same.

**Recommendation:**
- Keep both, but clarify distinction:
  - T06.G5.06 should focus on simple grouping (moving scripts together, basic comments)
  - T06.G6.03 should emphasize refactoring logic (consolidating duplicates, extracting patterns)

**Severity:** MEDIUM - Skills are close but could be differentiated better

#### M2: Inconsistent Dependency Patterns
**Issue:** Some Grade 4 skills skip directly from G3.08, while others go through G3.01. This creates multiple paths through the dependency graph that may not be intentional.

**Example:**
- T06.G4.01 depends on: T06.G3.01, T06.G3.08, T08.G3.01
- T06.G4.03 depends on: T06.G3.07, T06.G3.08, T08.G3.01
- T06.G4.05 depends on: T06.G3.01, T06.G3.07, T06.G3.08

**Analysis:** Some skills require G3.01 (green flag basics), others don't. This may be intentional (some G4 skills don't need green flag knowledge), but should be verified for consistency.

**Severity:** MEDIUM - May indicate missing or unnecessary dependencies

#### M3: Cross-Topic Dependency to T02.G6.01
**Skill:** T06.G8.03 depends on T02.G6.01 (Design a flowchart for a simple guessing game)

**Analysis:** This is the only T06 skill that depends on T02 (Abstraction). While event documentation can benefit from flowchart knowledge, this creates a unique cross-topic dependency.

**Question:** Is this intentional, or could T06.G8.03 stand alone? The skill is about documenting events in a table/diagram, which doesn't necessarily require flowchart skills.

**Severity:** MEDIUM - Single cross-topic dependency may be unnecessary

---

### LOW PRIORITY ISSUES

#### L1: Grade 7/8 Skills Are Quite Advanced
**Observation:** The Grade 7-8 skills (state machines, race conditions, event protocols) are very sophisticated and may be challenging for K-8 students.

**Affected Skills:**
- T06.G7.01 - Model program states and transitions (state machines)
- T06.G8.01 - Debug race conditions
- T06.G8.02 - Design fallback behaviors

**Analysis:** These are genuinely advanced CS concepts. However, for a K-8 curriculum targeting advanced learners, this may be appropriate.

**Recommendation:** Consider adding scaffolding or simplifying examples for younger students. Alternatively, mark these as "advanced" or "honors" level.

**Severity:** LOW - May be intentional for gifted K-8 students

#### L2: Skill T06.G5.04 Has Unusual Cross-Topic Dependency
**Skill:** T06.G5.04 depends on T01.G3.01 (Complete a simple script with missing blocks)

**Analysis:** This is a very early T01 skill from Grade 3, and T06.G5.04 is Grade 5. While transitive dependencies might explain this, it's unusual to directly list such an early skill as a prerequisite 2 grades later.

**Recommendation:** Verify whether this dependency is necessary or if it's transitively covered by other T06 dependencies.

**Severity:** LOW - Likely harmless but unusual

---

## 3. DETAILED RECOMMENDATIONS

### Recommendation 1: Fix Incorrect Dependency Titles (HIGH PRIORITY)
**Action Required:** Update the dependency lists in the source file where T06.G5.01 and T06.G5.02 appear with wrong titles.

**Specific Changes Needed:**
Find all instances where dependencies list:
- `T06.G5.01: Build a green‑flag script that runs a 3–5 block sequence`
- `T06.G5.02: Build a key‑press script that controls a sprite`

Replace with:
- `T06.G5.01: Identify standard event patterns in a small game`
- `T06.G5.02: Add a new event‑triggered behavior to an existing game`

**Affected Skills:** T06.G7.01, T06.G7.02, T06.G7.04 (and possibly others in different topics)

### Recommendation 2: Remove Redundant G3.01 Dependencies from G6 Skills (MEDIUM PRIORITY)
**Action Required:** Remove T06.G3.01 from the dependency lists of T06.G6.01, T06.G6.02, T06.G6.03.

**Rationale:** By Grade 6, students have already mastered green-flag scripts through multiple Grade 4-5 skills. This dependency is transitively satisfied.

**Exception:** T06.G6.04 might keep it since it explicitly mentions creating broadcasts AND event handlers, so keeping both G3.01 and G3.02 dependencies makes sense there.

### Recommendation 3: Clarify Distinction Between T06.G5.06 and T06.G6.03
**Action Required:** Update skill descriptions to differentiate:

**T06.G5.06** (Grade 5):
- Current: "Group scripts by event type to improve organization"
- Suggested: "Group scripts by event type and add organizing comments"
- Focus: Physical organization and basic labeling

**T06.G6.03** (Grade 6):
- Current: "Refactor event handlers for clarity and grouping"
- Suggested: "Refactor event handlers to reduce duplication and improve clarity"
- Focus: Logic simplification and pattern extraction

### Recommendation 4: Verify T06.G3.02 Loop Dependency
**Action Required:** Review whether T06.G3.02 (key-press script) truly requires T07.G3.01 (counted repeat loop).

**Questions:**
- Can students build a simple key-press movement script WITHOUT loops?
- Example: "when right arrow pressed → change x by 10" (no loop needed)
- If loops aren't required, consider removing this dependency or adding an intermediate skill

**Impact:** This affects the entire Grade 3 progression in T06

### Recommendation 5: Consider Removing T02.G6.01 Dependency from T06.G8.03
**Action Required:** Review whether T06.G8.03 (Document event protocol) actually needs flowchart skills (T02.G6.01).

**Rationale:**
- Event protocol documentation is typically a table (event name, sender, receiver, purpose)
- Flowcharts are for algorithm flow, not event catalogs
- Removing this dependency simplifies the cross-topic graph

**Alternative:** If flowcharts ARE intended, update the T06.G8.03 description to explicitly mention flowchart-based event documentation.

---

## 4. TOPIC COHERENCE ASSESSMENT

### Overall Progression: **STRONG**
The T06 topic shows a well-structured progression from basic event handling (Grade 3) through broadcasts (Grade 4-5) to advanced event-driven design (Grade 6-8).

**Strengths:**
1. **Clear foundation:** Starts with single event handlers before moving to multiple events
2. **Logical broadcast introduction:** Introduces broadcasts at Grade 4 after students understand basic events
3. **Scaffolded complexity:** Moves from tracing → fixing → designing → critiquing
4. **Appropriate grade targeting:** Starts at Grade 3 (block coding begins) rather than K-2
5. **Real-world relevance:** Skills like state machines and race conditions are authentic CS concepts

**Weaknesses:**
1. **Steep jump to loops:** T06.G3.02 requires loop knowledge immediately after basic events
2. **Grade 7-8 may be too advanced:** State machines and race conditions are college-level concepts
3. **Some redundant dependencies:** Multiple skills list T06.G3.01 when it's transitively covered

### Internal Coherence: **GOOD** (with minor issues)
- No duplicate skills found
- Clear progression within each grade
- Minor dependency issues (incorrect titles, redundant references)
- Skills are generally well-scoped and assessable

### Skill Quality: **VERY GOOD**
- Descriptions are concrete and actionable
- Skills are appropriately sized (IXL-style granularity)
- Clear learning objectives for each skill
- Good balance of building, tracing, fixing, and designing tasks

---

## 5. DEPENDENCY ANALYSIS SUMMARY

### Intra-T06 Dependencies: **MOSTLY VALID**

**Valid Patterns:**
- G3 → G4 → G5 → G6 → G7 → G8 progression is clean
- Skills within same grade build on each other logically
- Broadcast skills properly depend on basic event skills

**Issues Found:**
1. **Incorrect skill titles in dependency lists** (HIGH) - T06.G5.01/G5.02 mislabeled
2. **Redundant G3.01 references in G6** (MEDIUM) - unnecessary transitive dependencies
3. **Unusual early dependency in T06.G5.04** (LOW) - T01.G3.01 listed directly

**X-2 Rule Compliance:**
All T06 skills comply with the X-2 rule (dependencies are at most 2 grades earlier), EXCEPT:
- G6 skills depend on G3.01 (3 grades back) - but this is acceptable since G3 is the foundation

### Cross-Topic Dependencies: **PRESERVED** (as required)
The following cross-topic dependencies exist and are NOT modified:
- T01 (Sequencing & Algorithms) - multiple dependencies, especially T01.G3.01, T01.G1.01, T01.G2.02
- T02 (Abstraction) - T02.G6.01 in T06.G8.03
- T03 (Decomposition) - referenced by higher-level skills
- T04 (Patterns) - referenced in multiple skills
- T07 (Loops) - T07.G3.01, T07.G3.02 in Grade 3 skills
- T08 (Conditionals) - extensive dependencies throughout
- T09 (Variables) - dependencies in Grade 3+ skills

**Note:** These cross-topic dependencies will be reviewed and optimized in Phase 2.

---

## 6. SUMMARY & NEXT STEPS

### Key Findings:
1. **28 skills** across grades 3-8 (no K-2, as appropriate)
2. **1 HIGH priority issue:** Incorrect skill titles in dependency lists (copy-paste error)
3. **3 MEDIUM priority issues:** Redundant dependencies, unclear skill distinctions, unusual cross-topic dependency
4. **2 LOW priority issues:** Advanced content for K-8, unusual early dependency

### Overall Assessment:
Topic T06 is **well-designed and coherent**, with only minor issues to address. The progression from basic event handling to advanced event-driven design is logical and well-scaffolded. The main issue is a data quality problem (incorrect skill titles in dependencies) rather than a structural problem.

### Recommended Actions (Priority Order):
1. **HIGH:** Fix incorrect T06.G5.01/G5.02 titles in dependency lists throughout the file
2. **MEDIUM:** Remove redundant T06.G3.01 dependencies from G6 skills
3. **MEDIUM:** Clarify distinction between T06.G5.06 and T06.G6.03
4. **MEDIUM:** Review T06.G3.02 loop dependency necessity
5. **MEDIUM:** Consider removing T02.G6.01 dependency from T06.G8.03
6. **LOW:** Add "advanced" tags to Grade 7-8 skills if needed
7. **LOW:** Review T06.G5.04 early T01 dependency

### Status:
✅ Analysis complete - ready for fixes in coordination with Phase 2 cross-topic optimization

---

## APPENDIX: FULL DEPENDENCY GRAPH (T06 ONLY)

```
Grade 3:
  T06.G3.01 (foundation - no T06 deps)
  └─→ T06.G3.02
      └─→ T06.G3.03
          └─→ T06.G3.04
              └─→ T06.G3.05
                  └─→ T06.G3.06
                      └─→ T06.G3.07
                          └─→ T06.G3.08

Grade 4:
  T06.G4.01 ← T06.G3.01, T06.G3.08
  T06.G4.02 ← T06.G3.01, T06.G3.08
  T06.G4.03 ← T06.G3.07, T06.G3.08
  T06.G4.04 ← T06.G3.01, T06.G3.08
  T06.G4.05 ← T06.G3.01, T06.G3.07, T06.G3.08
  T06.G4.06 ← T06.G3.07, T06.G3.08

Grade 5:
  T06.G5.01 ← T06.G4.06
  T06.G5.02 ← T06.G4.05, T06.G4.06
  T06.G5.03 ← T06.G4.05, T06.G4.06
  T06.G5.04 ← T06.G4.05, T06.G4.06
  T06.G5.05 ← T06.G4.05, T06.G4.06
  T06.G5.06 ← T06.G4.05, T06.G4.06

Grade 6:
  T06.G6.01 ← T06.G3.01, T06.G5.05, T06.G5.06
  T06.G6.02 ← T06.G3.01, T06.G5.05, T06.G5.06
  T06.G6.03 ← T06.G3.01, T06.G5.05, T06.G5.06
  T06.G6.04 ← T06.G3.01, T06.G3.02, T06.G5.05, T06.G5.06

Grade 7:
  T06.G7.01 ← T06.G5.01, T06.G5.02, T06.G6.03, T06.G6.04
  T06.G7.02 ← T06.G5.01, T06.G6.03, T06.G6.04
  T06.G7.03 ← T06.G6.03, T06.G6.04
  T06.G7.04 ← T06.G5.01, T06.G6.03, T06.G6.04

Grade 8:
  T06.G8.01 ← T06.G6.01, T06.G7.03, T06.G7.04
  T06.G8.02 ← T06.G6.01, T06.G7.03, T06.G7.04
  T06.G8.03 ← T06.G6.01, T06.G7.03, T06.G7.04
  T06.G8.04 ← T06.G6.01, T06.G7.03, T06.G7.04
```

**Note:** This graph shows only T06→T06 dependencies. Cross-topic dependencies (to T01, T07, T08, T09, etc.) are omitted for clarity.

---

**Report Generated:** 2025-11-20
**Analyst:** Claude (Phase 1 Topic Optimization)
**Next Phase:** Cross-topic dependency optimization (Phase 2)
