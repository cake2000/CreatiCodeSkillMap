# T24 COMPREHENSIVE ANALYSIS REPORT
**Topic: T24 - XO & Generative AI Practices**
**Date: 2025-11-21**
**Scope: Skills GK.01 through G8.05 (41 skills)**

---

## EXECUTIVE SUMMARY

This analysis examines all 41 T24 skills across five critical dimensions:
1. Missing AI block coverage
2. Skill quality issues
3. Grade-appropriateness
4. Scaffolding and progression
5. Dependency issues

**Key Findings:**
- **CRITICAL GAPS**: Multiple AI block categories completely missing from T24
- **SCOPE ISSUE**: T24 focuses exclusively on XO (coding assistant) and overlooks many AI perception/ML blocks
- **COVERAGE**: Many AI blocks are already well-covered in T21 (AI Media), T22 (Chatbots), and T23 (AI Perception)
- **QUALITY**: Generally strong skill descriptions with clear implementation details
- **DEPENDENCIES**: Several violations of X-2 rule and unnecessary cross-topic dependencies

---

## 1. MISSING SKILLS / GAPS IN COVERAGE

### 1.1 CRITICAL: AI Blocks Completely Missing from T24

#### A. TensorFlow Neural Network Blocks (6 blocks NOT COVERED in T24)
**Location**: These are covered in T21.G7.13-G7.14 and T21.G8.05-G8.06
- `create neural network model named [NAME]`
- `add layer to model [NAME]`
- `compile model [NAME]`
- `train model [NAME] with data`
- `predict with model [NAME]`
- Neural network evaluation/testing blocks

**Status**: ✓ Covered in T21, NOT in T24 (appropriate - these are AI Media blocks, not XO-related)

---

#### B. KNN Classifier Blocks (2 blocks NOT COVERED in T24)
**Location**: Covered in T21.G7.15-G7.16 and T21.G8.15
- `create KNN number classifier from table [TABLE] K [K] named [NAME]`
- `use KNN classifier [NAME] to predict label from table [TABLE] show neighbors [yes/no]`

**Status**: ✓ Covered in T21, NOT in T24 (appropriate - these are ML classification blocks)

---

#### C. Semantic Search Blocks (3 blocks NOT COVERED in T24)
**Location**: Covered in T21.G8.14-G8.16 and T22.G8.01
- `create semantic database from table [TABLE]`
- `search semantic database with [QUERY] store top (K) in table [TABLE]`
- `search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE]`

**Status**: ✓ Covered in T21/T22, NOT in T24 (appropriate - these are RAG/database blocks)

---

#### D. Web Search Block (1 block NOT COVERED in T24)
**Location**: Covered in T21.G8.17-G8.18 and T22.G8.05
- `web search [QUERY] store top (K) in table [TABLE]`

**Status**: ✓ Covered in T21/T22, NOT in T24 (appropriate - not XO-specific)

---

#### E. Computer Vision Blocks - Face Detection (NOT COVERED in T24)
**Location**: Covered in T23.G6.09 and T23.G7.05
- `run face detection debug [yes/no] and write into table [TABLE]`
- `run face AR camera with effect [EFFECT_NAME]`

**Status**: ✓ Covered in T23, NOT in T24 (appropriate - these are AI Perception blocks)

---

#### F. Computer Vision Blocks - Body/Hand Detection (NOT COVERED in T24)
**Location**: Covered in T23.G5.07-G5.08, G6.08, G7.04, G8.06
- Body pose detection blocks (2D and 3D)
- Hand detection blocks
- Gesture recognition blocks

**Status**: ✓ Covered in T23, NOT in T24 (appropriate - these are AI Perception blocks)

---

### 1.2 MISSING: Multiple ChatGPT Session Management

#### Issue ID: T24-MISSING-001
**Block**: `select chatbot [1/2/3/4]`
**Current Coverage**: T22.G6.06 and T22.G8.02 cover multiple chatbot sessions
**T24 Coverage**: NONE

**Problem**: T24 never teaches students how to use multiple chatbot sessions, which would be valuable for:
- Comparing XO responses with different personas
- Having XO "debate" with itself
- Running multiple AI assistants simultaneously

**Recommended Fix**: Add skill at G7 or G8 level
- **ID**: T24.G7.06
- **Skill**: Compare XO responses using multiple sessions
- **Description**: Students use the `select chatbot [1/2/3/4]` block to create two XO sessions with different system instructions (e.g., "focus on readability" vs "focus on efficiency"). They send the same code review request to both, compare the responses, and synthesize a combined improvement plan.

---

### 1.3 MISSING: Attaching Files/Images to Chat

#### Issue ID: T24-MISSING-002
**Blocks**:
- `attach costume [NAME] to chat`
- `attach files to chat`
- `attach file from Google Drive [URL] to chat`

**Current Coverage**: T22.G7.06 covers these for chatbots
**T24 Coverage**: NONE

**Problem**: XO can analyze images and files, but T24 never teaches this capability. Students could:
- Send screenshots of their code to XO for debugging
- Attach sprite costumes for XO to suggest improvements
- Send project assets for XO to evaluate theme consistency

**Recommended Fix**: Add skill at G6 or G7 level
- **ID**: T24.G6.09
- **Skill**: Send screenshots and assets to XO for feedback
- **Description**: Students use the `attach costume [NAME] to chat` block to send sprite costumes or backdrops to XO. They ask questions like "Does this character design match a medieval theme?" or "What could improve this background?" They learn to get visual feedback from XO, not just code feedback.

---

### 1.4 MISSING: Stage Snapshot for Vision

#### Issue ID: T24-MISSING-003
**Block**: `looks_addcostumefromstagesnapshot` (add costume from stage snapshot)

**Current Coverage**: NOT covered anywhere in T21-T24
**T24 Coverage**: NONE

**Problem**: This block allows capturing the current stage as an image, which could be used with:
- XO analysis of visual outputs
- AI image comparison
- Debugging visual issues

**Recommended Fix**: Add skill at G6 level
- **ID**: T24.G6.10
- **Skill**: Capture and analyze stage output with XO
- **Description**: Students use the stage snapshot block to capture their project's visual output, then attach it to an XO request asking "Is this output correct for [specification]?" They learn to get visual debugging help from XO for graphics-heavy projects.

---

### 1.5 MISSING: OpenAI Whisper vs Azure Speech Recognition

#### Issue ID: T24-MISSING-004
**Blocks**:
- `start recognizing speech in [LANGUAGE] record as [SOUNDNAME]` with provider choice
- OpenAI Whisper-specific blocks

**Current Coverage**:
- T23.G4.04 covers OpenAI Whisper for advanced transcription
- T24.G2.04 and T24.G3.01 cover speech recognition generically

**T24 Coverage**: Generic speech recognition mentioned, but NO comparison of providers

**Problem**: Students don't learn:
- When to use Azure vs OpenAI Whisper
- Trade-offs (accuracy vs speed vs cost)
- How provider choice affects XO-integrated projects

**Recommended Fix**: Add to existing skill T24.G3.01 or create new skill
- **Enhanced T24.G3.01 Description**: Add paragraph: "Students experiment with both Azure and OpenAI Whisper speech recognition providers, comparing transcription accuracy for their voice. They learn that Whisper often provides better accuracy but may be slower, while Azure offers faster real-time recognition."

---

### 1.6 MISSING: Generic LLM Blocks and System Instructions

#### Issue ID: T24-MISSING-005
**Blocks**:
- `LLM model [PROVIDER] request [PROMPT]`
- `LLM set system instruction [INSTRUCTION] for model [PROVIDER]`

**Current Coverage**: T22.G7.08 covers generic LLM blocks
**T24 Coverage**: T24 only uses ChatGPT blocks, never mentions generic LLM blocks

**Problem**: T24 teaches only ChatGPT-specific interactions. Students don't learn:
- How to compare different LLM providers (small vs large models)
- How to set system instructions for XO-like behavior
- Speed/cost/quality trade-offs between models

**Recommended Fix**: Add skill at G7 or G8 level
- **ID**: T24.G7.08
- **Skill**: Compare LLM models for XO-style assistance
- **Description**: Students use the `LLM model [PROVIDER] request [PROMPT]` block to send the same coding question to "small" and "large" model options. They compare response quality, speed, and detail. They learn to use `LLM set system instruction` to configure the model with XO-like instructions ("You are a coding tutor for young students"). This teaches model selection trade-offs for AI-assisted coding.

---

## 2. SKILL QUALITY ISSUES

### 2.1 Skills That Are Too Broad/Complex

#### Issue ID: T24-QUALITY-001
**Skill**: T24.G8.05 - Build an interactive XO tutorial project
**Problem**: This is a CAPSTONE-LEVEL skill that combines:
- Step-by-step guidance system
- Example prompt storage in lists
- Interactive practice elements
- Tutorial flow management
- Multiple XO best practices

This should be broken into 2-3 skills:
1. Design tutorial structure and navigation
2. Store and display example prompts
3. Create interactive practice exercises

**Recommended Fix**: Split into multiple skills or mark as explicit capstone project

---

#### Issue ID: T24-QUALITY-002
**Skill**: T24.G8.04 - Implement AI usage tracking and policy enforcement
**Problem**: Extremely broad - combines:
- Tracking XO contributions in lists
- Displaying attribution labels
- Implementing approval workflows
- Logging usage statistics
- Documenting policy decisions

**Recommended Fix**: This is appropriate as a capstone, but description should clarify it's a comprehensive project, not a single skill

---

### 2.2 Skills with Vague Descriptions

#### Issue ID: T24-QUALITY-003
**Skill**: T24.G5.01 - Read and interpret XO's interface cues
**Problem**: Description mentions "template prompts" and "code/explanation tabs" but doesn't clearly explain:
- What specific interface elements to learn
- How to use "pause, copy, and pin answers"
- What the learning objectives are beyond "exploring"

**Recommended Fix**: Add more specific learning objectives:
"Students can: (1) locate and use template prompts, (2) switch between code and explanation views, (3) copy code snippets safely, (4) pin important responses for later reference, and (5) identify when XO is still generating vs finished."

---

### 2.3 Skills Missing Key Implementation Details

#### Issue ID: T24-QUALITY-004
**Skill**: T24.G6.05.01 - Generate custom images with the DALL-E block
**Problem**: Mentions "select appropriate resolutions" but doesn't specify:
- What resolutions are available
- When to use each resolution
- How resolution affects performance/quality

**Recommended Fix**: Add detail: "Students learn to choose between 256x256 (fast, small assets), 512x512 (balanced), and 1024x1024 (high quality, slower) based on whether they're generating thumbnails, game sprites, or detailed backdrops."

---

#### Issue ID: T24-QUALITY-005
**Skill**: T24.G5.07 - Use the ChatGPT block to get AI responses in code
**Problem**: Doesn't mention critical parameter: session management
- Should specify "session: new" vs "session: continue"
- Should explain when to use each mode
- This is essential for XO-style interactions

**Recommended Fix**: Add to description: "They learn to use 'session: new' for independent queries and 'session: continue' to maintain conversation context across multiple XO requests, enabling more sophisticated multi-turn assistance."

---

### 2.4 Skills with Unclear Block Specifications

#### Issue ID: T24-QUALITY-006
**Skill**: T24.G5.06 - Use AI sentence analysis to identify parts of speech
**Problem**: Description says "results are written to a table" but doesn't specify:
- What the table structure looks like
- What fields are returned (word, POS tag, index?)
- How to interpret the results

**Recommended Fix**: Add detail: "The table contains columns for word, part of speech (noun, verb, adjective, etc.), and word position. Students learn to read this structured data and use it to analyze sentence patterns."

---

## 3. GRADE-APPROPRIATENESS ISSUES

### 3.1 K-2 Skills Analysis (Should be UNPLUGGED)

#### CORRECT: All K-2 skills are appropriately unplugged ✓

**T24.GK.01**: Picture-based activity matching AI helpers - ✓ UNPLUGGED
**T24.GK.02**: View and identify AI-made vs human-made pictures - ✓ UNPLUGGED
**T24.GK.03**: Practice giving instructions (teacher demonstrates) - ✓ UNPLUGGED
**T24.G1.01**: Hear AI speech and describe differences - ✓ UNPLUGGED
**T24.G1.02**: Ask questions and compare answers - ✓ UNPLUGGED (guided by teacher)
**T24.G1.03**: See examples of unclear instructions - ✓ UNPLUGGED
**T24.G2.01**: Type sentences for text-to-speech - **CODING BLOCK** ✓ CORRECT (G2 can code)
**T24.G2.02**: Sort picture cards - ✓ UNPLUGGED
**T24.G2.03**: Practice describing images - ✓ UNPLUGGED
**T24.G2.04**: Observe AI transcription - ✓ UNPLUGGED (teacher-led demo)

**VERDICT**: No grade-appropriateness issues for K-2. All are properly unplugged or appropriate for grade level.

---

### 3.2 G3+ Skills Analysis (Should involve CODING)

#### Issue ID: T24-GRADE-001
**Skill**: T24.G3.02 - Evaluate if AI output matches the request
**Problem**: This is UNPLUGGED (just viewing and judging), but it's at G3 level
**Current Description**: "Students give an AI image generator a prompt and judge whether the result matches"
**Issue**: No coding involved - this is evaluation only

**Recommended Fix**: Either:
1. Move to G2 (as an unplugged activity), OR
2. Add coding component: "Students use the DALL-E block to generate images programmatically and build a rating system that stores prompts and quality ratings in a list"

---

#### Issue ID: T24-GRADE-002
**Skill**: T24.G3.03 - Revise a prompt to improve AI results
**Problem**: Still UNPLUGGED at G3 level
**Current Description**: "Students take an AI result that did not match their goal and revise their prompt"
**Issue**: No coding blocks specified

**Recommended Fix**: Add coding: "Students create a script that stores prompt versions in a list, generates images with each version, and logs which revision produced the best result. They learn iterative prompt engineering through coded experimentation."

---

#### Issue ID: T24-GRADE-003
**Skill**: T24.G3.04 - Recognize AI makes mistakes
**Problem**: Purely conceptual/unplugged at G3
**Current Description**: "Students examine AI outputs that contain errors and identify the mistakes"
**Issue**: No coding component

**Recommended Fix**: Add coding: "Students build a fact-checking script that sends AI answers to a verification system (e.g., comparing AI math answers to calculated results) and flags discrepancies. They learn to programmatically validate AI outputs."

---

### 3.3 Skills at Wrong Grade Level

#### Issue ID: T24-GRADE-004
**Skill**: T24.G4.02 - Write a multi-part prompt for AI
**Problem**: This is still primarily WRITING, not coding
**Grade Level**: G4
**Issue**: Should involve blocks by G4

**Recommended Fix**: Keep the skill but add: "Students create a prompt-builder script with dropdown menus for subject, action, setting, and style. When they click 'Generate,' the script joins these elements into a complete prompt and sends it to the AI image generator."

---

#### Issue ID: T24-GRADE-005
**Skill**: T24.G4.03 - Identify safe and unsafe AI interactions
**Problem**: This is SORTING CARDS (unplugged) at G4 level
**Current Description**: "Students sort examples of AI prompts into safe and unsafe categories"
**Issue**: Too simple for G4 - this is appropriate for G2

**Recommended Fix**: Either:
1. Move to G2 as unplugged activity, OR
2. Add coding: "Students build a safety-checker script that uses the content moderation block to automatically flag risky prompts and categorize them by risk type (personal info, inappropriate, off-task)."

---

## 4. SCAFFOLDING ISSUES

### 4.1 Missing Prerequisite Skills

#### Issue ID: T24-SCAFFOLD-001
**Skill**: T24.G5.03 - Turn an XO suggestion into starter code safely
**Problem**: Requires understanding of:
- How to read and interpret code (not explicitly taught before this)
- What "variables/events exist" means
- How to annotate code

**Missing Prerequisites**:
- No skill on "reading unfamiliar code"
- No skill on "identifying variables and events in a script"
- Dependency on T10.G3.03 (lists) seems unrelated

**Recommended Fix**: Add prerequisite skill at G4:
- **ID**: T24.G4.07
- **Skill**: Read and explain code written by others
- **Description**: Students are given short scripts (3-5 blocks) and explain what each block does in their own words. They identify variables, events, and loops. This prepares them to safely evaluate XO-generated code.

---

#### Issue ID: T24-SCAFFOLD-002
**Skill**: T24.G6.05 - Maintain a prompt/response lab notebook using lists
**Problem**: This is the FIRST time students systematically log AI interactions
**Gap**: No earlier practice with:
- Structured data collection
- Table/list schema design
- What fields to log (date, tool, prompt, result, action)

**Recommended Fix**: Add prerequisite at G5:
- **ID**: T24.G5.09
- **Skill**: Log XO interactions in a simple list
- **Description**: Students create a list called "XO Log" and add entries each time they use XO. Each entry includes: timestamp, prompt (first 20 characters), and whether they used the response (yes/no). This introduces basic interaction logging before the complex lab notebook at G6.

---

### 4.2 Skills That Jump Too Far in Complexity

#### Issue ID: T24-SCAFFOLD-003
**Skill**: T24.G6.01 - Provide complete context when asking XO to debug
**Problem**: Sudden jump from G5 (basic XO use) to G6 (assembling "debug packet")
**Complexity Jump**:
- G5: Basic XO interaction (insert code, ask questions)
- G6: Assemble bug description + script + expected outcome
- No intermediate scaffolding

**Recommended Fix**: Add intermediate skill at G5:
- **ID**: T24.G5.10
- **Skill**: Describe bugs clearly to XO
- **Description**: Students practice writing 2-3 sentence bug descriptions that include: (1) what they tried, (2) what happened, (3) what they expected. They learn that clear bug reports get better XO help. This scaffolds toward the full "debug packet" at G6.

---

#### Issue ID: T24-SCAFFOLD-004
**Skill**: T24.G7.01 - Create reusable XO prompt templates in lists
**Problem**: Huge jump in abstraction:
- G6: Maintain lab notebook (concrete data logging)
- G7: Design templates with placeholders (meta-level abstraction)
- No scaffolding for placeholder concept

**Recommended Fix**: Add intermediate skill at G6:
- **ID**: T24.G6.11
- **Skill**: Identify reusable patterns in XO prompts
- **Description**: Students review their XO log (from G6.05) and highlight prompts that are similar except for specific details (sprite names, variable names, goals). They identify the "template" structure and which parts vary. This prepares them to create formal templates at G7.

---

### 4.3 Gaps in Progression Within Topic

#### Issue ID: T24-SCAFFOLD-005
**Gap**: No progression from ChatGPT block (G5.07) to multi-turn conversations
**Current State**:
- G5.07: Basic ChatGPT block usage
- G6.08: Multi-turn chatbot (huge jump)
- Missing: Intermediate skill on session management

**Recommended Fix**: Add skill at G6:
- **ID**: T24.G6.12
- **Skill**: Maintain conversation context with session parameter
- **Description**: Students modify their ChatGPT block usage from G5.07 to use "session: continue" instead of "session: new". They ask XO a series of related questions (e.g., "What are loops?" then "Show me an example") and observe how context is maintained. This scaffolds toward multi-turn chatbots at G6.08.

---

#### Issue ID: T24-SCAFFOLD-006
**Gap**: No progression from keyword search (G4.01) to themed asset collection (G5.04)
**Current State**:
- G4.01: Single keyword search ("cat", "forest")
- G5.04: Multi-part queries for themed scenes (huge jump)
- Missing: Intermediate skill on combining search terms

**Recommended Fix**: Add skill at G4 or G5:
- **ID**: T24.G4.08
- **Skill**: Combine keywords for specific AI image results
- **Description**: Students learn to use multiple keywords in one search query (e.g., "cat sitting forest" instead of just "cat"). They compare results from single-word vs multi-word searches and learn how specificity improves results. This scaffolds toward themed collection at G5.04.

---

## 5. DEPENDENCY ISSUES WITHIN T24

### 5.1 Skills Depending on Later Skills

**NONE FOUND** - All T24 skills have dependencies only on earlier skills within T24 or on other topics. ✓

---

### 5.2 Circular Dependencies

**NONE FOUND** - No circular dependencies detected. ✓

---

### 5.3 Violations of X-2 Rule

#### Issue ID: T24-DEP-001
**Skill**: T24.G5.01 - Read and interpret XO's interface cues
**Dependencies**:
- T01.G3.01 (G3 skill) - ✓ OK (G5 - G3 = 2, at boundary)
- T09.G3.05 (G3 skill) - ✓ OK (G5 - G3 = 2, at boundary)
- T24.G4.03 (G4 skill) - ✓ OK (G5 - G4 = 1)
- T24.G4.06 (G4 skill) - ✓ OK (G5 - G4 = 1)

**Verdict**: No X-2 violation, but dependencies are at the boundary. Consider if T01.G3.01 and T09.G3.05 are truly necessary.

---

#### Issue ID: T24-DEP-002
**Skill**: T24.G7.02 - Run an XO-led code review with evidence
**Dependencies**:
- T06.G5.01 (G5 skill) - ✓ OK (G7 - G5 = 2, at boundary)
- T08.G5.01 (G5 skill) - ✓ OK (G7 - G5 = 2, at boundary)
- T09.G3.05 (G3 skill) - **X-2 VIOLATION** (G7 - G3 = 4 grades back)

**Problem**: T09.G3.05 is 4 grades back from G7
**Recommended Fix**: Replace T09.G3.05 with T09.G5.04 or T09.G6.01 (more recent variable skills)

---

#### Issue ID: T24-DEP-003
**Skill**: T24.G7.03 - Combine XO storyboards with AI sprite generation
**Dependencies**:
- T09.G3.05 (G3 skill) - **X-2 VIOLATION** (G7 - G3 = 4 grades back)

**Problem**: T09.G3.05 is 4 grades back from G7
**Recommended Fix**: Replace with T09.G5.04 or T09.G6.01

---

#### Issue ID: T24-DEP-004
**Skill**: T24.G7.05 - Use XO to coach peers with rubric-based feedback
**Dependencies**:
- T09.G3.01 (G3 skill) - **X-2 VIOLATION** (G7 - G3 = 4 grades back)

**Problem**: T09.G3.01 is 4 grades back from G7
**Recommended Fix**: Replace with T09.G5.01 or T09.G6.01

---

#### Issue ID: T24-DEP-005
**Skill**: T24.G8.05 - Build an interactive XO tutorial project
**Dependencies**:
- T01.G6.01 (G6 skill) - ✓ OK (G8 - G6 = 2, at boundary)
- T07.G6.01 (G6 skill) - ✓ OK
- T09.G6.01 (G6 skill) - ✓ OK
- T24.G7.05 and T24.G8.04 - ✓ OK

**Verdict**: No violations, but dependencies are at X-2 boundary

---

### 5.4 Unnecessary Dependencies

#### Issue ID: T24-DEP-006
**Skill**: T24.G5.03 - Turn an XO suggestion into starter code safely
**Dependencies**:
- **T10.G3.03**: Add and remove items from a list

**Problem**: This dependency seems unrelated to the skill
**Current Skill**: Reading XO code, verifying variables/events, annotating blocks
**Dependency**: List manipulation
**Question**: Why does reading and annotating XO code require list skills?

**Recommended Fix**: Remove T10.G3.03 dependency unless the skill description is updated to include list-based code annotation

---

#### Issue ID: T24-DEP-007
**Skill**: T24.G5.04 - Collect themed assets from narrative descriptions
**Dependencies**:
- T01.G3.01: Complete a simple script with missing blocks
- T09.G3.05: Trace code with variables to predict outcomes

**Problem**: These dependencies seem unrelated
**Current Skill**: Converting narrative to image search queries, collecting assets
**Dependencies**: Completing scripts and tracing variables
**Question**: Why does asset collection require script completion and variable tracing?

**Recommended Fix**: Remove T01.G3.01 and T09.G3.05. The only necessary dependencies are:
- T24.G4.01 (search skills)
- T24.G5.02 (getting narrative from XO)

---

#### Issue ID: T24-DEP-008
**Skill**: T24.G5.05 - Reject unsafe or off-spec XO suggestions
**Dependencies**:
- T01.G3.01: Complete a simple script with missing blocks
- T09.G3.05: Trace code with variables to predict outcomes

**Problem**: Same as above - these seem unrelated
**Current Skill**: Reviewing XO replies, identifying off-task/unsafe steps, writing replacements
**Dependencies**: Script completion and variable tracing

**Recommended Fix**: Remove T01.G3.01 and T09.G3.05. Keep only:
- T24.G4.03 (safety concepts)
- T24.G5.03 (reading XO code)

---

#### Issue ID: T24-DEP-009
**Skill**: Multiple G5 skills have identical boilerplate dependencies
**Skills Affected**:
- T24.G5.01, G5.02, G5.04, G5.05 all have:
  - T01.G3.01
  - T09.G3.05

**Problem**: These seem to be copy-pasted boilerplate dependencies without justification
**Evidence**: The skills have very different focuses (interface navigation, planning, asset collection, safety) but identical non-T24 dependencies

**Recommended Fix**: Review each skill individually and remove unnecessary dependencies. Not all G5 T24 skills need the same prerequisites.

---

## 6. CROSS-TOPIC COVERAGE NOTES

### 6.1 AI Blocks Well-Covered in Other Topics ✓

The following AI blocks are appropriately covered in their respective topics and do NOT need to be in T24:

**T21 (AI Media Generation):**
- Neural networks (TensorFlow)
- KNN classifiers
- Semantic search / vector databases
- Web search
- DALL-E image generation
- Image moderation
- Sentence analysis (NLP)

**T22 (Chatbots & Prompting):**
- ChatGPT blocks (basic and advanced)
- Generic LLM blocks
- Multiple chatbot sessions
- Attaching images/files to chat
- Image moderation for chatbots
- RAG (retrieval-augmented generation)
- Multi-agent conversations
- Structured output parsing
- Web search integration

**T23 (AI Perception):**
- Face detection
- Body pose detection (2D and 3D)
- Hand detection and gestures
- Speech recognition (Azure and Whisper)
- Real-time sensor processing
- AR effects with face detection

---

### 6.2 XO-Specific Skills Unique to T24 ✓

T24 correctly focuses on XO (the CreatiCode AI coding assistant) which is NOT covered in T21-T23:

**XO Interface & Interaction:**
- Reading XO's interface (G5.01)
- Asking XO for project plans (G5.02)
- Safely using XO code (G5.03)
- Rejecting unsafe XO suggestions (G5.05)

**XO Debugging & Review:**
- Providing context for XO debugging (G6.01)
- Verifying XO explanations (G6.02)
- XO-led code reviews (G7.02)

**XO Advanced Use:**
- Prompt templates for XO (G7.01)
- XO storyboard integration (G7.03)
- Automated XO requests (G8.01)
- XO with automated tests (G8.02)
- AI usage tracking (G8.04)

**This is appropriate topic focus** - T24 should be about XO and generative AI practices, not repeating T21-T23 content.

---

## 7. SUMMARY OF RECOMMENDED FIXES

### 7.1 Critical Additions Needed

1. **T24.G6.09**: Send screenshots and assets to XO for feedback (attaching images to XO)
2. **T24.G7.06**: Compare XO responses using multiple sessions (`select chatbot` block)
3. **T24.G7.08**: Compare LLM models for XO-style assistance (generic LLM blocks)

### 7.2 Skills to Modify

1. **T24.G3.01**: Add comparison of Azure vs OpenAI Whisper providers
2. **T24.G3.02, G3.03, G3.04**: Add coding components (currently too unplugged for G3)
3. **T24.G4.02**: Add prompt-builder script with dropdown menus
4. **T24.G4.03**: Add automated safety-checker using moderation blocks
5. **T24.G5.07**: Add explanation of session management (new vs continue)
6. **T24.G6.05.01**: Add detail about resolution choices

### 7.3 Scaffolding Skills to Add

1. **T24.G4.07**: Read and explain code written by others (prerequisite for G5.03)
2. **T24.G4.08**: Combine keywords for specific AI image results (prerequisite for G5.04)
3. **T24.G5.09**: Log XO interactions in a simple list (prerequisite for G6.05)
4. **T24.G5.10**: Describe bugs clearly to XO (prerequisite for G6.01)
5. **T24.G6.11**: Identify reusable patterns in XO prompts (prerequisite for G7.01)
6. **T24.G6.12**: Maintain conversation context with session parameter (prerequisite for G6.08)

### 7.4 Dependencies to Fix

**X-2 Violations (4 skills):**
- T24.G7.02: Replace T09.G3.05 with T09.G5.04
- T24.G7.03: Replace T09.G3.05 with T09.G5.04
- T24.G7.05: Replace T09.G3.01 with T09.G5.01
- (T24.G8.05 is OK at boundary)

**Unnecessary Dependencies (5+ skills):**
- T24.G5.03: Remove T10.G3.03 (unrelated list dependency)
- T24.G5.04: Remove T01.G3.01 and T09.G3.05 (unrelated)
- T24.G5.05: Remove T01.G3.01 and T09.G3.05 (unrelated)
- Review all G5 skills for boilerplate dependencies

### 7.5 Skills to Split or Mark as Capstone

1. **T24.G8.04**: Mark clearly as capstone project in description
2. **T24.G8.05**: Mark clearly as capstone project in description

---

## 8. FINAL STATISTICS

**Total T24 Skills Analyzed**: 41
**Issues Found**: 33
- Missing Skills/Blocks: 6
- Quality Issues: 6
- Grade-Appropriateness Issues: 5
- Scaffolding Issues: 6
- Dependency Issues: 10

**Severity Breakdown**:
- Critical: 3 (missing blocks that XO can use)
- High: 8 (grade-appropriateness, X-2 violations)
- Medium: 15 (quality improvements, scaffolding)
- Low: 7 (unnecessary dependencies)

**Overall Assessment**: T24 is STRONG in its core focus (XO practices) but has significant gaps in:
1. XO multimodal capabilities (images, files)
2. G3-G4 skills being too unplugged
3. G5 skills having unnecessary boilerplate dependencies
4. Missing scaffolding between complexity jumps

---

## 9. PRIORITIZED ACTION PLAN

### Phase 1: Critical Fixes (Do First)
1. Add T24.G6.09 (attach images to XO)
2. Add T24.G7.06 (multiple XO sessions)
3. Fix X-2 violations in G7 skills
4. Add coding components to G3 skills (G3.02, G3.03, G3.04)

### Phase 2: Quality & Scaffolding (Do Second)
1. Add scaffolding skills at G4-G6 (6 new skills)
2. Enhance descriptions for vague skills (G5.01, G6.05.01, G5.07)
3. Remove unnecessary dependencies from G5 skills

### Phase 3: Optional Enhancements (Do Last)
1. Add T24.G7.08 (generic LLM comparison)
2. Add stage snapshot skill (G6.10)
3. Mark capstone skills explicitly
4. Add provider comparison to speech recognition

---

**End of Analysis Report**
