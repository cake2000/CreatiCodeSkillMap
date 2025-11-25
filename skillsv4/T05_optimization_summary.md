# T05 (Human-Centered Design) Phase 1 Optimization Summary
Applied: 2025-11-25

## Overview
Topic T05 covers Human-Centered Design skills from Kindergarten through Grade 8. This optimization focused on improving skill clarity, breaking down overly broad skills into manageable IXL-style components, ensuring K-2 content is picture-based, adding scaffolding skills, and fixing intra-topic dependencies.

## Changes Made

### 1. K-2 Picture-Based Content Fixes (6 skills updated)

| Skill ID | Original Title | New Title | Change |
|----------|---------------|-----------|--------|
| T05.G1.01 | Identify what a character needs in a story | Identify what a character needs from pictures | Changed from read/hear scenarios to picture-based activity |
| T05.G1.02 | Match a need to a design idea | Match a need picture to a design solution picture | Changed to drag-and-drop picture matching |
| T05.G1.03 | Choose a better version of a simple screen for a given user | Choose a better screen version for a pictured user | Changed from "described user" to pictured user |
| T05.G1.04 | Suggest one change that helps a specific user | Choose one change picture that helps a pictured user | Changed to picture-based selection |
| T05.G2.02 | Identify features that make a design more accessible | Circle accessibility features in a picture | Changed to visual feature identification |
| T05.G2.03 | Recognize when a situation could be simulated | Match real situations to pretend computer versions | Removed written explanation requirement |

### 2. Skills Broken Down into Smaller Components

#### T05.G5.02 (Wireframing) - Split into 4 sub-skills:
| Skill ID | Title | Description |
|----------|-------|-------------|
| T05.G5.02 | Arrange UI elements to create a basic wireframe | Focus on spatial arrangement only |
| T05.G5.02a | Label wireframe elements with their purpose | Practice connecting elements to functions |
| T05.G5.02b | Explain how wireframe elements support user tasks | Connect elements to requirements |
| T05.G5.02c | Create two design alternatives for the same user need | Compare design tradeoffs |

#### T05.G7.01 (Accessibility Review) - Split into 4 sub-skills:
| Skill ID | Title | Description |
|----------|-------|-------------|
| T05.G7.01 | Check color contrast and text readability in a project | Focused on visual accessibility |
| T05.G7.01a | Check keyboard navigation and timing controls | Focused on interaction accessibility |
| T05.G7.01b | Check captions and alternative text | Focused on media accessibility |
| T05.G7.01c | Complete a full accessibility review with evidence | Comprehensive review combining all categories |

#### T05.G8.01 (Design Brief) - Split into 4 sub-skills:
| Skill ID | Title | Description |
|----------|-------|-------------|
| T05.G8.01 | Identify and describe target users for a design | Focus on user description |
| T05.G8.01a | Define specific design goals for a project | Focus on measurable goals |
| T05.G8.01b | List design constraints for a project | Focus on constraints identification |
| T05.G8.01c | Combine users, goals, and constraints into a design brief | Complete document assembly |

### 3. New Skills Added for Better Scaffolding

| Skill ID | Title | Purpose |
|----------|-------|---------|
| T05.G3.07 | Identify which questions a simulation can answer | Bridge simulation understanding (G2→G4) |
| T05.G3.08 | Identify which accessibility features are present in a design | Bridge feature matching (G3.06) to issue recognition (G4.03) |
| T05.G4.05a | Formulate questions a simulation should answer | Bridge G3.07 to G5/G6 simulation skills |
| T05.G4.08 | Write simple interview questions to learn about users | Bridge user research from G3.02 to G6.03 |

### 4. Dependency Fixes

#### Updated Internal Dependencies:
- T05.G3.02: Updated dependency name to "Identify what a character needs from pictures"
- T05.G3.03: Updated dependency to "Circle accessibility features in a picture"
- T05.G3.06: Updated dependency to "Circle accessibility features in a picture"
- T05.G4.03: Changed dependency from T05.G3.03 to T05.G3.08 (better scaffolding)
- T05.G5.03: Fixed incomplete dependency, added T05.G4.05a, added proper skill names
- T05.G5.05: Fixed incomplete dependencies, added T05.G4.07, added proper skill names
- T05.G6.03: Changed dependency to T05.G4.08 (better user research scaffolding)
- T05.G6.08: Changed T05.G3.07 to T05.G4.05a (X-2 rule compliance)
- T05.G7.02: Updated to depend on T05.G7.01c (full accessibility review)
- T05.G8.02: Updated to depend on T05.G8.01c (complete design brief)
- T05.G8.06: Updated to depend on T05.G8.01c (complete design brief)

### 5. X-2 Rule Violations Fixed
- T05.G5.03: Removed G3.07 dependency, replaced with G4.05a
- T05.G6.08: Removed G3.07 dependency, replaced with G4.05a

## Final Skill Count

| Grade | Original Count | New Count | Change |
|-------|---------------|-----------|--------|
| GK | 4 | 4 | No change |
| G1 | 4 | 4 | Titles/descriptions updated |
| G2 | 4 | 4 | Titles/descriptions updated |
| G3 | 6 | 8 | +2 new skills |
| G4 | 7 | 9 | +2 new skills (G4.05a, G4.08) |
| G5 | 7 | 9 | +2 from breakdown |
| G6 | 8 | 8 | No change |
| G7 | 8 | 11 | +3 from breakdown |
| G8 | 6 | 9 | +3 from breakdown |
| **Total** | **54** | **66** | **+12 skills** |

## Quality Improvements

1. **Age-Appropriateness**: All K-2 skills now explicitly use picture-based activities
2. **Granularity**: Complex skills broken into focused, manageable sub-skills (IXL-style)
3. **Scaffolding**: New intermediate skills provide smoother learning progressions
4. **Dependency Clarity**: All dependencies now have complete skill names
5. **X-2 Rule Compliance**: All intra-topic dependencies now follow the grade proximity rule

## Key Learning Progression Tracks

### HCD Process Track:
GK.01→GK.02→GK.03→GK.04→G1.01→G1.02→G1.03→G1.04→G2.01→G3.01→G4.01→G4.02→G5.01→G6.01→G7.03→G8.01→G8.01a→G8.01b→G8.01c

### Accessibility Track:
G1.04→G2.02→G3.06→G3.08→G4.03→G4.04→G5.05a→G7.01→G7.01a→G7.01b→G7.01c→G7.02

### Simulation Track:
G2.03→G2.04→G3.04→G3.05→G3.07→G4.05→G4.05a→G4.06→G5.03→G5.04→G5.06→G6.05→G6.06→G6.08→G7.08→G8.03→G8.04

### User Research Track:
G3.02→G4.01→G4.08→G6.03→G6.04→G7.05→G7.06→G7.07→G8.05

### Testing Track:
G3.03→G4.07→G5.05→G6.07→G7.05→G8.04

## Cross-Topic Dependencies Preserved

All dependencies on other topics were preserved as required by Phase 1 rules:
- T04.G2.03 (Patterns)
- T07.G2.01, T07.G5.01, T07.G6.01 (Loops)
- T08.G5.00, T08.G5.01, T08.G6.01a (Conditionals)
- T09.G3.03, T09.G5.01 (Variables)
- T10.G5.01, T10.G6.01 (Lists/Tables)
- T12.G6.01 (Program Organization)
- T13.G3.01, T13.G6.01 (Testing)
- T22.G6.01.01 (Chatbots)
- T30.G6.01 (Hardware)
- T35.G6.01 (Impacts/Ethics)

These will be reviewed in Phase 2 (cross-topic optimization).

## Validation Status

All 66 T05 skills have been verified for:
- ✓ Unique skill IDs following T05.G#.## pattern
- ✓ Intra-topic dependencies reference valid existing skills
- ✓ X-2 rule compliance (dependencies within 2 grade levels)
- ✓ No circular dependencies
- ✓ Age-appropriate content (K-2 picture-based, G3+ text/conceptual)
