# T30 Quick Fix Reference

## Critical Fixes Required

### 1. Remove Phantom Dependency - "Peripheral Ports"
**Skills affected**: T30.G3.03, T30.G4.03

**Current (WRONG)**:
```
T30.G3.03 depends on:
* T30.G3.02: Describe peripheral ports and accessories ❌
```

**Fixed**:
```
T30.G3.03 depends on:
* T30.G2.01: Explain core internal components ✓
```

**Current (WRONG)**:
```
T30.G4.03 depends on:
* T30.G3.02: Describe peripheral ports and accessories ❌
* T30.G2.03: Compare wired vs wireless connections
```

**Fixed**:
```
T30.G4.03 depends on:
* T30.G2.03: Compare wired vs wireless connections ✓
```

---

### 2. Fix Missing Skill T30.G4.06
**Skills affected**: T30.G5.06, T30.G7.07

**OPTION A - Remove dependency** (Recommended):
```
T30.G5.06 depends on:
* T30.G3.05: Access device camera in CreatiCode projects
* T30.G4.01: Trace data flow in CreatiCode AI projects ✓

T30.G7.07 depends on:
* T30.G7.03: Plan graceful degradation strategies ✓
```

**OPTION B - Create the skill**:
```
ID: T30.G4.06
Skill: Plan for device capability variations in CreatiCode projects
Description: Students identify which device capabilities their CreatiCode projects require (camera, microphone, keyboard, mouse) and plan how to communicate requirements to users and handle missing capabilities gracefully.
Dependencies:
* T30.G3.01: Connect project ideas to required sensors/actuators
```

---

### 3. Fix "Free Camera" Reference
**Skill**: T30.G5.05

**Current (WRONG)**:
```
Description: Students add and configure orbit, follow, and free cameras in 3D CreatiCode projects, controlling camera distance, angles, target position, and input methods (keyboard, mouse, or joystick).
```

**Fixed**:
```
Description: Students add and configure orbit and follow cameras in 3D CreatiCode projects, controlling camera distance, angles, target position, and input methods (keyboard and mouse controls).
```

---

## Medium Priority Fixes

### 4. Add Bridging Skill at G3
**New skill needed**:
```
ID: T30.G3.04
Skill: Use keyboard and mouse inputs in CreatiCode projects
Description: Students create simple CreatiCode projects that respond to keyboard keys and mouse clicks, connecting the conceptual understanding of input devices from Grade 2 to hands-on programming practice.
Dependencies:
* T30.G2.05: Identify common device sensors and their inputs
* T30.G3.02: Identify device input types for CreatiCode projects
```

Then update:
```
T30.G4.05 depends on:
* T30.G3.04: Use keyboard and mouse inputs in CreatiCode projects ✓
* T08.G3.01: Use a simple if in a script
```

---

### 5. Fix T30.G6.05.01 Dependencies
**Skill**: T30.G6.05.01 (Use webcam as 3D scene background for AR effects)

**Current (WRONG)**:
```
Dependencies:
* T30.G3.05: Access device camera in CreatiCode projects (4 grades back!)
* T30.G5.05: Configure 3D cameras for CreatiCode game scenes
* T30.G6.05: Use speech recognition in voice-controlled CreatiCode projects ❌ NOT RELEVANT
```

**Fixed**:
```
Dependencies:
* T30.G5.05: Configure 3D cameras for CreatiCode game scenes
* T30.G6.04: Plan device capability checklists for CreatiCode AI projects
```

---

### 6. Renumber T30.G6.06.02
**Current**: T30.G6.06.02 (under body tracking)
**New**: T30.G5.05.02 (under mouse interactions)

**Skill**: Implement 3D object dragging with mouse

**New dependencies**:
```
Dependencies:
* T30.G5.05.01: Enable mouse picking and hovering for 3D objects
* T30.G4.05: Respond to keyboard and mouse events in CreatiCode
```

---

### 7. Reframe T30.G4.03 to CreatiCode Context

**Current (WRONG)**:
```
Skill: Differentiate latency vs bandwidth
Description: Students describe latency and bandwidth using everyday metaphors and relate them to online games or video calls.
```

**Fixed**:
```
Skill: Understand network performance in CreatiCode cloud projects
Description: Students observe how internet connection speed affects CreatiCode projects that use cloud APIs (T21 image generation, T22 ChatGPT, T23 speech recognition), noting the delay (latency) between sending requests and receiving responses, and understanding why larger data transfers take longer than text.
Dependencies:
* T30.G3.01: Connect project ideas to required sensors/actuators
* T30.G2.03: Compare wired vs wireless connections
```

---

### 8. Add Skill to Distinguish 2D Widgets from 3D Elements

**New skill needed**:
```
ID: T30.G4.07
Skill: Distinguish 2D widgets from 3D scene elements
Description: Students identify the difference between 2D widgets (camera preview windows, textboxes, buttons) that appear as overlays on the CreatiCode stage and 3D objects/cameras that exist within the 3D scene coordinate system, understanding when to use each for different project needs.
Dependencies:
* T30.G4.05.01: Add camera preview widgets to CreatiCode projects
* T30.G3.01: Connect project ideas to required sensors/actuators
```

Then update:
```
T30.G5.05 depends on:
* T30.G4.07: Distinguish 2D widgets from 3D scene elements ✓
* T30.G4.05: Respond to keyboard and mouse events in CreatiCode
* T30.G3.01: Connect project ideas to required sensors/actuators
```

---

## Skill Renumbering Impact

After adding new skills and renumbering:

### New Skills to Add:
- T30.G3.04: Use keyboard and mouse inputs in CreatiCode projects
- T30.G4.06: Plan for device capability variations (OPTIONAL - see fix #2)
- T30.G4.07: Distinguish 2D widgets from 3D scene elements

### Skills to Renumber:
- T30.G6.06.02 → T30.G5.05.02

### This will shift some existing skill IDs:
- Current T30.G3.05 → becomes T30.G3.06 (if we add T30.G3.04)
- Current T30.G3.06 → becomes T30.G3.07
- All G4, G5, G6, G7, G8 skills after the insertions will shift

**IMPORTANT**: Because renumbering creates cascading changes and breaks many dependencies, consider these alternatives:
1. Use decimal notation (T30.G3.04, T30.G4.07) without renumbering existing skills
2. OR: Do a comprehensive renumbering in a separate phase with dependency update tool

---

## Dependency Fixes Summary

| Skill | Current Dependency (WRONG) | Fixed Dependency |
|-------|---------------------------|------------------|
| T30.G3.03 | T30.G3.02 (phantom) | T30.G2.01 |
| T30.G4.03 | T30.G3.02 (phantom) | Remove (keep only T30.G2.03) |
| T30.G5.06 | T30.G4.06 (missing) | T30.G4.01 |
| T30.G6.05.01 | T30.G6.05 (irrelevant) | Remove (use T30.G6.04 instead) |
| T30.G6.06.02 | T30.G6.06 (illogical) | T30.G5.05.01, T30.G4.05 |
| T30.G7.07 | T30.G4.06 (missing) | T30.G7.03 |

---

## CreatiCode Blocks Reference

### Camera Capabilities (CONFIRMED):
- ✓ Camera widgets (2D)
- ✓ Webcam as 3D background
- ✓ Front/back camera selection
- ✓ Flip modes

### 3D Camera Types (CONFIRMED):
- ✓ Orbit camera
- ✓ Follow camera
- ❌ Free camera (DOES NOT EXIST)

### Input Methods (CONFIRMED):
- ✓ Keyboard events
- ✓ Mouse events (click, drag, wheel)
- ✓ Sprite drag events
- ✓ 3D object picking
- ✓ 3D object hovering
- ✓ 3D object dragging
- ❌ Joystick (NOT FOUND)

### AI Perception (CONFIRMED):
- ✓ Face detection
- ✓ 2D body part recognition
- ✓ 3D pose detection
- ✓ Hand detection

### Speech (CONFIRMED):
- ✓ Speech recognition (Azure)
- ✓ Speech recognition (OpenAI Whisper)
- ✓ Continuous speech recognition
- ✓ Text-to-speech

### NOT FOUND:
- ❌ Device capability detection API
- ❌ Accelerometer/motion sensors
- ❌ Touch events (separate from mouse)
- ❌ Joystick input

---

**Quick Reference Version**: 1.0
**Date**: 2025-11-23
