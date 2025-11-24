# T33 Skill Splits - Detailed Breakdowns
**Date:** 2024-11-24

This document shows EXACTLY how to split each of the 8 overly broad T33 skills into focused, teachable units.

---

## Split #1: T33.G6.06 → 3 Skills

### BEFORE (1 skill):
```
ID: T33.G6.06
Skill: Handle latency and error states in service calls
Description: Students design UI patterns (loading messages, "try again" buttons)
that respond gracefully when Cloud blocks or AI blocks take too long or fail.
They detect error states by checking for empty responses or error tokens and
provide user feedback. This skill applies to any external service call including
web fetch, Google Sheets, and AI blocks.

Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T09.G4.01: Prompt user for input and store it in a variable
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.02: Fetch web content using the fetch URL block
```

### AFTER (3 skills):

```
ID: T33.G6.06a
Skill: Display loading indicators during service calls
Description: Students create visual feedback while Cloud blocks execute. They
display "Loading..." messages, animated sprites, or progress indicators before
calling service blocks. They use "say" or text display to inform users that a
request is in progress. They understand that service calls take time and users
need to know the app is working, not frozen.

Dependencies:
* T09.G4.01: Prompt user for input and store it in a variable
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.02: Fetch web content using the fetch URL block

---

ID: T33.G6.06b
Skill: Detect and display error messages from failed calls
Description: Students check if service calls succeeded by examining returned
values. They use if-else to test for empty strings, null values, or error
indicators. They display user-friendly error messages like "Could not connect"
or "Data not found" instead of leaving the app in a broken state. They
distinguish between different failure types (network error, invalid input,
service unavailable).

Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T09.G4.01: Prompt user for input and store it in a variable
* T33.G6.05b: Check if service call succeeded
* T33.G6.06a: Display loading indicators during service calls

---

ID: T33.G6.06c
Skill: Implement "try again" retry mechanisms
Description: Students add retry functionality when service calls fail. They
create "Try Again" buttons or automatic retry logic that repeats the service
call after an error. They understand that temporary network issues may resolve
on retry. They implement limits on retry attempts to avoid infinite loops
(e.g., try maximum 3 times). They provide feedback about retry status
("Retrying... attempt 2 of 3").

Dependencies:
* T07.G4.01: Use repeat-until to loop based on a condition
* T08.G4.01: Use if-else to choose between two outcomes
* T09.G4.01: Prompt user for input and store it in a variable
* T33.G6.06b: Detect and display error messages from failed calls
```

**Rationale:** Separates three distinct concepts: indicating progress, detecting errors, and handling retries. Each is independently teachable and assessable.

---

## Split #2: T33.G7.01 → 3 Skills

### BEFORE (1 skill):
```
ID: T33.G7.01
Skill: List, add, and remove sheets in a Google Spreadsheet
Description: Students use `list all sheets in google sheet`, `add sheet`,
`remove sheet`, and `clear sheet` blocks to manage sheet structure. They create
multi-sheet workbooks for organizing different types of project data (e.g.,
player stats on one sheet, game settings on another). They check if sheets exist
before adding and handle cases where sheets may be missing. (Note: Basic sheet
clearing covered in T33.G6.05)

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.04: Write data from a table to Google Sheets
```

### AFTER (3 skills):

```
ID: T33.G7.01a
Skill: List sheets in a Google Spreadsheet
Description: Students use the `list all sheets in google sheet at URL [URL]
into list [LIST]` block to retrieve names of all sheets in a workbook. They
iterate through the list to display sheet names in their project. They check
if a specific sheet exists by searching the list before attempting to access
it. They understand that the list reflects the current structure of the Google
Sheet at the time of the call.

Block: list all sheets in google sheet at URL [SHEET_URL] into list [LIST]

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G6.03: Read data from Google Sheets into a table

---

ID: T33.G7.01b
Skill: Add new sheets to organize data
Description: Students use the `add sheet [SHEETNAME] to google sheet at URL
[URL]` block to create new sheets in a workbook. They organize different types
of data on separate sheets (e.g., "PlayerStats" for scores, "Settings" for
configuration, "History" for logs). They use T33.G7.01a to check if a sheet
already exists before adding to avoid errors. They understand that adding
sheets allows better data organization than putting everything on one sheet.

Block: add sheet [SHEETNAME] to google sheet at URL [URL]

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G6.03: Read data from Google Sheets into a table
* T33.G7.01a: List sheets in a Google Spreadsheet

---

ID: T33.G7.01c
Skill: Remove sheets dynamically
Description: Students use the `remove sheet [SHEETNAME] from google sheet at
URL [URL]` block to delete sheets from workbooks. They implement safety checks
using T33.G7.01a to confirm a sheet exists before removing it. They understand
that removing a sheet permanently deletes all data in that sheet (no undo).
They create "archive and delete" workflows that save important data elsewhere
before removing sheets. They handle cases where a sheet is already removed by
checking the sheet list first.

Block: remove sheet [SHEETNAME] from google sheet at URL [URL]

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.01a: List sheets in a Google Spreadsheet
* T33.G7.01b: Add new sheets to organize data
```

**Rationale:** Each operation (list, add, remove) is distinct and builds on the previous. Clear sheet already covered in T33.G6.05, so removed from this skill. Fixed dependency violations (G5 → G6).

---

## Split #3: T33.G7.05 → 3 Skills

### BEFORE (1 skill):
```
ID: T33.G7.05
Skill: Synchronize variables across projects using cloud sessions
Description: Students use `create cloud session` and `join cloud session` blocks
to enable real-time sharing of cloud variables across multiple instances of the
same CreatiCode project. They build collaborative features where one user's
variable changes appear instantly for others: synchronized counters, shared text
displays, collaborative drawing coordinates, or shared data dashboards. They
understand that cloud sessions synchronize ONLY cloud variables—not sprites,
physics, costumes, or game state. Each session requires a unique ID, and only
projects connected to the same session will share variables. They test isolation
by connecting to different sessions (no sync) versus the same session (full
variable sync).

Dependencies:
* T09.G5.01: Use multiple variables together in a single expression
* T31.G5.01: Trace how a device reaches an online service
* T33.G5.02: Distinguish real-time collaboration from one-time requests
* T33.G5.03: Understand that shared URLs grant public access

Note: Cloud sessions synchronize cloud variables only. For full multiplayer
games with sprite replication, physics, and collision, see Topic T19.
```

### AFTER (3 skills):

```
ID: T33.G7.05a
Skill: Understand cloud session isolation
Description: Students learn that cloud sessions create isolated groups for
variable sharing. They understand that cloud variables are shared ONLY within
projects connected to the same session ID, not globally across all projects.
They explore the concept through diagrams and scenarios: Session A members see
each other's variables but not Session B's variables. They understand that
sessions are identified by unique names/IDs and that using different IDs
creates complete isolation. They recognize this is different from regular cloud
variables (shared across all instances) and from multiplayer game rooms (which
sync sprites and physics, not just variables).

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G5.02: Distinguish real-time collaboration from one-time requests
* T33.G5.03: Understand that shared URLs grant public access

Note: Cloud sessions sync cloud variables only. For full multiplayer games,
see Topic T19 (Multiplayer).

---

ID: T33.G7.05b
Skill: Create and join cloud sessions
Description: Students use `create cloud session [SESSION]` to start a new
session and `join cloud session [SESSION]` to connect to an existing session.
They experiment with session IDs to understand isolation: two browser tabs
using the same session ID see synchronized cloud variables, while tabs using
different IDs remain isolated. They implement simple session selection UIs
where users choose or enter a session ID. They understand that one user must
create the session before others can join it.

Blocks:
- create cloud session [SESSION]
- join cloud session [SESSION]

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.05a: Understand cloud session isolation

---

ID: T33.G7.05c
Skill: Synchronize variables across session members
Description: Students build collaborative features using cloud sessions:
synchronized counters (all users see same count), shared text displays
(collaborative writing), shared coordinates (collaborative drawing), or data
dashboards (real-time updates). They mark variables as "cloud variables" so
they sync automatically within the session. They test synchronization by
running multiple instances and observing real-time updates. They understand
that ONLY cloud variables sync—not sprites, physics, costumes, or local
variables. They identify use cases for cloud sessions (collaborative counters,
shared displays) versus multiplayer blocks (games with sprite synchronization).

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.05a: Understand cloud session isolation
* T33.G7.05b: Create and join cloud sessions
```

**Rationale:** Separates conceptual understanding (isolation), technical usage (create/join), and practical application (synchronization). Fixed dependency violations (G5 → G6).

---

## Split #4: T33.G7.07 → 3 Skills

### BEFORE (1 skill):
```
ID: T33.G7.07
Skill: Build workflows that combine multiple services
Description: Learners orchestrate multi-service workflows: fetch web content →
process with AI → store results in Google Sheets, or read settings from Sheets →
generate AI content → display. They handle intermediate data and ensure each
step completes before the next begins.

Dependencies:
* T06.G5.01: Identify standard event patterns in a small game
* T09.G5.01: Use multiple variables together in a single expression
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.02: Fetch web content using the fetch URL block
* T33.G6.04: Write data from a table to Google Sheets
* T33.G6.07: Respect usage limits and rate limiting
```

### AFTER (3 skills):

```
ID: T33.G7.07a
Skill: Chain web fetch with AI processing
Description: Students build a two-step workflow: fetch web content using the
fetch URL block, then send that content to AI blocks for analysis or
summarization. They store the fetched content in a variable, verify it's not
empty, then pass it to an AI prompt. They display both the original content
and the AI's analysis. They understand that the fetch must complete before
calling the AI block. This pattern is useful for summarizing web articles,
analyzing web data, or extracting information from web pages.

Example workflow: Fetch article → AI summarizes → Display summary

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G6.02: Fetch web content using the fetch URL block
* T33.G7.06b: Call two services in sequence

---

ID: T33.G7.07b
Skill: Read from Sheets, process data, and write results
Description: Students build workflows that read data from Google Sheets,
process or transform it (calculations, AI analysis, filtering), then write
results back to Sheets. They read a table from one sheet/range, perform
operations on the data using table manipulation or AI blocks, then write the
processed results to another sheet/range. They understand that reads must
complete before processing, and processing must complete before writing.

Example workflow: Read scores → Calculate stats → Write summary table

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.04: Write data from a table to Google Sheets
* T33.G7.06b: Call two services in sequence

---

ID: T33.G7.07c
Skill: Coordinate sequential service calls with dependencies
Description: Students build workflows where each service call depends on the
previous call's results. They implement error checking between steps: if step 1
fails, skip step 2. They use variables to pass data between services and
implement progress indicators showing which step is running. They understand
the importance of sequential execution (not parallel) when later steps need
earlier results. They implement three-or-more-step workflows combining web
fetch, AI, Google Sheets, and cloud database operations.

Example workflow: Fetch data → AI analyzes → Write to Sheet → Log to collection

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G6.06b: Detect and display error messages from failed calls
* T33.G6.07: Respect usage limits and rate limiting
* T33.G7.07a: Chain web fetch with AI processing
* T33.G7.07b: Read from Sheets, process data, and write results
```

**Rationale:** Provides three specific, concrete workflow patterns instead of "any workflow." Builds from 2-step to 3+-step workflows. Fixed dependency violations (G5 → G6). Added new foundation skill T33.G7.06b as prerequisite.

---

## Split #5: T33.G7.10 → 3 Skills

### BEFORE (1 skill):
```
ID: T33.G7.10
Skill: Query cloud collections with WHERE conditions
Description: Students use `fetch from collection` with WHERE conditions to
retrieve specific records matching criteria (field > value, field = value, field
contains text). They build query expressions using `cond` blocks with comparison
operators (>, <, =, ≠, ≥, ≤) and the `contains` operator for text searches. They
create filtered data views like "scores above 100" or "users whose name contains
'Alex'" and understand that conditions filter data on the server before returning
results, making queries more efficient than fetching all data and filtering
locally.

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.10: Insert and fetch data from cloud database collections
```

### AFTER (3 skills):

```
ID: T33.G7.10a
Skill: Use simple WHERE conditions with comparison operators
Description: Students use the `cond` block with comparison operators (>, <, =,
≠, ≥, ≤) to filter collection data. They build simple single-condition queries
like "score > 100" or "level = 5" using the comparison operator menu. They use
`field [FIELDNAME]` blocks to reference collection fields on the left side and
literal values on the right side. They understand that these conditions filter
on the server, returning only matching documents. They test queries and verify
results match their conditions.

Block pattern: <cond (field [score]) [>] [100]>

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G6.10: Insert and fetch data from cloud database collections
* T33.G7.09b: Understand query field references

---

ID: T33.G7.10b
Skill: Use contains operator for text searches
Description: Students use the `cond (field [FIELDNAME]) contains [TEXT]?` block
to search for text within field values. They build queries like "name contains
'Team A'" or "description contains 'robot'" to find partial matches. They
understand that contains checks if the text appears anywhere in the field (not
just exact matches). They combine contains with string handling: searching for
lowercase versions to make searches case-insensitive. They identify use cases
for contains (search functionality, filtering by keywords, finding partial names).

Block pattern: <cond (field [name]) contains [Alex]?>

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.09b: Understand query field references
* T33.G7.10a: Use simple WHERE conditions with comparison operators

---

ID: T33.G7.10c
Skill: Compare field values in WHERE conditions
Description: Students build queries that compare two field values instead of
field-to-literal comparisons. They use constructions like (field [score]) >
(field [threshold]) to find documents where one field exceeds another. They
understand when field-to-field comparison is useful: finding records where
actual > target, start > end, or current > max. They combine field references
on both sides of comparison operators. They understand this is more dynamic
than hardcoded values.

Block pattern: <cond (field [actual]) [>] (field [target])>

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.09b: Understand query field references
* T33.G7.10a: Use simple WHERE conditions with comparison operators
```

**Rationale:** Separates three distinct query patterns: comparison operators, contains searches, and field-to-field comparisons. Fixed dependency violations (G5 → G6). Added prerequisite T33.G7.09b for field reference understanding.

---

## Split #6: T33.G7.11 → 3 Skills

### BEFORE (1 skill):
```
ID: T33.G7.11
Skill: Update and delete cloud collection data
Description: Students use `update collection from table` to modify existing
records by loading data into a table, changing values, and writing back. They
use `update collection in-place` to change specific fields matching a WHERE
condition without loading data first (efficient for simple updates). They use
`remove all documents from collection` with WHERE conditions to delete specific
records. They understand the difference between table-based updates (modify then
write back) and in-place updates (direct field changes on server) and when each
is appropriate.

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G7.10: Query cloud collections with WHERE conditions
```

### AFTER (3 skills):

```
ID: T33.G7.11a
Skill: Update collections from modified tables
Description: Students use `update collection [COLLECTIONNAME v] from table
[TABLENAME v]` to modify collection data. They fetch documents into a table,
modify values in the table using table manipulation blocks, then write the
changed table back to the collection. They understand this is a three-step
process: fetch → modify → update. They use this approach when making complex
changes to multiple fields or when changes depend on calculations. They verify
updates by fetching data again and checking values changed correctly.

Block: update collection [COLLECTIONNAME v] from table [TABLENAME v]

Pattern: fetch to table → change table values → update from table

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.10: Query cloud collections with WHERE conditions

---

ID: T33.G7.11b
Skill: Update collections in-place with WHERE conditions
Description: Students use `update collection [COLLECTIONNAME v] in-place where
<CONDITION> set (FIELD1) to (VALUE1) set (FIELD2) to (VALUE2)...` to change
specific fields directly on the server without loading the entire collection.
They build WHERE conditions to target specific documents, then set new values
for one or more fields. They understand this is more efficient than
table-based updates for simple field changes. They use this for batch updates
like "set all items with type='old' to status='archived'" or "increase all
scores above 50 by 10".

Block: update collection [COLLECTIONNAME v] in-place where <CONDITION> set...

Pattern: specify WHERE → set field values → update on server

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.10: Query cloud collections with WHERE conditions
* T33.G7.11a: Update collections from modified tables

---

ID: T33.G7.11c
Skill: Delete documents with WHERE conditions
Description: Students use `remove all documents from collection [COLLECTIONNAME
v] where <CONDITION>` to permanently delete matching documents. They build
WHERE conditions to target specific documents for deletion (e.g., "score < 10"
or "status = 'expired'"). They understand deletion is permanent with no undo.
They implement safety checks: confirm before deleting, log what will be deleted,
or create backups. They test deletion queries carefully with harmless
conditions first. They understand when to delete versus update (marking as
inactive).

Block: remove all documents from collection [COLLECTIONNAME v] where <CONDITION>

Safety pattern: fetch matching records → display list → confirm → delete

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.10: Query cloud collections with WHERE conditions
* T33.G7.11a: Update collections from modified tables
```

**Rationale:** Separates three distinct operations (table-based update, in-place update, delete) that have different use cases and patterns. Fixed dependency violations (G5 → G6).

---

## Split #7: T33.G7.12 → 3 Skills

### BEFORE (1 skill):
```
ID: T33.G7.12
Skill: Build complex collection queries with AND/OR/NOT logic
Description: Students combine multiple conditions using `cond AND`, `cond OR`,
and `cond NOT` blocks to create sophisticated queries like "scores > 100 AND
player name contains 'Team A'" or "difficulty = 'hard' OR difficulty = 'expert'".
They use `LIMIT` to retrieve top N results and `SORT BY` to order results by
field values. They build leaderboard systems, filtered search interfaces, and
data dashboards that combine multiple query criteria to find exactly the records
they need.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.10: Query cloud collections with WHERE conditions
* T33.G7.11: Update and delete cloud collection data
```

### AFTER (3 skills):

```
ID: T33.G7.12a
Skill: Combine conditions with AND and OR logic
Description: Students use `cond <> AND <>` and `cond <> OR <>` blocks to combine
multiple query conditions. They nest condition blocks: put simple conditions
inside AND/OR blocks to create compound queries. They understand AND means "both
must be true" while OR means "either can be true." They build queries like
"(score > 100) AND (level = 5)" or "(difficulty = 'hard') OR (difficulty =
'expert')". They test AND versus OR to see different result sets. They combine
multiple AND/OR blocks for complex logic like "(A AND B) OR (C AND D)".

Blocks:
- <cond <> and <>>
- <cond <> or <>>

Example: <cond <cond (field [score]) [>] [100]> AND <cond (field [level]) [=]
[5]>>

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.10: Query cloud collections with WHERE conditions

---

ID: T33.G7.12b
Skill: Use NOT to invert conditions
Description: Students use `cond not <>` blocks to invert query conditions. They
understand that NOT reverses the boolean result: "NOT(score > 100)" means "score
≤ 100". They identify use cases for NOT: finding records that DON'T match
criteria, excluding certain values, or implementing "all except" logic. They
combine NOT with AND/OR for complex exclusions like "high score AND NOT
completed" or "NOT(type = 'test' OR type = 'demo')". They understand how NOT
changes query results.

Block: <cond not <>>

Example: <cond not <cond (field [status]) [=] [archived]>>

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.10: Query cloud collections with WHERE conditions
* T33.G7.12a: Combine conditions with AND and OR logic

---

ID: T33.G7.12c
Skill: Add LIMIT and SORT BY to optimize queries
Description: Students add LIMIT and SORT BY parameters to fetch queries. They
use LIMIT to retrieve only top N results (e.g., LIMIT 10 for top 10 scores).
They use SORT BY with field names and sort orders (1=ascending, -1=descending)
to order results. They combine multiple sort fields for tie-breaking: SORT BY
score descending, then by name ascending. They understand that sorting happens
on the server before returning results. They build leaderboards using SORT BY
score descending and LIMIT 10, filtered search with SORT BY relevance, and
paginated displays.

Parameters in fetch block:
- limit (NUMBER)
- sort by (FIELD1) [ORDER1] (FIELD2) [ORDER2]

Example query: Fetch top 10 high scores, sorted by score descending

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.10: Query cloud collections with WHERE conditions
* T33.G7.12a: Combine conditions with AND and OR logic
```

**Rationale:** Separates boolean logic (AND/OR), negation (NOT), and result optimization (LIMIT/SORT). Each is independently useful and testable. Fixed dependency violation (T10.G5.01 → T10.G6.01).

---

## Split #8: T33.G8.01 → 2 Skills (OPTIONAL)

### BEFORE (1 skill):
```
ID: T33.G8.01
Skill: Insert and remove rows and columns dynamically in Google Sheets
Description: Students use `insert rows`, `insert columns`, `remove rows`, and
`remove columns` blocks to dynamically resize spreadsheet data areas. They build
data management systems that archive old data by removing rows, expand storage
by inserting new rows/columns, and reorganize datasets. This extends G7.01's
sheet-level structure management to cell-range-level manipulation.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.01: List, add, and remove sheets in a Google Spreadsheet
* T33.G7.02: Perform targeted Google Sheets cell operations
```

### OPTION 1: Keep as 1 Skill (Recommended)
**Rationale:** Rows and columns are sufficiently related and both involve the same concept (resizing data areas). Four operations total, but they pair naturally (insert/remove rows, insert/remove columns).

### OPTION 2: Split into 2 Skills

```
ID: T33.G8.01a
Skill: Insert and remove rows dynamically in Google Sheets
Description: Students use `insert [COUNT] rows at row [STARTR]` and `remove
rows [FROMR] to [TOR]` blocks to manage row structure in sheets. They insert
rows to make space for new data without overwriting existing records. They
remove rows to archive or delete old data. They build data management features:
insert row for new player, remove rows for completed games, reorganize by
inserting rows between sections. They understand row indices shift after insert/
remove operations.

Blocks:
- insert [COUNT] rows at row [STARTR] in sheet [SHEET_NAME] in Google Sheet at
URL [SHEET_URL]
- remove rows [FROMR] to [TOR] from sheet [SHEET_NAME] in Google Sheet at URL
[SHEET_URL]

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.01: List, add, and remove sheets in a Google Spreadsheet
* T33.G7.02: Perform targeted Google Sheets cell operations

---

ID: T33.G8.01b
Skill: Insert and remove columns dynamically in Google Sheets
Description: Students use `insert [COUNT] columns at column [STARTC]` and
`remove columns [FROMC] to [TOC]` blocks to manage column structure in sheets.
They insert columns to add new data fields without restructuring existing data.
They remove columns to simplify datasets or remove obsolete fields. They build
schema evolution features: add column for new attribute, remove columns for
deprecated fields, reorganize by inserting columns between existing ones. They
understand column letters shift after insert/remove operations.

Blocks:
- insert [COUNT] columns at column [STARTC] in sheet [SHEET_NAME] in Google
Sheet at URL [SHEET_URL]
- remove columns [FROMC] to [TOC] from sheet [SHEET_NAME] in Google Sheet at
URL [SHEET_URL]

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.01: List, add, and remove sheets in a Google Spreadsheet
* T33.G7.02: Perform targeted Google Sheets cell operations
* T33.G8.01a: Insert and remove rows dynamically in Google Sheets
```

**Decision:** Recommend keeping as single skill T33.G8.01 unless testing shows students struggle with understanding the difference between row and column operations.

---

## Summary of Skill Count Changes

### Before Splits:
- 8 broad skills

### After Splits:
- 8 skills → 23-24 focused skills
- Net increase: +15-16 skills

### Complete T33 Skill Count:
- Before: 36 skills total
- After: 51-52 skills total (with all splits and new foundation skills)

### By Grade:
| Grade | Before | After | Change |
|-------|--------|-------|--------|
| K-5 | 8 | 8 | +0 |
| G6 | 10 | 14 | +4 (split G6.06, add 2 new) |
| G7 | 12 | 23 | +11 (split 5 skills, add 3 new) |
| G8 | 6 | 7 | +1 (keep or split G8.01) |
| **Total** | **36** | **52** | **+16** |

---

## Implementation Notes

### When Splitting Skills:
1. **Update skill IDs** - Add letter suffixes (a, b, c)
2. **Redistribute dependencies** - First skill gets base deps, later skills depend on earlier parts
3. **Fix dependency violations** - Replace all G5 deps with G6/G7
4. **Update descriptions** - Each split skill should be independently understandable
5. **Verify block alignment** - Each skill should clearly state which blocks it uses
6. **Check scaffolding** - Ensure smooth progression between split parts

### Cross-References to Update:
- Any skill that depends on a split skill needs updating
- Assessment materials referencing split skills
- Teaching examples and project ideas
- Pacing guides and curriculum maps

### Testing Split Skills:
- Can each skill be taught in one lesson?
- Can each skill be assessed independently?
- Does the sequence make sense pedagogically?
- Are prerequisites clear and appropriate?
- Do examples align with skill scope?

---

**END OF DETAILED SKILL SPLITS**
