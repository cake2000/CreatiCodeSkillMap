# T22 (Chatbots & Prompting) - COMPREHENSIVE ANALYSIS
## Comparison Against CreatiCode AI Blocks

**Analysis Date**: 2025-11-23
**Current Skills File**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/skills_T22_chatbots.md`
**AI Blocks Reference**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/AI_BLOCKS_COMPLETE_REFERENCE.md`

---

## EXECUTIVE SUMMARY

### Overall Assessment: MAJOR ISSUES IDENTIFIED

**Total Skills Analyzed**: 17 (G3-G8, excluding K-2 concept-only skills)
**Skills with Issues**: 12 (71%)
**Skills Ready for Implementation**: 5 (29%)

### Critical Problems:
1. **Missing Critical Features**: Chat window blocks never taught
2. **Overly Broad Skills**: Several skills try to teach too much at once
3. **Scaffolding Gaps**: Sudden jumps in complexity, missing intermediate steps
4. **Dependency Issues**: Skills depend on concepts not yet introduced
5. **Inaccurate Block References**: Some skills reference features incorrectly

---

## PART 1: MAJOR ISSUES (MUST FIX)

### 1.1 OVERLY BROAD SKILLS - Need Breaking Down

#### **T22.G6.03 – Build a basic chat UI with send button and log**
**Problem**: Tries to teach TOO MUCH in one skill
- Text input widget creation
- Button widget creation
- Quick-reply buttons (multiple)
- Scrolling label/log
- List management (conversation history)
- Displaying with timestamps
- Resetting input fields
- Managing "latest 6 turns visible"

**Recommended Fix**: Break into sub-skills:
- **T22.G6.03.01**: Add UI widgets (text input, send button, display label)
- **T22.G6.03.02**: Capture user input and display it
- **T22.G6.03.03**: Store conversation in a list variable
- **T22.G6.03.04**: Display conversation history with timestamps
- **T22.G6.03.05**: Manage conversation length (keep latest N turns)

---

#### **T22.G7.01 – Author a persona using system messages and few-shot turns**
**Problem**: Combines too many advanced concepts:
- Understanding system messages
- Writing few-shot examples
- Embedding them in code
- Maintaining character consistency

**Recommended Fix**: Break into sub-skills:
- **T22.G7.01.01**: Use system request block to set chatbot personality
- **T22.G7.01.02**: Write example dialogue (few-shot) to model tone
- **T22.G7.01.03**: Combine system message + examples for consistent persona

---

#### **T22.G7.04 – Add moderation guardrails and escalation paths**
**Problem**: Too many concepts at once:
- Text moderation block usage
- Output moderation
- Pre-written fallback messages
- Incident logging
- Escalation UI/logic
- Preventing LLM re-calls

**Recommended Fix**: Break into sub-skills:
- **T22.G7.04.01**: Use moderation block to check user input
- **T22.G7.04.02**: Handle moderation failures with fallback messages
- **T22.G7.04.03**: Log incidents and create escalation path

---

#### **T22.G8.01 – Add retrieval-augmented generation (RAG) to a chatbot**
**Problem**: Extremely complex, introduces multiple new concepts:
- Table data structures
- Semantic database creation
- Embedding vectors (abstract concept)
- Search queries
- Prepending retrieved data to prompts
- Citation display
- No-match handling

**Recommended Fix**: Break into sub-skills:
- **T22.G8.01.01**: Create semantic database from table data
- **T22.G8.01.02**: Search semantic database and retrieve results
- **T22.G8.01.03**: Integrate search results into ChatGPT prompts
- **T22.G8.01.04**: Display citations and handle no-match cases

---

#### **T22.G8.02 – Coordinate multi-agent conversations and summaries**
**Problem**: Too advanced, multiple complex concepts:
- Multiple ChatGPT sessions
- Session ID management
- Turn-taking logic with broadcasts
- Labeled logs for each agent
- Moderator role
- Summary generation

**Recommended Fix**: Break into sub-skills:
- **T22.G8.02.01**: Switch between multiple chatbot threads (select chatbot block)
- **T22.G8.02.02**: Coordinate turn-taking between two chatbots
- **T22.G8.02.03**: Create a moderator bot that summarizes conversations

---

### 1.2 MISSING CRITICAL SKILLS

#### **MISSING: Chat Window Blocks (Category 3)**
**Available Blocks NOT Taught**:
- `add chat window` (creates chat UI automatically)
- `append to chat [CHATNAME] message [...]` (adds messages to chat)
- `update last chat message to [MESSAGE]` (updates streaming responses)

**Problem**: T22.G6.03 teaches manual UI building with widgets, but never introduces the dedicated chat window blocks that CreatiCode provides!

**Recommended New Skills**:
- **T22.G6.05.01**: Add a chat window widget to display conversations
- **T22.G6.05.02**: Append messages to chat window (user and bot)
- **T22.G6.05.03**: Update chat messages during streaming mode

---

#### **MISSING: File Attachments to Chat**
**Available Blocks NOT Taught**:
- `attach files to chat` (local file attachment)
- `attach file from Google Drive [URL] to chat` (cloud file attachment)

**Problem**: T22.G7 mentions file attachments in G7.04 description but never actually teaches how to use these blocks.

**Recommended New Skill**:
- **T22.G7.06**: Attach files and images to chat requests

---

#### **MISSING: ChatGPT Cancel Block**
**Available Block NOT Taught**:
- `OpenAI ChatGPT: cancel request`

**Recommended Addition**: Add to T22.G6.02 or create new skill for managing long-running requests.

---

#### **MISSING: Generic LLM Blocks**
**Available Blocks NOT Taught**:
- `LLM model [PROVIDER] request [PROMPT]...` (alternative to ChatGPT)
- `LLM set system instruction [INSTRUCTION] for model [PROVIDER]`

**Recommended New Skill**:
- **T22.G7.08**: Compare different LLM providers (small vs large models)

---

#### **MISSING: Image Moderation**
**Available Blocks NOT Taught**:
- `get moderation result for image at URL [INPUT]`
- `get moderation result for costume named [INPUT]`

**Problem**: T22.G7.04 only teaches text moderation, but CreatiCode supports image moderation too.

**Recommended Addition**: Expand T22.G7.04 or create T22.G7.05 for image content moderation.

---

### 1.3 INACCURATE DESCRIPTIONS

#### **T22.G6.01 – Trace how a chatbot script processes each turn**
**Issue**: Description says "read a pre-built CreatiCode project" but doesn't specify:
- How to access example projects
- What blocks to look for specifically
- How conversation log lists work (which blocks manage them)

**Fix**: Add specific details:
- "Students examine a project using `OpenAI ChatGPT: request` block"
- "Identify how the conversation list stores [user message, bot response] pairs"
- "Trace when `session [new chat v]` vs `session [continue v]` is used"

---

#### **T22.G6.02 – Tune ChatGPT block settings**
**Issue 1**: Says "mode (streaming vs. waiting)" but doesn't explain:
- What streaming actually does (updates variable in real-time)
- When to use waiting (simpler, waits for full response)
- That streaming responses end with ✅ emoji

**Issue 2**: Says "max tokens" but AI_BLOCKS_COMPLETE_REFERENCE.md says:
> "Due to changes in OpenAI's API, this parameter became obsolete and is generally ignored"

**Fix**:
- Remove or de-emphasize "max tokens" parameter
- Add detail about streaming emoji indicator
- Explain when each mode is appropriate

---

#### **T22.G6.03 – Build a basic chat UI with send button and log**
**Issue**: Says "keeps only the latest six turns visible" but:
- Doesn't explain HOW to implement this (list slicing? conditional display?)
- Why 6? (arbitrary number, should be a learning decision)

**Fix**: Change to "implement conversation length management (e.g., display latest 6 turns)"

---

#### **T22.G7.01 – Author a persona using system messages and few-shot turns**
**Issue**: Says "embed these in the ChatGPT block (system request + prompt prefix)" but:
- There are TWO separate blocks: `openaichatcompletion` and `openaichatcompletionsystem`
- Doesn't clarify that system message goes in separate block
- "Prompt prefix" is unclear - does this mean prepending to each user message?

**Fix**: Clarify the two-block approach:
- "Use `OpenAI ChatGPT: system request` block to set personality"
- "Add few-shot examples to the system message OR prepend them to first user prompt"

---

#### **T22.G7.02 – Manage chat history and reset logic**
**Issue**: Says "switch the ChatGPT block's session mode" but:
- The session parameter is PART of the main ChatGPT request block
- Not a separate "mode" you "switch"
- Description implies dynamic switching mid-conversation

**Fix**: Clarify:
- "Use `session [new chat v]` to start fresh conversation"
- "Use `session [continue v]` to maintain context from previous turns"
- "Add 'New Chat' button that sets session to [new chat v] on next request"

---

#### **T22.G8.01 – Add retrieval-augmented generation (RAG)**
**Issue 1**: Says "build a Pinecone semantic index" but:
- CreatiCode abstracts this away
- Block is `create semantic database from table [...]`
- No mention of "Pinecone" needed in student-facing description

**Issue 2**: Says "when no match is found" but:
- Doesn't specify what "no match" means (low similarity score? empty results?)
- Doesn't explain how to detect this condition

**Fix**:
- "Create semantic database using `create semantic database from table` block"
- "Search returns top K results - check if table is empty to detect no matches"

---

### 1.4 GRADE APPROPRIATENESS ISSUES

#### **T22.G6.04 – Debug off-topic responses by rewriting prompts**
**Problem**: Grade 6 is too early for debugging AI behavior
- Requires understanding of:
  - How LLMs interpret instructions
  - Why models "ramble" or "refuse"
  - Iterative prompt engineering
  - System vs user messages (not yet taught!)

**Recommended Fix**: Move to Grade 7 (after T22.G7.01 which teaches system messages)

---

#### **T22.G8.03 – Parse structured chatbot outputs to trigger tools**
**Problem**: Extremely advanced for Grade 8 first attempt:
- JSON parsing (not a Scratch/CreatiCode strength)
- String validation
- Conditional tool routing
- Error handling for malformed responses

**Recommended Fix**:
- Either break into sub-skills
- OR move to advanced capstone (after more JSON/parsing practice)

---

## PART 2: DEPENDENCY ISSUES (WITHIN T22)

### 2.1 MISSING PREREQUISITES

#### **T22.G6.03 depends on widget knowledge (not in T22)**
**Problem**:
- Skill says "Students design a UI with text input, 'Send' button..."
- But NEVER teaches how to create widgets!
- Widget creation is T16 (UI & Widgets), but no T16 dependencies listed

**Fix**: Add dependencies:
- T16.G5.01 (or appropriate widget skill)
- OR create T22.G6.02.01 to introduce widgets in context

---

#### **T22.G7.01 depends on system messages (taught in same skill)**
**Problem**:
- System message block (`openaichatcompletionsystem`) never introduced before G7.01
- G7.01 is the FIRST time students see it
- But it's taught AS IF students already know it exists

**Fix**: Create earlier skill:
- **T22.G6.05**: Introduce system request block to set chatbot instructions

---

#### **T22.G7.03 depends on slot/form concepts (never taught)**
**Problem**:
- Skill says "gather key facts (age range, preferred topic, mood)" via widgets
- But never taught the CONCEPT of "slots" or structured data collection
- No prior skill explains form-driven chatbots

**Fix**: Add foundational skill:
- **T22.G7.02.01**: Understand slot-filling (collecting required info before API call)

---

#### **T22.G7.04 depends on understanding moderation (never taught)**
**Problem**:
- First time seeing moderation blocks
- No explanation of what "Pass"/"Fail" means
- No prior discussion of content safety

**Fix**: Add earlier skill:
- **T22.G6.07**: Understand content moderation and use moderation block

---

#### **T22.G8.01 depends on tables (taught in different topic)**
**Problem**:
- RAG requires table creation, manipulation
- Tables are T29 (Text & Data NLP)
- No T29 dependencies listed

**Fix**: Add dependency:
- T29.G6.01 or appropriate table skill

---

### 2.2 SKILLS DEPENDING ON LATER SKILLS (Forward References)

**GOOD NEWS**: No forward references detected within T22 after review.

All dependencies point to earlier grade levels within T22.

---

### 2.3 UNNECESSARY SAME-GRADE DEPENDENCIES

#### **T22.G6.04 depends on T22.G6.01**
**Analysis**:
- G6.01 is about tracing code
- G6.04 is about debugging prompts
- Dependency makes sense (need to trace before debug)
- **VERDICT**: Keep

---

#### **T22.G7.02 depends on T22.G7.01**
**Analysis**:
- G7.01 teaches system messages
- G7.02 teaches session management
- Could be independent, but system messages help with context management
- **VERDICT**: Questionable - could remove dependency

---

### 2.4 X-2 RULE VIOLATIONS

**Analysis**: All skills reviewed for X-2 rule compliance (skills at grade X can only depend on X, X-1, X-2)

**VIOLATIONS FOUND**: None

- G6 skills depend on G4, G5, G6 ✓
- G7 skills depend on G5, G6, G7 ✓
- G8 skills depend on G6, G7, G8 ✓

---

## PART 3: SCAFFOLDING GAPS

### 3.1 MISSING INTERMEDIATE STEPS

#### **Gap 1: G5 → G6 Jump**
**Current**:
- G5.01: Flag risky vs safe prompts (concept-only)
- G6.01: Trace full chatbot script (coding with ChatGPT blocks)

**Missing Steps**:
- How to add ChatGPT block to project
- First API call with simple prompt
- Understanding the result variable
- Displaying the response

**Recommended New Skill**:
- **T22.G5.02**: Make first ChatGPT request (ask question, display answer)

---

#### **Gap 2: G6 Parameter Tuning → G7 Advanced Features**
**Current**:
- G6.02: Tune temperature, length, mode
- G7.01: Write system messages and few-shot examples

**Missing Steps**:
- What IS a system message?
- How does it differ from user prompts?
- Simple example of using system block

**Recommended New Skill**:
- **T22.G6.05**: Use system request block to set chatbot role

---

#### **Gap 3: Basic Chat → Moderation**
**Current**:
- G6.03: Build basic chat UI
- G7.04: Add moderation guardrails

**Missing Steps**:
- What is content moderation?
- When to use it
- What "Pass" and "Fail" mean
- Simple moderation on user input only

**Recommended New Skill**:
- **T22.G7.03**: Check user input with moderation block

---

#### **Gap 4: Session Management → RAG**
**Current**:
- G7.02: Manage chat history and reset logic
- G8.01: Add retrieval-augmented generation

**Missing Steps**:
- What is semantic search?
- How is it different from keyword search?
- Understanding embedding vectors (conceptually)
- Creating simple semantic database

**Recommended New Skills**:
- **T22.G7.09**: Understand semantic search vs keyword search (concept)
- **T22.G8.01.01**: Create semantic database from table
- **T22.G8.01.02**: Search semantic database and use results

---

### 3.2 SUDDEN COMPLEXITY JUMPS

#### **Jump 1: G6.03 (Basic UI) → G6.04 (Debug AI Behavior)**
**Problem**:
- G6.03 is about UI construction
- G6.04 is about understanding AI failure modes
- Huge conceptual leap

**Fix**: Insert intermediate skills:
- Understanding why AI gives wrong answers
- Reading AI responses critically
- Simple prompt rewording

---

#### **Jump 2: G7.03 (Slot Values) → G7.04 (Moderation)**
**Problem**:
- G7.03 is about form inputs
- G7.04 is about content safety
- Completely different domains

**Fix**: Reorder or add transition skill about when/why safety matters

---

#### **Jump 3: G8.02 (Multi-Agent) → G8.03 (Parse JSON)**
**Problem**:
- G8.02 is about conversation coordination
- G8.03 is about structured data parsing
- JSON is a new, advanced concept

**Fix**: Add earlier JSON introduction or break G8.03 into smaller steps

---

## PART 4: ALIGNMENT WITH CREATICODE BLOCKS

### 4.1 BLOCKS USED CORRECTLY

| Skill | Block(s) Referenced | Correct Usage |
|-------|-------------------|---------------|
| T22.G6.01 | `OpenAI ChatGPT: request` | ✓ Accurate |
| T22.G6.02 | Temperature, mode, length, session | ✓ Mostly accurate (length obsolete) |
| T22.G7.01 | System request | ✓ Accurate |
| T22.G7.02 | Session parameter | ✓ Accurate (but description unclear) |
| T22.G7.04 | `get moderation result for [TEXT]` | ✓ Accurate |
| T22.G8.01 | `create semantic database`, `search semantic database` | ✓ Accurate |

---

### 4.2 BLOCKS REFERENCED INCORRECTLY

| Skill | Issue | Correction Needed |
|-------|-------|-------------------|
| T22.G6.02 | Says "max tokens" controls length | Update: parameter obsolete, use prompt instead |
| T22.G6.03 | Implies manual list management | Should mention `add chat window` block as alternative |
| T22.G7.01 | Unclear about system block vs main block | Specify two separate blocks |
| T22.G7.02 | Says "switch session mode" | Clarify: session is parameter, not mode toggle |

---

### 4.3 BLOCKS NEVER TAUGHT (But Available)

**From AI_BLOCKS_COMPLETE_REFERENCE.md (43 total AI blocks)**

#### Category 3: ChatGPT/LLM (9 blocks)
- ✓ `openaichatcompletion` - Taught in G6.01+
- ✓ `openaichatcompletionsystem` - Taught in G7.01
- **✗ `openai_chatgpt_cancel`** - NEVER TAUGHT
- **✗ `llmchatcompletion`** - NEVER TAUGHT (generic LLM)
- **✗ `llmsysteminstruction`** - NEVER TAUGHT
- ✓ `switchchatbot` - Taught in G8.02
- **✗ `attachimagetochat`** - NEVER TAUGHT (mentioned in G7.04 but not detailed)
- **✗ `attachfilestochat`** - NEVER TAUGHT
- **✗ `attachgooglefiletochat`** - NEVER TAUGHT

#### Category 5: Content Moderation (3 blocks)
- ✓ `getmoderationresult` (text) - Taught in G7.04
- **✗ `getmoderationresult2` (image URL)** - NEVER TAUGHT
- **✗ `getmoderationresult3` (costume)** - NEVER TAUGHT

#### Category 12: Semantic Search (3 blocks)
- ✓ `addtabletopinecone` - Taught in G8.01
- ✓ `searchfrompinecone` - Taught in G8.01
- ✓ `searchfrompinecone2` (with WHERE conditions) - Mentioned in G8.01

#### Category 13: Web Search (1 block)
- **✗ `googlesearch`** - NEVER TAUGHT
  - Block: `web search [QUERY] store top (K) in table [TABLE v]`
  - Perfect for G8 skill about web-augmented chatbots!

---

### 4.4 CHAT WINDOW BLOCKS (Critical Missing Feature)

**Available Blocks NOT in Current Skills**:
```
add chat window
append to chat [CHATNAME] message [...]
update last chat message to [MESSAGE]
```

**Problem**: T22 teaches manual chat UI building (T22.G6.03) but never introduces these purpose-built blocks!

**Impact**: Students spend time reinventing what CreatiCode already provides.

**Recommended Skills**:
- **T22.G6.05.01**: Add chat window widget
- **T22.G6.05.02**: Append messages to chat window
- **T22.G6.05.03**: Update streaming messages in chat window

---

## PART 5: SPECIFIC SKILL-BY-SKILL RECOMMENDATIONS

### Grade 3-5 (Concept-Only Skills)

#### T22.G3.01 – Tell chatbot behavior from fixed button replies
**Status**: ✓ GOOD
**Issues**: None
**Recommendation**: Keep as-is

---

#### T22.G4.01 – Write clear, polite questions for a helper bot
**Status**: ✓ GOOD
**Issues**: None
**Recommendation**: Keep as-is

---

#### T22.G5.01 – Flag risky vs safe chatbot prompts
**Status**: ✓ GOOD
**Issues**: None
**Recommendation**: Keep as-is

---

### Grade 6 Skills

#### T22.G6.01 – Trace how a chatbot script processes each turn
**Status**: ⚠ NEEDS REVISION
**Issues**:
1. Too vague about what to trace
2. Doesn't specify blocks by name
3. No mention of how session parameter affects memory

**Recommendation**:
- Add specific block names
- Clarify what "conversation log list" means
- Show example of list structure: `["User: hello", "Bot: Hi there!", "User: how are you", "Bot: I'm well!"]`

---

#### T22.G6.02 – Tune ChatGPT block settings for tone and length
**Status**: ⚠ NEEDS REVISION
**Issues**:
1. "Max tokens" parameter is obsolete
2. Doesn't explain streaming emoji indicator (✅)
3. Temperature range and effects unclear

**Recommendation**:
- Remove or de-emphasize "length" parameter
- Add: "Streaming mode shows ✅ when complete"
- Clarify: "Temperature 0 = consistent, 1 = creative"

---

#### T22.G6.03 – Build a basic chat UI with send button and log
**Status**: ⚠ MAJOR REVISION NEEDED
**Issues**:
1. Too broad (8+ concepts)
2. Missing widget prerequisite dependencies
3. Never mentions chat window blocks as alternative

**Recommendation**:
**SPLIT INTO 5 SUB-SKILLS**:
- **T22.G6.03.01**: Add UI widgets (text input, button, label)
- **T22.G6.03.02**: Capture and display user input
- **T22.G6.03.03**: Store conversation in list variable
- **T22.G6.03.04**: Display conversation with timestamps
- **T22.G6.03.05**: Manage conversation length

**ALTERNATIVE**: Replace with chat window blocks:
- **T22.G6.03**: Add chat window and send messages

---

#### T22.G6.04 – Debug off-topic responses by rewriting prompts
**Status**: ⚠ NEEDS REVISION
**Issues**:
1. Too early for Grade 6 (requires understanding of system messages)
2. "Edit the system message" but system messages not taught yet!
3. Should come after G7.01

**Recommendation**:
**MOVE TO G7.05** (after system messages taught)
OR
**REVISE** to focus only on rephrasing user prompts (not system messages)

---

#### **NEW SKILLS NEEDED FOR GRADE 6**:

**T22.G6.05 – Use system request block to set chatbot role**
- Description: "Students use `OpenAI ChatGPT: system request` block to give the chatbot a role (e.g., 'You are a helpful math tutor'). They compare responses with and without system instructions."
- Dependency: T22.G6.01, T22.G6.02

**T22.G6.06.01 – Add a chat window widget**
- Description: "Students use `add chat window` block to create automatic chat UI instead of manual widgets."
- Dependency: T22.G6.01

**T22.G6.06.02 – Append messages to chat window**
- Description: "Students use `append to chat [CHATNAME] message [...]` to add user and bot messages to the chat window."
- Dependency: T22.G6.06.01

**T22.G6.06.03 – Update chat messages during streaming**
- Description: "Students use `update last chat message to [MESSAGE]` to show real-time streaming responses (partial text updating)."
- Dependency: T22.G6.02, T22.G6.06.02

---

### Grade 7 Skills

#### T22.G7.01 – Author a persona using system messages and few-shot turns
**Status**: ⚠ MAJOR REVISION NEEDED
**Issues**:
1. Too broad (system messages + few-shot examples + embedding)
2. Should be taught AFTER T22.G6.05 (intro to system messages)
3. Few-shot is advanced concept

**Recommendation**:
**SPLIT INTO 3 SUB-SKILLS**:
- **T22.G7.01.01**: Use system request to set personality (simple)
- **T22.G7.01.02**: Write few-shot examples to model tone
- **T22.G7.01.03**: Combine system + few-shot for consistent persona

---

#### T22.G7.02 – Manage chat history and reset logic
**Status**: ⚠ NEEDS REVISION
**Issues**:
1. Description says "switch session mode" (misleading)
2. Doesn't clarify session is a parameter, not a toggle
3. "Summary label" feature unclear

**Recommendation**:
- Clarify: "Use `session [new chat v]` to reset, `session [continue v]` to maintain context"
- Add: "Create 'New Chat' button that triggers new session"
- Explain: "Context window = all previous messages in continue mode"

---

#### T22.G7.03 – Capture slot values through UI widgets and inject them into prompts
**Status**: ⚠ NEEDS REVISION
**Issues**:
1. Missing prerequisite: slot-filling concept
2. Widget dependencies not listed
3. "Inject them into prompts" is vague

**Recommendation**:
- Add dependency: T16.G6.01 (widgets)
- Add new prerequisite skill about structured data collection
- Clarify: "Concatenate slot values into prompt string before API call"

---

#### T22.G7.04 – Add moderation guardrails and escalation paths
**Status**: ⚠ MAJOR REVISION NEEDED
**Issues**:
1. Too broad (6+ concepts)
2. First time seeing moderation (no prerequisite)
3. Incident logging and escalation are separate advanced topics

**Recommendation**:
**SPLIT INTO 3 SUB-SKILLS**:
- **T22.G7.04.01**: Use moderation block on user input
- **T22.G7.04.02**: Handle moderation failures with fallback messages
- **T22.G7.04.03**: Log incidents and create escalation UI

**ALSO ADD MISSING BLOCK COVERAGE**:
- **T22.G7.04.04**: Moderate image content (URL and costume blocks)

---

#### T22.G7.05 – User-test the chatbot for inclusivity and clarity
**Status**: ✓ GOOD (Concept skill)
**Issues**: None major
**Recommendation**: Keep as-is (this is concept/evaluation, not coding)

---

#### **NEW SKILLS NEEDED FOR GRADE 7**:

**T22.G7.06 – Attach files and images to chat**
- Description: "Students use `attach costume [NAME] to chat`, `attach files to chat`, and `attach file from Google Drive [URL]` blocks to add images and documents to ChatGPT requests."
- Dependency: T22.G6.05, T22.G7.01

**T22.G7.07 – Moderate image content**
- Description: "Students use `get moderation result for image at URL` and `get moderation result for costume named [NAME]` to check images before sending to API or displaying to users."
- Dependency: T22.G7.04.01

**T22.G7.08 – Compare different LLM providers**
- Description: "Students use `LLM model [PROVIDER] request` block to test small vs large models and compare cost, speed, and quality."
- Dependency: T22.G6.02, T22.G7.01

**T22.G7.09 – Cancel long-running ChatGPT requests**
- Description: "Students use `OpenAI ChatGPT: cancel request` block to stop requests that are taking too long."
- Dependency: T22.G6.02

---

### Grade 8 Skills

#### T22.G8.01 – Add retrieval-augmented generation (RAG) to a chatbot
**Status**: ⚠ MAJOR REVISION NEEDED
**Issues**:
1. Too broad (7+ concepts)
2. No table dependency listed
3. "Pinecone" mention unnecessary
4. Semantic embeddings not explained

**Recommendation**:
**SPLIT INTO 4 SUB-SKILLS**:
- **T22.G8.01.01**: Create semantic database from table
- **T22.G8.01.02**: Search semantic database with query
- **T22.G8.01.03**: Integrate search results into ChatGPT prompt
- **T22.G8.01.04**: Display citations and handle no-match cases

**ALSO ADD PREREQUISITE**:
- Dependency: T29.G7.01 (table creation/manipulation)

---

#### T22.G8.02 – Coordinate multi-agent conversations and summaries
**Status**: ⚠ MAJOR REVISION NEEDED
**Issues**:
1. Too broad (6+ concepts)
2. Broadcast coordination is advanced
3. Session ID management unclear
4. Moderator role is separate skill

**Recommendation**:
**SPLIT INTO 3 SUB-SKILLS**:
- **T22.G8.02.01**: Switch between chatbot threads (`select chatbot` block)
- **T22.G8.02.02**: Coordinate turn-taking between two bots
- **T22.G8.02.03**: Create moderator bot that summarizes debate

---

#### T22.G8.03 – Parse structured chatbot outputs to trigger tools
**Status**: ⚠ NEEDS REVISION
**Issues**:
1. JSON parsing is very advanced for Grade 8
2. No prerequisite about JSON format
3. Tool routing is separate concept
4. Error handling for malformed JSON is complex

**Recommendation**:
- Either break into sub-skills (parse, validate, route)
- OR add prerequisite skill about JSON structure
- Consider moving to capstone/advanced track

---

#### T22.G8.04 – Publish a chatbot operations manual
**Status**: ✓ GOOD (Concept/Documentation skill)
**Issues**: None major
**Recommendation**: Keep as-is (synthesis/reflection activity)

---

#### **NEW SKILLS NEEDED FOR GRADE 8**:

**T22.G8.05 – Add web search to chatbot knowledge**
- Description: "Students use `web search [QUERY] store top (K) in table [TABLE v]` block to retrieve current information from the web and incorporate it into chatbot responses."
- Dependency: T22.G8.01.03, T29.G7.01

---

## PART 6: COMPLETE BLOCK COVERAGE MATRIX

### ChatGPT/LLM Blocks (9 total)

| Block ID | Block Name | Current Coverage | Recommended Skill |
|----------|-----------|------------------|-------------------|
| openaichatcompletion | ChatGPT request | ✓ G6.01, G6.02 | Keep |
| openaichatcompletionsystem | System request | ✓ G7.01 | Move to G6.05 (earlier) |
| openai_chatgpt_cancel | Cancel request | ✗ MISSING | NEW: G7.09 |
| llmchatcompletion | Generic LLM | ✗ MISSING | NEW: G7.08 |
| llmsysteminstruction | LLM system instruction | ✗ MISSING | NEW: G7.08 |
| switchchatbot | Select chatbot | ✓ G8.02 | Keep |
| attachimagetochat | Attach costume | ✗ MISSING | NEW: G7.06 |
| attachfilestochat | Attach files | ✗ MISSING | NEW: G7.06 |
| attachgooglefiletochat | Attach Google Drive file | ✗ MISSING | NEW: G7.06 |

---

### Chat Window Blocks (NOT IN ORIGINAL LIST - CRITICAL MISSING)

| Block ID | Block Name | Current Coverage | Recommended Skill |
|----------|-----------|------------------|-------------------|
| (unknown) | add chat window | ✗ MISSING | NEW: G6.06.01 |
| (unknown) | append to chat [CHATNAME] message [...] | ✗ MISSING | NEW: G6.06.02 |
| (unknown) | update last chat message to [MESSAGE] | ✗ MISSING | NEW: G6.06.03 |

**NOTE**: These blocks appear in T22_VERIFICATION_REPORT.md but are NOT in AI_BLOCKS_COMPLETE_REFERENCE.md!
Need to verify these blocks exist and add them to complete reference.

---

### Content Moderation Blocks (3 total)

| Block ID | Block Name | Current Coverage | Recommended Skill |
|----------|-----------|------------------|-------------------|
| getmoderationresult | Text moderation | ✓ G7.04 | Keep |
| getmoderationresult2 | Image URL moderation | ✗ MISSING | NEW: G7.07 |
| getmoderationresult3 | Costume moderation | ✗ MISSING | NEW: G7.07 |

---

### Semantic Search Blocks (3 total)

| Block ID | Block Name | Current Coverage | Recommended Skill |
|----------|-----------|------------------|-------------------|
| addtabletopinecone | Create semantic DB | ✓ G8.01 | Keep |
| searchfrompinecone | Search with filter | ✓ G8.01 | Keep |
| searchfrompinecone2 | Search with WHERE | ✓ G8.01 | Keep |

---

### Web Search Blocks (1 total)

| Block ID | Block Name | Current Coverage | Recommended Skill |
|----------|-----------|------------------|-------------------|
| googlesearch | Web search | ✗ MISSING | NEW: G8.05 |

---

## PART 7: SUMMARY OF RECOMMENDED CHANGES

### A. Skills to SPLIT into Sub-Skills (6 skills)

1. **T22.G6.03** → T22.G6.03.01 - .05 (Chat UI components)
2. **T22.G7.01** → T22.G7.01.01 - .03 (System messages + few-shot)
3. **T22.G7.04** → T22.G7.04.01 - .04 (Moderation + images)
4. **T22.G8.01** → T22.G8.01.01 - .04 (RAG pipeline)
5. **T22.G8.02** → T22.G8.02.01 - .03 (Multi-agent coordination)
6. **T22.G8.03** → Consider splitting into parse + validate + route

---

### B. NEW Skills to ADD (10 new skills)

**Grade 6 Additions**:
- T22.G6.05: Use system request block
- T22.G6.06.01: Add chat window
- T22.G6.06.02: Append to chat window
- T22.G6.06.03: Update streaming messages

**Grade 7 Additions**:
- T22.G7.06: Attach files and images
- T22.G7.07: Moderate image content
- T22.G7.08: Compare LLM providers
- T22.G7.09: Cancel ChatGPT requests

**Grade 8 Additions**:
- T22.G8.05: Add web search to chatbot

---

### C. Skills to REVISE (6 skills)

1. **T22.G6.01**: Add specific block names and list structure details
2. **T22.G6.02**: Remove "max tokens", add streaming details
3. **T22.G6.04**: Move to G7 OR revise to exclude system messages
4. **T22.G7.02**: Clarify session parameter vs mode
5. **T22.G7.03**: Add widget dependencies and clarify "injection"
6. **T22.G8.03**: Add JSON prerequisite or split further

---

### D. Skills to KEEP AS-IS (5 skills)

1. T22.G3.01 ✓
2. T22.G4.01 ✓
3. T22.G5.01 ✓
4. T22.G7.05 ✓
5. T22.G8.04 ✓

---

### E. Missing Dependencies to ADD

**Cross-Topic Dependencies**:
- T22.G6.03 → Add T16.G5.01 (widgets)
- T22.G7.03 → Add T16.G6.01 (widget events)
- T22.G8.01 → Add T29.G7.01 (tables)
- T22.G8.05 → Add T29.G7.01 (tables)

**Within-T22 Dependencies**:
- T22.G6.04 → Change to depend on T22.G6.05 (system messages)
- T22.G7.04 → Add prerequisite skill for moderation concept

---

## PART 8: PRIORITY ACTION ITEMS

### CRITICAL (Must Fix Before Implementation)

1. **Add Chat Window Block Skills** (G6.06.01 - .03)
   - These are purpose-built CreatiCode features not taught at all!

2. **Split T22.G6.03 into Sub-Skills**
   - Currently too broad to implement as single challenge

3. **Add System Request Block Introduction** (G6.05)
   - Required before G7.01 and G6.04

4. **Fix T22.G6.02 "Max Tokens" Reference**
   - Parameter is obsolete per block documentation

5. **Add Missing Block Coverage**:
   - File attachments (G7.06)
   - Image moderation (G7.07)
   - Web search (G8.05)

---

### HIGH PRIORITY (Significantly Improves Quality)

6. **Split T22.G7.01 into Sub-Skills**
   - System messages + few-shot is too much at once

7. **Split T22.G7.04 into Sub-Skills**
   - Moderation + logging + escalation is too broad

8. **Split T22.G8.01 into Sub-Skills**
   - RAG has too many new concepts

9. **Move or Revise T22.G6.04**
   - Too advanced for Grade 6 (needs system messages)

10. **Add Widget Dependencies to T22.G6.03 and T22.G7.03**
    - Missing cross-topic prerequisites

---

### MEDIUM PRIORITY (Improves Clarity)

11. **Clarify Session Parameter Usage** (G7.02)
    - Current description is misleading

12. **Add Table Dependencies** (G8.01, G8.05)
    - Missing cross-topic prerequisites

13. **Add LLM Provider Comparison Skill** (G7.08)
    - Good feature coverage, not urgent

14. **Add Cancel Request Skill** (G7.09)
    - Minor block, but completeness matters

---

### LOW PRIORITY (Nice to Have)

15. **Split T22.G8.02 into Sub-Skills**
    - Multi-agent is already capstone-level

16. **Revise T22.G8.03 with JSON Prerequisites**
    - Already flagged as advanced

17. **Add More Context Examples to Descriptions**
    - Existing descriptions work, but more detail helps

---

## PART 9: ESTIMATED NEW SKILL COUNT

**Current Skills**: 17 (G3-G8, excluding K-2)

**After Splitting**:
- T22.G6.03 → 5 sub-skills (+4)
- T22.G7.01 → 3 sub-skills (+2)
- T22.G7.04 → 4 sub-skills (+3)
- T22.G8.01 → 4 sub-skills (+3)
- T22.G8.02 → 3 sub-skills (+2)

**New Skills Added**:
- G6: +4 (system request, chat window x3)
- G7: +4 (attachments, image mod, LLM compare, cancel)
- G8: +1 (web search)

**Total New Skills**: +23 skills

**Projected Total**: 40 skills (G3-G8)

---

## PART 10: FINAL RECOMMENDATIONS

### For Immediate Implementation

**Phase 1 - Critical Fixes (Ship Blockers)**:
1. Split T22.G6.03 into 5 sub-skills
2. Add T22.G6.05 (system request intro)
3. Add T22.G6.06.01-.03 (chat window blocks)
4. Fix T22.G6.02 (remove max tokens reference)
5. Add T22.G7.06 (file attachments)

**Phase 2 - High Priority (Quality)**:
6. Split T22.G7.01 into 3 sub-skills
7. Split T22.G7.04 into 4 sub-skills
8. Split T22.G8.01 into 4 sub-skills
9. Add T22.G7.07 (image moderation)
10. Add T22.G8.05 (web search)

**Phase 3 - Polish (Completeness)**:
11. Split T22.G8.02 into 3 sub-skills
12. Add T22.G7.08 (LLM providers)
13. Add T22.G7.09 (cancel requests)
14. Revise remaining unclear descriptions

---

### For Future Consideration

**Advanced Topics (Grade 8+)**:
- Streaming protocols (WebSocket vs polling)
- Token counting and optimization
- Fine-tuning vs prompting trade-offs
- Chatbot evaluation metrics (perplexity, BLEU, etc.)

**Ethical AI Skills**:
- Bias detection in LLM outputs
- Environmental impact of AI queries
- Copyright and attribution for AI-generated content
- When NOT to use AI (human-critical decisions)

---

## CONCLUSION

T22 (Chatbots & Prompting) has a solid conceptual foundation but needs significant work to be implementation-ready:

**Strengths**:
- Good K-8 progression from concepts to implementation
- Covers core ChatGPT functionality
- Includes important ethics/safety topics

**Major Gaps**:
- **12 of 17 skills (71%)** need revision or splitting
- **10 critical blocks** never taught (chat windows, attachments, web search)
- **6 skills too broad** to implement as single challenges
- **Missing scaffolding** between grades (sudden jumps)

**Bottom Line**:
T22 requires **Phase 1 major revisions** before implementation. Current skills provide good outline but lack the granularity and completeness needed for actual teaching.

**Recommended Action**:
1. Implement Phase 1 critical fixes immediately
2. Review split skills with curriculum team
3. Add missing block coverage (chat windows, attachments)
4. Test G6 skills with students before proceeding to G7-G8

---

**Report Completed**: 2025-11-23
**Total Analysis Time**: Comprehensive review of 17 skills against 43 AI blocks
**Status**: MAJOR REVISIONS REQUIRED - SEE PHASE 1 ACTION ITEMS
