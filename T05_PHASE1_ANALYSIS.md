================================================================================
TOPIC T05 (HUMAN-CENTERED DESIGN) PHASE 1 ANALYSIS
================================================================================

SKILL COUNT PER GRADE:
----------------------
GK: 4 skills (T05.GK.01 - T05.GK.04)
G1: 4 skills (T05.G1.01 - T05.G1.04)
G2: 4 skills (T05.G2.01 - T05.G2.04)
G3: 6 skills (T05.G3.01 - T05.G3.06)
G4: 7 skills (T05.G4.01 - T05.G4.07) [includes T05.G4.04a]
G5: 6 skills (T05.G5.01 - T05.G5.06) [includes T05.G5.02a, T05.G5.05a]
G6: 8 skills (T05.G6.01 - T05.G6.08)
G7: 7 skills (T05.G7.01 - T05.G7.07)
G8: 6 skills (T05.G8.01 - T05.G8.06)

TOTAL: 52 skills across K-8

================================================================================
HIGH PRIORITY ISSUES (MUST FIX)
================================================================================

ISSUE H1: G3 skills depend on G3 skills from other topics (violates grade-level rule)
----------------------------------------------------------------------
Skills affected:
- T05.G3.01 depends on T08.G3.01 (same grade, different topic - likely not learned yet)
- T05.G3.03 depends on T08.G3.02 and T07.G3.01 (same grade, different topics)
- T05.G3.04 depends on T09.G3.01.04 (same grade, different topic)
- T05.G3.05 depends on T08.G3.03 (same grade, different topic)

Problem: Students working on T05 in G3 may not have encountered T07, T08, or T09 yet. These cross-topic dependencies at the same grade level create ordering problems.

Suggested fix: Either:
  a) Remove these cross-topic dependencies and make T05.G3 skills standalone, OR
  b) Change dependencies to prior-grade skills from those topics (e.g., T08.G2.xx if they exist)

This is the most critical issue affecting 4 out of 6 G3 skills.

----------------------------------------------------------------------

ISSUE H2: T05.G5.03 has circular dependency path
----------------------------------------------------------------------
Skill: T05.G5.03 - Identify variables and initial values for a simulation
Current dependencies:
  - T01.G3.01: Complete a simple script with missing blocks
  - T05.G4.05: Decide what to include vs ignore in a simulation
  - T09.G3.01.04: Display variable value on stage using the variable monitor

Problem: T05.G5.03 is in G5 but depends on T09.G3.01.04, which is in G3 - this violates the X-2 rule (G5 should not depend on G3). More importantly, T09.G3.01.04 likely depends on variable concepts that may require understanding what variables are first.

Suggested fix: 
  - Remove T09.G3.01.04 dependency
  - Keep only T05.G4.05 (prerequisite about what to include in simulation)
  - Add dependency on a G4 or G5 variable skill from T09 instead

----------------------------------------------------------------------

ISSUE H3: T05.G5.04 has same cross-topic G3 dependency issue
----------------------------------------------------------------------
Skill: T05.G5.04 - Draft simple update rules for a simulation
Current dependencies:
  - T05.G3.05: Select simple rules for a simulation
  - T05.G4.05: Decide what to include vs ignore in a simulation
  - T09.G3.01.04: Display variable value on stage using the variable monitor

Problem: Same as H2 - G5 skill depending on G3 skill from another topic violates X-2 rule.

Suggested fix: Replace T09.G3.01.04 with appropriate G4 or G5 variable skill.

----------------------------------------------------------------------

ISSUE H4: T05.G6.05 has same cross-topic G3 dependency issue
----------------------------------------------------------------------
Skill: T05.G6.05 - Plan a simple CreatiCode simulation with variables, rules, and UI
Current dependencies:
  - T01.G3.01: Complete a simple script with missing blocks
  - T05.G4.05: Decide what to include vs ignore in a simulation
  - T05.G4.06: Explain why a simplification is reasonable
  - T09.G3.01.04: Display variable value on stage using the variable monitor

Problem: G6 skill depending on G3 skill from another topic (T09.G3.01.04) violates X-2 rule.

Suggested fix: Replace T09.G3.01.04 with appropriate G5 or G6 variable skill.

----------------------------------------------------------------------

ISSUE H5: GK skills are NOT picture-based/unplugged
----------------------------------------------------------------------
Skills: T05.GK.01, T05.GK.02, T05.GK.03, T05.GK.04

Current descriptions suggest picture-based activities, which is GOOD. However:
- T05.GK.02 says "Students match simple everyday problems"
- T05.GK.03 says "compare two pictures of an interface/tool"
- T05.GK.04 says "pick one change"

These ARE picture-based, so actually this is CORRECT. No fix needed - removing from HIGH priority.

RETRACTION: After review, GK skills ARE appropriately picture-based. Not an issue.

----------------------------------------------------------------------

ISSUE H6: Unnecessary same-grade dependency in G1
----------------------------------------------------------------------
Skill: T05.G1.01 - Identify what a character needs in a story
Current dependencies:
  - T05.GK.02: Match a simple problem to a helpful tool
  - T01.GK.03: Find the first and last pictures

Problem: Why does identifying character needs require finding first/last pictures? The T01.GK.03 dependency seems arbitrary and unrelated to the HCD skill.

Suggested fix: Remove T01.GK.03 dependency. Keep only T05.GK.02.

----------------------------------------------------------------------

ISSUE H7: Unnecessary cross-topic dependency in G5
----------------------------------------------------------------------
Skill: T05.G5.01 - Write clear user needs and requirements for a small app
Current dependencies:
  - T05.G4.04a: Write one clear user need statement
  - T06.G3.01: Build a green-flag script that runs a 3-5 block sequence

Problem: Writing user needs is a planning/design activity. It doesn't require building scripts. The T06.G3.01 dependency (from G3!) seems unnecessary and violates X-2 rule.

Suggested fix: Remove T06.G3.01 dependency. This is purely a HCD writing/planning skill.

----------------------------------------------------------------------

ISSUE H8: Unnecessary cross-topic dependency in G5.03
----------------------------------------------------------------------
Skill: T05.G5.03 - Identify variables and initial values for a simulation
Current dependencies include T01.G3.01: Complete a simple script with missing blocks

Problem: This is a PLANNING skill about identifying variables. It doesn't require completing scripts. The T01.G3.01 dependency violates X-2 rule and is conceptually unnecessary.

Suggested fix: Remove T01.G3.01 dependency. Keep only simulation-related dependencies.

----------------------------------------------------------------------

ISSUE H9: Unnecessary cross-topic dependency in G6.05
----------------------------------------------------------------------
Skill: T05.G6.05 - Plan a simple CreatiCode simulation with variables, rules, and UI
Current dependencies include T01.G3.01: Complete a simple script with missing blocks

Problem: Same as H8. This is a PLANNING skill. Violates X-2 rule.

Suggested fix: Remove T01.G3.01 dependency.

================================================================================
MEDIUM PRIORITY ISSUES (SHOULD FIX)
================================================================================

ISSUE M1: Missing scaffolding between G2 and G3 for HCD process
----------------------------------------------------------------------
Gap: G2 ends with individual design choices (accessibility features, simulations). G3 suddenly introduces the full HCD cycle with steps in order.

Current: T05.G3.01 depends on T05.G2.01 (matching users to designs)

Problem: Students jump from matching designs to ordering the entire HCD process without intermediate steps.

Suggested fix: Consider adding a G2 or early G3 skill that introduces HCD steps informally before requiring students to order them.

----------------------------------------------------------------------

ISSUE M2: Simulation skills branch starts early but has gaps
----------------------------------------------------------------------
Observation:
- G2 introduces simulation concept (T05.G2.03, T05.G2.04)
- G3 continues simulation rules (T05.G3.04, T05.G3.05)
- G4 adds complexity (T05.G4.05, T05.G4.06)
- G5 adds variables and rules (T05.G5.03, T05.G5.04)
- G6 adds planning and UI (T05.G6.05, T05.G6.06, T05.G6.08)
- G8 adds controlled experiments (T05.G8.03, T05.G8.04)
- G7 has NO simulation skills (gap!)

Problem: G7 breaks the simulation progression. Students go from G6 planning to G8 experiments without G7 scaffolding.

Suggested fix: Add G7 simulation skill about implementing or testing a simple simulation, bridging planning (G6) and controlled experiments (G8).

----------------------------------------------------------------------

ISSUE M3: Accessibility progression could be clearer
----------------------------------------------------------------------
Accessibility skills appear at:
- G2: Identify accessible features (T05.G2.02)
- G3: Match features to users (T05.G3.06)
- G4: Recognize and choose improvements (T05.G4.03, T05.G4.04)
- G5: Identify needed features for personas (T05.G5.05a)
- G6: Apply checklist (T05.G6.01 mentions accessibility)
- G7: Perform systematic review (T05.G7.01, T05.G7.02)

This progression is generally good, but G6 has no dedicated accessibility skill - it only mentions it as part of broader HCD checklist.

Suggested fix: Make T05.G6.01's accessibility component more explicit, or add a G6 skill about applying accessibility in design.

----------------------------------------------------------------------

ISSUE M4: "a" suffix skills disrupt numbering
----------------------------------------------------------------------
Skills with "a" suffix:
- T05.G4.04a (between G4.04 and G4.05)
- T05.G5.02a (between G5.02 and G5.03)
- T05.G5.05a (between G5.05 and G5.06)

Problem: These were likely added later and disrupt the sequential numbering. Makes it harder to track progression.

Suggested fix: Renumber these as regular skills in future revision (e.g., T05.G4.05 becomes T05.G4.06, current G4.05 becomes G4.07, etc.)

----------------------------------------------------------------------

ISSUE M5: User testing skills appear late and sparsely
----------------------------------------------------------------------
User testing appears:
- G4: Choose test task (T05.G4.07) - selecting which task reveals a problem
- G5: Plan testing (T05.G5.05) - write test plan
- G7: Interpret data (T05.G7.05, T05.G7.06) - analyze testing results

Gap: No skill in G6 about conducting or observing a test, interpreting individual test observations, or synthesizing test results before jumping to data analysis in G7.

Suggested fix: Add G6 skill about conducting a simple user test or observing test sessions.

----------------------------------------------------------------------

ISSUE M6: Feedback loop skills could be more connected
----------------------------------------------------------------------
Feedback appears:
- G3: Choose changes based on feedback (T05.G3.03)
- G6: Update design based on feedback (T05.G6.04)
- G7: Write sentence connecting decision to feedback (T05.G7.07)

These skills are spread out and don't clearly build on each other. T05.G6.04 depends on T05.G6.03 (analyzing interview data) but not on T05.G3.03 (earlier feedback skill).

Suggested fix: Ensure feedback skills have clear dependencies showing progression from simple choices (G3) to updates (G6) to justifications (G7).

----------------------------------------------------------------------

ISSUE M7: Persona skills could start earlier
----------------------------------------------------------------------
Personas appear:
- G4: First mention (T05.G4.01, T05.G4.02)
- G5: Writing user needs for personas (T05.G4.04a, T05.G5.01)
- G6: Analyzing data (T05.G6.03)

Problem: Personas are a fundamental HCD concept but don't appear until G4. Earlier grades use "character" or "user" generically.

Suggested fix: Consider introducing simple persona concepts in G3 (e.g., "user cards" with age, goals) before full personas in G4.

----------------------------------------------------------------------

ISSUE M8: XO integration appears only in G8
----------------------------------------------------------------------
Skill: T05.G8.02 - Use XO to critique and refine a design brief

Problem: XO (AI assistant) is introduced suddenly in G8 without prior exposure to AI-assisted design critique.

Suggested fix: Either:
  a) Add G7 skill introducing XO for simpler tasks, OR
  b) Add note in description that XO has been used in other contexts before this skill

================================================================================
LOW PRIORITY ISSUES (NICE TO HAVE)
================================================================================

ISSUE L1: Minor wording inconsistencies
----------------------------------------------------------------------
Examples:
- Some skills say "Students see" while others say "Students read"
- Some use "choose" vs "select" inconsistently
- Some say "simple" vs "small" for app size

Suggested fix: Standardize terminology in future revision for consistency.

----------------------------------------------------------------------

ISSUE L2: Grade 2 has only 4 skills (smallest non-K grade)
----------------------------------------------------------------------
Observation: Most grades have 4-8 skills, but G2 has only 4.

This is not necessarily a problem if coverage is adequate, but worth noting.

Suggested fix: Review whether G2 could benefit from additional scaffolding skills.

----------------------------------------------------------------------

ISSUE L3: Some descriptions could be more concise
----------------------------------------------------------------------
Example: T05.G2.03 has a very long description with parenthetical examples.

Suggested fix: Move detailed examples to separate implementation notes; keep descriptions focused on the core skill.

----------------------------------------------------------------------

ISSUE L4: Simulation vs simulation terminology
----------------------------------------------------------------------
Some skills use "simulation" while others use "computer pretend version" (G2) or "CreatiCode simulation" (G6).

Suggested fix: Standardize terminology - use age-appropriate terms ("pretend" for early grades, "simulation" for later).

----------------------------------------------------------------------

ISSUE L5: Missing explicit connection between design and implementation
----------------------------------------------------------------------
Observation: T05 focuses heavily on design, planning, and testing. Connection to actual implementation in CreatiCode could be more explicit.

Some skills mention CreatiCode (e.g., T05.G6.05) but most don't specify where/how students will build what they design.

Suggested fix: Add notes about which T06 (Project Development) or other topic skills connect to each design phase.

----------------------------------------------------------------------

ISSUE L6: Harm identification appears suddenly in G7
----------------------------------------------------------------------
Skill: T05.G7.03 - Identify potential unintended harms from a design

Problem: This is the first mention of harms, ethics, or negative consequences. It's an important topic but appears without prior scaffolding.

Suggested fix: Consider adding G6 skill about "positive and negative impacts" before jumping to harms analysis in G7.

================================================================================
OVERALL ASSESSMENT OF TOPIC COHERENCE
================================================================================

STRENGTHS:
----------
1. Clear K-8 progression from concrete (pictures, matching) to abstract (planning, justification)
2. Good separation of concerns into threads:
   - Core HCD process (empathy, needs, testing, iteration)
   - Accessibility (features -> review -> systematic evaluation)
   - Simulation design (concept -> planning -> experiments)
3. Skills are generally well-scoped and IXL-like (specific, actionable)
4. Age-appropriate complexity increase
5. K-2 skills are appropriately picture-based/unplugged
6. G3+ skills involve block-based concepts (variables, conditionals, loops)
7. Good use of scaffolding within topics (e.g., identify -> match -> choose -> justify)

WEAKNESSES:
-----------
1. CRITICAL: Multiple cross-topic dependencies at same grade level (G3 skills depend on T07, T08, T09 G3 skills)
2. CRITICAL: Several violations of X-2 rule (G5-6 depending on G3 skills from other topics)
3. Some unnecessary cross-topic dependencies (T01.G3.01, T06.G3.01) that don't add value
4. G7 simulation gap breaks progression
5. Persona introduction could be earlier
6. User testing could have more scaffolding
7. Harm/ethics introduction is abrupt

TOPIC COHERENCE RATING: 7/10

The topic has strong internal structure with three well-developed threads (HCD process, accessibility, simulation). However, the cross-topic dependencies need urgent cleanup to make the topic truly coherent and teachable. The X-2 rule violations and same-grade cross-topic dependencies create potential ordering nightmares.

RECOMMENDATIONS FOR PHASE 2:
----------------------------
1. PRIORITY 1: Fix all cross-topic same-grade dependencies (H1)
2. PRIORITY 2: Fix all X-2 rule violations (H2-H4, H7-H9)
3. PRIORITY 3: Remove unnecessary cross-topic dependencies (H6, H8, H9)
4. PRIORITY 4: Fill G7 simulation gap (M2)
5. PRIORITY 5: Add G6 user testing skill (M5)
6. Review and strengthen feedback loop progression (M6)
7. Consider earlier persona introduction (M7)

ESTIMATED OPTIMIZATION SCOPE:
-----------------------------
- HIGH priority issues: 9 issues affecting 15+ skills
- MEDIUM priority issues: 8 issues affecting topic structure
- LOW priority issues: 6 issues (wording, terminology)

Phase 2 optimization should focus on dependency cleanup first, then structural gaps, then polish.

================================================================================
DETAILED SKILL-BY-SKILL ISSUE BREAKDOWN
================================================================================

HIGH PRIORITY ISSUES WITH SPECIFIC RECOMMENDATIONS:

1. T05.G3.01 - Put human-centered design steps in order
   Current dependencies:
   - T05.G2.01: Match different users to different preferred designs
   - T08.G3.01: Use a simple if in a script

   PROBLEM: Same-grade cross-topic dependency on T08.G3.01
   FIX: Remove T08.G3.01. The skill is about ordering HCD steps, not coding.
   JUSTIFICATION: Understanding HCD process doesn't require conditionals.

2. T05.G3.03 - Choose design changes based on simple feedback
   Current dependencies:
   - T05.G2.02: Identify features that make a design more accessible
   - T05.G1.04: Suggest one change that helps a specific user
   - T08.G3.02: Decide when a single if is enough
   - T07.G3.01: Use a counted repeat loop

   PROBLEM: Same-grade cross-topic dependencies on T08.G3.02 and T07.G3.01
   FIX: Remove T08.G3.02 and T07.G3.01
   JUSTIFICATION: Choosing design changes is a design skill, not coding.
   Keep only the two T05 dependencies which provide proper scaffolding.

3. T05.G3.04 - Decide what a simple simulation should show
   Current dependencies:
   - T05.G2.04: Choose what to include in a very simple simulation
   - T09.G3.01.04: Display variable value on stage using the variable monitor

   PROBLEM: Same-grade cross-topic dependency on T09.G3.01.04
   FIX: Remove T09.G3.01.04
   JUSTIFICATION: This is about DECIDING what to show (planning), not implementing variables.
   Students can learn what to display conceptually before coding it.

4. T05.G3.05 - Select simple rules for a simulation
   Current dependencies:
   - T05.G2.04: Choose what to include in a very simple simulation
   - T08.G3.03: Pick the right conditional block for a scenario

   PROBLEM: Same-grade cross-topic dependency on T08.G3.03
   FIX: Remove T08.G3.03
   JUSTIFICATION: Selecting rules conceptually (e.g., "if it rains, plant grows") 
   doesn't require knowing which conditional block to use in code.

5. T05.G5.01 - Write clear user needs and requirements for a small app
   Current dependencies:
   - T05.G4.04a: Write one clear user need statement
   - T06.G3.01: Build a green-flag script that runs a 3-5 block sequence

   PROBLEM: X-2 violation (G5 -> G3) and unnecessary cross-topic dependency
   FIX: Remove T06.G3.01
   JUSTIFICATION: Writing requirements is pure planning. Students don't need to 
   build scripts to write "As a user, I need X so that Y."

6. T05.G5.03 - Identify variables and initial values for a simulation
   Current dependencies:
   - T01.G3.01: Complete a simple script with missing blocks
   - T05.G4.05: Decide what to include vs ignore in a simulation
   - T09.G3.01.04: Display variable value on stage using the variable monitor

   PROBLEM: Two X-2 violations (G5 -> G3 twice)
   FIX: Remove T01.G3.01 and T09.G3.01.04. Keep only T05.G4.05.
   JUSTIFICATION: This is about IDENTIFYING variables in planning phase.
   Students can identify "number of rabbits = 10" without coding experience.
   ADD: Consider adding dependency on a G4 or G5 variable concept skill if it exists.

7. T05.G5.04 - Draft simple update rules for a simulation
   Current dependencies:
   - T05.G3.05: Select simple rules for a simulation
   - T05.G4.05: Decide what to include vs ignore in a simulation
   - T09.G3.01.04: Display variable value on stage using the variable monitor

   PROBLEM: X-2 violation (G5 -> G3)
   FIX: Remove T09.G3.01.04
   JUSTIFICATION: Drafting rules like "each month, rabbits double" is conceptual.
   ADD: Consider dependency on G4/G5 variable skill instead.

8. T05.G1.01 - Identify what a character needs in a story
   Current dependencies:
   - T05.GK.02: Match a simple problem to a helpful tool
   - T01.GK.03: Find the first and last pictures

   PROBLEM: Unnecessary cross-topic dependency
   FIX: Remove T01.GK.03
   JUSTIFICATION: Reading a story and identifying needs doesn't require 
   understanding sequence/ordering of pictures. The T01.GK.03 connection is tenuous.

9. T05.G6.05 - Plan a simple CreatiCode simulation with variables, rules, and UI
   Current dependencies:
   - T01.G3.01: Complete a simple script with missing blocks
   - T05.G4.05: Decide what to include vs ignore in a simulation
   - T05.G4.06: Explain why a simplification is reasonable
   - T09.G3.01.04: Display variable value on stage using the variable monitor

   PROBLEM: Two X-2 violations (G6 -> G3 twice)
   FIX: Remove T01.G3.01 and T09.G3.01.04
   JUSTIFICATION: Planning a simulation (listing variables, rules, UI elements)
   is a design/planning activity. Students can plan without implementation skills.
   Keep T05.G4.05 and T05.G4.06 which provide proper HCD planning scaffolding.

================================================================================
SUMMARY OF DEPENDENCY REMOVALS NEEDED:
================================================================================

Remove these cross-topic dependencies:
- T05.G3.01: Remove T08.G3.01
- T05.G3.03: Remove T08.G3.02 and T07.G3.01
- T05.G3.04: Remove T09.G3.01.04
- T05.G3.05: Remove T08.G3.03
- T05.G5.01: Remove T06.G3.01
- T05.G5.03: Remove T01.G3.01 and T09.G3.01.04
- T05.G5.04: Remove T09.G3.01.04
- T05.G1.01: Remove T01.GK.03
- T05.G6.05: Remove T01.G3.01 and T09.G3.01.04

TOTAL DEPENDENCIES TO REMOVE: 13

IMPACT: This will make T05 much more standalone and teachable. Students can 
learn HCD concepts (empathy, needs, planning, testing) without waiting for 
coding skills from other topics. The planning/design skills can be learned 
conceptually and then applied when coding skills are ready.

PRINCIPLE: Human-centered design is primarily about understanding users and 
planning solutions. Most T05 skills should NOT depend on implementation skills.
Only skills that explicitly involve building or coding should have coding 
prerequisites.

