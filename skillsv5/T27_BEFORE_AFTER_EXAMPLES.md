# T27 Optimization - Before/After Examples

This document shows concrete examples of the most impactful changes to T27 (Chance & Simulations).

---

## Example 1: Fixing Vague Verbs (T27.GK.02)

### BEFORE
```
ID: T27.GK.02
Skill: Identify "maybe" events using picture cards
Description: Students examine illustrated picture cards showing events with
uncertain outcomes (will it rain today? will I pick a red crayon from a mixed
box?). They place these "maybe" cards in a middle pile between "will happen"
and "won't happen" bins. This introduces the idea that some events are
uncertain—we don't know if they will happen until we try.
```

**Problem:** "Identify" is passive recognition. Students could just watch the teacher sort.

### AFTER
```
ID: T27.GK.02
Skill: Select "maybe" events from picture cards and test predictions
Description: Students examine 8 illustrated picture cards showing events. They
**select** cards showing uncertain outcomes (will it rain today? will I pick a
red crayon from a mixed box?) and place them in a "maybe" pile. Then they
**test** one scenario (e.g., pick from a real crayon box 3 times) to observe
that outcomes vary—reinforcing that "maybe" means "we don't know until we try."
```

**Impact:**
- Active verb: "Select" requires student action
- Added testing component: Makes it auto-gradable (did outcomes vary?)
- Specific number: "8 cards" (not "illustrated picture cards")

---

## Example 2: Filling Critical Gap (NEW T27.G2.05)

### THE GAP
**G2.04 ended with:** Physical coin flips, manual recording with stickers
**G3.01 jumped to:** Reading bar charts from CreatiCode simulations

Students had no introduction to the CreatiCode interface before analyzing data!

### THE SOLUTION
```
ID: T27.G2.05 [NEW]
Topic: T27 – Chance & Simulations
Skill: Watch a CreatiCode spinner simulation and match outcomes to pictures
Description: Students open a provided CreatiCode project showing a spinner
sprite. When they **click the green flag**, the spinner rotates and stops on
one of 4 colors. Students **run** the simulation 5 times and **match** each
outcome to a picture chart by placing a check mark. This unplugged-to-plugged
bridge introduces the CreatiCode stage interface and the concept that
"spinning the spinner = clicking green flag" before they analyze data charts.

Dependencies:
* T27.G2.04: Predict and observe outcomes
* T06.G2.01: Click the green flag and observe what happens
```

**Impact:**
- Smooth transition: Physical → digital
- Interface introduction: Green flag, stage, sprites
- Concrete activity: Match 5 outcomes (assessable)
- Sets up G3.01: Now students know how simulations work before reading charts

---

## Example 3: Enhanced K-2 Concrete Scenarios (T27.GK.01)

### BEFORE
```
Description: Students sort 6-8 illustrated picture cards showing everyday
events into two labeled bins: "will happen" (certain events like the sun
coming up, a dropped ball falling down) and "won't happen" (impossible events
like a fish flying in the sky, ice staying frozen in hot sun).
```

**Problem:** "6-8 cards" is vague. "Illustrated picture cards" doesn't tell teachers what to draw.

### AFTER
```
Description: Students sort **8 illustrated picture cards** showing specific
everyday events into two labeled bins:

- **"Will Happen"** (certain): Sun coming up tomorrow, a dropped ball falling
  down, ice melting in hot sun, a plant needing water to grow

- **"Won't Happen"** (impossible): Fish flying in the sky, ice staying frozen
  in hot sun, a person jumping to the moon without a rocket, water flowing uphill

After sorting, students **point to** one card from each bin and **say** why it
goes there. This unplugged activity introduces that some events are predictable
while others cannot occur.

**Success criterion:** All 8 cards sorted correctly.
```

**Impact:**
- Exact number: 8 cards (not "6-8")
- Specific examples: Teachers know exactly what to create
- Verification step: Point and explain (not just sort passively)
- Clear success criterion: All 8 correct

---

## Example 4: Breaking Down Overly Broad Skills (T27.G5.04)

### BEFORE (One broad skill)
```
ID: T27.G5.04
Skill: Write a simulation plan before coding
Description: Before building a simulation, students write a plan with 5 parts:
(1) Question: What am I trying to find out?
(2) Random model: What will be random?
(3) Variables: What will I track?
(4) Trials: How many times will I run it?
(5) Success metric: How will I know it worked?
```

**Problem:** 5 components is too much for one skill. Students can't master all at once.

### AFTER (Two focused skills)

```
ID: T27.G5.04.01
Skill: Define simulation question, variables, and trials
Description: Before building a simulation, students write a planning document
with 3 components:
1. **Question:** What am I trying to find out? (e.g., "How often does a team
   with 60% win rate win 3 games in a row?")
2. **Variables to track:** What will I measure? (e.g., wins, losses, streak length)
3. **Number of trials:** How many times will I run it? (At least 100 for stable results)

They **review** example plans and **identify** which are well-defined vs. vague.
This prevents "just start coding" without clear goals.
```

```
ID: T27.G5.04.02
Skill: Choose random model and define success criteria
Description: Students extend their simulation plan by adding:
4. **Random model:** What will be random? How will I model it? (e.g., "Each game
   = pick random 1 to 100. If ≤ 60, team wins.")
5. **Success criteria:** How will I know my simulation works? (e.g., "Overall
   win rate should be close to 60%")

They **compare** two models for the same problem and **explain** which is more
realistic. They **test** their success criterion after running the simulation.

Dependencies:
* T27.G5.04.01: Define simulation question, variables, and trials
```

**Impact:**
- IXL-style micro-progression: Master question/variables/trials first
- Then add complexity: Random model and success criteria
- Each skill is now focused and assessable
- Dependency ensures proper sequencing

---

## Example 5: Adding AI-Era Depth (NEW T27.G7.08)

### THE OPPORTUNITY
Current T27 teaches simulations well, but limited connection to how AI systems use probability.

### THE SOLUTION
```
ID: T27.G7.08 [NEW]
Topic: T27 – Chance & Simulations
Skill: Simulate AI confidence scores and test decision thresholds
Description: Students simulate an AI vision system with confidence scores.
Their simulation:
1. **Generates** 200 fake detections: object type (cat/dog/car) and confidence (0-100%)
2. **Applies** threshold rules: If confidence > 80%, accept; if 50-80%, "uncertain"; if < 50%, reject
3. **Tests** different thresholds (50%, 70%, 90%) and **calculates**: How many
   acceptances at each threshold?
4. **Analyzes** tradeoff: Higher threshold = fewer errors but also fewer detections

They **connect** to real AI: Self-driving cars must decide confidence threshold
for detecting pedestrians.

Dependencies:
* T27.G6.04: Simulate noisy sensors for AI perception testing
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T21.G5.01: Make an XO model prediction and interpret results
```

**Impact:**
- Connects simulations to real AI systems
- Teaches critical AI concept: Confidence scores aren't binary true/false
- Explores tradeoffs: Safety (high threshold) vs. utility (low threshold)
- Real-world relevance: Self-driving cars, medical diagnosis, content moderation

---

## Example 6: Adding Visual Models (NEW T27.G4.08)

### THE GAP
Students jump from counting frequencies (G4.02.03) to calculating theoretical
probability with fractions (G5.05) without visual connection between area and probability.

### THE SOLUTION
```
ID: T27.G4.08 [NEW]
Topic: T27 – Chance & Simulations
Skill: Draw area models to represent probability as part-of-whole
Description: Students create visual area models to represent probability before
running simulations. For a 4-section spinner, they **draw** a circle divided
into 4 equal parts and **label** each section 1/4 or 25%. For an unfair spinner
(half red, quarter blue, quarter green), they **draw** sections sized
proportionally and **label** 1/2, 1/4, 1/4. Then they **run** a CreatiCode
simulation of each spinner (50 trials) and **compare**: Did results match the
area fractions? This connects geometric reasoning to probability.

Dependencies:
* T27.G4.02.03: Calculate percentages from frequency counts
* T26.G4.04: Interpret circle graphs (pie charts)
```

**Impact:**
- Visual bridge: Area → Fraction → Percentage → Probability
- Connects to existing math knowledge (pie charts)
- Test understanding: Draw prediction, then verify with simulation
- Prepares for formal probability in G5

---

## Example 7: Combining Active Verbs (T27.G8.05)

### BEFORE
```
ID: T27.G8.05
Skill: Analyze how environment design biases agent behavior
```

**Problem:** "Analyze" is vague. What does "analyze" mean? Just look at it?

### AFTER
```
ID: T27.G8.05
Skill: Compare agent learning across two maze designs and measure bias
Description: Students run the same learning agent in two mazes: Maze A (one
clear path) and Maze B (multiple paths, one much shorter). They **run** 50
trials in each maze and **record**:
(1) average steps to goal
(2) most common path taken
(3) percentage of trials where shortest path was found

They **calculate** the "bias metric": (average steps - optimal steps) / optimal steps.

They **compare** the two mazes and **explain**: "Maze B creates bias because
early random success can lock in suboptimal paths."

They **connect** to AI training: How does data environment create bias?
```

**Impact:**
- Replaced "Analyze" with 5 active verbs: Run, Record, Calculate, Compare, Connect
- Specific measurements: "bias metric" with formula
- Clear process: 50 trials → record → calculate → compare → explain
- Real AI connection: Training environment creates bias

---

## Summary of Patterns

### Pattern 1: Vague → Specific + Test
**Before:** "Identify X"
**After:** "Select X and test by..."

### Pattern 2: Passive → Active + Measure
**Before:** "Analyze how X affects Y"
**After:** "Run X, measure Y, calculate difference, compare, explain"

### Pattern 3: General → Specific Examples
**Before:** "illustrated picture cards"
**After:** "8 cards showing: sun rising, ball falling, ice melting, plant growing..."

### Pattern 4: Broad → Micro-Steps
**Before:** One skill with 5 components
**After:** Two skills: Components 1-3, then components 4-5

### Pattern 5: Isolated → Connected
**Before:** Skill teaches concept in isolation
**After:** Skill connects to real AI applications (confidence scores, bias, training data)

---

## Teaching Implications

### For Teachers
- **Clearer instructions:** "8 specific cards" vs. "some illustrated cards"
- **Assessable outcomes:** "All 8 sorted correctly" vs. "students explore sorting"
- **Progressive complexity:** Teach question/variables first, then add model/criteria

### For Students
- **Active learning:** Select, test, compare, calculate (not just watch)
- **Immediate feedback:** Run simulation → see if prediction matched
- **Real-world relevance:** Every simulation connects to games, AI, or real problems

### For Assessment
- **Auto-gradable:** "Did all 8 cards sort correctly?" (yes/no)
- **Measurable:** "Calculate bias metric" (numeric answer)
- **Demonstrable:** "Run 5 times and match outcomes" (observable)

---

## Next Steps for Implementation

1. **Review these examples** with curriculum team
2. **Pilot test G2.05** (bridge skill) - most critical
3. **Create templates** for new skills (G4.08 area models, G7.08 confidence scores)
4. **Update assessment rubrics** based on new active verbs
5. **Train teachers** on the difference: "identify" vs. "select and test"

---

**Full Plan:** See `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv5/T27_OPTIMIZATION_PLAN.md` for complete details on all 78 skills.
