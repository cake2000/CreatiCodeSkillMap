# T27 Phase 1 Optimization - Quick Fix Reference

## Critical Fixes Required (HIGH Priority)

### 1. T27.G3.03 - Fix Filtering Logic (BACKWARDS)
```
CURRENT: "using 'delete rows with column [type] of value [desert]' to keep only forest levels"
PROBLEM: Deleting "desert" REMOVES deserts, doesn't keep forests!
FIX: "using 'delete rows with column [type] of value [desert]' to remove desert levels, keeping only other types"
```

### 2. T27.G4.02 - Non-existent "percentage chart block"
```
CURRENT: "using division and the percentage chart block"
PROBLEM: No such block exists! It's a chart TYPE, not a separate block
FIX: "using division and percentage charts (created with 'draw [percentage v] chart using columns [...] from table [...]')"
```

### 3. T27.G4.02d - Non-existent "keep rows" block
```
CURRENT: "or 'keep rows with column [level] > [5]' to analyze advanced levels only"
PROBLEM: There is NO "keep rows" block! Only "delete rows" with exact value match
FIX: "For complex filtering (like level > 5), iterate through rows with conditional logic to copy matching rows to a new table"
```

### 4. T27.G4.02d - Forward Dependency
```
CURRENT: Depends on T27.G4.03
PROBLEM: G4.03 comes BEFORE G4.02d - this is a forward dependency!
FIX: Change dependency from T27.G4.03 to T27.G3.03
```

### 5. T27.G6.01 - Impossible Compound Conditions
```
CURRENT: "filter rows by compound conditions (e.g., keep rows where score > 50 AND level = 'Forest')"
PROBLEM: No "keep rows" block, no > operator support in delete rows
FIX: "implement compound filtering by combining table operations: first delete rows where level ≠ 'Forest', then iterate to delete rows with score ≤ 50"
```

### 6. T27.G6.01b - Wrong VLOOKUP Syntax
```
CURRENT: "use 'item in column [age] of [students v] where column [name] equals [John]'"
PROBLEM: This syntax doesn't exist!
FIX: "use 'row # of [John] in column [name] in table [students v]' to find the row, then 'item at row (...) column [age] of table [students v]' to retrieve the value"
```

### 7. T27.G7.01b - Incomplete Google Sheets Syntax
```
CURRENT: "read from google sheet: url [...] into table [data v]"
PROBLEM: Missing required parameters (sheet name, range)
FIX: "read from google sheet: url [URL] sheet name [Sheet1] range [A1:D10] into table [data v]"
```

---

## Medium Priority Fixes

### 8. T27.G3.01 - Expand Aggregation Functions
```
CURRENT: "compute totals and means"
PROBLEM: CreatiCode supports sum, average, median, min, max - only mentions two!
FIX: "compute statistics from data tables: [sum v], [average v], [median v], [minimum v], and [maximum v] of column [scores]"
```

### 9. T27.G4.02c - No Mode Aggregation Block
```
CURRENT: "use CreatiCode's aggregation blocks ([median v]...)" [for mode]
PROBLEM: There is NO mode aggregation block!
FIX: "use aggregation blocks for median ([median v]...) and implement mode calculation manually by counting frequencies with loops"
```

### 10. T27.G5.01 - Specify Widget Blocks
```
CURRENT: "widgets (dropdown menus or buttons created with widget blocks)"
PROBLEM: Vague - which blocks?
FIX: "widgets (using 'add dropdown menu' and 'add button' blocks) responding to 'when widget [name v] clicked' or 'when widget [name v] changes'"
```

### 11. T27.G7.02b - Moving Average Needs Lists
```
CURRENT: "use 'value from [simple v] moving average window [7] of list [daily_scores v]'"
PROBLEM: Works on LISTS, not tables! Must extract first.
FIX: "extract table columns into lists, then use 'value from [simple v] moving average window [7] of list [daily_scores v]'"
```

---

## X-2 Rule Violations to Fix

### 12. T27.G7.02 - G3 → G7 (exceeds X-2)
```
CURRENT: Depends on T09.G3.05
PROBLEM: G3 to G7 is 4 grades (exceeds X-2 limit of 2)
FIX: Replace T09.G3.05 with T09.G5 or T09.G6 equivalent skill
```

### 13. T27.G7.03 - G3 → G7 (exceeds X-2)
```
CURRENT: Depends on T09.G3.05
PROBLEM: G3 to G7 is 4 grades
FIX: Replace T09.G3.05 with T09.G5 or T09.G6 skill
```

### 14. T27.G7.04 - G4 → G7 (exceeds X-2)
```
CURRENT: Depends on T10.G4.01
PROBLEM: G4 to G7 is 3 grades (exceeds X-2)
FIX: Replace T10.G4.01 with T10.G5 or T10.G6 skill
```

---

## Quick Stats

| Metric | Count |
|--------|-------|
| Total T27 Skills | 46 |
| HIGH Priority Fixes | 7 |
| MEDIUM Priority Fixes | 4 |
| X-2 Violations | 4 (3 unique) |
| Forward Dependencies | 1 |
| Wrong Block References | 5 |
| Estimated Fix Time | 6 hours |

---

## CreatiCode Block Reality Check

### ✅ These Blocks EXIST:
- `add column [name] at position (N) to table [table1 v]`
- `add to table [table1 v]: [val1] [val2] ...`
- `show table [table1 v]`
- `[sum v] of column [col] in table [table v]`
- `[average v] of column [col] in table [table v]`
- `[median v] of column [col] in table [table v]`
- `[minimum v] of column [col] in table [table v]`
- `[maximum v] of column [col] in table [table v]`
- `delete rows with column [col] of value [val] from table [table v]`
- `row count of table [table v]`
- `sort table [table v] by column [col] [order v]`
- `draw [chartType v] chart using columns [cols] from table [table v] x (X) y (Y) width (W) height (H)`
  - Chart types: line, bar, pie, percentage
- `set table [summary v] to [method v] of column [col1] in table [data v] by column [col2]`
  - Methods: minimum, maximum, sum, average, median (GROUP BY!)
- `pivot [table1] into [table2] row groups [cols] columns [valueCols] methods [methods]`
- `item at row (N) column [col] of table [table v]`
- `row # of [value] in column [col] in table [table v]`
- `export table [table v] as [filename]`
- `import file into table [table v]`
- `read from google sheet: url [URL] sheet name [name] range [range] into table [table v]`
- `write into google sheet: url [URL] sheet name [name] start cell [cell] from table [table v]`
- `value from [simple v] moving average window [N] of list [list v]`
- `add button [text] at X (X) Y (Y) width (W) height (H) tooltip [tip] as [name]`
- `add dropdown menu at X (X) Y (Y) width (W) height (H) using list [list v] as [name]`
- `when widget [name v] clicked`
- `when widget [name v] changes`
- `value of widget [name v]`

### ❌ These Blocks DO NOT EXIST:
- `percentage chart block` - It's a chart TYPE option, not separate block
- `keep rows with column [col] > [value]` - No "keep rows" block at all
- `delete rows with column [col] > [value]` - Only exact value match, no > operator
- `[mode v] of column [col] in table [table v]` - No mode aggregation block
- `item in column [col] of [table v] where column [col2] equals [value]` - Wrong syntax

---

## Priority Order for Fixes

1. **First:** Fix T27.G3.03 (backwards logic)
2. **Second:** Fix T27.G4.02d (remove "keep rows", fix dependency)
3. **Third:** Fix T27.G6.01 (compound conditions)
4. **Fourth:** Fix T27.G6.01b (VLOOKUP syntax)
5. **Fifth:** Fix T27.G4.02 (percentage chart)
6. **Sixth:** Fix T27.G7.01b (Google Sheets syntax)
7. **Seventh:** Fix T27.G4.02c (mode block)
8. **Eighth:** Fix X-2 violations in G7 skills
9. **Ninth:** Expand T27.G3.01 aggregations
10. **Tenth:** Clarify widgets in T27.G5.01

---

## End of Quick Reference
