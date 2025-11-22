# T30 (Devices & Hardware Systems) - Phase 1 Optimization Summary

**Date**: 2025-11-22
**Topic**: T30 – Devices & Hardware Systems
**Optimization Phase**: Phase 1 (Intra-Topic Focus)

---

## Overview

Topic T30 has been comprehensively optimized to accurately reflect CreatiCode's actual hardware and sensor capabilities. The optimization involved removing inaccurate content, adding missing features, and ensuring all skill descriptions match the platform's real blocks and functionality.

### Key Statistics

**Before Optimization:**
- Total Skills: 46
- Issues Found: 19 (7 HIGH, 9 MEDIUM, 3 LOW priority)

**After Optimization:**
- Total Skills: 49 (+3 net change)
- Skills Removed: 2
- Skills Added: 5
- Skills Edited: 8
- Dependencies Fixed: 2 (within T30)

---

## Major Changes Summary

### A. Skills Removed (2)

#### 1. **T30.G3.04** - Identify power sources for portable devices
**Reason**: CreatiCode is browser-based with no battery/power monitoring blocks. This content was off-topic for CreatiCode programming skills.

#### 2. **T30.G4.06** - Detect device capabilities in CreatiCode projects
**Reason**: CreatiCode has NO blocks for checking if a device has camera or microphone capabilities. Students cannot complete this skill as described. Permission error handling is covered more thoroughly in T30.G7.07.

---

### B. Skills Edited (8)

#### 1. **T30.G3.01** - Connect project ideas to required sensors/actuators
**What Changed**: Removed inaccurate hardware examples (accelerometers, LEDs, haptic feedback - none available in CreatiCode)
**New Focus**: Accurate hardware inputs (microphone, camera, keyboard, mouse)

**Before**:
> "Students map CreatiCode ideas (voice assistant, motion game, haptic feedback) to microphones, cameras, accelerometers, LEDs, etc."

**After**:
> "Students map CreatiCode project ideas (voice assistant, gesture game, face tracking app) to required hardware inputs (microphone, camera, keyboard, mouse) and explain how each sensor enables the project."

---

#### 2. **T30.G3.02** - Identify device input types for CreatiCode projects
**What Changed**: Shifted from physical peripheral ports/cables to logical input types
**New Focus**: Browser-based input methods relevant to CreatiCode

**Before** (Skill: "Describe peripheral ports and accessories"):
> "Learners match connector types to their uses and name one accessory for each."

**After** (Skill: "Identify device input types for CreatiCode projects"):
> "Students identify device input types used in CreatiCode projects (keyboard keys, mouse buttons, camera feed, microphone audio) and explain when to use each input method in games and interactive apps."

**Dependency Changed**: From T30.G3.01 → T30.G1.01 (more appropriate prerequisite)

---

#### 3. **T30.G4.05** - Respond to keyboard and mouse events in CreatiCode
**What Changed**: Added missing mouse wheel scrolling and sprite drag events
**New Coverage**: Comprehensive mouse/keyboard event blocks

**Before**:
> "...mouse clicks, drag events, and pointer movements..."

**After**:
> "...keyboard events (key press/release), mouse events (button click, drag, pointer movement, wheel scrolling), and sprite drag events (when sprite dragged/being dragged/stopped dragging)..."

---

#### 4. **T30.G6.03** - Explain camera and microphone privacy permissions
**What Changed**: Replaced abstract hardware security (TPM, secure enclave) with practical privacy concepts
**New Focus**: Camera/microphone permissions students actually encounter in CreatiCode

**Before** (Skill: "Summarize hardware security basics"):
> "Students explain secure elements (TPM, secure enclave) and why they protect passwords or encryption keys."

**After** (Skill: "Explain camera and microphone privacy permissions"):
> "Students explain why browsers require camera and microphone permissions, how CreatiCode projects request device access, and why these permissions protect user privacy from malicious apps."

**Dependencies Added**: T30.G3.05, T30.G3.06 (camera and microphone access skills)

---

#### 5. **T30.G6.05** - Use speech recognition in voice-controlled CreatiCode projects
**What Changed**: Added continuous streaming recognition mode
**New Coverage**: Both one-shot and continuous speech recognition

**Before**:
> "...speech-to-text and text-to-speech blocks..."

**After**:
> "...speech-to-text using both one-shot recognition (start/end speech recognition) and continuous streaming recognition (start continuous speech recognition) with Azure and OpenAI Whisper APIs, plus text-to-speech blocks..."

---

#### 6. **T30.G6.06** - Implement hand and 2D body tracking in CreatiCode projects
**What Changed**: Explicitly added 2D body part recognition (was completely omitted before)
**New Coverage**: Hand detection AND 2D body parts (single/multiple person modes)

**Before** (Skill: "Implement hand and body tracking"):
> "Learners use hand and body pose detection to create gesture-controlled games..."

**After** (Skill: "Implement hand and 2D body tracking"):
> "Students use hand detection (tracking finger curl angles) and 2D body part recognition (single or multiple person modes) to create gesture-controlled games..."

**Note**: 3D pose detection separated into new skill T30.G6.06.01

---

#### 7. **T30.G7.05** - Debate privacy implications of AI-powered sensors
**What Changed**: Made deliverable more specific and concrete
**New Focus**: Specific privacy guidelines, not just general debate

**Before**:
> "...and propose guidelines balancing AI utility and privacy per AI4K12..."

**After**:
> "...and propose specific guidelines balancing utility and privacy (when to ask permission, when to delete data, how to inform users)..."

**Dependency Updated**: T30.G6.03 now reflects the updated privacy permissions skill

---

#### 8. **T30.G5.02** - Plan safe device-handling procedures for group work
**What Changed**: Fixed dependency (removed unnecessary latency/bandwidth prerequisite)
**New Dependency**: T30.G2.04 (basic device care) instead of T30.G4.03 (latency/bandwidth)

---

### C. Skills Added (5)

#### 1. **T30.G4.05.01** - Add camera preview widgets to CreatiCode projects
**Grade**: 4
**Why Added**: CreatiCode has camera widget blocks (`add camera window`, `save picture from camera`) but no skill taught this feature

**Description**:
> "Students add camera widgets to display live camera feeds in CreatiCode projects using the 'add camera window' block, configure front/back camera selection and flip modes, and use 'save picture from camera' to capture photos, understanding when camera widgets enhance user experiences."

**Dependencies**:
- T30.G3.05: Access device camera in CreatiCode projects
- T30.G4.05: Respond to keyboard and mouse events in CreatiCode

**CreatiCode Blocks Covered**:
- `add camera window at x (X) y (Y) width (W) height (H) side [SIDE v] mode [MODE v] named [NAME]`
- `save picture from camera [NAME v] as [FILENAME]`

---

#### 2. **T30.G5.05.01** - Enable mouse picking and hovering for 3D objects
**Grade**: 5
**Why Added**: Critical 3D interaction feature (picking and hovering 3D objects with mouse) was not covered

**Description**:
> "Students enable mouse interactions for 3D objects using 'turn on picking' and 'turn on hovering' blocks, create 'when this 3D object is picked/hovered' event handlers, and use reporter blocks (picked point x/y/z, hovered 3D object name) to make interactive 3D scenes where objects respond to mouse clicks and hovers."

**Dependencies**:
- T30.G4.05: Respond to keyboard and mouse events in CreatiCode
- T30.G5.05: Configure 3D cameras for CreatiCode game scenes

**CreatiCode Blocks Covered**:
- `turn on picking with [BUTTON v] for objects created in sprites [SPRITELIST]`
- `turn on hovering for objects created in sprites [SPRITELIST]`
- `when this 3D object is picked` (hat block)
- `when this 3D object is hovered` (hat block)
- `picked point x/y/z` (reporter blocks)
- `hovered 3D object name` (reporter block)

---

#### 3. **T30.G6.05.01** - Use webcam as 3D scene background for AR effects
**Grade**: 6
**Why Added**: Cool AR feature (`turn on webcam background`) existed but wasn't taught

**Description**:
> "Students use the 'turn on webcam background' block to overlay 3D objects on live camera feeds, select front/back camera, configure flip modes (normal, left-right flipped, up-down flipped), and create augmented reality effects where 3D models appear in the real world."

**Dependencies**:
- T30.G3.05: Access device camera in CreatiCode projects
- T30.G5.05: Configure 3D cameras for CreatiCode game scenes
- T30.G6.05: Use speech recognition in voice-controlled CreatiCode projects

**CreatiCode Blocks Covered**:
- `turn [ONOFF v] webcam background [WHICHCAMERA v] in [FLIPMODE v] mode`
- Front/Back camera options
- Normal/Flipped modes

---

#### 4. **T30.G6.06.01** - Use 3D pose detection for depth-aware body tracking
**Grade**: 6
**Why Added**: Separated 3D pose (depth-aware) from 2D body parts and hand detection for clarity

**Description**:
> "Students implement 3D pose detection (detecting 3D positions of body parts like shoulders, wrists, knees) to create depth-aware gesture games where the camera tracks player movement in 3D space, comparing 2D body parts vs 3D pose detection and understanding when depth information improves interactions."

**Dependencies**:
- T30.G6.06: Implement hand and 2D body tracking in CreatiCode projects
- T30.G5.05: Configure 3D cameras for CreatiCode game scenes

**CreatiCode Blocks Covered**:
- `run 3D pose detection debug [DODEBUG v] table [TABLENAME v]`

---

#### 5. **T30.G6.06.02** - Implement 3D object dragging with mouse
**Grade**: 6
**Why Added**: 3D object dragging blocks existed but weren't covered

**Description**:
> "Students configure 3D objects to be draggable using 'set dragging mode' (specifying drag direction constraints), create event handlers for 'when this 3D object starts dragging' and 'when this 3D object is dragged', and use 'dragged 3D object name' reporter to build interactive 3D scenes where users can reposition objects by dragging."

**Dependencies**:
- T30.G5.05.01: Enable mouse picking and hovering for 3D objects
- T30.G6.06: Implement hand and 2D body tracking in CreatiCode projects

**CreatiCode Blocks Covered**:
- `set dragging mode [MODE] direction x (X) y (Y) z (Z)`
- `when this 3D object is dragged` (hat block)
- `when this 3D object starts dragging` (hat block)
- `dragged 3D object name` (reporter block)

---

## Skill Count by Grade

| Grade | Before | After | Change |
|-------|--------|-------|--------|
| K     | 3      | 3     | 0      |
| 1     | 3      | 3     | 0      |
| 2     | 5      | 5     | 0      |
| 3     | 6      | 5     | -1     |
| 4     | 6      | 6     | 0      |
| 5     | 6      | 7     | +1     |
| 6     | 6      | 9     | +3     |
| 7     | 7      | 7     | 0      |
| 8     | 4      | 4     | 0      |
| **Total** | **46** | **49** | **+3** |

---

## CreatiCode Features Now Properly Covered

### Hardware Input Blocks (Complete Coverage ✅)
- ✅ Keyboard events (key press/release)
- ✅ Mouse events (click, drag, pointer movement, **wheel scrolling**)
- ✅ **Sprite drag events** (when sprite dragged/being dragged/stopped dragging)
- ✅ Camera access and permissions
- ✅ Microphone access and permissions

### AI Perception Blocks (Complete Coverage ✅)
- ✅ Face detection (`run face detection`)
- ✅ **2D body part recognition** (single/multiple person - NEW)
- ✅ 3D pose detection (`run 3D pose detection`)
- ✅ Hand detection (finger curl angles)
- ✅ Speech recognition (one-shot AND **continuous streaming** - NEW)
- ✅ Text-to-speech

### 3D Interaction Blocks (Complete Coverage ✅)
- ✅ Orbit/follow/free cameras
- ✅ **3D object picking** (mouse clicks - NEW)
- ✅ **3D object hovering** (mouse hover - NEW)
- ✅ **3D object dragging** (mouse drag - NEW)
- ✅ **Webcam background for AR** (NEW)

### Widget Blocks (Complete Coverage ✅)
- ✅ **Camera widget** (add camera window, save picture - NEW)
- ✅ Button widgets with click events
- ✅ UI widgets (text input, sliders, etc.)

---

## Dependencies Fixed Within T30

### 1. T30.G3.02 Dependency Correction
**Changed**: T30.G3.01 → T30.G1.01
**Reason**: Peripheral ports/input types don't logically require sensor knowledge; basic computer parts is more appropriate.

### 2. T30.G5.02 Dependency Correction
**Removed**: T30.G4.03 (latency/bandwidth)
**Added**: T30.G2.04 (basic device care)
**Reason**: Device handling procedures don't require networking knowledge; basic care habits are more relevant.

### 3. T30.G6.03 Dependencies Added
**Added**: T30.G3.05, T30.G3.06
**Reason**: Privacy permissions skill now requires understanding of camera/microphone access.

---

## Issues for Phase 2 (Cross-Topic Dependencies)

The following skills reference other topics but currently lack formal dependencies. These should be addressed in Phase 2:

### T30.G7.04 - Cloud vs edge processing
**References**: T21 (image generation), T22 (ChatGPT), T23 (speech recognition)
**Suggested Phase 2 Dependencies**:
- T21.G6.01 or T21.G7.01 (AI media generation)
- T22.G6.01 or T22.G7.01 (ChatGPT usage)
- T23.G6.02 or T23.G7.01 (perception/speech)

### T30.G8.01 - Device-cloud architecture
**References**: Same as T30.G7.04
**Suggested Phase 2 Dependencies**: Same as above

---

## Quality Improvements

### Accuracy ✅
- ✅ Removed all references to non-existent hardware (accelerometers, LEDs, haptic, battery monitoring)
- ✅ All skill descriptions now match actual CreatiCode blocks
- ✅ No capability detection blocks mentioned (removed T30.G4.06)

### Completeness ✅
- ✅ 2D body part recognition now explicitly covered (was completely missing)
- ✅ Continuous speech recognition mode added
- ✅ Camera widgets covered
- ✅ 3D mouse interactions (picking, hovering, dragging) fully covered
- ✅ Webcam background AR effects covered
- ✅ Mouse wheel scrolling events covered
- ✅ Sprite drag events covered

### Clarity ✅
- ✅ Privacy permissions skill now practical and relevant
- ✅ Input types skill focused on logical inputs, not physical ports
- ✅ Privacy debate has specific deliverables
- ✅ 3D pose separated from 2D body parts for clear distinction

### Progression ✅
- ✅ K-2 skills remain picture-based (unchanged)
- ✅ Grade 3 introduces camera/microphone access appropriately
- ✅ Grade 4-5 builds practical input handling skills
- ✅ Grade 6 covers advanced computer vision
- ✅ Grade 7-8 addresses system architecture and privacy

---

## Remaining Considerations (Out of Scope for Phase 1)

### Storage Skills (T30.G3.03, T30.G6.02)
**Status**: Kept but flagged for review
**Concern**: Cloud vs local storage is more about software/platform than hardware
**Recommendation**: Consider moving to a different topic in future review OR reframe as "Device storage types" (SSD, HDD) to maintain hardware focus

### Accessibility Content
**Status**: Maintained (T30.G4.04, T30.G5.04)
**Quality**: Good connection between hardware and accessibility outcomes

### Privacy & Ethics
**Status**: Improved (T30.G6.03, T30.G7.05)
**Quality**: Now more practical and specific to CreatiCode

---

## Conclusion

Topic T30 has been successfully optimized with:

✅ **Accurate feature descriptions** matching CreatiCode's real capabilities
✅ **Complete coverage** of all hardware/sensor blocks
✅ **Clear skill progression** from K through Grade 8
✅ **Proper scaffolding** with new intermediate skills added
✅ **Fixed intra-topic dependencies**

**Next Steps (Phase 2)**:
- Add cross-topic dependencies to T30.G7.04 and T30.G8.01 (referencing T21, T22, T23)
- Review and potentially relocate storage skills (T30.G3.03, T30.G6.02)
- Ensure T23 (AI Perception) has complementary skills for features covered in T30

**Total Skills**: 49 (from 46)
**Quality Status**: Production-Ready ✅
