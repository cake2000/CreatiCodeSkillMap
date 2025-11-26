# T10 Lists & Tables - Analysis Executive Summary

**Date:** 2025-11-26
**Current Skills:** 115 (K=8, 1=6, 2=7, 3=12, 4=27, 5=23, 6=8, 7=14, 8=10)
**Status:** Previously optimized (K-2 format ✓, G8.08 split ✓), now needs quality improvements

---

## TL;DR: What Needs Fixing?

| Issue | Count | Priority | Effort | Impact |
|-------|-------|----------|--------|--------|
| 1. "Understand" in descriptions | 53 skills | P2 | 3 hrs | Language precision |
| 2. X-2 violations (3-4 grade gaps) | 7 deps | P1 | 30 min | Progression clarity |
| 3. Missing concepts (slicing, nested, stack) | 3 skills | P1 | 90 min | Curriculum completeness |
| 4. Orphaned skills (no T10 deps) | 2 skills | P1 | 5 min | Progression clarity |
| 5. Potential redundancy (filter vs select) | 1 pair | P3 | 45 min | Avoid duplication |
| 6. Grade 4 too dense (27 skills) | 3-4 skills | P3 | 60 min | Balance workload |

**Total Priority 1 Effort:** ~2 hours → **119 skills** (from 115)
**Total Priority 1+2 Effort:** ~5-6 hours → High quality across all 119 skills

---

## Issue #1: Vague Language (53 Skills) - PRIORITY 2

**Problem:** Descriptions use "understand," "learn," "know" instead of observable verbs.

**Example:**
```
BEFORE: "They understand this scans all items and returns the lowest value."
AFTER:  "They observe this scans all items and returns the lowest value."
```

**Scope:** Grade 3 (7), Grade 4 (16), Grade 5 (17), Grade 6 (2), Grade 7 (5), Grade 8 (4)

**Note:** This is in DESCRIPTIONS, not skill names. Skill names are already action-oriented.

**Fix:** Batch find-replace with manual review
- "understand" → "observe" / "verify" / "note"
- "learn" → "explore" / "apply"
- "know" → "recognize" / "identify"

---

## Issue #2: X-2 Rule Violations (7 Dependencies) - PRIORITY 1

**Problem:** Some skills depend on skills 3-4 grades earlier, exceeding X-2 rule.

**Violations:**

### High-Impact (3-grade gaps - fixable)
- T10.G6.06 depends on T10.G3.06 (Grade 6 → Grade 3)
- T10.G6.07 depends on T10.G3.06 (Grade 6 → Grade 3)

**Fix:** Add T10.G5.19 bridge skill, update 2 dependencies ✓

### Lower-Impact (4-grade gaps - algorithmic foundations)
- T10.G8.02 (Bubble sort) → T10.G4.10 (Swap)
- T10.G8.03 (Selection sort) → T10.G4.07 (Find min)
- T10.G8.07 (Hash table) → T10.G4.02 (Parallel lists)

**Recommendation:** Accept as "foundational exceptions" (like variables) OR add 3 bridge skills in G6-7.

**Decision needed:** Treat G4 list primitives as persistent foundations?

---

## Issue #3: Missing Concepts (6 Concepts) - PRIORITY 1 (Partial)

**Tier 1 (Essential - ADD NOW):**
1. ✅ **List slicing** (G5.20): Extract sublist from positions A to B
2. ✅ **Nested lists** (G6.11): Lists within lists (2D arrays, grids)
3. ✅ **Stack operations** (G7.16): Push/pop (LIFO) for undo, backtracking

**Tier 2 (Nice to Have - Consider Later):**
4. Queue operations (G7.17): Enqueue/dequeue (FIFO)
5. Merge sorted lists (G8.11): Combine two sorted lists
6. List concatenation (covered by G4.11.02 append)

**Action:** Add 3 Tier 1 skills = +3 to skill count

---

## Issue #4: Orphaned Skills (2 Skills) - PRIORITY 1

**Problem:** Skills in G3+ with no T10 dependencies appear disconnected.

1. **T10.GK.05** (Find first/last) → Add dependency on T10.GK.01
2. **T10.G3.01.01** (Create list variable) → Add dependency on T10.G2.07

**Action:** Update 2 dependency lists (5 minutes)

---

## Issue #5: Potential Redundancy (1 Pair) - PRIORITY 3

**Investigate:**
- T10.G4.08: Filter items from a list based on a condition
- T10.G4.20: Select multiple items from a list by criteria

**Action:** Read full descriptions, determine if duplicate or distinct → Merge or clarify

---

## Issue #6: Grade 4 Imbalance (27 Skills) - PRIORITY 3

**Problem:** Grade 4 has 27 skills vs 12 in G3, 23 in G5. May overwhelm learners.

**Candidates to move:**
- T10.G4.19 (Find substring) → Grade 5 (advanced text)
- T10.G4.16.02 (Seeded random) → Grade 5 (advanced concept)
- T10.G4.20 (Select multiple) → Grade 5 or merge with G4.08

**Action:** Move 2-3 skills to Grade 5 for balance

---

## What's Already GOOD?

✅ **K-2 skills** have detailed Visual scenario format (Student task, Visual scenario, Correct answer, Implementation note)

✅ **Skill names** use active verbs (no "Understand" or "Learn" in skill names)

✅ **T10.G8.08 split** into 3 focused sub-skills (binary search, two-pointer, sliding window)

✅ **Grade 3 foundation** covers CRUD operations comprehensively

✅ **Grade 5 table operations** mirror Grade 3-4 list operations well

✅ **Grade 7 real-world** focus (Google Sheets, external data, AI) is strong

✅ **No overly broad skills** (descriptions are appropriately scoped)

---

## Recommended Action Plan

### Phase 1: Quick Wins (2 hours)
1. Add T10.G5.19 bridge skill (30 min)
2. Update 2 orphaned skill dependencies (5 min)
3. Add T10.G5.20 (List slicing) (30 min)
4. Add T10.G6.11 (Nested lists) (30 min)
5. Add T10.G7.16 (Stack operations) (30 min)

**Result:** 115 → 119 skills, fixes X-2 violations, adds essential concepts

### Phase 2: Language Quality (3 hours)
6. Batch-replace "understand" in 53 skill descriptions
7. Manual review each change for context

**Result:** All descriptions use observable, assessable language

### Phase 3: Optional Polish (2 hours)
8. Investigate G4.08 vs G4.20 redundancy
9. Decide on G8 X-2 violations (exception vs bridge)
10. Consider moving 2-3 skills from G4 to G5

---

## Specific Changes Summary

| Grade | Current | Add | Modify | New Total | Notes |
|-------|---------|-----|--------|-----------|-------|
| K | 8 | 0 | 1 dep | 8 | Update GK.05 dependency |
| 1 | 6 | 0 | 0 | 6 | No changes |
| 2 | 7 | 0 | 0 | 7 | No changes |
| 3 | 12 | 0 | 1 dep + 7 desc | 12 | Update G3.01.01 dependency, revise descriptions |
| 4 | 27 | 0 | 16 desc | 27 | Revise "understand" in descriptions |
| 5 | 23 | +2 | 17 desc | 25 | Add G5.19 (bridge), G5.20 (slicing) |
| 6 | 8 | +1 | 2 dep + 2 desc | 9 | Add G6.11 (nested), update G6.06/07 deps |
| 7 | 14 | +1 | 5 desc | 15 | Add G7.16 (stack) |
| 8 | 10 | 0 | 4 desc | 10 | Revise descriptions (+ decide on X-2) |
| **Total** | **115** | **+4** | **53 desc + 4 dep** | **119** | 3.5% growth, 46% revised |

---

## Quality Metrics Before/After

| Metric | Before | After P1 | After P1+P2 |
|--------|--------|----------|-------------|
| Total skills | 115 | 119 | 119 |
| K-2 visual format | 21/21 ✓ | 21/21 ✓ | 21/21 ✓ |
| Vague language | 53 | 53 | 0 ✓ |
| X-2 violations | 7 | 4-7* | 4-7* |
| Missing concepts | 6 | 3 | 3 |
| Orphaned skills | 3 | 1 ✓ | 1 ✓ |

*Depends on Grade 8 decision

---

## Key Decision Point

**Question for stakeholder:** Should Grade 8 advanced algorithms be allowed to depend on Grade 4 foundational primitives (4-grade gap)?

**Context:**
- Grade 8 algorithms (bubble sort, selection sort, hash tables) need primitives: swap, find-min, parallel lists
- These primitives are taught in Grade 4
- Grades 5-7 focus on tables (different data structure)

**Option A:** Accept as "foundational exception" (like how all grades use variables from T09)
- Rationale: Grade 4 list primitives are persistent foundations, not transient knowledge
- Action: Add explanatory notes to 3 Grade 8 skills (10 min)

**Option B:** Add 3 bridge/refresher skills in Grades 6-7
- Action: Create T10.G6.09 (swap review), T10.G6.10 (find-min review), T10.G7.15 (parallel lists review)
- Effort: 90 minutes

**Recommendation:** Option A (foundational exception)

---

## Files Created

1. **T10_ADDITIONAL_ANALYSIS.md** - Comprehensive 4000-word analysis with all details
2. **T10_ACTION_PLAN.md** - Step-by-step implementation guide with exact text changes
3. **T10_EXECUTIVE_SUMMARY.md** - This file (quick reference)

**Next Step:** Review this summary → Approve Priority 1 changes → Implement in 2 hours
