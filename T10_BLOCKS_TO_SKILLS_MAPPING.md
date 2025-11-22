# T10 Skills to Block Mapping

## T10.G4.06 - List Statistics

### Verified Blocks

| Skill Requirement | Block ID | Exact Syntax | Category |
|---|---|---|---|
| Compute sum of list | data_itemspecificvalueoflist | [METHOD v] of list [LISTNAME v] | Variables |
| Compute average of list | data_itemspecificvalueoflist | [METHOD v] of list [LISTNAME v] | Variables |
| Compute minimum/smallest | data_itemspecificvalueoflist | [METHOD v] of list [LISTNAME v] | Variables |
| Compute maximum/largest | data_itemspecificvalueoflist | [METHOD v] of list [LISTNAME v] | Variables |
| Compute median of list | data_itemspecificvalueoflist | [METHOD v] of list [LISTNAME v] | Variables |

### Description
Students use a single reporter block with a METHOD dropdown. Selecting different methods (smallest, largest, sum, average, median) allows computing different statistics on numerical lists.

**Skill Concept:** "Statistical Analysis of Lists"
- Single block, multiple methods via dropdown
- Perfect for introduction to data aggregation
- Foundation for moving to table-based analysis

---

## T10.G5.01 - Table Row Operations

### Verified Blocks

| Skill Requirement | Block ID | Exact Syntax | Category |
|---|---|---|---|
| Add new row | data_addrowtotable | add to table [TABLENAME v]: [CELL1] [CELL2] ... [CELL12] | Variables |
| Get cell value | data_itematrowcolumnoftable | item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v] | Variables |
| Modify cell value | data_changeitematrowcolumn | change item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT) | Variables |
| Delete single row | data_deleterowoftable | delete row [ROWNUM] from table [TABLENAME v] | Variables |
| Delete all rows | data_deleteallrowsoftable | delete all rows of table [TABLENAME v] | Variables |
| Get row count | data_rowcountoftable | row count of table [TABLENAME v] | Variables |
| Access entire row | data_rowatindexoftable | row [ROWNUM] of table [TABLENAME v] | Variables |

### Description
Students learn fundamental table manipulation by adding, reading, modifying, and deleting rows.

**Skill Concept:** "Managing Table Rows"
- Add rows: Up to 12 cells per row using single block
- Read cells: Access individual cells by row and column name
- Modify cells: Change values with addition operator (not direct replacement)
- Delete: Single row or all rows
- Count: Get total number of rows in table

**Dependencies:** Students should understand basic table structure from T10.G4

---

## T10.G5.02 - Table Column Operations

### Verified Blocks

| Skill Requirement | Block ID | Exact Syntax | Category |
|---|---|---|---|
| Copy list to column | data_setlisttocolumn | copy list [LISTNAME v] to column [COLUMNNAME] of table [TABLENAME v] | Variables |
| Delete column | data_deletecolumnfromtable | delete column [COLUMNNAME] from table [TABLENAME v] | Variables |
| Remove all columns | data_removeallcolumnsfromtable | remove all columns from table [TABLENAME v] | Variables |
| Insert column (Google Sheets) | p2p_insertcolumnsinsheet | insert [N] columns in sheet [SHEETNAME] of [URL] | Cloud |

### Description
Students learn to work with table columns - adding/replacing data and removing structure.

**Skill Concept:** "Managing Table Columns"
- Add/replace column: Copy list data into existing column (overwrites existing data)
- Delete column: Remove entire column structure
- Insert columns: For Google Sheets integration (T10.G7.09)

**Important Notes:**
- Column must exist before copying list into it
- Use this after creating table structure
- For Google Sheets, must reference full URL

---

## T10.G5.03 - Table Aggregation & Statistics

### Verified Blocks

| Skill Requirement | Block ID | Exact Syntax | Category |
|---|---|---|---|
| Sum column | data_computetable | [METHOD] of column [COLUMNNAME] in table [TABLE v] | Variables |
| Average column | data_computetable | [METHOD] of column [COLUMNNAME] in table [TABLE v] | Variables |
| Min/Max of column | data_computetable | [METHOD] of column [COLUMNNAME] in table [TABLE v] | Variables |
| Median of column | data_computetable | [METHOD] of column [COLUMNNAME] in table [TABLE v] | Variables |
| Group and aggregate | data_settabletocomputed | set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2] | Variables |

### Description
Students learn to compute statistics across entire table columns, and to group data by category before aggregating.

**Skill Concept:** "Statistical Analysis of Tables"

**Basic Aggregation (data_computetable):**
- Methods: smallest, largest, sum, average, median
- Single reporter block with METHOD dropdown
- Returns single value for entire column

**Group By & Aggregate (data_settabletocomputed):**
- Groups rows by values in one column (e.g., by gender, grade)
- Aggregates another column (e.g., average scores) per group
- Stores results in new table
- Requirement: Need at least 2 tables in project

**Example Use Case:**
```
Input: Table of students with columns [name, grade, score]
Block: set table [summary v] to [average v] of column [score] in table [students v] by column [grade]
Output: New table with unique grades and average score per grade
```

---

## T10.G5.04 - Table Filtering & Lookup

### Verified Blocks

| Skill Requirement | Block ID | Exact Syntax | Category |
|---|---|---|---|
| Lookup value (WHERE) | data_lookuptable | item in column [RETURNCOLUMN] of [TABLENAME v] where column [SEARCHCOLUMN] equals [SEARCHTEXT] | Variables |

### Description
Students learn to search tables for specific values based on conditions.

**Skill Concept:** "Filtering and Looking Up Data"

**Single Block - Multiple Uses:**
- Find a specific value in one column (e.g., find age WHERE name equals 'John')
- Returns first matching value
- Can chain multiple lookups for more complex queries
- Reporter block (returns value, doesn't modify table)

**Example Use Cases:**
```
1. Find student age by name:
   item in column [age] of [students v] where column [name] equals [John]

2. Find product price by ID:
   item in column [price] of [inventory v] where column [id] equals [12345]

3. Find score by student name:
   item in column [score] of [results v] where column [student_name] equals [Alice]
```

---

## T10.G5.05 - Table Transformation: Pivot Tables

### Verified Blocks

| Skill Requirement | Block ID | Exact Syntax | Category |
|---|---|---|---|
| Create pivot table | data_pivot_table_into_table | pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST] | Variables |

### Description
Students learn to reshape and summarize data using pivot tables.

**Skill Concept:** "Pivoting and Reshaping Data"

**Syntax Breakdown:**
- TABLE1: Source table to pivot
- TABLE2: Destination table for results
- ROWGROUPLIST: Comma-separated columns to group by (e.g., `gender,grade`)
- VALUECOLUMNLIST: Comma-separated columns to aggregate (e.g., `age,score`)
- METHODLIST: Comma-separated aggregation methods (e.g., `average,sum`)

**Methods Available:** sum, maximum, minimum, average

**Example:**
```
pivot [sales v] into [summary v] row groups [region,product] columns [revenue,units] methods [sum,sum]

Input Table (sales):
| region | product | revenue | units |
|--------|---------|---------|-------|
| North  | Widget  | 1000    | 50    |
| North  | Gadget  | 2000    | 75    |
| South  | Widget  | 800     | 40    |
| South  | Gadget  | 1500    | 60    |

Output Table (summary):
| region | product | revenue | units |
|--------|---------|---------|-------|
| North  | Gadget  | 2000    | 75    |
| North  | Widget  | 1000    | 50    |
| South  | Gadget  | 1500    | 60    |
| South  | Widget  | 800     | 40    |
```

**Key Characteristics:**
- Powerful for multi-dimensional analysis
- Can have multiple row groups and value columns
- Different methods per value column (useful when one should sum, another average)
- Creates new table with unique combinations of grouping columns

---

## T10.G5.06 - Table Sorting & Organization

### Verified Blocks

| Skill Requirement | Block ID | Exact Syntax | Category |
|---|---|---|---|
| Sort table | data_sorttablebycolumn | sort table [TABLENAME v] by column [COLUMN] [SORTORDER v] | Variables |
| Shuffle table | data_reshuffletable | reshuffle table [TABLENAME v] randomly | Variables |

### Description
Students learn to organize table data for analysis and presentation.

**Skill Concept:** "Organizing and Ordering Data"

**Sorting:**
- Sort by any column (numerical or text)
- Two sort orders: 'large to small' (descending) or 'small to large' (ascending)
- Modifies table in place
- Can sort multiple times by different columns

**Shuffling:**
- Randomizes row order
- Useful for randomized testing or data anonymization
- Modifies table in place

**Use Cases:**
```
1. Sort students by score (highest to lowest):
   sort table [results v] by column [score] [large to small v]

2. Sort products alphabetically:
   sort table [inventory v] by column [name] [small to large v]

3. Randomize test question order:
   reshuffle table [questions v] randomly
```

---

## T10.G5.07 - Table Merging & Copying

### Verified Blocks

| Skill Requirement | Block ID | Exact Syntax | Category |
|---|---|---|---|
| Copy table | data_copy_table_into_table | copy table [TABLE1] into [TABLE2] | Variables |
| Append table | data_append_table_into_table | append table [TABLE1] to [TABLE2] | Variables |

### Description
Students learn to combine and duplicate table data.

**Skill Concept:** "Combining and Duplicating Tables"

**Copy Table:**
- Completely replaces destination table
- Result: TABLE2 = exact copy of TABLE1 (same columns, same data)
- Useful for: Backup, branching analysis, resetting data

**Append Table:**
- Adds rows from TABLE1 to bottom of TABLE2
- Tables must have same column structure
- Modifies TABLE2 in place
- Useful for: Combining datasets, accumulating results, merging data sources

**Example Workflow:**
```
1. Start with [original] table
2. copy table [original] into [working]     // Create working copy
3. sort table [working] by column [date]    // Modify working copy
4. append table [new_data] to [results]     // Add new rows to accumulator
```

---

## T10.G7.09 - Google Sheets Integration

### Verified Blocks

| Skill Requirement | Block ID | Exact Syntax | Category |
|---|---|---|---|
| Read from Google Sheet | p2p_readfromgooglesheet | read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v] | Cloud |
| Write to Google Sheet | p2p_writeintogooglesheet | write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v] | Cloud |
| Add sheet | p2p_addsheet | add sheet [SHEETNAME] to google sheet at URL [URL] | Cloud |
| Remove sheet | p2p_removesheet | remove sheet [SHEETNAME] from google sheet at URL [URL] | Cloud |
| Insert columns | p2p_insertcolumnsinsheet | insert [N] columns in sheet [SHEETNAME] of [URL] | Cloud |
| Insert rows | p2p_insertrowsinsheet | insert [N] rows in sheet [SHEETNAME] of [URL] | Cloud |
| Remove columns | p2p_removecolumnsfromsheet | remove [N] columns from sheet [SHEETNAME] of [URL] | Cloud |
| Remove rows | p2p_removerowsfromsheet | remove [N] rows from sheet [SHEETNAME] of [URL] | Cloud |
| Clear sheet | p2p_clearsheet | clear sheet [SHEETNAME] of [URL] | Cloud |
| List sheets | p2p_listSheetsInGoogleSheet | list of sheets in google sheet [URL] | Cloud |

### Description
Students learn to connect their applications to Google Sheets for persistent data storage and collaboration.

**Skill Concept:** "Cloud Data Integration with Google Sheets"

**Key Operations:**

**Read Data:**
```
read from google sheet:
  url [https://docs.google.com/spreadsheets/d/ABC123/edit?usp=sharing]
  sheet name [Sheet1]
  range [B2:G11]
  into table [mydata v]
```
- Downloads specific range from Google Sheet
- Range format: Excel-style (A1:Z99)
- Creates/replaces table with downloaded data

**Write Data:**
```
write into google sheet:
  url [https://docs.google.com/spreadsheets/d/ABC123/edit?usp=sharing]
  sheet name [Sheet2]
  start cell [B2]
  from table [mydata v]
```
- Uploads entire table starting at specified cell
- Includes column headers in first row
- Overwrites existing data in target range

**Sheet Management:**
- Add sheet: Create new sheet in spreadsheet
- Remove sheet: Delete entire sheet
- Insert/remove rows/columns: Modify sheet structure

**Prerequisites:**
- Google Account required
- Spreadsheet must be shared (via Share button)
- Full URL including `/edit?usp=sharing`
- Consistent column naming between application and sheets

**Use Cases:**
```
1. Save game progress to cloud:
   write into google sheet: ... from table [player_data v]

2. Load leaderboard from shared sheet:
   read from google sheet: ... into table [scores v]

3. Collaborative data collection:
   Multiple students read/write to same sheet

4. Data persistence:
   Save student work, reload on next session
```

---

## T10.G7.10 - AI/ML Table Analysis

### Verified Blocks

| Skill Requirement | Block ID | Exact Syntax | Category |
|---|---|---|---|
| Train neural network | train_model | train NN model [NAME] using table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN] batch size [BATCHSIZE] epochs [EPOCHS] | AI |
| Make predictions | predict_by_model | predict using NN model [NAME] for table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN] | AI |
| Create classifier | ai_createknnclassifier | create k-nn classifier [NAME] | AI |
| Predict class | ai_predictknnclassifier | predict using k-nn [NAME] with inputs [INPUTCOLUMNS] | AI |

### Description
Students learn to apply machine learning to tabular data for predictive analysis.

**Skill Concept:** "Machine Learning with Tables"

**Approach 1: Neural Network Regression/Classification**

**Training:**
```
train NN model [house_price_model]
  using table [training_data v]
  rows from [1] to [1000]
  input columns [sq_ft, bedrooms, age]
  output column [price]
  batch size [32]
  epochs [100]
```

**Parameters:**
- NAME: Model identifier (used in prediction)
- TABLENAME: Source data table
- STARTROW/ENDROW: Training data range (1-based indexing)
- INPUTCOLUMNS: Comma-separated feature columns (e.g., `sq_ft,bedrooms,age`)
- OUTPUTCOLUMN: Target variable (e.g., `price`)
- BATCHSIZE: Samples per gradient update (typically 16-64)
- EPOCHS: Full passes through training data (typically 50-500)

**Prediction:**
```
predict using NN model [house_price_model]
  for table [test_data v]
  rows from [1] to [100]
  input columns [sq_ft,bedrooms,age]
  output column [predicted_price]
```

**Approach 2: K-Nearest Neighbors Classification**

**Training:**
```
create k-nn classifier [digit_classifier]
```
(Training data is implicit, often collected separately)

**Prediction:**
```
predict using k-nn [digit_classifier]
  with inputs [pixel1,pixel2,pixel3,...]
```

**Key Differences:**
| Aspect | Neural Network | K-NN |
|---|---|---|
| Best for | Regression, complex patterns | Classification, pattern matching |
| Training | Explicit training phase required | Often trained separately/incrementally |
| Hyperparameters | Batch size, epochs, architecture | K value, distance metric |
| Accuracy | Generally high for complex data | Varies with data distribution |
| Speed | Medium (depends on size) | Fast (simple distance calculation) |

**Example Workflow:**

```
Predicting house prices:

1. Prepare training data table [homes v]:
   Columns: [sq_ft, bedrooms, bathrooms, price]
   Data: 1000 historical listings

2. Train model:
   train NN model [price_predictor]
     using table [homes v]
     rows from [1] to [900]
     input columns [sq_ft,bedrooms,bathrooms]
     output column [price]
     batch size [32] epochs [200]

3. Evaluate on test set:
   predict using NN model [price_predictor]
     for table [homes v]
     rows from [901] to [1000]
     input columns [sq_ft,bedrooms,bathrooms]
     output column [predicted_price]

4. Use for predictions on new data:
   predict using NN model [price_predictor]
     for table [listings v]
     rows from [1] to [50]
     input columns [sq_ft,bedrooms,bathrooms]
     output column [estimated_price]
```

**Prerequisites:**
- Clean numerical data required
- Input and output columns must exist in tables
- Training data should be representative
- Scale/normalize features for better results (may require pre-processing)

---

## SUMMARY TABLE: All T10 Blocks Verified

| T10 Topic | Category | Primary Blocks | Status |
|---|---|---|---|
| T10.G4.06 | List Stats | data_itemspecificvalueoflist | ✅ Verified |
| T10.G5.01 | Table Rows | data_addrowtotable, data_itematrowcolumnoftable, data_changeitem... | ✅ Verified |
| T10.G5.02 | Table Columns | data_setlisttocolumn, data_deletecolumnfromtable | ✅ Verified |
| T10.G5.03 | Table Aggregation | data_computetable, data_settabletocomputed | ✅ Verified |
| T10.G5.04 | Table Filtering | data_lookuptable | ✅ Verified |
| T10.G5.05 | Pivot Tables | data_pivot_table_into_table | ✅ Verified |
| T10.G5.06 | Sort/Shuffle | data_sorttablebycolumn, data_reshuffletable | ✅ Verified |
| T10.G5.07 | Merge Tables | data_copy_table_into_table, data_append_table_into_table | ✅ Verified |
| T10.G7.09 | Google Sheets | p2p_readfromgooglesheet, p2p_writeintogooglesheet, ... | ✅ Verified |
| T10.G7.10 | AI/ML | train_model, predict_by_model, ai_createknnclassifier | ✅ Verified |

---

## Important Implementation Notes

1. **Block Access:** All blocks referenced are available in TurboWarp (ScratchCopilot)
2. **Syntax:** Use EXACT syntax shown (capitalization, brackets, dropdown indicators [v])
3. **Block IDs:** Never use IDs in student-facing descriptions; use visible syntax
4. **Dropdowns:** [METHOD v], [SORTORDER v], etc. indicate user-selectable options
5. **Row Indexing:** Tables use 1-based indexing (first row = row 1, not 0)
6. **Data Types:** Aggregation with numbers requires numerical columns
7. **Column Names:** Must be exact matches (case-sensitive in many contexts)
8. **Google Sheets URLs:** Must include full share URL with `/edit?usp=sharing`

---

Document Generated: 2025-11-22
Source: `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`
All blocks verified to exist with exact syntax as documented.
