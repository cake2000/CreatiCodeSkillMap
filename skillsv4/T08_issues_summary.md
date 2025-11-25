# T08 Conditions & Logic - Issues Summary

## Overview
**Grade: B- → A- (after fixes)**

55 skills analyzed, 7 critical issues found, 40+ redundant dependencies identified

---

## Critical Issues Found

### 🔴 ISSUE #1: Grade 4 Dependency Bloat (HIGHEST PRIORITY)
**Severity**: Critical
**Affected Skills**: 9 skills (T08.G4.01, G4.02, G4.03, G4.04, G4.05, G4.06, G4.07, G4.08, G4.09)
**Problem**: 40+ unnecessary G2 dependencies violating X-2 rule

**Example - T08.G4.02 (Combine two conditions with OR):**
```
Current: 9 dependencies (5 from G2!)
├─ T04.G2.01 ❌ (Pattern recognition - irrelevant)
├─ T04.G2.02 ❌ (Algorithms - irrelevant)
├─ T06.G2.01 ❌ (Cause-effect - assumed in G3)
├─ T06.G2.02 ❌ (Multiple triggers - assumed in G3)
├─ T06.G2.03 ❌ (Game rules - assumed in G3)
├─ T06.G3.01 ❌ (Green flag - assumed in G3)
├─ T07.G2.01 ❌ (Repeat vs do once - assumed in G3)
├─ T08.G4.01 ✅ (Prerequisite: AND operator)
└─ T09.G3.01.04 ✅ (Variables - needed)

Proposed: 2 dependencies
├─ T08.G4.01c (Distinguish AND vs OR scenarios)
└─ T09.G3.01.04 (Display variable value)
```

**Impact**:
- Maintenance nightmare (changes to G2 break G4)
- Cognitive overload (students don't need 9 prerequisites)
- X-2 rule violation (G4 reaching back to G2)

**Fix**: Remove all G2 dependencies that are already assumed through G3 progression

---

### 🔴 ISSUE #2: Missing Critical Dependency (BUG)
**Severity**: Critical
**Affected Skills**: T08.G4.06 (Convert nested if to cleaner logic)
**Problem**: Skill about refactoring nested code doesn't depend on the nesting skill!

```
T08.G4.06: Convert nested if to cleaner logic
Current Dependencies:
├─ T06.G2.01 (Cause-effect chains) ❌
├─ T06.G2.02 (Multiple triggers) ❌
├─ T07.G2.01 (Repeat vs do once) ❌
├─ T08.G4.01 (Combine AND) ✅
├─ T08.G4.02 (Combine OR) ✅
└─ T08.G4.05 (Use else-if) ✅

MISSING: T08.G4.04 (Nest if/else statements) ❌❌❌

How can you refactor nested code if you haven't learned to nest?
```

**Fix**: Add T08.G4.04 as dependency, remove G2 bloat

---

### 🔴 ISSUE #3: Wrong Dependency Reference
**Severity**: Critical
**Affected Skills**: T08.G5.00 (Draw decision tree flowchart)
**Problem**: Depends on sequential box diagram skill instead of branching diagram skill

```
T08.G5.00: Draw decision tree flowchart
Current:
└─ T02.G2.01: Turn a picture routine into labeled boxes
   (This is about SEQUENTIAL steps, not BRANCHING decisions!)

Should be:
└─ T08.G2.01: Follow branching paths based on yes/no questions
   (This is about BRANCHING logic - the actual prerequisite!)
```

**Fix**: Replace T02.G2.01 → T08.G2.01

---

### 🟡 ISSUE #4: Missing Conceptual Bridge (K-2 to G3)
**Severity**: High
**Affected Skills**: T08.G3.00 (Identify if blocks in existing code)
**Problem**: Students jump from unplugged conditionals to identifying code blocks without conceptual bridge

```
Current progression:
G2: T08.G2.03 - Identify which rule applies (unplugged)
               ⬇️
               🚧 GAP - No bridge! 🚧
               ⬇️
G3: T08.G3.00 - Identify if blocks in existing code

Students need to understand WHAT an if-block represents
before they can identify one in code!
```

**Proposed Fix**: Add T08.G3.00-pre
```
Match scenarios to if-block descriptions (unplugged)
- "If sprite touches edge, turn around" → match to picture
- Bridges unplugged thinking to block-based concept
- No coding required yet
```

---

### 🟡 ISSUE #5: Illogical Boolean Operator Sequence
**Severity**: High
**Affected Skills**: T08.G4.00, G4.01a, G4.05a (Truth tables)
**Problem**: Truth tables scattered throughout G4, should be grouped together

```
Current Sequence:
T08.G4.00  - AND truth table      📚 (Learn concept)
T08.G4.00b - AND situations       👀 (Recognize)
T08.G4.01  - AND in code          💻 (Code it)
T08.G4.01a - OR truth table       📚 (Learn concept)
T08.G4.01b - AND vs OR scenarios  🤔 (Compare)
T08.G4.02  - OR in code           💻 (Code it)
... 3 more skills ...
T08.G4.05  - Use else-if          💻
T08.G4.05a - NOT truth table      📚 (Learn concept - LATE!)
T08.G4.05b - NOT in code          💻

Better Sequence:
T08.G4.00  - AND truth table  📚 }
T08.G4.00b - AND situations   👀 }
T08.G4.00c - OR truth table   📚 } ← Group all truth tables
T08.G4.00d - NOT truth table  📚 }   (conceptual foundation)
T08.G4.01  - AND in code      💻
T08.G4.01b - OR situations    👀
T08.G4.01c - AND vs OR        🤔
T08.G4.02  - OR in code       💻
...
T08.G4.05b - NOT in code      💻 (keep here, after else-if)
```

**Fix**: Move truth tables to beginning, teach all concepts before implementation

---

### 🟡 ISSUE #6: Merged Skills Too Broad
**Severity**: Medium
**Affected Skills**: T08.G6.01a, T08.G6.01b (Physics vs Biology simulations)
**Problem**: Domain-specific split creates unnecessary branching

```
Current:
T08.G6.01a - Conditionals in physics simulations
T08.G6.01b - Conditionals in population models
             Both required for:
T08.G6.01  - Conditionals to control simulations

Problem: Students must learn BOTH physics AND biology
to understand conditionals in simulations?

Solution: Merge into one skill with multiple domain examples
Students pick one domain (physics OR biology OR games)
```

---

### 🟡 ISSUE #7: Missing G7→G8 Bridge
**Severity**: Medium
**Affected Skills**: T08.G8.01 (Analyze logical equivalence)
**Problem**: G7 ends with fairness/testing, G8 jumps to formal logic

```
Grade 7 Skills:
├─ T08.G7.01: Reason about fairness
└─ T08.G7.02: Design tests

         ⬇️ BIG JUMP ⬇️

Grade 8 Skills:
├─ T08.G8.01: Analyze logical equivalence (De Morgan's laws!)
└─ T08.G8.02: Input validation

Missing: Practice simplifying boolean expressions before formal logic
```

**Proposed Fix**: Add T08.G7.03
```
Simplify complex boolean expressions
- Apply boolean algebra rules
- De Morgan's laws
- Distributive property
- Prepares for G8 logical equivalence
```

---

## Issue Statistics

### By Severity:
- 🔴 Critical: 3 issues (dependency bloat, missing dep, wrong dep)
- 🟡 High: 4 issues (missing bridge, operator sequence, merged skills, G7-G8 gap)

### By Type:
- Dependency Issues: 5 (bloat, missing, wrong, tangential)
- Sequencing Issues: 2 (operator order, K-2→G3 gap)
- Skill Granularity: 1 (G6 simulation merge)
- Missing Skills: 3 (G3 bridge, G4 practice, G7 bridge)

### By Grade:
- Grade 3: 1 issue (missing bridge)
- Grade 4: 3 issues (dependency bloat, missing dep, operator sequence)
- Grade 5: 1 issue (wrong dependency)
- Grade 6: 1 issue (skill merge)
- Grade 7: 1 issue (G8 bridge)

---

## Impact Assessment

### Before Fixes:
```
Grade K: ✅✅ (2 skills, clean)
Grade 1: ✅✅ (3 skills, clean)
Grade 2: ✅✅ (3 skills, clean)
Grade 3: ⚠️  (14 skills, missing bridge)
Grade 4: ❌❌ (19 skills, massive dependency bloat)
Grade 5: ⚠️  (6 skills, wrong dependency)
Grade 6: ⚠️  (5 skills, merge needed)
Grade 7: ⚠️  (2 skills, missing bridge to G8)
Grade 8: ✅  (2 skills, okay but needs G7.03)

Overall: B- (Functional but needs significant cleanup)
```

### After Fixes:
```
Grade K: ✅✅ (2 skills, clean)
Grade 1: ✅✅ (3 skills, clean)
Grade 2: ✅✅ (3 skills, clean)
Grade 3: ✅✅ (15 skills, bridge added)
Grade 4: ✅✅ (21 skills, dependencies streamlined)
Grade 5: ✅✅ (6 skills, dependency fixed)
Grade 6: ✅✅ (3 skills, simulations merged)
Grade 7: ✅✅ (3 skills, bridge added)
Grade 8: ✅✅ (2 skills, proper prerequisites)

Overall: A- (Clean, logical, maintainable)
```

---

## Dependency Reduction

### Quantified Impact:

| Skill | Before | After | Removed |
|-------|--------|-------|---------|
| T08.G4.00 | 4 | 1 | 3 |
| T08.G4.01 | 6 | 2 | 4 |
| T08.G4.02 | 9 | 2 | 7 |
| T08.G4.03 | 7 | 2 | 5 |
| T08.G4.04 | 5 | 1 | 4 |
| T08.G4.05 | 8 | 1 | 7 |
| T08.G4.06 | 6 | 3 | 3* |
| T08.G4.07 | 6 | 3 | 3 |
| T08.G4.08 | 9 | 3 | 6 |
| T08.G4.09 | 5 | 2 | 3 |
| **TOTAL** | **65** | **20** | **45** |

*Note: G4.06 adds 1 critical missing dependency but still nets -3

**Result**: 69% reduction in G4 dependencies (65 → 20)

---

## Skill Count Changes

### Additions (+6 skills):
1. T08.G3.00-pre - Match scenarios to if-block descriptions
2. T08.G4.00c - Understand OR truth table (renumbered)
3. T08.G4.00d - Understand NOT truth table (renumbered)
4. T08.G4.01b - Identify situations requiring OR (new)
5. T08.G4.02b - Choose AND vs OR for coding scenarios (optional)
6. T08.G7.03 - Simplify complex boolean expressions

### Removals (-2 skills):
1. T08.G6.01a - Physics simulations (merged into G6.01)
2. T08.G6.01b - Population models (merged into G6.01)

### Renumberings (3 skills):
1. T08.G4.01a → T08.G4.00c (OR truth table)
2. T08.G4.05a → T08.G4.00d (NOT truth table)
3. T08.G4.01b → T08.G4.01c (Distinguish AND vs OR)

### Net Change:
- With optional skill: 55 → 59 (+4)
- Without optional: 55 → 58 (+3)
- Recommended: 55 → 57 (+2) [skip G4.02b initially]

---

## X-2 Rule Compliance

### Before Fixes (Violations):
```
❌ T08.G4.01 reaches to G2 (should only reach G2 for foundational concepts)
❌ T08.G4.02 reaches to G2 (5 G2 dependencies!)
❌ T08.G4.03 reaches to G2
❌ T08.G4.04 reaches to G2
❌ T08.G4.05 reaches to G2
❌ T08.G4.07 reaches to G2
❌ T08.G4.08 reaches to G2
❌ T08.G4.09 reaches to G2

Total violations: 8 skills
```

### After Fixes (Compliant):
```
✅ All G4 skills only depend on G2-G4
✅ G2 dependencies are minimal and justified
✅ Most G4 skills depend on immediate prerequisites in G3-G4
✅ Cross-topic dependencies preserved (variables, events, testing)

Total violations: 0
```

---

## Key Metrics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total Skills | 55 | 57 | +2 |
| G4 Dependencies | 65 | 20 | -69% |
| X-2 Violations | 8 | 0 | -100% |
| Critical Bugs | 2 | 0 | Fixed |
| Missing Bridges | 2 | 0 | Added |
| Overall Grade | B- | A- | +1.5 |

---

## Implementation Effort

### Time Estimates:
- Phase 1 (Critical fixes): 1.5 hours
- Phase 2 (Structural): 1 hour
- Phase 3 (Optional): 0.5 hours
- **Total**: 3 hours

### Risk Level: LOW
- No breaking changes to cross-topic dependencies
- All changes are within T08
- Additive changes (new skills) are backward compatible
- Dependency removals simplify (don't complicate) the graph

### Testing Required:
- Verify no circular dependencies
- Check all T08 skills have valid prerequisites
- Validate cross-topic dependencies unchanged
- Confirm K-2 skills remain unplugged
- Ensure G3+ skills involve coding

---

## Recommendation

**APPROVE ALL CRITICAL FIXES (Issues #1-3)**
- High impact, low risk
- Fixes actual bugs (missing dep, wrong dep)
- Dramatically improves maintainability

**APPROVE HIGH PRIORITY FIXES (Issues #4-7)**
- Improves learning progression
- Fills conceptual gaps
- Better organization

**OPTIONAL: Add G4.02b practice skill**
- Nice to have, not essential
- Can be added later based on student needs

**Priority**: Implement Phase 1 immediately, Phase 2 within next iteration.
