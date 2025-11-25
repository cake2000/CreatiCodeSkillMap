# T27 Actionable Recommendations

## Executive Summary

**Analyzed:** 54 T27 skills (GK-G8)
**Issues Found:** 44 skills affected (81%)
**Critical Issues:** 27 skills (50%)
**Estimated Fix Time:** 11-16 hours

**Priority Actions:**
1. Renumber 39 skills to eliminate letter suffix chaos (4 hours)
2. Fix 1 circular dependency + 2 invalid references (1 hour)
3. Split 5 overly broad skills (3-4 hours)
4. Write 8 new foundational skills (3-4 hours)
5. Simplify excessive dependencies (2-3 hours)

---

## PRIORITY 1: CRITICAL FIXES (Must do immediately)

### 1.1 Systematic Renumbering (39 skills)

**Problem:** Letter suffixes (b, c, d, e) scattered illogically across grades, creating confusion and violating sequential logic.

**Action Items:**

#### Grade 3 Renumbering (7 skills)
```python
# Automated script needed - example logic:
renumber_map = {
    "T27.G3.01b": "T27.G3.01",  # Create/populate tables
    "T27.G3.01":  "T27.G3.02",  # Compute sum/average
    "T27.G3.01c": "T27.G3.03",  # Find min/max
    "T27.G3.02":  "T27.G3.04",  # Build comparison statements
    "T27.G3.03":  "T27.G3.05",  # Group and count
    "T27.G3.04":  "T27.G3.06",  # Side-by-side bar charts
    "T27.G3.05":  "T27.G3.07",  # Choose chart types
}

# Also update ALL dependencies that reference these IDs
```

**Files to modify:**
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (lines 24990-25057)
- All skills that reference G3 skills in dependencies

**Validation:**
- [ ] Verify no duplicate IDs after renumbering
- [ ] Confirm sequential ordering (G3.01, G3.02, G3.03...)
- [ ] Update all dependency references
- [ ] Check for any broken cross-references

#### Grade 4 Renumbering (8 skills)
```python
renumber_map = {
    "T27.G4.02d": "T27.G4.02",  # Filter rows by condition
    "T27.G4.02b": "T27.G4.03",  # Understand median/mode
    "T27.G4.02c": "T27.G4.04",  # Calculate median
    "T27.G4.02e": "T27.G4.05",  # Calculate mode
    "T27.G4.03":  "T27.G4.06",  # Check data quality
    "T27.G4.03b": "T27.G4.07",  # Handle missing data
    "T27.G4.04":  "T27.G4.08",  # Narrative captions
    "T27.G4.04b": "T27.G4.09",  # Sort tables
}
```

**Critical Note:** G4 has NO base G4.02 skill, yet has 02b, 02c, 02d, 02e suffixes! This is the most chaotic grade.

#### Grade 5 Renumbering (7 skills)
```python
renumber_map = {
    "T27.G5.00":  "T27.G5.01",  # Calculate percentages
    "T27.G5.00b": "T27.G5.02",  # Widget events
    "T27.G5.01":  "T27.G5.03",  # Interactive dashboard
    "T27.G5.01b": "T27.G5.04",  # GROUP BY
    "T27.G5.02":  "T27.G5.05",  # Correlate two variables
    "T27.G5.03":  "T27.G5.06",  # Compare two sources
    "T27.G5.04":  "T27.G5.07",  # Present findings
}
```

**Special Note:** The "00" notation in G5.00/G5.00b suggests uncertainty about placement. This renumbering clarifies their foundational role.

#### Grade 6 Renumbering (8 skills)
```python
renumber_map = {
    "T27.G6.01c": "T27.G6.02",  # OR conditions
    "T27.G6.01b": "T27.G6.03",  # VLOOKUP
    "T27.G6.01d": "T27.G6.04",  # Combine tables
    "T27.G6.02":  "T27.G6.05",  # Compare two groups
    "T27.G6.02b": "T27.G6.06",  # Pivot tables
    "T27.G6.03":  "T27.G6.07",  # Trends in time-series
    "T27.G6.03b": "T27.G6.08",  # Export/import CSV
    "T27.G6.04":  "T27.G6.09",  # Structured summaries
}
```

**Critical Issue:** G6.01c appears BEFORE G6.01b, violating alphabetical order expectations.

#### Grade 7 Renumbering (6 skills)
```python
renumber_map = {
    "T27.G7.01b": "T27.G7.02",  # Google Sheets
    "T27.G7.02":  "T27.G7.03",  # Compare predictions
    "T27.G7.02b": "T27.G7.04",  # Moving averages
    "T27.G7.02c": "T27.G7.05",  # Automate chart updates
    "T27.G7.03":  "T27.G7.06",  # Fairness metrics
    "T27.G7.04":  "T27.G7.07",  # Write findings reports
}
```

**Note:** Grade 8 needs NO renumbering (all sequential).

---

### 1.2 Fix Circular Dependency

**Problem:** T27.G5.00b (Widget events) depends on T27.G5.01 (Interactive dashboard), but dashboards NEED widget events to function. This creates impossible prerequisite.

**Current (WRONG):**
```
T27.G5.00b depends on → T27.G5.01
(Widget events need dashboards? No!)
```

**Should be:**
```
T27.G5.01 depends on → T27.G5.00b
(Dashboards need widget events ✓)
```

**Action:**
1. **Remove** T27.G5.01 from T27.G5.00b's dependency list
2. **Add** T27.G5.00b to T27.G5.01's dependency list (if not already present)
3. Verify logical flow: Widgets → Widget Events → Interactive Dashboard

**Files to modify:**
- T27.G5.00b (after renumbering: T27.G5.02) dependencies section
- T27.G5.01 (after renumbering: T27.G5.03) dependencies section

---

### 1.3 Remove Invalid Skill References

**Problem:** T26.G3.04 is marked as [Unknown skill] but referenced by T27.G4.03 and T27.G4.04.

**Investigation needed:**
1. Search for T26.G3.04 in allskills.md - does it exist?
2. If it exists, why is it marked "Unknown"?
3. If it doesn't exist, what SHOULD these dependencies reference?

**Possible T26 skills in G3:**
- T26.G3.01: Run a simple picture poll
- T26.G3.02: Count raised hands for a class vote
- T26.G3.03: Share two-sentence results
- T26.G3.04: ??? (Need to verify)
- T26.G3.04.01: Export list values to a CSV text file (This exists!)

**Likely correct reference:** T26.G3.04.01 (Export CSV) - makes sense for data quality checks.

**Action:**
1. Verify T26.G3.04 vs T26.G3.04.01 in allskills.md
2. Update T27.G4.03 dependencies to correct T26 skill
3. Update T27.G4.04 dependencies to correct T26 skill
4. If T26.G3.04 truly doesn't exist, remove these dependencies entirely

**Files to modify:**
- T27.G4.03 (after renumbering: T27.G4.06) dependencies
- T27.G4.04 (after renumbering: T27.G4.08) dependencies

---

### 1.4 Correct Block Reference Errors (6 skills)

#### Error 1: T27.G3.01c - Incorrect aggregation terms
**Current:** "Find minimum and maximum values using [minimum v] and [maximum v]"
**Correct:** "Find smallest and largest values using [smallest v] and [largest v]"

**Rationale:** CreatiCode block list specifies "smallest/largest", not "min/max"

**Action:**
```
File: skillsv4/allskills.md, T27.G3.01c (after renumbering: T27.G3.03)
Find: "minimum and maximum"
Replace: "smallest and largest"
Find: "[minimum v] and [maximum v]"
Replace: "[smallest v] and [largest v]"
```

#### Error 2: T27.G5.01b - Missing "computed" keyword
**Current:** "set table [summary v] to [average v] of column..."
**Correct:** "set table [summary v] to computed [average v] of column..."

**Rationale:** Block list shows "set table to computed" for GROUP BY operations

**Action:**
```
File: skillsv4/allskills.md, T27.G5.01b (after renumbering: T27.G5.04)
Find: "set table [summary v] to [average v]"
Replace: "set table [summary v] to computed [average v]"
```

#### Error 3: T27.G6.01b - Incorrect lookup terminology
**Current:** "row # of [John] in column [name]..."
**Correct:** "row index with column [name] of value [John]..."

**Rationale:** Block list shows "row index with condition" as the actual block name

**Action:**
```
File: skillsv4/allskills.md, T27.G6.01b (after renumbering: T27.G6.03)
Find: "row # of [John] in column [name] in table [students v]"
Replace: "row index with column [name] of value [John] in table [students v]"
```

#### Errors 4-6: Unverified syntax (need validation)
- **T27.G6.02b** (Pivot tables) - Verify pivot block signature
- **T27.G7.01b** (Google Sheets) - Verify read/write syntax
- **T27.G7.02b** (Moving averages) - Verify dropdown options

**Action:** Consult actual CreatiCode documentation or blockdes file before implementing.

---

## PRIORITY 2: CONTENT IMPROVEMENTS (High priority)

### 2.1 Split Overly Broad Skills (5 skills)

#### Split 1: T27.G3.01b → Two focused skills

**Current (too broad):**
"Create and populate data tables in CreatiCode"
- Add columns
- Populate rows
- Display tables
- Verify contents

**Recommended split:**

**NEW T27.G3.01: Create table structure and add columns**
```
Skill: Create table structure and add columns
Description: Students learn to define table structure by adding named columns
using 'add column [name] at position (1) to table [table1 v]'. They plan what
data each column will hold (names, scores, dates) and create empty table
structures ready for data entry. This teaches schema design before data
population.

Dependencies:
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T09.G3.01.04: Display variable value on stage using the variable monitor
```

**NEW T27.G3.02: Populate tables with data rows**
```
Skill: Populate tables with data rows
Description: Students add data rows to existing tables using 'add to table
[table1 v]: [value1] [value2] [value3]'. They learn to match data order with
column order, use loops for multiple entries, and display tables with 'show
table [table1 v]' to verify data entry. This separates data entry from
structure creation.

Dependencies:
* T27.G3.01: Create table structure and add columns
* T07.G3.01: Use a counted repeat loop (for multiple rows)
```

**OLD T27.G3.01 becomes T27.G3.03: Compute sum/average**
(Keep current content, update dependencies to T27.G3.02)

---

#### Split 2: T27.G4.02d → Two focused skills

**Current (too broad):**
"Filter table rows by condition"
- Built-in exact match filtering
- Range-based filtering with loops
- Two completely different techniques!

**Recommended split:**

**NEW T27.G4.02: Filter tables using exact match conditions**
```
Skill: Filter tables using exact match conditions
Description: Students use built-in filtering for exact matches: 'delete rows
with column [score] of value [0]' removes all rows where score equals zero.
They learn when exact match filtering is appropriate (removing invalid entries,
isolating specific categories) and practice with simple equality conditions.

Dependencies:
* T27.G3.02: Populate tables with data rows
* T08.G3.01: Use a simple if in a script
```

**NEW T27.G4.XX: Filter tables using range conditions**
```
Skill: Filter tables using range conditions
Description: For range-based filtering (score > 50, age < 18), students iterate
through rows using loops with conditional logic, copying matching rows to a new
table. They learn to check each row against criteria using 'if (item at row (i)
column [score] > (50))' and build filtered result tables. This extends beyond
built-in blocks to custom filtering logic.

Dependencies:
* T27.G4.02: Filter tables using exact match conditions
* T08.G3.01: Use a simple if in a script
* T07.G3.01: Use a counted repeat loop
```

---

#### Split 3: T27.G6.02 → Two focused skills

**Current (too broad):**
"Compare two groups using data"
- Split data into groups
- Compute averages per group
- Calculate differences
- Interpret magnitude

**Recommended approach:**
Actually, this skill should be REWRITTEN to depend on T27.G5.01b (GROUP BY), not split. The grouping operation already exists!

**REVISED T27.G6.05: Compare statistics between two groups**
```
Skill: Compare statistics between two groups
Description: Students use GROUP BY to split data into groups (e.g., 'set table
to computed [average v] of column [score] by column [version]' creates averages
for Version A vs Version B). They then compare group statistics by calculating
differences and determining if the difference is large relative to typical
variation in the data.

Dependencies:
* T27.G5.04: Group data by category and compute statistics (GROUP BY)
* T27.G6.01: Filter tables using AND conditions
* T09.G4.04: Trace code with variables to predict outcomes
```

---

#### Split 4: T27.G7.02b → Two focused skills

**Current (too broad):**
"Calculate moving averages for trend smoothing"
- Extract table column to list
- Calculate moving average
- Compare raw vs smoothed charts

**Recommended split:**

**NEW T27.G7.XX: Convert table columns to lists**
```
Skill: Convert table columns to lists
Description: Students extract table columns into lists using loops: iterate
through each row with 'repeat (row count of table [data v])' and append each
value to a list with 'add (item at row (i) column [score]) to [scores v]'. This
prepares data for list-based operations like moving averages, sorting, or
analysis that requires list format.

Dependencies:
* T27.G3.02: Populate tables with data rows
* T10.G5.01: Use list length and item access in expressions
* T07.G5.01: Use loops with variables
```

**NEW T27.G7.04: Calculate moving averages for trend smoothing**
```
Skill: Calculate moving averages for trend smoothing
Description: Students apply moving average calculations to lists using 'value
from [simple v] moving average window [7] of list [daily_scores v]'. They
compare raw data charts (with noise) versus smoothed charts (with trends) to
identify underlying patterns. They learn when simple vs exponential moving
averages are appropriate.

Dependencies:
* T27.G7.XX: Convert table columns to lists
* T27.G6.07: Identify trends and patterns in time-series data
* T10.G5.01: Use list length and item access in expressions
```

---

#### Split 5: T27.G5.01 - Already partially split, needs dependency fix

**Current state:** T27.G5.00b teaches widget events, but G5.01 doesn't depend on it!

**Action:** Don't split further, just fix dependencies (covered in 1.2 above).

---

### 2.2 Write 8 New Foundational Skills

#### New Skill 1: G3 - Verify table contents and structure
```
ID: T27.G3.XX (assign after renumbering)
Topic: T27 – Data Analysis & Storytelling
Skill: Verify table contents and structure
Description: Students learn to inspect tables to verify correct data entry.
They use 'show table [table1 v]' to display the entire table, 'row count of
table [data v]' to check size, and 'item at row (1) column [name] of table
[data v]' to check specific values. This debugging skill helps students catch
errors before analysis and builds confidence in their data structures.

Dependencies:
* T27.G3.02: Populate tables with data rows (NEW after split)
```

**Placement:** Between G3.02 (populate) and G3.03 (compute statistics)

---

#### New Skill 2: G3 - Create simple charts from lists
```
ID: T27.G3.XX
Topic: T27 – Data Analysis & Storytelling
Skill: Create simple charts from lists
Description: Students create bar charts directly from lists using 'draw [bar v]
chart using list [scores v]'. This is simpler than table-based charts because
it requires no column selection or table structure. Students learn that lists
are appropriate for simple, single-column data visualization before advancing
to multi-column table charts.

Dependencies:
* T10.G3.01: Create lists and add/remove items
* T27.G2.01: Create bar charts with axes labels (unplugged)
```

**Placement:** Early G3, before table-based charts (current G3.04/G3.06)

---

#### New Skill 3: G4 - Delete specific table rows
```
ID: T27.G4.XX
Topic: T27 – Data Analysis & Storytelling
Skill: Delete specific table rows by index
Description: Students remove individual rows from tables using 'delete row (i)
from table [data v]' where i is a specific row number. They learn when to use
index-based deletion (removing known bad entries) versus condition-based
deletion (removing all rows matching criteria). This enables precise data
cleaning.

Dependencies:
* T27.G3.02: Populate tables with data rows
* T09.G3.01.04: Display variable value on stage (to show row indices)
```

**Placement:** G4, alongside filtering skills

---

#### New Skill 4: G4 - Update table values and rows
```
ID: T27.G4.XX
Topic: T27 – Data Analysis & Storytelling
Skill: Update existing table values
Description: Students modify table data using 'replace item at row (i) column
[name] to [newValue] in table [data v]' for individual cells, or 'replace row
(i) in table [data v] to [val1] [val2] [val3]' for entire rows. They learn when
to update (correcting errors, applying transformations) versus when to delete
and re-add. This teaches data correction workflows.

Dependencies:
* T27.G3.02: Populate tables with data rows
* T09.G4.01: Read multiple inputs via ask blocks (to get correction values)
```

**Placement:** G4, with other data management skills

---

#### New Skill 5: G4 - Compute statistics from lists
```
ID: T27.G4.XX
Topic: T27 – Data Analysis & Storytelling
Skill: Compute statistics from lists
Description: Students calculate basic statistics on lists using [sum v],
[average v], [smallest v], [largest v], and [median v] of list [scores v].
They learn that list aggregation is simpler than table aggregation for
single-variable data, making it appropriate for simple datasets before advancing
to multi-column table analysis.

Dependencies:
* T10.G3.01: Create lists and add/remove items
* T09.G3.01.04: Display variable value on stage
```

**Placement:** G4, before or alongside table aggregation skills
**Note:** This should actually come BEFORE table aggregation (G3.03) to maintain simple→complex progression. Consider moving to G3.

---

#### New Skill 6: G5 - Copy and backup tables
```
ID: T27.G5.XX
Topic: T27 – Data Analysis & Storytelling
Skill: Copy and backup tables for safe experimentation
Description: Students create table copies using 'copy table [original v] to
[backup v]' before performing destructive operations like filtering or deletion.
They learn workflows for safe data experimentation: copy → modify → compare →
decide whether to keep changes. This teaches professional data safety practices.

Dependencies:
* T27.G3.02: Populate tables with data rows
* T27.G4.02: Filter tables using exact match conditions
```

**Placement:** Early G5, before complex transformations

---

#### New Skill 7: G6 - Combine AND/OR conditions in filters
```
ID: T27.G6.XX
Topic: T27 – Data Analysis & Storytelling
Skill: Combine AND/OR logic in complex filters
Description: Students build complex filters that mix AND/OR logic:
'(level = "Forest" AND score > 50) OR (level = "Desert" AND score > 75)'.
They learn to use nested conditionals to implement these compound conditions
and understand how parentheses affect logical evaluation order. This extends
beyond simple AND (all conditions true) or OR (any condition true) to realistic
database-style queries.

Dependencies:
* T27.G6.01: Filter tables using AND conditions
* T27.G6.02: Filter tables using OR conditions (renumbered)
* T08.G4.01: Use if-else blocks with compound conditions
```

**Placement:** G6, after teaching AND and OR separately

---

#### New Skill 8: G7 - Convert table columns to lists
(Already defined in Split 4 above - T27.G7.XX)

---

### 2.3 Rewrite Vague Descriptions (10 skills)

#### Vague 1: T27.GK.01 - "Sort objects by a rule and explain it"

**Current (vague):**
"In this unplugged picture-based activity, students physically group objects..."

**Problem:** No specific task format, unclear implementation.

**Improved description:**
```
Description: Students sort 6-10 picture cards into 2-3 labeled bins based on a
visible property (color, shape, or size). Using drag-and-drop (digital) or
physical cards, they place each card in the correct bin, then state their
sorting rule aloud: "I put all the red things together" or "I grouped by shape:
circles, squares, triangles." This builds explicit criteria thinking before data
analysis.

Implementation: Provide mixed cards (3 red circles, 2 blue squares, 3 red
squares, 2 blue circles) and 2 bins (RED, BLUE) or (CIRCLES, SQUARES). Students
choose which rule to apply, sort accordingly, and explain their choice. Validate
that all items in each bin match the stated rule.
```

---

#### Vague 2: T27.G2.03 - "Find values that look different from others"

**Current (vague):**
"Look different" is subjective, no concrete criteria.

**Improved description:**
```
Description: Students examine illustrated lists or bar charts where most values
cluster together with one clearly different value. Example: [3, 4, 3, 12]
displayed as bars showing three short bars (heights 3-4) and one tall bar
(height 12). They point out which value "doesn't fit the pattern" and explain:
"12 is much bigger than the others" or "12 is three times taller." This builds
visual outlier detection before formal statistical definitions.

Criteria for "different": The outlier should be at least 2x larger or smaller
than the cluster, making it visually obvious. Students don't calculate; they
use visual inspection and magnitude comparison language.

Implementation: Provide 4-6 values with one clear outlier. Students circle or
click the outlier and select explanation from options: "much bigger," "much
smaller," "doesn't match the pattern."
```

---

#### Vague 3: T27.G4.03 - "Check data quality before analysis"

**Current (vague):**
"Decide how to handle each" without decision framework.

**Improved description:**
```
Description: Students inspect tables for three specific quality issues, using
this decision framework:

**Issue 1: Missing entries (empty cells)**
- Strategy: If critical column (ID, name) is missing → Skip entire row
- Strategy: If optional column is missing → Mark as "N/A" or use average
- Check: Use conditional to detect empty strings or zero values

**Issue 2: Duplicate rows (identical values)**
- Strategy: Delete duplicates, keep first occurrence only
- Check: Compare each row to previous rows using nested loops

**Issue 3: Invalid values (negative age, score > 100)**
- Strategy: Flag for manual review, don't include in calculations
- Check: Use conditionals to test if values are outside valid ranges

Students document their decisions in a checklist: "Found 3 missing ages → used
average. Found 1 negative score → flagged for review." They implement their
chosen strategies using conditional blocks and filtering.

Implementation: Provide pre-seeded table with known issues. Students identify
each issue type, choose handling strategy, implement with code, and produce
cleaned table plus quality report.
```

---

#### Vague 4: T27.G5.01 - "Build a simple interactive dashboard"

**Current (vague):**
"Simple" is subjective, no specific scope.

**Improved description:**
```
Description: Students create a dashboard with exactly these components:
- **2-3 widgets:** 1 dropdown menu (filter selection) + 1 button (trigger update)
  + optional label (display results)
- **1 table:** Contains filterable data (e.g., game scores with level column)
- **1-2 charts:** Bar chart or line chart showing filtered data

**User interaction flow:**
1. User selects option from dropdown (e.g., "Forest" level)
2. User clicks "Update" button
3. Button event triggers filtering: keeps only rows matching dropdown value
4. Charts redraw using filtered table
5. Label displays summary (e.g., "Showing 15 Forest level scores")

**Complexity limits:** Max 3 widgets, max 1-2 simple filter conditions, max 2
charts. This ensures "simplicity" while teaching core dashboard concepts.

Implementation: Use 'when widget [updateButton v] clicked' to trigger, 'value
of widget [levelFilter v]' to read selection, filter table, then redraw charts
with 'draw [bar v] chart using columns [...] from table [filtered v]'.
```

---

#### Vague 5: T27.G8.01 - "Determine if differences are statistically meaningful"

**Current (vague):**
"Simple statistical reasoning" without concrete methods.

**Improved description:**
```
Description: Students use two grade-appropriate methods to judge if observed
differences are likely real or due to chance:

**Method 1: Compare difference to typical variation**
- Calculate typical variation: max - min within each group, or range/4 as estimate
- Compare difference between groups to typical variation
- If difference > typical variation → likely real
- If difference < typical variation → possibly chance
- Example: Group A averages 75 ± 5, Group B averages 77 ± 5. Difference (2)
  < variation (5), so likely chance.

**Method 2: Simple simulation (shuffle test)**
- Combine all data from both groups
- Randomly split into two new groups 20 times
- Count how often random splits show difference ≥ observed difference
- If rarely (< 2 out of 20) → observed difference likely real
- If often (> 10 out of 20) → observed difference possibly chance

Students document: "The [X]-point difference is [larger/smaller] than typical
variation ([Y]), suggesting it's [likely real / possibly chance]. Simulation
showed this large a difference in [Z] out of 20 random trials."

Implementation: Guide students through variation calculation OR provide
simulation template with shuffle and re-split logic. Students interpret results
rather than implementing complex statistics.
```

---

(Additional vague descriptions G1.01, G2.01, G3.02, G7.03 can be improved similarly with concrete examples, criteria, and implementation guidance.)

---

## PRIORITY 3: DEPENDENCY OPTIMIZATION (Medium priority)

### 3.1 Simplify Excessive Dependencies

#### Skill 1: T27.G4.01 - Analyze change over time (8 dependencies)

**Current dependencies:**
```
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G3.04.01: Export list values to a CSV text file
* T27.G3.04: Create side-by-side bar charts for two groups (after renumbering: G3.06)
```

**Analysis:**
- Pattern recognition (T04) - NOT essential for line graphs
- Loop identification (T07) - NOT essential, no loops in this skill
- Conditionals (T08) - NOT essential, no branching in this skill
- Variable display (T09.G3.01.04) - ESSENTIAL for showing data
- Variable tracing (T09.G3.05) - OPTIONAL, helpful but not required
- CSV export (T26) - ESSENTIAL for time-series data source
- Bar charts (T27.G3.06) - ESSENTIAL for chart foundation

**Simplified to 3 essential dependencies:**
```
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T26.G3.04.01: Export list values to a CSV text file
* T27.G3.06: Create side-by-side bar charts for two groups (renumbered from G3.04)
```

**Rationale:** Only keep dependencies directly used in the skill implementation.

---

#### Skill 2: T27.G4.03 - Check data quality (9 dependencies)

**Current dependencies:**
```
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G3.04: [Unknown skill]
* T27.G3.03: Use CreatiCode data tables to group and count (after renumbering: G3.05)
```

**Analysis:**
- Pattern recognition (T04) - NOT essential
- Event chains (T06.G2.01, G2.02) - NOT essential
- Green-flag script (T06.G3.01) - ESSENTIAL foundation
- Loop identification (T07) - NOT essential
- Variable tracing (T09) - OPTIONAL
- Unknown skill (T26) - REMOVE (invalid reference)
- Table operations (T27.G3.05) - ESSENTIAL

**Simplified to 3 essential dependencies:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T27.G3.05: Use CreatiCode data tables to group and count (renumbered from G3.03)
* T08.G3.01: Use a simple if in a script (for quality checks)
```

---

#### Skill 3: T27.G4.04 - Narrative captions (7 dependencies)

**Current dependencies:**
```
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G3.04: [Unknown skill]
* T27.G4.01: Analyze change over time using line graphs
```

**Simplified to 2 essential dependencies:**
```
* T27.G4.01: Analyze change over time using line graphs (need charts to caption)
* T09.G3.01.04: Display variable value on stage (for showing captions)
```

---

### 3.2 Add Missing Intra-Topic Dependencies

#### Missing Dep 1: T27.G3.04 (bar charts) should depend on T27.G3.01 (statistics)

**Rationale:** Students need to understand what they're visualizing before creating complex comparison charts.

**Action:** Add T27.G3.02 (after renumbering, was G3.01) to G3.06 dependencies (after renumbering, was G3.04).

---

#### Missing Dep 2: T27.G4.04b (sort tables) should depend on T27.G3.01b (create tables)

**Rationale:** Can't sort tables without knowing how to create them.

**Action:** Add T27.G3.02 (after renumbering, was G3.01b) to G4.09 dependencies (after renumbering, was G4.04b).

---

#### Missing Dep 3: T27.G5.02 (correlate variables) should depend on T27.G3.04 (multi-series charts)

**Rationale:** Correlation visualization uses side-by-side charts taught in G3.

**Action:** Add T27.G3.06 (after renumbering, was G3.04) to G5.05 dependencies (after renumbering, was G5.02).

---

#### Missing Dep 4: T27.G6.02 (compare groups) should depend on T27.G5.01b (GROUP BY)

**Rationale:** GROUP BY is the efficient way to compute statistics per group, which is what this skill does.

**Action:** Add T27.G5.04 (after renumbering, was G5.01b) to G6.05 dependencies (after renumbering, was G6.02).

---

#### Missing Dep 5: T27.G7.01 (multi-chart dashboards) should depend on T06.G5.01 (broadcasts)

**Rationale:** Dashboard synchronization uses broadcast messages explicitly mentioned in description.

**Action:** Add T06.G5.01 to G7.01 dependencies (verify not already present).

---

## VALIDATION CHECKLIST

Before marking T27 complete, verify:

### Structural Validation
- [ ] All 39 skills renumbered with no duplicates
- [ ] Sequential numbering (01, 02, 03...) with no gaps
- [ ] No remaining letter suffixes except legitimate sub-skills (like .04.01)
- [ ] All dependency references updated to new IDs

### Dependency Validation
- [ ] No circular dependencies (verify G5.02 ↔ G5.03 fixed)
- [ ] No invalid skill references (verify T26.G3.04 resolved)
- [ ] All X-2 rule compliant (no deps from >2 grades below)
- [ ] Excessive dependencies simplified (G4.01, G4.03, G4.04)
- [ ] Missing intra-topic dependencies added (5 additions)

### Content Validation
- [ ] 5 overly broad skills split appropriately
- [ ] 8 new foundational skills written with full specs
- [ ] 10 vague descriptions rewritten with concrete examples
- [ ] All block references verified against CreatiCode documentation
- [ ] All block syntax corrected (smallest/largest, computed, row index)

### Platform Alignment
- [ ] No scatter plots referenced (use bar/line charts instead)
- [ ] Aggregation uses built-in blocks (not manual loops)
- [ ] All referenced blocks actually exist in CreatiCode
- [ ] Google Sheets syntax verified
- [ ] Pivot table syntax verified
- [ ] Moving average syntax verified

### Documentation
- [ ] Comprehensive analysis document complete
- [ ] Quick reference guide complete
- [ ] Visual issue map complete
- [ ] Actionable recommendations complete (this document)
- [ ] Before/after comparison document created
- [ ] Stakeholder-ready summary created

---

## AUTOMATION OPPORTUNITIES

### Renumbering Script (Python)
```python
#!/usr/bin/env python3
"""
T27 Skills Renumbering Script
Systematically updates skill IDs and all dependencies
"""

import re
from pathlib import Path

# Renumbering maps for each grade
GRADE_3_MAP = {
    "T27.G3.01b": "T27.G3.01",
    "T27.G3.01": "T27.G3.02",
    "T27.G3.01c": "T27.G3.03",
    "T27.G3.02": "T27.G3.04",
    "T27.G3.03": "T27.G3.05",
    "T27.G3.04": "T27.G3.06",
    "T27.G3.05": "T27.G3.07",
}

GRADE_4_MAP = {
    "T27.G4.02d": "T27.G4.02",
    "T27.G4.02b": "T27.G4.03",
    "T27.G4.02c": "T27.G4.04",
    "T27.G4.02e": "T27.G4.05",
    "T27.G4.03": "T27.G4.06",
    "T27.G4.03b": "T27.G4.07",
    "T27.G4.04": "T27.G4.08",
    "T27.G4.04b": "T27.G4.09",
}

GRADE_5_MAP = {
    "T27.G5.00": "T27.G5.01",
    "T27.G5.00b": "T27.G5.02",
    "T27.G5.01": "T27.G5.03",
    "T27.G5.01b": "T27.G5.04",
    "T27.G5.02": "T27.G5.05",
    "T27.G5.03": "T27.G5.06",
    "T27.G5.04": "T27.G5.07",
}

GRADE_6_MAP = {
    "T27.G6.01c": "T27.G6.02",
    "T27.G6.01b": "T27.G6.03",
    "T27.G6.01d": "T27.G6.04",
    "T27.G6.02": "T27.G6.05",
    "T27.G6.02b": "T27.G6.06",
    "T27.G6.03": "T27.G6.07",
    "T27.G6.03b": "T27.G6.08",
    "T27.G6.04": "T27.G6.09",
}

GRADE_7_MAP = {
    "T27.G7.01b": "T27.G7.02",
    "T27.G7.02": "T27.G7.03",
    "T27.G7.02b": "T27.G7.04",
    "T27.G7.02c": "T27.G7.05",
    "T27.G7.03": "T27.G7.06",
    "T27.G7.04": "T27.G7.07",
}

# Combine all maps
ALL_MAPS = {**GRADE_3_MAP, **GRADE_4_MAP, **GRADE_5_MAP, **GRADE_6_MAP, **GRADE_7_MAP}

def renumber_skills(file_path: Path):
    """Renumber T27 skills in allskills.md"""
    content = file_path.read_text()

    # Sort by length (longest first) to avoid partial replacements
    sorted_old_ids = sorted(ALL_MAPS.keys(), key=len, reverse=True)

    for old_id in sorted_old_ids:
        new_id = ALL_MAPS[old_id]
        # Replace in ID lines
        content = re.sub(f"^ID: {re.escape(old_id)}$", f"ID: {new_id}", content, flags=re.MULTILINE)
        # Replace in dependency references
        content = re.sub(f"\\* {re.escape(old_id)}:", f"* {new_id}:", content)

    # Backup original
    backup_path = file_path.with_suffix('.md.backup_t27_renumber')
    file_path.rename(backup_path)

    # Write updated content
    file_path.write_text(content)
    print(f"✓ Renumbered {len(ALL_MAPS)} skills")
    print(f"✓ Backup saved to {backup_path}")

if __name__ == "__main__":
    allskills_path = Path("/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md")
    renumber_skills(allskills_path)
```

### Dependency Validator Script
```python
#!/usr/bin/env python3
"""
Validate T27 dependencies for X-2 rule compliance
"""

def extract_grade(skill_id: str) -> int:
    """Extract grade level from skill ID"""
    if ".GK." in skill_id:
        return 0
    match = re.search(r"\.G(\d+)\.", skill_id)
    return int(match.group(1)) if match else -1

def validate_x2_rule(skill_id: str, dependencies: list[str]) -> list[str]:
    """Check if dependencies violate X-2 rule"""
    skill_grade = extract_grade(skill_id)
    violations = []

    for dep in dependencies:
        dep_grade = extract_grade(dep)
        if skill_grade - dep_grade > 2:
            violations.append(f"{dep} is {skill_grade - dep_grade} grades below {skill_id}")

    return violations

# Run validation on all T27 skills
# ... (implementation left as exercise)
```

---

## TIMELINE ESTIMATE

### Week 1: Critical Fixes (Priority 1)
- **Day 1-2:** Write and test renumbering script
- **Day 2-3:** Execute renumbering on allskills.md
- **Day 3:** Fix circular dependency (G5.00b ↔ G5.01)
- **Day 4:** Resolve invalid skill references (T26.G3.04)
- **Day 5:** Correct 6 block reference errors

**Deliverables:** Updated allskills.md with all critical fixes applied

### Week 2: Content Improvements (Priority 2)
- **Day 1:** Split 2 skills (G3.01b, G4.02d)
- **Day 2:** Split 2 skills (G6.02, G7.02b) + write 4 new skills
- **Day 3:** Write remaining 4 new skills
- **Day 4-5:** Rewrite 10 vague descriptions

**Deliverables:** 5 split skills, 8 new skills, 10 improved descriptions

### Week 3: Dependencies (Priority 3)
- **Day 1-2:** Simplify 3 excessive dependency lists
- **Day 3:** Add 5 missing intra-topic dependencies
- **Day 4-5:** Verify X-2 rule compliance across all T27

**Deliverables:** Optimized dependency structure

### Week 4: Validation & Documentation
- **Day 1-2:** Run full validation checklist
- **Day 3:** Create before/after comparison document
- **Day 4:** Write stakeholder summary
- **Day 5:** Final review and approval

**Deliverables:** Complete T27 optimization with validation report

---

## SUCCESS METRICS

### Before Optimization:
- ❌ 72% skills with numbering issues (39/54)
- ❌ 22% skills with dependency problems (12/54)
- ❌ 19% skills with vague descriptions (10/54)
- ❌ 11% skills with block errors (6/54)
- ❌ 1 circular dependency
- ❌ 2 invalid skill references
- ❌ 5 overly broad skills
- ❌ 8 missing foundational skills

### After Optimization (Target):
- ✅ 0% skills with numbering issues (all sequential)
- ✅ 0% skills with circular dependencies
- ✅ 0% invalid skill references
- ✅ 0% block reference errors
- ✅ All descriptions concrete with examples
- ✅ All overly broad skills appropriately split
- ✅ All foundational skills filled in
- ✅ Dependency structure optimized (avg 3-4 deps per skill)

---

## CONTACT & NEXT STEPS

**Primary Contact:** [Stakeholder name]
**Review Required:** Yes, before implementing Priority 1 fixes
**Approval Required:** Yes, for splitting skills and adding new skills

**Next Steps:**
1. Review this recommendations document with stakeholders
2. Prioritize which recommendations to implement first
3. Get approval for adding 8 new skills (impacts curriculum scope)
4. Verify block syntax against CreatiCode documentation
5. Begin Phase 1 implementation (renumbering)

**Questions to Resolve:**
1. What is T26.G3.04? Does it exist or should we remove dependencies?
2. Does CreatiCode have a built-in median aggregation block?
3. What is the exact syntax for pivot table blocks?
4. Are Google Sheets block syntax examples correct?
5. Should new skills count toward grade-level skill targets?

---

**Document Status:** ✅ COMPLETE
**Generated:** 2025-11-25
**Scope:** T27 Skills (54 current, 62 after additions)
**Total Recommendations:** 50+ specific actions
**Estimated Work:** 11-16 hours (4 weeks at 4h/week)
