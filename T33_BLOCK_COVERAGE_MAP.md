# T33 Block Coverage Map
**Date:** 2024-11-24

## CreatiCode Blocks for Connected Services & Tool Wrappers

This document maps all available CreatiCode blocks in the Cloud and Database categories to their corresponding T33 skills.

---

## Category: Cloud (15 blocks)

### Web Fetch (1 block)

#### Block: `fetch web page as [FORMAT] from URL [URL]`
- **Block ID:** p2p_fetchfromurl
- **Skill:** T33.G6.02 (Fetch web content using the fetch URL block)
- **Grade:** 6
- **Status:** ✅ Fully covered
- **Description:** Retrieves web content and converts HTML to markdown

---

### Google Sheets - Basic Read/Write (3 blocks)

#### Block: `read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]`
- **Block ID:** p2p_readfromgooglesheet
- **Skill:** T33.G6.03 (Read data from Google Sheets into a table)
- **Grade:** 6
- **Status:** ✅ Fully covered
- **Parameters:**
  - URL: Google Sheet share URL
  - SHEETNAME: Name of sheet (e.g., "Sheet1")
  - RANGE: Cell range (e.g., "A1:C10")
  - TABLENAME: Target CreatiCode table

#### Block: `write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]`
- **Block ID:** p2p_writeintogooglesheet
- **Skill:** T33.G6.04 (Write data from a table to Google Sheets)
- **Grade:** 6
- **Status:** ✅ Fully covered
- **Parameters:**
  - URL: Google Sheet share URL
  - SHEETNAME: Target sheet name
  - ADDRESS: Starting cell (e.g., "A1")
  - TABLENAME: Source CreatiCode table

#### Block: `clear sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
- **Block ID:** p2p_clearsheet
- **Skill:** T33.G6.05 (Clear a Google Sheet to reset data)
- **Grade:** 6
- **Status:** ✅ Fully covered
- **Note:** Clears content but keeps sheet structure

---

### Google Sheets - Sheet Management (3 blocks)

#### Block: `list all sheets in google sheet at URL [SHEET_URL] into list [LIST]`
- **Block ID:** p2p_listSheetsInGoogleSheet
- **Skill:** T33.G7.01 (List, add, and remove sheets)
- **Grade:** 7
- **Status:** ⚠️ Combined with other operations
- **Recommendation:** Split into T33.G7.01a

#### Block: `add sheet [SHEETNAME] to google sheet at URL [URL]`
- **Block ID:** p2p_addsheet
- **Skill:** T33.G7.01 (List, add, and remove sheets)
- **Grade:** 7
- **Status:** ⚠️ Combined with other operations
- **Recommendation:** Split into T33.G7.01b

#### Block: `remove sheet [SHEETNAME] from google sheet at URL [URL]`
- **Block ID:** p2p_removesheet
- **Skill:** T33.G7.01 (List, add, and remove sheets)
- **Grade:** 7
- **Status:** ⚠️ Combined with other operations
- **Recommendation:** Split into T33.G7.01c

---

### Google Sheets - Cell Operations (3 blocks)

#### Block: `get value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
- **Block ID:** p2p_getvalue (reporter)
- **Skill:** T33.G7.02 (Perform targeted cell operations)
- **Grade:** 7
- **Status:** ✅ Covered (paired with set value)
- **Returns:** Single cell value

#### Block: `set value to [VALUE] at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
- **Block ID:** p2p_setvalue
- **Skill:** T33.G7.02 (Perform targeted cell operations)
- **Grade:** 7
- **Status:** ✅ Covered (paired with get value)
- **Note:** Updates single cell without rewriting entire sheet

#### Block: `append row [ROWNUMBER] from table [TABLENAME v] to sheet [SHEETNAME] in Google Sheet at URL [URL]`
- **Block ID:** p2p_appendrow
- **Skill:** T33.G7.03 (Append rows incrementally)
- **Grade:** 7
- **Status:** ✅ Fully covered
- **Use case:** Logging data over time without overwriting

---

### Google Sheets - Structure Management (4 blocks)

#### Block: `insert [COUNT] rows at row [STARTR] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
- **Block ID:** p2p_insertrowsinsheet
- **Skill:** T33.G8.01 (Insert and remove rows and columns)
- **Grade:** 8
- **Status:** ✅ Covered but may need split

#### Block: `remove rows [FROMR] to [TOR] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
- **Block ID:** p2p_removerowsfromsheet
- **Skill:** T33.G8.01 (Insert and remove rows and columns)
- **Grade:** 8
- **Status:** ✅ Covered but may need split

#### Block: `insert [COUNT] columns at column [STARTC] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
- **Block ID:** p2p_insertcolumnsinsheet
- **Skill:** T33.G8.01 (Insert and remove rows and columns)
- **Grade:** 8
- **Status:** ✅ Covered but may need split

#### Block: `remove columns [FROMC] to [TOC] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
- **Block ID:** p2p_removecolumnsfromsheet
- **Skill:** T33.G8.01 (Insert and remove rows and columns)
- **Grade:** 8
- **Status:** ✅ Covered but may need split

---

### Google Drive (1 block)

#### Block: `list content of Google Drive folder [URL] in table [TABLENAME v]`
- **Block ID:** p2p_getgooglefoldercontent
- **Skill:** T33.G7.04 (Browse Google Drive folder contents)
- **Grade:** 7
- **Status:** ✅ Fully covered
- **Returns:** Table with columns: filename, file ID, MIME type, URL

---

## Category: Database (11 blocks)

### Collection CRUD Operations (5 blocks)

#### Block: `insert from table [TABLENAME v] row from (STARTROW) to (ENDROW) into collection [COLLECTIONNAME v]`
- **Block ID:** database_insert_from_table
- **Skill:** T33.G6.10 (Insert and fetch data from collections)
- **Grade:** 6
- **Status:** ⚠️ Has dependency violations
- **Note:** Saves table rows as collection documents

#### Block: `fetch from collection [COLLECTIONNAME v] into table [TABLENAME v] where <CONDITION> limit (LIMIT) sort by (SORTFIELD1) [SORTORDER1 v] (SORTFIELD2) [SORTORDER2 v]`
- **Block ID:** database_find_from_collection
- **Skills:**
  - T33.G6.10 (basic fetch)
  - T33.G7.10 (with WHERE conditions)
  - T33.G7.12 (with AND/OR/NOT, LIMIT, SORT)
- **Grade:** 6, 7, 7
- **Status:** ⚠️ Too broad, needs splitting
- **Parameters:**
  - CONDITION: Boolean expression using cond blocks
  - LIMIT: Maximum documents to return
  - SORTFIELD: Field name to sort by
  - SORTORDER: 1 (ascending) or -1 (descending)

#### Block: `update collection [COLLECTIONNAME v] from table [TABLENAME v]`
- **Block ID:** database_update_collection
- **Skill:** T33.G7.11 (Update collections from tables)
- **Grade:** 7
- **Status:** ⚠️ Combined with other update operations
- **Recommendation:** Split into T33.G7.11a
- **Process:** Load to table → modify → write back

#### Block: `update collection [COLLECTIONNAME v] in-place where <CONDITION> set (FIELD1) to (VALUE1) set (FIELD2) to (VALUE2) ...`
- **Block ID:** database_update_collection_in_place
- **Skill:** T33.G7.11 (Update collections in-place)
- **Grade:** 7
- **Status:** ⚠️ Combined with other update operations
- **Recommendation:** Split into T33.G7.11b
- **Advantage:** Direct field updates without loading entire collection

#### Block: `remove all documents from collection [COLLECTIONNAME v] where <CONDITION>`
- **Block ID:** database_remove_all_document
- **Skill:** T33.G7.11 (Delete documents)
- **Grade:** 7
- **Status:** ⚠️ Combined with update operations
- **Recommendation:** Split into T33.G7.11c
- **Note:** Permanent deletion - no undo

---

### Query Helper Blocks (2 blocks)

#### Block: `collection [COLLECTIONNAME]`
- **Block ID:** database_collection (reporter)
- **Skill:** Not explicitly covered
- **Grade:** N/A
- **Status:** ⚠️ Missing coverage
- **Recommendation:** Add to T33.G6.10 or new foundation skill
- **Purpose:** Returns collection reference for queries

#### Block: `field [FIELDNAME]`
- **Block ID:** database_collectionfield (reporter)
- **Skill:** Mentioned in T33.G7.10 but not dedicated skill
- **Grade:** 7
- **Status:** ⚠️ Needs explicit coverage
- **Recommendation:** Add T33.G7.09b for field references
- **Purpose:** References field names in WHERE conditions and updates

---

### Condition Building Blocks (4 blocks)

#### Block: `<cond (field/value) [COMPARATOR] (field/value)>`
- **Block ID:** database_cond (boolean)
- **Skill:** T33.G7.10 (Query with WHERE conditions)
- **Grade:** 7
- **Status:** ⚠️ Too broad
- **Recommendation:** Split into T33.G7.10a (basic comparisons)
- **Comparators:** >, <, =, ≠, ≥, ≤
- **Use:** In WHERE conditions for fetch, update, delete

#### Block: `<cond (field [FIELDNAME]) contains [TEXT]?>`
- **Block ID:** database_contains (boolean)
- **Skill:** T33.G7.10 (Query with WHERE conditions)
- **Grade:** 7
- **Status:** ⚠️ Too broad
- **Recommendation:** Split into T33.G7.10b (contains operator)
- **Use:** Text search within field values

#### Block: `<cond not <>>`
- **Block ID:** database_not (boolean)
- **Skill:** T33.G7.12 (Complex queries with logic)
- **Grade:** 7
- **Status:** ⚠️ Too broad
- **Recommendation:** Split into T33.G7.12b (NOT operator)

#### Block: `<cond <> and <>>`
- **Block ID:** database_and (boolean)
- **Skill:** T33.G7.12 (Complex queries with logic)
- **Grade:** 7
- **Status:** ⚠️ Too broad
- **Recommendation:** Split into T33.G7.12a (AND/OR logic)

#### Block: `<cond <> or <>>`
- **Block ID:** database_or (boolean)
- **Skill:** T33.G7.12 (Complex queries with logic)
- **Grade:** 7
- **Status:** ⚠️ Too broad
- **Recommendation:** Split into T33.G7.12a (AND/OR logic)

---

## Category: Variables (Cloud Sessions) (2 blocks)

### Cloud Variable Synchronization

#### Block: `create cloud session [SESSION]`
- **Block ID:** data_createcloudsession
- **Skill:** T33.G7.05 (Synchronize variables using cloud sessions)
- **Grade:** 7
- **Status:** ⚠️ Too broad
- **Recommendation:** Split into T33.G7.05b (create/join)
- **Purpose:** Creates new session for variable sync
- **Note:** Only cloud variables sync, not sprites/physics

#### Block: `join cloud session [SESSION]`
- **Block ID:** data_joincloudsession
- **Skill:** T33.G7.05 (Synchronize variables using cloud sessions)
- **Grade:** 7
- **Status:** ⚠️ Too broad
- **Recommendation:** Split into T33.G7.05b (create/join)
- **Purpose:** Connects to existing session
- **Isolation:** Only members of same session share variables

---

## Block Coverage Summary

### By Category:
- **Cloud blocks:** 15 blocks → 100% covered
- **Database blocks:** 11 blocks → ~90% covered (field/collection helpers need explicit skills)
- **Cloud session blocks:** 2 blocks → 100% covered
- **Total:** 28 blocks → 96% covered

### By Grade:
- **Grade 6:** 7 blocks covered by 5 skills
- **Grade 7:** 18 blocks covered by 12 skills (many too broad)
- **Grade 8:** 4 blocks covered by 1 skill

### Issues Identified:
1. **13 blocks** in skills that are too broad and need splitting
2. **2 blocks** (field, collection helpers) need explicit dedicated skills
3. **4 blocks** in skills with dependency violations
4. **Many blocks** combined in single skills, reducing scaffolding

---

## Detailed Block-to-Skill Mapping Table

| Block ID | Block Type | Current Skill(s) | Grade | Issues | Recommended Fix |
|----------|-----------|------------------|-------|--------|-----------------|
| p2p_fetchfromurl | Stack | T33.G6.02 | 6 | None | ✅ Keep as-is |
| p2p_readfromgooglesheet | Stack | T33.G6.03 | 6 | None | ✅ Keep as-is |
| p2p_writeintogooglesheet | Stack | T33.G6.04 | 6 | None | ✅ Keep as-is |
| p2p_clearsheet | Stack | T33.G6.05 | 6 | None | ✅ Keep as-is |
| p2p_listSheetsInGoogleSheet | Stack | T33.G7.01 | 7 | Broad | Split to G7.01a |
| p2p_addsheet | Stack | T33.G7.01 | 7 | Broad | Split to G7.01b |
| p2p_removesheet | Stack | T33.G7.01 | 7 | Broad | Split to G7.01c |
| p2p_getvalue | Reporter | T33.G7.02 | 7 | None | ✅ Keep paired |
| p2p_setvalue | Stack | T33.G7.02 | 7 | None | ✅ Keep paired |
| p2p_appendrow | Stack | T33.G7.03 | 7 | None | ✅ Keep as-is |
| p2p_insertrowsinsheet | Stack | T33.G8.01 | 8 | Broad | Maybe split |
| p2p_removerowsfromsheet | Stack | T33.G8.01 | 8 | Broad | Maybe split |
| p2p_insertcolumnsinsheet | Stack | T33.G8.01 | 8 | Broad | Maybe split |
| p2p_removecolumnsfromsheet | Stack | T33.G8.01 | 8 | Broad | Maybe split |
| p2p_getgooglefoldercontent | Stack | T33.G7.04 | 7 | Dep viol | Fix deps |
| database_insert_from_table | Stack | T33.G6.10 | 6 | Dep viol | Fix deps |
| database_find_from_collection | Stack | T33.G6.10, G7.10, G7.12 | 6,7,7 | Very broad | Split into 4-5 skills |
| database_update_collection | Stack | T33.G7.11 | 7 | Broad | Split to G7.11a |
| database_update_collection_in_place | Stack | T33.G7.11 | 7 | Broad | Split to G7.11b |
| database_remove_all_document | Stack | T33.G7.11 | 7 | Broad | Split to G7.11c |
| database_collection | Reporter | Not explicit | N/A | Missing | Add to G6.10 |
| database_collectionfield | Reporter | T33.G7.10 (implicit) | 7 | No dedicated skill | Add G7.09b |
| database_cond | Boolean | T33.G7.10 | 7 | Broad | Split to G7.10a |
| database_contains | Boolean | T33.G7.10 | 7 | Broad | Split to G7.10b |
| database_not | Boolean | T33.G7.12 | 7 | Broad | Split to G7.12b |
| database_and | Boolean | T33.G7.12 | 7 | Broad | Split to G7.12a |
| database_or | Boolean | T33.G7.12 | 7 | Broad | Split to G7.12a |
| data_createcloudsession | Stack | T33.G7.05 | 7 | Broad | Split to G7.05b |
| data_joincloudsession | Stack | T33.G7.05 | 7 | Broad | Split to G7.05b |

---

## Skills Without Corresponding Blocks

These T33 skills are conceptual or apply to multiple blocks:

1. **T33.GK.01 through T33.G5.03** - Conceptual foundation (no blocks)
2. **T33.G6.01** - Survey of all Cloud blocks (meta-skill)
3. **T33.G6.06** - Error handling (applies to all service blocks)
4. **T33.G6.07** - Rate limiting (applies to all service blocks)
5. **T33.G6.08** - Privacy principles (conceptual)
6. **T33.G6.09** - Compare collections vs Sheets (conceptual)
7. **T33.G7.06** - Service authorization (conceptual)
8. **T33.G7.07** - Multi-service workflows (combines multiple blocks)
9. **T33.G7.08** - Compare service options (decision-making)
10. **T33.G7.09** - Caching pattern (pattern, not specific block)
11. **T33.G8.02** - Terms of service (conceptual)
12. **T33.G8.03** - Simulate outages (testing pattern)
13. **T33.G8.04** - Validate data (pattern across blocks)
14. **T33.G8.05** - Compare implementations (analysis)
15. **T33.G8.06** - Data pipeline (capstone combining blocks)

**Total conceptual skills:** 15 out of 36 (42%)
**Total hands-on block skills:** 21 out of 36 (58%)

---

## Blocks Not in Cloud/Database Categories (Related)

These blocks in other categories also connect to external services:

### AI Category (Referenced in T33.G6.01 note):
- Various ChatGPT/GPT-4 blocks
- DALL-E image generation
- Speech recognition
- Text-to-speech
- Semantic database search

**Note:** These are covered in Topic T32 (AI), not T33

### Multiplayer Category (Referenced in T33.G7.05 note):
- Host game, join game
- Sync sprite properties
- Multiplayer physics

**Note:** These are covered in Topic T19 (Multiplayer), not T33

This separation is GOOD - keeps T33 focused on data/cloud services, not AI or real-time gaming.

---

## Recommended Block Introduction Order

### Grade 6 (Foundation - Read-only emphasis):
1. **Survey all Cloud blocks** (T33.G6.01)
2. **Fetch URL** - simplest, read-only (T33.G6.02)
3. **Read from Sheets** - structured data input (T33.G6.03)
4. **Write to Sheets** - structured data output (T33.G6.04)
5. **Clear Sheet** - data management (T33.G6.05)
6. **Check success** - error detection (T33.G6.05b - NEW)
7. **Handle errors** - error display (T33.G6.06a - SPLIT)
8. **Compare collections vs Sheets** - conceptual (T33.G6.09)
9. **Identify collection blocks** - survey (T33.G6.09b - NEW)
10. **Insert/fetch collections** - basic CRUD (T33.G6.10)

### Grade 7 (Development - Write emphasis):
1. **List sheets** (T33.G7.01a - SPLIT)
2. **Add sheets** (T33.G7.01b - SPLIT)
3. **Remove sheets** (T33.G7.01c - SPLIT)
4. **Get/set cell values** (T33.G7.02)
5. **Append rows** (T33.G7.03)
6. **Google Drive folders** (T33.G7.04)
7. **Cloud session concepts** (T33.G7.05a - SPLIT)
8. **Create/join sessions** (T33.G7.05b - SPLIT)
9. **Simple WHERE queries** (T33.G7.10a - SPLIT)
10. **Contains operator** (T33.G7.10b - SPLIT)
11. **Update from table** (T33.G7.11a - SPLIT)
12. **Update in-place** (T33.G7.11b - SPLIT)
13. **Delete documents** (T33.G7.11c - SPLIT)
14. **AND/OR logic** (T33.G7.12a - SPLIT)
15. **NOT operator** (T33.G7.12b - SPLIT)

### Grade 8 (Mastery - Integration emphasis):
1. **LIMIT/SORT queries** (T33.G7.12c - SPLIT)
2. **Insert/remove rows** (T33.G8.01)
3. **Simulate outages** (T33.G8.03)
4. **Validate data** (T33.G8.04)
5. **Compare implementations** (T33.G8.05)
6. **Build data pipeline** (T33.G8.06)

---

## Block Complexity Analysis

### Simple Blocks (Good for G6):
- fetch URL (1 input)
- read from Sheets (4 inputs, structured)
- write to Sheets (4 inputs, structured)
- clear sheet (2 inputs)
- get cell value (4 inputs)
- set cell value (5 inputs)

### Moderate Blocks (Good for G7):
- list sheets (2 inputs, list output)
- add sheet (2 inputs)
- remove sheet (2 inputs)
- append row (4 inputs)
- insert into collection (4 inputs)
- basic fetch from collection (3 inputs minimum)
- update collection from table (2 inputs)

### Complex Blocks (Good for late G7/G8):
- fetch with WHERE (5+ inputs with nested conditions)
- update in-place (variable inputs)
- remove documents (3+ inputs with conditions)
- insert/remove rows/columns (4 inputs each)
- list Drive folder (2 inputs, complex output)

### Advanced Patterns (G8):
- fetch with AND/OR/NOT logic
- fetch with LIMIT and multi-field SORT
- Combining multiple blocks in workflows
- Error handling across service calls

---

**END OF BLOCK COVERAGE MAP**
