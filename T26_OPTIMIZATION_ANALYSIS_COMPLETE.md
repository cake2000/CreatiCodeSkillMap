# T26 Data Collection & Logging - Comprehensive Optimization Analysis

**Analysis Date:** 2025-11-25
**Analyst:** Claude
**Current Skill Count:** 66 skills (K-G8)

---

## EXECUTIVE SUMMARY

This analysis identifies optimization opportunities in T26 (Data Collection & Logging) by examining:
1. Skills that are too broad and need decomposition
2. Missing skills based on CreatiCode block coverage
3. Grade-level appropriateness issues
4. Dependency problems
5. Description clarity improvements

### Key Findings:
- **21 skills need to be added** (missing block coverage)
- **8 skills need to be broken down** (too broad)
- **3 skills need description improvements** (clarity issues)
- **2 dependency corrections needed**
- **Overall grade progression is good** (K-2 unplugged, G3+ coded)

---

## 1. SKILLS THAT ARE TOO BROAD

### 1.1 T26.G4.02 - "Use tables to log multi-attribute events"

**Problem:** This skill ID appears in dependencies but is defined as TWO separate skills:
- T26.G4.02.01: Create basic tables for logging
- T26.G4.02.02: Log structured events with multiple attributes

**Solution:** Remove the parent T26.G4.02 and use only the sub-skills.

**Dependencies to fix:**
- T26.G5.01 currently depends on "T26.G4.02: Use tables to log multi-attribute events"
- Should depend on T26.G4.02.02 instead

---

### 1.2 T26.G5.04 - "Store logs in CreatiCode tables for export"

**Problem:** This is used as both a parent skill AND has a sub-skill (T26.G5.04.01: Create tables with named columns). The parent skill description overlaps with multiple concepts.

**Recommendation:** Break into more granular skills:

**SUGGESTED NEW STRUCTURE:**

```
T26.G5.04.01: Create tables with named columns (KEEP - already exists)
T26.G5.04.02: Add rows to tables with event data (NEW)
T26.G5.04.03: Read specific cells from data tables (NEW)
T26.G5.04: Store complete event logs in tables (KEEP as parent)
```

**Rationale:** Students need to learn table operations step-by-step before combining them.

---

### 1.3 T26.G6.01 - "Map stakeholder questions to data requirements"

**Problem:** This skill has ELEVEN dependencies as a prerequisite for many G6-G8 skills, suggesting it's too conceptually heavy.

**Current Description:** "Students receive stakeholder questions ('Which level is hardest?') and specify what data to collect (attempt count, completion time), aligning collection with analysis goals."

**Recommendation:** Break into sub-skills:

```
T26.G6.01.01: Identify measurable variables from questions (NEW)
T26.G6.01.02: Design data schema for stakeholder needs (NEW)
T26.G6.01: Map stakeholder questions to data requirements (KEEP as parent)
```

**Rationale:** This is a complex planning skill that involves:
1. Understanding the question
2. Identifying what to measure
3. Designing the schema
4. Mapping to collection methods

**Note:** There's already a T26.G6.01.01 ("Build compound database conditions with AND/OR") which seems misplaced. This should probably be T26.G6.06.04 or similar (database series).

---

### 1.4 T26.G8.01 - "Design end-to-end telemetry pipelines"

**Problem:** This is a massive design skill covering 6 pipeline stages. The description lists: events → validation → table storage → database insert → query → export.

**Recommendation:** Break into sub-skills for each pipeline stage:

```
T26.G8.01.01: Design event capture layer (NEW)
T26.G8.01.02: Design validation rules (NEW)
T26.G8.01.03: Design storage schema (NEW)
T26.G8.01.04: Plan database persistence strategy (NEW)
T26.G8.01.05: Design query and export workflows (NEW)
T26.G8.01: Design end-to-end telemetry pipelines (KEEP as integration skill)
```

**Note:** There's already T26.G8.01.01 ("Implement end-to-end telemetry pipeline") which should be T26.G8.01.06 (implementation after design).

---

### 1.5 T26.G5.02 - "Plan sampling strategies"

**Problem:** Description covers TWO distinct concepts:
1. Convenience vs random sampling (conceptual)
2. Implementing with random number generator (technical)

**Recommendation:** Split into:

```
T26.G5.02.01: Compare sampling methods (convenience vs random) (NEW)
T26.G5.02.02: Implement random sampling with code (NEW)
T26.G5.02: Plan sampling strategies (KEEP as parent)
```

---

### 1.6 T26.G6.02 - "Automate logging from three different sensors"

**Problem:** Jumps from "two sensors" (G5.09) to "three sensors" (G6.02) without teaching the fundamental skill of synchronizing timestamps.

**Recommendation:** Add intermediate skill:

```
T26.G5.09: Collect data from two synchronized sensors (KEEP)
T26.G6.02.01: Add timestamps to sensor data collection (NEW)
T26.G6.02.02: Collect from three sensors with timestamps (rename current G6.02)
```

---

### 1.7 T26.G7.03 - "Document provenance for external CSV datasets"

**Problem:** Description covers:
1. Importing CSV files
2. Logging metadata (source, license, date, refresh schedule)
3. Citation practices

This is THREE separate skills.

**Recommendation:** Split into:

```
T26.G7.03.01: Import external CSV datasets (NEW)
T26.G7.03.02: Document dataset metadata and provenance (NEW)
T26.G7.03.03: Practice citation and attribution (NEW)
T26.G7.03: Document provenance for external datasets (KEEP as parent)
```

---

### 1.8 T26.G8.04 - "Publish data privacy agreements for peers"

**Problem:** This is a writing/communication skill, not a data collection skill. It belongs more in ethics/society topic.

**Recommendation:** Either:
1. Move to T36 (Computing Careers/Society topic)
2. OR rename to focus on the technical implementation aspect:

```
T26.G8.04: Create privacy documentation for data collection projects
```

And split into:
```
T26.G8.04.01: List data types collected and storage locations (NEW)
T26.G8.04.02: Define access controls and deletion timelines (NEW)
T26.G8.04: Document privacy agreements for projects (KEEP as parent)
```

---

## 2. MISSING SKILLS - BLOCK COVERAGE GAPS

### 2.1 MISSING: List Operations (G3-G4)

CreatiCode has 25 list blocks, but T26 only covers basic add/remove. Missing skills:

**G4 Level (matching T25.G4.07 series):**

```
T26.G4.07.01: Export list data to text format (NEW)
Description: Students convert a list of collected responses into a joined text string using the "join items of [] with []" block, learning to serialize list data for display or file storage.
Blocks: join items of list with separator
Dependencies: T26.G3.04.01 (Store raw data in lists)

T26.G4.07.02: Parse text data into lists (NEW)
Description: Students split comma-separated or tab-separated text data into list items using "split [] by []" block, learning to import and parse text-based data formats.
Blocks: split text by delimiter
Dependencies: T26.G4.07.01

T26.G4.07.03: Search for items in collected data (NEW)
Description: Students use "item # of [value] in [list]" and "[list] contains [value]" blocks to search through collected data, finding specific responses or checking if values were recorded.
Blocks: item # of value in list, list contains value
Dependencies: T26.G3.04.01
```

---

### 2.2 MISSING: List Statistics (G5)

CreatiCode has min/max/sum/average/median blocks for lists. T26 has no skills for analyzing collected numeric data.

**G5 Level (matching T25.G5.07 series):**

```
T26.G5.10.01: Calculate basic statistics on collected data (NEW)
Description: Students use statistical blocks (min/max/sum/average of list) to compute summary statistics from collected numeric data (survey ages, game scores, sensor readings).
Blocks: min of list, max of list, sum of list, average of list
Dependencies: T26.G3.04.01 (Store raw data in lists)

T26.G5.10.02: Calculate median of collected data (NEW)
Description: Students calculate the median value from collected numeric data to understand central tendency, learning when median is more appropriate than mean.
Blocks: median of list
Dependencies: T26.G5.10.01
```

---

### 2.3 MISSING: Table Column Operations (G5)

CreatiCode has column manipulation blocks. Current skills jump to full database without teaching table columns.

**G5 Level:**

```
T26.G5.11.01: Extract column data from logs as lists (NEW)
Description: Students extract specific columns from their data tables (e.g., all timestamps, all scores) as lists using "column [name] of table" for analysis or export.
Blocks: column [name] of table (returns list)
Dependencies: T26.G5.04

T26.G5.11.02: Add columns to existing data tables (NEW)
Description: Students add new columns to tables to track additional attributes discovered during data collection (e.g., adding "player_level" column to game event logs).
Blocks: add column to table
Dependencies: T26.G5.04

T26.G5.11.03: Remove columns from data tables (NEW)
Description: Students delete unnecessary columns from data tables to simplify datasets or remove sensitive information before sharing.
Blocks: delete column from table
Dependencies: T26.G5.11.02
```

---

### 2.4 MISSING: Table Query Operations (G6)

CreatiCode has sophisticated table filtering/aggregation blocks. Current skills jump straight to database queries without teaching table-level queries.

**G6 Level (matching T25.G6.05 series):**

```
T26.G6.10.01: Find specific records in data tables (NEW)
Description: Students use "find row number where column = value" to locate specific records in their collected data, learning to query tables by condition.
Blocks: find row number where column = value
Dependencies: T26.G5.04

T26.G6.10.02: Filter table data by conditions (NEW)
Description: Students filter their data tables using lookup blocks with comparison operators (>, <, =) to analyze subsets of collected data.
Blocks: lookup rows where condition, comparison operators
Dependencies: T26.G6.10.01

T26.G6.10.03: Calculate column statistics (NEW)
Description: Students aggregate columns in their data tables (sum of scores, average of durations, max of attempts) to generate summary statistics from collected events.
Blocks: sum/average/median/max/min of column [name] in table
Dependencies: T26.G5.04
```

---

### 2.5 MISSING: Server Storage Basics (G5-G6)

CreatiCode has simple key-value server storage. Current skills jump from file export to database collections, skipping the simpler server storage.

**G5 Level:**

```
T26.G5.12.01: Save single data values to server (NEW)
Description: Students save individual collected values (high score, response count, last collection date) to server storage with unique keys, learning persistent storage basics.
Blocks: save data [value] named [key], save private data [value] named [key]
Dependencies: T26.G4.05 (file export/import)

T26.G5.12.02: Load saved data from server (NEW)
Description: Students retrieve previously saved data values from server storage, understanding data persistence across sessions.
Blocks: load data named [key]
Dependencies: T26.G5.12.01

T26.G5.12.03: Understand public vs private data visibility (NEW)
Description: Students explore the difference between public server data (visible to all users of the project) and private data (visible only to the user who saved it), learning about data access control.
Blocks: save data vs save private data
Dependencies: T26.G5.12.02
```

---

### 2.6 MISSING: Console Logging Patterns (G5)

G5.01 mentions "print statements" but doesn't teach console logging systematically.

**G5 Level:**

```
T26.G5.01.01: Log messages to console with colors (NEW - make current G5.01 more specific)
Description: Students use color-coded console logging (green for success, yellow for warnings, red for errors) to create structured logs during data collection.
Blocks: print [] in [console v] color []
Dependencies: T09.G3.05 (trace code)

T26.G5.01.02: Retrieve console log history (NEW)
Description: Students programmatically retrieve all console output using "get console log" to save debug logs or export event histories as text.
Blocks: get console log
Dependencies: T26.G5.01.01
```

---

### 2.7 MISSING: CSV Operations (G5-G6)

Current skills mention "export to CSV" but don't teach CSV format or import.

**G5-G6 Level:**

```
T26.G5.13.01: Export table data as CSV files (RENAME from current implied skill)
Description: Students export their data tables to CSV format using "export table [] as []" for sharing with spreadsheet tools or other software.
Blocks: export table as [filename]
Dependencies: T26.G5.04

T26.G6.11.01: Import CSV files into tables (NEW)
Description: Students import CSV files (from surveys, sensors, external sources) into CreatiCode tables using file import blocks, learning to work with standard data formats.
Blocks: import file into table
Dependencies: T26.G5.13.01
```

---

### 2.8 MISSING: Table Transformation (G6)

CreatiCode has sort, shuffle, copy, group, pivot blocks for tables. These are analysis operations but relate to collection workflows.

**G6 Level:**

```
T26.G6.12.01: Sort collected data by columns (NEW)
Description: Students sort their data tables by timestamp, score, or other columns to organize collected data chronologically or by value for analysis.
Blocks: sort table by column [ascending/descending]
Dependencies: T26.G5.04

T26.G6.12.02: Copy and merge data tables (NEW)
Description: Students copy data tables and append tables together to combine data collected from multiple sources or sessions.
Blocks: copy table, append table to table
Dependencies: T26.G5.04

T26.G6.12.03: Group data by categories (NEW)
Description: Students group their collected data by categorical values (player name, level, time period) to aggregate events by category.
Blocks: group table by column
Dependencies: T26.G6.12.01
```

---

### 2.9 MISSING: Leaderboard Advanced Operations (G5-G6)

Current skills only cover basic record/display. CreatiCode has more leaderboard features.

**G6 Level:**

```
T26.G6.13.01: Fetch leaderboard data into tables (NEW)
Description: Students retrieve leaderboard rankings into table format for custom analysis or display, learning to work with ranked data programmatically.
Blocks: fetch leaderboard into table
Dependencies: T26.G5.06.02

T26.G6.13.02: Query leaderboard by player (NEW)
Description: Students look up specific players' ranks and scores from the leaderboard, implementing personalized data retrieval.
Blocks: get player rank, get player score from leaderboard
Dependencies: T26.G5.06.01
```

---

### 2.10 MISSING: Multiplayer Data Collection (G6-G7)

Current G6.09 mentions multiplayer logging but doesn't teach the building blocks.

**G6 Level:**

```
T26.G6.09.01: Track player IDs in multiplayer games (NEW)
Description: Students capture and log unique player identifiers in multiplayer sessions to attribute events to specific users.
Blocks: player ID, list of players in table
Dependencies: T26.G5.04

T26.G6.09.02: Log synchronized multiplayer events (rename current G6.09)
Description: Students implement data collection in multiplayer games to track player interactions, scores, and events across multiple connected users, learning to handle concurrent data streams.
Blocks: broadcast message with parameters, receive message, add row to table
Dependencies: T26.G6.09.01
```

---

## 3. GRADE APPROPRIATENESS REVIEW

### 3.1 K-G2 (Unplugged) ✅ GOOD

All K-G2 skills are appropriately unplugged:
- GK: Physical counting, tokens, cards
- G1: Stickers, observation logs, checklists
- G2: Paper tables, timers, tally marks

**No changes needed.**

---

### 3.2 G3 (First Coding) ✅ GOOD

G3 skills use basic Scratch concepts:
- ask and wait, repeat, lists
- Simple conditionals
- Variable monitors

**Appropriate for grade level.**

---

### 3.3 G4 (Tables Introduction) ⚠️ MINOR ISSUE

**Issue:** T26.G4.06 description mentions "AI sensor" which is vague.

**Current:** "Collect data from one AI sensor (like microphone volume or mouse position)"

**Problem:** Microphone and mouse aren't "AI sensors" - they're hardware sensors.

**Fix:** Clarify description:

```
T26.G4.06: Collect data from one sensor
Description: Students practice with a single sensor (microphone volume, mouse position, or timer) by logging its values to a list ten times using a counted loop, building familiarity with continuous data collection before combining multiple sensors.
```

---

### 3.4 G5-G8 ✅ GOOD

Grade progression is appropriate:
- G5: Console logging, file I/O, statistics
- G6: Databases, Google Sheets, multi-sensor
- G7: Custom blocks, provenance, bias evaluation
- G8: End-to-end pipelines, AI integration

**No changes needed.**

---

## 4. DEPENDENCY ISSUES

### 4.1 CRITICAL: T26.G6.01.01 is Misplaced

**Problem:** T26.G6.01.01 is listed as "Build compound database conditions with AND/OR" but is used as a dependency for T26.G6.01 (its parent skill).

**Current structure:**
```
T26.G6.01: Map stakeholder questions to data requirements
└── T26.G6.01.01: Build compound database conditions with AND/OR (WRONG!)
```

**This is illogical.** G6.01.01 should be about stakeholder mapping, not database queries.

**Fix:**
```
# Rename T26.G6.01.01 to T26.G6.06.04
T26.G6.06.01: Build simple database filter conditions (exists)
T26.G6.06.02: Query database collections with filters (exists)
T26.G6.06.03: Sort database query results (exists)
T26.G6.06.04: Build compound database conditions with AND/OR (MOVE HERE from G6.01.01)
```

Then create proper G6.01 sub-skills as suggested in Section 1.3.

---

### 4.2 MINOR: T26.G4.02 Phantom Skill

**Problem:** Dependencies reference "T26.G4.02: Use tables to log multi-attribute events" but this skill doesn't exist as a standalone skill (only as .01 and .02 sub-skills).

**Found in:**
- T26.G5.01 depends on "T26.G4.02"

**Fix:** Update dependency to:
```
T26.G5.01 should depend on T26.G4.02.02 (Log structured events with multiple attributes)
```

---

### 4.3 MINOR: Circular Dependency Risk in G8.01

**Problem:** T26.G8.01 and T26.G8.01.01 have confusing numbering.

**Current:**
- T26.G8.01: Design pipelines
- T26.G8.01.01: Implement pipelines (depends on G8.01)

**This is fine, but could be clearer:**

**Recommendation:** Renumber after adding design sub-skills:
```
T26.G8.01: Design end-to-end telemetry pipelines (parent)
├── T26.G8.01.01: Design event capture layer
├── T26.G8.01.02: Design validation rules
├── T26.G8.01.03: Design storage schema
├── T26.G8.01.04: Plan database persistence
├── T26.G8.01.05: Design query and export
└── T26.G8.01.06: Implement complete telemetry pipeline (MOVE current G8.01.01 here)
```

---

## 5. SKILL DESCRIPTION IMPROVEMENTS

### 5.1 T26.G3.02 - Unclear Blocks

**Current:** "...implement it in CreatiCode using the ask block with multiple-choice buttons..."

**Problem:** CreatiCode doesn't have "multiple-choice buttons" in ask block. It has widget dialog blocks.

**Fix:**
```
Description: Learners compare two survey questions—one that suggests an answer ("Don't you love cats?") and one that is neutral ("What is your favorite pet?")—then practice writing their own fair survey question and implement it in CreatiCode using the ask block with conditional logic to handle responses.
```

---

### 5.2 T26.G5.04 - Vague "for export"

**Current:** "Store logs in CreatiCode tables for export"

**Problem:** "for export" is implied future use, not clear learning objective.

**Fix:**
```
Description: Students organize collected events into table variables with named columns (time, event, player, data), learning to structure logs in tabular format for analysis and export.
```

---

### 5.3 T26.G8.05 - Needs Prerequisites Check

**Current:** "Create and search semantic databases for AI-powered data retrieval"

**Problem:** This is an advanced AI skill that seems disconnected from data collection.

**Check:** Does this belong in T26 (Data Collection) or T24 (AI Integration)?

**Recommendation:** Keep in T26 but clarify the data collection angle:

```
Description: Students collect text data (user comments, survey responses, notes) into a semantic database using AI embeddings, then use natural language searches to retrieve semantically similar records, understanding how AI enables meaning-based data retrieval beyond exact keyword matching in data collection systems.
```

---

## 6. SUMMARY OF RECOMMENDATIONS

### 6.1 Skills to Add (21 new skills)

**G4 Level (3 skills):**
- T26.G4.07.01: Export list data to text format
- T26.G4.07.02: Parse text data into lists
- T26.G4.07.03: Search for items in collected data

**G5 Level (12 skills):**
- T26.G5.01.01: Log messages to console with colors
- T26.G5.01.02: Retrieve console log history
- T26.G5.10.01: Calculate basic statistics on collected data
- T26.G5.10.02: Calculate median of collected data
- T26.G5.11.01: Extract column data from logs as lists
- T26.G5.11.02: Add columns to existing data tables
- T26.G5.11.03: Remove columns from data tables
- T26.G5.12.01: Save single data values to server
- T26.G5.12.02: Load saved data from server
- T26.G5.12.03: Understand public vs private data visibility
- T26.G5.13.01: Export table data as CSV files

**G6 Level (8 skills):**
- T26.G6.10.01: Find specific records in data tables
- T26.G6.10.02: Filter table data by conditions
- T26.G6.10.03: Calculate column statistics
- T26.G6.11.01: Import CSV files into tables
- T26.G6.12.01: Sort collected data by columns
- T26.G6.12.02: Copy and merge data tables
- T26.G6.12.03: Group data by categories
- T26.G6.13.01: Fetch leaderboard data into tables

**Total: 21 new skills**

---

### 6.2 Skills to Break Down (8 parent skills)

1. **T26.G4.02** - Remove phantom parent, keep .01 and .02
2. **T26.G5.04** - Add .02 and .03 for row/cell operations
3. **T26.G6.01** - Add .01 and .02 for stakeholder mapping steps (move current .01 to G6.06.04)
4. **T26.G8.01** - Add .01-.05 for design stages, renumber implementation to .06
5. **T26.G5.02** - Add .01 and .02 for conceptual vs implementation
6. **T26.G6.02** - Add .01 for timestamps before .02 for three sensors
7. **T26.G7.03** - Add .01-.03 for import, metadata, citation
8. **T26.G8.04** - Add .01 and .02 for privacy documentation steps

**Total: 18 new sub-skills from decomposition**

---

### 6.3 Dependencies to Fix (2 corrections)

1. **T26.G6.01.01** - Rename to T26.G6.06.04 (compound database conditions)
2. **T26.G5.01** - Change dependency from T26.G4.02 to T26.G4.02.02

---

### 6.4 Descriptions to Improve (3 skills)

1. **T26.G3.02** - Remove "multiple-choice buttons" reference
2. **T26.G4.06** - Change "AI sensor" to "sensor"
3. **T26.G8.05** - Clarify data collection context for semantic search

---

## 7. FINAL SKILL COUNT PROJECTION

**Current:** 66 skills

**After optimization:**
- Add 21 missing skills
- Add 18 sub-skills from decomposition
- Remove 0 skills (just reorganize)

**New Total: ~105 skills**

**Distribution:**
- GK: 3 (no change)
- G1: 3 (no change)
- G2: 5 (no change)
- G3: 6 (no change)
- G4: 11 (currently 7 + 3 new + 1 clarification)
- G5: 29 (currently 9 + 12 new + 8 sub-skills)
- G6: 26 (currently 13 + 8 new + 5 sub-skills)
- G7: 11 (currently 7 + 4 sub-skills)
- G8: 11 (currently 5 + 6 sub-skills)

---

## 8. MAPPING TO CREATICODE BLOCKS

### 8.1 Blocks with NO Skills (Gaps)

**List Blocks (7 blocks with no skills):**
- `reverse list` - Could add for data reordering
- `reshuffle list` - Could add for randomization
- `set list to random numbers` - Could add for test data generation
- `for each item in list` - Could add for iteration logging
- `for each index in list` - Could add for indexed logging
- `copy list to list` - Covered by T26.G4.07 suggestions
- `append list to list` - Covered by T26.G4.07 suggestions

**Table Blocks (5 blocks with no skills):**
- `insert row at position` - Advanced, G7 level
- `replace entire row` - Advanced, G7 level
- `change cell by amount` - Advanced, G6 level
- `reshuffle table` - Could add for sampling
- `pivot table` - Advanced analysis, maybe T27 (Analysis)

**Database Blocks (all covered) ✅**

**Google Sheets Blocks (4 blocks with no skills):**
- `add sheet` - Administrative, maybe skip
- `remove sheet` - Administrative, maybe skip
- `add rows to sheet` - Could add
- `remove rows from sheet` - Could add

**Recommendation:** Focus on core data collection blocks. Advanced transformation blocks (pivot, reshuffle, etc.) may belong in T27 (Data Analysis) instead of T26 (Data Collection).

---

## 9. CROSS-TOPIC DEPENDENCIES

### 9.1 Heavy Dependencies on T25 (Data Representation)

**Good:** Students learn list/table blocks in T25, then use them for collection in T26.

**Check:** Ensure all T26 skills that use tables depend on appropriate T25 table skills:
- T25.G3.06.01.01: Create table → T26.G4.02.01
- T25.G3.06.01.02: Add row → T26.G4.02.01
- T25.G4.08.01: Add column → T26.G5.11.02
- T25.G4.09.01: Get row count → (used in many T26 skills)

**Status:** Dependencies look good overall.

---

### 9.2 Heavy Dependencies on T09 (Variables)

**Good:** Students learn variables before using them for data collection.

**Check:** All T26 skills that use counters/variables depend on T09 variable skills.

**Status:** Dependencies look good.

---

### 9.3 Dependencies on T10 (Lists & Tables)

**Issue:** T10 and T25 overlap. T26 skills depend on both.

**Recommendation:** Clarify which topic teaches which blocks:
- T10: Basic list/table operations (creation, add, remove)
- T25: Advanced operations (statistics, transformations, queries)

**Status:** Needs cross-topic review (outside scope of T26 analysis).

---

## 10. PEDAGOGICAL FLOW ANALYSIS

### 10.1 Progression from Simple to Complex ✅ GOOD

**K-G2:** Physical → Unplugged
**G3:** Basic loops and lists
**G4:** Tables for structured data
**G5:** Console logging, file persistence, statistics
**G6:** Databases, cloud storage, multi-sensor
**G7:** Reusable modules, provenance, ethics
**G8:** End-to-end pipelines, AI integration

**Flow is logical.**

---

### 10.2 Missing: Data Collection Project Workflow

**Observation:** Skills cover individual operations but don't teach complete project workflow.

**Suggestion:** Add capstone project skills at each level:

```
T26.G4.08: Complete a simple data collection project (NEW)
Description: Students plan, implement, and document a complete data collection project (survey 10 people, log to table, export to file), practicing the full workflow.

T26.G6.14: Complete a multi-sensor data collection project (NEW)
Description: Students design and implement a project that collects data from multiple sensors, stores to database, and exports to Google Sheets, demonstrating end-to-end data pipeline skills.

T26.G8.06: Complete a telemetry analytics project (NEW)
Description: Students build a complete game analytics system that collects player behavior data, validates inputs, stores to database with metadata, and generates summary reports, demonstrating professional-level data collection and logging skills.
```

**Rationale:** Capstone projects help students integrate multiple skills and see the big picture.

---

## 11. ALIGNMENT WITH AI4K12 GUIDELINES

### 11.1 Ethics & Privacy ✅ GOOD

**Skills covering ethics:**
- T26.G3.06: Basic consent
- T26.G4.04: Reflect on privacy
- T26.G6.03: Consent workflows
- T26.G7.04: Bias evaluation
- T26.G8.04: Privacy agreements

**Status:** Good coverage of AI4K12 Societal Impact big idea.

---

### 11.2 Data Representation ✅ GOOD

**Connection to AI4K12 "Representation & Reasoning":**
- Students learn structured data (tables)
- Document schemas
- Understand transformations

**Status:** Aligns well with AI4K12.

---

### 11.3 Learning & Improvement ⚠️ COULD IMPROVE

**AI4K12 "Learning from Data":**
- T26 focuses on COLLECTION
- T27 (Analysis) presumably covers learning

**Suggestion:** Add bridge skill in G7-G8:

```
T26.G8.07: Collect training data for ML models (NEW)
Description: Students design and collect labeled datasets (images with labels, text with categories) for machine learning training, understanding how data collection choices affect model performance.

Dependencies: T26.G8.01, T24.G7.01 (AI prompts)
Blocks: tables, database, file export
```

---

## 12. IMPLEMENTATION PRIORITY

### Phase 1: Critical Fixes (Do First)
1. Fix T26.G6.01.01 misplacement (move to G6.06.04)
2. Fix T26.G5.01 phantom dependency (G4.02 → G4.02.02)
3. Add missing G5 console logging sub-skills (G5.01.01, G5.01.02)
4. Add missing G5 server storage skills (G5.12.01-03)

### Phase 2: Block Coverage (Do Second)
1. Add G4 list export/parse skills (G4.07.01-03)
2. Add G5 statistics skills (G5.10.01-02)
3. Add G5 column operations (G5.11.01-03)
4. Add G6 table query skills (G6.10.01-03)

### Phase 3: Decomposition (Do Third)
1. Break down T26.G8.01 into design stages
2. Break down T26.G6.01 into stakeholder sub-skills
3. Break down T26.G7.03 into import/metadata/citation
4. Add timestamp skill before G6.02

### Phase 4: Polish (Do Last)
1. Improve descriptions (G3.02, G4.06, G8.05)
2. Add capstone project skills (G4.08, G6.14, G8.06)
3. Add ML training data collection (G8.07)
4. Review cross-topic dependencies

---

## APPENDIX A: COMPLETE NEW SKILL LIST

### New Skills to Add (21 skills)

**G4 Level:**
1. T26.G4.07.01: Export list data to text format
2. T26.G4.07.02: Parse text data into lists
3. T26.G4.07.03: Search for items in collected data

**G5 Level:**
4. T26.G5.01.01: Log messages to console with colors
5. T26.G5.01.02: Retrieve console log history
6. T26.G5.10.01: Calculate basic statistics on collected data
7. T26.G5.10.02: Calculate median of collected data
8. T26.G5.11.01: Extract column data from logs as lists
9. T26.G5.11.02: Add columns to existing data tables
10. T26.G5.11.03: Remove columns from data tables
11. T26.G5.12.01: Save single data values to server
12. T26.G5.12.02: Load saved data from server
13. T26.G5.12.03: Understand public vs private data visibility
14. T26.G5.13.01: Export table data as CSV files

**G6 Level:**
15. T26.G6.10.01: Find specific records in data tables
16. T26.G6.10.02: Filter table data by conditions
17. T26.G6.10.03: Calculate column statistics
18. T26.G6.11.01: Import CSV files into tables
19. T26.G6.12.01: Sort collected data by columns
20. T26.G6.12.02: Copy and merge data tables
21. T26.G6.12.03: Group data by categories

---

### New Sub-Skills from Decomposition (18 skills)

**G5 Level:**
1. T26.G5.02.01: Compare sampling methods
2. T26.G5.02.02: Implement random sampling with code
3. T26.G5.04.02: Add rows to tables with event data
4. T26.G5.04.03: Read specific cells from data tables

**G6 Level:**
5. T26.G6.01.01: Identify measurable variables from questions (REPLACE current G6.01.01)
6. T26.G6.01.02: Design data schema for stakeholder needs
7. T26.G6.02.01: Add timestamps to sensor data collection
8. T26.G6.06.04: Build compound database conditions with AND/OR (MOVE from G6.01.01)

**G7 Level:**
9. T26.G7.03.01: Import external CSV datasets
10. T26.G7.03.02: Document dataset metadata and provenance
11. T26.G7.03.03: Practice citation and attribution

**G8 Level:**
12. T26.G8.01.01: Design event capture layer (REPLACE current G8.01.01)
13. T26.G8.01.02: Design validation rules
14. T26.G8.01.03: Design storage schema
15. T26.G8.01.04: Plan database persistence strategy
16. T26.G8.01.05: Design query and export workflows
17. T26.G8.01.06: Implement complete telemetry pipeline (MOVE from G8.01.01)
18. T26.G8.04.01: List data types collected and storage locations

---

## APPENDIX B: SKILLS TO RENAME/REORG

1. **T26.G4.02** - Delete parent, keep .01 and .02
2. **T26.G6.01.01** - Rename to T26.G6.06.04
3. **T26.G6.02** - Rename to T26.G6.02.02, add .01
4. **T26.G8.01.01** - Rename to T26.G8.01.06, add .01-.05

---

## CONCLUSION

T26 (Data Collection & Logging) has a **solid foundation** with good grade-level progression and strong ethics coverage. However, it has significant **block coverage gaps** (21 missing skills) and some **overly broad skills** (8 needing decomposition).

**Key Recommendations:**
1. Add 21 new skills for missing block operations
2. Break down 8 broad skills into 18 sub-skills
3. Fix 2 dependency/numbering errors
4. Improve 3 skill descriptions
5. Consider adding 3 capstone project skills

**Final Optimized Count:** ~105 skills (up from 66)

This will create a comprehensive, well-scaffolded progression from kindergarten physical counting to grade 8 professional telemetry pipelines.

---

**Analysis Complete**
**Date:** 2025-11-25
**Next Steps:** Review and prioritize recommendations for implementation
