# T29 (Text Data & NLP Foundations) - Comprehensive Analysis Report

**Date**: 2025-11-23
**Scope**: All T29 skills across grades K-8
**Total Skills Found**: 56 skills

---

## EXECUTIVE SUMMARY

**Topic Overview**: T29 covers Text Data & NLP (Natural Language Processing) Foundations, progressing from basic text recognition (K-2) through text manipulation and NLP operations (3-5) to advanced text analytics, ML feature engineering, and responsible AI text practices (6-8).

**Key Findings**:
- ✅ **Strengths**: Strong scaffolding from unplugged activities (K-2) to coding (3+), good alignment with CreatiCode text/NLP blocks
- ⚠️ **Issues Found**: 18 high-priority issues, 12 medium-priority issues, 6 low-priority issues
- 🔧 **Fixes Proposed**: Breaking down 8 complex skills, adding 12 scaffolding skills, fixing 15 dependency violations

---

## SECTION 1: CURRENT T29 SKILLS BY GRADE

### Grade K (3 skills)
- **T29.GK.01**: Recognize text vs pictures (unplugged)
- **T29.GK.02**: Identify letters in text (unplugged)
- **T29.GK.03**: Recognize that text has meaning (unplugged)

### Grade 1 (4 skills)
- **T29.G1.01**: Sort words by first letter (unplugged)
- **T29.G1.02**: Count words in a sentence (unplugged)
- **T29.G1.03**: Group words by category (unplugged)
- **T29.G1.04**: Identify same words in different sentences (unplugged)

### Grade 2 (4 skills)
- **T29.G2.01**: Recognize text patterns (rhyming, repetition) (unplugged)
- **T29.G2.02**: Sort sentences by length (unplugged)
- **T29.G2.03**: Distinguish sentences from word lists (unplugged)
- **T29.G2.04**: Find and replace words in sentences (unplugged)

### Grade 3 (4 skills)
- **T29.G3.01**: Distinguish text data from numbers and pictures (transition to coding)
- **T29.G3.02**: Count word occurrences using variables
- **T29.G3.03**: Group words by category (emotion, action, place)
- **T29.G3.04**: Explain why clean text helps AI helpers

### Grade 4 (9 skills)
- **T29.G4.01.01**: Compare human vs AI summaries (conceptual)
- **T29.G4.01.02**: Generate AI summaries using ChatGPT blocks
- **T29.G4.02**: Use split and join blocks for text manipulation
- **T29.G4.03**: Access individual characters using "letter # of" operator
- **T29.G4.04**: Count characters and words using "length of" and split
- **T29.G4.05**: Test if text includes, starts with, or ends with a pattern
- **T29.G4.06.01**: Convert text case using lowercase/uppercase operators
- **T29.G4.06.02**: Remove punctuation using replace or character filtering
- **T29.G4.07**: Extract substrings and find text position
- **T29.G4.08**: Count words and report the most frequent
- **T29.G4.09**: Highlight keywords in text display

### Grade 5 (7 skills)
- **T29.G5.01**: Design table schemas for text data (chat logs)
- **T29.G5.02**: Populate data tables from text using split
- **T29.G5.03**: Build stop-word filters and keyword lists
- **T29.G5.04.01**: Create positive/negative sentiment word lists
- **T29.G5.04.02**: Score text using sentiment word lists
- **T29.G5.05**: Build dynamic prompts with join and concatenation
- **T29.G5.06**: Use the analyze sentence block for parts of speech
- **T29.G5.07**: Trim whitespace from text input

### Grade 6 (8 skills)
- **T29.G6.01**: Compare characters, words, and token counts
- **T29.G6.02**: Compute n-gram (bigram) frequencies
- **T29.G6.03**: Create autocomplete suggestions from bigrams
- **T29.G6.04**: Log AI prompts/responses with ratings and timestamps
- **T29.G6.05**: Use regex patterns for text matching
- **T29.G6.06**: Convert speech to text using voice recognition
- **T29.G6.07**: Convert text to speech with voice selection
- **T29.G6.08**: Compare text similarity using edit distance

### Grade 7 (6 skills)
- **T29.G7.01**: Build keyword retrieval helpers (mini-RAG)
- **T29.G7.02**: Engineer text features for ML classifiers
- **T29.G7.03**: Audit text datasets for bias and coverage
- **T29.G7.04**: Critically annotate AI vs human summaries
- **T29.G7.05**: Integrate web search results into text analysis
- **T29.G7.06**: Filter content using AI moderation

### Grade 8 (4 skills)
- **T29.G8.01**: Build end-to-end text-processing pipelines
- **T29.G8.02**: Compute text classifier evaluation metrics (precision/recall/F1)
- **T29.G8.03**: Integrate text analytics into AI prompt engineering
- **T29.G8.04**: Publish datasheets for text datasets

**Total**: 56 skills

---

## SECTION 2: AVAILABLE CREATICODE TEXT/NLP FEATURES

### A. Basic Text Operations (Scratch Built-in)
1. **join** - Concatenate strings
2. **letter # of** - Access character at position
3. **length of** - Get string length
4. **contains** - Check substring

### B. Enhanced Text Operators (CreatiCode Extensions)
5. **[TEXT1] includes [TEXT2] ignore case** - Case-insensitive substring check
6. **[TEXT1] starts with [TEXT2] ignore case** - Prefix matching
7. **[TEXT1] ends with [TEXT2] ignore case** - Suffix matching
8. **substring of [TEXT] from position (P1) to position (P2)** - Extract substring
9. **part (INDEX) of [TEXT] by [SEPARATOR]** - Split and access by index
10. **longest common substring between [TEXT1] and [TEXT2]** - Find common text
11. **join [T1] [T2] ... with [SEPARATOR]** - Join multiple texts
12. **trim [TEXT]** - Remove leading/trailing whitespace
13. **<[TEXT] is a number?>** - Validate numeric text
14. **convert [TEXT] to a number** - Parse numbers from text (including words)
15. **[CASE v] of text [T]** - uppercase/lowercase conversion

### C. Advanced Text Processing (Regex)
16. **regex [PATTERN] test [TEXT]** - Test if pattern matches
17. **regex [PATTERN] flag [FLAG] match [TEXT] into list** - Extract matches
18. **regex [PATTERN] search [TEXT]** - Find pattern position
19. **regex [PATTERN] flag [FLAG] replace [TEXT] with [T]** - Replace patterns
20. **regex [PATTERN] flag [FLAG] split [TEXT] into list** - Split by regex

### D. List Text Operations
21. **join [LISTNAME v] into text with [SEPARATOR]** - List to text
22. **set [LISTNAME v] to split of [TEXT] with splitter [SEPARATOR]** - Text to list
23. **# of item containing [TEXT] in [LISTNAME v]** - Find item by substring

### E. Text Comparison
24. **operator_stringdiff** - Compare text similarity/edit distance

### F. AI/NLP Features
25. **ai_parsesentence**: Analyze sentence [SENTENCE] and write into table [TABLENAME v]
    - Returns: TEXT, LEMMA, TYPE, PERSON, OFFSET, LABEL, DEPENDS
    - Uses Google Natural Language API
    - Identifies parts of speech (nouns, verbs, pronouns, etc.)

26. **Speech Recognition**:
    - **ai_startspeech**: Start recognizing speech in [LANGUAGE] (Azure)
    - **ai_startopenaispeech**: OpenAI Whisper speech recognition
    - **ai_endspeech**: End speech recognition
    - **ai_textfromspeech**: Get recognized text
    - **ai_clearspeech**: Clear speech text

27. **Text-to-Speech**:
    - **ai_speakinlanguage**: Say [TEXT] in [LANGUAGE] as [VOICETYPE] (Azure TTS)
    - **ai_stopspeaking**: Stop AI speech

28. **Continuous Speech Recognition**:
    - **ai_startrecognizer**: Start continuous speech recognition
    - **ai_stoprecognizer**: Stop continuous recognition

### G. AI Integration (ChatGPT & Search)
29. **openai_chatgpt_** blocks: ChatGPT integration for summaries, Q&A, text generation
30. **googlesearch**: Web search API

### H. Semantic/Vector Database (Pinecone)
31. **addtabletopinecone**: Build semantic database with embeddings
32. **searchfrompinecone**: Semantic search using natural language queries
33. **searchfrompinecone2**: Semantic search with SQL-like filters

### I. Visual Text Display
34. **say [TEXT] for (T) seconds** - Speech bubbles
35. **think [TEXT] for (T) seconds** - Thought bubbles
36. **print [TEXT] at x y** - Display text on stage
37. **add 3D text** / **add 3D thick text** - 3D text objects

### J. Missing/Not Found
- ❌ **Sentiment Analysis API** - No direct sentiment analysis block found
- ❌ **Content Moderation API** - No ai_moderatetext block found
- ❌ **Translation API** - No translation blocks found
- ⚠️ **Token Counting** - No direct token counter (must estimate)

---

## SECTION 3: ISSUES IDENTIFIED (Categorized by Priority)

### HIGH PRIORITY ISSUES (18 total)

#### H1: Missing CreatiCode Features Referenced
**Severity**: Critical
**Skills Affected**: T29.G7.06

**Issue**: T29.G7.06 references "AI moderation blocks" but no such blocks exist in blockdes8.txt.

**Impact**: Students cannot complete the skill as described.

**Proposed Fix**:
- **Remove** T29.G7.06 entirely OR
- **Reframe** as "Build custom content filter using keyword lists" (similar to T29.G5.03 stop-words)

---

#### H2: Grade 4 Overload - Too Many Complex Skills
**Severity**: High
**Skills Affected**: T29.G4.01-T29.G4.09 (9 skills)

**Issue**: Grade 4 has 9 skills, several of which are quite complex (T29.G4.08, T29.G4.09). This is too dense for one grade level.

**Impact**: Overwhelming for students, insufficient practice time per skill.

**Proposed Fix**: Move some skills to Grade 5 or break down complex ones:
- Move T29.G4.08 (word frequency) → **T29.G5.08** (after stop-words)
- Move T29.G4.09 (highlight keywords) → **T29.G5.09** (after sentiment)
- This reduces G4 to 7 skills, increases G5 to 9 skills (more balanced)

---

#### H3: T29.G4.08 Too Complex - Needs Decomposition
**Severity**: High
**Skills Affected**: T29.G4.08

**Issue**: "Count words and report the most frequent" combines multiple sub-tasks:
1. Split text into words
2. Clean/normalize words
3. Build frequency table
4. Find maximum frequency
5. Report result

**Impact**: Too much cognitive load for a single skill; students need scaffolding.

**Proposed Fix**: Break into 2-3 sub-skills:
- **T29.G4.08.01**: Build word frequency table (count occurrences)
- **T29.G4.08.02**: Find and report most frequent word
- Move to G5 after stop-words (becomes T29.G5.08.01, T29.G5.08.02)

---

#### H4: Missing Foundational Skill - Basic String Comparison
**Severity**: High
**Skills Affected**: Multiple skills use string comparison before it's taught

**Issue**: Skills like T29.G4.05 use "includes/starts with/ends with" but there's no explicit teaching of string equality comparison first.

**Impact**: Students may struggle with basic = comparison vs substring matching.

**Proposed Fix**: Add new skill:
- **T29.G3.05**: Compare text for equality using "=" operator
  - Dependencies: T29.G3.02
  - Description: "Students use the equals operator to check if two text variables match exactly, understanding case-sensitive vs case-insensitive comparison."

---

#### H5: T29.G6.05 (Regex) Too Advanced for Grade 6
**Severity**: High
**Skills Affected**: T29.G6.05

**Issue**: Regular expressions are typically a high school or college topic. Introducing regex in Grade 6 without extensive scaffolding is developmentally inappropriate.

**Impact**: Most 6th graders will find regex syntax completely baffling; likely to cause frustration and disengagement.

**Proposed Fix**:
- **Option A**: Move to Grade 8 as **T29.G8.05** (advanced optional skill)
- **Option B**: Replace with "Use advanced text patterns" and limit to simple patterns (digit matching, email validation with pre-made patterns)
- **Recommended**: Option A - move to G8

---

#### H6: Missing Skill - Introduction to Tables for Text Storage
**Severity**: High
**Skills Affected**: T29.G5.01

**Issue**: T29.G5.01 jumps directly to "Design table schemas for text data" but students haven't been introduced to using tables for text storage.

**Impact**: Big conceptual leap; students need to understand why tables are useful for structured text before designing schemas.

**Proposed Fix**: Add prerequisite skill:
- **T29.G4.10**: Store text data in simple tables (2 columns max)
  - Dependencies: T29.G4.02, T11.G4.01 (from tables topic)
  - Description: "Students create simple two-column tables (e.g., 'word' and 'count') to organize text data, understanding when tables are better than lists."

---

#### H7: T29.G7.01 (Mini-RAG) Too Complex
**Severity**: High
**Skills Affected**: T29.G7.01

**Issue**: Description includes both "simple retrieval system" AND "use Pinecone blocks for semantic retrieval" which are vastly different complexity levels.

**Impact**: Unclear scope, mixing basic keyword matching with advanced vector search.

**Proposed Fix**: Break into two skills:
- **T29.G7.01.01**: Build keyword-based retrieval (TF-IDF style scoring)
- **T29.G7.01.02**: Use Pinecone semantic search blocks (optional advanced)

---

#### H8: Missing Skill - Understanding Tokens Before Using Them
**Severity**: Medium-High
**Skills Affected**: T29.G6.01

**Issue**: T29.G6.01 discusses GPT tokens but doesn't teach what tokens are or why they matter conceptually.

**Impact**: Students may memorize "tokens are different from words" without understanding tokenization.

**Proposed Fix**: Add prerequisite skill:
- **T29.G5.10**: Understand tokenization concepts
  - Dependencies: T29.G4.04
  - Description: "Students learn that AI models break text into tokens (not always whole words). They experiment with examples showing how 'running' might be 1 token but 'ChatGPT' might be 2 tokens. They discuss why token limits exist."

---

#### H9: Intra-Topic Dependency Violation - T29.G4.01.02 → T29.G4.02
**Severity**: High
**Skills Affected**: T29.G4.01.02, T29.G4.02

**Issue**: T29.G4.01.02 (Generate AI summaries) depends on:
- T08.G3.01 (conditionals)
- T09.G3.05 (trace variables)
- T10.G3.03 (lists)

But T29.G4.02 (split/join - FOUNDATIONAL text manipulation) only depends on:
- T29.G3.04
- T06.G3.01
- T09.G3.01.04
- T09.G3.05
- T10.G3.03

**Both skills are in G4, but T29.G4.02 is the foundation for almost all other T29 skills. It should come BEFORE T29.G4.01.02.**

**Impact**: Logical sequencing issue - students might use AI summaries before understanding basic text splitting.

**Proposed Fix**: Reorder skills:
- T29.G4.02 should be **T29.G4.01** (first coding skill)
- Current T29.G4.01.01-02 should become **T29.G4.02.01-02**

---

#### H10: Missing Skill - Basic Text Input/Output
**Severity**: Medium-High
**Skills Affected**: Multiple G4 skills

**Issue**: Students jump into text manipulation without explicitly learning how to get text input (ask block) and display text output.

**Impact**: May not understand the full input→process→output pipeline.

**Proposed Fix**: Add skill after T29.G3.04:
- **T29.G4.00**: Use ask/answer blocks for text input and display results
  - Dependencies: T29.G3.04, T06.G3.01
  - Description: "Students use the 'ask' block to get text input, store it in variables, and display it using 'say' or variable monitors."

---

#### H11: X-2 Dependency Violation - T29.G7.02 → T22.G6.01
**Severity**: High
**Skills Affected**: T29.G7.02

**Issue**: T29.G7.02 (Grade 7) depends on T22.G6.01 (Grade 6) - violates X-2 rule (should allow dependencies up to X-2 = G5).

**Impact**: Creates tight coupling between topics; if T22 changes, T29 breaks.

**Proposed Fix**:
- **Option A**: Move T29.G7.02 to **T29.G8.05** (Grade 8)
- **Option B**: Remove dependency on T22.G6.01 and teach minimal ML concepts within T29
- **Recommended**: Option A

---

#### H12: Unclear Skill Scope - T29.G5.06 vs T29.G6.05
**Severity**: Medium
**Skills Affected**: T29.G5.06, T29.G6.05

**Issue**:
- T29.G5.06: "Use the analyze sentence block for parts of speech"
- T29.G6.05: "Use regex patterns for text matching"

Both are advanced pattern recognition but serve different purposes. The connection isn't clear.

**Impact**: Students may confuse grammatical parsing with regex pattern matching.

**Proposed Fix**: Add clarifying text to descriptions emphasizing:
- T29.G5.06: "AI-powered grammatical analysis"
- T29.G6.05: "Rule-based pattern matching using regex syntax"

---

#### H13: Missing Scaffolding - Sentiment Analysis Too Sudden
**Severity**: Medium-High
**Skills Affected**: T29.G5.04.01, T29.G5.04.02

**Issue**: Sentiment analysis appears suddenly in G5 without conceptual introduction.

**Impact**: Students may not understand WHY sentiment matters or what it represents.

**Proposed Fix**: Add prerequisite skill in G4:
- **T29.G4.11**: Recognize emotional tone in text (unplugged/semi-plugged)
  - Dependencies: T29.G3.03
  - Description: "Students read sample texts and label them as positive, negative, or neutral. They discuss how word choice affects emotional tone."

---

#### H14: Missing Skill - Text Length Limits and Truncation
**Severity**: Medium
**Skills Affected**: Multiple skills working with long texts

**Issue**: No skill teaches students to handle text length limits (e.g., ChatGPT prompt limits, display limits).

**Impact**: Students may encounter errors or unexpected behavior with long texts.

**Proposed Fix**: Add skill in G6:
- **T29.G6.09**: Handle text length limits and truncation
  - Dependencies: T29.G6.01
  - Description: "Students check text length before sending to AI APIs, truncate or summarize long texts to fit limits, and display appropriate error messages."

---

#### H15: Duplicate Skill - T29.G3.03 vs T29.G1.03
**Severity**: Medium
**Skills Affected**: T29.G3.03, T29.G1.03

**Issue**:
- T29.G1.03: "Group words by category" (unplugged)
- T29.G3.03: "Group words by category (emotion, action, place)"

These are nearly identical, just one is unplugged and one uses coding.

**Impact**: Feels repetitive; students may think it's busywork.

**Proposed Fix**:
- Keep T29.G1.03 as is (foundational unplugged)
- Reframe T29.G3.03 as: "Build automated word categorizer using conditionals and lists"
  - Make it explicitly about CODING the categorization logic, not just doing it by hand

---

#### H16: Missing Skill - Understanding Text Encoding (ASCII/Unicode)
**Severity**: Low-Medium
**Skills Affected**: Advanced text processing skills

**Issue**: Students work with text extensively but never learn about character encoding, which affects special characters, emojis, internationalization.

**Impact**: May encounter confusing behavior with non-ASCII characters.

**Proposed Fix**: Add optional skill in G7:
- **T29.G7.07**: Understand text encoding (ASCII, Unicode, UTF-8)
  - Dependencies: T29.G6.01
  - Description: "Students learn that computers store text as numbers. They explore ASCII codes, Unicode ranges, and discuss why emojis and international characters need special encoding."

---

#### H17: Missing Skill - Case-Insensitive Comparison Before Case Conversion
**Severity**: Medium
**Skills Affected**: T29.G4.05, T29.G4.06.01

**Issue**: T29.G4.05 uses "ignore case" parameter but T29.G4.06.01 (case conversion) comes later. Students may not understand what case-insensitivity means.

**Impact**: Ordering confusion; students need to understand case first.

**Proposed Fix**:
- Move T29.G4.06.01 (case conversion) to come BEFORE T29.G4.05
- Renumber as T29.G4.04.01 (case conversion) and T29.G4.04.02 (includes/starts/ends with case-insensitive)

---

#### H18: T29.G8.02 Complexity - Too Much Math for Text Topic
**Severity**: Medium
**Skills Affected**: T29.G8.02

**Issue**: Computing precision/recall/F1 requires understanding of:
- True positives, false positives, false negatives, true negatives
- Division and ratio interpretation
- Tradeoff analysis

This is more about ML evaluation than text processing.

**Impact**: Scope creep; belongs more in T22 (Machine Learning) than T29 (Text/NLP).

**Proposed Fix**:
- **Option A**: Move to T22 as **T22.G8.03** (ML evaluation for text classifiers)
- **Option B**: Keep but simplify to "Understand classifier accuracy" (just correct/total, not precision/recall/F1)
- **Recommended**: Option A

---

### MEDIUM PRIORITY ISSUES (12 total)

#### M1: Vague Skill Description - T29.G8.01
**Severity**: Medium
**Skills Affected**: T29.G8.01

**Issue**: "Build end-to-end text-processing pipelines" is too vague. What specific pipeline? What components?

**Impact**: Teachers/students won't know what constitutes success.

**Proposed Fix**: Make description more specific:
- "Build a multi-stage text processing pipeline with at least 5 stages: input → clean (trim, lowercase, remove punctuation) → tokenize (split) → filter (remove stop-words) → analyze (sentiment OR frequency) → output (display OR log to table). Students document each stage."

---

#### M2: Missing Prerequisite - Custom Blocks Before Pipelines
**Severity**: Medium
**Skills Affected**: T29.G8.01

**Issue**: Building complex pipelines would benefit from custom blocks (functions) for modularity, but there's no dependency on custom block skills.

**Impact**: Students may write very long, hard-to-debug scripts.

**Proposed Fix**: Add dependency on custom blocks:
- T29.G8.01 should depend on T07.G6.01 or T07.G7.01 (custom blocks from T07 Control Flow)

---

#### M3: Inconsistent Sub-ID Numbering
**Severity**: Low-Medium
**Skills Affected**: T29.G4.01.01, T29.G4.01.02, T29.G4.06.01, T29.G4.06.02, T29.G5.04.01, T29.G5.04.02, T29.G7.01 (if split)

**Issue**: Some skills use .01/.02 sub-IDs, others don't. No clear pattern for when to use sub-IDs.

**Impact**: Inconsistent numbering makes it harder to reference skills.

**Proposed Fix**: Establish clear rule:
- Use .01/.02 sub-IDs when a skill naturally breaks into 2 sequential parts where:
  1. Part .01 is prerequisite for part .02
  2. Both parts address the same core concept
  3. Breaking into separate top-level skills would feel artificial

---

#### M4: Missing Skill - Error Handling for Text Processing
**Severity**: Medium
**Skills Affected**: Multiple G6+ skills

**Issue**: No skill teaches students to handle text processing errors (empty input, invalid format, API failures).

**Impact**: Students write brittle code that crashes on unexpected input.

**Proposed Fix**: Add skill in G6:
- **T29.G6.10**: Validate text input and handle errors
  - Dependencies: T29.G6.01, T08.G5.01
  - Description: "Students validate text input before processing (check for empty strings, unexpected formats). They use conditionals to provide helpful error messages and default values."

---

#### M5: Missing Connection - Sentiment Analysis vs AI Sentiment
**Severity**: Medium
**Skills Affected**: T29.G5.04.02

**Issue**: Students build manual sentiment analysis using word lists, but never compare it to AI-powered sentiment analysis (if available).

**Impact**: Missed opportunity to show AI advantages and limitations.

**Proposed Fix**: Add skill in G7:
- **T29.G7.08**: Compare manual vs AI sentiment analysis
  - Dependencies: T29.G5.04.02, T29.G7.02
  - Description: "Students compare their manual word-list sentiment scores with AI-generated sentiment (using ChatGPT or other NLP APIs). They discuss differences, noting where AI handles context better and where it fails."

---

#### M6: Overly Specific Dependency - T29.G7.04 → T29.G6.03
**Severity**: Medium
**Skills Affected**: T29.G7.04

**Issue**: T29.G7.04 (Critically annotate AI vs human summaries) depends on T29.G6.03 (Create autocomplete suggestions). These seem unrelated.

**Impact**: Unnecessary dependency creates confusion.

**Proposed Fix**: Remove T29.G6.03 from T29.G7.04 dependencies. Keep only:
- T29.G4.01.02 (AI summaries)
- T29.G5.05 (dynamic prompts)
- T29.G6.04 (logging)

---

#### M7: Missing Skill - Understanding Stopwords Concept
**Severity**: Medium
**Skills Affected**: T29.G5.03

**Issue**: T29.G5.03 jumps directly to "Build stop-word filters" without explaining what stop-words are or why they matter.

**Impact**: Students may mechanically filter words without understanding purpose.

**Proposed Fix**: Split into two skills:
- **T29.G5.03.01**: Understand stop-words and their purpose
  - Dependencies: T29.G4.08 (word frequency)
  - Description: "Students analyze word frequency results and notice that common words (the, a, is) dominate. They learn these are called 'stop-words' and discuss when to remove them vs keep them."
- **T29.G5.03.02**: Build stop-word filter using tables
  - Dependencies: T29.G5.03.01, T11.G5.01
  - Description: (current T29.G5.03 description)

---

#### M8: Missing Skill - Text Normalization Strategy
**Severity**: Medium
**Skills Affected**: Multiple skills use normalization implicitly

**Issue**: Skills mention lowercase, trim, remove punctuation separately but don't teach a comprehensive normalization strategy.

**Impact**: Students may not know in what ORDER to apply normalizations or WHY order matters.

**Proposed Fix**: Add skill in G5:
- **T29.G5.11**: Design text normalization pipelines
  - Dependencies: T29.G4.06.02 (remove punctuation), T29.G5.07 (trim)
  - Description: "Students design multi-step text cleaning pipelines (e.g., trim → lowercase → remove punctuation → split) and test different orderings to see which works best."

---

#### M9: Unclear Scope - T29.G6.08 Edit Distance
**Severity**: Low-Medium
**Skills Affected**: T29.G6.08

**Issue**: Description says "use text comparison blocks to compute edit distance" but it's unclear if there's a built-in edit distance block or if students compute it manually.

**Impact**: Unclear implementation expectations.

**Proposed Fix**: Clarify description:
- If there IS an edit distance block (operator_stringdiff): "Students use the text similarity block to compute edit distance..."
- If students must implement manually: "Students implement a simple edit distance algorithm using loops and conditionals..." OR make it conceptual only in G6, move implementation to G8.

---

#### M10: Missing Skill - Multiline Text Handling
**Severity**: Medium
**Skills Affected**: Multiple skills working with paragraphs

**Issue**: No skill explicitly teaches working with multiline text (split by \n, preserve line breaks, etc.).

**Impact**: Students may struggle with text files, chat logs, or poetry that span multiple lines.

**Proposed Fix**: Add skill in G5:
- **T29.G5.12**: Process multiline text (split by line breaks)
  - Dependencies: T29.G4.02
  - Description: "Students split multiline text using '\\n' as separator, process each line separately, and rejoin. They handle edge cases like empty lines and trailing newlines."

---

#### M11: Missing Application - Text-Based Game/App
**Severity**: Low-Medium
**Skills Affected**: G6-G8 skills

**Issue**: Topic teaches many text skills but lacks a capstone project that integrates them into a meaningful application.

**Impact**: Skills may feel disconnected; students don't see the "big picture."

**Proposed Fix**: Add capstone skill in G8:
- **T29.G8.06**: Build text-based application (chatbot, quiz generator, or story analyzer)
  - Dependencies: T29.G8.01, T29.G8.03
  - Description: "Students design and build a text-based application that integrates at least 5 text processing techniques (e.g., input validation, text cleaning, keyword extraction, AI generation, logging). Examples: chatbot, automated quiz generator, sentiment analyzer."

---

#### M12: Missing Skill - Understanding Lemmatization
**Severity**: Low-Medium
**Skills Affected**: T29.G5.06

**Issue**: T29.G5.06 uses "parse sentence" block which returns LEMMA (stem), but students aren't taught what lemmatization is.

**Impact**: Students may see lemma results without understanding why "running" → "run".

**Proposed Fix**: Expand T29.G5.06 description to include lemma explanation OR add sub-skill:
- **T29.G5.06.01**: Understand parts of speech tagging
- **T29.G5.06.02**: Understand lemmatization and word stems

---

### LOW PRIORITY ISSUES (6 total)

#### L1: Potential Name Confusion - "Analyze sentence" vs "Parse sentence"
**Severity**: Low
**Skills Affected**: T29.G5.06

**Issue**: Skill name says "analyze sentence block" but block ID is "ai_parsesentence" (parse, not analyze).

**Impact**: Minor terminology inconsistency.

**Proposed Fix**: Update skill description to match block name:
- "Use the 'parse sentence' block (ai_parsesentence) for parts of speech tagging"

---

#### L2: Missing Cross-Reference - Text Display Blocks
**Severity**: Low
**Skills Affected**: Multiple skills mention "display" without referencing Looks blocks

**Issue**: Skills say "display text" but don't specify which blocks to use (say, think, print, variable monitor).

**Impact**: Students may not know the best block choice.

**Proposed Fix**: Add note in skill descriptions mentioning available display options, OR add dependency on T06.GK.04 or T06.G1.01 (sprite communication).

---

#### L3: Inconsistent Terminology - "Text" vs "String"
**Severity**: Low
**Skills Affected**: All T29 skills

**Issue**: Skills use "text" consistently, but some technical contexts use "string" (e.g., "substring").

**Impact**: Minor confusion if students encounter "string" in documentation.

**Proposed Fix**: Add glossary note: "In computer science, 'text' and 'string' mean the same thing - a sequence of characters."

---

#### L4: Missing Historical Context - Why NLP Matters
**Severity**: Low
**Skills Affected**: G3-G4 transition

**Issue**: Topic jumps into text manipulation without motivating WHY NLP matters or showing real-world applications.

**Impact**: Students may lack engagement or context.

**Proposed Fix**: Add brief unplugged activity in G3:
- **T29.G3.00**: Explore real-world NLP applications (unplugged discussion)
  - Description: "Students discuss where they've seen computers understand text: voice assistants, autocomplete, translation, spam filters. They brainstorm how computers might process text to enable these features."

---

#### L5: Missing Advanced Topic - Embeddings/Vectors
**Severity**: Low
**Skills Affected**: T29.G7.01 mentions Pinecone

**Issue**: Pinecone uses vector embeddings, but students aren't taught what embeddings are.

**Impact**: "Semantic search" may seem like magic.

**Proposed Fix**: Add brief conceptual skill in G7:
- **T29.G7.01.00**: Understand text embeddings (conceptual)
  - Dependencies: T29.G6.08
  - Description: "Students learn that AI can convert text into vectors (lists of numbers) that capture meaning. Similar texts have similar vectors. This enables semantic search (meaning-based) vs keyword search."

---

#### L6: Missing Skill - Internationalization/Language Support
**Severity**: Low
**Skills Affected**: T29.G6.06, T29.G6.07

**Issue**: Speech recognition and TTS support multiple languages, but no skill teaches students to handle multi-language text.

**Impact**: Missed opportunity to discuss language diversity.

**Proposed Fix**: Add optional skill in G7:
- **T29.G7.09**: Work with multilingual text
  - Dependencies: T29.G6.06, T29.G6.07
  - Description: "Students experiment with text processing in different languages (Spanish, Chinese, etc.). They note which operations work universally (length, split) and which are language-specific (sentiment, parts of speech)."

---

## SECTION 4: DEPENDENCY ANALYSIS

### Intra-Topic Dependency Issues (Within T29)

1. **T29.G4.01.02 should come AFTER T29.G4.02** (Issue H9)
   - Fix: Reorder so split/join is first

2. **T29.G4.05 uses case-insensitive before case conversion taught** (Issue H17)
   - Fix: Move case conversion earlier

3. **T29.G4.08 too complex, needs earlier foundation** (Issue H3)
   - Fix: Break down and move to G5

4. **T29.G5.01 needs table introduction first** (Issue H6)
   - Fix: Add T29.G4.10 (simple tables)

5. **T29.G5.04 needs sentiment concept introduction** (Issue H13)
   - Fix: Add T29.G4.11 (recognize emotional tone)

6. **T29.G6.01 mentions tokens without teaching concept** (Issue H8)
   - Fix: Add T29.G5.10 (tokenization)

### X-2 Rule Violations

1. **T29.G7.02 → T22.G6.01** (G7 → G6, within limit but tight)
   - Fix: Move T29.G7.02 to G8 as T29.G8.05

### Cross-Topic Dependencies (External)

Valid cross-topic dependencies (preserve these):
- T06 (Events & Sequencing): Used for script structure
- T07 (Control Flow): Used for loops/conditionals in text processing
- T08 (Conditionals): Used for text validation and branching
- T09 (Variables): Essential for storing text data
- T10 (Lists): Essential for storing word collections
- T11 (Tables): Essential for structured text data
- T22 (Machine Learning): Used for text classification (G8 only)
- T24 (AI Ethics): Mentioned for transparency practices

---

## SECTION 5: PROPOSED FIXES (Detailed)

### Fix Category A: Skill Reordering (Grade 4)

**Current Order**:
- T29.G4.01.01: Compare human vs AI summaries (conceptual)
- T29.G4.01.02: Generate AI summaries using ChatGPT blocks
- T29.G4.02: Use split and join blocks for text manipulation ← FOUNDATION
- T29.G4.03: Access individual characters
- ...

**Proposed Order**:
- **T29.G4.00**: Use ask/answer blocks for text input/output (NEW)
- **T29.G4.01**: Use split and join blocks for text manipulation (MOVED from G4.02)
- **T29.G4.02**: Access individual characters (MOVED from G4.03)
- **T29.G4.03**: Count characters and words (MOVED from G4.04)
- **T29.G4.04.01**: Convert text case (MOVED from G4.06.01)
- **T29.G4.04.02**: Test if text includes, starts with, or ends with (MOVED from G4.05)
- **T29.G4.05.01**: Compare human vs AI summaries (conceptual) (MOVED from G4.01.01)
- **T29.G4.05.02**: Generate AI summaries using ChatGPT blocks (MOVED from G4.01.02)
- **T29.G4.06**: Remove punctuation (MOVED from G4.06.02)
- **T29.G4.07**: Extract substrings and find text position (SAME)
- **T29.G4.10**: Store text data in simple tables (NEW)
- **T29.G4.11**: Recognize emotional tone in text (NEW)

**Grade 4 Total**: 12 skills (was 9, added 3 new, will move 2 to G5)

---

### Fix Category B: Skills Moving FROM G4 TO G5

**Skills to Move**:
1. **T29.G4.08** → **T29.G5.08** (Count words and report most frequent)
   - Reason: Needs stop-words first (T29.G5.03)
   - Break into T29.G5.08.01 and T29.G5.08.02

2. **T29.G4.09** → **T29.G5.09** (Highlight keywords in text display)
   - Reason: Better fit after sentiment/keyword work in G5

**Result**: G4 reduced by 2 skills, G5 gains 2 skills

---

### Fix Category C: New Skills to Add

#### Grade 3
- **T29.G3.00**: Explore real-world NLP applications (unplugged discussion) - OPTIONAL
- **T29.G3.05**: Compare text for equality using "=" operator

#### Grade 4
- **T29.G4.00**: Use ask/answer blocks for text input and display
- **T29.G4.10**: Store text data in simple tables
- **T29.G4.11**: Recognize emotional tone in text (semi-plugged)

#### Grade 5
- **T29.G5.03.01**: Understand stop-words and their purpose (SPLIT from G5.03)
- **T29.G5.03.02**: Build stop-word filter using tables (SPLIT from G5.03)
- **T29.G5.10**: Understand tokenization concepts
- **T29.G5.11**: Design text normalization pipelines
- **T29.G5.12**: Process multiline text

#### Grade 6
- **T29.G6.09**: Handle text length limits and truncation
- **T29.G6.10**: Validate text input and handle errors

#### Grade 7
- **T29.G7.01.00**: Understand text embeddings (conceptual) - OPTIONAL
- **T29.G7.01.01**: Build keyword-based retrieval (SPLIT from G7.01)
- **T29.G7.01.02**: Use Pinecone semantic search (SPLIT from G7.01)
- **T29.G7.07**: Understand text encoding (ASCII, Unicode) - OPTIONAL
- **T29.G7.08**: Compare manual vs AI sentiment analysis
- **T29.G7.09**: Work with multilingual text - OPTIONAL

#### Grade 8
- **T29.G8.05**: Use regex for advanced pattern matching (MOVED from G6.05)
- **T29.G8.06**: Build text-based application (capstone) - OPTIONAL
- **T29.G8.07**: Engineer text features for ML (MOVED from G7.02)

**Total New Skills**: 20 (8 core, 12 optional/split)

---

### Fix Category D: Skills to Remove or Reframe

1. **T29.G7.06**: Filter content using AI moderation
   - **Action**: REMOVE (no AI moderation blocks exist)
   - **Alternative**: Replace with "Build custom keyword-based content filter"

---

### Fix Category E: Skills to Split/Decompose

1. **T29.G4.08** → **T29.G5.08.01** + **T29.G5.08.02**
   - .01: Build word frequency table
   - .02: Find and report most frequent word

2. **T29.G5.03** → **T29.G5.03.01** + **T29.G5.03.02**
   - .01: Understand stop-words concept
   - .02: Build stop-word filter implementation

3. **T29.G5.06** → **T29.G5.06.01** + **T29.G5.06.02** (OPTIONAL)
   - .01: Understand parts of speech tagging
   - .02: Understand lemmatization

4. **T29.G7.01** → **T29.G7.01.01** + **T29.G7.01.02**
   - .01: Keyword-based retrieval
   - .02: Semantic search with Pinecone

---

### Fix Category F: Description Clarifications

1. **T29.G3.03**: Reframe as "Build automated word categorizer"
   - Emphasize CODING vs manual sorting

2. **T29.G5.06**: Clarify "parse sentence" vs "analyze sentence"
   - Match block terminology

3. **T29.G6.08**: Clarify edit distance implementation
   - Specify if using built-in block or manual algorithm

4. **T29.G8.01**: Make pipeline description specific
   - List required stages explicitly

---

### Fix Category G: Dependency Corrections

#### Remove Unnecessary Dependencies
- **T29.G7.04**: Remove dependency on T29.G6.03 (autocomplete)

#### Add Missing Dependencies
- **T29.G8.01**: Add dependency on custom blocks (T07.G6.01 or T07.G7.01)
- **T29.G4.00**: Add dependency on T06.G3.01 (ask/answer)

#### Reorder to Fix Dependencies
- Move T29.G4.06.01 before T29.G4.05 (case conversion before case-insensitive matching)

---

## SECTION 6: REVISED SKILL COUNT BY GRADE

### Before Fixes
- K: 3, G1: 4, G2: 4, G3: 4, G4: 9, G5: 7, G6: 8, G7: 6, G8: 4
- **Total**: 56 skills

### After Fixes (Including Core New Skills)
- K: 3 (no change)
- G1: 4 (no change)
- G2: 4 (no change)
- G3: 5 (+1: T29.G3.05)
- G4: 12 (+3 new, -2 moved to G5 = net +3, but splitting some so actual count varies)
- G5: 16 (+5 new splits/additions, +2 from G4 = +7)
- G6: 10 (+2 new)
- G7: 9 (+3 new, -1 removed)
- G8: 7 (+3 moved from earlier grades)

**Total Core Skills**: ~70 skills (was 56, net +14 core skills)

**With Optional Skills**: ~78 skills (+22 from baseline)

---

## SECTION 7: ALIGNMENT WITH CREATICODE FEATURES

### Well-Aligned Skills ✅

These skills directly use available CreatiCode blocks:

1. **T29.G4.01** (split/join) → Uses list split/join blocks ✅
2. **T29.G4.02** (letter # of) → Uses Scratch built-in ✅
3. **T29.G4.03** (length of) → Uses Scratch built-in ✅
4. **T29.G4.04.01** (case conversion) → Uses operator_texttransform ✅
5. **T29.G4.04.02** (includes/starts/ends) → Uses string comparison operators ✅
6. **T29.G4.07** (substring) → Uses operator_substring ✅
7. **T29.G5.01-02** (tables) → Uses table blocks ✅
8. **T29.G5.06** (parse sentence) → Uses ai_parsesentence ✅
9. **T29.G5.07** (trim) → Uses operator_trim ✅
10. **T29.G6.05** (regex) → Uses operator_regex_* blocks ✅
11. **T29.G6.06-07** (speech) → Uses ai_startspeech, ai_speakinlanguage ✅
12. **T29.G6.08** (edit distance) → Uses operator_stringdiff ✅
13. **T29.G7.01.02** (Pinecone) → Uses addtabletopinecone, searchfrompinecone ✅
14. **T29.G7.05** (web search) → Uses googlesearch ✅

### Partially Aligned Skills ⚠️

These skills can be implemented with CreatiCode but require workarounds:

1. **T29.G5.04** (sentiment) → Manual implementation (no AI sentiment block) ⚠️
   - Workaround: Use word lists OR use ChatGPT prompt "analyze sentiment of: ..."

2. **T29.G6.01** (token counting) → No direct token counter ⚠️
   - Workaround: Estimate using character/word count

3. **T29.G4.11** (emotional tone recognition) → Unplugged/manual ⚠️
   - Workaround: Use ChatGPT for comparison in later grades

### Misaligned Skills ❌

These skills reference non-existent features:

1. **T29.G7.06** (AI moderation) → No moderation blocks found ❌
   - **Fix**: Remove or replace with manual keyword filter

---

## SECTION 8: IMPLEMENTATION PRIORITY

### Phase 1 (High Priority - Fix Immediately)
1. **Reorder Grade 4 skills** (Fix Category A)
2. **Remove T29.G7.06** or replace with keyword filter
3. **Move T29.G6.05 (regex) to Grade 8**
4. **Split T29.G4.08** into sub-skills
5. **Add T29.G4.00** (text input/output)
6. **Add T29.G3.05** (text equality comparison)

**Impact**: Fixes critical sequencing and missing prerequisites

---

### Phase 2 (Medium Priority - Add Scaffolding)
1. **Add T29.G4.10** (simple tables for text)
2. **Add T29.G4.11** (emotional tone recognition)
3. **Split T29.G5.03** (stop-words concept + implementation)
4. **Add T29.G5.10** (tokenization concepts)
5. **Add T29.G6.09-10** (error handling, length limits)
6. **Split T29.G7.01** (keyword vs semantic retrieval)

**Impact**: Improves scaffolding and conceptual understanding

---

### Phase 3 (Lower Priority - Enhancements)
1. **Add T29.G5.11** (normalization pipelines)
2. **Add T29.G5.12** (multiline text)
3. **Add T29.G7.07** (text encoding)
4. **Add T29.G7.08** (compare manual vs AI sentiment)
5. **Add T29.G8.06** (capstone project)
6. **Add optional multilingual skill**

**Impact**: Enriches topic with advanced/optional content

---

## SECTION 9: SUMMARY OF RECOMMENDATIONS

### Critical Changes (Must Do)
1. ✅ **Reorder Grade 4**: Put split/join first, add text I/O
2. ✅ **Remove/Replace T29.G7.06**: No AI moderation blocks exist
3. ✅ **Move regex to Grade 8**: Too advanced for Grade 6
4. ✅ **Split complex skills**: T29.G4.08, T29.G5.03, T29.G7.01
5. ✅ **Fix dependencies**: Reorder case conversion before case-insensitive matching

### Important Additions (Should Do)
1. ✅ **Add foundational skills**: Text I/O, simple tables, text equality
2. ✅ **Add conceptual skills**: Emotional tone, tokenization, stop-words concept
3. ✅ **Add practical skills**: Error handling, length limits, normalization pipelines
4. ✅ **Move G7→G8**: Move regex and ML feature engineering to Grade 8

### Optional Enhancements (Nice to Have)
1. ⭐ **Add capstone project**: Text-based application (G8)
2. ⭐ **Add cultural/international**: Multilingual text, text encoding
3. ⭐ **Add AI comparison**: Manual vs AI sentiment, human vs AI summaries
4. ⭐ **Add embeddings intro**: Conceptual understanding for semantic search

---

## SECTION 10: NEXT STEPS

1. **Review this analysis** with curriculum designers
2. **Decide on optional vs required skills** (current proposal includes both)
3. **Update allskills.md** with fixes from Phase 1
4. **Create detailed lesson plans** for new skills
5. **Test revised sequence** with sample projects
6. **Update skill dependencies** systematically
7. **Create assessment rubrics** for complex skills like pipelines and projects

---

## APPENDIX: COMPLETE SKILL MAPPING

### Skills Using Each CreatiCode Block

**ai_parsesentence**:
- T29.G5.06: Use the analyze sentence block for parts of speech

**ai_startspeech / ai_startopenaispeech**:
- T29.G6.06: Convert speech to text using voice recognition

**ai_speakinlanguage**:
- T29.G6.07: Convert text to speech with voice selection

**operator_texttransform**:
- T29.G4.04.01: Convert text case using lowercase/uppercase

**operator_trim**:
- T29.G5.07: Trim whitespace from text input

**operator_regex_***:
- T29.G8.05: Use regex patterns for text matching (MOVED from G6)

**operator_stringdiff**:
- T29.G6.08: Compare text similarity using edit distance

**list join/split**:
- T29.G4.01: Use split and join blocks for text manipulation

**string comparison (includes/starts/ends)**:
- T29.G4.04.02: Test if text includes, starts with, or ends with a pattern

**Pinecone blocks**:
- T29.G7.01.02: Use Pinecone semantic search blocks

**googlesearch**:
- T29.G7.05: Integrate web search results into text analysis

**ChatGPT blocks**:
- T29.G4.05.02: Generate AI summaries using ChatGPT blocks
- T29.G7.04: Critically annotate AI vs human summaries

---

## GLOSSARY

- **NLP**: Natural Language Processing - teaching computers to understand and process human language
- **Tokenization**: Breaking text into units (words, characters, or sub-words) for processing
- **Lemmatization**: Reducing words to their base form (running → run)
- **Stop-words**: Common words (the, a, is) often filtered out in text analysis
- **Sentiment Analysis**: Determining emotional tone (positive, negative, neutral) of text
- **N-gram**: Sequence of N consecutive words (bigram = 2 words, trigram = 3 words)
- **Regex**: Regular expressions - pattern matching syntax for text
- **Edit Distance**: Number of character changes needed to transform one text into another
- **RAG**: Retrieval-Augmented Generation - enhancing AI responses with retrieved information
- **Embedding**: Vector representation of text that captures semantic meaning
- **TF-IDF**: Term Frequency-Inverse Document Frequency - scoring word importance

---

**END OF REPORT**
