# K-2 Skills Dependency Examples

## Example Dependency Chains

This document shows real examples of how dependencies work in the K-2 skill map, illustrating different patterns.

---

## Pattern 1: Within-Topic Sequential Progression

### T01: Everyday Algorithms (K→G1→G2)

**Kindergarten Sequence:**
```
T01.GK.01 (K): []
    ↓
T01.GK.02 (K): [T01.GK.01]
    ↓
T01.GK.03 (K): [T01.GK.02]
    ↓
T01.GK.04 (K): [T01.GK.03]
```

**Grade 1 builds on K:**
```
T01.GK.04 (K): [T01.GK.03]
    ↓
T01.G1.01 (1): [T01.GK.04]  ← Builds on last K skill
    ↓
T01.G1.02 (1): [T01.G1.01]
```

**Grade 2 builds on G1:**
```
T01.G1.04 (1): [T01.G1.03]
    ↓
T01.G2.01 (2): [T01.G1.04]  ← Builds on last G1 skill
    ↓
T01.G2.02 (2): [T01.G2.01]
```

**Pattern:** Each grade builds sequentially, with cross-grade transitions at start of new grade level.

---

## Pattern 2: Cross-Topic with Within-Topic Progression

### T02: Representing Algorithms (References T01 + Sequential)

**Kindergarten:**
```
T01.GK.01 (K) ─────┐
                   ↓
T02.GK.01 (K): [T01.GK.01]  ← Cross-topic reference to T01
    ↓
T02.GK.02 (K): [T01.GK.01, T02.GK.01]  ← T01 + previous T02
    ↓
T02.GK.03 (K): [T01.GK.01, T02.GK.02]  ← T01 + previous T02
```

**Grade 1:**
```
T01.G1.01 (1) ─────┐
                   ↓
T02.GK.03 (K) ─────┤
                   ↓
T02.G1.01 (1): [T01.G1.01, T02.GK.03]  ← T01 G1 + last T02 K
    ↓
T02.G1.02 (1): [T01.G1.01, T02.G1.01]  ← T01 G1 + previous T02
```

**Pattern:** Every skill references both T01 (conceptual foundation) AND previous T02 skill (within-topic).

---

## Pattern 3: Cross-Topic Reference Only (Art from Patterns)

### T20: Algorithmic Art (Heavy T04 Pattern Reference)

**Kindergarten:**
```
T04.GK.01 (K Pattern) ─────┐
                           ↓
T20.GK.01 (K Art): [T04.GK.01]  ← References pattern skill
    ↓
T20.GK.02 (K Art): [T04.GK.01, T20.GK.01]  ← Pattern + previous art
```

**Grade 1:**
```
T04.G1.01 (1 Pattern) ─────┐
                           ↓
T20.GK.03 (K Art) ─────────┤
                           ↓
T20.G1.01 (1 Art): [T04.G1.01, T20.GK.03]  ← G1 pattern + last K art
```

**Pattern:** Art skills always reference corresponding grade-level pattern skill, essential for creating patterns in art.

---

## Pattern 4: Multiple Cross-Topic References

### T27: Data Analysis (T04 Patterns + T26 Data Collection)

**Grade 2 (Data Analysis only exists in G2 for K-2):**
```
T04.G1.01 (1 Patterns) ────┐
                           │
T26.G1.01 (1 Collection) ──┤
                           │
T27.G1.03 (1 Analysis) ────┤
                           ↓
T27.G2.01 (2): [T04.G1.01, T26.G1.01, T27.G1.03]
    ↓
T27.G2.02 (2): [T04.G1.01, T26.G1.01, T27.G2.01]
```

**Pattern:** Data analysis requires:
1. Pattern recognition (T04)
2. Data collection understanding (T26)
3. Previous analysis skills (T27)

This is the most dependencies (3) in the K-2 map, appropriate for integrative G2 activities.

---

## Pattern 5: Bridge Topics (G2 Only, Reference Foundations)

### T06: Events (Pre-Coding, References T01)

**Grade 2 only:**
```
T01.G1.01 (1 Algorithms) ─────┐
                              ↓
T06.G2.01 (2 Events): [T01.G1.01]  ← References G1 algorithm understanding
    ↓
T06.G2.02 (2 Events): [T01.G1.01, T06.G2.01]  ← Algorithm + previous event
```

**Pattern:** Bridge topics (preparing for Grade 3-8 coding) reference foundational concepts from earlier grades.

---

### T08: Conditionals (Pre-Coding, References T01)

**Grade 2 only:**
```
T01.GK.03 (K Algorithms) ─────┐
                              ↓
T08.G2.01 (2 Conditionals): [T01.GK.03]  ← References K if-then thinking
    ↓
T08.G2.02 (2): [T01.GK.03, T08.G2.01]
```

**Pattern:** Conditionals reference K algorithm skill that introduces if-then scenarios.

---

### T09: Variables Pre-Skills (References T25 Data)

**Grade 2 only:**
```
T25.GK.01 (K Data Rep) ─────┐
                            ↓
T09.G2.01 (2 Variables): [T25.GK.01]  ← References K data concepts
    ↓
T09.G2.02 (2): [T25.GK.01, T09.G2.01]
```

**Pattern:** Variables reference data representation (values that can change).

---

### T10: Lists Pre-Skills (References T25 Data)

**Grade 2 only:**
```
T25.G1.01 (1 Data Rep) ─────┐
                            ↓
T10.G2.01 (2 Lists): [T25.G1.01]  ← References G1 organizing data
    ↓
T10.G2.02 (2): [T25.G1.01, T10.G2.01]
```

**Pattern:** Lists reference organizing data concepts.

---

### T12: Program Organization (References T03 Decomposition)

**Grade 2 only:**
```
T03.G1.01 (1 Decomposition) ─────┐
                                 ↓
T12.G2.01 (2 Organization): [T03.G1.01]  ← Breaking down problems
    ↓
T12.G2.02 (2): [T03.G1.01, T12.G2.01]
```

**Pattern:** Organizing programs requires decomposition thinking.

---

## Pattern 6: Debugging (References What's Being Debugged)

### T13: Testing & Debugging

**Kindergarten (Debug Sequences):**
```
T01.GK.01 (K Algorithms) ─────┐
                              ↓
T13.GK.01 (K Debug): [T01.GK.01]  ← Debug sequences
    ↓
T13.GK.02 (K): [T01.GK.01, T13.GK.01]
```

**Grade 1 (Debug Algorithms):**
```
T01.GK.04 (Last K Algorithm) ─────┐
                                  ↓
T13.G1.01 (1 Debug): [T01.GK.04, T13.GK.03]  ← Debug more complex
```

**Grade 2 (Debug Representations):**
```
T02.G1.01 (1 Representing) ─────┐
                                ↓
T13.G2.01 (2 Debug): [T02.G1.01, T13.G1.04]  ← Debug representations
```

**Pattern:** Debugging references appropriate complexity level of what students are debugging at each grade.

---

## Pattern 7: Standalone Topics (Minimal/No Dependencies)

### T21: AI & Media (Standalone)

```
T21.G2.01 (2): []  ← No dependencies, conceptual introduction
```

### T30-T36: Systems & Society Topics

**Kindergarten:**
```
T30.GK.01 (K Hardware): []
T32.GK.01 (K Security): []
T34.GK.01 (K History): []
T35.GK.01 (K Impacts): []
T36.GK.01 (K Ethics): []
```

**Grade 2 (Minimal within-topic only):**
```
T30.G2.01 (2 Hardware): []
    ↓
T30.G2.02 (2): [T30.G2.01]  ← Only within-topic progression
```

**Pattern:** Conceptual topics (society, ethics, history) are mostly standalone with minimal within-topic progression in G2.

---

## Summary of Patterns

| Pattern | Example Topics | Typical Dep Count | Grade Distribution |
|---------|---------------|-------------------|-------------------|
| Within-topic sequential | T01, T04 | 1 per skill | All grades |
| Cross-topic + sequential | T02, T20, T13 | 2 per skill | All grades |
| Bridge topics | T06, T08, T09, T10, T12, T14 | 1-2 per skill | G2 only |
| Multi cross-topic | T27 | 3 per skill | G2 only |
| Standalone/minimal | T21, T30-T36 | 0-1 per skill | All grades |

---

## Grade-Level Dependency Philosophy

### Kindergarten (Avg: 0.62 deps/skill)
- **27 skills (48%)** have NO dependencies - foundational
- **24 skills (43%)** have 1 dependency - within-topic progression
- **5 skills (9%)** have 2 dependencies - cross-topic + within-topic
- **Focus:** Building foundations, simple sequences

### Grade 1 (Avg: 0.91 deps/skill)
- **20 skills (31%)** have NO dependencies - new foundations
- **33 skills (52%)** have 1 dependency - building on K or within G1
- **11 skills (17%)** have 2 dependencies - cross-topic connections
- **Focus:** Connecting concepts, cross-topic thinking

### Grade 2 (Avg: 1.45 deps/skill)
- **6 skills (7%)** have NO dependencies - bridge topic introductions
- **35 skills (41%)** have 1 dependency - building progressions
- **41 skills (48%)** have 2 dependencies - cross-topic integration
- **4 skills (5%)** have 3 dependencies - data analysis integration
- **Focus:** Integration, preparing for coding (bridge topics)

---

## Cross-Grade Transitions

### K → G1 Transitions

Topics that transition from K to G1:
```
T01.GK.04 → T01.G1.01  (Algorithms)
T02.GK.03 → T02.G1.01  (Representing)
T03.GK.03 → T03.G1.01  (Decomposition)
T04.GK.04 → T04.G1.01  (Patterns)
T20.GK.03 → T20.G1.01  (Art)
T25.GK.04 → T25.G1.01  (Data Rep)
... and more
```

**Pattern:** Last K skill → First G1 skill in same topic

### G1 → G2 Transitions

Topics that transition from G1 to G2:
```
T01.G1.04 → T01.G2.01  (Algorithms)
T02.G1.04 → T02.G2.01  (Representing)
T03.G1.04 → T03.G2.01  (Decomposition)
T04.G1.04 → T04.G2.01  (Patterns)
T20.G1.04 → T20.G2.01  (Art)
... and more
```

**Pattern:** Last G1 skill → First G2 skill in same topic

### G2 Bridge Topics (No Earlier Grades)

Some topics only exist in G2 (preparing for G3-8 coding):
- T06: Events
- T08: Conditionals
- T09: Variables Pre-Skills
- T10: Lists Pre-Skills
- T12: Program Organization
- T14: Games Pre-Skills

These reference appropriate K or G1 foundational skills from other topics.

---

## Quality Characteristics

✅ **Minimal:** No skill has more than 3 dependencies
✅ **Purposeful:** All cross-topic references are pedagogically necessary
✅ **Progressive:** Dependencies flow K→G1→G2 with no backward references
✅ **Balanced:** 72% of skills have 0-1 dependencies (minimal)
✅ **Developmental:** Complexity increases by grade level appropriately

---

**Document Generated:** 2025-11-17
**K-2 Skills:** 206 total
**Total Dependencies:** 218 connections
**Average Dependencies:** 1.06 per skill
