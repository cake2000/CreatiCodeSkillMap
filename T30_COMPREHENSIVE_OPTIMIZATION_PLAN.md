# T30 (Devices & Hardware Systems) - Comprehensive Optimization Plan

**Date**: 2025-11-25
**Topic**: T30 – Devices & Hardware Systems
**Current Skills**: 52 total (K: 3, G1: 3, G2: 5, G3: 6, G4: 7, G5: 8, G6: 9, G7: 7, G8: 4)
**Optimization Phase**: Phase 1 Follow-up Analysis

---

## Executive Summary

This analysis identifies remaining optimization opportunities for Topic T30 after the initial Phase 1 optimization (which took skills from 46 → 49, then to current 52). While Phase 1 successfully added missing features and removed inaccurate content, several issues remain:

**Key Findings:**
- **6 skills need to be broken down** (covering too many features)
- **3 dependency errors** need fixing (wrong skill IDs referenced)
- **2 missing feature gaps** (AR features, location sensing)
- **5 skills need description clarifications**
- **1 skill placement issue** (camera widgets at wrong grade)

---

## Part 1: Skills to Break Down (6 skills → 14 sub-skills)

### Priority: HIGH

### 1.1 T30.G4.05 - "Respond to keyboard and mouse events"

**Current Issue**: Covers 3 distinct feature categories in one skill:
1. Keyboard events (key press/release, when key pressed)
2. Mouse events (click, button press, drag, wheel scroll, pointer position)
3. Sprite drag events (when dragging starts/being dragged/stops)

**Current Description**:
> "Students program sprites to respond to keyboard events (key press/release), mouse events (button click, drag, pointer movement, wheel scrolling), and sprite drag events (when sprite dragged/being dragged/stopped dragging)..."

**Problem**: Too broad for Grade 4. Students need to master each input type separately.

**Proposed Breakdown**:

#### T30.G4.05 (UPDATED)
- **Skill**: Respond to keyboard events in CreatiCode
- **Description**: Students program sprites to respond to keyboard events using "when [KEY] key pressed", "key [KEY] pressed?", and "when any key pressed" blocks to create keyboard-controlled games and animations.
- **CreatiCode Blocks**:
  - `when [KEY] key pressed` (hat block)
  - `when any key pressed` (hat block)
  - `key [KEY] pressed?` (boolean reporter)
- **Dependencies**: T06.G2.01, T06.G2.02, T06.G3.01, T07.G2.01, T08.G3.01, T30.G3.01

#### T30.G4.05.01 (RENAME from camera widgets → mouse events)
- **Skill**: Respond to mouse button and wheel events
- **Description**: Students program sprites to respond to mouse button clicks (left/right/middle button press/release), mouse wheel scrolling, and track pointer position to create mouse-controlled interactive projects.
- **CreatiCode Blocks**:
  - `when [left/right/middle] mouse button pressed/released`
  - `[left/right/middle] mouse button pressed?` (boolean reporter)
  - `when mouse wheel scrolled`
  - `mouse pointer x/y` (reporter blocks)
- **Dependencies**: T30.G4.05 (keyboard events), T06.G3.01

#### T30.G4.05.02 (NEW)
- **Skill**: Respond to mouse drag events
- **Description**: Students program sprites to respond to mouse drag events using "when mouse button [button] is pressed at x [var] y [var]" and "when mouse button [button] is dragged to x [var] y [var]" blocks to capture drag coordinates and create drawing or selection features.
- **CreatiCode Blocks**:
  - `when mouse button [BUTTON] is pressed at x [var] y [var]`
  - `when mouse button [BUTTON] is dragged to x [var] y [var]`
- **Dependencies**: T30.G4.05.01 (mouse button events), T09.G3.01.04 (variable monitors)

#### T30.G4.05.03 (NEW)
- **Skill**: Respond to sprite drag events
- **Description**: Students enable sprite dragging and program responses using "when I start being dragged", "when I am being dragged", and "when I stop being dragged" hat blocks to create draggable game objects and UI elements.
- **CreatiCode Blocks**:
  - `when I start being dragged` (hat block)
  - `when I am being dragged` (hat block)
  - `when I stop being dragged` (hat block)
  - `set draggable [TRUE/FALSE]` (enable/disable dragging)
- **Dependencies**: T30.G4.05.02 (mouse drag events), T06.G3.01

#### T30.G4.05.04 (RELOCATE - was T30.G4.05.01 camera widgets)
- **Skill**: Add camera preview widgets to CreatiCode projects
- **Description**: Students add camera widgets to display live camera feeds in CreatiCode projects using the "add camera window" block, configure front/back camera selection and flip modes, and use "save picture from camera" to capture photos.
- **CreatiCode Blocks**:
  - `add camera window at x (X) y (Y) width (W) height (H) side [FRONT/BACK] mode [NORMAL/FLIPPED] named [NAME]`
  - `save picture from camera [NAME] as [FILENAME]`
- **Dependencies**: T30.G3.05 (Access device camera), T06.G3.01, T07.G2.01
- **Note**: Remove incorrect dependency on keyboard/mouse events

---

### 1.2 T30.G5.05 - "Configure 3D cameras for CreatiCode game scenes"

**Current Issue**: Combines basic camera setup with advanced camera configuration parameters.

**Current Description**:
> "Students add and configure orbit and follow cameras in 3D CreatiCode projects, controlling camera distance, angles, target position, and input methods (keyboard and mouse controls)."

**Problem**: Missing coverage of camera limits/constraints (min/max distance, speed ratios, angle limits).

**Proposed Breakdown**:

#### T30.G5.05 (UPDATED)
- **Skill**: Add orbit and follow cameras in 3D scenes
- **Description**: Students add orbit cameras (camera rotates around a target) and follow cameras (camera follows an object) using "add orbit camera" and "add follow camera" blocks, setting initial distance, height, and target objects for basic 3D game perspectives.
- **CreatiCode Blocks**:
  - `add orbit camera name [NAME] distance (D) height (H) target x (X) y (Y) z (Z)`
  - `add follow camera name [NAME] distance (D) height (H) follow object [OBJNAME]`
- **Dependencies**: T30.G4.05 (keyboard events), T30.G3.01

#### T30.G5.05.01 (RENAME from mouse picking → camera configuration)
- **Skill**: Configure 3D camera limits and constraints
- **Description**: Students configure camera movement limits using "configure orbit camera" blocks to set minimum/maximum distance, rotation speed ratios, and angle constraints, creating controlled camera behaviors that prevent players from zooming too far or rotating to invalid angles.
- **CreatiCode Blocks**:
  - `configure orbit camera [NAME] min distance (MIN) max distance (MAX)`
  - `configure orbit camera [NAME] alpha speed ratio (ALPHA) beta speed ratio (BETA)`
  - `configure orbit camera [NAME] lower beta limit (LOWER) upper beta limit (UPPER)`
- **Dependencies**: T30.G5.05 (basic camera setup), T09.G4.01 (variable comparison)

#### T30.G5.05.02 (NEW - relocate from T30.G5.05.01)
- **Skill**: Enable mouse picking and hovering for 3D objects
- **Description**: Students enable mouse interactions for 3D objects using "turn on picking" and "turn on hovering" blocks, create "when this 3D object is picked/hovered" event handlers, and use reporter blocks to make interactive 3D scenes.
- **CreatiCode Blocks**:
  - `turn on picking with [BUTTON] for objects created in sprites [LIST]`
  - `turn on hovering for objects created in sprites [LIST]`
  - `when this 3D object is picked` (hat block)
  - `when this 3D object is hovered` (hat block)
  - `picked point x/y/z` (reporters)
  - `hovered 3D object name` (reporter)
- **Dependencies**: T30.G4.05.01 (mouse button events), T30.G5.05 (basic camera setup), T06.G3.01

---

### 1.3 T30.G6.05 - "Use speech recognition in voice-controlled CreatiCode projects"

**Current Issue**: Combines speech-to-text (one-shot AND continuous modes) with text-to-speech in one skill.

**Current Description**:
> "Students implement speech-to-text using both one-shot recognition (start/end speech recognition) and continuous streaming recognition (start continuous speech recognition) with Azure and OpenAI Whisper APIs, plus text-to-speech blocks..."

**Problem**: Two distinct features (speech recognition vs text-to-speech) with different complexity levels.

**Proposed Breakdown**:

#### T30.G6.05 (UPDATED)
- **Skill**: Use one-shot speech recognition in CreatiCode
- **Description**: Students implement one-shot speech-to-text using "start speech recognition" and "end speech recognition" blocks to capture spoken phrases in CreatiCode projects, understanding microphone requirements, language options, and when to use one-shot vs continuous modes.
- **CreatiCode Blocks**:
  - `start speech recognition using [Azure/Whisper] language [LANG]`
  - `end speech recognition` (reporter - returns recognized text)
- **Dependencies**: T30.G3.06 (microphone access), T30.G5.01, T05.G5.01

#### T30.G6.05.01 (RENAME from webcam AR → continuous speech)
- **Skill**: Use continuous streaming speech recognition
- **Description**: Students implement continuous speech recognition using "start continuous speech recognition" to transcribe ongoing speech in real-time, handling live transcription use cases like dictation, live captions, or voice command systems.
- **CreatiCode Blocks**:
  - `start continuous speech recognition using [Azure/Whisper] language [LANG]`
  - `continuous transcription` (reporter - returns current transcription)
  - `stop continuous speech recognition`
- **Dependencies**: T30.G6.05 (one-shot speech recognition), T09.G5.01 (variables)

#### T30.G6.05.02 (NEW)
- **Skill**: Use text-to-speech for voice output
- **Description**: Students use text-to-speech blocks to make CreatiCode projects speak using "say [TEXT] in language [LANG] with voice [VOICE]" blocks, selecting appropriate voices and languages for different project contexts like voice assistants, narration, or accessibility features.
- **CreatiCode Blocks**:
  - `say [TEXT] in language [LANG] with voice [VOICE]`
  - Language options (English, Spanish, Chinese, etc.)
  - Voice options per language
- **Dependencies**: T30.G3.06 (microphone - for voice I/O conceptual understanding), T05.G5.01

#### T30.G6.05.03 (NEW - relocate from T30.G6.05.01)
- **Skill**: Use webcam as 3D scene background for AR effects
- **Description**: Students use the "turn on webcam background" block to overlay 3D objects on live camera feeds, select front/back camera, configure flip modes, and create augmented reality effects where 3D models appear in the real world.
- **CreatiCode Blocks**:
  - `turn [ON/OFF] webcam background [FRONT/BACK] in [NORMAL/FLIPPED] mode`
- **Dependencies**: T30.G3.05 (camera access), T30.G5.05 (3D cameras), T30.G6.04

---

### 1.4 T30.G6.06 - "Implement hand and 2D body tracking in CreatiCode projects"

**Current Issue**: Combines two separate computer vision features (hand detection + 2D body parts).

**Current Description**:
> "Students use hand detection (tracking finger curl angles) and 2D body part recognition (single or multiple person modes) to create gesture-controlled games..."

**Problem**: Hand detection and body tracking are distinct features that should be taught separately.

**Proposed Breakdown**:

#### T30.G6.06 (UPDATED)
- **Skill**: Use hand detection for gesture recognition
- **Description**: Students use hand detection blocks to track finger curl angles, finger directions, and 21 hand keypoints in CreatiCode projects, creating hand gesture controls for games and applications that recognize hand poses and finger movements.
- **CreatiCode Blocks**:
  - `run hand detection debug [TRUE/FALSE] table [NAME]`
  - `hand [LEFT/RIGHT] finger [THUMB/INDEX/etc] curl [NOCURL/HALFCURL/FULLCURL]?` (boolean)
  - `hand [LEFT/RIGHT] finger [FINGER] direction [UP/DOWN/LEFT/RIGHT]?` (boolean)
  - `hand [LEFT/RIGHT] keypoint [1-21] x/y` (reporters)
- **Dependencies**: T30.G3.05 (camera), T30.G5.06 (face detection), T30.G5.01, T05.G5.01

#### T30.G6.06.01 (RENAME from 3D pose → 2D body tracking)
- **Skill**: Use 2D body part recognition for pose detection
- **Description**: Students use 2D body part recognition to detect body keypoints (shoulders, elbows, wrists, hips, knees, ankles) in single or multiple person modes, creating pose-based games and fitness applications that track body movement in 2D space.
- **CreatiCode Blocks**:
  - `run 2D body parts recognition on [SINGLE/MULTIPLE] person debug [TRUE/FALSE] table [NAME]`
  - `person [N] body part [PART] x/y` (reporters)
- **Dependencies**: T30.G6.06 (hand detection), T09.G5.01

#### T30.G6.06.02 (RENAME from 3D dragging → 3D pose)
- **Skill**: Use 3D pose detection for depth-aware body tracking
- **Description**: Students implement 3D pose detection (detecting x/y/z positions of 33 body parts) to create depth-aware gesture games where the camera tracks player movement in 3D space, comparing 2D body parts vs 3D pose and understanding when depth information improves interactions.
- **CreatiCode Blocks**:
  - `run 3D pose detection debug [TRUE/FALSE] table [NAME]`
  - `body part [0-32] x/y/z` (reporters)
- **Dependencies**: T30.G6.06.01 (2D body parts), T30.G5.05 (3D cameras), T05.G5.01

#### T30.G6.06.03 (NEW - relocate from old T30.G6.06.02)
- **Skill**: Implement 3D object dragging with mouse
- **Description**: Students configure 3D objects to be draggable using "set dragging mode", create event handlers for dragging events, and use "dragged 3D object name" reporter to build interactive 3D scenes where users can reposition objects.
- **CreatiCode Blocks**:
  - `set dragging mode [MODE] direction x (X) y (Y) z (Z)`
  - `when this 3D object starts dragging` (hat block)
  - `when this 3D object is dragged` (hat block)
  - `dragged 3D object name` (reporter)
- **Dependencies**: T30.G4.05.02 (mouse drag events), T30.G5.05.02 (mouse picking)

---

### 1.5 T30.G5.06.01 - "Select appropriate sensors for different CreatiCode project types"

**Current Issue**: Too vague and evaluative for Grade 5. Doesn't teach a specific skill.

**Current Description**:
> "Students analyze different CreatiCode project types (quiz game, drawing app, fitness tracker, voice assistant, AR game) and justify which sensors (keyboard, mouse, camera, microphone) best suit each project's purpose..."

**Problem**: This is a meta-analysis skill, not a hands-on hardware skill. Should be merged into prerequisite skills or made more concrete.

**Proposed Change**:

#### Option A: MERGE into T30.G5.01
Merge this content into T30.G5.01 "Identify device requirements for CreatiCode AI features" as an extended activity.

#### Option B: MAKE MORE CONCRETE → T30.G5.06.01 (UPDATED)
- **Skill**: Design multi-sensor interactive projects
- **Description**: Students design and build CreatiCode projects that combine multiple input sensors (keyboard for menu navigation, camera for visual effects, mouse for object selection) to create richer interactions, understanding how to coordinate different input types for better user experiences.
- **Dependencies**: T30.G5.05, T30.G4.05.01, T30.G3.05, T09.G3.03

**Recommendation**: Choose Option A (merge into T30.G5.01) to avoid vague skill.

---

### 1.6 T30.G3.01 - "Connect project ideas to required sensors/actuators"

**Current Issue**: Title mentions "actuators" but CreatiCode has no actuator outputs (no LEDs, motors, etc.).

**Current Description**:
> "Students map CreatiCode project ideas (voice assistant, gesture game, face tracking app) to required hardware inputs (microphone, camera, keyboard, mouse) and explain how each sensor enables the project."

**Problem**: "Actuators" is misleading - CreatiCode is software-only with no hardware outputs.

**Proposed Fix**:

#### T30.G3.01 (UPDATED)
- **Skill**: Match project ideas to required input devices
- **Description**: Students map CreatiCode project ideas (voice assistant, gesture game, face tracking app, drawing tool) to required input devices (microphone, camera, keyboard, mouse) and explain how each input device enables specific project features.
- **Dependencies**: (unchanged) T30.G2.01, T30.G2.02

---

## Part 2: Missing Feature Coverage (2 gaps)

### Priority: MEDIUM

### 2.1 AR Features (Currently in T18, should reference from T30)

**Current Status**: AR blocks are covered in T18 (3D Worlds):
- T18.G8.04.01: Enable AR world camera mode
- T18.G8.04.02: Enable AR face tracking mode
- T18.G8.04.03: Enable AR image/logo tracking mode

**Issue**: These are camera/hardware features that logically belong in T30, not T18.

**Available CreatiCode Blocks**:
- `switch to AR world camera scale (SCALE) emulation mode (MODE)`
- `switch to AR face camera show marker (SHOW) scale (SCALE) emulation mode (MODE)`
- `switch to AR LOGO as [LOGO/IMAGE] camera`

**Proposed Solution**: Add T30 skills that reference or duplicate T18 AR skills

#### T30.G7.07.01 (NEW)
- **Skill**: Enable AR world camera for object placement
- **Description**: Students use AR world camera mode to overlay 3D objects on real-world surfaces detected by the device camera, understanding how AR uses camera input and device sensors to place virtual objects in physical space.
- **CreatiCode Blocks**:
  - `switch to AR world camera scale (SCALE) emulation mode (MODE)`
- **Dependencies**: T30.G6.05.03 (webcam background), T30.G5.05 (3D cameras), T18.G7.01 (3D scene basics)
- **Cross-Reference**: T18.G8.04.01

#### T30.G7.07.02 (NEW)
- **Skill**: Enable AR face tracking for face filters
- **Description**: Students use AR face camera mode to attach 3D objects to detected faces, creating face filter effects where virtual objects follow facial features, understanding how computer vision enables face-anchored AR experiences.
- **CreatiCode Blocks**:
  - `switch to AR face camera show marker (SHOW) scale (SCALE) emulation mode (MODE)`
- **Dependencies**: T30.G7.07.01 (AR world camera), T30.G5.06 (face detection)
- **Cross-Reference**: T18.G8.04.02

#### T30.G7.07.03 (NEW)
- **Skill**: Enable AR logo and image tracking
- **Description**: Students use AR logo/image tracking mode to display 3D content when specific images or logos are detected by the camera, creating marker-based AR applications where printed images trigger virtual content.
- **CreatiCode Blocks**:
  - `switch to AR LOGO as [LOGO/IMAGE] camera`
- **Dependencies**: T30.G7.07.02 (AR face tracking)
- **Cross-Reference**: T18.G8.04.03

**Alternative**: Keep AR in T18 but ensure T30 has cross-references/dependencies properly set.

---

### 2.2 Location Sensing (Not Currently Covered)

**Issue**: User analysis mentions "Location sensing (latitude, longitude, geo info)" but no skills exist.

**Question**: Does CreatiCode have location/GPS blocks?

**If YES, add**:

#### T30.G7.08 (NEW - if blocks exist)
- **Skill**: Access device location for geo-aware projects
- **Description**: Students use location sensing blocks to access device latitude, longitude, and geographic information in CreatiCode projects, understanding when location access is appropriate and how to protect user privacy when using location data.
- **CreatiCode Blocks**: [TO BE DETERMINED - need to verify blocks exist]
  - `latitude` (reporter)
  - `longitude` (reporter)
  - `geo info [FIELD]` (reporter)
- **Dependencies**: T30.G6.03 (privacy permissions), T30.G5.01
- **Privacy Note**: Emphasize privacy, consent, and appropriate use cases

**If NO blocks exist**: Remove from requirements list - no skill needed.

---

## Part 3: Dependency Fixes (3 errors)

### Priority: HIGH (Critical Corrections)

### 3.1 T30.G7.06 - Wrong Dependency ID

**Current Dependency**: T30.G5.01 (Identify device requirements for CreatiCode AI features)
**Should Be**: T30.G4.05 (Respond to keyboard and mouse events in CreatiCode)

**Skill**: T30.G7.06 - Optimize CreatiCode projects for mobile vs desktop devices

**Fix**:
```
Dependencies:
* T30.G4.05: Respond to keyboard and mouse events in CreatiCode  ← CORRECTED
* T30.G5.05: Configure 3D cameras for CreatiCode game scenes
```

---

### 3.2 T30.G4.05.01 - Unrelated Dependency

**Current Skill**: Add camera preview widgets
**Current Dependencies**: Includes T30.G4.05 (keyboard/mouse events) - WRONG

**Issue**: Camera widgets don't require keyboard/mouse knowledge.

**Fix**:
```
Dependencies:
* T30.G3.05: Access device camera in CreatiCode projects
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
[REMOVE: T30.G4.05]
```

---

### 3.3 T30.G4.03.01 - Weak Connection

**Current Skill**: Compare 2D camera widgets vs 3D webcam backgrounds
**Current Dependencies**: Includes T30.G4.03 (Differentiate latency vs bandwidth)

**Issue**: Comparing 2D widgets vs 3D backgrounds doesn't require networking knowledge.

**Fix**:
```
Dependencies:
* T30.G3.05: Access device camera in CreatiCode projects
* T06.G2.01, T06.G2.02, T07.G2.01
[REMOVE: T30.G4.03]
```

---

## Part 4: Skills Needing Description Updates (5 skills)

### Priority: MEDIUM

### 4.1 T30.G3.04 - "Explain how sensors provide input to computer programs"

**Current Description**:
> "Students connect the conceptual understanding of sensors (camera, microphone) from Grade 2 to how programs use sensor data, explaining how a camera provides image data that programs can analyze and how a microphone provides audio data that programs can process."

**Issue**: Too abstract and wordy for Grade 3.

**Suggested Revision**:
> "Students explain how sensors provide input to programs by describing how a camera captures image data that programs can analyze (e.g., detecting faces, colors) and how a microphone captures audio data that programs can process (e.g., recognizing speech, detecting loudness)."

---

### 4.2 T30.G5.03 - "Explain how different sensors collect data"

**Current Description**:
> "Students describe what each sensor measures (microphones capture sound waves, cameras capture light, accelerometers measure motion) and give one CreatiCode use case for each."

**Issue**: Mentions "accelerometers" which don't exist in CreatiCode.

**Suggested Revision**:
> "Students describe what each sensor measures (microphones capture sound waves as audio data, cameras capture light as image data, keyboards capture key presses as input signals, mice capture position and button states) and give one CreatiCode use case for each sensor type."

---

### 4.3 T30.G6.01 - "Analyze sensor specifications for CreatiCode projects"

**Current Description**:
> "Students read simplified spec sheets for cameras and microphones used in CreatiCode and decide which specifications (resolution, sample rate, frame rate) are important for different project types (face detection vs speech recognition)."

**Issue**: "Spec sheets" are external hardware docs, not CreatiCode features.

**Suggested Revision**:
> "Students analyze sensor requirements for CreatiCode projects by comparing camera specifications (resolution, frame rate needed for face detection vs hand tracking) and microphone specifications (sample rate for speech recognition vs sound detection), understanding how sensor quality affects project performance."

---

### 4.4 T30.G7.01 - "Monitor and optimize CreatiCode project performance"

**Current Description**:
> "Students use browser developer tools or CreatiCode features to monitor frame rate, lag, and responsiveness, then optimize projects by reducing sprite complexity or adjusting AI update frequency."

**Issue**: "Browser developer tools" may be too advanced for Grade 7. Be more specific.

**Suggested Revision**:
> "Students monitor CreatiCode project performance by observing frame rate, lag, and responsiveness during testing, then optimize projects by reducing sprite complexity, limiting AI update frequency, or simplifying visual effects to improve performance on different devices."

---

### 4.5 T30.G4.02 - "Explain how device performance affects project responsiveness"

**Current Description**:
> "Learners compare how CreatiCode projects perform on different devices (simple animation vs multi-sprite AI game) and describe how device speed affects frame rate, AI processing time, and user experience."

**Issue**: Slightly vague - what exactly are students doing?

**Suggested Revision**:
> "Students compare how the same CreatiCode project performs on different devices (fast vs slow computers, desktop vs mobile) by testing simple animations and AI-powered games, then describe how device speed affects frame rate, AI processing time, and overall user experience."

---

## Part 5: Grade Placement Issues (1 skill)

### Priority: LOW

### 5.1 T30.G4.05.01 - Camera Widgets Too Early?

**Current Grade**: 4
**Skill**: Add camera preview widgets

**Issue**: Camera widgets are UI elements that might be more appropriate at Grade 5-6 when students work with more complex UI layouts.

**Analysis**:
- G3: Basic camera access (T30.G3.05) ✓
- G4: Camera widgets (current placement)
- G6: Webcam as 3D background (T30.G6.05.03)

**Recommendation**: Keep at G4 OR move to G5 if widgets seem too advanced.

---

## Part 6: Cross-Topic Dependencies (For Phase 2)

### Priority: LOW (Phase 2 work)

These skills reference other topics but lack formal dependencies:

### 6.1 T30.G7.04 - Cloud vs edge processing
**References**: T21 (image generation), T22 (ChatGPT), T23 (speech recognition)
**Add Dependencies**:
- T21.G6.01 or T21.G7.01
- T22.G6.01 or T22.G7.01
- T23.G6.01 or T23.G7.01

### 6.2 T30.G8.01 - Device-cloud architecture
**References**: Same as T30.G7.04
**Add Dependencies**: Same as above

---

## Part 7: Proposed Skill Count After Optimization

| Grade | Current | After Breakdown | Change |
|-------|---------|-----------------|--------|
| K     | 3       | 3               | 0      |
| 1     | 3       | 3               | 0      |
| 2     | 5       | 5               | 0      |
| 3     | 6       | 6               | 0      |
| 4     | 7       | 11              | +4     |
| 5     | 8       | 9               | +1     |
| 6     | 9       | 14              | +5     |
| 7     | 7       | 11              | +4     |
| 8     | 4       | 4               | 0      |
| **Total** | **52** | **66** | **+14** |

**Note**: Skill count increase reflects proper granularity, not scope creep. Each new skill teaches ONE specific feature/block set.

---

## Part 8: Priority Order (High → Medium → Low)

### HIGH Priority (Do First)

1. **Break down T30.G4.05** (keyboard/mouse/sprite drag) → 4 sub-skills
2. **Fix dependency errors**:
   - T30.G7.06 (wrong ID)
   - T30.G4.05.01 (unrelated dependency)
   - T30.G4.03.01 (weak connection)
3. **Break down T30.G5.05** (3D cameras) → 3 sub-skills
4. **Update T30.G3.01** (remove "actuators" from title)

### MEDIUM Priority (Do Second)

5. **Break down T30.G6.05** (speech recognition + TTS) → 4 sub-skills
6. **Break down T30.G6.06** (hand + body tracking) → 4 sub-skills
7. **Update skill descriptions** (5 skills: T30.G3.04, T30.G5.03, T30.G6.01, T30.G7.01, T30.G4.02)
8. **Address AR features** (decide: duplicate in T30 or just cross-reference T18)

### LOW Priority (Do Last)

9. **Merge/remove T30.G5.06.01** (sensor selection meta-skill)
10. **Verify location sensing** (check if blocks exist, add skill if yes)
11. **Review camera widget grade placement** (T30.G4.05.04 - consider moving to G5)

---

## Part 9: Implementation Checklist

### Phase 1A: Critical Fixes (1-2 days)

- [ ] Split T30.G4.05 into T30.G4.05, T30.G4.05.01, T30.G4.05.02, T30.G4.05.03
- [ ] Relocate camera widgets to T30.G4.05.04
- [ ] Fix T30.G7.06 dependency (G5.01 → G4.05)
- [ ] Fix T30.G4.05.01 dependencies (remove G4.05)
- [ ] Fix T30.G4.03.01 dependencies (remove G4.03)
- [ ] Update T30.G3.01 title (remove "actuators")

### Phase 1B: Feature Breakdown (2-3 days)

- [ ] Split T30.G5.05 into T30.G5.05, T30.G5.05.01, T30.G5.05.02
- [ ] Split T30.G6.05 into T30.G6.05, T30.G6.05.01, T30.G6.05.02, T30.G6.05.03
- [ ] Split T30.G6.06 into T30.G6.06, T30.G6.06.01, T30.G6.06.02, T30.G6.06.03
- [ ] Update dependencies for all new sub-skills

### Phase 1C: Description Improvements (1 day)

- [ ] Update T30.G3.04 description (simplify wording)
- [ ] Update T30.G5.03 description (remove accelerometers)
- [ ] Update T30.G6.01 description (clarify "spec sheets")
- [ ] Update T30.G7.01 description (clarify dev tools)
- [ ] Update T30.G4.02 description (add testing detail)

### Phase 1D: Gap Analysis (1 day)

- [ ] Verify if location sensing blocks exist in CreatiCode
- [ ] If yes: Add T30.G7.08 (location sensing skill)
- [ ] If no: Document as "not available"
- [ ] Decide on AR features: duplicate in T30 or cross-reference T18?
- [ ] If duplicate: Add T30.G7.07.01, T30.G7.07.02, T30.G7.07.03

### Phase 1E: Meta-Skills (1 day)

- [ ] Merge T30.G5.06.01 into T30.G5.01 OR make more concrete
- [ ] Review camera widget placement (keep at G4 or move to G5?)

### Phase 2: Cross-Topic Dependencies (Later)

- [ ] Add T21/T22/T23 dependencies to T30.G7.04
- [ ] Add T21/T22/T23 dependencies to T30.G8.01
- [ ] Ensure T23 skills complement T30 sensor skills

---

## Part 10: Expected Outcomes

### Accuracy Improvements
✓ No skills covering multiple unrelated features
✓ Each skill teaches ONE specific block/feature set
✓ All dependencies point to correct skill IDs
✓ No references to non-existent hardware (actuators, accelerometers)

### Completeness Improvements
✓ 3D camera configuration parameters covered
✓ Speech recognition properly split (one-shot vs continuous)
✓ Keyboard, mouse, and sprite drag events separated
✓ Hand detection and body tracking separated
✓ AR features addressed (via T18 cross-reference or T30 duplication)

### Clarity Improvements
✓ Grade-appropriate skill descriptions
✓ Specific, actionable learning objectives
✓ Proper scaffolding from simple to complex
✓ Clear block coverage for each skill

### Dependency Quality
✓ No circular dependencies within T30
✓ No unnecessary same-grade dependencies
✓ Logical prerequisite chains (X-2 rule followed)
✓ Cross-topic references documented for Phase 2

---

## Part 11: Questions for Clarification

1. **Location Sensing**: Does CreatiCode have latitude/longitude/geo info blocks? If yes, provide block names.

2. **AR Features**: Should T30 duplicate T18's AR skills (T18.G8.04.01-03) or just add cross-references?

3. **Camera Widget Placement**: Should T30.G4.05.04 (camera widgets) stay at Grade 4 or move to Grade 5?

4. **Sensor Selection Skill**: Should T30.G5.06.01 be:
   - Option A: Merged into T30.G5.01
   - Option B: Made more concrete (multi-sensor project design)
   - Option C: Removed entirely

5. **3D Camera Limits**: Are the camera configuration blocks (min/max distance, speed ratios, angle limits) important enough to warrant a separate skill (T30.G5.05.01)?

---

## Conclusion

This optimization plan addresses 6 overly broad skills, 3 dependency errors, 2 missing feature gaps, and 5 description issues. The proposed changes will increase skill count from 52 to 66, but each new skill will teach a specific, focused feature set that students can master independently.

**Next Steps**:
1. Review and approve proposed skill breakdowns
2. Clarify questions about location sensing and AR features
3. Implement Phase 1A critical fixes
4. Proceed through Phase 1B-E systematically
5. Prepare for Phase 2 cross-topic dependency updates

**Quality Target**: Production-ready T30 with accurate, complete, and well-structured skills covering all CreatiCode hardware/sensor blocks.
