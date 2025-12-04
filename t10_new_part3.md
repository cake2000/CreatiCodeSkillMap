## GRADE 5 (40 skills)

ID: T10.G5.01
Topic: T10 – Lists & Tables
Skill: Compare lists vs tables conceptually (bridge skill)
Description: Students explore the conceptual difference between lists (one-dimensional, single sequence of values) and tables (two-dimensional, rows and columns) through comparison activities. They examine scenarios: a shopping list (1D: just item names) vs. a shopping cart (2D: item name, price, quantity). Students recognize that tables organize related attributes (columns) for each entity (row), while lists store a single sequence. They identify when to "graduate" from lists to tables: when each item needs multiple properties tracked together, when relationships between attributes matter, or when data needs to be searched/filtered by different criteria. This conceptual bridge skill prepares students for the structural shift from list thinking (position-based access) to table thinking (row-column coordinate system), reducing confusion when first encountering tables.
Dependencies:
* T10.G4.03: Store and retrieve parallel list data
* T10.G3.20: Explain to a partner why a list is useful for a problem

ID: T10.G5.02
Topic: T10 – Lists & Tables
Skill: Identify table structure (rows, columns, cells)
Description: Students identify and label the parts of a table: rows (horizontal, numbered), columns (vertical, named), and cells (values at row-column intersections). Given a sample table, they state the number of rows and columns, identify the value at a specific row-column intersection, and explain that each row represents one record while each column represents one attribute. Students recognize that a table is like having multiple parallel lists (one list per column) organized together, where all lists have the same length and items at the same position are related. A table makes it easier to manage related data than using many separate parallel lists.
Dependencies:
* T10.G5.01: Compare lists vs tables conceptually (bridge skill)

ID: T10.G5.03
Topic: T10 – Lists & Tables
Skill: Create a table and add columns
Description: Students create an empty table variable and use `add column [name] at position (n) to table [table]` to define the table structure. Columns must be created before data can be added to them, and the position parameter controls column order (1 = first column, 2 = second, etc.). Students verify the table structure by examining the table monitor.
Dependencies:
* T10.G5.02: Identify table structure (rows, columns, cells)

ID: T10.G5.04
Topic: T10 – Lists & Tables
Skill: Add rows of data to a table
Description: Students use the `add to table [table]: [value1] [value2] ...` block to add rows of data. They ensure the number of values matches the number of columns and understand that rows are numbered starting from 1.
Dependencies:
* T10.G5.03: Create a table and add columns

ID: T10.G5.05
Topic: T10 – Lists & Tables
Skill: Read a cell value from a table
Description: Students use the `item at row (n) column [name] of table [table]` block to retrieve a specific value. They practice reading different cells and using the values in their programs.
Dependencies:
* T10.G5.04: Add rows of data to a table

ID: T10.G5.06
Topic: T10 – Lists & Tables
Skill: Update a cell value in a table
Description: Students use the `replace item at row (n) column [name] of table [table] with [value]` block to modify existing data. They update cells based on position and understand this changes the table in place.
Dependencies:
* T10.G5.05: Read a cell value from a table

ID: T10.G5.07
Topic: T10 – Lists & Tables
Skill: Get the number of rows in a table
Description: Students use the `row count of table [table]` block to find how many rows exist in a table. They understand this is essential for loops (iterate from 1 to row count), checking if table is empty (row count = 0), and reporting table size.
Dependencies:
* T10.G5.05: Read a cell value from a table

ID: T10.G5.08
Topic: T10 – Lists & Tables
Skill: Find which row contains a value
Description: Students use the `row # of [value] in column [name] in table [table]` block to search for the first row where a specific column equals a value. They understand this returns the row number (index) or 0 if not found, enabling them to locate data for reading or updating.
Dependencies:
* T10.G5.07: Get the number of rows in a table
* T10.G3.26: Find an item's position using built-in block

ID: T10.G5.09
Topic: T10 – Lists & Tables
Skill: Loop through table rows to compute aggregates
Description: Students use a counted loop from 1 to `row count of table` to iterate through all rows. They access values in a specific column and compute totals (sum), counts, or find maximum/minimum values using a variable accumulator.
Dependencies:
* T07.G3.01: Use a counted repeat loop
* T10.G5.07: Get the number of rows in a table
* T10.G5.05: Read a cell value from a table
* T09.G3.01: Increment and decrement a variable

ID: T10.G5.10
Topic: T10 – Lists & Tables
Skill: Use built-in table aggregate blocks
Description: Students use CreatiCode's `[sum/average/smallest/largest/median] of column [name] in table [table]` blocks to compute statistics on a column without writing a loop. They compare this to manual aggregation using loops from the previous skill.
Dependencies:
* T10.G5.09: Loop through table rows to compute aggregates
* T10.G4.05: Use built-in list statistics (Sum, Average, Min, Max)

ID: T10.G5.11
Topic: T10 – Lists & Tables
Skill: Delete a single row by index
Description: Students use the `delete row (n) of table [table]` block to remove a specific row by its position number. They observe how remaining rows shift up (row 4 becomes row 3) and understand the row count decreases by 1.
Dependencies:
* T10.G5.07: Get the number of rows in a table

ID: T10.G5.12
Topic: T10 – Lists & Tables
Skill: Delete rows matching a condition
Description: Students use the `delete rows with column [name] of value [v] from table [table]` block to remove ALL rows where a specific column equals a value. They understand this can delete multiple rows at once (e.g., delete all students in grade 8) and is more efficient than looping to delete one by one.
Dependencies:
* T10.G5.11: Delete a single row by index
* T10.G5.08: Find which row contains a value

ID: T10.G5.13
Topic: T10 – Lists & Tables
Skill: Clear all rows from a table
Description: Students use the `delete all rows from table [table]` block to remove all data while preserving the column structure. They understand this is useful for resetting a table for new data without recreating columns, and compare this to deleting entire table vs. just clearing data.
Dependencies:
* T10.G5.11: Delete a single row by index

ID: T10.G5.14
Topic: T10 – Lists & Tables
Skill: Convert between lists and tables
Description: Students convert a list into a single-column table using available table operations and extract a column from a table into a list by looping through rows (or using a dedicated block if available). They understand when each data structure is more appropriate.
Dependencies:
* T10.G5.04: Add rows of data to a table
* T10.G3.02: Add an item to the end of a list
* T07.G3.01: Use a counted repeat loop

ID: T10.G5.15
Topic: T10 – Lists & Tables
Skill: Add a column at a specific position
Description: Students use the `add column [name] at position (n) to table [table]` block to insert a new column at a specific position (1 = first column, 2 = second, etc.). They understand existing columns shift right to make room, and the new column starts empty. They practice adding columns at beginning, middle, and end.
Dependencies:
* T10.G5.03: Create a table and add columns

ID: T10.G5.16
Topic: T10 – Lists & Tables
Skill: Delete a single column
Description: Students use the `delete column [name] from table [table]` block to permanently remove a column and ALL its data. They understand this cannot be undone, remaining columns shift left, and the table structure changes. They identify when column deletion is appropriate vs. just clearing cell values.
Dependencies:
* T10.G5.15: Add a column at a specific position
* T10.G5.04: Add rows of data to a table

ID: T10.G5.17
Topic: T10 – Lists & Tables
Skill: Remove all columns from a table
Description: Students use the `delete all columns from table [table]` block to completely reset a table to empty structure (no columns, no rows). They understand this is more destructive than deleting all rows (which keeps columns) and use this when completely restructuring a table.
Dependencies:
* T10.G5.16: Delete a single column

ID: T10.G5.18
Topic: T10 – Lists & Tables
Skill: Copy list data to table column
Description: Students use the `copy list [list] to column [name] of table [table]` block to populate or replace an entire column with list values. They understand this requires the column to already exist and will overwrite existing data in that column.
Dependencies:
* T10.G5.03: Create a table and add columns
* T10.G3.02: Add an item to the end of a list
* T10.G5.14: Convert between lists and tables

ID: T10.G5.19
Topic: T10 – Lists & Tables
Skill: Insert a row at a specific position
Description: Students use `insert at row (n) of table [table]: [cell1] [cell2] ...` to add a row at a specific position, shifting existing rows down. They understand the difference between appending (always adds at end) and inserting (can add anywhere).
Dependencies:
* T10.G5.04: Add rows of data to a table
* T10.G3.27: Insert an item at a specific position in a list

ID: T10.G5.20
Topic: T10 – Lists & Tables
Skill: Replace an entire row in a table
Description: Students use `replace row (n) of table [table] with: [cell1] [cell2] ...` to overwrite all values in a row at once. They compare this to updating individual cells (T10.G5.06) and understand when replacing entire rows is more efficient.
Dependencies:
* T10.G5.06: Update a cell value in a table
* T10.G5.04: Add rows of data to a table

ID: T10.G5.21
Topic: T10 – Lists & Tables
Skill: Get an entire row as a text string
Description: Students use `row (n) of table [table] separator [sep]` to extract all values from a row as a single text string with specified separator. They use this to display row data, save row snapshots, or pass row data to other parts of the program. They understand this returns text (e.g., "apple,banana,orange"), not a list data structure.
Dependencies:
* T10.G5.05: Read a cell value from a table
* T10.G5.14: Convert between lists and tables
* T10.G4.13: Split a text string into a list

ID: T10.G5.22
Topic: T10 – Lists & Tables
Skill: Find a row by partial match
Description: Students use `row # of item containing [substring] in column [name] in table [table]` to find the first row where a column value includes a substring (e.g., find student with "son" in last name). They compare exact vs partial matching.
Dependencies:
* T10.G5.08: Find which row contains a value
* T10.G4.20: Find an item containing a substring

ID: T10.G5.23
Topic: T10 – Lists & Tables
Skill: Increment or decrement a table cell value
Description: Students use `change item at row (n) column [name] of table [table] by (amount)` to modify numeric cell values arithmetically (e.g., increase a player's score by 10, decrease inventory by 3). For young learners, the `reduce item at row (n) column [name] of table [table] by (amount)` block provides a simpler way to decrease values without negative numbers. Students compare this to replacement (T10.G5.06) and recognize when arithmetic modification is more efficient than get-calculate-replace patterns.
Dependencies:
* T10.G5.06: Update a cell value in a table
* T10.G5.05: Read a cell value from a table
* T10.G3.14: Increment or decrement a list item's value

ID: T10.G5.24
Topic: T10 – Lists & Tables
Skill: Show and hide table monitors
Description: Students use `show table [table]` and `hide table [table]` blocks to display or hide the table monitor on the stage. Applications include debugging programs by observing table state, showing results to users, or hiding implementation details during gameplay.
Dependencies:
* T10.G5.03: Create a table and add columns
* T09.G3.01: Display variable value on stage using the variable monitor

ID: T10.G5.25
Topic: T10 – Lists & Tables
Skill: Trace filter algorithm for tables step by step
Description: Students extend their list filtering skills to tables by tracing the table filter algorithm on paper before coding. Given a source table with 4-5 rows and a condition (e.g., "keep only students with score > 75"), they manually step through: create empty result table with same columns, loop through each row number (1 to row count), read the relevant column value for that row, check if it meets the condition, if yes copy/add that entire row to result table, if no skip to next row. Students track which rows are being examined and which are added to the result, understanding that filtering preserves row integrity (all columns stay together). This tracing-first approach helps students visualize the algorithm flow before managing the more complex syntax of table operations, preventing errors like filtering only one column or losing row data.
Dependencies:
* T10.G4.07: Filter items from a list based on a condition
* T10.G4.08: Trace filter algorithm step by step before implementing
* T10.G5.09: Loop through table rows to compute aggregates

ID: T10.G5.26
Topic: T10 – Lists & Tables
Skill: Build a filtered table manually using conditionals
Description: Students create a new table containing only rows that match a specific condition by looping through the source table and using if-statements. For each row, they check if a column value meets a criterion (e.g., score > 80), and if so, add that row to a result table. This manual filtering approach builds the algorithmic thinking needed before using advanced built-in filter operations in Grade 6. Students trace through 5-7 sample rows and verify their filtered result contains exactly the matching rows.
Dependencies:
* T10.G5.25: Trace filter algorithm for tables step by step
* T10.G5.07: Get the number of rows in a table
* T10.G5.05: Read a cell value from a table
* T10.G5.04: Add rows of data to a table

ID: T10.G5.27
Topic: T10 – Lists & Tables
Skill: Debug table programs by tracing row and column access
Description: Students identify and fix bugs in table programs where cells are accessed at wrong row-column combinations, rows are skipped in loops, or data is written to incorrect positions. Given a buggy program that should update a student gradebook but produces incorrect results, students use step-by-step execution and table monitors to trace which cells are being read or written. They practice common debugging patterns: logging row/column indices during loops, verifying cell values match expectations, and checking loop bounds against row count.
Dependencies:
* T10.G5.05: Read a cell value from a table
* T10.G5.09: Loop through table rows to compute aggregates
* T10.G3.17: Debug a list program by identifying wrong positions

ID: T10.G5.28
Topic: T10 – Lists & Tables
Skill: Compare values across two columns in the same row
Description: Students write programs that compare values in different columns of the same row to make decisions or compute derived values. Examples: compare "budget" and "spent" columns to find rows that are over budget, compare "expected" and "actual" columns to calculate differences, or compare "score1" and "score2" columns to determine which is higher. Students loop through rows, read both column values, apply comparison logic, and either flag rows, update a third column, or count matches.
Dependencies:
* T10.G5.05: Read a cell value from a table
* T10.G5.09: Loop through table rows to compute aggregates
* T08.G4.14: Combine two conditions with AND

ID: T10.G5.29
Topic: T10 – Lists & Tables
Skill: Compare tables vs parallel lists and justify choice
Description: Students analyze scenarios and decide whether parallel lists or a table is the better data structure, then justify their choice. Comparison factors: (1) Tables keep related data visibly together, making it harder to accidentally desynchronize; (2) Tables have built-in lookup and aggregate operations; (3) Parallel lists may be simpler for very basic needs. Given scenarios like "track 3 properties for 20 students," students explain: "A table is better because all student data stays in one row—I can't accidentally add a name without adding a score. Plus I can sort the whole table by any column." Students practice articulating trade-offs to a partner or in writing.
Dependencies:
* T10.G5.02: Identify table structure (rows, columns, cells)
* T10.G4.03: Store and retrieve parallel list data

ID: T10.G5.30
Topic: T10 – Lists & Tables
Skill: Model a real-world scenario with table schema design
Description: Students design a table structure to model a real-world scenario they choose (or are given). Steps: (1) Identify what "things" need to be tracked (these become rows), (2) Identify what properties each thing has (these become columns), (3) Choose appropriate column names, (4) Add sample data to verify the design works. Example scenarios: classroom seating chart, pet adoption records, library book tracking, sports team roster. Students present their design, explain why they chose those columns, and demonstrate with 3-5 sample rows. This design-thinking skill prepares students for database modeling.
Dependencies:
* T10.G5.03: Create a table and add columns
* T10.G5.04: Add rows of data to a table

ID: T10.G5.31
Topic: T10 – Lists & Tables
Skill: Verify table operations produce expected results
Description: Students develop verification habits by checking that table operations produce correct results. Verification techniques: (1) Check row count before and after operations (did add increase by 1? did delete decrease by 1?), (2) Read back a cell value after updating to confirm the change, (3) Use table monitors to visually verify state, (4) Test edge cases (empty table, single row, first/last row operations). Given a table operation to perform, students write verification code that confirms the operation succeeded. This defensive programming skill prevents silent bugs in data manipulation.
Dependencies:
* T10.G5.07: Get the number of rows in a table
* T10.G5.06: Update a cell value in a table
* T10.G5.24: Show and hide table monitors

ID: T10.G5.32
Topic: T10 – Lists & Tables
Skill: Debug table access errors (wrong row, wrong column, missing data)
Description: Students learn to systematically debug common table access errors through a structured troubleshooting process. When a table program produces wrong results or errors, they: (1) verify the table structure (column names and count) using the table monitor, (2) verify row count using `row count of table`, (3) trace through access code checking row numbers are within bounds (1 to row count), (4) verify column names exactly match (case-sensitive, spelling), and (5) check if accessed rows contain expected data (not empty cells). Students practice with deliberately buggy code: accessing row 0 (invalid), using wrong column name "Score" vs "score", accessing beyond row count, and reading from empty tables. This systematic debugging skill builds confidence in table operations and reduces frustration when programs don't work.
Dependencies:
* T10.G5.05: Read a cell value from a table
* T10.G5.27: Debug table programs by tracing row and column access
* T10.G3.17: Debug a list program by identifying wrong positions

ID: T10.G5.33
Topic: T10 – Lists & Tables
Skill: Implement undo functionality using a list as history stack
Description: Students implement undo functionality by using a list as a history stack. Before each action (like moving a sprite, changing a value, or adding/deleting data), they save the previous state to a history list using `add [state] to [history]`. When the user requests undo, they retrieve the last saved state using `item (length of [history]) of [history]`, restore it, then `delete (length of [history]) of [history]` to remove that entry. Students implement a simple drawing program or game where: (1) each action is recorded to history, (2) pressing "U" undoes the last action, (3) the history list shows recent actions. Key insights: the list acts as a stack (LIFO), undo pops the most recent state, and there's a tradeoff between how much history to keep and memory usage. This practical pattern appears in text editors, drawing programs, and games.
Dependencies:
* T10.G3.27: Insert an item at a specific position in a list
* T10.G3.06: Delete an item at a specific position
* T10.G3.05: Get the length of a list

ID: T10.G5.34
Topic: T10 – Lists & Tables
Skill: Debug table programs using console logging and table monitors
Description: Students combine console logging with table monitors for comprehensive debugging of table programs. They use `log [message]` blocks to output: (1) current row number during loops, (2) cell values being read or written, (3) condition evaluation results. They use `show table [table]` to display the table state and observe changes during step-by-step execution. When a table program isn't working (e.g., aggregate is wrong, filter misses rows), students add strategic logs: before and after each row is processed, when conditions evaluate, and when cell values change. They correlate log output with table monitor state to pinpoint where the code diverges from expectations. Students practice debugging a buggy "calculate column total" program, using logs to discover the loop skips the first row.
Dependencies:
* T10.G5.27: Debug table programs by tracing row and column access
* T10.G5.24: Show and hide table monitors
* T10.G3.23: Debug list programs using console logging

ID: T10.G5.35
Topic: T10 – Lists & Tables
Skill: Choose between list of lists vs table for grid data
Description: Students compare two approaches for storing 2D grid data: nested lists (list of lists) versus tables. They analyze trade-offs: (1) Nested lists are flexible for irregular grids and allow direct coordinate access [[row][col]], but lack named columns and built-in operations; (2) Tables have named columns, built-in sorting/filtering/aggregation, but are optimized for records (each row is an entity) not pure grids. Students design solutions for scenarios: (A) Tic-tac-toe board → nested list (3x3 grid, pure position data); (B) Spreadsheet with student grades → table (each row is a student, columns are assignments); (C) Pixel art image → nested list (rows of RGB values); (D) Inventory with name/quantity/price → table (relational data). They implement both approaches for one scenario and compare readability, ease of access, and available operations.
Dependencies:
* T10.G5.29: Compare tables vs parallel lists and justify choice
* T10.G4.36: Store and access items in a list of lists (basic 2D introduction)

ID: T10.G5.36
Topic: T10 – Lists & Tables
Skill: Prepare table data for AI analysis (formatting, cleaning)
Description: Students learn to prepare table data for use with AI features by ensuring proper formatting and data quality. AI blocks work best with clean, consistent data. Students practice: (1) Ensuring column headers are clear and descriptive (AI uses these to understand data), (2) Removing or filling empty cells (AI may error or give poor results with missing data), (3) Standardizing formats (dates, numbers, text case) so AI can process consistently, (4) Removing duplicate rows that could skew AI analysis. Given a messy table (inconsistent names, empty cells, mixed formats), students clean it using table operations before passing to AI analysis blocks. They compare AI results before and after cleaning to see the impact of data quality. This practical skill prepares students for real-world AI data workflows where "garbage in = garbage out."
Dependencies:
* T10.G5.09: Loop through table rows to compute aggregates
* T10.G5.06: Update a cell value in a table
* T10.G5.12: Delete rows matching a condition

ID: T10.G5.37
Topic: T10 – Lists & Tables
Skill: Anonymize table data by removing identifying columns
Description: Students practice data anonymization by removing or masking columns that could identify individuals. Given a table with sensitive data (student gradebook with Name, ID, Address, Grade, Score), students identify which columns are identifying vs. non-identifying, then create an anonymized version by: (1) deleting columns that directly identify (Name, ID), (2) masking partial identifiers (truncate Address to just city), (3) keeping only data needed for analysis (Grade, Score). They verify anonymization by checking: "Can I figure out who this row is about?" Real-world applications: sharing survey results without revealing who said what, publishing research data, creating demo datasets. Ethics discussion: why do researchers anonymize data before sharing? What could go wrong if we don't? This builds on G4.46 (identifying sensitive data) by teaching students how to protect it.
Dependencies:
* T10.G4.38: Identify sensitive data that should not be shared
* T10.G5.15: Add a column at a specific position
* T10.G5.11: Delete a single row by index

ID: T10.G5.38
Topic: T10 – Lists & Tables
Skill: Design tables for multiplayer game state synchronization
Description: Students design table schemas for multiplayer game scenarios where data must be shared between players. They consider: (1) What data needs to be synchronized (player positions, scores, game state), (2) How to structure tables so updates are efficient (separate tables for frequently-changing vs. stable data), (3) How to identify which player each row belongs to (player ID column). Example: A multiplayer racing game needs tables for: PlayerInfo (ID, Name, CarColor - set once), PlayerPosition (ID, X, Y, Speed - update constantly), RaceState (CurrentLap, TimeRemaining, Leader - shared state). Students design schemas for 2-3 multiplayer scenarios, identifying which data changes often vs. rarely and why that matters for synchronization. This prepares students for cloud variables and multiplayer features in later skills.
Dependencies:
* T10.G5.30: Model a real-world scenario with table schema design
* T10.G5.03: Create a table and add columns

ID: T10.G5.39
Topic: T10 – Lists & Tables
Skill: Debug infinite loops in list/table operations
Description: Students identify and fix infinite loops that can occur when modifying lists or tables during iteration. Common bugs: (1) Deleting items while looping forward (indices shift, causing skipped items or infinite loops), (2) Adding items inside a loop that iterates over the list (list keeps growing), (3) Loop condition never becomes false (e.g., `repeat until <list empty>` but nothing deletes items). For each bug pattern, students: trace through to see why it's infinite, identify the root cause, and implement a fix (loop backwards when deleting, collect items to add/delete in a separate list first, verify loop termination condition). They practice with a buggy "remove all items > 5" program that gets stuck because indices shift after each delete. This debugging skill prevents one of the most frustrating programming problems.
Dependencies:
* T10.G5.09: Loop through table rows to compute aggregates
* T10.G3.06: Delete an item at a specific position
* T10.G5.12: Delete rows matching a condition

ID: T10.G5.40
Topic: T10 – Lists & Tables
Skill: Process live user input into table in real-time
Description: Students build programs that continuously capture user input and store it in tables, creating real-time data collection applications. Example projects: (1) Live quiz: each answer adds a row (timestamp, question#, answer, correct/wrong), (2) Drawing tracker: mouse position sampled every 0.1 seconds into position table, (3) Reaction time game: record time between stimulus and keypress. Students implement: input capture (keyboard, mouse, timer events), immediate storage to table, and live display of accumulated data. They learn to balance sampling rate (how often to capture) with data size (tables grow quickly with frequent sampling). Real-world connections: fitness trackers capturing heart rate, game analytics recording player actions, keystroke timing in typing tests. This skill bridges static data entry to dynamic, event-driven data collection.
Dependencies:
* T10.G5.04: Add rows of data to a table
* T10.G5.07: Get the number of rows in a table
* T10.G5.24: Show and hide table monitors

## GRADE 6 (31 skills)

ID: T10.G6.01
Topic: T10 – Lists & Tables
Skill: Sort a table by a column
Description: Students use CreatiCode's `sort table [table] by column [name] [large to small/small to large]` block to reorder rows based on values in a column. They understand sorting preserves row integrity (all columns in a row stay together). Students verify the sort worked by reading cell values before and after.
Dependencies:
* T10.G4.04: Use built-in blocks to sort a list
* T10.G5.05: Read a cell value from a table

ID: T10.G6.02
Topic: T10 – Lists & Tables
Skill: Filter table rows based on a condition
Description: Students loop through a table and identify rows where a column value meets a condition (e.g., "find all students with score > 80"). They collect matching row numbers into a list or build a new filtered table containing only matching rows. Students verify their filter by checking that all rows in the result satisfy the condition.
Dependencies:
* T10.G5.26: Build a filtered table manually using conditionals
* T08.G5.02: Use compound conditions with and/or/not

ID: T10.G6.03
Topic: T10 – Lists & Tables
Skill: Copy and append tables
Description: Students use `copy table [t1] into [t2]` to duplicate a table and `append table [t1] to [t2]` to combine tables vertically. Vertical appending adds new rows below existing rows; both tables must have matching columns for append to work correctly.
Dependencies:
* T10.G5.04: Add rows of data to a table

ID: T10.G6.04
Topic: T10 – Lists & Tables
Skill: Use table lookup to find related data
Description: Students use the `item in column [return_col] of [table] where column [search_col] equals [value]` block to look up data. For example, find a student's grade by looking up their name, similar to VLOOKUP in spreadsheets.
Dependencies:
* T10.G5.08: Find which row contains a value
* T10.G5.05: Read a cell value from a table

ID: T10.G6.05
Topic: T10 – Lists & Tables
Skill: Group data and compute aggregates per group
Description: Students use CreatiCode's `set table [result] to [method] of column [value_col] in table [source] by column [group_col]` block to group rows by a category and compute statistics (sum, average, count) for each group, creating a summary table.
Dependencies:
* T10.G5.10: Use built-in table aggregate blocks
* T10.G6.02: Filter table rows based on a condition

ID: T10.G6.06
Topic: T10 – Lists & Tables
Skill: Use set operations on lists
Description: Students implement set operations like union (all unique items from both lists), intersection (only items in both lists), and difference (items in list1 but not list2) using loops and conditionals. They understand mathematical set concepts applied to lists.
Dependencies:
* T10.G4.07: Filter items from a list based on a condition
* T10.G3.10: Check if a list contains a specific item

ID: T10.G6.07
Topic: T10 – Lists & Tables
Skill: Remove duplicate items from a list
Description: Students write code to remove duplicate values from a list, keeping only one instance of each unique value. They loop through the list, check if each item already exists in a result list, and add only unique items.
Dependencies:
* T10.G3.10: Check if a list contains a specific item
* T10.G4.07: Filter items from a list based on a condition

ID: T10.G6.08
Topic: T10 – Lists & Tables
Skill: Shuffle table rows randomly
Description: Students use the `reshuffle table [table] randomly` block to randomize row order while keeping row integrity (all columns in a row stay together). Applications include randomizing quiz questions stored in tables, shuffling game data, or anonymizing datasets for privacy.
Dependencies:
* T10.G4.16: Randomly shuffle items in a list
* T10.G5.04: Add rows of data to a table

ID: T10.G6.09
Topic: T10 – Lists & Tables
Skill: Create and populate a nested list (2D array)
Description: Students create a list where each item is itself a list, forming a 2D grid structure. For example, a 3x3 tic-tac-toe board can be represented as a list of 3 rows, where each row is a list of 3 cells. Students create the structure by making an outer list, then adding inner lists as items. They populate cells by first accessing the inner list, then setting items within it. This introduces the concept of nested data structures as an alternative to tables for grid-based data.
Dependencies:
* T10.G4.03: Store and retrieve parallel list data
* T10.G3.27: Insert an item at a specific position in a list
* T10.G3.28: Replace an item in a list

ID: T10.G6.10
Topic: T10 – Lists & Tables
Skill: Trace nested list access patterns (row then column)
Description: Students practice the two-step access pattern for 2D nested lists through explicit tracing exercises. Given a nested list representing a grid (e.g., [[1,2,3], [4,5,6], [7,8,9]] for a 3x3 grid), they trace through accessing specific cells: to get row 2, column 3, first use `item (2) of [grid]` to get the inner list [4,5,6], then use `item (3) of (...)` to get 6 from that inner list. Students draw grid diagrams with row and column numbers, identify target cells, write the two-step access code, and verify by running it. They also practice the reverse: given access code like `item (1) of (item (3) of [grid])`, they identify which cell is being accessed (row 3, column 1). This explicit tracing builds fluency with nested access syntax and prevents common errors like reversing row/column order or trying to access a 2D list with a single index.
Dependencies:
* T10.G6.09: Create and populate a nested list (2D array)
* T10.G3.03: Trace list index access step by step

ID: T10.G6.11
Topic: T10 – Lists & Tables
Skill: Access elements in a nested list using row and column indices
Description: Students read and write values in a 2D list using two indices: first to select the row (outer list item), then to select the column (inner list item). For example, to get the value at row 2, column 3 of a grid, they use `item 3 of (item 2 of grid)`. Students practice navigating the nested structure and recognize that accessing requires two steps: outer index first, then inner index.
Dependencies:
* T10.G6.10: Trace nested list access patterns (row then column)
* T10.G4.19: Loop through list indices

ID: T10.G6.12
Topic: T10 – Lists & Tables
Skill: Iterate through all elements of a 2D array with nested loops
Description: Students use nested loops to visit every cell in a 2D array: the outer loop iterates through rows (1 to number of rows), and the inner loop iterates through columns (1 to number of columns in that row). For each cell, they perform an operation like summing values, finding the maximum, or checking for a condition. Students trace through a 3x3 grid and predict the order in which cells are visited (row-major order).
Dependencies:
* T10.G6.11: Access elements in a nested list using row and column indices
* T07.G6.01: Trace nested loops with variable bounds

ID: T10.G6.13
Topic: T10 – Lists & Tables
Skill: Implement queue operations (enqueue and dequeue)
Description: Students implement queue behavior using a list: enqueue (add to end), dequeue (remove and return first item), and peek (read first item without removing). They use `add [item] to [queue]` for enqueue, `item (1) of [queue]` with `delete (1) of [queue]` for dequeue, and recognize FIFO (First-In-First-Out) behavior. Applications include task queues (process tasks in order received), print queues, breadth-first traversal, and simulating waiting lines. Students contrast FIFO (queue) with LIFO (stack) behavior by tracing the same operations on both data structures.
Dependencies:
* T10.G3.27: Insert an item at a specific position in a list
* T10.G3.06: Delete an item at a specific position
* T10.G3.05: Get the length of a list

ID: T10.G6.14
Topic: T10 – Lists & Tables
Skill: Use frequency counting with lists
Description: Students count occurrences of each unique value in a list by using parallel lists (one for unique values, one for counts). They loop through the source list, check if each item exists in the values list, and either increment its count or add a new entry. This technique enables finding the most/least frequent items, creating histograms, and analyzing data distributions. Students apply this to real scenarios like counting votes, tallying survey responses, or finding the mode of a dataset.
Dependencies:
* T10.G4.03: Store and retrieve parallel list data
* T10.G3.26: Find an item's position using built-in block
* T10.G3.14: Increment or decrement a list item's value

ID: T10.G6.15
Topic: T10 – Lists & Tables
Skill: Merge two sorted lists into one sorted list
Description: Students implement the merge algorithm: given two already-sorted lists, combine them into one sorted list without re-sorting. They use two pointers (one for each list), repeatedly compare the current items, add the smaller one to the result, and advance that pointer. This O(n) algorithm is more efficient than concatenating and re-sorting O(n log n), and is a building block for merge sort. Students trace through merging [1, 4, 7] and [2, 3, 8] step by step.
Dependencies:
* T10.G4.04: Use built-in blocks to sort a list
* T10.G4.19: Loop through list indices
* T10.G3.12: Check if a list is empty before accessing

ID: T10.G6.16
Topic: T10 – Lists & Tables
Skill: Swap adjacent items based on comparison
Description: Students practice the swap pattern in the context of sorting: compare two adjacent items, swap them if out of order, and recognize that multiple passes are needed to fully sort. They trace through swapping adjacent pairs and observe how items gradually move toward correct positions. This builds directly toward implementing bubble sort and selection sort algorithms in Grade 8.
Dependencies:
* T10.G4.10: Swap two items in a list
* T10.G4.19: Loop through list indices

ID: T10.G6.17
Topic: T10 – Lists & Tables
Skill: Find maximum in a sublist range
Description: Students extend the manual find-max algorithm (T10.G4.06) to find the maximum or minimum within a specific range of indices, not the entire list. They loop from a start position to an end position, tracking the best value and its position. This pattern is essential for selection sort (find min in remaining unsorted portion) and other range-based algorithms.
Dependencies:
* T10.G4.06: Find the maximum or minimum item in a list manually
* T10.G4.22: Extract a sublist from a range of positions

ID: T10.G6.18
Topic: T10 – Lists & Tables
Skill: Parse text into structured list data
Description: Students use text splitting and string operations to parse semi-structured text (like CSV lines, simple log entries, or formatted strings) into list items for programmatic processing. They use the split block to break text by delimiters, handle edge cases like extra spaces, and build lists from parsed text. This bridges text manipulation and list operations, preparing for complex data parsing in Grade 8.
Dependencies:
* T10.G4.13: Split a text string into a list
* T10.G4.07: Filter items from a list based on a condition

ID: T10.G6.19
Topic: T10 – Lists & Tables
Skill: Select a random item from a list
Description: Students use the `item (random v) of [list]` block or generate a random index using `pick random (1) to (length of [list])` to select items at random. Applications include picking random quiz questions, selecting random game events, or implementing simple random sampling. Students verify that multiple runs produce different selections and understand the difference between random access and sequential access.
Dependencies:
* T10.G4.19: Loop through list indices
* T10.G4.16: Randomly shuffle items in a list

ID: T10.G6.20
Topic: T10 – Lists & Tables
Skill: Filter table rows using OR conditions
Description: Students extend filtering to OR conditions, finding rows that match ANY of several criteria. For example, "find all students who scored above 90 OR are in grade 8" requires checking two conditions and including the row if EITHER is true. Students implement this with `if <condition1> or <condition2>` inside a loop, understanding that OR is more inclusive than AND (more rows match). They compare results: AND filtering returns fewer rows (must meet ALL conditions), OR filtering returns more rows (must meet ANY condition). Applications include searching for records that could match multiple categories.
Dependencies:
* T10.G6.02: Filter table rows based on a condition
* T08.G5.02: Use compound conditions with and/or/not

ID: T10.G6.21
Topic: T10 – Lists & Tables
Skill: Choose between filtering and sorting for a data task
Description: Students analyze data tasks and decide whether filtering, sorting, or both is the appropriate operation. Decision framework: Filtering REMOVES rows that don't match (when you only want certain items), Sorting REORDERS all rows (when you want everything but in a different order), Sometimes you need both (filter first, then sort the results). Given scenarios: (1) "Show only students who passed" → Filter, (2) "Show all students ranked by score" → Sort, (3) "Show the top 5 highest scores" → Sort then take first 5 (or filter by threshold). Students justify their operation choice and implement the solution.
Dependencies:
* T10.G6.02: Filter table rows based on a condition
* T10.G6.01: Sort a table by a column

ID: T10.G6.22
Topic: T10 – Lists & Tables
Skill: Verify data transformation correctness
Description: Students develop verification strategies for data transformations: after filtering, sorting, or aggregating, how do you know the result is correct? Techniques: (1) Check result count matches expectations (filtered result should be smaller), (2) Spot-check specific values (does the first sorted item have the smallest value?), (3) Verify aggregates manually on small test data (calculate sum by hand, compare to code result), (4) Check that no data was accidentally lost or duplicated. Students practice verifying transformations and articulate what "correct" means for each operation type.
Dependencies:
* T10.G6.02: Filter table rows based on a condition
* T10.G6.05: Group data and compute aggregates per group
* T10.G5.31: Verify table operations produce expected results

ID: T10.G6.23
Topic: T10 – Lists & Tables
Skill: Implement a simple lookup cache with lists
Description: Students implement a basic caching pattern: store recently looked-up values to avoid redundant searching. Using two parallel lists (keys and values), they check if a key is already cached before doing an expensive lookup. If found in cache, return immediately; if not, perform the lookup, store the result in the cache, then return it. This introduces the concept of time-space trade-offs: using memory (cache) to save time (avoid repeated searches). Students measure the performance difference with and without caching on repeated lookups.
Dependencies:
* T10.G6.04: Use table lookup to find related data
* T10.G4.03: Store and retrieve parallel list data
* T10.G3.26: Find an item's position using built-in block

ID: T10.G6.24
Topic: T10 – Lists & Tables
Skill: Choose between table, nested list, or parallel lists for a scenario
Description: Students compare three multi-dimensional data structures and justify their choice for specific scenarios. They analyze the tradeoffs: (1) Tables have built-in column names and aggregate functions, ideal for heterogeneous data (student: name, age, grade); (2) Nested lists are flexible for homogeneous grid data (game boards, images as pixel grids); (3) Parallel lists are simpler when only 2-3 attributes need to be tracked together. Given scenarios (store chess board state, track inventory with name/quantity/price, record game scores over time), students sketch data layouts for each approach, identify pros and cons (e.g., tables are clearer but more complex to set up; nested lists are compact but harder to read; parallel lists can get out of sync), and choose the best fit. They implement their choice and explain why alternatives would be less suitable. This design skill synthesizes data structure knowledge into practical decision-making.
Dependencies:
* T10.G5.29: Compare tables vs parallel lists and justify choice
* T10.G6.09: Create and populate a nested list (2D array)
* T10.G5.02: Identify table structure (rows, columns, cells)

ID: T10.G6.25
Topic: T10 – Lists & Tables
Skill: Model simple graph relationships using table as adjacency list
Description: Students learn to represent graph-like relationships using tables where one column stores a node and another column stores its connections. Example: a social network where each person can have multiple friends. Table structure: columns "Person" and "Friend" with multiple rows per person (Sam-Lia, Sam-Max, Lia-Max represents Sam knows Lia and Max, Lia knows Max). Students implement: (1) Add a friendship (add row), (2) Find all friends of a person (filter by Person column), (3) Check if two people are friends (search for row), (4) Count friends per person (group and count). They understand this "adjacency list" representation where relationships are stored as pairs, and compare it to a full grid/matrix approach (which would have many empty cells for sparse connections). This introduces graph thinking using familiar table operations.
Dependencies:
* T10.G6.02: Filter table rows based on a condition
* T10.G6.05: Group data and compute aggregates per group
* T10.G5.08: Find which row contains a value

ID: T10.G6.26
Topic: T10 – Lists & Tables
Skill: Critique a peer's data structure choice and suggest improvements
Description: Students review a peer's data structure design (or a provided example design) and provide constructive critique. Given a scenario and a proposed solution (e.g., "Track library books using parallel lists: titles, authors, available"), students analyze: (1) Does the structure fit the requirements? (2) Are there edge cases it handles poorly? (3) Could a different structure (table, nested list) work better? (4) What happens when the data grows? Students write a critique that includes: what works well, potential problems, and a specific suggestion for improvement with reasoning. Example critique: "Parallel lists work for basic tracking, but if books have multiple authors, you'd need to restructure. A table with a 'BookID' column and separate Authors table would handle this better." This peer review skill develops critical thinking about design choices and prepares students for code review practices.
Dependencies:
* T10.G6.24: Choose between table, nested list, or parallel lists for a scenario
* T10.G5.29: Compare tables vs parallel lists and justify choice
* T10.G4.30: Design data structure for a simple scenario (list vs multiple variables)

ID: T10.G6.27
Topic: T10 – Lists & Tables
Skill: Justify data structure choice in written documentation
Description: Students write formal documentation explaining and justifying their data structure choices for a project. Documentation includes: (1) Requirements analysis—what data needs to be stored and how it will be accessed, (2) Options considered—list the 2-3 data structures that could work, (3) Trade-off analysis—compare each option on criteria like ease of access, memory efficiency, operation speed, code readability, (4) Final decision and rationale—state what was chosen and the key reasons why. Students practice with a game inventory scenario, documenting why they chose a table over parallel lists: "A table was chosen because inventory items have 4+ properties (name, quantity, value, category), the table's built-in sorting allows displaying by any property, and row integrity prevents the synchronization bugs that parallel lists would introduce." This documentation skill prepares students for professional software development where design decisions must be communicated to team members.
Dependencies:
* T10.G6.26: Critique a peer's data structure choice and suggest improvements
* T10.G6.24: Choose between table, nested list, or parallel lists for a scenario

ID: T10.G6.28
Topic: T10 – Lists & Tables
Skill: Design table schemas optimized for AI processing
Description: Students learn to design table schemas specifically optimized for AI feature processing. AI blocks have specific requirements: (1) Semantic search databases need a 'key' column with searchable text, (2) KNN classification needs clearly separated feature columns and a label column, (3) Chart visualization needs numeric columns and appropriate category columns. Students design tables for AI scenarios: (A) FAQ system for semantic search—design with question (key), answer, category columns; (B) Flower classifier—design with petal_length, petal_width, species columns for KNN; (C) Sales dashboard—design with month, product, revenue columns for charts. For each, they identify which columns the AI will process, ensure correct data types (numbers for calculations, text for search), and add sample data to test. This forward-thinking design skill ensures data is AI-ready from the start.
Dependencies:
* T10.G6.26: Critique a peer's data structure choice and suggest improvements
* T10.G5.36: Prepare table data for AI analysis (formatting, cleaning)

ID: T10.G6.29
Topic: T10 – Lists & Tables
Skill: Parse and store AI-generated text data in tables
Description: Students learn that AI services often return data as formatted text (CSV-like strings, structured text, or key-value pairs) rather than pre-structured tables. They practice parsing these AI responses: split by delimiters, extract key fields, and store in table columns. Example: An AI returns product info as "Name: Widget Pro, Price: $29.99, Rating: 4.5 stars" → use text operations to extract name ("Widget Pro"), price (29.99), and rating (4.5) → store each in appropriate table columns. Pattern: (1) identify the format pattern in AI output, (2) split or search to isolate each field, (3) clean the data (remove "$", convert to number), (4) add to table. Students practice with 3-4 different AI response formats and build robust parsing that handles variations. This skill is essential because AI doesn't always return perfectly structured data—knowing how to parse messy text into clean tables is a real-world data engineering skill.
Dependencies:
* T10.G4.13: Split a text string into a list
* T10.G5.04: Add rows of data to a table
* T10.G5.36: Prepare table data for AI analysis (formatting, cleaning)

ID: T10.G6.30
Topic: T10 – Lists & Tables
Skill: Compare algorithm speed with different list sizes
Description: Students run empirical experiments to understand how algorithm performance changes with data size. They measure execution time using timer blocks for the same operation on lists of different sizes (10, 100, 500, 1000 items). Experiments: (1) Linear search vs binary search (on sorted list) - observe that binary search stays fast while linear search slows dramatically; (2) Finding maximum with loop - observe linear growth in time; (3) Sorting with built-in sort - observe that time grows but not as fast as expected. Students create a simple table or chart showing size vs time for each approach and make observations: "When the list got 10x bigger, linear search took about 10x longer, but binary search barely changed!" This introduces empirical performance analysis without formal Big-O notation—students develop intuition for algorithm efficiency through hands-on measurement before the formal analysis in G8.
Dependencies:
* T10.G4.02: Implement manual linear search with loop
* T10.G4.04: Use built-in blocks to sort a list
* T10.G6.01: Sort a table by a column

ID: T10.G6.31
Topic: T10 – Lists & Tables
Skill: Handle concurrent data updates in shared tables
Description: Students learn strategies for handling concurrent updates when multiple users or processes modify the same table data. They explore problems that arise: (1) Lost updates (two users read same value, both add 1, but result only shows +1 instead of +2), (2) Inconsistent reads (reading while another update is in progress), (3) Race conditions (outcome depends on timing). Students implement strategies: (1) Read-modify-write atomically (get current value, compute new value, update immediately), (2) Timestamp-based updates (only accept update if timestamp is newer), (3) Version numbers (reject update if version changed since read). Practice scenario: multiplayer game scoreboard where multiple players might score simultaneously. Students simulate concurrent updates and observe problems, then implement solutions. This real-world skill prepares students for collaborative applications and database concepts.
Dependencies:
* T10.G5.38: Design tables for multiplayer game state synchronization
* T10.G6.04: Use table lookup to find related data
* T10.G5.06: Update a cell value in a table

