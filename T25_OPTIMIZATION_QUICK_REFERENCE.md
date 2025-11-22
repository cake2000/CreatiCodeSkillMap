# T25 Optimization Plan - Quick Reference

**Date:** 2025-11-21

## Critical Issues Summary

### 🔴 HIGH PRIORITY (Must Fix Immediately)

1. **T25.G7.03 - JSON Reference** ⚠️ CRITICAL
   - **Problem:** References JSON, which CreatiCode does NOT support
   - **Fix:** Rewrite to use cloud storage serialization instead
   - **Impact:** Prevents teaching non-existent features

2. **T25.G3.04.01 - Non-Standard Numbering** 🔢
   - **Problem:** Has ".01" suffix which breaks numbering convention
   - **Fix:** Renumber to T25.G3.05
   - **Impact:** Maintains consistency

3. **Missing Table Operations** 📊
   - **Problem:** Tables mentioned but never taught how to use
   - **Fix:** Add 3 new skills (G5.06, G6.05, G7.05) for create/query/AI-vision tables
   - **Impact:** Teaches core CreatiCode feature

4. **Missing Cloud & Google Sheets** ☁️
   - **Problem:** Vague references without concrete implementation
   - **Fix:** Add 2 new skills (G6.06, G7.06) for cloud storage and Sheets integration
   - **Impact:** Covers unique CreatiCode persistence features

---

## Changes at a Glance

### Skills to Add (5 required + 2 optional):
- ✅ **T25.G5.06** - Create and populate tables
- ✅ **T25.G6.05** - Query and filter tables
- ✅ **T25.G6.06** - Cloud storage save/load
- ✅ **T25.G7.05** - Process AI vision table data
- ✅ **T25.G7.06** - Google Sheets integration
- 🔶 **T25.G7.07** - Regex validation (optional)
- 🔶 **T25.G8.05** - Data statistics (optional)

### Skills to Rewrite (1):
- 🔁 **T25.G7.03** - From JSON to cloud storage

### Skills to Renumber (1):
- 🔢 **T25.G3.04.01** → **T25.G3.05**

### Skills to Revise (5):
- ✏️ **T25.G3.04** - Strengthen description (more doing, less explaining)
- ✏️ **T25.G4.01** - Fix dependencies (use G3.02 instead of GK skills)
- ✏️ **T25.G5.01** - Remove premature table reference
- ✏️ **T25.G6.03** - Split into two skills (reduce complexity)
- ✏️ **T25.G8.01** - Add concrete guidance

---

## X-2 Rule Status

✅ **PASS** - No X-2 violations found within T25
- All dependencies properly grade-sequenced
- No skills depend on skills more than 2 grades prior (within T25)

---

## CreatiCode Platform Alignment

### ❌ Features Referenced but NOT in CreatiCode:
- **JSON parsing/formatting** (T25.G7.03) - MUST FIX

### ✅ Features in CreatiCode but NOT Covered:
- **Table operations** (create, add rows/columns, query cells)
- **Cloud storage** (persistent key-value data)
- **Google Sheets** (read/write external spreadsheet)
- **AI vision tables** (hand/pose landmark data in tables)
- **Regex** (optional - for validation)
- **Statistical functions** (optional - aggregations)

### ✅ Features Correctly Covered:
- Variables (text, number, Boolean)
- Lists (1D collections)
- General table concepts (but needs implementation)
- Data types and schema design
- Metadata documentation
- Nested structures (concepts)

---

## Implementation Phases

### Phase 1 (Week 1) - Critical Fixes:
1. Rewrite T25.G7.03 (JSON → cloud)
2. Renumber T25.G3.04.01 → T25.G3.05
3. Fix T25.G4.01 dependencies

### Phase 2 (Week 2) - Table & Cloud:
1. Add T25.G5.06 (create tables)
2. Add T25.G6.05 (query tables)
3. Add T25.G6.06 (cloud storage)
4. Revise T25.G5.01

### Phase 3 (Week 3) - Advanced:
1. Add T25.G7.05 (AI vision tables)
2. Add T25.G7.06 (Google Sheets)
3. Revise remaining skills

### Phase 4 (Week 4) - Polish:
1. Optional enhancements
2. Validation pass

---

## Key Statistics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total T25 Skills | 32 | 37-39 | +5 to +7 |
| Platform Errors | 1 | 0 | -1 ✅ |
| Numbering Issues | 1 | 0 | -1 ✅ |
| X-2 Violations | 0 | 0 | 0 ✅ |
| Missing Core Features | 5 | 0 | -5 ✅ |
| Vague Descriptions | 5 | 0 | -5 ✅ |

---

## Validation Checklist

After changes, verify:

- [ ] T25.G7.03 mentions cloud storage, NOT JSON
- [ ] No skill IDs have ".01" suffix at Grade 3
- [ ] Table creation taught before table usage
- [ ] Cloud storage has concrete implementation skill
- [ ] Google Sheets has concrete implementation skill
- [ ] All descriptions are assessable (not just "explain")
- [ ] Dependencies updated for renumbered G3.05
- [ ] No new X-2 violations introduced
- [ ] CSTA codes accurate for new skills

---

## Files Modified

1. `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/skills_T25_data_representation.md` - Source skill definitions
2. `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` - Integrated skill list
3. Any curriculum documents referencing T25.G3.04.01 (update to G3.05)

---

## Risk Mitigation

| Risk | Mitigation |
|------|------------|
| Breaking curricula | Test with sample projects |
| Renumbering confusion | Migration guide + update all refs |
| Over-complexity | Strong scaffolding in new skills |
| Missing blocks | Verify CreatiCode block availability |

---

## Success Criteria

✅ 100% platform accuracy (no unsupported features)
✅ Core data features explicitly covered (tables, cloud, sheets)
✅ All skill IDs follow standard convention
✅ Concrete, assessable descriptions
✅ No X-2 violations
✅ Grade-appropriate content

---

**For Details:** See `/media/binyu/USB2/dev/CreatiCodeSkillMap/T25_COMPREHENSIVE_OPTIMIZATION_PLAN.md`
