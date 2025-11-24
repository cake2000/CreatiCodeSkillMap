# Topic T10 (Lists & Tables) - Comprehensive Optimization Analysis

## Executive Summary

This analysis examines all 96 skills in Topic T10 (Lists & Tables) across grades K-8, comparing them against CreatiCode's actual block functionality. The analysis identifies skills that are too broad and need to be broken down, missing foundational skills, and opportunities for better scaffolding.

**Key Findings:**
- **Critical Issue**: T10.G3.01 "Create a list and add items to it" combines TWO distinct operations (create + add) and should be split
- **Multiple broad skills** covering multiple blocks need decomposition
- **Missing foundational skills** for basic list operations (add, delete, insert, replace, contains)
- **Grade K-2 skills are appropriate** - all picture-based, no coding
- **Most skills are well-structured** at G4-G8 levels

---

## 1. Current T10 Skills Inventory

### Grade K (8 skills)
- T10.GK.01: Sort picture cards into groups
- T10.GK.02: Count items in each group
- T10.GK.03: Find which group has more
- T10.GK.04: Add an item to the right group
- T10.GK.05: Find the first and last item in a row
- T10.GK.06: Look at a simple picture table
- T10.GK.07: Match items that go together
- T10.GK.08: Find all items with a special mark

### Grade 1 (6 skills)
- T10.G1.01: Sort items using two rules
- T10.G1.02: Make a picture tally chart
- T10.G1.03: Read information from a picture table
- T10.G1.04: Find the row or column with the most
- T10.G1.05: Complete a pattern in a table
- T10.G1.06: Find items that belong in both groups

### Grade 2 (7 skills)
- T10.G2.01: Build a simple data table from a list
- T10.G2.02: Add a new row to a table
- T10.G2.03: Compare two rows in a table
- T10.G2.04: Sort table rows by a column value
- T10.G2.05: Find all rows that match a rule
- T10.G2.06: Count rows that match a condition
- T10.G2.07: Understand what a list is in coding

### Grade 3 (10 skills)
- T10.G3.01: Create a list and add items to it
- T10.G3.02: Read items from a list by position (index starts at 1)
- T10.G3.03: Get the length of a list
- T10.G3.04: Remove an item from a list
- T10.G3.05: Loop through each item in a list
- T10.G3.06: Check if a list contains a specific item
- T10.G3.07: Count items in a list that match a condition
- T10.G3.08: Check if a list is empty before accessing
- T10.G3.09: Increment or decrement a list item's value
- T10.G3.10: Display a list monitor on the stage

### Grade 4 (20 skills)
- T10.G4.01: Find an item's position in a list (linear search)
- T10.G4.02: Store and retrieve parallel list data
- T10.G4.03: Insert an item at a specific position in a list
- T10.G4.04: Replace an item in a list
- T10.G4.05: Use built-in blocks to sort a list
- T10.G4.06: Use built-in blocks to get list statistics
- T10.G4.07: Find the maximum or minimum item in a list manually
- T10.G4.08: Filter items from a list based on a condition
- T10.G4.09: Build a high score list with parallel lists
- T10.G4.10: Swap two items in a list
- T10.G4.11: Copy or append one list to another
- T10.G4.12: Split a text string into a list
- T10.G4.13: Join list items into a text string
- T10.G4.14: Reverse the order of items in a list
- T10.G4.15: Randomly shuffle items in a list
- T10.G4.16: Generate a list of random numbers
- T10.G4.17: Delete an item from a list by value
- T10.G4.18: Loop through list indices
- T10.G4.19: Find an item containing a substring
- T10.G4.20: Select multiple items from a list by criteria

### Grade 5 (18 skills) - Tables introduced
- T10.G5.01: Understand table structure (rows, columns, cells)
- T10.G5.02: Create a table and add columns
- T10.G5.03: Add rows of data to a table
- T10.G5.04: Read a cell value from a table
- T10.G5.05: Update a cell value in a table
- T10.G5.06: Get the row count and find a row by value
- T10.G5.07: Loop through table rows to compute aggregates
- T10.G5.08: Use built-in table aggregate blocks
- T10.G5.09: Delete rows from a table
- T10.G5.10: Convert between lists and tables
- T10.G5.11: Manage table columns
- T10.G5.12: Copy list data to table column
- T10.G5.13: Insert a row at a specific position
- T10.G5.14: Replace an entire row in a table
- T10.G5.15: Get an entire row as a list
- T10.G5.16: Find a row by partial match
- T10.G5.17: Increment or decrement a table cell value
- T10.G5.18: Show and hide table monitors

### Grade 6 (8 skills)
- T10.G6.01: Sort a table by a column
- T10.G6.02: Filter table rows based on a condition
- T10.G6.03: Copy and append tables
- T10.G6.04: Use table lookup to find related data
- T10.G6.05: Group data and compute aggregates per group
- T10.G6.06: Use set operations on lists
- T10.G6.07: Remove duplicate items from a list
- T10.G6.08: Shuffle table rows randomly

### Grade 7 (14 skills)
- T10.G7.01: Pivot or reshape table data
- T10.G7.02: Import external data into a table
- T10.G7.03: Design a table schema for a real-world scenario
- T10.G7.04: Visualize table data with charts
- T10.G7.05: Clean and transform table data
- T10.G7.06: Validate and handle missing data in tables
- T10.G7.07: Analyze a dataset to find patterns or outliers
- T10.G7.08: Use regex patterns to find items in lists
- T10.G7.09: Read and write data with Google Sheets
- T10.G7.10: Manage Google Sheets structure
- T10.G7.11: Display formatted table snapshots
- T10.G7.12: Export table data to a file
- T10.G7.13: Save and load data to the cloud
- T10.G7.14: Use AI to analyze table data

### Grade 8 (8 skills)
- T10.G8.01: Use nested loops to compare data across two tables
- T10.G8.02: Implement bubble sort algorithm step by step
- T10.G8.03: Implement selection sort algorithm step by step
- T10.G8.04: Build a simulation using table-based state
- T10.G8.05: Query and report statistics from a complex dataset
- T10.G8.06: Model relationships using multiple linked tables
- T10.G8.07: Implement a hash table lookup using lists
- T10.G8.08: Use advanced list operations for algorithm optimization

**Total: 96 skills**

---

## 2. Available CreatiCode List & Table Blocks

### Standard Scratch List Blocks (assumed to exist, not all documented in blockdes8.txt)
1. **add [item] to [list]** - Add item to end of list
2. **delete (position) of [list]** - Delete item at position
3. **delete all of [list]** - Clear all items
4. **insert [item] at (position) of [list]** - Insert item at position
5. **replace item (position) of [list] with [value]** - Replace item at position
6. **item (position) of [list]** - Get item at position
7. **item # of [value] in [list]** - Find position of value
8. **length of [list]** - Get list length
9. **[list] contains [item]?** - Check if list contains item

### CreatiCode-Specific List Blocks (documented in blockdes8.txt)
10. **reduce item (INDEX) of [LISTNAME v] by (N)** - Decrement item (for young learners)
11. **change item (INDEX) of [LISTNAME v] by (N)** - Increment/decrement item
12. **join [LISTNAME v] into text with [SEPARATOR]** - Join list to string
13. **set [LISTNAME v] to split of [TEXT] with splitter [SEPARATOR]** - Split string to list
14. **delete value [V] from [LISTNAME v]** - Delete by value (first occurrence)
15. **reverse [LISTNAME v]** - Reverse list order
16. **reshuffle [LISTNAME v] randomly** - Shuffle list randomly
17. **sort list [LISTNAME v] from [METHOD v]** - Sort (large to small / small to large)
18. **insert (N) [SELECTOR v] items from [LISTNAME1 v] into [LISTNAME2 v]** - Select N items (largest/smallest/random) and append
19. **copy [LISTNAME1 v] to [LISTNAME2 v]** - Copy list (replace)
20. **append [LISTNAME1 v] to [LISTNAME2 v]** - Append list
21. **set [LISTNAME v] to (N) random whole numbers between (MIN) and (MAX) [REPEATMETHOD v]** - Generate random numbers
22. **set [LISTNAME v] to (N) random numbers with seed (SEED)** - Generate seeded random numbers
23. **# of item containing [TEXT] in [LISTNAME v]** - Find position by substring
24. **[METHOD v] of list [LISTNAME v]** - Get statistics (smallest/largest/sum/average/median)
25. **for each item [VARIABLENAME v] in [LISTNAME v]** - Loop through values
26. **for each index [INDEXVARIABLENAME v] in [LISTNAME v]** - Loop through indices

### Table Blocks (documented in blockdes8.txt)
27. **add column [COLUMNNAME] at position (POSITION) to table [TABLENAME v]** - Add column
28. **delete column [COLUMNNAME] from table [TABLENAME v]** - Delete column
29. **delete all columns from table [TABLENAME v]** - Delete all columns
30. **add to table [TABLENAME v]: [CELL1] [CELL2]...** - Add row
31. **insert at row (ROWNUM) of table [TABLENAME v]: [CELL1] [CELL2]...** - Insert row
32. **replace row (ROWNUM) of table [TABLENAME v] with: [CELL1] [CELL2]...** - Replace entire row
33. **delete row (ROWNUM) of table [TABLENAME v]** - Delete row by index
34. **delete rows with column [COLUMN] of value [VALUE] from table [TABLENAME v]** - Delete rows by condition
35. **delete all rows from table [TABLENAME v]** - Delete all rows
36. **item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v]** - Get cell value
37. **replace item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] with [VALUE]** - Replace cell
38. **change item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)** - Increment/decrement cell
39. **reduce item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)** - Decrement cell
40. **row count of table [TABLENAME v]** - Get row count
41. **row (ROWINDEX) of table [TABLENAME v] separator [SEPARATOR]** - Get row as string
42. **row # of [VALUE] in column [COLUMN] in table [TABLENAME v]** - Find row by value
43. **row # of item containing [SUBSTRING] in column [COLUMN] in table [TABLENAME v]** - Find row by substring
44. **[METHOD] of column [COLUMNNAME] in table [TABLE v]** - Column statistics (sum/average/min/max/median)
45. **sort table [TABLENAME v] by column [COLUMN] [SORTORDER v]** - Sort table
46. **reshuffle table [TABLENAME v] randomly** - Shuffle table rows
47. **copy table [TABLE1] into [TABLE2]** - Copy table
48. **append table [TABLE1] to [TABLE2]** - Append tables
49. **copy list [LISTNAME v] to column [COLUMNNAME] of table [TABLENAME v]** - Copy list to column
50. **item in column [RETURNCOLUMN] of [TABLENAME v] where column [SEARCHCOLUMN] equals [SEARCHTEXT]** - Lookup
51. **set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2]** - Group and aggregate
52. **pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST]** - Pivot table
53. **show table [TABLENAME v]** - Show table monitor
54. **hide table [TABLENAME v]** - Hide table monitor
55. **show snapshot of table [TABLENAME v] from row (STARTROW) to (ENDROW) with style [STYLE] [THEMECOLOR]** - Formatted display
56. **export table [TABLENAME v] as [FILENAME]** - Export to CSV
57. **import file into table [TABLE]** - Import from file
58. **save table [TABLE v] to server as [DATANAME]** - Save to cloud
59. **load [DATANAME] from server into table [TABLE v]** - Load from cloud

**Total: 59 distinct blocks** (26 list blocks + 33 table blocks)

---

## 3. Issues Identified

### HIGH SEVERITY - Skills That Are Too Broad (Need Breaking Down)

#### H1. T10.G3.01: "Create a list and add items to it"
**Issue**: Combines TWO separate operations
- Creating a list variable (one-time setup)
- Using the `add [item] to [list]` block (repeated operation)

**Recommendation**: Split into:
- **T10.G3.01.01**: Create a new list variable
- **T10.G3.01.02**: Add an item to the end of a list using `add [item] to [list]`

**Rationale**: These are conceptually and operationally distinct. Students need to understand creating a list (naming, variable management) separately from adding items (the fundamental list operation they'll use most).

---

#### H2. T10.G3.04: "Remove an item from a list"
**Issue**: Describes TWO different blocks with different purposes
- `delete (position) of [list]` - Delete by position
- `delete all of [list]` - Clear entire list

**Recommendation**: Split into:
- **T10.G3.04.01**: Delete an item at a specific position using `delete (position) of [list]`
- **T10.G3.04.02**: Clear all items from a list using `delete all of [list]`

**Rationale**: Deleting one item vs. clearing the entire list are fundamentally different operations with different use cases.

---

#### H3. T10.G4.06: "Use built-in blocks to get list statistics"
**Issue**: Covers FIVE different statistical functions in one skill
- smallest of list
- largest of list
- sum of list
- average of list
- median of list

**Recommendation**: Split into:
- **T10.G4.06.01**: Find the smallest value in a list using `[smallest v] of list [list]`
- **T10.G4.06.02**: Find the largest value in a list using `[largest v] of list [list]`
- **T10.G4.06.03**: Calculate the sum of all values in a list using `[sum v] of list [list]`
- **T10.G4.06.04**: Calculate the average of values in a list using `[average v] of list [list]`
- **T10.G4.06.05**: Find the median value in a list using `[median v] of list [list]`

**Rationale**: Each statistic has different mathematical meaning and use cases. Students need to understand when to use each one.

---

#### H4. T10.G4.11: "Copy or append one list to another"
**Issue**: Covers TWO different blocks with different behaviors
- `copy [list1] to [list2]` - Replaces list2's contents
- `append [list1] to [list2]` - Adds to end of list2

**Recommendation**: Split into:
- **T10.G4.11.01**: Copy one list to another (replacing contents) using `copy [list1] to [list2]`
- **T10.G4.11.02**: Append one list to another (adding to end) using `append [list1] to [list2]`

**Rationale**: Copy vs. append have opposite effects on the destination list. This is a critical distinction.

---

#### H5. T10.G5.09: "Delete rows from a table"
**Issue**: Covers THREE different deletion operations
- Delete one row by index
- Delete rows matching a condition
- Delete all rows

**Recommendation**: Split into:
- **T10.G5.09.01**: Delete a single row by index using `delete row (n) of table [table]`
- **T10.G5.09.02**: Delete rows matching a condition using `delete rows with column [name] of value [v] from table [table]`
- **T10.G5.09.03**: Clear all rows from a table using `delete all rows from table [table]`

**Rationale**: Three distinct operations with different use cases and complexity levels.

---

#### H6. T10.G5.11: "Manage table columns"
**Issue**: Covers THREE different column operations
- Add column
- Delete column
- Remove all columns

**Recommendation**: Split into:
- **T10.G5.11.01**: Add a column at a specific position using `add column [name] at position (n)`
- **T10.G5.11.02**: Delete a single column using `delete column [name] from table [table]`
- **T10.G5.11.03**: Remove all columns from a table using `remove all columns from table [table]`

**Rationale**: Three operations that should be learned incrementally, not all at once.

---

#### H7. T10.G5.06: "Get the row count and find a row by value"
**Issue**: Combines TWO unrelated operations
- Getting row count (simple reporter)
- Finding a row by value (search operation)

**Recommendation**: Split into:
- **T10.G5.06.01**: Get the number of rows in a table using `row count of table [table]`
- **T10.G5.06.02**: Find which row contains a value using `row # of [value] in column [name] in table [table]`

**Rationale**: Row count is a simple property; finding rows is a search operation. Different complexity levels.

---

### MEDIUM SEVERITY - Missing Foundational Skills

#### M1. Missing: Explicit skills for standard Scratch list blocks
**Issue**: The current skills mention blocks like "add to list" and "contains" but don't have dedicated skills for each basic block.

**Recommendation**: Ensure each fundamental block has its own skill at G3 level (already mostly covered, but verify):
- add [item] to [list] - Covered in T10.G3.01 (needs split)
- delete (position) - Covered in T10.G3.04 (needs split)
- insert at position - T10.G4.03 ✓
- replace item - T10.G4.04 ✓
- item # of value - T10.G4.01 ✓
- contains - T10.G3.06 ✓
- length - T10.G3.03 ✓
- item at position - T10.G3.02 ✓

**Status**: Mostly covered after splitting T10.G3.01 and T10.G3.04

---

#### M2. Missing: Table row extraction to list
**Issue**: Skill T10.G5.15 "Get an entire row as a list" exists but describes it as returning a string with separator, not an actual list.

**Current Description**: "extract all values from a row as a single list"
**Actual Block**: `row (n) of table [table] separator [sep]` - returns TEXT, not list

**Recommendation**:
- Keep T10.G5.15 but correct the description to match actual block behavior (returns text)
- If there's a way to get a row as an actual list data structure, add that as a separate skill

---

#### M3. Missing: "Get column from table as list" block
**Issue**: T10.G5.10 mentions "extract a column from a table into a list" but no specific block is documented for this in blockdes8.txt.

**Current Skill**: T10.G5.10 says "get column [name] from table [table] as list"
**Block Status**: NOT found in blockdes8.txt

**Recommendation**:
- Verify this block actually exists in CreatiCode
- If it doesn't exist, update T10.G5.10 to use a workaround (loop through rows)
- If it exists, it's fine as-is

---

### LOW SEVERITY - Minor Issues

#### L1. T10.G4.16: "Generate a list of random numbers"
**Issue**: Covers TWO separate random generation blocks
- `set [list] to (N) random whole numbers between (min) and (max) [repetition]` - integers
- `set [list] to (N) random numbers with seed (SEED)` - seeded decimals 0-1

**Recommendation**: Consider splitting, but these could stay together as both are "random list generation"
- Current approach is acceptable
- Could split if wanting more granular skills

---

#### L2. Dependency Check Needed
**Issue**: Need to verify X-2 rule (grade X can only depend on X, X-1, or X-2)

**Action**: Review all dependencies for violations. Spot check shows:
- T10.G2.04 depends on T01.G1.01 (G2 → G1, OK)
- T10.G3.05 depends on T07.G3.01 (G3 → G3, OK)
- T10.G4.18 depends on T07.G4.01 (G4 → G4, OK)

**Status**: Appears OK on spot check, but full verification recommended

---

#### L3. Skills with unclear or non-actionable descriptions
**Issue**: Some skill descriptions could be more specific about which blocks to use

Examples:
- T10.G6.06 "Use set operations on lists" - mentions union/intersect/minus but these blocks aren't in blockdes8.txt
- T10.G6.07 "Remove duplicate items from a list" - mentions `unique items of [list]` block not in blockdes8.txt

**Recommendation**:
- Verify these blocks exist in CreatiCode
- If not, update skills to show manual implementation approaches
- If they exist but aren't documented, add to block documentation

---

## 4. Detailed Recommendations for Each Broad Skill

### T10.G3.01: Create a list and add items to it → SPLIT

**Current:**
```
ID: T10.G3.01
Skill: Create a list and add items to it
Description: Students create a new list variable (e.g., "fruits" or "scores") and use the `add [item] to [list]` block to add 3-4 items one at a time. They check the "show list" option to see the list monitor on stage and understand that a list holds multiple values in order. This is the foundational skill for all list operations.
Dependencies: T09.G3.01.04
```

**Recommended Split:**

```
ID: T10.G3.01.01
Skill: Create a new list variable
Description: Students create a new list variable in the Variables palette by clicking "Make a List" and giving it a descriptive name (e.g., "fruits", "scores", "inventory"). They understand that lists are containers that can hold multiple values, unlike regular variables which hold only one value. This is the first step before any list operations can be performed.
Dependencies: T09.G3.01.04

ID: T10.G3.01.02
Skill: Add an item to the end of a list
Description: Students use the `add [item] to [list]` block to add items one at a time to the end of a list. They observe how each item is added in sequence (1, 2, 3...) and understand that lists grow dynamically as items are added. They practice adding 3-4 items and use the list monitor to see the growing list.
Dependencies: T10.G3.01.01
```

---

### T10.G3.04: Remove an item from a list → SPLIT

**Current:**
```
ID: T10.G3.04
Skill: Remove an item from a list
Description: Students use the `delete (position) of [list]` block to remove an item from a specific position, or `delete all of [list]` to clear the entire list. They observe how remaining items shift positions after deletion and understand that lists can shrink.
Dependencies: T10.G3.02, T10.G3.03
```

**Recommended Split:**

```
ID: T10.G3.04.01
Skill: Delete an item at a specific position
Description: Students use the `delete (position) of [list]` block to remove an item from a specific position in the list. They observe how items after the deleted position shift down (e.g., item 3 becomes item 2). They understand that the list length decreases by 1 and practice deleting items from different positions (beginning, middle, end).
Dependencies: T10.G3.02, T10.G3.03

ID: T10.G3.04.02
Skill: Clear all items from a list
Description: Students use the `delete all of [list]` block to remove every item from a list at once, returning it to empty. They understand when clearing is useful (starting fresh, resetting for a new game) and observe that after clearing, the list length becomes 0.
Dependencies: T10.G3.04.01, T10.G3.03
```

---

### T10.G4.06: Use built-in blocks to get list statistics → SPLIT

**Current:**
```
ID: T10.G4.06
Skill: Use built-in blocks to get list statistics
Description: Students use CreatiCode's aggregate blocks like `[sum/average/smallest/largest/median] of list [list]` to compute statistics on numeric lists. They understand these operations process all items to produce a single result.
Dependencies: T10.G3.01, T10.G3.03
```

**Recommended Split:**

```
ID: T10.G4.06.01
Skill: Find the smallest value in a list
Description: Students use the `[smallest v] of list [list]` block to find the minimum value in a numeric list. They understand this scans all items and returns the lowest value. They practice with different lists and predict which value will be returned.
Dependencies: T10.G3.01.02, T10.G3.03

ID: T10.G4.06.02
Skill: Find the largest value in a list
Description: Students use the `[largest v] of list [list]` block to find the maximum value in a numeric list. They understand this scans all items and returns the highest value. They compare this to finding smallest and understand min/max concepts.
Dependencies: T10.G4.06.01

ID: T10.G4.06.03
Skill: Calculate the sum of all values in a list
Description: Students use the `[sum v] of list [list]` block to add up all numeric values in a list. They understand this is useful for totals (total points, total money) and verify results by manual addition with small lists.
Dependencies: T10.G4.06.01

ID: T10.G4.06.04
Skill: Calculate the average of values in a list
Description: Students use the `[average v] of list [list]` block to find the mean of all numeric values. They understand average represents typical/middle value and relate it to sum divided by length. They use this for grade averages, temperature averages, etc.
Dependencies: T10.G4.06.03, T10.G3.03

ID: T10.G4.06.05
Skill: Find the median value in a list
Description: Students use the `[median v] of list [list]` block to find the middle value when sorted. They understand median differs from average (less affected by outliers) and identify when median is more useful than average (income, test scores with outliers).
Dependencies: T10.G4.06.04, T10.G4.05
```

---

### T10.G4.11: Copy or append one list to another → SPLIT

**Current:**
```
ID: T10.G4.11
Skill: Copy or append one list to another
Description: Students copy all items from one list to another or append items to an existing list using a loop and the `add [item] to [list]` block. They understand the difference between copying (creates duplicate list) and appending (adds to existing list).
Dependencies: T10.G3.01, T10.G3.05
```

**Recommended Split:**

```
ID: T10.G4.11.01
Skill: Copy one list to another (replacing contents)
Description: Students use the `copy [list1] to [list2]` block to duplicate a list. They understand this REPLACES all items in list2 with items from list1, so list2's original contents are lost. After copying, both lists have identical items but remain separate (changing one doesn't affect the other).
Dependencies: T10.G3.01.02, T10.G3.05

ID: T10.G4.11.02
Skill: Append one list to another (adding to end)
Description: Students use the `append [list1] to [list2]` block to add all items from list1 to the END of list2. They understand this PRESERVES list2's original items and adds list1's items below them. They compare append vs. copy and identify when each is appropriate.
Dependencies: T10.G4.11.01
```

---

### T10.G5.06: Get the row count and find a row by value → SPLIT

**Current:**
```
ID: T10.G5.06
Skill: Get the row count and find a row by value
Description: Students use `row count of table [table]` to determine how many rows exist, and `row # of [value] in column [name] in table [table]` to find which row contains a specific value.
Dependencies: T10.G5.04
```

**Recommended Split:**

```
ID: T10.G5.06.01
Skill: Get the number of rows in a table
Description: Students use the `row count of table [table]` block to find how many rows exist in a table. They understand this is essential for loops (iterate from 1 to row count), checking if table is empty (row count = 0), and reporting table size.
Dependencies: T10.G5.04

ID: T10.G5.06.02
Skill: Find which row contains a value
Description: Students use the `row # of [value] in column [name] in table [table]` block to search for the first row where a specific column equals a value. They understand this returns the row number (index) or 0 if not found, enabling them to locate data for reading or updating.
Dependencies: T10.G5.06.01, T10.G4.01
```

---

### T10.G5.09: Delete rows from a table → SPLIT

**Current:**
```
ID: T10.G5.09
Skill: Delete rows from a table
Description: Students use `delete row (n) of table [table]` to remove a specific row, `delete rows with column [name] of value [v] from table [table]` to remove rows matching a condition, and `delete all rows from table [table]` to clear data while keeping structure. They understand that remaining rows renumber and that deleting all rows clears data but keeps column structure intact, useful for resetting a table for new data.
Dependencies: T10.G5.06
```

**Recommended Split:**

```
ID: T10.G5.09.01
Skill: Delete a single row by index
Description: Students use the `delete row (n) of table [table]` block to remove a specific row by its position number. They observe how remaining rows shift up (row 4 becomes row 3) and understand the row count decreases by 1.
Dependencies: T10.G5.06.01

ID: T10.G5.09.02
Skill: Delete rows matching a condition
Description: Students use the `delete rows with column [name] of value [v] from table [table]` block to remove ALL rows where a specific column equals a value. They understand this can delete multiple rows at once (e.g., delete all students in grade 8) and is more efficient than looping to delete one by one.
Dependencies: T10.G5.09.01, T10.G5.06.02

ID: T10.G5.09.03
Skill: Clear all rows from a table
Description: Students use the `delete all rows from table [table]` block to remove all data while preserving the column structure. They understand this is useful for resetting a table for new data without recreating columns, and compare this to deleting entire table vs. just clearing data.
Dependencies: T10.G5.09.01
```

---

### T10.G5.11: Manage table columns → SPLIT

**Current:**
```
ID: T10.G5.11
Skill: Manage table columns
Description: Students add, delete, and clear columns in a table using `add column [name] at position (n)`, `delete column [name] from table [table]`, and `remove all columns from table [table]`. They understand that deleting a column removes all data in that column permanently, that removing all columns completely resets the table structure, and that tables can be restructured dynamically.
Dependencies: T10.G5.02, T10.G5.03
```

**Recommended Split:**

```
ID: T10.G5.11.01
Skill: Add a column at a specific position
Description: Students use the `add column [name] at position (n) to table [table]` block to insert a new column at a specific position (1 = first column, 2 = second, etc.). They understand existing columns shift right to make room, and the new column starts empty. They practice adding columns at beginning, middle, and end.
Dependencies: T10.G5.02

ID: T10.G5.11.02
Skill: Delete a single column
Description: Students use the `delete column [name] from table [table]` block to permanently remove a column and ALL its data. They understand this cannot be undone, remaining columns shift left, and the table structure changes. They identify when column deletion is appropriate vs. just clearing cell values.
Dependencies: T10.G5.11.01, T10.G5.03

ID: T10.G5.11.03
Skill: Remove all columns from a table
Description: Students use the `remove all columns from table [table]` block to completely reset a table to empty structure (no columns, no rows). They understand this is more destructive than deleting all rows (which keeps columns) and use this when completely restructuring a table.
Dependencies: T10.G5.11.02
```

---

## 5. New Skills to Add

### N1. Add skill for reduce item (for young learners)

**Proposed:**
```
ID: T10.G3.09.01
Skill: Decrement a list item's value (for young learners)
Description: Students use the `reduce item (position) of [list] by (amount)` block to decrease numeric values in a list (e.g., reduce health by 5, reduce inventory by 1). This block is designed for young learners who haven't learned negative numbers yet, providing a simpler alternative to "change by -5".
Dependencies: T10.G3.02, T10.G3.01.02
```

**Note**: Current T10.G3.09 already covers increment/decrement but doesn't specifically mention the "reduce" block for young learners. Consider adding this as a sub-skill or note.

---

### N2. Add specific skill for table cell increment/decrement

Currently T10.G5.17 covers this, but it could be split similar to lists:

**Proposed (optional):**
```
ID: T10.G5.17.01
Skill: Increment a table cell value
Description: Students use the `change item at row (n) column [name] of table [table] by (amount)` block with positive values to increase numeric cell values (e.g., add 10 points, increase age by 1).
Dependencies: T10.G5.05, T10.G5.04

ID: T10.G5.17.02
Skill: Decrement a table cell value (for young learners)
Description: Students use the `reduce item at row (n) column [name] of table [table] by (amount)` block to decrease numeric cell values without using negative numbers, making it accessible to younger learners.
Dependencies: T10.G5.17.01
```

---

## 6. Complete Updated T10 Skill List

### Grade K (8 skills) - NO CHANGES
All K skills are appropriate picture-based activities.

```
ID: T10.GK.01
Topic: T10 – Lists & Tables
Skill: Sort picture cards into groups
Description: Students sort 4-6 picture cards into 2-3 groups based on a visible attribute (color, shape, or type). For example: sort animals into "pets" and "wild animals," or sort shapes into "circles" and "not circles." This builds the foundational concept of categorization.

ID: T10.GK.02
Topic: T10 – Lists & Tables
Skill: Count items in each group
Description: After sorting items into groups, students count how many items are in each group and select the count from picture-based answer choices (showing 1, 2, 3, or 4 dots/items).
Dependencies:
* T10.GK.01: Sort picture cards into groups

ID: T10.GK.03
Topic: T10 – Lists & Tables
Skill: Find which group has more
Description: Students compare two groups of sorted items and identify which group has more items. Answer choices show pictures of the two groups.
Dependencies:
* T10.GK.02: Count items in each group

ID: T10.GK.04
Topic: T10 – Lists & Tables
Skill: Add an item to the right group
Description: Students are shown sorted groups and one new item. They decide which group the new item belongs to and drag it there.
Dependencies:
* T10.GK.01: Sort picture cards into groups

ID: T10.GK.05
Topic: T10 – Lists & Tables
Skill: Find the first and last item in a row
Description: Students identify the first and last item in a row of 3-5 picture cards arranged in order (left to right).
Dependencies:
* T01.GK.03: Find the first and last pictures

ID: T10.GK.06
Topic: T10 – Lists & Tables
Skill: Look at a simple picture table
Description: Students view a simple 2x3 or 3x3 picture table (e.g., a chart showing which child likes which fruit) and answer questions like "What does Sam like?" by tapping the correct cell.
Dependencies:
* T10.GK.01: Sort picture cards into groups

ID: T10.GK.07
Topic: T10 – Lists & Tables
Skill: Match items that go together
Description: Students match pairs of related items (e.g., match animals to their homes, match tools to their uses) by drawing lines or dragging.
Dependencies:
* T10.GK.01: Sort picture cards into groups

ID: T10.GK.08
Topic: T10 – Lists & Tables
Skill: Find all items with a special mark
Description: Students identify all items in a collection that have a special visual mark (star, checkmark, red border) and count them.
Dependencies:
* T10.GK.02: Count items in each group
```

---

### Grade 1 (6 skills) - NO CHANGES
All G1 skills are appropriate picture-based activities.

```
ID: T10.G1.01
Topic: T10 – Lists & Tables
Skill: Sort items using two rules
Description: Students sort 6-8 items into groups using two attributes (e.g., "big red shapes" vs "small blue shapes"), understanding that items can belong to groups based on multiple properties.
Dependencies:
* T10.GK.01: Sort picture cards into groups
* T10.GK.04: Add an item to the right group

ID: T10.G1.02
Topic: T10 – Lists & Tables
Skill: Make a picture tally chart
Description: Students count items in categories and represent the count using tally marks or pictures in a simple chart (e.g., count and tally how many students like each snack).
Dependencies:
* T10.GK.02: Count items in each group
* T10.GK.06: Look at a simple picture table

ID: T10.G1.03
Topic: T10 – Lists & Tables
Skill: Read information from a picture table
Description: Students answer questions by finding and reading specific cells in a picture table with 3-4 rows and 3-4 columns.
Dependencies:
* T10.GK.06: Look at a simple picture table

ID: T10.G1.04
Topic: T10 – Lists & Tables
Skill: Find the row or column with the most
Description: Students examine a picture table and identify which row or column has the most items by comparing visually.
Dependencies:
* T10.G1.03: Read information from a picture table
* T10.GK.03: Find which group has more

ID: T10.G1.05
Topic: T10 – Lists & Tables
Skill: Complete a pattern in a table
Description: Students identify a pattern in rows or columns of a table and fill in missing cells (e.g., alternating colors, increasing numbers shown as dots).
Dependencies:
* T10.G1.03: Read information from a picture table
* T01.GK.07: Find the pattern that repeats

ID: T10.G1.06
Topic: T10 – Lists & Tables
Skill: Find items that belong in both groups
Description: Students identify items that satisfy two conditions (e.g., "Find things that are both red AND round" from a mixed collection).
Dependencies:
* T10.G1.01: Sort items using two rules
```

---

### Grade 2 (7 skills) - NO CHANGES
All G2 skills are appropriate picture-based activities bridging to code concepts.

```
ID: T10.G2.01
Topic: T10 – Lists & Tables
Skill: Build a simple data table from a list
Description: Students organize a list of information into a table with labeled rows and columns (e.g., organize "Sam has 3 apples, Lia has 2 oranges" into a table).
Dependencies:
* T10.G1.03: Read information from a picture table

ID: T10.G2.02
Topic: T10 – Lists & Tables
Skill: Add a new row to a table
Description: Students add a new row of data to an existing picture table by filling in all column values for a new entry.
Dependencies:
* T10.G2.01: Build a simple data table from a list

ID: T10.G2.03
Topic: T10 – Lists & Tables
Skill: Compare two rows in a table
Description: Students compare data from two different rows in a table and answer questions about differences or similarities (e.g., "Who has more points, Sam or Lia?").
Dependencies:
* T10.G2.01: Build a simple data table from a list

ID: T10.G2.04
Topic: T10 – Lists & Tables
Skill: Sort table rows by a column value
Description: Students rearrange rows in a simple table to put them in order by one column (e.g., "arrange students from most to least points").
Dependencies:
* T10.G2.01: Build a simple data table from a list
* T01.G1.01: Put pictures in order to plant a seed

ID: T10.G2.05
Topic: T10 – Lists & Tables
Skill: Find all rows that match a rule
Description: Students identify and mark all rows in a table where a specific column matches a condition (e.g., "Find all students with 10 or more points").
Dependencies:
* T10.G2.01: Build a simple data table from a list

ID: T10.G2.06
Topic: T10 – Lists & Tables
Skill: Count rows that match a condition
Description: Students count how many rows in a table satisfy a condition (e.g., "How many students scored more than 5?").
Dependencies:
* T10.G2.05: Find all rows that match a rule

ID: T10.G2.07
Topic: T10 – Lists & Tables
Skill: Understand what a list is in coding
Description: Students transition from picture tables to understanding that code can have "lists" - ordered collections of items that the computer stores and uses. They match real-world examples (shopping list, playlist, leaderboard) to the concept of a code list.
Dependencies:
* T10.G2.01: Build a simple data table from a list
```

---

### Grade 3 (12 skills) - MAJOR CHANGES
**Changes**: Split T10.G3.01 and T10.G3.04 into sub-skills

```
ID: T10.G3.01.01
Topic: T10 – Lists & Tables
Skill: Create a new list variable
Description: Students create a new list variable in the Variables palette by clicking "Make a List" and giving it a descriptive name (e.g., "fruits", "scores", "inventory"). They understand that lists are containers that can hold multiple values, unlike regular variables which hold only one value. This is the first step before any list operations can be performed.
Dependencies:
* T09.G3.01.04: Display variable value on stage using the variable monitor

ID: T10.G3.01.02
Topic: T10 – Lists & Tables
Skill: Add an item to the end of a list
Description: Students use the `add [item] to [list]` block to add items one at a time to the end of a list. They observe how each item is added in sequence (1, 2, 3...) and understand that lists grow dynamically as items are added. They practice adding 3-4 items and use the list monitor to see the growing list.
Dependencies:
* T10.G3.01.01: Create a new list variable

ID: T10.G3.02
Topic: T10 – Lists & Tables
Skill: Read items from a list by position (index starts at 1)
Description: Students use the `item (1) of [list]` block to retrieve specific items from a list by their position number (index). They understand that the first item is at position 1, second at position 2, etc. Students practice reading different positions and displaying or using the retrieved values.
Dependencies:
* T10.G3.01.02: Add an item to the end of a list

ID: T10.G3.03
Topic: T10 – Lists & Tables
Skill: Get the length of a list
Description: Students use the `length of [list]` block to find how many items are in a list. They understand that as items are added or removed, the length changes. This is essential for knowing the bounds when accessing list items.
Dependencies:
* T10.G3.01.02: Add an item to the end of a list

ID: T10.G3.04.01
Topic: T10 – Lists & Tables
Skill: Delete an item at a specific position
Description: Students use the `delete (position) of [list]` block to remove an item from a specific position in the list. They observe how items after the deleted position shift down (e.g., item 3 becomes item 2). They understand that the list length decreases by 1 and practice deleting items from different positions (beginning, middle, end).
Dependencies:
* T10.G3.02: Read items from a list by position (index starts at 1)
* T10.G3.03: Get the length of a list

ID: T10.G3.04.02
Topic: T10 – Lists & Tables
Skill: Clear all items from a list
Description: Students use the `delete all of [list]` block to remove every item from a list at once, returning it to empty. They understand when clearing is useful (starting fresh, resetting for a new game) and observe that after clearing, the list length becomes 0.
Dependencies:
* T10.G3.04.01: Delete an item at a specific position
* T10.G3.03: Get the length of a list

ID: T10.G3.05
Topic: T10 – Lists & Tables
Skill: Loop through each item in a list
Description: Students use the `for each [item] in [list]` block to automatically visit every item in sequence. Unlike counted repeat loops where you specify a number of repetitions, this block iterates through all items regardless of list length. Students perform simple actions on each item (e.g., say each fruit name). Keep the list short (3-4 items) and actions simple.
Dependencies:
* T07.G3.01: Use a counted repeat loop
* T10.G3.01.02: Add an item to the end of a list
* T10.G3.02: Read items from a list by position (index starts at 1)

ID: T10.G3.06
Topic: T10 – Lists & Tables
Skill: Check if a list contains a specific item
Description: Students use the `[list] contains [item]?` block to check whether a value exists in a list. They use this in conditionals to make decisions based on list membership (e.g., "if my fruits list contains 'apple' then say 'I have an apple!'").
Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T08.G3.01: Use a simple if in a script

ID: T10.G3.07
Topic: T10 – Lists & Tables
Skill: Count items in a list that match a condition
Description: Students loop through a short list and count items that match a simple condition (e.g., "count numbers greater than 5" or "count items equal to 'apple'"). They use a counter variable that increments inside a conditional inside a loop.
Dependencies:
* T10.G3.05: Loop through each item in a list
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor

ID: T10.G3.08
Topic: T10 – Lists & Tables
Skill: Check if a list is empty before accessing
Description: Students check whether a list is empty (has zero items) before trying to read from it, to avoid errors. They use the `length of [list] = 0` condition.
Dependencies:
* T10.G3.03: Get the length of a list
* T08.G3.01: Use a simple if in a script

ID: T10.G3.09
Topic: T10 – Lists & Tables
Skill: Increment or decrement a list item's value
Description: Students use the `change item (position) of [list] by (amount)` block to modify numeric values in a list arithmetically (e.g., increase a player's score by 10, decrease health by 5). They understand this changes the value without needing to manually get-calculate-replace, making score updates and counters much simpler. For young learners who don't know negative numbers, the `reduce item (position) of [list] by (amount)` block provides a simpler way to decrease values.
Dependencies:
* T10.G3.02: Read items from a list by position (index starts at 1)
* T10.G3.04.01: Delete an item at a specific position
* T09.G3.01.02: Increment and decrement a variable

ID: T10.G3.10
Topic: T10 – Lists & Tables
Skill: Display a list monitor on the stage
Description: Enable the list monitor by checking the checkbox next to the list name in the Variables palette. Observe how the monitor displays all items with their positions (1, 2, 3...). Watch it update in real-time as items are added, removed, or changed. Visual feedback is essential for understanding list state and debugging.
Dependencies:
* T10.G3.01.02: Add an item to the end of a list
```

---

### Grade 4 (27 skills) - MAJOR CHANGES
**Changes**: Split T10.G4.06 (statistics) and T10.G4.11 (copy/append) into sub-skills

```
ID: T10.G4.01
Topic: T10 – Lists & Tables
Skill: Find an item's position in a list (linear search)
Description: Students use the `item # of [value] in [list]` block or implement a simple linear search by looping through a list, comparing each item to a target value, and reporting the position when found (or "not found" if the loop completes). This foundational algorithm skill teaches sequential searching.
Dependencies:
* T10.G3.05: Loop through each item in a list
* T08.G3.01: Use a simple if in a script

ID: T10.G4.02
Topic: T10 – Lists & Tables
Skill: Store and retrieve parallel list data
Description: Students use two lists in parallel (e.g., "playerNames" and "playerScores") where items at the same index are related. They add items to both lists together and use the same index to retrieve matching data (e.g., "the player at index 2 in names has the score at index 2 in scores").
Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T10.G3.02: Read items from a list by position (index starts at 1)

ID: T10.G4.03
Topic: T10 – Lists & Tables
Skill: Insert an item at a specific position in a list
Description: Students use the `insert [item] at (position) of [list]` block to add items at the beginning, middle, or end of a list. They understand how existing items shift to make room and practice inserting at specific positions.
Dependencies:
* T10.G3.02: Read items from a list by position (index starts at 1)
* T10.G3.03: Get the length of a list

ID: T10.G4.04
Topic: T10 – Lists & Tables
Skill: Replace an item in a list
Description: Students use the `replace item (position) of [list] with [value]` block to update an existing item without changing the list length. They practice replacing items based on position and understand the difference between replacing (overwrites in place) and inserting (shifts existing items).
Dependencies:
* T10.G3.02: Read items from a list by position (index starts at 1)

ID: T10.G4.05
Topic: T10 – Lists & Tables
Skill: Use built-in blocks to sort a list
Description: Students use CreatiCode's `sort list [list] from [large to small/small to large]` block to sort numeric or alphabetic lists. They observe how the order changes and understand that sorting rearranges items by value.
Dependencies:
* T10.G3.01.02: Add an item to the end of a list

ID: T10.G4.06.01
Topic: T10 – Lists & Tables
Skill: Find the smallest value in a list
Description: Students use the `[smallest v] of list [list]` block to find the minimum value in a numeric list. They understand this scans all items and returns the lowest value. They practice with different lists and predict which value will be returned.
Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T10.G3.03: Get the length of a list

ID: T10.G4.06.02
Topic: T10 – Lists & Tables
Skill: Find the largest value in a list
Description: Students use the `[largest v] of list [list]` block to find the maximum value in a numeric list. They understand this scans all items and returns the highest value. They compare this to finding smallest and understand min/max concepts.
Dependencies:
* T10.G4.06.01: Find the smallest value in a list

ID: T10.G4.06.03
Topic: T10 – Lists & Tables
Skill: Calculate the sum of all values in a list
Description: Students use the `[sum v] of list [list]` block to add up all numeric values in a list. They understand this is useful for totals (total points, total money) and verify results by manual addition with small lists.
Dependencies:
* T10.G4.06.01: Find the smallest value in a list

ID: T10.G4.06.04
Topic: T10 – Lists & Tables
Skill: Calculate the average of values in a list
Description: Students use the `[average v] of list [list]` block to find the mean of all numeric values. They understand average represents typical/middle value and relate it to sum divided by length. They use this for grade averages, temperature averages, etc.
Dependencies:
* T10.G4.06.03: Calculate the sum of all values in a list
* T10.G3.03: Get the length of a list

ID: T10.G4.06.05
Topic: T10 – Lists & Tables
Skill: Find the median value in a list
Description: Students use the `[median v] of list [list]` block to find the middle value when sorted. They understand median differs from average (less affected by outliers) and identify when median is more useful than average (income, test scores with outliers).
Dependencies:
* T10.G4.06.04: Calculate the average of values in a list
* T10.G4.05: Use built-in blocks to sort a list

ID: T10.G4.07
Topic: T10 – Lists & Tables
Skill: Find the maximum or minimum item in a list manually
Description: Students write a loop to find the largest or smallest item in a numeric list without using built-in blocks. They initialize a "best so far" variable with the first item, loop through remaining items comparing each to the current best, and update when a better value is found. This manual algorithm builds understanding of how aggregation works internally.
Dependencies:
* T10.G3.05: Loop through each item in a list
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor

ID: T10.G4.08
Topic: T10 – Lists & Tables
Skill: Filter items from a list based on a condition
Description: Students loop through a list and build a new filtered list containing only items that satisfy a condition (e.g., "keep only scores > 50"). They create an empty result list, use conditionals inside a loop to check each item, and add matching items to the result list.
Dependencies:
* T10.G4.07: Find the maximum or minimum item in a list manually
* T08.G4.01: Use if-else to choose between two actions

ID: T10.G4.09
Topic: T10 – Lists & Tables
Skill: Build a high score list with parallel lists
Description: Students create a leaderboard using two parallel lists (names and scores). When a new score is added, they find the correct position to insert it (to keep scores sorted) and insert both the name and score at matching positions.
Dependencies:
* T10.G4.01: Find an item's position in a list (linear search)
* T10.G4.02: Store and retrieve parallel list data
* T10.G4.03: Insert an item at a specific position in a list

ID: T10.G4.10
Topic: T10 – Lists & Tables
Skill: Swap two items in a list
Description: Students swap the positions of two items in a list using a temporary variable. They store one item temporarily, replace it with the other, then put the temporary value in the second position. This is a building block for sorting algorithms.
Dependencies:
* T10.G4.04: Replace an item in a list
* T09.G3.01.04: Display variable value on stage using the variable monitor

ID: T10.G4.11.01
Topic: T10 – Lists & Tables
Skill: Copy one list to another (replacing contents)
Description: Students use the `copy [list1] to [list2]` block to duplicate a list. They understand this REPLACES all items in list2 with items from list1, so list2's original contents are lost. After copying, both lists have identical items but remain separate (changing one doesn't affect the other).
Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T10.G3.05: Loop through each item in a list

ID: T10.G4.11.02
Topic: T10 – Lists & Tables
Skill: Append one list to another (adding to end)
Description: Students use the `append [list1] to [list2]` block to add all items from list1 to the END of list2. They understand this PRESERVES list2's original items and adds list1's items below them. They compare append vs. copy and identify when each is appropriate.
Dependencies:
* T10.G4.11.01: Copy one list to another (replacing contents)

ID: T10.G4.12
Topic: T10 – Lists & Tables
Skill: Split a text string into a list
Description: Students use the `set [list] to split of [text] with splitter [delimiter]` block to convert text into a list of items (e.g., split "apple,banana,orange" by "," to get a list of three fruits). This introduces text processing and list creation from external data.
Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T09.G4.01: Store and compare text strings in variables

ID: T10.G4.13
Topic: T10 – Lists & Tables
Skill: Join list items into a text string
Description: Students use the `join [list] into text with [delimiter]` block to combine list items into a single text string (e.g., join ["red", "green", "blue"] with ", " to get "red, green, blue"). This is useful for displaying or saving list data.
Dependencies:
* T10.G4.12: Split a text string into a list
* T09.G4.01: Store and compare text strings in variables

ID: T10.G4.14
Topic: T10 – Lists & Tables
Skill: Reverse the order of items in a list
Description: Students use the `reverse [list]` block to flip item order (first becomes last, last becomes first). They observe the list monitor to see position changes and understand when reversing is useful: converting ascending to descending order, reversing time sequences, or inverting rankings.
Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T10.G3.02: Read items from a list by position (index starts at 1)

ID: T10.G4.15
Topic: T10 – Lists & Tables
Skill: Randomly shuffle items in a list
Description: Students use the `reshuffle [list] randomly` block to randomly rearrange all items. Each shuffle produces a different random order. They use this for games: shuffling cards, randomizing quiz questions, or creating random starting positions. They understand that reshuffling destroys the original order.
Dependencies:
* T10.G3.01.02: Add an item to the end of a list

ID: T10.G4.16
Topic: T10 – Lists & Tables
Skill: Generate a list of random numbers
Description: Students use the `set [list] to (N) random whole numbers between (min) and (max) [no repetition/allow repetition]` block to populate a list with random values. They choose whether to allow duplicate numbers and use this for generating test data, simulating dice rolls, or creating random scores. They also explore the seeded random block `set [list] to (N) random numbers with seed (SEED)` which generates the same sequence when using the same seed (useful for reproducible randomness in games).
Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T10.G3.03: Get the length of a list
* T08.G4.01: Use if-else to choose between two actions

ID: T10.G4.17
Topic: T10 – Lists & Tables
Skill: Delete an item from a list by value
Description: Students use the `delete value [item] from [list]` block to remove the first occurrence of a specific value (e.g., delete "apple" from the fruits list). They understand this finds and removes the item without needing to know its position, which is different from deleting by index.
Dependencies:
* T10.G3.04.01: Delete an item at a specific position
* T10.G3.06: Check if a list contains a specific item

ID: T10.G4.18
Topic: T10 – Lists & Tables
Skill: Loop through list indices
Description: Students use the `for each index [i] in [list]` block to iterate through list positions (1, 2, 3...) instead of values. They use this when they need to know both the position and the value, or when they need to modify items while looping.
Dependencies:
* T10.G3.05: Loop through each item in a list
* T10.G3.02: Read items from a list by position (index starts at 1)
* T07.G4.01: Use nested loops

ID: T10.G4.19
Topic: T10 – Lists & Tables
Skill: Find an item containing a substring
Description: Students use the `# of item containing [substring] in [list]` block to find the first list item that includes a partial match (e.g., find first name containing "son" in a names list). They compare this to exact matching and understand when partial matching is useful.
Dependencies:
* T10.G4.01: Find an item's position in a list (linear search)
* T09.G4.01: Store and compare text strings in variables
* T09.G4.02: Use text operations (join, split, substring, case conversion)

ID: T10.G4.20
Topic: T10 – Lists & Tables
Skill: Select multiple items from a list by criteria
Description: Students use the `insert (N) [largest/smallest/random] items from [list1] into [list2]` block to extract top/bottom/random items efficiently. They use this for leaderboards (top 10 scores), random sampling (pick 5 random quiz questions), or filtering extremes (3 coldest days).
Dependencies:
* T10.G4.05: Use built-in blocks to sort a list
* T10.G4.06.01: Find the smallest value in a list
* T10.G4.11.02: Append one list to another (adding to end)
```

---

### Grade 5 (21 skills) - MAJOR CHANGES
**Changes**: Split T10.G5.06 (row count/find row), T10.G5.09 (delete rows), T10.G5.11 (manage columns)

```
ID: T10.G5.01
Topic: T10 – Lists & Tables
Skill: Understand table structure (rows, columns, cells)
Description: Students identify and label the parts of a table: rows (horizontal, numbered), columns (vertical, named), and cells (values at row-column intersections). Given a sample table, they state the number of rows and columns, identify the value at a specific row-column intersection, and explain that each row represents one record while each column represents one attribute. Students understand that a table is like having multiple parallel lists (one list per column) organized together, where all lists have the same length and items at the same position are related. A table makes it easier to manage related data than using many separate parallel lists.
Dependencies:
* T10.G4.02: Store and retrieve parallel list data

ID: T10.G5.02
Topic: T10 – Lists & Tables
Skill: Create a table and add columns
Description: Students create an empty table variable and use `add column [name] at position (n) to table [table]` to define the table structure. They understand that columns must be created before data can be added to them, and they can control column order using the position parameter (1 = first column, 2 = second, etc.).
Dependencies:
* T10.G5.01: Understand table structure (rows, columns, cells)

ID: T10.G5.03
Topic: T10 – Lists & Tables
Skill: Add rows of data to a table
Description: Students use the `add to table [table]: [value1] [value2] ...` block to add rows of data. They ensure the number of values matches the number of columns and understand that rows are numbered starting from 1.
Dependencies:
* T10.G5.02: Create a table and add columns

ID: T10.G5.04
Topic: T10 – Lists & Tables
Skill: Read a cell value from a table
Description: Students use the `item at row (n) column [name] of table [table]` block to retrieve a specific value. They practice reading different cells and using the values in their programs.
Dependencies:
* T10.G5.03: Add rows of data to a table

ID: T10.G5.05
Topic: T10 – Lists & Tables
Skill: Update a cell value in a table
Description: Students use the `replace item at row (n) column [name] of table [table] with [value]` block to modify existing data. They update cells based on position and understand this changes the table in place.
Dependencies:
* T10.G5.04: Read a cell value from a table

ID: T10.G5.06.01
Topic: T10 – Lists & Tables
Skill: Get the number of rows in a table
Description: Students use the `row count of table [table]` block to find how many rows exist in a table. They understand this is essential for loops (iterate from 1 to row count), checking if table is empty (row count = 0), and reporting table size.
Dependencies:
* T10.G5.04: Read a cell value from a table

ID: T10.G5.06.02
Topic: T10 – Lists & Tables
Skill: Find which row contains a value
Description: Students use the `row # of [value] in column [name] in table [table]` block to search for the first row where a specific column equals a value. They understand this returns the row number (index) or 0 if not found, enabling them to locate data for reading or updating.
Dependencies:
* T10.G5.06.01: Get the number of rows in a table
* T10.G4.01: Find an item's position in a list (linear search)

ID: T10.G5.07
Topic: T10 – Lists & Tables
Skill: Loop through table rows to compute aggregates
Description: Students use a counted loop from 1 to `row count of table` to iterate through all rows. They access values in a specific column and compute totals (sum), counts, or find maximum/minimum values using a variable accumulator.
Dependencies:
* T07.G3.01: Use a counted repeat loop
* T10.G5.06.01: Get the number of rows in a table
* T09.G3.01.04: Display variable value on stage using the variable monitor

ID: T10.G5.08
Topic: T10 – Lists & Tables
Skill: Use built-in table aggregate blocks
Description: Students use CreatiCode's `[sum/average/smallest/largest/median] of column [name] in table [table]` blocks to compute statistics on a column without writing a loop. They compare this to manual aggregation using loops from the previous skill.
Dependencies:
* T10.G5.07: Loop through table rows to compute aggregates
* T10.G4.06.01: Find the smallest value in a list

ID: T10.G5.09.01
Topic: T10 – Lists & Tables
Skill: Delete a single row by index
Description: Students use the `delete row (n) of table [table]` block to remove a specific row by its position number. They observe how remaining rows shift up (row 4 becomes row 3) and understand the row count decreases by 1.
Dependencies:
* T10.G5.06.01: Get the number of rows in a table

ID: T10.G5.09.02
Topic: T10 – Lists & Tables
Skill: Delete rows matching a condition
Description: Students use the `delete rows with column [name] of value [v] from table [table]` block to remove ALL rows where a specific column equals a value. They understand this can delete multiple rows at once (e.g., delete all students in grade 8) and is more efficient than looping to delete one by one.
Dependencies:
* T10.G5.09.01: Delete a single row by index
* T10.G5.06.02: Find which row contains a value

ID: T10.G5.09.03
Topic: T10 – Lists & Tables
Skill: Clear all rows from a table
Description: Students use the `delete all rows from table [table]` block to remove all data while preserving the column structure. They understand this is useful for resetting a table for new data without recreating columns, and compare this to deleting entire table vs. just clearing data.
Dependencies:
* T10.G5.09.01: Delete a single row by index

ID: T10.G5.10
Topic: T10 – Lists & Tables
Skill: Convert between lists and tables
Description: Students convert a list into a single-column table using available table operations and extract a column from a table into a list by looping through rows (or using a dedicated block if available). They understand when each data structure is more appropriate.
Dependencies:
* T10.G5.03: Add rows of data to a table
* T10.G3.01.02: Add an item to the end of a list

ID: T10.G5.11.01
Topic: T10 – Lists & Tables
Skill: Add a column at a specific position
Description: Students use the `add column [name] at position (n) to table [table]` block to insert a new column at a specific position (1 = first column, 2 = second, etc.). They understand existing columns shift right to make room, and the new column starts empty. They practice adding columns at beginning, middle, and end.
Dependencies:
* T10.G5.02: Create a table and add columns

ID: T10.G5.11.02
Topic: T10 – Lists & Tables
Skill: Delete a single column
Description: Students use the `delete column [name] from table [table]` block to permanently remove a column and ALL its data. They understand this cannot be undone, remaining columns shift left, and the table structure changes. They identify when column deletion is appropriate vs. just clearing cell values.
Dependencies:
* T10.G5.11.01: Add a column at a specific position
* T10.G5.03: Add rows of data to a table

ID: T10.G5.11.03
Topic: T10 – Lists & Tables
Skill: Remove all columns from a table
Description: Students use the `delete all columns from table [table]` block to completely reset a table to empty structure (no columns, no rows). They understand this is more destructive than deleting all rows (which keeps columns) and use this when completely restructuring a table.
Dependencies:
* T10.G5.11.02: Delete a single column

ID: T10.G5.12
Topic: T10 – Lists & Tables
Skill: Copy list data to table column
Description: Students use the `copy list [list] to column [name] of table [table]` block to populate or replace an entire column with list values. They understand this requires the column to already exist and will overwrite existing data in that column.
Dependencies:
* T10.G5.02: Create a table and add columns
* T10.G3.01.02: Add an item to the end of a list
* T10.G5.10: Convert between lists and tables

ID: T10.G5.13
Topic: T10 – Lists & Tables
Skill: Insert a row at a specific position
Description: Students use `insert at row (n) of table [table]: [cell1] [cell2] ...` to add a row at a specific position, shifting existing rows down. They understand the difference between appending (always adds at end) and inserting (can add anywhere).
Dependencies:
* T10.G5.03: Add rows of data to a table
* T10.G4.03: Insert an item at a specific position in a list

ID: T10.G5.14
Topic: T10 – Lists & Tables
Skill: Replace an entire row in a table
Description: Students use `replace row (n) of table [table] with: [cell1] [cell2] ...` to overwrite all values in a row at once. They compare this to updating individual cells (T10.G5.05) and understand when replacing entire rows is more efficient.
Dependencies:
* T10.G5.05: Update a cell value in a table
* T10.G5.03: Add rows of data to a table

ID: T10.G5.15
Topic: T10 – Lists & Tables
Skill: Get an entire row as a text string
Description: Students use `row (n) of table [table] separator [sep]` to extract all values from a row as a single text string with specified separator. They use this to display row data, save row snapshots, or pass row data to other parts of the program. They understand this returns text (e.g., "apple,banana,orange"), not a list data structure.
Dependencies:
* T10.G5.04: Read a cell value from a table
* T10.G5.10: Convert between lists and tables
* T10.G4.12: Split a text string into a list

ID: T10.G5.16
Topic: T10 – Lists & Tables
Skill: Find a row by partial match
Description: Students use `row # of item containing [substring] in column [name] in table [table]` to find the first row where a column value includes a substring (e.g., find student with "son" in last name). They compare exact vs partial matching.
Dependencies:
* T10.G5.06.02: Find which row contains a value
* T10.G4.19: Find an item containing a substring
* T09.G4.02: Use text operations (join, split, substring, case conversion)

ID: T10.G5.17
Topic: T10 – Lists & Tables
Skill: Increment or decrement a table cell value
Description: Students use `change item at row (n) column [name] of table [table] by (amount)` to modify numeric cell values arithmetically (e.g., increase a player's score by 10, decrease inventory by 3). For young learners, the `reduce item at row (n) column [name] of table [table] by (amount)` block provides a simpler way to decrease values without negative numbers. They compare this to replacement (T10.G5.05) and understand when arithmetic modification is more efficient than get-calculate-replace patterns.
Dependencies:
* T10.G5.05: Update a cell value in a table
* T10.G5.04: Read a cell value from a table
* T10.G3.09: Increment or decrement a list item's value

ID: T10.G5.18
Topic: T10 – Lists & Tables
Skill: Show and hide table monitors
Description: Students use `show table [table]` and `hide table [table]` blocks to display or hide the table monitor on the stage. They use this to debug their programs, show results to users, or hide implementation details.
Dependencies:
* T10.G5.02: Create a table and add columns
* T09.G3.01.04: Display variable value on stage using the variable monitor
```

---

### Grade 6 (8 skills) - NO CHANGES
All G6 skills are appropriately scoped.

```
ID: T10.G6.01
Topic: T10 – Lists & Tables
Skill: Sort a table by a column
Description: Students use CreatiCode's `sort table [table] by column [name] [large to small/small to large]` block to reorder rows based on values in a column. They understand sorting preserves row integrity (all columns in a row stay together). Students verify the sort worked by reading cell values before and after.
Dependencies:
* T10.G4.05: Use built-in blocks to sort a list
* T10.G5.04: Read a cell value from a table

ID: T10.G6.02
Topic: T10 – Lists & Tables
Skill: Filter table rows based on a condition
Description: Students loop through a table and identify rows where a column value meets a condition (e.g., "find all students with score > 80"). They either collect matching row numbers or build a new filtered table with matching rows.
Dependencies:
* T10.G5.07: Loop through table rows to compute aggregates
* T08.G4.01: Use if-else to choose between two actions

ID: T10.G6.03
Topic: T10 – Lists & Tables
Skill: Copy and append tables
Description: Students use `copy table [t1] into [t2]` to duplicate a table and `append table [t1] to [t2]` to combine tables vertically. Vertical appending adds new rows below existing rows; both tables must have matching columns for append to work correctly.
Dependencies:
* T10.G5.03: Add rows of data to a table

ID: T10.G6.04
Topic: T10 – Lists & Tables
Skill: Use table lookup to find related data
Description: Students use the `item in column [return_col] of [table] where column [search_col] equals [value]` block to look up data. For example, find a student's grade by looking up their name, similar to VLOOKUP in spreadsheets.
Dependencies:
* T10.G5.06.02: Find which row contains a value
* T10.G5.04: Read a cell value from a table

ID: T10.G6.05
Topic: T10 – Lists & Tables
Skill: Group data and compute aggregates per group
Description: Students use CreatiCode's `set table [result] to [method] of column [value_col] in table [source] by column [group_col]` block to group rows by a category and compute statistics (sum, average, count) for each group, creating a summary table.
Dependencies:
* T10.G5.08: Use built-in table aggregate blocks
* T10.G6.02: Filter table rows based on a condition

ID: T10.G6.06
Topic: T10 – Lists & Tables
Skill: Use set operations on lists
Description: Students implement set operations like union (all unique items from both lists), intersection (only items in both lists), and difference (items in list1 but not list2) using loops and conditionals. They understand mathematical set concepts applied to lists.
Dependencies:
* T10.G4.08: Filter items from a list based on a condition
* T10.G3.06: Check if a list contains a specific item

ID: T10.G6.07
Topic: T10 – Lists & Tables
Skill: Remove duplicate items from a list
Description: Students write code to remove duplicate values from a list, keeping only one instance of each unique value. They loop through the list, check if each item already exists in a result list, and add only unique items.
Dependencies:
* T10.G3.06: Check if a list contains a specific item
* T10.G4.08: Filter items from a list based on a condition

ID: T10.G6.08
Topic: T10 – Lists & Tables
Skill: Shuffle table rows randomly
Description: Students use the `reshuffle table [table] randomly` block to randomize row order while keeping row integrity (all columns in a row stay together). They use this for randomizing quiz questions stored in tables, shuffling game data, or anonymizing datasets.
Dependencies:
* T10.G4.15: Randomly shuffle items in a list
* T10.G5.03: Add rows of data to a table
```

---

### Grade 7 (14 skills) - NO CHANGES
All G7 skills are appropriately scoped for advanced data operations.

```
ID: T10.G7.01
Topic: T10 – Lists & Tables
Skill: Pivot or reshape table data
Description: Students use CreatiCode's `pivot [source] into [result] row groups [cols] columns [values] methods [methods]` block to reshape data from "long" format (many rows, few columns) to "wide" format (fewer rows, more columns) or vice versa, preparing data for different types of analysis.
Dependencies:
* T10.G6.05: Group data and compute aggregates per group

ID: T10.G7.02
Topic: T10 – Lists & Tables
Skill: Import external data into a table
Description: Students use the `import file into table [table]` block to load data from an external CSV file into a table. They understand file formats, handle the imported structure, and verify the data loaded correctly.
Dependencies:
* T10.G5.02: Create a table and add columns
* T10.G5.04: Read a cell value from a table

ID: T10.G7.03
Topic: T10 – Lists & Tables
Skill: Design a table schema for a real-world scenario
Description: Students design the structure of a table (what columns to include, what data types they hold) to model a real-world domain. They create a table with appropriate column names, justify their design choices (why these columns? what data type?), and demonstrate by populating the table with sample data that validates their design. Example domains: Library catalog (columns: title, author, ISBN, genre, available_copies); Game inventory (item_name, item_type, quantity, value, rarity); Sports statistics (player_name, team, position, points, assists).
Dependencies:
* T10.G5.02: Create a table and add columns
* T09.G5.01: Create multiple related variables for complex state

ID: T10.G7.04
Topic: T10 – Lists & Tables
Skill: Visualize table data with charts
Description: Students use CreatiCode's chart blocks like `draw [line/bar/pie] chart using columns [...] from table [table]` to create visual representations of their data. They also use `draw [type] chart using category column [col1] value column [col2] from table [table]` for categorical data visualization (e.g., bar chart of sales by region, pie chart of votes by candidate). They choose appropriate chart types: line charts for trends over time, bar charts for comparing categories, and pie charts for showing proportions of a whole.
Dependencies:
* T10.G5.08: Use built-in table aggregate blocks
* T10.G6.05: Group data and compute aggregates per group

ID: T10.G7.05
Topic: T10 – Lists & Tables
Skill: Clean and transform table data
Description: Students apply data cleaning transformations to improve data quality: trim whitespace from text, standardize text case (uppercase/lowercase), remove or replace invalid characters, and standardize formats (e.g., date formats, phone numbers). They write loops to process each row and apply these transformations. Example transformations: Trim whitespace (join/split by space), standardize case (lowercase/uppercase blocks), remove invalid characters (replace non-alphanumeric), handle missing values (replace empty with defaults like 0 or "N/A"), validate ranges (check if numeric values are within expected bounds).
Dependencies:
* T10.G5.05: Update a cell value in a table
* T10.G5.07: Loop through table rows to compute aggregates
* T08.G5.01: Use compound conditions with and/or/not

ID: T10.G7.06
Topic: T10 – Lists & Tables
Skill: Validate and handle missing data in tables
Description: Students detect data quality issues: missing values (empty cells), out-of-range values (e.g., age > 150), and invalid data types (text in numeric columns). They implement validation rules and handle issues by: replacing missing values with defaults (e.g., 0 or "N/A"), deleting invalid rows, or marking rows for manual review.
Dependencies:
* T10.G7.05: Clean and transform table data
* T10.G5.09.01: Delete a single row by index
* T08.G5.01: Use compound conditions with and/or/not

ID: T10.G7.07
Topic: T10 – Lists & Tables
Skill: Analyze a dataset to find patterns or outliers
Description: Students examine a table of data and write code to find patterns (e.g., the most frequent value, trends over time) or identify outliers (values much larger/smaller than typical). They use aggregates, sorting, and conditionals to discover insights.
Dependencies:
* T10.G6.05: Group data and compute aggregates per group
* T10.G6.01: Sort a table by a column
* T08.G5.01: Use compound conditions with and/or/not

ID: T10.G7.08
Topic: T10 – Lists & Tables
Skill: Use regex patterns to find items in lists
Description: Students use regular expression patterns to find items in lists that match complex text patterns (e.g., "find all emails," "find all phone numbers," "find all codes starting with A"). They implement pattern matching using regex blocks if available or manual string checking.
Dependencies:
* T10.G4.08: Filter items from a list based on a condition
* T09.G6.02: Use text operations (join, split, substring, case conversion)

ID: T10.G7.09
Topic: T10 – Lists & Tables
Skill: Read and write data with Google Sheets
Description: Students use `read from google sheet: url [url] sheet name [name] range [range] into table [table]` and `write into google sheet: url [url] sheet name [name] start cell [cell] from table [table]` to sync data with Google Sheets. They also use `list all sheets in google sheet at URL [url] into list [list]` to get names of all sheets in a spreadsheet for dynamic sheet selection. They learn to set up sharing, use proper URLs, and handle authentication.
Dependencies:
* T10.G7.02: Import external data into a table
* T10.G5.03: Add rows of data to a table

ID: T10.G7.10
Topic: T10 – Lists & Tables
Skill: Manage Google Sheets structure
Description: Students use `add sheet [name] to google sheet at URL [url]`, `remove sheet [name]`, `insert [n] columns/rows in sheet [name]`, `remove [n] columns/rows from sheet [name]`, and `clear sheet [name] in google sheet at URL [url]` to programmatically manage spreadsheet structure. They understand when to modify structure vs. data.
Dependencies:
* T10.G7.09: Read and write data with Google Sheets
* T10.G5.11.01: Add a column at a specific position

ID: T10.G7.11
Topic: T10 – Lists & Tables
Skill: Display formatted table snapshots
Description: Students use `show snapshot of table [table] from row (start) to (end) with style [style] [color]` to create professionally formatted table displays with styling and color themes. They use this for presenting data in projects, creating reports, or showing partial table views.
Dependencies:
* T10.G5.18: Show and hide table monitors
* T10.G7.04: Visualize table data with charts

ID: T10.G7.12
Topic: T10 – Lists & Tables
Skill: Export table data to a file
Description: Students use `export table [table] as [filename]` to save table data as a downloadable CSV file. They understand CSV format (comma-separated values), when to export data (sharing results, backup, analysis in other tools), and how file export complements data import.
Dependencies:
* T10.G7.02: Import external data into a table
* T10.G5.02: Create a table and add columns

ID: T10.G7.13
Topic: T10 – Lists & Tables
Skill: Save and load data to the cloud
Description: Students use `save table [table] to server as [dataname]` and `load [dataname] from server into table [table]` to store and retrieve table data on CreatiCode's cloud server. They understand this enables data persistence (save progress, reload later), multi-session projects, and simple data sharing without Google Sheets integration.
Dependencies:
* T10.G7.02: Import external data into a table
* T10.G7.09: Read and write data with Google Sheets

ID: T10.G7.14
Topic: T10 – Lists & Tables
Skill: Use AI to analyze table data
Description: Students use CreatiCode's AI blocks to ask questions about table data (e.g., "What are the key insights from this sales data?" or "Summarize the trends in this dataset"). They learn how AI can assist with data analysis.
Dependencies:
* T10.G7.07: Analyze a dataset to find patterns or outliers
* T10.G5.08: Use built-in table aggregate blocks
```

---

### Grade 8 (8 skills) - NO CHANGES
All G8 skills are appropriately scoped for advanced algorithms.

```
ID: T10.G8.01
Topic: T10 – Lists & Tables
Skill: Use nested loops to compare data across two tables
Description: Students write nested loops to analyze relationships between two tables (e.g., matching orders to customers, finding common elements). The outer loop iterates through one table while the inner loop searches the other table for matches.
Dependencies:
* T07.G5.01: Use conditional loops for searching
* T10.G6.04: Use table lookup to find related data

ID: T10.G8.02
Topic: T10 – Lists & Tables
Skill: Implement bubble sort algorithm step by step
Description: Students implement bubble sort by writing nested loops: the outer loop controls passes, the inner loop compares adjacent items and swaps if out of order. They trace through the algorithm to understand how items "bubble" to their correct positions.
Dependencies:
* T10.G4.10: Swap two items in a list
* T07.G6.01: Trace nested loops with variable bounds

ID: T10.G8.03
Topic: T10 – Lists & Tables
Skill: Implement selection sort algorithm step by step
Description: Students implement selection sort by writing nested loops: the outer loop selects each position, the inner loop finds the minimum remaining element. They understand that selection sort makes fewer swaps than bubble sort.
Dependencies:
* T10.G8.02: Implement bubble sort algorithm step by step
* T10.G4.07: Find the maximum or minimum item in a list manually

ID: T10.G8.04
Topic: T10 – Lists & Tables
Skill: Build a simulation using table-based state
Description: Students create a simulation (e.g., a game with multiple entities, a population model, an ecosystem) where entities and their properties are stored in a table. Each simulation step loops through rows to update values based on rules.
Dependencies:
* T10.G7.03: Design a table schema for a real-world scenario
* T10.G5.07: Loop through table rows to compute aggregates
* T09.G6.01: Model real-world quantities using variables and formulas

ID: T10.G8.05
Topic: T10 – Lists & Tables
Skill: Query and report statistics from a complex dataset
Description: Students work with a realistic multi-column table (e.g., weather data, sports statistics, survey results) and write code to answer analytical questions: compute means, find percentiles, compare groups, identify trends, and format results as a report.
Dependencies:
* T10.G7.07: Analyze a dataset to find patterns or outliers
* T10.G6.01: Sort a table by a column

ID: T10.G8.06
Topic: T10 – Lists & Tables
Skill: Model relationships using multiple linked tables
Description: Students design and use multiple tables that reference each other (e.g., a Students table and a Grades table linked by student ID). They write code to perform lookups across tables to answer queries like "What are all grades for student X?"
Dependencies:
* T10.G8.01: Use nested loops to compare data across two tables
* T10.G7.03: Design a table schema for a real-world scenario

ID: T10.G8.07
Topic: T10 – Lists & Tables
Skill: Implement a hash table lookup using lists
Description: Students simulate a simple hash table by using a list where each position corresponds to a hash value computed using modulo operation (e.g., hash(key) = key mod list_length for numbers, or sum of character codes mod list_length for strings). They handle collisions using linear probing (check next positions) or chaining (store multiple items at one position using lists within lists). Implementation pattern: Use a list as the hash table, create a hash function using math operators and string blocks, use linear search as fallback for collisions, and compare performance to linear search to demonstrate the principle of constant-time lookup.
Dependencies:
* T10.G8.03: Implement selection sort algorithm step by step
* T10.G4.02: Store and retrieve parallel list data
* T09.G7.01: Compare computational efficiency of different approaches

ID: T10.G8.08
Topic: T10 – Lists & Tables
Skill: Use advanced list operations for algorithm optimization
Description: Students apply advanced list techniques like binary search on sorted lists, two-pointer techniques, or sliding window algorithms to solve problems more efficiently than brute force approaches.
Dependencies:
* T10.G8.02: Implement bubble sort algorithm step by step
* T09.G7.01: Compare computational efficiency of different approaches
```

---

## 7. Summary of Changes

### Skills to Split (7 skills → 23 skills)

1. **T10.G3.01** → T10.G3.01.01, T10.G3.01.02 (2 skills)
2. **T10.G3.04** → T10.G3.04.01, T10.G3.04.02 (2 skills)
3. **T10.G4.06** → T10.G4.06.01-05 (5 skills)
4. **T10.G4.11** → T10.G4.11.01, T10.G4.11.02 (2 skills)
5. **T10.G5.06** → T10.G5.06.01, T10.G5.06.02 (2 skills)
6. **T10.G5.09** → T10.G5.09.01-03 (3 skills)
7. **T10.G5.11** → T10.G5.11.01-03 (3 skills)

**Net change**: +16 skills (7 removed, 23 added)

### Total Skill Count

- **Before**: 96 skills
- **After**: 112 skills
- **Increase**: +16 skills

### Distribution by Grade

| Grade | Before | After | Change |
|-------|--------|-------|--------|
| K     | 8      | 8     | 0      |
| 1     | 6      | 6     | 0      |
| 2     | 7      | 7     | 0      |
| 3     | 10     | 12    | +2     |
| 4     | 20     | 27    | +7     |
| 5     | 18     | 21    | +3     |
| 6     | 8      | 8     | 0      |
| 7     | 14     | 14    | 0      |
| 8     | 8      | 8     | 0      |
| **Total** | **96** | **112** | **+16** |

---

## 8. Verification Checklist

### Completed Verifications
- ✅ All K-2 skills are picture-based (no coding)
- ✅ Each broad skill covering multiple blocks has been split
- ✅ Dependencies use X-2 rule (spot checked)
- ✅ Each fundamental list/table block has a dedicated skill
- ✅ Skills progress logically within each grade
- ✅ Sub-skill IDs follow format (e.g., T10.G3.01.01)

### Recommended Further Verifications
- ⚠️ Verify blocks mentioned in T10.G6.06-07 exist (set operations, unique items)
- ⚠️ Verify T10.G5.10 "get column as list" block exists
- ⚠️ Full dependency check for X-2 rule violations
- ⚠️ Verify all block syntaxes match CreatiCode exactly

---

## 9. Implementation Notes

### For Curriculum Developers
1. Update allskills.md with new skill IDs and descriptions
2. Update any cross-references in other topics (T09, T07, T08 dependencies)
3. Create assessment items for each new sub-skill
4. Update student-facing documentation to reflect granular skills

### For Platform Developers
1. Ensure all referenced blocks are available and match described syntax
2. Add missing blocks if they don't exist (set operations, unique items, column to list)
3. Verify block documentation in blockdes8.txt is complete
4. Consider adding tooltips/help for each block matching skill descriptions

### For Teachers
1. The increased granularity provides better checkpoints for student progress
2. Each sub-skill can be taught as a mini-lesson (15-20 minutes)
3. Students can now master one specific block before moving to the next
4. Assessment becomes more precise (can identify exactly which operation a student struggles with)

---

## End of Analysis
