# T15 (Stories & Animation) Optimization Summary

**Date:** November 25, 2025
**Phase:** Phase 1 - Topic-Focused Optimization

## Overview

Topic T15 (Stories & Animation) has been optimized to improve skill clarity, eliminate redundancy, add missing foundational skills, and fix dependency issues. The topic covers storytelling through animation from Kindergarten through Grade 8.

## Summary Statistics

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Total Skills | 83 | 87 | +4 |
| Skills Deleted | - | 1 | -1 |
| Skills Added | - | 6 | +6 |
| Skills Modified | - | 6 | - |
| Dependencies Fixed | - | 3 | - |

## Changes Made

### HIGH PRIORITY FIXES

#### 1. Fixed T15.G3.01 - Separated Instant vs Animated Movement
**Problem:** Skill combined two distinct blocks (`go to x: y:` and `glide`) in one skill.
**Solution:** T15.G3.01 now focuses ONLY on instant positioning with `go to x: y:`. Glide is properly taught in T15.G3.01.01.

**Old Description:** "Use `go to x: () y: ()` and `glide (1) secs to x: () y: ()` to move sprites..."
**New Description:** "Use `go to x: () y: ()` to instantly move sprites to specific positions on the stage. The sprite teleports immediately without any animation..."

#### 2. Deleted T15.G7.02 - Removed Duplicate Skill
**Problem:** T15.G7.02 "AI text-to-speech narration" duplicated T15.G5.12 "Basic text-to-speech with AI voices".
**Solution:** Deleted T15.G7.02 entirely. Updated T15.G8.04's dependency to reference T15.G5.12 instead.

#### 3. Fixed Dependency Text Errors
- **T15.G3.06:** Changed dependency from "T15.G3.04: Say something" → "T15.G3.04: Display speech with say blocks"
- **T15.G3.07:** Changed dependency from "T15.G3.04: Say something" → "T15.G3.04: Display speech with say blocks"

#### 4. Fixed Circular Dependency in T15.G4.02.01
**Problem:** T15.G4.02.01 depended on T15.G4.03, which created a circular dependency chain.
**Solution:** Removed T15.G4.03 from T15.G4.02.01's dependencies.

### NEW SKILLS ADDED

#### T15.G3.02.01: Animate with costume switching
**Grade:** 3
**Description:** Use `switch costume to [costume2 v]` to change a sprite's appearance to a specific costume, or `next costume` to cycle through costumes in order. Combine with `repeat` and `wait` blocks to create frame-by-frame animations: walking cycles, talking mouths, blinking eyes, or any multi-frame animation.
**Rationale:** Costume switching is fundamental to character animation but was missing from the curriculum.

#### T15.G3.10: Play sounds for story atmosphere
**Grade:** 3
**Description:** Use `start sound [sound v]` to play sound effects without waiting (script continues immediately). Use `play sound [sound v] until done` when you need to wait for the sound to finish before the next action.
**Rationale:** Audio is essential for storytelling but was not covered in the topic.

#### T15.G4.02.02: Change stage backdrop for scenes
**Grade:** 4
**Description:** Use `switch backdrop to [backdrop2 v]` to change the stage background image to a specific backdrop, or `next backdrop` to cycle through backdrops.
**Rationale:** Backdrop changing is core to scene transitions but was never explicitly taught.

#### T15.G4.04.01: Show and hide widgets dynamically
**Grade:** 4
**Description:** Use `show widget`, `hide widget`, and `remove widget` blocks to control widget visibility during your story.
**Rationale:** Widget visibility management is essential for story UI but was missing.

#### T15.G4.09: Apply graphics effects for atmosphere
**Grade:** 4
**Description:** Use graphics effects (ghost, brightness, color) to create visual atmosphere for moods, transitions, and special effects.
**Rationale:** Graphics effects are powerful for storytelling mood but were not covered.

#### T15.G5.04.01: Change sprite layer position
**Grade:** 5
**Description:** Use `go to [front v] layer`, `go to [back v] layer`, and layer adjustment blocks to control sprite depth.
**Rationale:** T15.G5.04 was broken down - conceptual understanding separated from practical block usage.

### SKILLS MODIFIED

#### T15.G5.01: Coordinate scene changes with broadcasts
**Change:** Clarified description to distinguish from T15.G4.02.
**New Focus:** Emphasizes multi-sprite synchronization challenges, creating scene checklists, and testing transitions.

#### T15.G5.04: Layering sprites and text
**Change:** Now focuses ONLY on conceptual understanding of layer order.
**New Focus:** Understanding the layer hierarchy (backdrop → printed text → sprites → widgets) without teaching specific blocks. Block usage moved to T15.G5.04.01.

## Dependency Updates

| Skill | Old Dependency | New Dependency | Reason |
|-------|----------------|----------------|--------|
| T15.G3.06 | T15.G3.04: Say something | T15.G3.04: Display speech with say blocks | Title correction |
| T15.G3.07 | T15.G3.04: Say something | T15.G3.04: Display speech with say blocks | Title correction |
| T15.G4.02.01 | T15.G4.03 (removed) | - | Circular dependency fix |
| T15.G8.04 | T15.G7.02: AI text-to-speech narration | T15.G5.12: Basic text-to-speech with AI voices | Dependency on deleted skill |

## Skills by Grade After Optimization

| Grade | Skills |
|-------|--------|
| K | 3 |
| 1 | 3 |
| 2 | 3 |
| 3 | 22 (+2) |
| 4 | 11 (+3) |
| 5 | 26 (+1) |
| 6 | 8 |
| 7 | 3 (-1) |
| 8 | 9 |
| **Total** | **88** |

## Remaining Considerations (Lower Priority)

The following items were identified but not addressed in this optimization:

1. **T15.G5.02 vs T15.G5.01 overlap:** Both teach broadcasts for coordination. Consider further differentiation or merging in future optimization.

2. **T15.G6.07 "Rich text story displays":** Could benefit from clearer description of what specific rich text features are taught.

3. **T15.G8.02 "Accessibility in Media":** Consider clarifying what specific accessibility blocks/features are taught.

4. **Missing Pen/Drawing skills:** Topic doesn't cover pen blocks for creating trails/drawings on stage (if applicable to CreatiCode).

## Verification Checklist

- [x] All new skills have proper ID format
- [x] All new skills have correct topic reference
- [x] All new skills have dependencies to earlier skills
- [x] No circular dependencies within T15
- [x] Deleted skill (T15.G7.02) has no remaining references
- [x] Cross-topic dependencies preserved (not modified)
- [x] X-2 rule maintained (dependencies within 2 grades)

## Files Modified

- `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`

## Related Documentation

- Analysis conducted using `/media/binyu/USB2/ScratchCopilot/blockdes8.txt` for block verification
- CreatiCode blocks reference created at `/media/binyu/USB2/dev/CreatiCodeSkillMap/CREATICODE_BLOCKS_REFERENCE.md`
