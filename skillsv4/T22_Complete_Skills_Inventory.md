# T22 (Chatbots & Prompting) - Complete Skills Inventory & Analysis

## Summary Statistics
- **Total Skills**: 38
- **Grade Distribution**:
  - Kindergarten (GK): 2 skills
  - Grade 1 (G1): 2 skills
  - Grade 2 (G2): 2 skills
  - Grade 3 (G3): 1 skill
  - Grade 4 (G4): 1 skill
  - Grade 5 (G5): 4 skills
  - Grade 6 (G6): 11 skills
  - Grade 7 (G7): 9 skills
  - Grade 8 (G8): 5 skills

---

## KINDERGARTEN (GK) - 2 Skills

### T22.GK.01
- **Skill**: Recognize a talking helper vs a silent toy
- **Description**: Students look at picture pairs (a smart speaker that answers questions vs a stuffed animal, or a phone assistant vs a regular clock) and circle which one can talk back when you ask it something. This introduces the idea that some devices can have conversations.
- **Dependencies**: None

### T22.GK.02
- **Skill**: Practice asking a picture helper a friendly question
- **Description**: Students see a cartoon of a friendly robot helper. They choose from picture cards showing different ways to ask for help (pointing politely vs grabbing, saying "please" vs demanding). They learn that helpers respond better to kind requests.
- **Dependencies**:
  - T22.GK.01: Recognize a talking helper vs a silent toy

---

## GRADE 1 (G1) - 2 Skills

### T22.G1.01
- **Skill**: Sort good questions from confusing questions
- **Description**: Students sort question cards into two piles: clear questions a helper could answer ("What color is the sky?") vs confusing or incomplete questions ("Tell me the thing!"). They practice making one confusing question clearer by adding missing information.
- **Dependencies**:
  - T22.GK.02: Practice asking a picture helper a friendly question

### T22.G1.02
- **Skill**: Identify what a chatbot might not know
- **Description**: Students look at scenarios and decide if a chatbot helper could answer (facts, spelling help) or probably couldn't (what's in your backpack, how you're feeling today). This builds awareness that chatbots don't know everything about you.
- **Dependencies**:
  - T22.G1.01: Sort good questions from confusing questions

---

## GRADE 2 (G2) - 2 Skills

### T22.G2.01
- **Skill**: Role-play asking a helper for information
- **Description**: One student pretends to be a robot helper while another asks questions. They practice giving clear context ("I need help with my math homework about adding") vs vague requests. Students notice how clear questions get better "robot" answers.
- **Dependencies**:
  - T22.G1.01: Sort good questions from confusing questions
  - T22.G1.02: Identify what a chatbot might not know

### T22.G2.02
- **Skill**: Decide which questions are okay to ask a helper
- **Description**: Students sort question cards into "okay to ask" (homework help, fun facts) vs "not okay to ask" (my home address, passwords, mean things about classmates). They learn that some information should stay private even from helpful robots.
- **Dependencies**:
  - T22.G2.01: Role-play asking a helper for information

---

## GRADE 3 (G3) - 1 Skill

### T22.G3.01
- **Skill**: Identify chatbot behavior from fixed button replies
- **Description**: Students read short app stories (one with fixed replies, one with AI that sometimes makes mistakes) and sort them into "chatbot guesses answers" vs "fixed menu responses," explaining why. This introduces the concept that chatbots generate responses while menu-based apps only show pre-written options.
- **Dependencies**:
  - T08.G3.01: Use a simple if in a script
  - T22.G2.01: Role-play asking a helper for information
  - T22.G2.02: Decide which questions are okay to ask a helper

---

## GRADE 4 (G4) - 1 Skill

### T22.G4.01
- **Skill**: Write clear, polite questions for a helper bot
- **Description**: Students improve a vague or rude request ("Tell me everything now!!!") into a clear, focused question with context and tone, suitable for a helper bot. They learn that well-structured prompts get better responses.
- **Dependencies**:
  - T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  - T06.G3.09: Fix a behavior that runs at the wrong time
  - T09.G3.05: Trace code with variables to predict outcomes
  - T22.G3.01: Identify chatbot behavior from fixed button replies

---

## GRADE 5 (G5) - 4 Skills

### T22.G5.01
- **Skill**: Flag risky vs safe chatbot prompts
- **Description**: Students classify prompts that leak private info or ask for cheating vs safe learning questions, and rewrite one risky prompt to be safe. This builds awareness of responsible AI use.
- **Dependencies**:
  - T06.G3.09: Fix a behavior that runs at the wrong time
  - T09.G3.05: Trace code with variables to predict outcomes
  - T22.G3.01: Identify chatbot behavior from fixed button replies

### T22.G5.02
- **Skill**: Observe chatbot strengths and weaknesses through testing
- **Description**: Students use a pre-built CreatiCode chatbot project without modifying code. They test different types of questions (factual, creative, math, opinion) and document when the bot performs well vs. poorly. They create a simple chart showing "good at" vs "struggles with" categories based on their observations.
- **Dependencies**:
  - T22.G4.01: Write clear, polite questions for a helper bot
  - T22.G5.01: Flag risky vs safe chatbot prompts

### T22.G5.03
- **Skill**: Experiment with prompt phrasing to improve responses
- **Description**: Students take a question the chatbot answered poorly and systematically try variations: adding context ("I'm in 5th grade"), being more specific ("Explain in 2 sentences"), or providing an example format. They record which changes helped most and write a "prompting tip" based on their experiments.
- **Dependencies**:
  - T22.G4.01: Write clear, polite questions for a helper bot
  - T22.G5.02: Observe chatbot strengths and weaknesses through testing

### T22.G5.04
- **Skill**: Identify ChatGPT block parameters in starter code
- **Description**: Students examine a simple CreatiCode project using the ChatGPT block and identify what each parameter does (mode, temperature, max length, session). They don't modify the code yet, but label screenshots showing where each parameter is and predict what happens if values change. This prepares them for tracing more complex scripts in G6.
- **Dependencies**:
  - T22.G5.1.5: Use a chatbot block to get AI responses
  - T22.G5.02: Observe chatbot strengths and weaknesses through testing

### T22.G5.1.5
- **Skill**: Use a chatbot block to get AI responses
- **Description**: Students use the basic `OpenAI ChatGPT: request [PROMPT] result [VARIABLE]` block to send a simple message to ChatGPT and store the response in a variable. They build a minimal project that displays the AI's answer on the stage, learning the fundamental mechanics of making an AI request before exploring advanced features.
- **Dependencies**:
  - T09.G4.01: Build a simple string variable for name entry
  - T22.G5.01: Flag risky vs safe chatbot prompts
  - T22.G5.03: Experiment with prompt phrasing to improve responses

---

## GRADE 6 (G6) - 11 Skills

### T22.G6.01
- **Skill**: Trace how a chatbot script processes each turn
- **Description**: Students examine a pre-built CreatiCode project that uses `OpenAI ChatGPT: request [PROMPT] result [VARIABLE] mode [waiting] length [...] temperature [...] session [...]`. They identify which blocks capture user input, how the conversation log list is updated, and when the system clears history. This builds foundational reading skills before they modify anything.
- **Dependencies**:
  - T06.G4.01: Program multiple events to run independently
  - T08.G4.01: Use nested conditions or multi-branch selection
  - T09.G4.01: Build a simple string variable for name entry
  - T09.G4.04: Trace multi-step expressions with parentheses
  - T22.G5.01: Flag risky vs safe chatbot prompts
  - T22.G5.04: Identify ChatGPT block parameters in starter code

### T22.G6.02
- **Skill**: Adjust temperature for response creativity
- **Description**: Students adjust the ChatGPT block's temperature parameter (0=predictable, 1=creative) to control response variability. They experiment with different temperature values for different use cases (e.g., low temperature for factual answers, high temperature for creative stories) and observe how this affects bot behavior.
- **Dependencies**:
  - T06.G4.01: Program multiple events to run independently
  - T08.G4.01: Use nested conditions or multi-branch selection
  - T09.G4.04: Trace multi-step expressions with parentheses
  - T22.G5.01: Flag risky vs safe chatbot prompts
  - T22.G6.01: Trace how a chatbot script processes each turn

### T22.G6.03
- **Skill**: Handle streaming mode and long requests
- **Description**: Students adjust the ChatGPT block's mode (streaming vs. waiting) and max length settings to match different app goals. They learn to use `OpenAI ChatGPT: cancel request` to stop a long-running or stuck request, implementing a "Cancel" button that lets users abort slow responses.
- **Dependencies**:
  - T06.G4.01: Program multiple events to run independently
  - T08.G4.01: Use nested conditions or multi-branch selection
  - T09.G4.04: Trace multi-step expressions with parentheses
  - T22.G5.01: Flag risky vs safe chatbot prompts
  - T22.G6.01: Trace how a chatbot script processes each turn

### T22.G6.04.01
- **Skill**: Add input widgets for user messages
- **Description**: Students use text input widgets and buttons from the UI toolkit to create the input section of a chat interface. They connect a "Send" button to read the textbox value and trigger the chatbot request, learning how UI widgets collect user input for AI interactions.
- **Dependencies**:
  - T16.G3.01: Add a button widget to the stage
  - T16.G3.05: Add a textbox widget for user input
  - T22.G5.1.5: Use a chatbot block to get AI responses

### T22.G6.04.02
- **Skill**: Build a conversation log with dynamic updates
- **Description**: Students create a scrolling conversation display using label widgets or list displays. They append each user message and bot response to maintain a visible chat history, managing formatting and scroll position as new messages arrive.
- **Dependencies**:
  - T16.G3.03: Add a label widget to display text
  - T22.G6.02: Adjust temperature for response creativity
  - T22.G6.03: Handle streaming mode and long requests

### T22.G6.06.01
- **Skill**: Create and configure a pre-built chat window
- **Description**: Students use the `add chat window` block to create and configure a pre-styled chat interface with customizable size, colors, input rows, and visual styling. They explore customization options to match their app's design without building UI from scratch. This provides an alternative approach to T22.G6.04.02 for students who prefer using the pre-built chat window instead of creating their own conversation display.
- **Dependencies**:
  - T22.G6.01: Trace how a chatbot script processes each turn
  - T22.G6.02: Adjust temperature for response creativity
  - T22.G6.03: Handle streaming mode and long requests

### T22.G6.06.02
- **Skill**: Manage chat messages with append and update blocks
- **Description**: Students use `append to chat [CHATNAME] message [...] as [SENDER] icon [...] align [...]` to add messages to the chat window with proper sender identification and icons. They learn to differentiate user messages from bot responses through sender labels and alignment.
- **Dependencies**:
  - T22.G6.02: Adjust temperature for response creativity
  - T22.G6.03: Handle streaming mode and long requests
  - T22.G6.06.01: Create and configure a pre-built chat window

### T22.G6.06.03
- **Skill**: Display streaming responses in real-time
- **Description**: Students implement streaming mode responses using `update last chat message to [MESSAGE] for chat [CHATNAME]` to show text appearing word-by-word as the AI generates it. They compare the user experience of streaming vs. waiting mode and understand when each is appropriate.
- **Dependencies**:
  - T22.G6.02: Adjust temperature for response creativity
  - T22.G6.03: Handle streaming mode and long requests
  - T22.G6.06.02: Manage chat messages with append and update blocks

### T22.G6.05.5
- **Skill**: Understand chatbot session types
- **Description**: Students learn the difference between single-turn requests (independent questions) and multi-turn conversations (maintaining context across exchanges). They identify when to use the basic request block versus when to manage sessions with the session parameter, understanding how context affects chatbot responses.
- **Dependencies**:
  - T22.G6.01: Trace how a chatbot script processes each turn
  - T22.G6.02: Adjust temperature for response creativity
  - T22.G6.03: Handle streaming mode and long requests

### T22.G6.07
- **Skill**: Debug off-topic responses by rewriting prompts
- **Description**: Students investigate cases where the bot rambles, ignores instructions, or refuses to answer. They edit the system message, add clarifying phrases, or insert reminders about format, then re-run the chat to verify improvement. This introduces iterative prompting as a debugging skill.
- **Dependencies**:
  - T06.G4.08: Fix event timing issues in multi-event programs
  - T08.G4.01: Use nested conditions or multi-branch selection
  - T09.G4.04: Trace multi-step expressions with parentheses
  - T22.G4.01: Write clear, polite questions for a helper bot
  - T22.G5.01: Flag risky vs safe chatbot prompts
  - T22.G6.01: Trace how a chatbot script processes each turn

### T22.G6.08
- **Skill**: Use multiple chatbot sessions with the select chatbot block
- **Description**: Students use the `select chatbot [1/2/3/4]` block to maintain separate conversation threads. They build a project where different characters (e.g., a teacher and a student) each have their own chat history, switching between sessions to continue each conversation independently.
- **Dependencies**:
  - T22.G6.01: Trace how a chatbot script processes each turn
  - T22.G6.04.02: Build a conversation log with dynamic updates

---

## GRADE 7 (G7) - 9 Skills

### T22.G7.01
- **Skill**: Use system messages to set bot behavior
- **Description**: Students learn how to use the `OpenAI ChatGPT: system request` block to provide initial instructions that guide the chatbot's behavior. They experiment with simple system messages (e.g., "Be helpful and concise") and observe how this affects all subsequent responses.
- **Dependencies**:
  - T22.G6.02: Adjust temperature for response creativity
  - T22.G6.03: Handle streaming mode and long requests
  - T22.G6.07: Debug off-topic responses by rewriting prompts

### T22.G7.02
- **Skill**: Author a persona using system messages and few-shot turns
- **Description**: Students design a detailed character brief (e.g., "sarcastic space tour guide") and write a comprehensive system message plus 2–3 example exchanges that model the expected voice and style. They use advanced prompting techniques to ensure the bot stays in character across turns, building on their basic system message knowledge.
- **Dependencies**:
  - T22.G6.02: Adjust temperature for response creativity
  - T22.G6.03: Handle streaming mode and long requests
  - T22.G6.07: Debug off-topic responses by rewriting prompts
  - T22.G7.01: Use system messages to set bot behavior

### T22.G7.03
- **Skill**: Manage chat history and reset logic
- **Description**: Students practice when to continue a conversation versus start "new chat." They add buttons such as "Ask follow-up" (continue session) and "Start new topic" (new session), and they implement a summary label that tells the user what context is currently active.
- **Dependencies**:
  - T06.G5.01: Coordinate scripts across sprites using broadcasts
  - T08.G5.01: Use conditionals with comparison operators
  - T09.G5.04: Use variables to control animation timing
  - T22.G6.04.02: Build a conversation log with dynamic updates
  - T22.G6.07: Debug off-topic responses by rewriting prompts
  - T22.G6.08: Use multiple chatbot sessions with the select chatbot block

### T22.G7.04
- **Skill**: Capture data from UI widgets and inject into prompts
- **Description**: Students create widgets (dropdowns, sliders, toggles) that gather key facts (age range, preferred topic, mood). Before contacting ChatGPT, they assemble those data values into the prompt, ensuring the bot answers with personalized tips or stories.
- **Dependencies**:
  - T22.G6.04.02: Build a conversation log with dynamic updates
  - T22.G6.07: Debug off-topic responses by rewriting prompts
  - T22.G7.02: Author a persona using system messages and few-shot turns

### T22.G7.05
- **Skill**: Add moderation guardrails and escalation paths
- **Description**: Students integrate the `get moderation result for [TEXT]` block on both user input and bot output. If a message fails moderation, the chatbot responds with a pre-written supportive message, logs the incident, and offers to connect the user with a human helper. This meets AI4K12 priorities around responsible deployment.
- **Dependencies**:
  - T06.G5.01: Coordinate scripts across sprites using broadcasts
  - T08.G5.01: Use conditionals with comparison operators
  - T09.G5.04: Use variables to control animation timing
  - T21.G6.06: Check user input with AI content moderation
  - T22.G5.01: Flag risky vs safe chatbot prompts
  - T22.G6.04.02: Build a conversation log with dynamic updates
  - T22.G6.07: Debug off-topic responses by rewriting prompts

### T22.G7.09
- **Skill**: User-test the chatbot for inclusivity and clarity
- **Description**: Students prepare at least four tester personas (age, language level, accessibility need), run scripted conversations, and note where the bot confuses or excludes users. They adjust prompts or UI affordances (e.g., add a "simplify answer" button) and document changes.
- **Dependencies**:
  - T22.G6.04.02: Build a conversation log with dynamic updates
  - T22.G6.07: Debug off-topic responses by rewriting prompts
  - T22.G7.02: Author a persona using system messages and few-shot turns

### T22.G7.06
- **Skill**: Attach images and files to chatbot conversations
- **Description**: Students use `attach costume [NAME] to chat`, `attach files to chat`, and `attach file from Google Drive [URL] to chat` blocks to send images or documents to the chatbot for analysis. They build an app where users can upload pictures from their device or link files from Google Drive, then ask the bot questions about the content, learning multimodal AI interactions.
- **Dependencies**:
  - T22.G6.04.02: Build a conversation log with dynamic updates
  - T22.G6.07: Debug off-topic responses by rewriting prompts
  - T22.G7.02: Author a persona using system messages and few-shot turns

### T22.G7.07
- **Skill**: Use image moderation to filter visual content
- **Description**: Students use the `get moderation result for image at URL [URL]` and `get moderation result for costume named [NAME]` blocks to check images before processing or displaying them. They implement a content filter that prevents inappropriate images from being analyzed by the chatbot.
- **Dependencies**:
  - T21.G6.07: Use image moderation to check visual content
  - T22.G7.05: Add moderation guardrails and escalation paths
  - T22.G7.06: Attach images and files to chatbot conversations

### T22.G7.08
- **Skill**: Compare different LLM models using the generic LLM block
- **Description**: Students use the `LLM model [PROVIDER] request [PROMPT]` block with both "small" and "large" model options to compare response quality, speed, and cost trade-offs. They set system instructions using `LLM set system instruction [INSTRUCTION] for model [PROVIDER]` and build a comparison tool that shows how different models answer the same prompt, learning when to use smaller/faster models vs larger/more capable ones.
- **Dependencies**:
  - T22.G6.02: Adjust temperature for response creativity
  - T22.G7.01: Use system messages to set bot behavior

---

## GRADE 8 (G8) - 5 Skills

### T22.G8.01
- **Skill**: Add retrieval-augmented generation (RAG) to a chatbot
- **Description**: Students import curriculum notes into a table, build a semantic index using `create semantic database from table [TABLE]`, and before each ChatGPT call they run `search semantic database with [QUERY] store top (K) in table [TABLE]` to fetch the top facts. They prepend the retrieved snippets to the prompt so answers stay grounded in source material.
- **Dependencies**:
  - T06.G6.01: Trace event execution paths in a multi‑event program
  - T09.G6.01: Model real-world quantities using variables and formulas
  - T22.G7.02: Author a persona using system messages and few-shot turns
  - T22.G7.03: Manage chat history and reset logic
  - T22.G7.05: Add moderation guardrails and escalation paths

### T22.G8.02
- **Skill**: Coordinate multi-agent conversations and summaries
- **Description**: Students use the `select chatbot [1/2/3/4]` block to spin up two sessions (e.g., historian vs. scientist) and a third "moderator" script that alternates turns, enforces time limits, and summarizes agreements for the user. This mirrors advanced creative AI use cases.
- **Dependencies**:
  - T06.G6.01: Trace event execution paths in a multi‑event program
  - T09.G6.01: Model real-world quantities using variables and formulas
  - T22.G6.08: Use multiple chatbot sessions with the select chatbot block
  - T22.G7.02: Author a persona using system messages and few-shot turns
  - T22.G7.03: Manage chat history and reset logic
  - T22.G7.05: Add moderation guardrails and escalation paths
  - T22.G7.09: User-test the chatbot for inclusivity and clarity

### T22.G8.03
- **Skill**: Parse structured chatbot outputs to trigger tools
- **Description**: Students instruct ChatGPT to answer in a JSON-like format (e.g., `{"action":"schedule","details":"..."}`). Their script parses the response and routes to helper blocks: calculator, table lookup, or calendar writer. They add confirmations so the user sees exactly what the bot executed.
- **Dependencies**:
  - T03.G6.01: Propose modules for a medium project
  - T06.G6.01: Trace event execution paths in a multi‑event program
  - T09.G6.01: Model real-world quantities using variables and formulas
  - T22.G7.02: Author a persona using system messages and few-shot turns
  - T22.G7.05: Add moderation guardrails and escalation paths

### T22.G8.04
- **Skill**: Create an automated chatbot testing and reporting system
- **Description**: Students build a testing harness that runs their chatbot through a suite of test prompts (stored in a table), logs each response, flags moderation events, and generates a summary report showing pass/fail rates and edge cases. They add code to track response times and detect when the bot goes off-topic, creating an automated quality assurance system for their chatbot.
- **Dependencies**:
  - T06.G6.01: Trace event execution paths in a multi‑event program
  - T08.G6.01: Use conditionals to control simulation steps
  - T09.G6.01: Model real-world quantities using variables and formulas
  - T22.G7.05: Add moderation guardrails and escalation paths
  - T22.G7.09: User-test the chatbot for inclusivity and clarity

### T22.G8.05
- **Skill**: Integrate web search into chatbot responses
- **Description**: Students use the `web search [QUERY] store top (K) in table [TABLE]` block to fetch current information before generating a response. They prepend search results to the prompt so the chatbot can answer questions about recent events or live data not in its training.
- **Dependencies**:
  - T06.G6.01: Trace event execution paths in a multi‑event program
  - T09.G6.01: Model real-world quantities using variables and formulas
  - T22.G7.02: Author a persona using system messages and few-shot turns
  - T22.G7.05: Add moderation guardrails and escalation paths
  - T22.G8.01: Add retrieval-augmented generation (RAG) to a chatbot

---

## CRITICAL ISSUES & OBSERVATIONS

### 1. SKILL ID INCONSISTENCIES

**MAJOR ISSUE - Non-Standard Skill ID**:
- **T22.G5.1.5** - Should be **T22.G5.15** (uses dot notation instead of standard format)
  - Current: T22.G5.1.5 (Use a chatbot block to get AI responses)
  - Should be: T22.G5.15

**MAJOR ISSUE - Irregular Numbering Pattern**:
- **T22.G6.05.5** - Should be **T22.G6.055** or reorganized
  - Current: T22.G6.05.5 (Understand chatbot session types)
  - Should be: T22.G6.055 or renamed to follow proper sequence

### 2. DEPENDENCY ISSUES

**Circular/Forward Dependency Problem**:
- **T22.G5.04** depends on **T22.G5.1.5** (later skill)
- **T22.G5.1.5** depends on **T22.G5.01** and **T22.G5.03**
- This creates an ordering issue where G5.04 depends on G5.1.5 which should come later

**Suggested Fix**: Renumber to ensure proper sequence:
- T22.G5.01: Flag risky vs safe chatbot prompts
- T22.G5.02: Observe chatbot strengths and weaknesses through testing
- T22.G5.03: Experiment with prompt phrasing to improve responses
- T22.G5.04: Use a chatbot block to get AI responses (move from G5.1.5)
- T22.G5.05: Identify ChatGPT block parameters in starter code (move from G5.04)

### 3. GRADE PLACEMENT CONCERNS

**Grade 4 Dependency Issues**:
- **T22.G4.01** depends on **G3** skills (T06.G3.01, T06.G3.09, T09.G3.05)
- But the skill itself is fairly conceptual (rewriting prompts)
- This seems appropriate - just checking dependencies are correct

**Grade 5 Widget Dependencies**:
- **T22.G6.04.01** depends on T16.G3.01 and T16.G3.05 (Grade 3 widget skills)
- This is placed in Grade 6 but could potentially be Grade 5 based on dependencies
- **Recommend**: Consider if this should be T22.G5.XX instead of G6

### 4. LOGICAL PROGRESSION ISSUES

**Missing Foundation Skills**:
- Jump from G4 (1 skill) to G5 (4 skills) with actual coding
- G5 introduces actual ChatGPT blocks but students haven't seen basic AI blocks before
- **T22.G5.1.5** should probably come before G5.01-G5.04 in sequence

**Chat Window Alternatives**:
- **T22.G6.04.02** (Build conversation log manually)
- **T22.G6.06.01** (Use pre-built chat window)
- These are presented as alternatives but dependency chain favors G6.04.02
- Many G7 skills depend on G6.04.02, creating bias toward manual approach
- **Recommend**: Add note that G6.06.01-G6.06.03 can substitute for G6.04.02

### 5. SKILL QUALITY OBSERVATIONS

**Excellent Skills** (Clear, Well-Scoped):
- T22.GK.01 - T22.G2.02: Excellent unplugged/conceptual progression
- T22.G6.02: Adjust temperature (clear, focused)
- T22.G7.01-G7.02: System messages (good scaffolding)
- T22.G8.01: RAG implementation (advanced but clear)

**Skills Needing Clarification**:
- **T22.G5.02**: "Observe chatbot strengths and weaknesses" - needs more specific deliverable
- **T22.G6.05.5**: "Understand chatbot session types" - too conceptual, needs hands-on component
- **T22.G7.09**: "User-test for inclusivity" - very broad, could be multiple skills

**Potentially Too Complex**:
- **T22.G8.02**: Multi-agent coordination with moderator - very advanced
- **T22.G8.04**: Automated testing harness - could be 2-3 separate skills

### 6. CONTENT DUPLICATES/OVERLAPS

**Potential Overlap**:
- **T22.G4.01** (Write clear questions) vs **T22.G5.03** (Experiment with prompt phrasing)
- Both focus on improving prompts, but G5.03 adds systematic testing
- **Status**: Not a duplicate, good progression

**Potential Overlap**:
- **T22.G6.07** (Debug off-topic responses) vs **T22.G7.01** (Use system messages)
- G6.07 introduces editing prompts/system messages
- G7.01 formalizes system message usage
- **Status**: Some overlap but acceptable progression

### 7. MISSING SKILLS

**Recommended Additions**:
1. **Grade 4**: Basic AI blocks introduction (before jumping to ChatGPT in G5)
2. **Grade 5**: Error handling for failed API requests
3. **Grade 6**: Managing API costs/token limits awareness
4. **Grade 7**: Prompt chaining (using one response as input to next prompt)
5. **Grade 8**: Fine-tuning awareness (when to customize vs prompt engineering)

### 8. CROSS-TOPIC DEPENDENCIES

**Strong Dependencies on Other Topics**:
- **T06** (Events & Debugging): 13 dependencies across multiple grades
- **T08** (Conditionals): 8 dependencies
- **T09** (Variables): 11 dependencies
- **T16** (Widgets): 3 dependencies for UI
- **T21** (AI Literacy): 2 dependencies for moderation

**Dependency Analysis**:
- Heavy reliance on T06, T08, T09 is appropriate for grade 6+ skills
- Widget dependencies (T16) seem correct
- T21 moderation dependencies are well-placed

### 9. SPECIFIC SKILL ISSUES

**T22.G5.1.5 - Critical Fix Needed**:
```
Current dependencies:
- T09.G4.01 (Grade 4 skill)
- T22.G5.01 (Grade 5 skill)
- T22.G5.03 (Grade 5 skill)

Problem: This is the FOUNDATION skill for using ChatGPT blocks
but it depends on G5.01 and G5.03 which are conceptual skills
that should probably depend on this!
```

**Recommended Dependency Reversal**:
- T22.G5.04 (renamed from G5.1.5) should depend ONLY on T09.G4.01
- T22.G5.01, G5.02, G5.03 should depend on the basic chatbot block skill
- T22.G5.05 (renamed from G5.04) should depend on the basic skill

### 10. GRADE DISTRIBUTION ANALYSIS

**Distribution**:
- K-2: Very light (2, 2, 2 skills) - Good for foundational concepts
- G3-4: Minimal (1, 1 skills) - Potential gap
- G5: Moderate (4 skills + 1 misplaced) - Transition to coding
- G6: Heavy (11 skills) - Major implementation grade
- G7: Heavy (9 skills) - Advanced features
- G8: Moderate (5 skills) - Specialized/advanced

**Observations**:
- G3-G4 gap suggests missing bridge skills
- G6 has most skills (implementation heavy)
- Good progression from unplugged → observing → using → building → advanced

---

## RECOMMENDED FIXES - PRIORITY ORDER

### PRIORITY 1 (Critical - Breaks Dependencies):
1. **Rename T22.G5.1.5 → T22.G5.04** (or T22.G5.15 to avoid conflicts)
2. **Rename T22.G5.04 → T22.G5.05**
3. **Fix dependencies** for renamed skills
4. **Rename T22.G6.05.5 → T22.G6.055** (or reorganize to T22.G6.05)

### PRIORITY 2 (Important - Improves Clarity):
1. Add implementation details to **T22.G5.02** (make deliverable more concrete)
2. Add hands-on component to **T22.G6.05.5/G6.055** (too conceptual)
3. Break **T22.G8.04** into 2-3 smaller skills (testing harness too complex)
4. Clarify **T22.G7.09** scope (user testing is very broad)

### PRIORITY 3 (Enhancement - Fills Gaps):
1. Add Grade 4 bridge skill (introduction to AI blocks)
2. Add error handling skill in Grade 5-6
3. Add prompt chaining skill in Grade 7
4. Add cost/token awareness in Grade 6-7

### PRIORITY 4 (Polish - Documentation):
1. Add note about G6.04.02 vs G6.06.01-G6.06.03 alternatives
2. Document that many G7 skills can use either approach
3. Add progression note explaining K-2 unplugged → G3+ coded

---

## SKILL NAMING CONVENTIONS ANALYSIS

**Good Examples**:
- T22.GK.01: "Recognize a talking helper vs a silent toy" (clear, concrete)
- T22.G6.02: "Adjust temperature for response creativity" (action-oriented)
- T22.G7.01: "Use system messages to set bot behavior" (specific technique)

**Needs Improvement**:
- T22.G5.02: "Observe chatbot strengths and weaknesses through testing" (what's the output?)
- T22.G6.05.5: "Understand chatbot session types" (too passive/conceptual)
- T22.G7.09: "User-test the chatbot for inclusivity and clarity" (too broad)

---

## OVERALL ASSESSMENT

**Strengths**:
1. Excellent K-2 unplugged progression (building conceptual foundation)
2. Strong integration with other topics (Events, Variables, Conditionals)
3. Good coverage of modern chatbot features (streaming, sessions, RAG, multi-agent)
4. Responsible AI emphasized (moderation, safety, inclusivity)
5. Practical skills (building actual chat interfaces, not just theory)

**Weaknesses**:
1. G5.1.5 numbering breaks convention (critical fix needed)
2. G3-G4 gap needs bridge skills
3. Some skills too broad (G8.04, G7.09)
4. Dependency ordering issues (G5.04 → G5.1.5)
5. Some skills too conceptual (G6.05.5)

**Overall Grade**: B+ (would be A- after fixing numbering and dependencies)

**Recommendation**: This is one of the better-structured topics, but needs critical fixes to skill IDs and dependencies before it can be finalized. The content is excellent, but the organizational issues create confusion.
