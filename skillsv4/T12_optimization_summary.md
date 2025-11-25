# T12 (Organizing Programs) Optimization Summary

## Overview

Topic T12 focuses on code organization, documentation, naming conventions, custom blocks, and collaborative coding practices. This optimization addressed significant issues with skill granularity, dependency violations, and scaffolding gaps.

## Key Changes Made

### 1. Skills Broken Down into Smaller, Focused Skills

#### T12.G3.03.XX Series (Grade 3 Refactoring)
**Before:** 4 skills covering variable naming, reorder conditions, split scripts, combine blocks
**After:** 2 skills (removed over-advanced skills)
- **T12.G3.03.01** (kept): Use clearer variable names - added T09.G3.01 dependency
- **T12.G3.03.02** (renamed from .04): Combine similar consecutive blocks into one

**Removed (too advanced for G3):**
- "Reorder conditions to reduce nesting depth" - sophisticated refactoring concept
- "Split complex scripts into separate event-driven scripts" - covered by custom blocks

#### T12.G3.05 → Split into 3 Skills
**Before:** "Create and use a simple custom block without parameters" (1 skill)
**After:** 3 distinct skills
- **T12.G3.05.01**: Create a simple custom block without parameters
- **T12.G3.05.02**: Call a custom block from a script
- **T12.G3.06**: Add a comment describing what a custom block does (new)

#### T12.G4.04 → Split into 2 Skills
**Before:** "Analyze and improve variable scope and naming" (1 skill)
**After:** 2 distinct skills
- **T12.G4.04.01**: Improve variable naming in a project
- **T12.G4.04.02**: Understand and document variable scope

#### T12.G4.05 → Split into 3 Skills
**Before:** "Add input parameters to a custom block" (1 skill)
**After:** 3 scaffolded skills
- **T12.G4.05.01**: Define a custom block with one parameter
- **T12.G4.05.02**: Call a custom block with parameter values
- **T12.G4.05.03**: Define a custom block with multiple parameters

#### T12.G5.05 → Split into 4 Skills
**Before:** 3 skills (T12.G5.05, T12.G5.05.01, T12.G5.05.02)
**After:** 4 scaffolded skills
- **T12.G5.05.01**: Create a custom reporter block that returns a value
- **T12.G5.05.02**: Call a custom reporter block using report syntax
- **T12.G5.05.03**: Distinguish between command blocks and reporter blocks
- **T12.G5.05.04**: Create custom blocks with natural language-style signatures

### 2. Dependency Fixes

#### Grade 3 - Critical Missing Dependencies Added
- **T12.G3.03.01**: Added T09.G3.01 (must know variables before renaming them)
- **T12.G3.04**: Added T06.G3.01, T06.G3.02 (must understand events for multi-script)
- **T12.G3.04**: Added T12.G3.02 (header comments before explaining project structure)

#### Grade 4 - Cleaned Up X-2 Violations
- **T12.G4.01**: Removed T04.G2.03, T07.G2.01 (G2 deps at G4)
- **T12.G4.02**: Removed T03.G2.01, T03.G2.02, T06.G2.01, T06.G2.02 (G2 deps at G4)
- **T12.G4.03**: Removed T02.G2.01, T02.G2.02, T03.G2.01, T03.G2.02, T07.G2.01 (5 G2 deps!)
- **T12.G4.05**: Removed 7 G2 dependencies (massive cleanup)

#### Grade 5 - Improved Internal Flow
- **T12.G5.02**: Changed to depend on T12.G4.01 instead of T12.G3.01
- **T12.G5.03**: Added T12.G5.01, T12.G5.02 for proper scaffolding
- **T12.G5.04**: Changed to depend on T12.G5.01, T12.G5.02

#### Grade 6 - Fixed Missing Links
- **T12.G6.02**: Added T12.G6.01 dependency
- **T12.G6.03**: Removed T12.G4.02, T12.G4.04 (X-2 violation); added T12.G6.01
- **T12.G6.04**: Changed to depend on T12.G6.02, T12.G6.03

#### Grade 7 - Improved Progression
- **T12.G7.01**: Changed to depend on T12.G5.05.03, T12.G6.04
- **T12.G7.02**: Added T12.G7.01 dependency
- **T12.G7.03**: Added T12.G7.02 dependency
- **T12.G7.04**: Added T12.G7.03 dependency

#### Grade 8 - Removed Irrelevant Dependencies
- **T12.G8.01**: Removed T36.G6.01 (careers - irrelevant), T07.G6.01
- **T12.G8.02**: Removed T08.G6.01, T07.G6.01, T09.G6.02, T10.G6.01; added T12.G8.01
- **T12.G8.03**: Removed T06.G6.01, T08.G6.01, T09.G6.01, T10.G6.01; added T12.G8.02
- **T12.G8.04**: Removed T06.G6.01, T10.G6.01, T11.G6.01, T17.G6.01 (physics!); added T12.G8.03
- **T12.G8.05**: Removed T26.G6.01 (data), T34.G6.01 (history); added T12.G8.04

### 3. Skill Count Summary

| Grade | Before | After | Change |
|-------|--------|-------|--------|
| G1 | 4 | 4 | 0 |
| G2 | 4 | 4 | 0 |
| G3 | 9 | 8 | -1 (removed 2, added 1) |
| G4 | 5 | 8 | +3 |
| G5 | 7 | 8 | +1 |
| G6 | 4 | 4 | 0 |
| G7 | 4 | 4 | 0 |
| G8 | 5 | 5 | 0 |
| **Total** | **42** | **45** | **+3** |

## Specific Issues Resolved

### High Priority Issues Fixed:
1. **X-2 Rule Violations**: Cleaned up G4 skills that had 5-9 G2 dependencies
2. **Missing Critical Dependencies**: T12.G3.03.01 now requires T09 (variables)
3. **Over-Complex G3 Skills**: Removed advanced refactoring concepts from Grade 3
4. **Irrelevant Cross-Topic Dependencies**: Removed T36 (careers), T17 (physics), T26 (data), T34 (history) from G8 skills

### Medium Priority Issues Fixed:
1. **Skill Granularity**: Custom blocks broken into create/call/document
2. **Parameters**: Scaffolded from 1 parameter → calling → multiple parameters
3. **Reporter Blocks**: Scaffolded from create → call → distinguish → natural language

### Preserved Cross-Topic Dependencies:
- T01 (Algorithms): T01.GK.03, T01.G1.01
- T03 (Decomposition): T03.GK.01, T03.G1.02, T03.G1.03, T03.G5.01
- T04 (Patterns): T04.G3.01
- T06 (Events): T06.G3.01, T06.G3.02, T06.G6.01
- T07 (Loops): T07.G3.01, T07.G3.03, T07.G5.01
- T08 (Conditionals): T08.G3.01, T08.G3.03, T08.G5.01
- T09 (Variables): T09.G3.01, T09.G3.01.03, T09.G3.01.04, T09.G3.02, T09.G3.03, T09.G5.01, T09.G6.01
- T10 (Lists/Tables): T10.G5.01
- T11 (Functions): T11.G5.01, T11.G6.01
- T13 (Testing): T13.G6.01

## New Skill IDs Created

| Skill ID | Grade | Description |
|----------|-------|-------------|
| T12.G3.05.01 | G3 | Create a simple custom block without parameters |
| T12.G3.05.02 | G3 | Call a custom block from a script |
| T12.G3.06 | G3 | Add a comment describing what a custom block does |
| T12.G4.04.01 | G4 | Improve variable naming in a project |
| T12.G4.04.02 | G4 | Understand and document variable scope |
| T12.G4.05.01 | G4 | Define a custom block with one parameter |
| T12.G4.05.02 | G4 | Call a custom block with parameter values |
| T12.G4.05.03 | G4 | Define a custom block with multiple parameters |
| T12.G5.05.01 | G5 | Create a custom reporter block that returns a value |
| T12.G5.05.02 | G5 | Call a custom reporter block using report syntax |
| T12.G5.05.03 | G5 | Distinguish between command blocks and reporter blocks |
| T12.G5.05.04 | G5 | Create custom blocks with natural language-style signatures |

## Skills Removed/Renumbered

| Old ID | Action | Reason |
|--------|--------|--------|
| T12.G3.03.02 | Removed | "Reorder conditions" too advanced for G3 |
| T12.G3.03.03 | Removed | "Split scripts" covered by custom blocks |
| T12.G3.03.04 | Renumbered | Now T12.G3.03.02 (Combine similar blocks) |
| T12.G3.05 | Split | Now T12.G3.05.01 and T12.G3.05.02 |
| T12.G4.04 | Split | Now T12.G4.04.01 and T12.G4.04.02 |
| T12.G4.05 | Split | Now T12.G4.05.01, .02, .03 |
| T12.G5.05 | Renumbered | Now T12.G5.05.01 |
| T12.G5.05.01 | Renumbered | Now T12.G5.05.04 |
| T12.G5.05.02 | Renumbered | Now T12.G5.05.03 |

## Quality Improvements

1. **Each skill now focuses on ONE concept** (create vs. call vs. document)
2. **Clear scaffolding within grades** (1 param → call → multiple params)
3. **No X-2 violations remain** within T12 intra-topic dependencies
4. **Removed grade-inappropriate content** (advanced refactoring from G3)
5. **Clean G8 progression** without irrelevant cross-topic dependencies
