# T28 (Chance & Simulations) Comprehensive Analysis
**Date**: 2025-11-25
**Lines**: 25457-26112 in /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md

## Executive Summary

This analysis examines all T28 skills (Grade 2-8) for:
1. Skills that are TOO BROAD and need breakdown
2. Dependency issues (circular, forward, missing intra-topic, X-2 violations)
3. Quality issues (vague descriptions, missing examples, grade level mismatches)
4. Missing skills (progression gaps)
5. CreatiCode block alignment

---

## 1. SKILLS THAT ARE TOO BROAD

### 1.1 T28.G3.05 - "Describe randomness in games and simulate a simple game element"

**Current Description**: "Learners pick a familiar board or card game (Chutes and Ladders, Candy Land, Go Fish) and identify where randomness happens (dice roll, card shuffle, spinner). They create a simple CreatiCode simulation of one random element from the game (e.g., a virtual die or spinner) and explain in writing how that randomness affects whether skill or luck determines the winner."

**Issues**:
- Combines THREE separate tasks: (1) analyzing a real game, (2) building a simulation, (3) writing an analysis of skill vs luck
- Requires both coding AND game theory understanding
- Too complex for a single 30-minute skill
- The "skill vs luck" analysis is philosophical and not well-scoped

**Suggested Breakdown**:
1. **T28.G3.05.01**: Identify sources of randomness in familiar games
   - Students examine 2-3 board/card games and list where randomness occurs (dice, spinners, card draws, shuffles)
   - Write 1-2 sentences per game explaining the random element
   - No coding required - pure analysis

2. **T28.G3.05.02**: Simulate a game's random element
   - Students choose one random element from a familiar game and create a CreatiCode simulation
   - Build a virtual die, spinner, or card drawer
   - Test to verify all outcomes can occur

3. **T28.G3.05.03**: Compare skill and luck in games (OPTIONAL - could move to later grade)
   - Students explain in writing how randomness affects game outcomes
   - Identify games that are mostly luck vs mostly skill
   - This might belong in G4 or G5 as it requires more abstract thinking

---

### 1.2 T28.G4.02.01, T28.G4.02.02, T28.G4.02.03 - "Log → Count → Calculate percentages"

**Current Structure**: Three skills that form a tightly coupled sequence

**Issues**:
- These are actually THREE PHASES of the same project
- Students need all three to get meaningful results
- The dependencies suggest they should be learned together
- Breaking them apart creates incomplete experiences

**Analysis**:
- **Keep as separate skills** - they teach distinct concepts:
  - G4.02.01: Using lists for data collection
  - G4.02.02: Counting with conditionals and loops
  - G4.02.03: Mathematical conversion (fractions → percentages)
- BUT clarify that they form a natural sequence for simulation analysis
- Consider adding a note: "This skill is part 1 of a 3-skill sequence for analyzing simulation results"

**Verdict**: KEEP SEPARATE but add sequence notes to help teachers understand the progression

---

### 1.3 T28.G5.01.01 + T28.G5.01.02 - "Generate compound event data + Analyze distributions"

**Current Structure**: Two-part skill for two-dice simulation

**Analysis**:
- G5.01.01: Generate data (technical skill - loops, lists, random)
- G5.01.02: Analyze why 7 is most common (conceptual understanding)
- These complement each other well
- Breaking them down further would make them too granular

**Verdict**: KEEP AS IS - good balance

---

### 1.4 T28.G7.06.01 + T28.G7.06.02 - "Multi-agent simulation + Aggregate metrics"

**Current Description**:
- G7.06.01: Create 5-10 agents with different types
- G7.06.02: Calculate summary statistics across agents

**Issues**:
- Creating 5-10 agents is a MASSIVE jump from previous skills (which use 1-2 agents)
- "Different types" is vague - what makes agents different?
- Aggregating metrics across 10 agents requires advanced list/table operations

**Suggested Breakdown**:
1. **T28.G7.06.01**: Extend two-agent simulation to 3-4 agents
   - Build on T28.G7.01 (two-agent interaction)
   - Add 1-2 more agents with similar behavior
   - Verify all agents function independently

2. **T28.G7.06.02**: Create agents with different behaviors
   - Some agents move fast, others slow
   - Some avoid others, some seek others
   - Test that behavioral differences produce different outcomes

3. **T28.G7.06.03**: Scale to 5-10 agents
   - Use cloning or loops to create multiple agents efficiently
   - Track which agent is which (numbering, naming)
   - Observe emergent patterns from many agents

4. **T28.G7.06.04**: Calculate aggregate metrics
   - Average position, total energy, state counts
   - Display real-time updates
   - This becomes the current G7.06.02

---

### 1.5 T28.G8.01 - "Chain simulation → analysis → dashboard"

**Current Description**: "Students build an automated pipeline that runs simulations with multiple parameter configurations, analyzes the results to identify patterns, and displays key findings in an interactive dashboard with auto-refreshing charts and summary statistics. Stakeholders can select different scenarios to explore results in real-time."

**Issues**:
- This is a CAPSTONE-level project with multiple complex systems
- "Interactive dashboard with auto-refreshing charts" is extremely advanced
- "Multiple parameter configurations" requires parameter sweep logic
- "Stakeholders can select different scenarios" implies UI design
- Would take hours/days, not 30 minutes

**Suggested Breakdown**:
1. **T28.G8.01.01**: Run simulation with 2-3 parameter values
   - Manual parameter changes between runs
   - Record results in a table
   - Compare outcomes visually

2. **T28.G8.01.02**: Automate parameter sweeps
   - Use loops to test multiple parameter values
   - Store results systematically
   - This already exists as T28.G6.01.02

3. **T28.G8.01.03**: Create static results dashboard
   - Display bar charts, summary statistics
   - Show results from parameter sweep
   - No interactivity yet

4. **T28.G8.01.04**: Add user input for scenario selection
   - Use "ask and wait" to let users choose scenarios
   - Display relevant data based on selection
   - This teaches basic interactivity

5. **T28.G8.01.05**: Create auto-refreshing dashboard (IF POSSIBLE)
   - Update charts while simulation runs
   - This requires advanced event handling
   - VERIFY: Can CreatiCode do this?

**Verdict**: BREAK DOWN - too complex as one skill

---

## 2. DEPENDENCY ISSUES

### 2.1 Circular/Forward Dependencies

**NONE FOUND** - All T28 skills properly depend on earlier T28 skills (no forward references)

---

### 2.2 X-2 Rule Violations

Checking all cross-topic dependencies for grade level violations:

#### T28.G4.01 Dependencies

**Issue**: Has 11 dependencies spanning G2-G3, creating complexity burden

Dependencies:
- T02.G2.01, T02.G2.02 (Pictures → labeled boxes) ← G2
- T04.G2.01, T04.G2.02, T04.G2.03 (Pattern recognition) ← G2
- T04.G3.02 (Match repeat box to code) ← G3
- T06.G2.01, T06.G2.02, T06.G2.03 (Cause-effect, if-then rules) ← G2
- T07.G2.01 (When to repeat) ← G2
- T08.G3.01 (Use simple if) ← G3
- T09.G3.05 (Trace variables) ← G3
- T28.G3.07 (Build random generator) ← G3

**Analysis**:
- Most dependencies are G2-G3 → G4 skill (OK by X-2 rule)
- BUT: Why does building a random generator with if-statements need picture-based sequencing skills (T02.G2.01)?
- Dependency bloat suggests the skill requirements aren't well-focused

**Recommendation**:
- Reduce to core dependencies: T08.G3.01 (if blocks), T28.G3.07 (basic random), T07.G2.01 (repeating)
- Remove the T02, T04, T06 picture-based dependencies (too far back, not directly relevant)

---

#### T28.G4.02.01 Dependencies

**Issue**: Similar bloat - 10 dependencies including T05 (design) skills

Dependencies include:
- T05.G3.01, T05.G3.02 (Design steps, user needs) ← Why?

**Analysis**:
- A skill about logging trial results to a list doesn't need user-centered design skills
- This appears to be dependency pollution

**Recommendation**:
- Remove T05 dependencies
- Keep: T07.G3.01 (loops), T10.G3.03 (list length), T28.G4.01 (previous skill)

---

#### T28.G5.08 - "Track agent state for probabilistic simulations"

**Current Dependencies**:
- T09.G4.04 (Variables for animation/game state) ← G4 → G5 ✓
- T09.G5.01 (Modify variables from input/sensors) ← G5 → G5 ✓
- T03.G3.01 (Navigate sprite with coordinates) ← **G3 → G5 VIOLATION** ✗
- T07.G3.01 (Counted repeat loop) ← **G3 → G5 VIOLATION** ✗
- T10.G3.05 (Loop through list items) ← **G3 → G5 VIOLATION** ✗

**Analysis**:
- X-2 rule: G5 skill can depend on G5, G4, or G3 skills ✓
- All dependencies are within allowed range
- **NO VIOLATION** - G3→G5 is exactly at the X-2 boundary

---

#### T28.G6.05 - "Model a simple agent in a grid world"

**Current Dependencies**:
- T28.G5.08 (Track position and state) ← references "for a single sprite"
- T28.G5.04 (Document simulation plans)

**Issue**: T28.G5.08's description says "track agent state for probabilistic simulations" and talks about maintaining x,y coordinates and state variables. This is essentially TEACHING agent basics.

Then T28.G6.05 says "create a sprite that tracks position and facing direction in a grid" - this is REPEATING the same concept.

**Analysis**:
- T28.G5.08 is misplaced - it's teaching G6 concepts in G5
- T28.G6.05 is redundant with T28.G5.08
- Need to clarify the distinction

**Recommendation**:
- **Remove T28.G5.08** or move it to G6
- OR: Clarify that G5.08 is about CONTINUOUS coordinates, G6.05 is about DISCRETE grid positions
- Update descriptions to make the distinction clear

---

### 2.3 Missing Intra-Topic Dependencies

Checking for skills that should depend on earlier T28 skills but don't:

#### T28.G4.05 - "Generate and plot random coordinate pairs"

**Current Dependencies**: T01.G2.01, T02.G2.01, T02.G2.02, T03.G3.01, T04.G3.02, T07.G2.01, T28.G4.02.01

**Missing**: Should depend on T28.G3.02 (explain what pick random does)

**Rationale**: Generating random coordinates requires using `pick random` twice (for x and y). Students should understand the pick random block before using it for coordinate generation.

**Recommendation**: Add dependency on T28.G3.02

---

#### T28.G4.06 - "Interpret probabilities as fractions and percentages"

**Current Dependencies**: T04.G3.02, T06.G2.03, T06.G3.01, T07.G2.01, T28.G4.02.03

**Analysis**: Currently depends on G4.02.03 (calculate percentages). This is correct - students first calculate percentages from simulation data, then learn to interpret theoretical probabilities.

**Status**: OK - no missing dependencies

---

#### T28.G4.07 - "Generate random selections without repetition"

**Current Dependencies**: T04.G3.02, T05.G3.01, T05.G3.02, T07.G2.01, T10.G3.03, T28.G4.02.01

**Missing**: Should depend on T28.G3.07 (build random generator) or T28.G4.01 (random with if-statements)

**Rationale**: This skill involves random selection, but doesn't depend on any skills about using randomness in CreatiCode. Students need to understand basic random generators first.

**Recommendation**: Add dependency on T28.G4.01

---

#### T28.G5.02 - "Randomly assign participants to conditions"

**Current Dependencies**: T28.G4.02.03, T28.G4.04, T09.G3.03

**Issue**: Dependencies listed as "T28.G4.02.03" without skill names

**Description**: "Students write a script that tags each simulated user as 'A' or 'B,' logs assignment, and reports counts to ensure near-equal groups."

**Missing**: Should depend on T28.G4.02.01 (logging to lists) since it mentions logging assignments

**Recommendation**: Add dependency on T28.G4.02.01

---

#### T28.G5.08 - "Track agent state for probabilistic simulations"

**Current Dependencies**: T09.G4.04, T09.G5.01, T03.G3.01, T07.G3.01, T10.G3.05

**Missing**: Should depend on some T28 skill about randomness, since it's for "probabilistic simulations"

**Recommendation**: Add dependency on T28.G5.05 or T28.G5.06 (probability concepts)

---

#### T28.G6.10 - "Compare sampling methods"

**Current Dependencies**: T28.G5.02, T28.G5.11

**Description**: "Students implement and compare three sampling methods to collect data from a simulated population: random sampling (pick any items), systematic sampling (every Nth item), and stratified sampling (ensure equal representation from subgroups)."

**Missing**: Should depend on T10 list skills for working with populations and sampling

**Recommendation**: Add dependencies on T10.G4.x skills for list manipulation

---

#### T28.G7.04 - "Compare shuffled results to real outcomes"

**Current Dependencies**: T28.G6.01.02, T09.G5.05

**Description**: "Students take experimental results (e.g., scores from two game versions), shuffle the labels randomly 100+ times..."

**Missing**: Should depend on a skill about shuffling lists! CreatiCode has `reshuffle [list] randomly`

**Recommendation**: Add dependency on T10.G4.15 (reshuffle list randomly)

---

### 2.4 Cross-Topic Dependency Preservation

**Status**: All cross-topic dependencies (to T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, etc.) are preserved.

**Recommendation**: While preserving them, we should AUDIT which ones are actually necessary (see section 2.2 about dependency bloat)

---

## 3. SKILL QUALITY ISSUES

### 3.1 Vague Descriptions

#### T28.G3.01 - "Interpret provided simulation output"

**Current**: "Students watch a pre-built CreatiCode project that runs 20 random trials and displays results in a bar chart. They answer specific questions: Which color appeared most often? Which appeared least? Did all colors appear the same number of times? They write 2-3 sentences explaining what the chart shows about randomness."

**Issue**: What kind of simulation? What colors? How many colors?

**Recommendation**: Add specificity: "Students watch a pre-built 3-color spinner simulation that runs 20 spins and displays results in a bar chart..."

---

#### T28.G5.08 - "Track agent state for probabilistic simulations"

**Current**: "Students create a sprite that represents an agent in a probabilistic simulation. The agent maintains its position using x,y coordinate variables and tracks one additional state variable that can change randomly or based on conditions (e.g., direction facing, energy level, or current mode)."

**Issues**:
- "One additional state variable" is vague - what should students choose?
- "Can change randomly or based on conditions" - which one? Both?
- Examples in parentheses don't clarify the core requirement

**Recommendation**: Provide a specific example scenario: "Students create a 'foraging ant' sprite that tracks its x,y position and an 'has_food' variable (true/false). The ant moves randomly until it reaches food coordinates, then sets has_food to true."

---

#### T28.G6.04 - "Simulate noisy sensors for AI perception testing"

**Current**: "Students generate synthetic sensor data with realistic variation (e.g., pose coordinates that vary within ±10 pixels, voice confidence scores between 0.7-0.95) to test AI perception logic without needing a live camera or microphone."

**Issues**:
- "Realistic variation" - what makes it realistic?
- Why ±10 pixels specifically?
- "Test AI perception logic" - what logic? This is T28 (Chance), not T22 (AI)

**Recommendation**:
- Clarify that this is about generating RANDOM DATA that mimics sensor noise
- Provide concrete scenario: "Students simulate a pose detection sensor by generating x,y coordinates for a body part that vary ±10 pixels around the true position using `pick random`. They create 50 data points and verify the spread matches expected sensor accuracy."
- Consider moving this skill to T22 (AI) if it's specifically about testing AI systems

---

### 3.2 Missing Concrete Examples

Many skills provide good examples. Issues found:

#### T28.G4.04 - "Debug an 'unfair' simulation"

**Current**: "Learners inspect a script where one outcome is favored (duplicate entries, wrong range) and fix it so outcomes are equally likely."

**Missing**: Specific example of what makes it unfair

**Recommendation**: Add example: "For instance, a 4-color spinner that uses 'pick random 1 to 5' and assigns 1→red, 2→red, 3→blue, 4→green, 5→yellow (red appears twice as often). Students identify and fix the error."

---

#### T28.G6.11 - "Calculate and interpret conditional probability"

**Current**: "Students calculate the probability of an event given that another event has occurred (e.g., probability of drawing a red marble given that the first marble was blue and not replaced)."

**Missing**: How to calculate this in CreatiCode

**Recommendation**: Add implementation detail: "Students run a simulation 1000 times, count cases where first marble is blue, and among those cases count how many times the second marble is red. They calculate conditional probability as (both events) / (first event)."

---

### 3.3 Grade Level Mismatches

#### K-2 Skills (Should be Picture-Based)

**T28.G2.01-04**: All use physical manipulatives or picture-based activities ✓ CORRECT

---

#### G3+ Skills (Should be Block-Based)

**Checking for skills that claim to use blocks but don't specify which blocks:**

**T28.G3.02**: "Explain what 'pick random' does" - Good, names specific block ✓

**T28.G3.03**: "drag a provided script" - Good, scaffolded approach ✓

**T28.G3.07**: "assembling a green flag script that uses 'pick random'" - Good ✓

**T28.G4.01**: "uses 'pick random 1-4' with if-statements" - Good ✓

**T28.G5.08**: Does NOT specify which blocks to use for "tracks its position using x,y coordinate variables" - should specify `set x to`, `set y to`, `create variable`, etc.

**T28.G6.02**: "populate a list with seeded random numbers using 'set [list] to (N) random numbers with seed (SEED)'" - Excellent block reference ✓

---

### 3.4 Duplicate/Overlapping Skills

#### T28.G5.08 vs T28.G6.05

**T28.G5.08**: "Track agent state for probabilistic simulations" - create sprite with x,y and one state variable

**T28.G6.05**: "Model a simple agent in a grid world" - create sprite with x,y and direction variable

**Overlap**: Both teach creating a sprite with position tracking and one additional state variable

**Distinction**:
- G5.08 is for CONTINUOUS coordinates and "probabilistic" (random) behavior
- G6.05 is for DISCRETE grid positions and directional movement

**Recommendation**:
- Clarify G5.08: "Track agent position in continuous coordinates (decimals allowed)"
- Clarify G6.05: "Track agent position in discrete grid squares (snap to grid)"
- Update G6.05 dependencies to explicitly build on G5.08

---

#### T28.G4.02.03 vs T28.G4.06

**T28.G4.02.03**: "Calculate percentages from frequency counts" - convert counts to percentages

**T28.G4.06**: "Interpret probabilities as fractions and percentages" - express likelihood as fractions AND percentages

**Overlap**: Both deal with percentages in probability

**Distinction**:
- G4.02.03 is about EXPERIMENTAL data (calculate % from simulation results)
- G4.06 is about THEORETICAL probability (express 1/4 as 25%)

**Recommendation**: Good separation - keep as is, but add clarifying note to G4.06: "This skill focuses on theoretical probability, while T28.G4.02.03 covered experimental percentages."

---

## 4. MISSING SKILLS

### 4.1 Progression Gaps

#### Gap: G3 → G4 Random Generator Complexity

**Current Path**:
- T28.G3.07: Build simple 2-3 outcome random generator
- T28.G4.01: Build random generator with if-statements for 4 outcomes

**Gap**: Jump from 2-3 outcomes to 4 outcomes + if-statements is significant

**Missing Skill**:
**T28.G3.08**: Build a 4-6 outcome random generator using multiple if-statements (without the number→meaning conversion complexity)

---

#### Gap: Understanding Lists Before Using Them for Trials

**Current Path**:
- T28.G4.01: Build random generator with if-statements
- T28.G4.02.01: Suddenly use lists to log 50 trial results

**Gap**: Students haven't been introduced to using lists for data collection in the T28 context

**Missing Skill**:
**T28.G4.01.05**: Log 5-10 trial results manually
- Students run their random generator 5-10 times
- They manually record results in a list using "add (result) to [trials]"
- They display the list and verify it contains all results
- This bridges the gap to automated trial logging

---

#### Gap: Single Random Value → Compound Events

**Current Path**:
- T28.G4.07: Generate random selections without repetition
- T28.G5.01.01: Generate compound event data (two dice)

**Gap**: Students go from simple random selection to rolling two dice and calculating sums - this is a conceptual leap

**Missing Skill**:
**T28.G4.08**: Generate simple paired random values
- Students create a script that generates two independent random values (e.g., two coin flips, rolling a die twice)
- They record both values and observe the variety of combinations
- This introduces the concept of independent random events before compound analysis

---

#### Gap: Observing Randomness → Understanding Probability Math

**Current Path**:
- T28.G4.06: Interpret probabilities as fractions/percentages (theoretical)
- T28.G5.05: Calculate theoretical probability for simple events

**Gap**: G4.06 says "interpret" but G5.05 is the first skill that teaches HOW to calculate

**Issue**: Students in G4.06 need to already understand theoretical probability to interpret it

**Recommendation**:
- Move T28.G5.05 (calculate theoretical probability) earlier → T28.G4.06.01
- Make current T28.G4.06 → T28.G4.06.02 (interpret after calculating)

---

### 4.2 Foundational Concepts Missing

#### Missing: Introduction to "Random Seed" Concept

**Current**: T28.G6.02 suddenly introduces seeded random numbers without preparation

**Missing Foundational Skill**:
**T28.G5.12**: Observe that random results differ each run
- Students run the same simulation 3 times and record results
- They observe that results are similar but not identical
- They write 1-2 sentences explaining why randomness produces different results
- This sets up the need for reproducibility (G6.02)

---

#### Missing: Understanding Sample Size Before Monte Carlo

**Current Path**:
- T28.G4.03: Show how sample size changes variability
- T28.G5.03: Use Monte Carlo to estimate area (advanced application)

**Gap**: T28.G4.03 shows sample size effects, but students need to understand WHY more samples = better estimates

**Missing Skill**:
**T28.G5.02.05**: Explain the relationship between sample size and accuracy
- Students run simulations with 10, 100, 1000 trials
- They calculate how far each estimate is from the theoretical probability
- They write an explanation of why larger samples give more accurate estimates
- This prepares for Monte Carlo's core insight

---

#### Missing: Introduction to "Simulation as Experimental Tool"

**Current**: Students jump into simulations without understanding WHY we simulate

**Missing Foundational Skill** (should be early G4 or late G3):
**T28.G3.09**: Explain why simulations are useful
- Students compare physical experiments (flipping coins 100 times) vs simulations (clicking green flag once)
- They identify advantages: speed, repeatability, testing scenarios that are impossible/expensive physically
- They write 2-3 sentences explaining when simulation is better than physical experiments

---

### 4.3 Missing CreatiCode-Specific Skills

#### Missing: Using "Reshuffle List Randomly" Block

**Available Block**: `reshuffle [list] randomly`

**Current Coverage**:
- T10.G4.15 teaches this in the Variables/Lists topic
- T28.G7.04 USES shuffling but doesn't teach it

**Missing**: No T28 skill demonstrates using reshuffle for probability experiments

**Recommendation**: Add skill:
**T28.G4.09**: Shuffle a list to randomize order
- Students create a list of items (cards, quiz questions, player names)
- They use `reshuffle [list] randomly` to randomize the order
- They run it multiple times and observe different orderings
- They explain use cases: shuffling decks, randomizing questions, mixing player order

---

#### Missing: Using "Insert N Random Items" Block

**Available Block**: `insert (N) [random] items from [list1] into [list2]`

**Current Coverage**:
- T10.G4.17 teaches this in Variables/Lists topic
- T28.G4.07 "Generate random selections without repetition" could use this block but doesn't mention it

**Recommendation**: Update T28.G4.07 to reference this block:
"Students use the `insert (N) [random] items from [list1] into [list2]` block to randomly select items without choosing the same item twice. They compare this to repeated random selection and verify no duplicates appear."

---

#### Missing: Using "Noise" Block for Procedural Generation

**Available Block**: `noise at x (X) y (Y) seed (SEED)`

**Current Coverage**: NONE in T28

**Use Case**: Perlin noise is fundamental to procedural terrain generation, organic-looking randomness, etc.

**Missing Skill** (Advanced G7 or G8):
**T28.G7.09**: Use noise functions for smooth random variation
- Students compare `pick random` (produces jumpy values) vs `noise at x y seed` (produces smooth variation)
- They create a terrain height map using noise
- They explain use cases: procedural terrain, natural-looking variation, game level generation

---

## 5. CREATICODE BLOCK ALIGNMENT

### 5.1 Available Blocks

Based on codebase search, CreatiCode provides:

1. **Basic Random**:
   - `pick random (MIN) to (MAX)` - Standard Scratch block ✓ CONFIRMED

2. **Random List Generation**:
   - `set [list] to (N) random whole numbers between (MIN) and (MAX) [repetition method]` ✓ CONFIRMED
   - `set [list] to (N) random numbers with seed (SEED)` ✓ CONFIRMED

3. **List Shuffling**:
   - `reshuffle [list] randomly` ✓ CONFIRMED
   - `reshuffle table [table] randomly` ✓ CONFIRMED

4. **Random Selection from Lists**:
   - `insert (N) [random] items from [list1] into [list2]` ✓ CONFIRMED
   - `pick random item from [list]` - Standard Scratch block ✓ CONFIRMED

5. **Noise Function**:
   - `noise at x (X) y (Y) seed (SEED)` ✓ CONFIRMED

---

### 5.2 Block Usage in T28 Skills

#### ✓ CORRECT Block References

- **T28.G3.02**: "pick random" ✓
- **T28.G3.07**: "pick random" + "say" ✓
- **T28.G4.01**: "pick random 1-4" with if-statements ✓
- **T28.G6.02**: "set [list] to (N) random numbers with seed (SEED)" ✓ EXCELLENT

---

#### ⚠️ MISSING Block References

- **T28.G4.02.01**: "appending each result to a list variable"
  - Should specify: `add (result) to [list]`

- **T28.G4.02.02**: "count how many times each outcome appears"
  - Should mention: `(result) = (color)` comparison, `change [count] by (1)`

- **T28.G4.05**: "generates random x and y coordinates"
  - Should specify: `pick random (min) to (max)` used twice

- **T28.G4.07**: "randomly selects items from a list without choosing the same item twice"
  - Should reference: `insert (N) [random] items from [list1] into [list2]` OR manual method with `delete (index) of [list]`

- **T28.G5.08**: "maintains its position using x,y coordinate variables"
  - Should specify: `set [x] to`, `set [y] to`, `change [x] by`

- **T28.G6.05**: "tracks its position and facing direction in a grid"
  - Should specify: `set [gridX] to`, `set [direction] to`, `point in direction (direction)`

- **T28.G7.04**: "shuffle the labels randomly 100+ times"
  - Should reference: `reshuffle [list] randomly` block

---

#### ❌ INCORRECT/UNCLEAR Block References

**None found** - all block references appear accurate

---

### 5.3 Blocks Mentioned but Not Taught in T28

| Block | Mentioned In | Taught In | Status |
|-------|-------------|-----------|--------|
| `reshuffle [list] randomly` | T28.G7.04 (uses it) | T10.G4.15 | ⚠️ Should add T10.G4.15 dependency |
| `insert (N) [random] items from [list1] into [list2]` | Could use in T28.G4.07 | T10.G4.17 | ⚠️ Should reference this block |
| `noise at x (X) y (Y) seed (SEED)` | Not mentioned in T28 | NOT TAUGHT | ❌ Missing skill |

---

### 5.4 Recommendations for Block Alignment

1. **Add explicit block syntax to all skills that use blocks**
   - Format: `blockname [param1] to (param2)`
   - Helps students find the correct block

2. **Add T28.G7.09** to teach noise function for procedural generation

3. **Update T28.G4.07** to reference `insert (N) [random] items` block

4. **Add T10 dependencies** where T28 skills use list operations taught in T10

5. **Create a "T28 Block Reference"** section at the start of the topic listing all random/probability blocks

---

## 6. SUMMARY OF ISSUES BY CATEGORY

### Critical Issues (Fix First)

1. **T28.G8.01** - Too broad, needs breakdown into 4-5 sub-skills
2. **T28.G7.06.01** - Jump from 2 to 5-10 agents too steep, needs intermediate steps
3. **T28.G3.05** - Combines analysis + coding + philosophy, needs breakdown
4. **Dependency bloat in G4 skills** - Remove unnecessary T02, T05 dependencies
5. **Missing T28.G3.08** - Gap between simple random generator and if-statement version

### Important Issues (Fix Soon)

6. **T28.G5.08 vs T28.G6.05** - Clarify distinction or merge
7. **Add T28.G4.01.05** - Bridge gap to using lists for trials
8. **Add T28.G4.08** - Teach compound random values before two-dice analysis
9. **Move T28.G5.05** earlier - Students need to calculate probability before interpreting it
10. **Add missing block references** - Specify exact blocks in skill descriptions

### Enhancement Issues (Nice to Have)

11. **Add T28.G3.09** - Explain why simulations are useful
12. **Add T28.G5.12** - Observe randomness varies between runs
13. **Add T28.G7.09** - Teach noise function for procedural generation
14. **Add T28.G4.09** - Use reshuffle block for probability experiments
15. **Create T28 Block Reference** - Quick guide to all random/probability blocks

---

## 7. DEPENDENCY GRAPH RECOMMENDATIONS

### Dependencies to REMOVE (Bloat)

From **T28.G4.01**:
- Remove: T02.G2.01, T02.G2.02 (picture sequencing not needed for random+if)
- Remove: T04.G2.01, T04.G2.02, T04.G2.03 (pattern recognition not needed)
- Remove: T06.G2.01, T06.G2.02 (cause-effect pictures not needed)
- Keep: T06.G2.03 (if-then game rules - relevant), T08.G3.01 (if blocks), T28.G3.07

From **T28.G4.02.01**:
- Remove: T05.G3.01, T05.G3.02 (design skills not needed for logging trials)
- Keep: T07.G3.01 (loops), T10.G3.03 (list length), T28.G4.01

From **T28.G4.02.02**:
- Remove: T05.G3.01, T05.G3.02 (design skills)
- Keep: T09.G3.05 (trace variables), T28.G4.02.01

---

### Dependencies to ADD

To **T28.G4.05** (random coordinates):
- Add: T28.G3.02 (understand pick random)

To **T28.G4.07** (random without repetition):
- Add: T28.G4.01 (basic random generator)
- Add: T10.G4.17 (insert random items block)

To **T28.G5.02** (assign to conditions):
- Add: T28.G4.02.01 (logging to lists)

To **T28.G5.08** (track agent state):
- Add: T28.G5.05 or T28.G5.06 (probability concepts, since it's for probabilistic sims)

To **T28.G6.10** (sampling methods):
- Add: T10.G4.x (list manipulation skills)

To **T28.G7.04** (shuffle comparison):
- Add: T10.G4.15 (reshuffle list randomly)

---

## 8. ACTIONABLE RECOMMENDATIONS

### Phase 1: Fix Critical Breaks (Priority 1)

1. **Break down T28.G8.01** into T28.G8.01.01 through T28.G8.01.05
2. **Break down T28.G3.05** into T28.G3.05.01, T28.G3.05.02, (T28.G3.05.03 optional)
3. **Break down T28.G7.06.01** into progression: 3-4 agents → different behaviors → 5-10 agents → aggregate metrics
4. **Clean up dependencies** in T28.G4.01, G4.02.01, G4.02.02 (remove T02, T05 bloat)

### Phase 2: Fill Critical Gaps (Priority 2)

5. **Add T28.G3.08**: Bridge gap from simple random to if-statement random
6. **Add T28.G4.01.05**: Teach manual trial logging before automated logging
7. **Add T28.G4.08**: Teach paired random values before compound events
8. **Reorganize G4.06/G5.05**: Move probability calculation before interpretation

### Phase 3: Improve Quality (Priority 3)

9. **Add specific examples** to vague skills (G3.01, G5.08, G6.04, G4.04)
10. **Add block syntax** to all skills that use blocks (G4.02.01, G4.02.02, G4.05, G4.07, G5.08, G6.05)
11. **Clarify G5.08 vs G6.05** distinction (continuous vs discrete coordinates)
12. **Update T28.G4.07** to reference `insert random items` block

### Phase 4: Enhance Coverage (Priority 4)

13. **Add T28.G3.09**: Explain why simulations are useful
14. **Add T28.G5.12**: Observe run-to-run variation
15. **Add T28.G7.09**: Teach noise function
16. **Add T28.G4.09**: Use reshuffle block
17. **Create T28 Block Reference Guide** at topic start

---

## APPENDIX: Complete Block Inventory

### Blocks Available in CreatiCode

| Block | Syntax | Used in T28? |
|-------|--------|--------------|
| Pick random | `pick random (MIN) to (MAX)` | ✓ Yes - G3.02, G3.07, G4.01 |
| Random list | `set [list] to (N) random whole numbers between (MIN) and (MAX) [method]` | ⚠️ Not explicitly taught |
| Seeded random | `set [list] to (N) random numbers with seed (SEED)` | ✓ Yes - G6.02 |
| Reshuffle list | `reshuffle [list] randomly` | ⚠️ Used (G7.04) but not taught |
| Reshuffle table | `reshuffle table [table] randomly` | ❌ No |
| Insert random | `insert (N) [random] items from [list1] into [list2]` | ⚠️ Should use in G4.07 |
| Noise function | `noise at x (X) y (Y) seed (SEED)` | ❌ No |
| Pick from list | `pick random item from [list]` | ⚠️ Assumed but not explicitly taught |

### Recommendations

1. **Teach all random blocks explicitly in T28 or verify they're taught in T10**
2. **Add skill for noise function** (procedural generation is important)
3. **Reference blocks by exact syntax** in skill descriptions
4. **Add cross-references** to T10 skills that teach list-based random operations

---

## CONCLUSION

The T28 skill progression has a strong foundation but suffers from:

1. **Scope creep** in advanced skills (G8 especially)
2. **Dependency bloat** from including unnecessary prerequisite skills
3. **Missing intermediate steps** in several progressions
4. **Block coverage gaps** for advanced random operations

The recommendations above provide a clear path to:
- Break down overly complex skills
- Clean up dependency trees
- Fill progression gaps
- Improve block alignment
- Enhance skill descriptions

Priority should be given to Phase 1 and 2 fixes, as these affect the teachability and learnability of the progression.
