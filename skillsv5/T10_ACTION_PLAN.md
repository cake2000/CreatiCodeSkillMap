# T10 Lists & Tables - Specific Changes Required

## Quick Stats
- **Current:** 115 skills (K=8, 1=6, 2=7, 3=12, 4=27, 5=23, 6=8, 7=14, 8=10)
- **After changes:** ~119-120 skills
- **Estimated effort:** 2-3 hours for Priority 1, 4-6 hours for Priority 2

---

## PRIORITY 1: Critical Quality Improvements

### Change 1: Fix 3 Orphaned Skills (Add Dependencies)

**T10.GK.05** - Find first and last item in a row
```diff
Dependencies:
+ * T10.GK.01: Sort picture cards into groups
  * T01.GK.03: Find the first and last pictures
```

**T10.G3.01.01** - Create a new list variable
```diff
Dependencies:
+ * T10.G2.07: Identify real-world examples of lists
  * T09.G3.01.01: Create a new variable
```

**Effort:** 5 minutes (2 dependency additions)

---

### Change 2: Add 1 Bridge Skill for Grade 6 Dependencies

**ADD NEW SKILL:**

```
ID: T10.G5.19
Topic: T10 – Lists & Tables
Skill: Check if a list contains a specific value
Description: Students revisit the list membership concept from Grade 3 in the
context of table operations. Given a list extracted from a table column, they use
the `[list] contains [item]?` block to check for value presence. They apply this
to validate data, check for duplicates before adding, or verify expected values
exist before processing.

Dependencies:
* T10.G3.06: Check if a list contains a specific item
* T10.G5.10: Convert between lists and tables
```

**UPDATE 2 DEPENDENCIES:**

**T10.G6.06** - Use set operations on lists
```diff
Dependencies:
+ * T10.G5.19: Check if a list contains a specific value
- * T10.G3.06: Check if a list contains a specific item
  * T10.G4.08: Filter items from a list based on a condition
```

**T10.G6.07** - Remove duplicate items from a list
```diff
Dependencies:
+ * T10.G5.19: Check if a list contains a specific value
- * T10.G3.06: Check if a list contains a specific item
  * T10.G4.08: Filter items from a list based on a condition
```

**Impact:** Fixes 2 X-2 violations (G6 depending on G3 = 3-grade gap)

**Effort:** 30 minutes (1 new skill + 2 dependency updates)

---

### Change 3: Add 3 Missing Tier 1 Concepts

#### ADD: T10.G5.20 - List Slicing

```
ID: T10.G5.20
Topic: T10 – Lists & Tables
Skill: Extract a range of items from a list (slicing)
Description: Students extract a sublist containing items from position A to
position B using loops and conditionals. Given a list of 10 items, they create
a new list with items 3 through 7. They create an empty result list, loop from
start position to end position, read each item, and add it to the result list.
Students understand slicing creates a new list without modifying the original.
This is useful for processing data in chunks, analyzing time windows, or extracting
relevant portions of datasets.

Dependencies:
* T10.G3.02: Read items from a list by position (index starts at 1)
* T10.G3.03: Get the length of a list
* T10.G3.05: Loop through each item in a list
```

#### ADD: T10.G6.11 - Nested Lists

```
ID: T10.G6.11
Topic: T10 – Lists & Tables
Skill: Work with nested lists (lists within lists)
Description: Students create and manipulate lists where each item is itself a list,
creating a 2-dimensional structure (e.g., [[1,2], [3,4], [5,6]]). They access
nested items using double indexing: first select which inner list (item 2 of
myList), then select which item within that list (item 1 of [inner list]). They
use nested lists to represent grids (game boards, pixel art), matrices (math
operations), or grouped data (teams of players, classes of students). Students
loop through nested lists using nested loops: outer loop for each inner list,
inner loop for items within each list.

Dependencies:
* T10.G3.02: Read items from a list by position (index starts at 1)
* T10.G4.02: Store and retrieve parallel list data
* T07.G6.01: Trace nested loops with variable bounds
```

#### ADD: T10.G7.16 - Stack Operations

```
ID: T10.G7.16
Topic: T10 – Lists & Tables
Skill: Implement stack operations (push and pop)
Description: Students implement Last-In-First-Out (LIFO) data structure behavior
using list operations. Push operation: add item to end of list. Pop operation:
get the last item's value, delete it from the list, and return the value. They
build applications using stacks: undo functionality (push each action, pop to
undo), expression evaluation (parentheses matching), or backtracking (maze solving).
Students observe that the most recently added item is always the first one
removed, like a stack of plates. They handle edge cases: check if stack is empty
before popping to avoid errors.

Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T10.G3.04.01: Delete an item at a specific position
* T10.G3.03: Get the length of a list
* T10.G3.08: Check if a list is empty before accessing
```

**Impact:** Adds essential programming concepts missing from curriculum

**Effort:** 90 minutes (3 new skills with detailed descriptions)

---

## PRIORITY 2: Language Quality (53 Skills)

### Change 4: Replace "Understand" with Observable Verbs

**Pattern:** Replace "They understand X" → "They observe X" / "They verify X" / "They note X"

**Affected Skills:** 53 total across all grades

**Examples:**

**T10.G3.01.01** - Create a new list variable
```diff
Description: Students create a new list variable in the Variables palette by
clicking "Make a List" and giving it a descriptive name (e.g., "fruits", "scores",
- "inventory"). They understand that lists are containers that can hold multiple
+ "inventory"). They observe that lists are containers that can hold multiple
values, unlike regular variables which hold only one value. This is the first
step before any list operations can be performed.
```

**T10.G4.06.01** - Find the smallest value in a list
```diff
Description: Students use the `[smallest v] of list [list]` block to find the
- minimum value in a numeric list. They understand this scans all items and
+ minimum value in a numeric list. They verify this scans all items and
returns the lowest value. They practice with different lists and predict which
value will be returned.
```

**T10.G5.02** - Create a table and add columns
```diff
Description: Students create an empty table variable and use `add column [name]
at position (n) to table [table]` to define the table structure. They
- understand that columns must be created before data can be added to them, and
+ note that columns must be created before data can be added to them, and
they can control column order using the position parameter (1 = first column,
2 = second, etc.).
```

**Replacement Guide:**
- "understand that X happens" → "observe that X happens"
- "understand this returns X" → "verify this returns X"
- "understand when to use X" → "identify when to use X"
- "understand columns must..." → "note that columns must..."
- "understand sorting rearranges..." → "observe that sorting rearranges..."

**Batch Processing:**
- Grade 3: 7 skills (includes 2 with "know")
- Grade 4: 16 skills (includes 2 with "know")
- Grade 5: 17 skills
- Grade 6: 2 skills
- Grade 7: 5 skills (includes 2 with "learn")
- Grade 8: 4 skills

**Effort:** 2-3 hours (can be done in batch with find-replace + manual review)

---

## PRIORITY 3: Optional Enhancements

### Change 5: Clarify Potential Redundancy (Review Needed)

**Investigate T10.G4.08 vs T10.G4.20:**

- T10.G4.08: Filter items from a list based on a condition
- T10.G4.20: Select multiple items from a list by criteria

**Action:** Read both full descriptions to determine if:
- They are duplicates → Merge or remove one
- They teach different aspects → Add distinguishing notes

**Effort:** 15 minutes investigation + 30 minutes revision if needed

---

### Change 6: Address Grade 8 X-2 Violations

**Current violations (4-grade gaps):**
- T10.G8.02 (Bubble sort) → depends on T10.G4.10 (Swap)
- T10.G8.03 (Selection sort) → depends on T10.G4.07 (Find min manually)
- T10.G8.07 (Hash table) → depends on T10.G4.02 (Parallel lists)

**Option A: Accept as foundational exception**
- Add note: "This skill builds on list fundamentals from Grade 4. Students should review [prerequisite] before attempting this algorithm."
- **Effort:** 10 minutes (add 3 notes)

**Option B: Add bridge skills in Grade 6-7**
- Add T10.G6.09: Review list item swapping
- Add T10.G6.10: Find extremes in filtered lists
- Add T10.G7.15: Apply parallel lists to real-world data
- **Effort:** 90 minutes (3 new skills)

**Recommendation:** Option A (foundational exception) - Grade 4 list primitives are persistent foundations like variables

---

### Change 7: Balance Grade 4 (27 Skills is High)

**Consider moving to Grade 5:**
- T10.G4.19: Find an item containing a substring → More advanced text operation
- T10.G4.16.02: Generate seeded random list → Advanced concept
- T10.G4.20: Select multiple items (if redundant with G4.08)

**Effort:** 1 hour (move 2-3 skills + update dependencies)

---

## DECISION REQUIRED

### Grade 8 X-2 Violations: Exception or Bridge?

**Question:** Should Grade 8 algorithm skills be allowed to depend on Grade 4 fundamentals (4-grade gap), or should we add intermediate bridge skills in Grades 6-7?

**Recommendation:** ACCEPT AS EXCEPTION
- Grade 4 introduces foundational primitives (swap, find-min, parallel lists)
- These are PERSISTENT skills like variables, not transient knowledge
- Grade 5-7 focus on tables (different data structure) - adding "refresher" skills would dilute focus
- Better to treat Grade 4 list primitives as permanent foundations

**If accepted:** Add explanatory notes to 3 Grade 8 skills (10 minutes)
**If rejected:** Create 3 bridge skills in Grades 6-7 (90 minutes)

---

## IMPLEMENTATION SEQUENCE

1. **Week 1: Core Additions** (Priority 1)
   - Day 1: Add T10.G5.19 (bridge skill for G6 deps)
   - Day 1: Update T10.GK.05 and T10.G3.01.01 dependencies
   - Day 2: Add T10.G5.20 (list slicing)
   - Day 3: Add T10.G6.11 (nested lists)
   - Day 4: Add T10.G7.16 (stack operations)
   - Day 5: Test all new skills and dependencies

2. **Week 2: Language Quality** (Priority 2)
   - Batch-replace "understand" in Grades 3-4 (16+7 skills)
   - Batch-replace "understand" in Grades 5-6 (17+2 skills)
   - Batch-replace "understand" + "learn" in Grades 7-8 (5+4 skills)
   - Manual review each change for context

3. **Week 3: Optional** (Priority 3)
   - Investigate G4.08 vs G4.20 redundancy
   - Decide on G8 X-2 violations (exception vs bridge)
   - Consider Grade 4 rebalancing

---

## SUMMARY OF CHANGES

| Change | Type | Count | Effort | Impact |
|--------|------|-------|--------|--------|
| Fix orphaned skills | Dependency | 2 | 5 min | Clarify progression |
| Add G5 bridge skill | New skill | 1 | 30 min | Fix 2 X-2 violations |
| Add missing concepts | New skill | 3 | 90 min | Essential concepts |
| Replace "understand" | Revision | 53 | 3 hrs | Language precision |
| Clarify redundancy | Investigation | 2 | 45 min | Avoid duplication |
| G8 X-2 decision | Decision | 3 | 10-90 min | Depends on choice |
| **TOTAL Priority 1** | - | **6** | **2 hrs** | **High** |
| **TOTAL Priority 1+2** | - | **59** | **5-6 hrs** | **Very High** |

---

## EXPECTED OUTCOME

**Before:** 115 skills, 53 with "understand", 7 X-2 violations, 6 missing concepts
**After:** 119 skills, 0 with "understand", 4-7 X-2 violations*, 3 missing concepts

*Depends on Grade 8 decision: 4 if exception accepted, 7 if bridges added

**Quality Score Improvement:**
- K-2 Format: Already ✓ (from previous optimization)
- Vague Verbs: 53 → 0 ✓
- X-2 Rule: 7 → 4-7 (improvement)
- Missing Concepts: 6 → 3 (50% coverage improvement)
- Orphaned Skills: 3 → 1 ✓

---

## FILES TO CREATE/MODIFY

**New Skills to Add:**
1. `/skillsv5/allskills.md` - Insert T10.G5.19 after T10.G5.18
2. `/skillsv5/allskills.md` - Insert T10.G5.20 after T10.G5.19
3. `/skillsv5/allskills.md` - Insert T10.G6.11 after T10.G6.10
4. `/skillsv5/allskills.md` - Insert T10.G7.16 after T10.G7.15

**Skills to Modify:**
- 2 skills: Update dependencies (T10.GK.05, T10.G3.01.01)
- 2 skills: Update dependencies (T10.G6.06, T10.G6.07)
- 53 skills: Replace "understand" with observable verbs (batch edit)

**Documentation to Update:**
- Update skill count: 115 → 119
- Update T10 optimization summary
- Add rationale for G8 X-2 decision (once made)
