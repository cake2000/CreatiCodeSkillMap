# T10 Optimization - Visual Summary

## Before and After Comparison

```
GRADE K-2: NO CHANGES (21 skills remain unchanged)
├─ K: 8 skills (picture-based)
├─ 1: 6 skills (picture-based)
└─ 2: 7 skills (bridge to coding)

GRADE 3: SPLIT 2 SKILLS (+2 total)
Before (10 skills):                After (12 skills):
├─ T10.G3.01 ──────────────────┬─> T10.G3.01.01 Create list variable
│  (Create & add)              └─> T10.G3.01.02 Add item to list
├─ T10.G3.02                      T10.G3.02 (unchanged)
├─ T10.G3.03                      T10.G3.03 (unchanged)
├─ T10.G3.04 ──────────────────┬─> T10.G3.04.01 Delete at position
│  (Delete & clear)            └─> T10.G3.04.02 Clear all items
├─ T10.G3.05                      T10.G3.05 (unchanged)
├─ T10.G3.06                      T10.G3.06 (unchanged)
├─ T10.G3.07                      T10.G3.07 (unchanged)
├─ T10.G3.08                      T10.G3.08 (unchanged)
├─ T10.G3.09                      T10.G3.09 (unchanged)
└─ T10.G3.10                      T10.G3.10 (unchanged)

GRADE 4: SPLIT 2 SKILLS (+7 total)
Before (20 skills):                After (27 skills):
├─ T10.G4.01-05                   T10.G4.01-05 (unchanged)
├─ T10.G4.06 ──────────────────┬─> T10.G4.06.01 Smallest
│  (All statistics)            ├─> T10.G4.06.02 Largest
│                              ├─> T10.G4.06.03 Sum
│                              ├─> T10.G4.06.04 Average
│                              └─> T10.G4.06.05 Median
├─ T10.G4.07-10                   T10.G4.07-10 (unchanged)
├─ T10.G4.11 ──────────────────┬─> T10.G4.11.01 Copy list
│  (Copy & append)             └─> T10.G4.11.02 Append list
└─ T10.G4.12-20                   T10.G4.12-20 (unchanged)

GRADE 5: SPLIT 3 SKILLS (+7 total)
Before (18 skills):                After (21 skills):
├─ T10.G5.01-05                   T10.G5.01-05 (unchanged)
├─ T10.G5.06 ──────────────────┬─> T10.G5.06.01 Get row count
│  (Count & find)              └─> T10.G5.06.02 Find row by value
├─ T10.G5.07-08                   T10.G5.07-08 (unchanged)
├─ T10.G5.09 ──────────────────┬─> T10.G5.09.01 Delete one row
│  (All delete ops)            ├─> T10.G5.09.02 Delete matching rows
│                              └─> T10.G5.09.03 Clear all rows
├─ T10.G5.10                      T10.G5.10 (unchanged)
├─ T10.G5.11 ──────────────────┬─> T10.G5.11.01 Add column
│  (Manage columns)            ├─> T10.G5.11.02 Delete column
│                              └─> T10.G5.11.03 Delete all columns
└─ T10.G5.12-18                   T10.G5.12-18 (unchanged)

GRADES 6-8: NO CHANGES (30 skills remain unchanged)
├─ 6: 8 skills
├─ 7: 14 skills
└─ 8: 8 skills
```

---

## Skill Count by Grade

```
Grade  | Before | After | Change | Change %
-------|--------|-------|--------|----------
  K    |    8   |   8   |   0    |   0%
  1    |    6   |   6   |   0    |   0%
  2    |    7   |   7   |   0    |   0%
  3    |   10   |  12   |  +2    | +20%
  4    |   20   |  27   |  +7    | +35%
  5    |   18   |  21   |  +3    | +17%
  6    |    8   |   8   |   0    |   0%
  7    |   14   |  14   |   0    |   0%
  8    |    8   |   8   |   0    |   0%
-------|--------|-------|--------|----------
Total  |   96   | 112   | +16    | +17%
```

---

## Distribution of Changes

```
Splits by Type:
┌────────────────────────────┬───────┐
│ 2-way split (1 → 2)        │   5   │ (G3.01, G3.04, G4.11, G5.06, G5.11*)
│ 3-way split (1 → 3)        │   1   │ (G5.09)
│ 5-way split (1 → 5)        │   1   │ (G4.06)
└────────────────────────────┴───────┘
* G5.11 is a 3-way split

Most Common Pattern: 2-way split
Most Complex Split: T10.G4.06 (statistics, 1 → 5)
```

---

## Block Coverage

```
Standard Scratch List Blocks (9):
✓ add item to list
✓ delete (position) of list
✓ delete all of list
✓ insert item at position
✓ replace item at position
✓ item (position) of list
✓ item # of value in list
✓ length of list
✓ list contains item

CreatiCode List Extensions (17):
✓ change/reduce item by amount
✓ join list to text
✓ split text to list
✓ delete value from list
✓ reverse list
✓ reshuffle list
✓ sort list
✓ copy/append lists
✓ random number generation
✓ find item containing substring
✓ statistics (5 blocks)
✓ for-each loops (2 blocks)
✓ select multiple items

CreatiCode Table Blocks (33):
✓ Column operations (3)
✓ Row operations (8)
✓ Cell operations (3)
✓ Search operations (3)
✓ Aggregate operations (2)
✓ Data manipulation (6)
✓ Import/Export (4)
✓ Visualization (2)
✓ Google Sheets integration (2)
```

---

## Key Principles Applied

1. **One Skill = One Block**
   - Each skill now focuses on a single, specific block
   - Exceptions: closely related operations (e.g., increment/decrement)

2. **Progressive Complexity**
   - Simple operations (create, add) before complex ones (filter, aggregate)
   - Manual algorithms before automated blocks

3. **Clear Dependencies**
   - Sub-skills depend on parent or sibling sub-skills
   - X-2 rule maintained (grade X depends on X, X-1, or X-2)

4. **Consistent Naming**
   - Sub-skill IDs use format: T10.GX.YY.ZZ
   - Descriptions are action-oriented and specific

---

## Impact Highlights

### For Students
- ✓ Smaller learning steps = less overwhelming
- ✓ Clear success criteria for each operation
- ✓ Better understanding of when to use each block

### For Teachers
- ✓ Precise progress tracking (112 checkpoints vs 96)
- ✓ Can identify exactly which operation is challenging
- ✓ More granular assessment data

### For Curriculum
- ✓ Better alignment with actual CreatiCode blocks
- ✓ Improved scaffolding with smaller increments
- ✓ More opportunities for formative assessment

---

## Example: T10.G4.06 Split in Detail

### Before (1 skill covering 5 blocks)
```
T10.G4.06: Use built-in blocks to get list statistics
Description: Students use CreatiCode's aggregate blocks like
`[sum/average/smallest/largest/median] of list [list]`
to compute statistics on numeric lists.
```

### After (5 focused skills)
```
T10.G4.06.01: Find the smallest value in a list
  Block: [smallest v] of list [list]
  Focus: Understanding minimum value concept

T10.G4.06.02: Find the largest value in a list
  Block: [largest v] of list [list]
  Focus: Understanding maximum value concept

T10.G4.06.03: Calculate the sum of all values
  Block: [sum v] of list [list]
  Focus: Totaling for scores, money, etc.

T10.G4.06.04: Calculate the average
  Block: [average v] of list [list]
  Focus: Mean = sum ÷ count, typical value

T10.G4.06.05: Find the median value
  Block: [median v] of list [list]
  Focus: Middle value, resistant to outliers
```

**Result:** Students now learn each statistical concept separately,
understanding when and why to use each one, rather than learning
all five simultaneously.

---

End of Visual Summary
