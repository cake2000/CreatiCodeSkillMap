# T28 Quick Fix Reference

**Date:** 2025-11-23
**Status:** Analysis Complete - Ready for Implementation

---

## AT A GLANCE

- **Current Skills:** 58 (G2-G8)
- **Proposed Total:** 64 (K-G8)
- **Skills to Add:** 9 (6 new K-G1, 3 from G3.05 split)
- **Skills to Merge:** 3 (G5.01.01-02, optionally G4.02 series)
- **Skills Needing Description Updates:** 5
- **Overall Quality:** B+ → A- after fixes

---

## CRITICAL FIXES NEEDED

### 🔴 FIX 1: Add K-G1 Foundation (6 new skills)

**Why:** Topic starts at G2 with no foundational progression

**New Skills:**
```
T28.K.01: Sort pictures by "always" or "sometimes"
T28.K.02: Predict what comes next in a pattern
T28.K.03: Experience randomness through picture games

T28.G1.01: Identify which events can or cannot happen
T28.G1.02: Record simple experiment results with pictures
T28.G1.03: Describe fairness in simple games
```

---

### 🔴 FIX 2: Verify G6.02 Random Seed Block

**Current Issue:** Skill describes generic seed behavior but block may be list-specific

**Action Required:**
1. Test `data_setrandomlistseed` block in CreatiCode
2. Verify if it affects:
   - ✅ List shuffling (`data_reshuffle`)
   - ❓ Pick random operations
   - ❓ All randomness

**If list-only:** Update skill description to:
```
T28.G6.02: Use random seeds for list reproducibility
Description: Students use the 'set random list seed to [value]' block
before shuffling a list, observe the resulting order, then reset the
seed to verify the list order is identical. They explain why reproducible
randomness matters for debugging and sharing results.
```

---

### 🔴 FIX 3: Break Down G3.05 (Too Broad)

**Current Skill:** Describe randomness in games and simulate a simple game element

**Problem:** Combines analysis + coding + writing in one skill

**Proposed Split:**
```
T28.G3.05a: Identify randomness in familiar games
→ Analysis only: Circle random elements, explain unpredictability

T28.G3.05b: Simulate a single game element
→ Coding only: Create virtual die/spinner, test 10 times

T28.G3.05c: Explain luck vs skill in games
→ Writing only: Compare games with high vs low randomness
```

---

### 🟡 FIX 4: Fix G5.08 Placement

**Problem:** G5.09 comes before G5.08; G5.08 doesn't fit T28 focus

**Current G5.08:** Track position and state for a single sprite

**Options:**
- Move to G6 as prerequisite for G6.05 (grid world agents)
- Move to T03 (Motion) or T05 (Modeling)
- Add randomness element to make it fit T28

**Recommended:** Move to G6.04a as foundation for agent modeling

---

### 🟡 FIX 5: Merge G5.01.01-02

**Current:**
- G5.01.01: Generate compound event data (two dice)
- G5.01.02: Analyze compound event distributions

**Problem:** Artificial split; Part 2 impossible without Part 1

**Proposed Merge:**
```
T28.G5.01: Generate and analyze compound event data (two dice)
Description: Students simulate rolling two dice 200 times, store sums
in a list, create frequency distribution and bar chart, and explain why
7 is most common by identifying all combinations (1+6, 2+5, 3+4, etc.).
```

---

## DESCRIPTION IMPROVEMENTS NEEDED

### Skill: T28.G4.03
**Issue:** "Stability differences" is vague
**Fix:** "Students run the same spinner twice (50 vs 500 trials), create bar charts showing percentages, and explain how 500-trial results are closer to expected equal percentages (less variable) than 50-trial results."

---

### Skill: T28.G5.02
**Issue:** "Function" terminology, unclear context
**Fix:** "Students simulate random group assignment by creating code that randomly assigns 100 participants to Group A or B using 'pick random 1 to 2'. They verify the split is approximately 50/50 and explain why random assignment makes fair comparisons."

---

### Skill: T28.G6.03
**Issue:** No guidance on what "acceptable error" means
**Fix:** "Students run simulation (100 coin flips), calculate percent error using formula: |observed% - expected%| / expected% × 100. They compare error to acceptable ranges (<10% good, >20% suggests bug) and explain why some error is normal."

---

### Skill: T28.G6.05
**Issue:** Missing connection to "Chance & Simulations" topic
**Fix Option 1:** Add randomness - "...They add random movement (50% forward, 25% left, 25% right) and observe random walk pattern over 20 steps."
**Fix Option 2:** Move to T05 (Modeling)

---

### Skill: T28.G7.06.01-02
**Issue:** Unclear distinction between setup and analysis
**Fix:** Update G7.06.01 to emphasize "setup and verification", G7.06.02 to emphasize "measurement and analysis"

---

## OPTIONAL IMPROVEMENTS

### Optional 1: Merge G4.02.01-03
**Current:** Three sequential skills (log → count → calculate %)
**Consider:** Merge into single "Collect, count, and analyze simulation data" skill
**Decision:** Keep separate for scaffolding (acceptable either way)

### Optional 2: Add List Shuffle Skill at G4
**Block exists:** `data_reshuffle` - Reshuffle list randomly
**Currently:** Not explicitly taught
**Proposed:** Add T28.G4.08 to teach list shuffling after T10 list skills

### Optional 3: Strengthen T27 Dependencies
**Add explicit chart dependencies:**
- Any skill creating bar charts → depend on T27 bar chart skill
- Any skill computing median/mode → depend on T27 statistics skills

---

## CREATICODE BLOCK VERIFICATION

### ✅ Verified Accurate
- `pick random` (basic randomness)
- Chart types: line, bar, pie, percentage
- Chart sources: list, columns, categories
- List operations: append, length, remove
- Statistical functions: sum, average, median, mode
- List shuffle: `data_reshuffle`
- Table shuffle: `data_reshuffletable`

### ⚠️ Needs Verification
- `data_setrandomlistseed` - Scope unclear (list-only vs all randomness?)

---

## GRADE APPROPRIATENESS SUMMARY

| Grade | Status | Notes |
|-------|--------|-------|
| K | ❌ Missing | Add 3 picture-based skills |
| G1 | ❌ Missing | Add 3 unplugged/visual skills |
| G2 | ✅ Good | Physical experiments acceptable for probability |
| G3 | ✅ Good | Need to break down G3.05 |
| G4 | ✅ Good | Appropriate complexity increase |
| G5 | ✅ Good | Fix numbering (G5.08/09), merge G5.01 |
| G6 | ⚠️ Good | Verify seed block functionality |
| G7 | ✅ Excellent | Outstanding AI/ethics integration |
| G8 | ✅ Excellent | Sophisticated capstone content |

---

## SKILL COUNT CHANGES

**Current Distribution:**
```
K:  0 skills
G1: 0 skills
G2: 4 skills
G3: 7 skills
G4: 8 skills
G5: 11 skills
G6: 12 skills
G7: 7 skills
G8: 6 skills
─────────────
Total: 58 skills
```

**After Proposed Changes:**
```
K:  3 skills (+3 new)
G1: 3 skills (+3 new)
G2: 4 skills (no change)
G3: 9 skills (+3 from G3.05 split, -1 original)
G4: 8 skills (no change, or 6 if G4.02 merged)
G5: 10 skills (-1 from G5.01 merger)
G6: 12 skills (no change, or 13 if G5.08 moved here)
G7: 7 skills (no change)
G8: 6 skills (no change)
─────────────────────────────
Total: 64 skills (or 62-65 depending on optional mergers)
```

---

## IMPLEMENTATION PRIORITY

### Phase 1: Critical (Must Do)
1. Add 6 K-G1 skills
2. Verify G6.02 seed block, update description
3. Break G3.05 into 3 parts
4. Fix G5.08 placement
5. Merge G5.01.01-02

**Timeline:** 2-3 hours

---

### Phase 2: Important (Should Do)
6. Update 5 skill descriptions (G4.03, G5.02, G6.03, G6.05, G7.06 pair)
7. Review all G6+ dependencies for clarity
8. Add explicit T27 chart dependencies

**Timeline:** 1-2 hours

---

### Phase 3: Nice to Have (Consider)
9. Decide on G4.02 merger (keep or merge)
10. Add list shuffle skill at G4
11. Standardize action verbs across all skills
12. Add more real-world contexts to G4-G5 skills

**Timeline:** 1 hour

---

## QUALITY METRICS

**Before Fixes:**
- Missing foundational skills: ❌
- CreatiCode accuracy: ⚠️
- Overly broad skills: ❌
- Description clarity: ⚠️
- Grade appropriateness: ✅
- AI/ethics integration: ✅
**Overall: B+**

**After Fixes:**
- Missing foundational skills: ✅
- CreatiCode accuracy: ✅
- Overly broad skills: ✅
- Description clarity: ✅
- Grade appropriateness: ✅
- AI/ethics integration: ✅
**Overall: A-**

---

## STRENGTHS TO PRESERVE

✅ Excellent pedagogical progression (hands-on → coding → theory)
✅ Strong computational thinking integration
✅ Outstanding G7-G8 AI/ethics content (fairness, bias, model cards, policy briefs)
✅ Good balance of experimental and theoretical probability
✅ Sophisticated use of simulations for real-world modeling
✅ Clear connections to data analysis (T27) and visualization

---

## FINAL RECOMMENDATION

**Implement Phase 1 fixes immediately:**
- Fills critical K-G1 gap
- Ensures CreatiCode accuracy
- Improves skill assessability

**Result:** Transforms T28 from "very good" to "excellent" with relatively minor effort.

---

**See full analysis:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T28_COMPREHENSIVE_ANALYSIS_REPORT.md`
