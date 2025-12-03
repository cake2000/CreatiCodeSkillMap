# T21 – Chatbots & Prompting: Optimized Grade 4 & 5

**Generated:** 2025-12-02
**Total Skills:** 29 (15 G4 + 14 G5)
**Focus:** Multi-turn conversations, few-shot prompting, voice integration, advanced prompt patterns, error handling

---

## Grade 4 (G4): Multi-Turn Conversations & Systematic Testing (15 skills)

### T21.G4.01
**ID:** T21.G4.01
**Topic:** T21 – Chatbots & Prompting
**Skill:** Build a conversational bot that asks user 3 questions and remembers answers

**Description:** Students create a stateful chatbot that gathers information across multiple turns and uses it in a final response. Program flow: Turn 1: `say [What's your name?]` → `ask and wait` → store in `userName` variable → ChatGPT request using continue mode. Turn 2: `say [What's your favorite subject?]` → store in `favSubject` → ChatGPT processes. Turn 3: `say [What do you want to learn about (favSubject)?]` → store in `topic` → ChatGPT processes. Turn 4: ChatGPT generates personalized response using all three pieces of information (name, subject, topic). Students ensure context maintains throughout by using "continue" mode and optionally including gathered info in prompts. Assessment: Working 4-turn conversation where bot demonstrates knowledge of all previously gathered information in final response, such as "Emma, let me tell you about space science..."

**Dependencies:**
* T21.G3.05: Build a 3-turn conversation using "continue" session mode
* T21.G3.09: Build a simple chatbot interface with user input and ChatGPT response
* T09.G4.03: Use multiple variables for different purposes

---

### T21.G4.02
**ID:** T21.G4.02
**Topic:** T21 – Chatbots & Prompting
**Skill:** Create a quiz bot that generates questions and checks answers

**Description:** Students build an interactive quiz bot using ChatGPT to generate questions and evaluate answers. Program structure: (1) System prompt: "You are a quiz master. Ask one trivia question at a time about [topic]." (2) ChatGPT generates question → display question. (3) User inputs answer via `ask and wait`. (4) Send user's answer to ChatGPT with prompt "Is this answer correct: [user answer]? Say only YES or NO." (5) Check ChatGPT response, increment score if YES. (6) Repeat for 3-5 questions. (7) Display final score. Students use variables for score tracking, question count, and responses. They test quiz bot with different topics (science, math, history). Assessment: Working quiz bot that generates 3 questions like "What planet is closest to the sun?", accepts user input, uses ChatGPT to evaluate if answer is correct, maintains score, and displays final result.

**Dependencies:**
* T21.G3.06: Use the system prompt block to set ChatGPT role/personality
* T21.G3.09: Build a simple chatbot interface with user input and ChatGPT response
* T08.G4.11: Build a program that uses if-then-else

---

### T21.G4.03
**ID:** T21.G4.03
**Topic:** T21 – Chatbots & Prompting
**Skill:** Use streaming mode to display ChatGPT response word-by-word as it generates

**Description:** Students learn the difference between "waiting" mode (shows complete response at once) and "streaming" mode (shows response progressively as it's generated, like typing effect). They modify existing ChatGPT request blocks to use `mode [streaming]` instead of `mode [waiting]`. With streaming, they add a loop that continuously checks the response variable and updates display: `repeat until <(chatGPT status) = [complete]>` → `display current (response) content` → `wait (0.1) seconds`. Students observe streaming creates a more dynamic, responsive user experience. They compare user perception of waiting mode (seems to "freeze" then show all text) vs streaming mode (shows progress). Assessment: Working program that displays ChatGPT response in streaming mode with progressive text reveal, demonstrating the visual difference between both modes.

**Dependencies:**
* T21.G3.02: Create a simple ChatGPT request with one prompt and display result
* T07.G4.14: Use repeat-until loop with a condition

---

### T21.G4.04
**ID:** T21.G4.04
**Topic:** T21 – Chatbots & Prompting
**Skill:** Implement ChatGPT cancel request functionality

**Description:** Students learn to use the `OpenAI ChatGPT: cancel request` block to stop ongoing ChatGPT requests. This is important for long responses or when user wants to interrupt. They create a program with two sprites: Sprite 1 makes a ChatGPT request (long response like "Write a detailed story about adventures..."), Sprite 2 listens for spacebar press and broadcasts "cancel" message. When "cancel" received, use `cancel request` block. Students test by starting a request and pressing spacebar mid-response to stop it. They observe that canceled requests don't complete and response variable remains unchanged from before request. Assessment: Demonstrate working cancel functionality that interrupts ChatGPT request when triggered, such as a program that starts generating a long story and successfully stops when spacebar is pressed mid-generation with a "Press SPACE to cancel" instruction.

**Dependencies:**
* T21.G4.03: Use streaming mode to display ChatGPT response word-by-word as it generates
* T06.G4.01: Use broadcast to send a message
* T08.G4.14: Use keyboard sensing to detect specific key presses

---

### T21.G4.05
**ID:** T21.G4.05
**Topic:** T21 – Chatbots & Prompting
**Skill:** Build a branching conversation bot with 2 choice points

**Description:** Students create an interactive narrative or decision-tree chatbot where user choices determine conversation path. Structure: Turn 1: Bot offers choice A or B (e.g., "Do you want to hear a story about [A] space or [B] ocean?"). User responds → store choice. Turn 2: Bot continues based on choice (different ChatGPT prompt based on A vs B). Within chosen path, offer second choice (e.g., if space: "About [A] planets or [B] rockets?"). Use nested if-then-else blocks to handle choice routing: `if <(choice1) = [space]> then [follow space path] else [follow ocean path]`. Each path sends different prompts to ChatGPT with "continue" mode to maintain path context. Assessment: Working branching bot with at least 4 different possible conversation paths (2 choices × 2 sub-choices), such as an adventure bot with "Forest or Beach?" then "Day or Night?" or "Swim or Explore?" where each combination produces unique ChatGPT story path.

**Dependencies:**
* T21.G4.01: Build a conversational bot that asks user 3 questions and remembers answers
* T08.G4.11: Build a program that uses if-then-else
* T08.G4.22: Combine multiple conditions with AND

---

### T21.G4.06
**ID:** T21.G4.06
**Topic:** T21 – Chatbots & Prompting
**Skill:** Test ChatGPT bot with 5 diverse inputs and document unexpected results

**Description:** Students develop systematic testing skills by creating a test plan for their chatbot and documenting results. They choose one of their previous ChatGPT bots and test with 5 diverse input types: (1) Normal expected input, (2) Very short input (1-2 words), (3) Very long input (50+ words), (4) Off-topic input, (5) Nonsense/gibberish input. For each test, they document: Input text, Expected behavior, Actual ChatGPT response, Pass/Fail, Notes about unexpected behavior. Students identify which inputs caused problems (gibberish, off-topic) and propose improvements (add input validation, improve system prompt). Assessment: Complete test documentation for all 5 input types with analysis of unexpected results, such as testing a math homework helper bot with "Explain fractions" (works well), "help" (too vague), 200-word rambling question (gets confused), "Tell me a joke" (off-topic but responds), and "asdfghjkl" (attempts to interpret gibberish), with documented proposed fixes.

**Dependencies:**
* T21.G3.09: Build a simple chatbot interface with user input and ChatGPT response
* T21.G3.11: Debug a ChatGPT conversation that loses context or gives wrong response

---

### T21.G4.07
**ID:** T21.G4.07
**Topic:** T21 – Chatbots & Prompting
**Skill:** Add input validation to check user prompts before sending to ChatGPT

**Description:** Students improve chatbot robustness by adding validation checks before sending user input to ChatGPT. They implement three validation rules: (1) Check input is not empty: `if <(length of (userInput)) = [0]> then [say [Please type something]]`. (2) Check input meets minimum length: `if <(length of (userInput)) < [3]> then [say [Please say more]]`. (3) Check for inappropriate content keywords: `if <(userInput) contains [bad word]> then [say [Please ask appropriately]]`. Only if all validations pass, send to ChatGPT. Students test with invalid inputs to verify validation works, then with valid inputs to confirm requests succeed. Assessment: Working chatbot with at least 2 validation checks that provide helpful error messages and only send valid inputs to ChatGPT, such as rejecting empty input ("Please type a question") and single character input ("Please write at least 3 characters") while accepting and processing valid inputs normally.

**Dependencies:**
* T21.G4.06: Test ChatGPT bot with 5 diverse inputs and document unexpected results
* T08.G4.20: Use string operations (length, contains, letter X of)
* T08.G4.21: Combine multiple conditions with OR

---

### T21.G4.08
**ID:** T21.G4.08
**Topic:** T21 – Chatbots & Prompting
**Skill:** Create a topic-specific expert bot using detailed system prompt

**Description:** Students design a specialized ChatGPT bot for one specific topic using a comprehensive system prompt that establishes expertise, tone, and behavior rules. They choose a topic (e.g., Math Tutor, Science Explainer, Story Coach, Coding Helper) and write detailed system prompt including: (1) Role: "You are an expert [topic] tutor for grade 4-5 students", (2) Expertise: "You specialize in [specific areas within topic]", (3) Tone: "You are encouraging, patient, and use age-appropriate language", (4) Behavior rules: "Always ask if student understands before moving on", "Use examples from everyday life", "Never give complete answers, guide with hints". Students test their expert bot with 5 topic-related questions and verify responses match system prompt specifications. Assessment: Working specialized bot with comprehensive system prompt that demonstrably affects response quality and style across multiple test queries, such as a Math Tutor bot with system prompt specifying "Guide students to discover answers, don't solve for them" and "Use real-world examples like pizza slices and toys" that consistently follows these rules.

**Dependencies:**
* T21.G3.06: Use the system prompt block to set ChatGPT role/personality
* T21.G3.08: Compare ChatGPT responses with different system prompts for same question

---

### T21.G4.09
**ID:** T21.G4.09
**Topic:** T21 – Chatbots & Prompting
**Skill:** Chain two ChatGPT calls where output of first becomes input to second

**Description:** Students create a two-stage ChatGPT pipeline where the response from Call 1 is automatically used as the prompt (or part of prompt) for Call 2. Example pipeline: Call 1: "Write a sentence about robots" → stores response in `sentence1`. Call 2: "Translate this to Spanish: (sentence1)" → stores response in `translation`. Display both. Another example: Call 1: "Generate a random animal name" → stores in `animal`. Call 2: "Write 3 fun facts about (animal)" → stores in `facts`. Students create at least two different two-stage pipelines, each demonstrating how first response feeds second request. They use variables to pass data between stages and "new chat" for Call 2 if it should be independent context. Assessment: Working two-stage pipeline where Call 2 demonstrably uses Call 1's output, such as Stage 1 asking ChatGPT "Give me a country name" → gets "France", then Stage 2 asks "What is the capital of (country variable)?" → gets "Paris", demonstrating data flow between stages.

**Dependencies:**
* T21.G3.02: Create a simple ChatGPT request with one prompt and display result
* T09.G4.06: Pass variable values between different parts of a program

---

### T21.G4.10
**ID:** T21.G4.10
**Topic:** T21 – Chatbots & Prompting
**Skill:** Build a chatbot that maintains conversation history in a list variable

**Description:** Students create a chatbot with visible conversation history using list variables. They initialize two lists: `userMessages` and `botResponses`. In conversation loop: (1) User types input → add to `userMessages` list, (2) Send to ChatGPT with "continue" mode → store response, (3) Add response to `botResponses` list, (4) Display both lists showing complete conversation history. Students implement "show history" button that displays all paired messages (userMessages[1] with botResponses[1], etc.) and "clear history" button that deletes all list items and starts new chat. They test that history persists across multiple turns and can be reviewed. Assessment: Working chatbot where users can see scrolling conversation history showing all previous questions and answers, with ability to review past exchanges and clear history to start fresh.

**Dependencies:**
* T21.G4.01: Build a conversational bot that asks user 3 questions and remembers answers
* T10.G4.06: Add items to a list based on user input

---

### T21.G4.11
**ID:** T21.G4.11
**Topic:** T21 – Chatbots & Prompting
**Skill:** Compare responses from different bot slots with same prompt

**Description:** Students conduct a systematic experiment comparing how different ChatGPT bot slots respond to identical prompts when configured differently. Setup: Bot 1 with system prompt "You are enthusiastic and use exclamation marks", Bot 2 with system prompt "You are formal and academic", Bot 3 with no system prompt (default), Bot 4 with "You are humorous and tell jokes". Test prompt: "Explain what gravity is" sent to all 4 bots. Students document: (1) Each bot's response, (2) Differences in tone, vocabulary, and style, (3) Which bot configuration is best for which audience/purpose. They create a comparison table or side-by-side display showing all four responses. Assessment: Successfully generate 4 different styled responses to same prompt using 4 bot configurations and document observed differences with analysis, such as sending "What is photosynthesis?" to all 4 bots with different personalities and analyzing which version is best for young children (enthusiastic), high school students (academic), casual learning (default), and engagement (humorous).

**Dependencies:**
* T21.G3.07: Switch between different ChatGPT bots (1, 2, 3, 4) for separate conversations
* T21.G3.08: Compare ChatGPT responses with different system prompts for same question

---

### T21.G4.12
**ID:** T21.G4.12
**Topic:** T21 – Chatbots & Prompting
**Skill:** Use few-shot prompting by including examples in the prompt

**Description:** Students learn the powerful technique of few-shot prompting - providing examples in the prompt to guide ChatGPT's response format and style. Instead of just describing what they want, they SHOW what they want through examples. Prompt structure: "Here are examples of what I want: Example 1: Input: apple, Output: red fruit. Example 2: Input: banana, Output: yellow fruit. Now do this: Input: grape, Output: ?" Students compare zero-shot (no examples) vs few-shot (2-3 examples) responses for 4 tasks: (1) formatting data, (2) classification, (3) translation style, (4) creative writing tone. They document how examples improve response quality and consistency. Assessment: Demonstrate improved output alignment using few-shot prompting in 3 of 4 tasks, such as comparing zero-shot "Convert temperatures" (inconsistent formats) vs few-shot "Example: 100F → 100°F is 37.8°C. Example: 50F → 50°F is 10°C. Now: 75F →" (consistent format), documenting that examples produce more reliable formatting.

**Dependencies:**
* T21.G3.10: Create a prompt that requests specific output format (list, steps, short answer)
* T21.G4.08: Create a topic-specific expert bot using detailed system prompt

---

### T21.G4.13
**ID:** T21.G4.13
**Topic:** T21 – Chatbots & Prompting
**Skill:** Add constraints to prompts to limit chatbot response scope

**Description:** Students learn to control ChatGPT responses by adding explicit constraints. Types of constraints: (1) Length: "Answer in exactly 2 sentences" or "Use no more than 50 words", (2) Content: "Only mention facts from the story I provided" or "Do not include opinions", (3) Format: "Respond only with YES or NO" or "Start every sentence with a verb", (4) Scope: "Only discuss the first chapter" or "Focus only on the main character." Students test how well ChatGPT follows different constraint types. They create a chatbot that enforces constraints: user specifies topic + constraints, bot includes constraints in prompt, verify response follows constraints. This builds understanding of prompt engineering for controlled outputs. Assessment: Successfully implement and verify 4 different constraint types, such as creating prompt "Tell me about dogs in exactly 3 bullet points, using only positive words, each starting with 'Dogs'" and verifying ChatGPT response follows all three constraints.

**Dependencies:**
* T21.G4.12: Use few-shot prompting by including examples in the prompt
* T21.G3.10: Create a prompt that requests specific output format (list, steps, short answer)

---

### T21.G4.14
**ID:** T21.G4.14
**Topic:** T21 – Chatbots & Prompting
**Skill:** Recognize and handle basic prompt safety issues (private info, harmful requests)

**Description:** Students learn to implement basic safety checks before sending prompts to ChatGPT. Safety issues to detect: (1) Personal information: names, addresses, phone numbers, emails - warn user "This might contain personal info", (2) Potentially harmful requests: "how to hurt", "how to steal" patterns - block with "I can't help with that", (3) Attempts to bypass chatbot rules: "ignore your rules", "pretend you're not an AI" - ignore the override attempt. Students build a simple safety filter using string detection (contains keyword checks) that runs BEFORE sending to ChatGPT. They test with 10 inputs: 5 safe (pass through) and 5 unsafe (blocked/warned). This introduces security thinking for AI applications. Assessment: Safety filter correctly identifies 8 of 10 test cases, such as blocking "Tell me how to hack my friend's account" (harmful) but allowing "Tell me about cybersecurity careers" (safe), and warning on "My email is john@email.com, tell me..." (personal info).

**Dependencies:**
* T21.G4.07: Add input validation to check user prompts before sending to ChatGPT
* T21.GK.07: Sort pictures into "Safe to Tell Chatbot" vs "Keep Private" boxes

---

### T21.G4.15
**ID:** T21.G4.15
**Topic:** T21 – Chatbots & Prompting
**Skill:** Detect harmful content in chatbot responses and handle appropriately

**Description:** Students learn to review ChatGPT responses for inappropriate content before displaying to users. They implement post-generation content checking by examining response text for: (1) Profanity or inappropriate language (keyword list), (2) Personal information that ChatGPT might have inadvertently included, (3) Harmful advice (violence, dangerous activities), (4) Factual errors that could be harmful (medical misinformation). If problematic content detected, students implement fallback actions: regenerate with modified prompt adding safety constraints, display generic safe response ("I can't help with that, let's try a different topic"), or alert supervising adult. Students test with edge cases that might produce problematic responses. Assessment: Working content filter that identifies 4 out of 5 problematic responses and implements appropriate fallback actions, such as detecting when a response includes potentially harmful advice and regenerating with additional safety constraints like "Only provide safe, age-appropriate information suitable for 4th graders."

**Dependencies:**
* T21.G4.14: Recognize and handle basic prompt safety issues (private info, harmful requests)
* T08.G4.20: Use string operations (length, contains, letter X of)
* T21.G2.09: Identify when chatbot response seems wrong or made-up (hallucination awareness)

---

## Grade 5 (G5): Voice Integration & Advanced Prompting (14 skills)

### T21.G5.01
**ID:** T21.G5.01
**Topic:** T21 – Chatbots & Prompting
**Skill:** Integrate speech recognition to accept voice input for ChatGPT

**Description:** Students create a voice-enabled chatbot using CreatiCode's speech recognition blocks combined with ChatGPT. Program flow: (1) `start recognizing speech in [English] record as [SOUNDNAME]` - activates microphone and optionally records audio, (2) Wait for speech input (user speaks), (3) `set [userInput] to (text from speech)` - captures transcribed text, (4) Display captured text: `say (userInput)` to confirm, (5) `OpenAI ChatGPT: request (userInput) result [response]` - send to ChatGPT, (6) Display response, (7) `end speech recognition`. Students test with various spoken inputs and observe speech-to-text accuracy. They add error handling for empty/unclear speech input. Assessment: Working voice-to-chatbot pipeline that accepts spoken input, transcribes it, sends to ChatGPT, and displays response, such as speaking "Tell me about dolphins," which gets transcribed to text, sent to ChatGPT, and displays response about dolphins, tested with multiple spoken questions to verify consistency.

**Dependencies:**
* T21.G4.01: Build a conversational bot that asks user 3 questions and remembers answers
* T09.G5.01: Use a variable to store text values

---

### T21.G5.02
**ID:** T21.G5.02
**Topic:** T21 – Chatbots & Prompting
**Skill:** Add text-to-speech output to speak ChatGPT responses aloud

**Description:** Students create a fully voice-interactive chatbot by adding spoken output using `say [TEXT] in [LANGUAGE] as [VOICETYPE] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO)` block. After ChatGPT generates response, instead of displaying text only, the bot speaks it aloud. Program flow: (1) Get ChatGPT response in variable `response`, (2) `say (response) in [English] as [default voice] speed [100] pitch [100] volume [100]` - speaks the response. Students experiment with voice parameters: different voice types (Male, Female, Male2, Female2, Boy, Girl), speeds (50-150%), pitches (50-150%), volumes (0-100%). They create personality-matched voices (friendly teacher = normal speed/pitch, excited scientist = faster speed/higher pitch, calm storyteller = slower/lower). Assessment: Working chatbot that speaks ChatGPT responses aloud with at least one customized voice configuration, such as a storyteller bot that receives ChatGPT story response and speaks it aloud with slow speed (80%) and slightly lower pitch (90%) for calm narrative effect.

**Dependencies:**
* T21.G5.01: Integrate speech recognition to accept voice input for ChatGPT
* T21.G3.06: Use the system prompt block to set ChatGPT role/personality

---

### T21.G5.03
**ID:** T21.G5.03
**Topic:** T21 – Chatbots & Prompting
**Skill:** Build a fully voice-interactive chatbot (speech in, speech out)

**Description:** Students combine speech recognition input with text-to-speech output to create a completely voice-based ChatGPT interaction (no typing or reading required). Complete program flow: (1) Bot speaks: "What would you like to know?" using text-to-speech, (2) `start recognizing speech`, (3) User speaks question, (4) Capture with `text from speech` → store in variable, (5) Send to ChatGPT with "continue" mode, (6) Speak ChatGPT response aloud using `say` block, (7) `end speech recognition`, (8) Loop back to step 1. Students add conversation indicators (visual animation or sound beep when listening vs thinking vs speaking). They test complete voice conversation: speak question → wait for spoken response → speak follow-up → hear follow-up response. Assessment: Working hands-free voice chatbot that accepts spoken input and provides spoken output for multi-turn conversation, such as a voice assistant that says "Ask me anything" aloud, listens for spoken question, sends to ChatGPT, speaks answer aloud, and repeats for continuous conversation - all without typing or reading text.

**Dependencies:**
* T21.G5.01: Integrate speech recognition to accept voice input for ChatGPT
* T21.G5.02: Add text-to-speech output to speak ChatGPT responses aloud
* T07.G5.01: Use forever loop with embedded conditional logic

---

### T21.G5.04
**ID:** T21.G5.04
**Topic:** T21 – Chatbots & Prompting
**Skill:** Use LLM model blocks to compare small vs large model responses

**Description:** Students experiment with CreatiCode's alternative LLM blocks: `LLM model [small/large] request [PROMPT] result [VARIABLE] mode [MODE] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE]`. They compare performance and quality differences between small and large models. Test protocol: Same prompt sent to both models: "Explain quantum physics in simple terms." Bot 1: `LLM model [small] request [prompt]` → store response1. Bot 2: `LLM model [large] request [prompt]` → store response2. Students document differences: response time (small is faster), response quality (large may be more detailed), response accuracy (large generally better). They test 3 different prompt types (simple fact question, creative writing, complex explanation) and note which model performs better for each type. Assessment: Working comparison program testing both LLM models with analysis of when to use each, such as testing "Write a creative story about robots" with both models, finding small model gives shorter simpler story faster (good for quick responses) while large model gives more detailed engaging story (good for quality content), with documented findings.

**Dependencies:**
* T21.G3.03: Test the same prompt with different temperature values
* T21.G4.11: Compare responses from different bot slots with same prompt

---

### T21.G5.05
**ID:** T21.G5.05
**Topic:** T21 – Chatbots & Prompting
**Skill:** Set system instructions for LLM models using dedicated block

**Description:** Students learn to use `LLM set system instruction [TEXT] for model [small/large]` block to configure LLM model behavior separately from OpenAI ChatGPT bots. Unlike ChatGPT system requests, LLM system instructions persist across all subsequent requests to that model until changed. Program: (1) `LLM set system instruction [You are a helpful coding tutor] for model [small]`, (2) Make multiple LLM requests - all follow system instruction, (3) Change system instruction: `LLM set system instruction [You are a creative storyteller] for model [small]`, (4) Make more requests - now follow new instruction. Students compare this persistent system instruction approach vs ChatGPT's per-conversation system prompts. Assessment: Demonstrate LLM system instructions affect multiple subsequent requests and can be updated to change behavior, such as setting LLM small model system instruction to "Answer all questions like a pirate," making 3 different requests (all respond in pirate style), then changing to "Answer all questions like a scientist" and making 3 more requests (all now respond scientifically).

**Dependencies:**
* T21.G5.04: Use LLM model blocks to compare small vs large model responses
* T21.G3.06: Use the system prompt block to set ChatGPT role/personality

---

### T21.G5.06
**ID:** T21.G5.06
**Topic:** T21 – Chatbots & Prompting
**Skill:** Use sentence analysis block to parse natural language input

**Description:** Students experiment with CreatiCode's NLP block: `analyze sentence [SENTENCE] and write into table [TABLENAME]`. This block parses sentences into grammatical components (subject, verb, object, modifiers) and stores results in a table variable. Program: (1) Create table variable `sentenceData`, (2) Get user input: "The quick brown fox jumps over the lazy dog", (3) `analyze sentence (userInput) and write into table [sentenceData]`, (4) Display table showing parsed components. Students examine the table structure to see identified parts of speech, subjects, verbs, etc. They test with 5 different sentence types (simple, compound, question, command) and observe parsing results. Use cases: Input validation, intent detection, extracting key information before sending to ChatGPT. Assessment: Working program that parses sentences into table and displays grammatical components, such as a "sentence analyzer" that accepts input "I love playing basketball," parses it to identify subject (I), verb (love), object (playing basketball), and displays analysis in readable format.

**Dependencies:**
* T21.G4.07: Add input validation to check user prompts before sending to ChatGPT
* T12.G5.01: Create a table with specific columns and data types

---

### T21.G5.07
**ID:** T21.G5.07
**Topic:** T21 – Chatbots & Prompting
**Skill:** Extract keywords from user input to customize ChatGPT prompts

**Description:** Students build a smart chatbot that analyzes user input using sentence parsing, extracts key information, and uses it to construct optimized ChatGPT prompts. Program flow: (1) User inputs: "I want to learn about dinosaurs", (2) Parse sentence to extract main topic ("dinosaurs"), (3) Construct enhanced ChatGPT prompt using template: "You are an expert on (topic). Explain (topic) in an engaging way for 5th graders. Include 3 interesting facts.", (4) Send enhanced prompt to ChatGPT. Students use string operations and parsed sentence data to identify and extract: topics (nouns), actions (verbs), descriptors (adjectives). They compare results: direct user input vs enhanced constructed prompt. Assessment: Working chatbot that extracts keywords from natural user input and generates improved prompts, such as when user says "Tell me something cool about space," bot extracts "space" as topic and "cool" as style indicator, constructs prompt "You are a space expert. Tell fascinating facts about space that 5th graders would find amazing," resulting in better response than sending user's casual input directly.

**Dependencies:**
* T21.G5.06: Use sentence analysis block to parse natural language input
* T21.G3.10: Create a prompt that requests specific output format (list, steps, short answer)

---

### T21.G5.08
**ID:** T21.G5.08
**Topic:** T21 – Chatbots & Prompting
**Skill:** Build a context-aware chatbot that references previous turns

**Description:** Students create an advanced conversational bot that explicitly references information from previous conversation turns by tracking conversation state. Unlike simply using "continue" mode (which maintains implicit context), this bot explicitly recalls and mentions previous exchanges. Implementation: Maintain lists of previous questions and answers, when generating new ChatGPT prompt, include relevant previous context: "Earlier you told me about [previous topic]. Now I want to know [new question]." Example: Turn 1: User asks about dogs → store topic="dogs". Turn 2: User asks "What do they eat?" → construct prompt "Earlier we discussed dogs. What do dogs eat?" Students implement context memory using variables/lists and demonstrate that explicitly including context in prompts produces more coherent responses. Assessment: Bot explicitly references previous turn content in new prompts and displays improved contextual understanding, such as Turn 1: "Tell me about Mars," Turn 2: User asks "How far is it?", bot doesn't just send "How far is it?" but constructs "We just talked about Mars. How far is Mars from Earth?" - showing explicit context management.

**Dependencies:**
* T21.G4.10: Build a chatbot that maintains conversation history in a list variable
* T21.G3.05: Build a 3-turn conversation using "continue" session mode

---

### T21.G5.09
**ID:** T21.G5.09
**Topic:** T21 – Chatbots & Prompting
**Skill:** Implement temperature optimization for different task types

**Description:** Students systematically determine optimal temperature settings for different ChatGPT task categories through experimentation. They test 5 task types: (1) Factual Q&A (test temps 0.1-0.5), (2) Creative writing (test temps 0.7-1.0), (3) Code generation (test temps 0.2-0.5), (4) Brainstorming (test temps 0.8-1.2), (5) Summarization (test temps 0.3-0.6). For each task type, students: run same prompt at 3 different temperatures, evaluate output quality using criteria (accuracy, creativity, usefulness), document optimal temperature. They create a "temperature guide" table showing recommended settings for each task type. Students then build a smart chatbot that automatically sets temperature based on detected task type. Assessment: Complete temperature optimization study with documented findings and implementation of task-based temperature selection, such as discovering factual questions work best at temp=0.3 (consistent accurate answers), creative stories best at temp=0.9 (varied imaginative), and building a bot that detects "explain" vs "write story" and adjusts temperature automatically.

**Dependencies:**
* T21.G3.03: Test the same prompt with different temperature values
* T21.G5.07: Extract keywords from user input to customize ChatGPT prompts

---

### T21.G5.10
**ID:** T21.G5.10
**Topic:** T21 – Chatbots & Prompting
**Skill:** Create a multi-bot system where different bots handle different topics

**Description:** Students build a sophisticated chatbot system that routes user queries to specialized bots based on topic detection. System architecture: Main dispatcher bot analyzes user input to detect topic category (math, science, creative writing, coding, general), then selects appropriate specialized bot (1-4). Each bot has distinct system prompt optimizing it for its domain. Implementation: (1) User asks question, (2) Analyze input for keywords (math words → bot 1, science words → bot 2, story words → bot 3, code words → bot 4, default → bot 1), (3) `select ChatGPT bot [detected number]`, (4) Send request to selected bot, (5) Display response with label showing which expert answered. Students define keyword lists for each category and implement routing logic. Assessment: Working multi-bot system that correctly routes at least 80% of test queries to appropriate specialized bot, such as "What's 25 times 4?" → system detects math keywords, routes to math tutor bot (bot 1); "Write a poem about autumn" → detects creative writing, routes to story bot (bot 3), with each bot responding in its specialized style.

**Dependencies:**
* T21.G3.07: Switch between different ChatGPT bots (1, 2, 3, 4) for separate conversations
* T21.G4.08: Create a topic-specific expert bot using detailed system prompt
* T21.G5.07: Extract keywords from user input to customize ChatGPT prompts

---

### T21.G5.11
**ID:** T21.G5.11
**Topic:** T21 – Chatbots & Prompting
**Skill:** Implement error handling for ChatGPT API failures and timeouts

**Description:** Students add robust error handling to chatbot programs to gracefully manage API failures, timeouts, and errors. They implement try-catch patterns using conditional checks: (1) Before request: check internet connection indicator, (2) After request: check if response variable is empty or contains error message, (3) Timeout handling: add timer that cancels request if it takes >30 seconds using `OpenAI ChatGPT: cancel request`, (4) Display user-friendly error messages: "Sorry, I couldn't connect to the AI. Please try again." Students create test scenarios for each error type: disconnect internet (connection failure), send extremely long prompt (timeout), repeatedly make requests (rate limiting). They ensure chatbot remains functional and informative even when requests fail. Assessment: Working chatbot with at least 3 error handling mechanisms that provide clear feedback and recovery options, such as detecting when ChatGPT request fails, displaying "Oops, something went wrong connecting to AI. Let's try again!" instead of freezing, providing "Retry" button, and logging error type for debugging.

**Dependencies:**
* T21.G4.04: Implement ChatGPT cancel request functionality
* T21.G4.06: Test ChatGPT bot with 5 diverse inputs and document unexpected results
* T08.G5.16: Use try-catch or error checking patterns

---

### T21.G5.12
**ID:** T21.G5.12
**Topic:** T21 – Chatbots & Prompting
**Skill:** Build prompts using chain-of-thought pattern for complex reasoning

**Description:** Students learn to use chain-of-thought (CoT) prompting to improve ChatGPT's reasoning on complex problems. Instead of asking for just the answer, they prompt ChatGPT to show its thinking step-by-step. Prompt pattern: "Solve this problem step by step, showing your reasoning at each stage before giving the final answer: [problem]." Students compare direct prompts vs CoT prompts for 4 problem types: (1) Math word problems, (2) Logic puzzles, (3) Multi-step questions, (4) Cause-and-effect analysis. They document accuracy improvements when using CoT. Advanced: Combine with few-shot by providing example reasoning chains. Assessment: Demonstrate improved accuracy on 3 of 4 problem types using chain-of-thought prompting, such as for problem "If a train travels 60 miles in 2 hours, how long to travel 150 miles?" where direct prompt gets wrong answer but CoT prompt "Show your reasoning step by step" produces: "Step 1: Speed = 60÷2 = 30 mph. Step 2: Time = 150÷30 = 5 hours. Answer: 5 hours." (correct).

**Dependencies:**
* T21.G4.12: Use few-shot prompting by including examples in the prompt
* T21.G5.07: Extract keywords from user input to customize ChatGPT prompts

---

### T21.G5.13
**ID:** T21.G5.13
**Topic:** T21 – Chatbots & Prompting
**Skill:** Create advanced prompt templates with role-task-format structure

**Description:** Students design reusable prompt templates using the role-task-format (RTF) pattern for consistent, high-quality outputs. Template structure: "You are a [ROLE] who [ROLE_DESCRIPTION]. Your task is to [TASK] for [AUDIENCE]. Use [FORMAT] and ensure you [CONSTRAINTS]." Students create 4 different template types: (1) Educational content: ROLE=teacher, TASK=explain, FORMAT=simple examples, CONSTRAINTS=age-appropriate language, (2) Creative content: ROLE=storyteller, TASK=create narrative, FORMAT=beginning-middle-end, CONSTRAINTS=positive themes, (3) Analytical content: ROLE=researcher, TASK=analyze, FORMAT=pros and cons list, CONSTRAINTS=evidence-based, (4) Problem-solving: ROLE=tutor, TASK=guide through solution, FORMAT=step-by-step, CONSTRAINTS=don't give direct answers. For each template, students test with 3 different specific inputs and verify consistent quality. Assessment: Create at least 3 working RTF templates that produce consistently formatted, high-quality outputs, such as Educational template: "You are a science teacher who makes complex topics fun. Your task is to explain [TOPIC] for 5th graders. Use everyday examples and ensure you use simple vocabulary" tested with topics like photosynthesis, gravity, and electricity.

**Dependencies:**
* T21.G4.13: Add constraints to prompts to limit chatbot response scope
* T21.G5.07: Extract keywords from user input to customize ChatGPT prompts
* T21.G2.02: Identify Role, Task, and Format parts in text prompts

---

### T21.G5.14
**ID:** T21.G5.14
**Topic:** T21 – Chatbots & Prompting
**Skill:** Evaluate ChatGPT responses for accuracy, completeness, and relevance

**Description:** Students develop systematic evaluation skills for AI-generated content. They create an evaluation framework with 5 criteria: (1) Accuracy - Are facts correct and verifiable?, (2) Completeness - Does it fully answer the question?, (3) Relevance - Does it stay on topic?, (4) Clarity - Is it easy to understand?, (5) Helpfulness - Does it serve the user's actual need? Students evaluate 10 ChatGPT responses using this rubric (score each 1-5), calculate overall scores, and identify weak areas. They then improve prompts specifically targeting low-scoring criteria (e.g., if completeness is low, add "Include all relevant details" to prompt). This builds critical thinking and iterative improvement skills. Assessment: Create evaluation rubric, score 10 responses, identify 3 improvement opportunities, such as response to "Explain photosynthesis" scoring Accuracy 5, Completeness 3, Relevance 5, Clarity 4, Helpfulness 4, identifying completeness issue (missing details about light reactions), and improving prompt to "Explain photosynthesis including both light and dark reactions in detail."

**Dependencies:**
* T21.G4.06: Test ChatGPT bot with 5 diverse inputs and document unexpected results
* T21.G2.09: Identify when chatbot response seems wrong or made-up (hallucination awareness)

---

## Summary Statistics

**Grade 4 (15 skills):**
- Multi-turn conversation management (G4.01, G4.05, G4.10)
- Few-shot prompting and examples (G4.12)
- Branching conversation logic with if-then (G4.05)
- Systematic testing (G4.06)
- Basic prompt safety (G4.14, G4.15)
- Conversation history using lists (G4.10)
- Comparing different bot slots (G4.11)
- Streaming mode (G4.03)
- Cancel request functionality (G4.04)
- Input validation (G4.07)
- Topic-specific expert bots (G4.08)
- Chaining ChatGPT calls (G4.09)
- Constraints in prompts (G4.13)

**Grade 5 (14 skills):**
- Voice integration: speech recognition (G5.01), text-to-speech (G5.02), full voice interaction (G5.03)
- LLM model blocks: small vs large comparison (G5.04), system instructions (G5.05)
- NLP parsing: sentence analysis (G5.06), keyword extraction (G5.07)
- Chain-of-thought prompting (G5.12)
- Advanced prompt patterns: RTF templates (G5.13)
- Error handling for API failures (G5.11)
- Context-aware chatbots with explicit history (G5.08)
- Temperature optimization (G5.09)
- Multi-bot topic routing (G5.10)
- Systematic evaluation (G5.14)

**Dependency Compliance:**
- All G4 dependencies from G4, G3, G2 only (X-2 rule)
- All G5 dependencies from G5, G4, G3 only (X-2 rule)
- Cross-topic dependencies preserved (T06, T07, T08, T09, T10, T12)
- Clear progression from foundational to advanced skills

**Block Coverage:**
- OpenAI ChatGPT request block (with all parameters)
- ChatGPT system prompt block
- ChatGPT bot selection (1-4)
- ChatGPT cancel request
- Speech recognition blocks (start, end, text from speech)
- Text-to-speech block (with all voice parameters)
- LLM model blocks (small/large)
- LLM system instruction block
- Sentence analysis block

---

**Document Status:** COMPLETE
**Ready for:** Integration into main T21 skill map
**Next Steps:** Validate against existing G3 and G6 skills for smooth progression
