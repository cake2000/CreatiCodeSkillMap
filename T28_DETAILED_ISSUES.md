# T28 Detailed Issue Examples

This document provides concrete examples and rationale for each identified issue.

---

## HIGH PRIORITY: Missing Scaffolding Examples

### ISSUE 4A: G3→G4 Building Gap

**Current situation:**
- **T28.G3.06 (last G3 skill)**: "Students receive a simple 2-color spinner script and modify it to change the colors, the number of outcomes, or the range of random numbers."
  - Student role: MODIFY existing code
  - Complexity: Change values, maybe add one if-statement

- **T28.G4.01 (first G4 skill)**: "Students create a script that uses 'pick random 1-4' with if-statements to determine which of four colors was chosen, then report that color with a 'say' block."
  - Student role: BUILD from scratch
  - Complexity: Understand random-to-outcome mapping, create 4 if-statements, connect logic

**Why this is a problem:**
Students must leap from "change a value in existing code" to "design the entire control flow for a 4-outcome random generator." This requires:
1. Understanding the random→if→say pipeline
2. Knowing how to structure multiple if-statements
3. Translating "4 equal outcomes" into "random 1-4" with 4 conditionals

**What's missing:**
A skill where students ASSEMBLE pre-made blocks following explicit instructions, bridging "modify" and "create."

**Example proposed T28.G3.07 activity:**
```
Given blocks laid out on screen:
- [when green flag clicked]
- [pick random (1) to (2)]
- [if <result = 1> then]
- [say "Red" for 2 seconds]
- [if <result = 2> then]
- [say "Blue" for 2 seconds]

Task: Connect these blocks in the right order to create a working spinner.
```

This teaches structure without requiring design decisions.

---

### ISSUE 4B: Probability Calculation Appears Suddenly

**Current situation:**
- **T28.G4.02.03** (after split): Students calculate percentages from experimental data
  - Example: "Red appeared 23 times out of 50, so 23/50 × 100 = 46%"
  - Context: EXPERIMENTAL (we ran trials and counted)

- **T28.G5.05**: "Students determine the theoretical probability of simple events (rolling a specific number, flipping heads, choosing a colored marble from a bag) by counting favorable outcomes divided by total possible outcomes."
  - Example: "There are 3 red marbles and 4 total, so P(red) = 3/4 = 0.75"
  - Context: THEORETICAL (we calculate without running trials)

**Why this is a problem:**
Students haven't been introduced to the CONCEPT of probability as "expected frequency" before being asked to calculate it formally. They understand percentages from data but not "what should happen vs what did happen."

**What's missing:**
A skill that connects experimental percentages to theoretical expectations through reasoning, not just formula application.

**Example proposed T28.G4.06 activity:**
```
Scenario 1: Spinner with 4 equal sections (red, blue, green, yellow)
Question: "If you spin 100 times, about how many times would you expect red?"
Student reasoning: "There are 4 colors and they're equal, so red should be about 1 out of 4.
That's 25 out of 100."

Scenario 2: Bag with 3 red marbles, 1 blue marble
Question: "If you pick 100 times (putting the marble back each time), about how many times would you expect red?"
Student reasoning: "There are 3 red and 1 blue, so 3 out of 4 should be red.
That's 75 out of 100."
```

Then in T28.G5.05, students learn to write this as "3/4" or "0.75" - they already understand the concept.

---

### ISSUE 4D: Agent Concept Appears Without Introduction

**Current situation:**
- **T28.G6.05**: "Students create a sprite that tracks its position and facing direction in a grid (using x,y coordinates and a direction variable). They implement basic movement rules (move forward one grid square, turn left 90°, turn right 90°) and test the agent's movement."

**Why this is a problem:**
This skill introduces THREE new concepts simultaneously:
1. **Agent** as an entity with persistent state
2. **Grid world** abstraction (discrete positions vs continuous stage coordinates)
3. **Rule-based behavior** (formal movement rules)

Students haven't built anything with persistent state before (previous skills use variables for counters/scores, not entity attributes).

**What's missing:**
Experience creating sprites that "remember" their condition and behave accordingly.

**Example proposed T28.G5.08 activity:**
```
Create a sprite with a "mood" variable (values: 1=happy, 2=sad, 3=hungry)

Events:
- Green flag: Set mood to 1 (happy), sprite says "I'm happy!"
- Space key: Set mood to 2 (sad), sprite says "I'm sad..."
- Mouse click on sprite: Set mood to 3 (hungry), sprite says "Feed me!"

Add code that checks mood:
- If mood = 1, sprite shows costume "smile"
- If mood = 2, sprite shows costume "frown"
- If mood = 3, sprite shows costume "open-mouth"
```

This teaches "entity with state" before "agent in grid world."

---

## HIGH PRIORITY: Skills Too Broad Examples

### ISSUE 5A: T28.G4.02 Combines 3 Distinct Skills

**Current monolithic skill:**
"Learners extend their spinner to repeat 50 times, append results to a list, and calculate percentage for each color."

**Why this is too broad:**
This actually teaches THREE independent concepts:

1. **List accumulation in loops**
   - Concept: Using "repeat" + "add to list" to collect data
   - Common errors: Forgetting to clear the list first, adding the wrong value
   - Assessment: Can the student collect trial data?

2. **Frequency counting**
   - Concept: Iterating through a list to count occurrences
   - Common errors: Off-by-one errors, not resetting counters, counting the wrong outcome
   - Assessment: Can the student count categories?

3. **Percentage calculation**
   - Concept: Converting counts to percentages (count/total × 100)
   - Common errors: Wrong formula, division order, forgetting ×100
   - Assessment: Can the student compute proportions?

**If a student fails T28.G4.02, what do they need to relearn?**
We can't tell! They might understand loops and lists but struggle with division. Or they might calculate percentages fine but make loop errors.

**Proposed split:**

**T28.G4.02.01** (Focus: Data collection)
```
given: A working random color generator (red/blue)
Task: Add a repeat 50 loop and "add [result] to [results]" block
Success: List contains 50 entries
```

**T28.G4.02.02** (Focus: Counting)
```
Given: List with 50 color names
Task: Write code to count reds and blues
Success: "Red: 23, Blue: 27" (counts sum to 50)
```

**T28.G4.02.03** (Focus: Percentage calculation)
```
Given: Red count = 23, Blue count = 27
Task: Calculate and display percentages
Success: "Red: 46%, Blue: 54%"
```

Now we can assess each skill independently and provide targeted help.

---

### ISSUE 5B: T28.G5.01 Too Complex

**Current monolithic skill:**
"Students roll two virtual dice 200 times, store sums, and explain why 7 is most common by referencing combinations."

**Complexity breakdown:**
1. Create two independent random generators (pick random 1-6 twice)
2. Add the two values together
3. Store the result in a variable
4. Wrap in a 200-iteration loop
5. Collect all sums in a list
6. Count frequency of each sum (2, 3, 4... 12)
7. Create a bar chart showing distribution
8. Analyze which sum is most common
9. EXPLAIN theoretically why 7 is most common (list combinations: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1)

**This involves:**
- Variables (at least 3: die1, die2, sum)
- Lists (to store 200 results)
- Loops (200 iterations)
- Frequency analysis (11 possible sums to count)
- Data visualization (bar chart with 11 bars)
- Theoretical probability (combinatorics)

**If a student completes this, what have they learned?**
Too many things to assess individually!

**Proposed split:**

**T28.G5.01.01** (Focus: Compound random events)
```
Task: Create variables die1, die2, sum
Generate two random numbers (1-6)
Add them: sum = die1 + die2
Display sum with "say" block
Click green flag 10 times and observe sums vary from 2-12
```
Assessment: Can student create and combine random generators?

**T28.G5.01.02** (Focus: Compound event analysis)
```
Task: Wrap the above in "repeat 200"
Collect sums in a list
Create frequency table: sum value (2-12) → how many times
Make bar chart showing frequencies
Identify most common sum
Explain why by listing combinations for that sum
```
Assessment: Can student analyze patterns in compound events?

---

## MEDIUM PRIORITY: Vague Description Examples

### ISSUE 8F: T28.G8.01 Needs Concrete Specification

**Current vague description:**
"Students automate simulations, store results, and auto-refresh charts/HUD elements so stakeholders can explore scenarios live."

**Problems:**
- "Automate simulations" - how? Triggered by what?
- "Auto-refresh charts" - using what mechanism?
- "Stakeholders can explore scenarios" - what interface?
- What specific skills are being assessed?

**What does a complete student project look like?**
Without specificity, students might create:
- A button that reruns a simulation (too simple)
- A complex multi-parameter dashboard (too hard)
- A script that runs scenarios in sequence (wrong interpretation)

**Improved concrete description:**
"Students create an interactive dashboard with:
1. A variable for a tunable parameter (e.g., enemy speed slider)
2. A broadcast message system: when parameter changes → broadcast 'run simulation'
3. A receiving script that: runs simulation with current parameter → updates results table
4. A chart that automatically refreshes when table updates
5. Testing: Students change the parameter 3 times and verify chart updates correctly each time

Assessment deliverable: Working dashboard where changing a slider updates the chart within 2 seconds"

**Now the skill is assessable:**
- Does the parameter change trigger simulation? (Yes/No)
- Does the table update with new results? (Yes/No)
- Does the chart refresh automatically? (Yes/No)
- Does it work for multiple parameter values? (Yes/No)

---

### ISSUE 8G: T28.G8.03 AI Integration Vague

**Current vague description:**
"Students summarize simulation outcomes (key statistics, trends), pass them to an AI assistant (like CreatiCode's XO), and evaluate whether the AI's recommendations align with the data."

**Problems:**
- "Summarize outcomes" - what format? How detailed?
- "Pass them to an AI assistant" - copy-paste? API? Export?
- "Evaluate whether recommendations align" - what criteria?
- What if the AI gives poor advice? Is that a student error or AI limitation?

**Improved concrete description:**
"Students complete these steps:
1. Run their simulation and export a summary text file containing:
   - Scenario description (1 sentence)
   - Key statistics (mean, median, range - formatted as table)
   - Main finding (1 sentence: 'Setting A performed better than B by X%')
2. Paste this summary into CreatiCode's AI assistant chat
3. Read the AI's response
4. Write 2-3 sentences answering:
   - Did the AI correctly identify your main finding? (Quote the relevant part)
   - Do the AI's suggested next steps make sense given your data? Why or why not?
   - What did the AI miss or misunderstand?

Assessment: Student's written evaluation demonstrates critical thinking about AI interpretation"

**Now we can assess:**
- Can student create a clear data summary? (formatting, completeness)
- Can student identify accurate vs inaccurate AI interpretation? (critical reading)
- Can student justify their evaluation with evidence? (reasoning)

---

## DEPENDENCY VIOLATION EXAMPLES

### ISSUE 2A: T28.G3.06 Redundant Dependencies

**Current dependencies:**
```
T28.G3.06: Modify a teacher-provided random generator
Dependencies:
* T28.G3.02: Explain what "pick random" does by testing predictions
* T28.G3.03: Record experimental data with teacher-provided blocks
```

**Dependency chain:**
```
T28.G3.02 (explain pick random)
    ↓
T28.G3.03 (record data - depends on G3.02)
    ↓
T28.G3.06 (modify generator - depends on BOTH G3.02 and G3.03)
```

**Why this is redundant:**
If T28.G3.06 depends on T28.G3.03, and T28.G3.03 already depends on T28.G3.02, then G3.06 automatically has G3.02 as a transitive dependency.

Listing both creates clutter and potential confusion: "Do I need to complete G3.02 separately before G3.06, or is completing G3.03 sufficient?"

**Corrected dependencies:**
```
T28.G3.06: Modify a teacher-provided random generator
Dependencies:
* T28.G3.03: Record experimental data with teacher-provided blocks
```

Students must still complete G3.02 (because G3.03 requires it), but we don't list it twice.

---

### ISSUE 9A: T28.G4.01 Over-Specified Dependencies

**Current dependencies:**
```
T28.G4.01: Build a simple random generator
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T28.G3.02: Explain what "pick random" does by testing predictions
```

**What T28.G4.01 actually requires:**
Looking at the skill description: "Students create a script that uses 'pick random 1-4' with if-statements to determine which of four colors was chosen, then report that color with a 'say' block. They click the green flag multiple times to verify each color can appear."

**Actual code structure:**
```
when green flag clicked
set [result] to (pick random 1 to 4)
if <result = 1> then
  say [Red] for 2 seconds
end
if <result = 2> then
  say [Blue] for 2 seconds
end
... (2 more ifs)
```

**Skills actually needed:**
- ✅ T06.G3.01 (green flag script) - YES, used
- ❌ T07.G3.05 (fix repeat loop) - NO LOOP in this skill!
- ✅ T08.G3.01 (use if) - YES, core skill
- ❌ T09.G3.05 (trace variables) - Not required; students just run and observe
- ✅ T28.G3.02 (understand pick random) - YES, core skill

**Corrected dependencies:**
```
T28.G4.01: Build a simple random generator
Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.01: Use a simple if in a script
* T28.G3.02: Explain what "pick random" does by testing predictions
```

Removed T07.G3.05 (no loop used) and T09.G3.05 (tracing not required for this task).

---

## MISSING COVERAGE EXAMPLES

### ISSUE 10B: Expected Value Not Taught

**Why this matters:**
Expected value connects theoretical probability to practical decision-making. It's the bridge between "what are the chances?" and "is this a good choice?"

**Real-world applications students understand:**
- Should I spend $1 to spin a wheel that gives $5 with 25% probability? (EV = $1.25, yes!)
- Which game is better: guaranteed 5 points vs 50% chance of 12 points? (EV = 6, second is better)
- Is it worth paying 10 tickets to play a game where you win 50 tickets 15% of the time? (EV = 7.5 tickets, losing deal)

**Current gap:**
Students in T28.G5.05 learn to calculate probabilities (e.g., "30% chance of winning").
Students in T28.G5.06 compare experimental vs theoretical frequencies.
But no skill teaches: "If you play 100 times, how many total points do you expect?"

**Proposed T28.G6.10:**
```
Scenario: Spinner game
- Red (50%): win 10 points
- Blue (30%): win 5 points
- Green (20%): win 0 points

Task 1: Calculate expected value
Expected = (0.5 × 10) + (0.3 × 5) + (0.2 × 0) = 5 + 1.5 + 0 = 6.5 points per spin

Task 2: Run simulation
Repeat 100 times:
  - Spin and record points won
  - Add to total
Calculate average points per spin

Task 3: Compare
Expected value: 6.5
Simulation average: [varies, typically 6.2-6.8]
Explain: They should be close; more trials would match better

Task 4: Apply
A second game offers guaranteed 7 points per spin.
Which game is better long-term? Explain using expected value.
```

---

### ISSUE 10G: Gambler's Fallacy Not Addressed

**Why this matters:**
Students (and adults!) often believe "I've gotten heads 5 times in a row, so tails is due!" This fundamental misunderstanding of independence affects decision-making in games, statistics, and even things like weather prediction.

**T28 teaches randomness but never explicitly addresses independence of trials**

**Current related skills:**
- T28.G5.06: Compare experimental and theoretical probability
  - Teaches: probabilities stay constant across many trials
  - Doesn't teach: each trial is independent

- T28.G6.06: Simulate events with changing probabilities
  - Teaches: when probabilities DO change (dependent events)
  - Doesn't teach: how to recognize when they DON'T change

**Proposed T28.G5.10:**
```
Investigation: Does a coin "remember" previous flips?

Task 1: Run simulation
Repeat 1000 coin flips
Track sequences: count when "heads after heads" vs "tails after heads"

Task 2: Calculate conditional frequencies
P(heads | previous was heads) = [count HH] / [count of any result after H]
P(heads | previous was tails) = [count TH] / [count of any result after T]

Expected result: Both should be ≈ 50%

Task 3: Explain
"Even after 5 heads in a row, the next flip still has 50% chance of heads because the coin has no memory. Each flip is independent."

Task 4: Real-world connection
Discuss why people think "I'm due for a win" after losses in games.
Explain why this is false for independent random events.
```

This directly addresses a crucial misconception and connects to responsible gaming/gambling literacy.

---

## CREATICODE FEATURE MATCH EXAMPLES

### ISSUE 7A: Random Without Repetition Not Scaffolded

**Platform capability:**
CreatiCode has a "pick random from [list] without repetition" block.

**Why this matters:**
Many realistic simulations require this:
- Dealing cards (can't deal the same card twice)
- Selecting survey participants (can't survey same person twice)
- Random team assignment (can't assign person to multiple teams)
- Raffle drawings (can't win twice)

**Current T28 skills:**
All random selection uses "pick random 1 to N" or "pick random item from list" - both allow repetition.

**Students will discover this feature and use it incorrectly:**
Example confusion:
```
Student: "I want to deal 5 cards from a deck"
Student code: repeat 5 [add (pick random from [deck]) to [hand]]
Result: Might get same card multiple times!

Better code: repeat 5 [add (pick random from [deck] without repetition) to [hand]]
```

**But no T28 skill teaches when/how to use this!**

**Proposed T28.G5.09:**
```
Scenario A: Survey with replacement
- Pick 10 random students from class list
- Same student might be picked multiple times
- Code: repeat 10 [add (pick random from [class]) to [selected]]

Scenario B: Survey without replacement
- Pick 10 different students from class list
- Each student selected at most once
- Code: repeat 10 [add (pick random from [class] without repetition) to [selected]]

Task:
1. Run both simulations 5 times each
2. Check if any names appear multiple times in lists
3. Explain when each approach is appropriate:
   - With replacement: Testing where the same thing can happen multiple times
   - Without replacement: Selecting distinct items (cards, people, etc.)
```

This teaches a platform-specific feature that's essential for realistic simulations.

---

### ISSUE 7B: Seeds Introduced Too Late for Debugging

**Platform capability:**
CreatiCode supports setting random seeds for reproducible sequences.

**Current skill:**
T28.G6.02 (Grade 6): "Learners set a seed value before running a simulation, observe the sequence of random outputs, then reset and rerun with the same seed to verify identical results. They explain why reproducibility matters for debugging and sharing results with others."

**Problem:**
Students start debugging random simulations in G4 (T28.G4.04: Debug an "unfair" simulation), but don't learn about seeds until G6.

**Real debugging scenario without seeds (G4):**
```
Student: "My simulation seems unfair, blue appears more often"
Student runs simulation: Red 23, Blue 27
Student: "See, blue wins!"
Student runs again: Red 26, Blue 24
Student: "Wait, now red wins? Is it fair or not?"
Student runs 10 more times, gets different results each time
Student: "I can't tell what's wrong!"
```

**Same debugging scenario with seeds (should be G4):**
```
Student: "My simulation seems unfair"
Student sets seed to 42
Student runs simulation: Red 23, Blue 27
Student: "Let me check my code..."
Student runs again with seed 42: Red 23, Blue 27 (SAME RESULT)
Student: "The randomness is the same, so I can debug the counting logic"
Student finds bug (counting blue twice), fixes it
Student runs with seed 42: Red 25, Blue 25
Student: "Fixed! Now let me try different seeds to be sure..."
```

**Recommendation:**
Keep T28.G6.02 for advanced reproducibility concepts (sharing results, scientific reproducibility).

Add T28.G4.07 for debugging use:
```
Debugging with seeds

Problem: When testing random code, results change each run, making bugs hard to find.

Solution: Set a random seed to get the same random sequence each time.

Task:
1. Run your buggy simulation without a seed - observe results vary
2. Set seed to 100, run 3 times - observe identical results
3. Fix the bug while using seed 100 (so you know if your fix works)
4. Remove seed and run 10 times - verify all results now look fair

Explain: Seeds make random behavior predictable during testing, but remove the seed in the final version so users get varied experiences.
```

This teaches seeds as a debugging tool when students first need it.

---

## SUMMARY: Impact of Changes

### Current T28: 41 skills, multiple gaps and inefficiencies

**Problems:**
- 5 scaffolding gaps where students struggle to progress
- 4 overly broad skills that confound multiple learning objectives
- 12 vague descriptions that make assessment difficult
- 7 important probability concepts not explicitly addressed
- Several platform features not taught

### Optimized T28: ~53-56 skills, clear progression, comprehensive coverage

**Improvements:**
- All gaps filled with intermediate skills
- Complex skills split for independent assessment
- Every skill has concrete, assessable description
- All core probability concepts covered (independence, expected value, sampling bias)
- Platform features (seeds, no-repetition) taught when needed
- Cleaner dependency structure (removed redundancies)

**Student experience:**
- Clearer progression from G2→G8
- Better chance of success at each level (appropriate scaffolding)
- Deeper understanding of probability concepts
- More powerful simulation capabilities by G8
- Real-world applications (fairness testing, policy analysis)

**Teacher experience:**
- Can pinpoint exactly where student struggles (narrower skills)
- Clearer assessment criteria (specific descriptions)
- Better alignment with standards (explicit probability concepts)
- More examples of what "success" looks like

---
