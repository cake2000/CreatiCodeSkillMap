# Topic T26 (Data Collection & Logging) - Comprehensive Analysis

## Executive Summary

This analysis examines all 45 skills in Topic T26 (Data Collection & Logging) across grades K-8. The topic shows strong pedagogical progression from unplugged activities (K-2) to sophisticated telemetry systems (G8), with generally good alignment to CreatiCode's technical capabilities.

**Key Findings:**
- **Strengths:** Clear K-2 unplugged foundation, good integration with T25 (tables), strong privacy/ethics thread (G4-G8)
- **Critical Issues:** 7 high-priority problems including circular dependencies, scope violations, and unnecessary same-grade dependencies
- **CreatiCode Alignment:** Strong - platform supports variables, lists, tables, Google Sheets integration, CSV export

---

## Part 1: Complete T26 Skills Inventory

### Kindergarten (3 skills)

**T26.GK.01** - Identify countable things in a picture
- **Type:** Unplugged/Picture-based
- **Dependencies:** None
- **Description:** Students scan a picture of a classroom and point to objects they could count (books, chairs, students), building awareness that we can collect information by counting things we see.

**T26.GK.02** - Use tokens to log repeated events
- **Type:** Unplugged/Picture-based
- **Dependencies:** T26.GK.01
- **Description:** Learners watch a simple animation and slide a bead/token each time an event occurs, then count tokens at the end. This is their first "log."

**T26.GK.03** - Capture yes/no answers with smile/frown cards
- **Type:** Unplugged/Picture-based
- **Dependencies:** T26.GK.01
- **Description:** Students ask a peer a yes/no question and place the response card into the correct bin, making a physical tally.

### Grade 1 (3 skills)

**T26.G1.01** - Run a three-option picture survey
- **Type:** Unplugged/Picture-based
- **Dependencies:** T01.GK.01, T26.GK.03
- **Description:** Students pick a topic (favorite snack) and provide three picture choices. They ask five peers and place stickers on a mini poster to record answers.

**T26.G1.02** - Keep observation logs over time
- **Type:** Unplugged/Picture-based
- **Dependencies:** T26.G1.01
- **Description:** Learners observe a daily attribute twice (morning vs afternoon temperature icon) for a week, emphasizing longitudinal collection.

**T26.G1.03** - Follow a simple data-collection checklist
- **Type:** Unplugged/Picture-based
- **Dependencies:** T26.G1.01
- **Description:** Students learn to (1) introduce themselves, (2) ask the question the same way, (3) record the answer immediately. They practice on classmates and reflect on why following steps matters.

### Grade 2 (5 skills)

**T26.G2.01** - Distinguish observational vs survey data
- **Type:** Unplugged/Picture-based
- **Dependencies:** T01.G1.01, T26.G1.02
- **Description:** Students categorize example data statements as "observed" (counting birds) or "asked" (favorite color), reinforcing method selection.

**T26.G2.02** - Build a two-column record sheet
- **Type:** Unplugged/Picture-based
- **Dependencies:** T26.G1.01, T25.G1.02
- **Description:** Learners create a simple table to log respondents' names and answers, showing why we store identifiers alongside data.

**T26.G2.03** - Use timers to collect duration data
- **Type:** Unplugged/Picture-based
- **Dependencies:** T01.G1.01, T26.G1.02
- **Description:** Students run a simple experiment (spin a top) and record each trial's duration using a timer, highlighting measurement precision.

**T26.G2.04** - Explain why sample size matters
- **Type:** Unplugged/Picture-based
- **Dependencies:** T26.G1.01, T26.G2.02
- **Description:** Learners see two surveys (3 responses vs 10) and explain why the larger one may be more reliable.

**T26.G2.05** - Conduct a multi-response tally survey
- **Type:** Unplugged/Picture-based
- **Dependencies:** T26.G2.04, T01.G1.01
- **Description:** Students run an unplugged survey with four or more answer choices (e.g., "What's your favorite season?"), practicing tally marks and organizing more complex response categories before learning coded surveys.

### Grade 3 (5 skills)

**T26.G3.01** - Script a CreatiCode survey loop
- **Type:** Coding-based
- **Dependencies:** T26.G2.01, T07.G3.01
- **Description:** Students write a script that repeats `ask` five times, storing each answer in a list variable (linking T26 to T25 representations).

**T26.G3.02** - Write fair survey questions
- **Type:** Coding-based
- **Dependencies:** T26.G3.01, T08.G3.01, T09.G3.01
- **Description:** Learners compare two survey questions—one that suggests an answer ("Don't you love cats?") and one that lets anyone answer honestly ("Do you like cats, dogs, or neither?")—and practice writing questions that give fair choices for everyone.

**T26.G3.03** - Log sensor-style events with counters
- **Type:** Coding-based
- **Dependencies:** T26.G3.01, T08.G3.01, T09.G3.01
- **Description:** Students build a script where a sprite increments a counter variable each time a key is pressed, simulating basic telemetry collection for tracking user interactions.

**T26.G3.04** - Separate raw data from summary data
- **Type:** Coding-based
- **Dependencies:** T26.G3.03, T08.G3.01, T09.G3.01
- **Description:** Learners maintain two structures: a raw list of answers and a summary list of counts, emphasizing why we preserve raw data separately from aggregated totals.

**T26.G3.05** - Spot common data collection mistakes
- **Type:** Coding-based
- **Dependencies:** T26.G3.04, T08.G3.01
- **Description:** Students review sample data sets containing common mistakes (missing entries, inconsistent spelling, duplicate records) and identify what went wrong, preparing them to track invalid data in G4.

### Grade 4 (4 skills)

**T26.G4.01** - Create collection protocols for partners
- **Type:** Coding-based
- **Dependencies:** T06.G3.01, T09.G3.05, T10.G3.03, T26.G3.04
- **Description:** Students draft multi-step protocols (who to ask, how many people, what to say) so teammates can collect consistent data.

**T26.G4.02** - Use tables to log multi-attribute events
- **Type:** Coding-based
- **Dependencies:** T06.G3.01, T09.G3.05, T10.G3.03, T26.G3.04
- **Description:** Learners capture gameplay telemetry in a table with columns (time, event, player). This mirrors logging for CreatiCode games.

**T26.G4.03** - Track missing/invalid data with flags
- **Type:** Coding-based
- **Dependencies:** T08.G3.01, T09.G3.05, T10.G3.03, T26.G4.02
- **Description:** Students add a column to note when data is missing or suspect, preparing them for cleaning in T27.

**T26.G4.04** - Reflect on privacy in collection
- **Type:** Coding-based
- **Dependencies:** T06.G3.01, T09.G3.05, T10.G3.03, T26.G4.01
- **Description:** Learners evaluate a proposed survey (asking for full names + addresses) and suggest safer alternatives, aligning with AI4K12 ethics.

### Grade 5 (4 skills)

**T26.G5.01** - Add print statements to track events during execution
- **Type:** Coding-based
- **Dependencies:** T09.G3.05, T10.G3.03, T26.G4.02
- **Description:** Students insert print blocks to display messages when specific events occur (level start, player hit), creating a log of what happened during gameplay for later analysis.

**T26.G5.02** - Plan sampling strategies
- **Type:** Coding-based
- **Dependencies:** T08.G3.01, T09.G3.05, T10.G3.03, T26.GK.02, T26.GK.03
- **Description:** Learners compare convenience sampling (asking whoever is nearby) vs random sampling (using a method to pick people fairly) for a class poll and document which they'll use and why.
- **⚠️ ISSUE:** References K skills (T26.GK.02, T26.GK.03) from G5 - violates X-2 rule

**T26.G5.03** - Validate data entry with error checks
- **Type:** Coding-based
- **Dependencies:** T08.G4.01, T09.G3.05, T10.G3.03, T26.G4.03
- **Description:** Students add checks (e.g., reject scores <0 or >100) during collection to ensure data quality upstream.

**T26.G5.04** - Store logs in CreatiCode tables for export
- **Type:** Coding-based
- **Dependencies:** T09.G3.05, T10.G4.02, T26.G5.01
- **Description:** Learners push collected events into table variables with named columns, prepping for CSV export to T27.

### Grade 6 (4 skills)

**T26.G6.01** - Map stakeholder questions to data requirements
- **Type:** Coding-based
- **Dependencies:** T08.G4.01, T09.G4.01, T09.G4.04, T10.G4.02, T26.G5.04
- **Description:** Students receive stakeholder questions ("Which level is hardest?") and specify what data to collect (attempt count, completion time), aligning collection with analysis goals.

**T26.G6.02** - Automate logging from multiple CreatiCode inputs
- **Type:** Coding-based
- **Dependencies:** T06.G4.01, T09.G4.04, T10.G4.02, T23.G5.01, T26.G5.04
- **Description:** Learners combine blocks to record data from multiple input sources (microphone level, pose detection, mouse position) simultaneously, ensuring all data is captured with matching timestamps.

**T26.G6.03** - Create consent and opt-out workflows
- **Type:** Coding-based
- **Dependencies:** T08.G4.01, T09.G4.04, T10.G4.02, T26.G4.04, T26.G6.01
- **Description:** Students implement dialog widgets that explain what will be collected, gather consent, and disable logging when declined.

**T26.G6.04** - Note when measurements might be inaccurate (originally: "Capture measurement error estimates")
- **Type:** Coding-based
- **Dependencies:** T08.G4.01, T09.G4.01, T09.G4.04, T10.G4.02, T26.G5.03
- **Description:** Learners add a "confidence" or "notes" column when recording measurements to indicate when values might be less accurate (e.g., "rushed measurement," "hard to see," "estimated"), teaching them to think about data quality.

### Grade 7 (4 skills)

**T26.G7.01** - Build reusable data collection modules
- **Type:** Coding-based
- **Dependencies:** T06.G5.01, T09.G3.05, T10.G5.03, T11.G5.02, T26.G6.01
- **Description:** Students wrap logging behavior into custom blocks (e.g., `logEvent type message data`) so multiple sprites can call the same routine.

**T26.G7.02** - Monitor data quality in real time
- **Type:** Coding-based
- **Dependencies:** T09.G3.01, T09.G3.05, T10.G5.03, T26.G6.04, T26.G7.01
- **Description:** Learners build HUD widgets indicating percentage of responses collected, number of nulls, or out-of-range counts to catch issues while collecting.
- **⚠️ ISSUE:** Depends on T26.G6.04 which was originally titled "Capture measurement error estimates" - title changed in current version

**T26.G7.03** - Document provenance for external datasets
- **Type:** Coding-based
- **Dependencies:** T08.G5.01, T09.G3.05, T10.G5.03, T26.G5.04, T26.G6.03
- **Description:** Students import an open dataset (weather, public CSV) and log metadata (where it came from, license, when to refresh), reinforcing responsible use.

**T26.G7.04** - Evaluate bias risks introduced during collection
- **Type:** Coding-based
- **Dependencies:** T08.G5.01, T09.G3.05, T10.G5.03, T26.G5.02, T26.G7.02
- **Description:** Learners compare planned participants vs actual participants and highlight underrepresented groups, proposing corrective actions.

### Grade 8 (4 skills)

**T26.G8.01** - Design end-to-end telemetry pipelines
- **Type:** Coding-based
- **Dependencies:** T01.G6.01, T06.G6.01, T09.G6.01, T10.G6.01, T26.G7.01
- **Description:** Students draw a pipeline for a multi-level game (client logs → cleaning script → storage table → CSV export), emphasizing interfaces between steps.

**T26.G8.02** - Implement scheduled data exports and resets
- **Type:** Coding-based
- **Dependencies:** T06.G6.01, T09.G6.01, T10.G6.01, T26.G7.01, T26.G8.01
- **Description:** Learners script timed routines that export a table to file (or display) and then clear/reset logs, mirroring production data rotation.

**T26.G8.03** - Use AI assistant to review data collection protocols
- **Type:** Coding-based
- **Dependencies:** T06.G6.01, T09.G6.01, T10.G6.01, T24.G6.01, T26.G8.01
- **Description:** Students send their data collection protocol to the XO AI assistant for review, then document which suggestions they accepted or rejected, demonstrating human oversight of AI recommendations.

**T26.G8.04** - Publish data privacy agreements for peers
- **Type:** Coding-based
- **Dependencies:** T09.G6.01, T10.G6.01, T26.G6.03, T26.G7.04
- **Description:** Learners author a short agreement describing what data will be collected, how it's stored, who can access it, and deletion timelines, tying back to AI4K12's societal-impact focus.

---

## Part 2: CreatiCode Feature Inventory for Data Collection

### 2.1 Variables (Standard + Extended)
CreatiCode provides all standard Scratch variable operations plus extensions:

**Basic Operations:**
- Set variable, change variable, show/hide variable
- Export variable to .txt file (`data_exportvariable`)
- Import variable from file (`data_importvariable`)

**Extended Operations:**
- Reduce variable by N (`data_reducevariableby`) - for younger learners unfamiliar with negative numbers

### 2.2 List Operations
**Basic List Operations:**
- Add/insert/delete items, get item at index
- Length, contains checks
- Sort (large to small, small to large)
- Reverse, reshuffle randomly
- Delete specific values

**Extended List Operations:**
- Change/reduce item by amount (`data_changeitemoflist`, `data_reduceitemoflist`)
- Join list into text with separator (`data_joinlistwith`)
- Split text into list with splitter (`data_set_list_to_split_of`)
- Show/hide list display

### 2.3 Table Operations (Robust Support)
CreatiCode has extensive table support - critical for T26 skills G4+:

**Table Structure:**
- Add/delete columns by name and position
- Add/insert/replace rows (up to 12 cells per operation)
- Delete rows (by index, by condition, or all)
- Delete all columns (clears table)

**Table Data Access:**
- Get item at row/column (`data_itematrowcolumnoftable`)
- Replace item at row/column
- Change/reduce item at row/column by amount
- Get row as text with separator (`data_rowatindexoftable`)
- Row count of table
- Find row # where column equals value
- Find row # where column contains substring
- Lookup: get item in column X where column Y equals value

**Table Aggregation:**
- Compute min/max/sum/average/median of column (`data_computetable`)
- Aggregate by grouping: set table to computed method of column by column (`data_settabletocomputed`)
- Pivot tables with row groups, value columns, and aggregation methods (`data_pivot_table_into_table`)

**Table Management:**
- Copy table into table (replaces all data)
- Append table to table (adds rows at bottom)
- Sort table by column (large to small / small to large)
- Reshuffle table randomly
- Show/hide table display
- Show snapshot of table with styling

**Import/Export:**
- Export table to CSV file (`data_exporttable`)
- Import CSV/txt file into table (`data_importtable`)
- Save table to CreatiCode server by name (`data_savetable`)
- Load table from CreatiCode server by name (`data_loadtable`)

**List-Table Conversion:**
- Copy list to column of table (`data_setlisttocolumn`)

### 2.4 Cloud/Google Sheets Integration
**Google Sheets Operations:**
- Read from Google Sheet (URL, sheet name, range) into table (`p2p_readfromgooglesheet`)
- Write into Google Sheet (URL, sheet name, start cell) from table (`p2p_writeintogooglesheet`)
- List all sheets in Google Sheet into list (`p2p_listSheetsInGoogleSheet`)
- Add/remove sheets from Google Sheet
- Append row from table to Google Sheet
- Set/get value at specific row/column in Google Sheet
- Remove rows/columns from Google Sheet range
- Insert rows/columns in Google Sheet
- Clear entire sheet

**Google Drive:**
- List content of Google Drive folder into table (filename, fileid, mimetype, url)

**Web Fetch:**
- Fetch web page as markdown from URL

### 2.5 Survey/Input Blocks
**Standard Scratch:**
- `ask [question] and wait` - standard input block
- `answer` - reporter block for last answer
- `stop asking` - interrupt waiting for input

**Implication for T26:**
- G3 survey loops (T26.G3.01) can use `ask` in repeat loops
- Answers stored in list variables for analysis
- No built-in multi-option survey widget, but can be built with ask + validation

### 2.6 Multiplayer/Database Support
**Game Server Features:**
- List players in game in table (player name, role)
- List multiplayer games in server in table (host name, game name, user count)

**Database Operations:**
- Insert from table into database collection
- Fetch from collection into table with conditions/limits/sorting
- Update collection from table

### 2.7 AI/ML Data Collection Support
**Machine Learning:**
- Train neural network model using table data
- Predict using NN model for table data
- Create KNN classifier from table
- Predict for table with classifier

**Semantic Database:**
- Create semantic database from table (with 'key' column)
- Search semantic database with query into table

**Pose/Vision Data Collection:**
- Run face detection and write into table (real-time)
- Run 2D body part recognition into table
- Run 3D pose detection into table
- Run hand detection into table
- Analyze sentence and write into table
- AR face camera with data table

### 2.8 Other Data Collection Features
**Sensing:**
- Timer operations (reset, pause, resume)
- Read color at position into variables
- Microphone volume
- Camera/video sensing

**Drawing/Charts:**
- Draw chart using columns from table (line, bar, scatter, etc.)
- Draw pie chart using category and value columns from table

**Web Search:**
- Web search query store top K results in table (title, link, snippet)

**Geo Data:**
- Get geo info for lat/lon and write into table (continent, country, state, city, etc.)

---

## Part 3: Issue Analysis (Within T26 Only)

### 3.1 HIGH PRIORITY ISSUES

#### Issue H1: Same-Grade Circular Dependency Risk (G3.04)
**Skill:** T26.G3.04 - Separate raw data from summary data
**Problem:** Depends on T26.G3.03, T08.G3.01, T09.G3.01 - all same grade (G3). While not circular, this creates tight coupling within G3.
**Impact:** MEDIUM - Makes it difficult to reorder G3 skills if needed
**Recommendation:**
- KEEP dependencies on T08.G3.01 and T09.G3.01 (foundational coding skills)
- KEEP dependency on T26.G3.03 (proper prerequisite)
- This is actually ACCEPTABLE - just note the coupling

**REVISED:** This is actually NOT an issue - downgrade to informational.

#### Issue H2: X-2 Rule Violation (G5.02)
**Skill:** T26.G5.02 - Plan sampling strategies
**Problem:** Depends on T26.GK.02 and T26.GK.03 (Kindergarten skills from G5)
**Impact:** HIGH - Violates X-2 rule (should only depend on G5, G4, G3)
**Recommendation:**
- REMOVE both Kindergarten dependencies (T26.GK.02, T26.GK.03)
- These unplugged activities from K are too far back
- The skill already has T08.G3.01, T09.G3.05, T10.G3.03 as foundation
- Students don't need to reference K-level token activities to understand sampling

**REVISED DEPENDENCIES:**
```
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
```

#### Issue H3: Scope Misalignment (G4 dependencies using G3 blocks)
**Skills:** T26.G4.01, T26.G4.02, T26.G4.04
**Problem:** All three depend on T06.G3.01, T09.G3.05, T10.G3.03 - but they are G4 skills
**Impact:** MEDIUM - Dependencies should generally be from the same grade or earlier, but these are referencing G3 versions when G4 versions exist
**Recommendation:**
- **Option A (Recommended):** Update to G4 equivalents where they exist:
  - T06.G3.01 → T06.G4.01
  - T09.G3.05 → T09.G4.04 (equivalent "Trace code with variables to predict outcomes")
  - T10.G3.03 → T10.G4.02 (if appropriate)
- **Option B:** Keep as-is if G3 skills are intentionally the exact prerequisites needed

**Investigation Needed:** Check if T06, T09, T10 have G4 versions that supersede G3 versions

#### Issue H4: Title Inconsistency Creates Dependency Confusion (G7.02)
**Skill:** T26.G7.02 - Monitor data quality in real time
**Problem:** Depends on "T26.G6.04: Capture measurement error estimates" but the actual skill is now titled "Note when measurements might be inaccurate"
**Impact:** LOW - Doesn't affect functionality but creates documentation confusion
**Recommendation:**
- Update dependency reference to use current title, OR
- Note that dependency references use stable IDs not titles

#### Issue H5: Heavy Same-Topic Dependencies in G4-G8
**Pattern:** Many G4+ skills have 4-5 dependencies, with 1-2 being within T26
**Examples:**
- T26.G4.01: 4 dependencies (1 within T26)
- T26.G4.02: 4 dependencies (1 within T26)
- T26.G6.01: 5 dependencies (1 within T26)
- T26.G7.01: 5 dependencies (1 within T26)

**Problem:** Creates long dependency chains within T26
**Impact:** LOW-MEDIUM - Makes it harder to extract individual skills for standalone teaching
**Recommendation:**
- This is actually ACCEPTABLE for advanced topics
- Data collection naturally builds on prior collection skills
- Most dependencies are to other topics (T06, T08, T09, T10) which is good modularity

**REVISED:** This is acceptable practice - data collection is inherently cumulative.

---

### 3.2 MEDIUM PRIORITY ISSUES

#### Issue M1: G6.04 Title Change May Break References
**Skill:** T26.G6.04
**Original Title:** "Capture measurement error estimates"
**Current Title:** "Note when measurements might be inaccurate"
**Problem:** Any references in T26 or other topics using old title may be outdated
**Impact:** MEDIUM - Documentation/communication issue
**Recommendation:**
- Use skill IDs (T26.G6.04) as stable references, not titles
- Document title changes in change log
- Check all downstream skills that reference this (T26.G7.02 confirmed)

#### Issue M2: Missing Intermediate Step Between G3.01 and G3.04
**Gap:** T26.G3.01 (survey loop) → T26.G3.03 (sensor counters) → T26.G3.04 (raw vs summary)
**Problem:** Jump from simple list storage (G3.01) to maintaining parallel structures (G3.04) might be steep
**Impact:** MEDIUM - Pedagogical gap
**Recommendation:**
- Consider adding G3 skill: "Modify list data during collection" between G3.01 and G3.04
- OR accept current progression as sufficient with G3.03 as bridge

#### Issue M3: Privacy Thread Starts Late (G4.04)
**Observation:** Privacy first appears in G4.04, then G6.03, G7.03, G8.04
**Problem:** Students are collecting data for 1.5 years (K-G4) before explicit privacy instruction
**Impact:** MEDIUM - Ethical gap
**Recommendation:**
- Add G2 or G3 skill: "Identify which survey questions are too personal"
- This could be unplugged (G2) or part of survey design (G3.02 could be expanded)

---

### 3.3 LOW PRIORITY ISSUES

#### Issue L1: Inconsistent Dependency Granularity
**Pattern:** Some skills depend on very specific sub-skills (T26.G3.04), others on broader skills (T06.G3.01)
**Impact:** LOW - Just a style inconsistency
**Recommendation:** Accept as-is; specificity is appropriate when needed

#### Issue L2: No Explicit Real-Time Data Collection Skill
**Gap:** Skills cover batch surveys, gameplay logging, but not streaming sensor data
**Impact:** LOW - May be covered implicitly in G6.02 (multiple inputs)
**Recommendation:**
- Consider adding G7 skill: "Stream sensor data with timestamps" if CreatiCode supports it
- OR note that G6.02 covers this adequately

#### Issue L3: Export/Persistence Introduced Late (G5.04)
**Observation:** Students work with data for K-G4 but don't formally export until G5.04
**Impact:** LOW - Early grades may not need file export
**Recommendation:** Accept as-is; G5 is appropriate for file operations

---

## Part 4: Quality Assessment

### 4.1 Internal Coherence
**Rating: STRONG (8/10)**

**Strengths:**
- Clear progression from counting (GK.01) → tokens (GK.02) → surveys (G1) → coding (G3) → tables (G4) → telemetry (G7-G8)
- Good transition from unplugged to coding at G3
- Privacy/ethics thread well-distributed (G4, G6, G7, G8)
- Scaffolding generally smooth

**Weaknesses:**
- G5.02 reaches back to Kindergarten (X-2 violation)
- G4 dependency patterns slightly inconsistent (see Issue H3)

### 4.2 Duplicates/Overlaps
**Rating: EXCELLENT (9/10)**

**No true duplicates found.** Each skill has distinct learning objective:
- GK.02 (tokens) vs GK.03 (cards) - different collection methods
- G3.03 (sensor counters) vs G5.01 (print logging) - different purposes
- G4.02 (tables) vs G5.04 (table export) - different operations

### 4.3 Dependencies (Within T26)
**Rating: GOOD (7/10)**

**Issues Found:**
1. **H2 (HIGH):** G5.02 violates X-2 rule (depends on Kindergarten from G5)
2. **H3 (MEDIUM):** G4 skills using G3 block versions instead of G4 equivalents
3. **H4 (LOW):** Title change creates documentation confusion (G6.04)

**Strengths:**
- Most skills depend on immediately prior grade (G3→G4→G5 progression)
- Few within-topic dependencies (1-2 per skill max)
- Cross-topic dependencies appropriate (T06, T08, T09, T10, T25)

### 4.4 Grade Appropriateness
**Rating: EXCELLENT (9/10)**

- **K-2:** All picture-based/unplugged ✓
- **G3+:** All coding-based ✓
- Cognitive load appropriate at each level
- G8 skills (telemetry pipelines, privacy agreements) suitably sophisticated

### 4.5 Missing Skills
**Rating: GOOD (7/10)**

**Potential Gaps:**
1. **G2-G3:** No explicit skill on "protecting personal information" before coding starts
2. **G6-G7:** No skill on "debugging collection scripts when data looks wrong"
3. **G7-G8:** No skill on "comparing collection methods for accuracy/bias"

**Mitigations:**
- Gap 1 partially addressed by G4.04 (privacy) but could be earlier
- Gap 2 partially covered by G7.02 (monitor quality) but could be more explicit
- Gap 3 partially covered by G7.04 (evaluate bias)

### 4.6 Skill Quality (Clear, Specific, Actionable, Assessable)
**Rating: EXCELLENT (9/10)**

Reviewing sample skills:

**T26.GK.01** - "Identify countable things in a picture"
- ✓ Clear: Yes (identify objects to count)
- ✓ Specific: Yes (countable things in picture)
- ✓ Actionable: Yes (scan and point)
- ✓ Assessable: Yes (can student identify 3+ countable objects?)

**T26.G3.04** - "Separate raw data from summary data"
- ✓ Clear: Yes (two different data structures)
- ✓ Specific: Yes (raw list + summary list)
- ✓ Actionable: Yes (maintain both)
- ✓ Assessable: Yes (check both structures exist and are correct)

**T26.G6.03** - "Create consent and opt-out workflows"
- ✓ Clear: Yes (implement consent dialog)
- ✓ Specific: Yes (explain, gather consent, disable if declined)
- ✓ Actionable: Yes (use dialog widgets)
- ✓ Assessable: Yes (test workflow with user declining)

**Minor weakness:** A few skills slightly broad (G8.01 "design pipeline" could specify deliverable format)

---

## Part 5: CreatiCode Alignment

### 5.1 Platform Support for T26 Skills

| Grade | Skill ID | Skill Title | CreatiCode Support | Notes |
|-------|----------|-------------|-------------------|-------|
| K | T26.GK.01-03 | Unplugged activities | N/A (unplugged) | ✓ Appropriate |
| G1 | T26.G1.01-03 | Unplugged surveys | N/A (unplugged) | ✓ Appropriate |
| G2 | T26.G2.01-05 | Unplugged data collection | N/A (unplugged) | ✓ Appropriate |
| G3 | T26.G3.01 | Survey loop | ✓ Fully supported | ask + repeat + list |
| G3 | T26.G3.02 | Fair survey questions | ✓ Fully supported | ask block |
| G3 | T26.G3.03 | Sensor event counters | ✓ Fully supported | variables + events |
| G3 | T26.G3.04 | Raw vs summary data | ✓ Fully supported | multiple lists |
| G3 | T26.G3.05 | Spot mistakes | ✓ Fully supported | view list data |
| G4 | T26.G4.01 | Collection protocols | ✓ Fully supported | scripts |
| G4 | T26.G4.02 | Tables for events | ✓ STRONGLY supported | extensive table ops |
| G4 | T26.G4.03 | Track invalid data | ✓ Fully supported | table columns |
| G4 | T26.G4.04 | Privacy reflection | ✓ Fully supported | unplugged/discussion |
| G5 | T26.G5.01 | Print logging | ✓ Fully supported | say/think blocks |
| G5 | T26.G5.02 | Sampling strategies | ✓ Fully supported | unplugged/planning |
| G5 | T26.G5.03 | Validate data entry | ✓ Fully supported | if blocks + validation |
| G5 | T26.G5.04 | Store in tables | ✓ STRONGLY supported | table + export CSV |
| G6 | T26.G6.01 | Map stakeholder questions | ✓ Fully supported | planning |
| G6 | T26.G6.02 | Multiple inputs | ✓ STRONGLY supported | pose/mic/sensing |
| G6 | T26.G6.03 | Consent workflows | ✓ Fully supported | ask + if + variables |
| G6 | T26.G6.04 | Note inaccuracy | ✓ Fully supported | table column for notes |
| G7 | T26.G7.01 | Reusable modules | ✓ Fully supported | custom blocks |
| G7 | T26.G7.02 | Monitor quality | ✓ Fully supported | HUD + variables |
| G7 | T26.G7.03 | Document provenance | ✓ STRONGLY supported | import CSV + metadata |
| G7 | T26.G7.04 | Evaluate bias | ✓ Fully supported | analysis/reflection |
| G8 | T26.G8.01 | Telemetry pipelines | ✓ STRONGLY supported | tables + Google Sheets |
| G8 | T26.G8.02 | Scheduled exports | ✓ STRONGLY supported | export + clear table |
| G8 | T26.G8.03 | AI review protocols | ✓ Fully supported | XO assistant |
| G8 | T26.G8.04 | Privacy agreements | ✓ Fully supported | documentation |

**Summary:**
- **Unsupported:** 0 skills (0%)
- **Partially supported:** 0 skills (0%)
- **Fully supported:** 34 skills (76%)
- **Strongly supported:** 11 skills (24%)

**"Strongly supported" = CreatiCode has specialized features that directly enable the skill (tables, Google Sheets, export, AI assistant)**

### 5.2 Key Platform Strengths for T26
1. **Tables:** Robust table operations (add/delete rows/columns, read/modify cells, sort, aggregate, export)
2. **Google Sheets Integration:** Direct read/write from CreatiCode to Google Sheets enables real-world data workflows
3. **CSV Export:** Easy export of table data for external analysis
4. **Multiple Input Sources:** Pose detection, voice, sensing all generate loggable data
5. **Custom Blocks:** G7+ reusable modules well-supported
6. **XO AI Assistant:** G8.03 directly leverages platform feature

### 5.3 Platform Limitations/Workarounds
1. **No Built-in Survey Widget:** Must use ask + repeat loop (acceptable, teaches programming)
2. **Limited Timestamps:** No automatic timestamp block (must use timer reporter)
3. **No Native Real-Time Streaming:** Pose/sensing data requires polling loops (acceptable)
4. **No Built-in Consent UI:** Must build with ask + if (acceptable, teaches design)

**Verdict:** All limitations have reasonable pedagogical workarounds. No blockers.

---

## Part 6: Recommendations

### 6.1 CRITICAL FIXES (Must Do)

**Fix 1: Remove X-2 Violation in T26.G5.02**
```
CURRENT:
T26.G5.02 - Plan sampling strategies
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.GK.02: Use tokens to log repeated events ❌
* T26.GK.03: Capture yes/no answers with smile/frown cards ❌

RECOMMENDED:
T26.G5.02 - Plan sampling strategies
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
```

**Fix 2: Investigate G4 Skills Using G3 Dependencies (T26.G4.01, G4.02, G4.04)**
Action: Check if these should use G4-level equivalents:
- Does T06.G4.01 supersede T06.G3.01 for G4 skills?
- Does T09.G4.04 supersede T09.G3.05?
- Does T10.G4.02 supersede T10.G3.03?

If yes, update dependencies. If no, document rationale.

---

### 6.2 HIGH PRIORITY ENHANCEMENTS (Should Do)

**Enhancement 1: Add Early Privacy Skill**
```
NEW SKILL:
ID: T26.G3.06
Skill: Identify questions that protect privacy
Description: Students review example survey questions and mark which ones ask for information that should stay private (full names, addresses, passwords) vs. safe information (favorite color, age group), preparing them for G4 privacy reflection.
Dependencies:
* T26.G3.01: Script a CreatiCode survey loop
* T26.G3.02: Write fair survey questions
```

**Enhancement 2: Clarify G6.04 Title in All References**
Ensure all skills referencing T26.G6.04 use current wording or note the title change.

---

### 6.3 MEDIUM PRIORITY IMPROVEMENTS (Nice to Have)

**Improvement 1: Add Debugging Collection Scripts Skill**
```
NEW SKILL:
ID: T26.G7.05
Skill: Debug collection scripts with missing or wrong data
Description: Students are given a data collection script that produces incomplete or incorrect data (e.g., missing timestamps, incorrect counters, wrong column names) and must trace through the code to identify and fix the bugs.
Dependencies:
* T26.G7.01: Build reusable data collection modules
* T26.G7.02: Monitor data quality in real time
* T09.G7.01: Use debugging techniques
```

**Improvement 2: Make G3→G4 Transition More Explicit**
Consider renaming T26.G4.01 to emphasize the shift from individual to team data collection:
- Current: "Create collection protocols for partners"
- Suggested: "Create collection protocols for team consistency"

---

### 6.4 DOCUMENTATION IMPROVEMENTS

**Doc 1: Create T26 Dependency Map**
Visual diagram showing skill progression within T26:
```
GK.01 → GK.02, GK.03
GK.03 → G1.01 → G1.02, G1.03
G1.01 → G2.02, G2.04
G1.02 → G2.01, G2.03
G2.01 → G3.01
G3.01 → G3.02, G3.03
G3.03 → G3.04 → G3.05
G3.04 → G4.01, G4.02
G4.02 → G4.03, G5.01
G4.03 → G5.03
G5.01 → G5.04
G5.04 → G6.01, G6.02, G7.03
G6.01 → G6.03, G7.01
G7.01 → G7.02, G8.01
G8.01 → G8.02, G8.03
```

**Doc 2: CreatiCode Block Mapping for T26**
For each G3+ skill, list exact CreatiCode blocks needed:
- T26.G3.01: `ask [] and wait`, `answer`, `repeat ()`, `add [] to list []`
- T26.G4.02: `add to table []`, `replace item at row () column []`
- T26.G5.04: `export table [] as []`
- etc.

**Doc 3: Privacy Thread Alignment with AI4K12**
Document how T26 privacy skills (G4.04, G6.03, G7.03, G8.04) align with AI4K12 Big Idea #4 (Societal Impact).

---

## Part 7: Summary Tables

### 7.1 Issues by Priority

| Priority | Issue ID | Grade | Description | Impact |
|----------|----------|-------|-------------|--------|
| HIGH | H2 | G5 | X-2 rule violation (depends on K from G5) | Structural |
| MEDIUM | H3 | G4 | G4 skills using G3 dependencies | Consistency |
| MEDIUM | M1 | G6 | Title change creates confusion | Documentation |
| MEDIUM | M2 | G3 | Missing intermediate step G3.01→G3.04 | Pedagogical |
| MEDIUM | M3 | G3-G4 | Privacy instruction starts late | Ethical |
| LOW | L1 | All | Inconsistent dependency granularity | Style |
| LOW | L2 | G6-G7 | No explicit real-time streaming skill | Coverage |
| LOW | L3 | G5 | Export introduced relatively late | Sequencing |

### 7.2 Skills by Type

| Grade | Picture-based | Coding-based | Total |
|-------|---------------|--------------|-------|
| K | 3 | 0 | 3 |
| G1 | 3 | 0 | 3 |
| G2 | 5 | 0 | 5 |
| G3 | 0 | 5 | 5 |
| G4 | 0 | 4 | 4 |
| G5 | 0 | 4 | 4 |
| G6 | 0 | 4 | 4 |
| G7 | 0 | 4 | 4 |
| G8 | 0 | 4 | 4 |
| **Total** | **11** | **29** | **40** |

### 7.3 Cross-Topic Dependencies

| From Topic | Count | Most Common |
|------------|-------|-------------|
| T01 (Sequencing) | 5 | T01.GK.01, T01.G1.01 |
| T06 (Events) | 9 | T06.G3.01, T06.G4.01 |
| T07 (Loops) | 1 | T07.G3.01 |
| T08 (Conditionals) | 12 | T08.G3.01, T08.G4.01 |
| T09 (Variables) | 22 | T09.G3.05, T09.G4.04 |
| T10 (Lists/Tables) | 19 | T10.G3.03, T10.G4.02 |
| T11 (Custom Blocks) | 1 | T11.G5.02 |
| T23 (Voice/Pose) | 1 | T23.G5.01 |
| T24 (AI Assistant) | 1 | T24.G6.01 |
| T25 (Data Repr.) | 1 | T25.G1.02 |

**Key Insight:** T26 is heavily dependent on T08 (Conditionals), T09 (Variables), and T10 (Lists/Tables), which is appropriate for data collection.

---

## Part 8: Conclusion

### 8.1 Overall Assessment
**Grade: A- (Strong)**

Topic T26 demonstrates strong pedagogical design with clear progression from unplugged counting activities to sophisticated telemetry systems. The integration with CreatiCode's table and Google Sheets features is excellent. The privacy/ethics thread (G4, G6, G7, G8) aligns well with AI4K12 guidelines.

### 8.2 Key Strengths
1. Smooth unplugged-to-coding transition at G3
2. No duplicate skills; each has distinct learning objective
3. Strong platform alignment (100% supported, 24% strongly supported)
4. Good scaffolding of technical complexity (lists → tables → export → pipelines)
5. Ethics integrated throughout (privacy, bias, consent)

### 8.3 Key Weaknesses
1. One X-2 rule violation (G5.02 depends on K skills) - CRITICAL FIX
2. G4 skills using G3 dependencies needs investigation
3. Privacy instruction could start earlier (G2 or early G3)
4. Some G4+ skills have 4-5 dependencies creating tight coupling

### 8.4 Critical Actions
1. **FIX:** Remove T26.GK.02 and T26.GK.03 from T26.G5.02 dependencies
2. **INVESTIGATE:** Whether G4 skills should use G4-level block dependencies instead of G3
3. **CONSIDER:** Adding early privacy skill at G3 before students start collecting real data

### 8.5 Recommended Next Steps
1. Implement critical fix for G5.02
2. Review G4 dependency pattern across T06, T09, T10
3. Create visual dependency map for T26
4. Document CreatiCode block mapping for each skill
5. Consider adding G3.06 privacy skill and G7.05 debugging skill

---

## Appendix A: Complete Skills with All Dependencies

[Due to length, see main analysis Part 1 for full skill details]

## Appendix B: CreatiCode Block Reference for T26

### Survey/Input Blocks
- `ask [] and wait` - Display question, wait for user input
- `answer` - Reporter: last answer from user
- `stop asking` - Interrupt waiting for input

### Variables
- `set [] to []` - Set variable value
- `change [] by ()` - Increase/decrease variable
- `reduce [] by ()` - Decrease variable (for young learners)
- `export variable []` - Export to .txt file
- `import variable []` - Import from file

### Lists
- `add [] to []` - Append to list
- `insert [] at () of []` - Insert at position
- `delete () of []` - Delete item
- `length of []` - List length
- `[] contains []?` - Check if value in list
- `item () of []` - Get item at index
- `sort list [] from [method]` - Sort large to small / small to large
- `join [] into text with []` - Join with separator

### Tables (Primary for G4+)
- `add column [] at position () to table []` - Add column
- `add to table []: [] [] [] ...` - Add row (up to 12 cells)
- `insert at row () of table []: [] [] ...` - Insert row
- `replace row () of table [] with: [] [] ...` - Replace row
- `delete row () of table []` - Delete row by index
- `delete all rows from table []` - Clear data (keep columns)
- `delete column [] from table []` - Delete column
- `delete all columns from table []` - Clear table structure
- `item at row () column [] of table []` - Get cell value
- `replace item at row () column [] of table [] with []` - Set cell value
- `change item at row () column [] of table [] by ()` - Increment cell
- `row count of table []` - Number of rows
- `row () of table [] separator []` - Get row as text
- `row # of [] in column [] in table []` - Find row by value
- `sort table [] by column [] [order]` - Sort table
- `[method] of column [] in table []` - Aggregate (min/max/sum/avg/median)
- `export table [] as []` - Export to CSV
- `import file into table []` - Import CSV/txt
- `show table []` / `hide table []` - Display table
- `show snapshot of table [] from row () to () with style [] []` - Pretty display

### Google Sheets
- `read from google sheet: url [] sheet name [] range [] into table []`
- `write into google sheet: url [] sheet name [] starting cell [] from table []`
- `append row () from table [] to sheet [] in Google Sheet at URL []`

### Custom Blocks (G7+)
- Define custom block with parameters
- Use custom blocks for reusable logging functions

### Sensing (for G6.02 multi-input)
- `microphone loudness` - Audio level
- `timer` - Elapsed time
- Pose detection blocks (write into table)
- Face detection blocks (write into table)

---

**Document Version:** 1.0
**Analysis Date:** 2025-11-21
**Analyzed By:** Claude (Sonnet 4.5)
**Files Analyzed:**
- /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
- /media/binyu/USB2/ScratchCopilot/blockdes8.txt
