# T28 Quick Action Reference

## IMMEDIATE FIXES (Can be done now)

### Dependency Corrections

**T28.G3.06**: Remove T28.G3.02 from dependencies (redundant, G3.03 already depends on it)
- OLD: T28.G3.02, T28.G3.03
- NEW: T28.G3.03 only

**T28.G4.01**: Remove unnecessary dependencies
- OLD: T06.G3.01, T07.G3.05, T08.G3.01, T09.G3.05, T28.G3.02
- NEW: T06.G3.01, T08.G3.01, T28.G3.02

**T28.G4.03**: Remove redundant dependencies
- OLD: T07.G3.05, T08.G3.01, T09.G3.05, T28.G4.02, T27.G3.04
- NEW: T07.G3.05, T28.G4.02, T27.G3.04

**T28.G5.03**: Add missing dependency
- OLD: T28.G4.03, T28.G4.05
- NEW: T28.G4.03, T28.G4.05, T08.G4.01

**T28.G7.01**: Replace specific debugging skill with general loop skill
- OLD: T06.G5.01, T07.G6.05, T09.G5.01, T28.G6.08
- NEW: T06.G5.01, T07.G5.01, T09.G5.01, T28.G6.08

---

## DESCRIPTION ENHANCEMENTS (Copy-paste ready)

### T28.G2.02
**OLD**: Learners use a physical or on-screen spinner template, run 10 spins, and record tallies with stickers or pictographs to see which color appears more often.

**NEW**: Learners use a physical spinner template (cardboard with brad) or manipulate picture-based spinners (drag-and-drop digital images), run 10 spins, and record tallies with stickers or pictographs to see which color appears more often.

---

### T28.G2.04
**OLD**: Learners make a prediction before each of five coin flips, then compare correct vs incorrect guesses to appreciate randomness.

**NEW**: Learners use physical coins or picture cards to make a prediction before each of five trials, then compare correct vs incorrect guesses to appreciate randomness.

---

### T28.G3.01
**OLD**: Students watch a CreatiCode project run 20 random trials (pre-built) and answer questions about the resulting bar chart (Which color won? Did counts stay equal?).

**NEW**: Students watch a CreatiCode project run 20 random trials (pre-built) and answer specific questions about the resulting bar chart: Which color appeared most often? Were any colors close in frequency? Did the counts change much between the first 10 and second 10 trials?

---

### T28.G3.05
**OLD**: Learners pick a familiar board or card game (Chutes and Ladders, Candy Land, Go Fish) and identify where randomness happens (dice roll, card shuffle, spinner). They explain in writing how that randomness affects whether skill or luck determines the winner.

**NEW**: Learners pick a familiar board or card game (Chutes and Ladders, Candy Land, Go Fish) and identify where randomness happens (dice roll, card shuffle, spinner). They explain in writing how that randomness affects whether skill or luck determines the winner. Then they create a simple CreatiCode project that demonstrates one source of randomness from their chosen game (e.g., a virtual die roller for Chutes and Ladders).

---

### T28.G5.04
**OLD**: Learners outline question, inputs, random model, number of trials, and outputs, reinforcing intentional design before implementation.

**NEW**: Students create a written simulation plan using a template with sections: (1) Question to answer, (2) Random elements (what varies and how?), (3) How many trials will run?, (4) What data to collect, (5) How to analyze results. Students complete this template before coding their next simulation project.

---

### T28.G5.06
**OLD**: Students run a simulation for a simple event (coin flip, die roll, spinner), compare their experimental frequencies to calculated theoretical probabilities, and explain why differences occur and how sample size affects accuracy.

**NEW**: Students run a simulation for a simple event (coin flip, die roll, spinner), compare their experimental frequencies to calculated theoretical probabilities, and explain why differences occur and how sample size affects accuracy. They explain the 'law of large numbers': as we run more trials, experimental results get closer to theoretical probability.

---

### T28.G6.04
**OLD**: Learners generate random-but-bounded pose or voice data to test AI perception logic when a live camera/mic isn't available.

**NEW**: Students create a testing script that generates random pose coordinates (x, y) within realistic ranges (e.g., nose position between x:-100 to 100, y:-50 to 150) or volume values (0-100) with added random noise. They use these synthetic values to test their AI perception blocks when a camera/microphone isn't available, verifying their conditional logic works correctly.

---

### T28.G6.06
**OLD**: Students build a simulation where one event's probability depends on a previous outcome (e.g., drawing cards without replacement, weather patterns where today's weather affects tomorrow's probability). They compare results to simulations where probabilities stay constant.

**NEW**: Students build a simulation where one event's probability depends on a previous outcome (e.g., drawing cards without replacement, weather patterns where today's weather affects tomorrow's probability). They compare results to simulations where probabilities stay constant. They use the term "dependent events" to describe scenarios where outcomes affect future probabilities.

---

### T28.G7.02
**OLD**: Students observe a pre-built simulation where an agent's path-finding choices are updated based on a simple reward mechanism (e.g., a table showing which directions the agent prefers at each location is updated visually). They answer questions about why the agent's path changes over multiple trials. This remains a conceptual tracing skill.

**NEW**: Students observe a pre-built simulation where an agent's preference table updates based on rewards received. They complete a worksheet tracing: (1) initial preference values at each location, (2) what reward was received when the agent visited each location, (3) how the preference values changed after rewards, (4) how the agent's chosen path differed between trial 1 and trial 10. They explain in writing why the agent's behavior evolved.

---

### T28.G7.05
**OLD**: Learners write a short "model card" for their simulation listing at least two assumptions (e.g., events are independent, probabilities stay constant) and one limitation (e.g., doesn't account for weather changes). This transparency practice mirrors AI documentation standards.

**NEW**: Students write a model card with specific sections: (1) Purpose: what question does this simulation answer? (2) Assumptions: list 2-3 things assumed to be true (e.g., 'weather stays the same each day', 'all players have equal skill'), (3) Limitations: identify 1-2 things the model doesn't include (e.g., 'doesn't account for player fatigue'), (4) Appropriate use: when should/shouldn't someone rely on these results? This transparency practice mirrors AI documentation standards.

---

### T28.G8.01
**OLD**: Students automate simulations, store results, and auto-refresh charts/HUD elements so stakeholders can explore scenarios live.

**NEW**: Students create an interactive dashboard that runs a simulation when a parameter is changed (using broadcast messages), automatically updates a table with results, and refreshes a bar chart showing the new data. They test the dashboard by changing 3 different parameter values and verifying the chart updates correctly each time.

---

### T28.G8.03
**OLD**: Students summarize simulation outcomes (key statistics, trends), pass them to an AI assistant (like CreatiCode's XO), and evaluate whether the AI's recommendations align with the data. They critically assess if the AI's suggestions make sense given their simulation results.

**NEW**: Students export their simulation summary as formatted text (including key statistics, observed trends, and their conclusion), paste it into CreatiCode's AI assistant as a prompt, and compare the AI's interpretation to their own analysis. They write 2-3 sentences explaining whether the AI correctly identified the main finding and whether its suggested next steps make sense given the data.

---

## NEW SKILLS TO ADD

### T28.G3.07 (Insert after current G3.06, before G4.01)
**Skill**: Assemble a random generator from provided blocks
**Description**: Students receive separate blocks (pick random, if-statements, say blocks) laid out in the workspace and follow a visual guide to connect them in the correct order to create a working 2-option random generator. They test their assembled generator to verify both outcomes can appear.
**Dependencies**: T28.G3.06, T08.G3.01

---

### T28.G4.06 (Insert after G4.02.03, before G5.05)
**Skill**: Interpret simple probabilities from familiar contexts
**Description**: Students examine scenarios (spinner with 4 equal sections, bag with 3 red and 1 blue marble) and explain in words the chance of each outcome using fractions (e.g., 'red is 3 out of 4 because there are 3 red marbles and 4 total'). They do not yet write code to calculate probabilities.
**Dependencies**: T28.G4.02.03

---

### T28.G4.07 (Insert after G4.04, before G5.01)
**Skill**: Use seeds to reproduce random sequences
**Description**: Students set a random seed value before running their simulation, observe the sequence of results, then reset to the same seed and verify they get identical results. They explain how this helps with debugging by making random behavior predictable during testing.
**Dependencies**: T28.G4.02.01, T09.G3.05

---

### T28.G5.08 (Insert after G5.04, before G6.05)
**Skill**: Track a sprite's state across multiple events
**Description**: Students create a sprite that remembers its state (happy/sad/hungry) using a variable. They implement events (green flag sets happy, space key makes sad, click makes hungry) and use if-statements to make the sprite say different messages based on its current state.
**Dependencies**: T28.G5.04, T09.G4.04, T08.G4.01

---

### T28.G5.09 (Insert after G5.07, before G5.10)
**Skill**: Use random selection without repetition
**Description**: Students create a simulation that picks from a list without allowing repeats (e.g., dealing cards, selecting survey participants). They compare results to simulations where repetition is allowed and explain when each approach is appropriate (sampling with vs without replacement).
**Dependencies**: T28.G4.02.01, T10.G3.03

---

### T28.G5.10 (Insert after G5.09, before G6.01)
**Skill**: Test independence of random trials
**Description**: Students investigate whether previous outcomes affect future results. They run a coin-flip simulation tracking whether 'heads after heads' occurs more often than expected by chance, and explain why each flip is independent (the coin has no memory of past flips).
**Dependencies**: T28.G5.06, T28.G4.02.02

---

### T28.G6.09 (Insert after G6.08, before G7.01)
**Skill**: Create a simple two-sprite random interaction
**Description**: Students create two sprites that each randomly move around the stage. When they touch each other (using the touching? block), one changes color. Students run this 10 times and count how many steps it takes for them to touch, recording the variation across trials.
**Dependencies**: T28.G6.05, T06.G5.01, T07.G5.01

---

### T28.G6.10 (Insert after G6.03, before G6.04)
**Skill**: Calculate and compare expected values
**Description**: Students calculate the expected value for a simple random game (e.g., spinner where red gives 10 points, blue gives 5 points, each 50% likely: expected = 0.5×10 + 0.5×5 = 7.5 points). They run 100 simulations, calculate the actual average score, and compare it to the expected value.
**Dependencies**: T28.G5.06, T27.G4.02c

---

### T28.G7.07 (Insert after G7.03, before G7.04)
**Skill**: Identify sources of sampling bias
**Description**: Students compare two data collection methods for the same question (e.g., surveying only students in one class vs random selection from whole school). They run simulations showing how convenience sampling can lead to biased results compared to random sampling, and explain which method is more reliable for different scenarios.
**Dependencies**: T28.G5.02, T28.G5.09

---

## SKILLS TO SPLIT INTO SUB-SKILLS

### SPLIT T28.G4.02 into three sub-skills:

**T28.G4.02.01**: Log trial results into a list
**Description**: Students extend their random generator to repeat 50 times and append each result to a list. They verify the list contains 50 entries and can display the list on stage.
**Dependencies**: T28.G4.01, T07.G3.01, T10.G3.03

**T28.G4.02.02**: Count frequencies from a list
**Description**: Students write code to count how many times each outcome appears in their list of 50 results, storing counts in separate variables or a second list. They verify the counts add up to 50.
**Dependencies**: T28.G4.02.01, T07.G3.05, T08.G3.01

**T28.G4.02.03**: Calculate percentages from counts
**Description**: Students convert their frequency counts to percentages by dividing each count by the total number of trials (50) and multiplying by 100. They display these percentages on stage and verify they add up to approximately 100%.
**Dependencies**: T28.G4.02.02

---

### SPLIT T28.G5.01 into two sub-skills:

**T28.G5.01.01**: Generate and sum two random values
**Description**: Students create a script that picks two random numbers (1-6), adds them together, and displays the sum with a say block. They click the green flag multiple times to observe that different sums (2-12) can appear.
**Dependencies**: T28.G4.02.03, T07.G3.05

**T28.G5.01.02**: Collect and analyze compound event data
**Description**: Students extend their two-dice simulation to run 200 times, storing each sum in a two-column table (sum value, frequency count). They create a bar chart showing how often each sum (2-12) appeared and identify that 7 is most common. They explain why 7 appears more often by listing the combinations that produce it.
**Dependencies**: T28.G5.01.01, T28.G4.02.02, T27.G3.04

---

### SPLIT T28.G6.01 into two sub-skills:

**T28.G6.01.01**: Test multiple parameter values manually
**Description**: Students run a simple game simulation with three different parameter values (e.g., enemy speed = 5, 10, 15), recording the outcome (win/lose or score) for each. They compare results and identify which value creates the most balanced gameplay.
**Dependencies**: T28.G5.01.02, T28.G5.04, T09.G5.01

**T28.G6.01.02**: Automate parameter sweeps with loops
**Description**: Students write a script that automatically loops through a range of parameter values (e.g., speed from 5 to 15 in steps of 1), runs 10 trials at each value, and stores average outcomes in a table. They identify the optimal parameter value by examining the table.
**Dependencies**: T28.G6.01.01, T07.G4.01

---

### SPLIT T28.G7.06 into two sub-skills:

**T28.G7.06.01**: Create multiple agent instances
**Description**: Students clone their single agent sprite to create 5 identical agents, each with independent random behavior. They verify all agents move independently by observing the simulation run for 20 time steps.
**Dependencies**: T28.G7.01, T06.G5.01

**T28.G7.06.02**: Track and display aggregate statistics
**Description**: Students calculate summary statistics (average x-position, count of agents in each state, total energy across all agents) and display these values on stage, updating them each time step using CreatiCode's statistical functions (average, min, max).
**Dependencies**: T28.G7.06.01, T10.G6.01, T27.G4.02c

---

## AFFECTED DOWNSTREAM DEPENDENCIES

When splitting skills, update these downstream skills that reference the old IDs:

### Skills depending on OLD T28.G4.02:
- T28.G4.03 → Change to T28.G4.02.03
- T28.G4.05 → Change to T28.G4.02.01
- T28.G5.01 → Delete this old skill (replaced by .01 and .02)
- T28.G5.05 → Change to T28.G4.02.03

### Skills depending on OLD T28.G5.01:
- T28.G5.07 → Change to T28.G5.01.02
- T28.G6.01 → Change to T28.G5.01.02
- T28.G6.03 → Change to T28.G5.01.02

### Skills depending on OLD T28.G6.01:
- T28.G7.04 → Change to T28.G6.01.02
- T28.G8.01 → Change to T28.G6.01.02
- T28.G8.02 → Change to T28.G6.01.02
- T28.G8.05 → Change to T28.G6.01.02

### Skills depending on OLD T28.G7.06:
- None found

---

## IMPLEMENTATION ORDER

1. **First**: Fix dependencies (5 skills) - SAFE, no downstream impact
2. **Second**: Enhance descriptions (12 skills) - SAFE, no downstream impact
3. **Third**: Add standalone new skills (T28.G4.06, G4.07, G5.08, G5.09, G5.10, G6.09, G6.10, G7.07) - UPDATE dependencies of later skills
4. **Fourth**: Split T28.G4.02 → UPDATE 4 downstream skills
5. **Fifth**: Split T28.G5.01 → UPDATE 3 downstream skills
6. **Sixth**: Split T28.G6.01 → UPDATE 4 downstream skills
7. **Seventh**: Split T28.G7.06 → No downstream updates needed
8. **Eighth**: Add T28.G3.07 (after all G4 changes complete)

---

## VALIDATION CHECKLIST

After implementation, verify:
- [ ] All 41 original skills still present (some renumbered with .01/.02)
- [ ] All NEW skills have proper sequencing (T28.Gx.## maintains grade order)
- [ ] No orphaned dependencies (every dependency ID exists)
- [ ] No circular dependencies within T28
- [ ] G2 skills remain unplugged/picture-based
- [ ] G3+ skills include coding components
- [ ] All split skills maintain logical flow (.01 → .02 → .03)
- [ ] Downstream dependency updates completed
