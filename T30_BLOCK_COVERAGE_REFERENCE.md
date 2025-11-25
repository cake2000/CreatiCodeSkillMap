# T30 Block Coverage Reference

This document maps each T30 skill to the specific CreatiCode blocks it teaches.

---

## Keyboard & Mouse Input (Grade 4)

### T30.G4.05: Respond to keyboard events
**Blocks Covered**:
- `when [KEY] key pressed` (hat block)
- `when any key pressed` (hat block)
- `key [KEY] pressed?` (boolean reporter)

### T30.G4.05.01: Respond to mouse button and wheel events
**Blocks Covered**:
- `when [left/right/middle] mouse button pressed` (hat block)
- `when [left/right/middle] mouse button released` (hat block)
- `[left/right/middle] mouse button pressed?` (boolean reporter)
- `when mouse wheel scrolled` (hat block)
- `mouse pointer x` (reporter)
- `mouse pointer y` (reporter)

### T30.G4.05.02: Respond to mouse drag events
**Blocks Covered**:
- `when mouse button [BUTTON] is pressed at x [var] y [var]` (hat block)
- `when mouse button [BUTTON] is dragged to x [var] y [var]` (hat block)

### T30.G4.05.03: Respond to sprite drag events
**Blocks Covered**:
- `when I start being dragged` (hat block)
- `when I am being dragged` (hat block)
- `when I stop being dragged` (hat block)
- `set draggable [TRUE/FALSE]` (command block)

### T30.G4.05.04: Add camera preview widgets
**Blocks Covered**:
- `add camera window at x (X) y (Y) width (W) height (H) side [FRONT/BACK] mode [NORMAL/FLIPPED] named [NAME]`
- `save picture from camera [NAME] as [FILENAME]`

---

## 3D Camera Systems (Grade 5)

### T30.G5.05: Add orbit and follow cameras
**Blocks Covered**:
- `add orbit camera name [NAME] distance (D) height (H) target x (X) y (Y) z (Z)`
- `add follow camera name [NAME] distance (D) height (H) follow object [OBJNAME]`

### T30.G5.05.01: Configure 3D camera limits and constraints
**Blocks Covered**:
- `configure orbit camera [NAME] min distance (MIN) max distance (MAX)`
- `configure orbit camera [NAME] alpha speed ratio (ALPHA) beta speed ratio (BETA)`
- `configure orbit camera [NAME] lower beta limit (LOWER) upper beta limit (UPPER)`

### T30.G5.05.02: Enable mouse picking and hovering for 3D objects
**Blocks Covered**:
- `turn on picking with [BUTTON] for objects created in sprites [LIST]`
- `turn on hovering for objects created in sprites [LIST]`
- `when this 3D object is picked` (hat block)
- `when this 3D object is hovered` (hat block)
- `picked point x` (reporter)
- `picked point y` (reporter)
- `picked point z` (reporter)
- `hovered 3D object name` (reporter)

---

## Speech & Voice (Grade 6)

### T30.G6.05: Use one-shot speech recognition
**Blocks Covered**:
- `start speech recognition using [Azure/Whisper] language [LANG]`
- `end speech recognition` (reporter - returns recognized text)

### T30.G6.05.01: Use continuous streaming speech recognition
**Blocks Covered**:
- `start continuous speech recognition using [Azure/Whisper] language [LANG]`
- `continuous transcription` (reporter)
- `stop continuous speech recognition`

### T30.G6.05.02: Use text-to-speech for voice output
**Blocks Covered**:
- `say [TEXT] in language [LANG] with voice [VOICE]`
- Language options (English, Spanish, Chinese, French, German, etc.)
- Voice options per language

### T30.G6.05.03: Use webcam as 3D scene background for AR
**Blocks Covered**:
- `turn [ON/OFF] webcam background [FRONT/BACK] in [NORMAL/FLIPPED/UP-DOWN-FLIPPED] mode`

---

## Computer Vision (Grade 6)

### T30.G6.06: Use hand detection for gesture recognition
**Blocks Covered**:
- `run hand detection debug [TRUE/FALSE] table [NAME]`
- `hand [LEFT/RIGHT] finger [THUMB/INDEX/MIDDLE/RING/PINKY] curl [NOCURL/HALFCURL/FULLCURL]?` (boolean)
- `hand [LEFT/RIGHT] finger [FINGER] direction [UP/DOWN/LEFT/RIGHT]?` (boolean)
- `hand [LEFT/RIGHT] keypoint [1-21] x` (reporter)
- `hand [LEFT/RIGHT] keypoint [1-21] y` (reporter)

### T30.G6.06.01: Use 2D body part recognition
**Blocks Covered**:
- `run 2D body parts recognition on [SINGLE/MULTIPLE] person debug [TRUE/FALSE] table [NAME]`
- `person [N] body part [NOSE/LEFT_EYE/RIGHT_EYE/LEFT_EAR/RIGHT_EAR/LEFT_SHOULDER/RIGHT_SHOULDER/LEFT_ELBOW/RIGHT_ELBOW/LEFT_WRIST/RIGHT_WRIST/LEFT_HIP/RIGHT_HIP/LEFT_KNEE/RIGHT_KNEE/LEFT_ANKLE/RIGHT_ANKLE] x` (reporter)
- `person [N] body part [PART] y` (reporter)

### T30.G6.06.02: Use 3D pose detection for depth-aware tracking
**Blocks Covered**:
- `run 3D pose detection debug [TRUE/FALSE] table [NAME]`
- `body part [0-32] x` (reporter)
- `body part [0-32] y` (reporter)
- `body part [0-32] z` (reporter)

### T30.G6.06.03: Implement 3D object dragging with mouse
**Blocks Covered**:
- `set dragging mode [NONE/DRAG/DRAG_ON_X/DRAG_ON_Y/DRAG_ON_Z/DRAG_ON_XY/DRAG_ON_XZ/DRAG_ON_YZ] direction x (X) y (Y) z (Z)`
- `when this 3D object starts dragging` (hat block)
- `when this 3D object is dragged` (hat block)
- `dragged 3D object name` (reporter)

---

## AR Features (Grade 7 - PROPOSED)

### T30.G7.07.01: Enable AR world camera (PROPOSED)
**Blocks Covered**:
- `switch to AR world camera scale (SCALE) emulation mode (MODE)`

### T30.G7.07.02: Enable AR face tracking (PROPOSED)
**Blocks Covered**:
- `switch to AR face camera show marker (SHOW) scale (SCALE) emulation mode (MODE)`

### T30.G7.07.03: Enable AR logo/image tracking (PROPOSED)
**Blocks Covered**:
- `switch to AR LOGO as [LOGO/IMAGE] camera`

---

## Location Sensing (Grade 7 - IF BLOCKS EXIST)

### T30.G7.08: Access device location (PROPOSED - VERIFY)
**Blocks Covered** (TO BE CONFIRMED):
- `latitude` (reporter) - ?
- `longitude` (reporter) - ?
- `geo info [FIELD]` (reporter) - ?

**Status**: Need to verify if these blocks exist in CreatiCode.

---

## Block Coverage Summary

### Camera Input
- ✅ Camera access permissions (T30.G3.05)
- ✅ Camera widgets (T30.G4.05.04)
- ✅ Webcam background for 3D (T30.G6.05.03)
- ⚠️ AR camera modes (T18.G8.04.01-03 or proposed T30.G7.07.01-03)

### Microphone Input
- ✅ Microphone access permissions (T30.G3.06)
- ✅ One-shot speech recognition (T30.G6.05)
- ✅ Continuous speech recognition (T30.G6.05.01)
- ✅ Text-to-speech (T30.G6.05.02)

### Keyboard Input
- ✅ Key press/release events (T30.G4.05)
- ✅ Key state checking (T30.G4.05)

### Mouse Input
- ✅ Button press/release events (T30.G4.05.01)
- ✅ Button state checking (T30.G4.05.01)
- ✅ Mouse wheel scrolling (T30.G4.05.01)
- ✅ Pointer position (T30.G4.05.01)
- ✅ Mouse drag coordinates (T30.G4.05.02)

### Sprite Interaction
- ✅ Sprite dragging events (T30.G4.05.03)
- ✅ Draggable on/off (T30.G4.05.03)

### 3D Mouse Interaction
- ✅ 3D object picking (T30.G5.05.02)
- ✅ 3D object hovering (T30.G5.05.02)
- ✅ 3D object dragging (T30.G6.06.03)
- ✅ Picked point coordinates (T30.G5.05.02)

### 3D Camera Control
- ✅ Orbit camera (T30.G5.05)
- ✅ Follow camera (T30.G5.05)
- ✅ Camera distance limits (T30.G5.05.01)
- ✅ Camera speed ratios (T30.G5.05.01)
- ✅ Camera angle limits (T30.G5.05.01)

### Computer Vision
- ✅ Face detection (T30.G5.06)
- ✅ Hand detection (T30.G6.06)
- ✅ 2D body part recognition (T30.G6.06.01)
- ✅ 3D pose detection (T30.G6.06.02)

### Location Sensing
- ❓ Latitude/longitude (T30.G7.08 - VERIFY IF BLOCKS EXIST)

### AR Features
- ⚠️ AR world camera (T18.G8.04.01 OR proposed T30.G7.07.01)
- ⚠️ AR face tracking (T18.G8.04.02 OR proposed T30.G7.07.02)
- ⚠️ AR logo tracking (T18.G8.04.03 OR proposed T30.G7.07.03)

---

## Coverage Status Legend
- ✅ Fully covered by current or proposed T30 skills
- ⚠️ Covered elsewhere (T18) or needs decision (duplicate vs reference)
- ❓ Unsure if blocks exist (needs verification)
- ❌ Not covered (blocks exist but no skill teaches them)

---

## Notes

1. **AR Features Decision Needed**: Currently in T18, but logically belong in T30 (hardware/camera topic). Options:
   - Keep in T18, add cross-references in T30
   - Duplicate skills in T30 (T30.G7.07.01-03)
   - Move from T18 to T30

2. **Location Sensing Verification Needed**: User mentioned "latitude, longitude, geo info" but no blocks found in current analysis. Need to verify if these blocks exist in CreatiCode.

3. **Block Names**: Some block names are approximations based on typical Scratch-like syntax. Verify exact block text and parameters in CreatiCode.

4. **Missing Features**: If any camera/sensor blocks are NOT listed here, they need skills added.
