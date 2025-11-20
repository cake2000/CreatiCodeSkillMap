# G5 Fixes - Quick Reference Table

**Quick lookup table for all 28 G5 skill fixes**

| Skill ID | Skill Name | Remove | Add | Type |
|----------|------------|--------|-----|------|
| T03.G5.01 | Create a feature list and subtask breakdown | T03.G1.02 | T03.G3.01 | Simple |
| T03.G5.03 | Identify task dependencies in a project plan | T03.G1.02 | T03.G3.01 | Simple |
| T03.G5.04 | Flag high-risk or unclear tasks | T03.G1.02 | T03.G3.01 | Simple |
| T05.G5.01 | Write clear user needs and requirements for a small app | T05.G1.02, T05.GK.03 | T05.G3.01 | Complex |
| T05.G5.02 | Create a low-fidelity sketch for a user story | T05.G1.02, T05.GK.03 | T05.G3.01 | Complex |
| T05.G5.03 | Identify variables and initial values for a simulation | T05.GK.03 | - | Transitive |
| T05.G5.04 | Draft simple update rules for a simulation | T05.GK.03 | - | Transitive |
| T05.G5.05 | Plan how to test whether a design meets user needs | T04.G2.01, T05.G1.01, T05.GK.03 | T04.G3.01, T05.G3.01 | Complex |
| T05.G5.06 | Plan what to measure in a simulation experiment | T05.G1.02, T05.GK.03 | T05.G3.01 | Complex |
| T12.G5.02 | Document code functionality and choices | T12.G1.01 | T12.G3.01 | Simple |
| T13.G5.04 | Modify a program to improve reliability and correctness | T13.G1.01 | T13.G4.01 | Simple |
| T25.G5.01 | Model multi-type game state | T25.G1.01, T25.GK.02 | T25.G3.01 | Complex |
| T25.G5.02 | Convert messy inputs into canonical formats | T25.G1.01, T25.GK.02 | T25.G3.01 | Complex |
| T25.G5.03 | Decide when to upgrade from list to table | T25.G1.01, T25.G1.02, T25.GK.02 | T25.G3.01 | Complex |
| T30.G5.01 | Match CreatiCode AI features to hardware requirements | T30.G1.01, T30.G1.02, T30.GK.02 | T30.G3.01 | Complex |
| T30.G5.02 | Plan safe device-handling procedures for group work | T30.G1.01, T30.G1.02, T30.GK.02 | T30.G3.01 | Complex |
| T30.G5.03 | Explain how different sensors collect data | T30.GK.02 | - | Transitive |
| T30.G5.04 | Relate hardware choices to accessibility outcomes | T30.G1.01, T30.G1.02, T30.GK.02 | T30.G3.01 | Complex |
| T31.G5.02 | Decide when apps need the internet vs work offline | T31.G5.01 | - | Same-Grade |
| T32.G5.01 | Analyze social engineering tactics | T32.G1.01, T32.G1.02 | T32.G3.01 | Complex |
| T32.G5.02 | Evaluate terms of service/privacy policies (kid-friendly summaries) | T32.G1.01, T32.G1.02 | T32.G3.01 | Complex |
| T32.G5.03 | Secure AI training data and outputs | T32.G1.01, T32.G1.02 | T32.G3.01 | Complex |
| T34.G5.02 | Compare invention timelines in multiple industries | T34.G1.01, T34.G1.02 | T34.G3.01 | Complex |
| T34.G5.03 | Conduct interviews with tech users | T34.G1.01, T34.G1.02 | T34.G3.01 | Complex |
| T35.G5.01 | Examine global impacts of technology | T35.G1.01, T35.G1.02 | T35.G3.01 | Complex |
| T35.G5.02 | Debate digital well-being scenarios | T35.G1.01, T35.G1.02 | T35.G3.01 | Complex |
| T35.G5.03 | Analyze AI's differential impacts on workers and communities | T04.G2.01, T35.G1.01 | T04.G3.01, T35.G3.01 | Complex |
| T36.G5.03 | Evaluate inclusion in tech stories | T36.G1.01, T36.G1.02 | T36.G3.01 | Complex |

## Legend

**Type:**
- **Simple:** 1:1 replacement, no transitive issues (7 skills)
- **Complex:** Multiple changes or transitive cleanup (17 skills)
- **Transitive:** Only transitive dependency removal (3 skills)
- **Same-Grade:** Same-grade dependency removal (1 skill)

## By Type Summary

| Type | Count | Effort | Risk |
|------|-------|--------|------|
| Simple | 7 | Low | Low |
| Transitive | 3 | Very Low | Very Low |
| Same-Grade | 1 | Low | Low |
| Complex | 17 | Medium | Medium |
| **Total** | **28** | - | - |

## Implementation Order

### Phase 1: Quick Wins (4 skills, ~2 hours)
1. T05.G5.03 (transitive only)
2. T05.G5.04 (transitive only)
3. T30.G5.03 (transitive only)
4. T31.G5.02 (same-grade)

### Phase 2: Simple (7 skills, ~4 hours)
1. T03.G5.01, T03.G5.03, T03.G5.04
2. T12.G5.02
3. T13.G5.04

### Phase 3: Complex (17 skills, ~12 hours)
All remaining skills with multiple changes

## Cross-Reference

For full details on any skill, see:
- **G5_FIX_PLAN.md** - Complete specifications
- **G5_FIX_PLAN.json** - Machine-readable data

---

**Quick Tip:** Search for skill ID in G5_FIX_PLAN.md for complete details including rationale and validation.
