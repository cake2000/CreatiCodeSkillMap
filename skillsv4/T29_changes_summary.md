# T29 Topic Update Summary

## Changes Applied to skillsv4/allskills.md

### 1. Added 3 New Skills

#### T29.G4.01b: Access individual characters in text by position
- **Location:** Inserted after T29.G4.01 (line 13804)
- **Description:** Access and display specific characters from text using their position (index), understanding that positions start at 1
- **Dependencies:**
  - T29.G4.01: Compare a human summary to a computer summary
  - T07.G3.03: Trace code with simple loops to predict outcomes

#### T29.G4.02b: Count characters and words in text
- **Location:** Inserted after T29.G4.02 (line 13827)
- **Description:** Use length of text block to count characters, and count words by splitting text on spaces
- **Dependencies:**
  - T29.G4.02: Use split and join blocks for text manipulation
  - T07.G3.03: Trace code with simple loops to predict outcomes

#### T29.G5.01b: Create and populate data tables from text
- **Location:** Inserted after T29.G5.01 (line 13887)
- **Description:** Create tables with rows and columns from text data, using split operations to organize information
- **Dependencies:**
  - T29.G5.01: Structure chat logs into tables
  - T08.G4.02: Write scripts combining sequencing, loops, and conditionals

### 2. Added Loop Dependencies (T07.G3.03) to 3 Skills

#### T29.G4.03: Clean text: lowercase + remove punctuation
- **Added dependency:** T07.G3.03: Trace code with simple loops to predict outcomes
- **Reason:** Requires character-by-character iteration

#### T29.G4.04: Count words and report the most frequent
- **Added dependency:** T07.G3.03: Trace code with simple loops to predict outcomes
- **Reason:** Requires iteration over word list

#### T29.G4.05: Highlight keywords in a paragraph
- **Added dependency:** T07.G3.03: Trace code with simple loops to predict outcomes
- **Reason:** Requires scanning through text

### 3. Updated Skill Descriptions (3 skills)

#### T29.G4.01: Compare a human summary to a computer summary
- **Old:** Students read a short paragraph, write a one-sentence summary, and then compare it to a computer-generated summary, noting what the computer included or missed.
- **New:** Use AI (ChatGPT) to generate summaries of text content, understanding how AI can condense information
- **Reason:** Clarifies that AI (ChatGPT) is used for summary generation

#### T29.G5.04: Map story descriptions into AI prompt slots
- **Old:** Learners highlight parts of a description needed for T21/T24 prompts (subject, color palette, mood) and populate a structured form.
- **New:** Create dynamic prompts with variable slots (placeholders) that can be filled with different values to generate varied AI responses
- **Reason:** Clarifies what "prompt slots" means (variable placeholders)

#### T29.G8.01: Build end-to-end text-processing pipelines
- **Old:** Students design scripts that ingest raw text, normalize it, extract features, run analysis (sentiment or retrieval), and save results for future prompts.
- **New:** Build multi-stage text processing pipelines (e.g., input → clean → analyze → classify → output) using multiple NLP operations in sequence
- **Reason:** Makes pipeline stages explicit and clearer

### 4. Added Dependencies to Existing Skills

#### T29.G5.04: Map story descriptions into AI prompt slots
- **Added dependency:** T29.G5.03: Measure simple sentiment heuristics
- **Reason:** Was missing within-topic prerequisite

#### T29.G6.01: Explain characters vs words vs tokens
- **Added dependency:** T29.G4.02b: Count characters and words in text
- **Reason:** Needs the counting skill as foundation

## Summary Statistics

- **New skills added:** 3 (T29.G4.01b, T29.G4.02b, T29.G5.01b)
- **Skills with added loop dependencies:** 3 (T29.G4.03, T29.G4.04, T29.G4.05)
- **Skills with updated descriptions:** 3 (T29.G4.01, T29.G5.04, T29.G8.01)
- **Skills with added within-topic dependencies:** 2 (T29.G5.04, T29.G6.01)
- **Total skills modified:** 8 existing skills + 3 new skills = 11 changes
- **Total T29 skills now:** 30 (previously 27)
- **Skills by grade:** G3: 4, G4: 7, G5: 6, G6: 5, G7: 4, G8: 4

## Notes

Several changes mentioned in the original instructions were not applicable because:
- T29.G5.01 already had T29.G4.02 as a dependency (no change needed)
- T29.G5.02 did not have T11.G1.04 or T17.G4.02 dependencies to modify
- T29.G5.05 did not have T08.G1.01 dependency to change
- T29.G6.03, T29.G7.02, T29.G8.03 did not have T17 dependencies to modify

All changes that were applicable have been successfully applied to the file.
