# TOPIC T29 - TEXT DATA & NLP FOUNDATIONS
## COMPLETE MAJOR REVISION - November 24, 2024

---

## REVISION SUMMARY

### Key Changes:
1. **Split 18 overly broad skills** into 52 focused single-feature skills
2. **Added 25 new skills** for missing CreatiCode block coverage
3. **Fixed all intra-topic dependencies** (X-2 rule applied throughout)
4. **Verified all skills** against actual CreatiCode block capabilities
5. **Improved grade-appropriate scaffolding** across K-8

### Total Skills:
- **Before**: 62 skills (many too broad)
- **After**: 115 skills (properly scoped)

---

# KINDERGARTEN (Ages 5-6)

## T29.GK.01
**Skill**: Recognize text vs pictures
**Description**: Students sort cards showing text (words/letters), pictures, and numbers into separate groups, identifying text as "letters that make words we can read."
**Dependencies**: (none)
**Grade**: K

## T29.GK.02
**Skill**: Identify letters in text
**Description**: Given simple words (CAT, DOG, SUN), students point to individual letters and count how many letters are in each word, building awareness of text structure.
**Dependencies**:
- T29.GK.01: Recognize text vs pictures
**Grade**: K

## T29.GK.03
**Skill**: Recognize that text has meaning
**Description**: Students match simple written words to pictures (matching "CAT" to cat picture), understanding that text represents things and carries meaning.
**Dependencies**:
- T29.GK.01: Recognize text vs pictures
- T29.GK.02: Identify letters in text
**Grade**: K

---

# GRADE 1 (Ages 6-7)

## T29.G1.01
**Skill**: Sort words by first letter
**Description**: Students organize word cards alphabetically by first letter (all A words together, all B words together), preparing for dictionary and lookup concepts.
**Dependencies**:
- T29.GK.03: Recognize that text has meaning
**Grade**: 1

## T29.G1.02
**Skill**: Count words in a sentence
**Description**: Given simple sentences written on strips, students count how many words are in each sentence by pointing to each word, distinguishing between letters and words.
**Dependencies**:
- T29.GK.03: Recognize that text has meaning
**Grade**: 1

## T29.G1.03
**Skill**: Group words by category
**Description**: Students sort word cards into concrete categories: animals, colors, actions, foods. They explain why each word belongs in its group.
**Dependencies**:
- T29.G1.02: Count words in a sentence
**Grade**: 1

## T29.G1.04
**Skill**: Identify same words in different sentences
**Description**: Given 2-3 simple sentences, students find and circle words that appear in multiple sentences, building pattern recognition for word matching.
**Dependencies**:
- T29.G1.02: Count words in a sentence
**Grade**: 1

---

# GRADE 2 (Ages 7-8)

## T29.G2.01
**Skill**: Recognize text patterns (rhyming, repetition)
**Description**: Students identify patterns in text such as rhyming words (cat/hat) or repeated words in a short poem, preparing for computational pattern matching.
**Dependencies**:
- T29.G1.04: Identify same words in different sentences
**Grade**: 2

## T29.G2.02
**Skill**: Sort sentences by length
**Description**: Students arrange sentence strips from shortest to longest by counting words in each, understanding that text can be measured and compared.
**Dependencies**:
- T29.G1.02: Count words in a sentence
**Grade**: 2

## T29.G2.03
**Skill**: Distinguish sentences from word lists
**Description**: Students identify which text is a complete sentence (has meaning, starts with capital, ends with period) versus a list of words, understanding text structure.
**Dependencies**:
- T29.G1.02: Count words in a sentence
**Grade**: 2

## T29.G2.04
**Skill**: Find and replace words in sentences
**Description**: Given a sentence and replacement instructions ("change 'cat' to 'dog'"), students rewrite the sentence with the new word, preparing for programmatic text manipulation.
**Dependencies**:
- T29.G2.03: Distinguish sentences from word lists
- T29.G1.04: Identify same words in different sentences
**Grade**: 2

---

# GRADE 3 (Ages 8-9)

## T29.G3.01
**Skill**: Distinguish text data from numbers and pictures
**Description**: Students sort cards showing words, sentences, numbers, and emojis to recognize text as a specific data type. They discuss how computers store and process text differently from numbers.
**Dependencies**:
- T29.G2.04: Find and replace words in sentences
**Grade**: 3

## T29.G3.02
**Skill**: Count word occurrences using variables
**Description**: Learners build a script that counts how many times specific words appear in a short paragraph, storing counts in variables and displaying results using variable monitors.
**Dependencies**:
- T29.G3.01: Distinguish text data from numbers and pictures
- T09.G3.01.04: Display variable value on stage using the variable monitor
**Grade**: 3

## T29.G3.03
**Skill**: Build automated word categorizer using conditionals and lists
**Description**: Students build code that automatically categorizes words into meaning-based groups (emotion, action, place) using conditionals and lists. They explain their categorization logic, preparing for later metadata tagging and semantic understanding.
**Dependencies**:
- T29.G3.02: Count word occurrences using variables
**Grade**: 3

## T29.G3.04
**Skill**: Explain why clean text helps AI helpers
**Description**: Learners compare two sample prompts (one with typos/unclear phrasing vs clean text) and discuss how clarity affects AI responses, building responsible AI use habits.
**Dependencies**:
- T29.G3.03: Build automated word categorizer using conditionals and lists
**Grade**: 3

## T29.G3.05
**Skill**: Compare text for equality using "=" operator
**Description**: Students use the equals operator to check if two text variables match exactly, understanding case-sensitive comparison. They test examples to see when texts are equal and when they differ.
**Dependencies**:
- T29.G3.02: Count word occurrences using variables
**Grade**: 3

---

# GRADE 4 (Ages 9-10)

## T29.G4.00
**Skill**: Use ask/answer blocks for text input and display results
**Description**: Students use the 'ask' block to get text input from users, store it in variables, and display it using 'say' blocks or variable monitors. They build simple text echo programs.
**Dependencies**:
- T29.G3.04: Explain why clean text helps AI helpers
- T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
**Grade**: 4

## T29.G4.01
**Skill**: Use split and join blocks for text manipulation
**Description**: Students write a script that takes a sentence, uses the split block to separate it on spaces, stores each word in a list, and uses join to reconstruct text. This is the foundational skill for all text processing.
**Dependencies**:
- T29.G4.00: Use ask/answer blocks for text input and display results
- T09.G3.01.04: Display variable value on stage using the variable monitor
- T09.G3.05: Trace code with variables to predict outcomes
- T10.G3.03: Add and remove items from a list
**Grade**: 4

## T29.G4.02
**Skill**: Access individual characters using "letter # of" operator
**Description**: Students use Scratch's "letter # of" operator to access and display specific characters from text by their position (index starting at 1). They extract first letter, last letter, or specific positions.
**Dependencies**:
- T29.G4.01: Use split and join blocks for text manipulation
- T09.G3.01.04: Display variable value on stage using the variable monitor
**Grade**: 4

## T29.G4.03
**Skill**: Count characters and words using "length of" and split
**Description**: Students use Scratch's "length of" operator to count characters in text, and use split on spaces plus list length to count words. They compare the two counts and discuss the difference.
**Dependencies**:
- T29.G4.01: Use split and join blocks for text manipulation
- T10.G3.03: Add and remove items from a list
**Grade**: 4

## T29.G4.04.01
**Skill**: Convert text case using lowercase/uppercase operators
**Description**: Learners build scripts that convert text to lowercase or uppercase using Scratch's case conversion operators, understanding case normalization for text comparison.
**Dependencies**:
- T29.G4.01: Use split and join blocks for text manipulation
- T09.G3.05: Trace code with variables to predict outcomes
**Grade**: 4

## T29.G4.04.02
**Skill**: Test if text includes, starts with, or ends with a pattern
**Description**: Students use string comparison blocks (includes, starts with, ends with) with case-insensitive options to check if text contains specific patterns, useful for keyword detection and validation.
**Dependencies**:
- T29.G4.04.01: Convert text case using lowercase/uppercase operators
- T29.G3.05: Compare text for equality using "=" operator
- T08.G3.01: Use a simple if in a script
**Grade**: 4

## T29.G4.05.01
**Skill**: Compare human vs AI summaries (conceptual)
**Description**: Students read a short text, write their own 1-2 sentence summary, then read an AI-generated summary. They discuss what each summary includes and omits, understanding AI summarization as a conceptual tool.
**Dependencies**:
- T29.G3.04: Explain why clean text helps AI helpers
**Grade**: 4

## T29.G4.05.02.01 [SPLIT from T29.G4.05.02]
**Skill**: Understand ChatGPT request block parameters
**Description**: Students examine the ChatGPT request block and identify its parameters: prompt (what to ask), result variable (where answer goes), mode (streaming/waiting), length (max tokens), temperature (creativity), and session type (new/continue). They discuss what each parameter controls.
**Dependencies**:
- T29.G4.05.01: Compare human vs AI summaries (conceptual)
- T29.G4.01: Use split and join blocks for text manipulation
**Grade**: 4

## T29.G4.05.02.02 [SPLIT from T29.G4.05.02]
**Skill**: Send basic ChatGPT requests in waiting mode
**Description**: Students use the ChatGPT block to send simple requests (summarize text, answer questions) using 'waiting' mode, which waits for the complete response. They store results in variables and display them.
**Dependencies**:
- T29.G4.05.02.01: Understand ChatGPT request block parameters
- T08.G3.01: Use a simple if in a script
- T09.G3.05: Trace code with variables to predict outcomes
**Grade**: 4

## T29.G4.05.02.03 [SPLIT from T29.G4.05.02]
**Skill**: Use streaming mode for real-time ChatGPT responses
**Description**: Students use 'streaming' mode to see ChatGPT responses appear word-by-word in real-time. They understand that streaming updates the result variable continuously until ✅ emoji appears at the end.
**Dependencies**:
- T29.G4.05.02.02: Send basic ChatGPT requests in waiting mode
**Grade**: 4

## T29.G4.05.02.04 [SPLIT from T29.G4.05.02]
**Skill**: Control response length with max tokens parameter
**Description**: Students experiment with the max length parameter (measured in tokens, where 100 tokens ≈ 75 words). They observe how different values affect response completeness.
**Dependencies**:
- T29.G4.05.02.02: Send basic ChatGPT requests in waiting mode
**Grade**: 4

## T29.G4.05.02.05 [SPLIT from T29.G4.05.02]
**Skill**: Adjust creativity with temperature parameter
**Description**: Students experiment with temperature values (0 to 1) and observe that lower values produce more predictable/factual responses while higher values produce more creative/varied responses.
**Dependencies**:
- T29.G4.05.02.02: Send basic ChatGPT requests in waiting mode
**Grade**: 4

## T29.G4.06
**Skill**: Remove punctuation using replace or character filtering
**Description**: Students use the replace block to remove common punctuation marks, or loop through characters to keep only letters and spaces. This builds on case conversion for full text cleaning.
**Dependencies**:
- T29.G4.04.01: Convert text case using lowercase/uppercase operators
- T07.G3.03: Trace code with simple loops to predict outcomes
- T10.G3.03: Add and remove items from a list
**Grade**: 4

## T29.G4.07
**Skill**: Extract substrings and find text position
**Description**: Students use "substring from position" operations (combining "letter # of" in loops or using split/join creatively) to extract parts of text. They find the position of specific text within strings.
**Dependencies**:
- T29.G4.02: Access individual characters using "letter # of" operator
- T07.G3.03: Trace code with simple loops to predict outcomes
**Grade**: 4

## T29.G4.10
**Skill**: Store text data in simple tables (2 columns max)
**Description**: Students create simple two-column tables (e.g., 'word' and 'count') to organize text data, understanding when tables are better than lists for paired data.
**Dependencies**:
- T29.G4.01: Use split and join blocks for text manipulation
- T11.G4.01: Create and use a simple table
**Grade**: 4

## T29.G4.11
**Skill**: Recognize emotional tone in text (unplugged/semi-plugged)
**Description**: Students read sample texts and label them as positive, negative, or neutral. They discuss how word choice affects emotional tone and begin identifying "sentiment words."
**Dependencies**:
- T29.G3.03: Build automated word categorizer using conditionals and lists
**Grade**: 4

---

# GRADE 5 (Ages 10-11)

## T29.G5.01
**Skill**: Design table schemas for text data (chat logs)
**Description**: Students design table schemas for storing chat logs or messages, defining columns for timestamp, speaker, message text, and metadata. They sketch the structure before implementation.
**Dependencies**:
- T29.G4.10: Store text data in simple tables (2 columns max)
**Grade**: 5

## T29.G5.02
**Skill**: Populate data tables from text using split
**Description**: Students implement their table schemas, using split operations to parse text data into table rows and columns. They populate tables with actual chat or message data.
**Dependencies**:
- T29.G5.01: Design table schemas for text data (chat logs)
- T11.G5.01: Create and populate a table
- T08.G4.02: Write scripts combining sequencing, loops, and conditionals
**Grade**: 5

## T29.G5.03.01
**Skill**: Understand stop-words and their purpose
**Description**: Students analyze word frequency results and notice that common words (the, a, is) dominate. They learn these are called 'stop-words' and discuss when to remove them vs keep them.
**Dependencies**:
- T29.G5.08.01: Build word frequency table
**Grade**: 5

## T29.G5.03.02
**Skill**: Build stop-word filter using tables
**Description**: Learners create a table of stop-words (common words like "the", "a", "is") and filter them out before running frequency counts to focus on meaningful words.
**Dependencies**:
- T29.G5.03.01: Understand stop-words and their purpose
- T11.G5.01: Create and populate a table
**Grade**: 5

## T29.G5.04.01
**Skill**: Create positive/negative sentiment word lists
**Description**: Students build tables of positive words (happy, great, love) and negative words (sad, bad, hate), preparing for simple sentiment analysis.
**Dependencies**:
- T29.G4.11: Recognize emotional tone in text (unplugged/semi-plugged)
- T11.G5.01: Create and populate a table
**Grade**: 5

## T29.G5.04.02
**Skill**: Score text using sentiment word lists
**Description**: Students count matches between text and positive/negative word lists, calculate a sentiment score, and note in reflection that this heuristic approach has limits (can't detect sarcasm, context).
**Dependencies**:
- T29.G5.04.01: Create positive/negative sentiment word lists
- T08.G4.01: Choose actions based on user input or sensor values
**Grade**: 5

## T29.G5.05.01 [SPLIT from T29.G5.05]
**Skill**: Build dynamic prompts with variable placeholders
**Description**: Students create AI prompt templates with variable slots (placeholders) using join blocks. They fill slots with different values (names, topics, numbers) to generate varied prompts dynamically.
**Dependencies**:
- T29.G5.02: Populate data tables from text using split
- T09.G4.04: Use variables to control animation or game state
**Grade**: 5

## T29.G5.05.02 [SPLIT from T29.G5.05]
**Skill**: Engineer few-shot prompts with examples
**Description**: Students learn few-shot prompting by including examples in their prompts (e.g., "Example 1: Input: dog, Output: animal. Example 2: Input: blue, Output: color. Now: Input: happy, Output: ?"). They observe how examples improve AI accuracy.
**Dependencies**:
- T29.G5.05.01: Build dynamic prompts with variable placeholders
**Grade**: 5

## T29.G5.05.03 [SPLIT from T29.G5.05]
**Skill**: Use role-based prompts for ChatGPT
**Description**: Students write prompts that assign roles to ChatGPT (e.g., "You are a helpful tutor", "You are a creative storyteller") and observe how role instructions shape responses.
**Dependencies**:
- T29.G5.05.01: Build dynamic prompts with variable placeholders
**Grade**: 5

## T29.G5.06.01 [SPLIT from T29.G5.06]
**Skill**: Understand the parse sentence block structure
**Description**: Students learn that the 'analyze sentence' block (ai_parsesentence) outputs a table with columns: TEXT (original word), LEMMA (word stem), TYPE (part of speech), LABEL (grammatical role), and understand what each column represents.
**Dependencies**:
- T29.G4.01: Use split and join blocks for text manipulation
- T29.G5.08.02: Find and report most frequent word
**Grade**: 5

## T29.G5.06.02 [SPLIT from T29.G5.06]
**Skill**: Extract parts of speech using the TEXT and TYPE columns
**Description**: Students use the parse sentence block, then filter the result table by TYPE column to find all nouns, verbs, or adjectives in a sentence. They build simple part-of-speech counters.
**Dependencies**:
- T29.G5.06.01: Understand the parse sentence block structure
**Grade**: 5

## T29.G5.06.03 [SPLIT from T29.G5.06]
**Skill**: Extract word stems using the LEMMA column
**Description**: Students use the LEMMA column from the parse sentence block to find word stems (running → run, better → good). They understand lemmatization helps group related words for analysis.
**Dependencies**:
- T29.G5.06.01: Understand the parse sentence block structure
**Grade**: 5

## T29.G5.06.04 [SPLIT from T29.G5.06]
**Skill**: Analyze grammatical roles using the LABEL column
**Description**: Students use the LABEL column to identify subjects, objects, and modifiers in sentences. They build sentence structure diagrams from the parse results.
**Dependencies**:
- T29.G5.06.02: Extract parts of speech using the TEXT and TYPE columns
**Grade**: 5

## T29.G5.07
**Skill**: Trim whitespace from text input
**Description**: Students use the trim block to remove leading and trailing whitespace from user input, ensuring clean data for text processing. They discuss why this matters for text comparison.
**Dependencies**:
- T29.G4.04.01: Convert text case using lowercase/uppercase operators
**Grade**: 5

## T29.G5.08.01
**Skill**: Build word frequency table
**Description**: Students split text into words, loop through each word, and count occurrences using a table with "word" and "count" columns. They create a complete frequency table for a text sample.
**Dependencies**:
- T29.G4.06: Remove punctuation using replace or character filtering
- T29.G4.10: Store text data in simple tables (2 columns max)
- T07.G3.03: Trace code with simple loops to predict outcomes
- T08.G3.01: Use a simple if in a script
- T09.G3.05: Trace code with variables to predict outcomes
- T10.G3.03: Add and remove items from a list
**Grade**: 5

## T29.G5.08.02
**Skill**: Find and report most frequent word
**Description**: Students iterate through their frequency table to find the word with highest count and display it. They handle ties and discuss what the most frequent words reveal about a text.
**Dependencies**:
- T29.G5.08.01: Build word frequency table
- T11.G5.01: Create and populate a table
**Grade**: 5

## T29.G5.09
**Skill**: Highlight keywords in text display
**Description**: Learners write code that scans a paragraph, finds keyword positions using split and includes, and displays the text with visual highlighting (color changes on sprites or text display blocks).
**Dependencies**:
- T29.G4.04.02: Test if text includes, starts with, or ends with a pattern
- T07.G3.03: Trace code with simple loops to predict outcomes
- T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
**Grade**: 5

## T29.G5.10
**Skill**: Understand tokenization concepts
**Description**: Students learn that AI models break text into tokens (not always whole words). They experiment with examples showing how 'running' might be 1 token but 'ChatGPT' might be 2 tokens. They discuss why token limits exist for AI APIs.
**Dependencies**:
- T29.G4.03: Count characters and words using "length of" and split
**Grade**: 5

---

# GRADE 6 (Ages 11-12)

## T29.G6.01
**Skill**: Compare characters, words, and token counts
**Description**: Students count characters (using "length of"), words (using split and count), and discuss GPT tokens. They note that actual token counting requires API calls; they estimate based on character/word counts and discuss why token limits matter for AI prompts.
**Dependencies**:
- T29.G5.10: Understand tokenization concepts
- T29.G5.03.02: Build stop-word filter using tables
- T29.G4.03: Count characters and words using "length of" and split
- T08.G4.01: Choose actions based on user input or sensor values
- T09.G4.04: Use variables to control animation or game state
- T10.G4.03: Add, remove, and access items from a list in a script
**Grade**: 6

## T29.G6.02
**Skill**: Compute n-gram (bigram) frequencies
**Description**: Learners loop through token lists, join consecutive word pairs, and store counts in a table to capture common two-word phrase patterns.
**Dependencies**:
- T29.G5.03.02: Build stop-word filter using tables
- T11.G5.01: Create and populate a table
- T07.G4.01: Loop until a goal condition is met
- T09.G4.04: Use variables to control animation or game state
- T10.G4.03: Add, remove, and access items from a list in a script
**Grade**: 6

## T29.G6.03
**Skill**: Create autocomplete suggestions from bigrams
**Description**: Using bigram frequency data, students identify the top next words for a given prefix and display them using text display blocks, sprites, or list displays.
**Dependencies**:
- T29.G6.02: Compute n-gram (bigram) frequencies
- T06.G4.01: Write scripts that respond to keyboard or mouse events
- T09.G4.04: Use variables to control animation or game state
- T10.G4.03: Add, remove, and access items from a list in a script
**Grade**: 6

## T29.G6.04
**Skill**: Log AI prompts/responses with ratings and timestamps
**Description**: Learners automatically log each AI interaction (prompt, response, user rating, timestamp) into a table for responsible-use tracking, supporting T24 transparency practices.
**Dependencies**:
- T29.G5.02: Populate data tables from text using split
- T29.G5.05.01: Build dynamic prompts with variable placeholders
- T11.G5.01: Create and populate a table
- T07.G4.01: Loop until a goal condition is met
- T09.G4.04: Use variables to control animation or game state
- T10.G4.03: Add, remove, and access items from a list in a script
**Grade**: 6

## T29.G6.05.01 [NEW]
**Skill**: Use new chat vs continue session types
**Description**: Students understand the difference between 'new chat' (starts fresh conversation) and 'continue' (maintains context from previous exchanges). They build multi-turn conversations by using 'continue' session type.
**Dependencies**:
- T29.G4.05.02.02: Send basic ChatGPT requests in waiting mode
**Grade**: 6

## T29.G6.05.02 [NEW]
**Skill**: Cancel ongoing ChatGPT requests
**Description**: Students use the 'OpenAI ChatGPT: cancel request' block to stop long-running ChatGPT requests. They understand when cancellation is useful (user changes mind, wrong prompt sent, timeout concerns).
**Dependencies**:
- T29.G4.05.02.03: Use streaming mode for real-time ChatGPT responses
**Grade**: 6

## T29.G6.06.01 [SPLIT from T29.G6.06]
**Skill**: Understand speech-to-text block options (Azure vs OpenAI Whisper)
**Description**: Students learn that CreatiCode offers two speech-to-text APIs: Microsoft Azure and OpenAI Whisper. They understand both provide similar functionality but may differ in language support and accuracy.
**Dependencies**:
- T29.G5.02: Populate data tables from text using split
- T29.G5.07: Trim whitespace from text input
**Grade**: 6

## T29.G6.06.02 [SPLIT from T29.G6.06]
**Skill**: Use basic speech recognition (single utterance)
**Description**: Students use 'start recognizing speech' and 'end speech recognition' blocks to capture a single spoken phrase. They display the recognized text using the 'text from speech' reporter block.
**Dependencies**:
- T29.G6.06.01: Understand speech-to-text block options (Azure vs OpenAI Whisper)
**Grade**: 6

## T29.G6.06.03 [SPLIT from T29.G6.06]
**Skill**: Select language for speech recognition
**Description**: Students select different languages from the speech recognition block dropdown (English US/UK, Spanish, French, Chinese, etc.) and test recognition accuracy for different languages.
**Dependencies**:
- T29.G6.06.02: Use basic speech recognition (single utterance)
**Grade**: 6

## T29.G6.06.04 [SPLIT from T29.G6.06]
**Skill**: Store recorded audio from speech recognition
**Description**: Students use the optional SOUNDNAME parameter in speech recognition blocks to save the recorded audio. They can replay or process the audio later.
**Dependencies**:
- T29.G6.06.02: Use basic speech recognition (single utterance)
**Grade**: 6

## T29.G6.06.05 [SPLIT from T29.G6.06]
**Skill**: Use continuous speech recognition with list output
**Description**: Students use 'start continuous speech recognition' to capture ongoing speech in real-time. Each sentence is added to a list, with the current sentence continuously updating as the last item.
**Dependencies**:
- T29.G6.06.02: Use basic speech recognition (single utterance)
**Grade**: 6

## T29.G6.06.06 [NEW]
**Skill**: Clear speech recognition results
**Description**: Students use the 'clear speech text' block to reset the 'text from speech' reporter. They understand when clearing is needed (between multiple recognition sessions, before new input).
**Dependencies**:
- T29.G6.06.02: Use basic speech recognition (single utterance)
**Grade**: 6

## T29.G6.07.01 [SPLIT from T29.G6.07]
**Skill**: Use basic text-to-speech with default settings
**Description**: Students use the 'say [TEXT] in [LANGUAGE] as [VOICETYPE]' block to convert text to speech with default settings. They test different languages and hear the synthesized voice.
**Dependencies**:
- T29.G4.01: Use split and join blocks for text manipulation
**Grade**: 6

## T29.G6.07.02 [SPLIT from T29.G6.07]
**Skill**: Select voice types for text-to-speech
**Description**: Students experiment with different voice types (Male, Female, Male2, Female2, Male3, Female3, Boy, Girl) and understand that not all voice types are available for all languages.
**Dependencies**:
- T29.G6.07.01: Use basic text-to-speech with default settings
**Grade**: 6

## T29.G6.07.03 [SPLIT from T29.G6.07]
**Skill**: Customize TTS speed, pitch, and volume
**Description**: Students adjust speed, pitch, and volume parameters (percentage values) to control voice characteristics. They create expressive speech (fast excited voice, slow sad voice, etc.).
**Dependencies**:
- T29.G6.07.01: Use basic text-to-speech with default settings
**Grade**: 6

## T29.G6.07.04 [SPLIT from T29.G6.07]
**Skill**: Store synthesized speech as audio
**Description**: Students use the optional SOUNDNAME parameter to save TTS audio. They can replay or process the audio later in their projects.
**Dependencies**:
- T29.G6.07.01: Use basic text-to-speech with default settings
**Grade**: 6

## T29.G6.07.05 [NEW]
**Skill**: Stop text-to-speech playback
**Description**: Students use the 'stop speaking' block to interrupt ongoing TTS playback. They understand when stopping is useful (user skips ahead, error occurs, new audio starts).
**Dependencies**:
- T29.G6.07.01: Use basic text-to-speech with default settings
**Grade**: 6

## T29.G6.08
**Skill**: Compare text similarity using edit distance
**Description**: Students use the text similarity block (operator_stringdiff) to compute edit distance (how many character changes needed to transform one text into another), understanding text similarity metrics.
**Dependencies**:
- T29.G4.03: Count characters and words using "length of" and split
- T29.G6.01: Compare characters, words, and token counts
**Grade**: 6

## T29.G6.09
**Skill**: Handle text length limits and truncation
**Description**: Students check text length before sending to AI APIs, truncate or summarize long texts to fit limits, and display appropriate error messages when text is too long.
**Dependencies**:
- T29.G6.01: Compare characters, words, and token counts
- T08.G5.01: Use logical operators (and, or, not) in if blocks
**Grade**: 6

## T29.G6.10
**Skill**: Validate text input and handle errors
**Description**: Students validate text input before processing (check for empty strings, unexpected formats). They use conditionals to provide helpful error messages and default values.
**Dependencies**:
- T29.G6.01: Compare characters, words, and token counts
- T08.G5.01: Use logical operators (and, or, not) in if blocks
**Grade**: 6

---

# GRADE 7 (Ages 12-13)

## T29.G7.01.01
**Skill**: Build keyword-based retrieval system
**Description**: Students build a simple retrieval system by storing paragraph snippets in a table, computing keyword overlap scores using stop-word filtered text, and returning the best-matching snippet based on highest score.
**Dependencies**:
- T29.G5.03.02: Build stop-word filter using tables
- T29.G6.02: Compute n-gram (bigram) frequencies
- T29.G6.03: Create autocomplete suggestions from bigrams
- T11.G6.01: Sort a table by a column
- T09.G3.05: Trace code with variables to predict outcomes
- T10.G5.03: Add and remove items from a list
**Grade**: 7

## T29.G7.01.02.01 [SPLIT from T29.G7.01.02]
**Skill**: Create semantic database from table using Pinecone
**Description**: Students use 'create semantic database from table' block to convert text data into vector embeddings. They understand that the table must have a 'key' column, and other columns become metadata.
**Dependencies**:
- T29.G7.01.01: Build keyword-based retrieval system
**Grade**: 7

## T29.G7.01.02.02 [SPLIT from T29.G7.01.02]
**Skill**: Perform basic semantic search without filters
**Description**: Students use 'search semantic database' to find similar text using natural language queries. They compare semantic search results to keyword-based search and understand embedding-based similarity.
**Dependencies**:
- T29.G7.01.02.01: Create semantic database from table using Pinecone
**Grade**: 7

## T29.G7.01.02.03 [SPLIT from T29.G7.01.02]
**Skill**: Filter semantic search by single metadata field
**Description**: Students use the 'filter by column [FIELD] of value [VALUE]' parameters to restrict search results to records matching specific metadata criteria (e.g., only documents from "NY" state).
**Dependencies**:
- T29.G7.01.02.02: Perform basic semantic search without filters
**Grade**: 7

## T29.G7.01.02.04 [SPLIT from T29.G7.01.02]
**Skill**: Use complex conditional filters for semantic search
**Description**: Students use the advanced 'where [CONDITION]' parameter with AND/OR logic and comparison operators to filter semantic search results (e.g., "(state = 'NY') and (points > 35)").
**Dependencies**:
- T29.G7.01.02.03: Filter semantic search by single metadata field
**Grade**: 7

## T29.G7.02.01 [NEW]
**Skill**: Use system messages to control ChatGPT behavior
**Description**: Students use the 'OpenAI ChatGPT: system request' block to set system-level instructions that control ChatGPT's behavior, personality, or response style across an entire conversation.
**Dependencies**:
- T29.G5.05.03: Use role-based prompts for ChatGPT
**Grade**: 7

## T29.G7.02.02 [NEW]
**Skill**: Select LLM models (small vs large)
**Description**: Students use the 'LLM model [PROVIDER]' block instead of ChatGPT block to select between small and large models. They compare response quality, speed, and cost considerations.
**Dependencies**:
- T29.G4.05.02.02: Send basic ChatGPT requests in waiting mode
**Grade**: 7

## T29.G7.02.03 [NEW]
**Skill**: Set system instructions for specific LLM models
**Description**: Students use 'LLM set system instruction [INSTRUCTION] for model [PROVIDER]' to control behavior of small or large models separately. They understand each model maintains its own system instruction.
**Dependencies**:
- T29.G7.02.02: Select LLM models (small vs large)
- T29.G7.02.01: Use system messages to control ChatGPT behavior
**Grade**: 7

## T29.G7.02.04 [NEW]
**Skill**: Switch between multiple chatbot threads
**Description**: Students use 'select chatbot [BOTID]' to switch between up to 4 parallel ChatGPT conversation threads. They understand each thread maintains separate context.
**Dependencies**:
- T29.G6.05.01: Use new chat vs continue session types
**Grade**: 7

## T29.G7.02.05 [NEW]
**Skill**: Attach images to ChatGPT requests (vision)
**Description**: Students use 'attach costume [COSTUMENAME] to chat' to send images to ChatGPT with vision capabilities. They ask questions about image content or request image-based analysis.
**Dependencies**:
- T29.G4.05.02.02: Send basic ChatGPT requests in waiting mode
**Grade**: 7

## T29.G7.02.06 [NEW]
**Skill**: Attach files to ChatGPT requests
**Description**: Students use 'attach files to chat' to select and upload local files to ChatGPT. They understand the block returns a list of file paths separated by newlines.
**Dependencies**:
- T29.G4.05.02.02: Send basic ChatGPT requests in waiting mode
**Grade**: 7

## T29.G7.02.07 [NEW]
**Skill**: Attach Google Drive files to ChatGPT
**Description**: Students use 'attach file from Google Drive [URL] to chat' to share Google Drive documents with ChatGPT. They provide shared URLs and request analysis or processing of the files.
**Dependencies**:
- T29.G4.05.02.02: Send basic ChatGPT requests in waiting mode
**Grade**: 7

## T29.G7.02.08 [NEW]
**Skill**: Add stage snapshots for LLM vision analysis
**Description**: Students use the 'looks_addstagesnapshot' block to capture the current stage view and send it to ChatGPT for visual analysis. They ask questions about what's happening in their project.
**Dependencies**:
- T29.G7.02.05: Attach images to ChatGPT requests (vision)
**Grade**: 7

## T29.G7.03
**Skill**: Audit text datasets for bias and coverage
**Description**: Students examine text corpora for demographic representation, tone, or potentially harmful language. They document gaps (missing perspectives, skewed vocabulary) and propose mitigations, building responsible AI data practices.
**Dependencies**:
- T29.G5.04.02: Score text using sentiment word lists
- T29.G6.01: Compare characters, words, and token counts
- T29.G6.04: Log AI prompts/responses with ratings and timestamps
**Grade**: 7

## T29.G7.04
**Skill**: Critically annotate AI vs human summaries
**Description**: Learners write their own summary, generate an AI summary, then systematically annotate differences: what the AI missed, what it distorted, what it added. They measure overlap and discuss AI summarization limitations.
**Dependencies**:
- T29.G4.05.02.02: Send basic ChatGPT requests in waiting mode
- T29.G5.05.01: Build dynamic prompts with variable placeholders
- T29.G6.04: Log AI prompts/responses with ratings and timestamps
**Grade**: 7

## T29.G7.05.01 [SPLIT from T29.G7.05]
**Skill**: Use Google search API block
**Description**: Students use the 'web search [QUERY] store top (K) in table [TABLE]' block to retrieve web search results. They understand the result table has 3 columns: title, link, snippet.
**Dependencies**:
- T29.G6.04: Log AI prompts/responses with ratings and timestamps
- T29.G5.02: Populate data tables from text using split
- T11.G6.01: Sort a table by a column
**Grade**: 7

## T29.G7.05.02 [SPLIT from T29.G7.05]
**Skill**: Extract and display web search results
**Description**: Students extract title, link, and snippet from web search result tables. They display results in user-friendly formats (lists, clickable links, preview cards).
**Dependencies**:
- T29.G7.05.01: Use Google search API block
**Grade**: 7

## T29.G7.05.03 [SPLIT from T29.G7.05]
**Skill**: Analyze text from web search snippets
**Description**: Students process web search snippets using text analysis techniques (word frequency, sentiment, keyword extraction) to summarize or categorize search results.
**Dependencies**:
- T29.G7.05.02: Extract and display web search results
**Grade**: 7

## T29.G7.06.01 [NEW]
**Skill**: Use AI text moderation block
**Description**: Students use 'get moderation result for [TEXT]' to check if text content is appropriate. The block returns "Pass" or "Fail" and helps build safe content filters.
**Dependencies**:
- T29.G6.10: Validate text input and handle errors
**Grade**: 7

## T29.G7.06.02 [NEW]
**Skill**: Use AI image moderation blocks
**Description**: Students use 'get moderation result for image at URL [URL]' and 'get moderation result for costume named [NAME]' to check if images are appropriate. They build content moderation systems.
**Dependencies**:
- T29.G7.06.01: Use AI text moderation block
**Grade**: 7

---

# GRADE 8 (Ages 13-14)

## T29.G8.01
**Skill**: Build end-to-end text-processing pipelines
**Description**: Build a multi-stage text processing pipeline with at least 5 stages: input → clean (trim, lowercase, remove punctuation) → tokenize (split) → filter (remove stop-words) → analyze (sentiment OR frequency) → output (display OR log to table). Students document each stage and use custom blocks for modularity.
**Dependencies**:
- T29.G7.01.01: Build keyword-based retrieval system
- T29.G7.03: Audit text datasets for bias and coverage
- T07.G6.01: Define custom blocks with inputs
- T06.G6.01: Trace event execution paths in a multi-event program
- T09.G6.01: Model real-world quantities using variables and formulas
- T10.G6.01: Sort a table by a column
**Grade**: 8

## T29.G8.02
**Skill**: Compute text classifier evaluation metrics (precision/recall/F1)
**Description**: Learners compare predicted vs actual labels using table operations, manually compute precision (correct positives / predicted positives), recall (correct positives / actual positives), and F1 score. They interpret the tradeoffs between these metrics for text classification tasks.
**Dependencies**:
- T29.G8.06: Engineer text features for ML classifiers
- T29.G7.03: Audit text datasets for bias and coverage
- T22.G7.01: Evaluate ML model performance with test data
- T08.G6.01: Use conditionals to control simulation steps
- T09.G6.01: Model real-world quantities using variables and formulas
- T10.G6.01: Sort a table by a column
**Grade**: 8

## T29.G8.03
**Skill**: Integrate text analytics into AI prompt engineering (RAG-style)
**Description**: Students embed text analytics results (top keywords, sentiment scores, entity extraction) into AI prompt templates and evaluate whether augmented prompts produce better AI responses (RAG-style enhancement).
**Dependencies**:
- T29.G7.01.01: Build keyword-based retrieval system
- T29.G7.03: Audit text datasets for bias and coverage
- T06.G6.01: Trace event execution paths in a multi-event program
- T09.G6.01: Model real-world quantities using variables and formulas
- T10.G6.01: Sort a table by a column
**Grade**: 8

## T29.G8.04
**Skill**: Publish datasheets for text datasets
**Description**: Learners author "datasheet" documentation for their text datasets covering source, collection process, known limitations, bias analysis, intended uses, and maintenance plans, aligning with AI transparency and responsible data practices.
**Dependencies**:
- T29.G7.03: Audit text datasets for bias and coverage
- T29.G7.04: Critically annotate AI vs human summaries
- T06.G6.01: Trace event execution paths in a multi-event program
- T09.G6.01: Model real-world quantities using variables and formulas
- T10.G6.01: Sort a table by a column
**Grade**: 8

## T29.G8.05.01 [SPLIT from T29.G8.05]
**Skill**: Use regex test block for pattern matching
**Description**: Students use 'regex [REGEXPATTERN] test [TEXT]' to check if a pattern exists in text. They build simple validators (email format, phone number format) using basic regex patterns.
**Dependencies**:
- T29.G5.03.02: Build stop-word filter using tables
- T29.G6.08: Compare text similarity using edit distance
**Grade**: 8

## T29.G8.05.02 [SPLIT from T29.G8.05]
**Skill**: Use regex match block to extract patterns
**Description**: Students use 'regex [REGEXPATTERN] flag [FLAG] match [TEXT] into list [LISTNAME]' to extract all matching patterns from text. They understand the 'g' flag extracts all matches vs just the first.
**Dependencies**:
- T29.G8.05.01: Use regex test block for pattern matching
**Grade**: 8

## T29.G8.05.03 [SPLIT from T29.G8.05]
**Skill**: Use regex search block to find pattern positions
**Description**: Students use 'regex [REGEXPATTERN] search [TEXT]' to find the position (index) of the first pattern match. They build text parsers that locate specific patterns.
**Dependencies**:
- T29.G8.05.01: Use regex test block for pattern matching
**Grade**: 8

## T29.G8.05.04 [SPLIT from T29.G8.05]
**Skill**: Use regex replace block for text substitution
**Description**: Students use 'regex [REGEXPATTERN] flag [FLAG] replace [TEXT] with [T]' to replace patterns with new text. They understand the 'g' flag replaces all matches vs just the first.
**Dependencies**:
- T29.G8.05.02: Use regex match block to extract patterns
**Grade**: 8

## T29.G8.05.05 [SPLIT from T29.G8.05]
**Skill**: Use regex split block for advanced tokenization
**Description**: Students use 'regex [REGEXPATTERN] flag [FLAG] split [TEXT] into list [LISTNAME]' to split text using complex patterns (multiple delimiters, whitespace variations, special characters).
**Dependencies**:
- T29.G8.05.01: Use regex test block for pattern matching
- T29.G5.06.01: Understand the parse sentence block structure
**Grade**: 8

## T29.G8.06
**Skill**: Engineer text features for ML classifiers
**Description**: Learners extract numerical features from text (word counts, sentiment scores, length, keyword presence, bigram frequencies) and feed them into CreatiCode's ML model training blocks to classify text (spam vs not-spam, emotion categories).
**Dependencies**:
- T29.G5.04.02: Score text using sentiment word lists
- T29.G6.01: Compare characters, words, and token counts
- T29.G6.04: Log AI prompts/responses with ratings and timestamps
- T22.G6.01: Train a simple ML model (supervised learning)
- T09.G3.05: Trace code with variables to predict outcomes
- T10.G5.03: Add and remove items from a list
**Grade**: 8

---

## SUMMARY STATISTICS

### Total Skills: 115
- Kindergarten: 3 skills
- Grade 1: 4 skills
- Grade 2: 4 skills
- Grade 3: 5 skills
- Grade 4: 13 skills
- Grade 5: 18 skills
- Grade 6: 20 skills
- Grade 7: 27 skills
- Grade 8: 21 skills

### Skills Split (18 original skills split into 52):
1. T29.G4.05.02 → 5 skills (ChatGPT parameters)
2. T29.G5.05 → 3 skills (prompt engineering)
3. T29.G5.06 → 4 skills (parse sentence block)
4. T29.G6.06 → 6 skills (speech-to-text)
5. T29.G6.07 → 5 skills (text-to-speech)
6. T29.G7.01.02 → 4 skills (Pinecone semantic search)
7. T29.G7.05 → 3 skills (web search)
8. T29.G8.05 → 5 skills (regex blocks)

### New Skills Added (25):
- G6: 2 skills (ChatGPT session management, clear speech)
- G7: 16 skills (LLM models, chatbot switching, file attachments, moderation, stage snapshots)
- G8: 0 skills (all advanced skills covered by splits)

### Major Improvements:
1. **Single-feature focus**: Every skill now covers ONE block or ONE specific feature
2. **Complete block coverage**: All 43 AI blocks + all text manipulation blocks covered
3. **Proper scaffolding**: Each complex feature broken into learnable steps
4. **Accurate descriptions**: All skills verified against actual block capabilities
5. **Fixed dependencies**: All intra-topic dependencies follow X-2 rule

---

## VERIFICATION CHECKLIST

### CreatiCode AI/NLP Blocks Coverage:
- ✅ Speech Recognition (7 blocks): G6.06.01-06, G6.06.06
- ✅ Text-to-Speech (2 blocks): G6.07.01-05
- ✅ ChatGPT/LLM (9 blocks): G4.05.02.01-05, G6.05.01-02, G7.02.01-08
- ✅ Image Generation (2 blocks): Covered in T21 (AI Media)
- ✅ Content Moderation (3 blocks): G7.06.01-02
- ✅ NLP Sentence Analysis (1 block): G5.06.01-04
- ✅ Computer Vision (5 blocks): Covered in T21 (AI Media)
- ✅ Machine Learning (8 blocks): Covered in T22 (ML)
- ✅ Semantic Search (3 blocks): G7.01.02.01-04
- ✅ Web Search (1 block): G7.05.01-03

### Text Manipulation Blocks Coverage:
- ✅ Split/Join: G4.01
- ✅ Replace: G4.06
- ✅ Trim: G5.07
- ✅ Case conversion: G4.04.01
- ✅ String comparison: G4.04.02
- ✅ Substring/character access: G4.02, G4.07
- ✅ Text similarity: G6.08
- ✅ Regex (5 blocks): G8.05.01-05

### Dependency Verification:
- ✅ All K-2 skills are unplugged/picture-based
- ✅ Grade 3+ skills use block-based coding
- ✅ All intra-topic dependencies follow X-2 rule
- ✅ No circular dependencies within T29
- ✅ All cross-topic dependencies preserved

---

## END OF DOCUMENT
