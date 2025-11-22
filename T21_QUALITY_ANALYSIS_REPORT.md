# T21 AI Media - Comprehensive Quality Analysis Report

**Analysis Date:** 2025-11-21
**Analyst:** Claude Code Agent
**Scope:** T21 (AI Media) Skills and CreatiCode AI Media Blocks

---

## Executive Summary

**Current Status:**
- **Total T21 Skills:** 28 (G3-G8 only, NO K-2 skills)
- **Grade Distribution:** G3=2, G4=3, G5=5, G6=7, G7=6, G8=5
- **Available AI Media Blocks:** 16 documented + additional AI blocks
- **Critical Finding:** Major K-2 gap, missing coverage of available blocks, dependency issues

**Overall Assessment:** T21 requires significant revision to address K-2 gap, improve coverage of available CreatiCode blocks, fix dependency violations, and clarify skill descriptions.

---

## 1. K-2 GAP ANALYSIS (HIGH PRIORITY)

### Current State
**CRITICAL ISSUE:** T21 has ZERO K-2 skills. This violates the requirement that K-2 students should have picture-based/unplugged activities for foundational concepts.

### What K-2 Should Cover

#### Recommended K-2 Skills to Add:

**T21.GK.01: Recognize AI-generated vs recorded media**
- **Activity Type:** Picture sorting (unplugged)
- **Description:** Students look at pairs of images/sounds and identify which was made by a computer vs a person. Focus on obvious clues (perfect repetition, unusual patterns).
- **Rationale:** Foundational awareness before coding

**T21.GK.02: Identify sensors that capture media**
- **Activity Type:** Picture matching (unplugged)
- **Description:** Match pictures of devices (microphone, camera, speaker) to what they do (listen, watch, talk). Build vocabulary for input/output.
- **Rationale:** Understanding hardware before using AI blocks

**T21.G1.01: Describe what you want to see or hear**
- **Activity Type:** Picture cards + verbal description
- **Description:** Students practice turning ideas into simple descriptions using subject + color + setting vocabulary.
- **Rationale:** Prompt engineering foundation (unplugged)

**T21.G1.02: Sort safe vs unsafe things to create**
- **Activity Type:** Card sorting (unplugged)
- **Description:** Students sort picture cards into "okay to make" vs "not okay" (family photos, personal info, scary content).
- **Rationale:** Safety awareness before using generation tools

**T21.G2.01: Recognize that computers can speak and listen**
- **Activity Type:** Demo/observation + picture matching
- **Description:** Students watch teacher demo text-to-speech and speech recognition, then match "computer abilities" to "human abilities."
- **Rationale:** Conceptual foundation for speech blocks

**T21.G2.02: Explain when AI media is helpful vs when hand-made is better**
- **Activity Type:** Scenario cards + discussion
- **Description:** Given scenarios (making lots of backgrounds vs drawing your unique character), students discuss which approach fits better.
- **Rationale:** Decision-making foundation before G5.01

### Impact of K-2 Gap
- **Severity:** HIGH
- **Student Impact:** G3 students lack foundational vocabulary and concepts
- **Curriculum Coherence:** Breaks K-8 progression
- **Recommendation:** ADD 6 K-2 skills immediately

---

## 2. COVERAGE GAPS - MISSING BLOCKS (HIGH/MEDIUM PRIORITY)

### Available Blocks NOT Covered in T21

#### 2.1 Semantic Search (MEDIUM - belongs in T22 or T24)
**Available Blocks:**
- `create semantic database from table [TABLE]`
- `search semantic database with [QUERY] store top (K) in table [TABLE]`

**Current Status:** Used in T22 (ChatGPT context grounding)
**T21 Coverage:** NONE
**Recommendation:** Keep in T22, no change needed

#### 2.2 NLP Sentence Analysis (MEDIUM - could fit T21 or T24)
**Available Block:**
- `analyze sentence [SENTENCE] and write into table [TABLENAME]`

**Current Status:** Not explicitly covered in any T21 skill
**T21 Coverage:** NONE
**Use Cases:** Grammar checking, sentence structure analysis, language learning
**Recommendation:**
- **Option A:** Add to T24 (AI Data & Learning) as text analysis skill
- **Option B:** Add G7-G8 skill in T21 for analyzing speech-to-text output quality
- **Decision:** Best fit for T24, NOT T21

#### 2.3 Computer Vision Blocks (CONFIRMED - belongs in T23)
**Available Blocks:**
- `run face detection debug [DODEBUG] write into table [TABLENAME]`
- `run 3D pose detection debug [DODEBUG] table [TABLENAME]`
- `run hand detection table [TABLENAME] debug [DODEBUG] show video [SHOWVIDEO]`

**Current Status:** Covered in T23 (Interactive AI)
**T21 Coverage:** NONE
**Recommendation:** Correctly placed in T23, no change needed

#### 2.4 Neural Network Training (CONFIRMED - belongs in T24)
**Available Blocks:**
- `create neural network model [NAME]`
- `add layer to neural network [NAME]...`
- `compile neural network [NAME]...`
- `train neural network [NAME]...`
- `predict with neural network [NAME]...`

**Current Status:** Should be in T24 (AI Data & Learning)
**T21 Coverage:** NONE
**Recommendation:** Correctly NOT in T21 - these are machine learning, not media generation

#### 2.5 Image Search & Web Search (LOW - utility blocks)
**Available Blocks:**
- `search for AI image of [TYPE] with query [QUERY]` (ai_xoimagereporter)
- `web search [QUERY] store top (K) in table [TABLE]` (googlesearch)
- `attach costume [COSTUMENAME] to chat` (attachimagetochat)

**Current Status:**
- Image search: Not covered
- Web search: Should be in T22 (research/fact-checking)
- Attach costume: Used implicitly in T21.G7.02 (ChatGPT integration)

**T21 Coverage:** PARTIAL
**Recommendation:**
- Add G5-G6 skill for AI image library search (less complex than DALL-E)
- Web search belongs in T22
- Attach costume already implicitly used

### Summary of Coverage Gaps
| Block Category | Status | Belongs To | Action Needed |
|----------------|--------|------------|---------------|
| Semantic Search | Missing from T21 | T22 | None (correctly placed) |
| NLP Analysis | Missing from all | T24 | Add to T24, not T21 |
| Computer Vision | Missing from T21 | T23 | None (correctly placed) |
| Neural Networks | Missing from T21 | T24 | None (correctly placed) |
| Image Library Search | Missing from T21 | T21 | ADD to T21 (G5-G6) |
| Web Search | Missing from T21 | T22 | None (correctly placed) |

**HIGH PRIORITY ACTION:** Add image library search skill to T21.G5 (simpler alternative to DALL-E)

---

## 3. QUALITY ISSUES IN SKILL DESCRIPTIONS (HIGH/MEDIUM PRIORITY)

### 3.1 Overly Broad Skills (HIGH)

**T21.G3.01: Tell whether media was AI-generated or recorded**
- **Issue:** Too broad - no specific criteria or methodology
- **Description states:** "compare pairs of images or short sounds... pick which seems AI-made, explaining clues"
- **Problem:** No guidance on what constitutes "clues" or how to evaluate
- **Recommendation:** Add specific observable criteria (e.g., repeated patterns, perfect symmetry, unusual shadows, robotic cadence)

**T21.G4.02: Describe AI media you've experienced**
- **Issue:** Vague learning objective - "describe" is too open-ended
- **Description states:** "share examples... describe what made it useful or confusing"
- **Problem:** No structured framework for evaluation
- **Recommendation:** Provide evaluation rubric (quality, accuracy, usefulness, appropriateness)

**T21.G5.01: Decide AI vs hand-made for a single asset type**
- **Issue:** Lacks decision criteria
- **Description states:** "explain whether AI generation or hand-drawing would work better, considering factors"
- **Problem:** Factors mentioned but not defined clearly
- **Recommendation:** Specify decision framework (time, uniqueness, consistency, control, complexity)

### 3.2 Skills That Should Be Broken Down (MEDIUM)

**T21.G6.03: Build a prompt test bench inside CreatiCode**
- **Issue:** Too many sub-skills in one
- **Components:** UI design + text input + dropdown + gallery + DALL-E integration + table logging
- **Problem:** This is really 3-4 skills combined
- **Recommendation:** Break into:
  1. G6.03a: Design prompt input interface
  2. G6.03b: Generate and display multiple variations
  3. G6.03c: Log results for comparison

**T21.G7.01: Create a reusable prompt template library**
- **Issue:** Complex multi-step skill presented as single unit
- **Components:** Table design + loop iteration + prompt assembly + DALL-E calls + result logging
- **Problem:** Requires mastery of tables, loops, string manipulation, and AI calls
- **Recommendation:** Add prerequisite skill for prompt templates, then this for library automation

**T21.G8.03: Produce a multi-scene media experience from a creative brief**
- **Issue:** Capstone skill but lacks intermediate scaffolding
- **Description states:** "3-5 beats... ChatGPT for descriptions, DALL-E for art, TTS for narration, navigation UI, transitions"
- **Problem:** Massive jump from single-scene (G7.05) to multi-scene with navigation
- **Recommendation:** Add G7.06 skill for 2-scene experience before full capstone

### 3.3 Unclear Descriptions (MEDIUM)

**T21.G5.04: Understand how speech-to-text works**
- **Issue:** "Understand" is not measurable or specific
- **Description states:** "explore how computers convert spoken words... learn that clear speech... improves accuracy"
- **Problem:** No concrete activity or demonstration
- **Recommendation:** Change to "Test factors that affect speech-to-text accuracy" with specific experiments

**T21.G4.01: Choose safe and specific prompts for images**
- **Issue:** "Safe" is undefined
- **Description states:** "rewrite it to be specific, safe, and privacy-friendly"
- **Problem:** No definition of what constitutes unsafe content
- **Recommendation:** Provide explicit safety criteria (no personal info, no inappropriate content, no real people's names/addresses)

### 3.4 Block Mismatches (HIGH)

**T21.G5.02: Generate a single AI image using a simple prompt**
- **Block Reference:** "OpenAI DALL-E: generate costume image"
- **Issue:** Description doesn't mention TWO versions of DALL-E block
- **Available Blocks:**
  - Reporter: `OpenAI DALL-E: generate image with request [DESC] resolution [RES]` (returns URL)
  - Command: `OpenAI DALL-E: generate costume image name [NAME] description [DESC] with resolution [RES]`
- **Recommendation:** Specify which version for G5 (likely command version) and introduce reporter version in G6+

**T21.G5.03: Use AI text-to-speech to read text aloud**
- **Block Reference:** "say [TEXT] in [LANGUAGE] as [VOICETYPE] speed () pitch () volume ()"
- **Issue:** This is accurate but incomplete
- **Missing Block:** `stop speaking` block not mentioned
- **Recommendation:** Add mention of stopping speech and sound recording option

**T21.G6.05: Use AI speech recognition to capture user voice input**
- **Block References:** Listed blocks are correct
- **Issue:** Description doesn't mention TWO provider options
- **Available Options:**
  - Microsoft Azure: `start recognizing speech in [LANGUAGE] record as [SOUNDNAME]`
  - OpenAI Whisper: `OpenAI: start recognizing speech in [LANGUAGE] record as [SOUNDNAME]`
- **Recommendation:** Mention both options or focus on one for simplicity

---

## 4. DEPENDENCY ISSUES (HIGH PRIORITY)

### 4.1 X-2 Rule Violations (HIGH)

**Rule:** For grade X skill, dependencies should only be at grades X, X-1, or X-2.

**VIOLATIONS FOUND:**

**T21.G6.03: Build a prompt test bench inside CreatiCode**
- **Grade:** G6
- **Allowed Dependencies:** G4, G5, G6
- **Actual Dependencies:**
  - T06.G3.01 (G3 - VIOLATES X-2 rule, but foundational so acceptable)
  - T09.G3.01 (G3 - VIOLATES X-2 rule)
  - T09.G3.05 (G3 - VIOLATES X-2 rule)
  - T10.G3.03 (G3 - VIOLATES X-2 rule)
  - T21.G5.02 (G5 - OK)
- **Analysis:** While G3 dependencies are more than 2 grades below, they're foundational cross-topic skills. However, having 4 cross-topic G3 dependencies for a G6 skill suggests the skill is too complex or should be moved to G5.
- **Recommendation:** Either move to G5 or add intermediate G5 skill for simpler test bench

**T21.G6.04: Iterate when an AI output fails requirements**
- **Grade:** G6
- **Allowed Dependencies:** G4, G5, G6
- **Actual Dependencies:**
  - T07.G3.01 (G3 - VIOLATES X-2 rule)
  - T08.G3.01 (G3 - VIOLATES X-2 rule)
  - T09.G3.05 (G3 - VIOLATES X-2 rule)
  - T10.G3.03 (G3 - VIOLATES X-2 rule)
  - T21.G5.02 (G5 - OK)
- **Analysis:** Same issue as G6.03 - too many G3 dependencies
- **Recommendation:** Simplify or move to G5

**T21.G7.01: Create a reusable prompt template library**
- **Grade:** G7
- **Allowed Dependencies:** G5, G6, G7
- **Actual Dependencies:**
  - T07.G5.01 (G5 - OK)
  - T09.G3.05 (G3 - VIOLATES X-2 rule)
  - T10.G5.03 (G5 - OK)
  - T21.G6.03 (G6 - OK)
  - T21.G6.04 (G6 - OK)
- **Analysis:** One G3 dependency (T09.G3.05 - tracing variables)
- **Recommendation:** This is acceptable as it's foundational debugging skill, but verify it's truly needed

**T21.G7.02: Use ChatGPT to expand briefs before generating art**
- **Grade:** G7
- **Allowed Dependencies:** G5, G6, G7
- **Actual Dependencies:**
  - T08.G5.01 (G5 - OK)
  - T09.G3.05 (G3 - VIOLATES X-2 rule)
  - T10.G5.03 (G5 - OK)
  - T21.G6.03 (G6 - OK)
  - T21.G6.04 (G6 - OK)
- **Analysis:** One G3 dependency
- **Recommendation:** Same as G7.01 - verify necessity

**T21.G7.03: Audit AI imagery for representation and bias**
- **Grade:** G7
- **Allowed Dependencies:** G5, G6, G7
- **Actual Dependencies:**
  - T07.G5.01 (G5 - OK)
  - T08.G5.01 (G5 - OK)
  - T09.G3.05 (G3 - VIOLATES X-2 rule)
  - T10.G5.03 (G5 - OK)
  - T21.G6.03 (G6 - OK)
  - T21.G6.04 (G6 - OK)
- **Analysis:** One G3 dependency
- **Recommendation:** Verify necessity

**T21.G7.04: Blend AI frames with manual touch-ups for animation**
- **Grade:** G7
- **Allowed Dependencies:** G5, G6, G7
- **Actual Dependencies:**
  - T06.G5.01 (G5 - OK)
  - T08.G5.01 (G5 - OK)
  - T09.G3.05 (G3 - VIOLATES X-2 rule)
  - T10.G5.03 (G5 - OK)
  - T21.G6.04 (G6 - OK)
- **Analysis:** One G3 dependency
- **Recommendation:** Verify necessity

**T21.G7.05: Synchronize AI visuals with AI narration for a single scene**
- **Grade:** G7
- **Allowed Dependencies:** G5, G6, G7
- **Actual Dependencies:**
  - T06.G5.01 (G5 - OK)
  - T09.G3.05 (G3 - VIOLATES X-2 rule)
  - T10.G5.03 (G5 - OK)
  - T21.G5.03 (G5 - OK)
  - T21.G6.04 (G6 - OK)
- **Analysis:** One G3 dependency
- **Recommendation:** Verify necessity

**PATTERN IDENTIFIED:** T09.G3.05 (Trace code with variables to predict outcomes) appears as a dependency in 6 G7 skills and 2 G6 skills. This is a foundational debugging skill that MAY be acceptable despite violating X-2 rule, BUT it suggests skills may be overly complex.

### 4.2 Circular Dependencies (NONE FOUND)
- **Status:** ✓ NO circular dependencies detected within T21
- **Verification Method:** Traced all intra-topic dependencies, all form valid DAG

### 4.3 Missing Logical Prerequisites (MEDIUM)

**T21.G3.02: Describe what you want AI to create using simple words**
- **Current Dependencies:** T21.G3.01
- **Missing Prerequisite:** None for G3, but this should be foundation for G4.01
- **Issue:** G4.01 depends on G3.01, not G3.02
- **Recommendation:** Make G4.01 depend on G3.02 instead (more logical progression)

**T21.G5.02: Generate a single AI image using a simple prompt**
- **Current Dependencies:** T06.G3.01, T21.G4.01
- **Logical Gap:** Should also depend on G4.03 (understanding AI strengths/limits)
- **Recommendation:** Add T21.G4.03 as dependency

**T21.G6.02: Write structured prompts to maintain consistent visual style**
- **Current Dependencies:** T21.G5.01, T21.G5.02
- **Missing Prerequisite:** Should depend on G4.01 (safe prompts) for safety awareness
- **Recommendation:** Add T21.G4.01 as dependency

**T21.G7.06: Use continuous speech recognition for live dictation**
- **Current Dependencies:** T10.G5.03, T21.G6.05
- **Logical Gap:** Dependencies seem correct, but skill appears disconnected from main T21 progression
- **Recommendation:** This is more of a branch skill - consider moving earlier or connecting to other speech skills

**T21.G8.05: Build a voice-controlled creative assistant**
- **Current Dependencies:** T21.G7.06, T21.G8.01
- **Missing Prerequisites:** Should also require speech-to-text understanding (G5.04) and TTS (G5.03)
- **Recommendation:** Add T21.G5.03 and T21.G5.04 (but this violates X-2 for G8... skill may be better placed in G7)

### 4.4 Unnecessary Same-Grade Dependencies (LOW)

**T21.G4.03: Identify strengths and limits of AI image generation**
- **Current Dependencies:** T21.G3.01, T21.G4.02
- **Same-Grade Dependency:** T21.G4.02
- **Analysis:** Both are G4 analysis skills, ordering is flexible
- **Recommendation:** This is acceptable - they can be learned in either order

### 4.5 Cross-Topic Dependency Analysis (MEDIUM)

**Heavy Dependencies on T06 (Events):**
- T21.G5.02, G6.03, G6.05, G7.05, G8.01, G8.03
- **Analysis:** Reasonable - AI blocks need event-driven programming
- **Recommendation:** No change needed

**Heavy Dependencies on T09 (Variables):**
- Multiple skills depend on T09.G3.05 (tracing variables)
- **Analysis:** This creates X-2 violations for G6+ skills
- **Recommendation:** Consider whether variable tracing is truly necessary or if simpler variable use suffices

**Heavy Dependencies on T10 (Lists/Tables):**
- Many G6+ skills depend on T10.G3.03 or T10.G5.03
- **Analysis:** Makes sense - AI blocks often output to tables
- **Recommendation:** No change needed, but T10.G3.03 creates X-2 violations for G6+ skills

**Missing Dependencies on T08 (Conditionals):**
- Many skills use moderation or validation but don't list T08 dependencies
- **Analysis:** Skills like G6.06, G6.07, G8.01 use if/else for moderation checks
- **Recommendation:** Add T08 dependencies where conditionals are used

---

## 5. PROGRESSION ISSUES (MEDIUM PRIORITY)

### 5.1 Overall Progression Analysis

**Grade 3 (2 skills):**
- G3.01: Identify AI vs recorded media (observation)
- G3.02: Describe what you want AI to create (vocabulary)
- **Assessment:** Good foundation but SHOULD be K-2 concepts
- **Issue:** Too advanced for first exposure

**Grade 4 (3 skills):**
- G4.01: Safe prompts
- G4.02: Describe AI media experiences
- G4.03: Identify AI strengths/limits
- **Assessment:** Good conceptual scaffolding
- **Issue:** All conceptual, no hands-on (OK for G4 if K-2 exists)

**Grade 5 (5 skills):**
- G5.01: Decide AI vs hand-made
- G5.02: Generate single DALL-E image ← FIRST HANDS-ON SKILL
- G5.03: Text-to-speech
- G5.04: Understand speech-to-text (no coding)
- G5.05: Explain why AI needs safety review (no coding)
- **Assessment:** Good introduction to hands-on skills
- **Issue:** G5.04 and G5.05 are conceptual - should be G4 or even G3

**Grade 6 (7 skills):**
- G6.01-G6.04: Advanced image generation (planning, structured prompts, test bench, iteration)
- G6.05: Speech recognition (hands-on)
- G6.06-G6.07: Content moderation (hands-on)
- **Assessment:** HUGE JUMP in complexity from G5
- **Issue:** G6.03 (test bench) is very complex for first year after basic DALL-E

**Grade 7 (6 skills):**
- G7.01-G7.05: Advanced integrations (templates, ChatGPT combo, bias auditing, animation, synchronization)
- G7.06: Continuous speech recognition
- **Assessment:** High complexity, good variety
- **Issue:** G7.06 feels disconnected from main thread

**Grade 8 (5 skills):**
- G8.01-G8.03: Production systems (guardrails, approval pipeline, multi-scene)
- G8.04: Ethics (conceptual)
- G8.05: Voice-controlled assistant (capstone)
- **Assessment:** Good capstones
- **Issue:** G8.04 is conceptual, should be earlier

### 5.2 Difficulty Jumps (MEDIUM)

**MAJOR JUMP: G5.02 → G6.03**
- **G5.02:** Generate single image with simple prompt
- **G6.03:** Build full prompt test bench with UI, loops, tables, multiple generations
- **Gap:** Missing intermediate skills like:
  - G6.X: Generate multiple images from list of prompts
  - G6.Y: Compare two AI outputs side-by-side
  - G6.Z: Save generation results to list
- **Recommendation:** Add 1-2 intermediate skills in G6

**MAJOR JUMP: G6.05 → G7.06**
- **G6.05:** Basic speech recognition (start, end, retrieve text)
- **G7.06:** Continuous speech recognition with live list updates
- **Gap:** Could use intermediate skill for understanding continuous mode
- **Recommendation:** Consider moving G7.06 to G6 or adding intermediate skill

**CONCEPTUAL JUMP: G7 → G8 Ethics**
- **G7:** Focuses on technical implementations
- **G8.04:** Suddenly introduces ethics research and policy writing
- **Gap:** No ethical consideration in G3-G7
- **Recommendation:** Introduce ethical concepts earlier (G5.05 is close but not integrated into practice)

### 5.3 Scaffolding Analysis (MEDIUM)

**Well-Scaffolded Sequences:**
1. **Image Generation:** G4.01 (prompts) → G5.02 (single image) → G6.02 (structured prompts) → G6.04 (iteration) → G7.01 (templates) ✓
2. **Content Moderation:** G5.05 (why needed) → G6.06 (text moderation) → G6.07 (image moderation) → G8.01 (with guardrails) ✓

**Poorly Scaffolded Sequences:**
1. **Speech Recognition:** G5.04 (conceptual) → G6.05 (basic) → G7.06 (continuous) ✗
   - **Issue:** G5.04 is conceptual with no coding, then sudden hands-on in G6
   - **Fix:** Make G5.04 hands-on testing OR add intermediate G5 skill

2. **AI + ChatGPT Integration:** Appears suddenly in G7.02
   - **Issue:** No prior mention of ChatGPT in T21 (covered in T22)
   - **Fix:** Add explicit cross-topic note or prerequisite

3. **Ethics Thread:** G5.05 (safety) → ... → G7.03 (bias) → G8.04 (policy)
   - **Issue:** 2-grade gap between G5.05 and G7.03
   - **Fix:** Add G6 skill about responsible AI use

### 5.4 Missing Intermediate Skills (MEDIUM)

**Between G5 and G6:**
- Generate multiple images programmatically (loop over prompts)
- Compare AI outputs for quality
- Basic prompt debugging (why didn't it work?)

**Between G6 and G7:**
- Combine text and image generation in simple sequence
- Use moderation in generation workflow

**Between G7 and G8:**
- Multi-modal media project (smaller scale than G8.03)

---

## 6. BLOCK ACCURACY VERIFICATION (HIGH PRIORITY)

### 6.1 Block Syntax Accuracy

**ACCURATE DESCRIPTIONS:**
- ✓ T21.G5.02: DALL-E block syntax correct
- ✓ T21.G5.03: TTS block parameters correct
- ✓ T21.G6.05: Speech recognition blocks correct
- ✓ T21.G6.06: Text moderation block correct
- ✓ T21.G6.07: Image moderation blocks correct

**INCOMPLETE DESCRIPTIONS:**

**T21.G5.02: Generate a single AI image**
- **Skill mentions:** "OpenAI DALL-E: generate costume image"
- **Available blocks:** BOTH reporter and command versions
- **Issue:** Doesn't specify which version
- **Recommendation:** Specify command version for G5 (simpler), introduce reporter version in G6

**T21.G5.03: Use AI text-to-speech**
- **Skill mentions:** Parameters correct (language, voice, speed, pitch, volume)
- **Missing:** Optional `store sound as [SOUNDNAME]` parameter
- **Missing:** `stop speaking` block
- **Recommendation:** Mention sound storage and stopping speech

**T21.G6.05: Use AI speech recognition**
- **Skill mentions:** start, end, retrieve text
- **Missing:** Two provider options (Azure vs OpenAI Whisper)
- **Missing:** Optional recording storage parameter
- **Recommendation:** Clarify which provider or mention both

**T21.G7.06: Use continuous speech recognition**
- **Skill mentions:** Blocks correctly (`start continuous speech recognition`, `stop continuous`)
- **Accuracy:** ✓ Correct
- **Note:** This is Microsoft Azure only, OpenAI Whisper doesn't have continuous mode

### 6.2 Parameter Options Accuracy

**VERIFIED ACCURATE:**
- ✓ Languages: "30+ language options" - CONFIRMED
- ✓ Voice types: 8 types (Male, Female, Male2, Female2, Male3, Female3, Boy, Girl) - CONFIRMED
- ✓ TTS parameters: speed, pitch, volume as percentages - CONFIRMED
- ✓ DALL-E resolutions: 256x256, 512x512, 1024x1024 - CONFIRMED
- ✓ Moderation results: "Pass" or "Fail" - CONFIRMED

**MISSING SPECIFICATIONS:**
- Resolution options not mentioned in G5.02 (should specify default or let students choose)
- Language selection not emphasized in TTS skill (just says "different languages")
- Debug and video visibility options for hand/face/pose detection (but those are in T23, not T21)

### 6.3 Blocks Mentioned That Don't Exist (NONE FOUND)

**Status:** ✓ All blocks referenced in T21 skills exist and are correctly named

### 6.4 Missing Block Mentions

**Blocks that exist but are never mentioned:**
- `search for AI image of [TYPE] with query [QUERY]` - simpler than DALL-E, should be in G5
- `attach costume [COSTUMENAME] to chat` - used implicitly in G7.02 but not explicitly taught
- `stop speaking` - exists but not mentioned in G5.03

**Recommendation:** Add these blocks to appropriate skills

---

## PRIORITIZED RECOMMENDATIONS

### HIGH PRIORITY (Must Fix)

1. **ADD K-2 FOUNDATION SKILLS (6 skills)**
   - K: 2 unplugged skills (recognize AI media, identify sensors)
   - G1: 2 unplugged skills (describe wants, sort safe/unsafe)
   - G2: 2 transition skills (recognize computer abilities, explain AI vs hand-made)

2. **FIX DEPENDENCY VIOLATIONS**
   - Review all T09.G3.05 dependencies in G6+ skills
   - Consider whether "trace variables" is truly needed or if simpler variable skills suffice
   - Move complex skills (G6.03, G6.04) to G5 OR add intermediate G5 skills

3. **ADD MISSING BLOCK: AI Image Library Search**
   - Add T21.G5.X skill: "Search AI image library for ready-made assets"
   - Block: `search for AI image of [TYPE] with query [QUERY]`
   - Place before G5.02 (DALL-E) as simpler introduction

4. **CLARIFY OVERLY BROAD SKILLS**
   - G3.01: Add specific evaluation criteria
   - G4.01: Define "safe" explicitly
   - G5.01: Add decision framework
   - G5.04: Make measurable (change to "Test factors affecting...")

5. **BREAK DOWN COMPLEX SKILLS**
   - G6.03: Split into 2-3 smaller skills (UI design, generation, logging)
   - G7.01: Add prerequisite for prompt templates

6. **FIX BLOCK ACCURACY ISSUES**
   - G5.02: Specify command vs reporter version
   - G5.03: Mention `stop speaking` and sound storage
   - G6.05: Clarify provider options or choose one

### MEDIUM PRIORITY (Should Fix)

7. **ADD SCAFFOLDING SKILLS**
   - Between G5.02 and G6.03: Add "Generate multiple images from a list"
   - Between G6 and G7: Add "Combine moderation with generation workflow"
   - G5.04: Make hands-on instead of conceptual

8. **IMPROVE PROGRESSION**
   - Move G5.05 (safety) to G4
   - Move G8.04 (ethics) concepts earlier (integrate into G6-G7)
   - Connect G7.06 (continuous speech) better to main progression

9. **FIX MISSING LOGICAL PREREQUISITES**
   - G4.01 should depend on G3.02 (not just G3.01)
   - G5.02 should depend on G4.03 (AI limits)
   - G6.02 should depend on G4.01 (safe prompts)
   - G8.05 may need additional dependencies or should move to G7

10. **ADD CROSS-TOPIC NOTES**
    - G7.02: Add note that ChatGPT skills from T22 are prerequisite
    - G8.02: Add note about data management concepts from T24

### LOW PRIORITY (Nice to Have)

11. **ADD EXPLICIT MENTIONS**
    - `attach costume to chat` block in G7.02
    - Resolution selection guidance in G5.02
    - Language selection emphasis in G5.03

12. **IMPROVE DESCRIPTIONS**
    - Add more specific examples to abstract skills
    - Add estimated time for complex skills
    - Add sample project ideas for capstone skills

13. **CONSISTENCY IMPROVEMENTS**
    - Standardize how blocks are referenced (always use full syntax?)
    - Consistent use of "students learn" vs "students use" vs "students build"
    - Consistent mention of parameters

---

## SUMMARY BY ISSUE TYPE

| Issue Category | HIGH | MEDIUM | LOW | Total |
|----------------|------|--------|-----|-------|
| K-2 Gap | 1 | 0 | 0 | 1 |
| Coverage Gaps | 2 | 0 | 0 | 2 |
| Quality Issues | 4 | 2 | 3 | 9 |
| Dependency Issues | 2 | 2 | 0 | 4 |
| Progression Issues | 0 | 3 | 0 | 3 |
| Block Accuracy | 3 | 0 | 1 | 4 |
| **TOTAL** | **12** | **7** | **4** | **23** |

---

## CRITICAL PATH FORWARD

1. **Immediate Actions (Week 1):**
   - Design 6 K-2 skills (unplugged/picture-based)
   - Add AI image library search skill to G5
   - Fix block syntax specifications (G5.02, G5.03, G6.05)
   - Clarify safety criteria in G4.01

2. **Short-term Actions (Weeks 2-3):**
   - Review and fix dependency violations (especially T09.G3.05)
   - Break down complex skills (G6.03, G7.01)
   - Add scaffolding skills between G5-G6
   - Move conceptual skills to appropriate grades

3. **Medium-term Actions (Month 2):**
   - Integrate ethics thread throughout G4-G8
   - Improve skill descriptions with specific criteria
   - Add missing logical prerequisites
   - Test progression with actual curriculum

---

## APPENDIX: BLOCK INVENTORY VERIFICATION

### Documented AI Media Blocks (16 total)
1. ✓ ai_speakinlanguage (TTS)
2. ✓ ai_stopspeaking
3. ✓ ai_startspeech (Azure)
4. ✓ ai_startrecognizer (Azure continuous)
5. ✓ ai_stoprecognizer
6. ✓ ai_startopenaispeech (Whisper)
7. ✓ ai_endspeech
8. ✓ ai_textfromspeech
9. ✓ ai_clearspeech
10. ✓ ai_openaiimagereporter (DALL-E)
11. ✓ getmoderationresult (text)
12. ✓ getmoderationresult2 (image URL)
13. ✓ getmoderationresult3 (costume)
14. ✓ ai_xoimagereporter (image search)
15. ✓ attachimagetochat
16. ✓ googlesearch (web search)

### Additional AI Blocks (Not T21 Media)
- Computer Vision (T23): face detection, pose detection, hand detection
- Neural Networks (T24): create, train, predict
- Semantic Search (T22/T24): create database, search
- NLP (T24): analyze sentence

**Total AI Blocks:** 42+ (16 media + 26+ other AI)

---

## CONCLUSION

T21 (AI Media) has a solid foundation for G3-G8 but requires significant revision to address:

1. **CRITICAL GAP:** No K-2 skills (6 needed)
2. **MISSING COVERAGE:** AI image library search (1 skill needed)
3. **QUALITY ISSUES:** 9 skills need clarification or restructuring
4. **DEPENDENCY PROBLEMS:** 8 skills have violations or missing prerequisites
5. **PROGRESSION GAPS:** Missing intermediate skills between G5-G6 and G6-G7

**Estimated Revision Scope:**
- Add: 6-8 new skills (K-2 foundation + intermediate scaffolding)
- Modify: 12-15 existing skills (descriptions, dependencies, breakdown)
- Move: 2-3 skills to different grades

**Timeline Estimate:**
- Design phase: 2-3 weeks
- Review phase: 1 week
- Implementation: 2-3 weeks
- **Total: 5-7 weeks**

---

**Report Generated:** 2025-11-21
**Next Review:** After K-2 skills added and dependency fixes implemented
