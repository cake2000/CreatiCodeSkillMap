# Subagent Instructions for Skill Enrichment

## Your Task

You will analyze ONE topic file and add dependencies to each skill.

## Input

You will read:
1. The topic skill file (e.g., skills_T02_representing_tracing.md)
2. dependency_framework.md (guidelines)
3. T01_enriched_analysis.md (example)

## Output

Create a new markdown file named `T[NN]_enriched_analysis.md` with:

### Format for Each Skill

```markdown
#### T[NN].G[X].[YY] – [Skill Short Name]
- **Size**: [✓ Appropriate | ⚠ Too Large | ⚠ Too Small] ([reasoning])
- **Dependencies**: [[skill IDs]]
- **Notes**: [any important observations]
- **Grade-level check**: [✓ or ⚠ with explanation]
```

## Dependency Rules

### 1. Grade-Level Ordering
- A skill can ONLY depend on skills from the SAME grade or EARLIER grades
- If you find a dependency on a later grade, flag it as ⚠

### 2. Minimal Dependencies
- Only list DIRECT prerequisites
- Don't list transitive dependencies (if A→B and B→C, don't list A→C for C)

### 3. Common Cross-Topic Dependencies

#### For Programming Topics (T06-T13):
- **Events (T06)**: Foundation for most programming, minimal dependencies
- **Loops (T07)**: Depends on T06 (events), T04 (patterns for early grades), T01 (repeat concept for G2)
- **Conditionals (T08)**: Depends on T06 (events), T01 (if/then concept for G2)
- **Variables (T09)**: Depends on T06 (events)
- **Lists (T10)**: Depends on T09 (variables), T07 (loops to process)
- **Functions (T11)**: Depends on T03 (decomposition), T06, T09
- **Program Organization (T12)**: Depends on T03, T11
- **Testing (T13)**: Depends on T02 (tracing)

#### For Application Topics (T14-T24):
- **Games (T14)**: Depends on T06, T07, T08, T09
- **3D (T18)**: Depends on T14 or T15, spatial reasoning
- **AI topics (T21-T24)**: Depend on programming basics (T06-T09)

#### For Data Topics (T25-T29):
- **Representation (T25)**: Foundation
- **Collection (T26)**: Depends on T09, T10
- **Analysis (T27)**: Depends on T25, T26, T10
- **Chance/Sampling (T28)**: Depends on T25, T09, T07
- **Text/NLP (T29)**: Depends on T25, T22 (chatbots for later grades)

### 4. Within-Topic Dependencies

For early grades (K-2):
- Each skill typically depends on the previous skill in the same topic
- Grade 1 skills depend on foundational Grade K skills
- Grade 2 skills depend on Grade 1 skills

For middle grades (3-5):
- Skills depend on prior grade skills in same topic
- Start having rich cross-topic dependencies

For upper grades (6-8):
- Complex multi-topic dependencies
- Build on foundations from many topics

## Skill Size Guidelines

### ✓ Appropriate Size:
- Single clear learning objective
- 10-20 minute focused activity
- One primary concept assessed
- IXL-style granularity

### ⚠ Too Large (recommend splitting):
- Combines 2+ independent concepts
- Would take 30+ minutes
- Has multiple distinct assessment points
- Example: "Create a game with scoring, enemies, and levels" → Should be 3 skills

### ⚠ Too Small (recommend combining):
- Trivial variation of another skill
- No meaningful new concept
- Could be a sub-step of larger skill
- Example: "Move sprite left" + "Move sprite right" → Combine into "Move sprite with directional controls"

## Quality Checklist

Before finishing, verify:
- [ ] Every skill has a size assessment
- [ ] Every skill has dependencies listed (even if empty [])
- [ ] All dependencies reference valid skill IDs from same or earlier grades
- [ ] Grade-level checks completed for cross-topic dependencies
- [ ] Notes explain any non-obvious dependency choices
- [ ] Summary section at end with total skills, key patterns, issues found

## Output Format Example

See T01_enriched_analysis.md for complete example.

Start with:
```markdown
# T[NN] – [Topic Name]: Dependency Analysis

## Skill Review & Dependencies

### Grade K (PreK–K)
[skills...]

### Grade 1
[skills...]

[... through Grade 8]

## Summary

**Total Skills**: [N]
**Granularity**: [Assessment]
**Dependencies**: [Overview]
**Issues Found**: [List any problems]
**Key Dependency Patterns**: [Observations]
**Grade-Level Ordering**: [Status]
```

## Important Notes

- Use PLAIN TEXT in your analysis, not JSON objects
- Keep descriptions concise
- Focus on accuracy over speed
- When in doubt about a dependency, include it with a note explaining the reasoning
- Flag any skills that seem misplaced by grade level

## Example Dependency Reasoning

Good:
```markdown
#### T07.G3.02 – Create a forever game loop for controls
- **Dependencies**: [T07.G2.01, T06.G2.01, T08.G2.03]
  - T07.G2.01: Need to understand repeat loops first
  - T06.G2.01: Need to respond to key events
  - T08.G2.03: Need to use conditions inside loops
- **Notes**: Integrates loops, events, and conditionals for game control
- **Grade-level check**: ✓ All dependencies are Grade 2 or earlier
```

Bad:
```markdown
#### T07.G3.02 – Create a forever game loop for controls
- **Dependencies**: [some event stuff, loops maybe]
- **Notes**: for games
```

Now begin your analysis!
