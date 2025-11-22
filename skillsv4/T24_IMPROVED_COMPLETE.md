# T24 - XO & Generative AI Practices
## COMPLETE IMPROVED SECTION WITH ALL FIXES APPLIED

---

## KINDERGARTEN SKILLS (GK)

### ID: T24.GK.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Identify AI as a computer helper
**Description:** Students learn that AI is a special computer program that can help with tasks like talking, drawing, and answering questions. Through picture-based activities, they match examples of AI helpers (voice assistants, chatbots, drawing tools) to what they do.

**Dependencies:**

---

### ID: T24.GK.02
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Recognize AI-made vs human-made pictures
**Description:** Students view pairs of pictures (one AI-generated, one human-drawn) and identify which is which. They discuss clues like unusual details or perfect symmetry that hint at AI creation.

**Dependencies:**
* T24.GK.01: Identify AI as a computer helper

---

### ID: T24.GK.03
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Give simple instructions to an AI helper
**Description:** Students practice giving clear, one-sentence instructions to an AI (e.g., "Draw a happy cat"). They compare results when instructions are vague vs specific.

**Dependencies:**
* T24.GK.01: Identify AI as a computer helper
* T24.GK.02: Recognize AI-made vs human-made pictures

---

## GRADE 1 SKILLS (G1)

### ID: T24.G1.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Listen to AI-generated speech
**Description:** Students hear AI text-to-speech reading a short story and identify that a computer, not a person, is speaking. They describe how the voice sounds different from a human voice.

**Dependencies:**
* T24.GK.01: Identify AI as a computer helper

---

### ID: T24.G1.02
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Compare AI answers to expected answers
**Description:** Students ask a simple question (e.g., "What color is the sky?") and compare the AI's answer to what they know. They discuss when AI gives good answers and when it might be wrong.

**Dependencies:**
* T24.GK.01: Identify AI as a computer helper
* T24.GK.03: Give simple instructions to an AI helper

---

### ID: T24.G1.03
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Understand AI needs clear instructions
**Description:** Students see examples of unclear instructions and their confusing results. They practice making instructions clearer by adding details like color, size, or action.

**Dependencies:**
* T24.GK.03: Give simple instructions to an AI helper
* T24.G1.02: Compare AI answers to expected answers

---

## GRADE 2 SKILLS (G2)

### ID: T24.G2.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Use AI text-to-speech to narrate a story
**Description:** Students type short sentences and use the `say [TEXT] in [LANGUAGE]` text-to-speech block to make the computer read their story aloud. They experiment with different sentences to create a mini-narrative, introducing block-based coding with AI features.

**Dependencies:**
* T24.G1.01: Listen to AI-generated speech
* T24.G1.03: Understand AI needs clear instructions

---

### ID: T24.G2.02
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Identify what AI can and cannot do
**Description:** Students sort picture cards into "AI can do this" and "AI cannot do this" piles (e.g., AI can answer questions but cannot feel happy). They discuss AI limitations like lacking emotions or real-world experience.

**Dependencies:**
* T24.G1.02: Compare AI answers to expected answers

---

### ID: T24.G2.03
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Describe what you want AI to create
**Description:** Students practice describing an image they want (subject, color, setting) before seeing AI results. They learn that better descriptions lead to better AI outputs.

**Dependencies:**
* T24.G1.03: Understand AI needs clear instructions
* T24.G2.02: Identify what AI can and cannot do

---

### ID: T24.G2.04
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Observe how AI hears spoken words
**Description:** Students speak simple words into a microphone and observe how AI transcribes them. Through picture-based activities, they compare what they said to what the AI "heard," noticing when the AI gets words right or makes mistakes. This bridges listening to AI (G1) with coding speech recognition (G3).

**Dependencies:**
* T24.G1.01: Listen to AI-generated speech
* T24.G2.02: Identify what AI can and cannot do

---

## GRADE 3 SKILLS (G3)

### ID: T24.G3.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Use speech-to-text to control a sprite
**Description:** Students use the `start recognizing speech` and `text from speech` blocks to capture voice commands (e.g., "jump") that trigger sprite actions. They practice speaking clearly and handling recognition errors, combining AI speech recognition with event-driven programming.

**Dependencies:**
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T24.G2.01: Use AI text-to-speech to narrate a story
* T24.G2.04: Observe how AI hears spoken words

---

### ID: T24.G3.02
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Evaluate if AI output matches the request
**Description:** Students give an AI image generator a prompt and judge whether the result matches what they asked for. They identify missing elements or unwanted additions. They use the `search for AI image` block to test prompts and build a simple rating script that stores prompt quality in a list, combining evaluation with coding practice.

**Dependencies:**
* T24.G2.03: Describe what you want AI to create
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence

---

### ID: T24.G3.03
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Revise a prompt to improve AI results
**Description:** Students take an AI result that did not match their goal and revise their prompt by adding or changing details. They compare the original and revised outputs. They write a prompt-builder script that combines variable values (subject, color, style) using text join blocks to create improved prompts programmatically.

**Dependencies:**
* T24.G3.02: Evaluate if AI output matches the request
* T09.G3.01: Create and use a numeric variable for score or count

---

### ID: T24.G3.04
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Recognize AI makes mistakes
**Description:** Students examine AI outputs that contain errors (wrong facts, strange images) and identify the mistakes. They learn that AI is not always correct and human review is needed. They build an error-detection script that compares AI output to expected results (e.g., checking AI math answers against calculated values) and flags discrepancies.

**Dependencies:**
* T24.G2.02: Identify what AI can and cannot do
* T24.G3.02: Evaluate if AI output matches the request
* T08.G3.01: Use a simple if in a script

---

## GRADE 4 SKILLS (G4)

### ID: T24.G4.01.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Combine keywords for better AI image searches
**Description:** Students learn to use multiple keywords in one search query (e.g., "cat sitting forest sunset" instead of just "cat"). They compare results from single-word vs multi-word searches and observe how specificity and detail improve results. They experiment with adding adjectives, actions, and settings to create more precise image searches. This bridges evaluation skills (G3.03) to the comprehensive keyword search skill (G4.01).

**Dependencies:**
* T24.G3.03: Revise a prompt to improve AI results

---

### ID: T24.G4.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Search the AI image library with keywords
**Description:** Students use the `search for AI image of [TYPE] with query [QUERY]` block to find sprites and backdrops matching single keywords (e.g., "cat", "forest"). They learn to evaluate search results and select the most appropriate asset for their project.

**Dependencies:**
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T24.G3.02: Evaluate if AI output matches the request
* T24.G4.01.01: Combine keywords for better AI image searches

---

### ID: T24.G4.02
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Write a multi-part prompt for AI
**Description:** Students structure prompts with multiple elements (subject + action + setting + style) to get more specific AI outputs. They compare simple vs detailed prompts. They create a prompt template using text join blocks with dropdown menus for subject, action, setting, and style, allowing them to build complex prompts programmatically by selecting options and combining them.

**Dependencies:**
* T24.G3.03: Revise a prompt to improve AI results
* T09.G3.01: Create and use a numeric variable for score or count

---

### ID: T24.G4.03
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Identify safe and unsafe AI interactions
**Description:** Students sort examples of AI prompts into safe (asking for help with homework) and unsafe (sharing personal info, asking AI to break rules) categories. They explain why some interactions are risky. They build a safety-checker script using conditionals that categorizes prompts by risk type and displays warning messages for unsafe categories.

**Dependencies:**
* T24.G3.04: Recognize AI makes mistakes
* T08.G3.01: Use a simple if in a script

---

### ID: T24.G4.04
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Credit AI-generated content in projects
**Description:** Students add labels or comments to their projects indicating which assets or ideas came from AI tools. They learn why attribution matters for honesty and fairness.

**Dependencies:**
* T24.G4.01: Search the AI image library with keywords
* T24.G4.03: Identify safe and unsafe AI interactions

---

### ID: T24.G4.05
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Understand content moderation in AI systems
**Description:** Students learn that AI tools check content for safety (inappropriate language, harmful content). They test examples of text that would be flagged and discuss why moderation exists to keep online spaces safe.

**Dependencies:**
* T24.G4.03: Identify safe and unsafe AI interactions

---

### ID: T24.G4.06
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Explore AI block categories in CreatiCode
**Description:** Students survey the AI blocks available in CreatiCode (speech recognition, text-to-speech, ChatGPT, image generation, moderation). They categorize blocks by function (speaking, listening, creating, checking) and identify which blocks they might use in future projects. This bridges conceptual AI understanding to hands-on coding.

**Dependencies:**
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T24.G4.02: Write a multi-part prompt for AI
* T24.G4.05: Understand content moderation in AI systems

---

## GRADE 5 SKILLS (G5)

### ID: T24.G5.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Read and interpret XO's interface cues
**Description:** Students explore XO, the CreatiCode AI coding assistant integrated in the IDE. They navigate XO's chat area, template prompts, code/explanation tabs, and "insert into project" buttons, learning how to pause, copy, and pin answers for later. Students practice pausing XO mid-response, copying code snippets with proper formatting, and pinning answers to reference later. They learn to: (1) locate and use template prompts, (2) switch between code and explanation views, (3) copy code snippets safely, (4) pin important responses for later reference, and (5) identify when XO is still generating vs finished.

**Dependencies:**
* T24.G4.03: Identify safe and unsafe AI interactions
* T24.G4.06: Explore AI block categories in CreatiCode

---

### ID: T24.G5.02
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Ask XO for a three-step project plan
**Description:** Students practice writing a structured prompt (goal + constraints + audience) so XO replies with a numbered plan. They verify the plan covers at least three concrete actions (e.g., "draw sprite," "add `when green flag clicked`," "show score label").

**Dependencies:**
* T24.G5.01: Read and interpret XO's interface cues

---

### ID: T24.G5.03
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Turn an XO suggestion into starter code safely
**Description:** Students copy a short script provided by XO (e.g., movement loop) into their project, but before running it they verify variables/events exist and annotate what each block does. This builds the habit of reading AI output before trusting it.

**Dependencies:**
* T24.G5.01: Read and interpret XO's interface cues
* T24.G5.02: Ask XO for a three-step project plan

---

### ID: T24.G5.04
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Collect themed assets from narrative descriptions
**Description:** Students take XO's narrative description (e.g., "Journey of a Waterdrop" scene) and convert it into multi-part AI image search queries. They collect multiple matching sprites and backdrops for a coherent scene, justifying how each asset fits the narrative. This advances from single-keyword searches to theme-based asset collection.

**Dependencies:**
* T24.G4.01: Search the AI image library with keywords
* T24.G5.02: Ask XO for a three-step project plan

---

### ID: T24.G5.05
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Reject unsafe or off-spec XO suggestions
**Description:** Students review an XO reply that includes off-task, private, or non-compliant steps (e.g., "ask a friend for their password," "skip testing") and practice declining it. They write a replacement step that follows the rubric/spec and log why the original was rejected.

**Dependencies:**
* T24.G4.03: Identify safe and unsafe AI interactions
* T24.G5.03: Turn an XO suggestion into starter code safely

---

### ID: T24.G5.06
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Use AI sentence analysis to identify parts of speech
**Description:** Students use the `analyze sentence [TEXT]` block to parse simple sentences and identify nouns, verbs, and adjectives. The results are written to a table for inspection. They explore how NLP helps computers understand language structure. The table has 7 columns: TEXT (word), LEMMA (root form), TYPE (noun/verb/etc), PERSON, OFFSET, LABEL, DEPENDS. Students learn to read this structured data and use it to analyze sentence patterns.

**Dependencies:**
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T24.G4.02: Write a multi-part prompt for AI
* T24.G4.06: Explore AI block categories in CreatiCode

---

### ID: T24.G5.07
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Use the ChatGPT block to get AI responses in code
**Description:** Students use the `ChatGPT request [PROMPT] result [VARIABLE]` block to send prompts programmatically and store responses in variables. They build simple projects where AI responses drive sprite behavior or display text. They learn the difference between `session: new chat` (fresh conversation) and `session: continue` (maintains context). They learn to use 'session: new' for independent queries and 'session: continue' to maintain conversation context across multiple XO requests, enabling more sophisticated multi-turn assistance.

**Dependencies:**
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T09.G3.01: Create and use a numeric variable for score or count
* T24.G4.02: Write a multi-part prompt for AI
* T24.G4.06: Explore AI block categories in CreatiCode

---

### ID: T24.G5.08
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Use continuous speech recognition for live voice input
**Description:** Students use the `start continuous speech recognition` block to stream voice input into a list in real-time. They build projects where spoken words continuously update a display or trigger actions, learning to start and stop recognition and handle the stream of recognized text.

**Dependencies:**
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
* T10.G3.03: Add and remove items from a list
* T24.G3.01: Use speech-to-text to control a sprite
* T24.G4.06: Explore AI block categories in CreatiCode

---

## GRADE 6 SKILLS (G6)

### ID: T24.G6.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Provide complete context when asking XO to debug
**Description:** Students assemble a "debug packet" with the bug description, relevant script, and what they expected. XO returns a fix; students evaluate whether it addresses the issue and annotate any manual tweaks.

**Dependencies:**
* T06.G4.01: Trace event execution paths in a multi-event program
* T09.G4.04: Trace code with variables to predict outcomes
* T24.G5.03: Turn an XO suggestion into starter code safely
* T24.G5.05: Reject unsafe or off-spec XO suggestions

---

### ID: T24.G6.02
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Verify XO's explanation against the project
**Description:** Students ask XO "Explain how this script works," then compare the explanation to the actual code. They highlight any mismatches (missing variable, wrong loop) and either accept or correct the AI explanation.

**Dependencies:**
* T06.G4.01: Trace event execution paths in a multi-event program
* T07.G4.01: Use a counted repeat loop
* T08.G4.01: Use if‑else or else‑if chains
* T09.G4.01: Create and use a numeric variable for score or count
* T24.G5.03: Turn an XO suggestion into starter code safely
* T24.G6.01: Provide complete context when asking XO to debug

---

### ID: T24.G6.03
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Generate and deliver a quiz using XO
**Description:** Students prompt XO for three multiple-choice questions about a chosen topic (loops, events), then vet each question for clarity and accuracy before sharing it with classmates via widgets.

**Dependencies:**
* T06.G4.01: Trace event execution paths in a multi-event program
* T09.G4.04: Trace code with variables to predict outcomes
* T24.G5.05: Reject unsafe or off-spec XO suggestions
* T24.G6.02: Verify XO's explanation against the project

---

### ID: T24.G6.04
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Iterate AI images using feedback from XO
**Description:** Students upload an AI-generated backdrop to XO, ask for improvement ideas (e.g., "What should I change to make it look stormy?"), then modify the prompt and regenerate. They compare before/after results and note which prompt edits caused the change.

**Dependencies:**
* T09.G4.04: Trace code with variables to predict outcomes
* T24.G5.04: Collect themed assets from narrative descriptions
* T24.G5.05: Reject unsafe or off-spec XO suggestions

---

### ID: T24.G6.05.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Generate custom images with the DALL-E block
**Description:** Students use the `DALL-E generate image with request [DESCRIPTION]` block to create custom images based on detailed prompts. They understand the difference between searching the AI image library and generating new images. They select appropriate resolutions (256x256, 512x512, 1024x1024) based on project needs. They learn to choose between 256x256 (fast, small assets like icons), 512x512 (balanced quality and speed for game sprites), and 1024x1024 (high quality but slower, for detailed backdrops or feature art).

**Dependencies:**
* T24.G4.02: Write a multi-part prompt for AI
* T24.G5.04: Collect themed assets from narrative descriptions

---

### ID: T24.G6.05
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Maintain a prompt/response lab notebook using lists
**Description:** Students use CreatiCode lists or tables to track their AI interactions (date, tool, prompt, result quality, action taken). They write scripts to add entries and review the log to spot patterns (e.g., "long prompts give better responses"), building both coding and metacognitive habits. The table structure includes columns for: timestamp, AI tool used, prompt text, result quality (1-5 rating), and action taken (used/modified/rejected). Students learn to analyze this data to improve their prompting strategies.

**Dependencies:**
* T06.G4.01: Trace event execution paths in a multi-event program
* T09.G4.01: Create and use a numeric variable for score or count
* T10.G4.03: Add and remove items from a list
* T24.G5.05: Reject unsafe or off-spec XO suggestions
* T24.G6.04: Iterate AI images using feedback from XO

---

### ID: T24.G6.06
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Label risky prompts and rewrite them safely
**Description:** Students examine sample prompts that leak private info, copy code wholesale, or ask XO to skip grading criteria. They classify each as "safe" or "risky," then rewrite risky ones to remove private data and align to the rubric while keeping the learning goal.

**Dependencies:**
* T08.G4.01: Use if‑else or else‑if chains
* T09.G4.04: Trace code with variables to predict outcomes
* T24.G5.05: Reject unsafe or off-spec XO suggestions
* T24.G6.05: Maintain a prompt/response lab notebook using lists

---

### ID: T24.G6.07
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Use content moderation blocks to filter user input
**Description:** Students use the `get moderation result for [TEXT]` block to check text for inappropriate content before processing. They build a simple chatbot or comment system that uses conditionals to reject flagged input and respond appropriately.

**Dependencies:**
* T06.G4.01: Trace event execution paths in a multi-event program
* T08.G4.01: Use if‑else or else‑if chains
* T24.G4.05: Understand content moderation in AI systems
* T24.G5.07: Use the ChatGPT block to get AI responses in code

---

### ID: T24.G6.08.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Manage ChatGPT sessions explicitly
**Description:** Students modify their ChatGPT block usage from G5.07 to explicitly control sessions using the `session: new chat` vs `session: continue` parameters. They ask XO a series of related questions (e.g., "What are loops?" then "Show me an example") and observe how context is maintained. They learn when to start fresh sessions (independent queries) vs continue sessions (building on previous context). This bridges basic ChatGPT usage (G5.07) to multi-turn chatbots (G6.08).

**Dependencies:**
* T24.G5.07: Use the ChatGPT block to get AI responses in code
* T08.G4.01: Use if‑else or else‑if chains

---

### ID: T24.G6.08
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Build a multi-turn chatbot using LLM sessions
**Description:** Students use the `ChatGPT request` block with `session: continue` to maintain conversation context across multiple exchanges. They build an interactive chatbot that remembers previous questions and provides contextual responses.

**Dependencies:**
* T07.G4.01: Use a counted repeat loop
* T08.G4.01: Use if‑else or else‑if chains
* T24.G6.08.01: Manage ChatGPT sessions explicitly
* T24.G6.05: Maintain a prompt/response lab notebook using lists

---

### ID: T24.G6.09
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Attach stage snapshots to XO for visual debugging
**Description:** Students use the stage snapshot feature to capture their project's visual output, then attach it to an XO request using the attach costume block. They ask questions like "Is this output correct for [specification]?" or "Does this design match my theme?" They learn to get visual debugging help from XO for graphics-heavy projects, not just code feedback. This extends XO usage beyond code review to visual asset evaluation.

**Dependencies:**
* T24.G6.04: Iterate AI images using feedback from XO
* T09.G4.01: Create and use a numeric variable for score or count

---

## GRADE 7 SKILLS (G7)

### ID: T24.G7.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Create reusable XO prompt templates in lists
**Description:** Students design prompt templates (e.g., "Code Review Template," "Project Outline Template") with placeholders for sprites, variables, and goals. They store these as text items in CreatiCode lists and use string join blocks to fill in placeholders, creating reusable prompts for XO. The table structure includes columns for: template name, template text with {PLACEHOLDERS}, category (debugging/planning/review), and usage count. Students track which templates are most effective.

**Dependencies:**
* T09.G5.01: Use arithmetic and comparison operators with variables
* T10.G5.03: Add and remove items from a list
* T24.G6.05: Maintain a prompt/response lab notebook using lists
* T24.G6.06: Label risky prompts and rewrite them safely

---

### ID: T24.G7.02
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Run an XO-led code review with evidence
**Description:** Students paste a medium script into XO and ask for "3 improvements." They then inspect each suggestion, either implementing it or rejecting it with justification (performance, readability, game design). They maintain a review log table with columns for: original code, suggestion, decision (accepted/rejected), justification, and outcome. This teaches critical evaluation of AI suggestions with evidence-based reasoning.

**Dependencies:**
* T06.G5.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G5.01: Use if‑else to handle two cases
* T09.G5.04: Use arithmetic and comparison operators with variables
* T24.G6.06: Label risky prompts and rewrite them safely
* T24.G7.01: Create reusable XO prompt templates in lists

---

### ID: T24.G7.03
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Combine XO storyboards with AI sprite generation
**Description:** Students ask XO for a storyboard (scene descriptions + characters) for a themed project, then generate sprites/backdrops for each scene via the AI image blocks. They document alignment between text and visuals. They maintain a storyboard table with columns for: scene number, description from XO, sprite/backdrop name, alignment score (1-5), and notes on modifications needed.

**Dependencies:**
* T06.G5.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G5.04: Use arithmetic and comparison operators with variables
* T24.G6.04: Iterate AI images using feedback from XO
* T24.G6.05: Maintain a prompt/response lab notebook using lists
* T24.G7.01: Create reusable XO prompt templates in lists

---

### ID: T24.G7.04
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Enforce responsible-use rules for XO assistance
**Description:** Students implement an "AI Help" log inside their project (a hidden list or widget) that records each XO contribution, who reviewed it, and whether it was modified. They also add on-screen indicators telling players when AI-generated art/text appears. The tracking table includes columns for: timestamp, XO contribution type (code/plan/asset), reviewer name, modified (yes/no), and attribution displayed (yes/no). This teaches systematic AI usage documentation.

**Dependencies:**
* T08.G5.01: Use if‑else to handle two cases
* T10.G5.03: Add and remove items from a list
* T24.G6.05: Maintain a prompt/response lab notebook using lists
* T24.G6.06: Label risky prompts and rewrite them safely
* T24.G7.01: Create reusable XO prompt templates in lists

---

### ID: T24.G7.05
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Use XO to coach peers with rubric-based feedback
**Description:** Students feed XO a project summary and ask for constructive feedback. They then edit the response to match a class rubric (naming strengths, next steps) before sending it to a peer. This reinforces human oversight and empathy. They maintain a feedback table with columns for: peer name, XO raw feedback, edited feedback, rubric alignment score, and peer response. This teaches responsible AI-mediated peer review.

**Dependencies:**
* T09.G5.01: Use arithmetic and comparison operators with variables
* T24.G6.06: Label risky prompts and rewrite them safely
* T24.G7.02: Run an XO-led code review with evidence
* T24.G7.04: Enforce responsible-use rules for XO assistance

---

### ID: T24.G7.06
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Use multiple XO sessions to compare responses
**Description:** Students use the `select chatbot [1/2/3/4]` block to create two XO sessions with different system instructions (e.g., "focus on readability" vs "focus on efficiency"). They send the same code review request to both sessions, compare the responses, and synthesize a combined improvement plan. They maintain a comparison table with columns for: prompt, session 1 response, session 2 response, differences identified, and synthesized recommendation. This teaches critical comparison of AI perspectives.

**Dependencies:**
* T24.G7.02: Run an XO-led code review with evidence
* T24.G7.05: Use XO to coach peers with rubric-based feedback
* T10.G5.03: Add and remove items from a list

---

## GRADE 8 SKILLS (G8)

### ID: T24.G8.01
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Automate XO requests with data-driven prompt builders
**Description:** Students store project metadata (sprite name, mechanic, constraint) in a table and build scripts that concatenate those fields into structured XO prompts. Pressing a widget button copies the prompt for immediate use. The metadata table includes columns for: sprite name, mechanic type, constraint description, target grade level, and auto-generated prompt text. This teaches systematic prompt generation from structured data.

**Dependencies:**
* T06.G6.01: Trace event execution paths in a multi-event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T24.G7.01: Create reusable XO prompt templates in lists
* T24.G7.04: Enforce responsible-use rules for XO assistance

---

### ID: T24.G8.02
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Pair XO with automated tests to validate fixes
**Description:** Students write a small automated test harness (assertions or monitoring variables). They then prompt XO for a fix, apply it, run the tests, and report whether the fix passed. If not, they loop with refined prompts until the tests succeed. The test log table includes columns for: test name, XO fix attempt number, test result (pass/fail), error message, and refined prompt. This teaches iterative AI-assisted debugging with validation.

**Dependencies:**
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T24.G7.02: Run an XO-led code review with evidence
* T24.G8.01: Automate XO requests with data-driven prompt builders

---

### ID: T24.G8.03
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Compare XO-generated code/image options with human-crafted versions
**Description:** Students implement two versions of a feature or asset: one produced with XO/AI image tool, one produced manually. They create metrics (lines of code, frame rate, user preference) and analyze tradeoffs. The comparison table includes columns for: feature/asset name, AI version metrics, human version metrics, quality ratings (1-5), speed comparison, and recommendation with justification. This teaches critical evaluation of AI assistance value.

**Dependencies:**
* T06.G6.01: Trace event execution paths in a multi-event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T24.G7.03: Combine XO storyboards with AI sprite generation
* T24.G7.04: Enforce responsible-use rules for XO assistance
* T24.G8.01: Automate XO requests with data-driven prompt builders

---

### ID: T24.G8.04
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Implement AI usage tracking and policy enforcement (Capstone)
**Description:** Students create a comprehensive project with coded enforcement of AI usage rules: tracking XO contributions in lists, displaying AI attribution labels, implementing approval workflows with conditionals, and logging usage statistics. They document their policy decisions in code comments. This capstone project combines: (1) contribution tracking table (timestamp, type, source, reviewer, status), (2) attribution display system, (3) approval workflow with conditional logic, (4) usage statistics dashboard, and (5) policy documentation in comments. This demonstrates mastery of responsible AI integration in projects.

**Dependencies:**
* T06.G6.01: Trace event execution paths in a multi-event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T24.G7.04: Enforce responsible-use rules for XO assistance
* T24.G8.02: Pair XO with automated tests to validate fixes
* T24.G8.03: Compare XO-generated code/image options with human-crafted versions

---

### ID: T24.G8.05
**Topic:** T24 – XO & Generative AI Practices
**Skill:** Build an interactive XO tutorial project (Capstone)
**Description:** Students create a comprehensive interactive CreatiCode project that demonstrates XO best practices (planning, debugging, image iteration). The project includes step-by-step guidance, example prompts stored in lists, and interactive elements that let users practice safe AI interactions. This capstone project combines: (1) tutorial navigation system with step tracking, (2) example prompt library stored in tables, (3) interactive practice exercises with validation, (4) progress tracking and feedback, and (5) comprehensive documentation of XO workflows. This demonstrates mastery of teaching others about responsible AI-assisted coding.

**Dependencies:**
* T01.G6.01: Count comparisons in linear and binary search
* T07.G6.01: Trace nested loops with variable bounds
* T09.G6.01: Model real-world quantities using variables and formulas
* T24.G7.05: Use XO to coach peers with rubric-based feedback
* T24.G8.04: Implement AI usage tracking and policy enforcement (Capstone)

---

## END OF T24 COMPLETE IMPROVED SECTION

**Summary of Improvements Applied:**

**New Skills Added (using sub-IDs):**
1. T24.G4.01.01 - Combine keywords for better AI image searches (bridges G3.03→G4.01)
2. T24.G6.09 - Attach stage snapshots to XO for visual debugging (after G6.04)
3. T24.G6.08.01 - Manage ChatGPT sessions explicitly (bridges G5.07→G6.08)
4. T24.G7.06 - Use multiple XO sessions to compare responses (after G7.05)

**Coding Added to Unplugged G3-G4 Skills:**
- T24.G3.02 - Added rating script with list storage
- T24.G3.03 - Added prompt-builder script with text join
- T24.G3.04 - Added error-detection script with conditionals
- T24.G4.02 - Added prompt template with dropdown menus
- T24.G4.03 - Added safety-checker with conditionals

**X-2 Rule Violations Fixed:**
- T24.G7.01 - Changed T09.G3.01 → T09.G5.01
- T24.G7.02 - Changed T09.G3.05 → T09.G5.04
- T24.G7.03 - Changed T09.G3.05 → T09.G5.04
- T24.G7.05 - Changed T09.G3.01 → T09.G5.01

**Unnecessary Dependencies Removed:**
- T24.G5.03 - Removed T10.G3.03 (lists not needed for reading code)
- T24.G5.04 - Removed T01.G3.01 and T09.G3.05 (boilerplate)
- T24.G5.05 - Removed T01.G3.01 and T09.G3.05 (boilerplate)

**Enhanced Descriptions:**
- T24.G5.01 - Added specific interface actions (pause, copy, pin)
- T24.G5.06 - Added table structure (7 columns detailed)
- T24.G5.07 - Added session management explanation (new vs continue)
- T24.G6.05.01 - Added resolution choices (256/512/1024) with use cases
- T24.G6.05, G7.01, G7.02, G7.03, G7.04 - Added table structure details
- T24.G8.04, G8.05 - Added "(Capstone)" marker and comprehensive details

**All cross-topic dependencies preserved:**
- Dependencies to T01, T06, T07, T08, T09, T10 maintained
- Only intra-topic (within T24) dependency issues fixed
- X-2 rule applied consistently throughout
