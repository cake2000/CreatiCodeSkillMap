# T22 (Chatbots & Prompting) - Comprehensive Optimization Information Report

**Generated:** 2025-11-25
**Purpose:** Complete information gathering for T22 optimization

---

## EXECUTIVE SUMMARY

**Topic:** T22 - Chatbots & Prompting
**Total Skills:** 49 skills (K-8)
**Grade Range:** K, 1, 2, 3, 4, 5, 6, 7, 8
**CreatiCode AI Blocks Available:** 30+ chatbot/LLM-related blocks
**Current Status:** Ready for optimization review

### Quick Stats
- **K-2 Skills:** 6 (picture-based, foundational concepts)
- **Grade 3-5 Skills:** 15 (introduction to chatbot blocks and prompting)
- **Grade 6-8 Skills:** 28 (advanced prompting, RAG, multi-agent, structured output)
- **Key Block Categories:** ChatGPT requests, LLM models, chat UI, semantic search, moderation

---

## PART 1: ALL T22 SKILLS (COMPLETE LIST)

### KINDERGARTEN (2 skills)

**T22.GK.01** - Recognize a talking helper vs a silent toy
*Description:* Students look at picture pairs (a smart speaker that answers questions vs a stuffed animal, or a phone assistant vs a regular clock) and circle which one can talk back when you ask it something. This introduces the idea that some devices can have conversations.
*Dependencies:* None

**T22.GK.02** - Practice asking a picture helper a friendly question
*Description:* Students see a cartoon of a friendly robot helper. They choose from picture cards showing different ways to ask for help (pointing politely vs grabbing, saying "please" vs demanding). They learn that helpers respond better to kind requests.
*Dependencies:* T22.GK.01

---

### GRADE 1 (2 skills)

**T22.G1.01** - Sort good questions from confusing questions
*Description:* Students sort question cards into two piles: clear questions a helper could answer ("What color is the sky?") vs confusing or incomplete questions ("Tell me the thing!"). They practice making one confusing question clearer by adding missing information.
*Dependencies:* T22.GK.02

**T22.G1.02** - Identify what a chatbot might not know
*Description:* Students look at scenarios and decide if a chatbot helper could answer (facts, spelling help) or probably couldn't (what's in your backpack, how you're feeling today). This builds awareness that chatbots don't know everything about you.
*Dependencies:* T22.G1.01

---

### GRADE 2 (2 skills)

**T22.G2.01** - Role-play asking a helper for information
*Description:* One student pretends to be a robot helper while another asks questions. They practice giving clear context ("I need help with my math homework about adding") vs vague requests. Students notice how clear questions get better "robot" answers.
*Dependencies:* T22.G1.01, T22.G1.02

**T22.G2.02** - Decide which questions are okay to ask a helper
*Description:* Students sort question cards into "okay to ask" (homework help, fun facts) vs "not okay to ask" (my home address, passwords, mean things about classmates). They learn that some information should stay private even from helpful robots.
*Dependencies:* T22.G2.01

---

### GRADE 3 (3 skills)

**T22.G3.01** - Identify chatbot behavior from fixed button replies
*Description:* Students read short app stories (one with fixed replies, one with AI that sometimes makes mistakes) and sort them into "chatbot guesses answers" vs "fixed menu responses," explaining why. This introduces the concept that chatbots generate responses while menu-based apps only show pre-written options.
*Dependencies:* T08.G3.01, T22.G2.01, T22.G2.02

**T22.G3.02** - Make a simple ChatGPT request using blocks to ask questions
*Description:* Students use the basic `OpenAI ChatGPT: request [PROMPT] result [VARIABLE]` block with a pre-written question to get a response from ChatGPT. They observe how the block sends a message and receives an answer, learning the fundamental mechanics of AI interaction through blocks.
*Dependencies:* T06.G3.01, T09.G3.05, T22.G3.01

**T22.G3.03** - Display ChatGPT responses in speech bubbles or text
*Description:* Students take the AI response stored in a variable and display it using `say` blocks or label widgets. They learn to make the AI's answers visible to users through simple output methods.
*Dependencies:* T06.G3.01, T09.G3.05, T22.G3.02

---

### GRADE 4 (3 skills)

**T22.G4.01** - Write clear, polite questions for a helper bot
*Description:* Students improve a vague or rude request ("Tell me everything now!!!") into a clear, focused question with context and tone, suitable for a helper bot. They learn that well-structured prompts get better responses.
*Dependencies:* T06.G3.01, T06.G3.09, T07.G2.01, T09.G3.05, T22.G3.01

**T22.G4.02** - Create a simple Q&A chatbot using ChatGPT blocks
*Description:* Students build a basic question-and-answer chatbot that captures user input from a textbox, sends it to ChatGPT using the request block, and displays the response. They create a simple interactive AI application that responds to different questions.
*Dependencies:* T06.G3.09, T07.G2.01, T09.G4.01, T16.G3.05, T22.G3.02, T22.G3.03

**T22.G4.03** - Handle different user questions with ChatGPT
*Description:* Students test their Q&A chatbot with various types of questions (factual, creative, math) and observe how ChatGPT responds differently to each. They learn that AI can handle diverse question types without pre-programmed responses for each one.
*Dependencies:* T04.G2.03, T07.G2.01, T09.G4.01, T13.G3.01, T22.G4.01, T22.G4.02

---

### GRADE 5 (5 skills)

**T22.G5.01** - Flag risky vs safe chatbot prompts
*Description:* Students classify prompts that leak private info or ask for cheating vs safe learning questions, and rewrite one risky prompt to be safe. This builds awareness of responsible AI use.
*Dependencies:* T06.G3.09, T09.G3.05, T22.G3.01, T29.G3.01

**T22.G5.02** - Observe chatbot strengths and weaknesses through testing
*Description:* Students use a pre-built CreatiCode chatbot project without modifying code. They test different types of questions (factual, creative, math, opinion) and document when the bot performs well vs. poorly. They create a simple chart showing "good at" vs "struggles with" categories based on their observations.
*Dependencies:* T22.G4.01, T22.G5.01, T06.G3.01, T09.G3.01.01, T29.G3.01

**T22.G5.03** - Experiment with prompt phrasing to improve responses
*Description:* Students take a question the chatbot answered poorly and systematically try variations: adding context ("I'm in 5th grade"), being more specific ("Explain in 2 sentences"), or providing an example format. They record which changes helped most and write a "prompting tip" based on their experiments.
*Dependencies:* T22.G4.01, T22.G5.02, T06.G3.01, T09.G3.01.01, T29.G3.01

**T22.G5.04** - Use a chatbot block to get AI responses
*Description:* Students use the basic `OpenAI ChatGPT: request [PROMPT] result [VARIABLE]` block to send a simple message to ChatGPT and store the response in a variable. They build a minimal project that displays the AI's answer on the stage, learning the fundamental mechanics of making an AI request before exploring advanced features.
*Dependencies:* T09.G4.01, T22.G5.01, T22.G5.03, T06.G3.01, T29.G3.01

**T22.G5.05** - Identify ChatGPT block parameters in starter code
*Description:* Students examine a simple CreatiCode project using the ChatGPT block and identify what each parameter does (mode, temperature, max length, session). They don't modify the code yet, but label screenshots showing where each parameter is and predict what happens if values change. This prepares them for tracing more complex scripts in G6.
*Dependencies:* T22.G5.02, T22.G5.04, T12.G3.05, T09.G3.03, T12.G4.05, T06.G3.01, T29.G3.01

---

### GRADE 6 (16 skills)

**T22.G6.01.01** - Make a basic ChatGPT request with one parameter
*Description:* Students use the `OpenAI ChatGPT: request [PROMPT] result [VARIABLE]` block and experiment with ONE parameter at a time: either temperature (0-1 for creativity control) OR max tokens (length limit). They observe how changing this single parameter affects responses, building understanding before handling multiple parameters.
*Dependencies:* T05.G5.01, T06.G4.01, T07.G5.01, T09.G4.01, T09.G5.01, T12.G4.05, T16.G5.01, T22.G5.01, T22.G5.05

**T22.G6.01.02** - Configure multiple ChatGPT parameters and conversation flow
*Description:* Students work with multiple ChatGPT block parameters together: mode (streaming or waiting), temperature, max tokens, and session. They trace how these settings interact in a pre-built conversation project, identifying which blocks capture user input and how parameters affect the conversation flow.
*Dependencies:* T05.G5.01, T06.G4.01, T07.G5.01, T08.G4.01, T09.G4.04, T10.G4.01, T12.G4.05, T16.G5.01, T22.G6.01.01

**T22.G6.01.03** - Manage chat history and user input capture
*Description:* Students examine how a chatbot script maintains conversation history using lists or session management. They identify which blocks capture user input, how the conversation log is updated with each turn, and when/how the system clears history. This focuses specifically on data management in multi-turn conversations.
*Dependencies:* T05.G5.01, T07.G5.01, T08.G4.01, T09.G4.01, T09.G4.04, T10.G4.01, T12.G4.05, T16.G5.01, T22.G6.01.02

**T22.G6.02** - Adjust temperature for response creativity
*Description:* Students adjust the ChatGPT block's temperature parameter (scale 0-1, where 0 produces more predictable and focused responses, and 1 produces more creative and varied responses) to control response variability. They experiment with different temperature values for different use cases (e.g., low temperature for factual answers, high temperature for creative stories) and observe how this affects bot behavior.
*Dependencies:* T05.G5.01, T06.G4.01, T07.G5.01, T08.G4.01, T09.G4.04, T10.G4.01, T12.G4.05, T16.G5.01, T22.G5.01, T22.G6.01.01

**T22.G6.03** - Handle streaming mode and long requests
*Description:* Students adjust the ChatGPT block's mode parameter (streaming shows words as they arrive, waiting shows complete response all at once) and max length settings to match different app goals. They learn to use the `OpenAI ChatGPT: cancel request` block to stop a long-running or stuck request, implementing a "Cancel" button that lets users abort slow responses.
*Dependencies:* T05.G5.01, T06.G4.01, T07.G5.01, T08.G4.01, T09.G4.04, T10.G4.01, T12.G4.05, T16.G5.01, T22.G5.01, T22.G6.01.01

**T22.G6.04.01** - Add input widgets for user messages
*Description:* Students use text input widgets and buttons from the UI toolkit to create the input section of a chat interface. They connect a "Send" button to read the textbox value and trigger the chatbot request, learning how UI widgets collect user input for AI interactions.
*Dependencies:* T05.G5.01, T07.G5.01, T09.G5.01, T10.G5.01, T11.G5.01, T16.G5.01, T22.G5.04

**T22.G6.04.02** - Build a conversation log with dynamic updates
*Description:* Students create a scrolling conversation display using label widgets or list displays. They append each user message and bot response to maintain a visible chat history, managing formatting and scroll position as new messages arrive.
*Dependencies:* T05.G5.01, T07.G5.01, T09.G5.01, T10.G5.01, T11.G5.01, T16.G5.01, T22.G6.02, T22.G6.03

**T22.G6.05** - Implement session management for multi-turn conversations
*Description:* Students compare single-turn requests (independent questions) to multi-turn conversations (maintaining context across exchanges). They use the session parameter to maintain conversation context and build a project that demonstrates when context helps vs. when it causes confusion. They implement a "New Chat" button to clear session history.
*Dependencies:* T05.G5.01, T07.G5.01, T09.G5.01, T10.G5.01, T11.G5.01, T16.G5.01, T22.G6.01.02, T22.G6.01.03, T22.G6.02, T22.G6.03

**T22.G6.06.01** - Create and configure a pre-built chat window
*Description:* Students use the `add chat window` block to create and configure a pre-styled chat interface with customizable size, colors, input rows, and visual styling. They explore customization options to match their app's design without building UI from scratch. This provides an alternative approach to T22.G6.04.02 for students who prefer using the pre-built chat window instead of creating their own conversation display.
*Dependencies:* T05.G5.01, T07.G5.01, T09.G5.01, T10.G5.01, T11.G5.01, T16.G5.01, T22.G6.01.02, T22.G6.02, T22.G6.03

**T22.G6.06.02** - Manage chat messages with append and update blocks
*Description:* Students use the `append to chat [CHATNAME] message [...] as [SENDER] icon [...] align [...]` block to add messages to the chat window with proper sender identification and icons. They learn to differentiate user messages from bot responses through sender labels and alignment.
*Dependencies:* T05.G5.01, T07.G5.01, T09.G5.01, T10.G5.01, T11.G5.01, T16.G5.01, T22.G6.02, T22.G6.03, T22.G6.06.01

**T22.G6.06.03** - Display streaming responses in real-time
*Description:* Students implement streaming mode responses using the `update last chat message to [MESSAGE] for chat [CHATNAME]` block to show text appearing word-by-word as the AI generates it. They compare the user experience of streaming vs. waiting mode and understand when each is appropriate.
*Dependencies:* T05.G5.01, T07.G5.01, T09.G5.01, T10.G5.01, T11.G5.01, T16.G5.01, T22.G6.02, T22.G6.03, T22.G6.06.02

**T22.G6.07** - Debug off-topic responses by rewriting prompts
*Description:* Students investigate cases where the bot rambles, ignores instructions, or refuses to answer. They edit the system message, add clarifying phrases, or insert reminders about format, then re-run the chat to verify improvement. This introduces iterative prompting as a debugging skill.
*Dependencies:* T05.G5.01, T06.G4.08, T07.G5.01, T08.G4.01, T09.G4.04, T10.G4.01, T12.G4.05, T16.G5.01, T22.G4.01, T22.G5.01, T22.G6.01.02

**T22.G6.08** - Use multiple chatbot sessions with the select chatbot block
*Description:* Students use the `select chatbot [1/2/3/4]` block to maintain separate conversation threads. They build a project where different characters (e.g., a teacher and a student) each have their own chat history, switching between sessions to continue each conversation independently.
*Dependencies:* T05.G5.01, T07.G5.01, T09.G5.01, T10.G5.01, T11.G5.01, T16.G5.01, T22.G6.01.02, T22.G6.01.03, T22.G6.04.02

**T22.G6.09** - Combine temperature, mode, and session for character bots
*Description:* Students create two distinct character bots (e.g., formal historian, casual gamer) and configure temperature, mode, and session settings differently for each. They build a project with multiple chatbot personalities demonstrating mastery of parameter configuration.
*Dependencies:* T05.G5.01, T07.G5.01, T09.G5.01, T10.G5.01, T11.G5.01, T16.G5.01, T22.G6.02, T22.G6.03, T22.G6.05, T22.G6.08

**T22.G6.10** - Design a multi-stage chat flow with transitions
*Description:* Students design a chatbot that progresses through stages (greeting → main conversation → closing) with different behaviors at each stage. They implement transition logic that changes temperature or system instructions based on conversation progress.
*Dependencies:* T05.G5.01, T07.G5.01, T09.G5.01, T10.G5.01, T11.G5.01, T16.G5.01, T22.G6.02, T22.G6.05, T22.G6.07

**T22.G6.11** - Analyze and document a complete chatbot system
*Description:* Students examine a full-featured chatbot project and create documentation showing: parameter choices, UI flow, conversation states, and prompt strategies. They trace how all components work together and suggest one improvement.
*Dependencies:* T05.G5.01, T07.G5.01, T09.G5.01, T10.G5.01, T11.G5.01, T16.G5.01, T22.G6.04.02, T22.G6.07, T22.G6.08

---

### GRADE 7 (9 skills)

**T22.G7.01** - Use system messages to set bot behavior
*Description:* Students learn how to use the `OpenAI ChatGPT: system request` block to provide initial instructions that guide the chatbot's behavior. They experiment with simple system messages (e.g., "Be helpful and concise") and observe how this affects all subsequent responses. This introduces system-level prompting as a foundational technique for controlling bot personality and behavior.
*Dependencies:* T22.G6.02, T22.G6.03, T22.G6.07

**T22.G7.02.01** - Create and use custom personas with system messages
*Description:* Students design a detailed character brief (e.g., "sarcastic space tour guide," "friendly science tutor") and write a comprehensive system message that defines the bot's personality, tone, and behavior guidelines. They test how well the bot maintains this persona across different questions and refine the system message based on results.
*Dependencies:* T22.G6.02, T22.G6.03, T22.G6.07, T22.G7.01

**T22.G7.02.02** - Use few-shot prompting with example exchanges
*Description:* Students provide 2-3 example question-answer exchanges that model the expected voice, style, and response format for the chatbot. They use few-shot prompting to demonstrate the pattern they want the bot to follow, learning how examples shape subsequent responses more effectively than instructions alone.
*Dependencies:* T22.G6.02, T22.G6.03, T22.G6.07, T22.G7.02.01

**T22.G7.03** - Manage chat history and reset logic
*Description:* Students practice when to continue a conversation versus start "new chat." They add buttons such as "Ask follow-up" (continue session) and "Start new topic" (new session), and they implement a summary label that tells the user what context is currently active. This works with either custom-built conversation displays or pre-built chat windows.
*Dependencies:* T06.G5.01, T08.G5.01, T09.G5.04, T22.G6.07, T22.G6.08

**T22.G7.04** - Capture data from UI widgets and inject into prompts
*Description:* Students create widgets (dropdowns, sliders, toggles) that gather key facts (age range, preferred topic, mood). Before contacting ChatGPT, they assemble those data values into the prompt, ensuring the bot answers with personalized tips or stories. This works with either custom-built conversation displays or pre-built chat windows.
*Dependencies:* T22.G6.07, T22.G7.02.01, T10.G5.01

**T22.G7.05** - Add moderation guardrails and escalation paths
*Description:* Students integrate the `get moderation result for [TEXT]` block on both user input and bot output. If a message fails moderation, the chatbot responds with a pre-written supportive message, logs the incident, and offers to connect the user with a human helper. This meets AI4K12 priorities around responsible deployment. This works with either custom-built conversation displays or pre-built chat windows.
*Dependencies:* T06.G5.01, T08.G5.01, T09.G5.04, T21.G6.06, T22.G5.01, T22.G6.07

**T22.G7.06** - Attach images and files to chatbot conversations
*Description:* Students use the `attach costume [NAME] to chat`, `attach files to chat`, and `attach file from Google Drive [URL] to chat` blocks to send images or documents to the chatbot for analysis. They build an app where users can upload pictures from their device or link files from Google Drive, then ask the bot questions about the content, learning multimodal AI interactions.
*Dependencies:* T22.G7.02.01

**T22.G7.07** - Use image moderation to filter visual content
*Description:* Students use the `get moderation result for image at URL [URL]` and `get moderation result for costume named [NAME]` blocks to check images before processing or displaying them. They implement a content filter that prevents inappropriate images from being analyzed by the chatbot.
*Dependencies:* T21.G6.07, T22.G7.05, T22.G7.06

**T22.G7.08** - Compare different LLM models using the generic LLM block
*Description:* Students use the `LLM model [PROVIDER] request [PROMPT]` block with both "small" and "large" model options to compare response quality, speed, and cost trade-offs. They set system instructions using the `LLM set system instruction [INSTRUCTION] for model [PROVIDER]` block and build a comparison tool that shows how different models answer the same prompt, learning when to use smaller/faster models vs larger/more capable ones.
*Dependencies:* T22.G6.02, T22.G7.01

**T22.G7.09** - User-test the chatbot for inclusivity and clarity
*Description:* Students prepare at least four tester personas (age, language level, accessibility need), run scripted conversations, and note where the bot confuses or excludes users. They adjust prompts or UI affordances (e.g., add a "simplify answer" button) and document changes. This works with either custom-built conversation displays or pre-built chat windows.
*Dependencies:* T22.G6.07, T22.G7.02.01

---

### GRADE 8 (7 skills)

**T22.G8.01.01** - Import data and create a semantic index
*Description:* Students import curriculum notes, facts, or reference documents into a table and use the `create semantic database from table [TABLE]` block to build a semantic index. They learn how semantic indexing enables meaning-based search rather than just keyword matching, preparing the foundation for retrieval-augmented generation.
*Dependencies:* T06.G6.01, T09.G6.01, T22.G7.02.01, T07.G6.01, T12.G6.01

**T22.G8.01.02** - Search semantic database with filters and conditions
*Description:* Students use the `search semantic database with [QUERY] store top (K) in table [TABLE]` block to perform meaning-based searches that return the most relevant results. They experiment with different query phrasings and K values to retrieve the right amount of context, learning to filter and rank results by semantic similarity.
*Dependencies:* T06.G6.01, T09.G6.01, T22.G8.01.01, T07.G6.01, T10.G6.01

**T22.G8.01.03** - Integrate search results into chatbot prompts (RAG)
*Description:* Students complete the RAG (Retrieval-Augmented Generation) pipeline by prepending retrieved facts to their ChatGPT prompts. Before each ChatGPT call, they search the semantic database, extract relevant snippets, and inject them into the prompt so the bot's answers stay grounded in source material rather than relying on the model's training data alone.
*Dependencies:* T06.G6.01, T09.G6.01, T22.G7.03, T22.G7.05, T22.G8.01.02

**T22.G8.02** - Coordinate multi-agent conversations and summaries
*Description:* Students use the `select chatbot [1/2/3/4]` block to spin up two sessions (e.g., historian vs. scientist) and a third "moderator" script that alternates turns, enforces time limits, and summarizes agreements for the user. This mirrors advanced creative AI use cases.
*Dependencies:* T06.G6.01, T09.G6.01, T22.G6.08, T22.G7.02.01, T22.G7.02.02

**T22.G8.03.01** - Specify JSON format in prompts
*Description:* Students write system messages and prompts that instruct ChatGPT to respond in a specific JSON format (e.g., `{"action":"schedule","details":"..."}`). They experiment with clear format specifications and examples to ensure consistent structured responses, learning how to guide the model toward machine-readable output.
*Dependencies:* T03.G6.01, T06.G6.01, T09.G6.01, T22.G7.02.01, T22.G7.02.02

**T22.G8.03.02** - Parse and extract JSON responses
*Description:* Students use string parsing or JSON parsing blocks to extract structured data from ChatGPT's responses. They handle the response format, extract specific fields (like "action" and "details"), and store values in variables for further processing. They implement error handling for malformed JSON.
*Dependencies:* T06.G6.01, T09.G6.01, T22.G8.03.01, T07.G6.01, T10.G6.01

**T22.G8.03.03** - Route parsed data to conditional actions and tools
*Description:* Students complete the structured output pipeline by routing parsed JSON data to different helper blocks based on the action field: calculator, table lookup, calendar writer, etc. They implement conditional logic that triggers appropriate tools and add user confirmations showing exactly what action the bot executed.
*Dependencies:* T03.G6.01, T06.G6.01, T09.G6.01, T22.G7.05, T22.G8.03.02

**T22.G8.04** - Create an automated chatbot testing and reporting system
*Description:* Students build a testing harness that runs their chatbot through a suite of test prompts (stored in a table), logs each response, flags moderation events, and generates a summary report showing pass/fail rates and edge cases. They add code to track response times and detect when the bot goes off-topic, creating an automated quality assurance system for their chatbot.
*Dependencies:* T06.G6.01, T08.G6.01, T09.G6.01, T22.G7.05, T22.G7.09

**T22.G8.05** - Integrate web search into chatbot responses
*Description:* Students use the `web search [QUERY] store top (K) in table [TABLE]` block to fetch current information before generating a response. They prepend search results to the prompt so the chatbot can answer questions about recent events or live data not in its training.
*Dependencies:* T06.G6.01, T09.G6.01, T22.G8.01.02, T07.G6.01, T10.G6.01

---

## PART 2: CREATICODE AI/CHATBOT BLOCKS (COMPLETE LIST)

### Core ChatGPT/LLM Blocks

**Block ID: openaichatcompletion**
- **Syntax:** `OpenAI ChatGPT: request [PROMPT] result [VARIABLE v] mode [MODE v] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE v]`
- **Usage:** Sends PROMPT to ChatGPT Turbo 3.5 API and stores result in VARIABLE
- **Parameters:**
  - MODE: 'streaming' (continuous updates) or 'waiting' (wait for complete response)
  - MAXLENGTH: Maximum tokens (100 tokens ≈ 75 words)
  - TEMPERATURE: 0-1 (0=predictable, 1=creative)
  - SESSIONTYPE: 'new chat' or 'continue'
- **Features:** Strong moderation filter, streaming support with ✅ end marker

**Block ID: openaichatcompletionsystem**
- **Syntax:** `OpenAI ChatGPT: system request [PROMPT] session [SESSIONTYPE v] result [VARIABLE v] temperature [T]`
- **Usage:** Sends system-level instructions to guide ChatGPT behavior
- **Purpose:** Administrative instructions treated more seriously than user messages

**Block ID: openai_chatgpt_cancel**
- **Syntax:** `OpenAI ChatGPT: cancel request`
- **Usage:** Cancels an ongoing ChatGPT request
- **Use case:** Stop long-running or stuck requests

**Block ID: llmchatcompletion**
- **Syntax:** `LLM model [PROVIDER] request [PROMPT] result [VARIABLE v] mode [MODE v] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE v]`
- **Usage:** Generic LLM block supporting multiple providers
- **Providers:** "small" or "large" model options
- **Parameters:** Same as OpenAI ChatGPT block

**Block ID: llmsysteminstruction**
- **Syntax:** `LLM set system instruction [INSTRUCTION] for model [PROVIDER]`
- **Usage:** Sets system-level instruction for specific LLM provider
- **Providers:** "small" or "large"

---

### Chat Session Management

**Block ID: switchchatbot**
- **Syntax:** `select ChatGPT bot [BOTID v]`
- **Usage:** Switch between 4 independent chat threads (BOTID: 1/2/3/4)
- **Use case:** Multi-agent conversations, character bots with separate histories

---

### Chat Window UI Blocks

**Block ID: widget_addchatwindow**
- **Syntax:** `add chat window x (X) y (Y) width (WIDTH) height (HEIGHT) input rows (ROWS) background [BG] border [BORDERCOLOR] name [NAME]`
- **Usage:** Creates a pre-styled chat interface with input box and history panel
- **Features:** Customizable size, colors, input rows

**Block ID: widget_appendchatmessage**
- **Syntax:** `append to chat [CHATNAME v] message [MESSAGE] as [SENDER] icon [ICON v] align [ALIGN v] text size (TEXTSIZE) color [COLOR] background [BG]`
- **Usage:** Adds a message to chat history with sender identification
- **Features:** Custom icons, alignment, styling

**Block ID: widget_updatelastchatmessage**
- **Syntax:** `update last chat message to [MESSAGE] for chat [CHATNAME v]`
- **Usage:** Updates the last message in chat history
- **Use case:** Streaming responses, real-time updates

---

### Multimodal AI Blocks (Files & Images)

**Block ID: attachimagetochat**
- **Syntax:** `attach costume [COSTUMENAME] to chat`
- **Usage:** Sends a costume image as part of next ChatGPT request
- **Use case:** Visual question answering

**Block ID: attachfilestochat**
- **Syntax:** `attach files to chat`
- **Usage:** Opens file selection dialog to attach local files to chat
- **Returns:** List of file paths separated by "\n"

**Block ID: attachgooglefiletochat**
- **Syntax:** `attach file from Google Drive [URL] to chat`
- **Usage:** Attaches a Google Drive file to chat session

---

### Content Moderation Blocks

**Block ID: getmoderationresult**
- **Syntax:** `get moderation result for [TEXT]`
- **Usage:** Uses AI moderation to check text input
- **Returns:** "Pass" or "Fail"

**Block ID: getmoderationresult2**
- **Syntax:** `get moderation result for image at URL [INPUT]`
- **Usage:** Checks image at URL for inappropriate content
- **Returns:** "Pass" or "Fail"

**Block ID: getmoderationresult3**
- **Syntax:** `get moderation result for costume named [INPUT]`
- **Usage:** Checks costume image for inappropriate content
- **Returns:** "Pass" or "Fail"

---

### Semantic Search & RAG Blocks

**Block ID: addtabletopinecone**
- **Syntax:** `create semantic database from table [TABLE v]`
- **Usage:** Builds semantic index from table data using embedding vectors
- **Requirements:** Table must have a 'key' column
- **Process:** Converts key values to embeddings, stores with metadata

**Block ID: searchfrompinecone**
- **Syntax:** `search semantic database with [QUERY] store top (K) in table [t1 v] filter by column [FIELD] of value [VALUE]`
- **Usage:** Semantic search using query embeddings
- **Features:** Returns top K results, optional metadata filtering

**Block ID: searchfrompinecone2**
- **Syntax:** `search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE v]`
- **Usage:** Advanced semantic search with SQL-like conditions
- **Features:** Complex filtering with AND/OR, comparison operators

---

### Web Search Block

**Block ID: googlesearch**
- **Syntax:** `web search [QUERY] store top (K) in table [TABLE v]`
- **Usage:** Performs web search and stores results in table
- **Columns:** title, link, snippet
- **Use case:** RAG with current information

---

### Speech & Voice Blocks (Related to Chatbots)

**Block ID: ai_startspeech**
- **Syntax:** `start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`
- **Usage:** Starts recording voice for Azure speech recognition

**Block ID: ai_startopenaispeech**
- **Syntax:** `OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`
- **Usage:** Starts recording voice for OpenAI Whisper recognition

**Block ID: ai_endspeech**
- **Syntax:** `end speech recognition`
- **Usage:** Stops recording and triggers speech-to-text API

**Block ID: ai_textfromspeech**
- **Syntax:** `text from speech`
- **Usage:** Reporter block returning recognized speech text

**Block ID: ai_clearspeech**
- **Syntax:** `clear speech text`
- **Usage:** Clears the speech text buffer

**Block ID: ai_speakinlanguage**
- **Syntax:** `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]`
- **Usage:** Text-to-speech using Azure API
- **Parameters:** Language, voice type, speed, pitch, volume

**Block ID: ai_stopspeaking**
- **Syntax:** `stop speaking`
- **Usage:** Stops AI speech output

**Block ID: ai_startrecognizer**
- **Syntax:** `start continuous speech recognition in [LANGUAGE v] into list [LISTNAME v]`
- **Usage:** Continuous speech recognition with streaming results

**Block ID: ai_stoprecognizer**
- **Syntax:** `stop continuous speech recognition`
- **Usage:** Stops continuous recognition

---

### Additional AI Blocks (Vision, NLP, ML - context for T23, T21)

**Block ID: ai_facedetection**
- Turns on camera and detects faces, writes to table

**Block ID: ai_parsesentence**
- Analyzes sentence structure, writes to table

**Block ID: ai_bodydetection**
- 2D body part recognition from camera

**Block ID: ai_bodydetection3**
- 3D pose detection from camera

**Block ID: ai_handdetection3**
- Hand detection from camera

**Block ID: ai_createknnclassifier**
- Creates K-Nearest Neighbor classifier from table data

**Block ID: ai_predictknnclassifier**
- Uses KNN classifier to predict labels

**Block ID: ai_openaiimagereporter**
- DALL-E image generation

**Block ID: ai_xoimagereporter**
- XO AI image generation

**Block ID: create_nn_model, save_model, load_model, addlayertomodel, compile_model, train_model, predict_by_model**
- Neural network training and inference blocks

---

## PART 3: SPEC REQUIREMENTS FOR T22

From `/media/binyu/USB2/dev/CreatiCodeSkillMap/spec_v2_updated.md`:

### Topic Description (from spec)
**T22: AI Chatbots & Information Apps (34 skills)**
- Designing chatbot conversations
- Using LLMs for information retrieval
- Understanding how chatbots work
- RAG and semantic search

### AI4K12 Alignment Goals
- Category B: Representation & Reasoning (creating representations for AI)
- Category C: Machine Learning (using AI models)
- Category D: Ethical AI System Design and Programming
- Category E: Societal Impacts of AI

### K-2 Requirements
- **Deferred to G3+** - No K-2 picture-based skills specified in original spec
- **ACTUAL:** T22 has K-2 skills (6 skills across K, 1, 2)
- **ISSUE:** Spec says "Deferred to G3+" but allskills.md has K-2 content

### Grade 3-8 Requirements
- Block-based coding using CreatiCode
- Auto-gradable outcomes
- Progressive difficulty from G3 (basic requests) to G8 (RAG, multi-agent)
- Explicit dependencies (avg 3.72 per skill across system)

### Quality Standards
1. **Developmentally Appropriate:** Grade-aligned complexity
2. **Standards-Aligned:** CSTA + AI4K12 explicit mapping
3. **Auto-Gradable:** Runtime checks, code structure analysis
4. **Dependency-Driven:** Explicit prerequisites
5. **Accessible & Inclusive:** Clear instructions, scaffolding
6. **Granular & Focused:** One learning objective per skill
7. **CreatiCode-Specific:** Leverages unique platform capabilities

---

## PART 4: PROJECT CONTEXT (from 00-START-HERE.md)

### Overall System
- **Total Skills:** 1,155 skills (note: spec says 1,119, but includes later additions)
- **Topics:** 36
- **Domains:** 5 (CSTA-aligned)
- **Grades:** K-8 (K-2 picture-based, 3-8 coding)

### Domain Assignment
**T22** is in **Domain 3: Applications & AI (D3)**
- Topics: T14-T24 (295 skills, 26.4% of system)
- Focus: Project-based application of programming core + AI integration
- K-2: Minimal (pre-skills only for some topics)
- 3-8: Project-based application of programming core + AI integration

### Competition Alignment
T22 skills support:
- **Project competitions:** Planning, documentation, ethics
- **Scratch Olympiad:** Project-based creativity, technical proficiency
- **Chinese contests:** Structured problem-solving

### Implementation Status
- **Phase 1 (COMPLETE):** Skill definition with dependencies
- **Phase 2 (NEXT):** Auto-grading specifications
- **Phase 3 (FUTURE):** Content & examples
- **Phase 4 (FUTURE):** Teacher tools
- **Phase 5 (FUTURE):** Student experience

---

## PART 5: INITIAL OBSERVATIONS & POTENTIAL ISSUES

### Issue 1: K-2 Skills Contradiction
**Problem:** Spec v2 says T22 is "Deferred to G3+" but allskills.md has 6 K-2 skills (GK.01, GK.02, G1.01, G1.02, G2.01, G2.02)

**Impact:** Inconsistency between spec and implementation

**Recommendation:**
- Option A: Keep K-2 skills and update spec (makes sense for AI literacy foundation)
- Option B: Move K-2 skills to a different topic or remove them

### Issue 2: Grade 6 Skill Density
**Problem:** Grade 6 has 16 skills (33% of all T22 skills), while other grades have 2-9 skills

**Breakdown:**
- K: 2 skills
- G1: 2 skills
- G2: 2 skills
- G3: 3 skills
- G4: 3 skills
- G5: 5 skills
- G6: 16 skills ⚠️ (spike)
- G7: 9 skills
- G8: 7 skills

**Impact:** Uneven learning load, potential pacing issues

**Recommendation:** Consider redistributing G6 skills to G5/G7 or breaking into sub-skills

### Issue 3: Sub-Skill Numbering Inconsistency
**Problem:** Some skills use sub-numbering (e.g., T22.G6.01.01, T22.G6.01.02, T22.G6.01.03) while others don't

**Examples:**
- G6: T22.G6.01.01, T22.G6.01.02, T22.G6.01.03 (3 sub-skills)
- G6: T22.G6.04.01, T22.G6.04.02 (2 sub-skills)
- G6: T22.G6.06.01, T22.G6.06.02, T22.G6.06.03 (3 sub-skills)
- G7: T22.G7.02.01, T22.G7.02.02 (2 sub-skills)
- G8: T22.G8.01.01, T22.G8.01.02, T22.G8.01.03 (3 sub-skills)
- G8: T22.G8.03.01, T22.G8.03.02, T22.G8.03.03 (3 sub-skills)

**Impact:** Inconsistent skill granularity, possible counting issues

**Recommendation:** Review if sub-skills should be consolidated or if non-sub skills need breaking down

### Issue 4: Alternative Path Dependencies
**Problem:** Some skills have "Alternative UI Paths (need at least one)" in dependencies

**Example:** T22.G7.04 lists alternative UI paths but dependency structure doesn't formally support OR logic

**Impact:** Dependency graph tools may not handle "at least one of" logic

**Recommendation:** Clarify dependency model or restructure skills

### Issue 5: Missing AI4K12 Category Mapping
**Problem:** Skills don't explicitly show AI4K12 category (A/B/C/D/E) in the extracted data

**Impact:** Can't verify AI4K12 alignment without additional analysis

**Recommendation:** Add AI4K12 category to each T22 skill

### Issue 6: Voice Integration Unclear
**Problem:** T22 focuses on text chatbots but CreatiCode has extensive speech blocks

**Question:** Should T22 include voice-based chatbot skills or are those in T23 (Voice, Vision & Gesture)?

**Recommendation:** Clarify scope boundary between T22 (text chat) and T23 (voice interfaces)

### Issue 7: RAG Skills Late Introduction
**Problem:** RAG (Retrieval-Augmented Generation) only appears in G8, but it's a fundamental chatbot pattern

**Current:** T22.G8.01.01, T22.G8.01.02, T22.G8.01.03 (semantic database + RAG)

**Question:** Should simpler RAG concepts appear earlier (G6/G7)?

**Recommendation:** Consider introducing basic fact-retrieval pattern in G6/G7 before full RAG in G8

### Issue 8: Multimodal Skills Organization
**Problem:** Image/file attachment skills appear in G7 (T22.G7.06, T22.G7.07) but could be considered separate from pure chatbot prompting

**Question:** Are multimodal AI interactions core to "Chatbots & Prompting" or should they be in a different topic?

**Recommendation:** Clarify topic scope - is T22 text-only or multimodal chatbots?

### Issue 9: Testing Skills Placement
**Problem:** T22.G8.04 (automated testing) is the only testing skill, appears very late

**Question:** Should earlier grades have simpler testing concepts (manual test plans in G5/G6)?

**Recommendation:** Consider adding progressive testing skills earlier

### Issue 10: Skill Count Discrepancy
**Problem:** Spec says T22 has 34 skills, but count shows 49 skills

**Possible reasons:**
- Sub-skills counted differently
- Skills added after spec finalization
- Counting error

**Recommendation:** Verify official skill count and update spec or allskills.md

---

## PART 6: BLOCK COVERAGE ANALYSIS

### Blocks Well-Covered by Skills
✅ **openaichatcompletion** - Covered extensively (G3.02, G5.04, G6.01.01, G6.02, G6.03, etc.)
✅ **openaichatcompletionsystem** - Covered (G7.01, G7.02.01)
✅ **openai_chatgpt_cancel** - Covered (G6.03)
✅ **llmchatcompletion** - Covered (G7.08)
✅ **llmsysteminstruction** - Covered (G7.08)
✅ **switchchatbot** - Covered (G6.08, G8.02)
✅ **widget_addchatwindow** - Covered (G6.06.01)
✅ **widget_appendchatmessage** - Covered (G6.06.02)
✅ **widget_updatelastchatmessage** - Covered (G6.06.03)
✅ **attachimagetochat** - Covered (G7.06)
✅ **attachfilestochat** - Covered (G7.06)
✅ **attachgooglefiletochat** - Covered (G7.06)
✅ **getmoderationresult** - Covered (G7.05)
✅ **getmoderationresult2** - Covered (G7.07)
✅ **getmoderationresult3** - Covered (G7.07)
✅ **addtabletopinecone** - Covered (G8.01.01)
✅ **searchfrompinecone** - Covered (G8.01.02)
✅ **searchfrompinecone2** - Covered (G8.01.02)
✅ **googlesearch** - Covered (G8.05)

### Blocks NOT Covered (or unclear)
⚠️ **Speech blocks** (ai_startspeech, ai_endspeech, etc.) - Likely in T23, but voice chatbots could be T22
⚠️ **ai_startrecognizer** (continuous speech) - Could be voice chatbot feature
⚠️ **Vision/body detection blocks** - Likely T23
⚠️ **ai_parsesentence** - NLP analysis, could be used in chatbot contexts
⚠️ **KNN/ML blocks** - Likely T23 or T21

---

## PART 7: DEPENDENCY ANALYSIS

### Most Referenced Skills (from other topics)
These skills are frequently required by T22 skills:

**From T09 (Variables):**
- T09.G3.01.01, T09.G3.03, T09.G3.05, T09.G4.01, T09.G4.04, T09.G5.01, T09.G6.01

**From T06 (Events):**
- T06.G3.01, T06.G3.09, T06.G4.01, T06.G4.08, T06.G5.01, T06.G6.01

**From T07 (Loops):**
- T07.G2.01, T07.G5.01, T07.G6.01

**From T08 (Conditionals):**
- T08.G3.01, T08.G4.01, T08.G5.01, T08.G6.01

**From T05 (Design):**
- T05.G5.01 (appears in many G6 skills)

**From T10 (Lists/Tables):**
- T10.G4.01, T10.G5.01, T10.G6.01

**From T11 (Functions):**
- T11.G5.01

**From T12 (Organization):**
- T12.G3.05, T12.G4.05, T12.G6.01

**From T16 (UI Widgets):**
- T16.G3.05, T16.G5.01

**From T21 (AI Media):**
- T21.G6.06, T21.G6.07 (moderation skills)

**From T29 (Text/NLP):**
- T29.G3.01

---

## PART 8: RECOMMENDATIONS FOR OPTIMIZATION

### Priority 1: Resolve Structural Issues
1. **Fix K-2 spec contradiction** - Decide if K-2 skills stay or go
2. **Rebalance Grade 6** - Redistribute 16 skills across G5/G6/G7
3. **Standardize sub-skill numbering** - Consistent granularity
4. **Clarify alternative dependency logic** - Formalize OR dependencies

### Priority 2: Improve Skill Distribution
1. **G3-G5 could use more scaffolding** - Only 11 skills total before G6 explosion
2. **Introduce RAG concepts earlier** - Basic fact lookup in G6/G7
3. **Add progressive testing skills** - Manual testing in G5/G6, automated in G8
4. **Consider voice chatbot skills** - Or clarify they're in T23

### Priority 3: Enhance AI4K12 Alignment
1. **Add explicit AI4K12 categories** to each skill
2. **Map ethical considerations** - Which skills address Category D/E?
3. **Verify representation skills** - Which skills address Category B?

### Priority 4: Verify Block Coverage
1. **Check speech block assignment** - Are voice chatbots T22 or T23?
2. **Verify all chatbot blocks covered** - Cross-reference blockdes8.txt
3. **Document intentionally excluded blocks** - Explain why some blocks aren't in T22

### Priority 5: Improve Documentation
1. **Add skill count to spec** - Current mismatch (34 vs 49)
2. **Create skill progression diagram** - Visual map K-8
3. **Document design decisions** - Why G6 spike? Why K-2 included?
4. **Add example projects** - One per grade level

---

## PART 9: CROSS-REFERENCES

### Related Topics
- **T21 (AI Media):** Image generation, creative AI (dependency for T22.G7 moderation)
- **T23 (Voice, Vision & Gesture):** Speech interfaces, potentially voice chatbots
- **T24 (XO & AI Practices):** AI-assisted coding, may overlap with chatbot use
- **T29 (Text/NLP):** Text data processing (dependency for T22)

### Relevant CSTA Standards
(Would need to extract from skill metadata - not shown in current data)

### AI4K12 Categories
(Would need to add to each skill - not currently in data)

---

## APPENDICES

### Appendix A: Skill ID Format
- **K-2:** T22.GK.01, T22.G1.01, T22.G2.01
- **3-8 (simple):** T22.G3.01, T22.G4.01
- **3-8 (sub-skills):** T22.G6.01.01, T22.G6.01.02, T22.G8.03.01

### Appendix B: Block ID Naming Convention
- **AI category:** ai_* (ai_startspeech, ai_facedetection)
- **ChatGPT:** openaichatcompletion, openai_chatgpt_cancel
- **Generic LLM:** llmchatcompletion, llmsysteminstruction
- **Widgets:** widget_addchatwindow, widget_appendchatmessage
- **Search:** googlesearch, searchfrompinecone
- **Moderation:** getmoderationresult, getmoderationresult2
- **Attachments:** attachimagetochat, attachfilestochat

### Appendix C: Streaming Response Pattern
```
MODE = 'streaming'
Loop until response ends with '✅':
  - Read latest partial response
  - Update UI with current text
End loop
```

### Appendix D: Session Management Pattern
```
SESSIONTYPE = 'new chat' → Start fresh conversation
SESSIONTYPE = 'continue' → Maintain context from previous messages
```

---

## NEXT STEPS

1. **Review this report** with curriculum team
2. **Make decisions** on the 10 identified issues
3. **Update spec v2** to match implementation (or vice versa)
4. **Rebalance Grade 6** skills
5. **Add AI4K12 categories** to each skill
6. **Create optimization plan** based on priorities
7. **Generate optimized skills** document
8. **Validate dependencies** with graph tool
9. **Create example projects** for each grade
10. **Document design rationale** for future reference

---

**END OF REPORT**

Generated: 2025-11-25
Report Author: Claude (CreatiCode Skill Map Optimization Assistant)
Files Analyzed:
- /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
- /media/binyu/USB2/ScratchCopilot/blockdes8.txt
- /media/binyu/USB2/dev/CreatiCodeSkillMap/spec_v2_updated.md
- /media/binyu/USB2/dev/CreatiCodeSkillMap/00-START-HERE.md
