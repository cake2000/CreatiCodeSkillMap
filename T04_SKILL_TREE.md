# T04 Algorithm Patterns - Skill Tree Visualization

## Progression Overview

```
K → G1 → G2 → G3 → G4 → G5 → G6 → G7 → G8
4    4    5    8    8    7    7   10    6  = 59 skills
```

## Kindergarten: Visual Pattern Foundation (4 skills)

```
GK.01: Identify repeating pattern (ABAB, AABB)
  ↓
GK.02: Extend pattern by one tile
  ↓ ↓
GK.03: Describe pattern     GK.04: Fix broken pattern
```

## Grade 1: Action Patterns (4 skills)

```
       GK.02
         ↓
G1.01: Match picture to movement pattern
  ↓
G1.02: Plan repeating animation
  ↓
  ├→ G2.01 (feeds into Grade 2)

T01.GK.07 (from T01)
  ↓
G1.03: Find repeated steps in instruction list
  ↓
G1.04: Match picture story to step list
  ↓
  └→ G2.01 (feeds into Grade 2)
```

## Grade 2: Compression & Notation (5 skills)

```
G1.02 + G1.03
     ↓
G2.01: Identify repeating unit (ABCABC → ABC)
  ↓
G2.02: Spot repeated sequences in algorithms

T01.G2.02 (from T01)
  ↓
G2.03: Compare explicit vs "repeat" description
  ↓
G2.04: Replace steps with "repeat N times" phrase
  ↓
G2.05: Match "repeat box" diagram to repeated steps
  ↓
  └→ G3.01 (bridges to Grade 3 blocks)
```

## Grade 3: Block Patterns (8 skills)

```
        G2.05 + T07.G3.01
              ↓
G3.01: Identify where loop could replace blocks ⚠
  ↓
G3.02: Match repeat box to code blocks
  │
  ├→ G3.08: Match descriptions to code patterns ⚠
  │    ↓
  │    ├→ G4.05, G4.06, G4.07
  │
  └→ G4.01 (feeds Grade 4)

G2.03
  ↓
G3.03: Match "repeat N" loop to behavior ⚠ (should depend on G3.01)

T07.G3.02 + T03.G3.02
         ↓
G3.04: Recognize template ⚠ NEEDS SPLITTING
  ↓
G3.05: Customize template
  ↓
G3.06: Fix loop count ⚠ (remove T08.G3.01 dep)
  ↓
G3.07: Fix pattern with wrong step

[MISSING G3.09: Recognize nested loops] ← ADD THIS
```

## Grade 4: Complex Patterns (8 skills)

```
      G3.01 + T06.G3.01
            ↓
G4.01: Trace loop creating visual pattern

      G3.04 + T07.G3.01
            ↓
G4.02: Identify nested structure ⚠ (needs G3.09 first)

      G3.05 + T08.G3.01
            ↓
G4.03: Recognize "if" patterns for special cases
  ↓
G5.06: Identify changeable vs fixed parts

      G3.04 + G3.05
            ↓
G4.04: Identify template patterns ⚠ (built on problematic G3.04)
  ↓
G4.08: Use template to create project

      G3.08
        ↓
G4.05: Match snippets sharing same pattern ⚠ (G6.01, G6.02 should depend on THIS)
  ↓
  ├→ G5.01, G5.02, G5.03, G5.04 (algorithm patterns)
  │
  └→ G4.06: Identify when pattern solves problem
       ↓
       └→ G5.05

G4.07: Select reasons for reusing patterns

[MISSING G4.01b: Recognize counting in code] ← ADD THIS
[MISSING G4.09: Recognize for-each loop pattern] ← ADD THIS
```

## Grade 5: Algorithm Patterns (7 skills)

```
     G4.05 + T09.G3.01.04
            ↓
     ┌──────┴──────┐
     ↓             ↓
G5.01: Counter   G5.02: Accumulator
  ↓                 ↓
  └─────┬───────────┘
        ↓
  [MISSING G5.02a: Distinguish counter vs accumulator]
        ↓
G5.07: Apply counter to solve problem
  ↓
G6.07: Implement pattern-based solution

     G4.05 + T08.G3.01
            ↓
G5.03: Linear search pattern ⚠ (needs G4.09 for list iteration)
  ↓
  │ [MISSING G5.03b: Collect pattern] ← ADD THIS
  ↓
G5.04: Filter-and-collect pattern ⚠ (too complex jump)

     G4.06 + T09.G3.01.04
            ↓
G5.05: Compare pattern vs non-pattern solutions
  ↓
G6.06: Compare for efficiency and clarity

     G3.04 + G4.03
            ↓
G5.06: Identify changeable vs fixed parts
  ↓
G6.05: Analyze template customization points
```

## Grade 6: Pattern Application (7 skills)

```
     G4.04 + T09.G3.01.04
            ↓
G6.01: Group snippets by pattern ⚠ (should depend on G4.05, not G4.04)

     G4.04
       ↓
G6.02: Identify pattern variants ⚠ (should depend on G4.05)

     G5.01 + T11.G3.03 + T01.G3.01 + T07.G3.01
                  ↓
G6.03: Turn repeated code into custom block ⚠ (too many deps, remove G5.01 and T01.G3.01)
  ↓
  └→ G6.04: Add parameters to custom block

G5.06
  ↓
G6.05: Analyze template and identify customization

G5.05 + T07.G3.01 + T08.G3.01
         ↓
G6.06: Compare pattern solutions for efficiency
  ↓
G7.10: Compare for maintainability

G5.07 + G6.01
       ↓
G6.07: Implement pattern-based solution

[MISSING G6.08: Recognize 2D grid access pattern] ← ADD THIS
```

## Grade 7: Pattern Composition (10 skills)

```
     G6.01 + T07.G5.01 + T08.G5.01
              ↓
G7.01: Identify main loop patterns in game
  ↓
G8.03: Choose between alternative patterns

     G6.01 + T08.G5.01
            ↓
G7.02: Identify data structure patterns (list, grid) ⚠ (needs G6.08 for grid)

     G5.01 + G5.02 + G6.01
              ↓
G7.03: Identify problems requiring multiple patterns
  ↓
G7.04: Outline solution combining patterns
  ↓
G7.05: Implement combined pattern
  │
  ├→ G7.06: Trace composite pattern
  │    ↓
  │    └→ G7.07: Explain role of each pattern
  │
  └→ G7.08: Identify anti-patterns and mistakes

     G6.02 + T07.G5.01
            ↓
G7.09: Simplify by merging repeated patterns

     G6.06
       ↓
G7.10: Compare for long-term maintainability
  ↓
G8.04: Analyze tradeoffs (pattern vs custom)
```

## Grade 8: Advanced Patterns (6 skills)

```
[MISSING G8.00: Distinguish algorithm vs utility patterns] ← ADD THIS
              ↓
     G6.01 + T08.G6.01 + T09.G6.01
              ↓
G8.01: Recognize library patterns ⚠ (shift to utility patterns)
  ↓
G8.02: Adapt library function ⚠ (fix dependency name)

     G7.01 + T06.G6.01 + T07.G6.01
              ↓
G8.03: Choose between alternative patterns

     G7.10 + T06.G6.01 + T09.G6.01
              ↓
G8.04: Analyze tradeoffs (pattern vs custom)

     G6.01
       ↓
G8.05: Complete pattern card
  ↓
G8.06: Match pattern instructions to scenarios
```

## Pattern Categories Introduced by Grade

### K-G2: Basic Repeating Patterns
- Visual patterns (ABAB, AABB, ABCABC)
- Action patterns (movement, animation)
- Compression notation ("repeat N times")
- Repeat box diagrams

### G3-G4: Code Structure Patterns
- Loop patterns (single, nested)
- Conditional patterns (if for special cases)
- Template patterns (placeholders, customization)
- Pattern shape recognition

### G5: Algorithm Patterns
- **Counter**: Count occurrences
- **Accumulator**: Sum or concatenate
- **Search**: Find matching item
- **Filter**: Collect matching items

### G6-G7: Pattern Application & Composition
- Pattern grouping and variants
- Custom blocks as patterns
- Combining multiple patterns
- Anti-patterns and mistakes

### G8: Meta-Patterns
- Library/utility patterns
- Architectural pattern choices
- Tradeoffs and documentation

## Key Issues by Grade

- **GK**: ✓ Good foundation
- **G1**: ⚠ Minor dependency issue (G1.03)
- **G2**: ✓ Excellent progression
- **G3**: ⚠ Template too broad (G3.04), G3.08 overreaches, missing nested loop intro
- **G4**: ⚠ Nested loops jump (G4.02), missing counter intro, missing list iteration
- **G5**: ⚠ Counter/accumulator need distinction, search needs list prep, filter too complex
- **G6**: ⚠ Wrong dependencies (G6.01, G6.02, G6.03), missing grid scaffolding
- **G7**: ✓ Good progression, grid pattern needs prep
- **G8**: ⚠ Pattern category shift needs clarification

## Legend
- ✓ = Good, no issues
- ⚠ = Has issues (see notes)
- ← ADD THIS = Missing skill needed for scaffolding
- [MISSING X] = Recommended new skill
