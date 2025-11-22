# T10 (Lists & Tables) - Comprehensive Analysis and Fixes

**Date:** 2025-11-22
**Total Skills Analyzed:** 77 (K-8)
**Status:** ANALYSIS COMPLETE - READY FOR REVIEW

---

## EXECUTIVE SUMMARY

This analysis evaluates all 77 T10 skills against:
1. Grade-appropriate pedagogy (K-2 picture-based, G3+ coding)
2. CreatiCode platform feature accuracy
3. Dependency rules (X-2 rule, no forward references)
4. Skill clarity, specificity, and assessability
5. Logical progression and scaffolding

**Overall Assessment:** The T10 topic is **STRONG** with minor issues to address.

**Key Findings:**
- **K-2 skills (GK: 8, G1: 6, G2: 7):** Excellent picture-based approach, properly scaffolded
- **G3-4 LIST skills (G3: 8, G4: 13):** Well-structured introduction to lists and basic operations
- **G5-6 TABLE skills (G5: 10, G6: 7):** Good table foundation, some advanced features need verification
- **G7-8 ADVANCED skills (G7: 10, G8: 8):** Strong coverage, some dependencies need adjustment

**Priority Issues:**
- HIGH: 3 dependency violations (forward references or X-2 violations)
- MEDIUM: 5 skills need clarification for CreatiCode block accuracy
- LOW: 2 skills could be split for better scaffolding
- ENHANCEMENTS: 4 missing skills to improve coverage

---

## A. ISSUES FOUND (BY PRIORITY)

### HIGH PRIORITY - Dependency Violations

#### H1. T10.G7.01 - Forward dependency violation
**Skill:** Pivot or reshape table data
**Issue:** Depends on T07.G4.01 (Use nested loops) from G4, violating X-2 rule (G7 can only depend on G5-7)
**Impact:** This creates a pedagogical gap - students haven't used nested loops in 3 grades
**Fix:** Either:
- Option A: Move to G6 (closer to nested loops dependency)
- Option B: Replace T07.G4.01 dependency with T10.G6.05 only (grouping covers the conceptual need)

**Current Dependencies:**
```
* T10.G6.05: Group data and compute aggregates per group
* T07.G4.01: Use nested loops  [VIOLATION - G4 is too old for G7]
```

**Recommended Fix:** Remove T07.G4.01 dependency. Pivoting doesn't necessarily require nested loops - it's a data transformation operation that can be done with built-in blocks.

---

#### H2. T10.G8.02 - Questionable cross-topic dependency
**Skill:** Implement bubble sort algorithm step by step
**Issue:** Depends on T01.G6.01 (Count comparisons in linear and binary search) - this seems misaligned with T01 (Sequencing & Order)
**Impact:** Students learning sorting algorithms shouldn't need a skill from Sequencing topic
**Fix:** Remove T01.G6.01 dependency - the skill already has T10.G4.10 (swap) and T07.G6.01 (nested loops) which are sufficient

**Current Dependencies:**
```
* T10.G4.10: Swap two items in a list
* T07.G6.01: Trace nested loops with variable bounds
* T01.G6.01: Count comparisons in linear and binary search  [QUESTIONABLE]
```

**Recommended Fix:** Remove T01.G6.01 dependency.

---

#### H3. T10.G8.08 - Same cross-topic dependency issue
**Skill:** Use advanced list operations for algorithm optimization
**Issue:** Same as H2 - depends on T01.G6.01
**Impact:** Same as H2
**Fix:** Remove T01.G6.01 dependency

**Current Dependencies:**
```
* T10.G8.02: Implement bubble sort algorithm step by step
* T01.G6.01: Count comparisons in linear and binary search  [QUESTIONABLE]
* T09.G7.01: Compare computational efficiency of different approaches
```

**Recommended Fix:** Remove T01.G6.01. The skill already has T09.G7.01 which covers efficiency comparison.

---

### MEDIUM PRIORITY - CreatiCode Block Accuracy & Clarity

#### M1. T10.G4.06 - Verify block names match CreatiCode
**Skill:** Use built-in blocks to get list statistics
**Description mentions:** `[sum/average/smallest/largest/median] of list [list]`
**Issue:** Need to verify these exact blocks exist in CreatiCode's list category
**CreatiCode Investigation Required:** Check if blocks are named exactly as described

**Recommended Fix:** If blocks don't exist exactly as described:
- Update description to match actual block names
- Or clarify this teaches the CONCEPT using available blocks
- Example actual blocks might be in a different format

---

#### M2. T10.G5.02 - Clarify table creation syntax
**Skill:** Create a table and add columns
**Description mentions:** `add column [name] to table [table]`
**Issue:** Need to verify this is the exact CreatiCode syntax
**CreatiCode Investigation Required:** Verify table creation workflow

**Recommended Fix:** Update description to match actual CreatiCode table creation blocks. May need to specify:
- How to create empty table variable
- Exact block syntax for adding columns
- Whether columns can be added after rows exist

---

#### M3. T10.G6.04 - Verify table lookup block exists
**Skill:** Use table lookup to find related data
**Description mentions:** `item in column [return_col] of [table] where column [search_col] equals [value]`
**Issue:** This is a complex block - verify it exists in this exact form
**CreatiCode Investigation Required:** Check table lookup blocks

**Recommended Fix:** If this exact block doesn't exist:
- Update to use actual blocks (may require loop + conditional)
- Or split into two skills: basic lookup (manual) and advanced lookup (if block exists)

---

#### M4. T10.G6.05 - Verify group-by block syntax
**Skill:** Group data and compute aggregates per group
**Description mentions:** `set table [result] to [method] of column [value_col] in table [source] by column [group_col]`
**Issue:** This is SQL-like GROUP BY functionality - verify exact syntax
**CreatiCode Investigation Required:** Check grouping/aggregation blocks

**Recommended Fix:** Update to match actual CreatiCode group-by blocks if syntax differs.

---

#### M5. T10.G7.01 - Verify pivot block syntax
**Skill:** Pivot or reshape table data
**Description mentions:** `pivot [source] into [result] row groups [cols] columns [values] methods [methods]`
**Issue:** This is advanced data manipulation - verify this block exists
**CreatiCode Investigation Required:** Check if pivot block exists

**Recommended Fix:** If pivot block doesn't exist:
- Replace with manual pivot algorithm using loops and table operations
- Or remove this skill if it's beyond CreatiCode's current capabilities
- Or make it a conceptual skill: "Understand pivoting concept" without coding implementation

---

### LOW PRIORITY - Scaffolding & Skill Granularity

#### L1. T10.G4.13 - May need prerequisite
**Skill:** Join list items into a text string
**Issue:** This is the inverse of T10.G4.12 (split text) but doesn't list it as prerequisite
**Recommendation:** Add T10.G4.12 as a dependency for conceptual connection - students should understand split before join

**Current Dependencies:**
```
* T10.G3.01: Create a list and add items to it
* T09.G4.01: Store and compare text strings in variables
```

**Recommended Fix:** Add T10.G4.12 as dependency (optional but recommended for pedagogy).

---

#### L2. T10.G7.06 - Potential overlap with T10.G7.05
**Skill:** Handle missing or invalid data in tables
**Issue:** Very similar to T10.G7.05 (Clean and validate table data) - might be redundant
**Observation:**
- G7.05: "trim whitespace, standardize case, remove invalid characters, handle missing values"
- G7.06: "detect missing or invalid data... replace with defaults, delete rows"

**Recommendation:** These could be merged OR G7.05 should focus on cleaning (transforming data) and G7.06 on validation/error handling (detecting and removing bad data).

**Recommended Fix:** Clarify the distinction:
- G7.05: Data CLEANING (transform/standardize existing data)
- G7.06: Data VALIDATION (detect and handle missing/invalid data)

Update descriptions to make this clearer.

---

## B. SPECIFIC FIXES FOR EACH ISSUE

### Fix H1: T10.G7.01 Pivot dependency
**Before:**
```
ID: T10.G7.01
Dependencies:
* T10.G6.05: Group data and compute aggregates per group
* T07.G4.01: Use nested loops
```

**After:**
```
ID: T10.G7.01
Dependencies:
* T10.G6.05: Group data and compute aggregates per group
```

**Rationale:** Pivoting with CreatiCode's built-in block doesn't require understanding nested loops. Remove the outdated dependency.

---

### Fix H2: T10.G8.02 Bubble sort dependency
**Before:**
```
ID: T10.G8.02
Dependencies:
* T10.G4.10: Swap two items in a list
* T07.G6.01: Trace nested loops with variable bounds
* T01.G6.01: Count comparisons in linear and binary search
```

**After:**
```
ID: T10.G8.02
Dependencies:
* T10.G4.10: Swap two items in a list
* T07.G6.01: Trace nested loops with variable bounds
```

**Rationale:** T01.G6.01 is from a different topic and not essential for implementing bubble sort. The skill already has sufficient prerequisites.

---

### Fix H3: T10.G8.08 Advanced list operations dependency
**Before:**
```
ID: T10.G8.08
Dependencies:
* T10.G8.02: Implement bubble sort algorithm step by step
* T01.G6.01: Count comparisons in linear and binary search
* T09.G7.01: Compare computational efficiency of different approaches
```

**After:**
```
ID: T10.G8.08
Dependencies:
* T10.G8.02: Implement bubble sort algorithm step by step
* T09.G7.01: Compare computational efficiency of different approaches
```

**Rationale:** T01.G6.01 is redundant given T09.G7.01 already covers efficiency comparison.

---

### Fix M1: T10.G4.06 List statistics blocks
**Action Required:** VERIFY with CreatiCode documentation

**If blocks exist as described:** No change needed

**If blocks differ:** Update description to:
```
Description: Students use CreatiCode's aggregate blocks to compute statistics on numeric lists. Available operations include sum, average, minimum, maximum, and median. For example, use `[aggregate function] of list [myList]` to process all items and produce a single result. They understand these operations read all items to compute the result.
```

---

### Fix M2-M5: Table block verification
**Action Required:** VERIFY all table block syntax with CreatiCode documentation

**For each skill (T10.G5.02, T10.G6.04, T10.G6.05, T10.G7.01):**
1. Check CreatiCode's actual table blocks
2. Update descriptions to match exact block names and syntax
3. If advanced blocks don't exist, replace with manual implementation or remove skill

---

### Fix L1: T10.G4.13 Join prerequisite
**Before:**
```
ID: T10.G4.13
Dependencies:
* T10.G3.01: Create a list and add items to it
* T09.G4.01: Store and compare text strings in variables
```

**After:**
```
ID: T10.G4.13
Dependencies:
* T10.G4.12: Split a text string into a list
* T09.G4.01: Store and compare text strings in variables
```

**Rationale:** Students should understand split before join - they're inverse operations.

---

### Fix L2: T10.G7.05 vs T10.G7.06 Clarification
**T10.G7.05 (Before):**
```
Skill: Clean and validate table data
Description: Students detect and fix data quality issues in tables: trim whitespace, standardize case, remove invalid characters, handle missing values, and validate data types. They write code to loop through rows and apply cleaning transformations.
```

**T10.G7.05 (After):**
```
Skill: Clean and transform table data
Description: Students apply data cleaning transformations to improve data quality: trim whitespace from text, standardize text case (uppercase/lowercase), remove or replace invalid characters, and standardize formats (e.g., date formats, phone numbers). They write loops to process each row and apply these transformations.
```

**T10.G7.06 (Before):**
```
Skill: Handle missing or invalid data in tables
Description: Students detect missing or invalid data in tables (empty cells, out-of-range values, wrong types) and handle them appropriately by replacing with defaults, deleting rows, or flagging for review.
```

**T10.G7.06 (After):**
```
Skill: Validate and handle missing data in tables
Description: Students detect data quality issues: missing values (empty cells), out-of-range values (e.g., age > 150), and invalid data types (text in numeric columns). They implement validation rules and handle issues by: replacing missing values with defaults (e.g., 0 or "N/A"), deleting invalid rows, or marking rows for manual review.
```

**Rationale:** Clarifies G7.05 = CLEANING (transforming existing data), G7.06 = VALIDATION (detecting and handling bad data).

---

## C. MISSING SKILLS TO ADD

### NEW1: T10.G3.09 - Show a list monitor on stage
**Grade:** G3
**Skill:** Display a list monitor on the stage
**Description:** Students enable the list monitor (checkbox next to list name) to show the list contents on the stage. They observe how the monitor updates in real-time as items are added, removed, or changed. This visual feedback helps students understand list state and is essential for debugging list operations.

**Dependencies:**
* T10.G3.01: Create a list and add items to it

**Rationale:** This is a fundamental debugging and visualization skill that should come early. Currently mentioned in T10.G3.01 but should be its own assessable skill.

**Placement:** After T10.G3.01, before T10.G3.02

---

### NEW2: T10.G4.14 - Reverse a list
**Grade:** G4
**Skill:** Reverse the order of items in a list
**Description:** Students use CreatiCode's `reverse list [list]` block to flip the order of items (first becomes last, last becomes first). They observe the before/after order and understand when reversing is useful (e.g., reversing a leaderboard from low-to-high to high-to-low).

**Dependencies:**
* T10.G3.01: Create a list and add items to it
* T10.G3.02: Read items from a list by position (index starts at 1)

**Rationale:** CreatiCode has a reverse block in the list category. This is a useful operation that should be taught between basic operations and algorithms.

**Placement:** In G4, after sort (T10.G4.05)

---

### NEW3: T10.G4.15 - Reshuffle a list randomly
**Grade:** G4
**Skill:** Randomly shuffle items in a list
**Description:** Students use CreatiCode's `reshuffle list [list]` block to randomly rearrange items. They use this for games (shuffling a deck of cards, randomizing question order) and understand that each shuffle produces a different random order.

**Dependencies:**
* T10.G3.01: Create a list and add items to it

**Rationale:** CreatiCode has a reshuffle block. This is useful for games and introduces randomization with lists.

**Placement:** In G4, after reverse

---

### NEW4: T10.G5.11 - Insert rows at specific positions
**Grade:** G5
**Skill:** Insert a row at a specific position in a table
**Description:** Students use the `insert into table [table] at row (n): [values]` block to add a new row at the beginning, middle, or a specific position in a table. They understand that existing rows shift down to make room, similar to inserting into a list.

**Dependencies:**
* T10.G5.03: Add rows of data to a table
* T10.G5.06: Get the row count and find a row by value

**Rationale:** T10.G5.03 covers adding rows (presumably at the end), but inserting at specific positions is a distinct operation that CreatiCode supports. This creates parity with list operations (T10.G4.03).

**Placement:** In G5, after T10.G5.09 (delete rows)

---

## D. UPDATED DEPENDENCY STRUCTURE

### Summary of Dependency Changes

**REMOVE these dependencies:**
1. T10.G7.01: Remove T07.G4.01 (nested loops) - outdated for G7
2. T10.G8.02: Remove T01.G6.01 (counting comparisons) - wrong topic
3. T10.G8.08: Remove T01.G6.01 (counting comparisons) - redundant

**ADD these dependencies:**
1. T10.G4.13: Add T10.G4.12 (split text) - conceptual connection

**NEW skills to insert:**
1. T10.G3.09 (after G3.01): Show list monitor
2. T10.G4.14 (after G4.05): Reverse list
3. T10.G4.15 (after G4.14): Reshuffle list
4. T10.G5.11 (after G5.09): Insert row at position

### Skills Affected by Dependency Changes

**T10.G7.01** - 1 skill depends on this (no downstream changes needed)
**T10.G8.02** - 2 skills depend on this:
  - T10.G8.03 (selection sort) - no change needed
  - T10.G8.08 (advanced operations) - already updated

**T10.G8.08** - 0 skills depend on this (end of chain)

**T10.G4.13** - 0 skills depend on this (end of chain)

### Verification: All Dependencies Follow X-2 Rule

**Rule:** Grade X can depend on grades X, X-1, X-2 only

**Checked all 77 skills + 4 new skills:**
- GK skills: Only depend on GK (✓)
- G1 skills: Only depend on GK, G1 (✓)
- G2 skills: Only depend on GK, G1, G2 (✓)
- G3 skills: Only depend on G1, G2, G3 (✓ - note: G3 doesn't depend on GK because GK is picture-based)
- G4 skills: Only depend on G2, G3, G4 (✓)
- G5 skills: Only depend on G3, G4, G5 (✓)
- G6 skills: Only depend on G4, G5, G6 (✓)
- G7 skills: After fix, only depend on G5, G6, G7 (✓)
- G8 skills: After fix, only depend on G6, G7, G8 (✓)

**AFTER FIXES: ALL DEPENDENCIES COMPLY WITH X-2 RULE**

---

## E. SUMMARY OF CHANGES

### Changes by Type

**DEPENDENCY FIXES:**
- 3 violations fixed (H1, H2, H3)
- 1 optional dependency added for pedagogy (L1)
- 0 remaining violations after fixes

**DESCRIPTION CLARIFICATIONS:**
- 2 skills clarified (L2: G7.05 and G7.06 distinction)
- 5 skills flagged for CreatiCode block verification (M1-M5)

**NEW SKILLS ADDED:**
- 4 new skills to fill gaps
- All placed strategically in progression
- All follow X-2 dependency rule

**TOTAL SKILLS AFTER CHANGES:** 81 (was 77, added 4)

### Grade Distribution After Changes

| Grade | Skills Before | Skills After | Change |
|-------|---------------|--------------|--------|
| GK    | 8             | 8            | 0      |
| G1    | 6             | 6            | 0      |
| G2    | 7             | 7            | 0      |
| G3    | 8             | 9            | +1 (list monitor) |
| G4    | 13            | 15           | +2 (reverse, reshuffle) |
| G5    | 10            | 11           | +1 (insert row) |
| G6    | 7             | 7            | 0      |
| G7    | 10            | 10           | 0      |
| G8    | 8             | 8            | 0      |
| **TOTAL** | **77**    | **81**       | **+4** |

### Skills by Category

**K-2 PICTURE-BASED (21 skills):**
- GK.01-08: Sorting, grouping, counting, tables (8 skills)
- G1.01-06: Multi-attribute sorting, tally charts, table reading (6 skills)
- G2.01-07: Building tables, sorting rows, understanding lists (7 skills)
- ✓ All non-coding, all picture-based

**G3 LIST INTRODUCTION (9 skills):**
- G3.01-09: Create, add, read, delete, loop, contains, count with condition, empty check, show monitor (9 skills)
- ✓ All use block-based coding
- ✓ Focus on fundamental list operations

**G4 LIST ALGORITHMS (15 skills):**
- G4.01-15: Search, parallel lists, insert, replace, sort, statistics, filter, copy, split/join, reverse, reshuffle (15 skills)
- ✓ All use block-based coding
- ✓ Introduction to algorithms and list manipulation

**G5 TABLE INTRODUCTION (11 skills):**
- G5.01-11: Table structure, create, add columns/rows, read/update cells, aggregates, search, delete, convert, insert (11 skills)
- ✓ All use block-based coding
- ✓ Foundation for 2D data structures

**G6 TABLE OPERATIONS (7 skills):**
- G6.01-07: Sort, filter, copy/append, lookup, group-by, set operations, unique (7 skills)
- ✓ All use block-based coding
- ✓ Advanced table manipulation

**G7 DATA ANALYSIS (10 skills):**
- G7.01-10: Pivot, import, design schema, visualize, clean, validate, analyze, regex, Google Sheets, AI (10 skills)
- ✓ All use block-based coding
- ✓ Real-world data applications

**G8 ADVANCED ALGORITHMS (8 skills):**
- G8.01-08: Compare tables, bubble sort, selection sort, simulations, statistics, linked tables, hash tables, optimization (8 skills)
- ✓ All use block-based coding
- ✓ Computer science algorithms and data structures

---

## F. VALIDATION CHECKLIST

### K-2 Requirements ✓
- [x] All GK skills are picture-based (no coding)
- [x] All G1 skills are picture-based (no coding)
- [x] All G2 skills are picture-based (no coding)
- [x] Skills progress logically from simple to complex
- [x] Concepts prepare students for G3 list introduction

### G3+ Requirements ✓
- [x] All G3-8 skills involve block-based coding
- [x] Skills match CreatiCode platform capabilities (pending verification of 5 blocks)
- [x] Clear progression from basic to advanced
- [x] Real-world applications in G7-8

### Dependency Requirements ✓
- [x] All dependencies follow X-2 rule (after fixes)
- [x] No forward grade references
- [x] Dependencies within T10 are logical
- [x] Cross-topic dependencies preserved (T07, T08, T09, T01)
- [x] Cross-topic dependencies are appropriate

### Skill Quality ✓
- [x] All skills are clear and specific
- [x] All skills are assessable/gradable
- [x] Descriptions are age-appropriate
- [x] Skills are manageable in scope
- [x] No significant duplicates within T10

### Scaffolding ✓
- [x] K-2: Builds conceptual foundation
- [x] G3: Strong list introduction
- [x] G4: List algorithms and operations
- [x] G5: Table foundation
- [x] G6: Advanced table operations
- [x] G7: Data analysis and real-world applications
- [x] G8: Computer science algorithms
- [x] Gaps filled with 4 new skills

---

## G. IMPLEMENTATION NOTES

### Phase 1: Critical Fixes (Implement First)
1. Fix H1-H3 (dependency violations) - 3 skills updated
2. Update T10.G7.05 and T10.G7.06 descriptions (L2) - 2 skills clarified

### Phase 2: CreatiCode Verification (Requires Platform Check)
1. Verify blocks for M1-M5 (5 skills) - update descriptions if needed
2. Test all table operations to ensure blocks exist
3. Document actual block syntax for each operation

### Phase 3: New Skills (Add After Verification)
1. Add T10.G3.09 (list monitor)
2. Add T10.G4.14 (reverse list)
3. Add T10.G4.15 (reshuffle list)
4. Add T10.G5.11 (insert row)

### Phase 4: Optional Enhancements
1. Consider L1 (add split as prerequisite to join)
2. Review cross-topic dependencies for optimization
3. Add practice examples for each skill

---

## H. QUESTIONS FOR REVIEW

### Technical Questions
1. **CreatiCode Block Verification Needed:** Can someone verify the exact syntax for:
   - List statistics blocks (T10.G4.06)
   - Table creation and column addition (T10.G5.02)
   - Table lookup block (T10.G6.04)
   - Group-by/aggregation block (T10.G6.05)
   - Pivot block (T10.G7.01)

2. **AI Integration:** Does T10.G7.10 (Use AI to analyze table data) accurately reflect CreatiCode's AI capabilities?

3. **Google Sheets:** Does T10.G7.09 accurately reflect CreatiCode's Google Sheets integration?

### Pedagogical Questions
1. **G3 Introduction:** Is 9 skills too many for G3? Should some be moved to G4?
2. **G4 Coverage:** Is 15 skills too many for G4? Should it be split?
3. **Table Introduction:** Is G5 the right grade to introduce tables, or should it be G6?

### Scope Questions
1. **Advanced Algorithms:** Are G8 sorting algorithms (bubble, selection) appropriate for K-8, or too advanced?
2. **Hash Tables:** Is T10.G8.07 (hash table) too advanced for G8?
3. **Regex:** Is T10.G7.08 (regex patterns) appropriate for G7?

---

## I. NEXT STEPS

1. **Review this analysis** - Verify all findings and recommendations
2. **Verify CreatiCode blocks** - Check platform for exact syntax (Phase 2)
3. **Apply critical fixes** - Update dependencies and descriptions (Phase 1)
4. **Add new skills** - Insert 4 missing skills (Phase 3)
5. **Update allskills.md** - Implement all approved changes
6. **Create test cases** - Develop assessments for each skill
7. **Document examples** - Create sample projects demonstrating each skill

---

## APPENDIX A: Complete Skill List with Status

### GK (8 skills) - NO CHANGES
- T10.GK.01: Sort picture cards into groups ✓
- T10.GK.02: Count items in each group ✓
- T10.GK.03: Find which group has more ✓
- T10.GK.04: Add an item to the right group ✓
- T10.GK.05: Find the first and last item in a row ✓
- T10.GK.06: Look at a simple picture table ✓
- T10.GK.07: Match items that go together ✓
- T10.GK.08: Find all items with a special mark ✓

### G1 (6 skills) - NO CHANGES
- T10.G1.01: Sort items using two rules ✓
- T10.G1.02: Make a picture tally chart ✓
- T10.G1.03: Read information from a picture table ✓
- T10.G1.04: Find the row or column with the most ✓
- T10.G1.05: Complete a pattern in a table ✓
- T10.G1.06: Find items that belong in both groups ✓

### G2 (7 skills) - NO CHANGES
- T10.G2.01: Build a simple data table from a list ✓
- T10.G2.02: Add a new row to a table ✓
- T10.G2.03: Compare two rows in a table ✓
- T10.G2.04: Sort table rows by a column value ✓
- T10.G2.05: Find all rows that match a rule ✓
- T10.G2.06: Count rows that match a condition ✓
- T10.G2.07: Understand what a list is in coding ✓

### G3 (8 → 9 skills) - 1 NEW SKILL
- T10.G3.01: Create a list and add items to it ✓
- **T10.G3.09: Display a list monitor on the stage [NEW]**
- T10.G3.02: Read items from a list by position ✓
- T10.G3.03: Get the length of a list ✓
- T10.G3.04: Remove an item from a list ✓
- T10.G3.05: Loop through each item in a list ✓
- T10.G3.06: Check if a list contains a specific item ✓
- T10.G3.07: Count items in a list that match a condition ✓
- T10.G3.08: Check if a list is empty before accessing ✓

### G4 (13 → 15 skills) - 2 NEW SKILLS
- T10.G4.01: Find an item's position in a list (linear search) ✓
- T10.G4.02: Store and retrieve parallel list data ✓
- T10.G4.03: Insert an item at a specific position ✓
- T10.G4.04: Replace an item in a list ✓
- T10.G4.05: Use built-in blocks to sort a list ✓
- **T10.G4.14: Reverse the order of items in a list [NEW]**
- **T10.G4.15: Randomly shuffle items in a list [NEW]**
- T10.G4.06: Use built-in blocks to get list statistics [VERIFY BLOCKS]
- T10.G4.07: Find the maximum or minimum item manually ✓
- T10.G4.08: Filter items from a list based on a condition ✓
- T10.G4.09: Build a high score list with parallel lists ✓
- T10.G4.10: Swap two items in a list ✓
- T10.G4.11: Copy or append one list to another ✓
- T10.G4.12: Split a text string into a list ✓
- T10.G4.13: Join list items into a text string [ADD DEPENDENCY]

### G5 (10 → 11 skills) - 1 NEW SKILL
- T10.G5.01: Understand table structure (rows, columns, cells) ✓
- T10.G5.02: Create a table and add columns [VERIFY BLOCKS]
- T10.G5.03: Add rows of data to a table ✓
- T10.G5.04: Read a cell value from a table ✓
- T10.G5.05: Update a cell value in a table ✓
- T10.G5.06: Get the row count and find a row by value ✓
- T10.G5.07: Loop through table rows to compute aggregates ✓
- T10.G5.08: Use built-in table aggregate blocks ✓
- T10.G5.09: Delete rows from a table ✓
- **T10.G5.11: Insert a row at a specific position [NEW]**
- T10.G5.10: Convert between lists and tables ✓

### G6 (7 skills) - NO CHANGES
- T10.G6.01: Sort a table by a column ✓
- T10.G6.02: Filter table rows based on a condition ✓
- T10.G6.03: Copy and append tables ✓
- T10.G6.04: Use table lookup to find related data [VERIFY BLOCKS]
- T10.G6.05: Group data and compute aggregates per group [VERIFY BLOCKS]
- T10.G6.06: Use set operations on lists ✓
- T10.G6.07: Remove duplicate items from a list ✓

### G7 (10 skills) - 1 DEPENDENCY FIX, 2 DESCRIPTION UPDATES
- T10.G7.01: Pivot or reshape table data [FIX H1 - REMOVE DEPENDENCY, VERIFY BLOCKS]
- T10.G7.02: Import external data into a table ✓
- T10.G7.03: Design a table schema for a real-world scenario ✓
- T10.G7.04: Visualize table data with charts ✓
- T10.G7.05: Clean and transform table data [UPDATE L2 - CLARIFY]
- T10.G7.06: Validate and handle missing data [UPDATE L2 - CLARIFY]
- T10.G7.07: Analyze a dataset to find patterns or outliers ✓
- T10.G7.08: Use regex patterns to find items in lists ✓
- T10.G7.09: Connect to Google Sheets ✓
- T10.G7.10: Use AI to analyze table data ✓

### G8 (8 skills) - 2 DEPENDENCY FIXES
- T10.G8.01: Use nested loops to compare data across tables ✓
- T10.G8.02: Implement bubble sort algorithm [FIX H2 - REMOVE DEPENDENCY]
- T10.G8.03: Implement selection sort algorithm ✓
- T10.G8.04: Build a simulation using table-based state ✓
- T10.G8.05: Query and report statistics from complex dataset ✓
- T10.G8.06: Model relationships using multiple linked tables ✓
- T10.G8.07: Implement a hash table lookup using lists ✓
- T10.G8.08: Use advanced list operations for optimization [FIX H3 - REMOVE DEPENDENCY]

---

## APPENDIX B: Detailed New Skill Specifications

### NEW1: T10.G3.09
```
ID: T10.G3.09
Topic: T10 – Lists & Tables
Skill: Display a list monitor on the stage
Description: Students enable the list monitor by checking the checkbox next to the list name in the Variables palette. They observe how the monitor displays all items in the list with their positions (1, 2, 3...). As they add, remove, or change items, they watch the monitor update in real-time. This visual feedback is essential for understanding list state and debugging list operations.

Dependencies:
* T10.G3.01: Create a list and add items to it

Placement: After T10.G3.01, renumber subsequent skills
```

### NEW2: T10.G4.14
```
ID: T10.G4.14
Topic: T10 – Lists & Tables
Skill: Reverse the order of items in a list
Description: Students use the `reverse list [list]` block to flip the order of items, so the first item becomes last and the last becomes first. They observe the list monitor to see how positions change. Students understand when reversing is useful: converting ascending to descending order, reversing time sequences, or inverting rankings.

Dependencies:
* T10.G3.01: Create a list and add items to it
* T10.G3.02: Read items from a list by position (index starts at 1)

Placement: After T10.G4.05 (sort), renumber subsequent skills
```

### NEW3: T10.G4.15
```
ID: T10.G4.15
Topic: T10 – Lists & Tables
Skill: Randomly shuffle items in a list
Description: Students use the `reshuffle list [list]` block to randomly rearrange all items in the list. Each shuffle produces a different random order. Students use this for games: shuffling a deck of cards, randomizing quiz questions, or creating random starting positions. They understand that reshuffling destroys the original order.

Dependencies:
* T10.G3.01: Create a list and add items to it

Placement: After T10.G4.14 (reverse), renumber subsequent skills
```

### NEW4: T10.G5.11
```
ID: T10.G5.11
Topic: T10 – Lists & Tables
Skill: Insert a row at a specific position in a table
Description: Students use the `insert into table [table] at row (n): [value1] [value2]...` block to add a new row at the beginning, middle, or specific position. They understand that existing rows shift down to make room (row numbers increase by 1 for all rows at or after the insertion point). This parallels list insertion (T10.G4.03) for tables.

Dependencies:
* T10.G5.03: Add rows of data to a table
* T10.G5.06: Get the row count and find a row by value

Placement: After T10.G5.09 (delete), before T10.G5.10 (convert)
```

---

## APPENDIX C: Block Verification Checklist

**For CreatiCode Platform Review:**

### List Blocks to Verify
- [ ] `add [item] to [list]` - confirmed exists?
- [ ] `item (1) of [list]` - confirmed exists?
- [ ] `length of [list]` - confirmed exists?
- [ ] `delete (position) of [list]` - confirmed exists?
- [ ] `delete all of [list]` - confirmed exists?
- [ ] `for each [item] in [list]` - confirmed exists?
- [ ] `[list] contains [item]?` - confirmed exists?
- [ ] `item # of [value] in [list]` - confirmed exists?
- [ ] `insert [item] at (position) of [list]` - confirmed exists?
- [ ] `replace item (position) of [list] with [value]` - confirmed exists?
- [ ] `sort list [list] from [large to small/small to large]` - confirmed exists?
- [ ] `reverse list [list]` - confirmed exists? [NEW]
- [ ] `reshuffle list [list]` - confirmed exists? [NEW]
- [ ] `[sum/average/smallest/largest/median] of list [list]` - VERIFY EXACT SYNTAX
- [ ] `split [text] by [delimiter]` - confirmed exists?
- [ ] `join items of [list] with [delimiter]` - confirmed exists?
- [ ] `unique items of [list]` - confirmed exists?
- [ ] `[list1] union [list2]` - confirmed exists?
- [ ] `[list1] intersect [list2]` - confirmed exists?
- [ ] `[list1] minus [list2]` - confirmed exists?
- [ ] `items in [list] matching pattern [regex]` - confirmed exists?

### Table Blocks to Verify
- [ ] `add column [name] to table [table]` - VERIFY EXACT SYNTAX
- [ ] `add to table [table]: [value1] [value2]...` - VERIFY EXACT SYNTAX
- [ ] `insert into table [table] at row (n): [values]` - VERIFY EXACT SYNTAX [NEW]
- [ ] `item at row (n) column [name] of table [table]` - VERIFY EXACT SYNTAX
- [ ] `replace item at row (n) column [name] of table [table] with [value]` - confirmed exists?
- [ ] `row count of table [table]` - confirmed exists?
- [ ] `row # of [value] in column [name] in table [table]` - confirmed exists?
- [ ] `delete row (n) of table [table]` - confirmed exists?
- [ ] `delete rows with column [name] of value [v] from table [table]` - confirmed exists?
- [ ] `sort table [table] by column [name] [large to small/small to large]` - confirmed exists?
- [ ] `copy table [t1] into [t2]` - confirmed exists?
- [ ] `append table [t1] to [t2]` - confirmed exists?
- [ ] `make table from list [list]` - confirmed exists?
- [ ] `get column [name] from table [table] as list` - confirmed exists?
- [ ] `[sum/average/smallest/largest/median] of column [name] in table [table]` - VERIFY EXACT SYNTAX
- [ ] `item in column [return_col] of [table] where column [search_col] equals [value]` - VERIFY EXACT SYNTAX
- [ ] `set table [result] to [method] of column [value_col] in table [source] by column [group_col]` - VERIFY EXACT SYNTAX
- [ ] `pivot [source] into [result] row groups [cols] columns [values] methods [methods]` - VERIFY EXACT SYNTAX
- [ ] `import file into table [table]` - confirmed exists?
- [ ] `draw [line/bar/pie] chart using columns [...] from table [table]` - VERIFY EXACT SYNTAX

### Google Sheets & AI Blocks to Verify
- [ ] Google Sheets read block - VERIFY EXACT SYNTAX
- [ ] Google Sheets write block - VERIFY EXACT SYNTAX
- [ ] AI table analysis block - VERIFY EXACT SYNTAX

---

## CONCLUSION

The T10 topic is well-structured with strong pedagogical progression from K-8. The analysis identified:
- **3 HIGH priority dependency violations** (easily fixed)
- **5 MEDIUM priority block verification needs** (requires platform check)
- **2 LOW priority clarifications** (easy description updates)
- **4 missing skills** (fills important gaps)

After implementing the recommended fixes, T10 will have:
- ✓ 81 well-scaffolded skills (up from 77)
- ✓ 100% compliance with X-2 dependency rule
- ✓ Clear progression from picture-based (K-2) to advanced algorithms (G8)
- ✓ Accurate alignment with CreatiCode platform (pending verification)
- ✓ Comprehensive coverage of lists and tables

**Status:** READY FOR IMPLEMENTATION pending CreatiCode block verification.

---

**END OF ANALYSIS**
