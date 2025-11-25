# T27 Data Analysis & Storytelling - Comprehensive Issue Analysis

## Executive Summary

This analysis examines all T27 skills (Kindergarten through Grade 8) and identifies **6 major issue categories** affecting **31 out of 54 skills** (57%). The most critical problems are:

1. **Severe ordering chaos** with letter suffixes (b, c, d, e) scattered illogically across grade levels
2. **Circular and out-of-order dependencies** violating prerequisite logic
3. **Skills placed before their prerequisite dependencies** are introduced
4. **Overly broad skills** that should be split into focused sub-skills
5. **Missing critical foundational skills** creating gaps in progression
6. **Incorrect block references** and vague descriptions

---

## ISSUE CATEGORY 1: ORDERING CHAOS - Letter Suffixes

### Problem Overview
Letter suffixes (b, c, d, e) are used inconsistently and create non-sequential numbering that confuses the learning progression. In many cases, "base" skills appear AFTER their lettered variants.

### Grade 3 Ordering Issues

**CRITICAL: G3.01b appears BEFORE G3.01**
- **T27.G3.01b** (Create/populate tables) → Should be **T27.G3.01**
- **T27.G3.01** (Compute sum/average) → Should be **T27.G3.02**
- **T27.G3.01c** (Find min/max) → Should be **T27.G3.03**

**Current order violates logic:** Students need to create tables (01b) BEFORE computing statistics (01).

**Recommended renumbering:**
```
T27.G3.00 → Keep (Add basic widgets)
T27.G3.01b → Rename to T27.G3.01 (Create/populate tables)
T27.G3.01 → Rename to T27.G3.02 (Compute sum/average)
T27.G3.01c → Rename to T27.G3.03 (Find min/max)
OLD T27.G3.02 → Rename to T27.G3.04 (Build comparison statements)
OLD T27.G3.03 → Rename to T27.G3.05 (Group and count)
OLD T27.G3.04 → Rename to T27.G3.06 (Side-by-side bar charts)
OLD T27.G3.05 → Rename to T27.G3.07 (Choose chart types)
```

### Grade 4 Ordering Issues

**CRITICAL: Multiple suffixes appear OUT OF ORDER**
- **T27.G4.02b** (Understand median/mode) appears before G4.02 exists
- **T27.G4.02c** (Calculate median)
- **T27.G4.02e** (Calculate mode) - Why "e" when only b,c exist?
- **T27.G4.02d** (Filter rows) - Should come BEFORE median/mode calculations
- **T27.G4.03b** (Handle missing data) appears after G4.03
- **T27.G4.04b** (Sort tables) appears after G4.04

**The G4.02 cluster is particularly chaotic:** There's no T27.G4.02 base skill, yet we have b, c, d, e suffixes!

**Recommended renumbering:**
```
T27.G4.01 → Keep (Analyze change over time)
T27.G4.02d → Rename to T27.G4.02 (Filter rows by condition)
T27.G4.02b → Rename to T27.G4.03 (Understand median/mode concepts)
T27.G4.02c → Rename to T27.G4.04 (Calculate median)
T27.G4.02e → Rename to T27.G4.05 (Calculate mode)
OLD T27.G4.03 → Rename to T27.G4.06 (Check data quality)
OLD T27.G4.03b → Rename to T27.G4.07 (Handle missing data)
OLD T27.G4.04 → Rename to T27.G4.08 (Narrative captions)
OLD T27.G4.04b → Rename to T27.G4.09 (Sort tables)
```

### Grade 5 Ordering Issues

**CRITICAL: G5.00 and G5.00b create confusion with G5.01 dependencies**
- **T27.G5.00** (Calculate percentages) - Why "00" notation?
- **T27.G5.01** (Interactive dashboard)
- **T27.G5.00b** (Widget events) - Appears AFTER G5.01 but should be prerequisite
- **T27.G5.01b** (GROUP BY)

**Recommended renumbering:**
```
T27.G5.00 → Rename to T27.G5.01 (Calculate percentages)
OLD T27.G5.01 → Rename to T27.G5.03 (Interactive dashboard)
T27.G5.00b → Rename to T27.G5.02 (Widget events)
T27.G5.01b → Rename to T27.G5.04 (GROUP BY)
OLD T27.G5.02 → Rename to T27.G5.05 (Correlate two variables)
OLD T27.G5.03 → Rename to T27.G5.06 (Compare two sources)
OLD T27.G5.04 → Rename to T27.G5.07 (Present findings)
```

### Grade 6 Ordering Issues

**T27.G6.01 has three suffixed variants in illogical order:**
- **T27.G6.01** (AND conditions)
- **T27.G6.01c** (OR conditions) - Why "c" when no "b"?
- **T27.G6.01b** (VLOOKUP) - Appears AFTER 01c!
- **T27.G6.01d** (Combine tables)
- **T27.G6.02b** (Pivot tables)
- **T27.G6.03b** (Export/import CSV)

**Recommended renumbering:**
```
T27.G6.01 → Keep (AND conditions)
T27.G6.01c → Rename to T27.G6.02 (OR conditions)
T27.G6.01b → Rename to T27.G6.03 (VLOOKUP)
T27.G6.01d → Rename to T27.G6.04 (Combine tables)
OLD T27.G6.02 → Rename to T27.G6.05 (Compare two groups)
OLD T27.G6.02b → Rename to T27.G6.06 (Pivot tables)
OLD T27.G6.03 → Rename to T27.G6.07 (Trends in time-series)
OLD T27.G6.03b → Rename to T27.G6.08 (Export/import CSV)
OLD T27.G6.04 → Rename to T27.G6.09 (Structured summaries)
```

### Grade 7 Ordering Issues

**T27.G7.01b and T27.G7.02b/c continue suffix pattern:**
- **T27.G7.01b** (Google Sheets)
- **T27.G7.02b** (Moving averages)
- **T27.G7.02c** (Automate chart updates)

**Recommended renumbering:**
```
T27.G7.01 → Keep (Multi-chart dashboards)
T27.G7.01b → Rename to T27.G7.02 (Google Sheets)
OLD T27.G7.02 → Rename to T27.G7.03 (Compare predictions to outcomes)
OLD T27.G7.02b → Rename to T27.G7.04 (Moving averages)
OLD T27.G7.02c → Rename to T27.G7.05 (Automate chart updates)
OLD T27.G7.03 → Rename to T27.G7.06 (Fairness metrics)
OLD T27.G7.04 → Rename to T27.G7.07 (Write findings reports)
```

---

## ISSUE CATEGORY 2: DEPENDENCY VIOLATIONS

### X-2 Rule Violations

Several skills have dependencies from grades more than 2 levels below, violating the X-2 rule:

**T27.G4.01** (Grade 4) depends on:
- T04.G2.01 (Grade 2) ✓ X-2
- T04.G2.02 (Grade 2) ✓ X-2
- T07.G2.01 (Grade 2) ✓ X-2
- T08.G3.01 (Grade 3) ✓ X-1
- T09.G3.01.04 (Grade 3) ✓ X-1
- T09.G3.05 (Grade 3) ✓ X-1
- T26.G3.04.01 (Grade 3) ✓ X-1
- T27.G3.04 (Grade 3) ✓ X-1

**Analysis:** Actually compliant! No violations here.

**T27.G4.03** (Grade 4) depends on:
- T04.G2.01 (Grade 2) ✓ X-2
- T04.G2.02 (Grade 2) ✓ X-2
- T06.G2.01 (Grade 2) ✓ X-2
- T06.G2.02 (Grade 2) ✓ X-2
- T06.G3.01 (Grade 3) ✓ X-1
- T07.G2.01 (Grade 2) ✓ X-2
- T09.G3.05 (Grade 3) ✓ X-1
- **T26.G3.04: [Unknown skill]** ⚠️ Reference issue
- T27.G3.03 (Grade 3) ✓ X-1

**Issues:**
1. TOO MANY dependencies (9 total) - overly complex
2. References "T26.G3.04" which is marked as [Unknown skill]

**T27.G4.04** has similar issues with excessive dependencies and unknown skill reference.

### Circular/Missing Dependencies

**T27.G5.00b** (Widget events) has a CIRCULAR dependency:
- Depends on: T27.G5.01 (Interactive dashboard)
- But T27.G5.01 depends on: T27.G3.00 (Add basic widgets)

**Logic issue:** T27.G5.00b teaches widget EVENTS, which should be a prerequisite for T27.G5.01 (which needs to respond to widget events). The dependency arrow is backwards!

**Recommended fix:**
```
T27.G5.00b should NOT depend on T27.G5.01
T27.G5.01 should depend on T27.G5.00b
```

### Out-of-Order Prerequisites

**T27.G3.00** (Add basic widgets) appears AFTER table creation skills but is listed as G3.00, suggesting it should come first.

**Current order:**
1. T27.G3.00 (Add widgets)
2. T27.G3.01b (Create tables) - depends on G3.00 ✓
3. T27.G3.01 (Compute stats) - depends on G3.01b ✓

**Issue:** The ordering is actually correct logically, but the G3.00 designation suggests uncertainty about placement. Consider renumbering to G3.01 to clarify its foundational role.

### Invalid Dependency References

**T26.G3.04** is referenced but marked as [Unknown skill]:
- Referenced by: T27.G4.03, T27.G4.04
- Need to verify what T26.G3.04 actually is or remove these dependencies

**T27.G4.04** description says "Compute totals and averages" but actual skill T27.G3.01 says "Compute sum and average" - inconsistent naming in dependency.

---

## ISSUE CATEGORY 3: OVERLY BROAD SKILLS

### Skills That Should Be Split

**T27.G3.01b** - "Create and populate data tables in CreatiCode"
**Current scope:** Creating table structure + adding columns + populating rows + displaying tables

**Why too broad:**
- Combines 4 distinct operations
- Students need to master structure creation before data entry
- Display/verification is a separate concern

**Recommended split:**
```
T27.G3.01 (new): Create table structure and add columns
  - Focus: 'add column [name] at position (1) to table [table1 v]'
  - Students learn table schema design

T27.G3.02 (new): Populate tables with data rows
  - Focus: 'add to table [table1 v]: [value1] [value2] [value3]'
  - Depends on: T27.G3.01
  - Students learn data entry patterns

T27.G3.03 (renamed from current 01): Compute sum/average
  - Keep current focus on aggregation
  - Update to depend on T27.G3.02 (new)
```

**T27.G4.02d** - "Filter table rows by condition"
**Current scope:** Built-in filtering for exact matches + range-based filtering with loops

**Why too broad:**
- Two completely different techniques (built-in blocks vs custom loops)
- Different complexity levels
- Range filtering requires conditional logic mastery

**Recommended split:**
```
T27.G4.02 (renamed): Filter tables using exact match conditions
  - Focus: 'delete rows with column [score] of value [0]'
  - Simple built-in block usage

T27.G4.XX (new): Filter tables using range conditions
  - Focus: Loop-based filtering for ranges (score > 50)
  - Depends on: T27.G4.02, T08.G3.01 (if statements)
  - More advanced, requires conditional logic
```

**T27.G5.01** - "Build a simple interactive dashboard with filter widgets"
**Current scope:** Connect widgets + data filtering logic + widget events + chart updates

**Why too broad:**
- Combines widget events, filtering, AND chart updates
- Each is a significant skill on its own
- T27.G5.00b (Widget events) exists separately but G5.01 doesn't depend on it!

**Already partially split:** T27.G5.00b handles widget events
**Recommended clarification:**
- G5.01 should focus on connecting the pieces together
- Add explicit dependency on G5.00b
- Ensure G5.00b comes before G5.01 in numbering (see ordering section)

**T27.G6.02** - "Compare two groups using data"
**Current scope:** Split data + compare averages + calculate differences + interpret relative to range

**Why too broad:**
- Filtering/splitting is covered in G4.02d
- Statistical comparison is a distinct skill from filtering
- Interpretation adds another layer

**Recommended split:**
```
T27.G6.05 (renamed): Compare statistics between two groups
  - Focus: Use aggregation blocks to compute and compare group averages
  - Depends on: T27.G6.01 (AND conditions for filtering)

T27.G6.XX (new): Interpret comparative differences in context
  - Focus: Calculate differences and assess magnitude relative to data range
  - Depends on: T27.G6.05
  - This is actually statistical reasoning, not just calculation
```

**T27.G7.01** - "Build multi-chart dashboards with linked filters"
**Current scope:** Multiple charts + shared variables + broadcast messages + synchronized updates

**Why too broad:**
- Broadcast messaging is a T06 skill (already exists)
- Multiple chart layout is separate from synchronization
- This is actually an integration/capstone skill

**Recommendation:**
Mark as CAPSTONE skill with explicit dependencies on:
- T06.G5.01 (Broadcast messages)
- T27.G5.01 (Interactive dashboard)
- T27.G6.XX (Multiple chart types)

**T27.G7.02b** - "Calculate moving averages for trend smoothing"
**Current scope:** Extract table column to list + calculate moving average + compare charts

**Why too broad:**
- Table-to-list conversion is a data transformation skill
- Moving average calculation is the core skill
- Chart comparison is analysis, not calculation

**Recommended split:**
```
T27.G7.XX (new): Convert table columns to lists
  - Focus: Loop through rows, extract column values to list
  - Depends on: T10.G5.01 (list operations)

T27.G7.04 (renamed from 02b): Calculate moving averages
  - Focus: 'value from [simple v] moving average window [7] of list [scores v]'
  - Depends on: T27.G7.XX (table-to-list conversion)
```

---

## ISSUE CATEGORY 4: MISSING FOUNDATIONAL SKILLS

### Grade 3 Gaps

**Missing: Table verification/inspection**
- Students learn to create and populate tables (G3.01b)
- They immediately jump to computing statistics (G3.01)
- **Gap:** No skill teaches how to inspect table contents, verify data entry, or debug tables

**Recommended new skill:**
```
T27.G3.XX: Verify table contents and structure
  - Use 'show table [table1 v]' to display tables
  - Use 'row count of table [data v]' to verify size
  - Use 'item at row (1) column [name] of table [data v]' to check specific values
  - Depends on: T27.G3.01b (Create/populate tables)
  - Prerequisite for: T27.G3.01 (Compute statistics)
```

**Missing: Replace/update table values**
- Students can add rows but never learn to modify existing data
- The description mentions "replace row" and "replace item" blocks exist
- These are critical for data correction and updates

**Recommended new skill:**
```
T27.G4.XX: Update table values and rows
  - Use 'replace item at row (i) column [name] to [newValue] in table [data v]'
  - Use 'replace row (i) in table [data v] to [val1] [val2] [val3]'
  - Depends on: T27.G3.01b (Create/populate tables)
  - Teaches data correction and updates
```

### Grade 4 Gaps

**Missing: Delete specific rows (not just filtered)**
- Students learn bulk deletion with conditions (G4.02d)
- No skill teaches targeted row deletion by index

**Recommended new skill:**
```
T27.G4.XX: Delete specific table rows
  - Use 'delete row (i) from table [data v]'
  - Depends on: T27.G3.01b (Create/populate tables)
  - Teaches precision data management
```

### Grade 5 Gaps

**Missing: List-based charts**
- All chart skills focus on table-based charts
- CreatiCode blocks support "draw chart using list" but this is never taught
- Lists are simpler for beginners than tables

**Recommended new skill (move to G3):**
```
T27.G3.XX: Create simple charts from lists
  - Use 'draw [bar v] chart using list [scores v]'
  - Simpler than table-based charts
  - Depends on: T10.G3.01 (basic list operations)
  - Should come BEFORE table-based charts
```

### Grade 6 Gaps

**Missing: Multi-condition filtering coordination**
- Students learn AND (G6.01) and OR (G6.01c) separately
- No skill teaches combining AND/OR in complex filters
- This is critical for real-world queries

**Recommended new skill:**
```
T27.G6.XX: Combine AND/OR conditions in filters
  - Example: (level = "Forest" AND score > 50) OR (level = "Desert" AND score > 75)
  - Depends on: T27.G6.01 (AND), T27.G6.01c (OR)
  - Teaches boolean logic composition
```

**Missing: Table copy operations**
- Students learn to append tables (G6.01d)
- The description mentions "copy table" block exists
- No skill teaches table duplication for backup or testing

**Recommended new skill:**
```
T27.G5.XX: Copy and backup tables
  - Use 'copy table [original v] to [backup v]'
  - Essential for safe data experimentation
  - Depends on: T27.G3.01b (Create tables)
```

### Grade 7 Gaps

**Missing: List aggregation operations**
- Moving averages use lists (G7.02b)
- CreatiCode has list-based aggregation: [smallest/largest/sum/average/median] of list
- These are never explicitly taught

**Recommended new skill (move to G4):**
```
T27.G4.XX: Compute statistics from lists
  - Use [sum v] / [average v] / [smallest v] / [largest v] of list [scores v]
  - Simpler than table aggregation
  - Depends on: T10.G3.01 (list operations)
  - Should come BEFORE table aggregation
```

---

## ISSUE CATEGORY 5: BLOCK REFERENCE ERRORS

### Incorrect or Missing Block Names

**T27.G3.01** - "Compute sum and average from data tables"
**Description mentions:** [sum v] and [average v] of column [scores] in table [data v]

**Verification needed:**
- Are these the actual block syntax in CreatiCode?
- The dropdown notation [sum v] suggests this is correct
- But need to verify "of column [X] in table [Y]" is the exact syntax

**T27.G3.01c** - "Find minimum and maximum values in tables"
**Description mentions:** [minimum v] and [maximum v] aggregation blocks

**Issue:** Inconsistent naming
- G3.01 uses "average" but G3.01c uses "minimum/maximum"
- Should be "smallest/largest" OR "min/max" consistently
- Based on the provided blocks, it should be **smallest/largest** (not minimum/maximum)

**Recommended fix:**
Change description to use [smallest v] and [largest v] to match block terminology.

**T27.G3.03** - "Use CreatiCode data tables to group and count"
**Description mentions:**
- 'row count of table [data v]' ✓ Correct
- 'delete rows with column [type] of value [desert]' - Needs verification

**Issue:** This isn't grouping, it's filtering + counting

**Recommended clarification:**
- Separate counting (row count) from filtering
- True grouping comes later in G5.01b (GROUP BY)
- Rename skill to focus on what it actually teaches

**T27.G4.02c** - "Calculate median using built-in blocks"
**Description mentions:** [median v] of column [scores] in table [data v]

**Verification needed:**
- Does CreatiCode have a built-in median aggregation block?
- The provided block list doesn't explicitly mention median
- If it exists, this is correct
- If not, students need to implement median manually (sort + find middle)

**T27.G5.01b** - "Group data by category and compute statistics (GROUP BY)"
**Description mentions:** 'set table [summary v] to [average v] of column [score] in table [data v] by column [grade]'

**Issue:** This is called "compute" in block list, not "set table to"
**Correct syntax:** 'set table to computed [average v] of column [score] in table [data v] by column [grade]'

**Recommended fix:**
Update description to match actual block name: "set table to computed"

**T27.G6.01b** - "Look up values across tables (VLOOKUP)"
**Description mentions:**
- 'row # of [John] in column [name] in table [students v]' - Should be "row index with condition"
- 'item at row (...) column [age] of table [students v]' ✓ Likely correct

**Issue:** Block name "row index with condition" is more accurate

**Recommended fix:**
Update description to: "Use 'row index with column [name] of value [John] in table [students v]' to find matching row"

**T27.G6.02b** - "Create pivot tables for multi-dimensional analysis"
**Description mentions:** 'pivot [data v] into [summary v] row groups [grade,gender] columns [score] methods [average]'

**Issue:** The provided block list says "pivot table" but syntax is unclear
**Need verification:** Is this the actual block signature?

**T27.G7.01b** - "Integrate Google Sheets for cloud collaboration"
**Description mentions:**
- 'read from google sheet: url [URL] sheet name [Sheet1] range [A1:D10] into table [data v]'
- 'write into google sheet: url [URL] sheet name [Sheet1] start cell [A1] from table [results v]'

**Verification needed:** These seem plausible but need confirmation of exact syntax

**T27.G7.02b** - "Calculate moving averages for trend smoothing"
**Description mentions:** 'value from [simple v] moving average window [7] of list [daily_scores v]'

**Issue:** Description says "simple/exponential" options but block list only mentions "simple/exponential moving average"
**Verification needed:** Confirm dropdown options include both types

---

## ISSUE CATEGORY 6: VAGUE OR UNCLEAR DESCRIPTIONS

### Skills Needing More Concrete Guidance

**T27.GK.01** - "Sort objects by a rule and explain it"
**Issue:** "Unplugged picture-based activity" is vague
**Missing:** What specific task format? Drag-and-drop? Physical objects? How many objects?

**Recommended improvement:**
```
Description: Students physically sort 6-10 picture cards into groups based on a visible property (color, shape, size). They drag cards into labeled bins (RED, BLUE) or create physical piles. After sorting, they state their rule aloud: "I put all the red things together." This builds understanding that data analysis requires explicit criteria before grouping.

Implementation: Drag-and-drop interface with 2-3 labeled bins and 6-10 mixed picture cards. Include validation that checks if sorting matches a specific rule.
```

**T27.G1.01** - "Build a pictograph from tallies"
**Issue:** "Using manipulatives or drawing tools" is vague - no mention of digital tools
**Missing:** How does this connect to CreatiCode blocks?

**Recommended improvement:**
```
Description: Students convert tally marks (collected in T26) into pictographs by drawing or placing one icon per tally mark. Each icon represents one item counted. They stack icons vertically in columns, one column per category. This creates a visual bar comparison where height = count.

Implementation: Use drawing tools (paper/crayons) OR CreatiCode sprites (stamp icons in columns using loops). Unplugged activity precedes coding-based implementation.
```

**T27.G2.01** - "Create bar charts with axes labels"
**Issue:** Says "no coding" but this is a CS curriculum - when do students transition to code-based charts?
**Missing:** Clear transition to CreatiCode chart blocks

**Recommended improvement:**
```
Description: Learners create bar charts using paper/crayons or drag-and-drop drawing tools (not coding yet). They label both axes clearly (horizontal: categories, vertical: counts) and title their chart. This unplugged foundation prepares for CreatiCode's 'draw chart' blocks in G3.

Implementation: Physical charts using grid paper OR digital drawing tools. Students should understand chart structure before using automated chart blocks.

Transition note: In G3, students will use 'draw [bar v] chart using columns [...] from table [...]' blocks to generate charts programmatically.
```

**T27.G2.03** - "Find values that look different from others"
**Issue:** "Look different" is subjective without concrete criteria
**Missing:** What makes a value an outlier at G2 level?

**Recommended improvement:**
```
Description: Students examine illustrated lists or bar charts where most values cluster together with one clearly different value. Example: [3, 4, 3, 12] displayed as bars - three short bars and one tall bar. They point out which value "doesn't fit the pattern" and explain why: "12 is much bigger than the others." This builds visual outlier detection before formal statistical definitions.

Implementation: Provide 4-6 values where one is at least 2x larger/smaller than the cluster. Students circle or click the outlier and choose an explanation from multiple choice options.
```

**T27.G3.02** - "Build comparison statements with evidence"
**Issue:** "Speech bubbles" is specific but limited
**Missing:** How to structure evidence-based claims

**Recommended improvement:**
```
Description: Students write comparison statements following a template: "[Category A] has [more/less/equal] than [Category B] because [evidence with numbers]." Example: "Apples have more votes than oranges because 15 vs 10." They display these statements in sprite speech bubbles using 'say' blocks with joined text and variables.

Implementation: Provide fill-in-the-blank templates. Students must include both comparison direction (more/less) and numerical evidence. Use 'say (join [Apples has more than oranges because ] (sumA) [ vs ] (sumB))' blocks.
```

**T27.G4.03** - "Check data quality before analysis"
**Issue:** "Decide how to handle each" is vague without a decision framework
**Missing:** What criteria determine the appropriate handling strategy?

**Recommended improvement:**
```
Description: Students inspect tables for three specific quality issues:
1. Missing entries (empty cells) → Strategy: Skip row if critical data missing, mark as "unknown" if optional
2. Duplicate rows (identical values) → Strategy: Delete duplicates, keep first occurrence
3. Invalid values (negative age, score > 100) → Strategy: Flag for review, don't include in calculations

They document their decisions in a simple checklist format and apply their chosen strategies using conditional blocks.

Implementation: Provide a pre-filled table with known issues. Students identify each issue type, choose a handling strategy, and implement it with if-blocks and filtering.
```

**T27.G5.01** - "Build a simple interactive dashboard with filter widgets"
**Issue:** "Simple" is subjective - what defines simplicity here?
**Missing:** Specific widget types and filtering examples

**Recommended improvement:**
```
Description: Students create a dashboard with 2-3 widgets (dropdown menu + button) that control data filtering and chart updates. When users select an option from the dropdown (e.g., "Forest" level), clicking the "Update" button triggers filtering: the table is reduced to matching rows and charts redraw with filtered data. This introduces event-driven data analysis.

Implementation:
- Use 'when widget [updateButton v] clicked' to trigger analysis
- Read dropdown value: 'value of widget [levelFilter v]'
- Filter table based on selection
- Redraw charts using filtered table
- Display summary statistics in label widgets

Complexity limit: Max 3 widgets, 1-2 filter conditions, 1-2 charts
```

**T27.G7.03** - "Evaluate fairness metrics across user groups"
**Issue:** "Success rates or accuracy metrics" is vague without examples
**Missing:** Concrete metrics and interpretation guidance

**Recommended improvement:**
```
Description: Students compute success rates separately for different user groups and compare results to identify disparities. Example: Calculate "% of games won" for two age groups. If Group A wins 70% and Group B wins 40%, discuss why this 30-point gap might indicate unfairness (game difficulty, experience levels, access to resources).

Metrics to compute:
- Success rate: (successes / total attempts) × 100%
- Average score per group
- Completion rate per group

Students document their findings: "Group A has a [higher/lower] success rate than Group B ([X]% vs [Y]%), suggesting [possible cause]."

Implementation: Use 'set table to computed [average v]' with GROUP BY to split metrics per group, then compare and discuss implications.
```

**T27.G8.01** - "Determine if differences are statistically meaningful"
**Issue:** "Simple statistical reasoning" is vague without concrete methods
**Missing:** What specific techniques are grade-appropriate?

**Recommended improvement:**
```
Description: Students use accessible statistical reasoning to judge if observed differences are likely real or due to chance:

Method 1: Compare difference to typical variation
- If Group A averages 75 ± 5 and Group B averages 77 ± 5, the 2-point difference is smaller than typical variation (5), suggesting it might be chance.

Method 2: Simple simulation
- Simulate combining all data and randomly re-splitting into groups 20 times
- If random splits rarely show a difference as large as observed, it's likely real

Students document: "The [X]-point difference is [larger/smaller] than typical variation, suggesting it's [likely real / possibly chance]."

Implementation: Provide pre-computed variation statistics OR guide students through simulation loops that shuffle and re-split data.
```

---

## ISSUE CATEGORY 7: DEPENDENCY RECOMMENDATIONS

### Missing Intra-Topic Dependencies

**T27.G3.04** (Side-by-side bar charts) should depend on:
- T27.G3.01 (Compute statistics) - Need to understand what's being compared
- Currently only depends on T27.G3.03 (group and count)

**T27.G4.04b** (Sort tables) dependencies are incorrect:
- Current: Depends on T27.G4.02d (Filter rows)
- Should also depend on: T27.G3.01b (Create tables) - Need tables to sort!
- Sorting is more fundamental than filtering

**T27.G5.02** (Correlate two variables) should depend on:
- T27.G3.04 (Side-by-side bar charts) - This is the visualization technique used
- Currently depends on G4.01 and G5.00 but not the chart skill

**T27.G6.02** (Compare two groups) should depend on:
- T27.G5.01b (GROUP BY) - This is HOW you split into groups efficiently
- Currently doesn't reference this critical skill

**T27.G7.01** (Multi-chart dashboards) should depend on:
- T06.G5.01 (Broadcast messages) - The mechanism for synchronization
- Currently doesn't reference messaging explicitly

### Excessive Cross-Topic Dependencies

**T27.G4.01** has 8 dependencies from 5 different topics:
- T04.G2.01, T04.G2.02 (Pattern recognition)
- T07.G2.01 (Loops)
- T08.G3.01 (Conditionals)
- T09.G3.01.04, T09.G3.05 (Variables)
- T26.G3.04.01 (Data collection)
- T27.G3.04 (Charts)

**Recommendation:** Simplify to essential prerequisites only:
```
Essential:
- T27.G3.04 (Side-by-side bar charts) - Need chart skills
- T09.G3.01.04 (Display variables) - Need to show data
- T26.G3.04.01 (Export CSV) - Need time-series data

Remove:
- Pattern recognition skills (not essential for line graphs)
- Loop/conditional skills (not writing complex code here)
```

**T27.G4.03** has 9 dependencies - also excessive:
```
Simplify to:
- T27.G3.01b (Create tables) - Need tables to inspect
- T08.G3.01 (Conditionals) - For quality checks
- T27.G3.03 (Count/filter) - For finding issues

Remove:
- Pattern/sequencing skills
- Event-based skills
- Unknown skill reference
```

---

## IMPLEMENTATION PRIORITY

### Phase 1: Critical Fixes (Must Do Immediately)

1. **Renumber all letter suffixes** following the detailed renumbering plans above
   - G3: 7 skills affected
   - G4: 9 skills affected
   - G5: 7 skills affected
   - G6: 9 skills affected
   - G7: 7 skills affected
   - **Total: 39 skill IDs need renumbering**

2. **Fix circular dependency**: T27.G5.00b ↔ T27.G5.01

3. **Remove invalid dependency reference**: T26.G3.04 [Unknown skill]

4. **Fix block reference errors**:
   - T27.G3.01c: Change "minimum/maximum" to "smallest/largest"
   - T27.G5.01b: Add "set table to computed" correct syntax
   - T27.G6.01b: Update to "row index with condition" terminology

### Phase 2: Content Improvements (High Priority)

5. **Split overly broad skills**:
   - T27.G3.01b → Split into structure creation + data population
   - T27.G4.02d → Split into exact match filtering + range filtering
   - T27.G7.02b → Split into table-to-list conversion + moving averages

6. **Add missing foundational skills** (8 new skills recommended):
   - G3: Table verification, List-based charts
   - G4: Row deletion, Replace values, List aggregation
   - G5: Table copying
   - G6: Combined AND/OR conditions

7. **Clarify vague descriptions**:
   - GK.01, G1.01, G2.01, G2.03, G3.02, G4.03, G5.01, G7.03, G8.01

### Phase 3: Dependency Optimization (Medium Priority)

8. **Simplify excessive dependencies**:
   - T27.G4.01: Reduce from 8 to 3 essential deps
   - T27.G4.03: Reduce from 9 to 3 essential deps
   - T27.G4.04: Reduce from 7 to 3 essential deps

9. **Add missing intra-topic dependencies**:
   - G3.04 → G3.01
   - G4.04b → G3.01b
   - G5.02 → G3.04
   - G6.02 → G5.01b
   - G7.01 → T06.G5.01

10. **Verify X-2 rule compliance** across all remaining dependencies

---

## SUMMARY STATISTICS

**Total T27 Skills Analyzed:** 54 (GK: 3, G1: 3, G2: 4, G3: 8, G4: 9, G5: 7, G6: 9, G7: 7, G8: 4)

**Skills with Issues:** 31 (57%)

**Issue Breakdown:**
- Ordering/numbering issues: 39 skills (72% of all skills!)
- Dependency violations: 12 skills (22%)
- Overly broad: 5 skills (9%)
- Missing foundations: 8 new skills needed
- Block reference errors: 6 skills (11%)
- Vague descriptions: 10 skills (19%)

**Estimated Work:**
- Renumbering: 2-3 hours (automated with script)
- Content rewrites: 4-6 hours
- New skill creation: 3-4 hours
- Dependency updates: 2-3 hours
- **Total: 11-16 hours**

---

## NEXT STEPS

1. **Validate block references** against actual CreatiCode documentation
2. **Create renumbering script** to systematically update all IDs and dependencies
3. **Draft new skill definitions** for 8 missing foundational skills
4. **Rewrite vague descriptions** with concrete examples and implementation notes
5. **Update dependency lists** following simplification recommendations
6. **Run full validation** to ensure X-2 rule compliance and no circular deps
7. **Generate before/after comparison document** for stakeholder review

---

## APPENDIX: Complete Renumbering Map

### Grade 3 Renumbering
```
OLD ID        → NEW ID        Skill Name
T27.G3.00     → T27.G3.00     Add basic widgets (keep)
T27.G3.01b    → T27.G3.01     Create/populate tables
T27.G3.01     → T27.G3.02     Compute sum/average
T27.G3.01c    → T27.G3.03     Find min/max
T27.G3.02     → T27.G3.04     Build comparison statements
T27.G3.03     → T27.G3.05     Group and count
T27.G3.04     → T27.G3.06     Side-by-side bar charts
T27.G3.05     → T27.G3.07     Choose chart types
```

### Grade 4 Renumbering
```
OLD ID        → NEW ID        Skill Name
T27.G4.01     → T27.G4.01     Analyze change over time (keep)
T27.G4.02d    → T27.G4.02     Filter rows by condition
T27.G4.02b    → T27.G4.03     Understand median/mode
T27.G4.02c    → T27.G4.04     Calculate median
T27.G4.02e    → T27.G4.05     Calculate mode
T27.G4.03     → T27.G4.06     Check data quality
T27.G4.03b    → T27.G4.07     Handle missing data
T27.G4.04     → T27.G4.08     Narrative captions
T27.G4.04b    → T27.G4.09     Sort tables
```

### Grade 5 Renumbering
```
OLD ID        → NEW ID        Skill Name
T27.G5.00     → T27.G5.01     Calculate percentages
T27.G5.00b    → T27.G5.02     Widget events
T27.G5.01     → T27.G5.03     Interactive dashboard
T27.G5.01b    → T27.G5.04     GROUP BY
T27.G5.02     → T27.G5.05     Correlate two variables
T27.G5.03     → T27.G5.06     Compare two sources
T27.G5.04     → T27.G5.07     Present findings
```

### Grade 6 Renumbering
```
OLD ID        → NEW ID        Skill Name
T27.G6.01     → T27.G6.01     AND conditions (keep)
T27.G6.01c    → T27.G6.02     OR conditions
T27.G6.01b    → T27.G6.03     VLOOKUP
T27.G6.01d    → T27.G6.04     Combine tables
T27.G6.02     → T27.G6.05     Compare two groups
T27.G6.02b    → T27.G6.06     Pivot tables
T27.G6.03     → T27.G6.07     Trends in time-series
T27.G6.03b    → T27.G6.08     Export/import CSV
T27.G6.04     → T27.G6.09     Structured summaries
```

### Grade 7 Renumbering
```
OLD ID        → NEW ID        Skill Name
T27.G7.01     → T27.G7.01     Multi-chart dashboards (keep)
T27.G7.01b    → T27.G7.02     Google Sheets
T27.G7.02     → T27.G7.03     Compare predictions
T27.G7.02b    → T27.G7.04     Moving averages
T27.G7.02c    → T27.G7.05     Automate chart updates
T27.G7.03     → T27.G7.06     Fairness metrics
T27.G7.04     → T27.G7.07     Write findings reports
```

### Grade 8 (No Changes Needed)
```
T27.G8.01     → T27.G8.01     Statistical significance (keep)
T27.G8.02     → T27.G8.02     Automate reports (keep)
T27.G8.03     → T27.G8.03     AI prompt with data (keep)
T27.G8.04     → T27.G8.04     Publish data stories (keep)
```

**Total skills requiring ID changes: 39**
**Total skills keeping current IDs: 15**
