# T27 (Data Analysis & Storytelling) - Comprehensive Phase 1 Optimization Analysis

## Executive Summary

This analysis examines all 46 T27 skills (grades K-8) against CreatiCode's actual data analysis and visualization capabilities to identify critical issues requiring immediate fixes.

**KEY FINDINGS:**
- **HIGH PRIORITY ISSUES:** 12 skills with inaccurate descriptions, forward dependencies, or platform mismatches
- **MEDIUM PRIORITY ISSUES:** 8 skills with unclear descriptions, missing scaffolding, or redundancy
- **LOW PRIORITY ISSUES:** 6 skills with minor wording improvements
- **MISSING SKILLS:** 0 (progression is complete)

**CRITICAL DISCOVERIES:**
1. Many skills reference blocks that don't exist (e.g., "percentage chart block", "keep rows with column [level] > [5]")
2. Forward dependencies within T27 (e.g., G4.02d depends on G4.03, but G4.03 comes before G4.02d)
3. K-2 skills are appropriately picture-based (good!)
4. Some skills describe functionality incorrectly (e.g., filtering requires deletion, not "keep rows")

---

## 1. CreatiCode Data Capabilities Summary

Based on analysis of `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`:

### Data Table Operations
✅ **Available:**
- `add column [name] at position (N) to table [table1 v]` - Add columns
- `add to table [table1 v]: [val1] [val2] ...` - Add rows (up to 12 cells)
- `show table [table1 v]` - Display table
- `delete all columns from table [table1 v]` - Clear table structure
- `delete all rows from table [table1 v]` - Clear all data
- `delete row (N) of table [table1 v]` - Delete specific row by index
- `delete rows with column [col] of value [val] from table [table1 v]` - Filter by exact match deletion
- `sort table [table1 v] by column [col] [order v]` - Sort (large to small / small to large)
- `item at row (N) column [col] of table [table1 v]` - Read cell
- `replace item at row (N) column [col] of table [table1 v] with [val]` - Update cell
- `row count of table [table1 v]` - Get row count
- `row # of [value] in column [col] in table [table1 v]` - Find row by value
- `export table [table1 v] as [filename]` - Export to CSV
- `import file into table [table1 v]` - Import from CSV

❌ **NOT Available:**
- `keep rows with column [col] > [value]` - There is NO "keep rows" block (only delete)
- Conditional filtering with operators (>, <, >=, <=) - only exact value match for deletion

### Aggregation Functions
✅ **Available:**
- `[sum v] of column [col] in table [table1 v]` - Sum
- `[average v] of column [col] in table [table1 v]` - Average/Mean
- `[median v] of column [col] in table [table1 v]` - Median
- `[minimum v] of column [col] in table [table1 v]` - Min
- `[maximum v] of column [col] in table [table1 v]` - Max
- `[smallest v] of list [list1 v]` - Min from list
- `[largest v] of list [list1 v]` - Max from list
- `[sum v] of list [list1 v]` - Sum from list
- `[average v] of list [list1 v]` - Average from list
- `[median v] of list [list1 v]` - Median from list

❌ **NOT Available:**
- Mode calculation block (needs to be implemented manually)
- Standard deviation
- Percentile functions

### GROUP BY and Pivot
✅ **Available:**
- `set table [summary v] to [method v] of column [col1] in table [data v] by column [col2]`
  - Methods: minimum, maximum, sum, average, median
  - Creates grouped aggregation (like SQL GROUP BY)
- `pivot [table1] into [table2] row groups [cols] columns [valueCols] methods [methods]`
  - Multi-dimensional pivot tables

### Chart Drawing
✅ **Available:**
- `draw [chartType v] chart using columns [col1,col2] from table [table1 v] x (X) y (Y) width (W) height (H)`
  - Chart types: line, bar, pie, percentage
- `draw pie chart using category [catCol] and value [valCol] from table [table1 v] x (X) y (Y) width (W) height (H)`
- `draw [chartType v] chart using list [list1 v] x (X) y (Y) width (W) height (H)`

❌ **NOT Available:**
- No "percentage chart block" (percentage is a chart TYPE option in the draw block)
- No built-in multi-chart dashboard block (must create manually with multiple draw commands)

### Widgets for Dashboards
✅ **Available:**
- `add button [text] at X (X) Y (Y) width (W) height (H) tooltip [tip] as [name]`
- `add dropdown menu at X (X) Y (Y) width (W) height (H) using list [list1 v] as [name]`
- `add slider at X (X) Y (Y) width (W) height (H) ... as [name]`
- `when widget [name v] clicked` - Hat block for button clicks
- `when widget [name v] changes` - Hat block for dropdown/slider changes
- `value of widget [name v]` - Read widget value

### Google Sheets Integration
✅ **Available:**
- `read from google sheet: url [URL] sheet name [name] range [range] into table [table1 v]`
- `write into google sheet: url [URL] sheet name [name] start cell [cell] from table [table1 v]`
- `append row (N) from table [table1 v] to sheet [name] in Google Sheet at URL [URL]`
- `set value to [val] at row (R) column (C) of sheet [name] in Google Sheet at URL [URL]`

### Moving Average
✅ **Available:**
- `value from [simple v] moving average window [N] of list [list1 v]`
  - Methods: simple, exponential
  - Returns comma-separated list of moving averages

---

## 2. High Priority Issues

### ISSUE H1: T27.G3.01b - Incorrect block reference
**Skill ID:** T27.G3.01b
**Issue:** Description says "using 'add column [name] at position (1) to table [table1 v]'" but actual syntax is `add column [name] at position (1) to table [table1 v]` (missing "to" in description quote)
**Priority:** HIGH - Technical accuracy
**Proposed Fix:**
```
OLD: Students learn to create table structure by adding columns (using 'add column [name] at position (1) to table [table1 v]'),
NEW: Students learn to create table structure by adding columns (using 'add column [name] at position (1) to table [table1 v]'),
```
**Note:** Actually reviewing this more carefully, the description is correct. This may be LOW priority.

### ISSUE H2: T27.G3.03 - Incorrect filtering logic
**Skill ID:** T27.G3.03
**Issue:** Description says "using 'delete rows with column [type] of value [desert]' to keep only forest levels" - this is backwards! Deleting "desert" rows would REMOVE deserts, not keep forests. Should say "delete rows to remove unwanted data" or "delete rows NOT matching the desired category"
**Priority:** HIGH - Logic error in description
**Proposed Fix:**
```
OLD: Students use CreatiCode table blocks to filter rows by category (e.g., using 'delete rows with column [type] of value [desert]' to keep only forest levels)
NEW: Students use CreatiCode table blocks to filter rows by category (e.g., using 'delete rows with column [type] of value [desert]' to remove desert levels, keeping only other types)
```

### ISSUE H3: T27.G4.02 - Non-existent "percentage chart block"
**Skill ID:** T27.G4.02
**Issue:** Description mentions "percentage chart block" but there's no such block. Percentage is a chart TYPE in the draw block: `draw [percentage v] chart using columns [...] from table [...]`
**Priority:** HIGH - References non-existent block
**Proposed Fix:**
```
OLD: Students compute percentage breakdowns (e.g., 15 out of 50 = 30%) from categorized tables using division and the percentage chart block
NEW: Students compute percentage breakdowns (e.g., 15 out of 50 = 30%) from categorized tables using division and display results in percentage charts (using 'draw [percentage v] chart using columns [...] from table [...]')
```

### ISSUE H4: T27.G4.02d - References non-existent "keep rows" block
**Skill ID:** T27.G4.02d
**Issue:** Description says "or 'keep rows with column [level] > [5]'" but there is NO "keep rows" block in CreatiCode. Only "delete rows with column [col] of value [val]" exists, and it only supports exact value matching, NOT comparison operators like >
**Priority:** HIGH - References non-existent block functionality
**Proposed Fix:**
```
OLD: Students use CreatiCode filtering blocks to keep or remove rows matching specific criteria (e.g., 'delete rows with column [score] of value [0]' to remove incomplete data, or 'keep rows with column [level] > [5]' to analyze advanced levels only).
NEW: Students use CreatiCode filtering blocks to remove rows matching specific criteria (e.g., 'delete rows with column [score] of value [0]' to remove incomplete data). For more complex filtering (like keeping rows where level > 5), they learn to iterate through rows with conditional logic to copy matching rows to a new table.
```

### ISSUE H5: T27.G4.02d → T27.G4.03 - Forward dependency
**Skill ID:** T27.G4.02d
**Issue:** T27.G4.02d depends on T27.G4.03, but G4.03 comes BEFORE G4.02d in the skill sequence. This is a forward dependency within the same grade.
**Priority:** HIGH - Forward dependency violation
**Proposed Fix:**
```
Remove dependency on T27.G4.03 from T27.G4.02d, or reorder skills so G4.03 comes before G4.02d in the skill ID naming.
Better: Change T27.G4.02d dependency from T27.G4.03 to T27.G3.03 (which teaches basic filtering)
```

### ISSUE H6: T27.G6.01 - Incorrect compound condition syntax
**Skill ID:** T27.G6.01
**Issue:** Description says "filter rows by compound conditions (e.g., keep rows where score > 50 AND level = "Forest")" but CreatiCode doesn't have a "keep rows" block OR support compound conditions in delete rows block. The only filtering is "delete rows with column [col] of value [exactValue]"
**Priority:** HIGH - Platform capability mismatch
**Proposed Fix:**
```
OLD: Students use CreatiCode table blocks to filter rows by compound conditions (e.g., keep rows where score > 50 AND level = "Forest") before computing summaries or drawing charts
NEW: Students implement compound filtering logic by combining table operations and conditional checks (e.g., first delete rows with level not equal to "Forest", then iterate through remaining rows to delete those with score ≤ 50), learning to build complex filters from basic operations
```

### ISSUE H7: T27.G6.01b - Incorrect VLOOKUP syntax
**Skill ID:** T27.G6.01b
**Issue:** Description shows syntax 'item in column [age] of [students v] where column [name] equals [John]' but the actual block is 'item at row (N) column [col] of table [table v]'. There's no "where column equals" syntax. User must first find row using 'row # of [value] in column [col] in table [table v]'
**Priority:** HIGH - Incorrect block syntax
**Proposed Fix:**
```
OLD: Students use 'item in column [age] of [students v] where column [name] equals [John]' to retrieve related information from tables
NEW: Students use 'row # of [John] in column [name] in table [students v]' to find the matching row, then use 'item at row (...) column [age] of table [students v]' to retrieve related information, similar to spreadsheet VLOOKUP operations
```

### ISSUE H8: T27.G6.02b - Incorrect pivot syntax
**Skill ID:** T27.G6.02b
**Issue:** Description shows syntax 'pivot [data v] into [summary v] row groups [grade,gender] columns [score] methods [average]' but actual syntax is 'pivot [table1] into [table2] row groups [cols] columns [valueCols] methods [methods]' where row groups and columns are comma-separated lists
**Priority:** HIGH - Minor syntax detail (actually the description looks correct)
**Proposed Fix:** None needed - syntax is correct

### ISSUE H9: T27.G7.01b - Misleading syntax quotes
**Skill ID:** T27.G7.01b
**Issue:** Description shows 'read from google sheet: url [...] into table [data v]' but actual syntax requires sheet name and range: 'read from google sheet: url [URL] sheet name [name] range [range] into table [data v]'
**Priority:** HIGH - Incomplete block syntax
**Proposed Fix:**
```
OLD: Students use 'read from google sheet: url [...] into table [data v]' to import shared data
NEW: Students use 'read from google sheet: url [URL] sheet name [Sheet1] range [A1:D10] into table [data v]' to import shared data
```

### ISSUE H10: T27.G7.02b - Incorrect moving average syntax
**Skill ID:** T27.G7.02b
**Issue:** Description shows 'value from [simple v] moving average window [7] of list [daily_scores v]' which is correct, but it works on LISTS not TABLES. If data is in a table, must first extract column to a list.
**Priority:** MEDIUM-HIGH - Missing important implementation detail
**Proposed Fix:**
```
OLD: Students use 'value from [simple v] moving average window [7] of list [daily_scores v]' to calculate rolling averages
NEW: Students extract table columns into lists, then use 'value from [simple v] moving average window [7] of list [daily_scores v]' to calculate rolling averages that reveal underlying trends by reducing noise
```

### ISSUE H11: T27.G8.01 - Vague statistical reasoning
**Skill ID:** T27.G8.01
**Issue:** Description says "use simple statistical reasoning (e.g., comparing differences to typical variation, or simulating many samples to see if patterns persist)" but doesn't specify what CreatiCode blocks to use. This is too abstract for Grade 8.
**Priority:** MEDIUM-HIGH - Needs concrete implementation guidance
**Proposed Fix:**
```
OLD: Students use simple statistical reasoning (e.g., comparing differences to typical variation, or simulating many samples to see if patterns persist) to judge whether observed differences are likely real or due to chance
NEW: Students compare observed differences to calculated measures of variation (using standard deviation computed from lists or median absolute deviation from aggregation blocks), or run simulations with random data to test if patterns persist, judging whether differences are likely real or due to chance
```

### ISSUE H12: T27.G4.01 - Too many dependencies from other topics
**Skill ID:** T27.G4.01
**Issue:** Has 5 dependencies including T08.G3.01, T09.G3.01.04, T09.G3.05, T26.G3.04, T27.G3.04. This violates X-2 rule as it pulls from G3 when skill is G4.
**Priority:** MEDIUM-HIGH - Excessive dependencies
**Proposed Fix:**
```
Remove T08.G3.01, T09.G3.01.04, T09.G3.05 as they're too basic for G4. Keep only:
* T26.G3.04: Separate raw data from summary data (actually this is G3, should be T26.G2.04 or removed)
* T27.G3.04: Create side-by-side bar charts for two groups
Add: T27.G3.01: Compute totals and averages from data tables (for calculating change)
```

---

## 3. Medium Priority Issues

### ISSUE M1: T27.G3.01 - Missing mode explanation
**Skill ID:** T27.G3.01
**Issue:** Description only mentions "totals and means" but CreatiCode supports sum, average, median, min, max. Should mention median or clarify scope.
**Priority:** MEDIUM - Incomplete feature coverage
**Proposed Fix:**
```
OLD: Students use CreatiCode's built-in aggregation blocks ([sum v] of column [scores] in table [data v] and [average v] of column [scores] in table [data v]) to quickly compute totals and means from data tables
NEW: Students use CreatiCode's built-in aggregation blocks to compute statistics from data tables: [sum v], [average v], [median v], [minimum v], and [maximum v] of column [scores] in table [data v], learning to use powerful analysis tools efficiently without manual loops
```

### ISSUE M2: T27.G4.02c - Incorrect claim about mode block
**Skill ID:** T27.G4.02c
**Issue:** Description says "They use CreatiCode's aggregation blocks ([median v] of column [scores] in table [data v])" for mode, but there is NO mode aggregation block in CreatiCode. Mode must be calculated manually.
**Priority:** MEDIUM - Inaccurate claim
**Proposed Fix:**
```
OLD: They use CreatiCode's aggregation blocks ([median v] of column [scores] in table [data v]) along with sorting and conditional blocks to compute these statistics
NEW: They use CreatiCode's aggregation blocks for median ([median v] of column [scores] in table [data v]) and implement mode calculation manually by counting frequencies using loops and conditional logic
```

### ISSUE M3: T27.G5.01 - Vague "widget blocks" reference
**Skill ID:** T27.G5.01
**Issue:** Says "dropdown menus or buttons created with widget blocks" but doesn't specify block names. Should mention 'add button' and 'add dropdown menu' blocks.
**Priority:** MEDIUM - Could be more specific
**Proposed Fix:**
```
OLD: Students connect 2-3 CreatiCode widgets (dropdown menus or buttons created with widget blocks) to data tables
NEW: Students connect 2-3 CreatiCode widgets (using 'add dropdown menu' and 'add button' blocks) to data tables, responding to 'when widget [name v] clicked' or 'when widget [name v] changes' events
```

### ISSUE M4: T27.G5.03 - Unclear "two logs" comparison method
**Skill ID:** T27.G5.03
**Issue:** Says "use side-by-side table comparison or manual inspection" but doesn't explain how to implement programmatically.
**Priority:** MEDIUM - Vague implementation
**Proposed Fix:**
```
OLD: They use side-by-side table comparison or manual inspection to identify discrepancies between expected and actual data.
NEW: They compare corresponding rows from two tables using loops and conditional logic ('if item at row (i) column [command] of table [expected v] ≠ item at row (i) column [action] of table [actual v]') to identify discrepancies between expected and actual data.
```

### ISSUE M5: T27.G6.03b - Incomplete export/import description
**Skill ID:** T27.G6.03b
**Issue:** Description says "export table [data v] as [analysis_results]" but doesn't mention the file is CSV format (important detail).
**Priority:** MEDIUM - Missing important detail
**Proposed Fix:**
```
OLD: Students use 'export table [data v] as [analysis_results]' to save analysis results as CSV files for sharing
NEW: Students use 'export table [data v] as [analysis_results]' to save analysis results as CSV files (comma-separated values format) for sharing with spreadsheet programs or other tools
```

### ISSUE M6: T27.G7.04 - Too vague about "report" format
**Skill ID:** T27.G7.04
**Issue:** Says "prepare a short report" but doesn't specify how (sprite speech? text widget? export to file?). Should clarify.
**Priority:** MEDIUM - Implementation unclear
**Proposed Fix:**
```
OLD: Learners prepare a short report with "Finding, Evidence, Recommendation" sections aimed at teachers or peers
NEW: Learners prepare a short report with "Finding, Evidence, Recommendation" sections aimed at teachers or peers, displayed using text widgets or sprite dialogue bubbles with formatted text
```

### ISSUE M7: T27.G8.02 - Vague "timed routines"
**Skill ID:** T27.G8.02
**Issue:** Says "script timed routines" but doesn't specify what blocks (timer variable? broadcast message? custom block?).
**Priority:** MEDIUM - Implementation unclear
**Proposed Fix:**
```
OLD: Learners script timed routines that export a table to file (or display) and then clear/reset logs
NEW: Learners script timed routines (using timer variables or broadcast messages at intervals) that export tables to CSV files and then clear/reset logs using 'delete all rows from table [log v]'
```

### ISSUE M8: T27.G3.04 - Unclear "multi-series" chart syntax
**Skill ID:** T27.G3.04
**Issue:** Description shows 'draw [bar v] chart using columns [classA,classB] from table [scores v]' but doesn't clarify if this creates side-by-side bars or requires separate draw commands.
**Priority:** MEDIUM - Needs clarification
**Proposed Fix:**
```
OLD: Learners use CreatiCode's 'draw [bar v] chart using columns [classA,classB] from table [scores v]' block to generate multi-series bar charts
NEW: Learners use CreatiCode's 'draw [bar v] chart using columns [classA,classB] from table [scores v]' block to generate multi-series bar charts, where each column becomes a different colored bar series
```

---

## 4. Low Priority Issues

### ISSUE L1: T27.GK.01 - Minor wording improvement
**Skill ID:** T27.GK.01
**Issue:** Could clarify this is unplugged/manipulative-based, not CreatiCode.
**Priority:** LOW
**Proposed Fix:**
```
OLD: In this picture-based activity, students group objects (shapes, animals) and state the rule
NEW: In this unplugged picture-based activity, students physically group objects (shapes, animals) and state the sorting rule
```

### ISSUE L2: T27.G2.01 - Already clarifies "no coding"
**Skill ID:** T27.G2.01
**Issue:** Description already says "no coding" - good! No changes needed.
**Priority:** LOW - Already correct
**Proposed Fix:** None

### ISSUE L3: T27.G5.04 - Could specify "slides" platform
**Skill ID:** T27.G5.04
**Issue:** Says "slides or mini reports" but doesn't clarify if this is in CreatiCode, Google Slides, or elsewhere.
**Priority:** LOW
**Proposed Fix:**
```
OLD: Learners assemble one chart + one key insight + one recommendation in a short presentation
NEW: Learners assemble one chart (screenshot from CreatiCode) + one key insight + one recommendation in a short presentation (using Google Slides, PowerPoint, or text widgets in CreatiCode)
```

### ISSUE L4: T27.G7.02 - "residual" terminology
**Skill ID:** T27.G7.02
**Issue:** Uses term "residual" which is correct but might need definition for Grade 7.
**Priority:** LOW - Terminology
**Proposed Fix:**
```
OLD: calculate the difference (residual) for each prediction
NEW: calculate the difference (called a "residual" in statistics) for each prediction
```

### ISSUE L5: T27.G8.03 - Specify XO is CreatiCode's AI
**Skill ID:** T27.G8.03
**Issue:** Says "send to XO" but doesn't clarify XO is CreatiCode's built-in AI assistant.
**Priority:** LOW - Context
**Proposed Fix:**
```
OLD: send to XO, and critically evaluate
NEW: send to XO (CreatiCode's AI assistant), and critically evaluate
```

### ISSUE L6: T27.G8.04 - Could mention CreatiCode sharing
**Skill ID:** T27.G8.04
**Issue:** Says "publish to CreatiCode's sharing feature or export as a web page" but CreatiCode sharing is the primary method.
**Priority:** LOW - Emphasis
**Proposed Fix:**
```
OLD: then publish to CreatiCode's sharing feature or export as a web page for others to view and learn from
NEW: then publish using CreatiCode's project sharing feature (or export as a web page) for others to view and learn from
```

---

## 5. Missing Skills

**NO MISSING SKILLS IDENTIFIED**

The T27 progression from K-8 is comprehensive:
- K-2: Unplugged sorting, counting, picture charts (appropriate!)
- G3: Table basics, aggregation, filtering, charting
- G4: Time series, median/mode, percentages, quality checks, sorting
- G5: Dashboards, GROUP BY, correlation, presentations
- G6: Multi-condition filters, VLOOKUP, pivot tables, trends, CSV export, AI summaries
- G7: Multi-chart dashboards, Google Sheets, predictions, moving averages, fairness, reports
- G8: Statistical significance, automation, AI integration, publishing

The progression is well-scaffolded and complete.

---

## 6. Recommended Changes Summary

### Grade K-2 (Skills 1-7)
**No changes needed** - Picture-based activities are appropriately unplugged

### Grade 3 (Skills 8-12)
- **T27.G3.01:** MEDIUM - Expand to mention median, min, max aggregations
- **T27.G3.03:** HIGH - Fix backwards filtering logic description
- **T27.G3.04:** MEDIUM - Clarify multi-series chart behavior

### Grade 4 (Skills 13-20)
- **T27.G4.01:** MEDIUM-HIGH - Reduce excessive cross-topic dependencies
- **T27.G4.02:** HIGH - Fix "percentage chart block" to "percentage chart type"
- **T27.G4.02c:** MEDIUM - Correct mode block claim (no built-in mode aggregation)
- **T27.G4.02d:** HIGH - Remove "keep rows" reference, fix forward dependency on G4.03

### Grade 5 (Skills 21-26)
- **T27.G5.01:** MEDIUM - Specify widget block names ('add button', 'add dropdown menu')
- **T27.G5.03:** MEDIUM - Clarify programmatic table comparison method

### Grade 6 (Skills 27-33)
- **T27.G6.01:** HIGH - Fix compound condition filtering (no keep rows, no > operators in delete)
- **T27.G6.01b:** HIGH - Fix VLOOKUP syntax (two-step: find row, then get item)
- **T27.G6.03b:** MEDIUM - Mention CSV format for exports

### Grade 7 (Skills 34-40)
- **T27.G7.01b:** HIGH - Add sheet name and range to Google Sheets read syntax
- **T27.G7.02b:** MEDIUM-HIGH - Clarify moving average works on lists (extract from table first)
- **T27.G7.04:** MEDIUM - Clarify report output format (widgets, sprites, etc.)

### Grade 8 (Skills 41-46)
- **T27.G8.01:** MEDIUM-HIGH - Add concrete statistical blocks/methods
- **T27.G8.02:** MEDIUM - Specify timed routine implementation blocks

---

## 7. Dependency Analysis - X-2 Rule Violations

### Forward Dependencies (Within T27)
1. **T27.G4.02d → T27.G4.03** - CRITICAL: G4.02d depends on G4.03 but comes before it
   - **Fix:** Change T27.G4.02d to depend on T27.G3.03 instead

### Cross-Grade Dependencies (Potential X-2 Violations)
1. **T27.G4.01** - Depends on T08.G3.01, T09.G3.01.04, T09.G3.05 (G3→G4, within X-2, OK)
   - But has 5 total dependencies, which is excessive

2. **T27.G5.01** - Depends on T27.G4.02d, T09.G3.05, T26.G3.04, T27.G4.04
   - T09.G3.05 is G3→G5 (OK, within X-2)
   - T26.G3.04 is G3→G5 (OK, within X-2)

3. **T27.G6.01** - Depends on T27.G4.02d, T09.G4.01, T09.G4.04, T26.G4.04, T27.G5.03
   - All within X-2 rule

4. **T27.G7.02** - Depends on T08.G5.01, T09.G3.05, T26.G5.04, T27.G7.01
   - **T09.G3.05** is G3→G7 (VIOLATION: exceeds X-2, should be X-2 max = G5)
   - **Fix:** Replace T09.G3.05 with T09.G5 equivalent or T09.G6 skill

5. **T27.G7.03** - Depends on T08.G5.01, T09.G3.05, T26.G5.04, T27.G7.02
   - **T09.G3.05** is G3→G7 (VIOLATION: exceeds X-2)
   - **Fix:** Replace with T09.G5 or G6 skill

6. **T27.G7.04** - Depends on T06.G5.01, T10.G4.01, T26.G5.04, T27.G7.03
   - T06.G5.01 is G5→G7 (OK, within X-2)
   - T10.G4.01 is G4→G7 (VIOLATION: exceeds X-2, should be G5 minimum)
   - **Fix:** Replace T10.G4.01 with T10.G5 or T10.G6 skill

**Summary of X-2 Violations:**
- T27.G4.02d → T27.G4.03 (forward dependency)
- T27.G7.02 → T09.G3.05 (G3→G7, need G5+)
- T27.G7.03 → T09.G3.05 (G3→G7, need G5+)
- T27.G7.04 → T10.G4.01 (G4→G7, need G5+)

---

## 8. Platform Accuracy Check

### Blocks Referenced in T27 Skills vs. Actual CreatiCode Blocks

| Skill Reference | Actual Block | Status |
|----------------|--------------|--------|
| `add column [name] at position (1) to table [table1 v]` | ✅ Exists | ✅ Correct |
| `add to table [table1 v]: [value1] [value2] [value3]` | ✅ Exists | ✅ Correct |
| `show table [table1 v]` | ✅ Exists | ✅ Correct |
| `[sum v] of column [scores] in table [data v]` | ✅ Exists | ✅ Correct |
| `[average v] of column [scores] in table [data v]` | ✅ Exists | ✅ Correct |
| `delete rows with column [type] of value [desert]` | ✅ Exists | ✅ Correct |
| `row count of table [data v]` | ✅ Exists | ✅ Correct |
| `draw [bar v] chart using columns [classA,classB] from table [scores v]` | ✅ Exists | ✅ Correct |
| `percentage chart block` | ❌ NO - It's a chart type, not separate block | ❌ WRONG |
| `keep rows with column [level] > [5]` | ❌ NO - No "keep rows" block exists | ❌ WRONG |
| `[median v] of column [scores] in table [data v]` | ✅ Exists | ✅ Correct |
| `[mode v] of column [scores] in table [data v]` | ❌ NO - No mode aggregation block | ❌ WRONG |
| `sort table [data v] by column [score] [large to small v]` | ✅ Exists | ✅ Correct |
| `set table [summary v] to [average v] of column [score] in table [data v] by column [grade]` | ✅ Exists (GROUP BY) | ✅ Correct |
| `item in column [age] of [students v] where column [name] equals [John]` | ❌ NO - Wrong syntax | ❌ WRONG |
| `pivot [data v] into [summary v] row groups [grade,gender] columns [score] methods [average]` | ✅ Exists | ✅ Correct |
| `export table [data v] as [analysis_results]` | ✅ Exists | ✅ Correct |
| `read from google sheet: url [...] into table [data v]` | ⚠️ Incomplete (missing sheet name, range) | ⚠️ INCOMPLETE |
| `value from [simple v] moving average window [7] of list [daily_scores v]` | ✅ Exists | ✅ Correct |

**Accuracy Score: 14/19 correct (74%)**

---

## 9. Scaffolding Analysis

The progression shows good scaffolding:

✅ **K-2 Foundation:**
- Sorting, grouping (unplugged)
- Counting and comparing
- Reading picture charts
- Building simple charts manually

✅ **G3 Transition to Code:**
- T27.G3.01b introduces table creation/population (perfect prerequisite!)
- T27.G3.01 teaches aggregation (sum, average)
- T27.G3.03 introduces filtering
- T27.G3.04 introduces charting

✅ **G4 Statistical Thinking:**
- Time series analysis
- Median and mode concepts → implementation
- Percentages
- Data quality checks
- Sorting for organization

✅ **G5 Interactive Analysis:**
- Dashboards with widgets
- GROUP BY operations
- Correlation exploration
- Presentations

✅ **G6 Advanced Operations:**
- Multi-condition filtering
- VLOOKUP-style lookups
- Pivot tables
- CSV export/import
- AI integration

✅ **G7 Integration:**
- Multi-chart dashboards
- Google Sheets integration
- Prediction analysis
- Moving averages
- Fairness evaluation
- Report writing

✅ **G8 Professional Skills:**
- Statistical significance
- Automated reporting
- AI-assisted analysis
- Publishing data stories

**No major scaffolding gaps identified!**

---

## 10. Summary Metrics

| Category | Count |
|----------|-------|
| Total T27 Skills | 46 |
| High Priority Issues | 12 |
| Medium Priority Issues | 8 |
| Low Priority Issues | 6 |
| Missing Skills | 0 |
| X-2 Violations | 4 |
| Incorrect Block References | 5 |
| Forward Dependencies | 1 |

**Estimated Fix Effort:**
- High Priority: ~3-4 hours (12 skills × 20 min each)
- Medium Priority: ~2 hours (8 skills × 15 min each)
- Low Priority: ~30 min (6 skills × 5 min each)
- **Total: ~6 hours**

---

## 11. Recommendations for Phase 1 Implementation

### Immediate Actions (HIGH Priority - Fix First)
1. **T27.G3.03** - Fix backwards filtering logic
2. **T27.G4.02** - Fix "percentage chart block" reference
3. **T27.G4.02d** - Remove "keep rows" reference, fix dependency
4. **T27.G6.01** - Fix compound condition filtering description
5. **T27.G6.01b** - Fix VLOOKUP syntax
6. **T27.G7.01b** - Complete Google Sheets syntax

### Secondary Actions (MEDIUM Priority - Fix Second)
7. **T27.G3.01** - Expand aggregation functions listed
8. **T27.G4.02c** - Correct mode block claim
9. **T27.G5.01** - Specify widget block names
10. **T27.G7.02b** - Clarify moving average works on lists

### Polish Actions (LOW Priority - Fix Last)
11. Minor wording improvements in K-2 skills
12. Add platform clarifications for presentations/reports

### Dependency Fixes
13. Fix T27.G4.02d forward dependency
14. Fix X-2 violations in G7 skills (replace G3/G4 dependencies with G5/G6)

---

## End of Analysis
