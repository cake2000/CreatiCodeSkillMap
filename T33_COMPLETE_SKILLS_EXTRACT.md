# T33 Complete Skills Extract - With Proposed Changes

## Current Skills (As-Is from allskills.md)

### Kindergarten

```
ID: T33.GK.01
Topic: T33 – Connected Services & Tool Wrappers
Skill: Recognize that apps can talk to helpers on the internet
Description: Using illustrated scenes, students identify apps that need the internet to work (weather apps, video streaming, voice assistants) versus apps that work offline (calculator, drawing app). They point to cloud/internet symbols and explain that some apps ask "helpers on the internet" for information or answers.

Dependencies:
(none)
```

### Grade 1

```
ID: T33.G1.01
Topic: T33 – Connected Services & Tool Wrappers
Skill: Sort apps into online helpers and offline tools
Description: Students sort picture cards of apps into two groups: those that need internet helpers (maps, search, video chat) and those that work alone (camera, clock, basic games). They explain their sorting choices using simple language like "this one asks the internet for help."

Dependencies:
* T33.GK.01: Recognize that apps can talk to helpers on the internet
```

### Grade 2

```
ID: T33.G2.01
Topic: T33 – Connected Services & Tool Wrappers
Skill: Describe what happens when an app waits for the internet
Description: Students act out or illustrate what happens when an app sends a question to the internet: waiting, getting an answer, showing results. They recognize loading spinners and understand that internet helpers need time to respond. They discuss what happens when there's no internet connection.

Dependencies:
* T33.G1.01: Sort apps into online helpers and offline tools
```

### Grade 3

```
ID: T33.G3.01
Topic: T33 – Connected Services & Tool Wrappers
Skill: Identify cloud-connected features in familiar apps
Description: Students explore familiar apps and identify which features require internet connectivity (saving to cloud, getting weather updates, translating text). They trace the flow: user action → app sends request → cloud responds → app shows result. They understand that cloud features may not work offline.

Dependencies:
* T33.G2.01: Describe what happens when an app waits for the internet
```

### Grade 4

```
ID: T33.G4.01
Topic: T33 – Connected Services & Tool Wrappers
Skill: Explain how apps store and retrieve data from the cloud
Description: Students learn that apps can save data "in the cloud" so it's available on different devices. They trace examples: saving a document on one device and opening it on another, or a game saving progress online. They understand basic cloud concepts: data travels over the internet to remote servers and back.

Dependencies:
* T31.G4.01: Identify the devices and wires in a local network
* T33.G3.01: Identify cloud-connected features in familiar apps
```

### Grade 5

```
ID: T33.G5.01
Topic: T33 – Connected Services & Tool Wrappers
Skill: Compare local storage versus cloud storage tradeoffs
Description: Students compare saving data locally (on device) versus in the cloud. They identify tradeoffs: local is faster but only on one device; cloud works across devices but needs internet. They discuss scenarios where each approach is better and understand that many apps use both methods.

Dependencies:
* T31.G5.01: Trace how a device reaches an online service
* T33.G4.01: Explain how apps store and retrieve data from the cloud
```

### Grade 6

```
ID: T33.G6.01
Topic: T33 – Connected Services & Tool Wrappers
Skill: Identify and test which blocks require internet connectivity
Description: Students experiment with CreatiCode's Cloud blocks to identify which blocks require internet connectivity and external services. They test network-dependent blocks (Google Sheets, fetch URL, AI blocks) and observe what happens when offline. They categorize blocks as local-only versus service-dependent.

Dependencies:
* T09.G4.04: Trace code with variables to predict outcomes
* T31.G5.01: Trace how a device reaches an online service
* T33.G5.01: Compare local storage versus cloud storage tradeoffs


ID: T33.G6.02
Topic: T33 – Connected Services & Tool Wrappers
Skill: Fetch web content using the fetch URL block
Description: Students use the `fetch web page as markdown from URL` block to retrieve content from a public URL and display it in their project. They learn that the block converts HTML to markdown and understand that network requests take time. They handle cases where the URL is invalid or unreachable by checking for empty results.

Block(s): p2p_fetchfromurl
Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T09.G4.01: Prompt user for input and store it in a variable
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.01: Identify which blocks require internet connectivity and external services


ID: T33.G6.03
Topic: T33 – Connected Services & Tool Wrappers
Skill: Read data from Google Sheets into a table
Description: Students use the `read from google sheet` block to load data from a shared Google Sheet into a CreatiCode table. They specify the sheet URL, sheet name, range, and target table, then iterate through the loaded data to display or process it. They understand that the sheet must be publicly accessible.

Block(s): p2p_readfromgooglesheet
Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T10.G4.01: Create a list and populate it with items
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.01: Identify which blocks require internet connectivity and external services


ID: T33.G6.04
Topic: T33 – Connected Services & Tool Wrappers
Skill: Write data from a table to Google Sheets
Description: Students use the `write into google sheet` block to export a CreatiCode table to a Google Sheet. They specify the starting cell and understand that this writes the entire table including headers. They verify successful writes by reading back the data.

Block(s): p2p_writeintogooglesheet
Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T10.G4.01: Create a list and populate it with items
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table


ID: T33.G6.04.01 [TO BE RENUMBERED → T33.G6.05]
Topic: T33 – Connected Services & Tool Wrappers
Skill: Clear a Google Sheet to reset data
Description: Students use the `clear sheet` block to remove all content from a specified sheet while keeping the sheet itself intact. They learn when clearing is preferable to deleting (preserving sheet structure and formatting). They implement a "reset data" feature in their project that clears old data before loading new data.

Block(s): p2p_clearsheet
Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.04: Write data from a table to Google Sheets


ID: T33.G6.05 [TO BE RENUMBERED → T33.G6.06]
Topic: T33 – Connected Services & Tool Wrappers
Skill: Handle latency and error states in service calls
Description: Students design UI patterns (loading messages, "try again" buttons) that respond gracefully when Cloud blocks or AI blocks take too long or fail. They detect error states by checking for empty responses or error tokens and provide user feedback. This skill applies to any external service call including web fetch, Google Sheets, and AI blocks.

Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T09.G4.01: Prompt user for input and store it in a variable
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.02: Fetch web content using the fetch URL block


ID: T33.G6.06 [TO BE RENUMBERED → T33.G6.07]
Topic: T33 – Connected Services & Tool Wrappers
Skill: Respect usage limits and rate limiting
Description: Learners implement counters and cool-down timers so projects don't spam external service blocks (AI or Cloud). They create a call counter that prevents additional requests until a timer expires, understanding that excessive calls may be blocked.

Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T09.G4.01: Prompt user for input and store it in a variable
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.05: Handle latency and error states in service calls [WILL BE T33.G6.06]
```

### Grade 7

```
ID: T33.G7.01
Topic: T33 – Connected Services & Tool Wrappers
Skill: List, add, and remove sheets in a Google Spreadsheet
Description: Students use `list all sheets in google sheet`, `add sheet`, `remove sheet`, and `clear sheet` blocks to manage sheet structure. They create multi-sheet workbooks for organizing different types of project data (e.g., player stats on one sheet, game settings on another). They check if sheets exist before adding and handle cases where sheets may be missing.

Block(s): p2p_listSheetsInGoogleSheet, p2p_addsheet, p2p_removesheet, p2p_clearsheet
Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.04: Write data from a table to Google Sheets


ID: T33.G7.02
Topic: T33 – Connected Services & Tool Wrappers
Skill: Perform targeted Google Sheets cell operations
Description: Students use `get value at row column` and `set value at row column` blocks to read and write individual cells without loading entire sheets. They build projects that update high scores or individual settings efficiently without rewriting the entire dataset.

Block(s): p2p_getvalue, p2p_setvalue
Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.04: Write data from a table to Google Sheets


ID: T33.G7.02.01 [TO BE RENUMBERED → T33.G7.03]
Topic: T33 – Connected Services & Tool Wrappers
Skill: Append rows incrementally to a Google Sheet
Description: Students use the `append row from table to sheet` block to add new records to the bottom of existing data in a Google Sheet. They build data logging features that append game scores, user actions, or sensor readings over time without overwriting previous entries. They understand the difference between appending (adding to end) and writing (replacing from a starting cell).

Block(s): p2p_appendrow
Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.04: Write data from a table to Google Sheets
* T33.G7.02: Perform targeted Google Sheets cell operations


ID: T33.G7.03 [TO BE RENUMBERED → T33.G7.04]
Topic: T33 – Connected Services & Tool Wrappers
Skill: Browse Google Drive folder contents
Description: Students use the `list content of Google Drive folder` block to get file names, IDs, and types from a shared folder. They parse the returned table to display files, filter by type, or create file browsers for their projects. The block returns metadata including filename, file ID, MIME type, and URL.

Block(s): p2p_getgooglefoldercontent
Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.05: Handle latency and error states in service calls [WILL BE T33.G6.06]


[NEW SKILL TO BE INSERTED HERE AS T33.G7.05]


ID: T33.G7.04 [TO BE RENUMBERED → T33.G7.06]
Topic: T33 – Connected Services & Tool Wrappers
Skill: Understand service authorization and keep shared URLs private
Description: Students learn that CreatiCode's Cloud and AI blocks handle authentication automatically through the platform. They understand that shared Google Sheet/Drive URLs grant access to anyone with the link and should not be publicly posted with sensitive data. They document best practices: use test data in shared sheets, avoid storing personal information, and understand that URL sharing is equivalent to granting access.

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.04: Write data from a table to Google Sheets


ID: T33.G7.05 [TO BE RENUMBERED → T33.G7.07]
Topic: T33 – Connected Services & Tool Wrappers
Skill: Build workflows that combine multiple services
Description: Learners orchestrate multi-service workflows: fetch web content → process with AI → store results in Google Sheets, or read settings from Sheets → generate AI content → display. They handle intermediate data and ensure each step completes before the next begins.

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T09.G5.01: Use multiple variables together in a single expression
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.02: Fetch web content using the fetch URL block
* T33.G6.04: Write data from a table to Google Sheets
* T33.G6.06: Respect usage limits and rate limiting [WILL BE T33.G6.07]


ID: T33.G7.06 [TO BE RENUMBERED → T33.G7.08]
Topic: T33 – Connected Services & Tool Wrappers
Skill: Compare service options and pick the right tool
Description: Students analyze requirements and select the appropriate block: Google Sheets for structured persistent data, web fetch for external content, AI blocks for generation/analysis. They justify choices based on capabilities, latency, and data format.

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.05: Handle latency and error states in service calls [WILL BE T33.G6.06]
* T33.G6.06: Respect usage limits and rate limiting [WILL BE T33.G6.07]


ID: T33.G7.07 [TO BE RENUMBERED → T33.G7.09]
Topic: T33 – Connected Services & Tool Wrappers
Skill: Cache service responses in tables to avoid redundant API calls
Description: Learners implement a caching pattern: before calling an external service, check if the same request was made recently by looking up a local table. If found, use the cached response; otherwise, make the call and store the result. This reduces service calls, improves performance, and respects rate limits. Students implement cache expiration by storing timestamps with entries and clearing old entries after a set duration (e.g., 5 minutes).

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.05: Handle latency and error states in service calls [WILL BE T33.G6.06]
```

### Grade 8

```
ID: T33.G8.01
Topic: T33 – Connected Services & Tool Wrappers
Skill: Insert and remove rows and columns dynamically in Google Sheets
Description: Students use `insert rows`, `insert columns`, `remove rows`, and `remove columns` blocks to dynamically resize spreadsheet data areas. They build data management systems that archive old data by removing rows, expand storage by inserting new rows/columns, and reorganize datasets. This extends G7.01's sheet-level structure management to cell-range-level manipulation.

Block(s): p2p_insertrowsinsheet, p2p_insertcolumnsinsheet, p2p_removerowsfromsheet, p2p_removecolumnsfromsheet
Dependencies:
* T08.G6.01: Use boolean logic to combine multiple conditions
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.01: List, add, and remove sheets in a Google Spreadsheet
* T33.G7.02: Perform targeted Google Sheets cell operations


ID: T33.G8.02
Topic: T33 – Connected Services & Tool Wrappers
Skill: Analyze legal and ethical obligations when integrating services
Description: Students read summarized terms for services (OpenAI, Google APIs) and document obligations: attribution requirements, content restrictions, data retention policies, and safety filters. They map these requirements to their project design and ensure compliance.

Dependencies:
* T08.G6.01: Use boolean logic to combine multiple conditions
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.06: Compare service options and pick the right tool [WILL BE T33.G7.08]


ID: T33.G8.03
Topic: T33 – Connected Services & Tool Wrappers
Skill: Simulate service outages and design fallbacks
Description: Learners create outage simulators that force error responses for Cloud or AI services. They design fallback experiences: offline cached data, manual input alternatives, or graceful degradation. They document incident response and recovery procedures.

Dependencies:
* T08.G6.01: Use boolean logic to combine multiple conditions
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.06: Compare service options and pick the right tool [WILL BE T33.G7.08]


ID: T33.G8.04
Topic: T33 – Connected Services & Tool Wrappers
Skill: Validate and sanitize data received from external services
Description: Students create validation logic for external service data: checking AI responses for inappropriate content, verifying data types from Google Sheets imports, confirming web fetch results are non-empty and correctly formatted. They implement logging of validation failures and create user-friendly error messages when data doesn't meet expectations.

Dependencies:
* T08.G6.01: Use boolean logic to combine multiple conditions
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.06: Compare service options and pick the right tool [WILL BE T33.G7.08]


ID: T33.G8.05
Topic: T33 – Connected Services & Tool Wrappers
Skill: Compare service-based and local implementations through hands-on testing
Description: Learners implement the same feature twice—once using a Cloud/AI service block and once using local data—then measure and compare tradeoffs: internet dependency, response time, data persistence, and offline reliability. For example, they build a quiz app that reads questions from Google Sheets versus one with hardcoded questions, then test both offline and online. They document measured differences and create a decision framework for when each approach is better.

Dependencies:
* T08.G6.01: Use boolean logic to combine multiple conditions
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.06: Compare service options and pick the right tool [WILL BE T33.G7.08]


ID: T33.G8.06
Topic: T33 – Connected Services & Tool Wrappers
Skill: Build a cloud-integrated data pipeline
Description: Students build a complete data pipeline as a capstone: fetch external data → process and transform → store in Google Sheets → use in AI calls → save AI outputs back to cloud. They handle errors at each stage, implement validation for external data, and create a dashboard showing pipeline status. This capstone integrates skills from G6 through G8 of this topic.

Dependencies:
* T08.G6.01: Use boolean logic to combine multiple conditions
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.05: Build workflows that combine multiple services [WILL BE T33.G7.07]
* T33.G8.04: Validate and sanitize data received from external services
```

---

## NEW SKILL TO BE ADDED

```
ID: T33.G7.05 (NEW)
Topic: T33 – Connected Services & Tool Wrappers
Skill: Create and join cloud sessions for real-time collaboration
Description: Students use `create cloud session` and `join cloud session` blocks to enable real-time sharing of cloud variables across multiple instances of the same project. They build multiplayer experiences or collaborative tools where changes by one user are immediately visible to others in the same session. They understand session isolation: cloud variables only sync within projects connected to the same session, and users must join an existing session after it's created. They implement session management features like creating unique session IDs, displaying current session status, and handling cases where a session doesn't exist yet.

Block(s): data_createcloudsession, data_joincloudsession
Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T09.G5.01: Use multiple variables together in a single expression
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.04: Write data from a table to Google Sheets
```

---

## Summary of Changes

### Skills to Renumber (9 total)
1. T33.G6.04.01 → T33.G6.05
2. T33.G6.05 → T33.G6.06
3. T33.G6.06 → T33.G6.07
4. T33.G7.02.01 → T33.G7.03
5. T33.G7.03 → T33.G7.04
6. T33.G7.04 → T33.G7.06
7. T33.G7.05 → T33.G7.07
8. T33.G7.06 → T33.G7.08
9. T33.G7.07 → T33.G7.09

### Skills to Add (1 total)
1. T33.G7.05 (NEW) - Cloud sessions

### Dependencies to Update (7 total)
1. T33.G6.06 (new) - update from T33.G6.05
2. T33.G6.07 (new) - update from T33.G6.05
3. T33.G7.04 (new) - update from T33.G6.05
4. T33.G7.07 (new) - update from T33.G6.06
5. T33.G7.08 (new) - update from T33.G6.05, T33.G6.06
6. T33.G7.09 (new) - update from T33.G6.05
7. T33.G8.05 - update from T33.G7.06
8. T33.G8.06 - update from T33.G7.05

### Final Count
- **Before:** 27 skills (K-8)
- **After:** 28 skills (K-8)
- **Coverage:** 17/17 blocks (100%)
