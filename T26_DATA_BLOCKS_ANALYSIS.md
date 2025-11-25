# T26 Data Collection & Logging - Available CreatiCode Blocks

## Analysis Date: 2025-11-25
## Source: /media/binyu/USB2/ScratchCopilot/blockdes8.txt

---

## 1. DATA COLLECTION & STORAGE

### 1.1 Variables (Category: Variables)

#### Basic Variable Operations
- **export variable [VARIABLE v]**
  - Exports variable content to a txt file with the variable's name
  - Works with both regular variables and lists

- **import variable [VARIABLE v]**
  - Opens file dialog to select txt or csv file
  - Reads content and stores in the variable
  - If no file selected, variable remains unchanged

#### Server-Based Data Persistence
- **save [VISIBILITY v] data [VALUE] with name [KEY]**
  - Saves data to server database with specified KEY
  - VISIBILITY: 'public' (all users of project) or 'private' (only this user)
  - Data stored per project
  - Block ID: data_savedata

- **load data named [KEY]**
  - Reporter block that returns data stored with KEY
  - Respects VISIBILITY (can only read private data if you saved it)
  - Block ID: data_loaddata

- **remove [VISIBILITY v] data named [KEY]**
  - Removes data stored with specified KEY
  - VISIBILITY: 'public' or 'private'
  - Block ID: data_removedata

- **data names**
  - Reporter block returning all data names in project
  - Returns list separated by '&&' (e.g., 'a&&b&&c')
  - Block ID: data_load_data_names

---

## 2. LISTS (Category: Variables)

### 2.1 List Modification
- **add to [LISTNAME v] item [VALUE]** (Standard Scratch)
- **delete (INDEX) of [LISTNAME v]** (Standard Scratch)
- **delete all of [LISTNAME v]** (Standard Scratch)
- **insert [VALUE] at (INDEX) of [LISTNAME v]** (Standard Scratch)
- **replace item (INDEX) of [LISTNAME v] with [VALUE]** (Standard Scratch)

### 2.2 Extended List Operations

#### Item Modification
- **reduce item (INDEX) of [LISTNAME v] by (N)**
  - Reduces value at INDEX by N
  - Simpler for young learners than negative numbers
  - Block ID: data_reduceitemoflist

- **change item (INDEX) of [LISTNAME v] by (N)**
  - Changes value at INDEX by N
  - Block ID: data_changeitemoflist

- **delete value [V] from [LISTNAME v]**
  - Finds first item with value V and deletes it
  - Block ID: data_deletevalueoflist

#### List Ordering
- **reverse [LISTNAME v]**
  - Reverses order of all items
  - Block ID: data_reverselist

- **reshuffle [LISTNAME v] randomly**
  - Randomly reshuffles all items
  - Block ID: data_reshuffle

- **sort list [LISTNAME v] from [METHOD v]**
  - METHOD: 'large to small' or 'small to large'
  - Block ID: data_sortlistby

#### List Combination
- **copy [LISTNAME1 v] to [LISTNAME2 v]**
  - Copies all items, replacing existing in LISTNAME2
  - Both lists identical after operation
  - Block ID: data_copytolist

- **append [LISTNAME1 v] to [LISTNAME2 v]**
  - Appends LISTNAME1 items to end of LISTNAME2
  - Block ID: data_appendtolist

- **insert (N) [SELECTOR v] items from [LISTNAME1 v] into [LISTNAME2 v]**
  - Selects N items from LISTNAME1, appends to LISTNAME2
  - SELECTOR: 'largest', 'smallest', or 'random'
  - Block ID: data_insertitemsfromlist

#### List Generation
- **set [LISTNAME v] to (N) random whole numbers between (MIN) and (MAX) [REPEATMETHOD v]**
  - Populates list with N random numbers
  - REPEATMETHOD: 'no repetition' or 'allow repetition'
  - Block ID: data_setrandomlist

- **set [LISTNAME v] to (N) random numbers with seed (SEED)**
  - Uses SEED for reproducible random sequences
  - Same SEED = same sequence (useful for shared puzzles)
  - Numbers between 0 and 1
  - Block ID: data_setrandomlistseed

### 2.3 List Analysis

- **[METHOD v] of list [LISTNAME v]**
  - METHOD: smallest, largest, sum, average, median
  - Reporter block
  - Block ID: data_itemspecificvalueoflist

- **# of item containing [TEXT] in [LISTNAME v]**
  - Returns position of first item containing TEXT as substring
  - Reporter block
  - Block ID: data_itemnumoflist2

- **item (INDEX) of [LISTNAME v]** (Standard Scratch reporter)
- **length of [LISTNAME v]** (Standard Scratch reporter)
- **[LISTNAME v] contains [VALUE]?** (Standard Scratch boolean)

### 2.4 List Text Operations

- **join [LISTNAME v] into text with [SEPARATOR]**
  - Joins all items into one text with SEPARATOR
  - Use '\n' for multiple lines
  - Example: ['a','b','c'] with ',' → 'a,b,c'
  - Block ID: data_joinlistwith

- **set [LISTNAME v] to split of [TEXT] with splitter [SEPARATOR]**
  - Splits TEXT by SEPARATOR, stores parts in list
  - For multi-line split by '\n', use '\\n' (escaped)
  - Block ID: data_set_list_to_split_of

- **regex [REGEXPATTERN] flag [FLAG] match [TEXT] into list [LISTNAME v]**
  - Matches REGEXPATTERN in TEXT, stores matches in list
  - FLAG 'g' = all matches, empty = first match only
  - Example: regex [\d] flag [g] match [a01b2c3] → [0,1,2,3]
  - Block ID: operator_regex_match_into_list

- **regex [REGEXPATTERN] flag [FLAG] split [TEXT] into list [LISTNAME v]**
  - Splits TEXT using REGEXPATTERN as separator
  - Stores parts in list
  - Block ID: operator_regex_split_into_list

### 2.5 List Iteration

- **for each item [VARIABLENAME v] in [LISTNAME v]**
  - C-block that iterates through all items
  - Variable takes value of each item
  - Block ID: data_for_each

- **for each index [INDEXVARIABLENAME v] in [LISTNAME v]**
  - C-block that iterates through all items
  - Variable takes index of each item (starting at 1)
  - Block ID: data_for_each_index

---

## 3. TABLES (Category: Variables)

### 3.1 Table Import/Export

- **export table [TABLENAME v] as [FILENAME]**
  - Exports table as CSV file
  - If FILENAME empty, uses table name
  - Extension '.csv' added automatically
  - Block ID: data_exporttable

- **import file into table [TABLE]**
  - Opens file dialog to select txt or csv file
  - Reads and splits content into rows/columns
  - Stores in table variable
  - Block ID: data_importtable

- **save table [TABLE v] to server as [DATANAME]**
  - Saves entire table to CreatiCode server
  - Block ID: data_savetable

- **load [DATANAME] from server into table [TABLE v]**
  - Loads data from CreatiCode server into table
  - Block ID: data_loadtable

### 3.2 Table Row Operations

- **add to table [TABLENAME v]: [CELL1] [CELL2] ... [CELL12]**
  - Appends new row at bottom with up to 12 values
  - Empty inputs ignored
  - Block ID: data_addrowtotable

- **insert at row (ROWNUM) of table [TABLENAME v]: [CELL1] [CELL2] ... [CELL12]**
  - Inserts new row at ROWNUM (1-indexed)
  - Up to 12 cell values
  - Block ID: data_insertrowtotable

- **replace row (ROWNUM) of table [TABLENAME v] with: [CELL1] [CELL2] ... [CELL12]**
  - Replaces data in row at ROWNUM
  - Up to 12 cell values
  - Block ID: data_replacerowoftable

- **delete row (ROWNUM) of table [TABLENAME v]**
  - Deletes row at ROWNUM, shifts rows below up
  - Block ID: data_deleterowoftable

- **delete all rows from table [TABLENAME v]**
  - Deletes all rows, keeps columns
  - Block ID: data_deleteallrowsfromtable

- **row (ROWINDEX) of table [TABLENAME v] separator [SEPARATOR]**
  - Reporter: returns all data in row joined by SEPARATOR
  - Block ID: data_rowatindexoftable

### 3.3 Table Column Operations

- **delete column [COLUMNNAME] from table [TABLENAME v]**
  - Deletes specified column
  - Block ID: data_deletecolumnfromtable

- **delete all columns from table [TABLENAME v]**
  - Deletes all columns, table becomes empty
  - Block ID: data_removeallcolumnsfromtable

### 3.4 Table Cell Operations

- **item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v]**
  - Reporter: returns content of one cell
  - Block ID: data_itematrowcolumnoftable

### 3.5 Table Analysis

- **row count of table [TABLENAME v]**
  - Reporter: returns total number of rows
  - Block ID: data_rowcountoftable

- **[METHOD] of column [COLUMNNAME] in table [TABLE v]**
  - Aggregates column data
  - METHOD: smallest, largest, sum, average, median
  - Reporter block
  - Block ID: data_columnstatoftable

### 3.6 Table Organization

- **reshuffle table [TABLENAME v] randomly**
  - Randomly reshuffles table rows
  - Block ID: data_reshuffletable

- **sort table [TABLENAME v] by column [COLUMN] [SORTORDER v]**
  - Sorts by specified column
  - SORTORDER: 'large to small' or 'small to large'
  - Block ID: data_sorttable

### 3.7 Table Combination

- **copy table [TABLE1] into [TABLE2]**
  - Copies all rows, replaces existing in TABLE2
  - Both tables identical after operation
  - Block ID: data_copytable

- **append table [TABLE1] to [TABLE2]**
  - Appends TABLE1 rows to bottom of TABLE2
  - Tables should have same columns
  - Block ID: data_appendtable

### 3.8 Advanced Table Operations

- **set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2]**
  - Aggregates data from TABLENAME2 into TABLENAME1
  - Groups by COLUMN2 values, aggregates COLUMN1
  - METHOD: minimum, maximum, sum, average, median
  - Requires at least 2 tables in project
  - Block ID: data_settabletocomputed

- **pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST]**
  - Pivot table operation
  - Block ID: data_pivottable

---

## 4. DATABASE (Category: Database)

### 4.1 Database Collections

- **insert from table [TABLENAME v] row from (STARTROW) to (ENDROW) into collection [COLLECTIONNAME v]**
  - Inserts rows from table into database collection
  - Uses table as intermediate storage
  - Block ID: database_insert_from_table

- **fetch from collection [COLLECTIONNAME v] into table [TABLENAME v] where <CONDITION> limit (LIMIT) sort by (SORTFIELD1) [SORTORDER1 v] (SORTFIELD2) [SORTORDER2 v]**
  - Fetches data from collection into table
  - Optional CONDITION filter
  - Optional sorting by up to 2 fields (1=ascending, -1=descending)
  - Block ID: database_find_from_collection

- **update collection [COLLECTIONNAME v] from table [TABLENAME v]**
  - Updates collection rows with table data
  - Table rows must have been fetched from collection first (maintains hidden 'id')
  - Block ID: database_update_collection

- **update collection [COLLECTIONNAME v] in-place where <CONDITION> set (FIELD1) to (VALUE1) set (FIELD2) to (VALUE2) set (FIELD3) to (VALUE3) set (FIELD4) to (VALUE4)**
  - Updates rows matching CONDITION
  - Can update up to 4 fields at once
  - If CONDITION empty, updates all rows
  - Block ID: database_update_collection_inplace

- **remove all documents from collection [COLLECTIONNAME v] where <CONDITION>**
  - Removes rows matching CONDITION
  - If CONDITION empty, removes all rows
  - Block ID: database_remove_all_document

- **collection [COLLECTIONNAME]**
  - Reporter: returns collection definition (field names and types)
  - Format: [[{"field":"name","type":"string"},{"field":"age","type":"number"}]]
  - Block ID: database_collection

### 4.2 Database Condition Blocks

- **<cond (field [FIELDNAME]) [COMPARATOR v] [INPUT2]>**
  - Boolean comparator: >, <, =, ≠, ≥, ≤
  - Each input can be value or field
  - Block ID: database_condition_compare

- **<cond (field [FIELDNAME]) contains [TEXT]?>**
  - Boolean: checks if field contains TEXT
  - Block ID: database_condition_contains

- **<cond <> and <>>**
  - Boolean AND operator
  - Block ID: database_condition_and

- **<cond <> or <>>**
  - Boolean OR operator
  - Block ID: database_condition_or

- **<cond not <>>**
  - Boolean NOT operator
  - Block ID: database_condition_not

- **field [FIELDNAME]**
  - Reporter: specifies field in collection
  - Block ID: database_field

- **op [INPUT1] [OPERATOR v] [INPUT2]**
  - Reporter: calculator for conditions
  - OPERATOR: inc (+), dec (-), mul (*), div (/)
  - Block ID: database_operator

---

## 5. CLOUD STORAGE (Category: Cloud)

### 5.1 Google Sheets Integration

- **read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]**
  - Reads data from Google Sheet into table
  - Specify sheet name and cell range
  - Block ID: cloud_read_google_sheet

- **write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]**
  - Writes table data to Google Sheet
  - Includes column headers (first row)
  - Block ID: cloud_write_google_sheet

- **list all sheets in google sheet at URL [SHEET_URL] into list [LIST]**
  - Gets names of all sheets
  - Block ID: cloud_list_sheets

- **add sheet [SHEETNAME] to google sheet at URL [URL]**
  - Adds new sheet
  - Block ID: cloud_add_sheet

- **remove sheet [SHEETNAME] from google sheet at URL [URL]**
  - Removes sheet
  - Block ID: cloud_remove_sheet

- **clear sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]**
  - Clears all content
  - Block ID: cloud_clear_sheet

- **append row [ROWNUMBER] from table [TABLENAME v] to sheet [SHEETNAME] in Google Sheet at URL [URL]**
  - Appends table row to bottom of sheet
  - Block ID: cloud_append_row

- **set value to [VALUE] at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]**
  - Sets single cell value
  - Block ID: cloud_set_cell

- **value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]**
  - Reporter: reads single cell value
  - Block ID: cloud_get_cell

- **insert [COUNT] rows at row [STARTR] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]**
  - Inserts rows below specified row
  - Block ID: cloud_insert_rows

- **insert [COUNT] columns at column [STARTC] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]**
  - Inserts columns to right of specified column
  - Block ID: cloud_insert_columns

- **remove rows [FROMR] to [TOR] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]**
  - Removes specified rows
  - Block ID: cloud_remove_rows

- **remove columns [FROMC] to [TOC] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]**
  - Removes specified columns
  - Block ID: cloud_remove_columns

### 5.2 Google Drive

- **list content of Google Drive folder [URL] in table [TABLENAME v]**
  - Lists files and subfolders
  - Columns: filename, fileid, mimetype, url
  - Block ID: cloud_list_drive_folder

### 5.3 Web Fetching

- **fetch web page as [FORMAT] from URL [URL]**
  - Fetches web page content
  - FORMAT: can be markdown
  - Block ID: cloud_fetch_web_page

---

## 6. LOGGING & DEBUGGING (Category: Control)

### 6.1 Console Logging

- **print [MESSAGE] in [WINDOW v] color [COLOR]**
  - WINDOW: 'console' (panel below editor) or 'alert' (modal window)
  - COLOR: only for console output
  - Useful for debugging execution steps and variable values
  - Block ID: control_debug (internally called control_log)

- **get console log**
  - Reporter: returns all output printed to console panel
  - Block ID: control_get_console_log

---

## 7. MULTIPLAYER DATA SHARING (Category: Multiplayer)

### 7.1 Game Management

- **create game named [GAMENAME] password [PASSWORD] my name [HOSTNAME] role [ROLE] server [LOCATION v] capacity (CAPACITY) world width (W) height (H)**
  - Creates multiplayer game on server
  - Players need PASSWORD to join
  - LOCATION: server location (e.g., US-East)
  - Block ID: mp_createmultiplayergame

- **list players in game [GAMENAME] hosted by [HOSTNAME] from server [LOCATION v] in table [TABLE v]**
  - Fetches player list into table
  - Columns: 'Player Name', 'Role'
  - Block ID: mp_listmultiplayergameusers

- **reset game world**
  - Resets multiplayer game world
  - Block ID: mp_resetmultiplayergame

### 7.2 Sprite Synchronization

- **synchronously set speed x (X) y (Y)**
  - Syncs sprite speed across all clients
  - Block ID: mp_setsyncmovement

- **synchronously set speed (SPEED) dir (DIR)**
  - Syncs sprite speed and direction
  - Direction in degrees
  - Block ID: mp_setsyncmovement2

### 7.3 Messaging

- **broadcast message to all** (specific syntax not fully captured)
  - Broadcasts to all players
  - Block ID: mp_broadcastmessagetoall

- **when touching [SPRITENAME v] will [STOPTYPE v] and trigger [MESSAGE v] with parameter [PARAMETER]**
  - Specifies collision behavior and message
  - STOPTYPE: 'stop', 'stop and delete', 'continue', 'continue and delete'
  - Block ID: mp_broadcasttouchmessage

---

## 8. AI-RELATED DATA OPERATIONS (Category: AI)

### 8.1 Semantic Database

- **create semantic database from table [TABLE v]**
  - Builds semantic database from table
  - Table must have 'key' column
  - Converts keys to embedding vectors
  - One database per project
  - Block ID: addtabletopinecone

- **search semantic database with [QUERY] store top (K) in table [t1 v] filter by column [FIELD] of value [VALUE]**
  - Searches using query (converted to embedding)
  - Returns top K results
  - Optional filter condition
  - Block ID: searchpinecone

- **search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE v]**
  - Advanced search with complex conditions
  - Block ID: searchpinecone2

### 8.2 Web Search

- **web search [QUERY] store top (K) in table [TABLE v]**
  - Runs web search
  - Stores top K results in table
  - Columns: title, link, snippet
  - Block ID: websearch

---

## SUMMARY OF BLOCK CATEGORIES

### Data Persistence Options:
1. **Local Files**: Export/import variables, lists, tables as txt/csv
2. **Server Storage**: Save/load data by key (public/private visibility)
3. **Database Collections**: Full CRUD operations with filtering/sorting
4. **Google Sheets**: Full read/write integration
5. **Google Drive**: List folder contents
6. **Multiplayer Server**: Game state synchronization

### Data Structures:
1. **Variables**: Single values with export/import
2. **Lists**: Dynamic arrays with 20+ specialized operations
3. **Tables**: 2D data with rows/columns, CSV import/export
4. **Database Collections**: Persistent structured data with queries

### Logging Methods:
1. **Console Panel**: print block with color coding
2. **Alert Windows**: Modal message display
3. **Console Log Retrieval**: Get all console output

### Data Analysis Capabilities:
- Statistical functions (min, max, sum, average, median)
- Sorting and filtering
- Text operations (split, join, regex)
- Aggregation and pivoting
- Random data generation (with seeds)

---

## RECOMMENDATIONS FOR T26 TOPIC

### Strong Coverage:
✅ List operations (20+ blocks)
✅ Table operations (20+ blocks)
✅ Data persistence (5 different methods)
✅ Console logging and debugging
✅ Cloud storage (Google Sheets/Drive)
✅ Database with full CRUD operations

### Topic Structure Suggestion:

1. **Basic Data Collection**
   - Variables and lists
   - Adding, modifying, deleting items
   - List iteration

2. **Local Storage**
   - Export/import to files
   - CSV handling

3. **Server Storage**
   - Save/load data with keys
   - Public vs private data

4. **Advanced Tables**
   - Creating and manipulating tables
   - Statistical analysis
   - Import/export

5. **Cloud Integration**
   - Google Sheets read/write
   - Google Drive access

6. **Database Operations**
   - Collections and queries
   - CRUD operations
   - Filtering and sorting

7. **Logging & Debugging**
   - Console output
   - Alert messages
   - Retrieving logs

8. **Multiplayer Data**
   - Shared game state
   - Player synchronization

---

## TECHNICAL NOTES

- All list indices are 1-based (first item is at index 1)
- Tables support up to 12 columns per operation in some blocks
- Regular expressions use ripgrep syntax (not grep)
- Console colors specified in hex format (e.g., #C08666FF)
- Server data is project-scoped (not cross-project accessible)
- Google Sheets require proper sharing permissions
- Database uses MongoDB-like query syntax

