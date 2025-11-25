# T11 (Functions & Procedures) Optimization Summary

## Overview

Topic T11 has been comprehensively optimized for Phase 1 of the skill map improvement process. The topic now covers custom blocks (My Blocks) in CreatiCode from kindergarten through grade 8 with proper scaffolding and skill granularity.

## Key Statistics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total Skills | 41 | 75 | +34 (+83%) |
| Grade Coverage | G3-G8 | GK-G8 | +3 grades |
| K-2 Skills | 0 | 12 | +12 |
| Sub-skills (broken down) | 0 | 22 | +22 |

## Major Changes

### 1. Added K-2 Foundation (12 new skills)

These unplugged/picture-based skills build conceptual foundations before coding:

**Kindergarten (3 skills):**
- T11.GK.01: Group activities that belong together
- T11.GK.02: Name a group of activities
- T11.GK.03: Use a named group in a bigger plan

**Grade 1 (4 skills):**
- T11.G1.01: Find repeated groups of activities
- T11.G1.02: Create labels for repeated activity groups
- T11.G1.03: Use a label to replace repeated activity groups
- T11.G1.04: Recognize the need for different versions of similar groups

**Grade 2 (5 skills):**
- T11.G2.01: Identify when to create activity groups for organization
- T11.G2.02: Create multiple labeled groups that work together
- T11.G2.03: Explain dependencies between labeled groups
- T11.G2.04: Recognize when labeled groups can be reused in different plans
- T11.G2.05: Describe the purpose of each labeled group

### 2. Skills Broken Down into Smaller Units

**T11.G3.05 (Explore Make a Block interface) -> 2 skills:**
- T11.G3.05.01: Explore the "Make a Block" interface basics
- T11.G3.05.02: Add one parameter to a custom block interface

**T11.G4.06 (Understand argument block) -> 2 skills:**
- T11.G4.06.01: Identify the argument block in a custom block definition
- T11.G4.06.02: Trace the flow of a parameter value through a custom block

**T11.G5.01 (Decompose problem) -> 2 skills:**
- T11.G5.01.01: Identify 2-3 main responsibilities in a project description
- T11.G5.01.02: Create a complete custom block decomposition plan

**T11.G5.02 (Use custom blocks in larger project) -> 2 skills:**
- T11.G5.02.01: Create 2-3 parameterized custom blocks for a small project
- T11.G5.02.02: Demonstrate code reuse with parameterized custom blocks

**T11.G6.01 (Design clear interfaces) -> 3 skills:**
- T11.G6.01.01: Choose clear, descriptive names for custom blocks
- T11.G6.01.02: Design clear parameter lists for custom blocks
- T11.G6.01.03: Design complete custom block interfaces before implementation

**T11.G6.02 (Create modular programs) -> 2 skills:**
- T11.G6.02.01: Create a program with 4-6 coordinated custom blocks
- T11.G6.02.02: Verify custom block independence and isolation

**T11.G7.02 (Design coordinated block set) -> 3 skills:**
- T11.G7.02.01: Plan a coordinated set of 3-5 custom blocks for one feature
- T11.G7.02.02: Implement a coordinated set of custom blocks for one feature
- T11.G7.02.03: Document a coordinated custom block set

### 3. New Extension Skills Added

**Grade 3:**
- T11.G3.00: Distinguish custom blocks from built-in blocks (new foundational skill)

**Grade 4:**
- T11.G4.01.01: Call a custom block from multiple places
- T11.G4.03.01: Nest reporter blocks inside other reporters
- T11.G4.07.01: Call the same custom block with different parameter values
- T11.G4.09: Recognize when to use a parameter vs a fixed value

**Grade 5:**
- T11.G5.03.01: Debug incorrect parameter order
- T11.G5.08.01: Use custom reporter return value in multiple contexts
- T11.G5.12: Identify when code duplication signals need for custom block

**Grade 6:**
- T11.G6.03.01: Handle invalid inputs gracefully in custom blocks
- T11.G6.09: Compare before and after code organization

**Grade 7:**
- T11.G7.05: Understand when custom blocks call each other (helper blocks)

**Grade 8:**
- T11.G8.06: Create a reusable block library across projects
- T11.G8.07: Refactor redundant custom blocks into general versions

### 4. Dependency Fixes

**Removed problematic dependencies:**
- Removed T12.G3.05 and T12.G4.05 dependencies from all G5 skills (12 removals)
- These cross-topic dependencies were not appropriate for basic function usage

**Fixed internal T11 dependencies:**
- T11.G4.06.01 now depends on T11.G4.01 (must create blocks before understanding argument block)
- T11.G4.07 now depends on T11.G4.06.01 (understand argument block before creating parameterized blocks)
- Added proper T11.G3.00 as dependency for T11.G3.02

**Fixed external reference:**
- Changed T08.G6.01a to T08.G6.01 (invalid skill ID)

**Preserved all valid cross-topic dependencies:**
- All dependencies to other topics (T01, T02, T03, T04, T06, T07, T08, T09, T10, T13, T17, T22) were preserved

### 5. Skill Description Improvements

**T11.G3.04 (renamed):**
- Was: "Understand the concept of return values"
- Now: "Identify reporter blocks in existing code"
- Rationale: Focuses on observable behavior at G3 level; "return values" concept deferred to G5

**T11.G4.02 (clarified):**
- Removed `report` syntax discussion (deferred to G5)
- Focused on conceptual distinction between command and reporter blocks
- Clarified that students categorize BUILT-IN blocks first

**T11.G6.05 (renamed):**
- Was: "Add error handling to custom blocks"
- Now: "Add input validation to custom blocks"
- Rationale: More specific and achievable at this level

**T11.G6.08 (improved):**
- Was: vague discussion of "side effects"
- Now: Clear language about "blocks that change variables/move sprites" vs "blocks that calculate and return values"

**T11.G7.03 (enhanced):**
- Added concrete examples comparing well-encapsulated vs poorly-encapsulated blocks
- Made abstract concepts concrete with specific code scenarios

## CreatiCode My Blocks Integration

All skills accurately reflect the 6 blocks available in CreatiCode's My Blocks category:

1. `define (BLOCKSIGNATURE)` - Covered in G3.05.01, G3.05.02, G4.01, G4.07, G5.06, G5.11
2. `call BLOCKSIGNATURE` - Covered in G4.01, G4.01.01, G4.07.01, G5.02.01
3. `report BLOCKSIGNATURE` - Covered in G5.08, G5.08.01
4. `(argument (ARGUMENTNAME))` - Covered in G4.06.01, G4.06.02, G4.07
5. `return [VALUE]` - Covered in G5.08
6. `// [COMMENT]` - Covered in G5.10

## Skill Progression Summary

| Grade | Focus | Skill Count |
|-------|-------|-------------|
| K | Grouping and naming activities (unplugged) | 3 |
| 1 | Finding repetition, creating labels (unplugged) | 4 |
| 2 | Multiple groups, dependencies, reuse (unplugged) | 5 |
| 3 | Introduction to custom blocks concept, exploring interface | 7 |
| 4 | Creating simple blocks, parameters, tracing | 12 |
| 5 | Multi-parameter blocks, reporters, design decisions | 14 |
| 6 | Interface design, testing, refactoring, evaluation | 13 |
| 7 | Algorithms, coordinated blocks, encapsulation, helper blocks | 7 |
| 8 | General-purpose blocks, libraries, hierarchical structures | 7 |

## Quality Assurance

- All 75 skills have complete metadata (ID, Topic, Skill, Description, Dependencies)
- All skills have concrete assessment examples
- All skills follow the IXL-style granularity (small, focused, assessable)
- All Grade 3+ skills involve CreatiCode block-based coding
- All K-2 skills are unplugged/picture-based
- No duplicate or overlapping skills within topic
- Proper scaffolding from simple to complex across grades
