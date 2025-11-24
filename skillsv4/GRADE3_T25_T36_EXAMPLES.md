# Grade 3 (T25-T36) Cross-Topic Dependency Examples

This document provides detailed examples of missing cross-topic dependencies identified in the analysis.

## Example 1: Variable Creation Skills Need Variable Foundations

**SKILL_ID**: T25.G3.00.01
**SKILL_NAME**: Create and name variables in CreatiCode
**DESCRIPTION**: Students learn to create new variables using the 'Make a Variable' button in CreatiCode. They practice choosing meaningful names (like 'score' not 'x') and understand that variables store one value at a time.

**CURRENT DEPENDENCIES**:
- T06.G3.01: Build a green-flag script that runs a 3–5 block sequence

**MISSING DEPENDENCIES**:
- **T09.GK.01**: Recognize that a label can hold a number
  - **REASON**: Students need foundational understanding that labels/variables can store values before learning to create them in code
- **T16.G1.01**: Match interface elements to their purpose (unplugged)
  - **REASON**: Using the 'Make a Variable' button and variable monitors requires understanding UI elements

**IMPACT**: Without T09.GK.01, students jump directly to creating variables without understanding the core concept of what a variable is.

---

## Example 2: List Operations Need List Foundations

**SKILL_ID**: T25.G3.01.01
**SKILL_NAME**: Add items to a list manually
**DESCRIPTION**: Students practice building lists by manually adding items one at a time using 'add [item] to [list]' blocks. They create simple lists (favorite foods, color names, numbers) and learn that lists maintain insertion order.

**CURRENT DEPENDENCIES**:
- T25.G3.00.02: Create and name lists in CreatiCode

**MISSING DEPENDENCIES**:
- **T09.GK.01**: Recognize that a label can hold a number
  - **REASON**: Lists are like variables but hold multiple values
- **T10.GK.01**: Sort picture cards into groups
  - **REASON**: Understanding grouping/collections is foundational to working with lists
- **T01.GK.01**: Put pictures in order for getting ready for bed
  - **REASON**: Lists maintain order, so understanding sequences is essential
- **T16.G1.01**: Match interface elements to their purpose (unplugged)
  - **REASON**: Using list blocks and monitors requires UI understanding

**IMPACT**: Without T10.GK.01, students don't have the conceptual foundation that lists are collections of items.

---

## Example 3: Survey Loops Need Foundational Skills

**SKILL_ID**: T26.G3.01
**SKILL_NAME**: Script a CreatiCode survey loop
**DESCRIPTION**: Students write a script that repeats `ask` five times, storing each answer in a list variable.

**CURRENT DEPENDENCIES**:
- T07.G3.02: Combine loops with conditionals to filter data
- T25.G3.01.02: Map survey responses into list variables

**MISSING DEPENDENCIES**:
- **T09.GK.01**: Recognize that a label can hold a number
  - **REASON**: Storing answers requires understanding variables
- **T10.GK.01**: Sort picture cards into groups
  - **REASON**: Storing multiple answers in a list requires understanding collections
- **T16.G1.01**: Match interface elements to their purpose (unplugged)
  - **REASON**: Using ask blocks and viewing responses requires UI understanding

**IMPACT**: The skill assumes students understand variables and lists, but doesn't explicitly require those foundations.

---

## Example 4: Data Validation Needs Conditionals

**SKILL_ID**: T25.G3.05
**SKILL_NAME**: Identify when data needs cleaning
**DESCRIPTION**: Students examine lists containing inconsistent data (different date formats, mixed capitalization like 'Red', 'red', 'RED') and mark which entries need fixing. They explain what makes data inconsistent and why consistent formatting matters.

**CURRENT DEPENDENCIES**:
- T25.G3.02.01: Use number variables for counting and scoring
- T10.G2.03: Use "=" to check if items match

**MISSING DEPENDENCIES**:
- **T08.GK.01**: Match pictures to "if it rains" rules
  - **REASON**: Identifying what needs cleaning involves checking conditions (if capitalization differs, if formats vary)

**IMPACT**: Students need to understand conditional thinking to evaluate "what makes data inconsistent."

---

## Example 5: Random Generator Needs Multiple Foundations

**SKILL_ID**: T28.G3.07
**SKILL_NAME**: Assemble blocks to build a random generator
**DESCRIPTION**: Students build a simple random generator from scratch by assembling a green flag script that uses 'pick random' to choose between 2-3 outcomes and displays the result with a 'say' block.

**CURRENT DEPENDENCIES**:
- T28.G3.06: Modify a teacher-provided random generator
- T06.G3.01: Build a green-flag script that runs a 3–5 block sequence

**MISSING DEPENDENCIES**:
- **T07.G1.01**: Count repetitions in a pattern
  - **REASON**: Random generators often run multiple trials, requiring loop understanding
- **T08.GK.01**: Match pictures to "if it rains" rules
  - **REASON**: Choosing between outcomes involves conditional logic

**IMPACT**: Building a generator from scratch requires understanding how to repeat trials and handle different outcomes.

---

## Example 6: Text Comparison Needs Conditional Foundations

**SKILL_ID**: T29.G3.05
**SKILL_NAME**: Compare text for equality using "=" operator
**DESCRIPTION**: Students use the equals operator to check if two text variables match exactly, understanding case-sensitive comparison. They test examples to see when texts are equal and when they differ.

**CURRENT DEPENDENCIES**:
- T09.G3.04: Join text dynamically using the "join" operator

**MISSING DEPENDENCIES**:
- **T08.GK.01**: Match pictures to "if it rains" rules
  - **REASON**: Using "=" to compare is conditional logic (if text1 = text2 then...)

**IMPACT**: Students use comparison operators without understanding they're implementing conditional logic.

---

## Example 7: Device Permissions Need Conditional Understanding

**SKILL_ID**: T30.G3.05
**SKILL_NAME**: Access device camera in CreatiCode projects
**DESCRIPTION**: Students enable camera permissions and display the camera feed in CreatiCode projects, understanding when and why camera access is needed and how to respect user privacy.

**CURRENT DEPENDENCIES**:
- T30.G3.04: Explain how sensors provide input to computer programs
- T30.G2.02: Name specific devices by their storage type

**MISSING DEPENDENCIES**:
- **T08.GK.01**: Match pictures to "if it rains" rules
  - **REASON**: Enabling permissions involves conditional logic (if user grants permission, then access camera)
- **T16.G1.01**: Match interface elements to their purpose (unplugged)
  - **REASON**: Camera feed display and permission dialogs are UI elements

**IMPACT**: Students interact with permission workflows without understanding the conditional nature of access control.

---

## Example 8: Phishing Detection Needs Decision-Making Skills

**SKILL_ID**: T32.G3.05
**SKILL_NAME**: Recognize phishing-like messages
**DESCRIPTION**: Learners see sample email/text messages asking for logins or offering prizes and use a 4-point checklist (unknown sender? urgent tone? misspellings? suspicious link?) to identify red flags. They decide whether to trust or ignore each message.

**CURRENT DEPENDENCIES**:
- T32.G3.04: Evaluate and use sharing settings in CreatiCode projects
- T32.G2.02: Recognize what information should stay private

**MISSING DEPENDENCIES**:
- **T08.GK.01**: Match pictures to "if it rains" rules
  - **REASON**: Using a checklist involves conditional evaluation (if unknown sender AND urgent tone, then suspicious)
- **T16.G1.01**: Match interface elements to their purpose (unplugged)
  - **REASON**: Recognizing message elements (sender, links, buttons) requires UI understanding

**IMPACT**: Students evaluate security without explicit training in conditional decision-making frameworks.

---

## Example 9: Timeline Sequencing Needs Algorithm Foundations

**SKILL_ID**: T34.G3.01
**SKILL_NAME**: Sequence milestones on a timeline
**DESCRIPTION**: Students place 4-5 computing history milestones in chronological order on a timeline, understanding the progression from early computers to modern devices.

**CURRENT DEPENDENCIES**:
- T34.G2.01: Match early and modern computing devices

**MISSING DEPENDENCIES**:
- **T01.GK.01**: Put pictures in order for getting ready for bed
  - **REASON**: Sequencing events chronologically is the same skill as ordering algorithm steps

**IMPACT**: Students sequence historical events without connecting to their foundational sequencing skills from T01.

---

## Example 10: Collaboration Reflection Needs Collection Skills

**SKILL_ID**: T36.G3.03
**SKILL_NAME**: Reflect on collaboration habits
**DESCRIPTION**: Students identify their collaboration strengths and areas for improvement, creating a personal reflection on what worked well and what they'd like to improve in group work.

**CURRENT DEPENDENCIES**:
- T36.G3.02: Draft simple team agreements

**MISSING DEPENDENCIES**:
- **T10.GK.01**: Sort picture cards into groups
  - **REASON**: Reflecting on multiple habits involves categorizing (strengths vs areas for improvement)

**IMPACT**: Students organize reflection points without explicit connection to categorization/grouping skills.

---

## Key Patterns Across Examples

### Pattern 1: Variable/List Skills Missing Core Foundations
Skills that create or manipulate variables/lists often assume students already understand what variables and lists ARE, but don't require the foundational conceptual skills.

### Pattern 2: Decision-Making Without Conditional Foundations
Many skills involve comparing, checking, choosing, or deciding, but don't require foundational conditional thinking skills from T08.

### Pattern 3: UI Interaction Without Interface Foundations
Skills using buttons, monitors, widgets, and displays assume UI literacy without requiring T16 foundations.

### Pattern 4: Sequencing Without Algorithm Foundations
Skills involving ordering, steps, or timelines miss the connection to foundational sequencing from T01.

### Pattern 5: Repetition Without Loop Foundations
Skills involving multiple trials, counting occurrences, or iteration miss explicit loop foundations from T07.

---

## Recommendations Summary

1. **Strengthen Conceptual Foundations**: Ensure Grade 3 students have GK/G1/G2 foundations before advanced applications
2. **Make Cross-Topic Connections Explicit**: Dependencies help students see how concepts connect across topics
3. **Progressive Complexity**: GK teaches concepts, G1 applies them, G2 combines them, G3 uses them in authentic contexts
4. **Prerequisite Clarity**: Teachers need clear dependency paths to know what students should already understand

---

## Implementation Priority

**High Priority** (affects 15+ skills):
1. T08 (Conditionals) - 20 skills
2. T09 (Variables) - 15 skills
3. T16 (User Interfaces) - 15 skills

**Medium Priority** (affects 10-14 skills):
4. T10 (Lists) - 13 skills

**Lower Priority** (affects <10 skills):
5. T07 (Loops) - 7 skills
6. T01 (Algorithms) - 5 skills
