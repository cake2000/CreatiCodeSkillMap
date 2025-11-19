# T22 – Chatbots & Prompting: G6–8 Skill List (Draft v2)

Topic reference: `T22 Chatbots` in `domains_topics_overview.md`
Domain: Programming Core (D2) & Computing and Society (D5) · CSTA focus: MS-PRO-PF, MS-PRO-TR, MS-CAS-ET (with links to MS-PRO-DH, MS-CAS-HC)

Each skill below has:

- a stable **ID** (`T22.G<grade>.<nn>`),
- an IXL-style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** T22 now includes **concept-only Grade 3–5** chat/AI helper skills plus **applied Grade 6–8** prompting workflows.  
- G3–5: Identify chatbot behavior vs fixed scripts, practice polite/safe prompts, and classify risky vs good questions without touching parameters.  
- G6–8: Design prompt flows, wire CreatiCode’s ChatGPT block, capture user intent via widgets, log conversations, enforce guardrails, and layer retrieval/tools for reliable answers. Theory about machine learning lives elsewhere—this topic is the day-to-day craft of prompting.  
- _AI4K12:_ Humans & AI; Machine Learning (language); Ethical AI Design; Societal Impacts.

---

## Grade 3–5 (concept-only, no coding)

### T22.G3.01 – Tell chatbot behavior from fixed button replies

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script


- **Short name:** Chatbot or fixed script?  
- **Description:** Students read short app stories (one with fixed replies, one with AI that sometimes makes mistakes) and sort them into “chatbot guesses answers” vs “fixed menu responses,” explaining why.  
- **Challenge format:** Scenario sorting + justification; auto-graded.  
- **AI4K12:** A1 Humans & AI.

### T22.G4.01 – Write clear, polite questions for a helper bot

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G3.01: Tell chatbot behavior from fixed button replies


- **Short name:** Make a good request  
- **Description:** Students improve a vague or rude request (“Tell me everything now!!!”) into a clear, focused question with context and tone, suitable for a helper bot.  
- **Challenge format:** Prompt rewrite checklist; auto-graded for clarity/tone.  
- **AI4K12:** A3 Human role; D1 Ethical Design.

### T22.G5.01 – Flag risky vs safe chatbot prompts

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G3.01: Tell chatbot behavior from fixed button replies


- **Short name:** Which questions are okay to ask?  
- **Description:** Students classify prompts that leak private info or ask for cheating vs safe learning questions, and rewrite one risky prompt to be safe.  
- **Challenge format:** Drag to Safe/Risky + rewrite; auto-graded.  
- **AI4K12:** D1 Ethical Design; E1 Societal Impacts.

---

## Grade 6

Grade 6 students learn to read and build simple LLM-powered chats. They trace how prompts and responses travel through blocks, tune ChatGPT parameters, and implement a basic chat UI with clear iteration steps when the model drifts off topic.

### T22.G6.01 – Trace how a chatbot script processes each turn

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G5.01: Flag risky vs safe chatbot prompts


- **Short name:** Follow prompt → response flow in block code
- **Description:** Students examine a pre-built CreatiCode project that uses `OpenAI ChatGPT: request [PROMPT] result [VARIABLE] mode [waiting] length [...] temperature [...] session [...]`. They identify which blocks capture user input, how the conversation log list is updated, and when the system clears history. This builds foundational reading skills before they modify anything.
- **Challenge format:** Read/trace activity. Learners receive an annotated script and answer targeted questions (e.g., “Which variable stores the last bot reply?” “When do we start a new chat session?”). Auto-grading checks for precise explanations tied to block names.
- **CSTA:** MS-PRO-PF-01.

### T22.G6.02 – Tune ChatGPT block settings for tone and length

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G4.01: Write clear, polite questions for a helper bot
  * T22.G5.01: Flag risky vs safe chatbot prompts


- **Short name:** Experiment with temperature, mode, and max tokens
- **Description:** Students adjust the ChatGPT block’s temperature, length, and mode (streaming vs. waiting) to match different app goals (serious tutor vs. silly NPC). They compare outputs and decide which configuration best fits each scenario, reinforcing that prompting includes parameter control.
- **Challenge format:** Concept + applied testing. Students are given three user stories and must produce screenshots/logs showing how a setting change improved the fit. Auto-grading checks that all three configuration sets differ and that reflections justify each choice.
- **CSTA:** MS-PRO-TR-12.

### T22.G6.03 – Build a basic chat UI with send button and log

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G5.01: Flag risky vs safe chatbot prompts


- **Short name:** Create a working two-turn chatbot interface
- **Description:** Students design a UI with a text input, “Send” button, quick-reply buttons, and a scrolling label/log of the conversation. Pressing “Send” pushes the user message into a list, calls the ChatGPT block, appends the response, and keeps only the latest six turns visible.
- **Challenge format:** Coding, guided build. Starter project includes the widgets. Students add code to (1) capture input, (2) update a `conversation` list, (3) display text with timestamps, and (4) reset the input field. Auto-grading simulates chat sequences and verifies log ordering and state reset behavior.
- **CSTA:** MS-PRO-PF-02, MS-PRO-DH-04.

### T22.G6.04 – Debug off-topic responses by rewriting prompts

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G4.01: Write clear, polite questions for a helper bot
  * T22.G5.01: Flag risky vs safe chatbot prompts


- **Short name:** Diagnose why the bot gave a bad answer and fix it
- **Description:** Students investigate cases where the bot rambles, ignores instructions, or refuses to answer. They edit the system message, add clarifying phrases, or insert reminders about format, then re-run the chat to verify improvement. This introduces iterative prompting as a debugging skill.
- **Challenge format:** Coding + reflection. Learners receive three failing transcripts; for each they must (1) name the failure type, (2) show the revised prompt/system message, and (3) capture the improved response. Auto-grading checks for explicit mapping between failure and fix.
- **CSTA:** MS-PRO-TR-11.

---

## Grade 7

Grade 7 students go beyond single prompts. They craft personas with system + few-shot examples, manage conversation context, capture user slots via widgets, and build guardrails that moderate input/output before escalating to a human helper.

### T22.G7.01 – Author a persona using system messages and few-shot turns

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G6.04: Debug off-topic responses by rewriting prompts


- **Short name:** Use examples to lock in chatbot tone
- **Description:** Students design a character brief (e.g., “sarcastic space tour guide”) and write a system message plus 2–3 example exchanges that model the expected voice. They embed these in the ChatGPT block (system request + prompt prefix) so the bot stays in character across turns.
- **Challenge format:** Coding + writing. Students submit the persona brief, example dialogue, and a transcript showing the bot staying on voice for five user questions. Auto-grading checks that the transcript reflects the specified tone and that example turns are present in the code.
- **CSTA:** MS-PRO-PF-02, MS-ALG-HD-04.

### T22.G7.02 – Manage chat history and reset logic

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G6.03: Build a basic chat UI with send button and log
  * T22.G6.04: Debug off-topic responses by rewriting prompts


- **Short name:** Control context windows with session types
- **Description:** Students practice when to continue a conversation versus start “new chat.” They add buttons such as “Ask follow-up” (continue session) and “Start new topic” (new session), and they implement a summary label that tells the user what context is currently active.
- **Challenge format:** Coding, state-management task. Starter project has two buttons; students complete scripts that switch the ChatGPT block’s session mode, store recent prompts in a list, and surface the active summary. Auto-grading triggers buttons in different orders to ensure context resets happen at the right times.
- **CSTA:** MS-PRO-PD-08, MS-PRO-DH-04.

### T22.G7.03 – Capture slot values through UI widgets and inject them into prompts

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G6.04: Debug off-topic responses by rewriting prompts


- **Short name:** Build a structured form-driven chatbot
- **Description:** Students create widgets (dropdowns, sliders, toggles) that gather key facts (age range, preferred topic, mood). Before contacting ChatGPT, they assemble those slots into the prompt, ensuring the bot answers with personalized tips or stories.
- **Challenge format:** Coding, UX + logic. Learners wire widget changes to variables, show the user a “current profile” summary, and only enable “Chat” once mandatory slots are filled. Auto-grading manipulates widget values and checks that prompts include them in the correct format and that the UI disables/enables at the right time.
- **CSTA:** MS-PRO-PF-02, MS-ALG-HD-03.

### T22.G7.04 – Add moderation guardrails and escalation paths

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G6.03: Build a basic chat UI with send button and log
  * T22.G6.04: Debug off-topic responses by rewriting prompts


- **Short name:** Keep chats safe with filters and fallback scripts
- **Description:** Students integrate the `get moderation result` block on both user input and bot output. If a message fails, the chatbot responds with a pre-written supportive message, logs the incident, and offers to connect the user with a human helper. This meets AI4K12 priorities around responsible deployment.
- **Challenge format:** Coding + testing. Learners implement guardrail logic, an incident counter, and a visible indicator (e.g., “Content filtered”). Auto-grading feeds safe and unsafe inputs to ensure moderation triggers correctly and that escalation messages do not call the LLM again.
- **CSTA:** MS-PRO-TR-12, MS-CAS-ET-06.

### T22.G7.05 – User-test the chatbot for inclusivity and clarity

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G6.04: Debug off-topic responses by rewriting prompts


- **Short name:** Evaluate how different users experience the bot
- **Description:** Students prepare at least four tester personas (age, language level, accessibility need), run scripted conversations, and note where the bot confuses or excludes users. They adjust prompts or UI affordances (e.g., add a “simplify answer” button) and document changes.
- **Challenge format:** Concept + evidence. Learners submit their persona table, transcripts, identified issues, and fixes. Auto-grading uses a rubric to confirm coverage of all personas and that each change ties to observed evidence.
- **CSTA:** MS-CAS-ET-05, MS-PRO-TR-13.

---

## Grade 8

Grade 8 students build production-grade assistants. They connect LLMs to curated knowledge bases, orchestrate multi-agent conversations, parse structured outputs to trigger tools, and publish operations manuals that explain handoffs between AI and humans.

### T22.G8.01 – Add retrieval-augmented generation (RAG) to a chatbot

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G7.04: Add moderation guardrails and escalation paths


- **Short name:** Answer questions with a semantic knowledge base
- **Description:** Students import curriculum notes into a table, build a Pinecone semantic index (`create semantic database from table [...]`), and before each ChatGPT call they run `search semantic database with [QUERY]` to fetch the top facts. They prepend the retrieved snippets to the prompt so answers stay grounded.
- **Challenge format:** Coding, data integration project. Starter data includes a sample unit. Students finish the pipeline so that user questions trigger retrieval, display cited snippets, and highlight when no match is found. Auto-grading asks factual questions and checks that outputs quote specific table rows.
- **CSTA:** MS-PRO-DH-04, MS-CAS-ET-07.

### T22.G8.02 – Coordinate multi-agent conversations and summaries

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G7.04: Add moderation guardrails and escalation paths
  * T22.G7.05: User-test the chatbot for inclusivity and clarity


- **Short name:** Run two ChatGPT personas in a debate with a moderator
- **Description:** Students spin up two sessions (e.g., historian vs. scientist) and a third “moderator” script that alternates turns, enforces time limits, and summarizes agreements for the user. This mirrors advanced creative AI use cases described in CreatiCode modules.
- **Challenge format:** Coding, concurrency simulation. Learners implement session IDs, schedule turns via broadcasts, and push each response into labeled logs before producing a final summary for the user. Auto-grading checks that agents alternate correctly and that the summary references points from both sides.
- **CSTA:** MS-PRO-PD-08, MS-ALG-HD-04.

### T22.G8.03 – Parse structured chatbot outputs to trigger tools

_Dependency:_
  * T03.G3.01: Identify features in a small game description
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G7.04: Add moderation guardrails and escalation paths


- **Short name:** Let the bot pick an action and run Scratch code
- **Description:** Students instruct ChatGPT to answer in a JSON-like format (e.g., `{"action":"schedule","details":"..."}`). Their script parses the response and routes to helper blocks: calculator, table lookup, or calendar writer. They add confirmations so the user sees exactly what the bot executed.
- **Challenge format:** Coding, tool-use scenario. Starter code includes sample helper blocks. Students add parsing logic, validation, and fallback when the bot returns invalid JSON. Auto-grading feeds responses to ensure that each action triggers the right helper and that malformed data is gracefully handled.
- **CSTA:** MS-PRO-PF-02, MS-PRO-TR-12.

### T22.G8.04 – Publish a chatbot operations manual

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T22.G7.04: Add moderation guardrails and escalation paths


- **Short name:** Document policies, limits, and human handoffs
- **Description:** Students combine everything learned to author a concise manual covering: purpose, data sources, guardrails, escalation steps, maintenance checklist, and responsible-use statements. They reference evidence from their logs (e.g., “Week 3: 2 moderation events, both escalated”).
- **Challenge format:** Concept, technical writing. Learners submit a manual and a quick video or slide walkthrough. Auto-grading rubric checks for required sections, references to actual telemetry, and clear expectations for future maintainers.
- **CSTA:** MS-CAS-HC-02, MS-PRO-PM-03.

---
