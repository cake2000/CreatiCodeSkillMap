# Quick Reference: Verified Block Syntax for T10 Skills

## LIST STATISTICS (T10.G4.06)

```
[METHOD v] of list [LISTNAME v]
```
- Methods: smallest, largest, sum, average, median
- Block ID: `data_itemspecificvalueoflist`

---

## TABLE OPERATIONS (T10.G5+)

### Row Operations
```
add to table [TABLENAME v]: [CELL1] [CELL2] ... [CELL12]
item at row (ROWINDEX) column [COLUMNNAME] of table [TABLE v]
change item at row (ROWNUM) column [COLUMN] of table [TABLENAME v] by (CHANGEAMOUNT)
delete row [ROWNUM] from table [TABLENAME v]
```

### Column Operations
```
copy list [LISTNAME v] to column [COLUMNNAME] of table [TABLENAME v]
delete column [COLUMNNAME] from table [TABLENAME v]
```

### Aggregation
```
[METHOD] of column [COLUMNNAME] in table [TABLE v]
```
Methods: smallest, largest, sum, average, median

### Group By & Aggregate
```
set table [TABLENAME1 v] to [METHOD v] of column [COLUMN1] in table [TABLENAME2 v] by column [COLUMN2]
```
Methods: minimum, maximum, sum, average, median
Requirement: At least 2 tables must exist

### Lookup/Filter
```
item in column [RETURNCOLUMN] of [TABLENAME v] where column [SEARCHCOLUMN] equals [SEARCHTEXT]
```

### Pivot Table
```
pivot [TABLE1] into [TABLE2] row groups [ROWGROUPLIST] columns [VALUECOLUMNLIST] methods [METHODLIST]
```
Example:
```
pivot [table1 v] into [table2 v] row groups [gender,grade] columns [age,height] methods [average,maximum]
```
Methods: sum, maximum, minimum, average

### Sorting & Organization
```
sort table [TABLENAME v] by column [COLUMN] [SORTORDER v]
reshuffle table [TABLENAME v] randomly
```
Sort order: 'large to small' or 'small to large'

### Table Merging
```
copy table [TABLE1] into [TABLE2]
append table [TABLE1] to [TABLE2]
```

---

## GOOGLE SHEETS (T10.G7.09)

### Read/Write
```
read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]
write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]
```

### Sheet Management
```
add sheet [SHEETNAME] to google sheet at URL [URL]
remove sheet [SHEETNAME] from google sheet at URL [URL]
```

### Modify Sheets
```
insert columns in sheet [SHEETNAME] of [URL]
insert rows in sheet [SHEETNAME] of [URL]
remove columns from sheet [SHEETNAME] of [URL]
remove rows from sheet [SHEETNAME] of [URL]
clear sheet [SHEETNAME] of [URL]
```

---

## AI/ML TABLE ANALYSIS (T10.G7.10)

### Neural Network Training
```
train NN model [NAME] using table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN] batch size [BATCHSIZE] epochs [EPOCHS]
```

### Neural Network Prediction
```
predict using NN model [NAME] for table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN]
```

### K-NN Classifier
```
create k-nn classifier [NAME]
predict using k-nn [NAME] with inputs [INPUTCOLUMNS]
```

---

## KEY NOTES

- **Row Indexing:** 1-based (first row = 1)
- **Column Specifiers:** Use dropdowns [COLUMNNAME]
- **Comma Lists:** Use for multiple columns/methods: `col1,col2` or `sum,average`
- **Google Sheets:** Full URL required: `https://docs.google.com/spreadsheets/d/[ID]/edit?usp=sharing`
- **Group By Requirement:** Need at least 2 tables defined in project

---

Generated: 2025-11-22
Source: `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`
