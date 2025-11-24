# T27 (Data Analysis & Storytelling) - Comprehensive Analysis Report

## Executive Summary

Topic T27 contains **54 skills** spanning grades K-8, teaching data analysis, visualization, and storytelling. The analysis identified several critical issues requiring immediate attention, particularly around skill ordering, dependencies, and alignment with CreatiCode's actual features.

### Priority Issues
- **HIGH**: 8 issues (skill ordering, circular dependencies, missing prerequisites)
- **MEDIUM**: 12 issues (overlaps, splits needed, description clarity)
- **LOW**: 6 issues (minor improvements, consistency)

---

## Complete T27 Skills Inventory

### Grade K (3 skills)
1. **T27.GK.01** - Sort objects by a rule and explain it
2. **T27.GK.02** - Compare which group has more
3. **T27.GK.03** - Read a two-column picture chart

### Grade 1 (3 skills)
4. **T27.G1.01** - Build a pictograph from tallies
5. **T27.G1.02** - Answer "how many more?" questions
6. **T27.G1.03** - Tell a one-sentence story with data

### Grade 2 (4 skills)
7. **T27.G2.01** - Create bar charts with axes labels
8. **T27.G2.02** - Interpret simple line plots
9. **T27.G2.03** - Find values that look different from others
10. **T27.G2.04** - Decide if data answers the question asked

### Grade 3 (9 skills)
11. **T27.G3.00** - Add basic widgets to display information
12. **T27.G3.01b** - Create and populate data tables in CreatiCode
13. **T27.G3.01** - Compute sum and average from data tables
14. **T27.G3.01c** - Find minimum and maximum values in tables
15. **T27.G3.02** - Build comparison statements with evidence
16. **T27.G3.03** - Use CreatiCode data tables to group and count
17. **T27.G3.04** - Create side-by-side bar charts for two groups
18. **T27.G3.05** - Choose appropriate chart types for data
19. (Note: T27.G3.05 is the last official G3 skill, though some G4 skills appear to build on G3)

### Grade 4 (9 skills)
20. **T27.G4.01** - Analyze change over time using line graphs
21. **T27.G4.02b** - Understand median and mode concepts
22. **T27.G4.02c** - Calculate median using built-in blocks
23. **T27.G4.02e** - Calculate mode by counting frequencies
24. **T27.G4.02d** - Filter table rows by condition
25. **T27.G4.03** - Check data quality before analysis
26. **T27.G4.03b** - Handle missing or invalid data
27. **T27.G4.04** - Create narrative captions for charts
28. **T27.G4.04b** - Sort tables to organize data

### Grade 5 (8 skills)
29. **T27.G5.00** - Calculate percentages from grouped data
30. **T27.G5.01** - Build a simple interactive dashboard with filter widgets
31. **T27.G5.00b** - Respond to widget events in dashboards
32. **T27.G5.01b** - Group data by category and compute statistics (GROUP BY)
33. **T27.G5.02** - Correlate two variables visually
34. **T27.G5.03** - Compare data from two sensors or sources
35. **T27.G5.04** - Present findings using slides or mini reports

### Grade 6 (9 skills)
36. **T27.G6.01** - Filter tables using AND conditions
37. **T27.G6.01c** - Filter tables using OR conditions
38. **T27.G6.01b** - Look up values across tables (VLOOKUP)
39. **T27.G6.01d** - Combine data from two tables
40. **T27.G6.02** - Compare two groups using data
41. **T27.G6.02b** - Create pivot tables for multi-dimensional analysis
42. **T27.G6.03** - Identify trends and patterns in time-series data
43. **T27.G6.03b** - Export and import data using CSV files
44. **T27.G6.04** - Create structured summaries with labeled findings

### Grade 7 (6 skills)
45. **T27.G7.01** - Build multi-chart dashboards with linked filters
46. **T27.G7.01b** - Integrate Google Sheets for cloud collaboration
47. **T27.G7.02** - Compare predictions to actual outcomes
48. **T27.G7.02b** - Calculate moving averages for trend smoothing
49. **T27.G7.02c** - Automate chart updates with variables
50. **T27.G7.03** - Evaluate fairness metrics across user groups
51. **T27.G7.04** - Write findings reports for an audience

### Grade 8 (4 skills)
52. **T27.G8.01** - Determine if differences are statistically meaningful
53. **T27.G8.02** - Automate report generation
54. **T27.G8.03** - Integrate data analysis into AI prompt engineering
55. **T27.G8.04** - Publish data stories to a shared platform

---

## CreatiCode Feature Verification

### Available Blocks (Confirmed)
✓ **Widgets Category**: add button, add label, add textbox, add dropdown, add slider, add checkbox, when widget clicked, value of widget, set value for widget
✓ **Table Operations**: create table, add column, add to table, show table, row count, delete rows, sort table, export table, import file
✓ **Aggregations**: sum, average, median, minimum, maximum (all work on table columns)
✓ **Charts**: draw [bar/line/pie/percentage] chart using columns from table, draw chart using list
✓ **Advanced Table**: pivot, GROUP BY aggregation, filter by column value, copy table, append table
✓ **Data Import/Export**: Google Sheets integration (read/write), CSV export/import
✓ **Moving Average**: value from [simple/exponential] moving average window of list

### Missing/Unclear Features
⚠ **Mode aggregation**: No built-in mode block found (T27.G4.02e correctly notes students must build custom algorithm)
⚠ **Range filtering**: Delete rows only works for exact value matches, not ranges (skills correctly note need for loops)

---

## Issues Found (Prioritized)

### HIGH PRIORITY (Must Fix)

#### H1. Skill Ordering Violation: T27.G5.00b depends on T27.G5.01
**Issue**: T27.G5.00b (Respond to widget events) lists T27.G5.01 as a dependency, but G5.00b comes BEFORE G5.01 in the skill sequence. This violates the fundamental ordering rule.

**Fix**: Rename T27.G5.00b → T27.G5.01a (placing it immediately after T27.G5.01)

**Updated Skill**:
```
ID: T27.G5.01a
Skill: Respond to widget events in dashboards
Description: [same as current T27.G5.00b]
Dependencies:
* T27.G5.01: Build a simple interactive dashboard with filter widgets
* T27.G3.00: Add basic widgets to display information
```

#### H2. Circular/Complex Dependency: T27.G5.01b depends on T27.G4.04b, but logical flow is reversed
**Issue**: T27.G5.01b (GROUP BY) depends on T27.G4.04b (Sort tables), but GROUP BY is actually MORE fundamental than sorting. Students should learn grouping before needing sorting for median calculations.

**Fix**: Remove T27.G4.04b from T27.G5.01b dependencies. Sorting is useful but not prerequisite for GROUP BY.

**Updated Skill**:
```
ID: T27.G5.01b
Skill: Group data by category and compute statistics (GROUP BY)
Description: [same]
Dependencies:
* T27.G3.01: Compute totals and averages from data tables
* T09.G4.01: Read multiple inputs via ask blocks and apply them in conditions
```

#### H3. Missing Prerequisite: T27.G4.04b (Sort tables) needs earlier introduction
**Issue**: Sorting is introduced in G4.04b but is described as "essential for finding medians" - yet median skill (T27.G4.02c) comes BEFORE sorting skill. Also, sorting is fundamental enough to be introduced earlier.

**Fix**: Move sorting earlier (to G3) and split into conceptual + implementation skills.

**New Skills**:
```
ID: T27.G3.06
Skill: Understand sorting and data organization
Description: Students learn why sorting is useful for data analysis: finding top/bottom values, identifying patterns, and organizing data for comparison. They practice sorting small datasets manually (on paper or using drag-and-drop) to understand ascending vs descending order, and discuss when each is appropriate.
Dependencies:
* T27.G3.03: Use CreatiCode data tables to group and count

ID: T27.G3.07
Skill: Sort tables using built-in blocks
Description: Students use 'sort table [data v] by column [score] [large to small v]' to organize data programmatically, practicing both ascending and descending sorts and understanding how sorting reveals patterns like top performers, lowest values, or alphabetical order.
Dependencies:
* T27.G3.06: Understand sorting and data organization
Blocks: sort table by column
```

**Remove**: T27.G4.04b (redundant after moving to G3)

#### H4. Dependency Chain Issue: T27.G3.02 has incorrect dependency reference
**Issue**: T27.G3.02 depends on "T27.G3.01: Compute totals and averages from data tables" but the actual skill title uses "sum" not "totals".

**Fix**: Update dependency text for consistency (minor text fix, but affects validation)

#### H5. G4.02 Skills Sequence: b → c, e, d violates alphabetical sub-ordering
**Issue**: T27.G4.02b → T27.G4.02c → T27.G4.02e → T27.G4.02d is out of order. Should be b, c, d, e.

**Fix**: Renumber:
- T27.G4.02b (Understand median and mode) → keep
- T27.G4.02c (Calculate median) → keep
- T27.G4.02e (Calculate mode) → rename to T27.G4.02d
- T27.G4.02d (Filter table rows) → rename to T27.G4.02e

#### H6. Widget Skills Split Needed: T27.G3.00 is too basic
**Issue**: T27.G3.00 teaches "Add basic widgets" but doesn't cover setting widget values or reading widget values, which are needed for T27.G5.01 (dashboards). There's a gap.

**Fix**: Split T27.G3.00 into progression:

```
ID: T27.G3.00
Skill: Add and position widgets
Description: Students learn to add simple widgets (labels, buttons) using 'add button at x (X) y (Y) width (W) height (H) as [name]' and position them on stage. This foundational skill introduces the widget coordinate system and naming conventions.
Dependencies:
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T09.G3.01.04: Display variable value on stage using the variable monitor
Blocks: add button, add label

ID: T27.G3.00a
Skill: Set and read widget values
Description: Students use 'set value to [V] for widget [name v]' to update widget text/values and 'value of widget [name v]' to read user inputs. They practice updating labels with computed values and reading button states.
Dependencies:
* T27.G3.00: Add and position widgets
Blocks: set value for widget, value of widget
```

#### H7. Missing Skill: Data table copying/manipulation
**Issue**: Skills reference "copy matching rows to a new table" (T27.G4.02d, filtering) but no skill teaches table copying operations explicitly.

**Fix**: Add new skill in G4:

```
ID: T27.G4.02f
Skill: Copy and manipulate table data
Description: Students learn to create new tables and copy selected rows using loops: create empty table with same columns, iterate through source table rows, conditionally copy rows to new table. This is essential for non-destructive filtering and data transformation.
Dependencies:
* T27.G4.02e: Filter table rows by condition
* T10.G4.01: Use list length and item access in expressions
Blocks: create table, add column, add to table, get cell from table
```

#### H8. G5.00 and G5.00b Naming: Two "00" skills at same grade level
**Issue**: Both T27.G5.00 and T27.G5.00b exist, causing numbering confusion. After renaming G5.00b to G5.01a (per H1), G5.00 should be renumbered to fit sequence.

**Fix**:
- T27.G5.00 (Calculate percentages) should come BEFORE T27.G5.01 (dashboards) logically
- Keep as T27.G5.00 (it's appropriately placed as a prerequisite)
- After H1 fix, sequence becomes: G5.00 → G5.01 → G5.01a → G5.01b → G5.02...

---

### MEDIUM PRIORITY (Should Fix)

#### M1. Overlap: T27.G4.03 and T27.G4.03b are very similar
**Issue**: G4.03 (Check data quality) and G4.03b (Handle missing/invalid data) have significant conceptual overlap - both deal with data quality issues.

**Recommendation**: Consider merging or clarifying distinction. Current split works but could be clearer.

**Proposed Update**:
```
ID: T27.G4.03
Skill: Identify data quality issues
Description: Students inspect tables to find specific problems: missing entries (empty cells), duplicate rows (same values in all columns), invalid numbers (negative ages, impossible dates). They document issues found but don't fix them yet. They learn to distinguish between different types of problems and prioritize which are most critical.
Dependencies: [same]

ID: T27.G4.03b
Skill: Implement data cleaning strategies
Description: Students decide how to handle each type of data quality issue and implement their chosen strategy: skip rows with missing values (using filtering), replace missing numbers with averages (using aggregation + cell updates), or flag invalid entries for manual review (adding a status column). They document their cleaning decisions and justify their choices.
Dependencies:
* T27.G4.03: Identify data quality issues
* T27.G4.02f: Copy and manipulate table data
```

#### M2. Skill Split Needed: T27.G7.02b is too complex
**Issue**: T27.G7.02b teaches BOTH "extract table column to list" AND "calculate moving averages" - two distinct operations.

**Fix**: Split into two skills:

```
ID: T27.G7.02b
Skill: Convert between tables and lists
Description: Students extract table columns into lists using loops (copying each row's value) and populate table columns from lists. They learn when to use lists vs tables: lists are required for moving averages and certain mathematical operations, while tables are better for structured multi-column data.
Dependencies:
* T27.G6.03: Identify trends and patterns in time-series data
* T10.G4.01: Use list length and item access in expressions
Blocks: add to list, item # of list, get cell from table

ID: T27.G7.02c (renumbered from old G7.02b content)
Skill: Calculate moving averages for trend smoothing
Description: Students use 'value from [simple v] moving average window [7] of list [daily_scores v]' to calculate rolling averages that reveal underlying trends by reducing noise in time-series data. They compare raw vs smoothed charts to interpret patterns more clearly and choose appropriate window sizes for different data frequencies.
Dependencies:
* T27.G7.02b: Convert between tables and lists
Blocks: value from moving average window of list

[Renumber old T27.G7.02c → T27.G7.02d]
```

#### M3. Description Clarity: Multiple skills mention "blocks" that aren't in Blocks field
**Issue**: Several skills reference specific block names in descriptions but don't list them in the Blocks field.

**Fix**: Add Blocks field to these skills:
- T27.G3.00: add button, add label
- T27.G3.01b: add column, add to table, show table
- T27.G3.01: aggregation blocks (sum, average)
- T27.G3.01c: minimum, maximum
- T27.G3.03: row count of table, delete rows with column
- T27.G3.04: draw chart using columns from table
- T27.G4.02c: median aggregation
- T27.G4.02e: (no blocks - custom algorithm, correct as is)
- T27.G4.04b: sort table by column
- T27.G5.00: draw percentage chart
- T27.G5.01b: GROUP BY aggregation (set table to aggregation by column)
- T27.G6.01c: (no new blocks - uses conditionals)
- T27.G6.01b: row # in column, item at row column of table
- T27.G6.02b: pivot table
- T27.G6.03b: export table, import file
- T27.G7.01b: read from google sheet, write into google sheet

#### M4. Inconsistent Terminology: "totals" vs "sum"
**Issue**: T27.G3.01 title says "sum and average" but T27.G3.02 dependency says "totals and averages"

**Fix**: Standardize to "sum" (matches CreatiCode block naming)

#### M5. Missing Cross-Reference: T27.G7.01b (Google Sheets) should mention T27.G6.03b (CSV)
**Issue**: T27.G7.01b (Google Sheets integration) lists T27.G6.03b (CSV export/import) as dependency, but description doesn't explain progression from CSV → cloud.

**Fix**: Update T27.G7.01b description:

```
Description: Students learn cloud-based data collaboration by connecting CreatiCode to Google Sheets. Building on their CSV export/import experience (T27.G6.03b), they now use real-time cloud integration: 'read from google sheet: url [URL] sheet name [Sheet1] range [A1:D10] into table [data v]' to import shared data and 'write into google sheet: url [URL] sheet name [Sheet1] start cell [A1] from table [results v]' to publish findings. This enables collaborative workflows where multiple users can access the same living dataset, unlike static CSV files.
```

#### M6. Skill Gap: Pie charts mentioned but not explicitly taught
**Issue**: T27.G3.05 mentions "percentage charts" and T27.G5.00 references them, but pie charts (a common data viz type) are mentioned in CreatiCode blocks but not explicitly taught as a skill.

**Recommendation**: Update T27.G3.05 to explicitly include pie charts:

```
ID: T27.G3.05
Skill: Choose appropriate chart types for data
Description: Students learn when to use different chart types based on their data and questions: bar charts for comparing categories, line charts for showing change over time, pie charts for showing parts of a whole (composition), and percentage charts for comparing proportions across groups. They practice selecting the right chart type and explaining their choice, understanding that the same data can tell different stories depending on visualization choice.
Dependencies: [same]
Blocks: draw [bar/line/pie/percentage] chart
```

#### M7. Content Appropriateness: K-2 skills are appropriately unplugged
**Issue**: None - this is a positive finding. K-2 skills correctly focus on physical/unplugged activities (sorting objects, picture charts, manipulatives) rather than coding. G3 is the appropriate transition point to CreatiCode tools.

**Recommendation**: Maintain current approach. Add note in curriculum guidance about K-2 being unplugged.

#### M8. Statistical Concepts: Median requires sorting prerequisite
**Issue**: T27.G4.02c (Calculate median) notes "median requires sorted data" but doesn't depend on sorting skill.

**Fix**: After implementing H3 (moving sort to G3), update T27.G4.02c:

```
Dependencies:
* T27.G4.02b: Understand median and mode concepts
* T27.G3.07: Sort tables using built-in blocks
```

#### M9. Advanced Feature Timing: Pivot tables (G6.02b) might be too early
**Issue**: Pivot tables are a complex concept introduced in G6. Students might not have sufficient multi-dimensional thinking skills yet.

**Recommendation**: Monitor difficulty. Consider adding scaffolding skill before pivot:

```
ID: T27.G6.02a
Skill: Understand multi-dimensional grouping
Description: Students practice thinking about data grouped by TWO categories simultaneously using physical manipulatives or drawings. For example, sorting blocks by both color AND size, or analyzing class data by both grade AND gender. They create two-way tables on paper showing how counts change across both dimensions before using CreatiCode's pivot blocks.
Dependencies:
* T27.G5.01b: Group data by category and compute statistics (GROUP BY)
```

#### M10. Dashboard Progression: Multiple dashboard skills could be better scaffolded
**Issue**: T27.G5.01 (simple dashboard), T27.G7.01 (multi-chart dashboard) jump significantly in complexity.

**Recommendation**: Add intermediate skill in G6:

```
ID: T27.G6.05
Skill: Create dashboards with multiple visualizations
Description: Students build dashboards containing 2-3 different chart types (bar + line, or pie + table) displaying related data. Unlike G7.01's linked filters, these charts are independent but thematically connected. They learn to arrange charts effectively on stage and add titles/labels for clarity.
Dependencies:
* T27.G5.04: Present findings using slides or mini reports
* T27.G6.02: Compare two groups using data
Blocks: draw chart (multiple types)
```

#### M11. AI Integration: T27.G8.03 mentions XO but no prior AI skills in T27
**Issue**: T27.G8.03 references "XO (CreatiCode's AI assistant)" but students haven't used AI for data analysis before this point.

**Recommendation**: Either add G7 skill introducing AI for data insights, or update G8.03 to be more explicit about first AI usage:

```
Description: Students learn to augment their data analysis with AI assistance. They extract key statistics from their analysis (averages, trends, outliers), construct structured prompts that include these metrics (e.g., "Given average score=75, median=72, and 20% drop-off at level 3, suggest game improvements"), send to XO (CreatiCode's AI assistant), and critically evaluate whether the AI's recommendations align with their data evidence. This introduces AI as a reasoning partner while maintaining human judgment as primary.
```

#### M12. Export/Import Skills: Should mention file formats explicitly
**Issue**: T27.G6.03b (Export/import CSV) and T27.G7.01b (Google Sheets) don't clarify file format compatibility.

**Fix**: Update T27.G6.03b:

```
Description: Students learn to exchange data beyond CreatiCode using CSV (Comma-Separated Values) format, a universal spreadsheet format readable by Excel, Google Sheets, and other tools. They use 'export table [data v] as [analysis_results]' to save analysis results as downloadable CSV files for sharing, and 'import file into table [imported v]' to load external data from CSV files. This enables real-world data exchange, collaboration, and importing datasets from other sources like government data portals or scientific studies.
```

---

### LOW PRIORITY (Optional Improvements)

#### L1. Naming Convention: .01b, .02b, .00a creates confusion
**Issue**: Sub-skill naming uses letters inconsistently (some b's are sub-skills of non-existent "a" versions)

**Recommendation**: Maintain current system but document convention:
- .01, .02, .03 = main progression
- .01a, .01b, .01c = variations/extensions of .01
- .00 = foundational prerequisites introduced before main sequence

#### L2. Block Field: Not all skills have Blocks field populated
**Issue**: Blocks field is missing from many skills, making it hard to map to CreatiCode features.

**Fix**: See M3 for comprehensive list. This is lower priority than content issues but important for curriculum implementation.

#### L3. Grade Distribution: G6 has 9 skills (most), G8 has 4 skills (least)
**Issue**: Uneven distribution might indicate pacing issues.

**Analysis**:
- G3: 9 skills (intro to coding + tables, appropriate)
- G4: 9 skills (statistics + filtering, appropriate)
- G5: 8 skills (dashboards + advanced analysis, good)
- G6: 9 skills (complex queries + multi-table, dense but manageable)
- G7: 6 skills (automation + advanced viz, appropriate)
- G8: 4 skills (statistics + AI + publishing, could add 1-2 more)

**Recommendation**: Consider adding 1-2 G8 skills in advanced topics:
- Regression analysis basics
- A/B testing statistical comparison
- Data ethics and bias detection

#### L4. Cross-Topic Dependencies: Verify all T26 dependencies are appropriate
**Issue**: T27 skills depend on T26 (Data Collection) skills - need to verify alignment.

**Analysis of T26 dependencies**:
- T26.G3.04: Separate raw data from summary data (used in T27.G4.01, G5.01, G5.03, G5.04, G7.02, G7.03, G7.04)
- T26.G4.04: Plan a one-week observation schedule (used in T27.G6.01, G6.02, G6.04)
- T26.G5.04: Separate raw data from summary data (used in T27.G7.01, G7.02, G7.03, G7.04)
- T26.G6.01: Map stakeholder questions to data requirements (used in T27.G8.01, G8.02, G8.03, G8.04)

**Finding**: Dependencies are logical and appropriate. T26 focuses on collection, T27 focuses on analysis - clean separation.

#### L5. Terminology: "Storytelling" in topic name but limited narrative skills
**Issue**: Topic is "Data Analysis & Storytelling" but only a few skills explicitly teach storytelling (G1.03, G4.04, G6.04, G7.04).

**Recommendation**: Either:
1. Strengthen narrative skills in existing descriptions, OR
2. Add explicit "data storytelling" skills in G6-G8

Suggested new skill:
```
ID: T27.G7.05
Skill: Structure data narratives with story arcs
Description: Students learn to structure data presentations using narrative techniques: Setup (context and question), Challenge (what problem the data reveals), Resolution (insights and recommendations). They practice writing compelling data stories that engage audiences emotionally while maintaining analytical rigor, using the "So what?" test to ensure every chart has a clear takeaway.
Dependencies:
* T27.G7.04: Write findings reports for an audience
```

#### L6. Assessment: No explicit skills about evaluating visualizations
**Issue**: Students learn to CREATE charts but not critically EVALUATE them for misleading elements.

**Recommendation**: Add G6 or G7 skill:

```
ID: T27.G6.06
Skill: Identify misleading visualizations
Description: Students analyze example charts for common misleading techniques: truncated y-axes (making small differences look large), cherry-picked date ranges, inappropriate chart types, missing context or scales. They learn to spot these issues in others' work and avoid them in their own visualizations, developing critical data literacy.
Dependencies:
* T27.G5.02: Correlate two variables visually
* T27.G6.03: Identify trends and patterns in time-series data
```

---

## Recommended Changes Summary

### Immediate Changes (HIGH Priority)
1. **Rename T27.G5.00b → T27.G5.01a** (ordering fix)
2. **Remove T27.G4.04b dependency from T27.G5.01b** (circular dependency fix)
3. **Add T27.G3.06 and T27.G3.07** (move sorting to G3, remove T27.G4.04b)
4. **Renumber T27.G4.02d and T27.G4.02e** (alphabetical order)
5. **Split T27.G3.00 → T27.G3.00 + T27.G3.00a** (widget values)
6. **Add T27.G4.02f** (table copying)
7. **Update all dependency references** (consistency)

### Secondary Changes (MEDIUM Priority)
8. **Clarify T27.G4.03 and T27.G4.03b** (data quality distinction)
9. **Split T27.G7.02b** (table/list conversion separate from moving averages)
10. **Add Blocks fields** (M3 list - 15+ skills)
11. **Standardize terminology** (sum not totals)
12. **Update descriptions** (Google Sheets, pie charts, AI integration)

### Optional Enhancements (LOW Priority)
13. **Add G8 advanced skills** (regression, A/B testing, ethics)
14. **Add storytelling skill G7.05**
15. **Add critical evaluation skill G6.06**
16. **Add intermediate dashboard skill G6.05**

---

## CreatiCode Feature Recommendations

### Features That Work Well
✓ Table operations are comprehensive
✓ Chart variety is good (bar, line, pie, percentage)
✓ Aggregation blocks match statistical needs
✓ Google Sheets integration enables real workflows
✓ Widget system supports dashboard building

### Potential Enhancements for CreatiCode
1. **Add mode aggregation block** - Currently students must build custom algorithm (good for learning, but inefficient for analysis)
2. **Add range filtering block** - "delete rows where column [X] > [value]" would simplify common operation
3. **Add chart templates** - Pre-configured chart styles for common use cases
4. **Add table validation blocks** - "check column [X] for missing values" → returns count
5. **Add data profiling blocks** - "profile table [X]" → generates summary statistics for all columns

---

## X-2 Rule Compliance Check

Checking if all skills have prerequisites no more than 2 grades before:

### Violations Found: NONE

All T27 internal dependencies follow X-2 rule:
- GK skills have no dependencies (appropriate)
- G1 skills depend on GK (1 grade back)
- G2 skills depend on G1 (1 grade back)
- G3 skills depend on G2 and G1 (1-2 grades back)
- G4 skills depend on G3 (1 grade back)
- G5 skills depend on G4 and G3 (1-2 grades back)
- G6 skills depend on G5 and G4 (1-2 grades back)
- G7 skills depend on G6 and G5 (1-2 grades back)
- G8 skills depend on G7 and G6 (1-2 grades back)

Cross-topic dependencies (T01, T06-T10, T26) are not evaluated here as they belong to other topics.

---

## Forward References Check

Checking if any skill references a skill that comes AFTER it:

### Violations Found: 1

**T27.G5.00b → T27.G5.01** (FIXED in H1 above by renaming to G5.01a)

All other dependencies point backward correctly.

---

## Grade Appropriateness Check

### K-2: Picture-based activities ✓
- All K-2 skills correctly use unplugged, manipulative-based, or picture-based activities
- No coding required until G3
- Appropriate cognitive level

### G3+: Block coding ✓
- G3 introduces CreatiCode widgets and tables
- Progression from simple (display) to complex (analysis) is logical
- All skills use block-based coding (no text coding)

---

## Duplicate/Overlap Analysis

### Significant Overlaps:
1. **T27.G4.03 + T27.G4.03b** (data quality) - MEDIUM issue, addressed in M1
2. **T27.G3.00 gaps** (widgets) - HIGH issue, addressed in H6
3. **T27.G7.02b** (two concepts) - MEDIUM issue, addressed in M2

### Minor Overlaps (acceptable):
- Multiple skills mention "comparison" but in different contexts (groups, variables, sources)
- Multiple skills mention "filters" but progress from simple → complex
- Multiple skills mention "charts" but teach different aspects (types, creation, interpretation)

---

## Skills Needing Breakdown

Based on complexity analysis:

### Already Well-Broken:
- T27.G4.02 series (b, c, d, e) breaks down statistics appropriately
- T27.G6.01 series (a, b, c, d) breaks down filtering/lookup appropriately
- T27.G7.02 series (a, b, c) breaks down prediction analysis appropriately

### Need Additional Breakdown:
1. **T27.G3.00** (HIGH - addressed in H6)
2. **T27.G7.02b** (MEDIUM - addressed in M2)
3. **T27.G6.02b** (MEDIUM - consider adding M9 prerequisite)

---

## Missing Skills Identified

1. **T27.G3.00a** - Set and read widget values (H6)
2. **T27.G3.06** - Understand sorting concepts (H3)
3. **T27.G3.07** - Sort tables programmatically (H3)
4. **T27.G4.02f** - Copy and manipulate table data (H7)
5. **T27.G6.02a** - Multi-dimensional grouping concepts (M9 - optional)
6. **T27.G6.05** - Multi-chart dashboards (M10 - optional)
7. **T27.G6.06** - Identify misleading visualizations (L6 - optional)
8. **T27.G7.05** - Structure data narratives (L5 - optional)

---

## Implementation Priority

### Phase 1 (Immediate - Required for Correctness)
1. Fix skill ordering issues (H1, H5)
2. Fix dependency issues (H2, H4)
3. Move sorting to G3 (H3)
4. Split widget skills (H6)
5. Add table copying skill (H7)
6. Fix numbering issues (H8)

### Phase 2 (Short-term - Improve Quality)
1. Clarify data quality skills (M1, M8)
2. Split complex skills (M2)
3. Add Blocks fields (M3)
4. Update descriptions (M4, M5, M6, M11, M12)

### Phase 3 (Long-term - Enhancements)
1. Add optional scaffolding skills (M9, M10)
2. Add advanced G8 skills (L3)
3. Add storytelling/evaluation skills (L5, L6)
4. Consider CreatiCode feature requests (see Feature Recommendations)

---

## Final Recommendations

### Strengths of Current T27:
✓ Comprehensive coverage from unplugged (K) to advanced AI integration (G8)
✓ Strong alignment with CreatiCode features (blocks accurately referenced)
✓ Good progression from simple → complex
✓ X-2 rule compliance (after fixes)
✓ Appropriate K-2 unplugged approach
✓ Clear connection to T26 (Data Collection)

### Critical Fixes Needed:
1. Skill ordering and dependencies (H1-H8)
2. Add missing foundational skills (widgets, sorting, table copying)

### After Fixes, T27 Will Be:
- Logically ordered
- Properly scaffolded
- Feature-accurate
- Developmentally appropriate
- Ready for curriculum implementation

---

**Report Generated**: 2025-11-24
**Total Skills Analyzed**: 54
**Issues Found**: 26 (8 HIGH, 12 MEDIUM, 6 LOW)
**New Skills Recommended**: 8 (3 required, 5 optional)
**Skills to Remove**: 1 (T27.G4.04b - redundant after move to G3)
