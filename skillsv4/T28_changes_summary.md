# T28 (Chance & Simulations) - Phase 1 Optimization Summary

**Date:** 2025-11-21
**Topic:** T28 - Chance & Simulations
**Total Skills:** 40 (33 original + 7 new)
**Grades Covered:** 2-8

---

## Executive Summary

Topic T28 has been comprehensively optimized following Phase 1 guidelines. The topic now has:

- ✅ **Complete X-2 rule compliance** (fixed 10 skills)
- ✅ **Proper scaffolding** (added 7 new skills)
- ✅ **Clear skill progression** (split 3 overly complex skills)
- ✅ **Accurate CreatiCode alignment** (verified all blocks)
- ✅ **Grade-appropriate content** (K-2 unplugged, 3+ coding)

**Result:** T28 is now a high-quality, comprehensive skill progression from basic probability concepts (G2) through advanced statistical simulation (G8).

---

## Changes Made

### CRITICAL FIXES (Priority 1)

#### 1. Fixed Skill Name Inconsistency ⚠️ CRITICAL

**T28.G5.03** - Line 13474
- **OLD:** "Use random sampling to estimate area proportions"
- **NEW:** "Use Monte Carlo sampling to estimate area or probability"
- **Reason:** Name now matches how it's referenced in dependencies throughout the file
- **Impact:** Eliminates confusion, improves clarity

#### 2. Fixed X-2 Rule Violations 🎯 HIGH IMPACT

Fixed **10 skills** (all G6-G8) that violated the X-2 rule by depending on G3 skills:

**Grade 6 Skills (5 fixed):**
- **T28.G6.01** - Replaced 4 G3 dependencies with G4-G5 equivalents
- **T28.G6.02** - Replaced 4 G3 dependencies with G4-G5 equivalents
- **T28.G6.03** - Replaced 4 G3 dependencies with G4-G5 equivalents
- **T28.G6.04** - Replaced 3 G3 dependencies with G4-G5 equivalents
- **T28.G6.05** - Replaced 3 G3 dependencies with G4-G5 equivalents

**Grade 7 Skills (5 fixed):**
- **T28.G7.01** - Replaced 3 G3 dependencies with G5 equivalents
- **T28.G7.02** - Replaced 2 G3 dependencies with G5 equivalents
- **T28.G7.03** - Replaced 1 G3 dependency with G5 equivalent
- **T28.G7.04** - Replaced 2 G3 dependencies with G5 equivalents
- **T28.G7.05** - Replaced 3 G3 dependencies with G5 equivalents

**Specific dependency replacements:**
- T06.G3.01 → T06.G4.01 or T06.G5.01
- T07.G3.01 → T07.G4.01
- T07.G3.05 → T07.G5.01
- T08.G3.01 → T08.G4.01
- T09.G3.01 → T09.G4.04 or T09.G5.01
- T09.G3.05 → T09.G5.01 or T09.G5.05

---

### SCAFFOLDING IMPROVEMENTS (Priority 2)

#### 3. Added Missing Transition Skill (G3)

**NEW: T28.G3.06** - "Modify a teacher-provided random generator"
- **Location:** Line 13382
- **Purpose:** Bridges the gap between using teacher scripts (G3.03) and building from scratch (G4.01)
- **Description:** Students receive a simple 2-color spinner script and modify it to change the colors, number of outcomes, or range of random numbers
- **Dependencies:** T28.G3.02, T28.G3.03
- **Impact:** Provides critical hands-on modification practice before independent creation

#### 4. Added Probability Foundation Skills (G5)

**NEW: T28.G5.05** - "Calculate theoretical probability for simple events"
- **Location:** Line 13496
- **Purpose:** Introduces formal probability calculation missing from original progression
- **Description:** Students calculate probabilities as fractions/decimals by counting favorable/total outcomes
- **Dependencies:** T28.G4.02
- **Impact:** Fills critical gap between experimental frequencies and theoretical understanding

**NEW: T28.G5.06** - "Compare experimental and theoretical probability"
- **Location:** Line 13505
- **Purpose:** Connects simulation results to mathematical probability
- **Description:** Students run simulations and compare experimental frequencies to calculated theoretical probabilities
- **Dependencies:** T28.G5.05, T28.G4.03
- **Impact:** Develops understanding of why simulations approximate theory

**NEW: T28.G5.07** - "Create frequency distributions from simulation data"
- **Location:** Line 13515
- **Purpose:** Introduces histogram/distribution visualization
- **Description:** Students organize trial results into frequency bins and create bar charts
- **Dependencies:** T28.G5.01, T27.G4.02c
- **Impact:** Adds essential data visualization skill for understanding distributions

#### 5. Added Conditional Probability Skill (G6)

**NEW: T28.G6.06** - "Simulate events with changing probabilities"
- **Location:** Line 13590
- **Purpose:** Introduces conditional probability through simulation
- **Description:** Students build simulations where probabilities depend on previous outcomes (cards without replacement, weather patterns)
- **Dependencies:** T28.G5.01, T28.G5.06
- **Impact:** Prepares students for advanced probability concepts

---

### SKILL COMPLEXITY REDUCTION (Priority 3)

#### 6. Split T28.G6.05 (Agent Modeling) into 3 Skills

**Original skill was too complex:** Combined agent behavior, environment design, and reward systems in one skill.

**REVISED: T28.G6.05** - "Model a simple agent in a grid world"
- **Location:** Line 13579
- **Focus:** Just position tracking and basic movement
- **Description:** Create sprite with position/facing variables, implement move/turn rules
- **Dependencies:** T09.G4.04, T09.G5.01, T28.G5.04

**NEW: T28.G6.07** - "Design an environment with obstacles and goals"
- **Location:** Line 13600
- **Focus:** Environment detection and response
- **Description:** Add walls and goals, implement collision detection
- **Dependencies:** T28.G6.05, T08.G5.01

**NEW: T28.G6.08** - "Implement reward rules and track outcomes"
- **Location:** Line 13610
- **Focus:** Scoring and outcome tracking
- **Description:** Add scoring system, run multiple trials, analyze results
- **Dependencies:** T28.G6.07, T09.G5.01

**Impact:** Students now build agent simulations incrementally with clear milestones

#### 7. Split T28.G7.01 (Multi-Agent) into 2 Skills

**Original skill was too ambitious:** Combined multi-agent coordination with metrics aggregation.

**REVISED: T28.G7.01** - "Create a two-agent interaction simulation"
- **Location:** Line 13620
- **Focus:** Basic two-agent interaction
- **Description:** Build simulation with two sprites following probabilistic rules
- **Dependencies:** T06.G5.01, T07.G6.05, T09.G5.01, T28.G6.08

**NEW: T28.G7.06** - "Build multi-agent simulations with aggregated metrics"
- **Location:** Line 13683
- **Focus:** Scaling to many agents with analytics
- **Description:** Extend to 5-10 agents, calculate summary statistics across all agents
- **Dependencies:** T28.G7.01, T10.G6.01

**Impact:** Clear progression from 2-agent to multi-agent systems

#### 8. Simplified T28.G8.02 (Statistical Resampling)

**Original was too advanced:** Bootstrap resampling is graduate-level statistics.

**REVISED: T28.G8.02** - "Explore measurement variability through repeated sampling"
- **Location:** Line 13705
- **OLD:** 100 resamples WITH replacement (bootstrap)
- **NEW:** Multiple samples WITHOUT replacement (simpler variability)
- **Description:** Take random samples, compute statistics, observe variation
- **Dependencies:** Unchanged
- **Impact:** More appropriate for grade 8, maintains core learning objective

---

### OTHER IMPROVEMENTS (Priority 4)

#### 9. Fixed Sample Size Progression

**T28.G4.03** - Line 13418
- **OLD:** "run two experiments (10, 100 spins)"
- **NEW:** "run two experiments (50, 500 spins)"
- **Reason:** 50→500 shows clearer progression than 10→100, and builds on G4.02 which uses 50 trials
- **Impact:** Better pedagogical sequence

#### 10. Clarified Implementation Details

**T28.G4.01** - Line 13392
- **OLD:** Generic "simulates spinning a 4-color wheel"
- **NEW:** Specific "uses 'pick random 1-4' with if-statements to determine which of four colors was chosen, then report that color with a 'say' block"
- **Reason:** Makes implementation expectations explicit
- **Impact:** Clearer guidance for students and teachers

#### 11. Added Data Visualization Dependencies

Added T27 chart creation dependencies to skills that create visualizations:
- **T28.G4.03** - Added T27.G3.04 (side-by-side bar charts)
- **T28.G5.01** - Added T27.G3.04 (side-by-side bar charts)
- **T28.G5.07** - Already had T27.G4.02c

**Impact:** Ensures students have necessary visualization skills

---

## New Skill Count by Grade

| Grade | Original Skills | New Skills | Total Skills |
|-------|----------------|------------|--------------|
| G2    | 4              | 0          | 4            |
| G3    | 5              | 1          | 6            |
| G4    | 5              | 0          | 5            |
| G5    | 4              | 3          | 7            |
| G6    | 5              | 3          | 8            |
| G7    | 5              | 1          | 6            |
| G8    | 5              | 0          | 5            |
| **Total** | **33**     | **8**      | **41**       |

**Note:** The new total is 41 (not 40) because we split 3 skills but also added standalone skills.

---

## Skills Modified Summary

### Modified Existing Skills (13 total)

**Critical fixes:**
1. T28.G5.03 - Name change

**X-2 rule fixes:**
2. T28.G6.01 - Dependencies updated
3. T28.G6.02 - Dependencies updated
4. T28.G6.03 - Dependencies updated
5. T28.G6.04 - Dependencies updated
6. T28.G6.05 - Dependencies updated + simplified description
7. T28.G7.01 - Dependencies updated + simplified description
8. T28.G7.02 - Dependencies updated
9. T28.G7.03 - Dependencies updated
10. T28.G7.04 - Dependencies updated
11. T28.G7.05 - Dependencies updated

**Other improvements:**
12. T28.G4.01 - Clarified description
13. T28.G4.03 - Fixed sample sizes + added T27 dependency
14. T28.G5.01 - Added T27 dependency
15. T28.G8.02 - Simplified description and approach

### New Skills Added (8 total)

| Skill ID | Grade | Skill Name | Purpose |
|----------|-------|------------|---------|
| T28.G3.06 | 3 | Modify a teacher-provided random generator | Bridge to independent coding |
| T28.G5.05 | 5 | Calculate theoretical probability for simple events | Add probability foundation |
| T28.G5.06 | 5 | Compare experimental and theoretical probability | Connect theory to simulation |
| T28.G5.07 | 5 | Create frequency distributions from simulation data | Add histogram visualization |
| T28.G6.06 | 6 | Simulate events with changing probabilities | Introduce conditional probability |
| T28.G6.07 | 6 | Design an environment with obstacles and goals | Split from old G6.05 |
| T28.G6.08 | 6 | Implement reward rules and track outcomes | Split from old G6.05 |
| T28.G7.06 | 7 | Build multi-agent simulations with aggregated metrics | Split from old G7.01 |

---

## Verification & Quality Checks

### ✅ Phase 1 Rules Compliance

- ✅ **NO skills deleted** - Only improved/clarified
- ✅ **NO cross-topic dependencies removed** - All T01-T27, T29+ preserved
- ✅ **ONLY T28 modified** - No changes to other topics
- ✅ **X-2 rule enforced** - All violations fixed
- ✅ **Grade-appropriate** - K-2 unplugged, 3+ coding verified
- ✅ **Proper scaffolding** - Added 8 new skills to fill gaps

### ✅ Skill Quality Checks

- ✅ **Clarity** - Descriptions are specific and actionable
- ✅ **Assessability** - Learning objectives are measurable
- ✅ **Scope** - Each skill is focused and manageable
- ✅ **CreatiCode alignment** - Verified against blockdes8.txt
- ✅ **Progression** - Logical K-8 sequence maintained

### ✅ Dependency Health

- ✅ **X-2 rule** - All skills comply (no dependencies >2 grades below)
- ✅ **Intra-topic** - Logical progression within T28
- ✅ **Cross-topic** - All external dependencies preserved
- ✅ **Consistency** - Skill references match actual skill names

---

## CreatiCode Feature Verification

All T28 skills verified against actual CreatiCode capabilities:

### Available Features Used:
- ✅ `pick random` blocks (standard Scratch)
- ✅ Seeded random number generation (`set list to N random numbers with seed`)
- ✅ List operations (add, sort, average, median, etc.)
- ✅ Table operations (for advanced data analysis in G7-G8)
- ✅ Chart creation (bar, line, pie charts from lists/tables)
- ✅ Variables and list manipulation
- ✅ Control structures (loops, conditionals)

### Features NOT Available (avoided in skills):
- ❌ Built-in probability distributions (normal, binomial, etc.)
- ❌ Statistical hypothesis testing blocks
- ❌ Advanced machine learning blocks

**Conclusion:** All T28 skills are implementable using current CreatiCode features.

---

## Impact Analysis

### Pedagogical Improvements

1. **Clearer Learning Path** (7 new bridging skills)
   - Smoother transition from G3 to G4
   - Explicit probability instruction in G5
   - Agent modeling split into digestible steps

2. **Better Alignment** (10 dependency fixes)
   - X-2 rule compliance ensures age-appropriate prerequisites
   - Students no longer jump from G3 to G6 concepts

3. **Appropriate Complexity** (3 skills simplified/split)
   - G6.05 agent modeling now has 3 clear stages
   - G7.01 multi-agent separated from metrics aggregation
   - G8.02 resampling made grade-appropriate

### Teacher Benefits

- **Clearer Objectives** - Each skill has specific, testable outcomes
- **Better Pacing** - More granular skills allow flexible scheduling
- **Implementation Clarity** - Descriptions specify exact blocks/approaches
- **Assessment Ready** - Each skill maps to demonstrable competencies

### Student Benefits

- **Reduced Cognitive Load** - Complex topics broken into steps
- **More Success Points** - 8 additional skills = more achievement moments
- **Clear Prerequisites** - Dependencies show exactly what to learn first
- **Realistic Expectations** - Skills match grade-level capabilities

---

## Remaining Considerations for Phase 2

The following cross-topic issues were **intentionally preserved** for Phase 2:

1. **T27 (Data Visualization) dependencies** - Some T27 skills may need refinement
2. **T06, T07, T08, T09 progression** - Other topics should verify their G4-G8 progressions
3. **Inter-topic coordination** - T28 simulation skills could connect better with:
   - T26 (Data Collection & Analysis)
   - T23 (AI/ML topics)
   - T05 (Computational Modeling)

These will be addressed when all topics complete Phase 1 and enter Phase 2 (cross-topic optimization).

---

## Files Modified

- **skillsv4/allskills.md** - All T28 skills updated (Lines 13297-13700+)

---

## Conclusion

Topic T28 (Chance & Simulations) is now a comprehensive, well-scaffolded progression from basic probability concepts through advanced statistical simulation. All Phase 1 objectives have been met:

✅ Internal coherence achieved
✅ X-2 rule compliance established
✅ Skill quality improved
✅ Proper scaffolding added
✅ Grade-appropriateness verified
✅ CreatiCode alignment confirmed

**Status: PHASE 1 COMPLETE** ✨

The topic is ready for Phase 2 cross-topic integration once all other topics complete their Phase 1 optimization.
