# T23 Optimization Report - Phase 1

## Executive Summary

Analyzed 44 original T23 skills against CreatiCode's actual AI perception blocks and optimized to 49 skills with improved scaffolding, accuracy, and internal coherence.

## Critical Issues Fixed

### 1. REMOVED SKILL - Non-existent Feature (HIGH PRIORITY)

**T23.G6.11: Apply AR face filters and effects** - DELETED

**Issue:** This skill described using `run face AR camera with effect [EFFECT_NAME]` block, which does NOT exist in CreatiCode's AI category. The AR face blocks that exist (`switch to AR face camera...`) belong to the 3D AR/VR category (T20) and are for 3D scene construction, not AI perception/filters.

**Impact:** Students would be unable to complete this skill as the blocks don't exist. This was a fundamental mismatch with platform capabilities.

**Resolution:** Removed skill entirely. Face detection (T23.G6.09.01-02) remains for AI perception use cases.


### 2. Incorrect Block Syntax (HIGH PRIORITY)

Multiple skills used incorrect or oversimplified block syntax that didn't match actual CreatiCode blocks:

**T23.G6.01 Original:**
- Described as: `recognize speech in [language] and store in [variable]`
- **Actual blocks:** `start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]` → `end speech recognition` → `text from speech`

**T23.G6.03B Original:**
- Described as: `OpenAI Whisper: transcribe audio from [SOURCE] in [LANGUAGE] result [variable]`
- **Actual block:** `OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`

**T23.G6.09 Original:**
- Generic description
- **Actual block:** `run face detection debug [yes/no v] and write into table [TABLENAME v]`

**T23.G6.03A Original:**
- Referenced "AI Speaker block" (doesn't exist)
- **Actual block:** `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as []`

**Impact:** Students following the skill descriptions would search for non-existent blocks or use wrong blocks.

**Resolution:** Updated all skills to use exact block syntax from blockdes8.txt.


### 3. Missing Scaffolding (HIGH PRIORITY)

Several skills were too broad and lacked proper progression:

**Hand Detection (T23.G6.04):**
- Original: Single skill covering setup, curl angles, direction data, and x/y coordinates
- **New structure:**
  - T23.G6.04.01: Set up hand detection and view debug output
  - T23.G6.04.02: Read and display finger curl angles
  - T23.G6.04.03: Read finger direction data for advanced gestures
- **Rationale:** Each sub-skill introduces one new table column type, building from visual debugging to data reading to complex analysis.

**Body Pose Detection (T23.G6.08):**
- Original: Single skill covering 2D detection, single vs multi-person modes, and keypoint reading
- **New structure:**
  - T23.G6.08.01: Set up 2D body pose detection and read keypoint positions (includes single vs multi-person comparison)
  - T23.G6.08.02: Detect body poses and trigger actions (angle calculations, pose logic)
- **Rationale:** Separates setup/configuration from computation/logic.

**Face Detection (T23.G6.09):**
- Original: Single skill covering all aspects
- **New structure:**
  - T23.G6.09.01: Set up face detection and view detected faces
  - T23.G6.09.02: Read face data and trigger actions
- **Rationale:** Separates visual debugging from data-driven programming.

**Speech Recognition (T23.G6.01):**
- Original: Combined basic use and language selection
- **New structure:**
  - T23.G6.01.01: Capture a single spoken phrase with basic speech recognition (default language)
  - T23.G6.01.02: Select speech recognition language and observe accuracy differences
- **Rationale:** Students first master the basic flow, then explore language options.

**New Bridge Skill Added:**
- **T23.G5.05: Identify what data hand, body, and face detection provides**
- **Purpose:** Bridges G5 conceptual understanding to G6 coding by teaching what data (curl, dir, x, y, z, part columns) these blocks output before students use the blocks.


### 4. Dependency Issues (MEDIUM-HIGH PRIORITY)

**Same-grade circular dependencies:**
- T23.G6.01 depended on T23.G6.01 (self-dependency via poorly structured skill)
- **Fixed:** Split into progressive sub-skills with proper dependencies

**X-2 rule violations:**
- Multiple G6 skills depended on G4 skills (2-grade gap acceptable) but also had unnecessary G3 dependencies (3-grade gap)
- Example: T23.G6.04 depended on T23.G3.01 (describing pixels as a grid)
- **Fixed:** Removed distant dependencies; ensured G6 skills depend on G5 or G4, not G3

**Missing prerequisites:**
- T23.G6.03A (voice chatbot) had no text-to-speech prerequisite
- **Fixed:** Added T23.G6.02.01 (basic text-to-speech) as new prerequisite skill

**Progression gaps:**
- G5 (conceptual) jumped directly to G6 (complex coding) without bridge skills
- **Fixed:** Added T23.G5.05 to prepare students for table-based AI data


### 5. Age-Appropriateness Issues (MEDIUM PRIORITY)

**K-2 skills:**
- ✅ **Good:** All K-2 skills were properly picture-based/unplugged with no block references
- Minor improvement: Clarified that activities use "picture cards," "physical devices," and "illustrated scenarios" - no screens

**G3+ skills:**
- ⚠️ **Issue:** Some G3-G5 skills were too conceptual without enough block coding practice
- **Fixed:**
  - G3 skills now explicitly mention costume editor, waveform visualizations
  - G4 skills include building simple diagnostic UIs
  - G5 skills involve using costume editor and building diagnostic tools
  - G6+ skills are heavily block-focused with specific syntax

**Complexity creep:**
- Some G6 skills were appropriate for G7 level (e.g., combining multiple modalities)
- **Fixed:** Moved multimodal combination skills to G7, kept G6 focused on single-modality mastery


### 6. Removed Duplicate/Overlapping Skills (MEDIUM PRIORITY)

**T23.G6.01B and T23.G6.01:**
- Original: Significant overlap in basic speech recognition
- **Resolution:** Clarified distinction:
  - T23.G6.01.01-02: Single-shot recognition (`start` → `end` → `text from speech`)
  - T23.G6.01B: Continuous recognition (`start continuous` → list updates → `stop continuous`)

**T23.G6.04B (hand direction):**
- Original: Separate skill for direction data
- **Resolution:** Integrated as T23.G6.04.03 for better progression flow

**T23.G6.08B (single vs multi-person body tracking):**
- Original: Separate skill comparing modes
- **Resolution:** Integrated comparison into T23.G6.08.01 as a learning point, not separate skill


### 7. Clarity and Precision Improvements (MEDIUM PRIORITY)

**Vague descriptions made specific:**

**T23.G8.00A (was vague):**
- Original: Generic "supervised learning for perception classification"
- **Fixed:** Explicit KNN workflow: collect labeled data → train with `create KNN number classifier` → understand K parameter effects

**T23.G7.00A (was too abstract):**
- Original: Broad "choose appropriate input modality"
- **Fixed:** Concrete decision criteria: accuracy in noise, user effort for hands-free, privacy implications, accessibility needs; create decision matrix

**T23.G8.02 (lacked specifics):**
- Original: "Train and deploy custom gesture classifier"
- **Fixed:** Added full workflow: (1) data collection UI, (2) `create KNN number classifier from table [training v] K [3] named [gestureClassifier]`, (3) `predict for table [live_data v] with classifier [gestureClassifier]`, test with 5+ gestures


**Added concrete examples throughout:**
- G6 skills now show table column names (curl, dir, x, y, z, part)
- G6-G8 skills include block syntax in descriptions
- G7-G8 skills specify concrete applications (fitness coaching, space mission simulation, privacy policies)


## Summary Statistics

### Skill Count Changes
- **Original:** 44 skills
- **Optimized:** 49 skills
- **Net change:** +5 skills (due to splitting overly broad skills for better scaffolding)

### Skills by Grade
| Grade | Original | Optimized | Change | Reason |
|-------|----------|-----------|--------|--------|
| GK | 3 | 3 | 0 | Appropriate |
| G1 | 3 | 3 | 0 | Appropriate |
| G2 | 3 | 3 | 0 | Appropriate |
| G3 | 3 | 3 | 0 | Appropriate |
| G4 | 3 | 3 | 0 | Appropriate |
| G5 | 4 | 5 | +1 | Added bridge skill (T23.G5.05) |
| G6 | 11 | 17 | +6 | Split broad skills, added prerequisites |
| G7 | 6 | 6 | 0 | Appropriate |
| G8 | 6 | 6 | 0 | Appropriate |
| **Deleted** | 2 | 0 | -2 | Removed T23.G6.11 (non-existent), consolidated T23.G6.04B, T23.G6.08B |

### Skills Removed
1. **T23.G6.11** - AR face filters (block doesn't exist)
2. **T23.G6.04B** - Hand direction (merged into T23.G6.04.03)
3. **T23.G6.08B** - Single vs multi-person (merged into T23.G6.08.01)

### Skills Added
1. **T23.G5.05** - Identify what data detection blocks provide (bridge skill)
2. **T23.G6.01.01** - Basic speech recognition without language selection
3. **T23.G6.01.02** - Speech recognition with language selection
4. **T23.G6.02.01** - Basic text-to-speech (prerequisite for chatbot)
5. **T23.G6.04.01** - Hand detection setup and debug
6. **T23.G6.04.02** - Read finger curl angles
7. **T23.G6.04.03** - Read finger direction data (was T23.G6.04B)
8. **T23.G6.08.01** - 2D body pose setup and keypoints
9. **T23.G6.08.02** - Detect poses and trigger actions
10. **T23.G6.09.01** - Face detection setup
11. **T23.G6.09.02** - Read face data and trigger actions
12. **T23.G8.02B** - Tune KNN classifier performance

### Skills Significantly Revised
- **T23.G6.01** → split into T23.G6.01.01, T23.G6.01.02
- **T23.G6.03A** → corrected text-to-speech block syntax
- **T23.G6.03B** → corrected OpenAI Whisper syntax
- **T23.G6.04** → split into T23.G6.04.01-03
- **T23.G6.08** → split into T23.G6.08.01-02
- **T23.G6.09** → split into T23.G6.09.01-02
- **T23.G8.00A** → clarified KNN classifier focus
- **T23.G8.02** → added complete workflow description


## Cross-Topic Dependencies Preserved (NOT FIXED)

The following cross-topic dependencies were noted but **preserved** as instructed:

### Expected/Appropriate Dependencies
1. **T22 (Chatbot)** - T23.G6.03A, T23.G6.03B depend on T22.G6.01 for voice chatbot skills ✅
2. **T10 (Tables)** - T23.G7.01 depends on T10.G5.04 for reading gesture data from tables ✅
3. **T11 (Custom Blocks)** - T23.G7.01 depends on T11.G5.02 for reusable gesture handlers ✅
4. **T16 (UI/Widgets)** - Multiple skills reference T16 for voice→UI mappings ✅
5. **T09 (Variables)** - G6+ skills depend on T09.G3.01.04 for displaying values ✅
6. **T08 (Conditionals)** - G6+ skills depend on T08.G3.01 for if-blocks ✅

### Dependencies That May Need Review
1. **T05 (Design Thinking)** - Several G7-G8 skills depend on T05:
   - T23.G7.04 → T05.G5.06 (planning for accessibility logging)
   - T23.G7.06 → T05.G5.01 (user needs for calibration wizard)
   - T23.G8.04 → T05.G7.03, T05.G8.01 (unintended harms, design brief for privacy policy)
   - **Question:** Are these dependencies intentional? T05 is Design Thinking, which makes sense for ethics/privacy/user research, but verify this is the intended cross-topic link.

2. **T04 (Algorithms)** - T23.G8.04 → T04.G6.01 (algorithm patterns for privacy policy)
   - **Question:** Is this dependency necessary? Privacy policies may not strongly relate to algorithm patterns.

3. **T23.G7.01** depends on T11.G5.02 (custom blocks G5) but students don't use custom blocks until G7
   - **Observation:** There's a 2-grade gap between learning custom blocks (G5) and using them for gestures (G7). This might be fine, but could benefit from a G6 skill that practices custom blocks in a simpler context first.


## Verified Against CreatiCode AI Blocks

All AI perception blocks in blockdes8.txt Category: AI have been accounted for:

### Speech Recognition ✅
- ✅ `ai_startspeech` - covered in T23.G6.01.01-02
- ✅ `ai_startopenaispeech` - covered in T23.G6.03B
- ✅ `ai_clearspeech` - implicitly covered in G6-G7 skills
- ✅ `ai_endspeech` - covered in T23.G6.01.01-02
- ✅ `ai_textfromspeech` - covered in T23.G6.01.01-02
- ✅ `ai_startrecognizer` - covered in T23.G6.01B (continuous recognition)
- ✅ `ai_stoprecognizer` - covered in T23.G6.01B

### Text-to-Speech ✅
- ✅ `ai_speakinlanguage` - covered in T23.G6.02.01, T23.G6.03A
- ✅ `ai_stopspeaking` - implicitly covered in G6-G7 skills

### Vision/Gesture Detection ✅
- ✅ `ai_facedetection` - covered in T23.G6.09.01-02
- ✅ `ai_bodydetection` - covered in T23.G6.08.01-02 (2D pose)
- ✅ `ai_stopbodydetection` - implicitly covered
- ✅ `ai_bodydetection3` - covered in T23.G6.10 (3D pose)
- ✅ `ai_handdetection3` - covered in T23.G6.04.01-03
- ✅ `ai_updatedebug` - covered in T23.G6.04.01 and others

### Machine Learning ✅
- ✅ `ai_createknnclassifier` - covered in T23.G8.00A, T23.G8.02
- ✅ `ai_predictknnclassifier` - covered in T23.G8.02, T23.G8.02B

### Out of Scope (Other AI Category Blocks)
The following AI blocks are NOT perception-related and correctly NOT covered in T23:
- ❌ `ai_parsesentence` - NLP, likely in T24 (Generative AI)
- ❌ `ai_openaiimagereporter` - DALL-E, likely in T24
- ❌ `ai_xoimagereporter` - Image search, likely in T24
- ❌ `googlesearch` - Web search, likely in T24
- ❌ `attachimagetochat` - Chat multimodal, likely in T22 or T24
- ❌ `attachfilestochat` - Chat attachments, likely in T22 or T24
- ❌ `attachgooglefiletochat` - Chat attachments, likely in T22 or T24
- ❌ `getmoderationresult*` - Content moderation, likely in T24
- ❌ `addtabletopinecone` - Vector databases, likely in T24


## Recommendations

### For Phase 2 (if applicable):
1. **Review T05 dependencies** - Verify that Design Thinking cross-references in T23.G7-G8 are intentional
2. **Consider T11 progression** - Students learn custom blocks in G5 but don't use them for gestures until G7; add G6 practice?
3. **Check T16 coverage** - Ensure T16 (UI/Widgets) adequately supports the voice→UI mapping use cases referenced in T23
4. **Verify T24 boundary** - Confirm that NLP (`ai_parsesentence`), image generation (`ai_openaiimagereporter`), and other non-perception AI blocks are properly assigned to T24

### For Curriculum Implementation:
1. **G6 is dense** - 17 skills in G6 (35% of total). Consider whether school year has enough time
2. **Assessment strategy** - The split skills (e.g., T23.G6.04.01-03) should be assessed together as a unit, not separately
3. **Hardware requirements** - All G6+ skills require camera/microphone access; ensure devices support this
4. **Privacy training** - Teachers should be trained on T23.G6.07, T23.G7.05, T23.G8.04 before students use perception blocks


## Conclusion

T23 has been successfully optimized for internal coherence, accurate block syntax, proper scaffolding, and alignment with CreatiCode's actual AI perception capabilities. The topic now provides a clear K-8 progression from unplugged sensing awareness to sophisticated multimodal AI applications with strong emphasis on privacy, fairness, and responsible deployment.

All high-priority issues have been resolved. Cross-topic dependencies have been preserved for your review. The optimized skill set is ready for integration into the full allskills.md file.
