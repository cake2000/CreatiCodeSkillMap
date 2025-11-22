# T27 Phase 1 - Detailed Fix Specifications

## Instructions for Implementation

This document provides exact find-replace instructions for all T27 fixes. Each fix includes:
- Skill ID
- Issue type
- Current text (to find)
- New text (to replace)
- Rationale

---

## HIGH PRIORITY FIXES

### FIX H1: T27.G3.03 - Backwards Filtering Logic

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G3.03

**Find:**
```
Description: Students use CreatiCode table blocks to filter rows by category (e.g., using 'delete rows with column [type] of value [desert]' to keep only forest levels) and count how many rows match (using 'row count of table [data v]'), learning simple data grouping and filtering operations.
```

**Replace:**
```
Description: Students use CreatiCode table blocks to filter rows by category (e.g., using 'delete rows with column [type] of value [desert]' to remove desert levels, keeping only other types) and count how many rows match (using 'row count of table [data v]'), learning simple data grouping and filtering operations.
```

**Rationale:** Deleting rows with value "desert" REMOVES deserts, it doesn't keep forests. The description logic was backwards.

---

### FIX H2: T27.G4.02 - Non-existent "percentage chart block"

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G4.02

**Find:**
```
Description: Students compute percentage breakdowns (e.g., 15 out of 50 = 30%) from categorized tables using division and the percentage chart block, connecting raw counts to relative comparisons for interpretive analysis.
```

**Replace:**
```
Description: Students compute percentage breakdowns (e.g., 15 out of 50 = 30%) from categorized tables using division and display results using percentage charts (created with 'draw [percentage v] chart using columns [...] from table [...]'), connecting raw counts to relative comparisons for interpretive analysis.
```

**Rationale:** There is no "percentage chart block" - percentage is a chart TYPE option in the draw chart block.

---

### FIX H3: T27.G4.02d - Non-existent "keep rows" block (Part 1)

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G4.02d

**Find:**
```
Description: Students use CreatiCode filtering blocks to keep or remove rows matching specific criteria (e.g., 'delete rows with column [score] of value [0]' to remove incomplete data, or 'keep rows with column [level] > [5]' to analyze advanced levels only). This prepares for dashboard filtering and data quality control.
```

**Replace:**
```
Description: Students use CreatiCode filtering blocks to remove rows matching specific criteria (e.g., 'delete rows with column [score] of value [0]' to remove incomplete data). For more complex filtering (like keeping rows where level > 5), they learn to iterate through rows using loops and conditional logic to copy matching rows to a new table. This prepares for dashboard filtering and data quality control.
```

**Rationale:** There is NO "keep rows" block in CreatiCode. Only "delete rows with column [col] of value [exactValue]" exists, and it only supports exact value matching (no >, <, >= operators).

---

### FIX H4: T27.G4.02d - Forward Dependency (Part 2)

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G4.02d

**Find:**
```
Dependencies:
* T27.G4.03: Check data quality before analysis
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
```

**Replace:**
```
Dependencies:
* T27.G3.03: Use CreatiCode data tables to group and count
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
```

**Rationale:** T27.G4.02d was depending on T27.G4.03, but G4.03 comes BEFORE G4.02d in the sequence. This is a forward dependency. Changed to depend on T27.G3.03 which teaches basic filtering.

---

### FIX H5: T27.G6.01 - Impossible Compound Conditions

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G6.01

**Find:**
```
Description: Students use CreatiCode table blocks to filter rows by compound conditions (e.g., keep rows where score > 50 AND level = "Forest") before computing summaries or drawing charts, enabling more sophisticated data subset analysis.
```

**Replace:**
```
Description: Students implement compound filtering logic by combining multiple table operations and conditional checks (e.g., first delete rows where level ≠ "Forest", then use loops with conditionals to delete rows where score ≤ 50), building complex filters from basic operations before computing summaries or drawing charts.
```

**Rationale:** CreatiCode doesn't have "keep rows" blocks or support compound conditions with comparison operators. Students must build complex filters using loops and conditionals.

---

### FIX H6: T27.G6.01b - Wrong VLOOKUP Syntax

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G6.01b

**Find:**
```
Description: Students use 'item in column [age] of [students v] where column [name] equals [John]' to retrieve related information from tables, similar to spreadsheet VLOOKUP operations. This enables cross-referencing data from different sources (e.g., looking up student scores by matching names across two tables).
```

**Replace:**
```
Description: Students use a two-step lookup process: first 'row # of [John] in column [name] in table [students v]' to find the matching row, then 'item at row (...) column [age] of table [students v]' to retrieve related information, similar to spreadsheet VLOOKUP operations. This enables cross-referencing data from different sources (e.g., looking up student scores by matching names across two tables).
```

**Rationale:** The syntax "item in column [age] of [students v] where column [name] equals [John]" doesn't exist. Must use two blocks: find row number, then get item at that row.

---

### FIX H7: T27.G7.01b - Incomplete Google Sheets Syntax

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G7.01b

**Find:**
```
Description: Students use 'read from google sheet: url [...] into table [data v]' to import shared data and 'write into google sheet: ... from table [results v]' to publish findings. This enables real-time collaboration and data sharing beyond CreatiCode, connecting to professional cloud workflows.
```

**Replace:**
```
Description: Students use 'read from google sheet: url [URL] sheet name [Sheet1] range [A1:D10] into table [data v]' to import shared data and 'write into google sheet: url [URL] sheet name [Sheet1] start cell [A1] from table [results v]' to publish findings. This enables real-time collaboration and data sharing beyond CreatiCode, connecting to professional cloud workflows.
```

**Rationale:** The abbreviated syntax was missing required parameters: sheet name, range (for read), and start cell (for write).

---

## MEDIUM PRIORITY FIXES

### FIX M1: T27.G3.01 - Expand Aggregation Functions

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G3.01

**Find:**
```
Description: Students use CreatiCode's built-in aggregation blocks ([sum v] of column [scores] in table [data v] and [average v] of column [scores] in table [data v]) to quickly compute totals and means from data tables, learning to use powerful analysis tools efficiently without manual loops.
```

**Replace:**
```
Description: Students use CreatiCode's built-in aggregation blocks to compute statistics from data tables: [sum v], [average v], [median v], [minimum v], and [maximum v] of column [scores] in table [data v], learning to use powerful analysis tools efficiently without manual loops.
```

**Rationale:** CreatiCode supports 5 aggregation functions (sum, average, median, min, max), but description only mentioned 2 (sum, average).

---

### FIX M2: T27.G4.02c - No Mode Aggregation Block

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G4.02c

**Find:**
```
Description: Students implement median calculation by sorting a list and finding the middle value, and mode calculation by counting frequencies. They use CreatiCode's aggregation blocks ([median v] of column [scores] in table [data v]) along with sorting and conditional blocks to compute these statistics, connecting statistical concepts to code implementation.
```

**Replace:**
```
Description: Students implement median calculation using CreatiCode's built-in aggregation block ([median v] of column [scores] in table [data v]), and mode calculation by manually counting frequencies using loops and conditional logic (as there is no built-in mode aggregation block). They connect statistical concepts to code implementation through a mix of built-in functions and custom algorithms.
```

**Rationale:** There is NO mode aggregation block in CreatiCode. Mode must be calculated manually with loops. Description incorrectly implied mode was built-in.

---

### FIX M3: T27.G5.01 - Specify Widget Blocks

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G5.01

**Find:**
```
Description: Students connect 2-3 CreatiCode widgets (dropdown menus or buttons created with widget blocks) to data tables so viewers can filter by one category (e.g., clicking "Forest" button shows only forest level data) and watch a single chart update dynamically. This introduces interactive data exploration.
```

**Replace:**
```
Description: Students connect 2-3 CreatiCode widgets (using 'add dropdown menu' and 'add button' blocks) to data tables, responding to 'when widget [name v] clicked' or 'when widget [name v] changes' events, so viewers can filter by one category (e.g., clicking "Forest" button shows only forest level data) and watch a single chart update dynamically. This introduces interactive data exploration.
```

**Rationale:** Made explicit which widget blocks to use and how to handle events, reducing ambiguity.

---

### FIX M4: T27.G7.02b - Moving Average Works on Lists

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G7.02b

**Find:**
```
Description: Students use 'value from [simple v] moving average window [7] of list [daily_scores v]' to calculate rolling averages that reveal underlying trends by reducing noise in time-series data. They compare raw vs smoothed charts to interpret patterns more clearly.
```

**Replace:**
```
Description: Students extract table columns into lists (since moving average works on lists, not tables), then use 'value from [simple v] moving average window [7] of list [daily_scores v]' to calculate rolling averages that reveal underlying trends by reducing noise in time-series data. They compare raw vs smoothed charts to interpret patterns more clearly.
```

**Rationale:** Critical implementation detail: moving average block works on LISTS not TABLES. Must extract column to list first.

---

## X-2 RULE VIOLATION FIXES

### FIX X1: T27.G7.02 - G3→G7 Dependency (T09.G3.05)

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G7.02

**Find:**
```
Dependencies:
* T08.G5.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G5.04: Separate raw data from summary data
* T27.G7.01: Build multi-chart dashboards with linked filters
```

**Replace:**
```
Dependencies:
* T08.G5.01: Use a simple if in a script
* T09.G5.01: Model real-world quantities using variables and formulas
* T26.G5.04: Separate raw data from summary data
* T27.G7.01: Build multi-chart dashboards with linked filters
```

**Rationale:** T09.G3.05 is G3→G7 (4 grade jump, exceeds X-2). Replaced with T09.G5.01 (G5→G7, within X-2).

---

### FIX X2: T27.G7.03 - G3→G7 Dependency (T09.G3.05)

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G7.03

**Find:**
```
Dependencies:
* T08.G5.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G5.04: Separate raw data from summary data
* T27.G7.02: Compare predictions to actual outcomes
```

**Replace:**
```
Dependencies:
* T08.G5.01: Use a simple if in a script
* T09.G5.01: Model real-world quantities using variables and formulas
* T26.G5.04: Separate raw data from summary data
* T27.G7.02: Compare predictions to actual outcomes
```

**Rationale:** Same as FIX X1 - T09.G3.05 exceeds X-2 rule. Replaced with T09.G5.01.

---

### FIX X3: T27.G7.04 - G4→G7 Dependency (T10.G4.01)

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G7.04

**Find:**
```
Dependencies:
* T06.G5.01: Broadcast a custom message and respond in another sprite
* T10.G4.01: Use list length and item access in expressions
* T26.G5.04: Separate raw data from summary data
* T27.G7.03: Evaluate fairness metrics across user groups
```

**Replace:**
```
Dependencies:
* T06.G5.01: Broadcast a custom message and respond in another sprite
* T10.G5.03: Add and remove items from a list
* T26.G5.04: Separate raw data from summary data
* T27.G7.03: Evaluate fairness metrics across user groups
```

**Rationale:** T10.G4.01 is G4→G7 (3 grade jump, exceeds X-2). Replaced with T10.G5.03 (G5→G7, within X-2).

---

## LOW PRIORITY FIXES (Optional)

### FIX L1: T27.GK.01 - Clarify Unplugged

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.GK.01

**Find:**
```
Description: In this picture-based activity, students group objects (shapes, animals) and state the rule ("all red things"), reinforcing that analysis starts with describing criteria.
```

**Replace:**
```
Description: In this unplugged picture-based activity, students physically group objects (shapes, animals) and state the sorting rule ("all red things"), reinforcing that analysis starts with describing criteria.
```

**Rationale:** Minor clarity improvement - explicitly states this is unplugged (no computer/CreatiCode).

---

### FIX L2: T27.G5.04 - Specify Presentation Platform

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G5.04

**Find:**
```
Description: Learners assemble one chart + one key insight + one recommendation in a short presentation, practicing clear data-driven communication for specific audiences.
```

**Replace:**
```
Description: Learners assemble one chart (screenshot from CreatiCode) + one key insight + one recommendation in a short presentation (using Google Slides, PowerPoint, or text widgets in CreatiCode), practicing clear data-driven communication for specific audiences.
```

**Rationale:** Clarifies where/how to create the presentation.

---

### FIX L3: T27.G7.02 - Define "Residual"

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G7.02

**Find:**
```
Description: Learners compare predicted values versus actual outcomes (e.g., XO's time estimate vs actual time), calculate the difference (residual) for each prediction, and identify patterns in errors to detect systematic over- or under-prediction.
```

**Replace:**
```
Description: Learners compare predicted values versus actual outcomes (e.g., XO's time estimate vs actual time), calculate the difference (called a "residual" in statistics) for each prediction, and identify patterns in errors to detect systematic over- or under-prediction.
```

**Rationale:** Defines unfamiliar term "residual" inline for Grade 7 students.

---

### FIX L4: T27.G8.03 - Clarify XO is CreatiCode's AI

**File:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

**Skill ID:** T27.G8.03

**Find:**
```
Description: Students extract key statistics from their analysis, construct prompts that include these metrics (e.g., "Given average score=75 and 20% drop-off at level 3, suggest improvements"), send to XO, and critically evaluate whether the AI's recommendations align with the data.
```

**Replace:**
```
Description: Students extract key statistics from their analysis, construct prompts that include these metrics (e.g., "Given average score=75 and 20% drop-off at level 3, suggest improvements"), send to XO (CreatiCode's AI assistant), and critically evaluate whether the AI's recommendations align with the data.
```

**Rationale:** Clarifies XO is CreatiCode's built-in AI for educators unfamiliar with the platform.

---

## SUMMARY OF CHANGES

| Fix ID | Skill ID | Type | Change Summary |
|--------|----------|------|----------------|
| H1 | T27.G3.03 | Logic Error | Fix backwards filtering description |
| H2 | T27.G4.02 | Wrong Block | "percentage chart block" → "percentage chart type" |
| H3 | T27.G4.02d | Wrong Block | Remove "keep rows" reference |
| H4 | T27.G4.02d | Dependency | Fix forward dependency (G4.03→G3.03) |
| H5 | T27.G6.01 | Wrong Block | Fix compound condition filtering |
| H6 | T27.G6.01b | Wrong Syntax | Fix VLOOKUP two-step process |
| H7 | T27.G7.01b | Incomplete | Complete Google Sheets syntax |
| M1 | T27.G3.01 | Incomplete | Add median, min, max to aggregations |
| M2 | T27.G4.02c | Wrong Block | Clarify no mode aggregation block |
| M3 | T27.G5.01 | Vague | Specify widget block names |
| M4 | T27.G7.02b | Missing Detail | Note moving average uses lists not tables |
| X1 | T27.G7.02 | X-2 Violation | Replace T09.G3.05 with T09.G5.01 |
| X2 | T27.G7.03 | X-2 Violation | Replace T09.G3.05 with T09.G5.01 |
| X3 | T27.G7.04 | X-2 Violation | Replace T10.G4.01 with T10.G5.03 |
| L1 | T27.GK.01 | Clarity | Add "unplugged" clarification |
| L2 | T27.G5.04 | Clarity | Specify presentation platforms |
| L3 | T27.G7.02 | Terminology | Define "residual" inline |
| L4 | T27.G8.03 | Context | Clarify XO is CreatiCode's AI |

**Total Changes: 18 fixes**
- 7 HIGH priority (accuracy)
- 4 MEDIUM priority (completeness)
- 3 X-2 violations (dependencies)
- 4 LOW priority (clarity)

---

## VALIDATION CHECKLIST

After implementing all fixes, verify:
- [ ] All block syntax matches blockdes8.txt exactly
- [ ] No forward dependencies within T27
- [ ] All cross-topic dependencies satisfy X-2 rule (max 2 grade jumps)
- [ ] K-2 skills remain unplugged (no CreatiCode blocks)
- [ ] G3 skills introduce table basics before advanced operations
- [ ] All aggregation references are accurate (sum, average, median, min, max only)
- [ ] No references to non-existent blocks ("keep rows", "mode aggregation", "percentage chart block")
- [ ] Google Sheets syntax includes all required parameters
- [ ] Moving average descriptions mention lists not tables

---

**End of Detailed Fix Specifications**
