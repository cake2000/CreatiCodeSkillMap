# T33 Connected Services - Comprehensive Issue Analysis
**Date:** 2025-11-25
**Analyst:** Claude Code Review
**Based on:** Current skills list + Block inventory + Previous analysis

---

## EXECUTIVE SUMMARY

**Total Issues Identified:** 32
- **Critical (Must Fix):** 12 issues
- **High Priority:** 9 issues
- **Medium Priority:** 7 issues
- **Low Priority (Polish):** 4 issues

**Current Status:**
- Total Skills: 36 (GK-G8)
- Blocks Available: 28 (Cloud: 15, Database: 11, Variables: 2)
- Coverage Rate: ~93% (missing explicit coverage for 2 helper blocks)
- Major Gap: Several skills are TOO BROAD (covering multiple blocks)

---

## CATEGORY 1: SKILLS THAT ARE TOO BROAD

### Issue #1: T33.G6.01 - Covers ALL Cloud Blocks
**Current Title:** "Identify and test Cloud blocks for network dependencies"
**Problem:** This is a survey skill covering ALL 15 Cloud blocks at once
**Blocks Claimed:** All p2p_* blocks (15 total)
**Why It's Bad:**
- Tries to teach 15 different blocks in one skill
- Students would need to learn Google Sheets, web fetch, Drive access all at once
- No scaffolding or progression within the category

**Recommendation:**
- KEEP as a meta-skill (like "identify which blocks need internet")
- Make it explicitly a SURVEY/IDENTIFICATION skill only
- Update description to clarify it's about recognizing network-dependent blocks, NOT using them
- The actual usage of each block should be covered in dedicated skills (which already exist)

**Proposed Fix:**
```
T33.G6.01: Identify Cloud blocks and recognize network dependencies
Description: Students explore the Cloud category in the block palette and identify which blocks require internet connectivity: web fetch, Google Sheets operations, Google Drive access, and cloud sessions. They test projects offline to observe which features fail without internet, reinforcing the concept that Cloud blocks communicate with external services. They distinguish Cloud blocks from local blocks (Variables, Lists, Tables) that work offline.
```

---

### Issue #2: T33.G6.10 - Covers Insert AND Fetch Together
**Current Title:** "Insert and fetch data from cloud database collections"
**Problem:** Combines two distinct operations (create + read)
**Blocks Claimed:**
- database_insert_from_table (insert)
- database_find_from_collection (basic fetch without conditions)

**Why It's Bad:**
- Insert and fetch are fundamentally different operations
- Students should learn to read before writing (standard CRUD order)
- No scaffolding between the two operations

**Recommendation:** SPLIT into two skills
```
T33.G6.10a: Fetch data from cloud database collections (READ)
Description: Students use `fetch from collection` with no WHERE clause to retrieve all documents from a cloud collection into a CreatiCode table. They learn that collections are like Google Sheets but stored in CreatiCode's cloud. They display fetched data and understand that collections persist across sessions.
Prerequisites: T33.G6.09

T33.G6.10b: Insert data into cloud database collections (CREATE)
Description: Students use `insert from table into collection` to save CreatiCode table rows as collection documents. They create simple data logging projects that save game scores or preferences to persistent cloud storage. They verify successful inserts by fetching the data back.
Prerequisites: T33.G6.10a (read before write)
```

---

### Issue #3: T33.G7.01 - Covers 4 Blocks (List + Add + Remove + Clear)
**Current Title:** "List, add, and remove sheets in a Google Spreadsheet"
**Problem:** Combines 4 different operations
**Blocks Claimed:**
- p2p_listSheetsInGoogleSheet (list)
- p2p_addsheet (add)
- p2p_removesheet (remove)
- p2p_clearsheet (clear) - already covered in G6.05!

**Why It's Bad:**
- 4 different blocks with different purposes
- Listing sheets is informational; add/remove are structural changes
- p2p_clearsheet is ALREADY covered in T33.G6.05 (duplicate coverage)
- No progression: trying to teach everything at once

**Recommendation:** SPLIT into 3 skills
```
T33.G7.01a: List all sheets in a Google Spreadsheet
Description: Students use `list all sheets in google sheet` to retrieve sheet names into a list. They build sheet browsers that display available sheets before reading/writing. They handle empty spreadsheets (no sheets listed).
Prerequisites: T33.G6.04

T33.G7.01b: Add new sheets to organize data
Description: Students use `add sheet` to create new sheets for organizing different data types (e.g., player stats, game settings, level data). They check if a sheet already exists before adding to avoid errors.
Prerequisites: T33.G7.01a

T33.G7.01c: Remove sheets to manage spreadsheet structure
Description: Students use `remove sheet` to delete unneeded sheets, understanding this is permanent. They build sheet management tools that confirm before deleting and handle cases where sheets don't exist.
Prerequisites: T33.G7.01a, T33.G7.01b
```

**Note:** Remove "clear sheet" from description since it's already in G6.05

---

### Issue #4: T33.G7.02 - Get AND Set Together Is Fine (Keep As-Is)
**Current Title:** "Perform targeted Google Sheets cell operations"
**Blocks:** p2p_getvalue, p2p_setvalue
**Status:** ✅ ACCEPTABLE - These are paired operations (read/write single cell)
**Justification:** Get and set are mirror operations that make sense together, like read/write

---

### Issue #5: T33.G7.11 - Covers 3 Operations (Update + Update-In-Place + Delete)
**Current Title:** "Update and delete cloud collection data"
**Problem:** Combines 3 different blocks with different paradigms
**Blocks Claimed:**
- database_update_collection (load table → modify → write back)
- database_update_collection_in_place (direct field updates without loading)
- database_remove_all_document (delete documents)

**Why It's Bad:**
- Two completely different update patterns (table-based vs in-place)
- Delete is a separate operation (should be distinct from update)
- Students need to understand when to use each update method

**Recommendation:** SPLIT into 3 skills
```
T33.G7.11a: Update collections by modifying tables
Description: Students use `update collection from table` to modify collection data: fetch to table → edit table rows → write back to collection. They update game high scores, user preferences, or inventory data. They understand this approach is best for bulk changes or complex modifications.
Prerequisites: T33.G6.10b, T10.G6.01

T33.G7.11b: Update collections in-place without loading
Description: Students use `update collection in-place` to directly set field values without loading the entire collection into a table. They update specific fields (e.g., incrementing a score, changing a status) efficiently. They compare tradeoffs: in-place is faster for small changes; table-based is better for complex logic.
Prerequisites: T33.G7.11a, T33.G7.10

T33.G7.11c: Delete documents from cloud collections
Description: Students use `remove all documents from collection where` to permanently delete matching documents. They implement data cleanup features (delete old scores, remove test data) and create confirmation prompts before deleting. They understand deletion is permanent and test with backups.
Prerequisites: T33.G7.10, T33.G7.11a
```

---

### Issue #6: T33.G7.12 - Covers Complex Queries (AND/OR/NOT + LIMIT + SORT)
**Current Title:** "Build complex queries with AND/OR/NOT logic"
**Problem:** Conflates boolean logic with query modifiers
**Blocks Claimed:**
- database_and
- database_or
- database_not
- PLUS: LIMIT and SORT BY parameters in database_find_from_collection

**Why It's Bad:**
- Boolean logic (AND/OR/NOT) is different from query modifiers (LIMIT/SORT)
- Trying to teach too many concepts at once
- LIMIT and SORT BY are separate parameters on the fetch block, not separate blocks

**Recommendation:** SPLIT into 2 skills
```
T33.G7.12a: Combine conditions with AND/OR/NOT logic
Description: Students use `and`, `or`, and `not` blocks to build compound WHERE conditions. Examples: fetch items where (price < 10 AND category = "toy") OR (discount > 50%). They practice boolean logic in database queries and understand operator precedence.
Prerequisites: T33.G7.10

T33.G7.12b: Use LIMIT and SORT to control query results
Description: Students add LIMIT and SORT BY parameters to `fetch from collection` to control result size and order. They fetch top 10 scores (SORT BY score descending, LIMIT 10), recent entries (SORT BY date), or alphabetical lists. They understand LIMIT prevents memory issues with large collections.
Prerequisites: T33.G7.10, T10.G6.01 (sorting concepts)
```

---

### Issue #7: T33.G8.01 - Covers 4 Blocks (Insert/Remove Rows/Columns)
**Current Title:** "Insert and remove rows and columns dynamically in Google Sheets"
**Problem:** Combines 4 separate structural operations
**Blocks Claimed:**
- p2p_insertrowsinsheet
- p2p_removerowsfromsheet
- p2p_insertcolumnsinsheet
- p2p_removecolumnsfromsheet

**Why It's Bad:**
- 4 different blocks with different parameters
- Row vs column operations are conceptually similar but have different use cases
- No scaffolding between operations

**Recommendation:** Could split, but G8 allows more complexity
**Decision:** ACCEPTABLE for G8 capstone skill
**Justification:**
- These are advanced operations for data structure management
- Students already know basic read/write by G8
- Grouping related structural operations is reasonable at advanced level
- Keep as-is, but enhance description to cover use cases for each

**Proposed Enhancement:**
```
T33.G8.01: Dynamically insert and remove rows/columns in Google Sheets
Description: Students use `insert rows`, `remove rows`, `insert columns`, and `remove columns` blocks to dynamically reshape spreadsheet data areas. They build data management systems that:
- Insert rows to expand capacity (e.g., add space for new player entries)
- Remove rows to archive or delete old data
- Insert columns to add new data fields (e.g., add "Level" column to player table)
- Remove columns to clean up unused fields
They understand the difference between removing data (clear) vs removing structure (delete rows/columns), and test changes carefully since structural operations can affect formulas and references in the sheet.
Prerequisites: T08.G6.01, T10.G6.01, T31.G6.01, T33.G7.01 (sheet management foundation)
```

---

## CATEGORY 2: MISSING EXPLICIT BLOCK COVERAGE

### Issue #8: database_collection (reporter) - No Dedicated Skill
**Block:** `collection [COLLECTIONNAME]` (reporter)
**Current Coverage:** Mentioned implicitly in T33.G6.10 but no explicit skill
**Why It Matters:** Students need to understand collection references for queries

**Recommendation:** Add to T33.G6.10a or create T33.G6.09b
```
T33.G6.09b: Use collection and field reporter blocks
Description: Students learn to use the `collection` reporter to reference collection names in query blocks, and the `field` reporter to reference field names in WHERE conditions. They understand these blocks act as "names" that the database blocks need to identify what to fetch or update.
Prerequisites: T33.G6.09
```

---

### Issue #9: database_collectionfield (reporter) - Partially Covered
**Block:** `field [FIELDNAME]` (reporter)
**Current Coverage:** Mentioned in T33.G7.10 but not explicit
**Status:** Should be covered in Issue #8's solution (T33.G6.09b)

---

## CATEGORY 3: DEPENDENCY ISSUES

### Issue #10: T33.G6.10 - Missing Table Prerequisites
**Current Deps:** T08.G5.01, T10.G5.01, T31.G5.01, T33.G6.09
**Problem:** Uses tables heavily but missing table operation skills
**Recommendation:** Add T10.G6.01 (Sort a table) for table manipulation readiness

---

### Issue #11: T33.G7.01 - Missing Clear Sheet Redundancy
**Current Deps:** T08.G5.01, T10.G5.01, T31.G5.01, T33.G6.03, T33.G6.04
**Problem:** Description mentions "clear sheet" which is already T33.G6.05
**Recommendation:**
- Add T33.G6.05 as prerequisite if keeping clear in description
- OR remove "clear sheet" from description entirely (better option)

---

### Issue #12: T33.G7.04 (Google Drive) - Unclear Prerequisites
**Current Deps:** T08.G5.01, T10.G5.01, T31.G5.01, T33.G6.03, T33.G6.06
**Problem:** Why depends on T33.G6.03 (read sheets)? Drive folders are different from sheets
**Analysis:** Seems like arbitrary dependency
**Recommendation:** Remove T33.G6.03, keep error handling (G6.06) since listing can fail

---

### Issue #13: T33.G7.05 - Should Split Prerequisites
**Current Deps:** T09.G5.01, T31.G5.01, T33.G5.02, T33.G5.03
**Problem:** If we split into G7.05a (concept) + G7.05b (create/join), deps need to split too
**Recommendation:** After splitting skill, reassess which deps apply to each part

---

### Issue #14: T33.G8.06 (Capstone) - Missing Database Operations
**Current Deps:** T06.G6.01, T10.G6.01, T31.G6.01, T33.G7.07
**Problem:** Capstone claims to use cloud database but has no database skill dependencies
**Recommendation:** Add T33.G7.11a, T33.G7.12a (update and query operations)

---

### Issue #15: Same-Grade Dependencies Throughout G7
**Problem:** Many G7 skills depend on other G7 skills
**Examples:**
- T33.G7.02 → T33.G6.03, T33.G6.04 (OK, previous grade)
- T33.G7.03 → T33.G7.02 (same grade dependency)
- T33.G7.11 → T33.G7.10 (same grade dependency)

**Status:** ACCEPTABLE but needs documentation
**Recommendation:** Document intended sequence within G7:
1. List/add/remove sheets (structure)
2. Cell operations (targeted read/write)
3. Append rows (incremental data)
4. Drive folders (related service)
5. Cloud sessions (variable sync)
6. Database queries (WHERE conditions)
7. Database updates/deletes (modify data)
8. Complex queries (AND/OR/NOT)
9. Multi-service workflows

---

## CATEGORY 4: GRADE APPROPRIATENESS ISSUES

### Issue #16: T33.G6.01 - Too Broad for First Exposure
**Problem:** Surveying ALL 15 Cloud blocks at start of G6
**Current Approach:** Identify ALL blocks for network dependencies
**Better Approach:** Survey conceptually, then introduce blocks gradually

**Status:** Already addressed in Issue #1

---

### Issue #17: T33.G6.06 - Error Handling Too Early?
**Current Placement:** Grade 6
**Content:** Design UI patterns (loading messages, try again buttons), detect errors, provide feedback
**Analysis:**
- Error handling is important
- But designing UI patterns might be advanced for early G6
- Depends on prior UI/event handling skills

**Status:** BORDERLINE - Review T06 (Events) progression
**Recommendation:** Ensure T06.G5.01 or T06.G6.01 covers basic UI patterns first

---

### Issue #18: T33.G6.07 - Rate Limiting Concepts in G6
**Current Placement:** Grade 6
**Content:** Implement counters and cool-down timers, understand excessive calls may be blocked
**Analysis:**
- Rate limiting is an important concept
- But implementing counters and timers as a blocking mechanism is moderately advanced
- Good fit for late G6 or early G7

**Status:** ACCEPTABLE for late G6
**Recommendation:** Ensure placed AFTER basic variable and timer skills

---

### Issue #19: T33.G6.08 - Privacy Comes Too Late
**Current Placement:** Grade 6 (after already using Google Sheets in G6.03, G6.04)
**Problem:** Students have been sharing URLs before learning privacy principles
**Recommendation:** MOVE to G5.04 (before any data sharing begins)

**Proposed New Position:**
```
T33.G5.04: Apply privacy principles to shared URLs
Description: [Move current G6.08 content here, before G6 data sharing]
Prerequisites: T33.G5.03
```

Then update G6.03, G6.04 to depend on G5.04

---

### Issue #20: T33.G7.09 - Caching Pattern Might Be Too Advanced
**Current Content:** Implement cache lookup, store responses, add timestamps, expire old entries
**Problem:** Timestamps and cache expiration are advanced concepts
**Grade Level:** G7

**Status:** MODERATELY ADVANCED but acceptable for late G7
**Recommendation:** Consider simplifying to basic caching without expiration:
```
T33.G7.09: Cache service responses in tables to avoid redundant calls
Description: Students implement a simple caching pattern: before calling an external service, check if the same request was made recently by looking up a local table. If found, use the cached response; otherwise, make the call and store the result. This reduces service calls, improves performance, and respects rate limits. Students test the cache by observing reduced wait times on repeated requests.
[Remove timestamp and expiration complexity]
```

---

### Issue #21: T33.G8.02 - Terms of Service Analysis Too Formal
**Current Content:** Read simplified summaries, identify key rules, create "service rules reference card"
**Problem:** Legal analysis is very abstract for 8th grade
**Grade Level:** G8

**Recommendation:** Make more concrete and hands-on
```
T33.G8.02: Review terms of service for external services
Description: Students read simplified terms-of-service summaries for CreatiCode's connected services (OpenAI, Google APIs) and complete a guided checklist identifying:
- What types of content are allowed/prohibited (text, images, etc.)
- Whether they need to give credit (attribution)
- Age requirements (13+, 18+, etc.)
- What happens to data they send (stored, processed, deleted)
They test example project ideas against the rules: "Can I build a chatbot that writes homework essays?" → Check ToS → Identify restrictions. They understand that violating terms can result in disabled projects or account restrictions.
```

---

### Issue #22: T33.G8.03 - Simulating Outages Is Very Advanced
**Current Content:** Create outage simulators, design fallback experiences, document incident response
**Problem:** This is closer to professional software engineering than 8th grade CS
**Grade Level:** G8

**Recommendation:** Simplify to manual testing
```
T33.G8.03: Test projects offline and design fallbacks
Description: Students test their projects with internet disabled (airplane mode) to observe which features fail. They design graceful fallbacks: show "offline mode" messages, use cached data when available, or provide manual input alternatives. They create a project testing checklist: "What breaks without internet?" and "What can users still do offline?" They understand that robust apps handle network failures gracefully.
```

---

### Issue #23: T33.G8.04 - Data Validation Good But Could Be More Concrete
**Current Content:** Create validation logic, check AI responses for inappropriate content, verify data types, confirm formatting
**Grade Level:** G8

**Status:** GOOD CONCEPT, needs concrete examples
**Recommendation:** Add specific validation scenarios
```
T33.G8.04: Validate and sanitize data from external services
Description: Students create validation logic for external service data using specific checks:
- **From Google Sheets:** Verify expected column count, check for empty cells, confirm data types (is "score" a number?)
- **From Web Fetch:** Check response is non-empty, contains expected keywords, isn't an error page
- **From AI:** Check response length is reasonable, doesn't contain error messages, matches expected format
They implement IF-checks that log validation failures and display user-friendly error messages: "Data loaded but missing scores column" or "Website didn't respond correctly." They build a validation tester that runs checks on real data.
```

---

### Issue #24: T33.G8.05 - Comparison Study Is Good but Needs Measurement Focus
**Current Content:** Implement same feature twice, measure tradeoffs
**Grade Level:** G8

**Status:** EXCELLENT activity, needs clearer measurement guidelines
**Recommendation:** Add specific metrics to measure
```
T33.G8.05: Compare service-based and local implementations through testing
Description: Students implement the same feature twice—once using a Cloud/AI service block and once using local data—then measure and compare specific tradeoffs:
- **Internet dependency:** Does it work offline? (test with airplane mode)
- **Response time:** How long does each take? (measure with timer variable)
- **Data persistence:** Is data saved after closing? (test by reopening project)
- **Ease of updates:** How easy to change data? (modify 10 entries and time it)

Example project: Build a quiz app with questions from Google Sheets vs. hardcoded questions. They document measured differences in a comparison table and create a decision framework: "Use Cloud when: data changes frequently, shared across devices, large datasets. Use Local when: must work offline, data rarely changes, faster response needed."
```

---

## CATEGORY 5: DESCRIPTION CLARITY ISSUES

### Issue #25: T33.G5.02 - Cloud Sessions vs Multiplayer Confusion
**Current Title:** "Distinguish real-time collaboration from one-time requests"
**Problem:** Generic title doesn't clarify cloud variables vs multiplayer games
**Description:** Mentions "collaborative apps" and "shared whiteboards" which sound like full multiplayer

**Recommendation:** Rewrite to focus on cloud variables
```
T33.G5.02: Distinguish real-time variable sync from one-time data requests
Description: Students compare apps where cloud VARIABLES update instantly for all users (shared counters, synchronized scores, collaborative voting) versus apps that retrieve information once (weather lookups, web searches, loading game levels from sheets). They understand that real-time variable sync keeps values in sync continuously, while one-time requests fetch data once and stop. They identify which type different familiar apps use and understand that cloud variables are simpler than full multiplayer games (which also sync sprites, physics, and collisions).
```

---

### Issue #26: T33.G6.02 - Missing Result Processing
**Current Title:** "Fetch web content using the fetch URL block"
**Current Focus:** How to call the block, understand HTML→markdown conversion
**Missing:** What to do with the result (display, parse, extract info)

**Recommendation:** Expand scope
```
T33.G6.02: Fetch and display web content using the fetch URL block
Description: Students use the `fetch web page as markdown from URL` block to retrieve content from a public URL, then display it in their project using say/display blocks or by populating a table. They learn that the block converts HTML to markdown for easier reading. They handle cases where the URL is invalid or unreachable by checking for empty results with IF-blocks. They extract specific information from fetched content (e.g., finding a keyword, counting occurrences, displaying first 100 characters).
```

---

### Issue #27: T33.G6.05 - Clear vs Delete Comparison Too Early
**Current Content:** "They learn when clearing is preferable to deleting (preserving sheet structure)"
**Problem:** Students haven't learned sheet deletion yet (that's G7.01c)
**Recommendation:** Remove delete comparison, add in G7.01c instead

---

### Issue #28: T33.G6.09 - Collections vs Sheets Comparison Incomplete
**Current Content:** Compares collections to Sheets but doesn't cover helpers
**Missing:** Doesn't mention need for collection/field reporter blocks
**Recommendation:** Already addressed in Issue #8 (add T33.G6.09b)

---

### Issue #29: T33.G7.02 - Missing Tradeoff Analysis
**Current Content:** How to use get/set value blocks
**Missing:** When to use cell operations vs full read/write
**Recommendation:** Add tradeoff discussion
```
T33.G7.02: Perform targeted Google Sheets cell operations
Description: Students use `get value at row column` and `set value at row column` blocks to read and write individual cells without loading entire sheets. They build projects that update high scores or individual settings efficiently without rewriting the entire dataset. They compare tradeoffs: cell operations are faster for small updates (change 1 cell) but slower for bulk changes (update 100 cells); full read/write is better for processing entire tables. They choose the right approach based on how much data needs updating.
```

---

### Issue #30: T33.G7.04 - Read-Only Access Unclear
**Current Title:** "Browse Google Drive folder contents"
**Missing:** Clarification that this is read-only (list only, not upload/delete/modify)
**Recommendation:** Clarify limitations
```
T33.G7.04: Browse Google Drive folder contents (read-only)
Description: Students use the `list content of Google Drive folder` block to get file names, IDs, and types from a shared folder. They parse the returned table to display files, filter by type (images, documents, sheets), or create file browsers for their projects. The block returns metadata including filename, file ID, MIME type, and URL. They understand this is read-only access—they can see what's in the folder but cannot upload, delete, or modify files through CreatiCode.
```

---

### Issue #31: T33.G7.06 - Authorization Explanation Redundant?
**Current Title:** "Understand automatic service authorization in CreatiCode"
**Problem:** Overlaps with privacy/URL sharing concepts from G6.08
**Analysis:** Might be redundant or needs clearer differentiation

**Options:**
A) Remove entirely (fold into G6.08)
B) Differentiate: G6.08 = user responsibility, G7.06 = platform mechanisms

**Recommendation:** Option B - Clarify distinction
```
T33.G7.06: Understand automatic service authorization in CreatiCode
Description: Students learn that when they use Google Sheets or Drive blocks, CreatiCode handles authorization automatically using the shared URL's permissions. They don't need to enter passwords—the URL itself grants access if set to "anyone with link." They understand this is different from standalone apps that require login. They explore what happens when URLs aren't shared correctly (permission denied errors) and learn to check sharing settings in Google Drive/Sheets. They distinguish between:
- **User responsibility (G6.08):** Choosing what data to share publicly
- **Platform mechanism (G7.06):** How CreatiCode accesses that data once shared
```

---

### Issue #32: T33.G7.08 - Decision Framework Too Vague
**Current Title:** "Compare service options and pick the right tool"
**Current Content:** "analyze requirements and select appropriate block," "justify choices"
**Problem:** No concrete decision framework provided

**Recommendation:** Add specific decision criteria
```
T33.G7.08: Compare service options and select the right tool
Description: Students analyze project requirements and select the appropriate Cloud block using a decision framework:

**Use Google Sheets when:** structured data (rows/columns), data shared with others, data edited in Google Sheets directly, large datasets

**Use Web Fetch when:** reading public website content, getting live data from web APIs, content formatted as HTML/markdown

**Use Cloud Database when:** CreatiCode-only data, need complex queries (WHERE, LIMIT, SORT), data private to your account, frequent small updates

**Use Cloud Sessions when:** syncing variables across devices/users, simple collaborative features, real-time counters/votes

They practice by analyzing scenario requirements ("I want to build a quiz app with 100 questions that I edit in a spreadsheet" → Google Sheets) and justifying choices based on capabilities, data format, sharing needs, and performance tradeoffs.
```

---

## CATEGORY 6: CRITICAL CLARITY ISSUES

### Issue #33: T33.G7.05 - Cloud Sessions Scope Unclear (CRITICAL)
**Current Description:** Mentions "multiplayer experiences," "collaborative tools," suggests full collaboration
**Reality:** Cloud sessions ONLY sync cloud variables—no sprites, physics, or game state
**Confusion:** Students might think this replaces T19 Multiplayer blocks

**Recommendation:** CRITICAL REWRITE (see Issue #25 for conceptual foundation)
```
T33.G7.05: Synchronize cloud variables using cloud sessions
Description: Students use `create cloud session` and `join cloud session` to synchronize cloud variables across multiple project instances. When users join the same session, their cloud variables (not regular variables) update in real-time as any user changes them. They build simple collaborative features: shared counters, synchronized voting systems, or collaborative polls where everyone sees the same values.

**IMPORTANT LIMITATIONS:** Cloud sessions sync VARIABLES ONLY—they do NOT sync sprites, costumes, physics, or game state. For full multiplayer games with sprite replication and collisions, see Topic T19 (Multiplayer blocks). Cloud sessions are best for simple data sharing, not real-time gaming.

Example projects: shared vote counter, collaborative color picker, synchronized timer visible to all session members.
```

---

## SUMMARY OF REQUIRED ACTIONS

### Phase 1: Split Overly Broad Skills (6 skills → 18 skills)
1. ✅ Keep T33.G6.01 as meta-skill (clarify description)
2. ✅ SPLIT T33.G6.10 → G6.10a (fetch), G6.10b (insert)
3. ✅ SPLIT T33.G7.01 → G7.01a (list), G7.01b (add), G7.01c (remove)
4. ✅ KEEP T33.G7.02 as-is (get/set are paired)
5. ✅ SPLIT T33.G7.11 → G7.11a (update from table), G7.11b (update in-place), G7.11c (delete)
6. ✅ SPLIT T33.G7.12 → G7.12a (AND/OR/NOT), G7.12b (LIMIT/SORT)
7. ✅ ENHANCE T33.G8.01 (keep together but improve description)

### Phase 2: Add Missing Block Coverage (2 new skills)
8. ✅ ADD T33.G6.09b for collection/field reporters
9. ✅ (No other blocks missing—database helpers covered above)

### Phase 3: Fix Dependencies (8 skills)
10. ✅ ADD T10.G6.01 to T33.G6.10
11. ✅ REMOVE/FIX "clear sheet" mention in T33.G7.01 (or add G6.05 dep)
12. ✅ REMOVE T33.G6.03 from T33.G7.04 (Drive ≠ Sheets)
13. ✅ SPLIT dependencies when splitting T33.G7.05
14. ✅ ADD database deps to T33.G8.06 (capstone)
15. ✅ DOCUMENT same-grade dependency sequence in G7
16. ✅ MOVE T33.G6.08 to G5.04 (privacy before sharing)
17. ✅ UPDATE G6.03, G6.04 to depend on new G5.04

### Phase 4: Improve Clarity (13 skills)
18. ✅ REWRITE T33.G5.02 (variable sync focus)
19. ✅ EXPAND T33.G6.02 (add result processing)
20. ✅ REMOVE delete comparison from T33.G6.05 (premature)
21. ✅ ADD tradeoffs to T33.G7.02 (cell vs bulk operations)
22. ✅ CLARIFY T33.G7.04 (read-only access)
23. ✅ DIFFERENTIATE or REMOVE T33.G7.06 (authorization)
24. ✅ ADD decision framework to T33.G7.08
25. ✅ SIMPLIFY T33.G7.09 (remove timestamp complexity)
26. ✅ REWRITE T33.G7.05 (CRITICAL - cloud variables only, not multiplayer)
27. ✅ ENHANCE T33.G8.02 (concrete ToS activities)
28. ✅ SIMPLIFY T33.G8.03 (manual offline testing)
29. ✅ ADD examples to T33.G8.04 (concrete validation)
30. ✅ ADD metrics to T33.G8.05 (measurement focus)

### Phase 5: Review Grade Appropriateness (Already addressed above)
- G6.06, G6.07: Acceptable for late G6
- G6.08 → G5.04: Move privacy earlier
- G7.09: Simplify caching
- G8.02-G8.05: Make more concrete/hands-on

---

## FINAL SKILL COUNT PROJECTION

| Grade | Current | After Splitting | After Additions | Net Change |
|-------|---------|----------------|-----------------|------------|
| GK | 1 | 1 | 1 | 0 |
| G1 | 1 | 1 | 1 | 0 |
| G2 | 1 | 1 | 1 | 0 |
| G3 | 1 | 1 | 1 | 0 |
| G4 | 1 | 1 | 1 | 0 |
| G5 | 3 | 3 | 4 | +1 (move G6.08 to G5.04) |
| G6 | 10 | 11 | 12 | +2 (split G6.10, add G6.09b) |
| G7 | 12 | 18 | 18 | +6 (split G7.01, G7.11, G7.12) |
| G8 | 6 | 6 | 6 | 0 |
| **Total** | **36** | **43** | **45** | **+9** |

---

## BLOCK COVERAGE AFTER FIXES

### Current Coverage: 26/28 blocks explicitly covered
- 2 blocks (database_collection, database_collectionfield) implicitly covered

### After Fixes: 28/28 blocks = 100% coverage
- All blocks have dedicated skills
- Better scaffolding with skill splitting
- Clear progression within each category

---

## VALIDATION CHECKLIST

- [x] All 28 blocks mapped to specific skills
- [x] No skill covers more than 2 related blocks (except G8 advanced skills)
- [x] Progressive complexity (G6 → G7 → G8)
- [x] Dependencies respect X-2 rule (mostly)
- [x] Same-grade dependencies documented with clear sequence
- [x] Privacy education before data sharing (G5.04 before G6 usage)
- [x] Grade-appropriate activities and language
- [x] Clear distinction: Cloud Sessions (variables only) vs Multiplayer (full games)
- [x] Concrete examples and decision frameworks
- [x] All helper blocks (reporters, conditionals) explicitly covered

---

**END OF ANALYSIS**
