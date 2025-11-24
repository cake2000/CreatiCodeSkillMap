# T10 (Lists & Tables) - Quick Reference Guide

## Summary of Changes

**Total Skills:**
- Before: 96 skills
- After: 112 skills
- Net Change: +16 skills

**Skills Split:** 7 skills → 23 skills

---

## Skills That Were Split

### Grade 3 (2 splits = +2 skills)

| Old ID | New IDs | Description |
|--------|---------|-------------|
| T10.G3.01 | T10.G3.01.01, T10.G3.01.02 | Create list → (1) Create variable, (2) Add item |
| T10.G3.04 | T10.G3.04.01, T10.G3.04.02 | Remove item → (1) Delete at position, (2) Delete all |

### Grade 4 (2 splits = +7 skills)

| Old ID | New IDs | Description |
|--------|---------|-------------|
| T10.G4.06 | T10.G4.06.01-05 | Statistics → (1) Smallest, (2) Largest, (3) Sum, (4) Average, (5) Median |
| T10.G4.11 | T10.G4.11.01, T10.G4.11.02 | Copy/append → (1) Copy, (2) Append |

### Grade 5 (3 splits = +7 skills)

| Old ID | New IDs | Description |
|--------|---------|-------------|
| T10.G5.06 | T10.G5.06.01, T10.G5.06.02 | Row operations → (1) Get row count, (2) Find row by value |
| T10.G5.09 | T10.G5.09.01-03 | Delete rows → (1) Delete one, (2) Delete matching, (3) Delete all |
| T10.G5.11 | T10.G5.11.01-03 | Manage columns → (1) Add column, (2) Delete column, (3) Delete all columns |

---

## New Skill ID Mapping

Use this table to update references in other topics:

| Old ID | Maps to New ID | Notes |
|--------|----------------|-------|
| T10.G3.01 | T10.G3.01.02 | Most references mean "add to list" |
| T10.G3.04 | T10.G3.04.01 | Most references mean "delete at position" |
| T10.G4.06 | T10.G4.06.01 | Use .01 for general statistics references |
| T10.G4.11 | T10.G4.11.01 or .02 | Check context: copy vs append |
| T10.G5.06 | T10.G5.06.01 or .02 | .01 for counting, .02 for searching |
| T10.G5.09 | T10.G5.09.01 | Most references mean "delete one row" |
| T10.G5.11 | T10.G5.11.01 | Most references mean "add column" |

---

## Grade Distribution

| Grade | Skill Count | Major Changes |
|-------|-------------|---------------|
| K | 8 | None - all picture-based |
| 1 | 6 | None - all picture-based |
| 2 | 7 | None - bridge to coding |
| 3 | 12 | +2 (split create/add, split delete) |
| 4 | 27 | +7 (split statistics, split copy/append) |
| 5 | 21 | +7 (split row ops, delete, columns) |
| 6 | 8 | None |
| 7 | 14 | None |
| 8 | 8 | None |

---

## Key Blocks by Category

### Standard Scratch List Blocks
1. `add [item] to [list]` - T10.G3.01.02
2. `delete (position) of [list]` - T10.G3.04.01
3. `delete all of [list]` - T10.G3.04.02
4. `insert [item] at (position) of [list]` - T10.G4.03
5. `replace item (position) of [list] with [value]` - T10.G4.04
6. `item (position) of [list]` - T10.G3.02
7. `item # of [value] in [list]` - T10.G4.01
8. `length of [list]` - T10.G3.03
9. `[list] contains [item]?` - T10.G3.06

### CreatiCode List Extensions
10. `change item (position) of [list] by (N)` - T10.G3.09
11. `reduce item (position) of [list] by (N)` - T10.G3.09 (for young learners)
12. `join [list] into text with [separator]` - T10.G4.13
13. `set [list] to split of [text] with splitter [sep]` - T10.G4.12
14. `delete value [V] from [list]` - T10.G4.17
15. `reverse [list]` - T10.G4.14
16. `reshuffle [list] randomly` - T10.G4.15
17. `sort list [list] from [method]` - T10.G4.05
18. `copy [list1] to [list2]` - T10.G4.11.01
19. `append [list1] to [list2]` - T10.G4.11.02
20. `set [list] to (N) random whole numbers...` - T10.G4.16
21. `# of item containing [text] in [list]` - T10.G4.19
22. `[method] of list [list]` - T10.G4.06.01-05 (smallest/largest/sum/avg/median)
23. `for each item [var] in [list]` - T10.G3.05
24. `for each index [var] in [list]` - T10.G4.18
25. `insert (N) [selector] items from [list1] into [list2]` - T10.G4.20

### Table Blocks (Grade 5+)
26. `add column [name] at position (n) to table [table]` - T10.G5.11.01
27. `add to table [table]: [cell1] [cell2]...` - T10.G5.03
28. `item at row (n) column [name] of table [table]` - T10.G5.04
29. `replace item at row (n) column [name]... with [value]` - T10.G5.05
30. `change item at row (n) column [name]... by (amount)` - T10.G5.17
31. `row count of table [table]` - T10.G5.06.01
32. `row # of [value] in column [name] in table [table]` - T10.G5.06.02
33. `delete row (n) of table [table]` - T10.G5.09.01
34. `delete rows with column [name] of value [v]...` - T10.G5.09.02
35. `delete all rows from table [table]` - T10.G5.09.03
36. `sort table [table] by column [name] [order]` - T10.G6.01
37. `copy table [t1] into [t2]` - T10.G6.03
38. `append table [t1] to [t2]` - T10.G6.03

---

## Common Dependency Patterns

### Lists (Grade 3-4)
- Create list (T10.G3.01.01) → Add items (T10.G3.01.02) → Read/manipulate
- Loop basics (T07.G3.01) + Lists → for-each loops (T10.G3.05)
- Conditionals (T08.G3.01) + Lists → Contains checks (T10.G3.06)

### Tables (Grade 5+)
- Understand structure (T10.G5.01) → Create table (T10.G5.02) → Add data (T10.G5.03)
- Row operations build on list position concepts (T10.G3.02)
- Parallel lists (T10.G4.02) → Tables (T10.G5.01)

### Advanced Operations (Grade 6-8)
- Manual algorithms (G4-5) before automated blocks (G6-7)
- Sorting/filtering algorithms (G8) build on basic operations (G4-5)

---

## Implementation Checklist

### For Developers
- [ ] Verify all 59 documented blocks exist in CreatiCode
- [ ] Check blocks mentioned in G6 (set operations, unique items)
- [ ] Verify T10.G5.10 "get column as list" block exists
- [ ] Ensure block syntaxes match documentation exactly

### For Curriculum Writers
- [ ] Update all cross-references from other topics (T07, T08, T09)
- [ ] Create assessment items for 16 new sub-skills
- [ ] Update progression guides to reflect granular skills
- [ ] Review example projects to ensure they match new skill breakdown

### For Teachers
- [ ] Each sub-skill = one mini-lesson (15-20 min)
- [ ] Grade 3 now has 12 checkpoints instead of 10
- [ ] Grade 4 now has 27 checkpoints instead of 20
- [ ] Use sub-skill IDs for precise progress tracking

---

## Files Generated

1. **T10_COMPREHENSIVE_ANALYSIS.md** - Full analysis with rationale
2. **T10_UPDATED_SKILLS_COMPLETE.md** - Ready-to-use skill list
3. **T10_QUICK_REFERENCE.md** - This file

---

## Next Steps

1. Review and approve the skill decomposition
2. Update allskills.md with new skills
3. Update cross-topic dependencies
4. Create assessment materials for new skills
5. Update student-facing documentation
6. Train teachers on new skill granularity
