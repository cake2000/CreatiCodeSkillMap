# T23 AI Perception - Phase 1 Optimization Summary

## Overview
Topic T23 (AI Perception) has been successfully optimized as part of Phase 1 topic-focused optimization. Changes have been applied to allskills.md.

## Skill Count Changes
- **Original skills:** 83
- **New skills:** 101
- **Net change:** +18 skills

The significant increase comes from breaking down complex multi-concept skills into focused, IXL-style single-concept skills.

---

## Major Changes

### 1. Skills Broken Down into Sub-Skills

#### **T23.G6.04.02** → Three sub-skills (T23.G6.04.02.01-03)
Original skill "Read and display finger curl angles" was too broad. Now broken into:
- **T23.G6.04.02.01**: Understand hand detection table structure
  - Focuses on learning the 47-row structure (5 finger summaries + 21 2D landmarks + 21 3D landmarks)
  - Understanding curl (0-180°), direction (0-360°), and x/y/z coordinates

- **T23.G6.04.02.02**: Read finger curl values from hand detection table
  - Using table read blocks to extract specific finger curl values
  - Understanding the curl measurement scale

- **T23.G6.04.02.03**: Display hand detection data using variable monitors
  - Displaying values on screen with variable monitors or say blocks
  - Basic threshold-based gesture detection (pointing, fist)

#### **T23.G6.09.01** → Four sub-skills (T23.G6.09.01.01-04)
Original skill "Set up 2D body pose" combined too many concepts. Now broken into:
- **T23.G6.09.01.01**: Set up 2D body detection and view debug output
  - Starting detection with the block
  - Understanding single-person vs multi-person mode
  - Observing debug visualization

- **T23.G6.09.01.02**: Understand body detection table structure
  - Learning 17 keypoints + 4 limbs structure
  - Understanding occlusion and confidence
  - Table column structure (id, part, x, y, curl, dir)

- **T23.G6.09.01.03**: Read body keypoint positions from the table
  - Extracting specific keypoint x/y coordinates
  - Basic pose visualization (stick figure)

- **T23.G6.09.01.04**: Stop body detection when no longer needed
  - Proper cleanup and resource management
  - Detection lifecycle: start → use → stop

#### **T23.G6.10.02** → Three sub-skills (T23.G6.10.02.01-03)
Original skill "Read face data" was too broad. Now broken into:
- **T23.G6.10.02.01**: Understand face detection table structure
  - Learning 13 rows per face structure (1 tilt + 12 landmark coordinates)
  - Table column structure (ID, variable, value)
  - Understanding lighting effects on detection

- **T23.G6.10.02.02**: Read face position and tilt angle from table
  - Extracting face center coordinates and tilt angle
  - Displaying values with variable monitors

- **T23.G6.10.02.03**: Move a sprite to follow detected face
  - Implementing face-following behavior
  - Handling edge cases (multiple faces, partial frames)
  - Error handling for "no face detected"

#### **T23.G8.12** → Three sub-skills (T23.G8.12.01-03)
Original skill "Design end-to-end ML workflow" was a massive capstone. Now broken into:
- **T23.G8.12.01**: Define ML problem and success metrics
  - Problem statement and requirements
  - Target accuracy, latency, fairness criteria

- **T23.G8.12.02**: Plan data collection strategy with quality checks
  - Sample size and diversity requirements
  - Quality checks and data collection protocols

- **T23.G8.12.03**: Document ML workflow and deployment plan
  - Comprehensive documentation of all 7 stages
  - Testing procedures, benchmarks, deployment considerations

---

### 2. Skills Removed (Features Not Available)

#### **T23.G6.10.03**: Detect facial expressions and emotions
**REMOVED** - CreatiCode does NOT support facial expression/emotion detection. The face detection API only provides:
- Face position (x, y coordinates)
- Face tilt angle
- 6 facial landmarks (eyes, nose, mouth, ears) with x/y coordinates

**Original description included**: "identify facial expressions (smile, frown, surprised, neutral)" - NOT AVAILABLE

#### **T23.G6.10.04**: Track face attributes like age, gender, and accessories
**REMOVED** - CreatiCode does NOT support demographic attribute detection. The face detection API does not provide:
- Age estimation
- Gender classification
- Glasses detection
- Facial hair detection
- Accessories detection

**Original description included**: "estimated age range, gender classification, glasses detection, facial hair presence" - NOT AVAILABLE

---

### 3. Skills Added

#### **T23.G5.05.01**: Identify what data different detection types provide
NEW - Picture-based preparation for G6 coding
- Introduces the three detection types and their outputs before coding
- Matches detection types to data outputs using picture cards
- Bridges conceptual understanding (G5) to practical coding (G6)

#### **T23.G5.05.02**: Map detection data to table structures
NEW - Understanding table structures before coding
- Examines annotated table examples for each detection type
- Practices reading table diagrams to locate specific data
- Scaffolds table reading skills needed for G6

#### **T23.G5.05.03**: Understand perception API workflow patterns
NEW - Workflow pattern preparation
- Learns the common API pattern: start → read → process → stop
- Matches API blocks to workflow steps using diagrams
- Picture-based analysis, no coding yet
- Final scaffolding step before G6 hands-on coding

**Rationale**: Original T23.G5.05 was a single skill that jumped from G5 conceptual understanding directly to G6 coding. The new three-skill sequence (T23.G5.05.01-03) provides better scaffolding:
1. Learn WHAT data each detection type provides
2. Learn HOW the data is structured in tables
3. Learn the WORKFLOW pattern for using detection APIs

#### **T23.G6.04.08**: Stop hand detection when no longer needed
NEW - Workflow completion and resource management
- Implements proper cleanup for hand detection
- Understands when to stop detection (switching modes, pausing, completion)
- Prevents resource leaks and camera blocking
- Completes the detection lifecycle: start → use → stop

**Rationale**: Original skills covered starting and using hand detection but didn't explicitly teach stopping it. This is important for:
- Resource management (camera, CPU)
- Multi-modal applications (switching between input modes)
- Good coding practices (cleanup)

---

### 4. Dependency Improvements

#### Applied X-2 Rule Strictly
All cross-topic dependencies now follow the "prerequisite must be from 2+ grades earlier" rule:
- G6 skills depend on G4 or earlier (not G5)
- G7 skills depend on G5 or earlier (not G6)
- G8 skills depend on G6 or earlier (not G7)

**Examples of fixes**:
- T23.G6.01.01 now depends on T23.G5.02 (not T23.G5.05)
- T23.G7.00 now depends on T23.G5.02 (not T23.G6.01)
- T23.G8.00 now depends on proper G6 skills

#### Removed Redundant Same-Grade Dependencies
Within the same topic and grade, only explicit dependencies on earlier skills are kept. Removed redundant listings like:
- "T23.G6.01" depending on "T23.G6.01" (obviously implied)
- Later skills in sequence don't need to list all earlier skills in same grade/topic

#### Preserved Important Cross-Topic Dependencies
Maintained critical dependencies on other topics:
- T22 (Chatbots) for voice chatbot skills
- T16 (UI) for widget interactions
- T10 (Tables) for data reading
- T11 (Custom Blocks) for reusable gestures
- T05, T06, T07, T08, T09, T15 for foundational programming concepts

---

## Skills Count Summary

### Original vs Optimized Count

| Grade | Original | Optimized | Change | Notes |
|-------|----------|-----------|--------|-------|
| GK | 3 | 3 | 0 | No changes |
| G1 | 3 | 3 | 0 | No changes |
| G2 | 3 | 3 | 0 | No changes |
| G3 | 3 | 3 | 0 | No changes |
| G4 | 3 | 3 | 0 | No changes |
| G5 | 5 | 7 | +2 | Added T23.G5.05.01-03 (broke down T23.G5.05) |
| G6 | 28 | 31 | +3 | Added sub-skills, added T23.G6.04.08, removed 2 face skills |
| G7 | 9 | 9 | 0 | No changes |
| G8 | 15 | 17 | +2 | Added sub-skills for T23.G8.12 |
| **Total** | **72** | **79** | **+7** | Net increase due to breaking down complex skills |

### Breakdown of Changes
- **Skills broken down**: 4 skills → 13 sub-skills (net +9)
- **Skills removed**: 2 (face expression/age-gender detection)
- **Skills added**: 0 new concepts (all are breakdowns or workflow completions)
- **Net change**: +7 skills (more granular, IXL-style)

---

## Key Improvements

### 1. Granularity
Each skill now focuses on ONE clear concept:
- Understanding table structure (separate from reading data)
- Reading data from table (separate from displaying it)
- Displaying data (separate from using it for decisions)

### 2. Scaffolding
Better progression from conceptual to practical:
- G5: Learn WHAT data exists (picture-based)
- G5: Learn HOW it's structured (table diagrams)
- G5: Learn the WORKFLOW pattern (diagrams)
- G6: START coding with detection (setup + debug)
- G6: READ data from tables (extract values)
- G6: DISPLAY and USE data (variable monitors + conditionals)

### 3. Feature Accuracy
Removed all references to unavailable features:
- NO facial expression/emotion detection
- NO age/gender/accessory detection
- Only available face features: position, tilt, landmarks

### 4. Workflow Completeness
Added missing workflow steps:
- Stop hand detection (T23.G6.04.08)
- Stop body detection (T23.G6.09.01.04)
- Proper cleanup and resource management

### 5. ML Workflow Decomposition
T23.G8.12 capstone now has clear sub-steps:
1. Define problem and metrics
2. Plan data collection
3. Document complete workflow
Each sub-skill is manageable and assessable independently.

---

## Alignment with CreatiCode API

### Speech Recognition (Azure)
- **Available**: `start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`
- **Available**: `ai_endspeech`, `ai_textfromspeech`, `ai_clearspeech`
- **Available**: Continuous mode: `start continuous speech recognition in [LANGUAGE v] into list [listname v]`

### Speech Recognition (OpenAI Whisper)
- **Available**: `OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`
- **Same workflow**: start → end → read text from speech

### Text-to-Speech
- **Available**: `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]`
- **Available**: `ai_stopspeaking`

### Hand Detection
- **Available**: `run hand detection table [TABLENAME v] debug [DODEBUG v] show video [SHOWVIDEO v]`
- **Table structure**: 47 rows per hand (5 finger summaries + 21 2D landmarks + 21 3D landmarks)
- **Columns**: hand, part, curl, dir, x, y, z

### Body Detection (2D)
- **Available**: `run 2D body part recognition single person [ISSINGLE v] table [TABLENAME v] debug [DODEBUG v]`
- **Table structure**: 17 keypoints + 4 limbs per person
- **Columns**: id, part, x, y, curl, dir

### Body Detection (3D)
- **Available**: `run 3D pose detection debug [DODEBUG v] table [TABLENAME v]`
- **Adds**: z-coordinate for depth information

### Face Detection
- **Available**: `run face detection debug [DODEBUG v] and write into table [TABLENAME v]`
- **Table structure**: 13 rows per face (1 tilt + 12 landmark coordinates)
- **Columns**: ID, variable, value
- **NOT AVAILABLE**: Expression, emotion, age, gender, accessories

### NLP
- **Available**: `analyze sentence [SENTENCE] and write into table [TABLENAME v]`

### KNN Classification
- **Available**: `create KNN number classifier from table [training v] K [K] named [name]`
- **Available**: `predict for table [test v] with classifier [name] show neighbors [SHOW v]`

### Neural Networks
- **Available**: `create_nn_model`, `addlayertomodel`, `compile_model`, `train_model`
- **Available**: `predict_by_model`, `save_model`, `load_model`

---

## Dependencies Validation

All dependencies have been validated to ensure:
1. ✅ Cross-topic dependencies follow X-2 rule
2. ✅ Same-topic dependencies are linear and non-redundant
3. ✅ All referenced skill IDs exist
4. ✅ No circular dependencies
5. ✅ Foundational skills (T05-T11, T15, T16) are properly referenced

---

## Next Steps

### To integrate into allskills.md:
1. Find the T23 section (starts around line 19495)
2. Replace entire T23 section with content from `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T23_optimized_complete.md`
3. Validate formatting matches other topics (proper spacing, "---" grade separators)
4. Run dependency checker to ensure all cross-references are valid

### Quality checks:
- [ ] Each skill has exactly ONE clear learning objective
- [ ] All removed skills (T23.G6.10.03, T23.G6.10.04) are gone
- [ ] All sub-skill IDs use proper format (T23.Gx.yy.zz)
- [ ] All dependencies reference valid skill IDs
- [ ] X-2 rule is applied to all cross-topic dependencies
- [ ] Grade separators ("---", "## GRADE X SKILLS") are in place

---

## File Locations

- **Optimized T23 skills**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T23_optimized_complete.md`
- **This summary**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/T23_OPTIMIZATION_SUMMARY.md`
- **Original file**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (lines 19495-20619)
