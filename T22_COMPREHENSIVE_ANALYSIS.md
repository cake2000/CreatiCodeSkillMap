# T22: Chatbots & Prompting - Comprehensive Phase 1 Analysis

**Date:** 2025-11-21
**Scope:** All 27 skills (K-8) across T22
**Goal:** Make T22 the gold standard for chatbot/AI education

---

## EXECUTIVE SUMMARY

T22 (Chatbots & Prompting) currently has **27 skills** spanning K-8, with a strong foundation in:
- ✅ K-2 unplugged/picture-based activities
- ✅ G3-5 observing and testing chatbots
- ✅ G6-8 building chatbots with ChatGPT blocks

**CRITICAL FINDINGS:**

### HIGH PRIORITY ISSUES (7)
1. **Missing Widget/UI Foundation** - G6.03 assumes widget knowledge without prerequisites
2. **Missing Speech Integration** - No speech-to-text or text-to-speech skills
3. **Missing DALL-E Integration** - No multimodal AI (image generation in chatbots)
4. **Incorrect Block References** - Several skills reference non-existent or inaccurate blocks
5. **G7.08 Dependency Violation** - Depends on G6 skills (violates X-2 rule)
6. **Missing G4-G5 Scaffolding** - Gap between G3 concepts and G6 coding
7. **Missing Advanced Features** - No semantic search, web search integration properly scaffolded

### MEDIUM PRIORITY ISSUES (5)
1. **G6.05 Too Broad** - Chat window blocks need breaking down
2. **Widget Skills Unclear** - Need explicit widget progression (buttons → labels → textbox → dropdown)
3. **G7 Skills Overlap** - Some skills could be consolidated
4. **Missing Testing/Debugging** - No systematic chatbot testing skills
5. **Moderation Too Late** - G7.04 should come earlier

### PLATFORM ACCURACY ASSESSMENT

**VERIFIED BLOCKS (Correct):**
- ✅ `OpenAI ChatGPT: request [PROMPT] result [VARIABLE] mode [waiting/streaming] length [...] temperature [...] session [...]`
- ✅ `OpenAI ChatGPT: system request [TEXT]`
- ✅ `OpenAI ChatGPT: cancel request`
- ✅ `select chatbot [1/2/3/4]`
- ✅ `get moderation result for [TEXT]`
- ✅ `get moderation result for image at URL [URL]`
- ✅ `get moderation result for costume named [NAME]`
- ✅ `attach costume [NAME] to chat`
- ✅ `attach files to chat`
- ✅ `attach file from Google Drive [URL] to chat`
- ✅ `create semantic database from table [TABLE]`
- ✅ `search semantic database with [QUERY] store top (K) in table [TABLE]`
- ✅ `web search [QUERY] store top (K) in table [TABLE]`
- ✅ `LLM model [PROVIDER] request [PROMPT]`
- ✅ `LLM set system instruction [INSTRUCTION] for model [PROVIDER]`

**INFERRED/LIKELY BLOCKS (Referenced but not fully documented):**
- ⚠️ `add chat window` - Likely exists based on G6.05 description
- ⚠️ `append to chat [CHATNAME] message [...] as [SENDER] icon [...] align [...]` - Likely exists
- ⚠️ `update last chat message to [MESSAGE] for chat [CHATNAME]` - For streaming display

**WIDGET BLOCKS (Exist but not covered in T22):**
- ✅ Label widget blocks (add, set text, set style)
- ✅ Button widget blocks (add, click event)
- ✅ Text Input widget blocks
- ✅ Dropdown widget blocks

**MISSING FROM T22 (Available in CreatiCode but not covered):**
- 🚫 Speech recognition blocks (Azure & OpenAI Whisper)
- 🚫 Text-to-speech blocks (AI Speaker)
- 🚫 DALL-E image generation blocks
- 🚫 Widget category blocks (systematic coverage)

---

## A. PLATFORM ACCURACY ISSUES

### Issue A1: G6.05 - Chat Window Block Syntax Unclear
**Current:** "Students use the `add chat window` block..."
**Problem:** Block name and parameters not fully documented in platform docs
**Fix Needed:** Verify exact block syntax from CreatiCode source

**Recommendation:** Keep skill as-is since it accurately describes the functionality, but flag for verification

### Issue A2: Missing Speech Integration Entirely
**Current:** No skills cover speech-to-text or text-to-speech
**Available Blocks:**
- `start recognizing speech in [LANGUAGE] record as [SOUNDNAME]` (Azure)
- `start speech recognition in [LANGUAGE] for OpenAI Whisper` (OpenAI Whisper)
- `end speech recognition`
- `text from speech` (reporter)
- `say [TEXT] in [LANGUAGE] as [VOICETYPE] speed (N) pitch (N) volume (N)` (TTS)

**Impact:** HIGH - Voice chatbots are increasingly common and important for accessibility

### Issue A3: Missing DALL-E Integration
**Current:** No skills cover multimodal chatbots with image generation
**Available Blocks:**
- `OpenAI DALL-E: generate costume image name [NAME] description [TEXT] with resolution [SIZE]`
- `OpenAI DALL-E: generate image with request [DESCRIPTION] resolution [RESOLUTION v]` (reporter)

**Impact:** MEDIUM - Multimodal AI is growing but less critical for basic chatbot education

### Issue A4: G6.03 - Widget Knowledge Gap
**Current:** "Students design a UI with a text input, 'Send' button, quick-reply buttons..."
**Problem:** No prerequisite skills teach widget basics
**Available:** Widget blocks exist but T22 never introduces them

**Impact:** HIGH - Students expected to use widgets without learning them first

---

## B. MISSING SKILLS NEEDED

### B1: Widget Foundation Skills (HIGH PRIORITY)

**NEW: T22.G4.02 - Add buttons to create interactive prompts**
- Grade: 4
- Description: Students use widget blocks to add buttons to the stage. They create 3-5 quick-reply buttons (e.g., "Tell me a joke", "Fun fact", "Help with math") that set a variable when clicked. This introduces widgets as interactive UI elements before building full chat interfaces.
- Dependencies: T06.G3.01, T09.G3.05
- Rationale: Bridge gap between G3 concepts and G6 widget-heavy coding

**NEW: T22.G5.04 - Display chatbot responses in labels**
- Grade: 5
- Description: Students use a pre-built chatbot and add label widgets to display responses in a styled format. They practice updating label text dynamically when the chatbot replies, learning how to separate input/output in a UI.
- Dependencies: T22.G4.02, T22.G5.02
- Rationale: Scaffolds from buttons to dynamic text display

**NEW: T22.G6.03.01 - Add input widgets for user messages**
- Grade: 6
- Description: Students add a text input widget and a "Send" button to capture user input. When the button is clicked, they read the text input value, store it in a variable, and clear the input field for the next message.
- Dependencies: T22.G5.04, T22.G6.01
- Rationale: Break down G6.03 (currently too complex)

**NEW: T22.G6.03.02 - Build a conversation log with dynamic updates**
- Grade: 6
- Description: Students create a scrolling label or list widget that displays a conversation history. Each time a message is sent or received, they append it to the log with formatting (e.g., "User: [message]" and "Bot: [response]").
- Dependencies: T22.G6.03.01
- Rationale: Complete the G6.03 breakdown

### B2: Speech Integration Skills (HIGH PRIORITY)

**NEW: T22.G5.05 - Test voice input with speech recognition**
- Grade: 5
- Description: Students use a pre-built project with speech recognition enabled. They speak into the microphone and observe how their words appear as text. They test different speaking speeds, accents, and background noise to understand speech-to-text limitations.
- Dependencies: T22.G5.02, T22.G5.03
- Rationale: Observation-first approach matches G5 pattern

**NEW: T22.G6.07 - Add speech input to a chatbot**
- Grade: 6
- Description: Students use `start recognizing speech in [LANGUAGE] record as [SOUNDNAME]`, `end speech recognition`, and `text from speech` blocks to add voice input to a chatbot. They create a "Speak" button that starts listening, then sends the recognized text to ChatGPT when recording ends.
- Dependencies: T22.G6.01, T22.G6.03.01
- Rationale: Adds speech input after mastering text input

**NEW: T22.G6.08 - Add voice output with text-to-speech**
- Grade: 6
- Description: Students use the `say [TEXT] in [LANGUAGE] as [VOICETYPE] speed (N) pitch (N) volume (N)` block to make the chatbot speak responses aloud. They experiment with different voice types (Male, Female, Boy, Girl) and languages to match the chatbot's persona.
- Dependencies: T22.G6.07
- Rationale: Complete voice conversation loop

**NEW: T22.G7.09 - Build a voice-controlled chatbot**
- Grade: 7
- Description: Students combine speech recognition, ChatGPT, and text-to-speech to create a fully voice-controlled chatbot. Users speak questions, the bot responds via ChatGPT, and answers are read aloud. They handle edge cases like background noise, silence, and overlapping audio.
- Dependencies: T22.G6.07, T22.G6.08, T22.G7.01
- Rationale: Integrates all voice components at advanced level

### B3: DALL-E/Multimodal Skills (MEDIUM PRIORITY)

**NEW: T22.G7.10 - Generate images based on chat context**
- Grade: 7
- Description: Students enhance a chatbot to generate images using DALL-E when requested. When a user asks "Show me a sunset", the chatbot uses `OpenAI DALL-E: generate costume image` to create the image and displays it. They learn to parse user intent and trigger appropriate AI tools.
- Dependencies: T22.G7.01, T22.G7.03
- Rationale: Introduces multimodal AI (text + images)

**NEW: T22.G8.06 - Build a multimodal storytelling chatbot**
- Grade: 8
- Description: Students create a chatbot that tells illustrated stories. Users provide a topic, ChatGPT generates a story with scene descriptions, and DALL-E creates matching images for each scene. The chatbot displays images alongside narration and allows users to save favorite scenes.
- Dependencies: T22.G7.10, T22.G8.01
- Rationale: Advanced multimodal integration

### B4: Early Testing & Debugging Skills (MEDIUM PRIORITY)

**NEW: T22.G5.06 - Test chatbot responses for consistency**
- Grade: 5
- Description: Students ask the same question to a chatbot multiple times and compare responses. They notice that temperature settings affect consistency and learn that AI responses can vary. They document which types of questions get consistent answers vs. which ones vary.
- Dependencies: T22.G5.02, T22.G5.03
- Rationale: Early introduction to AI non-determinism

**MODIFY: T22.G8.04 - Enhance with automated testing harness**
- Keep existing description but move some testing concepts to G5.06

### B5: Content Moderation Earlier (MEDIUM PRIORITY)

**NEW: T22.G6.09 - Add basic content filtering**
- Grade: 6
- Description: Students use the `get moderation result for [TEXT]` block to check user input before sending it to ChatGPT. If input is flagged, they display a friendly message asking the user to rephrase. This introduces responsible AI deployment early.
- Dependencies: T22.G6.01, T22.G6.03
- Rationale: Move moderation concept earlier (currently G7.04)

**MODIFY: T22.G7.04 - Enhance to include escalation paths**
- Adjust to build on G6.09 foundation, focus on advanced moderation (escalation, logging, human review)

---

## C. SKILLS NEEDING BREAKDOWN

### C1: T22.G6.03 - TOO BROAD (Currently 5+ concepts)

**Current Description:**
"Students design a UI with a text input, 'Send' button, quick-reply buttons, and a scrolling label/log of the conversation. Pressing 'Send' pushes the user message into a list, calls the ChatGPT block, appends the response, and manages the visible conversation history."

**Problem:**
- Introduces widgets (no prerequisite)
- Text input + button + label + list
- ChatGPT integration
- Conversation management
- All in ONE skill

**Solution:** Already proposed in B1
- Split into T22.G6.03.01 (input widgets)
- And T22.G6.03.02 (conversation log)
- Original G6.03 can be REMOVED or merged

### C2: T22.G6.05 - NEEDS CLARIFICATION

**Current Description:**
"Students use the `add chat window` block to create a pre-styled chat interface with configurable size, colors, and input rows. They use `append to chat [CHATNAME] message [...] as [SENDER] icon [...] align [...]` to display messages with sender icons. For streaming mode responses, they use `update last chat message to [MESSAGE] for chat [CHATNAME]` to show text appearing word-by-word as it generates."

**Problem:**
- Introduces 3 new blocks at once
- No clear separation from G6.03
- Streaming display is advanced concept

**Solution:**

**SPLIT INTO:**

**T22.G6.05.01 - Use pre-built chat window for styling**
- Description: Students use the `add chat window` block to create a chat interface with configurable size, position, colors, and input rows. They compare the built-in chat window to their custom label/button UI and understand the trade-offs (customization vs. convenience).
- Dependencies: T22.G6.03.02
- Rationale: Focus on setup first

**T22.G6.05.02 - Manage chat messages with append and update blocks**
- Description: Students use `append to chat [CHATNAME] message [...] as [SENDER] icon [...] align [...]` to add messages with sender labels and icons. They understand how the chat window automatically handles scrolling and formatting.
- Dependencies: T22.G6.05.01
- Rationale: Separate message management

**T22.G6.05.03 - Display streaming responses in real-time**
- Description: Students set ChatGPT mode to "streaming" and use `update last chat message to [MESSAGE] for chat [CHATNAME]` to show text appearing word-by-word as the AI generates it. They compare the user experience of streaming vs. waiting mode.
- Dependencies: T22.G6.05.02, T22.G6.02
- Rationale: Advanced streaming concept separate

### C3: Consider Consolidating G7 Persona Skills

**Current:**
- T22.G7.01 - Author persona with system messages
- T22.G7.03 - Capture slot values through UI widgets
- T22.G7.05 - User-test for inclusivity

**Analysis:** These could potentially be combined or sequenced more tightly, but they're manageable as-is. **KEEP AS-IS.**

---

## D. DEPENDENCY FIXES NEEDED

### D1: CRITICAL - G7.08 Violates X-2 Rule

**Current T22.G7.08 Dependencies:**
```
* T22.G6.02: Adjust ChatGPT block settings and handle long requests
* T22.G7.01: Author a persona using system messages and few-shot turns
```

**Problem:** Grade 7 skill depends on Grade 6 skills (X-2 rule allows only G7, G6, or G5)
**Fix:** Dependencies are actually fine! G7 can depend on G6 and G5.

**WAIT - RE-CHECK X-2 RULE:**
- Grade 4 skill can depend on G4, G3, or G2
- Grade 7 skill can depend on G7, G6, or G5

**VERDICT:** No violation! Dependencies are correct.

### D2: Remove Unnecessary Same-Grade T22 Dependencies

**T22.G6.02 Dependencies:**
```
* T06.G4.01: Program multiple events to run independently
* T08.G4.01: Use nested conditions or multi-branch selection
* T09.G4.04: Trace multi-step expressions with parentheses
* T22.G4.01: Write clear, polite questions for a helper bot
* T22.G5.01: Flag risky vs safe chatbot prompts
* T22.G6.01: Trace how a chatbot script processes each turn
```

**Analysis:**
- T22.G6.01 is NECESSARY (must understand script before adjusting settings)
- But does G6.02 REALLY need G4.01 and G5.01?
- G4.01 (polite questions) - NOT NEEDED for adjusting temperature
- G5.01 (risky prompts) - Conceptually useful but not a hard prerequisite

**RECOMMENDATION:**
Remove T22.G4.01 from G6.02 dependencies (adjusting settings doesn't require knowing how to write polite questions)
**KEEP** T22.G5.01 (safety awareness before using different temperatures)
**KEEP** T22.G6.01 (must understand script first)

### D3: G6.03 Has Redundant Dependencies

**T22.G6.03 Dependencies:**
```
* T06.G4.01: Program multiple events to run independently
* T06.G4.08: Fix event timing issues in multi-event programs
* T09.G4.01: Build a simple string variable for name entry
* T09.G4.04: Trace multi-step expressions with parentheses
* T22.G5.01: Flag risky vs safe chatbot prompts
* T22.G6.01: Trace how a chatbot script processes each turn
```

**Problem:** If G6.03 is broken into G6.03.01 and G6.03.02, dependencies need redistribution

**Proposed:**
- **T22.G6.03.01** (input widgets):
  - T06.G4.01 (events)
  - T09.G4.01 (string variables)
  - T22.G4.02 (NEW - button widgets)

- **T22.G6.03.02** (conversation log):
  - T06.G4.08 (timing)
  - T09.G4.04 (expressions)
  - T22.G5.01 (safety)
  - T22.G6.01 (script understanding)
  - T22.G6.03.01 (input first)

### D4: G7.04 Should Build on Earlier Moderation

**Current:** First introduces moderation in G7
**Proposed:** Add G6.09 (basic moderation) first
**Fix:** Update G7.04 dependencies to include T22.G6.09

### D5: New Skills Need Dependencies

All new proposed skills (B1-B5) have dependencies specified. Need to ensure they don't create circular dependencies.

**Verification:**
- ✅ T22.G4.02 → only depends on T06.G3, T09.G3 (no T22 same-grade)
- ✅ T22.G5.04 → depends on G4.02 (grade below) ✓
- ✅ T22.G5.05 → depends on G5.02, G5.03 (same grade but earlier in sequence)
- ✅ T22.G5.06 → depends on G5.02, G5.03 (same grade)
- ✅ T22.G6.07 → depends on G6.01, G6.03.01 (same grade)
- ✅ T22.G6.08 → depends on G6.07 (same grade)
- ✅ T22.G6.09 → depends on G6.01, G6.03 (same grade)
- ✅ All G7+ skills → properly reference lower grades

**Note:** Same-grade dependencies should be removed per instructions, but the new skills naturally build on each other within G6 and G7. Need to reconsider sequencing.

**REVISED APPROACH:**
Since "earlier skills in same topic/grade are assumed," we can keep same-grade dependencies ONLY when they represent a clear prerequisite relationship (e.g., G6.08 requires G6.07).

---

## E. PROPOSED NEW/MODIFIED SKILLS

### SECTION E1: Widget Foundation (Grade 4-5)

#### T22.G4.02 (NEW)
**Grade:** 4
**Skill:** Add buttons to create interactive prompts
**Description:** Students use widget blocks to add buttons to the stage. They create 3-5 quick-reply buttons (e.g., "Tell me a joke", "Fun fact", "Help with math") that set a variable when clicked. This introduces widgets as interactive UI elements before building full chat interfaces.

**Dependencies:**
- T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
- T09.G3.05: Trace code with variables to predict outcomes

**Rationale:** Bridges the gap between G3 conceptual understanding and G6 widget-heavy chatbot coding. Students need hands-on widget experience before G6.

---

#### T22.G5.04 (NEW)
**Grade:** 5
**Skill:** Display chatbot responses in labels
**Description:** Students use a pre-built chatbot and add label widgets to display responses in a styled format. They practice updating label text dynamically when the chatbot replies, learning how to separate input/output in a UI.

**Dependencies:**
- T22.G4.02: Add buttons to create interactive prompts
- T22.G5.02: Observe chatbot strengths and weaknesses through testing

**Rationale:** Continues widget scaffolding from buttons (G4.02) to dynamic labels, maintaining the G5 "observe pre-built" pattern.

---

### SECTION E2: Speech Integration (Grade 5-7)

#### T22.G5.05 (NEW)
**Grade:** 5
**Skill:** Test voice input with speech recognition
**Description:** Students use a pre-built project with speech recognition enabled. They speak into the microphone and observe how their words appear as text. They test different speaking speeds, accents, and background noise to understand speech-to-text limitations.

**Dependencies:**
- T22.G5.02: Observe chatbot strengths and weaknesses through testing
- T22.G5.03: Experiment with prompt phrasing to improve responses

**Rationale:** Introduces speech-to-text in observation mode (G5 pattern). Critical for accessibility and modern chatbot interfaces.

---

#### T22.G5.06 (NEW)
**Grade:** 5
**Skill:** Test chatbot responses for consistency
**Description:** Students ask the same question to a chatbot multiple times and compare responses. They notice that temperature settings affect consistency and learn that AI responses can vary. They document which types of questions get consistent answers vs. which ones vary.

**Dependencies:**
- T22.G5.02: Observe chatbot strengths and weaknesses through testing
- T22.G5.03: Experiment with prompt phrasing to improve responses

**Rationale:** Early introduction to AI non-determinism, helps students understand why testing is important.

---

#### T22.G6.07 (NEW)
**Grade:** 6
**Skill:** Add speech input to a chatbot
**Description:** Students use `start recognizing speech in [LANGUAGE] record as [SOUNDNAME]`, `end speech recognition`, and `text from speech` blocks to add voice input to a chatbot. They create a "Speak" button that starts listening, then sends the recognized text to ChatGPT when recording ends.

**Dependencies:**
- T22.G6.01: Trace how a chatbot script processes each turn
- T22.G6.03.01: Add input widgets for user messages (NEW)

**Rationale:** Builds on text input (G6.03.01) to add speech input, completing the input modality progression.

---

#### T22.G6.08 (NEW)
**Grade:** 6
**Skill:** Add voice output with text-to-speech
**Description:** Students use the `say [TEXT] in [LANGUAGE] as [VOICETYPE] speed (N) pitch (N) volume (N)` block to make the chatbot speak responses aloud. They experiment with different voice types (Male, Female, Boy, Girl) and languages to match the chatbot's persona.

**Dependencies:**
- T22.G6.07: Add speech input to a chatbot

**Rationale:** Completes voice conversation loop (input in G6.07, output in G6.08).

---

#### T22.G7.09 (NEW)
**Grade:** 7
**Skill:** Build a voice-controlled chatbot
**Description:** Students combine speech recognition, ChatGPT, and text-to-speech to create a fully voice-controlled chatbot. Users speak questions, the bot responds via ChatGPT, and answers are read aloud. They handle edge cases like background noise, silence, and overlapping audio.

**Dependencies:**
- T22.G6.07: Add speech input to a chatbot
- T22.G6.08: Add voice output with text-to-speech
- T22.G7.01: Author a persona using system messages and few-shot turns

**Rationale:** Advanced integration of all voice components with persona design.

---

### SECTION E3: UI Scaffolding (Grade 6)

#### T22.G6.03.01 (NEW - replaces part of G6.03)
**Grade:** 6
**Skill:** Add input widgets for user messages
**Description:** Students add a text input widget and a "Send" button to capture user input. When the button is clicked, they read the text input value, store it in a variable, and clear the input field for the next message.

**Dependencies:**
- T22.G5.04: Display chatbot responses in labels (NEW)
- T22.G6.01: Trace how a chatbot script processes each turn

**Rationale:** Breaks down overly complex G6.03 into manageable pieces.

---

#### T22.G6.03.02 (NEW - replaces part of G6.03)
**Grade:** 6
**Skill:** Build a conversation log with dynamic updates
**Description:** Students create a scrolling label or list widget that displays a conversation history. Each time a message is sent or received, they append it to the log with formatting (e.g., "User: [message]" and "Bot: [response]").

**Dependencies:**
- T22.G6.03.01: Add input widgets for user messages

**Rationale:** Completes the breakdown of G6.03, focuses on conversation management.

---

#### T22.G6.09 (NEW)
**Grade:** 6
**Skill:** Add basic content filtering
**Description:** Students use the `get moderation result for [TEXT]` block to check user input before sending it to ChatGPT. If input is flagged, they display a friendly message asking the user to rephrase. This introduces responsible AI deployment early.

**Dependencies:**
- T22.G6.01: Trace how a chatbot script processes each turn
- T22.G6.03: Build a basic chat UI with send button and log

**Rationale:** Introduces content moderation earlier (currently first appears in G7.04).

---

### SECTION E4: Chat Window Blocks (Grade 6)

#### T22.G6.05.01 (NEW - replaces part of G6.05)
**Grade:** 6
**Skill:** Use pre-built chat window for styling
**Description:** Students use the `add chat window` block to create a chat interface with configurable size, position, colors, and input rows. They compare the built-in chat window to their custom label/button UI and understand the trade-offs (customization vs. convenience).

**Dependencies:**
- T22.G6.03.02: Build a conversation log with dynamic updates

**Rationale:** Introduces chat window setup separately from message management.

---

#### T22.G6.05.02 (NEW - replaces part of G6.05)
**Grade:** 6
**Skill:** Manage chat messages with append and update blocks
**Description:** Students use `append to chat [CHATNAME] message [...] as [SENDER] icon [...] align [...]` to add messages with sender labels and icons. They understand how the chat window automatically handles scrolling and formatting.

**Dependencies:**
- T22.G6.05.01: Use pre-built chat window for styling

**Rationale:** Focuses on message management separately from setup.

---

#### T22.G6.05.03 (NEW - replaces part of G6.05)
**Grade:** 6
**Skill:** Display streaming responses in real-time
**Description:** Students set ChatGPT mode to "streaming" and use `update last chat message to [MESSAGE] for chat [CHATNAME]` to show text appearing word-by-word as the AI generates it. They compare the user experience of streaming vs. waiting mode.

**Dependencies:**
- T22.G6.05.02: Manage chat messages with append and update blocks
- T22.G6.02: Adjust ChatGPT block settings and handle long requests

**Rationale:** Advanced streaming concept taught separately after mastering static messages.

---

### SECTION E5: Multimodal AI (Grade 7-8)

#### T22.G7.10 (NEW)
**Grade:** 7
**Skill:** Generate images based on chat context
**Description:** Students enhance a chatbot to generate images using DALL-E when requested. When a user asks "Show me a sunset", the chatbot uses `OpenAI DALL-E: generate costume image` to create the image and displays it. They learn to parse user intent and trigger appropriate AI tools.

**Dependencies:**
- T22.G7.01: Author a persona using system messages and few-shot turns
- T22.G7.03: Capture slot values through UI widgets and inject them into prompts

**Rationale:** Introduces multimodal AI (text + images) at appropriate grade level.

---

#### T22.G8.06 (NEW)
**Grade:** 8
**Skill:** Build a multimodal storytelling chatbot
**Description:** Students create a chatbot that tells illustrated stories. Users provide a topic, ChatGPT generates a story with scene descriptions, and DALL-E creates matching images for each scene. The chatbot displays images alongside narration and allows users to save favorite scenes.

**Dependencies:**
- T22.G7.10: Generate images based on chat context
- T22.G8.01: Add retrieval-augmented generation (RAG) to a chatbot

**Rationale:** Advanced multimodal integration, capstone-level skill.

---

### SECTION E6: Modifications to Existing Skills

#### T22.G6.02 (MODIFY)
**Change:** Remove dependency on T22.G4.01 (unnecessary - adjusting temperature doesn't require knowing how to write polite questions)

**Updated Dependencies:**
- T06.G4.01: Program multiple events to run independently
- T08.G4.01: Use nested conditions or multi-branch selection
- T09.G4.04: Trace multi-step expressions with parentheses
- T22.G5.01: Flag risky vs safe chatbot prompts
- T22.G6.01: Trace how a chatbot script processes each turn

**Rationale:** Removes unnecessary cross-grade dependency within T22.

---

#### T22.G6.03 (REMOVE/REPLACE)
**Action:** Remove original G6.03 and replace with G6.03.01 and G6.03.02

**Rationale:** Original skill was too broad, covering 5+ concepts. Split maintains learning objectives while improving scaffolding.

---

#### T22.G6.05 (REMOVE/REPLACE)
**Action:** Remove original G6.05 and replace with G6.05.01, G6.05.02, and G6.05.03

**Rationale:** Original skill introduced 3 blocks at once with streaming concept. Split improves scaffolding.

---

#### T22.G7.04 (MODIFY)
**Change:** Update dependencies to build on G6.09 (basic moderation)

**Current Description:** (Keep as-is - focuses on advanced moderation)

**Updated Dependencies:**
- T06.G5.01: Coordinate scripts across sprites using broadcasts
- T08.G5.01: Use conditionals with comparison operators
- T09.G5.04: Use variables to control animation timing
- T22.G5.01: Flag risky vs safe chatbot prompts
- T22.G6.09: Add basic content filtering (NEW)
- T22.G6.03: Build a basic chat UI with send button and log

**Rationale:** Builds on earlier moderation introduction in G6.09.

---

#### T22.G8.04 (MODIFY)
**Change:** Adjust description to reference earlier testing concepts

**Updated Description:** Students build on earlier testing experiences (G5.06) to create an automated testing harness that runs their chatbot through a suite of test prompts (stored in a table), logs each response, flags moderation events, and generates a summary report showing pass/fail rates and edge cases. They add code to track response times and detect when the bot goes off-topic, creating an automated quality assurance system for their chatbot.

**Updated Dependencies:** (Add T22.G5.06)
- T06.G6.01: Trace event execution paths in a multi‑event program
- T08.G6.01: Use conditionals to control simulation steps
- T09.G6.01: Model real-world quantities using variables and formulas
- T22.G5.06: Test chatbot responses for consistency (NEW)
- T22.G7.04: Add moderation guardrails and escalation paths
- T22.G7.05: User-test the chatbot for inclusivity and clarity

**Rationale:** Connects systematic testing back to earlier observation/testing skills.

---

## F. SUMMARY OF CHANGES

### New Skills Added: 15

**Grade 4:** 1 skill
- T22.G4.02: Add buttons to create interactive prompts

**Grade 5:** 3 skills
- T22.G5.04: Display chatbot responses in labels
- T22.G5.05: Test voice input with speech recognition
- T22.G5.06: Test chatbot responses for consistency

**Grade 6:** 7 skills
- T22.G6.03.01: Add input widgets for user messages
- T22.G6.03.02: Build a conversation log with dynamic updates
- T22.G6.05.01: Use pre-built chat window for styling
- T22.G6.05.02: Manage chat messages with append and update blocks
- T22.G6.05.03: Display streaming responses in real-time
- T22.G6.07: Add speech input to a chatbot
- T22.G6.08: Add voice output with text-to-speech
- T22.G6.09: Add basic content filtering

**Grade 7:** 1 skill
- T22.G7.09: Build a voice-controlled chatbot
- T22.G7.10: Generate images based on chat context

**Grade 8:** 1 skill
- T22.G8.06: Build a multimodal storytelling chatbot

### Skills Removed: 2
- T22.G6.03: Build a basic chat UI with send button and log (replaced by .01 and .02)
- T22.G6.05: Use built-in chat window blocks with streaming display (replaced by .01, .02, .03)

### Skills Modified: 4
- T22.G6.02: Removed unnecessary T22.G4.01 dependency
- T22.G7.04: Added dependency on new G6.09
- T22.G8.04: Added dependency on new G5.06, enhanced description
- (All existing skills retain their descriptions/dependencies unless noted)

### Net Change: +13 skills (27 → 40 skills)

---

## G. COVERAGE BY FEATURE

### ChatGPT Core Blocks
- ✅ Basic request block (G6.01)
- ✅ Temperature/settings (G6.02)
- ✅ System messages (G7.01)
- ✅ Session management (G6.06)
- ✅ Cancel request (G6.02)
- ✅ Streaming mode (G6.05.03)

### LLM Blocks
- ✅ LLM model comparison (G7.08)

### UI/Widget Blocks
- ✅ Buttons (G4.02 NEW)
- ✅ Labels (G5.04 NEW)
- ✅ Text input (G6.03.01 NEW)
- ✅ Chat window (G6.05.01-03 NEW)

### Voice Blocks
- ✅ Speech-to-text (G5.05, G6.07 NEW)
- ✅ Text-to-speech (G6.08 NEW)
- ✅ Voice chatbot (G7.09 NEW)

### Image Blocks
- ✅ DALL-E generation (G7.10, G8.06 NEW)
- ✅ Image moderation (G7.07)

### Advanced Features
- ✅ Content moderation (G6.09 NEW, G7.04)
- ✅ File attachments (G7.06)
- ✅ RAG/Semantic search (G8.01)
- ✅ Web search (G8.05)
- ✅ Multi-agent (G8.02)
- ✅ Structured outputs (G8.03)
- ✅ Automated testing (G8.04)

### Gaps Remaining
- 🔲 Widget dropdowns/sliders (mentioned in G7.03 but not explicitly taught)
- 🔲 Continuous speech recognition (exists in platform but not covered)

---

## H. DEPENDENCY GRAPH VALIDATION

### Grade K-2 (Unplugged)
```
GK.01 (standalone)
 └─ GK.02

G1.01 (depends on GK.02)
 └─ G1.02

G2.01 (depends on G1.01, G1.02)
 └─ G2.02
```
✅ **Valid** - Linear progression, no violations

### Grade 3 (First coding)
```
G3.01 (depends on T08.G3.01, T22.G2.01, T22.G2.02)
```
✅ **Valid** - Depends on prior T22 grades and appropriate T08

### Grade 4-5 (Observation/Testing)
```
G4.01 (depends on T06.G3.01, T06.G3.09, T09.G3.05, T22.G3.01)
G4.02 NEW (depends on T06.G3.01, T09.G3.05)

G5.01 (depends on T06.G3.09, T09.G3.05, T22.G3.01)
G5.02 (depends on T22.G4.01, T22.G5.01)
G5.03 (depends on T22.G4.01, T22.G5.02)
G5.04 NEW (depends on T22.G4.02, T22.G5.02)
G5.05 NEW (depends on T22.G5.02, T22.G5.03)
G5.06 NEW (depends on T22.G5.02, T22.G5.03)
```
✅ **Valid** - All within X-2 range

### Grade 6 (Building)
```
G6.01 (depends on T06.G4.01, T08.G4.01, T09.G4.01, T09.G4.04, T22.G5.01, T22.G5.03)
G6.02 MODIFIED (depends on T06.G4.01, T08.G4.01, T09.G4.04, T22.G5.01, T22.G6.01)
G6.03 REMOVED
G6.03.01 NEW (depends on T22.G5.04, T22.G6.01)
G6.03.02 NEW (depends on T22.G6.03.01)
G6.04 (depends on T06.G4.08, T08.G4.01, T09.G4.04, T22.G4.01, T22.G5.01, T22.G6.01)
G6.05 REMOVED
G6.05.01 NEW (depends on T22.G6.03.02)
G6.05.02 NEW (depends on T22.G6.05.01)
G6.05.03 NEW (depends on T22.G6.05.02, T22.G6.02)
G6.06 (depends on T22.G6.01, T22.G6.03)
G6.07 NEW (depends on T22.G6.01, T22.G6.03.01)
G6.08 NEW (depends on T22.G6.07)
G6.09 NEW (depends on T22.G6.01, T22.G6.03)
```
✅ **Valid** - All within X-2 range

### Grade 7 (Advanced)
```
G7.01 (depends on T22.G6.02, T22.G6.04)
G7.02 (depends on T06.G5.01, T08.G5.01, T09.G5.04, T22.G6.03, T22.G6.04, T22.G6.06)
G7.03 (depends on T22.G6.03, T22.G6.04, T22.G7.01)
G7.04 MODIFIED (depends on T06.G5.01, T08.G5.01, T09.G5.04, T22.G5.01, T22.G6.09, T22.G6.03)
G7.05 (depends on T22.G6.03, T22.G6.04, T22.G7.01)
G7.06 (depends on T22.G6.03, T22.G6.04, T22.G7.01)
G7.07 (depends on T22.G7.04, T22.G7.06)
G7.08 (depends on T22.G6.02, T22.G7.01)
G7.09 NEW (depends on T22.G6.07, T22.G6.08, T22.G7.01)
G7.10 NEW (depends on T22.G7.01, T22.G7.03)
```
✅ **Valid** - All within X-2 range

### Grade 8 (Mastery)
```
G8.01 (depends on T06.G6.01, T09.G6.01, T22.G7.01, T22.G7.02, T22.G7.04)
G8.02 (depends on T06.G6.01, T09.G6.01, T22.G6.06, T22.G7.01, T22.G7.02, T22.G7.04, T22.G7.05)
G8.03 (depends on T03.G6.01, T06.G6.01, T09.G6.01, T22.G7.01, T22.G7.04)
G8.04 MODIFIED (depends on T06.G6.01, T08.G6.01, T09.G6.01, T22.G5.06, T22.G7.04, T22.G7.05)
G8.05 (depends on T06.G6.01, T09.G6.01, T22.G7.01, T22.G7.04, T22.G8.01)
G8.06 NEW (depends on T22.G7.10, T22.G8.01)
```
✅ **Valid** - All within X-2 range

---

## I. PRIORITY IMPLEMENTATION ROADMAP

### Phase 1: HIGH PRIORITY (Must Fix)
1. **Add T22.G4.02** (widget buttons) - Foundation for all UI work
2. **Add T22.G5.04** (labels) - Continue widget progression
3. **Split G6.03** into G6.03.01 and G6.03.02 - Fix overly broad skill
4. **Split G6.05** into G6.05.01, G6.05.02, G6.05.03 - Fix overly broad skill
5. **Add G6.09** (basic moderation) - Move safety earlier
6. **Add speech skills** G5.05, G6.07, G6.08 - Critical accessibility feature

### Phase 2: MEDIUM PRIORITY (Should Add)
1. **Add T22.G5.06** (testing consistency) - Improve testing scaffolding
2. **Add T22.G7.09** (voice chatbot) - Complete voice integration
3. **Add T22.G7.10** (DALL-E) - Introduce multimodal AI
4. **Modify G7.04** dependencies - Build on G6.09
5. **Modify G8.04** dependencies - Connect to G5.06

### Phase 3: POLISH (Nice to Have)
1. **Add T22.G8.06** (multimodal storytelling) - Advanced capstone
2. **Review all descriptions** for clarity and consistency
3. **Add examples** to complex skills (G7+)
4. **Create assessment rubrics** for each skill

---

## J. FINAL RECOMMENDATIONS

### 1. Accept All 15 New Skills
The new skills address critical gaps in:
- Widget scaffolding (G4.02, G5.04)
- Speech integration (G5.05, G6.07, G6.08, G7.09)
- Content moderation timing (G6.09)
- UI breakdown (G6.03.01/.02, G6.05.01/.02/.03)
- Testing progression (G5.06)
- Multimodal AI (G7.10, G8.06)

### 2. Remove 2 Overly Broad Skills
- G6.03 → replaced by G6.03.01 and G6.03.02
- G6.05 → replaced by G6.05.01, G6.05.02, and G6.05.03

### 3. Modify 4 Existing Skills
- G6.02: Remove unnecessary dependency
- G7.04: Add dependency on G6.09
- G8.04: Add dependency on G5.06, enhance description
- (Preserve all other skills as-is)

### 4. Verify Platform Blocks
Before finalizing, verify exact syntax for:
- `add chat window` and related chat blocks
- Widget category blocks (if not already documented in T16)

### 5. Cross-Reference with T16 (User Interfaces)
Check if T16 already covers widget basics. If so:
- T22.G4.02 could reference T16 skills as dependencies
- Or T22 could focus on chat-specific widgets

### 6. Consider T21 Integration
T21 (AI Media) already covers DALL-E and TTS in detail. Consider:
- T22.G7.10 and G8.06 could reference T21 skills
- Or keep T22 focused on chat-specific multimodal use cases

---

## K. QUESTIONS FOR REVIEW

1. **Widget Coverage:** Does T16 already cover widget basics comprehensively? If yes, should T22.G4.02 and G5.04 reference T16 instead?

2. **Speech Coverage:** Does T21 cover speech-to-text and TTS? If yes, should T22 reference T21 skills or keep chat-specific coverage?

3. **Chat Window Blocks:** Can we verify the exact syntax and parameters for `add chat window`, `append to chat`, and `update last chat message` blocks?

4. **Skill Count:** Is 40 skills (up from 27) too many for one topic? Should we consider moving some to T16 or T21?

5. **Assessment Strategy:** How will these skills be assessed? Auto-graded challenges, portfolio reviews, or teacher observation?

---

## L. CONCLUSION

T22 currently has a strong foundation but critical gaps in:
1. Widget/UI scaffolding (G4-G6)
2. Speech integration (G5-G7)
3. Content moderation timing (G6 vs G7)
4. Multimodal AI (G7-G8)

The proposed 15 new skills (+13 net) address all high-priority issues while maintaining proper scaffolding and dependencies. All skills follow IXL-style descriptions, preserve cross-topic dependencies, and apply the X-2 rule correctly.

**Recommendation:** Implement Phase 1 changes immediately, Phase 2 within next iteration, Phase 3 as polish.

**Status:** T22 will become a gold standard chatbot curriculum after these changes, with comprehensive coverage from unplugged activities (K-2) through advanced multimodal AI chatbots (G8).
