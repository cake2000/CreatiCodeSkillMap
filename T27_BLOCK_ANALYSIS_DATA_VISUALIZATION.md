# T27 Data Analysis & Visualization Block Analysis

**Date**: 2025-11-21
**Source**: `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`
**Purpose**: Identify all data analysis and visualization blocks available in CreatiCode to ensure T27 skills accurately reflect platform capabilities

---

## EXECUTIVE SUMMARY

CreatiCode provides **comprehensive data analysis and visualization capabilities** organized across 4 main categories:

1. **Widgets Category** - Chart/Graph Visualization (3 specialized blocks)
2. **Variables Category** - Table/Data Structure Operations (30+ blocks)
3. **Database Category** - Cloud Database Operations (13 blocks)
4. **Cloud Category** - Google Sheets Integration (14 blocks)
5. **Operators Category** - Statistical/Data Processing (1 specialized block)

**Total Data/Visualization Blocks**: 60+

---

## 1. WIDGETS CATEGORY: CHART & VISUALIZATION BLOCKS

### Category Location: Widgets
All blocks in this category can be used for 2D visualization on stage.

#### 1.1 Line Chart Block
**Block ID**: `widget_drawchartusinglist`
**Syntax**: `draw [CHARTTYPE v] chart using list [LISTNAME v] x (X) y (Y) width (WIDTH) height (HEIGHT)`
**Example**: `draw [line v] chart using list [list1 v] x (0) y (0) width (100) height (100)`
**Description**:
- Draws a chart from a single list of data points
- Supports CHARTTYPE options: **'line'**, **'bar'**, **'pie'**, **'percentage'**
- X-axis labeled by data point index (starting at 1)
- Y-axis scaled to data range
- Positioned at (X, Y) with specified WIDTH x HEIGHT
- Used for simple single-series visualizations

**Operations Supported**:
- Single-series data visualization
- Basic line/bar/pie/percentage chart rendering
- Position and size customization

---

#### 1.2 Multi-Column Chart Block
**Block ID**: `widget_drawchartusingcolumn`
**Syntax**: `draw [CHARTTYPE v] chart using columns [COLUMNLIST] from table [TABLENAME v] x (X) y (Y) width (WIDTH) height (HEIGHT)`
**Example**: `draw [line v] chart using columns [age,height] from table [k v] x (0) y (0) width (100) height (100)`
**Description**:
- Draws a chart from multiple columns in a table
- Supports CHARTTYPE options: **'line'**, **'bar'**, **'pie'**, **'percentage'**
- COLUMNLIST: comma-separated column names
- Each column treated as a separate data series
- X-axis labeled by row number (starting at 1)
- Y-axis scaled to accommodate all data series
- Positioned at (X, Y) with specified dimensions

**Operations Supported**:
- Multi-series data visualization
- Table column selection and filtering
- Comparative analysis (multiple data series on one chart)
- Chart positioning and sizing

---

#### 1.3 Pie Chart with Categories Block
**Block ID**: `widget_drawchartusingcategory`
**Syntax**: `draw pie chart using category [CATEGORYCOLUMN] and value [VALUECOLUMN] from table [TABLENAME v] x (X) y (Y) width (WIDTH) height (HEIGHT)`
**Example**: `draw pie chart using category [grade] and value [height] from table [student table v] x (0) y (0) width (100) height (100)`
**Description**:
- Specialized pie chart with categorical labels
- CATEGORYCOLUMN: provides labels for each slice
- VALUECOLUMN: provides numeric values for slice sizes
- Automatically calculates percentages per row
- Used for compositional data visualization
- Positioned at (X, Y) with specified dimensions

**Operations Supported**:
- Categorical data visualization
- Percentage calculation from values
- Labeled pie slices
- Composition analysis

---

#### 1.4 Progress Bar Widget Block
**Block ID**: `widget_progressbar`
**Syntax**: `add progress bar as (CURRENT) out of total (TOTAL) at x (X) y (Y) width (WIDTH) height (HEIGHT) color [COLOR] background [BG] border width (BORDERWIDTH) color [BORDERCOLOR] as [NAME]`
**Example**: `add progress bar as (50) out of total (100) at x (0) y (0) width (200) height (20) color [#1777FFFF] background [#F0F0F0FF] border width (0) color [#F0F0F0FF] as [progressbar1]`
**Description**:
- Creates interactive progress visualization
- Calculates percentage: (CURRENT / TOTAL) * 100
- Customizable colors for progress (COLOR) and remainder (BG)
- Customizable border styling
- Named widget for reference and updates
- Useful for showing completion status or progress

**Operations Supported**:
- Progress tracking visualization
- Percentage-based display
- Custom styling and theming
- Widget naming and referencing

---

## 2. VARIABLES CATEGORY: TABLE & DATA STRUCTURE OPERATIONS

### Category Location: Variables

#### 2.1 Table Creation & Structure Operations

##### 2.1.1 Add Row Block
**Block ID**: `data_addrowtotable`
**Syntax**: `add to table [TABLENAME v]: [CELL1] [CELL2] ... [CELL12]`
**Example**: `add to table [table1 v]: [a] [b] [] [] [] [] [] [] [] [] [] []`
**Description**:
- Appends a new row at the bottom of a table
- Accepts up to 12 cell values
- Empty inputs are ignored
- Dynamic row insertion

---

##### 2.1.2 Insert Row at Position Block
**Block ID**: `data_insertrowtotable`
**Syntax**: `insert at row (ROWNUM) of table [TABLENAME v]: [CELL1] [CELL2] ... [CELL12]`
**Example**: `insert at row (1) of table [table1 v]: [c] [d] [] [] [] [] [] [] [] [] [] []`
**Description**:
- Inserts a row at specific position (row index 1 = first row)
- Shifts existing rows down
- Accepts up to 12 cell values

---

##### 2.1.3 Replace Row Block
**Block ID**: `data_replacerowoftable`
**Syntax**: `replace row (ROWNUM) of table [TABLENAME v] with: [CELL1] [CELL2] ... [CELL12]`
**Example**: `replace row (1) of table [table1 v] with: [2] [sophia] [] [] [] [] [] [] [] [] [] []`
**Description**:
- Replaces entire row content at specified index
- Updates all cells in that row

---

##### 2.1.4 Delete Row Block
**Block ID**: `data_deleterowoftable`
**Syntax**: `delete row (ROWNUM) of table [TABLENAME v]`
**Example**: `delete row (1) of table [table1 v]`
**Description**:
- Deletes row at specified index
- Shifts remaining rows up

---

##### 2.1.5 Delete All Rows Block
**Block ID**: `data_deleteallrowsoftable`
**Syntax**: `delete all rows from table [TABLENAME v]`
**Example**: `delete all rows from table [table1 v]`
**Description**:
- Clears all rows but keeps columns
- Useful for resetting data while maintaining structure

---

##### 2.1.6 Delete Column Block
**Block ID**: `data_deletecolumnfromtable`
**Syntax**: `delete column [COLUMNNAME] from table [TABLENAME v]`
**Example**: `delete column [age] from table [table1 v]`
**Description**:
- Removes a column by name
- All data in that column is deleted

---

##### 2.1.7 Delete All Columns Block
**Block ID**: `data_removeallcolumnsfromtable`
**Syntax**: `delete all columns from table [TABLENAME v]`
**Example**: `delete all columns from table [table1 v]`
**Description**:
- Completely clears table structure and data
- Leaves empty table

---

##### 2.1.8 Add Column Block
**Block ID**: `data_addcolatposition`
**Syntax**: `add column [COLUMNNAME] at position (POSITION) to table [TABLENAME v]`
**Example**: `add column [age] at position (1) to table [table1 v]`
**Description**:
- Adds new column at specific position
- Column position 1 = first column
- Used to structure table schema

---

#### 2.2 Table Cell Operations (CRUD)

##### 2.2.1 Get Cell Value Block
**Block ID**: `data_itematrowcolumnoftable`
**Syntax**: `item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v]`
**Example**: `item at row (1) column [age] of table [table1 v]`
**Description**:
- Reporter block that retrieves a single cell value
- Row index starts at 1

---

##### 2.2.2 Replace Cell Value Block
**Block ID**: `data_replaceitematrowcolumn`
**Syntax**: `replace item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] with [VALUE]`
**Example**: `replace item at row (1) column [age] of table [table1 v] with [13]`
**Description**:
- Updates a single cell value

---

##### 2.2.3 Change Cell Value (Add) Block
**Block ID**: `data_changeitematrowcolumn`
**Syntax**: `change item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)`
**Example**: `change item at row (1) column [age] of table [table1 v] by (1)`
**Description**:
- Increments/decrements a numeric cell value
- Used for data updates and calculations

---

##### 2.2.4 Reduce Cell Value (Subtract) Block
**Block ID**: `data_reduceitematrowcolumn`
**Syntax**: `reduce item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)`
**Example**: `reduce item at row (1) column [age] of table [table1 v] by (1)`
**Description**:
- Decrements a numeric cell value
- Subtraction-specific operation

---

#### 2.3 Table Query & Search Operations

##### 2.3.1 Get Row Index by Value Block
**Block ID**: `data_rowindexwithcondition`
**Syntax**: `row # of [VALUE] in column [COLUMN] in table [TABLENAME v]`
**Example**: `row # of [john] in column [name] in table [table1 v]`
**Description**:
- Finds row index containing specific value
- Returns -1 if not found
- Exact match search

---

##### 2.3.2 Get Row Index by Substring Block
**Block ID**: `data_rowindexwithcondition2`
**Syntax**: `row # of item containing [SUBSTRING] in column [COLUMN] in table [TABLENAME v]`
**Example**: `row # of item containing [zh] in column [name] in table [table1 v]`
**Description**:
- Finds first row where column contains substring
- Returns -1 if not found
- Partial match search

---

##### 2.3.3 Get Full Row Data Block
**Block ID**: `data_rowatindexoftable`
**Syntax**: `row (ROWINDEX) of table [TABLENAME v] separator [SEPARATOR]`
**Example**: `row (1) of table [table1 v] separator [,]`
**Description**:
- Returns entire row as delimited string
- Convenient for reading all cells in a row

---

##### 2.3.4 Lookup/VLOOKUP Block
**Block ID**: `data_lookuptable`
**Syntax**: `item in column [RETURNCOLUMN] of [TABLENAME v] where column [SEARCHCOLUMN] equals [SEARCHTEXT]`
**Example**: `item in column [age] of [table1 v] where column [name] equals [John]`
**Description**:
- Performs lookup/VLOOKUP-like operation
- Returns value from RETURNCOLUMN where SEARCHCOLUMN matches SEARCHTEXT
- Single match lookup

---

##### 2.3.5 Row Count Block
**Block ID**: `data_rowcountoftable`
**Syntax**: `row count of table [TABLENAME v]`
**Example**: `row count of table [table1 v]`
**Description**:
- Reporter block returning total rows in table
- Useful for looping and validation

---

#### 2.4 Table Data Analysis & Aggregation Operations

##### 2.4.1 Compute Aggregation Block
**Block ID**: `data_computetable`
**Syntax**: `[METHOD] of column [COLUMNNAME] in table [TABLE v]`
**Example**: `[smallest v] of column [age] in table [table1 v]`
**Description**:
- Aggregates single column data
- Supported METHODS: **'smallest'**, **'largest'**, **'sum'**, **'average'**, **'median'**
- Returns single value
- Statistical analysis on column data

---

##### 2.4.2 Set Table by Aggregation Block
**Block ID**: `data_settabletocomputed`
**Syntax**: `set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2]`
**Example**: `set table [table1 v] to [smallest v] of column [age] in table [table2 v] by column [grade]`
**Description**:
- Groups data by COLUMN2, aggregates COLUMN1 using METHOD
- Supported METHODS: **'minimum'**, **'maximum'**, **'sum'**, **'average'**, **'median'**
- Creates summary table
- GROUP BY functionality

**Example Program**:
```
when green flag clicked
    delete all columns from table [t1 v]
    add column [name] at position (1) to table [t1 v]
    add column [gender] at position (2) to table [t1 v]
    add column [score] at position (3) to table [t1 v]
    add to table [t1 v]: [Joe] [M] [92] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Mike] [M] [96] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Sophia] [F] [100] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Jenny] [F] [98] [] [] [] [] [] [] [] [] []
    set table [summary v] to [largest v] of column [score] in table [t1 v] by column [gender]
end
```

---

##### 2.4.3 Pivot Table Block
**Block ID**: `data_pivot_table_into_table`
**Syntax**: `pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST]`
**Example**: `pivot [table1 v] into [table2 v] row groups [gender,grade] columns [age,height] methods [average,maximum]`
**Description**:
- Creates pivot/crosstab tables
- ROWGROUPLIST: comma-separated grouping columns
- VALUECOLUMNLIST: comma-separated value columns to aggregate
- METHODLIST: comma-separated aggregation methods (one per value column)
- Supported METHODS: **'sum'**, **'maximum'**, **'minimum'**, **'average'**
- Advanced data summarization

**Example Program**:
```
when green flag clicked
    delete all columns from table [t1 v]
    add column [name] at position (1) to table [t1 v]
    add column [gender] at position (2) to table [t1 v]
    add column [score] at position (3) to table [t1 v]
    add to table [t1 v]: [Joe] [M] [92] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Mike] [M] [96] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Sophia] [F] [100] [] [] [] [] [] [] [] [] []
    add to table [t1 v]: [Jenny] [F] [98] [] [] [] [] [] [] [] [] []
    pivot [t1 v] into [summary v] row groups [gender] columns [score] methods [average]
end
```

---

#### 2.5 Table Sorting & Shuffling

##### 2.5.1 Sort Table Block
**Block ID**: `data_sorttablebycolumn`
**Syntax**: `sort table [TABLENAME v] by column [COLUMN] [SORTORDER v]`
**Example**: `sort table [table1 v] by column [age] [SORTORDER v]`
**Description**:
- Sorts entire table by specified column
- SORTORDER options: **'large to small'** (descending) or **'small to large'** (ascending)
- In-place sorting
- Useful for data organization and analysis

---

##### 2.5.2 Reshuffle Table Block
**Block ID**: `data_reshuffletable`
**Syntax**: `reshuffle table [TABLENAME v] randomly`
**Example**: `reshuffle table [table1 v] randomly`
**Description**:
- Randomly shuffles table rows
- Used for randomization in data processing

---

#### 2.6 Table Combination Operations

##### 2.6.1 Copy Table Block
**Block ID**: `data_copy_table_into_table`
**Syntax**: `copy table [TABLE1] into [TABLE2]`
**Example**: `copy table [table1 v] into [table2 v]`
**Description**:
- Copies all rows from TABLE1 to TABLE2
- Replaces existing data in TABLE2
- Creates identical tables

---

##### 2.6.2 Append Table Block
**Block ID**: `data_append_table_into_table`
**Syntax**: `append table [TABLE1] to [TABLE2]`
**Example**: `append table [table1 v] to [table2 v]`
**Description**:
- Appends rows from TABLE1 to bottom of TABLE2
- Tables must have same columns
- Concatenates data
- Used for data consolidation

---

#### 2.7 Table Display Operations

##### 2.7.1 Show Table Block
**Block ID**: `data_showtable`
**Syntax**: `show table [TABLENAME v]`
**Example**: `show table [table1 v]`
**Description**:
- Displays table on stage
- Makes table visible to user
- For visualization and debugging

---

##### 2.7.2 Hide Table Block
**Block ID**: `data_hidetable`
**Syntax**: `hide table [TABLENAME v]`
**Example**: `hide table [table1 v]`
**Description**:
- Hides table from stage
- Keeps data in memory

---

##### 2.7.3 Show Table Snapshot Block
**Block ID**: `data_showsnapshotoftable`
**Syntax**: `show snapshot of table [TABLENAME v] from row (STARTROW) to (ENDROW) with style [STYLE] [THEMECOLOR]`
**Example**: `show snapshot of table [table1 v] from row (1) to (10) with style [style1 v] [#1E54B6FF]`
**Description**:
- Shows table in popup window
- Displays row range: STARTROW to ENDROW
- STYLE options: **'style1'**, **'style2'**, **'style3'**, **'style4'**
- Customizable theme color
- For report generation and data inspection

---

#### 2.8 Table Import/Export Operations

##### 2.8.1 Export Table to CSV Block
**Block ID**: `data_exporttable`
**Syntax**: `export table [TABLENAME v] as [FILENAME]`
**Example**: `export table [table1 v] as [datatable]`
**Description**:
- Exports table as CSV file
- If FILENAME empty, uses table name
- Automatic '.csv' extension
- For data sharing and external analysis

---

##### 2.8.2 Import Table from File Block
**Block ID**: `data_importtable`
**Syntax**: `import file into table [TABLE]`
**Example**: `import file into table [TABLE]`
**Description**:
- Opens file selection dialog
- Accepts txt or csv files
- Parses into rows and columns
- Populates specified table
- For data ingestion

---

##### 2.8.3 Save Table to Server Block
**Block ID**: `data_savetable`
**Syntax**: `save table [TABLE v] to server as [DATANAME]`
**Example**: `save table [tt v] to server as [info]`
**Description**:
- Saves table to CreatiCode cloud server
- Named data storage

---

##### 2.8.4 Load Table from Server Block
**Block ID**: `data_loadtable`
**Syntax**: `load [DATANAME] from server into table [TABLE v]`
**Example**: `load [info] from server into table [tt v]`
**Description**:
- Loads previously saved table from server
- Restores complete table data
- For data persistence

---

#### 2.9 Table List Integration

##### 2.9.1 Copy List to Column Block
**Block ID**: `data_setlisttocolumn`
**Syntax**: `copy list [LISTNAME v] to column [COLUMNNAME] of table [TABLENAME v]`
**Example**: `copy list [i v] to column [age] of table [table1 v]`
**Description**:
- Copies list data into table column
- Column must already exist
- Replaces existing column data
- Useful for data transformation

---

#### 2.10 Table Deletion with Conditions

##### 2.10.1 Delete Rows by Condition Block
**Block ID**: `data_deleterowwithcondition`
**Syntax**: `delete rows with column [COLUMN] of value [VALUE] from table [TABLENAME v]`
**Example**: `delete rows with column [x] of value [1] from table [table1 v]`
**Description**:
- Deletes all rows where COLUMN equals VALUE
- Conditional row removal
- Used for data filtering/cleaning

---

## 3. DATABASE CATEGORY: CLOUD DATABASE OPERATIONS

### Category Location: Database
All blocks integrate with CreatiCode cloud database backend.

#### 3.1 Database Collection Query Blocks

##### 3.1.1 Fetch from Collection Block
**Block ID**: `database_find_from_collection`
**Syntax**: `fetch from collection [COLLECTIONNAME v] into table [TABLENAME v] where <CONDITION> limit (LIMIT) sort by (SORTFIELD1) [SORTORDER1 v] (SORTFIELD2) [SORTORDER2 v]`
**Example**: `fetch from collection [students v] into table [students_table v] where <cond (field [ID]) [gt v] [80]> limit (100) sort by (field [Name]) [1 v] (field [Age]) [-1 v]`
**Description**:
- Fetches data from cloud collection into local table
- CONDITION: WHERE clause for filtering
- LIMIT: maximum rows to fetch
- SORTFIELD1/SORTFIELD2: optional multi-field sorting
- SORTORDER1/SORTORDER2: 1 (ascending) or -1 (descending)
- Supports complex query conditions

---

##### 3.1.2 Collection Reporter Block
**Block ID**: `database_collection`
**Syntax**: `collection [COLLECTIONNAME]`
**Example**: `collection [ccc]`
**Description**:
- Reporter block returning collection schema
- Returns JSON array with field names and types
- Example: `[{"field":"name","type":"string"},{"field":"age","type":"number"}]`
- For schema inspection

---

#### 3.2 Database Insert Operations

##### 3.2.1 Insert from Table Block
**Block ID**: `database_insert_from_table`
**Syntax**: `insert from table [TABLENAME v] row from (STARTROW) to (ENDROW) into collection [COLLECTIONNAME v]`
**Example**: `insert from table [students_table v] row from (1) to (100) into collection [students v]`
**Description**:
- Inserts table rows into cloud collection
- Two-step process: prepare data in table first
- Uses table as intermediate storage
- Allows data review before database insert
- Row range from STARTROW to ENDROW

---

#### 3.3 Database Update Operations

##### 3.3.1 Update Collection from Table Block
**Block ID**: `database_update_collection`
**Syntax**: `update collection [COLLECTIONNAME v] from table [TABLENAME v]`
**Example**: `update collection [students v] from table [students_table v]`
**Description**:
- Updates existing database rows from modified table data
- Requires rows previously fetched from collection
- Maintains hidden 'id' property linking to database
- Workflow: fetch → modify → update
- Preserves database record identity

---

##### 3.3.2 Update Collection In-Place Block
**Block ID**: `database_update_collection_in_place`
**Syntax**: `update collection [COLLECTIONNAME v] in-place where <CONDITION> set (FIELD1) to (VALUE1) set (FIELD2) to (VALUE2) set (FIELD3) to (VALUE3) set (FIELD4) to (VALUE4)`
**Example**: `update collection [students v] in-place where <cond (field [ID]) [eq v] [1]> set (field [Name]) to (abc) set (field [Age]) to (22) set () to () set () to ()`
**Description**:
- Direct in-place update without fetching to table
- CONDITION: WHERE clause
- Can update up to 4 fields simultaneously
- FIELD/VALUE pairs for each update
- Efficient for targeted updates

---

#### 3.4 Database Delete Operations

##### 3.4.1 Remove Documents Block
**Block ID**: `database_remove_all_document`
**Syntax**: `remove all documents from collection [COLLECTIONNAME v] where <CONDITION>`
**Example**: `remove all documents from collection [students v] where <>`
**Description**:
- Deletes rows matching CONDITION
- Empty CONDITION deletes all rows (truncates collection)
- Conditional deletion support

---

#### 3.5 Database Query Condition Blocks

##### 3.5.1 Comparison Query Block
**Block ID**: `database_query`
**Syntax**: `<cond [INPUT1] [COMPARATOR v] [INPUT2]>`
**Example**: `<cond (field [a]) [lt v] [30]>`
**Description**:
- Boolean condition for database queries
- COMPARATOR options: **'>'**, **'<'**, **'='**, **'≠'**, **'≥'**, **'≤'**
- Each INPUT can be field or literal value
- Used in WHERE clauses

---

##### 3.5.2 Operator Query Block
**Block ID**: `database_operator`
**Syntax**: `op [INPUT1] [OPERATOR v] [INPUT2]`
**Example**: `op (field [a]) [inc v] [20]`
**Description**:
- Calculator for query conditions
- OPERATOR options: **'inc'** (+), **'dec'** (-), **'mul'** (*), **'div'** (/)
- Each INPUT can be field or literal value
- Used within database conditions

---

##### 3.5.3 Field Reference Block
**Block ID**: `database_collectionfield`
**Syntax**: `field [FIELDNAME]`
**Example**: `field [ID]`
**Description**:
- Reporter block specifying collection field
- Used within condition blocks
- Allows field references in WHERE clauses

---

##### 3.5.4 Contains Condition Block
**Block ID**: `database_contains`
**Syntax**: `<cond (field [FIELDNAME]) contains [TEXT]?>`
**Example**: `<cond (field [Name]) contains [a]?>`
**Description**:
- Text containment check
- Used for partial string matching in conditions
- Boolean result for WHERE filtering

---

##### 3.5.5 Logical NOT Block
**Block ID**: `database_not`
**Syntax**: `<cond not <>>`
**Example**: `<cond not <>>`
**Description**:
- Boolean negation
- Inverts condition result
- Used for NOT logic in WHERE clauses

---

##### 3.5.6 Logical AND Block
**Block ID**: `database_and`
**Syntax**: `<cond <> and <>>`
**Example**: `<cond <> and <>>`
**Description**:
- Boolean AND operation
- Combines two conditions
- Used for multiple criteria in WHERE clauses

---

##### 3.5.7 Logical OR Block
**Block ID**: `database_or`
**Syntax**: `<cond <> or <>>`
**Example**: `<cond <> or <>>`
**Description**:
- Boolean OR operation
- Combines two conditions
- Used for alternative criteria in WHERE clauses

---

## 4. CLOUD CATEGORY: GOOGLE SHEETS INTEGRATION

### Category Location: Cloud

#### 4.1 Google Sheets Read Operations

##### 4.1.1 Read from Google Sheet Block
**Block ID**: `p2p_readfromgooglesheet`
**Syntax**: `read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]`
**Example**: `read from google sheet: url [https://docs.google.com/spreadsheets/d/...] sheet name [Sheet1] range [B2:G11] into table [tt v]`
**Description**:
- Reads data from Google Sheet into table
- Supports cell range specification
- Multiple sheet support
- Data import from external sources

---

#### 4.1.2 List Sheets Block
**Block ID**: `p2p_listSheetsInGoogleSheet`
**Syntax**: `list all sheets in google sheet at URL [SHEET_URL] into list [LIST]`
**Example**: `list all sheets in google sheet at URL [https://xxx] into list [list1 v]`
**Description**:
- Gets all sheet names from Google Sheet
- Stores names in list
- Useful for dynamic sheet access

---

#### 4.2 Google Sheets Write Operations

##### 4.2.1 Write to Google Sheet Block
**Block ID**: `p2p_writeintogooglesheet`
**Syntax**: `write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]`
**Example**: `write into google sheet: url [https://docs.google.com/spreadsheets/d/...] sheet name [Sheet2] starting cell [B2] from table [tt v]`
**Description**:
- Writes table data to Google Sheet
- Includes column headers
- Starts at specified cell address
- Two-way sync capability

---

#### 4.3 Google Sheets Structural Operations

##### 4.3.1 Add Sheet Block
**Block ID**: `p2p_addsheet`
**Syntax**: `add sheet [SHEETNAME] to google sheet at URL [URL]`
**Example**: `add sheet [summary] to google sheet at URL [https://docs.google.com/spreadsheets/d/aaaa/edit?usp=sharing]`
**Description**:
- Adds new sheet to Google Sheet
- Named sheet creation

---

##### 4.3.2 Remove Sheet Block
**Block ID**: `p2p_removesheet`
**Syntax**: `remove sheet [SHEETNAME] from google sheet at URL [URL]`
**Description**:
- Deletes sheet from Google Sheet

---

##### 4.3.3 Clear Sheet Block
**Block ID**: `p2p_clearsheet`
**Syntax**: `clear sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
**Example**: `clear sheet [sheet1] in Google Sheet at URL [example.com]`
**Description**:
- Clears all content from sheet
- Preserves sheet structure

---

#### 4.4 Google Sheets Row/Column Operations

##### 4.4.1 Insert Rows Block
**Block ID**: `p2p_insertrowsinsheet`
**Syntax**: `insert [COUNT] rows at row [STARTR] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
**Example**: `insert [2] rows at row [5] in sheet [sheet1] in Google Sheet at URL [example.com]`
**Description**:
- Inserts specified number of rows
- At specified row position

---

##### 4.4.2 Remove Rows Block
**Block ID**: `p2p_removerowsfromsheet`
**Syntax**: `remove rows [FROMR] to [TOR] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
**Example**: `remove rows [10] to [15] from sheet [sheet1] in Google Sheet at URL [example.com]`
**Description**:
- Deletes range of rows
- Row range specification

---

##### 4.4.3 Insert Columns Block
**Block ID**: `p2p_insertcolumnsinsheet`
**Syntax**: `insert [COUNT] columns at column [STARTC] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
**Example**: `insert [2] columns at column [B] in sheet [sheet1] in Google Sheet at URL [example.com]`
**Description**:
- Inserts specified number of columns
- At specified column position
- Shifts existing columns right

---

##### 4.4.4 Remove Columns Block
**Block ID**: `p2p_removecolumnsfromsheet`
**Syntax**: `remove columns [FROMC] to [TOC] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
**Example**: `remove columns [H] to [Z] from sheet [sheet1] in Google Sheet at URL [example.com]`
**Description**:
- Deletes range of columns
- Column range specification

---

## 5. OPERATORS CATEGORY: STATISTICAL ANALYSIS

### Category Location: Operators

#### 5.1 Moving Average Block
**Block ID**: `operator_value_from_moving_average`
**Syntax**: `value from [METHOD v] moving average window [LENGTH] of list [LISTNAME v]`
**Example**: `value from [simple v] moving average window [30] of list [i v]`
**Description**:
- Calculates moving average over list data
- METHOD options: **'simple'**, **'exponential'**
- Returns comma-separated moving average values
- Window-based calculation
- Example: list [1,2,3,4,5,6] with window 3 → "2,3,4,5"
- Used for trend analysis and data smoothing

---

## SUMMARY TABLE: DATA ANALYSIS CAPABILITIES

| Category | Block Count | Primary Functions |
|----------|-------------|-------------------|
| **Widgets** | 4 | Chart rendering, progress visualization |
| **Variables (Table Operations)** | 30+ | CRUD, aggregation, pivot, import/export |
| **Database** | 13 | Cloud collection queries, CRUD with conditions |
| **Cloud (Google Sheets)** | 14 | Google Sheets read/write, sheet management |
| **Operators** | 1 | Statistical moving average |
| **TOTAL** | **60+** | Complete data analysis ecosystem |

---

## OPERATIONS SUPPORTED ACROSS ALL BLOCKS

### Data Retrieval Operations
✓ Single cell/value retrieval
✓ Row retrieval
✓ Multi-row fetching with conditions
✓ Table schema inspection
✓ Google Sheets integration

### Data Filtering Operations
✓ Column-based filtering
✓ Value-based row deletion
✓ Query conditions (>, <, =, ≠, ≥, ≤)
✓ Text containment filtering
✓ Substring matching
✓ Logical operators (AND, OR, NOT)

### Data Sorting Operations
✓ Sort by single column (ascending/descending)
✓ Multi-field sorting (database)
✓ Random shuffling

### Data Aggregation & Statistics
✓ Sum, Average, Median, Min, Max
✓ GROUP BY aggregation
✓ Pivot tables
✓ Moving average (simple & exponential)
✓ Count operations

### Data Transformation Operations
✓ Copy/Append tables
✓ List to column conversion
✓ Row/Column insertion/deletion
✓ Cell value updates (replace, increment, decrement)

### Data Visualization Operations
✓ Line charts
✓ Bar charts
✓ Pie charts (both simple and categorical)
✓ Percentage charts
✓ Progress bars
✓ Table display (inline and snapshot)

### Data Import/Export Operations
✓ CSV export
✓ CSV/TXT import
✓ Google Sheets import/export
✓ Cloud server persistence
✓ Multiple sheet handling

### Database Operations
✓ Create/fetch/update/delete documents
✓ WHERE clause support
✓ Multi-field conditions
✓ In-place updates
✓ Collection schema inspection

---

## RECOMMENDATIONS FOR T27 SKILLS

Based on this comprehensive analysis, T27 should include skills for:

1. **Table Operations Fundamentals**
   - Creating, adding, deleting rows/columns
   - Basic CRUD operations on cells
   - Table display and export

2. **Data Analysis Core Skills**
   - Sorting and filtering tables
   - Computing aggregations (sum, average, min, max, median)
   - Pivot table creation
   - GROUP BY operations

3. **Data Visualization Skills**
   - Creating line, bar, pie charts from lists
   - Multi-series visualization from table columns
   - Categorical pie charts
   - Progress bar creation

4. **Advanced Data Operations**
   - Lookup/VLOOKUP functionality
   - Conditional row deletion
   - Row insertion at specific positions
   - Multi-table operations (copy, append)

5. **Cloud Integration**
   - Google Sheets read/write operations
   - Cloud database collection queries
   - Condition-based filtering in database
   - Cloud persistence (save/load tables)

6. **Statistical Analysis**
   - Moving averages
   - Trend analysis
   - Group-based statistics

7. **Data Import/Export**
   - CSV import/export
   - Google Sheets integration
   - File handling for data ingestion

---

## BLOCK LOCATION REFERENCE

| Category | File Path | Line Range |
|----------|-----------|-----------|
| Widgets (Charts) | blockdes8.txt | 9461-9515 |
| Variables (Tables) | blockdes8.txt | 9771-10256+ |
| Database | blockdes8.txt | 3839-4009 |
| Cloud (Google Sheets) | blockdes8.txt | 10269+ |
| Operators (Moving Avg) | blockdes8.txt | 2310-2323 |

---

**Report Generated**: 2025-11-21
**Analysis Type**: Complete Block Inventory with Capability Assessment
