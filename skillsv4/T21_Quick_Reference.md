# T21 (AI Media) - Quick Reference Guide

## Topic Overview
**T21 – AI Media** teaches students how to use AI tools for generating, analyzing, and working with media content including images, text, speech, and video. Progresses from basic AI literacy (K-2) through hands-on implementation (3-6) to advanced integration and ethics (7-8).

---

## Grade-by-Grade Quick View

### Kindergarten (3 skills) - Unplugged
- Identify AI-generated images
- Match images to descriptions
- Identify AI-capable devices

### Grade 1 (2 skills) - Unplugged
- Build descriptions with word cards
- Privacy awareness with AI

### Grade 2 (2 skills) - Unplugged
- Improve prompts with details
- Understand AI oversight needs

### Grade 3 (2 skills) - Transition
- Distinguish AI vs. recorded media
- Describe ideas for AI creation

### Grade 4 (3 skills) - Concepts
- G4.01: Safe, specific prompts
- G4.02: Describe AI media experiences
- G4.03: AI strengths and limits

### Grade 5 (8 skills) - First Hands-On
- G5.01: AI vs. hand-made decisions
- G5.02: **DALL-E image generation**
- G5.02a: **AI image library search**
- G5.03: **Text-to-speech**
- G5.04: Speech-to-text understanding (observation)
- G5.05: Why AI needs safety review
- G5.06: **ChatGPT basics**
- G5.07: ChatGPT parameters

### Grade 6 (13 skills) - Core Implementation
- G6.01: Plan mixed-source assets
- G6.02: Structured prompts
- G6.03: **Prompt test bench**
- G6.04: Iteration and debugging
- G6.05: **Speech recognition** (Azure/Whisper)
- G6.06: **Text moderation**
- G6.07: **Image moderation**
- G6.08: **ChatGPT for stories**
- G6.09: Temperature experiments
- G6.10: **System instructions**
- G6.11: **Face detection**
- G6.12: **2D body tracking**
- G6.13: **Stop camera detection** ⭐NEW

### Grade 7 (24 skills) - Advanced Integration
**AI Workflows:**
- G7.01: Prompt template library
- G7.02: ChatGPT-enhanced prompts
- G7.03: Bias auditing
- G7.04: Hybrid AI-human workflows
- G7.05: Sync visuals + narration

**Speech & Audio:**
- G7.06: **Continuous speech recognition**

**Vision & Multimodal:**
- G7.07: **ChatGPT vision**
- G7.07a: **File attachments**
- G7.08: **Multi-thread conversations**
- G7.09: **Hand tracking**
- G7.10: Pose-based game
- G7.11: **3D pose tracking**

**Machine Learning:**
- G7.12: Neural network concepts
- G7.13: Design NN architecture
- G7.13a: Compile NN
- G7.13b: Train NN
- G7.14: Save/load NN models
- G7.14a: **NN predictions**
- G7.15: KNN concepts
- G7.16: **Create KNN classifier**

**NLP & Advanced:**
- G7.17: **Parts-of-speech tagging**
- G7.18: **Generic LLM models** ⭐NEW
- G7.19: **Cancel requests** ⭐NEW
- G7.20: **Debug mode toggle** ⭐NEW

### Grade 8 (24 skills) - Capstone & Ethics
**Production Systems:**
- G8.01: Generative art widget with guardrails
- G8.02: Approval pipeline
- G8.03: Multi-scene media experience
- G8.04: Ethical guidelines

**Advanced Applications:**
- G8.05: Voice-controlled assistant
- G8.06: **Multi-turn chatbot**
- G8.07: **Web search + ChatGPT**
- G8.08: Gesture-controlled app
- G8.09: Fitness tracker

**Machine Learning Applications:**
- G8.10: NN for number recognition
- G8.11: NN for pattern classification
- G8.12: Evaluate NN performance
- G8.13: Real-time KNN

**Semantic Search:**
- G8.14: **Create semantic database**
- G8.15: **Semantic search**
- G8.16: **Knowledge base (RAG)**

**Web Integration:**
- G8.17: **Web search basics**
- G8.18: Research assistant

**AI Ethics & Safety:**
- G8.19: **AI hallucinations** ⭐NEW
- G8.20: **Prompt injection prevention** ⭐NEW
- G8.21: **Cost management** ⭐NEW

⭐ = New skills added in Phase 1

---

## Key CreatiCode Blocks by Category

### Image Generation
```
OpenAI DALL-E: generate image with request [DESCRIPTION] resolution [RESOLUTION v]
→ Returns: Image URL (256x256, 512x512, or 1024x1024)

search for AI image of [TYPE v] with query [QUERY]
→ TYPE: Object, Character, Backdrop
```

### Text Generation
```
OpenAI ChatGPT: request [PROMPT] result [VARIABLE v] mode [MODE v] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE v]
→ MODE: streaming/waiting
→ SESSION: new chat/continue

OpenAI ChatGPT: system request [PROMPT] session [SESSION v] result [VARIABLE v] temperature [T]

LLM model [PROVIDER] request [PROMPT] result [VARIABLE v] mode [MODE v] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE v]
→ PROVIDER: small/large models

OpenAI ChatGPT: cancel request
```

### Speech Recognition
```
start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]  (Azure)
OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]  (Whisper)
end speech recognition
text from speech  (reporter)
clear speech text

start continuous speech recognition in [LANGUAGE v] into list [LISTNAME v]
stop continuous speech recognition
```

### Text-to-Speech
```
say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]
→ VOICE: Male, Female, Boy, Girl, Male2, Female2, Male3, Female3
→ Parameters: 0.5-2.0 range

stop speaking
```

### Computer Vision
```
run face detection debug [yes/no] and write into table [TABLE v]
→ Output: id, variable (tilt, eye/ear/nose/mouth x/y), value

run 2D body part recognition single person [yes/no] table [TABLE v] debug [yes/no]
→ Output: id, part, x, y, curl, dir
→ 17 core parts + 4 aggregate (arms/legs)

run 3D pose detection debug [yes/no] table [TABLE v]
→ Output: 33 body landmarks with x, y, z

run hand detection table [TABLE v] debug [yes/no] show video [yes/no]
→ Output: 47 data points per hand (5 fingers + 21 2D + 21 3D)

set debug mode [DODEBUG v]
→ Toggle debug visualization during runtime
```

### Multimodal AI
```
attach costume [COSTUMENAME] to chat
attach files to chat  (reporter - file selection dialog)
attach file from Google Drive [URL] to chat

select chatbot [BOTID v]
→ Switch between 4 parallel chat threads (1-4)
```

### Content Moderation
```
get moderation result for [TEXT]
get moderation result for image at URL [INPUT]
get moderation result for costume named [INPUT]
→ Returns: Pass/Fail
```

### Machine Learning - Neural Networks
```
create NN model named [NAME]
add layer to NN model [NAME] input shape (SHAPESIZE) output size (OUTPUTSIZE) activation [FUNCTION v]
→ FUNCTION: relu, sigmoid, tanh, softmax

compile NN model [NAME] loss [LOSSFUNCTION v] optimizer [OPTIMIZER v] learning rate (RATE)
→ LOSS: meanSquaredError, categoricalCrossentropy
→ OPTIMIZER: adam, sgd, adagrad

train NN model [NAME] using table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN] batch size [BATCHSIZE] epochs [EPOCHS]

predict using NN model [NAME] for table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN]

save NN model named [NAME]
load NN model named [NAME]
```

### Machine Learning - KNN
```
create KNN number classifier from table [TABLENAME v] K [K] named [NAME]
predict for table [TABLENAME v] with classifier [NAME] show neighbors [yes/no]
```

### NLP
```
analyze sentence [SENTENCE] and write into table [TABLENAME v]
→ Output: TEXT, LEMMA, TYPE, PERSON, OFFSET, LABEL, DEPENDS
```

### Semantic Search
```
create semantic database from table [TABLE v]
→ Requires 'key' column + optional metadata

search semantic database with [QUERY] store top (K) in table [TABLE v]
search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE v]
→ WHERE: SQL-like conditions (AND/OR)
→ Returns: similarity score (0-1, >0.7 typically relevant)
```

### Web Search
```
web search [QUERY] store top (K) in table [TABLE v]
→ Output: title, link, snippet
```

---

## Common Patterns

### Basic ChatGPT Flow
1. Ask question with `OpenAI ChatGPT: request`
2. Display result from variable
3. Continue conversation with `session: continue`

### Image Generation Flow
1. Write descriptive prompt
2. Call DALL-E block
3. Load returned image URL
4. Moderate if user-generated

### Speech Recognition Flow
1. `start recognizing speech`
2. User speaks
3. `end speech recognition`
4. Read `text from speech` reporter

### Vision Detection Flow
1. `run [type] detection debug [yes] table [TABLE]`
2. Read table for positions/values
3. Use data to trigger actions
4. Stop detection when done (NEW!)
5. Toggle debug mode as needed (NEW!)

### Neural Network Flow
1. Create model
2. Add layers
3. Compile with loss/optimizer
4. Train with data table
5. Save model
6. Load model (later)
7. Predict on new data (NEW!)

### Semantic Search (RAG) Flow
1. Create database from knowledge table
2. User asks question
3. Search database for relevant entries
4. Send results to ChatGPT as context
5. ChatGPT synthesizes answer
6. Display with sources

---

## Safety & Ethics Checklist

✅ **Always moderate user input** (G6.06, G6.07)
✅ **Check AI outputs before display** (G5.05, G8.01, G8.02)
✅ **Test for bias** (G7.03)
✅ **Fact-check AI responses** (G8.07, G8.19)
✅ **Protect against prompt injection** (G8.20)
✅ **Track and optimize costs** (G8.21)
✅ **Stop detection when not needed** (G6.13)
✅ **Implement cancel options** (G7.19)
✅ **Develop ethical guidelines** (G8.04)

---

## Skill Dependencies Quick Lookup

### Grade 4 Chain
G4.01 → G4.02 → G4.03 (linear progression)

### Grade 5 Branches
- Image: G4.01 → G5.02 → G5.02a
- Safety: G4.01, G4.03 → G5.01, G5.05
- ChatGPT: G5.06 → G5.07

### Grade 6 Integration
- Prompting: G5.01, G5.02 → G6.02, G6.03, G6.04
- Speech: G5.04 → G6.05
- Safety: G5.05 → G6.06 → G6.07
- ChatGPT: G5.06, G5.07 → G6.08, G6.09, G6.10

### Grade 7 Advanced
- Templates: G6.03, G6.04 → G7.01
- AI Workflows: G6.04, G6.08 → G7.02
- Vision: G6.12 → G7.09, G7.10, G7.11
- ML: G7.12 → G7.13 → G7.13a → G7.13b → G7.14 → G7.14a
- ML: G7.12 → G7.15 → G7.16

### Grade 8 Capstones
- Production: G7.01, G6.06 → G8.01, G8.02
- Multi-scene: G7.02, G7.05 → G8.03
- Web+AI: G6.08 → G8.07 → G8.18, G8.19
- Security: G6.06, G8.06 → G8.20
- Costs: G7.18, G8.02 → G8.21

---

## Phase 1 Improvements Summary

**10 New Skills Added:**
1. G6.13 - Stop camera detection
2. G7.18 - Generic LLM models
3. G7.19 - Cancel requests
4. G7.20 - Debug mode toggle
5. G8.19 - AI hallucinations
6. G8.20 - Prompt injection
7. G8.21 - Cost management

**Major Fixes:**
- ✅ DALL-E block syntax corrected
- ✅ Speech recognition providers clarified
- ✅ G4 dependency chain fixed
- ✅ X-2 rule violations resolved (11 skills)
- ✅ Same-grade dependencies removed
- ✅ Redundant dependencies eliminated

**Coverage Gaps Filled:**
- ✅ Resource management (stop/start detection)
- ✅ Multi-provider LLM support
- ✅ Request cancellation
- ✅ Debug control
- ✅ AI reliability/security awareness
- ✅ Cost consciousness

---

## Quick Start by Grade Level

**K-2:** Picture-based activities, no coding required
**Grade 3-4:** Conceptual foundation, light coding
**Grade 5:** First hands-on with DALL-E, ChatGPT, TTS
**Grade 6:** Core implementations, all major AI features introduced
**Grade 7:** Advanced integration, ML introduction, professional workflows
**Grade 8:** Production systems, ethics, security, complex integrations

---

*For detailed descriptions, see T21_Phase1_Summary.md or skillsv4/allskills.md*
