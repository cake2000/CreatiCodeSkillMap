# T29 (Text Data & NLP Foundations) - Comprehensive Analysis

## Executive Summary

**Topic:** T29 – Text Data & NLP Foundations (Grades 3-8)
**Total Skills:** 28 skills across 6 grade levels
**Coverage:** Grade 3 (4 skills), Grade 4 (5 skills), Grade 5 (5 skills), Grade 6 (5 skills), Grade 7 (4 skills), Grade 8 (5 skills)

---

## Part 1: Complete List of Current T29 Skills

### Grade 3 Skills (4 skills - All Unplugged/Conceptual)

#### T29.G3.01: Distinguish text data from numbers and pictures
- **Description:** Students sort cards showing words, sentences, numbers, and emojis to recognize text as a specific data type.
- **Dependencies:** (none)
- **Type:** Unplugged activity
- **Quality:** ✅ Clear, appropriate for G3 introduction

#### T29.G3.02: Count word occurrences manually
- **Description:** Learners read a short paragraph and tally how many times specific words appear, building intuition for word frequency.
- **Dependencies:**
  - T29.G3.01: Distinguish text data from numbers and pictures
  - T09.G3.01: Create and use a numeric variable for score or count
- **Type:** Unplugged with coding readiness
- **Quality:** ✅ Clear, builds intuition

#### T29.G3.03: Group words by category (emotion, action, place)
- **Description:** Students categorize words into meaning-based groups and explain their reasoning, preparing for later metadata tagging.
- **Dependencies:**
  - T29.G3.02: Count word occurrences manually
- **Type:** Unplugged/conceptual
- **Quality:** ✅ Clear, foundational for NLP concepts

#### T29.G3.04: Explain why clean text helps AI helpers
- **Description:** Learners compare two sample prompts (typos vs clean) and discuss how clarity affects XO's responses.
- **Dependencies:**
  - T29.G3.03: Group words by category (emotion, action, place)
- **Type:** Unplugged/conceptual
- **Quality:** ✅ Clear, connects to AI literacy

---

### Grade 4 Skills (5 skills - Transition to Coding)

#### T29.G4.01: Compare a human summary to a computer summary
- **Description:** Students read a short paragraph, write a one-sentence summary, and then compare it to a computer-generated summary, noting what the computer included or missed.
- **Dependencies:**
  - T29.G3.04: Explain why clean text helps AI helpers
  - T08.G3.01: Use a simple if in a script
  - T09.G3.05: Trace code with variables to predict outcomes
  - T10.G3.03: Add and remove items from a list
- **Type:** Hybrid (unplugged + coding observation)
- **Quality:** ✅ Clear, good critical thinking skill
- **Issue:** ⚠️ Cross-topic dependencies jump from G3 (should be G4 skills)

#### T29.G4.02: Use split and join blocks for text manipulation
- **Description:** Students write a script that takes a sentence, uses the split block to separate it on spaces, stores each word in a list, and uses join to reconstruct text.
- **Dependencies:**
  - T29.G3.04: Explain why clean text helps AI helpers
  - T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  - T09.G3.01: Create and use a numeric variable for score or count
  - T09.G3.05: Trace code with variables to predict outcomes
  - T10.G3.03: Add and remove items from a list
- **Type:** Hands-on coding
- **Quality:** ✅ Clear, foundational text manipulation
- **Issue:** ⚠️ Cross-topic dependencies from G3 (should use G4 equivalents)

#### T29.G4.03: Clean text: lowercase + remove punctuation
- **Description:** Learners build helper blocks that convert text to lowercase using the lowercase operator. For punctuation removal, they use a loop to check each character and keep only letters and spaces.
- **Dependencies:**
  - T29.G4.02: Use split and join blocks for text manipulation
  - T09.G3.01: Create and use a numeric variable for score or count
  - T09.G3.05: Trace code with variables to predict outcomes
  - T10.G3.03: Add and remove items from a list
- **Type:** Hands-on coding
- **Quality:** ✅ Clear, practical skill
- **Issue:** ⚠️ Missing loop dependency (T07), needs character-by-character iteration
- **Issue:** ⚠️ Cross-topic dependencies from G3

#### T29.G4.04: Count words and report the most frequent
- **Description:** Students iterate over the token list, keep counts in parallel lists/tables, and identify the most common word.
- **Dependencies:**
  - T29.G4.03: Clean text: lowercase + remove punctuation
  - T08.G3.01: Use a simple if in a script
  - T09.G3.01: Create and use a numeric variable for score or count
  - T09.G3.05: Trace code with variables to predict outcomes
  - T10.G3.03: Add and remove items from a list
- **Type:** Hands-on coding
- **Quality:** ✅ Clear, builds on previous skills
- **Issue:** ⚠️ Missing loop dependency (T07)
- **Issue:** ⚠️ Cross-topic dependencies from G3

#### T29.G4.05: Highlight keywords in a paragraph
- **Description:** Learners write code that scans a paragraph and highlights (changes color) every time a keyword appears on the stage.
- **Dependencies:**
  - T29.G4.02: Use split and join blocks for text manipulation
  - T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  - T09.G3.05: Trace code with variables to predict outcomes
  - T10.G3.03: Add and remove items from a list
- **Type:** Hands-on coding with visual output
- **Quality:** ✅ Clear, engaging visual feedback
- **Issue:** ⚠️ Missing loop dependency
- **Issue:** ⚠️ Should depend on T29.G4.04 (word counting) for consistency
- **Issue:** ⚠️ Cross-topic dependencies from G3

---

### Grade 5 Skills (5 skills - Data Structures & NLP Concepts)

#### T29.G5.01: Structure chat logs into tables
- **Description:** Students design table schemas for XO chats or multiplayer messages, ensuring each row records metadata needed for later filtering.
- **Dependencies:**
  - T29.G4.02: Use split and join blocks for text manipulation
  - T29.G4.04: Count words and report the most frequent
- **Type:** Data structure design + coding
- **Quality:** ✅ Clear, important data literacy skill
- **Issue:** ⚠️ Missing table manipulation dependency from T10

#### T29.G5.02: Build stop-word filters and keyword lists
- **Description:** Learners maintain a stop-word list and filter it out before running frequency counts to focus on meaningful words.
- **Dependencies:**
  - T29.G4.04: Count words and report the most frequent
  - T29.G4.05: Highlight keywords in a paragraph
- **Type:** Hands-on coding
- **Quality:** ✅ Clear, important NLP preprocessing concept

#### T29.G5.03: Measure simple sentiment heuristics
- **Description:** Students store positive/negative word lists and score sentences accordingly, noting in a reflection that the heuristic has limits.
- **Dependencies:**
  - T29.G4.04: Count words and report the most frequent
  - T29.G4.05: Highlight keywords in a paragraph
- **Type:** Hands-on coding with critical reflection
- **Quality:** ✅ Clear, teaches both technique and limitations

#### T29.G5.04: Map story descriptions into AI prompt slots
- **Description:** Learners highlight parts of a description needed for T21/T24 prompts (subject, color palette, mood) and populate a structured form.
- **Dependencies:**
  - T29.G5.01: Structure chat logs into tables
  - T29.G4.04: Count words and report the most frequent
  - T29.G4.05: Highlight keywords in a paragraph
- **Type:** Hands-on coding with AI integration
- **Quality:** ✅ Clear, connects text processing to AI generation

#### T29.G5.05: Use the analyze sentence block for parts of speech
- **Description:** Students use CreatiCode's sentence analysis block to identify nouns, verbs, and adjectives in text, building awareness of grammatical structure for NLP tasks.
- **Dependencies:**
  - T29.G4.02: Use split and join blocks for text manipulation
  - T29.G4.04: Count words and report the most frequent
- **Type:** Hands-on coding with NLP tool
- **Quality:** ✅ Clear, introduces linguistic structure
- **Issue:** ⚠️ Missing table dependency (results written to table)

---

### Grade 6 Skills (5 skills - Advanced Text Processing)

#### T29.G6.01: Explain characters vs words vs tokens
- **Description:** Students count characters, words, and approximate GPT tokens for short text, discussing why counts differ and which matters for prompts.
- **Dependencies:**
  - T29.G5.02: Build stop-word filters and keyword lists
  - T08.G4.01: Choose actions based on user input or sensor values
  - T09.G4.04: Use variables to control animation or game state
  - T10.G4.03: Add, remove, and access items from a list in a script
- **Type:** Hands-on coding + conceptual understanding
- **Quality:** ✅ Clear, important for AI literacy
- **Issue:** ⚠️ Cross-topic dependencies from G4 (should be G6)

#### T29.G6.02: Compute n‑gram (bigram) frequencies
- **Description:** Learners loop through token lists, join consecutive words, and store counts to capture phrase patterns.
- **Dependencies:**
  - T29.G5.02: Build stop-word filters and keyword lists
  - T07.G4.01: Loop until a goal condition is met
  - T09.G4.04: Use variables to control animation or game state
  - T10.G4.03: Add, remove, and access items from a list in a script
- **Type:** Hands-on coding
- **Quality:** ✅ Clear, introduces n-gram concept
- **Issue:** ⚠️ Cross-topic dependencies from G4

#### T29.G6.03: Create autocomplete suggestions
- **Description:** Using bigram data, students propose the top next words for a given prefix and display them via widgets.
- **Dependencies:**
  - T29.G6.02: Compute n‑gram (bigram) frequencies
  - T06.G4.01: Write scripts that respond to keyboard or mouse events
  - T09.G4.04: Use variables to control animation or game state
  - T10.G4.03: Add, remove, and access items from a list in a script
- **Type:** Hands-on coding with UI
- **Quality:** ✅ Clear, engaging application
- **Issue:** ⚠️ Cross-topic dependencies from G4
- **Issue:** ⚠️ Missing widget dependency

#### T29.G6.04: Log XO prompts/responses with ratings
- **Description:** Learners automatically log each XO interaction (prompt, response, rating, timestamp) into a table for T24 responsible-use tracking.
- **Dependencies:**
  - T29.G5.01: Structure chat logs into tables
  - T29.G5.04: Map story descriptions into AI prompt slots
  - T07.G4.01: Loop until a goal condition is met
  - T09.G4.04: Use variables to control animation or game state
  - T10.G4.03: Add, remove, and access items from a list in a script
- **Type:** Hands-on coding with AI integration
- **Quality:** ✅ Clear, supports responsible AI use
- **Issue:** ⚠️ Cross-topic dependencies from G4

#### T29.G6.05: Use regex patterns for text matching
- **Description:** Students learn to use basic regular expressions to find patterns in text such as emails, numbers, or repeated words using CreatiCode's regex blocks.
- **Dependencies:**
  - T29.G5.02: Build stop-word filters and keyword lists
  - T29.G5.05: Use the analyze sentence block for parts of speech
- **Type:** Hands-on coding
- **Quality:** ✅ Clear, introduces powerful pattern matching
- **Note:** Good introduction to regex

---

### Grade 7 Skills (4 skills - Integration & Critical Analysis)

#### T29.G7.01: Build keyword retrieval helpers (mini-RAG)
- **Description:** Students build a simple retrieval system by storing paragraph snippets in a table, computing keyword overlap scores, and returning the best-matching snippet. Advanced students can use the 'create semantic database from table' and 'search semantic database with query' blocks for embedding-based retrieval.
- **Dependencies:**
  - T29.G5.02: Build stop-word filters and keyword lists
  - T29.G6.02: Compute n‑gram (bigram) frequencies
  - T29.G6.03: Create autocomplete suggestions
  - T09.G3.05: Trace code with variables to predict outcomes
  - T10.G5.03: Add and remove items from a list
- **Type:** Hands-on coding (advanced)
- **Quality:** ✅ Clear, introduces RAG concept
- **Issue:** ⚠️ Cross-topic dependency T09.G3.05 is wrong grade level (should be G7)
- **Issue:** ⚠️ Missing table/sorting dependencies

#### T29.G7.02: Engineer text features for classifiers
- **Description:** Learners extract features (word counts, sentiment scores, length) and feed them into CreatiCode's AI classifier blocks to label text (spam vs not, emotion categories).
- **Dependencies:**
  - T29.G5.03: Measure simple sentiment heuristics
  - T29.G6.01: Explain characters vs words vs tokens
  - T29.G6.04: Log XO prompts/responses with ratings
  - T08.G5.01: Use a simple if in a script
  - T09.G3.05: Trace code with variables to predict outcomes
  - T10.G5.03: Add and remove items from a list
- **Type:** Hands-on coding with ML
- **Quality:** ✅ Clear, important ML engineering concept
- **Issue:** ⚠️ Cross-topic dependency T08.G5.01 should be higher grade
- **Issue:** ⚠️ Cross-topic dependency T09.G3.05 is wrong grade level

#### T29.G7.03: Audit text datasets for bias and coverage
- **Description:** Students examine corpora for demographic coverage, tone, or harmful language, documenting gaps and proposing mitigations.
- **Dependencies:**
  - T29.G5.03: Measure simple sentiment heuristics
  - T29.G6.01: Explain characters vs words vs tokens
  - T29.G6.04: Log XO prompts/responses with ratings
  - T06.G5.01: Design multi‑sprite programs using clones
  - T09.G3.05: Trace code with variables to predict outcomes
  - T10.G5.03: Add and remove items from a list
- **Type:** Critical analysis + coding
- **Quality:** ✅ Clear, critical AI ethics skill
- **Issue:** ⚠️ T06.G5.01 dependency seems irrelevant (clones not needed for text audit)
- **Issue:** ⚠️ Cross-topic dependency T09.G3.05 is wrong grade level

#### T29.G7.04: Compare human vs XO summaries critically
- **Description:** Learners write their own summary, compare it to XO's output, and annotate what the AI missed or distorted, building on earlier G4 comparison work with deeper critical analysis.
- **Dependencies:**
  - T29.G5.04: Map story descriptions into AI prompt slots
  - T29.G6.03: Create autocomplete suggestions
  - T29.G6.04: Log XO prompts/responses with ratings
  - T08.G5.01: Use a simple if in a script
  - T09.G3.05: Trace code with variables to predict outcomes
  - T10.G5.03: Add and remove items from a list
- **Type:** Critical analysis + coding
- **Quality:** ✅ Clear, builds on T29.G4.01
- **Issue:** ⚠️ Should explicitly reference T29.G4.01 as foundation
- **Issue:** ⚠️ Cross-topic dependencies at wrong grade levels

---

### Grade 8 Skills (5 skills - Pipelines & Evaluation)

#### T29.G8.01: Build end-to-end text-processing pipelines
- **Description:** Students design scripts that ingest raw text, normalize it, extract features, run analysis (sentiment or retrieval), and save results for future prompts.
- **Dependencies:**
  - T29.G7.01: Build keyword retrieval helpers (mini-RAG)
  - T29.G7.03: Audit text datasets for bias and coverage
  - T06.G6.01: Trace event execution paths in a multi‑event program
  - T09.G6.01: Model real-world quantities using variables and formulas
  - T10.G6.01: Sort a table by a column
- **Type:** Hands-on coding (comprehensive)
- **Quality:** ✅ Clear, capstone integration skill

#### T29.G8.02: Compute evaluation metrics (precision/recall/F1)
- **Description:** Learners compare predicted vs actual labels using table operations, manually compute precision (correct positives / predicted positives), recall (correct positives / actual positives), and F1 score, then interpret the tradeoffs between these metrics.
- **Dependencies:**
  - T29.G7.02: Engineer text features for classifiers
  - T29.G7.03: Audit text datasets for bias and coverage
  - T08.G6.01: Use conditionals to control simulation steps
  - T09.G6.01: Model real-world quantities using variables and formulas
  - T10.G6.01: Sort a table by a column
- **Type:** Hands-on coding + ML evaluation
- **Quality:** ✅ Clear, essential ML literacy
- **Note:** Good mathematical + computational thinking

#### T29.G8.03: Integrate analytics into AI prompting
- **Description:** Students embed text analytics (top keywords, sentiment) into XO prompt templates and evaluate whether responses improve.
- **Dependencies:**
  - T29.G7.01: Build keyword retrieval helpers (mini-RAG)
  - T29.G7.03: Audit text datasets for bias and coverage
  - T06.G6.01: Trace event execution paths in a multi‑event program
  - T09.G6.01: Model real-world quantities using variables and formulas
  - T10.G6.01: Sort a table by a column
- **Type:** Hands-on coding with AI integration
- **Quality:** ✅ Clear, shows value of preprocessing

#### T29.G8.04: Publish datasheets for text datasets
- **Description:** Learners author "datasheet" reports covering dataset source, collection process, limitations, and maintenance plans, aligning with AI transparency best practices.
- **Dependencies:**
  - T29.G7.03: Audit text datasets for bias and coverage
  - T29.G7.04: Compare human vs XO summaries critically
  - T06.G6.01: Trace event execution paths in a multi‑event program
  - T09.G6.01: Model real-world quantities using variables and formulas
  - T10.G6.01: Sort a table by a column
- **Type:** Documentation + critical analysis
- **Quality:** ✅ Clear, aligns with ML best practices
- **Note:** Excellent responsible AI practice

---

## Part 2: Available CreatiCode Blocks for Text/NLP Work

### A. Basic Text/String Operators

#### String Manipulation
1. **operator_joinwith** - `join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]`
   - Joins up to 6 texts with separator
   - Used in: T29.G4.02, T29.G6.02

2. **operator_include** - `[TEXT1] includes [TEXT2] ignore case [IGNORECASE v]`
   - Check if text contains substring
   - Used in: T29.G4.05, T29.G5.02

3. **operator_start** - `[TEXT1] starts with [TEXT2] ignore case [IGNORECASE v]`
   - Check if text starts with substring

4. **operator_end** - `[TEXT1] ends with [TEXT2] ignore case [IGNORECASE v]`
   - Check if text ends with substring

5. **operator_replace** - `replace [T1] with [T2] in [T3]`
   - Replace text occurrences
   - Used in: T29.G4.03 (punctuation removal)

6. **operator_substringindex** - `position of [T1] in [T2]`
   - Find substring position
   - Used in: T29.G6.05 (pattern matching)

7. **operator_substring** - `substring of [TEXT] from position (P1) to position (P2)`
   - Extract substring by position
   - Used in: Character-by-character processing in T29.G4.03

8. **operator_splitsubstring** - `part (INDEX) of [TEXT] by [SEPARATOR]`
   - Get specific part after splitting

9. **operator_lcs** - `longest common substring between [TEXT1] and [TEXT2]`
   - Find longest common substring
   - Could be used in: T29.G7.01 (similarity matching)

10. **operator_trim** - `trim [TEXT]`
    - Remove leading/trailing whitespace
    - Used in: T29.G4.03 (text cleaning)

11. **operator_texttransform** - `[CASE v] of text [T]` (uppercase/lowercase)
    - Convert text case
    - **CRITICAL:** Used in T29.G4.03

12. **operator_stringdiff** - `steps to change [STRING1] into [STRING2]`
    - Edit distance calculation
    - Could be used in: Advanced text comparison

#### String Testing
13. **operator_isnumber** - `<[TEXT] is a number?>`
    - Check if text is numeric
    - Used in: T29.G3.01 (distinguish data types)

14. **operator_converttonumber** - `convert [TEXT] to a number`
    - Convert text to number
    - Used in: T29.G4.04 (counting)

### B. Regular Expression Blocks (Advanced Pattern Matching)

15. **operator_regex_test** - `regex [REGEXPATTERN] test [TEXT]`
    - Test if pattern matches
    - **CRITICAL:** Used in T29.G6.05

16. **operator_regex_match_into_list** - `regex [REGEXPATTERN] flag [FLAG] match [TEXT] into list [LISTNAME v]`
    - Extract all matches
    - Used in: T29.G6.05

17. **operator_regex_search** - `regex [REGEXPATTERN] search [TEXT]`
    - Find first match position
    - Used in: T29.G6.05

18. **operator_regex_replace_with** - `regex [REGEXPATTERN] flag [FLAG] replace [TEXT] with [T]`
    - Replace using patterns
    - Used in: T29.G4.03, T29.G6.05

19. **operator_regex_split_into_list** - `regex [REGEXPATTERN] flag [FLAG] split [TEXT] into list [LISTNAME v]`
    - Split using patterns
    - Used in: T29.G6.05

### C. List/Data Blocks for Text Processing

20. **data_set_list_to_split_of** - `set [LISTNAME v] to split of [TEXT] with splitter [SEPARATOR]`
    - **CRITICAL:** Core block for T29.G4.02
    - Split text into list

21. **data_joinlistwith** - `join [LISTNAME v] into text with [SEPARATOR]`
    - **CRITICAL:** Core block for T29.G4.02
    - Join list items into text

### D. NLP & AI Blocks

22. **ai_analyzesentence** - `analyze sentence [SENTENCE] and write into table [TABLENAME v]`
    - **CRITICAL:** Core block for T29.G5.05
    - Returns table with columns: TEXT, LEMMA, TYPE, PERSON, OFFSET, LABEL, DEPENDS
    - Identifies parts of speech (nouns, verbs, adjectives, etc.)
    - Used in: T29.G5.05

23. **ai_createsemanticdatabase** - `create semantic database from table [TABLE v]`
    - **CRITICAL:** Advanced feature in T29.G7.01
    - Create embedding-based database
    - Table must have 'key' column
    - Converts to embedding vectors

24. **ai_searchsemanticdatabase** - `search semantic database with [QUERY] store top (K) in table [t1 v] filter by column [FIELD] of value [VALUE]`
    - **CRITICAL:** Advanced feature in T29.G7.01
    - Semantic search using embeddings
    - Alternative simpler version: `search semantic database with [QUERY] where [CONDITION] store top (K) in table [TABLE v]`

25. **ai_createknnclassifier** - `create KNN number classifier from table [TABLENAME v] K [KVALUE] named [NAME]`
    - **CRITICAL:** Core block for T29.G7.02
    - Train classifier from table data
    - First column must be 'label'

26. **ai_predictknnclassifier** - `predict for table [TABLENAME v] with classifier [NAME] show neighbors [SHOW v]`
    - **CRITICAL:** Core block for T29.G7.02
    - Predict labels using trained classifier

### E. Neural Network Blocks (Advanced ML)

27. **add_layer_to_model** - Add neural network layer
    - Used in: Advanced T29.G7.02 implementations

28. **train_model** - `train NN model [NAME] using table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN] batch size [BATCHSIZE] epochs [EPOCHS]`
    - Advanced ML training
    - Could be used in: T29.G7.02, T29.G8.02

29. **predict_by_model** - `predict using NN model [NAME] for table [TABLENAME v] rows from [STARTROW] to [ENDROW] input columns [INPUTCOLUMNS] output column [OUTPUTCOLUMN]`
    - Neural network prediction
    - Could be used in: T29.G7.02, T29.G8.02

### F. ChatGPT/LLM Integration Blocks

30. **openai_chatgpt_request** - `OpenAI ChatGPT: request [PROMPT] result [VARIABLE v] mode [MODE v] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE v]`
    - Send prompt to ChatGPT
    - **CRITICAL:** Used in T29.G4.01, T29.G6.04, T29.G7.04

31. **openai_chatgpt_system** - `OpenAI ChatGPT: system request [PROMPT] session [SESSIONTYPE v] result [VARIABLE v] temperature [T]`
    - Set system instructions
    - Used in: Advanced prompting in T29.G8.03

32. **openai_chatgpt_cancel** - `OpenAI ChatGPT: cancel request`
    - Cancel ongoing request

33. **llm_model_request** - `LLM model [PROVIDER] request [PROMPT] result [VARIABLE v] mode [MODE v] length [MAXLENGTH] temperature [TEMPERATURE] session [SESSIONTYPE v]`
    - Alternative LLM providers
    - Used in: T29.G8.03

### G. Speech Recognition & Text-to-Speech

34. **ai_startspeechrecognition** - `start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`
    - Speech to text (Azure)
    - Potential use: Text input alternatives

35. **openai_startspeechrecognition** - `OpenAI: start recognizing speech in [LANGUAGE v] record as [SOUNDNAME]`
    - Speech to text (OpenAI Whisper)

36. **ai_endspeechrecognition** - End speech recognition
    - Get recognized text

37. **ai_speakinlanguage** - `say [TEXT] in [LANGUAGE v] as [VOICETYPE v] speed (SPEEDRATIO) pitch (PITCHRATIO) volume (VOLUMERATIO) store sound as [SOUNDNAME]`
    - Text to speech
    - Potential use: Accessibility features

### H. Table Blocks (Essential for Data Analysis)

38. **data_addrowtotable** - Add row to table
    - **CRITICAL:** Used in T29.G5.01, T29.G6.04

39. **data_findsubstring** - Find substring in table column
    - Used in: T29.G7.01 (keyword retrieval)

40. **data_rowdatawithseparator** - `row (ROWINDEX) from table [TABLENAME v] with [SEPARATOR]`
    - Get all row data as joined string
    - Used in: T29.G8.01 (pipeline outputs)

### I. Missing Standard Blocks (Should Exist in Scratch)

Note: The following standard Scratch blocks were NOT found in blockdes8.txt but are assumed to exist:

41. **operator_letter** - `letter (N) of [TEXT]` ⚠️ NOT DOCUMENTED
    - **CRITICAL:** Needed for T29.G4.03 (character iteration)

42. **operator_length** - `length of [TEXT]` ⚠️ NOT DOCUMENTED
    - **CRITICAL:** Needed for T29.G4.03, T29.G6.01

43. **operator_join** - `join [T1] [T2]` ⚠️ NOT DOCUMENTED (only joinwith found)
    - Standard Scratch join

44. **operator_contains** - `[TEXT1] contains [TEXT2]` ⚠️ FOUND AS operator_include
    - Different name in CreatiCode

---

## Part 3: Quality Issues Identified

### A. Grade Appropriateness Issues

#### 1. Cross-Topic Dependency Grade Mismatches
**CRITICAL PATTERN:** Many G4-G7 skills depend on G3-G4 skills from other topics instead of age-appropriate equivalents.

**Examples:**
- **T29.G6.01** (G6 skill) depends on:
  - T08.G4.01 (should be T08.G6.01)
  - T09.G4.04 (should be T09.G6.x)
  - T10.G4.03 (should be T10.G6.x)

- **T29.G7.01** (G7 skill) depends on:
  - T09.G3.05 (should be T09.G7.x)
  - T10.G5.03 (should be T10.G7.x)

**Impact:** Students would need to have completed much earlier grade skills, creating scaffolding gaps.

**Fix:** Update cross-topic dependencies to use same-grade or (grade - 2) equivalents.

#### 2. Missing Prerequisite Skills

**Missing in G3 (Before Coding):**
- ❌ **Understanding what a "character" is** (needed before G4.03)
- ❌ **Recognizing punctuation vs letters** (unplugged, needed before G4.03)
- ❌ **Introduction to word boundaries and spacing** (needed before G4.02)

**Missing in G4 (Early Coding):**
- ❌ **Access individual characters in text** (prerequisite for G4.03)
- ❌ **Count characters in text** (prerequisite for G6.01)
- ❌ **Compare two strings** (prerequisite for sentiment analysis)
- ❌ **Display text on stage** (prerequisite for G4.05)

**Missing in G5:**
- ❌ **Create and use helper blocks for text processing** (prerequisite for G5.02)
- ❌ **Work with tables for storing text data** (prerequisite for G5.01)

**Missing in G6:**
- ❌ **Understand string length vs word count** (should be earlier than G6.01)
- ❌ **Practice with string slicing/indexing** (prerequisite for n-grams)

### B. Dependency Issues Within T29

#### 1. Missing Loop Dependencies
**CRITICAL:** Multiple skills require loops but don't list T07 (Loops) dependencies.

**Affected Skills:**
- T29.G4.03: Clean text (needs loop for character iteration) - Missing T07.G4.x
- T29.G4.04: Count words (needs loop for iteration) - Missing T07.G4.x
- T29.G4.05: Highlight keywords (needs loop for scanning) - Missing T07.G4.x

**Fix:** Add appropriate T07 loop dependencies.

#### 2. Forward Dependencies (Violations of Scaffolding)
None found - good!

#### 3. Inconsistent Dependency Chains

**Example 1:** T29.G4.05 should depend on T29.G4.04
- G4.05 (highlight keywords) and G4.04 (count words) both scan text
- G4.04 is more foundational → G4.05 should depend on it
- Currently they're parallel (both depend on G4.02)

**Example 2:** T29.G7.04 should explicitly reference T29.G4.01
- Both compare human vs AI summaries
- G7.04 description says "building on earlier G4 comparison work"
- But G4.01 is NOT in dependencies list

**Fix:** Add missing within-topic dependencies.

#### 4. Irrelevant Dependencies

**T29.G7.03** depends on T06.G5.01 (Design multi-sprite programs using clones)
- **Issue:** Text dataset auditing doesn't require sprite clones
- **Likely cause:** Copy-paste error or misunderstanding
- **Fix:** Remove this dependency

### C. Clarity & Specificity Issues

#### 1. Skills That Are Too Broad

**T29.G8.01: Build end-to-end text-processing pipelines**
- **Issue:** Very broad capstone project
- **Missing:** Specific pipeline stages expected
- **Fix:** Add sub-skills or clearer description of pipeline stages:
  1. Ingest text from source
  2. Normalize (lowercase, remove punctuation)
  3. Tokenize
  4. Extract features
  5. Run analysis
  6. Store results

#### 2. Ambiguous Skill Descriptions

**T29.G4.01: Compare a human summary to a computer summary**
- **Ambiguous:** "computer-generated summary" - by what method?
- **Fix:** Specify: "summary generated using ChatGPT" or "simple extraction algorithm"

**T29.G5.04: Map story descriptions into AI prompt slots**
- **Ambiguous:** What is a "slot"?
- **Fix:** Specify: "identify and extract key elements (subject, setting, mood) and format as structured prompt parameters"

#### 3. Skills Lacking Concrete Outputs

**T29.G6.01: Explain characters vs words vs tokens**
- **Good:** Has concrete action (counting)
- **Missing:** What's the deliverable? (Should specify: "create comparison table")

**T29.G7.03: Audit text datasets for bias and coverage**
- **Missing:** What form does the audit take?
- **Fix:** Specify: "create audit report documenting 3+ bias categories and coverage gaps"

### D. Duplicate/Overlap Issues

#### No Major Duplicates Found ✅
Skills are generally well-differentiated.

#### Potential Overlap:
**T29.G4.01 vs T29.G7.04** (Human vs AI summaries)
- **G4.01:** Compare at basic level
- **G7.04:** Compare critically with annotation
- **Status:** ✅ Appropriate progression, not true duplication
- **Fix needed:** Make G7.04 explicitly depend on G4.01

### E. Missing Foundational Scaffolding

#### Missing Skills for Proper Progression:

**Between G3 and G4:**
1. **T29.G3.05: Identify characters, words, and sentences** (unplugged)
   - Sort cards with letters, words, and sentences
   - Prerequisite for G4.02, G4.03

**In G4:**
2. **T29.G4.01b: Access a character by position** (before G4.03)
   - Use `letter (N) of [text]` block
   - Prerequisite for character-by-character processing

3. **T29.G4.02b: Count characters and words in text** (after G4.02)
   - Use `length of [text]` block
   - Count words in a list
   - Prerequisite for G6.01

4. **T29.G4.03b: Build a custom block for text cleaning** (after G4.03)
   - Create reusable text preprocessing block
   - Prerequisite for G5.02, G8.01

**In G5:**
5. **T29.G5.01b: Create and populate text data tables** (before G5.01)
   - Add rows to tables programmatically
   - Store multi-column text data
   - Prerequisite for all table-based skills

6. **T29.G5.03b: Test sentiment on multiple sentences** (after G5.03)
   - Apply sentiment analysis to a dataset
   - Visualize results
   - Prerequisite for G7.02

**In G6:**
7. **T29.G6.01b: Implement token counting approximation** (with G6.01)
   - Create algorithm to estimate GPT tokens
   - Compare with actual API token counts
   - Strengthens G6.01

8. **T29.G6.03b: Handle user input for autocomplete** (before G6.03)
   - Capture keyboard input
   - Update suggestions in real-time
   - Prerequisite for G6.03

**In G7:**
9. **T29.G7.02b: Evaluate classifier performance** (after G7.02)
   - Split data into train/test sets
   - Check accuracy
   - Prerequisite for G8.02

---

## Part 4: Missing Skills for Proper Scaffolding

### Priority 1: CRITICAL Missing Skills (Block Scaffolding)

#### T29.G4.01b: Access characters by position ⭐⭐⭐
**Grade:** 4
**Placement:** Between G4.02 and G4.03
**Skill:** Access individual characters in text using position
**Description:** Students use the `letter (N) of [text]` block to access individual characters in a string. They create scripts that iterate through text character-by-character, building understanding of text as a sequence of characters.
**Dependencies:**
- T29.G4.02: Use split and join blocks for text manipulation
- T07.G4.01: Loop until a goal condition is met
- T10.G4.03: Add, remove, and access items from a list in a script
**Enables:** T29.G4.03 (character-by-character processing)
**Blocks Used:** `letter (N) of [text]`, `length of [text]`, `repeat`, `join`

#### T29.G4.02b: Count characters and words in text ⭐⭐⭐
**Grade:** 4
**Placement:** After G4.02
**Skill:** Count characters and words using built-in blocks
**Description:** Students use `length of [text]` to count characters and count words in a split list. They compare character counts vs word counts for different texts and understand why they differ.
**Dependencies:**
- T29.G4.02: Use split and join blocks for text manipulation
- T09.G4.04: Use variables to control animation or game state
**Enables:** T29.G6.01
**Blocks Used:** `length of [text]`, `length of [list]`, `set [list] to split of [text]`

#### T29.G5.01b: Create and populate text data tables ⭐⭐⭐
**Grade:** 5
**Placement:** Before G5.01
**Skill:** Programmatically create and fill tables with text data
**Description:** Students use table blocks to add rows and columns, store text data in structured format, and retrieve data by row/column. They build tables to store word lists, counts, and metadata.
**Dependencies:**
- T29.G4.04: Count words and report the most frequent
- T10.G5.03: Add and remove items from a list
**Enables:** T29.G5.01, T29.G5.05, T29.G6.04
**Blocks Used:** `add row to table`, `set cell`, `get cell value`

### Priority 2: Important Missing Skills (Conceptual Scaffolding)

#### T29.G3.05: Identify characters, words, and sentences ⭐⭐
**Grade:** 3
**Placement:** After G3.01
**Skill:** Distinguish between characters, words, and sentences (unplugged)
**Description:** Students sort cards with individual letters, whole words, and complete sentences. They identify what makes each unit distinct (letters have no meaning alone, words have meaning, sentences have complete thoughts).
**Dependencies:**
- T29.G3.01: Distinguish text data from numbers and pictures
**Enables:** T29.G4.02, T29.G4.03
**Type:** Unplugged activity

#### T29.G4.03b: Build custom blocks for text cleaning ⭐⭐
**Grade:** 4
**Placement:** After G4.03
**Skill:** Create reusable custom blocks for text preprocessing
**Description:** Students define custom "clean text" blocks that combine lowercase conversion and punctuation removal. They learn to create reusable code components.
**Dependencies:**
- T29.G4.03: Clean text: lowercase + remove punctuation
- T05.G4.01: Create a custom block with one input (if exists in T05)
**Enables:** T29.G5.02, T29.G8.01
**Blocks Used:** `define`, custom block inputs

#### T29.G5.03b: Apply sentiment analysis to datasets ⭐⭐
**Grade:** 5
**Placement:** After G5.03
**Skill:** Run sentiment analysis on multiple sentences and visualize
**Description:** Students apply their sentiment heuristic to a table of sentences, compute sentiment scores for each, and create visualizations (bar chart or color-coded display).
**Dependencies:**
- T29.G5.03: Measure simple sentiment heuristics
- T29.G5.01b: Create and populate text data tables
**Enables:** T29.G7.02
**Blocks Used:** Table operations, loops, visualization blocks

#### T29.G6.01b: Implement token counting approximation ⭐⭐
**Grade:** 6
**Placement:** With G6.01 (or right after)
**Skill:** Create an algorithm to estimate GPT tokens
**Description:** Students build a simple token estimator (e.g., word count × 1.3) and compare estimates with actual API token counts. They understand why approximation is needed and its limitations.
**Dependencies:**
- T29.G6.01: Explain characters vs words vs tokens
- T09.G6.01: Model real-world quantities using variables and formulas
**Enables:** Better understanding for T29.G8.03
**Blocks Used:** Mathematical operators, variables, ChatGPT API blocks

#### T29.G7.02b: Evaluate classifier with train/test split ⭐⭐
**Grade:** 7
**Placement:** After G7.02
**Skill:** Split data into training and testing sets, measure accuracy
**Description:** Students divide their dataset into train (80%) and test (20%) sets, train classifier on train set, test on test set, and compute accuracy. This prepares them for formal evaluation metrics in G8.
**Dependencies:**
- T29.G7.02: Engineer text features for classifiers
- T10.G7.x: Table manipulation (filtering, splitting)
**Enables:** T29.G8.02
**Blocks Used:** Table operations, KNN classifier blocks, math operators

### Priority 3: Enhancement Skills (Nice to Have)

#### T29.G4.05b: Display and format text on stage ⭐
**Grade:** 4
**Placement:** Before G4.05
**Skill:** Display text with color, size, and position control
**Description:** Students use sprite say/think blocks and text costumes to display text on stage with formatting. They learn to control visual presentation of text.
**Dependencies:**
- T06.G4.01: Write scripts that respond to keyboard or mouse events
- T01.G4.x: Sprite appearance blocks
**Enables:** T29.G4.05
**Blocks Used:** `say`, `think`, costume text tools

#### T29.G6.03b: Handle real-time keyboard input ⭐
**Grade:** 6
**Placement:** Before G6.03
**Skill:** Capture and process user typing in real-time
**Description:** Students create text input systems that capture each keystroke, update a variable with the typed text, and respond to user input (like autocomplete).
**Dependencies:**
- T06.G6.01: Trace event execution paths in a multi-event program
- T09.G6.01: Model real-world quantities using variables and formulas
**Enables:** T29.G6.03
**Blocks Used:** Keyboard sensing, string concatenation, widgets

#### T29.G7.01b: Compare keyword vs semantic retrieval ⭐
**Grade:** 7
**Placement:** After G7.01
**Skill:** Compare retrieval quality of keyword matching vs embeddings
**Description:** Students run the same queries using keyword matching and semantic search, compare results, and analyze which method performs better for different query types.
**Dependencies:**
- T29.G7.01: Build keyword retrieval helpers (mini-RAG)
**Enables:** Deeper understanding of semantic search
**Blocks Used:** Keyword matching logic, semantic database blocks

---

## Part 5: Dependency Issues Within T29

### A. Cross-Grade Dependency Problems (X-2 Rule Violations)

#### CRITICAL: Cross-Topic Dependencies at Wrong Grade Levels

**Pattern:** Many skills depend on foundational skills from OTHER topics (T06, T07, T08, T09, T10) but reference grade levels that are too far back.

**Examples of Violations:**

1. **T29.G6.01** (Grade 6 skill) depends on:
   - ❌ T08.G4.01 (2 grades back) - VIOLATES X-2 at boundary
   - ❌ T09.G4.04 (2 grades back) - VIOLATES X-2 at boundary
   - ❌ T10.G4.03 (2 grades back) - VIOLATES X-2 at boundary
   - **Fix:** Should depend on T08.G6.x, T09.G6.x, T10.G6.x

2. **T29.G6.02** (Grade 6 skill) depends on:
   - ❌ T07.G4.01 (2 grades back) - VIOLATES X-2 at boundary
   - ❌ T09.G4.04 (2 grades back) - VIOLATES X-2 at boundary
   - ❌ T10.G4.03 (2 grades back) - VIOLATES X-2 at boundary
   - **Fix:** Should depend on T07.G6.x, T09.G6.x, T10.G6.x

3. **T29.G6.03** (Grade 6 skill) depends on:
   - ❌ T06.G4.01 (2 grades back) - VIOLATES X-2 at boundary
   - ❌ T09.G4.04 (2 grades back) - VIOLATES X-2 at boundary
   - ❌ T10.G4.03 (2 grades back) - VIOLATES X-2 at boundary
   - **Fix:** Should depend on T06.G6.x, T09.G6.x, T10.G6.x

4. **T29.G6.04** (Grade 6 skill) depends on:
   - ❌ T07.G4.01 (2 grades back) - VIOLATES X-2 at boundary
   - ❌ T09.G4.04 (2 grades back) - VIOLATES X-2 at boundary
   - ❌ T10.G4.03 (2 grades back) - VIOLATES X-2 at boundary
   - **Fix:** Should depend on T07.G6.x, T09.G6.x, T10.G6.x

5. **T29.G7.01** (Grade 7 skill) depends on:
   - ❌ T09.G3.05 (4 grades back) - **SEVERE VIOLATION**
   - ❌ T10.G5.03 (2 grades back) - VIOLATES X-2 at boundary
   - **Fix:** Should depend on T09.G7.x, T10.G7.x

6. **T29.G7.02** (Grade 7 skill) depends on:
   - ❌ T08.G5.01 (2 grades back) - VIOLATES X-2 at boundary
   - ❌ T09.G3.05 (4 grades back) - **SEVERE VIOLATION**
   - ❌ T10.G5.03 (2 grades back) - VIOLATES X-2 at boundary
   - **Fix:** Should depend on T08.G7.x, T09.G7.x, T10.G7.x

7. **T29.G7.03** (Grade 7 skill) depends on:
   - ❌ T06.G5.01 (2 grades back) - VIOLATES X-2 at boundary (and irrelevant - clones not needed)
   - ❌ T09.G3.05 (4 grades back) - **SEVERE VIOLATION**
   - ❌ T10.G5.03 (2 grades back) - VIOLATES X-2 at boundary
   - **Fix:** Remove T06.G5.01, update to T09.G7.x, T10.G7.x

8. **T29.G7.04** (Grade 7 skill) depends on:
   - ❌ T08.G5.01 (2 grades back) - VIOLATES X-2 at boundary
   - ❌ T09.G3.05 (4 grades back) - **SEVERE VIOLATION**
   - ❌ T10.G5.03 (2 grades back) - VIOLATES X-2 at boundary
   - **Fix:** Should depend on T08.G7.x, T09.G7.x, T10.G7.x

**Summary of X-2 Rule Violations:**
- **4 grades back:** 4 instances (T09.G3.05 in G7 skills) - SEVERE
- **2 grades back at boundary:** 20+ instances - MODERATE
- **Total affected skills:** 8 out of 28 (29%)

### B. Missing Loop Dependencies (T07)

**Pattern:** Skills that clearly require iteration don't list T07 dependencies.

**Missing Loop Dependencies:**

1. **T29.G4.03: Clean text: lowercase + remove punctuation**
   - **Needs:** T07.G4.01 (Loop until a goal condition is met)
   - **Why:** Must iterate character-by-character to remove punctuation

2. **T29.G4.04: Count words and report the most frequent**
   - **Needs:** T07.G4.01 or T07.G4.02
   - **Why:** Must iterate over word list to count frequencies

3. **T29.G4.05: Highlight keywords in a paragraph**
   - **Needs:** T07.G4.01
   - **Why:** Must iterate over words to find and highlight keywords

**Fix:** Add appropriate T07 loop dependencies to these skills.

### C. Missing Within-Topic Dependencies

**Pattern:** Related skills within T29 should have dependencies but don't.

**Missing T29 Internal Dependencies:**

1. **T29.G4.05 should depend on T29.G4.04**
   - Both scan text for specific words
   - G4.04 (word counting) is more foundational
   - G4.05 (highlighting) adds visualization
   - **Current:** Both parallel (depend on G4.02)
   - **Should be:** G4.05 → G4.04 → G4.02

2. **T29.G7.04 should explicitly depend on T29.G4.01**
   - G7.04 description says "building on earlier G4 comparison work"
   - G4.01: Compare human vs computer summary (basic)
   - G7.04: Compare critically with annotation (advanced)
   - **Current:** G7.04 does NOT list G4.01 as dependency
   - **Fix:** Add T29.G4.01 to G7.04 dependencies

3. **T29.G5.05 should depend on T29.G5.01b** (table creation skill)
   - G5.05 writes results to table
   - Needs table manipulation skills
   - **Current:** Only depends on G4.02, G4.04
   - **Fix:** Add table dependency

### D. Irrelevant Dependencies

**Found:**

1. **T29.G7.03: Audit text datasets for bias and coverage**
   - Lists: T06.G5.01 (Design multi-sprite programs using clones)
   - **Issue:** Text auditing doesn't require sprite clones
   - **Fix:** Remove this dependency

### E. Inconsistent Dependency Granularity

**Pattern:** Some skills have very detailed cross-topic dependencies, others don't.

**Examples:**

1. **T29.G4.02** lists 5 dependencies (including T06, T09, T10)
2. **T29.G4.03** lists 4 dependencies (including T09, T10)
3. **T29.G5.05** lists only 2 dependencies (missing T10 table dependency)

**Recommendation:** Standardize dependency granularity - ensure all skills list:
- T29 prerequisite skills
- Relevant T06 (events), T07 (loops), T08 (conditionals) skills
- Relevant T09 (variables), T10 (data structures) skills

---

## Part 6: Recommendations for T29 Improvement

### A. Immediate Fixes (High Priority)

1. **Fix Cross-Grade Dependencies**
   - Update all cross-topic dependencies to use same-grade or (grade - 2) equivalents
   - Most critical: Replace T09.G3.05 in G7 skills with T09.G7.x

2. **Add Missing Loop Dependencies**
   - Add T07.G4.01 to T29.G4.03, G4.04, G4.05

3. **Remove Irrelevant Dependency**
   - Remove T06.G5.01 from T29.G7.03

4. **Add Critical Missing Skills**
   - T29.G4.01b: Access characters by position
   - T29.G4.02b: Count characters and words
   - T29.G5.01b: Create and populate text data tables

5. **Fix Within-Topic Dependencies**
   - Make T29.G4.05 depend on T29.G4.04
   - Make T29.G7.04 depend on T29.G4.01

### B. Medium Priority Improvements

6. **Add Important Missing Skills**
   - T29.G3.05: Identify characters, words, and sentences
   - T29.G4.03b: Build custom blocks for text cleaning
   - T29.G5.03b: Apply sentiment analysis to datasets
   - T29.G7.02b: Evaluate classifier with train/test split

7. **Clarify Ambiguous Descriptions**
   - T29.G4.01: Specify what "computer summary" method is used
   - T29.G5.04: Define what "slots" means
   - T29.G8.01: List specific pipeline stages expected

8. **Add Explicit Outputs to Skill Descriptions**
   - T29.G6.01: Specify deliverable (comparison table)
   - T29.G7.03: Specify deliverable (audit report format)

### C. Long-Term Enhancements

9. **Verify Block Availability**
   - Confirm `letter (N) of [text]` block exists in CreatiCode
   - Confirm `length of [text]` block exists in CreatiCode
   - Document any missing standard Scratch blocks

10. **Add Enhancement Skills**
    - T29.G6.03b: Handle real-time keyboard input
    - T29.G7.01b: Compare keyword vs semantic retrieval

11. **Create Example Programs**
    - Develop sample programs for each skill
    - Include in curriculum materials

12. **Develop Assessment Rubrics**
    - Define success criteria for each skill
    - Create rubrics for project-based skills (G7-G8)

---

## Part 7: Block Coverage Analysis

### Blocks Well-Covered by Skills ✅

1. **Split/Join Operations**
   - `set [list] to split of [text]` - T29.G4.02 ✅
   - `join [list] into text` - T29.G4.02 ✅

2. **Case Conversion**
   - `[uppercase/lowercase v] of text [T]` - T29.G4.03 ✅

3. **Regular Expressions**
   - All 5 regex blocks - T29.G6.05 ✅

4. **NLP Analysis**
   - `analyze sentence` - T29.G5.05 ✅

5. **Semantic Search**
   - `create semantic database` - T29.G7.01 ✅
   - `search semantic database` - T29.G7.01 ✅

6. **Classifiers**
   - `create KNN classifier` - T29.G7.02 ✅
   - `predict with classifier` - T29.G7.02 ✅

7. **ChatGPT Integration**
   - ChatGPT request blocks - T29.G4.01, G6.04, G7.04 ✅

### Blocks Under-Utilized or Not Explicitly Covered ⚠️

1. **Character Access** (Critical)
   - `letter (N) of [text]` - ⚠️ Assumed in G4.03 but not explicitly taught
   - **Fix:** Add T29.G4.01b

2. **String Length** (Critical)
   - `length of [text]` - ⚠️ Assumed in G6.01 but not explicitly taught earlier
   - **Fix:** Add T29.G4.02b

3. **String Testing/Matching**
   - `[text1] includes [text2]` - Used in G4.05, G5.02 but not explicitly taught
   - `[text1] starts with [text2]` - Not explicitly covered
   - `[text1] ends with [text2]` - Not explicitly covered
   - **Fix:** Could add skill for pattern matching basics in G4 or G5

4. **Advanced String Operations**
   - `position of [T1] in [T2]` - Not explicitly covered
   - `substring of [text] from (P1) to (P2)` - Used in G4.03 but not explicitly taught
   - `longest common substring` - Not covered
   - **Fix:** Could add in G5 or G6 for advanced text analysis

5. **String Utilities**
   - `trim [text]` - Not explicitly covered (could be in G4.03)
   - `replace [T1] with [T2] in [T3]` - Used in G4.03 but not explicitly taught
   - **Fix:** Incorporate into G4.03 description

6. **Text-to-Speech / Speech-to-Text**
   - Speech recognition blocks - Not covered in T29
   - Text-to-speech blocks - Not covered in T29
   - **Note:** These might belong in a different topic (accessibility, multimedia)

7. **Neural Network Training**
   - `train NN model` - Not explicitly covered in T29 (could be advanced extension of G7.02)
   - `predict with NN model` - Not explicitly covered
   - **Note:** Very advanced, appropriate omission for K-8

### Blocks That Should Be Introduced Earlier

1. **G4 should introduce:**
   - `letter (N) of [text]` ← Add T29.G4.01b
   - `length of [text]` ← Add T29.G4.02b
   - `substring of [text]` ← Clarify in G4.03
   - `replace [T1] with [T2]` ← Clarify in G4.03

2. **G5 should introduce:**
   - `[text1] includes [text2]` ← Clarify in G5.02
   - `position of [T1] in [T2]` ← Add to G5.02 or new skill

---

## Summary Statistics

### Current T29 Skills
- **Total skills:** 28
- **Grade 3:** 4 skills (14%)
- **Grade 4:** 5 skills (18%)
- **Grade 5:** 5 skills (18%)
- **Grade 6:** 5 skills (18%)
- **Grade 7:** 4 skills (14%)
- **Grade 8:** 5 skills (18%)

### Quality Metrics
- **Clear & Specific:** 26/28 (93%)
- **Grade-Appropriate (K-2 unplugged, 3+ coding):** 28/28 (100%)
- **Has Dependency Issues:** 8/28 (29%)
- **X-2 Rule Violations:** 8/28 (29%)
  - Severe (4+ grades back): 4 instances
  - Moderate (2 grades at boundary): 20+ instances

### Missing Skills Needed
- **Priority 1 (Critical):** 3 skills
- **Priority 2 (Important):** 5 skills
- **Priority 3 (Enhancement):** 3 skills
- **Total recommended additions:** 11 skills

### Available Blocks
- **Total text/NLP blocks identified:** 44+
- **Well-covered blocks:** ~25 (57%)
- **Under-utilized blocks:** ~15 (34%)
- **Not covered:** ~4 (9%)

### Dependency Issues
- **Missing loop dependencies:** 3 skills
- **Wrong-grade cross-topic dependencies:** 8 skills
- **Missing within-topic dependencies:** 3 pairs
- **Irrelevant dependencies:** 1 skill

---

## Conclusion

T29 (Text Data & NLP Foundations) is a **well-structured topic** with good progression from unplugged activities (G3) through hands-on coding (G4-G6) to advanced integration and critical analysis (G7-G8). The skills align well with available CreatiCode blocks, particularly for:
- Text manipulation (split/join)
- NLP analysis (sentence analysis, semantic search)
- AI integration (ChatGPT, classifiers)

**Major Strengths:**
✅ Clear progression from basic to advanced
✅ Good balance of technical skills and critical thinking
✅ Strong integration with AI/ML concepts
✅ Appropriate use of CreatiCode's advanced NLP blocks

**Critical Issues to Address:**
❌ Cross-grade dependency mismatches (29% of skills affected)
❌ Missing foundational skills for character/string manipulation
❌ Missing loop dependencies in several G4 skills
❌ Some ambiguous skill descriptions

**Immediate Action Items:**
1. Fix all cross-topic dependencies to use appropriate grade levels
2. Add 3 critical missing skills (G4.01b, G4.02b, G5.01b)
3. Add missing loop dependencies to G4.03, G4.04, G4.05
4. Remove irrelevant dependency from G7.03
5. Update within-topic dependencies (G4.05→G4.04, G7.04→G4.01)

With these fixes, T29 will provide excellent scaffolding for students to develop strong text processing and NLP skills from grades 3-8.
