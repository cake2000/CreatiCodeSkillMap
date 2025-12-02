# T12 - Testing, Debugging & Error Handling - IMPROVED SKILLS
# Generated: 2025-12-01
# Total New/Modified Skills: 25

## THREAD 1: NEW - Debugging by Comparison (K-2)

ID: T12.GK.05
Topic: T12 – Testing, Debugging & Error Handling
Skill: Compare two picture sequences - one works, one doesn't
Description: Students view two side-by-side picture sequences showing the same task (e.g., making a sandwich). One sequence shows the correct order and result, the other shows a wrong step and wrong result. Students identify which picture is different between the sequences. Example: Correct sequence shows "bread → peanut butter → jelly → bread" with complete sandwich. Wrong sequence shows "bread → jelly → peanut butter → bread" with messy result. Students circle the different step. _Assessment: Show 3 pairs of sequences; student correctly identifies the different picture in each pair._

Dependencies:
* T01.GK.01: Sequence three picture cards for a bedtime routine
* T12.GK.01: Spot a wrong action in a picture sequence


ID: T12.G1.06
Topic: T12 – Testing, Debugging & Error Handling
Skill: Find the difference between working and broken instructions
Description: Students compare two sets of written instructions for the same task - one that produces correct result, one that fails. Using picture evidence of outcomes, they identify which instruction is different. Example: Working recipe "1. Mix flour 2. Add eggs 3. Bake 20 min" shows cake. Broken recipe "1. Mix flour 2. Bake 20 min 3. Add eggs" shows failed cake. Students circle step 2 as different. _Assessment: Compare 3 pairs of instructions; identify the different step and explain why it breaks the result._

Dependencies:
* T12.GK.05: Compare two picture sequences - one works, one doesn't
* T01.G1.02: Follow multi-step picture instructions with branching


ID: T12.G2.06
Topic: T12 – Testing, Debugging & Error Handling
Skill: Use a "known good" example to find what's wrong
Description: Students debug broken block sequences by comparing them to a provided working example. Given a screenshot of working code and their non-working version, they identify differences in block order, block types, or parameter values. Example: Working code shows "move 10 steps" in a loop; broken code shows "move 100 steps" causing sprite to disappear. _Assessment: Compare broken code to reference; identify 2-3 specific differences and fix them._

Dependencies:
* T12.G1.06: Find the difference between working and broken instructions
* T06.G2.01: Arrange 5-7 blocks in correct order


## THREAD 2: NEW - Code Reading & Static Analysis (G3-G8)

ID: T12.G3.08
Topic: T12 – Testing, Debugging & Error Handling
Skill: Read code and predict output before running
Description: Students examine a 5-8 block script without running it and write down what they predict will happen. They trace through sequences, noting sprite position, costume changes, or messages. Then they run the code and compare actual output to prediction. Example: Script shows "move 50 steps, turn 90 degrees, move 50 steps" - student predicts "L-shaped path" before running. _Assessment: Predict output for 3 scripts; accuracy of at least 2 predictions; explain reasoning._

Dependencies:
* T12.G3.04: Trace a 5-block script mentally then run to verify
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence


ID: T12.G4.10
Topic: T12 – Testing, Debugging & Error Handling
Skill: Spot common bug patterns visually without running code
Description: Students review code screenshots and identify common bug patterns by visual inspection: (1) Missing "wait" blocks causing timing issues, (2) Wrong mathematical operators (+ vs -), (3) Missing "forever" around repeated code, (4) Wrong comparison operators (> vs <), (5) Unreachable code after "stop all". They mark bugs before testing. _Assessment: Review 5 code screenshots; identify at least 4/5 bug patterns correctly by visual inspection only._

Dependencies:
* T12.G3.08: Read code and predict output before running
* T12.G4.01: Test code with different starting conditions


ID: T12.G5.11
Topic: T12 – Testing, Debugging & Error Handling
Skill: Review code for missing edge case handling
Description: Students analyze code for robustness by checking edge cases: (1) What if input is 0? Negative? Very large? (2) What if list is empty? (3) What if division by zero occurs? (4) What if sprite reaches screen boundary? They create a checklist of edge cases, review code against it, and identify missing protections. _Assessment: Given code with 3+ missing edge case handlers, identify them without running; propose fixes._

Dependencies:
* T12.G5.04: Add input validation to reject invalid entries
* T12.G4.10: Spot common bug patterns visually without running code
* T09.G4.01: Use conditionals with AND/OR to test two conditions


ID: T12.G6.09
Topic: T12 – Testing, Debugging & Error Handling
Skill: Review peer code systematically using a checklist
Description: Students use a structured code review checklist to evaluate peer work: (1) Does code match the intended behavior? (2) Are variables named clearly? (3) Are there magic numbers that should be variables? (4) Is repeated code that could be a custom block? (5) Are edge cases handled? (6) Could this fail with unexpected input? They document findings with line-specific feedback. _Assessment: Complete code review of peer project; provide 5+ specific, constructive feedback items with explanations._

Dependencies:
* T12.G5.11: Review code for missing edge case handling
* T07.G5.01: Design a custom block with 2+ parameters


ID: T12.G7.09
Topic: T12 – Testing, Debugging & Error Handling
Skill: Compare two implementations for correctness and efficiency
Description: Students evaluate two different code solutions to the same problem for both correctness and efficiency. They analyze: (1) Do both produce correct output? (2) Which handles edge cases better? (3) Which is more readable? (4) Which would perform better with large inputs? (5) Which is easier to modify? They document trade-offs using evidence. _Assessment: Compare 2 implementations; create comparison table rating correctness, efficiency, readability; recommend best choice with justification._

Dependencies:
* T12.G6.09: Review peer code systematically using a checklist
* T11.G6.01: Identify unnecessary repeated code that could be optimized


ID: T12.G8.09
Topic: T12 – Testing, Debugging & Error Handling
Skill: Analyze code for security vulnerabilities
Description: Students review code for security issues relevant to block coding: (1) Does user input get validated before use? (2) Could malicious input crash the program? (3) Is sensitive data exposed in variables? (4) Could infinite loops be triggered by input? (5) Are broadcast messages predictable/exploitable? Example: Code accepts username but doesn't limit length - attacker could input 10000 characters. _Assessment: Security audit of 3 projects; identify 5+ vulnerabilities; propose mitigations._

Dependencies:
* T12.G7.09: Compare two implementations for correctness and efficiency
* T12.G5.11: Review code for missing edge case handling


## THREAD 3: CONSOLIDATE G5 Tracing Skills (Replacement Skills)

ID: T12.G5.01.NEW
Topic: T12 – Testing, Debugging & Error Handling
Skill: Use multiple tracing techniques to debug complex code
Description: Students apply comprehensive tracing strategy combining (1) **Console logging** with print blocks showing flow and values, (2) **Visual feedback** with say blocks for step-by-step execution, (3) **Real-time monitors** for variable tracking, (4) **Breakpoint simulation** by adding pause/wait blocks, (5) **Color coding** debug output by severity. They select appropriate techniques based on bug type. _Assessment: Debug a multi-sprite, multi-variable program using 4+ tracing techniques; document which technique revealed the bug and why._

Dependencies:
* T12.G4.10: Add print blocks to trace which code is running
* T09.G4.01: Use conditionals with AND/OR to test two conditions
* T12.G4.12: Use colored print blocks to categorize debug output


ID: T12.G5.12
Topic: T12 – Testing, Debugging & Error Handling
Skill: Automate testing with reporter custom blocks
Description: Students create custom reporter blocks that return true/false to automate test checking. Example: Create "test move 10 ()" block that moves sprite 10 steps, checks if x position increased by ~10, returns true if pass. Build a test suite with multiple test blocks and report overall results. Use "if not (test move 10) then say 'FAILED: move 10'" pattern. _Assessment: Create 5+ test reporter blocks; run automated test suite; accurately report pass/fail status._

Dependencies:
* T07.G5.02: Create a reporter block returning calculated values
* T12.G5.01.NEW: Use multiple tracing techniques to debug complex code


ID: T12.G5.13
Topic: T12 – Testing, Debugging & Error Handling
Skill: Build visual regression test comparisons
Description: Students create tests that compare visual output against expected appearance. They use costume numbers, position values, size, and color to verify sprite state. Example: After animation, test "is sprite at x=100, y=50, costume=3, size=150%?" Create reference screenshots and automated checks comparing current state to reference values. _Assessment: Build 3+ visual regression tests; demonstrate detecting when visual output changes unexpectedly._

Dependencies:
* T12.G5.12: Automate testing with reporter custom blocks
* T06.G4.03: Use sensing blocks to detect sprite properties


## THREAD 4: NEW - IoT/Microbit Debugging (G6-G8)

ID: T12.G6.10
Topic: T12 – Testing, Debugging & Error Handling
Skill: Debug sensor input issues when values don't update
Description: Students troubleshoot Microbit sensor problems: (1) Check if sensor is enabled in project settings, (2) Verify sensor blocks return changing values using monitors, (3) Test sensor physically (tilt device, press buttons), (4) Add logging to confirm sensor values are being read, (5) Check if values are being used correctly (compass gives 0-360, not true/false). _Assessment: Debug 3 sensor-related issues; document steps taken and root cause found for each._

Dependencies:
* T12.G5.01.NEW: Use multiple tracing techniques to debug complex code
* T10.G6.01: Read Microbit accelerometer values for tilt detection


ID: T12.G7.10
Topic: T12 – Testing, Debugging & Error Handling
Skill: Debug hardware-software communication timing
Description: Students identify and fix timing issues between Microbit hardware and CreatiCode software: (1) Add wait blocks after hardware state changes (button press needs time to register), (2) Use event-driven handlers instead of polling (when button A pressed vs forever checking), (3) Debug race conditions (LED display vs button input timing), (4) Handle sensor settling time (accelerometer needs stabilization). _Assessment: Fix 3 timing-related bugs; explain timing issue and solution for each._

Dependencies:
* T12.G6.10: Debug sensor input issues when values don't update
* T10.G7.01: Combine multiple Microbit sensors in one project
* T12.G6.04: Debug race conditions between sprite scripts


ID: T12.G8.10
Topic: T12 – Testing, Debugging & Error Handling
Skill: Debug distributed IoT systems with multiple devices
Description: Students debug systems with multiple Microbits communicating via radio: (1) Verify radio group matches on all devices, (2) Test message sending/receiving separately, (3) Add logging on both sender and receiver, (4) Handle message loss (add acknowledgments/retries), (5) Debug message ordering issues, (6) Test with devices at different distances. _Assessment: Debug multi-device project with 3+ communication issues; document issue type and fix for each._

Dependencies:
* T12.G7.10: Debug hardware-software communication timing
* T10.G8.01: Build multi-Microbit radio communication project


## THREAD 5: ENHANCE AI Debugging Earlier (G5-G6)

ID: T12.G5.14
Topic: T12 – Testing, Debugging & Error Handling
Skill: Recognize when AI output doesn't match expectations
Description: Students test AI block output quality by comparing results to requirements: (1) Does AI generate text response follow the prompt? (2) Is image recognition identifying correct objects? (3) Does sentiment analysis match human judgment? (4) Is text-to-speech pronunciation acceptable? Students document mismatches, identify patterns (e.g., AI always fails on specific word types), and adjust prompts or add validation. _Assessment: Test AI feature with 10+ inputs; document 3+ failure cases; propose improved prompts or validation._

Dependencies:
* T12.G5.04: Add input validation to reject invalid entries
* T08.G5.01: Use AI text generation blocks with custom prompts


ID: T12.G6.11
Topic: T12 – Testing, Debugging & Error Handling
Skill: Systematically test AI responses with different inputs
Description: Students create test input sets to evaluate AI robustness: (1) **Typical inputs** (expected use cases), (2) **Edge cases** (empty, very long, special characters), (3) **Adversarial inputs** (trying to break AI), (4) **Ambiguous inputs** (could mean multiple things), (5) **Multilingual inputs** if relevant. They document AI behavior across categories and add input filtering or output validation where needed. _Assessment: Design 20+ test inputs across 4+ categories; document AI behavior; implement 3+ mitigations for failures._

Dependencies:
* T12.G5.14: Recognize when AI output doesn't match expectations
* T12.G6.01: Design test cases covering normal and edge cases


## THREAD 6: NEW - Testing Different Perspectives (G5-G8)

ID: T12.G5.15
Topic: T12 – Testing, Debugging & Error Handling
Skill: Test with extreme inputs users might try
Description: Students deliberately test with extreme inputs to find breaking points: (1) **Boundary values** (0, negative, maximum), (2) **Repeated inputs** (clicking button 100 times rapidly), (3) **Unexpected timing** (input before program ready), (4) **Special characters** in text input, (5) **Maximum length** strings or lists. They document when program breaks and add protective code. _Assessment: Test program with 10+ extreme inputs; document 5+ failures; fix at least 3 breaking cases._

Dependencies:
* T12.G5.11: Review code for missing edge case handling
* T12.G5.04: Add input validation to reject invalid entries


ID: T12.G6.12
Topic: T12 – Testing, Debugging & Error Handling
Skill: Test game from new player perspective
Description: Students playtest games as if they've never seen them before: (1) Are instructions clear without explanation? (2) What happens if player ignores intended path? (3) Can player get stuck or soft-locked? (4) Is difficulty ramp appropriate? (5) Do error messages help? They recruit actual new players, observe silently (no hints!), document confusion points, and improve tutorials/feedback. _Assessment: Conduct 3+ new player tests; document 5+ usability issues discovered; implement improvements; verify with follow-up test._

Dependencies:
* T12.G5.15: Test with extreme inputs users might try
* T12.G6.01: Design test cases covering normal and edge cases


ID: T12.G7.11
Topic: T12 – Testing, Debugging & Error Handling
Skill: Test for different screen sizes and devices
Description: Students verify projects work across contexts: (1) Test fullscreen vs embedded mode, (2) Test on different screen sizes (use browser zoom 50%-200%), (3) Verify UI elements visible at different resolutions, (4) Test with mouse vs touchscreen controls, (5) Check sprite positioning uses relative coordinates not hardcoded values. They document layout issues and fix responsive design problems. _Assessment: Test project on 5+ configurations; document 3+ device-specific issues; implement responsive fixes that work across all._

Dependencies:
* T12.G6.12: Test game from new player perspective
* T06.G6.01: Build multi-scene project with scene transitions


ID: T12.G8.11
Topic: T12 – Testing, Debugging & Error Handling
Skill: Design inclusive test strategies for diverse users
Description: Students create comprehensive testing plans considering diverse user needs: (1) **Visual accessibility** (colorblind-safe palettes, sufficient contrast, not relying only on color), (2) **Cognitive accessibility** (clear instructions, adjustable speed/difficulty, no time pressure), (3) **Motor accessibility** (large click targets, keyboard alternatives, no rapid clicking required), (4) **Literacy levels** (appropriate reading level, icons supplement text), (5) **Cultural context** (avoiding culture-specific assumptions). _Assessment: Accessibility audit of project; document 10+ issues across 3+ categories; implement 5+ improvements; verify with diverse testers._

Dependencies:
* T12.G7.11: Test for different screen sizes and devices
* T12.G6.12: Test game from new player perspective


## ADDITIONAL IMPROVEMENTS TO EXISTING SKILLS

ID: T12.G3.09
Topic: T12 – Testing, Debugging & Error Handling
Skill: Document bugs with steps to reproduce
Description: Students learn structured bug reporting: (1) **Title** (clear 1-sentence summary), (2) **Steps to reproduce** (numbered list starting from green flag), (3) **Expected result** (what should happen), (4) **Actual result** (what actually happens), (5) **Frequency** (always/sometimes/rare). They practice writing bug reports for 3+ issues in their own or peer projects, learning that good bug reports enable faster fixes. _Assessment: Write 3+ bug reports following template; each report enables another student to reproduce the bug from steps alone._

Dependencies:
* T12.G3.04: Trace a 5-block script mentally then run to verify
* T12.G3.01: Recognize that bugs occur when code does not match intent


ID: T12.G4.11
Topic: T12 – Testing, Debugging & Error Handling
Skill: Use binary search debugging to isolate bugs quickly
Description: Students learn efficient bug isolation by disabling half the code at a time. If bug disappears, it's in disabled half; if bug persists, it's in enabled half. Repeat until narrowed to specific blocks. Example: 20-block script has bug. Disable blocks 11-20 - bug gone, so it's in 11-20. Disable 16-20 - bug persists, so it's in 11-15. Continue until found. _Assessment: Debug 3 scripts using binary search method; document number of steps taken vs testing sequentially._

Dependencies:
* T12.G4.02: Test code in small chunks before combining
* T12.G3.08: Read code and predict output before running


ID: T12.G6.13
Topic: T12 – Testing, Debugging & Error Handling
Skill: Debug async timing with broadcast and wait blocks
Description: Students identify and fix asynchronous timing bugs in multi-sprite projects: (1) Recognize when "broadcast" finishes immediately but other sprite's response takes time, (2) Use "broadcast and wait" when order matters, (3) Add timeout checks for stuck scripts, (4) Use variables as flags to signal completion, (5) Avoid race conditions by sequencing dependencies. _Assessment: Debug 3 projects with async timing issues; explain timing problem and why solution works for each._

Dependencies:
* T12.G6.04: Debug race conditions between sprite scripts
* T06.G5.02: Use broadcast with message passing between sprites


ID: T12.G7.12
Topic: T12 – Testing, Debugging & Error Handling
Skill: Profile performance to find bottlenecks
Description: Students measure and optimize performance: (1) Add timer variable tracking execution time of code sections, (2) Use FPS counter to measure frame rate, (3) Identify slow operations (complex calculations in loops, AI calls in forever loops), (4) Test with increasing data sizes to find O(n²) problems, (5) Optimize by caching results, reducing loop iterations, or moving code outside loops. _Assessment: Profile project; identify 3+ bottlenecks with timing data; implement optimizations that measurably improve performance._

Dependencies:
* T12.G7.09: Compare two implementations for correctness and efficiency
* T11.G7.01: Refactor code to eliminate nested loop inefficiencies


ID: T12.G8.12
Topic: T12 – Testing, Debugging & Error Handling
Skill: Build comprehensive test documentation
Description: Students create complete test documentation for projects: (1) **Test plan** (what will be tested and why), (2) **Test cases** (inputs, expected outputs, actual results), (3) **Test results** (pass/fail with evidence), (4) **Bug tracking** (known issues and status), (5) **Test coverage** (which features/code paths tested), (6) **Regression tests** (tests to run before releases). Documentation enables others to verify correctness and catch regressions. _Assessment: Create full test documentation for project; documentation enables peer to run all tests and reproduce results._

Dependencies:
* T12.G8.05: Design a comprehensive test plan for a full project
* T12.G6.09: Review peer code systematically using a checklist
* T12.G5.12: Automate testing with reporter custom blocks
