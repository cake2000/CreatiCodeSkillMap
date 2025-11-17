# T13 – Testing, Debugging & Error Handling: K–8 Skill List (Draft v1)

Topic reference: `T13 Testing, Debugging & Error Handling` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑TR (Testing and Refinement)

Each skill below has:

- a stable **ID** (`T13.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

At this stage, students begin recognizing that programs might not work and need fixing. Debugging is intuitive: spotting obvious mistakes in sequences and simple animations.

### T13.GK.01 – Spot a missing or wrong action

- **Short name:** Find what's wrong in a simple sequence
- **Description:** Students watch a short animation or look at a simple script and identify that something is obviously missing or incorrect (e.g., the character should jump but doesn't, or moves the wrong direction). They point to the error without needing to fix it yet.
- **Challenge format:** Concept, visual matching. Show a script and a video of what should happen vs. what does happen. Students choose which block is wrong or missing from several pictures. Auto‑grading checks the selected item.
- **CSTA:** EK‑PRO‑TR‑04 (Identify errors in programs that do not work as expected).

### T13.GK.02 – Try again when a program doesn't work

- **Short name:** Test and see if the program works
- **Description:** Students run a program, observe that it did something unexpected or incomplete, and experience the idea of "test, check, then try to fix." They may not yet understand the fix, but they learn the test‑and‑observe cycle.
- **Challenge format:** Concept, guided exploration. A starter project has a simple script with an obvious error. The system prompts: "Click the green flag. Does the cat do what you wanted? No? Let's look at the blocks." Auto‑grading tracks that the student ran the project and proceeded to code view.
- **CSTA:** EK‑PRO‑TR‑04.

### T13.GK.03 – Fix a single wrong direction or action

- **Short name:** Fix the wrong move direction
- **Description:** Given a script where a sprite moves in the wrong direction (e.g., left instead of right), students change the block's parameter or replace it with the correct direction block. This is the first hands‑on fix.
- **Challenge format:** Coding, guided fix. Starter project: a sprite should move right, but the block says "move left 10." Prompt: "Change the move to go the right way." Auto‑grading checks that the block is corrected and that running the project shows the sprite moving right.
- **CSTA:** EK‑PRO‑TR‑04.

---

## Grade 1

Grade 1 students begin more intentional debugging: identifying the bug's location, understanding sequence errors, and making deliberate fixes.

### T13.G1.01 – Identify where an error is in a script

- **Short name:** Point out the wrong block
- **Description:** Students examine a script where a sequence is out of order or a block is obviously wrong (e.g., "jump before moving" when the intent is move-then-jump). They select or highlight the incorrect block without yet fixing it.
- **Challenge format:** Concept, multiple choice or highlighting. Show a script and ask "Which block is in the wrong place?" or "Which block should not be there?" Students choose from highlighted regions. Auto‑grading checks the selection against reference.
- **CSTA:** E1‑PRO‑TR‑03 (Debug a program that includes sequence and events to correct errors).

### T13.G1.02 – Fix a sequence error

- **Short name:** Put the blocks in the right order
- **Description:** Students reorder blocks in a script to fix a sequencing error. For example, they rearrange so that "say hello" happens before "jump" instead of after, or move a `wait` block to the correct position.
- **Challenge format:** Coding, drag-and-drop reorder. Starter project shows a script in the wrong order; students drag blocks to reorder them. Auto‑grading checks the final sequence against the intended order and runs the project to verify behavior.
- **CSTA:** E1‑PRO‑TR‑03.

### T13.G1.03 – Change a parameter to fix behavior

- **Short name:** Fix a number or value in a block
- **Description:** Students modify a numeric parameter (e.g., change "move 100 steps" to "move 50 steps" to make a sprite stop in a better spot, or change a wait duration) to correct unexpected behavior.
- **Challenge format:** Coding, guided parameter edit. Starter project: a sprite moves too far or waits too long. Prompt: "The cat should only move 50 steps. Change the number." Auto‑grading checks the modified value and that running the project now matches the expected behavior.
- **CSTA:** E1‑PRO‑TR‑03.

### T13.G1.04 – Run a program and report what went wrong

- **Short name:** Test a program and say what's wrong
- **Description:** Students click the green flag, watch what happens, and explain (in words, pictures, or simple text) what did not match expectations or what's missing.
- **Challenge format:** Concept, guided observation + response. Starter project runs a simple script with a deliberate error. Prompt: "What did the cat do wrong?" with answer choices (e.g., "jumped instead of spinning," "moved left instead of right"). Auto‑grading checks the selected or typed observation.
- **CSTA:** E1‑PRO‑TR‑03.

---

## Grade 2

Grade 2 students debug programs with more complex structure (events, iteration). They use systematic approaches: testing, isolating problems, and trying fixes.

### T13.G2.01 – Debug an event handler

- **Short name:** Fix a program that doesn't respond to input
- **Description:** Students examine a script where a sprite should respond to a key press or click, but doesn't. The bug might be a missing `when key pressed` block or an incorrect key. They identify and fix the event handler.
- **Challenge format:** Coding, guided debugging. Starter project: expected behavior is "When you press the space bar, the cat jumps." The script is missing the event handler or has the wrong key. Students add or correct the block. Auto‑grading checks the event and runs the project to verify the sprite responds correctly.
- **CSTA:** E2‑PRO‑TR‑03 (Debug errors in programs that include sequence, events, and iteration).

### T13.G2.02 – Trace a script and predict behavior

- **Short name:** Follow the blocks and say what will happen
- **Description:** Students "walk through" a simple script step by step, predicting what each block does and what the sprite will look like at the end. This mental tracing helps them spot logic errors before running.
- **Challenge format:** Concept, tracing item. Show a script with 4–6 blocks; ask "What will the cat do?" or "Where will the cat be at the end?" with picture or multiple-choice answers. Auto‑grading compares the answer to simulation.
- **CSTA:** E2‑PRO‑TR‑03.

### T13.G2.03 – Fix a loop that doesn't repeat correctly

- **Short name:** Fix the repeat count or loop structure
- **Description:** Students modify a script where a `repeat` loop doesn't run the correct number of times (e.g., repeats 2 times instead of 5, or the condition in a `repeat until` is wrong). They change the count or condition.
- **Challenge format:** Coding, debugging challenge. Starter project: a sprite should jump 5 times but only jumps 3 times (or the repeat count is clearly wrong). Students fix the loop count or structure. Auto‑grading checks the corrected count and verifies behavior.
- **CSTA:** E2‑PRO‑TR‑03.

### T13.G2.04 – Add a test with a debug sprite

- **Short name:** Use a helper sprite to check what's happening
- **Description:** Students add a small sprite (e.g., a thought bubble or debug sprite) that displays the value of a variable or a simple test message at a key point in the script. This helps them see what's going on internally.
- **Challenge format:** Coding, guided enhancement. Starter project has a simple game or animation with a variable (e.g., score, counter). Students add a `say` block or debug sprite that shows the variable's value at a critical moment (e.g., after a collision). Auto‑grading checks that the debug output appears and reflects the correct value at that moment.
- **CSTA:** E2‑PRO‑TR‑03.

---

## Grade 3

Grade 3 students debug more complex programs with iteration and selection. They create alternative versions and reason about different designs.

### T13.G3.01 – Debug a conditional inside a loop

- **Short name:** Fix an if block inside a loop
- **Description:** Students debug a program where a conditional statement inside a loop doesn't work as expected. The bug might be a wrong condition (e.g., `if touching color red` should be `if touching color blue`), a missing action, or the condition being checked at the wrong time.
- **Challenge format:** Coding, debugging challenge. Starter project: a sprite moves and should earn points whenever it touches a certain color or object, but the condition is incorrect or missing. Students fix the condition or complete the block. Auto‑grading checks the fixed condition and verifies behavior on test runs.
- **CSTA:** E3‑PRO‑TR‑03 (Debug errors in iteration or selection in a program).

### T13.G3.02 – Test edge cases in a simple condition

- **Short name:** Test what happens at boundaries
- **Description:** Students consider edge cases for a simple conditional program (e.g., "What happens if the sprite is exactly on the edge?" or "What if the score is 0?") and run the program with those inputs to see if it behaves correctly.
- **Challenge format:** Concept, testing item. Starter project defines a condition (e.g., "bounce if touching the edge") and lists a few test cases (sprite in middle, sprite exactly on edge, sprite just past edge). Students run each test and choose which cases the program handles correctly. Auto‑grading compares results to reference behavior.
- **CSTA:** E3‑PRO‑TR‑03.

### T13.G3.03 – Create an alternative solution to the same problem

- **Short name:** Solve the same problem a different way
- **Description:** Given a working program, students redesign it to accomplish the same task using a different approach (e.g., using a different loop structure, rearranging conditions, or using different sprites). Both versions should produce the same result.
- **Challenge format:** Coding, alternative design. Starter project: a simple game or animation with a reference solution. Prompt: "Modify this program to do the same thing but in a different way." Auto‑grading checks that the final behavior matches the original and that the code structure is genuinely different.
- **CSTA:** E3‑PRO‑TR‑04 (Create alternative versions of a program to solve the same problem or complete the same task).

### T13.G3.04 – Identify and fix an infinite loop or program hang

- **Short name:** Fix a program that doesn't stop
- **Description:** Students recognize that a `forever` or `repeat until` loop is stuck (never exits) and diagnose why (e.g., the condition never becomes true, or the update is missing). They fix the condition or add a stopping mechanism.
- **Challenge format:** Coding, debugging challenge. Starter project includes a loop that hangs or runs endlessly under certain conditions. Students run it, observe it doesn't stop, then modify the condition or add a break. Auto‑grading checks that the script now terminates within a reasonable time.
- **CSTA:** E3‑PRO‑TR‑03.

---

## Grade 4

Grade 4 students use more systematic debugging strategies, compare program designs, and handle errors in more complex scripts.

### T13.G4.01 – Use systematic testing with multiple test cases

- **Short name:** Test a program with different inputs
- **Description:** Students write or follow a simple test plan: a list of inputs and expected outputs. They run the program with each test case and check if results match expectations, recording passes and failures.
- **Challenge format:** Coding and concept, testing checklist. Starter project: a simple calculator or game with a provided test plan (e.g., "Input: 2 + 3, Expected: 5; Input: 10 − 3, Expected: 7"). Students run each test case and choose which passed or failed. Auto‑grading checks the test results against reference behavior.
- **CSTA:** E4‑PRO‑TR‑03 (Debug errors in a program that includes sequence, events, iteration, and selection).

### T13.G4.02 – Compare two programs solving the same task

- **Short name:** Choose the better version of a program
- **Description:** Students examine two different programs that both accomplish the same goal but may have different structure, efficiency, or maintainability. They explain which is better and why (e.g., easier to read, more concise, fewer bugs).
- **Challenge format:** Concept, comparison and explanation. Show two short scripts that both solve the same problem (e.g., move a sprite in a square). Ask "Which program is easier to understand?" or "Which has less repeated code?" Students select one and give a reason. Auto‑grading scores the choice and checks for relevant reasoning.
- **CSTA:** E4‑PRO‑TR‑04 (Compare programs that complete a similar task and determine which would be easiest to repurpose).

### T13.G4.03 – Debug a complex loop with nested structures

- **Short name:** Fix a bug in nested loops or conditionals
- **Description:** Students debug a script containing nested loops or multiple conditionals (e.g., a loop inside a loop with a condition inside) where the bug affects the overall behavior. They identify the incorrect level or operator and fix it.
- **Challenge format:** Coding, debugging challenge. Starter project: a pattern‑drawing or game script with nested structure and a subtle bug (e.g., condition in the wrong loop level, or counter not updating at the right scope). Students fix the code. Auto‑grading checks the corrected structure and verifies behavior.
- **CSTA:** E4‑PRO‑TR‑03.

### T13.G4.04 – Document the steps you took to find and fix a bug

- **Short name:** Explain how you debugged a program
- **Description:** After finding and fixing a bug, students write a short explanation: what the bug was, what symptoms they saw, what they tried, and how they confirmed the fix worked. This metacognitive reflection reinforces debugging practice.
- **Challenge format:** Concept, guided reflection. After fixing a bug in a coding challenge, students answer structured prompts (e.g., "What was wrong?" "How did you know?" "What did you change?" "How did you test it?") with short text responses or sentence starters. Auto‑grading checks that responses reference the bug, the testing process, and the fix.
- **CSTA:** E4‑PRO‑TR‑03.

---

## Grade 5

Grade 5 students debug more sophisticated programs, use systematic strategies like tracing, and think about error handling and edge cases.

### T13.G5.01 – Debug programs using tracing and logging

- **Short name:** Use debug output to find bugs
- **Description:** Students intentionally add `say` blocks or output variables at key points in a program to trace the execution and reveal what's happening (variable values, which branch is taken, how many times a loop runs). They use this information to locate and fix bugs.
- **Challenge format:** Coding, debugging challenge. Starter project: a program with a subtle bug that's hard to spot by running alone (e.g., a variable doesn't increase when expected, or a condition is checked at the wrong time). Students add debug output blocks to log what's happening, identify the issue, then remove or comment out the debug blocks. Auto‑grading checks that debug output appears and that the final program is corrected.
- **CSTA:** E5‑PRO‑TR‑03 (Debug programs, using systematic strategies to ensure they run as intended).

### T13.G5.02 – Handle invalid or edge case input

- **Short name:** Prevent errors from bad input
- **Description:** Students design a program that accepts user input and add checks to reject invalid entries or handle edge cases gracefully (e.g., if a player enters a negative number when a positive is required, the program should ask again or default safely instead of crashing or behaving weirdly).
- **Challenge format:** Coding, input-validation challenge. Starter project: a simple game or tool that asks the user for a number (e.g., "Pick a number from 1 to 10"). Students add an `if` block to check if the input is in range, and if not, re-prompt or use a safe default. Auto‑grading tests with valid and invalid inputs and checks for appropriate handling.
- **CSTA:** E5‑PRO‑TR‑03, ALG‑IM (input correctness).

### T13.G5.03 – Create and follow a test plan

- **Short name:** Write a test plan and use it
- **Description:** Students design a test plan that lists multiple test cases (normal, boundary, and invalid inputs) for a program, then systematically run each test, record results, and document any failures.
- **Challenge format:** Coding and concept, test planning. Starter project: a simple program (e.g., a score calculator or game). Prompt: "List 5 test cases that would check if this program works correctly. Run each test and record which passed." Students fill in a table or checklist, run tests, and mark results. Auto‑grading checks that test cases cover normal, boundary, and possibly invalid scenarios, and verifies results are recorded accurately.
- **CSTA:** E5‑PRO‑TR‑03.

### T13.G5.04 – Modify a program to improve reliability and correctness

- **Short name:** Refactor for correctness and robustness
- **Description:** Students take a working but fragile program (one that handles only happy-path cases) and refactor it to handle more edge cases, reduce duplication, or make it less error-prone. They test the improved version.
- **Challenge format:** Coding, refactor challenge. Starter project: a program that works for typical cases but fails on edge cases or has redundant checks. Prompt: "Improve this program so it works correctly for all inputs." Students add error handling, remove duplication, improve clarity. Auto‑grading runs a comprehensive test suite including edge cases and checks that the refactored program passes more tests than the original.
- **CSTA:** E5‑PRO‑TR‑03.

---

## Grade 6

In middle school, debugging becomes a formal practice with structured approaches, and students reason about algorithmic correctness.

### T13.G6.01 – Trace complex code with multiple variables

- **Short name:** Trace code and track variable changes
- **Description:** Students step through a program with multiple variables and complex logic, tracking how each variable changes at each step. They use a table or mental model to predict the final state and verify correctness.
- **Challenge format:** Concept, code‑tracing item. Show a script with 2–3 variables and several steps (e.g., assignments, conditions, loops). Students trace through and answer questions like "What is the value of `x` after the loop?" or "What will the sprite say at the end?" with numeric or text answers. Auto‑grading compares to simulation.
- **CSTA:** MS‑PRO‑TR‑11 (Use standard practices to test, debug, document, and peer-review code).

### T13.G6.02 – Use a systematic debugging process

- **Short name:** Use a debugging checklist
- **Description:** Students apply a structured debugging method: observe symptoms, form a hypothesis about the cause, test the hypothesis by adding debug output or modifying code, and verify the fix. This replaces trial-and-error with strategy.
- **Challenge format:** Coding, guided debugging with a checklist. Starter project: a program with a bug. Prompt guides students through steps: (1) "What should the program do?" (2) "What does it actually do?" (3) "Where might the problem be?" (4) "Add debug output to check." (5) "Fix it." (6) "Run the test again." Auto‑grading checks that the student completes the process and that the bug is fixed.
- **CSTA:** MS‑PRO‑TR‑11.

### T13.G6.03 – Test code with boundary and invalid inputs

- **Short name:** Test edge cases and bad inputs
- **Description:** Students design and run tests that deliberately use boundary values (e.g., 0, negative numbers, very large numbers) and invalid inputs to ensure a program handles all cases without crashing or producing wrong results.
- **Challenge format:** Coding and concept, test design and execution. Starter project: a program with a function or calculation (e.g., age calculator, converter). Students identify boundary and invalid cases (e.g., negative age, age 0, age 150), run tests with these inputs, and report results. Auto‑grading checks that they tested appropriate edge cases and that results are correct.
- **CSTA:** MS‑PRO‑TR‑11.

### T13.G6.04 – Document known limitations and potential bugs

- **Short name:** Write about what your program doesn't do
- **Description:** Students examine their program and document cases or inputs it doesn't handle correctly, potential future bugs, or design limitations. This self-aware documentation reflects mature debugging thinking.
- **Challenge format:** Concept, guided documentation. After creating a program, students fill in a short form: "What inputs or situations might break this program?" "What could be improved?" Auto‑grading checks that the documented issues are realistic and specific to the code.
- **CSTA:** MS‑PRO‑TR‑11.

---

## Grade 7

Grade 7 students apply testing and debugging to increasingly complex algorithms and simulations, and think critically about program design correctness.

### T13.G7.01 – Write comprehensive test cases for an algorithm

- **Short name:** Create tests for all algorithm cases
- **Description:** Students analyze an algorithm (e.g., finding the maximum in a list, checking if a number is prime) and write a thorough test suite covering normal cases, edge cases (e.g., empty list, single item, boundary values), and invalid inputs. They run all tests and record coverage.
- **Challenge format:** Coding and concept, test suite design. Starter project: a program implementing an algorithm. Prompt: "Write at least 8 test cases that would thoroughly test this algorithm." Students list inputs and expected outputs, run the tests, and mark which pass/fail. Auto‑grading evaluates the breadth of test coverage (normal, edge, invalid) and checks that tests are actually run.
- **CSTA:** MS‑PRO‑TR‑11, MS‑ALG‑AF‑02 (algorithm verification).

### T13.G7.02 – Debug logic errors in complex programs

- **Short name:** Find and fix logic bugs
- **Description:** Students identify and correct logic errors in a program (bugs that don't crash the program but produce wrong results, such as off-by-one errors, incorrect operators, or wrong variable assignments). These are harder to spot than syntax errors.
- **Challenge format:** Coding, debugging challenge. Starter project: a simulation or calculation with a subtle logic error (e.g., a loop that runs n+1 times instead of n, or a wrong comparison operator). The program runs but gives incorrect results. Students debug using tracing and testing. Auto‑grading checks the fixed code and verifies correct behavior on test cases.
- **CSTA:** MS‑PRO‑TR‑11.

### T13.G7.03 – Refactor for testability and clarity

- **Short name:** Improve code so it's easier to test and debug
- **Description:** Students refactor a program to reduce complexity, improve clarity, and make testing easier (e.g., breaking large scripts into smaller functions, naming variables clearly, removing duplicated code). They then verify the refactored version still works.
- **Challenge format:** Coding, refactoring challenge. Starter project: a working program that is complex, repetitive, or uses unclear names. Prompt: "Refactor this program to make it easier to understand and test." Students clean up code, add comments, and test. Auto‑grading checks that the refactored version produces the same behavior and is genuinely improved.
- **CSTA:** MS‑PRO‑TR‑11, PRO‑PM.

### T13.G7.04 – Compare reliability of different program designs

- **Short name:** Analyze programs for robustness
- **Description:** Students examine two or more designs for the same task, evaluate their handling of edge cases and error conditions, and argue which is more reliable and why.
- **Challenge format:** Concept, analysis and comparison. Show two program designs (e.g., two different sorting algorithms, or two input validation approaches). Ask students to evaluate each for robustness with various inputs and edge cases, then choose which is more reliable with justification. Auto‑grading scores the selection and validates reasoning.
- **CSTA:** MS‑PRO‑TR‑11, MS‑ALG‑AF‑02.

---

## Grade 8

Grade 8 students think like computer scientists, using rigorous testing to verify program correctness, considering program specifications, and reasoning about accuracy and bias.

### T13.G8.01 – Design and execute a rigorous test suite

- **Short name:** Create comprehensive test cases with coverage reporting
- **Description:** Students design a test suite that explicitly covers all code paths and critical scenarios, run the tests systematically, and document coverage (e.g., how many branches were tested, how many edge cases). They track which tests pass and fail.
- **Challenge format:** Coding and concept, test suite design with documentation. Starter project: a program with multiple branches and conditions. Prompt: "Design a test suite that covers every branch and every edge case. Document which tests pass and which fail." Students create a list of tests (ideally in a table or spreadsheet), run them, and report results. Auto‑grading evaluates coverage breadth, test quality, and documentation.
- **CSTA:** MS‑PRO‑TR‑11, MS‑PRO‑TR‑12.

### T13.G8.02 – Debug for correctness against specifications

- **Short name:** Verify program matches its specification
- **Description:** Given a formal (or semi-formal) specification of a program's expected behavior, students test the implementation against it, identify discrepancies, and fix bugs until the program matches the specification.
- **Challenge format:** Coding, specification-based debugging. Starter project: a program and a specification document (e.g., "The program should accept numbers from 1 to 100, compute the sum, and display it"). Students test the implementation against the specification, identify any deviations, and fix them. Auto‑grading checks that the program matches the spec on a suite of test cases.
- **CSTA:** MS‑PRO‑TR‑12 (Verify that a program performs according to its design specifications).

### T13.G8.03 – Handle errors gracefully with try-and-catch patterns

- **Short name:** Use error handling blocks
- **Description:** Students add error-handling logic (e.g., checking for valid input, handling cases where operations might fail) to make a program robust. They prevent crashes and ensure graceful degradation or user-friendly error messages.
- **Challenge format:** Coding, error-handling challenge. Starter project: a program that might encounter errors (division by zero, invalid list access, missing input). Prompt: "Add checks and error messages so the program never crashes." Students add conditional guards and helpful feedback. Auto‑grading tests with error conditions and checks that the program handles them without crashing and with appropriate messages.
- **CSTA:** MS‑PRO‑TR‑12.

### T13.G8.04 – Reflect on accuracy, bias, and quality of generated code

- **Short name:** Evaluate code for correctness and bias
- **Description:** Students review code (either their own or AI-generated) and consider questions like: Does it correctly solve the stated problem? Are there edge cases it misses? Could it introduce bias or unintended harm? What assumptions does it make? This critical analysis develops higher-order thinking about code quality.
- **Challenge format:** Concept, reflective analysis. Starter: show a program or code snippet and a description of its intended task. Students answer reflection prompts: "Does this code correctly do what it claims?" "What edge cases might it miss?" "Could this code be biased or harmful?" "What assumptions does it make?" with short written or selected responses. Auto‑grading checks that responses demonstrate critical evaluation and reference specific code or scenarios.
- **CSTA:** MS‑PRO‑TR‑13 (Describe issues of accuracy and bias in computer-generated code).

