# T26 Before/After Changes - Detailed Comparison

This document shows exact changes to make to allskills.md for Topic T26.

---

## SECTION 1: NEW SKILLS TO ADD

### NEW SKILL 1: After T26.G4.04

```markdown
ID: T26.G4.05
Topic: T26 – Data Collection & Logging
Skill: Understand persistent vs temporary data storage
Description: Students compare what happens to their data when they close and reopen a CreatiCode project (variables and lists reset to initial values) vs when they save data externally using file export (data stays saved). They experiment by creating a list, closing the project, reopening, and observing the list is empty, then repeat with file export and see the data persists.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G4.02: Use tables to log multi-attribute events

Blocks: variables, lists, tables, export table, import file into table
```

### NEW SKILL 2: After T26.G4.05

```markdown
ID: T26.G4.06
Topic: T26 – Data Collection & Logging
Skill: Collect simple sensor data into lists
Description: Students create a script that captures mouse X/Y positions or microphone volume levels repeatedly (using a repeat loop) and stores each reading into a list with timestamps, learning to collect continuous sensor readings over time.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T10.G3.03: Add and remove items from a list
* T26.G3.03: Log sensor-style events with counters

Blocks: mouse x, mouse y, loudness, repeat, add to list, timer
```

### NEW SKILL 3: After T26.G5.08

```markdown
ID: T26.G5.09
Topic: T26 – Data Collection & Logging
Skill: Collect data from two sensors simultaneously
Description: Students create a script that logs data from two different sensors (such as face position and hand tracking, or microphone level and mouse position) into a table where each row has matching timestamps, learning to coordinate multiple data sources and keep them synchronized.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T23.G4.01: Detect faces and show bounding boxes
* T26.G5.07: Collect face detection data into tables

Blocks: face detection, hand tracking, microphone level, mouse position, timer, tables
```

---

## SECTION 2: SKILLS TO REPLACE

### CHANGE 1: T26.G5.05

**BEFORE:**
```markdown
ID: T26.G5.05
Topic: T26 – Data Collection & Logging
Skill: Save and load tables to/from CreatiCode cloud storage
Description: Students use CreatiCode cloud blocks to save their data tables to cloud storage and retrieve them later, enabling persistent data collection across multiple play sessions or sharing data between different projects.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export
```

**AFTER:**
```markdown
ID: T26.G5.05
Topic: T26 – Data Collection & Logging
Skill: Store tables in cloud database for persistence
Description: Students use CreatiCode database blocks to insert their data tables into cloud database collections, enabling persistent data storage across multiple play sessions and retrieval in later projects. This introduces the concept of using remote databases for data that needs to survive beyond a single session.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G4.05: Understand persistent vs temporary data storage
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: insert from table into collection, fetch from collection into table
```

### CHANGE 2: T26.G5.06

**BEFORE:**
```markdown
ID: T26.G5.06
Topic: T26 – Data Collection & Logging
Skill: Record player scores and retrieve leaderboard data
Description: Learners implement leaderboard functionality by recording player names and scores to cloud storage, then retrieving and displaying the top scores, introducing concepts of persistent data storage and basic database operations.

Dependencies:
* T09.G4.01: Create and use a numeric variable for score or count
* T10.G4.02: Read and modify cells in a table
* T26.G5.05: Save and load tables to/from CreatiCode cloud storage
```

**AFTER:**
```markdown
ID: T26.G5.06
Topic: T26 – Data Collection & Logging
Skill: Record player scores and retrieve leaderboard data
Description: Learners implement leaderboard functionality by recording player names and scores using the game leaderboard blocks, then displaying the top scores sorted by highest or lowest. This introduces concepts of persistent data storage on game servers and automatic ranking systems.

Dependencies:
* T09.G4.01: Create and use a numeric variable for score or count
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: record game score, show game leaderboard, hide game leaderboard
```

### CHANGE 3: T26.G5.08

**BEFORE:**
```markdown
ID: T26.G5.08
Topic: T26 – Data Collection & Logging
Skill: Export and import variables to/from files
Description: Learners save individual variables or lists to local files and reload them in later sessions, understanding basic file I/O operations for data persistence and backup.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G5.04: Store logs in CreatiCode tables for export
```

**AFTER:**
```markdown
ID: T26.G5.08
Topic: T26 – Data Collection & Logging
Skill: Export and import variables and tables to/from files
Description: Learners save individual variables, lists, or tables to local files (CSV for tables, TXT for variables) using export blocks, and reload them in later sessions using import blocks with a file picker dialog. This teaches basic file I/O operations for data persistence, backup, and sharing with others.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G4.05: Understand persistent vs temporary data storage
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: export variable, import variable, export table, import file into table
```

### CHANGE 4: T26.G6.02

**BEFORE:**
```markdown
ID: T26.G6.02
Topic: T26 – Data Collection & Logging
Skill: Automate logging from multiple CreatiCode sensors
Description: Learners combine blocks to record data from multiple sensor types (face detection, hand tracking, pose estimation, body segmentation, microphone level, mouse position) simultaneously into a unified table, ensuring all data streams are captured with matching timestamps for synchronized analysis.

Dependencies:
* T06.G4.01: Build a green-flag script that runs a 3-5 block sequence
* T09.G4.04: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export
```

**AFTER:**
```markdown
ID: T26.G6.02
Topic: T26 – Data Collection & Logging
Skill: Automate logging from multiple CreatiCode sensors
Description: Learners create scripts that record data from 2-3 different sensor types (such as face detection and microphone level, or hand tracking and mouse position) simultaneously into a unified table, ensuring all data streams are captured with matching timestamps for synchronized analysis. This builds on coordinating two sensors by adding complexity and more sophisticated data structures.

Dependencies:
* T06.G4.01: Build a green-flag script that runs a 3-5 block sequence
* T09.G4.04: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.09: Collect data from two sensors simultaneously

Blocks: face detection, hand tracking, pose estimation, microphone level, mouse position, timer, tables
```

### CHANGE 5: T26.G2.02

**BEFORE:**
```markdown
ID: T26.G2.02
Topic: T26 – Data Collection & Logging
Skill: Build a two-column record sheet
Description: Learners create a simple table to log respondents' names and answers, showing why we store identifiers alongside data.

Dependencies:
* T26.G1.01: Run a three-option picture survey
* T25.G1.02: Design a picture table
```

**AFTER:**
```markdown
ID: T26.G2.02
Topic: T26 – Data Collection & Logging
Skill: Build a two-column record sheet
Description: Learners create a simple paper table with two columns—one for respondents' names (or ID numbers) and one for their answers—showing why we store identifiers alongside data to track who provided each response.

Dependencies:
* T26.G1.01: Run a three-option picture survey
* T25.G1.02: Design a picture table
```

### CHANGE 6: T26.G3.06

**BEFORE:**
```markdown
ID: T26.G3.06
Topic: T26 – Data Collection & Logging
Grade: Grade 3
Skill: Explain why you should ask permission before collecting data
Description: Students learn basic data privacy by discussing why it's important to ask permission before collecting information from others (like their favorite color or game scores). They practice adding a "Do you want to share your answer?" step before saving responses.

Dependencies:
* T26.G3.01: Script a CreatiCode survey loop

Blocks: ask and wait, if-then
```

**AFTER:**
```markdown
ID: T26.G3.06
Topic: T26 – Data Collection & Logging
Grade: Grade 3
Skill: Explain why you should ask permission before collecting data
Description: Students learn basic data privacy by discussing real scenarios where permission matters (recording voices, taking pictures, saving game scores). They explore why asking permission shows respect and builds trust. Then they practice adding a "Do you want to share your answer?" confirmation step using an if-then block before saving responses in their survey programs.

Dependencies:
* T26.G3.01: Script a CreatiCode survey loop

Blocks: ask and wait, if-then
```

### CHANGE 7: T26.G5.02

**BEFORE:**
```markdown
ID: T26.G5.02
Topic: T26 – Data Collection & Logging
Skill: Plan sampling strategies
Description: Learners compare convenience sampling (asking whoever is nearby) vs random sampling (using a method to pick people fairly) for a class poll, plan and document which sampling strategy they'll use and why, explaining the trade-offs between ease of collection and representativeness.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G2.05: Conduct a multi-response tally survey
```

**AFTER:**
```markdown
ID: T26.G5.02
Topic: T26 – Data Collection & Logging
Skill: Plan sampling strategies
Description: Learners compare convenience sampling (asking whoever is nearby) vs random sampling (using a method like picking names from a hat or using random numbers to select people fairly) for a class poll. They document in writing which sampling strategy they'll use and explain the trade-offs: convenience sampling is easier but might miss certain groups, while random sampling takes more effort but better represents everyone.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G2.05: Conduct a multi-response tally survey
```

### CHANGE 8: T26.G4.04

**BEFORE:**
```markdown
ID: T26.G4.04
Topic: T26 – Data Collection & Logging
Skill: Reflect on privacy in collection
Description: Learners evaluate a proposed survey (asking for full names + addresses) and suggest safer alternatives, aligning with AI4K12 ethics.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G4.01: Create collection protocols for partners
```

**AFTER:**
```markdown
ID: T26.G4.04
Topic: T26 – Data Collection & Logging
Skill: Reflect on privacy in collection
Description: Learners evaluate proposed surveys with different privacy risks (such as asking for full names and addresses vs asking for ages and favorite colors) and explain which questions are safer and why. They suggest less invasive alternatives that still collect useful data, understanding that not all information is appropriate to collect.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G4.01: Create collection protocols for partners
```

### CHANGE 9: T26.G5.01

**BEFORE:**
```markdown
ID: T26.G5.01
Topic: T26 – Data Collection & Logging
Skill: Add print statements to track events during execution
Description: Students insert print blocks at key points in their code to display messages to the console when specific events occur (level start, player hit, score update), creating a chronological log of what happened during gameplay for debugging and later analysis.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G4.02: Use tables to log multi-attribute events
```

**AFTER:**
```markdown
ID: T26.G5.01
Topic: T26 – Data Collection & Logging
Skill: Add say or print blocks to track events during execution
Description: Students insert "say for 2 seconds" blocks or "print to console" blocks at key points in their code to display messages when specific events occur (level start, player hit, score update), creating a chronological log of what happened during gameplay for debugging and later analysis.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G4.02: Use tables to log multi-attribute events

Blocks: say for 2 seconds, print to console
```

---

## SECTION 3: ADD BLOCK HINTS TO EXISTING SKILLS

### ADD BLOCKS to T26.G5.04

**BEFORE:**
```markdown
ID: T26.G5.04
Topic: T26 – Data Collection & Logging
Skill: Store logs in CreatiCode tables for export
Description: Learners push collected events into table variables with named columns, prepping for CSV export to T27.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.01: Add print statements to track events during execution
```

**AFTER:**
```markdown
ID: T26.G5.04
Topic: T26 – Data Collection & Logging
Skill: Store logs in CreatiCode tables for export
Description: Learners push collected events into table variables with named columns, prepping for CSV export to T27.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.01: Add say or print blocks to track events during execution

Blocks: tables, add row to table, set cell value
```

### ADD BLOCKS to T26.G6.05

**BEFORE:**
```markdown
ID: T26.G6.05
Topic: T26 – Data Collection & Logging
Skill: Insert data from tables into database collections
Description: Students use CreatiCode database blocks to insert rows from their data tables into cloud database collections, learning the basics of database operations and structured data storage for larger-scale data management.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.05: Save and load tables to/from CreatiCode cloud storage
* T26.G6.01: Map stakeholder questions to data requirements
```

**AFTER:**
```markdown
ID: T26.G6.05
Topic: T26 – Data Collection & Logging
Skill: Insert data from tables into database collections
Description: Students use CreatiCode database blocks to insert rows from their data tables into cloud database collections, learning the basics of database operations and structured data storage for larger-scale data management.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.05: Store tables in cloud database for persistence
* T26.G6.01: Map stakeholder questions to data requirements

Blocks: insert from table into collection
```

### ADD BLOCKS to T26.G6.06

**BEFORE:**
```markdown
ID: T26.G6.06
Topic: T26 – Data Collection & Logging
Skill: Query database collections with filters and sorting
Description: Learners write database queries to retrieve specific subsets of collected data using filter conditions (e.g., "score > 100") and sorting criteria, understanding how to efficiently access relevant data from larger collections.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G6.05: Insert data from tables into database collections
```

**AFTER:**
```markdown
ID: T26.G6.06
Topic: T26 – Data Collection & Logging
Skill: Query database collections with filters and sorting
Description: Learners write database queries to retrieve specific subsets of collected data using filter conditions (e.g., "score > 100") and sorting criteria, understanding how to efficiently access relevant data from larger collections.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G6.05: Insert data from tables into database collections

Blocks: fetch from collection into table where, database condition blocks (>, <, =, contains, and, or, not)
```

### ADD BLOCKS to T26.G6.07

**BEFORE:**
```markdown
ID: T26.G6.07
Topic: T26 – Data Collection & Logging
Skill: Import data from Google Sheets into tables
Description: Students use Google Sheets integration blocks to pull data from shared spreadsheets into CreatiCode tables, enabling collaboration and data collection from external sources.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export
```

**AFTER:**
```markdown
ID: T26.G6.07
Topic: T26 – Data Collection & Logging
Skill: Import data from Google Sheets into tables
Description: Students use Google Sheets integration blocks to pull data from shared spreadsheets into CreatiCode tables, enabling collaboration and data collection from external sources.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: read from google sheet into table
```

### ADD BLOCKS to T26.G6.08

**BEFORE:**
```markdown
ID: T26.G6.08
Topic: T26 – Data Collection & Logging
Skill: Export tables to Google Sheets
Description: Learners push their collected data tables to Google Sheets for sharing with teammates or further analysis in spreadsheet tools, understanding data export workflows.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export
* T26.G6.07: Import data from Google Sheets into tables
```

**AFTER:**
```markdown
ID: T26.G6.08
Topic: T26 – Data Collection & Logging
Skill: Export tables to Google Sheets
Description: Learners push their collected data tables to Google Sheets for sharing with teammates or further analysis in spreadsheet tools, understanding data export workflows.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export
* T26.G6.07: Import data from Google Sheets into tables

Blocks: write into google sheet from table
```

---

## SECTION 4: UPDATE DEPENDENCY REFERENCES

Several skills reference T26.G5.05 in their dependencies. These need to be updated with the new skill name:

### Skills that depend on T26.G5.05:
- **T26.G5.06**: ALREADY updated in Change 2 above
- **T26.G6.05**: Update dependency from "T26.G5.05: Save and load tables..." to "T26.G5.05: Store tables in cloud database for persistence"

**Note**: Dependency IDs stay the same (T26.G5.05), just the description text in comments changes.

---

## SECTION 5: RENUMBER SKILLS (if needed)

With 3 new skills added:
- T26.G4.05 (new)
- T26.G4.06 (new)
- T26.G5.09 (new)

**No renumbering needed** - these are new IDs that don't conflict with existing ones.

---

## SUMMARY OF CHANGES

### New Skills: 3
- T26.G4.05: Persistent vs temporary storage
- T26.G4.06: Simple sensor data collection
- T26.G5.09: Two sensors simultaneously

### Revised Skills: 9
- T26.G5.05: Cloud storage → database
- T26.G5.06: Cloud storage → leaderboard blocks
- T26.G5.08: Add database persistence concept
- T26.G6.02: Reduce sensor count, add dependency
- T26.G2.02: Clarify description
- T26.G3.06: Add concrete examples
- T26.G5.02: Enhance description
- T26.G4.04: Broaden examples
- T26.G5.01: Clarify block names

### Block Hints Added: 5
- T26.G5.04
- T26.G6.05
- T26.G6.06
- T26.G6.07
- T26.G6.08

### Total Changes: 17
- 3 additions
- 9 revisions
- 5 block hint additions

---

## VERIFICATION CHECKLIST

After making changes, verify:

- [ ] All new skill IDs are unique
- [ ] All dependencies reference existing skills
- [ ] All block names match blockdes8.txt
- [ ] No X-2 rule violations introduced
- [ ] No backward dependencies introduced
- [ ] Skill count: 52 total (was 49, +3 new)
- [ ] Grade distribution: GK(3), G1(3), G2(5), G3(6), G4(6), G5(9), G6(9), G7(7), G8(5)
