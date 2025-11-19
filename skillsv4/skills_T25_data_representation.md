# T25 – Data Representation: K–8 Skill List (Draft v2)

Topic reference: `T25 Data Representation` in `domains_topics_overview.md`
Domain: Data & Analysis (D3) · CSTA focus: DAA‑DF, PRO‑DH (links to DAA‑DP, DAA‑DI)

Each skill below has:

- a stable **ID** (`T25.G<grade>.<nn>`),
- an IXL-style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Role and scope in v3:** T25 explains the *shape* of information that powers CreatiCode projects and is the central home for data representation concepts. It begins in Kindergarten with picture-based experiences (no code) that help students see numbers, words, and symbols as interchangeable representations of the same facts. Grades 3–5 translate those intuitions into concrete program structures (variables, lists, tables). Grades 6–8 reason about schema design, metadata, nested structures, and how representation choices influence AI systems (bias, compression, interpretability). T25 feeds directly into **T26 Data Collection** (how we gather information) and **T27 Data Analysis** (how we interrogate it). Programming topics (T07–T10) and AI topics (T21–T24) should depend on T25 skills rather than re-teaching representation concepts. This topic owns all teaching about data schemas, types, formats, and structure design.

---

## Grade K (PreK–K)

### T25.GK.01 – Spot data in everyday objects

- **Short name:** Picture, word, or number?
- **Description:** Students decide whether a card shows a picture, a word, or a numeral and explain what information it carries. This builds foundational awareness that data can appear in multiple forms.
- **Challenge format:** Concept, drag-and-drop sorting. Learners drag cards (🐱, “cat,” 3) into labeled bins. Auto-grading checks placements and asks a follow-up (“What does the numeral tell us?”).
- **CSTA:** EK‑DAA‑DF‑01.

### T25.GK.02 – Match quantities to symbols

_Dependency:_
  * T03.GK.01: Identify parts that make up a whole


- **Short name:** Use icons to represent “how many”
- **Description:** Students count a small set of items and choose a symbol (tally marks, dots, stickers) to represent the quantity, reinforcing that symbols can encode counts.
- **Challenge format:** Interactive counting. Learners tap items to count, then pick a symbol card (e.g., 🔟, |||) that matches the count. Auto-grading compares the symbol to the actual quantity.
- **CSTA:** EK‑PRO‑DH‑03.

### T25.GK.03 – Build a two-symbol legend

_Dependency:_
  * T01.GK.01: Put pictures in order for getting ready for bed


- **Short name:** Create a tiny data key
- **Description:** Given two emotions or states (happy/sad, hot/cold), students invent or select symbols to stand for each and use them to label pictures. This sets up later ideas about legends in charts.
- **Challenge format:** Concept. Learners choose icons for each category, then tag photos accordingly. Auto-grading verifies consistent use of the legend.
- **CSTA:** EK‑DAA‑DF‑01.

---

## Grade 1

### T25.G1.01 – Record data with tally marks

_Dependency:_
  * T01.GK.01: Put pictures in order for getting ready for bed


- **Short name:** Tally and translate to numbers
- **Description:** Students watch a short animation (e.g., fish swimming by) and record occurrences with tally marks, then convert the tallies to numerals.
- **Challenge format:** Interactive tally tool. Auto-grading checks tally accuracy and the final numeric translation.
- **CSTA:** E1‑DAA‑DF‑01.

### T25.G1.02 – Design a picture table

_Dependency:_
  * T01.GK.01: Put pictures in order for getting ready for bed


- **Short name:** Use a 2×2 picture table
- **Description:** Learners arrange four objects into a simple table (rows = choices, columns = counts) using pictures instead of numerals, showing that tables are structured representations.
- **Challenge format:** Concept + manipulatives. Students drag icons into a blank table template. Auto-grading ensures each row/column is labeled and filled.
- **CSTA:** E1‑DAA‑DF‑01.

### T25.G1.03 – Describe the same fact in words and numbers

_Dependency:_
  * T01.GK.01: Put pictures in order for getting ready for bed


- **Short name:** Switch between word and number data
- **Description:** Students practice saying “There are five apples” and also representing it with the numeral “5” and the word “five,” highlighting multi-format representation.
- **Challenge format:** Fill-in-the-blank sentences paired with selecting numerals. Auto-grading checks both entries.
- **CSTA:** E1‑DAA‑DF‑01.

---

## Grade 2

### T25.G2.01 – Choose labels for a category chart

_Dependency:_
  * T01.G1.10: Match pictures to "if/then" rules


- **Short name:** Name the columns correctly
- **Description:** Students study a picture-based bar chart and provide meaningful text labels (e.g., rename “Column A” to “Bananas”). This underscores the importance of descriptive labels.
- **Challenge format:** Concept, short-answer. Auto-grading checks labels against provided category descriptions.
- **CSTA:** E2‑DAA‑DF‑01.

### T25.G2.02 – Translate between timeline, table, and sentence

_Dependency:_
  * T01.G1.01: Put pictures in order to plant a seed
  * T01.GK.08: Count how many times


- **Short name:** Represent events three ways
- **Description:** Learners view a three-step story (wake up → eat breakfast → go to school) and encode it as (1) a timeline drawing, (2) a table with time + action, and (3) a narrative sentence. Emphasis is on seeing equivalence across forms.
- **Challenge format:** Guided worksheet. Auto-grading checks each representation for correct sequence.
- **CSTA:** E2‑DAA‑DF‑01.

### T25.G2.03 – Pick the best representation for a question

_Dependency:_
  * T01.GK.08: Count how many times


- **Short name:** Picture, list, or number line?
- **Description:** Students match questions (“How many stickers?” “Which order do things happen?”) to the most useful representation type, building judgement about data tools.
- **Challenge format:** Matching cards. Auto-grading checks pairings and requires justification sentences.
- **CSTA:** E2‑DAA‑DI‑02.

### T25.G2.04 – Combine two data attributes

_Dependency:_
  * T01.G1.01: Put pictures in order to plant a seed
  * T01.GK.08: Count how many times


- **Short name:** Make a two-column card
- **Description:** Learners create flashcards with two pieces of info (animal + habitat) to see how pairing attributes forms richer records.
- **Challenge format:** Concept. Students fill a template: Column 1 (animal), Column 2 (home). Auto-grading ensures consistent pairing and labels.
- **CSTA:** E2‑DAA‑DF‑01.

---

## Grade 3

### T25.G3.01 – Map survey responses into list variables

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T25.G2.01: Choose labels for a category chart


- **Short name:** Store answers as list items
- **Description:** Students take physical sticky notes and type each response as an item in a list, demonstrating how analog data becomes digital.
- **Challenge format:** Coding exercise. Auto-grading checks that the list contains all responses and preserves order.
- **CSTA:** E3‑PRO‑DH‑02.
- **Editor notes:** Builds on T26 survey collection methods; connects to T10 list basics.

### T25.G3.02 – Choose the right variable type

_Dependency:_
  * T25.G3.01: Map survey responses into list variables
  * T09.G3.01: Create and use a numeric variable for score or count
  * T08.G3.02: Decide when a single if is enough


- **Short name:** Number vs text vs Boolean
- **Description:** Learners receive mini-scenarios (store score, store player name, store didWin?) and match them to variable types, reinforcing type selection.
- **Challenge format:** Multiple choice + explanation. Auto-grading checks answers and short reasoning.
- **CSTA:** E3‑PRO‑DH‑02.

### T25.G3.03 – Break sentences into structured records

_Dependency:_
  * T25.G3.02: Choose the right variable type
  * T08.G3.03: Pick the right conditional block for a scenario
  * T10.G3.01: Loop through and process each item in a list


- **Short name:** Parse story sentences into fields
- **Description:** Students read sentences (“Luna fed 4 fish to the seal”) and fill a table with fields (character, action, quantity, target). This links narrative data to structured formats.
- **Challenge format:** Concept worksheet. Auto-grading verifies fields are filled with correct tokens.
- **CSTA:** E3‑DAA‑DF‑01.

### T25.G3.04 – Explain why consistent units matter

_Dependency:_
  * T25.G3.03: Break sentences into structured records
  * T09.G3.02: Use a variable in a conditional (if block)
  * T07.G3.03: Build a forever loop for simple animation


- **Short name:** Keep units aligned
- **Description:** Learners examine a table mixing minutes and seconds, identify the issue, and normalize it (convert to one unit), emphasizing representation integrity.
- **Challenge format:** Concept editing. Auto-grading checks for corrected values and justification text.
- **CSTA:** E3‑DAA‑DF‑01.

---

## Grade 4

### T25.G4.01 – Build schema diagrams for simple apps

_Dependency:_
  * T02.G3.01: Identify start, action, and end symbols
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Sketch what data tables need
- **Description:** Students diagram an app’s data needs (e.g., to-do list: task text, due date, done?) showing column names and types before coding.
- **Challenge format:** Concept + drawing. Auto-grading reviews submitted diagrams via checklist (all required fields included, data types labeled).
- **CSTA:** E4‑DAA‑DF‑01, E4‑ALG‑HD‑01.

### T25.G4.02 – Encode the same fact in decimal, fraction, and percentage

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Represent parts of a whole three ways
- **Description:** Learners convert a simple measurement (half of a pizza) into decimal (0.5), fraction (1/2), and percent (50%), emphasizing equivalent numeric representations.
- **Challenge format:** Conversion problems. Auto-grading checks equivalence.
- **CSTA:** E4‑DAA‑DF‑01.

### T25.G4.03 – Compare dense vs sparse representations

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** When to use lists vs paired lists
- **Description:** Students analyze two data representations (list of coordinates vs list of only non-empty squares) and decide which is better for specific tasks (drawing, storage efficiency).
- **Challenge format:** Concept analysis. Auto-grading expects a selected option plus reasoning referencing storage or readability.
- **CSTA:** E4‑DAA‑DF‑01.

### T25.G4.04 – Document assumptions in a data key

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Write a legend and note exceptions
- **Description:** Learners create a legend for a mini-map (color = terrain) and add a note describing exceptions (e.g., “Purple = portal unless near volcano”). This highlights metadata importance.
- **Challenge format:** Concept writing. Auto-grading checks for legend completeness and exception description.
- **CSTA:** E4‑PRO‑PM‑05.

---

## Grade 5

### T25.G5.01 – Model multi-type game state

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T25.G1.01: Record data with tally marks
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Design a full player record
- **Description:** Students design a “player” data structure using text, number, Boolean, and list fields, matching CreatiCode variable/list/table options.
- **Challenge format:** Coding + documentation. Auto-grading verifies variables/lists exist with correct initial values.
- **CSTA:** E5‑PRO‑DH‑02.

### T25.G5.02 – Convert messy inputs into canonical formats

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T25.G1.01: Record data with tally marks
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Clean capitalization and spacing
- **Description:** Learners write small scripts (or pseudo-code) to normalize name inputs (trim spaces, capitalize first letter) so data is consistent for later analysis.
- **Challenge format:** Coding. Auto-grading feeds sample inputs and checks normalized outputs.
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DF.

### T25.G5.03 – Decide when to upgrade from list to table

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.G1.02: Design a picture table
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Compare single vs multi-column storage
- **Description:** Students examine a list of names and a table with names + scores, then choose which representation fits new requirements (“store both name and score”).
- **Challenge format:** Concept multiple choice plus justification. Auto-grading checks reasoning referencing columns/fields.
- **CSTA:** E5‑DAA‑DF‑01.

### T25.G5.04 – Encode categorical values with symbols or enums

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Replace text labels with codes
- **Description:** Learners map repeated string values (difficulty Easy/Medium/Hard) to symbolic codes (E/M/H) and explain how a legend keeps them readable.
- **Challenge format:** Concept + legend design. Auto-grading checks mapping completeness and legend clarity.
- **CSTA:** E5‑PRO‑DH‑02.

---

## Grade 6

### T25.G6.01 – Document metadata for datasets

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T25.G1.01: Record data with tally marks
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Fill a data dictionary
- **Description:** Students complete metadata tables (field name, description, type, units, valid range) for a project dataset, ensuring future teammates understand the schema.
- **Challenge format:** Documentation task. Auto-grading verifies every column has descriptions, units, and ranges.
- **CSTA:** MS‑DAA‑DF‑03.

### T25.G6.02 – Explain lossy vs lossless representation

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.G1.02: Design a picture table
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Decide when simplification loses detail
- **Description:** Learners compare representing a path as every coordinate (lossless) vs key checkpoints (lossy) and discuss tradeoffs.
- **Challenge format:** Concept analysis. Auto-grading checks that students identify which representation loses detail and cite a consequence.
- **CSTA:** MS‑DAA‑DF‑03.

### T25.G6.03 – Nest structures (list of records, record of lists)

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T25.G1.01: Record data with tally marks
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Build nested data for inventory
- **Description:** Students design data that contains a list within a record (player inventory with multiple items) or records within a list (NPC roster) and explain access patterns.
- **Challenge format:** Coding + explanation. Auto-grading checks data initialization and requires a short description of how to read/write nested parts.
- **CSTA:** MS‑PRO‑DH‑04.

### T25.G6.04 – Trace AI prompt inputs to structured slots

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.G1.02: Design a picture table
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Map prompt text to data fields
- **Description:** Learners examine an AI prompt template ("Write a summary about {topic} in {tone}") and identify which fields store each slot's values.
- **Challenge format:** Concept. Auto-grading checks field assignments and a reflection on why structured slots help reuse prompts.
- **CSTA:** MS‑PRO‑PM‑03.
- **Editor notes:** Links to XO/T22 prompts and structured data models; foundation for AI prompt engineering.

---

## Grade 7

### T25.G7.01 – Normalize repeating data into separate tables

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.G1.02: Design a picture table
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Split one table into two linked tables
- **Description:** Students examine a table with repeated player info per score entry and refactor it into two tables (Players, Scores) with IDs, emphasizing normalization.
- **Challenge format:** Concept + table editing. Auto-grading validates correct column choices and foreign key references.
- **CSTA:** MS‑DAA‑DF‑03, MS‑PRO‑DH‑04.

### T25.G7.02 – Identify bias introduced by representation choices

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.G1.02: Design a picture table
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Does encoding hide important detail?
- **Description:** Learners critique data schemas that collapse categories (e.g., “Other” gender) and discuss the downstream impact for AI fairness.
- **Challenge format:** Concept + reflection. Auto-grading checks for explicit identification of missing detail and a proposed improvement (add category, collect text comments).
- **CSTA:** MS‑CAS‑ET‑05.

### T25.G7.03 – Create JSON-like snippets to store structured state

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Represent UI state as key/value pairs
- **Description:** Students practice expressing a CreatiCode screen’s data as nested key/value text (pseudo-JSON) and aligning it with program variables.
- **Challenge format:** Concept + coding. Auto-grading checks syntax (matching braces) and alignment with UI elements.
- **CSTA:** MS‑PRO‑DH‑04.

### T25.G7.04 – Evaluate storage vs performance tradeoffs

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.G1.02: Design a picture table
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Choose between precomputed and computed fields
- **Description:** Learners consider whether to store derived values (e.g., total score) or compute them on demand, documenting pros/cons (speed, accuracy).
- **Challenge format:** Concept analysis. Auto-grading requires a decision plus supporting evidence tied to scenario constraints.
- **CSTA:** MS‑PRO‑PM‑03.

---

## Grade 8

### T25.G8.01 – Design schemas for multi-modal apps

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T25.G1.01: Record data with tally marks
  * T25.G1.02: Design a picture table
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Plan data for voice/vision/AI features
- **Description:** Students outline data structures that hold transcripts, detected poses, and AI prompts for multi-modal CreatiCode projects (linking to T23/T24). They document relationships and storage formats.
- **Challenge format:** Concept + diagram. Auto-grading checks that each modality has fields, data types, and cross-links.
- **CSTA:** MS‑DAA‑DF‑03, MS‑CAS‑ET‑07.

### T25.G8.02 – Document versioning and lineage metadata

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.G1.02: Design a picture table
  * T25.G1.03: Describe the same fact in words and numbers
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Track where data originated
- **Description:** Learners add fields for source, timestamp, and transformation notes to a dataset, explaining why lineage matters for audits and AI ethics.
- **Challenge format:** Documentation. Auto-grading ensures every record includes lineage entries and reflection ties to AI4K12 priorities (transparency, human oversight).
- **CSTA:** MS‑CAS‑ET‑06.

### T25.G8.03 – Evaluate compression strategies for large datasets

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T25.G1.01: Record data with tally marks
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Compare binary vs textual storage
- **Description:** Students investigate storing sprite paths as raw coordinate lists vs run-length encoded segments, discussing memory usage and lossiness.
- **Challenge format:** Concept + calculation. Auto-grading checks simple size estimates and identification of tradeoffs.
- **CSTA:** MS‑DAA‑DF‑03.

### T25.G8.04 – Create data interface contracts for teammates

_Dependency:_
  * T25.G1.01: Record data with tally marks
  * T25.G1.02: Design a picture table
  * T25.G1.03: Describe the same fact in words and numbers
  * T25.GK.02: Match quantities to symbols
  * T25.GK.03: Build a two-symbol legend


- **Short name:** Write API-style data agreements
- **Description:** Learners draft a short contract describing what data format their module consumes/produces (field names, types, optional values) so other students can integrate seamlessly.
- **Challenge format:** Documentation + peer review. Auto-grading checks for required sections (input schema, output schema, validation rules).
- **CSTA:** MS‑PRO‑PM‑03, MS‑PRO‑PD‑08.

---
