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
