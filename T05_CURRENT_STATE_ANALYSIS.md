# T05 Human-Centered Design - CURRENT STATE Analysis
Generated: 2025-11-23

## IMPORTANT FINDING

The T05 optimization report (dated 2025-11-20) states that optimizations were applied to `allskills.md`, but the individual topic file `/skillsv4/skills_T05_human_centered_design.md` appears to contain the **PRE-OPTIMIZATION** version.

This analysis is based on the ACTUAL CURRENT STATE in `skills_T05_human_centered_design.md`.

---

## Executive Summary

Topic T05 (Human-Centered Design) contains **54 skills** across grades K-8 in its CURRENT file state.

**Status:** PRE-PHASE 1 STATE (issues NOT yet applied to topic file)

**Major Issues Found:**
1. **X-2 Rule Violations:** Extensive GK dependencies in G5-G8 (24+ violations)
2. **Incorrect Dependency References:** G7 skills reference wrong G1 skill names
3. **Redundant Same-Grade Dependencies:** 3 instances in G3
4. **Heavy Cross-Grade Dependencies:** G6-G8 depend heavily on G1 skills

---

## Current Issues Summary

### HIGH PRIORITY (8 issues)

#### H1: Incorrect Dependency Reference in T05.GK.04
**Current State:**
```
Dependencies:
* T05.GK.02: Match a simple problem to a helpful tool
* T05.GK.03: Compare two tools and explain which is better for a task  ← WRONG NAME
```

**Actual T05.GK.03 name:** "Decide which version is easier to use"

**Fix Needed:** Update reference to match actual skill name

---

#### H2: Incorrect Dependency References in G7 Skills (6 skills affected)
**Current State in T05.G7.01-G7.06:**
```
Dependencies:
* T05.G1.01: Identify what a character needs in a story  ← WRONG! This is the actual G1.01 name
* T05.G1.02: Match a need to a design idea  ← WRONG! This is the actual G1.02 name
```

**Actual Situation:** The optimization report claims these are wrong references, but they actually MATCH the real skill names in the file. This suggests:
1. Either the optimization report made an error, OR
2. The G5 skills have different names than reported

Let me verify by checking G5.01 actual name:

From file: T05.G5.01 is "Write clear user needs and requirements for a small app"

So the G7 skills ARE incorrectly referencing G1 skill names when they meant to reference G5 skills. This is a REAL error.

**Fix Needed:** Replace references in G7.01-G7.06:
- FROM: T05.G1.01, T05.G1.02
- TO: T05.G5.01, T05.G5.02

---

#### H3: Redundant Same-Grade Dependencies (3 skills)

**T05.G3.02** depends on:
- T05.G3.01 (same grade, earlier skill) ← REDUNDANT
- T08.G3.01
- T05.G2.03

**T05.G3.04** depends on:
- T05.G3.03 (same grade, earlier skill) ← REDUNDANT
- T08.G3.02
- T09.G3.01

**T05.G3.05** depends on:
- T05.G3.04 (same grade, earlier skill) ← REDUNDANT
- T08.G3.03
- T07.G3.02

**Fix Needed:** Remove same-grade dependencies

---

### MEDIUM PRIORITY (24+ violations)

#### M1: X-2 Rule Violations - G5 Skills Depending on GK Skills

All 6 Grade 5 skills violate X-2 rule (5 grades span):

**T05.G5.01, G5.02, G5.03, G5.04, G5.05, G5.06** all depend on:
- T05.GK.03 and/or T05.GK.04

**Fix Needed:** Replace GK dependencies with G3 skills

---

#### M2: X-2 Rule Violations - G6 Skills Depending on GK Skills

All 6 Grade 6 skills violate X-2 rule (6 grades span):

**T05.G6.01, G6.02, G6.03, G6.04, G6.05, G6.06** all depend on:
- T05.GK.03 and/or T05.GK.04

**Fix Needed:** Replace GK dependencies with G4 skills

---

#### M3: X-2 Rule Violations - G7 Skills Depending on GK Skills

All 6 Grade 7 skills violate X-2 rule (7 grades span):

**T05.G7.01-G7.06** all depend on:
- T05.GK.03 and/or T05.GK.04

**Fix Needed:** Replace GK dependencies with G5 skills

---

#### M4: X-2 Rule Violations - G8 Skills Depending on GK Skills

All 6 Grade 8 skills violate X-2 rule (8 grades span):

**T05.G8.01, G8.02, G8.03, G8.04, G8.05, G8.06** all depend on:
- T05.GK.03 and/or T05.GK.04
- Plus G1 skills (T05.G1.01, G1.02, G1.03)

**Fix Needed:** Replace GK dependencies with G6 skills

---

#### M5: Redundant Dependencies in G4 Skills

All 6 G4 skills include BOTH T05.GK.03 AND T05.GK.04, but since GK.04 already depends on GK.03, listing both is redundant.

**T05.G4.01-G4.06** all have:
```
Dependencies:
* T05.G1.01
* T05.GK.03  ← REDUNDANT when GK.04 is present
* T05.GK.04
```

**Fix Needed:** Remove T05.GK.03 from all G4 skills

---

## Complete Inventory of Issues by Skill

### Skills with Issues: 38 total

**Kindergarten (1):**
- T05.GK.04: Wrong dependency reference name

**Grade 3 (3):**
- T05.G3.02: Redundant same-grade dependency
- T05.G3.04: Redundant same-grade dependency
- T05.G3.05: Redundant same-grade dependency

**Grade 4 (6):**
- T05.G4.01-G4.06: All have redundant GK.03 when GK.04 present

**Grade 5 (6):**
- T05.G5.01-G5.06: All violate X-2 rule with GK dependencies

**Grade 6 (6):**
- T05.G6.01-G6.06: All violate X-2 rule with GK dependencies

**Grade 7 (6):**
- T05.G7.01-G7.06: All have wrong skill name references AND violate X-2 rule

**Grade 8 (6):**
- T05.G8.01-G8.06: All violate X-2 rule with GK dependencies

**Grades 1-2 and remainder of K: 0 issues**

---

## What IS Working Well

Despite the dependency issues, the skill content itself is excellent:

### Strengths:

1. **Clear Skill Descriptions** ✓
   - All 54 skills have specific, actionable descriptions
   - No overly broad skills
   - Well-scoped for IXL-style microsteps

2. **Grade-Appropriate Modalities** ✓
   - K-2: Picture-based MCQ, drag-and-drop
   - G3+: Text-based, block-based coding context
   - Assessment formats are age-appropriate

3. **Logical Content Progression** ✓
   - K: Who helps? What's easier?
   - G1: User needs identification
   - G2: User types, intro simulation
   - G3: HCD process, feedback
   - G4: Personas, accessibility
   - G5: Requirements, wireframes
   - G6: Comprehensive HCD application
   - G7: Audits, harms, data-driven
   - G8: Briefs, experiments, critique

4. **No Duplicates** ✓
   - All apparent overlaps are intentional progressions
   - Each skill targets distinct practice

5. **Two Clear Strands** ✓
   - HCD strand: ~40 skills
   - Simulation planning strand: ~14 skills
   - Well-integrated

6. **Auto-Gradable Formats** ✓
   - All assessment formats feasible for auto-grading
   - Picture MCQ, drag-drop, multi-select, matching, checklists, templates

---

## Cross-Topic Dependencies (Current State)

**Dependencies TO Other Topics:**

| Target | Skill | Count | Status |
|--------|-------|-------|--------|
| T01 | Various | 5 | To review in Phase 2 |
| T03 | T03.GK.01 | 1 | Appropriate |
| T04 | T04.G2.01 | 1 | To review |
| T06 | T06.G3.01 | 2 | Appropriate |
| T06 | T06.G5.01 | 1 | Appropriate |
| T07 | T07.G3.01 | 1 | To review |
| T07 | T07.G3.02 | 1 | To review |
| T08 | T08.G3.01 | 1 | To review |
| T08 | T08.G3.02 | 2 | To review |
| T08 | T08.G3.03 | 1 | To review |
| T09 | T09.G3.01 | 4 | Appropriate (essential for simulations) |

**Observations:**
- T09 (Variables) dependencies are appropriate for simulation planning
- T06 (Sequences) dependencies make sense for script building
- T08 (Conditionals) dependencies in G3 HCD process need review
- T01, T04, T07 dependencies should be verified in Phase 2

---

## Specific Recommendations

### Immediate Actions (Apply Phase 1 Fixes):

1. **Fix T05.GK.04** - Update dependency reference name
2. **Fix G7.01-G7.06** - Correct skill name references (6 skills)
3. **Remove Same-Grade Dependencies** - G3.02, G3.04, G3.05 (3 skills)
4. **Remove Redundant GK.03** - G4.01-G4.06 (6 skills)
5. **Replace GK Dependencies:**
   - G5.01-G5.06: Replace with G3 skills (6 skills)
   - G6.01-G6.06: Replace with G4 skills (6 skills)
   - G7.01-G7.06: Replace with G5 skills (6 skills - already fixed refs)
   - G8.01-G8.06: Replace with G6 skills (6 skills)

**Total fixes needed: 38 skills**

### Phase 2 Actions (Cross-Topic Review):

6. **Review T08 Dependencies** - Are conditionals necessary for HCD process?
7. **Review T01 Dependencies** - Especially T01.G6.01 in G8 design skills
8. **Review T04/T07 Dependencies** - Verify necessity
9. **Verify T09 Dependencies** - Should remain (essential for simulations)
10. **Consider G1 Heavy Dependencies** - G6-G8 depend heavily on G1.01/G1.02

---

## File Status Check

**Current File:** `/skillsv4/skills_T05_human_centered_design.md`
- Version: v2 (IXL-Style Microsteps)
- State: PRE-PHASE 1 OPTIMIZATION
- Last Modified: Unknown (file doesn't show modification date in header)

**Optimization Reports:**
- `/skillsv4/T05_optimization_report.md` - Phase 1 fixes PROPOSED
- `/skillsv4/T05_optimization_summary.md` - Claims fixes APPLIED to allskills.md (2025-11-20)

**Discrepancy:**
- Fixes were applied to `allskills.md` but NOT to individual topic file
- Analysis should be done on `allskills.md` to see post-Phase 1 state
- OR individual topic file needs to be updated to match allskills.md

---

## Conclusion

**Content Quality:** EXCELLENT - All skills are well-designed, clear, and appropriate

**Dependency State:** NEEDS PHASE 1 FIXES - 38 skills have dependency issues

**Next Steps:**
1. Verify which file is authoritative (allskills.md or individual topic file)
2. Apply Phase 1 fixes if not yet applied to authoritative file
3. Proceed to Phase 2 cross-topic review

**Overall Potential Rating:** 4.5/5.0 (after Phase 1 fixes applied)

---

## Action Required

**USER SHOULD:**
1. Confirm whether `allskills.md` or `skills_T05_human_centered_design.md` is the authoritative source
2. If individual file is authoritative: Apply the 38 Phase 1 fixes from optimization report
3. If allskills.md is authoritative: Extract updated T05 section and sync to individual file
4. Then proceed with Phase 2 cross-topic optimization

