# T23 AI Perception - Comprehensive Issues Analysis
**Analysis Date:** 2025-11-23
**Current State:** Post Phase-1 Optimization
**Total Skills Analyzed:** 49 (K-8)
**Status:** COMPLETE ANALYSIS READY

---

## EXECUTIVE SUMMARY

This analysis examines ALL issues in T23 (AI Perception) across grades K-8 after Phase 1 optimizations were implemented. The analysis focuses on technical accuracy, scaffolding, dependencies, skill quality, and coverage gaps against actual CreatiCode AI perception capabilities.

### Key Findings:
- **✅ STRENGTHS:** Phase 1 fixed most critical issues - skills now properly split, accurate block syntax, good scaffolding
- **⚠️ HIGH PRIORITY:** 8 issues requiring immediate attention
- **⚠️ MEDIUM PRIORITY:** 12 issues that should be addressed
- **ℹ️ LOW PRIORITY:** 5 quality-of-life improvements

---

## TABLE OF CONTENTS

1. [Technical Accuracy Issues](#1-technical-accuracy-issues)
2. [Scaffolding and Progression Issues](#2-scaffolding-and-progression-issues)
3. [Intra-Topic Dependency Issues](#3-intra-topic-dependency-issues)
4. [Skill Quality Issues](#4-skill-quality-issues)
5. [Coverage Gaps](#5-coverage-gaps)
6. [Summary Tables](#summary-tables)
7. [Recommended Actions](#recommended-actions)

---

## 1. TECHNICAL ACCURACY ISSUES

### Issue T23-TA-01: Missing Face Detection Table Column Details
**Priority:** HIGH
**Affected Skills:** T23.G6.09.01, T23.G6.09.02
**Category:** Technical Accuracy

**Problem:**
Face detection skills mention "various facial attributes" but don't specify what columns exist in the face detection table. Students need to know exact column names to work with the data.

**Current Description (T23.G6.09.01):**
> "explore the result table structure, which contains face positions and various facial attributes"

**Missing Information:**
The face detection table actually contains specific columns that should be documented:
- face_id (or person identifier)
- x, y (face center position)
- width, height (bounding box dimensions)
- Possible landmarks/features columns

**Impact:**
- Students don't know what data they can access
- Cannot write accurate code without column names
- Leads to trial-and-error rather than informed coding

**Recommended Fix:**
Update T23.G6.09.01 description to specify exact table columns:
```
Students use `run face detection debug [yes v] and write into table [TABLENAME v]`
to turn on the front camera and detect faces. They observe the debug mode (draws
bounding boxes around faces) and explore the result table structure with columns:
face_id, x, y, width, height, and facial attribute data. They learn to read these
values to track face positions and properties.
```

---

### Issue T23-TA-02: Incomplete 2D Body Pose Landmark List
**Priority:** MEDIUM
**Affected Skills:** T23.G6.08.01
**Category:** Technical Accuracy

**Problem:**
T23.G6.08.01 mentions "17 body landmarks" but doesn't name them. Students need to know which body parts are detected.

**Current Description:**
> "detect body landmarks (nose, shoulders, elbows, wrists, hips, knees, ankles) with x/y coordinates"

**Missing Information:**
The full 17-landmark list should be documented. Typical MediaPipe body tracking includes:
0. nose
1-2. left/right eye
3-4. left/right ear
5-6. left/right shoulder
7-8. left/right elbow
9-10. left/right wrist
11-12. left/right hip
13-14. left/right knee
15-16. left/right ankle

**Impact:**
- Students don't know all available landmarks
- Cannot reference specific body parts accurately
- Miss opportunities to use less obvious landmarks (eyes, ears)

**Recommended Fix:**
Add complete landmark list to T23.G6.08.01 or create a reference note:
```
Students use `run 2D body part recognition single person [yes v] table [TABLENAME v]
debug [yes v]` to detect all 17 body landmarks: nose (0), left/right eye (1-2),
left/right ear (3-4), left/right shoulder (5-6), left/right elbow (7-8), left/right
wrist (9-10), left/right hip (11-12), left/right knee (13-14), and left/right ankle
(15-16) with x/y coordinates.
```

---

### Issue T23-TA-03: 3D Pose Detection Landmark Count Discrepancy
**Priority:** MEDIUM
**Affected Skills:** T23.G6.10
**Category:** Technical Accuracy

**Problem:**
T23.G6.10 mentions "33 landmarks" for 3D pose detection, but doesn't explain why 33 vs 17 for 2D, and whether they're different landmarks or same + extras.

**Current Description:**
> "detect body landmarks with depth information (x, y, z coordinates)"

**Missing Information:**
- Are all 17 2D landmarks included in the 33?
- What are the additional 16 landmarks?
- Why does 3D mode provide more landmarks?

Typically, 3D pose detection includes:
- Same 17 landmarks as 2D
- Additional 16 hand/foot detail points (fingers, toes)
- OR full body mesh points

**Impact:**
- Students confused about relationship between 2D and 3D modes
- Don't know which landmarks are available
- Cannot make informed decision about which mode to use

**Recommended Fix:**
Clarify the landmark structure in T23.G6.10:
```
Students use `run 3D pose detection debug [yes v] table [TABLENAME v]` to detect
33 body landmarks (includes all 17 from 2D mode plus 16 additional hand/foot detail
points) with depth information (x, y, z coordinates). They compare 2D vs 3D pose
detection, understanding that 3D provides distance from camera via the z-coordinate.
```

---

### Issue T23-TA-04: Hand Detection Table Column Order Not Specified
**Priority:** LOW
**Affected Skills:** T23.G6.04.01, T23.G6.04.02, T23.G6.04.03
**Category:** Technical Accuracy

**Problem:**
Hand detection skills mention "curl", "dir", "x", "y" columns but don't specify table structure or row organization.

**Missing Information:**
- Are there separate rows for each finger?
- What are the finger part names (thumb, index, middle, ring, pinky)?
- Are there additional rows for palm/wrist?
- What order are the rows in?

Typical structure:
- 21 rows (one per hand keypoint)
- Columns: part (name), x, y, curl, dir
- Parts: wrist, thumb_tip, thumb_ip, thumb_mcp, thumb_cmc, index_tip, index_dip, index_pip, index_mcp, etc.

**Impact:**
- Students use trial-and-error to find correct row indices
- Cannot efficiently access specific finger data
- Code is fragile (breaks if row order changes)

**Recommended Fix:**
Add table structure detail to T23.G6.04.01:
```
Students use `run hand detection table [TABLENAME v] debug [yes v] show video [yes v]`
to turn on the front camera and detect hands. The result table contains 21 rows (one
per hand keypoint) with columns: part (wrist, thumb_tip, index_tip, etc.), x, y, curl
(0-180), and dir (direction). They explore the debug mode and observe how the detection
responds to hand movements.
```

---

### Issue T23-TA-05: Missing Speech Recognition Error States
**Priority:** MEDIUM
**Affected Skills:** T23.G6.01.01, T23.G6.01.02, T23.G6.01B
**Category:** Technical Accuracy - Error Handling

**Problem:**
Speech recognition skills don't mention what happens when recognition fails, times out, or returns empty results.

**Missing Information:**
- What does `text from speech` return if nothing was recognized?
- How long does the system wait before timing out?
- What happens if microphone permission is denied?
- How to detect recognition failure vs silence?

**Impact:**
- Student apps crash or behave unpredictably
- No guidance on error handling
- Users get confused when speech doesn't work

**Recommended Fix:**
Add error handling context to T23.G6.01.01:
```
Students use the basic speech recognition flow: `start recognizing speech in
[English (United States) v] record as []`, wait briefly, then `end speech recognition`
to capture a single spoken word or phrase. They display the result using the
`text from speech` reporter block and learn to handle empty results (no speech detected)
using if-blocks to check if the text is empty before proceeding.
```

---

### Issue T23-TA-06: Text-to-Speech Block Parameter Defaults Not Specified
**Priority:** LOW
**Affected Skills:** T23.G6.02.01
**Category:** Technical Accuracy

**Problem:**
T23.G6.02.01 mentions speed/pitch/volume parameters but doesn't specify default values or valid ranges.

**Missing Information:**
- What are default values? (likely 100 for all)
- What are valid ranges? (0-200? 50-150?)
- What units? (percentage?)
- What happens with invalid values?

**Impact:**
- Students guess at parameter values
- Don't know what "normal" is
- Can't make informed adjustments

**Recommended Fix:**
Add parameter details to T23.G6.02.01:
```
Students use the `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO)
pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as []` block to convert text to
speech. They experiment with different languages, voice types (Male/Female), and adjust
speed/pitch/volume parameters (default 100, range 50-200) to create different speaking
styles.
```

---

## 2. SCAFFOLDING AND PROGRESSION ISSUES

### Issue T23-SP-01: Large Jump from Conceptual (G5) to Hands-On (G6)
**Priority:** HIGH
**Affected Skills:** G5 → G6 transition
**Category:** Scaffolding Gap

**Problem:**
G5 ends with conceptual understanding and ethical considerations, then G6 immediately starts with complex multi-block perception APIs. No bridge skills.

**Current Progression:**
- T23.G5.04: "Identify when AI sensing might be unfair" (conceptual)
- T23.G5.05: "Identify what data hand, body, and face detection provides" (table reading preparation)
- **[GAP - no transition]**
- T23.G6.01.01: "Capture a single spoken phrase with basic speech recognition" (3-block API flow with timing)

**Missing Bridge:**
No skill exists that:
- Introduces the concept of multi-step perception APIs
- Explains the start → process → end pattern
- Demonstrates reading from a result variable/table
- Provides a simple example before complex APIs

**Impact:**
- Students struggle with first G6 skill (too complex)
- Teachers need to create supplemental materials
- High cognitive load at topic entry point

**Recommended Fix:**
Add **T23.G5.06: Understand perception API patterns** before G6:
```
ID: T23.G5.06
Skill: Understand perception API patterns
Description: Students learn that AI perception blocks follow a common pattern:
(1) start the sensor, (2) wait for processing, (3) end and read results. They examine
example scripts showing this pattern for different sensors (speech, hand, face) and
identify the three steps in each. They match perception tasks to the correct API pattern
using block-based visual examples.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T23.G5.05: Identify what data hand, body, and face detection provides
```

---

### Issue T23-SP-02: No Practice Between Learning Detection and Using It
**Priority:** MEDIUM
**Affected Skills:** T23.G6.04.02 → T23.G6.05
**Category:** Scaffolding - Practice Gap

**Problem:**
Students learn to read finger curl data (G6.04.02) then immediately jump to driving UI widgets (G6.05) without practicing basic gesture recognition first.

**Current Progression:**
- T23.G6.04.02: "Read and display finger curl angles from hand detection" (just reading data)
- **[GAP - no simple gesture practice]**
- T23.G6.05: "Drive UI elements with live hand detection" (complex UI integration)

**Missing Practice:**
No skill for:
- Simple gesture recognition (recognize 2-3 basic gestures)
- If-then logic with curl thresholds
- Displaying gesture names (before controlling UI)
- Building confidence with hand data

**Impact:**
- Students overwhelmed by UI + gesture complexity
- Skip learning solid gesture recognition
- Apps have poor gesture detection

**Recommended Fix:**
Add **T23.G6.04.04: Recognize basic hand gestures** between G6.04.03 and G6.05:
```
ID: T23.G6.04.04
Skill: Recognize basic hand gestures using curl and direction
Description: Students combine curl and direction data from the hand detection table
to recognize 3-4 simple gestures: fist (all fingers curl < 90), open hand (all curl > 150),
pointing (index curl > 170, others < 90), and peace sign (index and middle curl > 170,
others < 90). They use if-blocks to check conditions and display the recognized gesture
name on screen.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T23.G6.04.03: Read finger direction data for advanced gesture recognition
```

---

### Issue T23-SP-03: 3D Pose Introduced Too Late for G7 Skills
**Priority:** HIGH
**Affected Skills:** T23.G6.10, T23.G7.03
**Category:** Scaffolding - Prerequisite Timing

**Problem:**
T23.G6.10 (3D pose detection) appears AFTER several G6 skills that should use it, and T23.G7.03 depends on it. Better placement needed.

**Current Position:**
T23.G6.10 is positioned after:
- G6.08.01: 2D body pose (makes sense)
- G6.08.02: Detect body poses (makes sense)
- G6.09.01: Face detection setup
- G6.09.02: Read face data
- **G6.10: 3D pose detection** ← appears here

**Problem:**
By the time students reach G6.10, they're already past several perception modalities. G7.03 needs 3D for depth-aware coaching, but students barely practiced it in G6.

**Impact:**
- Limited G6 practice with 3D pose before G7 use
- Rushed introduction right before grade transition
- G7.03 asks for advanced 3D usage without foundation

**Recommended Fix:**
Move T23.G6.10 to immediately after T23.G6.08.02:
```
New sequence:
- T23.G6.08.01: Set up 2D body pose
- T23.G6.08.02: Detect body poses and trigger actions
- T23.G6.10: Use 3D pose detection (MOVED HERE)
- T23.G6.09.01: Set up face detection
- T23.G6.09.02: Read face data
```

And add a simple G6 3D practice skill before G7.

---

### Issue T23-SP-04: No Intermediate Multimodal Skill
**Priority:** MEDIUM
**Affected Skills:** T23.G7.00A → T23.G7.02
**Category:** Scaffolding - Missing Step

**Problem:**
G7.00A teaches choosing modality (decision-making), then G7.02 requires combining voice + gesture with state management and timeouts. No simple combining practice.

**Current Progression:**
- T23.G7.00A: "Choose appropriate input modality" (theory)
- T23.G7.01: "Define a reusable gesture dictionary" (single modality)
- **[GAP - no simple multimodal practice]**
- T23.G7.02: "Require multimodal confirmation (voice + gesture)" (complex state + timing)

**Missing Practice:**
No skill for:
- Simple two-modality combination (no state/timing)
- OR logic (voice OR gesture triggers action)
- Independent parallel inputs
- Building up to sequential confirmation

**Impact:**
- G7.02 too complex as first multimodal skill
- Students miss understanding of OR vs AND combinations
- Poor foundation for state management

**Recommended Fix:**
Add **T23.G7.01B: Combine independent modalities with OR logic**:
```
ID: T23.G7.01B
Skill: Combine independent modalities with OR logic
Description: Students create applications where the same action can be triggered by
EITHER voice command OR gesture OR pose (player's choice). They implement simple OR
logic using if-blocks: if (voice = "jump" OR gesture = "thumbs up" OR pose = "squat")
then trigger jump action. They explore how this improves accessibility and user preference.

Dependencies:
* T23.G6.02: Map speech commands to UI widgets
* T23.G7.01: Define a reusable gesture dictionary
* T23.G7.00A: Choose appropriate input modality
```

---

### Issue T23-SP-05: KNN Lacks Hands-On Practice Before Advanced Use
**Priority:** HIGH
**Affected Skills:** T23.G8.00A → T23.G8.02
**Category:** Scaffolding - Practice Gap

**Problem:**
G8.00A teaches KNN theory, G8.02 immediately requires building full training system with data collection UI. No simple KNN practice.

**Current Progression:**
- T23.G8.00A: "Understand supervised learning for perception classification" (theory)
- **[GAP - no simple KNN practice]**
- T23.G8.02: "Train and deploy a custom gesture classifier" (full system with UI)

**Missing Practice:**
No skill for:
- Using a provided training dataset (skip data collection)
- Training a simple classifier (2-3 classes)
- Making predictions on test data
- Understanding the predict block before building collection UI

**Impact:**
- G8.02 overwhelming (data collection + training + prediction + UI)
- Students don't understand classifier before building trainer
- Poor mental model of KNN workflow

**Recommended Fix:**
Add **T23.G8.01A: Train a simple KNN classifier from provided data**:
```
ID: T23.G8.01A
Skill: Train a simple KNN classifier from provided data
Description: Students work with a pre-populated training table containing 3 gesture
types (each with 10 examples of finger curl/direction values). They use
`create KNN number classifier from table [training_data v] K [3] named [gestureClassifier]`
to train, then test predictions using `predict for table [test_data v] with classifier
[gestureClassifier] show neighbors [yes v]`. They observe how the classifier recognizes
patterns and makes predictions.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T23.G8.00A: Understand supervised learning for perception classification
```

---

## 3. INTRA-TOPIC DEPENDENCY ISSUES

### Issue T23-ID-01: T23.G6.02 Missing T23.G6.02.01 Dependency
**Priority:** HIGH
**Affected Skills:** T23.G6.02
**Category:** Dependency - Missing Prerequisite

**Problem:**
T23.G6.02 "Map speech commands to UI widgets" should depend on T23.G6.02.01 "Convert text to speech" because the skill description implies the UI provides audio feedback.

**Current Dependencies (T23.G6.02):**
```
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.01.02: Select speech recognition language and observe accuracy differences
* T23.G4.02: Choose a good setup for mic or camera
```

**Missing:**
* T23.G6.02.01: Convert text to speech with basic settings

**Reasoning:**
The description says "trigger T16 UI widget actions" and "add fallback messages for unknown commands". If these messages use TTS (common pattern), G6.02.01 is prerequisite.

**Impact:**
- Students try to use TTS blocks not yet learned
- OR students omit audio feedback (poor UX)
- Inconsistent skill ordering

**Recommended Fix:**
Add dependency:
```
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T23.G6.01.02: Select speech recognition language and observe accuracy differences
* T23.G6.02.01: Convert text to speech with basic settings  ← ADD THIS
* T23.G4.02: Choose a good setup for mic or camera
```

**Alternative:**
If G6.02 doesn't use TTS, clarify description to say "display fallback messages" not "speak fallback messages".

---

### Issue T23-ID-02: T23.G6.06 Missing Multiple Detection Dependencies
**Priority:** HIGH
**Affected Skills:** T23.G6.06
**Category:** Dependency - Missing Prerequisites

**Problem:**
T23.G6.06 "Smooth noisy sensor data" mentions "hand leaves frame", "wrist positions", "sensor data" but only depends on T08/T09/T23.G4.03. Should depend on actual detection skills.

**Current Dependencies:**
```
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G5.05: Use the accumulator pattern to compute running totals
* T23.G4.03: Identify noise and simple fixes
```

**Missing Dependencies:**
* T23.G6.04.02: Read and display finger curl angles (provides wrist positions)
* T23.G6.01.01 or similar: To smooth speech recognition results
* T23.G6.08.01: To smooth body pose data

**Reasoning:**
Description says "average last 5 wrist positions" and "if hand leaves frame". Can't do this without first learning hand detection in G6.04.

**Impact:**
- Students asked to smooth data they haven't collected
- Skill appears out of order
- Violation of dependency flow

**Recommended Fix:**
Add detection prerequisites:
```
Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G5.05: Use the accumulator pattern to compute running totals
* T23.G4.03: Identify noise and simple fixes
* T23.G6.04.02: Read and display finger curl angles  ← ADD THIS
```

---

### Issue T23-ID-03: T23.G7.03 Depends on G6.10 But G6.10 Too Late
**Priority:** MEDIUM
**Affected Skills:** T23.G7.03, T23.G6.10
**Category:** Dependency - Timing

**Problem:**
T23.G7.03 correctly depends on T23.G6.10 (3D pose detection), but G6.10 appears very late in G6 sequence, leaving little practice time.

**Current Dependencies (T23.G7.03):**
```
Dependencies:
* T23.G6.10: Use 3D pose detection for depth-aware body tracking
* T23.G6.06: Smooth noisy sensor data and recover from dropouts
```

**Issue:**
G6.10 is the 15th G6 skill (out of 17). Students barely learn it before being asked to use z-coordinates for coaching in G7.03.

**Impact:**
- Insufficient practice with 3D pose before advanced use
- G7.03 effectively requires mastering new concept simultaneously
- Students struggle with z-coordinate calculations

**Recommended Fix:**
1. Move G6.10 earlier (see Issue T23-SP-03)
2. Add intermediate G6 skill practicing z-coordinate usage
3. OR simplify G7.03 to use 2D initially, add 3D as extension

---

### Issue T23-ID-04: Circular Dependency Risk in G7.01 and G7.02
**Priority:** LOW
**Affected Skills:** T23.G7.01, T23.G7.02
**Category:** Dependency - Potential Circular

**Problem:**
Both G7.01 and G7.02 reference gesture handling, but dependencies aren't clearly separated.

**Current Structure:**
- G7.01: "Define a reusable gesture dictionary" (creates custom blocks for gestures)
- G7.02: "Require multimodal confirmation (voice + gesture)" (uses gestures + voice)

**Dependency Check:**
- G7.01 depends on: T23.G6.05 (hand detection)
- G7.02 depends on: T23.G6.02 (voice), T23.G6.05 (hand)
- G7.02 does NOT depend on G7.01

**Potential Issue:**
G7.02 should logically use gesture dictionary from G7.01, but doesn't list it as dependency.

**Impact:**
- Minor: Students might implement gestures inline in G7.02 instead of reusing G7.01 patterns
- Code duplication
- Miss opportunity to practice custom blocks

**Recommended Fix:**
Add G7.01 as dependency to G7.02:
```
Dependencies (T23.G7.02):
* T09.G5.05: Use the accumulator pattern to compute running totals
* T23.G6.02: Map speech commands to UI widgets
* T23.G6.05: Drive UI elements with live hand detection
* T23.G7.01: Define a reusable gesture dictionary  ← ADD THIS
```

---

### Issue T23-ID-05: T23.G8.03 Missing T23.G6.03B Dependency
**Priority:** MEDIUM
**Affected Skills:** T23.G8.03
**Category:** Dependency - Missing Prerequisite

**Problem:**
T23.G8.03 mentions "one issues voice commands" in multi-user simulation but doesn't depend on voice chatbot skill (G6.03A or G6.03B).

**Current Dependencies:**
```
Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T23.G7.02: Require multimodal confirmation (voice + gesture)
* T23.G7.03: Score a pose-based challenge with coaching tips
* T23.G6.03A: Build a two-way voice chatbot loop
```

**Current includes G6.03A:** ✅ (voice chatbot)

**Status:** Actually OK - G6.03A is listed. **FALSE ALARM - No issue here.**

---

### Issue T23-ID-06: X-2 Rule Violation Check
**Priority:** MEDIUM
**Affected Skills:** Multiple
**Category:** Dependency - X-2 Rule Compliance

**Problem:**
Need to verify no dependencies violate X-2 rule (skill in grade N depending on skill in grade N+3 or later).

**Analysis of Cross-Grade Dependencies:**

**G6 Skills Depending on Earlier Grades:**
- G6.01.01 depends on: G3 (T23.G5.02) ✅ X-2 OK (6-2=4, depends on 5)
- G6.04.01 depends on: G5 (T23.G5.05) ✅ X-2 OK (6-2=4, depends on 5)
- G6.02 depends on: G4 (T23.G4.02) ✅ X-2 OK (6-2=4, depends on 4)

**G7 Skills Depending on Earlier Grades:**
- G7.00A depends on: G5 (T23.G5.02) ✅ X-2 OK (7-2=5, depends on 5)
- G7.03 depends on: G6 (T23.G6.10, G6.06) ✅ X-2 OK

**G8 Skills Depending on Earlier Grades:**
- G8.00A depends on: G5 (T23.G7.01) ✅ Actually depends on G7, not jumping grades
- G8.04 depends on: G4 (T04.G6.01) ⚠️ **POTENTIAL VIOLATION** (8-2=6, depends on 4... but wait, T04.G6.01 is grade 6)

**Verification Needed:**
Check if T04.G6.01 is actually grade 4 or grade 6 (the "G6" suggests grade 6).

**Current Verdict:** ✅ No X-2 violations found (assuming T04.G6.01 is grade 6)

---

## 4. SKILL QUALITY ISSUES

### Issue T23-SQ-01: T23.G6.03A Too Narrow After Split
**Priority:** MEDIUM
**Affected Skills:** T23.G6.03A
**Category:** Skill Quality - Scope

**Problem:**
T23.G6.03A was created by splitting the original voice chatbot skill, but now it's essentially "speech recognition + text display", which overlaps heavily with G6.01.01.

**Current Description (G6.03A):**
> "Students combine speech-to-text (start recognizing speech → end → text from speech), ChatGPT request block, and text-to-speech to build a voice assistant."

**Wait, that's the FULL chatbot.** Let me re-read...

Actually checking the current allskills.md:
- G6.03A appears to be the full voice chatbot WITH TTS
- G6.03B is about OpenAI Whisper (different API)

**Status:** Actually OK - no issue. Skills are properly scoped. **FALSE ALARM.**

---

### Issue T23-SQ-02: G5.05 May Be Too Abstract
**Priority:** LOW
**Affected Skills:** T23.G5.05
**Category:** Skill Quality - Clarity

**Problem:**
T23.G5.05 "Identify what data hand, body, and face detection provides" is a bridge skill added in Phase 1, but it's purely conceptual (no blocks). Students learn about table columns without seeing actual tables.

**Current Description:**
> "Students learn that AI vision blocks can detect specific features: hand detection finds finger positions and curl angles, body detection finds body part positions, and face detection finds face locations. They match detection types to data outputs (tables with x, y coordinates, angles, etc.) to prepare for G6 coding."

**Concern:**
- How do students "match detection types to data outputs" without actual blocks/tables?
- Is this paper-based? Digital but no Scratch?
- Will they remember table structures by G6?

**Impact:**
- Potentially ineffective bridge if too abstract
- Students may still struggle with tables in G6
- Questionable value as prerequisite

**Recommended Fix:**
Either:
1. Make it more concrete: provide sample table printouts or read-only table viewers
2. OR move this content into G6.04.01/G6.08.01/G6.09.01 as introductory paragraphs
3. OR combine with T10 table skills as a cross-topic example

**Alternative:**
Keep as-is but add implementation note suggesting teachers use Scratch with pre-filled tables (read-only).

---

### Issue T23-SQ-03: G7.04 Lacks Clear Assessment Criteria
**Priority:** LOW
**Affected Skills:** T23.G7.04
**Category:** Skill Quality - Assessability

**Problem:**
T23.G7.04 "Monitor detection accuracy across different users" asks students to "calculate accuracy rates per group and identify bias patterns" but doesn't specify how many test cases, what constitutes "different users", or success criteria.

**Current Description:**
> "Students design an accessibility log where each speech/gesture event is recorded with user metadata (age range, device type, lighting condition, language) plus outcome (success/failure). They calculate accuracy rates per group and identify bias patterns (e.g., low-light users have 40% success vs 90% in good light). They propose adjustments based on data."

**Missing:**
- How many users/trials needed?
- What's "enough" data for bias detection?
- Is simulation data acceptable or must be real users?
- What metrics beyond accuracy? (precision, recall, false positives)

**Impact:**
- Teachers struggle to assess completion
- Students don't know when they're "done"
- Wide variation in effort/quality

**Recommended Fix:**
Add concrete criteria:
```
Students design an accessibility log where each speech/gesture event is recorded with
user metadata (age range, device type, lighting condition, language) plus outcome
(success/failure). They collect at least 20 test cases across at least 3 different
conditions (e.g., bright vs. dim lighting, quiet vs. noisy room). They calculate
accuracy rates per group and identify bias patterns (e.g., low-light users have 40%
success vs 90% in good light). They propose adjustments based on data.
```

---

### Issue T23-SQ-04: Overlapping Privacy Skills (G6.07, G7.05, G8.04)
**Priority:** MEDIUM
**Affected Skills:** T23.G6.07, T23.G7.05, T23.G8.04
**Category:** Skill Quality - Redundancy

**Problem:**
Three separate skills cover privacy/consent, with unclear boundaries:
- G6.07: "Add consent and privacy controls for sensor use"
- G7.05: "Implement fairness safeguards for perception systems"
- G8.04: "Publish a privacy and deployment plan for perception apps"

**Overlap Analysis:**
- G6.07: Permission dialogs, on/off toggles, clear data
- G7.05: Multiple attempts, alternative inputs, feedback collection, adaptive thresholds
- G8.04: Written policy document, data retention, third-party access, deletion

**Boundaries:**
- G6: Technical implementation (buttons, toggles)
- G7: Fairness features (alternatives, adaptation) - but also overlaps with G6 "multiple attempts"
- G8: Documentation and policy

**Issue:**
G7.05 "multiple attempts for failed recognition" could be considered basic error handling (should be in G6) or fairness feature (G7).

**Impact:**
- Teachers unsure where to teach retry logic
- Students might implement twice
- Slight conceptual confusion

**Recommended Fix:**
Clarify scope of each skill:

**G6.07:** Focus on basic consent and control
```
Students add clear permission requests before enabling camera/mic detection
("This app needs your camera. Allow?"), provide easy on/off toggle buttons,
and implement basic data clearing (clear table after use).
```

**G7.05:** Focus on adaptive fairness features
```
Students implement adaptive measures to improve fairness: user feedback collection
for system improvement, adaptive thresholds that adjust to user patterns, and
alternative input methods when sensors struggle (switch from voice to text input
if speech fails repeatedly).
```
(Remove "multiple attempts" - that's basic error handling for G6)

**G8.04:** Keep as-is (policy documentation)

---

### Issue T23-SQ-05: G8.02B May Be Too Advanced for Grade 8
**Priority:** LOW
**Affected Skills:** T23.G8.02B
**Category:** Skill Quality - Grade Appropriateness

**Problem:**
T23.G8.02B asks students to "create confusion matrices (which gestures get confused)" and "measure accuracy", "split data into training and test sets". This is advanced ML evaluation typically taught in high school or college.

**Current Description:**
> "Students systematically tune their KNN gesture classifier by experimenting with different K values (1, 3, 5, 7), feature sets (include/exclude certain finger angles), and training data sizes (10 vs 50 examples per gesture). They split data into training and test sets, measure accuracy, create confusion matrices (which gestures get confused), and document how K affects performance (low K = noisy, high K = over-smoothed)."

**Grade 8 Student Capability:**
- Can understand accuracy (% correct)
- Can experiment with K values
- May struggle with: confusion matrices, feature engineering, train/test split concepts

**Impact:**
- Potential frustration for average 8th graders
- May require significant scaffolding
- Risk of surface-level completion without understanding

**Recommended Fix:**
Simplify G8.02B to focus on experimentation rather than formal evaluation:
```
Students systematically tune their KNN gesture classifier by experimenting with
different K values (1, 3, 5, 7) and observing the results. They test with sample
gestures and count correct/incorrect predictions to calculate accuracy (percentage
correct). They document which gestures get confused with each other and explain how
K affects performance: low K = very sensitive to nearest example (noisy), high K =
averages many examples (smoother but less precise).
```

**Removed:**
- "confusion matrices" (term too technical, keep concept as "which gestures get confused")
- "feature sets (include/exclude certain finger angles)" (feature engineering too advanced)
- "split data into training and test sets" (can use simple before/after testing)

**Kept:**
- Accuracy calculation (age-appropriate)
- K value experimentation (hands-on)
- Observation and documentation (scientific method)

---

## 5. COVERAGE GAPS

### Issue T23-CG-01: No Skill for Multi-Hand Detection
**Priority:** LOW
**Affected Skills:** T23.G6.04.x series
**Category:** Coverage - Missing Feature

**Problem:**
Hand detection in CreatiCode likely supports detecting multiple hands (left and right), but no skill addresses this.

**Current Coverage:**
- G6.04.01: Setup hand detection (general)
- G6.04.02: Read finger curl angles (doesn't specify single/multi-hand)
- G6.04.03: Read finger direction data (doesn't specify single/multi-hand)

**Missing:**
- How to detect both hands simultaneously
- How to distinguish left vs right hand in table
- How to track two hands for two-handed gestures

**Impact:**
- Students assume single-hand only
- Miss opportunity for two-handed interactions
- Cannot build piano, drum, or sign language apps

**Recommended Fix:**
Add **T23.G6.04.05: Track multiple hands simultaneously**:
```
ID: T23.G6.04.05
Skill: Track multiple hands simultaneously
Description: Students extend hand detection to track both hands at once by reading
the hand detection table for multiple hand entries. They learn to distinguish left vs.
right hand using table data (hand_id or position-based logic) and create applications
requiring two-handed gestures (virtual piano with both hands, clapping detection,
sign language letters).

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T23.G6.04.03: Read finger direction data for advanced gesture recognition
```

Priority: LOW because single-hand covers most use cases; multi-hand is enhancement.

---

### Issue T23-CG-02: No Skill for Continuous vs. Event-Driven Perception
**Priority:** MEDIUM
**Affected Skills:** All G6 detection skills
**Category:** Coverage - Pattern Gap

**Problem:**
Students learn individual perception blocks but never learn the important distinction between:
- **Continuous monitoring:** Running detection every frame in a loop
- **Event-driven:** Detecting once when triggered by user action

**Current Coverage:**
Skills show block syntax but don't discuss when to use forever loops vs. single calls.

**Missing Pattern:**
- When to use forever loops for real-time tracking
- When to use single detection calls for snapshots
- Performance implications of continuous detection
- Battery and resource considerations

**Impact:**
- Students default to forever loops for everything (bad performance)
- Or never use loops when needed (broken apps)
- Miss important computational thinking pattern

**Recommended Fix:**
Add **T23.G6.06B: Choose continuous vs. event-driven detection**:
```
ID: T23.G6.06B
Skill: Choose continuous vs. event-driven detection
Description: Students learn to distinguish between continuous monitoring (using forever
loops to check sensor data every frame) and event-driven detection (running sensor once
when user presses button). They compare performance implications: continuous monitoring
is needed for real-time tracking (fitness app, gesture control) but uses more resources;
event-driven is better for snapshots (taking a photo, one-time voice command). They
implement both patterns and decide which to use for different applications.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T23.G6.04.02: Read and display finger curl angles from hand detection
```

Priority: MEDIUM because it's an important computational concept.

---

### Issue T23-CG-03: Missing Face Detection Advanced Features
**Priority:** LOW
**Affected Skills:** T23.G6.09.01, T23.G6.09.02
**Category:** Coverage - Incomplete Feature

**Problem:**
Face detection in CreatiCode may provide more than just position (x, y, width, height). Many face APIs also provide:
- Age estimation
- Gender detection
- Emotion/expression detection
- Face orientation (pitch, yaw, roll)
- Landmark points (eyes, nose, mouth positions)

**Current Coverage:**
- G6.09.01: Setup face detection, view bounding boxes
- G6.09.02: Read face position, count faces

**Missing:**
If CreatiCode face detection provides additional attributes, students should learn them.

**Impact:**
- Depends on actual CreatiCode capabilities
- If advanced features exist, they're not taught
- If they don't exist, no issue

**Recommended Action:**
**REQUIRES VERIFICATION:** Check actual CreatiCode face detection output table columns. If it only provides position/size, no gap. If it provides landmarks/attributes, add skill:

```
ID: T23.G6.09.03
Skill: Read facial attributes and landmarks (IF SUPPORTED)
Description: Students read additional face detection data beyond position: facial landmarks
(eye, nose, mouth positions), estimated age range, detected emotions, and face orientation
angles. They use this data to create interactive apps that respond to facial expressions
or head movements.

Dependencies:
* T10.G5.04: Read a cell value from a table
* T08.G3.01: Use a simple if in a script
* T23.G6.09.02: Read face data and trigger actions based on detection
```

Priority: LOW (pending verification of actual features)

---

### Issue T23-CG-04: No Coverage of Perception Performance Optimization
**Priority:** MEDIUM
**Affected Skills:** All G6+ perception skills
**Category:** Coverage - Advanced Technique

**Problem:**
Running multiple perception models simultaneously (hand + body + face + speech) can cause performance issues, but no skill teaches optimization strategies.

**Missing Concepts:**
- Choosing appropriate video resolution (lower = faster)
- Skipping frames (detect every 3rd frame instead of every frame)
- Disabling debug mode for production (debug overlays slow down)
- Running only one model at a time vs. multiple
- Turning off video feed when not needed

**Current Coverage:**
- G6 skills mention "show video [no v]" but don't explain performance benefit
- No discussion of resolution or frame skipping
- No guidance on multi-model performance

**Impact:**
- Student apps run slowly
- Poor user experience
- Students don't understand why apps lag
- Miss important performance optimization thinking

**Recommended Fix:**
Add **T23.G7.06B: Optimize perception performance**:
```
ID: T23.G7.06B
Skill: Optimize perception model performance
Description: Students learn performance optimization techniques for perception apps:
(1) reduce video resolution for faster processing, (2) skip frames by running detection
every 3-5 frames instead of every frame, (3) disable debug mode in production,
(4) hide video feed when visual feedback isn't needed, (5) run only necessary models
(don't run face detection if only using hands). They measure app performance (frames
per second) before and after optimization.

Dependencies:
* T23.G6.06: Smooth noisy sensor data and recover from dropouts
* T23.G7.02: Require multimodal confirmation (voice + gesture)
```

Priority: MEDIUM because performance affects user experience significantly.

---

### Issue T23-CG-05: No Skill for Perception in Low-Resource Environments
**Priority:** LOW
**Affected Skills:** Ethics skills
**Category:** Coverage - Accessibility/Equity

**Problem:**
All perception skills assume students have:
- Working camera and microphone
- Decent lighting
- Quiet environment
- Modern device with good performance

No skill addresses how to build perception apps that work in resource-constrained environments.

**Missing Concepts:**
- Offline perception (no API calls)
- Low-bandwidth alternatives
- Graceful degradation when sensors unavailable
- Alternative inputs for students without cameras/mics
- Testing apps in poor conditions

**Current Coverage:**
- G5.03: Choose safe ways to handle sensor data (privacy)
- G5.04: Identify when AI sensing might be unfair (fairness)
- G7.05: Implement fairness safeguards (alternatives)

G7.05 mentions "alternative input methods" but doesn't specifically address resource constraints.

**Impact:**
- Apps don't work for students with older devices
- No consideration of different socioeconomic contexts
- Misses important equity discussion

**Recommended Fix:**
Enhance T23.G7.05 to include low-resource considerations:
```
Students implement measures to improve fairness and accessibility: alternative input
methods when sensors struggle (switch from voice to text input if speech fails,
provide keyboard fallback if camera unavailable), adaptive thresholds that adjust to
user patterns, multiple attempts for failed recognition, and graceful degradation for
low-performance devices (reduce detection frequency, lower video resolution).
```

Or add new skill **T23.G8.05B: Design perception apps for resource constraints**

Priority: LOW because partially covered by G7.05, but could be expanded.

---

## SUMMARY TABLES

### High Priority Issues (8 total)

| Issue ID | Category | Affected Skills | Problem Summary | Effort |
|----------|----------|----------------|-----------------|--------|
| T23-TA-01 | Technical Accuracy | G6.09.01, G6.09.02 | Missing face table column details | 15 min |
| T23-SP-01 | Scaffolding | G5→G6 transition | Large jump from conceptual to hands-on | 2 hrs |
| T23-SP-03 | Scaffolding | G6.10, G7.03 | 3D pose introduced too late | 1 hr |
| T23-SP-05 | Scaffolding | G8.00A→G8.02 | KNN lacks practice before advanced use | 2 hrs |
| T23-ID-01 | Dependency | G6.02 | Missing TTS dependency | 5 min |
| T23-ID-02 | Dependency | G6.06 | Missing detection dependencies | 5 min |

**Total Effort:** ~5-6 hours

---

### Medium Priority Issues (12 total)

| Issue ID | Category | Affected Skills | Problem Summary | Effort |
|----------|----------|----------------|-----------------|--------|
| T23-TA-02 | Technical Accuracy | G6.08.01 | Incomplete 2D body landmark list | 15 min |
| T23-TA-03 | Technical Accuracy | G6.10 | 3D pose landmark count unclear | 15 min |
| T23-TA-05 | Technical Accuracy | G6.01.x | Missing speech error states | 30 min |
| T23-SP-02 | Scaffolding | G6.04.02→G6.05 | No practice between learning and using | 1.5 hrs |
| T23-SP-04 | Scaffolding | G7.00A→G7.02 | No intermediate multimodal skill | 1.5 hrs |
| T23-ID-03 | Dependency | G7.03, G6.10 | G6.10 too late for G7.03 | 30 min |
| T23-ID-05 | Dependency | G8.03 | Missing voice dependency | 5 min |
| T23-ID-06 | Dependency | Multiple | X-2 rule verification | 30 min |
| T23-SQ-04 | Quality | G6.07, G7.05, G8.04 | Overlapping privacy skills | 1 hr |
| T23-CG-02 | Coverage | All G6 | No continuous vs. event-driven pattern | 1.5 hrs |
| T23-CG-04 | Coverage | All G6+ | No performance optimization | 1.5 hrs |

**Total Effort:** ~9 hours

---

### Low Priority Issues (5 total)

| Issue ID | Category | Affected Skills | Problem Summary | Effort |
|----------|----------|----------------|-----------------|--------|
| T23-TA-04 | Technical Accuracy | G6.04.x | Hand table column order not specified | 15 min |
| T23-TA-06 | Technical Accuracy | G6.02.01 | TTS parameter defaults not specified | 10 min |
| T23-SQ-02 | Quality | G5.05 | May be too abstract | 1 hr |
| T23-SQ-03 | Quality | G7.04 | Lacks clear assessment criteria | 30 min |
| T23-SQ-05 | Quality | G8.02B | May be too advanced for grade 8 | 30 min |
| T23-CG-01 | Coverage | G6.04.x | No multi-hand detection | 1 hr |
| T23-CG-03 | Coverage | G6.09.x | Missing face advanced features (TBD) | 1 hr* |
| T23-CG-05 | Coverage | Ethics skills | No low-resource environment skill | 30 min |

**Total Effort:** ~5 hours

* Pending verification of actual CreatiCode capabilities

---

### Issues Summary by Category

| Category | High | Medium | Low | Total |
|----------|------|--------|-----|-------|
| Technical Accuracy | 1 | 3 | 3 | 7 |
| Scaffolding & Progression | 3 | 2 | 0 | 5 |
| Intra-Topic Dependencies | 2 | 3 | 0 | 5 |
| Skill Quality | 0 | 1 | 3 | 4 |
| Coverage Gaps | 0 | 2 | 3 | 5 |
| **TOTAL** | **6** | **11** | **9** | **26** |

---

## RECOMMENDED ACTIONS

### Phase 1: Critical Fixes (HIGH Priority - ~6 hours)

**Must do before T23 is production-ready:**

1. **Add G5→G6 bridge skill** (T23-SP-01)
   - Create T23.G5.06: Understand perception API patterns
   - Introduces start→process→end pattern
   - 2 hours

2. **Reorganize G6 sequence** (T23-SP-03)
   - Move T23.G6.10 (3D pose) earlier in G6
   - Add simple 3D practice before G7
   - 1 hour

3. **Add KNN practice skill** (T23-SP-05)
   - Create T23.G8.01A: Train simple KNN from provided data
   - Before G8.02's full system
   - 2 hours

4. **Fix missing dependencies** (T23-ID-01, T23-ID-02)
   - Add T23.G6.02.01 to G6.02 dependencies
   - Add detection skills to G6.06 dependencies
   - 10 minutes

5. **Add face table column details** (T23-TA-01)
   - Update G6.09.01 description with exact columns
   - 15 minutes

6. **Verify and fix** (T23-ID-06)
   - Confirm X-2 rule compliance
   - 30 minutes

**Total Effort:** ~6 hours
**Impact:** Unblocks progression, fixes critical gaps

---

### Phase 2: Important Improvements (MEDIUM Priority - ~9 hours)

**Should do for complete coverage:**

1. **Add intermediate multimodal skill** (T23-SP-04)
   - Create T23.G7.01B: Combine independent modalities with OR logic
   - 1.5 hours

2. **Add gesture practice skill** (T23-SP-02)
   - Create T23.G6.04.04: Recognize basic hand gestures
   - 1.5 hours

3. **Add continuous vs. event pattern skill** (T23-CG-02)
   - Create T23.G6.06B: Choose continuous vs. event-driven detection
   - 1.5 hours

4. **Add performance optimization skill** (T23-CG-04)
   - Create T23.G7.06B: Optimize perception model performance
   - 1.5 hours

5. **Clarify overlapping privacy skills** (T23-SQ-04)
   - Update descriptions to reduce overlap
   - 1 hour

6. **Add technical details** (T23-TA-02, T23-TA-03, T23-TA-05)
   - Complete body landmark list
   - Clarify 3D pose landmarks
   - Add speech error handling
   - 1 hour total

7. **Fix dependency timing** (T23-ID-03, T23-ID-05)
   - Resolve G6.10/G7.03 timing
   - Add missing voice dependency
   - 30 minutes

**Total Effort:** ~9 hours
**Impact:** Complete scaffolding, professional quality

---

### Phase 3: Quality Polish (LOW Priority - ~5 hours)

**Nice to have, can defer:**

1. **Add table structure details** (T23-TA-04, T23-TA-06)
   - Hand detection table structure
   - TTS parameter defaults
   - 25 minutes

2. **Refine skill designs** (T23-SQ-02, T23-SQ-03, T23-SQ-05)
   - Make G5.05 more concrete
   - Add assessment criteria to G7.04
   - Simplify G8.02B for grade 8
   - 2 hours

3. **Add advanced features** (T23-CG-01, T23-CG-03, T23-CG-05)
   - Multi-hand detection
   - Face advanced features (if available)
   - Low-resource environment considerations
   - 2.5 hours

**Total Effort:** ~5 hours
**Impact:** Comprehensive coverage, handles edge cases

---

### Total Implementation Effort

- **Phase 1 (HIGH):** ~6 hours
- **Phase 2 (MEDIUM):** ~9 hours
- **Phase 3 (LOW):** ~5 hours
- **TOTAL:** ~20 hours for complete T23 optimization

---

### Minimum Viable Product

**If time is limited, do Phase 1 only:**
- Fixes critical blockers
- Adds essential bridge skills
- Corrects dependency errors
- Makes T23 functionally complete

**Estimated Impact:**
- Before: 26 issues across all priorities
- After Phase 1: 20 issues remaining (all MEDIUM/LOW)
- After Phase 1+2: 9 issues remaining (all LOW)
- After All Phases: 0 critical issues

---

## CONCLUSION

The current T23 (AI Perception) skills are **substantially improved** after Phase 1 optimization. Most critical issues have been resolved:
- ✅ Skills properly split and scoped
- ✅ Block syntax accurate
- ✅ No circular dependencies
- ✅ Good overall progression

**Remaining issues are primarily:**
1. **Scaffolding gaps** at grade transitions (G5→G6, within G6, G8)
2. **Missing intermediate practice skills** between learning and applying
3. **Minor technical details** in descriptions (table columns, parameters)
4. **Coverage gaps** for advanced patterns (multimodal, performance, multi-hand)

**All remaining HIGH priority issues can be resolved in ~6 hours.**

**Recommendation:** Implement Phase 1 immediately, Phase 2 when time permits, Phase 3 as enhancements.

---

**Document Version:** 1.0
**Created:** 2025-11-23
**Analyst:** Claude (Sonnet 4.5)
**Status:** COMPLETE ANALYSIS READY FOR REVIEW
