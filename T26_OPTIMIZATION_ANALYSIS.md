# T26 (Data Collection & Logging) - Comprehensive Optimization Analysis

## Executive Summary

This analysis compares the current T26 skills (40 total across K-8) against CreatiCode's actual data collection and logging features to identify critical gaps, misalignments, and optimization needs.

**CRITICAL FINDING:** T26 is missing coverage for **10 major CreatiCode features** including:
- Cloud storage (save/load data by name)
- Database collections (MongoDB-style operations)
- Player score recording & leaderboards
- Semantic database (embedding-based search)
- Sensor data collection to tables (face, body, hand, pose)
- Console logging with print blocks
- Google Sheets integration (partially mentioned, needs expansion)
- Multiplayer game data storage
- File export/import (CSV mentioned in G5.04, but variable export missing)

---

## Part 1: CRITICAL GAPS - Missing CreatiCode-Specific Features

### Gap 1: Cloud Storage (Save/Load Data by Name) - NOT COVERED

**CreatiCode Blocks:**
- `save table [TABLE v] to server as [DATANAME]` - Save entire table to CreatiCode server
- `load [DATANAME] from server into table [TABLE v]` - Load table from server
- `save variable to server as [NAME]` (implied from variable export)
- `load variable from server` (implied)

**Current T26 Coverage:**
- G5.04 mentions "Store logs in CreatiCode tables for export" but focuses on CSV export, NOT cloud save/load
- NO skills teaching students to persist data to the cloud
- NO skills teaching students to load previously saved data

**Impact:** HIGH - This is a fundamental cloud feature that enables:
- Saving game progress
- Storing user preferences
- Sharing data between sessions
- Collaborative data projects

**Recommended Action:**
```
NEW SKILL:
ID: T26.G5.05
Title: Save and load table data from cloud storage
Description: Students save a table to the CreatiCode server with a name, then load it back in a new session, enabling data persistence across project runs.
Dependencies:
* T10.G5.01: Create and populate a table variable
* T10.G5.03: Update or insert rows in a table
* T26.G5.04: Store logs in CreatiCode tables for export
Challenge: Create a survey that saves responses to cloud, then load and display the saved data when the project restarts.
CreatiCode Blocks: `save table [] to server as []`, `load [] from server into table []`
```

### Gap 2: Database Collections (MongoDB-Style) - NOT COVERED

**CreatiCode Blocks:**
- `insert from table [TABLE v] rows [START] to [END] into collection [COLLECTION]` - Insert rows into database
- `fetch from collection [COLLECTION] condition [CONDITION] limit [LIMIT] sort by [FIELD] [ORDER] into table [TABLE v]` - Query database
- `remove rows from collection [COLLECTION] where [CONDITION]` - Delete from database
- `update collection [COLLECTION] from table [TABLE v]` - Update database rows

**Current T26 Coverage:**
- ZERO skills mention database collections
- Students never learn to insert, query, update, or delete from persistent databases
- No mention of conditions, sorting, or limits for data queries

**Impact:** CRITICAL - Database collections are essential for:
- Large-scale data storage (beyond tables)
- Multi-user data sharing
- Advanced data management (CRUD operations)
- Real-world data workflows

**Recommended Action:**
```
NEW SKILL GROUP (Grade 6-7):

ID: T26.G6.05
Title: Insert data into a database collection
Description: Students populate a table with structured data (e.g., game inventory items with name, type, quantity) and insert it into a CreatiCode database collection, understanding how to persist data beyond local tables.
Dependencies:
* T10.G5.03: Update or insert rows in a table
* T26.G5.05: Save and load table data from cloud storage (NEW)
Challenge: Create an inventory system where items are stored in a database collection.
CreatiCode Blocks: `insert from table [] rows [] to [] into collection []`

ID: T26.G6.06
Title: Query data from a database collection
Description: Students fetch data from a database collection using conditions (e.g., "fetch all items where type = 'weapon'"), limits, and sorting, loading results into a table for processing.
Dependencies:
* T26.G6.05: Insert data into a database collection
* T10.G5.05: Search and filter table data
Challenge: Query a leaderboard database to show top 10 players sorted by score.
CreatiCode Blocks: `fetch from collection [] condition [] limit [] sort by [] into table []`

ID: T26.G7.05
Title: Update and delete database records
Description: Students fetch rows from a database collection, modify them in a table, then update the collection. They also practice deleting records based on conditions.
Dependencies:
* T26.G6.06: Query data from a database collection
* T10.G7.03: Transform or clean data in a table using loops and conditions
Challenge: Update player stats in a database, then delete inactive players.
CreatiCode Blocks: `update collection [] from table []`, `remove rows from collection [] where []`
```

### Gap 3: Player Score Recording & Leaderboards - NOT COVERED

**CreatiCode Blocks:**
- `record player score (VALUE)` - Record score for current user (auto-timestamped)
- `show game leaderboard [SORT v] rows [ROWS] header [COLOR] background [COLOR]` - Display leaderboard
- `hide game leaderboard` - Hide leaderboard
- `clear game leaderboard` - Clear all scores

**Current T26 Coverage:**
- ZERO skills teach leaderboard functionality
- Students never learn to record player scores
- No coverage of game-specific data collection

**Impact:** CRITICAL - Leaderboards are:
- A primary use case for data collection in games
- Motivating for students (competitive element)
- Real-world skill (most games have leaderboards)

**Recommended Action:**
```
NEW SKILL:
ID: T26.G5.06
Title: Record and display player scores with leaderboards
Description: Students use the `record player score` block to save scores for multiple players during gameplay, then display a leaderboard showing the top scorers with customizable styling.
Dependencies:
* T09.G4.01: Use a variable to track a sprite's property
* T14.G4.01: Track score in a simple game
* T26.G4.02: Use tables to log multi-attribute events
Challenge: Create a simple game that records player scores and displays a top-5 leaderboard.
CreatiCode Blocks: `record player score ()`, `show game leaderboard [] rows []`
```

### Gap 4: Semantic Database (Embedding-Based Search) - NOT COVERED

**CreatiCode Blocks:**
- `create semantic database from table [TABLE v]` - Build semantic index from table with 'key' column
- `search semantic database with [QUERY] store top (K) in table [TABLE v] filter by column [FIELD] of value [VALUE]` - Semantic search with filtering
- `search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE v]` - Semantic search with SQL-like conditions

**Current T26 Coverage:**
- ZERO mention of semantic databases
- No coverage of embedding-based search
- Missing advanced AI-powered data retrieval

**Impact:** MEDIUM-HIGH - Semantic databases are:
- A cutting-edge AI feature unique to CreatiCode
- Relevant for chatbot/QA systems (T22)
- Part of modern AI/ML workflows (T20-T24)

**Recommended Action:**
```
NEW SKILL:
ID: T26.G8.05
Title: Create and query a semantic database
Description: Students build a semantic database from a table containing FAQ entries (with a 'key' column for questions/content) and use natural language queries to retrieve relevant entries based on meaning rather than exact matches.
Dependencies:
* T26.G6.06: Query data from a database collection
* T22.G7.01: Build a rule-based chatbot with multi-turn conversation
* T10.G7.01: Design and populate a table for a real-world inventory or database
Challenge: Create a FAQ chatbot that uses semantic search to find answers to user questions.
CreatiCode Blocks: `create semantic database from table []`, `search semantic database with [] store top () in table []`
```

### Gap 5: Sensor Data Collection to Tables - BARELY COVERED

**CreatiCode Blocks:**
- `run face detection debug [DEBUG v] and write into table [TABLE v]` - Real-time face detection to table
- `run 3D pose detection debug [DEBUG v] table [TABLE v]` - 3D pose skeleton to table
- `run hand detection table [TABLE v] debug [DEBUG v] show video [VIDEO v]` - Hand landmarks to table
- `run 2D body part recognition into table [TABLE v]` - 2D body pose to table

**Current T26 Coverage:**
- G6.02 mentions "Automate multi-sensor logging (voice + pose)" but is VAGUE
- Original description says "Learners combine T23 blocks to record speech text and pose coordinates"
- NO SPECIFIC MENTION of the `write into table` blocks for face/hand/pose detection
- Missing Grade 4-5 introduction to sensor data collection

**Impact:** HIGH - Sensor data collection is:
- A unique CreatiCode feature (AI perception)
- Highly engaging for students
- Relevant for pose-based games, gesture controls, AR projects

**Recommended Action:**
```
MODIFY EXISTING:
ID: T26.G6.02
OLD TITLE: Automate multi-sensor logging (voice + pose)
NEW TITLE: Log sensor data from face, body, hand, and pose detection

OLD DESCRIPTION: Learners combine T23 blocks to record speech text and pose coordinates simultaneously, ensuring all data is captured with matching timestamps.

NEW DESCRIPTION: Students use CreatiCode's AI perception blocks to automatically log sensor data into tables: face detection (face position, expressions), 3D pose detection (body skeleton joints), hand detection (finger landmarks), and body part recognition. They capture data with timestamps and process it for gesture-based controls or analytics.

NEW CHALLENGE: Build a pose-based game that logs all player body movements into a table for post-game analysis.

SPECIFIC BLOCKS:
* `run face detection debug [yes v] and write into table [faces v]`
* `run 3D pose detection debug [yes v] table [poses v]`
* `run hand detection table [hands v] debug [yes v] show video [yes v]`
* `run 2D body part recognition into table [bodyparts v]`

ADD NEW EARLIER SKILL:
ID: T26.G5.07
Title: Collect face detection data into a table
Description: Students use the face detection block to log detected faces into a table, capturing face position, size, and detection confidence for each frame, then analyze the data to count how many times faces appeared.
Dependencies:
* T10.G5.01: Create and populate a table variable
* T23.G5.01: Run face recognition and report results (detecting a face)
Challenge: Build a "face counter" that logs all detected faces and reports total count.
CreatiCode Blocks: `run face detection debug [yes v] and write into table []`
```

### Gap 6: Console Logging with Print Blocks - PARTIALLY COVERED

**CreatiCode Blocks:**
- `print [MESSAGE] in [WINDOW v] color [COLOR]` - Print to console or alert window
- `get console log` - Reporter that returns all console output

**Current T26 Coverage:**
- G5.01 titled "Instrument a project with runtime logs" mentions "print blocks" in description
- BUT the description says "insert scripts that append event descriptions to a list" - NOT printing to console
- G5.01 conflates list-based logging with console logging

**Impact:** MEDIUM - Console logging is:
- Essential for debugging
- Standard practice in professional development
- Different from list-based logging (ephemeral vs persistent)

**Recommended Action:**
```
MODIFY EXISTING:
ID: T26.G5.01
CURRENT TITLE: Instrument a project with runtime logs
KEEP TITLE (it's good)

CURRENT DESCRIPTION: Students insert scripts that append event descriptions to a list whenever certain actions occur (level start, damage taken), enabling post-play analysis.

NEW DESCRIPTION: Students add logging to their projects using TWO methods: (1) print messages to the console panel using `print [] in [console v]` for debugging during development, and (2) append event data to lists or tables for post-play analysis. They learn when to use each method: console for immediate debugging, data structures for persistent analysis.

NEW CHALLENGE: Add both console logging (for debugging) and list logging (for analysis) to a game, then review console output and analyze the list data.

SPECIFIC BLOCKS:
* `print [] in [console v] color []` - For debugging
* `add [] to list []` - For persistent logging
* `add to table []: [] [] []` - For structured logging
```

### Gap 7: Google Sheets Integration - NEEDS EXPANSION

**CreatiCode Blocks:**
- `read from google sheet: url [] sheet name [] range [] into table []` - Import from Sheets
- `write into google sheet: url [] sheet name [] starting cell [] from table []` - Export to Sheets
- `list all sheets in google sheet at URL [] into list []` - List sheet names
- `append row () from table [] to sheet [] in Google Sheet at URL []` - Append single row
- `set value at row () column [] to [] in sheet [] in Google Sheet at URL []` - Update cell
- `get value at row () column [] in sheet [] in Google Sheet at URL []` - Read cell
- `remove rows/columns from sheet [] in Google Sheet at URL []` - Delete ranges
- `insert rows/columns at position [] in sheet [] in Google Sheet at URL []` - Insert ranges
- `clear sheet [] in Google Sheet at URL []` - Clear all data

**Current T26 Coverage:**
- G8.01 mentions "Google Sheets" in passing for telemetry pipelines
- NO DEDICATED SKILL for Google Sheets read/write operations
- Missing collaborative data collection workflows
- Not leveraging Google Sheets as a data source/destination

**Impact:** HIGH - Google Sheets integration enables:
- Collaborative data collection (multiple users)
- Real-world data import/export workflows
- Data sharing beyond CreatiCode platform
- Integration with other tools (Excel, data science tools)

**Recommended Action:**
```
NEW SKILL GROUP:

ID: T26.G6.07
Title: Import data from Google Sheets into tables
Description: Students use a shared Google Sheet URL to import a range of cells into a CreatiCode table, enabling them to work with real-world datasets shared via Google Sheets (e.g., survey results, public datasets).
Dependencies:
* T10.G5.01: Create and populate a table variable
* T10.G5.05: Search and filter table data
Challenge: Import a public dataset from Google Sheets and analyze it.
CreatiCode Blocks: `read from google sheet: url [] sheet name [] range [] into table []`

ID: T26.G6.08
Title: Export data to Google Sheets for collaboration
Description: Students export their CreatiCode table data to a Google Sheet, enabling them to share results with others, collaborate on data analysis, or import data into other tools like Excel or Tableau.
Dependencies:
* T26.G6.07: Import data from Google Sheets into tables
* T10.G5.03: Update or insert rows in a table
Challenge: Export survey results to Google Sheets for team analysis.
CreatiCode Blocks: `write into google sheet: url [] sheet name [] starting cell [] from table []`

ID: T26.G7.06
Title: Update and append data in Google Sheets
Description: Students use advanced Google Sheets operations to append new rows, update specific cells, insert/remove rows and columns, and clear sheets, enabling dynamic data management across platforms.
Dependencies:
* T26.G6.08: Export data to Google Sheets for collaboration
* T10.G6.02: Join or merge data from two tables
Challenge: Build a data pipeline that continuously appends new survey responses to a Google Sheet.
CreatiCode Blocks: `append row () from table [] to sheet []`, `set value at row () column [] to []`
```

### Gap 8: Multiplayer Game Data Storage - NOT COVERED

**CreatiCode Blocks:**
- `list players in game in table [TABLE v]` - Get all players in current game (name, role)
- `list multiplayer games in server in table [TABLE v]` - Get all active games (host, game name, user count)

**Current T26 Coverage:**
- NO skills teach logging multiplayer game state
- Missing coverage of player tracking in multiplayer contexts
- Not integrated with T19 (Multiplayer Games)

**Impact:** MEDIUM - Multiplayer data is relevant for:
- Understanding game dynamics (who played when)
- Analytics on multiplayer sessions
- Integration with leaderboards

**Recommended Action:**
```
NEW SKILL:
ID: T26.G6.09
Title: Log multiplayer game session data
Description: Students use multiplayer blocks to log player information (names, roles) and game session data (host, player count) into tables, enabling post-game analysis of who participated and when.
Dependencies:
* T19.G5.01: Join a multiplayer game as a player
* T10.G5.01: Create and populate a table variable
* T26.G5.04: Store logs in CreatiCode tables for export
Challenge: Build a multiplayer game that logs all players and exports session data after each game.
CreatiCode Blocks: `list players in game in table []`, `list multiplayer games in server in table []`
```

### Gap 9: Variable Export to Files - NOT COVERED

**CreatiCode Blocks:**
- `export variable [] to file []` - Export variable value to .txt file
- `import variable [] from file []` - Import variable from file

**Current T26 Coverage:**
- G5.04 mentions table export to CSV
- NO mention of exporting individual variables to files
- Missing simple file I/O for variables

**Impact:** LOW-MEDIUM - Variable file export enables:
- Saving settings/preferences
- Simple data exchange
- Debugging by inspecting variable values

**Recommended Action:**
```
NEW SKILL:
ID: T26.G5.08
Title: Export and import variables to files
Description: Students export variable values (numbers, text) to .txt files and import them back, learning basic file I/O for saving user preferences or simple data.
Dependencies:
* T09.G4.01: Use a variable to track a sprite's property
* T26.G5.04: Store logs in CreatiCode tables for export
Challenge: Create a settings system that saves user preferences to a file and loads them on restart.
CreatiCode Blocks: `export variable [] to file []`, `import variable [] from file []`
```

### Gap 10: CSV Import from Files - PARTIALLY COVERED

**CreatiCode Blocks:**
- `import file into table [TABLE v]` - Import CSV/TXT into table
- `export table [TABLE v] as [FILENAME]` - Export table to CSV

**Current T26 Coverage:**
- G5.04 mentions "prepping for CSV export to T27"
- G7.03 mentions "import an open dataset (weather, public CSV)"
- BUT no dedicated skill on CSV import mechanics

**Impact:** LOW - CSV import is covered in G7.03, but could be more explicit

**Recommended Action:**
```
MODIFY EXISTING:
ID: T26.G7.03
CURRENT: Document provenance for external datasets
EXPAND DESCRIPTION to explicitly mention:
* Using `import file into table []` to load CSV files
* Understanding CSV format and column headers
* Validating imported data before analysis
```

---

## Part 2: SKILLS THAT DON'T MATCH PLATFORM

### Issue P1: G5.01 Confuses Console Logging with List Logging

**Problem:**
- Title says "Instrument a project with runtime logs"
- Description says "insert scripts that append event descriptions to a list"
- BUT there's a separate console logging feature: `print [] in [console v]`
- Skill doesn't teach actual console logging

**Fix:** See Gap 6 above - separate console logging (debugging) from data structure logging (analysis)

### Issue P2: G6.02 Too Vague About Sensor Data Collection

**Problem:**
- Says "combine T23 blocks to record speech text and pose coordinates"
- Doesn't mention the specific `write into table` blocks for face/hand/pose detection
- Missing explicit block references

**Fix:** See Gap 5 above - rewrite to focus on sensor-to-table blocks

### Issue P3: G8.01 Mentions Google Sheets But No Prior Teaching

**Problem:**
- G8.01 mentions Google Sheets in "telemetry pipelines"
- BUT no prior skill teaches Google Sheets integration
- Students never learned read/write operations

**Fix:** See Gap 7 above - add G6-G7 skills for Google Sheets before G8.01

---

## Part 3: PROGRESSION ISSUES

### Progression Issue 1: Cloud Features Come Too Late

**Problem:**
- Cloud save/load not taught until proposed G5.05 (NEW)
- Database collections not taught at all
- Students work with local data K-G5 without learning persistence

**Impact:** Students miss 5+ years of cloud data concepts

**Fix:**
```
RECOMMENDED PROGRESSION:
G5: Introduce cloud save/load for tables (NEW G5.05)
G6: Introduce database insert/query (NEW G6.05, G6.06)
G7: Introduce database update/delete (NEW G7.05)
G8: Advanced pipelines with semantic databases (NEW G8.05)
```

### Progression Issue 2: Leaderboards Should Come Before Database Collections

**Problem:**
- Leaderboards are simpler (one block) than database CRUD
- More motivating for students (games)
- Should appear in G5, not G6+

**Fix:**
```
G5.06 (NEW): Record player scores and show leaderboards
G6.05 (NEW): Insert data into database collections
```

### Progression Issue 3: Sensor Data Logging Should Start in G5

**Problem:**
- G6.02 is the FIRST mention of sensor data collection
- But sensor detection is introduced in T23.G5.01 (face recognition)
- Gap between learning detection and learning to log detection data

**Fix:**
```
G5.07 (NEW): Collect face detection data into a table
G6.02 (MODIFIED): Log all sensor types (face, body, hand, pose)
```

### Progression Issue 4: Google Sheets Too Late (G8)

**Problem:**
- Google Sheets first mentioned in G8.01
- But import/export concepts ready by G6
- Missing collaborative data workflows

**Fix:**
```
G6.07 (NEW): Import data from Google Sheets
G6.08 (NEW): Export data to Google Sheets
G7.06 (NEW): Update and append to Google Sheets
G8.01 (KEEP): Use Google Sheets in telemetry pipelines
```

---

## Part 4: PRIVACY/CONSENT ISSUES

### Privacy Issue 1: Privacy Skills Exist But Not Integrated with Cloud Features

**Current Privacy Skills:**
- G4.04: Reflect on privacy in collection
- G6.03: Create consent and opt-out workflows
- G7.03: Document provenance for external datasets
- G8.04: Publish data privacy agreements for peers

**Problem:**
- Privacy skills exist but don't reference cloud save/load, databases, or Google Sheets
- Students learn to save data to cloud (proposed G5.05) BEFORE learning privacy (G6.03)

**Fix:**
```
MODIFY G6.03:
Add explicit coverage of:
* Asking consent before saving data to cloud
* Disabling database inserts when users opt out
* Privacy implications of Google Sheets sharing

ADD NEW DEPENDENCY:
G6.03 should depend on G5.05 (cloud save/load) and G6.05 (database insert)
```

### Privacy Issue 2: Leaderboards and Player Data Not Covered in Privacy Skills

**Problem:**
- Leaderboards record player names + scores (proposed G5.06)
- This is personally identifiable information
- No privacy skill addresses leaderboard data

**Fix:**
```
MODIFY G6.03:
Add coverage of:
* Leaderboard privacy (anonymous vs named scores)
* Clearing leaderboard data (user's right to be forgotten)
* GDPR-style considerations for game data
```

---

## Part 5: SKILL QUALITY ISSUES

### Quality Issue 1: Too Broad - G8.01 "Design Telemetry Pipelines"

**Problem:**
- G8.01 asks students to "diagram sources → processing → storage → export"
- Too abstract without specific CreatiCode context
- Doesn't specify which blocks to use at each stage

**Fix:**
```
REWRITE G8.01 DESCRIPTION:
Students design a multi-stage data pipeline for a CreatiCode game:
1. SOURCES: Face detection, pose detection, game events → tables
2. PROCESSING: Filter, aggregate, clean data using table operations
3. STORAGE: Save to cloud using `save table to server`, insert into database collections
4. EXPORT: Export to CSV, write to Google Sheets
They diagram each stage, specify the CreatiCode blocks used, and implement a working prototype.

ADD SPECIFIC BLOCKS:
* `run face detection and write into table []`
* `delete row () of table []` (cleaning)
* `save table [] to server as []`
* `insert from table [] into collection []`
* `export table [] as []`
* `write into google sheet: url [] from table []`
```

### Quality Issue 2: Overlapping - G5.04 vs G7.03

**Problem:**
- G5.04: "Store logs in CreatiCode tables for export"
- G7.03: "Document provenance for external datasets"
- Both mention CSV import, but G7.03 focuses on metadata

**Fix:** These are actually distinct (G5.04 = export, G7.03 = import + metadata). No change needed.

### Quality Issue 3: Missing Block References Throughout

**Problem:**
- Many skills don't specify exact CreatiCode blocks
- Makes it hard for teachers to know what to teach
- Auto-grading difficult without block specificity

**Fix:**
```
RECOMMENDATION FOR ALL SKILLS:
Add "CreatiCode Blocks Used:" section to every G3+ skill listing exact blocks:
* Block syntax from blockdes8.txt
* Example usage
* Parameters to focus on

EXAMPLE (for proposed G6.05):
CreatiCode Blocks Used:
* `insert from table [inventory v] rows [1] to [10] into collection [game_items]`
  - TABLE: source table name
  - START/END: row range to insert
  - COLLECTION: database collection name
```

---

## Part 6: DEPENDENCY ISSUES WITHIN T26

### Dependency Issue 1: G5.02 Violates X-2 Rule (Already Identified)

**Problem:** G5.02 depends on T26.GK.02 and T26.GK.03 (Kindergarten from Grade 5)

**Fix:** (Already covered in existing T26_COMPREHENSIVE_ANALYSIS.md - remove K dependencies)

### Dependency Issue 2: Proposed New Skills Need Careful Dependency Chains

**New Skills Dependencies:**

```
G5.05 (cloud save/load) depends on:
* T10.G5.01: Create and populate a table variable
* T10.G5.03: Update or insert rows in a table
* T26.G5.04: Store logs in CreatiCode tables for export

G5.06 (leaderboards) depends on:
* T09.G4.01: Use a variable to track a sprite's property
* T14.G4.01: Track score in a simple game
* T26.G4.02: Use tables to log multi-attribute events

G5.07 (face detection to table) depends on:
* T10.G5.01: Create and populate a table variable
* T23.G5.01: Run face recognition and report results

G5.08 (variable export) depends on:
* T09.G4.01: Use a variable to track a sprite's property
* T26.G5.04: Store logs in CreatiCode tables for export

G6.05 (database insert) depends on:
* T10.G5.03: Update or insert rows in a table
* T26.G5.05: Save and load table data from cloud storage (NEW)

G6.06 (database query) depends on:
* T26.G6.05: Insert data into a database collection (NEW)
* T10.G5.05: Search and filter table data

G6.07 (Google Sheets import) depends on:
* T10.G5.01: Create and populate a table variable
* T10.G5.05: Search and filter table data

G6.08 (Google Sheets export) depends on:
* T26.G6.07: Import data from Google Sheets (NEW)
* T10.G5.03: Update or insert rows in a table

G6.09 (multiplayer data logging) depends on:
* T19.G5.01: Join a multiplayer game as a player
* T10.G5.01: Create and populate a table variable
* T26.G5.04: Store logs in CreatiCode tables for export

G7.05 (database update/delete) depends on:
* T26.G6.06: Query data from a database collection (NEW)
* T10.G7.03: Transform or clean data in a table

G7.06 (Google Sheets append/update) depends on:
* T26.G6.08: Export data to Google Sheets (NEW)
* T10.G6.02: Join or merge data from two tables

G8.05 (semantic database) depends on:
* T26.G6.06: Query data from a database collection (NEW)
* T22.G7.01: Build a rule-based chatbot
* T10.G7.01: Design and populate a table for real-world inventory
```

**Validation:** All dependencies satisfy X-2 rule and logical progression.

---

## Part 7: SUMMARY OF RECOMMENDED ACTIONS

### CRITICAL ACTIONS (Must Add)

1. **Add Cloud Storage Skills (G5.05)**
   - Save/load tables from CreatiCode server
   - Essential foundational feature

2. **Add Database Collection Skills (G6.05, G6.06, G7.05)**
   - Insert, query, update, delete from database
   - MongoDB-style operations
   - Critical gap in current curriculum

3. **Add Leaderboard Skill (G5.06)**
   - Record player scores
   - Display game leaderboards
   - High student engagement

4. **Add Google Sheets Skills (G6.07, G6.08, G7.06)**
   - Import from Google Sheets
   - Export to Google Sheets
   - Append/update operations
   - Collaborative data workflows

5. **Modify G6.02 for Sensor Data Collection**
   - Explicitly teach face/hand/pose detection to tables
   - Add specific block references
   - Add earlier G5.07 for face detection introduction

6. **Modify G5.01 for Console Logging**
   - Separate console logging (debugging) from list logging (analysis)
   - Teach `print [] in [console v]` explicitly

### HIGH PRIORITY ACTIONS (Should Add)

7. **Add Semantic Database Skill (G8.05)**
   - Create and query semantic databases
   - Embedding-based search
   - Advanced AI feature

8. **Add Multiplayer Data Logging (G6.09)**
   - Log player information
   - Track game sessions

9. **Add Variable Export Skill (G5.08)**
   - Export/import variables to files
   - Simple file I/O

10. **Update Privacy Skills (G6.03)**
    - Add cloud storage privacy
    - Add database privacy
    - Add leaderboard privacy
    - Add Google Sheets sharing privacy

### MEDIUM PRIORITY ACTIONS (Nice to Have)

11. **Expand G7.03 CSV Import**
    - Make CSV import more explicit
    - Add validation techniques

12. **Add Specific Block References**
    - Every G3+ skill should list exact blocks
    - Include syntax and parameters

13. **Rewrite G8.01 for Specificity**
    - Concrete pipeline stages
    - Specific CreatiCode blocks at each stage

---

## Part 8: REVISED T26 STRUCTURE

### Grade K (3 skills) - UNCHANGED
- GK.01: Notice things you can count or compare
- GK.02: Use tokens to log repeated events
- GK.03: Capture yes/no answers with smile/frown cards

### Grade 1 (3 skills) - UNCHANGED
- G1.01: Run a three-option picture survey
- G1.02: Keep observation logs over time
- G1.03: Follow a simple data-collection checklist

### Grade 2 (5 skills) - UNCHANGED
- G2.01: Distinguish observational vs survey data
- G2.02: Build a two-column record sheet
- G2.03: Use timers to collect duration data
- G2.04: Explain why sample size matters
- G2.05: Conduct a multi-response tally survey

### Grade 3 (5 skills) - UNCHANGED
- G3.01: Script a CreatiCode survey loop
- G3.02: Write fair survey questions
- G3.03: Log sensor-style events with counters
- G3.04: Separate raw data from summary data
- G3.05: Spot common data collection mistakes

### Grade 4 (4 skills) - UNCHANGED
- G4.01: Create collection protocols for partners
- G4.02: Use tables to log multi-attribute events
- G4.03: Track missing/invalid data with flags
- G4.04: Reflect on privacy in collection

### Grade 5 (8 skills) - ADD 4 NEW SKILLS
- G5.01: Instrument a project with runtime logs (MODIFY - add console logging)
- G5.02: Plan sampling strategies (FIX - remove K dependencies)
- G5.03: Validate data entry with error checks
- G5.04: Store logs in CreatiCode tables for export
- **G5.05 (NEW): Save and load table data from cloud storage**
- **G5.06 (NEW): Record and display player scores with leaderboards**
- **G5.07 (NEW): Collect face detection data into a table**
- **G5.08 (NEW): Export and import variables to files**

### Grade 6 (9 skills) - ADD 5 NEW SKILLS
- G6.01: Map stakeholder questions to data requirements
- G6.02: Log sensor data from face, body, hand, and pose detection (MODIFY)
- G6.03: Create consent and opt-out workflows (MODIFY - add cloud/database privacy)
- G6.04: Note when measurements might be inaccurate
- **G6.05 (NEW): Insert data into a database collection**
- **G6.06 (NEW): Query data from a database collection**
- **G6.07 (NEW): Import data from Google Sheets into tables**
- **G6.08 (NEW): Export data to Google Sheets for collaboration**
- **G6.09 (NEW): Log multiplayer game session data**

### Grade 7 (6 skills) - ADD 2 NEW SKILLS
- G7.01: Build reusable data collection modules
- G7.02: Monitor data quality in real time
- G7.03: Document provenance for external datasets (MODIFY - expand CSV import)
- G7.04: Evaluate bias risks introduced during collection
- **G7.05 (NEW): Update and delete database records**
- **G7.06 (NEW): Update and append data in Google Sheets**

### Grade 8 (5 skills) - ADD 1 NEW SKILL
- G8.01: Design end-to-end telemetry pipelines (MODIFY - add specificity)
- G8.02: Implement scheduled data exports and resets
- G8.03: Use AI assistant to review data collection protocols
- G8.04: Publish data privacy agreements for peers
- **G8.05 (NEW): Create and query a semantic database**

**TOTAL SKILLS:**
- Current: 40 skills
- Proposed: 52 skills (+12 new, +6 modified)

---

## Part 9: ALIGNMENT WITH CREATICODE FEATURES

### Feature Coverage Summary

| CreatiCode Feature | Current Coverage | Proposed Coverage | Status |
|-------------------|------------------|-------------------|--------|
| Variables (basic) | ✓ G3+ (T09) | ✓ G3+ (T09) | Covered |
| Lists (basic) | ✓ G3+ (T10) | ✓ G3+ (T10) | Covered |
| Tables (create/populate) | ✓ G5+ (T10.G5.01) | ✓ G5+ (T10.G5.01) | Covered |
| Tables (query/filter) | ✓ G5+ (T10.G5.05) | ✓ G5+ (T10.G5.05) | Covered |
| Tables (sort/join) | ✓ G6+ (T10.G6.01-02) | ✓ G6+ (T10.G6.01-02) | Covered |
| CSV Export | ✓ G5.04 | ✓ G5.04 | Covered |
| CSV Import | Partial G7.03 | ✓ G7.03 (EXPAND) | Improved |
| Variable Export/Import | ✗ Missing | ✓ G5.08 (NEW) | ADDED |
| Cloud Save/Load Tables | ✗ Missing | ✓ G5.05 (NEW) | ADDED |
| Database Insert | ✗ Missing | ✓ G6.05 (NEW) | ADDED |
| Database Query | ✗ Missing | ✓ G6.06 (NEW) | ADDED |
| Database Update/Delete | ✗ Missing | ✓ G7.05 (NEW) | ADDED |
| Semantic Database | ✗ Missing | ✓ G8.05 (NEW) | ADDED |
| Google Sheets Import | ✗ Missing | ✓ G6.07 (NEW) | ADDED |
| Google Sheets Export | ✗ Missing | ✓ G6.08 (NEW) | ADDED |
| Google Sheets Update | ✗ Missing | ✓ G7.06 (NEW) | ADDED |
| Player Score Recording | ✗ Missing | ✓ G5.06 (NEW) | ADDED |
| Game Leaderboards | ✗ Missing | ✓ G5.06 (NEW) | ADDED |
| Face Detection to Table | Partial G6.02 | ✓ G5.07 (NEW) + G6.02 (MODIFY) | ADDED |
| Pose Detection to Table | Partial G6.02 | ✓ G6.02 (MODIFY) | Improved |
| Hand Detection to Table | Partial G6.02 | ✓ G6.02 (MODIFY) | Improved |
| Body Detection to Table | Partial G6.02 | ✓ G6.02 (MODIFY) | Improved |
| Console Logging | Partial G5.01 | ✓ G5.01 (MODIFY) | Improved |
| Multiplayer Player List | ✗ Missing | ✓ G6.09 (NEW) | ADDED |
| Survey (ask blocks) | ✓ G3.01 | ✓ G3.01 | Covered |
| Timers | ✓ G2.03 | ✓ G2.03 | Covered |

**Coverage Rate:**
- Current: 11/25 features covered (44%)
- Proposed: 25/25 features covered (100%)

---

## Part 10: CROSS-TOPIC INTEGRATION

### Integration with T10 (Lists & Tables)
- T26 heavily depends on T10 for data structures
- Current dependency is good
- New skills maintain this relationship

### Integration with T23 (AI Perception)
- T23 teaches face/pose/hand detection
- T26 should teach LOGGING the detection data
- G5.07 and modified G6.02 create this bridge

### Integration with T22 (Chatbots)
- Semantic database (G8.05) enables chatbot FAQ systems
- Should reference T22.G7.01 (rule-based chatbots)

### Integration with T19 (Multiplayer)
- G6.09 creates bridge between T19 and T26
- Multiplayer data logging enables analytics

### Integration with T14 (Games)
- G5.06 (leaderboards) bridges T14 and T26
- Game scoring feeds into data collection

### Integration with T27 (Data Analysis)
- T26 collects data, T27 analyzes it
- Current relationship is good
- New skills (database, Google Sheets) expand analysis possibilities

### Integration with T24 (AI Assistant/XO)
- G8.03 already uses XO to review protocols
- Could expand to use XO for data validation

---

## Part 11: IMPLEMENTATION PRIORITY

### Phase 1: Critical Gaps (Implement First)
1. G5.05 - Cloud save/load tables
2. G5.06 - Leaderboards
3. G6.05 - Database insert
4. G6.06 - Database query
5. G6.07 - Google Sheets import
6. G6.08 - Google Sheets export

### Phase 2: Sensor Data & Advanced Features
7. G5.07 - Face detection to table
8. G6.02 (MODIFY) - All sensor data to tables
9. G7.05 - Database update/delete
10. G7.06 - Google Sheets append/update
11. G8.05 - Semantic database

### Phase 3: Supporting Features
12. G5.01 (MODIFY) - Console logging
13. G5.08 - Variable export
14. G6.09 - Multiplayer data
15. G6.03 (MODIFY) - Privacy updates
16. G7.03 (MODIFY) - CSV import expansion
17. G8.01 (MODIFY) - Pipeline specificity

---

## CONCLUSION

T26 currently covers basic data collection (surveys, lists, tables, CSV export) well, but is **missing 10 major CreatiCode features** that are essential for real-world data workflows:

**CRITICAL MISSING FEATURES:**
1. Cloud storage (save/load data)
2. Database collections (MongoDB-style CRUD)
3. Player score recording & leaderboards
4. Google Sheets integration (import/export/update)
5. Sensor data collection to tables (face/hand/pose/body)
6. Console logging (print blocks)
7. Semantic databases
8. Multiplayer data logging
9. Variable file export
10. Advanced Google Sheets operations

**RECOMMENDED ACTIONS:**
- Add 12 new skills (G5.05-G5.08, G6.05-G6.09, G7.05-G7.06, G8.05)
- Modify 6 existing skills (G5.01, G5.02, G6.02, G6.03, G7.03, G8.01)
- Total: 52 skills (up from 40)
- Coverage: 100% of CreatiCode data features (up from 44%)

**PRIORITY:** Phase 1 (critical gaps) should be implemented immediately, as these are foundational features that enable authentic data workflows (cloud persistence, databases, collaboration via Google Sheets, game leaderboards).

---

**Document Version:** 1.0
**Analysis Date:** 2025-11-22
**Analyzed By:** Claude (Sonnet 4.5)
**Files Analyzed:**
- /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/skills_T26_data_collection_organization.md
- /media/binyu/USB2/dev/CreatiCodeSkillMap/T26_COMPREHENSIVE_ANALYSIS.md
- /media/binyu/USB2/ScratchCopilot/blockdes8.txt
