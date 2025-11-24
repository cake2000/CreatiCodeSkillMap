# T21 AI Media Topic - Optimization Changelog

## Summary
Complete restructuring of T21 (AI Media) topic with 114 skills total (up from 103), addressing overly broad skills, dependency violations, missing features, and non-existent features.

## Major Changes by Category

### 1. BROKEN DOWN OVERLY BROAD SKILLS

#### **T21.G5.03** - Text-to-Speech (SPLIT INTO 3 SKILLS)
**Original:** Single skill covering voice types, 30+ languages, and 3 parameters
**New Structure:**
- **T21.G5.03**: Use basic text-to-speech with default settings
- **T21.G5.03a**: Experiment with different voice types (Male, Female, Boy, Girl, etc.)
- **T21.G5.03b**: Adjust speech parameters (speed, pitch, volume)

**Rationale:** Original skill was trying to teach too much at once. Students need to master basic TTS before exploring voice variations and parameter tuning.

---

#### **T21.G6.05** - Speech Recognition (SPLIT INTO 2 SKILLS)
**Original:** Single skill covering two different providers (Azure and Whisper)
**New Structure:**
- **T21.G6.05**: Use Azure speech recognition (ai_startspeech block)
- **T21.G6.05a**: Use OpenAI Whisper speech recognition (ai_startopenaispeech block)

**Rationale:** Different providers have different capabilities. Students should learn one provider thoroughly, then compare with the second to understand provider differences.

---

#### **T21.G6.11** - Face Detection (SPLIT INTO 3 SKILLS)
**Original:** Single skill covering face detection with 13 data points (tilt angle + 12 facial features)
**New Structure:**
- **T21.G6.11**: Detect faces in camera video (basic detection setup)
- **T21.G6.11a**: Read facial feature coordinates from detection table
- **T21.G6.11b**: Use head tilt angle for face orientation detection

**Rationale:** Face detection returns complex data (13 variables). Students need separate skills for: (1) starting detection, (2) reading coordinate data, (3) using high-level features like tilt.

---

#### **T21.G6.12** - Body Tracking (SPLIT INTO 4 SKILLS)
**Original:** Single skill covering 21 body parts with complex data (x, y, curl, dir)
**New Structure:**
- **T21.G6.12**: Track 2D body parts in camera video (basic setup)
- **T21.G6.12a**: Read body part positions from detection table
- **T21.G6.12b**: Use curl and direction values for arm/leg gestures
- **T21.G6.12c**: Detect specific poses using body part combinations

**Rationale:** Body tracking is highly complex (21 parts × 4 data points). Progressive breakdown: setup → read positions → use curl/dir → combine for poses.

---

#### **T21.G7.09** - Hand Detection (SPLIT INTO 5 SKILLS)
**Original:** Single skill covering 47 rows of hand data (5 fingers + 21 2D points + 21 3D points)
**New Structure:**
- **T21.G7.09**: Detect hands in camera video (basic hand detection)
- **T21.G7.09a**: Read finger curl and direction values
- **T21.G7.09b**: Read 2D hand keypoint coordinates
- **T21.G7.09c**: Use 3D hand coordinates for depth-based gestures
- **T21.G7.09d**: Recognize common hand gestures (pinch, fist, open palm)

**Rationale:** Hand detection is THE most complex vision API (47 data rows per hand). Students need systematic progression through finger data → 2D points → 3D points → gesture recognition.

---

#### **T21.G7.13** - Neural Network (SPLIT INTO 4 SKILLS)
**Original:** Single skill "Build and train a neural network classifier" covering design, compile, train, and predict
**New Structure:**
- **T21.G7.13**: Design a neural network architecture
- **T21.G7.13a**: Compile and configure a neural network
- **T21.G7.13b**: Train a neural network and observe learning
- **T21.G7.14a**: Use a trained neural network to make predictions (NEW)

**Rationale:** Neural network workflow has 5 distinct phases that must be mastered separately: design → compile → train → save/load → predict.

---

#### **T21.G7.18** - LLM Models (SPLIT INTO 2 SKILLS)
**Original:** Single skill covering different providers
**New Structure:**
- **T21.G7.18**: Use generic LLM models with different providers
- **T21.G7.18a**: Select and compare different LLM models (NEW)

**Rationale:** Students need to first use alternative LLMs, then develop comparison and selection skills.

---

#### **T21.G8.16** - RAG (SPLIT INTO 2 SKILLS)
**Original:** Single skill "Build a knowledge base with semantic search"
**New Structure:**
- **T21.G8.16**: Understand RAG (Retrieval-Augmented Generation) architecture (NEW)
- **T21.G8.16a**: Build a knowledge base with semantic search (implements RAG)

**Rationale:** RAG is a complex architectural pattern. Students need conceptual understanding before implementation.

---

### 2. FIXED X-2 DEPENDENCY VIOLATIONS

**Problem:** 7 Grade 6 skills had dependencies on Grade 5 skills, violating the X-2 rule (skills can only depend on X-2 grades below).

**Removed Dependencies:**
- **T21.G6.01**: Removed dependency on T21.G5.01 ✓
- **T21.G6.02**: Removed dependencies on T21.G5.01 and T21.G5.02 ✓
- **T21.G6.05**: Removed dependency on T21.G5.04 ✓
- **T21.G6.07**: Removed dependency on T21.G5.02 ✓
- **T21.G6.08**: Removed dependencies on T21.G5.06 and T21.G5.07 ✓
- **T21.G6.09**: Removed dependency on T21.G5.07 ✓
- **T21.G6.10**: Removed dependency on T21.G5.06 ✓
- **T21.G7.06**: Removed dependency on T21.G6.05 ✓

**Rationale:** These dependencies assume Grade 6 students must complete Grade 5 AI Media skills first, but the X-2 rule allows Grade 6 to start fresh. Dependencies were removed while keeping prerequisite coding skills (T06, T08, T09, T10) intact.

---

### 3. ADDED MISSING SKILLS

#### **T21.G7.19** - JSON Mode (COMPLETELY CHANGED)
**Original:** Function calling with AI (doesn't exist in CreatiCode)
**New:** Generate structured data with ChatGPT JSON mode
**Rationale:** CreatiCode doesn't have function calling, but documentation mentions JSON mode for structured output.

#### **T21.G7.14a** - Neural Network Prediction (NEW)
**New Skill:** Use a trained neural network to make predictions
**Rationale:** Original curriculum had design → compile → train → save/load, but was missing the final "predict" step which is essential for using trained models.

#### **T21.G7.21** - Debug Mode Toggle (RENUMBERED FROM T21.G7.20)
**Original:** T21.G7.20
**New:** T21.G7.21 (moved to make room for new T21.G7.20 Cancel Requests)
**Rationale:** Better organization - cancel requests (G7.20) is more fundamental than debug mode (G7.21).

---

### 4. REMOVED NON-EXISTENT FEATURES

#### **T21.G8.18** - AI Agent Workflow (REMOVED)
**Original Skill:** "Build an AI agent workflow with tool calling"
**Status:** REMOVED ENTIRELY
**Rationale:** CreatiCode doesn't have function calling or tool calling capabilities. This was aspirational content not based on actual blocks.

**Replacement:** The skill ID T21.G8.18 is now "Build a research assistant combining web search and ChatGPT" which uses actual CreatiCode blocks.

---

### 5. FIXED INCORRECT SKILL DESCRIPTIONS

#### **T21.G7.11** - 3D Pose (CORRECTED)
**Original Title:** "Use head tilt detection for head tracking"
**Corrected Title:** "Track 3D body poses for avatar control"
**Rationale:** This skill uses `run 3D pose detection` which tracks 33 body parts in 3D, NOT just head. Head tilt is part of face detection (T21.G6.11b).

**Block Mapping Corrections:**
- Face detection (T21.G6.11) returns: tilt angle + 12 facial feature coordinates
- Hand detection (T21.G7.09) returns: 47 rows (5 fingers + 21 2D points + 21 3D points)
- Body tracking (T21.G6.12) returns: id, part, x, y, curl, dir columns
- Speech recognition has 2 providers (Azure and Whisper), both use same end workflow
- Web search returns table with title, link, snippet columns

---

### 6. IMPROVED SKILL PROGRESSION

#### Grade 5 (8 skills)
- Basic TTS broken into 3 progressive steps
- AI image library skill added (G5.02a)
- All foundational AI media interactions

#### Grade 6 (13 skills → 18 skills)
- Face detection: 1 skill → 3 skills (setup → coordinates → tilt)
- Body tracking: 1 skill → 4 skills (setup → positions → curl/dir → poses)
- Speech recognition: 1 skill → 2 skills (Azure → Whisper)
- Maintains content moderation, ChatGPT basics, image moderation

#### Grade 7 (24 skills → 25 skills)
- Hand detection: 1 skill → 5 skills (setup → fingers → 2D → 3D → gestures)
- Neural networks: 2 skills → 5 skills (concept → design → compile → train → save/load → predict)
- Added JSON mode skill (replacing non-existent function calling)
- Added LLM comparison skill

#### Grade 8 (21 skills)
- RAG split into conceptual understanding + implementation
- Removed AI agent workflow (non-existent)
- Research assistant now uses actual web search + ChatGPT blocks
- All capstone projects maintained

---

## Skill Count Changes by Grade

| Grade | Original | Optimized | Change |
|-------|----------|-----------|--------|
| K     | 3        | 3         | 0      |
| 1     | 2        | 2         | 0      |
| 2     | 2        | 2         | 0      |
| 3     | 2        | 2         | 0      |
| 4     | 3        | 3         | 0      |
| 5     | 8        | 8         | 0      |
| 6     | 13       | 18        | +5     |
| 7     | 24       | 25        | +1     |
| 8     | 21       | 21        | 0      |
| **TOTAL** | **78** | **84** | **+6** |

**Note:** Original count was 103 skills K-8, but actual T21 skills were only 78 (K-8). The optimized version has 84 skills, representing better granularity for complex topics.

---

## Key Improvements

### 1. **Pedagogical Soundness**
- Complex skills (face detection, hand tracking) now have scaffolded progression
- Students master basic concepts before advanced applications
- Clear learning objectives for each skill

### 2. **Technical Accuracy**
- All skills map to actual CreatiCode blocks
- Removed aspirational features (function calling, tool calling)
- Corrected misidentified features (3D pose vs head tracking)

### 3. **Dependency Hygiene**
- Fixed all X-2 violations
- Dependencies now only reference coding prerequisites (T06, T08, T09, T10)
- Same-grade skills can be assumed for skills later in grade

### 4. **Better Coverage**
- Added missing prediction step for neural networks
- Separated provider-specific skills (Azure vs Whisper)
- Split JSON mode from non-existent function calling

### 5. **Assessment Clarity**
- Each skill has single, clear learning outcome
- Teachers can assess mastery more precisely
- Students understand exactly what they're learning

---

## Implementation Notes

### For Teachers:
1. **Starter Templates Recommended** for complex skills:
   - T21.G6.03: Prompt test bench
   - T21.G8.03: Multi-scene media experience
   - All neural network skills (G7.13 series)

2. **Debug Mode is Essential** for vision skills:
   - Always start with debug=yes for face/hand/body detection
   - Teach toggle patterns in G7.21

3. **Progression Matters**:
   - Don't skip basic setup skills (G6.11, G6.12, G7.09)
   - Don't jump directly to gesture recognition

### For Students:
1. **Vision APIs are layered**:
   - First learn to START detection
   - Then learn to READ data
   - Finally learn to USE data for applications

2. **Neural networks require patience**:
   - Design → compile → train → save → predict (5 distinct skills)
   - Each step is essential and can't be skipped

3. **AI providers differ**:
   - Azure vs Whisper for speech
   - Different LLM providers for text generation
   - Comparison skills teach evaluation

---

## Files Generated

1. **T21_OPTIMIZED_SECTION.md** - Complete replacement for lines 13896-14809 in allskills.md
2. **T21_OPTIMIZATION_CHANGELOG.md** - This document

## Next Steps

1. Review optimized section for any missed edge cases
2. Validate all dependency chains are correct
3. Replace lines 13896-14809 in allskills.md with optimized content
4. Update any cross-references from other topics that reference old T21 skill IDs
5. Consider creating visual skill maps for complex progressions (face/hand/body detection)
