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
* T21.G4.02: Construct a prompt with Role, Context, Task, and Format components




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
* T21.G4.06: Write a system prompt that defines chatbot behavior and boundaries
* T21.G4.08: Design a 4-turn conversation building toward a specific goal




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
* T21.G4.05: Design a prompt specifying desired output format (list, table, summary)
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
* T21.G4.10: Test a chatbot with 5 different prompt variations to assess reliability




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
* T21.G4.09: Identify why a chatbot misunderstood a prompt and fix it
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
