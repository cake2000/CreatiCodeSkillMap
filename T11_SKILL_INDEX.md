# T11 (Functions & Procedures) - Skill Index

## Quick Reference Guide

### Grade 3 - Conceptual Foundation (5 skills)
- **T11.G3.01**: Understand when to use custom blocks vs loops
- **T11.G3.02**: Use a pre-made custom block with parameters
- **T11.G3.03**: Identify repeated or grouped actions that could become custom blocks
- **T11.G3.04**: Understand the concept of return values
- **T11.G3.05**: Explore the "Make a Block" interface in CreatiCode

### Grade 4 - Basic Custom Blocks (6 skills)
- **T11.G4.01**: Define and call a simple custom block (no parameters)
- **T11.G4.02**: Distinguish command blocks from reporter blocks
- **T11.G4.03**: Use a reporter block's result in a calculation or condition
- **T11.G4.04**: Describe the purpose of each custom block in a script
- **T11.G4.05**: Trace execution through a script with custom blocks
- **T11.G4.06**: Understand the argument block for accessing parameters

### Grade 5 - Parameterized Blocks (8 skills)
- **T11.G5.01**: Decompose a problem into logical custom block boundaries
- **T11.G5.02**: Define a custom block with one parameter
- **T11.G5.02.5**: Match parameter names to argument values when calling custom blocks ⭐ NEW
- **T11.G5.03**: Choose between adding a parameter vs. creating a separate block
- **T11.G5.04**: Analyze a modular program structure
- **T11.G5.05**: Define a custom block with two or more parameters
- **T11.G5.05.5**: Decide whether a custom block should be a command or reporter ⭐ NEW
- **T11.G5.06**: Define a custom reporter block that returns a value
- **T11.G5.07**: Debug a script with incorrect custom block calls
- **T11.G5.08**: Use comments to document custom block purpose

### Grade 6 - Modular Design (5 skills)
- **T11.G6.01**: Design custom blocks with clear, predictable interfaces
- **T11.G6.02**: Create modular programs with multiple custom blocks
- **T11.G6.02.5**: Test custom blocks with boundary and edge cases ⭐ NEW
- **T11.G6.03**: Refactor spaghetti code into organized custom blocks
- **T11.G6.04**: Evaluate and critique custom block designs

### Grade 7 - Advanced Concepts (4 skills)
- **T11.G7.01**: Implement algorithms as reusable custom blocks
- **T11.G7.02**: Design a set of related custom blocks for a subsystem
- **T11.G7.03**: Understand encapsulation and information hiding
- **T11.G7.04**: Trace and debug multi-level custom block calls

### Grade 8 - Mastery & Application (4 skills)
- **T11.G8.01**: Design a reusable library of custom blocks for games
- **T11.G8.02**: Refactor a large program into a hierarchical block structure
- **T11.G8.03**: Create custom blocks that work with lists and complex data
- **T11.G8.04**: Analyze trade-offs between modular and inline code

## New Skills Added (Phase 1 Optimization)

### T11.G5.02.5 - Match parameter names to argument values
**Why added**: Students need explicit practice understanding how argument values map to parameter names before working with multiple parameters. This scaffolding prevents confusion when parameters are in different orders.

**Key learning**: Positional matching between arguments and parameters

### T11.G5.05.5 - Decide whether a custom block should be a command or reporter
**Why added**: Students need explicit practice making this design decision before creating reporter blocks. Without this skill, they struggle to choose the appropriate block type.

**Key learning**: Commands DO something, reporters COMPUTE something

### T11.G6.02.5 - Test custom blocks with boundary and edge cases
**Why added**: Testing is a critical skill gap between creating blocks and evaluating them. Students need to learn systematic testing practices.

**Key learning**: Test with normal inputs, boundary values (0, negative, very large), and edge cases

## Major Improvements (Phase 1 Optimization)

### Dependency Fixes
1. **G4.04** and **G4.05**: Now require G4.01 and G4.02 (basic custom block skills)
2. **G5.02**: Changed from G4.05 to G4.06 dependency (more logical prerequisite)
3. **G5.05**: Now requires G5.02 (one parameter before multiple)
4. **G5.08**: Now requires both G5.02 and G5.06 (documenting both block types)

### Scope Reductions
1. **G7.01**: Reduced from multiple algorithms to ONE algorithm with thorough testing
2. **G8.01**: Reduced from library + two projects to 3-5 blocks in one project with multiple contexts

### Clarity Improvements
1. **G3.03**: Clarified as ANALYSIS of existing code (vs G5.01's DESIGN before coding)
2. **G4.03**: Added forward reference to creating custom reporters in G5
3. **G5.04**: Specified focus on MAJOR COMPONENTS with diagram requirement
4. **G6.04**: Added explicit DESIGN CRITERIA list and example problems

## Learning Progressions

### Parameter Mastery Path
1. G3.02: Use pre-made blocks with parameters
2. G4.06: Understand the argument block
3. G5.02: Define block with ONE parameter
4. G5.02.5: Match arguments to parameters ⭐
5. G5.05: Define block with MULTIPLE parameters

### Block Type Understanding Path
1. G3.04: Understand return values concept
2. G4.02: Distinguish commands from reporters
3. G4.03: Use reporter results
4. G5.05.5: Decide command vs reporter ⭐
5. G5.06: Define custom reporter blocks

### Testing & Debugging Path
1. G5.07: Debug incorrect custom block calls
2. G6.02.5: Test with boundary and edge cases ⭐
3. G6.04: Evaluate and critique designs
4. G7.04: Trace and debug multi-level calls

## Total Skills by Grade

- Grade 3: 5 skills (Conceptual)
- Grade 4: 6 skills (Basic)
- Grade 5: 8 skills (Parameterized) ⭐ +2 new
- Grade 6: 5 skills (Modular) ⭐ +1 new
- Grade 7: 4 skills (Advanced)
- Grade 8: 4 skills (Mastery)

**Total: 33 skills** (was 30, added 3 in Phase 1)

## File Location
`/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`
Lines 6107-6461 (355 lines)
