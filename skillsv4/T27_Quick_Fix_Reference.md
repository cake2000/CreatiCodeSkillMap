# T27 Phase 1 - Quick Fix Reference

**Quick lookup for issues requiring immediate action**

---

## CRITICAL FIXES (Do First)

### 1. Split Over-Broad Skills

| Skill ID | Current Title | Action | New Structure |
|----------|---------------|--------|---------------|
| T27.G3.01 | Compute totals and averages | SPLIT into 2 skills | → T27.G3.01a (sum/count) + T27.G3.01c (avg/min/max) |
| T27.G4.02c | Calculate median and mode | SPLIT into 2 skills | → Keep for median only + NEW T27.G5.03b (mode) |
| T27.G5.01 | Interactive dashboard | SIMPLIFY | → Requires NEW T27.G4.05 (widgets first) |
| T27.G7.01 | Multi-chart linked dashboards | ADD PREREQUISITE | → Requires NEW T27.G6.05 (multi-chart without links) |

### 2. Fix Dependency Violations

| Skill ID | Problem | Fix |
|----------|---------|-----|
| T27.G4.02 | Depends on T27.G4.02b (backward dependency) | REMOVE T27.G4.02b dependency |
| T27.G4.04b | Misplaced in sequence | RENUMBER to T27.G4.03b |

### 3. Fix Duplicate Content

| Skills | Problem | Fix |
|--------|---------|-----|
| T27.G3.03 + T27.G4.02d | Both teach filtering | REWRITE T27.G3.03 to focus on counting only |

---

## SKILLS TO ADD (7 New Skills)

1. **T27.G3.01a** - Use sum and count aggregations
2. **T27.G3.05** - Recognize complete vs. incomplete data
3. **T27.G4.05** - Create basic UI widgets
4. **T27.G4.06** - Choose appropriate chart types
5. **T27.G5.03b** - Calculate mode by counting frequencies (moved from G4)
6. **T27.G5.05** - Extract table columns into lists
7. **T27.G6.05** - Create dashboard with multiple independent charts

---

## SKILLS TO MOVE

| Skill | Current Grade | Move To | Reason |
|-------|---------------|---------|--------|
| T27.G4.02 (Percentages) | Grade 4 | Grade 5 | Too advanced for G4 math level |

---

## SKILLS REQUIRING REWRITE

| Skill ID | Issue | Priority |
|----------|-------|----------|
| T27.G3.02 | Unclear title | MEDIUM - Rename to "Display comparison results with computed evidence" |
| T27.G3.03 | Contains filtering (duplicate) | HIGH - Rewrite to focus on counting only |
| T27.G6.01 | Too implementation-specific | HIGH - Rewrite to emphasize compound logic concept |
| T27.G5.04 | Mixes external/internal tools | MEDIUM - Focus on CreatiCode only |
| T27.G6.04 | Drifts to AI topic | MEDIUM - De-emphasize AI, focus on structured reporting |
| T27.G7.03 | Vague metrics | MEDIUM - Add concrete formulas and thresholds |

---

## SKILLS REQUIRING RENAME

| Skill ID | Current Title | New Title |
|----------|---------------|-----------|
| T27.G2.03 | Identify outliers visually | Find the value that doesn't fit the pattern |
| T27.G3.02 | Build comparison statements | Display comparison results with computed evidence |
| T27.G3.01 | Compute totals and averages | (becomes T27.G3.01c) Use min/max/average aggregations |
| T27.G4.04b | Sort tables to organize data | (becomes T27.G4.03b) Sort tables to organize data |

---

## DEPENDENCIES TO FIX

### Remove These Dependencies:
- T27.G4.02: Remove dependency on T27.G4.02b
- T27.G4.01: Remove dependency on T27.G3.04
- T27.G4.04: Remove dependency on T27.G4.01

### Add These Dependencies:
- T27.G4.02b: Add dependency on T27.G4.03b (sorting - for median)
- T27.G5.01: Add dependency on T27.G4.05 (widget creation)
- T27.G7.01: Add dependency on T27.G6.05 (multi-chart foundation)

---

## CREATICODE BLOCKS TO VERIFY (Priority Order)

### CRITICAL (Must verify immediately):
1. ✓ Table operations: `add column`, `add to table`, `show table`, `row count`
2. ✓ Aggregations: `[sum v]`, `[average v]`, `[median v]`, `[minimum v]`, `[maximum v]`
3. ✓ Charts: `draw [bar/line/pie/percentage v] chart`

### HIGH (Verify before finalizing G5+):
4. ⚠ Widgets: `add button`, `add dropdown menu`, `when widget clicked/changes`
5. ⚠ GROUP BY: `set table [summary v] to [average v] of column [...] by column [...]`
6. ⚠ Sorting: `sort table [data v] by column [score] [large to small v]`

### MEDIUM (Verify for advanced skills):
7. ⚠ Pivot: `pivot [data v] into [summary v] row groups [...] columns [...] methods [...]`
8. ⚠ Moving average: `value from [simple v] moving average window [7] of list [...]`
9. ⚠ Google Sheets: `read from google sheet` / `write into google sheet`

---

## GRADE-BY-GRADE SUMMARY

| Grade | Total Skills | Status | Issues | Priority Actions |
|-------|--------------|--------|--------|------------------|
| K | 3 | ✓ STRONG | 0 | None - keep as-is |
| 1 | 3 | ✓ STRONG | 0 | None - keep as-is |
| 2 | 4 | ⚠ MINOR | 1 | Fix M8.1 (outlier terminology) |
| 3 | 5 → 6 | ⚠ FIXES | 3 | Split G3.01, rewrite G3.03, add G3.05 |
| 4 | 8 → 10 | ⚠ MAJOR | 6 | Split G4.02c, move G4.02 to G5, add G4.05 & G4.06 |
| 5 | 4 → 7 | ⚠ ADDS | 3 | Add G5.03b, G5.05, G5.06 (from G4) |
| 6 | 6 → 7 | ⚠ VERIFY | 4 | Rewrite G6.01, add G6.05, verify blocks |
| 7 | 7 | ⚠ BLOCKS | 2 | Verify Google Sheets, moving average blocks |
| 8 | 4 | ✓ STRONG | 0 | Dependent on earlier fixes |

---

## BEFORE/AFTER SKILL COUNTS

| Grade | Current Count | After Phase 1 | Change |
|-------|---------------|---------------|--------|
| K | 3 | 3 | 0 |
| 1 | 3 | 3 | 0 |
| 2 | 4 | 4 | 0 |
| 3 | 4 | 6 | +2 (split G3.01, add G3.05) |
| 4 | 8 | 9 | +1 (split G4.02c, add 2, move 1 out) |
| 5 | 4 | 7 | +3 (add 2 new, receive 1 from G4) |
| 6 | 6 | 7 | +1 (add G6.05) |
| 7 | 7 | 7 | 0 |
| 8 | 4 | 4 | 0 |
| **Total** | **43** | **50** | **+7** |

---

## IMPLEMENTATION PRIORITY ORDER

1. **First:** Verify all CreatiCode blocks (foundation for everything)
2. **Second:** Fix dependency violations (H5.1, H5.2) - affects numbering
3. **Third:** Split over-broad skills (H1.1, H1.2) - core fixes
4. **Fourth:** Add missing foundation skills (H3.1, H3.2, H3.3)
5. **Fifth:** Fix duplicates and rewrites (H2.1, H1.3, H1.4, H1.5)
6. **Sixth:** Update descriptions and terminology (M7.x, M8.x)
7. **Seventh:** Clean up dependencies (M9.x)

---

## NOTES FOR PHASE 2 (Optional Improvements)

- Consider adding example projects for complex skills (dashboards, GROUP BY)
- Create visual progression map showing K-8 data analysis journey
- Develop assessment rubrics for open-ended skills (fairness evaluation, report writing)
- Add connection to Common Core Math standards (particularly statistics in G6-8)
- Consider integration with science data collection activities
- Explore real-world datasets appropriate for each grade level

---

**END OF QUICK REFERENCE**
