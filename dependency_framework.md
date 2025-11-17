# Skill Dependency Mapping Framework

## Principles

### 1. Dependency Types
- **Prerequisite (hard)**: Skill A MUST be mastered before Skill B can be attempted
- **Related (soft)**: Skill A enhances understanding of Skill B but isn't strictly required
- **Co-requisite**: Skills that build on each other and could be learned together

### 2. Dependency Rules
1. **Grade-level ordering**: A skill can only depend on skills from the same grade or earlier grades
2. **Within-topic progression**: Skills within a topic naturally build on previous skills in that topic
3. **Cross-topic dependencies**: Identify when skills require concepts from other topics
4. **Minimal dependencies**: Only list direct prerequisites, not transitive ones

### 3. Common Dependency Patterns

#### Within Algorithms & Design (T01-T05)
- T01 (Everyday Algorithms): Foundation for algorithm thinking
- T02 (Representing & Tracing): Depends on T01 for algorithm concepts
- T03 (Decomposition): Depends on T01 for understanding multi-step processes
- T04 (Patterns): Depends on T01 for recognizing repetition
- T05 (Human-Centered Design): Depends on T01, T03 for design thinking

#### Programming Core (T06-T13)
- T06 (Events): Foundation for all programming - minimal dependencies
- T07 (Loops): Depends on T06 (events to trigger loops), T04 (pattern recognition)
- T08 (Conditionals): Depends on T06 (events), T01 (if/then thinking)
- T09 (Variables): Depends on T06 (events), used by T07, T08
- T10 (Lists): Depends on T09 (variables), T07 (loops to process lists)
- T11 (Functions): Depends on T03 (decomposition), T06 (events), T09 (variables/parameters)
- T12 (Program Organization): Depends on T03, T11
- T13 (Testing): Depends on T02 (tracing), can work with any programming topic

#### Applications (T14-T24)
- T14 (Games): Depends on T06, T07, T08, T09
- T15-T23: Various applications, each with specific dependencies
- T24 (XO AI Practices): Meta-skill, depends on many others

#### Data (T25-T29)
- T25 (Data Representation): Foundation for data
- T26-T29: Build on T25 and require T09, T10

#### Systems & Society (T30-T36)
- Mostly conceptual, lighter dependencies on programming topics

### 4. Grade-Level Dependency Guidelines

**Grade K**: Minimal dependencies (foundational skills)
**Grade 1**: Depends primarily on Grade K of same topic
**Grade 2**: Depends on G1 + may start cross-topic dependencies
**Grade 3**: First significant cross-topic dependencies (coding starts)
**Grade 4-5**: Rich cross-topic dependencies
**Grade 6-8**: Complex multi-topic dependencies

### 5. Skill Size Guidelines (IXL-style)

**Too Large** (should be split):
- Combines multiple distinct concepts
- Takes more than one focused session
- Has multiple independent assessment points

**Appropriate Size**:
- Single clear learning objective
- Can be completed in 10-20 minutes
- Has one primary concept being assessed
- Builds incrementally on prerequisites

**Too Small** (should be combined):
- Trivial extension of another skill
- No meaningful new concept
- Could be assessed as part of a larger skill

## Process for Each Skill

1. **Review skill description**: Is it focused and appropriately sized?
2. **Identify within-topic prerequisites**: What prior skills in this topic are needed?
3. **Identify cross-topic prerequisites**: What skills from other topics are needed?
4. **Check grade-level consistency**: Are all dependencies from same grade or earlier?
5. **Validate**: Test dependency logic - can student realistically do skill with just those prerequisites?
