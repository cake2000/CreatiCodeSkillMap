# T30 Phase 1 Optimization Summary
## Topic: Devices & Hardware Systems

**Date:** November 25, 2025
**Status:** Complete

---

## Overview

This document summarizes the Phase 1 optimization changes made to Topic T30 (Devices & Hardware Systems) in the CreatiCode Skill Map.

### Skill Count Change
- **Before:** 45 skills
- **After:** 51 skills (+6 new sub-skills)

---

## Key Changes Made

### 1. Title Updates

| Skill ID | Old Title | New Title | Reason |
|----------|-----------|-----------|--------|
| T30.G3.01 | Connect project ideas to required sensors/actuators | Connect project ideas to required sensors | Removed "actuators" since CreatiCode doesn't have hardware outputs |

### 2. Skill Breakdowns (Major Changes)

#### T30.G4.05 - Input Events Breakdown
**Original:** One broad skill covering keyboard + mouse + sprite drag events

**Split into 4 focused skills:**
| New Skill ID | Title | Description |
|--------------|-------|-------------|
| T30.G4.05 | Respond to keyboard key press and release events in CreatiCode | Covers: when key pressed, when key released, key is pressed reporter, when key variable pressed/released |
| T30.G4.05.02 | Respond to mouse button events in CreatiCode | Covers: when left/right mouse button pressed/released, mouse x/y position variables |
| T30.G4.05.03 | Respond to mouse drag and wheel events in CreatiCode | Covers: when mouse pointer dragged, when mouse wheel scroll |
| T30.G4.05.04 | Use sprite drag events in CreatiCode | Covers: when dragging starts, when being dragged, when dragging stops |

#### T30.G5.05 - 3D Camera Breakdown
**Original:** One skill covering all 3D camera types and settings

**Split into 3 focused skills:**
| New Skill ID | Title | Description |
|--------------|-------|-------------|
| T30.G5.05 | Add orbit cameras for 3D CreatiCode scenes | Basic orbit camera with distance, angle, target, keyboard/mouse inputs |
| T30.G5.05.02 | Add follow cameras for 3D CreatiCode scenes | Follow camera with direction locks, see-through percentage |
| T30.G5.05.03 | Configure advanced 3D camera settings in CreatiCode | Camera limits (radius, visible range, v-angle), speed ratios, viewport |

#### T30.G6.05 - Speech Recognition Breakdown
**Original:** One skill covering all speech features (recognition + synthesis)

**Split into 3 focused skills:**
| New Skill ID | Title | Description |
|--------------|-------|-------------|
| T30.G6.05 | Use one-shot speech recognition in CreatiCode projects | start/end recognition, text from speech, Azure & OpenAI Whisper |
| T30.G6.05.02 | Use continuous speech recognition in CreatiCode projects | Continuous streaming recognition into list |
| T30.G6.05.03 | Use text-to-speech in CreatiCode projects | say in language, voice types, speed/pitch/volume control |

#### T30.G6.06 - Gesture Detection Breakdown
**Original:** One skill combining hand detection AND 2D body tracking

**Split into:**
| New Skill ID | Title | Description |
|--------------|-------|-------------|
| T30.G6.06 | Use hand detection in CreatiCode gesture games | Hand/finger tracking with curl/dir values for gesture recognition |
| T30.G6.06.03 | Use 2D body part recognition in CreatiCode projects | Full body 2D tracking, single/multiple person modes |

*Note: T30.G6.06.01 (3D pose detection) was already appropriately scoped and kept as-is.*

### 3. Dependency Fixes

| Skill ID | Fix Applied | Reason |
|----------|-------------|--------|
| T30.G4.03.01 | Removed dependency on T30.G4.03 (latency/bandwidth) | Camera widget comparison doesn't require networking concepts |
| T30.G4.05.01 | Removed dependency on T30.G4.05 | Camera widgets don't require keyboard/mouse skills |
| T30.G7.06 | Changed T30.G5.01 to T30.G4.05 | Fixed wrong reference - mobile optimization needs input skills, not AI device requirements |

### 4. All T30 Dependencies Updated
- All intra-topic dependencies referencing the old T30.G3.01 title now use "Connect project ideas to required sensors" (without "actuators")
- All dependencies referencing T30.G4.05 now reference "Respond to keyboard key press and release events in CreatiCode"
- All dependencies referencing T30.G5.05 now reference "Add orbit cameras for 3D CreatiCode scenes"

---

## Skills by Grade Level (After Optimization)

| Grade | Skill Count | Skill IDs |
|-------|-------------|-----------|
| K | 3 | T30.GK.01, T30.GK.02, T30.GK.03 |
| 1 | 3 | T30.G1.01, T30.G1.02, T30.G1.03 |
| 2 | 5 | T30.G2.01 - T30.G2.05 |
| 3 | 6 | T30.G3.01 - T30.G3.06 |
| 4 | 9 | T30.G4.01 - T30.G4.05.04 |
| 5 | 10 | T30.G5.01 - T30.G5.06.01, T30.G5.05.02, T30.G5.05.03 |
| 6 | 11 | T30.G6.01 - T30.G6.06.03 |
| 7 | 7 | T30.G7.01 - T30.G7.07 |
| 8 | 4 | T30.G8.01 - T30.G8.04 |

**Total: 51 skills**

---

## New Skills Added

1. **T30.G4.05.02** - Respond to mouse button events in CreatiCode
2. **T30.G4.05.03** - Respond to mouse drag and wheel events in CreatiCode
3. **T30.G4.05.04** - Use sprite drag events in CreatiCode
4. **T30.G5.05.02** - Add follow cameras for 3D CreatiCode scenes
5. **T30.G5.05.03** - Configure advanced 3D camera settings in CreatiCode
6. **T30.G6.05.02** - Use continuous speech recognition in CreatiCode projects
7. **T30.G6.05.03** - Use text-to-speech in CreatiCode projects
8. **T30.G6.06.03** - Use 2D body part recognition in CreatiCode projects

---

## CreatiCode Block Coverage Verification

The optimized skills now properly cover these CreatiCode block categories:

### Input Events (Grade 4)
- Keyboard: `when key pressed`, `when key released`, `key is pressed`, `when key variable pressed/released`
- Mouse buttons: `when left/right mouse button pressed/released`, `mouse x`, `mouse y`
- Mouse drag/wheel: `when mouse pointer dragged`, `when mouse wheel scroll`
- Sprite drag: `when dragging starts`, `when being dragged`, `when dragging stops`

### Camera Widgets (Grade 4)
- `show camera in x y width height as`
- `save picture from camera as costume`

### 3D Cameras (Grade 5)
- `add orbit camera distance v-angle h-angle panning speed inputs key pointer active as`
- `add follow camera distance z offset v-angle h-angle direction lock see-through active as`
- `configure camera radius min max visible range min max v-angle min max speed ratio panning angular`
- `set camera target xyz`
- `set camera viewport`

### Speech Recognition (Grade 6)
- `start recognizing speech in language record as`
- `end speech recognition`
- `text from speech`
- `clear speech text`
- `OpenAI: start recognizing speech in language`
- `start continuous speech recognition in language into list`
- `stop continuous speech recognition`

### Text-to-Speech (Grade 6)
- `say text in language as voice speed pitch volume store sound as`
- `stop speaking`

### Computer Vision (Grades 5-6)
- Face detection: `run face detection debug and write into table`
- Hand detection: `run hand detection table debug show video`
- 2D body: `run 2D body part recognition single person table debug`
- 3D pose: `run 3D pose detection debug table`

---

## Cross-Topic Dependencies Preserved

All dependencies to other topics were preserved:
- T01, T03, T04, T05, T06, T07, T08, T09, T10, T12, T22, T26, T32, T34

---

## Verification Checklist

- [x] No skills deleted (only improved/clarified)
- [x] All cross-topic dependencies preserved
- [x] X-2 rule applied (dependencies max 2 grades lower)
- [x] Each new skill focuses on ONE block/feature category
- [x] Skills are grade-appropriate
- [x] Descriptions are actionable and specific
- [x] All CreatiCode block categories properly covered
