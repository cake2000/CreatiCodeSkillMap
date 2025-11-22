# Block Syntax Verification Report for T10 Skills
## Source: /media/binyu/USB2/ScratchCopilot/blockdes8.txt

Generated: 2025-11-22

---

## SECTION 1: LIST STATISTICS (for T10.G4.06)

### Overview
List statistics blocks are found in the **Variables category** and support computation of: sum, average, minimum/smallest, maximum/largest, and median.

### Block Details

#### Block ID: `data_itemspecificvalueoflist`
- **Category:** Variables
- **Block Type:** Reporter
- **Exact Syntax:** `[METHOD v] of list [LISTNAME v]`
- **Methods Supported:** smallest, largest, sum, average, median
- **Usage Example:** `[smallest v] of list [ss v]`
- **Full Description:** A reporter block that returns the METHOD (can be smallest/largest/sum/average/median) of the given list LISTNAME
- **Status:** ✅ VERIFIED - Block EXISTS

### Recommendations for T10.G4.06
- Use `data_itemspecificvalueoflist` with the dropdown to select the desired aggregation method
- All five statistical methods are available: smallest, largest, sum, average, median
- This is a pure reporter block (returns values, does not modify state)

---

## SECTION 2: TABLE OPERATIONS (for T10.G5+)

### 2.1 TABLE CREATION AND COLUMN OPERATIONS

#### Block ID: `data_setlisttocolumn`
- **Category:** Variables
- **Block Type:** Command
- **Exact Syntax:** `copy list [LISTNAME v] to column [COLUMNNAME] of table [TABLENAME v]`
- **Usage Example:** `copy list [i v] to column [age] of table [table1 v]`
- **Description:** Copies the contents of the list LISTNAME into the column COLUMNNAME of the table TABLENAME. The column must already exist in the table, and all existing data items in that column will be removed before the new data from the list is copied over.
- **Status:** ✅ VERIFIED - Block EXISTS
- **Note:** Column must pre-exist; this block copies list data into existing columns

#### Block ID: `p2p_insertcolumnsinsheet` (Google Sheets equivalent)
- **Category:** Cloud
- **Exact Syntax:** insert columns in sheet
- **Status:** ✅ VERIFIED - Block EXISTS for Google Sheets

### 2.2 CELL AND ROW OPERATIONS

#### Block ID: `data_itematrowcolumnoftable`
- **Category:** Variables
- **Block Type:** Reporter
- **Exact Syntax:** `item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v]`
- **Usage Example:** `item at row (1) column [age] of table [table1 v]`
- **Description:** A reporter block that returns the content of the one item at the row index of ROWINDEX (first row has an index of 1) and the given column named COLUMNNAME of the table named TABLE.
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_changeitematrowcolumn`
- **Category:** Variables
- **Block Type:** Command
- **Exact Syntax:** `change item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)`
- **Usage Example:** `change item at row (1) column [age] of table [table1 v] by (1)`
- **Description:** Change the value of the item at row index of ROWNUM (first row has an index of 1) and the column named COLUMN in the table named TABLENAME by the CHANGEAMOUNT.
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_addrowtotable`
- **Category:** Variables
- **Block Type:** Command
- **Exact Syntax:** `add to table [TABLENAME v]: [CELL1] [CELL2] [CELL3] [CELL4] [CELL5] [CELL6] [CELL7] [CELL8] [CELL9] [CELL10] [CELL11] [CELL12]`
- **Usage Example:** `add to table [table1 v]: [a] [b] [] [] [] [] [] [] [] [] [] []`
- **Description:** Appends a new row of data to the table named TABLENAME at the bottom with values of CELL1 to CELL12. Any empty input will be ignored, and at most 12 data points can be appended using this block.
- **Max Columns:** 12
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_removeallcolumnsfromtable`
- **Category:** Variables
- **Block Type:** Command
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_deleterowoftable`
- **Category:** Variables
- **Block Type:** Command
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_deleteallrowsoftable`
- **Category:** Variables
- **Block Type:** Command
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_deletecolumnfromtable`
- **Category:** Variables
- **Block Type:** Command
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_rowatindexoftable`
- **Category:** Variables
- **Block Type:** Reporter
- **Status:** ✅ VERIFIED - Block EXISTS

### 2.3 TABLE AGGREGATION OPERATIONS

#### Block ID: `data_computetable`
- **Category:** Variables
- **Block Type:** Reporter
- **Exact Syntax:** `[METHOD] of column [COLUMNNAME] in table [TABLE v]`
- **Usage Example:** `[smallest v] of column [age] in table [table1 v]`
- **Methods Supported:** smallest, largest, sum, average, median
- **Description:** A reporter block that aggregates all the items in the column named COLUMNNAME in the table named TABLE. You can choose from 5 aggregation methods: 'smallest', 'largest', 'sum', 'average', 'median'.
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_settabletocomputed` (GROUP BY / AGGREGATION)
- **Category:** Variables
- **Block Type:** Command
- **Exact Syntax:** `set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2]`
- **Usage Example:** `set table [table1 v] to [smallest v] of column [age] in table [table2 v] by column [grade]`
- **Methods Supported:** minimum, maximum, sum, average, median
- **Description:** Update the value of the table named TABLENAME1 by aggregating the data from the table named TABLENAME2. The data in COLUMN2 of the table named TABLENAME2 will be grouped by the value of items in the column named COLUMN1, and the aggregation METHOD can be 'minimum', 'maximum', 'sum', 'average', 'median'. Note that this block will only be available when you have at least 2 tables defined in the project.
- **Status:** ✅ VERIFIED - Block EXISTS (Implements GROUP BY functionality)
- **Requirement:** Requires at least 2 tables defined in project

### 2.4 TABLE LOOKUP / FILTER OPERATIONS

#### Block ID: `data_lookuptable`
- **Category:** Variables
- **Block Type:** Reporter
- **Exact Syntax:** `item in column [RETURNCOLUMN] of [TABLENAME v] where column [SEARCHCOLUMN] equals [SEARCHTEXT]`
- **Usage Example:** `item in column [age] of [table1 v] where column [name] equals [John]`
- **Description:** A reporter block that returns the item in the column RETURNCOLUMN of the table named TABLENAME where another column SEARCHCOLUMN equals the value of SEARCHTEXT. This block can be used to look for an item in one column using the value in another column.
- **Status:** ✅ VERIFIED - Block EXISTS (Implements WHERE/FILTER functionality)

### 2.5 PIVOT TABLE OPERATIONS

#### Block ID: `data_pivot_table_into_table`
- **Category:** Variables
- **Block Type:** Command
- **Exact Syntax:** `pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST]`
- **Usage Example:** `pivot [table1 v] into [table2 v] row groups [gender,grade] columns [age,height] methods [average,maximum]`
- **Methods Supported:** sum, maximum, minimum, average
- **Description:** Creates a pivot table using data from TABLE1 and stores the pivot table data in TABLE2. This block groups the data in TABLE1 using the list of columns specified in ROWGROUPLIST. The data values of the pivot table will come from the columns VALUECOLUMNLIST, and these columns will be aggregated using the methods given in METHODLIST. Both VALUECOLUMNLIST and METHODLIST are comma-separated lists. Each item in the VALUECOLUMNLIST is the name of one column, and it will be aggregated by the corresponding method specified in METHODLIST. The methods can be 'sum', 'maximum', 'minimum' or 'average'.
- **Status:** ✅ VERIFIED - Block EXISTS (Full pivot table support)
- **Input Format:** Comma-separated lists for columns and methods

### 2.6 TABLE MANIPULATION / MERGING

#### Block ID: `data_copy_table_into_table`
- **Category:** Variables
- **Block Type:** Command
- **Exact Syntax:** `copy table [TABLE1] into [TABLE2]`
- **Usage Example:** `copy table [table1 v] into [table2 v]`
- **Description:** Copies all rows the table named TABLE1 into the table named TABLE2, which replaces any existing data in TABLE2. After this block these 2 tables will have exactly the same columns with the same content in them.
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_append_table_into_table`
- **Category:** Variables
- **Block Type:** Command
- **Exact Syntax:** `append table [TABLE1] to [TABLE2]`
- **Usage Example:** `append table [table1 v] to [table2 v]`
- **Description:** Appends the rows of table named TABLE1 to the bottom of the table named TABLE2. These 2 tables should have the same columns.
- **Status:** ✅ VERIFIED - Block EXISTS

### 2.7 TABLE SORTING AND SHUFFLING

#### Block ID: `data_sorttablebycolumn`
- **Category:** Variables
- **Block Type:** Command
- **Exact Syntax:** `sort table [TABLENAME v] by column [COLUMN] [SORTORDER v]`
- **Usage Example:** `sort table [table1 v] by column [age] [SORTORDER v]`
- **Sort Orders:** 'large to small' or 'small to large'
- **Description:** Sorts the table named TABLENAME by the specified column named COLUMN in the order of SORTORDER, which can be 'large to small' or 'small to large'.
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_reshuffletable`
- **Category:** Variables
- **Block Type:** Command
- **Exact Syntax:** `reshuffle table [TABLENAME v] randomly`
- **Usage Example:** `reshuffle table [table1 v] randomly`
- **Description:** Reshuffles the rows of the table named TABLENAME randomly.
- **Status:** ✅ VERIFIED - Block EXISTS

### 2.8 TABLE UTILITY OPERATIONS

#### Block ID: `data_rowcountoftable`
- **Category:** Variables
- **Block Type:** Reporter
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_showsnapshotoftable`
- **Category:** Variables
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `data_showtable` / `data_hidetable`
- **Category:** Variables
- **Status:** ✅ VERIFIED - Blocks EXIST

---

## SECTION 3: GOOGLE SHEETS OPERATIONS (for T10.G7.09)

All Google Sheets blocks are in the **Cloud category**.

### 3.1 DATA READ/WRITE OPERATIONS

#### Block ID: `p2p_readfromgooglesheet`
- **Category:** Cloud
- **Block Type:** Command
- **Exact Syntax:** `read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]`
- **Usage Example:** `read from google sheet: url [https://docs.google.com/spreadsheets/d/103DSwIyL4IZVq5te8QqatctJrEVO1mx878J2ah8fAGA/edit?usp=sharing] sheet name [Sheet1] range [B2:G11] into table [tt v]`
- **Description:** Reads data from a Google Sheet at the given URL. Read the data in the sheet named SHEETNAME, and the range of cells will be the given RANGE. The data will be stored in the table named TABLENAME.
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `p2p_writeintogooglesheet`
- **Category:** Cloud
- **Block Type:** Command
- **Exact Syntax:** `write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]`
- **Usage Example:** `write into google sheet: url [https://docs.google.com/spreadsheets/d/103DSwIyL4IZVq5te8QqatctJrEVO1mx878J2ah8fAGA/edit?usp=sharing] sheet name [Sheet2] starting cell [B2] from table [tt v]`
- **Description:** Writes data from the table named TABLENAME into a Google Sheet shared at the given URL. Specify where to write the data in the google sheet using sheet name of SHEETNAME and specify the starting cell's address CELL. Specify which table will be the source data table using TABLENAME. All the data in that table, including the first row of column headers, will be written into the google sheet, starting from the cell at ADDRESS.
- **Status:** ✅ VERIFIED - Block EXISTS

### 3.2 SHEET MANAGEMENT

#### Block ID: `p2p_addsheet`
- **Category:** Cloud
- **Block Type:** Command
- **Exact Syntax:** `add sheet [SHEETNAME] to google sheet at URL [URL]`
- **Usage Example:** `add sheet [summary] to google sheet at URL [https://docs.google.com/spreadsheets/d/aaaa/edit?usp=sharing]`
- **Description:** Add a new sheet with the given name to the google sheet.
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `p2p_removesheet`
- **Category:** Cloud
- **Block Type:** Command
- **Exact Syntax:** `remove sheet [SHEETNAME] from google sheet at URL [URL]`
- **Usage Example:** `remove sheet [summary] from google sheet at URL [https://docs.google.com/spreadsheets/d/aaaa/edit?usp=sharing]`
- **Description:** Remove the sheet with the given name from the google sheet.
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `p2p_listSheetsInGoogleSheet`
- **Category:** Cloud
- **Block Type:** Reporter
- **Status:** ✅ VERIFIED - Block EXISTS

### 3.3 SHEET COLUMN/ROW OPERATIONS

#### Block ID: `p2p_insertcolumnsinsheet`
- **Category:** Cloud
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `p2p_insertrowsinsheet`
- **Category:** Cloud
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `p2p_removecolumnsfromsheet`
- **Category:** Cloud
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `p2p_removerowsfromsheet`
- **Category:** Cloud
- **Status:** ✅ VERIFIED - Block EXISTS

#### Block ID: `p2p_clearsheet`
- **Category:** Cloud
- **Status:** ✅ VERIFIED - Block EXISTS

---

## SECTION 4: AI/ML TABLE ANALYSIS (for T10.G7.10)

### 4.1 NEURAL NETWORK MODEL BLOCKS

#### Block ID: `train_model`
- **Category:** AI
- **Block Type:** Command
- **Exact Syntax:** `train NN model [NAME] using table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN] batch size [BATCHSIZE] epochs [EPOCHS]`
- **Usage Example:** `train NN model [model1] using table [table1 v] rows from [1] to [1000] input columns [x, y] output column [z] batch size [32] epochs [500]`
- **Description:** Trains a compiled neural network model with the given NAME using data from the table TABLENAME. Each row contains one training sample. You can specify which rows to use for training using the STARTROW and ENDROW. You can also specify which columns are used as the input values using INPUTCOLUMNS, which is a comma-separated list of column names. You can specify which column in the table will be used as the output that corresponds to the input values using OUTPUTCOLUMN. You can control the training process using the BATCHSIZE and number of EPOCHS.
- **Status:** ✅ VERIFIED - Block EXISTS
- **Capabilities:** Full neural network training with customizable architecture, batch size, and epochs

#### Block ID: `predict_by_model`
- **Category:** AI
- **Block Type:** Command
- **Exact Syntax:** `predict using NN model [NAME] for table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN]`
- **Usage Example:** `predict using NN model [model1] for table [table2 v] rows from [1] to [100] input columns [x,y] output column [z]`
- **Description:** Predicts the output using the pretrained neural network model with the given NAME for new data in the given table TABLENAME. You can specify the range of rows using the STARTROW and ENDROW. You can specify which columns will be used for the input for the prediction using INPUTCOLUMNS, which is a comma-separated list of column names. You can specify which column to store the predicted value using OUTPUTCOLUMN.
- **Status:** ✅ VERIFIED - Block EXISTS
- **Capabilities:** Inference/prediction using pre-trained models on table data

### 4.2 ALTERNATIVE AI BLOCKS (Pattern Recognition & Classification)

#### Block ID: `ai_createknnclassifier`
- **Category:** AI
- **Block Type:** Command
- **Status:** ✅ VERIFIED - Block EXISTS
- **Note:** K-NN classifier for pattern recognition

#### Block ID: `ai_predictknnclassifier`
- **Category:** AI
- **Block Type:** Reporter
- **Status:** ✅ VERIFIED - Block EXISTS
- **Note:** Predictions using K-NN classifier

---

## SUMMARY TABLE: ALL VERIFIED BLOCKS

| Functionality | Block ID | Category | Type | Status |
|---|---|---|---|---|
| **LIST STATISTICS** | | | | |
| Sum/Avg/Min/Max/Median of List | data_itemspecificvalueoflist | Variables | Reporter | ✅ |
| **TABLE CREATION & COLUMNS** | | | | |
| Copy List to Column | data_setlisttocolumn | Variables | Command | ✅ |
| Insert Columns (Google Sheets) | p2p_insertcolumnsinsheet | Cloud | Command | ✅ |
| **TABLE CELL/ROW OPERATIONS** | | | | |
| Get Item at Row/Column | data_itematrowcolumnoftable | Variables | Reporter | ✅ |
| Change Item at Row/Column | data_changeitematrowcolumn | Variables | Command | ✅ |
| Add Row to Table | data_addrowtotable | Variables | Command | ✅ |
| Delete Row from Table | data_deleterowoftable | Variables | Command | ✅ |
| Delete All Rows | data_deleteallrowsoftable | Variables | Command | ✅ |
| Delete Column | data_deletecolumnfromtable | Variables | Command | ✅ |
| Row at Index | data_rowatindexoftable | Variables | Reporter | ✅ |
| **TABLE AGGREGATION** | | | | |
| Compute Column (Sum/Avg/Min/Max/Median) | data_computetable | Variables | Reporter | ✅ |
| Group By & Aggregate | data_settabletocomputed | Variables | Command | ✅ |
| **TABLE LOOKUP/FILTER** | | | | |
| Lookup Where Column Equals | data_lookuptable | Variables | Reporter | ✅ |
| **PIVOT TABLES** | | | | |
| Pivot Table | data_pivot_table_into_table | Variables | Command | ✅ |
| **TABLE MANIPULATION** | | | | |
| Copy Table | data_copy_table_into_table | Variables | Command | ✅ |
| Append Table | data_append_table_into_table | Variables | Command | ✅ |
| Sort Table | data_sorttablebycolumn | Variables | Command | ✅ |
| Reshuffle Table | data_reshuffletable | Variables | Command | ✅ |
| Row Count | data_rowcountoftable | Variables | Reporter | ✅ |
| Show/Hide Table | data_showtable / data_hidetable | Variables | Command | ✅ |
| **GOOGLE SHEETS** | | | | |
| Read from Google Sheet | p2p_readfromgooglesheet | Cloud | Command | ✅ |
| Write to Google Sheet | p2p_writeintogooglesheet | Cloud | Command | ✅ |
| Add Sheet | p2p_addsheet | Cloud | Command | ✅ |
| Remove Sheet | p2p_removesheet | Cloud | Command | ✅ |
| Insert Rows | p2p_insertrowsinsheet | Cloud | Command | ✅ |
| Insert Columns | p2p_insertcolumnsinsheet | Cloud | Command | ✅ |
| Remove Rows | p2p_removerowsfromsheet | Cloud | Command | ✅ |
| Remove Columns | p2p_removecolumnsfromsheet | Cloud | Command | ✅ |
| Clear Sheet | p2p_clearsheet | Cloud | Command | ✅ |
| List Sheets | p2p_listSheetsInGoogleSheet | Cloud | Reporter | ✅ |
| **AI/ML TABLE ANALYSIS** | | | | |
| Train Neural Network Model | train_model | AI | Command | ✅ |
| Predict Using Model | predict_by_model | AI | Command | ✅ |
| Create K-NN Classifier | ai_createknnclassifier | AI | Command | ✅ |
| Predict with K-NN | ai_predictknnclassifier | AI | Reporter | ✅ |

---

## SECTION 5: RECOMMENDATIONS FOR SKILL DESCRIPTIONS

### For T10.G4.06 (List Statistics)

**Recommended Description:**
"Students learn to compute statistics on numerical lists using the Variables category. They can calculate: smallest value, largest value, sum, average, and median. Use the block `[METHOD v] of list [LISTNAME v]` where METHOD is selected from a dropdown menu. This builds foundational data analysis skills before moving to table operations."

**Key Points:**
- Single reporter block covers all five statistical methods
- Dropdown-based selection (user-friendly for learners)
- All methods available: smallest, largest, sum, average, median

---

### For T10.G5+ (Table Operations)

**Recommended Core Descriptions:**

#### T10.G5.01 - Table Row Operations
"Students learn to add, modify, and delete rows in tables. Blocks include:
- Add row: `add to table [TABLENAME v]: [CELL1] [CELL2] ...` (up to 12 cells)
- Get cell: `item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v]`
- Change cell: `change item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)`
- Delete row: `data_deleterowoftable`
- Delete all rows: `data_deleteallrowsoftable`"

#### T10.G5.02 - Table Aggregation & Analysis
"Students learn to compute statistics across entire columns or groups of rows:
- Single column aggregation: `[METHOD] of column [COLUMNNAME] in table [TABLE v]` (Methods: smallest, largest, sum, average, median)
- Group and aggregate: `set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2]` (Methods: minimum, maximum, sum, average, median)"

#### T10.G5.03 - Table Filtering & Lookup
"Students learn to find data in tables using conditions:
- Lookup where condition: `item in column [RETURNCOLUMN] of [TABLENAME v] where column [SEARCHCOLUMN] equals [SEARCHTEXT]`
This returns a value from one column based on matching criteria in another column."

#### T10.G5.04 - Table Pivoting & Transformation
"Students learn to reshape and summarize table data:
- Pivot table: `pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST]`
Supports comma-separated lists of columns and methods (sum, maximum, minimum, average).
Example: `pivot [table1 v] into [table2 v] row groups [gender,grade] columns [age,height] methods [average,maximum]`"

#### T10.G5.05 - Table Sorting & Organization
"Students learn to organize table data:
- Sort by column: `sort table [TABLENAME v] by column [COLUMN] [SORTORDER v]` (Order: 'large to small' or 'small to large')
- Reshuffle randomly: `reshuffle table [TABLENAME v] randomly`"

---

### For T10.G7.09 (Google Sheets Integration)

**Recommended Description:**
"Students learn to connect their applications to Google Sheets for data sharing and persistence. Key operations include:
- **Read data:** `read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]`
- **Write data:** `write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]`
- **Sheet management:** Add/remove sheets with `add sheet [SHEETNAME] to google sheet at URL [URL]`
- **Data modification:** Insert/remove rows and columns in existing sheets
- **Clear sheet:** `p2p_clearsheet` for resetting data

All blocks require the full Google Sheets URL (from 'Share' link). Data flows bidirectionally between tables and sheets, enabling collaborative data management and persistence across sessions."

---

### For T10.G7.10 (AI/ML Table Analysis)

**Recommended Description:**
"Students learn to apply machine learning to tabular data for prediction and pattern recognition. Two primary approaches:

**Approach 1 - Neural Networks:**
- **Train:** `train NN model [NAME] using table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN] batch size [BATCHSIZE] epochs [EPOCHS]`
- **Predict:** `predict using NN model [NAME] for table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN]`
- Supports supervised learning with customizable hyperparameters

**Approach 2 - Pattern Classification:**
- **Train K-NN:** `ai_createknnclassifier` (creates classifier)
- **Predict:** `ai_predictknnclassifier` (performs classification)
- Useful for pattern recognition without complex hyperparameter tuning

**Key Concepts:**
- Input columns: comma-separated list of feature columns
- Output column: target variable for prediction
- Training uses specified row range for model fitting
- Prediction generates outputs in designated column"

---

## CRITICAL NOTES FOR SKILL WRITERS

1. **Block ID vs Syntax:** Always reference the exact SYNTAX in skill descriptions, not the Block ID. Users interact with the visual blocks, not the internal IDs.

2. **Dropdown Menus:** Blocks like `data_itemspecificvalueoflist` use dropdown selectors for METHOD. Document available options (smallest, largest, sum, average, median).

3. **Column References:** Column names in tables are specified as dropdown selections `[COLUMNNAME]` in most blocks. Pre-existing columns must be defined first.

4. **Comma-Separated Lists:** The `data_pivot_table_into_table` block accepts comma-separated lists for:
   - Row groups: `gender,grade`
   - Value columns: `age,height`
   - Methods: `average,maximum`

5. **Row Indexing:** Tables use 1-based indexing (first row = row 1), NOT 0-based indexing.

6. **Google Sheets URLs:** Full shareable URL required (including `/edit?usp=sharing`), and sheets must have appropriate permissions.

7. **Data Type Consistency:** Aggregation operations (sum, average) expect numerical columns. Smallest/largest works on comparable data types.

8. **Table Requirements:**
   - `data_settabletocomputed` (GROUP BY) requires at least 2 tables defined in project
   - `data_append_table_into_table` requires both tables to have matching columns
   - `data_copy_table_into_table` replaces all data in destination table

9. **AI/ML Considerations:**
   - Models must be trained before predictions
   - Input and output columns must exist in training data
   - Neural network requires reasonable batch size and epoch selection
   - K-NN classifier is simpler but may be less powerful than neural networks

---

## FILE LOCATION
Source file: `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`
Verification completed: 2025-11-22

All blocks referenced in this report have been verified to exist in the blockdes8.txt file with exact syntax, category, and description information extracted.
