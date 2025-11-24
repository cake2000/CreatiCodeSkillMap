# T27 Analysis - Executive Summary

## Overview
- **Total Skills**: 54 (K-8)
- **Issues Found**: 26 total (8 HIGH, 12 MEDIUM, 6 LOW)
- **New Skills Needed**: 8 (3 required, 5 optional)
- **Skills to Remove**: 1

## Critical Fixes Required (HIGH Priority)

### 1. Skill Ordering Violation
**Issue**: T27.G5.00b depends on T27.G5.01 but comes before it
**Fix**: Rename T27.G5.00b → T27.G5.01a

### 2. Circular Dependency
**Issue**: T27.G5.01b (GROUP BY) depends on T27.G4.04b (Sort), but GROUP BY is more fundamental
**Fix**: Remove T27.G4.04b from T27.G5.01b dependencies

### 3. Sorting Skills Missing/Misplaced
**Issue**: Sorting introduced in G4 but needed for median in G4. Too late in progression.
**Fix**:
- Add T27.G3.06 (Understand sorting concepts)
- Add T27.G3.07 (Sort tables with blocks)
- Remove T27.G4.04b (redundant)

### 4. Widget Skills Incomplete
**Issue**: T27.G3.00 teaches adding widgets but not reading/setting values
**Fix**:
- T27.G3.00: Add and position widgets
- T27.G3.00a: Set and read widget values (NEW)

### 5. Sub-skill Numbering Wrong
**Issue**: G4.02 sequence is b, c, e, d (should be b, c, d, e)
**Fix**: Renumber T27.G4.02e → T27.G4.02d, old T27.G4.02d → T27.G4.02e

### 6. Missing Table Manipulation Skill
**Issue**: Skills reference "copy rows to new table" but no skill teaches this
**Fix**: Add T27.G4.02f (Copy and manipulate table data)

## Quality Improvements (MEDIUM Priority)

### 1. Clarify Data Quality Skills
Split T27.G4.03 (identify issues) vs T27.G4.03b (implement fixes) more clearly

### 2. Split Complex Skill
T27.G7.02b teaches TWO things (extract column to list + moving averages)
**Fix**: Split into T27.G7.02b (convert table/list) + T27.G7.02c (moving averages)

### 3. Add Missing Blocks Fields
15+ skills reference specific blocks but don't list them in Blocks field

### 4. Standardize Terminology
Use "sum" consistently (not "totals")

### 5. Update Descriptions
- Google Sheets skill: explain CSV → cloud progression
- Pie charts: explicitly include in chart types skill
- AI skill: clarify first AI usage for data analysis

## Optional Enhancements (LOW Priority)

### 1. Add G8 Advanced Skills
- Regression analysis basics
- A/B testing statistical comparison
- Data ethics and bias detection

### 2. Add Storytelling Skill
T27.G7.05: Structure data narratives with story arcs

### 3. Add Critical Evaluation Skill
T27.G6.06: Identify misleading visualizations

## Skills That Work Well ✓

- K-2 appropriately unplugged (physical objects, pictures)
- G3+ properly use CreatiCode blocks
- X-2 rule compliance (after fixes)
- No forward references (after fixes)
- Good T26 integration (collection → analysis)
- Accurate CreatiCode feature mapping

## CreatiCode Feature Verification ✓

**Confirmed Available**:
- Widgets: add button, label, dropdown, slider, etc.
- Tables: create, add column, add row, show, sort, export, import
- Aggregations: sum, average, median, min, max
- Charts: bar, line, pie, percentage
- Advanced: pivot, GROUP BY, Google Sheets integration
- Moving averages: simple and exponential

**Correctly Noted as Missing**:
- Mode aggregation (no built-in block - skills correctly teach custom algorithm)
- Range filtering (exact match only - skills correctly teach loop-based workaround)

## Implementation Sequence

### Phase 1: Fix Ordering/Dependencies (Week 1)
1. Rename G5.00b → G5.01a
2. Remove circular dependency from G5.01b
3. Renumber G4.02d/e

### Phase 2: Add Missing Skills (Week 2)
4. Add G3.06, G3.07 (sorting)
5. Add G3.00a (widget values)
6. Add G4.02f (table copying)
7. Remove G4.04b (redundant)

### Phase 3: Quality Updates (Week 3)
8. Split G7.02b
9. Clarify G4.03/G4.03b
10. Add Blocks fields
11. Update descriptions

### Phase 4: Enhancements (Optional)
12. Add G6/G7/G8 optional skills
13. Consider CreatiCode feature requests

## Quick Stats

| Grade | Skills | Notes |
|-------|--------|-------|
| K | 3 | Unplugged sorting/comparing |
| G1 | 3 | Picture charts, storytelling |
| G2 | 4 | Bar/line charts, outliers |
| G3 | 9 → 11 | Intro coding (tables, widgets, basic stats) |
| G4 | 9 → 10 | Statistics, filtering, data quality |
| G5 | 8 | Dashboards, GROUP BY, correlation |
| G6 | 9 | Multi-table, complex filtering, pivot |
| G7 | 6 → 7 | Automation, Google Sheets, moving averages |
| G8 | 4 | Statistical reasoning, AI, publishing |

**Total**: 54 → 60 skills (after required additions)

## Bottom Line

**Current State**: T27 has strong content but critical ordering/dependency issues prevent correct implementation

**After Fixes**: T27 will be production-ready with proper scaffolding, accurate CreatiCode alignment, and logical progression

**Estimated Fix Time**: 2-3 weeks for all required changes

**Risk if Not Fixed**: Students will encounter:
- Skills before prerequisites (confusion)
- Missing foundational knowledge (gaps)
- Incorrect block references (frustration)

**Recommendation**: Implement Phase 1-2 (required fixes) immediately, Phase 3 (quality) within 1 month, Phase 4 (enhancements) as resources allow
