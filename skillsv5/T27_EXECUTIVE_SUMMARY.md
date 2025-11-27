# T27 Optimization - Executive Summary

## Overview
Analyzed and optimized T27 (Chance & Simulations) from 63 skills to 78 skills, addressing vague verbs, progression gaps, and AI-era readiness.

## Key Improvements

### 1. Fixed Vague Verbs (7 skills modified)
**Problem:** Skills used passive verbs like "identify," "classify," "explain"
**Solution:** Replaced with active verbs + verification

Examples:
- T27.GK.02: "Identify maybe events" → "**Select** maybe events and **test** predictions"
- T27.G3.01: "Read and explain" → "**Compare** to predictions and **calculate** differences"
- T27.G5.10: "Identify independent events" → "**Test** independence by tracking streaks"

### 2. Enhanced K-2 Concrete Scenarios (3 skills)
**Problem:** Descriptions used vague "illustrated picture cards"
**Solution:** Added specific examples and material lists

Example (T27.GK.01):
- Before: "6-8 illustrated picture cards..."
- After: "8 cards showing: sun coming up, ball falling, ice melting, plant needing water (certain) vs. fish flying, ice staying frozen in hot sun, jumping to moon, water flowing uphill (impossible)"

### 3. Filled 5 Critical Progression Gaps

| Gap | Location | Solution |
|-----|----------|----------|
| G2→G3 too large | Physical coins → bar charts | **New T27.G2.05**: Watch CreatiCode spinner (bridge) |
| Missing visual probability | G4 frequencies → G5 theory | **New T27.G4.08**: Draw area models (pie charts) |
| No combinations coverage | G5 compound → G7 multi-agent | **New T27.G6.12**: Tree diagrams, organized lists |
| Missing variance concept | G5 expected value → G8 bootstrap | **New T27.G5.12**: Calculate mean & spread |
| Limited assessment skills | Scattered debugging | **New G4.09, G6.13**: Test reliability, edge cases |

### 4. Added AI-Era Depth (3 new skills)
- **T27.G5.13**: Generate synthetic training data (understand datasets)
- **T27.G7.08**: Simulate AI confidence scores (test thresholds)
- **T27.G8.07**: Compare random vs. guided search (Monte Carlo tree search intro)

### 5. Split Overly Broad Skills (3 → 6 sub-skills)
- T27.G5.04 → G5.04.01 (define question/variables) + G5.04.02 (choose model/criteria)
- T27.G7.05 → G7.05.01 (document assumptions) + G7.05.02 (identify stakeholders)
- T27.G8.01 → G8.01.01 (automate data collection) + G8.01.02 (build dashboard)

## Updated Skill Counts

| Grade | Before | After | Change | Key Additions |
|-------|--------|-------|--------|---------------|
| GK | 3 | 3 | 0 | (Enhanced descriptions) |
| G1 | 3 | 3 | 0 | (Enhanced descriptions) |
| G2 | 4 | 5 | +1 | G2.05 (CreatiCode bridge) |
| G3 | 7 | 7 | 0 | (Fixed vague verbs) |
| G4 | 7 | 9 | +2 | G4.08 (area models), G4.09 (test reliability) |
| G5 | 11 | 14 | +3 | G5.12 (variance), G5.13 (training data), split G5.04 |
| G6 | 11 | 13 | +2 | G6.12 (combinations), G6.13 (edge cases) |
| G7 | 7 | 9 | +2 | G7.08 (AI confidence), split G7.05 |
| G8 | 6 | 8 | +2 | G8.07 (Monte Carlo), split G8.01 |
| **Total** | **63** | **78** | **+15** | |

## What We DIDN'T Change

### No Skills Removed
All existing skills serve distinct purposes. Apparent "duplicates" are actually intentional progressions:
- Fairness appears in G2 (intuitive), G4 (debugging), G7 (systematic testing) - all necessary
- Parameter testing in G6.01.01 (manual) → G6.01.02 (automated) - clear progression

### Preserved Dependencies
All cross-topic dependencies maintained exactly:
- T24 (data collection with tally marks)
- T26 (charts and statistics)
- T21 (AI features)
- T09, T10 (variables and lists)
- T06, T07, T08 (control structures)

## Implementation Phases

### Phase 1: Critical Fixes (2-3 hours)
- Fix 7 vague verbs
- Add G2.05 bridge skill
- Update dependencies

### Phase 2: Fill Gaps (4-5 hours)
- Add G4.08, G5.12, G6.12
- Split G5.04 into sub-skills
- Update dependencies

### Phase 3: AI Enhancements (3-4 hours)
- Add G5.13, G7.08, G8.07
- Enhance K-2 descriptions

### Phase 4: Advanced (3-4 hours)
- Split G7.05, G8.01
- Add G4.09, G6.13
- Final dependency review

## Quality Verification

### Verb Audit Results
✓ Active verbs: Select, Match, Trace, Compare, Test, Predict, Calculate, Build, Debug
✗ Removed: Identify, Understand, Appreciate, Explore (when used passively)

### Progression Check
✓ K-2: Picture-based, concrete materials, specific examples
✓ G3-4: Smooth unplugged→digital transition via G2.05 bridge
✓ G5-6: Theory + practice integrated (calculate theoretical, then simulate)
✓ G7-8: Professional workflows (multi-agent, fairness, AI, documentation)

### AI-Era Readiness
✓ Training data generation (G5.13)
✓ Confidence scores & thresholds (G7.08)
✓ Fairness & bias testing (G7.03, G7.07, G8.05)
✓ Monte Carlo methods (G8.07)
✓ Ethical considerations (G7.05.02, G8.04)
✓ AI tool integration (G8.03)

### IXL-Style Quality
✓ Auto-gradable: "Sort 8 cards correctly" (not "explore sorting")
✓ Immediate feedback: Run simulation → compare to prediction
✓ Micro-steps: G5.04 split into 2 skills (question/variables, then model/criteria)
✓ Clear outcomes: "Calculate percent error" (not "understand accuracy")

## Key Takeaways

1. **No major restructuring needed** - T27 already had solid foundation
2. **Verb precision matters** - Changing "identify" to "select and test" makes skills assessable
3. **Bridge skills are critical** - G2.05 prevents the "cliff" from physical to digital
4. **AI integration throughout** - Not just one "AI unit" but woven into G5-G8
5. **Sub-skills enable mastery** - Breaking broad skills like G5.04 into steps prevents overwhelming students

## Next Steps

1. Review and approve Phase 1 changes (critical fixes)
2. Test G2.05 bridge skill with sample implementation
3. Validate new skill dependencies don't create circular references
4. Prepare detailed implementation guides for new skills (G4.08, G5.12, etc.)
5. Create assessment rubrics for modified skills with active verbs

---

**Document Location:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv5/T27_OPTIMIZATION_PLAN.md`

**Full Details:** See optimization plan for complete skill descriptions, dependencies, and rationale.
