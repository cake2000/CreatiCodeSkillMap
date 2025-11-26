# T10 Lists & Tables - Additional Quality Analysis

## Executive Summary

T10 has already undergone optimization (113→115 skills), with K-2 visual scenarios added and T10.G8.08 split. However, **systematic analysis reveals 7 categories of issues** requiring attention:

### Issue Count Summary
- **53 skills** with "understand" in descriptions (not in skill names)
- **7 X-2 rule violations** (dependencies spanning 3-4 grades)
- **6 missing concepts** (slicing, nested lists, stack/queue, merge)
- **3 orphaned skills** lacking T10 dependencies
- **Multiple potential redundancies** between skills

### Priority: MEDIUM
The existing optimization addressed the most critical issues (K-2 format, skill granularity). The remaining issues are **quality improvements** rather than structural problems.

---

## 1. VAGUE LANGUAGE: "Understand" in Descriptions

### Issue
**53 skills** use "understand" in their descriptions (not skill names). While skill names are action-oriented, descriptions contain passive learning language.

### Context
The word "understand" appears in **supportive explanatory text** within descriptions, not as the primary learning verb. Example:

**T10.G3.01.01**: "Create a new list variable"
- Description: "Students create a new list variable... They **understand** that lists are containers..."

This is **less critical** than having "Understand" in the skill name itself, but still adds vagueness.

### Affected Skills (Sample)
| Grade | Count | Examples |
|-------|-------|----------|
| G3 | 5 | G3.01.01 (Create list), G3.01.02 (Add item), G3.03 (Get length) |
| G4 | 16 | G4.06.01-05 (Aggregates), G4.11.01-02 (Copy/Append) |
| G5 | 17 | G5.02 (Create table), G5.06.01 (Row count), G5.09.01-03 (Delete operations) |
| G6 | 2 | G6.01 (Sort table), G6.06 (Set operations) |
| G7 | 5 | G7.02 (Import), G7.10 (Manage Sheets), G7.13 (Cloud storage) |
| G8 | 4 | G8.02 (Bubble sort), G8.03 (Selection sort), G8.08.02-03 (Two-pointer, Sliding window) |

### Recommended Fix
**Option A (Conservative):** Replace "understand" with observable outcomes
- "They understand X" → "They observe X" / "They verify X" / "They explain why X"

**Option B (Aggressive):** Remove understanding clauses entirely
- Keep only concrete actions and outcomes

**Example Revision:**
```
BEFORE: "They understand this scans all items and returns the lowest value."
AFTER: "They observe this scans all items and returns the lowest value."
OR: "They verify the result by comparing to manual inspection."
```

### Effort: MEDIUM (53 skills to revise)

---

## 2. X-2 RULE VIOLATIONS: Long-Range Dependencies

### Issue
**7 skills** depend on skills from 3-4 grades earlier, violating the X-2 rule for intra-topic dependencies.

### Violations

| Skill ID | Grade | Depends On | Dep Grade | Gap | Why Problematic |
|----------|-------|------------|-----------|-----|-----------------|
| **T10.G8.02** | 8 | T10.G4.10 (Swap) | 4 | **4 grades** | Bubble sort needs swap, but 4-year gap is too long |
| **T10.G8.03** | 8 | T10.G4.07 (Find min manually) | 4 | **4 grades** | Selection sort needs find-min concept |
| **T10.G8.07** | 8 | T10.G4.02 (Parallel lists) | 4 | **4 grades** | Hash table uses parallel lists concept |
| T10.G6.06 | 6 | T10.G3.06 (Contains) | 3 | 3 grades | Set operations use list membership |
| T10.G6.07 | 6 | T10.G3.06 (Contains) | 3 | 3 grades | Remove duplicates uses contains |
| T10.G7.08 | 7 | T10.G4.08 (Filter) | 4 | 3 grades | Regex filtering uses filter concept |
| T10.G8.04 | 8 | T10.G5.07 (Loop table rows) | 5 | 3 grades | Simulation loops through table |

### Root Cause Analysis

**Why These Gaps Exist:**
1. **Grade 5 focuses on tables** (not lists), creating a gap in list skill progression
2. **Grade 6-7** emphasize data operations over algorithmic foundations
3. **Grade 8** introduces algorithms requiring Grade 4 primitives not reinforced in G5-7

**Conceptual Flow:**
- G3: List basics (CRUD)
- G4: List algorithms (search, sort, aggregates, swap, parallel lists)
- G5: **TABLES** (different data structure)
- G6-7: Table operations + some list utilities
- G8: Advanced algorithms → **reach back to G4 for primitives**

### Recommended Fixes

#### Priority 1: Grade 8 Violations (4-grade gaps)

**Fix A: Add intermediate skills in Grade 6-7**

Add these bridging skills to reinforce G4 concepts:

**Grade 6:**
- **T10.G6.09**: Review and apply list item swapping (refresher on T10.G4.10)
- **T10.G6.10**: Find extreme values in filtered lists (combines T10.G4.07 + T10.G4.08)

**Grade 7:**
- **T10.G7.15**: Implement parallel lists for real-world data (refresher on T10.G4.02)

Then update G8 dependencies:
- T10.G8.02: Depends on **T10.G6.09** (swap refresher) instead of T10.G4.10
- T10.G8.03: Depends on **T10.G6.10** (find min in context) instead of T10.G4.07
- T10.G8.07: Depends on **T10.G7.15** (parallel lists) instead of T10.G4.02

**Fix B: Accept cross-topic exception**

Acknowledge that G4 foundational algorithms are **foundational primitives** that can be referenced from G8, similar to how T09 (Variables) are referenced across all grades.

Add note to skill: *"This skill builds on list fundamentals from Grade 4 (T10.G4.10). Students should review swapping before attempting this advanced algorithm."*

#### Priority 2: Grade 6-7 Violations (3-grade gaps)

**Fix:** Add intermediate skill in Grade 5:
- **T10.G5.19**: Check if a list contains a value (revisit T10.G3.06 in context of tables)

Then update:
- T10.G6.06, T10.G6.07: Depend on T10.G5.19 instead of T10.G3.06

### Recommendation: **Fix B (Cross-topic Exception)** for G8, **Fix A (Add bridge)** for G6-7

**Rationale:** Grade 8 skills are advanced algorithms that inherently require foundational primitives. Adding "refresher" skills in G6-7 would dilute focus on table operations. Better to treat G4 list primitives as **persistent foundations** like variables.

For G6-7 (3-grade gaps), adding one bridge skill in G5 is reasonable.

---

## 3. MISSING CONCEPTS: Important List Operations

### Issue
**6 important list/table concepts** are missing from the curriculum:

| Missing Concept | Description | Typical Grade | Importance |
|-----------------|-------------|---------------|------------|
| **List slicing** | Extract sublist (items 2-5) | Grade 5-6 | HIGH - Common in real programming |
| **List concatenation** | Join two lists into one (not append) | Grade 4-5 | MEDIUM - Overlaps with append |
| **Nested lists** | Lists within lists (2D arrays) | Grade 6-7 | HIGH - Essential for matrices, grids |
| **Stack operations** | Push/pop (LIFO) | Grade 7-8 | MEDIUM - Important CS concept |
| **Queue operations** | Enqueue/dequeue (FIFO) | Grade 7-8 | MEDIUM - Important CS concept |
| **Merge sorted lists** | Combine two sorted lists into one sorted list | Grade 8 | MEDIUM - Foundational for merge sort |

### Recommended Additions

#### Tier 1 (Essential - Add Now)

**Grade 5:**
```
ID: T10.G5.20
Skill: Extract a range of items from a list (slicing)
Description: Students use blocks or loops to extract a sublist containing items
from position A to position B (e.g., get items 2-5 from a 10-item list). They
understand slicing creates a new list without modifying the original.
Dependencies: T10.G3.02 (Read by position), T10.G3.03 (Get length)
```

**Grade 6:**
```
ID: T10.G6.11
Skill: Work with nested lists (lists within lists)
Description: Students create and manipulate lists where each item is itself a list
(e.g., [[1,2], [3,4], [5,6]]). They access nested items using double indexing
(item 2 of (item 1 of myList)) and use nested lists to represent grids, matrices,
or grouped data.
Dependencies: T10.G3.02 (Read by position), T10.G4.02 (Parallel lists)
```

**Grade 7:**
```
ID: T10.G7.16
Skill: Implement stack operations (push and pop)
Description: Students implement Last-In-First-Out (LIFO) behavior using list
operations: push (add to end), pop (remove from end and return value). They build
simple stack applications like undo functionality or expression evaluation.
Dependencies: T10.G3.01.02 (Add to end), T10.G3.04.01 (Delete at position)
```

#### Tier 2 (Nice to Have - Consider for Future)

**Grade 7:**
```
ID: T10.G7.17
Skill: Implement queue operations (enqueue and dequeue)
Description: Students implement First-In-First-Out (FIFO) behavior: enqueue
(add to end), dequeue (remove from beginning and return value). They build
applications like waiting lines or task scheduling.
Dependencies: T10.G7.16 (Stack operations)
```

**Grade 8:**
```
ID: T10.G8.11
Skill: Merge two sorted lists into one sorted list
Description: Students implement the merge operation used in merge sort: given two
sorted lists, create a new sorted list containing all items. They use two-pointer
technique to compare and interleave items efficiently.
Dependencies: T10.G8.08.02 (Two-pointer technique), T10.G4.05 (Sort lists)
```

### Effort: HIGH (5 new skills + dependencies + testing)

---

## 4. ORPHANED SKILLS: Missing T10 Dependencies

### Issue
**3 skills** (excluding Grade K/1) have NO dependencies within T10, making them appear disconnected from the topic progression.

| Skill ID | Skill Name | Current Dependencies | Issue |
|----------|------------|---------------------|-------|
| **T10.GK.01** | Sort picture cards into groups | *(none)* | Expected - foundational K skill |
| **T10.GK.05** | Find first and last item in a row | T01.GK.03 | Should depend on T10.GK.01 |
| **T10.G3.01.01** | Create a new list variable | T09.G3.01.01 | Should depend on T10.G2.07 |

### Recommended Fixes

**1. T10.GK.05** - Add T10 dependency:
```
Dependencies:
* T10.GK.01: Sort picture cards into groups  [ADD THIS]
* T01.GK.03: Find the first and last pictures
```
**Rationale:** Understanding "first" and "last" in a row builds on the concept of ordered groups introduced in T10.GK.01.

**2. T10.G3.01.01** - Add T10 dependency:
```
Dependencies:
* T10.G2.07: Identify real-world examples of lists  [ADD THIS]
* T09.G3.01.01: Create a new variable
```
**Rationale:** Students should recognize what lists ARE (G2.07) before learning to create them in code (G3.01.01). This bridges picture-based lists to code-based lists.

---

## 5. POTENTIAL REDUNDANCIES

### Issue
Some skills have high name similarity (60-90%), suggesting potential overlap or unclear differentiation.

### High-Priority Cases to Review

#### Case 1: Count vs. Find All (Grade 2)
- **T10.G2.05**: Find all rows that match a rule → Returns/marks the rows
- **T10.G2.06**: Count rows that match a condition → Returns a number

**Assessment:** NOT redundant - different outputs (collection vs. count).
**Recommendation:** Add clarification to descriptions to emphasize the difference.

#### Case 2: Filter vs. Select Multiple (Grade 4)
- **T10.G4.08**: Filter items from a list based on a condition
- **T10.G4.20**: Select multiple items from a list by criteria

**Assessment:** Potentially redundant (62% similar names).
**Action Required:** Check actual descriptions to determine if they're distinct or duplicates.

#### Case 3: Add Column vs. Insert Row (Grade 5)
- **T10.G5.11.01**: Add a column at a specific position
- **T10.G5.13**: Insert a row at a specific position

**Assessment:** NOT redundant - different operations (columns vs. rows).
**Recommendation:** Ensure descriptions clearly distinguish column vs. row operations.

#### Case 4: Sort Algorithms (Grade 8)
- **T10.G8.02**: Implement bubble sort algorithm step by step
- **T10.G8.03**: Implement selection sort algorithm step by step

**Assessment:** NOT redundant (87% similar is expected - both sorting algorithms).
**Recommendation:** Ensure each skill clearly describes which algorithm and its unique characteristics.

### Low-Priority Cases
The T10.G4.06 sub-skills (smallest, largest, sum, average, median) show high similarity (60-89%) but are **intentionally parallel** - each is a distinct aggregate function. No action needed.

---

## 6. DEPENDENCY CHAIN ISSUES

### Issue: Grade 4 Skills Without Grade 3 Foundation

**5 Grade 4 skills** have T10 dependencies but skip directly to G4 skills without building on G3:

| Skill | Dependencies | Issue |
|-------|--------------|-------|
| T10.G4.06.02 (Largest) | T10.G4.06.01 only | Should also depend on G3 fundamentals |
| T10.G4.06.03 (Sum) | T10.G4.06.01 only | Missing G3 loop foundation |
| T10.G4.06.05 (Median) | T10.G4.05, T10.G4.06.04 | Missing G3 list basics |
| T10.G4.09 (High scores) | T10.G4.01.02, T10.G4.02, T10.G4.03 | All G4 - missing G3 foundation |
| T10.G4.10 (Swap) | T10.G4.04 only | Missing G3 read/write basics |

### Analysis
These skills likely have **implicit** G3 dependencies through their existing deps:
- T10.G4.06.01 → depends on T10.G3.01.02 (Add items) and T10.G3.03 (Get length)
- T10.G4.02 → depends on T10.G3.01.02 and T10.G3.02

**Assessment:** This is a **documentation clarity issue**, not a pedagogical problem.

### Recommendation
**No structural changes needed.** The dependencies flow correctly through the chain. This is TRANSITIVE dependency inheritance working as expected.

**Optional Enhancement:** Add comment to T10.G4 section header:
```
"Note: All Grade 4 skills build on Grade 3 list fundamentals (create, add, read,
delete, loop) through their direct dependencies. Transitive dependencies ensure
proper prerequisite coverage."
```

---

## 7. GRADE-SPECIFIC OBSERVATIONS

### Grade K-2: ✓ EXCELLENT
- All 21 skills have proper Visual scenario format
- Clear progression from sorting to basic tables
- Good use of picture-based concrete scenarios

### Grade 3: ✓ STRONG
- 12 skills cover CRUD operations comprehensively
- Good foundation for Grade 4 expansion
- Clear progression from create → read → modify → delete → iterate

**Potential Addition:** Consider adding one skill on "When to use a list vs. a variable" to help students choose appropriate data structures.

### Grade 4: ⚠ DENSE (27 skills)
- Largest grade by far (27 skills vs. 12 in G3, 23 in G5)
- Covers search, parallel lists, aggregates, text conversion, random generation
- Might benefit from moving some skills to G5

**Recommendation:** Consider moving 3-4 advanced skills to Grade 5:
- T10.G4.19 (Find substring) → G5 (more advanced text operation)
- T10.G4.20 (Select multiple by criteria) → G5 (if redundant with G4.08)
- T10.G4.16.02 (Seeded random) → G5 (advanced concept)

### Grade 5: ✓ WELL-STRUCTURED (23 skills)
- Focus on tables is clear and appropriate
- Good parallel to G3-G4 list operations
- Comprehensive table CRUD coverage

### Grade 6: ⚠ LIGHT (8 skills)
- Smallest non-K grade
- Focuses on advanced table operations (sort, filter, group)
- **Could accommodate the missing concepts** (nested lists, slicing)

**Recommendation:** Add 2-3 skills here to balance workload:
- T10.G6.11: Nested lists (proposed above)
- T10.G6.09-10: Bridge skills for G8 dependencies (if using Fix A)

### Grade 7: ✓ APPROPRIATE (14 skills)
- Real-world focus (external data, Google Sheets, AI)
- Good integration with practical applications
- Could add stack/queue operations here

### Grade 8: ✓ STRONG (10 skills)
- Advanced algorithms well-scoped
- Splitting G8.08 into 3 sub-skills was correct
- Dependency issues (X-2 violations) need addressing

---

## SUMMARY OF RECOMMENDED CHANGES

### Priority 1 (High Impact, Moderate Effort)

1. **Fix X-2 violations for Grade 6-7** (3-grade gaps)
   - Add T10.G5.19: Check if list contains (bridge for G6.06, G6.07)
   - Update 2 dependencies
   - **Effort:** 1 new skill

2. **Add missing Tier 1 concepts**
   - T10.G5.20: List slicing
   - T10.G6.11: Nested lists
   - T10.G7.16: Stack operations
   - **Effort:** 3 new skills

3. **Fix orphaned skills**
   - Add T10 dependencies to T10.GK.05 and T10.G3.01.01
   - **Effort:** 2 dependency updates

### Priority 2 (Quality Improvement, Higher Effort)

4. **Replace "understand" in descriptions** (53 skills)
   - Use "observe," "verify," "explain," or remove
   - **Effort:** 53 skill revisions (can be batched)

5. **Clarify similar-named skills**
   - Review T10.G4.08 vs T10.G4.20 (filter vs select)
   - Add distinguishing notes to 3-4 skill pairs
   - **Effort:** 6-8 skill revisions

### Priority 3 (Consider for Future Versions)

6. **Balance Grade 4** (27 skills is high)
   - Move 3-4 skills to Grade 5 or 6
   - **Effort:** 4 skill relocations + dependency updates

7. **Address Grade 8 X-2 violations** (4-grade gaps)
   - Decision: Accept as foundational exceptions OR add bridge skills
   - **Effort:** 0 (accept) or 3 new skills (bridge)

8. **Add Tier 2 concepts**
   - T10.G7.17: Queue operations
   - T10.G8.11: Merge sorted lists
   - **Effort:** 2 new skills

---

## IMPACT ASSESSMENT

### Current State: 115 skills
After Priority 1 + 2 changes: **119-120 skills**
- +4 new skills (slicing, nested lists, stack, list-contains-bridge)
- +53 description revisions (understand → observe/verify)
- +2 dependency additions (orphaned skills)
- +6 clarifications (similar-named skills)

### Quality Improvements
- **X-2 violations:** 7 → 4 (G6-7 fixed, G8 remain as foundational exceptions)
- **Missing concepts:** 6 → 3 (Tier 1 added, Tier 2 deferred)
- **Orphaned skills:** 3 → 1 (GK.01 remains as expected foundation)
- **Vague language:** 53 → 0 (all "understand" replaced)

### Pedagogical Impact
- **Grade 5:** +2 skills (slicing, list-contains)
- **Grade 6:** +1 skill (nested lists)
- **Grade 7:** +1 skill (stack operations)
- Better concept coverage
- Clearer progression from G4 → G8

---

## NEXT STEPS

1. **Review and approve** Priority 1 recommendations
2. **Decide on Grade 8 X-2 violations:** Exception or bridge?
3. **Draft new skill descriptions** for 4 new skills
4. **Batch-revise 53 descriptions** to remove "understand"
5. **Test dependency chain** after changes
6. **Update skill count documentation**

---

## APPENDIX: Detailed Skill List with "Understand"

<details>
<summary>Click to expand full list of 53 skills containing "understand"</summary>

### Grade 3 (5 skills)
- T10.G3.01.01: Create a new list variable
- T10.G3.01.02: Add an item to the end of a list
- T10.G3.02: Read items from a list by position
- T10.G3.03: Get the length of a list
- T10.G3.04.01: Delete an item at a specific position
- T10.G3.04.02: Clear all items from a list
- T10.G3.09: Increment or decrement a list item's value (also has "know")

### Grade 4 (16 skills)
- T10.G4.01.01: Find an item's position using built-in block
- T10.G4.03: Insert an item at a specific position
- T10.G4.04: Replace an item in a list
- T10.G4.05: Use built-in blocks to sort a list
- T10.G4.06.01: Find the smallest value in a list
- T10.G4.06.02: Find the largest value in a list
- T10.G4.06.03: Calculate the sum of all values in a list
- T10.G4.06.04: Calculate the average of values in a list
- T10.G4.06.05: Find the median value in a list
- T10.G4.11.01: Copy one list to another
- T10.G4.11.02: Append one list to another
- T10.G4.14: Reverse the order of items
- T10.G4.15: Randomly shuffle items
- T10.G4.16.02: Generate seeded random list
- T10.G4.17: Delete an item by value (also has "know")
- T10.G4.18: Loop through list indices (has "know")
- T10.G4.19: Find an item containing a substring

### Grade 5 (17 skills)
- T10.G5.02: Create a table and add columns
- T10.G5.03: Add rows of data to a table
- T10.G5.05: Update a cell value in a table
- T10.G5.06.01: Get the number of rows
- T10.G5.06.02: Find which row contains a value
- T10.G5.09.01: Delete a single row by index
- T10.G5.09.02: Delete rows matching a condition
- T10.G5.09.03: Clear all rows from a table
- T10.G5.10: Convert between lists and tables
- T10.G5.11.01: Add a column at a specific position
- T10.G5.11.02: Delete a single column
- T10.G5.11.03: Remove all columns from a table
- T10.G5.12: Copy list data to table column
- T10.G5.13: Insert a row at a specific position
- T10.G5.14: Replace an entire row in a table
- T10.G5.15: Get an entire row as a text string
- T10.G5.17: Increment or decrement a table cell value

### Grade 6 (2 skills)
- T10.G6.01: Sort a table by a column
- T10.G6.06: Use set operations on lists

### Grade 7 (5 skills)
- T10.G7.02: Import external data into a table
- T10.G7.09: Read and write data with Google Sheets (has "learn")
- T10.G7.10: Manage Google Sheets structure
- T10.G7.12: Export table data to a file
- T10.G7.13: Save and load data to the cloud
- T10.G7.14: Use AI to analyze table data (has "learn")

### Grade 8 (4 skills)
- T10.G8.02: Implement bubble sort algorithm
- T10.G8.03: Implement selection sort algorithm
- T10.G8.08.02: Use two-pointer technique
- T10.G8.08.03: Apply sliding window algorithms

</details>
