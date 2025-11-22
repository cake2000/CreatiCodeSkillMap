# T26 New Skills - Detailed Descriptions

This document contains the complete skill descriptions for all 12 new T26 skills, ready to be integrated into `skills_T26_data_collection_organization.md`.

---

## Grade 5 New Skills (4 skills)

### T26.G5.05 – Save and load table data from cloud storage

_Dependency:_
  * T10.G5.01: Create and populate a table variable
  * T10.G5.03: Update or insert rows in a table
  * T26.G5.04: Store logs in CreatiCode tables for export

- **Short name:** Cloud save/load for tables
- **Description:** Students save a table to the CreatiCode server with a name (e.g., "survey_results"), then load it back in a new session or from a different project, enabling data persistence across runs. They learn the difference between local tables (lost when project stops) and cloud-stored tables (persist on server).
- **Challenge format:** Coding. Create a survey that collects 5 responses, saves them to the cloud with `save table [] to server as []`, then loads the saved data when the project restarts and displays the total count. Auto-grading verifies the table is saved and loaded correctly.
- **CSTA:** E5-PRO-DH-02 (using cloud data structures), E5-DAA-DF-01 (collecting and storing data).
- **CreatiCode Blocks:**
  - `save table [tt v] to server as [mydata]` - Save entire table to server
  - `load [mydata] from server into table [tt v]` - Load table from server

---

### T26.G5.06 – Record and display player scores with leaderboards

_Dependency:_
  * T09.G4.01: Use a variable to track a sprite's property
  * T14.G4.01: Track score in a simple game
  * T26.G4.02: Use tables to log multi-attribute events

- **Short name:** Game leaderboards
- **Description:** Students use the `record player score` block to save scores for the current player during gameplay, then display a leaderboard showing the top scorers with customizable styling (header color, background color, number of rows). They learn that scores are automatically associated with player names and timestamps.
- **Challenge format:** Coding. Create a simple game (e.g., click target 10 times as fast as possible), record the final time as the player's score, then display a top-5 leaderboard sorted by fastest times. Auto-grading verifies scores are recorded and leaderboard displays correctly.
- **CSTA:** E5-DAA-DF-01 (collecting game data), E5-PRO-DH-02 (using server storage).
- **CreatiCode Blocks:**
  - `record player score (100)` - Record score for current user
  - `show game leaderboard [highest v] rows [10] header [#0000FF] background [#FFFFFF]` - Display leaderboard
  - `hide game leaderboard` - Hide leaderboard
  - `clear game leaderboard` - Clear all scores (admin use)

---

### T26.G5.07 – Collect face detection data into a table

_Dependency:_
  * T10.G5.01: Create and populate a table variable
  * T23.G5.01: Run face recognition and report results (detecting a face)

- **Short name:** Log face detection data
- **Description:** Students use the face detection block to automatically log detected faces into a table, capturing face position (x, y), size (width, height), and detection confidence for each frame. They then analyze the table to count how many faces were detected or compute average face size.
- **Challenge format:** Coding. Build a "face counter" that runs face detection for 10 seconds, logs all detections into a table, then reports the total number of faces detected. Auto-grading verifies the table contains face data and the count is accurate.
- **CSTA:** E5-DAA-DF-01 (collecting sensor data), E5-PRO-PF-01 (using AI blocks).
- **CreatiCode Blocks:**
  - `run face detection debug [yes v] and write into table [faces v]` - Log face detection to table
  - `row count of table [faces v]` - Count detections
  - `item at row (1) column [x] of table [faces v]` - Access face data

---

### T26.G5.08 – Export and import variables to files

_Dependency:_
  * T09.G4.01: Use a variable to track a sprite's property
  * T26.G5.04: Store logs in CreatiCode tables for export

- **Short name:** Save variables to files
- **Description:** Students export variable values (numbers, text) to .txt files using `export variable [] to file []` and import them back using `import variable [] from file []`, learning basic file I/O for saving user preferences or simple data (e.g., high score, player name, settings).
- **Challenge format:** Coding. Create a settings system that saves a "difficulty" variable to a file when the user changes it, then loads the saved difficulty when the project restarts. Auto-grading verifies the file is created and the variable is restored correctly.
- **CSTA:** E5-PRO-DH-02 (using file I/O), E5-DAA-DF-01 (storing data).
- **CreatiCode Blocks:**
  - `export variable [difficulty v] to file [settings.txt]` - Export variable to file
  - `import variable [difficulty v] from file [settings.txt]` - Import variable from file

---

## Grade 6 New Skills (5 skills)

### T26.G6.05 – Insert data into a database collection

_Dependency:_
  * T10.G5.03: Update or insert rows in a table
  * T26.G5.05: Save and load table data from cloud storage

- **Short name:** Database insert operations
- **Description:** Students populate a table with structured data (e.g., game inventory items with columns: name, type, quantity, price) and insert rows into a CreatiCode database collection using `insert from table [] rows [] to [] into collection []`. They learn that database collections persist across all users and projects (unlike cloud-saved tables which are project-specific).
- **Challenge format:** Coding. Create an inventory system where students add items to a table (at least 5 items), then insert all rows into a database collection named "game_items". Auto-grading verifies rows are inserted into the collection.
- **CSTA:** MS-DAA-DF-03 (organizing data in databases), MS-PRO-DH-04 (using persistent storage).
- **CreatiCode Blocks:**
  - `insert from table [inventory v] rows [1] to [10] into collection [game_items]` - Insert rows into database

---

### T26.G6.06 – Query data from a database collection

_Dependency:_
  * T26.G6.05: Insert data into a database collection
  * T10.G5.05: Search and filter table data

- **Short name:** Database query operations
- **Description:** Students fetch data from a database collection using conditions (e.g., "fetch all items where type = 'weapon'"), limits (e.g., top 10), and sorting (e.g., sort by price descending), loading results into a table for processing. They learn SQL-like querying concepts: filtering, limiting, ordering.
- **Challenge format:** Coding. Query a leaderboard database to show the top 10 players sorted by score (highest first). Auto-grading verifies the query returns correct results in the right order.
- **CSTA:** MS-DAA-DP-05 (processing and querying data), MS-DAA-DF-03 (using database queries).
- **CreatiCode Blocks:**
  - `fetch from collection [game_items] condition [type = "weapon"] limit [20] sort by [price] [descending] into table [results v]` - Query database

---

### T26.G6.07 – Import data from Google Sheets into tables

_Dependency:_
  * T10.G5.01: Create and populate a table variable
  * T10.G5.05: Search and filter table data

- **Short name:** Google Sheets import
- **Description:** Students use a shared Google Sheet URL to import a range of cells into a CreatiCode table, enabling them to work with real-world datasets shared via Google Sheets (e.g., survey results collected by a team, public datasets, teacher-provided data). They learn how to specify URL, sheet name, and cell range.
- **Challenge format:** Coding. Import a public dataset from a Google Sheet (provided URL, range A1:D20) and display the first 5 rows. Auto-grading verifies the table contains the correct imported data.
- **CSTA:** MS-DAA-DF-03 (importing external data), MS-PRO-DH-04 (using cloud data sources).
- **CreatiCode Blocks:**
  - `read from google sheet: url [URL] sheet name [Sheet1] range [A1:D10] into table [tt v]` - Import from Google Sheets
  - `list all sheets in google sheet at URL [URL] into list [sheets v]` - List available sheets

---

### T26.G6.08 – Export data to Google Sheets for collaboration

_Dependency:_
  * T26.G6.07: Import data from Google Sheets into tables
  * T10.G5.03: Update or insert rows in a table

- **Short name:** Google Sheets export
- **Description:** Students export their CreatiCode table data to a Google Sheet, enabling them to share results with others, collaborate on data analysis, or import data into other tools like Excel or Tableau. They learn how to specify the starting cell and sheet name for writing data.
- **Challenge format:** Coding. Export survey results (table with at least 10 rows) to a Google Sheet at a given URL. Auto-grading verifies the data appears in the Google Sheet.
- **CSTA:** MS-DAA-DF-04 (exporting and sharing data), MS-PRO-DH-04 (cloud collaboration).
- **CreatiCode Blocks:**
  - `write into google sheet: url [URL] sheet name [Sheet1] starting cell [A1] from table [tt v]` - Export to Google Sheets

---

### T26.G6.09 – Log multiplayer game session data

_Dependency:_
  * T19.G5.01: Join a multiplayer game as a player
  * T10.G5.01: Create and populate a table variable
  * T26.G5.04: Store logs in CreatiCode tables for export

- **Short name:** Multiplayer session logging
- **Description:** Students use multiplayer blocks to log player information (player names, roles) and game session data (host name, game name, player count) into tables using `list players in game in table []` and `list multiplayer games in server in table []`, enabling post-game analysis of who participated and when.
- **Challenge format:** Coding. Build a multiplayer game that logs all players at the start of each session and exports the player list at the end. Auto-grading verifies player data is captured correctly.
- **CSTA:** MS-DAA-DF-03 (collecting multiplayer data), MS-PRO-DH-04 (logging session data).
- **CreatiCode Blocks:**
  - `list players in game in table [players v]` - Log current players (name, role)
  - `list multiplayer games in server in table [games v]` - Log active game sessions (host, game name, user count)

---

## Grade 7 New Skills (2 skills)

### T26.G7.05 – Update and delete database records

_Dependency:_
  * T26.G6.06: Query data from a database collection
  * T10.G7.03: Transform or clean data in a table using loops and conditions

- **Short name:** Database update and delete
- **Description:** Students fetch rows from a database collection into a table, modify them (e.g., increase player health, update item quantity), then update the collection using `update collection [] from table []`. They also practice deleting records based on conditions using `remove rows from collection [] where []` (e.g., delete all items with quantity = 0).
- **Challenge format:** Coding. Fetch player stats from a database, increase all players' levels by 1, update the database, then delete all inactive players (where last_login < 30 days ago). Auto-grading verifies updates and deletes are applied correctly.
- **CSTA:** MS-DAA-DP-05 (updating data), MS-PRO-DH-04 (database operations).
- **CreatiCode Blocks:**
  - `update collection [players] from table [player_data v]` - Update database with modified table
  - `remove rows from collection [players] where [status = "inactive"]` - Delete matching records

---

### T26.G7.06 – Update and append data in Google Sheets

_Dependency:_
  * T26.G6.08: Export data to Google Sheets for collaboration
  * T10.G6.02: Join or merge data from two tables

- **Short name:** Google Sheets append and update
- **Description:** Students use advanced Google Sheets operations to append new rows using `append row () from table []`, update specific cells using `set value at row () column [] to []`, insert/remove rows and columns, and clear sheets. They learn to maintain live data connections where CreatiCode continuously updates a Google Sheet.
- **Challenge format:** Coding. Build a data pipeline that appends a new survey response to a Google Sheet every time someone completes a survey (simulate 5 responses). Auto-grading verifies all 5 responses appear in the Google Sheet.
- **CSTA:** MS-DAA-DP-05 (updating external data), MS-PRO-DH-04 (cloud data integration).
- **CreatiCode Blocks:**
  - `append row (1) from table [responses v] to sheet [Sheet1] in Google Sheet at URL [URL]` - Append single row
  - `set value at row (5) column [B] to [100] in sheet [Sheet1] in Google Sheet at URL [URL]` - Update specific cell
  - `insert [3] rows at row [10] in sheet [Sheet1] in Google Sheet at URL [URL]` - Insert rows
  - `remove rows [5] to [8] from sheet [Sheet1] in Google Sheet at URL [URL]` - Delete rows
  - `clear sheet [Sheet1] in Google Sheet at URL [URL]` - Clear all data

---

## Grade 8 New Skills (1 skill)

### T26.G8.05 – Create and query a semantic database

_Dependency:_
  * T26.G6.06: Query data from a database collection
  * T22.G7.01: Build a rule-based chatbot with multi-turn conversation
  * T10.G7.01: Design and populate a table for a real-world inventory or database

- **Short name:** Semantic database search
- **Description:** Students build a semantic database from a table containing FAQ entries (with a 'key' column for questions/content and other columns for metadata like category, author). They use `create semantic database from table []` to convert text to embedding vectors, then use natural language queries with `search semantic database with [] store top () in table []` to retrieve relevant entries based on meaning rather than exact text matches. They learn about embedding-based search and filtering by metadata.
- **Challenge format:** Coding + AI. Create a FAQ chatbot that uses semantic search: (1) populate a table with 20+ FAQ entries, (2) create semantic database, (3) when user asks a question, search the database and display the top 3 matching answers. Auto-grading tests with sample questions and verifies relevant answers are retrieved.
- **CSTA:** MS-CAS-AI-02 (using AI for search), MS-DAA-DP-05 (querying with AI), MS-PRO-PF-02 (implementing AI algorithms).
- **CreatiCode Blocks:**
  - `create semantic database from table [faq v]` - Build semantic index (requires 'key' column)
  - `search semantic database with [what is your refund policy?] store top (3) in table [results v]` - Semantic search
  - `search semantic database with [is scratch free?] where [(category = "pricing") and (region = "US")] store top (3) in table [results v]` - Search with SQL-like filters

---

## Modified Skills - Detailed Changes

### T26.G5.01 (MODIFIED) – Instrument a project with runtime logs

**CURRENT DESCRIPTION:**
Students insert scripts that append event descriptions to a list whenever certain actions occur (level start, damage taken), enabling post-play analysis.

**NEW DESCRIPTION:**
Students add logging to their projects using TWO methods: (1) **console logging** using `print [] in [console v] color []` for debugging during development (messages appear in console panel, ephemeral), and (2) **data structure logging** by appending event data to lists or tables for post-play analysis (persistent). They learn when to use each method: console for immediate debugging (e.g., "Level 1 started", "Score = 50"), data structures for persistent analysis (e.g., storing all player actions for later review).

**NEW CHALLENGE FORMAT:**
Coding. Add both types of logging to a game: (1) print debug messages to console when key events occur (level start, player hit), and (2) append event data to a table (timestamp, event type, event detail). Auto-grading verifies console contains expected messages and table contains event logs.

**ADDED BLOCKS:**
- `print [Debug: level started] in [console v] color [#FF0000]` - Console logging
- `get console log` - Retrieve all console output
- `add to table [events v]: [timestamp] [event] [detail]` - Table logging (already covered)

---

### T26.G5.02 (MODIFIED) – Plan sampling strategies

**CURRENT DEPENDENCIES:**
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.GK.02: Use tokens to log repeated events ❌ (X-2 VIOLATION)
* T26.GK.03: Capture yes/no answers with smile/frown cards ❌ (X-2 VIOLATION)

**NEW DEPENDENCIES:**
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list

**RATIONALE:** Removed T26.GK.02 and T26.GK.03 because they violate the X-2 rule (Grade 5 depending on Kindergarten). The remaining dependencies provide sufficient foundation for understanding sampling strategies.

---

### T26.G6.02 (MODIFIED) – Log sensor data from face, body, hand, and pose detection

**CURRENT TITLE:** Automate multi-sensor logging (voice + pose)

**NEW TITLE:** Log sensor data from face, body, hand, and pose detection

**CURRENT DESCRIPTION:**
Learners combine T23 blocks to record speech text and pose coordinates simultaneously, ensuring all data is captured with matching timestamps.

**NEW DESCRIPTION:**
Students use CreatiCode's AI perception blocks to automatically log sensor data into tables: **face detection** (face position, size, expressions), **3D pose detection** (body skeleton with 33 joint positions), **hand detection** (21 finger landmarks per hand), and **2D body part recognition** (17 body keypoints). They capture data with timestamps and process it for gesture-based controls, pose-based games, or post-session analytics. Each sensor writes directly to a table using specialized blocks.

**NEW CHALLENGE FORMAT:**
Coding. Build a pose-based game that logs all player body movements into a table for 30 seconds, then analyzes the data to report: (1) total frames captured, (2) average nose position (x, y, z), (3) whether player raised their hand above shoulder height. Auto-grading verifies table contains pose data and analytics are correct.

**SPECIFIC BLOCKS:**
- `run face detection debug [yes v] and write into table [faces v]` - Log face detection
- `run 3D pose detection debug [yes v] table [poses v]` - Log 3D body skeleton (33 joints)
- `run hand detection table [hands v] debug [yes v] show video [yes v]` - Log hand landmarks (21 points)
- `run 2D body part recognition into table [bodyparts v]` - Log 2D body keypoints (17 points)

**NOTE:** Voice/speech recognition should be handled separately (T23 Speech blocks don't auto-write to tables; students must manually log transcriptions).

---

### T26.G6.03 (MODIFIED) – Create consent and opt-out workflows

**CURRENT DESCRIPTION:**
Students implement dialog widgets that explain what will be collected, gather consent, and disable logging when declined.

**NEW DESCRIPTION:**
Students implement consent and opt-out workflows that explain what data will be collected (e.g., player scores, gameplay actions, face detection data), gather user consent using `ask [] and wait`, and disable logging when declined. They learn privacy implications for different data types: (1) **cloud storage** (data persists on server), (2) **database collections** (shared across all users), (3) **leaderboards** (public player names and scores), (4) **Google Sheets** (data shared externally). They practice asking consent BEFORE enabling these features and provide clear opt-out mechanisms.

**NEW CHALLENGE FORMAT:**
Coding + ethics. Build a game that: (1) asks for consent to record player score on leaderboard, (2) asks for consent to save game progress to cloud, (3) only enables each feature if user consents, (4) provides a "clear my data" button. Auto-grading tests both consent and opt-out paths.

**ADDED PRIVACY COVERAGE:**
- Cloud storage privacy (consent before `save table to server`)
- Database privacy (opt-out from `insert into collection`)
- Leaderboard privacy (anonymous vs named scores)
- Google Sheets privacy (warning about external data sharing)

**DEPENDENCIES ADDED:**
* T26.G5.05: Save and load table data from cloud storage (NEW)
* T26.G6.05: Insert data into a database collection (NEW)

---

### T26.G7.03 (MODIFIED) – Document provenance for external datasets

**CURRENT DESCRIPTION:**
Students import an open dataset (weather, public CSV) and log metadata (where it came from, license, when to refresh), reinforcing responsible use.

**NEW DESCRIPTION:**
Students import an external dataset using `import file into table []` (for CSV/TXT files) or `read from google sheet` (for Google Sheets), then document metadata about the data source: (1) **origin** (URL or source name), (2) **license** (Creative Commons, public domain, etc.), (3) **last updated** (date), (4) **refresh schedule** (how often to re-import), (5) **known limitations** (missing data, biases). They create a metadata table alongside the data table to track this information, reinforcing responsible data use and citation practices.

**NEW CHALLENGE FORMAT:**
Coding + documentation. Import a public dataset (provided URL), create a metadata table with the required fields (origin, license, date, refresh schedule, limitations), then write a summary explaining how to cite this data. Auto-grading checks metadata table completeness and citation accuracy.

**SPECIFIC BLOCKS EMPHASIZED:**
- `import file into table [data v]` - Import CSV/TXT files
- `read from google sheet: url [URL] sheet name [Sheet1] range [A1:Z100] into table [data v]` - Import from Google Sheets

**CURRENT CHALLENGE FORMAT:**
Concept + documentation. Auto-grading checks metadata fields are filled and references a real source.

**NEW CHALLENGE FORMAT:**
Coding + documentation (as above)

---

### T26.G8.01 (MODIFIED) – Design end-to-end telemetry pipelines

**CURRENT DESCRIPTION:**
Students draw a pipeline for a multi-level game (client logs → cleaning script → storage table → CSV export), emphasizing interfaces between steps.

**NEW DESCRIPTION:**
Students design a complete data pipeline for a CreatiCode game with 4 stages and implement a working prototype:

1. **SOURCES** (Data Collection): Use sensor blocks and event logging to generate raw data
   - Face detection → `faces` table
   - Pose detection → `poses` table
   - Game events → `events` table

2. **PROCESSING** (Data Cleaning): Filter, aggregate, and clean data
   - Delete invalid rows (missing data)
   - Aggregate events by type (count per category)
   - Join tables to combine sensor + game data

3. **STORAGE** (Persistence): Save processed data
   - Cloud storage: `save table [] to server as []`
   - Database: `insert from table [] into collection []`

4. **EXPORT** (Sharing): Output data for analysis
   - CSV export: `export table [] as []`
   - Google Sheets: `write into google sheet [] from table []`

They diagram each stage, specify the CreatiCode blocks used at each step, document data formats at each handoff, and implement a working prototype that demonstrates the full pipeline.

**NEW CHALLENGE FORMAT:**
Design + coding. Students create: (1) a pipeline diagram showing all 4 stages with specific blocks, (2) a working CreatiCode project that implements the pipeline, (3) documentation of data formats at each stage. Auto-grading verifies: (a) diagram completeness, (b) pipeline executes successfully, (c) data flows through all stages.

**SPECIFIC BLOCKS BY STAGE:**

**Stage 1 (Sources):**
- `run face detection debug [yes v] and write into table [faces v]`
- `run 3D pose detection debug [yes v] table [poses v]`
- `add to table [events v]: [time] [event] [player]`

**Stage 2 (Processing):**
- `delete row () of table []` - Remove invalid data
- `[sum] of column [score] in table [events v]` - Aggregate
- Join operations using loops (T10.G6.02)

**Stage 3 (Storage):**
- `save table [processed v] to server as [game_data]`
- `insert from table [processed v] rows [1] to [100] into collection [analytics]`

**Stage 4 (Export):**
- `export table [processed v] as [game_data.csv]`
- `write into google sheet: url [URL] sheet name [Analytics] starting cell [A1] from table [processed v]`

---

## Integration Notes

### When adding these skills to `skills_T26_data_collection_organization.md`:

1. **Grade 5 section:** Insert G5.05-G5.08 after current G5.04
2. **Grade 6 section:** Insert G6.05-G6.09 after current G6.04
3. **Grade 7 section:** Insert G7.05-G7.06 after current G7.04
4. **Grade 8 section:** Insert G8.05 after current G8.04
5. **Modify existing skills** as documented above

### Update section headers:
- Grade 5: Change from "Grade 5 (4 skills)" to "Grade 5 (8 skills)"
- Grade 6: Change from "Grade 6 (4 skills)" to "Grade 6 (9 skills)"
- Grade 7: Change from "Grade 7 (4 skills)" to "Grade 7 (6 skills)"
- Grade 8: Change from "Grade 8 (4 skills)" to "Grade 8 (5 skills)"

### Update T26 topic scope statement:
Add mention of cloud storage, database collections, Google Sheets integration, leaderboards, semantic databases, and sensor data logging as key covered features.

---

**Document Version:** 1.0
**Date:** 2025-11-22
**Total New Skills:** 12
**Total Modified Skills:** 6
**Ready for Integration:** Yes
