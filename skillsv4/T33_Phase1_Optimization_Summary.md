# T33 - Connected Services: Phase 1 Optimization Summary

## Overview

Topic T33 (Connected Services & Tool Wrappers) has been optimized to break down overly broad skills into more focused, manageable units. Each skill now focuses on ONE specific block or feature, making it easier for students to learn and for instructors to assess.

## Skills Count

| Grade | Before | After | Change |
|-------|--------|-------|--------|
| GK | 1 | 1 | - |
| G1 | 1 | 1 | - |
| G2 | 1 | 1 | - |
| G3 | 1 | 1 | - |
| G4 | 1 | 1 | - |
| G5 | 3 | 3 | - |
| G6 | 10 | 11 | +1 |
| G7 | 12 | 16 | +4 |
| G8 | 6 | 10 | +4 |
| **Total** | **36** | **46** | **+10** |

## Key Changes Made

### Grade 6 Changes

**T33.G6.10** (Insert and fetch data from cloud database collections) was split into:
- **T33.G6.10.01**: Insert table data into a cloud database collection
  - Focuses on the `insert from table [TABLENAME v] row from (STARTROW) to (ENDROW) into collection [COLLECTIONNAME v]` block
- **T33.G6.10.02**: Fetch all data from a cloud database collection
  - Focuses on the `fetch from collection [COLLECTIONNAME v] into table [TABLENAME v]` block (without WHERE conditions)

### Grade 7 Changes

**T33.G7.01** (List, add, and remove sheets in a Google Spreadsheet) was split into:
- **T33.G7.01.01**: List all sheets in a Google Spreadsheet
  - Uses `list all sheets in google sheet at URL [SHEET_URL] into list [LIST]`
- **T33.G7.01.02**: Add a new sheet to a Google Spreadsheet
  - Uses `add sheet [SHEETNAME] to google sheet at URL [URL]`
- **T33.G7.01.03**: Remove a sheet from a Google Spreadsheet
  - Uses `remove sheet [SHEETNAME] from google sheet at URL [URL]`

**T33.G7.02** (Perform targeted Google Sheets cell operations) was split into:
- **T33.G7.02.01**: Get a single cell value from a Google Sheet
  - Uses `value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
- **T33.G7.02.02**: Set a single cell value in a Google Sheet
  - Uses `set value to [VALUE] at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`

**T33.G7.05** (Synchronize variables across projects using cloud sessions) was split into:
- **T33.G7.05.01**: Create a cloud session for real-time variable sharing
  - Uses `create cloud session [SESSION]`
- **T33.G7.05.02**: Join a cloud session to synchronize variables with others
  - Uses `join cloud session [SESSION]`

**T33.G7.11** (Update and delete cloud collection data) was split into:
- **T33.G7.11.01**: Update cloud collection data using table-based updates
  - Uses `update collection [COLLECTIONNAME v] from table [TABLENAME v]`
- **T33.G7.11.02**: Update cloud collection fields in-place with WHERE conditions
  - Uses `update collection [COLLECTIONNAME v] in-place where <CONDITION> set (FIELD1) to (VALUE1)`
- **T33.G7.11.03**: Remove documents from cloud collections with WHERE conditions
  - Uses `remove all documents from collection [COLLECTIONNAME v] where <CONDITION>`

**T33.G7.12** (Build complex collection queries with AND/OR/NOT logic) was split into:
- **T33.G7.12.01**: Combine query conditions with AND/OR/NOT logic
  - Uses `<cond <> and <>>`, `<cond <> or <>>`, and `<cond not <>>` blocks
- **T33.G7.12.02**: Sort and limit collection query results
  - Uses `LIMIT` and `SORT BY` parameters in fetch queries

### Grade 8 Changes

**T33.G8.01** (Insert and remove rows and columns dynamically in Google Sheets) was split into:
- **T33.G8.01.01**: Insert and remove rows dynamically in Google Sheets
  - Uses `insert [COUNT] rows at row [STARTR]` and `remove rows [FROMR] to [TOR]` blocks
- **T33.G8.01.02**: Insert and remove columns dynamically in Google Sheets
  - Uses `insert [COUNT] columns at column [STARTC]` and `remove columns [FROMC] to [TOC]` blocks

## Dependency Updates

All intra-topic dependencies were updated to reference the new skill IDs:

| Old Dependency | New Dependency | Skills Affected |
|----------------|----------------|-----------------|
| T33.G6.10 | T33.G6.10.02 | T33.G7.10 |
| T33.G7.01 | T33.G7.01.03 | T33.G8.01.01 |
| T33.G7.02 | T33.G7.02.02 | T33.G7.03, T33.G8.01.01 |
| T33.G7.11 | T33.G7.11.01 | T33.G7.12.01 |

## Dependency Rule Compliance

All dependencies follow the **X-2 rule**:
- Grade 6 skills depend only on grades 4, 5, 6 (or earlier)
- Grade 7 skills depend only on grades 5, 6, 7 (or earlier)
- Grade 8 skills depend only on grades 6, 7, 8 (or earlier)

All **cross-topic dependencies** (T## where ## != 33) were preserved unchanged.

## Skills Now Accurately Reflect CreatiCode Blocks

Each skill description now includes the exact block syntax from CreatiCode, making it clear which specific block students will learn:

### Cloud Category Blocks Covered:
1. **Web Fetch**: `fetch web page as [FORMAT] from URL [URL]`
2. **Google Sheets Read**: `read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]`
3. **Google Sheets Write**: `write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]`
4. **Get Cell Value**: `value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
5. **Set Cell Value**: `set value to [VALUE] at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
6. **Append Row**: `append row [ROWNUMBER] from table [TABLENAME v] to sheet [SHEETNAME] in Google Sheet at URL [URL]`
7. **List Sheets**: `list all sheets in google sheet at URL [SHEET_URL] into list [LIST]`
8. **Add Sheet**: `add sheet [SHEETNAME] to google sheet at URL [URL]`
9. **Remove Sheet**: `remove sheet [SHEETNAME] from google sheet at URL [URL]`
10. **Clear Sheet**: `clear sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
11. **Insert Rows**: `insert [COUNT] rows at row [STARTR] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
12. **Insert Columns**: `insert [COUNT] columns at column [STARTC] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
13. **Remove Rows**: `remove rows [FROMR] to [TOR] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
14. **Remove Columns**: `remove columns [FROMC] to [TOC] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
15. **Google Drive List**: `list content of Google Drive folder [URL] in table [TABLENAME v]`
16. **Create Cloud Session**: `create cloud session [SESSION]`
17. **Join Cloud Session**: `join cloud session [SESSION]`

### Database Category Blocks Covered:
1. **Insert**: `insert from table [TABLENAME v] row from (STARTROW) to (ENDROW) into collection [COLLECTIONNAME v]`
2. **Fetch**: `fetch from collection [COLLECTIONNAME v] into table [TABLENAME v] where <CONDITION> limit (LIMIT) sort by (SORTFIELD1) [SORTORDER1 v]`
3. **Update from Table**: `update collection [COLLECTIONNAME v] from table [TABLENAME v]`
4. **Update In-Place**: `update collection [COLLECTIONNAME v] in-place where <CONDITION> set (FIELD1) to (VALUE1)`
5. **Remove**: `remove all documents from collection [COLLECTIONNAME v] where <CONDITION>`
6. **Query Condition**: `<cond [INPUT1] [COMPARATOR v] [INPUT2]>` (>, <, =, etc.)
7. **Contains**: `<cond (field [FIELDNAME]) contains [TEXT]?>`
8. **AND/OR/NOT**: `<cond <> and <>>`, `<cond <> or <>>`, `<cond not <>>`
9. **Field Reference**: `field [FIELDNAME]`

## Complete New Skill List for T33

### Grade K (1 skill)
- T33.GK.01: Recognize that apps can talk to helpers on the internet

### Grade 1 (1 skill)
- T33.G1.01: Sort apps into online helpers and offline tools

### Grade 2 (1 skill)
- T33.G2.01: Describe what happens when an app waits for the internet

### Grade 3 (1 skill)
- T33.G3.01: Identify cloud-connected features in familiar apps

### Grade 4 (1 skill)
- T33.G4.01: Explain how apps store and retrieve data from the cloud

### Grade 5 (3 skills)
- T33.G5.01: Compare local storage versus cloud storage tradeoffs
- T33.G5.02: Distinguish real-time collaboration from one-time requests
- T33.G5.03: Understand that shared URLs grant public access

### Grade 6 (11 skills)
- T33.G6.01: Identify and test Cloud blocks for network dependencies
- T33.G6.02: Fetch web content using the fetch URL block
- T33.G6.03: Read data from Google Sheets into a table
- T33.G6.04: Write data from a table to Google Sheets
- T33.G6.05: Clear a Google Sheet to reset data
- T33.G6.06: Handle latency and error states in service calls
- T33.G6.07: Respect usage limits and rate limiting
- T33.G6.08: Apply privacy principles to Google Sheet URLs
- T33.G6.09: Understand cloud database collections versus Google Sheets
- T33.G6.10.01: Insert table data into a cloud database collection
- T33.G6.10.02: Fetch all data from a cloud database collection

### Grade 7 (16 skills)
- T33.G7.01.01: List all sheets in a Google Spreadsheet
- T33.G7.01.02: Add a new sheet to a Google Spreadsheet
- T33.G7.01.03: Remove a sheet from a Google Spreadsheet
- T33.G7.02.01: Get a single cell value from a Google Sheet
- T33.G7.02.02: Set a single cell value in a Google Sheet
- T33.G7.03: Append rows incrementally to a Google Sheet
- T33.G7.04: Browse Google Drive folder contents
- T33.G7.05.01: Create a cloud session for real-time variable sharing
- T33.G7.05.02: Join a cloud session to synchronize variables with others
- T33.G7.06: Understand automatic service authorization in CreatiCode
- T33.G7.07: Build workflows that combine multiple services
- T33.G7.08: Compare service options and pick the right tool
- T33.G7.09: Cache service responses in tables to avoid redundant API calls
- T33.G7.10: Query cloud collections with WHERE conditions
- T33.G7.11.01: Update cloud collection data using table-based updates
- T33.G7.11.02: Update cloud collection fields in-place with WHERE conditions
- T33.G7.11.03: Remove documents from cloud collections with WHERE conditions
- T33.G7.12.01: Combine query conditions with AND/OR/NOT logic
- T33.G7.12.02: Sort and limit collection query results

### Grade 8 (10 skills)
- T33.G8.01.01: Insert and remove rows dynamically in Google Sheets
- T33.G8.01.02: Insert and remove columns dynamically in Google Sheets
- T33.G8.02: Review terms of service for external services
- T33.G8.03: Simulate service outages and design fallbacks
- T33.G8.04: Validate and sanitize data received from external services
- T33.G8.05: Compare service-based and local implementations through hands-on testing
- T33.G8.06: Build a cloud-integrated data pipeline
