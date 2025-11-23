# T10 Phase 1 Optimization - Quick Reference Guide

**Generated:** 2025-11-22
**For:** Quick scanning of issues and recommendations
**Full Analysis:** See T10_PHASE1_OPTIMIZATION_ANALYSIS.md

---

## TLDR: What Needs to Be Fixed

### The Numbers
- **Current Skills:** 88 (K-8)
- **Block Coverage:** 54/75 blocks (72%)
- **Issues Found:** 51 total (31 HIGH, 12 MEDIUM, 8 LOW)
- **Recommended New Skills:** ~19 skills
- **Expected Final Coverage:** 75/75 blocks (100%)

### Top 5 Critical Issues

1. **MISSING:** 19 critical skills covering 21 blocks (list operations, table structure)
2. **WRONG SYNTAX:** T10.G5.02 references non-existent block (missing position parameter)
3. **TOO COMPLEX:** T10.G7.09 teaches 10 blocks at once (needs split)
4. **MISSING SCAFFOLDING:** No G3 skill for incrementing list items (essential for scores/counters)
5. **INCOMPLETE:** Many partial skill coverages (e.g., delete row but not "delete all rows")

---

## High Priority Issues - Must Fix

### Missing Critical Skills (19 new skills needed)

| Issue | Grade | What's Missing | Block(s) Affected | Impact |
|-------|-------|---------------|------------------|---------|
| A1 | G3 | Increment/decrement list item | data_changeitemoflist | Can't update scores, counters |
| A2 | G4 | Reverse list order | data_reverselist | Missing fundamental operation |
| A3 | G4 | Shuffle list randomly | data_reshuffle | No randomization for games |
| A4 | G4 | Generate random list | data_setrandomlist | No test data generation |
| A5 | G4 | Delete item by value | data_deletevalueoflist | Only can delete by position |
| A6 | G4 | Loop with index | data_for_each_index | Can't get position during loop |
| A7 | G4 | Find substring in list | data_itemnumoflist2 | Only exact matching |
| A8 | G4 | Select N items by criteria | data_insertitemsfromlist | No top-N or sampling |
| A9 | G5 | Add/delete columns properly | data_addcolatposition + 3 more | Wrong syntax in current skill |
| A10 | G5 | Insert/replace rows, get row | data_insertrowtotable + 2 more | Incomplete row operations |
| A11 | G5 | Find row by substring | data_rowindexwithcondition2 | Only exact matching |
| A12 | G5 | Increment/decrement cell | data_changeitematrowcolumn | Can't update cell values easily |
| A13 | G6 | Shuffle table rows | data_reshuffletable | No table randomization |
| A14 | G5-6 | Delete all rows/columns | 2 blocks | Missing bulk operations |
| A15 | G5-7 | Show/hide table monitors | 3 blocks | Missing display controls |
| A16 | G7 | Export table as CSV | data_exporttable | Can import but not export |
| A17 | G7 | Cloud save/load | 4 blocks | Missing data persistence |
| A18 | G7 | List sheets in spreadsheet | p2p_listSheetsInGoogleSheet | Incomplete Google Sheets |
| A19 | G7 | Chart with categories | widget_drawchartusingcategory | Limited chart types |

### Inaccurate Descriptions (2 fixes needed)

| Issue | Skill ID | Problem | Fix |
|-------|----------|---------|-----|
| B1 | T10.G5.02 | Says "add column [name] to table" but actual block requires position parameter | Change to "add column [name] at position (n) to table" |
| B2 | T10.G5.10 | References "make table from list" block - may not exist | Verify block or use alternative approach |

### Overly Complex Skills (2 splits needed)

| Issue | Skill ID | Problem | Fix |
|-------|----------|---------|-----|
| D1 | T10.G7.09 | Teaches 10 Google Sheets blocks at once | Split into: (1) read/write data, (2) manage structure |
| D2 | T10.G7.10 | Teaches NN and KNN together | Keep together but clearly distinguish the two approaches |

---

## Medium Priority Issues

### Scaffolding & Ordering

| Issue | Problem | Recommendation |
|-------|---------|---------------|
| H1 | Gap between G4 lists and G5 tables | Enhance T10.G5.01 description to explicitly connect tables to parallel lists |
| H2 | G7 introduces 10 diverse concepts at once | Reorder thematically: acquire → clean → transform → analyze → visualize |

### Unclear Descriptions

| Issue | Skill ID | Problem | Fix |
|-------|----------|---------|-----|
| G1 | T10.G8.07 | Hash table simulation lacks implementation details | Add specific hash function approach, collision handling method |
| G2 | T10.G7.01/03/05 & T10.G8.04/06 | Advanced skills lack concrete examples | Add example schemas, transformations, use cases |

---

## Low Priority Issues

### Terminology Consistency
- I1: Use "position" in G3-G5, introduce "index" in G6+ as technical synonym
- I2: Note whether blocks are "reporter" or "stack" blocks in complex skills

### Missing Examples
- J1: Add example themes to K-2 picture-based skills (animals, shapes, foods, etc.)

---

## Recommended Action Plan

### Phase 1A: Critical Fixes (Do First)
1. ✅ Fix T10.G5.02 incorrect block syntax
2. ✅ Verify T10.G5.10 "make table from list" block
3. ✅ Add T10.G3.09: Increment/decrement list item
4. ✅ Add 3 skills for column management (fix A9)
5. ✅ Add 3 skills for row operations (fix A10)

### Phase 1B: Complete List Skills (G3-G4)
6. ✅ Add T10.G4.14: Reverse list
7. ✅ Add T10.G4.15: Shuffle list
8. ✅ Add T10.G4.16: Generate random list
9. ✅ Add T10.G4.17: Delete by value
10. ✅ Add T10.G4.18: Loop with index
11. ✅ Add T10.G4.19: Find substring
12. ✅ Add T10.G4.20: Select N items by criteria

### Phase 1C: Complete Table Skills (G5-G6)
13. ✅ Add T10.G5.16: Find row by substring
14. ✅ Add T10.G5.17: Increment/decrement cell
15. ✅ Add T10.G5.18: Show/hide table monitors
16. ✅ Add T10.G6.08: Shuffle table rows
17. ✅ Expand T10.G5.09: Include delete all rows
18. ✅ Expand T10.G5.11: Include remove all columns

### Phase 1D: Advanced Features (G7)
19. ✅ Split T10.G7.09 into 2 skills (read/write + structure)
20. ✅ Add T10.G7.11: Formatted table snapshots
21. ✅ Add T10.G7.12: Export table as CSV
22. ✅ Add T10.G7.13: Cloud save/load
23. ✅ Expand T10.G7.09: Add list sheets block
24. ✅ Expand T10.G7.04: Add category charts

### Phase 1E: Polish & Enhancement
25. ✅ Enhance G8.07 with implementation details
26. ✅ Enhance G5.01 with list-to-table connection
27. ✅ Add examples to G7-G8 advanced skills
28. ⭕ Optional: Reorder G7 skills thematically
29. ⭕ Optional: Standardize terminology
30. ⭕ Optional: Add K-2 example themes

---

## Block Coverage Map

### Lists: 42 total blocks

**Covered (26/42 = 62%):**
- ✅ Basic CRUD: add, delete, delete all, insert, replace, item, length, contains
- ✅ Iteration: for each item
- ✅ Algorithms: find position, sort, filter
- ✅ Aggregation: sum, avg, min, max, median
- ✅ Text operations: split, join
- ✅ Set operations: union, intersect, minus, unique
- ✅ Advanced: copy, append

**Missing (16/42 = 38%):**
- ❌ Modification: change item by value, reduce item
- ❌ Operations: reverse, shuffle
- ❌ Generation: random list, random with seed
- ❌ Searching: delete by value, find substring, select N items
- ❌ Iteration: for each index
- ❌ Import/export: export variable, import variable

### Tables: 42 total blocks

**Covered (28/42 = 67%):**
- ✅ Basic CRUD: add row, get cell, replace cell, delete row, delete rows by condition
- ✅ Structure: row count, find row
- ✅ Aggregation: column sum/avg/min/max/median, group by
- ✅ Operations: sort, copy, append, pivot, lookup
- ✅ Import: import CSV file
- ✅ Google Sheets: read, write, manage sheets (8 blocks)
- ✅ Visualization: charts (2 blocks)
- ✅ AI/ML: train, predict (3 blocks)

**Missing (14/42 = 33%):**
- ❌ Structure: add column at position, insert row, replace row, get row
- ❌ Modification: change cell by value, reduce cell
- ❌ Columns: delete column, remove all columns, copy list to column
- ❌ Rows: delete all rows, find row by substring
- ❌ Operations: shuffle table
- ❌ Display: show/hide monitor, formatted snapshot
- ❌ Export: export CSV, cloud save/load (3 blocks)
- ❌ Google Sheets: list sheets
- ❌ Visualization: category charts

---

## Success Metrics

### Before Optimization:
- Skills: 88
- Blocks covered: 54/75 (72%)
- HIGH issues: 31
- MEDIUM issues: 12
- Inaccurate descriptions: 2
- Block coverage gaps: 21 blocks

### After Optimization (Target):
- Skills: ~107 (+19)
- Blocks covered: 75/75 (100%)
- HIGH issues: 0
- MEDIUM issues: 0
- Inaccurate descriptions: 0
- Block coverage gaps: 0

### Quality Gates (All must pass):
- ✅ All blocks have associated skills
- ✅ All skill descriptions match actual block syntax
- ✅ No X-2 dependency violations
- ✅ No overly complex skills (max 4 blocks/skill)
- ✅ Clear scaffolding progression
- ✅ All skills are assessable

---

## Quick Lookup: New Skill IDs

When adding new skills, use these IDs:

### G3 (currently 8 skills, add 1):
- T10.G3.09: Increment/decrement list item ← NEW

### G4 (currently 13 skills, add 7):
- T10.G4.14: Reverse list ← NEW
- T10.G4.15: Shuffle list ← NEW
- T10.G4.16: Generate random list ← NEW
- T10.G4.17: Delete by value ← NEW
- T10.G4.18: Loop with index ← NEW
- T10.G4.19: Find substring ← NEW
- T10.G4.20: Select N items by criteria ← NEW

### G5 (currently 10 skills, add 7):
- T10.G5.11: Manage table columns ← NEW (replaces incomplete G5.02)
- T10.G5.12: Copy list to column ← NEW
- T10.G5.13: Insert row at position ← NEW
- T10.G5.14: Replace entire row ← NEW
- T10.G5.15: Get row as list ← NEW
- T10.G5.16: Find row by substring ← NEW
- T10.G5.17: Increment/decrement cell ← NEW
- T10.G5.18: Show/hide table monitors ← NEW

### G6 (currently 7 skills, add 1):
- T10.G6.08: Shuffle table rows ← NEW

### G7 (currently 10 skills, renumber and add):
- T10.G7.09: Read/write Google Sheets ← SPLIT from old G7.09
- T10.G7.10: Manage Google Sheets structure ← SPLIT from old G7.09
- T10.G7.11: Display formatted table snapshots ← NEW
- T10.G7.12: Export table as CSV ← NEW
- T10.G7.13: Cloud save/load ← NEW
- T10.G7.14: Use AI to analyze table data ← RENUMBERED from old G7.10

### G8 (currently 8 skills, no additions needed):
- No new skills, just enhance G8.07 description

**Total New Skills: 19**
**New Skill Count: 88 + 19 = 107**

---

## Dependencies to Watch

When adding new skills, ensure dependencies follow X-2 rule:

### Cross-topic dependencies needed by new skills:
- T09.G3.01.02 (for T10.G3.09 - increment list item)
- T09.G4.02 (for T10.G4.19 - text contains operation)
- T08.G4.01 (for several G4 skills - if-else logic)

### Intra-topic dependencies for new skills:
- Most new G4 skills depend on G3 foundation
- New G5 table skills depend on G5.02-G5.04
- New G7 skills depend on earlier G5-G6 table skills

All dependencies have been checked - no violations expected.

---

**Use this guide for quick reference during implementation.**
**Refer to full analysis document for detailed recommendations and rationale.**

