# COMPLETE ANALYSIS: CreatiCode Variable-Related Blocks
## Comprehensive Reference for T09 Skills Verification

**Date:** 2025-11-25
**Source:** `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`

---

## EXECUTIVE SUMMARY

CreatiCode offers **90 variable-related blocks** across 3 categories:
- **Variables Category**: 59 blocks
- **Operators Category**: 30 blocks
- **Control Category**: 1 block (for-loop with variable)

### Key Feature Areas:
1. **Tables** - 34 blocks (major feature, not in standard Scratch)
2. **Lists** - 18 blocks (enhanced beyond standard Scratch)
3. **String Operations** - 15 blocks (extensive text manipulation)
4. **Regular Expressions** - 5 blocks (advanced pattern matching)
5. **Cloud Storage** - 4 blocks (server data persistence)
6. **Mathematical** - 6 blocks (equations, expressions, noise, averages)
7. **Basic Variables** - 3 blocks (set, change, reduce, import/export)

---

## CATEGORY 1: VARIABLES (59 BLOCKS)

### 1.1 BASIC VARIABLE OPERATIONS (3 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_reducevariableby | `reduce [VARIABLE v] by (N)` | Reduces variable by N (simpler for young learners than negative numbers) |
| data_exportvariable | `export variable [VARIABLE v]` | Exports variable content to txt file with variable name |
| data_importvariable | `import variable [VARIABLE v]` | Opens dialog to import txt/csv file into variable |

### 1.2 LIST OPERATIONS - BASIC MANIPULATION (10 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_reduceitemoflist | `reduce item (INDEX) of [LISTNAME v] by (N)` | Reduces list item by N |
| data_changeitemoflist | `change item (INDEX) of [LISTNAME v] by (N)` | Changes list item by N |
| data_deletevalueoflist | `delete value [V] from [LISTNAME v]` | Deletes first item with given value |
| data_reverselist | `reverse [LISTNAME v]` | Reverses order of all items |
| data_reshuffle | `reshuffle [LISTNAME v] randomly` | Randomly shuffles items |
| data_sortlistby | `sort list [LISTNAME v] from [METHOD v]` | Sorts 'large to small' or 'small to large' |
| data_insertitemsfromlist | `insert (N) [SELECTOR v] items from [LISTNAME1 v] into [LISTNAME2 v]` | Inserts N items (largest/smallest/random) from list1 to list2 |
| data_copytolist | `copy [LISTNAME1 v] to [LISTNAME2 v]` | Copies all items (replaces destination) |
| data_appendtolist | `append [LISTNAME1 v] to [LISTNAME2 v]` | Appends all items to end of list2 |
| data_setlisttocolumn | (syntax not shown) | Sets list to table column |

### 1.3 LIST OPERATIONS - TEXT & CONVERSION (2 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_joinlistwith | `join [LISTNAME v] into text with [SEPARATOR]` | Reporter: joins items into text (e.g., 'a,b,c') |
| data_set_list_to_split_of | `set [LISTNAME v] to split of [TEXT] with splitter [SEPARATOR]` | Splits text by separator into list |

### 1.4 LIST OPERATIONS - RANDOM & SEEDED (2 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_setrandomlist | `set [LISTNAME v] to (N) random whole numbers between (MIN) and (MAX) [REPEATMETHOD v]` | Populates with random numbers (with/without repetition) |
| data_setrandomlistseed | `set [LISTNAME v] to (N) random numbers with seed (SEED)` | Populates with seeded random numbers 0-1 (same seed = same sequence) |

### 1.5 LIST OPERATIONS - SEARCH & AGGREGATION (2 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_itemnumoflist2 | `# of item containing [TEXT] in [LISTNAME v]` | Reporter: returns position of first item containing substring |
| data_itemspecificvalueoflist | `[METHOD v] of list [LISTNAME v]` | Reporter: returns smallest/largest/sum/average/median of list |

### 1.6 LIST OPERATIONS - ITERATION (2 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_for_each | `for each item [VARIABLENAME v] in [LISTNAME v]` | C-block: variable takes value of each item |
| data_for_each_index | `for each index [INDEXVARIABLENAME v] in [LISTNAME v]` | C-block: variable takes index of each item (starts at 1) |

### 1.7 CLOUD/SERVER DATA STORAGE (4 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_savedata | `save [VISIBILITY v] data [VALUE] with name [KEY]` | Saves data to server (public/private) for current project |
| data_removedata | `remove [VISIBILITY v] data named [KEY]` | Removes data from server (public/private) |
| data_loaddata | `load data named [KEY]` | Reporter: loads data by key (respects privacy) |
| data_load_data_names | `data names` | Reporter: returns all data names separated by '&&' |

### 1.8 TABLE STRUCTURE - CREATE & DELETE (4 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_removeallcolumnsfromtable | `delete all columns from table [TABLENAME v]` | Deletes all columns (empties entire table) |
| data_addcolatposition | `add column [COLUMNNAME] at position (POSITION) to table [TABLENAME v]` | Adds column at position (1 = first) |
| data_deletecolumnfromtable | `delete column [COLUMNNAME] from table [TABLENAME v]` | Deletes specific column by name |
| data_deleteallrowsoftable | `delete all rows from table [TABLENAME v]` | Deletes all rows (keeps column structure) |

### 1.9 TABLE ROWS - ADD & MODIFY (4 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_addrowtotable | `add to table [TABLENAME v]: [CELL1] [CELL2] ... [CELL12]` | Appends row at bottom (max 12 cells) |
| data_insertrowtotable | `insert at row (ROWNUM) of table [TABLENAME v]: [CELL1] ... [CELL12]` | Inserts row at position (1 = first row) |
| data_replacerowoftable | `replace row (ROWNUM) of table [TABLENAME v] with: [CELL1] ... [CELL12]` | Replaces entire row |
| data_deleterowoftable | `delete row (ROWNUM) of table [TABLENAME v]` | Deletes row by index (shifts rows up) |

### 1.10 TABLE ROWS - SEARCH & DELETE (2 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_deleterowwithcondition | `delete rows with column [COLUMN] of value [VALUE] from table [TABLENAME v]` | Deletes all rows where column equals value |
| data_rowatindexoftable | `row (ROWINDEX) of table [TABLENAME v] separator [SEPARATOR]` | Reporter: returns row as joined text |

### 1.11 TABLE ROWS - FIND (2 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_rowindexwithcondition | `row # of [VALUE] in column [COLUMN] in table [TABLENAME v]` | Reporter: returns row index of exact value (-1 if not found) |
| data_rowindexwithcondition2 | `row # of item containing [SUBSTRING] in column [COLUMN] in table [TABLENAME v]` | Reporter: returns row index containing substring (-1 if not found) |

### 1.12 TABLE CELLS - MODIFY (3 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_replaceitematrowcolumn | `replace item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] with [VALUE]` | Replaces cell value |
| data_reduceitematrowcolumn | `reduce item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)` | Reduces cell value by amount |
| data_changeitematrowcolumn | `change item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)` | Changes cell value by amount |

### 1.13 TABLE CELLS - READ (2 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_rowcountoftable | `row count of table [TABLENAME v]` | Reporter: returns total row count |
| data_itematrowcolumnoftable | `item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v]` | Reporter: returns cell value |

### 1.14 TABLE AGGREGATION (2 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_computetable | `[METHOD] of column [COLUMNNAME] in table [TABLE v]` | Reporter: aggregates column (smallest/largest/sum/average/median) |
| data_lookuptable | `item in column [RETURNCOLUMN] of [TABLENAME v] where column [SEARCHCOLUMN] equals [SEARCHTEXT]` | Reporter: VLOOKUP-style function |

### 1.15 TABLE TRANSFORMATIONS (6 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_settabletocomputed | `set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2]` | Aggregates data grouped by column (like SQL GROUP BY) |
| data_reshuffletable | `reshuffle table [TABLENAME v] randomly` | Randomly shuffles all rows |
| data_sorttablebycolumn | `sort table [TABLENAME v] by column [COLUMN] [SORTORDER v]` | Sorts by column (large to small / small to large) |
| data_copy_table_into_table | `copy table [TABLE1] into [TABLE2]` | Copies entire table (replaces destination) |
| data_append_table_into_table | `append table [TABLE1] to [TABLE2]` | Appends table1 rows to bottom of table2 |
| data_pivot_table_into_table | `pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST]` | Creates pivot table with grouping and aggregation |

### 1.16 TABLE IMPORT/EXPORT & DISPLAY (6 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_showsnapshotoftable | `show snapshot of table [TABLENAME v] from row (STARTROW) to (ENDROW) with style [STYLE] [THEMECOLOR]` | Shows table rows in popup (4 style choices) |
| data_exporttable | `export table [TABLENAME v] as [FILENAME]` | Exports as CSV file |
| data_importtable | `import file into table [TABLE]` | Opens dialog to import txt/csv |
| data_savetable | `save table [TABLE v] to server as [DATANAME]` | Saves table to CreatiCode server |
| data_loadtable | (syntax not shown) | Loads table from server |
| data_showtable | (syntax not shown) | Shows table display |
| data_hidetable | (syntax not shown) | Hides table display |

### 1.17 CLOUD SESSION MANAGEMENT (2 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| data_joincloudsession | (syntax not shown) | Joins cloud multiplayer session |
| data_createcloudsession | (syntax not shown) | Creates cloud multiplayer session |

---

## CATEGORY 2: OPERATORS (30 BLOCKS)

### 2.1 MATHEMATICAL OPERATIONS (6 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| operator_pow | `(BASE) ^ (P)` | Reporter: BASE to the power of P |
| operator_calc | `calculate expression [EXPRESSION]` | Reporter: evaluates any expression like (1+1)*(2^4) |
| operator_solveequation | `solve equation [EQUATION]` | Reporter: solves equations (returns 'x,8,y,2' format) |
| operator_noise2d | `noise at x (XPOS) y (YPOS) seed (SEED)` | Reporter: 2D Perlin noise function |
| operator_value_from_moving_average | `value from [METHOD v] moving average window [LENGTH] of list [LISTNAME v]` | Reporter: simple/exponential moving average |

### 2.2 COMPARISON OPERATORS (3 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| operator_diff | `[V1] ≠ [V2]` | Boolean: not equal comparison |
| operator_gte | `[V1] ≥ [V2]` | Boolean: greater than or equal |
| operator_lte | `[V1] ≤ [V2]` | Boolean: less than or equal |

### 2.3 STRING OPERATIONS - TESTING (3 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| operator_include | `[TEXT1] includes [TEXT2] ignore case [IGNORECASE v]` | Boolean: checks if includes substring |
| operator_start | `[TEXT1] starts with [TEXT2] ignore case [IGNORECASE v]` | Boolean: checks if starts with |
| operator_end | `[TEXT1] ends with [TEXT2] ignore case [IGNORECASE v]` | Boolean: checks if ends with |

### 2.4 STRING OPERATIONS - MANIPULATION (5 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| operator_replace | `replace [T1] with [T2] in [T3]` | Reporter: replaces all occurrences |
| operator_substringindex | `position of [T1] in [T2]` | Reporter: returns position (1 = first letter) |
| operator_substring | `substring of [TEXT] from position (P1) to position (P2)` | Reporter: extracts substring |
| operator_splitsubstring | `part (INDEX) of [TEXT] by [SEPARATOR]` | Reporter: splits and returns part at index |
| operator_joinwith | `join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]` | Reporter: joins up to 6 texts |

### 2.5 STRING OPERATIONS - ADVANCED (4 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| operator_lcs | `longest common substring between [TEXT1] and [TEXT2]` | Reporter: returns LCS |
| operator_trim | `trim [TEXT]` | Reporter: trims leading/ending spaces |
| operator_texttransform | `[CASE v] of text [T]` | Reporter: uppercase/lowercase conversion |
| operator_stringdiff | `steps to change [STRING1] into [STRING2]` | Reporter: returns minimum steps line by line |

### 2.6 STRING OPERATIONS - TYPE CONVERSION (2 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| operator_isnumber | `<[TEXT] is a number?>` | Boolean: checks if text is convertible to number |
| operator_converttonumber | `convert [TEXT] to a number` | Reporter: converts text to number (supports 'one', 'two hundreds', 'third') |

### 2.7 REGULAR EXPRESSION OPERATIONS (5 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| operator_regex_test | `regex [REGEXPATTERN] test [TEXT]` | Boolean: tests if text contains pattern |
| operator_regex_match_into_list | `regex [REGEXPATTERN] flag [FLAG] match [TEXT] into list [LISTNAME v]` | Extracts matches to list (flag 'g' for all matches) |
| operator_regex_search | `regex [REGEXPATTERN] search [TEXT]` | Reporter: returns position of first match |
| operator_regex_replace_with | `regex [REGEXPATTERN] flag [FLAG] replace [TEXT] with [T]` | Reporter: replaces matches (flag 'g' for all) |
| operator_regex_split_into_list | `regex [REGEXPATTERN] flag [FLAG] split [TEXT] into list [LISTNAME v]` | Splits text by regex pattern |

### 2.8 GEOMETRIC/VECTOR OPERATIONS (3 blocks)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| operator_vector_distance | `distance between x (X1) y (Y1) and x (X2) y (Y2) [METHOD v]` | Reporter: direct or manhattan distance (2D) |
| operator_vector_distance3d | `distance between x (X1) y (Y1) z (Z1) and x (X2) y (Y2) z (Z2) [METHOD v]` | Reporter: direct or manhattan distance (3D) |
| operator_vector_direction | `direction from x (X1) y (Y1) to x (X2) y (Y2)` | Reporter: direction in degrees |

---

## CATEGORY 3: CONTROL (1 BLOCK)

### 3.1 FOR-LOOP WITH VARIABLE (1 block)

| Block ID | Syntax | Description |
|----------|--------|-------------|
| control_set_variable_in_loop | `for [VARIABLE v] from (START) to (LIMIT) at step (S)` | C-block: for-loop that sets variable each iteration. Checks limit based on step direction. Step cannot be 0. |

**Full Description:** Variable starts at START, changes by S each iteration. Before each iteration, checks if exceeded LIMIT (if S>0: check if var>LIMIT; if S<0: check if var<LIMIT). Stops when limit exceeded.

---

## COMPARISON WITH STANDARD SCRATCH

### CreatiCode ADDS these features not in standard Scratch:

1. **TABLES** (34 blocks) - Complete spreadsheet-like functionality
   - Create/modify structure (columns)
   - Add/insert/delete/replace rows
   - Cell-level operations
   - Search and lookup (VLOOKUP-style)
   - Aggregation and statistics
   - Pivot tables
   - Import/export CSV
   - Sort and shuffle

2. **CLOUD STORAGE** (4 blocks) - Server-side data persistence
   - Save/load data by key
   - Public vs private visibility
   - Data names listing

3. **ADVANCED LIST OPERATIONS** (8 blocks)
   - Seeded random numbers
   - Copy/append lists
   - Insert selected items (largest/smallest/random)
   - For-each loops
   - Aggregation (min/max/sum/avg/median)
   - Find by substring

4. **REGULAR EXPRESSIONS** (5 blocks)
   - Test, match, search, replace, split
   - Full regex pattern support

5. **ADVANCED STRING OPERATIONS** (12 blocks beyond basic)
   - Case-insensitive checking
   - Replace all
   - Longest common substring
   - String diff
   - Convert word numbers to digits

6. **ADVANCED MATH** (4 blocks)
   - Equation solver
   - Expression calculator
   - 2D noise function
   - Moving averages

7. **ENHANCED VARIABLES**
   - Import/export to files
   - Reduce by (for young learners)

8. **GEOMETRIC CALCULATIONS**
   - 2D/3D distance (direct/manhattan)
   - Direction in degrees

---

## KEY INSIGHTS FOR T09 SKILLS VERIFICATION

### Critical Features to Check:

1. **TABLES ARE MAJOR** - 34 blocks = 37% of all variable-related functionality
   - T09 must adequately cover table operations
   - Should include: creation, row/column operations, search, aggregation, pivot

2. **CLOUD STORAGE** - Unique CreatiCode feature
   - T09 should mention server data persistence
   - Public/private data visibility

3. **REGEX SUPPORT** - 5 dedicated blocks
   - T09 should cover pattern matching capabilities
   - Match, replace, split with regex

4. **ADVANCED LIST FEATURES** beyond standard Scratch
   - Seeded random
   - Copy/append between lists
   - Insert selected items
   - Aggregation functions
   - For-each loops

5. **STRING MANIPULATION** is extensive (15 blocks)
   - Case-insensitive operations
   - Advanced replacements
   - Word-to-number conversion
   - String diffing

6. **MATHEMATICAL CAPABILITIES** beyond basic
   - Equation solving
   - Expression evaluation
   - Noise functions
   - Statistical analysis (moving averages)

### Potential T09 Gaps to Verify:

- [ ] Are table operations comprehensively documented?
- [ ] Is cloud/server storage mentioned?
- [ ] Are regex capabilities covered?
- [ ] Is pivot table functionality documented?
- [ ] Are moving averages and statistical functions included?
- [ ] Is the for-loop with variable control block mentioned?
- [ ] Are seeded random lists documented?
- [ ] Is the equation solver mentioned?
- [ ] Are geometric calculation blocks (distance, direction) covered?

---

## BLOCK COUNT SUMMARY

| Category | Count | % of Total |
|----------|-------|------------|
| Variables | 59 | 66% |
| Operators | 30 | 33% |
| Control | 1 | 1% |
| **TOTAL** | **90** | **100%** |

### Variables Category Breakdown:
- Basic Variables: 3 (5%)
- Lists: 18 (31%)
- Cloud Storage: 4 (7%)
- Tables: 34 (58%)

### Operators Category Breakdown:
- Math: 6 (20%)
- Comparison: 3 (10%)
- Strings: 12 (40%)
- Regex: 5 (17%)
- Geometric: 3 (10%)
- Advanced: 1 (3%)

---

## NOTES

1. **Tables are not available in standard Scratch** - this is a major CreatiCode enhancement
2. **Cloud storage is built-in** - no external extensions needed
3. **Regex support is comprehensive** - rare in educational coding platforms
4. **List operations are significantly enhanced** beyond standard Scratch
5. **String manipulation rivals professional programming languages**
6. **Mathematical capabilities include advanced features** (noise, equations, expressions)

**END OF ANALYSIS**
