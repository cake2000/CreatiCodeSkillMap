# T25 Data Representation - Comprehensive Optimization Plan

**Date:** 2025-11-21
**Scope:** Intra-topic T25 optimization based on CreatiCode platform accuracy
**Goal:** Fix platform misalignment, skill ID issues, X-2 violations, missing features, and quality concerns

---

## Executive Summary

This plan addresses critical platform accuracy issues in T25 where skills reference features not available in CreatiCode (JSON parsing, generic "records") instead of actual platform capabilities (Tables with named columns, Cloud data storage, Google Sheets integration). Additionally, one skill has non-standard numbering (T25.G3.04.01 should be renumbered), and several skills need clarity improvements for better assessability.

**Key Findings:**
- **1 Critical JSON Issue:** T25.G7.03 explicitly mentions JSON, which CreatiCode does not support
- **0 X-2 Rule Violations:** All dependencies within T25 follow the X-2 rule
- **Missing Coverage:** Table operations (add/delete columns/rows, queries, sorting, pivot), Google Sheets integration, server/cloud storage specifics
- **1 Numbering Issue:** T25.G3.04.01 needs renumbering to T25.G3.05
- **Quality Issues:** Several skills are too broad or vague for assessment

---

## A. HIGH PRIORITY FIXES (Must Fix)

### A.1 CRITICAL PLATFORM ACCURACY - JSON Reference

**Issue:** T25.G7.03 explicitly mentions "JSON-like snippets" which is NOT supported by CreatiCode.

**Skill ID:** T25.G7.03
**Current Title:** Create JSON-like snippets to store structured state
**Current Description:** "Students express a CreatiCode project's data as nested key/value text (e.g., 'name: Player1, score: 100, items: [sword, shield]') and practice converting between this text format and program variables/lists for saving and loading game state."

**Problem:**
- CreatiCode does NOT support JSON parsing or JSON format
- The skill teaches a data format that students CANNOT actually use in CreatiCode
- CreatiCode uses: Tables (structured), Lists, Variables, Cloud Storage (key-value), Google Sheets

**Proposed Solution:** Completely rewrite this skill to focus on CreatiCode's actual data serialization:

**NEW T25.G7.03 - Serialize game state to cloud storage**
- **Title:** Store and load game state using cloud variables
- **Description:** Students design a game state schema (player name, score, inventory items) and implement save/load functionality using CreatiCode's cloud storage blocks. They convert between program variables/lists/tables and cloud key-value storage, learning to serialize structured data (e.g., converting an inventory list to a comma-separated text value for storage, then parsing it back on load).
- **Challenge format:** Coding. Students implement save/load buttons that store current game state (3-4 variables/lists) to cloud storage and restore it on project restart. Auto-grading checks that data persists across sessions.
- **CSTA:** MS-PRO-DH-04
- **Dependencies:** Keep current dependencies (T06.G3.01, T09.G3.01, T25.G6.03, T25.G5.04)

**Impact:** HIGH - This fixes a fundamental platform mismatch that would confuse students

---

### A.2 SKILL ID RENUMBERING

**Issue:** T25.G3.04.01 has non-standard numbering (should not have sub-number at Grade 3)

**Skill ID:** T25.G3.04.01
**Current Title:** Identify when data needs cleaning
**Current Description:** "Before normalizing data, students first identify examples of inconsistent data (different date formats, mixed capitalization in a list) and mark which entries need fixing. This prepares them for data cleaning in Grade 5."

**Problem:**
- The ".01" suffix implies a sub-skill structure not used elsewhere in Grade 3
- Creates confusion in the numbering system
- Should be a standalone skill at same level

**Proposed Solution:** Renumber to **T25.G3.05**

**NEW T25.G3.05 - Identify when data needs cleaning**
- Keep all content the same
- Update ID from T25.G3.04.01 → T25.G3.05
- Keep dependencies: T25.G3.03

**Impact:** MEDIUM - Critical for consistency, low risk to implement

**Implementation Notes:**
- Check if any other skills depend on T25.G3.04.01 (likely none external to T25)
- Update any cross-references in documentation

---

### A.3 MISSING CREATICODE FEATURES - TABLE OPERATIONS

**Issue:** T25 mentions "tables" generically but never teaches the actual CreatiCode table blocks for manipulation

**CreatiCode Table Capabilities (per creaticode.md):**
- Table variables (2D structured data)
- Blocks to: insert rows, delete rows, set cell values, get cell values by row/column
- Row count reporter
- Search/filter table entries (possibly)
- Tables used heavily in AI features (hand detection outputs 47-row table, body pose detection outputs table)

**Missing Skills:** None of the current T25 skills teach students HOW to:
1. Create a table programmatically
2. Add/delete columns or rows
3. Query specific cells by row/column
4. Search or filter table data
5. Sort table data
6. Use tables for AI data (hand landmarks, pose data)

**Proposed New Skills:**

#### **NEW T25.G5.06 - Create and populate a table variable**
- **Title:** Build a table to store multi-attribute records
- **Description:** Students create a table variable with named columns (e.g., "Name", "Score", "Level") and use blocks to insert rows of data. They add 5-10 records by scripting insertions, demonstrating how tables organize structured data better than parallel lists.
- **Challenge format:** Coding. Provided: data as text or lists. Students create table, add columns, insert rows. Auto-grading checks table structure (correct columns) and row count.
- **CSTA:** E5-DAA-DF-01, E5-PRO-DH-02
- **Dependencies:** T25.G5.03 (when to upgrade from list to table), T10.G3.03 (add/remove from list)
- **Grade:** 5

#### **NEW T25.G6.05 - Query and filter table data**
- **Title:** Extract specific records from a table
- **Description:** Students write scripts to query tables by condition (e.g., "find all players with score > 100") using loops and conditionals to check each row. They build a filtered result list or display matching rows, preparing for database-style queries.
- **Challenge format:** Coding. Provided: pre-populated table. Students loop through rows, check conditions, collect matches. Auto-grading validates filtered results.
- **CSTA:** MS-DAA-DP-01, MS-PRO-DH-04
- **Dependencies:** T25.G5.06 (create table), T10.G3.02 (find items with condition)
- **Grade:** 6

#### **NEW T25.G7.05 - Process AI vision data from tables**
- **Title:** Extract and use hand/pose landmark data
- **Description:** Students use hand detection or pose detection blocks (which output tables) and write scripts to access specific landmarks by row/column. For example, reading finger curl angles from the hand table to count extended fingers, or calculating distances between pose keypoints to detect a squat.
- **Challenge format:** Coding. Students enable AI detection, access table data, perform calculations. Auto-grading checks correct data extraction and basic analysis.
- **CSTA:** MS-DAA-DP-01, MS-PRO-DH-04
- **Dependencies:** T25.G6.05 (query tables), T23.G6.01 (assuming basic vision skill exists)
- **Grade:** 7

**Impact:** HIGH - Tables are a core CreatiCode feature used extensively in AI, but never explicitly taught

---

### A.4 MISSING CREATICODE FEATURES - CLOUD & GOOGLE SHEETS

**Issue:** Skills mention "cloud storage" and "Google Sheets" vaguely but never teach actual implementation

**CreatiCode Cloud Capabilities (per creaticode.md):**
- Cloud blocks for storing data online (persistent across sessions)
- Google Sheets integration via specialized blocks
- Cloud data can be public or private (key-value storage)
- Used for: saving progress, high scores, user data, multi-user data sharing

**Current Coverage:**
- T25.G7.03 mentions "store structured state" but incorrectly uses JSON
- No skills teach HOW to use cloud blocks
- No skills teach Google Sheets integration

**Proposed New Skills:**

#### **NEW T25.G6.06 - Save and load data with cloud storage**
- **Title:** Use cloud blocks for persistent data
- **Description:** Students use CreatiCode's cloud storage blocks to save game data (high score, player name, progress) that persists across sessions. They implement save/load functionality and explain the difference between local variables (lost on project stop) and cloud data (persistent).
- **Challenge format:** Coding. Students add save/load buttons, use cloud blocks for 2-3 key values. Auto-grading checks data persists by stopping and restarting project.
- **CSTA:** MS-DAA-DF-03, MS-PRO-DH-04
- **Dependencies:** T25.G5.01 (model game state), T09.G3.01 (variables)
- **Grade:** 6

#### **NEW T25.G7.06 - Integrate Google Sheets as external database**
- **Title:** Read from and write to Google Sheets
- **Description:** Students connect a CreatiCode project to a Google Sheet and use blocks to read data (e.g., quiz questions from a sheet) and write results (e.g., log survey responses). They explain benefits of external data storage (easy updates without code changes, collaboration, data analysis in spreadsheet).
- **Challenge format:** Coding + documentation. Students set up sheet access, implement read/write operations. Auto-grading checks successful data exchange.
- **CSTA:** MS-DAA-DF-03, MS-NET-IC-01
- **Dependencies:** T25.G6.06 (cloud storage basics), T31.G6.01 (assuming basic network/API skill)
- **Grade:** 7

**Impact:** HIGH - Cloud and Sheets are unique CreatiCode features enabling persistence and external data

---

## B. MEDIUM PRIORITY IMPROVEMENTS (Should Fix)

### B.1 VAGUE SKILL CLARITY - STRENGTHENING DESCRIPTIONS

**Issue:** Several skills have descriptions that are too conceptual/vague and need more concrete, assessable actions

#### **T25.G3.04 - Explain why consistent units matter**

**Current:** "Learners examine a table mixing minutes and seconds, identify the inconsistency, and convert all values to one unit. They explain why consistent units are essential for accurate comparisons and calculations in programs."

**Problem:**
- "Explain why" is hard to auto-grade
- Should focus more on the DOING (conversion) than explaining

**Proposed Revision:**
- **Description:** "Students receive a table mixing time units (some in minutes, some in seconds) and write a script to detect and convert all entries to a single unit (e.g., all to seconds). They then perform a calculation (e.g., find total time) that would fail with mixed units, demonstrating why consistency matters."
- **Challenge format:** Coding + concept. Students fix the table, perform calculation. Auto-grading checks correct conversions and result. Short answer: explain why mixed units caused wrong result initially.

**Impact:** MEDIUM - Improves assessability

---

#### **T25.G4.01 - Build schema diagrams for simple apps**

**Current:** "Students diagram an app's data needs (e.g., to-do list: task text, due date, done?) showing column names and types before coding."

**Problem:**
- Dependencies include GK skills (T25.GK.02, T25.GK.03) which are too far back (violates X-2 in spirit)
- Should depend on more recent Grade 3 skills about variable types

**Proposed Revision:**
- **Dependencies:** Change from (T02.G3.01, T25.GK.02, T25.GK.03) to:
  - T02.G3.01 (keep)
  - T25.G3.02 (choose right variable type)
  - T25.G2.04 (combine two data attributes)
- This makes more logical sense - schema design builds on knowing variable types and combining attributes

**Impact:** MEDIUM - Improves dependency logic

---

#### **T25.G5.01 - Model multi-type game state**

**Current Description:** "Students design a 'player' data structure using text (name), number (score, health), Boolean (isAlive), and list (inventory) fields, then implement it using CreatiCode variables, lists, and tables."

**Problem:**
- Mentions "tables" but students haven't learned to create/use tables yet
- Should either: (a) remove table reference, or (b) add table prerequisite

**Proposed Revision (Option A - Remove Tables):**
- **Description:** "Students design a 'player' data structure using text (name), number (score, health), Boolean (isAlive), and list (inventory) fields, then implement it using CreatiCode variables and lists. They explain which data type fits each field and initialize all values."

**Proposed Revision (Option B - Add Table Prerequisite - BETTER):**
- Keep description, but add dependency on NEW T25.G5.06 (create table)
- This allows students to implement player as a table row with multiple columns

**Recommended:** Option A for now (simpler), then teach table-based implementation in G6

**Impact:** MEDIUM - Clarifies platform alignment

---

### B.2 SCAFFOLDING IMPROVEMENTS - BREAKING DOWN COMPLEX SKILLS

#### **T25.G5.03 - Decide when to upgrade from list to table**

**Current:** Concept-only skill about choosing between lists and tables

**Enhancement:** Add a follow-up coding skill

**NEW T25.G5.03b - Refactor parallel lists into a table** (insert after G5.03, before G5.04)
- **Title:** Convert parallel lists to a structured table
- **Description:** Students receive code using 2-3 parallel lists (names, scores, levels) and refactor it to use a single table with named columns. They update access code to read from table rows/columns instead of list indices, maintaining identical program behavior.
- **Challenge format:** Coding. Provided: working code with parallel lists. Students convert to table and verify output matches. Auto-grading compares behavior.
- **CSTA:** E5-PRO-DH-02, E5-PRO-PF-02
- **Dependencies:** T25.G5.03 (decide when to upgrade), NEW T25.G5.06 (create table)
- **Grade:** 5

**Impact:** MEDIUM - Provides hands-on practice of conceptual skill

---

#### **T25.G6.03 - Nest structures (list of records, record of lists)**

**Current:** Very broad skill covering multiple nested patterns

**Problem:**
- "List of records" and "record of lists" are distinct patterns that should be taught separately
- Too much cognitive load in one skill

**Proposed Split:**

**REVISED T25.G6.03a - Store lists within table records**
- **Description:** Students design a table where one column contains lists (e.g., a "Players" table with a "Inventory" column holding a list per player). They implement adding items to a specific player's inventory by accessing the table cell, modifying the list, and updating the cell.
- **Challenge format:** Coding. Students work with pre-structured nested data, perform specific operations. Auto-grading checks nested data integrity.
- **CSTA:** MS-PRO-DH-04
- **Dependencies:** T25.G5.01, NEW T25.G5.06 (create table)
- **Grade:** 6

**NEW T25.G6.03b - Manage lists of structured records** (new skill)
- **Description:** Students maintain a list where each item is a structured record (e.g., list of NPCs, each with name/health/position). They implement adding, removing, and searching through records, explaining when this pattern is useful vs a table.
- **Challenge format:** Coding + concept. Students implement record list operations. Short answer on pattern tradeoffs.
- **CSTA:** MS-PRO-DH-04
- **Dependencies:** T25.G6.03a, T25.G5.01
- **Grade:** 6

**Impact:** MEDIUM - Reduces cognitive load, improves learning progression

---

### B.3 GRADE-APPROPRIATENESS CONCERNS

#### **T25.G8.01 - Design schemas for multi-modal apps**

**Current:** "Students outline data structures that hold transcripts, detected poses, and AI prompts for multi-modal CreatiCode projects (linking to T23/T24). They document relationships and storage formats."

**Concern:**
- Very abstract and complex for Grade 8
- Depends heavily on T23/T24 AI skills
- Needs more concrete scaffolding

**Proposed Enhancement:**
Add more specific guidance in description:

**Revised Description:** "Students design data schemas for a multi-modal project (e.g., voice-controlled game with pose detection). They create tables/lists to store: (1) voice command history (timestamp, text, response), (2) pose landmarks (body joints table from detection), (3) AI prompt templates (slots for runtime values). They document field names, types, and relationships (e.g., 'command ID' links voice table to response log)."

**Challenge format:** Enhanced - provide a specific project scenario, require documented schema with all fields, types, and relationships clearly labeled. Peer review component.

**Impact:** LOW-MEDIUM - Makes capstone skill more concrete

---

## C. LOW PRIORITY ENHANCEMENTS (Nice to Have)

### C.1 ADDITIONAL FEATURE COVERAGE

#### **NEW T25.G7.07 - Use regex for data validation**

**Context:** CreatiCode likely supports regex in text blocks (common in Scratch extensions)

- **Title:** Validate data formats with pattern matching
- **Description:** Students use regular expressions to validate user inputs (e.g., email format, phone number format) before storing. They implement input validation that rejects invalid formats and explains the pattern rules.
- **Challenge format:** Coding. Students add validation to a form project. Auto-grading tests with valid/invalid inputs.
- **CSTA:** MS-PRO-DH-04, MS-DAA-DF-03
- **Dependencies:** T25.G5.02 (normalize inputs), T10.G6.01 (text processing)
- **Grade:** 7

**Impact:** LOW - Useful but not critical, depends on CreatiCode regex support

---

#### **NEW T25.G8.05 - Implement data aggregation and statistics**

- **Title:** Calculate statistics across table/list data
- **Description:** Students write functions to aggregate data (sum, average, count, min/max) across table columns or list items. They implement a leaderboard with sorting and a dashboard showing statistics (e.g., "average score: 75, highest: 95").
- **Challenge format:** Coding. Students implement stat functions and display. Auto-grading checks calculations.
- **CSTA:** MS-DAA-DI-02, MS-PRO-DH-04
- **Dependencies:** NEW T25.G6.05 (query tables), T11.G7.01 (functions)
- **Grade:** 8

**Impact:** LOW - Nice statistical practice but covered somewhat in T27 (Analysis)

---

### C.2 DESCRIPTION ENHANCEMENTS FOR CLARITY

Minor wording improvements for better clarity (no structural changes):

1. **T25.G2.04 - Combine two data attributes**
   - Current: "...to see how pairing attributes forms richer records"
   - Enhanced: "...to see how pairing attributes creates structured records (like a mini-database row)"

2. **T25.G4.05 - Distinguish between raw data and computed values**
   - Add example to description: "For instance, storing round scores (raw) vs total (computed) allows recalculation if scoring rules change."

3. **T25.G5.04 - Encode categorical values with symbols or enums**
   - Clarify CreatiCode context: "...explain how a legend/lookup table keeps codes readable (since CreatiCode doesn't have native enum types)"

**Impact:** LOW - Cosmetic improvements

---

## D. SUMMARY OF CHANGES

### New Skills to Add (7 skills):
1. **T25.G5.06** - Create and populate a table variable (Grade 5)
2. **T25.G6.05** - Query and filter table data (Grade 6)
3. **T25.G6.06** - Save and load data with cloud storage (Grade 6)
4. **T25.G7.05** - Process AI vision data from tables (Grade 7)
5. **T25.G7.06** - Integrate Google Sheets as external database (Grade 7)
6. **T25.G7.07** - Use regex for data validation (Grade 7) [OPTIONAL]
7. **T25.G8.05** - Implement data aggregation and statistics (Grade 8) [OPTIONAL]

### Skills to Rewrite (1 skill):
1. **T25.G7.03** - Completely rewrite from JSON to cloud storage serialization

### Skills to Renumber (1 skill):
1. **T25.G3.04.01** → **T25.G3.05** - Identify when data needs cleaning

### Skills to Revise (5 skills):
1. **T25.G3.04** - Strengthen description (more coding, less explaining)
2. **T25.G4.01** - Fix dependencies (remove GK, add G3 variable type skill)
3. **T25.G5.01** - Remove table reference or add table prerequisite
4. **T25.G6.03** - Split into two skills (G6.03a and G6.03b)
5. **T25.G8.01** - Add more specific guidance to description

### Total Impact:
- **3 Critical Fixes** (JSON, numbering, dependencies)
- **7 High-Priority Additions** (tables, cloud, sheets)
- **5 Quality Improvements** (clarity, scaffolding, appropriateness)

---

## E. IMPLEMENTATION PRIORITY

### Phase 1 (Immediate - Week 1):
1. Fix T25.G7.03 (JSON → Cloud storage)
2. Renumber T25.G3.04.01 → T25.G3.05
3. Revise T25.G4.01 dependencies

### Phase 2 (High Priority - Week 2):
1. Add T25.G5.06 (Create tables)
2. Add T25.G6.05 (Query tables)
3. Add T25.G6.06 (Cloud storage)
4. Revise T25.G5.01 (remove table reference)

### Phase 3 (Medium Priority - Week 3):
1. Add T25.G7.05 (AI vision tables)
2. Add T25.G7.06 (Google Sheets)
3. Revise T25.G3.04 (strengthen description)
4. Split T25.G6.03 (nested structures)

### Phase 4 (Polish - Week 4):
1. Add T25.G8.05 (statistics) if desired
2. Minor description enhancements (C.2)
3. Comprehensive validation pass

---

## F. VALIDATION CHECKLIST

After implementing changes, verify:

- [ ] No skills reference JSON or unsupported formats
- [ ] All skill IDs follow standard numbering (no .01 at G3)
- [ ] All intra-T25 dependencies respect X-2 rule
- [ ] Table operations are explicitly taught before advanced use
- [ ] Cloud storage and Google Sheets have concrete implementations
- [ ] All descriptions are concrete and assessable
- [ ] Grade-level appropriateness is maintained
- [ ] No broken cross-references to other topics
- [ ] CSTA codes are accurate for new/revised skills

---

## G. NOTES ON CROSS-TOPIC PRESERVATION

**Important:** This plan ONLY addresses intra-T25 issues. Do NOT modify:

1. Dependencies FROM other topics TO T25 (e.g., T26 depending on T25.G3.01)
2. Dependencies FROM T25 TO other topics (e.g., T25.G3.01 depending on T08.G3.01)
3. Skills in other topics that reference T25 concepts

**After T25 changes**, run global validation to update:
- T26 skills that depend on renumbered T25.G3.05
- T27 skills that might benefit from new table query skills
- T10 (Lists & Tables) - ensure T25 table skills don't duplicate T10 content
- T23/T24 (AI) - ensure AI vision skills align with new T25.G7.05

---

## H. ESTIMATED EFFORT

| Task | Effort (hours) |
|------|----------------|
| Rewrite T25.G7.03 (JSON fix) | 2 |
| Renumber T25.G3.04.01 → G3.05 | 1 |
| Create 5 new table/cloud skills | 10 |
| Revise 5 existing skills | 5 |
| Update dependencies | 3 |
| Validation & testing | 4 |
| Documentation | 2 |
| **TOTAL** | **27 hours** |

---

## I. RISK ASSESSMENT

| Risk | Severity | Mitigation |
|------|----------|------------|
| Breaking existing curricula | HIGH | Test with sample projects before deployment |
| Confusion from renumbering | MEDIUM | Provide migration guide, update all references |
| Over-complicating Grade 5 | MEDIUM | Strong scaffolding in new table skills |
| Missing CreatiCode features | LOW | Verify all blocks exist before finalizing skills |
| Scope creep | LOW | Stick to defined phases, defer optional enhancements |

---

## J. SUCCESS METRICS

After implementation, T25 should achieve:

1. **Platform Accuracy:** 100% of skills reference actual CreatiCode features
2. **Completeness:** Core data features (tables, cloud, sheets) have explicit skill coverage
3. **Clarity:** 90%+ of skills have concrete, assessable descriptions
4. **Consistency:** All skill IDs follow standard numbering conventions
5. **Progression:** No X-2 violations within T25
6. **Grade-Appropriate:** All skills match developmental expectations

---

**END OF OPTIMIZATION PLAN**

*For questions or clarifications, refer to:*
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/creaticode.md` (platform capabilities)
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/skills_T25_data_representation.md` (current skill definitions)
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (full integrated skills)
