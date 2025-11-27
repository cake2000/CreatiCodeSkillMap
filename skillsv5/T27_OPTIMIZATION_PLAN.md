# T27 (Chance & Simulations) - Optimization Plan

## Executive Summary

T27 currently has 63 skills spanning GK-G8, teaching chance, probability, and simulations. This plan identifies specific improvements to create a world-class curriculum that:
- Fixes vague verbs (replace "understand" with "Trace/Debug/Predict/Compare/Analyze/Design/Build")
- Ensures K-2 skills use concrete, picture-based scenarios
- Fills gaps in the K-8 progression
- Adds AI-era depth (fairness testing, bias analysis, statistical reasoning)
- Maintains IXL-style micro-progressions with auto-gradable activities

---

## Current State Analysis

### Grade Distribution
- **GK**: 3 skills (T27.GK.01-03) - Certain/impossible, maybe events, spinner games
- **G1**: 3 skills (T27.G1.01-03) - Coin flip recording, spinner comparison, likelihood sorting
- **G2**: 4 skills (T27.G2.01-04) - Certain/possible/impossible, experiments, fairness, prediction
- **G3**: 7 skills (T27.G3.01-07) - Reading simulation output, pick random block, first coded simulations
- **G4**: 7 main skills (T27.G4.01-07) with sub-skills - Mapping outcomes, logging, frequencies, debugging
- **G5**: 11 skills (T27.G5.01-11) with sub-skills - Compound events, theoretical probability, expected value
- **G6**: 11 skills (T27.G6.01-11) with sub-skills - Parameter testing, agents, sampling, conditional probability
- **G7**: 7 skills (T27.G7.01-07) with sub-skills - Multi-agent simulations, fairness testing, learning agents
- **G8**: 6 skills (T27.G8.01-06) - Pipelines, bootstrap sampling, AI integration, policy briefs

### Strengths
1. **Clear progression** from unplugged (K-2) to digital simulations (G3+)
2. **Concrete activities** with specific CreatiCode blocks referenced
3. **Real-world connections** (games, sensors, fairness, policy)
4. **Sub-skill structure** breaks complex topics into manageable steps
5. **Cross-topic integration** with T24 (data), T26 (charts), T21 (AI)

### Key Issues Identified

#### 1. VAGUE VERBS - CRITICAL FIXES NEEDED
**Current problems:**
- T27.GK.02: "**Identify** 'maybe' events" - passive recognition
- T27.G1.03: "**Sort** picture cards by likelihood" - OK but could be more active
- T27.G2.01: "**Classify** illustrated picture cards" - passive sorting
- T27.G3.01: "Read and **explain** simulation output" - OK but vague "explain"
- T27.G3.05: "**Classify** games by their random elements" - passive categorization
- T27.G5.10: "**Identify** independent events" - passive recognition
- T27.G8.05: "**Analyze** how environment design biases" - OK but vague

**Recommended verb replacements:**
- Replace "Identify" → **"Select"** or **"Match"** or **"Predict"** (more active)
- Replace "Classify" → **"Sort"** + verification test (e.g., "Sort and test")
- Replace "Explain" → **"Compare and describe"** or **"Predict then verify"**
- Replace vague "Analyze" → **"Trace and compare"** or **"Test and measure"**

#### 2. K-2 CONCRETE SCENARIOS - NEEDS ENHANCEMENT
**Current state:** K-2 skills use picture cards well, but some descriptions are wordy

**Opportunities:**
- Add more specific picture examples (not just "illustrated picture cards")
- Include exact number of cards/trials for consistency
- Add visual success criteria (e.g., "sort all 8 cards correctly")

#### 3. GAPS IN PROGRESSION

**Gap 1: G2→G3 transition too large**
- G2.04 ends with physical coin flips and manual recording
- G3.01 jumps to reading bar charts from CreatiCode simulations
- **MISSING:** Bridge activity to introduce the stage/sprite interface before reading charts

**Gap 2: Missing "probability as part of whole" concept (G4-G5)**
- G4 focuses on counting frequencies and percentages
- G5 introduces compound events and theoretical probability
- **MISSING:** Visual area models for probability (e.g., spinner divided into sections, fraction representations)

**Gap 3: No explicit coverage of permutations/combinations (G6-G7)**
- G5.01 introduces compound events (two dice)
- G6.06 covers dependent events (drawing without replacement)
- **MISSING:** Systematic counting of outcomes (tree diagrams, organized lists, combination formulas)

**Gap 4: Limited connection between simulation and prediction (G3-G4)**
- G3.04 asks students to predict before running
- G4.04 focuses on debugging unfair simulations
- **MISSING:** Skills that teach "designing fair games" from scratch using probability reasoning

**Gap 5: No coverage of random variables or distributions beyond histograms (G6-G7)**
- G5.07 creates frequency distributions
- G7.06.02 aggregates metrics
- **MISSING:** Explicit teaching of mean/variance of random variables, normal distribution introduction

#### 4. DUPLICATES OR OVERLAPS

**Overlap 1: Parameter testing appears twice**
- T27.G6.01.01: "Manually test parameters and log results"
- T27.G6.01.02: "Automate parameter sweeps with nested loops"
- **STATUS:** This is intentional progression (manual → automated). KEEP both.

**Overlap 2: Fairness appears in multiple places**
- T27.G2.03: "Decide if a simple game is fair" (spinners)
- T27.G4.04: "Debug an 'unfair' simulation"
- T27.G7.03: "Test for fairness using synthetic game testers"
- **STATUS:** These represent progression (intuitive → debugging → systematic testing). KEEP all.

**Overlap 3: Random generation appears multiple times**
- T27.G3.07: "Build a random number generator from scratch"
- T27.G4.01: "Map random numbers to named outcomes"
- **STATUS:** G3.07 is just numbers, G4.01 adds mapping. Good progression. KEEP both.

#### 5. SKILLS THAT ARE TOO BROAD

**Too Broad 1: T27.G5.04 - "Write a simulation plan before coding"**
- Lists 5 planning components
- Should be broken into: (1) Define question/variables, (2) Choose random model, (3) Set success criteria

**Too Broad 2: T27.G7.05 - "Write a model card documenting simulation assumptions"**
- Covers purpose, assumptions, limitations, stakeholders
- Should be broken into: (1) Document assumptions/limitations, (2) Identify affected stakeholders

**Too Broad 3: T27.G8.01 - "Build an automated simulation-to-dashboard pipeline"**
- Covers parameter sweep, data storage, analysis, visualization
- Should be broken into: (1) Automate data collection, (2) Build dashboard from simulation data

#### 6. AI-ERA DEPTH OPPORTUNITIES

**Current AI integration:**
- T27.G6.04: Simulate noisy sensors (good!)
- T27.G7.03: Test for fairness (good!)
- T27.G8.03: Integrate simulations into AI workflows (good!)
- T27.G8.05: Analyze environment design bias (good!)

**Missing opportunities:**
- **G5-G6:** No coverage of "training data" concept through simulation (e.g., generating synthetic datasets)
- **G7:** No explicit connection to how AI systems use probability (confidence scores, prediction intervals)
- **G8:** No coverage of Monte Carlo methods in AI (e.g., tree search in game AI, dropout in neural nets)

---

## Optimization Plan

### SECTION A: SKILLS TO MODIFY

#### A1. Fix Vague Verbs (7 skills)

**MODIFY: T27.GK.02**
```
CURRENT:
Skill: Identify "maybe" events using picture cards

REPLACE WITH:
Skill: Select "maybe" events from picture cards and test predictions
Description: Students examine 8 illustrated picture cards showing events. They **select** cards showing uncertain outcomes (will it rain today? will I pick a red crayon from a mixed box?) and place them in a "maybe" pile. Then they **test** one scenario (e.g., pick from a real crayon box 3 times) to observe that outcomes vary—reinforcing that "maybe" means "we don't know until we try."
```
**Rationale:** "Select" is more active than "Identify," and adding a test component makes it auto-gradable.

---

**MODIFY: T27.G2.01**
```
CURRENT:
Skill: Sort events into certain / possible / impossible

REPLACE WITH:
Skill: Sort picture cards into certain/possible/impossible and defend one choice
Description: Students **sort** 9 illustrated picture cards into three labeled bins: Certain (sun rising tomorrow), Possible (rolling a 3 on a die), Impossible (rolling a 7 on a six-sided die). After sorting, they **select** one card from each bin and **explain** their choice using the picture: "This card shows ____ and it goes in the ____ bin because ____." This adds a verification step beyond passive sorting.
```
**Rationale:** Adding "defend one choice" makes it more active and assessable.

---

**MODIFY: T27.G3.01**
```
CURRENT:
Skill: Read and explain simulation output from a bar chart

REPLACE WITH:
Skill: Compare simulation bar chart to predictions and identify differences
Description: Students receive a prediction worksheet: "If a fair 4-color spinner spins 20 times, about how many times will each color appear?" They write predictions (e.g., 5, 5, 5, 5). Then they run a pre-built CreatiCode simulation that displays results in a bar chart. They **compare** their predictions to the actual results and **calculate differences** for each color. They **describe** why results don't match perfectly: "Even with equal chances, results vary because of randomness."
```
**Rationale:** "Compare" + "calculate differences" is more active than "read and explain."

---

**MODIFY: T27.G3.05**
```
CURRENT:
Skill: Classify games by their random elements

REPLACE WITH:
Skill: Trace the role of randomness in a board game and predict impact
Description: Students select a familiar board game (Chutes and Ladders, Candy Land, Sorry!). They **trace** one game playthrough, noting each time a random element (die roll, spinner, card draw) affects the outcome. They **tally** how many decisions were player-controlled vs. random. Then they **predict**: "If we removed all random elements, would this game still be fun?" and **test** by playing a modified version. This moves from passive classification to active analysis.
```
**Rationale:** "Trace" and "predict impact" are more active than "classify."

---

**MODIFY: T27.G5.10**
```
CURRENT:
Skill: Identify independent events and the gambler's fallacy

REPLACE WITH:
Skill: Test independence by tracking streaks and predicting next outcomes
Description: Students run a coin flip simulation that tracks streaks (e.g., "HHHH = 4 heads in a row"). After observing a streak of 5 heads, they **predict**: "Is the next flip more likely to be tails?" Then they **test** by running 100 trials where this situation occurred and calculating: How often was the 6th flip tails? (Should be ~50%). They **compare** to the gambler's fallacy scenario: "Red came up 10 times at roulette, so black is due!" and **explain** why this reasoning is flawed using their simulation evidence.
```
**Rationale:** "Test" and "predict" are more active than "identify."

---

**MODIFY: T27.G8.05**
```
CURRENT:
Skill: Analyze how environment design biases agent behavior

REPLACE WITH:
Skill: Compare agent learning across two maze designs and measure bias
Description: Students run the same learning agent in two mazes: Maze A (one clear path) and Maze B (multiple paths, one much shorter). They **run** 50 trials in each maze and **record**: (1) average steps to goal, (2) most common path taken, (3) percentage of trials where shortest path was found. They **calculate** the "bias metric": (average steps - optimal steps) / optimal steps. They **compare** the two mazes and **explain**: "Maze B creates bias because early random success can lock in suboptimal paths." They **connect** to AI training: How does data environment create bias?
```
**Rationale:** "Compare and measure bias" with specific metrics is more concrete than vague "analyze."

---

**MODIFY: T27.G3.04 (minor enhancement)**
```
CURRENT:
Skill: Predict outcomes and compare to simulation results

ENHANCE TO:
Skill: Predict simulation outcomes, run trials, and calculate prediction error
Description: [Keep most of current description, but add at end:]
They **calculate** prediction error for each color using: |prediction - actual|. They **identify** which color had the largest error and **discuss**: "Was your prediction close? Why is it hard to predict exact results? Would 100 trials give a closer match?"
```
**Rationale:** Adding calculation makes it more rigorous.

---

#### A2. Enhance K-2 Concrete Scenarios (3 skills)

**MODIFY: T27.GK.01**
```
CURRENT:
Description: Students sort 6-8 illustrated picture cards...

ENHANCE TO:
Description: Students sort **8 illustrated picture cards** showing specific everyday events into two labeled bins:
- **"Will Happen"** (certain): Sun coming up tomorrow, a dropped ball falling down, ice melting in hot sun, a plant needing water to grow
- **"Won't Happen"** (impossible): Fish flying in the sky, ice staying frozen in hot sun, a person jumping to the moon without a rocket, water flowing uphill

After sorting, students **point to** one card from each bin and **say** why it goes there. This unplugged activity introduces that some events are predictable while others cannot occur. **Success criterion:** All 8 cards sorted correctly.
```
**Rationale:** Specific examples make it easier to implement and assess.

---

**MODIFY: T27.G1.01**
```
CURRENT:
Description: Students predict "heads" or "tails" before each flip by pointing to a picture card. After flipping a real coin, they place a sticker on a recording sheet under the matching picture (heads or tails). After 6 flips, they count stickers in each column and compare to their predictions.

ENHANCE TO:
Description: Students use a recording sheet with two columns showing **picture of a coin's head side** and **picture of a coin's tail side**. For each of 6 flips:
1. **Point** to their prediction (heads or tails picture)
2. **Flip** a real coin
3. **Place** a sticker in the column matching what came up

After 6 flips, they **count** stickers in each column and **compare**: "I predicted heads ___ times. Heads came up ___ times." They **circle** whether their predictions matched reality. This introduces recording random outcomes using concrete picture-based tools.

**Materials needed:** Recording sheet with 2 columns × 6 rows, coin pictures, 6 stickers per student.
```
**Rationale:** More explicit steps make implementation clearer.

---

**MODIFY: T27.G2.02**
```
CURRENT:
Description: Learners use a physical spinner (made with a pencil and paperclip on a paper circle) or draw from a bag of colored blocks...

ENHANCE TO:
Description: Learners conduct a concrete chance experiment using **one of these two setups**:

**Option A - Spinner:** Paper circle divided into 4 equal sections (red, blue, yellow, green) with pencil and paperclip spinner. Run **10 spins**.

**Option B - Block drawing:** Bag with 8 colored blocks (2 red, 2 blue, 2 yellow, 2 green). Draw one block, record color, return to bag. Run **10 draws**.

Recording: After each trial, make a **tally mark** under the matching color picture. After all 10 trials, **count** tally marks for each color and **identify**: Which color appeared most? Did all colors appear? Did any color appear zero times?

**Success criterion:** Complete 10 trials with tally marks in correct columns.
```
**Rationale:** Two specific setups make it easier for teachers to implement consistently.

---

#### A3. Fill Progression Gaps (Add Bridge Skills)

**NEW: T27.G2.05 (Bridge G2→G3)**
```
ID: T27.G2.05
Topic: T27 – Chance & Simulations
Skill: Watch a CreatiCode spinner simulation and match outcomes to pictures
Description: Students open a provided CreatiCode project showing a spinner sprite. When they **click the green flag**, the spinner rotates and stops on one of 4 colors. Students **run** the simulation 5 times and **match** each outcome to a picture chart by placing a check mark. This unplugged-to-plugged bridge introduces the CreatiCode stage interface and the concept that "spinning the spinner = clicking green flag" before they analyze data charts.

Dependencies:
* T27.G2.04: Predict and observe outcomes
* T06.G2.01: Click the green flag and observe what happens

---
INSERT POSITION: Between current T27.G2.04 and T27.G3.01
RATIONALE: G2 ends with physical experiments; G3.01 starts with reading bar charts. This bridges by introducing the simulation interface first.
```

---

**NEW: T27.G4.08 (Visual probability models)**
```
ID: T27.G4.08
Topic: T27 – Chance & Simulations
Skill: Draw area models to represent probability as part-of-whole
Description: Students create visual area models to represent probability before running simulations. For a 4-section spinner, they **draw** a circle divided into 4 equal parts and **label** each section 1/4 or 25%. For an unfair spinner (half red, quarter blue, quarter green), they **draw** sections sized proportionally and **label** 1/2, 1/4, 1/4. Then they **run** a CreatiCode simulation of each spinner (50 trials) and **compare**: Did results match the area fractions? This connects geometric reasoning to probability.

Dependencies:
* T27.G4.02.03: Calculate percentages from frequency counts
* T26.G4.04: Interpret circle graphs (pie charts)

---
INSERT POSITION: After T27.G4.07
RATIONALE: Fills gap between counting frequencies and theoretical probability by adding visual fraction models.
```

---

**NEW: T27.G6.12 (Combinations and permutations foundation)**
```
ID: T27.G6.12
Topic: T27 – Chance & Simulations
Skill: Generate all possible outcomes using organized lists and tree diagrams
Description: Students systematically list all outcomes for compound events. For flipping 2 coins: **create** organized list (HH, HT, TH, TT) and verify 4 outcomes. For rolling 2 dice: **start** a tree diagram (first die: 1,2,3,4,5,6; for each, second die: 1-6) and **calculate**: 6 × 6 = 36 outcomes. They **code** a simulation using nested loops to generate all pairs and **verify** their count. This introduces systematic counting before formal combinations.

Dependencies:
* T27.G5.01.01: Generate compound event data (two dice)
* T07.G5.01: Use nested loops for grid or matrix operations

---
INSERT POSITION: After T27.G6.11
RATIONALE: Fills gap between compound events (G5) and advanced simulations (G7) by teaching systematic outcome enumeration.
```

---

**NEW: T27.G5.12 (Mean and variance of random variables)**
```
ID: T27.G5.12
Topic: T27 – Chance & Simulations
Skill: Calculate the mean and spread of a random variable from simulation
Description: Students extend their dice simulation to calculate not just frequency but the **mean** and **variance** of outcomes. They **run** 1000 die rolls, **store** results in a list, and **calculate**: (1) Mean = sum of all rolls ÷ 1000, (2) Spread = largest - smallest, (3) Standard deviation (using CreatiCode's stats blocks). They **compare** to theoretical mean (3.5 for fair die) and **explain**: "The average of many rolls approaches the expected value." This introduces random variables as distributions.

Dependencies:
* T27.G5.09: Calculate expected value for simple scenarios
* T26.G5.01: Calculate mean from a dataset

---
INSERT POSITION: After T27.G5.11
RATIONALE: Bridges expected value (G5.09) and bootstrap sampling (G8.02) by explicitly teaching variance.
```

---

#### A4. Break Down Overly Broad Skills

**SPLIT: T27.G5.04 → Two skills**

**T27.G5.04.01: Define simulation question, variables, and trials**
```
ID: T27.G5.04.01
Topic: T27 – Chance & Simulations
Skill: Define simulation question, variables, and trials
Description: Before building a simulation, students write a planning document with 3 components:
1. **Question:** What am I trying to find out? (e.g., "How often does a team with 60% win rate win 3 games in a row?")
2. **Variables to track:** What will I measure? (e.g., wins, losses, streak length)
3. **Number of trials:** How many times will I run it? (At least 100 for stable results)

They **review** example plans and **identify** which are well-defined vs. vague. This prevents "just start coding" without clear goals.

Dependencies:
* T27.G4.03: Show how sample size changes variability
* T27.G4.04: Debug an "unfair" simulation
```

**T27.G5.04.02: Choose random model and define success criteria**
```
ID: T27.G5.04.02
Topic: T27 – Chance & Simulations
Skill: Choose random model and define success criteria
Description: Students extend their simulation plan by adding:
4. **Random model:** What will be random? How will I model it? (e.g., "Each game = pick random 1 to 100. If ≤ 60, team wins.")
5. **Success criteria:** How will I know my simulation works? (e.g., "Overall win rate should be close to 60%")

They **compare** two models for the same problem and **explain** which is more realistic. They **test** their success criterion after running the simulation.

Dependencies:
* T27.G5.04.01: Define simulation question, variables, and trials
* T05.G4.01: Describe what a simulation should do before building
```

---

**SPLIT: T27.G7.05 → Two skills**

**T27.G7.05.01: Document simulation assumptions and limitations**
```
ID: T27.G7.05.01
Topic: T27 – Chance & Simulations
Skill: Document simulation assumptions and limitations
Description: Students write documentation for their multi-agent simulation with:
1. **Purpose:** What question does it answer? (e.g., "Does adding walls change how long prey survive?")
2. **Assumptions:** What did we simplify? (e.g., "Agents can't see through walls," "All agents have equal speed," "Energy decreases at constant rate")
3. **Limitations:** What can't this simulation predict? (e.g., "Real animals can learn new strategies," "Doesn't model reproduction")

They **compare** their assumptions to reality and **identify** which simplifications might change results the most. This mirrors professional simulation documentation.

Dependencies:
* T27.G7.01: Create a two-agent interaction simulation
* T27.G7.03: Test for fairness using synthetic game testers
```

**T27.G7.05.02: Identify stakeholders affected by simulation-based decisions**
```
ID: T27.G7.05.02
Topic: T27 – Chance & Simulations
Skill: Identify stakeholders affected by simulation-based decisions
Description: Students analyze who might be affected if someone made decisions based on their simulation. They **list** 3-5 stakeholder groups and **describe** potential impacts. Example for school lunch line simulation:
- Students: Shorter wait times (positive)
- Cafeteria staff: Might need more training for new system (mixed)
- Students with disabilities: New system must accommodate wheelchair access (critical)

They **identify** groups that might be harmed and **propose** how to test for fairness across groups. This connects to ethical AI development.

Dependencies:
* T27.G7.05.01: Document simulation assumptions and limitations
* T32.G7.07: Identify stakeholders affected by a computing solution
```

---

**SPLIT: T27.G8.01 → Two skills**

**T27.G8.01.01: Automate data collection with parameter sweeps and logging**
```
ID: T27.G8.01.01
Topic: T27 – Chance & Simulations
Skill: Automate data collection with parameter sweeps and logging
Description: Students create an automated data collection system:
1. **Outer loop:** Repeat for each configuration (e.g., speed = 1, 2, 3, 4, 5)
2. **Inner loop:** For current config, run 50 trials
3. **Logging:** After each trial, add row to data table: [config, trial_number, outcome, score, timestamp]

After running, they **verify**: Data table should have 5 configs × 50 trials = 250 rows. They **export** data as CSV. This automates what was previously manual testing.

Dependencies:
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T27.G7.06.02: Aggregate metrics across multiple agents
```

**T27.G8.01.02: Build interactive dashboard from simulation data**
```
ID: T27.G8.01.02
Topic: T27 – Chance & Simulations
Skill: Build interactive dashboard from simulation data
Description: Students create a dashboard that displays simulation results:
1. **Summary view:** Bar chart comparing average score for each configuration
2. **Detail view:** When user clicks a config, show histogram of all 50 trial scores for that config
3. **Stats panel:** Display mean, median, range for selected config
4. **Update button:** "Run 50 more trials" button adds new data and updates all charts

This creates a professional-grade analytics interface for exploring simulation results.

Dependencies:
* T27.G8.01.01: Automate data collection with parameter sweeps and logging
* T26.G6.01: Calculate statistics (mean, median, mode, range)
* T06.G5.01: Broadcast a custom message and respond in another sprite
```

---

### SECTION B: NEW SKILLS TO ADD

#### B1. AI-Era Depth Skills

**NEW: T27.G5.13 (Training data generation)**
```
ID: T27.G5.13
Topic: T27 – Chance & Simulations
Skill: Generate synthetic training data with labeled examples
Description: Students generate synthetic datasets to understand AI training data. Example: Create 100 synthetic "fruit" examples with features [size, color, shape] and labels [apple/orange/banana]. They **code** rules: apples = [size: 5-8, color: red/green, shape: round], oranges = [size: 6-9, color: orange, shape: round], bananas = [size: 8-12, color: yellow, shape: curved]. They **generate** 100 random examples following these rules and **export** as training data. They **discuss**: How does training data quality affect AI?

Dependencies:
* T27.G5.01.01: Generate compound event data (two dice)
* T27.G4.02.01: Log trial results to a list
* T21.G4.01: Explain what "training data" means for AI models

---
INSERT POSITION: After T27.G5.12 (new skill from A3)
```

---

**NEW: T27.G7.08 (AI confidence scores)**
```
ID: T27.G7.08
Topic: T27 – Chance & Simulations
Skill: Simulate AI confidence scores and test decision thresholds
Description: Students simulate an AI vision system with confidence scores. Their simulation:
1. **Generates** 200 fake detections: object type (cat/dog/car) and confidence (0-100%)
2. **Applies** threshold rules: If confidence > 80%, accept; if 50-80%, "uncertain"; if < 50%, reject
3. **Tests** different thresholds (50%, 70%, 90%) and **calculates**: How many acceptances at each threshold?
4. **Analyzes** tradeoff: Higher threshold = fewer errors but also fewer detections

They **connect** to real AI: Self-driving cars must decide confidence threshold for detecting pedestrians.

Dependencies:
* T27.G6.04: Simulate noisy sensors for AI perception testing
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T21.G5.01: Make an XO model prediction and interpret results

---
INSERT POSITION: After T27.G7.07
```

---

**NEW: T27.G8.07 (Monte Carlo tree search intro)**
```
ID: T27.G8.07
Topic: T27 – Chance & Simulations
Skill: Compare random exploration vs. guided search in game trees
Description: Students explore how game AI uses simulation to make decisions. They build a simple game (tic-tac-toe or connect-4 simplified) and **compare** two move-selection strategies:

**Strategy A - Random:** For each possible move, simulate 10 random games and choose move with highest win rate.

**Strategy B - Guided:** For each possible move, simulate 10 games but favor moves that won previously (add weight to successful moves).

They **measure**: Win rate after 50 games for each strategy. They **connect** to real AI: AlphaGo uses Monte Carlo Tree Search with millions of simulations. This introduces how simulation powers AI decision-making.

Dependencies:
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T27.G7.02: Trace agent learning from rewards over trials
* T21.G7.01: Explain how AI makes decisions (classification, game playing)

---
INSERT POSITION: After T27.G8.06
```

---

#### B2. Assessment & Debugging Skills

**NEW: T27.G4.09 (Test simulation reliability)**
```
ID: T27.G4.09
Topic: T27 – Chance & Simulations
Skill: Test simulation reliability by running multiple times
Description: Students test whether their simulation gives consistent results. They **run** the same simulation (e.g., 100 coin flips) **5 separate times** without changing any code. They **record** the percentage of heads for each run (e.g., 48%, 52%, 49%, 51%, 50%). They **calculate** the range (52% - 48% = 4%) and **evaluate**: Is 4% range acceptable for 100 flips? They **predict**: Would 1000 flips have a smaller or larger range? Then **test** to verify.

Dependencies:
* T27.G4.03: Show how sample size changes variability
* T27.G4.04: Debug an "unfair" simulation

---
INSERT POSITION: After T27.G4.08 (new skill from A3)
```

---

**NEW: T27.G6.13 (Debug edge cases in simulations)**
```
ID: T27.G6.13
Topic: T27 – Chance & Simulations
Skill: Identify and fix edge-case bugs in simulations
Description: Students receive simulations with edge-case bugs (errors that only appear in rare situations):

**Bug 1:** Division by zero when no items in list (calculating average of empty list)
**Bug 2:** Index out of bounds when list becomes empty during random selection
**Bug 3:** Infinite loop when success condition is impossible (agent can't reach goal behind wall)

For each buggy simulation, they **identify** the edge case by reading code and **predict** when it will crash. They **test** by forcing the edge case (e.g., start with empty list). They **fix** using defensive checks (if length > 0 then...) and **verify** the fix works.

Dependencies:
* T27.G4.04: Debug an "unfair" simulation
* T12.G5.01: Use error messages to locate and fix bugs
* T08.G5.01: Use compound conditions (AND, OR, NOT)

---
INSERT POSITION: After T27.G6.12 (new skill from A3)
```

---

### SECTION C: SKILLS TO REMOVE OR MERGE

**NO SKILLS RECOMMENDED FOR REMOVAL.**

All current skills serve distinct purposes in the progression:
- K-2 unplugged activities build foundational intuition
- G3-4 bridge to digital simulations
- G5-6 add theoretical probability and agent modeling
- G7-8 cover advanced topics (multi-agent, fairness, AI integration)

The overlaps identified in Section "Issues → Duplicates" are intentional progressions, not true duplicates.

---

### SECTION D: DEPENDENCY FIXES (WITHIN T27 ONLY)

#### D1. Update Dependencies for Modified Skills

**UPDATE: T27.G3.01 dependencies** (skill modified in A1)
```
CURRENT:
* T27.G2.04: Predict and observe outcomes
* T26.G2.01: Read a picture graph (pictograph)

ADD NEW DEPENDENCY:
* T27.G2.05: Watch a CreatiCode spinner simulation and match outcomes to pictures [NEW SKILL]

FINAL:
* T27.G2.04: Predict and observe outcomes
* T27.G2.05: Watch a CreatiCode spinner simulation and match outcomes to pictures
* T26.G2.01: Read a picture graph (pictograph)
```

---

**UPDATE: T27.G5.05 dependencies** (to prepare for new skills)
```
CURRENT:
* T27.G4.06: Interpret probabilities as fractions and percentages

ADD:
* T27.G4.08: Draw area models to represent probability as part-of-whole [NEW SKILL]

FINAL:
* T27.G4.06: Interpret probabilities as fractions and percentages
* T27.G4.08: Draw area models to represent probability as part-of-whole
```

---

**UPDATE: T27.G7.05 dependencies** (since we split it)
```
OLD SKILL: T27.G7.05 will become T27.G7.05.01 + T27.G7.05.02

Any skill that previously depended on T27.G7.05 should now depend on BOTH:
* T27.G7.05.01: Document simulation assumptions and limitations
* T27.G7.05.02: Identify stakeholders affected by simulation-based decisions

AFFECTED SKILLS:
- T27.G8.01 → T27.G8.01.01
- T27.G8.03
- T27.G8.04

UPDATE each to list both new sub-skills.
```

---

**UPDATE: T27.G8.01 dependencies** (since we split it)
```
OLD SKILL: T27.G8.01 will become T27.G8.01.01 + T27.G8.01.02

Any skill that previously depended on T27.G8.01 should now depend on:
* T27.G8.01.02: Build interactive dashboard from simulation data [the comprehensive one]

AFFECTED SKILLS:
- T27.G8.03

UPDATE:
CURRENT: * T27.G8.01: Build an automated simulation-to-dashboard pipeline
CHANGE TO: * T27.G8.01.02: Build interactive dashboard from simulation data
```

---

#### D2. Add Missing Internal Dependencies

**UPDATE: T27.G6.04 dependencies**
```
CURRENT:
* T27.G5.03: Use Monte Carlo sampling to estimate area
* T27.G5.04: Write a simulation plan before coding

CHANGE TO (using new split skills):
* T27.G5.03: Use Monte Carlo sampling to estimate area
* T27.G5.04.01: Define simulation question, variables, and trials
```

---

**UPDATE: T27.G7.01 dependencies**
```
CURRENT:
* T27.G6.09: Create simple two-sprite interaction
* T27.G6.08: Implement reward rules and track outcomes

ADD MISSING:
* T27.G5.08: Track agent state for probabilistic simulations [should have been there]

FINAL:
* T27.G5.08: Track agent state for probabilistic simulations
* T27.G6.08: Implement reward rules and track outcomes
* T27.G6.09: Create simple two-sprite interaction
```

---

**UPDATE: T27.G8.02 dependencies**
```
CURRENT:
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T27.G7.04: Perform permutation tests
* T26.G6.01: Calculate statistics (mean, median, mode, range)

ADD MISSING:
* T27.G5.12: Calculate the mean and spread of a random variable [NEW, should be prerequisite]

FINAL:
* T27.G5.12: Calculate the mean and spread of a random variable from simulation
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T27.G7.04: Perform permutation tests
* T26.G6.01: Calculate statistics (mean, median, mode, range)
```

---

### SECTION E: UPDATED SKILL COUNT SUMMARY

#### Current: 63 skills
- GK: 3
- G1: 3
- G2: 4
- G3: 7
- G4: 7 (with sub-skills counted separately)
- G5: 11
- G6: 11
- G7: 7
- G8: 6

#### After Optimization: 78 skills

**Grade-by-grade breakdown:**

**GK: 3 skills** (no change)
- GK.01 (modified)
- GK.02 (modified)
- GK.03

**G1: 3 skills** (no change)
- G1.01 (modified)
- G1.02
- G1.03

**G2: 5 skills** (+1)
- G2.01 (modified)
- G2.02 (modified)
- G2.03
- G2.04
- **G2.05 [NEW]** - Watch CreatiCode spinner (bridge skill)

**G3: 7 skills** (no change)
- G3.01 (modified)
- G3.02
- G3.03
- G3.04 (modified)
- G3.05 (modified)
- G3.06
- G3.07

**G4: 9 skills** (+2)
- G4.01
- G4.02.01
- G4.02.02
- G4.02.03
- G4.03
- G4.04
- G4.05
- G4.06
- G4.07
- **G4.08 [NEW]** - Area models for probability
- **G4.09 [NEW]** - Test simulation reliability

**G5: 14 skills** (+3)
- G5.01.01
- G5.01.02
- G5.02
- G5.03
- G5.04.01 [SPLIT from G5.04]
- G5.04.02 [SPLIT from G5.04]
- G5.05
- G5.06
- G5.07
- G5.08
- G5.09
- G5.10 (modified)
- G5.11
- **G5.12 [NEW]** - Mean and variance of random variables
- **G5.13 [NEW]** - Generate synthetic training data

**G6: 13 skills** (+2)
- G6.01.01
- G6.01.02
- G6.02
- G6.03
- G6.04
- G6.05
- G6.06
- G6.07
- G6.08
- G6.09
- G6.10
- G6.11
- **G6.12 [NEW]** - Generate outcomes with organized lists/tree diagrams
- **G6.13 [NEW]** - Debug edge-case bugs

**G7: 9 skills** (+2)
- G7.01
- G7.02
- G7.03
- G7.04
- G7.05.01 [SPLIT from G7.05] - Document assumptions/limitations
- G7.05.02 [SPLIT from G7.05] - Identify stakeholders
- G7.06.01
- G7.06.02
- G7.07
- **G7.08 [NEW]** - AI confidence scores

**G8: 8 skills** (+2)
- G8.01.01 [SPLIT from G8.01] - Automate data collection
- G8.01.02 [SPLIT from G8.01] - Build dashboard
- G8.02
- G8.03
- G8.04
- G8.05 (modified)
- G8.06
- **G8.07 [NEW]** - Monte Carlo tree search intro

---

### SECTION F: IMPLEMENTATION PRIORITIES

#### Phase 1: Critical Fixes (Do First)
1. **Fix vague verbs** (A1) - 7 skills modified
2. **Add G2.05 bridge skill** (A3) - Critical for G2→G3 transition
3. **Update dependencies** for modified skills (D1)

**Estimated effort:** 2-3 hours for content editing + testing

---

#### Phase 2: Fill Progression Gaps (Do Second)
1. **Add G4.08** (Area models) - Fills conceptual gap
2. **Add G5.12** (Mean/variance) - Essential for G8 bootstrap
3. **Add G6.12** (Combinations) - Fills systematic counting gap
4. **Split G5.04** into two sub-skills (A4)
5. **Update dependencies** (D2)

**Estimated effort:** 4-5 hours for content development

---

#### Phase 3: AI-Era Enhancements (Do Third)
1. **Add G5.13** (Synthetic training data)
2. **Add G7.08** (AI confidence scores)
3. **Add G8.07** (Monte Carlo tree search)
4. **Enhance K-2 descriptions** (A2) - 3 skills

**Estimated effort:** 3-4 hours

---

#### Phase 4: Advanced Improvements (Optional)
1. **Split G7.05** into two sub-skills (A4)
2. **Split G8.01** into two sub-skills (A4)
3. **Add G4.09** (Test reliability)
4. **Add G6.13** (Debug edge cases)
5. **Final dependency review**

**Estimated effort:** 3-4 hours

---

### SECTION G: VERIFICATION CHECKLIST

After implementing changes, verify:

#### Content Quality
- [ ] All skills use active verbs (Trace, Debug, Predict, Compare, Build, Test, Calculate)
- [ ] K-2 skills have specific picture examples and material lists
- [ ] G3-8 skills reference specific CreatiCode blocks
- [ ] All descriptions include clear success criteria
- [ ] No skill uses vague "understand" or passive "identify"

#### Progression Logic
- [ ] Each skill builds on prerequisites (test by trying to complete without doing dependencies first)
- [ ] No sudden jumps in complexity (K-2 → G3 bridge via G2.05)
- [ ] Sub-skills progress from simple to complex (e.g., G5.04.01 before G5.04.02)
- [ ] Grade-level alignment matches typical student readiness

#### Dependencies
- [ ] All T27 internal dependencies point to existing skills
- [ ] Split skills updated everywhere (old skill ID → new sub-skill IDs)
- [ ] Cross-topic dependencies preserved exactly (T24, T26, T21, T09, T10, etc.)
- [ ] No circular dependencies (A depends on B, B depends on A)

#### AI-Era Readiness
- [ ] At least 3 skills connect to AI concepts (training data, confidence scores, tree search) ✓
- [ ] At least 2 skills address fairness/bias (G7.03, G7.07, G8.05) ✓
- [ ] At least 1 skill addresses ethics/stakeholders (G7.05.02, G8.04) ✓
- [ ] Skills prepare for AI interpretation, not just coding (G8.03) ✓

#### IXL-Style Quality
- [ ] Auto-gradable activities (sorting cards → specific number correct)
- [ ] Immediate feedback opportunities (run simulation → compare to prediction)
- [ ] Micro-progressions (no skill covers more than one concept)
- [ ] Clear, measurable outcomes (not vague "appreciate" or "explore")

---

## Summary of Changes

### Modifications: 13 skills edited
- T27.GK.01, GK.02 (enhanced K-2 scenarios)
- T27.G1.01 (enhanced K-2 scenarios)
- T27.G2.01, G2.02 (fixed vague verbs + enhanced)
- T27.G3.01, G3.04, G3.05 (fixed vague verbs)
- T27.G5.04 → split into G5.04.01 + G5.04.02
- T27.G5.10 (fixed vague verbs)
- T27.G7.05 → split into G7.05.01 + G7.05.02
- T27.G8.01 → split into G8.01.01 + G8.01.02
- T27.G8.05 (fixed vague verbs)

### Additions: 11 new skills
- T27.G2.05 (bridge skill)
- T27.G4.08 (area models)
- T27.G4.09 (test reliability)
- T27.G5.12 (mean/variance)
- T27.G5.13 (training data)
- T27.G6.12 (combinations)
- T27.G6.13 (edge cases)
- T27.G7.08 (AI confidence)
- T27.G8.07 (Monte Carlo)
- Plus 4 sub-skills from splits (G5.04.01/02, G7.05.01/02, G8.01.01/02)

### Removals: 0 skills deleted

### Net Change: +15 skills (63 → 78)

---

## Conclusion

This optimization plan transforms T27 from a solid curriculum into a world-class, AI-era ready progression by:

1. **Eliminating vague language** - All verbs are now active and assessable
2. **Strengthening K-2 foundation** - Concrete materials, specific examples, clear success criteria
3. **Filling progression gaps** - Bridge skills ensure smooth transitions
4. **Adding AI-era depth** - Training data, confidence scores, Monte Carlo methods, fairness testing
5. **Maintaining IXL quality** - Micro-progressions, auto-gradable, immediate feedback

The updated T27 now provides 78 carefully sequenced skills that take students from concrete picture-based probability (GK) to professional-grade simulation pipelines and AI integration (G8), with no gaps and no vague outcomes.

**Ready for implementation in phases as outlined in Section F.**
