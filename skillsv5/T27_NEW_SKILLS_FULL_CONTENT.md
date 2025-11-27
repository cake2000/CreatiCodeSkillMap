# T27 Optimization - Complete New Skills Content

This document contains the full content for all NEW skills to be added to T27 (Chance & Simulations). Modified skills are documented separately in the optimization plan.

---

## NEW SKILL 1: T27.G2.05 (Bridge Skill)

```
ID: T27.G2.05
Topic: T27 – Chance & Simulations
Skill: Watch a CreatiCode spinner simulation and match outcomes to pictures
Description: Students open a provided CreatiCode project showing a spinner sprite. When they click the green flag, the spinner rotates and stops on one of 4 colors. Students run the simulation 5 times and match each outcome to a picture chart by placing a check mark. This unplugged-to-plugged bridge introduces the CreatiCode stage interface and the concept that "spinning the spinner = clicking green flag" before they analyze data charts.

Dependencies:
* T27.G2.04: Predict and observe outcomes
* T06.G2.01: Click the green flag and observe what happens
```

**Rationale:** Critical bridge between physical experiments (G2) and digital simulations with data analysis (G3).

**Implementation Notes:**
- Provide starter project with spinner costume and simple rotation animation
- Create printable chart with 5 rows and 4 color columns for check marks
- Success criterion: All 5 outcomes correctly matched

---

## NEW SKILL 2: T27.G4.08 (Visual Probability Models)

```
ID: T27.G4.08
Topic: T27 – Chance & Simulations
Skill: Draw area models to represent probability as part-of-whole
Description: Students create visual area models to represent probability before running simulations. For a 4-section spinner, they draw a circle divided into 4 equal parts and label each section 1/4 or 25%. For an unfair spinner (half red, quarter blue, quarter green), they draw sections sized proportionally and label 1/2, 1/4, 1/4. Then they run a CreatiCode simulation of each spinner (50 trials) and compare: Did results match the area fractions? This connects geometric reasoning to probability.

Dependencies:
* T27.G4.02.03: Calculate percentages from frequency counts
* T26.G4.04: Interpret circle graphs (pie charts)
```

**Rationale:** Fills gap between counting frequencies and theoretical probability by adding visual fraction models.

**Implementation Notes:**
- Provide circle templates (blank circles for drawing)
- Provide two spinner simulations (fair 4-way, unfair with 1/2, 1/4, 1/4)
- Success criterion: Drawings labeled correctly, simulation results within 10% of theoretical

---

## NEW SKILL 3: T27.G4.09 (Test Reliability)

```
ID: T27.G4.09
Topic: T27 – Chance & Simulations
Skill: Test simulation reliability by running multiple times
Description: Students test whether their simulation gives consistent results. They run the same simulation (e.g., 100 coin flips) 5 separate times without changing any code. They record the percentage of heads for each run (e.g., 48%, 52%, 49%, 51%, 50%). They calculate the range (52% - 48% = 4%) and evaluate: Is 4% range acceptable for 100 flips? They predict: Would 1000 flips have a smaller or larger range? Then test to verify.

Dependencies:
* T27.G4.03: Show how sample size changes variability
* T27.G4.04: Debug an "unfair" simulation
```

**Rationale:** Teaches students that randomness means results vary, and how to quantify that variation.

**Implementation Notes:**
- Provide recording sheet with 5 rows for trial results
- Teach range calculation: max - min
- Extension: Compare range for 100 vs 1000 trials
- Success criterion: Complete 5 runs, calculate range correctly, make valid prediction

---

## NEW SKILL 4: T27.G5.12 (Random Variable Statistics)

```
ID: T27.G5.12
Topic: T27 – Chance & Simulations
Skill: Calculate the mean and spread of a random variable from simulation
Description: Students extend their dice simulation to calculate not just frequency but the mean and variance of outcomes. They run 1000 die rolls, store results in a list, and calculate: (1) Mean = sum of all rolls ÷ 1000, (2) Spread = largest - smallest, (3) Standard deviation (using CreatiCode's stats blocks). They compare to theoretical mean (3.5 for fair die) and explain: "The average of many rolls approaches the expected value." This introduces random variables as distributions.

Dependencies:
* T27.G5.09: Calculate expected value for simple scenarios
* T26.G5.01: Calculate mean from a dataset
```

**Rationale:** Bridges expected value (G5.09) and bootstrap sampling (G8.02) by explicitly teaching variance.

**Implementation Notes:**
- Use CreatiCode's list operations: sum, length, min, max
- Optional: Use stats blocks for standard deviation (or calculate manually)
- Compare to theoretical: E(die) = 3.5, range = 1 to 6
- Success criterion: Mean within 0.2 of 3.5 for 1000 rolls, spread correctly calculated

---

## NEW SKILL 5: T27.G5.13 (Synthetic Training Data)

```
ID: T27.G5.13
Topic: T27 – Chance & Simulations
Skill: Generate synthetic training data with labeled examples
Description: Students generate synthetic datasets to understand AI training data. Example: Create 100 synthetic "fruit" examples with features [size, color, shape] and labels [apple/orange/banana]. They code rules: apples = [size: 5-8, color: red/green, shape: round], oranges = [size: 6-9, color: orange, shape: round], bananas = [size: 8-12, color: yellow, shape: curved]. They generate 100 random examples following these rules and export as training data. They discuss: How does training data quality affect AI?

Dependencies:
* T27.G5.01.01: Generate compound event data (two dice)
* T27.G4.02.01: Log trial results to a list
* T21.G4.01: Explain what "training data" means for AI models
```

**Rationale:** Connects simulations to AI training, teaches that training data can be synthesized with specific distributions.

**Implementation Notes:**
- Use nested lists or table format: [[size, color, shape, label], ...]
- Generate using pick random for size, random selection from color list
- Export as CSV or display in table format
- Discussion questions: What if we made apples too big? What if colors overlapped?
- Success criterion: 100 examples generated, all follow rules, export successful

---

## NEW SKILL 6: T27.G6.12 (Combinations Foundation)

```
ID: T27.G6.12
Topic: T27 – Chance & Simulations
Skill: Generate all possible outcomes using organized lists and tree diagrams
Description: Students systematically list all outcomes for compound events. For flipping 2 coins: create organized list (HH, HT, TH, TT) and verify 4 outcomes. For rolling 2 dice: start a tree diagram (first die: 1,2,3,4,5,6; for each, second die: 1-6) and calculate: 6 × 6 = 36 outcomes. They code a simulation using nested loops to generate all pairs and verify their count. This introduces systematic counting before formal combinations.

Dependencies:
* T27.G5.01.01: Generate compound event data (two dice)
* T07.G5.01: Use nested loops for grid or matrix operations
```

**Rationale:** Fills gap between compound events and advanced simulations by teaching systematic outcome enumeration.

**Implementation Notes:**
- Provide tree diagram template
- Code structure: repeat 6 (first die) → repeat 6 (second die) → add [die1, die2] to list
- Verify: length of list should be 36
- Extension: How many outcomes for 3 coins? (8)
- Success criterion: Organized list complete, tree diagram started, code generates all 36 pairs

---

## NEW SKILL 7: T27.G6.13 (Edge Case Debugging)

```
ID: T27.G6.13
Topic: T27 – Chance & Simulations
Skill: Identify and fix edge-case bugs in simulations
Description: Students receive simulations with edge-case bugs (errors that only appear in rare situations):

Bug 1: Division by zero when no items in list (calculating average of empty list)
Bug 2: Index out of bounds when list becomes empty during random selection
Bug 3: Infinite loop when success condition is impossible (agent can't reach goal behind wall)

For each buggy simulation, they identify the edge case by reading code and predict when it will crash. They test by forcing the edge case (e.g., start with empty list). They fix using defensive checks (if length > 0 then...) and verify the fix works.

Dependencies:
* T27.G4.04: Debug an "unfair" simulation
* T12.G5.01: Use error messages to locate and fix bugs
* T08.G5.01: Use compound conditions (AND, OR, NOT)
```

**Rationale:** Teaches defensive programming and edge case thinking critical for robust simulations.

**Implementation Notes:**
- Provide 3 buggy starter projects (one for each bug type)
- Bug 1: set average to sum / length (fails when length = 0)
- Bug 2: set item to item (pick random 1 to length of list) (fails when list empty)
- Bug 3: repeat until touching goal (fails when goal unreachable)
- Success criterion: All 3 bugs identified, fixed, and verified with test cases

---

## NEW SKILL 8: T27.G7.08 (AI Confidence Scores)

```
ID: T27.G7.08
Topic: T27 – Chance & Simulations
Skill: Simulate AI confidence scores and test decision thresholds
Description: Students simulate an AI vision system with confidence scores. Their simulation:
1. Generates 200 fake detections: object type (cat/dog/car) and confidence (0-100%)
2. Applies threshold rules: If confidence > 80%, accept; if 50-80%, "uncertain"; if < 50%, reject
3. Tests different thresholds (50%, 70%, 90%) and calculates: How many acceptances at each threshold?
4. Analyzes tradeoff: Higher threshold = fewer errors but also fewer detections

They connect to real AI: Self-driving cars must decide confidence threshold for detecting pedestrians.

Dependencies:
* T27.G6.04: Simulate noisy sensors for AI perception testing
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T21.G5.01: Make an XO model prediction and interpret results
```

**Rationale:** Connects simulations to real AI systems, teaches that confidence scores aren't binary.

**Implementation Notes:**
- Generate detections: type = pick random item from [cat, dog, car], confidence = pick random 0 to 100
- Store as nested list: [[type, confidence], ...]
- For each threshold, count acceptances
- Create bar chart: threshold on x-axis, acceptances on y-axis
- Discussion: Self-driving cars—prioritize safety (high threshold) or utility (low threshold)?
- Success criterion: 200 detections generated, 3 thresholds tested, tradeoff explained

---

## NEW SKILL 9: T27.G8.07 (Monte Carlo Tree Search)

```
ID: T27.G8.07
Topic: T27 – Chance & Simulations
Skill: Compare random exploration vs. guided search in game trees
Description: Students explore how game AI uses simulation to make decisions. They build a simple game (tic-tac-toe or connect-4 simplified) and compare two move-selection strategies:

Strategy A - Random: For each possible move, simulate 10 random games and choose move with highest win rate.

Strategy B - Guided: For each possible move, simulate 10 games but favor moves that won previously (add weight to successful moves).

They measure: Win rate after 50 games for each strategy. They connect to real AI: AlphaGo uses Monte Carlo Tree Search with millions of simulations. This introduces how simulation powers AI decision-making.

Dependencies:
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T27.G7.02: Trace agent learning from rewards over trials
* T21.G7.01: Explain how AI makes decisions (classification, game playing)
```

**Rationale:** Shows how simulations power AI game playing, previews reinforcement learning and tree search.

**Implementation Notes:**
- Simplified game: 3x3 grid, 3 in a row wins (or even simpler: pick from 5 choices, one is "winning")
- Strategy A: For each legal move, simulate 10 random continuations, pick move with most wins
- Strategy B: Same but bias random moves toward previously successful ones (weight = wins + 1)
- Measure: Play 50 games, compare win rates
- Connection: AlphaGo, chess engines use this with millions of simulations
- Success criterion: Both strategies implemented, 50 games played, win rates compared, AlphaGo connection made

---

## SPLIT SKILLS - Full Content

### Split: T27.G5.04 → Two Sub-Skills

**T27.G5.04.01**
```
ID: T27.G5.04.01
Topic: T27 – Chance & Simulations
Skill: Define simulation question, variables, and trials
Description: Before building a simulation, students write a planning document with 3 components:
1. Question: What am I trying to find out? (e.g., "How often does a team with 60% win rate win 3 games in a row?")
2. Variables to track: What will I measure? (e.g., wins, losses, streak length)
3. Number of trials: How many times will I run it? (At least 100 for stable results)

They review example plans and identify which are well-defined vs. vague. This prevents "just start coding" without clear goals.

Dependencies:
* T27.G4.03: Show how sample size changes variability
* T27.G4.04: Debug an "unfair" simulation
```

**T27.G5.04.02**
```
ID: T27.G5.04.02
Topic: T27 – Chance & Simulations
Skill: Choose random model and define success criteria
Description: Students extend their simulation plan by adding:
4. Random model: What will be random? How will I model it? (e.g., "Each game = pick random 1 to 100. If ≤ 60, team wins.")
5. Success criteria: How will I know my simulation works? (e.g., "Overall win rate should be close to 60%")

They compare two models for the same problem and explain which is more realistic. They test their success criterion after running the simulation.

Dependencies:
* T27.G5.04.01: Define simulation question, variables, and trials
* T05.G4.01: Describe what a simulation should do before building
```

---

### Split: T27.G7.05 → Two Sub-Skills

**T27.G7.05.01**
```
ID: T27.G7.05.01
Topic: T27 – Chance & Simulations
Skill: Document simulation assumptions and limitations
Description: Students write documentation for their multi-agent simulation with:
1. Purpose: What question does it answer? (e.g., "Does adding walls change how long prey survive?")
2. Assumptions: What did we simplify? (e.g., "Agents can't see through walls," "All agents have equal speed," "Energy decreases at constant rate")
3. Limitations: What can't this simulation predict? (e.g., "Real animals can learn new strategies," "Doesn't model reproduction")

They compare their assumptions to reality and identify which simplifications might change results the most. This mirrors professional simulation documentation.

Dependencies:
* T27.G7.01: Create a two-agent interaction simulation
* T27.G7.03: Test for fairness using synthetic game testers
```

**T27.G7.05.02**
```
ID: T27.G7.05.02
Topic: T27 – Chance & Simulations
Skill: Identify stakeholders affected by simulation-based decisions
Description: Students analyze who might be affected if someone made decisions based on their simulation. They list 3-5 stakeholder groups and describe potential impacts. Example for school lunch line simulation:
- Students: Shorter wait times (positive)
- Cafeteria staff: Might need more training for new system (mixed)
- Students with disabilities: New system must accommodate wheelchair access (critical)

They identify groups that might be harmed and propose how to test for fairness across groups. This connects to ethical AI development.

Dependencies:
* T27.G7.05.01: Document simulation assumptions and limitations
* T32.G7.07: Identify stakeholders affected by a computing solution
```

---

### Split: T27.G8.01 → Two Sub-Skills

**T27.G8.01.01**
```
ID: T27.G8.01.01
Topic: T27 – Chance & Simulations
Skill: Automate data collection with parameter sweeps and logging
Description: Students create an automated data collection system:
1. Outer loop: Repeat for each configuration (e.g., speed = 1, 2, 3, 4, 5)
2. Inner loop: For current config, run 50 trials
3. Logging: After each trial, add row to data table: [config, trial_number, outcome, score, timestamp]

After running, they verify: Data table should have 5 configs × 50 trials = 250 rows. They export data as CSV. This automates what was previously manual testing.

Dependencies:
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T27.G7.06.02: Aggregate metrics across multiple agents
```

**T27.G8.01.02**
```
ID: T27.G8.01.02
Topic: T27 – Chance & Simulations
Skill: Build interactive dashboard from simulation data
Description: Students create a dashboard that displays simulation results:
1. Summary view: Bar chart comparing average score for each configuration
2. Detail view: When user clicks a config, show histogram of all 50 trial scores for that config
3. Stats panel: Display mean, median, range for selected config
4. Update button: "Run 50 more trials" button adds new data and updates all charts

This creates a professional-grade analytics interface for exploring simulation results.

Dependencies:
* T27.G8.01.01: Automate data collection with parameter sweeps and logging
* T26.G6.01: Calculate statistics (mean, median, mode, range)
* T06.G5.01: Broadcast a custom message and respond in another sprite
```

---

## Summary Table: All New Skills

| ID | Grade | Skill Name | Type | Priority |
|----|-------|------------|------|----------|
| T27.G2.05 | G2 | Watch CreatiCode spinner | NEW | URGENT |
| T27.G4.08 | G4 | Draw area models | NEW | HIGH |
| T27.G4.09 | G4 | Test simulation reliability | NEW | LOW |
| T27.G5.04.01 | G5 | Define question/variables/trials | SPLIT | HIGH |
| T27.G5.04.02 | G5 | Choose model/success criteria | SPLIT | HIGH |
| T27.G5.12 | G5 | Calculate mean and spread | NEW | HIGH |
| T27.G5.13 | G5 | Generate training data | NEW | MEDIUM |
| T27.G6.12 | G6 | Generate outcomes systematically | NEW | HIGH |
| T27.G6.13 | G6 | Debug edge cases | NEW | LOW |
| T27.G7.05.01 | G7 | Document assumptions | SPLIT | LOW |
| T27.G7.05.02 | G7 | Identify stakeholders | SPLIT | LOW |
| T27.G7.08 | G7 | AI confidence scores | NEW | MEDIUM |
| T27.G8.01.01 | G8 | Automate data collection | SPLIT | LOW |
| T27.G8.01.02 | G8 | Build dashboard | SPLIT | LOW |
| T27.G8.07 | G8 | Monte Carlo tree search | NEW | MEDIUM |

**Total: 15 new skill records** (9 entirely new + 6 from splits)

---

## Implementation Notes for All Skills

### General Guidelines
1. **Success criteria:** Every skill should have measurable outcomes
2. **Active verbs:** All skills use active verbs (Select, Test, Compare, Calculate, Build)
3. **Specific numbers:** "8 cards," "50 trials," "100 examples" (not "some cards" or "multiple trials")
4. **Real connections:** Link to games, AI, real-world decisions where possible

### Dependencies Best Practices
- **Internal first:** T27 skills before cross-topic
- **Prerequisites only:** Don't list "nice to have" dependencies
- **Check existence:** Verify all dependency IDs exist in curriculum

### Assessment Design
- **Auto-gradable where possible:** "All 8 cards sorted correctly" can be checked automatically
- **Clear success states:** Not "explore" or "appreciate" but "calculate X correctly"
- **Immediate feedback:** Students can verify their work (run simulation, check result)

---

**Next Step:** Use action checklist to implement these skills in phases.
