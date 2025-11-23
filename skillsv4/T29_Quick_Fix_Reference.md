# T29 Quick Fix Reference

## HIGH-PRIORITY FIXES (Do These First)

### 1. REORDER GRADE 4 SKILLS
**Problem**: Split/join (foundation) comes AFTER AI summaries
**Fix**: Make split/join the FIRST G4 skill

**New G4 Order**:
```
T29.G4.00 (NEW) → Use ask/answer blocks for text I/O
T29.G4.01 ← Use split and join (WAS G4.02)
T29.G4.02 ← Access individual characters (WAS G4.03)
T29.G4.03 ← Count characters and words (WAS G4.04)
T29.G4.04.01 ← Convert case (WAS G4.06.01)
T29.G4.04.02 ← Test includes/starts/ends (WAS G4.05)
T29.G4.05.01 ← Compare human vs AI summaries (WAS G4.01.01)
T29.G4.05.02 ← Generate AI summaries (WAS G4.01.02)
T29.G4.06 ← Remove punctuation (WAS G4.06.02)
T29.G4.07 ← Extract substrings (SAME)
```

---

### 2. REMOVE T29.G7.06
**Problem**: References "AI moderation blocks" that don't exist
**Fix**: DELETE this skill OR replace with:
```
T29.G7.06 (REVISED): Build custom content filter using keyword lists
Description: Students create tables of inappropriate keywords and use
string matching to flag potentially problematic content. They discuss
limitations of keyword-based filtering and ethical considerations.
```

---

### 3. MOVE REGEX TO GRADE 8
**Problem**: T29.G6.05 (regex) is too advanced for 6th grade
**Fix**:
```
DELETE: T29.G6.05
ADD: T29.G8.05 - Use regex for advanced pattern matching
(same description, moved to G8)
```

---

### 4. SPLIT T29.G4.08 (Word Frequency)
**Problem**: Too complex, combines multiple sub-tasks
**Fix**: Break into 2 skills and MOVE to G5:
```
DELETE: T29.G4.08

ADD: T29.G5.08.01 - Build word frequency table
Description: Students split text into words, loop through each word,
and count occurrences using a table with "word" and "count" columns.

ADD: T29.G5.08.02 - Find and report most frequent word
Description: Students iterate through their frequency table to find
the word with highest count and display it.
Dependencies: T29.G5.08.01
```

---

### 5. ADD MISSING FOUNDATIONS

#### T29.G3.05 - Compare text for equality
```
ID: T29.G3.05
Skill: Compare text for equality using "=" operator
Description: Students use the equals operator to check if two text
variables match exactly, understanding case-sensitive vs case-insensitive
comparison.
Dependencies: T29.G3.02
```

#### T29.G4.00 - Text input/output
```
ID: T29.G4.00
Skill: Use ask/answer blocks for text input and display results
Description: Students use the 'ask' block to get text input, store it
in variables, and display it using 'say' or variable monitors.
Dependencies: T29.G3.04, T06.G3.01
```

#### T29.G4.10 - Simple tables for text
```
ID: T29.G4.10
Skill: Store text data in simple tables (2 columns max)
Description: Students create simple two-column tables (e.g., 'word'
and 'count') to organize text data, understanding when tables are
better than lists.
Dependencies: T29.G4.02, T11.G4.01
```

#### T29.G4.11 - Emotional tone recognition
```
ID: T29.G4.11
Skill: Recognize emotional tone in text (unplugged/semi-plugged)
Description: Students read sample texts and label them as positive,
negative, or neutral. They discuss how word choice affects emotional tone.
Dependencies: T29.G3.03
```

---

## MEDIUM-PRIORITY FIXES

### 6. SPLIT T29.G5.03 (Stop-words)
```
DELETE: T29.G5.03

ADD: T29.G5.03.01 - Understand stop-words and their purpose
Description: Students analyze word frequency results and notice that
common words (the, a, is) dominate. They learn these are called
'stop-words' and discuss when to remove them vs keep them.
Dependencies: T29.G5.08.01

ADD: T29.G5.03.02 - Build stop-word filter using tables
Description: Learners create a table of stop-words (common words like
"the", "a", "is") and filter them out before running frequency counts
to focus on meaningful words.
Dependencies: T29.G5.03.01, T11.G5.01
```

---

### 7. SPLIT T29.G7.01 (Mini-RAG)
```
DELETE: T29.G7.01

ADD: T29.G7.01.01 - Build keyword-based retrieval
Description: Students build a simple retrieval system by storing
paragraph snippets in a table, computing keyword overlap scores,
and returning the best-matching snippet.
Dependencies: T29.G5.03.02, T29.G6.02, T29.G6.03, T11.G6.01

ADD: T29.G7.01.02 - Use Pinecone semantic search blocks (advanced)
Description: Advanced students use "add table to Pinecone" and
"search from Pinecone" blocks for embedding-based semantic retrieval,
comparing results to keyword-based retrieval.
Dependencies: T29.G7.01.01
```

---

### 8. ADD ERROR HANDLING & VALIDATION

#### T29.G6.09 - Text length limits
```
ID: T29.G6.09
Skill: Handle text length limits and truncation
Description: Students check text length before sending to AI APIs,
truncate or summarize long texts to fit limits, and display
appropriate error messages.
Dependencies: T29.G6.01
```

#### T29.G6.10 - Input validation
```
ID: T29.G6.10
Skill: Validate text input and handle errors
Description: Students validate text input before processing (check
for empty strings, unexpected formats). They use conditionals to
provide helpful error messages and default values.
Dependencies: T29.G6.01, T08.G5.01
```

---

### 9. ADD TEXT PROCESSING SKILLS

#### T29.G5.10 - Tokenization concepts
```
ID: T29.G5.10
Skill: Understand tokenization concepts
Description: Students learn that AI models break text into tokens
(not always whole words). They experiment with examples showing how
'running' might be 1 token but 'ChatGPT' might be 2 tokens. They
discuss why token limits exist.
Dependencies: T29.G4.04
```

#### T29.G5.11 - Text normalization pipelines
```
ID: T29.G5.11
Skill: Design text normalization pipelines
Description: Students design multi-step text cleaning pipelines
(e.g., trim → lowercase → remove punctuation → split) and test
different orderings to see which works best.
Dependencies: T29.G4.06, T29.G5.07
```

#### T29.G5.12 - Multiline text processing
```
ID: T29.G5.12
Skill: Process multiline text (split by line breaks)
Description: Students split multiline text using '\\n' as separator,
process each line separately, and rejoin. They handle edge cases
like empty lines and trailing newlines.
Dependencies: T29.G4.01
```

---

### 10. MOVE SKILLS BETWEEN GRADES

**FROM G4 TO G5**:
- T29.G4.08 → T29.G5.08.01 + T29.G5.08.02 (word frequency)
- T29.G4.09 → T29.G5.09 (highlight keywords)

**FROM G7 TO G8**:
- T29.G7.02 → T29.G8.07 (ML feature engineering)
  - Reason: Violates X-2 rule (depends on T22.G6.01)

**FROM G6 TO G8**:
- T29.G6.05 → T29.G8.05 (regex)
  - Reason: Too advanced for G6

---

## LOW-PRIORITY ENHANCEMENTS

### 11. ADD ADVANCED/OPTIONAL SKILLS

#### T29.G7.07 - Text encoding (OPTIONAL)
```
ID: T29.G7.07
Skill: Understand text encoding (ASCII, Unicode, UTF-8)
Description: Students learn that computers store text as numbers.
They explore ASCII codes, Unicode ranges, and discuss why emojis
and international characters need special encoding.
Dependencies: T29.G6.01
```

#### T29.G7.08 - Compare manual vs AI sentiment
```
ID: T29.G7.08
Skill: Compare manual vs AI sentiment analysis
Description: Students compare their manual word-list sentiment scores
with AI-generated sentiment (using ChatGPT or other NLP APIs). They
discuss differences, noting where AI handles context better and where
it fails.
Dependencies: T29.G5.04.02, T29.G7.02
```

#### T29.G7.09 - Multilingual text (OPTIONAL)
```
ID: T29.G7.09
Skill: Work with multilingual text
Description: Students experiment with text processing in different
languages (Spanish, Chinese, etc.). They note which operations work
universally (length, split) and which are language-specific
(sentiment, parts of speech).
Dependencies: T29.G6.06, T29.G6.07
```

#### T29.G8.06 - Capstone project (OPTIONAL)
```
ID: T29.G8.06
Skill: Build text-based application (chatbot, quiz generator, or
story analyzer)
Description: Students design and build a text-based application that
integrates at least 5 text processing techniques (e.g., input
validation, text cleaning, keyword extraction, AI generation, logging).
Dependencies: T29.G8.01, T29.G8.03
```

---

## DESCRIPTION CLARIFICATIONS

### T29.G3.03 - Make coding explicit
**Current**: "Group words by category (emotion, action, place)"
**Better**: "Build automated word categorizer using conditionals and lists"
**Why**: Distinguishes from unplugged G1.03

---

### T29.G5.06 - Match block name
**Current**: "Use the analyze sentence block..."
**Better**: "Use the parse sentence block (ai_parsesentence)..."
**Why**: Matches actual block ID

---

### T29.G6.08 - Clarify implementation
**Current**: "Students use text comparison blocks to compute edit distance"
**Better**: "Students use the text similarity block (operator_stringdiff)
to compute edit distance (how many character changes needed to transform
one text into another), understanding text similarity metrics."
**Why**: Specifies which block to use

---

### T29.G8.01 - Make pipeline specific
**Current**: "Build end-to-end text-processing pipelines"
**Better**: "Build a multi-stage text processing pipeline with at least
5 stages: input → clean (trim, lowercase, remove punctuation) → tokenize
(split) → filter (remove stop-words) → analyze (sentiment OR frequency)
→ output (display OR log to table). Students document each stage."
**Why**: Gives clear success criteria

---

## DEPENDENCY FIXES

### Add Missing Dependencies
- T29.G8.01: Add dependency on T07.G6.01 or T07.G7.01 (custom blocks)

### Remove Unnecessary Dependencies
- T29.G7.04: Remove dependency on T29.G6.03 (autocomplete - unrelated)

### Fix Ordering Dependencies
- Move T29.G4.06.01 BEFORE T29.G4.05 (case conversion before case-insensitive)

---

## SKILL COUNT SUMMARY

**Current**: 56 skills (K: 3, G1: 4, G2: 4, G3: 4, G4: 9, G5: 7, G6: 8, G7: 6, G8: 4)

**After Core Fixes**: ~70 skills
- K: 3
- G1: 4
- G2: 4
- G3: 5 (+1)
- G4: 12 (+3 new, after reordering/splitting)
- G5: 16 (+9 from splits/additions/moves)
- G6: 10 (+2)
- G7: 9 (+3, -1 removed)
- G8: 7 (+3 moved from earlier)

**With Optional**: ~78 skills

---

## IMPLEMENTATION CHECKLIST

**Phase 1 (Critical - Do First)**:
- [ ] Reorder all Grade 4 skills (new sequence above)
- [ ] Remove or replace T29.G7.06 (AI moderation)
- [ ] Move T29.G6.05 (regex) to T29.G8.05
- [ ] Split T29.G4.08 into T29.G5.08.01 + T29.G5.08.02
- [ ] Add T29.G4.00 (text I/O)
- [ ] Add T29.G3.05 (text equality)

**Phase 2 (Important - Do Next)**:
- [ ] Add T29.G4.10 (simple tables)
- [ ] Add T29.G4.11 (emotional tone)
- [ ] Split T29.G5.03 into .01 + .02
- [ ] Add T29.G5.10 (tokenization)
- [ ] Add T29.G6.09 (length limits)
- [ ] Add T29.G6.10 (error handling)
- [ ] Split T29.G7.01 into .01 + .02
- [ ] Move T29.G7.02 to T29.G8.07

**Phase 3 (Enhancements - Do Later)**:
- [ ] Add T29.G5.11 (normalization pipelines)
- [ ] Add T29.G5.12 (multiline text)
- [ ] Add T29.G7.07 (text encoding - optional)
- [ ] Add T29.G7.08 (compare sentiment - optional)
- [ ] Add T29.G7.09 (multilingual - optional)
- [ ] Add T29.G8.06 (capstone - optional)
- [ ] Update all descriptions per clarifications section

---

**END OF QUICK REFERENCE**
