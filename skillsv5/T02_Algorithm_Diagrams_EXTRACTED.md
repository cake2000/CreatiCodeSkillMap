# T02 - Algorithm Diagrams (Phase 10 Optimized - December 2025)
# Applied Phase 10 comprehensive optimizations:
# MAJOR CHANGES FROM PHASE 9 → PHASE 10:
# 1. NEW SKILLS ADDED (24 new skills for depth, computational thinking, AI-era mastery):
#    K-2 NEW SKILLS (picture-based, visual reasoning):
#    - T02.GK.08: Match a diagram to its real-world outcome picture
#    - T02.G1.10: Debug a diagram by finding the step that causes a wrong outcome
#    - T02.G1.11: Predict outcomes for diagrams with different starting conditions
#    - T02.G2.13: Build a diagram with a "wait for" step (introduces timing concepts)
#    - T02.G2.14: Compare two diagrams and explain which is clearer for a helper
#    G3-5 NEW SKILLS (block-based, algorithmic thinking):
#    - T02.G3.13: Predict how many times each block executes in a simple script
#    - T02.G3.14: Debug a flowchart by finding the missing connection
#    - T02.G4.12: Trace a counting algorithm that skips by 2s, 3s, or 5s
#    - T02.G4.13: Build a flowchart showing algorithm with early exit condition
#    - T02.G4.14: Compare trace tables from two different algorithm approaches
#    - T02.G5.12: Trace a swap algorithm exchanging two values
#    - T02.G5.13: Build and trace a bubble sort visualization for 4 elements
#    - T02.G5.14: Design an algorithm diagram showing data validation steps
#    G6-8 NEW SKILLS (advanced algorithms, AI collaboration, systems):
#    - T02.G6.14: Trace a selection sort algorithm showing minimum-finding passes
#    - T02.G6.15: Draw a flowchart showing algorithm with multiple data sources
#    - T02.G7.12: Trace a merge operation combining two sorted lists
#    - T02.G7.13: Design a flowchart for event-driven algorithm with multiple triggers
#    - T02.G7.14: Build algorithm animation showing backtracking (maze solving)
#    - T02.G8.19: Design algorithm diagrams for distributed systems with message passing
#    - T02.G8.20: Trace a graph traversal algorithm (BFS or DFS) on a simple graph
#    - T02.G8.21: Critique and improve an AI-generated algorithm for bias and edge cases
#    - T02.G8.22: Design modular algorithm architecture separating concerns
#    - T02.G8.23: Build an algorithm complexity comparison tool with visual output
#    - T02.G8.24: Create a comprehensive algorithm portfolio with multiple diagram types
# 2. SKILLS ENHANCED for better active verbs and granularity:
#    - All "Identify" → "Locate and tap", "Find and highlight", or "Detect"
#    - All "Understand" → "Explain", "Demonstrate", or "Verify"
#    - Added prediction-verification cycles throughout
#    - Enhanced debugging focus across all grades
# 3. DEPENDENCY REFINEMENTS:
#    - All X-2 rule validations confirmed
#    - Strengthened visual → code → algorithm progression
#    - Added sorting algorithm progression (G5 bubble → G6 selection → G7 merge concepts)
#    - Better scaffolding for complex algorithm concepts
# 4. ENHANCED AI INTEGRATION:
#    - AI-generated diagram verification and improvement skills
#    - Human-AI collaboration with explicit verification protocols
#    - Critical evaluation of AI outputs for correctness and bias
#    - AI as design partner for complex algorithms
# 5. REAL-WORLD ALGORITHM TYPES EXPANDED:
#    - Sorting algorithms: bubble sort, selection sort, merge concepts
#    - Graph algorithms: BFS/DFS introduction at G8
#    - Distributed systems: message passing, synchronization
#    - Data validation and error handling patterns
#    - Event-driven and backtracking algorithms
# 6. COMPUTATIONAL THINKING EMPHASIS:
#    - Explicit debugging skills at every grade level
#    - Algorithm comparison and efficiency analysis
#    - Pattern recognition in algorithm structures
#    - Abstraction through flowchart templates
# Previous Phase 9 optimizations preserved
# Total: 143 skills (K:8, G1:11, G2:14, G3:15, G4:16, G5:14, G6:17, G7:18, G8:30)

## KINDERGARTEN (8 skills - added T02.GK.08 for outcome matching)




ID: T02.GK.01
Topic: T02 – Algorithm Diagrams
Skill: Tap the arrow showing "what comes next" in a picture strip
Description: **Student task:** Look at a picture strip with 3 pictures connected by arrows (→). Tap the arrow that shows "what comes next" after brushing teeth. **Visual scenario:** Strip shows: [get toothbrush] →₁ [add toothpaste] →₂ [brush teeth]. Students tap arrow₁ or arrow₂ based on the question "Which arrow shows what happens after 'get toothbrush'?" **Correct answer:** Arrow₁. _Implementation note: Introduces arrows as directional symbols in diagrams; focuses on arrow meaning rather than sequencing. Large colorful arrows with highlight on tap. Auto-graded by selection. CSTA: EK‑ALG‑AF‑01._

Dependencies:
* T01.GK.01: Sequence three picture cards for a bedtime routine






ID: T02.GK.02
Topic: T02 – Algorithm Diagrams
Skill: Place pictures into a diagram strip with numbered boxes
Description: **Student task:** Drag 3–4 scrambled picture cards into a pre-made diagram strip with numbered boxes (Box 1 → Box 2 → Box 3 → Box 4) connected by arrows. **Visual scenario:** Empty diagram strip shows: [1] → [2] → [3] → [4]. Cards show "robot getting dressed": (A) robot in pajamas, (B) robot putting on shirt, (C) robot putting on pants, (D) robot with backpack ready. Students drag cards into boxes: A in Box 1, B in Box 2, C in Box 3, D in Box 4. _Implementation note: Focuses on filling a diagram structure (not creating sequence); arrows are fixed in the diagram. Auto-graded by final arrangement. CSTA: EK‑ALG‑AF‑01._

Dependencies:
* T02.GK.01: Identify arrows showing "what comes next" in a picture strip






ID: T02.GK.03
Topic: T02 – Algorithm Diagrams
Skill: Label START and END boxes in a picture diagram
Description: **Student task:** Look at a 3-box diagram strip. Drag the "START" label to the first box and "END" label to the last box. **Visual scenario:** Diagram shows 3 boxes connected by arrows: [?] → [add soap] → [?]. Labels available: "START: turn on water" and "END: dry hands." Students drag START label to first box, END label to last box. _Implementation note: Introduces START/END as diagram conventions; foundational for flowcharts. Audio support reads labels. Auto-graded by correct label placement. CSTA: EK‑ALG‑AF‑01._

Dependencies:
* T02.GK.02: Place pictures into a diagram strip with numbered boxes





ID: T02.GK.04
Topic: T02 – Algorithm Diagrams
Skill: Fix a diagram by moving one misplaced picture box
Description: **Student task:** Look at a 3-box diagram where one picture box is in the wrong position. Drag that box to fix the diagram. **Visual scenario:** Diagram shows "watering a plant": [water plant] → [get watering can] → [watch plant grow]. The first box is wrong—"water plant" should come after "get watering can." Student drags "water plant" box to the middle position. _Implementation note: Emphasizes fixing a diagram structure; wobbling animation highlights misplaced box. Auto-graded by final arrangement. CSTA: EK‑ALG‑AF‑01, EK‑ALG‑PS‑03._

Dependencies:
* T02.GK.03: Label START and END boxes in a picture diagram




ID: T02.GK.05
Topic: T02 – Algorithm Diagrams
Skill: Tap the "question box" in a simple picture diagram
Description: **Student task:** Look at a picture diagram with regular boxes and one special "question box" (shown with a question mark or different color). Tap the question box. **Visual scenario:** Diagram shows: [START: wake up] → [?Is it raining?] → [get umbrella OR wear hat]. The question box has a "?" symbol and different shape/color. Students tap the question box. _Implementation note: Pre-cursor to flowchart decision diamonds; introduces concept that some boxes ask questions. Auto-graded by selection. CSTA: EK‑ALG‑AF‑01._

Dependencies:
* T02.GK.03: Label START and END boxes in a picture diagram


ID: T02.GK.06
Topic: T02 – Algorithm Diagrams
Skill: Tap the picture box that does NOT belong in a diagram
Description: **Student task:** Look at a 4-box diagram strip where one picture box does not belong with the others. Tap the picture box that should be removed. **Visual scenario:** Diagram shows "brushing teeth": [get toothbrush] → [eat pizza] → [add toothpaste] → [brush]. The "eat pizza" box doesn't belong—it's unrelated to the task! Student taps "eat pizza" to identify the wrong box. _Implementation note: Develops error-detection in diagrams; precursor to debugging. Large picture cards with audio support: "Which box doesn't belong?" Auto-graded by selection. CSTA: EK‑ALG‑AF‑01, EK‑ALG‑PS‑03._

Dependencies:
* T02.GK.02: Place pictures into a diagram strip with numbered boxes


ID: T02.GK.07
Topic: T02 – Algorithm Diagrams
Skill: Sort picture cards by step size (big steps vs small steps)
Description: **Student task:** Look at picture cards showing steps of different sizes (e.g., "make a sandwich" vs "put peanut butter on bread"). Sort cards into two piles: "BIG steps" and "small steps." **Visual scenario:** Cards show: (A) "Make lunch" (BIG—many actions inside), (B) "Open jar" (small—one action), (C) "Get dressed" (BIG), (D) "Put on left sock" (small). Students drag each card to the correct pile. Discussion: "Why is 'Make lunch' a BIG step?" **Answer:** It has many smaller steps inside! _Implementation note: Introduces granularity concept visually; precursor to decomposition. Large picture cards with clear visuals. Audio support: "Is this a BIG step or a small step?" Auto-graded by correct pile placement. CSTA: EK‑ALG‑AF‑01, EK‑DEC‑01._

Dependencies:
* T02.GK.04: Fix a diagram by moving one misplaced picture box


ID: T02.GK.08
Topic: T02 – Algorithm Diagrams
Skill: Match a diagram to its real-world outcome picture
Description: **Student task:** Look at a completed picture diagram showing steps for a task. Then look at 3 outcome pictures and tap the one that shows what would happen if you followed the diagram. **Visual scenario:** Diagram shows: [get cup] → [pour milk] → [add cookies]. Outcome pictures: (A) glass of juice, (B) cup of milk with cookies, (C) empty cup. Question: "What do you get if you follow this diagram?" **Correct answer:** (B) cup of milk with cookies. _Implementation note: Tests diagram comprehension by predicting real-world results; bridges abstract diagrams to concrete outcomes. Large colorful pictures. Auto-graded by selection. CSTA: EK‑ALG‑AF‑01._

Dependencies:
* T02.GK.03: Label START and END boxes in a picture diagram
* T02.GK.02: Place pictures into a diagram strip with numbered boxes


---

## GRADE 1 (11 skills - added T02.G1.10 debugging, T02.G1.11 conditional outcomes)




ID: T02.G1.01
Topic: T02 – Algorithm Diagrams
Skill: Build a 4-box diagram strip for a given task
Description: **Student task:** Given a task description, drag 4 picture cards into empty diagram boxes connected by arrows to create an algorithm diagram. **Visual scenario:** Task: "Feed the class fish." Empty diagram: [1] → [2] → [3] → [4]. Available picture cards: (A) sprinkle food, (B) open food container, (C) look at fish tank, (D) close container. Students build diagram: [C: look at tank] → [B: open container] → [A: sprinkle food] → [D: close container]. _Implementation note: Emphasizes building a diagram structure from scratch; arrows are pre-drawn. Auto-graded by valid sequence. CSTA: E1‑ALG‑AF‑01._

Dependencies:
* T02.GK.02: Place pictures into a diagram strip with numbered boxes





ID: T02.G1.02
Topic: T02 – Algorithm Diagrams
Skill: Fill the missing box in a diagram strip
Description: **Student task:** Look at a diagram strip with one empty box marked "?". Select the correct picture card to fill the missing box. **Visual scenario:** Diagram shows "making lemonade": [get cup] → [?] → [stir] → [drink]. Answer choices: (A) add water and lemon, (B) wash hands, (C) put on hat. **Correct answer:** (A) add water and lemon fills the empty box. _Implementation note: MCQ with 3 picture options to complete diagram; emphasizes diagram completeness. Auto-graded by selection. CSTA: E1‑ALG‑AF‑01._

Dependencies:
* T02.G1.01: Build a 4-box diagram strip for a given task





ID: T02.G1.03
Topic: T02 – Algorithm Diagrams
Skill: Trace a diagram and predict the final result
Description: **Student task:** Follow a 4-box diagram strip from START to END. Predict what the result will be after all steps complete. **Visual scenario:** Diagram shows "planting a seed": [START: get pot] → [add soil] → [plant seed] → [water] → END. Question: "What will happen after following this diagram?" Answer choices: (A) plant grows, (B) pot breaks, (C) seed disappears. **Correct answer:** (A) plant grows. _Implementation note: Introduces tracing as following arrows through a diagram; MCQ with 3 picture outcomes. Auto-graded by selection. CSTA: E1‑ALG‑AF‑01._

Dependencies:
* T02.G1.01: Build a 4-box diagram strip for a given task





ID: T02.G1.04
Topic: T02 – Algorithm Diagrams
Skill: Compare two diagrams and identify the broken one
Description: **Student task:** Compare two diagram strips for the same task. One diagram is correct, one has a missing or wrong box. Tap the broken diagram. **Visual scenario:** Task: "Wash hands." Diagram A: [turn on water] → [add soap] → [rub hands] → [dry hands]. Diagram B: [turn on water] → [rub hands] → [dry hands] (missing soap box). Question: "Which diagram is broken?" **Correct answer:** Diagram B (missing a box). _Implementation note: Side-by-side diagram comparison; focuses on diagram structure integrity. Auto-graded by selection. CSTA: E1‑ALG‑AF‑01, E1‑ALG‑PS‑03._

Dependencies:
* T02.G1.01: Build a 4-box diagram strip for a given task





ID: T02.G1.05
Topic: T02 – Algorithm Diagrams
Skill: Debug a diagram by replacing the wrong box
Description: **Student task:** Look at a diagram strip with one clearly wrong picture in a box. Tap the wrong box, then select the correct picture to replace it. **Visual scenario:** Diagram shows "make a sandwich": [eat sandwich] → [add peanut butter] → [add jelly] → [put bread on top]. The first box "eat sandwich" is wrong—you can't eat before making! Student taps it and selects "get bread slices" from 3 options. _Implementation note: Two-step debug: (1) identify wrong box, (2) select replacement. Emphasizes diagram debugging. Auto-graded by correct replacement. CSTA: E1‑ALG‑AF‑01, E1‑ALG‑PS‑03._

Dependencies:
* T02.G1.04: Compare two diagrams and identify the broken one


ID: T02.G1.06
Topic: T02 – Algorithm Diagrams
Skill: Trace a diagram with a Yes/No question box
Description: **Student task:** Follow a diagram that has a "question box" with Yes and No arrows leading to different picture boxes. Answer what happens for a given scenario. **Visual scenario:** Diagram shows: [START: Is it cold?] with two arrows: "Yes" → [wear jacket] → END, "No" → [wear t-shirt] → END. Question: "It IS cold today. What do you wear?" **Correct answer:** wear jacket (follow the Yes arrow). _Implementation note: First branching diagram; introduces conditional paths visually. MCQ with 2 picture options. Auto-graded by selection. CSTA: E1‑ALG‑AF‑01, E1‑ALG‑PS‑03._

Dependencies:
* T02.GK.05: Identify the "question box" in a simple picture diagram
* T02.G1.03: Trace a diagram and predict the final result


ID: T02.G1.07
Topic: T02 – Algorithm Diagrams
Skill: Trace a two-step decision diagram with multiple question boxes
Description: **Student task:** Follow a diagram with TWO question boxes in sequence. Answer what happens based on two conditions. **Visual scenario:** Diagram shows: [START] → ◇Is it morning?◇ "Yes" → ◇Hungry?◇ "Yes" → [Eat breakfast] → END, "No" → [Play] → END. "No" (not morning) → [Go to bed] → END. Question: "It IS morning and you ARE hungry. What do you do?" **Correct answer:** Eat breakfast (follow Yes→Yes path). _Implementation note: Two-level decision tree; extends G1.06 with chained decisions. Picture-based with clear arrow paths. Auto-graded by selection. CSTA: E1‑ALG‑AF‑01, E1‑ALG‑PS‑03._

Dependencies:
* T02.G1.06: Trace a diagram with a Yes/No question box


ID: T02.G1.08
Topic: T02 – Algorithm Diagrams
Skill: Build two different diagrams that achieve the same goal
Description: **Student task:** Create TWO different diagram strips that both accomplish the same task, showing that problems can have multiple solutions. **Visual scenario:** Task: "Get ready for bed." Students build Diagram A: [brush teeth] → [put on pajamas] → [get in bed]. Then build Diagram B: [put on pajamas] → [brush teeth] → [get in bed]. Both achieve the goal! Students drag pictures to build both versions. Question: "Do both diagrams work?" **Answer:** Yes—different order, same result. _Implementation note: Introduces algorithm alternatives; foundational for efficiency comparisons later. Two side-by-side diagram builders. Audio support. Auto-graded by both diagrams achieving goal. CSTA: E1‑ALG‑AF‑01, E1‑ALG‑IM‑04._

Dependencies:
* T02.G1.01: Build a 4-box diagram strip for a given task


ID: T02.G1.09
Topic: T02 – Algorithm Diagrams
Skill: Predict which path a character takes through a branching diagram
Description: **Student task:** Look at a branching diagram with multiple paths. Given information about the character, predict which path they will follow and what they will do. **Visual scenario:** Diagram shows: [START: Robot at home] → ◇Is it sunny?◇ → "Yes" → [go to park] → ◇Has ball?◇ → "Yes" → [play catch] → END, "No" → [play on swings] → END. "No" (not sunny) → [stay inside] → [read book] → END. Question: "It IS sunny and the robot HAS a ball. What will the robot do?" Students trace the Yes→Yes path and select: "Play catch." _Implementation note: Multi-step prediction through branching structure; extends G1.07 with concrete scenarios. Picture-based with clear character and path highlighting. Auto-graded by correct final action selection. CSTA: E1‑ALG‑AF‑01, E1‑ALG‑PS‑03._

Dependencies:
* T02.G1.07: Trace a two-step decision diagram with multiple question boxes


ID: T02.G1.10
Topic: T02 – Algorithm Diagrams
Skill: Debug a diagram by finding the step that causes a wrong outcome
Description: **Student task:** Look at a diagram that produces a wrong result. Find which step is causing the problem by tracing through and checking each step's effect. **Visual scenario:** Diagram for "making toast": [put bread in toaster] → [press button] → [take out bread] → [put butter on bread]. But the toast is burned! Students trace: Step 1 OK, Step 2 OK... wait, there's no "wait until done" step between pressing button and taking out bread! They tap the gap where a step is missing. Alternate version: one step says "wait 10 minutes" — that's too long! **Correct answer:** Identify the missing or wrong step. _Implementation note: Introduces debugging as systematic checking; connects outcome to step. Animated outcome shows "what went wrong." Auto-graded by correct identification. CSTA: E1‑ALG‑PS‑03._

Dependencies:
* T02.G1.03: Trace a diagram and predict the final result
* T02.G1.05: Debug a diagram by replacing the wrong box


ID: T02.G1.11
Topic: T02 – Algorithm Diagrams
Skill: Predict outcomes for diagrams with different starting conditions
Description: **Student task:** Look at the same diagram but with different starting information. Predict what happens in each case. **Visual scenario:** Diagram: [Check weather] → ◇Sunny?◇ → Yes: [Go to park] → END, No: [Stay inside] → END. Scenario 1: "Today is sunny!" What happens? → Go to park. Scenario 2: "Today is rainy!" What happens? → Stay inside. Scenario 3: "Today is cloudy but not raining!" What happens? → Discuss what "sunny" means — is cloudy still sunny? _Implementation note: Same algorithm, different inputs → different outputs; foundational for understanding parameters. Three scenarios with same diagram. Auto-graded by correct predictions. CSTA: E1‑ALG‑AF‑01._

Dependencies:
* T02.G1.06: Trace a diagram with a Yes/No question box
* T02.G1.09: Predict which path a character takes through a branching diagram


---

## GRADE 2 (14 skills - added T02.G2.13 timing, T02.G2.14 clarity comparison)




ID: T02.G2.01
Topic: T02 – Algorithm Diagrams
Skill: Convert a picture diagram into a text-label diagram
Description: **Student task:** Look at a 4-box picture diagram. Create an equivalent text-label diagram by dragging word labels into matching boxes. **Visual scenario:** Picture diagram shows "getting ready for school": [🌅wake up] → [👕get dressed] → [🍳eat breakfast] → [🎒grab backpack]. Empty text diagram: [___] → [___] → [___] → [___]. Students drag text labels: "Wake up" → "Get dressed" → "Eat" → "Get bag" to match the picture diagram. _Implementation note: Introduces text-based diagrams as abstraction from pictures; same structure, different representation. Auto-graded by label placement. CSTA: E2‑ALG‑AF‑01._

Dependencies:
* T02.G1.01: Build a 4-box diagram strip for a given task





ID: T02.G2.02
Topic: T02 – Algorithm Diagrams
Skill: Match a text-label diagram to its picture diagram
Description: **Student task:** Look at a text-label diagram. Select which picture diagram shows the same algorithm from 2-3 options. **Visual scenario:** Text diagram: [Get ball] → [Throw ball] → [Catch ball]. Picture diagram options: (A) [🏀get] → [🤾throw] → [🙌catch], (B) [⚽kick] → [🏃run] → [🪑sit], (C) [🍕eat] → [😴sleep] → [🎮play]. **Correct answer:** (A). _Implementation note: Reverses G2.01 direction; tests understanding that diagrams can use different representations. Auto-graded by selection. CSTA: E2‑ALG‑AF‑01._

Dependencies:
* T02.G2.01: Convert a picture diagram into a text-label diagram





ID: T02.G2.03
Topic: T02 – Algorithm Diagrams
Skill: Trace a text-label diagram on a number line
Description: **Student task:** Follow a text-label diagram with movement instructions. Track position on a number line and predict the final result. **Visual scenario:** Diagram: [START at 0] → [Move right 2] → [Move right 3] → [Say number]. Number line 0-10 shown below. Students trace: 0 → 2 → 5 → say "5". Question: "What number does the character say?" Answer choices: 3, 5, 7. **Correct answer:** 5. _Implementation note: Introduces tracing as stepping through diagram boxes while tracking state. Auto-graded by final answer. CSTA: E2‑ALG‑AF‑01, E2‑ALG‑PS‑03._

Dependencies:
* T02.G2.02: Match a text-label diagram to its picture diagram





ID: T02.G2.04
Topic: T02 – Algorithm Diagrams
Skill: Build a trace table for a diagram step-by-step
Description: **Student task:** As each box in a diagram is revealed, mark the character's position in a trace table. **Visual scenario:** Diagram boxes revealed one at a time: [Start at 2] → write "2" in table, [Move right 3] → write "5", [Move left 1] → write "4", [Move right 2] → write "6". Trace table has columns: Step | Position. Students fill in each row. _Implementation note: First trace table experience; builds systematic tracking. Auto-graded by position sequence in table. CSTA: E2‑ALG‑AF‑01, E2‑ALG‑PS‑03._

Dependencies:
* T02.G2.03: Trace a text-label diagram on a number line





ID: T02.G2.05
Topic: T02 – Algorithm Diagrams
Skill: Trace a diagram with a Yes/No decision box
Description: **Student task:** Follow a text-label diagram that includes a decision box (shown as diamond shape) with Yes/No paths. Predict the result for a given condition. **Visual scenario:** Diagram: [START: x=7] → ◇Is x > 5?◇ with "Yes" → [Say "Big!"] → END, "No" → [Say "Small!"] → END. Question: "What does the character say?" **Correct answer:** "Big!" (since 7 > 5, follow Yes path). _Implementation note: Introduces diamond decision shape; builds on G1.06 Yes/No boxes with formal notation. Auto-graded by selection. CSTA: E2‑ALG‑AF‑01, E2‑ALG‑PS‑03._

Dependencies:
* T02.G1.06: Trace a diagram with a Yes/No question box
* T02.G2.03: Trace a text-label diagram on a number line





ID: T02.G2.06
Topic: T02 – Algorithm Diagrams
Skill: Debug a diagram by reordering misplaced boxes
Description: **Student task:** Look at a diagram where boxes are in the wrong order. Drag boxes to reorder them to match the target algorithm. **Visual scenario:** Target: "Get paint" → "Dip brush" → "Paint picture." Given broken diagram: [Paint picture] → [Get paint] → [Dip brush]. Students drag boxes to fix: [Get paint] → [Dip brush] → [Paint picture]. _Implementation note: Multi-step diagram debugging; reorder multiple boxes. Auto-graded by final arrangement. CSTA: E2‑ALG‑AF‑01, E2‑ALG‑PS‑03._

Dependencies:
* T02.G2.04: Build a trace table for a diagram step-by-step





ID: T02.G2.07
Topic: T02 – Algorithm Diagrams
Skill: Explore the CreatiCode workspace and run a pre-made block script
Description: **Student task:** Open CreatiCode, locate the block workspace, sprite stage, and green flag button. Run a pre-made script by clicking the green flag. **Visual scenario:** Students see CreatiCode with a simple 3-block script already built. They locate and tap: (1) block palette on left, (2) script area in middle, (3) stage on right, (4) green flag at top. Click green flag to run and watch sprite move. _Implementation note: Guided exploration; prepares for understanding blocks as executable diagrams. Auto-graded by correct hotspot selections + script execution. CSTA: E2‑ALG‑AF‑01._

Dependencies:
* T02.G2.06: Debug a diagram by reordering misplaced boxes




ID: T02.G2.08
Topic: T02 – Algorithm Diagrams
Skill: Match a text-label diagram to a block script (bridging skill)
Description: **Student task:** Look at a text-label diagram. Select which block script (shown as images of stacked blocks) implements the same algorithm. **Visual scenario:** Text diagram: [Move forward] → [Turn right] → [Move forward] → [Say hello]. Block options show 3 different block stacks. Students select the one with: move → turn right → move → say blocks matching the diagram. _Implementation note: CRITICAL BRIDGING SKILL from diagrams to blocks; shows blocks as executable versions of diagrams. Auto-graded by selection. CSTA: E2‑ALG‑AF‑01._

Dependencies:
* T02.G2.07: Identify CreatiCode workspace and run a pre-made block script
* T02.G2.03: Trace a text-label diagram on a number line


ID: T02.G2.09
Topic: T02 – Algorithm Diagrams
Skill: Tap the repeat symbol (loop arrow) and predict how many times it runs
Description: **Student task:** Look at a diagram that has a "repeat" symbol (curved arrow going back to an earlier box). Tap the repeat symbol and predict how many times the loop runs. **Visual scenario:** Diagram shows: [START] → [Jump] → [Clap] with a curved arrow labeled "×3" going from [Clap] back to [Jump] → [END]. Question: "What does the curved arrow mean?" Answer choices: (A) Do Jump-Clap 3 times, (B) Skip Jump, (C) Go backwards. **Correct answer:** (A). _Implementation note: Introduces loop notation in diagrams; precursor to repeat blocks. Auto-graded by selection. CSTA: E2‑ALG‑AF‑01._

Dependencies:
* T02.G2.04: Build a trace table for a diagram step-by-step
* T04.G2.01: Identify the repeating unit in a longer pattern


ID: T02.G2.10
Topic: T02 – Algorithm Diagrams
Skill: Trace a repeat diagram step-by-step showing each iteration
Description: **Student task:** Follow a diagram with a repeat symbol (loop arrow "×3"). Show what happens each time through the loop by filling in a simple trace strip. **Visual scenario:** Diagram: [START at step 0] → [Step forward] with curved "×3" arrow → [END]. Trace strip shows: Step 0 → Step 1 (iteration 1) → Step 2 (iteration 2) → Step 3 (iteration 3) → END. Students fill in step counts: 0, 1, 2, 3. Question: "What step number at the END?" **Answer:** 3. _Implementation note: Explicit loop iteration tracing; builds foundation for loop trace tables. Picture-based with number-line visual. Auto-graded by trace strip values. CSTA: E2‑ALG‑AF‑01, E2‑ALG‑PS‑03._

Dependencies:
* T02.G2.09: Identify a repeat symbol (loop arrow) in a diagram
* T02.G2.04: Build a trace table for a diagram step-by-step


ID: T02.G2.11
Topic: T02 – Algorithm Diagrams
Skill: Debug a diagram by adding a missing arrow connection
Description: **Student task:** Look at a diagram where boxes are disconnected—an arrow is missing between two boxes. Drag an arrow to connect the broken diagram. **Visual scenario:** Diagram shows "making a card": [fold paper] [GAP—no arrow] [draw picture] → [give to friend]. Student sees that "fold paper" and "draw picture" are not connected. Drag an arrow from "fold paper" to "draw picture" to fix the diagram. _Implementation note: Introduces arrow/connection as critical diagram element; different from wrong box content. Drag-drop arrow tool. Auto-graded by correct arrow placement. CSTA: E2‑ALG‑AF‑01, E2‑ALG‑PS‑03._

Dependencies:
* T02.G2.06: Debug a diagram by reordering misplaced boxes
* T02.GK.01: Identify arrows showing "what comes next" in a picture strip


ID: T02.G2.12
Topic: T02 – Algorithm Diagrams
Skill: Compare two diagrams and tap the one with more steps
Description: **Student task:** Look at two diagrams side by side. Count the steps in each diagram and tap the one that has more steps. Explain why one might be more detailed than the other. **Visual scenario:** Diagram A shows "making a bed": [pull up blanket] → [fluff pillow] → [done] (3 steps). Diagram B shows: [remove old sheets] → [put on fitted sheet] → [put on flat sheet] → [add blanket] → [fluff pillow] → [done] (6 steps). Question: "Which diagram has more steps? Tap it." **Answer:** Diagram B. Follow-up: "Why might someone use more steps?" **Answer:** More detail, clearer instructions. _Implementation note: Introduces diagram complexity comparison; connects to granularity concept from GK.07. Side-by-side visual comparison with counting support. Auto-graded by correct selection. CSTA: E2‑ALG‑AF‑01, E2‑ALG‑IM‑04._

Dependencies:
* T02.G2.04: Build a trace table for a diagram step-by-step
* T02.GK.07: Sort picture cards by step size (big steps vs small steps)


ID: T02.G2.13
Topic: T02 – Algorithm Diagrams
Skill: Build a diagram with a "wait for" step (introduces timing concepts)
Description: **Student task:** Create a diagram that includes a "wait for" box — a special step where you wait until something happens before continuing. **Visual scenario:** Task: "Cross the street safely." Students build: [Walk to crosswalk] → [Push button] → [WAIT FOR: light turns green] → [Look both ways] → [Cross street] → [END]. The "WAIT FOR" box is shown differently (hourglass icon, different color). Discussion: "Why can't we skip the wait step?" _Implementation note: Introduces synchronization/timing concept; precursor to "wait until" blocks and event-driven thinking. Different visual for wait box. Auto-graded by correct wait placement. CSTA: E2‑ALG‑AF‑01._

Dependencies:
* T02.G2.05: Trace a diagram with a Yes/No decision box
* T02.G1.06: Trace a diagram with a Yes/No question box


ID: T02.G2.14
Topic: T02 – Algorithm Diagrams
Skill: Compare two diagrams and explain which is clearer for a helper
Description: **Student task:** Look at two diagrams for the same task. Decide which diagram would be easier for a helper (like a robot or friend) to follow, and explain why. **Visual scenario:** Task: "Make a paper airplane." Diagram A: [Fold paper] → [Throw]. Diagram B: [Get paper] → [Fold in half longways] → [Fold corners to center] → [Fold wings down] → [Throw]. Question: "Which diagram would help a robot make a better airplane?" **Answer:** Diagram B — it has more detail! Follow-up: "When might the shorter diagram be OK?" _Implementation note: Introduces diagram quality evaluation; connects to audience awareness and appropriate detail level. Side-by-side comparison with explain prompt. Auto-graded by selection + brief explanation. CSTA: E2‑ALG‑AF‑01, E2‑ALG‑IM‑04._

Dependencies:
* T02.G2.12: Compare two diagrams and tap the one with more steps
* T02.GK.07: Sort picture cards by step size (big steps vs small steps)


---

## GRADE 3 (15 skills - added T02.G3.13 execution counting, T02.G3.14 flowchart debugging)




ID: T02.G3.00
Topic: T02 – Algorithm Diagrams
Skill: Arrange provided blocks in the order shown by a diagram
Description: **Student task:** Look at a simple 4-box diagram and arrange pre-made blocks to match the diagram order. Blocks are already provided; students only need to drag them into correct sequence. **Visual scenario:** Diagram: [set x to 0] → [move 50] → [turn 90] → [say "done"]. Four loose blocks are shown scrambled. Students drag blocks into the correct top-to-bottom order matching the diagram left-to-right. _Implementation note: Bridge between reading diagrams (G2) and building code (G3); scaffolds coding entry. Auto-graded by block arrangement. CSTA: E3-ALG-AF-01._

Dependencies:
* T02.G2.08: Match a text-label diagram to a block script (bridging skill)




ID: T02.G3.01
Topic: T02 – Algorithm Diagrams
Skill: Build and run a 4-block sequence in CreatiCode
Description: **Student task:** Build a simple 4-block sequence in CreatiCode by snapping blocks together, then run it with the green flag. **Visual scenario:** Students create: [move 50 steps] → [turn 90°] → [move 50 steps] → [say "Hello!"]. They observe blocks execute top-to-bottom, just like diagram boxes execute left-to-right. _Implementation note: First block-building task; emphasizes blocks as executable diagram boxes. Auto-graded by sprite position + message. CSTA: E3‑ALG‑AF‑01, E3‑PRO‑PF‑01._

Dependencies:
* T02.G2.08: Match a text-label diagram to a block script (bridging skill)





ID: T02.G3.02
Topic: T02 – Algorithm Diagrams
Skill: Predict the outcome of a block sequence without running it
Description: **Student task:** Look at a 5-block script WITHOUT running it. Predict what the sprite will do and where it ends up. **Visual scenario:** Script: [move 100] → [turn 90°] → [move 50] → [turn 90°] → [say "Done!"]. Grid shows starting position. Students predict: (1) sprite's final position on grid, (2) sprite says "Done!". _Implementation note: Mental tracing without execution; same skill as tracing a diagram. Auto-graded by position and message selection. CSTA: E3‑ALG‑AF‑01, E3‑ALG‑PS‑03._

Dependencies:
* T02.G3.01: Build and run a 4-block sequence in CreatiCode





ID: T02.G3.03
Topic: T02 – Algorithm Diagrams
Skill: Build a block script to implement a given algorithm
Description: **Student task:** Given a task description, create a 4–6 block script that implements the algorithm. **Visual scenario:** Task: "Make the sprite draw a short line, then say 'Done!'" Students build: [pen down] → [move 100] → [pen up] → [say "Done!"]. This is the executable version of a diagram. _Implementation note: Task specification → block implementation; auto-graded by behavior. CSTA: E3‑ALG‑AF‑01, E3‑PRO‑PF‑01._

Dependencies:
* T02.G3.02: Predict the outcome of a block sequence without running it





ID: T02.G3.04
Topic: T02 – Algorithm Diagrams
Skill: Trace a block script with one if/else decision
Description: **Student task:** Follow a block script with one if/else block. Given a starting value, trace which branch executes and predict the outcome. **Visual scenario:** Script: [if x > 50 then] → [say "Big!"] [else] → [say "Small!"]. Given: x = 30. Students trace: condition 30 > 50 is FALSE → follow "else" branch → sprite says "Small!". _Implementation note: Single if/else tracing; mirrors tracing a decision diamond in a diagram. Auto-graded by path and outcome. CSTA: E3‑ALG‑AF‑01, E3‑ALG‑PS‑03._

Dependencies:
* T02.G3.03: Build a block script to implement a given algorithm
* T02.G2.05: Trace a diagram with a Yes/No decision box





ID: T02.G3.05
Topic: T02 – Algorithm Diagrams
Skill: Build a block script with one if/else decision
Description: **Student task:** Build a block script with one if/else block to handle a simple decision. **Visual scenario:** Task: "If the sprite is touching the edge, say 'Stop!' Otherwise, move forward 10 steps." Students build: [if touching edge?] → [say "Stop!"] [else] → [move 10]. _Implementation note: First conditional building; implements a decision diagram as executable code. Auto-graded by testing both branches. CSTA: E3‑ALG‑AF‑01, E3‑PRO‑PF‑01._

Dependencies:
* T02.G3.04: Trace a block script with one if/else decision





ID: T02.G3.06
Topic: T02 – Algorithm Diagrams
Skill: Compare two block scripts for the same task
Description: **Student task:** Look at two block scripts that both accomplish the same goal. Identify which uses fewer blocks or is clearer. **Visual scenario:** Task: "Move sprite to (100, 100)." Script A: [go to x:0 y:0] → [glide to x:100 y:100] (2 blocks). Script B: [set x to 100] → [set y to 100] → [wait 1 sec] (3 blocks). Question: "Which script is simpler?" **Answer:** Script A (fewer blocks, same result). _Implementation note: Algorithm comparison; introduces efficiency thinking. Auto-graded by selection. CSTA: E3‑ALG‑IM‑04._

Dependencies:
* T02.G3.03: Build a block script to implement a given algorithm




ID: T02.G3.07
Topic: T02 – Algorithm Diagrams
Skill: Determine when an algorithm diagram needs a loop symbol
Description: **Student task:** Look at a task description and determine whether the algorithm diagram would need a repeat/loop symbol. **Visual scenario:** Task A: "Draw a square (4 equal sides)" – needs [move-turn] repeated 4×. Task B: "Say hello once" – no repetition. Question: "Which task needs a loop in its diagram?" **Answer:** Task A (same steps repeat). _Implementation note: Connects loop concept to diagram notation (repeat symbols). Auto-graded by selection. CSTA: E3‑ALG‑AF‑01._

Dependencies:
* T02.G2.09: Tap the repeat symbol (loop arrow) and predict how many times it runs
* T02.G3.03: Build a block script to implement a given algorithm




ID: T02.G3.08
Topic: T02 – Algorithm Diagrams
Skill: Trace a repeat block script and predict the final result
Description: **Student task:** Follow a block script with a "repeat N times" block. Predict what happens after all repetitions. **Visual scenario:** Script: [repeat 4] → [move 50] → [turn 90°]. Trace table: Iteration 1: move+turn, Iteration 2: move+turn, Iteration 3: move+turn, Iteration 4: move+turn. Result: sprite draws a square, ends at start. _Implementation note: First loop tracing in blocks; connects to diagram repeat symbols. Auto-graded by final position/pattern. CSTA: E3‑ALG‑AF‑01, E3‑ALG‑PS‑03._

Dependencies:
* T02.G3.07: Identify when an algorithm diagram needs a loop symbol
* T07.G2.01: Identify when to use "repeat" vs "do once"


ID: T02.G3.09
Topic: T02 – Algorithm Diagrams
Skill: Draw a simple flowchart for a block script
Description: **Student task:** Given a simple 4-5 block script, draw a matching flowchart using START/END ovals, action rectangles, and arrows. **Visual scenario:** Script: [move 50] → [turn 90°] → [say "Done!"]. Students draw: (START oval) → [move 50 rect] → [turn 90° rect] → [say "Done!" rect] → (END oval). Drag flowchart shapes and connect with arrows. _Implementation note: First flowchart creation; introduces standard symbols. Auto-graded by shape sequence and connections. CSTA: E3‑ALG‑AF‑01._

Dependencies:
* T02.G3.01: Build and run a 4-block sequence in CreatiCode
* T02.GK.03: Label START and END boxes in a picture diagram


ID: T02.G3.10
Topic: T02 – Algorithm Diagrams
Skill: Match flowchart symbols to their meanings and demonstrate understanding
Description: **Student task:** Match flowchart symbols to their meanings by dragging labels, then demonstrate understanding by answering questions about each symbol's purpose. **Visual scenario:** Show 4 symbols: (1) oval, (2) rectangle, (3) diamond, (4) arrow. Labels: "Start/End", "Process/Action", "Decision/Question", "Flow direction". Students drag: oval="Start/End", rectangle="Process", diamond="Decision", arrow="Flow". Follow-up question: "Which symbol asks a question?" **Answer:** Diamond. "When would you use a rectangle?" **Answer:** For an action step. _Implementation note: Explicit symbol vocabulary with active demonstration; foundational for flowchart literacy. Drag-drop matching + MCQ verification. Auto-graded by correct matches and answers. CSTA: E3‑ALG‑AF‑01._

Dependencies:
* T02.G3.09: Draw a simple flowchart for a block script
* T02.G2.05: Trace a diagram with a Yes/No decision box


ID: T02.G3.11
Topic: T02 – Algorithm Diagrams
Skill: Plan an algorithm using the diagram editor before building blocks
Description: **Student task:** Before coding, use the CreatiCode diagram editor to create a visual plan showing the steps of your algorithm. Include START/END ovals, action boxes, and arrows. Then build the matching blocks. **Visual scenario:** Task: "Make sprite draw a triangle." Students first create diagram in diagram editor: (START) → [pen down] → [move 100] → [turn 120] → [repeat back arrow ×3] → (END). Then build blocks to match their diagram. Compare diagram to final code. _Implementation note: Pre-coding visual planning tool; connects diagram skills to coding workflow. Auto-graded by diagram completeness + block implementation match. CSTA: E3-ALG-AF-01, E3-PRO-PF-01._

Dependencies:
* T02.G3.09: Draw a simple flowchart for a block script
* T02.G3.03: Build a block script to implement a given algorithm


ID: T02.G3.12
Topic: T02 – Algorithm Diagrams
Skill: Draw a flowchart programmatically using drawing blocks
Description: **Student task:** Use CreatiCode's drawing blocks (draw rectangle, draw oval, draw line) to create a flowchart on the stage. Program your sprite to draw START/END ovals, action rectangles, and connecting arrows. **Visual scenario:** Students build a script: [draw oval at x:-150 y:100 (START)] → [draw line from START to first action] → [draw rectangle at x:-150 y:0 (action: move 50)] → [draw line to next] → [draw rectangle at x:-150 y:-100 (action: turn 90)] → [draw oval at x:-150 y:-200 (END)]. Result: a programmatically-generated flowchart appears on stage! Compare to hand-drawn version. _Implementation note: First programmatic diagram creation; connects drawing skills to algorithm visualization. Uses draw_rectangle, draw_oval, draw_line blocks. Auto-graded by shape positions and connections. CSTA: E3-ALG-AF-01, E3-PRO-PF-01._

Dependencies:
* T02.G3.09: Draw a simple flowchart for a block script
* T02.G3.01: Build and run a 4-block sequence in CreatiCode


ID: T02.G3.13
Topic: T02 – Algorithm Diagrams
Skill: Predict how many times each block executes in a simple script
Description: **Student task:** Look at a script with a repeat block. Without running it, predict how many times each block inside and outside the loop will execute. Fill in an execution count table. **Visual scenario:** Script: [move 10] → [repeat 3] → [turn 90] → [move 20] → [say "Done"]. Execution count table: Block | Count. "move 10" = 1, "turn 90" = 3, "move 20" = 3, "say Done" = 1. Students fill in counts BEFORE running, then verify by adding print blocks or running with counter variable. _Implementation note: Mental tracing of execution frequency; builds loop understanding. Table format for organized prediction. Auto-graded by prediction accuracy. CSTA: E3‑ALG‑AF‑01, E3‑ALG‑PS‑03._

Dependencies:
* T02.G3.08: Trace a repeat block script and predict the final result
* T02.G3.02: Predict the outcome of a block sequence without running it


ID: T02.G3.14
Topic: T02 – Algorithm Diagrams
Skill: Debug a flowchart by finding the missing connection
Description: **Student task:** Look at a flowchart where one arrow/connection is missing. Find where the gap is and add the missing arrow to complete the flowchart. **Visual scenario:** Flowchart: (START) → [move 50] → [turn 90] [GAP — no arrow] [move 50] → (END). The flowchart has a broken flow between "turn 90" and the second "move 50". Students identify the gap and draw/drag an arrow to connect them. Question: "What happens if you try to follow this flowchart?" **Answer:** You get stuck at "turn 90" — don't know where to go next! _Implementation note: Flowchart integrity checking; emphasizes that every box needs incoming and outgoing connections (except START/END). Drag-drop arrow tool. Auto-graded by correct connection placement. CSTA: E3‑ALG‑AF‑01, E3‑ALG‑PS‑03._

Dependencies:
* T02.G3.09: Draw a simple flowchart for a block script
* T02.G2.11: Debug a diagram by adding a missing arrow connection


---

## GRADE 4 (16 skills - added T02.G4.12 skip counting, T02.G4.13 early exit, T02.G4.14 trace comparison)




ID: T02.G4.01
Topic: T02 – Algorithm Diagrams
Skill: Predict and trace loop variable changes in a trace table
Description: **Student task:** BEFORE running a loop script, fill in a trace table predicting variable values for each iteration. Then run the script and verify your predictions match actual output. **Visual scenario:** Script: [set count to 0] → [repeat 5] → [change count by 2]. Prediction trace table: Iteration | count: 1 | 2, 2 | 4, 3 | 6, 4 | 8, 5 | 10. Students fill predictions FIRST, then run script and add print blocks to verify. Match predictions to actual console output. _Implementation note: Prediction-first tracing builds mental model before execution; combines loop tracing with formal trace tables. Auto-graded by prediction accuracy against actual execution. CSTA: E4‑ALG‑AF‑01, E4‑ALG‑PS‑03._

Dependencies:
* T02.G3.08: Trace a repeat block script and predict the final result
* T02.G2.04: Build a trace table for a diagram step-by-step





ID: T02.G4.02
Topic: T02 – Algorithm Diagrams
Skill: Build a block script with a repeat loop for a pattern
Description: **Student task:** Create a block script using a repeat block to draw a geometric pattern. **Visual scenario:** Task: "Draw a square (4 sides, each 100 steps, turn 90° after each)." Students build: [repeat 4] → [move 100] → [turn 90°]. Result: sprite draws a square. _Implementation note: First loop building; implements repetitive algorithm. Auto-graded by drawn shape. CSTA: E4‑ALG‑AF‑01, E4‑PRO‑PF‑01._

Dependencies:
* T02.G4.01: Trace a repeat loop with variable tracking in a trace table
* T02.G3.03: Build a block script to implement a given algorithm





ID: T02.G4.03.01
Topic: T02 – Algorithm Diagrams
Skill: Trace a script with sequential if/else decisions
Description: **Student task:** Trace a block script with 2 if/else blocks that run one after another (sequential, not nested). Track which conditions are true. **Visual scenario:** Script: [if x > 50 say "Big" else say "Small"] → [if y > 50 say "High" else say "Low"]. Given: x=60, y=30. Trace: first if: 60>50=TRUE → "Big"; second if: 30>50=FALSE → "Low". Result: "Big" then "Low". _Implementation note: Sequential conditionals; each decision independent. Auto-graded by both outputs. CSTA: E4‑ALG‑AF‑01, E4‑ALG‑PS‑03._

Dependencies:
* T02.G3.05: Build a block script with one if/else decision
* T12.G3.01: Test and trace simple block-based scripts




ID: T02.G4.03.02
Topic: T02 – Algorithm Diagrams
Skill: Trace a script with nested if/else decisions
Description: **Student task:** Trace a block script where one if/else is INSIDE another if/else (nested). Track the path through nested structure. **Visual scenario:** Script: [if x > 50] → [if y > 50 say "Big & High" else say "Big & Low"] [else say "Small"]. Given: x=60, y=30. Trace: outer if: 60>50=TRUE → enter inner; inner if: 30>50=FALSE → "Big & Low". _Implementation note: Nested conditionals; requires tracking depth level. Auto-graded by final output. CSTA: E4‑ALG‑AF‑01, E4‑ALG‑PS‑03._

Dependencies:
* T02.G4.03.01: Trace a script with sequential if/else decisions





ID: T02.G4.04.01
Topic: T02 – Algorithm Diagrams
Skill: Build a script with loop followed by decision (sequential)
Description: **Student task:** Build a block script with a repeat loop FOLLOWED BY an if/else block (sequential, not nested). **Visual scenario:** Task: "Move 4 times (10 steps each), then check if you've gone far." Students build: [repeat 4] → [move 10] → [if x > 100 say "Far!" else say "Close!"]. Loop runs first, then decision checks result. _Implementation note: Sequential combination of structures. Auto-graded by position + message. CSTA: E4‑ALG‑AF‑01, E4‑PRO‑PF‑01._

Dependencies:
* T02.G4.02: Build a block script with a repeat loop for a pattern
* T02.G3.05: Build a block script with one if/else decision





ID: T02.G4.04.02
Topic: T02 – Algorithm Diagrams
Skill: Build a script with decision inside a loop (nested)
Description: **Student task:** Build a block script with an if/else block INSIDE a repeat loop (decision made each iteration). **Visual scenario:** Task: "Repeat 10 times: if touching blue, turn; otherwise move." Students build: [repeat 10] → [if touching blue? turn 90° else move 10]. Decision runs each iteration—behavior depends on environment. _Implementation note: Nested combination; decision affects each iteration. Auto-graded by final path. CSTA: E4‑ALG‑AF‑01, E4‑PRO‑PF‑01._

Dependencies:
* T02.G4.04.01: Build a script with loop followed by decision (sequential)
* T02.G4.03.02: Trace a script with nested if/else decisions





ID: T02.G4.04.03
Topic: T02 – Algorithm Diagrams
Skill: Draw a flowchart with a decision diamond
Description: **Student task:** Draw a flowchart for a block script that includes an if/else decision, using diamond shape for the decision. **Visual scenario:** Script: [if score > 10] → [say "Winner!"] [else] → [say "Try again"]. Students draw: (START) → ◇score > 10?◇ with "Yes" → [say "Winner!"] → (END), "No" → [say "Try again"] → (END). _Implementation note: Introduces diamond decision symbol in flowcharts. Auto-graded by shape types and connections. CSTA: E4‑ALG‑AF‑01._

Dependencies:
* T02.G3.09: Draw a simple flowchart for a block script
* T02.G3.05: Build a block script with one if/else decision





ID: T02.G4.05.01
Topic: T02 – Algorithm Diagrams
Skill: Locate and use the print block to display a message in console
Description: **Student task:** Find the "print [MESSAGE] in [console]" block in the Operators category. Add it to a script and run to see output in the console panel. **Visual scenario:** Students locate the print block, add it with message "Hello from console!", run the script, and find the Console panel (click Console tab at bottom). See "Hello from console!" appear. Verify you can clear and rerun. _Implementation note: Tool discovery—console panel orientation is critical foundation. Auto-graded by console output. CSTA: E4‑PRO‑TR‑03._

Dependencies:
* T02.G4.01: Predict and trace loop variable changes in a trace table
* T12.G3.01: Test and trace simple block-based scripts


ID: T02.G4.05.02
Topic: T02 – Algorithm Diagrams
Skill: Add strategic print blocks inside a loop to trace variable changes
Description: **Student task:** Add print blocks at strategic points inside a repeat loop to display variable changes. Compare console output to trace table predictions. **Visual scenario:** Script: [set count to 0] → [repeat 5] → [change count by 3, print "count = " + count]. Console shows: count = 3, count = 6, count = 9, count = 12, count = 15. Students verify their trace table predictions match console output. Identify where to place prints: AFTER the variable changes, not before. _Implementation note: Strategic print placement; builds debugging intuition. Auto-graded by trace table matching console output. CSTA: E4‑ALG‑AF‑01, E4‑PRO‑TR‑03._

Dependencies:
* T02.G4.05.01: Locate and use the print block to display a message in console






ID: T02.G4.06
Topic: T02 – Algorithm Diagrams
Skill: Debug a script by adding print blocks to find the error
Description: **Student task:** Given a buggy script, add "print" blocks to display variable values. Use console output to identify and fix the error. **Visual scenario:** Buggy script supposed to count 0-10 by 2s, but outputs 2,4,6,8,10,12. Students add print blocks, discover initialization error (starts at 2 not 0). Fix: change "set x to 2" to "set x to 0". _Implementation note: Print-based debugging workflow. Auto-graded by corrected script behavior. CSTA: E4‑ALG‑AF‑01, E4‑PRO‑TR‑03._

Dependencies:
* T02.G4.05.02: Add strategic print blocks inside a loop to trace variable changes






ID: T02.G4.07
Topic: T02 – Algorithm Diagrams
Skill: Draw a flowchart with a loop symbol
Description: **Student task:** Draw a flowchart for a block script with a repeat loop, using proper loop notation (back-arrow or loop box). **Visual scenario:** Script: [repeat 4] → [move 50] → [turn 90°]. Students draw: (START) → [Loop: 4 times] → [move 50] → [turn 90°] → (back to loop check) → (END when done). _Implementation note: Introduces loop representation in flowcharts. Auto-graded by structure and connections. CSTA: E4‑ALG‑AF‑01._

Dependencies:
* T02.G4.04.03: Draw a flowchart with a decision diamond
* T02.G4.02: Build a block script with a repeat loop for a pattern


ID: T02.G4.08
Topic: T02 – Algorithm Diagrams
Skill: Display algorithm state using a table variable monitor on stage
Description: **Student task:** Create a table variable to display algorithm state visually on stage. Add columns for "Step", "Variable", and "Value". Update the table during loop execution so viewers can watch the algorithm progress. **Visual scenario:** Counting algorithm: table shows rows like [Step 1 | count | 2], [Step 2 | count | 4], etc. Students use "add row to table [table]" block inside the loop to log each state change. Watch the table grow as the algorithm runs—visual trace on stage! _Implementation note: Visual algorithm tracing using CreatiCode table variables; connects to T10 data skills. Auto-graded by table content accuracy. CSTA: E4-ALG-AF-01, E4-ALG-PS-03._

Dependencies:
* T02.G4.05.02: Add strategic print blocks inside a loop to trace variable changes
* T10.G3.01: Create a table variable with named columns


ID: T02.G4.09
Topic: T02 – Algorithm Diagrams
Skill: Draw a data flow diagram showing input, process, and output
Description: **Student task:** Create a data flow diagram that shows where data comes from (input), what happens to it (process), and where it goes (output). Use rounded rectangles for processes, arrows for data flow. **Visual scenario:** Task: "Calculate a tip." Students draw: [User enters bill amount] → [Calculate 15% of bill] → [Display tip amount]. Data flows along arrows: "billAmount" flows into process, "tipAmount" flows out. Students label each arrow with the data name. _Implementation note: Introduces data flow notation; different from control flow (flowcharts). Foundation for system design. Auto-graded by correct input/process/output structure. CSTA: E4‑ALG‑AF‑01._

Dependencies:
* T02.G4.04.03: Draw a flowchart with a decision diamond
* T02.G4.01: Predict and trace loop variable changes in a trace table


ID: T02.G4.10
Topic: T02 – Algorithm Diagrams
Skill: Build a decision table for a multi-condition algorithm
Description: **Student task:** Create a decision table that lists all combinations of conditions and their corresponding actions. Use the table to verify your algorithm handles all cases. **Visual scenario:** Task: "What to wear based on weather." Conditions: Is it cold? (Y/N), Is it raining? (Y/N). Decision table with 4 rows: Cold+Rain→jacket+umbrella, Cold+NoRain→jacket, NotCold+Rain→umbrella, NotCold+NoRain→t-shirt. Students fill in table, then build matching if/else blocks. Verify all 4 combinations work. _Implementation note: Decision tables as algorithm planning tool; alternative to flowcharts for multi-condition logic. Table variable display on stage. Auto-graded by table completeness + code matching all cases. CSTA: E4‑ALG‑AF‑01, E4‑ALG‑PS‑03._

Dependencies:
* T02.G4.03.02: Trace a script with nested if/else decisions
* T02.G4.08: Display algorithm state using a table variable monitor on stage


ID: T02.G4.11
Topic: T02 – Algorithm Diagrams
Skill: Create an animated flowchart that highlights current step during execution
Description: **Student task:** Build a visual flowchart on stage using drawing blocks. As your algorithm runs, highlight the current step by changing its color. Create a "live" flowchart that shows execution progress. **Visual scenario:** Students draw a 4-step flowchart. Script runs: draw all boxes in gray → start algorithm → change box 1 to green (current) → execute step 1 → change box 1 back to gray, box 2 to green → continue. Viewers see the flowchart "light up" step by step! Add wait blocks for visibility. _Implementation note: Self-illustrating algorithm; advanced diagram-code integration. Uses draw_rectangle with color changes. Auto-graded by correct highlighting sequence matching execution. CSTA: E4-ALG-AF-01, E4-PRO-PF-01._

Dependencies:
* T02.G3.12: Draw a flowchart programmatically using drawing blocks
* T02.G4.05.02: Add strategic print blocks inside a loop to trace variable changes


ID: T02.G4.12
Topic: T02 – Algorithm Diagrams
Skill: Trace a counting algorithm that skips by 2s, 3s, or 5s
Description: **Student task:** Trace an algorithm that counts by a skip value (2, 3, or 5). Fill in a trace table predicting each value, then verify with console output. **Visual scenario:** Script: [set count to 0] → [repeat 5] → [change count by 3] → [print count]. Trace table: Iteration | count: 1|3, 2|6, 3|9, 4|12, 5|15. Students predict all values first, then run to verify. Follow-up: "What if we changed 'by 3' to 'by 5'?" Students predict new pattern without running. _Implementation note: Pattern recognition in counting; connects to math skip counting and prepares for multiplication/modulo thinking. Auto-graded by trace table accuracy + prediction of modified pattern. CSTA: E4‑ALG‑AF‑01, E4‑ALG‑PS‑03._

Dependencies:
* T02.G4.01: Predict and trace loop variable changes in a trace table
* T02.G4.05.02: Add strategic print blocks inside a loop to trace variable changes


ID: T02.G4.13
Topic: T02 – Algorithm Diagrams
Skill: Build a flowchart showing algorithm with early exit condition
Description: **Student task:** Create a flowchart for an algorithm that might exit early — before all iterations complete. Show the exit path clearly with a different-colored arrow. **Visual scenario:** Task: "Find the first even number in a list." Flowchart: (START) → [set i to 1] → (Loop) → ◇Is list[i] even?◇ → Yes → [FOUND! Exit early] → (END). No → [i = i + 1] → ◇i > list length?◇ → Yes → [Not found] → (END). No → (back to Loop). Highlight the "Yes, found" path in green as the early exit. Students draw both the early exit path AND the "checked everything" path. _Implementation note: Early termination concept in flowcharts; essential for search algorithm understanding. Different visual treatment for exit paths. Auto-graded by correct early exit structure. CSTA: E4‑ALG‑AF‑01._

Dependencies:
* T02.G4.04.03: Draw a flowchart with a decision diamond
* T02.G4.07: Draw a flowchart with a loop symbol


ID: T02.G4.14
Topic: T02 – Algorithm Diagrams
Skill: Compare trace tables from two different algorithm approaches
Description: **Student task:** Given two different algorithms that solve the same problem, create trace tables for both. Compare the tables to understand how the algorithms differ in their approach and number of steps. **Visual scenario:** Task: "Sum numbers 1 to 4." Algorithm A (loop): [sum=0] → [repeat i from 1 to 4] → [sum += i]. Trace: 1,3,6,10 (4 iterations). Algorithm B (formula): [sum = 4 × 5 / 2]. Trace: 10 (1 step). Students create both trace tables and answer: "Which uses more steps?" "Which is easier to understand?" "Which would you use for summing 1 to 1000?" _Implementation note: Algorithm comparison through trace analysis; introduces efficiency thinking. Side-by-side trace tables. Auto-graded by correct traces + comparison insights. CSTA: E4‑ALG‑AF‑01, E4‑ALG‑IM‑04._

Dependencies:
* T02.G4.01: Predict and trace loop variable changes in a trace table
* T02.G3.06: Compare two block scripts for the same task


---

## GRADE 5 (14 skills - added T02.G5.12 swap, T02.G5.13 bubble sort, T02.G5.14 validation)




ID: T02.G5.01
Topic: T02 – Algorithm Diagrams
Skill: Trace nested loops using print blocks and a trace table
Description: **Student task:** Trace a script with nested repeat blocks by adding print blocks inside both loops. Record console output in a trace table showing outer and inner loop iterations. **Visual scenario:** Script: [repeat 3 (outer)] → [repeat 2 (inner)] → [print "outer: " + i + " inner: " + j]. Trace table: outer=1,inner=1 | outer=1,inner=2 | outer=2,inner=1 | outer=2,inner=2 | outer=3,inner=1 | outer=3,inner=2. _Implementation note: Multi-level loop tracing. Auto-graded by trace table accuracy. CSTA: E5‑ALG‑AF‑01, E5‑ALG‑PS‑03._

Dependencies:
* T02.G4.05.02: Add strategic print blocks inside a loop to trace variable changes
* T02.G4.07: Draw a flowchart with a loop symbol





ID: T02.G5.02
Topic: T02 – Algorithm Diagrams
Skill: Build a nested loop script to create a 2D pattern
Description: **Student task:** Create a script using nested repeat blocks to generate a 2D grid pattern (outer loop for rows, inner loop for columns). **Visual scenario:** Task: "Create a 4×3 grid of stamps." Students build: [repeat 3 (rows)] → [repeat 4 (cols)] → [stamp, move right 50], [move to next row]. Result: 3 rows of 4 stamps each. _Implementation note: Nested loop construction for 2D patterns. Auto-graded by visual grid output. CSTA: E5‑ALG‑AF‑01, E5‑PRO‑PF‑01._

Dependencies:
* T02.G5.01: Trace nested loops using print blocks and a trace table





ID: T02.G5.03
Topic: T02 – Algorithm Diagrams
Skill: Trace multiple variables including accumulators in custom trace tables
Description: **Student task:** Trace a script with multiple changing values, designing your own trace table format. Include accumulator patterns (running totals, growing values). Predict values before running, then verify with print output. **Visual scenario:** Script: running total adds position each step. Student designs table: Iteration | x | total | change. Predict: 1|50|50|+50, 2|100|150|+100, 3|150|300|+150. Verify with console output. Tracks both regular variables AND accumulators. _Implementation note: Combines multi-variable tracing with student-designed tables and accumulator patterns. Auto-graded by prediction accuracy. CSTA: E5-ALG-AF-01, E5-ALG-PS-03._

Dependencies:
* T02.G4.05.02: Add strategic print blocks inside a loop to trace variable changes
* T09.G5.01: Use multiple variables together in a single expression


ID: T02.G5.04
Topic: T02 – Algorithm Diagrams
Skill: Trace an algorithm with multiple exit points and predict which exit is taken
Description: **Student task:** Trace a script that has multiple possible exit points (early returns, different stop conditions). Predict which exit path executes for a given input. **Visual scenario:** Search algorithm with 3 exits: (1) item found → return position, (2) end of list → return "not found", (3) invalid input → return "error". Students trace with inputs: [5,3,8], target=3 → exits at position 2 (found). [5,3,8], target=9 → exits at end (not found). [], target=5 → exits immediately (error). Draw flowchart showing all exit paths. _Implementation note: Multiple exit point analysis; critical for understanding algorithm termination. Auto-graded by correct exit prediction. CSTA: E5‑ALG‑AF‑01, E5‑ALG‑PS‑03._

Dependencies:
* T02.G5.03: Trace multiple variables including accumulators in custom trace tables
* T02.G4.04.02: Build a script with decision inside a loop (nested)







ID: T02.G5.05
Topic: T02 – Algorithm Diagrams
Skill: Analyze two algorithms by counting operations to determine efficiency
Description: **Student task:** Compare two block scripts that solve the same problem. Count blocks and trace execution steps to identify which is more efficient. **Visual scenario:** Task: "Move sprite 200 steps." Algorithm A: [repeat 4] → [move 50] (4 iterations). Algorithm B: [move 200] (1 operation). Students count: A=4 move operations, B=1 move operation. B is more efficient. _Implementation note: Efficiency analysis by operation counting. Auto-graded by efficiency identification. CSTA: E5‑ALG‑IM‑04._

Dependencies:
* T02.G3.06: Compare two block scripts for the same task
* T02.G5.01: Trace nested loops using print blocks and a trace table





ID: T02.G5.06
Topic: T02 – Algorithm Diagrams
Skill: Optimize an algorithm by removing redundant blocks
Description: **Student task:** Given a working script with unnecessary blocks, identify and remove redundant operations while keeping the same output behavior. **Visual scenario:** Script with redundant steps: [move 50] → [move -50] → [move 50] → [turn 90°]. Redundant: first two moves cancel out. Optimized: [move 50] → [turn 90°]. Students identify and remove waste. _Implementation note: Algorithm optimization; same behavior, fewer blocks. Auto-graded by output matching + block count reduction. CSTA: E5‑ALG‑IM‑04._

Dependencies:
* T02.G5.05: Compare two algorithms by counting operations


ID: T02.G5.07
Topic: T02 – Algorithm Diagrams
Skill: Draw a flowchart with nested structures
Description: **Student task:** Draw a flowchart for a block script that has a loop containing a decision (or vice versa). Show proper nesting in the diagram. **Visual scenario:** Script: [repeat 5] → [if touching edge, turn 180°, else move 10]. Flowchart shows: loop box containing a decision diamond inside, with both branches returning to loop check. _Implementation note: Advanced flowchart with nested control structures. Auto-graded by structure and nesting accuracy. CSTA: E5‑ALG‑AF‑01._

Dependencies:
* T02.G4.07: Draw a flowchart with a loop symbol
* T02.G4.04.02: Build a script with decision inside a loop (nested)


ID: T02.G5.08
Topic: T02 – Algorithm Diagrams
Skill: Convert a flowchart to a block script
Description: **Student task:** Given a flowchart diagram, build the equivalent block script in CreatiCode. **Visual scenario:** Flowchart shows: (START) → ◇x > 0?◇ → "Yes" → [move x] → (END), "No" → [turn 180°] → (END). Students build: [if x > 0] → [move x] [else] → [turn 180°]. _Implementation note: Flowchart-to-code translation. Auto-graded by script behavior matching flowchart logic. CSTA: E5‑ALG‑AF‑01, E5‑PRO‑PF‑01._

Dependencies:
* T02.G5.07: Draw a flowchart with nested structures
* T02.G4.04.02: Build a script with decision inside a loop (nested)


ID: T02.G5.09
Topic: T02 – Algorithm Diagrams
Skill: Build an interactive algorithm stepper using button and label widgets
Description: **Student task:** Create an interactive algorithm visualization using widgets: a "Step" button that executes one algorithm step per click, a label widget showing current state, and a "Reset" button. **Visual scenario:** Sorting visualizer: 5 numbers displayed. Click "Step" button → one comparison happens, label shows "Comparing 5 and 3", swapped elements highlight. Click again → next comparison. Students control algorithm pace and observe each step. _Implementation note: Widget-based algorithm stepper; combines UI skills (T15) with algorithm tracing. Auto-graded by correct step-by-step behavior. CSTA: E5-ALG-AF-01, E5-PRO-PF-01._

Dependencies:
* T02.G5.03: Trace multiple variables including accumulators in custom trace tables
* T15.G4.01: Add a button widget to the stage


ID: T02.G5.10
Topic: T02 – Algorithm Diagrams
Skill: Export trace table data to a stage display for visual debugging
Description: **Student task:** Build a trace table during algorithm execution and display it on stage using table variable monitor. Add a "Show Trace" button that reveals the complete execution history. **Visual scenario:** After running a search algorithm, click "Show Trace" button. Table appears on stage showing: [Step 1 | index=1 | value=5 | not match], [Step 2 | index=2 | value=12 | FOUND!]. Students can scroll through trace history. _Implementation note: Persistent visual trace for algorithm analysis. Auto-graded by trace table content + display functionality. CSTA: E5-ALG-AF-01, E5-PRO-TR-03._

Dependencies:
* T02.G5.03: Trace multiple variables including accumulators in custom trace tables
* T02.G4.08: Display algorithm state using a table variable monitor on stage


ID: T02.G5.11
Topic: T02 – Algorithm Diagrams
Skill: Design a flowchart for error handling with try/catch patterns
Description: **Student task:** Draw a flowchart that includes error handling paths. Show what happens when things go right AND what happens when errors occur. Use a special "error path" notation. **Visual scenario:** Task: "Load a file and display contents." Flowchart: START → [Try: Open file] → ◇Success?◇ → Yes → [Read contents] → [Display on stage] → END. No → [Error path: Show "File not found"] → [Ask user to try again] → (back to Open file). Students draw both the "happy path" and the error recovery path. Color-code error paths in red. _Implementation note: Error handling in algorithm design; critical for robust programs. Introduces try/catch thinking at diagram level. Auto-graded by correct error path structure. CSTA: E5-ALG-AF-01, E5-PRO-TR-03._

Dependencies:
* T02.G5.07: Draw a flowchart with nested structures
* T02.G5.04: Trace an algorithm with multiple exit points and predict which exit is taken


ID: T02.G5.12
Topic: T02 – Algorithm Diagrams
Skill: Trace a swap algorithm exchanging two values
Description: **Student task:** Trace an algorithm that swaps the values of two variables using a temporary variable. Track all three variables (a, b, temp) in a trace table, showing the state after each step. **Visual scenario:** Initial: a=5, b=8, temp=?. Algorithm: [temp = a] → [a = b] → [b = temp]. Trace table: Step | a | b | temp: Start|5|8|?, After step 1|5|8|5, After step 2|8|8|5, After step 3|8|5|5. Final: a=8, b=5 (swapped!). Students fill in trace table and verify: "Why do we need the temp variable?" _Implementation note: Classic swap pattern; foundational for sorting algorithms. Three-variable tracing. Auto-graded by trace table accuracy + explanation of temp necessity. CSTA: E5‑ALG‑AF‑01, E5‑ALG‑PS‑03._

Dependencies:
* T02.G5.03: Trace multiple variables including accumulators in custom trace tables
* T02.G4.05.02: Add strategic print blocks inside a loop to trace variable changes


ID: T02.G5.13
Topic: T02 – Algorithm Diagrams
Skill: Build and trace a bubble sort visualization for 4 elements
Description: **Student task:** Create a visual representation of bubble sort on 4 numbers. Show each comparison, swap decision, and the state after each pass. Build a simple animation or trace table showing the sorting process. **Visual scenario:** List: [4, 2, 7, 1]. Pass 1: Compare 4-2 → swap → [2,4,7,1]. Compare 4-7 → no swap. Compare 7-1 → swap → [2,4,1,7]. Pass 2: [2,4,1,7] → ... Students create trace showing: Pass | Comparisons | Swaps | Result. Or build animated sprites that move and swap positions. Identify: "After each pass, what's guaranteed about the rightmost element?" _Implementation note: First sorting algorithm visualization; bubble sort chosen for simplicity. Can use sprites as visual elements or pure trace tables. Auto-graded by correct intermediate states. CSTA: E5‑ALG‑AF‑01, E5‑ALG‑PS‑03._

Dependencies:
* T02.G5.12: Trace a swap algorithm exchanging two values
* T02.G5.01: Trace nested loops using print blocks and a trace table


ID: T02.G5.14
Topic: T02 – Algorithm Diagrams
Skill: Design an algorithm diagram showing data validation steps
Description: **Student task:** Create a flowchart that validates input data before processing it. Include checks for: empty input, wrong type, out-of-range values. Show error handling for each invalid case. **Visual scenario:** Task: "Get a valid age (number between 0-120)." Flowchart: (START) → [Get input] → ◇Is empty?◇ → Yes → [Show "Please enter a number"] → (back to Get input). No → ◇Is a number?◇ → No → [Show "That's not a number!"] → (back). Yes → ◇Is 0-120?◇ → No → [Show "Age must be 0-120"] → (back). Yes → [Use valid age] → (END). Students draw the multi-check validation flow with specific error messages. _Implementation note: Input validation pattern; critical for robust programs. Shows multiple decision points with loops back. Auto-graded by correct validation sequence + error handling. CSTA: E5‑ALG‑AF‑01, E5‑PRO‑TR‑03._

Dependencies:
* T02.G5.07: Draw a flowchart with nested structures
* T02.G5.11: Design a flowchart for error handling with try/catch patterns


---

## GRADE 6 (17 skills - added T02.G6.14 selection sort, T02.G6.15 multi-source)




ID: T02.G6.00
Topic: T02 – Algorithm Diagrams
Skill: Classify algorithms into families: search, sort, accumulate, transform
Description: **Student task:** Given 4-5 code snippets, classify each into an algorithm family: Search (find item), Sort (arrange order), Accumulate (combine values), Transform (change each item). Explain your classification. **Visual scenario:** Snippet A: loops finding maximum → "Accumulate" (combines values to find result). Snippet B: compares adjacent items and swaps → "Sort". Snippet C: looks for target value → "Search". Snippet D: doubles each item → "Transform". Match each to its family and explain why. _Implementation note: Algorithm pattern vocabulary; foundational for G7 pattern recognition. Auto-graded by correct classification + brief explanation. CSTA: E6-ALG-AF-01._

Dependencies:
* T02.G5.05: Analyze two algorithms by counting operations to determine efficiency
* T02.G5.03: Trace multiple variables including accumulators in custom trace tables


ID: T02.G6.01.01
Topic: T02 – Algorithm Diagrams
Skill: Find and use the pseudocode generation block
Description: **Student task:** Locate the "get scripts for all blocks from sprite [SPRITE] into list [LIST]" block in the Data category. Add it to your script and run it to generate pseudocode. Confirm the list contains text. **Visual scenario:** Students find the block in Data palette, connect it to a simple 3-block script, and run. They see item 1 of the list contains text description of their code. _Implementation note: Tool discovery skill. Auto-graded by successful block execution and list populated. CSTA: E6-ALG-AF-01._

Dependencies:
* T02.G5.08: Convert a flowchart to a block script


ID: T02.G6.01.02
Topic: T02 – Algorithm Diagrams
Skill: Read and interpret generated pseudocode text
Description: **Student task:** After generating pseudocode, read item 1 of the list and identify how each block translates to text. Match phrases in pseudocode back to their original blocks. **Visual scenario:** Script: [move 50] → [turn 90] → [say "Hello"]. Generated pseudocode: "move 50 steps, turn 90 degrees, say Hello". Students match each phrase: "move 50 steps" ↔ [move 50], "turn 90 degrees" ↔ [turn 90], etc. _Implementation note: Comprehension of generated pseudocode. Auto-graded by correct matching. CSTA: E6-ALG-AF-01._

Dependencies:
* T02.G6.01.01: Find and use the pseudocode generation block





ID: T02.G6.02
Topic: T02 – Algorithm Diagrams
Skill: Match block structures to their pseudocode representation
Description: **Student task:** Build scripts with different structures (sequence, loop, if/else), generate pseudocode for each, and identify how each structure appears in text form. **Visual scenario:** Students build 3 scripts: (1) sequence only, (2) with loop, (3) with if/else. Generate pseudocode for each. Match: "if...then...else" appears for conditionals, "repeat N times" for loops. _Implementation note: Structure recognition in pseudocode. Auto-graded by correct structure-to-text matching. CSTA: E6‑ALG‑AF‑01._

Dependencies:
* T02.G6.01.02: Read and interpret generated pseudocode text





ID: T02.G6.03
Topic: T02 – Algorithm Diagrams
Skill: Analyze representation differences between block script and generated pseudocode
Description: **Student task:** Compare a block script to its generated pseudocode. Identify what information is preserved vs. lost in translation. **Visual scenario:** Script uses specific block names; pseudocode uses generic terms. Script: [glide 1 secs to x:100 y:100]. Pseudocode: "glide to position (100,100) over 1 second". Students note: exact block name differs, but meaning preserved. _Implementation note: Critical analysis of representation differences. Auto-graded by correct identification. CSTA: E6‑ALG‑AF‑01._

Dependencies:
* T02.G6.02: Match block structures to their pseudocode representation





ID: T02.G6.04
Topic: T02 – Algorithm Diagrams
Skill: Write pseudocode first, then implement as blocks
Description: **Student task:** Write pseudocode on paper for a given task BEFORE coding. Then build the matching block script. Compare your pseudocode to the generated pseudocode. **Visual scenario:** Task: "Draw a triangle." Student writes: "repeat 3: move 100, turn 120". Then builds: [repeat 3] → [move 100] → [turn 120°]. Generate pseudocode to verify match. _Implementation note: Pseudocode-first planning workflow. Auto-graded by script behavior + pseudocode similarity. CSTA: E6‑ALG‑AF‑01, E6‑PRO‑PF‑01._

Dependencies:
* T02.G6.03: Identify differences between block script and its pseudocode





ID: T02.G6.05
Topic: T02 – Algorithm Diagrams
Skill: Debug by comparing actual pseudocode to intended algorithm
Description: **Student task:** Generate pseudocode from a buggy script. Compare to the intended algorithm description. Identify the mismatch and fix the blocks. **Visual scenario:** Task was "draw a square" but sprite draws a line. Generate pseudocode, see "repeat 4: move 100" (missing turn!). Compare to correct: "repeat 4: move 100, turn 90". Fix: add [turn 90°] inside loop. _Implementation note: Pseudocode-based debugging. Auto-graded by corrected script output. CSTA: E6‑ALG‑AF‑01, E6‑PRO‑TR‑03._

Dependencies:
* T02.G6.03: Identify differences between block script and its pseudocode





ID: T02.G6.06
Topic: T02 – Algorithm Diagrams
Skill: Trace a list-processing algorithm with print blocks
Description: **Student task:** Trace a script that processes a list (e.g., finding the largest value). Add print blocks to show each item examined and how the result variable updates. **Visual scenario:** Script: [set max to item 1] → [repeat for each item] → [if item > max, set max to item, print "new max: " + max]. Console shows progression: "checking 5... checking 12, new max: 12... checking 8..." _Implementation note: List traversal tracing. Auto-graded by trace accuracy. CSTA: E6‑ALG‑AF‑01, E6‑ALG‑PS‑03._

Dependencies:
* T02.G5.03: Trace multiple variables including accumulators in custom trace tables
* T10.G5.03: Work with list data structures





ID: T02.G6.07.01
Topic: T02 – Algorithm Diagrams
Skill: Build a find-maximum algorithm with trace output
Description: **Student task:** Create a script that finds the maximum value in a list. Track the "max so far" variable and print when it changes. **Visual scenario:** List: [5, 12, 8, 3, 15, 7]. Students build: [set max to item 1] → [repeat for items 2-6] → [if item > max, set max to item, print "new max found: " + max]. Console: "new max: 12... new max: 15". Final max = 15. _Implementation note: Classic find-max algorithm with tracing. Auto-graded by correct max + trace log. CSTA: E6‑ALG‑AF‑01, E6‑PRO‑PF‑01._

Dependencies:
* T02.G6.06: Trace a list-processing algorithm with print blocks


ID: T02.G6.07.02
Topic: T02 – Algorithm Diagrams
Skill: Adapt find-maximum to find-minimum and trace the difference
Description: **Student task:** Modify your find-maximum algorithm to find the minimum value instead. Trace both algorithms on the same list and compare their behavior. **Visual scenario:** List: [5, 12, 8, 3, 15, 7]. Find-max trace: starts 5, updates to 12, updates to 15. Find-min trace: starts 5, updates to 3, done. Students identify: (1) only the comparison operator changes (> becomes <), (2) update patterns differ. Question: "What's the minimum change needed to convert max to min?" **Answer:** Change > to <. _Implementation note: Algorithm adaptation skill; shows how small changes create different behaviors. Auto-graded by correct min + comparison to max trace. CSTA: E6‑ALG‑AF‑01, E6‑ALG‑IM‑04._

Dependencies:
* T02.G6.07.01: Build a find-maximum algorithm with trace output




ID: T02.G6.08
Topic: T02 – Algorithm Diagrams
Skill: Test an algorithm with normal, edge, and boundary inputs
Description: **Student task:** Test your find-max algorithm with different categories of inputs. Document results for each category. **Visual scenario:** Test categories: (1) Normal: [5, 12, 8] → max=12 ✓. (2) Edge - empty list: [] → should handle gracefully. (3) Edge - one item: [7] → max=7 ✓. (4) Boundary: all same [5,5,5] → max=5 ✓. Students test each and record pass/fail. _Implementation note: Systematic testing categories. Auto-graded by correct handling of all cases. CSTA: E6‑ALG‑AF‑01, E6‑PRO‑TR‑03._

Dependencies:
* T02.G6.07.02: Adapt find-maximum to find-minimum and trace the difference


ID: T02.G6.09
Topic: T02 – Algorithm Diagrams
Skill: Convert a flowchart diagram directly to pseudocode text
Description: **Student task:** Given a flowchart with sequence, decision, and loop structures, write equivalent pseudocode that captures the same logic. **Visual scenario:** Flowchart shows: (START) → [set sum to 0] → [repeat 5 times] → [add i to sum] → (loop back) → ◇sum > 10?◇ → "Yes" → [print "Big"] → (END), "No" → [print "Small"] → (END). Students write: "SET sum TO 0; FOR i FROM 1 TO 5: sum = sum + i; IF sum > 10 THEN PRINT 'Big' ELSE PRINT 'Small'". _Implementation note: Bridges visual flowchart to text pseudocode; critical translation skill. Auto-graded by pseudocode structure matching flowchart logic. CSTA: E6‑ALG‑AF‑01._

Dependencies:
* T02.G5.07: Draw a flowchart with nested structures
* T02.G6.02: Match block structures to their pseudocode representation


ID: T02.G6.10
Topic: T02 – Algorithm Diagrams
Skill: Create animated algorithm visualization using sprite movements
Description: **Student task:** Build an animated visualization where sprites physically demonstrate algorithm behavior. Create sprite clones or multiple sprites that move, change color, or swap positions to show algorithm steps. **Visual scenario:** Bubble sort visualization: 5 "bar" sprites of different heights. Each comparison step: two bars glow yellow, if out of order they slide and swap positions. Animation continues until sorted (all bars in ascending order left to right). Students see sorting happen step-by-step visually. _Implementation note: Animated algorithm demonstration; advanced visual tracing. Auto-graded by correct final state + animation sequence. CSTA: E6-ALG-AF-01, E6-PRO-PF-01._

Dependencies:
* T02.G6.06: Trace a list-processing algorithm with print blocks
* T06.G5.02: Broadcast a message and wait for all receivers to finish


ID: T02.G6.11
Topic: T02 – Algorithm Diagrams
Skill: Design a flowchart template for reuse across similar problems
Description: **Student task:** Create a reusable flowchart template that can be adapted for multiple similar problems. Identify which parts are fixed (structure) and which are variable (can be customized). **Visual scenario:** Template: "Process each item in a collection." Fixed structure: START → [Initialize] → [Loop through items] → ◇More items?◇ → Yes → [Process item] → (back to loop) → No → [Finalize] → END. Variable slots marked: "Initialize what?", "Process how?", "Finalize how?". Students apply template to 2 problems: (1) find sum, (2) count matches. Same structure, different slot values. _Implementation note: Template-based design thinking; introduces abstraction over algorithm patterns. Auto-graded by correct template application. CSTA: E6-ALG-AF-01, E6-ALG-IM-04._

Dependencies:
* T02.G6.09: Convert a flowchart diagram directly to pseudocode text
* T02.G6.00: Classify algorithms into families: search, sort, accumulate, transform


ID: T02.G6.12
Topic: T02 – Algorithm Diagrams
Skill: Draw a recursive algorithm diagram showing call stack
Description: **Student task:** Create a diagram that visualizes a recursive algorithm. Show the "call stack" as nested boxes or a vertical stack, with each recursive call as a new layer. Draw arrows showing how values pass down and results return up. **Visual scenario:** Task: "Diagram for factorial(4)." Students draw: [factorial(4)] calls → [factorial(3)] calls → [factorial(2)] calls → [factorial(1)] returns 1 → returns 2 → returns 6 → returns 24. Stack visualization shows 4 layers deep. Label each layer with: input value, calculation, return value. Show "going down" (calls) and "coming back up" (returns) phases. _Implementation note: Recursive call visualization; critical for understanding recursion. Uses either nested boxes or vertical stack notation. Auto-graded by correct call sequence and return values. CSTA: E6-ALG-AF-01, E6-ALG-PS-03._

Dependencies:
* T02.G6.09: Convert a flowchart diagram directly to pseudocode text
* T02.G5.07: Draw a flowchart with nested structures


ID: T02.G6.13
Topic: T02 – Algorithm Diagrams
Skill: Build an interactive flowchart editor using sprites and clicks
Description: **Student task:** Create a simple flowchart editor where users can click to place flowchart symbols on the stage, then click to connect them. Use sprites for symbols and click detection for user interaction. **Visual scenario:** Students build: (1) Toolbar with symbol sprites (rectangle, diamond, oval, arrow), (2) When user clicks a symbol, it creates a clone at the mouse position, (3) When user clicks two symbols in sequence, draw a line connecting them. Users can build their own flowcharts! Add a "Clear" button to reset. _Implementation note: Advanced project combining sprites, cloning, click detection, and drawing. Introduces tool-building mindset. Auto-graded by editor functionality: can create symbols + can connect them. CSTA: E6-PRO-PF-01, E6-ALG-AF-01._

Dependencies:
* T02.G6.10: Create animated algorithm visualization using sprite movements
* T02.G4.11: Create an animated flowchart that highlights current step during execution


ID: T02.G6.14
Topic: T02 – Algorithm Diagrams
Skill: Trace a selection sort algorithm showing minimum-finding passes
Description: **Student task:** Trace a selection sort algorithm, focusing on how each pass finds the minimum of the unsorted portion and swaps it into place. Create a detailed trace showing: which elements are compared, which minimum is found, and the list state after each pass. **Visual scenario:** List: [64, 25, 12, 22]. Pass 1: Find min of [64,25,12,22] → 12 at index 2. Swap with index 0 → [12,25,64,22]. Pass 2: Find min of [25,64,22] → 22 at index 3. Swap with index 1 → [12,22,64,25]. Pass 3: Find min of [64,25] → 25 at index 3. Swap with index 2 → [12,22,25,64]. Students trace each pass showing: Pass | Unsorted portion | Min found | Swap | Result. Compare to bubble sort: "Which checks fewer elements?" _Implementation note: Selection sort as second sorting algorithm; shows different strategy than bubble sort. Emphasizes algorithm comparison. Auto-graded by trace accuracy + comparison insight. CSTA: E6‑ALG‑AF‑01, E6‑ALG‑PS‑03._

Dependencies:
* T02.G5.13: Build and trace a bubble sort visualization for 4 elements
* T02.G6.07.01: Build a find-maximum algorithm with trace output


ID: T02.G6.15
Topic: T02 – Algorithm Diagrams
Skill: Draw a flowchart showing algorithm with multiple data sources
Description: **Student task:** Create a flowchart for an algorithm that combines data from multiple sources. Show data inputs coming from different places, how they merge, and the combined output. **Visual scenario:** Task: "Calculate final grade from homework (40%), quizzes (30%), and exam (30%)." Flowchart shows three input branches: [Get homework scores] → [Calculate HW average], [Get quiz scores] → [Calculate quiz average], [Get exam score]. These three paths converge at: [Combine: 0.4×HW + 0.3×quiz + 0.3×exam] → [Show final grade] → END. Students draw the merging flow pattern. Question: "What happens if one source is missing?" Add error paths. _Implementation note: Data aggregation pattern; common in real applications. Shows non-linear flow with multiple inputs. Auto-graded by correct merge structure + error handling. CSTA: E6‑ALG‑AF‑01, E6‑DATA‑02._

Dependencies:
* T02.G6.09: Convert a flowchart diagram directly to pseudocode text
* T02.G5.14: Design an algorithm diagram showing data validation steps


---

## GRADE 7 (18 skills - added T02.G7.12 merge, T02.G7.13 event-driven, T02.G7.14 backtracking)




ID: T02.G7.01.01
Topic: T02 – Algorithm Diagrams
Skill: Trace a simulation with counter/accumulator patterns
Description: **Student task:** Trace a script that simulates change over time using counters (e.g., score increasing, population growing). Print state after each iteration and predict future values. **Visual scenario:** Simulation: bank balance grows by 10% each year. Script: [set balance to 100] → [repeat 5] → [change balance by balance * 0.1, print balance]. Trace: 110, 121, 133.1... Students predict year 6 value. _Implementation note: Simulation tracing with growth patterns. Auto-graded by prediction accuracy. CSTA: E7‑ALG‑AF‑01, E7‑ALG‑PS‑03._

Dependencies:
* T02.G6.06: Trace a list-processing algorithm with print blocks





ID: T02.G7.01.02
Topic: T02 – Algorithm Diagrams
Skill: Trace a physics simulation with position and velocity
Description: **Student task:** Trace a physics simulation where velocity affects position each frame. Track multiple state variables (position, velocity, acceleration) in a trace table. **Visual scenario:** Falling ball: [set y to 200, velocity to 0] → [repeat] → [change velocity by -2 (gravity), change y by velocity, print "y=" + y + " v=" + velocity]. Trace: y=200,v=0 | y=198,v=-2 | y=194,v=-4... _Implementation note: Physics simulation with multiple coupled variables. Auto-graded by trace table accuracy. CSTA: E7‑ALG‑AF‑01, E7‑ALG‑PS‑03._

Dependencies:
* T02.G7.01.01: Trace a simulation with counter/accumulator patterns





ID: T02.G7.02.01
Topic: T02 – Algorithm Diagrams
Skill: Add a breakpoint block to pause execution at a specific line
Description: **Student task:** Add the "breakpoint" block from Control category at a strategic point in a script. Run in Debug Mode (blue arrow) to pause execution there. **Visual scenario:** Script: [set x to 0] → [repeat 5] → [change x by 10] → [BREAKPOINT] → [say x]. Run in Debug Mode. Execution pauses after the loop. Students see x=50 before the say block runs. _Implementation note: Introduces breakpoint debugging tool. Auto-graded by correct breakpoint placement and pause observation. CSTA: E7‑PRO‑TR‑03._

Dependencies:
* T02.G6.05: Debug by comparing actual pseudocode to intended algorithm





ID: T02.G7.02.02
Topic: T02 – Algorithm Diagrams
Skill: Inspect variable values and compare to predictions at a breakpoint
Description: **Student task:** Pause at a breakpoint in Debug Mode. Examine the current values of all variables in the variable panel. Compare actual values to your predictions. **Visual scenario:** Script paused at breakpoint mid-loop. Variable panel shows: x=30, count=3. Student predicted x=40 at this point—there's a bug! The mismatch reveals the loop started counting from 1 instead of 0. _Implementation note: Variable inspection during pause. Auto-graded by prediction vs actual comparison. CSTA: E7‑PRO‑TR‑03._

Dependencies:
* T02.G7.02.01: Add a breakpoint block to pause execution at a specific line





ID: T02.G7.02.03
Topic: T02 – Algorithm Diagrams
Skill: Step through code block-by-block using Debug Mode controls
Description: **Student task:** After pausing at a breakpoint, use Debug Mode's step controls to execute one block at a time. Watch variables and sprite state change after each step. **Visual scenario:** Paused at breakpoint. Click "Step Over" → one block executes → x changes from 10 to 20 → click again → another block → sprite moves. Students trace execution manually, block by block. _Implementation note: Step-through debugging. Auto-graded by accurate step-by-step trace. CSTA: E7‑PRO‑TR‑03._

Dependencies:
* T02.G7.02.02: Examine variable values in the variable panel at a breakpoint





ID: T02.G7.03.01
Topic: T02 – Algorithm Diagrams
Skill: Build a linear search algorithm to find a target value
Description: **Student task:** Create a script that searches through a list sequentially to find a specific target value. Return the position where it's found (or "not found"). **Visual scenario:** List: [4, 8, 2, 7, 5]. Target: 7. Students build: [repeat for each item] → [if item = target, say "Found at position " + i]. Script checks 4, 8, 2, 7 → "Found at position 4". _Implementation note: Basic linear search algorithm. Auto-graded by correct position returned. CSTA: E7‑ALG‑AF‑01, E7‑PRO‑PF‑01._

Dependencies:
* T02.G6.07: Build a find-maximum algorithm with trace output
* T10.G5.03: Work with list data structures





ID: T02.G7.03.02
Topic: T02 – Algorithm Diagrams
Skill: Add trace output to visualize search algorithm steps
Description: **Student task:** Add print blocks to your search algorithm to show each comparison in the console. Make the search process visible step-by-step. **Visual scenario:** Searching for 7 in [4, 8, 2, 7, 5]. Console output: "Checking item 1: 4 - no match", "Checking item 2: 8 - no match", "Checking item 3: 2 - no match", "Checking item 4: 7 - FOUND!" _Implementation note: Search algorithm tracing. Auto-graded by correct trace sequence. CSTA: E7‑ALG‑AF‑01, E7‑PRO‑TR‑03._

Dependencies:
* T02.G7.03.01: Build a linear search algorithm to find a target value





ID: T02.G7.03.03
Topic: T02 – Algorithm Diagrams
Skill: Optimize search with early exit when target is found
Description: **Student task:** Modify your search algorithm to stop immediately when the target is found instead of checking all remaining items. Use "stop this script" or a flag variable. **Visual scenario:** List: [4, 8, 7, 2, 5]. Target: 7. Without early exit: checks all 5 items. With early exit: stops after item 3. Console shows only 3 checks instead of 5. Compare efficiency. _Implementation note: Early exit optimization. Auto-graded by reduced comparison count. CSTA: E7‑ALG‑IM‑04, E7‑PRO‑PF‑01._

Dependencies:
* T02.G7.03.02: Add trace output to visualize search algorithm steps





ID: T02.G7.04
Topic: T02 – Algorithm Diagrams
Skill: Generate and analyze pseudocode for a search algorithm
Description: **Student task:** Generate pseudocode from your search algorithm. Analyze how the pseudocode represents the search logic (iteration, comparison, early exit). **Visual scenario:** Block script for linear search with early exit. Generated pseudocode: "for each item in list: if item equals target: return position; stop searching; return not found". Students identify: loop structure, conditional check, early exit pattern. _Implementation note: Pseudocode analysis of search algorithms. Auto-graded by structure identification. CSTA: E7‑ALG‑AF‑01._

Dependencies:
* T02.G7.03.03: Optimize search with early exit when target is found
* T02.G6.02: Match block structures to their pseudocode representation





ID: T02.G7.05
Topic: T02 – Algorithm Diagrams
Skill: Compare search algorithm efficiency by counting comparisons
Description: **Student task:** Compare two search algorithms on the same input. Count comparisons each makes using a counter variable and print blocks. **Visual scenario:** List: [4, 8, 2, 7, 5, 9, 1, 3]. Target: 7. Algorithm A (no early exit): 8 comparisons. Algorithm B (early exit): 4 comparisons. Students add [change comparisons by 1] inside loop and print final count. _Implementation note: Algorithm efficiency comparison. Auto-graded by correct counts. CSTA: E7‑ALG‑IM‑04._

Dependencies:
* T02.G7.03.03: Optimize search with early exit when target is found
* T02.G5.05: Compare two algorithms by counting operations





ID: T02.G7.06
Topic: T02 – Algorithm Diagrams
Skill: Debug edge case failures using breakpoints and trace output
Description: **Student task:** Test your search algorithm with edge cases. Use breakpoints and print blocks to identify where/why it fails. **Visual scenario:** Edge cases: (1) empty list [] → should return "not found" without error. (2) single item [7] → should find it. (3) target not in list [1,2,3] target=9 → should return "not found". Students step through with breakpoints to find bugs. _Implementation note: Edge case debugging. Auto-graded by all edge cases handled. CSTA: E7‑PRO‑TR‑03._

Dependencies:
* T02.G7.02.03: Step through code block-by-block using Debug Mode controls
* T02.G7.03.02: Add trace output to visualize search algorithm steps
* T02.G6.08: Test an algorithm with normal, edge, and boundary inputs


ID: T02.G7.07.01
Topic: T02 – Algorithm Diagrams
Skill: Explain the split-the-list strategy for efficient search
Description: **Student task:** Given a sorted list, explain why checking the middle element first is faster than checking from the start. Compare linear vs binary approach. **Visual scenario:** Sorted list [2,5,8,11,14,17,20]. Target: 17. Compare: Linear search checks 2,5,8,11,14,17 (6 comparisons). Binary: check 11 (too small, go right), check 17 (found!) (2 comparisons). Students explain why splitting eliminates half the list each time. _Implementation note: Conceptual understanding before tracing; builds intuition for logarithmic efficiency. Auto-graded by explanation of elimination reasoning. CSTA: E7-ALG-AF-01._

Dependencies:
* T02.G7.05: Compare search algorithm efficiency by counting comparisons


ID: T02.G7.07.02
Topic: T02 – Algorithm Diagrams
Skill: Trace binary search showing search space reduction at each step
Description: **Student task:** Trace a binary search algorithm on a sorted list. Record after each step: the range being searched, the middle element checked, and the decision (go left/right/found). **Visual scenario:** Sorted list: [2, 5, 8, 11, 14, 17, 20]. Target: 14. Trace table: Step 1: Range [0-6], mid=11, 14>11 → go right. Step 2: Range [4-6], mid=17, 14<17 → go left. Step 3: Range [4-4], mid=14, FOUND! Students fill detailed trace showing each split decision. _Implementation note: Detailed binary search tracing; O(log n) efficiency demonstrated. Auto-graded by trace table accuracy. CSTA: E7-ALG-AF-01, E7-ALG-PS-03._

Dependencies:
* T02.G7.07.01: Explain the split-the-list strategy for efficient search
* T02.G7.03.03: Optimize search with early exit when target is found


ID: T02.G7.08
Topic: T02 – Algorithm Diagrams
Skill: Design a flowchart showing multi-sprite algorithm coordination
Description: **Student task:** Create a flowchart that shows how multiple sprites coordinate to execute an algorithm together. Use swim lanes (parallel columns) for each sprite, with arrows showing broadcasts between them. **Visual scenario:** Turn-based game flowchart: Player sprite column shows "wait for turn → make move → broadcast 'done'". Enemy sprite column shows "wait for 'done' → calculate move → execute move → broadcast 'player-turn'". Draw synchronization arrows between lanes showing message passing. _Implementation note: Multi-actor flowchart with swim lanes; connects to T06 events. Auto-graded by correct swim lane structure and broadcast arrows. CSTA: E7-ALG-AF-01._

Dependencies:
* T02.G6.09: Convert a flowchart diagram directly to pseudocode text
* T06.G5.03: Build a level-start/level-end broadcast sequence coordinating 3 sprites


ID: T02.G7.09
Topic: T02 – Algorithm Diagrams
Skill: Build an algorithm visualization that animates execution with user controls
Description: **Student task:** Create an interactive algorithm visualization where users can control playback: play, pause, step forward, step backward, and adjust speed. Display current step, variable values, and highlight active code. **Visual scenario:** Binary search visualization: sorted list of numbers displayed. User clicks "Step" → middle element highlights, comparison shown, half of list grays out. User clicks "Step" again → next middle highlights. "Speed" slider adjusts animation timing. "Reset" button restarts. Students build controls using button widgets and implement animation logic. _Implementation note: Full-featured algorithm animator; combines T15 widgets with algorithm tracing. Auto-graded by control functionality + correct algorithm animation. CSTA: E7-ALG-AF-01, E7-PRO-PF-01._

Dependencies:
* T02.G6.10: Create animated algorithm visualization using sprite movements
* T02.G5.09: Build an interactive algorithm stepper using button and label widgets


ID: T02.G7.10
Topic: T02 – Algorithm Diagrams
Skill: Design a sequence diagram for multi-sprite message passing
Description: **Student task:** Create a sequence diagram showing how multiple sprites communicate over time. Draw vertical "lifelines" for each sprite, with horizontal arrows showing broadcasts and responses. Time flows downward. **Visual scenario:** Three sprites: Player, Enemy, GameManager. Sequence diagram shows: Player→GameManager: "I moved" | GameManager→Enemy: "Check collision" | Enemy→GameManager: "Collision detected" | GameManager→Player: "Take damage". Students draw lifelines, arrows with message labels, and show the order of communication. Compare to actual broadcast/receive blocks in code. _Implementation note: UML-lite sequence diagrams; visualizes event-driven programming. Connects to T06 broadcast skills. Auto-graded by correct message order and sprite identification. CSTA: E7-ALG-AF-01, E7-PRO-PF-01._

Dependencies:
* T02.G7.08: Design a flowchart showing multi-sprite algorithm coordination
* T02.G6.10: Create animated algorithm visualization using sprite movements


ID: T02.G7.11
Topic: T02 – Algorithm Diagrams
Skill: Trace parallel algorithms showing concurrent execution paths
Description: **Student task:** Trace an algorithm where multiple scripts run simultaneously on different sprites. Create a timeline diagram showing what each sprite is doing at each moment, and identify points where they interact. **Visual scenario:** Two sprites both running "forever" loops. Sprite A: move, check collision. Sprite B: move, check collision. Timeline shows: t=0: both start | t=1: A moves, B moves | t=2: A checks, B checks | t=3: COLLISION—both respond. Students trace parallel paths, mark synchronization points, identify race conditions (what if A checks before B moves?). _Implementation note: Parallel execution tracing; critical for understanding concurrent programs and multiplayer games. Auto-graded by correct timeline + interaction point identification. CSTA: E7-ALG-AF-01, E7-ALG-PS-03._

Dependencies:
* T02.G7.10: Design a sequence diagram for multi-sprite message passing
* T02.G7.01.02: Trace a physics simulation with position and velocity


ID: T02.G7.12
Topic: T02 – Algorithm Diagrams
Skill: Trace a merge operation combining two sorted lists
Description: **Student task:** Trace the merge operation that combines two already-sorted lists into one sorted list. Track pointers for each list and show how elements are selected and placed. **Visual scenario:** List A: [2, 5, 8]. List B: [1, 4, 6, 9]. Merge trace: Compare 2 vs 1 → take 1 from B → result [1]. Compare 2 vs 4 → take 2 from A → [1,2]. Compare 5 vs 4 → take 4 from B → [1,2,4]. Continue... Final: [1,2,4,5,6,8,9]. Trace table shows: Step | A pointer | B pointer | Compare | Take from | Result so far. Students fill complete trace and predict result before verifying. _Implementation note: Merge as foundational operation for merge sort; O(n) merge of sorted inputs. Builds toward divide-and-conquer understanding. Auto-graded by trace table accuracy. CSTA: E7‑ALG‑AF‑01, E7‑ALG‑PS‑03._

Dependencies:
* T02.G6.14: Trace a selection sort algorithm showing minimum-finding passes
* T02.G7.03.01: Build a linear search algorithm to find a target value


ID: T02.G7.13
Topic: T02 – Algorithm Diagrams
Skill: Design a flowchart for event-driven algorithm with multiple triggers
Description: **Student task:** Create a flowchart that shows an algorithm responding to multiple different events. Show how different triggers lead to different paths, and how the system returns to a "waiting" state. **Visual scenario:** Task: "Smart home controller." Flowchart: IDLE state (waiting) → receives different events: [motion detected] → [turn on lights] → [wait 5 min] → [turn off] → IDLE. [doorbell pressed] → [send phone notification] → [show camera] → IDLE. [temperature > 80] → [turn on AC] → [wait until temp < 75] → [turn off AC] → IDLE. Students draw the multi-trigger structure with clear event labels and return paths. _Implementation note: Event-driven design pattern; shows non-linear algorithm triggered by external events. Common in games, IoT, UI programming. Auto-graded by correct event-response structure. CSTA: E7‑ALG‑AF‑01, E7‑PRO‑PF‑01._

Dependencies:
* T02.G7.08: Design a flowchart showing multi-sprite algorithm coordination
* T02.G6.11: Design a flowchart template for reuse across similar problems


ID: T02.G7.14
Topic: T02 – Algorithm Diagrams
Skill: Build algorithm animation showing backtracking (maze solving)
Description: **Student task:** Create a visual animation that shows a backtracking algorithm solving a maze. Show the algorithm trying a path, hitting a dead end, backing up, and trying another path. Display "tried" cells differently from "current path" cells. **Visual scenario:** Simple 5x5 maze grid. Animation shows: sprite moves right (mark as current) → moves down → dead end! → backtrack (change color to "tried, not part of solution") → try different direction → eventually find exit. Students see: green = current path, gray = tried and rejected, white = not yet explored. Final solution path highlighted. Discussion: "Why does the algorithm remember where it tried?" _Implementation note: Backtracking visualization; classic algorithm pattern for search problems. Uses sprite movement and costume/color changes. Auto-graded by correct animation sequence showing backtrack behavior. CSTA: E7‑ALG‑AF‑01, E7‑PRO‑PF‑01._

Dependencies:
* T02.G7.09: Build an algorithm visualization that animates execution with user controls
* T02.G6.10: Create animated algorithm visualization using sprite movements


---

## GRADE 8 (30 skills - added 8 advanced skills for AI-era mastery, graph algorithms, systems)




ID: T02.G8.01.01
Topic: T02 – Algorithm Diagrams
Skill: Write pseudocode for a multi-step calculation algorithm
Description: **Student task:** Write pseudocode on paper for an algorithm that performs multiple sequential calculations. Use clear variable names and proper structure. **Visual scenario:** Task: "Calculate the average of a list of numbers." Student writes: "SET sum to 0; FOR each number in list: ADD number to sum; SET average to sum / count; RETURN average". Then implement and verify. _Implementation note: Pseudocode writing for calculations. Auto-graded by pseudocode structure + implementation match. CSTA: E8‑ALG‑AF‑01._

Dependencies:
* T02.G6.04: Write pseudocode first, then implement as blocks





ID: T02.G8.01.02
Topic: T02 – Algorithm Diagrams
Skill: Write pseudocode for input validation with error handling
Description: **Student task:** Write pseudocode for an algorithm that validates user input and handles invalid cases. Use loops for re-prompting and conditionals for validation. **Visual scenario:** Task: "Get a number between 1-100 from user." Student writes: "REPEAT: ASK user for number; IF number < 1 OR number > 100: PRINT 'Invalid, try again'; UNTIL number is valid; RETURN number". _Implementation note: Validation loop pattern. Auto-graded by handling invalid inputs correctly. CSTA: E8‑ALG‑AF‑01._

Dependencies:
* T02.G8.01.01: Write pseudocode for a multi-step calculation algorithm





ID: T02.G8.01.03
Topic: T02 – Algorithm Diagrams
Skill: Write pseudocode for a data processing algorithm
Description: **Student task:** Write pseudocode for an algorithm that processes a collection of data to produce a result. Include loops, conditionals, and helper steps. **Visual scenario:** Task: "Find the median of a list." Student writes: "SORT the list; SET middle to length / 2; IF length is odd: RETURN item at middle; ELSE: RETURN average of items at middle and middle+1". _Implementation note: Complex data processing pseudocode. Auto-graded by algorithm correctness. CSTA: E8‑ALG‑AF‑01._

Dependencies:
* T02.G8.01.01: Write pseudocode for a multi-step calculation algorithm
* T10.G6.01: Sort a table by a column





ID: T02.G8.02
Topic: T02 – Algorithm Diagrams
Skill: Implement pseudocode as blocks and verify with generated pseudocode
Description: **Student task:** Take written pseudocode and implement it as a CreatiCode block script. Generate pseudocode from your blocks and compare to verify your implementation matches the plan. **Visual scenario:** Given pseudocode for average calculation. Students build blocks. Generate pseudocode. Compare: original says "divide by count", generated says "divide by length of list" — equivalent! Implementation verified. _Implementation note: Pseudocode → code → verification cycle. Auto-graded by behavior match. CSTA: E8‑ALG‑AF‑01, E8‑PRO‑PF‑01._

Dependencies:
* T02.G8.01.01: Write pseudocode for a multi-step calculation algorithm
* T02.G6.01: Use the pseudocode generation block to export algorithm text





ID: T02.G8.03.01
Topic: T02 – Algorithm Diagrams
Skill: Design a comprehensive test plan for an algorithm
Description: **Student task:** Create a test plan document listing test cases by category: normal cases (typical inputs), edge cases (empty, single item, extremes), boundary cases (at limits). Write expected output for each. **Visual scenario:** For median algorithm, students create: Normal: [1,2,3,4,5]→expected 3. Edge: []→error, [5]→5. Boundary: [1,1,1,1]→1, all same values. Even length: [1,2,3,4]→2.5. List 8+ test cases with expected outputs before running any code. _Implementation note: Test planning skill; design before execution. Auto-graded by test case coverage + correct expected outputs. CSTA: E8-ALG-AF-01, E8-PRO-TR-03._

Dependencies:
* T02.G8.02: Implement pseudocode as blocks and verify with generated pseudocode
* T02.G7.06: Debug edge case failures using breakpoints and trace output


ID: T02.G8.03.02
Topic: T02 – Algorithm Diagrams
Skill: Execute test plan and document results
Description: **Student task:** Run each test case from your test plan, record actual output, compare to expected, mark pass/fail. Document any failures with details about what went wrong. **Visual scenario:** Test matrix with columns: Test | Input | Expected | Actual | Pass/Fail. Students fill in actual outputs: [1,2,3,4,5]→3 ✓Pass. []→crash ✗Fail (expected error message, got crash). Document failure details: "Empty list causes division by zero". _Implementation note: Test execution and documentation; systematic verification. Auto-graded by accuracy of pass/fail determination. CSTA: E8-PRO-TR-03._

Dependencies:
* T02.G8.03.01: Design a comprehensive test plan for an algorithm





ID: T02.G8.04
Topic: T02 – Algorithm Diagrams
Skill: Refactor algorithms by identifying and removing redundancy
Description: **Student task:** Analyze a complex algorithm to find redundant operations. Remove them and verify the simplified version still works. **Visual scenario:** Original: calculates sum twice, stores intermediate values never used. Pseudocode shows: "sum = 0; for each x: sum += x; total = sum; average = total / count". Redundant: "total" variable. Simplified: "sum = 0; for each x: sum += x; average = sum / count". Test to verify same behavior. _Implementation note: Algorithm refactoring. Auto-graded by behavior preservation + reduced complexity. CSTA: E8‑ALG‑IM‑04._

Dependencies:
* T02.G8.03.02: Execute test plan and document results
* T02.G5.06: Optimize an algorithm by removing redundant blocks






ID: T02.G8.05
Topic: T02 – Algorithm Diagrams
Skill: Compare deterministic vs probabilistic algorithm outputs
Description: **Student task:** Build two versions of an algorithm—one deterministic (same input → same output) and one probabilistic (uses randomness). Run each multiple times and compare outputs. **Visual scenario:** Task: "Select an item from a list." Deterministic: always return first item. Probabilistic: return random item using [pick random]. Run 5 times each. Deterministic: A,A,A,A,A. Probabilistic: C,A,D,B,A. Discuss when each is appropriate. _Implementation note: Algorithm behavior comparison. Auto-graded by correct identification of patterns. CSTA: E8‑ALG‑AF‑01._

Dependencies:
* T02.G8.03.02: Execute test plan and document results
* T02.G7.01.02: Trace a physics simulation with position and velocity








ID: T02.G8.06.01
Topic: T02 – Algorithm Diagrams
Skill: Draw a state diagram for a multi-state algorithm
Description: **Student task:** Create a state diagram showing states (circles) and transitions (arrows with labels) for an algorithm with multiple modes. **Visual scenario:** Task: "Draw a state diagram for a traffic light controller." States: Red, Yellow, Green (shown as circles). Transitions: Red→Green (after 30s), Green→Yellow (after 25s), Yellow→Red (after 5s). Students draw circles for each state, arrows with timing labels. Question: "If currently Green for 20s, what's next state after 10s?" **Answer:** Yellow. _Implementation note: State diagram notation; useful for game states, UI modes, simulations. Auto-graded by correct states and transitions. CSTA: E8‑ALG‑AF‑01._

Dependencies:
* T02.G7.01.02: Trace a physics simulation with position and velocity
* T02.G6.09: Convert a flowchart diagram directly to pseudocode text


ID: T02.G8.06.02
Topic: T02 – Algorithm Diagrams
Skill: Implement a state machine from a state diagram using variables and conditionals
Description: **Student task:** Take a state diagram and implement it as a working CreatiCode script. Use a variable to track current state, conditionals to handle transitions. **Visual scenario:** Implement the traffic light state diagram. Students build: [set state to "red"] → [forever loop] → [if state = "red" and timer > 30: set state to "green", reset timer] → [if state = "green" and timer > 25: set state to "yellow", reset timer] → [if state = "yellow" and timer > 5: set state to "red", reset timer]. Light sprite changes color based on state variable. _Implementation note: State machine implementation; connects diagram representation to executable code. Auto-graded by correct state transitions. CSTA: E8‑ALG‑AF‑01, E8‑PRO‑PF‑01._

Dependencies:
* T02.G8.06.01: Draw a state diagram for a multi-state algorithm


ID: T02.G8.07
Topic: T02 – Algorithm Diagrams
Skill: Analyze algorithm complexity by counting operations at different scales
Description: **Student task:** Compare two algorithms by counting operations for small and large inputs. Recognize which algorithm scales better. **Visual scenario:** Task: "Count comparisons for linear search vs binary search." List sizes: 8 items, 64 items, 1024 items. Linear search (worst): 8, 64, 1024 comparisons. Binary search (worst): 3, 6, 10 comparisons. Students fill in table, observe: linear grows with N, binary grows slowly (log N). Question: "For 1 million items, which is faster?" **Answer:** Binary search (by far). _Implementation note: Intuitive complexity comparison; lays foundation for Big-O thinking. Auto-graded by correct operation counts and comparison. CSTA: E8‑ALG‑IM‑04._

Dependencies:
* T02.G7.07.02: Trace binary search showing search space reduction at each step
* T02.G7.05: Compare search algorithm efficiency by counting comparisons


ID: T02.G8.08
Topic: T02 – Algorithm Diagrams
Skill: Use AI to generate and verify pseudocode for a complex algorithm
Description: **Student task:** Use the ChatGPT block to request pseudocode for a given task. Verify the AI-generated pseudocode by tracing through test cases, then implement and compare. **Visual scenario:** Task: "Get pseudocode for finding the second-largest number in a list." Prompt ChatGPT: "Write pseudocode to find the second largest number." AI returns pseudocode. Students: (1) trace pseudocode with [5,9,3,9,7], (2) identify if it handles duplicates correctly, (3) implement in blocks, (4) test edge cases. If AI made errors, debug and fix. _Implementation note: AI-assisted algorithm design with human verification; critical skill for AI-augmented programming. Auto-graded by correct implementation handling all test cases. CSTA: E8‑ALG‑AF‑01, E8‑AI‑INT‑04._

Dependencies:
* T02.G8.01.03: Write pseudocode for a data processing algorithm
* T02.G8.03.02: Execute test plan and document results


ID: T02.G8.09
Topic: T02 – Algorithm Diagrams
Skill: Document an algorithm with structured comments explaining each section
Description: **Student task:** Add comprehensive documentation to a complex algorithm: (1) Header comment explaining algorithm purpose and inputs/outputs, (2) Section comments marking major phases (initialize, process, output), (3) Inline comments explaining non-obvious logic. **Visual scenario:** Document a find-median algorithm: "-- PURPOSE: Find median of list, handles odd/even lengths --", "-- PHASE 1: Sort the list --", "-- PHASE 2: Find middle --", "-- Note: for even length, average two middle values --". Students create self-documenting code with clear structure. _Implementation note: Algorithm documentation standards; prepares for collaborative coding and code review. Auto-graded by comment structure + coverage of key sections. CSTA: E8-PRO-PF-01._

Dependencies:
* T02.G8.04: Refactor algorithms by identifying and removing redundancy
* T02.G6.04: Write pseudocode first, then implement as blocks


ID: T02.G8.10
Topic: T02 – Algorithm Diagrams
Skill: Verify AI-generated algorithm against test cases to identify and correct errors
Description: **Student task:** Given AI-generated pseudocode for a task, systematically verify it by: (1) tracing through 3+ test cases (normal, edge, boundary), (2) identifying any errors in the AI output, (3) correcting the pseudocode. **Visual scenario:** AI generates pseudocode for "find second smallest". Students trace: [5,3,8]→works. [5,5,5]→fails (duplicates not handled). [5]→fails (not enough items). Students identify bugs: "AI assumed all unique values" and "AI didn't check list length". Propose corrections: add duplicate handling, add length check. _Implementation note: Critical AI verification skill; human oversight of AI tools. Auto-graded by error identification + correction quality. CSTA: E8-ALG-AF-01, E8-AI-INT-04._

Dependencies:
* T02.G8.08: Use AI to generate and verify pseudocode for a complex algorithm
* T02.G8.03.02: Execute test plan and document results


ID: T02.G8.11
Topic: T02 – Algorithm Diagrams
Skill: Compare and reconcile algorithm diagrams from multiple team members
Description: **Student task:** Given two different flowcharts created by different team members for the same problem, compare them systematically: identify structural differences, determine which elements are equivalent but expressed differently, find genuine disagreements, and propose a reconciled version. **Visual scenario:** Team member A's flowchart for "validate password": checks length first, then special characters. Team member B's flowchart: checks special characters first, then length. Students analyze: (1) Both check the same things, (2) Order differs—does it matter? (3) A has more detailed error messages, (4) B handles empty input explicitly. Reconcile: combine A's detail with B's edge case handling. Propose merged flowchart. _Implementation note: Collaborative algorithm design; critical for team projects. Prepares for code review skills. Auto-graded by identification of differences + quality of reconciliation. CSTA: E8-ALG-AF-01, E8-PRO-PF-01._

Dependencies:
* T02.G8.09: Document an algorithm with structured comments explaining each section
* T02.G7.08: Design a flowchart showing multi-sprite algorithm coordination


ID: T02.G8.12
Topic: T02 – Algorithm Diagrams
Skill: Draw a system architecture diagram showing component interactions
Description: **Student task:** Create a system architecture diagram for a multi-component project. Show components as boxes, data flows as arrows, and external systems (user input, databases, APIs) with special notation. **Visual scenario:** Project: "Multiplayer quiz game." Architecture diagram shows: [User Interface] ↔ [Game Logic] ↔ [Score Manager] | [Game Logic] ↔ [Cloud Database] | [Game Logic] ↔ [Timer] | [Multiple Players] ↔ [Sync Manager]. Students identify: (1) Which components talk to each other, (2) Data flowing between them, (3) External dependencies. Label each arrow with what data flows (e.g., "quiz question", "player answer", "score update"). _Implementation note: System-level design thinking; prepares for large project architecture. Similar to professional architecture diagrams. Auto-graded by correct component relationships. CSTA: E8-ALG-AF-01, E8-SYS-02._

Dependencies:
* T02.G8.06.02: Implement a state machine from a state diagram using variables and conditionals
* T02.G7.10: Design a sequence diagram for multi-sprite message passing


ID: T02.G8.13
Topic: T02 – Algorithm Diagrams
Skill: Use AI to generate flowcharts from natural language descriptions
Description: **Student task:** Use the ChatGPT block to request a flowchart description from a natural language algorithm description. Parse the AI response into actual flowchart elements and draw the diagram. Verify the AI-generated structure is correct. **Visual scenario:** Task: "I want to check if a number is prime." Students prompt ChatGPT: "Describe a flowchart for checking if a number is prime. List each shape and connection." AI responds with text description. Students: (1) Parse response into shapes/connections, (2) Draw the flowchart, (3) Trace through examples to verify correctness, (4) Fix any AI errors. _Implementation note: AI-assisted diagram generation with human verification; critical skill for AI-augmented development. Auto-graded by correct final flowchart + verification documentation. CSTA: E8-ALG-AF-01, E8-AI-INT-04._

Dependencies:
* T02.G8.08: Use AI to generate and verify pseudocode for a complex algorithm
* T02.G6.09: Convert a flowchart diagram directly to pseudocode text


ID: T02.G8.14
Topic: T02 – Algorithm Diagrams
Skill: Create algorithm diagrams for scalable systems (millions of data points)
Description: **Student task:** Design algorithm diagrams that work at scale. Show how your algorithm handles 10 items vs 1,000,000 items. Identify bottlenecks and show optimization strategies in the diagram. **Visual scenario:** Task: "Search algorithm at scale." Diagram 1: Linear search on 10 items (simple loop). Diagram 2: Same algorithm on 1,000,000 items—add annotations showing "1M comparisons needed!" Diagram 3: Binary search alternative with annotations "only 20 comparisons needed at 1M scale". Students annotate diagrams with operation counts at different scales. Question: "At what scale does the difference matter?" _Implementation note: Scalability thinking in algorithm design; critical for real-world applications. Connects to G8.07 complexity analysis. Auto-graded by correct scale annotations + bottleneck identification. CSTA: E8-ALG-IM-04, E8-ALG-AF-01._

Dependencies:
* T02.G8.07: Analyze algorithm complexity by counting operations at different scales
* T02.G7.07.02: Trace binary search showing search space reduction at each step


ID: T02.G8.15
Topic: T02 – Algorithm Diagrams
Skill: Build a diagram version control system tracking changes over time
Description: **Student task:** Create a system that saves multiple versions of a diagram and allows comparing versions. Use list variables to store diagram states, add "Save Version" and "Load Version" buttons, and show what changed between versions. **Visual scenario:** Students build: (1) "Save Version" button that stores current diagram state to a list, (2) Version selector showing v1, v2, v3, (3) "Load Version" to restore a previous state, (4) "Compare Versions" that highlights differences (boxes added/removed/moved). Test by making changes, saving, making more changes, then comparing. _Implementation note: Version control concepts applied to diagrams; prepares for git/collaboration workflows. Advanced project using lists + widgets. Auto-graded by save/load functionality + version comparison. CSTA: E8-PRO-PF-01, E8-COL-02._

Dependencies:
* T02.G8.11: Compare and reconcile algorithm diagrams from multiple team members
* T02.G6.13: Build an interactive flowchart editor using sprites and clicks


ID: T02.G8.16
Topic: T02 – Algorithm Diagrams
Skill: Design a formal specification from a flowchart for verification
Description: **Student task:** Convert a flowchart into a formal specification that can be verified. Write preconditions (what must be true before), postconditions (what must be true after), and invariants (what stays true during). Use these to prove the algorithm is correct. **Visual scenario:** Flowchart for "find maximum in list." Formal specification: PRECONDITION: list has ≥1 item. POSTCONDITION: result equals the largest value in list. INVARIANT: maxSoFar is always ≥ all items seen so far. Students annotate flowchart with these formal statements. Trace through to verify invariant holds at each step. _Implementation note: Formal methods introduction; prepares for software verification and correctness proofs. Advanced theoretical concept. Auto-graded by correct specification statements + verification trace. CSTA: E8-ALG-AF-01, E8-PRO-TR-03._

Dependencies:
* T02.G8.04: Refactor algorithms by identifying and removing redundancy
* T02.G8.03.02: Execute test plan and document results


ID: T02.G8.17
Topic: T02 – Algorithm Diagrams
Skill: Critique AI-generated diagrams and improve them systematically
Description: **Student task:** Given an AI-generated flowchart (with intentional flaws), systematically critique it: identify structural issues, missing edge cases, unclear labels, and incorrect logic. Then improve the diagram with specific fixes. **Visual scenario:** AI generated a flowchart for "password validation." Flaws: (1) Missing edge case for empty password, (2) Unclear label "check stuff", (3) Wrong order—checks length after checking characters, (4) No error messages shown. Students: (1) List all flaws found, (2) Explain why each is a problem, (3) Draw improved version fixing all issues. Compare original to improved. _Implementation note: Critical evaluation of AI outputs; essential skill for AI-augmented work. Develops systematic critique methodology. Auto-graded by flaw identification + quality of improvements. CSTA: E8-AI-INT-04, E8-ALG-AF-01._

Dependencies:
* T02.G8.13: Use AI to generate flowcharts from natural language descriptions
* T02.G8.10: Verify AI-generated algorithm against test cases to identify and correct errors


ID: T02.G8.18
Topic: T02 – Algorithm Diagrams
Skill: Draw a pipeline diagram for data processing workflows
Description: **Student task:** Create a pipeline diagram showing how data flows through multiple processing stages. Each stage transforms the data and passes it to the next. Show intermediate data states between stages. **Visual scenario:** Task: "Image processing pipeline." Diagram: [Raw image] → Stage 1: [Resize to 256x256] → [256x256 image] → Stage 2: [Convert to grayscale] → [grayscale image] → Stage 3: [Detect edges] → [edge map] → Stage 4: [Find shapes] → [shape list] → OUTPUT. Label each arrow with the data format at that point. Question: "What happens if Stage 2 fails?" Add error handling branches. _Implementation note: Pipeline architecture; common in data science, ML, and modern applications. Shows data transformation focus vs control flow focus. Auto-graded by correct stage sequence + data labels. CSTA: E8-ALG-AF-01, E8-DATA-02._

Dependencies:
* T02.G8.12: Draw a system architecture diagram showing component interactions
* T02.G4.09: Draw a data flow diagram showing input, process, and output


ID: T02.G8.19
Topic: T02 – Algorithm Diagrams
Skill: Design algorithm diagrams for distributed systems with message passing
Description: **Student task:** Create diagrams showing how algorithms work across multiple computers or processes that communicate through messages. Show message sends, receives, and how state synchronizes. **Visual scenario:** Task: "Multiplayer game score sync." Diagram shows: Player 1 computer | Server | Player 2 computer. When P1 scores: P1 → [send "score +10" to Server] → Server receives → [update global score] → [broadcast "new total: 150" to all] → P2 receives → [update local display]. Students draw timeline showing: message send (arrow out), network delay (dashed line), message receive (arrow in), local processing. Include: "What if a message is lost?" handling. _Implementation note: Distributed systems thinking; critical for modern applications. Shows asynchronous communication patterns. Auto-graded by correct message flow + error handling consideration. CSTA: E8‑ALG‑AF‑01, E8‑SYS‑02._

Dependencies:
* T02.G8.12: Draw a system architecture diagram showing component interactions
* T02.G7.11: Trace parallel algorithms showing concurrent execution paths


ID: T02.G8.20
Topic: T02 – Algorithm Diagrams
Skill: Trace a graph traversal algorithm (BFS or DFS) on a simple graph
Description: **Student task:** Given a simple graph (5-7 nodes with connections), trace either breadth-first search (BFS) or depth-first search (DFS). Show the order nodes are visited, track which nodes are "seen but not yet processed" vs "fully processed". **Visual scenario:** Graph: A connects to B,C. B connects to D,E. C connects to F. Start at A. BFS trace: Visit A → queue [B,C] → visit B → queue [C,D,E] → visit C → queue [D,E,F] → ... Order: A,B,C,D,E,F (level by level). DFS trace: Visit A → stack [C,B] → visit B → stack [C,E,D] → visit D → ... Order: A,B,D,E,C,F (depth first). Students draw graph with numbered visit order, plus table tracking queue/stack state. _Implementation note: Graph algorithm introduction; BFS uses queue, DFS uses stack. Fundamental CS algorithms. Auto-graded by correct visit order + state tracking. CSTA: E8‑ALG‑AF‑01, E8‑ALG‑PS‑03._

Dependencies:
* T02.G7.14: Build algorithm animation showing backtracking (maze solving)
* T02.G8.07: Analyze algorithm complexity by counting operations at different scales


ID: T02.G8.21
Topic: T02 – Algorithm Diagrams
Skill: Critique and improve an AI-generated algorithm for bias and edge cases
Description: **Student task:** Given an AI-generated algorithm (flowchart + pseudocode), systematically analyze it for: (1) potential bias in assumptions, (2) edge cases not handled, (3) unclear or ambiguous steps, (4) inefficiencies. Provide specific improvements. **Visual scenario:** AI generated algorithm for "suggest activity based on weather." Critique: (1) Bias: assumes outdoor activities are "better" — not accessible for all users. (2) Edge case: doesn't handle "weather unknown". (3) Unclear: "nice weather" not defined. (4) Inefficient: checks temperature twice. Students document each issue with evidence and propose fixes: add indoor options, define thresholds, combine checks. _Implementation note: Critical evaluation of AI with social awareness; combines technical and ethical analysis. Essential for responsible AI use. Auto-graded by issue identification quality + improvement proposals. CSTA: E8‑AI‑INT‑04, E8‑ALG‑AF‑01._

Dependencies:
* T02.G8.17: Critique AI-generated diagrams and improve them systematically
* T02.G8.10: Verify AI-generated algorithm against test cases to identify and correct errors


ID: T02.G8.22
Topic: T02 – Algorithm Diagrams
Skill: Design modular algorithm architecture separating concerns
Description: **Student task:** Decompose a complex algorithm into modular components with clear responsibilities. Create an architecture diagram showing: modules, their interfaces (what goes in/out), and how they connect. Apply separation of concerns. **Visual scenario:** Task: "Build a game with scoring, levels, and player management." Architecture: [Input Handler] → sends "player action" → [Game Logic] ← gets "level data" ← [Level Manager]. [Game Logic] → sends "score change" → [Score Manager] → sends "display update" → [UI Renderer]. Each module shows: inputs, outputs, responsibility. Students explain: "Why separate Score Manager from Game Logic?" _Implementation note: Software architecture principles; modular design for maintainability. Prepares for professional development practices. Auto-graded by clear module boundaries + correct interface definitions. CSTA: E8‑PRO‑PF‑01, E8‑ALG‑AF‑01._

Dependencies:
* T02.G8.12: Draw a system architecture diagram showing component interactions
* T02.G8.11: Compare and reconcile algorithm diagrams from multiple team members


ID: T02.G8.23
Topic: T02 – Algorithm Diagrams
Skill: Build an algorithm complexity comparison tool with visual output
Description: **Student task:** Create a CreatiCode project that compares two algorithms visually. Input: list size. Output: animated comparison showing how many operations each algorithm takes, with visual representation (bars, graphs, or counters). **Visual scenario:** Tool compares linear search vs binary search. User enters list size (e.g., 100). Tool shows: Linear search: up to 100 comparisons (tall red bar growing). Binary search: max 7 comparisons (short green bar). Animation runs through searches, counting comparisons in real-time. Graph shows O(n) vs O(log n) growth curves. Students build the tool with input, both algorithms, comparison counters, and visual output. _Implementation note: Meta-tool for algorithm analysis; combines coding skills with algorithm understanding. Uses charts/graphs from T10 or custom drawing. Auto-graded by correct operation counts + visual representation. CSTA: E8‑ALG‑IM‑04, E8‑PRO‑PF‑01._

Dependencies:
* T02.G8.07: Analyze algorithm complexity by counting operations at different scales
* T02.G7.09: Build an algorithm visualization that animates execution with user controls


ID: T02.G8.24
Topic: T02 – Algorithm Diagrams
Skill: Create a comprehensive algorithm portfolio with multiple diagram types
Description: **Student task:** Build a portfolio demonstrating mastery of algorithm diagramming. Include at least 5 different diagram types (flowchart, sequence diagram, state diagram, data flow diagram, architecture diagram) for a complex project. Each diagram should show a different aspect of the same system. **Visual scenario:** Project: "Multiplayer Drawing Game." Portfolio includes: (1) Flowchart: main game loop, (2) Sequence diagram: player join process, (3) State diagram: game states (waiting, playing, paused, ended), (4) Data flow: how drawing data moves from player to server to other players, (5) Architecture: client-server component structure. Students create all 5 diagrams for their project, with brief explanation of what each diagram shows. _Implementation note: Synthesis skill demonstrating diagram type selection; shows when to use each type. Portfolio format for assessment. Auto-graded by diagram variety + accuracy + appropriate type selection. CSTA: E8‑ALG‑AF‑01, E8‑PRO‑PF‑01._

Dependencies:
* T02.G8.12: Draw a system architecture diagram showing component interactions
* T02.G8.06.01: Draw a state diagram for a multi-state algorithm
* T02.G7.10: Design a sequence diagram for multi-sprite message passing


