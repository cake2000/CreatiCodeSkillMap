# T33 Connected Services & Tool Wrappers - Comprehensive Issue Analysis

**Analysis Date:** 2025-11-22
**Skills Analyzed:** T33 (30 skills from K-8)
**Platform Reference:** CreatiCode actual features and blocks

---

## EXECUTIVE SUMMARY

After analyzing the current T33 skills against CreatiCode's actual platform capabilities, I identified **11 HIGH PRIORITY issues**, **7 MEDIUM PRIORITY issues**, and **8 DEPENDENCY issues** that must be addressed. The most critical finding is that T33 completely **MISSES the cloud database category** (13 blocks with collections, queries, cloud storage) - a major CreatiCode feature that has NO coverage in the current skills.

### Critical Findings:
1. **Missing Database Category** - 13 cloud database blocks (collections, queries, CRUD operations) not covered
2. **Cloud Sessions vs Multiplayer Confusion** - Skills conflate two distinct systems
3. **Missing URL-based Media Loading** - No coverage of loading images/sounds from URLs
4. **Conceptual Misalignment** - "Tool Wrappers" framing doesn't match CreatiCode's architecture

---

## HIGH PRIORITY ISSUES (Must Fix)

### 1. MISSING CRITICAL SKILLS - Cloud Database Category ⚠️⚠️⚠️

**Issue Type:** Missing Coverage
**Priority:** CRITICAL
**Affected:** Entire topic (no skills cover this)

**Problem:**
CreatiCode has an entire **Database category** with 13 blocks for cloud database operations:
- `database_find_from_collection` - Query with WHERE/ORDER/LIMIT
- `database_insert_from_table` - Insert table data into collection
- `database_update_collection` - Update collection from modified table
- `database_update_collection_in_place` - Direct WHERE-based updates
- `database_remove_all_document` - Delete documents matching condition
- `database_collection` - Get collection definition
- Query builders: `database_query`, `database_operator`, `database_contains`, `database_collectionfield`, `database_not`, `database_and`, `database_or`

These enable **persistent cloud storage with query capabilities** - far more powerful than Google Sheets for structured data. This is a **major feature** with zero coverage in T33.

**Recommended Fix:**
Add 4-5 new skills across G6-G8:
- **G6:** Introduction to cloud collections (create, basic insert/find)
- **G7:** Query building with conditions (WHERE clauses, ordering, limiting)
- **G7:** Update and delete operations
- **G8:** Advanced queries (AND/OR logic, computed fields, complex conditions)
- **G8:** Collection design and schema planning

**Educational Value:**
This introduces students to:
- NoSQL database concepts
- Query languages (WHERE, ORDER BY, LIMIT)
- CRUD operations (Create, Read, Update, Delete)
- Data persistence and retrieval
- Structured data modeling

---

### 2. MISSING CRITICAL SKILLS - URL-Based Media Loading

**Issue Type:** Missing Coverage
**Priority:** HIGH
**Affected:** Entire topic

**Problem:**
CreatiCode supports loading images and sounds from URLs (mentioned in documentation as a cloud feature), but T33 has NO skills covering this. This is distinct from:
- `p2p_fetchfromurl` (fetches text/markdown content) - COVERED in T33.G6.02
- Loading media assets directly from web URLs - NOT COVERED

**Recommended Fix:**
Add new skill at G6:
- **T33.G6.XX:** "Load media from URLs into projects"
  - Description: Students use blocks to load images from public URLs as costumes/backdrops, and sounds from URLs as audio clips. They understand URL requirements (public accessibility, format compatibility). They handle loading failures gracefully.
  - Prerequisites: T31.G5.01 (networking), T33.G6.01 (Cloud blocks intro)

---

### 3. INACCURATE SKILL - Cloud Sessions Conflated with Multiplayer

**Issue Type:** Conceptual Error
**Priority:** HIGH
**Affected:** T33.G7.05, T33.G5.02

**Problem:**
**T33.G7.05** describes cloud sessions as "real-time variable synchronization" for "collaborative features" and "multiplayer experiences." This is **MISLEADING** because:

1. **Cloud Sessions** (`data_createcloudsession`, `data_joincloudsession`) synchronize VARIABLES ONLY - simple data sharing
2. **Multiplayer Games** (Topic T19, `mp_creategame`, `mp_joingame`) are a COMPLETELY DIFFERENT system with:
   - Sprite replication across players
   - Physics synchronization
   - Collision detection across network
   - Game rooms with hosts and clients
   - Full game state management

**Current T33.G7.05 Description Issues:**
- Says "multiplayer experiences" - WRONG, that's T19
- Says "collaborative tools" - Too vague, conflates with multiplayer
- Doesn't clarify the LIMITED scope (variables only, no sprites/physics)
- Note says "For full multiplayer games... see Topic T19" - This is GOOD but description contradicts it

**T33.G5.02 Issues:**
- Title: "Recognize apps that share data in real-time"
- Description mixes collaborative apps (Google Docs), multiplayer games, and one-way requests
- Too conceptual, doesn't prepare for EITHER cloud sessions OR multiplayer
- Should focus on cloud variable concepts, not multiplayer games

**Recommended Fix:**

**Rewrite T33.G5.02:**
```
ID: T33.G5.02
Skill: Understand cloud-synced variables vs local variables
Description: Students learn that cloud variables can be shared across multiple instances of the same project running on different devices, while local variables exist only on one device. They identify scenarios where cloud variables are useful (shared counters, collaborative data displays) versus where local variables are sufficient (player's own score, temporary calculations). They understand that cloud variables require internet and sync in real-time across connected instances. They distinguish this from multiplayer games which synchronize entire game states including sprites and physics.

Dependencies:
* T31.G5.01: Trace how a device reaches an online service
* T33.G5.01: Compare local storage versus cloud storage tradeoffs
```

**Rewrite T33.G7.05:**
```
ID: T33.G7.05
Skill: Create and join cloud sessions for variable synchronization
Description: Students use `create cloud session` and `join cloud session` blocks to enable real-time sharing of CLOUD VARIABLES across multiple instances of the same project. They understand session isolation: only projects in the same session share cloud variables. They build simple collaborative data tools (shared counter that all users can increment, collaborative text display, synchronized color picker) where variable changes by one user appear instantly for all session members. They understand cloud sessions synchronize VARIABLES ONLY - not sprites, positions, physics, or game logic. They implement session management (creating unique session IDs, displaying session status, handling non-existent sessions).

Block(s): data_createcloudsession, data_joincloudsession

Dependencies:
* T09.G5.01: Use multiple variables together in a single expression
* T31.G5.01: Trace how a device reaches an online service
* T33.G5.02: Understand cloud-synced variables vs local variables

Note: Cloud sessions sync variables only. For full multiplayer games with sprite replication, physics, and collision detection across network, see Topic T19 Multiplayer blocks.
```

---

### 4. TOO BROAD SKILL - T33.G6.01 Tries to Cover Too Much

**Issue Type:** Scope Too Large
**Priority:** HIGH
**Affected:** T33.G6.01

**Problem:**
T33.G6.01 tries to cover:
- Identifying which Cloud blocks need internet
- Testing blocks offline
- Understanding data flow (read-only, write-only, bidirectional)
- Categorizing by service (Google APIs, web servers)
- Creating reference charts
- References AI blocks (but says "see T32") and Multiplayer (but says "see T19")

This is trying to be an introduction to THREE different topics (Cloud, AI, Multiplayer) simultaneously while also teaching testing methodology and data flow analysis.

**Recommended Fix:**
**Narrow to Cloud category only:**
```
ID: T33.G6.01
Skill: Identify and test Cloud blocks for network dependencies
Description: Students examine CreatiCode's Cloud category blocks and identify which require internet connectivity: Google Sheets operations (read, write, manage sheets/cells/rows/columns), web fetch (URL content retrieval), Google Drive access (folder browsing), and cloud database operations (collections, queries). They test these blocks offline to observe error states and understand the difference between blocks that work entirely locally (math, motion, looks) versus blocks requiring external services. They create a simple reference chart documenting which Cloud blocks need internet and what services they connect to (Google APIs, web servers, cloud database). They understand basic error handling: checking for empty responses when network is unavailable.

Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T09.G4.04: Trace code with variables to predict outcomes
* T31.G5.01: Trace how a device reaches an online service
* T33.G5.01: Compare local storage versus cloud storage tradeoffs

Note: For AI blocks, see Topic T32. For Multiplayer game blocks, see Topic T19. This skill focuses on Cloud category service blocks only.
```

**Rationale:**
- Removes AI/Multiplayer references from main description
- Adds database operations (currently missing)
- Simplifies data flow analysis (removed "bidirectional" categorization - too advanced for G6.01)
- Keeps testing methodology but makes it practical
- Clear scope: Cloud category only

---

### 5. MISSING SKILL - Cell Operations Missing Before Append Row

**Issue Type:** Missing Prerequisite
**Priority:** HIGH
**Affected:** T33.G7.02, T33.G7.03

**Problem:**
**T33.G7.03** (Append rows) depends on **T33.G7.02** (Get/set cell values), which makes sense pedagogically. However, there's a gap:
- Students learn bulk operations first (G6.03 read range, G6.04 write table)
- Then jump to individual cell operations (G7.02)
- No transition skill explaining when/why to use cell operations vs bulk

**Also:** The block coverage is incomplete:
- `p2p_getvalue` - get value at row/column ✓ COVERED (G7.02)
- `p2p_setvalue` - set value at row/column ✓ COVERED (G7.02)
- `p2p_appendrow` - append row from table ✓ COVERED (G7.03)

But this is the ONLY coverage of targeted operations. Students don't understand the tradeoff:
- When to read whole sheet vs single cell
- When to write whole table vs update one cell
- Performance implications

**Recommended Fix:**
Keep T33.G7.02 but enhance the description to explain tradeoffs:
```
ID: T33.G7.02
Skill: Perform targeted Google Sheets cell operations
Description: Students use `get value at row column` and `set value at row column` blocks to read and write individual cells without loading entire sheets. They understand when targeted operations are better: updating a high score (1 cell) vs reading whole leaderboard (entire range), or setting a user preference (1 cell) vs initializing all settings (full table). They build projects that update individual values efficiently (high score updater, settings manager, cell-based calculator). They compare performance: reading 1 cell from a 100-row sheet vs reading all 100 rows when only 1 value needed.

Block(s): p2p_getvalue, p2p_setvalue

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.04: Write data from a table to Google Sheets
```

**Rationale:**
- Adds explicit tradeoff analysis (targeted vs bulk)
- Gives concrete examples when each approach is better
- Introduces performance thinking (important for cloud services)

---

### 6. POOR PROGRESSION - Privacy Skill Appears Too Late

**Issue Type:** Grade Level Misplacement
**Priority:** HIGH
**Affected:** T33.G6.08

**Problem:**
**T33.G6.08** "Understand privacy implications of shared Google Sheet URLs" appears in G6, AFTER students have already:
- Started using Google Sheets (G6.03, G6.04)
- Written data to sheets (G6.04)
- Shared URLs in their projects (implied by G6.03-G6.04)

Students should understand privacy BEFORE they start putting data in shared sheets, not after.

**Also:** The current G6.08 is very specific to Google Sheets, but privacy concerns apply to:
- Cloud database (students will share collection access)
- Google Drive (shared folder URLs)
- Web fetch (URLs in code visible to anyone)

**Recommended Fix:**
**Move and broaden the scope:**

**Option A:** Move to G5 as conceptual foundation:
```
ID: T33.G5.03 (NEW)
Skill: Understand privacy in shared online data
Description: Students learn that data stored "in the cloud" and accessed via URLs can be seen by anyone who has the URL. They understand that sharing a project that contains a Google Sheet URL, cloud database collection name, or web URL means giving everyone who sees that project access to that data. They practice creating "safe" test datasets with fictional information (fake names, made-up numbers) for learning projects. They identify what types of data should NEVER be in shared cloud storage (real names, addresses, phone numbers, passwords). They understand that "sharing the URL = sharing the data."

Dependencies:
* T31.G5.01: Trace how a device reaches an online service
* T33.G5.01: Compare local storage versus cloud storage tradeoffs
```

**Then update G6.08:**
```
ID: T33.G6.08
Skill: Apply privacy practices when using Google Sheets
Description: Students apply privacy principles to Google Sheets integration. Before creating a project with shared sheets, they create test datasets with fictional data. They verify that their Google Sheets are set to "Anyone with the link can edit/view" (required for CreatiCode access) and understand this means the sheet is effectively public. They document which sheets contain real versus test data and use separate sheets for learning projects versus personal data. They implement safety checks: avoiding hardcoded personal data in projects, using generic column headers, creating "demo mode" that uses sample data.

Dependencies:
* T31.G5.01: Trace how a device reaches an online service
* T33.G5.03: Understand privacy in shared online data (NEW)
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.04: Write data from a table to Google Sheets
```

**Rationale:**
- Privacy foundation comes BEFORE first data sharing (G5 before G6)
- G5.03 is broad (applies to all cloud services)
- G6.08 is specific application to Google Sheets
- Students can't accidentally share sensitive data because they learned safety first

---

### 7. INACCURATE SKILL - "Tool Wrappers" Framing is Wrong

**Issue Type:** Conceptual Misalignment
**Priority:** MEDIUM-HIGH
**Affected:** Entire topic title and framing

**Problem:**
The topic is titled **"T33 – Connected Services & Tool Wrappers"** but:
1. CreatiCode doesn't use "wrapper" terminology in its documentation
2. "Tool Wrappers" suggests a technical implementation detail (wrapping APIs)
3. Students won't understand what a "wrapper" is
4. The actual content is about **cloud services integration** and **external data sources**

**Current framing issues:**
- K-2 skills use generic "apps talk to internet helpers" (good for age)
- G3-G5 transition to "cloud-connected features" (appropriate)
- G6-G8 dive into specific blocks (Google Sheets, web fetch, database, cloud sessions)

The "Tool Wrappers" part of the title never appears in the skills themselves - it's just the topic label.

**Recommended Fix:**
**Option 1 (Minimal Change):** Keep "Connected Services" only:
```
T33 – Connected Services
```

**Option 2 (More Descriptive):** Clarify the scope:
```
T33 – Cloud Services & External Data
```

**Option 3 (Platform-Specific):** Match CreatiCode's actual categories:
```
T33 – Cloud & Database Integration
```

**Recommended:** Option 1 (Connected Services) - simple, clear, no jargon.

**Also update topic descriptions** in K-2 skills to remove "Tool Wrappers":
- Current: "T33 – Connected Services & Tool Wrappers"
- Updated: "T33 – Connected Services"

---

### 8. WEAK SCAFFOLDING - Jump from Sheets to Multi-Service Workflows Too Steep

**Issue Type:** Missing Intermediate Steps
**Priority:** MEDIUM-HIGH
**Affected:** T33.G7.07

**Problem:**
**T33.G7.07** "Build workflows that combine multiple services" expects students to:
- Orchestrate 3+ services (web fetch → AI → Google Sheets)
- Handle intermediate data between services
- Ensure sequential execution (async coordination)
- Manage errors at each stage

**But prerequisites only cover:**
- Individual service usage (fetch URL, write to Sheets)
- Error handling for single services
- Rate limiting for single services

**Missing skills:**
- How to store intermediate results
- How to ensure step 2 waits for step 1 (async coordination)
- How to debug multi-step workflows
- When workflows fail in the middle (partial completion)

**Recommended Fix:**
**Add intermediate skill before G7.07:**

```
ID: T33.G7.06A (NEW - insert before current G7.07, renumber rest)
Skill: Chain two services together in sequence
Description: Students create simple 2-step workflows by chaining services: fetch web content → display in label, read from Google Sheets → save to cloud database, or get AI response → write to Google Sheet. They use variables to store intermediate results between steps. They implement sequential execution: waiting for step 1 to complete before starting step 2 (using "wait until" or checking for non-empty results). They add basic error handling: if step 1 fails (empty result), don't run step 2. They test each step independently before combining them.

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T09.G5.01: Use multiple variables together in a single expression
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.02: Fetch web content using the fetch URL block
* T33.G6.04: Write data from a table to Google Sheets
* T33.G6.06: Handle latency and error states in service calls
```

**Then simplify G7.07** (renumbered to G7.08):
```
ID: T33.G7.08 (renumbered from G7.07)
Skill: Build workflows that combine multiple services
Description: Learners extend 2-step workflows to 3+ steps by orchestrating multiple services: fetch web content → process with AI → store results in Google Sheets → save summary to cloud database, or read settings from Sheets → generate AI content → speak with text-to-speech → log usage to database. They handle intermediate data storage across all steps and ensure each step completes before the next begins. They implement comprehensive error handling: if any step fails, the workflow stops gracefully and reports which step failed. They add status indicators (labels showing "Step 1: Fetching...", "Step 2: Processing...") for user feedback during long workflows.

Dependencies:
* T06.G5.01: Identify standard event patterns in a small game
* T09.G5.01: Use multiple variables together in a single expression
* T31.G5.01: Trace how a device reaches an online service
* T33.G7.06A: Chain two services together in sequence (NEW)
* T33.G6.07: Respect usage limits and rate limiting
```

**Rationale:**
- New G7.06A focuses on 2-step workflows (simpler)
- Covers async coordination explicitly
- Introduces intermediate variable storage
- G7.08 (old G7.07) now extends to 3+ steps
- Clear progression: 1 service → 2 services → 3+ services

---

### 9. UNCLEAR DESCRIPTION - G8.02 Legal/Ethical Analysis Too Vague

**Issue Type:** Unclear Learning Objectives
**Priority:** MEDIUM
**Affected:** T33.G8.02

**Problem:**
**T33.G8.02** "Analyze legal and ethical obligations when integrating services" says students will:
- "Read summarized terms for services"
- "Document obligations"
- "Map requirements to project design"

**But:**
- Where do students find these summarized terms? (CreatiCode provides them? External research?)
- What does "document obligations" mean? (Write a report? Fill a checklist? Annotate code?)
- "Map requirements to project design" - too abstract for G8
- No concrete deliverables or success criteria

**Also:** This skill has no block references, which is unusual for T33. Is it purely conceptual?

**Recommended Fix:**
**Make it concrete and actionable:**

```
ID: T33.G8.02
Skill: Review and apply service usage policies
Description: Students read CreatiCode's summarized service usage policies (provided in knowledge base or by teacher) for Google APIs, OpenAI, and cloud database. They identify specific rules that affect their projects: Google Sheets rate limits (how many reads/writes per minute), OpenAI content policies (what prompts are blocked), cloud database storage limits (how much data allowed). They create a project checklist documenting: which services their project uses, what rate limits apply, whether their content follows policies, and how they handle errors when limits are exceeded. They test their project to verify it stays within rate limits by adding counters and throttling mechanisms.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi-event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.08: Compare service options and pick the right tool

Note: Teachers should provide summarized, age-appropriate service policies. Focus on practical compliance (rate limits, content filters, data retention) rather than full legal terms.
```

**Rationale:**
- Specifies WHERE students get information (teacher/knowledge base)
- Concrete activities (create checklist, count API calls, test limits)
- Focuses on actionable rules (rate limits, content policies) not abstract ethics
- Includes testing and verification
- Teacher note clarifies scope

---

### 10. MISSING SKILL - No Coverage of Google Drive Operations

**Issue Type:** Incomplete Block Coverage
**Priority:** MEDIUM
**Affected:** T33.G7.04

**Problem:**
**T33.G7.04** covers `p2p_getgooglefoldercontent` (browse folder contents), which is listed under Google Drive in the block inventory. However:

**Current coverage:**
- T33.G7.04: List folder contents (metadata only) ✓

**Missing operations:**
- Downloading files from Drive
- Uploading files to Drive
- Deleting files from Drive
- Creating folders
- Moving/renaming files

**Check:** Do these blocks exist in CreatiCode?
- Looking at block inventory: Only `p2p_getgooglefoldercontent` is listed
- CreatiCode appears to provide READ-ONLY Google Drive access (browsing only)

**Recommended Fix:**
**IF** CreatiCode only provides folder browsing (read-only):
- Current skill T33.G7.04 is CORRECT - keep as-is
- Update description to clarify this is READ-ONLY access:

```
ID: T33.G7.04
Skill: Browse Google Drive folder contents (read-only)
Description: Students use the `list content of Google Drive folder` block to get file metadata (names, IDs, types, URLs) from a shared folder. They parse the returned table to display files, filter by type (images, documents, videos), or create file browsers for their projects. They understand this is READ-ONLY access: they can see what files exist and get their URLs, but cannot download, modify, or delete files through CreatiCode blocks. They use file URLs in other blocks: loading images from Drive URLs into costumes, or displaying file lists in their projects.

Block(s): p2p_getgooglefoldercontent

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.06: Handle latency and error states in service calls

Note: CreatiCode provides read-only access to Google Drive folders. Use the returned file URLs with other blocks to load media or reference files.
```

**IF** CreatiCode provides write operations (upload/delete/create):
- Add new skills at G7 or G8 covering those operations

**Verdict:** Based on available evidence, appears to be read-only → Update description to clarify.

---

### 11. GRADE-INAPPROPRIATE - G8 Skills Assume Too Much Technical Depth

**Issue Type:** Developmental Appropriateness
**Priority:** MEDIUM
**Affected:** T33.G8.03, T33.G8.04, T33.G8.05

**Problem:**
Several G8 skills expect advanced software engineering practices:

**T33.G8.03** "Simulate service outages and design fallbacks"
- Expects students to CREATE outage simulators (forcing error responses)
- Requires understanding of incident response procedures
- Asks for "recovery procedures documentation"
- This is professional DevOps/SRE work, not middle school CS

**T33.G8.04** "Validate and sanitize data received from external services"
- "Checking AI responses for inappropriate content" - how? (no content moderation blocks mentioned)
- "Verifying data types from Google Sheets" - assumes understanding of type systems
- "Confirming web fetch results are correctly formatted" - requires regex or parsing knowledge
- "Implement logging of validation failures" - assumes logging infrastructure

**T33.G8.05** "Compare service-based and local implementations through hands-on testing"
- "Measure and compare tradeoffs" - requires profiling/timing tools
- "Document measured differences" - assumes scientific method rigor
- "Create a decision framework" - very abstract for G8

**Recommended Fix:**
**Simplify to age-appropriate activities:**

**T33.G8.03 (Revised):**
```
ID: T33.G8.03
Skill: Design fallback behavior for service failures
Description: Students design "Plan B" responses when cloud services fail: if Google Sheets can't load, show a "using sample data" message and use hardcoded values; if AI doesn't respond, display "AI unavailable, try again later"; if web fetch fails, show cached content from last successful request. They use conditional checks (if result is empty, then use fallback) to detect failures. They test fallbacks by intentionally using invalid URLs or sheet IDs to trigger errors. They explain why fallbacks improve user experience (project still works even when internet fails).

Dependencies:
* T06.G6.01: Trace event execution paths in a multi-event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.08: Compare service options and pick the right tool
```

**T33.G8.04 (Revised):**
```
ID: T33.G8.04
Skill: Check external data before using it
Description: Students implement basic validation checks for external service data: checking if AI responses are empty before displaying them, verifying Google Sheets data has expected columns before processing, confirming web fetch results aren't blank before parsing. They use conditional statements (if length > 0, if contains expected text) to validate data. They create user-friendly error messages when data doesn't match expectations ("Data not found - check sheet name", "AI response empty - try different prompt"). They test validation by trying broken inputs (wrong sheet name, invalid URL) and verifying error messages appear.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.08: Compare service options and pick the right tool
```

**T33.G8.05 (Revised):**
```
ID: T33.G8.05
Skill: Compare cloud-based and local-only project versions
Description: Students build the same feature twice—once using cloud services and once using only local data—then compare the experiences: a quiz app that reads questions from Google Sheets versus one with hardcoded questions, or a chatbot using AI versus one with scripted responses. They test both versions online and offline, documenting what works in each scenario (cloud version fails offline, local version always works but can't be updated without code changes). They identify tradeoffs: cloud versions need internet but can update data without changing code; local versions work offline but require code edits to change content. They choose which approach fits different project goals (demo for presentation = local; app for continuous use = cloud).

Dependencies:
* T06.G6.01: Trace event execution paths in a multi-event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.08: Compare service options and pick the right tool
```

**Rationale:**
- Removed "simulate outages" - just test with invalid inputs
- Removed "logging" - just show error messages
- Removed "measurement" - just qualitative comparison
- Removed "decision frameworks" - just explain tradeoffs
- All revised skills focus on hands-on testing and observation
- Appropriate for G8 students (13-14 years old)

---

## MEDIUM PRIORITY ISSUES

### 12. WEAK SCAFFOLDING - No Introduction to Tables Before Cloud Database

**Issue Type:** Missing Foundation
**Priority:** MEDIUM
**Affected:** Cloud database skills (when added)

**Problem:**
When cloud database skills are added (see Issue #1), students will need to:
- Understand table structures (collections are like tables)
- Work with rows (documents) and columns (fields)
- Use query results stored in tables

**Current table coverage:**
- T10.G4.01: Create a list (not tables)
- T10.G5.01: Understand table structure
- T10.G6.01: Sort a table

**Gap:** Students learn tables in T10 (Data Structures) but may not have practiced enough with tables before encountering database operations in T33.

**Recommended Fix:**
**Option A:** Add dependency on T10.G5.01 to all database skills
**Option B:** Add a transitional skill at G6 that uses tables with Cloud blocks before databases:

```
ID: T33.G6.XX (NEW)
Skill: Store cloud service results in tables for further processing
Description: Students use tables to store and organize data from cloud services: fetching multiple web pages and storing results in a table (URL, content, timestamp columns), reading from multiple Google Sheets and combining into one table, or collecting AI responses for batch analysis. They practice table operations (add row, get cell, sort by column) with cloud data. They understand that tables let them process multiple service responses together rather than one at a time.

Dependencies:
* T10.G5.01: Understand table structure (rows, columns, cells)
* T33.G6.02: Fetch web content using the fetch URL block
* T33.G6.03: Read data from Google Sheets into a table
```

**Recommended:** Option B - reinforces table skills in Cloud context before database

---

### 13. UNCLEAR DESCRIPTION - G7.06 Authorization Skill Too Abstract

**Issue Type:** Vague Learning Objectives
**Priority:** MEDIUM
**Affected:** T33.G7.06

**Problem:**
**T33.G7.06** "Understand service authorization and keep shared URLs private" covers two distinct concepts:
1. How CreatiCode handles authentication (automatic)
2. Privacy of shared URLs (covered better in G6.08)

**Current description:**
- "CreatiCode's Cloud and AI blocks handle authentication automatically" - good
- "Shared URLs grant access to anyone with the link" - already covered in G6.08
- "Best practices: use test data, avoid personal info" - already covered in G6.08

**This skill seems redundant with G6.08.** What's the G7-level addition?

**Recommended Fix:**
**Option A:** Remove this skill (consolidate into G6.08)
**Option B:** Refocus on understanding how authorization works (not just privacy):

```
ID: T33.G7.06 (Revised)
Skill: Understand how cloud service authorization works
Description: Students learn that CreatiCode handles Google API and cloud database authorization automatically using the platform's credentials—they don't need API keys or OAuth tokens. They understand this means: projects work immediately without setup, but all projects share CreatiCode's usage quotas (rate limits apply to ALL users combined), and students can't use personal Google accounts for project-specific data (must use publicly-shared sheets/folders). They compare this to other platforms where users bring their own API keys. They explain why shared quotas require responsible usage (respecting rate limits helps everyone).

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.08: Understand privacy implications of shared Google Sheet URLs
```

**Recommended:** Option B - explains authorization model as distinct concept from privacy

---

### 14. TOO BROAD - G7.08 "Compare Service Options" Lacks Criteria

**Issue Type:** Unclear Success Criteria
**Priority:** MEDIUM
**Affected:** T33.G7.08

**Problem:**
**T33.G7.08** "Compare service options and pick the right tool" says students will:
- "Analyze requirements and select appropriate block"
- "Justify choices based on capabilities, latency, and data format"

**But:**
- No specific comparison framework provided
- "Capabilities, latency, data format" are abstract criteria
- No examples of decision scenarios
- How do students "justify" - verbal explanation? Written report? Code comments?

**Recommended Fix:**
**Provide concrete comparison framework:**

```
ID: T33.G7.08 (Revised)
Skill: Choose the right cloud service for project needs
Description: Students analyze project requirements and select appropriate cloud services using a decision framework: Use Google Sheets when data needs persistent storage and human editing (leaderboards, settings, user-submitted content); use web fetch when retrieving existing online content (news, weather, public data); use AI blocks when generating or analyzing text (chatbots, creative writing, translation); use cloud database when data needs complex queries or large scale (game logs, search functionality, filtered results). They create comparison tables showing service strengths (Sheets: editable, web fetch: fast, AI: creative, database: queryable) and limitations (Sheets: slow with large data, web fetch: read-only, AI: uses quota, database: requires schema). They justify their choice for a project by explaining which requirements match which service strengths.

Dependencies:
* T08.G5.01: Use nested conditionals for multi-branch decisions
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.06: Handle latency and error states in service calls
* T33.G6.07: Respect usage limits and rate limiting
```

**Rationale:**
- Specific decision criteria (persistent? editable? queryable? creative?)
- Concrete service strengths and limitations
- Examples of what each service is best for
- Clear justification format (explain requirements → service strengths match)

---

### 15. MISSING INTERMEDIATE - No Skill on Reading Web Fetch Results

**Issue Type:** Missing Scaffolding
**Priority:** MEDIUM
**Affected:** T33.G6.02

**Problem:**
**T33.G6.02** teaches fetching web content, but the description says:
- "Block converts HTML to markdown"
- "Display it in their project"

**Questions:**
- How do students display markdown? (Label widget? Say block? Text sprite?)
- What if markdown has formatting (bold, links)? (Does CreatiCode render markdown or just show raw text?)
- How do students parse/extract specific info from fetched content? (Get weather from page, extract headlines, find specific text)

**The skill teaches fetching but not processing the result.**

**Recommended Fix:**
**Option A:** Expand T33.G6.02 to include basic result display
**Option B:** Add follow-up skill for parsing/processing fetched content

**Recommended: Option A** (simpler):
```
ID: T33.G6.02 (Revised)
Skill: Fetch and display web content using the fetch URL block
Description: Students use the `fetch web page as markdown from URL` block to retrieve content from a public URL and display it in their project. They learn that the block converts HTML to markdown (formatted text) and store the result in a variable. They display fetched content using labels or "say" blocks, understanding that markdown formatting (like ** for bold) appears as plain text in CreatiCode. They extract specific information from fetched content using string operators: finding position of text, getting substrings, checking if content contains keywords. They handle cases where URLs are invalid or unreachable by checking for empty results before displaying.

Block(s): p2p_fetchfromurl

Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T09.G4.01: Prompt user for input and store it in a variable
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.01: Identify and test Cloud blocks for network dependencies

Note: Fetched content appears as markdown text. Use string operators (join, letter N of, find) to extract specific information.
```

---

### 16. GRADE-INAPPROPRIATE - Cache Expiration with Timestamps Too Advanced for G7

**Issue Type:** Complexity Mismatch
**Priority:** MEDIUM
**Affected:** T33.G7.09

**Problem:**
**T33.G7.09** "Cache service responses" expects students to:
- "Implement cache expiration by storing timestamps with entries"
- "Clearing old entries after a set duration (e.g., 5 minutes)"

**This requires:**
- Understanding Unix timestamps or current time values
- Calculating time differences (now - stored time > 300 seconds)
- Managing timestamp columns in cache table
- Implementing cache eviction logic

**This is advanced data structures work** (LRU cache concepts) for G7 (12-13 year olds).

**Recommended Fix:**
**Simplify to basic caching without timestamps:**

```
ID: T33.G7.09 (Revised)
Skill: Cache service responses to avoid redundant calls
Description: Students implement a simple caching pattern: before calling an external service, check if the same request was made recently by looking up a local table (cache). The cache table has columns for request input (search term, URL, prompt) and response output (result text, fetched content, AI answer). If the input is found in cache, use the stored response instead of making a new service call. Otherwise, make the call and add the input-output pair to cache. Students understand this reduces service calls (respects rate limits), improves speed (no network wait), and works offline once cached. They implement a simple cache clear button to reset the cache when needed or when cache table gets too large.

Dependencies:
* T09.G5.01: Use multiple variables together in a single expression
* T10.G5.01: Understand table structure (rows, columns, cells)
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.06: Handle latency and error states in service calls

Note: This basic cache doesn't expire automatically. Advanced caching with timestamps and auto-expiration can be explored as an extension activity.
```

**Rationale:**
- Removes timestamp/expiration complexity
- Focuses on core concept: lookup before call
- Keeps benefits (speed, offline, rate limiting)
- Manual cache clearing instead of automatic expiration
- Appropriate for G7 cognitive level

---

### 17. UNCLEAR DESCRIPTION - G6.05 Sheet Clearing Motivation Weak

**Issue Type:** Unclear Rationale
**Priority:** LOW-MEDIUM
**Affected:** T33.G6.05

**Problem:**
**T33.G6.05** teaches clearing sheets but says:
- "When clearing is preferable to deleting (preserving sheet structure and formatting)"

**Question:** Does CreatiCode have a "delete sheet" block at G6 level?
- Looking at progression: Delete sheets (`p2p_removesheet`) appears in T33.G7.01
- So at G6.05, students haven't learned deleting sheets yet

**This creates confusion:** Why mention "clearing vs deleting" before students know how to delete?

**Recommended Fix:**
**Remove comparison to deleting, focus on clearing use cases:**

```
ID: T33.G6.05 (Revised)
Skill: Clear a Google Sheet to reset data
Description: Students use the `clear sheet` block to remove all content from a specified sheet while keeping the sheet structure (sheet name, position in spreadsheet) intact. They implement "reset data" features in projects: clearing old quiz results before starting new quiz, removing previous leaderboard entries before new game, or wiping survey responses to start fresh data collection. They understand that clearing is different from deleting all rows one-by-one (clearing is faster and keeps column headers if needed). They verify successful clearing by reading the sheet after clearing and checking it's empty.

Block(s): p2p_clearsheet

Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
* T33.G6.04: Write data from a table to Google Sheets
```

**Rationale:**
- Removes premature "vs deleting" comparison
- Focuses on concrete use cases (reset features)
- Explains what clearing does (removes content, keeps structure)
- Students learn clear-vs-delete comparison later in G7.01

---

### 18. WEAK PROGRESSION - Missing Skill on Understanding Service Costs/Quotas

**Issue Type:** Missing Conceptual Foundation
**Priority:** MEDIUM
**Affected:** G6-G8 service usage skills

**Problem:**
Multiple skills reference "rate limits" and "usage quotas":
- T33.G6.07: Respect usage limits and rate limiting
- T33.G7.08: Pick the right tool (mentions latency)
- T33.G8.02: Legal/ethical obligations (mentions rate limits in fix)

**But there's no foundational skill explaining WHY services have limits:**
- Cloud services cost money (API calls, storage, compute)
- Free tiers have quotas (X calls per day/minute)
- Exceeding quotas can block access or cost money
- Shared quotas (like CreatiCode's) affect all users

**Students might think:** "Why can't I call AI 1000 times per second? It's just a block!"

**Recommended Fix:**
**Add conceptual skill at G5 or early G6:**

```
ID: T33.G5.04 (NEW)
Skill: Understand why cloud services have usage limits
Description: Students learn that cloud services (AI, Google Sheets, databases) cost money to run: servers, electricity, storage, and processing time all have real-world costs. They understand that free services have usage limits (quotas) to control costs: AI might allow 100 requests per day, Google Sheets might limit 60 reads per minute. They explain what happens when limits are exceeded: services might block further requests until quota resets, show error messages, or require payment to continue. They understand that in CreatiCode, all users share the platform's quotas, so using services responsibly helps everyone. They identify which blocks use external services (and have quotas) versus which run locally (unlimited).

Dependencies:
* T31.G5.01: Trace how a device reaches an online service
* T33.G5.01: Compare local storage versus cloud storage tradeoffs
```

**Then update G6.07:**
```
ID: T33.G6.07 (Revised)
Skill: Implement rate limiting in projects
Description: Learners implement counters and cool-down timers so projects don't exceed service quotas: counting AI calls and stopping at limit (e.g., max 10 per session), adding delays between Google Sheets writes (wait 1 second between writes), or disabling service buttons temporarily after use (5-second cooldown). They create user feedback showing quota status: "3 AI calls remaining today", "Please wait 5 seconds before next request". They test what happens when projects call services too rapidly and observe error responses or blocked requests.

Dependencies:
* T07.G4.01: Use repeat-until to loop based on a condition
* T09.G4.01: Prompt user for input and store it in a variable
* T31.G5.01: Trace how a device reaches an online service
* T33.G5.04: Understand why cloud services have usage limits (NEW)
* T33.G6.06: Handle latency and error states in service calls
```

**Rationale:**
- G5.04 provides conceptual foundation (why limits exist)
- G6.07 focuses on implementation (how to respect limits)
- Clear progression: understand why → implement how
- Appropriate age: G5 can grasp "costs money" concept

---

## DEPENDENCY ISSUES (T33 Internal)

### 19. X-2 RULE VIOLATION - T33.G8.01 Depends on T31.G6.01

**Issue Type:** Dependency Too Far Back
**Priority:** LOW
**Affected:** T33.G8.01, T33.G8.02, T33.G8.03, T33.G8.04, T33.G8.05, T33.G8.06

**Problem:**
Multiple T33.G8 skills depend on **T31.G6.01** (HTTP/HTTPS requests), which is 2 grades back. While not strictly violating X-2 rule (2 grades back is allowed), this creates a weak progression in T33 itself.

**Current T33 → T31 dependencies:**
- G6 skills → T31.G5.01 (device reaches online service) ✓ 1 grade back
- G7 skills → T31.G5.01 ✓ 1 grade back
- G8 skills → T31.G6.01 ✗ 2 grades back

**Issue:** T33.G8 skills don't build on T33.G7 skills directly for networking knowledge; they skip to T31.

**Recommended Fix:**
**Option A:** Change G8 dependencies from T31.G6.01 to T31.G7.01 if available
**Option B:** Accept 2-grade dependency as valid (X-2 allows it)
**Option C:** Add T33.G7 skill that covers HTTP concepts, then G8 depends on that

**Recommended: Option B** - This is valid per X-2 rule, no fix needed. But note for future: consider if T33 should have its own HTTP-focused skill.

---

### 20. CIRCULAR DEPENDENCY RISK - G6.08 and G7.06 Both Cover Privacy

**Issue Type:** Redundancy
**Priority:** LOW
**Affected:** T33.G6.08, T33.G7.06

**Problem:**
Both skills cover privacy/authorization:
- T33.G6.08: Privacy implications of shared URLs
- T33.G7.06: Service authorization and keeping URLs private

**G7.06 depends on G6.08, but they cover overlapping content** (both mention "keep URLs private", "use test data", "avoid personal info").

**Recommended Fix:**
See Issue #13 - either remove G7.06 (consolidate into G6.08) or refocus G7.06 on authorization model distinct from privacy.

**Already addressed above.**

---

### 21. MISSING PREREQUISITE - G8.06 Pipeline Missing Database Dependency

**Issue Type:** Missing Dependency
**Priority:** MEDIUM
**Affected:** T33.G8.06

**Problem:**
**T33.G8.06** "Build a cloud-integrated data pipeline" describes:
- "Fetch external data → process → store in Google Sheets → use in AI calls → save AI outputs back to cloud"

The skill mentions "cloud" storage but only depends on Google Sheets skills (G7.07 workflows). If this is meant to be a comprehensive cloud integration capstone, it should include:
- Cloud database operations (when added per Issue #1)
- Cloud sessions (G7.05)
- All major cloud blocks covered in T33

**Current dependencies:**
- T06.G6.01: Events
- T10.G6.01: Tables
- T31.G6.01: HTTP
- T33.G7.07: Workflows
- T33.G8.04: Validation

**Missing:**
- Cloud database skills (not yet added)
- Cloud sessions (G7.05) - should be included for comprehensive cloud coverage

**Recommended Fix:**
**After adding database skills (Issue #1), update G8.06:**

```
ID: T33.G8.06 (Revised)
Skill: Build a cloud-integrated data pipeline
Description: Students build a complete data pipeline as a capstone: fetch external data → process and transform → store in Google Sheets OR cloud database → use in AI calls → save AI outputs back to cloud storage OR publish via cloud sessions. They handle errors at each stage, implement validation for external data, and create a dashboard showing pipeline status (which stages completed, how many records processed, any errors). They demonstrate understanding of when to use each cloud service: Google Sheets for human-editable data, cloud database for queryable logs, cloud sessions for real-time sharing, AI for content generation, web fetch for external sources. This capstone integrates skills from G6 through G8 of this topic.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi-event program
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace the steps of an HTTP/HTTPS request
* T33.G7.05: Create and join cloud sessions for variable synchronization
* T33.G7.08: Build workflows that combine multiple services (renumbered from G7.07)
* T33.G8.XX: Cloud database operations (NEW - from Issue #1)
* T33.G8.04: Validate and sanitize data received from external services
```

**Rationale:**
- Adds cloud database to pipeline options
- Adds cloud sessions to demonstrate real-time sharing
- Makes this a true "comprehensive cloud integration" capstone
- Covers all major T33 cloud services

---

### 22. UNNECESSARY SAME-GRADE DEPENDENCY - Multiple G7 Skills

**Issue Type:** Same-Grade Dependency
**Priority:** LOW
**Affected:** Multiple G7 skills

**Problem:**
Several T33.G7 skills depend on other T33.G7 skills:
- T33.G7.03 → T33.G7.02 (append rows → cell operations)
- T33.G7.08 → T33.G7.07 (compare services → build workflows) [after renumbering]

**In a well-structured curriculum:**
- Same-grade dependencies should be minimized (order shouldn't matter within grade)
- Cross-skill dependencies within grade suggest one should be moved

**Recommended Fix:**
**Option A:** Keep dependencies if there's clear pedagogical progression
**Option B:** Remove same-grade dependencies by reordering

**Analysis:**
- **G7.03 → G7.02:** Makes sense - append builds on cell operations. Could G7.02 move to G6? No, it uses `get value` which needs table understanding beyond G6 level.
- **G7.08 → G7.07:** Comparing services requires having built workflows first. This makes sense.

**Recommended: Option A** - Keep same-grade dependencies where pedagogically necessary. Document the intended sequence in teaching materials.

---

### 23. WEAK DEPENDENCY CHAIN - G6 Skills Missing T10 Table Dependencies

**Issue Type:** Missing Prerequisite
**Priority:** MEDIUM
**Affected:** T33.G6.03, T33.G6.04

**Problem:**
**T33.G6.03** and **T33.G6.04** work with Google Sheets and CreatiCode tables:
- "Load data into a CreatiCode table"
- "Export a CreatiCode table to Google Sheet"
- "Iterate through loaded data"

**Current dependencies:**
- T10.G4.01: Create a list

**But lists ≠ tables:**
- Lists are 1D (just items)
- Tables are 2D (rows and columns)
- Working with sheet data requires table understanding

**T10.G5.01 "Understand table structure"** should be a prerequisite for any skill working with tables.

**Recommended Fix:**
**Update G6.03 and G6.04 dependencies:**

```
ID: T33.G6.03 (Add dependency)
Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T10.G4.01: Create a list and populate it with items
* T10.G5.01: Understand table structure (rows, columns, cells)  ← ADD THIS
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.01: Identify and test Cloud blocks for network dependencies
```

```
ID: T33.G6.04 (Add dependency)
Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T10.G4.01: Create a list and populate it with items
* T10.G5.01: Understand table structure (rows, columns, cells)  ← ADD THIS
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.03: Read data from Google Sheets into a table
```

**Rationale:**
- Tables are central to Google Sheets integration
- Students need to understand rows/columns before working with sheet data
- T10.G5.01 is only 1 grade back (G5 → G6), valid per X-2 rule

---

### 24. DEPENDENCY GAP - Missing T09 Variable Prerequisites in G6

**Issue Type:** Missing Prerequisite
**Priority:** LOW-MEDIUM
**Affected:** T33.G6.02, T33.G6.06, T33.G6.07

**Problem:**
Several G6 skills work with variables to store service results:
- T33.G6.02: Store fetched URL content in variable
- T33.G6.06: Check for empty responses (variable checking)
- T33.G6.07: Implement call counters (variables for counting)

**Current dependencies:**
- T33.G6.02 → T09.G4.01 (prompt and store) ✓
- T33.G6.06 → T09.G4.01 (prompt and store) ✓
- T33.G6.07 → T09.G4.01 (prompt and store) ✓

**But these skills also use:**
- String checking (is variable empty? length > 0?)
- Numeric comparison (counter > limit?)
- Variable inspection (checking variable values)

**T09.G4.04 "Trace code with variables to predict outcomes"** would help students understand variable state changes during service calls.

**Recommended Fix:**
**Add T09.G4.04 as dependency where appropriate:**

```
ID: T33.G6.06 (Add dependency)
Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T09.G4.01: Prompt user for input and store it in a variable
* T09.G4.04: Trace code with variables to predict outcomes  ← ADD THIS
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.02: Fetch web content using the fetch URL block
```

```
ID: T33.G6.07 (Add dependency)
Dependencies:
* T07.G4.01: Use repeat-until to loop based on a condition
* T09.G4.01: Prompt user for input and store it in a variable
* T09.G4.04: Trace code with variables to predict outcomes  ← ADD THIS
* T31.G5.01: Trace how a device reaches an online service
* T33.G5.04: Understand why cloud services have usage limits (NEW)
* T33.G6.06: Handle latency and error states in service calls
```

**Rationale:**
- Tracing variables helps understand async operations (send request → wait → variable updates)
- Helps debug "why is my variable empty?" issues common with service calls
- Already referenced in T33.G6.01, so consistent

---

### 25. MISSING PREREQUISITE - G7.09 Caching Missing Lookup Dependency

**Issue Type:** Missing Prerequisite
**Priority:** LOW
**Affected:** T33.G7.09

**Problem:**
**T33.G7.09** "Cache service responses" requires:
- Looking up values in table by key (check if request exists in cache)
- Using `data_rowindexwithcondition` or similar lookup blocks

**Current dependencies:**
- T10.G5.01: Understand table structure ✓

**But T10 doesn't cover table LOOKUP operations.** Students need to know how to:
- Search table for matching row
- Check if value exists in column
- Retrieve row by condition

**These are advanced table operations** typically covered in later T10 skills.

**Recommended Fix:**
**Check T10 progression for lookup skills, add dependency:**

If T10 has lookup skills (like T10.G6.XX "Search table by column value"), add to G7.09:
```
ID: T33.G7.09 (Add dependency)
Dependencies:
* T09.G5.01: Use multiple variables together in a single expression
* T10.G5.01: Understand table structure (rows, columns, cells)
* T10.G6.XX: Search/lookup operations in tables  ← ADD IF EXISTS
* T31.G5.01: Trace how a device reaches an online service
* T33.G6.06: Handle latency and error states in service calls
```

If T10 doesn't have lookup skills, either:
1. Add lookup skill to T10
2. Teach basic lookup inline in G7.09 description
3. Move G7.09 to G8 after more table skills

**Recommended:** Check T10 for lookup coverage, add dependency if exists.

---

### 26. CIRCULAR DEPENDENCY POTENTIAL - G8.06 Capstone

**Issue Type:** Dependency Chain Length
**Priority:** LOW
**Affected:** T33.G8.06

**Problem:**
**T33.G8.06** is a capstone that depends on:
- T33.G7.08 (workflows) which depends on:
  - T33.G7.06A (2-service chains) which depends on:
    - T33.G6.02, T33.G6.04 (individual services)

**And:**
- T33.G8.04 (validation) which depends on:
  - T33.G7.08 (service comparison)

**This creates long dependency chains:**
G8.06 → G7.08 → G7.06A → G6.XX (3+ levels)

**While not circular,** long dependency chains can make the curriculum rigid and hard to navigate.

**Recommended Fix:**
**Option A:** Accept this as natural for capstone skills
**Option B:** Flatten dependencies by making G8.06 depend directly on core skills

**Recommended: Option A** - Capstones naturally have long dependency chains. This is acceptable as long as:
- No actual circular dependencies exist ✓
- Dependencies are logically progressive ✓
- Students can't skip to capstone without foundations ✓

**No fix needed** - this is expected for culminating skills.

---

## SUMMARY OF RECOMMENDED ACTIONS

### Immediate Actions (High Priority):

1. **Add 4-5 cloud database skills** (G6-G8) covering collections, queries, CRUD operations
2. **Add URL-based media loading skill** (G6)
3. **Rewrite T33.G5.02** to focus on cloud variables vs local variables
4. **Rewrite T33.G7.05** to clarify cloud sessions sync variables only, not full multiplayer
5. **Narrow T33.G6.01** to focus on Cloud category only (remove AI/Multiplayer references)
6. **Add privacy foundation skill T33.G5.03** before first data sharing
7. **Move and update T33.G6.08** privacy skill to apply after foundation
8. **Rename topic** from "Connected Services & Tool Wrappers" to "Connected Services"
9. **Add intermediate skill T33.G7.06A** for 2-service workflows before multi-service
10. **Simplify G8 skills** (G8.02, G8.03, G8.04, G8.05) to age-appropriate activities

### Secondary Actions (Medium Priority):

11. **Add table practice skill** at G6 before database operations
12. **Revise/remove T33.G7.06** to avoid redundancy with G6.08
13. **Add decision framework** to T33.G7.08 service comparison
14. **Expand T33.G6.02** to cover displaying/parsing fetched content
15. **Simplify T33.G7.09** caching to remove timestamp complexity
16. **Update T33.G6.05** to remove premature delete comparison
17. **Add T33.G5.04** explaining why services have quotas/limits

### Dependency Fixes:

18. **Add T10.G5.01 dependency** to T33.G6.03 and T33.G6.04 (table understanding)
19. **Add T09.G4.04 dependency** to T33.G6.06 and T33.G6.07 (variable tracing)
20. **Update T33.G8.06** to include cloud database and cloud sessions when added
21. **Check T10 for lookup skills**, add to T33.G7.09 if exists

---

## BLOCK COVERAGE ANALYSIS

### Currently Covered Blocks (17/17 claimed):
✅ Google Sheets: p2p_readfromgooglesheet, p2p_writeintogooglesheet, p2p_clearsheet, p2p_listSheetsInGoogleSheet, p2p_addsheet, p2p_removesheet, p2p_getvalue, p2p_setvalue, p2p_appendrow, p2p_insertrowsinsheet, p2p_removerowsfromsheet, p2p_insertcolumnsinsheet, p2p_removecolumnsfromsheet
✅ Web Fetch: p2p_fetchfromurl
✅ Google Drive: p2p_getgooglefoldercontent
✅ Cloud Sessions: data_createcloudsession, data_joincloudsession

### Missing Blocks (13+ blocks):
❌ **Cloud Database (13 blocks):**
- database_find_from_collection
- database_insert_from_table
- database_update_collection
- database_update_collection_in_place
- database_remove_all_document
- database_collection
- database_query
- database_operator
- database_contains
- database_collectionfield
- database_not
- database_and
- database_or

### Potentially Missing Blocks (needs verification):
⚠️ URL-based media loading (if exists as separate blocks)

---

## FINAL RECOMMENDATIONS

### Top 3 Critical Fixes:
1. **Add cloud database coverage** - 13 blocks with zero skills is unacceptable
2. **Fix cloud sessions vs multiplayer confusion** - currently misleading students
3. **Add privacy foundation before data sharing** - safety-first approach

### Topic Restructure Proposal:
Consider splitting T33 into two topics:
- **T33 - Cloud Data Services:** Google Sheets, cloud database, cloud sessions
- **T33B - External Content:** Web fetch, Google Drive, URL media

This would:
- Clarify scope of each topic
- Reduce cognitive load per topic
- Make it easier to find relevant skills
- Separate persistent storage from content retrieval

**However:** This may be too disruptive. Alternative is to keep current structure but improve organization within T33.

---

**End of Analysis**
**Total Issues Identified:** 26
**High Priority:** 11
**Medium Priority:** 7
**Dependency Issues:** 8
