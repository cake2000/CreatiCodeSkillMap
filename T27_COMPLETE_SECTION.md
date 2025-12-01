# T27 - Chance & Simulations (Phase 9 Optimized - November 2025)
# Applied Phase 9 topic-focused optimizations:
# MAJOR CHANGES IN PHASE 9:
# 1. NEW K-2 Scaffolding Skills:
#    - T27.GK.00: Sort events by "always/never" using weather pictures (prerequisite to GK.01)
#    - T27.GK.01.02: Identify events that depend on nature vs choices
#    - T27.G1.00: Connect prediction to real outcomes with sticker feedback
#    - T27.G2.00: Compare two random tools and identify which has more possibilities
# 2. NEW Debugging Progression for Simulations:
#    - T27.G3.09: Debug a simulation with wrong outcome count
#    - T27.G4.04.01: Trace probability flow through if-else chains
#    - T27.G4.04.02: Fix off-by-one errors in probability calculations
#    - T27.G5.12: Validate simulation correctness using expected value
# 3. NEW Advanced Simulation Types (G6-G8):
#    - T27.G6.12: Build a waiting line (queue) simulation
#    - T27.G7.08: Simulate disease spread with infection probability
#    - T27.G7.09: Model weather using Markov chain transitions
#    - T27.G8.13: Design and validate an epidemiological simulation (capstone)
#    - T27.G8.14: Build agent-based environmental model
# 4. Split Broad Skills for Granularity:
#    - T27.G5.03 (Monte Carlo π) → G5.03.01 (setup) + G5.03.02 (calculate + visualize)
#    - T27.G6.06 → G6.06.01 (with replacement) + G6.06.02 (without replacement) + G6.06.03 (compare)
#    - T27.G8.04 → G8.04.01 (structure) + G8.04.02 (evidence) + G8.04.03 (defense)
# 5. Enhanced Real-World Applications:
#    - Environmental simulations (population dynamics, climate)
#    - Public health (epidemiology, disease spread)
#    - Civic data (voting, resource allocation)
# 6. Improved Verb Quality:
#    - "Understand" → "Trace and explain"
#    - "Know about" → "Demonstrate through simulation"
#    - All K-2 skills have detailed visual scenarios
# 7. Fixed Dependencies:
#    - All intra-topic deps verified for X-2 rule
#    - Removed redundant cross-topic deps
# Total: 99 skills (added 26 new skills for scaffolding, debugging, validation, and advanced simulation types)

ID: T27.GK.00
Topic: T27 – Chance & Simulations
Skill: Sort weather events by "always happens" and "never happens"
Description: **Student task:** Sort 6 picture cards showing weather events into two bins: "always happens" (every day) and "never happens" (impossible). **Visual scenario:** Cards show: (A) sun in sky during daytime, (B) clouds in sky, (C) rain falling from clouds—these are weather events that DO happen. Cards showing: (D) snow falling in summer at the beach, (E) rainbow at night (impossible—needs sun), (F) clouds on the ground (fog is different!)—help students identify tricky ones. **Simplified for K:** Start with just "always" and "never"—no middle category yet. **Success criteria:** Sort at least 5 of 6 correctly. **Discussion prompt:** "Can YOU make it rain? Or does weather just happen?" _Implementation note: Large picture cards with audio. Simpler than GK.01 by avoiding abstract events._

Dependencies:
(none)



ID: T27.GK.01
Topic: T27 – Chance & Simulations
Skill: Sort picture cards into "will happen" and "won't happen"
Description: **Student task:** Sort 8 illustrated picture cards into two labeled bins: "will happen" and "won't happen." **Visual scenario:** Picture cards show: (A) sun rising tomorrow, (B) dropped ball falling down, (C) ice melting in hot sun, (D) water flowing downhill—these go in "will happen." Cards showing: (E) fish flying in the sky, (F) ice staying frozen in boiling water, (G) person walking through walls, (H) cat speaking English—these go in "won't happen." **Materials:** 8 large laminated cards, 2 sorting bins. **Success criteria:** All 8 cards sorted correctly. _Implementation note: Drag-drop interface with audio support reading card descriptions. Auto-graded by final positions._

Dependencies:
* T27.GK.00: Sort weather events by "always happens" and "never happens"




ID: T27.GK.01.01
Topic: T27 – Chance & Simulations
Skill: Explain why some events always happen using picture examples
Description: **Student task:** Select the picture that shows WHY an event always happens. **Visual scenario:** Show 4 picture pairs: (A) "Ball falls" → student picks reason: "gravity pulls down" (picture of arrow pointing down), (B) "Ice melts in sun" → "sun is hot" (picture of sun with heat lines). Multiple choice for each. **Discussion prompt:** "The sun ALWAYS rises. Can anyone stop it?" (No—nature's rules). **Key concept:** Some events follow rules that never break. **Success criteria:** Match 3 of 4 events to correct reasons. _Implementation note: Matching game with picture-based reasons._

Dependencies:
* T27.GK.01: Sort picture cards into "will happen" and "won't happen"




ID: T27.GK.01.02
Topic: T27 – Chance & Simulations
Skill: Identify events that depend on nature vs events that depend on choices
Description: **Student task:** Sort 6 picture cards into "Nature decides" and "I can choose." **Visual scenario:** "Nature decides" cards: (A) rainy day picture (you can't choose weather), (B) leaves falling in autumn, (C) sun setting in evening. "I can choose" cards: (D) picking a red or blue crayon, (E) choosing to share a cookie or not, (F) deciding to walk or skip to school. **Discussion prompt:** "Can you make it stop raining? No—nature decides! But can you choose which crayon to pick? Yes!" **Key concept:** Some things are beyond our control (nature, luck), others are our choice. This builds toward understanding randomness. **Success criteria:** Sort 5 of 6 correctly. _Implementation note: Two-bin sorting with audio explanations for each card._

Dependencies:
* T27.GK.01.01: Explain why some events always happen using picture examples




ID: T27.GK.02
Topic: T27 – Chance & Simulations
Skill: Select "maybe" events and place them in the middle bin
Description: **Student task:** Given 6 new picture cards, select those showing uncertain events and place them in a "maybe" bin between "will happen" and "won't happen." **Visual scenario:** Cards show: (A) "Will it rain today?" with clouds in sky, (B) "Will I pick a red crayon?" showing hand reaching into mixed crayon box, (C) "Will the coin land heads?" showing a flipping coin, (D) "Will the spinner land on blue?" showing a 4-color spinner. The "will happen" and "won't happen" cards from GK.01 remain in their bins as anchors. **Success criteria:** Student correctly identifies 4+ cards as "maybe" events. **Discussion prompt:** "Why can't we know for sure what will happen?" _Implementation note: Three-bin sorting with audio confirmation. Auto-graded by correct placements._

Dependencies:
* T27.GK.01.02: Identify events that depend on nature vs events that depend on choices




ID: T27.GK.02.01
Topic: T27 – Chance & Simulations
Skill: Match random tools to their outcomes using picture cards
Description: **Student task:** Match 4 picture cards of random tools (coin, die, spinner, grab bag) to picture cards showing their possible results. **Visual scenario:** Tools: (A) coin → heads or tails pictures, (B) 6-sided die → numbers 1-6 dots, (C) 4-color spinner → color circles, (D) bag with mixed candies → different candy colors. **Procedure:** Drag each tool card to its matching outcome card set. **Discussion prompt:** "What makes these tools special? We don't know what will happen until we try!" **Key concept:** Random tools give different results each time. **Success criteria:** Match all 4 tools to correct outcome sets. _Implementation note: Drag-to-match interface with visual outcome cards._

Dependencies:
* T27.GK.02: Select "maybe" events and place them in the middle bin




ID: T27.GK.03
Topic: T27 – Chance & Simulations
Skill: Spin a picture spinner and compare results to hopes
Description: **Student task:** Spin a 4-color paper spinner 5 times. Before each spin, tap the color you hope to land on. After spinning, tap the color you actually landed on. **Visual scenario:** Digital spinner with 4 equal sections (red, blue, green, yellow). Screen shows two columns: "I hoped for" and "I got." After 5 spins, student sees comparison table. **Key observation:** Students notice their hopes didn't control outcomes—sometimes they got what they hoped for, sometimes not. **Discussion prompt:** "Could you make the spinner land where you wanted? Why not?" **Success criteria:** Complete 5 spins and answer reflection question. _Implementation note: Animated spinner with tap-to-select prediction before each spin. Records hope vs outcome for comparison._

Dependencies:
* T27.GK.02.01: Match random tools to their outcomes using picture cards




ID: T27.GK.04
Topic: T27 – Chance & Simulations
Skill: Count items in a picture bag and predict which color is easiest to pick
Description: **Student task:** Look at a picture of a bag with colored balls visible inside. Count each color and predict which is easiest to pick randomly. **Visual scenario:** Transparent bag shows: 5 red balls, 2 blue balls, 1 green ball. **Questions:** (1) "How many red balls?" (5), (2) "How many blue balls?" (2), (3) "If you close your eyes and pick one, which color will you PROBABLY get?" (Red—there are more red). **Discussion prompt:** "Why is red easier to pick? Because there are MORE of them!" **Key concept:** More items = easier to pick randomly. **Success criteria:** Count all colors correctly, predict most likely color. _Implementation note: Interactive counting with highlight feature._

Dependencies:
* T27.GK.03: Spin a picture spinner and compare results to hopes




ID: T27.G1.00
Topic: T27 – Chance & Simulations
Skill: Connect prediction to outcome using picture matching
Description: **Student task:** Make a prediction before a random event, then match prediction to actual outcome. **Visual scenario:** Three activities: (1) Spinner with 2 colors—student taps prediction color, watches spin, taps to match if correct. (2) Grab bag with shapes visible—predict circle or square, see what's drawn. (3) Weather forecast tomorrow—sunny or cloudy guess, return next day to compare. **Key insight:** "Did what you hoped for actually happen? Sometimes yes, sometimes no!" **Discussion prompt:** "Why can't we always be right when we guess about 'maybe' things?" **Purpose:** Bridges GK "maybe" concept to G1 formal prediction-vs-outcome recording. **Success criteria:** Complete all 3 activities, correctly identify matches. _Implementation note: Simple tap-to-predict, animate event, tap-to-match interface._

Dependencies:
* T27.GK.04: Count items in a picture bag and predict which color is easiest to pick




ID: T27.G1.01
Topic: T27 – Chance & Simulations
Skill: Predict coin flips and record outcomes with stickers
Description: **Student task:** Predict "heads" or "tails" before each of 6 coin flips, then record what actually happens. **Visual scenario:** Recording sheet with two columns labeled with pictures: coin showing heads, coin showing tails. Before each flip, student taps prediction (heads/tails picture). After flip, student places a virtual sticker in the correct column. **Procedure:** (1) Tap prediction, (2) Watch coin flip animation, (3) Place sticker under matching result. **After 6 flips:** Count stickers in each column. Answer: "How many heads? How many tails? Were your guesses mostly right or mostly wrong?" **Success criteria:** Complete 6 flips with predictions and counts recorded correctly. _Implementation note: Animated coin flip with sticker placement. Auto-graded by correct recording._

Dependencies:
* T27.G1.00: Connect prediction to outcome using picture matching




ID: T27.G1.02
Topic: T27 – Chance & Simulations
Skill: Compare spinners with different numbers of sections
Description: **Student task:** Spin two different spinners (2-section and 4-section) and compare how often each color appears. **Visual scenario:** Spinner A has 2 equal sections (red, blue). Spinner B has 4 equal sections (red, blue, green, yellow). **Procedure:** Spin each spinner 8 times, recording with tally marks on a picture chart. **Comparison questions:** (1) "Which spinner gives more color choices?" (B—4 colors), (2) "On Spinner A, how many times out of 8 did you get red?" (typically 3-5), (3) "On Spinner B, how many times out of 8 did you get red?" (typically 1-3). **Key insight:** Red appears more often on the 2-section spinner because it has fewer choices. **Success criteria:** Complete tallies and answer comparison questions correctly. _Implementation note: Two animated spinners with tally recording interface._

Dependencies:
* T27.G1.01: Predict coin flips and record outcomes with stickers




ID: T27.G1.03
Topic: T27 – Chance & Simulations
Skill: Sort picture cards by likelihood (more likely, less likely)
Description: **Student task:** Sort 6 illustrated scenario cards into "more likely" and "less likely" piles by comparing chances. **Visual scenarios:** (A) Picking a red marble from bag with 5 red, 1 blue → "more likely red", (B) Picking blue from same bag → "less likely," (C) Rolling 1-5 on a die vs rolling exactly 6, (D) Drawing a heart from 10 hearts + 2 stars, (E) Spinner landing on big section vs small section. **Reasoning required:** Student must explain using counts: "Red is more likely because there are MORE red marbles than blue." **Success criteria:** Correctly sort 5+ cards with valid reasoning for at least 2. _Implementation note: Drag-drop sorting with picture cards showing item counts. Reasoning captured via simple tap-to-select explanation options._

Dependencies:
* T27.G1.02: Compare spinners with different numbers of sections




ID: T27.G1.04
Topic: T27 – Chance & Simulations
Skill: Order events from impossible to certain on a picture line
Description: **Student task:** Place 5 event picture cards on a line from "Impossible" to "Certain." **Visual scenario:** Line has markers: Impossible (0) - Maybe (middle) - Certain (1). Event cards: (A) Sun rising tomorrow (certain), (B) Rolling a 7 on a regular die (impossible), (C) Picking a red from 3 red + 3 blue (middle-maybe), (D) Dropping a ball and it falls (certain), (E) Getting heads on a coin (middle-maybe). **Procedure:** Drag each card to its position on the line. **Discussion prompt:** "Which events go in the middle? Why can't we be SURE about them?" **Key concept:** Events have different levels of certainty—some always happen, some never, some might. **Success criteria:** Place all 5 cards in approximately correct positions. _Implementation note: Drag-to-line interface with feedback on placement._

Dependencies:
* T27.G1.03: Sort picture cards by likelihood (more likely, less likely)




ID: T27.G2.00
Topic: T27 – Chance & Simulations
Skill: Compare two random tools and count their possibilities
Description: **Student task:** Look at two random tools side by side and decide which has MORE possible outcomes. **Visual scenario:** Comparison pairs: (1) Coin (2 sides) vs die (6 sides)—which has more possibilities? (Die—6 vs 2), (2) 3-color spinner vs 5-color spinner—which has more? (5-color), (3) Bag with 2 colors vs bag with 4 colors—which? (4-color bag). **Procedure:** Count outcomes for each tool, circle the one with more. **Key concept:** More possibilities means each single outcome is less likely to happen—harder to predict! **Discussion prompt:** "If you're trying to land on blue, would you rather have a 2-color or 10-color spinner?" (2-color—better chance!). **Success criteria:** Correctly compare 3 pairs and explain why more possibilities means harder to predict. _Implementation note: Side-by-side comparison with counting interface._

Dependencies:
* T27.G1.04: Order events from impossible to certain on a picture line




ID: T27.G2.01
Topic: T27 – Chance & Simulations
Skill: Classify events as certain, possible, or impossible
Description: **Student task:** Sort 9 illustrated picture cards into three labeled bins: "Certain" (always happens), "Possible" (might happen), and "Impossible" (cannot happen). **Visual scenarios:** Certain events: (A) sun rising tomorrow, (B) dropped rock falling down, (C) January coming after December. Possible events: (D) rolling a 3 on a die, (E) picking a red marble from bag with red and blue, (F) coin landing heads. Impossible events: (G) rolling 7 on a standard die, (H) drawing blue from bag with only red marbles, (I) person jumping to the moon. **Success criteria:** Sort all 9 cards correctly. **Extension question:** "Can you think of another possible event?" _Implementation note: Three-bin sorting with visual feedback showing why each answer is correct._

Dependencies:
* T27.G2.00: Compare two random tools and count their possibilities





ID: T27.G2.02
Topic: T27 – Chance & Simulations
Skill: Run a chance experiment and tally results
Description: **Student task:** Conduct a 10-trial experiment with a spinner or bag draw, recording each result with tally marks. **Procedure:** (1) Choose tool: 4-color spinner OR bag with 3 red, 2 blue blocks, (2) Run 10 trials, (3) After each trial, add tally mark to correct column, (4) After all trials, count totals. **Recording sheet:** Picture columns for each possible outcome (colors). **Analysis questions:** "Which color appeared most often? How many times? Did any color appear exactly 0 times?" **Key insight:** Results vary—running the same experiment again might give different counts. **Success criteria:** Complete 10 trials with accurate tally recording and correct final counts. _Implementation note: Animated spinner/bag draw with tally interface. Auto-graded by matching tallies to recorded outcomes._

Dependencies:
* T27.G2.01: Classify events as certain, possible, or impossible
* T24.G1.01: Record data with tally marks





ID: T27.G2.03
Topic: T27 – Chance & Simulations
Skill: Compare spinners and decide which game is fair
Description: **Student task:** Examine two spinners and determine which would make a fair game. **Visual scenario:** Spinner A has 4 equal-sized sections (red, blue, green, yellow—each takes 1/4). Spinner B has uneven sections (red takes half the circle, blue/green/yellow split the other half). **Game rules:** Each of 4 players picks a color; whoever's color is spun wins. **Analysis questions:** (1) "On Spinner A, does each color have the same chance?" (Yes—equal slices), (2) "On Spinner B, which color has the best chance?" (Red—biggest slice), (3) "Which spinner is fairer for this game?" (Spinner A). **Key concept:** Fair = equal chances for everyone. **Success criteria:** Correctly identify fair spinner and explain why using slice sizes. _Implementation note: Side-by-side spinner comparison with tap-to-select answers._

Dependencies:
* T27.G2.02: Run a chance experiment and tally results





ID: T27.G2.04
Topic: T27 – Chance & Simulations
Skill: Test whether predictions can beat random chance
Description: **Student task:** Make predictions before 10 coin flips and track whether guessing helps. **Procedure:** (1) Before each flip, tap your prediction (heads or tails), (2) Watch the flip, (3) Record if prediction was correct (✓) or wrong (✗). **After 10 flips:** Count correct predictions. **Analysis questions:** (1) "How many did you get right out of 10?" (2) "Is that more than 5, less than 5, or about 5?" (3) "If you guess randomly, you'd expect about 5 right. Did your careful guessing do much better?" **Key insight:** Even careful predictions can't reliably beat random chance—each flip is independent. **Success criteria:** Complete 10 predictions with accurate tracking and answer analysis questions. _Implementation note: Animated coin with prediction tracking and comparison to expected 50% success rate._

Dependencies:
* T27.G2.02: Run a chance experiment and tally results





ID: T27.G2.05
Topic: T27 – Chance & Simulations
Skill: Watch a CreatiCode spinner simulation and compare to physical results
Description: **Student task:** Watch a pre-built CreatiCode spinner simulation run 20 times and compare digital results to physical spinner experience. **Procedure:** (1) Run the provided project (click green flag), (2) Watch 20 automated spins with results displayed on screen, (3) Record final counts for each color. **Comparison questions:** Think back to your physical spinner from G2.02—did you see similar variation? The computer spinner follows the same rules as a physical spinner, but runs much faster! **Analysis:** (1) "Did all colors appear the same number of times?" (No—randomness causes variation), (2) "Would you get the exact same counts if you ran it again?" (No—each run is different). **Bridge concept:** This introduces CreatiCode as a tool for running chance experiments faster than by hand. **Success criteria:** Record counts accurately and answer both questions correctly. _Implementation note: Pre-built project students observe (not edit). Shows spinning animation with live count update._

Dependencies:
* T27.G2.04: Test whether predictions can beat random chance
* T27.G2.02: Run a chance experiment and tally results




ID: T27.G2.06
Topic: T27 – Chance & Simulations
Skill: Identify unfair spinners by comparing section sizes in pictures
Description: **Student task:** Look at 4 spinner pictures and identify which ones are "fair" vs "unfair." **Visual scenario:** (A) 4 equal sections—FAIR, (B) One section takes half the circle—UNFAIR (that color has better chance), (C) 3 equal sections—FAIR, (D) 6 sections but one is twice as big—UNFAIR. **Questions for each:** "Would you want to play a game where everyone picks a color on this spinner? Why or why not?" **Key concept:** Fair means everyone has the SAME chance. If sections are different sizes, chances are different! **Discussion prompt:** "If you could pick any color on spinner B, which would you pick? Why?" (The big one—it has a better chance). **Success criteria:** Correctly classify 4 of 4 spinners as fair or unfair with reasoning. _Implementation note: Spinner pictures with interactive fair/unfair toggle and reasoning selection._

Dependencies:
* T27.G2.03: Compare spinners and decide which game is fair




ID: T27.G3.01
Topic: T27 – Chance & Simulations
Skill: Interpret bar chart results from a spinner simulation
Description: **Student task:** Run a pre-built CreatiCode spinner simulation and interpret the bar chart results. **Procedure:** (1) Click green flag to run simulation (spinner spins 20 times automatically), (2) Observe the bar chart updating as results come in, (3) After all spins, analyze the final chart. **Analysis questions:** (1) "Which color appeared most often? How many times?" (2) "Which color appeared least often?" (3) "Did all colors appear exactly 5 times each (20 spins ÷ 4 colors)?" (Probably not—randomness!). **Written response:** Write 2-3 sentences explaining: "Even though each color has an equal chance, the results weren't exactly equal because..." **Key concept:** Variability in random experiments is normal. **Success criteria:** Correctly identify most/least frequent colors and explain variability. _Implementation note: Pre-built project with automated bar chart generation._

Dependencies:
* T27.G2.05: Watch a CreatiCode spinner simulation and compare to physical results
* T26.G2.01: Read a picture graph (pictograph)





ID: T27.G3.02
Topic: T27 – Chance & Simulations
Skill: Explore the "pick random" block and predict its boundaries
Description: **Student task:** Drag the 'pick random 1 to 6' block into a 'say' block and test what values it can produce. **Exploration procedure:** (1) Click the block 10+ times and observe different numbers appearing, (2) Record the smallest and largest numbers you see. **Prediction tests:** Can this block show: (A) 0? (No—below range), (B) 7? (No—above range), (C) 3.5? (No—whole numbers only), (D) 6? (Yes—at upper boundary). Test each prediction by clicking many times. **Written summary:** "The pick random block picks a whole number from __ to __, where each number has an equal chance of being picked." **Success criteria:** Correctly predict all 4 boundary tests and write accurate summary. _Implementation note: Interactive block testing with prediction checkboxes._

Dependencies:
* T27.G3.01: Interpret bar chart results from a spinner simulation





ID: T27.G3.03
Topic: T27 – Chance & Simulations
Skill: Run a simulation loop and record results in a table
Description: **Student task:** Run a provided simulation that generates 10 random 0s and 1s, then record results in a table. **Code provided:** 'when green flag clicked → repeat 10 [set result to pick random 0 to 1, say result for 0.5 secs]'. **Procedure:** (1) Click green flag, (2) Watch each result appear, (3) Record each value (0 or 1) in your table as it appears. **After 10 trials:** Count totals—"How many 0s? How many 1s?" **Analysis question:** "If 0 and 1 have equal chances, would you expect exactly 5 of each? Did you get exactly 5?" **Key concept:** This is your first experience with code that automatically generates random data—much faster than flipping coins! **Success criteria:** Accurate recording of all 10 results and correct totals. _Implementation note: Pre-built project with step-by-step recording interface._

Dependencies:
* T27.G3.02: Explore the "pick random" block and predict its boundaries
* T07.G3.01: Use a counted repeat loop





ID: T27.G3.04
Topic: T27 – Chance & Simulations
Skill: Predict simulation outcomes and measure prediction error
Description: **Student task:** Make predictions before running a 20-trial simulation, then compare predictions to actual results. **Procedure:** (1) Before running: Write predictions—"I think red will appear ___ times, blue will appear ___ times" (out of 20 trials on a 50/50 spinner), (2) Run the simulation, (3) Record actual counts, (4) Calculate difference: |prediction - actual| for each color. **Analysis questions:** (1) "Was your prediction within 3 of the actual count?" (2) "Why is it hard to predict the exact number?" (Because randomness causes variation). **Key insight:** Even though we expect 10 red and 10 blue on average, any single run might be 12-8 or 9-11 or even 15-5. **Success criteria:** Complete predictions, run simulation, calculate errors correctly, and explain why exact prediction is difficult. _Implementation note: Prediction entry before simulation unlocks, error calculation automatic._

Dependencies:
* T27.G3.03: Run a simulation loop and record results in a table





ID: T27.G3.05
Topic: T27 – Chance & Simulations
Skill: Classify games by their random elements (dice, spinner, cards)
Description: **Student task:** Analyze 4 familiar games and identify what random element makes each game "lucky." **Games to analyze:** (A) Chutes and Ladders—uses a spinner, (B) Candy Land—draws from shuffled cards, (C) Sorry!—draws from shuffled cards + dice for movement, (D) Go Fish—shuffled cards dealt randomly. **Classification table:** For each game, fill in: (1) Random element type (dice/spinner/cards), (2) "Mostly luck" or "Luck + some skill." **Analysis question:** "Chess has no dice, spinner, or card shuffling. Is chess a luck game or skill game? Why?" (Skill—no random elements). **Key concept:** Random elements (dice, spinners, shuffled cards) create uncertainty that makes games unpredictable. **Success criteria:** Correctly identify random element for 3+ games and explain chess classification. _Implementation note: Game cards with checkboxes for random element types._

Dependencies:
* T27.G3.04: Predict simulation outcomes and measure prediction error





ID: T27.G3.06
Topic: T27 – Chance & Simulations
Skill: Modify a random generator to change its possible outcomes
Description: **Student task:** Modify a starter project to change what outcomes are possible. **Starter code:** 'if pick random 1 to 2 = 1 then say "red" else say "blue"'. **Modification choices (pick one):** (A) Change colors to "cat" and "dog", (B) Expand to 3 outcomes by changing range to 1-3 and adding 'else if = 2 then say "green"', (C) Change to show numbers "1" and "2" instead of colors. **Testing:** Click green flag 15+ times to verify: (1) All intended outcomes can appear, (2) No unintended outcomes appear. **Verification question:** "If you changed to 3 outcomes, did you see all 3 appear after 15 clicks?" **Success criteria:** Successfully modify code, test thoroughly, and confirm all outcomes are possible. _Implementation note: Starter project with side-by-side code comparison showing original and modified._

Dependencies:
* T27.G3.03: Run a simulation loop and record results in a table
* T08.G3.01: Use a simple if in a script





ID: T27.G3.07
Topic: T27 – Chance & Simulations
Skill: Build a random number generator from scratch
Description: **Student task:** Create your own random generator starting from an empty project. **Build steps:** (1) Add 'when green flag clicked' event, (2) Create a variable named 'result' using Make a Variable, (3) Add 'set result to pick random 1 to 3', (4) Add 'say result'. **Testing:** Click green flag 15+ times. Tally how often each number (1, 2, 3) appears. **Analysis questions:** (1) "Did each number appear at least once?" (Should yes after 15 tries), (2) "Did they appear exactly 5 times each?" (Probably not—that's randomness!). **Achievement:** This is your first fully self-built simulation—you created a digital die from scratch! **Extension challenge:** Change it to pick random 1 to 6 to simulate a real die. **Success criteria:** Working generator that produces values 1-3, tested 15+ times with recorded tallies. _Implementation note: Empty project with step-by-step guidance and tally recording._

Dependencies:
* T27.G3.06: Modify a random generator to change its possible outcomes
* T09.G3.01.01: Create a variable using the Make a Variable button
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence





ID: T27.G3.08
Topic: T27 – Chance & Simulations
Skill: Shuffle a list randomly and observe the results
Description: **Student task:** Use CreatiCode's 'reshuffle list randomly' block to explore randomized ordering. **Build steps:** (1) Create a list with 5 items: [A, B, C, D, E], (2) Display the list, (3) Add 'reshuffle [mylist] randomly' block, (4) Display the list again. **Observation:** Run 5 times and write down each shuffled order. **Analysis questions:** (1) "Did you ever get the same order twice?" (Unlikely!), (2) "Did every letter appear in every position at least once across your 5 runs?" (Check!), (3) "Why is shuffling useful in games?" (For card dealing, random turn order, surprise elements). **Real-world connections:** Card shuffling, randomized quiz questions, music shuffle. **Key concept:** Shuffling rearranges items randomly—each possible order has equal chance. **Success criteria:** Successfully shuffle list multiple times, record different orderings. _Implementation note: Use data_reshuffle block._

Dependencies:
* T27.G3.07: Build a random number generator from scratch
* T10.G3.02: Add an item to a list




ID: T27.G3.09
Topic: T27 – Chance & Simulations
Skill: Debug a simulation that counts wrong number of outcomes
Description: **Student task:** Find and fix the bug in a simulation that doesn't count all outcomes correctly. **Buggy code provided:** A die roll counter that should count values 1-6, but only shows counts for 1-5. **Bug hunt steps:** (1) Run simulation 50 times, observe counts displayed, (2) Notice "6" count is always 0, (3) Inspect code—find 'if roll = 6' is missing from the counting logic, (4) Add the missing condition. **Debugging scaffolds:** (A) "How many different values can a die show?" (6), (B) "How many counters do you see in the code?" (5—one is missing!), (C) "Which value has no counter?" (6). **Verification:** Run again—now all 6 values have counts, total should equal 50. **Key concept:** Every possible outcome needs to be accounted for in simulation counting. **Success criteria:** Identify missing counter, fix code, verify total equals trial count. _Implementation note: Pre-built buggy project with guided hints._

Dependencies:
* T27.G3.07: Build a random number generator from scratch
* T12.G3.01: Identify a bug when output differs from expectation




ID: T27.G4.01
Topic: T27 – Chance & Simulations
Skill: Map random numbers to named outcomes using if-statements
Description: **Student task:** Extend a random generator to show meaningful words instead of raw numbers. **Build steps:** (1) Set 'roll' to pick random 1 to 4, (2) Add if-statements to convert: 'if roll = 1 then say "red"', 'else if roll = 2 then say "blue"', 'else if roll = 3 then say "green"', 'else say "yellow"'. **Testing:** Click green flag 20+ times. **Verification checklist:** □ Red appeared at least once, □ Blue appeared at least once, □ Green appeared at least once, □ Yellow appeared at least once. **Debugging scenario:** "What if you only see 3 colors after 20 tries? Is the code broken?" (Not necessarily—rare outcomes might need more tries. Try 50 times.) **Key concept:** Random numbers can drive meaningful outcomes—the number 1 BECOMES "red." **Success criteria:** All 4 colors appear within 25 tries, if-statement structure is correct. _Implementation note: Verification checklist auto-checks as outcomes appear._

Dependencies:
* T27.G3.08: Shuffle a list randomly and observe the results
* T08.G3.01: Use a simple if in a script





ID: T27.G4.02.01
Topic: T27 – Chance & Simulations
Skill: Automate data collection by logging trial results to a list
Description: **Student task:** Extend your random generator to automatically collect 50 trials in a list. **Build steps:** (1) Create a list called 'results', (2) Add 'delete all of [results]' at start (to clear old data), (3) Wrap generator in 'repeat 50' loop, (4) Inside loop, add 'add (result) to [results]' after each random pick. **After running:** Check list length—'say (length of results)' should show 50. **Verification:** (1) List has exactly 50 items, (2) Items are only valid outcomes (red/blue/green/yellow), (3) Running again gives different results. **Key advantage:** This automates data collection—50 trials in seconds instead of minutes of manual tallying! **Success criteria:** List contains exactly 50 valid outcomes after one click. _Implementation note: List display shows items accumulating during run._

Dependencies:
* T27.G4.01: Map random numbers to named outcomes using if-statements
* T07.G3.01: Use a counted repeat loop
* T10.G3.02: Add an item to a list





ID: T27.G4.02.02
Topic: T27 – Chance & Simulations
Skill: Count frequencies of each outcome from collected data
Description: **Student task:** After collecting 50 trials, count how many times each outcome appeared. **Build steps:** (1) Create counter variables: redCount, blueCount, greenCount, yellowCount, (2) Set all counters to 0, (3) Loop through results list using 'for each item in [results]', (4) Inside loop: 'if item = "red" then change redCount by 1', repeat for each color. **Display:** Show all counts on stage using 'say' or variable monitors. **Verification:** Counts should add up to 50 (redCount + blueCount + greenCount + yellowCount = 50). **Analysis question:** "Are all counts close to 12-13 (which is 50÷4)? Which color appeared most? Which least?" **Success criteria:** All 4 counts calculated correctly, total equals 50. _Implementation note: Counter variables visible on stage with final summary display._

Dependencies:
* T27.G4.02.01: Automate data collection by logging trial results to a list
* T10.G3.05: Loop through each item in a list
* T09.G3.03: Use a variable in a simple conditional (if block)





ID: T27.G4.02.03
Topic: T27 – Chance & Simulations
Skill: Calculate percentages from frequency counts
Description: **Student task:** Convert frequency counts to percentages to compare outcomes fairly. **Formula:** percentage = (count / total trials) × 100. **Example:** If red appeared 12 times out of 50: (12/50)×100 = 24%. **Code:** Create 'redPercent' variable, set it to '(redCount / 50) * 100'. **Display:** Show all 4 percentages. **Analysis questions:** (1) "Does each color appear about 25% of the time?" (For fair 4-color spinner, expect ~25% each), (2) "If red is 40% and blue is 10%, what might that mean?" (Could be random variation, or code bug making outcomes unfair), (3) "What would 'perfect fairness' look like?" (Exactly 25% each—but that rarely happens!). **Success criteria:** Calculate all 4 percentages correctly, identify whether results suggest fairness. _Implementation note: Percentage calculator with comparison to expected 25%._

Dependencies:
* T27.G4.02.02: Count frequencies of each outcome from collected data





ID: T27.G4.03
Topic: T27 – Chance & Simulations
Skill: Compare variability at different sample sizes (50 vs 500 trials)
Description: **Student task:** Run the same simulation at two sample sizes and compare how much results vary from expected. **Procedure:** (1) Run with 50 trials, record all 4 percentages, (2) Run with 500 trials, record all 4 percentages. **Comparison table:** Create side-by-side comparison—50 trials vs 500 trials. **Expected observation:** With 50 trials, percentages might be 18%, 32%, 24%, 26% (spread from 25%). With 500 trials, closer to 24%, 26%, 25%, 25% (tighter around 25%). **Key concept:** "More trials = results closer to expected percentages." This is because random variation 'averages out' over many trials. **Analysis questions:** (1) "Which run had percentages closer to 25% each?" (500 trials), (2) "Why does more data give more stable results?" **Success criteria:** Complete both runs, accurately compare variability, explain the pattern. _Implementation note: Variable for trial count that student changes; side-by-side chart generation._

Dependencies:
* T27.G4.02.03: Calculate percentages from frequency counts
* T26.G3.04: Create side-by-side bar charts for two groups





ID: T27.G4.04
Topic: T27 – Chance & Simulations
Skill: Debug an unfair simulation by finding probability bugs
Description: **Student task:** Find and fix the bug in a simulation that produces unfair results. **Buggy project:** Run the provided simulation 100 times—notice red appears ~50% instead of 25%. **Bug hunt:** Inspect the code. **Common bugs to look for:** (A) 'if roll = 1 OR roll = 2 then "red"'—red gets 2 chances out of 4, (B) 'pick random 1 to 3' but 4 outcomes mapped—one color never appears, (C) Missing 'else if' causing fall-through. **Debugging process:** (1) Trace through code with sample values (roll=1, roll=2, etc.), (2) Count how many roll values lead to each color, (3) Find the mismatch. **Fix:** Modify code so each color gets exactly 1 chance. **Verification:** Run 100 trials—percentages should now be roughly 25% each. **Success criteria:** Identify the specific bug, fix it correctly, verify with test run. _Implementation note: Pre-built buggy project with debugging hints._

Dependencies:
* T27.G4.01: Map random numbers to named outcomes using if-statements
* T12.G3.01: Identify a bug when output differs from expectation




ID: T27.G4.04.01
Topic: T27 – Chance & Simulations
Skill: Trace probability flow through nested if-else chains
Description: **Student task:** Trace through a nested if-else chain and count how many random values lead to each outcome. **Code to trace:** 'roll = pick random 1 to 8; if roll < 3 then "A", else if roll < 6 then "B", else "C"'. **Tracing table:** Create table with columns: roll value (1-8), condition check, outcome. Fill in all 8 rows. **Analysis:** Count outcomes: A gets values 1,2 (2 chances = 25%), B gets 3,4,5 (3 chances = 37.5%), C gets 6,7,8 (3 chances = 37.5%). **Discussion:** "Is this fair for a 3-player game?" (No—A has less chance than B and C). **Key concept:** Tracing helps reveal hidden unfairness in probability logic. **Verification:** Run 100 trials and compare to traced predictions. **Success criteria:** Complete trace table correctly, calculate percentages, identify fairness issue. _Implementation note: Interactive tracing table with auto-check._

Dependencies:
* T27.G4.04: Debug an unfair simulation by finding probability bugs
* T27.G4.01: Map random numbers to named outcomes using if-statements




ID: T27.G4.04.02
Topic: T27 – Chance & Simulations
Skill: Fix off-by-one errors in random range boundaries
Description: **Student task:** Find and fix off-by-one errors that cause simulation bugs. **Bug scenario 1:** 'pick random 1 to 5' but code expects 0-5 (6 values)—5 is never reached for the 6th outcome. **Bug scenario 2:** 'if roll <= 2' when you meant 'if roll < 2'—changes probability from 1/6 to 2/6. **Bug scenario 3:** 'pick random 0 to 3' for 4 outcomes, but if-conditions use 1-4—outcome "0" never triggers any action. **Debugging process:** (1) List all possible random values, (2) Trace each through conditions, (3) Find values that don't trigger expected behavior. **Fix patterns:** (A) Adjust random range to match expected values, (B) Adjust condition comparisons, (C) Add missing case handling. **Success criteria:** Fix 3 off-by-one scenarios, explain why boundaries matter. _Implementation note: Three buggy code snippets with correction interface._

Dependencies:
* T27.G4.04.01: Trace probability flow through nested if-else chains
* T27.G3.09: Debug a simulation that counts wrong number of outcomes





ID: T27.G4.05
Topic: T27 – Chance & Simulations
Skill: Generate and visualize random coordinate pairs
Description: **Student task:** Create a script that generates random x,y coordinates and visualizes them as dots. **Build steps:** (1) 'repeat 50 times', (2) 'set x to pick random -200 to 200', (3) 'set y to pick random -150 to 150', (4) 'go to x: (x) y: (y)', (5) 'stamp'. **After running:** See 50 dots scattered across the stage. **Observation questions:** (1) "Do the points clump in one area or spread out?" (Spread out fairly evenly), (2) "Are there any big empty gaps?" (Usually not, but possible by chance), (3) "Run it again—do you get the same pattern?" (No—different random coordinates each time). **Key concept:** Random 2D coordinates fill space uniformly—this is the foundation for Monte Carlo simulations! **Success criteria:** Generate 50 visible dots that appear distributed across the stage. _Implementation note: Clear stage before stamping; use small dot costume._

Dependencies:
* T27.G4.02.01: Automate data collection by logging trial results to a list
* T03.G3.01: Navigate a sprite using coordinates





ID: T27.G4.06
Topic: T27 – Chance & Simulations
Skill: Convert between probability fractions, decimals, and percentages
Description: **Student task:** Practice converting probability expressions between different forms. **Conversion examples:** (A) Fair 6-sided die: "chance of rolling 3" = 1 out of 6 = 1/6 ≈ 0.167 ≈ 16.7%, (B) 4-color spinner: "chance of red" = 1 out of 4 = 1/4 = 0.25 = 25%, (C) Bag with 3 red, 2 blue: "chance of red" = 3 out of 5 = 3/5 = 0.6 = 60%. **Practice problems:** (1) "2 out of 5 chance of rain"—what percentage? (40%), (2) "75% chance of success"—what fraction? (3/4), (3) "0.1 probability"—what percentage? (10%). **Connection to simulation:** Compare theoretical values (calculated) to experimental results (from your simulation). If theory says 25% but you got 32%, is that surprising? **Success criteria:** Convert 5+ probability expressions correctly between forms. _Implementation note: Interactive conversion practice with immediate feedback._

Dependencies:
* T27.G4.02.03: Calculate percentages from frequency counts





ID: T27.G4.07
Topic: T27 – Chance & Simulations
Skill: Generate random selections without repetition (sampling without replacement)
Description: **Student task:** Create a simulation that picks items randomly without repeats—like dealing cards or choosing team captains. **Build steps:** (1) Create list of items: ["Alice", "Bob", "Carol", "David", "Eve"], (2) 'repeat 5 times', (3) 'set index to pick random 1 to length of [names]', (4) 'say item (index) of [names]' (display the pick), (5) 'delete item (index) from [names]' (remove so it can't be picked again). **Verification:** (1) Run it—each name should appear exactly once, (2) After all picks, list should be empty, (3) No name should repeat. **Real-world connections:** Card dealing, lottery drawings, random team assignment. **Key concept:** This is "sampling without replacement"—once picked, an item is gone. **Success criteria:** All 5 names picked exactly once, list empty at end, no repeats. _Implementation note: Visual list showing items being removed as picked._

Dependencies:
* T27.G4.02.01: Automate data collection by logging trial results to a list
* T10.G3.04: Delete an item from a list





ID: T27.G4.08
Topic: T27 – Chance & Simulations
Skill: Visualize probability using area models
Description: **Student task:** Create visual area models to represent and calculate probabilities. **Build steps:** (1) Draw a square on stage (200×200 pixels), (2) Divide it into sections proportional to probabilities, (3) Color each section differently. **Example 1:** Fair die—divide square into 6 equal vertical strips. Each has area = 1/6 of total. **Example 2:** Weighted spinner (50% red, 30% blue, 20% green)—divide square: red gets half (100×200), blue gets 30% (60×200), green gets 20% (40×200). **Connection to simulation:** Generate 100 random points in the square. Count how many land in each region. Does the count match the area proportion? **Analysis question:** "If red is 50% of the area, about how many of 100 random points should land in red?" (About 50). **Success criteria:** Create accurate area model for given probabilities, verify with random point sampling. _Implementation note: Drawing tools for rectangles with proportion calculations._

Dependencies:
* T27.G4.05: Generate and visualize random coordinate pairs
* T27.G4.06: Convert between probability fractions, decimals, and percentages




ID: T27.G5.01.01
Topic: T27 – Chance & Simulations
Skill: Simulate compound events (two dice) and collect sum data
Description: **Student task:** Simulate rolling two dice 200 times and record the sum of each roll. **Build steps:** (1) Create list 'sums', (2) 'repeat 200 times', (3) 'set die1 to pick random 1 to 6', (4) 'set die2 to pick random 1 to 6', (5) 'set sum to die1 + die2', (6) 'add sum to [sums]'. **Verification:** (1) List has exactly 200 items, (2) All values are between 2 and 12 (smallest: 1+1=2, largest: 6+6=12), (3) No 1s or 13s appear (impossible sums). **Key concept:** This is a compound event—two separate random events combine to create a new outcome. The possible sums (2-12) don't all have equal chances! **Preview question:** "Do you think 7 and 2 are equally likely? We'll find out in the next skill." **Success criteria:** Collect 200 valid sums (all between 2-12). _Implementation note: Dual die visualization showing each roll before adding to list._

Dependencies:
* T27.G4.02.01: Automate data collection by logging trial results to a list
* T27.G4.06: Convert between probability fractions, decimals, and percentages





ID: T27.G5.01.02
Topic: T27 – Chance & Simulations
Skill: Analyze compound event distributions and explain why 7 is most common
Description: **Student task:** Count frequencies for each sum (2-12) from your two-dice data and explain the pattern. **Analysis steps:** (1) Create counters for each sum (2 through 12), (2) Loop through sums list counting each, (3) Create bar chart showing frequency of each sum. **Key observation:** 7 appears most often! **Explanation:** Count the ways to make each sum: Sum 2 = 1 way (1+1), Sum 7 = 6 ways (1+6, 2+5, 3+4, 4+3, 5+2, 6+1), Sum 12 = 1 way (6+6). **Fill in table:** "How many ways to make sum 3?" (2 ways: 1+2, 2+1), "How many ways to make sum 6?" (5 ways). **Key concept:** Compound events aren't equally likely even when individual events are equal—more combinations = higher probability! **Success criteria:** Create accurate frequency chart, explain why 7 is most common using combination counting. _Implementation note: Interactive combination counter alongside bar chart._

Dependencies:
* T27.G5.01.01: Simulate compound events (two dice) and collect sum data
* T27.G4.02.02: Count frequencies of each outcome from collected data
* T26.G4.01: Create a bar chart from a data table





ID: T27.G5.02
Topic: T27 – Chance & Simulations
Skill: Simulate random assignment for A/B testing
Description: **Student task:** Simulate an A/B test by randomly assigning 100 participants to two groups. **Build steps:** (1) Create list 'groups', (2) 'repeat 100 times', (3) 'if pick random 1 to 2 = 1 then add "A" to [groups] else add "B"'. **After running:** Count how many A's and B's. **Expected results:** Roughly 50 each (but rarely exactly 50-50). **Analysis questions:** (1) "Why is random assignment important for experiments?" (Ensures groups are similar, no bias in who gets which treatment), (2) "If you got 60 A's and 40 B's, is the code broken?" (Probably not—that's within normal random variation for 100 trials). **Real-world connection:** Medical trials, website testing, psychology experiments all use random assignment. **Success criteria:** Create working random assignment, verify roughly equal groups, explain importance. _Implementation note: Visual split showing two groups filling up._

Dependencies:
* T27.G4.02.02: Count frequencies of each outcome from collected data
* T27.G4.04: Debug an unfair simulation by finding probability bugs





ID: T27.G5.03
Topic: T27 – Chance & Simulations
Skill: Use Monte Carlo sampling to estimate π
Description: **Student task:** Estimate the area of a circle (and π!) using random points. **Setup:** Square from -100 to 100 (side = 200), circle with radius 100 centered at origin. **Build steps:** (1) 'repeat 1000 times', (2) 'set x to pick random -100 to 100', (3) 'set y to pick random -100 to 100', (4) 'if (x*x + y*y) < 10000 then change hits by 1' (point inside circle), (5) 'change total by 1'. **Calculation:** Circle area / Square area = π×100² / 200² = π/4. So π ≈ 4 × (hits/total). **Expected result:** With 1000 points, estimate π ≈ 3.14 (±0.1 usually). **Visualization:** Color hits green (inside circle), misses red (outside). **Key concept:** Random sampling can solve geometry problems! This is called Monte Carlo simulation. **Success criteria:** Estimate π within 0.2 of 3.14159. _Implementation note: Visual circle with dots appearing, running estimate displayed._

Dependencies:
* T27.G4.05: Generate and visualize random coordinate pairs
* T27.G4.03: Compare variability at different sample sizes (50 vs 500 trials)
* T08.G4.01: Choose actions based on user input or sensor values




ID: T27.G5.03.01
Topic: T27 – Chance & Simulations
Skill: Explain the geometry behind Monte Carlo π estimation
Description: **Student task:** Draw and label the geometric setup for Monte Carlo π estimation before coding. **Drawing task:** On graph paper or digital canvas: (1) Draw a 200×200 square centered at origin, (2) Draw inscribed circle with radius 100, (3) Shade the circle area. **Calculation preview:** (A) Square area = 200 × 200 = 40000, (B) Circle area = π × 100² = 10000π, (C) Ratio = Circle/Square = π/4 ≈ 0.785. **Prediction:** "If I drop 1000 random points in the square, about how many will land inside the circle?" (About 785—that's π/4 × 1000). **Key insight:** The ratio of hits to total points estimates π/4. Multiply by 4 to get π! **Connection:** This uses area ratios to estimate an irrational number—math meets simulation. **Success criteria:** Correct diagram, calculate areas, predict hit count within 50. _Implementation note: Interactive diagram builder with area calculator._

Dependencies:
* T27.G5.03: Use Monte Carlo sampling to estimate π




ID: T27.G5.03.02
Topic: T27 – Chance & Simulations
Skill: Visualize convergence of Monte Carlo π estimate with increasing samples
Description: **Student task:** Run π estimation at different sample sizes and graph how the estimate converges. **Experiment:** Run with n = 100, 500, 1000, 5000, 10000 points. For each, record estimate. **Visualization:** Plot sample size (x-axis) vs estimate (y-axis). Draw horizontal line at π = 3.14159. **Expected pattern:** Estimates jump around more at low n, stabilize closer to 3.14159 at high n. **Quantitative analysis:** Calculate |estimate - 3.14159| for each n. Does error decrease with more samples? (Yes!) **Discussion:** "If you needed π accurate to 2 decimal places (3.14), how many points might you need?" (Usually 1000+ works). **Key concept:** Monte Carlo accuracy improves with sample size—this is the law of large numbers applied to geometry! **Success criteria:** Complete 5 runs, create convergence plot, explain accuracy vs sample size relationship. _Implementation note: Auto-plotting of estimate vs sample size._

Dependencies:
* T27.G5.03.01: Explain the geometry behind Monte Carlo π estimation
* T27.G5.11: Demonstrate the law of large numbers through simulation





ID: T27.G5.04
Topic: T27 – Chance & Simulations
Skill: Write a 5-part simulation plan before coding
Description: **Student task:** Before building any simulation, create a written plan with 5 required parts. **Plan template:** (1) **Question:** What am I trying to find out? (e.g., "How often does rolling two dice give a sum of 7?"), (2) **Random model:** What will be random? (die roll, coin flip, coordinates, card draw?), (3) **Variables:** What will I track? (counters, lists, totals, positions?), (4) **Trials:** How many times will I run it? (justify: 100 for quick test, 1000 for accuracy), (5) **Success metric:** How will I know it worked? (expected percentage, comparison to theory, visual pattern). **Practice problem:** Write a plan for: "Estimate the probability of getting at least one 6 when rolling 4 dice." **Key benefit:** Planning prevents "just start coding" and builds design thinking—real engineers always plan first! **Success criteria:** Complete all 5 plan sections with logical, specific content. _Implementation note: Plan template with required fields before coding environment unlocks._

Dependencies:
* T27.G4.03: Compare variability at different sample sizes (50 vs 500 trials)
* T27.G4.04: Debug an unfair simulation by finding probability bugs
* T05.G4.01: Describe what a simulation should do before building





ID: T27.G5.05
Topic: T27 – Chance & Simulations
Skill: Calculate theoretical probability using the formula P = favorable/total
Description: **Student task:** Calculate probability using the formula: P(event) = favorable outcomes / total outcomes. **Examples:** (A) P(rolling a 3 on die) = 1/6 ≈ 0.167 ≈ 16.7%, (B) P(heads on coin) = 1/2 = 0.5 = 50%, (C) P(red from bag with 3 red, 2 blue) = 3/5 = 0.6 = 60%. **Practice problems:** (1) Bag with 4 red, 3 blue, 2 green marbles. P(blue) = ? (3/9 = 1/3 ≈ 33%), (2) Standard deck of 52 cards. P(ace) = ? (4/52 = 1/13 ≈ 7.7%), (3) Spinner with 5 equal sections. P(landing on any specific section) = ? (1/5 = 20%). **Key concept:** This is "theoretical" probability—calculated from logic, not experiments. It tells us what SHOULD happen in the long run. **Success criteria:** Calculate 5+ theoretical probabilities correctly and convert between fraction/decimal/percentage. _Implementation note: Interactive formula calculator with conversion tools._

Dependencies:
* T27.G4.06: Convert between probability fractions, decimals, and percentages





ID: T27.G5.06
Topic: T27 – Chance & Simulations
Skill: Compare experimental probability to theoretical probability
Description: **Student task:** Calculate theoretical probability, run a simulation, then compare. **Procedure:** (1) Calculate: P(heads) = 1/2 = 50% (theoretical), (2) Run simulation: flip coin 100 times, count heads, (3) Calculate experimental: (heads count / 100) × 100%. **Example result:** Theory = 50%, Experiment = 47 heads = 47%. **Analysis questions:** (1) "Why are they different?" (Random variation—each run is different), (2) "Will they ever match exactly?" (Rarely—randomness almost always causes some difference), (3) "What happens with more trials?" (Experimental gets closer to theoretical). **Try it:** Run with 100 trials, then 1000 trials. Which is closer to 50%? **Key concept:** Experimental probability is what we OBSERVE; theoretical is what we EXPECT. They converge with more data! **Success criteria:** Correctly compare experimental vs theoretical for 2+ scenarios. _Implementation note: Side-by-side comparison with adjustable trial count._

Dependencies:
* T27.G5.05: Calculate theoretical probability using the formula P = favorable/total
* T27.G4.03: Compare variability at different sample sizes (50 vs 500 trials)





ID: T27.G5.07
Topic: T27 – Chance & Simulations
Skill: Create and analyze frequency distributions from simulation data
Description: **Student task:** Organize simulation results into a frequency table and histogram, then analyze the distribution. **Procedure:** (1) Run 100 die rolls, (2) Create frequency table: Value | Count (1|___, 2|___, ... 6|___), (3) Create histogram/bar chart from table. **Analysis questions:** (1) "What is the mode (most common value)?" (2) "What is the range?" (1 to 6), (3) "Is the distribution 'flat' (uniform) or 'peaked'?" (Should be roughly flat for fair die). **Comparison:** For a fair die, expect each value ~16-17 times out of 100. Is your distribution close? **Shape vocabulary:** Uniform = all bars roughly equal, Peaked = one value much higher, Skewed = bars slope in one direction. **Success criteria:** Create accurate frequency table and histogram, correctly identify mode and distribution shape. _Implementation note: Interactive histogram builder with distribution shape identifier._

Dependencies:
* T27.G5.01.02: Analyze compound event distributions and explain why 7 is most common
* T26.G4.02: Create a histogram from continuous data





ID: T27.G5.07.01
Topic: T27 – Chance & Simulations
Skill: Generate batch random data using the set-random-list block
Description: **Student task:** Use CreatiCode's 'set list to N random numbers' block to efficiently generate large datasets. **Build steps:** (1) 'set [rolls] to (100) random whole numbers between (1) and (6) [allow repetition]', (2) Display the list to verify 100 values, (3) Count each outcome (1-6) from the list. **Comparison:** This single block replaces a 100-iteration loop with pick random inside! **Efficiency test:** Time how long it takes to generate 1000 values with a loop vs with this block. **Analysis:** Generate 1000 die rolls, count frequencies, compare to expected ~167 each. **Extension:** Try 'no repetition' mode—what happens if you try to generate 10 unique numbers between 1 and 6? (Works—gives all 6 in random order. What about 100 unique numbers between 1 and 6? Error—impossible!). **Success criteria:** Generate batch data, understand repetition modes, count frequencies correctly. _Implementation note: Use data_setrandomlist block._

Dependencies:
* T27.G5.07: Create and analyze frequency distributions from simulation data
* T27.G4.02.01: Automate data collection by logging trial results to a list




ID: T27.G5.08
Topic: T27 – Chance & Simulations
Skill: Build a random walker agent with state tracking
Description: **Student task:** Create a "random walker" sprite that moves based on random choices and tracks its state. **Agent state variables:** (1) x, y position, (2) direction (0=up, 90=right, 180=down, 270=left), (3) energy (starts at 50, decreases each step). **Movement logic:** Each step: (A) Set direction to pick random from [0, 90, 180, 270], (B) Move 10 pixels in that direction, (C) Change energy by -1, (D) If energy = 0, stop. **Visualization:** Leave a trail (use pen or stamp) to see the random path. **Observation questions:** (1) "Does the walker end up near where it started or far away?" (Varies—that's randomness!), (2) "Run it 5 times—do you get the same path?" (No—each run is different). **Key concept:** This is an "agent-based" simulation—the agent has state and makes probabilistic decisions. **Success criteria:** Walker completes 50 steps, trail is visible, energy depletes correctly. _Implementation note: Pen trail with energy counter display._

Dependencies:
* T27.G4.05: Generate and visualize random coordinate pairs
* T09.G4.04: Use variables to control animation or game state
* T03.G3.01: Navigate a sprite using coordinates





ID: T27.G5.09
Topic: T27 – Chance & Simulations
Skill: Calculate and verify expected value through simulation
Description: **Student task:** Calculate expected value (long-run average) and verify with simulation. **Formula:** E = Σ(outcome × probability). **Example 1:** Fair die: E = (1×1/6) + (2×1/6) + (3×1/6) + (4×1/6) + (5×1/6) + (6×1/6) = 3.5. **Example 2:** Game: 50% chance win $10, 50% chance win $0. E = (10×0.5) + (0×0.5) = $5. **Example 3:** Weighted game: 10% chance win $100, 90% chance lose $5. E = (100×0.1) + (-5×0.9) = 10 - 4.5 = $5.50. **Verification:** Run 1000 simulations, calculate average outcome. Compare to calculated E. **Key insight:** Expected value tells you what to expect ON AVERAGE over many trials—not what happens in any single trial. **Success criteria:** Calculate E for 3 scenarios, verify one with simulation (average within 10% of E). _Implementation note: Calculator for E with simulation verification tool._

Dependencies:
* T27.G5.05: Calculate theoretical probability using the formula P = favorable/total
* T27.G5.06: Compare experimental probability to theoretical probability





ID: T27.G5.10
Topic: T27 – Chance & Simulations
Skill: Identify independent events and debunk the gambler's fallacy
Description: **Student task:** Explore whether past results affect future outcomes in random events. **Simulation experiment:** (1) Run coin flip simulation that tracks streaks, (2) After getting 5 heads in a row, predict: Is tails now more likely? (3) Continue flipping 100 more times after a streak of 5 heads, (4) Count: What fraction were tails? **Key discovery:** Still ~50%! Each flip is INDEPENDENT—the coin has no memory of past flips. **Gambler's fallacy examples:** (A) "Red has come up 10 times at roulette, so black is due!" (WRONG), (B) "I've lost 5 games, so I'm due for a win!" (WRONG for random games), (C) "This lottery number hasn't won in years, it's overdue!" (WRONG). **Analysis question:** "If events ARE independent, why do we still see streaks?" (Streaks happen by chance—5 heads in a row occurs 1/32 ≈ 3% of the time). **Success criteria:** Demonstrate independence through simulation, identify 3+ gambler's fallacy scenarios. _Implementation note: Streak tracker with "after streak" analysis._

Dependencies:
* T27.G5.06: Compare experimental probability to theoretical probability





ID: T27.G5.11
Topic: T27 – Chance & Simulations
Skill: Demonstrate the law of large numbers through simulation
Description: **Student task:** Run simulations at increasing sample sizes and observe convergence to theoretical probability. **Experiment:** Run coin flip simulations with n = 10, 100, 1000, 10000 trials. Record % heads for each. **Expected pattern:** n=10: might get 30-70% (high variability), n=100: usually 40-60%, n=1000: usually 47-53%, n=10000: usually 49-51% (very close to 50%). **Visualization:** Plot percentage vs trial count on line graph. The line should stabilize around 50% as n increases. **The Law of Large Numbers:** As the number of trials increases, experimental probability approaches theoretical probability. **Discussion:** "Does this mean that after many heads, tails becomes more likely?" (NO! That's the gambler's fallacy. The law says the AVERAGE stabilizes, not that results 'even out'). **Success criteria:** Complete 4 runs at different n values, create convergence graph, explain the law correctly. _Implementation note: Running percentage display that updates during simulation._

Dependencies:
* T27.G5.06: Compare experimental probability to theoretical probability
* T27.G4.03: Compare variability at different sample sizes (50 vs 500 trials)
* T26.G4.03: Create a line graph showing change over time




ID: T27.G5.12
Topic: T27 – Chance & Simulations
Skill: Validate simulation correctness using expected value comparison
Description: **Student task:** Create a validation test to check if your simulation is working correctly. **Validation method:** (1) Calculate theoretical expected value (e.g., fair die: E = 3.5), (2) Run simulation 1000+ times, (3) Calculate average result, (4) Compare to theoretical—should be within reasonable tolerance. **Example validation:** Die roll simulation: Theory E = 3.5. If your average is 2.1, something is wrong! Debug until average is 3.4-3.6. **Tolerance rule of thumb:** With 1000 trials, average should be within ±5% of expected. With 10000 trials, within ±2%. **Common bugs this catches:** (A) Random range wrong (1-5 instead of 1-6), (B) One outcome weighted incorrectly, (C) Counting logic error. **Key concept:** Expected value comparison is a powerful validation tool—if your simulation produces wrong averages, the probabilities are wrong! **Success criteria:** Validate 2 simulations using expected value, catch and fix one intentional bug. _Implementation note: Pre-built validation checker comparing simulation mean to theoretical._

Dependencies:
* T27.G5.09: Calculate and verify expected value through simulation
* T27.G5.11: Demonstrate the law of large numbers through simulation





ID: T27.G6.01.01
Topic: T27 – Chance & Simulations
Skill: Manually test simulation parameters and log results systematically
Description: **Student task:** Test how changing a parameter affects simulation outcomes by running controlled experiments. **Example scenario:** Catch-the-falling-object game with adjustable ball speed. **Procedure:** (1) Set speed = 1, play 10 times, record wins/losses, (2) Repeat for speed = 2, 3, 4, 5. **Results table:** Speed 1 → 10/10 wins (too easy), Speed 3 → 7/10 wins (challenging), Speed 5 → 2/10 wins (too hard). **Analysis:** Identify the "sweet spot"—the parameter value where the game is challenging but fair (around 60-70% win rate). **Key concept:** Systematic parameter testing helps optimize simulations. This is how game designers balance difficulty! **Documentation:** Record hypothesis before testing, actual results, and conclusion. **Success criteria:** Test 5 parameter values, create organized results table, identify optimal range. _Implementation note: Game with adjustable parameter and results logging._

Dependencies:
* T27.G5.04: Write a 5-part simulation plan before coding
* T27.G5.06: Compare experimental probability to theoretical probability





ID: T27.G6.01.02
Topic: T27 – Chance & Simulations
Skill: Automate parameter sweeps with nested loops
Description: **Student task:** Automate the parameter testing from G6.01.01 using nested loops. **Code structure:** Outer loop: 'for speed from 1 to 5', Inner loop: 'repeat 20 times [run trial, track win/loss]'. After inner loop: log [speed, totalWins]. **Expected output:** Table like [[1, 20], [2, 18], [3, 15], [4, 10], [5, 4]]—showing wins out of 20 for each speed. **Advantages over manual testing:** (1) Faster—tests all parameters in seconds, (2) More trials—can easily run 100 instead of 10, (3) Reproducible—same code gives comparable results. **Visualization:** Create bar chart showing win rate vs parameter value. **Extension:** Test 2 parameters (speed AND size) with triple-nested loops. **Success criteria:** Automated sweep produces results table for 5+ parameter values, each with 20+ trials. _Implementation note: Progress indicator showing current parameter and trial._

Dependencies:
* T27.G6.01.01: Manually test simulation parameters and log results systematically
* T07.G5.01: Use nested loops for grid or matrix operations





ID: T27.G6.02
Topic: T27 – Chance & Simulations
Skill: Use random seeds for reproducible simulations
Description: **Student task:** Use CreatiCode's seeded random block to create reproducible simulations. **Code:** 'set [randomList] to (100) random numbers with seed (42)'. Use values from this list instead of 'pick random'. **Verification tests:** (1) Run with seed 42 twice → identical results both times, (2) Change to seed 43 → different results but still reproducible with seed 43. **Why this matters:** (A) Debugging: "I got a weird result on trial 47—can you reproduce it?" (Yes, with same seed!), (B) Fairness: "Same puzzle/challenge for all players in competition", (C) Testing: "Run same scenario to compare different algorithms." **Real-world uses:** Video game speedrunning exploits seeds, scientific simulations require reproducibility, multiplayer games use shared seeds for fairness. **Success criteria:** Demonstrate identical results with same seed, different results with different seed. _Implementation note: Side-by-side output comparison for same vs different seeds._

Dependencies:
* T27.G5.04: Write a 5-part simulation plan before coding
* T27.G6.01.02: Automate parameter sweeps with nested loops





ID: T27.G6.03
Topic: T27 – Chance & Simulations
Skill: Calculate percent error to evaluate simulation accuracy
Description: **Student task:** Calculate percent error to quantify how close simulation results are to theoretical values. **Formula:** Percent Error = |experimental - theoretical| / theoretical × 100%. **Example:** Theory: P(heads) = 50%. Experiment: 47 heads out of 100 = 47%. Error = |47-50|/50 × 100% = 6%. **Quality thresholds:** <5% error = excellent (results match theory well), 5-10% = acceptable (normal random variation), >10% = investigate (possible bug or too few trials). **Practice:** Calculate percent error for: (1) Die roll: expected 16.7% for each face, got 12% for "6" → error = ?, (2) 4-color spinner: expected 25% each, got red=32% → error = ?. **When to worry:** High error might mean: bug in code, unfair simulation, or just need more trials. **Success criteria:** Calculate percent error for 3+ scenarios, apply quality thresholds correctly. _Implementation note: Error calculator with threshold indicator (green/yellow/red)._

Dependencies:
* T27.G5.06: Compare experimental probability to theoretical probability
* T27.G5.11: Demonstrate the law of large numbers through simulation





ID: T27.G6.04
Topic: T27 – Chance & Simulations
Skill: Generate synthetic sensor data for AI testing
Description: **Student task:** Generate fake sensor data to test AI systems without real hardware. **Example: Hand detection testing.** Generate 50 fake hand positions: x = 200 + pick random -15 to 15 (adds noise), y = 150 + pick random -15 to 15, confidence = 0.8 + (pick random 0 to 20) / 100 (ranges 0.8-1.0). **Testing scenarios:** (A) High confidence readings (0.9+): AI should respond normally, (B) Low confidence readings (0.6-0.8): AI should show warning or ignore, (C) Jittery data (lots of noise): AI should smooth or filter. **Why synthetic data?** Faster than collecting real data, can create rare edge cases, reproducible for debugging, no camera needed. **Real-world use:** Self-driving car simulation, robot testing, game AI development. **Success criteria:** Generate realistic synthetic data, test AI with different noise levels, identify edge cases. _Implementation note: Synthetic data generator with adjustable noise parameters._

Dependencies:
* T27.G5.03: Use Monte Carlo sampling to estimate π
* T27.G5.04: Write a 5-part simulation plan before coding





ID: T27.G6.05
Topic: T27 – Chance & Simulations
Skill: Model an agent in a discrete grid world
Description: **Student task:** Create a grid-based agent with position and direction state. **Agent variables:** (1) gridX, gridY: integer positions (0-9), (2) direction: 0=up, 1=right, 2=down, 3=left. **Movement commands:** "forward": if direction=0, gridY += 1; if direction=1, gridX += 1; etc. "turn right": direction = (direction + 1) mod 4. **Visualization:** Convert grid to pixels: screenX = gridX × 40, screenY = gridY × 40. Draw grid lines, show agent as arrow pointing in current direction. **Test sequence:** "forward, forward, turn right, forward" starting at (0,0) facing up → should end at (1,2) facing right. **Key concept:** Grid worlds are the foundation for many AI simulations—the discrete positions make it easier to track state and test algorithms. **Success criteria:** Agent moves correctly on grid, direction changes work, visualization shows position and heading. _Implementation note: Visible grid with agent sprite that rotates based on direction._

Dependencies:
* T27.G5.08: Build a random walker agent with state tracking
* T27.G5.04: Write a 5-part simulation plan before coding





ID: T27.G6.06
Topic: T27 – Chance & Simulations
Skill: Simulate dependent events where probabilities change
Description: **Student task:** Simulate drawing marbles without replacement and observe how probabilities change. **Setup:** Bag contains 5 red, 3 blue marbles (list: [R,R,R,R,R,B,B,B]). **First draw:** P(red) = 5/8 = 62.5%. If red drawn, remove it from list. **Second draw:** Now 4 red, 3 blue remain. P(red) = 4/7 = 57.1%. **Simulation comparison:** Run 1000 trials each: (A) WITHOUT replacement (remove drawn marble), (B) WITH replacement (put marble back). **Compare results:** Track P(both red). Without replacement: (5/8)×(4/7) ≈ 35.7%. With replacement: (5/8)×(5/8) = 39.1%. **Key concept:** In dependent events, the outcome of one event changes the probabilities for the next. This is the foundation of conditional probability! **Success criteria:** Simulate both scenarios, explain why probabilities differ, calculate theoretical values. _Implementation note: Visual bag showing marbles being drawn and removed._

Dependencies:
* T27.G5.01.01: Simulate compound events (two dice) and collect sum data
* T27.G4.07: Generate random selections without repetition (sampling without replacement)




ID: T27.G6.06.01
Topic: T27 – Chance & Simulations
Skill: Trace probability changes through sequential draws without replacement
Description: **Student task:** Create a probability tree showing how probabilities change after each draw without replacement. **Setup:** Bag with 4 red, 2 blue marbles. **Tree construction:** First branch: P(red) = 4/6, P(blue) = 2/6. If red drawn first: second branch P(red) = 3/5, P(blue) = 2/5. If blue drawn first: second branch P(red) = 4/5, P(blue) = 1/5. **Calculate all paths:** P(red,red) = (4/6)×(3/5) = 12/30 = 40%, P(red,blue) = (4/6)×(2/5) = 8/30 ≈ 27%, P(blue,red) = (2/6)×(4/5) = 8/30 ≈ 27%, P(blue,blue) = (2/6)×(1/5) = 2/30 ≈ 7%. **Verification:** All probabilities sum to 100%. **Key insight:** Each path's probability is product of branches—this is the multiplication rule for dependent events. **Success criteria:** Build correct probability tree, calculate all 4 path probabilities, verify they sum to 1. _Implementation note: Interactive tree builder with probability calculator._

Dependencies:
* T27.G6.06: Simulate dependent events where probabilities change
* T27.G5.05: Calculate theoretical probability using the formula P = favorable/total




ID: T27.G6.06.02
Topic: T27 – Chance & Simulations
Skill: Compare simulation results for with vs without replacement sampling
Description: **Student task:** Run parallel simulations comparing sampling with and without replacement, analyzing the differences. **Experiment design:** Same starting bag (5 red, 3 blue), draw 3 marbles, track color sequence. Run 1000 trials of each: (A) With replacement: after each draw, put marble back, (B) Without replacement: after each draw, marble stays out. **Data collection:** For each method, count: all red, all blue, mixed combinations. **Expected differences:** With replacement: P(3 red) = (5/8)³ ≈ 24%. Without replacement: P(3 red) = (5/8)×(4/7)×(3/6) ≈ 18%. **Analysis questions:** (1) "Which method has higher P(all same color)?" (Without—once you start a streak, pool becomes more favorable), (2) "Which method gives more consistent results?" (With—probabilities stay constant). **Success criteria:** Run both simulations, compare probabilities, explain the differences. _Implementation note: Side-by-side simulation runners with comparison charts._

Dependencies:
* T27.G6.06.01: Trace probability changes through sequential draws without replacement
* T27.G6.01.02: Automate parameter sweeps with nested loops





ID: T27.G6.07
Topic: T27 – Chance & Simulations
Skill: Design a grid environment with obstacles and goals
Description: **Student task:** Extend the grid world by adding walls and a goal. **Environment elements:** (1) walls list: [[2,3], [2,4], [3,4], [4,4]] (blocked cells), (2) goal: [5,5] (target location), (3) start: [0,0]. **Movement logic update:** Before moving, check: 'if [newX, newY] in walls list, don't move (or bounce back)'. **Win detection:** 'if [gridX, gridY] = goal, say "You win!" and stop'. **Testing:** (A) Try to walk through a wall—should be blocked, (B) Reach the goal—should trigger win, (C) Create a maze configuration that has a valid path to goal. **Visualization:** Draw walls as solid blocks, goal as a star/flag, clear cells as empty. **Extension:** Make some walls only appear 50% of the time (random obstacles). **Success criteria:** Agent respects walls, reaches goal triggers win, maze is navigable. _Implementation note: Grid display with wall/goal visualization._

Dependencies:
* T27.G6.05: Model an agent in a discrete grid world
* T10.G4.01: Search for an item in a list





ID: T27.G6.08
Topic: T27 – Chance & Simulations
Skill: Implement reward functions and track agent outcomes
Description: **Student task:** Add a scoring system to the grid agent and analyze outcomes. **Reward rules:** +10 points: reach goal, -1 point: each step taken, -5 points: bump into wall. **Experiment:** Run 10 trials with random starting positions: 'startX = pick random 0 to 5, startY = pick random 0 to 5'. **Data logging:** For each trial, record [startX, startY, steps, wallBumps, finalScore]. **Analysis questions:** (1) "Which starting positions lead to higher scores?" (Closer to goal, fewer obstacles), (2) "What's the theoretical maximum score from position (4,4) if goal is (5,5)?" (+10 goal - 2 steps = +8), (3) "Why might random movement give negative scores?" (Many steps, wall bumps). **Key concept:** Reward functions define what "success" means—this is how AI learns what to optimize! **Success criteria:** Implement scoring, run 10 trials, identify patterns in results. _Implementation note: Score tracker with trial log table._

Dependencies:
* T27.G6.07: Design a grid environment with obstacles and goals
* T27.G6.01.01: Manually test simulation parameters and log results systematically





ID: T27.G6.09
Topic: T27 – Chance & Simulations
Skill: Create two-sprite interaction with chase/flee dynamics
Description: **Student task:** Create two sprites that detect and respond to each other's positions. **Sprite behaviors:** Cat (predator): moves randomly each tick (pick random direction, move 5 pixels). Mouse (prey): 'if distance to cat < 50 then glide 10 pixels away from cat, else move randomly'. **Detection methods:** (A) 'touching [cat]?' block, (B) 'distance to [cat]' < threshold, (C) Calculate manually: sqrt((catX-mouseX)² + (catY-mouseY)²). **Game loop:** Both sprites update position each tick, creating emergent chase/flee dynamics. **Analysis:** Run for 100 ticks and count: How many times did cat catch mouse? Does mouse survive longer with better flee logic? **Key concept:** Multi-agent systems create emergent behavior—the chase pattern wasn't explicitly programmed, it emerges from individual rules! **Success criteria:** Both sprites move appropriately, mouse flees when cat is near. _Implementation note: Tick counter with catch detection._

Dependencies:
* T27.G6.05: Model an agent in a discrete grid world
* T06.G5.01: Broadcast a custom message and respond in another sprite





ID: T27.G6.10
Topic: T27 – Chance & Simulations
Skill: Compare random, systematic, and stratified sampling methods
Description: **Student task:** Sample from a population using three different methods and compare results. **Population:** 100 survey responses with attributes [age, gender, score]. **Sampling methods:** (1) **Random:** Pick 20 items using pick random index, (2) **Systematic:** Take every 5th item (items 5, 10, 15, 20...), (3) **Stratified:** Ensure 10 male and 10 female in sample. **Comparison metrics:** Does sample average match population average? Does sample have similar gender ratio as population? **Discussion questions:** (1) "When might random sampling give a biased sample?" (By chance, might get mostly one group), (2) "When is stratified sampling better?" (When you need guaranteed representation of subgroups), (3) "What's the risk of systematic sampling?" (If there's a pattern in the data order, might be biased). **Success criteria:** Implement all three methods, compare representativeness, explain trade-offs. _Implementation note: Population generator with sampling tools and comparison stats._

Dependencies:
* T27.G5.02: Simulate random assignment for A/B testing
* T27.G5.11: Demonstrate the law of large numbers through simulation





ID: T27.G6.11
Topic: T27 – Chance & Simulations
Skill: Calculate and verify conditional probability through simulation
Description: **Student task:** Learn conditional probability notation and verify calculations with simulation. **Notation:** P(A|B) = "probability of A given that B occurred." **Example:** Bag has 3 red, 2 blue marbles. What is P(2nd is red | 1st was blue)? **Calculation:** After blue removed, 3 red + 1 blue remain. P(red) = 3/4 = 75%. **Simulation verification:** (1) Run 1000 two-draw trials, (2) Filter to only trials where first was blue, (3) Of those, count what fraction had red second, (4) Should be ≈75%. **Real-world examples:** (A) P(rain | cloudy) ≠ P(rain)—clouds make rain more likely, (B) P(pass test | studied) > P(pass test | didn't study), (C) P(flight delayed | winter) > P(flight delayed | summer). **Formula:** P(A|B) = P(A and B) / P(B). **Success criteria:** Calculate conditional probability for 2+ scenarios, verify one with simulation. _Implementation note: Conditional filter tool showing filtered subset analysis._

Dependencies:
* T27.G6.06: Simulate dependent events where probabilities change
* T27.G5.05: Calculate theoretical probability using the formula P = favorable/total




ID: T27.G6.12
Topic: T27 – Chance & Simulations
Skill: Build a waiting line (queue) simulation
Description: **Student task:** Simulate a service queue to analyze wait times and optimize staffing. **Scenario:** School cafeteria line—students arrive randomly, get served, leave. **Model components:** (1) Arrival: Each tick, 30% chance a new student joins queue, (2) Service: If line not empty, serve one student per tick, (3) Track: queue length, wait time for each student, max queue length. **Build steps:** (1) Create list for queue (student arrival times), (2) Each tick: maybe add student (pick random), (3) If queue not empty: remove first student, calculate wait time, (4) Log wait times to results list. **Run for 100 ticks:** Calculate average wait time, max queue length. **Optimization question:** "What if we add a second server? How does that change wait times?" (Add: if queue length > 1, serve two per tick). **Key concept:** Queue simulations help optimize real-world systems—restaurants, hospitals, airports! **Success criteria:** Working queue simulation, average wait time calculated, compare 1 vs 2 servers. _Implementation note: Visual queue display with wait time statistics._

Dependencies:
* T27.G6.08: Implement reward functions and track agent outcomes
* T27.G6.01.02: Automate parameter sweeps with nested loops





ID: T27.G7.01
Topic: T27 – Chance & Simulations
Skill: Build a predator-prey simulation with probabilistic behaviors
Description: **Student task:** Build a predator-prey simulation where agents have probabilistic decision-making. **Predator behavior:** Each step: 70% chance move toward prey (calculate direction), 30% chance random move. Has "hunger" variable that increases each step, resets to 0 when catching prey, dies if hunger > 50. **Prey behavior:** Each step: if distance to predator < 100, flee (move away); else random move. Has "energy" that decreases by 1 each step, dies if energy = 0. **Simulation metrics:** Run 100 time steps, log: number of catches, average prey lifespan, predator hunger over time. **Analysis:** (1) "Does the prey always get caught?" (No—randomness means sometimes it escapes), (2) "What if predator is 90% vs 50% likely to chase?" (Higher = more catches, but more predictable). **Key concept:** Probabilistic rules create varied, realistic behaviors. **Success criteria:** Both agents have correct probabilistic behaviors, metrics logged correctly. _Implementation note: State variables for both agents with visual tracking._

Dependencies:
* T27.G6.09: Create two-sprite interaction with chase/flee dynamics
* T27.G6.08: Implement reward functions and track agent outcomes





ID: T27.G7.02
Topic: T27 – Chance & Simulations
Skill: Trace how an agent learns from rewards over multiple trials
Description: **Student task:** Observe and trace a pre-built "learning agent" simulation to understand reinforcement learning basics. **Agent setup:** Preference table stores direction weights for each grid cell. Initially: up=25%, right=25%, down=25%, left=25%. **Learning rule:** After reaching goal, trace back the successful path. For each cell on the path, increase weight of the direction taken by 10%. Normalize so weights sum to 100%. **Trace activity:** Run 10 trials, recording for cell (2,2): Trial 1 weights, Trial 5 weights, Trial 10 weights. **Analysis questions:** (1) "How did the preference table change?" (Successful directions get higher weights), (2) "Why does the agent take fewer steps by trial 10?" (It's learned which directions lead to goal), (3) "Is this 'intelligent'?" (It's learning from experience, a basic form of AI!). **Key concept:** This is reinforcement learning—the foundation of modern AI like game-playing bots. **Success criteria:** Accurately trace weight changes, explain why performance improves. _Implementation note: Visible preference table updating after each trial._

Dependencies:
* T27.G6.08: Implement reward functions and track agent outcomes
* T27.G7.01: Build a predator-prey simulation with probabilistic behaviors





ID: T27.G7.03
Topic: T27 – Chance & Simulations
Skill: Test game fairness using synthetic player populations
Description: **Student task:** Test whether a game treats different player groups fairly using synthetic test populations. **Create synthetic players:** 50 "new players" (skill = pick random 1 to 3), 50 "experienced players" (skill = pick random 7 to 10). **Run experiment:** Each synthetic player plays the game, record their score. **Analysis:** (1) Average score for new players vs experienced players, (2) Is 3x higher for experienced fair? (Yes—skill should matter), (3) If new players score 0 and experienced score 100, is that fair? (Maybe not—game might be too punishing). **Additional test—Avatar bias:** Create players with different avatar types, same skill level. Do certain avatars get different outcomes? (If yes, that's unfair bias!). **Fairness questions:** "Should random elements affect skilled and new players equally?" "Should everyone have SOME chance to win?" **Success criteria:** Create test populations, run comparative analysis, identify fairness issues. _Implementation note: Population generator with group comparison stats._

Dependencies:
* T27.G6.04: Generate synthetic sensor data for AI testing
* T27.G6.08: Implement reward functions and track agent outcomes





ID: T27.G7.04
Topic: T27 – Chance & Simulations
Skill: Perform permutation tests to determine if differences are statistically meaningful
Description: **Student task:** Use shuffling to test whether an observed difference could happen by chance. **Scenario:** Version A scores: [85, 90, 88] (avg=87.7). Version B scores: [70, 75, 72] (avg=72.3). Real difference = 15.4 points. Is this meaningful or just random variation? **Permutation test procedure:** (1) Combine all scores into one pool: [85,90,88,70,75,72], (2) Shuffle the pool, (3) Split into fake "A" (first 3) and fake "B" (last 3), (4) Calculate fake difference in averages, (5) Repeat 200 times, (6) Count: How often is |fake difference| ≥ 15.4? **Interpretation:** If only 5 of 200 shuffles (2.5%) have difference ≥ 15.4, the real difference is unlikely to be chance. If 50 of 200 (25%) have difference ≥ 15.4, could easily be chance. **Key concept:** This is the foundation of statistical hypothesis testing—used by scientists to determine if results are "significant." **Success criteria:** Implement permutation test, interpret results correctly. _Implementation note: Shuffle animation with running count of extreme differences._

Dependencies:
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T27.G6.02: Use random seeds for reproducible simulations





ID: T27.G7.05
Topic: T27 – Chance & Simulations
Skill: Write a model card documenting simulation assumptions and limitations
Description: **Student task:** Write a "model card" documenting your simulation following AI industry standards. **Model card sections:** (1) **Purpose:** What question does this simulation answer? (e.g., "Estimates how long prey survives when predator has different chase probabilities"), (2) **Assumptions:** What did we simplify? (e.g., "Agents can't see through walls," "All agents move at same speed," "Environment is 2D grid"), (3) **Limitations:** What can't it predict? (e.g., "Doesn't model fatigue," "Assumes perfect detection," "Only one predator"), (4) **Who might be affected:** Would decisions based on this simulation hurt anyone? (e.g., "If used to design a real security system, missed assumptions could create vulnerabilities"), (5) **Validation:** How did we test that it works correctly? **Why this matters:** Real AI systems require documentation so others understand limitations. Undocumented assumptions cause real-world failures! **Success criteria:** Complete all 5 sections with thoughtful, specific content. _Implementation note: Model card template with required fields._

Dependencies:
* T27.G7.01: Build a predator-prey simulation with probabilistic behaviors
* T27.G7.03: Test game fairness using synthetic player populations





ID: T27.G7.06.01
Topic: T27 – Chance & Simulations
Skill: Scale to multi-agent simulations using clones (5-10 agents)
Description: **Student task:** Scale from 2 agents to 5-10 using clone-based architecture. **Architecture:** Each clone has own state stored in lists indexed by clone ID: positions[id], speeds[id], types[id], energies[id]. **Clone-to-clone interaction:** Each frame, each clone: (1) Gets its position from list using ID, (2) Checks distance to ALL other clones, (3) Responds based on type (predator chases prey, prey flees predators, neutrals wander). **Independence test:** Delete one clone mid-simulation—others should continue working without crashing. **Common bugs:** Using sprite variables instead of list lookup (causes all clones to share state), forgetting to update list when clone state changes. **Emergent behaviors:** Watch for flocking, chasing packs, or prey grouping for safety. **Success criteria:** 5-10 agents running simultaneously with independent states, interactions work correctly. _Implementation note: Clone ID tracking with list-based state management._

Dependencies:
* T27.G7.01: Build a predator-prey simulation with probabilistic behaviors
* T11.G5.03: Create clones with different behaviors





ID: T27.G7.06.02
Topic: T27 – Chance & Simulations
Skill: Aggregate and display population-level metrics from multi-agent simulations
Description: **Student task:** Calculate population-level statistics from your multi-agent simulation and display them as a real-time dashboard. **Metrics to calculate:** (1) **Population counts:** # prey alive, # predators alive, (2) **Average position:** center of mass = (avg of all x positions, avg of all y positions), (3) **Total energy:** sum of all agents' energy levels, (4) **Clustering metric:** standard deviation of positions (low = clustered, high = spread out). **Dashboard display:** Show all metrics updating each tick. Graph population over time (line chart showing prey count vs predator count vs time). **Analysis questions:** (1) "Do prey cluster for safety?" (Check clustering metric when predator is near), (2) "Does total energy stay constant, increase, or decrease?" (Depends on your rules). **Key concept:** Population-level views reveal patterns invisible when watching individual agents. **Success criteria:** All 4 metrics calculated correctly, dashboard updates in real-time. _Implementation note: Real-time stat display with live graph._

Dependencies:
* T27.G7.06.01: Scale to multi-agent simulations using clones (5-10 agents)
* T26.G5.01: Calculate mean from a dataset






ID: T27.G7.07
Topic: T27 – Chance & Simulations
Skill: Identify and fix bias in random selection algorithms
Description: **Student task:** Investigate how "random" selection can be unfair and learn to detect/fix biases. **Example 1—Biased pool:** Random from [A,A,A,B] gives 75% A, 25% B—the pool itself is biased, not the selection. Fix: Ensure equal representation in pool. **Example 2—Flawed shuffle (Fisher-Yates bug):** Swap with ANY position (biased) vs swap with LATER positions only (correct). Test: Run 10000 shuffles of [1,2,3], count how often each permutation appears. Correct algorithm gives ~1667 each; flawed gives unequal counts. **Historical case studies:** (A) 1970 Vietnam draft lottery—capsules not mixed well, later birthdays called more, (B) Early browser random number bugs exploited by online casinos. **Fixes:** Use verified library functions, audit distributions with many trials, use stratified selection when representation matters. **Success criteria:** Identify bias in 2+ scenarios, explain why they're biased, propose corrections. _Implementation note: Shuffle tester comparing biased vs correct algorithms._

Dependencies:
* T27.G7.03: Test game fairness using synthetic player populations
* T27.G6.10: Compare random, systematic, and stratified sampling methods




ID: T27.G7.08
Topic: T27 – Chance & Simulations
Skill: Simulate disease spread with infection probability
Description: **Student task:** Build a simplified epidemic simulation showing how diseases spread through a population. **SIR Model basics:** Agents are Susceptible (S), Infected (I), or Recovered (R). **Rules:** (1) Infected agents have 20% chance to infect nearby Susceptible agents each tick, (2) Infected agents recover after 10 ticks and become immune (R), (3) Recovered agents can't be reinfected. **Setup:** 50 agents, 1 starts infected. **Metrics to track:** Peak infected count, total ever infected, time to peak, time to end. **Parameter experiments:** (A) Infection rate 10% vs 30%—how does peak change? (B) Starting with 1 vs 5 infected—how does timeline change? (C) Add "social distancing"—agents move less, lower infection rate. **Real-world connection:** This is how epidemiologists model COVID, flu, measles! **Key insight:** Small changes in infection rate cause big changes in outcomes—exponential growth is powerful. **Success criteria:** Working SIR simulation, track metrics, compare different infection rates. _Implementation note: Agents with color-coded states (green=S, red=I, blue=R)._

Dependencies:
* T27.G7.06.01: Scale to multi-agent simulations using clones (5-10 agents)
* T27.G7.01: Build a predator-prey simulation with probabilistic behaviors




ID: T27.G7.09
Topic: T27 – Chance & Simulations
Skill: Model weather transitions using Markov chain probabilities
Description: **Student task:** Build a Markov chain weather model where tomorrow's weather depends only on today's weather. **Transition matrix:** If today is Sunny: 70% tomorrow sunny, 30% rainy. If today is Rainy: 40% tomorrow sunny, 60% rainy. **Simulation:** (1) Start with random weather, (2) Each day: use today's state to pick tomorrow's state, (3) Run 100 days, track sequence. **Analysis questions:** (1) "What fraction of days are sunny in the long run?" (Calculate steady state: ~57% sunny), (2) "If it's been rainy for 3 days, is sunny more likely?" (No—Markov property means only today matters, not history!), (3) "How long are typical sunny/rainy streaks?" (Simulate and count). **Key concept:** Markov chains are "memoryless"—the future depends only on the present, not the past. Used in: weather forecasting, page rank, text generation. **Extension:** Add a third state (Cloudy) with 3×3 transition matrix. **Success criteria:** Implement transition logic, run 100-day simulation, calculate long-run percentages. _Implementation note: Transition matrix as 2D list, state visualization._

Dependencies:
* T27.G6.11: Calculate and verify conditional probability through simulation
* T27.G7.01: Build a predator-prey simulation with probabilistic behaviors





ID: T27.G8.01
Topic: T27 – Chance & Simulations
Skill: Build an automated simulation-to-dashboard pipeline
Description: **Student task:** Create a professional end-to-end pipeline from simulation to interactive dashboard. **Pipeline stages:** (1) **Data collection:** Automated parameter sweep—5 configurations × 50 trials each = 250 total runs. (2) **Storage:** Results in table with columns [configID, trialNum, outcome, score, timestamp]. (3) **Analysis:** Code calculates for each config: mean, median, range, standard deviation. (4) **Visualization:** Dashboard with bar chart comparing config means, error bars showing variability. (5) **Interactivity:** Click a config bar to see detailed histogram of that config's results. **Professional features:** Auto-refresh when new data added, export results to CSV, color-code configs by performance. **Why this matters:** This is how professional data scientists work—automating the entire pipeline from experiment to insight. **Success criteria:** Complete pipeline running, dashboard updates automatically, interactive drill-down works. _Implementation note: Integrated data collection, analysis, and visualization workflow._

Dependencies:
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T27.G7.06.02: Aggregate and display population-level metrics from multi-agent simulations
* T27.G7.05: Write a model card documenting simulation assumptions and limitations





ID: T27.G8.02
Topic: T27 – Chance & Simulations
Skill: Use bootstrap sampling to estimate confidence intervals
Description: **Student task:** Learn bootstrap sampling to understand how measurements vary by chance. **Bootstrap procedure:** (1) Original data: 100 scores, (2) Draw 100 items WITH replacement (same item can be picked multiple times), (3) Calculate mean of this bootstrap sample, (4) Repeat 500 times → 500 bootstrap means. **Analysis:** Create histogram of 500 means to see the "sampling distribution." Find the middle 95%: sort means, take values at positions 13 and 488 (2.5% from each end). This range is your 95% confidence interval! **Interpretation:** "We are 95% confident the true population mean is between X and Y." **Why WITH replacement?** Simulates drawing from a population—each draw is independent. **Real-world use:** Medical studies, poll margins of error, A/B test confidence. **Success criteria:** Generate bootstrap samples, calculate 95% CI, interpret correctly. _Implementation note: Bootstrap sampler with histogram and CI visualization._

Dependencies:
* T27.G6.01.02: Automate parameter sweeps with nested loops
* T27.G7.04: Perform permutation tests to determine if differences are statistically meaningful
* T26.G6.01: Calculate statistics (mean, median, mode, range)






ID: T27.G8.03
Topic: T27 – Chance & Simulations
Skill: Integrate AI assistants into simulation analysis workflows
Description: **Student task:** Use AI assistants to help analyze simulation results and suggest next steps. **Workflow:** (1) Export simulation summary as structured text: "Config A: mean=85, sd=12. Config B: mean=72, sd=8...", (2) Prompt XO/ChatGPT: "Here are my simulation results. What patterns do you see? What parameter should I test next? Are there any outliers or anomalies?", (3) Critically evaluate AI response: Did it notice the outlier in Config C? Did it suggest something useful? Did it miss context you know? **Reflection questions:** (1) "What did the AI catch that you missed?" (2) "What did you know that the AI couldn't?" (context about your simulation design), (3) "Would you trust the AI's suggestion without verification?" **Key insight:** AI assistants are tools, not replacements—they can spot patterns but lack domain knowledge. Always verify AI suggestions! **Success criteria:** Complete AI-assisted analysis, write critical reflection comparing AI insights to your own. _Implementation note: Export tool with AI integration and reflection template._

Dependencies:
* T27.G7.05: Write a model card documenting simulation assumptions and limitations
* T27.G8.01: Build an automated simulation-to-dashboard pipeline
* T21.G6.01.01: Make a basic ChatGPT request with one parameter





ID: T27.G8.04
Topic: T27 – Chance & Simulations
Skill: Write simulation-backed policy briefs for real-world problems
Description: **Student task:** Write a 1-2 page policy brief using simulation evidence to recommend action on a real problem. **Brief structure:** (1) **Problem:** "School lunch lines average 15 minutes, students miss class time." (2) **Method:** "Simulated 3 checkout configurations with 500 students over 50 lunch periods." (3) **Findings:** "Configuration B (2 lines with mobile ordering) reduced average wait by 40% (15min → 9min)." (4) **Recommendation:** "Implement Configuration B; estimated cost $X, saves Y student-hours per week." (5) **Limitations & Ethics:** "Assumes equal walking speed; doesn't account for students with disabilities who may need priority access; mobile ordering requires smartphone access." (6) **Next Steps:** "Pilot test in one cafeteria before full rollout." **Real-world connection:** This is civic data journalism—using data to advocate for policy changes! **Success criteria:** Complete all 6 sections with specific, evidence-backed content. _Implementation note: Policy brief template with evidence linking._

Dependencies:
* T27.G8.03: Integrate AI assistants into simulation analysis workflows
* T27.G7.05: Write a model card documenting simulation assumptions and limitations
* T32.G7.07: Identify stakeholders affected by a computing solution




ID: T27.G8.04.01
Topic: T27 – Chance & Simulations
Skill: Structure a policy brief with simulation-backed evidence sections
Description: **Student task:** Learn the professional structure of a policy brief and create an outline for your simulation study. **Required sections:** (1) **Executive Summary:** 2-3 sentence overview for busy decision-makers, (2) **Problem Statement:** What issue needs solving? Who is affected? Why does it matter?, (3) **Methodology:** How did your simulation model the problem? What assumptions?, (4) **Key Findings:** What did the data show? Include specific numbers, (5) **Recommendations:** What action should be taken? What's the expected benefit?, (6) **Limitations:** What did your simulation NOT capture? What uncertainties exist?, (7) **Next Steps:** How should this be tested/validated before full implementation? **Practice:** Write an outline for: "Should our school add a traffic light at the main entrance?" **Success criteria:** Complete outline with all 7 sections, each with 2-3 bullet points. _Implementation note: Outline template with section prompts._

Dependencies:
* T27.G8.04: Write simulation-backed policy briefs for real-world problems




ID: T27.G8.04.02
Topic: T27 – Chance & Simulations
Skill: Support policy recommendations with simulation statistics and visualizations
Description: **Student task:** Create compelling evidence presentations using your simulation data. **Evidence types:** (1) **Comparative statistics:** "Configuration A: mean wait 15min, sd 4min. Configuration B: mean wait 9min, sd 2min. Difference significant (p < 0.05)." (2) **Visualizations:** Side-by-side bar charts, before/after comparison, trend lines. (3) **Confidence intervals:** "We estimate 30-50% reduction in wait times (95% CI)." **Practice problems:** Create evidence package for: (A) Comparing two traffic light timings, (B) Evaluating three cafeteria layouts, (C) Testing vaccination rates vs disease spread. **Critical evaluation:** Would a skeptic find this convincing? What counter-arguments might they raise? How would you address them? **Key concept:** Strong evidence = clear statistics + compelling visuals + acknowledgment of uncertainty. **Success criteria:** Create 3 evidence presentations with statistics, charts, and confidence measures. _Implementation note: Chart templates with statistical summary generators._

Dependencies:
* T27.G8.04.01: Structure a policy brief with simulation-backed evidence sections
* T27.G8.02: Use bootstrap sampling to estimate confidence intervals




ID: T27.G8.04.03
Topic: T27 – Chance & Simulations
Skill: Present and defend simulation-based recommendations to stakeholders
Description: **Student task:** Present your policy brief to a panel and defend your methodology and conclusions. **Presentation elements:** (1) 5-minute summary of problem, method, findings, (2) Key visualizations that communicate main message, (3) Clear "ask"—what action do you want the audience to take? **Defense preparation:** Anticipate questions: (A) "How do we know your simulation is realistic?", (B) "What if your assumptions are wrong?", (C) "What's the cost of your recommendation?", (D) "Have you considered [alternative approach]?". **Practice responses:** For each anticipated question, prepare 30-second response with evidence reference. **Peer review:** Exchange briefs with classmate, role-play as skeptical stakeholder, give feedback. **Key concept:** Simulation results only matter if you can communicate them effectively and withstand scrutiny. **Success criteria:** Complete presentation, field 3+ questions, incorporate peer feedback into revised brief. _Implementation note: Presentation template with Q&A preparation guide._

Dependencies:
* T27.G8.04.02: Support policy recommendations with simulation statistics and visualizations
* T27.G7.05: Write a model card documenting simulation assumptions and limitations





ID: T27.G8.05
Topic: T27 – Chance & Simulations
Skill: Analyze how environment design creates bias in learned agent behaviors
Description: **Student task:** Run the same learning agent in different environments and analyze how design affects what it learns. **Experiment:** **Maze A:** One clear path to goal. **Maze B:** Multiple paths—one short (hidden), one long (obvious). **Run each:** 50 learning trials per maze. **Compare results:** In Maze A, agent consistently learns the same path. In Maze B, agent might learn the LONGER path if it found reward before discovering shortcut—"good enough" prevented finding optimal! **Analysis questions:** (1) "Why might an agent learn a suboptimal solution?" (Early reward stops exploration), (2) "How is this like AI training data bias?" (AI learns patterns in its training environment, which may not generalize), (3) "How could you design the environment to encourage better learning?" (Sparse rewards, exploration bonuses). **Real-world connection:** Self-driving cars trained in sunny California struggle with snow. Hiring AI trained on historical data perpetuates past biases. **Success criteria:** Complete comparative analysis, explain bias mechanism, connect to real AI issues. _Implementation note: Dual maze comparison with path visualization._

Dependencies:
* T27.G7.02: Trace how an agent learns from rewards over multiple trials
* T27.G7.05: Write a model card documenting simulation assumptions and limitations
* T32.G7.07: Identify stakeholders affected by a computing solution





ID: T27.G8.06
Topic: T27 – Chance & Simulations
Skill: Explain pseudorandom vs true random and their appropriate uses
Description: **Student task:** Explore how computers generate "random" numbers and when different types are needed. **Demonstration:** Same seed → same "random" sequence every time. Change seed → different sequence. **How pseudorandom works:** Linear Congruential Generator: next = (a × current + c) mod m. Simple formula, deterministic, but LOOKS random. **Research topics:** (1) **Speedrunning exploits:** Video game speedrunners manipulate seeds to get "lucky" item drops—because they're predictable! (2) **Cryptography requirements:** Encryption needs TRUE randomness from hardware sources (mouse movement timing, electrical noise, radioactive decay). Using pseudorandom for crypto = hackable! **Discussion questions:** (1) "When is pseudorandom good enough?" (Games, simulations, sampling), (2) "When must you use true randomness?" (Passwords, encryption keys, lotteries with real money), (3) "Could someone predict your 'random' game if they knew the algorithm?" (Yes, if they know the seed!). **Success criteria:** Explain the difference, identify appropriate uses for each. _Implementation note: LCG visualizer showing formula generating sequence._

Dependencies:
* T27.G6.02: Use random seeds for reproducible simulations
* T27.G7.07: Identify and fix bias in random selection algorithms




ID: T27.G8.07
Topic: T27 – Chance & Simulations
Skill: Use physics simulation for probability experiments (Galton board)
Description: **Student task:** Build a virtual Galton board (bean machine) using CreatiCode's 2D physics engine to demonstrate the normal distribution. **Build steps:** (1) Initialize 2D physics world with gravity: 'initialize 2D physics world with gravity x [0] y [-100]', (2) Create rows of pegs (circles with frozen physics bodies), (3) Drop balls from top center with small random x offset, (4) Collect balls in bins at bottom, count per bin. **Physics setup:** Balls have restitution 50% (bounce), pegs have friction. **After 100+ balls:** The bin counts form a bell curve! **Analysis questions:** (1) "Why does a ball end up in the middle more often?" (Equal chance left/right at each peg → more paths to middle), (2) "How is this related to flipping coins?" (Each peg is like a coin flip—left or right). **Connection:** This is the Central Limit Theorem in physical form—many random choices sum to a normal distribution. **Success criteria:** Working Galton board, bell curve visible in bin counts. _Implementation note: Use physics engine blocks for realistic ball bouncing._

Dependencies:
* T27.G7.01: Build a predator-prey simulation with probabilistic behaviors
* T27.G5.01.02: Analyze compound event distributions and explain why 7 is most common




ID: T27.G8.08
Topic: T27 – Chance & Simulations
Skill: Apply variance reduction techniques to improve simulation efficiency
Description: **Student task:** Learn and apply techniques to get accurate simulation results with fewer trials. **Problem:** Estimating probability of rare event (1%) with standard Monte Carlo requires 10,000+ trials for accuracy. **Technique 1—Stratified sampling:** Instead of fully random, ensure proportional sampling from known subgroups. Run both methods, compare variance. **Technique 2—Antithetic variates:** For each random number R, also use 1-R. Reduces variance because R and 1-R are negatively correlated. **Experiment:** Estimate π with 500 random points vs 250 pairs of antithetic points. Compare standard deviation of estimates over 20 runs. **Analysis questions:** (1) "Why does stratified sampling reduce variance?" (Guarantees coverage of all subgroups), (2) "When is antithetic sampling helpful?" (When outcome is monotonic in the random variable). **Key concept:** Smart sampling > brute force. Professional simulations use these techniques to save computation time. **Success criteria:** Implement both techniques, demonstrate reduced variance. _Implementation note: Variance comparison across multiple runs._

Dependencies:
* T27.G8.02: Use bootstrap sampling to estimate confidence intervals
* T27.G7.04: Perform permutation tests to determine if differences are statistically meaningful




ID: T27.G8.09
Topic: T27 – Chance & Simulations
Skill: Perform sensitivity analysis on simulation parameters
Description: **Student task:** Systematically analyze how sensitive simulation outcomes are to changes in each input parameter. **Procedure:** (1) Identify all parameters: e.g., predator speed, prey speed, detection range, starting populations. (2) For each parameter, vary by ±10%, ±25%, ±50% while holding others constant. (3) Record outcome change (e.g., average prey survival time). (4) Calculate sensitivity index: (% change in output) / (% change in input). **Results table:** Parameter | Base value | Sensitivity index. **Interpretation:** High sensitivity (>1) means small input changes cause big output changes—these parameters need careful calibration! Low sensitivity (<0.1) means parameter barely matters. **Tornado diagram:** Sort parameters by sensitivity, create horizontal bar chart showing range of outcomes. **Key concept:** Sensitivity analysis identifies which assumptions matter most—crucial for model credibility. **Success criteria:** Analyze 4+ parameters, create tornado diagram, identify most sensitive parameter. _Implementation note: Automated parameter variation with tornado chart generation._

Dependencies:
* T27.G8.01: Build an automated simulation-to-dashboard pipeline
* T27.G6.01.02: Automate parameter sweeps with nested loops




ID: T27.G8.10
Topic: T27 – Chance & Simulations
Skill: Implement evolutionary optimization using random mutation and selection
Description: **Student task:** Build a simple genetic algorithm to optimize a solution through random variation and selection. **Problem:** Find the best parameters for a game AI (speed, aggression, caution) to maximize score. **Algorithm:** (1) Create population of 10 random parameter sets, (2) Run each set in simulation, record scores, (3) Select top 3 performers as "parents", (4) Create new population by copying parents with random mutations (e.g., speed ± pick random -5 to 5), (5) Repeat for 20 generations. **Visualization:** Graph best score and average score per generation—should see improvement over time! **Analysis questions:** (1) "Why do we keep top performers?" (Preserve good solutions), (2) "Why add random mutations?" (Explore new possibilities, escape local optima), (3) "How is this like biological evolution?" (Survival of fittest + variation). **Real-world use:** Neural network training, game AI, logistics optimization. **Success criteria:** Algorithm improves scores over generations, visualize improvement. _Implementation note: Population list with mutation and selection logic._

Dependencies:
* T27.G8.01: Build an automated simulation-to-dashboard pipeline
* T27.G7.01: Build a predator-prey simulation with probabilistic behaviors




ID: T27.G8.11
Topic: T27 – Chance & Simulations
Skill: Use seeded random lists for batch simulation experiments
Description: **Student task:** Leverage CreatiCode's 'set list to N random numbers with seed' block for efficient batch simulations. **Procedure:** (1) Generate 1000 random numbers with seed 42: 'set [randomList] to (1000) random numbers with seed (42)', (2) Use list values in simulation instead of calling pick random repeatedly, (3) Run same simulation on different seeds (42, 43, 44...) to create replications. **Advantages:** (A) Pre-generating is faster than per-trial generation, (B) Same seed = exact reproduction for debugging, (C) Different seeds = independent replications for statistics. **Experiment:** Run 100 trials each with seeds 1-20. Calculate mean and standard deviation of means across seeds. **The Central Limit Theorem:** Distribution of means is tighter than distribution of individual trials! **Analysis:** "Why do we run multiple seeds instead of one big run?" (Each seed is an independent experiment, giving us a sample of possible outcomes). **Success criteria:** Batch runs across 20 seeds, demonstrate mean convergence, explain CLT. _Implementation note: Use CreatiCode's seeded random list block._

Dependencies:
* T27.G6.02: Use random seeds for reproducible simulations
* T27.G8.02: Use bootstrap sampling to estimate confidence intervals




ID: T27.G8.12
Topic: T27 – Chance & Simulations
Skill: Visualize simulation results with real-time charts
Description: **Student task:** Use CreatiCode's chart widget blocks to display live simulation data as bar, line, and pie charts. **Build steps:** (1) Collect simulation data in a list during run, (2) After collection: 'draw [bar v] chart using list [results] x (0) y (0) width (200) height (150)', (3) Add line chart for time series data: 'draw [line v] chart using columns [step,value] from table [data v]'. **Chart types:** Bar for comparing categories (outcomes A vs B vs C), Line for trends over time, Pie for proportions. **Dashboard:** Create multi-chart display showing different views of same data. **Interactivity:** Update chart after each parameter change to show real-time impact. **Professional practice:** Data scientists always visualize before analyzing—patterns visible in charts might be missed in numbers. **Success criteria:** Create 3 different chart types from simulation data, dashboard updates dynamically. _Implementation note: Use widget_drawchartusinglist and widget_drawchartusingcolumn blocks._

Dependencies:
* T27.G8.01: Build an automated simulation-to-dashboard pipeline
* T27.G7.06.02: Aggregate and display population-level metrics from multi-agent simulations




ID: T27.G8.13
Topic: T27 – Chance & Simulations
Skill: Design and validate an epidemiological simulation (capstone)
Description: **Student task:** Build a comprehensive disease spread simulation with validation against known patterns. **CAPSTONE PROJECT** combining multiple simulation skills. **Full SIR model with extensions:** (1) Base SIR from G7.08, (2) Add vaccination: some agents start immune, (3) Add quarantine: infected agents removed from population temporarily, (4) Add super-spreaders: 20% of infected have 3x infection rate. **Validation:** Compare your simulation to known epidemiological patterns: (A) R0 (basic reproduction number)—calculate from your simulation, (B) Herd immunity threshold—test vaccination rates 0%, 50%, 80%, (C) Flatten the curve—test social distancing impact. **Analysis deliverables:** (1) Model card documenting assumptions, (2) Parameter sensitivity analysis, (3) Policy recommendations based on findings. **Real-world connection:** Your simulation mirrors tools used by CDC, WHO for pandemic planning. **Success criteria:** Working simulation with 3+ extensions, validation against 2+ known patterns, complete documentation. _Implementation note: Multi-agent simulation with dashboard and analysis._

Dependencies:
* T27.G7.08: Simulate disease spread with infection probability
* T27.G8.09: Perform sensitivity analysis on simulation parameters
* T27.G8.04.01: Structure a policy brief with simulation-backed evidence sections




ID: T27.G8.14
Topic: T27 – Chance & Simulations
Skill: Build an agent-based environmental model
Description: **Student task:** Create an agent-based model of an ecosystem or environmental system with interacting species and resources. **Model components:** (1) **Resources:** Grass grows with probability each tick, depletes when eaten. (2) **Herbivores:** Rabbits eat grass, reproduce when energy high, die when energy depleted. (3) **Predators:** Foxes eat rabbits, reproduce when energy high, die when hungry. **Population dynamics:** Track population counts over 500 ticks. Expected pattern: predator-prey cycles (Lotka-Volterra). **Environmental factors:** Add random events: drought (grass grows slower), disease outbreak (rabbits die faster), hunting season (foxes removed). **Analysis questions:** (1) "Do populations stabilize, oscillate, or crash?", (2) "What initial conditions lead to extinction?", (3) "How do environmental shocks affect long-term balance?" **Real-world connection:** Ecologists use similar models for wildlife management, conservation planning. **Success criteria:** 3-species model with resource dynamics, population tracking over 500 ticks, analysis of stability conditions. _Implementation note: Multi-sprite ecosystem with population graphs._

Dependencies:
* T27.G7.08: Simulate disease spread with infection probability
* T27.G8.10: Implement evolutionary optimization using random mutation and selection
* T27.G8.01: Build an automated simulation-to-dashboard pipeline




