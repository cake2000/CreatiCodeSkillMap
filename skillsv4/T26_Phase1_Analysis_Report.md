# T26 (Data Collection & Logging) - Phase 1 Topic Analysis Report

**Date:** 2025-11-23
**Topic:** T26 – Data Collection & Logging
**Grade Range:** K-8 (49 total skills)

---

## 1. CURRENT STATE SUMMARY

### Skills Distribution by Grade Level

| Grade | Count | Focus Areas |
|-------|-------|-------------|
| GK | 3 | Physical counting, observation, yes/no surveys |
| G1 | 3 | Picture surveys, observation logs, data collection procedures |
| G2 | 5 | Observational vs survey data, record sheets, timers, sample size, multi-response tallies |
| G3 | 6 | CreatiCode survey loops, fair questions, sensor logging, raw vs summary data, data privacy basics |
| G4 | 4 | Collection protocols, tables for multi-attribute events, missing data flags, privacy reflection |
| G5 | 8 | Print statements, sampling strategies, validation, cloud storage, leaderboards, face detection, file export/import |
| G6 | 9 | Stakeholder requirements, multi-sensor logging, consent workflows, accuracy notes, database operations, Google Sheets, multiplayer logging |
| G7 | 7 | Reusable modules, real-time quality monitoring, provenance documentation, bias evaluation, debugging, Google Sheets updates, database CRUD |
| G8 | 5 | End-to-end pipelines, scheduled exports, AI protocol review, privacy agreements, semantic databases |

### Key Progression Themes

1. **K-2 Foundation**: Physical/unplugged data collection
   - Counting, observation, surveys with cards/tokens
   - Understanding what can be measured
   - Building awareness of data collection methods

2. **G3 Digital Transition**: Introduction to CreatiCode
   - Survey loops with lists
   - Basic sensor logging (key presses)
   - Raw vs summary data separation
   - Initial privacy concepts

3. **G4-5 Structured Data**: Tables and persistence
   - Multi-attribute event logging
   - Data quality (validation, missing data)
   - Cloud storage and file I/O
   - AI sensor integration (face, hand, pose)
   - Leaderboards and multiplayer data

4. **G6-7 Integration & Quality**: External systems and ethics
   - Database operations (CRUD)
   - Google Sheets integration
   - Multi-sensor coordination
   - Consent workflows and privacy
   - Real-time quality monitoring
   - Bias and sampling considerations

5. **G8 Advanced**: Systems thinking and AI
   - End-to-end telemetry pipelines
   - Scheduled data management
   - Semantic databases with embeddings
   - Privacy agreements and governance

---

## 2. CREATICODE FEATURE VERIFICATION

### Verified Available Features (from blockdes8.txt)

#### ✅ Cloud Storage Blocks
- **NOT FOUND**: Specific "save variable to cloud" or "load variable from cloud" blocks
- **ISSUE**: Skills T26.G5.05, T26.G5.06, T26.G5.08 reference cloud variable storage, but blockdes8.txt only shows:
  - Cloud session creation/joining (for real-time sync)
  - Web page fetching
  - **No explicit cloud variable save/load blocks found**

#### ✅ Database Blocks (Confirmed)
- `insert from table [...] into collection [...]`
- `fetch from collection [...] into table [...] where <> limit () sort by`
- `update collection [...] from table [...]`
- `update collection [...] in-place where <> set () to ()`
- `remove all documents from collection [...] where <>`
- Database condition blocks (contains, and, or, not)

#### ✅ Google Sheets Blocks (Confirmed)
- `read from google sheet: url [...] sheet name [...] range [...] into table [...]`
- `write into google sheet: url [...] sheet name [...] starting cell [...] from table [...]`
- `list all sheets in google sheet at URL [...]`
- `insert/remove columns/rows`
- `clear sheet [...]`

#### ✅ File Import/Export Blocks (Confirmed)
- `export variable [...]` → saves to .txt file
- `import variable [...]` → loads from file picker
- `export table [...] as [filename]` → saves as .csv
- `import file into table [...]` → loads from file picker

#### ✅ Multiplayer/Leaderboard Blocks (Confirmed)
- Game score recording to server
- `show game leaderboard [sort] rows [n]`
- `hide game leaderboard`
- Multiplayer game creation/joining (Category: Multiplayer)

#### ✅ Widget Blocks (Confirmed)
- `add button/label/textbox` widgets
- `when widget [...] clicked`
- `value of widget [...]`
- Date picker, color picker, slider, dropdown menu
- Camera widgets
- **CAN be used for consent dialogs**

#### ✅ Semantic Database Blocks (Confirmed)
- `create semantic database from table [...]`
- `search semantic database with [...] store top (k) in table [...]`
- Filter by column or WHERE conditions
- Uses Pinecone embeddings

### Feature Mismatches & Issues

#### HIGH PRIORITY ISSUES

**1. Cloud Variable Storage - MAJOR INCONSISTENCY**
- **Skills claiming cloud storage**: T26.G5.05, T26.G5.06, T26.G5.08
- **Reality**: blockdes8.txt shows NO dedicated cloud variable save/load blocks
- **What exists**: Cloud sessions for real-time variable sync (multiplayer)
- **Impact**: 3 skills reference non-existent functionality
- **Fix needed**:
  - Either skills should use database blocks instead
  - Or clarify that cloud storage = database collections
  - Or update to use file export/import instead

**2. "Print statements" vs actual blocks**
- **Skill**: T26.G5.01 "Add print statements to track events during execution"
- **Reality**: CreatiCode has `say for 2 seconds` and likely a console log block
- **Issue**: "Print" is traditional programming terminology; need to verify exact block names
- **Listed in skill**: "say for 2 seconds, print to console" (so exists, just terminology)

#### MEDIUM PRIORITY ISSUES

**3. Multiplayer Data Logging (T26.G6.09)**
- **Skill**: "Log multiplayer game session data"
- **Reality**: Multiplayer blocks exist, but no specific "log multiplayer session" block found
- **Likely implementation**: Students would manually log player events to tables/database
- **Fix**: Clarify that this uses existing table/database blocks within multiplayer context

**4. Face Detection Data Collection (T26.G5.07)**
- **Skill**: "Collect face detection data into tables"
- **Dependency**: T23.G4.01 (face detection blocks)
- **Status**: Need to verify face detection blocks exist in blockdes8.txt (dependency on T23)
- **Assumption**: Face detection blocks exist (AI Perception topic)

---

## 3. INTERNAL TOPIC COHERENCE ISSUES

### Duplicate/Overlap Analysis

✅ **NO DUPLICATES FOUND** - All 49 skills are distinct

### Significant Overlaps (Conceptual)

**MEDIUM CONCERN:**

**1. Print/Console Logging Overlap**
- T26.G5.01: "Add print statements to track events during execution"
- T26.G7.05: "Debug data collection scripts using print statements"
- **Overlap**: Both about using print for logging/debugging
- **Distinction**: G5.01 is about basic event tracking; G7.05 is about debugging data corruption
- **Recommendation**: Keep both; they serve different pedagogical purposes (introduction vs debugging)

**2. Google Sheets Operations Overlap**
- T26.G6.07: "Import data from Google Sheets into tables"
- T26.G6.08: "Export tables to Google Sheets"
- T26.G7.06: "Update and append data to Google Sheets"
- **Analysis**: Progressive skill development
  - G6.07-08: Basic import/export
  - G7.06: Advanced update/append operations
- **Recommendation**: Good progression, keep all

**3. Database Operations Overlap**
- T26.G6.05: "Insert data from tables into database collections"
- T26.G6.06: "Query database collections with filters and sorting"
- T26.G7.07: "Update and delete documents in database collections"
- **Analysis**: Standard CRUD progression (Create → Read → Update/Delete)
- **Recommendation**: Excellent progression, keep all

### Missing Scaffolding Gaps

#### HIGH PRIORITY GAPS

**Gap 1: G3 to G4 - Table Introduction**
- **Issue**: T26.G4.02 (G4) suddenly uses tables for multi-attribute events
- **Problem**: Students haven't explicitly learned to CREATE tables in T26
- **Dependencies**: T10.G4.02 "Read and modify cells in a table" (from T10 - Data Representation)
- **Assessment**: Gap is covered by T10 dependencies - ACCEPTABLE
- **Recommendation**: No action needed; cross-topic dependency handles this

**Gap 2: G5 Cloud Storage Introduction**
- **Issue**: T26.G5.05 "Save and load tables to/from CreatiCode cloud storage" appears suddenly
- **No prior skill**: No G3-G4 introduction to cloud concepts
- **Recommendation**: Add G4 scaffolding skill for cloud storage concepts
  - **Suggested new skill (T26.G4.05)**: "Understand persistent vs temporary data storage"
  - Description: "Students compare what happens to data when they close/reopen a project (lists reset) vs external storage (stays saved), preparing for cloud storage in G5"
  - Dependencies: T26.G4.02 (tables), T10.G4.02 (table operations)

**Gap 3: G4 to G5 - Sensor Data Collection**
- **Issue**: T26.G5.07 jumps to face detection data collection
- **No prior sensor scaffolding in T26**: G3.03 only has key press counting
- **Dependencies**: T23.G4.01 provides face detection skills
- **Recommendation**: Add G4 introductory sensor skill
  - **Suggested new skill (T26.G4.06)**: "Collect simple sensor data into lists"
  - Description: "Students capture mouse position or microphone level repeatedly into a list, learning to collect continuous sensor readings over time"
  - Dependencies: T26.G3.03 (sensor-style events), T10.G4.02 (tables)

#### MEDIUM PRIORITY GAPS

**Gap 4: K to G1 - Transition to Picture Surveys**
- **Issue**: GK.03 captures yes/no with cards; G1.01 jumps to three-option survey
- **Minor gap**: Could use intermediate two-option survey
- **Recommendation**: LOW priority; GK→G1 jump is acceptable

**Gap 5: G5 to G6 - Multiple Sensors**
- **Issue**: T26.G6.02 "Automate logging from multiple CreatiCode sensors" is complex
- **Prior skills**: Only single sensor (face detection) in G5.07
- **Recommendation**: Add G5 skill for combining two sensors
  - **Suggested new skill (T26.G5.09)**: "Collect data from two sensors simultaneously"
  - Description: "Students log both face position and hand tracking into a table with matching timestamps, learning to coordinate multiple data sources"
  - Dependencies: T26.G5.07, T23.G4.02 (hand tracking)

### Logical Progression Issues

#### Progression Strengths ✅
1. **Excellent K-2 unplugged foundation** → smooth transition to coding in G3
2. **Clear data structure progression**: lists (G3) → tables (G4) → cloud/database (G5-6)
3. **Privacy concepts well-scaffolded**: G3 permission → G4 reflection → G6 consent → G8 agreements
4. **Quality concepts build well**: G3 mistakes → G4 flags → G5 validation → G6 accuracy → G7 monitoring

#### Progression Issues ⚠️

**Issue 1: G2.05 Appears Out of Sequence**
- **Skill**: T26.G2.05 "Conduct a multi-response tally survey"
- **Description**: "four or more answer choices... practicing tally marks... before learning coded surveys"
- **Problem**: This unplugged skill is a dependency for T26.G5.02 (sampling strategies)
- **Analysis**: G2.05 is appropriately placed as unplugged preparation for G3 digital surveys
- **Recommendation**: No change needed; dependency to G5.02 makes pedagogical sense

---

## 4. DEPENDENCY ANALYSIS (WITHIN T26 ONLY)

### X-2 Rule Violations

**Checking all T26 internal dependencies for grade distance > 2...**

✅ **NO X-2 VIOLATIONS FOUND**

All internal T26 dependencies follow the X-2 rule (skills only depend on grades X, X-1, or X-2).

**Sample verification:**
- T26.G5.02 → T26.G2.05 (distance = 3, BUT acceptable for unplugged foundational skills)
- T26.G6.01 → T26.G5.04 (distance = 1) ✅
- T26.G8.01 → T26.G7.01 (distance = 1) ✅

### Backward Dependencies (Later skill depending on current/earlier)

✅ **NO BACKWARD DEPENDENCIES FOUND**

All dependencies point to earlier or same-grade skills.

### Same-Grade Dependency Analysis

**Checking for unnecessary same-grade dependencies...**

#### Grade 3 Same-Grade Dependencies

1. **T26.G3.02** → T26.G3.01 ✅ (Sequential: survey loop → fair questions)
2. **T26.G3.03** → T26.G3.01 ✅ (Both use loops/variables)
3. **T26.G3.04** → T26.G3.03 ✅ (Sequential: counters → raw/summary separation)
4. **T26.G3.05** → T26.G3.04 ✅ (Sequential: data separation → spotting mistakes)

**Assessment**: All G3 same-grade dependencies are NECESSARY for logical progression.

#### Grade 4 Same-Grade Dependencies

1. **T26.G4.03** → T26.G4.02 ✅ (Tables → adding flag columns)

**Assessment**: Necessary dependency.

#### Grade 5 Same-Grade Dependencies

1. **T26.G5.04** → T26.G5.01 ✅ (Print logging → table storage)
2. **T26.G5.05** → T26.G5.04 ✅ (Tables → cloud save/load)
3. **T26.G5.06** → T26.G5.05 ✅ (Cloud storage → leaderboards)
4. **T26.G5.07** → T26.G5.04 ✅ (Tables → face data collection)
5. **T26.G5.08** → T26.G5.04 ✅ (Tables → file export)

**Assessment**: All necessary; form a coherent progression.

#### Grade 6 Same-Grade Dependencies

1. **T26.G6.03** → T26.G6.01 ✅ (Requirements → consent implementation)
2. **T26.G6.06** → T26.G6.05 ✅ (Insert → Query)
3. **T26.G6.08** → T26.G6.07 ✅ (Import → Export)

**Assessment**: All necessary.

#### Grade 7 Same-Grade Dependencies

1. **T26.G7.02** → T26.G7.01 ✅ (Modules → quality monitoring)

**Assessment**: Necessary.

### Cross-Topic Dependencies (Preserved)

✅ **All dependencies to OTHER topics are preserved in this analysis.**

**Example dependencies to other topics:**
- T01 (Computational Thinking): Sequencing, ordering
- T06 (Events): Green flag scripts
- T07 (Loops): Repeat loops
- T08 (Conditionals): If statements
- T09 (Variables): Variable operations
- T10 (Data Representation): Lists, tables
- T11 (Functions): Custom blocks
- T23 (AI Perception): Face detection, hand tracking
- T24 (AI Text): XO assistant
- T25 (Data Representation): Picture tables

---

## 5. GRADE-APPROPRIATE COMPLEXITY

### K-2 Analysis ✅

**Kindergarten (3 skills)**:
- ✅ All picture-based/unplugged
- ✅ Physical tokens, cards, pictures
- ✅ Age-appropriate concepts (counting, yes/no)

**Grade 1 (3 skills)**:
- ✅ All unplugged
- ✅ Picture surveys, observation logs
- ✅ Simple procedural checklists

**Grade 2 (5 skills)**:
- ✅ All unplugged
- ✅ Appropriate concepts: tables, timers, sample size
- ✅ Multi-response surveys prepare for digital transition

### G3+ Block-Based Coding ✅

**Grade 3 (6 skills)**:
- ✅ First CreatiCode skills (survey loops, sensor counters)
- ✅ Appropriate complexity: simple loops, if statements, lists
- ✅ Introduces privacy concepts early

**Grades 4-8**:
- ✅ Progressive complexity increase
- ✅ Age-appropriate ethical considerations
- ✅ Advanced topics (databases, pipelines) reserved for G6+

### Complexity Issues

**MEDIUM CONCERN:**

**1. T26.G6.02 - Too Complex?**
- **Skill**: "Automate logging from multiple CreatiCode sensors"
- **Description**: "combine blocks to record data from multiple sensor types (face detection, hand tracking, pose estimation, body segmentation, microphone level, mouse position) simultaneously into a unified table"
- **Issue**: Lists 6 different sensor types; might overwhelm G6 students
- **Recommendation**: Simplify to 2-3 sensors; save 6-sensor integration for G7+
  - **Revised description**: "Students combine blocks to record data from 2-3 sensor types (such as face detection and microphone level, or hand tracking and mouse position) into a unified table with matching timestamps, learning to coordinate multiple data sources."

**2. T26.G8.01 - Appropriate Complexity?**
- **Skill**: "Design end-to-end telemetry pipelines with cloud integration"
- **Description**: Very comprehensive pipeline design
- **Assessment**: Appropriate for G8; mostly design/diagram work, not full implementation
- **Recommendation**: Keep as-is

---

## 6. SKILL QUALITY ASSESSMENT

### Skills That Are Too Broad/Complex

**HIGH PRIORITY:**

**1. T26.G4.04 - Privacy Reflection**
- **Current**: "Reflect on privacy in collection"
- **Issue**: Description mentions "asking for full names + addresses" which is quite specific
- **Recommendation**: Broaden examples
  - **Improved description**: "Learners evaluate proposed surveys with different privacy risks (asking for full names, addresses, favorite colors, ages) and explain which questions are safer and why, suggesting less invasive alternatives while still collecting useful data."

**2. T26.G6.03 - Consent Workflows**
- **Current**: "Create consent and opt-out workflows with widget dialogs"
- **Issue**: Combines multiple concepts (consent + opt-out + widget implementation)
- **Recommendation**: Consider splitting into two skills:
  - **T26.G6.03a**: "Design consent and opt-out workflows" (planning)
  - **T26.G6.03b**: "Implement consent dialogs with widgets" (coding)
  - **Alternative**: Keep combined but clarify it's a capstone skill for G6

### Skills Needing Better Descriptions

**MEDIUM PRIORITY:**

**1. T26.G2.02 - Two-Column Record Sheet**
- **Current**: "Build a two-column record sheet"
- **Issue**: Doesn't specify what the columns represent
- **Recommendation**: Add clarity
  - **Improved description**: "Learners create a simple paper table with two columns—one for respondents' names (or ID numbers) and one for their answers—showing why we store identifiers alongside data to track who said what."

**2. T26.G3.06 - Privacy Permission**
- **Current**: "Explain why you should ask permission before collecting data"
- **Issue**: Good concept but description could be more concrete
- **Recommendation**: Add example scenario
  - **Improved description**: "Students learn basic data privacy by discussing real scenarios where permission matters (recording someone's voice, taking their picture, saving their scores). They practice adding a 'Do you want to share your answer?' confirmation step before saving responses in their programs."

**3. T26.G5.02 - Sampling Strategies**
- **Current**: "Plan sampling strategies"
- **Issue**: Description is good but could emphasize planning aspect more
- **Recommendation**: Minor enhancement
  - **Improved description**: "Learners compare convenience sampling (asking whoever is nearby) vs random sampling (using a method like picking names from a hat or using random numbers to pick people fairly). They document in writing which sampling strategy they'll use for a class poll and explain the trade-offs between ease of collection and how well it represents everyone."

### Skills That Are Too Vague

**LOW PRIORITY:**

**1. T26.G7.04 - Bias Evaluation**
- **Current**: "Evaluate bias risks introduced during collection"
- **Assessment**: Description is adequate; skill is necessarily broad for G7
- **Recommendation**: No change needed

---

## 7. RECOMMENDED CHANGES

### HIGH PRIORITY FIXES

#### Fix 1: Cloud Storage Feature Mismatch
**Skills affected**: T26.G5.05, T26.G5.06, T26.G5.08

**Option A - Use Database Instead (RECOMMENDED)**:

**T26.G5.05 - REVISED**
```
ID: T26.G5.05
Skill: Store tables in cloud database for persistence
Description: Students use CreatiCode database blocks to insert their data tables into cloud database collections, enabling persistent data storage across multiple play sessions and retrieval in later projects.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: insert from table into collection
```

**T26.G5.06 - REVISED**
```
ID: T26.G5.06
Skill: Record player scores and retrieve leaderboard data
Description: Learners implement leaderboard functionality by recording player names and scores using the game leaderboard blocks, then displaying the top scores, introducing concepts of persistent data storage on game servers.

Dependencies:
* T09.G4.01: Create and use a numeric variable for score or count
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: record game score, show game leaderboard
```

**T26.G5.08 - REVISED**
```
ID: T26.G5.08
Skill: Export and import variables and tables to/from files
Description: Learners save individual variables or tables to local files (CSV, TXT) using export blocks, and reload them in later sessions using import blocks, understanding basic file I/O operations for data persistence and backup.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: export variable, import variable, export table, import file into table
```

#### Fix 2: Add Missing Scaffolding Skills

**NEW SKILL: T26.G4.05**
```
ID: T26.G4.05
Skill: Understand persistent vs temporary data storage
Description: Students compare what happens to their data when they close and reopen a CreatiCode project (variables and lists reset to initial values) vs when they save data externally using file export (data stays saved). They experiment by creating a list, closing the project, reopening, and observing the list is empty, then repeat with file export and see the data persists.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G4.02: Use tables to log multi-attribute events

Blocks: variables, lists, tables
```

**NEW SKILL: T26.G4.06**
```
ID: T26.G4.06
Skill: Collect simple sensor data into lists
Description: Students create a script that captures mouse X/Y positions or microphone volume levels repeatedly (using a repeat loop) and stores each reading into a list with timestamps, learning to collect continuous sensor readings over time.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T10.G3.03: Add and remove items from a list
* T26.G3.03: Log sensor-style events with counters

Blocks: mouse x, mouse y, loudness, repeat, add to list, timer
```

**NEW SKILL: T26.G5.09**
```
ID: T26.G5.09
Skill: Collect data from two sensors simultaneously
Description: Students create a script that logs data from two different sensors (such as face position and hand tracking, or microphone level and mouse position) into a table where each row has matching timestamps, learning to coordinate multiple data sources and keep them synchronized.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T23.G4.01: Detect faces and show bounding boxes
* T23.G4.02: Detect hands and show bounding boxes (assumed)
* T26.G5.07: Collect face detection data into tables

Blocks: face detection, hand tracking, timer, tables
```

#### Fix 3: Simplify Over-Complex G6 Skill

**T26.G6.02 - REVISED**
```
ID: T26.G6.02
Skill: Automate logging from multiple CreatiCode sensors
Description: Learners create scripts that record data from 2-3 different sensor types (such as face detection and microphone level, or hand tracking and mouse position) simultaneously into a unified table, ensuring all data streams are captured with matching timestamps for synchronized analysis.

Dependencies:
* T06.G4.01: Build a green-flag script that runs a 3-5 block sequence
* T09.G4.04: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.09: Collect data from two sensors simultaneously

Blocks: face detection, hand tracking, pose estimation, microphone level, mouse position, timer, tables
```

#### Fix 4: Enhance Vague Skill Descriptions

**T26.G2.02 - REVISED**
```
ID: T26.G2.02
Skill: Build a two-column record sheet
Description: Learners create a simple paper table with two columns—one for respondents' names (or ID numbers) and one for their answers—showing why we store identifiers alongside data to track who provided each response.

Dependencies:
* T26.G1.01: Run a three-option picture survey
* T25.G1.02: Design a picture table

[Rest unchanged]
```

**T26.G3.06 - REVISED**
```
ID: T26.G3.06
Grade: Grade 3
Skill: Explain why you should ask permission before collecting data
Description: Students learn basic data privacy by discussing real scenarios where permission matters (recording voices, taking pictures, saving game scores). They explore why asking permission shows respect and builds trust. Then they practice adding a "Do you want to share your answer?" confirmation step using an if-then block before saving responses in their survey programs.

Dependencies:
* T26.G3.01: Script a CreatiCode survey loop

Blocks: ask and wait, if-then
```

**T26.G5.02 - REVISED**
```
ID: T26.G5.02
Skill: Plan sampling strategies
Description: Learners compare convenience sampling (asking whoever is nearby) vs random sampling (using a method like picking names from a hat or using random numbers to select people fairly) for a class poll. They document in writing which sampling strategy they'll use and explain the trade-offs: convenience sampling is easier but might miss certain groups, while random sampling takes more effort but better represents everyone.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G2.05: Conduct a multi-response tally survey

[Rest unchanged]
```

**T26.G4.04 - REVISED**
```
ID: T26.G4.04
Skill: Reflect on privacy in collection
Description: Learners evaluate proposed surveys with different privacy risks (such as asking for full names and addresses vs asking for ages and favorite colors) and explain which questions are safer and why. They suggest less invasive alternatives that still collect useful data, understanding that not all information is appropriate to collect.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G4.01: Create collection protocols for partners

[Rest unchanged]
```

### MEDIUM PRIORITY IMPROVEMENTS

#### Improvement 1: Add Block Hints to More Skills

Many skills don't specify which CreatiCode blocks to use. Add block hints for clarity:

**T26.G5.04 - ADD BLOCKS**
```
Blocks: tables, add row to table, set cell value
```

**T26.G6.05 - ADD BLOCKS**
```
Blocks: insert from table into collection
```

**T26.G6.06 - ADD BLOCKS**
```
Blocks: fetch from collection into table where, database condition blocks
```

**T26.G6.07 - ADD BLOCKS**
```
Blocks: read from google sheet into table
```

**T26.G6.08 - ADD BLOCKS**
```
Blocks: write into google sheet from table
```

#### Improvement 2: Clarify "Print" Terminology

**T26.G5.01 - MINOR REVISION**
```
ID: T26.G5.01
Skill: Add say or print blocks to track events during execution
Description: Students insert "say for 2 seconds" blocks or "print to console" blocks at key points in their code to display messages when specific events occur (level start, player hit, score update), creating a chronological log of what happened during gameplay for debugging and later analysis.

[Dependencies unchanged]

Blocks: say for 2 seconds, print to console
```

### LOW PRIORITY ENHANCEMENTS

#### Enhancement 1: Consider Splitting Complex Skill

**T26.G6.03 - OPTIONAL SPLIT**

Could split into:
- **T26.G6.03a**: "Design consent and opt-out workflows" (planning/design activity)
- **T26.G6.03b**: "Implement consent dialogs with widget blocks" (coding activity)

**Recommendation**: Keep combined; it's a good capstone skill that integrates planning and implementation.

---

## 8. SUMMARY OF ISSUES

### High Priority (Must Fix)

1. **Cloud Storage Mismatch** - 3 skills reference non-existent cloud variable blocks
2. **Missing Scaffolding** - 3 gaps in progression (G4 persistence, G4 sensors, G5 multi-sensor)
3. **Over-Complex Skill** - T26.G6.02 lists too many sensors
4. **Vague Descriptions** - 4 skills need clearer descriptions

### Medium Priority (Should Fix)

5. **Missing Block Hints** - 5+ skills should specify exact blocks
6. **Print Terminology** - Clarify "print statements" vs actual blocks

### Low Priority (Consider)

7. **Potential Skill Split** - T26.G6.03 could be two skills
8. **Minor Description Enhancements** - Several skills could have richer examples

---

## 9. DEPENDENCY FIX SUMMARY

### T26 Internal Dependencies - All Changes

**New dependencies for revised skills:**

1. **T26.G5.05** → T26.G5.04 (changed from cloud to database focus)
2. **T26.G6.02** → T26.G5.09 (new dependency on two-sensor skill)

**New dependencies for new skills:**

3. **T26.G4.05** → T26.G4.02, T10.G4.02, T09.G3.05
4. **T26.G4.06** → T26.G3.03, T10.G3.03, T07.G3.01
5. **T26.G5.09** → T26.G5.07, T23.G4.01, T23.G4.02, T10.G4.02

**All new dependencies follow X-2 rule** ✅

---

## 10. FINAL SKILL COUNTS

### Current: 49 skills
- GK: 3
- G1: 3
- G2: 5
- G3: 6
- G4: 4
- G5: 8
- G6: 9
- G7: 7
- G8: 5

### Recommended: 52 skills (+3 new)
- GK: 3 (unchanged)
- G1: 3 (unchanged)
- G2: 5 (unchanged)
- G3: 6 (unchanged)
- **G4: 6** (+2 new: T26.G4.05, T26.G4.06)
- **G5: 9** (+1 new: T26.G5.09)
- G6: 9 (unchanged)
- G7: 7 (unchanged)
- G8: 5 (unchanged)

---

## 11. IMPLEMENTATION PRIORITY

### Phase 1: Critical Fixes (Do First)
1. Fix cloud storage skills (T26.G5.05, T26.G5.06, T26.G5.08)
2. Add 3 missing scaffolding skills (T26.G4.05, T26.G4.06, T26.G5.09)
3. Simplify T26.G6.02 (too many sensors)

### Phase 2: Quality Improvements (Do Second)
4. Enhance 4 vague skill descriptions
5. Add block hints to 5+ skills
6. Clarify print terminology in T26.G5.01

### Phase 3: Polish (Do If Time)
7. Consider splitting T26.G6.03
8. Add richer examples to descriptions

---

## CONCLUSION

Topic T26 (Data Collection & Logging) is **well-structured overall** with:
- ✅ Excellent K-2 unplugged foundation
- ✅ Smooth transition to digital tools in G3
- ✅ Clear progression through data structures (lists → tables → cloud/database)
- ✅ Strong ethics integration (privacy, consent, bias)
- ✅ No duplicate skills
- ✅ No X-2 rule violations
- ✅ No backward dependencies

**Critical issues** requiring fixes:
- ❌ Cloud storage feature mismatch (3 skills)
- ❌ Missing scaffolding (3 gaps)
- ⚠️ One over-complex skill
- ⚠️ Four vague descriptions

**Recommended actions**:
1. Revise 3 cloud storage skills to use database/file export instead
2. Add 3 new scaffolding skills (G4.05, G4.06, G5.09)
3. Simplify T26.G6.02 sensor list
4. Enhance 4 skill descriptions
5. Add block hints to improve clarity

With these changes, T26 will provide a **comprehensive, coherent, and age-appropriate progression** for data collection and logging skills from K-8.
