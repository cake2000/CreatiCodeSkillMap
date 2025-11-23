# T23 AI Perception - Before/After Changes Detail

## NEW SKILLS ADDED (6 Total)

### 1. T23.G5.06 - NEW BRIDGE SKILL
**Status:** ✅ ADDED
**Location:** After T23.G5.05
**Grade:** 5

**Complete Skill:**
```
ID: T23.G5.06
Topic: T23 – AI Perception
Skill: Understand perception API workflow patterns
Description: Students learn the common pattern for using perception APIs: (1) start detection
with configuration, (2) read results from output table, (3) process data with conditionals,
(4) stop detection. They examine annotated code examples for hand, speech, and body detection
showing this pattern. They match API blocks to workflow steps (start→read→process→stop) using
diagrams. Picture-based workflow analysis, no coding yet.
Dependencies:
* T23.G5.05: Identify what data hand, body, and face detection provides
Grade: 5
```

---

### 2. T23.G6.04.04 - NEW GESTURE RECOGNITION PRACTICE
**Status:** ✅ ADDED
**Location:** After T23.G6.04.03
**Grade:** 6

**Complete Skill:**
```
ID: T23.G6.04.04
Topic: T23 – AI Perception
Skill: Recognize basic gestures from hand detection data
Description: Students use hand detection curl and direction data to identify 3-5 basic gestures:
fist (all fingers curl < 90), open hand (all curl > 150), pointing (index curl > 170, others < 90),
thumbs up (thumb curl > 170 and dir near 0°), peace sign (index and middle curl > 170, others < 90).
They use if-blocks to check conditions and display gesture names. No UI integration yet, just
gesture recognition logic.
Dependencies:
* T23.G6.04.03: Read finger direction data for advanced gesture recognition
Grade: 6
```

---

### 3. T23.G6.06B - NEW PERFORMANCE PATTERN SKILL
**Status:** ✅ ADDED
**Location:** After T23.G6.06
**Grade:** 6

**Complete Skill:**
```
ID: T23.G6.06B
Topic: T23 – AI Perception
Skill: Choose continuous vs. event-driven detection patterns
Description: Students compare two detection patterns: (1) continuous polling in forever loop
(constantly read table and update), (2) event-driven (start detection, wait for specific condition,
then act). They implement both patterns with hand detection: continuous mode moves sprite smoothly
following hand, event-driven mode triggers action when gesture detected. They discuss trade-offs:
continuous is smooth but CPU-intensive, event-driven is efficient but may miss quick gestures.
Dependencies:
* T23.G6.04.04: Recognize basic gestures from hand detection data
* T23.G6.06: Smooth noisy sensor data and recover from dropouts
Grade: 6
```

---

### 4. T23.G7.01B - NEW OR LOGIC SKILL
**Status:** ✅ ADDED
**Location:** After T23.G7.01
**Grade:** 7

**Complete Skill:**
```
ID: T23.G7.01B
Topic: T23 – AI Perception
Skill: Combine inputs with simple OR logic
Description: Students build interactions where users can choose different input methods:
"say 'next' OR perform swipe gesture" to advance, "press space bar OR raise hand" to start game.
They use OR conditions to check multiple inputs and trigger the same action. They learn when OR
logic is appropriate (giving users choices) vs. when specific input is required. Simpler than
AND multimodal confirmation (G7.02).
Dependencies:
* T23.G7.01: Define a reusable gesture dictionary
* T23.G6.02: Map speech commands to UI widgets
Grade: 7
```

---

### 5. T23.G7.06B - NEW OPTIMIZATION SKILL
**Status:** ✅ ADDED
**Location:** After T23.G7.06
**Grade:** 7

**Complete Skill:**
```
ID: T23.G7.06B
Topic: T23 – AI Perception
Skill: Optimize perception system performance
Description: Students identify and fix perception performance issues: reduce detection frame rate
(process every 3rd frame instead of every frame), limit table size (clear old data), disable debug
visualization in production, use efficient data structures (variables for single values instead of
searching tables). They measure and compare performance before/after optimization using timer blocks.
They understand trade-offs between accuracy and speed.
Dependencies:
* T23.G7.06: Build a calibration wizard for sensors
* T23.G6.06B: Choose continuous vs. event-driven detection patterns
Grade: 7
```

---

### 6. T23.G8.01A - NEW KNN PRACTICE SKILL
**Status:** ✅ ADDED
**Location:** After T23.G8.00A (before original G8.01)
**Grade:** 8

**Complete Skill:**
```
ID: T23.G8.01A
Topic: T23 – AI Perception
Skill: Practice KNN classification with simple numeric data
Description: Students practice KNN with a simple dataset before gesture classification: given a table
of measurements (height, weight) and labels (category), they use `create KNN number classifier from
table [training v] K [3] named [simple]` to train a classifier, then test it with new data using
`predict for table [test v] with classifier [simple] show neighbors [yes v]`. They experiment with
K values (1, 3, 5) and observe how it affects predictions. They understand KNN finds "similar" examples.
Dependencies:
* T23.G8.00A: Understand supervised learning for perception classification
* T10.G6.02: Sort a table by a column
Grade: 8
```

---

## MODIFIED SKILLS (9 Total)

### 1. T23.G5.05 - ADDED CONCRETE ACTIVITY
**Status:** ✅ MODIFIED

**BEFORE:**
```
Description: Students learn that AI vision blocks can detect specific features: hand detection
finds finger positions and curl angles, body detection finds body part positions, and face
detection finds face locations. They match detection types to data outputs (tables with x, y
coordinates, angles, etc.) to prepare for G6 coding.
```

**AFTER:**
```
Description: Students learn that AI vision blocks can detect specific features: hand detection
finds finger positions and curl angles, body detection finds body part positions, and face
detection finds face locations. They sort picture cards showing different detection types
(hand/body/face) to their data outputs (finger angles, body positions, face landmarks). They
match detection types to data outputs (tables with x, y coordinates, angles, etc.) to prepare
for G6 coding.
```

**CHANGES:**
- ✅ Added concrete activity: sorting picture cards
- ✅ Makes learning more hands-on and tangible

---

### 2. T23.G6.01.01 - ADDED COMPLETE TECHNICAL DETAILS
**Status:** ✅ MODIFIED

**BEFORE:**
```
Description: Students use the basic speech recognition flow: `start recognizing speech in
[English (United States) v] record as []` (with default language), wait briefly, then `end
speech recognition` to capture a single spoken word or phrase. They display the result using
the `text from speech` reporter block and a `say` block or variable monitor.
```

**AFTER:**
```
Description: Students use the basic speech recognition flow: `start recognizing speech in
[English (United States) v] record as []` (with default language), wait briefly, then `end
speech recognition` to capture a single spoken word or phrase. The recognized text is stored
in a variable (not in a table). They display the result using the `text from speech` reporter
block and a `say` block or variable monitor. Common issues include silent rooms (no input
detected), background noise (mis-recognition), and recognition delay (typically 1-3 seconds
after speaking stops).
```

**CHANGES:**
- ✅ Clarified storage: variable, not table
- ✅ Added common issues: silent room, background noise
- ✅ Added timing info: 1-3 seconds delay

---

### 3. T23.G6.02 - ADDED TTS DEPENDENCY
**Status:** ✅ MODIFIED

**BEFORE:**
```
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.01.02: Select speech recognition language and observe accuracy differences
* T23.G4.02: Choose a good setup for mic or camera
```

**AFTER:**
```
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.01.02: Select speech recognition language and observe accuracy differences
* T23.G6.02.01: Convert text to speech with basic settings
* T23.G4.02: Choose a good setup for mic or camera
```

**CHANGES:**
- ✅ Added dependency on T23.G6.02.01 (TTS skill)
- ✅ Ensures students learn TTS before command mapping

---

### 4. T23.G6.04.02 - ADDED COMPLETE TABLE STRUCTURE
**Status:** ✅ MODIFIED (HIGH PRIORITY)

**BEFORE:**
```
Description: Students read the result table from `run hand detection table [result v] debug
[yes v] show video [yes v]` to get curl angles for each finger (thumb, index, middle, ring,
pinky). Curl angles range from 0 (fully curled/fist) to 180 (fully extended/straight). They
display curl values on screen and recognize simple gestures like pointing (index curl > 170,
others < 170) or fist (all curl < 90).
```

**AFTER:**
```
Description: Students read the result table from `run hand detection table [result v] debug
[yes v] show video [yes v]` to get hand detection data. The table contains 47 rows per detected
hand with complete structure: the first 5 rows contain finger summaries (one row per finger:
thumb, index, middle, ring, pinky) with columns [hand, part, curl, dir, x, y, z]; followed by
21 rows of 2D landmark positions; then 21 rows of 3D landmark positions. Curl angles range from
0° (fully curled/fist) to 180° (fully extended/straight). Direction (dir) ranges from 0° to 360°
indicating pointing direction. X and Y are screen coordinates, Z is depth. They display curl
values on screen and recognize simple gestures like pointing (index curl > 170, others < 170)
or fist (all curl < 90).
```

**CHANGES:**
- ✅ Added complete table structure: 47 rows per hand
- ✅ Breakdown: 5 finger summary + 21 2D + 21 3D landmarks
- ✅ All column names: hand, part, curl, dir, x, y, z
- ✅ Value ranges: curl 0-180°, dir 0-360°
- ✅ Coordinate system explained

---

### 5. T23.G6.05 - UPDATED DEPENDENCY
**Status:** ✅ MODIFIED

**BEFORE:**
```
Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T23.G6.04.02: Read and display finger curl angles from hand detection
```

**AFTER:**
```
Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T23.G6.04.04: Recognize basic gestures from hand detection data
```

**CHANGES:**
- ✅ Changed from G6.04.02 to G6.04.04
- ✅ UI integration now comes after gesture recognition practice

---

### 6. T23.G6.06 - ADDED HAND DETECTION DEPENDENCY
**Status:** ✅ MODIFIED

**BEFORE:**
```
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G5.05: Use the accumulator pattern to compute running totals
* T23.G4.03: Identify noise and simple fixes
```

**AFTER:**
```
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G5.05: Use the accumulator pattern to compute running totals
* T23.G6.04.02: Read and display finger curl angles from hand detection
* T23.G4.03: Identify noise and simple fixes
```

**CHANGES:**
- ✅ Added T23.G6.04.02 dependency
- ✅ Students must understand hand data before smoothing it

---

### 7. T23.G6.08.01 - ADDED COMPLETE BODY POSE DETAILS
**Status:** ✅ MODIFIED (HIGH PRIORITY)

**BEFORE:**
```
Description: Students use `run 2D body part recognition single person [yes v] table [TABLENAME v]
debug [yes v]` to detect body landmarks (nose, shoulders, elbows, wrists, hips, knees, ankles)
with x/y coordinates. They display keypoint positions on screen and create simple applications
like a virtual mirror. They also explore multi-person mode (`single person [no v]`) which returns
data with person IDs.
```

**AFTER:**
```
Description: Students use `run 2D body part recognition single person [yes v] table [TABLENAME v]
debug [yes v]` to detect body landmarks with x/y coordinates. The detection identifies all 17
keypoints: nose, left_eye, right_eye, left_ear, right_ear, left_shoulder, right_shoulder,
left_elbow, right_elbow, left_wrist, right_wrist, left_hip, right_hip, left_knee, right_knee,
left_ankle, right_ankle. The table also includes 4 limb measurements (left_arm, right_arm,
left_leg, right_leg) with curl and dir values. Table columns are: id, part, x, y, curl, dir.
They display keypoint positions on screen and create simple applications like a virtual mirror.
Multi-person mode (`single person [no v]`) assigns each person a unique ID in the table.
```

**CHANGES:**
- ✅ All 17 keypoints enumerated explicitly
- ✅ Added 4 limb measurements with curl and dir
- ✅ Complete column structure: id, part, x, y, curl, dir
- ✅ Multi-person mode explanation improved

---

### 8. T23.G6.09.02 - ADDED COMPLETE FACE DETECTION DETAILS
**Status:** ✅ MODIFIED (HIGH PRIORITY)

**BEFORE:**
```
Description: Students read the face detection table to get face position (x, y coordinates) and
use it to trigger events: move a sprite to follow the face, display a message when a face is
detected, or count the number of faces. They understand how lighting affects detection accuracy
and implement error handling for "no face detected."
```

**AFTER:**
```
Description: Students read the face detection table to get face position and attributes. The
table contains 13 rows per detected face: 1 row for tilt angle, plus 12 rows for 6 facial landmark
positions (left_eye, right_eye, nose, mouth, left_ear, right_ear, each with x and y coordinates).
Table columns are: ID, variable, value. They use this data to trigger events: move a sprite to
follow the face, display a message when a face is detected, or count the number of faces. They
understand how lighting affects detection accuracy, note that face data can be noisy and may need
smoothing, and implement error handling for "no face detected."
```

**CHANGES:**
- ✅ Table structure: 13 rows per face (1 tilt + 12 landmarks)
- ✅ 6 facial landmarks enumerated: left_eye, right_eye, nose, mouth, left_ear, right_ear
- ✅ Column structure: ID, variable, value
- ✅ Added note about data noise needing smoothing

---

### 9. T23.G7.04 - ADDED ASSESSMENT CRITERIA
**Status:** ✅ MODIFIED

**BEFORE:**
```
Description: Students design an accessibility log where each speech/gesture event is recorded
with user metadata (age range, device type, lighting condition, language) plus outcome
(success/failure). They calculate accuracy rates per group and identify bias patterns (e.g.,
low-light users have 40% success vs 90% in good light). They propose adjustments based on data.
```

**AFTER:**
```
Description: Students design an accessibility log where each speech/gesture event is recorded
with user metadata (age range, device type, lighting condition, language) plus outcome
(success/failure). They calculate accuracy rates per group (success rate = correct detections /
total attempts) and identify significant disparities (>20% difference between groups), such as
low-light users having 40% success vs 90% in good light. They propose adjustments based on data.
```

**CHANGES:**
- ✅ Added formula: success rate = correct detections / total attempts
- ✅ Added threshold: >20% difference = significant disparity
- ✅ Provides clear, measurable assessment criteria

---

## SKILL MOVED/RENUMBERED (1 Total)

### T23.G6.10 → T23.G6.08.03
**Status:** ✅ MOVED

**BEFORE:**
```
ID: T23.G6.10
Topic: T23 – AI Perception
Skill: Use 3D pose detection for depth-aware body tracking
[Located at end of G6 sequence]
```

**AFTER:**
```
ID: T23.G6.08.03
Topic: T23 – AI Perception
Skill: Use 3D pose detection for depth-aware body tracking
[Located after G6.08.02, before G6.09.01]
```

**CHANGES:**
- ✅ Renumbered from G6.10 to G6.08.03
- ✅ Creates logical progression: 2D body → 2D poses → 3D depth → face
- ✅ All references updated (T23.G7.03 dependency updated)

**DEPENDENCY UPDATES:**
```
T23.G7.03 BEFORE:
* T23.G6.10: Use 3D pose detection for depth-aware body tracking

T23.G7.03 AFTER:
* T23.G6.08.03: Use 3D pose detection for depth-aware body tracking
```

---

## DEPENDENCY CHAIN UPDATES

### Skills with Updated Dependencies:

1. **T23.G6.02** - Added T23.G6.02.01
2. **T23.G6.05** - Changed to T23.G6.04.04
3. **T23.G6.06** - Added T23.G6.04.02
4. **T23.G7.01** - Added T23.G6.04.04
5. **T23.G7.02** - Added T23.G7.01
6. **T23.G7.03** - Changed from T23.G6.10 to T23.G6.08.03

---

## SUMMARY STATISTICS

### Changes by Type:
- **New Skills Added:** 6
- **Skills Modified:** 9
- **Skills Moved:** 1
- **Total Skills Affected:** 16
- **Dependencies Updated:** 6

### Changes by Priority:
- **HIGH Priority:** 7 changes (G5.06, G6.01.01, G6.04.02, G6.08.01, G6.09.02, G6.04.04, G6.10→G6.08.03)
- **MEDIUM Priority:** 9 changes (G6.02, G6.05, G6.06, G6.06B, G7.01, G7.01B, G7.02, G7.06B, G8.01A)

### Changes by Grade Level:
- **Grade 5:** 2 changes (G5.05, G5.06)
- **Grade 6:** 10 changes (G6.01.01, G6.02, G6.04.02, G6.04.04, G6.05, G6.06, G6.06B, G6.08.01, G6.08.03, G6.09.02)
- **Grade 7:** 4 changes (G7.01, G7.01B, G7.04, G7.06B)
- **Grade 8:** 1 change (G8.01A)

---

## VERIFICATION COMPLETED

✅ All new skills properly inserted
✅ All modified skills updated with new content
✅ All dependencies verified and updated
✅ Skill G6.10 successfully moved to G6.08.03
✅ No skills deleted
✅ Only T23 skills modified
✅ All cross-topic dependencies preserved
✅ File integrity verified
✅ Backup created before changes

**File:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
**Backup:** /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills_backup_before_t23_fixes.md
