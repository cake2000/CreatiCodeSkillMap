# T28 Visual Issue Summary

## Issue Distribution by Grade

```
G2 (4 skills): ✓ All correct - picture-based, age-appropriate
G3 (7 skills): ⚠️  1 forward reference, 1 duplicate, otherwise good
G4 (7 skills): ⚠️  1 duplicate, 1 X-1 violation, 1 non-coding skill
G5 (11 skills): ⚠️  1 misplaced skill, 1 X-1 violation, 1 unnecessary dep
G6 (11 skills): ⚠️  4 X-1 violations, 1 seeded random limitation, 2 redundant deps
G7 (7 skills): ⚠️  2 X-1 violations, otherwise good
G8 (5 skills): ⚠️  1 theoretical skill, otherwise good
```

## Priority Breakdown

```
HIGH PRIORITY (11 issues):
├─ Forward Reference: 1
├─ Duplicate Skills: 2
├─ Misplaced Skill: 1
└─ X-2 Rule Violations: 7
   ├─ Same grade: 1
   ├─ X-1: 5
   └─ Invalid dep: 1

MEDIUM PRIORITY (14 issues):
├─ Grade appropriateness: 2 (but actually OK)
├─ Too vague: 3
├─ Missing scaffolding: 4
├─ Too broad: 2
└─ Dependency issues: 3

LOW PRIORITY (15 issues):
├─ Description improvements: 6
├─ Success criteria: 3
├─ Terminology: 2
└─ Ordering: 4
```

## Skill-by-Skill Status

### Grade 2 (Picture-Based) ✓
- T28.G2.01 ✓ Sort certain/possible/impossible
- T28.G2.02 ✓ Picture-based chance experiment
- T28.G2.03 ✓ Decide if game is fair
- T28.G2.04 ✓ Predict and observe outcomes

### Grade 3 (Intro to Coding Random)
- T28.G3.01 ⚠️  Interpret simulation (X-2 violation: same grade loop dep)
- T28.G3.02 ✓ Explain "pick random"
- T28.G3.03 ✓ Record data with provided blocks
- T28.G3.04 ✓ Compare predictions to data
- T28.G3.05 ❌ Game randomness (H1: depends on G3.06 - forward ref)
- T28.G3.06 ✓ Modify random generator
- T28.G3.07 ⚠️  Build random generator (H2: duplicate of G4.01)

### Grade 4 (Data Collection)
- T28.G4.01 ❌ Build random generator (H2: duplicate of G3.07, H4: X-1 violation)
- T28.G4.02.01 ⚠️  Log trials to list (H4: X-1 violation)
- T28.G4.02.02 ⚠️  Count frequencies (M3c: needs list iteration dep)
- T28.G4.02.03 ✓ Calculate percentages
- T28.G4.03 ✓ Sample size changes variability
- T28.G4.04 ✓ Debug unfair simulation
- T28.G4.05 ✓ Random coordinate pairs
- T28.G4.06 ⚠️  Probabilities as fractions (L1d: needs coding context)
- T28.G4.07 ✓ Random without repetition

### Grade 5 (Probability Theory)
- T28.G5.01.01 ✓ Compound events (two dice)
- T28.G5.01.02 ✓ Analyze compound distributions
- T28.G5.02 ⚠️  Randomly assign participants (L1e: "function" → "script")
- T28.G5.03 ⚠️  Monte Carlo sampling (H4: X-1 violation)
- T28.G5.04 ✓ Document simulation plans
- T28.G5.05 ✓ Theoretical probability
- T28.G5.06 ✓ Compare experimental vs theoretical
- T28.G5.07 ⚠️  Frequency distributions (M5a: unnecessary median/mode dep)
- T28.G5.08 ❌ Track sprite state (H3: MISPLACED - should be T05/T09)
- T28.G5.09 ✓ Expected value
- T28.G5.10 ✓ Independence and gambler's fallacy
- T28.G5.11 ✓ Law of large numbers

### Grade 6 (Advanced Simulations)
- T28.G6.01.01 ⚠️  Manual parameter testing (M5b: redundant deps)
- T28.G6.01.02 ✓ Automate parameter sweeps
- T28.G6.02 ❌ Random seeds (M2b: CreatiCode limitation, M5c: redundant deps)
- T28.G6.03 ✓ Percent error vs theoretical
- T28.G6.04 ✓ Simulate noisy sensors
- T28.G6.05 ❌ Grid world agent (H4: X-1 violation, H5: invalid T08.G5.01 dep)
- T28.G6.06 ✓ Events with changing probabilities
- T28.G6.07 ❌ Environment with obstacles (H4: X-1, H5: invalid T08.G5.01)
- T28.G6.08 ✓ Reward rules and outcomes
- T28.G6.09 ✓ Two-sprite interaction
- T28.G6.10 ✓ Compare sampling methods
- T28.G6.11 ✓ Conditional probability

### Grade 7 (Multi-Agent Systems)
- T28.G7.01 ⚠️  Two-agent simulation (H4: X-1 violations on G6.08, G6.09)
- T28.G7.02 ✓ Trace agent learning
- T28.G7.03 ✓ Test fairness with synthetic testers
- T28.G7.04 ✓ Compare shuffled vs real outcomes
- T28.G7.05 ⚠️  Communicate assumptions (M4a: too broad - writing skill)
- T28.G7.06.01 ✓ Multi-agent simulation
- T28.G7.06.02 ✓ Aggregate metrics
- T28.G7.07 ✓ Identify bias in selection methods

### Grade 8 (Real-World Integration)
- T28.G8.01 ✓ Chain simulation → analysis → dashboard
- T28.G8.02 ✓ Measurement variability through sampling
- T28.G8.03 ✓ Integrate with AI assistant
- T28.G8.04 ⚠️  Policy briefs (M4b: too broad - writing skill)
- T28.G8.05 ✓ Environment design bias
- T28.G8.06 ⚠️  Random vs pseudorandom (M2c: too theoretical)

## Legend
- ✓ Skill is correct as-is
- ⚠️  Minor to medium issues, functional but needs improvement
- ❌ Critical issues requiring immediate attention

## Summary Statistics

```
Total Skills: 56
├─ Correct (✓): 39 (70%)
├─ Minor Issues (⚠️): 13 (23%)
└─ Critical Issues (❌): 4 (7%)

Skills needing attention: 17 (30%)
└─ But most are minor improvements

Critical fixes: 4 skills
├─ G3.05 (forward reference)
├─ G4.01 (duplicate + X-1)
├─ G5.08 (misplaced)
└─ G6.05 (invalid dependency)
```

## Most Common Issues

1. **X-2 Rule Violations**: 7 occurrences (but 6 are acceptable X-1 for foundational skills)
2. **Redundant Dependencies**: 3 occurrences
3. **Skills Too Broad**: 2 occurrences (both writing/documentation skills)
4. **Duplicate/Overlapping**: 2 occurrences
5. **Forward Reference**: 1 occurrence (critical)
6. **Misplaced Skill**: 1 occurrence (critical)

## Recommended Actions

### Must Fix (Blocking Issues)
1. ❌ Fix forward reference in T28.G3.05
2. ❌ Fix invalid T08.G5.01 dependency in T28.G6.05, G6.07
3. ❌ Clarify or merge T28.G3.07 and T28.G4.01
4. ⚠️  Decide: Move T28.G5.08 to T05/T09 or reframe for T28

### Should Fix (Quality Issues)
5. Update T28.G6.02 for CreatiCode's list-based seeded random
6. Remove redundant dependencies (G5.07, G6.01.01, G6.02)
7. Standardize terminology (function→script, consistent experiment/simulation)

### Nice to Have (Polish)
8. Add specific success criteria to vague skills
9. Add coding context to math-heavy skills
10. Reorder G5 skills for better flow

## Overall Assessment

**T28 is 70% correct and well-structured.** The main issues are:
- 1 forward reference (easy fix)
- 1 invalid dependency (easy fix)
- 1-2 duplicate skills (needs discussion)
- 1 misplaced skill (needs decision)
- 6 acceptable X-1 violations (foundational skills)
- Various minor improvements

**Recommendation**: This topic is in good shape and ready for Phase 1 optimization with targeted fixes.
