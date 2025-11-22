# T28 (Chance & Simulations) Optimization - Executive Summary

## Scope
**Topic**: T28 – Chance & Simulations: G2–8 Skill List
**Location**: /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md, lines 14792-15247
**Current Skills**: 41 skills across 7 grade levels (G2-G8)
**Analysis Date**: 2025-11-22

---

## Overall Assessment

**Internal Coherence: GOOD (7/10)** with significant opportunities for improvement

### Strengths ✓
- Clear progression from unplugged (G2) to sophisticated multi-agent simulations (G8)
- Appropriate grade-level positioning for most skills
- Good connection to real-world applications (game balance, fairness testing, policy analysis)
- Leverages CreatiCode platform capabilities effectively in most areas
- Strong integration with complementary topics (T27 Data Viz, T10 Lists, T23 AI)

### Weaknesses ✗
- **5 critical scaffolding gaps** where students face significant difficulty jumps
- **4 overly broad skills** that combine multiple learning objectives (assessment confusion)
- **12 vague descriptions** reducing assessability
- **7 important probability concepts** not explicitly addressed
- Some redundant dependencies cluttering specifications

---

## Issues by Priority

### HIGH PRIORITY: 24 Issues

| Category | Count | Impact |
|----------|-------|--------|
| **Missing Scaffolding** | 5 | Students struggle to progress; retention issues |
| **Skills Too Broad** | 4 | Cannot diagnose student difficulties; combines 2-4 concepts each |
| **CreatiCode Mismatches** | 5 | Students miss platform features or use incorrectly |
| **Grade-Inappropriate Content** | 2 | Minor; G2 needs more explicit unplugged focus |
| **Dependency Violations** | 1 | Redundant specification (T28.G3.06) |
| **Duplicates/Redundancies** | 2 | Actually appropriate progressions; KEEP |
| **X-2 Rule Violations** | 0 | ✓ All cross-grade dependencies within acceptable range |

### MEDIUM PRIORITY: 21 Issues

| Category | Count | Impact |
|----------|-------|--------|
| **Vague Descriptions** | 8 | Reduces teacher clarity; harder to assess |
| **Missing Explicit Coverage** | 7 | Important concepts taught implicitly or not at all |
| **Unnecessary Dependencies** | 4 | Over-specified; creates confusion |
| **Unnecessary Same-Grade Deps** | 2 | Clutters skill definitions |

---

## Recommended Changes

### 1. New Skills to Add: 9

#### Critical Scaffolding Skills (4)
- **T28.G3.07**: Assemble a random generator from provided blocks *(bridges modify→build gap)*
- **T28.G4.06**: Interpret simple probabilities from familiar contexts *(conceptual foundation before calculation)*
- **T28.G5.08**: Track a sprite's state across multiple events *(foundation for agent modeling)*
- **T28.G6.09**: Create a simple two-sprite random interaction *(scaffolds multi-agent systems)*

#### Important Missing Concepts (5)
- **T28.G4.07**: Use seeds to reproduce random sequences *(debugging tool when first needed)*
- **T28.G5.09**: Use random selection without repetition *(platform feature; essential for realistic sims)*
- **T28.G5.10**: Test independence of random trials *(addresses gambler's fallacy)*
- **T28.G6.10**: Calculate and compare expected values *(practical decision-making)*
- **T28.G7.07**: Identify sources of sampling bias *(data literacy)*

### 2. Skills to Split into Sub-skills: 4 → 11

#### T28.G4.02 → 3 sub-skills
Current: "Log 50 trials into a list and compute frequencies"
- **T28.G4.02.01**: Log trial results into a list
- **T28.G4.02.02**: Count frequencies from a list
- **T28.G4.02.03**: Calculate percentages from counts

#### T28.G5.01 → 2 sub-skills
Current: "Simulate compound events (two dice)"
- **T28.G5.01.01**: Generate and sum two random values
- **T28.G5.01.02**: Collect and analyze compound event data

#### T28.G6.01 → 2 sub-skills
Current: "Conduct parameter sweeps for tuning"
- **T28.G6.01.01**: Test multiple parameter values manually
- **T28.G6.01.02**: Automate parameter sweeps with loops

#### T28.G7.06 → 2 sub-skills
Current: "Build multi-agent simulations with aggregated metrics"
- **T28.G7.06.01**: Create multiple agent instances
- **T28.G7.06.02**: Track and display aggregate statistics

### 3. Skills Needing Description Enhancements: 12

**Make more concrete/assessable:**
- T28.G2.02, T28.G2.04 (clarify unplugged methods)
- T28.G3.01, T28.G3.05 (add specific deliverables)
- T28.G5.04, T28.G5.06 (add explicit terminology)
- T28.G6.04, T28.G6.06 (clarify technical details)
- T28.G7.02, T28.G7.05 (specify worksheet/rubric)
- T28.G8.01, T28.G8.03 (break down vague capstone into steps)

### 4. Dependency Fixes: 7 skills

**Remove redundancies:**
- T28.G3.06 (remove T28.G3.02; covered by G3.03)
- T28.G4.01 (remove T07.G3.05, T09.G3.05; not used)
- T28.G4.03 (remove T08.G3.01, T09.G3.05; redundant)
- T28.G6.01, T28.G6.03 (simplify variable dependencies)
- T28.G7.01 (remove T07.G6.05; replace with general loop)

**Add missing dependencies:**
- T28.G5.03 (add T08.G4.01 for boundary checking)

---

## Implementation Impact

### Before Optimization
- **41 skills** total
- **5 major scaffolding gaps** causing student struggle
- **4 skills** conflate multiple concepts
- **12 vague descriptions** reducing clarity
- **7 concepts** missing explicit coverage

### After Optimization
- **~53-56 skills** total (41 original + 9 new + 4 split into 11 = net +13 to +16)
- **0 scaffolding gaps** - smooth progression at each level
- **All skills** assess single clear concept
- **All descriptions** concrete and assessable
- **Comprehensive coverage** of probability/simulation concepts

### Student Impact
- ✅ **Clearer progression**: Each skill builds logically on previous
- ✅ **Higher success rate**: Appropriate scaffolding at transitions
- ✅ **Deeper understanding**: Important concepts explicitly taught
- ✅ **More powerful tools**: Platform features taught systematically
- ✅ **Real-world connections**: Explicit links to AI fairness, civic data

### Teacher Impact
- ✅ **Easier diagnosis**: Narrow skills pinpoint student difficulties
- ✅ **Clearer assessment**: Concrete deliverables specified
- ✅ **Better alignment**: Explicit probability concepts match standards
- ✅ **Richer examples**: Detailed descriptions show what success looks like

---

## Skill Count by Grade (After Optimization)

| Grade | Current | After Split | New Skills | Total | Change |
|-------|---------|-------------|------------|-------|--------|
| G2 | 4 | 4 | 0 | 4 | 0 |
| G3 | 6 | 6 | +1 (G3.07) | 7 | +1 |
| G4 | 5 | 8 (G4.02→3) | +2 (G4.06, G4.07) | 10 | +5 |
| G5 | 7 | 8 (G5.01→2) | +3 (G5.08, G5.09, G5.10) | 11 | +4 |
| G6 | 8 | 9 (G6.01→2) | +2 (G6.09, G6.10) | 11 | +3 |
| G7 | 6 | 8 (G7.06→2) | +1 (G7.07) | 9 | +3 |
| G8 | 5 | 5 | 0 | 5 | 0 |
| **TOTAL** | **41** | **48** | **+9** | **57** | **+16** |

**Note**: Some splits involve renumbering (G4.02 becomes G4.02.01-.03), so "after split" count includes original skill IDs that get subdivided.

---

## Priority Ranking for Implementation

### PHASE 1: Critical Fixes (1-2 hours)
**Immediate impact; no downstream complications**

1. Fix dependency redundancies (7 skills)
2. Enhance vague descriptions (12 skills)
3. Clarify unplugged methods (2 G2 skills)

**Deliverable**: Cleaner, clearer existing skills

---

### PHASE 2: Fill Scaffolding Gaps (2-3 hours)
**Highest student impact; enables progression**

4. Add T28.G3.07 (assemble generator) - *critical G3→G4 bridge*
5. Add T28.G4.06 (interpret probabilities) - *conceptual foundation*
6. Add T28.G5.08 (state tracking) - *agent modeling foundation*
7. Add T28.G6.09 (two-sprite interaction) - *multi-agent bridge*

**Deliverable**: Smooth progression, reduced struggle

---

### PHASE 3: Split Complex Skills (3-4 hours)
**Assessment clarity; diagnostic power**

8. Split T28.G4.02 into .01, .02, .03
9. Split T28.G5.01 into .01, .02
10. Split T28.G6.01 into .01, .02
11. Split T28.G7.06 into .01, .02
12. Update 11 downstream dependencies

**Deliverable**: Independent assessment of each concept

---

### PHASE 4: Advanced Concepts (2-3 hours)
**Comprehensive coverage; enrichment**

13. Add T28.G4.07 (seeds for debugging)
14. Add T28.G5.09 (random without repetition)
15. Add T28.G5.10 (independence/gambler's fallacy)
16. Add T28.G6.10 (expected value)
17. Add T28.G7.07 (sampling bias)

**Deliverable**: Complete probability/simulation curriculum

---

## Total Effort Estimate

**Phase 1**: 1-2 hours (text edits only)
**Phase 2**: 2-3 hours (write 4 new skills)
**Phase 3**: 3-4 hours (split 4 skills, update references)
**Phase 4**: 2-3 hours (write 5 new skills)

**TOTAL: 8-12 hours** for complete T28 optimization

---

## Risk Assessment

### Low Risk ✓
- Dependency fixes (improve clarity, no functionality change)
- Description enhancements (same skills, better specified)
- New scaffolding skills (fill gaps without disrupting existing)

### Medium Risk ⚠
- Splitting skills (requires updating downstream dependencies)
  - **Mitigation**: Systematic search-and-replace for each split ID
  - **Affected skills**: 11 downstream skills need updates

### No High Risks Identified

---

## Success Metrics

### Quantitative
- [ ] All 57 skills have concrete, assessable descriptions
- [ ] No X-2 rule violations
- [ ] No circular dependencies within T28
- [ ] Zero redundant same-skill dependencies
- [ ] All grade levels maintain K-2 unplugged, G3+ coding requirement

### Qualitative
- [ ] Smooth conceptual progression G2→G8 (no sudden jumps)
- [ ] Each skill assesses single clear concept
- [ ] All core probability concepts explicitly addressed
- [ ] Platform features taught systematically
- [ ] Real-world applications integrated throughout

---

## Cross-Topic Dependencies (To verify in Phase 2)

T28 correctly depends on:
- **T27** (Data Visualization): 4 skills for charts
- **T10** (Lists & Tables): 8 skills for data structures
- **T09** (Variables): 15 skills for state tracking
- **T08** (Conditionals): 12 skills for simulation logic
- **T07** (Loops): 18 skills for repeated trials
- **T06** (Events): 6 skills for multi-sprite coordination
- **T05** (Simulation Design): 3 skills for planning
- **T03** (Motion): 2 skills for coordinates
- **T01** (Sequences): 2 skills for basic logic

**Note**: These cross-topic dependencies are appropriate and should be preserved. They will be verified in Phase 2 (cross-topic dependency analysis).

---

## Conclusion

**T28 is fundamentally sound but needs refinement.** The topic has a clear vision (unplugged → observation → building → advanced applications) and good real-world connections. However:

1. **Critical gaps** in G3→G4 and G5→G6 transitions impede student progress
2. **Overly broad skills** in G4-G7 reduce diagnostic power
3. **Vague G8 descriptions** make capstone projects unclear
4. **Important concepts** (independence, expected value, sampling bias) missing

**Recommendation: Proceed with 4-phase optimization.**

After optimization, T28 will provide:
- Smooth, well-scaffolded progression through probability and simulation concepts
- Clear assessment criteria at each level
- Comprehensive coverage of standards-aligned probability concepts
- Systematic introduction to CreatiCode platform capabilities
- Strong preparation for AI fairness and data literacy in upper grades

**Estimated effort: 8-12 hours for complete optimization**
**Impact: High - fixes fundamental progression issues and fills important conceptual gaps**
