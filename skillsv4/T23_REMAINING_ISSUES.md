# T23 AI Perception - Remaining Issues Analysis

## Executive Summary

The T23 optimization has made excellent progress, but there are still several issues that need fixing:

1. **9 skills need to be broken down** (too broad, covering multiple concepts)
2. **5 missing scaffolding skills** (gaps in progression)
3. **3 inaccurate descriptions** (don't match actual API behavior)
4. **Multiple dependency issues** (cross-grade references, missing prereqs)
5. **Several grade-appropriateness issues** (K-2 coding, G3+ missing hands-on)

**Total issues identified**: 25+ individual problems across 20+ skills

---

## 1. SKILLS THAT NEED TO BE BROKEN DOWN

### ISSUE 1.1: T23.G6.04.04 - Too Broad (Gesture Recognition)
**Current Skill**: "Recognize basic gestures from hand detection data"
**Problem**: Combines multiple complex concepts:
- Understanding gesture detection logic (thresholds, conditions)
- Implementing 3-5 different gestures (fist, open hand, pointing, thumbs up, peace sign)
- Using if-blocks to check conditions
- Displaying gesture names
- No UI integration (but description says "display")

**Suggested Breakdown**:
- **T23.G6.04.04.01**: Detect fist gesture using curl thresholds
  - Focus: ONE gesture (fist = all fingers curl < 90)
  - Single if-block check
  - Display result

- **T23.G6.04.04.02**: Detect open hand gesture using curl thresholds
  - Focus: ONE gesture (open = all curl > 150)
  - Understanding opposite threshold logic

- **T23.G6.04.04.03**: Detect pointing gesture combining multiple fingers
  - Focus: Compound conditions (index > 170 AND others < 90)
  - Using AND logic for multi-finger gestures

- **T23.G6.04.04.04**: Build multi-gesture recognition system
  - Focus: Combining multiple gesture checks with if-else
  - State management (which gesture is active)
  - Display logic for multiple options

**Impact**: 4 sub-skills instead of 1 mega-skill

---

### ISSUE 1.2: T23.G6.09.02 - Too Broad (Body Pose Detection)
**Current Skill**: "Detect body poses and trigger actions"
**Problem**: Combines:
- Calculating angles between body landmarks (math/geometry)
- Detecting specific poses (arms up, squat)
- Triggering actions when poses detected
- Using if-blocks to compare y-coordinates
- Multiple pose types in one skill

**Suggested Breakdown**:
- **T23.G6.09.02.01**: Calculate distance between two body keypoints
  - Focus: Reading two keypoints, computing distance
  - Understanding coordinate math (distance formula or simple subtraction)

- **T23.G6.09.02.02**: Detect "arms up" pose using y-coordinate comparison
  - Focus: ONE pose (wrists above shoulders)
  - Simple y-coordinate comparison

- **T23.G6.09.02.03**: Detect "squat" pose using y-coordinate comparison
  - Focus: ONE pose (knees below hips)
  - Understanding vertical position thresholds

- **T23.G6.09.02.04**: Trigger actions based on detected poses
  - Focus: Event-driven programming (when pose detected, do action)
  - State management across pose changes

**Impact**: 4 sub-skills instead of 1 mega-skill

---

### ISSUE 1.3: T23.G6.03.01 - Too Broad (Voice Chatbot Loop)
**Current Skill**: "Build a two-way voice chatbot loop"
**Problem**: Combines THREE major AI systems:
- Speech-to-text (speech recognition workflow)
- ChatGPT API (prompt, request, response handling)
- Text-to-speech (TTS workflow)
- Turn-taking logic (complex state management)
- Timing issues (waiting for TTS to complete)
- Conversation state across turns

**Suggested Breakdown**:
- **T23.G6.03.01.01**: Connect speech recognition output to ChatGPT input
  - Focus: Data flow from speech → text → ChatGPT
  - Understanding the pipeline concept

- **T23.G6.03.01.02**: Connect ChatGPT output to TTS input
  - Focus: Data flow from ChatGPT response → TTS
  - Voice parameter selection

- **T23.G6.03.01.03**: Implement turn-taking logic for voice chat
  - Focus: State management (listening → processing → speaking → repeat)
  - Timing coordination
  - Preventing overlapping speech

**Rationale**: This is a MAJOR integration skill that combines T22 (ChatGPT) and T23 (Speech). It deserves scaffolding.

**Impact**: 3 sub-skills instead of 1 mega-skill

---

### ISSUE 1.4: T23.G8.02.01 - Too Broad (Data Collection UI)
**Current Skill**: "Create data collection UI for gesture samples"
**Problem**: Combines:
- Building UI widgets (buttons, counters, feedback)
- Implementing collection workflow (select type → perform → capture → store)
- Data structure design (training table format)
- Quality checks (reject bad samples)
- Collecting 20+ samples per gesture class

**Suggested Breakdown**:
- **T23.G8.02.01.01**: Design training data table structure
  - Focus: Understanding feature columns vs label column
  - Table schema design

- **T23.G8.02.01.02**: Build UI for sample collection
  - Focus: Buttons, counters, visual feedback
  - User interaction design

- **T23.G8.02.01.03**: Implement capture and store workflow
  - Focus: Capturing hand data when button pressed
  - Storing in table with correct format
  - Quality checks

**Impact**: 3 sub-skills instead of 1 mega-skill

---

### ISSUE 1.5: T23.G8.03.01 - Too Broad (Confusion Matrix Evaluation)
**Current Skill**: "Evaluate classifier performance using confusion matrices"
**Problem**: Combines:
- Understanding confusion matrix concept
- Testing classifier with labeled data
- Recording predicted vs actual in matrix table
- Calculating accuracy (overall metric)
- Calculating precision (per-class metric)
- Calculating recall (per-class metric)
- Identifying confused pairs
- Using analysis to improve training

**Suggested Breakdown**:
- **T23.G8.03.01.01**: Build confusion matrix from test results
  - Focus: Testing classifier, recording predictions
  - Matrix table structure (actual rows, predicted columns)

- **T23.G8.03.01.02**: Calculate accuracy, precision, and recall
  - Focus: Computing metrics from confusion matrix
  - Understanding true/false positives/negatives

- **T23.G8.03.01.03**: Identify and fix common misclassifications
  - Focus: Analysis and improvement
  - Using metrics to guide training data changes

**Impact**: 3 sub-skills instead of 1 mega-skill

---

### ISSUE 1.6: T23.G7.06 - Too Broad (Calibration Wizard)
**Current Skill**: "Build a calibration wizard for sensors"
**Problem**: Combines:
- Multi-step UI wizard (T16 UI patterns)
- Microphone volume check
- Lighting test
- Gesture framing
- Each step has different sensor test
- Display readings
- Offer fixes

**Suggested Breakdown**:
- **T23.G7.06.01**: Build microphone calibration step
  - Focus: ONE sensor calibration
  - Volume meter, speak test

- **T23.G7.06.02**: Build camera lighting calibration step
  - Focus: ONE sensor calibration
  - Brightness meter, lighting guidance

- **T23.G7.06.03**: Create multi-step wizard UI flow
  - Focus: Connecting multiple calibration steps
  - Navigation between steps
  - Overall wizard pattern

**Impact**: 3 sub-skills instead of 1 mega-skill

---

### ISSUE 1.7: T23.G8.03 - Too Broad (Multi-User Cooperative Simulation)
**Current Skill**: "Fuse voice, pose, and UI widgets into a cooperative simulation"
**Problem**: Extremely broad capstone skill combining:
- Multi-user scenario design
- THREE different input modalities simultaneously
- Voice commands from one user
- Gestures from another user
- Widget confirmation from third user
- Timing coordination
- Conflict prevention
- Event logging

**Suggested Breakdown**:
- **T23.G8.03.01**: Design multi-user scenario with role assignments
  - Focus: Planning who uses which modality
  - Role definition and coordination

- **T23.G8.03.02**: Implement parallel input processing
  - Focus: Handling multiple modalities at once
  - State management for multiple users

- **T23.G8.03.03**: Add conflict prevention and event logging
  - Focus: Validation (can't launch if gesture not confirmed)
  - Live event log display

**Note**: Current T23.G8.03.01 is "Evaluate classifier performance" which should be BEFORE the cooperative simulation (dependency issue).

**Impact**: Need to renumber - this mega-skill needs breakdown but conflicts with existing .01

---

### ISSUE 1.8: T23.G8.08 - Too Broad (Custom Neural Network)
**Current Skill**: "Build a custom neural network for gesture classification"
**Problem**: Combines:
- Understanding neural network architecture
- Specifying layer sizes (input, hidden, output)
- Configuring training parameters (learning rate, epochs)
- Training the network
- Deploying for real-time recognition
- Comparing to KNN classifier
- Understanding when neural networks are appropriate

**Suggested Breakdown**:
- **T23.G8.08.01**: Design neural network architecture for gesture data
  - Focus: Determining layer sizes based on features and classes
  - Understanding input/hidden/output structure

- **T23.G8.08.02**: Train neural network with collected gesture data
  - Focus: Using training blocks
  - Monitoring training progress
  - Configuring parameters

- **T23.G8.08.03**: Compare neural network vs KNN performance
  - Focus: Evaluation and comparison
  - Understanding trade-offs

**Impact**: 3 sub-skills instead of 1 mega-skill

---

### ISSUE 1.9: T23.G8.12.03 - Still Too Broad
**Current Skill**: "Document ML workflow and deployment plan"
**Problem**: Even after breaking down T23.G8.12, the .03 sub-skill still combines:
- All 7 stages documentation
- Testing procedures
- Performance benchmarks
- Deployment considerations
- Maintenance and updates

**Suggested Breakdown**:
- **T23.G8.12.03.01**: Document model training and evaluation workflow
  - Focus: Stages 1-5 (problem definition through evaluation)
  - Training documentation

- **T23.G8.12.03.02**: Create deployment and monitoring plan
  - Focus: Stages 6-7 (deployment and maintenance)
  - Production considerations
  - Monitoring strategy

**Impact**: 2 sub-skills instead of 1 still-too-broad skill

---

## 2. MISSING SCAFFOLDING SKILLS

### ISSUE 2.1: Gap Between G5.05.03 and G6.01.01 (Speech Recognition)
**Problem**: Students go from "picture-based workflow analysis" (G5.05.03) directly to implementing full speech recognition with error handling (G6.01.01).

**Missing Skill**:
- **T23.G5.05.04**: Trace speech recognition workflow in example code
  - Description: Students examine annotated code showing speech recognition workflow: start detection → speak → wait → end → read text. They match each code block to workflow steps and identify what each block does. Picture-based code reading, no hands-on coding yet. Prepares for G6 implementation.
  - Dependencies: T23.G5.05.03
  - Grade: 5

**Impact**: Better bridge from conceptual (G5) to practical (G6)

---

### ISSUE 2.2: Gap Between G6.04.02.03 and G6.04.03 (Hand Detection)
**Problem**: Students jump from "displaying curl values" to "reading direction data for advanced gestures" without learning basic gesture logic first.

**Missing Skill**:
- **T23.G6.04.02.04**: Detect single threshold-based gesture
  - Description: Students implement ONE simple gesture using a single threshold: "finger extended" = curl > 150. They use a simple if-block to check the condition and display "yes/no". Focus on understanding how thresholds work with one example before combining multiple conditions.
  - Dependencies: T23.G6.04.02.03
  - Grade: 6

**Impact**: Scaffolds between display and complex multi-finger gestures

---

### ISSUE 2.3: Gap Between G6.01.03 and G6.01.04 (Speech Recognition)
**Problem**: Students jump from "continuous speech recognition" directly to "error handling with retry logic" without basic error detection.

**Missing Skill**:
- **T23.G6.01.03.01**: Detect when speech recognition returns empty result
  - Description: Students check if `text from speech` is empty (no speech detected) and display a message: "No speech detected, please try again." They learn the if-empty check pattern before implementing complex retry logic.
  - Dependencies: T23.G6.01.03
  - Grade: 6

**Impact**: Scaffolds between basic recognition and error recovery

---

### ISSUE 2.4: Gap Between G8.00 and G8.01.02 (KNN Classification)
**Problem**: Students learn supervised learning concepts (G8.00) then jump to practicing KNN with numeric data (G8.01.02) without understanding what KNN actually does.

**Missing Skill**:
- **T23.G8.00.01**: Understand how KNN finds similar examples
  - Description: Students examine a visual diagram showing how KNN works: given a new data point, find the K nearest training examples, use majority vote for classification. They practice with a paper-based activity plotting points and finding nearest neighbors before coding.
  - Dependencies: T23.G8.00
  - Grade: 8

**Impact**: Conceptual understanding before hands-on practice

---

### ISSUE 2.5: Gap Between G8.08 and G8.09 (Neural Networks)
**Problem**: Students build custom neural networks (G8.08) then immediately save/load them (G8.09) without evaluating performance first.

**Missing Skill**:
- **T23.G8.08.04**: Evaluate neural network performance on test data
  - Description: Students test their trained neural network on test data, calculate accuracy, and compare to target metrics. They identify when the network needs more training (low accuracy) vs when it's ready to save. Prepares for model persistence (G8.09).
  - Dependencies: T23.G8.08.03 (after comparison to KNN)
  - Grade: 8

**Impact**: Ensures students understand model quality before persistence

---

## 3. INACCURATE SKILL DESCRIPTIONS

### ISSUE 3.1: T23.G6.11 - NLP Description Too Specific
**Current Description**: "Students use `analyze sentence [SENTENCE] and write into table [TABLENAME v]` to analyze sentence structure and extract parts of speech (nouns, verbs, adjectives, etc.) from recognized speech or text input. They implement applications that parse voice commands to identify action words (verbs) and objects (nouns): 'move the robot forward' → action: move, object: robot, direction: forward."

**Problem**:
- Description assumes NLP block provides structured output with labeled parts of speech
- Doesn't specify what the table actually contains (columns, rows)
- Over-promises what the NLP block can do
- Need to verify actual NLP block output format

**Correction Needed**:
Without documentation of what `analyze sentence` actually returns, the description should be more generic:
"Students use `analyze sentence [SENTENCE] and write into table [TABLENAME v]` to analyze sentence structure. They explore the table output to understand what linguistic information is provided (word tokens, part-of-speech tags, dependencies). They read table values to extract key information from sentences."

**Impact**: More accurate expectations

---

### ISSUE 3.2: T23.G6.04.02.01 - Table Structure Incomplete
**Current Description**: Mentions "47 rows per hand (5 summaries + 21 2D + 21 3D)" and columns "hand, part, curl, dir, x, y, z"

**Problem**:
- Doesn't explain that rows 1-5 are finger summaries (ONE row per finger)
- Doesn't explain rows 6-26 are 2D landmarks (21 keypoints with x, y)
- Doesn't explain rows 27-47 are 3D landmarks (21 keypoints with x, y, z)
- Doesn't clarify that curl and dir are ONLY in rows 1-5 (finger summaries), not in landmark rows

**Correction Needed**:
"Students learn hand detection table structure: 47 rows per detected hand divided into three sections: (1) rows 1-5 contain finger summaries (thumb, index, middle, ring, pinky) with columns [hand, part, curl, dir, x, y, z], (2) rows 6-26 contain 2D landmark positions (21 keypoints) with columns [hand, part, x, y], (3) rows 27-47 contain 3D landmark positions (21 keypoints) with columns [hand, part, x, y, z]. They understand that curl (0-180°) and dir (0-360°) are only available in finger summary rows."

**Impact**: Accurate understanding of table structure

---

### ISSUE 3.3: T23.G6.09.01.02 - Body Detection Table Incomplete
**Current Description**: "17 keypoints + 4 limbs per person" with columns "id, part, x, y, curl, dir"

**Problem**:
- Doesn't explain that limbs (left_arm, right_arm, left_leg, right_leg) have curl and dir values
- Doesn't explain that individual keypoints (nose, left_eye, etc.) may NOT have curl and dir
- Needs clarification on which rows have which columns
- 17 keypoints + 4 limbs = 21 total rows per person

**Correction Needed**:
"Students learn body detection table structure: 21 rows per detected person consisting of 17 keypoint rows (nose, left_eye, right_eye, left_ear, right_ear, left_shoulder, right_shoulder, left_elbow, right_elbow, left_wrist, right_wrist, left_hip, right_hip, left_knee, right_knee, left_ankle, right_ankle) with columns [id, part, x, y] and 4 limb measurement rows (left_arm, right_arm, left_leg, right_leg) with additional columns [curl, dir] indicating limb angle and direction. They understand that curl and dir are only available for limb measurements, not individual keypoints."

**Impact**: Accurate understanding of what data is available where

---

## 4. DEPENDENCY ISSUES

### ISSUE 4.1: T23.G7.00 Dependencies Violate X-2 Rule
**Current Dependencies**:
- T23.G6.03.01 (G6 → G7, only 1 grade gap)
- T23.G6.04.05 (G6 → G7, only 1 grade gap)
- T23.G6.09.02 (G6 → G7, only 1 grade gap)
- T23.G5.02 (G5 → G7, satisfies X-2)

**Problem**: Three cross-topic dependencies from G6 violate the X-2 rule for G7.

**Fix**: Change dependencies to G5 or earlier skills, OR move T23.G7.00 to G8 (if it's truly advanced).

**Suggested Fix**:
- Keep T23.G5.02 (conceptual understanding of modality issues)
- Remove specific G6 skill dependencies
- Add: T23.G5.05.03 (workflow patterns - prepares for comparing modalities)

**Corrected Dependencies**:
- T23.G5.02: Explain why an AI might mis-hear or mis-see
- T23.G5.05.03: Understand perception API workflow patterns

---

### ISSUE 4.2: Many G6 Skills Depend on G5 Skills (Potential X-2 Violation)
**Examples**:
- T23.G6.01.01 depends on T05.G5.01, T06.G5.01, T08.G5.01, etc. (all G5)
- T23.G6.04.01 depends on multiple G5 skills

**Problem**: If strict X-2 applies to ALL cross-topic dependencies, these violate the rule (G5 → G6 is only 1 grade gap).

**Clarification Needed**: Does X-2 rule apply to foundational programming skills (T05-T11, T15) or only to advanced cross-topic dependencies?

**Recommendation**:
- If X-2 applies to foundational skills, change G6 dependencies to G4 skills from those topics
- If X-2 only applies to advanced cross-topic deps, current dependencies are OK

---

### ISSUE 4.3: T23.G6.01.01 Has Duplicate Dependency
**Current Dependencies**:
- T09.G5.01: Display variable value on stage using the variable monitor
- T09.G5.01: Use multiple variables together in a single expression (DUPLICATE)

**Fix**: Remove duplicate, keep both concepts if they're different skills, or clarify which T09.G5.01 is correct.

---

### ISSUE 4.4: T23.G8.01 Incorrect Numbering/Dependencies
**Problem**:
- T23.G8.01 is "Offer interchangeable input modes with accessibility rules"
- T23.G8.01.02 is "Practice KNN classification with simple numeric data"
- These are NOT related skills - numbering issue

**Fix**:
- Renumber T23.G8.01.02 to T23.G8.00.01 or create new section
- T23.G8.01.03 should also be renumbered
- Current structure has KNN skills (G8.00, G8.01.02, G8.01.03) mixed with multimodal skills (G8.01)

---

### ISSUE 4.5: T23.G8.03 Has Child Before Parent
**Problem**:
- T23.G8.03 is the cooperative simulation (major capstone)
- T23.G8.03.01 is "Evaluate classifier performance" (should be earlier)

**Fix**: Renumber classifier evaluation skills to proper sequence before the cooperative simulation.

---

### ISSUE 4.6: Missing Dependency - T23.G6.04.08 Should Depend on Earlier Hand Skills
**Current**: T23.G6.04.08 only depends on T23.G6.04.02.03

**Problem**: Stopping hand detection requires understanding the full workflow, not just displaying data.

**Fix**: Add dependency on T23.G6.04.05 or T23.G6.04.04 (actually using hand detection before stopping it).

---

## 5. GRADE-APPROPRIATENESS ISSUES

### ISSUE 5.1: GK-G2 Skills Are Appropriate (Picture-Based)
**Status**: ✅ GOOD
- All GK-G2 skills are picture-based, unplugged activities
- No coding required
- Age-appropriate conceptual learning

---

### ISSUE 5.2: G3 Skills Start Coding (Appropriate)
**Status**: ✅ GOOD
- G3.01: Using costume editor (hands-on visual)
- G3.02: Waveform visualization (visual observation)
- G3.03: Identifying event blocks (code reading)
- Appropriate transition to coding environment

---

### ISSUE 5.3: G4 Skills Mix Activities and Coding (Minor Issue)
**T23.G4.01**: "use a provided slider UI" - hands-on ✅
**T23.G4.02**: "build a simple Scratch script" - hands-on ✅
**T23.G4.03**: "create a troubleshooting flowchart using sprites" - hands-on ✅

**Status**: ✅ GOOD - All G4 skills involve hands-on coding

---

### ISSUE 5.4: G5 Skills Missing Hands-On Component
**T23.G5.05.01**: "match detection types to data outputs using picture cards" - picture-based ❌
**T23.G5.05.02**: "examine annotated table examples" - picture-based ❌
**T23.G5.05.03**: "match API blocks to workflow steps using diagrams" - picture-based ❌

**Problem**: G5 skills are MORE picture-based than G3/G4, violating progression.

**Fix**: Add hands-on component to G5 skills:
- T23.G5.05.01: Use provided example projects to observe different detection types
- T23.G5.05.02: Read sample table data in CreatiCode (not just pictures)
- T23.G5.05.03: Trace through example code in CreatiCode (remix projects)

**Impact**: Make G5 appropriately hands-on for grade level

---

### ISSUE 5.5: G6-G8 Skills Are Appropriately Advanced
**Status**: ✅ GOOD
- All G6-G8 skills involve hands-on coding
- Increasing complexity and abstraction
- Age-appropriate challenges

---

## SUMMARY OF ISSUES

### By Category:
1. **Overly Broad Skills**: 9 skills need breakdown (→ 30+ sub-skills)
2. **Missing Scaffolding**: 5 gaps identified
3. **Inaccurate Descriptions**: 3 skills need corrections
4. **Dependency Issues**: 6 problems (X-2 violations, duplicates, numbering)
5. **Grade-Appropriateness**: 3 G5 skills need hands-on component

### Total Issues: 26 distinct problems across 22 skills

---

## PRIORITY RANKING

### HIGH PRIORITY (Breaks Curriculum):
1. **Issue 4.4**: Numbering conflict (G8.01 vs G8.01.02) - breaks structure
2. **Issue 4.5**: Child before parent (G8.03.01) - breaks structure
3. **Issue 3.2**: Hand detection table structure - core to many skills
4. **Issue 3.3**: Body detection table structure - core to many skills

### MEDIUM PRIORITY (Impacts Learning Quality):
5. **Issue 1.1**: T23.G6.04.04 breakdown (gesture recognition)
6. **Issue 1.2**: T23.G6.09.02 breakdown (pose detection)
7. **Issue 1.3**: T23.G6.03.01 breakdown (voice chatbot)
8. **Issue 2.1-2.5**: Missing scaffolding skills (5 gaps)
9. **Issue 5.4**: G5 hands-on component

### LOW PRIORITY (Nice to Have):
10. **Issue 1.4-1.9**: Additional skill breakdowns (improve granularity)
11. **Issue 3.1**: NLP description accuracy
12. **Issue 4.1-4.3, 4.6**: Dependency fine-tuning

---

## RECOMMENDED ACTION PLAN

### Phase 1: Fix Critical Structure Issues
1. Renumber KNN skills (G8.01.02, G8.01.03 → G8.00.01, G8.00.02)
2. Renumber classifier evaluation (G8.03.01 → proper sequence)
3. Correct table structure descriptions (hand, body)

### Phase 2: Add Missing Scaffolding
4. Add 5 missing scaffolding skills identified in Section 2

### Phase 3: Break Down Overly Broad Skills
5. Break down high-impact skills (G6.04.04, G6.09.02, G6.03.01)
6. Consider breaking down remaining skills for better granularity

### Phase 4: Fix Dependencies
7. Review and fix X-2 violations
8. Remove duplicates
9. Add missing dependencies

### Phase 5: Improve Grade-Appropriateness
10. Add hands-on components to G5 skills

---

## FINAL NOTES

The T23 optimization has made **excellent progress**:
- ✅ Removed unavailable features (expressions, demographics)
- ✅ Added workflow completion skills (stop detection)
- ✅ Improved granularity (72 → 92 skills)
- ✅ Better scaffolding at G5 level

**Remaining work** focuses on:
- Further breaking down complex skills (IXL-style one-concept-per-skill)
- Filling scaffolding gaps (smooth progression)
- Fixing structural issues (numbering, dependencies)
- Ensuring all descriptions match actual API behavior

**Estimated effort**:
- High priority fixes: 4-6 hours
- Medium priority: 8-12 hours
- Low priority: 4-8 hours
- **Total: 16-26 hours of additional work**

This is a **solid foundation** that needs refinement, not a complete redo.
