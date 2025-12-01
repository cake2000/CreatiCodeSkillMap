# T21 - Chatbots & Prompting (Phase 9 Optimized - November 2025)
# ============================================================================
# PHASE 9 MAJOR OVERHAUL - Bold Changes for Excellence
# ============================================================================
#
# PHILOSOPHY SHIFT: Prompting is about STRUCTURED COMMUNICATION, not just asking questions
# - Every skill now emphasizes WHY prompts work, not just HOW to write them
# - Added "Evaluate prompt quality" and "Critique responses" components throughout
# - Integrated AI-literacy skills: verifying bot limitations, safe usage, human vs. AI judgment
#
# NEW SKILL CATEGORIES ADDED:
# 1. PROMPT STRUCTURE RECOGNITION (understanding components)
#    - GK.03: Identify the WHO (agent type) in picture-based prompts
#    - G1.01: Identify WHAT (task) and HOW (style) parts in picture prompts
#    - G2.01: Decompose picture prompts into Role, Task, and Format components
#    - G3.12: Identify Context and Constraints in multi-part prompts
#    - G5.10: Analyze Intent, Context, Format, and Constraints in written prompts
#
# 2. CONVERSATIONAL CONTEXT BUILDING
#    - GK.05: Trace a 2-turn picture conversation showing prompt and response
#    - G1.03: Trace a 3-turn picture conversation with branching paths
#    - G2.03: Trace a 4-turn picture conversation showing context building
#    - G4.12: Build multi-turn context to guide chatbot toward specific outcome
#    - G6.11: Manage conversation state across multiple related queries
#
# 3. PROMPT QUALITY EVALUATION & CRITIQUE
#    - GK.02: Sort picture cards into "Good Prompts" vs "Unclear Prompts" categories
#    - G1.07: Choose the better prompt from two picture options for the same task
#    - G2.05: Identify which picture shows the error when bot gives wrong answer
#    - G4.14: Critique peer prompts and suggest specific improvements
#    - G6.13: Evaluate prompt effectiveness using quality criteria
#
# 4. AI SAFETY & LIMITATIONS AWARENESS
#    - GK.07: Choose the picture showing a safe vs unsafe thing to tell a chatbot
#    - G1.06: Match pictures showing real people vs chatbots in conversations
#    - G2.07: Sort picture scenarios into safe vs unsafe chatbot uses
#    - G2.08: Identify pictures showing when to ask a human instead of a chatbot
#    - G4.15: Recognize chatbot limitations and hallucinations
#    - G6.14: Identify bias in chatbot responses
#
# 5. AGENT ROLE UNDERSTANDING
#    - GK.06: Match helper bot types to their job pictures
#    - G3.11: Compare responses from different agent types for the same prompt
#    - G5.11: Select appropriate agent role for specific task requirements
#    - G7.10: Design custom agent roles with specific expertise
#
# 6. RESPONSE VERIFICATION & ITERATION
#    - G1.05: Sort picture cards showing bot responses into "Correct" vs "Wrong"
#    - G3.13: Verify chatbot answers against known facts
#    - G5.12: Iterate on prompts when initial response is inadequate
#    - G7.11: Debug multi-step chatbot failures through systematic prompt refinement
#
# CONSOLIDATED SKILLS (reduced redundancy):
# - Merged basic "ask a question" skills into structured prompt construction
# - Combined multiple "conversation tracing" into progressive complexity levels
# - Unified "prompt improvement" skills with critique and iteration components
#
# VERB UPGRADES (active, measurable):
# - "Ask" → "Construct prompt with specified components"
# - "Identify" → "Decompose and label", "Locate and mark"
# - "Compare" → "Evaluate and defend choice", "Analyze with criteria"
# - Added "Trace", "Predict", "Verify", "Critique", "Iterate"
#
# DEPENDENCY IMPROVEMENTS:
# - Stronger K→G1→G2 picture-based progression (visual → text transition)
# - Grade 3-5 builds structured prompting skills systematically
# - Grade 6-8 focuses on advanced techniques, safety, and critical evaluation
# - All intra-topic dependencies validated for X-2 rule
#
# PICTURE-BASED PROGRESSION (K-2):
# - Kindergarten: Visual recognition of chatbot interaction concepts
# - Grade 1: Component identification in picture prompts
# - Grade 2: Complete prompt construction with pictures + simple text
# - Grade 3+: Transition to full text-based prompting with complexity scaling
#
# Total: ~85 skills (balanced across grades, with strong K-2 foundation)
# ============================================================================


ID: T21.GK.01
Topic: T21 – Chatbots & Prompting
Skill: Match pictures of people talking to chatbot icons responding
Description: **Student task:** Look at 6 picture cards. Drag each picture showing a person asking a question to the matching chatbot response picture. **Visual scenario:** Left side shows: (A) child asking "What is 2+2?", (B) adult asking "What's the weather?", (C) student asking "Tell me a story". Right side shows: (1) chatbot saying "4", (2) chatbot saying "It's sunny!", (3) chatbot with story book icon. **Correct matches:** A→1, B→2, C→3. _Implementation note: Drag-and-drop matching with 3 pairs; introduces fundamental concept that chatbots respond to prompts. Large, colorful icons distinguish humans from bots (human = photo, bot = robot icon). Audio support reads questions on hover. Auto-graded by final matches. CSTA: EK‑IC‑SV‑01._




ID: T21.GK.02
Topic: T21 – Chatbots & Prompting
Skill: Sort picture cards into "Good Prompts" vs "Unclear Prompts" categories
Description: **Student task:** Look at 6 picture cards showing different prompts. Drag each card into either the "Clear" box or the "Unclear" box. **Visual scenario:** Cards show: (A) "Help me" (unclear), (B) "Draw a red circle" (clear), (C) "Do something" (unclear), (D) "Tell me about dogs" (clear), (E) "Make it better" (unclear), (F) "Count to 5" (clear). **Correct sorting:** Clear box gets B, D, F; Unclear box gets A, C, E. **Key insight:** Good prompts say exactly what you want. _Implementation note: Binary sorting with visual feedback; cards show speech bubbles with text plus supporting icons. Audio reads prompts. After sorting, brief animation shows why unclear prompts confuse chatbots (bot shows question marks). Auto-graded by final placement. CSTA: EK‑IC‑SV‑01._

Dependencies:
* T21.GK.01: Match pictures of people talking to chatbot icons responding




ID: T21.GK.03
Topic: T21 – Chatbots & Prompting
Skill: Identify the WHO (agent type) in picture-based prompts
Description: **Student task:** Look at 4 picture cards showing prompts with different helper bots. For each card, tap the picture of WHO is being asked (the helper bot type). **Visual scenario:** Card 1 shows: "Artist bot, draw a cat" → student taps artist bot icon. Card 2 shows: "Teacher bot, explain addition" → student taps teacher bot icon. Card 3 shows: "Story bot, tell me a tale" → student taps story bot icon. Card 4 shows: "Math bot, what is 3+5?" → student taps math bot icon. **Key insight:** Different bots are good at different jobs. _Implementation note: MCQ with 4 scenarios; each shows prompt text + 3 bot icons to choose from. Distinct visual bot types (artist = paintbrush, teacher = apple, story = book, math = calculator). Audio reads prompts. Introduces concept that WHO matters in prompting. Auto-graded by selections. CSTA: EK‑IC‑SV‑01._

Dependencies:
* T21.GK.02: Sort picture cards into "Good Prompts" vs "Unclear Prompts" categories




ID: T21.GK.04
Topic: T21 – Chatbots & Prompting
Skill: Predict which picture shows what chatbot will say next
Description: **Student task:** Look at a picture showing a prompt being given to a chatbot. Tap the picture that shows what the chatbot will probably say or do. **Visual scenario:** Prompt shows: child says "Math bot, count to 3" → Answer choices show: (A) chatbot saying "1, 2, 3", (B) chatbot drawing a picture, (C) chatbot playing music. **Correct answer:** (A). Additional scenarios test: recipe bot asked for instructions, story bot asked for tale, artist bot asked to draw. _Implementation note: MCQ with 4 scenarios, 3 visual choices each. Introduces prediction and cause-effect reasoning in chatbot interactions. Audio support. Auto-graded by selections. CSTA: EK‑IC‑SV‑01, EK‑ALG‑AF‑01._

Dependencies:
* T21.GK.03: Identify the WHO (agent type) in picture-based prompts




ID: T21.GK.05
Topic: T21 – Chatbots & Prompting
Skill: Trace a 2-turn picture conversation showing prompt and response
Description: **Student task:** Look at a picture showing a 2-turn conversation. Draw lines connecting the prompt to the response, then the next prompt to the next response. **Visual scenario:** Turn 1: child → "What's 2+2?" → chatbot → "4". Turn 2: same child → "What about 3+3?" → chatbot → "6". Student traces arrows from each speaker to each message bubble. **Key insight:** Conversations go back and forth. _Implementation note: Visual conversation flow diagram with 4 empty arrow lines to draw/trace. Touch-based tracing or drag-and-drop arrow placement. Introduces conversational structure. Audio narrates conversation. Auto-graded by correct arrow placement. CSTA: EK‑IC‑SV‑01._

Dependencies:
* T21.GK.04: Predict which picture shows what chatbot will say next




ID: T21.GK.06
Topic: T21 – Chatbots & Prompting
Skill: Match helper bot types to their job pictures
Description: **Student task:** Look at 5 helper bot icons and 5 job pictures. Drag each bot to the job it does best. **Visual scenario:** Bots: (A) Math bot, (B) Story bot, (C) Artist bot, (D) Music bot, (E) Teacher bot. Jobs: (1) solving addition, (2) telling bedtime stories, (3) drawing animals, (4) playing songs, (5) explaining science. **Correct matches:** A→1, B→2, C→3, D→4, E→5. **Key insight:** Different bots have different skills, just like people have different jobs. _Implementation note: Drag-and-drop matching with 5 pairs; reinforces agent role concept with broader variety. Colorful, distinct bot designs. Audio describes each bot's specialty. Auto-graded by matches. CSTA: EK‑IC‑SV‑01._

Dependencies:
* T21.GK.03: Identify the WHO (agent type) in picture-based prompts




ID: T21.GK.07
Topic: T21 – Chatbots & Prompting
Skill: Choose the picture showing a safe vs unsafe thing to tell a chatbot
Description: **Student task:** Look at 6 picture cards showing things someone might tell a chatbot. Sort them into "Safe to Share" vs "Keep Private" boxes. **Visual scenario:** Cards show: (A) "My favorite color is blue" (safe), (B) "My home address is..." (private), (C) "I like pizza" (safe), (D) "My password is..." (private), (E) "I want to learn about space" (safe), (F) "My mom's phone number is..." (private). **Correct sorting:** Safe = A, C, E; Private = B, D, F. **Key insight:** Never tell chatbots private information like addresses, passwords, or phone numbers. _Implementation note: Binary sorting with visual safety emphasis (green "Safe" box, red "Private" box with lock icon). Audio explains why certain info should stay private. Introduces crucial AI safety concept. Auto-graded with explanation feedback. CSTA: EK‑IC‑SV‑01, EK‑IC‑SL‑02._

Dependencies:
* T21.GK.06: Match helper bot types to their job pictures




ID: T21.G1.01
Topic: T21 – Chatbots & Prompting
Skill: Identify WHAT (task) and HOW (style) parts in picture prompts
Description: **Student task:** Look at 4 picture prompts. For each one, tap the part that shows WHAT to do, then tap the part that shows HOW to do it. **Visual scenario:** Prompt 1: "Draw [WHAT] a cat [HOW] in blue crayon" → student taps "cat" (what), then "blue crayon" (how). Prompt 2: "Tell [WHAT] a story [HOW] about dragons" → student taps "story" (what), then "about dragons" (how). Prompt 3: "Count [WHAT] to 10 [HOW] in Spanish" → student taps "to 10" (what), then "in Spanish" (how). **Key insight:** Prompts have two parts: the action (WHAT) and the details (HOW). _Implementation note: Two-tap selection for 4 scenarios; visual highlighting shows WHAT in one color, HOW in another after taps. Introduces prompt decomposition. Audio explains "WHAT is the action, HOW is the details." Auto-graded by correct taps. CSTA: E1‑IC‑SV‑01._

Dependencies:
* T21.GK.03: Identify the WHO (agent type) in picture-based prompts




ID: T21.G1.02
Topic: T21 – Chatbots & Prompting
Skill: Build a complete picture prompt by dragging WHO, WHAT, HOW cards together
Description: **Student task:** Build 3 complete prompts by dragging word cards into the correct order: WHO (agent type), WHAT (task), HOW (details). **Visual scenario:** Scenario 1 cards: [Artist bot] [draw] [a dog with spots]. Scenario 2 cards: [Math bot] [count] [from 1 to 5]. Scenario 3 cards: [Story bot] [tell a story] [about pirates]. Student drags cards into WHO → WHAT → HOW slots for each scenario. **Key insight:** Complete prompts need all three parts. _Implementation note: Drag-and-drop assembly with 3 prompts; visual prompt template shows labeled WHO/WHAT/HOW boxes. Cards use color coding (blue=WHO, green=WHAT, orange=HOW). Audio feedback when prompt is complete. Auto-graded by final arrangement. CSTA: E1‑IC‑SV‑01._

Dependencies:
* T21.G1.01: Identify WHAT (task) and HOW (style) parts in picture prompts




ID: T21.G1.03
Topic: T21 – Chatbots & Prompting
Skill: Trace a 3-turn picture conversation with branching paths
Description: **Student task:** Look at a conversation diagram showing 3 turns with two possible paths. Trace the path that reaches the happy ending. **Visual scenario:** Turn 1: child → "Story bot, tell me a story". Turn 2a: chatbot → "What kind?" → child → "About space". Turn 3a: chatbot → [tells space story] → happy child. Turn 2b: chatbot → "What kind?" → child → [no answer]. Turn 3b: chatbot → [confused, no story] → sad child. **Correct trace:** Path A (with complete answers) leads to success. **Key insight:** Answering chatbot questions helps get better results. _Implementation note: Visual tree diagram with arrow tracing or path highlighting. Two branches clearly marked. Audio narrates each turn. Introduces concept that conversations have choices and consequences. Auto-graded by traced path. CSTA: E1‑IC‑SV‑01, E1‑ALG‑AF‑01._

Dependencies:
* T21.GK.05: Trace a 2-turn picture conversation showing prompt and response




ID: T21.G1.04
Topic: T21 – Chatbots & Prompting
Skill: Predict what happens when a prompt is missing WHAT or HOW parts
Description: **Student task:** Look at 4 incomplete prompts. For each one, tap the picture showing what will probably happen. **Visual scenario:** Prompt 1: "Artist bot, draw [missing WHAT]" → Choices: (A) bot draws something, (B) bot says "Draw what?", (C) bot sings a song. **Correct:** (B). Prompt 2: "Math bot [missing WHAT AND HOW]" → Choices: (A) bot asks "What do you want?", (B) bot solves a problem, (C) bot tells a story. **Correct:** (A). Additional scenarios test missing HOW details. **Key insight:** Missing parts make chatbots confused. _Implementation note: MCQ with 4 scenarios, 3 picture choices each. Reinforces importance of complete prompts through prediction. Audio support. Auto-graded by selections. CSTA: E1‑IC‑SV‑01._

Dependencies:
* T21.G1.02: Build a complete picture prompt by dragging WHO, WHAT, HOW cards together




ID: T21.G1.05
Topic: T21 – Chatbots & Prompting
Skill: Sort picture cards showing bot responses into "Correct" vs "Wrong" for given prompts
Description: **Student task:** Look at a prompt, then sort 6 bot response cards into "Correct" or "Wrong" boxes. **Visual scenario:** Prompt: "Math bot, count from 1 to 3". Response cards show: (A) "1, 2, 3" (correct), (B) "3, 2, 1" (wrong - backwards), (C) "1, 2, 3, 4, 5" (wrong - too many), (D) "One, two, three" (correct - words count), (E) picture of 3 cats (correct - visual count), (F) "A, B, C" (wrong - letters not numbers). **Correct sorting:** Correct = A, D, E; Wrong = B, C, F. **Key insight:** Check if chatbot really answered what you asked. _Implementation note: Binary sorting with 3 different prompts tested; introduces response verification. Visual feedback explains why wrong answers don't match. Audio support. Auto-graded by placement. CSTA: E1‑IC‑SV‑01._

Dependencies:
* T21.G1.04: Predict what happens when a prompt is missing WHAT or HOW parts




ID: T21.G1.06
Topic: T21 – Chatbots & Prompting
Skill: Match pictures showing real people vs chatbots in conversations
Description: **Student task:** Look at 6 conversation pictures. Sort them into "Talking to Real Person" vs "Talking to Chatbot" boxes. **Visual scenario:** Cards show: (A) child at computer with robot icon (chatbot), (B) two children facing each other talking (real), (C) phone screen showing AI assistant (chatbot), (D) teacher helping student at desk (real), (E) tablet with voice assistant icon (chatbot), (F) parent reading with child (real). **Correct sorting:** Real = B, D, F; Chatbot = A, C, E. **Key insight:** Recognize when you're talking to AI vs. real people. _Implementation note: Binary sorting with clear visual distinctions (robots/screens for AI, face-to-face for humans). Introduces AI literacy and human vs. AI recognition. Audio explains differences. Auto-graded by placement. CSTA: E1‑IC‑SV‑01._

Dependencies:
* T21.GK.07: Choose the picture showing a safe vs unsafe thing to tell a chatbot




ID: T21.G1.07
Topic: T21 – Chatbots & Prompting
Skill: Choose the better prompt from two picture options for the same task
Description: **Student task:** Look at 4 pairs of prompts trying to do the same thing. For each pair, tap the BETTER prompt. **Visual scenario:** Pair 1: Task is "get chatbot to draw a tree". Option A: "Draw something" (worse). Option B: "Artist bot, draw a green tree" (better - has WHO, WHAT, HOW). Pair 2: Task is "learn about space". Option A: "Teacher bot, tell me about planets" (better). Option B: "Teach me" (worse). **Correct choices:** Better prompts are specific and complete. **Key insight:** Better prompts = better results. _Implementation note: Side-by-side comparison with 4 pairs; introduces prompt quality evaluation. Visual highlighting shows complete vs. incomplete prompts after selection. Audio explains why better choice works. Auto-graded by selections. CSTA: E1‑IC‑SV‑01._

Dependencies:
* T21.G1.05: Sort picture cards showing bot responses into "Correct" vs "Wrong" for given prompts




ID: T21.G2.01
Topic: T21 – Chatbots & Prompting
Skill: Decompose picture prompts into Role, Task, and Format components
Description: **Student task:** Look at 3 complete picture prompts. For each one, drag the parts into the correct labeled boxes: ROLE (who), TASK (what to do), FORMAT (how to present it). **Visual scenario:** Prompt 1: "You are a chef [ROLE]. Explain how to make a sandwich [TASK]. Use 3 simple steps [FORMAT]." Student drags "chef" → ROLE box, "explain sandwich" → TASK box, "3 steps" → FORMAT box. Prompt 2: "You are a scientist [ROLE]. Tell me about the sun [TASK]. Use kid-friendly words [FORMAT]." **Key insight:** Good prompts set the role, give the task, and specify the format. _Implementation note: Drag-and-drop sorting with 3 prompts; extends WHO/WHAT/HOW to Role/Task/Format model. Color-coded boxes and cards. Audio explains three-part structure. Auto-graded by placement. CSTA: E2‑IC‑SV‑01._

Dependencies:
* T21.G1.01: Identify WHAT (task) and HOW (style) parts in picture prompts
* T21.G1.02: Build a complete picture prompt by dragging WHO, WHAT, HOW cards together




ID: T21.G2.02
Topic: T21 – Chatbots & Prompting
Skill: Build complete picture prompts using Role, Task, Format cards
Description: **Student task:** Build 4 complete prompts by selecting cards from three piles (Role, Task, Format) and dragging them into prompt builder. **Visual scenario:** Scenario 1: Goal is "get a story about animals for young kids". Student selects: Role = "storyteller", Task = "tell story about animals", Format = "simple words for 5-year-olds". Combined prompt: "You are a storyteller. Tell a story about animals. Use simple words for 5-year-olds." Scenario 2: Goal is "learn how addition works". Student builds appropriate Role/Task/Format combination. **Key insight:** Matching Role, Task, and Format to your goal makes strong prompts. _Implementation note: Drag-and-drop assembly with 4 scenarios; each scenario provides 3-4 options per category. Visual prompt builder combines cards into sentence. Audio reads completed prompt. Auto-graded by logical matches. CSTA: E2‑IC‑SV‑01._

Dependencies:
* T21.G2.01: Decompose picture prompts into Role, Task, and Format components




ID: T21.G2.03
Topic: T21 – Chatbots & Prompting
Skill: Trace a 4-turn picture conversation showing context building
Description: **Student task:** Look at a 4-turn conversation diagram. Draw arrows showing how each answer builds on the last one (context building). **Visual scenario:** Turn 1: "Tell me about dogs" → chatbot explains dogs. Turn 2: "What do they eat?" [context: still talking about dogs] → chatbot explains dog food. Turn 3: "Do they need exercise?" [context: still dogs] → chatbot explains dog exercise. Turn 4: "How much?" [context: referring to exercise amount] → chatbot gives exercise amount. Student traces arrows showing how "they" refers to dogs, and "how much" refers to exercise. **Key insight:** Chatbots remember what you were just talking about. _Implementation note: Visual conversation tree with context reference arrows to trace. Dotted lines show hidden context connections. Audio narrates conversation flow. Introduces conversational context concept. Auto-graded by traced arrows. CSTA: E2‑IC‑SV‑01._

Dependencies:
* T21.G1.03: Trace a 3-turn picture conversation with branching paths




ID: T21.G2.04
Topic: T21 – Chatbots & Prompting
Skill: Predict bot behavior when context changes mid-conversation
Description: **Student task:** Look at 3 conversation scenarios. For each one, predict what happens when the topic suddenly changes. **Visual scenario:** Scenario 1: Talking about dogs → "What's 2+2?" → Choices: (A) chatbot still talks about dogs (wrong), (B) chatbot switches to math (correct). Scenario 2: Asking for recipes → "Tell me a joke" → Choices: (A) chatbot tells joke (correct - new topic), (B) chatbot gives recipe joke (possible but not asked for). **Key insight:** Changing the topic resets the context. _Implementation note: MCQ with 3 scenarios, 2-3 choices each. Visual highlighting shows topic switch. Introduces context management. Audio support. Auto-graded by selections. CSTA: E2‑IC‑SV‑01._

Dependencies:
* T21.G2.03: Trace a 4-turn picture conversation showing context building




ID: T21.G2.05
Topic: T21 – Chatbots & Prompting
Skill: Identify which picture shows the error when bot gives wrong answer
Description: **Student task:** Look at 3 scenarios where a chatbot gave a wrong answer. For each one, tap the picture showing what went wrong: (1) unclear prompt, (2) chatbot mistake, or (3) missing information. **Visual scenario:** Scenario 1: Prompt was "Draw it" → Bot drew random thing → **Error:** (1) unclear prompt (didn't say WHAT to draw). Scenario 2: Prompt was "Math bot, what's 2+2?" → Bot said "5" → **Error:** (2) chatbot mistake (math was wrong). Scenario 3: Prompt was "Chef bot, give me a recipe" → Bot asked "For what food?" → **Error:** (3) missing information (didn't specify food type). **Key insight:** Wrong answers have different causes. _Implementation note: MCQ with 3 scenarios, 3 error type choices shown as pictures. Introduces debugging and error analysis. Visual error type icons (fuzzy speech bubble = unclear, X = mistake, question mark = missing info). Audio explains errors. Auto-graded by selections. CSTA: E2‑IC‑SV‑01._

Dependencies:
* T21.G1.05: Sort picture cards showing bot responses into "Correct" vs "Wrong" for given prompts




ID: T21.G2.06
Topic: T21 – Chatbots & Prompting
Skill: Match simple text prompts to their visual outcomes
Description: **Student task:** Look at 5 text prompts. Drag each prompt to the picture showing its result. **Visual scenario:** Prompts: (A) "Artist bot, draw a blue circle", (B) "Story bot, tell me about a dragon", (C) "Math bot, show me 2+3", (D) "Music bot, play a happy song", (E) "Teacher bot, explain what rain is". Outcome pictures: (1) blue circle image, (2) storybook with dragon, (3) equation "2+3=5", (4) musical notes with smiley face, (5) rain diagram with labels. **Correct matches:** A→1, B→2, C→3, D→4, E→5. **Key insight:** Good prompts lead to predictable results. _Implementation note: Drag-and-drop matching with 5 pairs; bridges picture-based prompts to text-based prompts. Text is simple, with visual support. Audio reads prompts. Auto-graded by matches. CSTA: E2‑IC‑SV‑01._

Dependencies:
* T21.G2.02: Build complete picture prompts using Role, Task, Format cards




ID: T21.G2.07
Topic: T21 – Chatbots & Prompting
Skill: Sort picture scenarios into safe vs unsafe chatbot uses
Description: **Student task:** Look at 8 picture cards showing different chatbot situations. Sort them into "Safe Use" vs "Unsafe Use" boxes. **Visual scenario:** Cards show: (A) asking for homework help (safe), (B) sharing your password (unsafe), (C) learning about animals (safe), (D) meeting strangers chatbot suggested (unsafe), (E) asking for story ideas (safe), (F) believing everything bot says without checking (unsafe), (G) getting math practice (safe), (H) sharing home address (unsafe). **Correct sorting:** Safe = A, C, E, G; Unsafe = B, D, F, H. **Key insight:** Use chatbots as helpers, but protect your private info and always check important facts. _Implementation note: Binary sorting with 8 cards; reinforces AI safety with broader scenarios. Visual feedback explains each safety issue. Audio support. Introduces critical thinking about AI use. Auto-graded by placement. CSTA: E2‑IC‑SV‑01, E2‑IC‑SL‑02._

Dependencies:
* T21.G1.06: Match pictures showing real people vs chatbots in conversations




ID: T21.G2.08
Topic: T21 – Chatbots & Prompting
Skill: Identify pictures showing when to ask a human instead of a chatbot
Description: **Student task:** Look at 6 situation cards. Sort them into "Ask Chatbot" vs "Ask Human (parent/teacher)" boxes. **Visual scenario:** Cards show: (A) "How do you spell 'elephant'?" (chatbot OK), (B) "I feel sad and scared" (ask human - emotional support), (C) "What's 5+7?" (chatbot OK), (D) "Can I go to my friend's house?" (ask human - needs permission), (E) "What do dinosaurs eat?" (chatbot OK), (F) "I'm being bullied at school" (ask human - serious problem). **Correct sorting:** Chatbot = A, C, E; Human = B, D, F. **Key insight:** Chatbots are great for facts and practice, but talk to real people about feelings, problems, and permissions. _Implementation note: Binary sorting with 6 cards; introduces human vs. AI judgment and emotional intelligence. Visual cues show emotional scenarios (heart icon) vs. factual (book icon). Audio explains when humans are needed. Critical AI literacy skill. Auto-graded by placement. CSTA: E2‑IC‑SV‑01, E2‑IC‑SL‑02._

Dependencies:
* T21.G2.07: Sort picture scenarios into safe vs unsafe chatbot uses
# T21 - Chatbots & Prompting - PART 2 (Grades 3-4)
# ============================================================================
# GRADE 3-4 SKILLS: RCTF Framework & Structured Prompting
# ============================================================================
#
# This section focuses on:
# - Transitioning from picture-based to text-based prompting
# - Introducing RCTF (Role, Context, Task, Format) framework
# - Building multi-turn conversational chatbots
# - Debugging and iterating on prompts
# - Testing chatbot behavior systematically
# - Understanding audience and tone in AI communication
#
# ============================================================================

---

## GRADE 3 SKILLS




ID: T21.G3.01
Topic: T21 – Chatbots & Prompting
Skill: Trace how a simple text prompt flows through a chatbot system diagram
Description: **Student task:** Examine a visual flowchart showing how a chatbot processes prompts: [User enters prompt] → [Prompt sent to AI model] → [AI generates response] → [Response displayed to user]. Students label each step and trace what happens when they ask "What is the capital of France?" They identify where the input goes, where processing happens, and where output appears. They answer questions: "Where does the AI's answer come from?" (generated by model, not from a database), "Will the same prompt always give the exact same answer?" (no, slight variations). **Key insight:** Understanding the chatbot pipeline helps debug problems and set realistic expectations. _Implementation note: Interactive diagram with drag-to-label components and trace-path activity. Builds on G2.06's system understanding. CSTA: E3-IC-SV-01._

Dependencies:
* T21.G2.06: Match simple text prompts to their visual outcomes




ID: T21.G3.02
Topic: T21 – Chatbots & Prompting
Skill: Create a one-sentence text prompt with Role and Task components
Description: **Student task:** Write 3 simple one-sentence prompts that include WHO (Role) and WHAT (Task). **Scenario 1:** "I want help writing a story about space." Student writes: "You are a storyteller. Write a story about space." **Scenario 2:** "I need math help with fractions." Student writes: "You are a math teacher. Explain fractions." **Scenario 3:** "I want to learn about animals." Student writes: "You are a scientist. Tell me about animals." System checks that each prompt has both Role ("You are a...") and Task (action verb + subject). **Key insight:** Starting with Role + Task creates clear, focused prompts. _Implementation note: Text entry with template guidance; auto-check verifies presence of role statement and task verb. Provides feedback if components missing. CSTA: E3-IC-SV-01._

Dependencies:
* T21.G2.01: Decompose picture prompts into Role, Task, and Format components
* T21.G2.02: Build complete picture prompts using Role, Task, Format cards




ID: T21.G3.03
Topic: T21 – Chatbots & Prompting
Skill: Add Context and Format components to expand a basic prompt
Description: **Student task:** Take 3 basic Role+Task prompts and expand them by adding Context (why/what situation) and Format (how to present answer). **Example:** Basic prompt: "You are a chef. Explain how to make cookies." Student adds: **Context:** "I'm 8 years old and want to help my parents bake." **Format:** "Give me 5 simple steps." **Final prompt:** "You are a chef. I'm 8 years old and want to help my parents bake cookies. Explain how to make cookies. Give me 5 simple steps." Students create 3 expanded prompts, each building from Role+Task to full RCTF. **Key insight:** Context and Format make responses more relevant and useful. _Implementation note: Guided prompt builder with four text fields (R, C, T, F); shows before/after comparison. Auto-graded by presence of all components. CSTA: E3-IC-SV-01._

Dependencies:
* T21.G3.02: Create a one-sentence text prompt with Role and Task components




ID: T21.G3.03.01
Topic: T21 – Chatbots & Prompting
Skill: Identify which RCTF component is missing in incomplete prompts
Description: **Student task:** Read 6 incomplete prompts and identify which RCTF component (Role, Context, Task, or Format) is missing. **Example 1:** "I'm working on a science project about volcanoes [Context]. Explain volcanoes [Task]. Use bullet points [Format]." **Missing:** Role. **Example 2:** "You are a history expert [Role]. Explain the American Revolution [Task]. Use simple words [Format]." **Missing:** Context. Students drag each prompt into the correct "Missing ___" box. After sorting, they add the missing component to complete each prompt. **Key insight:** Recognizing gaps in prompts helps improve them systematically. _Implementation note: Sorting activity with 6 prompts (2 per missing component type); follow-up asks students to fill in missing parts. Auto-graded. CSTA: E3-IC-SV-01._

Dependencies:
* T21.G3.03: Add Context and Format components to expand a basic prompt




ID: T21.G3.04
Topic: T21 – Chatbots & Prompting
Skill: Create a simple chatbot that responds to one specific keyword
Description: **Student task:** Build a basic chatbot script in CreatiCode using if-then logic. Chatbot detects ONE keyword and responds accordingly. **Example:** User asks "help" → Chatbot says "I'm here to help! What do you need?" Students use blocks: `when green flag clicked` → `ask [Type your message] and wait` → `if <(answer) contains [help]> then` → `say [I'm here to help!]`. Students test with multiple inputs to see when chatbot responds vs. stays silent. **Key insight:** Simple chatbots use pattern matching, not true understanding. _Implementation note: Block-based coding activity using conditional logic; introduces keyword detection. Students must test with 3+ inputs. CSTA: E3-AP-AF-01, E3-IC-SV-01._

Dependencies:
* T21.G3.01: Trace how a simple text prompt flows through a chatbot system diagram




ID: T21.G3.05
Topic: T21 – Chatbots & Prompting
Skill: Predict chatbot response for 3-4 different user inputs to same bot
Description: **Student task:** Given a chatbot with defined behavior, predict how it will respond to different inputs. **Scenario:** Chatbot programmed to: if input contains "hello" → say "Hi there!"; if input contains "help" → say "What do you need?"; otherwise → say "I don't understand." Students predict responses for: (1) "hello friend", (2) "I need help", (3) "what's the weather?", (4) "hello, I need help". **Correct predictions:** (1) "Hi there!", (2) "What do you need?", (3) "I don't understand", (4) depends on which condition is checked first. **Key insight:** Understanding chatbot logic helps predict behavior and find edge cases. _Implementation note: MCQ prediction activity with 4 inputs; reveals importance of condition order and overlapping patterns. CSTA: E3-AP-AF-01._

Dependencies:
* T21.G3.04: Create a simple chatbot that responds to one specific keyword




ID: T21.G3.06
Topic: T21 – Chatbots & Prompting
Skill: Trace a 3-turn conversation showing how context is preserved
Description: **Student task:** Examine a conversation transcript and trace how information from early turns is used in later responses. **Conversation:** Turn 1: User: "My favorite animal is a dolphin." Bot: "Dolphins are amazing! They're very intelligent." Turn 2: User: "Where do they live?" Bot: "Dolphins live in oceans around the world." Turn 3: User: "What do they eat?" Bot: "Dolphins eat fish and squid." Students highlight pronouns ("they") and draw arrows showing what each refers to (dolphins). They identify that context is maintained across all 3 turns without re-stating "dolphins." **Key insight:** Conversational AI maintains context by remembering previous exchanges. _Implementation note: Visual annotation activity with conversation transcript; students mark context references. CSTA: E3-IC-SV-01._

Dependencies:
* T21.G3.05: Predict chatbot response for 3-4 different user inputs to same bot




ID: T21.G3.07
Topic: T21 – Chatbots & Prompting
Skill: Build a 2-turn chatbot conversation with context from turn 1 used in turn 2
Description: **Student task:** Create a chatbot that asks for information in turn 1, then uses that information in turn 2. **Example script:** Turn 1: Bot asks "What's your favorite color?" → stores answer in variable `favoriteColor`. Turn 2: Bot says: `join [My favorite color is also] (favoriteColor)!`. Students build this using blocks: `ask [What's your favorite color?] and wait` → `set [favoriteColor] to (answer)` → `say (join [My favorite color is also ] (favoriteColor)!)`. They test with different inputs to verify context carries over. **Key insight:** Variables store context between conversation turns. _Implementation note: Block-based coding with variables; introduces state management in conversations. CSTA: E3-AP-AF-01, E3-AP-V-01._

Dependencies:
* T21.G3.06: Trace a 3-turn conversation showing how context is preserved




ID: T21.G3.08
Topic: T21 – Chatbots & Prompting
Skill: Compare expected vs actual chatbot output to identify prompt problems
Description: **Student task:** Students are given 3 scenarios where desired output doesn't match actual output. They identify what went wrong in each prompt. **Scenario 1:** Desired: "Three rhyming words about cats." Actual: Long paragraph about cat history. **Problem:** Prompt didn't specify Format (3 words). **Scenario 2:** Desired: "Funny story for kids." Actual: Serious scientific explanation. **Problem:** Prompt didn't specify Role (comedian/storyteller) or Context (for kids). **Scenario 3:** Desired: "Recipe with exact measurements." Actual: Vague cooking instructions. **Problem:** Prompt didn't specify Format (include measurements). Students select the problem from multiple choices and rewrite the prompt to fix it. **Key insight:** Debugging prompts requires comparing intent vs. result. _Implementation note: Three debugging scenarios with MCQ problem identification + prompt rewriting. CSTA: E3-IC-SV-01._

Dependencies:
* T21.G3.05: Predict chatbot response for 3-4 different user inputs to same bot




ID: T21.G3.09
Topic: T21 – Chatbots & Prompting
Skill: Fix a broken prompt by adding missing details or correcting vague language
Description: **Student task:** Students receive 4 broken prompts and fix each one by adding specificity or correcting vague language. **Broken Prompt 1:** "Tell me about it." **Problem:** No subject specified. **Fixed:** "You are a science teacher. Tell me about photosynthesis. Use simple language for a 3rd grader." **Broken Prompt 2:** "Write something good." **Problem:** Too vague. **Fixed:** "You are a poet. Write a short, happy poem about sunshine. Use 4 lines with rhyming words." Students identify the vague parts (highlighted) and rewrite with specific details. After fixing, they test both versions with AI and compare results. **Key insight:** Specific details transform vague prompts into effective ones. _Implementation note: Prompt editing activity with before/after testing; highlights improvements in output quality. CSTA: E3-IC-SV-01._

Dependencies:
* T21.G3.08: Compare expected vs actual chatbot output to identify prompt problems




ID: T21.G3.10
Topic: T21 – Chatbots & Prompting
Skill: Create chatbot responses for 3 different user moods (happy, sad, confused)
Description: **Student task:** Design a chatbot that detects user mood keywords and responds appropriately. **Mood detection:** Happy keywords: "great", "happy", "excited". Sad keywords: "sad", "upset", "bad day". Confused keywords: "don't understand", "confused", "help". Students build if-then-else logic: `if <answer contains [happy OR great OR excited]>` → `say [That's wonderful! I'm glad you're feeling good!]`. `else if <answer contains [sad OR upset OR bad]>` → `say [I'm sorry you're feeling down. Want to talk about it?]`. `else if <answer contains [confused OR don't understand OR help]>` → `say [Let me help clarify! What are you confused about?]`. Test with 6+ inputs representing different moods. **Key insight:** Empathetic chatbots adapt responses to user emotional state. _Implementation note: Block-based coding with multiple conditionals; introduces tone adaptation. CSTA: E3-AP-AF-01, E3-IC-SV-01._

Dependencies:
* T21.G3.04: Create a simple chatbot that responds to one specific keyword




ID: T21.G3.11
Topic: T21 – Chatbots & Prompting
Skill: Identify which prompts ask the chatbot to do harmful or inappropriate things
Description: **Student task:** Review 8 prompts and sort them into "Appropriate" vs "Inappropriate/Harmful" categories. **Appropriate prompts:** "Help me write a thank-you letter", "Explain how recycling works", "Create a fun quiz about animals", "Write a story about friendship". **Inappropriate prompts:** "Write my essay so I can pretend it's mine" (academic dishonesty), "Help me lie to my parents" (dishonest), "Say mean things about someone" (harmful), "Tell me how to break into a computer" (illegal). Students sort and explain WHY each inappropriate prompt is problematic (dishonesty, harm, illegal activity, academic cheating). **Key insight:** AI should be used ethically and responsibly, not to harm, cheat, or deceive. _Implementation note: Sorting activity with ethical reasoning; includes follow-up questions about consequences. Critical AI literacy skill. CSTA: E3-IC-SL-02._

Dependencies:
* T21.G3.03: Add Context and Format components to expand a basic prompt




ID: T21.G3.12
Topic: T21 – Chatbots & Prompting
Skill: Design a chatbot personality by choosing role, tone, and sample responses
Description: **Student task:** Create a complete chatbot personality profile including Role, Tone, and example responses. Students choose from personality templates or create custom: **Example 1 - Friendly Tutor Bot:** Role: "Helpful math teacher", Tone: "Encouraging and patient", Sample responses: "Great question! Let's work through this together." **Example 2 - Adventure Guide Bot:** Role: "Explorer and storyteller", Tone: "Exciting and adventurous", Sample responses: "What an amazing discovery! Let's explore further!" Students define their bot's personality in a character sheet, then write 3 system prompts that establish this personality, and create 5 example user-bot exchanges showing the personality in action. **Key insight:** Chatbot personality is defined through carefully crafted role and tone instructions. _Implementation note: Creative design activity with personality template; students test their chatbot personality with real AI. CSTA: E3-IC-SV-01._

Dependencies:
* T21.G3.03: Add Context and Format components to expand a basic prompt
* T21.G3.10: Create chatbot responses for 3 different user moods (happy, sad, confused)


---

## GRADE 4 SKILLS




ID: T21.G4.01
Topic: T21 – Chatbots & Prompting
Skill: Trace how different RCTF components change chatbot behavior
Description: **Student task:** Test the same prompt with systematic changes to each RCTF component and document how behavior changes. **Base prompt:** "You are a teacher [R]. I'm studying for a test [C]. Explain fractions [T]. Use simple language [F]." Students create variations: Change R: "You are a comedian" → response becomes funny/playful. Change C: "I'm teaching my younger sibling" → response becomes even simpler. Change T: "Give examples of fractions in daily life" → response shows real-world applications. Change F: "Use a story format" → response becomes narrative. Students complete a comparison table showing how each component shapes the output. **Key insight:** Each RCTF component independently influences chatbot behavior. _Implementation note: Systematic experimentation activity; students document observations in structured table. CSTA: E4-IC-SV-01._

Dependencies:
* T21.G3.03: Add Context and Format components to expand a basic prompt




ID: T21.G4.02
Topic: T21 – Chatbots & Prompting
Skill: Build prompts using RCTF framework for 3 different scenarios
Description: **Student task:** Apply RCTF framework to create complete prompts for three distinct scenarios. **Scenario 1 - Homework Help:** R: "You are a patient science tutor", C: "I'm a 4th grader working on my homework about the water cycle", T: "Explain the water cycle", F: "Use 4-5 simple sentences with an example I can relate to". **Scenario 2 - Creative Writing:** R: "You are a creative writing coach", C: "I want to write a story for my class assignment about adventure", T: "Help me brainstorm story ideas", F: "Give me 3 different story concepts as bullet points". **Scenario 3 - Learning New Skill:** R: "You are a coding instructor", C: "I'm learning to code and want to make a simple game", T: "Explain what a variable is", F: "Use a real-world analogy that a 10-year-old would understand". Students write all RCTF components for each scenario and test with AI. **Key insight:** RCTF provides a systematic approach to prompt construction for any purpose. _Implementation note: Structured prompt-writing activity with template; students test and compare outputs. CSTA: E4-IC-SV-01._

Dependencies:
* T21.G4.01: Trace how different RCTF components change chatbot behavior




ID: T21.G4.02.01
Topic: T21 – Chatbots & Prompting
Skill: Optimize each RCTF component to improve prompt clarity
Description: **Student task:** Take 3 poorly-written prompts and optimize each RCTF component for clarity and effectiveness. **Poor Prompt 1:** "You are someone who knows stuff [R - too vague]. I need information [C - unclear]. Tell me things [T - no specific task]. Make it good [F - meaningless]." **Optimized:** "You are a marine biologist [R - specific expertise]. I'm preparing a presentation for my class about ocean conservation [C - clear purpose]. Explain why coral reefs are important [T - focused task]. Give me 3 main reasons with one example for each [F - concrete format]." Students optimize 3 prompts by: 1) Making Role specific and relevant, 2) Adding meaningful Context, 3) Creating focused Task, 4) Defining clear Format. They compare outputs from original vs. optimized prompts. **Key insight:** Optimization means making each component specific, relevant, and measurable. _Implementation note: Prompt refinement activity; side-by-side comparison shows quality improvement. CSTA: E4-IC-SV-01._

Dependencies:
* T21.G4.02: Build prompts using RCTF framework for 3 different scenarios




ID: T21.G4.03
Topic: T21 – Chatbots & Prompting
Skill: Create a chatbot with 4-5 different response patterns using if-then logic
Description: **Student task:** Build a more sophisticated chatbot that can handle 4-5 different user intents using nested if-then-else logic. **Example - Homework Helper Bot:** Detects: (1) Math keywords → "I can help with math! What's the problem?", (2) Science keywords → "Science is fascinating! What topic?", (3) Writing keywords → "Let's work on your writing! What are you writing about?", (4) "I don't know" → "That's okay! Let's figure out what you need help with.", (5) None of above → "I help with math, science, and writing. Which subject?". Students implement using nested conditionals, test with 10+ varied inputs, and document which inputs trigger which patterns. **Key insight:** Complex chatbots use decision trees with multiple branches. _Implementation note: Block-based coding with nested conditionals; students create comprehensive test plan. CSTA: E4-AP-AF-01, E4-IC-SV-01._

Dependencies:
* T21.G3.04: Create a simple chatbot that responds to one specific keyword
* T21.G3.10: Create chatbot responses for 3 different user moods (happy, sad, confused)




ID: T21.G4.04
Topic: T21 – Chatbots & Prompting
Skill: Test chatbot with 5+ diverse inputs and document which ones fail
Description: **Student task:** Create a systematic test plan for a chatbot, execute tests, and document failures. Students design test cases covering: (1) Normal inputs (expected keywords), (2) Edge cases (typos, capitalization, extra words), (3) Out-of-scope inputs (unrelated topics), (4) Boundary cases (multiple keywords in one input), (5) Empty/minimal inputs. **Example test table:** Input: "help me with math please" | Expected: Math response | Actual: Math response | Pass/Fail: Pass. Input: "HELP MATH" | Expected: Math response | Actual: No response | Pass/Fail: Fail (case-sensitive). Students document at least 5 failures, categorize failure types (case sensitivity, missing keywords, unexpected format), and propose fixes. **Key insight:** Systematic testing reveals chatbot limitations and improvement opportunities. _Implementation note: Test documentation activity with pass/fail tracking; introduces QA methodology. CSTA: E4-AP-AF-01._

Dependencies:
* T21.G4.03: Create a chatbot with 4-5 different response patterns using if-then logic




ID: T21.G4.05
Topic: T21 – Chatbots & Prompting
Skill: Parse user input to extract key information (name, number, topic)
Description: **Student task:** Build a chatbot that extracts specific information from user input and uses it in responses. **Scenario 1 - Name extraction:** User: "My name is Alex" → Bot extracts "Alex" → Stores in variable → Says "Nice to meet you, Alex!" **Scenario 2 - Number extraction:** User: "I have 3 cats" → Bot extracts "3" → Says "Wow, 3 cats! That's a lot!" **Scenario 3 - Topic extraction:** User: "I want to learn about dinosaurs" → Bot extracts "dinosaurs" → Says "Dinosaurs are fascinating! What do you want to know about dinosaurs?" Students use string manipulation blocks (`letter () of ()`, `join`, `contains`) to locate and extract information. They test extraction with varied sentence structures. **Key insight:** Information extraction allows personalized, context-aware responses. _Implementation note: Block-based coding with string manipulation; introduces basic NLP concepts. CSTA: E4-AP-AF-01, E4-AP-V-01._

Dependencies:
* T21.G4.03: Create a chatbot with 4-5 different response patterns using if-then logic




ID: T21.G4.06
Topic: T21 – Chatbots & Prompting
Skill: Build a 3-turn conversation where bot remembers 2 pieces of information
Description: **Student task:** Create a stateful chatbot conversation that gathers and uses multiple pieces of information across turns. **Conversation flow:** Turn 1: Bot: "What's your name?" → User: "Emma" → Store in `userName`. Bot: "Nice to meet you, Emma! What's your favorite subject?" Turn 2: User: "Science" → Store in `favoriteSubject`. Bot: "Science is great, Emma! What science topic interests you most?" Turn 3: User: "Space" → Store in `scienceTopic`. Bot: "Emma, I can tell you love science, especially space! Here's a fun fact about space: ..." Students implement using variables to maintain state, ensure pronouns and names are used correctly to show context, and test that information persists throughout the conversation. **Key insight:** Multi-variable state management enables natural, contextual conversations. _Implementation note: Block-based coding with multiple variables and sequential dialogue; introduces conversation state complexity. CSTA: E4-AP-AF-01, E4-AP-V-01._

Dependencies:
* T21.G3.07: Build a 2-turn chatbot conversation with context from turn 1 used in turn 2
* T21.G4.05: Parse user input to extract key information (name, number, topic)




ID: T21.G4.07
Topic: T21 – Chatbots & Prompting
Skill: Trace conversation flow through a 4-turn branching dialogue tree
Description: **Student task:** Examine a complex branching dialogue tree with 4 turns and multiple paths. Students trace different conversation paths based on user choices. **Dialogue tree:** Turn 1: Bot: "Do you want help with homework or want to play a game?" Turn 2a (if homework): Bot: "What subject?" → branches to math/science/writing. Turn 2b (if game): Bot: "What type of game?" → branches to trivia/word game/story. Turn 3: Further specialization based on Turn 2 choice. Turn 4: Final response tailored to path. Students trace 3 different complete paths, identify decision points, and document how context from each turn influences subsequent options. They draw arrows showing valid and invalid transitions. **Key insight:** Branching conversations create decision trees with multiple valid paths. _Implementation note: Visual tree diagram tracing with annotation; prepares for implementing branching logic. CSTA: E4-AP-AF-01._

Dependencies:
* T21.G3.06: Trace a 3-turn conversation showing how context is preserved




ID: T21.G4.08
Topic: T21 – Chatbots & Prompting
Skill: Implement a branching conversation with 2 choice points
Description: **Student task:** Build a chatbot with a branching conversation structure featuring 2 decision points. **Implementation example - Story Game Bot:** Turn 1: "Do you want a scary story or a funny story?" → Store choice. Turn 2 (if scary): "Do you want ghosts or monsters?" → Branch A: ghosts, Branch B: monsters. Turn 2 (if funny): "Do you want animals or silly people?" → Branch C: animals, Branch D: silly people. Turn 3: Tell appropriate story based on path taken. Students use nested if-then-else structures, track which path user is on using variables, and create 4 different story endings (one per path). They test all 4 paths and verify correct story is told. **Key insight:** Branching logic creates interactive, personalized experiences. _Implementation note: Block-based coding with nested conditionals and state tracking; students create flowchart before coding. CSTA: E4-AP-AF-01, E4-AP-V-01._

Dependencies:
* T21.G4.07: Trace conversation flow through a 4-turn branching dialogue tree




ID: T21.G4.09
Topic: T21 – Chatbots & Prompting
Skill: Debug a prompt by testing one RCTF component change at a time
Description: **Student task:** Use systematic debugging to fix a prompt that produces poor output. Students follow scientific method: (1) Identify the problem with current output, (2) Form hypothesis about which RCTF component is causing issue, (3) Test by changing ONLY that component, (4) Observe if output improves, (5) Iterate. **Example:** Prompt: "You are a helper [R - vague]. I need information [C - unclear]. Tell me about dogs [T]. Make it interesting [F - vague]." **Problem:** Output is too technical and long. **Hypothesis 1:** Role is too vague. **Test:** Change R to "You are a friendly pet expert for kids" → Output improves slightly. **Hypothesis 2:** Format is vague. **Test:** Add F: "Use 3-4 simple sentences" → Output much better! Students debug 3 prompts, documenting each hypothesis and test result. **Key insight:** Systematic debugging isolates which components need improvement. _Implementation note: Structured debugging worksheet with hypothesis-test-result tracking. CSTA: E4-IC-SV-01._

Dependencies:
* T21.G3.09: Fix a broken prompt by adding missing details or correcting vague language
* T21.G4.01: Trace how different RCTF components change chatbot behavior




ID: T21.G4.10
Topic: T21 – Chatbots & Prompting
Skill: Create test cases for chatbot covering normal, edge, and error inputs
Description: **Student task:** Design comprehensive test suite with three categories of test cases. **Normal cases:** Expected inputs that should work perfectly. **Edge cases:** Unusual but valid inputs (typos, mixed case, extra punctuation, very short/long inputs). **Error cases:** Invalid or out-of-scope inputs that should be handled gracefully. **Example test suite for Math Helper Bot:** Normal: "help with addition", "I need math help", "solve 2+2". Edge: "HELP", "m a t h", "help???", "can you maybe possibly help with math please". Error: "cook a recipe", "12345", "", "asdfghjkl". Students create 15+ test cases (5 per category), predict expected behavior, run tests, and document which cases fail. They propose error handling for failed cases. **Key insight:** Comprehensive testing ensures robust chatbot performance across all input types. _Implementation note: Test suite design activity with categorization and prediction; introduces software testing principles. CSTA: E4-AP-AF-01._

Dependencies:
* T21.G4.04: Test chatbot with 5+ diverse inputs and document which ones fail




ID: T21.G4.11
Topic: T21 – Chatbots & Prompting
Skill: Compare two different prompts for the same task and evaluate quality
Description: **Student task:** Evaluate and compare two prompts designed for the same goal using quality criteria. Students receive rubric: (1) Clarity - Are instructions clear? (2) Completeness - Are all RCTF components present? (3) Specificity - Is language precise? (4) Output quality - Does it produce desired result? **Example comparison:** Goal: "Get help writing a poem about nature." **Prompt A:** "Write a nature poem." **Prompt B:** "You are a creative poetry teacher [R]. I'm a 4th grade student working on a class project about appreciating nature [C]. Help me write a short poem celebrating trees and forests [T]. Use 4 lines with simple rhymes that paint a visual picture [F]." Students score each prompt (1-5) on each criterion, test both prompts, compare outputs, and write a justification for which is better and why. They complete this for 3 different prompt pairs. **Key insight:** Systematic evaluation reveals what makes prompts effective. _Implementation note: Comparison activity with scoring rubric; students analyze quality factors. CSTA: E4-IC-SV-01._

Dependencies:
* T21.G4.02: Build prompts using RCTF framework for 3 different scenarios




ID: T21.G4.12
Topic: T21 – Chatbots & Prompting
Skill: Identify when chatbot output contains incorrect or made-up information
Description: **Student task:** Learn to spot AI hallucinations and factual errors. Students receive 8 chatbot responses and verify accuracy using trusted sources. **Example responses to check:** (1) "The capital of France is Paris" (correct), (2) "Penguins live in the Arctic" (incorrect - they live in Antarctica), (3) "George Washington was the 3rd president" (incorrect - he was 1st), (4) "The fastest land animal is the cheetah" (correct), (5) [Made-up fact about invented animal], (6) [Plausible-sounding but false historical claim]. Students categorize each as: Correct, Factually wrong, or Made-up (hallucination). For incorrect/made-up items, they find the correct information and explain why AI might have made the error. **Key insight:** AI can confidently state incorrect information; always verify important facts. _Implementation note: Fact-checking activity with research component; critical AI literacy skill. CSTA: E4-IC-SV-01, E4-IC-SL-02._

Dependencies:
* T21.G4.04: Test chatbot with 5+ diverse inputs and document which ones fail




ID: T21.G4.13
Topic: T21 – Chatbots & Prompting
Skill: Design a chatbot for a specific audience (young children, teenagers, adults)
Description: **Student task:** Create three versions of the same chatbot optimized for different age groups. Students adapt vocabulary, tone, complexity, and examples for each audience. **Task:** Create a chatbot that explains "what is gravity" for: **Audience 1 - Young children (ages 5-7):** R: "You are a friendly teacher for young kids", C: "Explain to a 6-year-old", T: "Explain gravity", F: "Use 2-3 very simple sentences with an example like dropping a ball". Sample output: "Gravity is like an invisible force that pulls things down. When you drop a ball, gravity makes it fall to the ground!" **Audience 2 - Preteens (ages 10-12):** More detailed explanation with scientific terms. **Audience 3 - Teenagers (ages 14-16):** Include physics concepts, formulas, and real-world applications. Students write RCTF prompts for all three audiences, test outputs, and analyze how vocabulary, sentence structure, and examples differ. **Key insight:** Effective communication adapts to audience knowledge and needs. _Implementation note: Audience-adaptation activity; students compare outputs across age groups. CSTA: E4-IC-SV-01._

Dependencies:
* T21.G3.12: Design a chatbot personality by choosing role, tone, and sample responses
* T21.G4.02: Build prompts using RCTF framework for 3 different scenarios


---

## END OF GRADE 4 SKILLS
# T21 - Chatbots & Prompting - PART 3: Grades 5-6
# ============================================================================
# GRADE 5: Parameters & Testing (14 skills)
# GRADE 6: Advanced Parameters & Multimodal (16 skills)
# ============================================================================


ID: T21.G5.01
Topic: T21 – Chatbots & Prompting
Skill: Trace how the same prompt with different parameters produces different outputs
Description: **Student task:** Given one prompt ("Write a story about a dragon"), run it with three different parameter settings and observe how outputs change. **Example scenarios:** (A) temperature=0.2 → consistent, predictable story; (B) temperature=0.7 → creative variations; (C) temperature=1.5 → highly unpredictable, experimental. Record observations about: (1) consistency between runs, (2) creativity level, (3) coherence quality. **Part 1 (Predict):** Before running, predict which parameter setting produces which type of output. **Part 2 (Verify):** Run each configuration and confirm predictions. **Part 3 (Document):** Complete observation table noting key differences. **Skill focus:** Understanding that parameters control HOW models generate responses, not just WHAT they say. _Implementation note: Interactive parameter tester with side-by-side output comparison. Student completes guided observation worksheet. Auto-graded by prediction accuracy + observation completeness. CSTA: E5‑IC‑SV‑01, E5‑DA‑IM‑01._

Dependencies:
* T21.G4.02: Build prompts using RCTF framework for 3 different scenarios




ID: T21.G5.02
Topic: T21 – Chatbots & Prompting
Skill: Predict output characteristics based on parameter settings
Description: **Student task:** Given a prompt and specific parameter values, predict key characteristics of the output BEFORE running it. **Example:** "Summarize this article" with temperature=0.1, max_tokens=50. **Predict:** (A) Will summary be creative or factual? (B) Will it be short or long? (C) Will multiple runs give same result? **Correct predictions:** (A) Factual (low temp = deterministic), (B) Short (max 50 tokens), (C) Same (low temp = consistent). **Part 1:** Make predictions for 3 different parameter combinations. **Part 2:** Run chatbot and verify. **Part 3:** Explain when predictions were wrong and why. **Skill focus:** Developing mental model of parameter effects. _Implementation note: Prediction quiz with instant verification; rubric checks reasoning quality. Auto-graded for predictions + self-graded explanation of errors. CSTA: E5‑IC‑SV‑01, E5‑AP‑AA‑02._

Dependencies:
* T21.G5.01: Trace how the same prompt with different parameters produces different outputs




ID: T21.G5.03
Topic: T21 – Chatbots & Prompting
Skill: Design a complex multi-turn chatbot implementing RCTF in system prompt
Description: **Student task:** Create a chatbot with a detailed system prompt that includes all RCTF components (Role, Context, Task, Format) and test it through a 5+ turn conversation. **Example system prompt:** "You are a Homework Helper Bot [Role]. You work with 5th grade students who need help understanding math concepts, not just getting answers [Context]. Your task is to guide students to discover answers through questions, hints, and examples rather than directly solving problems [Task]. Always respond with: (1) a clarifying question, (2) a helpful hint or example, (3) encouragement [Format]." **Requirements:** (A) System prompt includes all RCTF elements, (B) Test with 5 turns covering different scenarios, (C) Bot stays in character consistently, (D) Format rules are followed throughout. _Implementation note: Coding task with system prompt editor + conversation tester. Rubric grades: RCTF completeness, multi-turn consistency, format adherence. CSTA: E5‑IC‑SV‑01, E5‑CS‑PC‑02._

Dependencies:
* T21.G4.06: Build a 3-turn conversation where bot remembers 2 pieces of information
* T21.G4.08: Implement a branching conversation with 2 choice points




ID: T21.G5.04
Topic: T21 – Chatbots & Prompting
Skill: Implement temperature parameter to control creative vs deterministic outputs
Description: **Student task:** Create three versions of the same chatbot with different temperature settings and explain when to use each. **Example bot: "Story Generator"** - (A) Version 1: temp=0.2 (for consistent moral lessons), (B) Version 2: temp=0.7 (for varied creative stories), (C) Version 3: temp=1.2 (for experimental wild stories). **Task:** For each version: (1) Set temperature appropriately, (2) Test with same prompt 3 times, (3) Document consistency level, (4) Identify best use case. **Deliverable:** Comparison table showing: temperature value, output consistency (same/similar/very different), creativity level (low/medium/high), recommended use case. **Skill focus:** Matching parameter settings to application needs. _Implementation note: Parameter configuration interface + multi-run tester. Rubric grades setting choices and use case justifications. CSTA: E5‑IC‑SV‑01, E5‑AP‑AA‑02._

Dependencies:
* T21.G5.01: Trace how the same prompt with different parameters produces different outputs
* T21.G5.02: Predict output characteristics based on parameter settings




ID: T21.G5.04.01
Topic: T21 – Chatbots & Prompting
Skill: Compare outputs across temperature range to find optimal setting
Description: **Student task:** Given a specific task ("Generate quiz questions from a science passage"), systematically test temperature values from 0.0 to 2.0 in increments of 0.3 to find the optimal setting. **Process:** (1) Define success criteria (e.g., questions must be factually accurate, moderately varied, properly formatted), (2) Test 7 temperature values: 0.0, 0.3, 0.6, 0.9, 1.2, 1.5, 1.8, (3) Rate each output on success criteria (1-5 scale), (4) Identify temperature with best average rating, (5) Explain trade-offs. **Example findings:** "temp=0.6 produced accurate questions with some variety (avg rating 4.2), temp=0.9 was more creative but sometimes less accurate (avg 3.8), temp=0.3 was too repetitive (avg 3.5)." **Deliverable:** Data table + recommendation with justification. **Skill focus:** Systematic parameter optimization through empirical testing. _Implementation note: Multi-run comparison tool with rating interface. Rubric grades methodology, data quality, and reasoning. CSTA: E5‑DA‑IM‑01, E5‑AP‑AA‑02._

Dependencies:
* T21.G5.04: Implement temperature parameter to control creative vs deterministic outputs




ID: T21.G5.05
Topic: T21 – Chatbots & Prompting
Skill: Use max tokens parameter to plan and control response length
Description: **Student task:** Design prompts with max_tokens settings to achieve specific length requirements. **Three scenarios:** (A) Tweet summary (max_tokens=50), (B) Paragraph explanation (max_tokens=150), (C) Detailed essay (max_tokens=500). **For each:** (1) Set appropriate max_tokens, (2) Test if output fits requirement, (3) Adjust if too long/short, (4) Document final setting and why it works. **Challenge:** Some prompts may get cut off mid-sentence if max_tokens is too low—identify these cases and fix by either (a) increasing tokens or (b) adding format instruction "end with complete sentences only". **Skill focus:** Understanding token limits as output length control mechanism. _Implementation note: Length-testing interface with character/token counter. Auto-graded by output length matching requirements. CSTA: E5‑IC‑SV‑01, E5‑AP‑AA‑02._

Dependencies:
* T21.G5.02: Predict output characteristics based on parameter settings




ID: T21.G5.06
Topic: T21 – Chatbots & Prompting
Skill: Implement stop sequences to create structured output formats
Description: **Student task:** Use stop sequences to force chatbot to produce output in specific structured format. **Example task:** "Generate a quiz with exactly 3 questions." **Without stop sequence:** Bot might generate 4+ questions. **With stop sequence:** Set stop="Question 4:" to force it to stop after exactly 3 questions. **Three applications to implement:** (1) List with exactly 5 items (stop="6."), (2) Dialogue ending at specific point (stop="END"), (3) Code snippet without explanation (stop="Explanation:"). **For each:** (A) Identify where output should stop, (B) Set appropriate stop sequence, (C) Test and verify it stops correctly, (D) Handle edge cases where stop sequence appears in content. **Skill focus:** Precise control over output structure using stop conditions. _Implementation note: Stop sequence configuration interface with format testing. Auto-graded by output structure matching requirements. CSTA: E5‑IC‑SV‑01, E5‑AP‑AA‑02._

Dependencies:
* T21.G5.05: Use max tokens parameter to plan and control response length




ID: T21.G5.07
Topic: T21 – Chatbots & Prompting
Skill: Apply frequency and presence penalties to control output variety
Description: **Student task:** Use frequency_penalty and presence_penalty parameters to reduce repetition and increase topic diversity. **Example problem:** "Generate creative story ideas" produces repetitive themes (dragons, princesses, treasure). **Solution testing:** (A) Baseline (no penalties) → note repetition level, (B) frequency_penalty=0.5 → reduces repeating exact words/phrases, (C) presence_penalty=0.5 → encourages new topics, (D) both penalties=0.7 → maximum diversity. **Task:** For three different prompt types (story ideas, product names, conversation responses), test penalty combinations and identify optimal settings. **Deliverable:** Settings table with examples showing: (1) baseline output, (2) with frequency penalty, (3) with presence penalty, (4) with both, (5) recommended combination for each prompt type. **Skill focus:** Fine-tuning output variety using penalty parameters. _Implementation note: Parameter comparison interface with side-by-side output viewer. Rubric grades systematic testing and justified recommendations. CSTA: E5‑IC‑SV‑01, E5‑DA‑IM‑01._

Dependencies:
* T21.G5.04: Implement temperature parameter to control creative vs deterministic outputs




ID: T21.G5.08
Topic: T21 – Chatbots & Prompting
Skill: Parse and extract structured data from chatbot responses (JSON, lists)
Description: **Student task:** Design prompts that produce structured output, then write code to parse and use that data. **Example:** "List 5 countries in JSON format: {name, capital, population}". **Expected output:** `[{"name": "France", "capital": "Paris", "population": 67000000}, ...]`. **Task parts:** (1) Write prompt that requests specific JSON structure, (2) Run chatbot and save response, (3) Parse JSON in JavaScript, (4) Extract specific fields (e.g., all country names), (5) Use extracted data in a program (e.g., display on screen, create quiz). **Three formats to implement:** (A) JSON object list, (B) CSV table, (C) Numbered list. **Skill focus:** Treating chatbot output as structured data source for programs. _Implementation note: Coding task with JSON/text parsing functions. Auto-graded by successful data extraction and usage. CSTA: E5‑AP‑PF‑01, E5‑DA‑ST‑01._

Dependencies:
* T21.G4.05: Parse user input to extract key information (name, number, topic)
* T21.G5.06: Implement stop sequences to create structured output formats




ID: T21.G5.09
Topic: T21 – Chatbots & Prompting
Skill: Chain two chatbot calls where output of first becomes input to second
Description: **Student task:** Create a two-step chatbot pipeline where the output from Call 1 is automatically used as input for Call 2. **Example chain:** **Call 1:** "Write a short story about a robot" → Output: 3-paragraph story. **Call 2:** "Summarize this story in one sentence: [story from Call 1]" → Output: one-sentence summary. **Implementation:** (1) Make first chatbot call, (2) Store response in a variable, (3) Construct second prompt using stored response, (4) Make second chatbot call, (5) Display final result. **Three chains to implement:** (A) Generate text → Translate it, (B) Generate code → Explain it, (C) Generate question → Generate answer. **Skill focus:** Sequential chatbot operations with data flow. _Implementation note: Coding task with chatbot API calls and variable passing. Auto-graded by successful chain execution and correct final output. CSTA: E5‑AP‑PF‑01, E5‑AP‑AA‑02._

Dependencies:
* T21.G5.08: Parse and extract structured data from chatbot responses (JSON, lists)




ID: T21.G5.10
Topic: T21 – Chatbots & Prompting
Skill: Design systematic test cases covering diverse prompt scenarios
Description: **Student task:** Create a comprehensive test suite for a chatbot that covers normal cases, edge cases, and error cases. **Example chatbot:** "Math Homework Helper" that answers 5th grade math questions. **Test case categories to design:** (1) **Normal cases** - typical math questions across topics (addition, fractions, word problems), (2) **Edge cases** - very simple problems (1+1), very complex problems (multi-step), ambiguous wording, (3) **Error cases** - off-topic questions ("What's the weather?"), inappropriate requests, impossible problems. **Deliverable:** Test suite table with columns: Test ID, Category, Input prompt, Expected behavior, Pass/Fail criteria. **Minimum 15 test cases** covering all categories. **Part 2:** Run all tests and document results. **Skill focus:** Systematic quality assurance for chatbot applications. _Implementation note: Test case template + testing interface. Rubric grades test coverage, diversity, and criteria clarity. CSTA: E5‑AP‑PF‑01, E5‑CS‑PC‑02._

Dependencies:
* T21.G4.10: Create test cases for chatbot covering normal, edge, and error inputs




ID: T21.G5.11
Topic: T21 – Chatbots & Prompting
Skill: Implement regression testing when modifying prompts
Description: **Student task:** When updating a chatbot's system prompt, run regression tests to ensure old functionality still works. **Scenario:** You have a "Story Generator" bot with 10 passing test cases. You want to add a new feature: "always include a moral lesson." **Process:** (1) Run baseline tests - document all 10 passing, (2) Modify system prompt to add new feature, (3) Run regression tests - check if all 10 still pass, (4) Fix any broken tests by adjusting prompt, (5) Add 3 new tests for the new feature. **Regression test tracking:** Create table with columns: Test ID, Description, Baseline result, After modification, Status (Pass/Regression/Fixed), Notes. **Skill focus:** Ensuring new changes don't break existing functionality. _Implementation note: Test runner with before/after comparison view. Rubric grades regression detection and fix documentation. CSTA: E5‑AP‑PF‑01, E5‑CS‑PC‑02._

Dependencies:
* T21.G5.10: Design systematic test cases covering diverse prompt scenarios




ID: T21.G5.12
Topic: T21 – Chatbots & Prompting
Skill: Integrate voice input to chatbot using speech-to-text
Description: **Student task:** Create a chatbot that accepts spoken input using CreatiCode's speech-to-text features. **Implementation steps:** (1) Add "listen and wait" block to capture spoken input, (2) Store transcribed text in a variable, (3) Send that text to chatbot as prompt, (4) Display chatbot response. **Three voice-activated bots to create:** (A) Voice-activated story generator ("Tell me a story about..."), (B) Voice math helper ("What is 25 times 4?"), (C) Voice trivia bot ("Ask me a trivia question"). **Testing requirements:** Test with (1) clear speech in quiet environment, (2) speech with background noise, (3) complex sentences with numbers/names, (4) accented speech. Document accuracy and limitations. **Skill focus:** Multimodal input integration - spoken prompts. _Implementation note: Coding task with speech-to-text blocks + chatbot integration. Auto-graded by successful voice → chatbot → response flow. CSTA: E5‑IC‑SV‑01, E5‑CS‑HS‑01._

Dependencies:
* T21.G5.03: Design a complex multi-turn chatbot implementing RCTF in system prompt




ID: T21.G5.13
Topic: T21 – Chatbots & Prompting
Skill: Implement text-to-speech for chatbot responses
Description: **Student task:** Create a chatbot that speaks its responses using text-to-speech. **Implementation steps:** (1) Make chatbot call with prompt, (2) Store response text in variable, (3) Use "speak" block to vocalize the response, (4) Optionally adjust speech rate/pitch/voice. **Three speaking bots to create:** (A) Story narrator (slow, expressive speech), (B) Quiz master (clear, moderate pace), (C) Joke teller (playful, varied pitch). **Enhancement:** Add speech controls allowing user to choose: (1) voice type (male/female/robotic), (2) speed (slow/normal/fast), (3) language. **Testing:** Verify (1) entire response is spoken, (2) punctuation affects pacing appropriately, (3) long responses don't get cut off, (4) special characters/emojis are handled correctly. **Skill focus:** Multimodal output - voiced chatbot responses. _Implementation note: Coding task with text-to-speech blocks + chatbot integration. Auto-graded by successful chatbot → speech flow. CSTA: E5‑IC‑SV‑01, E5‑CS‑HS‑01._

Dependencies:
* T21.G5.12: Integrate voice input to chatbot using speech-to-text




# ============================================================================
# GRADE 6: Advanced Parameters & Multimodal (16 skills)
# ============================================================================


ID: T21.G6.01
Topic: T21 – Chatbots & Prompting
Skill: Analyze how parameter combinations interact to affect output quality
Description: **Student task:** Investigate how multiple parameters work together to produce different output characteristics. **Research question:** "How do temperature and top_p interact to control randomness?" **Experimental design:** Test 9 combinations in a 3×3 grid: temperature (0.3, 0.7, 1.2) × top_p (0.5, 0.8, 0.95). **For each combination:** (1) Run same prompt 5 times, (2) Measure output variance (are responses very similar or very different?), (3) Rate output quality (coherence, relevance, creativity), (4) Record observations. **Deliverable:** (A) Data table with 9 rows (one per combination), (B) Analysis identifying: which combinations produce most/least variance, which produce highest quality, any surprising interactions. **Example finding:** "High temp (1.2) + low top_p (0.5) produced incoherent results, but medium temp (0.7) + high top_p (0.95) balanced creativity with quality." **Skill focus:** Understanding parameter interactions through systematic experimentation. _Implementation note: Multi-parameter testing interface with data collection forms. Rubric grades experimental rigor and insight quality. CSTA: E6‑DA‑IM‑01, E6‑AP‑AA‑02._

Dependencies:
* T21.G5.04: Implement temperature parameter to control creative vs deterministic outputs
* T21.G5.05: Use max tokens parameter to plan and control response length
* T21.G5.07: Apply frequency and presence penalties to control output variety




ID: T21.G6.02
Topic: T21 – Chatbots & Prompting
Skill: Optimize parameters for specific use cases through experimentation
Description: **Student task:** Given a specific application, systematically optimize all relevant parameters to maximize output quality. **Example use case:** "Generate marketing slogans for a lemonade stand." **Success criteria:** Slogans must be (1) under 10 words, (2) catchy and memorable, (3) varied across runs, (4) appropriate for kids. **Parameters to optimize:** max_tokens, temperature, frequency_penalty, presence_penalty. **Process:** (1) Start with default values, (2) Tune one parameter at a time while holding others constant, (3) Identify best value for each parameter, (4) Test final combination, (5) Document optimization journey with examples. **Deliverable:** Optimization report showing: (A) Parameter evolution table, (B) Before/after examples, (C) Final recommended settings with justification, (D) Quality metrics (success criteria ratings). **Skill focus:** Applied parameter tuning for real-world tasks. _Implementation note: Parameter optimization workspace with A/B testing tools. Rubric grades systematic approach and results quality. CSTA: E6‑AP‑AA‑02, E6‑DA‑IM‑01._

Dependencies:
* T21.G6.01: Analyze how parameter combinations interact to affect output quality




ID: T21.G6.03
Topic: T21 – Chatbots & Prompting
Skill: Implement few-shot learning by providing examples in prompts
Description: **Student task:** Improve chatbot performance by including example input-output pairs in prompts. **Concept:** Instead of just describing what you want, SHOW examples. **Example task:** "Convert casual text to formal language." **Zero-shot prompt (no examples):** "Make this text more formal: [input]" → inconsistent results. **Few-shot prompt (with examples):** "Convert casual to formal. Examples: 'hey dude' → 'Hello', 'yeah sure' → 'Yes, certainly', 'kinda cool' → 'quite impressive'. Now convert: [input]" → much better results. **Assignment:** Create three few-shot prompts: (A) Sentiment classification (positive/negative/neutral), (B) Question type identification (who/what/when/where/why/how), (C) Text simplification for younger readers. **For each:** Include 3-5 examples, test with 10 new inputs, compare accuracy to zero-shot version. **Skill focus:** Using examples to teach chatbots desired behavior patterns. _Implementation note: Prompt template builder with example slots. Auto-graded by accuracy improvement over zero-shot baseline. CSTA: E6‑IC‑SV‑01, E6‑AP‑AA‑02._

Dependencies:
* T21.G5.04: Implement temperature parameter to control creative vs deterministic outputs




ID: T21.G6.03.01
Topic: T21 – Chatbots & Prompting
Skill: Select effective examples for few-shot learning
Description: **Student task:** Investigate which types of examples produce the best few-shot learning results. **Research question:** "Does example quality and diversity matter?" **Experiment:** Create three versions of a classification prompt with different example selection strategies. **Task:** Classify text as "complaint," "question," or "compliment." **Version A - Similar examples:** All examples are short, simple sentences. **Version B - Diverse examples:** Mix of short/long, simple/complex, clear/ambiguous. **Version C - Edge-case examples:** Challenging cases that could be multiple categories. **For each version:** Test with 15 inputs covering easy, medium, hard cases. Measure accuracy for each difficulty level. **Deliverable:** (A) Analysis of which example strategy works best overall and why, (B) Recommendations for example selection (how many? how diverse? include edge cases?), (C) Documented examples showing strategy differences. **Skill focus:** Strategic example selection to maximize few-shot effectiveness. _Implementation note: Example comparison interface with accuracy tracking. Rubric grades experimental design and insights. CSTA: E6‑DA‑IM‑01, E6‑AP‑AA‑02._

Dependencies:
* T21.G6.03: Implement few-shot learning by providing examples in prompts




ID: T21.G6.04
Topic: T21 – Chatbots & Prompting
Skill: Create prompt templates with variables for reusable patterns
Description: **Student task:** Design reusable prompt templates with variables that can be filled in for different use cases. **Concept:** Instead of writing new prompts from scratch, create a template once and reuse with different inputs. **Example template:** "You are a [ROLE] helping with [SUBJECT]. Explain [CONCEPT] to a [GRADE_LEVEL] student using [STYLE] language and [FORMAT] format." **Variables to fill:** ROLE=teacher, SUBJECT=science, CONCEPT=photosynthesis, GRADE_LEVEL=5th grade, STYLE=simple, FORMAT=bullet points. **Assignment:** Create three reusable templates: (A) Educational content generator (any subject, any grade), (B) Creative writing assistant (any genre, any character), (C) Code explainer (any language, any skill level). **For each template:** (1) Define all variables with descriptions, (2) Provide 3 example instantiations with different variable values, (3) Test that template works across varied inputs, (4) Document template usage instructions. **Skill focus:** Abstraction and reusability in prompt engineering. _Implementation note: Template builder with variable substitution interface. Rubric grades template flexibility and documentation quality. CSTA: E6‑AP‑AA‑01, E6‑CS‑PC‑02._

Dependencies:
* T21.G5.03: Design a complex multi-turn chatbot implementing RCTF in system prompt




ID: T21.G6.05
Topic: T21 – Chatbots & Prompting
Skill: Implement top-p (nucleus sampling) parameter for controlled randomness
Description: **Student task:** Use the top_p parameter to control output randomness by limiting the token pool the model samples from. **Concept:** top_p=0.9 means "only consider the top 90% most likely next tokens" (ignoring unlikely options). **Comparison task:** Generate creative product names with different top_p values: (A) top_p=0.5 (conservative - only most likely tokens), (B) top_p=0.8 (balanced), (C) top_p=0.95 (adventurous - includes less likely tokens). **For each setting:** (1) Generate 10 product names, (2) Rate creativity (1-5), (3) Rate coherence (1-5), (4) Note if any outputs are nonsensical. **Expected finding:** Lower top_p = safer but less creative, higher top_p = more creative but sometimes incoherent. **Follow-up:** Compare top_p to temperature control. When should you use each? **Deliverable:** Data table + recommendation for when to use top_p vs temperature. **Skill focus:** Alternative randomness control mechanism for specific use cases. _Implementation note: top_p configuration interface with side-by-side comparison. Rubric grades understanding of top_p vs temperature. CSTA: E6‑IC‑SV‑01, E6‑AP‑AA‑02._

Dependencies:
* T21.G5.04: Implement temperature parameter to control creative vs deterministic outputs




ID: T21.G6.06
Topic: T21 – Chatbots & Prompting
Skill: Use logit bias to increase/decrease probability of specific tokens
Description: **Student task:** Apply logit bias to encourage or discourage specific words/tokens in chatbot output. **Use case examples:** (A) Generate G-rated stories (negative bias on violent/inappropriate words), (B) Technical writing (positive bias on professional terminology, negative on casual slang), (C) Inclusive language (positive bias on gender-neutral terms). **Implementation:** For "Story Generator" chatbot: (1) Identify 10 words to avoid (e.g., "kill," "blood," "hate"), (2) Set logit bias = -5.0 for those token IDs, (3) Generate 10 stories and verify unwanted words are rare/absent, (4) Compare to baseline without bias. **Challenge:** Logit bias works on tokens, not words—some words are multiple tokens. Must handle tokenization. **Deliverable:** Bias configuration + before/after examples showing effectiveness. **Limitation discussion:** Bias doesn't guarantee exclusion, just reduces probability—alternative strategies if 100% exclusion required? **Skill focus:** Fine-grained control over vocabulary using token-level biases. _Implementation note: Logit bias configuration interface with tokenization helper. Rubric grades correct bias application and limitation understanding. CSTA: E6‑IC‑SV‑01, E6‑AP‑AA‑02._

Dependencies:
* T21.G6.05: Implement top-p (nucleus sampling) parameter for controlled randomness




ID: T21.G6.07
Topic: T21 – Chatbots & Prompting
Skill: Implement best-of-n sampling to select highest quality output
Description: **Student task:** Generate multiple outputs for the same prompt and automatically select the best one using a quality scoring function. **Concept:** Instead of using the first response, generate N responses and pick the best. **Example task:** "Write a haiku about technology." **Process:** (1) Generate 5 haikus (n=5), (2) Score each on criteria: follows 5-7-5 syllable rule (auto-check), contains technology theme (keyword check), poetic quality (simplicity: word count, complexity: adjective/verb ratio), (3) Select haiku with highest total score, (4) Return that as final output. **Assignment:** Implement best-of-n for three tasks: (A) Haiku generation (syllable count + theme scoring), (B) Multiple-choice question generation (difficulty scoring based on distractor quality), (C) Code generation (correctness scoring via test execution). **For each:** Define scoring function, test n=1,3,5,10 to find quality improvement vs cost. **Skill focus:** Quality maximization through generate-and-select strategies. _Implementation note: Multi-generation interface with scoring function builder. Rubric grades scoring function design and n-value analysis. CSTA: E6‑AP‑AA‑02, E6‑DA‑IM‑01._

Dependencies:
* T21.G6.02: Optimize parameters for specific use cases through experimentation




ID: T21.G6.08
Topic: T21 – Chatbots & Prompting
Skill: Chain multiple specialized prompts to accomplish complex tasks
Description: **Student task:** Break down a complex task into a pipeline of specialized chatbot calls, where each call performs one focused step. **Example complex task:** "Create a quiz from a Wikipedia article." **Pipeline:** (1) **Summarizer bot:** Extract key facts from article → list of 10 facts, (2) **Question generator bot:** Convert each fact into a question → 10 questions, (3) **Answer generator bot:** Create 3 wrong answers for each question → full multiple-choice quiz, (4) **Quality checker bot:** Review quiz for clarity and difficulty → final polished quiz. **Assignment:** Design and implement a 4+ step pipeline for one of: (A) Story writing: idea generator → outliner → writer → editor, (B) Code development: requirement analyzer → code generator → bug finder → documenter, (C) Learning content: topic researcher → concept explainer → example creator → quiz maker. **Deliverable:** Pipeline diagram, specialized prompts for each step, working implementation, example showing full pipeline execution. **Skill focus:** Task decomposition and sequential specialization. _Implementation note: Coding task with multi-step chatbot pipeline. Rubric grades pipeline design and specialization clarity. CSTA: E6‑AP‑PF‑01, E6‑AP‑AA‑01._

Dependencies:
* T21.G5.09: Chain two chatbot calls where output of first becomes input to second




ID: T21.G6.09
Topic: T21 – Chatbots & Prompting
Skill: Implement conversational memory with summarization for long contexts
Description: **Student task:** Build a chatbot that maintains conversation history but summarizes old messages to stay under token limits. **Problem:** Chatbot APIs have token limits (e.g., 4000 tokens). Long conversations exceed limits and fail or forget early context. **Solution:** Rolling summarization: (1) Keep recent 5 messages in full detail, (2) Summarize older messages into compact form, (3) Include summary + recent messages in each call. **Example:** After 10 turns, conversation history = "[Summary of turns 1-5: User asked about dogs, bot explained breeds]" + [Full text of turns 6-10]. **Implementation:** Create a "Homework Helper" bot that: (1) Tracks all conversation turns, (2) After every 5 turns, summarizes turns 1-5, (3) After 10 turns, summarizes turns 1-10 into one compact summary, (4) Always includes summary + recent context in chatbot calls. **Testing:** Have a 20-turn conversation and verify bot remembers key facts from turn 1. **Skill focus:** Managing context windows with summarization strategies. _Implementation note: Coding task with conversation state management. Auto-graded by long-conversation coherence tests. CSTA: E6‑AP‑PF‑01, E6‑DA‑ST‑01._

Dependencies:
* T21.G5.03: Design a complex multi-turn chatbot implementing RCTF in system prompt
* T21.G5.05: Use max tokens parameter to plan and control response length




ID: T21.G6.10
Topic: T21 – Chatbots & Prompting
Skill: Debug prompts using systematic parameter isolation
Description: **Student task:** When a chatbot produces unexpected output, systematically isolate the cause using controlled parameter testing. **Debugging process:** (1) **Identify the problem:** Describe what's wrong (output too long, incoherent, wrong format, etc.), (2) **Form hypothesis:** Which parameter or prompt element might cause this? (3) **Isolate variables:** Test with one parameter changed at a time, (4) **Verify fix:** Once problem is isolated, apply fix and retest. **Example debugging scenario:** Chatbot generates inconsistent story tones (sometimes funny, sometimes serious). **Hypothesis A:** Temperature too high → Test: lower temp from 0.9 to 0.3. **Result:** Still inconsistent. **Hypothesis B:** Prompt lacks tone specification → Test: Add "always use humorous tone" to system prompt. **Result:** Fixed! **Assignment:** Debug three broken chatbots: (A) Responses too short (token limit issue?), (B) Responses repetitive (penalty issue?), (C) Responses ignore format (prompt clarity issue?). For each, document: problem, hypothesis, tests, solution. **Skill focus:** Systematic debugging using scientific method. _Implementation note: Debugging sandbox with hypothesis tracking form. Rubric grades systematic approach and root cause identification. CSTA: E6‑AP‑TR‑02, E6‑AP‑AA‑02._

Dependencies:
* T21.G4.09: Debug a prompt by testing one RCTF component change at a time
* T21.G6.01: Analyze how parameter combinations interact to affect output quality




ID: T21.G6.11
Topic: T21 – Chatbots & Prompting
Skill: Design automated test suites with pass/fail criteria
Description: **Student task:** Create an automated test suite that can verify chatbot behavior without human judgment. **Test suite components:** (1) **Test cases:** Input prompts with expected output characteristics, (2) **Automated checks:** Code that verifies outputs meet criteria, (3) **Pass/fail reporting:** Clear indication of which tests passed. **Example test for "Quiz Generator" bot:** **Test 1:** Input="Generate 5 math questions" → Check: output contains exactly 5 question marks (regex: count "?"), Check: each question contains numbers (regex: `\d+`), Check: output under 500 chars. **Pass criteria:** All 3 checks true. **Assignment:** Build automated test suite for a "Summarizer" bot with 10+ tests checking: (1) Length requirements (summary shorter than original), (2) Content preservation (key terms from original appear in summary), (3) Format compliance (no bullet points if prompt says paragraph), (4) Edge cases (very short input, very long input, no coherent content). **Deliverable:** Test code + test results table showing pass/fail for each test. **Skill focus:** Programmatic quality assurance. _Implementation note: Coding task with test assertion helpers. Auto-graded by test suite completeness and correctness. CSTA: E6‑AP‑PF‑01, E6‑AP‑TR‑02._

Dependencies:
* T21.G5.10: Design systematic test cases covering diverse prompt scenarios
* T21.G5.11: Implement regression testing when modifying prompts




ID: T21.G6.12
Topic: T21 – Chatbots & Prompting
Skill: Implement A/B testing to compare prompt variants
Description: **Student task:** Design and execute an A/B test to determine which of two prompt variants produces better results. **A/B testing process:** (1) **Define variants:** Create two different prompts for the same task (Prompt A vs Prompt B), (2) **Define success metric:** How will you measure which is better? (accuracy, user preference, output length, etc.), (3) **Collect data:** Run each prompt N times with diverse inputs, (4) **Analyze results:** Calculate success metric for each variant, determine statistical significance, (5) **Choose winner:** Select better prompt with justification. **Example test:** **Task:** "Explain science concepts to 5th graders." **Prompt A:** Direct approach - "Explain [topic] simply." **Prompt B:** Analogy approach - "Explain [topic] using everyday analogies a 5th grader knows." **Success metric:** Readability score (Flesch-Kincaid grade level) + contains analogy (yes/no). **Test with 20 topics.** **Assignment:** Run A/B test comparing prompt strategies for one task type. Present results with data visualization. **Skill focus:** Empirical prompt optimization through controlled comparison. _Implementation note: A/B testing framework with data collection and analysis tools. Rubric grades experimental design and statistical reasoning. CSTA: E6‑DA‑IM‑01, E6‑AP‑AA‑02._

Dependencies:
* T21.G6.11: Design automated test suites with pass/fail criteria




ID: T21.G6.13
Topic: T21 – Chatbots & Prompting
Skill: Create test cases for edge cases and failure modes
Description: **Student task:** Design test cases specifically targeting scenarios where chatbots are likely to fail. **Edge case categories:** (1) **Boundary conditions:** Empty input, extremely long input, input at exact token limit, (2) **Ambiguous input:** Multiple valid interpretations, contradictory instructions, (3) **Unexpected input:** Wrong language, code instead of text, gibberish, (4) **Adversarial input:** Attempts to break instructions (jailbreaking), inappropriate content, prompt injection, (5) **Format violations:** Missing required fields, wrong data types, malformed structure. **Assignment:** For a "Customer Service Bot," create 20 edge case tests covering all 5 categories. **For each test:** (A) Describe the edge case scenario, (B) Provide example input, (C) Define expected behavior (graceful failure, error message, clarification request), (D) Run test and document actual behavior, (E) If chatbot handles poorly, propose prompt improvement. **Deliverable:** Edge case test suite + analysis of chatbot robustness + recommendations. **Skill focus:** Adversarial thinking and robustness testing. _Implementation note: Edge case test builder with failure mode library. Rubric grades test creativity and coverage. CSTA: E6‑AP‑TR‑02, E6‑IC‑SL‑01._

Dependencies:
* T21.G6.11: Design automated test suites with pass/fail criteria




ID: T21.G6.14
Topic: T21 – Chatbots & Prompting
Skill: Implement image-based prompting with vision-capable models
Description: **Student task:** Create chatbots that accept images as input and respond based on visual content. **Use cases:** (1) **Image description:** Upload photo → bot describes what's in the image, (2) **Visual question answering:** Upload image + ask question → bot answers based on image content, (3) **Image analysis:** Upload diagram → bot explains the concept shown. **Assignment:** Build three vision-based bots: (A) "Homework Helper" - upload photo of math problem → bot explains solution steps, (B) "Art Critic" - upload artwork → bot analyzes style, colors, mood, (C) "Object Counter" - upload image → bot counts specific objects (e.g., "how many red circles?"). **Technical implementation:** (1) Use image upload block in CreatiCode, (2) Send image + text prompt to vision-capable chatbot API, (3) Parse and display response. **Testing:** Test with (1) clear, high-quality images, (2) blurry or low-quality images, (3) images with text, (4) abstract images. Document accuracy and limitations. **Skill focus:** Multimodal prompting with visual input. _Implementation note: Image upload + vision API integration coding task. Auto-graded by successful image → response flow. CSTA: E6‑IC‑SV‑01, E6‑AP‑PF‑01._

Dependencies:
* T21.G6.03: Implement few-shot learning by providing examples in prompts




ID: T21.G6.15
Topic: T21 – Chatbots & Prompting
Skill: Ensure consistency between voice, text, and image modalities
Description: **Student task:** Create a multimodal chatbot that accepts input in any format (voice, text, image) and maintains consistent behavior across modalities. **Challenge:** Voice input may be transcribed imperfectly, images may be interpreted differently than text descriptions—bot must handle gracefully. **Assignment:** Build a "Multimodal Quiz Bot" that: (1) Accepts questions via voice, text, or image upload, (2) Processes each modality appropriately (speech-to-text, direct text, vision analysis), (3) Responds with consistent quiz format regardless of input type, (4) Optionally outputs answers via text OR speech based on user preference. **Consistency requirements:** (A) Same content question via voice vs text produces same quiz, (B) Image of written question produces same quiz as typed question, (C) Response quality doesn't degrade with any modality. **Testing:** Create 10 test questions, submit each via all three modalities, compare outputs for consistency. **Deliverable:** Multimodal bot + consistency test report with examples showing matched outputs. **Skill focus:** Unified multimodal experience design. _Implementation note: Coding task integrating speech, text, and vision APIs. Rubric grades cross-modality consistency. CSTA: E6‑IC‑SV‑01, E6‑AP‑PF‑01._

Dependencies:
* T21.G5.13: Implement text-to-speech for chatbot responses
* T21.G6.14: Implement image-based prompting with vision-capable models
# T21 - Chatbots & Prompting - PART 4 (Grades 7-8)

## GRADE 7 SKILLS




ID: T21.G7.01
Topic: T21 – Chatbots & Prompting
Skill: Implement chain-of-thought prompting for complex reasoning tasks
Description: Students build prompts that explicitly request step-by-step reasoning for complex problems. They add instructions like "Let's solve this step by step," "First analyze..., then consider..., finally conclude..." to guide the AI through multi-stage reasoning. They test on challenging tasks (word problems, logic puzzles, multi-step analysis) and compare chain-of-thought responses to direct answers, documenting accuracy improvements. They create a "reasoning template" that structures prompts into: (1) problem statement, (2) reasoning instructions, (3) format for showing work, (4) final answer format.

Dependencies:
* T21.G6.08: Chain multiple specialized prompts to accomplish complex tasks




ID: T21.G7.02
Topic: T21 – Chatbots & Prompting
Skill: Create self-consistency prompting with multiple reasoning paths
Description: Students implement self-consistency by requesting the AI generate multiple independent reasoning paths for the same problem, then identify the most common answer. They build a system that runs the same complex question 3-5 times with chain-of-thought prompting, collects all answers, and uses voting or pattern detection to find consensus. They test on problems with definitive answers (math, logic) to verify that self-consistency improves accuracy. They document cases where answers diverge and analyze why.

Dependencies:
* T21.G7.01: Implement chain-of-thought prompting for complex reasoning tasks




ID: T21.G7.03
Topic: T21 – Chatbots & Prompting
Skill: Implement tree-of-thought prompting with branching exploration
Description: Students design prompts that explore multiple solution strategies simultaneously, creating a "tree" of possibilities. They prompt the AI to: (1) generate 2-3 different approaches to a problem, (2) evaluate pros/cons of each approach, (3) select the most promising path, (4) solve using that approach. They build a visual display showing the branching exploration process. They compare tree-of-thought to linear chain-of-thought on complex planning tasks (game strategy, project planning, creative problem-solving).

Dependencies:
* T21.G7.02: Create self-consistency prompting with multiple reasoning paths




ID: T21.G7.04
Topic: T21 – Chatbots & Prompting
Skill: Parse and validate structured outputs against schemas
Description: Students create prompts that request specific structured formats (JSON, CSV, key-value pairs) and build code to validate the response matches the expected schema. They define schema requirements (required fields, data types, value constraints), parse the AI response, and check each requirement. They implement error handling for malformed outputs with retry logic. Example: request "Generate 3 product records with fields: name (text), price (number 0-1000), category (one of: Electronics, Clothing, Food)" and validate each field.

Dependencies:
* T21.G5.08: Parse and extract structured data from chatbot responses (JSON, lists)
* T21.G6.04: Create prompt templates with variables for reusable patterns




ID: T21.G7.05
Topic: T21 – Chatbots & Prompting
Skill: Implement prompt compression to reduce token usage
Description: Students learn techniques to compress prompts while maintaining effectiveness: abbreviations, removing redundancy, using symbols over words, condensing examples. They take verbose prompts and systematically reduce token count by 30-50% while testing that outputs remain equivalent. They measure token usage before/after using a token counter, document compression strategies, and create a "compression checklist." They balance token savings against clarity loss.

Dependencies:
* T21.G5.05: Use max tokens parameter to plan and control response length
* T21.G6.09: Implement conversational memory with summarization for long contexts




ID: T21.G7.06
Topic: T21 – Chatbots & Prompting
Skill: Create role-based prompts for domain expertise simulation
Description: Students design prompts that assign the AI a specific expert role with appropriate knowledge, tone, and constraints. They create role definitions for different domains: "You are a patient science teacher explaining to 7th graders," "You are a professional editor reviewing academic writing," "You are a friendly coding tutor helping beginners debug." They test how role framing affects response style, vocabulary, explanation depth, and accuracy. They build a role library with 5+ distinct personas and document when each is most effective.

Dependencies:
* T21.G6.04: Create prompt templates with variables for reusable patterns




ID: T21.G7.07
Topic: T21 – Chatbots & Prompting
Skill: Implement instruction hierarchy in prompts (system, user, context)
Description: Students structure prompts into distinct layers with clear precedence: SYSTEM instructions (unchanging behavioral rules), USER CONTEXT (session information), TASK (current request). They learn that system-level instructions take priority and user inputs cannot override them. They build a chatbot with layered prompts: system="Always respond in simple language. Never discuss politics," context="User is 12 years old learning about history," task=user's question. They test boundary cases where user tries to override system rules.

Dependencies:
* T21.G7.06: Create role-based prompts for domain expertise simulation




ID: T21.G7.08
Topic: T21 – Chatbots & Prompting
Skill: Build conversational agents with personality consistency across sessions
Description: Students create chatbots with persistent personality traits that remain consistent across multiple conversations and sessions. They define personality dimensions (formality, humor, enthusiasm, verbosity) and encode them in system prompts. They implement session memory that recalls personality-relevant facts ("You mentioned you like science fiction in our last chat"). They test personality consistency by running multiple conversations and checking that tone, vocabulary, and behavioral patterns remain stable. They document what breaks consistency.

Dependencies:
* T21.G6.09: Implement conversational memory with summarization for long contexts
* T21.G7.06: Create role-based prompts for domain expertise simulation




ID: T21.G7.09
Topic: T21 – Chatbots & Prompting
Skill: Implement semantic similarity search for context retrieval
Description: Students build a system that finds relevant past conversations or knowledge based on meaning rather than exact keyword matches. They maintain a list of previous Q&A pairs, compute which are semantically similar to the current question (using AI to judge relevance), and include the most relevant past exchanges in the prompt context. They compare keyword search vs semantic search for retrieving helpful context. Example: "What causes rain?" should retrieve past conversation about "water cycle" even without the word "rain."

Dependencies:
* T21.G6.09: Implement conversational memory with summarization for long contexts




ID: T21.G7.10
Topic: T21 – Chatbots & Prompting
Skill: Create prompts that handle ambiguity through clarification questions
Description: Students design prompts that detect ambiguous or underspecified user requests and respond with clarifying questions before attempting a full answer. They build logic to identify ambiguity signals (vague pronouns, missing details, multiple interpretations) and generate targeted questions. Example: User asks "How do I fix it?" → Bot responds "What are you trying to fix? Can you describe the problem?" They implement multi-turn clarification dialogs and test on intentionally vague requests.

Dependencies:
* T21.G7.07: Implement instruction hierarchy in prompts (system, user, context)




ID: T21.G7.11
Topic: T21 – Chatbots & Prompting
Skill: Implement function calling for external tool integration
Description: Students learn to describe available tools/functions in prompts so the AI can decide when and how to call them. They define function signatures (name, description, parameters, return type) and include them in the system prompt. When the AI generates a function call request in structured format, they parse it, execute the actual function, and feed results back to the AI. Example tools: calculator, web search, database lookup, unit converter. They build a tool registry and dispatcher system.

Dependencies:
* T21.G7.04: Parse and validate structured outputs against schemas




ID: T21.G7.11.01
Topic: T21 – Chatbots & Prompting
Skill: Design function calling prompts with clear tool descriptions
Description: Students focus on writing effective tool descriptions that help the AI understand when and how to use each function. They learn to specify: tool purpose, when it should be used, parameter requirements, example inputs/outputs, and error conditions. They create descriptions for 5+ diverse tools (math, data lookup, formatting, external APIs) and test whether the AI correctly chooses appropriate tools for various user requests. They iterate on descriptions that cause confusion or misuse.

Dependencies:
* T21.G7.11: Implement function calling for external tool integration




ID: T21.G7.12
Topic: T21 – Chatbots & Prompting
Skill: Build tool-use orchestration with sequential tool calls
Description: Students implement systems where the AI chains multiple tool calls to accomplish complex tasks. They prompt the AI to create multi-step plans (call tool A, use result in tool B, combine with tool C) and execute them sequentially. They handle data passing between tools, track execution state, and display progress. Example: "What's the weather in Tokyo in Fahrenheit?" requires: (1) get weather in Celsius, (2) convert to Fahrenheit, (3) format response. They build error recovery when any step fails.

Dependencies:
* T21.G7.11: Implement function calling for external tool integration




ID: T21.G7.13
Topic: T21 – Chatbots & Prompting
Skill: Implement error handling and retry logic for tool calls
Description: Students build robust error handling for tool call failures: network errors, invalid parameters, tool unavailability, timeout. They implement retry strategies (exponential backoff, retry with modified parameters), fallback alternatives (use different tool, skip step, ask user for help), and user-friendly error messages. They test failure scenarios systematically and document recovery paths. They add logging to track error patterns and success rates for each tool.

Dependencies:
* T21.G7.12: Build tool-use orchestration with sequential tool calls




ID: T21.G7.14
Topic: T21 – Chatbots & Prompting
Skill: Create evaluation metrics for prompt quality assessment
Description: Students develop quantitative and qualitative metrics to measure prompt effectiveness: accuracy (% correct answers on test set), relevance (response addresses the question), completeness (includes all requested information), format compliance (follows structure instructions), tone appropriateness. They build a test suite with 20+ diverse prompts and expected outputs, run evaluations automatically, and generate quality scores. They use metrics to compare prompt variations objectively.

Dependencies:
* T21.G6.12: Implement A/B testing to compare prompt variants




ID: T21.G7.15
Topic: T21 – Chatbots & Prompting
Skill: Analyze prompts for potential bias in outputs
Description: Students systematically test prompts for biased outputs across demographic dimensions (gender, race, age, culture), topic areas (politics, religion, social issues), and language patterns. They create test cases with role reversal (swapping gendered names, changing cultural context) and check for different responses. They identify bias sources: training data, prompt framing, default assumptions. They document bias patterns and severity. Example: testing if "Tell me about a successful scientist" shows gender bias in pronoun use or example selection.

Dependencies:
* T21.G7.14: Create evaluation metrics for prompt quality assessment




ID: T21.G7.16
Topic: T21 – Chatbots & Prompting
Skill: Implement bias mitigation strategies in prompt design
Description: Students apply strategies to reduce bias in chatbot outputs: neutral language in prompts, explicit diversity instructions ("Include examples from multiple cultures/genders"), bias-checking constraints ("Avoid stereotypes about..."), balanced framing. They implement bias detection in responses (flagging stereotypical language) and automatic reprompting with bias mitigation instructions when detected. They test effectiveness using their bias evaluation suite from G7.15.

Dependencies:
* T21.G7.15: Analyze prompts for potential bias in outputs




ID: T21.G7.17
Topic: T21 – Chatbots & Prompting
Skill: Implement rate limiting and error handling for production use
Description: Students build production-ready error handling: rate limiting (maximum requests per user/timeframe), quota management, API error handling (service unavailable, authentication failures), timeout handling, graceful degradation. They implement user-facing status messages, request queuing for high load, and fallback responses when the service is down. They test edge cases: rapid-fire requests, network failures mid-stream, quota exhaustion.

Dependencies:
* T21.G7.13: Implement error handling and retry logic for tool calls




ID: T21.G7.18
Topic: T21 – Chatbots & Prompting
Skill: Monitor and log chatbot usage for cost and performance analysis
Description: Students implement comprehensive logging: request/response tracking, token usage per request, response latency, error rates, user satisfaction ratings. They build analytics dashboards showing: cost trends, most expensive prompts, slowest requests, error patterns, usage by feature. They identify optimization opportunities (compress high-token prompts, cache common requests) and estimate cost for different usage levels. They implement cost alerts when spending exceeds thresholds.

Dependencies:
* T21.G7.17: Implement rate limiting and error handling for production use




ID: T21.G7.19
Topic: T21 – Chatbots & Prompting
Skill: Design prompts preventing common security vulnerabilities
Description: Students learn prompt injection vulnerabilities and defenses. They test attacks: users trying to override system instructions ("Ignore previous instructions and..."), extract sensitive data, generate harmful content, bypass filters. They implement defenses: input sanitization, instruction hierarchy enforcement (system > user), output filtering, harmful content detection. They build a security test suite with 10+ attack vectors and verify their chatbot resists each. They document the security model and limitations.

Dependencies:
* T21.G7.07: Implement instruction hierarchy in prompts (system, user, context)


----

## GRADE 8 SKILLS




ID: T21.G8.01
Topic: T21 – Chatbots & Prompting
Skill: Implement meta-prompting where AI generates its own prompts
Description: Students build systems where AI analyzes a high-level goal and generates optimized prompts to achieve it. They create a two-stage process: (1) meta-prompt asks AI to design an effective prompt for a specific task, (2) use the AI-generated prompt for the actual task. They compare human-written vs AI-generated prompts for effectiveness. They build a prompt improvement loop: AI generates prompt → test it → AI analyzes failures → AI generates improved version. They explore when meta-prompting helps vs adds unnecessary complexity.

Dependencies:
* T21.G7.01: Implement chain-of-thought prompting for complex reasoning tasks




ID: T21.G8.02
Topic: T21 – Chatbots & Prompting
Skill: Design automatic prompt optimization through feedback loops
Description: Students implement systems that automatically improve prompts based on performance feedback. They track success metrics (accuracy, user ratings, task completion), identify underperforming prompts, and systematically test variations. They implement A/B testing with automatic variant generation, measure comparative performance, and promote winning variants. They build optimization history tracking and rollback capability. They set up continuous improvement cycles: monitor → identify issues → generate alternatives → test → deploy.

Dependencies:
* T21.G8.01: Implement meta-prompting where AI generates its own prompts
* T21.G7.14: Create evaluation metrics for prompt quality assessment




ID: T21.G8.03
Topic: T21 – Chatbots & Prompting
Skill: Implement constitutional AI prompting with principle-based constraints
Description: Students design chatbots governed by explicit principles codified in prompts. They define a "constitution" of behavioral rules (helpfulness, harmlessness, honesty) and encode them as constraints the AI must follow. They implement principle prioritization for conflict resolution (when principles conflict, which takes precedence). They test edge cases where principles clash (being honest vs being kind) and verify the AI resolves them according to priority rules. They document the constitutional framework and its limitations.

Dependencies:
* T21.G7.16: Implement bias mitigation strategies in prompt design




ID: T21.G8.04
Topic: T21 – Chatbots & Prompting
Skill: Create retrieval-augmented generation (RAG) systems with vector databases
Description: Students build RAG systems that retrieve relevant information from a knowledge base before generating responses. They create a document collection, split it into chunks, generate embeddings (vector representations) for each chunk, and store in a vector database. When users ask questions, they: (1) convert question to vector, (2) find most similar document chunks, (3) include them in the prompt context, (4) generate answer grounded in retrieved information. They compare RAG responses to pure generation for accuracy and hallucination reduction.

Dependencies:
* T21.G7.09: Implement semantic similarity search for context retrieval




ID: T21.G8.05
Topic: T21 – Chatbots & Prompting
Skill: Implement hybrid search combining keyword and semantic retrieval
Description: Students enhance RAG systems by combining traditional keyword search (BM25, TF-IDF) with semantic vector search. They implement parallel retrieval: run both keyword and semantic search, combine results using weighted ranking or reciprocal rank fusion. They test on diverse queries showing when each method excels (keyword for exact terms/names, semantic for concepts/paraphrases). They build a hybrid system that adaptively weights methods based on query characteristics.

Dependencies:
* T21.G8.04: Create retrieval-augmented generation (RAG) systems with vector databases




ID: T21.G8.06
Topic: T21 – Chatbots & Prompting
Skill: Design prompt caching strategies to reduce latency and cost
Description: Students implement intelligent caching to avoid redundant API calls: cache identical prompts, recognize semantically similar prompts, cache partial prompts (system instructions) separately from dynamic content. They implement cache invalidation policies (time-based, usage-based), measure cache hit rates, and calculate cost savings. They handle cache staleness (when cached responses become outdated) and implement smart refresh strategies. They balance cache memory usage against API cost savings.

Dependencies:
* T21.G7.05: Implement prompt compression to reduce token usage
* T21.G7.18: Monitor and log chatbot usage for cost and performance analysis




ID: T21.G8.07
Topic: T21 – Chatbots & Prompting
Skill: Build streaming response handlers for real-time chat experiences
Description: Students implement production-quality streaming: display tokens as they arrive with smooth animation, handle partial sentences gracefully, update UI progressively without flicker, implement cancel-during-stream functionality. They handle streaming errors (connection drops mid-stream, partial responses), implement resume/retry logic, and provide seamless UX. They optimize rendering performance for long responses, add features like "copy partial response" and "pause stream." They compare streaming latency and UX across different network conditions.

Dependencies:
* T21.G7.17: Implement rate limiting and error handling for production use




ID: T21.G8.08
Topic: T21 – Chatbots & Prompting
Skill: Implement context window management for long conversations
Description: Students build systems to handle conversations exceeding the model's context window (token limit). They implement strategies: conversation summarization (periodically compress old messages), selective message retention (keep important messages, drop filler), sliding window (keep recent N messages), hierarchical summary (summaries of summaries). They track context usage in real-time, warn users approaching limits, and automatically apply compression when needed. They test that conversation coherence is maintained after compression.

Dependencies:
* T21.G6.09: Implement conversational memory with summarization for long contexts
* T21.G8.06: Design prompt caching strategies to reduce latency and cost




ID: T21.G8.09
Topic: T21 – Chatbots & Prompting
Skill: Create prompt ensembles combining multiple model outputs
Description: Students build ensemble systems that combine outputs from multiple AI calls for improved quality. They implement strategies: majority voting (for classification), averaging (for numeric outputs), best-of-N selection (generate N responses, use quality heuristic to pick best), mixture-of-experts (route different question types to specialized prompts). They measure ensemble accuracy vs single-model baseline, document quality-cost tradeoffs, and identify which strategies work best for different tasks.

Dependencies:
* T21.G6.07: Implement best-of-n sampling to select highest quality output
* T21.G7.02: Create self-consistency prompting with multiple reasoning paths




ID: T21.G8.10
Topic: T21 – Chatbots & Prompting
Skill: Implement output verification with fact-checking mechanisms
Description: Students build automated fact-checking for chatbot responses. They implement verification strategies: cross-reference with trusted sources (RAG with curated documents), consistency checking (ask same fact multiple ways, check agreement), confidence scoring (parse "I think" vs "definitely"), explicit source citation requirements. They flag low-confidence or unverifiable claims for review. They test on factual domains (history, science) and measure false-positive and false-negative rates.

Dependencies:
* T21.G8.04: Create retrieval-augmented generation (RAG) systems with vector databases
* T21.G8.05: Implement hybrid search combining keyword and semantic retrieval




ID: T21.G8.11
Topic: T21 – Chatbots & Prompting
Skill: Design systematic prompt debugging workflows
Description: Students create structured debugging processes for prompt failures: isolate the problem (which part of prompt causes issue), create minimal reproducing example, test hypotheses systematically (change one variable at a time), document findings, apply fixes, verify resolution. They build debugging tools: prompt diff viewer (compare working vs broken versions), variable isolation testing (test each prompt component separately), regression test suite (verify fixes don't break other cases). They practice on 5+ realistic debugging scenarios.

Dependencies:
* T21.G6.10: Debug prompts using systematic parameter isolation
* T21.G7.15: Analyze prompts for potential bias in outputs




ID: T21.G8.12
Topic: T21 – Chatbots & Prompting
Skill: Implement hallucination detection and mitigation strategies
Description: Students build systems to detect and reduce AI hallucinations (confident false statements). They implement detection methods: fact verification against knowledge base, consistency checking across multiple responses, confidence calibration (ask AI to rate certainty), source attribution (require citations). They apply mitigation: constrain responses to retrieved documents only, add "I don't know" instructions, temperature tuning for factual tasks. They measure hallucination rates before/after interventions on a test set with known facts.

Dependencies:
* T21.G8.10: Implement output verification with fact-checking mechanisms




ID: T21.G8.13
Topic: T21 – Chatbots & Prompting
Skill: Create adversarial test suites for robustness evaluation
Description: Students build comprehensive test suites to probe chatbot weaknesses: edge cases (very long/short inputs, special characters, multiple languages), adversarial inputs (prompt injections, jailbreak attempts, manipulation), domain boundaries (questions outside training data), ambiguous/contradictory requests. They automate testing, track failure modes, measure robustness scores, and prioritize fixes. They document attack vectors and defensive measures.

Dependencies:
* T21.G7.19: Design prompts preventing common security vulnerabilities
* T21.G8.11: Design systematic prompt debugging workflows




ID: T21.G8.14
Topic: T21 – Chatbots & Prompting
Skill: Implement multi-agent systems with specialized agent roles
Description: Students design systems where multiple AI agents collaborate, each with specialized roles. They create agent architectures: researcher (gathers information), analyzer (evaluates options), writer (creates content), critic (reviews quality). Each agent has distinct prompts, capabilities, and expertise. They build agent coordination: agents communicate by passing structured messages, maintain shared context, and work toward common goals. They test on complex tasks requiring diverse skills (research report, product analysis, creative projects).

Dependencies:
* T21.G7.12: Build tool-use orchestration with sequential tool calls




ID: T21.G8.14.01
Topic: T21 – Chatbots & Prompting
Skill: Design agent communication protocols and message passing
Description: Students create structured communication systems for multi-agent collaboration. They define message schemas (sender, recipient, message type, payload, metadata), implement message routing (direct, broadcast, subscription-based), and build message queues. They design protocols for common patterns: request-response, event notification, collaborative editing. They implement message logging for debugging and tracing agent interactions. They test communication reliability and handle message delivery failures.

Dependencies:
* T21.G8.14: Implement multi-agent systems with specialized agent roles




ID: T21.G8.15
Topic: T21 – Chatbots & Prompting
Skill: Create agent orchestration with task decomposition and delegation
Description: Students build orchestration systems where a "manager" agent decomposes complex tasks and delegates to specialist agents. The manager: analyzes task requirements, breaks into subtasks, assigns to appropriate agents, monitors progress, integrates results. They implement task dependencies (subtask B needs subtask A's output), parallel execution (independent subtasks run simultaneously), error handling (reassign failed tasks). They test on multi-step projects and measure efficiency gains from parallelization.

Dependencies:
* T21.G8.14: Implement multi-agent systems with specialized agent roles




ID: T21.G8.16
Topic: T21 – Chatbots & Prompting
Skill: Implement ReAct pattern (Reasoning and Acting) for agentic AI
Description: Students build ReAct agents that interleave reasoning (thinking about what to do) and acting (using tools). They implement the ReAct loop: (1) agent observes current state, (2) reasons about next action using chain-of-thought, (3) selects and executes tool/action, (4) observes result, (5) reasons about new state, (6) repeat until task complete. They trace ReAct execution showing thought-action-observation sequences. They test on tasks requiring multi-step tool use with adaptive planning.

Dependencies:
* T21.G7.12: Build tool-use orchestration with sequential tool calls
* T21.G8.15: Create agent orchestration with task decomposition and delegation




ID: T21.G8.17
Topic: T21 – Chatbots & Prompting
Skill: Build self-correction loops where agents review and improve outputs
Description: Students implement iterative refinement where agents critique and improve their own work. They create multi-stage pipelines: (1) agent generates initial response, (2) critic agent identifies flaws, (3) generator revises based on critique, (4) repeat until quality threshold met or max iterations reached. They implement quality scoring to decide when to stop iterating. They test on tasks where quality improves with revision (writing, code, analysis) and measure quality-vs-iteration tradeoffs.

Dependencies:
* T21.G8.16: Implement ReAct pattern (Reasoning and Acting) for agentic AI




ID: T21.G8.18
Topic: T21 – Chatbots & Prompting
Skill: Implement prompt versioning and A/B testing in production
Description: Students build production systems for managing prompt versions and testing variations. They implement: version control for prompts (track changes, rollback capability), A/B testing infrastructure (randomly assign users to variants, collect metrics), statistical significance testing, gradual rollout (expose new versions to increasing user percentages). They run real A/B tests comparing prompt variants, analyze results, and make data-driven deployment decisions. They document the testing methodology and results.

Dependencies:
* T21.G6.12: Implement A/B testing to compare prompt variants
* T21.G7.18: Monitor and log chatbot usage for cost and performance analysis




ID: T21.G8.19
Topic: T21 – Chatbots & Prompting
Skill: Design fallback strategies for chatbot failures
Description: Students implement comprehensive fallback mechanisms when primary systems fail. They create fallback chains: primary AI → simplified prompt → cached response → static helpful message → escalation to human. They implement failure detection (timeouts, error rates, quality checks), automatic fallback triggering, and recovery monitoring (when to retry primary system). They test all failure modes and verify graceful degradation. They balance user experience against cost/complexity of fallback layers.

Dependencies:
* T21.G7.17: Implement rate limiting and error handling for production use
* T21.G8.13: Create adversarial test suites for robustness evaluation




ID: T21.G8.20
Topic: T21 – Chatbots & Prompting
Skill: Create human-in-the-loop workflows with review and approval gates
Description: Students design systems where humans review and approve AI outputs before delivery. They implement review queues (flag responses needing human review based on confidence, content type, user role), approval workflows (submit → review → approve/reject/edit → deliver), and feedback loops (human edits train future AI behavior). They build reviewer dashboards showing pending items, approval rates, common issues. They measure impact of human review on quality and identify which outputs most benefit from review.

Dependencies:
* T21.G8.17: Build self-correction loops where agents review and improve outputs
* T21.G8.19: Design fallback strategies for chatbot failures




ID: T21.G8.21
Topic: T21 – Chatbots & Prompting
Skill: Implement comprehensive observability for production chatbot systems
Description: Students build complete observability: distributed tracing (track requests across multiple AI calls, tools, agents), structured logging (searchable, filterable logs with context), metrics dashboards (latency, error rates, token usage, cost), alerting (automated notifications for anomalies), and incident response playbooks. They instrument their chatbot to track the full request lifecycle, diagnose issues from logs, and optimize based on metrics. They simulate production issues and use observability tools to debug them.

Dependencies:
* T21.G7.18: Monitor and log chatbot usage for cost and performance analysis
* T21.G8.07: Build streaming response handlers for real-time chat experiences




ID: T21.G8.22
Topic: T21 – Chatbots & Prompting
Skill: Design ethical deployment frameworks for chatbot applications
Description: Students create comprehensive ethical frameworks for deploying AI chatbots. They address: informed consent (users know they're talking to AI), data privacy (handling user information responsibly), fairness (bias testing and mitigation), transparency (explaining AI limitations), accountability (human oversight and appeals process), safety (preventing harmful outputs). They implement ethical review checklists, conduct stakeholder impact analysis, and create incident response plans for ethical violations. They document the ethical framework and justify design choices.

Dependencies:
* T21.G8.03: Implement constitutional AI prompting with principle-based constraints
* T21.G8.13: Create adversarial test suites for robustness evaluation
* T21.G8.20: Create human-in-the-loop workflows with review and approval gates
