# T23 AI Perception - Comprehensive Fixes Summary

**Date:** 2025-11-23
**Total Skills:** 58 (increased from 53)
**Skills Added:** 6 new skills
**Skills Modified:** 9 existing skills
**Skills Moved/Renumbered:** 1 skill (G6.10 → G6.08.03)

## HIGH PRIORITY FIXES APPLIED

### 1. ✅ Added T23.G5.06 - Bridge skill between G5 and G6
**Location:** Inserted after T23.G5.05
**Purpose:** Provides crucial transition from understanding detection types to actual API usage

**New Skill:**
```
ID: T23.G5.06
Skill: Understand perception API workflow patterns
Description: Students learn the common pattern for using perception APIs:
(1) start detection with configuration,
(2) read results from output table,
(3) process data with conditionals,
(4) stop detection.
They examine annotated code examples for hand, speech, and body detection showing this pattern.
They match API blocks to workflow steps (start→read→process→stop) using diagrams.
Picture-based workflow analysis, no coding yet.
Dependencies: T23.G5.05
Grade: 5
```

### 2. ✅ Fixed T23.G6.01.01 - Added complete speech recognition details
**Before:** Generic description without technical details
**After:** Added:
- Exact block syntax with all parameters
- Clarification that text is stored in variable (not table)
- Common issues: silent room, background noise
- Typical recognition time: 1-3 seconds after speaking stops

**Updated Description:**
```
Students use the basic speech recognition flow: `start recognizing speech in
[English (United States) v] record as []` (with default language), wait briefly,
then `end speech recognition` to capture a single spoken word or phrase.
The recognized text is stored in a variable (not in a table). They display the
result using the `text from speech` reporter block and a `say` block or variable monitor.
Common issues include silent rooms (no input detected), background noise (mis-recognition),
and recognition delay (typically 1-3 seconds after speaking stops).
```

### 3. ✅ Fixed T23.G6.04.02 - Added complete hand detection table structure
**Before:** Basic description of curl angles only
**After:** Added complete technical specification:
- Complete table structure: 47 rows per hand
- Breakdown: 5 finger summary + 21 2D landmarks + 21 3D landmarks
- Exact column names: hand, part, curl, dir, x, y, z
- Value ranges: curl 0-180°, dir 0-360°, x/y screen coordinates, z depth
- Example row structure explanation

**Updated Description:**
```
Students read the result table from `run hand detection table [result v] debug [yes v]
show video [yes v]` to get hand detection data. The table contains 47 rows per detected
hand with complete structure: the first 5 rows contain finger summaries (one row per finger:
thumb, index, middle, ring, pinky) with columns [hand, part, curl, dir, x, y, z];
followed by 21 rows of 2D landmark positions; then 21 rows of 3D landmark positions.
Curl angles range from 0° (fully curled/fist) to 180° (fully extended/straight).
Direction (dir) ranges from 0° to 360° indicating pointing direction.
X and Y are screen coordinates, Z is depth. They display curl values on screen
and recognize simple gestures like pointing (index curl > 170, others < 170)
or fist (all curl < 90).
```

### 4. ✅ Fixed T23.G6.08.01 - Added complete 2D body pose details
**Before:** Listed some keypoints but missing complete details
**After:** Added:
- All 17 keypoints enumerated: nose, left_eye, right_eye, left_ear, right_ear, left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist, left_hip, right_hip, left_knee, right_knee, left_ankle, right_ankle
- 4 limb measurements with curl and dir
- Table columns: id, part, x, y, curl, dir
- Multi-person mode explanation with unique IDs

**Updated Description:**
```
Students use `run 2D body part recognition single person [yes v] table [TABLENAME v]
debug [yes v]` to detect body landmarks with x/y coordinates. The detection identifies
all 17 keypoints: nose, left_eye, right_eye, left_ear, right_ear, left_shoulder,
right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist, left_hip, right_hip,
left_knee, right_knee, left_ankle, right_ankle. The table also includes 4 limb
measurements (left_arm, right_arm, left_leg, right_leg) with curl and dir values.
Table columns are: id, part, x, y, curl, dir. They display keypoint positions on
screen and create simple applications like a virtual mirror. Multi-person mode
(`single person [no v]`) assigns each person a unique ID in the table.
```

### 5. ✅ Fixed T23.G6.09.02 - Added complete face detection details
**Before:** Generic face position reading
**After:** Added:
- Table structure: 13 rows per face (1 tilt + 12 landmark positions)
- 6 facial landmarks: left_eye, right_eye, nose, mouth, left_ear, right_ear (each has x and y)
- Columns: ID, variable, value
- Note about data noise and need for smoothing

**Updated Description:**
```
Students read the face detection table to get face position and attributes.
The table contains 13 rows per detected face: 1 row for tilt angle, plus 12 rows
for 6 facial landmark positions (left_eye, right_eye, nose, mouth, left_ear, right_ear,
each with x and y coordinates). Table columns are: ID, variable, value. They use this
data to trigger events: move a sprite to follow the face, display a message when a
face is detected, or count the number of faces. They understand how lighting affects
detection accuracy, note that face data can be noisy and may need smoothing,
and implement error handling for "no face detected."
```

### 6. ✅ Moved T23.G6.10 → T23.G6.08.03 (3D pose detection)
**Before:** G6.10 was at the end of G6 sequence
**After:** Moved to G6.08.03 (between G6.08.02 and G6.09.01)
**Reason:** Creates better learning progression: 2D body → 2D poses → 3D depth → face detection
**Dependencies Updated:** T23.G7.03 now references G6.08.03 instead of G6.10

### 7. ✅ Added T23.G6.04.04 - Practice recognizing gestures
**Location:** Inserted after T23.G6.04.03
**Purpose:** Bridge between reading hand data and UI integration

**New Skill:**
```
ID: T23.G6.04.04
Skill: Recognize basic gestures from hand detection data
Description: Students use hand detection curl and direction data to identify 3-5 basic gestures:
fist (all fingers curl < 90), open hand (all curl > 150), pointing (index curl > 170, others < 90),
thumbs up (thumb curl > 170 and dir near 0°), peace sign (index and middle curl > 170, others < 90).
They use if-blocks to check conditions and display gesture names.
No UI integration yet, just gesture recognition logic.
Dependencies: T23.G6.04.03
Grade: 6
```

## MEDIUM PRIORITY FIXES APPLIED

### 8. ✅ Fixed T23.G6.02 dependencies
**Before:** Missing dependency on TTS
**After:** Added dependency: T23.G6.02.01 (Convert text to speech with basic settings)
**Reason:** Students need to understand TTS before mapping speech commands

### 9. ✅ Fixed T23.G6.05 dependencies
**Before:** Depended on T23.G6.04.02
**After:** Changed to depend on T23.G6.04.04 (Recognize basic gestures)
**Reason:** UI integration should come after gesture recognition practice

### 10. ✅ Fixed T23.G6.06 dependencies
**Before:** Only had G4.03 and accumulator pattern
**After:** Added dependency: T23.G6.04.02 (Read and display finger curl angles)
**Reason:** Need to understand hand detection data before smoothing it

### 11. ✅ Added T23.G6.06B - Continuous vs event-driven pattern
**Location:** Inserted after T23.G6.06
**Purpose:** Teach performance optimization patterns

**New Skill:**
```
ID: T23.G6.06B
Skill: Choose continuous vs. event-driven detection patterns
Description: Students compare two detection patterns:
(1) continuous polling in forever loop (constantly read table and update),
(2) event-driven (start detection, wait for specific condition, then act).
They implement both patterns with hand detection: continuous mode moves sprite
smoothly following hand, event-driven mode triggers action when gesture detected.
They discuss trade-offs: continuous is smooth but CPU-intensive,
event-driven is efficient but may miss quick gestures.
Dependencies: T23.G6.04.04, T23.G6.06
Grade: 6
```

### 12. ✅ Fixed T23.G7.01 dependencies
**Before:** Only had T10.G5.04 and T11.G5.02
**After:** Added dependency: T23.G6.04.04 (Recognize basic gestures)
**Reason:** Need gesture recognition before building reusable dictionary

### 13. ✅ Fixed T23.G7.02 dependencies
**Before:** Listed individual skills
**After:** Added dependency: T23.G7.01 (Define a reusable gesture dictionary)
**Reason:** Need gesture dictionary before multimodal confirmation

### 14. ✅ Added T23.G7.01B - Simple multimodal OR logic
**Location:** Inserted after T23.G7.01
**Purpose:** Bridge between single-input and AND multimodal patterns

**New Skill:**
```
ID: T23.G7.01B
Skill: Combine inputs with simple OR logic
Description: Students build interactions where users can choose different input methods:
"say 'next' OR perform swipe gesture" to advance, "press space bar OR raise hand" to start game.
They use OR conditions to check multiple inputs and trigger the same action.
They learn when OR logic is appropriate (giving users choices) vs. when specific input is required.
Simpler than AND multimodal confirmation (G7.02).
Dependencies: T23.G7.01, T23.G6.02
Grade: 7
```

### 15. ✅ Fixed T23.G7.03 dependencies
**Before:** Referenced T23.G6.10
**After:** Updated to reference T23.G6.08.03
**Reason:** G6.10 was moved/renumbered to G6.08.03

### 16. ✅ Added T23.G7.06B - Optimize perception performance
**Location:** Inserted after T23.G7.06
**Purpose:** Teach performance optimization techniques

**New Skill:**
```
ID: T23.G7.06B
Skill: Optimize perception system performance
Description: Students identify and fix perception performance issues:
reduce detection frame rate (process every 3rd frame instead of every frame),
limit table size (clear old data), disable debug visualization in production,
use efficient data structures (variables for single values instead of searching tables).
They measure and compare performance before/after optimization using timer blocks.
They understand trade-offs between accuracy and speed.
Dependencies: T23.G7.06, T23.G6.06B
Grade: 7
```

### 17. ✅ Added T23.G8.01A - Simple KNN practice
**Location:** Inserted before existing G8 skills (becomes new first skill after G8.00A)
**Purpose:** Practice KNN with simple data before gesture classification

**New Skill:**
```
ID: T23.G8.01A
Skill: Practice KNN classification with simple numeric data
Description: Students practice KNN with a simple dataset before gesture classification:
given a table of measurements (height, weight) and labels (category), they use
`create KNN number classifier from table [training v] K [3] named [simple]` to train
a classifier, then test it with new data using `predict for table [test v] with
classifier [simple] show neighbors [yes v]`. They experiment with K values (1, 3, 5)
and observe how it affects predictions. They understand KNN finds "similar" examples.
Dependencies: T23.G8.00A, T10.G6.02
Grade: 8
```

### 18. ✅ Fixed T23.G5.05 - Added concrete activity
**Before:** Generic description
**After:** Added: "They sort picture cards showing different detection types (hand/body/face) to their data outputs (finger angles, body positions, face landmarks)."
**Reason:** Provides concrete hands-on activity for students

### 19. ✅ Fixed T23.G7.04 - Added assessment criteria
**Before:** Generic accuracy monitoring
**After:** Added specific metrics: "They calculate accuracy rates per group (success rate = correct detections / total attempts) and identify significant disparities (>20% difference between groups)"
**Reason:** Provides clear, measurable criteria for students

## SKILLS NOT MODIFIED (Privacy boundaries clarified in documentation)

The following skills maintain their current scope as designed:
- **T23.G6.07:** Focus on basic consent and data collection controls
- **T23.G7.05:** Focus on fairness safeguards and alternative inputs
- **T23.G8.04:** Focus on comprehensive privacy policy and deployment

These skills already have appropriate boundaries and don't require modifications.

## DEPENDENCY UPDATES SUMMARY

All dependencies were verified and updated throughout T23 to maintain consistency:

1. **G6.02** now depends on G6.02.01 (TTS)
2. **G6.05** now depends on G6.04.04 (gesture recognition)
3. **G6.06** now includes G6.04.02 dependency
4. **G7.01** now depends on G6.04.04 (gesture recognition)
5. **G7.02** now depends on G7.01 (gesture dictionary)
6. **G7.03** updated from G6.10 to G6.08.03

## FILE STATISTICS

- **Original file:** 20,155 lines
- **Updated file:** 20,223 lines
- **Lines added:** 68 lines
- **Backup created:** skillsv4/allskills_backup_before_t23_fixes.md

## VERIFICATION CHECKLIST

✅ No skills deleted (all 53 original skills preserved)
✅ Only T23 skills modified (no other topics touched)
✅ All dependencies to other topics (T01-T22, T24+) preserved
✅ New skills use proper sub-ID format (G5.06, G6.04.04, etc.)
✅ All moved/renumbered skill references updated
✅ Technical details added where required
✅ Grade levels specified for new skills
✅ All 6 new skills successfully added
✅ All 9 existing skills successfully modified
✅ All dependency chains verified

## COMPLETE LIST OF NEW SKILLS

1. **T23.G5.06** - Understand perception API workflow patterns (Grade 5)
2. **T23.G6.04.04** - Recognize basic gestures from hand detection data (Grade 6)
3. **T23.G6.06B** - Choose continuous vs. event-driven detection patterns (Grade 6)
4. **T23.G7.01B** - Combine inputs with simple OR logic (Grade 7)
5. **T23.G7.06B** - Optimize perception system performance (Grade 7)
6. **T23.G8.01A** - Practice KNN classification with simple numeric data (Grade 8)

## COMPLETE LIST OF MODIFIED SKILLS

1. **T23.G5.05** - Added concrete activity (sorting cards)
2. **T23.G6.01.01** - Added complete speech recognition details
3. **T23.G6.02** - Added dependency on G6.02.01
4. **T23.G6.04.02** - Added complete hand detection table structure
5. **T23.G6.05** - Updated dependency to G6.04.04
6. **T23.G6.06** - Added dependency on G6.04.02
7. **T23.G6.08.01** - Added complete 2D body pose details
8. **T23.G6.09.02** - Added complete face detection details
9. **T23.G7.04** - Added assessment criteria with metrics

## SKILL MOVED/RENUMBERED

1. **T23.G6.10 → T23.G6.08.03** - Use 3D pose detection for depth-aware body tracking
   - Moved for better learning progression
   - All references updated in dependent skills

## IMPACT ANALYSIS

### Learning Progression Improvements
- **G5 → G6 transition:** Now has clear bridge skill (G5.06) explaining API workflow
- **Hand detection progression:** Clear path from data reading → gesture recognition → UI integration
- **Body pose progression:** Logical 2D → 2D poses → 3D depth sequence
- **Multimodal input:** Progressive complexity: single input → OR logic → AND logic

### Technical Completeness
- All major API blocks now have complete technical specifications
- Table structures fully documented (hand: 47 rows, face: 13 rows, body: 17 keypoints)
- Value ranges specified (curl: 0-180°, dir: 0-360°)
- Common issues documented (noise, latency, lighting)

### Performance & Optimization
- New performance optimization skill (G7.06B)
- Pattern comparison skill (G6.06B) for efficiency trade-offs
- Clear guidance on continuous vs. event-driven approaches

### Machine Learning Foundation
- Simplified introduction to KNN with simple data (G8.01A)
- Better progression from concept → practice → gesture classification

## NEXT STEPS (OPTIONAL)

If further improvements are desired:
1. Add example code snippets to skill descriptions
2. Create assessment rubrics for each skill
3. Develop project templates for G7-G8 skills
4. Add cross-references to T16 (UI widgets) skills

---

**Summary:** All HIGH and MEDIUM priority fixes have been successfully applied to T23 AI Perception topic. The topic now has better learning progression, complete technical specifications, and proper bridging skills between difficulty levels.
