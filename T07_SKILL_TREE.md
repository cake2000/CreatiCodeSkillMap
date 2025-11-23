# T07 (Loops) - Skill Tree Visualization

## Loop Concept Progression

```
KINDERGARTEN - GRADE 2: Unplugged Foundation
==============================================
K.01: Complete repeating pattern (AB, AAB, ABC)
  ↓
G1.01: Count repetitions in pattern
  ↓
G1.02: Match "do N times" to outcomes
  ↓
G2.01: Identify "repeat" vs "do once"


GRADE 3: Introduction to Loop Blocks
=====================================
                    G3.01: Use repeat N loop ⚠️ (gateway skill)
                      ↓
        ┌─────────────┴─────────────┐
        ↓                           ↓
    G3.02: Trace                G3.03: Build forever loop
    simple loop                      ↓
                                G3.04: Use repeat-until ⚠️ BROKEN DEP
                                     ↓
                                G3.05: Fix loop count


GRADE 4: Loop Sophistication
=============================
            ┌───────────┬───────────┬───────────┐
            ↓           ↓           ↓           ↓
        G4.01:      G4.02:      G4.03:      G4.04:
        Forever     If inside   Counter     Identify
        game loop   loop        variable    repeated code
            │           │           │           │
            │           │           │           │
            └───────────┴───────────┴───────────┘
                        ↓
            ┌───────────┼───────────┐
            ↓           ↓           ↓
        G4.05:      G4.06:      G4.07:
        Debug       Trace       Trace nested
        complex     loop+cond   (fixed bounds)
            │           │           │
            └───────────┴───────────┘
                        │
                    G4.08:
                    Timed repeat


GRADE 5: Data & Loops
======================
        ┌───────────┬───────────┬───────────┐
        ↓           ↓           ↓           ↓
    G5.01:      G5.02:      G5.03:      G5.04:
    Simulate    Build       Compute     Nested
    experiments list        aggregates  patterns


GRADE 6: Advanced Loop Techniques
==================================
        ┌───────────┬───────────┬───────────┐
        ↓           ↓           ↓           ↓
    G6.01:      G6.02:      G6.03:      G6.04:
    Variable    Refactor    Search      Infinite
    bounds      patterns    in list     loop bugs
        │           │           │           │
        └───────────┴───────────┴───────────┘
                        ↓
        ┌───────────┬───────────┬───────────┐
        ↓           ↓           ↓           ↓
    G6.05:      G6.06:      G6.07:      G6.08:
    Trace       Trace       Iterative   break &
    table       visual      updates     continue
    method      patterns                    │
        │           │           │           │
        └───────────┴───────────┴───────────┘
                        ↓
                    G6.09:
                    for-each loops ⚠️ Should be G5


GRADE 7: Algorithms & Analysis
===============================
        ┌───────────┬───────────┬───────────┐
        ↓           ↓           ↓           ↓
    G7.01:      G7.02:      G7.03:      G7.04:
    Motion      2D grids    Compare     Loop
    simulation              algorithms  patterns


GRADE 8: Classic Algorithms
============================
        ┌───────────┬───────────┬───────────┐
        ↓           ↓           ↓           ↓
    G8.01:      G8.02: ⚠️    G8.03:      G8.04:
    Monte       Design      Process     Justify
    Carlo       iterative   2D data     design
                    │
        ┌───────────┼───────────┐
        ↓           ↓           ↓
    G8.02.01:   G8.02.02:   G8.02.03:
    GCD         Primality   Fibonacci
```

## Loop Types Coverage by Grade

```
┌─────────┬────────┬─────────┬───────────┬────────┬──────────┬──────────┐
│ Grade   │ repeat │ forever │ rep-until │ for    │ for-each │ timed    │
│         │   N    │         │           │ loop   │          │ repeat   │
├─────────┼────────┼─────────┼───────────┼────────┼──────────┼──────────┤
│ K-G2    │   -    │    -    │     -     │   -    │    -     │    -     │
│ (prep)  │        │         │           │        │          │          │
├─────────┼────────┼─────────┼───────────┼────────┼──────────┼──────────┤
│ G3      │   ●    │    ●    │     ●     │   -    │    -     │    -     │
│ (intro) │  G3.01 │  G3.03  │   G3.04   │        │          │          │
├─────────┼────────┼─────────┼───────────┼────────┼──────────┼──────────┤
│ G4      │   ●    │    ●    │     ●     │   ●    │    -     │    ●     │
│ (mastery│  G4.04 │  G4.01  │   G4.05   │ G4.03  │          │  G4.08   │
├─────────┼────────┼─────────┼───────────┼────────┼──────────┼──────────┤
│ G5      │   ●    │    ●    │     ●     │   ●    │    -     │    -     │
│ (apply) │        │         │           │        │          │          │
├─────────┼────────┼─────────┼───────────┼────────┼──────────┼──────────┤
│ G6      │   ●    │    ●    │     ●     │   ●    │    ●     │    -     │
│ (adv)   │        │         │   G6.04   │        │  G6.09   │          │
├─────────┼────────┼─────────┼───────────┼────────┼──────────┼──────────┤
│ G7-G8   │   ●    │    ●    │     ●     │   ●    │    ●     │    -     │
│ (algos) │        │         │           │        │          │          │
└─────────┴────────┴─────────┴───────────┴────────┴──────────┴──────────┘

● = Used in skills at this grade
```

## Dependency Clusters

### Cluster 1: Basic Sequential Skills (No loops yet)
```
T06.G3.01: Build green-flag script
    ↓
T07.K.01 → T07.G1.01 → T07.G1.02 → T07.G2.01
    ↓
T07.G3.01: FIRST LOOP
```

### Cluster 2: Loop Types (G3)
```
T07.G3.01: repeat N
    ├───→ T07.G3.02: trace
    ├───→ T07.G3.03: forever
    │         ↓
    │     T07.G3.04: repeat-until
    │         ↓
    └───→ T07.G3.05: debug count
```

### Cluster 3: Loops + Logic (G4)
```
T08.G3.01: Simple if
    +
T07.G3.03/G3.04: Loops
    ↓
T07.G4.01: Forever game loop
T07.G4.02: If inside loop
T07.G4.06: Trace loop+condition
```

### Cluster 4: Loops + Variables (G4-G5)
```
T09.G3.01.04: Display variable
    +
T07.G3.01: Basic loop
    ↓
T07.G4.03: Loop counter
    ↓
T07.G5.03: Compute aggregates
```

### Cluster 5: Loops + Lists (G5-G6)
```
T10.G5.01: Create list
    +
T07.G4.03: Counter
    ↓
T07.G5.02: Build list with loop
    ↓
T07.G6.03: Search in list
    ↓
T07.G6.09: for-each loop
```

### Cluster 6: Nested Loops (G4-G7)
```
T07.G4.07: Trace nested (fixed)
    ↓
T07.G5.04: Build nested patterns
    ↓
T07.G6.01: Trace nested (variable)
T07.G6.05: Trace tables
T07.G6.06: Trace visual
    ↓
T07.G7.02: 2D grid processing
```

### Cluster 7: Advanced Control (G6)
```
T07.G6.03: Search
    +
T07.G6.04: Infinite loop bugs
    ↓
T07.G6.08: break & continue
```

### Cluster 8: Algorithms (G7-G8)
```
T07.G7.03: Compare algorithms
T07.G7.04: Loop patterns
    ↓
T07.G8.02.01: GCD
T07.G8.02.02: Primality
T07.G8.02.03: Fibonacci
    ↓
T07.G8.04: Justify design
```

## Issues by Skill

```
✅ = No issues
⚠️  = Minor issues (LOW/MEDIUM)
❌ = Critical issues (HIGH)

K.01  ✅
G1.01 ✅
G1.02 ⚠️  (could be merged with G1.01)
G2.01 ⚠️  (needs examples)

G3.01 ❌ (overloaded dependencies)
G3.02 ⚠️  (redundant with G3.01?)
G3.03 ✅
G3.04 ❌ (broken dependency T09.G3.02)
G3.05 ⚠️  (unnecessary T08 dependency)

G4.01 ⚠️  (redundant dependencies)
G4.02 ⚠️  (unnecessary T09 dependency)
G4.03 ❌ (mixes two concepts)
G4.04 ⚠️  (wrong dependencies)
G4.05 ⚠️  (vague "complex")
G4.06 ⚠️  (similar to G4.02)
G4.07 ✅
G4.08 ⚠️  (narrow feature focus)

G5.01 ⚠️  (overly broad)
G5.02 ⚠️  (unclear sensor support)
G5.03 ⚠️  (vague "repeated events")
G5.04 ⚠️  (generic "advanced")

G6.01 ❌ (concept conflation)
G6.02 ⚠️  (math not taught)
G6.03 ⚠️  (should use for-each)
G6.04 ⚠️  (missing break dependency)
G6.05 ❌ (unclear vs G6.06)
G6.06 ❌ (unclear vs G6.05)
G6.07 ⚠️  (overlaps G7.01)
G6.08 ✅
G6.09 ⚠️  (should be G5)

G7.01 ⚠️  (vague "simple rule")
G7.02 ⚠️  (confusing 1D note)
G7.03 ✅
G7.04 ✅

G8.01 ⚠️  (missing list dependency)
G8.02 ❌ (too abstract)
G8.02.01 ✅
G8.02.02 ✅
G8.02.03 ✅
G8.03 ✅
G8.04 ✅
```

## Critical Path (Minimum Skills for Basic Competency)

```
T07.K.01 (pattern recognition)
    ↓
T07.G1.01 (count repetitions)
    ↓
T07.G2.01 (when to repeat)
    ↓
T07.G3.01 (repeat N) ← GATEWAY
    ↓
T07.G3.03 (forever)
    ↓
T07.G4.01 (game loop)
    ↓
T07.G4.03 (counter)
    ↓
T07.G5.02 (build list)
    ↓
T07.G6.09 (for-each)
    ↓
T07.G7.04 (patterns)
```

**Minimum for basic loop literacy: 9 skills (22% of total)**

## CreatiCode Loop Block Coverage

```
Standard Scratch Blocks (undocumented):
----------------------------------------
repeat (N)           → G3.01, G3.02, G4.04
forever              → G3.03, G4.01
repeat until <cond>  → G3.04, G4.05, G6.04

CreatiCode Enhanced Blocks:
----------------------------
for [v] from-to-step → G4.03, G6.01, G6.02
repeat-times-at-int  → G4.08
break                → G6.04, G6.08
continue             → G6.08
for each item        → G6.09
for each index       → G6.09
```

## Recommended Skill Reordering

### Current G4 (8 skills - TOO MANY)
Move to G5:
- G4.07 (trace nested - needs maturity)
- G4.08 (timed repeat - specific feature)

### Current G6 (9 skills - HEAVY)
Move G6.09 (for-each) to G5
Result: G4=6, G5=6, G6=8 (more balanced)

## Gateway Skills (Must Master)

1. **T07.G3.01** - Use repeat N (first loop)
2. **T07.G3.03** - Forever loop (continuous behavior)
3. **T07.G3.04** - Repeat until (conditional loop)
4. **T07.G4.03** - Loop counter (tracking iterations)
5. **T07.G6.09** - For-each (clean iteration)

## Teaching Sequence Summary

```
Phase 1 (K-G2): Recognize patterns and repetition
Phase 2 (G3):   Build first loops (repeat, forever, until)
Phase 3 (G4):   Combine loops with logic and variables
Phase 4 (G5):   Apply loops to data (lists, simulations)
Phase 5 (G6):   Master advanced techniques (nested, for-each, break)
Phase 6 (G7):   Analyze and optimize loop algorithms
Phase 7 (G8):   Implement classic iterative algorithms
```

---

**Visual Legend:**
- ✅ No issues
- ⚠️  Minor issues (fixable)
- ❌ Critical issues (must fix)
- → Dependency flow
- ● Concept taught at this level

