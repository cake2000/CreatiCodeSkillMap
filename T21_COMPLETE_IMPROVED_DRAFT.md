# T21 – Chatbots & Prompting (IMPROVED DRAFT)
## Total Skills: 118 (up from 91)

---

## MAJOR IMPROVEMENTS SUMMARY

### 1. K-2 ENHANCEMENTS (Picture-based, Auto-gradable)
- **NEW: Prompt Parts Framework** (T21.GK.01-03, T21.G1.01-02, T21.G2.01-02)
  - Visual decomposition: WHO (agent), WHAT (task), HOW (style/constraints)
  - Matching exercises before coding
  - Foundation for later RCTF framework

- **NEW: Tracing & Prediction Ladder** (T21.GK.04-05, T21.G1.03-04, T21.G2.03-05)
  - "What will chatbot say?" prediction exercises
  - Multi-turn conversation tracing
  - Error prediction at picture level

- **NEW: Safety Awareness** (T21.G1.06, T21.G2.07-08)
  - Privacy basics (what NOT to share)
  - Recognizing bot vs. human
  - Safe/unsafe prompt identification

### 2. G3-G4 BRIDGE SKILLS (Unplugged-to-Coding Transition)
- **NEW: RCTF Framework Introduction** (T21.G3.01-03, T21.G4.01-02)
  - Role, Context, Task, Format taught systematically
  - Sub-skills for each component
  - Tracing before building

- **NEW: Debugging Foundations** (T21.G3.08-09, T21.G4.09-10)
  - "Prompt doesn't work" diagnostic process
  - Compare expected vs. actual output
  - Iterative refinement patterns

- **NEW: Multi-turn Conversation Logic** (T21.G3.06-07, T21.G4.06-08)
  - Context preservation understanding
  - Turn-taking patterns
  - State tracking basics

### 3. G5-G6 TECHNICAL DEPTH (Parameters & Testing)
- **NEW: Parameter Learning Progression** (T21.G5.04-07, T21.G6.05-08)
  - Temperature: sub-skills for creative vs. deterministic
  - Max tokens: planning response length
  - Stop sequences: structured output control
  - Frequency/presence penalties: variation control

- **NEW: Testing Methodologies** (T21.G5.10-11, T21.G6.11-13)
  - Test case design for prompts
  - Edge case identification
  - Regression testing for prompt changes
  - A/B testing different prompt versions

- **NEW: Voice/Multimodal** (T21.G5.12-13, T21.G6.14-15)
  - Voice input/output integration
  - Image-based prompting basics
  - Cross-modal consistency

### 4. G7-G8 ADVANCED PATTERNS (Agentic AI & Production)
- **NEW: Agentic AI Patterns** (T21.G7.11-14, T21.G8.14-17)
  - Tool-use orchestration (T21.G7.11-12)
  - Multi-agent collaboration (T21.G8.14-15)
  - ReAct pattern (Reasoning + Acting) (T21.G8.16)
  - Self-correction loops (T21.G8.17)

- **NEW: Production Deployment** (T21.G7.17-18, T21.G8.18-20)
  - Rate limiting & error handling (T21.G7.17)
  - Cost monitoring (T21.G7.18)
  - Prompt versioning (T21.G8.18)
  - Fallback strategies (T21.G8.19)
  - Human-in-the-loop workflows (T21.G8.20)

- **NEW: Advanced Debugging** (T21.G7.15-16, T21.G8.11-13)
  - Systematic prompt analysis frameworks
  - Bias detection and mitigation
  - Hallucination prevention strategies
  - Logging and observability

### 5. NEW CROSS-CUTTING THEMES

#### A. PROMPT DEBUGGING PROGRESSION (GK→G8)
- GK: Identify picture where bot fails
- G1-G2: Predict errors, match fixes
- G3-G4: Compare expected vs. actual, iterative fixes
- G5-G6: Systematic test cases, edge cases
- G7-G8: Bias detection, hallucination prevention, production debugging

#### B. AI LITERACY DEPTH
- K-2: "Bot follows rules" mental model
- G3-G4: "Pattern matching" introduction
- G5-G6: Token prediction, probability basics
- G7-G8: Limitations, bias sources, training data impact

#### C. SAFETY & ETHICS LADDER
- K-2: Privacy basics, bot recognition
- G3-G4: Appropriate use cases, citation needs
- G5-G6: Bias awareness, fact-checking
- G7-G8: Misuse prevention, ethical deployment, societal impact

#### D. TESTING & EVALUATION
- G3-G4: Manual output checking
- G5-G6: Test case design, regression testing
- G7-G8: Automated evaluation, metrics, A/B testing

#### E. HUMAN-AI COLLABORATION
- G3-G4: "AI as helper" workflows
- G5-G6: "AI as co-pilot" patterns
- G7-G8: "AI as agent" orchestration, oversight

---

## SKILL DISTRIBUTION BY GRADE
- GK: 7 skills (picture-based)
- G1: 7 skills (picture-based)
- G2: 8 skills (picture-based, intro simple code)
- G3: 12 skills (unplugged-to-code bridge)
- G4: 13 skills (basic coding, RCTF framework)
- G5: 14 skills (parameters, testing)
- G6: 16 skills (advanced parameters, multimodal)
- G7: 19 skills (agentic patterns, production basics)
- G8: 22 skills (advanced agentic, production deployment)
- **TOTAL: 118 skills**

---

## COMPLETE SKILL LISTING

---

### KINDERGARTEN (7 skills) - Picture-Based Only

**T21.GK.01**
- Topic: T21 – Chatbots & Prompting
- Skill: Match pictures of people talking to chatbot icons responding
- Description: Students match simple illustrated prompts (e.g., "Tell me a joke") with corresponding chatbot response pictures (e.g., chatbot displaying joke text). Develops understanding that chatbots respond to human input. Purely visual matching activity with 4-6 pairs. Auto-gradable through correct pair identification.
- Dependencies: None

**T21.GK.02**
- Topic: T21 – Chatbots & Prompting
- Skill: Sort picture cards into "Good Prompts" vs "Unclear Prompts" categories
- Description: Students drag illustrated prompt examples into two bins: clear prompts (showing specific request with details) vs unclear prompts (vague or missing information). For example, "Draw a red circle" (clear) vs "Draw something" (unclear). 6-8 cards total. Introduces prompt clarity concept visually. Auto-gradable.
- Dependencies: T21.GK.01

**T21.GK.03**
- Topic: T21 – Chatbots & Prompting
- Skill: Identify the WHO (agent type) in picture-based prompts
- Description: Students look at illustrated scenarios and circle/tap the agent type (helper bot, teacher bot, artist bot, storyteller bot) that matches the task shown. Example: Picture shows "paint a picture" task → student taps artist bot. 5-6 scenarios. Introduces WHO component of prompt framework visually. Auto-gradable.
- Dependencies: T21.GK.02

**T21.GK.04**
- Topic: T21 – Chatbots & Prompting
- Skill: Predict which picture shows what chatbot will say next
- Description: Students see a simple illustrated conversation (1-2 turns) and choose from 3 picture options showing what the chatbot will respond next. Example: Human says "What color is the sky?" → students choose picture of bot saying "Blue." 4-5 prediction tasks. Develops response prediction skills. Auto-gradable.
- Dependencies: T21.GK.03

**T21.GK.05**
- Topic: T21 – Chatbots & Prompting
- Skill: Trace a 2-turn picture conversation showing prompt and response
- Description: Students follow arrows in an illustrated 2-turn conversation flowchart, dragging pictures into correct sequence: Human asks → Bot responds → Human asks again → Bot responds. 2-3 conversation sequences to trace. Introduces multi-turn concept visually. Auto-gradable through sequence verification.
- Dependencies: T21.GK.04

**T21.GK.06**
- Topic: T21 – Chatbots & Prompting
- Skill: Match helper bot types to their job pictures
- Description: Students match different chatbot character illustrations (weather bot, math bot, story bot, music bot) to pictures showing what they do (weather forecast, math problem, book, musical notes). 4-5 bot types. Develops understanding that different bots have different purposes. Auto-gradable.
- Dependencies: T21.GK.03

**T21.GK.07**
- Topic: T21 – Chatbots & Prompting
- Skill: Choose the picture showing a safe vs unsafe thing to tell a chatbot
- Description: Students view pairs of illustrated scenarios and tap the safe option: sharing favorite color (safe) vs sharing home address (unsafe), asking for game help (safe) vs sharing password (unsafe). 4 pairs. Introduces privacy basics visually. Auto-gradable.
- Dependencies: T21.GK.06

---

### GRADE 1 (7 skills) - Picture-Based Only

**T21.G1.01**
- Topic: T21 – Chatbots & Prompting
- Skill: Identify WHAT (task) and HOW (style) parts in picture prompts
- Description: Students examine illustrated prompts decomposed into parts and drag labels "WHAT" and "HOW" to correct sections. Example: "Draw [WHAT: a cat] [HOW: with stripes]" shown as pictures. 5-6 prompts. Extends prompt parts framework from GK. Auto-gradable.
- Dependencies: T21.GK.03

**T21.G1.02**
- Topic: T21 – Chatbots & Prompting
- Skill: Build a complete picture prompt by dragging WHO, WHAT, HOW cards together
- Description: Students construct prompts by dragging 3 illustrated cards into sequence: WHO card (bot type), WHAT card (task), HOW card (style/detail). Example: [Artist bot] + [draw house] + [with red roof]. 4-5 prompt construction tasks. Auto-gradable through correct card sequence.
- Dependencies: T21.G1.01

**T21.G1.03**
- Topic: T21 – Chatbots & Prompting
- Skill: Trace a 3-turn picture conversation with branching paths
- Description: Students follow a more complex illustrated conversation flowchart with one decision point: Human asks → Bot responds → Human chooses path A or B → Bot gives different response based on choice. 2-3 conversation traces. Introduces conditional responses visually. Auto-gradable.
- Dependencies: T21.GK.05

**T21.G1.04**
- Topic: T21 – Chatbots & Prompting
- Skill: Predict what happens when a prompt is missing WHAT or HOW parts
- Description: Students view incomplete illustrated prompts (missing task or missing details) and choose from 3 picture outcomes showing bot confusion, wrong output, or asking for clarification. 5-6 scenarios. Develops understanding that incomplete prompts cause problems. Auto-gradable.
- Dependencies: T21.G1.02

**T21.G1.05**
- Topic: T21 – Chatbots & Prompting
- Skill: Sort picture cards showing bot responses into "Correct" vs "Wrong" for given prompts
- Description: Students see an illustrated prompt and sort 4-6 response pictures into correct/incorrect bins. Example: Prompt "Draw a big tree" → correct responses show large trees, incorrect show small trees or non-trees. Develops evaluation skills. Auto-gradable.
- Dependencies: T21.G1.04

**T21.G1.06**
- Topic: T21 – Chatbots & Prompting
- Skill: Match pictures showing real people vs chatbots in conversations
- Description: Students identify whether illustrated conversation partners are humans or bots by visual cues (screen interface vs face, text responses vs speech bubbles, bot icons). 6-8 identification tasks. Develops bot recognition skills for safety. Auto-gradable.
- Dependencies: T21.GK.07

**T21.G1.07**
- Topic: T21 – Chatbots & Prompting
- Skill: Choose the better prompt from two picture options for the same task
- Description: Students compare two illustrated prompts for the same goal and tap the clearer/more specific one. Example: "Make something fun" vs "Make a puzzle game with animals" for same desired output. 5-6 comparison pairs. Develops prompt quality judgment. Auto-gradable.
- Dependencies: T21.G1.05

---

### GRADE 2 (8 skills) - Picture-Based, Introduction to Simple Code

**T21.G2.01**
- Topic: T21 – Chatbots & Prompting
- Skill: Decompose picture prompts into Role, Task, and Format components
- Description: Students analyze illustrated prompts and drag labels for three components: ROLE (who the bot pretends to be), TASK (what to do), FORMAT (how to present answer). Example: [ROLE: Teacher] [TASK: Explain addition] [FORMAT: With pictures]. 5-6 decomposition exercises. Introduces RCTF framework visually. Auto-gradable.
- Dependencies: T21.G1.01, T21.G1.02

**T21.G2.02**
- Topic: T21 – Chatbots & Prompting
- Skill: Build complete picture prompts using Role, Task, Format cards
- Description: Students construct more complex prompts by sequencing illustrated ROLE + TASK + FORMAT cards. Example: [Scientist role] + [Explain weather] + [Use simple words]. 4-5 construction tasks with verification. Extends RCTF framework practice. Auto-gradable.
- Dependencies: T21.G2.01

**T21.G2.03**
- Topic: T21 – Chatbots & Prompting
- Skill: Trace a 4-turn picture conversation showing context building
- Description: Students follow illustrated multi-turn conversations where bot remembers previous context: Turn 1 establishes topic, Turn 2-4 build on it. Example: "Tell me about dogs" → "What do they eat?" → bot answers using dog context. 2-3 traces. Auto-gradable through sequence verification.
- Dependencies: T21.G1.03

**T21.G2.04**
- Topic: T21 – Chatbots & Prompting
- Skill: Predict bot behavior when context changes mid-conversation (picture-based)
- Description: Students view illustrated conversations where topic shifts occur and predict from 3 picture options how bot will respond: continue old topic (wrong), ask for clarification (good), or start new topic (good). 5-6 scenarios. Develops context awareness. Auto-gradable.
- Dependencies: T21.G2.03

**T21.G2.05**
- Topic: T21 – Chatbots & Prompting
- Skill: Identify which picture shows the error when bot gives wrong answer
- Description: Students see prompt + incorrect bot response in pictures and choose which part of the prompt caused the error from 3 illustrated options (unclear task, wrong details, missing information). 5-6 debugging scenarios. Introduces error analysis visually. Auto-gradable.
- Dependencies: T21.G1.05

**T21.G2.06**
- Topic: T21 – Chatbots & Prompting
- Skill: Match simple text prompts to their visual outcomes
- Description: Bridge to coding: Students match 5-6 short text prompts (1 sentence each, in visual speech bubbles) to illustrated bot response outcomes. Example: Text "Draw a sun" matches picture of sun drawing. Transitions from pure pictures to text-picture connection. Auto-gradable.
- Dependencies: T21.G2.02

**T21.G2.07**
- Topic: T21 – Chatbots & Prompting
- Skill: Sort picture scenarios into safe vs unsafe chatbot uses
- Description: Students categorize 6-8 illustrated scenarios: safe uses (homework help, learning games, creative stories) vs unsafe (sharing personal info, believing everything bot says, using for cheating). Extends privacy/safety awareness. Auto-gradable.
- Dependencies: T21.G1.06

**T21.G2.08**
- Topic: T21 – Chatbots & Prompting
- Skill: Identify pictures showing when to ask a human instead of a chatbot
- Description: Students view 6-8 illustrated situations and tap those requiring human help rather than bot help: medical emergency, feeling sad, complex math homework explanation, stranger danger. Develops appropriate use judgment. Auto-gradable.
- Dependencies: T21.G2.07

---

### GRADE 3 (12 skills) - Unplugged-to-Coding Bridge

**T21.G3.01**
- Topic: T21 – Chatbots & Prompting
- Skill: Trace how a simple text prompt flows through a chatbot system diagram
- Description: Students follow a system diagram showing: User input → Prompt processing → Pattern matching → Response generation → Output. They label each stage and trace a sample prompt through. Uses simplified flowchart with 4-5 stages. Unplugged activity introducing bot internals conceptually.
- Dependencies: T21.G2.06

**T21.G3.02**
- Topic: T21 – Chatbots & Prompting
- Skill: Create a one-sentence text prompt with Role and Task components
- Description: Students write their first coded prompts using a fill-in-template: "You are a [ROLE]. [TASK]." Example: "You are a math tutor. Explain what addition means." 3-4 prompts created with verification against rubric. Introduces RCTF systematically in code.
- Dependencies: T21.G2.01, T21.G2.02

**T21.G3.03**
- Topic: T21 – Chatbots & Prompting
- Skill: Add Context and Format components to expand a basic prompt
- Description: Students enhance their T21.G3.02 prompts by adding context and format: "You are a [ROLE]. [CONTEXT]. [TASK]. [FORMAT]." Example: "You are a science teacher. I am 8 years old. Explain photosynthesis. Use simple words and one example." 3-4 expanded prompts. Completes basic RCTF framework.
- Dependencies: T21.G3.02

**T21.G3.03.01** (Sub-skill)
- Topic: T21 – Chatbots & Prompting
- Skill: Identify which RCTF component is missing in incomplete prompts
- Description: Students analyze 5-6 incomplete prompts and label which component (Role, Context, Task, or Format) is missing or weak. Diagnostic skill supporting T21.G3.03. Helps students understand each component's necessity.
- Dependencies: T21.G3.03

**T21.G3.04**
- Topic: T21 – Chatbots & Prompting
- Skill: Create a simple chatbot that responds to one specific keyword
- Description: Students build their first chatbot using if-then logic: IF user input contains "hello" THEN respond "Hi there!" Implements 2-3 keyword-response pairs. Introduces conditional response logic in code (block-based or simple text).
- Dependencies: T21.G3.01

**T21.G3.05**
- Topic: T21 – Chatbots & Prompting
- Skill: Predict chatbot response for 3-4 different user inputs to same bot
- Description: Students analyze a chatbot's rules/prompts and predict responses for various inputs without running code. Example: Given bot with prompt "You are helpful and polite," predict responses to "Help me" vs "Go away" vs "What's 2+2?" Develops mental modeling.
- Dependencies: T21.G3.04

**T21.G3.06**
- Topic: T21 – Chatbots & Prompting
- Skill: Trace a 3-turn conversation showing how context is preserved
- Description: Students trace through code/pseudocode showing conversation history being stored and passed to bot each turn. They identify where previous context appears in each new prompt. Introduces context/memory concept in code form.
- Dependencies: T21.G3.05

**T21.G3.07**
- Topic: T21 – Chatbots & Prompting
- Skill: Build a 2-turn chatbot conversation with context from turn 1 used in turn 2
- Description: Students implement a simple multi-turn bot where turn 2 response depends on turn 1 input. Example: Turn 1: "My name is Alex" → Turn 2: "What do you like?" → Bot responds "Nice to meet you, Alex. What do you like?" Implements basic context passing.
- Dependencies: T21.G3.06

**T21.G3.08**
- Topic: T21 – Chatbots & Prompting
- Skill: Compare expected vs actual chatbot output to identify prompt problems
- Description: Students write down expected output for a prompt, run it, compare actual output, and identify differences. They document: What I expected, What I got, Why different. 3-4 comparison exercises. Introduces systematic debugging process.
- Dependencies: T21.G3.05

**T21.G3.09**
- Topic: T21 – Chatbots & Prompting
- Skill: Fix a broken prompt by adding missing details or correcting vague language
- Description: Students debug 3-4 prompts that produce wrong/unclear outputs by: identifying the problem (missing info, vague wording, wrong role), making one targeted fix, testing again. Iterative refinement practice. Builds on T21.G3.08 comparison skills.
- Dependencies: T21.G3.08

**T21.G3.10**
- Topic: T21 – Chatbots & Prompting
- Skill: Create chatbot responses for 3 different user moods (happy, sad, confused)
- Description: Students implement conditional logic to detect mood keywords and respond appropriately: happy input → encouraging response, sad input → comforting response, confused input → clarifying response. Introduces sentiment-aware responses.
- Dependencies: T21.G3.04

**T21.G3.11**
- Topic: T21 – Chatbots & Prompting
- Skill: Identify which prompts ask the chatbot to do harmful or inappropriate things
- Description: Students review 6-8 prompts and categorize them: appropriate (educational, creative, helpful) vs inappropriate (harmful instructions, personal info requests, cheating, generating mean content). Develops ethical use awareness.
- Dependencies: T21.G3.03

**T21.G3.12**
- Topic: T21 – Chatbots & Prompting
- Skill: Design a chatbot personality by choosing role, tone, and sample responses
- Description: Students create a chatbot character profile: select role (tutor, friend, guide), define tone (formal, casual, encouraging), write 3 sample responses demonstrating personality consistency. Introduces personality design thinking.
- Dependencies: T21.G3.03, T21.G3.10

---

### GRADE 4 (13 skills) - Basic Coding with RCTF Framework

**T21.G4.01**
- Topic: T21 – Chatbots & Prompting
- Skill: Trace how different RCTF components change chatbot behavior
- Description: Students analyze 4-5 prompts where only one RCTF component changes each time and trace how output differs. Example: Same task with different roles (teacher vs comedian) produces different tones. Documents component impact systematically.
- Dependencies: T21.G3.03

**T21.G4.02**
- Topic: T21 – Chatbots & Prompting
- Skill: Build prompts using RCTF framework for 3 different scenarios
- Description: Students create complete RCTF prompts for distinct use cases: educational (tutoring), creative (story writing), practical (task planning). Each must have all 4 components clearly defined. Demonstrates framework versatility.
- Dependencies: T21.G4.01

**T21.G4.02.01** (Sub-skill)
- Topic: T21 – Chatbots & Prompting
- Skill: Optimize each RCTF component to improve prompt clarity
- Description: Students take a working RCTF prompt and iteratively improve each component: make role more specific, add relevant context, clarify task, detail format requirements. Compare outputs before/after optimization.
- Dependencies: T21.G4.02

**T21.G4.03**
- Topic: T21 – Chatbots & Prompting
- Skill: Create a chatbot with 4-5 different response patterns using if-then logic
- Description: Students build a more complex rule-based chatbot handling multiple input types: greetings, questions, commands, farewells, unknown input. Each type has appropriate response pattern. Extends conditional response complexity.
- Dependencies: T21.G3.04, T21.G3.10

**T21.G4.04**
- Topic: T21 – Chatbots & Prompting
- Skill: Test chatbot with 5+ diverse inputs and document which ones fail
- Description: Students create a test plan with varied inputs (expected cases, edge cases, unusual inputs), run tests, document results in table: Input | Expected Output | Actual Output | Pass/Fail. Introduces systematic testing.
- Dependencies: T21.G4.03

**T21.G4.05**
- Topic: T21 – Chatbots & Prompting
- Skill: Parse user input to extract key information (name, number, topic)
- Description: Students implement input parsing to extract data from user messages: "My name is Jamie" → extract "Jamie", "I want 5 apples" → extract "5" and "apples". Store extracted data for later use. Introduces data extraction from natural language.
- Dependencies: T21.G4.03

**T21.G4.06**
- Topic: T21 – Chatbots & Prompting
- Skill: Build a 3-turn conversation where bot remembers 2 pieces of information
- Description: Students create multi-turn bot that stores and uses user data: Turn 1 asks name (stores), Turn 2 asks favorite color (stores), Turn 3 uses both in response: "Hi [name], I remember you like [color]!" Develops state management.
- Dependencies: T21.G3.07, T21.G4.05

**T21.G4.07**
- Topic: T21 – Chatbots & Prompting
- Skill: Trace conversation flow through a 4-turn branching dialogue tree
- Description: Students trace through a visual or code-based dialogue tree where user choices at turn 2 determine paths for turns 3-4. Map all possible conversation paths. Introduces complex conversation logic.
- Dependencies: T21.G3.06

**T21.G4.08**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement a branching conversation with 2 choice points
- Description: Students build a dialogue tree with user choices that branch: Opening → Choice A or B → Different follow-up → Choice C or D → Different endings. 4+ distinct paths possible. Implements branching conversation structure.
- Dependencies: T21.G4.07

**T21.G4.09**
- Topic: T21 – Chatbots & Prompting
- Skill: Debug a prompt by testing one RCTF component change at a time
- Description: Students use isolation debugging: if output is wrong, test by changing only Role (keep RCTF same), then only Context, etc. Document which component fixes issue. Teaches systematic debugging methodology.
- Dependencies: T21.G3.09, T21.G4.01

**T21.G4.10**
- Topic: T21 – Chatbots & Prompting
- Skill: Create test cases for chatbot covering normal, edge, and error inputs
- Description: Students design comprehensive test suite: normal cases (expected inputs), edge cases (boundary values, extremes), error cases (invalid input, empty input). 8-10 test cases minimum. Formalizes testing practice.
- Dependencies: T21.G4.04

**T21.G4.11**
- Topic: T21 – Chatbots & Prompting
- Skill: Compare two different prompts for the same task and evaluate quality
- Description: Students write two alternative prompts for identical goal, test both, compare outputs using rubric: accuracy, clarity, completeness, appropriateness. Select better prompt with justification. Develops evaluative judgment.
- Dependencies: T21.G4.02

**T21.G4.12**
- Topic: T21 – Chatbots & Prompting
- Skill: Identify when chatbot output contains incorrect or made-up information
- Description: Students test prompts asking for factual information, verify outputs against trusted sources, identify "hallucinations" (incorrect facts presented confidently). Document 3-4 examples. Introduces hallucination awareness.
- Dependencies: T21.G4.04

**T21.G4.13**
- Topic: T21 – Chatbots & Prompting
- Skill: Design a chatbot for a specific audience (young children, teenagers, adults)
- Description: Students create audience-appropriate chatbot by adjusting: language complexity, tone, examples used, interaction style. Test with sample inputs from target audience. Demonstrates audience-aware design.
- Dependencies: T21.G3.12, T21.G4.02

---

### GRADE 5 (14 skills) - Parameters & Testing Methodologies

**T21.G5.01**
- Topic: T21 – Chatbots & Prompting
- Skill: Trace how the same prompt with different parameters produces different outputs
- Description: Students run identical prompt with varying temperature (0.0, 0.5, 1.0) and document output differences. Analyze: low temperature → consistent/focused, high temperature → creative/varied. 3-4 parameter experiments with analysis.
- Dependencies: T21.G4.02

**T21.G5.02**
- Topic: T21 – Chatbots & Prompting
- Skill: Predict output characteristics based on parameter settings
- Description: Students examine parameter configurations (temperature, max tokens) and predict output features before running: will output be creative or deterministic? Long or short? Varied or consistent? 5-6 prediction exercises. Develops parameter intuition.
- Dependencies: T21.G5.01

**T21.G5.03**
- Topic: T21 – Chatbots & Prompting
- Skill: Design a complex multi-turn chatbot implementing RCTF in system prompt
- Description: Students create sophisticated bot with: detailed system prompt using full RCTF framework, conversation memory, consistent personality across turns, ability to handle 5+ turn conversations. Tests conversation coherence.
- Dependencies: T21.G4.06, T21.G4.08

**T21.G5.04**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement temperature parameter to control creative vs deterministic outputs
- Description: Students build prompts with temperature control: creative tasks (story writing) use high temperature (0.8-1.0), factual tasks (math) use low temperature (0.0-0.3). Test 3-4 scenarios choosing appropriate temperature with justification.
- Dependencies: T21.G5.01, T21.G5.02

**T21.G5.04.01** (Sub-skill)
- Topic: T21 – Chatbots & Prompting
- Skill: Compare outputs across temperature range to find optimal setting
- Description: Students run same prompt at 0.0, 0.3, 0.5, 0.7, 1.0 temperature, compare outputs, select optimal value for specific use case with detailed reasoning. A/B testing for temperature.
- Dependencies: T21.G5.04

**T21.G5.05**
- Topic: T21 – Chatbots & Prompting
- Skill: Use max tokens parameter to plan and control response length
- Description: Students set max tokens based on desired output: short answer (50 tokens), paragraph (150 tokens), essay (500 tokens). Test 3-4 scenarios, verify outputs fit length requirements. Introduces token-based planning.
- Dependencies: T21.G5.02

**T21.G5.06**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement stop sequences to create structured output formats
- Description: Students use stop sequences to control output structure: stop at newline for single-line outputs, stop at delimiter for list items, stop at marker for sections. Create 3 structured output formats (list, table, sections).
- Dependencies: T21.G5.05

**T21.G5.07**
- Topic: T21 – Chatbots & Prompting
- Skill: Apply frequency and presence penalties to control output variety
- Description: Students experiment with frequency penalty (reduce repetition) and presence penalty (encourage new topics): test prompts with/without penalties, document impact on vocabulary diversity and topic coverage. 3-4 experiments.
- Dependencies: T21.G5.04

**T21.G5.08**
- Topic: T21 – Chatbots & Prompting
- Skill: Parse and extract structured data from chatbot responses (JSON, lists)
- Description: Students design prompts requesting structured output (JSON format, numbered lists, tables), implement parsing code to extract data programmatically, store in variables. Creates 2-3 structured data extraction pipelines.
- Dependencies: T21.G4.05, T21.G5.06

**T21.G5.09**
- Topic: T21 – Chatbots & Prompting
- Skill: Chain two chatbot calls where output of first becomes input to second
- Description: Students implement prompt chaining: Call 1 generates content → extract result → use as input to Call 2 → final output. Example: Call 1 writes story outline → Call 2 expands outline into full story. Introduces composition patterns.
- Dependencies: T21.G5.08

**T21.G5.10**
- Topic: T21 – Chatbots & Prompting
- Skill: Design systematic test cases covering diverse prompt scenarios
- Description: Students create comprehensive test plan: vary RCTF components, vary parameters, vary user inputs, vary conversation length. Minimum 15 test cases covering normal, edge, and error conditions. Formalizes test design methodology.
- Dependencies: T21.G4.10

**T21.G5.11**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement regression testing when modifying prompts
- Description: Students establish baseline outputs for test cases, modify prompt, re-run tests, compare to baseline. Document: improvements, regressions, side effects. Ensures changes don't break existing functionality. 3-4 modification cycles.
- Dependencies: T21.G5.10

**T21.G5.12**
- Topic: T21 – Chatbots & Prompting
- Skill: Integrate voice input to chatbot using speech-to-text
- Description: Students add voice input capability: capture audio → convert to text → send as prompt → receive response. Test with 3-4 voice commands. Handle speech recognition errors gracefully. Introduces multimodal input.
- Dependencies: T21.G5.03

**T21.G5.13**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement text-to-speech for chatbot responses
- Description: Students add voice output: receive chatbot text response → convert to speech → play audio. Test with different voices/speeds. Ensure appropriate voice matches bot personality. Completes voice interaction loop.
- Dependencies: T21.G5.12

---

### GRADE 6 (16 skills) - Advanced Parameters & Multimodal

**T21.G6.01**
- Topic: T21 – Chatbots & Prompting
- Skill: Analyze how parameter combinations interact to affect output quality
- Description: Students test parameter combinations systematically: temperature + max tokens, temperature + penalties, stop sequences + format instructions. Document interaction effects. 5-6 combination experiments with analysis matrix.
- Dependencies: T21.G5.04, T21.G5.05, T21.G5.07

**T21.G6.02**
- Topic: T21 – Chatbots & Prompting
- Skill: Optimize parameters for specific use cases through experimentation
- Description: Students select optimal parameter set for distinct scenarios: creative writing, factual Q&A, code generation, summarization. Test multiple configurations, measure quality, document final choices with justification. 3-4 optimization tasks.
- Dependencies: T21.G6.01

**T21.G6.03**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement few-shot learning by providing examples in prompts
- Description: Students enhance prompts with 2-4 input-output examples demonstrating desired behavior. Compare zero-shot (no examples) vs few-shot performance. Test on 3 different tasks: classification, generation, transformation. Introduces few-shot prompting.
- Dependencies: T21.G5.04

**T21.G6.03.01** (Sub-skill)
- Topic: T21 – Chatbots & Prompting
- Skill: Select effective examples for few-shot learning
- Description: Students experiment with different example types: diverse vs similar, simple vs complex, typical vs edge cases. Evaluate which example selection strategies improve output quality most. Test 3-4 example sets per task.
- Dependencies: T21.G6.03

**T21.G6.04**
- Topic: T21 – Chatbots & Prompting
- Skill: Create prompt templates with variables for reusable patterns
- Description: Students design parameterized prompt templates: "You are a {role}. {context}. {task}. Output as {format}." Implement 3-4 templates for common patterns (tutoring, content generation, analysis). Test with different variable values.
- Dependencies: T21.G5.03

**T21.G6.05**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement top-p (nucleus sampling) parameter for controlled randomness
- Description: Students experiment with top-p parameter: compare top-p=0.1 (very focused) vs top-p=0.9 (diverse) for same prompt. Understand difference from temperature. Test 3-4 scenarios documenting when top-p vs temperature is better.
- Dependencies: T21.G5.04

**T21.G6.06**
- Topic: T21 – Chatbots & Prompting
- Skill: Use logit bias to increase/decrease probability of specific tokens
- Description: Students apply logit bias to encourage/discourage specific words or phrases: bias against profanity, bias toward domain vocabulary, bias away from common phrases. Test 3 bias scenarios and verify impact on outputs.
- Dependencies: T21.G6.05

**T21.G6.07**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement best-of-n sampling to select highest quality output
- Description: Students generate n outputs (3-5) for same prompt, implement scoring criteria (relevance, accuracy, clarity), select best output programmatically. Compare single generation vs best-of-n quality improvement.
- Dependencies: T21.G6.02

**T21.G6.08**
- Topic: T21 – Chatbots & Prompting
- Skill: Chain multiple specialized prompts to accomplish complex tasks
- Description: Students build multi-stage pipeline: Stage 1 analyzes input → Stage 2 plans approach → Stage 3 executes → Stage 4 reviews/refines. Each stage has specialized prompt. Test on 2-3 complex tasks requiring decomposition.
- Dependencies: T21.G5.09

**T21.G6.09**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement conversational memory with summarization for long contexts
- Description: Students build chatbot that: stores full conversation history, summarizes older messages to save space, maintains relevant context without exceeding token limits. Test with 10+ turn conversations tracking context management.
- Dependencies: T21.G5.03, T21.G5.05

**T21.G6.10**
- Topic: T21 – Chatbots & Prompting
- Skill: Debug prompts using systematic parameter isolation
- Description: Students troubleshoot problematic outputs by isolating variables: reset all parameters to default, retest, change one parameter at a time, identify which causes issue. Document debugging process for 3-4 complex cases.
- Dependencies: T21.G4.09, T21.G6.01

**T21.G6.11**
- Topic: T21 – Chatbots & Prompting
- Skill: Design automated test suites with pass/fail criteria
- Description: Students create programmatic tests: define expected output criteria (contains keywords, matches format, within length range), run prompts, automatically score pass/fail. Build suite of 15-20 automated tests.
- Dependencies: T21.G5.10, T21.G5.11

**T21.G6.12**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement A/B testing to compare prompt variants
- Description: Students design controlled experiments: create 2 prompt versions for same goal, run each with identical inputs, measure quality metrics (accuracy, user preference, clarity), select winner with statistical reasoning. 2-3 A/B tests.
- Dependencies: T21.G6.11

**T21.G6.13**
- Topic: T21 – Chatbots & Prompting
- Skill: Create test cases for edge cases and failure modes
- Description: Students identify potential failure scenarios: very long inputs, unusual characters, contradictory instructions, ambiguous requests. Design 10+ edge case tests. Document failure patterns and mitigation strategies.
- Dependencies: T21.G6.11

**T21.G6.14**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement image-based prompting with vision-capable models
- Description: Students create prompts that include images as input: image + text question → response. Test scenarios: describe image, answer questions about image, compare images. 3-4 vision tasks. Introduces multimodal prompting.
- Dependencies: T21.G6.03

**T21.G6.15**
- Topic: T21 – Chatbots & Prompting
- Skill: Ensure consistency between voice, text, and image modalities
- Description: Students build multimodal chatbot handling all input types (voice, text, image) with consistent responses regardless of modality. Test same query via different modalities, verify output consistency. 3-4 cross-modal tests.
- Dependencies: T21.G5.13, T21.G6.14

---

### GRADE 7 (19 skills) - Agentic Patterns & Production Basics

**T21.G7.01**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement chain-of-thought prompting for complex reasoning tasks
- Description: Students design prompts requesting step-by-step reasoning: "Let's think through this step by step..." Compare chain-of-thought vs direct answer quality on math, logic, planning tasks. 3-4 reasoning scenarios.
- Dependencies: T21.G6.08

**T21.G7.02**
- Topic: T21 – Chatbots & Prompting
- Skill: Create self-consistency prompting with multiple reasoning paths
- Description: Students generate multiple chain-of-thought paths (3-5) for same problem, compare reasoning processes, select most common answer or synthesize consensus. Test on problems with clear correct answers to verify improvement.
- Dependencies: T21.G7.01

**T21.G7.03**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement tree-of-thought prompting with branching exploration
- Description: Students design prompts that explore multiple solution branches: generate options → evaluate each → expand promising paths → backtrack if needed. Build tree-of-thought for 2-3 complex problems (planning, strategy, design).
- Dependencies: T21.G7.02

**T21.G7.04**
- Topic: T21 – Chatbots & Prompting
- Skill: Parse and validate structured outputs against schemas
- Description: Students define output schemas (JSON schema, format rules), implement validation logic to verify chatbot outputs match schema, handle validation failures with retry logic. Test 3-4 structured output types (data records, API responses, configurations).
- Dependencies: T21.G5.08, T21.G6.04

**T21.G7.05**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement prompt compression to reduce token usage
- Description: Students analyze verbose prompts, compress while maintaining effectiveness: remove redundancy, use abbreviations, optimize examples. Measure token reduction and quality impact. Compress 3-4 long prompts targeting 30-50% reduction.
- Dependencies: T21.G5.05, T21.G6.09

**T21.G7.06**
- Topic: T21 – Chatbots & Prompting
- Skill: Create role-based prompts for domain expertise simulation
- Description: Students design detailed role prompts simulating expert personas: define expertise area, knowledge boundaries, communication style, reasoning approach. Test expert roles: scientist, lawyer, teacher, engineer. Evaluate domain appropriateness.
- Dependencies: T21.G6.04

**T21.G7.07**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement instruction hierarchy in prompts (system, user, context)
- Description: Students structure prompts with clear hierarchy: system-level instructions (personality, constraints), user-level instructions (specific task), context-level information (background data). Test instruction precedence and conflict resolution. 3-4 hierarchical prompts.
- Dependencies: T21.G7.06

**T21.G7.08**
- Topic: T21 – Chatbots & Prompting
- Skill: Build conversational agents with personality consistency across sessions
- Description: Students create chatbots with persistent personality: store personality profile, apply consistently across multiple conversations, track personality-appropriate responses. Test personality stability over 5+ sessions with varied topics.
- Dependencies: T21.G6.09, T21.G7.06

**T21.G7.09**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement semantic similarity search for context retrieval
- Description: Students build retrieval-augmented prompting: user query → find similar past conversations/documents → inject relevant context into prompt → generate response. Test on knowledge base of 20+ documents. Introduces RAG concepts.
- Dependencies: T21.G6.09

**T21.G7.10**
- Topic: T21 – Chatbots & Prompting
- Skill: Create prompts that handle ambiguity through clarification questions
- Description: Students design prompts that detect ambiguous input and ask targeted clarification questions before responding: identify ambiguity types (missing info, multiple interpretations), generate appropriate clarification questions. Test 5-6 ambiguous scenarios.
- Dependencies: T21.G7.07

**T21.G7.11**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement function calling for external tool integration
- Description: Students create prompts that invoke external tools: chatbot decides when to call function (calculator, search, database), formats function call, integrates result into response. Implement 3-4 tool integrations. Introduces agentic tool use.
- Dependencies: T21.G7.04

**T21.G7.11.01** (Sub-skill)
- Topic: T21 – Chatbots & Prompting
- Skill: Design function calling prompts with clear tool descriptions
- Description: Students write detailed tool descriptions for function calling: function purpose, parameters, return format, when to use. Test whether chatbot selects correct tools for various queries. 4-5 tool description refinement cycles.
- Dependencies: T21.G7.11

**T21.G7.12**
- Topic: T21 – Chatbots & Prompting
- Skill: Build tool-use orchestration with sequential tool calls
- Description: Students implement multi-tool workflows: query requires multiple tools in sequence (search → extract → calculate → format). Chatbot orchestrates tool call order and data passing between tools. 2-3 multi-tool scenarios.
- Dependencies: T21.G7.11

**T21.G7.13**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement error handling and retry logic for tool calls
- Description: Students add robustness: detect tool failures, implement retry strategies (with backoff), provide fallback responses when tools unavailable, log errors. Test error scenarios: network failures, invalid parameters, timeout.
- Dependencies: T21.G7.12

**T21.G7.14**
- Topic: T21 – Chatbots & Prompting
- Skill: Create evaluation metrics for prompt quality assessment
- Description: Students define quantitative metrics: accuracy (correct answers / total), relevance (on-topic score), completeness (required elements present), consistency (similar inputs → similar outputs). Apply metrics to 10+ prompt-output pairs.
- Dependencies: T21.G6.12

**T21.G7.15**
- Topic: T21 – Chatbots & Prompting
- Skill: Analyze prompts for potential bias in outputs
- Description: Students test prompts with demographic variations (names, genders, cultures), identify bias patterns in outputs (stereotyping, assumptions, unequal treatment), document bias sources. Test 3-4 prompts across 5+ demographic variations each.
- Dependencies: T21.G7.14

**T21.G7.16**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement bias mitigation strategies in prompt design
- Description: Students apply debiasing techniques: explicit fairness instructions, diverse examples, neutral language, demographic-agnostic phrasing. Test mitigation effectiveness by comparing biased vs debiased versions. 3-4 mitigation implementations.
- Dependencies: T21.G7.15

**T21.G7.17**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement rate limiting and error handling for production use
- Description: Students add production safeguards: rate limiting (max requests/minute), timeout handling, graceful degradation when API unavailable, user-friendly error messages. Test under load and failure conditions.
- Dependencies: T21.G7.13

**T21.G7.18**
- Topic: T21 – Chatbots & Prompting
- Skill: Monitor and log chatbot usage for cost and performance analysis
- Description: Students implement monitoring: log all requests/responses, track token usage, calculate costs, measure latency, identify expensive queries. Build dashboard showing usage patterns over time. Analyze 50+ interactions.
- Dependencies: T21.G7.17

**T21.G7.19**
- Topic: T21 – Chatbots & Prompting
- Skill: Design prompts preventing common security vulnerabilities
- Description: Students identify and prevent: prompt injection attacks (user overriding system instructions), data leakage (revealing sensitive info), jailbreaking attempts (bypassing safety). Implement defenses and test against 5+ attack patterns.
- Dependencies: T21.G7.07

---

### GRADE 8 (22 skills) - Advanced Agentic & Production Deployment

**T21.G8.01**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement meta-prompting where AI generates its own prompts
- Description: Students create meta-prompt systems: initial prompt generates task-specific prompts → execute generated prompts → refine based on results. Test recursive prompt improvement. 2-3 meta-prompting applications.
- Dependencies: T21.G7.01

**T21.G8.02**
- Topic: T21 – Chatbots & Prompting
- Skill: Design automatic prompt optimization through feedback loops
- Description: Students build prompt evolution system: run prompt → evaluate output quality → generate improved prompt variant → test → repeat. Implement fitness function for prompt quality. Track 5+ optimization iterations.
- Dependencies: T21.G8.01, T21.G7.14

**T21.G8.03**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement constitutional AI prompting with principle-based constraints
- Description: Students design prompts with embedded ethical principles: define 5+ principles (helpfulness, harmlessness, honesty), implement principle checking, revise outputs violating principles. Test principle enforcement across scenarios.
- Dependencies: T21.G7.16

**T21.G8.04**
- Topic: T21 – Chatbots & Prompting
- Skill: Create retrieval-augmented generation (RAG) systems with vector databases
- Description: Students build full RAG pipeline: chunk documents → generate embeddings → store in vector DB → retrieve relevant chunks for queries → inject into prompts → generate grounded responses. Test on knowledge base of 50+ documents.
- Dependencies: T21.G7.09

**T21.G8.05**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement hybrid search combining keyword and semantic retrieval
- Description: Students enhance RAG with hybrid search: keyword search (BM25) + semantic search (embeddings) → merge and rank results → use top-k for context. Compare hybrid vs single-method retrieval quality. Test on diverse queries.
- Dependencies: T21.G8.04

**T21.G8.06**
- Topic: T21 – Chatbots & Prompting
- Skill: Design prompt caching strategies to reduce latency and cost
- Description: Students implement caching: identify cacheable prompt components (system instructions, examples, context), cache at appropriate levels, implement cache invalidation. Measure latency and cost reduction. Test on high-volume scenarios.
- Dependencies: T21.G7.05, T21.G7.18

**T21.G8.07**
- Topic: T21 – Chatbots & Prompting
- Skill: Build streaming response handlers for real-time chat experiences
- Description: Students implement streaming: process chatbot output tokens as they arrive (not waiting for completion), display progressive responses, handle stream interruptions. Build responsive UI showing token-by-token generation. Measure UX improvement.
- Dependencies: T21.G7.17

**T21.G8.08**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement context window management for long conversations
- Description: Students handle token limit constraints: track running token count, implement sliding window (keep recent messages), summarize old context, preserve critical information. Test with 20+ turn conversations exceeding context limits.
- Dependencies: T21.G6.09, T21.G8.06

**T21.G8.09**
- Topic: T21 – Chatbots & Prompting
- Skill: Create prompt ensembles combining multiple model outputs
- Description: Students build ensemble systems: run same prompt on different models or configurations, aggregate outputs (voting, averaging, synthesis), produce final response. Compare ensemble vs single-model quality on 10+ tasks.
- Dependencies: T21.G6.07, T21.G7.02

**T21.G8.10**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement output verification with fact-checking mechanisms
- Description: Students add verification layer: generate response → extract factual claims → verify against trusted sources → flag unverified claims → regenerate if needed. Test on factual queries measuring accuracy improvement.
- Dependencies: T21.G8.04, T21.G8.05

**T21.G8.11**
- Topic: T21 – Chatbots & Prompting
- Skill: Design systematic prompt debugging workflows
- Description: Students create debugging framework: 1) Reproduce issue, 2) Isolate component (RCTF/parameters), 3) Hypothesis about cause, 4) Test fix, 5) Verify across cases, 6) Document solution. Apply framework to 5+ complex debugging scenarios.
- Dependencies: T21.G6.10, T21.G7.15

**T21.G8.12**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement hallucination detection and mitigation strategies
- Description: Students build hallucination defense: identify high-risk scenarios (rare facts, creative elaboration), request citations, verify against sources, use lower temperature, add explicit accuracy instructions. Test on 10+ hallucination-prone queries.
- Dependencies: T21.G8.10

**T21.G8.13**
- Topic: T21 – Chatbots & Prompting
- Skill: Create adversarial test suites for robustness evaluation
- Description: Students design adversarial tests: prompt injection attempts, edge cases, contradictory instructions, malformed inputs, bias triggers. Build suite of 20+ adversarial tests. Measure prompt robustness and failure modes.
- Dependencies: T21.G7.19, T21.G8.11

**T21.G8.14**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement multi-agent systems with specialized agent roles
- Description: Students build agent teams: create 3-5 specialized agents (researcher, analyst, writer, critic), define roles and communication protocols, orchestrate collaboration toward shared goal. Test on complex multi-step tasks.
- Dependencies: T21.G7.12

**T21.G8.14.01** (Sub-skill)
- Topic: T21 – Chatbots & Prompting
- Skill: Design agent communication protocols and message passing
- Description: Students define structured inter-agent communication: message format, routing rules, priority handling, conflict resolution when agents disagree. Implement and test communication layer for multi-agent system.
- Dependencies: T21.G8.14

**T21.G8.15**
- Topic: T21 – Chatbots & Prompting
- Skill: Create agent orchestration with task decomposition and delegation
- Description: Students build orchestrator agent: receives complex task → decomposes into subtasks → delegates to specialist agents → integrates results → produces final output. Test on 3+ complex multi-step problems requiring collaboration.
- Dependencies: T21.G8.14

**T21.G8.16**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement ReAct pattern (Reasoning and Acting) for agentic AI
- Description: Students create ReAct loops: Think (reason about what to do) → Act (take action/call tool) → Observe (see result) → repeat until task complete. Implement on 3+ tasks requiring tool use and multi-step reasoning.
- Dependencies: T21.G7.12, T21.G8.15

**T21.G8.17**
- Topic: T21 – Chatbots & Prompting
- Skill: Build self-correction loops where agents review and improve outputs
- Description: Students implement self-refinement: generate initial response → self-critique against criteria → regenerate improved version → repeat 2-3 cycles. Compare initial vs final quality. Test on creative and analytical tasks.
- Dependencies: T21.G8.16

**T21.G8.18**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement prompt versioning and A/B testing in production
- Description: Students build version control for prompts: track versions, deploy percentage-based rollouts, A/B test versions in production, measure metrics, promote winning version. Test version management workflow with 3+ prompt iterations.
- Dependencies: T21.G6.12, T21.G7.18

**T21.G8.19**
- Topic: T21 – Chatbots & Prompting
- Skill: Design fallback strategies for chatbot failures
- Description: Students implement graceful degradation: detect failure types (timeout, error, low-quality output), provide appropriate fallbacks (cached response, simpler prompt, human handoff, error message). Test 5+ failure scenarios with recovery paths.
- Dependencies: T21.G7.17, T21.G8.13

**T21.G8.20**
- Topic: T21 – Chatbots & Prompting
- Skill: Create human-in-the-loop workflows with review and approval gates
- Description: Students design human oversight: flag uncertain outputs for review, implement approval workflows for critical tasks, log human feedback, use feedback to improve prompts. Build 2-3 HITL workflows for high-stakes scenarios.
- Dependencies: T21.G8.17, T21.G8.19

**T21.G8.21**
- Topic: T21 – Chatbots & Prompting
- Skill: Implement comprehensive observability for production chatbot systems
- Description: Students build observability stack: structured logging (all inputs/outputs), distributed tracing (multi-step workflows), metrics dashboard (latency, cost, quality, errors), alerting on anomalies. Monitor production system handling 100+ requests.
- Dependencies: T21.G7.18, T21.G8.07

**T21.G8.22**
- Topic: T21 – Chatbots & Prompting
- Skill: Design ethical deployment frameworks for chatbot applications
- Description: Students create deployment checklist: bias testing results, safety evaluation, privacy compliance, user consent, transparency (disclose AI use), misuse prevention, incident response plan. Apply framework to 2-3 deployment scenarios with documentation.
- Dependencies: T21.G8.03, T21.G8.13, T21.G8.20

---

## DEPENDENCY VALIDATION NOTES

All dependencies follow the X-2 rule:
- Grade X skills can only depend on grades X, X-1, or X-2
- All dependencies are within T21 (intra-topic)
- Sub-skills depend on their parent skill or earlier skills
- No circular dependencies exist

## SKILL COUNT SUMMARY
- GK: 7 skills
- G1: 7 skills
- G2: 8 skills
- G3: 12 skills (includes 1 sub-skill)
- G4: 13 skills (includes 1 sub-skill)
- G5: 14 skills (includes 1 sub-skill)
- G6: 16 skills (includes 1 sub-skill)
- G7: 19 skills (includes 1 sub-skill)
- G8: 22 skills (includes 1 sub-skill)
- **TOTAL: 118 skills**

---

## KEY PEDAGOGICAL IMPROVEMENTS

### 1. **Concrete-to-Abstract Progression**
- K-2: Picture-based understanding (WHO/WHAT/HOW)
- G3-G4: RCTF framework with coding
- G5-G6: Parameter control and optimization
- G7-G8: Agentic patterns and production deployment

### 2. **Debugging Ladder (Every Grade)**
- GK-G2: Visual error identification, prediction
- G3-G4: Expected vs actual comparison, iterative fixes
- G5-G6: Systematic testing, A/B testing, regression tests
- G7-G8: Bias detection, hallucination prevention, adversarial testing

### 3. **Safety & Ethics Integration**
- Introduced at GK (privacy basics)
- Reinforced every grade with age-appropriate complexity
- Culminates in G8 ethical deployment frameworks

### 4. **Testing Methodology Progression**
- G3-G4: Manual testing, test case design
- G5-G6: Automated tests, regression testing, A/B testing
- G7-G8: Adversarial testing, production monitoring, observability

### 5. **Agentic AI Introduction**
- G7: Tool use, function calling, orchestration basics
- G8: Multi-agent systems, ReAct pattern, self-correction, HITL workflows

### 6. **Production Readiness**
- G7: Rate limiting, cost monitoring, basic deployment
- G8: Caching, streaming, versioning, fallbacks, observability, ethical deployment

---

END OF DOCUMENT
