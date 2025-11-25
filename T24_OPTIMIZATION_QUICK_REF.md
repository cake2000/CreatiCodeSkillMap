# T24 Optimization Quick Reference

## Skills Requiring Immediate Breakdown (Priority 1)

### 1. ChatGPT Parameters (G5.07.01-03) → Split into 5-6 skills
**Current:** 3 skills cover all ChatGPT parameters
**Issue:** Missing session management, system instructions, cancel
**New Skills Needed:**
- T24.G5.07.04: Adjust response length (max tokens)
- T24.G5.07.05: Understand session continuity
- T24.G5.07.06: Cancel requests
- T24.G6.08.02: System instructions
- T24.G6.08.03: Multiple chatbot sessions (1-4)

---

### 2. Face Detection (G5.09) → Split into 3-4 skills
**Current:** 1 skill covers block + 13-row table
**Issue:** Too much at once - block, table, coordinates
**New Skills Needed:**
- T24.G5.09.01: Enable detection + debug
- T24.G5.09.02: Understand table (13 rows)
- T24.G5.09.03: Read facial features

---

### 3. Hand Detection (G6.10.01-03) → Split into 6 skills
**Current:** 3 skills for 47-row complex table
**Issue:** 3 sections (fingers, 2D, 3D) need separate skills
**New Skills Needed:**
- T24.G6.10.01: Enable hand detection
- T24.G6.10.02: Table structure (3 sections)
- T24.G6.10.03: Finger curl & direction
- T24.G6.10.04: 2D keypoints
- T24.G6.10.05: 3D keypoints
- T24.G6.10.06: Single-hand gestures

---

### 4. 3D Pose Detection (G7.08.01-04) → Split into 9 skills
**Current:** 4 skills for 33 body parts × 3D coordinates
**Issue:** 99 data points, math calculations compressed
**New Skills Needed:**
- T24.G7.08.01: Enable + coordinate system
- T24.G7.08.02: Table structure (33 parts)
- T24.G7.08.03: Upper body positions
- T24.G7.08.04: Lower body positions
- T24.G7.08.05: 3D distance calculations
- T24.G7.08.06: Angle calculations
- T24.G7.08.07: Simple poses
- T24.G7.08.08: Complex poses
- T24.G7.08.09: Full-body games

---

### 5. Neural Networks (G8.08-09) → Split into 13 skills
**Current:** 6 skills for create/compile/train/save
**Issue:** Missing predictions! Missing activation/loss/optimizer explanations
**New Skills Needed:**
- T24.G8.08.01: Create model
- T24.G8.08.02: Add layers
- T24.G8.08.03: Activation functions
- T24.G8.08.04: Loss functions
- T24.G8.08.05: Optimizers
- T24.G8.08.06: Compile
- T24.G8.09.01: Prepare datasets
- T24.G8.09.02: Batch size
- T24.G8.09.03: Epochs
- T24.G8.09.04: Train & monitor
- T24.G8.09.05: **Make predictions** (MISSING!)
- T24.G8.09.06: **Evaluate accuracy** (MISSING!)
- T24.G8.09.07: Save/load

---

## Critical Missing Blocks (Priority 1)

### 1. Neural Network Predictions - COMPLETELY MISSING
**Block:** `predict with NN model [NAME] using table...`
**Impact:** Students train but never use models!
**Add:** T24.G8.09.05 + T24.G8.09.06

### 2. ChatGPT System Instructions - NO DEDICATED SKILL
**Block:** `ChatGPT: system request [PROMPT]...`
**Impact:** Can't configure chatbot personality/rules
**Add:** T24.G6.08.02

### 3. Multiple Chatbot Sessions - BARELY COVERED
**Block:** `select ChatGPT bot [1/2/3/4]`
**Impact:** Used in G7.06 but never taught fundamentals
**Add:** T24.G6.08.03

---

## Critical Scaffolding Gaps (Priority 1)

### Gap 1: No Bridge to Multi-Turn ChatGPT
**Jump:** G5 basic → G6 sessions → G6 multi-turn
**Missing:** Simple two-turn practice
**Add:** T24.G6.07.05

### Gap 2: No CV Coordinate Practice
**Jump:** Coordinate system → 13-row face tables
**Missing:** Reading simple x,y from tables
**Add:** T24.G5.08.02

### Gap 3: No Table Practice Before CV
**Jump:** Basic CRUD → Complex multi-row CV tables
**Missing:** Reading/filtering multi-row data
**Add:** T24.G5.05.02

### Gap 4: No NN Architecture Practice
**Jump:** Concepts → Coding
**Missing:** Analyzing pre-built architectures
**Add:** T24.G7.15.01

---

## Moderate Priority Additions (Priority 2)

### Semantic Search (G8.10-11) → +4 skills
- T24.G8.10.01: Vector embeddings
- T24.G8.10.03: SQL-like filters
- T24.G8.11.04: Semantic vs keyword comparison
- T24.G8.11.05: ChatGPT without context

### RAG Systems (G8.12) → +4 skills
- T24.G8.12.03: Add web search
- T24.G8.12.04: Rank/deduplicate
- T24.G8.12.05: Format context
- T24.G8.12.07: Domain chatbots

### Body Detection (G6.11) → +3 skills
- T24.G6.11.01-06: Break current 3 into 6 skills
- Better progression for 21-row tables

---

## Minor Additions (Priority 3)

1. T24.G5.07.06: Cancel ChatGPT requests
2. T24.G7.13.01: Parse multiple file paths
3. T24.G7.15.02: Compare KNN vs NN
4. T24.G6.07.04: Content validation systems
5. T24.G8.01.04: LLM model selection

---

## Overall Metrics

### Current State
- **Total Skills:** 107
- **Grade Distribution:** GK(3), G1(3), G2(4), G3(6), G4(8), G5(18), G6(21), G7(16), G8(24)

### Recommended New State
- **New Skills to Add:** ~45-55
- **New Total:** ~152-162 skills
- **Grade Distribution:** GK(3), G1(3), G2(4), G3(6-8), G4(8-9), G5(25-28), G6(28-32), G7(24-28), G8(38-45)

### Quality Assessment
- ✅ No circular dependencies
- ✅ Excellent K-2 unplugged approach
- ✅ Appropriate grade progression
- ⚠️ Some skills too broad
- ⚠️ Missing critical blocks (NN prediction)
- ⚠️ Scaffolding gaps before complex features

**Overall:** 85% complete → 95%+ with additions

---

## Implementation Priority

1. **Immediate (Priority 1):** 6-8 critical missing blocks + 4 scaffolding gaps = ~10-12 skills
2. **Short-term (Priority 2):** Break down overly broad skills = ~20-30 skills
3. **Long-term (Priority 3):** Enhancement skills = ~15-20 skills

**Estimated Work:**
- Priority 1: 2-3 weeks
- Priority 2: 4-6 weeks
- Priority 3: 3-4 weeks
- **Total: 9-13 weeks for complete optimization**

---

## Block Coverage Summary

### ✅ Fully Covered (Good)
- Speech recognition (Azure + Whisper)
- Text-to-speech
- AI image search
- DALL-E generation
- Face detection
- Hand detection (needs breakdown)
- 2D body detection (needs breakdown)
- 3D pose detection (needs breakdown)
- KNN classifier
- Moderation (3 types)
- Web search
- Sentence analysis
- Semantic database (needs expansion)

### ⚠️ Partially Covered (Needs Work)
- ChatGPT (missing system instructions, cancel, sessions)
- Neural networks (missing prediction, evaluation)
- RAG (needs more detail)
- File attachments (missing multi-file handling)

### ❌ Not Covered
- LLM model selection (small/large)
- Debug mode toggle as standalone skill

---

*See T24_OPTIMIZATION_ANALYSIS.md for complete details*
