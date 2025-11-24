# T21 Skill ID Mapping: Original → Optimized

## Skills That Were Split (1 → Multiple)

### T21.G5.03: Text-to-Speech
```
OLD: T21.G5.03 (covered voice types, languages, and parameters)

NEW:
├── T21.G5.03  - Use basic text-to-speech with default settings
├── T21.G5.03a - Experiment with different voice types
└── T21.G5.03b - Adjust speech parameters (speed, pitch, volume)
```

### T21.G6.05: Speech Recognition
```
OLD: T21.G6.05 (covered both Azure and Whisper)

NEW:
├── T21.G6.05  - Use Azure speech recognition (ai_startspeech block)
└── T21.G6.05a - Use OpenAI Whisper speech recognition (ai_startopenaispeech block)
```

### T21.G6.11: Face Detection
```
OLD: T21.G6.11 (covered detection setup and all 13 data points)

NEW:
├── T21.G6.11  - Detect faces in camera video (basic detection setup)
├── T21.G6.11a - Read facial feature coordinates from detection table
└── T21.G6.11b - Use head tilt angle for face orientation detection
```

### T21.G6.12: Body Tracking
```
OLD: T21.G6.12 (covered detection and all body part data)

NEW:
├── T21.G6.12  - Track 2D body parts in camera video (basic setup)
├── T21.G6.12a - Read body part positions from detection table
├── T21.G6.12b - Use curl and direction values for arm/leg gestures
└── T21.G6.12c - Detect specific poses using body part combinations
```

### T21.G7.09: Hand Detection
```
OLD: T21.G7.09 (covered detection and all 47 rows of data)

NEW:
├── T21.G7.09  - Detect hands in camera video (basic hand detection)
├── T21.G7.09a - Read finger curl and direction values
├── T21.G7.09b - Read 2D hand keypoint coordinates
├── T21.G7.09c - Use 3D hand coordinates for depth-based gestures
└── T21.G7.09d - Recognize common hand gestures (pinch, fist, open palm)
```

### T21.G7.13-14: Neural Networks
```
OLD:
├── T21.G7.13 - Build and train a neural network classifier
└── T21.G7.14 - Save and load trained neural network models

NEW:
├── T21.G7.13  - Design a neural network architecture
├── T21.G7.13a - Compile and configure a neural network
├── T21.G7.13b - Train a neural network and observe learning
├── T21.G7.14  - Save and load trained neural network models
└── T21.G7.14a - Use a trained neural network to make predictions (NEW)
```

### T21.G7.18: LLM Models
```
OLD: T21.G7.18 (covered using different providers)

NEW:
├── T21.G7.18  - Use generic LLM models with different providers
└── T21.G7.18a - Select and compare different LLM models (NEW)
```

### T21.G8.16: RAG / Knowledge Base
```
OLD: T21.G8.16 - Build a knowledge base with semantic search

NEW:
├── T21.G8.16  - Understand RAG (Retrieval-Augmented Generation) architecture (NEW)
└── T21.G8.16a - Build a knowledge base with semantic search (implements RAG)
```

---

## Skills That Were Added

### Grade 5
- **T21.G5.02a** - Search AI image library for pre-made assets (NEW)
  - Previously missing skill for ai_xoimagereporter block

- **T21.G5.03a** - Experiment with different voice types (SPLIT from G5.03)

- **T21.G5.03b** - Adjust speech parameters (SPLIT from G5.03)

### Grade 6
- **T21.G6.05a** - Use OpenAI Whisper speech recognition (SPLIT from G6.05)

- **T21.G6.11a** - Read facial feature coordinates from detection table (SPLIT from G6.11)

- **T21.G6.11b** - Use head tilt angle for face orientation detection (SPLIT from G6.11)

- **T21.G6.12a** - Read body part positions from detection table (SPLIT from G6.12)

- **T21.G6.12b** - Use curl and direction values for arm/leg gestures (SPLIT from G6.12)

- **T21.G6.12c** - Detect specific poses using body part combinations (SPLIT from G6.12)

### Grade 7
- **T21.G7.07a** - Attach files and documents to ChatGPT conversations (NEW)
  - Previously missing: attachfilestochat and attachgooglefiletochat blocks

- **T21.G7.09a** - Read finger curl and direction values (SPLIT from G7.09)

- **T21.G7.09b** - Read 2D hand keypoint coordinates (SPLIT from G7.09)

- **T21.G7.09c** - Use 3D hand coordinates for depth-based gestures (SPLIT from G7.09)

- **T21.G7.09d** - Recognize common hand gestures (SPLIT from G7.09)

- **T21.G7.13a** - Compile and configure a neural network (SPLIT from G7.13)

- **T21.G7.13b** - Train a neural network and observe learning (SPLIT from G7.13)

- **T21.G7.14a** - Use a trained neural network to make predictions (NEW)
  - Previously missing: predict_by_model block

- **T21.G7.18a** - Select and compare different LLM models (SPLIT from G7.18)

- **T21.G7.19** - Generate structured data with ChatGPT JSON mode (CHANGED)
  - Was: Function calling with AI (doesn't exist)
  - Now: JSON mode for structured output (exists in blocks)

- **T21.G7.21** - Toggle AI debug mode during development (RENUMBERED)
  - Was T21.G7.20, moved to make room for G7.20 Cancel

### Grade 8
- **T21.G8.16** - Understand RAG architecture (NEW, conceptual)

- **T21.G8.16a** - Build a knowledge base with semantic search (was G8.16, now implements RAG)

---

## Skills That Were Removed

### Grade 7
- **OLD T21.G7.19** - Use AI function calling to access external tools
  - **REASON:** Function calling doesn't exist in CreatiCode
  - **REPLACEMENT:** T21.G7.19 now teaches JSON mode for structured output

### Grade 8
- **OLD T21.G8.18** - Build an AI agent workflow with tool calling
  - **REASON:** Tool calling doesn't exist in CreatiCode
  - **REPLACEMENT:** T21.G8.18 now teaches building a research assistant with web search + ChatGPT (actual blocks)

---

## Skills That Were Corrected

### T21.G7.11: TITLE CORRECTED
```
OLD: "Use head tilt detection for head tracking"
NEW: "Track 3D body poses for avatar control"

REASON: This skill uses `run 3D pose detection` which tracks 33 body parts in 3D,
        NOT just head. Head tilt is part of face detection (T21.G6.11b).
```

---

## Skills With Dependency Changes

### Removed X-2 Violations (Grade 6 skills depending on Grade 5)

**T21.G6.01** - Plan a mixed-source asset kit
- REMOVED: T21.G5.01
- KEPT: T21.G4.01, T21.G5.01 (different - this is same-grade)

**T21.G6.02** - Write structured prompts
- REMOVED: T21.G5.01, T21.G5.02
- KEPT: Same-grade dependencies only

**T21.G6.05** - Use Azure speech recognition
- REMOVED: T21.G5.04 (was understanding speech-to-text)
- KEPT: T06.G4.01, T21.G5.04 as same-grade assumed

**T21.G6.07** - Use image moderation
- REMOVED: T21.G5.02 (generate AI image)
- KEPT: T21.G6.06 (same-grade), other dependencies

**T21.G6.08** - Use ChatGPT to generate story text
- REMOVED: T21.G5.06, T21.G5.07
- KEPT: Same-grade assumptions only

**T21.G6.09** - Compare ChatGPT responses with different temperatures
- REMOVED: T21.G5.07
- KEPT: Same-grade dependencies

**T21.G6.10** - Use system instructions to guide ChatGPT
- REMOVED: T21.G5.06
- KEPT: Same-grade dependencies

### Removed Invalid Dependency

**T21.G7.12** - Understand neural networks
- REMOVED: T21.G4.03 (identify strengths/limits of AI image generation)
- REASON: Conceptual foundation skill doesn't require specific coding prerequisites
- NEW: No dependencies (pure conceptual skill)

---

## Quick Reference: "Where did skill X go?"

| Looking for... | Find it at... |
|----------------|---------------|
| T21.G5.03 (old, covered everything) | T21.G5.03, T21.G5.03a, T21.G5.03b |
| T21.G6.05 (old, both providers) | T21.G6.05, T21.G6.05a |
| T21.G6.11 (old, all face data) | T21.G6.11, T21.G6.11a, T21.G6.11b |
| T21.G6.12 (old, all body data) | T21.G6.12, T21.G6.12a, T21.G6.12b, T21.G6.12c |
| T21.G7.09 (old, all hand data) | T21.G7.09, T21.G7.09a, T21.G7.09b, T21.G7.09c, T21.G7.09d |
| T21.G7.13 (old, build & train) | T21.G7.13, T21.G7.13a, T21.G7.13b |
| T21.G7.14 (old, save & load) | T21.G7.14 (same), T21.G7.14a (predict - NEW) |
| T21.G7.19 (old, function calling) | T21.G7.19 (JSON mode - CHANGED) |
| T21.G7.20 (old, debug toggle) | T21.G7.21 (renumbered) |
| T21.G8.16 (old, build knowledge base) | T21.G8.16 (understand RAG), T21.G8.16a (implement) |
| T21.G8.18 (old, AI agent workflow) | REMOVED - didn't exist in CreatiCode |

---

## Migration Guide for Existing Curricula

### If you taught the old T21.G5.03 (TTS):
Your students learned everything. Map to:
- Basic usage → T21.G5.03 ✓
- Voice types → T21.G5.03a ✓
- Parameters → T21.G5.03b ✓

### If you taught the old T21.G6.11 (Face):
Your students learned everything. Map to:
- Detection setup → T21.G6.11 ✓
- Reading coordinates → T21.G6.11a ✓
- Using tilt angle → T21.G6.11b ✓

### If you taught the old T21.G7.09 (Hand):
Your students learned everything. Map to:
- Detection setup → T21.G7.09 ✓
- Finger curl/dir → T21.G7.09a ✓
- 2D keypoints → T21.G7.09b ✓
- 3D coordinates → T21.G7.09c ✓
- Gesture recognition → T21.G7.09d ✓

### If you taught the old T21.G7.19 (Function Calling):
**WARNING:** This feature doesn't exist in CreatiCode.
- If you used actual blocks → You likely used something else
- NEW T21.G7.19 → JSON mode (different feature)
- Check what blocks you actually used

### If you taught the old T21.G8.18 (AI Agents):
**WARNING:** Tool calling doesn't exist in CreatiCode.
- NEW T21.G8.18 → Research assistant (web search + ChatGPT)
- This is a real, implementable capstone project

---

## Summary Statistics

- **Total Skills**: 78 → 84 (+6)
- **Skills Split**: 8 skills → 27 skills
- **Skills Added**: 11 new skills
- **Skills Removed**: 2 skills (non-existent features)
- **Skills Corrected**: 1 skill (wrong description)
- **Dependencies Fixed**: 8 X-2 violations resolved
