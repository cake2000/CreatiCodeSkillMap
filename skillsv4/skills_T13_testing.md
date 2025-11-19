# T13 – Testing, Debugging & Error Handling: K–8 Skill List (v2, IXL‑Style Microsteps)

Topic reference: `T13 Testing, Debugging & Error Handling` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑TR (Testing and Refinement)

This v2 version upgrades the original draft to an **IXL‑style microstep design**, aligned with the principles in `docs/TOPIC_IXL_MICROSTEP_GUIDE.md` and the v6 design for T01.

Each skill below has:

- a stable **ID** (`T13.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** T13 is the home for **testing and debugging practices** across K–8. It focuses on noticing when behavior does not match intent, designing and running test cases, using debugging tools (tracing, logging, checks), handling invalid inputs and edge cases, and reflecting on reliability and bias.

- **Separation from T01–T05:**  
  - T01–T04 introduce everyday algorithms, patterns, and core constructs (loops, conditionals, variables); T13 assumes those ideas and focuses on *how we test and fix them* rather than teaching the constructs themselves.  
  - T02 is the primary home for algorithm representations and tracing (strips, flowcharts, pseudocode); T13 uses those representations but emphasizes behavior, failures, and fixes.  
  - T03 and T05 cover project‑level planning and user‑centered or simulation testing; T13 focuses on program correctness and robustness at the feature or script level.
- **Separation from T06–T12:**  
  - T06–T11 introduce and extend programming constructs; T12 focuses on naming, structure, and documentation so code is readable and maintainable.  
  - T13 complements them by teaching systematic debugging workflows, test design, and error handling. Refactoring for clarity appears in T12; refactoring “so it’s easier to test and debug” lives in T13.
- **Grade bands:**  
  - K–2: Picture‑based, unplugged/light‑digital skills about “try–check–fix” habits and spotting/fixing mistakes in everyday step sequences (no blocks, code, or environment terms).  
  - 3–5: Highest density of coding‑based debugging skills (loops, conditionals, variables) plus concrete test‑case design and basic error handling.  
  - 6–8: Higher‑order skills around systematic debugging processes, algorithm verification, robustness, and reasoning about accuracy and bias (including AI‑generated code).
- **Implementability:** All skills can be implemented with CreatiCode’s picture‑based K–2 activities, the block editor (for G3+), and simple UI for test‑plan tables, logging output, and reflection prompts.

IDs follow `T13.G<grade>.<nn>`. Existing IDs are preserved so JSON skill maps can be updated in a later data pass.

---

## Grade K (PreK–K)

At this stage, students begin recognizing that a set of steps might not work and may need fixing. Debugging is intuitive: trying out simple picture‑based routines, spotting obvious mistakes in what happens, and making one small change so the story “works.”

### T13.GK.01 – Spot a missing or wrong action

- **Short name:** Find what's wrong in a simple sequence
- **Description:** Students watch a short picture story or animation and compare what happens to what was supposed to happen (e.g., the character should jump but doesn't, or moves the wrong direction). They point to the step that is missing or incorrect without needing to fix it yet.
- **Challenge format:** Concept, visual matching. Show two versions of a short sequence: one correct and one with a missing or wrong picture. Students choose the wrong or missing step from several pictures. Auto‑grading checks the selected item.
- **CSTA:** EK‑PRO‑TR‑04 (Identify errors in step‑by‑step processes that do not work as expected).

### T13.GK.02 – Try again when the steps don't work

_Dependency:_
  * T01.GK.03: Find the first and last pictures


- **Short name:** Test and see if the steps work
- **Description:** Students follow a simple set of picture steps for a task (e.g., stacking blocks, moving a character on a board) and notice when the result is not what was intended. They experience the idea of "try, check, then try again" without needing to know how to change the steps themselves.
- **Challenge format:** Concept, guided exploration. Show a child or character following a set of picture instructions that leads to an obviously wrong result (e.g., the tower falls over). Prompt: "Did these steps work? Should we try again a different way?" Auto‑grading tracks that students identify when the steps did not work as intended.
- **CSTA:** EK‑PRO‑TR‑04.

### T13.GK.03 – Fix a single wrong direction or action in steps

_Dependency:_
  * T01.GK.03: Find the first and last pictures


- **Short name:** Fix a wrong move in the steps
- **Description:** Students “play computer” by acting out or watching a character follow a short list of picture steps to reach a fun goal (like a treasure or door). When the character ends up in the wrong place or does something silly, they identify which one movement is wrong (e.g., an arrow pointing left instead of right, or “sit down” too early) and swap it for a better step so the routine works.
- **Challenge format:** Concept, guided fix. Show a 3–4 step arrow/path sequence or routine with one incorrect picture and an animation of the character following it to the wrong place. Prompt: "Which step should we change so the character reaches the goal?" Students choose and replace the wrong picture from simple options. Auto‑grading checks that the corrected sequence reaches the intended outcome.  
- **CSTA:** EK‑PRO‑TR‑04.

---

## Grade 1

Grade 1 students begin more intentional debugging: identifying where a mistake lives in a set of steps, understanding sequence errors, and making deliberate fixes after “testing” a routine in their heads or with pictures.

### T13.G1.01 – Identify where a step is wrong

_Dependency:_
  * T01.GK.03: Find the first and last pictures


- **Short name:** Point out the wrong step
- **Description:** Students look at a set of picture‑based steps that, when “played out” as a story, clearly go wrong (e.g., “jump before moving” when the intent is move‑then‑jump). They select or highlight the step that causes the problem without yet fixing everything.
- **Challenge format:** Concept, multiple choice or highlighting. Show a strip of steps and ask "If we follow these steps, which one will make the routine go wrong?" or "Which step should not be there?" Students choose from highlighted regions. Auto‑grading checks the selection against reference.
- **CSTA:** E1‑PRO‑TR‑03 (Debug a step‑by‑step process with sequence errors to correct mistakes).

### T13.G1.02 – Fix a sequence error in steps

_Dependency:_
  * T01.GK.02: Put pictures in order for coming to class


- **Short name:** Put the steps in the right order
- **Description:** Students reorder picture or word cards in a step list to fix a sequencing error that made a story or game behave strangely (for example, moving “say hello” so it happens after “walk to friend,” or moving a “wait” picture to the correct position).
- **Challenge format:** Concept, drag‑and‑drop reorder. Show a set of steps in the wrong order and a short description or final picture of what should happen. Students drag cards to reorder them so the behavior matches the intent. Auto‑grading checks the final sequence against a reasonable intended order.
- **CSTA:** E1‑PRO‑TR‑03.

### T13.G1.03 – Change a number to fix a repeated action

_Dependency:_
  * T04.GK.02: Extend a repeating pattern by one tile


- **Short name:** Fix a number in the steps
- **Description:** Students modify a number in picture‑based instructions (e.g., change "jump 10 times" to "jump 3 times" so the movement matches a picture, or change a count of claps) to correct unexpected behavior in a routine.
- **Challenge format:** Concept, guided number edit. Show steps where a character repeats an action too many or too few times compared to a target picture. Prompt: "How many times should we do this?" Students choose or adjust the number. Auto‑grading checks that the new number matches the intended outcome.
- **CSTA:** E1‑PRO‑TR‑03.

### T13.G1.04 – Act out steps and say what went wrong

_Dependency:_
  * T01.GK.01: Put pictures in order for getting ready for bed


- **Short name:** Test steps and say what's wrong
- **Description:** Students act out or watch a character follow a set of steps and then play “bug detective” by explaining (in words, pictures, or simple text) what did not match expectations or what is missing (e.g., "We forgot to open the paint before painting").
- **Challenge format:** Concept, guided observation + response. Show a routine being followed with a deliberate error and ask: "What went wrong?" with answer choices (e.g., "skipped washing hands," "put shoes on before socks"). Auto‑grading checks the selected or typed observation.
- **CSTA:** E1‑PRO‑TR‑03.

---

## Grade 2

Grade 2 students debug step‑by‑step processes with simple repeats and signals (like “when we clap, start”). They use systematic approaches: testing, isolating problems, and trying fixes, still without needing a computer.

### T13.G2.01 – Fix steps that use the wrong signal

_Dependency:_
  * T01.GK.05: Move the picture that's in the wrong place


- **Short name:** Fix steps that don't respond at the right time
- **Description:** Students examine instructions where a character is supposed to act on a certain signal (e.g., clap, whistle, or card color) but the written or picture steps mention the wrong signal. They identify and fix the signal in the instructions so the behavior matches the story.
- **Challenge format:** Concept, guided debugging. Starter scenario: expected behavior is "When the teacher claps, everyone freezes." The instruction card instead says "When the teacher whistles." Students choose or replace the signal so it matches the intended behavior. Auto‑grading checks that the signal in the steps matches the description.
- **CSTA:** E2‑PRO‑TR‑03.

### T13.G2.02 – Trace a set of steps and predict behavior

_Dependency:_
  * T01.G1.05: Find the missing step in an algorithm
  * T03.G1.03: List steps for a simple classroom routine


- **Short name:** Follow the steps and say what will happen
- **Description:** Students "walk through" a simple set of instructions step by step, predicting what each step does and what the character or object will look like or where it will end up at the end. This mental tracing helps them spot logic errors before acting it out.
- **Challenge format:** Concept, tracing item. Show 4–6 picture steps and ask "What will the character do?" or "Where will the character be at the end?" with picture or multiple‑choice answers. Auto‑grading compares the answer to a reference outcome.
- **CSTA:** E2‑PRO‑TR‑03.

### T13.G2.03 – Fix a repeated step that happens too many or too few times

_Dependency:_
  * T13.G2.01: Spot what doesn't belong in a pattern


- **Short name:** Fix how many times something repeats
- **Description:** Students modify instructions where an action repeats the wrong number of times (e.g., clap 2 times instead of 5, or march too many steps). They change the number of repeats so the behavior matches a picture or description.
- **Challenge format:** Concept, guided debugging. Starter routine: a character should jump 5 times but only jumps 3 times (or the count in the instructions is clearly wrong). Students adjust the repeat number. Auto‑grading checks that the new count matches the intended total.  
- **CSTA:** E2‑PRO‑TR‑03.

### T13.G2.04 – Add a simple check to see if steps worked

_Dependency:_
  * T13.G2.03: Fix the wrong step in a simple task
  * T03.G1.03: List steps for a simple classroom routine


- **Short name:** Use a helper check to see what's happening
- **Description:** Students add a small “check” card or picture (e.g., a thumbs‑up or scoreboard picture) at a key point in a set of steps to show that something important has happened (like reaching a goal or using all the cards). This helps them see what is going on inside a longer routine.
- **Challenge format:** Concept, guided enhancement. Starter routine has several steps but no clear sign when the important part is done. Students choose where to place a check‑mark or “goal reached” picture. Auto‑grading checks that the check is placed at a reasonable point in the sequence.  
- **CSTA:** E2‑PRO‑TR‑03.

---

## Grade 3

**Note:** Grade 3 debugging skills are now integrated into core programming topics (T06-T09) as contextualized debugging within each construct. Abstract debugging as a formal topic begins in Grade 4.

---

## Grade 4

Grade 4 introduces abstract debugging as a formal topic. Students debug complex programs with iteration and selection, use systematic testing strategies, and compare program designs.

### T13.G4.01 – Debug a conditional inside a loop

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T13.GK.02: Try again when the steps don't work


- **Short name:** Fix an if block inside a loop
- **Description:** Students debug a program where a conditional statement inside a loop doesn't work as expected. The bug might be a wrong condition (e.g., `if touching color red` should be `if touching color blue`), a missing action, or the condition being checked at the wrong time.
- **Challenge format:** Coding, debugging challenge. Starter project: a sprite moves and should earn points whenever it touches a certain color or object, but the condition is incorrect or missing. Students fix the condition or complete the block. Auto‑grading checks the fixed condition and verifies behavior on test runs.
- **CSTA:** E4‑PRO‑TR‑03 (Debug errors in iteration or selection in a program).

### T13.G4.02 – Test edge cases in a simple condition

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T13.GK.02: Try again when the steps don't work


- **Short name:** Test what happens at boundaries
- **Description:** Students consider edge cases for a simple conditional program (e.g., "What happens if the sprite is exactly on the edge?" or "What if the score is 0?") and run the program with those inputs to see if it behaves correctly.
- **Challenge format:** Concept, testing item. Starter project defines a condition (e.g., "bounce if touching the edge") and lists a few test cases (sprite in middle, sprite exactly on edge, sprite just past edge). Students run each test and choose which cases the program handles correctly. Auto‑grading compares results to reference behavior.
- **CSTA:** E4‑PRO‑TR‑03.

### T13.G4.03 – Create an alternative solution to the same problem

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T13.GK.02: Try again when the steps don't work


- **Short name:** Solve the same problem a different way
- **Description:** Given a working program, students redesign it to accomplish the same task using a different approach (e.g., using a different loop structure, rearranging conditions, or using different sprites), then test both versions on the same inputs to confirm they behave the same.
- **Challenge format:** Coding, alternative design. Starter project: a simple game or animation with a reference solution. Prompt: "Modify this program to do the same thing but in a different way, then test both versions with the same moves or inputs." Auto‑grading checks that the final behavior matches the original across tests and that the code structure is genuinely different.
- **CSTA:** E4‑PRO‑TR‑04 (Create alternative versions of a program to solve the same problem or complete the same task).

### T13.G4.04 – Identify and fix an infinite loop or program hang

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Fix a program that doesn't stop
- **Description:** Students recognize that a `forever` or `repeat until` loop is stuck (never exits) and diagnose why (e.g., the condition never becomes true, or the update is missing). They fix the condition or add a stopping mechanism.
- **Challenge format:** Coding, debugging challenge. Starter project includes a loop that hangs or runs endlessly under certain conditions. Students run it, observe it doesn't stop, then modify the condition or add a break. Auto‑grading checks that the script now terminates within a reasonable time.
- **CSTA:** E4‑PRO‑TR‑03.

### T13.G4.05 – Use systematic testing with multiple test cases

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Test a program with different inputs
- **Description:** Students write or follow a simple test plan: a list of inputs and expected outputs. They run the program with each test case and check if results match expectations, recording passes and failures.
- **Challenge format:** Coding and concept, testing checklist. Starter project: a simple calculator or game with a provided test plan (e.g., "Input: 2 + 3, Expected: 5; Input: 10 − 3, Expected: 7"). Students run each test case and choose which passed or failed. Auto‑grading checks the test results against reference behavior.
- **CSTA:** E4‑PRO‑TR‑03 (Debug errors in a program that includes sequence, events, iteration, and selection).

### T13.G4.06 – Compare two programs solving the same task

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Choose the better version of a program
- **Description:** Students examine two different programs that both accomplish the same goal but may have different structure, efficiency, or robustness. They decide which version would be easier to test, debug, and reuse (e.g., clearer structure, fewer special‑case bugs, helpful messages) and explain why.
- **Challenge format:** Concept, comparison and explanation. Show two short scripts that both solve the same problem (e.g., move a sprite in a square or keep score in a mini‑game). Ask questions like "Which program would be easier to test and fix if something went wrong?" or "Which is less likely to hide bugs?" Students select one and give a reason. Auto‑grading scores the choice and checks for reasoning that mentions clarity, structure, or error handling.
- **CSTA:** E4‑PRO‑TR‑04 (Compare programs that complete a similar task and determine which would be easiest to repurpose).

### T13.G4.07 – Debug a complex loop with nested structures

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Fix a bug in nested loops or conditionals
- **Description:** Students debug a script containing nested loops or multiple conditionals (e.g., a loop inside a loop with a condition inside) where the bug affects the overall behavior. They identify the incorrect level or operator and fix it.
- **Challenge format:** Coding, debugging challenge. Starter project: a pattern‑drawing or game script with nested structure and a subtle bug (e.g., condition in the wrong loop level, or counter not updating at the right scope). Students fix the code. Auto‑grading checks the corrected structure and verifies behavior.
- **CSTA:** E4‑PRO‑TR‑03.

### T13.G4.08 – Document the steps you took to find and fix a bug

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Explain how you debugged a program
- **Description:** After finding and fixing a bug, students write a short explanation: what the bug was, what symptoms they saw, what they tried, and how they confirmed the fix worked. This metacognitive reflection reinforces debugging practice.
- **Challenge format:** Concept, guided reflection. After fixing a bug in a coding challenge, students answer structured prompts (e.g., "What was wrong?" "How did you know?" "What did you change?" "How did you test it?") with short text responses or sentence starters. Auto‑grading checks that responses reference the bug, the testing process, and the fix.
- **CSTA:** E4‑PRO‑TR‑03.

---

## Grade 5

Grade 5 students debug more sophisticated programs, use systematic strategies like tracing, and think about error handling and edge cases.

### T13.G5.01 – Debug programs using tracing and logging

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T09.G3.01: Create and use a numeric variable for score or count
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Use debug output to find bugs
- **Description:** Students intentionally add `say` blocks, a “debug helper” sprite, or output variables at key points in a program to trace the execution and reveal what's happening (variable values, which branch is taken, how many times a loop runs). They use this information to locate and fix bugs.
- **Challenge format:** Coding, debugging challenge. Starter project: a program with a subtle bug that's hard to spot by running alone (e.g., a variable doesn't increase when expected, or a condition is checked at the wrong time). Students add fun debug output (like a helper sprite that announces values) to log what's happening, identify the issue, then remove or comment out the debug blocks. Auto‑grading checks that debug output appears during debugging and that the final program is corrected.
- **CSTA:** E5‑PRO‑TR‑03 (Debug programs, using systematic strategies to ensure they run as intended).

### T13.G5.02 – Handle invalid or edge case input

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Prevent errors from bad input
- **Description:** Students design a program that accepts user input and add checks to reject invalid entries or handle edge cases gracefully (e.g., if a player enters a negative number when a positive is required, the program should ask again or default safely instead of crashing or behaving weirdly).
- **Challenge format:** Coding, input-validation challenge. Starter project: a simple game or tool that asks the user for a number (e.g., "Pick a number from 1 to 10"). Students add an `if` block to check if the input is in range, and if not, re-prompt or use a safe default. Auto‑grading tests with valid and invalid inputs and checks for appropriate handling.
- **CSTA:** E5‑PRO‑TR‑03, ALG‑IM (input correctness).

### T13.G5.03 – Create and follow a test plan

_Dependency:_
  * T01.G3.01: Complete a simple script with missing blocks
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Write a test plan and use it
- **Description:** Students design a test plan that lists multiple test cases (normal, boundary, and invalid inputs) for a program, then systematically run each test, record results, and document any failures.
- **Challenge format:** Coding and concept, test planning. Starter project: a simple program (e.g., a score calculator or game). Prompt: "List 5 test cases that would check if this program works correctly. Run each test and record which passed." Students fill in a table or checklist, run tests, and mark results. Auto‑grading checks that test cases cover normal, boundary, and possibly invalid scenarios, and verifies results are recorded accurately.
- **CSTA:** E5‑PRO‑TR‑03.

### T13.G5.04 – Modify a program to improve reliability and correctness

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T13.G1.01: Identify where a step is wrong
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Refactor for correctness and robustness
- **Description:** Students take a working but fragile program (one that handles only happy-path cases) and refactor it to handle more edge cases, reduce duplication, or make it less error-prone. They test the improved version.
- **Challenge format:** Coding, refactor challenge. Starter project: a program that works for typical cases but fails on edge cases or has redundant checks. Prompt: "Improve this program so it works correctly for all inputs." Students add error handling, remove duplication, improve clarity. Auto‑grading runs a comprehensive test suite including edge cases and checks that the refactored program passes more tests than the original.
- **CSTA:** E5‑PRO‑TR‑03.

---

## Grade 6

In middle school, debugging becomes a formal practice with structured approaches, and students reason about algorithmic correctness.

### T13.G6.01 – Trace complex code with multiple variables

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Trace code and track variable changes
- **Description:** Students step through a program with multiple variables and complex logic, tracking how each variable changes at each step. They use a table or mental model to predict the final state and verify correctness.
- **Challenge format:** Concept, code‑tracing item. Show a script with 2–3 variables and several steps (e.g., assignments, conditions, loops). Students trace through and answer questions like "What is the value of `x` after the loop?" or "What will the sprite say at the end?" with numeric or text answers. Auto‑grading compares to simulation.
- **CSTA:** MS‑PRO‑TR‑11 (Use standard practices to test, debug, document, and peer-review code).

### T13.G6.02 – Use a systematic debugging process

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T13.G1.01: Identify where a step is wrong
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Use a debugging checklist
- **Description:** Students apply a structured debugging method: observe symptoms, form a hypothesis about the cause, test the hypothesis by adding debug output or modifying code, and verify the fix. This replaces trial-and-error with strategy.
- **Challenge format:** Coding, guided debugging with a checklist. Starter project: a program with a bug. Prompt guides students through steps: (1) "What should the program do?" (2) "What does it actually do?" (3) "Where might the problem be?" (4) "Add debug output to check." (5) "Fix it." (6) "Run the test again." Auto‑grading checks that the student completes the process and that the bug is fixed.
- **CSTA:** MS‑PRO‑TR‑11.

### T13.G6.03 – Test code with boundary and invalid inputs

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Test edge cases and bad inputs
- **Description:** Students design and run tests that deliberately use boundary values (e.g., 0, negative numbers, very large numbers) and invalid inputs to ensure a program handles all cases without crashing or producing wrong results.
- **Challenge format:** Coding and concept, test design and execution. Starter project: a program with a function or calculation (e.g., age calculator, converter). Students identify boundary and invalid cases (e.g., negative age, age 0, age 150), run tests with these inputs, and report results. Auto‑grading checks that they tested appropriate edge cases and that results are correct.
- **CSTA:** MS‑PRO‑TR‑11.

### T13.G6.04 – Document known limitations and potential bugs

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T13.G1.01: Identify where a step is wrong
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Write about what your program doesn't do
- **Description:** Students examine their program and document cases or inputs it doesn't handle correctly, potential future bugs, or design limitations. This self-aware documentation reflects mature debugging thinking.
- **Challenge format:** Concept, guided documentation. After creating a program, students fill in a short form: "What inputs or situations might break this program?" "What could be improved?" Auto‑grading checks that the documented issues are realistic and specific to the code.
- **CSTA:** MS‑PRO‑TR‑11.

---

## Grade 7

Grade 7 students apply testing and debugging to increasingly complex algorithms and simulations, and think critically about program design correctness.

### T13.G7.01 – Write comprehensive test cases for an algorithm

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Create tests for all algorithm cases
- **Description:** Students analyze an algorithm (e.g., finding the maximum in a list, checking if a number is prime) and write a thorough test suite covering normal cases, edge cases (e.g., empty list, single item, boundary values), and invalid inputs. They run all tests and record coverage.
- **Challenge format:** Coding and concept, test suite design. Starter project: a program implementing an algorithm. Prompt: "Write at least 8 test cases that would thoroughly test this algorithm." Students list inputs and expected outputs, run the tests, and mark which pass/fail. Auto‑grading evaluates the breadth of test coverage (normal, edge, invalid) and checks that tests are actually run.
- **CSTA:** MS‑PRO‑TR‑11, MS‑ALG‑AF‑02 (algorithm verification).

### T13.G7.02 – Debug logic errors in complex programs

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Find and fix logic bugs
- **Description:** Students identify and correct logic errors in a program (bugs that don't crash the program but produce wrong results, such as off-by-one errors, incorrect operators, or wrong variable assignments). These are harder to spot than syntax errors.
- **Challenge format:** Coding, debugging challenge. Starter project: a simulation or calculation with a subtle logic error (e.g., a loop that runs n+1 times instead of n, or a wrong comparison operator). The program runs but gives incorrect results. Students debug using tracing and testing. Auto‑grading checks the fixed code and verifies correct behavior on test cases.
- **CSTA:** MS‑PRO‑TR‑11.

### T13.G7.03 – Refactor for testability and clarity

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Improve code so it's easier to test and debug
- **Description:** Students refactor a program to reduce complexity, improve clarity, and make testing easier (e.g., breaking large scripts into smaller functions, naming variables clearly, removing duplicated code). They then verify the refactored version still works.
- **Challenge format:** Coding, refactoring challenge. Starter project: a working program that is complex, repetitive, or uses unclear names. Prompt: "Refactor this program to make it easier to understand and test." Students clean up code, add comments, and test. Auto‑grading checks that the refactored version produces the same behavior and is genuinely improved.
- **CSTA:** MS‑PRO‑TR‑11, PRO‑PM.

### T13.G7.04 – Compare reliability of different program designs

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T13.G1.01: Identify where a step is wrong
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Analyze programs for robustness
- **Description:** Students examine two or more designs for the same task, evaluate their handling of edge cases and error conditions, and argue which is more reliable and why.
- **Challenge format:** Concept, analysis and comparison. Show two program designs (e.g., two different sorting algorithms, or two input validation approaches). Ask students to evaluate each for robustness with various inputs and edge cases, then choose which is more reliable with justification. Auto‑grading scores the selection and validates reasoning.
- **CSTA:** MS‑PRO‑TR‑11, MS‑ALG‑AF‑02.

---

## Grade 8

Grade 8 students think like computer scientists, using rigorous testing to verify program correctness, considering program specifications, and reasoning about accuracy and bias.

### T13.G8.01 – Design and execute a rigorous test suite

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T13.G1.01: Identify where a step is wrong
  * T13.G1.02: Fix a sequence error in steps
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Create comprehensive test cases with coverage reporting
- **Description:** Students design a test suite that explicitly covers all code paths and critical scenarios, run the tests systematically, and document coverage (e.g., how many branches were tested, how many edge cases). They track which tests pass and fail.
- **Challenge format:** Coding and concept, test suite design with documentation. Starter project: a program with multiple branches and conditions. Prompt: "Design a test suite that covers every branch and every edge case. Document which tests pass and which fail." Students create a list of tests (ideally in a table or spreadsheet), run them, and report results. Auto‑grading evaluates coverage breadth, test quality, and documentation.
- **CSTA:** MS‑PRO‑TR‑11, MS‑PRO‑TR‑12.

### T13.G8.02 – Debug for correctness against specifications

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T13.G1.01: Identify where a step is wrong
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Verify program matches its specification
- **Description:** Given a formal (or semi-formal) specification of a program's expected behavior, students test the implementation against it, identify discrepancies, and fix bugs until the program matches the specification.
- **Challenge format:** Coding, specification-based debugging. Starter project: a program and a specification document (e.g., "The program should accept numbers from 1 to 100, compute the sum, and display it"). Students test the implementation against the specification, identify any deviations, and fix them. Auto‑grading checks that the program matches the spec on a suite of test cases.
- **CSTA:** MS‑PRO‑TR‑12 (Verify that a program performs according to its design specifications).

### T13.G8.03 – Handle errors gracefully with try-and-catch patterns

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T13.G1.01: Identify where a step is wrong
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Use error handling blocks
- **Description:** Students add error-handling logic (e.g., checking for valid input, handling cases where operations might fail) to make a program robust. They prevent crashes and ensure graceful degradation or user-friendly error messages.
- **Challenge format:** Coding, error-handling challenge. Starter project: a program that might encounter errors (division by zero, invalid list access, missing input). Prompt: "Add checks and error messages so the program never crashes." Students add conditional guards and helpful feedback. Auto‑grading tests with error conditions and checks that the program handles them without crashing and with appropriate messages.
- **CSTA:** MS‑PRO‑TR‑12.

### T13.G8.04 – Reflect on accuracy, bias, and quality of generated code

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T13.G1.01: Identify where a step is wrong
  * T13.GK.02: Try again when the steps don't work
  * T13.GK.03: Fix a single wrong direction or action in steps


- **Short name:** Evaluate code for correctness and bias
- **Description:** Students review code (either their own or AI-generated) and consider questions like: Does it correctly solve the stated problem? Are there edge cases it misses? Could it introduce bias or unintended harm? What assumptions does it make? This critical analysis develops higher-order thinking about code quality.
- **Challenge format:** Concept, reflective analysis. Starter: show a program or code snippet and a description of its intended task. Students answer reflection prompts: "Does this code correctly do what it claims?" "What edge cases might it miss?" "Could this code be biased or harmful?" "What assumptions does it make?" with short written or selected responses. Auto‑grading checks that responses demonstrate critical evaluation and reference specific code or scenarios.
- **CSTA:** MS‑PRO‑TR‑13 (Describe issues of accuracy and bias in computer-generated code).

---

### Notes on Dependencies and Alignment

**Editor Notes:**
- K–2 foundations: Picture‑based debugging activities about "try–check–fix" habits and spotting/fixing mistakes in everyday step sequences are unplugged/light‑digital with no blocks or code terms.
- G3: Grade 3 debugging skills have been moved to be integrated within core programming topics (T06-T09) as contextualized debugging within each construct. This teaches debugging as a natural part of learning each new construct rather than as a separate abstract topic.
- G4–5: Abstract debugging as a formal topic begins in G4, with highest density of coding‑based debugging skills for loops, conditionals, and variables, plus concrete test‑case design and basic error handling.
- G6–8: Higher‑order skills around systematic debugging processes, algorithm verification, robustness, and reasoning about accuracy and bias (including AI‑generated code).
- The approach of contextualizing G3 debugging within construct topics (e.g., T07.G3.05 "Fix a loop that runs too many times", T08.G3.05 "Fix wrong comparison operator", T09.G3.03 "Fix missing variable update") teaches debugging as a natural part of learning rather than as abstract skill.
- This design aligns with CSTA PRO‑TR expectations while managing G3 cognitive load effectively and keeping skills small, progressive, and CreatiCode‑implementable.
