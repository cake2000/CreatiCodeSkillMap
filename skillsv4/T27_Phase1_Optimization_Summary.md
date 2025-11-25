# T27 Data Analysis & Storytelling - Phase 1 Optimization Summary

## Overview

Topic T27 (Data Analysis & Storytelling) has been comprehensively optimized to address skill granularity, logical ordering, dependency issues, and accurate CreatiCode block references.

## Key Statistics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total Skills | 54 | 59 | +5 skills |
| GK Skills | 3 | 3 | No change |
| G1 Skills | 3 | 3 | No change |
| G2 Skills | 4 | 4 | No change |
| G3 Skills | 8 | 12 | +4 skills |
| G4 Skills | 9 | 11 | +2 skills |
| G5 Skills | 7 | 10 | +3 skills |
| G6 Skills | 9 | 11 | +2 skills |
| G7 Skills | 7 | 9 | +2 skills |
| G8 Skills | 4 | 4 | No change |

## Major Changes Made

### 1. Skill ID Renumbering (ALL grades affected)

**Problem:** Skills had inconsistent IDs with letter suffixes (G3.01b, G3.01c, G4.02b, etc.) making ordering confusing.

**Solution:** All skills now use sequential numeric IDs (G3.01, G3.02, G3.03, etc.)

### 2. Grade 3 Skills Expanded (8 → 12 skills)

The overly broad "Create and populate data tables" skill was broken down into focused, single-block skills:

| Old ID | New IDs | What Changed |
|--------|---------|--------------|
| T27.G3.01b | T27.G3.01 | Create a data table with columns |
| (merged) | T27.G3.02 | Add rows of data to a table |
| (new) | T27.G3.03 | Display tables on stage |
| (new) | T27.G3.04 | Read individual values from a table |
| (new) | T27.G3.05 | Count rows in a table |
| T27.G3.01 | T27.G3.06 | Compute sum of a column |
| (split) | T27.G3.07 | Compute average of a column |
| T27.G3.01c | T27.G3.08 | Find smallest and largest values |
| T27.G3.02 | T27.G3.09 | Build comparison statements with evidence |
| T27.G3.04 | T27.G3.10 | Draw a bar chart from table data |
| (new) | T27.G3.11 | Draw a line chart from table data |
| T27.G3.05 | T27.G3.12 | Choose appropriate chart types |

### 3. Grade 4 Skills Reorganized (9 → 11 skills)

| Old ID | New ID | Skill |
|--------|--------|-------|
| (new) | T27.G4.01 | Delete rows from a table by value |
| (new) | T27.G4.02 | Delete all rows from a table |
| T27.G4.02b | T27.G4.03 | Understand median concept |
| T27.G4.02c | T27.G4.04 | Calculate median using built-in blocks |
| T27.G4.02e | T27.G4.05 | Understand mode concept |
| T27.G4.04b | T27.G4.06 | Sort tables by a column |
| T27.G4.02d | T27.G4.07 | Filter rows by condition using loops |
| T27.G4.01 | T27.G4.08 | Analyze change over time using line graphs |
| T27.G4.03 | T27.G4.09 | Check data quality before analysis |
| T27.G4.03b | T27.G4.10 | Handle missing or invalid data |
| T27.G4.04 | T27.G4.11 | Create narrative captions for charts |

### 4. Grade 5 Skills Reorganized (7 → 10 skills)

| Old ID | New ID | Skill |
|--------|--------|-------|
| (new) | T27.G5.01 | Draw percentage charts from table data |
| (new) | T27.G5.02 | Draw pie charts using category/value columns |
| T27.G5.00 | T27.G5.03 | Calculate percentages from grouped data |
| T27.G5.01b | T27.G5.04 | Group data by category (GROUP BY) |
| T27.G3.00 | T27.G5.05 | Add basic widgets to display information (MOVED from G3) |
| T27.G5.00b | T27.G5.06 | Respond to widget click events |
| T27.G5.01 | T27.G5.07 | Build a simple interactive dashboard |
| T27.G5.02 | T27.G5.08 | Correlate two variables visually |
| T27.G5.03 | T27.G5.09 | Compare data from two sources |
| T27.G5.04 | T27.G5.10 | Present findings using slides or mini reports |

### 5. Grade 6 Skills Reorganized (9 → 11 skills)

| Old ID | New ID | Skill |
|--------|--------|-------|
| (new) | T27.G6.01 | Look up row index by value |
| T27.G6.01b | T27.G6.02 | Look up values across tables (VLOOKUP) |
| T27.G6.01 | T27.G6.03 | Filter tables using AND conditions |
| T27.G6.01c | T27.G6.04 | Filter tables using OR conditions |
| T27.G6.01d | T27.G6.05 | Combine data from two tables |
| T27.G6.02 | T27.G6.06 | Compare two groups using data |
| T27.G6.02b | T27.G6.07 | Create pivot tables |
| T27.G6.03 | T27.G6.08 | Identify trends in time-series data |
| T27.G6.03b | T27.G6.09 | Export tables to CSV files |
| (split) | T27.G6.10 | Import data from CSV files |
| T27.G6.04 | T27.G6.11 | Create structured summaries |

### 6. Grade 7 Skills Reorganized (7 → 9 skills)

| Old ID | New ID | Skill |
|--------|--------|-------|
| T27.G7.01b | T27.G7.01 | Read data from Google Sheets |
| (split) | T27.G7.02 | Write data to Google Sheets |
| T27.G7.01 | T27.G7.03 | Build multi-chart dashboards |
| (new) | T27.G7.04 | Extract table column to list for processing |
| T27.G7.02b | T27.G7.05 | Calculate moving averages |
| T27.G7.02 | T27.G7.06 | Compare predictions to actual outcomes |
| T27.G7.02c | T27.G7.07 | Automate chart updates with variables |
| T27.G7.03 | T27.G7.08 | Evaluate fairness metrics |
| T27.G7.04 | T27.G7.09 | Write findings reports for an audience |

### 7. Grade 8 Skills (4 skills, no change in count)

IDs remain T27.G8.01 through T27.G8.04 with cleaned up dependencies.

## Dependency Fixes

### Issues Fixed:

1. **Removed invalid references** - Eliminated references to unknown skill T26.G3.04
2. **Fixed circular dependency** - Resolved T27.G5.00b ↔ T27.G5.01 circular reference
3. **Simplified excessive dependencies** - Reduced G8 skills from 7-10 dependencies to 2-3 focused dependencies
4. **Corrected X-2 rule violations** - All dependencies now follow the X-2 rule (deps can only be at grade X, X-1, or X-2)
5. **Improved intra-topic flow** - Each skill now properly depends on prerequisite skills within T27
6. **Preserved cross-topic dependencies** - All valid dependencies to other topics maintained

### New Dependency Pattern:

- GK-G2: Simple linear progressions within topic
- G3: Table operations build sequentially (create → populate → display → read → count → aggregate → visualize)
- G4-G5: Statistics and interactivity branch from table foundations
- G6-G7: Advanced operations build on G4-G5 foundations
- G8: Capstone skills integrate all previous learning

## Block Reference Corrections

| Issue | Before | After |
|-------|--------|-------|
| Aggregation methods | [minimum v], [maximum v] | [smallest v], [largest v] |
| Sum/Average | Combined in one skill | Separate skills for each |
| Chart blocks | Generic references | Specific block syntax with parameters |
| Export/Import | Combined in one skill | Separate skills for export and import |

## Skill Quality Improvements

1. **More specific descriptions** - Each skill now describes exactly one block or concept
2. **Concrete examples** - Real scenarios added (e.g., "student names and test scores")
3. **Clear success criteria** - What students can do is explicit
4. **Grade-appropriate complexity** - K-2 unplugged, G3+ block-based with increasing complexity
5. **Scaffolded learning** - Each skill builds on previous skills in logical sequence

## Files Modified

- `skillsv4/allskills.md` - Main skill file updated with all T27 changes
- `skillsv4/allskills_backup_before_T27_optimization_*.md` - Backup created before changes

## Verification Checklist

- [x] All skills have unique sequential IDs
- [x] No letter suffixes in skill IDs
- [x] All skills have valid dependencies
- [x] No circular dependencies within T27
- [x] X-2 rule followed for all dependencies
- [x] Cross-topic dependencies preserved
- [x] Block references match CreatiCode actual blocks
- [x] K-2 skills are unplugged/picture-based
- [x] G3+ skills involve block-based coding
- [x] Each skill focuses on ONE concept/block
