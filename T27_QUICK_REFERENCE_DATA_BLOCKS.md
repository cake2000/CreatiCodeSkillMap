# T27 Data Analysis & Visualization - Quick Reference

## Chart Visualization Blocks (3 blocks)

| Block | Chart Types | Primary Use |
|-------|------------|------------|
| `widget_drawchartusinglist` | line, bar, pie, percentage | Single list visualization |
| `widget_drawchartusingcolumn` | line, bar, pie, percentage | Multi-column table visualization |
| `widget_drawchartusingcategory` | pie (only) | Category-based pie charts |

## Table Operations - Quick Group

### Create & Structure (2)
- Add rows, insert rows, replace rows
- Add columns, delete columns

### Read Data (5)
- Get cell value (row/column)
- Get full row (all columns)
- Lookup (VLOOKUP-like)
- Find row by value/substring
- Count rows

### Modify Data (4)
- Replace cell value
- Increment cell (+)
- Decrement cell (-)
- Delete rows (conditional)

### Analysis & Aggregation (4)
- Compute column stats (min, max, sum, avg, median)
- GROUP BY aggregation
- Pivot tables
- Multi-field sorting

### Display (3)
- Show table on stage
- Hide table
- Show snapshot popup with styling

### Import/Export (4)
- Export to CSV
- Import from file (CSV/TXT)
- Save to cloud server
- Load from cloud server

### Combine Tables (3)
- Copy table
- Append table
- Copy list to column

## Database Blocks (13 blocks)

### Fetch/Query (2)
- `database_find_from_collection` - fetch with WHERE/ORDER BY/LIMIT

### Insert/Update/Delete (4)
- Insert from table into collection
- Update from table
- Update in-place with WHERE
- Delete with WHERE

### Conditions (6)
- Comparison (<, >, =, ≠, ≥, ≤)
- Operators (+, -, *, /)
- Contains (substring)
- AND, OR, NOT
- Field reference

### Schema (1)
- Get collection definition

## Google Sheets Blocks (14 blocks)

### Read (2)
- Read from Google Sheet (by range)
- List sheet names

### Write (1)
- Write table to Google Sheet (by cell address)

### Manage (4)
- Add sheet
- Remove sheet
- Clear sheet
- List sheets

### Row/Column Ops (4)
- Insert rows
- Remove rows
- Insert columns
- Remove columns

## Statistical Analysis (1 block)

- **Moving Average**: Simple or exponential on list data

---

## Key Aggregation Methods Supported

**Single Column Stats**:
- smallest, largest, sum, average, median

**GROUP BY & Pivot**:
- minimum, maximum, sum, average

**Database Operations**:
- sum, maximum, minimum, average

---

## Sort Operations

| Operation | Support |
|-----------|---------|
| Single column sort | ✓ (ascending/descending) |
| Multi-field sort | ✓ (database only) |
| Random shuffle | ✓ |

---

## Filter/Query Capabilities

| Capability | Where Available |
|-----------|-----------------|
| Exact value match | Tables, Database |
| Substring match | Tables, Database |
| Numeric comparison | Database (>, <, =, ≠, ≥, ≤) |
| Multiple conditions | Database (AND, OR, NOT) |
| Row deletion by condition | Tables |

---

## Chart Type Support

**Supported Chart Types**:
1. **Line Chart** - Trend visualization
2. **Bar Chart** - Comparative analysis
3. **Pie Chart** - Composition (with/without categories)
4. **Percentage Chart** - Proportional display

**Data Sources**:
- Single list (for simple charts)
- Multiple table columns (for multi-series)
- Category + value columns (for labeled pie)

---

## Data Persistence Options

| Method | Scope | Format |
|--------|-------|--------|
| CSV Export | Local | .csv file |
| File Import | Local | CSV/TXT |
| Cloud Save | Server | Native table format |
| Google Sheets | External | Google Sheets |

---

## Typical Data Analysis Workflow

```
1. Import Data
   - Load from CSV/file OR Google Sheets

2. Clean & Prepare
   - Delete unwanted rows/columns
   - Find and lookup values
   - Transform with list→column copy

3. Analyze
   - Sort/shuffle data
   - Compute aggregations
   - Create pivot tables
   - GROUP BY operations

4. Visualize
   - Create charts from columns/list
   - Show table on stage
   - Display progress bars

5. Export/Save
   - Export to CSV
   - Save to cloud
   - Push to Google Sheets
```

---

## Database Workflow (Cloud Integration)

```
1. Fetch from Collection
   - Query with WHERE conditions
   - Optional sorting
   - Limit results
   → Loads into local table

2. Modify Data
   - Edit table cells
   - Apply transformations

3. Update Back
   - update collection from table OR
   - update collection in-place

4. Delete
   - Remove documents by condition
```

---

## Performance Considerations

**Table Operations**: Fast for <10K rows
**Database Queries**: Indexed lookups available
**Google Sheets**: Network latency expected
**Charts**: Real-time rendering, handles up to ~1000 data points
**Pivot Tables**: Efficient for grouping/aggregation

---

**Use Case Mappings**:
- **Report Generation**: Pivot tables + Charts + Snapshot
- **Data Cleaning**: Filter, delete, replace operations
- **Trend Analysis**: Moving average + Charts
- **Data Integration**: Google Sheets + Import/Export
- **Cloud Storage**: Database collections + Persistence
