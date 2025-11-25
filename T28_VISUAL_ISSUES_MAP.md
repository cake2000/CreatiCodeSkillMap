# T28 Visual Issues Map
**Generated**: 2025-11-25

## Issue Categories at a Glance

```
┌─────────────────────────────────────────────────────────────┐
│ T28 SKILLS ANALYSIS SUMMARY                                 │
├─────────────────────────────────────────────────────────────┤
│ Total Skills: 48 (G2:4, G3:7, G4:7, G5:11, G6:11, G7:6, G8:5)│
│                                                               │
│ CRITICAL: 4 skills TOO BROAD ⚠️                              │
│ IMPORTANT: 7 skills MISSING 📌                               │
│ QUALITY: 12 skills need better descriptions 📝               │
│ DEPENDENCIES: 19 changes needed (12 remove, 7 add) 🔗        │
└─────────────────────────────────────────────────────────────┘
```

---

## Skill Breakdown Needs

```
G3 ┃ ┌─────────────────────────────────┐
   ┃ │ T28.G3.05 (TOO BROAD)           │
   ┃ │ "Describe randomness in games"  │
   ┃ │ ❌ 3 tasks in one skill         │
   ┃ └─────────────────────────────────┘
   ┃         │
   ┃         ├─→ T28.G3.05.01: Identify randomness in games
   ┃         ├─→ T28.G3.05.02: Simulate one game element
   ┃         └─→ T28.G3.05.03: Analyze skill vs luck (optional)
───────────────────────────────────────────────────────────────

G7 ┃ ┌─────────────────────────────────┐
   ┃ │ T28.G7.06.01 (TOO BROAD)        │
   ┃ │ "Create 5-10 agent simulation"  │
   ┃ │ ❌ Huge jump from 2 agents      │
   ┃ └─────────────────────────────────┘
   ┃         │
   ┃         ├─→ T28.G7.06.01: Extend to 3-4 agents
   ┃         ├─→ T28.G7.06.02: Different agent behaviors
   ┃         ├─→ T28.G7.06.03: Scale to 5-10 agents
   ┃         └─→ T28.G7.06.04: Aggregate metrics
───────────────────────────────────────────────────────────────

G8 ┃ ┌─────────────────────────────────┐
   ┃ │ T28.G8.01 (CAPSTONE OVERLOAD)   │
   ┃ │ "Sim → Analysis → Dashboard"    │
   ┃ │ ❌ Multiple complex systems      │
   ┃ └─────────────────────────────────┘
   ┃         │
   ┃         ├─→ T28.G8.01.01: Manual parameter testing
   ┃         ├─→ T28.G8.01.02: Automate parameter sweep (exists as G6.01.02)
   ┃         ├─→ T28.G8.01.03: Static results dashboard
   ┃         ├─→ T28.G8.01.04: Add user scenario selection
   ┃         └─→ T28.G8.01.05: Auto-refresh (if possible)
```

---

## Progression Gaps (Missing Skills)

```
G3                G4                G5                G6
│                 │                 │                 │
├─ G3.07: Simple  │                 │                 │
│  random gen     │                 │                 │
│  (2-3 outcomes) │                 │                 │
│                 │                 │                 │
│  📌 MISSING:    │                 │                 │
│  G3.08: 4-6     │                 │                 │
│  outcome random │                 │                 │
│  ───────────────┼→ G4.01: Random  │                 │
│                 │  + if-statements│                 │
│                 │  (4 outcomes)   │                 │
│                 │                 │                 │
│                 │                 │                 │
│                 ├─ G4.01: Random  │                 │
│                 │  with if        │                 │
│                 │                 │                 │
│                 │  📌 MISSING:    │                 │
│                 │  G4.01.05:      │                 │
│                 │  Manual trial   │                 │
│                 │  logging (5-10) │                 │
│                 ├─────────────────┼→ G4.02.01:      │
│                 │                 │  Auto trial     │
│                 │                 │  logging (50)   │
│                 │                 │                 │
│                 │                 │                 │
│                 ├─ G4.07: Random  │                 │
│                 │  without repeat │                 │
│                 │                 │                 │
│                 │  📌 MISSING:    │                 │
│                 │  G4.08: Paired  │                 │
│                 │  random values  │                 │
│                 ├─────────────────┼→ G5.01.01:      │
│                 │                 │  Two dice +     │
│                 │                 │  sum analysis   │
│                 │                 │                 │
│                 │                 │                 │
│                 ├─ G4.06:         │                 │
│                 │  INTERPRET prob │                 │
│                 │  ❌ Wrong order  │                 │
│                 │                 ├─ G5.05:         │
│                 │                 │  CALCULATE prob │
│                 │                 │  ⬆ Move earlier │
│                 │                 │                 │
│                 │                 │                 │
│                 │                 ├─ G5.11: Law of  │
│                 │                 │  large numbers  │
│                 │                 │                 │
│                 │                 │  📌 MISSING:    │
│                 │                 │  G5.12: Observe │
│                 │                 │  run variation  │
│                 │                 ├─────────────────┼→ G6.02:
│                 │                 │                 │  Seeded random
│                 │                 │                 │
```

---

## Dependency Cleanup Map

```
┌───────────────────────────────────────────────────────────┐
│ BLOATED DEPENDENCIES (Remove These)                      │
└───────────────────────────────────────────────────────────┘

T28.G4.01 (Random + if-statements)
  ┣━━ ❌ T02.G2.01, T02.G2.02 ─── Picture sequencing not needed
  ┣━━ ❌ T04.G2.01, T04.G2.02 ─── Pattern recognition not needed
  ┣━━ ❌ T04.G2.03 ─────────────── Compression not needed
  ┣━━ ❌ T06.G2.01, T06.G2.02 ─── Cause-effect pictures not needed
  ┃
  ┣━━ ✅ T06.G2.03 ─────────────── If-then rules (relevant)
  ┣━━ ✅ T07.G2.01 ─────────────── When to repeat (relevant)
  ┣━━ ✅ T08.G3.01 ─────────────── Use if block (core)
  ┣━━ ✅ T09.G3.05 ─────────────── Trace variables (core)
  └━━ ✅ T28.G3.07 ────────────── Basic random (core)

T28.G4.02.01 (Log trial results)
  ┣━━ ❌ T05.G3.01, T05.G3.02 ─── Design skills not needed
  ┃
  ┣━━ ✅ T07.G3.01 ─────────────── Counted loops (core)
  ┣━━ ✅ T10.G3.03 ─────────────── List length (core)
  └━━ ✅ T28.G4.01 ────────────── Previous random skill (core)

T28.G4.02.02 (Count frequencies)
  ┣━━ ❌ T05.G3.01, T05.G3.02 ─── Design skills not needed
  ┃
  ┣━━ ✅ T09.G3.05 ─────────────── Trace variables (core)
  └━━ ✅ T28.G4.02.01 ──────────── Previous data skill (core)

┌───────────────────────────────────────────────────────────┐
│ MISSING DEPENDENCIES (Add These)                         │
└───────────────────────────────────────────────────────────┘

T28.G4.05 (Random coordinates)
  └─→ 📌 ADD: T28.G3.02 (Explain pick random)

T28.G4.07 (Random without repetition)
  ├─→ 📌 ADD: T28.G4.01 (Basic random understanding)
  └─→ 📌 ADD: T10.G4.17 (Insert random items block)

T28.G5.02 (Assign to conditions)
  └─→ 📌 ADD: T28.G4.02.01 (Log to lists)

T28.G5.08 (Track agent state)
  └─→ 📌 ADD: T28.G5.05 or .06 (Probability concepts)

T28.G6.10 (Sampling methods)
  └─→ 📌 ADD: T10.G4.x (List manipulation)

T28.G7.04 (Shuffle comparison)
  └─→ 📌 ADD: T10.G4.15 (Reshuffle block)
```

---

## Block Coverage Map

```
┌─────────────────────────────────────────────────────────┐
│ RANDOM/PROBABILITY BLOCKS IN CREATICODE                │
└─────────────────────────────────────────────────────────┘

Basic Random
  pick random (MIN) to (MAX)
  ├─ ✅ T28.G3.02: Explain what it does
  ├─ ✅ T28.G3.07: Build simple generator
  ├─ ✅ T28.G4.01: Use with if-statements
  └─ ⚠️  Many skills use but don't specify syntax

Random List Generation
  set [list] to (N) random whole numbers between (MIN) and (MAX) [method]
  └─ ⚠️  Taught in T10, never used in T28

  set [list] to (N) random numbers with seed (SEED)
  └─ ✅ T28.G6.02: Use for reproducibility

List Shuffling
  reshuffle [list] randomly
  ├─ ⚠️  Taught in T10.G4.15
  └─ ⚠️  Used in T28.G7.04 but not taught in T28
     📌 RECOMMEND: Add T28.G4.09 to teach in T28 context

  reshuffle table [table] randomly
  └─ ❌ Never used in T28

Random Selection
  insert (N) [random] items from [list1] into [list2]
  ├─ ⚠️  Taught in T10.G4.17
  └─ ⚠️  Could use in T28.G4.07 but doesn't
     📌 RECOMMEND: Update G4.07 to reference this

  pick random item from [list]
  └─ ⚠️  Assumed available, not explicitly taught in T28

Noise Function
  noise at x (X) y (Y) seed (SEED)
  └─ ❌ Never taught or used in T28
     📌 RECOMMEND: Add T28.G7.09 for procedural generation
```

---

## Quality Issues Map

```
VAGUE DESCRIPTIONS (Need Specific Examples)
═══════════════════════════════════════════

T28.G3.01 "Interpret provided simulation output"
  ❌ Vague: "pre-built CreatiCode project"
  ✅ Better: "pre-built 3-color spinner simulation"

T28.G4.04 "Debug an unfair simulation"
  ❌ Vague: "one outcome is favored"
  ✅ Better: "pick random 1-5 for 4 colors makes red twice as likely"

T28.G5.08 "Track agent state"
  ❌ Vague: "one additional state variable"
  ✅ Better: "foraging ant with has_food boolean variable"

T28.G6.04 "Simulate noisy sensors"
  ❌ Vague: "realistic variation"
  ✅ Better: "±10 pixels around true position using pick random"

T28.G6.11 "Conditional probability"
  ❌ Vague: "calculate probability given another event"
  ✅ Better: "run 1000 trials, count (first=blue), count (first=blue AND second=red)"

MISSING BLOCK SYNTAX (Need Explicit References)
═══════════════════════════════════════════════

T28.G4.02.01 "Log trial results to a list"
  📝 Add: add (result) to [trials]

T28.G4.02.02 "Count frequencies"
  📝 Add: if (item) = (color), change [count] by (1)

T28.G4.05 "Generate random coordinates"
  📝 Add: pick random (MIN) to (MAX) used twice

T28.G4.07 "Random selections without repetition"
  📝 Add: insert (N) [random] items from [list1] into [list2]

T28.G5.08 "Track position"
  📝 Add: set [x] to, set [y] to, change [x] by

T28.G6.05 "Grid world agent"
  📝 Add: set [gridX] to, set [direction] to

T28.G7.04 "Shuffle labels"
  📝 Add: reshuffle [list] randomly
```

---

## Skill Overlap Analysis

```
┌────────────────────────────────────────────────────────┐
│ OVERLAPPING SKILLS (Need Clarification)               │
└────────────────────────────────────────────────────────┘

T28.G5.08 vs T28.G6.05
Both: "Create sprite that tracks x,y position and state"

  T28.G5.08                    T28.G6.05
  "Track agent state"          "Model agent in grid"
  ┌─────────────────┐          ┌─────────────────┐
  │ Continuous      │          │ Discrete grid   │
  │ coordinates     │          │ positions       │
  │ (decimals OK)   │          │ (snap to grid)  │
  │                 │          │                 │
  │ Probabilistic   │          │ Directional     │
  │ movement        │          │ movement        │
  └─────────────────┘          └─────────────────┘

📝 RECOMMENDATION: Update descriptions to clarify distinction

────────────────────────────────────────────────────────────

T28.G4.02.03 vs T28.G4.06
Both: "Work with percentages in probability"

  T28.G4.02.03                 T28.G4.06
  "Calculate percentages"      "Interpret probabilities"
  ┌─────────────────┐          ┌─────────────────┐
  │ EXPERIMENTAL    │          │ THEORETICAL     │
  │ From simulation │          │ From counting   │
  │ results         │          │ outcomes        │
  │                 │          │                 │
  │ count/total×100 │          │ favorable/total │
  └─────────────────┘          └─────────────────┘

✅ Good separation, but add clarifying notes
```

---

## Implementation Roadmap

```
┌───────────────────────────────────────────────────────────┐
│ PHASE 1: CRITICAL FIXES (Priority 1)                     │
│ Estimated Time: 4-6 hours                                │
└───────────────────────────────────────────────────────────┘

Week 1
  ☐ Break down T28.G8.01 → 5 sub-skills
  ☐ Break down T28.G3.05 → 2-3 sub-skills
  ☐ Break down T28.G7.06.01/.02 → 4 sub-skills
  ☐ Clean dependencies (remove T02, T05 from G4 skills)

┌───────────────────────────────────────────────────────────┐
│ PHASE 2: FILL GAPS (Priority 2)                          │
│ Estimated Time: 3-4 hours                                │
└───────────────────────────────────────────────────────────┘

Week 2
  ☐ Add T28.G3.08 (4-6 outcome random)
  ☐ Add T28.G4.01.05 (manual trial logging)
  ☐ Add T28.G4.08 (paired random values)
  ☐ Reorganize G4.06/G5.05 (calc before interpret)
  ☐ Add missing dependencies (7 additions)

┌───────────────────────────────────────────────────────────┐
│ PHASE 3: QUALITY (Priority 3)                            │
│ Estimated Time: 2-3 hours                                │
└───────────────────────────────────────────────────────────┘

Week 3
  ☐ Add specific examples to 5 vague skills
  ☐ Add block syntax to 7 skills
  ☐ Clarify G5.08 vs G6.05 distinction
  ☐ Update T28.G4.07 block reference

┌───────────────────────────────────────────────────────────┐
│ PHASE 4: ENHANCEMENT (Priority 4)                        │
│ Estimated Time: 2-3 hours                                │
└───────────────────────────────────────────────────────────┘

Week 4
  ☐ Add T28.G3.09 (why simulate)
  ☐ Add T28.G5.12 (run variation)
  ☐ Add T28.G7.09 (noise function)
  ☐ Add T28.G4.09 (reshuffle block)
  ☐ Create T28 Block Reference Guide

TOTAL ESTIMATED TIME: 11-16 hours
```

---

## Success Metrics

After fixes, verify:

```
DEPENDENCY CHECKS
  ☐ No circular dependencies
  ☐ No forward dependencies within T28
  ☐ X-2 rule satisfied for all cross-topic dependencies
  ☐ All dependencies are necessary and relevant

SKILL SCOPE CHECKS
  ☐ No skill teaches 3+ distinct concepts
  ☐ All skills completable in ~30 minutes
  ☐ Smooth progression (no big jumps)

QUALITY CHECKS
  ☐ All skills have specific examples
  ☐ All coding skills reference specific blocks
  ☐ Descriptions are clear and concrete
  ☐ Grade-level appropriate (K-2 pictures, G3+ blocks)

COVERAGE CHECKS
  ☐ All CreatiCode random/probability blocks taught
  ☐ No major gaps in progression
  ☐ Foundational concepts precede advanced applications
```

---

## Contact/Questions

For questions about this analysis:
- See detailed analysis: T28_COMPREHENSIVE_ANALYSIS.md
- See quick reference: T28_ISSUES_QUICK_REFERENCE.md
- See this visual map: T28_VISUAL_ISSUES_MAP.md
