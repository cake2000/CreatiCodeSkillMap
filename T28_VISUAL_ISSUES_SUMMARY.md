# T28 Visual Issues Summary

**Analysis Date:** 2025-11-23
**Total Skills Analyzed:** 58 (G2-G8)
**Issues Found:** 18 items across 6 categories

---

## 📊 ISSUE DISTRIBUTION

```
Category                    Count  Priority
────────────────────────────────────────────
Missing Foundation (K-G1)     1     🔴 HIGH
Overly Broad/Complex          5     🔴 HIGH
CreatiCode Accuracy           1     🔴 HIGH
Description Quality          11     🟡 MED
Duplicates/Overlaps           0     ✅ NONE
Grade Appropriateness         0     ✅ GOOD
────────────────────────────────────────────
Total Issues                 18
```

---

## 🔴 HIGH PRIORITY ISSUES (3)

### Issue #1: Missing K-G1 Foundation
```
Problem:  Topic starts at G2 with no K or G1 skills
Impact:   Students lack intuitive foundation before formal concepts
Fix:      Add 6 new skills (3 for K, 3 for G1)
Effort:   2 hours
```

**Proposed K Skills:**
- K.01: Sort pictures by "always" or "sometimes"
- K.02: Predict what comes next in a pattern
- K.03: Experience randomness through picture games

**Proposed G1 Skills:**
- G1.01: Identify which events can or cannot happen
- G1.02: Record simple experiment results with pictures
- G1.03: Describe fairness in simple games

---

### Issue #2: G6.02 Random Seed Block - Unverified
```
Skill:    T28.G6.02 - Use random seeds for reproducibility
Problem:  Block 'data_setrandomlistseed' may only seed LISTS, not all randomness
Impact:   Skill description may promise more than block delivers
Fix:      Test block, update description if list-only
Effort:   30 minutes (test) + 15 minutes (update)
```

**Current Description Says:**
"Set a seed value before running a simulation, observe random outputs..."
→ Implies works with all random operations

**If Block is List-Only, Update To:**
"Use 'set random list seed to [value]' before shuffling a list..."
→ Clarifies scope accurately

---

### Issue #3: G3.05 Combines Too Many Concepts
```
Skill:    T28.G3.05 - Describe randomness in games and simulate
Problem:  Teaches analysis + coding + writing in one skill
Impact:   Too complex to assess; students may struggle with scope
Fix:      Break into 3 sub-skills
Effort:   1 hour
```

**Current (1 skill):**
- Identify game randomness
- Code simulation
- Explain luck vs skill

**Proposed (3 skills):**
- G3.05a: Identify randomness in familiar games
- G3.05b: Simulate a single game element
- G3.05c: Explain luck vs skill in games

---

## 🟡 MEDIUM PRIORITY ISSUES (15)

### Issue #4: Overly Broad Skills Needing Breakdown

```
┌─────────────┬──────────────────────────────────────┬───────────┐
│ Skill ID    │ Issue                                │ Action    │
├─────────────┼──────────────────────────────────────┼───────────┤
│ G3.05       │ Analysis + coding + writing          │ Split (3) │
│ G4.02.01-03 │ Sequential triplet (tight coupling)  │ Consider  │
│ G5.01.01-02 │ Generate + analyze (artificial gap)  │ Merge     │
│ G7.06.01-02 │ Unclear setup vs analysis split      │ Clarify   │
└─────────────┴──────────────────────────────────────┴───────────┘
```

**G3.05:** Already addressed above ✓

**G4.02.01-03:** Log → Count → Calculate %
- **Option A:** Merge into single comprehensive skill
- **Option B:** Keep for scaffolding (currently acceptable)
- **Decision:** Keep separate (but could go either way)

**G5.01.01-02:** Generate dice data → Analyze distribution
- **Recommendation:** Merge into single skill
- **Reason:** Part 2 cannot exist without Part 1; natural project flow

**G7.06.01-02:** Create multi-agent → Aggregate metrics
- **Recommendation:** Keep separate but clarify descriptions
- **Reason:** Good separation of setup vs measurement phases

---

### Issue #5-9: Vague Skill Descriptions (5 skills)

#### G4.03: "Stability differences" unclear
```
Current:  "...plot bar charts to see stability differences"
Problem:  What does "stability" mean? How measured?
Fix:      "...explain how 500-trial results are closer to expected
          percentages (less variable) than 50-trial results"
```

#### G5.02: "Function" terminology too advanced
```
Current:  "Learners write a function that tags each simulated user..."
Problem:  "Function" is advanced for G5; unclear context
Fix:      "Students create code that randomly assigns 100 participants
          to Group A or B using 'pick random 1 to 2'..."
```

#### G6.03: No guidance on "acceptable error"
```
Current:  "...stating whether the error is acceptable"
Problem:  No criteria provided for acceptability
Fix:      "They compare error to acceptable ranges (<10% good,
          >20% suggests bug) and explain why some error is normal"
```

#### G6.05: Missing randomness element
```
Current:  "Students create a sprite that tracks position..."
Problem:  No connection to "Chance & Simulations" topic
Fix:      Add: "They add random movement (50% forward, 25% left,
          25% right) and observe random walk pattern"
OR:       Move to T05 (Modeling & Simulation)
```

#### G7.06.01-02: Unclear distinction
```
Current:  Both skills describe multi-agent simulation work
Problem:  Not clear what's different between .01 and .02
Fix:      .01 emphasizes "setup and verification"
          .02 emphasizes "measurement and analysis"
```

---

### Issue #10: G5.08 Out of Sequence
```
Current Order:   G5.07 → G5.09 → G5.10 → G5.11 → G5.08
Expected Order:  G5.07 → G5.08 → G5.09 → G5.10 → G5.11
```

**Additional Problem:** G5.08 doesn't fit T28 focus
- Skill: "Track position and state for a single sprite"
- No randomness/simulation element
- Seems like prep for G6.05 (grid world agents)

**Recommendation:** Move to G6 as G6.04a (prerequisite)

---

### Issue #11-15: Description Improvements (6 more skills)

```
┌──────────┬───────────────────────────────┬──────────────────────┐
│ Skill    │ Current Issue                 │ Improvement Needed   │
├──────────┼───────────────────────────────┼──────────────────────┤
│ G3.03    │ "Copy table into notebook"    │ Clarify how/what     │
│ G4.04    │ "Duplicate entries"           │ Give specific example│
│ G5.04    │ "Simulation plan template"    │ Show template format │
│ G6.01.01 │ "Most balanced gameplay"      │ Define "balanced"    │
│ G6.06    │ "Changing probabilities"      │ Give concrete example│
│ G8.01    │ "Automated pipeline"          │ Clarify components   │
└──────────┴───────────────────────────────┴──────────────────────┘
```

These are lower priority but would benefit from more specific language.

---

## ✅ WHAT'S WORKING WELL

### Excellent Progression
```
G2: Physical experiments (spinners, coins, tallies)
    ↓
G3: Digital simulations (watch → modify → build)
    ↓
G4: Data collection + analysis (lists, frequencies, %)
    ↓
G5: Theoretical probability + Monte Carlo methods
    ↓
G6: Advanced techniques (seeds, parameters, conditional prob)
    ↓
G7: Multi-agent + AI fairness + ethics
    ↓
G8: Pipelines + pseudorandom + policy briefs
```

### Strong AI/Ethics Integration (G7-G8)
- ✅ Fairness testing with synthetic game testers
- ✅ Bias identification in random selection
- ✅ Model cards and documentation standards
- ✅ Simulation assumptions and limitations
- ✅ Policy briefs with ethical analysis
- ✅ Environment design bias analysis

### Good Cross-Topic Integration
- ✅ Uses T07 (Loops) for repeated trials
- ✅ Uses T08 (Conditionals) for outcome logic
- ✅ Uses T09 (Variables) for state tracking
- ✅ Uses T10 (Lists) for data collection
- ✅ Uses T27 (Data Analysis) for charts/statistics

### CreatiCode Feature Accuracy (Mostly Verified)
- ✅ `pick random` - confirmed available
- ✅ Chart types (line, bar, pie, percentage) - all available
- ✅ List operations (append, length, remove) - confirmed
- ✅ Statistical functions (sum, avg, median, mode) - available via T27
- ✅ List/table shuffle blocks - confirmed available
- ⚠️ `data_setrandomlistseed` - needs scope verification

---

## 📈 QUALITY TREND

```
Before Analysis: 58 skills (G2-G8 only)
Grade Coverage:  [--][--][✓✓][✓✓✓][✓✓✓][✓✓✓][✓✓][✓✓]
                  K   G1   G2   G3   G4   G5  G6  G7  G8
Quality Score:   B+ (Very Good)


After Fixes:     64 skills (K-G8 complete)
Grade Coverage:  [✓✓][✓✓✓][✓✓][✓✓✓][✓✓✓][✓✓✓][✓✓][✓✓]
                  K   G1   G2   G3   G4   G5  G6  G7  G8
Quality Score:   A- (Excellent)
```

---

## 🎯 IMPLEMENTATION ROADMAP

### Phase 1: Critical Fixes (2-3 hours)
```
✓ Add 6 K-G1 skills
✓ Verify G6.02 seed block
✓ Break G3.05 into 3 parts
✓ Merge G5.01.01-02
✓ Fix G5.08 placement

Impact: Fills foundation gap, ensures accuracy, improves assessability
```

### Phase 2: Important Updates (1-2 hours)
```
✓ Update 5 vague descriptions (G4.03, G5.02, G6.03, G6.05, G7.06)
✓ Review all G6+ dependency chains
✓ Add explicit T27 dependencies for charts

Impact: Improves clarity, ensures prerequisites are correct
```

### Phase 3: Polish (1 hour)
```
✓ Decide on G4.02 merger (keep or merge)
✓ Add list shuffle skill at G4 (optional)
✓ Standardize action verbs
✓ Add real-world contexts to G4-G5

Impact: Nice-to-have improvements, not critical
```

---

## 📋 CHECKLIST FOR IMPLEMENTATION

### Must Do (Phase 1)
- [ ] Write T28.K.01 (sort by always/sometimes)
- [ ] Write T28.K.02 (predict pattern)
- [ ] Write T28.K.03 (experience randomness)
- [ ] Write T28.G1.01 (identify possible/impossible)
- [ ] Write T28.G1.02 (record with pictures)
- [ ] Write T28.G1.03 (describe fairness)
- [ ] Test `data_setrandomlistseed` block in CreatiCode
- [ ] Update T28.G6.02 description based on test results
- [ ] Break T28.G3.05 into G3.05a, G3.05b, G3.05c
- [ ] Merge T28.G5.01.01 + G5.01.02 → G5.01
- [ ] Move T28.G5.08 to G6.04a (or add randomness)

### Should Do (Phase 2)
- [ ] Improve T28.G4.03 description (add specific measurements)
- [ ] Improve T28.G5.02 description (remove "function", add context)
- [ ] Improve T28.G6.03 description (add error formula)
- [ ] Improve T28.G6.05 description (add randomness or move to T05)
- [ ] Clarify T28.G7.06.01-02 distinction
- [ ] Review all G6+ skills for dependency clarity
- [ ] Add T27 chart dependencies where needed

### Nice to Have (Phase 3)
- [ ] Decide on G4.02.01-03 (merge or keep)
- [ ] Consider adding T28.G4.08 (list shuffle)
- [ ] Standardize action verbs across all descriptions
- [ ] Add more real-world application contexts

---

## 📊 FINAL METRICS

```
Category                      Before  After  Change
────────────────────────────────────────────────────
Total Skills                    58     64    +6
K Skills                         0      3    +3
G1 Skills                        0      3    +3
Overly Broad Skills              5      1    -4
Vague Descriptions              11      6    -5
Verified CreatiCode Blocks      95%   100%   +5%
Grade Appropriateness          Good   Excellent ↑
Overall Quality                 B+     A-     ↑
────────────────────────────────────────────────────
```

---

## 🏆 STRENGTHS TO CELEBRATE

1. **Outstanding AI/Ethics Content** (G7-G8)
   - Fairness testing, bias identification, model cards
   - Policy briefs with civic applications
   - Real-world ethical computing integration

2. **Strong Pedagogical Progression**
   - Hands-on → Digital → Theoretical
   - Concrete → Abstract
   - Simple → Complex

3. **Excellent Computational Thinking**
   - Debugging unfair simulations
   - Parameter testing (manual → automated)
   - Multi-agent systems
   - Data pipelines

4. **Good Cross-Topic Integration**
   - Leverages loops, conditionals, variables, lists
   - Uses data analysis and visualization skills
   - Connects to motion and modeling concepts

5. **Age-Appropriate Complexity**
   - G2: Physical experiments with pictographs
   - G3-G4: Basic coding and data collection
   - G5-G6: Theoretical probability and advanced techniques
   - G7-G8: Sophisticated applications and ethics

---

**Full Analysis:** `T28_COMPREHENSIVE_ANALYSIS_REPORT.md`
**Quick Reference:** `T28_QUICK_FIX_REFERENCE.md`
