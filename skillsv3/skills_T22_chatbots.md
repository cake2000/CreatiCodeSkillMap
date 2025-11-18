# T22 – AI Prompting: K–8 Skill List (Draft v1)

Topic reference: `T22 AI Prompting` in `domains_topics_overview.md`
Domain: Programming (D2) & Computing and Society (D5) · CSTA focus: PRO‑PF, ALG‑PS, CAS‑ET

Each skill below has:

- a stable **ID** (`T22.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Grade K introduces the idea of asking questions and getting answers from a computer, with simple chatbot interactions as a precursor to understanding AI conversations.

### T22.GK.01 – Recognize a chatbot is a talking computer

- **Short name:** Identify a chatbot character
- **Description:** Students recognize that a chatbot is a computer character that can answer questions or have conversations, distinguishing it from a regular sprite or character that only repeats pre-written dialogue.
- **Challenge format:** Concept, multiple choice. Show three scenarios: (1) a sprite that says "Hello" whenever clicked, (2) a sprite that responds to different questions with different answers, (3) a sprite that only moves. Students select which one is a chatbot. Auto‑grading checks the selection.
- **CSTA:** EK‑PRO‑PF‑02, EK‑CAS‑ET‑02.

### T22.GK.02 – Ask a question and hear an answer

- **Short name:** Get an answer from a chatbot
- **Description:** Students experience asking a simple question to a chatbot in a CreatiCode project and receiving a response, recognizing that the computer understood their question and provided relevant information.
- **Challenge format:** Interactive, guided demo project. A CreatiCode project has a chatbot sprite. Students click a button or press a key to ask a pre-set question (e.g., "What is your name?"). The chatbot's response appears on screen. Students then answer a simple comprehension question (e.g., "What did the chatbot say its name was?"). Auto‑grading checks the answer.
- **CSTA:** EK‑PRO‑PF‑02, EK‑CAS‑ET‑02.

### T22.GK.03 – Describe what a chatbot does in words

- **Short name:** Explain how a chatbot helps
- **Description:** Students articulate in simple language how a chatbot is useful (e.g., it answers questions, it tells jokes, it helps you learn) and what makes it different from talking to a person.
- **Challenge format:** Concept, open-ended response or word bank matching. After interacting with a simple chatbot, students complete a sentence: "A chatbot can help by ___" with options like "answering questions," "telling jokes," "playing games," or "teaching lessons." Auto‑grading checks selection or short recorded/typed response.
- **CSTA:** EK‑CAS‑ET‑02, EK‑CAS‑CE‑03.

---

## Grade 1

Grade 1 builds on K by having students recognize that different questions can get different answers, and that talking to a chatbot is like asking for information.

### T22.G1.01 – Ask different questions, get different answers

- **Short name:** Chatbot answers different questions
- **Description:** Students understand that a chatbot can respond to multiple different questions with appropriate answers, not just repeat the same response, and they begin to think of chatbots as information providers.
- **Challenge format:** Concept, interactive scenario. A CreatiCode chatbot is shown; students ask it 3–4 different questions (via buttons or pre-written questions) and observe that the answers differ. Students then match each question to its correct answer from a shuffled list. Auto‑grading checks correctness of matches.
- **CSTA:** E1‑PRO‑PF‑01, E1‑CAS‑ET‑02.

### T22.G1.02 – Recognize chatbot responses are pre-written

- **Short name:** Understand the chatbot's answers come from the creator
- **Description:** Students learn that each response a chatbot gives was written by the person who created the chatbot, not generated fresh by the computer. This introduces the idea that chatbots are tools designed by humans.
- **Challenge format:** Concept, code-reading or explanation. Show a simple CreatiCode script with a chatbot: a question-and-answer block showing "If asked 'What's your name?' then say 'I'm ChatBot.'" Students answer: "Who wrote this answer?" or "Who decided what the chatbot would say?" Auto‑grading checks for student understanding (e.g., "the creator" or "the programmer").
- **CSTA:** E1‑PRO‑PF‑01, E1‑CAS‑ET‑02.

### T22.G1.03 – Build a simple chatbot with 2–3 Q&A pairs

- **Short name:** Create a basic chatbot
- **Description:** Students build their first chatbot by adding blocks that detect a question and respond with a specific answer, connecting the idea of input (question) to output (answer).
- **Challenge format:** Coding, starter project with guided steps. Provided: a sprite and blocks for `ask [question] and wait` and `if <> then say <>`. Students are prompted: "Make your chatbot answer 'What is your name?' with your name." Students drag or create 2–3 question-answer pairs. Auto‑grading checks that at least one Q&A pair is correct and that the script runs without error.
- **CSTA:** E1‑PRO‑PF‑01, E1‑ALG‑PS‑03.

---

## Grade 2

Grade 2 introduces using actual AI (ChatGPT) for responses, prompt engineering in simple form, and the idea that chatbots can learn from input.

### T22.G2.01 – Use ChatGPT to generate an answer

- **Short name:** Ask ChatGPT a question in a project
- **Description:** Students use a CreatiCode ChatGPT block to send a question to an AI and receive a response, experiencing that the AI can generate novel answers not pre-written by the project creator.
- **Challenge format:** Coding, guided starter project. Provided: a sprite, a variable for storage, and a partial ChatGPT block. Prompt: "Ask ChatGPT 'What is 2+2?' and make the sprite say the answer." Students fill in the prompt or select options to complete the block. Auto‑grading checks that the block is present, a response is stored, and the sprite displays it.
- **CSTA:** E2‑PRO‑PF‑01, E2‑CAS‑ET‑02.

### T22.G2.02 – Notice different prompts give different answers

- **Short name:** Different questions get different ChatGPT answers
- **Description:** Students experiment with asking ChatGPT the same question in slightly different ways (e.g., "What is a cat?" vs "Describe a cat") and notice that the AI generates related but distinct responses.
- **Challenge format:** Concept, interactive exploration. A CreatiCode project includes a ChatGPT block and two text input fields. Students enter two slightly different prompts and run the project twice, observing the two different responses. They then answer: "Are the answers the same or different?" and "Why might the AI give different answers to similar questions?" Auto‑grading checks understanding via multiple choice or short response.
- **CSTA:** E2‑PRO‑PF‑01, E2‑ALG‑PS‑03, E2‑CAS‑ET‑02.

### T22.G2.03 – Build a simple information chatbot

- **Short name:** Make an info chatbot using ChatGPT
- **Description:** Students create a chatbot that takes user input (a topic or question) and uses ChatGPT to generate informative responses, combining user input with AI to create an interactive information tool.
- **Challenge format:** Coding, starter project with some scaffolding. Provided: a sprite, an `ask` block, and a ChatGPT block template. Prompt: "Build a chatbot that asks the user 'What would you like to learn about?' and then uses ChatGPT to teach them." Students connect the user's answer to the ChatGPT prompt. Auto‑grading checks that user input is captured and fed into the ChatGPT block and that a response is displayed.
- **CSTA:** E2‑PRO‑PF‑01, E2‑ALG‑AF‑01.

### T22.G2.04 – Recognize ChatGPT is not always accurate

- **Short name:** Understand AI can make mistakes
- **Description:** Students learn that ChatGPT is not a perfect source of truth and may generate plausible-sounding but incorrect information, introducing critical evaluation of AI outputs.
- **Challenge format:** Concept, scenario-based. Show a chatbot conversation where ChatGPT is asked a factual question (e.g., "How many legs does a spider have?") and gives an incorrect answer (e.g., "6"). Students are asked to evaluate: "Is this answer correct?" and "How could we check if the chatbot's answer is right?" Auto‑grading checks for understanding that the AI can be wrong and that humans should verify.
- **CSTA:** E2‑CAS‑ET‑02, E2‑ALG‑PS‑03.

---

## Grade 3

Grade 3 emphasizes prompt engineering, using context/sessions to maintain conversation flow, and character chatbots with personality.

### T22.G3.01 – Write a clear prompt for ChatGPT

- **Short name:** Craft a good prompt for the AI
- **Description:** Students learn that how you write a prompt affects the quality of the AI's response, and they practice writing clear, specific prompts rather than vague ones.
- **Challenge format:** Concept, comparison and construction. Show two prompts: "Tell me about dogs" and "Describe three interesting facts about dogs in 2–3 sentences." Students identify which will likely get a better answer and explain why. Then they write their own clear prompt. Auto‑grading uses rubric criteria (specificity, clarity) and may do automated checks.
- **CSTA:** E3‑ALG‑PS‑03, E3‑CAS‑ET‑02.

### T22.G3.02 – Maintain conversation context with ChatGPT

- **Short name:** Keep conversation history for context
- **Description:** Students understand that using the same ChatGPT session allows the AI to remember prior messages in a conversation, enabling follow-up questions and maintaining context, versus starting fresh each time.
- **Challenge format:** Concept, interactive comparison. Two CreatiCode projects: one uses a "new chat" for each question, the other uses the same "session" for multiple questions. Students ask the bot "What is your favorite color?" in one project and "Why did you choose that color?" in another project. They compare results and notice that the second approach maintains context. Auto‑grading checks understanding via multiple choice.
- **CSTA:** E3‑PRO‑PF‑01, E3‑CAS‑ET‑02.

### T22.G3.03 – Create a character chatbot with personality

- **Short name:** Build a chatbot with a specific personality
- **Description:** Students design a chatbot that embodies a specific character or personality (e.g., a pirate, a teacher, a detective) by giving ChatGPT a system prompt or context that shapes its responses to match that character.
- **Challenge format:** Coding, creative starter project. Provided: a sprite (with a fitting costume), a variable for the character context, and a ChatGPT block. Prompt: "Create a 'Wise Owl' chatbot. Use ChatGPT with a prompt like 'You are a wise owl...' to make it answer questions in character." Students write the character description or select from options and test the chatbot. Auto‑grading checks that the ChatGPT block uses a character-defining prompt and that responses reflect the intended personality.
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑PS‑03.

### T22.G3.04 – Handle invalid or off-topic user input gracefully

- **Short name:** Make chatbot handle unexpected input
- **Description:** Students add conditional logic to detect when a user input is off-topic or unclear and respond politely with a redirection, improving the chatbot's user experience.
- **Challenge format:** Coding, refactoring or extension. Starter project includes a working chatbot. Prompt: "Add a check: if the user's input is less than 3 characters, say 'Please ask me a real question!' instead of sending it to ChatGPT." Students add an `if` block to validate input. Auto‑grading checks logic and tests with various inputs.
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑AF‑01.

---

## Grade 4

Grade 4 focuses on using ChatGPT for content transformation (summarizing, translating, reformatting), session management for multi-turn conversations, and ethical use of AI.

### T22.G4.01 – Summarize text using ChatGPT

- **Short name:** Use AI to summarize information
- **Description:** Students ask ChatGPT to take a longer text and produce a concise summary, understanding that AI can transform content in useful ways.
- **Challenge format:** Coding, starter project. Provided: a text input field and a ChatGPT block. Prompt: "Build a tool that takes a paragraph from the user and uses ChatGPT to summarize it in 1–2 sentences." Students create the project and test it. Auto‑grading checks that the summarize prompt is correctly passed to ChatGPT and that output is displayed.
- **CSTA:** E4‑PRO‑PF‑01, E4‑ALG‑PS‑03.

### T22.G4.02 – Translate text using ChatGPT

- **Short name:** Translate words or sentences with AI
- **Description:** Students use ChatGPT to translate user input into another language, expanding the idea of content transformation and showing practical AI applications.
- **Challenge format:** Coding, starter project. Provided: an input field for text, a dropdown to select target language, and a ChatGPT block. Prompt: "Create a translator that lets the user type English text and select a language, then uses ChatGPT to translate it." Students configure the blocks. Auto‑grading checks that the ChatGPT prompt includes the target language and that translated output appears.
- **CSTA:** E4‑PRO‑PF‑01, E4‑ALG‑AF‑01.

### T22.G4.03 – Build a multi-turn Q&A chatbot with context

- **Short name:** Chatbot remembers previous questions
- **Description:** Students create a chatbot that maintains conversation history across multiple turns, so the AI can reference earlier messages and provide coherent, context-aware replies.
- **Challenge format:** Coding, guided project. Provided: a variable to store session ID, multiple ask/ChatGPT blocks, and a display area. Prompt: "Create a chatbot that asks 'What is your hobby?' and then asks 'Tell me more about that.' The second response should reference the first answer." Students use the same session for both ChatGPT calls. Auto‑grading checks that session ID is reused and that responses reference prior context.
- **CSTA:** E4‑PRO‑PF‑01, E4‑PRO‑DH‑02.

### T22.G4.04 – Identify and discuss responsible AI use

- **Short name:** Understand ethical use of chatbots
- **Description:** Students reflect on how to use ChatGPT responsibly (e.g., not claiming AI output as their own, fact-checking AI answers, respecting privacy in conversations) and discuss ethical concerns.
- **Challenge format:** Concept, discussion and scenario analysis. Present scenarios: (1) A student uses ChatGPT to write their entire essay and submits it. (2) A student uses ChatGPT to brainstorm ideas for an essay, then writes it themselves. (3) A chatbot is asked for someone's address. Students evaluate which are responsible and explain why. Auto‑grading uses rubric for reasoning.
- **CSTA:** E4‑CAS‑ET‑02, E4‑ALG‑IM‑04.

---

## Grade 5

Grade 5 emphasizes building information applications (tutors, FAQ bots), managing multiple conversation sessions, and evaluating chatbot quality.

### T22.G5.01 – Build a virtual tutor chatbot

- **Short name:** Create an educational chatbot
- **Description:** Students design a tutoring chatbot that helps users learn a topic by asking guiding questions, providing hints, and adapting responses based on user answers.
- **Challenge format:** Coding, project challenge. Prompt: "Create a math tutor chatbot. It should ask the user a math question, receive their answer, and use ChatGPT to give feedback (e.g., 'Good try! Here's a hint...' or 'Correct!')." Students integrate user input with ChatGPT feedback. Auto‑grading checks that the chatbot asks questions, processes answers, and provides adaptive feedback.
- **CSTA:** E5‑PRO‑PF‑01, E5‑ALG‑PS‑03.

### T22.G5.02 – Handle multiple chatbot sessions simultaneously

- **Short name:** Manage different conversation topics at once
- **Description:** Students use multiple session variables to track separate conversations with the chatbot on different topics, understanding that sessions isolate context.
- **Challenge format:** Coding, advanced starter project. Provided: buttons for "Science Questions" and "History Questions," variables for two different session IDs, and ChatGPT blocks. Prompt: "Let users ask about science or history. Each topic should remember its own conversation history." Students ensure each button uses its own session variable. Auto‑grading checks that sessions are maintained separately by testing both conversation threads.
- **CSTA:** E5‑PRO‑PF‑01, E5‑PRO‑DH‑02.

### T22.G5.03 – Create a FAQ chatbot that stores Q&A pairs

- **Short name:** Build a searchable question-answer bot
- **Description:** Students build a chatbot that stores frequently asked questions and answers in a list or table, and responds by searching the list before asking ChatGPT, improving efficiency and consistency.
- **Challenge format:** Coding, project challenge. Provided: a list of predefined Q&A pairs and a search mechanism. Prompt: "Create a FAQ bot. If a user's question matches one in the list, show that answer. If not, ask ChatGPT." Students implement a loop to check the list. Auto‑grading tests with matching and non-matching questions.
- **CSTA:** E5‑PRO‑PF‑01, E5‑PRO‑DH‑02, E5‑DAA‑DF‑01.

### T22.G5.04 – Evaluate chatbot responses for accuracy and quality

- **Short name:** Assess the quality of AI output
- **Description:** Students learn to critically evaluate chatbot responses, checking for accuracy, clarity, bias, and appropriateness, and making notes on when the chatbot performed well or poorly.
- **Challenge format:** Concept, evaluation task. Students interact with a sample chatbot (or review transcripts) and rate responses on a rubric: accuracy, helpfulness, clarity, absence of bias. They write short explanations. Auto‑grading uses rubric and keyword matching for reasoning.
- **CSTA:** E5‑CAS‑ET‑02, E5‑ALG‑PS‑03.

---

## Grade 6

Grade 6 emphasizes designing chatbots for specific user needs, using tables to structure complex information, and considering societal impacts of AI information systems.

### T22.G6.01 – Design a chatbot for a specific audience

- **Short name:** Target a chatbot to a user group
- **Description:** Students consider who will use their chatbot (e.g., young learners, people with disabilities, non-native speakers) and design its language, tone, and features accordingly, applying human-centered design.
- **Challenge format:** Concept, design challenge. Prompt: "You are designing a chatbot for 3rd graders to learn about animals. Write a short description of how the chatbot should talk and what it should focus on. Then compare your design to one for university biology students." Students analyze differences. Auto‑grading checks for demonstration of audience-centered thinking.
- **CSTA:** MS‑ALG‑HD‑03, MS‑CAS‑ET‑04.

### T22.G6.02 – Use a table to store chatbot knowledge

- **Short name:** Organize information in a table for lookup
- **Description:** Students structure a chatbot's knowledge base as a table, where each row contains a question, category, and answer, enabling efficient searching and scalable information management.
- **Challenge format:** Coding, data structure exercise. Provided: an empty table and sample columns (question, category, answer). Prompt: "Create a biology FAQ table. Add 5 rows with questions about animals. Then build a chatbot that searches this table." Students populate the table and implement search logic. Auto‑grading checks table structure, population, and chatbot search functionality.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑DH‑04.

### T22.G6.03 – Combine ChatGPT with pre-trained knowledge

- **Short name:** Hybrid chatbot with facts and AI
- **Description:** Students build a chatbot that first checks a local knowledge base (list/table) and only uses ChatGPT if an answer is not found, balancing efficiency and flexibility.
- **Challenge format:** Coding, integration challenge. Provided: a knowledge table and a ChatGPT block. Prompt: "Build a chatbot that looks up the answer in your table first. If found, reply with that. If not found, ask ChatGPT and save the answer for future use." Students implement the hybrid logic. Auto‑grading tests both lookup and ChatGPT fallback paths.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑01.

### T22.G6.04 – Discuss bias and fairness in chatbot responses

- **Short name:** Examine bias in AI-generated answers
- **Description:** Students ask a chatbot questions that might elicit biased responses (e.g., about gender roles, cultural stereotypes) and analyze whether the responses are fair and inclusive, or if they reflect stereotypes.
- **Challenge format:** Concept, analysis and discussion. Students use a ChatGPT block to ask questions like "What jobs are best for men/women?" and "Describe a typical family." They evaluate responses for bias. Auto‑grading checks for thoughtful analysis and use of fairness criteria.
- **CSTA:** MS‑CAS‑ET‑04, MS‑ALG‑IM‑08.

---

## Grade 7

Grade 7 focuses on advanced conversational design, integrating external APIs or data sources into chatbots, and analyzing the societal impacts of information apps.

### T22.G7.01 – Design a multi-intent chatbot

- **Short name:** Chatbot that handles different user goals
- **Description:** Students design and build a chatbot that can recognize when a user wants different things (e.g., get information, ask for help, provide feedback) and respond appropriately to each intent.
- **Challenge format:** Coding, advanced design project. Prompt: "Create a chatbot for a school library. Users might want to search for a book, ask about hours, or request help. Design how the chatbot should identify the user's intent and respond." Students map intents to ChatGPT prompts or branching logic. Auto‑grading checks that multiple intents are handled.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑02.

### T22.G7.02 – Build a chatbot that learns from user feedback

- **Short name:** Chatbot that improves over time
- **Description:** Students implement a chatbot that logs user interactions and feedback, using the data to identify common questions or problematic responses to improve future versions.
- **Challenge format:** Coding, project with logging. Provided: a cloud variable or table to log interactions (question, answer, feedback). Prompt: "Build a chatbot that asks 'Was this answer helpful?' and stores feedback. Review the log to see what questions are common and which answers are poorly rated." Students implement logging and analyze results. Auto‑grading checks that interactions are logged and feedback is recorded.
- **CSTA:** MS‑PRO‑PF‑01, MS‑DAA‑DP‑05.

### T22.G7.03 – Integrate external data into chatbot responses

- **Short name:** Use live data in a chatbot
- **Description:** Students enhance a chatbot by fetching or referencing external data sources (e.g., a spreadsheet, an API call simulation, or sensor data) to provide current or dynamic information.
- **Challenge format:** Coding, extension challenge. Provided: a variable or table representing external data (e.g., class schedule, weather data). Prompt: "Create a 'School Info Bot' that uses a table of class schedules. When asked 'When is math class?' it looks up the schedule and answers based on current data." Students integrate the data reference. Auto‑grading checks that responses correctly pull from the data source.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑DH‑04.

### T22.G7.04 – Analyze societal impacts of chatbot misinformation

- **Short name:** Understand risks of AI information systems
- **Description:** Students investigate how chatbots can spread misinformation or false information, discuss the societal consequences, and brainstorm safeguards.
- **Challenge format:** Concept, research and analysis. Students read case studies or scenarios about misinformation from chatbots (e.g., medical misinformation, fake news). They analyze: "How could a chatbot spread false information?" "Who is harmed?" "What safeguards could help?" Auto‑grading uses rubric for depth of reasoning.
- **CSTA:** MS‑CAS‑ET‑06, MS‑DAA‑IM‑15.

---

## Grade 8

Grade 8 emphasizes advanced NLP/information retrieval, evaluating and improving chatbot performance systematically, and discussing ethical and societal implications of AI-powered information systems.

### T22.G8.01 – Extract key information from user input

- **Short name:** Parse user intent from natural language
- **Description:** Students implement logic to identify key entities or keywords in user questions (e.g., "Book by Roald Dahl" → extract "Roald Dahl" as author) to improve chatbot responses or data lookups.
- **Challenge format:** Coding, natural language processing task. Provided: user input strings and examples of entities to extract. Prompt: "Build a book search chatbot. When a user asks 'Find books by Stephen King,' extract 'Stephen King' and use that to search a database." Students use string operations or partial matching to identify entities. Auto‑grading tests extraction accuracy on varied inputs.
- **CSTA:** MS‑PRO‑PF‑01, MS‑DAA‑DP‑06.

### T22.G8.02 – Design and run chatbot performance tests

- **Short name:** Test chatbot accuracy and quality
- **Description:** Students create test cases for a chatbot (predefined questions with expected answers) and run them to measure accuracy, identifying which types of questions the chatbot handles well or poorly.
- **Challenge format:** Coding, testing and evaluation. Students create a list of test questions and expected answers, run the chatbot on each, and compare results. They calculate accuracy (% correct) and categorize errors. Auto‑grading checks test design and accuracy calculation.
- **CSTA:** MS‑PRO‑TR‑11, MS‑PRO‑PF‑01.

### T22.G8.03 – Compare different chatbot designs for a task

- **Short name:** Evaluate design trade-offs in chatbots
- **Description:** Students implement two different approaches to the same chatbot task (e.g., rule-based lookup vs. ChatGPT-only, or different prompt strategies) and compare them on metrics like accuracy, speed, and user satisfaction.
- **Challenge format:** Coding, comparative analysis. Prompt: "Build two versions of a FAQ bot: Version A uses a lookup table, Version B uses ChatGPT directly. Test both on the same questions and compare." Students measure accuracy and note speed/flexibility trade-offs. Auto‑grading checks that both versions exist and analysis is detailed.
- **CSTA:** MS‑PRO‑TR‑11, MS‑ALG‑AF‑02.

### T22.G8.04 – Discuss ethical design and deployment of information bots

- **Short name:** Ethics and responsibility in AI information systems
- **Description:** Students engage in structured discussion or written reflection about ethical responsibilities when deploying chatbots (e.g., transparency about AI use, managing user expectations, preventing harm, protecting privacy).
- **Challenge format:** Concept, debate and reflection. Scenarios: (1) A school chatbot helps students with homework but doesn't tell them it's AI. (2) A chatbot stores all user questions for analysis. (3) A health bot gives medical advice without disclaimers. Students evaluate each and discuss: Should the chatbot disclose it is AI? What data should be stored? What warnings are needed? Auto‑grading uses rubric assessing ethical reasoning and consideration of multiple perspectives.
- **CSTA:** MS‑CAS‑ET‑07, MS‑DAA‑IM‑15.

---
