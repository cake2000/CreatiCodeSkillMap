# T28 (Chance & Simulations) Internal Analysis
## Lines 14792-15247 | 41 Skills | Grades G2-G8

---

## HIGH PRIORITY ISSUES

### 1. DUPLICATES/REDUNDANCIES

**ISSUE 1A: Overlapping experiment observation skills**
- **Skills**: T28.G2.04, T28.G3.01
- **Problem**: Both involve observing pre-built experiments and interpreting results
  - T28.G2.04 (G2): "make a prediction before each of five coin flips, then compare"
  - T28.G3.01 (G3): "watch a CreatiCode project run 20 random trials (pre-built) and answer questions about the resulting bar chart"
- **Severity**: Medium overlap - G2 is unplugged (physical coins), G3 is on-screen (CreatiCode project)
- **Recommendation**: KEEP BOTH - they represent appropriate progression (unplugged → digital), but clarify that G2 should be physical/picture-based

**ISSUE 1B: Redundant "fairness" concepts**
- **Skills**: T28.G2.03, T28.G4.04
- **Problem**:
  - T28.G2.03 (G2): "compare two drawn spinners (equal vs uneven slices) and explain which is 'fairer'"
  - T28.G4.04 (G4): "Debug an 'unfair' simulation... inspect a script where one outcome is favored (duplicate entries, wrong range) and fix it"
- **Severity**: Moderate - same concept at different abstraction levels
- **Recommendation**: KEEP BOTH - G2 is visual/unplugged, G4 is code-based debugging. This is appropriate scaffolding.

---

### 2. DEPENDENCY VIOLATIONS WITHIN T28

**ISSUE 2A: G3.06 depends on both G3.02 AND G3.03**
- **Skill**: T28.G3.06 (Modify a teacher-provided random generator)
- **Problem**: Depends on both T28.G3.02 and T28.G3.03, but G3.03 already depends on G3.02
- **Fix**: Remove redundant dependency on T28.G3.02
- **Updated dependencies**: T28.G3.03 only

**ISSUE 2B: Circular dependency pattern in G6**
- **Skill**: T28.G6.05 (Model a simple agent in a grid world)
- **Dependencies**: T09.G4.04, T09.G5.01, T28.G5.04
- **Problem**: T28.G6.05 has no T28 prerequisites except G5.04, then T28.G6.07 depends on T28.G6.05
- **Severity**: Low - this is actually fine progression
- **Recommendation**: NO CHANGE needed

---

### 3. X-2 RULE VIOLATIONS (Dependencies more than 2 grades back)

**ISSUE 3A: G4 skills reaching back to G1**
- **Skill**: T28.G4.01 (Build a simple random generator)
- **Problem**: No direct violation, but dependencies include T07.G3.05, which is only 1 grade back
- **Severity**: NONE - all dependencies are within acceptable range

**ISSUE 3B: G6 skills with G3 dependencies**
- **Skills**: T28.G6.03, T28.G6.01, T28.G6.04
- **Problem**: None found - all G6 skills depend on G4 or G5 T28 skills
- **Severity**: NONE

**NO X-2 VIOLATIONS FOUND IN T28**

---

### 4. MISSING SCAFFOLDING

**ISSUE 4A: Jump from G3 modification to G4 building**
- **Gap**: T28.G3.06 (modify teacher-provided generator) → T28.G4.01 (build from scratch)
- **Problem**: Students go from modifying existing code to building complete if-statement logic with random numbers
- **Missing step**: A G3 skill where students assemble pre-built components (drag if-blocks, random blocks) with guidance
- **Recommendation**: INSERT T28.G3.07: "Assemble a random generator from provided blocks"
  - Description: "Students receive separate blocks (pick random, if-statements, say blocks) and follow a visual guide to connect them in the correct order to create a working 2-option random generator."
  - Dependencies: T28.G3.06, T08.G3.01
  - Position: Between current G3.06 and G4.01

**ISSUE 4B: Probability concept appears suddenly**
- **Gap**: No introduction to basic probability concepts before T28.G5.05
- **Problem**: T28.G5.05 "Calculate theoretical probability" has no T28 foundation - students jump from collecting experimental data to calculating formal probabilities
- **Missing step**: Understanding what probability means before calculating it
- **Recommendation**: INSERT T28.G4.06: "Interpret simple probabilities from familiar contexts"
  - Description: "Students examine scenarios (spinner with 4 equal sections, bag with 3 red and 1 blue marble) and explain in words the chance of each outcome using fractions (e.g., 'red is 3 out of 4 because there are 3 red marbles and 4 total')."
  - Dependencies: T28.G4.02
  - Position: Before T28.G5.05

**ISSUE 4C: Monte Carlo appears without foundation**
- **Gap**: T28.G5.03 (Use Monte Carlo sampling) has complex logic
- **Problem**: Students must "check if each point lands inside a simple shape" - this requires conditional logic for geometric boundaries that hasn't been scaffolded in T28
- **Missing step**: Simpler boundary-checking exercises
- **Recommendation**: This is actually covered by dependencies (T28.G4.05 generates random coordinates, T28.G4.03 shows variability). The geometric checking should be scaffolded in T03 (motion) or T08 (conditionals).
- **Action**: NO NEW SKILL needed, but T28.G5.03 should add dependency on T08.G4.01

**ISSUE 4D: Agent-based simulation appears abruptly**
- **Gap**: T28.G6.05 (Model a simple agent in a grid world) introduces complex agent modeling
- **Problem**: This is the first mention of "agent" concepts in T28, but immediately expects tracking position, direction, and implementing movement rules
- **Missing step**: Introduction to what agents are and simpler state tracking
- **Recommendation**: INSERT T28.G5.08: "Track a sprite's state across multiple events"
  - Description: "Students create a simple sprite that remembers its state (happy/sad/hungry) using a variable. They implement events (green flag sets happy, space key makes sad, click makes hungry) and use if-statements to make the sprite say different messages based on its current state."
  - Dependencies: T28.G5.04, T09.G4.04
  - Position: Before T28.G6.05

**ISSUE 4E: Two-agent interaction too complex**
- **Gap**: T28.G7.01 expects students to build two-agent interactions with "probabilistic rules" and mutual state changes
- **Problem**: Jump from single-agent reward tracking (G6.08) to complex multi-agent systems
- **Missing step**: Simpler two-sprite communication without probabilistic elements
- **Recommendation**: This is partially covered by T06.G5.01 (broadcasting), but needs T28-specific scaffolding
- **Action**: INSERT T28.G6.09: "Create a simple two-sprite random interaction"
  - Description: "Students create two sprites that each randomly move around the stage. When they touch (using touching? block), one changes color. Students run this 10 times and count how many steps it takes for them to touch."
  - Dependencies: T28.G6.05, T06.G5.01
  - Position: Before T28.G7.01

---

### 5. SKILLS TOO BROAD (Need sub-skills with .01, .02 notation)

**ISSUE 5A: T28.G4.02 combines too many concepts**
- **Skill**: T28.G4.02 (Log 50 trials into a list and compute frequencies)
- **Problem**: "extend their spinner to repeat 50 times, append results to a list, and calculate percentage for each color"
  - This includes: looping, list management, counting frequencies, calculating percentages
- **Recommendation**: SPLIT into:
  - **T28.G4.02.01**: "Log trial results into a list"
    - Description: "Students extend their random generator to repeat 50 times and append each result to a list. They verify the list contains 50 entries."
    - Dependencies: T28.G4.01, T07.G3.01, T10.G3.03
  - **T28.G4.02.02**: "Count frequencies from a list"
    - Description: "Students write code to count how many times each outcome appears in their list of 50 results, storing counts in separate variables or a second list."
    - Dependencies: T28.G4.02.01, T07.G3.05
  - **T28.G4.02.03**: "Calculate percentages from counts"
    - Description: "Students convert their frequency counts to percentages by dividing each count by the total number of trials (50) and multiplying by 100. They display these percentages on stage."
    - Dependencies: T28.G4.02.02

**ISSUE 5B: T28.G5.01 too complex**
- **Skill**: T28.G5.01 (Simulate compound events - two dice)
- **Problem**: "roll two virtual dice 200 times, store sums, and explain why 7 is most common by referencing combinations"
  - Combines: two random generators, summing, 200-trial loop, data storage, analysis, theoretical explanation
- **Recommendation**: SPLIT into:
  - **T28.G5.01.01**: "Generate and sum two random values"
    - Description: "Students create a script that picks two random numbers (1-6) and adds them together, displaying the sum. They click multiple times to verify different sums appear."
    - Dependencies: T28.G4.02.03, T07.G3.05
  - **T28.G5.01.02**: "Collect and analyze compound event data"
    - Description: "Students extend their two-dice simulation to run 200 times, storing sums in a list. They create a frequency distribution showing how often each sum (2-12) appeared and identify which sum is most common."
    - Dependencies: T28.G5.01.01, T28.G4.02.02, T27.G3.04

**ISSUE 5C: T28.G6.01 too vague and broad**
- **Skill**: T28.G6.01 (Conduct parameter sweeps for tuning)
- **Problem**: "loop over a range of parameters (e.g., enemy speed) and log win rates to choose balanced values"
  - This is extremely broad and could be an entire unit
- **Recommendation**: SPLIT into:
  - **T28.G6.01.01**: "Test multiple parameter values manually"
    - Description: "Students run a simple game simulation with three different parameter values (e.g., enemy speed = 5, 10, 15), recording the outcome for each. They compare results and identify which value creates the most balanced gameplay."
    - Dependencies: T28.G5.01.02, T28.G5.04, T09.G5.01
  - **T28.G6.01.02**: "Automate parameter sweeps with loops"
    - Description: "Students write a script that automatically loops through a range of parameter values (e.g., speed from 5 to 15 in steps of 1), runs 10 trials at each value, and stores average outcomes in a table."
    - Dependencies: T28.G6.01.01, T07.G4.01

**ISSUE 5D: T28.G7.06 too ambitious**
- **Skill**: T28.G7.06 (Build multi-agent simulations with aggregated metrics)
- **Problem**: "extend their two-agent simulation to include 5-10 agents of different types... create summary statistics... display these metrics updating in real-time"
  - Combines: cloning/multiple sprites, type differentiation, aggregation logic, real-time display
- **Recommendation**: SPLIT into:
  - **T28.G7.06.01**: "Create multiple agent instances"
    - Description: "Students clone their single agent to create 5 identical agents, each with independent random behavior. They verify all agents move independently."
    - Dependencies: T28.G7.01
  - **T28.G7.06.02**: "Track and display aggregate statistics"
    - Description: "Students calculate summary statistics (average position, count in each state) across all agents and display these values, updating them each time step."
    - Dependencies: T28.G7.06.01, T10.G6.01

---

### 6. GRADE-INAPPROPRIATE CONTENT

**ISSUE 6A: G2 skills not sufficiently unplugged**
- **Skills**: T28.G2.02, T28.G2.04
- **Problem**:
  - T28.G2.02: "physical or on-screen spinner template" - should be physical only
  - T28.G2.04: "five coin flips" - good, but doesn't specify physical
- **Recommendation**:
  - T28.G2.02: Change to "Learners use a physical spinner template or manipulate picture-based spinners (drag-and-drop), run 10 spins, and record tallies with stickers or pictographs"
  - T28.G2.04: Change to "Learners use physical coins or picture cards to make predictions before each of five trials"

**ISSUE 6B: K-2 violations - none found**
- All G2 skills appropriately use unplugged/picture-based approaches

**ISSUE 6C: G3+ coding requirement**
- **Problem**: T28.G3.05 (Describe randomness in games they play) is purely written/reflective, no coding
- **Severity**: Minor - this is a valuable conceptual skill that connects to real-world
- **Recommendation**: KEEP but add a coding component to the description:
  - Add: "Then create a simple CreatiCode project that demonstrates one source of randomness from their chosen game (e.g., a virtual die roller for Chutes and Ladders)."

---

### 7. CREATICODE FEATURE MISMATCHES

**ISSUE 7A: Random without repetition not scaffolded**
- **Finding**: Platform supports "pick random without repetition" but no skills explicitly teach this
- **Problem**: This is a powerful feature for realistic simulations (card draws, surveys)
- **Recommendation**: INSERT T28.G5.09: "Use random selection without repetition"
  - Description: "Students create a simulation that picks from a list without allowing repeats (e.g., dealing cards, selecting survey participants). They compare results to simulations where repetition is allowed and explain when each approach is appropriate."
  - Dependencies: T28.G4.02.01, T10.G3.03
  - Position: After T28.G5.07

**ISSUE 7B: Seed-setting introduced too late**
- **Skill**: T28.G6.02 (Use random seeds for reproducibility)
- **Problem**: Seeds are introduced in G6, but debugging skills in G4 would benefit from reproducible randomness
- **Recommendation**: MOVE seed introduction earlier
  - Keep T28.G6.02 for advanced reproducibility concepts
  - ADD T28.G4.07: "Use seeds to reproduce random sequences"
    - Description: "Students set a random seed value before running their simulation, observe the sequence of results, then reset to the same seed and verify they get identical results. They explain how this helps with debugging."
    - Dependencies: T28.G4.02.01
    - Position: After T28.G4.04

**ISSUE 7C: Statistical functions underutilized**
- **Finding**: Platform has avg, median, sum, min, max functions
- **Problem**: T28.G5.07 mentions median/mode but most skills only calculate percentages
- **Recommendation**: ENHANCE T28.G7.06.02 to explicitly use these functions:
  - Add to description: "...using CreatiCode's statistical functions (average, median, min, max) to compute summaries."

**ISSUE 7D: Charts underutilized in early grades**
- **Problem**: Bar charts mentioned in G3.01, G4.03, G5.07 but not taught systematically within T28
- **Dependencies**: All chart skills depend on T27 (Data Visualization)
- **Recommendation**: NO CHANGE - this is correct cross-topic dependency. T27 should own chart creation.

**ISSUE 7E: Tables vs Lists confusion**
- **Problem**: Some skills mention "tables" (T28.G3.03, T28.G6.01.02, T28.G7.02, T10.G6.01) but T28 dependencies mostly reference lists (T10.G3.03)
- **Finding**: CreatiCode supports both lists and tables
- **Recommendation**: CLARIFY when to use each:
  - Lists: single-column data (one result per trial)
  - Tables: multi-column data (trial number, result, timestamp, etc.)
  - UPDATE T28.G5.01.02 to use tables: "Students store data in a two-column table (sum, frequency)"

---

## MEDIUM PRIORITY ISSUES

### 8. VAGUE DESCRIPTIONS

**ISSUE 8A: T28.G3.01 lacks specificity**
- **Skill**: T28.G3.01 (Interpret provided simulation output)
- **Vague**: "answer questions about the resulting bar chart"
- **Better**: "answer specific questions: Which color appeared most often? Were any colors close in frequency? Did the counts change much between the first 10 and second 10 trials?"

**ISSUE 8B: T28.G5.04 too abstract**
- **Skill**: T28.G5.04 (Document simulation plans before coding)
- **Vague**: "outline question, inputs, random model, number of trials, and outputs"
- **Better**: "create a written plan using a template with sections: (1) Question to answer, (2) Random elements (what varies?), (3) How many trials?, (4) What data to collect, (5) How to analyze results. Students complete this template before coding their next simulation."

**ISSUE 8C: T28.G6.04 unclear application**
- **Skill**: T28.G6.04 (Simulate noisy sensors for T23 testing)
- **Vague**: "generate random-but-bounded pose or voice data"
- **Better**: "create a testing script that generates random pose coordinates (x, y) within realistic ranges (e.g., nose position between x:-100 to 100, y:-50 to 150) or volume values (0-100). They use these synthetic values to test their AI perception blocks when a camera/microphone isn't available."

**ISSUE 8D: T28.G7.02 passive tracing skill**
- **Skill**: T28.G7.02 (Trace how a simple agent learns from rewards)
- **Vague**: "answer questions about why the agent's path changes"
- **Better**: "observe a pre-built simulation where an agent's preference table updates based on rewards. Students complete a worksheet tracing: (1) initial preferences at each location, (2) what reward was received, (3) how the preference values changed, (4) how the agent's path differed in trial 1 vs trial 10."

**ISSUE 8E: T28.G7.05 lacks concrete deliverable**
- **Skill**: T28.G7.05 (Communicate simulation assumptions & limits)
- **Vague**: "write a short 'model card'"
- **Better**: "write a model card with specific sections: (1) Purpose: what question does this simulation answer? (2) Assumptions: list 2-3 things assumed to be true (e.g., 'weather stays the same each day', 'all players have equal skill'), (3) Limitations: identify 1-2 things the model doesn't include, (4) Appropriate use: when should/shouldn't someone rely on these results?"

**ISSUE 8F: T28.G8.01 extremely vague**
- **Skill**: T28.G8.01 (Chain simulation → analysis → dashboard)
- **Vague**: "automate simulations, store results, and auto-refresh charts/HUD elements so stakeholders can explore scenarios live"
- **Problem**: This is an entire capstone project, not a single skill
- **Better**: SPLIT or make concrete:
  - "Students create a dashboard that runs a simulation when a parameter is changed (using broadcast messages), automatically updates a table with results, and refreshes a bar chart showing the new data. They test the dashboard by changing 3 different parameter values and verifying the chart updates each time."

**ISSUE 8G: T28.G8.03 vague AI integration**
- **Skill**: T28.G8.03 (Integrate simulations into AI assistant workflows)
- **Vague**: "pass them to an AI assistant (like CreatiCode's XO), and evaluate whether the AI's recommendations align with the data"
- **Better**: "Students export their simulation summary (as formatted text including key statistics and a conclusion), paste it into CreatiCode's AI assistant as a prompt, and compare the AI's interpretation to their own analysis. They write 2-3 sentences explaining whether the AI correctly identified the main finding and if its suggested next steps make sense."

---

### 9. UNNECESSARY SAME-GRADE DEPENDENCIES

**ISSUE 9A: T28.G4.01 over-specified**
- **Skill**: T28.G4.01 (Build a simple random generator)
- **Dependencies**: T06.G3.01, T07.G3.05, T08.G3.01, T09.G3.05, T28.G3.02
- **Problem**: Lists T07.G3.05 and T09.G3.05 when the skill doesn't actually use loops or complex variable tracing
- **Recommendation**: REMOVE T07.G3.05, T09.G3.05
- **Keep**: T06.G3.01, T08.G3.01, T28.G3.02

**ISSUE 9B: T28.G4.03 over-specified**
- **Skill**: T28.G4.03 (Show how sample size changes variability)
- **Dependencies**: T07.G3.05, T08.G3.01, T09.G3.05, T28.G4.02, T27.G3.04
- **Problem**: T08.G3.01 and T09.G3.05 already assumed from T28.G4.02's dependencies
- **Recommendation**: REMOVE T08.G3.01, T09.G3.05 (redundant)
- **Keep**: T07.G3.05 (needed to change loop count), T28.G4.02, T27.G3.04

**ISSUE 9C: Multiple G6 skills list redundant dependencies**
- **Skills**: T28.G6.01, T28.G6.03
- **Pattern**: Both list T07.G5.01, T09.G4.04, T09.G5.01, T28.G5.04
- **Problem**: If T28.G5.04 already depends on variable skills, no need to re-list them
- **Recommendation**: Simplify to just list the highest-level T28 dependency
- **T28.G6.01.02**: Keep T28.G6.01.01, T07.G4.01 (for parameter sweeps)
- **T28.G6.03**: Keep T28.G5.01.02 (provides simulation capability)

**ISSUE 9D: T28.G7.01 redundant loop dependency**
- **Skill**: T28.G7.01 (Create a two-agent interaction simulation)
- **Dependencies**: T06.G5.01, T07.G6.05, T09.G5.01, T28.G6.08
- **Problem**: T07.G6.05 is oddly specific (fix a loop) when general loop skills assumed
- **Recommendation**: REMOVE T07.G6.05 (debugging skill, not prerequisite)
- **Keep**: T06.G5.01, T09.G5.01, T28.G6.08, ADD T07.G5.01 (general counting loop)

---

### 10. MISSING EXPLICIT SKILL COVERAGE

**ISSUE 10A: Conditional probability not covered**
- **Gap**: T28.G6.06 touches "changing probabilities" but doesn't teach conditional probability explicitly
- **Missing concept**: P(A|B) notation and interpretation
- **Recommendation**: This is borderline high-school math. For G6-8, the current T28.G6.06 (dependent events) is appropriate without formal notation
- **Action**: NO CHANGE, but enhance T28.G6.06 description to mention "dependent events" terminology

**ISSUE 10B: Expected value not taught**
- **Gap**: No skill teaches expected value calculation
- **Missing concept**: Students run simulations and compare to "what we'd expect on average"
- **Recommendation**: INSERT T28.G6.10: "Calculate and compare expected values"
  - Description: "Students calculate the expected value for a simple game (e.g., spinner where red gives 10 points, blue gives 5 points, each 50% likely: expected = 7.5 points). They run 100 simulations and compare the actual average to the expected value."
  - Dependencies: T28.G5.06, T27.G4.02c
  - Position: After T28.G6.03

**ISSUE 10C: Sampling bias not explicitly addressed**
- **Gap**: T28.G8.02 mentions sampling variation but not sampling bias
- **Missing concept**: How the method of sampling affects results (convenience vs random sampling)
- **Recommendation**: INSERT T28.G7.07: "Identify sources of sampling bias"
  - Description: "Students compare two data collection methods for the same question (e.g., surveying only students in one class vs random selection from whole school). They explain how each method might lead to biased results and which is more reliable."
  - Dependencies: T28.G5.02 (random assignment), T26 skills (survey design)
  - Position: After T28.G7.03

**ISSUE 10D: Confidence intervals missing**
- **Gap**: Advanced simulations estimate results but don't quantify uncertainty
- **Missing concept**: "We're confident the true value is between X and Y"
- **Recommendation**: TOO ADVANCED for G8. Current skills on variability (T28.G4.03, T28.G8.02) are sufficient.
- **Action**: NO CHANGE

**ISSUE 10E: Randomness in AI not connected**
- **Gap**: T28 teaches simulation and probability, T23 teaches AI, but connection is weak
- **Current**: T28.G6.04 mentions sensor testing, T28.G8.03 mentions AI assistant
- **Missing**: Understanding where randomness appears in AI systems (random initialization, dropout, data augmentation)
- **Recommendation**: ENHANCE T28.G7.03 to explicitly mention AI fairness testing
  - Add: "This synthetic testing approach is similar to how AI developers test their systems for fairness across different user groups before deployment."

**ISSUE 10F: Law of large numbers not explicit**
- **Gap**: T28.G4.03, T28.G5.06 show sample size effects but don't name the principle
- **Missing concept**: Explicit statement of law of large numbers
- **Recommendation**: ENHANCE T28.G5.06 description:
  - Add: "They explain the 'law of large numbers': as we run more trials, experimental results get closer to theoretical probability."

**ISSUE 10G: Gambler's fallacy not addressed**
- **Gap**: No skill explicitly teaches about independence of random events
- **Missing concept**: Past events don't affect future random outcomes
- **Recommendation**: INSERT T28.G5.10: "Test independence of random trials"
  - Description: "Students investigate whether previous outcomes affect future results. They run a coin-flip simulation, track whether 'heads follows heads' more often than expected by chance, and explain why each flip is independent (the coin has no memory)."
  - Dependencies: T28.G5.06
  - Position: After T28.G5.09

---

## SUMMARY STATISTICS

### Total Issues Found: 45

**HIGH PRIORITY: 24 issues**
- Duplicates/Redundancies: 2 (both resolved as appropriate)
- Dependency Violations: 1 (T28.G3.06 redundant dependency)
- X-2 Rule Violations: 0
- Missing Scaffolding: 5 gaps requiring new skills
- Skills Too Broad: 4 skills need splitting into sub-skills
- Grade-Inappropriate: 2 minor issues
- CreatiCode Feature Mismatches: 5 issues

**MEDIUM PRIORITY: 21 issues**
- Vague Descriptions: 8 skills need more specificity
- Unnecessary Same-Grade Dependencies: 4 skills over-specified
- Missing Explicit Coverage: 7 conceptual gaps

### New Skills Recommended: 15

**HIGH PRIORITY NEW SKILLS (9):**
1. T28.G3.07: Assemble a random generator from provided blocks
2. T28.G4.06: Interpret simple probabilities from familiar contexts
3. T28.G4.07: Use seeds to reproduce random sequences
4. T28.G5.08: Track a sprite's state across multiple events
5. T28.G5.09: Use random selection without repetition
6. T28.G5.10: Test independence of random trials
7. T28.G6.09: Create a simple two-sprite random interaction
8. T28.G6.10: Calculate and compare expected values
9. T28.G7.07: Identify sources of sampling bias

**SUB-SKILLS TO CREATE (6):**
10. T28.G4.02.01: Log trial results into a list
11. T28.G4.02.02: Count frequencies from a list
12. T28.G4.02.03: Calculate percentages from counts
13. T28.G5.01.01: Generate and sum two random values
14. T28.G5.01.02: Collect and analyze compound event data
15. T28.G6.01.01: Test multiple parameter values manually
16. T28.G6.01.02: Automate parameter sweeps with loops
17. T28.G7.06.01: Create multiple agent instances
18. T28.G7.06.02: Track and display aggregate statistics

### Skills Needing Revision: 12

**Description enhancements**: T28.G2.02, T28.G2.04, T28.G3.01, T28.G3.05, T28.G5.04, T28.G5.06, T28.G6.04, T28.G6.06, T28.G7.02, T28.G7.03, T28.G7.05, T28.G8.01, T28.G8.03

**Dependency fixes**: T28.G3.06, T28.G4.01, T28.G4.03, T28.G5.03, T28.G6.01, T28.G6.03, T28.G7.01

---

## PRIORITY RECOMMENDATIONS FOR IMPLEMENTATION

### Phase 1: Critical Fixes (Fix existing skills)
1. Fix T28.G3.06 redundant dependency
2. Enhance vague descriptions for G3.01, G5.04, G8.01
3. Simplify over-specified dependencies (T28.G4.01, G4.03, G6.01, G6.03, G7.01)

### Phase 2: Fill Scaffolding Gaps (Add new skills)
4. Add T28.G3.07 (assemble generator)
5. Add T28.G4.06 (interpret probabilities)
6. Add T28.G5.08 (state tracking)
7. Add T28.G6.09 (two-sprite interaction)

### Phase 3: Split Complex Skills (Create sub-skills)
8. Split T28.G4.02 into .01, .02, .03
9. Split T28.G5.01 into .01, .02
10. Split T28.G6.01 into .01, .02
11. Split T28.G7.06 into .01, .02

### Phase 4: Advanced Concepts (Add missing coverage)
12. Add T28.G4.07 (seeds for debugging)
13. Add T28.G5.09 (random without repetition)
14. Add T28.G5.10 (independence)
15. Add T28.G6.10 (expected value)
16. Add T28.G7.07 (sampling bias)

---

## COHERENCE ASSESSMENT

**Overall T28 Internal Coherence: GOOD with significant room for improvement**

**Strengths:**
- Clear progression from unplugged (G2) → observation (G3) → building (G4+)
- Appropriate scaffolding for basic random number generation
- Good integration of data collection and analysis
- Advanced skills connect to real-world applications (fairness testing, policy briefs)

**Weaknesses:**
- Several skills too broad and need decomposition
- Missing intermediate scaffolding steps (especially G3→G4, agent introduction)
- Vague descriptions in G7-G8 skills reduce assessability
- Some important probability concepts missing (expected value, independence, sampling bias)
- Redundant dependencies clutter skill specifications

**Cross-Topic Dependencies Look Reasonable:**
- T27 (Data Viz) for charts - appropriate
- T10 (Lists) for data structures - appropriate
- T07 (Loops) for repeated trials - appropriate
- T08 (Conditionals) for simulation logic - appropriate
- T09 (Variables) for tracking state - appropriate
- T23 (AI) for fairness testing - appropriate but underutilized

**Recommendation: Proceed with optimization following the 4-phase plan above.**
