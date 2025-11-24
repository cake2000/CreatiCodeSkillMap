# T28 (Chance & Simulations) - Quick Reference
**Date:** 2024-11-24

## AT A GLANCE

**Total Skills:** 50 (G2-G8)
**Overall Status:** ⚠️ Nearly Ready (needs 4 critical fixes)
**Quality Score:** 88% (44/50 skills have no issues)

---

## CRITICAL ISSUES (MUST FIX)

| # | Issue | Impact | Fix Effort |
|---|-------|--------|------------|
| 1 | Missing K-1 foundation | Students lack pre-G2 vocabulary | 1-2 days (7 new skills) |
| 2 | T28.G5.01.02 → T27.G3.04 (X-2 violation) | Violates grade dependency rule | 5 minutes |
| 3 | T28.G5.08 → T03.G3.01 (X-2 violation) | Violates grade dependency rule | 5 minutes |
| 4 | T28.G3.05 too complex | Too broad for single skill | 1 hour (split to 2) |
| 5 | "pick random" block unverified | 9 skills depend on this | 1 hour (verify + update) |

---

## ALL T28 SKILLS BY GRADE

### Kindergarten (GK) - ❌ MISSING
**Recommended to add:**
- GK.01: Sort events by likelihood using pictures
- GK.02: Identify random vs predictable events
- GK.03: Participate in class random event

### Grade 1 (G1) - ❌ MISSING
**Recommended to add:**
- G1.01: Predict simple chance event outcomes
- G1.02: Compare likely vs unlikely events
- G1.03: Count and record outcomes with tally marks
- G1.04: Explain fair vs unfair in games

### Grade 2 (G2) - ✅ ALL GOOD (4 skills)
- T28.G2.01: Sort events into certain/possible/impossible
- T28.G2.02: Conduct picture-based chance experiment
- T28.G2.03: Decide if simple game is fair
- T28.G2.04: Predict and observe outcomes

### Grade 3 (G3) - ⚠️ 1 ISSUE (7 skills)
- T28.G3.01: Interpret provided simulation output ✅
- T28.G3.02: Explain "pick random" block ⚠️ (verify block exists)
- T28.G3.03: Record experimental data ✅
- T28.G3.04: Compare predictions to data ✅
- T28.G3.05: Describe game randomness + simulate ⚠️ **TOO COMPLEX - SPLIT**
- T28.G3.06: Modify provided random generator ✅
- T28.G3.07: Build random generator from scratch ✅

### Grade 4 (G4) - ✅ MOSTLY GOOD (7 skills)
- T28.G4.01: Build random generator with if-statements ✅
- T28.G4.02.01: Log trial results to list ✅
- T28.G4.02.02: Count frequencies ✅
- T28.G4.02.03: Calculate percentages ✅
- T28.G4.03: Show sample size effects ✅
- T28.G4.04: Debug unfair simulation ✅
- T28.G4.05: Generate random coordinate pairs ✅
- T28.G4.06: Interpret probabilities as fractions/percentages ✅
- T28.G4.07: Random selections without repetition ✅

### Grade 5 (G5) - ⚠️ 3 ISSUES (11 skills)
- T28.G5.01.01: Generate compound event data (two dice) ✅
- T28.G5.01.02: Analyze compound distributions ⚠️ **X-2 VIOLATION**
- T28.G5.02: Randomly assign participants ✅
- T28.G5.03: Monte Carlo sampling ✅
- T28.G5.04: Document simulation plans ✅
- T28.G5.05: Calculate theoretical probability ✅
- T28.G5.06: Compare experimental/theoretical probability ✅
- T28.G5.07: Create frequency distributions ⚠️ (redundant with G5.01.02?)
- T28.G5.08: Track agent state ⚠️ **X-2 VIOLATION**
- T28.G5.09: Calculate expected value ✅
- T28.G5.10: Recognize independence/gambler's fallacy ✅
- T28.G5.11: Demonstrate law of large numbers ✅

### Grade 6 (G6) - ✅ MOSTLY GOOD (11 skills)
- T28.G6.01.01: Manually test parameters ✅
- T28.G6.01.02: Automate parameter sweeps ✅
- T28.G6.02: Use random seeds ✅ **VERIFIED**
- T28.G6.03: Measure percent error ✅
- T28.G6.04: Simulate noisy sensors ✅
- T28.G6.05: Model agent in grid world ⚠️ (indirect X-2 via G5.08)
- T28.G6.06: Simulate changing probabilities ✅
- T28.G6.07: Design environment with obstacles ✅
- T28.G6.08: Implement reward rules ✅
- T28.G6.09: Create two-sprite interaction ✅
- T28.G6.10: Compare sampling methods ✅
- T28.G6.11: Calculate conditional probability ✅

### Grade 7 (G7) - ✅ ALL GOOD (7 skills)
- T28.G7.01: Create two-agent interaction ✅
- T28.G7.02: Trace agent learning ✅
- T28.G7.03: Test fairness with synthetic testers ✅
- T28.G7.04: Compare shuffled results ✅
- T28.G7.05: Communicate assumptions/limitations ✅
- T28.G7.06.01: Create multi-agent simulation ✅
- T28.G7.06.02: Aggregate metrics across agents ✅
- T28.G7.07: Identify bias in random selection ✅

### Grade 8 (G8) - ⚠️ 2 ISSUES (6 skills)
- T28.G8.01: Chain simulation→analysis→dashboard ⚠️ **TOO COMPLEX - SPLIT**
- T28.G8.02: Explore measurement variability ✅
- T28.G8.03: Integrate simulations into AI assistants ✅
- T28.G8.04: Publish policy briefs ⚠️ **TOO COMPLEX - SPLIT**
- T28.G8.05: Analyze environment bias ✅
- T28.G8.06: Distinguish random vs pseudorandom ✅

---

## X-2 RULE VIOLATIONS

| Skill | Violating Dependency | Grade Gap | Fix |
|-------|---------------------|-----------|-----|
| T28.G5.01.02 | T27.G3.04 | G5→G3 (2 grades) | Use T27.G5.x instead |
| T28.G5.08 | T03.G3.01 | G5→G3 (2 grades) | Use T03.G4.x or T03.G5.x |

**Note:** Several G4-G6 skills reference G3 dependencies but are within the X-2 rule (X, X-1, X-2 allowed)

---

## SKILLS NEEDING DECOMPOSITION

| Skill | Reason | Split Into |
|-------|--------|-----------|
| T28.G3.05 | Game analysis + coding + writing | 3.05a (analysis), 3.05b (coding) |
| T28.G8.01 | Full data pipeline | 8.01a (run), 8.01b (analyze), 8.01c (dashboard) |
| T28.G8.04 | Policy brief + viz + ethics | 8.04a (methodology), 8.04b (visualizations), 8.04c (ethical analysis) |

---

## CREATICODE BLOCKS STATUS

### ✅ Verified Available
- `data_setrandomlistseed` (random with seed)
- `data_setrandomlist` (random with/without repetition)
- Table shuffle operations

### ❓ Needs Verification
- Standard "pick random (1) to (10)" block
- Bar chart creation
- Interactive dashboards
- Variable monitors

### 📋 Check Other Topics
- T27: Chart blocks
- T09: Variable operations
- T10: Table operations
- T03: Coordinate navigation

---

## SKILL DEPENDENCY PATTERNS

### Grade 2 (Foundation)
- Physical experiments
- Picture-based classification
- Unplugged only

### Grade 3 (Introduction)
- Watch provided simulations
- Modify provided code
- Build first generators
- **Pattern:** Provided → Modified → Built

### Grade 4 (Expansion)
- Add conditionals
- Work with lists
- Calculate statistics
- **Pattern:** Single event → Multiple trials → Analysis

### Grade 5 (Deepening)
- Compound events
- Theoretical probability
- Compare theory vs experiment
- **Pattern:** Experimental → Theoretical → Compare

### Grade 6 (Application)
- Parameter testing
- Multi-agent systems
- Advanced sampling
- **Pattern:** Single → Multiple → Optimize

### Grade 7 (Integration)
- AI/ML concepts
- Fairness testing
- Ethical considerations
- **Pattern:** Build → Test → Document

### Grade 8 (Synthesis)
- Real-world applications
- Policy analysis
- AI integration
- **Pattern:** Simulate → Analyze → Communicate

---

## TOPIC STRENGTHS

1. ✅ Clear concrete→abstract progression
2. ✅ Strong scaffolding (provided→modified→built)
3. ✅ Excellent AI/ethics integration
4. ✅ Good balance of coding + concepts
5. ✅ Real-world applications (G8)
6. ✅ 88% of skills have clean dependencies

---

## TOPIC WEAKNESSES

1. ❌ Missing K-1 foundation
2. ⚠️ 2 X-2 rule violations
3. ⚠️ 3 overly broad skills
4. ⚠️ Some redundancy (G5.01.02 vs G5.07)
5. ⚠️ CreatiCode features unverified (9+ skills)
6. ⚠️ Steep jump G4→G5 (single→compound events)

---

## ACTION ITEMS CHECKLIST

### Priority 1: CRITICAL (Must fix before deployment)
- [ ] Add 2-3 GK skills (unplugged)
- [ ] Add 3-4 G1 skills (unplugged)
- [ ] Fix T28.G5.01.02 dependency (T27.G3.04 → T27.G5.x)
- [ ] Fix T28.G5.08 dependency (T03.G3.01 → T03.G4/5.x)
- [ ] Verify "pick random" block exists
- [ ] Split T28.G3.05 into 2 sub-skills

### Priority 2: QUALITY (Should fix)
- [ ] Split T28.G8.01 into 3 sub-skills
- [ ] Split T28.G8.04 into 3 sub-skills
- [ ] Add T28.G4.08 (intermediate multi-outcome skill)
- [ ] Resolve G5.01.02 vs G5.07 overlap
- [ ] Update G4 skills to reference G4 loops (not G3)

### Priority 3: POLISH (Nice to have)
- [ ] Add specific criteria to 4 ambiguous skills
- [ ] Cross-reference T27, T09, T10, T03 analyses
- [ ] Add math/writing cross-topic dependencies
- [ ] Document CreatiCode block usage patterns
- [ ] Create teacher implementation guide

---

## COMPARISON SUMMARY

**T28 vs Other Topics:**
- **Better than:** T27 (Data Viz)
- **Comparable to:** T26 (Surveys)
- **Status:** Nearly ready with fixes

**After Priority 1 fixes: Expected to be STRONG** ✅

---

## FILES REFERENCE

1. **T28_ANALYSIS_REPORT.md** - Full detailed analysis (50 pages)
2. **T28_FEATURE_VERIFICATION.md** - CreatiCode blocks verification
3. **T28_EXECUTIVE_SUMMARY_FINAL.md** - Executive overview
4. **T28_QUICK_REFERENCE.md** - This file (quick lookup)

---

**Last Updated:** 2024-11-24
**Status:** Ready for review
**Next Action:** Stakeholder approval for Priority 1 fixes
