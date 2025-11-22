# T31 (Internet & Cloud) - Phase 1 Optimization Analysis

## Executive Summary

**Total T31 Skills:** 37 skills (K-8)
**Major Issues Found:** 18 high-priority, 12 medium-priority, 7 low-priority issues
**Topic Overlap:** Significant confusion between T31 (Internet & Cloud) and T33 (Connected Services & Tool Wrappers)

### Critical Finding
There is **substantial topic confusion** between T31 and T33. Many skills currently in T31 should be in T33, and vice versa. T31 should focus on networking concepts, protocols, and infrastructure, while T33 should focus on using specific cloud services (Google Sheets, Database, Multiplayer).

---

## Part 1: CreatiCode Platform Features Available

### A. Cloud Category Blocks (14 blocks)

#### Google Sheets Operations
1. **fetch web page as [FORMAT] from URL [URL]**
   - Fetches web content as markdown or other formats

2. **read from google sheet: url [URL] sheet name [SHEETNAME] range [RANGE] into table [TABLENAME]**
   - Reads data from Google Sheets into a table

3. **write into google sheet: url [URL] sheet name [SHEETNAME] starting cell [ADDRESS] from table [TABLENAME]**
   - Writes table data to Google Sheets

4. **value at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]**
   - Gets individual cell value

5. **set value to [VALUE] at row (ROW) column (COL) of sheet [SHEETNAME] in Google Sheet at URL [URL]**
   - Sets individual cell value

6. **append row [ROWNUMBER] from table [TABLENAME] to sheet [SHEETNAME] in Google Sheet at URL [URL]**
   - Appends row to existing sheet data

7. **list all sheets in google sheet at URL [SHEET_URL] into list [LIST]**
   - Lists all sheets in a spreadsheet

8. **add sheet [SHEETNAME] to google sheet at URL [URL]**
   - Creates new sheet in spreadsheet

9. **remove sheet [SHEETNAME] from google sheet at URL [URL]**
   - Removes sheet from spreadsheet

10. **clear sheet [SHEETNAME] in Google Sheet at URL [SHEET_URL]**
    - Clears all content from sheet

11. **insert [COUNT] rows at row [STARTR] in sheet [SHEETNAME] in Google Sheet at URL [SHEET_URL]**
    - Inserts rows dynamically

12. **insert [COUNT] columns at column [STARTC] in sheet [SHEETNAME] in Google Sheet at URL [SHEET_URL]**
    - Inserts columns dynamically

13. **remove rows [FROMR] to [TOR] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]**
    - Removes row range

14. **remove columns [FROMC] to [TOC] from sheet [SHEET_NAME] in Google Sheet at URL [SHEET_URL]**
    - Removes column range

#### Google Drive Operations
15. **list content of Google Drive folder [URL] in table [TABLENAME]**
    - Lists files in a shared Drive folder

### B. Multiplayer Category Blocks (13 blocks)

1. **create game named [GAMENAME] password [PASSWORD] my name [HOSTNAME] role [ROLE] server [LOCATION] capacity (CAPACITY) world width (W) height (H)**
   - Creates multiplayer game session

2. **join multiplayer game named [GAMENAME] by host [HOSTNAME] from server [LOCATION] with password [PASSWORD] my name [DISPLAYNAME] role [ROLE]**
   - Joins existing multiplayer game

3. **list multiplayer games in server [LOCATION] in table [TABLE]**
   - Lists available games on server

4. **list players in game [GAMENAME] hosted by [HOSTNAME] from server [LOCATION] in table [TABLE]**
   - Lists players in a game session

5. **add this sprite to game as a [MODE] [SHAPE]**
   - Adds sprite to multiplayer game world

6. **when added to game** (hat block)
   - Event triggered when sprite joins game

7. **remove this sprite from game**
   - Removes sprite from game world

8. **synchronously set speed x (X) y (Y)**
   - Syncs sprite velocity across players

9. **synchronously set speed (SPEED) dir (DIR)**
   - Syncs sprite speed/direction across players

10. **broadcast [MESSAGE] with parameter [PARAMETER] mode [MODE]**
    - Sends messages in multiplayer context

11. **when touching [SPRITENAME] will [STOPTYPE] and trigger [MESSAGE] with parameter [PARAMETER]**
    - Collision detection in multiplayer

12. **connected to game** (boolean)
    - Checks multiplayer connection status

13. **reset game world**
    - Resets the multiplayer game state

### C. Database Category Blocks (12 blocks)

1. **insert from table [TABLENAME] row from (STARTROW) to (ENDROW) into collection [COLLECTIONNAME]**
   - Inserts table rows into database collection

2. **fetch from collection [COLLECTIONNAME] into table [TABLENAME] where <CONDITION> limit (LIMIT) sort by (SORTFIELD1) [SORTORDER1] (SORTFIELD2) [SORTORDER2]**
   - Fetches documents from collection with queries

3. **remove all documents from collection [COLLECTIONNAME] where <CONDITION>**
   - Removes documents matching condition

4. **update collection [COLLECTIONNAME] from table [TABLENAME]**
   - Updates collection from table data

5. **update collection [COLLECTIONNAME] in-place where <CONDITION> set (FIELD1) to (VALUE1)...**
   - Updates specific fields in matching documents

6. **collection [COLLECTIONNAME]** (reporter)
   - Collection name reporter

7. **field [FIELDNAME]** (reporter)
   - Field name reporter for queries

8. **<cond [INPUT1] [COMPARATOR] [INPUT2]>** (boolean)
   - Comparison condition for queries

9. **<cond (field [FIELDNAME]) contains [TEXT]?>** (boolean)
   - Text contains condition

10. **<cond not <>>** (boolean)
    - NOT operator

11. **<cond <> and <>>** (boolean)
    - AND operator

12. **<cond <> or <>>** (boolean)
    - OR operator

### D. Game Category - Persistent Data Blocks (5 blocks)

1. **record player score (VALUE)**
   - Records score for leaderboard

2. **show game leaderboard [SORT] rows [ROWS] header [HEADER_COLOR] background [BACKGROUND_COLOR]**
   - Displays leaderboard on stage

3. **hide game leaderboard**
   - Hides leaderboard

4. **clear scores for [WHO]**
   - Clears scores (my scores vs all users)

5. **store user data key [KEY] value [VALUE]**
   - Stores persistent user data

6. **read user data key [KEY]** (reporter)
   - Reads persistent user data

### E. Other Network-Related Blocks

1. **read URL parameter [PARAMETER]** (Sensing category)
   - Reads query parameters from project URL

2. **add costume named [NAME] from URL [URL] max width (W) max height (H)** (Looks category)
   - Loads image from URL as costume

3. **Various AI blocks that require internet** (covered in T21-T24 topics)
   - Text-to-speech, speech recognition, ChatGPT, DALL-E, etc.

---

## Part 2: Current T31 Skills Analysis

### Kindergarten (1 skill)

#### T31.GK.01 ✅ GOOD
**Skill:** Recognize devices that connect to the internet (picture-based)
**Status:** Appropriate - picture-based for K level
**Issues:** None

---

### Grade 1 (1 skill)

#### T31.G1.01 ✅ GOOD
**Skill:** Identify when a device is connected or disconnected (picture-based)
**Status:** Appropriate - picture-based for Grade 1
**Issues:** None

---

### Grade 2 (2 skills)

#### T31.G2.01 ✅ GOOD
**Skill:** Understand that the internet connects many computers (picture-based)
**Status:** Appropriate - foundational network concept
**Issues:** None

#### T31.G2.02 ✅ GOOD
**Skill:** Practice safe online behavior (picture-based)
**Status:** Appropriate for Grade 2
**Issues:** None - but note this overlaps with T32 (Cybersecurity). Consider if this belongs in T32 instead.

---

### Grade 3 (2 skills)

#### T31.G3.01 ✅ GOOD
**Skill:** Trace a simple path from device to website
**Status:** Appropriate - introduces network path concept
**Issues:** None

#### T31.G3.02 ✅ GOOD
**Skill:** Recognize different types of online information sharing
**Status:** Appropriate - conceptual understanding
**Issues:** None

---

### Grade 4 (2 skills)

#### T31.G4.01 ✅ GOOD
**Skill:** Explain how data travels across the internet
**Status:** Appropriate - packet concept
**Issues:** None

#### T31.G4.02 ⚠️ MINOR ISSUE
**Skill:** Identify secure vs insecure websites
**Status:** Conceptual security skill
**Issue:** This might belong in T32 (Cybersecurity) instead of T31. LOW PRIORITY.

---

### Grade 5 (5 skills)

#### T31.G5.01 ✅ GOOD
**Skill:** Trace how a device reaches an online service
**Status:** Appropriate progression from G4.01
**Issues:** None

#### T31.G5.02 ✅ GOOD
**Skill:** Decide when apps need the internet vs work offline
**Status:** Good conceptual skill
**Issues:** None

#### T31.G5.03 🔴 HIGH PRIORITY - MOVE TO T33
**Skill:** Fetch and display a web page as markdown
**Current Location:** T31
**Should Be:** T33 (Connected Services)
**Reason:** This is using a specific CreatiCode Cloud block, not teaching networking concepts. T33 is for "tool wrappers" and service usage.
**Block Used:** `fetch web page as [markdown] from URL`
**Recommendation:** MOVE to T33.G6.02 (which already exists and covers this)

#### T31.G5.04 🔴 HIGH PRIORITY - MOVE TO T19 or create T19 cross-reference
**Skill:** Create and join a multiplayer game session
**Current Location:** T31
**Issue:** This should be in T19 (Multiplayer/Physics) topic, not Internet & Cloud
**Block Used:** Multiplayer category blocks
**Recommendation:** MOVE to T19 or create T19 topic if it doesn't exist. If keeping cross-reference in T31, make it conceptual only.

#### T31.G5.05 🔴 HIGH PRIORITY - MOVE TO T19
**Skill:** Check multiplayer connection status
**Current Location:** T31
**Issue:** Same as G5.04 - belongs in T19
**Recommendation:** MOVE to T19

---

### Grade 6 (7 skills)

#### T31.G6.01 ✅ GOOD
**Skill:** Trace the steps of an HTTP/HTTPS request
**Status:** Appropriate - core networking concept
**Issues:** None

#### T31.G6.02 🔴 HIGH PRIORITY - MOVE TO T33
**Skill:** Read data from a Google Sheet cell
**Current Location:** T31
**Should Be:** T33
**Reason:** Using specific CreatiCode service blocks, not networking concepts
**Recommendation:** MOVE to T33 (this is duplicate of T33.G6.03)

#### T31.G6.03 🔴 HIGH PRIORITY - MOVE TO T33
**Skill:** Write data to a Google Sheet cell
**Current Location:** T31
**Should Be:** T33
**Recommendation:** MOVE to T33 (this is duplicate of T33.G6.04)

#### T31.G6.03.01 🔴 HIGH PRIORITY - MOVE TO T33
**Skill:** Update entire rows in Google Sheets
**Current Location:** T31
**Should Be:** T33
**Issues:**
1. **ID numbering violation** - G6.03.01 implies it's a sub-skill of G6.03, but they're peers
2. Should be T33 skill
**Recommendation:** MOVE to T33 and renumber (maybe T33.G7.03)

#### T31.G6.03.02 🔴 HIGH PRIORITY - MOVE TO T33
**Skill:** List and manage multiple Google Sheets
**Current Location:** T31
**Should Be:** T33
**Issues:** Same as G6.03.01
**Recommendation:** MOVE to T33 (this is duplicate of T33.G7.01)

#### T31.G6.04 ⚠️ MEDIUM PRIORITY - KEEP BUT CLARIFY
**Skill:** Measure and analyze how latency affects AI responsiveness and fairness
**Status:** Conceptual networking/latency skill
**Issues:**
1. Heavy dependency on T21-T24 AI topics
2. Could be clearer about what CreatiCode blocks to use (timer blocks)
3. Vague on implementation
**Recommendation:** KEEP in T31 but add specific implementation details using timer blocks and sample measurements

#### T31.G6.05 ⚠️ MEDIUM PRIORITY - MIGHT BELONG IN T32 or T35
**Skill:** Evaluate privacy when sharing AI-generated content and data
**Status:** Privacy/ethics skill
**Issues:**
1. This seems more like T32 (Cybersecurity) or T35 (Ethics) content
2. Not specifically about networking/cloud infrastructure
**Recommendation:** Consider moving to T32 or T35, or keep as cross-topic skill

#### T31.G6.06 🔴 HIGH PRIORITY - MOVE TO T19
**Skill:** Add sprites to multiplayer game world
**Current Location:** T31
**Should Be:** T19 (Multiplayer)
**Recommendation:** MOVE to T19

---

### Grade 7 (8 skills)

#### T31.G7.01 🔴 HIGH PRIORITY - MOVE TO T19
**Skill:** Model a distributed multiplayer server
**Current Location:** T31
**Issues:**
1. This is more T19 (Multiplayer implementation) content
2. Could also work as networking architecture skill in T31 if made more general
**Recommendation:** Either MOVE to T19 or make it a general distributed systems architecture skill (not multiplayer-specific)

#### T31.G7.02 🔴 HIGH PRIORITY - MOVE TO T19
**Skill:** Synchronize sprite movement in multiplayer games
**Current Location:** T31
**Should Be:** T19
**Recommendation:** MOVE to T19

#### T31.G7.02.01 🔴 HIGH PRIORITY - MOVE TO T19
**Skill:** Broadcast messages in multiplayer games
**Issues:**
1. Should be in T19
2. **ID numbering violation** - shouldn't use G7.02.01 format
**Recommendation:** MOVE to T19 and renumber

#### T31.G7.02.02 🔴 HIGH PRIORITY - MOVE TO T19
**Skill:** Handle sprite collisions in multiplayer games
**Issues:** Same as G7.02.01
**Recommendation:** MOVE to T19 and renumber

#### T31.G7.02.03 🔴 HIGH PRIORITY - MOVE TO T33
**Skill:** Insert data into a database collection
**Current Location:** T31
**Should Be:** T33
**Issues:**
1. Database blocks are service usage, not networking concepts
2. **ID numbering violation**
**Recommendation:** MOVE to T33

#### T31.G7.02.04 🔴 HIGH PRIORITY - MOVE TO T33
**Skill:** Fetch data from a database collection
**Issues:** Same as G7.02.03
**Recommendation:** MOVE to T33

#### T31.G7.02.05 🔴 HIGH PRIORITY - MOVE TO T33
**Skill:** Update and remove database records
**Issues:** Same as G7.02.03
**Recommendation:** MOVE to T33

#### T31.G7.03 ✅ GOOD
**Skill:** Compare network topology options
**Status:** Excellent networking concept skill
**Issues:** None

#### T31.G7.04 ✅ GOOD
**Skill:** Client-server vs peer-to-peer architecture
**Status:** Core networking architecture concept
**Issues:** None

#### T31.G7.05 ✅ GOOD
**Skill:** Analyze societal impacts of networked systems
**Status:** Appropriate high-level thinking skill
**Issues:** None

---

### Grade 8 (6 skills)

#### T31.G8.01 ⚠️ MEDIUM PRIORITY - CLARIFY
**Skill:** Architect edge vs cloud processing pipelines for AI
**Status:** Good conceptual skill
**Issues:**
1. Very AI-heavy (T21-T24 dependencies)
2. Not clear what CreatiCode blocks demonstrate this
3. More conceptual than hands-on
**Recommendation:** KEEP but clarify it's a diagramming/design skill, not implementation. Add example scenarios.

#### T31.G8.02 ⚠️ MEDIUM PRIORITY - CLARIFY
**Skill:** Understand AI service network requirements
**Status:** Conceptual networking skill
**Issues:** Similar to G8.01 - needs clarification on implementation
**Recommendation:** KEEP but add specific analysis tasks (bandwidth estimation, latency requirements)

#### T31.G8.03 ⚠️ MEDIUM PRIORITY - MIGHT BELONG IN T32
**Skill:** Design secure AI-powered cloud systems
**Status:** Security-focused
**Issues:** This seems more T32 (Cybersecurity) than T31
**Recommendation:** Consider moving to T32 or keeping as cross-topic skill

#### T31.G8.04 🔴 HIGH PRIORITY - BELONGS IN T32 or T33
**Skill:** Implement privacy protection for AI data
**Current Location:** T31
**Should Be:** T32 (Cybersecurity) or T33 if implementation-focused
**Issues:** This is clearly security/privacy, not networking architecture
**Recommendation:** MOVE to T32

#### T31.G8.05 ⚠️ MEDIUM PRIORITY - CLARIFY
**Skill:** Evaluate AI service resilience and fallbacks
**Status:** Good systems design skill
**Issues:** Not clear how to implement in CreatiCode
**Recommendation:** KEEP but add specific implementation guidance (error handling, caching patterns)

#### T31.G8.06 ⚠️ MEDIUM PRIORITY - TOO ADVANCED
**Skill:** Build AI service monitoring and ethics dashboards
**Status:** Very advanced capstone skill
**Issues:**
1. Requires extensive dashboard/UI building
2. Not clear what CreatiCode blocks support this
3. Might be too ambitious for Grade 8
**Recommendation:** Either simplify to "Track AI service usage metrics" or move to advanced track

---

## Part 3: Issues Summary

### High Priority Issues (18 issues)

#### Topic Confusion - Skills in Wrong Topic
1. **T31.G5.03** - Move to T33 (web fetch)
2. **T31.G5.04** - Move to T19 (multiplayer create/join)
3. **T31.G5.05** - Move to T19 (multiplayer connection status)
4. **T31.G6.02** - Move to T33 (Google Sheets read)
5. **T31.G6.03** - Move to T33 (Google Sheets write)
6. **T31.G6.03.01** - Move to T33 (Google Sheets rows)
7. **T31.G6.03.02** - Move to T33 (Google Sheets multiple sheets)
8. **T31.G6.06** - Move to T19 (multiplayer sprites)
9. **T31.G7.01** - Move to T19 (multiplayer server model)
10. **T31.G7.02** - Move to T19 (multiplayer movement sync)
11. **T31.G7.02.01** - Move to T19 (multiplayer broadcast)
12. **T31.G7.02.02** - Move to T19 (multiplayer collisions)
13. **T31.G7.02.03** - Move to T33 (database insert)
14. **T31.G7.02.04** - Move to T33 (database fetch)
15. **T31.G7.02.05** - Move to T33 (database update/remove)
16. **T31.G8.04** - Move to T32 (privacy/security)

#### ID Numbering Violations
17. **T31.G6.03.01** - Invalid numbering (should be G6.04 or G7.01)
18. **T31.G6.03.02** - Invalid numbering (should be G6.05 or G7.02)
19. **T31.G7.02.01-05** - Five skills with invalid numbering

### Medium Priority Issues (12 issues)

1. **T31.G6.04** - Needs implementation details (timer blocks, specific measurements)
2. **T31.G6.05** - Consider moving to T32 or T35
3. **T31.G8.01** - Needs clarification - more design than implementation
4. **T31.G8.02** - Needs specific analysis tasks
5. **T31.G8.03** - Consider moving to T32
6. **T31.G8.05** - Needs implementation guidance
7. **T31.G8.06** - Too advanced, needs simplification
8. **Missing Grade 3 hands-on skill** - No CreatiCode blocks introduced in Grade 3
9. **Missing Grade 4 hands-on skill** - No CreatiCode blocks introduced in Grade 4
10. **Missing Grade 5 hands-on basics** - Jumped straight to web fetch without simpler intro
11. **Missing persistent data skills** - Game category blocks (leaderboard, user data) not covered
12. **Missing URL parameter skill** - Sensing block `read URL parameter` not covered

### Low Priority Issues (7 issues)

1. **T31.G2.02** - Consider if belongs in T32 instead
2. **T31.G4.02** - Consider if belongs in T32 instead
3. **Missing scaffolding K-2 to 3** - Could add transition skill
4. **Missing network troubleshooting concepts** - No skills about debugging connection issues
5. **Missing bandwidth/data transfer concepts** - No skills about how much data different activities use
6. **Missing local vs cloud storage comparison** - Conceptual understanding (though T33.G5.01 covers this)
7. **T31 has too much AI cross-dependency** - Many Grade 6-8 skills heavily reference T21-T24

---

## Part 4: Missing Skills (What Should Be Added)

### Grade 3 Missing Skills

#### Recommended: Add simple network communication concept
**Skill ID:** T31.G3.03
**Skill:** Understand that programs can send and receive information
**Description:** Students learn that programs can communicate with other programs over the internet. They identify examples: messaging apps send text to friends, games receive updates from servers, weather apps fetch current conditions. This prepares for actual implementation in later grades.
**Dependencies:** T31.G3.01
**Blocks:** None (conceptual only)

### Grade 4 Missing Skills

#### Recommended: Add network speed/bandwidth concept
**Skill ID:** T31.G4.03
**Skill:** Understand that different internet activities use different amounts of data
**Description:** Students categorize activities by data usage (low: text messages, medium: music streaming, high: video streaming, very high: video calls). They understand that faster internet connections can handle more data and multiple activities simultaneously.
**Dependencies:** T31.G4.01
**Blocks:** None (conceptual only)

### Grade 5 Missing Skills

#### Recommended: Add URL parameter reading (before web fetch)
**Skill ID:** T31.G5.03 (RENUMBERED from current)
**Skill:** Read and use URL parameters in projects
**Description:** Students use CreatiCode's `read URL parameter [PARAMETER]` block to read query parameters from the project URL (e.g., ?question=1). They understand how URLs can pass information to programs and create projects that behave differently based on URL parameters.
**Dependencies:** T09.G3.01.04 (variables), T31.G5.01
**Blocks:** `read URL parameter [PARAMETER]` (Sensing category)

#### Recommended: Add persistent user data storage
**Skill ID:** T31.G5.06
**Skill:** Store and retrieve user data in the cloud
**Description:** Students use `store user data key [KEY] value [VALUE]` and `read user data key [KEY]` blocks to save user preferences or game progress that persists across sessions. They understand that data is stored per-user and per-project on CreatiCode's servers.
**Dependencies:** T09.G4.04 (variables), T31.G5.01
**Blocks:** `store user data key`, `read user data key` (Game category)

### Grade 6 Missing Skills

#### Recommended: Add game leaderboard feature
**Skill ID:** T31.G6.07
**Skill:** Record scores and display leaderboards
**Description:** Students use `record player score (VALUE)` to save scores and `show game leaderboard` to display top players. They understand how leaderboards aggregate data from all users and sort by highest/lowest scores.
**Dependencies:** T09.G4.04 (variables), T31.G5.06 (user data)
**Blocks:** `record player score`, `show game leaderboard`, `clear scores for` (Game category)

### Grade 7 Missing Skills

#### Recommended: Add network troubleshooting/error handling
**Skill ID:** T31.G7.06
**Skill:** Handle network errors and offline states
**Description:** Students implement error handling for network operations: checking if web fetch returns empty results, detecting offline status, showing user-friendly error messages. They understand that network operations can fail and programs should handle failures gracefully.
**Dependencies:** T08.G5.01 (conditionals), T31.G6.01 (HTTP requests)
**Blocks:** Various Cloud/Multiplayer blocks with error checking

---

## Part 5: Recommendations

### A. Critical Actions (Must Do)

#### 1. Clarify T31 vs T33 Scope
**Current Problem:** 15+ skills in wrong topic
**Recommendation:**
- **T31 (Internet & Cloud)** should focus on:
  - Networking concepts (how internet works)
  - Protocols (HTTP/HTTPS)
  - Network architecture (client-server, P2P)
  - Latency, bandwidth, connectivity concepts
  - General cloud computing concepts
  - Societal impacts of networked systems

- **T33 (Connected Services)** should focus on:
  - Using specific CreatiCode service blocks
  - Google Sheets integration
  - Database operations
  - Web fetch implementation
  - Service error handling
  - API rate limiting

#### 2. Create or Identify T19 (Multiplayer/Physics)
**Current Problem:** 8 multiplayer skills incorrectly in T31
**Recommendation:**
- If T19 exists, MOVE all multiplayer skills there
- If T19 doesn't exist, create it or identify correct topic for multiplayer
- Keep only conceptual "distributed systems" skill in T31 if appropriate

#### 3. Fix ID Numbering Violations
**Current Problem:** 7 skills with invalid IDs (G6.03.01, G7.02.01, etc.)
**Recommendation:** Renumber all skills to follow X.GN.MM format (no three-level numbering)

### B. Structural Improvements

#### 4. Add Missing Scaffolding Skills
**Grades 3-5 Gap:** No hands-on blocks until G5, then jump straight to complex web fetch
**Recommendation:**
- Add URL parameter reading in G5 (simpler than web fetch)
- Add user data storage in G5 (simpler than Google Sheets)
- Add leaderboard in G6 (builds on user data)
- Add conceptual skills in G3-G4 to prepare

#### 5. Reduce AI Cross-Dependencies
**Current Problem:** 11 skills heavily reference T21-T24
**Recommendation:**
- Keep conceptual skills (G6.04, G8.01, G8.02) but make them less AI-specific
- Make skills applicable to any cloud service, not just AI
- Provide non-AI examples as well as AI examples

#### 6. Strengthen Core Networking Content
**Missing Areas:**
- Network troubleshooting
- Bandwidth/data usage concepts
- Connection quality concepts
- DNS/domain names
- IP addresses (basic concept)

**Recommendation:** Add 2-3 skills covering these fundamentals

### C. Skill-Level Fixes

#### 7. Clarify Implementation vs Conceptual Skills
**Problem:** Some G8 skills unclear if hands-on or conceptual
**Recommendation:**
- T31.G8.01 - Mark as "design/diagramming" skill
- T31.G8.02 - Add specific analysis metrics to measure
- T31.G8.05 - Add specific error handling patterns
- T31.G8.06 - Simplify to "Track service usage metrics"

#### 8. Review Security/Privacy Skills for T32 Movement
**Candidates for T32:**
- T31.G2.02 (safe online behavior)
- T31.G4.02 (secure websites)
- T31.G6.05 (privacy of AI data)
- T31.G8.03 (secure cloud systems)
- T31.G8.04 (privacy protection)

**Recommendation:** Review with T32 topic to determine best placement

---

## Part 6: Proposed Reorganization

### Option A: Minimal Changes (Fix Critical Issues Only)

**Actions:**
1. Move 15 skills to T33 (Google Sheets, Database, Web Fetch implementation)
2. Move 8 skills to T19 (Multiplayer)
3. Fix ID numbering for 7 skills
4. Add 3-4 missing skills (URL params, user data, leaderboard)

**Result:** T31 would have ~20 skills (down from 37), focused on networking concepts

### Option B: Complete Restructure (Recommended)

**T31 Grade Progression:**

**K-2:** Foundational concepts (keep current 4 skills)
- GK.01: Recognize internet-connected devices ✅
- G1.01: Connected vs disconnected ✅
- G2.01: Internet connects computers ✅
- G2.02: Safe online behavior (or move to T32)

**Grade 3:** Basic network concepts (2 skills)
- G3.01: Trace path from device to website ✅
- G3.02: Types of online information sharing ✅
- **NEW G3.03:** Programs can send/receive information

**Grade 4:** Data transfer concepts (3 skills)
- G4.01: How data travels (packets) ✅
- G4.02: Secure vs insecure websites (or move to T32)
- **NEW G4.03:** Different activities use different data amounts

**Grade 5:** Introduction to connectivity (4-5 skills)
- G5.01: Trace device to online service ✅
- G5.02: Apps need internet vs offline ✅
- **NEW G5.03:** Read URL parameters (hands-on intro)
- **NEW G5.04:** Store/retrieve user data in cloud (hands-on)
- **KEEP conceptual reference:** Understanding multiplayer sessions exist

**Grade 6:** HTTP/HTTPS and basic cloud concepts (4-5 skills)
- G6.01: Trace HTTP/HTTPS request ✅
- G6.02: Measure latency effects (clarified) ✅
- **NEW G6.03:** Record scores and leaderboards (hands-on)
- G6.04: Privacy of cloud data (or move to T32)
- **OPTIONAL:** Basic DNS concept

**Grade 7:** Network architecture (4-5 skills)
- G7.01: Network topology options ✅
- G7.02: Client-server vs P2P ✅
- G7.03: Societal impacts of networks ✅
- **NEW G7.04:** Handle network errors/offline states
- **OPTIONAL:** Distributed systems concepts (generic, not multiplayer-specific)

**Grade 8:** Advanced systems design (4-5 skills)
- G8.01: Edge vs cloud processing (clarified as design) ✅
- G8.02: Service network requirements (add metrics) ✅
- **G8.03:** System resilience and fallbacks (clarified) ✅
- **OPTIONAL:** Network performance optimization
- **OPTIONAL:** Cloud storage architectures

**Total: ~23-27 skills** (compared to current 37)

---

## Part 7: Detailed Block Coverage Gap Analysis

### Blocks Currently Covered in T31 Skills

#### Cloud Category
- ❌ fetch web page (WRONGLY in T31.G5.03, should be T33)
- ❌ All Google Sheets blocks (WRONGLY in T31.G6.02-G6.03.02, should be T33)
- ❌ Google Drive blocks (NOT COVERED ANYWHERE)

#### Multiplayer Category
- ❌ All multiplayer blocks (WRONGLY in T31.G5.04-G7.02.02, should be T19)

#### Database Category
- ❌ All database blocks (WRONGLY in T31.G7.02.03-05, should be T33)

#### Game Category (Persistent Data)
- ❌ record player score (NOT COVERED)
- ❌ show/hide leaderboard (NOT COVERED)
- ❌ clear scores (NOT COVERED)
- ❌ store user data (NOT COVERED)
- ❌ read user data (NOT COVERED)

#### Sensing Category
- ❌ read URL parameter (NOT COVERED)

### Blocks That SHOULD Be in T31 (Conceptual References Only)
- Connection status concepts (not specific blocks)
- Network request concepts (HTTP/HTTPS)
- Latency/performance concepts (using timer blocks)
- Cloud storage concepts (conceptual, specific implementation in T33)

### Blocks for T33 (Connected Services)
All the Cloud, Database, and Game persistent data blocks should be systematically covered in T33, NOT T31.

---

## Part 8: Action Items Priority List

### Immediate (Before any other topics)
1. ✅ Decide on T19 existence/location for multiplayer skills
2. ✅ Define clear boundary between T31 and T33
3. ✅ Fix 7 ID numbering violations

### High Priority (Phase 1)
4. ⬜ Move 8 multiplayer skills to T19
5. ⬜ Move 7 Google Sheets/Database skills to T33
6. ⬜ Add 3 missing skills: URL params (G5), user data (G5), leaderboard (G6)
7. ⬜ Clarify 4 vague G8 skills (add implementation details or mark as conceptual)

### Medium Priority (Phase 2)
8. ⬜ Add 2-3 conceptual skills for G3-G4 scaffolding
9. ⬜ Review 5 security/privacy skills for possible T32 movement
10. ⬜ Add network troubleshooting skill (G7)
11. ⬜ Reduce AI-specific language in cross-topic skills

### Low Priority (Future)
12. ⬜ Add advanced networking concepts (DNS, IP addresses basics)
13. ⬜ Add bandwidth/data usage concepts
14. ⬜ Add network performance optimization concepts

---

## Part 9: Cross-Topic Dependencies to Review

### Dependencies FROM T31 (other topics depend on T31)
Many topics reference T31.G5.01 and T31.G6.01 - these should remain stable.

**Most referenced T31 skills:**
- T31.G5.01 (Trace device to service) - 47 references across T33, T21-T24
- T31.G6.01 (HTTP/HTTPS request) - 12 references

**Skills being moved/renumbered:**
- T31.G5.03 → T33 (will break 2 dependencies)
- T31.G5.04-05 → T19 (will break 3 dependencies)
- T31.G6.02-03 → T33 (already duplicated in T33)

**Action Required:** Update dependency references when moving skills

### Dependencies TO T31 (T31 skills depend on other topics)
- Heavy dependencies on T21-T24 (AI topics) in G6-G8 skills
- Dependencies on T01-T10 (appropriate foundational skills)
- Dependencies on T32 (security) and T35 (ethics) in some skills

---

## Conclusion

T31 currently has **severe topic confusion** with 15+ skills that should be in T33, 8+ skills that should be in T19, and several skills that might belong in T32. After reorganization, T31 should focus on **networking concepts and architecture** (23-27 skills), while practical service usage moves to T33 and multiplayer implementation moves to T19.

**Next Steps:**
1. Confirm T19 topic existence and scope
2. Agree on T31/T33 boundary definition
3. Execute high-priority moves and fixes
4. Add missing scaffolding skills
5. Update cross-topic dependencies

**Estimated Impact:**
- T31: 37 → ~25 skills (11 moved to T33, 8 moved to T19, 4 new skills added, 3 consolidated)
- T33: Will gain 11 skills from T31
- T19: Will gain 8 skills from T31
- Dependencies: ~15-20 dependency updates needed across topics
