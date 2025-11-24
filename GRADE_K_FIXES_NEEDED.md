# Grade K Dependency Fixes - Action Items

## Summary
- **Total GK Skills:** 97
- **Total Issues:** 9
- **High Priority Fixes:** 3
- **Medium Priority Review:** 1
- **Redundant Dependencies to Consider Removing:** 3

---

## HIGH PRIORITY - Missing Cross-Topic Dependencies (Add These)

### 1. T06.GK.01 - Add T01 dependency
```
ID: T06.GK.01
Topic: T06 – Events & Sequences
Skill: Order pictures showing a morning routine (event sequence concept)

ACTION: Add dependency
* T01.GK.01: Put pictures in order for getting ready for bed

REASON: Ordering pictures is taught in T01.GK.01-02. This is the exact prerequisite skill.
```

### 2. T26.GK.01 - Add counting dependency
```
ID: T26.GK.01
Topic: T26 – Data Collection & Logging
Skill: Identify countable things in a picture

Current Dependencies:
* T09.GK.01: Recognize that a label can hold a number

ACTION: Add dependency
* T01.GK.08: Count how many times

REASON: Skill requires counting ability. T09.GK.01 teaches variables, not counting mechanics.
```

### 3. T26.GK.02 - Add pattern dependency
```
ID: T26.GK.02
Topic: T26 – Data Collection & Logging
Skill: Use tokens to log repeated events

Current Dependencies:
* T09.GK.01: Recognize that a label can hold a number
* T26.GK.01: Identify countable things in a picture

ACTION: Add dependency (choose one)
* T01.GK.07: Find the pattern that repeats
OR
* T04.GK.01: Identify a simple repeating pattern

REASON: Logging "repeated" events requires recognizing repetition/patterns first.
RECOMMENDATION: Use T01.GK.07 (simpler, earlier skill)
```

---

## MEDIUM PRIORITY - Review Required

### 4. T29.GK.02 - Possibly add counting dependency
```
ID: T29.GK.02
Topic: T29 – Text Data & NLP Foundations
Skill: Identify letters in text

Current Dependencies:
* T29.GK.01: Recognize text vs pictures

ACTION: Review implementation
- If skill involves counting letters ("how many letters"), add:
  * T01.GK.08: Count how many times
- If skill is only about letter identification, no change needed

REASON: Unclear if counting is core to this skill or incidental.
```

---

## CONSIDER REMOVING - Redundant Transitive Dependencies

These dependencies are already reachable through other paths and may be genuinely redundant.

### 5. T02.GK.04 - Remove redundant dependency
```
ID: T02.GK.04
Topic: T02 – Algorithm Diagrams
Skill: Fix one picture that is out of order

Current Dependencies:
* T02.GK.02: Order 3–4 pictures to make a story
* T02.GK.03: Use first/next/last to describe a sequence

ACTION: Remove T02.GK.02 (keep T02.GK.03)

REASON: T02.GK.03 already depends on T02.GK.02, making direct dependency redundant.
Dependency path: T02.GK.04 → T02.GK.03 → T02.GK.02
```

### 6. T26.GK.02 - Remove redundant dependency
```
ID: T26.GK.02
Topic: T26 – Data Collection & Logging
Skill: Use tokens to log repeated events

Current Dependencies:
* T09.GK.01: Recognize that a label can hold a number
* T26.GK.01: Identify countable things in a picture

ACTION: Remove T09.GK.01 (keep T26.GK.01)

REASON: T26.GK.01 already depends on T09.GK.01, making direct dependency redundant.
Dependency path: T26.GK.02 → T26.GK.01 → T09.GK.01

NOTE: After adding T01.GK.07 (from fix #3), keep the new dependency.
```

### 7. T29.GK.03 - Remove redundant dependency
```
ID: T29.GK.03
Topic: T29 – Text Data & NLP Foundations
Skill: Recognize that text has meaning

Current Dependencies:
* T29.GK.01: Recognize text vs pictures
* T29.GK.02: Identify letters in text

ACTION: Remove T29.GK.01 (keep T29.GK.02)

REASON: T29.GK.02 already depends on T29.GK.01, making direct dependency redundant.
Dependency path: T29.GK.03 → T29.GK.02 → T29.GK.01
```

---

## KEEP AS IS - Intentional Dual Dependencies

These appear redundant but should be kept for pedagogical clarity:

### T02.GK.03 - Keep both dependencies
```
ID: T02.GK.03
Dependencies: T01.GK.01, T02.GK.02

REASON: Emphasizes two distinct prerequisites:
- T01.GK.01: Basic ordering skill (from Everyday Algorithms)
- T02.GK.02: Algorithm diagram skill (from Algorithm Diagrams)
Different conceptual foundations.
```

### T24.GK.03 - Keep both dependencies
```
ID: T24.GK.03
Dependencies: T24.GK.01, T24.GK.02

REASON: Two distinct prerequisites:
- T24.GK.01: Understanding what AI is
- T24.GK.02: Recognizing AI output
Different aspects of AI understanding before giving instructions.
```

---

## Implementation Order

1. **Add missing dependencies** (fixes #1, #2, #3)
2. **Review T29.GK.02** (fix #4)
3. **Remove redundant dependencies** (fixes #5, #6, #7) - ONLY if agreed upon

---

## Validation Checklist

After making changes:
- [ ] All GK skills still depend only on GK skills (X-2 rule)
- [ ] No circular dependencies introduced
- [ ] Cross-topic dependencies are appropriate
- [ ] T06.GK.01 has T01 dependency
- [ ] T26 skills have counting/pattern dependencies
- [ ] Redundant dependencies removed (if agreed)

---

## No Action Needed

✅ **X-2 Rule Compliance:** Perfect - all GK skills depend only on GK skills
✅ **Circular Dependencies:** None found
✅ **Most Dependencies:** Already correct and appropriate
