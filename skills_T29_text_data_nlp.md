# T29 – Text Data & Introductory NLP: K–8 Skill List (Draft v1)

Topic reference: `T29 Text Data & Introductory NLP` in `domains_topics_overview.md`
Domain: Data & Analysis (D3) · CSTA focus: DAA‑DF, DAA‑DP, CAS‑ET (with links to PRO‑PF, ALG‑PS)

Each skill below has:

- a stable **ID** (`T29.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

At this stage, students are introduced to words and text through listening, speaking, and visual recognition. Text skills focus on awareness of patterns in language and simple word recognition rather than computational work.

### T29.GK.01 – Spot repeated words in a story

- **Short name:** Identify the same word appears again
- **Description:** Students listen to or read a short story and identify when a word repeats (e.g., the word "cat" appears three times). They recognize that words can repeat, connecting to the concept of frequency and pattern recognition in text.
- **Challenge format:** Concept, interactive story. A sprite reads aloud a simple story (3–5 sentences) with a clear repeated word (e.g., "The cat sat. The cat jumped. The cat slept."). Students click on or drag out an image representing each instance of the target word. Auto‑grading counts correct identifications.
- **CSTA:** EK‑DAA‑DF‑01 (Demonstrate how people create and collect data).

### T29.GK.02 – Match words to pictures

- **Short name:** Connect words to pictures
- **Description:** Students match simple written words to corresponding pictures (e.g., the word "dog" to a dog image), building early sight-word recognition and the understanding that text represents meaning.
- **Challenge format:** Concept, matching activity. Show 3–4 picture‑word pairs and scrambled labels; students click on or drag a word label to its matching picture. Auto‑grading checks correct matches.
- **CSTA:** EK‑DAA‑DF‑01.

### T29.GK.03 – Recognize initial letter sounds

- **Short name:** Spot words starting with a letter
- **Description:** Students identify words that start with a given letter or sound (e.g., words beginning with "B"). This builds foundational phonemic awareness and introduces letter–sound correspondence.
- **Challenge format:** Concept, multiple choice or click. Read or hear a target letter; show 4–5 word cards and ask "Which word starts with the letter B?" Students click the correct card. Auto‑grading validates the choice.
- **CSTA:** EK‑DAA‑DF‑01.

---

## Grade 1

Grade 1 focuses on simple text recognition, basic word analysis, and the idea that text can be searched, sorted, or counted within a CreatiCode project context.

### T29.G1.01 – Count words in a sentence

- **Short name:** How many words are in this sentence?
- **Description:** Students count the number of words in a short sentence or phrase, recognizing that text is made of discrete units. This is a foundational step toward text data collection and analysis.
- **Challenge format:** Concept, interactive text. Display a short sentence (e.g., "The cat sat down.") and ask "How many words?" Provide picture‑based or numeric answer choices (2, 4, 5, etc.). Auto‑grading compares to the correct word count.
- **CSTA:** E1‑DAA‑DF‑01 (Compare numeric and non‑numeric data).

### T29.G1.02 – Find a word in a list

- **Short name:** Search for a word in a list
- **Description:** Students locate a target word within a short list of words, introducing the concept of keyword search in its simplest form. This prepares the ground for later computational search.
- **Challenge format:** Coding, guided search project. Provided: a list variable with 5–8 words. A prompt asks "Is the word 'apple' in the list?" Students use a script with loop and conditional (or just ask the students to say yes/no from inspection) to find it. Auto‑grading checks if they correctly identify presence or absence.
- **CSTA:** E1‑DAA‑DF‑01, PRO‑PF.

### T29.G1.03 – Classify words by first letter

- **Short name:** Sort words by their first letter
- **Description:** Students organize a small set of words by their initial letter (e.g., words starting with A, B, C), building categorization skills that relate to data organization.
- **Challenge format:** Concept or light coding, drag-and-sort. Show a list of 6–8 words; students drag each word into one of 3 letter-category bins (A words, B words, C words). Auto‑grading checks correct grouping.
- **CSTA:** E1‑DAA‑DF‑01, DAA‑DP (organizing data).

### T29.G1.04 – Count how many times a word repeats

- **Short name:** How many times does the word appear?
- **Description:** Students count instances of a specific word in a short text, introducing the concept of word frequency in a very concrete way.
- **Challenge format:** Concept, interactive text. Display a short passage (e.g., "Sam likes cats. Cats are fun. Sam and cats play.") and ask "How many times does 'cats' (or 'Sam') appear?" Provide numeric answer choices. Auto‑grading compares to the actual count.
- **CSTA:** E1‑DAA‑DP‑01 (implied, organizing/counting data).

---

## Grade 2

Grade 2 introduces CreatiCode projects where students begin to work with text data in code: storing words in lists, performing simple keyword searches, and counting word frequencies programmatically.

### T29.G2.01 – Create a word list in a project

- **Short name:** Build a list of words in code
- **Description:** Students create a list variable and populate it with words (e.g., a list of animals), learning that text can be stored and managed as data within a project.
- **Challenge format:** Coding, starter project. Provided: a sprite and an empty list variable. Prompt: "Make a list of 5 animals." Students add items to the list using blocks. Auto‑grading checks that (1) the list contains approximately the right number of items and (2) items are recognizable words.
- **CSTA:** E2‑DAA‑DF‑01 (Collect data using multiple methods).

### T29.G2.02 – Search a word list for a keyword

- **Short name:** Find a word in your list
- **Description:** Students write a script that searches through a word list to find if a target word is present, introducing basic algorithmic search.
- **Challenge format:** Coding, starter project. Provided: a list of 5–8 words (e.g., animals) and a target word in a variable. Students create a loop that goes through the list and reports "Found!" or "Not found." Auto‑grading checks for correct output on multiple test cases (words present and absent).
- **CSTA:** E2‑PRO‑PF‑01, DAA‑DP (processing data).

### T29.G2.03 – Count a word's frequency in text

- **Short name:** Count how many times a word appears
- **Description:** Students write code that counts how many times a specific word appears in a given text (stored as a variable or list of words), applying iteration and a counter accumulator pattern.
- **Challenge format:** Coding, starter project. Provided: a text string or list and a target word. Students initialize a counter, loop through the text, increment the counter when they find a match, and display the final count. Auto‑grading checks the final count value against the reference answer.
- **CSTA:** E2‑DAA‑DP‑01 (Organize, filter, and manipulate data).

### T29.G2.04 – Sort words alphabetically

- **Short name:** Arrange words in alphabetical order
- **Description:** Students organize a list of words in alphabetical order (by first letter or by letter sequence), reinforcing understanding of text ordering and data organization.
- **Challenge format:** Concept or light coding, sorting activity. Show a list of 6–8 words; students drag them to arrange in A–Z order. Alternatively, provide a sorting block or custom block in CreatiCode. Auto‑grading checks final order.
- **CSTA:** E2‑DAA‑DP‑01.

---

## Grade 3

Grade 3 extends text analysis: students perform basic text transformations, extract parts of text, and begin to use CreatiCode's AI blocks for simple text classification or response tasks.

### T29.G3.01 – Extract the first letter of a word

- **Short name:** Get the first letter of a word
- **Description:** Students use text blocks (such as `letter 1 of [word]`) to extract the first character of a word, learning to manipulate strings at a character level.
- **Challenge format:** Coding, starter project. Provided: a word in a variable. Students use a block to extract and display the first letter. Auto‑grading checks the extracted character.
- **CSTA:** E3‑PRO‑PF‑01 (Programming fundamentals).

### T29.G3.02 – Check if text contains a specific substring

- **Short name:** Does the text contain this word?
- **Description:** Students use a `contains` block or write a simple check to determine if a text string includes a substring, extending keyword search to substrings.
- **Challenge format:** Coding, starter project. Provided: a text string and a substring to search for. Students use a block or short script to check and report true/false or yes/no. Auto‑grading validates the result.
- **CSTA:** E3‑PRO‑PF‑01, DAA‑DP.

### T29.G3.03 – Ask a question to an AI and receive a response

- **Short name:** Ask ChatGPT a question
- **Description:** Students use CreatiCode's ChatGPT block to send a simple text prompt and receive an AI-generated text response, introducing the concept of natural language processing and AI text generation in a beginner‑friendly way.
- **Challenge format:** Coding, guided project. Provided: a sprite and a prompt input mechanism (e.g., `ask` block or text input widget). Students insert a ChatGPT request block with a prompt (e.g., "What is the capital of France?") and have the sprite display the response. Auto‑grading checks that a response is generated and displayed.
- **CSTA:** E3‑PRO‑PF‑01, CAS‑ET‑02 (Impacts of computing).

### T29.G3.04 – Convert text to uppercase or lowercase

- **Short name:** Change text case
- **Description:** Students use text manipulation blocks to convert a string to uppercase or lowercase, learning basic text transformation.
- **Challenge format:** Coding, starter project. Provided: a text string in a variable. Students apply an uppercase or lowercase block and display the result. Auto‑grading checks the transformed output.
- **CSTA:** E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 builds on text analysis with more complex patterns: students analyze text for character and word properties, use AI to classify or summarize text, and begin working with basic natural language concepts.

### T29.G4.01 – Find the length of a text string

- **Short name:** How long is this text?
- **Description:** Students use a `length of` block to determine the number of characters in a text string, introducing measurement of text data.
- **Challenge format:** Coding, starter project. Provided: a text variable. Students use a length block and report the result. Auto‑grading checks the numeric output.
- **CSTA:** E4‑PRO‑PF‑01, DAA‑DF‑01.

### T29.G4.02 – Count words in a longer text passage

- **Short name:** How many words in the passage?
- **Description:** Students write code to count the number of words in a longer passage (split by spaces), applying string manipulation and counting logic.
- **Challenge format:** Coding, starter project. Provided: a multi‑sentence text. Students use blocks to split by spaces and count the resulting words list. Auto‑grading validates the word count.
- **CSTA:** E4‑PRO‑PF‑01, DAA‑DP‑01.

### T29.G4.03 – Use AI to classify text sentiment or topic

- **Short name:** Ask AI to describe text
- **Description:** Students write a prompt for ChatGPT that asks the AI to classify text (e.g., "Is this sentence happy or sad?") and process the AI's response, learning basic text classification.
- **Challenge format:** Coding, starter project. Provided: a sentence or short text in a variable. Students craft a ChatGPT prompt like "Classify the sentiment of this text: [text]. Answer only with 'positive', 'negative', or 'neutral'." and display the response. Auto‑grading checks that a valid classification was returned.
- **CSTA:** E4‑PRO‑PF‑01, CAS‑ET‑02 (Emerging tech impacts).

### T29.G4.04 – Remove spaces or punctuation from text

- **Short name:** Clean up text
- **Description:** Students use text blocks or write logic to strip spaces or punctuation from text, learning text preprocessing.
- **Challenge format:** Coding, starter project. Provided: text with spaces or punctuation. Students use `replace` blocks (if available) or write logic to remove them. Auto‑grading checks the cleaned output.
- **CSTA:** E4‑PRO‑PF‑01, DAA‑DP‑01 (Data processing/cleaning).

---

## Grade 5

Grade 5 deepens text analysis with statistics, data visualization of text properties, and more sophisticated AI applications like text summarization and keyword extraction.

### T29.G5.01 – Analyze word frequency in a list of words

- **Short name:** Find the most common word
- **Description:** Students analyze a list or passage of words to determine which word appears most frequently, combining counting and comparison skills to extract insights from text data.
- **Challenge format:** Coding, data analysis project. Provided: a list of words (simulating a simple corpus). Students loop through, count each word's occurrences, and identify the maximum. Auto‑grading checks the identified most‑frequent word.
- **CSTA:** E5‑DAA‑DP‑01 (Process data).

### T29.G5.02 – Visualize text data as a word frequency chart

- **Short name:** Show word counts as a chart
- **Description:** Students count word frequencies and create a visual representation (bar chart, stamping pattern, or simple graph) to display the data, connecting text analysis to data visualization.
- **Challenge format:** Coding, creative project. Provided: a passage and a framework for creating a bar chart (using stamping or sprite positioning). Students populate word counts, then visualize them. Auto‑grading checks that the chart reflects accurate counts and is visually sensible.
- **CSTA:** E5‑DAA‑DI‑01 (Data visualization/representation).

### T29.G5.03 – Use AI to summarize a text passage

- **Short name:** Ask AI to summarize text
- **Description:** Students use a ChatGPT prompt to summarize a longer passage, learning that AI can extract key information from text.
- **Challenge format:** Coding, starter project. Provided: a longer text passage (e.g., a paragraph from a story). Students craft a prompt like "Summarize this text in 2 sentences: [text]" and display the summary. Auto‑grading checks that a summary is generated and is reasonable in length.
- **CSTA:** E5‑PRO‑PF‑01, CAS‑ET‑02.

### T29.G5.04 – Extract keywords or main ideas from text

- **Short name:** Find the main words in text
- **Description:** Students use an AI prompt or simple heuristics to identify the most important words in a passage (keywords), learning basic natural language understanding concepts.
- **Challenge format:** Coding, starter project. Provided: a passage. Students send a prompt to ChatGPT like "Extract 3 keywords from this text: [text]. List only the keywords." and parse the response. Auto‑grading validates that keywords are relevant to the passage.
- **CSTA:** E5‑DAA‑DP‑01, CAS‑ET‑02.

---

## Grade 6

In middle school, students engage with more structured text data analysis: parsing and organizing text, using AI for more complex text tasks, and analyzing societal impacts of text analysis and AI.

### T29.G6.01 – Split text into words and store in a list

- **Short name:** Break text into words
- **Description:** Students use text manipulation blocks to split a passage by spaces into a list of words, a foundational text preprocessing step for many NLP tasks.
- **Challenge format:** Coding, starter project. Provided: a sentence or passage in a variable. Students use a `split` block (or equivalent) to create a list of words. Auto‑grading checks that the resulting list has the correct word count and content.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP‑03 (Use computational tools to collect and organize data).

### T29.G6.02 – Find all occurrences of a substring in text

- **Short name:** Find all instances of a word
- **Description:** Students write code that locates all instances of a substring within a text and reports their positions or count, extending basic search to complete pattern matching.
- **Challenge format:** Coding, starter project. Provided: a passage and a target substring. Students loop through the text, find matches, and store positions in a list or report the total count. Auto‑grading validates the list of positions or count.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP‑05 (Use computational tools to organize and filter data).

### T29.G6.03 – Classify text with AI into multiple categories

- **Short name:** Sort text into categories with AI
- **Description:** Students use ChatGPT with a well‑crafted prompt to classify multiple text samples into predefined categories (e.g., genre, sentiment, topic), learning prompt engineering and structured AI output.
- **Challenge format:** Coding, data classification project. Provided: a list of text samples. Students create a ChatGPT prompt like "Classify each of these as 'Happy', 'Sad', or 'Neutral': [sample1], [sample2], ..." and parse the response. Auto‑grading checks accuracy of classifications.
- **CSTA:** MS‑PRO‑PF‑01, CAS‑ET‑04 (Evaluate how design decisions influence user experiences).

### T29.G6.04 – Analyze text data and report statistics

- **Short name:** Compute text statistics
- **Description:** Students compute statistics on text data, such as average word length, sentence count, or vocabulary diversity, learning to extract quantitative insights from qualitative data.
- **Challenge format:** Coding, data analysis project. Provided: a passage. Students compute metrics like (1) average word length, (2) number of unique words, or (3) longest word. Auto‑grading checks computed values.
- **CSTA:** MS‑DAA‑DP‑05, MS‑DAA‑DP‑06 (Manipulate data, compute new variables).

---

## Grade 7

Grade 7 emphasizes complex text operations, AI-driven insights from text, and critical thinking about the societal implications of text processing and natural language understanding.

### T29.G7.01 – Pre‑process text for analysis

- **Short name:** Prepare text for analysis
- **Description:** Students perform multiple preprocessing steps on text (remove punctuation, convert to lowercase, trim spaces, remove common words) to prepare it for analysis or AI processing, learning data cleaning for text.
- **Challenge format:** Coding, data preprocessing project. Provided: messy text with mixed case, punctuation, and extra spaces. Students apply a sequence of text transformation blocks and output cleaned text. Auto‑grading compares the cleaned result to a reference.
- **CSTA:** MS‑DAA‑DP‑07 (Identify errors and ways to fix them).

### T29.G7.02 – Compute text similarity or comparison

- **Short name:** Compare how similar two texts are
- **Description:** Students use AI or string matching logic to assess similarity between two text passages, learning that text similarity can be computed and compared.
- **Challenge format:** Coding, comparison project. Provided: two text passages. Students either (1) ask ChatGPT "How similar are these two texts? Answer with a number 1-10" or (2) count shared words as a simple similarity metric. Auto‑grading validates the comparison output.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP‑06 (Manipulate data).

### T29.G7.03 – Use AI to answer questions based on a text passage

- **Smart Retrieval:** Ask AI questions about text
- **Description:** Students use a ChatGPT prompt that provides context (e.g., a passage) and asks a question about it, learning how AI can retrieve and synthesize information from text.
- **Challenge format:** Coding, question‑answering project. Provided: a passage. Students ask ChatGPT: "Based on this text: [passage], what is [question]?" and process the response. Auto‑grading checks answer validity against expected responses.
- **CSTA:** MS‑PRO‑PF‑01, CAS‑ET‑05 (Emerging technologies in innovative ways).

### T29.G7.04 – Reflect on bias and fairness in text data and AI responses

- **Short name:** Think about bias in text and AI
- **Description:** Students examine how text datasets or AI models might reflect or introduce bias, learning critical thinking about text processing and AI fairness.
- **Challenge format:** Concept, analysis and reflection. Provide scenarios like "A chatbot trained on old texts gives advice that doesn't reflect modern diversity. Why might this happen? How could it be improved?" Students select or write structured responses explaining bias sources and mitigation. Auto‑grading scores key concepts (representation, training data, fairness).
- **CSTA:** MS‑CAS‑ET‑04, MS‑CAS‑ET‑07 (Emerging technology evaluation).

---

## Grade 8

Grade 8 builds toward high school expectations with sophisticated text analysis, multi-step AI applications, and in‑depth exploration of the ethical and societal dimensions of natural language processing and AI.

### T29.G8.01 – Build a keyword search and retrieval system

- **Short name:** Create a keyword search tool
- **Description:** Students design a project that takes user input (keywords) and searches a collection of text documents (or passages in a list), returning matching documents. This is a simplified version of real search engines.
- **Challenge format:** Coding, project design. Provided: a list of text passages (simulating documents). Students create a search interface (input field, button) and code that filters documents by keyword presence. Auto‑grading checks that search returns correct matching documents and doesn't return non‑matching ones.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP‑05, ALG‑PS (Problem solving).

### T29.G8.02 – Analyze sentiment or emotion in multiple texts using AI

- **Short name:** Analyze emotions in text samples
- **Description:** Students apply an AI model (via ChatGPT) to analyze sentiment or emotion in a batch of text samples, then aggregate and visualize the results (e.g., how many positive, negative, neutral texts are in the set).
- **Challenge format:** Coding, batch analysis project. Provided: a list of text samples (e.g., student reviews or social media‑style posts). Students loop through, send each to ChatGPT for sentiment analysis, record results in a table or list, and compute counts. Auto‑grading checks the accuracy of classifications and aggregates.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP‑05, MS‑DAA‑DI‑03 (Data investigation).

### T29.G8.03 – Extract entities or relationships from text using AI

- **Short name:** Find names and connections in text
- **Description:** Students use AI (ChatGPT) to extract named entities (people, places, organizations) or relationships from text, learning that AI can identify and structure information from unstructured text.
- **Challenge format:** Coding, information extraction project. Provided: a passage (e.g., a news article or story). Students craft prompts like "Extract all person names and place names from this text: [passage]" or "Who is talking to whom in this dialogue?" and parse the AI's response into structured lists. Auto‑grading validates extracted entities.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP‑06, CAS‑ET‑06 (How emerging tech transforms existing processes).

### T29.G8.04 – Evaluate the ethical implications of text processing and NLP

- **Short name:** Discuss ethics of text AI
- **Description:** Students analyze and discuss complex issues: how NLP systems might perpetuate biases, privacy concerns with text collection, and the use of NLP in surveillance or manipulation. They propose mitigations.
- **Challenge format:** Concept, structured debate or essay. Provide scenarios (e.g., "A school analyzes student emails for mental health risk; privacy advocates worry about misuse") and ask students to identify ethical issues, stakeholders affected, and potential solutions. Auto‑grading uses rubrics scoring understanding of stakeholders, ethical tensions, and proposed mitigations.
- **CSTA:** MS‑CAS‑ET‑06, MS‑CAS‑ET‑07 (Societal impacts of emerging tech).

---
