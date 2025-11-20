# G5 Fix Plan - Quick Summary

## Files Generated

1. **G5_FIX_PLAN.md** (1,335 lines)
   - Comprehensive fix plan for all 28 affected G5 skills
   - Detailed specifications for each fix
   - Implementation guide with 4-week timeline
   - Validation checklists
   - Replacement mapping tables
   - Ready for immediate implementation

2. **G5_FIX_PLAN.json**
   - Machine-readable version of all fixes
   - Complete data structure for programmatic implementation
   - Includes current/proposed dependencies, rationale, validation flags

3. **generate_g5_fix_plan.py**
   - Python script that generated both files above
   - Can be modified and re-run if needed
   - Parses all 1,204 skills from allskills.md

## What Was Done

### Analysis
- Read and parsed complete allskills.md file (1,204 skills)
- Analyzed all 28 affected G5 skills identified in analysis reports
- Found G3/G4 replacement skills for each problematic G1/G2 dependency
- Identified transitive dependencies to remove
- Validated all proposed fixes

### Fix Plan Generation
Created comprehensive fixes for:
- **38 HIGH priority issues** - Invalid grade dependencies (G1/G2)
- **25 MEDIUM priority issues** - Transitive dependencies
- **1 MEDIUM priority issue** - Same-grade dependency

### Key Statistics
- **Total skills to fix:** 28 (out of 172 G5 skills)
- **Dependencies to remove:** 52
- **Dependencies to add:** 26
- **Net change:** -26 dependencies (cleaner graph)
- **Skills needing manual review:** 1 (T31.G5.02)

## Fix Breakdown by Topic

| Topic | Skills | Issue | Fix Strategy |
|-------|--------|-------|--------------|
| T03 | 3 | All depend on T03.G1.02 | Replace with T03.G3.01 |
| T05 | 6 | Mix of G1/G2 deps + transitives | Replace with T05.G3.01, clean transitives |
| T12 | 1 | Depends on T12.G1.01 | Replace with T12.G3.01 |
| T13 | 1 | Depends on T13.G1.01 | Replace with T13.G4.01 |
| T25 | 3 | G1 deps + transitives | Replace with T25.G3.01, clean transitives |
| T30 | 4 | Multiple G1 deps + transitives | Replace with T30.G3.01, clean transitives |
| T31 | 1 | Same-grade dependency | Remove T31.G5.01 |
| T32 | 3 | Double G1 deps + transitives | Replace with T32.G3.01 |
| T34 | 2 | Double G1 deps + transitives | Replace with T34.G3.01 |
| T35 | 3 | G1 deps + cross-topic G2 | Replace with T35.G3.01, T04.G3.01 |
| T36 | 1 | Double G1 deps + transitives | Replace with T36.G3.01 |

## Implementation Ready

The fix plan is **ready for immediate implementation**:

1. **All fixes specified** - Every skill has detailed before/after dependencies
2. **Rationale provided** - Each change includes explanation
3. **Validated** - All proposed dependencies use only G3/G4/G5/GK
4. **No missing skills** - All G3/G4 replacements exist in allskills.md
5. **Pedagogically sound** - Replacements are same-topic when possible

## Next Steps

### Option 1: Manual Implementation
1. Open G5_FIX_PLAN.md
2. Follow the detailed specifications for each skill
3. Update dependencies in allskills.md
4. Use the validation checklist to verify changes

### Option 2: Automated Implementation
1. Use G5_FIX_PLAN.json for programmatic updates
2. Write script to apply changes to allskills.md
3. Run validation checks automatically
4. Review and commit changes

### Option 3: Phased Implementation
Follow the 4-week implementation guide in G5_FIX_PLAN.md:
- **Week 1:** Simple fixes (4 skills)
- **Week 2:** Single-topic replacements (15 skills)
- **Week 3:** Complex fixes (9 skills)
- **Week 4:** T05 topic + validation (6 skills)

## Risk Assessment

- **Low risk:** 17 skills (simple 1:1 replacements)
- **Medium risk:** 9 skills (multiple changes)
- **High risk:** 2 skills (cross-topic dependencies)
  - T05.G5.05 (T04.G2.01 → T04.G3.01)
  - T35.G5.03 (T04.G2.01 → T04.G3.01)

## Manual Review Required

Only **1 skill** needs manual review:
- **T31.G5.02** - Removing same-grade dependency T31.G5.01
  - Not a technical issue, just verify pedagogically appropriate

## Validation

After implementation, run:
```bash
python3 analyze_g5_comprehensive.py
```

Expected result: **0 issues** (down from 64)

## Most Common Replacements

The fix plan uses these replacements most frequently:

1. **T05.G1.02 → T05.G3.01** (4 times)
2. **T03.G1.02 → T03.G3.01** (3 times)
3. **T25.G1.01 → T25.G3.01** (3 times)
4. **T30.G1.01/G1.02 → T30.G3.01** (3 times)
5. **T32.G1.01/G1.02 → T32.G3.01** (3 times)
6. **T35.G1.01/G1.02 → T35.G3.01** (3 times)

Pattern: Most G1/G2 skills have direct G3 equivalents in same topic.

## Files to Reference

- **Start here:** G5_FIX_PLAN.md (main document)
- **For automation:** G5_FIX_PLAN.json (structured data)
- **For context:** G5_ANALYSIS_EXECUTIVE_SUMMARY.md (original analysis)
- **For details:** G5_COMPREHENSIVE_ANALYSIS_REPORT.txt (all 64 issues)

---

**Generated:** 2025-11-20
**Status:** Ready for implementation
**Confidence:** High (all replacements validated to exist)
