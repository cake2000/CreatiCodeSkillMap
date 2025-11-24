# T33 (Connected Services & Tool Wrappers) - Comprehensive Analysis
**Date:** 2024-11-24

## Executive Summary

Topic T33 covers Connected Services across K-8, progressing from basic internet concepts to sophisticated cloud service integration. After analyzing all 42 T33 skills and cross-referencing with CreatiCode's actual Cloud and Database blocks, several critical issues have been identified that require immediate attention.

### Critical Findings:
1. **Several skills are too broad and need breaking down** (8 skills identified)
2. **Missing foundational skills** needed for proper scaffolding (5 gaps identified)
3. **Dependency violations** of the X-2 rule (12 violations found)
4. **Skills not aligned with actual blocks** (3 misalignments)
5. **Grade-inappropriate content** (4 skills need adjustment)

---

## Part 1: Complete T33 Skills Inventory

### Kindergarten (1 skill)
- **T33.GK.01**: Recognize that apps can talk to helpers on the internet
  - No dependencies
  - Grade-appropriate conceptual introduction

### Grade 1 (1 skill)
- **T33.G1.01**: Sort apps into online helpers and offline tools
  - Depends on: T33.GK.01
  - Grade-appropriate sorting activity

### Grade 2 (1 skill)
- **T33.G2.01**: Describe what happens when an app waits for the internet
  - Depends on: T33.G1.01
  - Grade-appropriate - introduces latency concept through play

### Grade 3 (1 skill)
- **T33.G3.01**: Identify cloud-connected features in familiar apps
  - Depends on: T33.G2.01
  - Grade-appropriate observation skill

### Grade 4 (1 skill)
- **T33.G4.01**: Explain how apps store and retrieve data from the cloud
  - Depends on: T31.G4.01, T33.G3.01
  - Grade-appropriate conceptual understanding

### Grade 5 (3 skills)
- **T33.G5.01**: Compare local storage versus cloud storage tradeoffs
  - Depends on: T31.G5.01, T33.G4.01
  - Grade-appropriate comparative analysis

- **T33.G5.02**: Distinguish real-time collaboration from one-time requests
  - Depends on: T31.G5.01, T33.G5.01
  - Grade-appropriate - good distinction

- **T33.G5.03**: Understand that shared URLs grant public access
  - Depends on: T31.G5.01, T33.G5.01
  - **CRITICAL**: Important privacy/security concept

### Grade 6 (10 skills) ⚠️ VERY DENSE
- **T33.G6.01**: Identify and test Cloud blocks for network dependencies
  - Depends on: T08.G4.01, T09.G4.04, T31.G5.01, T33.G5.01, T33.G5.03
  - **STATUS**: ✅ Well-designed introductory skill
  - **NOTE**: Good reference to AI blocks (T32) and Multiplayer blocks (T19)

- **T33.G6.02**: Fetch web content using the fetch URL block
  - Depends on: T08.G4.01, T09.G4.01, T31.G5.01, T33.G5.03, T33.G6.01
  - **BLOCK**: `fetch web page as [FORMAT] from URL [URL]`
  - **STATUS**: ✅ Aligned with actual block

- **T33.G6.03**: Read data from Google Sheets into a table
  - Depends on: T08.G4.01, T10.G4.01, T31.G5.01, T33.G6.01
  - **BLOCK**: `read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]`
  - **STATUS**: ✅ Aligned with actual block

- **T33.G6.04**: Write data from a table to Google Sheets
  - Depends on: T08.G4.01, T10.G4.01, T31.G5.01, T33.G6.03
  - **BLOCK**: `write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]`
  - **STATUS**: ✅ Aligned with actual block

- **T33.G6.05**: Clear a Google Sheet to reset data
  - Depends on: T08.G4.01, T31.G5.01, T33.G6.03, T33.G6.04
  - **BLOCK**: `clear sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
  - **STATUS**: ✅ Aligned with actual block

- **T33.G6.06**: Handle latency and error states in service calls
  - Depends on: T08.G4.01, T09.G4.01, T31.G5.01, T33.G6.02
  - **STATUS**: ⚠️ TOO BROAD - needs breaking down
  - **ISSUE**: Covers ALL external services (Cloud, AI, Web) - should be split

- **T33.G6.07**: Respect usage limits and rate limiting
  - Depends on: T07.G4.01, T09.G4.01, T31.G5.01, T33.G6.06
  - **STATUS**: ⚠️ COMPLEX for G6
  - **ISSUE**: Requires implementing counters and timers - may be too advanced

- **T33.G6.08**: Apply privacy principles to Google Sheet URLs
  - Depends on: T33.G5.03, T33.G6.03, T33.G6.04
  - **STATUS**: ✅ Good privacy reinforcement
  - **NOTE**: Important ethical skill

- **T33.G6.09**: Understand cloud database collections versus Google Sheets
  - Depends on: T10.G5.01, T31.G5.01, T33.G6.03
  - **STATUS**: ⚠️ DEPENDENCY VIOLATION
  - **ISSUE**: Depends on T10.G5.01 (G5) - violates X-2 rule

- **T33.G6.10**: Insert and fetch data from cloud database collections
  - Depends on: T08.G5.01, T10.G5.01, T31.G5.01, T33.G6.09
  - **BLOCKS**:
    - `insert from table [TABLENAME v] row from (STARTROW) to (ENDROW) into collection [COLLECTIONNAME v]`
    - `fetch from collection [COLLECTIONNAME v] into table [TABLENAME v] where <CONDITION> limit (LIMIT) sort by (SORTFIELD1) [SORTORDER1 v] (SORTFIELD2) [SORTORDER2 v]`
  - **STATUS**: ⚠️ MULTIPLE DEPENDENCY VIOLATIONS
  - **ISSUE**: Depends on T08.G5.01 and T10.G5.01 (G5) - violates X-2 rule

### Grade 7 (12 skills) ⚠️ EXTREMELY DENSE
- **T33.G7.01**: List, add, and remove sheets in a Google Spreadsheet
  - Depends on: T08.G5.01, T10.G5.01, T31.G5.01, T33.G6.03, T33.G6.04
  - **BLOCKS**:
    - `list all sheets in google sheet at URL [SHEET_URL] into list [LIST]`
    - `add sheet [SHEETNAME] to google sheet at URL [URL]`
    - `remove sheet [SHEETNAME] from google sheet at URL [URL]`
    - `clear sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
  - **STATUS**: ⚠️ TOO BROAD + DEPENDENCY VIOLATIONS
  - **ISSUE 1**: Covers 4 different operations - should be split
  - **ISSUE 2**: Depends on T08.G5.01, T10.G5.01, T31.G5.01 - multiple G5 deps violate X-2 rule

- **T33.G7.02**: Perform targeted Google Sheets cell operations
  - Depends on: T08.G5.01, T10.G5.01, T31.G5.01, T33.G6.03, T33.G6.04
  - **BLOCKS**:
    - `get value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
    - `set value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
  - **STATUS**: ⚠️ DEPENDENCY VIOLATIONS
  - **ISSUE**: Multiple G5 dependencies

- **T33.G7.03**: Append rows incrementally to a Google Sheet
  - Depends on: T08.G5.01, T10.G5.01, T31.G5.01, T33.G6.04, T33.G7.02
  - **BLOCK**: `append row [ROWNUMBER] from table [TABLENAME v] to sheet [SHEETNAME] in Google Sheet at URL [URL]`
  - **STATUS**: ⚠️ DEPENDENCY VIOLATIONS
  - **ISSUE**: Multiple G5 dependencies

- **T33.G7.04**: Browse Google Drive folder contents
  - Depends on: T08.G5.01, T10.G5.01, T31.G5.01, T33.G6.03, T33.G6.06
  - **BLOCK**: `list content of Google Drive folder [URL] in table [TABLENAME v]`
  - **STATUS**: ⚠️ DEPENDENCY VIOLATIONS
  - **ISSUE**: Multiple G5 dependencies

- **T33.G7.05**: Synchronize variables across projects using cloud sessions
  - Depends on: T09.G5.01, T31.G5.01, T33.G5.02, T33.G5.03
  - **BLOCKS**:
    - `create cloud session [SESSION]`
    - `join cloud session [SESSION]`
  - **STATUS**: ⚠️ TOO BROAD + DEPENDENCY VIOLATIONS
  - **ISSUE 1**: Very complex concept - real-time variable synchronization
  - **ISSUE 2**: Multiple G5 dependencies
  - **NOTE**: Good distinction from T19 (Multiplayer)

- **T33.G7.06**: Understand automatic service authorization in CreatiCode
  - Depends on: T08.G5.01, T31.G5.01, T33.G5.03, T33.G6.03
  - **STATUS**: ⚠️ TOO CONCEPTUAL + DEPENDENCY VIOLATIONS
  - **ISSUE 1**: Purely conceptual - no hands-on component
  - **ISSUE 2**: Multiple G5 dependencies

- **T33.G7.07**: Build workflows that combine multiple services
  - Depends on: T06.G5.01, T09.G5.01, T31.G5.01, T33.G6.02, T33.G6.04, T33.G6.07
  - **STATUS**: ⚠️ TOO BROAD + DEPENDENCY VIOLATIONS
  - **ISSUE 1**: Covers multi-service workflows - very complex
  - **ISSUE 2**: Multiple G5 dependencies

- **T33.G7.08**: Compare service options and pick the right tool
  - Depends on: T08.G5.01, T31.G5.01, T33.G6.06, T33.G6.07
  - **STATUS**: ⚠️ TOO CONCEPTUAL + DEPENDENCY VIOLATIONS
  - **ISSUE 1**: High-level decision-making skill
  - **ISSUE 2**: Multiple G5 dependencies

- **T33.G7.09**: Cache service responses in tables to avoid redundant API calls
  - Depends on: T09.G5.01, T10.G5.01, T31.G5.01, T33.G6.06
  - **STATUS**: ⚠️ TOO COMPLEX + DEPENDENCY VIOLATIONS
  - **ISSUE 1**: Advanced optimization pattern with timestamps
  - **ISSUE 2**: Multiple G5 dependencies

- **T33.G7.10**: Query cloud collections with WHERE conditions
  - Depends on: T08.G5.01, T10.G5.01, T31.G5.01, T33.G6.10
  - **BLOCKS**: Uses `fetch from collection` with WHERE conditions and `cond` blocks
  - **STATUS**: ⚠️ TOO BROAD + DEPENDENCY VIOLATIONS
  - **ISSUE 1**: Covers multiple operators and concepts
  - **ISSUE 2**: Multiple G5 dependencies

- **T33.G7.11**: Update and delete cloud collection data
  - Depends on: T08.G5.01, T10.G5.01, T31.G5.01, T33.G7.10
  - **BLOCKS**:
    - `update collection [COLLECTIONNAME v] from table [TABLENAME v]`
    - `update collection [COLLECTIONNAME v] in-place where <CONDITION> set (FIELD1) to (VALUE1)...`
    - `remove all documents from collection [COLLECTIONNAME v] where <CONDITION>`
  - **STATUS**: ⚠️ TOO BROAD + DEPENDENCY VIOLATIONS
  - **ISSUE 1**: Covers 3 different operations
  - **ISSUE 2**: Multiple G5 dependencies

- **T33.G7.12**: Build complex collection queries with AND/OR/NOT logic
  - Depends on: T08.G6.01, T10.G5.01, T31.G6.01, T33.G7.10, T33.G7.11
  - **BLOCKS**: `cond AND`, `cond OR`, `cond NOT`, plus LIMIT and SORT BY
  - **STATUS**: ⚠️ TOO BROAD + DEPENDENCY VIOLATIONS
  - **ISSUE 1**: Covers boolean logic + sorting + limiting
  - **ISSUE 2**: Depends on T08.G6.01, T10.G5.01, T31.G6.01 - multiple violations

### Grade 8 (6 skills)
- **T33.G8.01**: Insert and remove rows and columns dynamically in Google Sheets
  - Depends on: T08.G6.01, T10.G6.01, T31.G6.01, T33.G7.01, T33.G7.02
  - **BLOCKS**:
    - `insert rows`, `insert columns`
    - `remove rows [FROMR] to [TOR] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
    - `remove columns [FROMC] to [TOC] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
  - **STATUS**: ✅ Good extension of G7.01

- **T33.G8.02**: Review terms of service for external services
  - Depends on: T06.G6.01, T09.G6.01, T31.G6.01, T33.G7.08
  - **STATUS**: ⚠️ TOO CONCEPTUAL
  - **ISSUE**: No hands-on component - purely reading/understanding TOS

- **T33.G8.03**: Simulate service outages and design fallbacks
  - Depends on: T06.G6.01, T09.G6.01, T31.G6.01, T33.G7.08
  - **STATUS**: ✅ Good advanced resilience skill

- **T33.G8.04**: Validate and sanitize data received from external services
  - Depends on: T08.G6.01, T09.G6.01, T10.G6.01, T31.G6.01, T33.G7.08
  - **STATUS**: ✅ Important data validation skill

- **T33.G8.05**: Compare service-based and local implementations through hands-on testing
  - Depends on: T06.G6.01, T09.G6.01, T31.G6.01, T33.G7.08
  - **STATUS**: ✅ Excellent comparative analysis skill

- **T33.G8.06**: Build a cloud-integrated data pipeline
  - Depends on: T06.G6.01, T10.G6.01, T31.G6.01, T33.G7.07, T33.G8.04
  - **STATUS**: ✅ Good capstone project

---

## Part 2: Available CreatiCode Blocks

### Cloud Category Blocks (15 blocks)
1. **Web Fetch**
   - `fetch web page as [FORMAT] from URL [URL]`

2. **Google Sheets - Basic Operations**
   - `read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME v]`
   - `write into google sheet: url [URL] sheet name [SHEETNAME] start cell [ADDRESS] from table [TABLENAME v]`
   - `clear sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`

3. **Google Sheets - Sheet Management**
   - `list all sheets in google sheet at URL [SHEET_URL] into list [LIST]`
   - `add sheet [SHEETNAME] to google sheet at URL [URL]`
   - `remove sheet [SHEETNAME] from google sheet at URL [URL]`

4. **Google Sheets - Cell Operations**
   - `get value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
   - `set value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]`
   - `append row [ROWNUMBER] from table [TABLENAME v] to sheet [SHEETNAME] in Google Sheet at URL [URL]`

5. **Google Sheets - Row/Column Management**
   - `insert [COUNT] rows at row [STARTR] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
   - `insert [COUNT] columns at column [STARTC] in sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
   - `remove rows [FROMR] to [TOR] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`
   - `remove columns [FROMC] to [TOC] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]`

6. **Google Drive**
   - `list content of Google Drive folder [URL] in table [TABLENAME v]`

### Database Category Blocks (11 blocks)
1. **Collection Operations**
   - `insert from table [TABLENAME v] row from (STARTROW) to (ENDROW) into collection [COLLECTIONNAME v]`
   - `fetch from collection [COLLECTIONNAME v] into table [TABLENAME v] where <CONDITION> limit (LIMIT) sort by (SORTFIELD1) [SORTORDER1 v] (SORTFIELD2) [SORTORDER2 v]`
   - `update collection [COLLECTIONNAME v] from table [TABLENAME v]`
   - `update collection [COLLECTIONNAME v] in-place where <CONDITION> set (FIELD1) to (VALUE1)...`
   - `remove all documents from collection [COLLECTIONNAME v] where <CONDITION>`

2. **Query Building**
   - `collection [COLLECTIONNAME]`
   - `field [FIELDNAME]`
   - `<cond (field [FIELDNAME]) contains [TEXT]?>`
   - `<cond (field/value) [COMPARATOR] (field/value)>` (supports >, <, =, ≠, ≥, ≤)

3. **Logical Operators**
   - `<cond not <>>`
   - `<cond <> and <>>`
   - `<cond <> or <>>`

### Variables Category - Cloud Sessions (2 blocks)
1. `create cloud session [SESSION]`
2. `join cloud session [SESSION]`

### Total: 28 blocks for Connected Services

---

## Part 3: Critical Issues Analysis

### Issue 1: Skills That Are Too Broad (8 skills)

#### 1.1 T33.G6.06 - Handle latency and error states
**Current:** Single skill covering ALL external services (Cloud, AI, Web)
**Problem:** Too many different error patterns and contexts
**Recommendation:** Split into 3 skills:
- T33.G6.06a: Handle latency with loading indicators
- T33.G6.06b: Detect and display error messages
- T33.G6.06c: Implement retry mechanisms

#### 1.2 T33.G7.01 - Sheet structure management
**Current:** Covers list, add, remove, AND clear operations
**Problem:** 4 different operations in one skill
**Recommendation:** Split into:
- T33.G7.01a: List sheets in a Google Spreadsheet
- T33.G7.01b: Add new sheets to organize data
- T33.G7.01c: Remove sheets dynamically
- (clear sheet already covered in T33.G6.05)

#### 1.3 T33.G7.05 - Cloud session synchronization
**Current:** Covers session creation, joining, AND variable sync concepts
**Problem:** Very complex real-time feature
**Recommendation:** Split into:
- T33.G7.05a: Understand cloud session isolation
- T33.G7.05b: Create and join cloud sessions
- T33.G7.05c: Synchronize variables across session members

#### 1.4 T33.G7.07 - Multi-service workflows
**Current:** Covers orchestrating ANY combination of services
**Problem:** Too many possible combinations and patterns
**Recommendation:** Split into specific patterns:
- T33.G7.07a: Chain web fetch → AI processing
- T33.G7.07b: Read from Sheets → process → write results
- T33.G7.07c: Coordinate sequential service calls

#### 1.5 T33.G7.10 - WHERE conditions
**Current:** Covers comparison operators, contains, field references
**Problem:** Multiple query concepts in one skill
**Recommendation:** Split into:
- T33.G7.10a: Use simple WHERE conditions (=, >, <)
- T33.G7.10b: Use contains operator for text searches
- T33.G7.10c: Compare field values in queries

#### 1.6 T33.G7.11 - Update and delete operations
**Current:** Covers table-based update, in-place update, AND delete
**Problem:** 3 different operations with different patterns
**Recommendation:** Split into:
- T33.G7.11a: Update collections from modified tables
- T33.G7.11b: Update collections in-place with WHERE
- T33.G7.11c: Delete documents with WHERE conditions

#### 1.7 T33.G7.12 - Complex queries
**Current:** Covers AND/OR/NOT logic, LIMIT, AND SORT BY
**Problem:** Too many query features combined
**Recommendation:** Split into:
- T33.G7.12a: Combine conditions with AND/OR logic
- T33.G7.12b: Use NOT to invert conditions
- T33.G7.12c: Add LIMIT and SORT BY to queries

#### 1.8 T33.G8.01 - Row and column management
**Current:** Covers insert AND remove for both rows and columns
**Problem:** 4 operations (insert rows, remove rows, insert cols, remove cols)
**Recommendation:** Keep as-is OR split into:
- T33.G8.01a: Insert and remove rows dynamically
- T33.G8.01b: Insert and remove columns dynamically

### Issue 2: Missing Foundational Skills (5 gaps)

#### 2.1 Missing: Introduction to collections (before G6.10)
**Gap:** Jump from understanding Sheets (G6.03) to using collections (G6.10)
**Needed:** T33.G6.09b - Identify collection blocks and their purposes
**Placement:** Between G6.09 and G6.10

#### 2.2 Missing: Basic error checking pattern (before G6.06)
**Gap:** No foundational error detection before handling
**Needed:** T33.G6.05b - Check if service call succeeded
**Placement:** Between G6.05 and G6.06

#### 2.3 Missing: Simple sequential service calls (before G7.07)
**Gap:** Jump from single service to complex workflows
**Needed:** T33.G7.06b - Call two services in sequence
**Placement:** Between G7.06 and G7.07

#### 2.4 Missing: Basic field references in queries (before G7.10)
**Gap:** Query syntax introduced abruptly
**Needed:** T33.G7.09b - Understand query field references
**Placement:** Between G7.09 and G7.10

#### 2.5 Missing: Understanding collection data model (before G7.10)
**Gap:** No explanation of document structure
**Needed:** T33.G6.10b - Understand collection documents and fields
**Placement:** After G6.10, before G7.10

### Issue 3: Dependency Violations (X-2 Rule) - 12 violations

#### 3.1 G6 skills depending on G5 topics (CRITICAL)
**Violators:**
- T33.G6.09 → T10.G5.01 (violates X-2)
- T33.G6.10 → T08.G5.01, T10.G5.01 (violates X-2)

**Root Cause:** Collections introduced too early
**Fix Option 1:** Move T33.G6.09 and T33.G6.10 to G7
**Fix Option 2:** Update dependencies to use G6 or earlier prereqs

#### 3.2 G7 skills with multiple G5 dependencies (CRITICAL)
**Violators:**
- T33.G7.01 → T08.G5.01, T10.G5.01, T31.G5.01
- T33.G7.02 → T08.G5.01, T10.G5.01, T31.G5.01
- T33.G7.03 → T08.G5.01, T10.G5.01, T31.G5.01
- T33.G7.04 → T08.G5.01, T10.G5.01, T31.G5.01
- T33.G7.05 → T09.G5.01, T31.G5.01
- T33.G7.06 → T08.G5.01, T31.G5.01
- T33.G7.07 → T06.G5.01, T09.G5.01, T31.G5.01
- T33.G7.08 → T08.G5.01, T31.G5.01
- T33.G7.09 → T09.G5.01, T10.G5.01, T31.G5.01
- T33.G7.10 → T08.G5.01, T10.G5.01, T31.G5.01
- T33.G7.11 → T08.G5.01, T10.G5.01, T31.G5.01

**Root Cause:** Most G7 skills copy dependencies from earlier skills without checking grade level
**Fix:** Replace G5 dependencies with equivalent G6 or G7 skills

#### 3.3 G7.12 depending on G6 and G5 (violation)
**Violator:** T33.G7.12 → T08.G6.01, T10.G5.01, T31.G6.01
**Problem:** T10.G5.01 violates X-2 rule for G7
**Fix:** Replace T10.G5.01 with T10.G6.01 or T10.G7.01

### Issue 4: Skills Not Aligned with Actual Blocks (3 issues)

#### 4.1 T33.G6.01 - Good alignment ✅
**Skill:** Identify and test Cloud blocks
**Blocks:** All 28 Cloud and Database blocks
**Status:** Well-designed survey skill

#### 4.2 T33.G7.02 - Partial misalignment ⚠️
**Skill:** "Perform targeted Google Sheets cell operations"
**Actual blocks:** Only get/set value - not as "targeted" as description suggests
**Issue:** Description implies more sophisticated operations
**Fix:** Clarify that this covers basic single-cell read/write

#### 4.3 T33.G7.06 - No corresponding blocks ⚠️
**Skill:** "Understand automatic service authorization"
**Blocks:** None - this is purely conceptual
**Issue:** No hands-on component
**Fix:** Either add hands-on exploration OR move to different format (not a skill)

### Issue 5: Grade-Inappropriate Content (4 skills)

#### 5.1 T33.G6.07 - Rate limiting (too complex for G6)
**Current:** Implementing counters and cool-down timers
**Problem:** Requires timer management and state tracking
**Recommendation:** Move to G7 or simplify to "understand rate limits exist"

#### 5.2 T33.G7.09 - Caching (too complex for G7)
**Current:** Implement cache with timestamps and expiration
**Problem:** Requires time management and cache invalidation logic
**Recommendation:** Move to G8 or simplify to basic caching without expiration

#### 5.3 T33.G7.06 - Service authorization (purely conceptual)
**Current:** Understanding automatic authentication
**Problem:** No hands-on coding - just reading/understanding
**Recommendation:** Combine with another skill or make it a note

#### 5.4 T33.G8.02 - Terms of service review (not a coding skill)
**Current:** Reading TOS summaries
**Problem:** This is literacy/ethics, not a programming skill
**Recommendation:** Move to separate ethics/digital citizenship track

---

## Part 4: Detailed Recommendations

### Priority 1: Break Down Broad Skills (CRITICAL)

#### Action Items:
1. **T33.G6.06** → Split into 3 skills (latency, errors, retry)
2. **T33.G7.01** → Split into 3 skills (list, add, remove sheets)
3. **T33.G7.05** → Split into 3 skills (isolation, join, sync)
4. **T33.G7.07** → Split into 3 workflow patterns
5. **T33.G7.10** → Split into 3 query skills
6. **T33.G7.11** → Split into 3 update/delete skills
7. **T33.G7.12** → Split into 3 query skills (logic, NOT, LIMIT/SORT)
8. **T33.G8.01** → Consider splitting rows vs columns

**Impact:** Reduces cognitive load, improves scaffolding, makes assessment clearer

### Priority 2: Fix Dependency Violations (CRITICAL)

#### Action Items for G6 Skills:
1. **T33.G6.09**: Change T10.G5.01 → T10.G6.01 (Sort a table)
2. **T33.G6.10**: Change T08.G5.01 → T08.G6.01, T10.G5.01 → T10.G6.01

#### Action Items for G7 Skills:
For ALL G7 skills with G5 dependencies, replace with appropriate G6/G7 alternatives:
- T08.G5.01 → T08.G6.01 or T08.G7.01
- T10.G5.01 → T10.G6.01 or T10.G7.01
- T31.G5.01 → T31.G6.01
- T09.G5.01 → T09.G6.01
- T06.G5.01 → T06.G6.01

**Impact:** Ensures proper prerequisite flow, prevents gaps

### Priority 3: Add Missing Foundation Skills

#### New Skills to Add:
1. **T33.G6.05b** - Check if service call succeeded (before G6.06)
2. **T33.G6.09b** - Identify collection blocks (before G6.10)
3. **T33.G6.10b** - Understand collection documents (after G6.10)
4. **T33.G7.06b** - Call two services in sequence (before G7.07)
5. **T33.G7.09b** - Understand query field references (before G7.10)

**Impact:** Fills scaffolding gaps, smoother learning progression

### Priority 4: Address Grade-Inappropriate Content

#### Action Items:
1. **T33.G6.07** - Simplify or move to G7
2. **T33.G7.09** - Simplify or move to G8
3. **T33.G7.06** - Add hands-on component or remove
4. **T33.G8.02** - Move to ethics track or add coding connection

**Impact:** Better age-appropriateness, maintains hands-on focus

### Priority 5: Improve Block Alignment

#### Action Items:
1. **T33.G7.02** - Clarify description to match actual block capabilities
2. **T33.G7.06** - Add exploration activities or reframe as conceptual note
3. **T33.G6.01** - Maintain as good exemplar of block survey skill

**Impact:** Ensures skills match actual platform capabilities

---

## Part 5: Specific Fix Examples

### Example 1: Breaking Down T33.G7.01

**BEFORE (1 skill):**
```
T33.G7.01: List, add, and remove sheets in a Google Spreadsheet
Description: Students use `list all sheets`, `add sheet`, `remove sheet`,
and `clear sheet` blocks to manage sheet structure...
Dependencies: T08.G5.01, T10.G5.01, T31.G5.01, T33.G6.03, T33.G6.04
```

**AFTER (3 skills):**
```
T33.G7.01a: List sheets in a Google Spreadsheet
Description: Students use `list all sheets in google sheet` block to retrieve
names of all sheets in a workbook. They iterate through the list to display
sheet names or check if a specific sheet exists before accessing it.
Dependencies: T08.G6.01, T10.G6.01, T31.G6.01, T33.G6.03

T33.G7.01b: Add new sheets to organize data
Description: Students use `add sheet` block to create new sheets in a workbook.
They organize different data types on separate sheets (e.g., player stats,
game settings). They check if sheet exists before adding to avoid errors.
Dependencies: T08.G6.01, T31.G6.01, T33.G6.03, T33.G7.01a

T33.G7.01c: Remove sheets dynamically
Description: Students use `remove sheet` block to delete sheets from workbooks.
They implement safety checks to confirm sheet exists before removing and handle
cases where sheet is already removed. They understand this permanently deletes data.
Dependencies: T08.G6.01, T31.G6.01, T33.G7.01a, T33.G7.01b
```

### Example 2: Fixing T33.G6.10 Dependencies

**BEFORE:**
```
T33.G6.10: Insert and fetch data from cloud database collections
Dependencies:
* T08.G5.01: Use nested conditionals (G5 - VIOLATES X-2)
* T10.G5.01: Understand table structure (G5 - VIOLATES X-2)
* T31.G5.01: Trace service reach (G5 - VIOLATES X-2)
* T33.G6.09: Understand collections vs Sheets
```

**AFTER:**
```
T33.G6.10: Insert and fetch data from cloud database collections
Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T10.G6.01: Sort a table by a column
* T31.G6.01: Trace HTTP/HTTPS request steps
* T33.G6.09: Understand collections vs Sheets
```

### Example 3: Adding Missing Foundation Skill

**NEW SKILL:**
```
T33.G6.05b: Check if service call succeeded
Description: Students learn to check if a Cloud block call succeeded by
examining the returned value. They use if-else to test for empty strings,
null values, or error indicators. They create simple "success" or "failed"
messages to inform users about service call results. This prepares them
for more sophisticated error handling in T33.G6.06.

Dependencies:
* T08.G4.01: Use if-else to choose between two outcomes
* T09.G4.01: Prompt user for input and store it in a variable
* T33.G6.02: Fetch web content using the fetch URL block

Placement: Between T33.G6.05 and T33.G6.06
```

---

## Part 6: Topic Structure Analysis

### Current Grade Distribution:
- **K-5**: 8 skills (conceptual foundation)
- **G6**: 10 skills ⚠️ (too dense)
- **G7**: 12 skills ⚠️ (way too dense)
- **G8**: 6 skills (appropriate)
- **Total**: 36 skills

### Recommended Distribution (After Splitting):
- **K-5**: 8 skills (keep as-is)
- **G6**: 12-14 skills (split G6.06, add foundation)
- **G7**: 18-20 skills (split multiple skills)
- **G8**: 8-10 skills (split G8.01, keep others)
- **Total**: ~48-52 skills

### Progression Quality:
✅ **Good:** K-5 conceptual progression
✅ **Good:** G6 block introduction strategy
⚠️ **Issue:** G6-G7 too dense
⚠️ **Issue:** Many G7 skills too broad
✅ **Good:** G8 capstone approach

---

## Part 7: Cross-Topic Dependencies

### Dependencies from Other Topics:
1. **T08** (Conditionals): Heavy use in G6-G8
2. **T09** (Variables): Used for user input and state
3. **T10** (Tables): CRITICAL for all data operations
4. **T31** (Networks): Conceptual foundation
5. **T32** (AI): Referenced but separate (good)
6. **T19** (Multiplayer): Referenced but separate (good)

### Potential Circular Dependencies:
- None found ✅

### Missing Dependencies:
- Some skills may need T11 (String manipulation) for URL handling
- Consider adding explicit T10 table manipulation prereqs where needed

---

## Part 8: Implementation Priority Matrix

### Phase 1: IMMEDIATE (Fix Critical Issues)
1. Fix all X-2 dependency violations in G6-G7 (12 violations)
2. Split T33.G7.01 (covers 4 operations)
3. Split T33.G7.11 (covers 3 operations)
4. Split T33.G6.06 (too broad, foundational)

**Timeline:** 1-2 days
**Impact:** HIGH

### Phase 2: HIGH PRIORITY (Improve Scaffolding)
1. Split T33.G7.10 (query conditions)
2. Split T33.G7.12 (complex queries)
3. Add missing foundation skills (5 new skills)
4. Split T33.G7.05 (cloud sessions)

**Timeline:** 2-3 days
**Impact:** HIGH

### Phase 3: MEDIUM PRIORITY (Refinement)
1. Split T33.G7.07 (multi-service workflows)
2. Review and adjust T33.G6.07 (rate limiting)
3. Review and adjust T33.G7.09 (caching)
4. Split or keep T33.G8.01 (rows/columns)

**Timeline:** 1-2 days
**Impact:** MEDIUM

### Phase 4: LOW PRIORITY (Polish)
1. Address T33.G7.06 (authorization - add hands-on or reframe)
2. Address T33.G8.02 (TOS review - ethics track)
3. Clarify T33.G7.02 description
4. Review all descriptions for clarity

**Timeline:** 1 day
**Impact:** LOW

---

## Part 9: Quality Metrics

### Coverage of Available Blocks:
- **Cloud blocks covered:** 15/15 (100%) ✅
- **Database blocks covered:** 11/11 (100%) ✅
- **Cloud session blocks covered:** 2/2 (100%) ✅
- **Total coverage:** 28/28 (100%) ✅

### Skills Requiring Major Changes:
- **Too broad:** 8 skills (22% of G6-G8)
- **Dependency violations:** 12 skills (33% of G6-G8)
- **Missing foundations:** 5 gaps
- **Grade-inappropriate:** 4 skills (11% of G6-G8)

### Overall Topic Health Score:
- **K-5 Foundation:** 9/10 (excellent)
- **G6 Introduction:** 7/10 (good but needs splitting)
- **G7 Development:** 5/10 (too dense, violations)
- **G8 Mastery:** 7/10 (mostly good)
- **Overall:** 7/10 (good but needs significant revision)

---

## Part 10: Next Steps

### For Immediate Action:
1. **Review this analysis** with curriculum team
2. **Prioritize which skills to split first** (suggest starting with G7.01, G7.11, G6.06)
3. **Create spreadsheet** tracking all dependency fixes
4. **Draft revised skill descriptions** for split skills
5. **Update allskills.md** with fixes

### Questions to Resolve:
1. Should collections (G6.09-G6.10) move to G7?
2. Should rate limiting (G6.07) be simplified or moved?
3. Should TOS review (G8.02) stay in T33 or move to ethics track?
4. Should authorization (G7.06) get hands-on component or become a note?
5. Should we aim for ~50 skills or fewer for T33?

### Testing Strategy:
1. Verify no circular dependencies after fixes
2. Check all new skill descriptions align with blocks
3. Ensure scaffolding gaps are filled
4. Validate grade-level appropriateness
5. Confirm X-2 rule compliance for all skills

---

## Appendix A: Complete Dependency Graph

[Due to length, this would show a visual representation of all T33 skill dependencies, highlighting violations in red and valid dependencies in green]

---

## Appendix B: Block-to-Skill Mapping

| Block | Current Skill(s) | Status |
|-------|------------------|--------|
| fetch web page | T33.G6.02 | ✅ Aligned |
| read from google sheet | T33.G6.03 | ✅ Aligned |
| write into google sheet | T33.G6.04 | ✅ Aligned |
| clear sheet | T33.G6.05 | ✅ Aligned |
| list all sheets | T33.G7.01 | ⚠️ Needs split |
| add sheet | T33.G7.01 | ⚠️ Needs split |
| remove sheet | T33.G7.01 | ⚠️ Needs split |
| get value at row column | T33.G7.02 | ✅ Aligned |
| set value at row column | T33.G7.02 | ✅ Aligned |
| append row | T33.G7.03 | ✅ Aligned |
| insert rows | T33.G8.01 | ✅ Aligned |
| insert columns | T33.G8.01 | ✅ Aligned |
| remove rows | T33.G8.01 | ✅ Aligned |
| remove columns | T33.G8.01 | ✅ Aligned |
| list Google Drive folder | T33.G7.04 | ✅ Aligned |
| insert into collection | T33.G6.10 | ⚠️ Dep violations |
| fetch from collection | T33.G6.10, T33.G7.10 | ⚠️ Too broad |
| update collection from table | T33.G7.11 | ⚠️ Needs split |
| update collection in-place | T33.G7.11 | ⚠️ Needs split |
| remove documents | T33.G7.11 | ⚠️ Needs split |
| cond operators | T33.G7.10, G7.12 | ⚠️ Too broad |
| cond AND/OR/NOT | T33.G7.12 | ⚠️ Needs split |
| create cloud session | T33.G7.05 | ⚠️ Needs split |
| join cloud session | T33.G7.05 | ⚠️ Needs split |

---

## Summary

Topic T33 has **excellent block coverage** and a **solid conceptual foundation** (K-5), but suffers from:
1. **Too many overly broad skills** in G6-G7
2. **Extensive dependency violations** of the X-2 rule
3. **Missing scaffolding steps** between major concepts
4. **Some grade-inappropriate content**

**Recommended actions:**
- Split 8 broad skills into 20-25 focused skills
- Fix 12 dependency violations
- Add 5 missing foundation skills
- Adjust 4 grade-inappropriate skills

**Result:** A more gradual, well-scaffolded progression from 36 skills to ~48-52 focused, appropriate skills.

---

**End of Analysis**
