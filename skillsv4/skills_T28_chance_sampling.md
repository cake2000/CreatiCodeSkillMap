# T28 – Chance & Simulations: G2–8 Skill List (Draft v3)

Topic reference: `T28 Chance & Simulations` in `domains_topics_overview.md`
Domain: Data & Analysis (D3) · CSTA focus: DAA‑DI, DAA‑IM (links to PRO‑PF, ALG‑PS, CAS‑ET)

Each skill below has:

- a stable **ID** (`T28.G<grade>.<nn>`),
- an IXL-style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** Probability concepts are abstract, so T28 now begins in **Grade 2** with unplugged, picture-based intuition before introducing any code. Grades 2–3 focus on vocabulary (certain/possible/impossible), physical experiments, and interpreting provided CreatiCode simulations. Starting in **Grade 4**, students leverage list/loop skills from **T10 (Programming Data Structures)** to build their own random generators, log outcomes, and compare them to expectations. Later grades connect simulations to project tuning (games, AI fairness checks) and ethical decision-making per AI4K12 priorities. Every coding skill that records data explicitly depends on earlier T25–T27 skills for representation, collection, and analysis.  
- _AI4K12:_ Machine Learning (A&E, Representation), Humans & AI, Ethical AI Design.

---

## Grade 2

### T28.G2.01 – Sort events into certain / possible / impossible

_Dependency:_
  * T01.G1.01: Put pictures in order to plant a seed


- **Short name:** Chance vocabulary sorter
- **Description:** Students classify illustrated events (the sun rising, rolling a 7 on a six-sided die, drawing a red marble from a bag that only has red) using everyday language about certainty.
- **Challenge format:** Concept, drag-and-drop. Auto-grading checks correct placements and a brief explanation for one event.
- **CSTA:** E2‑DAA‑DI‑02.

### T28.G2.02 – Conduct a picture-based chance experiment

_Dependency:_
  * T01.G1.01: Put pictures in order to plant a seed
  * T01.GK.08: Count how many times


- **Short name:** Spin, tally, and compare
- **Description:** Learners use a physical or on-screen spinner template, run 10 spins, and record tallies with stickers or pictographs to see which color appears more often.
- **Challenge format:** Unplugged + upload. Students submit a photo of their tally chart; auto-grading checks counts add to 10 and asks “Which color showed up most?”
- **CSTA:** E2‑DAA‑DF‑01.

### T28.G2.03 – Decide if a simple game is fair

_Dependency:_
  * T01.G1.10: Match pictures to "if/then" rules


- **Short name:** Which spinner is fair?
- **Description:** Students compare two drawn spinners (equal vs uneven slices) and explain which is “fairer” when playing a game.
- **Challenge format:** Concept multiple choice + justification. Auto-grading checks reasoning referencing slice sizes.
- **CSTA:** E2‑DAA‑DI‑02.

### T28.G2.04 – Predict and observe outcomes

_Dependency:_
  * T01.G1.01: Put pictures in order to plant a seed
  * T01.GK.08: Count how many times


- **Short name:** Guess before you flip
- **Description:** Learners make a prediction before each of five coin flips, then compare correct vs incorrect guesses to appreciate randomness.
- **Challenge format:** Guided worksheet. Auto-grading ensures predictions are recorded before results and reflection mentions unpredictability.
- **CSTA:** E2‑DAA‑IM‑04.

---

## Grade 3

### T28.G3.01 – Interpret provided simulation output

_Dependency:_
  * T28.G2.01: Sort events into certain / possible / impossible
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop


- **Short name:** Read the spinner report
- **Description:** Students watch a CreatiCode project run 20 random trials (pre-built) and answer questions about the resulting bar chart (Which color won? Did counts stay equal?).
- **Challenge format:** Concept Q&A tied to screenshots. Auto-grading checks answers referencing actual counts.
- **CSTA:** E3‑DAA‑DI‑02.

### T28.G3.02 – Record experimental data with teacher-provided blocks

_Dependency:_
  * T28.G3.01: Interpret provided simulation output
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Use a template to log coin flips
- **Description:** Learners drag a provided script (`repeat 10` + `pick random 0 1`) into the workspace, run it, and copy the generated table into their notebook. They explain what each column means (trial, result).
- **Challenge format:** Guided coding with template; minimal edits allowed. Auto-grading verifies the script remains unchanged and that students submit the resulting table screenshot plus explanation.
- **CSTA:** E3‑PRO‑PF‑01, DAA‑DP.

### T28.G3.03 – Compare predictions to simulated data

_Dependency:_
  * T28.G3.02: Record experimental data with teacher-provided blocks
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Was your guess close?
- **Description:** Before running the provided simulation, students predict how many times each color will appear. Afterward, they compute the difference between prediction and actual counts.
- **Challenge format:** Concept worksheet referencing the same dataset as G3.02. Auto-grading checks calculations and reflection about why predictions may differ.
- **CSTA:** E3‑DAA‑DI‑02.

### T28.G3.04 – Describe randomness in games they play

_Dependency:_
  * T28.G3.03: Compare predictions to simulated data
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Find chance in board games
- **Description:** Learners analyze a familiar board/card game (Chutes, Candy Land) and describe where randomness occurs and how it changes strategy.
- **Challenge format:** Short writing. Auto-grading rubric checks mention of chance mechanism and impact on gameplay.
- **CSTA:** E3‑DAA‑IM‑05.

---

## Grade 4 *(requires T10 Grade 4 list basics)*

### T28.G4.01 – Build a simple random generator

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G3.03: Compare predictions to simulated data


- **Short name:** Code a spinner with `pick random`
- **Description:** Students create a script that simulates spinning a 4-color wheel once and reports which color was chosen. They verify each color can appear.
- **Challenge format:** Coding. Auto-grading runs many trials to ensure all colors appear over time.
- **CSTA:** E4‑PRO‑PF‑01, DAA‑DI.

### T28.G4.02 – Log 50 trials into a list and compute frequencies

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G3.04: Describe randomness in games they play


- **Short name:** Turn list counts into percentages
- **Description:** Learners extend their spinner to repeat 50 times, append results to a list (T10 dependency), and calculate percentage for each color.
- **Challenge format:** Coding + analysis. Auto-grading checks list length = 50 and percentages sum ~100%.
- **CSTA:** E4‑DAA‑DP‑02.

### T28.G4.03 – Show how sample size changes variability

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G3.04: Describe randomness in games they play


- **Short name:** Compare 10 vs 100 trials in a graph
- **Description:** Students run two experiments (10, 100 spins) and plot bar charts to see stability differences.
- **Challenge format:** Coding + concept. Auto-grading verifies both datasets exist and reflections mention reduced variability.
- **CSTA:** E4‑DAA‑DI‑02.

### T28.G4.04 – Debug an “unfair” simulation

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G3.04: Describe randomness in games they play


- **Short name:** Find the bug in the random code
- **Description:** Learners inspect a script where one outcome is favored (duplicate entries, wrong range) and fix it so outcomes are equally likely.
- **Challenge format:** Coding + explanation. Auto-grading runs fairness tests (counts within tolerance) and checks students describe the fix.
- **CSTA:** E4‑PRO‑TR‑01.

---

## Grade 5

### T28.G5.01 – Simulate compound events (two dice)

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G4.04: Debug an “unfair” simulation


- **Short name:** Collect sums and compare to theory
- **Description:** Students roll two virtual dice 200 times, store sums, and explain why 7 is most common by referencing combinations.
- **Challenge format:** Coding + explanation. Auto-grading checks counts and requires textual justification.
- **CSTA:** E5‑DAA‑DI‑02.

### T28.G5.02 – Randomly assign participants to conditions

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G4.03: Show how sample size changes variability
  * T28.G4.04: Debug an “unfair” simulation


- **Short name:** Create a fair A/B splitter
- **Description:** Learners write a function that tags each simulated user as “A” or “B,” logs assignment, and reports counts to ensure near-equal groups.
- **Challenge format:** Coding. Auto-grading simulates many users and ensures counts stay within ±10%.
- **CSTA:** E5‑DAA‑DF‑01.

### T28.G5.03 – Use Monte Carlo to estimate an area or probability

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G4.03: Show how sample size changes variability
  * T28.G4.04: Debug an “unfair” simulation


- **Short name:** Throw darts at a square
- **Description:** Students generate random coordinate pairs, check if points land inside a circle, and approximate π or region area.
- **Challenge format:** Coding + math. Auto-grading ensures ≥500 trials and estimates within tolerance.
- **CSTA:** E5‑DAA‑DI‑02.

### T28.G5.04 – Document simulation plans before coding

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G4.03: Show how sample size changes variability
  * T28.G4.04: Debug an “unfair” simulation


- **Short name:** Fill a simulation design brief
- **Description:** Learners outline question, inputs, random model, number of trials, and outputs, drawing on T05.G5.03 (variables and initial values) and T05.G5.04 (update rules), reinforcing intentional design.
- **Challenge format:** Concept form. Auto-grading checks alignment between plan and submitted code.
- **CSTA:** E5‑PRO‑PM‑05.

---

## Grade 6

### T28.G6.01 – Conduct parameter sweeps for tuning

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G5.04: Document simulation plans before coding


- **Short name:** Auto-test multiple difficulty settings
- **Description:** Students loop over a range of parameters (e.g., enemy speed) and log win rates to choose balanced values.
- **Challenge format:** Coding + table logging. Auto-grading verifies all parameter values were tested and recommendation references data.
- **CSTA:** MS‑PRO‑PF‑02, DAA‑DI‑03.

### T28.G6.02 – Use random seeds for reproducibility

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G5.04: Document simulation plans before coding


- **Short name:** Repeat the same random story
- **Description:** Learners store a seed variable and demonstrate that rerunning the simulation with the same seed yields identical logs, a key scientific practice.
- **Challenge format:** Coding. Auto-grading runs scenarios to ensure repeatability.
- **CSTA:** MS‑PRO‑TR‑12.

### T28.G6.03 – Measure percent error vs theoretical probability

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G5.04: Document simulation plans before coding


- **Short name:** Quantify how close you are
- **Description:** Students calculate percent error between observed frequencies and expected probabilities, stating whether the error is acceptable.
- **Challenge format:** Calculation + reflection. Auto-grading checks math and justification referencing sample size.
- **CSTA:** MS‑DAA‑DI‑03.

### T28.G6.04 – Simulate noisy sensors for T23 testing

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G5.03: Use Monte Carlo to estimate an area or probability
  * T28.G5.04: Document simulation plans before coding


- **Short name:** Fake pose values with randomness
- **Description:** Learners generate random-but-bounded pose or voice data to test AI perception logic when a live camera/mic isn’t available.
- **Challenge format:** Coding. Auto-grading ensures values stay in valid ranges and trigger expected branches.
- **CSTA:** MS‑PRO‑PF‑02, CAS‑ET‑07.

### T28.G6.05 – Model an agent, its environment, and reward rules

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G5.03: Use Monte Carlo to estimate an area or probability
  * T28.G5.04: Document simulation plans before coding


- **Short name:** Define an agent in a grid world  
- **Description:** Students set up a simple grid world with one agent (position + facing), walls, and a goal/reward rule. They encode agent rules ("if front is clear, move; else turn right") and log states/rewards over 20 steps, highlighting how environment design affects behavior.  
- **Challenge format:** Coding + logging. Provided: starter grid and move/turn blocks. Students script the agent policy, track position and reward in lists, and answer a prompt about how changing walls/goal alters paths. Auto-grading checks that state logs are recorded each step and that rewards align to the defined rule.  
- **CSTA:** MS‑ALG‑AF‑01.
- **AI4K12:** Machine Learning - Agents and Environments.
- **Editor notes:** Builds on T05.G5.03 and T05.G5.04 (simulation design skills).

---

## Grade 7

### T28.G7.01 – Build agent-based simulations

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G6.05: Model an agent, its environment, and reward rules


- **Short name:** Model interacting sprites with chance
- **Description:** Students create multi-agent systems (e.g., rumor spread, ecosystem) where sprites follow probabilistic rules and log aggregated metrics.
- **Challenge format:** Coding + data logging. Auto-grading looks for multiple agents, randomness, and summary tables.
- **CSTA:** MS‑PRO‑PF‑02, DAA‑DI‑03.

### T28.G7.02 – Evaluate AI fairness using synthetic populations

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G6.04: Simulate noisy sensors for T23 testing
  * T28.G6.05: Model an agent, its environment, and reward rules


- **Short name:** Generate virtual testers
- **Description:** Learners create synthetic user profiles (attributes randomly sampled) and run AI assistants/chatbots through them to check for disparate outcomes.
- **Challenge format:** Coding + analysis. Auto-grading checks attribute diversity and disparity metrics per group.
- **CSTA:** MS‑CAS‑ET‑05.

### T28.G7.03 – Perform randomization tests (permutation tests)

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G6.05: Model an agent, its environment, and reward rules


- **Short name:** Shuffle labels to gauge significance
- **Description:** Students shuffle existing experimental labels many times and count how often results as extreme as the real one occur, estimating p-values.
- **Challenge format:** Coding + calculation. Auto-grading verifies ≥500 shuffles and correct interpretation.
- **CSTA:** MS‑DAA‑DI‑03.

### T28.G7.04 – Communicate simulation assumptions & limits

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G6.05: Model an agent, its environment, and reward rules


- **Short name:** Write "what this model can/can't tell us"
- **Description:** Learners document assumptions (independence, fixed probabilities) and limitations to promote transparency per AI4K12 guidance.
- **Challenge format:** Writing. Rubric checks at least two assumptions and one limitation tied to their code.
- **CSTA:** MS‑PRO‑PM‑03.

### T28.G7.05 – Trace how a simple agent learns from rewards

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G6.04: Simulate noisy sensors for T23 testing
  * T28.G6.05: Model an agent, its environment, and reward rules


- **Short name:** Observe agent path-finding improvements
- **Description:** Students observe a pre-built simulation where an agent's path-finding choices are updated based on a simple reward mechanism (e.g., a table of Q-values is updated visually). They answer questions about why the agent's path changes over multiple trials. This remains a conceptual tracing skill.
- **Challenge format:** Concept + observation. Auto-grading checks comprehension questions referencing agent behavior changes over time.
- **CSTA:** MS‑DAA‑DI‑03.
- **AI4K12:** Machine Learning - Agents and Environments.

---

## Grade 8

### T28.G8.01 – Chain simulation → analysis → dashboard

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G2.01: Sort events into certain / possible / impossible
  * T28.G7.04: Communicate simulation assumptions & limits


- **Short name:** Build a full Monte Carlo dashboard
- **Description:** Students automate simulations, store results, and auto-refresh charts/HUD elements so stakeholders can explore scenarios live.
- **Challenge format:** Coding + UI. Auto-grading re-runs simulations to ensure visuals update without manual edits.
- **CSTA:** MS‑PRO‑PF‑02, DAA‑DP.

### T28.G8.02 – Estimate uncertainty via bootstrap/resampling

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G2.01: Sort events into certain / possible / impossible
  * T28.G7.04: Communicate simulation assumptions & limits


- **Short name:** Create confidence intervals from data
- **Description:** Learners repeatedly resample collected data (with replacement) to produce distributions of a statistic and report percentile-based intervals.
- **Challenge format:** Coding. Auto-grading checks number of resamples and interval reporting.
- **CSTA:** MS‑DAA‑DI‑03.

### T28.G8.03 – Integrate simulations into XO/AI workflows

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G7.04: Communicate simulation assumptions & limits


- **Short name:** Feed metrics into XO for advice
- **Description:** Students summarize simulation outcomes, pass them to XO, and evaluate whether AI recommendations align with the data.
- **Challenge format:** Concept + reflection. Auto-grading checks transcripts and decision rationale referencing metrics.
- **CSTA:** MS‑CAS‑ET‑06.

### T28.G8.04 – Publish simulation-backed policy briefs

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G7.04: Communicate simulation assumptions & limits


- **Short name:** Advocate with data and ethics
- **Description:** Learners write briefs outlining scenario, simulation method, findings, and ethical impacts (winners/losers), mirroring civic data journalism.
- **Challenge format:** Writing. Rubric ensures inclusion of data summary, recommendation, and ethical reflection.
- **CSTA:** MS‑CAS‑HC‑02, DAA‑DI.

### T28.G8.05 – Analyze how environment design can bias agent behavior

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T28.G2.01: Sort events into certain / possible / impossible
  * T28.G7.04: Communicate simulation assumptions & limits


- **Short name:** Compare agent learning across different environments
- **Description:** Students compare two simulations where the same agent 'learns' in different environments (e.g., one with many obstacles near the reward, one with none). They write a short analysis on how the environment's design led to different learned behaviors, discussing the "bias" introduced by the world itself.
- **Challenge format:** Concept + analysis. Auto-grading checks for comparison of two scenarios and identification of environment-induced bias.
- **CSTA:** MS‑CAS‑ET‑05.
- **AI4K12:** Ethical AI System Design.

---
