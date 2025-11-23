# T27 Data Analysis - Quick Block Reference

**Quick lookup for implementing T27 (Data Analysis & Storytelling) skills**

---

## TABLE BASICS (T27.G3.01b)

### Create & Setup
```scratch
delete all columns from table [data v]
add column [name] at position (1) to table [data v]
add column [age] at position (2) to table [data v]
add column [score] at position (3) to table [data v]
```

### Add Data
```scratch
add to table [data v]: [John] [15] [95] [] [] [] [] [] [] [] [] []
add to table [data v]: [Mary] [14] [88] [] [] [] [] [] [] [] [] []
add to table [data v]: [Bob] [15] [92] [] [] [] [] [] [] [] [] []
```

### Display
```scratch
show table [data v]
hide table [data v]
```

---

## STATISTICS (T27.G3.01)

### Basic Aggregations
```scratch
// All 5 methods work:
([smallest v] of column [score] in table [data v])  // minimum
([largest v] of column [score] in table [data v])   // maximum
([sum v] of column [score] in table [data v])       // total
([average v] of column [score] in table [data v])   // mean
([median v] of column [score] in table [data v])    // middle value

// For MODE - no built-in block, must use loops
```

### Get Count
```scratch
(row count of table [data v])
```

---

## SORTING (T27.G4.04b)

```scratch
sort table [data v] by column [score] [large to small v]
sort table [data v] by column [name] [small to large v]
reshuffle table [data v] randomly
```

---

## FILTERING (T27.G4.02d)

### Simple Filter (Exact Match)
```scratch
delete rows with column [score] of value [0] from table [data v]
```

### Complex Filter (Requires Loop)
```scratch
// Keep rows where score > 80
set [row v] to (row count of table [data v])
repeat (row)
  if <(item at row (1) column [score] of table [data v]) < [80]> then
    delete row (1) of table [data v]
  else
    // Keep this row, check next
    delete row (2) of table [data v]  // this shifts rows up
  end
end
```

---

## GROUP BY (T27.G5.01b)

```scratch
// Create summary table: average score per grade
set table [summary v] to [average v] of column [score] in table [data v] by column [grade]

// Result: summary table has 2 columns
// Column 1: unique values from "grade" column
// Column 2: average of "score" for each grade

// Methods: minimum, maximum, sum, average, median
```

---

## PIVOT TABLES (T27.G6.02b)

```scratch
// Multi-dimensional summary
pivot [data v] into [summary v] row groups [grade,gender] columns [score,attendance] methods [average,sum]

// Creates summary with:
// - Row groups: all unique combinations of grade+gender
// - Value columns: average(score), sum(attendance)
```

---

## VLOOKUP (T27.G6.01b)

### Method 1: Direct VLOOKUP
```scratch
(item in column [age] of [students v] where column [name] equals [John])
```

### Method 2: Two-Step Lookup
```scratch
set [row v] to (row # of [John] in column [name] in table [students v])
set [age v] to (item at row (row) column [age] of table [students v])
```

### Find Substring
```scratch
(row # of item containing [john] in column [name] in table [students v])
```

---

## CHARTS (T27.G3.04, T27.G4.01, T27.G4.02)

### Bar Chart (Multi-Column)
```scratch
draw [bar v] chart using columns [classA,classB] from table [scores v] x (0) y (0) width (400) height (300)
```

### Line Chart (Trends)
```scratch
draw [line v] chart using columns [week1,week2,week3] from table [progress v] x (0) y (0) width (400) height (300)
```

### Pie Chart (Proportions)
```scratch
draw pie chart using category [fruit] and value [count] from table [survey v] x (0) y (0) width (300) height (300)
```

### Percentage Chart
```scratch
draw [percentage v] chart using columns [votes] from table [election v] x (0) y (0) width (400) height (300)
```

### Chart from List
```scratch
draw [line v] chart using list [daily_scores v] x (0) y (0) width (400) height (300)
```

---

## WIDGETS (T27.G5.01)

### Button
```scratch
add button [Filter Data] at X (0) Y (150) width (120) height (40) tooltip [Click to filter] as [btn_filter]

when widget [btn_filter v] clicked
  // Your filter logic here
end
```

### Dropdown Menu
```scratch
// First create list with options
delete all of [grades v]
add [Grade 3] to [grades v]
add [Grade 4] to [grades v]
add [Grade 5] to [grades v]

add dropdown menu at X (0) Y (150) width (150) height (35) using list [grades v] as [menu_grade]

when widget [menu_grade v] changes
  set [selected_grade v] to (value of widget [menu_grade v])
  // Filter/update based on selection
end
```

### Label (Display Results)
```scratch
add label [Average: ] at X (-100) Y (150) width (200) height (35) padding (6) as [lbl_result]

// Update label
set value to (join [Average: ] ([average v] of column [score] in table [data v])) for widget [lbl_result v]
```

### Slider
```scratch
add slider at X (0) Y (100) width (250) between (0) and (100) as [slider_threshold]

when widget [slider_threshold v] changes
  set [threshold v] to (value of widget [slider_threshold v])
  // Use threshold value
end
```

---

## IMPORT/EXPORT

### CSV Files (T27.G6.03b)
```scratch
// Export
export table [results v] as [my_analysis]  // Creates my_analysis.csv

// Import
import file into table [imported_data v]  // Shows file picker
```

### Google Sheets (T27.G7.01b)

#### Read Data
```scratch
read from google sheet: url [https://docs.google.com/spreadsheets/d/YOUR_ID/edit] sheet name [Sheet1] range [A1:D10] into table [data v]
```

#### Write Data
```scratch
write into google sheet: url [https://docs.google.com/spreadsheets/d/YOUR_ID/edit] sheet name [Results] starting cell [A1] from table [summary v]
```

#### Append Single Row
```scratch
append row [1] from table [new_data v] to sheet [Results] in Google Sheet at URL [YOUR_URL]
```

---

## MOVING AVERAGE (T27.G7.02b)

⚠️ **Works on LISTS only, not tables directly**

```scratch
// Step 1: Extract table column to list
delete all of [scores v]
repeat (row count of table [data v])
  add (item at row (counter) column [score] of table [data v]) to [scores v]
end

// Step 2: Calculate moving average
set [ma_result v] to (value from [simple v] moving average window [7] of list [scores v])

// Result is comma-separated string: "2.5,3.2,3.8,4.1,..."
// Methods: simple, exponential
```

---

## COMMON PATTERNS

### Read Single Cell
```scratch
(item at row (5) column [age] of table [students v])
```

### Update Single Cell
```scratch
replace item at row (5) column [age] of table [students v] with [16]
```

### Increment Value
```scratch
change item at row (5) column [score] of table [students v] by (10)
```

### Find Row by Value
```scratch
(row # of [Mary] in column [name] in table [students v])  // Returns -1 if not found
```

### Copy Table
```scratch
copy table [original v] into [backup v]  // Replaces backup completely
append table [new_data v] to [combined v]  // Adds rows to bottom
```

### Table to List
```scratch
// Extract column to list
copy list [names v] to column [name] of table [students v]
// Note: This WRITES list TO table column

// To extract FROM table TO list (must do manually):
delete all of [names v]
repeat (row count of table [students v])
  add (item at row (counter) column [name] of table [students v]) to [names v]
end
```

---

## DASHBOARD EXAMPLE (T27.G5.01, T27.G7.01)

```scratch
when green flag clicked
  // Setup data
  delete all columns from table [sales v]
  add column [month] at position (1) to table [sales v]
  add column [amount] at position (2) to table [sales v]
  add to table [sales v]: [Jan] [1200] [] [] [] [] [] [] [] [] [] []
  add to table [sales v]: [Feb] [1450] [] [] [] [] [] [] [] [] [] []
  add to table [sales v]: [Mar] [1380] [] [] [] [] [] [] [] [] [] []

  // Create widgets
  add label [Monthly Sales Dashboard] at X (0) Y (150) width (300) height (40) padding (6) as [lbl_title]
  add button [Show Chart] at X (-100) Y (-150) width (120) height (40) tooltip [] as [btn_chart]
  add label [Total: ] at X (100) Y (-150) width (150) height (40) padding (6) as [lbl_total]

  // Display total
  set [total v] to ([sum v] of column [amount] in table [sales v])
  set value to (join [Total: $] (total)) for widget [lbl_total v]
end

when widget [btn_chart v] clicked
  draw [bar v] chart using columns [amount] from table [sales v] x (0) y (0) width (400) height (250)
end
```

---

## TROUBLESHOOTING

### Table Not Showing?
```scratch
show table [data v]  // Make it visible
```

### Wrong Data Type?
```scratch
// Tables store everything as text
// Convert when needed:
set [num v] to ((item at row (1) column [score] of table [data v]) + (0))  // Force number
```

### Chart Not Appearing?
```scratch
// Check:
// 1. Position is on stage: x from -240 to 240, y from -180 to 180
// 2. Width/height are positive numbers
// 3. Table has numeric data in columns
```

### "Row not found" Error?
```scratch
// Check row exists:
if <(row # of [name] in column [student] in table [data v]) > [0]> then
  // Row found, safe to use
end
```

### Widget Not Responding?
```scratch
// Make sure widget is enabled:
[Enable v] widget [button1 v]

// Make sure it's visible:
set visibility [show v] for widget named [button1 v]
```

---

## LIMITS & NOTES

### Table Limits
- ✅ **Max cells per row operation:** 12 (use multiple calls for wider tables)
- ✅ **Max rows:** No documented limit (tested with 1000+ rows)
- ✅ **Max columns:** No documented limit

### Chart Limits
- ✅ **Position:** Stage coordinates (-240 to 240, -180 to 180)
- ✅ **Multiple charts:** Can draw multiple, latest overwrites if same position

### Widget Limits
- ✅ **Max widgets:** No documented limit
- ✅ **Naming:** Must be unique
- ✅ **Z-index:** Default 10, can customize with `set z-index`

### Google Sheets
- ⚠️ **Permissions:** Sheet must be shared ("Anyone with link can edit")
- ⚠️ **Rate limits:** Google API limits apply
- ✅ **Concurrent access:** Real-time collaboration supported

---

## BLOCK IDS (For Reference)

If you need to search blockdes8.txt:

**Tables:**
- data_addrowtotable
- data_removeallcolumnsfromtable
- data_addcolatposition
- data_sorttablebycolumn
- data_computetable
- data_settabletocomputed
- data_pivot_table_into_table
- data_lookuptable

**Charts:**
- widget_drawchartusinglist
- widget_drawchartusingcolumn
- widget_drawchartusingcategory

**Widgets:**
- widget_addbutton
- widget_addlabel
- widget_addmenu
- widget_addslider
- widget_whenwidgetclicked
- widget_whenwidgetchanges

**Import/Export:**
- data_exporttable
- data_importtable
- p2p_readfromgooglesheet
- p2p_writeintogooglesheet

**Advanced:**
- operator_value_from_moving_average
- data_rowindexwithcondition
- data_rowindexwithcondition2
