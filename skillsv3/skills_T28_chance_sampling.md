# T28 – Chance & Simulations: K–8 Skill List (Draft v1)

Topic reference: `T28 Chance & Simulations` in `domains_topics_overview.md`
Domain: Data & Analysis (D3) · CSTA focus: DAA‑DI, DAA‑IM (with links to PRO‑PF, ALG‑AF, ALG‑PS)

Each skill below has:

- a stable **ID** (`T28.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Kindergarten introduces the idea of chance and randomness in play and simple stories, recognizing predictable vs. unpredictable events without formal probability language.

### T28.GK.01 – Spot predictable vs. surprising events

- **Short name:** Is it predictable or surprising?
- **Description:** Students observe simple events and distinguish between outcomes that are predictable (always happen the same way) and outcomes that are surprising or unpredictable (could happen in different ways). This builds intuition about randomness vs. determinism in a concrete, play-based way.
- **Challenge format:** Concept, interactive story or animation. A sequence of pictures shows simple events (e.g., "If you drop a ball, it falls" vs. "You flip a coin"). Students choose "Always happens the same" or "Could be different." Auto‑grading checks their classification based on logical reasoning.
- **CSTA:** EK‑DAA‑DI‑02 (Recognize patterns that people and machines can use to make decisions).

### T28.GK.02 – Count outcomes in a simple game

- **Short name:** Count how many different ways
- **Description:** After playing a simple game (e.g., picking colored blocks from a bag) several times, students count how many different outcomes were observed (red, blue, yellow) and compare counts informally. This introduces the idea that some outcomes may happen more or less often.
- **Challenge format:** Concept, interactive play with counting. CreatiCode shows a simple random event (e.g., a die roll or spinner) performed 5–10 times, with outcomes displayed as pictures. Students count and report how many times each outcome appeared. Auto‑grading checks the counts and may ask which outcome appeared most.
- **CSTA:** EK‑DAA‑DI‑02, EK‑DAA‑IM‑04 (Explore how data can help a person make informed decisions).

### T28.GK.03 – Make a simple prediction about chance

- **Short name:** Guess what will happen next
- **Description:** Based on a few trials of a random event (e.g., spinner, coin flip), students make a prediction about the next outcome, building early intuition about probability (even if they cannot articulate why). They observe the actual result and reflect on whether they were correct.
- **Challenge format:** Concept, guided prediction. A CreatiCode animation shows a spinner or random picker 3–4 times; students predict the next outcome by choosing from pictures or words. The system then reveals the actual outcome and provides feedback. Auto‑grading checks the prediction type (did they guess at all?) and can track correctness.
- **CSTA:** EK‑DAA‑IM‑04.

---

## Grade 1

Grade 1 introduces the language of "fair" and "unfair" chance, and recognizes that some things are more likely to happen than others.

### T28.G1.01 – Recognize "more likely" and "less likely"

- **Short name:** Is it more or less likely?
- **Description:** Students compare simple probability scenarios informally (e.g., picking a red ball from a bag with 5 red and 1 blue vs. a bag with 3 red and 3 blue) and decide which outcome is "more likely" or "less likely," building qualitative probability reasoning.
- **Challenge format:** Concept, multiple choice. Present two scenarios with pictures of the bags/spinners and ask, "Which is more likely to give you a red ball?" Students choose the scenario. Auto‑grading compares to correct reasoning about relative likelihood.
- **CSTA:** E1‑DAA‑DI‑02 (Investigate questions that can be answered by manually collecting data), E1‑DAA‑IM‑04 (Investigate a variety of data questions that address the needs of a person or community).

### T28.G1.02 – Perform and record a simple chance experiment

- **Short name:** Run an experiment and keep score
- **Description:** Students physically perform a simple chance experiment (e.g., flip a coin, spin a spinner) multiple times and use tally marks or pictures to record each outcome, introducing data collection in the context of chance.
- **Challenge format:** Coding and concept, guided hands-on activity with digital recording. A CreatiCode project simulates a simple chance event (e.g., coin flip or die roll); students click to "run" the experiment 5–10 times and the system records outcomes in a list or tally chart. Auto‑grading checks that (1) multiple trials were recorded, and (2) each outcome is correctly tallied.
- **CSTA:** E1‑DAA‑DI‑02.

### T28.G1.03 – Compare predictions to actual results

- **Short name:** Did you guess right?
- **Description:** Before running an experiment, students make a prediction (e.g., "I think the coin will land on heads 5 times out of 10"); they then perform the experiment and compare their prediction to the actual results, introducing the idea that predictions are not always correct.
- **Challenge format:** Concept and hands-on, prediction check. A CreatiCode project asks students to predict outcomes before running a 10-trial experiment (e.g., "How many heads will there be?"). After the experiment runs, the system displays the predicted count and actual count, allowing students to see the difference. Auto‑grading measures the accuracy of the prediction and informs reflection.
- **CSTA:** E1‑DAA‑IM‑04.

---

## Grade 2

Grade 2 uses loops to run many trials of a chance experiment, introduces fairness of games, and begins comparing experimental results to theoretical expectations.

### T28.G2.01 – Use a loop to run many trials

- **Short name:** Run an experiment 20 times with a loop
- **Description:** Students use a `repeat` loop in code to simulate a chance event (e.g., coin flip or die roll) many times automatically, avoiding manual repetition and introducing the connection between loops (T07) and data collection.
- **Challenge format:** Coding, starter project. Provided: a `pick random` block for a coin or die. Students insert a `repeat` loop (e.g., 20 trials) around the random pick, with each trial recorded in a variable or list. Auto‑grading checks (1) correct loop structure with appropriate count, and (2) that trials are recorded.
- **CSTA:** E2‑PRO‑PF‑01, E2‑DAA‑DI‑02 (Evaluate different representations of the same data).

### T28.G2.02 – Create a tally or count from experiment results

- **Short name:** Count heads and tails
- **Description:** After running an experiment (manually or in code), students create a tally chart, count, or list to show how many times each outcome occurred, building data organization and summary skills.
- **Challenge format:** Coding, starter project with or without a loop. A CreatiCode project runs a 20-trial coin flip experiment (using a loop or pre-recorded data). Students update `count_heads` and `count_tails` variables and display the final counts. Auto‑grading checks that (1) both counts are correct, and (2) they sum to 20.
- **CSTA:** E2‑DAA‑DI‑02.

### T28.G2.03 – Recognize patterns in repeated experiments

- **Short name:** Run the experiment twice and compare
- **Description:** Students run the same chance experiment twice (or look at results from two trials) and notice that results differ each time, even with the same rules. This builds intuition that randomness produces variability.
- **Challenge format:** Concept and coding, comparative analysis. A CreatiCode project runs a 10-trial die-roll experiment, records counts, and then repeats it again. Students observe the counts from both runs and answer, "Did you get the same number of 1s both times?" Auto‑grading encourages reflection on variability.
- **CSTA:** E2‑DAA‑DI‑02.

### T28.G2.04 – Introduce the idea of a "fair game"

- **Short name:** Is this a fair game?
- **Description:** Students play or simulate simple games with chance and evaluate whether the game is "fair" (all players have equal chance to win) or "unfair" (one player has an advantage). They may compare experimental outcomes to justify their reasoning.
- **Challenge format:** Concept and analysis, game evaluation. A CreatiCode project describes a simple game (e.g., "Win if you roll a 6") and shows results from many trials. Students decide "Fair" or "Not fair" and explain by looking at the outcome frequencies. Auto‑grading checks the choice and looks for reasoning related to equal chances or observed frequencies.
- **CSTA:** E2‑DAA‑IM‑04 (Distinguish among data collection approaches that may lead to poor information).

---

## Grade 3

Grade 3 uses loops and variables to run larger-scale simulations, explores bias in experiments, and begins reasoning about expected outcomes vs. observed outcomes.

### T28.G3.01 – Simulate an experiment 50+ times to see a pattern

- **Short name:** Run many trials to spot the trend
- **Description:** Students write code to run a simulation a larger number of times (50–100 trials) using a loop and accumulator variables, allowing them to observe stabilizing frequencies and patterns in randomness over larger sample sizes.
- **Challenge format:** Coding, starter project. A CreatiCode project template provides a `repeat` loop to run (say) 100 coin flips or die rolls. Students update count variables for each outcome. The system displays the final counts as numbers or a simple bar chart. Auto‑grading checks loop count and variable updates.
- **CSTA:** E3‑PRO‑PF‑01, E3‑DAA‑DI‑03 (Create a data visualization and a brief narrative to report the process and results of a data investigation).

### T28.G3.02 – Compare frequencies from two different experiments

- **Short name:** Is coin or die more likely to land on one side?
- **Description:** Students run two different chance experiments (e.g., coin flip vs. spinner with unequal sections) and compare the frequencies to reason about which outcome is more likely based on empirical data from their simulations.
- **Challenge format:** Coding and analysis, comparative simulation. A CreatiCode project asks students to run two experiments (each 50 trials) side by side. They record counts and compare (e.g., "Heads appeared 24 times. Does that match what you expected?"). Auto‑grading checks code structure and may ask students to select which outcome was more frequent.
- **CSTA:** E3‑DAA‑DI‑03.

### T28.G3.03 – Plan a simple survey with clear questions

- **Short name:** Write a survey question
- **Description:** Students design a simple survey question (e.g., "What is your favorite color?") to collect data from classmates or a simulated population, learning that data can come from observation or asking people, and that question clarity matters.
- **Challenge format:** Concept and design, guided worksheet or CreatiCode dialog. A prompt asks, "Write a survey question to find out [topic]." Students draft a question and the system may offer feedback on clarity (is it too vague?). Auto‑grading checks that the question is reasonable and would yield useful data.
- **CSTA:** E3‑DAA‑IM‑05 (Design a data collection approach that addresses the needs of people from different backgrounds or groups).

### T28.G3.04 – Recognize sampling bias and its effect

- **Short name:** Is your sample fair?
- **Description:** Students examine a hypothetical experiment or survey where the sample is biased (e.g., "Ask only kids in the library about favorite recess activity") and reason about why the results might not represent the whole group. This introduces the concept of bias without requiring formal statistical language.
- **Challenge format:** Concept, multiple choice or reasoning. A CreatiCode scenario describes a survey or experiment with a biased sample; students choose "Fair sample" or "Biased sample" or explain who is missing. Auto‑grading checks understanding of bias.
- **CSTA:** E3‑DAA‑IM‑05.

---

## Grade 4

Grade 4 designs and runs more complex simulations, calculates and compares observed frequencies to theoretical probabilities, and explores privacy concerns related to data collection.

### T28.G4.01 – Calculate theoretical probability from a model

- **Short name:** What should happen in theory?
- **Description:** Given a clear model (e.g., a die with 6 equal sides, or a bag with 3 red and 2 blue marbles), students calculate or reason about the theoretical probability of an outcome (e.g., "1 in 6 chance for each number") and express it as a ratio or simple fraction.
- **Challenge format:** Concept, multiple choice or short-answer. Show a model (spinner diagram, bag of marbles, or die) and ask, "What is the chance of picking red?" Students choose an answer (1/3, 1/4, etc.) or count to justify their reasoning. Auto‑grading compares to correct calculation.
- **CSTA:** E4‑DAA‑DI‑02 (Investigate a data question involving relationships between multiple attributes).

### T28.G4.02 – Compare experimental results to theoretical probability

- **Short name:** Do your results match the prediction?
- **Description:** Students run a simulation with a known theoretical probability (e.g., rolling a fair die 60 times and expecting each number ~10 times) and compare their observed frequency to the theoretical expectation, building reasoning about variability and sample size.
- **Challenge format:** Coding and analysis, simulation with comparison. A CreatiCode project runs (say) 60 die rolls and displays the observed count for each number alongside a visual or numeric representation of the theoretical expectation (10 times each). Students answer, "Are your results close to the theoretical prediction?" Auto‑grading checks the simulation code and the reasoning quality.
- **CSTA:** E4‑DAA‑DI‑02.

### T28.G4.03 – Run a weighted or unequal probability simulation

- **Short name:** Simulate a spinner with unequal sections
- **Description:** Students code a simulation where probabilities are unequal (e.g., a spinner with one large section and one small section, or a weighted die), using conditional logic or random ranges to encode the different probabilities.
- **Challenge format:** Coding, starter project. Provided: description of an unequal spinner or die. Students use a `pick random` block with custom logic (e.g., if random number is 1–8 out of 10, pick "A"; if 9–10, pick "B") to weight outcomes, then run many trials and observe frequencies. Auto‑grading checks that (1) the code correctly implements the unequal probabilities, and (2) trial counts show appropriate frequencies.
- **CSTA:** E4‑PRO‑PF‑01, E4‑DAA‑DI‑02.

### T28.G4.04 – Collect survey data responsibly and discuss privacy

- **Short name:** Plan a survey and respect privacy
- **Description:** Students design a survey for peers or a community, addressing privacy concerns such as: What information is necessary to collect? How will responses be stored? Who will see the results? This connects data collection to ethics and privacy awareness.
- **Challenge format:** Concept and design, worksheet or CreatiCode dialog. Students write survey questions and answer prompts such as, "Will you ask for names?" and "How will you keep responses private?" Auto‑grading checks that they have considered privacy in their plan.
- **CSTA:** E4‑DAA‑IM‑04 (Analyze privacy concerns related to collected data).

---

## Grade 5

Grade 5 uses loops to design and implement full simulations with multiple variables, estimates probabilities from larger datasets, and analyzes how experimental design choices affect results.

### T28.G5.01 – Design a realistic simulation (e.g., weather, sports)

- **Short name:** Build a simulation with probabilities
- **Description:** Students design and code a simulation of a real-world scenario (e.g., daily weather patterns, a sports match outcome) that uses random events and accumulator variables to model the scenario over many iterations, integrating loops, variables, and randomness.
- **Challenge format:** Coding, open-ended project with structure. A CreatiCode template outlines a simulation (e.g., "Simulate a basketball player's free-throw percentage"). Students add logic to pick random outcomes based on a given probability (e.g., 70% success), run many trials with a loop, and collect statistics. Auto‑grading checks code structure (loop, randomness, variable updates) and correctness of the probability encoding.
- **CSTA:** E5‑PRO‑PF‑01, E5‑DAA‑DI‑02 (Analyze a dataset to identify the nature and possible sources of variability in the data).

### T28.G5.02 – Estimate a probability from observed data

- **Short name:** Guess the probability from the data
- **Description:** Given results from a large number of trials (from code or from a provided dataset), students estimate the probability of an outcome by calculating the frequency (e.g., "47 successes out of 100 trials means about 47% chance"), building the connection between frequency and probability.
- **Challenge format:** Concept and coding, data analysis. A CreatiCode project shows a table or bar chart from a 100+ trial simulation. Students calculate or estimate the probability (e.g., "How many times did it land on heads?" to estimate probability). Auto‑grading checks their calculation against the actual frequency.
- **CSTA:** E5‑DAA‑DI‑02.

### T28.G5.03 – Identify how sample size affects frequency stability

- **Short name:** Does 10 trials match 100 trials?
- **Description:** Students run the same simulation with two different sample sizes (e.g., 10 trials vs. 100 trials) and compare the frequency distributions, observing that larger samples produce more stable (less variable) frequency estimates.
- **Challenge format:** Concept and coding, comparative analysis. A CreatiCode project allows students to run a coin-flip simulation with a variable trial count. They run it once with 10 trials, once with 100 trials, and compare the frequency distributions visually. Auto‑grading checks observations about stability with larger samples.
- **CSTA:** E5‑DAA‑DI‑02.

### T28.G5.04 – Analyze bias in a simulated or real experiment

- **Short name:** Find the flaw in the experiment
- **Description:** Students examine a described or simulated experiment with a flaw or bias (e.g., "Only survey kids who like sports to find out if kids like sports") and reason about how the flaw would affect the results, building critical analysis of experimental design.
- **Challenge format:** Concept, explanation or multiple choice. A CreatiCode scenario describes a flawed survey or experiment. Students identify the bias and explain how it would skew results. Auto‑grading checks for understanding of bias and its effect.
- **CSTA:** E5‑DAA‑IM‑04 (Analyze the benefits and risks of using data in real-world scenarios, including AI).

---

## Grade 6

In middle school, students design and evaluate full experiments with control variables and random samples, and reason about uncertainty and variability in data.

### T28.G6.01 – Design a controlled experiment with random sampling

- **Short name:** Design an experiment with controls
- **Description:** Students plan a controlled experiment (e.g., testing if plant growth is affected by light) that includes identifying variables to control, identifying what to measure, and planning to collect data fairly from a random sample. This moves from simulation to real-world experimental design.
- **Challenge format:** Concept and planning, design document or CreatiCode dialog. Students answer prompts: "What will you change?" (independent variable), "What will you measure?" (dependent variable), "What stays the same?" (controls), "How will you choose which observations to include?" (sampling). Auto‑grading checks for presence of controls and awareness of sampling.
- **CSTA:** MS‑DAA‑DI‑08 (Pose data questions that anticipate variability in the data).

### T28.G6.02 – Run a simulation and analyze variability in results

- **Short name:** Run the simulation multiple times and see the spread
- **Description:** Students code a complete simulation (building on grade 5) and run it multiple times, each time obtaining slightly different results due to randomness. They analyze the distribution of outcomes across runs to understand variability.
- **Challenge format:** Coding and analysis, simulation with multiple runs. A CreatiCode project allows students to run a simulation 3–5 times, recording the final result each time. They compare the results, noting differences, and discuss what causes the variability. Auto‑grading checks for understanding of variability due to randomness.
- **CSTA:** MS‑PRO‑PF‑01, MS‑DAA‑DI‑08.

### T28.G6.03 – Use computational tools to identify relationships among variables

- **Short name:** Find which variable affects the outcome
- **Description:** Students use a provided dataset or run a simulation that has multiple input variables, and use filtering, sorting, or conditional analysis in code or tools to identify which variable most affects the outcome (e.g., "Does rain always come after clouds?").
- **Challenge format:** Coding and data analysis, starter project with a dataset. A CreatiCode project provides a table or list with multiple variables and asks, "Which variable best predicts [outcome]?" Students filter or analyze the data programmatically and justify their answer. Auto‑grading checks the analytical approach and conclusion.
- **CSTA:** MS‑DAA‑DI‑09 (Use computational tools to identify relationships among variables in a dataset and make classifications or predictions).

### T28.G6.04 – Evaluate fairness of a game or sampling process

- **Short name:** Is this game or survey fair?
- **Description:** Students analyze a game, survey, or experimental procedure and judge whether all possible outcomes or participants have an equal (fair) or unequal (biased) chance of being included or winning. They may use simulation or logical reasoning to support their judgment.
- **Challenge format:** Concept and analysis, reasoning or simulation. A CreatiCode scenario describes a game rule or survey method. Students decide if it is fair and explain using evidence (logical reasoning or simulation results). Auto‑grading checks the fairness judgment and reasoning quality.
- **CSTA:** MS‑DAA‑IM‑14 (Analyze how decisions made during data collection, data processing, data analysis, and data presentation can lead to biased data, misleading conclusions, and compromised AI models).

---

## Grade 7

Grade 7 emphasizes the experimental method, Monte Carlo simulations for probability estimation, and ethical considerations in data-driven decision-making.

### T28.G7.01 – Conduct a full multi-step experiment with hypothesis

- **Short name:** Test a hypothesis with an experiment
- **Description:** Students formulate a clear hypothesis (prediction), design an experiment to test it (with controls, variables, and sample size decisions), collect data, and draw conclusions, practicing the scientific method within a probability or observational context.
- **Challenge format:** Coding and project, full experiment design. A CreatiCode starter project guides students through: hypothesis, method, data collection (manual or simulated), analysis, and conclusion. They may simulate an experiment or design a real survey with peers. Auto‑grading checks that all components are present and that the conclusion is justified by data.
- **CSTA:** MS‑DAA‑DI‑08, MS‑DAA‑DI‑11 (Evaluate the quality and limitations of a dataset for answering different data questions).

### T28.G7.02 – Implement a Monte Carlo simulation to estimate a probability

- **Short name:** Run 1000s of trials to estimate odds
- **Description:** Students code a simulation using a large number of iterations (e.g., 1000 or 10,000 trials) to empirically estimate a complex probability (e.g., chance of rolling three dice that sum to 10, or chance of at least two people sharing a birthday in a room of 20). They interpret the frequency as a probability estimate.
- **Challenge format:** Coding, algorithmic challenge. A CreatiCode project asks students to estimate a probability (e.g., "In 1000 random days, how many are Mondays?"). They code the simulation with nested loops or lists, run it, and report the frequency as a probability. Auto‑grading checks simulation correctness and the reasonableness of the frequency estimate.
- **CSTA:** MS‑PRO‑PF‑01, MS‑DAA‑DI‑09.

### T28.G7.03 – Analyze sources of bias in data collection and its impact

- **Short name:** How did bias affect the results?
- **Description:** Students examine a real or simulated dataset known to have bias (e.g., results from a survey taken only online, results from a controlled experiment run only in one location), analyze how the bias occurred, and reason about how the results would differ if the bias were eliminated.
- **Challenge format:** Concept and analysis, case study. A CreatiCode presentation describes a study with bias (source revealed or hidden). Students identify the bias, explain its source, and predict how results would change if the bias were removed. Auto‑grading checks identification of bias and reasoning about impact.
- **CSTA:** MS‑DAA‑IM‑14, MS‑DAA‑IM‑15 (Analyze the societal impacts of data-driven algorithms and computational systems, including AI).

### T28.G7.04 – Conduct a sampling experiment and compare to population parameter

- **Short name:** Does your sample match the whole group?
- **Description:** Students take multiple random samples from a known population (real or simulated), compute a statistic (e.g., mean, proportion) for each sample, and compare sample statistics to the true population parameter, building intuition about sampling variability and estimators.
- **Challenge format:** Coding and analysis, simulation. A CreatiCode project defines a population (e.g., a list of 100 numbers or simulated heights). Students code a loop that repeatedly draws a random sample of fixed size, computes a statistic (mean or median), and collects statistics from multiple samples. They then compare the distribution of sample statistics to the population value. Auto‑grading checks code correctness and observation of sampling variability.
- **CSTA:** MS‑DAA‑DI‑08, MS‑DAA‑DI‑11.

---

## Grade 8

Grade 8 builds toward high school by integrating probability, statistical analysis, and ethical reasoning about data-driven decisions, bias in algorithms, and informed consent.

### T28.G8.01 – Design and conduct an experiment addressing a real question

- **Short name:** Run an experiment to answer your question
- **Description:** Students develop their own research question, design an experiment or survey to answer it (including decisions about variables, controls, sample size, and data collection method), conduct the experiment, analyze results, and communicate findings. This is a capstone skill integrating earlier concepts.
- **Challenge format:** Coding and project, open-ended. Students choose a question (e.g., "Does music help concentration?" or "What is the most popular lunch item?"), design the experiment, collect or simulate data, and write a brief report with analysis and conclusion. Auto‑grading checks that the design is sound, data collection is recorded, and conclusion is justified.
- **CSTA:** MS‑DAA‑DI‑08, MS‑DAA‑DI‑11, MS‑DAA‑DI‑12 (Share the story of a data investigation with peers, including what data question was asked, how the data was collected and analyzed, and what evidence supports the conclusion).

### T28.G8.02 – Estimate probability using large-scale simulation or real data

- **Short name:** Estimate odds from data
- **Description:** Students estimate the probability of a complex or uncertain event (e.g., a hurricane, a sports outcome) by analyzing historical data or running a sophisticated Monte Carlo simulation with many variables, integrating lists, loops, and conditional logic.
- **Challenge format:** Coding and analysis, data-driven estimation. A CreatiCode project provides real or realistic data (e.g., a list of past weather events, or parameters for a complex system). Students code a simulation to estimate probability, or analyze the historical data to compute a frequency estimate. Auto‑grading checks simulation/analysis correctness and the plausibility of the probability estimate.
- **CSTA:** MS‑PRO‑PF‑01, MS‑DAA‑DI‑09.

### T28.G8.03 – Analyze bias in AI models trained on biased data

- **Short name:** How does biased data hurt AI?
- **Description:** Students learn that AI systems trained on biased datasets produce biased outputs, and can examine examples (e.g., if a training dataset has more images of one gender, the model may perform worse on that gender). They reason about consequences and potential fixes.
- **Challenge format:** Concept and analysis, case study or interactive simulation. A CreatiCode scenario or interactive demo shows how training data composition affects model outputs. Students analyze a specific bias and explain its source and consequence. Auto‑grading checks for understanding of training data bias and its effects.
- **CSTA:** MS‑DAA‑IM‑14, MS‑DAA‑IM‑15.

### T28.G8.04 – Evaluate ethical considerations in data-driven decisions

- **Short name:** Is it fair to decide this way?
- **Description:** Students examine a real-world scenario where a decision is made using data (e.g., hiring, lending, school admissions, content recommendation) and analyze ethical concerns: Is the data biased? Will the decision harm some groups? What are privacy implications? Should people be informed and given agency?
- **Challenge format:** Concept and reasoning, case study or structured discussion. A CreatiCode presentation describes a data-driven decision scenario. Students analyze it using prompts about bias, fairness, privacy, and consent, and propose alternatives. Auto‑grading checks for depth of ethical reasoning.
- **CSTA:** MS‑DAA‑IM‑14, MS‑DAA‑IM‑15.
