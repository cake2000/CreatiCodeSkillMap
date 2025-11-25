# T27 Analysis Quick Reference

## Critical Issues at a Glance

### 🔴 SEVERITY 1: Ordering Chaos
**39 of 54 skills** (72%) need renumbering due to illogical letter suffixes

**Examples:**
- G3.01b appears BEFORE G3.01 ❌
- G4.02 doesn't exist, but G4.02b, c, d, e do ❌
- G6.01c appears before G6.01b ❌

**Fix:** Systematic renumbering (see detailed map in main analysis)

---

### 🟠 SEVERITY 2: Circular Dependencies
**T27.G5.00b ↔ T27.G5.01** creates impossible prerequisite

- G5.00b (Widget events) depends on → G5.01 (Interactive dashboard)
- But G5.01 NEEDS widget events to work!

**Fix:** Reverse the dependency arrow

---

### 🟡 SEVERITY 3: Invalid References
**T26.G3.04** marked as [Unknown skill] but referenced by:
- T27.G4.03 (Check data quality)
- T27.G4.04 (Narrative captions)

**Fix:** Identify correct T26 skill or remove dependencies

---

### 🟢 SEVERITY 4: Block Reference Errors
**6 skills** use incorrect block terminology

| Skill | Wrong Term | Correct Term |
|-------|-----------|--------------|
| G3.01c | minimum/maximum | smallest/largest |
| G5.01b | set table to | set table to computed |
| G6.01b | row # of | row index with condition |

---

## Renumbering Summary

### Before → After Counts
- **Grade 3:** 8 skills → 8 skills (7 renumbered)
- **Grade 4:** 9 skills → 9 skills (8 renumbered)
- **Grade 5:** 7 skills → 7 skills (7 renumbered)
- **Grade 6:** 9 skills → 9 skills (8 renumbered)
- **Grade 7:** 7 skills → 7 skills (6 renumbered)
- **Grade 8:** 4 skills → 4 skills (0 renumbered)

**Total renumbering needed:** 39 skills

---

## Missing Skills (8 new skills recommended)

1. **G3.XX** - Verify table contents and structure
2. **G3.XX** - Create simple charts from lists
3. **G4.XX** - Delete specific table rows
4. **G4.XX** - Update table values and rows
5. **G4.XX** - Compute statistics from lists
6. **G5.XX** - Copy and backup tables
7. **G6.XX** - Combine AND/OR conditions in filters
8. **G7.XX** - Convert table columns to lists

---

## Overly Broad Skills (5 need splitting)

1. **T27.G3.01b** - Create/populate tables
   - Split into: Structure creation + Data population

2. **T27.G4.02d** - Filter rows by condition
   - Split into: Exact match + Range filtering

3. **T27.G5.01** - Interactive dashboard
   - Already partially split, needs dependency fixes

4. **T27.G6.02** - Compare two groups
   - Split into: Statistical comparison + Interpretation

5. **T27.G7.02b** - Moving averages
   - Split into: Table-to-list conversion + MA calculation

---

## Vague Descriptions (10 need clarification)

High Priority:
- **GK.01** - "Unplugged activity" too vague
- **G2.03** - "Look different" needs concrete criteria
- **G4.03** - Missing decision framework for data quality
- **G5.01** - "Simple" is subjective, needs specifics
- **G8.01** - "Simple statistical reasoning" without methods

Medium Priority:
- G1.01, G2.01, G3.02, G7.03

---

## Dependency Issues

### Excessive Dependencies (need simplification)
- **T27.G4.01** - 8 deps from 5 topics → reduce to 3
- **T27.G4.03** - 9 deps → reduce to 3
- **T27.G4.04** - 7 deps → reduce to 3

### Missing Intra-Topic Dependencies
- G3.04 should depend on G3.01 (statistics before charts)
- G4.04b should depend on G3.01b (tables before sorting)
- G5.02 should depend on G3.04 (chart skills)
- G6.02 should depend on G5.01b (GROUP BY)
- G7.01 should depend on T06.G5.01 (broadcasts)

---

## Work Estimates

| Phase | Tasks | Hours |
|-------|-------|-------|
| Phase 1: Critical Fixes | Renumbering, circular deps, invalid refs | 2-3 |
| Phase 2: Content | Split skills, add missing, clarify vague | 7-10 |
| Phase 3: Dependencies | Simplify excessive, add missing | 2-3 |
| **Total** | | **11-16** |

---

## Implementation Checklist

### Phase 1 (Do First) ✓
- [ ] Create automated renumbering script
- [ ] Renumber 39 skill IDs following appendix map
- [ ] Fix T27.G5.00b circular dependency
- [ ] Remove T26.G3.04 [Unknown skill] references
- [ ] Correct 6 block reference errors

### Phase 2 (Do Second) ✓
- [ ] Split 5 overly broad skills
- [ ] Write 8 new missing foundational skills
- [ ] Rewrite 10 vague descriptions with concrete examples
- [ ] Add implementation notes to all new/updated skills

### Phase 3 (Do Last) ✓
- [ ] Simplify excessive dependencies (G4.01, G4.03, G4.04)
- [ ] Add 5 missing intra-topic dependencies
- [ ] Verify X-2 rule compliance for all deps
- [ ] Run full validation suite

---

## Key Files

- **Full Analysis:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T27_COMPREHENSIVE_ANALYSIS.md`
- **This Quick Reference:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T27_ANALYSIS_NEW_QUICK_REF.md`
- **Current Skills:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (lines 24884-25530)

---

## Contact Points for Validation

Before implementing fixes, verify:
1. **Block syntax** - Check actual CreatiCode block names
2. **T26.G3.04** - What is this mystery skill?
3. **Median block** - Does built-in median exist in CreatiCode?
4. **Pivot syntax** - Confirm 'pivot table' block signature
5. **Google Sheets** - Verify read/write block syntax

---

Generated: 2025-11-25
Analyzer: Claude Sonnet 4.5
Scope: T27 skills (54 total)
Issues Found: 31 skills (57%)
