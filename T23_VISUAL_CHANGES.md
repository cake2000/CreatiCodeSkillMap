# T23 AI Perception - Visual Changes Reference

## NEW SKILLS AT A GLANCE

```
GRADE 5 (Bridge to G6):
├── T23.G5.01 through G5.04 (existing)
├── T23.G5.05 (existing - enhanced)
└── ⭐ T23.G5.06 [NEW] - Perception API workflow patterns
    └── Purpose: Bridge conceptual understanding to hands-on coding

GRADE 6 (Hand Detection Path):
├── T23.G6.04.01 - Set up hand detection
├── T23.G6.04.02 - Read finger curl angles (ENHANCED with 47-row table structure)
├── T23.G6.04.03 - Read finger direction data
├── ⭐ T23.G6.04.04 [NEW] - Recognize basic gestures
│   └── Purpose: Practice gesture recognition before UI
├── T23.G6.05 - Drive UI elements
├── T23.G6.06 - Smooth noisy sensor data (DEPENDENCY ADDED)
└── ⭐ T23.G6.06B [NEW] - Continuous vs. event-driven patterns
    └── Purpose: Teach when to use loops vs single calls

GRADE 6 (Body Pose Path - REORGANIZED):
├── T23.G6.08.01 - 2D body pose (ENHANCED with all 17 keypoints + 4 limbs)
├── T23.G6.08.02 - Detect body poses
└── ⭐ T23.G6.08.03 [RENUMBERED from G6.10] - 3D pose detection
    └── Moved earlier for better progression

GRADE 6 (Face Detection):
├── T23.G6.09.01 - Set up face detection
└── T23.G6.09.02 - Read face data (ENHANCED with 13-row table structure)

GRADE 7 (Multimodal Progression):
├── T23.G7.01 - Define gesture dictionary (DEPENDENCY ADDED)
├── ⭐ T23.G7.01B [NEW] - Combine inputs with OR logic
│   └── Purpose: Simpler multimodal before AND confirmation
├── T23.G7.02 - Multimodal confirmation (AND)
├── T23.G7.06 - Build calibration wizard
└── ⭐ T23.G7.06B [NEW] - Optimize perception performance
    └── Purpose: Teach frame rate reduction, efficient data structures

GRADE 8 (Machine Learning):
├── T23.G8.00A - Understand supervised learning
├── ⭐ T23.G8.01A [NEW] - Practice KNN with simple data
│   └── Purpose: Practice classifier before building full system
└── T23.G8.02 - Train custom gesture classifier
```

---

## BEFORE vs AFTER: Key Progressions

### Hand Detection Learning Path

**BEFORE:**
```
G6.04.01 (setup)
    → G6.04.02 (read curl)
    → G6.04.03 (read direction)
    → [GAP]
    → G6.05 (drive UI) ❌ Too big jump!
```

**AFTER:**
```
G6.04.01 (setup)
    → G6.04.02 (read curl) [ENHANCED: 47-row table]
    → G6.04.03 (read direction)
    → ⭐ G6.04.04 (recognize gestures) [NEW]
    → G6.05 (drive UI) ✅ Clear progression!
```

---

### Body Pose Learning Path

**BEFORE:**
```
G6.08.01 (2D setup)
    → G6.08.02 (2D poses)
    → G6.09.01 (face setup)
    → G6.09.02 (face data)
    → G6.10 (3D pose) ❌ Too late!
```

**AFTER:**
```
G6.08.01 (2D setup) [ENHANCED: all 17 keypoints]
    → G6.08.02 (2D poses)
    → ⭐ G6.08.03 (3D pose) [MOVED from G6.10] ✅ Logical progression!
    → G6.09.01 (face setup)
    → G6.09.02 (face data) [ENHANCED: 13-row table]
```

---

### Grade 5 → 6 Transition

**BEFORE:**
```
G5.04 (conceptual: fairness)
    → G5.05 (conceptual: identify detection data)
    → [HUGE GAP] ❌
    → G6.01.01 (hands-on: speech API)
```

**AFTER:**
```
G5.04 (conceptual: fairness)
    → G5.05 (conceptual: identify data) [ENHANCED: sorting cards activity]
    → ⭐ G5.06 (workflow: start→read→process→stop) [NEW] ✅
    → G6.01.01 (hands-on: speech API) [ENHANCED: timing, issues]
```

---

### Multimodal Input Learning Path

**BEFORE:**
```
G7.00A (choose modality)
    → G7.01 (gesture dictionary)
    → [GAP] ❌
    → G7.02 (AND confirmation with state management)
```

**AFTER:**
```
G7.00A (choose modality)
    → G7.01 (gesture dictionary)
    → ⭐ G7.01B (OR logic - simple multimodal) [NEW] ✅
    → G7.02 (AND confirmation with state)
```

---

### KNN Machine Learning Path

**BEFORE:**
```
G8.00A (theory: supervised learning)
    → [GAP] ❌
    → G8.02 (full system: UI + collection + training + prediction)
```

**AFTER:**
```
G8.00A (theory: supervised learning)
    → ⭐ G8.01A (practice: simple dataset, just train/predict) [NEW] ✅
    → G8.02 (full system: UI + collection + training)
```

---

## TECHNICAL ENHANCEMENTS

### Hand Detection Table (G6.04.02)

**BEFORE:**
```
"read curl angles for each finger"
```

**AFTER:**
```
"The table contains 47 rows per detected hand:
 - First 5 rows: finger summaries (thumb, index, middle, ring, pinky)
   Columns: [hand, part, curl, dir, x, y, z]
 - Next 21 rows: 2D landmark positions
 - Last 21 rows: 3D landmark positions

 Curl: 0° (fist) to 180° (straight)
 Direction: 0° to 360° (pointing direction)
 X, Y: screen coordinates
 Z: depth"
```

---

### 2D Body Pose Table (G6.08.01)

**BEFORE:**
```
"detect body landmarks (nose, shoulders, elbows, wrists, hips, knees, ankles)"
```

**AFTER:**
```
"The detection identifies all 17 keypoints:
 nose, left_eye, right_eye, left_ear, right_ear,
 left_shoulder, right_shoulder, left_elbow, right_elbow,
 left_wrist, right_wrist, left_hip, right_hip,
 left_knee, right_knee, left_ankle, right_ankle

 Plus 4 limb measurements:
 left_arm, right_arm, left_leg, right_leg (with curl, dir)

 Table columns: id, part, x, y, curl, dir"
```

---

### Face Detection Table (G6.09.02)

**BEFORE:**
```
"read the face detection table to get face position"
```

**AFTER:**
```
"The table contains 13 rows per detected face:
 - 1 row for tilt angle
 - 12 rows for 6 facial landmarks (x, y each):
   left_eye, right_eye, nose, mouth, left_ear, right_ear

 Table columns: ID, variable, value

 Note: Face data can be noisy, may need smoothing"
```

---

### Speech Recognition (G6.01.01)

**BEFORE:**
```
"capture a single spoken word or phrase and display the result"
```

**AFTER:**
```
"Recognized text stored in VARIABLE (not table)

 Common issues:
 - Silent room → no input detected
 - Background noise → mis-recognition
 - Recognition delay → typically 1-3 seconds after speaking stops

 Display using: `text from speech` reporter + `say` or variable monitor"
```

---

### Text-to-Speech Parameters (G6.02.01)

**BEFORE:**
```
"adjust speed/pitch/volume parameters"
```

**AFTER:**
```
"Parameters:
 - Default: 100
 - Range: 50-200
 - Units: percentage"
```

---

## DEPENDENCY FIXES

### Added Dependencies

```
T23.G6.02 (Map speech to UI)
  OLD: Missing TTS dependency
  NEW: + T23.G6.02.01 (Convert text to speech) ✅

T23.G6.05 (Drive UI with hand)
  OLD: Depends on G6.04.02 (just read data)
  NEW: Depends on G6.04.04 (recognize gestures) ✅

T23.G6.06 (Smooth sensor data)
  OLD: Missing hand detection dependency
  NEW: + T23.G6.04.02 (Read finger curl) ✅

T23.G7.01 (Gesture dictionary)
  OLD: Depends on G6.05 (UI integration)
  NEW: + G6.04.04 (Recognize gestures) ✅

T23.G7.02 (Multimodal AND confirmation)
  OLD: Missing gesture dictionary
  NEW: + T23.G7.01 (Define gesture dictionary) ✅
```

---

## SKILL COUNT BY GRADE

| Grade | Before | After | Added Skills |
|-------|--------|-------|--------------|
| K     | 3      | 3     | - |
| 1     | 3      | 3     | - |
| 2     | 3      | 3     | - |
| 3     | 3      | 3     | - |
| 4     | 3      | 3     | - |
| 5     | 6      | 7     | +1 (G5.06) |
| 6     | 17     | 20    | +3 (G6.04.04, G6.06B, renumber G6.10→G6.08.03) |
| 7     | 7      | 9     | +2 (G7.01B, G7.06B) |
| 8     | 6      | 7     | +1 (G8.01A) |
| **Total** | **51** | **58** | **+7 skills** |

---

## WHAT WASN'T CHANGED

✅ K-2 skills remain picture-based/unplugged
✅ All cross-topic dependencies preserved (T01, T06, T08, T09, T10, T11, T16, T22)
✅ Existing skill IDs unchanged (except G6.10 renumber)
✅ Privacy skill boundaries remain clear (G6.07, G7.05, G8.04)
✅ Ethics content preserved (G5.03, G5.04, G7.04, G7.05, G8.05)

---

## QUICK SEARCH COMMANDS

```bash
# Find all new skills
grep "G5.06\|G6.04.04\|G6.06B\|G7.01B\|G7.06B\|G8.01A" T23_COMPLETE_REWRITE.md

# Verify renumbering
grep "G6.10" T23_COMPLETE_REWRITE.md  # Should NOT appear
grep "G6.08.03" T23_COMPLETE_REWRITE.md  # Should appear

# Count total skills
grep "^ID: T23\." T23_COMPLETE_REWRITE.md | wc -l  # Should be 58

# Check dependency fixes
grep -A 5 "^ID: T23.G6.02$" T23_COMPLETE_REWRITE.md | grep "G6.02.01"
grep -A 5 "^ID: T23.G6.06$" T23_COMPLETE_REWRITE.md | grep "G6.04.02"
```

---

## FILES CREATED

1. **T23_COMPLETE_REWRITE.md** - Complete T23 skills ready to replace lines 13579-14167
2. **T23_REWRITE_SUMMARY.md** - Detailed summary of all changes
3. **T23_VISUAL_CHANGES.md** - This visual reference

---

**Status:** ✅ READY FOR DEPLOYMENT
**Recommendation:** Use T23_COMPLETE_REWRITE.md to replace current T23 section
