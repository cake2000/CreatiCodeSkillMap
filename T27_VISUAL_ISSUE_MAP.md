# T27 Visual Issue Map

## Issue Distribution by Grade Level

```
Grade  | Total Skills | Issues Found | Issue Rate | Critical Issues
-------|-------------|--------------|------------|----------------
  GK   |      3      |      1       |    33%     |      0
  G1   |      3      |      2       |    67%     |      0
  G2   |      4      |      2       |    50%     |      0
  G3   |      8      |      7       |    88%     |      4 ⚠️
  G4   |      9      |      9       |   100%     |      7 ⚠️⚠️
  G5   |      7      |      7       |   100%     |      5 ⚠️⚠️
  G6   |      9      |      8       |    89%     |      6 ⚠️⚠️
  G7   |      7      |      6       |    86%     |      4 ⚠️
  G8   |      4      |      2       |    50%     |      1
-------|-------------|--------------|------------|----------------
TOTAL  |     54      |     44       |    81%     |     27
```

**KEY INSIGHT:** Grades 3-7 have the highest concentration of issues (90%+ affected)

---

## Issue Type Distribution

```
ISSUE TYPE                  | Count | % of Skills | Severity
----------------------------|-------|-------------|----------
Ordering/Numbering Chaos    |   39  |     72%     |  🔴 CRITICAL
Excessive Dependencies      |    3  |      6%     |  🟠 HIGH
Circular Dependencies       |    1  |      2%     |  🔴 CRITICAL
Invalid Skill References    |    2  |      4%     |  🟠 HIGH
Overly Broad Skills         |    5  |      9%     |  🟡 MEDIUM
Missing Foundational Skills |    8  |    (new)    |  🟡 MEDIUM
Block Reference Errors      |    6  |     11%     |  🟢 LOW
Vague Descriptions          |   10  |     19%     |  🟢 LOW
Missing Intra-Topic Deps    |    5  |      9%     |  🟡 MEDIUM
```

---

## Grade 3 Issue Breakdown (88% issues)

```
Skill ID      | Ordering | Dependency | Broad | Blocks | Vague | Status
--------------|----------|------------|-------|--------|-------|--------
T27.G3.00     |          |            |       |        |       | ✓ OK
T27.G3.01b    |    ❌    |            |  ⚠️   |   ⚠️   |       | ISSUES
T27.G3.01     |    ❌    |     ⚠️     |       |        |       | ISSUES
T27.G3.01c    |    ❌    |            |       |   ❌   |       | ISSUES
T27.G3.02     |    ❌    |     ⚠️     |       |        |   ⚠️  | ISSUES
T27.G3.03     |    ❌    |            |       |   ⚠️   |       | ISSUES
T27.G3.04     |    ❌    |     ⚠️     |       |        |       | ISSUES
T27.G3.05     |    ❌    |            |       |        |       | ISSUES
```

**CRITICAL:** G3.01b appears BEFORE G3.01 in numbering (illogical)

---

## Grade 4 Issue Breakdown (100% issues)

```
Skill ID      | Ordering | Dependency | Broad | Blocks | Vague | Status
--------------|----------|------------|-------|--------|-------|--------
T27.G4.01     |          |    ❌❌    |       |        |       | ISSUES
T27.G4.02b    |    ❌    |            |       |        |       | ISSUES
T27.G4.02c    |    ❌    |            |       |   ⚠️   |       | ISSUES
T27.G4.02e    |    ❌    |            |       |        |       | ISSUES
T27.G4.02d    |    ❌    |            |  ⚠️   |        |       | ISSUES
T27.G4.03     |    ❌    |    ❌❌    |       |        |   ❌  | ISSUES
T27.G4.03b    |    ❌    |            |       |        |       | ISSUES
T27.G4.04     |    ❌    |    ❌❌    |       |        |       | ISSUES
T27.G4.04b    |    ❌    |     ⚠️     |       |        |       | ISSUES
```

**CRITICAL:**
- No G4.02 base skill exists, but b/c/d/e suffixes do!
- G4.01 has 8 dependencies from 5 topics
- G4.03 has 9 dependencies + references unknown skill

---

## Grade 5 Issue Breakdown (100% issues)

```
Skill ID      | Ordering | Dependency | Broad | Blocks | Vague | Status
--------------|----------|------------|-------|--------|-------|--------
T27.G5.00     |    ❌    |            |       |        |       | ISSUES
T27.G5.01     |    ❌    |            |  ⚠️   |        |   ❌  | ISSUES
T27.G5.00b    |    ❌    |    🔴🔴   |       |        |       | CRITICAL
T27.G5.01b    |    ❌    |            |       |   ❌   |       | ISSUES
T27.G5.02     |    ❌    |     ⚠️     |       |        |       | ISSUES
T27.G5.03     |    ❌    |            |       |        |       | ISSUES
T27.G5.04     |    ❌    |            |       |        |       | ISSUES
```

**CRITICAL:**
- G5.00b has CIRCULAR dependency with G5.01
- "00" and "00b" notation creates confusion

---

## Grade 6 Issue Breakdown (89% issues)

```
Skill ID      | Ordering | Dependency | Broad | Blocks | Vague | Status
--------------|----------|------------|-------|--------|-------|--------
T27.G6.01     |          |            |       |        |       | ✓ OK
T27.G6.01c    |    ❌    |            |       |        |       | ISSUES
T27.G6.01b    |    ❌    |            |       |   ❌   |       | ISSUES
T27.G6.01d    |    ❌    |            |       |        |       | ISSUES
T27.G6.02     |    ❌    |     ⚠️     |  ⚠️   |        |       | ISSUES
T27.G6.02b    |    ❌    |            |       |   ⚠️   |       | ISSUES
T27.G6.03     |    ❌    |            |       |        |       | ISSUES
T27.G6.03b    |    ❌    |            |       |        |       | ISSUES
T27.G6.04     |    ❌    |            |       |        |       | ISSUES
```

**CRITICAL:**
- G6.01c appears BEFORE G6.01b (illogical order)
- G6.01b has incorrect block terminology

---

## Grade 7 Issue Breakdown (86% issues)

```
Skill ID      | Ordering | Dependency | Broad | Blocks | Vague | Status
--------------|----------|------------|-------|--------|-------|--------
T27.G7.01     |          |     ⚠️     |  ⚠️   |        |       | ISSUES
T27.G7.01b    |    ❌    |            |       |   ⚠️   |       | ISSUES
T27.G7.02     |    ❌    |            |       |        |       | ISSUES
T27.G7.02b    |    ❌    |            |  ⚠️   |   ⚠️   |       | ISSUES
T27.G7.02c    |    ❌    |            |       |        |       | ISSUES
T27.G7.03     |    ❌    |            |       |        |   ❌  | ISSUES
T27.G7.04     |          |            |       |        |       | ✓ OK
```

**ISSUES:**
- G7.01 is overly broad (capstone skill)
- G7.02b needs splitting (table-to-list + moving average)
- G7.03 has vague fairness metrics description

---

## Grade 8 Issue Breakdown (50% issues)

```
Skill ID      | Ordering | Dependency | Broad | Blocks | Vague | Status
--------------|----------|------------|-------|--------|-------|--------
T27.G8.01     |          |            |       |        |   ❌  | ISSUES
T27.G8.02     |          |            |       |        |       | ✓ OK
T27.G8.03     |          |            |       |        |       | ✓ OK
T27.G8.04     |          |            |       |        |       | ✓ OK
```

**NOTE:** Grade 8 is relatively clean (only vague descriptions)

---

## Critical Issue Clusters

### CLUSTER 1: The G3-G4-G5 Ordering Disaster
```
Current Order (WRONG):
  G3.00 → G3.01b → G3.01 → G3.01c → G3.02 → G3.03 → G3.04 → G3.05
  G4.01 → G4.02b → G4.02c → G4.02e → G4.02d → G4.03 → G4.03b → G4.04 → G4.04b
  G5.00 → G5.01 → G5.00b → G5.01b → G5.02 → G5.03 → G5.04

Logical Order (SHOULD BE):
  G3.00 → G3.01 → G3.02 → G3.03 → G3.04 → G3.05 → G3.06 → G3.07
  G4.01 → G4.02 → G4.03 → G4.04 → G4.05 → G4.06 → G4.07 → G4.08 → G4.09
  G5.01 → G5.02 → G5.03 → G5.04 → G5.05 → G5.06 → G5.07
```

### CLUSTER 2: The Circular Dependency Loop
```
T27.G5.00b (Widget events)
    ↓ depends on
T27.G5.01 (Interactive dashboard)
    ↓ needs (logically)
T27.G5.00b (Widget events) ← CIRCULAR!

FIX: Reverse G5.00b dependency
```

### CLUSTER 3: The Unknown Skill Mystery
```
T27.G4.03 → depends on → T26.G3.04 [Unknown skill]
T27.G4.04 → depends on → T26.G3.04 [Unknown skill]

FIX: Identify T26.G3.04 or remove dependency
```

### CLUSTER 4: The Excessive Dependency Problem
```
T27.G4.01 → 8 dependencies from 5 topics
T27.G4.03 → 9 dependencies (too many!)
T27.G4.04 → 7 dependencies from 6 topics

FIX: Simplify to 3-4 essential prerequisites each
```

---

## Missing Skills Gap Analysis

```
Grade | Missing Skills | Impact
------|---------------|--------
  G3  | - Table verification           | Can't debug tables
      | - List-based charts            | Tables before simpler lists
  G4  | - Delete specific rows         | Limited data management
      | - Update table values          | Can't correct errors
      | - List aggregation             | Tables before lists (wrong order)
  G5  | - Copy/backup tables           | Can't experiment safely
  G6  | - Combined AND/OR conditions   | Can't build complex queries
  G7  | - Table-to-list conversion     | Moving averages need this
```

**TOTAL MISSING:** 8 foundational skills

---

## Block Reference Accuracy

```
Skill      | Incorrect Block Term     | Correct Block Term
-----------|--------------------------|---------------------------
T27.G3.01c | [minimum v] / [maximum v]| [smallest v] / [largest v]
T27.G5.01b | set table to             | set table to computed
T27.G6.01b | row # of                 | row index with condition
T27.G6.02b | (unverified syntax)      | (need verification)
T27.G7.01b | (unverified syntax)      | (need verification)
T27.G7.02b | (unverified syntax)      | (need verification)
```

**VERIFICATION NEEDED:** 6 skills need block syntax confirmation

---

## Dependency Type Distribution

```
Dependency Pattern        | Count | Notes
--------------------------|-------|-------------------------------
Within T27 (intra-topic)  |  34   | Good progression
To T26 (Data Collection)  |   8   | Expected, related topic
To T09 (Variables)        |  12   | Essential for data work
To T10 (Lists)            |   6   | Lists used in charts/analysis
To T06 (Events)           |   8   | For dashboards
To T07 (Loops)            |   5   | For iteration
To T08 (Conditionals)     |   4   | For filtering
To T04 (Patterns)         |   3   | For analysis patterns
To T01 (Algorithms)       |   2   | Basic sequencing
To T12/T15/T17/T36        |   4   | Questionable relevance
```

**ISSUE:** Some cross-topic dependencies seem tangential

---

## Renumbering Impact Analysis

```
Grade | Skills Affected | Dependency Updates Needed | Estimated Time
------|-----------------|---------------------------|---------------
  G3  |       7         |          12               |    45 min
  G4  |       8         |          18               |    60 min
  G5  |       7         |          15               |    50 min
  G6  |       8         |          16               |    55 min
  G7  |       6         |          10               |    40 min
  G8  |       0         |           0               |     0 min
------|-----------------|---------------------------|---------------
TOTAL |      36         |          71               |   250 min (4h)
```

**NOTE:** Automated script can reduce time to 1-2 hours

---

## Priority Matrix

```
                    HIGH IMPACT
                         ↑
        ┌────────────────┼────────────────┐
        │  URGENT         │  IMPORTANT     │
        │                 │                │
        │ • Renumbering   │ • Missing      │
        │ • Circular dep  │   skills       │
 LOW    │ • Invalid ref   │ • Broad skills │    HIGH
EFFORT  │                 │                │   EFFORT
←───────┼─────────────────┼────────────────┼─────────→
        │  NICE TO HAVE   │  LOW PRIORITY  │
        │                 │                │
        │ • Vague desc    │ • (none)       │
        │ • Block errors  │                │
        └────────────────┼────────────────┘
                         ↓
                    LOW IMPACT
```

**RECOMMENDATION:** Start top-left, move clockwise

---

## Success Metrics

### BEFORE Analysis:
- ❌ 72% skills have numbering issues
- ❌ 22% skills have dependency problems
- ❌ 19% skills have vague descriptions
- ❌ 11% skills have block errors
- ❌ 0 systematic documentation of issues

### AFTER Fixes:
- ✅ 100% skills numbered logically
- ✅ 0 circular dependencies
- ✅ 0 invalid references
- ✅ All block terms accurate
- ✅ Complete issue documentation

---

## Implementation Roadmap

### Week 1: Critical Fixes
- Day 1-2: Create renumbering script
- Day 2-3: Execute renumbering (39 skills)
- Day 3: Fix circular dependency
- Day 4: Remove invalid references
- Day 5: Correct block terminology

### Week 2: Content Improvements
- Day 1-2: Split 5 overly broad skills
- Day 3-4: Write 8 new foundational skills
- Day 5: Peer review new content

### Week 3: Descriptions & Dependencies
- Day 1-2: Rewrite 10 vague descriptions
- Day 3-4: Simplify excessive dependencies
- Day 5: Add missing intra-topic deps

### Week 4: Validation & Testing
- Day 1-2: Verify X-2 rule compliance
- Day 3: Run full validation suite
- Day 4: Create example implementations
- Day 5: Final stakeholder review

---

**Generated:** 2025-11-25
**Scope:** T27 Skills (54 total)
**Issues Mapped:** 44 skills (81%)
**Critical Issues:** 27 skills (50%)
