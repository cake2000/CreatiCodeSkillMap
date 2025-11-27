# T27 Optimization - Action Checklist

Quick reference for implementing the T27 (Chance & Simulations) optimization.

---

## Phase 1: Critical Fixes (Priority: URGENT)
**Goal:** Fix vague verbs and add critical bridge skill
**Time:** 2-3 hours
**Impact:** Makes all skills assessable

### Skills to Modify (Content Changes)
- [ ] **T27.GK.02** - Change "Identify maybe events" → "Select maybe events and test predictions"
  - Add testing component (pick from crayon box 3 times)
  - Make auto-gradable

- [ ] **T27.G2.01** - Change "Sort events" → "Sort events and defend one choice"
  - Add verification: Select one from each bin and explain
  - Success criterion: All 9 cards sorted correctly

- [ ] **T27.G3.01** - Change "Read and explain" → "Compare to predictions and calculate differences"
  - Add prediction worksheet
  - Calculate differences for each color
  - More active assessment

- [ ] **T27.G3.05** - Change "Classify games" → "Trace role of randomness and predict impact"
  - Trace one playthrough, tally random vs. controlled decisions
  - Test by playing modified version

- [ ] **T27.G5.10** - Change "Identify independent events" → "Test independence by tracking streaks"
  - Run simulation: 100 trials after streak of 5 heads
  - Calculate actual percentage
  - Compare to gambler's fallacy

- [ ] **T27.G3.04** - Enhance: Add "calculate prediction error"
  - Keep current content
  - Add: Calculate |prediction - actual| for each color

- [ ] **T27.G8.05** - Change "Analyze how environment biases" → "Compare and measure bias"
  - Run 50 trials in two mazes
  - Calculate bias metric: (avg steps - optimal) / optimal
  - Compare mazes quantitatively

### New Skills to Add
- [ ] **T27.G2.05** - NEW: Watch CreatiCode spinner simulation and match outcomes
  - Create starter project with spinner sprite
  - 5 trials, match to picture chart
  - Bridges G2→G3 gap

### Dependency Updates
- [ ] Update **T27.G3.01** dependencies to include new T27.G2.05

---

## Phase 2: Fill Progression Gaps (Priority: HIGH)
**Goal:** Add missing conceptual bridges
**Time:** 4-5 hours
**Impact:** Smoother K-8 progression

### New Skills to Add

- [ ] **T27.G4.08** - NEW: Draw area models to represent probability
  - Draw circle divided proportionally
  - Label with fractions and percentages
  - Run simulation and compare
  - **Dependencies:** T27.G4.02.03, T26.G4.04

- [ ] **T27.G5.12** - NEW: Calculate mean and spread of random variable
  - 1000 die rolls
  - Calculate mean, range, standard deviation
  - Compare to theoretical mean (3.5)
  - **Dependencies:** T27.G5.09, T26.G5.01

- [ ] **T27.G6.12** - NEW: Generate all outcomes using organized lists/tree diagrams
  - Create organized list for 2 coins (HH, HT, TH, TT)
  - Start tree diagram for 2 dice (36 outcomes)
  - Code nested loops to generate all pairs
  - **Dependencies:** T27.G5.01.01, T07.G5.01

### Skills to Split

- [ ] **Split T27.G5.04** → T27.G5.04.01 + T27.G5.04.02
  - **G5.04.01:** Define question, variables, trials (3 components)
  - **G5.04.02:** Choose model, define success criteria (2 components)
  - **G5.04.02 depends on:** T27.G5.04.01

### Dependency Updates
- [ ] Update **T27.G5.05** dependencies to include T27.G4.08 (area models)
- [ ] Update **T27.G6.04** dependencies: Change T27.G5.04 → T27.G5.04.01
- [ ] Update **T27.G8.02** dependencies to include T27.G5.12 (mean/spread)
- [ ] Update **T27.G7.01** dependencies to include T27.G5.08 (track agent state)

---

## Phase 3: AI-Era Enhancements (Priority: MEDIUM)
**Goal:** Add AI-relevant skills
**Time:** 3-4 hours
**Impact:** Prepares for AI integration

### New Skills to Add

- [ ] **T27.G5.13** - NEW: Generate synthetic training data with labels
  - Create 100 synthetic fruits with [size, color, shape] features
  - Code rules for each fruit type
  - Export as training data
  - Discuss: How does data quality affect AI?
  - **Dependencies:** T27.G5.01.01, T27.G4.02.01, T21.G4.01

- [ ] **T27.G7.08** - NEW: Simulate AI confidence scores and test thresholds
  - Generate 200 fake detections with confidence 0-100%
  - Test thresholds: 50%, 70%, 90%
  - Calculate acceptances at each threshold
  - Connect to self-driving cars
  - **Dependencies:** T27.G6.04, T27.G6.01.02, T21.G5.01

- [ ] **T27.G8.07** - NEW: Compare random vs. guided search in game trees
  - Build simple game (tic-tac-toe simplified)
  - Strategy A: Random simulation (10 games per move)
  - Strategy B: Guided (weight successful moves)
  - Measure win rates after 50 games
  - Connect to Monte Carlo Tree Search / AlphaGo
  - **Dependencies:** T27.G6.01.02, T27.G7.02, T21.G7.01

### K-2 Enhancements

- [ ] **T27.GK.01** - Enhance description
  - List exact 8 cards (4 certain, 4 impossible)
  - Add verification: Point and explain one from each bin
  - Success criterion: All 8 sorted correctly

- [ ] **T27.G1.01** - Enhance description
  - Add specific materials list
  - Describe recording sheet (2 columns × 6 rows)
  - Add comparison step at end

- [ ] **T27.G2.02** - Enhance description
  - Two specific setups: Option A (spinner), Option B (bag)
  - Exact numbers: 10 trials, 4 colors, 8 blocks
  - Success criterion: 10 trials with correct tally marks

---

## Phase 4: Advanced Improvements (Priority: LOW)
**Goal:** Complete optimization with assessment skills and final splits
**Time:** 3-4 hours
**Impact:** Professional-grade curriculum

### Skills to Split

- [ ] **Split T27.G7.05** → T27.G7.05.01 + T27.G7.05.02
  - **G7.05.01:** Document assumptions and limitations
  - **G7.05.02:** Identify stakeholders affected by decisions
  - **G7.05.02 depends on:** T27.G7.05.01

- [ ] **Split T27.G8.01** → T27.G8.01.01 + T27.G8.01.02
  - **G8.01.01:** Automate data collection with parameter sweeps
  - **G8.01.02:** Build interactive dashboard from simulation data
  - **G8.01.02 depends on:** T27.G8.01.01

### New Assessment Skills

- [ ] **T27.G4.09** - NEW: Test simulation reliability by running multiple times
  - Run same simulation 5 times
  - Record results each time
  - Calculate range
  - Evaluate: Is range acceptable?
  - **Dependencies:** T27.G4.03, T27.G4.04

- [ ] **T27.G6.13** - NEW: Identify and fix edge-case bugs
  - Debug: Division by zero (empty list)
  - Debug: Index out of bounds (deleted items)
  - Debug: Infinite loop (impossible condition)
  - For each: Identify, test, fix, verify
  - **Dependencies:** T27.G4.04, T12.G5.01, T08.G5.01

### Dependency Updates for Splits
- [ ] Update all skills that depended on **T27.G7.05** to depend on both:
  - T27.G7.05.01 (assumptions)
  - T27.G7.05.02 (stakeholders)
  - **Affected:** T27.G8.01.01, T27.G8.03, T27.G8.04

- [ ] Update all skills that depended on **T27.G8.01** to depend on:
  - T27.G8.01.02 (the comprehensive dashboard skill)
  - **Affected:** T27.G8.03

---

## Verification Checklist

### After Each Phase, Verify:

#### Content Quality
- [ ] All modified skills use active verbs (no "identify", "understand")
- [ ] K-2 skills have specific examples (not "illustrated cards")
- [ ] Success criteria are measurable (e.g., "8 cards sorted correctly")
- [ ] Each skill has clear prerequisite dependencies listed

#### Dependencies
- [ ] No circular dependencies (A→B, B→A)
- [ ] All T27 internal dependencies point to existing skills
- [ ] Cross-topic dependencies preserved (T24, T26, T21, etc.)
- [ ] Split skills updated everywhere (old ID → new sub-skill IDs)

#### Progression Logic
- [ ] Can complete each skill if prerequisites are mastered
- [ ] No sudden complexity jumps
- [ ] Bridge skills in place (especially G2.05)
- [ ] Sub-skills progress simple → complex

---

## Testing Protocol

### For Each New Skill:
1. **Read aloud** - Does it make sense without context?
2. **Check prerequisites** - Can students do this if they mastered dependencies?
3. **Simulate teaching** - Could you teach this in 20-30 minutes?
4. **Assess measurability** - Can you tell if a student succeeded?

### For Modified Skills:
1. **Compare before/after** - Is new version more specific?
2. **Check verb** - Is it active and testable?
3. **Success criteria** - Is there a clear "done" state?

### For Dependencies:
1. **Trace backwards** - Follow dependency chain to foundational skills
2. **Check cross-topic** - Verify T24, T26, T21 skills still exist
3. **Test order** - Arrange skills by dependencies, verify logical order

---

## Quick Reference: Where to Find Details

| Document | Purpose | Location |
|----------|---------|----------|
| **Optimization Plan** | Complete details, all skills | `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv5/T27_OPTIMIZATION_PLAN.md` |
| **Executive Summary** | Overview, skill counts, rationale | `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv5/T27_EXECUTIVE_SUMMARY.md` |
| **Before/After Examples** | Concrete examples of changes | `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv5/T27_BEFORE_AFTER_EXAMPLES.md` |
| **This Checklist** | Implementation steps | `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv5/T27_ACTION_CHECKLIST.md` |

---

## Skill Count Tracking

| Phase | Skills Added | Skills Modified | Skills Split | Total Count |
|-------|--------------|-----------------|--------------|-------------|
| Current | - | - | - | 63 |
| Phase 1 | 1 (G2.05) | 7 | 0 | 64 |
| Phase 2 | 3 (G4.08, G5.12, G6.12) | 0 | 1 (G5.04→2) | 68 |
| Phase 3 | 3 (G5.13, G7.08, G8.07) | 3 (K-2 enhanced) | 0 | 71 |
| Phase 4 | 2 (G4.09, G6.13) | 0 | 2 (G7.05→2, G8.01→2) | 78 |
| **TOTAL** | **9 new** | **10 modified** | **3 split (→6)** | **78** |

---

## Implementation Notes

### Priority Rationale
- **Phase 1 is urgent** because vague verbs make skills unassessable
- **G2.05 bridge is critical** - without it, G3 is too hard
- **Phase 2 fills conceptual gaps** that would confuse students
- **Phases 3-4 are enhancements** that add depth but aren't blocking

### Time Estimates
- Skill modification: ~20 minutes each (read, rewrite, test)
- New skill creation: ~30-40 minutes each (write, dependencies, test)
- Dependency updates: ~5 minutes each (find, update, verify)
- Verification: ~10 minutes per skill (check all criteria)

### Common Pitfalls to Avoid
1. **Don't skip verification** - Circular dependencies will break progression
2. **Don't batch dependency updates** - Update as you modify each skill
3. **Don't forget cross-topic checks** - T24/T26 dependencies must stay valid
4. **Don't rewrite descriptions from scratch** - Edit existing (preserves voice)

---

## Sign-Off Checklist

### Phase 1 Complete
- [ ] All 7 vague verbs fixed
- [ ] G2.05 bridge skill added and tested
- [ ] G3.01 dependencies updated
- [ ] Spot check: Pick 3 modified skills and verify they work

### Phase 2 Complete
- [ ] All 3 gap-filling skills added
- [ ] G5.04 split into 2 sub-skills
- [ ] All dependency updates completed
- [ ] Progression check: K→8 flows smoothly

### Phase 3 Complete
- [ ] All 3 AI-era skills added
- [ ] K-2 descriptions enhanced
- [ ] Cross-topic checks: T21 dependencies valid
- [ ] AI integration: Verify 3+ skills connect to AI concepts

### Phase 4 Complete
- [ ] G7.05 and G8.01 split
- [ ] Assessment skills added
- [ ] All dependencies updated for splits
- [ ] Final count: 78 skills confirmed

### Final Verification
- [ ] All 78 skills use active verbs
- [ ] No circular dependencies
- [ ] All success criteria are measurable
- [ ] K-8 progression tested
- [ ] AI-era readiness verified (training data, confidence, fairness, ethics)

---

**Ready to begin? Start with Phase 1, item 1: T27.GK.02**
