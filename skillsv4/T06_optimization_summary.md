# T06 – Events & Sequences: Phase 1 Optimization Summary

## Overview
- **Previous skill count**: ~70 skills
- **New skill count**: 87 skills
- **Net change**: +17 skills added for better coverage and granularity

## Key Changes Made

### 1. Added Missing CreatiCode Event Blocks (NEW SKILLS)
Based on analysis of CreatiCode's blockdes8.txt, added skills for event blocks that were missing or underrepresented:

| New Skill ID | Skill Name | Grade |
|--------------|------------|-------|
| T06.G3.02 | Use "prepare for green flag click" for initialization | G3 |
| T06.G3.05 | Use "when backdrop switches to" for scene changes | G3 |
| T06.G3.06 | Use "when I start as a clone" for cloned sprites | G3 |
| T06.G7.09 | Use "when variable changed" events for reactive UI updates | G7 |
| T06.G8.05 | Use "when added to game" for multiplayer initialization | G8 |
| T06.G8.06 | Use "broadcast to all players" for multiplayer coordination | G8 |

### 2. Skill Renumbering for Better Progression
Reorganized Grade 3 skills for clearer scaffolding:
- T06.G3.01: when green flag clicked (foundation)
- T06.G3.02: prepare for green flag (initialization before green flag)
- T06.G3.03: when key pressed (user input)
- T06.G3.04: when sprite clicked (interaction)
- T06.G3.05: when backdrop switches (scene management)
- T06.G3.06: when I start as clone (clone initialization)
- T06.G3.07-12: Understanding and debugging events

### 3. Fixed Dependency Issues

#### X-2 Rule Violations Fixed:
- Removed dependencies that went more than 2 grades back
- Ensured all intra-topic dependencies follow the X-2 rule (dependencies only from grades X, X-1, or X-2)

#### Dependency Simplification:
- Reduced excessive dependencies on each skill
- Removed redundant same-grade dependencies (implied by skill ordering)
- Kept only direct prerequisite dependencies

#### Examples of Fixed Dependencies:
| Skill | Before | After |
|-------|--------|-------|
| T06.G4.02 | T06.G2.01, T06.G2.02, T06.G3.01, T06.G4.01 | T06.G4.01 |
| T06.G4.03 | T06.G2.01, T06.G2.02, T06.G3.01, T06.G4.02 | T06.G4.02 |
| T06.G4.04 | T06.G2.01, T06.G2.02, T06.G3.01, T06.G4.03 | T06.G4.03 |

### 4. Skill Description Improvements
- Made descriptions more concrete and actionable
- Each skill now focuses on ONE specific block or concept
- Added clear examples of what students will create
- Improved skill titles to be more specific (e.g., using exact block names)

### 5. Preserved Cross-Topic Dependencies
All dependencies to other topics (T##.G#.##) were preserved exactly as they were. Examples:
- T06.G3.01 → T01.G2.02 (preserved)
- T06.G4.07 → T13.G3.01 (preserved)
- T06.G6.07 → T16.G3.02 (preserved)
- T06.G8.07 → T18.G6.02 (preserved)

## Skills by Grade Distribution

| Grade | Skill Count | Description |
|-------|-------------|-------------|
| GK | 3 | Picture-based sequencing |
| G1 | 3 | Trigger-action matching |
| G2 | 3 | Cause-effect chains, game rules |
| G3 | 12 | Basic event blocks (green flag, key, click, backdrop, clone) |
| G4 | 14 | Multiple handlers, broadcasts, collisions |
| G5 | 12 | Event patterns, parameters, condition events |
| G6 | 19 | Widget events, drag events, targeted messaging |
| G7 | 10 | State machines, advanced mouse events, variable change events |
| G8 | 11 | Multiplayer, 3D events, debugging |

## Notable Improvements

### Grade 3 (Gateway Year)
- Split the original T06.G3.01 into multiple focused skills
- Added "prepare for green flag click" as essential initialization pattern
- Added "when backdrop switches" for multi-scene projects
- Added "when I start as clone" for clone behavior

### Grade 4 (Building Complexity)
- Better scaffolding for broadcast concepts
- Clear progression: recognize need → build pair → add wait → match → fix errors
- Added collision events (sprite, edge, color) as separate skills

### Grade 5 (Intermediate Patterns)
- Added parameter-passing broadcasts as separate skills
- Added 2D physics collision events
- Better coverage of reactive programming with condition events

### Grade 6 (Advanced UI and Messaging)
- Widget events now properly broken down (click, change, hover, tab, video)
- Drag events broken down into start/during/stop
- Targeted messaging (send to sprite) as separate skills

### Grade 7 (State Management)
- State machines with proper progression
- All advanced mouse events covered
- Variable change events for reactive updates

### Grade 8 (Professional Patterns)
- Multiplayer events properly covered
- 3D events fully represented
- Event documentation and review skills

## CreatiCode Block Coverage

The following CreatiCode event blocks are now fully covered in T06:

### Standard Events (22 blocks)
- [x] when green flag clicked
- [x] prepare for green flag click
- [x] when key pressed / released
- [x] when key [variable] pressed / released
- [x] when this sprite clicked
- [x] when backdrop switches to
- [x] when I start as clone
- [x] when <condition>
- [x] when variable changed

### Broadcast Events
- [x] broadcast / broadcast and wait
- [x] broadcast with parameter / and wait
- [x] when I receive / with parameter
- [x] send to sprite / with parameter / and wait

### Collision Events
- [x] when touching sprite / edge / color
- [x] 2D physics collision events
- [x] 3D collision events

### Mouse/Drag Events
- [x] when dragging starts / being dragged / stops
- [x] when mouse button pressed/released at x,y
- [x] when mouse dragged to x,y
- [x] when mouse wheel scroll

### Widget Events
- [x] when widget clicked
- [x] when widget changes
- [x] when pointer enters/leaves widget
- [x] when tab selected
- [x] when any button named clicked
- [x] when video events

### 3D Events
- [x] when 3D scene initialized
- [x] when colliding with (3D)
- [x] when object picked
- [x] when object dragged (start/during/stop)
- [x] broadcast when distance <= / overlap

### Multiplayer Events
- [x] when added to game
- [x] broadcast to all players

## Quality Metrics

| Metric | Status |
|--------|--------|
| K-2 skills are picture-based | ✅ |
| G3+ skills involve coding | ✅ |
| Each skill = one concept | ✅ |
| Dependencies follow X-2 rule | ✅ |
| Cross-topic dependencies preserved | ✅ |
| All CreatiCode event blocks covered | ✅ |
| Logical grade progression | ✅ |
