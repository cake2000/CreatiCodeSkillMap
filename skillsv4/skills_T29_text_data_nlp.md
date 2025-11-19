# T29 – Text Data & NLP Foundations: G3–8 Skill List (Draft v3)

Topic reference: `T29 Text Data` in `domains_topics_overview.md`
Domain: Data & Analysis (D3) · CSTA focus: DAA‑DF, DAA‑DP, CAS‑ET (links to PRO‑PF, PRO‑DH)

Each skill below has:

- a stable **ID** (`T29.G<grade>.<nn>`),
- an IXL-style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** Text data appears in XO prompts, chat logs, knowledge bases, and accessibility features. Because string manipulation depends on **T10 Programming Data Structures**, T29 starts with **Grade 3** unplugged/conceptual work (no coding yet) and introduces block-based string/list processing beginning in **Grade 4** once students have seen variables and loops. Additional skills layer into prompting (T22/T24), RAG workflows, and AI ethics (AI4K12: human oversight, societal impact). Every coding challenge references prior list/table work from T10/T25.

---

## Grade 3 (conceptual, no coding)

### T29.G3.01 – Distinguish text data from numbers and pictures

- **Short name:** What type of information is this?
- **Description:** Students sort cards showing words, sentences, numbers, and emojis to recognize text as a specific data type.
- **Challenge format:** Concept sorting. Auto-grading checks placements and a short explanation of why one item counts as text.
- **CSTA:** E3‑DAA‑DF‑01.

### T29.G3.02 – Count word occurrences manually

- **Short name:** Use tick marks to count repeated words
- **Description:** Learners read a short paragraph and tally how many times specific words appear, building intuition for word frequency.
- **Challenge format:** Worksheet/photo upload. Auto-grading checks tallies and that counts match the passage.
- **CSTA:** E3‑DAA‑DI‑02.

### T29.G3.03 – Group words by category (emotion, action, place)

- **Short name:** Build a simple word classification key
- **Description:** Students categorize words into meaning-based groups and explain their reasoning, preparing for later metadata tagging.
- **Challenge format:** Concept drag-and-drop plus written justification. Auto-grading checks groupings reference meaning rather than spelling.
- **CSTA:** E3‑DAA‑DF‑01.

### T29.G3.04 – Explain why clean text helps AI helpers

- **Short name:** Describe messy vs clean prompts
- **Description:** Learners compare two sample prompts (typos vs clean) and discuss how clarity affects XO’s responses.
- **Challenge format:** Short writing. Auto-grading rubric checks mention of clarity and predicted AI behavior.
- **CSTA:** E3‑CAS‑ET‑02.

---

## Grade 4 *(first coding year; assumes T10 loops/lists intro)*

### T29.G4.01 – Store sentences in lists and access words

- **Short name:** Break sentences into list items
- **Description:** Students write a script that takes a sentence, splits it on spaces, and stores each word in a list, referencing T10 list basics.
- **Challenge format:** Coding. Auto-grading feeds sentences and checks list content/length.
- **CSTA:** E4‑PRO‑PF‑01, DAA‑DF.

### T29.G4.02 – Clean text: lowercase + remove punctuation

- **Short name:** Normalize strings for fair comparison
- **Description:** Learners build helper blocks that convert text to lowercase and strip punctuation before counting words.
- **Challenge format:** Coding. Auto-grading supplies messy sentences and checks normalized output.
- **CSTA:** E4‑PRO‑PF‑01.

### T29.G4.03 – Count words and report the most frequent

- **Short name:** Build a simple frequency table
- **Description:** Students iterate over the token list, keep counts in parallel lists/tables, and identify the most common word.
- **Challenge format:** Coding + explanation. Auto-grading checks counts and requires a sentence citing evidence.
- **CSTA:** E4‑DAA‑DI‑02.

### T29.G4.04 – Highlight keywords in a paragraph

- **Short name:** Mark all instances of a target word
- **Description:** Learners write code that scans a paragraph and highlights (changes color) every time a keyword appears on the stage.
- **Challenge format:** Coding + UI. Auto-grading ensures highlights align with keyword occurrences.
- **CSTA:** E4‑PRO‑PF‑01.

---

## Grade 5

### T29.G5.01 – Structure chat logs into tables

- **Short name:** Store timestamp, speaker, message
- **Description:** Students design table schemas for XO chats or multiplayer messages, ensuring each row records metadata needed for later filtering.
- **Challenge format:** Coding. Auto-grading checks columns (time, user, text, tag) exist and rows append correctly.
- **CSTA:** E5‑PRO‑DH‑02.

### T29.G5.02 – Build stop-word filters and keyword lists

- **Short name:** Ignore filler words before counting
- **Description:** Learners maintain a stop-word list and filter it out before running frequency counts to focus on meaningful words.
- **Challenge format:** Coding. Auto-grading verifies stop words are removed and resulting keyword list matches expectations.
- **CSTA:** E5‑DAA‑DI‑02.

### T29.G5.03 – Measure simple sentiment heuristics

- **Short name:** Count positive vs negative tokens
- **Description:** Students store positive/negative word lists and score sentences accordingly, noting in a reflection that the heuristic has limits.
- **Challenge format:** Coding + reflection. Auto-grading checks scoring and requires mention of at least one limitation.
- **CSTA:** E5‑DAA‑DI‑02, CAS‑ET‑05.

### T29.G5.04 – Map story descriptions into AI prompt slots

- **Short name:** Extract subject/style/mood from text
- **Description:** Learners highlight parts of a description needed for T21/T24 prompts (subject, color palette, mood) and populate a structured form.
- **Challenge format:** Concept + structured response. Auto-grading checks slots reference actual words from the passage.
- **CSTA:** E5‑PRO‑PM‑04.

---

## Grade 6

### T29.G6.01 – Explain characters vs words vs tokens

- **Short name:** Compare different length counts
- **Description:** Students count characters, words, and approximate GPT tokens for short text, discussing why counts differ and which matters for prompts.
- **Challenge format:** Concept + calculation. Auto-grading checks counts and reasoning.
- **CSTA:** MS‑DAA‑DF‑03.

### T29.G6.02 – Compute n‑gram (bigram) frequencies

- **Short name:** Track pairs of words
- **Description:** Learners loop through token lists, join consecutive words, and store counts to capture phrase patterns.
- **Challenge format:** Coding. Auto-grading feeds text and checks bigram tables.
- **CSTA:** MS‑PRO‑PF‑02.

### T29.G6.03 – Create autocomplete suggestions

- **Short name:** Predict likely next words
- **Description:** Using bigram data, students propose the top next words for a given prefix and display them via widgets.
- **Challenge format:** Coding + UI. Auto-grading types prefixes to ensure suggestions update.
- **CSTA:** MS‑PRO‑PF‑02, DAA‑DI.

### T29.G6.04 – Log XO prompts/responses with ratings

- **Short name:** Keep a prompt journal with usefulness scores
- **Description:** Learners automatically log each XO interaction (prompt, response, rating, timestamp) into a table for T24 responsible-use tracking.
- **Challenge format:** Coding + documentation. Auto-grading checks required columns and sample rows.
- **CSTA:** MS‑CAS‑ET‑06.

---

## Grade 7

### T29.G7.01 – Build keyword retrieval helpers (mini-RAG)

- **Short name:** Return best paragraph for a query
- **Description:** Students store paragraph snippets, compute keyword overlap or TF‑IDF-like scores, and return the highest-scoring snippet to answer a question.
- **Challenge format:** Coding + analysis. Auto-grading queries the system to ensure outputs cite correct paragraphs.
- **CSTA:** MS‑PRO‑DH‑04, DAA‑DP.

### T29.G7.02 – Engineer text features for classifiers

- **Short name:** Turn text into numeric vectors
- **Description:** Learners extract features (word counts, sentiment scores, length) and feed them into CreatiCode’s AI classifier blocks to label text (spam vs not, emotion categories).
- **Challenge format:** Coding. Auto-grading checks feature tables and classifier accuracy on validation samples.
- **CSTA:** MS‑DAA‑DF‑03.

### T29.G7.03 – Audit text datasets for bias and coverage

- **Short name:** Check representation in your corpus
- **Description:** Students examine corpora for demographic coverage, tone, or harmful language, documenting gaps and proposing mitigations.
- **Challenge format:** Concept + evidence. Rubric ensures they cite data stats and actionable steps.
- **CSTA:** MS‑CAS‑ET‑05.

### T29.G7.04 – Compare human vs XO summaries critically

- **Short name:** Annotate strengths/weaknesses of AI summaries
- **Description:** Learners write their own summary, compare it to XO’s output, and annotate what the AI missed or distorted.
- **Challenge format:** Concept + markup. Auto-grading checks annotated texts and reflection referencing specifics.
- **CSTA:** MS‑CAS‑ET‑06.

---

## Grade 8

### T29.G8.01 – Build end-to-end text-processing pipelines

- **Short name:** Clean → feature → analyze → store
- **Description:** Students design scripts that ingest raw text, normalize it, extract features, run analysis (sentiment or retrieval), and save results for future prompts.
- **Challenge format:** Coding. Auto-grading runs provided corpora to ensure each stage executes and persists outputs.
- **CSTA:** MS‑PRO‑PF‑02, DAA‑DP.

### T29.G8.02 – Compute evaluation metrics (precision/recall/F1)

- **Short name:** Measure classifier quality
- **Description:** Learners compare predicted vs actual labels and compute precision, recall, and F1, interpreting tradeoffs.
- **Challenge format:** Coding + math. Auto-grading checks metric calculations and analysis.
- **CSTA:** MS‑DAA‑DI‑03.

### T29.G8.03 – Integrate analytics into AI prompting

- **Short name:** Feed extracted facts into prompts
- **Description:** Students embed text analytics (top keywords, sentiment) into XO prompt templates and evaluate whether responses improve.
- **Challenge format:** Coding + reflection. Auto-grading ensures prompts include analytics output and comparisons cite concrete improvements.
- **CSTA:** MS‑PRO‑PM‑03.

### T29.G8.04 – Publish datasheets for text datasets

- **Short name:** Document source, purpose, risks
- **Description:** Learners author “datasheet” reports covering dataset source, collection process, limitations, and maintenance plans, aligning with AI transparency best practices.
- **Challenge format:** Policy writing. Rubric checks for required sections and references to their actual corpus.
- **CSTA:** MS‑CAS‑ET‑06, CAS‑HC‑02.

---
