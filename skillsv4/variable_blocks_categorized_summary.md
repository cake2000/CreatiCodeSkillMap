# CreatiCode Variable-Related Blocks - Complete Categorized Summary

This document lists ALL variable-related blocks available in CreatiCode, organized by functionality type.

**Total Counts:**
- Variables Category: 59 blocks
- Operators Category: 30 blocks
- **Grand Total: 89 blocks**

---

## CATEGORY 1: VARIABLES (59 blocks)

### A. Basic Variable Operations (3 blocks)
1. **data_reducevariableby** - `reduce [VARIABLE v] by (N)`
   - Reduces a variable by N (for young learners who don't know negative numbers)

2. **data_exportvariable** - `export variable [VARIABLE v]`
   - Exports variable content to a txt file

3. **data_importvariable** - `import variable [VARIABLE v]`
   - Import variable from txt or csv file via dialog

### B. List Manipulation - Basic Operations (7 blocks)
4. **data_reduceitemoflist** - `reduce item (INDEX) of [LISTNAME v] by (N)`
   - Reduces a list item by N

5. **data_changeitemoflist** - `change item (INDEX) of [LISTNAME v] by (N)`
   - Changes a list item value by N

6. **data_deletevalueoflist** - `delete value [V] from [LISTNAME v]`
   - Deletes first item with given value

7. **data_reverselist** - `reverse [LISTNAME v]`
   - Reverses list order

8. **data_reshuffle** - `reshuffle [LISTNAME v] randomly`
   - Randomly shuffles list items

9. **data_sortlistby** - `sort list [LISTNAME v] from [METHOD v]`
   - Sorts list (large to small or small to large)

10. **data_insertitemsfromlist** - `insert (N) [SELECTOR v] items from [LISTNAME1 v] into [LISTNAME2 v]`
    - Inserts N items (largest/smallest/random) from one list to another

### C. List Manipulation - Advanced Operations (11 blocks)
11. **data_copytolist** - `copy [LISTNAME1 v] to [LISTNAME2 v]`
    - Copies list (replaces destination)

12. **data_appendtolist** - `append [LISTNAME1 v] to [LISTNAME2 v]`
    - Appends one list to another

13. **data_joinlistwith** - `join [LISTNAME v] into text with [SEPARATOR]`
    - Joins list items into text with separator

14. **data_set_list_to_split_of** - `set [LISTNAME v] to split of [TEXT] with splitter [SEPARATOR]`
    - Splits text into list by separator

15. **data_setrandomlist** - `set [LISTNAME v] to (N) random whole numbers between (MIN) and (MAX) [REPEATMETHOD v]`
    - Populates list with random numbers (with/without repetition)

16. **data_setrandomlistseed** - `set [LISTNAME v] to (N) random numbers with seed (SEED)`
    - Populates list with seeded random numbers (0-1)

17. **data_itemnumoflist2** - `# of item containing [TEXT] in [LISTNAME v]`
    - Returns position of first item containing substring

18. **data_itemspecificvalueoflist** - `[METHOD v] of list [LISTNAME v]`
    - Returns smallest/largest/sum/average/median of list

19. **data_for_each** - `for each item [VARIABLENAME v] in [LISTNAME v]`
    - C-block: iterates through list items

20. **data_for_each_index** - `for each index [INDEXVARIABLENAME v] in [LISTNAME v]`
    - C-block: iterates through list indices

21. **data_setlisttocolumn** - (syntax not fully visible in excerpt)
    - Sets list to table column

### D. Cloud/Server Data Storage (4 blocks)
22. **data_savedata** - `save [VISIBILITY v] data [VALUE] with name [KEY]`
    - Saves data to server (public/private)

23. **data_removedata** - `remove [VISIBILITY v] data named [KEY]`
    - Removes data from server

24. **data_loaddata** - `load data named [KEY]`
    - Loads data from server by key

25. **data_load_data_names** - `data names`
    - Returns list of all data names (separated by &&)

### E. Table Operations - Creation & Structure (4 blocks)
26. **data_removeallcolumnsfromtable** - `delete all columns from table [TABLENAME v]`
    - Deletes all columns (empties table)

27. **data_addcolatposition** - `add column [COLUMNNAME] at position (POSITION) to table [TABLENAME v]`
    - Adds column at position

28. **data_deletecolumnfromtable** - `delete column [COLUMNNAME] from table [TABLENAME v]`
    - Deletes specific column

29. **data_deleteallrowsoftable** - `delete all rows from table [TABLENAME v]`
    - Deletes all rows (keeps columns)

### F. Table Operations - Row Manipulation (8 blocks)
30. **data_addrowtotable** - `add to table [TABLENAME v]: [CELL1] [CELL2] ... [CELL12]`
    - Appends new row (up to 12 cells)

31. **data_insertrowtotable** - `insert at row (ROWNUM) of table [TABLENAME v]: [CELL1] ... [CELL12]`
    - Inserts row at position

32. **data_replacerowoftable** - `replace row (ROWNUM) of table [TABLENAME v] with: [CELL1] ... [CELL12]`
    - Replaces entire row

33. **data_deleterowoftable** - `delete row (ROWNUM) of table [TABLENAME v]`
    - Deletes row by index

34. **data_deleterowwithcondition** - `delete rows with column [COLUMN] of value [VALUE] from table [TABLENAME v]`
    - Deletes rows matching condition

35. **data_rowatindexoftable** - `row (ROWINDEX) of table [TABLENAME v] separator [SEPARATOR]`
    - Returns all data in row as text

36. **data_rowindexwithcondition** - `row # of [VALUE] in column [COLUMN] in table [TABLENAME v]`
    - Finds row index by exact value

37. **data_rowindexwithcondition2** - `row # of item containing [SUBSTRING] in column [COLUMN] in table [TABLENAME v]`
    - Finds row index by substring

### G. Table Operations - Cell Manipulation (3 blocks)
38. **data_replaceitematrowcolumn** - `replace item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] with [VALUE]`
    - Replaces cell value

39. **data_reduceitematrowcolumn** - `reduce item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)`
    - Reduces cell value

40. **data_changeitematrowcolumn** - `change item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)`
    - Changes cell value

### H. Table Operations - Data Retrieval (3 blocks)
41. **data_rowcountoftable** - `row count of table [TABLENAME v]`
    - Returns row count

42. **data_computetable** - `[METHOD] of column [COLUMNNAME] in table [TABLE v]`
    - Aggregates column (smallest/largest/sum/average/median)

43. **data_itematrowcolumnoftable** - `item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v]`
    - Returns cell value

44. **data_lookuptable** - `item in column [RETURNCOLUMN] of [TABLENAME v] where column [SEARCHCOLUMN] equals [SEARCHTEXT]`
    - Lookup value in one column based on another

### I. Table Operations - Advanced Transformations (6 blocks)
45. **data_settabletocomputed** - `set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2]`
    - Aggregates data grouped by column

46. **data_reshuffletable** - `reshuffle table [TABLENAME v] randomly`
    - Randomly shuffles rows

47. **data_sorttablebycolumn** - `sort table [TABLENAME v] by column [COLUMN] [SORTORDER v]`
    - Sorts table by column

48. **data_copy_table_into_table** - `copy table [TABLE1] into [TABLE2]`
    - Copies entire table (replaces)

49. **data_append_table_into_table** - `append table [TABLE1] to [TABLE2]`
    - Appends one table to another

50. **data_pivot_table_into_table** - `pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST]`
    - Creates pivot table

### J. Table Operations - Import/Export & Display (6 blocks)
51. **data_showsnapshotoftable** - `show snapshot of table [TABLENAME v] from row (STARTROW) to (ENDROW) with style [STYLE] [THEMECOLOR]`
    - Shows table in popup window

52. **data_exporttable** - `export table [TABLENAME v] as [FILENAME]`
    - Exports table as CSV file

53. **data_importtable** - `import file into table [TABLE]`
    - Imports txt/csv file into table

54. **data_savetable** - `save table [TABLE v] to server as [DATANAME]`
    - Saves table to server

55. **data_loadtable** - (syntax not shown in excerpt)
    - Loads table from server

56. **data_showtable** - (syntax not shown in excerpt)
    - Shows table display

57. **data_hidetable** - (syntax not shown in excerpt)
    - Hides table display

### K. Cloud Session Management (2 blocks)
58. **data_joincloudsession** - (syntax not shown in excerpt)
    - Joins cloud session

59. **data_createcloudsession** - (syntax not shown in excerpt)
    - Creates cloud session

---

## CATEGORY 2: OPERATORS (30 blocks)

### A. Mathematical Operations (4 blocks)
1. **operator_pow** - `(BASE) ^ (P)`
   - Power/exponent operation

2. **operator_calc** - `calculate expression [EXPRESSION]`
   - Calculates any expression

3. **operator_solveequation** - `solve equation [EQUATION]`
   - Solves equations (returns comma-separated variable values)

4. **operator_noise2d** - `noise at x (XPOS) y (YPOS) seed (SEED)`
   - 2D noise function

### B. Comparison & Logic Operations (3 blocks)
5. **operator_diff** - `[V1] ≠ [V2]`
   - Not equal comparison

6. **operator_gte** - `[V1] ≥ [V2]`
   - Greater than or equal

7. **operator_lte** - `[V1] ≤ [V2]`
   - Less than or equal

### C. String Operations - Basic (8 blocks)
8. **operator_include** - `[TEXT1] includes [TEXT2] ignore case [IGNORECASE v]`
   - Checks if text includes substring

9. **operator_start** - `[TEXT1] starts with [TEXT2] ignore case [IGNORECASE v]`
   - Checks if text starts with substring

10. **operator_end** - `[TEXT1] ends with [TEXT2] ignore case [IGNORECASE v]`
    - Checks if text ends with substring

11. **operator_replace** - `replace [T1] with [T2] in [T3]`
    - Replaces all occurrences

12. **operator_substringindex** - `position of [T1] in [T2]`
    - Returns position of substring

13. **operator_substring** - `substring of [TEXT] from position (P1) to position (P2)`
    - Extracts substring

14. **operator_splitsubstring** - `part (INDEX) of [TEXT] by [SEPARATOR]`
    - Splits text and returns part at index

15. **operator_joinwith** - `join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]`
    - Joins up to 6 texts with separator

### D. String Operations - Advanced (7 blocks)
16. **operator_lcs** - `longest common substring between [TEXT1] and [TEXT2]`
    - Returns longest common substring

17. **operator_trim** - `trim [TEXT]`
    - Trims leading/ending spaces

18. **operator_texttransform** - `[CASE v] of text [T]`
    - Converts to uppercase/lowercase

19. **operator_isnumber** - `<[TEXT] is a number?>`
    - Checks if text is a number

20. **operator_converttonumber** - `convert [TEXT] to a number`
    - Converts text to number (supports words like 'one', 'two hundreds')

21. **operator_stringdiff** - `steps to change [STRING1] into [STRING2]`
    - Returns minimum steps to convert string line by line

22. **operator_value_from_moving_average** - `value from [METHOD v] moving average window [LENGTH] of list [LISTNAME v]`
    - Calculates moving average (simple/exponential)

### E. Regular Expression Operations (5 blocks)
23. **operator_regex_test** - `regex [REGEXPATTERN] test [TEXT]`
    - Tests if text contains regex pattern

24. **operator_regex_match_into_list** - `regex [REGEXPATTERN] flag [FLAG] match [TEXT] into list [LISTNAME v]`
    - Matches regex and stores results in list

25. **operator_regex_search** - `regex [REGEXPATTERN] search [TEXT]`
    - Returns position of first regex match

26. **operator_regex_replace_with** - `regex [REGEXPATTERN] flag [FLAG] replace [TEXT] with [T]`
    - Replaces regex matches

27. **operator_regex_split_into_list** - `regex [REGEXPATTERN] flag [FLAG] split [TEXT] into list [LISTNAME v]`
    - Splits text by regex into list

### F. Geometric/Vector Operations (3 blocks)
28. **operator_vector_distance** - `distance between x (X1) y (Y1) and x (X2) y (Y2) [METHOD v]`
    - Calculates distance (direct/manhattan)

29. **operator_vector_distance3d** - `distance between x (X1) y (Y1) z (Z1) and x (X2) y (Y2) z (Z2) [METHOD v]`
    - Calculates 3D distance

30. **operator_vector_direction** - `direction from x (X1) y (Y1) to x (X2) y (Y2)`
    - Returns direction in degrees

---

## KEY OBSERVATIONS FOR T09 SKILLS VERIFICATION:

### Variables Covered:
- ✅ Basic variable operations (set, change, reduce)
- ✅ List operations (comprehensive - 18+ blocks)
- ✅ Table operations (comprehensive - 35+ blocks)
- ✅ Cloud/server data storage (4 blocks)
- ✅ Import/export capabilities

### Operators Covered:
- ✅ Mathematical operations (power, expressions, equations)
- ✅ Comparison operators (≠, ≥, ≤)
- ✅ String manipulation (15+ blocks)
- ✅ Regular expressions (5 blocks)
- ✅ Geometric calculations (distance, direction)

### Notable Features:
1. **Tables are a major feature** - 35+ dedicated blocks for table manipulation
2. **Advanced list operations** - sorting, shuffling, aggregation, seeded random
3. **Regular expressions** - full regex support with match, replace, split
4. **Cloud storage** - built-in server data storage
5. **Import/Export** - variables, lists, and tables can be saved/loaded
6. **Advanced math** - equation solver, noise functions, moving averages

### Potential Gaps to Check in T09:
- Verify if T09 adequately covers TABLE operations (major CreatiCode feature)
- Check if cloud/server data storage blocks are mentioned
- Verify regex blocks are included
- Check if pivot table functionality is documented
- Verify moving average and advanced statistical functions
