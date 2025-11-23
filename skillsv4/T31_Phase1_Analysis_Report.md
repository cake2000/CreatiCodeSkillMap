# T31 (Internet & Cloud) - Phase 1 Analysis Report

**Date:** 2025-11-23
**Analyst:** Claude (Sonnet 4.5)
**Scope:** Complete analysis of T31 skills against CreatiCode's actual Internet/Cloud blocks

---

## Executive Summary

**Total Current Skills:** 37 (K-8)
**Total CreatiCode Blocks Found:** 40 blocks across 3 categories

**Key Findings:**
1. **CRITICAL GAPS:** 6 advanced Google Sheets operations missing from curriculum
2. **MISSING FEATURE:** Google Drive folder listing not covered
3. **MISSING FEATURE:** Multiplayer game reset not covered
4. **MISSING FEATURE:** Multiplayer list players not covered
5. **DATABASE INACCURACY:** Current skills incorrectly describe how database insert works
6. **GOOD COVERAGE:** Most core features are well represented

---

## Part 1: Complete CreatiCode Block Inventory

### A. Cloud Category (15 blocks)

#### 1. Web Page Fetching
- **Block ID:** `p2p_fetchfromurl`
- **Syntax:** `fetch web page as [FORMAT] from URL [URL]`
- **Description:** Fetch content of web page as markdown
- **Covered by:** T31.G5.03 ✓

#### 2-14. Google Sheets Operations

**Basic Read/Write:**
- **Block ID:** `p2p_readfromgooglesheet`
- **Syntax:** `read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]`
- **Covered by:** T31.G6.02 (partial - only mentions "cell" not "range") ⚠️

- **Block ID:** `p2p_writeintogooglesheet`
- **Syntax:** `write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]`
- **Covered by:** T31.G6.03 (partial - describes as "cell" not table-based) ⚠️

**Single Cell Operations:**
- **Block ID:** `p2p_getvalue`
- **Syntax:** `value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
- **Covered by:** T31.G6.02 ✓

- **Block ID:** `p2p_setvalue`
- **Syntax:** `set value to [VALUE] at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
- **Covered by:** T31.G6.03 ✓

**Row Operations:**
- **Block ID:** `p2p_appendrow`
- **Syntax:** `append row [ROWNUMBER] from table [TABLENAME v] to sheet [SHEETNAME] in Google Sheet at URL [URL]`
- **Covered by:** T31.G6.03.01 ✓

- **Block ID:** `p2p_removerowsfromsheet`
- **Syntax:** `remove rows [FROMR] to [TOR] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
- **Covered by:** ❌ MISSING

- **Block ID:** `p2p_insertrowsinsheet`
- **Syntax:** `insert [COUNT] rows at row [STARTR] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
- **Covered by:** ❌ MISSING

**Column Operations:**
- **Block ID:** `p2p_removecolumnsfromsheet`
- **Syntax:** `remove columns [FROMC] to [TOC] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
- **Covered by:** ❌ MISSING

- **Block ID:** `p2p_insertcolumnsinsheet`
- **Syntax:** `insert [COUNT] columns at column [STARTC] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
- **Covered by:** ❌ MISSING

**Sheet Management:**
- **Block ID:** `p2p_listSheetsInGoogleSheet`
- **Syntax:** `list all sheets in google sheet at URL [SHEET_URL] into list [LIST]`
- **Covered by:** T31.G6.03.02 (partial - mentions listing sheets) ✓

- **Block ID:** `p2p_addsheet`
- **Syntax:** `add sheet [SHEETNAME] to google sheet at URL [URL]`
- **Covered by:** T31.G6.03.02 ✓

- **Block ID:** `p2p_removesheet`
- **Syntax:** `remove sheet [SHEETNAME] from google sheet at URL [URL]`
- **Covered by:** T31.G6.03.02 (implied by "manage") ✓

- **Block ID:** `p2p_clearsheet`
- **Syntax:** `clear sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
- **Covered by:** ❌ MISSING

#### 15. Google Drive
- **Block ID:** `p2p_getgooglefoldercontent`
- **Syntax:** `list content of Google Drive folder [URL] in table [TABLENAME v]`
- **Description:** List files and subfolders with filename, fileid, mimetype, url
- **Covered by:** ❌ MISSING

---

### B. Multiplayer Category (13 blocks)

#### Game Session Management

- **Block ID:** `mp_createmultiplayergame`
- **Syntax:** `create game named [GAMENAME] password [PASSWORD] my name [HOSTNAME] role [ROLE] server [LOCATION v] capacity (CAPACITY) world width (W) height (H)`
- **Covered by:** T31.G5.04 ✓

- **Block ID:** `mp_joinmultiplayergame`
- **Syntax:** `join multiplayer game named [GAMENAME] by host [HOSTNAME] from server [LOCATION v] with password [PASSWORD] my name [DISPLAYNAME] role [ROLE]`
- **Covered by:** T31.G5.04 ✓

- **Block ID:** `mp_listmultiplayergames`
- **Syntax:** `list multiplayer games in server [LOCATION v] in table [TABLE v]`
- **Description:** Lists games with Host Name, Game Name, User Count
- **Covered by:** ❌ MISSING (implied but not explicitly taught)

- **Block ID:** `mp_listmultiplayergameusers`
- **Syntax:** `list players in game [GAMENAME] hosted by [HOSTNAME] from server [LOCATION v] in table [TABLE v]`
- **Description:** Lists players with Player Name and Role
- **Covered by:** ❌ MISSING

- **Block ID:** `mp_resetmultiplayergame`
- **Syntax:** `reset game world`
- **Description:** Clean up all objects so game can be restarted
- **Covered by:** ❌ MISSING

#### Connection Status

- **Block ID:** `mp_isconnectedtogame`
- **Syntax:** `connected to game`
- **Description:** Boolean indicating connection status
- **Covered by:** T31.G5.05 ✓

#### Sprite Management

- **Block ID:** `mp_addspritetogame`
- **Syntax:** `add this sprite to game as a [MODE v] [SHAPE v]`
- **Description:** MODE: Dynamic/Static, SHAPE: Rectangle/Circle
- **Covered by:** T31.G6.06 ✓

- **Block ID:** `mp_whenaddedtogame`
- **Syntax:** `when added to game`
- **Description:** Event triggered when sprite is registered
- **Covered by:** T31.G6.06 (implied) ✓

- **Block ID:** `mp_removespritefromgame`
- **Syntax:** `remove this sprite from game`
- **Covered by:** T31.G6.06 (implied by lifecycle) ⚠️

#### Movement Synchronization

- **Block ID:** `mp_setsyncmovement`
- **Syntax:** `synchronously set speed x (X) y (Y)`
- **Covered by:** T31.G7.02 ✓

- **Block ID:** `mp_setsyncmovement2`
- **Syntax:** `synchronously set speed (SPEED) dir (DIR)`
- **Covered by:** T31.G7.02 ✓

#### Messaging

- **Block ID:** `mp_broadcastmessagetoall`
- **Syntax:** `broadcast [MESSAGE v] with parameter [PARAMETER] mode [MODE v]`
- **Description:** MODE: All Sprites / Exclude Replicate
- **Covered by:** T31.G7.02.01 ✓

- **Block ID:** `mp_broadcasttouchmessage`
- **Syntax:** `when touching [SPRITENAME v] will [STOPTYPE v] and trigger [MESSAGE v] with parameter [PARAMETER]`
- **Description:** STOPTYPE: stop / stop and delete / continue / continue and delete
- **Covered by:** T31.G7.02.02 ✓

---

### C. Database Category (13 blocks)

#### Data Insertion

- **Block ID:** `database_insert_from_table`
- **Syntax:** `insert from table [TABLENAME v] row from (STARTROW) to (ENDROW) into collection [COLLECTIONNAME v]`
- **Description:** Insert rows from table into collection (table is intermediate storage)
- **Covered by:** T31.G7.02.03 but INCORRECTLY described ⚠️

#### Data Retrieval

- **Block ID:** `database_find_from_collection`
- **Syntax:** `fetch from collection [COLLECTIONNAME v] into table [TABLENAME v] where <CONDITION> limit (LIMIT) sort by (SORTFIELD1) [SORTORDER1 v] (SORTFIELD2) [SORTORDER2 v]`
- **Description:** Fetch data with conditions, limits, sorting
- **Covered by:** T31.G7.02.04 ✓

#### Collection Information

- **Block ID:** `database_collection`
- **Syntax:** `collection [COLLECTIONNAME]`
- **Description:** Returns collection definition (field names and types)
- **Covered by:** ❌ MISSING (not explicitly taught)

#### Data Updates

- **Block ID:** `database_update_collection`
- **Syntax:** `update collection [COLLECTIONNAME v] from table [TABLENAME v]`
- **Description:** Update collection rows using table with preserved 'id' property
- **Covered by:** T31.G7.02.05 (partial) ✓

- **Block ID:** `database_update_collection_in_place`
- **Syntax:** `update collection [COLLECTIONNAME v] in-place where <CONDITION> set (FIELD1) to (VALUE1) set (FIELD2) to (VALUE2) set (FIELD3) to (VALUE3) set (FIELD4) to (VALUE4)`
- **Description:** Update up to 4 fields in rows matching condition
- **Covered by:** T31.G7.02.05 ✓

#### Data Deletion

- **Block ID:** `database_remove_all_document`
- **Syntax:** `remove all documents from collection [COLLECTIONNAME v] where <CONDITION>`
- **Description:** Remove all rows matching condition (empty condition removes all)
- **Covered by:** T31.G7.02.05 ✓

#### Query Condition Blocks

- **Block ID:** `database_query`
- **Syntax:** `<cond [INPUT1] [COMPARATOR v] [INPUT2]>`
- **Description:** Boolean comparator (>, <, =, ≠, ≥, ≤)
- **Covered by:** T31.G7.02.04 (implied) ✓

- **Block ID:** `database_contains`
- **Syntax:** `<cond (field [FIELDNAME]) contains [TEXT]?>`
- **Description:** Check if field contains text
- **Covered by:** T31.G7.02.04 (implied) ⚠️

- **Block ID:** `database_not`
- **Syntax:** `<cond not <>>`
- **Description:** Boolean NOT operator
- **Covered by:** T31.G7.02.04 (implied) ⚠️

- **Block ID:** `database_and`
- **Syntax:** `<cond <> and <>>`
- **Description:** Boolean AND operator
- **Covered by:** T31.G7.02.04 (implied) ⚠️

- **Block ID:** `database_or`
- **Syntax:** `<cond <> or <>>`
- **Description:** Boolean OR operator
- **Covered by:** T31.G7.02.04 (implied) ⚠️

- **Block ID:** `database_collectionfield`
- **Syntax:** `field [FIELDNAME]`
- **Description:** Reference to collection field
- **Covered by:** T31.G7.02.04 (implied) ✓

- **Block ID:** `database_operator`
- **Syntax:** `op [INPUT1] [OPERATOR v] [INPUT2]`
- **Description:** Arithmetic operators (inc/+, dec/-, mul/*, div//)
- **Covered by:** T31.G7.02.04 (implied) ⚠️

---

## Part 2: Gap Analysis

### CRITICAL GAPS - Missing Features

#### Gap 1: Advanced Google Sheets Row/Column Operations
**Missing Blocks:**
1. `p2p_insertrowsinsheet` - Insert multiple rows
2. `p2p_removerowsfromsheet` - Remove row ranges
3. `p2p_insertcolumnsinsheet` - Insert multiple columns
4. `p2p_removecolumnsfromsheet` - Remove column ranges
5. `p2p_clearsheet` - Clear entire sheet

**Impact:** Students can't fully manage spreadsheet structure programmatically
**Recommendation:** Add skill at G6-G7 level covering sheet structure manipulation

#### Gap 2: Google Drive Integration
**Missing Block:** `p2p_getgooglefoldercontent`
**Impact:** Students unaware of Google Drive integration capability
**Recommendation:** Add skill at G7-G8 level for listing and working with Drive files

#### Gap 3: Multiplayer Game Discovery
**Missing Block:** `mp_listmultiplayergames`
**Impact:** Students can't discover available games to join
**Recommendation:** Add to G5-G6 level alongside game joining

#### Gap 4: Multiplayer Player Roster
**Missing Block:** `mp_listmultiplayergameusers`
**Impact:** Students can't see who's in the game
**Recommendation:** Add to G6 level for game management

#### Gap 5: Multiplayer Game Reset
**Missing Block:** `mp_resetmultiplayergame`
**Impact:** Students can't restart multiplayer games properly
**Recommendation:** Add to G6-G7 level

#### Gap 6: Database Query Operators Detail
**Missing Explicit Coverage:**
- `database_contains` - Text search
- `database_not` / `database_and` / `database_or` - Boolean logic
- `database_operator` - Arithmetic in queries

**Impact:** Students may not know full query capabilities
**Recommendation:** Expand T31.G7.02.04 to explicitly mention these operators

---

### ACCURACY ISSUES

#### Issue 1: Database Insert Description (CRITICAL)
**Skill:** T31.G7.02.03
**Current Description:** "Students use CreatiCode's Database blocks to insert documents into a cloud-based collection"
**Actual Behavior:** Students must FIRST add data to a TABLE, then insert rows from the table into the collection. Direct insertion is not supported.

**Fix Required:**
```
Skill: Insert data into a database collection via tables
Description: Students use CreatiCode's Database blocks to prepare data in a table,
then insert specific rows from the table into a cloud-based collection. They learn
why the table serves as intermediate storage (easy to prepare and review before insertion).
```

#### Issue 2: Google Sheets Cell vs Range Operations
**Skills:** T31.G6.02, T31.G6.03
**Current:** Describes as "read/write cell"
**Actual:** Blocks support both single-cell operations AND range/table operations

**Fix Required:**
- T31.G6.02 should mention BOTH `p2p_getvalue` (single cell) AND `p2p_readfromgooglesheet` (range into table)
- T31.G6.03 should mention BOTH `p2p_setvalue` (single cell) AND `p2p_writeintogooglesheet` (table into range)

#### Issue 3: Remove Sprite from Game
**Skill:** T31.G6.06
**Current:** Only mentions adding sprites
**Missing:** `mp_removespritefromgame` block should be explicitly mentioned

---

## Part 3: Progression Analysis

### Kindergarten (K) - 1 skill ✓
- T31.GK.01: Device recognition (picture-based)
**Assessment:** Appropriate, no blocks needed

### Grade 1 - 1 skill ✓
- T31.G1.01: Connection status indicators (picture-based)
**Assessment:** Appropriate, no blocks needed

### Grade 2 - 2 skills ✓
- T31.G2.01: Internet connection concepts (picture-based)
- T31.G2.02: Online safety (picture-based)
**Assessment:** Appropriate, no blocks needed

### Grade 3 - 2 skills ✓
- T31.G3.01: Device to website path tracing
- T31.G3.02: Types of information sharing
**Assessment:** Appropriate conceptual foundation

### Grade 4 - 2 skills ✓
- T31.G4.01: Data packets concept
- T31.G4.02: Secure vs insecure websites
**Assessment:** Good security foundation

### Grade 5 - 5 skills
- T31.G5.01: Trace device to service ✓
- T31.G5.02: Internet vs offline apps ✓
- T31.G5.03: Fetch web page as markdown ✓
- T31.G5.04: Create/join multiplayer game ✓
- T31.G5.05: Check connection status ✓

**Issues:**
- Missing: List available games (should come before/with joining)

### Grade 6 - 6 skills
- T31.G6.01: HTTP/HTTPS request steps ✓
- T31.G6.02: Read Google Sheet cell ⚠️ (needs range mention)
- T31.G6.03: Write Google Sheet cell ⚠️ (needs range mention)
- T31.G6.03.01: Update entire rows ✓
- T31.G6.03.02: List/manage sheets ✓
- T31.G6.04: Latency analysis for AI ✓
- T31.G6.05: Privacy for AI data ✓
- T31.G6.06: Add sprites to multiplayer ⚠️ (needs remove sprite)

**Issues:**
- Missing: List players in game
- Missing: Clear sheet operation
- Need to mention both cell AND range operations

### Grade 7 - 9 skills
- T31.G7.01: Distributed server model ✓
- T31.G7.02: Sync sprite movement ✓
- T31.G7.02.01: Broadcast messages ✓
- T31.G7.02.02: Handle collisions ✓
- T31.G7.02.03: Insert database data ❌ INCORRECT
- T31.G7.02.04: Fetch database data ⚠️ (needs operator detail)
- T31.G7.02.05: Update/remove database ✓
- T31.G7.03: Network topologies ✓
- T31.G7.04: Client-server vs P2P ✓
- T31.G7.05: Societal impacts ✓

**Issues:**
- CRITICAL: T31.G7.02.03 incorrectly describes database insert
- Missing: Database query operators (contains, not, and, or, arithmetic)
- Missing: Reset multiplayer game
- Missing: Advanced Google Sheets operations (insert/remove rows/columns)

### Grade 8 - 6 skills
- T31.G8.01: Edge vs cloud processing ✓
- T31.G8.02: AI service network requirements ✓
- T31.G8.03: Secure AI cloud systems ✓
- T31.G8.04: Privacy protection for AI ✓
- T31.G8.05: AI service resilience ✓
- T31.G8.06: AI monitoring dashboards ✓

**Issues:**
- Missing: Google Drive integration (good fit for G8)

---

## Part 4: Specific Recommendations

### Immediate Fixes (Required)

#### Fix 1: Correct Database Insert (T31.G7.02.03)
**OLD:**
```
Skill: Insert data into a database collection
Description: Students use CreatiCode's Database blocks to insert documents into
a cloud-based collection, storing persistent data like player progress, game
settings, or user-generated content.
```

**NEW:**
```
Skill: Insert data into database collections via tables
Description: Students use CreatiCode's Database blocks to prepare data in a
table, then insert rows from the table into a cloud-based collection. They
learn that the table serves as intermediate storage, making it easy to prepare
and review data before insertion. They can insert specific row ranges from the
table into the collection.
```

#### Fix 2: Expand Google Sheets Skills (T31.G6.02, T31.G6.03)

**T31.G6.02 - NEW:**
```
Skill: Read data from Google Sheets
Description: Students use CreatiCode's Google Sheets integration to read data
from a shared spreadsheet in two ways: (1) reading a single cell value using
row/column coordinates, or (2) reading an entire range of cells into a table
for batch processing. This introduces cloud-based data sharing.
```

**T31.G6.03 - NEW:**
```
Skill: Write data to Google Sheets
Description: Students use CreatiCode's Google Sheets blocks to write data to
a shared spreadsheet in two ways: (1) setting a single cell value using
row/column coordinates, or (2) writing an entire table to a range starting
at a specified cell. They create persistent leaderboards that update in real-time.
```

#### Fix 3: Expand Database Query Operators (T31.G7.02.04)

**NEW:**
```
Skill: Fetch data from a database with complex queries
Description: Students use CreatiCode's Database blocks to fetch documents from
a collection using query conditions including: comparison operators (>, <, =, ≠, ≥, ≤),
text search (contains), boolean logic (and, or, not), and arithmetic operators
(+, -, *, /). They apply limits, sorting by multiple fields, and retrieve data
into tables for display.
```

### New Skills to Add

#### New Skill 1: List Available Multiplayer Games
**Placement:** After T31.G5.04 → **T31.G5.04.01**
```
ID: T31.G5.04.01
Topic: T31 – Internet & Cloud: Grade 5–8 Skill List
Skill: List available multiplayer games on a server
Description: Students use CreatiCode's multiplayer blocks to list all games
running on a specific server, showing host name, game name, and player count.
This helps them discover games to join.
CSTA: MS-SAS-NW-06

Dependencies:
* T31.G5.04: Create and join a multiplayer game session
```

#### New Skill 2: Multiplayer Player Roster
**Placement:** After T31.G6.06 → **T31.G6.06.01**
```
ID: T31.G6.06.01
Topic: T31 – Internet & Cloud: Grade 5–8 Skill List
Skill: List players in a multiplayer game
Description: Students use CreatiCode's multiplayer blocks to fetch and display
the list of all players currently in a game, showing their display names and
roles. This enables creating lobby screens and team rosters.
CSTA: MS-SAS-NW-06

Dependencies:
* T31.G6.06: Add sprites to multiplayer game world
```

#### New Skill 3: Manage Sprite Lifecycle in Multiplayer
**Placement:** Replace T31.G6.06 with expanded version
```
ID: T31.G6.06
Topic: T31 – Internet & Cloud: Grade 5–8 Skill List
Skill: Manage sprite lifecycle in multiplayer games
Description: Students use CreatiCode's multiplayer blocks to add sprites to
the shared game world as dynamic or static objects with rectangle or circle
colliders. They handle the "when added to game" event and remove sprites when
needed. They understand how sprites are synchronized across all players.
CSTA: MS-SAS-NW-06

Dependencies:
* T31.G5.04: Create and join a multiplayer game session
* T31.G5.05: Check multiplayer connection status
```

#### New Skill 4: Reset Multiplayer Games
**Placement:** After T31.G7.02.02 → **T31.G7.02.02.01**
```
ID: T31.G7.02.02.01
Topic: T31 – Internet & Cloud: Grade 5–8 Skill List
Skill: Reset multiplayer game sessions
Description: Students use CreatiCode's multiplayer reset block to clean up
all objects in the game world so the game can be restarted. They understand
when and why game resets are needed (between rounds, after game over).
CSTA: MS-SAS-NW-06

Dependencies:
* T31.G7.02.02: Handle sprite collisions in multiplayer games
```

#### New Skill 5: Advanced Google Sheets Structure Management
**Placement:** After T31.G6.03.02 → **T31.G6.03.03**
```
ID: T31.G6.03.03
Topic: T31 – Internet & Cloud: Grade 5–8 Skill List
Skill: Modify Google Sheets structure programmatically
Description: Students use CreatiCode's Google Sheets blocks to modify sheet
structure: inserting and removing rows and columns, and clearing entire sheets.
They apply these operations to dynamically manage spreadsheet layouts for
different game phases or data reorganization.
CSTA: MS-SAS-NW-06

Dependencies:
* T31.G6.03.02: List and manage multiple Google Sheets
```

#### New Skill 6: Google Drive Integration
**Placement:** After T31.G8.04 → **T31.G8.04.01**
```
ID: T31.G8.04.01
Topic: T31 – Internet & Cloud: Grade 5–8 Skill List
Skill: Access Google Drive folders programmatically
Description: Students use CreatiCode's Google Drive blocks to list files and
subfolders in shared Google Drive folders, retrieving file names, IDs, types,
and URLs. They apply this to create file browsers, asset libraries, or
data catalogs for their projects.
CSTA: MS-SAS-NW-06

Dependencies:
* T31.G6.02: Read data from Google Sheets
* T31.G8.04: Implement privacy protection for AI data
```

---

## Part 5: Summary Statistics

### Block Coverage Summary
- **Total Blocks:** 40
- **Well Covered:** 22 (55%)
- **Partially Covered:** 9 (23%)
- **Not Covered:** 9 (22%)

### Coverage by Category
| Category | Total Blocks | Well Covered | Partial | Missing |
|----------|-------------|--------------|---------|---------|
| Cloud | 15 | 7 | 2 | 6 |
| Multiplayer | 13 | 9 | 1 | 3 |
| Database | 13 | 6 | 6 | 1 |

### Critical Issues
1. **Database insert:** Incorrectly described (must use table intermediate)
2. **Google Sheets:** Missing 5 structure manipulation blocks
3. **Multiplayer:** Missing game discovery and management features
4. **Google Drive:** Completely missing

### Skill Distribution
- **K-2:** 4 skills (conceptual, picture-based) ✓
- **G3-4:** 4 skills (foundational concepts) ✓
- **G5:** 5 skills (first coding blocks) ✓
- **G6:** 8 skills (expanding features)
- **G7:** 9 skills (advanced integration)
- **G8:** 6 skills (AI integration focus) ✓

**Total:** 37 current skills → **Recommended:** 44 skills (+7)

---

## Part 6: Action Items

### Priority 1: Immediate Corrections (Critical)
1. Fix T31.G7.02.03 database insert description
2. Expand T31.G6.02 to cover both cell and range reading
3. Expand T31.G6.03 to cover both cell and range writing
4. Expand T31.G7.02.04 to list query operators explicitly
5. Expand T31.G6.06 to include removing sprites

### Priority 2: Add Missing Core Features (High)
6. Add T31.G5.04.01: List multiplayer games
7. Add T31.G6.06.01: List players in game
8. Add T31.G7.02.02.01: Reset multiplayer game

### Priority 3: Add Advanced Features (Medium)
9. Add T31.G6.03.03: Advanced Google Sheets structure
10. Add T31.G8.04.01: Google Drive integration

### Priority 4: Documentation Improvements (Low)
11. Note database collection definition block in reference materials
12. Create comprehensive operator reference for database queries

---

## Conclusion

The T31 curriculum has **strong conceptual coverage** (K-4) and **good core block coverage** (G5-6), but has **critical accuracy issues** in database operations and **significant gaps** in advanced Google Sheets and multiplayer management features.

**Most Critical Fix:** Database insert mechanism must be corrected immediately as current description is fundamentally wrong about how the feature works.

**Biggest Gaps:** Google Sheets structure manipulation (5 blocks) and multiplayer game discovery/management (3 blocks) represent significant missing functionality that students should learn.

**Overall Assessment:** 7/10 - Good foundation but needs corrections and expansions for completeness.
