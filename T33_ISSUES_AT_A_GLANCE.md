# T33 Connected Services - Issues At A Glance
**Date:** 2025-11-25

## Quick Stats
- **Total Issues:** 32
- **Skills Affected:** 20 out of 36 (56%)
- **Skills Needing Splits:** 5 → 15 (net +10 skills)
- **Final Skill Count:** 36 → 45 (+9 skills, with 1 move)

---

## PRIORITY 1: CRITICAL SPLITS (Must Fix)

### Too Broad - Need Splitting

| Current Skill | Problem | Split Into | Block Count |
|---------------|---------|------------|-------------|
| **T33.G6.01** | ALL 15 Cloud blocks | Keep as meta-skill, clarify as SURVEY only | 0 (meta) |
| **T33.G6.10** | Insert + Fetch together | → G6.10a (fetch), G6.10b (insert) | 2 |
| **T33.G7.01** | List + Add + Remove + Clear | → G7.01a (list), G7.01b (add), G7.01c (remove) | 3 |
| **T33.G7.11** | Update + Update-in-place + Delete | → G7.11a (table), G7.11b (in-place), G7.11c (delete) | 3 |
| **T33.G7.12** | AND/OR/NOT + LIMIT + SORT | → G7.12a (logic), G7.12b (modifiers) | 3 + params |

**Total:** 5 skills → 12 skills (+7 net)

---

## PRIORITY 2: MISSING COVERAGE

| Block | Type | Currently | Should Be |
|-------|------|-----------|-----------|
| `database_collection` | Reporter | Implicit in G6.10 | **NEW: T33.G6.09b** |
| `database_collectionfield` | Reporter | Implicit in G7.10 | **NEW: T33.G6.09b** |

**Total:** +1 new skill

---

## PRIORITY 3: CRITICAL CLARITY ISSUES

### Issue #33: T33.G7.05 - Cloud Sessions Misleading (CRITICAL!)
**Problem:** Description says "multiplayer experiences" and "collaborative tools"
**Reality:** ONLY syncs cloud variables (NOT sprites, physics, game state)
**Risk:** Students confuse with T19 Multiplayer blocks
**Fix:** Complete rewrite emphasizing variables-only scope

### Issue #25: T33.G5.02 - Generic "Collaboration" Title
**Problem:** Doesn't specify cloud VARIABLES vs full multiplayer
**Fix:** Rename to "Distinguish real-time variable sync from one-time requests"

### Issue #19: T33.G6.08 - Privacy Taught Too Late
**Problem:** Placed AFTER students already use Google Sheets (G6.03, G6.04)
**Fix:** MOVE to **G5.04** (before any data sharing)

---

## PRIORITY 4: DEPENDENCY FIXES

| Skill | Current Issue | Fix Required |
|-------|--------------|--------------|
| T33.G6.10 | Missing table ops | Add T10.G6.01 |
| T33.G7.01 | Mentions "clear" (dup of G6.05) | Remove from description |
| T33.G7.04 | Depends on G6.03 (sheets ≠ drive) | Remove G6.03 |
| T33.G8.06 | Missing DB skills for capstone | Add G7.11a, G7.12a |
| G6.03, G6.04 | Should depend on privacy | Add new G5.04 |

**Total:** 5 skills need dependency updates

---

## PRIORITY 5: DESCRIPTION IMPROVEMENTS

### Needs More Concrete Content
- **T33.G6.02:** Add result processing (display/parse/extract)
- **T33.G7.02:** Add tradeoff analysis (cell ops vs bulk)
- **T33.G7.04:** Clarify read-only access
- **T33.G7.08:** Add decision framework (when to use which service)
- **T33.G8.02:** Add concrete ToS checklist
- **T33.G8.04:** Add specific validation examples
- **T33.G8.05:** Add measurement metrics

### Needs Simplification
- **T33.G7.09:** Remove timestamp/expiration complexity
- **T33.G8.03:** Simplify from "outage simulator" to "offline testing"

### Needs Clarification
- **T33.G6.05:** Remove premature delete comparison
- **T33.G7.06:** Differentiate from G6.08 (or remove)

**Total:** 12 skills need description updates

---

## GRADE DISTRIBUTION CHANGES

### Before:
- G5: 3 skills
- G6: 10 skills
- G7: 12 skills
- G8: 6 skills

### After:
- G5: 4 skills (+1 moved privacy)
- G6: 12 skills (+2 split + new)
- G7: 18 skills (+6 splits)
- G8: 6 skills (enhanced descriptions)

---

## BLOCK COVERAGE SUMMARY

### Current:
- 28 blocks available
- 26 explicitly covered (93%)
- 2 implicitly covered (reporters)

### After Fixes:
- 28 blocks available
- **28 explicitly covered (100%)** ✅
- Better scaffolding through splits
- Clear progression within categories

---

## ACTION SEQUENCE

1. **Week 1:** Split 5 broad skills → 12 skills
2. **Week 2:** Add T33.G6.09b, move G6.08→G5.04
3. **Week 3:** Fix 5 dependency issues
4. **Week 4:** Update 12 skill descriptions
5. **Week 5:** Validate and test progression

---

## FILES REFERENCE

- **Full Analysis:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T33_Phase1_Comprehensive_Issues.md`
- **Block Mapping:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T33_BLOCK_COVERAGE_MAP.md`
- **Current Skills:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (lines 28913-29350)

---

## KEY TAKEAWAYS

✅ **Good:**
- Most blocks covered (93%)
- Solid conceptual foundation (GK-G5)
- Good error handling and privacy concepts

⚠️ **Issues:**
- Several skills too broad (5 need splitting)
- Critical confusion: cloud sessions vs multiplayer
- Privacy taught after data sharing starts
- Missing explicit coverage for 2 helper blocks

🎯 **Impact After Fixes:**
- 100% block coverage
- Better scaffolding (5→12 splits)
- Clear cloud variables ≠ multiplayer distinction
- Privacy before practice
- More concrete, age-appropriate descriptions

