# T22 (Chatbots & Prompting) Comprehensive Analysis Report

## 1. COMPLETE SKILL INVENTORY (K-8)

### Kindergarten (2 skills)
- **T22.GK.01**: Recognize a talking helper vs a silent toy
- **T22.GK.02**: Practice asking a picture helper a friendly question

### Grade 1 (2 skills)
- **T22.G1.01**: Sort good questions from confusing questions
- **T22.G1.02**: Identify what a chatbot might not know

### Grade 2 (2 skills)
- **T22.G2.01**: Role-play asking a helper for information
- **T22.G2.02**: Decide which questions are okay to ask a helper

### Grade 3 (1 skill)
- **T22.G3.01**: Identify chatbot behavior from fixed button replies

### Grade 4 (1 skill)
- **T22.G4.01**: Write clear, polite questions for a helper bot

### Grade 5 (5 skills)
- **T22.G5.01**: Flag risky vs safe chatbot prompts
- **T22.G5.02**: Observe chatbot strengths and weaknesses through testing
- **T22.G5.03**: Experiment with prompt phrasing to improve responses
- **T22.G5.04**: Use a chatbot block to get AI responses
- **T22.G5.05**: Identify ChatGPT block parameters in starter code

### Grade 6 (10 skills)
- **T22.G6.01**: Trace how a chatbot script processes each turn
- **T22.G6.02**: Adjust temperature for response creativity
- **T22.G6.03**: Handle streaming mode and long requests
- **T22.G6.04.01**: Add input widgets for user messages
- **T22.G6.04.02**: Build a conversation log with dynamic updates
- **T22.G6.05**: Implement session management for multi-turn conversations
- **T22.G6.06.01**: Create and configure a pre-built chat window
- **T22.G6.06.02**: Manage chat messages with append and update blocks
- **T22.G6.06.03**: Display streaming responses in real-time
- **T22.G6.07**: Debug off-topic responses by rewriting prompts
- **T22.G6.08**: Use multiple chatbot sessions with the select chatbot block

### Grade 7 (9 skills)
- **T22.G7.01**: Use system messages to set bot behavior
- **T22.G7.02**: Author a persona using system messages and few-shot turns
- **T22.G7.03**: Manage chat history and reset logic
- **T22.G7.04**: Capture data from UI widgets and inject into prompts
- **T22.G7.05**: Add moderation guardrails and escalation paths
- **T22.G7.06**: Attach images and files to chatbot conversations
- **T22.G7.07**: Use image moderation to filter visual content
- **T22.G7.08**: Compare different LLM models using the generic LLM block
- **T22.G7.09**: User-test the chatbot for inclusivity and clarity

### Grade 8 (5 skills)
- **T22.G8.01**: Add retrieval-augmented generation (RAG) to a chatbot
- **T22.G8.02**: Coordinate multi-agent conversations and summaries
- **T22.G8.03**: Parse structured chatbot outputs to trigger tools
- **T22.G8.04**: Create an automated chatbot testing and reporting system
- **T22.G8.05**: Integrate web search into chatbot responses

**TOTAL: 37 skills**

---

## 2. SKILLS THAT ARE TOO BROAD AND NEED BREAKING DOWN

### CRITICAL - Severely Overloaded Skills

#### **T22.G6.01: Trace how a chatbot script processes each turn**
**Problem**: This skill covers ALL ChatGPT parameters (mode, length, temperature, session) plus conversation flow, user input capture, and history management - at least 6 different concepts.

**Recommendation**: Break into multiple skills:
1. Trace basic chatbot request-response flow (user input → API call → display response)
2. Identify conversation log/history management in code
3. Identify session parameter usage in starter code
4. (Parameters are already covered in G6.02-G6.03)

**Justification**: Students can't master 6+ concepts in one skill. This is particularly problematic as G6.02, G6.03, and G6.05 depend on this and expect students to already understand all parameters.

---

#### **T22.G6.04.01: Add input widgets for user messages**
**Problem**: Combines UI widget creation, event handling, and chatbot integration.

**Current State**: Reasonable scope - adds textbox + button + connection to chatbot. No breakdown needed.

---

#### **T22.G6.06.01: Create and configure a pre-built chat window**
**Problem**: Single block with "customizable size, colors, input rows, and visual styling" - potentially 8+ parameters to understand.

**Recommendation**: Consider splitting:
1. Create basic chat window with default settings
2. Customize chat window appearance and layout

**Justification**: Students need to learn the block mechanics before exploring all customization options.

---

#### **T22.G7.02: Author a persona using system messages and few-shot turns**
**Problem**: Covers character design (creative writing), system message authoring, AND few-shot prompting (technical concept) - these are distinct skillsets.

**Recommendation**: Break into:
1. Design a chatbot persona with consistent personality traits
2. Implement few-shot examples to reinforce persona behavior

**Justification**: Creative character design vs. technical few-shot implementation are fundamentally different cognitive tasks.

---

#### **T22.G8.01: Add retrieval-augmented generation (RAG) to a chatbot**
**Problem**: Covers data import, semantic indexing, search queries, result integration, and prompt engineering - this is 5+ steps of a complex workflow.

**Recommendation**: Break into sequence:
1. Create semantic database from structured knowledge
2. Search semantic database to retrieve relevant context
3. Integrate retrieved context into chatbot prompts (RAG workflow)

**Justification**: RAG is a complex multi-step workflow. Students need to master each component before integration.

---

#### **T22.G8.03: Parse structured chatbot outputs to trigger tools**
**Problem**: Combines JSON format specification in prompts, response parsing, conditional routing, AND multiple tool integrations.

**Recommendation**: Break into:
1. Request structured JSON output from chatbot
2. Parse chatbot JSON responses and route to tools
3. Add user confirmations for chatbot-triggered actions

**Justification**: Prompt engineering for JSON, parsing, and routing are separate competencies.

---

### MODERATE - Multiple Concepts in One Skill

#### **T22.G6.03: Handle streaming mode and long requests**
**Problem**: Combines mode parameter (streaming vs waiting) AND cancel functionality - two separate concerns.

**Recommendation**: Consider splitting:
1. Adjust mode parameter for streaming vs waiting responses
2. Implement cancel button for long-running requests

**Justification**: Understanding async behavior vs. implementing cancellation are different skills.

---

#### **T22.G7.03: Manage chat history and reset logic**
**Problem**: Covers continue vs new session, UI buttons for both, AND status displays.

**Current State**: Reasonable for Grade 7 - building on G6.05 foundation. No split recommended.

---

#### **T22.G8.02: Coordinate multi-agent conversations and summaries**
**Problem**: Multiple chatbot sessions, turn alternation, time limits, AND summarization.

**Current State**: Acceptable capstone complexity for Grade 8. No split recommended.

---

## 3. DUPLICATES AND OVERLAPS WITHIN T22

### Significant Overlaps

#### **Session Management Overlap**
- **T22.G6.05**: Implement session management for multi-turn conversations
- **T22.G7.03**: Manage chat history and reset logic

**Analysis**:
- G6.05: Basic session parameter usage, comparing single vs multi-turn, "New Chat" button
- G7.03: Advanced with multiple buttons ("Ask follow-up", "Start new topic") and status displays

**Verdict**: NOT duplicate - clear progression from basic (G6) to advanced (G7). G7 builds substantially on G6.

---

#### **System Message Skills**
- **T22.G7.01**: Use system messages to set bot behavior (basic)
- **T22.G7.02**: Author a persona using system messages and few-shot turns (advanced)

**Analysis**: G7.01 is foundational (simple system messages), G7.02 builds on it (complex personas + few-shot).

**Verdict**: NOT duplicate - proper scaffolding. However, G7.02 is overloaded (see Section 2).

---

#### **Chat Window UI Paths**
- **T22.G6.04.02**: Build a conversation log with dynamic updates (custom UI)
- **T22.G6.06.01-03**: Create/manage pre-built chat window (templated UI)

**Analysis**: These are ALTERNATIVE approaches, not duplicates. Students choose one path:
- Path A: Build custom UI (G6.04.02)
- Path B: Use pre-built chat window (G6.06.01-03)

**Verdict**: NOT duplicate - intentional branching. However, dependency structure is confusing (see Section 5).

---

### No True Duplicates Found
All apparent overlaps represent intentional progression or alternative implementation paths.

---

## 4. LOGICAL PROGRESSION ANALYSIS (K-8)

### K-2: Unplugged Foundation (EXCELLENT)
**Skills**: GK.01-02, G1.01-02, G2.01-02 (6 total)

**Strengths**:
- Fully unplugged/picture-based (age-appropriate)
- Clear progression: recognition → questioning → privacy awareness
- Strong ethical foundation (privacy, kindness, clarity)

**Issues**: None - this sequence is exemplary.

---

### Grade 3: Conceptual Bridge (NEEDS ATTENTION)

**T22.G3.01**: Identify chatbot behavior from fixed button replies

**Issues**:
1. **Single skill for entire grade** - inadequate coverage
2. **Missing scaffolding**: No bridge between unplugged questioning (G2) and block-based implementation (G5)
3. **Conceptual gap**: Understanding AI generation vs. fixed responses is important but insufficient preparation for G4-5

**Recommendations**:
Add Grade 3 skills:
- Recognize when computers might make mistakes vs. follow rules
- Practice improving unclear questions through iteration (unplugged)
- Discuss examples of helpful vs unhelpful bot responses

---

### Grade 4: Transition to Practice (WEAK)

**T22.G4.01**: Write clear, polite questions for a helper bot

**Issues**:
1. **Single skill for entire grade** - insufficient
2. **Still conceptual** - no hands-on experience yet
3. **Late introduction**: Students don't touch actual chatbot blocks until G5.04

**Recommendations**:
Add Grade 4 skills:
- Read simple chatbot code and identify what it does
- Test a pre-built chatbot with different question types
- Observe how the same question phrased differently produces different results

---

### Grade 5: First Implementation (REASONABLE)

**Skills**: G5.01-05 (5 skills)

**Strengths**:
- Good mix: safety (G5.01), testing (G5.02-03), implementation (G5.04-05)
- G5.04 introduces actual block usage
- G5.05 builds reading skills before modification

**Issues**:
- **G5.02 says "without modifying code"** but there's no earlier skill where they USE a chatbot project
- **G5.03 has students "try variations"** but still not modify code
- **G5.04 is late** (skill 4 of 5) for first block usage

**Recommendations**:
Resequence:
1. Use a pre-built chatbot (testing)
2. Use basic chatbot block (G5.04 moved earlier)
3. Experiment with prompt variations (G5.03)
4. Identify parameters (G5.05)
5. Safety awareness (G5.01)

---

### Grade 6: Major Implementation (OVERLOADED)

**Skills**: G6.01-08 (11 skills)

**Issues**:
1. **11 skills is too many** - more than double any other grade
2. **G6.01 is severely overloaded** (see Section 2)
3. **Two UI paths (custom vs pre-built) create confusion**
4. **Many skills depend on overloaded G6.01**

**Strengths**:
- Good coverage of parameters (temperature, mode, session)
- Introduces important concepts (streaming, multi-session)

**Recommendations**:
1. Fix G6.01 overloading (break into 2-3 skills)
2. Clarify that G6.04.02 and G6.06.01-03 are alternatives
3. Consider moving some skills to G7 (e.g., G6.08 multi-session)

---

### Grade 7: Advanced Techniques (STRONG)

**Skills**: G7.01-09 (9 skills)

**Strengths**:
- System messages (G7.01-02) are well-scaffolded
- Multimodal (G7.06-07) builds on foundation
- User testing (G7.09) brings human-centered design
- LLM comparison (G7.08) shows AI isn't monolithic

**Issues**:
- G7.02 overloaded (see Section 2)
- G7.05 moderation has cross-topic dependency on T21.G6.06

**Recommendations**:
- Split G7.02 into persona design + few-shot implementation
- Ensure T21 moderation skills are properly sequenced

---

### Grade 8: Capstone Integration (EXCELLENT CONCEPTS, EXECUTION ISSUES)

**Skills**: G8.01-05 (5 skills)

**Strengths**:
- Advanced topics (RAG, multi-agent, structured outputs, testing, web search)
- Appropriate complexity for Grade 8
- Focus on integration and systems thinking

**Issues**:
- **G8.01 (RAG) is severely overloaded** (see Section 2)
- **G8.03 (structured outputs) is overloaded** (see Section 2)
- **G8.05 (web search)** has only 1 dependency - seems isolated

**Recommendations**:
- Break G8.01 into 3 skills (semantic DB creation, search, RAG integration)
- Break G8.03 into 2-3 skills (JSON prompting, parsing/routing, confirmations)
- Add earlier scaffolding for web search concept

---

### GRADE DISTRIBUTION ANALYSIS

| Grade | Skills | Status |
|-------|--------|--------|
| K     | 2      | Good   |
| 1     | 2      | Good   |
| 2     | 2      | Good   |
| 3     | 1      | **TOO FEW** |
| 4     | 1      | **TOO FEW** |
| 5     | 5      | Good   |
| 6     | 11     | **TOO MANY** |
| 7     | 9      | Good   |
| 8     | 5      | Good   |

**Recommendation**: Rebalance G3-G6 by adding to G3-4 and splitting overloaded G6 skills.

---

## 5. INTRA-TOPIC DEPENDENCY ISSUES

### Dependencies Beyond X-2 Range

#### **T22.G6.04.01** (Grade 6)
Depends on:
- **T16.G3.01**: Add a button widget (Grade 3) - **3 grades back, VIOLATION**
- **T16.G3.05**: Add a textbox widget (Grade 3) - **3 grades back, VIOLATION**
- T22.G5.04: Use a chatbot block (Grade 5) - OK

**Issue**: Assumes UI widget skills from 3 grades prior. If student learned widgets in G3, they may have forgotten by G6.

**Recommendation**: Add refresher or move to G5, OR accept that foundational UI skills persist.

---

#### **T22.G6.04.02** (Grade 6)
Depends on:
- **T16.G3.03**: Add a label widget (Grade 3) - **3 grades back, VIOLATION**
- Other G6 skills - OK

**Issue**: Same as above - 3-grade dependency gap.

---

#### **T22.G6.06.02** (Grade 6)
Depends on pre-built chat window but also:
- T22.G6.02, T22.G6.03 (same grade) - OK

**Issue**: No X-2 violation, but unclear if students can skip G6.04.01-02 and use G6.06.01-03 instead.

---

#### **T22.G7.03** (Grade 7)
Depends on:
- **T06.G5.01**: Coordinate scripts with broadcasts (Grade 5) - **2 grades back, BORDERLINE**
- T08.G5.01, T09.G5.04 (Grade 5) - 2 grades back, borderline
- T22.G6.04.02, G6.07, G6.08 (Grade 6) - OK

**Issue**: Multiple 2-grade-back dependencies. Not violation but heavy reliance on G5 skills.

---

#### **T22.G8.01** (Grade 8)
Depends on:
- **T06.G6.01**: Trace event execution (Grade 6) - **2 grades back, BORDERLINE**
- **T09.G6.01**: Model quantities with variables (Grade 6) - **2 grades back, BORDERLINE**
- T22.G7.02, G7.03, G7.05 (Grade 7) - OK

**Issue**: Multiple 2-grade-back dependencies from other topics.

---

### Skills Depending on Later Skills (CIRCULAR DEPENDENCIES)

**None found** - dependency chains within T22 are properly ordered.

---

### Alternative Path Confusion

#### **Chat UI Implementation**
Students can build conversation displays using:
- **Path A**: Custom widgets (G6.04.01 → G6.04.02)
- **Path B**: Pre-built chat window (G6.06.01 → G6.06.02 → G6.06.03)

**Problem**: Dependency graph shows:
- G6.06.02 depends on G6.02, G6.03 (OK)
- G6.06.03 depends on G6.06.02 (OK)
- G6.04.02 depends on T16.G3.03 + G6.02 + G6.03 (OK)
- **BUT**: Later skills (G7.03, G7.04, G7.05) depend on G6.04.02 (custom path only!)

**Issue**: If students choose pre-built path (G6.06.x), they can't access G7+ skills that depend on G6.04.02.

**Recommendation**:
- Make G7+ skills depend on "G6.04.02 OR G6.06.03"
- OR clarify that all students must complete both paths
- OR merge paths into single recommended approach

---

## 6. GRADE-APPROPRIATENESS ISSUES

### K-2 Compliance: EXCELLENT

All K-2 skills are:
- Unplugged (no screen time required)
- Picture-based or role-play
- Conceptually appropriate (recognition, kindness, clarity, privacy)

**No issues found.**

---

### Grade 3+ Block-Based Requirement: VIOLATIONS

#### **T22.G3.01** (Grade 3)
"Students read short app stories (one with fixed replies, one with AI that sometimes makes mistakes)"

**Status**: Unplugged analysis, not block-based. **VIOLATION**.

**Recommendation**: Add block-based component - have students examine actual code showing fixed responses vs. variable responses, or test two simple apps.

---

#### **T22.G4.01** (Grade 4)
"Students improve a vague or rude request... into a clear, focused question"

**Status**: Writing exercise, not block-based. **VIOLATION**.

**Recommendation**: Convert to block-based - students use a chatbot project to test their questions and see results, not just write on paper.

---

#### **T22.G5.01** (Grade 5)
"Students classify prompts that leak private info... and rewrite one risky prompt"

**Status**: Classification exercise, not clearly block-based. **POTENTIAL VIOLATION**.

**Recommendation**: Add block-based component - students test prompts in a chatbot and observe what information the bot requests or stores.

---

#### **T22.G5.02** (Grade 5)
"Students use a pre-built CreatiCode chatbot project without modifying code. They test different types of questions..."

**Status**: Uses blocks but doesn't modify - borderline. **ACCEPTABLE** as it's hands-on testing.

---

#### **T22.G5.03** (Grade 5)
"Students take a question the chatbot answered poorly and systematically try variations..."

**Status**: Testing/experimentation with running code. **ACCEPTABLE**.

---

### Cognitive Appropriateness

#### **T22.G6.01**: Overloaded for first comprehensive implementation
Too many concepts for initial tracing skill. See Section 2.

#### **T22.G8.01**: RAG concepts appropriate for Grade 8
Retrieval-augmented generation is advanced but suitable for Grade 8 IF properly scaffolded.

#### **T22.G8.03**: JSON parsing appropriate for Grade 8
Structured output parsing is appropriate complexity.

---

## 7. MISSING SKILLS FOR PROPER SCAFFOLDING

### Grade 3 Gaps

**Missing**:
1. **Test and compare pre-built chatbot vs menu app** (hands-on, block-based)
2. **Read simple chatbot code with adult guidance** (code reading before G6 tracing)
3. **Identify when a bot answer doesn't match the question** (response evaluation)

**Justification**: Only 1 skill in G3 is insufficient. Need block-based activities.

---

### Grade 4 Gaps

**Missing**:
1. **Use a pre-built chatbot to answer questions** (first hands-on experience)
2. **Test how different questions produce different answers** (experimentation)
3. **Read chatbot code to find where questions and answers are stored** (code literacy)

**Justification**: G4 should bridge conceptual understanding (G3) to implementation (G5).

---

### Grade 5 Gaps

**Missing**:
1. **Modify a chatbot's starter prompt or system message** (first code modification)
2. **Change max length parameter and observe results** (parameter experimentation)

**Justification**: Students jump from reading code (G5.05) to full implementation (G6) without gradual modification practice.

---

### Grade 6 Gaps

**Missing** (after fixing overloaded skills):
1. **Trace basic request-response flow** (extracted from G6.01)
2. **Identify conversation log management in code** (extracted from G6.01)
3. **Choose between custom and pre-built chat UI** (decision-making skill)

**Justification**: Breaking down G6.01 creates these needed skills.

---

### Grade 7 Gaps

**Missing**:
1. **Design persona character profile** (extracted from G7.02)
2. **Implement few-shot examples** (extracted from G7.02)
3. **Test prompts with different LLM providers** (preparation for G7.08)

**Justification**: G7.02 overloading hides these skills.

---

### Grade 8 Gaps

**Missing**:
1. **Create semantic database from table** (extracted from G8.01)
2. **Search semantic database for context** (extracted from G8.01)
3. **Integrate RAG context into prompts** (extracted from G8.01)
4. **Write prompts that request JSON output** (extracted from G8.03)
5. **Parse JSON responses from chatbot** (extracted from G8.03)
6. **Implement user confirmations for bot actions** (extracted from G8.03)

**Justification**: Breaking down overloaded capstone skills.

---

## 8. VERIFICATION AGAINST CREATICODE BLOCKS

### Core ChatGPT Blocks (FULLY COVERED)

✅ **OpenAI ChatGPT: request [PROMPT] result [VARIABLE] mode [MODE] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE]**
- Introduced: T22.G5.04 (basic usage)
- Parameters: T22.G5.05 (identify), G6.02 (temperature), G6.03 (mode/length), G6.05 (session)

✅ **OpenAI ChatGPT: system request [PROMPT] session [SESSION] result [VARIABLE] temperature [T]**
- Covered: T22.G7.01 (use system messages)

✅ **OpenAI ChatGPT: cancel request**
- Covered: T22.G6.03 (cancel button implementation)

---

### Multi-Session Blocks (FULLY COVERED)

✅ **select chatbot [1/2/3/4]**
- Covered: T22.G6.08 (multiple sessions), G8.02 (multi-agent conversations)

---

### LLM Blocks (FULLY COVERED)

✅ **LLM model [PROVIDER] request [PROMPT] result [VARIABLE] mode [MODE] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE]**
- Covered: T22.G7.08 (compare LLM models)

✅ **LLM set system instruction [INSTRUCTION] for model [PROVIDER]**
- Covered: T22.G7.08 (LLM system instructions)

---

### Chat Window Blocks (FULLY COVERED)

✅ **add chat window x (X) y (Y) width (WIDTH) height (HEIGHT) input rows (ROWS) background [BG] border [BORDERCOLOR] name [NAME]**
- Covered: T22.G6.06.01 (create and configure chat window)

✅ **append to chat [CHATNAME] message [MESSAGE] as [SENDER] icon [ICON] align [ALIGN] text size (TEXTSIZE) color [COLOR] background [BG]**
- Covered: T22.G6.06.02 (manage chat messages)

✅ **update last chat message to [MESSAGE] for chat [CHATNAME]**
- Covered: T22.G6.06.03 (streaming responses)

---

### File Attachment Blocks (FULLY COVERED)

✅ **attach costume [NAME] to chat**
- Covered: T22.G7.06 (attach images and files)

✅ **attach files to chat**
- Covered: T22.G7.06 (attach images and files)

✅ **attach file from Google Drive [URL] to chat**
- Covered: T22.G7.06 (attach images and files)

---

### Moderation Blocks (FULLY COVERED)

✅ **get moderation result for [TEXT]**
- Covered: T22.G7.05 (moderation guardrails)

✅ **get moderation result for image at URL [INPUT]**
- Covered: T22.G7.07 (image moderation)

✅ **get moderation result for costume named [INPUT]**
- Covered: T22.G7.07 (image moderation)

---

### Semantic Database Blocks (FULLY COVERED)

✅ **create semantic database from table [TABLE]**
- Covered: T22.G8.01 (RAG implementation)

✅ **search semantic database with [QUERY] store top (K) in table [TABLE] filter by column [FIELD] of value [VALUE]**
- Covered: T22.G8.01 (RAG search)

✅ **search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE]**
- Covered: T22.G8.01 (RAG search with conditions)

---

### Web Search Blocks (FULLY COVERED)

✅ **web search [QUERY] store top (K) in table [TABLE]**
- Covered: T22.G8.05 (web search integration)

---

### Blocks NOT Covered (Appropriately)

These AI blocks are NOT chatbot/prompting related and belong in other topics:

- Speech recognition blocks → T21 (AI Media & Output)
- Text-to-speech blocks → T21 (AI Media & Output)
- Face detection → T21 (Computer Vision)
- Body part recognition → T21 (Computer Vision)
- Hand detection → T21 (Computer Vision)
- KNN classifier → T20 (Machine Learning)
- Neural network blocks → T20 (Machine Learning)
- DALL-E image generation → T21 (AI Media - Image Generation)
- Sentence analysis → T21 (NLP/Language Analysis)

---

## 9. SUMMARY OF CRITICAL ISSUES

### HIGH PRIORITY (Must Fix)

1. **G6.01 is severely overloaded** - covers 6+ concepts, blocks learning
   - **Action**: Split into 2-3 separate skills

2. **G8.01 (RAG) is overloaded** - 5 distinct steps in one skill
   - **Action**: Split into 3 skills (DB creation, search, integration)

3. **G8.03 (JSON parsing) is overloaded** - prompt engineering + parsing + routing
   - **Action**: Split into 2-3 skills

4. **G3-4 have insufficient skills** (1 each) and lack block-based activities
   - **Action**: Add 2-3 hands-on skills per grade

5. **G3.01 and G4.01 are not block-based** (violates grade 3+ requirement)
   - **Action**: Add block-based components

6. **Chat UI alternative paths create dependency confusion**
   - **Action**: Clarify that G6.04.02 and G6.06.03 are alternatives, update G7+ dependencies

---

### MEDIUM PRIORITY (Should Fix)

7. **G6 has too many skills** (11 total) - overwhelming
   - **Action**: Rebalance by moving some to G7 or combining where appropriate

8. **G7.02 is overloaded** - combines creative and technical skills
   - **Action**: Split into persona design + few-shot implementation

9. **Multiple 3-grade-back dependencies** (G6.04.01-02 → T16.G3.x)
   - **Action**: Add refreshers or accept foundational skill persistence

10. **G5 sequencing could be improved** - block usage comes late
    - **Action**: Move G5.04 earlier, resequence testing before implementation

---

### LOW PRIORITY (Consider)

11. **G6.03 combines mode + cancel** - two separate concerns
    - **Action**: Consider splitting if time allows

12. **G6.06.01 covers many parameters** - potentially overwhelming
    - **Action**: Consider splitting into basic + advanced customization

13. **Web search (G8.05) seems isolated** - only 1 T22 dependency
    - **Action**: Add scaffolding or move to different topic

---

## 10. POSITIVE HIGHLIGHTS

### Strengths of T22 Curriculum

1. **Excellent K-2 foundation** - developmentally appropriate, unplugged, ethical focus
2. **Comprehensive block coverage** - all ChatGPT/LLM blocks are taught
3. **Strong ethical thread** - safety, privacy, moderation throughout
4. **Advanced G8 topics** - RAG, multi-agent, structured outputs are cutting-edge
5. **Alternative UI paths** - flexibility for different learning styles (custom vs pre-built)
6. **Multimodal integration** - text, images, files (G7.06-07)
7. **Human-centered design** - user testing (G7.09), inclusivity, accessibility
8. **No true duplicates** - apparent overlaps are intentional scaffolding
9. **System thinking** - integration skills (G8.02, G8.04) prepare for real-world AI

---

## 11. RECOMMENDED ACTIONS SUMMARY

### Immediate (Before Curriculum Launch)

1. **Split G6.01** into:
   - G6.01a: Trace basic chatbot request-response flow
   - G6.01b: Identify conversation log and history management
   - G6.01c: Understand session parameter in code

2. **Split G8.01 (RAG)** into:
   - G8.01a: Create semantic database from knowledge table
   - G8.01b: Search semantic database for relevant context
   - G8.01c: Integrate retrieved context into chatbot prompts (RAG)

3. **Split G8.03 (JSON)** into:
   - G8.03a: Request structured JSON output in prompts
   - G8.03b: Parse JSON responses and route to tools
   - G8.03c: Add user confirmations for chatbot actions

4. **Add block-based components** to G3.01 and G4.01

5. **Clarify alternative paths** in G6.04.x vs G6.06.x documentation

---

### Short-Term (Next Revision)

6. **Add Grade 3 skills** (2-3 hands-on block-based activities)
7. **Add Grade 4 skills** (2-3 bridging activities from conceptual to implementation)
8. **Split G7.02** into persona design + few-shot implementation
9. **Rebalance G6** - reduce from 11 to 8-9 skills
10. **Resequence G5** - move G5.04 earlier

---

### Long-Term (Future Iterations)

11. **Add refreshers** for long dependency chains (G6 → T16.G3)
12. **Consider splitting G6.03** (mode + cancel)
13. **Evaluate web search placement** (G8.05)
14. **Consider G6.06.01 split** (basic + advanced chat window)

---

## CONCLUSION

T22 (Chatbots & Prompting) is a **well-designed curriculum with strong ethical foundations and comprehensive coverage** of CreatiCode's ChatGPT/LLM capabilities. The K-2 unplugged sequence is exemplary, and the G8 advanced topics (RAG, multi-agent, JSON parsing) are appropriately sophisticated.

**However, the curriculum suffers from several critical structural issues**:
- Severely overloaded skills (G6.01, G8.01, G8.03) that combine 4-6 concepts
- Insufficient Grade 3-4 coverage (1 skill each, not block-based)
- Grade 6 overload (11 skills)
- Confusing alternative implementation paths (custom vs pre-built UI)

**The recommended fixes are straightforward**: splitting overloaded skills into logical components, adding hands-on activities to G3-4, and clarifying documentation. With these changes, T22 would provide an excellent scaffolded progression from unplugged fundamentals (K-2) through advanced AI integration (G8).

**Block Coverage**: All CreatiCode chatbot/prompting blocks are properly covered. No missing block instruction was found.
