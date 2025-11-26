# T10 Lists & Tables - Before/After Examples

This document shows concrete examples of the proposed changes.

---

## Example 1: Fixing Orphaned Skill (T10.GK.05)

### BEFORE
```
ID: T10.GK.05
Topic: T10 – Lists & Tables
Skill: Find the first and last item in a row
Description: **Student task:** Look at a row of 3-5 picture cards arranged from
left to right. Tap the first item, then tap the last item. **Visual scenario:**
Five picture cards in a row: apple, banana, orange, grape, watermelon.
**Correct answer:** Tap apple (first), then tap watermelon (last).
_Implementation note: Sequential tap activity with visual order indicators.
CSTA: EK-ALG-AF-01._

Dependencies:
* T01.GK.03: Find the first and last pictures
```

### AFTER
```
ID: T10.GK.05
Topic: T10 – Lists & Tables
Skill: Find the first and last item in a row
Description: **Student task:** Look at a row of 3-5 picture cards arranged from
left to right. Tap the first item, then tap the last item. **Visual scenario:**
Five picture cards in a row: apple, banana, orange, grape, watermelon.
**Correct answer:** Tap apple (first), then tap watermelon (last).
_Implementation note: Sequential tap activity with visual order indicators.
CSTA: EK-ALG-AF-01._

Dependencies:
* T10.GK.01: Sort picture cards into groups               [← ADDED]
* T01.GK.03: Find the first and last pictures
```

**Why:** Builds on the concept of ordered collections from GK.01

---

## Example 2: Adding Bridge Skill (NEW T10.G5.19)

### NEW SKILL INSERTION (After T10.G5.18)

```
ID: T10.G5.19
Topic: T10 – Lists & Tables
Skill: Check if a list contains a specific value
Description: Students revisit the list membership concept from Grade 3 in the
context of table operations. Given a list extracted from a table column, they
use the `[list] contains [item]?` block to check for value presence. They apply
this to validate data, check for duplicates before adding, or verify expected
values exist before processing. This bridges Grade 3 list fundamentals to
Grade 6 set operations.

Dependencies:
* T10.G3.06: Check if a list contains a specific item
* T10.G5.10: Convert between lists and tables
```

**Purpose:** Fixes 3-grade gap for G6.06 and G6.07

---

## Example 3: Updating Dependencies (T10.G6.06)

### BEFORE
```
ID: T10.G6.06
Topic: T10 – Lists & Tables
Skill: Use set operations on lists
Description: Students implement set operations like union (all unique items
from both lists), intersection (only items in both lists), and difference
(items in list1 but not list2) using loops and conditionals. They understand
mathematical set concepts applied to lists.

Dependencies:
* T10.G4.08: Filter items from a list based on a condition
* T10.G3.06: Check if a list contains a specific item      [← 3-GRADE GAP]
```

### AFTER
```
ID: T10.G6.06
Topic: T10 – Lists & Tables
Skill: Use set operations on lists
Description: Students implement set operations like union (all unique items
from both lists), intersection (only items in both lists), and difference
(items in list1 but not list2) using loops and conditionals. They observe
mathematical set concepts applied to lists.

Dependencies:
* T10.G4.08: Filter items from a list based on a condition
* T10.G5.19: Check if a list contains a specific value     [← FIXED: 1-GRADE GAP]
```

**Changes:**
1. "understand" → "observe" (language precision)
2. Dependency updated to T10.G5.19 (fixes X-2 violation)

---

## Example 4: Adding Missing Concept - List Slicing (NEW T10.G5.20)

### NEW SKILL

```
ID: T10.G5.20
Topic: T10 – Lists & Tables
Skill: Extract a range of items from a list (slicing)
Description: Students extract a sublist containing items from position A to
position B using loops and conditionals. Given a list of 10 items, they create
a new list with items 3 through 7. They create an empty result list, loop from
start position to end position, read each item, and add it to the result list.
Students observe that slicing creates a new list without modifying the original.
This is useful for processing data in chunks, analyzing time windows, or
extracting relevant portions of datasets.

Dependencies:
* T10.G3.02: Read items from a list by position (index starts at 1)
* T10.G3.03: Get the length of a list
* T10.G3.05: Loop through each item in a list
```

**Impact:** Fills essential programming concept gap

---

## Example 5: Adding Missing Concept - Nested Lists (NEW T10.G6.11)

### NEW SKILL

```
ID: T10.G6.11
Topic: T10 – Lists & Tables
Skill: Work with nested lists (lists within lists)
Description: Students create and manipulate lists where each item is itself a
list, creating a 2-dimensional structure (e.g., [[1,2], [3,4], [5,6]]). They
access nested items using double indexing: first select which inner list
(item 2 of myList), then select which item within that list (item 1 of
[inner list]). They use nested lists to represent grids (game boards, pixel art),
matrices (math operations), or grouped data (teams of players, classes of
students). Students loop through nested lists using nested loops: outer loop
for each inner list, inner loop for items within each list.

Dependencies:
* T10.G3.02: Read items from a list by position (index starts at 1)
* T10.G4.02: Store and retrieve parallel list data
* T07.G6.01: Trace nested loops with variable bounds
```

**Impact:** Essential for 2D data structures (grids, matrices)

---

## Example 6: Adding Missing Concept - Stack Operations (NEW T10.G7.16)

### NEW SKILL

```
ID: T10.G7.16
Topic: T10 – Lists & Tables
Skill: Implement stack operations (push and pop)
Description: Students implement Last-In-First-Out (LIFO) data structure behavior
using list operations. Push operation: add item to end of list. Pop operation:
get the last item's value, delete it from the list, and return the value. They
build applications using stacks: undo functionality (push each action, pop to
undo), expression evaluation (parentheses matching), or backtracking (maze
solving). Students observe that the most recently added item is always the first
one removed, like a stack of plates. They handle edge cases: check if stack is
empty before popping to avoid errors.

Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T10.G3.04.01: Delete an item at a specific position
* T10.G3.03: Get the length of a list
* T10.G3.08: Check if a list is empty before accessing
```

**Impact:** Essential CS data structure concept

---

## Example 7: Replacing "Understand" - Grade 3 Skill

### BEFORE
```
ID: T10.G3.01.01
Topic: T10 – Lists & Tables
Skill: Create a new list variable
Description: Students create a new list variable in the Variables palette by
clicking "Make a List" and giving it a descriptive name (e.g., "fruits", "scores",
"inventory"). They understand that lists are containers that can hold multiple
values, unlike regular variables which hold only one value. This is the first
step before any list operations can be performed.

Dependencies:
* T09.G3.01.01: Create a new variable
```

### AFTER
```
ID: T10.G3.01.01
Topic: T10 – Lists & Tables
Skill: Create a new list variable
Description: Students create a new list variable in the Variables palette by
clicking "Make a List" and giving it a descriptive name (e.g., "fruits", "scores",
"inventory"). They observe that lists are containers that can hold multiple
values, unlike regular variables which hold only one value. This is the first
step before any list operations can be performed.

Dependencies:
* T10.G2.07: Identify real-world examples of lists        [← ADDED]
* T09.G3.01.01: Create a new variable
```

**Changes:**
1. "understand" → "observe" (observable verb)
2. Added T10.G2.07 dependency (fixes orphaned skill)

---

## Example 8: Replacing "Understand" - Grade 4 Aggregate

### BEFORE
```
ID: T10.G4.06.01
Topic: T10 – Lists & Tables
Skill: Find the smallest value in a list
Description: Students use the `[smallest v] of list [list]` block to find the
minimum value in a numeric list. They understand this scans all items and returns
the lowest value. They practice with different lists and predict which value will
be returned.

Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T10.G3.03: Get the length of a list
```

### AFTER
```
ID: T10.G4.06.01
Topic: T10 – Lists & Tables
Skill: Find the smallest value in a list
Description: Students use the `[smallest v] of list [list]` block to find the
minimum value in a numeric list. They verify this scans all items and returns
the lowest value. They practice with different lists and predict which value will
be returned.

Dependencies:
* T10.G3.01.02: Add an item to the end of a list
* T10.G3.03: Get the length of a list
```

**Change:** "understand" → "verify" (testable action)

---

## Example 9: Replacing "Understand" - Grade 5 Table Operation

### BEFORE
```
ID: T10.G5.02
Topic: T10 – Lists & Tables
Skill: Create a table and add columns
Description: Students create an empty table variable and use `add column [name]
at position (n) to table [table]` to define the table structure. They understand
that columns must be created before data can be added to them, and they can
control column order using the position parameter (1 = first column, 2 = second,
etc.).

Dependencies:
* T10.G5.01: Identify table structure (rows, columns, cells)
```

### AFTER
```
ID: T10.G5.02
Topic: T10 – Lists & Tables
Skill: Create a table and add columns
Description: Students create an empty table variable and use `add column [name]
at position (n) to table [table]` to define the table structure. They note that
columns must be created before data can be added to them, and they can control
column order using the position parameter (1 = first column, 2 = second, etc.).

Dependencies:
* T10.G5.01: Identify table structure (rows, columns, cells)
```

**Change:** "understand that" → "note that" (neutral observation verb)

---

## Example 10: Replacing "Understand" - Grade 8 Algorithm

### BEFORE
```
ID: T10.G8.02
Topic: T10 – Lists & Tables
Skill: Implement bubble sort algorithm step by step
Description: Students implement bubble sort by writing nested loops: the outer
loop controls passes, the inner loop compares adjacent items and swaps if out of
order. They trace through the algorithm to understand how items "bubble" to their
correct positions.

Dependencies:
* T10.G4.10: Swap two items in a list
* T07.G6.01: Trace nested loops with variable bounds
```

### AFTER
```
ID: T10.G8.02
Topic: T10 – Lists & Tables
Skill: Implement bubble sort algorithm step by step
Description: Students implement bubble sort by writing nested loops: the outer
loop controls passes, the inner loop compares adjacent items and swaps if out of
order. They trace through the algorithm to observe how items "bubble" to their
correct positions.

Dependencies:
* T10.G4.10: Swap two items in a list                     [← 4-GRADE GAP]
* T07.G6.01: Trace nested loops with variable bounds
```

**Change:** "understand how" → "observe how" (observable action)

**Note:** 4-grade dependency gap remains (see decision point in Executive Summary)

---

## Example 11: Replacing "Learn" - Grade 7 Integration

### BEFORE
```
ID: T10.G7.09
Topic: T10 – Lists & Tables
Skill: Read and write data with Google Sheets
Description: Students use `read from google sheet: url [url] sheet name [name]
range [range] into table [table]` and `write into google sheet: url [url] sheet
name [name] start cell [cell] from table [table]` to sync data with Google Sheets.
They also use `list all sheets in google sheet at URL [url] into list [list]` to
get names of all sheets in a spreadsheet for dynamic sheet selection. They learn
to set up sharing, use proper URLs, and handle authentication.

Dependencies:
* T10.G7.02: Import external data into a table
* T10.G5.03: Add rows of data to a table
```

### AFTER
```
ID: T10.G7.09
Topic: T10 – Lists & Tables
Skill: Read and write data with Google Sheets
Description: Students use `read from google sheet: url [url] sheet name [name]
range [range] into table [table]` and `write into google sheet: url [url] sheet
name [name] start cell [cell] from table [table]` to sync data with Google Sheets.
They also use `list all sheets in google sheet at URL [url] into list [list]` to
get names of all sheets in a spreadsheet for dynamic sheet selection. They apply
these blocks to set up sharing, use proper URLs, and handle authentication.

Dependencies:
* T10.G7.02: Import external data into a table
* T10.G5.03: Add rows of data to a table
```

**Change:** "learn to" → "apply these blocks to" (active application)

---

## Summary of Changes in Examples

| Example | Type | Grade | Change |
|---------|------|-------|--------|
| 1 | Dependency | K | Add T10.GK.01 dependency |
| 2 | New Skill | 5 | Add T10.G5.19 (bridge skill) |
| 3 | Dependency + Language | 6 | Update dependency, "understand" → "observe" |
| 4 | New Skill | 5 | Add T10.G5.20 (list slicing) |
| 5 | New Skill | 6 | Add T10.G6.11 (nested lists) |
| 6 | New Skill | 7 | Add T10.G7.16 (stack operations) |
| 7 | Dependency + Language | 3 | Add dependency, "understand" → "observe" |
| 8 | Language | 4 | "understand" → "verify" |
| 9 | Language | 5 | "understand that" → "note that" |
| 10 | Language | 8 | "understand how" → "observe how" |
| 11 | Language | 7 | "learn to" → "apply...to" |

**Total Changes Shown:** 4 new skills, 3 dependency updates, 7 language improvements

**Pattern:** All changes maintain or improve pedagogical quality while making language more precise and observable.

---

## Verification Checklist After Changes

- [ ] All 4 new skills have proper dependencies
- [ ] All 4 new skills have clear, actionable descriptions
- [ ] All dependency updates maintain logical progression
- [ ] All "understand" replacements use observable verbs
- [ ] All "learn" replacements use active verbs
- [ ] Grade sequence remains K → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8
- [ ] Total skill count updated to 119
- [ ] No broken dependency references
- [ ] All cross-topic dependencies preserved
- [ ] CSTA standards preserved where present

---

## Quick Reference: Verb Replacement Guide

| Vague Verb | Context | Replace With | Example |
|------------|---------|--------------|---------|
| understand that X happens | Observable outcome | observe that X happens | "They observe that items shift down" |
| understand this returns X | Verifiable result | verify this returns X | "They verify this returns the minimum" |
| understand when to use X | Decision-making | identify when to use X | "They identify when slicing is needed" |
| understand columns must... | Required step | note that columns must... | "They note that columns must exist first" |
| understand sorting rearranges | Observable effect | observe that sorting rearranges | "They observe that sorting changes order" |
| learn to set up X | Active application | apply blocks to set up X | "They apply these blocks to set up sharing" |
| learn how X works | Investigation | explore how X works | "They explore how pivot tables work" |
| know the list length | Awareness | recognize the list length | "They recognize the list length changes" |

---

## File Usage Guide

**For quick review:** Read **T10_EXECUTIVE_SUMMARY.md** (2 pages)
**For specific changes:** Use **T10_ACTION_PLAN.md** (step-by-step)
**For visual examples:** This file (**T10_BEFORE_AFTER_EXAMPLES.md**)
**For complete analysis:** Read **T10_ADDITIONAL_ANALYSIS.md** (comprehensive)

**Recommended flow:**
1. Stakeholder reviews Executive Summary → approves Priority 1
2. Developer uses Action Plan → implements changes
3. Developer references Before/After Examples → ensures correct formatting
4. QA verifies changes using Additional Analysis → comprehensive checklist
