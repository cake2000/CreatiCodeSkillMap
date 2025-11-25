# CreatiCode Variable-Related Blocks - Quick Reference Table

## VARIABLES CATEGORY (59 blocks)

| # | Block ID | Syntax | Function |
|---|----------|--------|----------|
| 1 | data_reducevariableby | `reduce [VARIABLE v] by (N)` | Reduce variable by N |
| 2 | data_exportvariable | `export variable [VARIABLE v]` | Export variable to file |
| 3 | data_importvariable | `import variable [VARIABLE v]` | Import variable from file |
| 4 | data_reduceitemoflist | `reduce item (INDEX) of [LISTNAME v] by (N)` | Reduce list item by N |
| 5 | data_changeitemoflist | `change item (INDEX) of [LISTNAME v] by (N)` | Change list item by N |
| 6 | data_joinlistwith | `join [LISTNAME v] into text with [SEPARATOR]` | Join list to text |
| 7 | data_set_list_to_split_of | `set [LISTNAME v] to split of [TEXT] with splitter [SEPARATOR]` | Split text to list |
| 8 | data_deletevalueoflist | `delete value [V] from [LISTNAME v]` | Delete value from list |
| 9 | data_reverselist | `reverse [LISTNAME v]` | Reverse list order |
| 10 | data_reshuffle | `reshuffle [LISTNAME v] randomly` | Shuffle list randomly |
| 11 | data_sortlistby | `sort list [LISTNAME v] from [METHOD v]` | Sort list |
| 12 | data_insertitemsfromlist | `insert (N) [SELECTOR v] items from [LISTNAME1 v] into [LISTNAME2 v]` | Insert items between lists |
| 13 | data_copytolist | `copy [LISTNAME1 v] to [LISTNAME2 v]` | Copy list |
| 14 | data_appendtolist | `append [LISTNAME1 v] to [LISTNAME2 v]` | Append list to list |
| 15 | data_setrandomlist | `set [LISTNAME v] to (N) random whole numbers between (MIN) and (MAX) [REPEATMETHOD v]` | Populate with random numbers |
| 16 | data_setrandomlistseed | `set [LISTNAME v] to (N) random numbers with seed (SEED)` | Populate with seeded randoms |
| 17 | data_itemnumoflist2 | `# of item containing [TEXT] in [LISTNAME v]` | Find item by substring |
| 18 | data_itemspecificvalueoflist | `[METHOD v] of list [LISTNAME v]` | Get min/max/sum/avg/median |
| 19 | data_for_each | `for each item [VARIABLENAME v] in [LISTNAME v]` | Loop through items |
| 20 | data_for_each_index | `for each index [INDEXVARIABLENAME v] in [LISTNAME v]` | Loop through indices |
| 21 | data_savedata | `save [VISIBILITY v] data [VALUE] with name [KEY]` | Save to server |
| 22 | data_removedata | `remove [VISIBILITY v] data named [KEY]` | Remove from server |
| 23 | data_loaddata | `load data named [KEY]` | Load from server |
| 24 | data_load_data_names | `data names` | Get all data names |
| 25 | data_rowatindexoftable | `row (ROWINDEX) of table [TABLENAME v] separator [SEPARATOR]` | Get row as text |
| 26 | data_rowindexwithcondition | `row # of [VALUE] in column [COLUMN] in table [TABLENAME v]` | Find row by value |
| 27 | data_rowindexwithcondition2 | `row # of item containing [SUBSTRING] in column [COLUMN] in table [TABLENAME v]` | Find row by substring |
| 28 | data_addrowtotable | `add to table [TABLENAME v]: [CELL1] ... [CELL12]` | Add row to table |
| 29 | data_removeallcolumnsfromtable | `delete all columns from table [TABLENAME v]` | Delete all columns |
| 30 | data_addcolatposition | `add column [COLUMNNAME] at position (POSITION) to table [TABLENAME v]` | Add column at position |
| 31 | data_insertrowtotable | `insert at row (ROWNUM) of table [TABLENAME v]: [CELL1] ... [CELL12]` | Insert row at position |
| 32 | data_replacerowoftable | `replace row (ROWNUM) of table [TABLENAME v] with: [CELL1] ... [CELL12]` | Replace entire row |
| 33 | data_replaceitematrowcolumn | `replace item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] with [VALUE]` | Replace cell value |
| 34 | data_reduceitematrowcolumn | `reduce item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)` | Reduce cell value |
| 35 | data_changeitematrowcolumn | `change item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)` | Change cell value |
| 36 | data_settabletocomputed | `set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2]` | Aggregate data by group |
| 37 | data_reshuffletable | `reshuffle table [TABLENAME v] randomly` | Shuffle table rows |
| 38 | data_sorttablebycolumn | `sort table [TABLENAME v] by column [COLUMN] [SORTORDER v]` | Sort table by column |
| 39 | data_deleterowoftable | `delete row (ROWNUM) of table [TABLENAME v]` | Delete row by index |
| 40 | data_deleterowwithcondition | `delete rows with column [COLUMN] of value [VALUE] from table [TABLENAME v]` | Delete rows by condition |
| 41 | data_deleteallrowsoftable | `delete all rows from table [TABLENAME v]` | Delete all rows |
| 42 | data_deletecolumnfromtable | `delete column [COLUMNNAME] from table [TABLENAME v]` | Delete column |
| 43 | data_rowcountoftable | `row count of table [TABLENAME v]` | Get row count |
| 44 | data_computetable | `[METHOD] of column [COLUMNNAME] in table [TABLE v]` | Aggregate column |
| 45 | data_itematrowcolumnoftable | `item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v]` | Get cell value |
| 46 | data_copy_table_into_table | `copy table [TABLE1] into [TABLE2]` | Copy table |
| 47 | data_append_table_into_table | `append table [TABLE1] to [TABLE2]` | Append table |
| 48 | data_pivot_table_into_table | `pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST]` | Create pivot table |
| 49 | data_showsnapshotoftable | `show snapshot of table [TABLENAME v] from row (STARTROW) to (ENDROW) with style [STYLE] [THEMECOLOR]` | Show table in popup |
| 50 | data_lookuptable | `item in column [RETURNCOLUMN] of [TABLENAME v] where column [SEARCHCOLUMN] equals [SEARCHTEXT]` | Lookup value |
| 51 | data_exporttable | `export table [TABLENAME v] as [FILENAME]` | Export table to CSV |
| 52 | data_importtable | `import file into table [TABLE]` | Import file to table |
| 53 | data_savetable | `save table [TABLE v] to server as [DATANAME]` | Save table to server |
| 54 | data_loadtable | (not shown) | Load table from server |
| 55 | data_showtable | (not shown) | Show table display |
| 56 | data_hidetable | (not shown) | Hide table display |
| 57 | data_setlisttocolumn | (not shown) | Set list to table column |
| 58 | data_joincloudsession | (not shown) | Join cloud session |
| 59 | data_createcloudsession | (not shown) | Create cloud session |

## OPERATORS CATEGORY (30 blocks)

| # | Block ID | Syntax | Function |
|---|----------|--------|----------|
| 1 | operator_vector_distance | `distance between x (X1) y (Y1) and x (X2) y (Y2) [METHOD v]` | 2D distance calculation |
| 2 | operator_vector_distance3d | `distance between x (X1) y (Y1) z (Z1) and x (X2) y (Y2) z (Z2) [METHOD v]` | 3D distance calculation |
| 3 | operator_vector_direction | `direction from x (X1) y (Y1) to x (X2) y (Y2)` | Direction in degrees |
| 4 | operator_include | `[TEXT1] includes [TEXT2] ignore case [IGNORECASE v]` | Check if includes |
| 5 | operator_start | `[TEXT1] starts with [TEXT2] ignore case [IGNORECASE v]` | Check if starts with |
| 6 | operator_end | `[TEXT1] ends with [TEXT2] ignore case [IGNORECASE v]` | Check if ends with |
| 7 | operator_replace | `replace [T1] with [T2] in [T3]` | Replace text |
| 8 | operator_substringindex | `position of [T1] in [T2]` | Find position |
| 9 | operator_substring | `substring of [TEXT] from position (P1) to position (P2)` | Extract substring |
| 10 | operator_splitsubstring | `part (INDEX) of [TEXT] by [SEPARATOR]` | Split and get part |
| 11 | operator_lcs | `longest common substring between [TEXT1] and [TEXT2]` | Longest common substring |
| 12 | operator_joinwith | `join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]` | Join texts |
| 13 | operator_trim | `trim [TEXT]` | Trim spaces |
| 14 | operator_isnumber | `<[TEXT] is a number?>` | Check if number |
| 15 | operator_converttonumber | `convert [TEXT] to a number` | Convert to number |
| 16 | operator_texttransform | `[CASE v] of text [T]` | Change case |
| 17 | operator_regex_test | `regex [REGEXPATTERN] test [TEXT]` | Test regex |
| 18 | operator_regex_match_into_list | `regex [REGEXPATTERN] flag [FLAG] match [TEXT] into list [LISTNAME v]` | Match regex to list |
| 19 | operator_regex_search | `regex [REGEXPATTERN] search [TEXT]` | Search with regex |
| 20 | operator_regex_replace_with | `regex [REGEXPATTERN] flag [FLAG] replace [TEXT] with [T]` | Replace with regex |
| 21 | operator_regex_split_into_list | `regex [REGEXPATTERN] flag [FLAG] split [TEXT] into list [LISTNAME v]` | Split by regex |
| 22 | operator_diff | `[V1] ≠ [V2]` | Not equal |
| 23 | operator_gte | `[V1] ≥ [V2]` | Greater or equal |
| 24 | operator_lte | `[V1] ≤ [V2]` | Less or equal |
| 25 | operator_pow | `(BASE) ^ (P)` | Power/exponent |
| 26 | operator_solveequation | `solve equation [EQUATION]` | Solve equation |
| 27 | operator_stringdiff | `steps to change [STRING1] into [STRING2]` | String diff |
| 28 | operator_calc | `calculate expression [EXPRESSION]` | Calculate expression |
| 29 | operator_noise2d | `noise at x (XPOS) y (YPOS) seed (SEED)` | 2D noise |
| 30 | operator_value_from_moving_average | `value from [METHOD v] moving average window [LENGTH] of list [LISTNAME v]` | Moving average |

## SUMMARY STATISTICS

### Variables Category Breakdown:
- **Basic Variables**: 3 blocks
- **List Operations**: 18 blocks
- **Cloud Storage**: 4 blocks
- **Table Operations**: 34 blocks

### Operators Category Breakdown:
- **Math Operations**: 4 blocks
- **Comparison**: 3 blocks
- **String Operations**: 15 blocks
- **Regex Operations**: 5 blocks
- **Geometric**: 3 blocks

### Key Features:
1. **Tables are extensively supported** (34 blocks = 58% of Variables category)
2. **String manipulation is rich** (15 blocks in Operators)
3. **Regex support is comprehensive** (5 dedicated blocks)
4. **Cloud/server storage built-in** (4 blocks for data persistence)
5. **Advanced list operations** (aggregation, seeded random, loops)
6. **Mathematical capabilities** (equations, expressions, noise, moving avg)
