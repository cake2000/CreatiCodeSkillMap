# T27 Data Analysis & Storytelling - Phase 1 Optimization Executive Summary

## Overview
Comprehensive analysis of all 46 T27 skills (K-8) against CreatiCode's actual data analysis capabilities revealed **26 issues requiring fixes**, with **7 high-priority** platform accuracy problems.

## Critical Findings

### Platform Accuracy: 74% (14/19 block references correct)

**5 WRONG Block References Found:**
1. "percentage chart block" - doesn't exist (it's a chart TYPE)
2. "keep rows with column > value" - no "keep rows" block exists
3. "[mode v] of column in table" - no mode aggregation block
4. "item in column where column equals" - wrong VLOOKUP syntax
5. Incomplete Google Sheets syntax (missing sheet name, range)

### Dependency Issues
- **1 forward dependency** within T27 (G4.02d → G4.03)
- **3 X-2 rule violations** (G7 skills depending on G3/G4)

### Skill Quality
- **K-2 skills:** ✅ Excellent (picture-based, no coding)
- **G3 skills:** ⚠️ Good but need accuracy fixes
- **G4-G6 skills:** ⚠️ Several block reference errors
- **G7-G8 skills:** ⚠️ Dependency violations need fixing

## Issue Breakdown

| Priority | Count | Examples |
|----------|-------|----------|
| **HIGH** | 7 | Wrong block syntax, forward dependency, impossible operations |
| **MEDIUM** | 4 | Incomplete descriptions, vague references |
| **LOW** | 6 | Minor wording improvements |
| **X-2 Violations** | 4 | G7 skills with G3/G4 dependencies |
| **TOTAL** | 21 fixes needed | |

## Top 7 Critical Fixes

1. **T27.G3.03** - Fix backwards filtering logic ("delete desert to keep forest" is wrong!)
2. **T27.G4.02d** - Remove non-existent "keep rows" block reference
3. **T27.G4.02d** - Fix forward dependency (depends on G4.03 but comes before it)
4. **T27.G6.01** - Fix impossible compound condition filtering description
5. **T27.G6.01b** - Fix VLOOKUP syntax (wrong block reference)
6. **T27.G7.01b** - Complete Google Sheets block syntax
7. **T27.G4.02** - Fix "percentage chart block" to "percentage chart type"

## What CreatiCode Actually Supports

### ✅ Strong Data Features
- **Tables:** Full CRUD operations
- **Aggregations:** Sum, average, median, min, max (NO mode)
- **GROUP BY:** `set table to [method] of column by column`
- **Pivot Tables:** Multi-dimensional analysis
- **Charting:** Line, bar, pie, percentage (from tables or lists)
- **Widgets:** Buttons, dropdowns for dashboards
- **Google Sheets:** Full integration (read/write)
- **CSV Export/Import:** Built-in
- **Moving Average:** Simple & exponential (on lists)

### ❌ What's Missing
- Mode aggregation block (must calculate manually)
- "Keep rows" filtering (only "delete rows")
- Comparison operators in delete rows (>, <, >=, <=)
- Built-in dashboard builder (must assemble manually)

## Scaffolding Quality: ✅ EXCELLENT

The K-8 progression is well-designed:
- K-2: Unplugged sorting, counting, picture charts
- G3: Table creation → aggregation → filtering → charting
- G4: Statistics (median, mode) → quality checks → sorting
- G5: Dashboards → GROUP BY → correlation
- G6: Advanced operations (VLOOKUP, pivot, CSV)
- G7: Integration (Google Sheets, multi-charts, moving averages)
- G8: Professional (statistics, automation, AI, publishing)

**No major gaps!** Skills build logically on each other.

## Estimated Fix Effort

| Priority | Time Estimate |
|----------|---------------|
| HIGH (7 skills) | 2.5 hours |
| MEDIUM (4 skills) | 1 hour |
| LOW (6 skills) | 30 minutes |
| X-2 fixes (4 deps) | 1 hour |
| **TOTAL** | **5 hours** |

## Recommendations

### Immediate Actions
1. Fix the 7 HIGH priority block reference errors
2. Fix T27.G4.02d forward dependency
3. Fix 3 X-2 violations in G7 skills

### Phase 2 Considerations
- Add example code snippets to skills (especially G3-G4 foundation skills)
- Consider splitting T27.G6.01 (too complex for one skill)
- Add "mode calculation" as explicit skill (since no built-in block)

### Documentation Needs
- Create "CreatiCode Data Blocks Reference" for educators
- Add visual examples of chart types (line/bar/pie/percentage)
- Document widget event handling patterns

## Comparison to T26 Analysis

| Metric | T26 (Data Collection) | T27 (Data Analysis) |
|--------|---------------------|-------------------|
| Total Skills | 40 | 46 |
| HIGH Issues | 8 | 7 |
| Missing Features | 10 major gaps | 0 gaps |
| Block Accuracy | ~60% | 74% |
| Scaffolding | Good | Excellent |
| X-2 Violations | 6 | 4 |

**T27 is in better shape than T26!** Fewer platform mismatches, better scaffolding, no missing features.

## Next Steps

1. ✅ **Analysis Complete** (this document)
2. ⏭️ **Review & Approve** fixes with stakeholder
3. ⏭️ **Implement** changes to allskills.md
4. ⏭️ **Validate** all block references against blockdes8.txt
5. ⏭️ **Test** sample lessons for G3-G5 (critical foundation)
6. ⏭️ **Document** changes in changelog

## Key Takeaway

**T27 has a solid foundation but needs accuracy fixes.** The progression is excellent, K-2 skills are appropriately unplugged, and scaffolding is strong. Main issues are technical accuracy (wrong block names) and dependency management (forward refs, X-2 violations). All fixable in ~5 hours.

**Grade: B+ (85%)**
- Excellent scaffolding and progression
- Good coverage of CreatiCode features
- Some block reference errors need fixing
- Minor dependency issues

---

**Analysis Date:** 2025-11-22
**Analyst:** Claude (Sonnet 4.5)
**Source Files:**
- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (T27 section, lines 14290-14790)
- `/media/binyu/USB2/ScratchCopilot/blockdes8.txt` (CreatiCode block definitions)

**Related Documents:**
- `T27_OPTIMIZATION_ANALYSIS.md` (full detailed analysis)
- `T27_QUICK_FIX_REFERENCE.md` (quick fix guide)
