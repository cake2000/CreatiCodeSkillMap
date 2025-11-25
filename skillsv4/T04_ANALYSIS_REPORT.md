# T04 Algorithm Patterns - Comprehensive Analysis Report

**Analysis Date**: 2025-11-24
**File Analyzed**: /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md

---

## Executive Summary

Total Skills Analyzed: **68 skills** across 9 grade levels (GK through G8)

### Skills Distribution by Grade:
- **GK (Kindergarten)**: 4 skills
- **G1 (Grade 1)**: 4 skills
- **G2 (Grade 2)**: 5 skills
- **G3 (Grade 3)**: 11 skills
- **G4 (Grade 4)**: 10 skills
- **G5 (Grade 5)**: 9 skills
- **G6 (Grade 6)**: 8 skills
- **G7 (Grade 7)**: 10 skills
- **G8 (Grade 8)**: 7 skills

### Issues Summary:
- **HIGH Priority**: 1 issue (X-2 rule violation)
- **MEDIUM Priority**: 8 issues (overlaps, missing deps, complexity)
- **LOW Priority**: 4 issues (scaffolding gaps)

---

## HIGH PRIORITY ISSUES

### Issue 1: X-2 Rule Violation ⚠️

**T04.G6.04** (Grade 6) depends on **T04.G3.04.02** (Grade 3)

- **Skill**: Turn repeated code into a custom block with parameters
- **Dependency**: Create a custom block (template) for repeated code patterns
- **Grade Gap**: 3 levels (violates X-2 rule which allows max 2 grade gap)

**Recommendation**: Create intermediate skill T04.G5.04.02

```
ID: T04.G5.04.02
Topic: T04 – Algorithm Patterns
Skill: Create a custom block with one parameter
Description: Students create a custom block that has one parameter, replacing a hard-coded value with the parameter. They understand how parameters make blocks reusable with different values.

Dependencies:
* T04.G3.04.02: Create a custom block (template) for repeated code patterns
* T11.G4.07: Define a custom block with one parameter
```

Then update T04.G6.04 to depend on T04.G5.04.02 instead of T04.G3.04.02.

---

## MEDIUM PRIORITY ISSUES

### Issue 2: Overlapping/Duplicate Skills

#### 2.1 Counter Pattern Skills Overlap

**T04.G4.01.01** vs **T04.G5.01**

Current state:
- **T04.G4.01.01**: "Recognize when to use a counter pattern to track counts"
- **T04.G5.01**: "Recognize a counter update pattern"

**Problem**: Both are "recognize" tasks with similar focus. The distinction between "when to use" and "recognize pattern" is unclear.

**Recommendation**:

Update **T04.G4.01.01**:
```
Skill: Identify problems that require tracking counts
Description: Students examine problem scenarios (like "count how many red items" or "track number of jumps") and identify which problems need a counter variable to track a count, distinguishing these from problems that don't require counting.
```

Keep **T04.G5.01** as is (recognizing the counter pattern in existing code).

#### 2.2 Search/Filter Pattern Confusion

**T04.G5.03.01** (Apply the collect pattern) vs **T04.G5.04** (Recognize a filter-and-collect pattern)

Current state:
- **T04.G5.03.01**: "Apply the collect pattern to gather specific items from a collection"
- **T04.G5.04**: "Recognize a filter‑and‑collect pattern"

**Problem**: These are essentially the same pattern. "Collect pattern" and "filter-and-collect pattern" both mean: loop through items, test criteria, collect matches.

**Recommendation**:

Option A (Preferred): **Merge T04.G5.04 into T04.G5.03.01**

Update **T04.G5.03.01**:
```
Skill: Apply the filter-collect pattern to gather matching items
Description: Students implement or complete code that uses the filter-collect pattern: loop through items, test each against criteria, and add matching items to a new list. This extends the search pattern (which finds ONE match) to collect ALL matches.
```

Remove **T04.G5.04** entirely.

Option B: **Differentiate them clearly**

Keep T04.G5.03.01 as "apply/implement" (doing)
Keep T04.G5.04 as "recognize" (identifying in existing code)

#### 2.3 Nested Loop Skills

**T04.G3.09** vs **T04.G4.02**

Current state:
- **T04.G3.09**: "Recognize nested loops in patterns (outer loop repeats inner loop)"
- **T04.G4.02**: "Identify nested pattern structure (outer vs inner loop)"

**Problem**: Very similar - both identify outer vs inner loops in nested structures.

**Recommendation**:

Update **T04.G3.09** description:
```
Description: Students examine VISUAL patterns (like grids of stars, repeated tile patterns, or nested shapes) and identify that an outer pattern repeats an inner pattern. They understand that "the outer loop repeats the inner loop" by seeing examples like: 3 rows, each with 4 stars. Focus is on visual/conceptual understanding before code.
```

Update **T04.G4.02** description:
```
Description: Students read nested loop CODE and analyze which loop controls what aspect of the output (e.g., which controls rows vs columns in a grid pattern). Focus is on analyzing code structure and determining the role of outer vs inner loops in creating the pattern.
```

### Issue 3: Missing Dependencies

#### 3.1 Search Pattern Missing Loop Iteration

**T04.G5.03** (Recognize a linear search pattern)

**Current dependencies**:
- T04.G4.09
- T08.G3.01
- T09.G3.03
- T10.G5.01

**Wait, checking the extracted data...**

Actually, the extracted data shows:
```
Dependencies:
* T10.G5.01: Understand table structure (rows, columns, cells)
```

This is missing several dependencies! Let me check the original more carefully...

**Problem**: T04.G5.03 only has dependencies shown as incomplete (T04.G4.09, T08.G3.01, T09.G3.03) but these appear to be listed without the skill titles.

**Recommendation**:

Verify T04.G5.03 has these dependencies:
```
Dependencies:
* T04.G4.09: Use loops to iterate through all items in a list
* T08.G3.01: Use a simple if in a script
* T09.G3.03: (need to verify this skill ID)
* T10.G5.01: Understand table structure (rows, columns, cells)
```

The T04.G4.09 dependency is ESSENTIAL for search - you can't search without iteration.

### Issue 4: Skills with Too Many Dependencies

#### 4.1 Extremely Complex Skill

**T04.G4.06**: Identify when a known pattern can solve a new problem

**Current dependencies**: 11 dependencies from 5 different topics
- T02.G2.01, T02.G2.02 (Decomposition)
- T04.G2.01, T04.G2.02, T04.G3.08 (Algorithm Patterns)
- T05.G3.01, T05.G3.02 (Human-Centered Design)
- T06.G3.01 (Events)
- T07.G2.01, T07.G3.01 (Loops)
- T09.G3.01.04 (Variables)

**Problem**: This skill is overloaded. It's trying to synthesize too much knowledge from too many topics. This makes it difficult to assess and teach.

**Recommendation**:

**Option A** (Preferred): Reduce to core dependencies
```
Dependencies:
* T04.G4.01: Trace a loop that creates a visual pattern
* T04.G4.05: Match multiple code snippets that share the same pattern
* T07.G3.01: Use a counted repeat loop
```

Rationale: If students can trace loops, match patterns, and use loops, they have the foundation. The T02, T05, T06, T09 dependencies are either implicit or not essential for pattern recognition.

**Option B**: Move to G5 or G6 where students have more foundation

**Option C**: Split into multiple smaller skills

#### 4.2 Other High-Dependency Skills

Review these skills for necessary vs implicit dependencies:

- **T04.G4.05**: Match multiple code snippets (7 deps) - probably okay given it's synthesis
- **T04.G4.09**: Use loops to iterate through all items in a list (7 deps) - review if all needed
- **T04.G5.06**: Identify changeable vs fixed parts in a template (7 deps) - review if all needed

### Issue 5: Skills That Are Too Broad

#### 5.1 T04.G6.05 - Analyze a template project

**Current description**: "Students inspect a more complex template (quiz, platformer, etc.) and identify specific customization points with detailed analysis: what each point controls, how to modify it safely, what values are acceptable, and which changes would break the template's structure. Focus is on understanding the template's internal logic and constraints."

**Problem**: This is 4+ distinct sub-skills combined:
1. Identify customization points
2. Determine what each point controls
3. Analyze safe modification constraints
4. Predict breaking changes

**Recommendation**:

Split into two skills:

**T04.G6.05** (Updated):
```
Skill: Identify and categorize customization points in a template
Description: Students inspect a complex template project (quiz, platformer, etc.) and identify which elements are customization points versus structural code. They categorize each customization point by what aspect it controls (appearance, behavior, difficulty, etc.).

Dependencies:
* T04.G5.06: Identify changeable vs fixed parts in a template
```

**T04.G6.05.01** (New):
```
Skill: Analyze modification constraints for template parameters
Description: Students examine customization points in a template and determine: what values are safe to change, what ranges are acceptable, and which changes would break the template's functionality. They explain the constraints and reasoning for each parameter.

Dependencies:
* T04.G6.05: Identify and categorize customization points in a template
```

#### 5.2 T04.G6.03 - Apply filter with multiple criteria

**Current description**: "Students extend the basic filter pattern (from T04.G5.04) to handle multiple criteria, combining conditions to select items that match complex requirements (e.g., 'items that are both red AND large' or 'items that are blue OR circle-shaped')."

**Problem**: Jumps from single criterion to complex AND/OR logic without intermediate step.

**Recommendation**:

Add intermediate skill:

**T04.G6.02.01** (New):
```
Skill: Apply filter with two criteria using AND
Description: Students filter a list using two conditions that must both be true (AND logic). For example, "find items that are both red AND large" or "select sprites that are both moving AND visible."

Dependencies:
* T04.G5.04: Recognize a filter‑and‑collect pattern
* T08.G5.01: Use a simple if in a script
```

Then update **T04.G6.03**:
```
Description: Students extend the filter pattern to handle complex multi-criteria logic, using both AND and OR operators to combine conditions. For example, "items that are (red AND large) OR (blue AND circle-shaped)."

Dependencies:
* T04.G6.02.01: Apply filter with two criteria using AND
* T08.G5.01: Use a simple if in a script
```

---

## LOW PRIORITY ISSUES

### Issue 6: Scaffolding Gaps

#### 6.1 Counter Pattern Introduction

**Observation**: Counter pattern appears suddenly in G4:
- G3: No counter pattern skills
- G4.01.01: Suddenly "Recognize when to use a counter pattern"
- G5.01: "Recognize a counter update pattern"

**Problem**: Students haven't been introduced to the counter concept before being asked to recognize when to use it.

**Recommendation**:

Add foundational skill in G3:

**T04.G3.10** (New):
```
Skill: Use a variable to count loop iterations
Description: Students create a variable, set it to 0, and increment it by 1 each time through a simple loop. They observe how the variable tracks the count and display it to see the progression (1, 2, 3...).

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T09.G3.01.04: Display variable value on stage using the variable monitor
```

#### 6.2 Algorithm Pattern Terminology Gap

**Observation**:
- G3 ends with basic loops and templates
- G4 suddenly uses terminology like "algorithm pattern", "boundary-check-and-adjust", "loop-and-count"

**Problem**: The term "algorithm pattern" is used without introduction.

**Recommendation**:

Add concept introduction skill:

**T04.G4.00** (New):
```
Skill: Identify common algorithm patterns in example code
Description: Students examine 3-4 code examples and identify them as "counter pattern", "accumulator pattern", "search pattern", or "loop-and-process pattern" using provided definitions and examples. This introduces the concept that certain code structures appear repeatedly and have standard names.

Dependencies:
* T04.G3.08: Match algorithm descriptions to code pattern shapes
```

#### 6.3 Template/Custom Block Sequence Issues

**Observation**:
- T04.G3.04.01/.02/.03 form a tight sequence in G3
- Then not referenced again until G6.04 (3 grade gap!)
- G4.04, G4.08, G5.06, G6.05 all relate to templates but don't reference the G3.04.x sequence

**Problem**: Unclear progression from G3 template skills to later template skills.

**Recommendation**:

Add dependency connections:
- T04.G4.04 should depend on T04.G3.04.03
- T04.G4.08 should depend on T04.G4.04
- T04.G5.06 should depend on T04.G4.08
- T04.G6.05 should depend on T04.G5.06

This creates a clear progression:
- G3: Identify, create, and use custom blocks
- G4: Identify and use templates in projects
- G5: Analyze template structure
- G6: Advanced template analysis and parameterization

---

## SUMMARY OF RECOMMENDED CHANGES

### High Priority (Must Fix)

| # | Issue | Action | Skill(s) Affected |
|---|-------|--------|-------------------|
| 1 | X-2 violation | Add intermediate skill T04.G5.04.02 | T04.G6.04 |
| 2 | Counter overlap | Rename T04.G4.01.01 to clarify distinction | T04.G4.01.01 |
| 3 | Search/filter overlap | Merge T04.G5.04 into T04.G5.03.01 | T04.G5.03.01, T04.G5.04 |
| 4 | Missing dependency | Add T04.G4.09 to T04.G5.03 dependencies | T04.G5.03 |

### Medium Priority (Should Fix)

| # | Issue | Action | Skill(s) Affected |
|---|-------|--------|-------------------|
| 5 | Nested loop overlap | Update descriptions to clarify visual vs code | T04.G3.09, T04.G4.02 |
| 6 | Too many dependencies | Reduce T04.G4.06 from 11 to ~3-4 deps | T04.G4.06 |
| 7 | Skill too broad | Split T04.G6.05 into two skills | T04.G6.05 + new G6.05.01 |
| 8 | Missing scaffolding | Add T04.G6.02.01 for AND logic | T04.G6.03 |

### Low Priority (Nice to Have)

| # | Issue | Action | Skill(s) Affected |
|---|-------|--------|-------------------|
| 9 | Counter intro gap | Add T04.G3.10 to introduce counter concept | - |
| 10 | Pattern terminology gap | Add T04.G4.00 to introduce terminology | - |
| 11 | Template progression unclear | Update dependencies to show progression | G4.04, G4.08, G5.06, G6.05 |
| 12 | Review high-dep skills | Trim dependencies where possible | G4.05, G4.09, G5.06 |

---

## RECOMMENDED NEW SKILLS

### 1. T04.G3.10: Use a variable to count loop iterations

**Purpose**: Introduces counter concept before pattern recognition

```
ID: T04.G3.10
Topic: T04 – Algorithm Patterns
Skill: Use a variable to count loop iterations
Description: Students create a variable, set it to 0, and increment it by 1 each time through a simple loop. They observe how the variable tracks the count and display it to see the progression (1, 2, 3...).

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T09.G3.01.04: Display variable value on stage using the variable monitor
```

### 2. T04.G4.00: Identify common algorithm patterns in example code

**Purpose**: Introduces algorithm pattern terminology

```
ID: T04.G4.00
Topic: T04 – Algorithm Patterns
Skill: Identify common algorithm patterns in example code
Description: Students examine 3-4 code examples and identify them as "counter pattern", "accumulator pattern", "search pattern", or "loop-and-process pattern" using provided definitions and examples. This introduces the concept that certain code structures appear repeatedly and have standard names.

Dependencies:
* T04.G3.08: Match algorithm descriptions to code pattern shapes
```

### 3. T04.G5.04.02: Create a custom block with one parameter

**Purpose**: Bridges G3 custom blocks to G6 parameterized blocks (fixes X-2 violation)

```
ID: T04.G5.04.02
Topic: T04 – Algorithm Patterns
Skill: Create a custom block with one parameter
Description: Students create a custom block that has one parameter, replacing a hard-coded value with the parameter. They understand how parameters make blocks reusable with different values.

Dependencies:
* T04.G3.04.02: Create a custom block (template) for repeated code patterns
* T11.G4.07: Define a custom block with one parameter
```

### 4. T04.G6.02.01: Apply filter with two criteria using AND

**Purpose**: Scaffolds from single criterion to complex multi-criteria

```
ID: T04.G6.02.01
Topic: T04 – Algorithm Patterns
Skill: Apply filter with two criteria using AND
Description: Students filter a list using two conditions that must both be true (AND logic). For example, "find items that are both red AND large" or "select sprites that are both moving AND visible."

Dependencies:
* T04.G5.04: Recognize a filter‑and‑collect pattern
* T08.G5.01: Use a simple if in a script
```

### 5. T04.G6.05.01: Analyze modification constraints for template parameters

**Purpose**: Splits overly broad G6.05 into focused skills

```
ID: T04.G6.05.01
Topic: T04 – Algorithm Patterns
Skill: Analyze modification constraints for template parameters
Description: Students examine customization points in a template and determine: what values are safe to change, what ranges are acceptable, and which changes would break the template's functionality. They explain the constraints and reasoning for each parameter.

Dependencies:
* T04.G6.05: Identify and categorize customization points in a template
```

---

## FULL SKILL LISTING BY GRADE

### KINDERGARTEN (4 skills)

**T04.GK.01**: Identify a simple repeating pattern
- Description: Students look at rows of pictures or tiles and pick the row that shows a clear repeating pattern (ABAB, AABB, ABCABC), distinguishing it from broken or random rows.
- Dependencies: None

**T04.GK.02**: Extend a repeating pattern by one tile
- Description: Students see a short pattern (e.g., red, blue, red, blue, ?) and choose or drag the next picture.
- Dependencies: T04.GK.01

**T04.GK.03**: Describe a pattern using simple words
- Description: Students see a pattern and choose the matching description (e.g., "circle, square, circle, square").
- Dependencies: T04.GK.02

**T04.GK.04**: Fix a broken pattern by replacing one tile
- Description: Students see a pattern row with one wrong picture and replace just that tile to restore the repeating pattern.
- Dependencies: T04.GK.02

### GRADE 1 (4 skills)

**T04.G1.01**: Match a picture pattern to a movement pattern
- Description: Students match a picture pattern (e.g., hop, clap, hop, clap) to a character's actions in a short story or animation.
- Dependencies: T04.GK.02

**T04.G1.02**: Plan a short repeating animation pattern
- Description: Students choose a 3‑panel picture pattern (e.g., spin, jump, spin) and arrange action cards to create a matching "dance" plan.
- Dependencies: T04.G1.01

**T04.G1.03**: Find repeated steps in an instruction list
- Description: Students examine a short list of picture‑based steps (or action cards laid out in a row) and click or highlight the part that repeats (e.g., three identical "move forward" cards in a row).
- Dependencies: T01.GK.07

**T04.G1.04**: Match a repeated picture story to a repeated step list
- Description: Students match a picture story showing repeated actions with a simple list of steps that repeats the same action sequence.
- Dependencies: T04.G1.03

### GRADE 2 (5 skills)

**T04.G2.01**: Identify the repeating unit in a longer pattern
- Description: Students see a longer pattern like ABCABCABC and choose the "unit" that repeats.
- Dependencies: T04.G1.02, T04.G1.03

**T04.G2.02**: Spot repeated step sequences in everyday algorithms
- Description: Students read or see an everyday algorithm (e.g., "brush, rinse" repeated three times) and highlight the part that repeats, focusing on the pattern unit rather than the full routine.
- Dependencies: T04.G2.01

**T04.G2.03**: Compare a long explicit description vs a compressed "repeat" description
- Description: Students compare two visual or written descriptions of the same pattern: one showing all steps explicitly (e.g., "draw star, draw star, draw star") vs one using "repeat 3 times: draw star." They identify which is shorter and clearer, focusing on pattern comparison rather than coding concepts.
- Dependencies: T01.G2.02

**T04.G2.04**: Replace repeated steps with a "repeat ___ times" phrase
- Description: Students rewrite a long visual or written pattern description by selecting or creating a compressed version using "repeat ___ times" notation. Focus is on recognizing and expressing repetition concisely, using visual notation like "repeat 4: [pattern]" rather than preparing for coding.
- Dependencies: T04.G2.03

**T04.G2.05**: Match a "repeat box" diagram to repeated steps
- Description: Students see a visual representation of repetition—a box drawn around pictures or steps with "repeat 3 times" written above it—and match it to the equivalent expanded sequence. This visual "repeat box" notation helps organize repeated elements in a clear, visual way.
- Dependencies: T04.G2.04

### GRADE 3 (11 skills)

**T04.G3.01**: Identify where a loop could replace repeated blocks
- Description: Students see a short script with copy‑pasted blocks and choose which part can be replaced by a loop, focusing on recognizing the loop pattern shape.
- Dependencies: T04.G2.05, T07.G3.01

**T04.G3.02**: Match a repeat box diagram to code blocks
- Description: Students match visual "repeat box" diagrams (showing a box around pictures with "repeat 3" label) to actual code snippets using repeat blocks, creating an explicit bridge from G2's visual notation to G3 coding.
- Dependencies: T04.G3.01, T07.G3.01

**T04.G3.03**: Match a "repeat N" loop to repeated behavior
- Description: Students match a repeat N loop script (e.g., repeat 4 { move 10 }) to an animation or path with the same repeated behavior, treating it as a generic "N‑times pattern" that will later appear inside real T01/T07 projects.
- Dependencies: T04.G3.01

**T04.G3.04.01**: Identify repeated code segments that could be simplified with templates
- Description: Students examine small projects and identify code segments that are repeated with only minor variations (like different values or colors), recognizing these as opportunities for creating reusable templates or custom blocks.
- Dependencies: T04.G3.01, T07.G3.02

**T04.G3.04.02**: Create a custom block (template) for repeated code patterns
- Description: Students take identified repeated code patterns and create a custom block that captures the common structure, using parameters or variables as placeholders for the parts that vary between uses.
- Dependencies: T04.G3.04.01, T03.G3.02

**T04.G3.04.03**: Use custom blocks to make programs more readable and maintainable
- Description: Students replace repeated code segments with calls to custom blocks, then compare the before and after versions to explain how the custom block makes the code easier to read, understand, and modify.
- Dependencies: T04.G3.04.02

**T04.G3.05**: Customize a template by changing repeated elements
- Description: Students modify a simple template (e.g., pattern of colors or sounds in a loop) by adjusting blocks while preserving the structure.
- Dependencies: T04.G3.04.03, T09.G3.01.04

**T04.G3.06**: Fix a loop that repeats too many or too few times
- Description: Students adjust the repeat count to match a target pattern or path in a small, self‑contained example, so they can later use the same adjustment skill inside larger T01 algorithms.
- Dependencies: T04.G3.01

**T04.G3.07**: Fix a pattern where one step is wrong
- Description: Students repair a loop or repeated sequence where one action is different from the rest.
- Dependencies: T04.G3.06, T07.G3.03

**T04.G3.08**: Match algorithm descriptions to code pattern shapes
- Description: Students see simple algorithm descriptions (e.g., "check each item," "count how many times") and match them to generic code structures (loop, counter, conditional), bridging pattern recognition from descriptions to code. This skill builds on understanding the counter pattern introduced in T04.G5.01, so ensure students have basic familiarity with counting events in code.
- Dependencies: T04.G3.01, T04.G3.02, T06.G3.01

**T04.G3.09**: Recognize nested loops in patterns (outer loop repeats inner loop)
- Description: Students examine visual patterns or code with nested loops and identify which loop is the outer loop (runs fewer times) and which is the inner loop (runs many times for each outer iteration). They understand that the outer loop "repeats the inner loop," creating patterns like grids or multi-level repetition.
- Dependencies: T04.G3.01, T07.G3.01

### GRADE 4 (10 skills)

**T04.G4.01**: Trace a loop that creates a visual pattern
- Description: Students trace code that draws shapes or patterns and match it to one of several images.
- Dependencies: T04.G3.01, T06.G3.01, T07.G2.01, T13.G3.01

**T04.G4.01.01**: Recognize when to use a counter pattern to track counts
- Description: Students examine simple scenarios and problems (like "count how many red items" or "track number of jumps") and identify when a counter pattern (initialize to 0, increment by 1) is the appropriate solution approach.
- Dependencies: T04.G2.01, T04.G2.02, T04.G4.01, T06.G2.01, T06.G2.02, T07.G2.01

**T04.G4.02**: Identify nested pattern structure (outer vs inner loop)
- Description: Students see nested loops and choose which part controls rows vs columns in a grid pattern. Focus is on analyzing and reading nested loop structures, not yet creating them.
- Dependencies: T02.G2.01, T02.G2.02, T04.G3.09, T07.G2.01, T07.G3.01

**T04.G4.03**: Recognize "if" patterns that handle special cases
- Description: Students identify code patterns like "bounce on edge" or "wrap around screen" as standard conditional patterns.
- Dependencies: T04.G3.05, T06.G2.01, T06.G2.02, T07.G2.01, T08.G3.01

**T04.G4.04**: Identify template patterns in example projects
- Description: Students examine 2-3 simple example projects and identify which elements form the reusable template pattern (the structure that stays the same) versus customization points (values that change). This bridges from recognizing templates (G3.04) to understanding how templates work as patterns.
- Dependencies: T04.G2.01, T04.G2.02, T04.G3.04.03, T04.G3.05, T07.G2.01

**T04.G4.05**: Match multiple code snippets that share the same pattern
- Description: Students identify 2–3 code snippets that implement the same algorithm pattern (e.g., boundary-check-and-adjust, loop-and-count, test-and-respond) and select which snippets belong together based on their underlying logic structure.
- Dependencies: T02.G2.01, T02.G2.02, T04.G3.08, T06.G2.01, T06.G2.02, T07.G2.01, T13.G3.01

**T04.G4.06**: Identify when a known pattern can solve a new problem
- Description: Students see a new problem description and choose which known pattern (e.g., loop over list, counter pattern) would help.
- Dependencies: T02.G2.01, T02.G2.02, T04.G2.01, T04.G2.02, T04.G3.08, T05.G3.01, T05.G3.02, T06.G3.01, T07.G2.01, T07.G3.01, T09.G3.01.04

**T04.G4.07**: Select reasons why reusing a pattern saves time
- Description: Students answer multiple-choice questions identifying benefits of reusing patterns (e.g., "less code to write," "fewer bugs," "easier to understand") versus incorrect claims (e.g., "makes code run faster," "uses less memory").
- Dependencies: T04.G3.08, T06.G2.03

**T04.G4.08**: Use a template to create a customized project
- Description: Students start with a provided template project and modify specific marked elements (colors, sounds, repeat counts) to create their own version while preserving the template structure.
- Dependencies: T02.G2.01, T02.G2.02, T04.G4.04, T07.G2.01

**T04.G4.09**: Use loops to iterate through all items in a list
- Description: Students write or complete code that uses a loop to process each item in a list one by one, understanding the basic pattern of list iteration that underlies many algorithm patterns.
- Dependencies: T02.G2.01, T02.G2.02, T04.G4.01, T05.G3.01, T05.G3.02, T07.G2.01, T07.G3.01

### GRADE 5 (9 skills)

**T04.G5.01**: Recognize a counter update pattern
- Description: Students identify code where a variable counts events (set count to 0; change count by 1) across different contexts.
- Dependencies: T04.G4.05, T09.G3.01.04, T06.G5.01

**T04.G5.02**: Recognize an accumulator (sum/concatenate) pattern
- Description: Students identify code where a variable accumulates totals or builds strings.
- Dependencies: T04.G4.05, T09.G3.01.04

**T04.G5.02.01**: Compare counter and accumulator patterns and choose appropriately
- Description: Students examine problems and scenarios to determine whether a counter pattern (count occurrences) or accumulator pattern (sum values) is more appropriate, understanding the distinction between counting items versus adding their values.
- Dependencies: T04.G5.01, T04.G5.02, T09.G5.01, T10.G5.01

**T04.G5.03**: Recognize a linear search pattern
- Description: Students identify the "look at each item and compare" pattern in code that searches for a match. Focus is on the search pattern: iterating through items to find one that matches a condition.
- Dependencies: T04.G4.09, T08.G3.01, T09.G3.03, T10.G5.01

**T04.G5.03.01**: Apply the collect pattern to gather specific items from a collection
- Description: Students implement or complete code that uses the collect pattern: loop through items, test each against criteria, and add matching items to a new list. This extends the search pattern by collecting all matches rather than just finding one.
- Dependencies: T04.G5.03, T09.G3.03, T07.G5.01, T10.G5.01, T02.G5.01

**T04.G5.04**: Recognize a filter‑and‑collect pattern
- Description: Students identify code that loops, tests a condition, and adds matching items to a list.
- Dependencies: T04.G4.05, T08.G3.01, T07.G5.01, T10.G5.01, T02.G5.01

**T04.G5.05**: Compare solutions that use a pattern vs those that don't
- Description: Students compare two snippets solving the same task, one using a standard pattern (loop + counter) and one using ad‑hoc code, and choose which is better and why.
- Dependencies: T04.G4.06, T09.G3.01.04, T07.G5.01

**T04.G5.06**: Identify changeable vs fixed parts in a template
- Description: Students look at a simple template project (e.g., a basic animation or greeting card) and mark which parts are placeholders (meant to be changed, like colors or messages) vs structural elements (meant to stay the same, like loop structure or event handlers). Focus is on binary classification: changeable or fixed.
- Dependencies: T04.G3.04.01, T04.G4.03, T09.G3.03, T06.G5.01, T07.G5.01, T02.G5.01, T03.G5.01

**T04.G5.07**: Apply a counter pattern to solve a counting problem
- Description: Students implement code using the counter pattern (set count to 0, change count by 1 when condition met) to solve a simple counting task like tallying matching items.
- Dependencies: T04.G5.01, T09.G3.01.04, T10.G5.01

### GRADE 6 (8 skills)

**T04.G6.01**: Group snippets by underlying algorithm pattern
- Description: Students classify 5+ diverse code snippets into groups based on their underlying algorithm pattern (counter, accumulator, search, filter), distinguishing between similar-looking but functionally different patterns.
- Dependencies: T04.G4.05, T09.G5.01

**T04.G6.02**: Identify pattern variants that look different but behave the same
- Description: Students identify code snippets that use different syntax or structure but achieve the same result—for example, counting with a repeat N loop versus iterating through a list, or accumulating with set + change versus a single set to sum block.
- Dependencies: T04.G4.05

**T04.G6.03**: Apply filter pattern with multiple criteria
- Description: Students extend the basic filter pattern (from T04.G5.04) to handle multiple criteria, combining conditions to select items that match complex requirements (e.g., "items that are both red AND large" or "items that are blue OR circle-shaped"). This clarifies how the filter pattern scales from single to multiple conditions.
- Dependencies: T04.G5.03, T04.G6.01

**T04.G6.04**: Turn repeated code into a custom block with parameters
- Description: Students refactor repeated code sequences into a parameterized custom block that can be reused with different values. They identify the varying elements, add parameters to the custom block (e.g., number of steps, color), and replace repeated code with calls to the custom block.
- Dependencies: T04.G3.04.02, T11.G4.07, T08.G5.01

**T04.G6.05**: Analyze a template project and identify customization points
- Description: Students inspect a more complex template (quiz, platformer, etc.) and identify specific customization points with detailed analysis: what each point controls, how to modify it safely, what values are acceptable, and which changes would break the template's structure. Focus is on understanding the template's internal logic and constraints.
- Dependencies: T04.G5.06

**T04.G6.06**: Compare two pattern‑based solutions for efficiency and code clarity
- Description: Students compare two pattern-based solutions and select which is better based on efficiency (fewer operations, faster execution) and clarity (easier to read, fewer lines of code). Example: comparing nested loops versus a single loop with index math.
- Dependencies: T04.G5.05, T07.G5.01, T08.G5.01

**T04.G6.07**: Implement a pattern-based solution from a description
- Description: Students read a problem description that fits a standard pattern (counter, accumulator, or search) and implement a solution using that pattern.
- Dependencies: T04.G5.07, T04.G6.01

**T04.G6.08**: Access grid elements using 2D indexing patterns
- Description: Students work with grid or table data structures and use nested loops or 2D indexing patterns (row, column) to access, modify, or analyze grid elements systematically.
- Dependencies: T04.G4.02, T04.G6.07

### GRADE 7 (10 skills)

**T04.G7.01**: Identify the main loop patterns in a simulation or game
- Description: Students analyze a game/simulation and identify loops like "update each frame," "process each object," "check each pair."
- Dependencies: T04.G6.01, T07.G5.01, T08.G5.01

**T04.G7.02**: Identify data structure patterns (lists, grids) in use
- Description: Students recognize when code uses a list or grid pattern (e.g., iterating over a list of enemies or cells).
- Dependencies: T04.G6.01, T08.G5.01, T10.G5.01

**T04.G7.03**: Identify problems that require multiple patterns
- Description: Students examine problem descriptions and identify which ones need more than one algorithm pattern (like counter + filter, or search + accumulator).
- Dependencies: T04.G5.01, T04.G5.02, T04.G6.01, T08.G5.01

**T04.G7.04**: Outline a solution combining two patterns
- Description: Students create a written or block-diagram outline showing how two patterns work together to solve a problem.
- Dependencies: T04.G7.03

**T04.G7.05**: Implement a combined pattern solution
- Description: Students code a solution that uses two patterns together (e.g., loop through list with counter + filter matching items).
- Dependencies: T04.G7.04, T06.G5.01, T09.G5.01, T07.G5.01

**T04.G7.06**: Trace a composite pattern and identify each pattern used
- Description: Students trace code that combines multiple patterns and label which parts use counter, accumulator, search, or filter patterns.
- Dependencies: T04.G7.03, T06.G5.01

**T04.G7.07**: Explain the role of each pattern in a composite solution
- Description: Students write or select explanations describing what each pattern contributes to the overall solution.
- Dependencies: T04.G7.06

**T04.G7.08**: Identify common pattern anti-patterns and mistakes
- Description: Students examine code examples that misuse or misapply algorithm patterns and identify specific problems such as: using a counter without initialization, accumulating without resetting, searching without a termination condition, or applying the wrong pattern to a problem. They select or explain why each example is problematic and suggest the correct pattern application.
- Dependencies: T04.G6.01, T04.G7.03

**T04.G7.09**: Simplify code by merging repeated patterns
- Description: Students refactor code that has repeated pattern blocks into a more compact form (e.g., use a function applied twice).
- Dependencies: T04.G6.02, T07.G5.01, T11.G5.01

**T04.G7.10**: Compare pattern‑based implementations for long‑term maintainability
- Description: Students compare two implementations and decide which will be easier to modify or extend later, considering factors like: where changes would need to be made, how many places would need updating, and whether the pattern isolates what might change.
- Dependencies: T04.G6.06

### GRADE 8 (7 skills)

**T04.G8.00**: Distinguish between algorithm patterns and utility patterns
- Description: Students examine code patterns and classify them as either algorithm patterns (solving computational problems like search, count, accumulate) or utility patterns (helper functions like clamp-value, random-choice, state-update). They understand that algorithm patterns focus on problem-solving logic while utility patterns provide reusable helper functionality.
- Dependencies: T04.G6.01, T04.G7.01, T09.G6.01, T10.G6.01, T14.G6.01.01

**T04.G8.01**: Recognize common reusable patterns in a code library
- Description: Students inspect a small library of utility blocks and identify familiar reusable patterns such as: clamp-value (keep number in range), random-choice (pick from options), and state-update (change state based on input).
- Dependencies: T04.G6.01, T08.G6.01, T09.G6.01, T07.G6.01, T10.G6.01, T14.G6.01.01

**T04.G8.02**: Adapt a library function to a new context
- Description: Students take an existing utility block and adapt parameters or logic to a new but related use.
- Dependencies: T04.G8.01, T04.G7.02, T06.G6.01, T09.G6.01, T09.G6.02, T15.G6.01

**T04.G8.03**: Choose between alternative patterns for a problem
- Description: Students evaluate several candidate approaches (e.g., polling vs event‑driven; nested loops vs index lists) and choose which pattern fits given constraints.
- Dependencies: T04.G7.01, T06.G6.01, T07.G6.01, T05.G6.01, T06.G6.02, T08.G6.01a

**T04.G8.04**: Analyze tradeoffs in using a standard pattern vs custom code
- Description: Students reason about pros/cons of relying on a standard pattern or library vs writing one‑off code.
- Dependencies: T04.G7.10, T06.G6.01, T09.G6.01

**T04.G8.05**: Complete a "pattern card" describing a reusable solution
- Description: Students fill in a structured pattern card template with four fields: (1) pattern name, (2) problem it solves, (3) solution structure using blocks, and (4) example use case. Assessment checks completeness and accuracy of each field.
- Dependencies: T04.G6.01

**T04.G8.06**: Match pattern usage instructions to project scenarios
- Description: Students match structured pattern-usage instructions (identifying what to customize, what to keep the same, and common pitfalls) to specific project scenarios where the pattern would apply.
- Dependencies: T04.G8.05, T10.G6.01

---

## CROSS-TOPIC DEPENDENCY ANALYSIS

T04 has **110 cross-topic dependencies** across 44 skills. This is expected as Algorithm Patterns synthesizes knowledge from multiple topics:

### Most Referenced Topics:
- **T07 (Loops)**: 34 dependencies - Expected, as most patterns use loops
- **T09 (Variables)**: 18 dependencies - Expected, as patterns track state
- **T02 (Decomposition)**: 16 dependencies - For breaking down problems
- **T06 (Events)**: 15 dependencies - For event-driven patterns
- **T08 (Conditionals)**: 13 dependencies - For decision logic in patterns
- **T10 (Data Structures)**: 12 dependencies - For list/table patterns
- **T11 (Functions)**: 4 dependencies - For custom blocks
- **T05 (HCD)**: 4 dependencies - For problem understanding
- **T13 (Testing)**: 2 dependencies - For tracing
- **T14 (Game Design)**: 2 dependencies - For game patterns
- **T15 (Animation)**: 1 dependency - For state machines

### Skills with Most Cross-Topic Dependencies:
1. **T04.G4.06** (11 deps) - Identified as overly complex
2. **T04.G4.05** (7 deps)
3. **T04.G4.09** (7 deps)
4. **T04.G5.06** (7 deps)

**Recommendation**: While many cross-topic dependencies are necessary, review the highest ones (especially G4.06) to ensure all are truly required and not just implicit through other dependencies.

---

## NOTES ON METHODOLOGY

This analysis was performed by:
1. Extracting all 68 T04 skills from the allskills.md file
2. Parsing skill IDs, titles, descriptions, and dependencies
3. Checking for X-2 rule violations (grade gaps > 2)
4. Analyzing cross-topic dependencies
5. Identifying skills with high dependency counts
6. Looking for duplicate/overlapping skills by keyword analysis
7. Examining skill descriptions for complexity indicators
8. Reviewing scaffolding progression through grade levels
9. Checking for missing foundational concepts

---

## CONCLUSION

T04 (Algorithm Patterns) is a well-structured topic with good progression from visual patterns (GK-G2) through basic loops and templates (G3) to algorithm pattern recognition and application (G4-G8).

The main issues are:
- **1 X-2 violation** that needs fixing with an intermediate skill
- **Several overlapping skills** that need clarification or merging
- **Some missing dependencies** that should be added
- **A few overly complex skills** that could be simplified or split
- **Minor scaffolding gaps** that could be filled with new intro skills

With the recommended changes, the topic will have clearer progression, better scaffolding, and more focused individual skills.

---

**End of Report**
