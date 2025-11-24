# Grade 6 Skills - Comprehensive Analysis Report

## Executive Summary

- **Total Grade 6 Skills**: 233
- **Topics with Grade 6 Skills**: 36
- **X-2 Rule Violations**: 42
- **Skills Needing Updates**: 224

## Grade 6 Skills Distribution by Topic

- **T01**: 8 skills
- **T02**: 6 skills
- **T03**: 5 skills
- **T04**: 8 skills
- **T05**: 8 skills
- **T06**: 5 skills
- **T07**: 9 skills
- **T08**: 3 skills
- **T09**: 7 skills
- **T10**: 8 skills
- **T11**: 8 skills
- **T12**: 4 skills
- **T13**: 5 skills
- **T14**: 6 skills
- **T15**: 8 skills
- **T16**: 6 skills
- **T17**: 8 skills
- **T18**: 2 skills
- **T19**: 6 skills
- **T20**: 5 skills
- **T21**: 13 skills
- **T22**: 5 skills
- **T23**: 4 skills
- **T24**: 10 skills
- **T25**: 4 skills
- **T26**: 8 skills
- **T27**: 4 skills
- **T28**: 10 skills
- **T29**: 9 skills
- **T30**: 6 skills
- **T31**: 6 skills
- **T32**: 8 skills
- **T33**: 10 skills
- **T34**: 3 skills
- **T35**: 3 skills
- **T36**: 5 skills

## Detailed Analysis by Topic

### T01 (8 skills)

#### T01.G6.01
**Skill**: Compare efficiency of linear and binary search

**Description**: Students qualitatively compare linear and binary search on small sorted lists, identifying that binary search uses fewer comparisons by eliminating half the remaining options with each step. _Implemen...

**Current Dependencies**: 1
  - T01.G5.04

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T01.G6.02
**Skill**: Compare how step counts grow with input size

**Description**: Students interpret tables/graphs to see which algorithm scales better. _Implementation note: MCQ + explanation. CSTA: MS‑ALG‑AF‑02, MS‑ALG‑PS‑05._

**Current Dependencies**: 1
  - T01.G5.06

**Recommended Additions**:
  - T05.G6.01: Data Viz skill needs 5 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts

---

#### T01.G6.03
**Skill**: Spot unnecessary work in an algorithm

**Description**: Students highlight lines where an algorithm keeps working after the result is found. _Implementation note: Code highlight; auto‑graded. CSTA: MS‑ALG‑AF‑01._

**Current Dependencies**: 2
  - T06.G3.01
  - T09.G3.01

**Issues Found**:
  - X-2 rule violation: depends on T06.G3.01 (grade 3), should be >= grade 4

**Recommended Removals**:
  - T06.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T01.G6.04
**Skill**: Revise an algorithm to do less work

**Description**: Students remove redundant checks/loops without changing output. _Implementation note: Pseudocode/coding edit; auto‑graded on correctness + fewer steps. CSTA: MS‑ALG‑AF‑01, MS‑ALG‑PS‑05._

**Current Dependencies**: 3
  - T01.G6.03
  - T07.G3.01
  - T08.G3.01

**Issues Found**:
  - X-2 rule violation: depends on T07.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Removals**:
  - T07.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T01.G6.05
**Skill**: Identify who is favored or harmed by a decision algorithm

**Description**: Students analyze a simple decision algorithm for fairness across groups. _Implementation note: Scenario MCQ + short explanation. CSTA: MS‑ALG‑IM‑08. AI4K12: Ethical design (D), Societal impacts (E)._

**Current Dependencies**: 0
  - None

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T01.G6.06
**Skill**: Suggest a change to make a decision algorithm more fair

**Description**: Students propose specific changes to reduce bias or harm. _Implementation note: Structured response; auto‑graded by alignment with identified issue. CSTA: MS‑ALG‑IM‑09. AI4K12: Ethical design (D), Soc...

**Current Dependencies**: 1
  - T01.G6.05

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T01.G6.07
**Skill**: Design a flowchart for a multi‑step program

**Description**: Students design a flowchart for a game turn (ask, check, update score, continue/stop), building on the flowchart symbols, loops, and decisions practiced in T02 up through Grade 6. _Implementation note...

**Current Dependencies**: 4
  - T01.G5.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01

**Issues Found**:
  - X-2 rule violation: depends on T07.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T01.G5.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Data Viz skill needs 5 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

**Recommended Removals**:
  - T07.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T01.G6.08
**Skill**: Implement code from a detailed flowchart

**Description**: Students map each shape in a detailed, multi‑step flowchart to code constructs in a CreatiCode project, focusing on correctness and readability rather than learning new notation. _Implementation note:...

**Current Dependencies**: 2
  - T01.G5.02
  - T09.G3.01

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

### T02 (6 skills)

#### T02.G6.01
**Skill**: Learn the pseudocode generation block

**Description**: Students discover the "get pseudocode from sprite blocks" block in CreatiCode's control category and understand that it converts their block scripts into text-based pseudocode that describes what the ...

**Current Dependencies**: 1
  - T02.G5.02

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T02.G6.02
**Skill**: Generate and read pseudocode from a simple script

**Description**: Students build a simple block script (with sequence and one loop or if/else), use the pseudocode generation block to convert it, and read the resulting pseudocode to understand how their blocks transl...

**Current Dependencies**: 1
  - T02.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T02.G6.03
**Skill**: Compare block code to its generated pseudocode

**Description**: Students create a script with loops and decisions, generate its pseudocode, and identify how each block structure (repeat, if/else, sequence) is represented in the pseudocode text.

**Current Dependencies**: 1
  - T02.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T02.G6.04
**Skill**: Use pseudocode to plan before coding

**Description**: Students write simple pseudocode on paper first (e.g., "repeat 4 times: draw side, turn 90"), then build the matching block script in CreatiCode, learning to plan algorithms before implementing them.

**Current Dependencies**: 1
  - T02.G6.03

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T02.G6.05
**Skill**: Debug using pseudocode comparison

**Description**: Students generate pseudocode from a buggy script, read the pseudocode to understand what the algorithm actually does (vs. what it should do), then fix the blocks based on the insight gained.

**Current Dependencies**: 1
  - T02.G6.03

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T02.G6.06
**Skill**: Trace a data processing algorithm using debug print

**Description**: Students trace a script that processes multiple inputs (e.g., "check 5 numbers and find the largest") using debug print blocks to show how the algorithm examines each value and updates the result.

**Current Dependencies**: 1
  - T02.G5.04

---

### T03 (5 skills)

#### T03.G6.01
**Skill**: Propose modules for a medium project

**Description**: Students read about an existing project and propose logical modules (e.g., "player control," "enemy behavior," "scoring"), grouping related functionality and components.

**Current Dependencies**: 3
  - T03.G5.01
  - T06.G3.01
  - T09.G3.01

**Issues Found**:
  - X-2 rule violation: depends on T06.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T03.G2.04

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts

**Recommended Removals**:
  - T06.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T03.G6.02
**Skill**: Identify reusable components in a complex process

**Description**: Students see an overlong process description and identify which pieces appear multiple times or could be turned into reusable components (e.g., "collision detection," "level reset," "score update"), t...

**Current Dependencies**: 2
  - T03.G5.01
  - T06.G3.01

**Issues Found**:
  - X-2 rule violation: depends on T06.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T03.G2.04

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

**Recommended Removals**:
  - T06.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T03.G6.03
**Skill**: Break a project into milestones (v1/v2/v3)

**Description**: Students organize tasks into "first version," "improvements," and "stretch goals" columns, deciding which features are essential for a working prototype versus which can be added later.

**Current Dependencies**: 1
  - T03.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T03.G2.04

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T03.G6.04
**Skill**: Adjust milestones when constraints are discovered

**Description**: Students read that a planned feature is harder than expected (e.g., "multiplayer will take 3 weeks instead of 1") and adjust the milestone plan by moving the difficult feature to a later version (e.g....

**Current Dependencies**: 2
  - T03.G6.03
  - T03.G4.06

**Issues Found**:
  - Potential circular dependency: Circular: T03.G2.04

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T03.G6.05
**Skill**: Use XO to expand a basic idea into subtasks

**Description**: Students start with a brief project idea, ask XO to suggest subtasks, then evaluate and select which suggestions to keep, modify, or discard based on their understanding of what makes a good project b...

**Current Dependencies**: 1
  - T03.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T03.G2.04

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts

---

### T04 (8 skills)

#### T04.G6.01
**Skill**: Group snippets by underlying algorithm pattern

**Description**: Students classify 5+ diverse code snippets into groups based on their underlying algorithm pattern (counter, accumulator, search, filter), distinguishing between similar-looking but functionally diffe...

**Current Dependencies**: 2
  - T04.G4.05
  - T09.G3.01

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T02.G6.02: Animation skill needs 2 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T04.G6.02
**Skill**: Identify pattern variants that look different but behave the same

**Description**: Students identify code snippets that use different syntax or structure but achieve the same result—for example, counting with a `repeat N` loop versus iterating through a list, or accumulating with `s...

**Current Dependencies**: 1
  - T04.G4.05

**Recommended Additions**:
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T04.G6.03
**Skill**: Apply filter pattern with multiple criteria

**Description**: Students extend the basic filter pattern (from T04.G5.04) to handle multiple criteria, combining conditions to select items that match complex requirements (e.g., "items that are both red AND large" o...

**Current Dependencies**: 2
  - T04.G5.03
  - T04.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T04.G4.01

**Recommended Additions**:
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T04.G6.04
**Skill**: Turn repeated code into a custom block with parameters

**Description**: Students refactor repeated code sequences into a parameterized custom block that can be reused with different values. They identify the varying elements, add parameters to the custom block (e.g., numb...

**Current Dependencies**: 3
  - T04.G3.04
  - T11.G4.07
  - T08.G3.01

**Issues Found**:
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T02.G6.02: Animation skill needs 2 concepts

**Recommended Removals**:
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T04.G6.05
**Skill**: Analyze a template project and identify customization points

**Description**: Students inspect a more complex template (quiz, platformer, etc.) and identify specific customization points with detailed analysis: what each point controls, how to modify it safely, what values are ...

**Current Dependencies**: 1
  - T04.G5.06

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts

---

#### T04.G6.06
**Skill**: Compare two pattern‑based solutions for efficiency and code clarity

**Description**: Students compare two pattern-based solutions and select which is better based on efficiency (fewer operations, faster execution) and clarity (easier to read, fewer lines of code). Example: comparing n...

**Current Dependencies**: 3
  - T04.G5.05
  - T07.G3.01
  - T08.G3.01

**Issues Found**:
  - X-2 rule violation: depends on T07.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

**Recommended Removals**:
  - T07.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T04.G6.07
**Skill**: Implement a pattern-based solution from a description

**Description**: Students read a problem description that fits a standard pattern (counter, accumulator, or search) and implement a solution using that pattern.

**Current Dependencies**: 2
  - T04.G5.07
  - T04.G6.01

**Recommended Additions**:
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T04.G6.08
**Skill**: Access grid elements using 2D indexing patterns

**Description**: Students work with grid or table data structures and use nested loops or 2D indexing patterns (row, column) to access, modify, or analyze grid elements systematically.

**Current Dependencies**: 2
  - T04.G4.02
  - T04.G6.07

**Recommended Additions**:
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

### T05 (8 skills)

#### T05.G6.01
**Skill**: Apply empathy, needs, and accessibility checklist to a design

**Description**: Students review a small app idea using a structured checklist. They mark where empathy (understanding users), needs (solving real problems), and accessibility (usable by everyone) have been addressed ...

**Current Dependencies**: 2
  - T05.G4.02
  - T05.G4.04

---

#### T05.G6.02
**Skill**: Propose specific design changes to address all three HCD principles

**Description**: Students review a design with identified gaps and propose 2–3 specific changes, each addressing one HCD principle: empathy (e.g., "add feature for colorblind users"), needs (e.g., "simplify main task ...

**Current Dependencies**: 1
  - T05.G6.01

**Recommended Additions**:
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T05.G6.03
**Skill**: Analyze short interview or survey data to extract user needs

**Description**: Students read 5–6 short user responses (mock interview quotes or survey answers) and identify 2–3 common themes or needs by highlighting repeated ideas and grouping similar feedback.

**Current Dependencies**: 1
  - T05.G4.02

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T05.G6.04
**Skill**: Update a design based on specific user feedback

**Description**: Students read 3–4 specific feedback items from user testing (e.g., "I couldn't find the save button") and match each to an appropriate design change from a list of options.

**Current Dependencies**: 1
  - T05.G6.03

---

#### T05.G6.05
**Skill**: Plan a simple CreatiCode simulation with variables, rules, and UI

**Description**: Students complete a planning template listing variables, rules, and simple UI widgets (sliders for parameters, labels for displays, buttons for controls, charts for results) for a simulation idea, as ...

**Current Dependencies**: 2
  - T05.G4.05
  - T05.G4.06

**Recommended Additions**:
  - T11.G6.03: Data Viz skill needs 11 concepts

---

#### T05.G6.06
**Skill**: Justify what is modeled vs simplified in a simulation design

**Description**: Students select or write brief reasons for including or ignoring certain aspects of reality.

**Current Dependencies**: 2
  - T05.G4.05
  - T05.G4.06

**Recommended Additions**:
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T05.G6.07
**Skill**: Read a simple bar chart showing user preferences

**Description**: View bar chart of user preferences, answer factual questions (most popular, least used). Builds data literacy before G7.05 pattern analysis.

**Current Dependencies**: 1
  - T05.G5.05

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T05.G6.08
**Skill**: Identify user questions a simulation should answer

**Description**: Read user scenario and identify which questions are best answered by CreatiCode simulation (e.g., "What happens over time?", "How do variables interact?") vs other methods. Connects simulation design ...

**Current Dependencies**: 2
  - T05.G5.06
  - T05.G6.01

**Recommended Additions**:
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

---

### T06 (5 skills)

#### T06.G6.01
**Skill**: Trace event execution paths in a multi‑event program

**Description**: Students analyze a program with several event handlers and broadcasts and determine which scripts run in response to different input sequences.

**Current Dependencies**: 3
  - T06.G3.06
  - T06.G5.04
  - T06.G5.05

**Issues Found**:
  - X-2 rule violation: depends on T06.G3.06 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Animation skill needs 2 concepts

**Recommended Removals**:
  - T06.G3.06: Grade 3 violates X-2 rule for grade 6

---

#### T06.G6.02
**Skill**: Simplify complex event logic with conditionals

**Description**: Students refactor complex event handlers by consolidating multiple similar event scripts into fewer handlers with conditional logic, improving maintainability without changing behavior. For example, r...

**Current Dependencies**: 8
  - T06.G6.01
  - T06.G4.04
  - T06.G5.05
  - T06.G5.06
  - T06.G6.03
  - T12.G5.01
  - T06.G6.03
  - T08.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T06.G6.04
**Skill**: Design meaningful custom broadcasts and document them

**Description**: Students replace generic "message1/message2" with semantic broadcasts (e.g., "player‑hit," "game‑over") and update listeners; they also fill in a small "event dictionary" describing each broadcast.

**Current Dependencies**: 3
  - T06.G5.03
  - T06.G5.05
  - T06.G5.06

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

#### T06.G6.05
**Skill**: Use 'when dragging stops' for drag completion

**Description**: Students use "when dragging stops" to trigger actions when dragging ends (e.g., snap to grid, check final position, play drop sound). Combine all three drag events to create complete drag-and-drop int...

**Current Dependencies**: 19
  - T06.G6.01
  - T16.G3.02
  - T06.G6.05
  - T16.G4.01
  - T06.G6.05
  - T16.G5.01
  - T06.G6.05
  - T16.G4.01
  - T06.G6.05
  - T16.G5.02
  - T06.G6.05
  - T16.G5.03
  - T06.G6.04
  - T06.G6.06
  - T06.G5.08
  - T06.G6.06
  - T06.G6.01
  - T06.G6.07
  - T06.G6.07

**Issues Found**:
  - X-2 rule violation: depends on T16.G3.02 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

**Recommended Removals**:
  - T16.G3.02: Grade 3 violates X-2 rule for grade 6

---

#### T06.G6.08
**Skill**: Use a variable to track simple program states

**Description**: Students create a 'game-state' variable with two or three values (0 = menu, 1 = playing, 2 = game-over) and use conditionals to run different code based on the current state. This introduces state-bas...

**Current Dependencies**: 2
  - T09.G4.01
  - T08.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T07 (9 skills)

#### T07.G6.01
**Skill**: Trace nested loops with variable bounds

**Description**: Students analyze code with nested loops where the inner loop bound depends on the outer loop counter (e.g., `for i from 1 to n` outer, `repeat (n - i)` inner). The key challenge is understanding that ...

**Current Dependencies**: 4
  - T07.G4.03
  - T07.G5.03
  - T07.G5.04
  - T09.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T07.G6.02
**Skill**: Refactor complex repeated patterns into loops with variables

**Description**: Students refactor longer scripts where the repeated segments have slight variations (e.g., "move 10, move 20, move 30" becomes a loop with a changing variable). Unlike G4.04's identical repetitions, t...

**Current Dependencies**: 3
  - T07.G4.03
  - T07.G4.04
  - T07.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T07.G6.03
**Skill**: Loop‑based search in a list

**Description**: Students implement a simple linear search using a for-each loop to find the first item in a list that matches a target (e.g., find the first score above 90), and then respond (e.g., report the positio...

**Current Dependencies**: 3
  - T07.G5.02
  - T07.G6.09
  - T08.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

#### T07.G6.04
**Skill**: Avoid and fix infinite loops

**Description**: Students identify scripts that never stop because of improper use of `forever` or `repeat until` with a condition that never becomes true. They modify the code to add a stopping condition or use the `...

**Current Dependencies**: 2
  - T07.G4.05
  - T07.G6.08

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T07.G6.05
**Skill**: Trace nested loops with abstract calculations using trace tables

**Description**: Students use trace tables to systematically track variable values through nested loops that perform abstract calculations (e.g., computing sums, products, or counts). They create a table with columns ...

**Current Dependencies**: 3
  - T07.G5.03
  - T07.G5.04
  - T09.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T07.G6.06
**Skill**: Trace nested loops that generate spatial patterns

**Description**: Students trace nested loops that produce visual/spatial output where row and column counters control position (e.g., drawing a checkerboard, creating a grid of stamps, or generating triangle patterns)...

**Current Dependencies**: 2
  - T07.G6.05
  - T07.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T07.G6.07
**Skill**: Use loops to update values iteratively

**Description**: Students implement loops that repeatedly update a variable based on its previous value (e.g., adding interest each year, reducing health points each turn, or growing/shrinking a value by a percentage)...

**Current Dependencies**: 3
  - T07.G5.01
  - T07.G5.03
  - T07.G6.05

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

#### T07.G6.08
**Skill**: Use break and continue to control loop flow

**Description**: Students use CreatiCode's `break` block to exit a loop early when a condition is met (e.g., stopping a search once an item is found), and use the `continue` block to skip the rest of the current itera...

**Current Dependencies**: 3
  - T07.G5.02
  - T07.G6.03
  - T07.G6.04

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

---

#### T07.G6.09
**Skill**: Use for-each loops to iterate over lists

**Description**: Students use CreatiCode's `for each item [variable] in [list]` block to process all items in a list, performing an action with each value (e.g., say each word, draw each number, check each score). The...

**Current Dependencies**: 3
  - T07.G5.02
  - T07.G6.03
  - T10.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

### T08 (3 skills)

#### T08.G6.01
**Skill**: Draw state transition diagram

**Description**: Students create state transition diagrams showing which states connect to which others and what conditions trigger transitions (e.g., idle → walking when "move key pressed", walking → jumping when "sp...

**Current Dependencies**: 6
  - T08.G6.01
  - T08.G6.01
  - T08.G5.03
  - T08.G5.04
  - T08.G4.07
  - T08.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T08.G6.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T08.G6.02
**Skill**: Implement simple state machines using conditionals

**Description**: Students use variables and conditionals to implement simple state machines (e.g., idle → walking → jumping based on inputs and timers). This introduces formal state machine concepts and teaches managi...

**Current Dependencies**: 2
  - T08.G6.02
  - T08.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T08.G6.02

**Recommended Additions**:
  - T02.G6.02: Animation skill needs 2 concepts

---

#### T08.G6.03
**Skill**: Debug multi-condition logic

**Description**: Students debug scripts where multi-part conditions (AND/OR/NOT) are wrong or mis-parenthesized, leading to incorrect behavior. This develops systematic debugging approaches for complex boolean express...

**Current Dependencies**: 3
  - T08.G5.03
  - T08.G5.04
  - T08.G4.08

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

### T09 (7 skills)

#### T09.G6.01
**Skill**: Model real-world quantities using variables and formulas

**Description**: Students create variables representing real-world quantities (e.g., distance, time, money, temperature) and update them using formulas. Examples: total_cost = price × quantity, distance = speed × time...

**Current Dependencies**: 2
  - T09.G5.05
  - T09.G5.07

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T09.G6.02
**Skill**: Use parentheses to override operator precedence

**Description**: Students use parentheses to control evaluation order in expressions, overriding default PEMDAS precedence. They predict and explain different results from "(a + b) * c" vs "a + b * c". This enables th...

**Current Dependencies**: 2
  - T09.G5.07
  - T09.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T09.G6.03
**Skill**: Use modulo (remainder) operator in expressions

**Description**: Students use the modulo operator (mod or %) to find remainders from division. They apply this to practical tasks like determining odd/even numbers (n mod 2), cycling through values (position mod max),...

**Current Dependencies**: 2
  - T09.G6.02
  - T09.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T09.G6.04
**Skill**: Use case conversion (uppercase/lowercase) operators

**Description**: Students use `[CASE v] of text [T]` blocks to convert text to uppercase or lowercase. They apply this for formatting output or case-insensitive comparisons. Examples: uppercase for shouting effects, l...

**Current Dependencies**: 2
  - T09.G5.03
  - T09.G6.04

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

---

#### T09.G6.05
**Skill**: Use substring operator to extract text portions

**Description**: Students use `substring of [text] from position (start) to (end)` to extract parts of strings. They apply this for text parsing, extracting initials, or getting file extensions. Example: extract first...

**Current Dependencies**: 2
  - T09.G6.04
  - T09.G6.05

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

---

#### T09.G6.06
**Skill**: Understand variable persistence across events and broadcasts

**Description**: Students understand that variables maintain their values across different event handlers and broadcasts. When one script sets a variable and broadcasts a message, another script receiving that broadca...

**Current Dependencies**: 3
  - T09.G5.05
  - T09.G6.02
  - T09.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T02.G6.02: Animation skill needs 2 concepts

---

#### T09.G6.07
**Skill**: Debug off-by-one and comparison operator errors

**Description**: Students debug scripts where variables control program flow through conditionals and loops. Common bugs include: wrong comparison operator (using > instead of >=), off-by-one errors in loop conditions...

**Current Dependencies**: 2
  - T09.G4.09
  - T09.G5.07

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

---

### T10 (8 skills)

#### T10.G6.01
**Skill**: Sort a table by a column

**Description**: Students use CreatiCode's `sort table [table] by column [name] [large to small/small to large]` block to reorder rows based on values in a column. They understand sorting preserves row integrity (all ...

**Current Dependencies**: 2
  - T10.G4.05
  - T10.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T10.G3.03

---

#### T10.G6.02
**Skill**: Filter table rows based on a condition

**Description**: Students loop through a table and identify rows where a column value meets a condition (e.g., "find all students with score > 80"). They either collect matching row numbers or build a new filtered tab...

**Current Dependencies**: 2
  - T10.G5.07
  - T08.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

#### T10.G6.03
**Skill**: Copy and append tables

**Description**: Students use `copy table [t1] into [t2]` to duplicate a table and `append table [t1] to [t2]` to combine tables vertically. Vertical appending adds new rows below existing rows; both tables must have ...

**Current Dependencies**: 1
  - T10.G5.03

**Recommended Additions**:
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T10.G6.04
**Skill**: Use table lookup to find related data

**Description**: Students use the `item in column [return_col] of [table] where column [search_col] equals [value]` block to look up data. For example, find a student's grade by looking up their name, similar to VLOOK...

**Current Dependencies**: 2
  - T10.G5.06
  - T10.G5.04

---

#### T10.G6.05
**Skill**: Group data and compute aggregates per group

**Description**: Students use CreatiCode's `set table [result] to [method] of column [value_col] in table [source] by column [group_col]` block to group rows by a category and compute statistics (sum, average, count) ...

**Current Dependencies**: 2
  - T10.G5.08
  - T10.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

---

#### T10.G6.06
**Skill**: Use set operations on lists

**Description**: Students implement set operations like union (all unique items from both lists), intersection (only items in both lists), and difference (items in list1 but not list2) using loops and conditionals. Th...

**Current Dependencies**: 2
  - T10.G4.08
  - T10.G3.06

**Issues Found**:
  - X-2 rule violation: depends on T10.G3.06 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Removals**:
  - T10.G3.06: Grade 3 violates X-2 rule for grade 6

---

#### T10.G6.07
**Skill**: Remove duplicate items from a list

**Description**: Students write code to remove duplicate values from a list, keeping only one instance of each unique value. They loop through the list, check if each item already exists in a result list, and add only...

**Current Dependencies**: 2
  - T10.G3.06
  - T10.G4.08

**Issues Found**:
  - X-2 rule violation: depends on T10.G3.06 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

**Recommended Removals**:
  - T10.G3.06: Grade 3 violates X-2 rule for grade 6

---

#### T10.G6.08
**Skill**: Shuffle table rows randomly

**Description**: Students use the `reshuffle table [table] randomly` block to randomize row order while keeping row integrity (all columns in a row stay together). They use this for randomizing quiz questions stored i...

**Current Dependencies**: 2
  - T10.G4.15
  - T10.G5.03

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

### T11 (8 skills)

#### T11.G6.01
**Skill**: Design custom blocks with clear, predictable interfaces

**Description**: Students design custom blocks by first deciding what the block should do, what inputs (parameters) it needs, and what it should return (if anything) BEFORE writing the code inside. They choose clear, ...

**Current Dependencies**: 3
  - T11.G5.04
  - T11.G5.05
  - T11.G5.06

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T11.G6.02
**Skill**: Create modular programs with multiple custom blocks

**Description**: Students design and implement a moderately complex program (e.g., a game with setup, gameplay, and end screen) structured as a set of custom blocks, each handling a distinct responsibility. They demon...

**Current Dependencies**: 2
  - T11.G5.05
  - T11.G5.06

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T11.G6.03
**Skill**: Test custom blocks with boundary and edge cases

**Description**: Students test their custom blocks systematically with normal inputs, boundary values (e.g., 0, negative numbers, very large numbers), and edge cases. They identify and fix bugs that only appear with c...

**Current Dependencies**: 2
  - T11.G5.06
  - T11.G5.09

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T11.G6.04
**Skill**: Refactor spaghetti code into organized custom blocks

**Description**: Students take a messy, unorganized script (20-30 blocks) and improve it by identifying and extracting logical units into custom blocks, improving readability without changing behavior. They verify the...

**Current Dependencies**: 1
  - T11.G5.05

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

---

#### T11.G6.05
**Skill**: Add error handling to custom blocks

**Description**: Students add simple error handling to custom blocks to prevent unexpected behavior. They use conditional blocks to check parameter values before executing the main logic (e.g., checking if a number is...

**Current Dependencies**: 2
  - T11.G5.06
  - T11.G6.03

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T11.G6.06
**Skill**: Critique custom block naming and parameter choices

**Description**: Students evaluate custom block designs focusing specifically on naming conventions and parameter choices. They identify unclear or inconsistent names (e.g., "block1" vs "CalculateScore"), overly gener...

**Current Dependencies**: 2
  - T11.G5.04
  - T11.G5.11

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T11.G6.07
**Skill**: Evaluate custom block scope and single responsibility

**Description**: Students evaluate whether custom blocks follow the "single responsibility principle" - each block should do ONE thing well. They identify blocks that try to do too much (e.g., a "SetupGame" block that...

**Current Dependencies**: 2
  - T11.G5.05
  - T11.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T11.G6.08
**Skill**: Critique return value usage in custom blocks

**Description**: Students evaluate whether custom blocks correctly use return values versus side effects (setting variables, moving sprites, etc.). They identify blocks that should return a value but don't (e.g., a ca...

**Current Dependencies**: 2
  - T11.G5.07
  - T11.G5.08

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

### T12 (4 skills)

#### T12.G6.01
**Skill**: Analyze a program's structure using a checklist and suggest specific improvements

**Description**: Students use a structured checklist (covering naming, comments, script organization, etc.) to systematically evaluate a multi-script program and propose specific refactoring steps. Focus is on methodi...

**Current Dependencies**: 2
  - T12.G5.03
  - T12.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

---

#### T12.G6.02
**Skill**: Use comments to explain algorithm logic

**Description**: Students add comments explaining their reasoning and design choices at the algorithm level (e.g., "I use a repeat loop instead of separate move blocks because it's easier to change the distance later"...

**Current Dependencies**: 1
  - T12.G5.02

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T12.G6.03
**Skill**: Follow a provided style guide for naming conventions

**Description**: Students are given a style guide (e.g., camelCase for variables, verb-based names for custom blocks) and apply it consistently when reviewing or refactoring a project. Focus is on understanding and fo...

**Current Dependencies**: 3
  - T12.G4.02
  - T12.G4.04
  - T12.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

#### T12.G6.04
**Skill**: Document code for collaborative maintenance

**Description**: Students add comments and documentation to a project so that a peer or their future self can understand and modify it. They explain key variables, the role of each script, and any non-obvious design c...

**Current Dependencies**: 2
  - T12.G5.01
  - T12.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

### T13 (5 skills)

#### T13.G6.01
**Skill**: Trace complex code with multiple variables

**Description**: Students step through a program with multiple variables and complex logic, tracking how each variable changes at each step. They use a table or mental model to predict the final state and verify corre...

**Current Dependencies**: 4
  - T08.G3.01
  - T09.G3.01
  - T13.G5.01
  - T13.G5.06

**Issues Found**:
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

**Recommended Removals**:
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T13.G6.02
**Skill**: Use a systematic debugging process (hypothesis-driven)

**Description**: Students apply a 4-step debugging method: (1) observe and describe the symptom (what goes wrong and when), (2) form a hypothesis about which block or logic causes it (e.g., "I think the repeat count i...

**Current Dependencies**: 2
  - T08.G3.01
  - T13.G5.01

**Issues Found**:
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Removals**:
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T13.G6.03
**Skill**: Design systematic boundary tests using a matrix

**Description**: Students design a systematic boundary test matrix for a program with numeric inputs. For each input variable, they identify 5 test values: (1) minimum valid, (2) just below minimum (invalid), (3) typi...

**Current Dependencies**: 2
  - T09.G3.01
  - T13.G5.02

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T13.G6.04
**Skill**: Document known limitations and potential bugs

**Description**: Students examine their program and document cases or inputs it doesn't handle correctly, potential future bugs, or design limitations. This self-aware documentation reflects mature debugging thinking.

**Current Dependencies**: 2
  - T13.G4.07
  - T13.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T13.G6.05
**Skill**: Debug a peer's program using systematic observation

**Description**: Students are given a classmate's broken program (without seeing the fix). They use systematic observation: (1) run the program and observe symptoms, (2) add `say` blocks or monitors to trace variable ...

**Current Dependencies**: 2
  - T13.G5.01
  - T13.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

### T14 (6 skills)

#### T14.G6.02
**Skill**: Hitbox separation

**Description**: Create a simple rectangular sprite (called a 'collision box' or 'hitbox') that is hidden during gameplay. Use this sprite for detecting when the player touches walls or enemies, while a separate art s...

**Current Dependencies**: 2
  - T14.G5.03
  - T09.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T04.G6.01: Sensing skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T14.G6.03
**Skill**: Multi-layer HUD with viewport attachments

**Description**: Attach multiple sprites to the viewport (score, minimap, buttons) and manage their layering so UI always sits above gameplay while remaining interactive. Use `go to front layer` to ensure proper z-ord...

**Current Dependencies**: 2
  - T14.G5.06
  - T09.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T14.G6.04
**Skill**: Stream level chunks with viewport reporters

**Description**: Use `viewport x` and `viewport y` to track where the camera is positioned. Write scripts that create new game objects (platforms, enemies) when the camera gets close to them, and delete objects that a...

**Current Dependencies**: 3
  - T14.G5.04
  - T14.G5.05
  - T09.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T14.G6.05
**Skill**: Cinematic camera rails

**Description**: Call `detach from viewport`, run scripted `move viewport` sequences for intro/outro scenes, then relock to the player once the cutscene ends. Create smooth camera movements by using glide-like techniq...

**Current Dependencies**: 3
  - T14.G5.04
  - T14.G5.05
  - T08.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T14.G6.06
**Skill**: Mode and pause manager

**Description**: Maintain a `Game Mode` variable and gate scripts so physics, UI, and spawns only run in the appropriate mode (Play, Pause, Shop, Cutscene). Use conditionals at the start of forever loops to check the ...

**Current Dependencies**: 2
  - T14.G6.01
  - T08.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T14.G6.07
**Skill**: Monitor and optimize clone count

**Description**: Create a `Clone Count` variable and increment it when clones are created, decrement when deleted. Display this on stage to monitor performance. If count gets too high (causing lag), implement limits: ...

**Current Dependencies**: 3
  - T14.G4.01
  - T14.G4.03
  - T09.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T15 (8 skills)

#### T15.G6.01
**Skill**: Animation state machine

**Description**: Use a `(state)` variable (e.g., "idle", "moving", "talking") to control character behavior. Inside a `forever` loop, use `if <(state) = [moving]>` blocks to run different animation sequences (like siz...

**Current Dependencies**: 2
  - T15.G5.08
  - T09.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T15.G3.01

**Recommended Additions**:
  - T02.G6.02: Animation skill needs 2 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T15.G6.02
**Skill**: List-based Dialogue

**Description**: Store dialogue lines in a list and use `repeat (length of [dialogue])` with `say (item (i) of [dialogue])` to iterate through them, making dialogue easy to edit and extend.

**Current Dependencies**: 2
  - T15.G6.01
  - T10.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T15.G3.01

---

#### T15.G6.03
**Skill**: Cutscene controller with custom blocks

**Description**: Create a custom block called "Cutscene" (using "Make a Block") that orchestrates multi-step story sequences using `broadcast and wait` to ensure strict timing. Inside the custom block: `broadcast [Ste...

**Current Dependencies**: 3
  - T15.G6.02
  - T15.G5.02
  - T11.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T15.G3.01

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T02.G6.02: Animation skill needs 2 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T15.G6.04
**Skill**: Multi-language text-to-speech storytelling

**Description**: Create stories that speak in multiple languages by combining text-to-speech with conditionals. Store the player's language preference in a variable: `set [playerLanguage v] to [Spanish]`. Use `if <(pl...

**Current Dependencies**: 3
  - T15.G5.12
  - T09.G5.01
  - T08.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T15.G3.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T15.G6.05
**Skill**: Basic speech recognition input

**Description**: Use speech recognition blocks to accept voice input from players. Start listening with `start recognizing speech in [English (United States) v] record as [input1]` (uses Microsoft Azure API) or `OpenA...

**Current Dependencies**: 2
  - T15.G6.04
  - T09.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T15.G3.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T15.G6.06
**Skill**: Voice-controlled story choices

**Description**: Combine speech recognition with conditional logic to trigger story events based on spoken keywords. After using `start recognizing speech` and `end speech recognition`, check the result: `if <(text fr...

**Current Dependencies**: 3
  - T15.G6.05
  - T15.G4.06
  - T08.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T15.G3.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T15.G6.07
**Skill**: Rich text story displays

**Description**: Use `add rich textbox at X (0) Y (0) width (400) height (300) padding (10) mode [read only v] as [storyText]` to create formatted text displays that support bold, italics, colors, and multiple paragra...

**Current Dependencies**: 2
  - T15.G5.14
  - T16.G5.05

**Issues Found**:
  - Potential circular dependency: Circular: T15.G3.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Data Viz skill needs 5 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T15.G6.08
**Skill**: Visual stat tracking with sliders

**Description**: Use `add slider at X (0) Y (0) width (200) min (0) max (100) as [healthBar]` to create visual stat displays for story variables. After creating the slider widget, link it to a variable by updating the...

**Current Dependencies**: 2
  - T15.G5.07
  - T15.G5.13

**Issues Found**:
  - Potential circular dependency: Circular: T15.G3.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T04.G6.01: Sensing skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T16 (6 skills)

#### T16.G6.01
**Skill**: Evaluate an interface for usability

**Description**: Students examine an existing interface (a simple app screenshot) and identify issues or strengths: Are buttons clearly labeled? Is the layout intuitive? Are colors accessible for colorblind users? The...

**Current Dependencies**: 1
  - T16.G5.03

**Issues Found**:
  - Potential circular dependency: Circular: T16.G3.02

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T16.G6.02
**Skill**: Design an interface based on user feedback

**Description**: Students design an initial interface (buttons, labels, layout), ask peers or a teacher to try it, gather feedback on usability, and then modify the design to address the feedback. This introduces the ...

**Current Dependencies**: 1
  - T16.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T16.G3.02

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T16.G6.03
**Skill**: Manage widget states and focus for clear feedback

**Description**: Manage widget states to provide clear feedback. Use "disable widget" to grey out and prevent interaction. Use "enable widget" to restore interactivity. Use "release focus for widget [NAME]" to deselec...

**Current Dependencies**: 6
  - T16.G5.03
  - T16.G4.02
  - T16.G6.03
  - T16.G3.07
  - T16.G6.03
  - T08.G4.03

**Issues Found**:
  - X-2 rule violation: depends on T16.G3.07 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T16.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

**Recommended Removals**:
  - T16.G3.07: Grade 3 violates X-2 rule for grade 6

---

#### T16.G6.04
**Skill**: Create an interface that works on different screen sizes

**Description**: Create interfaces that adapt to different screen sizes using the "apply layout row" block. Define multiple rows with percentage heights summing to 100% (e.g., Row 1: 15% header, Row 2: 70% content, Ro...

**Current Dependencies**: 3
  - T16.G5.01
  - T16.G4.01
  - T16.G3.08

**Issues Found**:
  - X-2 rule violation: depends on T16.G3.08 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T16.G3.02

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

**Recommended Removals**:
  - T16.G3.08: Grade 3 violates X-2 rule for grade 6

---

#### T16.G6.05
**Skill**: Display camera feed in a widget

**Description**: Use "show [front/back v] camera in [normal/flipped v] x (X) y (Y) width (WIDTH) height (HEIGHT) as [NAME]" block to display a live camera feed. Choose front or back camera, normal or flipped (mirror) ...

**Current Dependencies**: 2
  - T16.G5.05
  - T16.G4.02

**Issues Found**:
  - Potential circular dependency: Circular: T16.G3.02

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T16.G6.06
**Skill**: Navigate to other projects

**Description**: Use "run project [PROJECTID] in [new/this v] browser tab" block to launch another CreatiCode project. The target project auto-starts in full stage mode. Choose "new" to open in a new browser tab (keep...

**Current Dependencies**: 4
  - T16.G5.01
  - T16.G4.03
  - T16.G6.06
  - T16.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T16.G3.02

**Recommended Additions**:
  - T02.G6.02: Animation skill needs 2 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

### T17 (8 skills)

#### T17.G6.01
**Skill**: Configure surface friction parameters

**Description**: Students adjust the friction percentage using `update density [value] friction [value]% restitution [value]%` and measure how far objects slide on different surfaces. They learn to map friction values...

**Current Dependencies**: 2
  - T17.G5.09
  - T17.G5.10

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T17.G6.02
**Skill**: Compare dynamic vs movable body types

**Description**: Students compare dynamic bodies (affected by forces and gravity) with movable (kinematic) bodies (move via velocity but don't respond to forces). They identify scenarios where each type is appropriate...

**Current Dependencies**: 8
  - T17.G6.01
  - T17.G5.06
  - T17.G5.08
  - T17.G6.02
  - T17.G6.02
  - T17.G6.02
  - T17.G5.06
  - T17.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

#### T17.G6.03
**Skill**: Build a movable (kinematic) moving platform

**Description**: Students create a platform using `behave as a [movable] [object]` that moves on a fixed path while still colliding with players. They use `set x speed` and `set y speed` to control platform motion dir...

**Current Dependencies**: 2
  - T07.G3.05
  - T17.G6.02

**Issues Found**:
  - X-2 rule violation: depends on T07.G3.05 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

**Recommended Removals**:
  - T07.G3.05: Grade 3 violates X-2 rule for grade 6

---

#### T17.G6.04
**Skill**: Build trigger zones and collectibles with sensor bodies

**Description**: Use sensor bodies to create trigger zones, checkpoints, and collectible items that detect without physical collision

**Current Dependencies**: 8
  - T06.G4.01
  - T17.G5.10
  - T17.G6.04
  - T17.G6.04
  - T17.G6.04
  - T17.G6.04
  - T17.G5.06
  - T17.G6.04

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T04.G6.01: Sensing skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T17.G6.05
**Skill**: Use dominance groups for one-way pushing

**Description**: Use dominance groups to create one-way interactions where stronger objects push weaker ones

**Current Dependencies**: 4
  - T08.G4.01
  - T17.G6.04
  - T17.G6.05
  - T17.G6.05

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T17.G6.06
**Skill**: Lock movement or rotation of physics bodies

**Description**: Students use `prevent body movement from forces [Yes]` and `prevent body rotation from forces [Yes]` to constrain physics objects. They create characters that stay upright, platforms that resist being...

**Current Dependencies**: 3
  - T17.G5.10
  - T17.G5.11
  - T17.G5.06

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T17.G6.07
**Skill**: Configure world borders for wrap-around or open-edge levels

**Description**: Set physics world border collision groups. Students use 'physics world border collision groups' block to configure whether certain sprites or groups can collide with stage borders, enabling scenarios ...

**Current Dependencies**: 5
  - T17.G6.01
  - T17.G6.02
  - T17.G5.05
  - T17.G6.01
  - T17.G6.07

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T17.G6.08
**Skill**: Compare simulations to real-world motion

**Description**: Students record bounce heights or slide distances in CreatiCode, compare them to expected real-world results, and discuss how closely the simulation matches reality and what simplifications the physic...

**Current Dependencies**: 1
  - T17.G5.10

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

---

### T18 (2 skills)

#### T18.G6.02
**Skill**: Trace multi-step 3D scripts with transforms

**Description**: Students read longer scripts that mix coordinate changes, rotations, and camera commands (orbit, zoom) and predict final object positions or camera headings without running it.

**Current Dependencies**: 1
  - T18.G6.01

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T18.G6.03
**Skill**: Analyze trade-offs in 3D design decisions

**Description**: Students review a completed 3D project and explain design choices (physics vs manual motion, camera placement, effect usage), citing pros and cons relative to requirements.

**Current Dependencies**: 41
  - T18.G6.02
  - T07.G3.01
  - T11.G3.01
  - T18.G6.03
  - T18.G6.04
  - T18.G6.04
  - T18.G6.05
  - T18.G6.05
  - T18.G6.05
  - T18.G6.06
  - T18.G6.06
  - T18.G7.01
  - T18.G7.01
  - T18.G7.01
  - T18.G7.02
  - T18.G7.02
  - T18.G7.02
  - T18.G7.03
  - T18.G7.03
  - T18.G7.03
  - T18.G7.04
  - T18.G7.04
  - T18.G7.05
  - T18.G7.05
  - T18.G7.06
  - T18.G7.06
  - T18.G7.06
  - T18.G8.01
  - T09.G3.01
  - T18.G8.01
  - T18.G8.01
  - T18.G8.02
  - T18.G8.02
  - T18.G8.03
  - T18.G8.03
  - T18.G8.04
  - T18.G8.04
  - T18.G8.04
  - T18.G8.05
  - T18.G8.05
  - T18.G8.06

**Issues Found**:
  - X-2 rule violation: depends on T07.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T11.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

**Recommended Removals**:
  - T07.G3.01: Grade 3 violates X-2 rule for grade 6
  - T11.G3.01: Grade 3 violates X-2 rule for grade 6

---

### T19 (6 skills)

#### T19.G6.06
**Skill**: Configure collision deletion (delete sprite on touch)

**Description**: Students learn that collisions can delete sprites using "stop and delete" or "continue and delete" modes in the collision message block. They understand "stop and delete" makes this sprite stop moving...

**Current Dependencies**: 4
  - T19.G6.02
  - T14.G5.01
  - T19.G6.06
  - T19.G6.07

**Issues Found**:
  - Potential circular dependency: Circular: T19.G6.06

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T04.G6.01: Sensing skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T19.G6.07
**Skill**: Handle multiplayer collisions with triggered messages

**Description**: Students use the collision message block to trigger a message with a parameter when sprites collide. They understand this message is broadcast to all relevant sprites in the multiplayer game. They rec...

**Current Dependencies**: 2
  - T19.G6.06
  - T06.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T19.G6.06

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T19.G6.08
**Skill**: Create shared world objects that stay synchronized

**Description**: Students add static sprites (coins, doors, obstacles, switches) to the game world and ensure their state stays synchronized across all players. When a player interacts with an object (collects a coin,...

**Current Dependencies**: 2
  - T19.G6.02
  - T19.G6.04

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T19.G6.09
**Skill**: Remove sprites and clean up when players leave

**Description**: Students automatically remove sprites and clean up resources when players disconnect from the game. They use player leave detection to trigger sprite removal, remove sprites from the multiplayer game ...

**Current Dependencies**: 8
  - T19.G6.04
  - T09.G5.01
  - T19.G6.01
  - T19.G6.01
  - T19.G6.10
  - T19.G6.02
  - T19.G6.10
  - T19.G6.11

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T19.G6.11
**Skill**: Remove sprites from the multiplayer game world

**Description**: Students use the `remove this sprite from game` block to remove sprites when players disconnect, objects are collected, or enemies are defeated. They ensure the removal is synchronized by broadcasting...

**Current Dependencies**: 2
  - T19.G6.02
  - T19.G6.07

**Issues Found**:
  - Potential circular dependency: Circular: T19.G6.06

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

#### T19.G6.12
**Skill**: Understand network delay and its impact on gameplay

**Description**: Students learn that network delay (latency) is the time it takes for messages to travel from one computer to the server and then to other computers, and how this affects gameplay design. They understa...

**Current Dependencies**: 9
  - T19.G6.08
  - T19.G6.04
  - T19.G6.00
  - T19.G6.01
  - T08.G4.01
  - T19.G6.00
  - T19.G6.00
  - T19.G6.00
  - T19.G7.00

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

### T20 (5 skills)

#### T20.G6.01
**Skill**: Trace and explain an art algorithm

**Description**: Students examine code with comments and section markers containing nested loops, variables, and color changes. They explain what each section (identified by comments) contributes to the final artwork,...

**Current Dependencies**: 3
  - T07.G5.01
  - T09.G5.01
  - T20.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T20.G6.02
**Skill**: Refactor repetitive art into loops/custom blocks

**Description**: Learners take a long, repetitive art script and reorganize it with loops or custom blocks without changing the visual result.

**Current Dependencies**: 3
  - T07.G5.01
  - T11.G5.01
  - T20.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

---

#### T20.G6.03
**Skill**: Use variables and conditionals to branch designs

**Description**: Students create art where colors/shapes change based on variable thresholds (e.g., alternate palette when index is even, draw special motif every 5th loop).

**Current Dependencies**: 4
  - T07.G5.01
  - T08.G5.01
  - T09.G5.01
  - T20.G5.02

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts
  - T04.G6.01: Sensing skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T20.G6.04
**Skill**: **[Technical Skill]** Implement multi-field data visualization

**Description**: Students implement algorithms to process structured data (nested lists or multiple parallel lists representing objects with multiple attributes) and map different data fields to distinct visual proper...

**Current Dependencies**: 4
  - T07.G5.01
  - T08.G5.01
  - T10.G5.01
  - T20.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T20.G6.05
**Skill**: Create interactive 3D generative art

**Description**: Students add interactivity to their 3D algorithmic art by mapping keyboard/mouse input to 3D transformations, camera angles, or generative parameters. They create art that viewers can explore and mani...

**Current Dependencies**: 9
  - T07.G5.01
  - T09.G5.01
  - T20.G5.04
  - T20.G5.10
  - T20.G6.05
  - T20.G5.10
  - T20.G6.05
  - T20.G5.03
  - T20.G5.10

**Issues Found**:
  - Potential circular dependency: Circular: T07.G4.03

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T21 (13 skills)

#### T21.G6.01
**Skill**: Plan a mixed-source asset kit for a game or story project

**Description**: Given a specific project (e.g., a simple platformer game or an interactive story), students list all visual and audio assets needed, categorize each as "AI-generated," "hand-created," or "library," an...

**Current Dependencies**: 2
  - T21.G4.01
  - T21.G5.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T21.G6.02
**Skill**: Write structured prompts to maintain consistent visual style

**Description**: Students transform vague ideas (e.g., "dragon in a cave") into detailed prompts with five components: subject, action, camera angle, color palette, and mood. By reusing this structure across multiple ...

**Current Dependencies**: 2
  - T21.G5.01
  - T21.G5.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts

---

#### T21.G6.03
**Skill**: Build a prompt test bench inside CreatiCode

**Description**: Students use a provided starter template with a text input, dropdown style selector, and gallery of preview sprites already set up. They complete the implementation by adding the `OpenAI DALL-E: gener...

**Current Dependencies**: 3
  - T06.G4.01
  - T09.G3.01
  - T10.G5.03

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T21.G6.04
**Skill**: Iterate when an AI output fails requirements

**Description**: Students practice reading a failed generation (wrong colors, missing character, awkward proportions), identifying the cause (prompt missing detail, wrong style keyword, conflicting terms), and rewriti...

**Current Dependencies**: 1
  - T10.G5.03

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T21.G6.05
**Skill**: Use OpenAI Whisper speech recognition (ai_startopenaispeech block)

**Description**: Students use OpenAI Whisper speech recognition with the `OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]` (ai_startopenaispeech) block to record their voice and convert it to te...

**Current Dependencies**: 4
  - T06.G4.01
  - T21.G5.04
  - T06.G4.01
  - T21.G6.05

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T21.G6.06
**Skill**: Check user input with AI content moderation

**Description**: Students use the `get moderation result for [TEXT]` block to check whether user-submitted text is appropriate. They build a simple input checker that displays "Pass" or "Fail" based on the moderation ...

**Current Dependencies**: 2
  - T08.G4.01
  - T21.G5.05

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T21.G6.07
**Skill**: Use image moderation to check visual content

**Description**: Students use `get moderation result for image at URL [URL]` or `get moderation result for costume named [NAME]` to check whether uploaded or AI-generated images meet content guidelines. They build a c...

**Current Dependencies**: 2
  - T21.G5.02
  - T21.G6.06

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T21.G6.08
**Skill**: Use ChatGPT to generate story text or dialogue

**Description**: Students use ChatGPT to generate creative text content for their projects, such as story narration, character dialogue, or scene descriptions. They provide clear prompts that specify the tone, style, ...

**Current Dependencies**: 2
  - T21.G5.06
  - T21.G5.07

---

#### T21.G6.09
**Skill**: Compare ChatGPT responses with different temperatures

**Description**: Students experiment with the temperature parameter (0 = predictable/focused, 2 = creative/random) by asking ChatGPT the same question multiple times with different temperature values. They analyze how...

**Current Dependencies**: 1
  - T21.G5.07

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T21.G6.10
**Skill**: Use system instructions to guide ChatGPT behavior

**Description**: Students use the `OpenAI ChatGPT: system request [PROMPT] session [SESSION v] result [VARIABLE v] temperature [T]` block to set system-level instructions that guide how ChatGPT responds. They learn ho...

**Current Dependencies**: 1
  - T21.G5.06

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T21.G6.11
**Skill**: Use head tilt angle for face orientation detection

**Description**: Students read the tilt angle value from the face detection table to determine head orientation (tilt left vs tilt right vs straight). They use this data to create interactive applications that respond...

**Current Dependencies**: 6
  - T06.G4.01
  - T10.G5.03
  - T10.G5.03
  - T21.G6.11
  - T08.G4.01
  - T21.G6.11

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T21.G6.12
**Skill**: Detect specific poses using body part combinations

**Description**: Students combine multiple body part readings to recognize complex poses, such as: T-pose (both arms straight and horizontal), hands on hips (wrists near hips), jumping (both knees bent then straighten...

**Current Dependencies**: 8
  - T06.G4.01
  - T10.G4.01
  - T10.G4.01
  - T21.G6.12
  - T08.G4.01
  - T21.G6.12
  - T08.G4.01
  - T21.G6.12

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T21.G6.13
**Skill**: Stop camera-based AI detection to manage resources

**Description**: Students learn to properly stop camera-based AI features when they're no longer needed. They use `stop 2D body part recognition` to stop body tracking and `stop continuous speech recognition` to stop ...

**Current Dependencies**: 2
  - T21.G6.11
  - T21.G6.12

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

### T22 (5 skills)

#### T22.G6.02
**Skill**: Adjust temperature for response creativity

**Description**: Students adjust the ChatGPT block's temperature parameter (scale 0-1, where 0 produces more predictable and focused responses, and 1 produces more creative and varied responses) to control response va...

**Current Dependencies**: 5
  - T06.G4.01
  - T08.G4.01
  - T09.G4.04
  - T22.G5.01
  - T22.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T22.G6.03
**Skill**: Build a conversation log with dynamic updates

**Description**: Students create a scrolling conversation display using label widgets or list displays. They append each user message and bot response to maintain a visible chat history, managing formatting and scroll...

**Current Dependencies**: 11
  - T06.G4.01
  - T08.G4.01
  - T09.G4.04
  - T22.G5.01
  - T22.G6.01
  - T16.G3.01
  - T16.G3.05
  - T22.G5.04
  - T16.G3.03
  - T22.G6.02
  - T22.G6.03

**Issues Found**:
  - X-2 rule violation: depends on T16.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T16.G3.05 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T16.G3.03 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

**Recommended Removals**:
  - T16.G3.01: Grade 3 violates X-2 rule for grade 6
  - T16.G3.05: Grade 3 violates X-2 rule for grade 6
  - T16.G3.03: Grade 3 violates X-2 rule for grade 6

---

#### T22.G6.05
**Skill**: Display streaming responses in real-time

**Description**: Students implement streaming mode responses using the `update last chat message to [MESSAGE] for chat [CHATNAME]` block to show text appearing word-by-word as the AI generates it. They compare the use...

**Current Dependencies**: 13
  - T22.G6.01
  - T22.G6.01
  - T22.G6.02
  - T22.G6.03
  - T22.G6.01
  - T22.G6.02
  - T22.G6.03
  - T22.G6.02
  - T22.G6.03
  - T22.G6.06
  - T22.G6.02
  - T22.G6.03
  - T22.G6.06

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T22.G6.07
**Skill**: Debug off-topic responses by rewriting prompts

**Description**: Students investigate cases where the bot rambles, ignores instructions, or refuses to answer. They edit the system message, add clarifying phrases, or insert reminders about format, then re-run the ch...

**Current Dependencies**: 6
  - T06.G4.08
  - T08.G4.01
  - T09.G4.04
  - T22.G4.01
  - T22.G5.01
  - T22.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T22.G6.08
**Skill**: Use multiple chatbot sessions with the select chatbot block

**Description**: Students use the `select chatbot [1/2/3/4]` block to maintain separate conversation threads. They build a project where different characters (e.g., a teacher and a student) each have their own chat hi...

**Current Dependencies**: 3
  - T22.G6.01
  - T22.G6.01
  - T22.G6.04

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T02.G6.02: Animation skill needs 2 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

### T23 (4 skills)

#### T23.G6.07
**Skill**: Choose continuous vs. event-driven detection patterns

**Description**: Students compare two detection patterns: (1) continuous polling in forever loop (constantly read table and update), (2) event-driven (start detection, wait for specific condition, then act). They impl...

**Current Dependencies**: 2
  - T23.G6.04
  - T23.G6.06

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T23.G6.08
**Skill**: Track face attributes like age, gender, and accessories

**Description**: Students explore face detection attributes beyond position: estimated age range, gender classification, glasses detection, and facial hair presence. They read these attributes from the face detection ...

**Current Dependencies**: 31
  - T16.G6.01
  - T08.G3.01
  - T09.G3.01
  - T23.G5.03
  - T10.G5.04
  - T08.G3.01
  - T09.G3.01
  - T23.G6.04
  - T23.G5.05
  - T10.G5.04
  - T08.G3.01
  - T09.G3.01
  - T23.G6.09
  - T10.G5.04
  - T08.G3.01
  - T09.G3.01
  - T23.G6.09
  - T10.G5.04
  - T08.G3.01
  - T09.G3.01
  - T23.G5.05
  - T10.G5.04
  - T08.G3.01
  - T09.G3.01
  - T23.G6.10
  - T10.G5.04
  - T08.G3.01
  - T23.G6.10
  - T10.G5.04
  - T08.G3.01
  - T23.G6.10

**Issues Found**:
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T16.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts

**Recommended Removals**:
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T23.G6.11
**Skill**: Use NLP sentence analysis to extract parts of speech

**Description**: Students use natural language processing blocks to analyze sentence structure and extract parts of speech (nouns, verbs, adjectives, etc.) from recognized speech or text input. They implement applicat...

**Current Dependencies**: 3
  - T08.G3.01
  - T09.G3.01
  - T23.G6.01

**Issues Found**:
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Removals**:
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T23.G6.12
**Skill**: Compare Azure vs OpenAI Whisper speech recognition performance

**Description**: Students run comparative tests between the default speech recognition (Azure) and OpenAI Whisper API. They test both systems with the same audio samples in different conditions: clear speech, accented...

**Current Dependencies**: 3
  - T08.G3.01
  - T09.G3.01
  - T23.G6.03

**Issues Found**:
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T02.G6.02: Animation skill needs 2 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

**Recommended Removals**:
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6

---

### T24 (10 skills)

#### T24.G6.01
**Skill**: Provide complete context when asking XO to debug

**Description**: Students assemble a "debug packet" with the bug description, relevant script, and what they expected. XO returns a fix; students evaluate whether it addresses the issue and annotate any manual tweaks.

**Current Dependencies**: 4
  - T06.G4.01
  - T09.G4.04
  - T24.G5.03
  - T24.G5.05

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T24.G6.02
**Skill**: Verify XO's explanation against the project

**Description**: Students ask XO "Explain how this script works," then compare the explanation to the actual code. They highlight any mismatches (missing variable, wrong loop) and either accept or correct the AI expla...

**Current Dependencies**: 6
  - T06.G4.01
  - T07.G4.01
  - T08.G4.01
  - T09.G4.01
  - T24.G5.03
  - T24.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T24.G6.03
**Skill**: Generate and deliver a quiz using XO

**Description**: Students prompt XO for three multiple-choice questions about a chosen topic (loops, events), then vet each question for clarity and accuracy before sharing it with classmates via widgets.

**Current Dependencies**: 4
  - T06.G4.01
  - T09.G4.04
  - T24.G5.05
  - T24.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T24.G6.04
**Skill**: Generate custom images with the DALL-E block

**Description**: Students use the `DALL-E generate image with request [DESCRIPTION]` block to create custom images based on detailed prompts. They understand the difference between searching the AI image library (G4.0...

**Current Dependencies**: 6
  - T09.G4.04
  - T24.G5.04
  - T24.G5.05
  - T24.G4.02
  - T24.G5.04
  - T24.G5.11

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T24.G6.05
**Skill**: Use AI sentence analysis to identify parts of speech

**Description**: Students use the `analyze sentence [TEXT] and write into table [TABLENAME]` block to parse sentences and identify nouns, verbs, adjectives, and other parts of speech. The block automatically creates a...

**Current Dependencies**: 8
  - T06.G4.01
  - T09.G4.01
  - T10.G4.03
  - T24.G5.05
  - T24.G6.04
  - T24.G4.02
  - T24.G4.06
  - T24.G5.05

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T24.G6.06
**Skill**: Manage ChatGPT sessions explicitly

**Description**: Students modify their ChatGPT block usage from G5.07 to explicitly control sessions using the `session: new chat` vs `session: continue` parameters. They ask a series of related questions (e.g., "What...

**Current Dependencies**: 17
  - T08.G4.01
  - T09.G4.04
  - T24.G5.05
  - T24.G6.05
  - T06.G4.01
  - T08.G4.01
  - T24.G4.05
  - T06.G4.01
  - T08.G4.01
  - T24.G4.05
  - T24.G6.07
  - T08.G4.01
  - T24.G4.05
  - T24.G6.07
  - T24.G6.07
  - T24.G5.07
  - T08.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T24.G6.08
**Skill**: Build a multi-turn chatbot using LLM sessions

**Description**: Students use the `ChatGPT request` block with `session: continue` to maintain conversation context across multiple exchanges. They build an interactive chatbot that remembers previous questions and pr...

**Current Dependencies**: 4
  - T07.G4.01
  - T08.G4.01
  - T24.G6.08
  - T24.G6.05

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T24.G6.09
**Skill**: Build interactive games with body tracking

**Description**: Students combine 2D body position reading with conditionals to build interactive games responding to body movements. They create projects where players control gameplay through physical movements like...

**Current Dependencies**: 16
  - T24.G6.04
  - T09.G4.01
  - T06.G4.01
  - T24.G5.09
  - T24.G5.05
  - T24.G6.10
  - T09.G4.01
  - T08.G4.01
  - T24.G6.10
  - T06.G4.01
  - T24.G6.10
  - T24.G5.05
  - T09.G4.01
  - T24.G6.11
  - T08.G4.01
  - T24.G6.11

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T24.G6.12
**Skill**: Use ChatGPT vision with costume attachment

**Description**: Students use the `attach costume [COSTUMENAME] to chat` block before ChatGPT requests to enable vision analysis. They send images with prompts like "Describe this scene" or "What objects do you see?" ...

**Current Dependencies**: 3
  - T06.G4.01
  - T24.G5.07
  - T24.G6.09

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T24.G6.13
**Skill**: Use web search blocks for real-time information

**Description**: Students use the `web search [QUERY] store top (K) in table [TABLENAME]` block to retrieve current information from the web. The block returns results in a table with 3 columns: title, link, and snipp...

**Current Dependencies**: 4
  - T06.G4.01
  - T09.G4.01
  - T24.G4.06
  - T24.G6.05

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T25 (4 skills)

#### T25.G6.01
**Skill**: Document metadata for datasets

**Description**: Students create a metadata documentation table in CreatiCode with columns: FieldName, Description, DataType, Units, ValidRange. They complete metadata tables for a project dataset, documenting each fi...

**Current Dependencies**: 3
  - T25.G5.01
  - T25.G4.04
  - T25.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T25.G6.02
**Skill**: Explain lossy vs lossless representation

**Description**: Learners compare representing a path as every coordinate (lossless) vs key checkpoints (lossy) and discuss tradeoffs. Students implement both approaches in CreatiCode: store a sprite's position every ...

**Current Dependencies**: 2
  - T25.G5.03
  - T25.G4.03

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T25.G6.03
**Skill**: Nest tables and lists within each other

**Description**: Students design and implement nested data structures using CreatiCode tables and lists. They practice creating a table where one column stores lists (e.g., a player table with Name, Score, and Invento...

**Current Dependencies**: 2
  - T25.G5.01
  - T25.G5.03

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T25.G6.04
**Skill**: Apply normalization to a game database

**Description**: Students take a denormalized game database (Players table with repeated team info per player, scores repeated multiple times) and normalize it through 1NF, 2NF, and 3NF. They create separate tables (P...

**Current Dependencies**: 16
  - T25.G5.04
  - T25.G5.02
  - T25.G5.06
  - T25.G4.06
  - T25.G6.05
  - T25.G6.05
  - T25.G5.01
  - T25.G6.06
  - T25.G5.06
  - T25.G6.07
  - T25.G5.01
  - T25.G5.03
  - T25.G7.01
  - T25.G6.03
  - T25.G7.01
  - T25.G7.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T26 (8 skills)

#### T26.G6.01
**Skill**: Map stakeholder questions to data requirements

**Description**: Students receive stakeholder questions ("Which level is hardest?") and specify what data to collect (attempt count, completion time), aligning collection with analysis goals.

**Current Dependencies**: 5
  - T08.G4.01
  - T09.G4.01
  - T09.G4.04
  - T10.G4.02
  - T26.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

#### T26.G6.02
**Skill**: Automate logging from three different sensors

**Description**: Learners combine blocks to record data from three different sensor types (face detection, hand tracking, microphone level) simultaneously into a unified table, ensuring all data streams are captured w...

**Current Dependencies**: 5
  - T06.G4.01
  - T09.G4.04
  - T10.G4.02
  - T26.G5.04
  - T26.G5.09

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T26.G6.03
**Skill**: Create consent and opt-out workflows with widget dialogs

**Description**: Students implement dialog widget blocks that explain what will be collected, gather explicit user consent, and disable logging when declined, following privacy-by-design principles.

**Current Dependencies**: 5
  - T08.G4.01
  - T09.G4.04
  - T10.G4.02
  - T26.G4.04
  - T26.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T26.G6.04
**Skill**: Understand document structure for database collections

**Description**: Students examine how table rows (with column names as fields) map to database documents with field-value pairs, understanding the data structure transformation between tables and NoSQL documents.

**Current Dependencies**: 7
  - T08.G4.01
  - T09.G4.01
  - T09.G4.04
  - T10.G4.02
  - T26.G5.03
  - T10.G4.02
  - T26.G5.05

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T02.G6.02: Animation skill needs 2 concepts

---

#### T26.G6.05
**Skill**: Sort database query results

**Description**: Students add sorting criteria to their database queries to retrieve data in specific order (ascending/descending by field), learning to organize query results for analysis.

**Current Dependencies**: 13
  - T10.G4.02
  - T26.G5.05
  - T26.G6.01
  - T26.G6.05
  - T08.G5.02
  - T10.G4.02
  - T26.G6.06
  - T08.G5.02
  - T10.G4.02
  - T26.G6.06
  - T26.G5.05
  - T10.G6.01
  - T26.G6.06

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T26.G6.07
**Skill**: Import data from Google Sheets into tables

**Description**: Students use Google Sheets integration blocks to pull data from shared spreadsheets into CreatiCode tables, enabling collaboration and data collection from external sources.

**Current Dependencies**: 2
  - T10.G4.02
  - T26.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

---

#### T26.G6.08
**Skill**: Export tables to Google Sheets

**Description**: Learners push their collected data tables to Google Sheets for sharing with teammates or further analysis in spreadsheet tools, understanding data export workflows.

**Current Dependencies**: 3
  - T10.G4.02
  - T26.G5.04
  - T26.G6.07

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

---

#### T26.G6.09
**Skill**: Log multiplayer game session data

**Description**: Students implement data collection in multiplayer games to track player interactions, scores, and events across multiple connected users, learning to handle concurrent data streams and player identifi...

**Current Dependencies**: 3
  - T10.G4.02
  - T26.G5.06
  - T26.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

### T27 (4 skills)

#### T27.G6.01
**Skill**: Combine data from two tables

**Description**: Students learn to merge data from two related tables using lookups iteratively, copying matching rows into a new combined table. This prepares for database-style JOIN operations in data analysis.

**Current Dependencies**: 9
  - T27.G4.02
  - T09.G4.01
  - T09.G4.04
  - T26.G4.04
  - T27.G5.03
  - T27.G6.01
  - T27.G5.01
  - T09.G4.04
  - T27.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

---

#### T27.G6.02
**Skill**: Create pivot tables for multi-dimensional analysis

**Description**: Students use 'pivot [data v] into [summary v] row groups [grade,gender] columns [score] methods [average]' to create multi-dimensional summaries (e.g., average scores broken down by both grade AND gen...

**Current Dependencies**: 6
  - T08.G4.01
  - T09.G4.04
  - T26.G4.04
  - T27.G6.01
  - T27.G5.01
  - T10.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T27.G6.03
**Skill**: Export and import data using CSV files

**Description**: Students use 'export table [data v] as [analysis_results]' to save analysis results as CSV files for sharing, and 'import file into table [imported v]' to load external data. This enables real-world d...

**Current Dependencies**: 5
  - T27.G5.02
  - T27.G6.01
  - T09.G4.04
  - T27.G6.01
  - T06.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T27.G6.04
**Skill**: Create structured summaries with labeled findings

**Description**: Learners condense findings into structured text formats using consistent labels: METRIC (key number), INSIGHT (pattern observed), ACTION (recommended next step). These structured summaries can be used...

**Current Dependencies**: 5
  - T06.G4.01
  - T09.G4.01
  - T09.G4.04
  - T26.G4.04
  - T27.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T28 (10 skills)

#### T28.G6.02
**Skill**: Use random seeds for reproducibility

**Description**: Students populate a list with seeded random numbers using 'set [list] to (N) random numbers with seed (SEED)', then draw values from this list sequentially to create reproducible random sequences in t...

**Current Dependencies**: 3
  - T28.G5.04
  - T09.G5.01
  - T07.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T02.G6.02: Animation skill needs 2 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T28.G6.03
**Skill**: Measure percent error vs theoretical probability

**Description**: Students calculate percent error between observed frequencies and expected probabilities, stating whether the error is acceptable.

**Current Dependencies**: 2
  - T28.G5.06
  - T28.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T27.G3.01

**Recommended Additions**:
  - T02.G6.02: Animation skill needs 2 concepts

---

#### T28.G6.04
**Skill**: Simulate noisy sensors for AI perception testing

**Description**: Students generate synthetic sensor data with realistic variation (e.g., pose coordinates that vary within ±10 pixels, voice confidence scores between 0.7-0.95) to test AI perception logic without need...

**Current Dependencies**: 3
  - T28.G5.03
  - T28.G5.04
  - T08.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T27.G3.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T28.G6.05
**Skill**: Model a simple agent in a grid world

**Description**: Students create a sprite that tracks its position and facing direction in a grid (using x,y coordinates and a direction variable). They implement basic movement rules (move forward one grid square, tu...

**Current Dependencies**: 2
  - T28.G5.08
  - T28.G5.04

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T28.G6.06
**Skill**: Simulate events with changing probabilities

**Description**: Students build a simulation where one event's probability depends on a previous outcome (e.g., drawing cards without replacement, weather patterns where today's weather affects tomorrow's probability)...

**Current Dependencies**: 2
  - T28.G5.01
  - T28.G5.06

**Issues Found**:
  - Potential circular dependency: Circular: T27.G3.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T28.G6.10
**Skill**: Compare sampling methods (random, systematic, stratified)

**Description**: Students implement and compare three sampling methods to collect data from a simulated population: random sampling (pick any items), systematic sampling (every Nth item), and stratified sampling (ensu...

**Current Dependencies**: 2
  - T28.G5.02
  - T28.G5.11

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T28.G6.11
**Skill**: Calculate and interpret conditional probability

**Description**: Students calculate the probability of an event given that another event has occurred (e.g., probability of drawing a red marble given that the first marble was blue and not replaced). They use simulat...

**Current Dependencies**: 2
  - T28.G6.06
  - T28.G5.05

**Issues Found**:
  - Potential circular dependency: Circular: T27.G3.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts

---

#### T28.G6.07
**Skill**: Design an environment with obstacles and goals

**Description**: Students add walls (as sprites or using collision detection) and goal locations to their grid world. The agent detects when it hits a wall (can't move) or reaches a goal (mission complete). They test ...

**Current Dependencies**: 2
  - T28.G6.05
  - T08.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T28.G6.08
**Skill**: Implement reward rules and track outcomes

**Description**: Students add a score variable that increases when the agent reaches goals and decreases when hitting walls. They run 10 trials with random starting positions and log the agent's final score for each t...

**Current Dependencies**: 2
  - T28.G6.07
  - T09.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

#### T28.G6.09
**Skill**: Create simple two-sprite interaction

**Description**: Students build a project with two sprites that can detect each other and respond (e.g., one sprite changes color when touching the other, or sprites bounce away from each other). They use broadcasting...

**Current Dependencies**: 2
  - T28.G6.05
  - T06.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Animation skill needs 2 concepts
  - T04.G6.01: Sensing skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T29 (9 skills)

#### T29.G6.01
**Skill**: Compare characters, words, and token counts

**Description**: Students count characters (using "length of"), words (using split and count), and discuss GPT tokens. They note that actual token counting requires API calls; they estimate based on character/word cou...

**Current Dependencies**: 6
  - T29.G5.10
  - T29.G5.03
  - T29.G4.03
  - T08.G4.01
  - T09.G4.04
  - T10.G4.03

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T29.G6.02
**Skill**: Compute n-gram (bigram) frequencies

**Description**: Learners loop through token lists, join consecutive word pairs, and store counts in a table to capture common two-word phrase patterns.

**Current Dependencies**: 5
  - T29.G5.03
  - T11.G5.01
  - T07.G4.01
  - T09.G4.04
  - T10.G4.03

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T29.G6.03
**Skill**: Create autocomplete suggestions from bigrams

**Description**: Using bigram frequency data, students identify the top next words for a given prefix and display them using text display blocks, sprites, or list displays.

**Current Dependencies**: 4
  - T29.G6.02
  - T06.G4.01
  - T09.G4.04
  - T10.G4.03

**Issues Found**:
  - Potential circular dependency: Circular: T07.G3.02

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T29.G6.04
**Skill**: Log AI prompts/responses with ratings and timestamps

**Description**: Learners automatically log each AI interaction (prompt, response, user rating, timestamp) into a table for responsible-use tracking, supporting T24 transparency practices.

**Current Dependencies**: 6
  - T29.G5.02
  - T29.G5.05
  - T11.G5.01
  - T07.G4.01
  - T09.G4.04
  - T10.G4.03

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T29.G6.06
**Skill**: Convert speech to text using voice recognition

**Description**: Students use CreatiCode's speech-to-text blocks (Azure or OpenAI Whisper) to convert spoken input into text, then process the text using split, clean, and analysis techniques.

**Current Dependencies**: 2
  - T29.G5.02
  - T29.G5.07

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T29.G6.07
**Skill**: Convert text to speech with voice selection

**Description**: Students use CreatiCode's text-to-speech blocks (Azure TTS) to read text aloud, experimenting with different voices and languages. They discuss accessibility applications.

**Current Dependencies**: 1
  - T29.G4.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

---

#### T29.G6.08
**Skill**: Compare text similarity using edit distance

**Description**: Students use the text similarity block (operator_stringdiff) to compute edit distance (how many character changes needed to transform one text into another), understanding text similarity metrics.

**Current Dependencies**: 2
  - T29.G4.03
  - T29.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T29.G6.09
**Skill**: Handle text length limits and truncation

**Description**: Students check text length before sending to AI APIs, truncate or summarize long texts to fit limits, and display appropriate error messages when text is too long.

**Current Dependencies**: 2
  - T29.G6.01
  - T08.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T29.G6.10
**Skill**: Use Pinecone semantic search blocks (advanced)

**Description**: Advanced students use "add table to Pinecone" and "search from Pinecone" blocks for embedding-based semantic retrieval, comparing results to keyword-based retrieval and understanding the difference be...

**Current Dependencies**: 9
  - T29.G6.01
  - T08.G5.01
  - T29.G5.03
  - T29.G6.02
  - T29.G6.03
  - T11.G6.01
  - T09.G3.05
  - T10.G5.03
  - T29.G7.01

**Issues Found**:
  - X-2 rule violation: depends on T09.G3.05 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T02.G6.02: Animation skill needs 2 concepts

**Recommended Removals**:
  - T09.G3.05: Grade 3 violates X-2 rule for grade 6

---

### T30 (6 skills)

#### T30.G6.01
**Skill**: Analyze sensor specifications for CreatiCode projects

**Description**: Students read simplified spec sheets for cameras and microphones used in CreatiCode and decide which specifications (resolution, sample rate, frame rate) are important for different project types (fac...

**Current Dependencies**: 2
  - T30.G5.03
  - T30.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T04.G6.01: Sensing skill needs 4 concepts

---

#### T30.G6.02
**Skill**: Compare browser storage options for CreatiCode projects

**Description**: Learners compare storage methods in CreatiCode (cloud save, local browser storage, export to device) based on accessibility, persistence, and sharing capabilities.

**Current Dependencies**: 2
  - T30.G5.01
  - T30.G3.03

**Issues Found**:
  - X-2 rule violation: depends on T30.G3.03 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Removals**:
  - T30.G3.03: Grade 3 violates X-2 rule for grade 6

---

#### T30.G6.03
**Skill**: Explain camera and microphone privacy permissions

**Description**: Students explain why browsers require camera and microphone permissions, how CreatiCode projects request device access, and why these permissions protect user privacy from malicious apps.

**Current Dependencies**: 3
  - T30.G5.02
  - T30.G3.05
  - T30.G3.06

**Issues Found**:
  - X-2 rule violation: depends on T30.G3.05 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T30.G3.06 (grade 3), should be >= grade 4

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

**Recommended Removals**:
  - T30.G3.05: Grade 3 violates X-2 rule for grade 6
  - T30.G3.06: Grade 3 violates X-2 rule for grade 6

---

#### T30.G6.04
**Skill**: Plan device capability checklists for CreatiCode AI projects

**Description**: Learners create checklists specifying device requirements for CreatiCode AI features (camera resolution for face detection, microphone quality for speech recognition, internet speed for cloud APIs), e...

**Current Dependencies**: 2
  - T30.G5.01
  - T30.G5.03

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T30.G6.05
**Skill**: Use webcam as 3D scene background for AR effects

**Description**: Students use the "turn on webcam background" block to overlay 3D objects on live camera feeds, select front/back camera, configure flip modes (normal, left-right flipped, up-down flipped), and create ...

**Current Dependencies**: 4
  - T30.G3.06
  - T30.G5.01
  - T30.G5.05
  - T30.G6.04

**Issues Found**:
  - X-2 rule violation: depends on T30.G3.06 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

**Recommended Removals**:
  - T30.G3.06: Grade 3 violates X-2 rule for grade 6

---

#### T30.G6.06
**Skill**: Implement 3D object dragging with mouse

**Description**: Students configure 3D objects to be draggable using "set dragging mode" (specifying drag direction constraints), create event handlers for "when this 3D object starts dragging" and "when this 3D objec...

**Current Dependencies**: 6
  - T30.G5.06
  - T30.G4.05
  - T30.G6.06
  - T30.G5.05
  - T30.G5.05
  - T30.G4.05

**Issues Found**:
  - Potential circular dependency: Circular: T09.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T31 (6 skills)

#### T31.G6.01
**Skill**: Trace the steps of an HTTP/HTTPS request

**Description**: Students identify the sequence: client sends request, server processes, server responds, client renders, and—if HTTPS—encryption occurs before transit. CSTA: MS-SAS-NW-06

**Current Dependencies**: 1
  - T31.G5.01

**Recommended Additions**:
  - T02.G6.02: Animation skill needs 2 concepts

---

#### T31.G6.02
**Skill**: Read data from a Google Sheet cell

**Description**: Students use CreatiCode's Google Sheets integration to read data from a specific cell or range of cells in a shared spreadsheet and display it in their project. This introduces cloud-based data sharin...

**Current Dependencies**: 1
  - T31.G5.03

---

#### T31.G6.03
**Skill**: Manage Google Sheets structure programmatically

**Description**: Students use CreatiCode's blocks to insert and remove rows and columns in Google Sheets programmatically, and clear entire sheets. They apply these operations to dynamically restructure data as their ...

**Current Dependencies**: 4
  - T31.G6.02
  - T31.G6.03
  - T31.G6.03
  - T31.G6.03

**Issues Found**:
  - Potential circular dependency: Circular: T31.G6.03

---

#### T31.G6.04
**Skill**: Measure and analyze how latency affects AI responsiveness and fairness

**Description**: Students use timer blocks to measure network latency in scenarios where it affects T22 chatbot conversations, T21 image generation feedback, and T23 real-time gesture recognition. They record and comp...

**Current Dependencies**: 2
  - T31.G5.01
  - T31.G5.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T31.G6.05
**Skill**: Evaluate privacy when sharing AI-generated content and data

**Description**: Students review datasets containing T24 XO conversation logs, T21 generated images, T23 sensor recordings, and T22 chatbot interactions. They decide when to anonymize prompts, restrict access to AI ou...

**Current Dependencies**: 2
  - T31.G5.01
  - T31.G5.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T31.G6.06
**Skill**: Manage players and game state in multiplayer sessions

**Description**: Students use CreatiCode's multiplayer blocks to list all players currently in a game session, remove sprites from the game world, and reset the entire game state. They understand how to manage the lif...

**Current Dependencies**: 3
  - T31.G5.04
  - T31.G5.05
  - T31.G6.06

**Issues Found**:
  - Potential circular dependency: Circular: T31.G5.04

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

### T32 (8 skills)

#### T32.G6.01
**Skill**: Identify common malware types

**Description**: Students learn about malware including viruses (self-replicating code), ransomware (holds data hostage), spyware (monitors activity), and trojans (disguised as legitimate software). For each type, the...

**Current Dependencies**: 2
  - T32.G4.03
  - T32.G5.01

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T32.G6.02
**Skill**: Recognize phishing attack patterns and warning signs

**Description**: Students analyze phishing attacks in depth: fake emails requesting login credentials, impersonation of trusted organizations, urgent language to pressure action, and suspicious links. They examine rea...

**Current Dependencies**: 1
  - T32.G6.01

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T32.G6.03
**Skill**: Understand network attacks (DoS, MitM)

**Description**: Students learn about network-level attacks: denial-of-service (DoS) attacks that overload systems making them unavailable, and man-in-the-middle (MitM) attacks that intercept communications. They disc...

**Current Dependencies**: 1
  - T32.G6.01

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T32.G6.04
**Skill**: Learn about database vulnerabilities (SQL injection basics)

**Description**: Students learn conceptually about SQL injection attacks where attackers insert malicious code into input fields to manipulate databases. Through simplified examples (no actual SQL coding), they unders...

**Current Dependencies**: 1
  - T32.G6.01

---

#### T32.G6.05
**Skill**: Design secure login flows in CreatiCode apps

**Description**: Students design a CreatiCode UI that implements basic login security: (1) Check password length (minimum 8 characters using string length blocks), (2) Display password as dots/asterisks instead of pla...

**Current Dependencies**: 6
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T16.G3.01
  - T32.G4.02

**Issues Found**:
  - X-2 rule violation: depends on T07.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
  - X-2 rule violation: depends on T16.G3.01 (grade 3), should be >= grade 4
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

**Recommended Removals**:
  - T07.G3.01: Grade 3 violates X-2 rule for grade 6
  - T08.G3.01: Grade 3 violates X-2 rule for grade 6
  - T16.G3.01: Grade 3 violates X-2 rule for grade 6

---

#### T32.G6.06
**Skill**: Conduct AI-specific threat modeling for class projects

**Description**: Students analyze their AI-powered apps and identify AI-specific threats: prompt injection (tricking chatbots with special inputs), bias amplification (AI learning from unfair data), and inappropriate ...

**Current Dependencies**: 5
  - T21.G6.02
  - T22.G6.01
  - T23.G5.01
  - T32.G5.01
  - T32.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T32.G6.07
**Skill**: Analyze ethical hacking vs malicious hacking through case studies

**Description**: Students read simplified bug bounty reports and analyze: (1) What was the vulnerability discovered? (2) How did the researcher report it responsibly? (3) Why was getting permission crucial? They role-...

**Current Dependencies**: 2
  - T32.G6.01
  - T32.G4.03

---

#### T32.G6.08
**Skill**: Explore simple cipher techniques with alphabet position lookup

**Description**: Students use CreatiCode blocks to shift letters using alphabet position. They create a simple encoder that: (1) Sets an alphabet string variable to "ABCDEFGHIJKLMNOPQRSTUVWXYZ", (2) For each letter in...

**Current Dependencies**: 2
  - T10.G4.01
  - T32.G5.09

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T33 (10 skills)

#### T33.G6.01
**Skill**: Identify and test Cloud blocks for network dependencies

**Description**: Students examine CreatiCode's Cloud category blocks and identify which require internet connectivity: Google Sheets operations (read, write, manage), web fetch, and Google Drive access. They test thes...

**Current Dependencies**: 5
  - T08.G4.01
  - T09.G4.04
  - T31.G5.01
  - T33.G5.01
  - T33.G5.03

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T02.G6.02: Animation skill needs 2 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T33.G6.02
**Skill**: Fetch web content using the fetch URL block

**Description**: Students use the `fetch web page as markdown from URL` block to retrieve content from a public URL and display it in their project. They learn that the block converts HTML to markdown and understand t...

**Current Dependencies**: 5
  - T08.G4.01
  - T09.G4.01
  - T31.G5.01
  - T33.G5.03
  - T33.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T33.G6.03
**Skill**: Read data from Google Sheets into a table

**Description**: Students use the `read from google sheet` block to load data from a shared Google Sheet into a CreatiCode table. They specify the sheet URL, sheet name, range, and target table, then iterate through t...

**Current Dependencies**: 4
  - T08.G4.01
  - T10.G4.01
  - T31.G5.01
  - T33.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T33.G6.04
**Skill**: Write data from a table to Google Sheets

**Description**: Students use the `write into google sheet` block to export a CreatiCode table to a Google Sheet. They specify the starting cell and understand that this writes the entire table including headers. They...

**Current Dependencies**: 4
  - T08.G4.01
  - T10.G4.01
  - T31.G5.01
  - T33.G6.03

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T33.G6.05
**Skill**: Clear a Google Sheet to reset data

**Description**: Students use the `clear sheet` block to remove all content from a specified sheet while keeping the sheet itself intact. They learn when clearing is preferable to deleting (preserving sheet structure ...

**Current Dependencies**: 4
  - T08.G4.01
  - T31.G5.01
  - T33.G6.03
  - T33.G6.04

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

---

#### T33.G6.06
**Skill**: Handle latency and error states in service calls

**Description**: Students design UI patterns (loading messages, "try again" buttons) that respond gracefully when Cloud blocks or AI blocks take too long or fail. They detect error states by checking for empty respons...

**Current Dependencies**: 4
  - T08.G4.01
  - T09.G4.01
  - T31.G5.01
  - T33.G6.02

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Drawing skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T33.G6.07
**Skill**: Respect usage limits and rate limiting

**Description**: Learners implement counters and cool-down timers so projects don't spam external service blocks (AI or Cloud). They create a call counter that prevents additional requests until a timer expires, under...

**Current Dependencies**: 4
  - T07.G4.01
  - T09.G4.01
  - T31.G5.01
  - T33.G6.06

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T33.G6.08
**Skill**: Apply privacy principles to Google Sheet URLs

**Description**: Students apply their understanding of URL sharing (from T33.G5.03) specifically to Google Sheets integration. They practice checking sheet permissions before integrating, creating test sheets with fic...

**Current Dependencies**: 3
  - T33.G5.03
  - T33.G6.03
  - T33.G6.04

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

#### T33.G6.09
**Skill**: Understand cloud database collections versus Google Sheets

**Description**: Students compare CreatiCode's cloud database collections with Google Sheets to understand when each is appropriate. They learn that collections are like spreadsheet tables but stored on CreatiCode's s...

**Current Dependencies**: 3
  - T10.G5.01
  - T31.G5.01
  - T33.G6.03

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts

---

#### T33.G6.10
**Skill**: Insert and fetch data from cloud database collections

**Description**: Students use `insert from table into collection` to save CreatiCode table data to a cloud collection, and `fetch from collection` to retrieve it back into a table. They create simple data logging proj...

**Current Dependencies**: 4
  - T08.G5.01
  - T10.G5.01
  - T31.G5.01
  - T33.G6.09

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T13.G6.03: Cloning skill needs 13 concepts

---

### T34 (3 skills)

#### T34.G6.01
**Skill**: Analyze major waves of computing (mainframe → personal computer → internet → mobile → AI), identifying what each wave made possible and what barriers remained

**Description**: Students build comparison charts showing key characteristics (dominant hardware, typical users, limitations) for each computing era and make predictions about the next wave.

**Current Dependencies**: 2
  - T34.G4.01
  - T34.G5.02

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts

---

#### T34.G6.02
**Skill**: Evaluate historical inclusion and exclusion in computing, including how user interface evolution (command line → GUI → touchscreen → voice) has changed who can use computers

**Description**: Learners examine who gained or lacked access to computing historically (by cost, geography, language, disability) and connect these patterns to current access barriers and inclusion efforts.

**Current Dependencies**: 2
  - T34.G5.01
  - T34.G4.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts
  - T02.G6.02: Drawing skill needs 2 concepts

---

#### T34.G6.03
**Skill**: Analyze historical computing failures (e.g., Therac-25, Y2K, failed AI systems) to identify lessons for preventing similar problems today

**Description**: Students study famous software bugs and system failures (Ariane 5 rocket, Y2K problem, Therac-25) and explain what lessons these events taught the computing industry.

**Current Dependencies**: 2
  - T34.G5.01
  - T34.G4.01

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

### T35 (3 skills)

#### T35.G6.01
**Skill**: Apply ethics lenses (beneficence, fairness, autonomy)

**Description**: Students apply three ethics lenses to evaluate CreatiCode projects (their own or community examples): Beneficence (Does this help people? Who benefits most? - Use ChatGPT blocks to analyze project pur...

**Current Dependencies**: 4
  - T16.G6.01
  - T35.G5.01
  - T35.G4.01
  - T22.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T16.G3.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T35.G6.02
**Skill**: Develop ethics guidelines for AI perception and assistance (T23-T24)

**Description**: Students actively test AI perception and assistance tools to develop evidence-based guidelines. For T23 (Perception): Test hand/body tracking with different skin tones and lighting, documenting accura...

**Current Dependencies**: 19
  - T35.G5.01
  - T35.G4.02
  - T16.G6.01
  - T19.G6.01
  - T35.G6.02
  - T16.G6.01
  - T19.G6.01
  - T35.G6.05
  - T16.G6.01
  - T19.G6.01
  - T35.G5.03
  - T35.G4.03
  - T21.G6.01
  - T22.G6.01
  - T35.G6.03
  - T16.G6.01
  - T35.G5.03
  - T23.G6.01
  - T24.G6.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T02.G6.02: Game skill needs 2 concepts
  - T03.G6.02: Game skill needs 3 concepts
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts

---

#### T35.G6.04
**Skill**: Examine digital divide data

**Description**: Learners interpret charts (broadband availability, device ownership) and propose community actions.

**Current Dependencies**: 1
  - T35.G5.01

**Issues Found**:
  - Potential circular dependency: Circular: T08.G3.00

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts

---

### T36 (5 skills)

#### T36.G6.01
**Skill**: Connect AI skills to career pathways

**Description**: Students examine how AI skills (image generation, chatbots, voice/vision recognition) connect to real-world AI career roles and identify strategies for building AI expertise.

**Current Dependencies**: 4
  - T36.G5.01
  - T36.G4.01
  - T36.G5.03
  - T36.G5.01

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T36.G6.02
**Skill**: Practice stand-ups, task boards, and sprint reviews in team projects

**Description**: Teams run daily stand-up check-ins ("yesterday/today/blocked"), maintain task boards, and hold weekly sprint reviews; they track action items and reflect on progress.

**Current Dependencies**: 2
  - T36.G5.02
  - T36.G4.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T36.G6.03
**Skill**: Analyze job descriptions for skills/values

**Description**: Students annotate simplified postings to highlight technical skills, collaboration traits, and values (accessibility, ethics).

**Current Dependencies**: 2
  - T36.G5.01
  - T36.G4.04

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts

---

#### T36.G6.04
**Skill**: Add ethics clauses to team charters

**Description**: Learners amend team charters with commitments about responsible AI use, crediting sources and collaborators, protecting user data, and ensuring accessibility.

**Current Dependencies**: 1
  - T36.G5.02

**Recommended Additions**:
  - T05.G6.01: Ai skill needs 5 concepts
  - T04.G6.01: Ai skill needs 4 concepts
  - T11.G6.03: Data Viz skill needs 11 concepts

---

#### T36.G6.05
**Skill**: Document project contributions for a portfolio

**Description**: Students write brief summaries of their CreatiCode projects including their role, skills used, and what they learned, creating the foundation for future portfolios.

**Current Dependencies**: 2
  - T36.G5.02
  - T36.G5.01

---


## X-2 Rule Violations

- **T01.G6.03**: X-2 rule violation: depends on T06.G3.01 (grade 3), should be >= grade 4
- **T01.G6.04**: X-2 rule violation: depends on T07.G3.01 (grade 3), should be >= grade 4
- **T01.G6.04**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T01.G6.07**: X-2 rule violation: depends on T07.G3.01 (grade 3), should be >= grade 4
- **T01.G6.07**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T03.G6.01**: X-2 rule violation: depends on T06.G3.01 (grade 3), should be >= grade 4
- **T03.G6.02**: X-2 rule violation: depends on T06.G3.01 (grade 3), should be >= grade 4
- **T04.G6.04**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T04.G6.06**: X-2 rule violation: depends on T07.G3.01 (grade 3), should be >= grade 4
- **T04.G6.06**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T06.G6.01**: X-2 rule violation: depends on T06.G3.06 (grade 3), should be >= grade 4
- **T06.G6.05**: X-2 rule violation: depends on T16.G3.02 (grade 3), should be >= grade 4
- **T10.G6.06**: X-2 rule violation: depends on T10.G3.06 (grade 3), should be >= grade 4
- **T10.G6.07**: X-2 rule violation: depends on T10.G3.06 (grade 3), should be >= grade 4
- **T13.G6.01**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T13.G6.02**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T16.G6.03**: X-2 rule violation: depends on T16.G3.07 (grade 3), should be >= grade 4
- **T16.G6.04**: X-2 rule violation: depends on T16.G3.08 (grade 3), should be >= grade 4
- **T17.G6.03**: X-2 rule violation: depends on T07.G3.05 (grade 3), should be >= grade 4
- **T18.G6.03**: X-2 rule violation: depends on T07.G3.01 (grade 3), should be >= grade 4
- **T18.G6.03**: X-2 rule violation: depends on T11.G3.01 (grade 3), should be >= grade 4
- **T22.G6.03**: X-2 rule violation: depends on T16.G3.01 (grade 3), should be >= grade 4
- **T22.G6.03**: X-2 rule violation: depends on T16.G3.05 (grade 3), should be >= grade 4
- **T22.G6.03**: X-2 rule violation: depends on T16.G3.03 (grade 3), should be >= grade 4
- **T23.G6.08**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T23.G6.08**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T23.G6.08**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T23.G6.08**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T23.G6.08**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T23.G6.08**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T23.G6.08**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T23.G6.08**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T23.G6.11**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T23.G6.12**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T29.G6.10**: X-2 rule violation: depends on T09.G3.05 (grade 3), should be >= grade 4
- **T30.G6.02**: X-2 rule violation: depends on T30.G3.03 (grade 3), should be >= grade 4
- **T30.G6.03**: X-2 rule violation: depends on T30.G3.05 (grade 3), should be >= grade 4
- **T30.G6.03**: X-2 rule violation: depends on T30.G3.06 (grade 3), should be >= grade 4
- **T30.G6.05**: X-2 rule violation: depends on T30.G3.06 (grade 3), should be >= grade 4
- **T32.G6.05**: X-2 rule violation: depends on T07.G3.01 (grade 3), should be >= grade 4
- **T32.G6.05**: X-2 rule violation: depends on T08.G3.01 (grade 3), should be >= grade 4
- **T32.G6.05**: X-2 rule violation: depends on T16.G3.01 (grade 3), should be >= grade 4

## Recommendations Summary

Total skills with recommendations: 224

### T01.G6.01: Compare efficiency of linear and binary search
- Current dependencies: 1
- Issues: 0
- Additions suggested: 4
- Removals suggested: 0

### T01.G6.02: Compare how step counts grow with input size
- Current dependencies: 1
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T01.G6.03: Spot unnecessary work in an algorithm
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 1

### T01.G6.04: Revise an algorithm to do less work
- Current dependencies: 3
- Issues: 3
- Additions suggested: 0
- Removals suggested: 2

### T01.G6.05: Identify who is favored or harmed by a decision algorithm
- Current dependencies: 0
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T01.G6.06: Suggest a change to make a decision algorithm more fair
- Current dependencies: 1
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T01.G6.07: Design a flowchart for a multi‑step program
- Current dependencies: 4
- Issues: 3
- Additions suggested: 5
- Removals suggested: 2

### T01.G6.08: Implement code from a detailed flowchart
- Current dependencies: 2
- Issues: 0
- Additions suggested: 4
- Removals suggested: 0

### T02.G6.01: Learn the pseudocode generation block
- Current dependencies: 1
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T02.G6.02: Generate and read pseudocode from a simple script
- Current dependencies: 1
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T02.G6.03: Compare block code to its generated pseudocode
- Current dependencies: 1
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T02.G6.04: Use pseudocode to plan before coding
- Current dependencies: 1
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T02.G6.05: Debug using pseudocode comparison
- Current dependencies: 1
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T03.G6.01: Propose modules for a medium project
- Current dependencies: 3
- Issues: 2
- Additions suggested: 1
- Removals suggested: 1

### T03.G6.02: Identify reusable components in a complex process
- Current dependencies: 2
- Issues: 2
- Additions suggested: 2
- Removals suggested: 1

### T03.G6.03: Break a project into milestones (v1/v2/v3)
- Current dependencies: 1
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T03.G6.04: Adjust milestones when constraints are discovered
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T03.G6.05: Use XO to expand a basic idea into subtasks
- Current dependencies: 1
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T04.G6.01: Group snippets by underlying algorithm pattern
- Current dependencies: 2
- Issues: 0
- Additions suggested: 3
- Removals suggested: 0

### T04.G6.02: Identify pattern variants that look different but behave the same
- Current dependencies: 1
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T04.G6.03: Apply filter pattern with multiple criteria
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T04.G6.04: Turn repeated code into a custom block with parameters
- Current dependencies: 3
- Issues: 2
- Additions suggested: 1
- Removals suggested: 1

### T04.G6.05: Analyze a template project and identify customization points
- Current dependencies: 1
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T04.G6.06: Compare two pattern‑based solutions for efficiency and code clarity
- Current dependencies: 3
- Issues: 3
- Additions suggested: 2
- Removals suggested: 2

### T04.G6.07: Implement a pattern-based solution from a description
- Current dependencies: 2
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T04.G6.08: Access grid elements using 2D indexing patterns
- Current dependencies: 2
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T05.G6.02: Propose specific design changes to address all three HCD principles
- Current dependencies: 1
- Issues: 0
- Additions suggested: 1
- Removals suggested: 0

### T05.G6.03: Analyze short interview or survey data to extract user needs
- Current dependencies: 1
- Issues: 0
- Additions suggested: 1
- Removals suggested: 0

### T05.G6.05: Plan a simple CreatiCode simulation with variables, rules, and UI
- Current dependencies: 2
- Issues: 0
- Additions suggested: 1
- Removals suggested: 0

### T05.G6.06: Justify what is modeled vs simplified in a simulation design
- Current dependencies: 2
- Issues: 0
- Additions suggested: 1
- Removals suggested: 0

### T05.G6.07: Read a simple bar chart showing user preferences
- Current dependencies: 1
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T05.G6.08: Identify user questions a simulation should answer
- Current dependencies: 2
- Issues: 0
- Additions suggested: 3
- Removals suggested: 0

### T06.G6.01: Trace event execution paths in a multi‑event program
- Current dependencies: 3
- Issues: 2
- Additions suggested: 1
- Removals suggested: 1

### T06.G6.02: Simplify complex event logic with conditionals
- Current dependencies: 8
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T06.G6.04: Design meaningful custom broadcasts and document them
- Current dependencies: 3
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T06.G6.05: Use 'when dragging stops' for drag completion
- Current dependencies: 19
- Issues: 2
- Additions suggested: 1
- Removals suggested: 1

### T06.G6.08: Use a variable to track simple program states
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T07.G6.01: Trace nested loops with variable bounds
- Current dependencies: 4
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T07.G6.02: Refactor complex repeated patterns into loops with variables
- Current dependencies: 3
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T07.G6.03: Loop‑based search in a list
- Current dependencies: 3
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T07.G6.04: Avoid and fix infinite loops
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T07.G6.05: Trace nested loops with abstract calculations using trace tables
- Current dependencies: 3
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T07.G6.06: Trace nested loops that generate spatial patterns
- Current dependencies: 2
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T07.G6.07: Use loops to update values iteratively
- Current dependencies: 3
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T07.G6.08: Use break and continue to control loop flow
- Current dependencies: 3
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T07.G6.09: Use for-each loops to iterate over lists
- Current dependencies: 3
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T08.G6.01: Draw state transition diagram
- Current dependencies: 6
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T08.G6.02: Implement simple state machines using conditionals
- Current dependencies: 2
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T08.G6.03: Debug multi-condition logic
- Current dependencies: 3
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T09.G6.01: Model real-world quantities using variables and formulas
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T09.G6.02: Use parentheses to override operator precedence
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T09.G6.03: Use modulo (remainder) operator in expressions
- Current dependencies: 2
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T09.G6.04: Use case conversion (uppercase/lowercase) operators
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T09.G6.05: Use substring operator to extract text portions
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T09.G6.06: Understand variable persistence across events and broadcasts
- Current dependencies: 3
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T09.G6.07: Debug off-by-one and comparison operator errors
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T10.G6.01: Sort a table by a column
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T10.G6.02: Filter table rows based on a condition
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T10.G6.03: Copy and append tables
- Current dependencies: 1
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T10.G6.05: Group data and compute aggregates per group
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T10.G6.06: Use set operations on lists
- Current dependencies: 2
- Issues: 2
- Additions suggested: 0
- Removals suggested: 1

### T10.G6.07: Remove duplicate items from a list
- Current dependencies: 2
- Issues: 2
- Additions suggested: 1
- Removals suggested: 1

### T10.G6.08: Shuffle table rows randomly
- Current dependencies: 2
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T11.G6.01: Design custom blocks with clear, predictable interfaces
- Current dependencies: 3
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T11.G6.02: Create modular programs with multiple custom blocks
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T11.G6.03: Test custom blocks with boundary and edge cases
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T11.G6.04: Refactor spaghetti code into organized custom blocks
- Current dependencies: 1
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T11.G6.05: Add error handling to custom blocks
- Current dependencies: 2
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T11.G6.06: Critique custom block naming and parameter choices
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T11.G6.07: Evaluate custom block scope and single responsibility
- Current dependencies: 2
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T11.G6.08: Critique return value usage in custom blocks
- Current dependencies: 2
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T12.G6.01: Analyze a program's structure using a checklist and suggest specific improvements
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T12.G6.02: Use comments to explain algorithm logic
- Current dependencies: 1
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T12.G6.03: Follow a provided style guide for naming conventions
- Current dependencies: 3
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T12.G6.04: Document code for collaborative maintenance
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T13.G6.01: Trace complex code with multiple variables
- Current dependencies: 4
- Issues: 2
- Additions suggested: 2
- Removals suggested: 1

### T13.G6.02: Use a systematic debugging process (hypothesis-driven)
- Current dependencies: 2
- Issues: 2
- Additions suggested: 0
- Removals suggested: 1

### T13.G6.03: Design systematic boundary tests using a matrix
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T13.G6.04: Document known limitations and potential bugs
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T13.G6.05: Debug a peer's program using systematic observation
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T14.G6.02: Hitbox separation
- Current dependencies: 2
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T14.G6.03: Multi-layer HUD with viewport attachments
- Current dependencies: 2
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T14.G6.04: Stream level chunks with viewport reporters
- Current dependencies: 3
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T14.G6.05: Cinematic camera rails
- Current dependencies: 3
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T14.G6.06: Mode and pause manager
- Current dependencies: 2
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T14.G6.07: Monitor and optimize clone count
- Current dependencies: 3
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T15.G6.01: Animation state machine
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T15.G6.02: List-based Dialogue
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T15.G6.03: Cutscene controller with custom blocks
- Current dependencies: 3
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T15.G6.04: Multi-language text-to-speech storytelling
- Current dependencies: 3
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T15.G6.05: Basic speech recognition input
- Current dependencies: 2
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T15.G6.06: Voice-controlled story choices
- Current dependencies: 3
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T15.G6.07: Rich text story displays
- Current dependencies: 2
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T15.G6.08: Visual stat tracking with sliders
- Current dependencies: 2
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T16.G6.01: Evaluate an interface for usability
- Current dependencies: 1
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T16.G6.02: Design an interface based on user feedback
- Current dependencies: 1
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T16.G6.03: Manage widget states and focus for clear feedback
- Current dependencies: 6
- Issues: 2
- Additions suggested: 2
- Removals suggested: 1

### T16.G6.04: Create an interface that works on different screen sizes
- Current dependencies: 3
- Issues: 2
- Additions suggested: 1
- Removals suggested: 1

### T16.G6.05: Display camera feed in a widget
- Current dependencies: 2
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T16.G6.06: Navigate to other projects
- Current dependencies: 4
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T17.G6.01: Configure surface friction parameters
- Current dependencies: 2
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T17.G6.02: Compare dynamic vs movable body types
- Current dependencies: 8
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T17.G6.03: Build a movable (kinematic) moving platform
- Current dependencies: 2
- Issues: 2
- Additions suggested: 3
- Removals suggested: 1

### T17.G6.04: Build trigger zones and collectibles with sensor bodies
- Current dependencies: 8
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T17.G6.05: Use dominance groups for one-way pushing
- Current dependencies: 4
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T17.G6.06: Lock movement or rotation of physics bodies
- Current dependencies: 3
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T17.G6.07: Configure world borders for wrap-around or open-edge levels
- Current dependencies: 5
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T17.G6.08: Compare simulations to real-world motion
- Current dependencies: 1
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T18.G6.02: Trace multi-step 3D scripts with transforms
- Current dependencies: 1
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T18.G6.03: Analyze trade-offs in 3D design decisions
- Current dependencies: 41
- Issues: 3
- Additions suggested: 2
- Removals suggested: 2

### T19.G6.06: Configure collision deletion (delete sprite on touch)
- Current dependencies: 4
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T19.G6.07: Handle multiplayer collisions with triggered messages
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T19.G6.08: Create shared world objects that stay synchronized
- Current dependencies: 2
- Issues: 0
- Additions suggested: 4
- Removals suggested: 0

### T19.G6.09: Remove sprites and clean up when players leave
- Current dependencies: 8
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T19.G6.11: Remove sprites from the multiplayer game world
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T19.G6.12: Understand network delay and its impact on gameplay
- Current dependencies: 9
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T20.G6.01: Trace and explain an art algorithm
- Current dependencies: 3
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T20.G6.02: Refactor repetitive art into loops/custom blocks
- Current dependencies: 3
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T20.G6.03: Use variables and conditionals to branch designs
- Current dependencies: 4
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T20.G6.04: **[Technical Skill]** Implement multi-field data visualization
- Current dependencies: 4
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T20.G6.05: Create interactive 3D generative art
- Current dependencies: 9
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T21.G6.01: Plan a mixed-source asset kit for a game or story project
- Current dependencies: 2
- Issues: 0
- Additions suggested: 5
- Removals suggested: 0

### T21.G6.02: Write structured prompts to maintain consistent visual style
- Current dependencies: 2
- Issues: 0
- Additions suggested: 3
- Removals suggested: 0

### T21.G6.03: Build a prompt test bench inside CreatiCode
- Current dependencies: 3
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T21.G6.04: Iterate when an AI output fails requirements
- Current dependencies: 1
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T21.G6.05: Use OpenAI Whisper speech recognition (ai_startopenaispeech block)
- Current dependencies: 4
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T21.G6.06: Check user input with AI content moderation
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T21.G6.07: Use image moderation to check visual content
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T21.G6.09: Compare ChatGPT responses with different temperatures
- Current dependencies: 1
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T21.G6.10: Use system instructions to guide ChatGPT behavior
- Current dependencies: 1
- Issues: 0
- Additions suggested: 5
- Removals suggested: 0

### T21.G6.11: Use head tilt angle for face orientation detection
- Current dependencies: 6
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T21.G6.12: Detect specific poses using body part combinations
- Current dependencies: 8
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T21.G6.13: Stop camera-based AI detection to manage resources
- Current dependencies: 2
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T22.G6.02: Adjust temperature for response creativity
- Current dependencies: 5
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T22.G6.03: Build a conversation log with dynamic updates
- Current dependencies: 11
- Issues: 4
- Additions suggested: 5
- Removals suggested: 3

### T22.G6.05: Display streaming responses in real-time
- Current dependencies: 13
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T22.G6.07: Debug off-topic responses by rewriting prompts
- Current dependencies: 6
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T22.G6.08: Use multiple chatbot sessions with the select chatbot block
- Current dependencies: 3
- Issues: 0
- Additions suggested: 4
- Removals suggested: 0

### T23.G6.07: Choose continuous vs. event-driven detection patterns
- Current dependencies: 2
- Issues: 0
- Additions suggested: 5
- Removals suggested: 0

### T23.G6.08: Track face attributes like age, gender, and accessories
- Current dependencies: 31
- Issues: 9
- Additions suggested: 3
- Removals suggested: 8

### T23.G6.11: Use NLP sentence analysis to extract parts of speech
- Current dependencies: 3
- Issues: 2
- Additions suggested: 0
- Removals suggested: 1

### T23.G6.12: Compare Azure vs OpenAI Whisper speech recognition performance
- Current dependencies: 3
- Issues: 2
- Additions suggested: 5
- Removals suggested: 1

### T24.G6.01: Provide complete context when asking XO to debug
- Current dependencies: 4
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T24.G6.02: Verify XO's explanation against the project
- Current dependencies: 6
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T24.G6.03: Generate and deliver a quiz using XO
- Current dependencies: 4
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T24.G6.04: Generate custom images with the DALL-E block
- Current dependencies: 6
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T24.G6.05: Use AI sentence analysis to identify parts of speech
- Current dependencies: 8
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T24.G6.06: Manage ChatGPT sessions explicitly
- Current dependencies: 17
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T24.G6.08: Build a multi-turn chatbot using LLM sessions
- Current dependencies: 4
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T24.G6.09: Build interactive games with body tracking
- Current dependencies: 16
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T24.G6.12: Use ChatGPT vision with costume attachment
- Current dependencies: 3
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T24.G6.13: Use web search blocks for real-time information
- Current dependencies: 4
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T25.G6.01: Document metadata for datasets
- Current dependencies: 3
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T25.G6.02: Explain lossy vs lossless representation
- Current dependencies: 2
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T25.G6.03: Nest tables and lists within each other
- Current dependencies: 2
- Issues: 0
- Additions suggested: 4
- Removals suggested: 0

### T25.G6.04: Apply normalization to a game database
- Current dependencies: 16
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T26.G6.01: Map stakeholder questions to data requirements
- Current dependencies: 5
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T26.G6.02: Automate logging from three different sensors
- Current dependencies: 5
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T26.G6.03: Create consent and opt-out workflows with widget dialogs
- Current dependencies: 5
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T26.G6.04: Understand document structure for database collections
- Current dependencies: 7
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T26.G6.05: Sort database query results
- Current dependencies: 13
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T26.G6.07: Import data from Google Sheets into tables
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T26.G6.08: Export tables to Google Sheets
- Current dependencies: 3
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T26.G6.09: Log multiplayer game session data
- Current dependencies: 3
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T27.G6.01: Combine data from two tables
- Current dependencies: 9
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T27.G6.02: Create pivot tables for multi-dimensional analysis
- Current dependencies: 6
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T27.G6.03: Export and import data using CSV files
- Current dependencies: 5
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T27.G6.04: Create structured summaries with labeled findings
- Current dependencies: 5
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T28.G6.02: Use random seeds for reproducibility
- Current dependencies: 3
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T28.G6.03: Measure percent error vs theoretical probability
- Current dependencies: 2
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T28.G6.04: Simulate noisy sensors for AI perception testing
- Current dependencies: 3
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T28.G6.05: Model a simple agent in a grid world
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T28.G6.06: Simulate events with changing probabilities
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T28.G6.07: Design an environment with obstacles and goals
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T28.G6.08: Implement reward rules and track outcomes
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T28.G6.09: Create simple two-sprite interaction
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T28.G6.10: Compare sampling methods (random, systematic, stratified)
- Current dependencies: 2
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T28.G6.11: Calculate and interpret conditional probability
- Current dependencies: 2
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T29.G6.01: Compare characters, words, and token counts
- Current dependencies: 6
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T29.G6.02: Compute n-gram (bigram) frequencies
- Current dependencies: 5
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T29.G6.03: Create autocomplete suggestions from bigrams
- Current dependencies: 4
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T29.G6.04: Log AI prompts/responses with ratings and timestamps
- Current dependencies: 6
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T29.G6.06: Convert speech to text using voice recognition
- Current dependencies: 2
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T29.G6.07: Convert text to speech with voice selection
- Current dependencies: 1
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T29.G6.08: Compare text similarity using edit distance
- Current dependencies: 2
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T29.G6.09: Handle text length limits and truncation
- Current dependencies: 2
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T29.G6.10: Use Pinecone semantic search blocks (advanced)
- Current dependencies: 9
- Issues: 2
- Additions suggested: 1
- Removals suggested: 1

### T30.G6.01: Analyze sensor specifications for CreatiCode projects
- Current dependencies: 2
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T30.G6.02: Compare browser storage options for CreatiCode projects
- Current dependencies: 2
- Issues: 2
- Additions suggested: 0
- Removals suggested: 1

### T30.G6.03: Explain camera and microphone privacy permissions
- Current dependencies: 3
- Issues: 2
- Additions suggested: 2
- Removals suggested: 2

### T30.G6.04: Plan device capability checklists for CreatiCode AI projects
- Current dependencies: 2
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T30.G6.05: Use webcam as 3D scene background for AR effects
- Current dependencies: 4
- Issues: 2
- Additions suggested: 3
- Removals suggested: 1

### T30.G6.06: Implement 3D object dragging with mouse
- Current dependencies: 6
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T31.G6.01: Trace the steps of an HTTP/HTTPS request
- Current dependencies: 1
- Issues: 0
- Additions suggested: 1
- Removals suggested: 0

### T31.G6.03: Manage Google Sheets structure programmatically
- Current dependencies: 4
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T31.G6.04: Measure and analyze how latency affects AI responsiveness and fairness
- Current dependencies: 2
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T31.G6.05: Evaluate privacy when sharing AI-generated content and data
- Current dependencies: 2
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T31.G6.06: Manage players and game state in multiplayer sessions
- Current dependencies: 3
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T32.G6.01: Identify common malware types
- Current dependencies: 2
- Issues: 0
- Additions suggested: 1
- Removals suggested: 0

### T32.G6.02: Recognize phishing attack patterns and warning signs
- Current dependencies: 1
- Issues: 0
- Additions suggested: 5
- Removals suggested: 0

### T32.G6.03: Understand network attacks (DoS, MitM)
- Current dependencies: 1
- Issues: 0
- Additions suggested: 4
- Removals suggested: 0

### T32.G6.05: Design secure login flows in CreatiCode apps
- Current dependencies: 6
- Issues: 4
- Additions suggested: 2
- Removals suggested: 3

### T32.G6.06: Conduct AI-specific threat modeling for class projects
- Current dependencies: 5
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T32.G6.08: Explore simple cipher techniques with alphabet position lookup
- Current dependencies: 2
- Issues: 1
- Additions suggested: 1
- Removals suggested: 0

### T33.G6.01: Identify and test Cloud blocks for network dependencies
- Current dependencies: 5
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T33.G6.02: Fetch web content using the fetch URL block
- Current dependencies: 5
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T33.G6.03: Read data from Google Sheets into a table
- Current dependencies: 4
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T33.G6.04: Write data from a table to Google Sheets
- Current dependencies: 4
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T33.G6.05: Clear a Google Sheet to reset data
- Current dependencies: 4
- Issues: 1
- Additions suggested: 0
- Removals suggested: 0

### T33.G6.06: Handle latency and error states in service calls
- Current dependencies: 4
- Issues: 1
- Additions suggested: 4
- Removals suggested: 0

### T33.G6.07: Respect usage limits and rate limiting
- Current dependencies: 4
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T33.G6.08: Apply privacy principles to Google Sheet URLs
- Current dependencies: 3
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T33.G6.09: Understand cloud database collections versus Google Sheets
- Current dependencies: 3
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T33.G6.10: Insert and fetch data from cloud database collections
- Current dependencies: 4
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T34.G6.01: Analyze major waves of computing (mainframe → personal computer → internet → mobile → AI), identifying what each wave made possible and what barriers remained
- Current dependencies: 2
- Issues: 0
- Additions suggested: 5
- Removals suggested: 0

### T34.G6.02: Evaluate historical inclusion and exclusion in computing, including how user interface evolution (command line → GUI → touchscreen → voice) has changed who can use computers
- Current dependencies: 2
- Issues: 0
- Additions suggested: 4
- Removals suggested: 0

### T34.G6.03: Analyze historical computing failures (e.g., Therac-25, Y2K, failed AI systems) to identify lessons for preventing similar problems today
- Current dependencies: 2
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)
- Current dependencies: 4
- Issues: 1
- Additions suggested: 2
- Removals suggested: 0

### T35.G6.02: Develop ethics guidelines for AI perception and assistance (T23-T24)
- Current dependencies: 19
- Issues: 1
- Additions suggested: 5
- Removals suggested: 0

### T35.G6.04: Examine digital divide data
- Current dependencies: 1
- Issues: 1
- Additions suggested: 3
- Removals suggested: 0

### T36.G6.01: Connect AI skills to career pathways
- Current dependencies: 4
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T36.G6.02: Practice stand-ups, task boards, and sprint reviews in team projects
- Current dependencies: 2
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T36.G6.03: Analyze job descriptions for skills/values
- Current dependencies: 2
- Issues: 0
- Additions suggested: 2
- Removals suggested: 0

### T36.G6.04: Add ethics clauses to team charters
- Current dependencies: 1
- Issues: 0
- Additions suggested: 3
- Removals suggested: 0

