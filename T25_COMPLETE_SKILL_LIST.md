# T25 Data Representation - Complete Skill List with Dependencies

## Legend
- ✅ = No issues
- ⚠️ = Overly broad, needs splitting
- 🔴 = Critical issue (circular dependency, major violation)
- [GX] = Dependency from Grade X

---

## KINDERGARTEN (3 skills)

### T25.GK.01 - Spot data in everyday objects ✅
**Description**: Students decide whether a card shows a picture, a word, or a numeral and explain what information it carries.
**Dependencies**: None

### T25.GK.02 - Match quantities to symbols ✅
**Description**: Students count a small set of items and choose a symbol (tally marks, dots, stickers) to represent the quantity.
**Dependencies**:
- T25.GK.01 [K]

### T25.GK.03 - Build a two-symbol legend ✅
**Description**: Given two emotions or states (happy/sad, hot/cold), students invent or select symbols to stand for each and use them to label pictures.
**Dependencies**:
- T25.GK.02 [K]

---

## GRADE 1 (3 skills)

### T25.G1.01 - Record data with tally marks ✅
**Description**: Students watch a short animation (e.g., fish swimming by) and record occurrences with tally marks, then convert the tallies to numerals.
**Dependencies**:
- T25.GK.02 [K]

### T25.G1.02 - Arrange data in picture rows and columns ✅
**Description**: Learners arrange four objects into a simple table (rows = choices, columns = counts) using pictures instead of numerals.
**Dependencies**:
- T25.G1.01 [1]

### T25.G1.03 - Describe the same fact in words and numbers ✅
**Description**: Students practice saying "There are five apples" and also representing it with the numeral "5" and the word "five".
**Dependencies**:
- T25.G1.01 [1]

---

## GRADE 2 (4 skills)

### T25.G2.01 - Choose labels for a category chart ✅
**Description**: Students study a picture-based bar chart and provide meaningful text labels (e.g., rename "Column A" to "Bananas").
**Dependencies**:
- T25.G1.02 [1]

### T25.G2.02 - Translate between timeline, table, and sentence ✅
**Description**: Learners view a three-step story and encode it as (1) timeline, (2) table, (3) sentence. Emphasis on equivalence across forms.
**Dependencies**:
- T01.G1.01 [1] (cross-topic)
- T25.G1.03 [1]

### T25.G2.03 - Pick the best representation for a question ✅
**Description**: Students match questions to the most useful representation type.
**Dependencies**:
- T25.G1.02 [1]
- T25.G2.02 [2]

### T25.G2.04 - Combine two data attributes ✅
**Description**: Learners create flashcards with two pieces of info (animal + habitat).
**Dependencies**:
- T25.G1.02 [1]

---

## GRADE 3 (11 skills)

### T25.G3.00.01 - Create and name variables in CreatiCode 🔴
**Description**: Students create variables, choose meaningful names, set values, and observe variable monitors.
**Dependencies**:
- T06.G3.01 [3] (cross-topic: green-flag scripts)
- T09.G3.01.04 [3] (cross-topic: display variable) 🔴 **CIRCULAR DEPENDENCY**

**Issue**: T09.G3.01.04 likely depends on T25.G3.00.01 - can't display variables without creating them first!

### T25.G3.00.02 - Create and name lists in CreatiCode ✅
**Description**: Students create lists, name them descriptively, add items, and display list monitors.
**Dependencies**:
- T25.G3.00.01 [3]
- T09.G3.01.04 [3] (cross-topic)

### T25.G3.01.01 - Add items to a list manually ✅
**Description**: Students build lists by manually adding items one at a time, understanding list order.
**Dependencies**:
- T25.G3.00.02 [3]

### T25.G3.01.02 - Map survey responses into list variables ✅
**Description**: Students transfer physical sticky note data into digital CreatiCode lists.
**Dependencies**:
- T25.G3.01.01 [3]
- T25.G2.01 [2]

### T25.G3.02 - Choose the right variable type ⚠️
**Description**: Students learn to choose: (1) number vs text variables, (2) boolean values, (3) single variables vs lists.
**Dependencies**:
- T25.G3.01.02 [3]
- T09.G3.01.04 [3] (cross-topic)
- T08.G3.02 [3] (cross-topic: if blocks)

**Issue**: Covers 3 distinct concepts - should be 3 separate skills

### T25.G3.03 - Break sentences into structured records ✅
**Description**: Students read sentences and fill tables with fields (character, action, quantity, target).
**Dependencies**:
- T25.G3.02 [3]
- T08.G3.03 [3] (cross-topic: conditionals)

### T25.G3.04.01 - Identify inconsistent units in data ✅
**Description**: Learners examine tables mixing units (minutes/seconds) and identify inconsistencies.
**Dependencies**:
- T25.G3.03 [3]

### T25.G3.04.02 - Convert data to consistent units ✅
**Description**: Students build CreatiCode project converting mixed time formats to single unit.
**Dependencies**:
- T25.G3.04.01 [3]
- T09.G3.02 [3] (cross-topic: variables in conditionals)

### T25.G3.05 - Identify when data needs cleaning ✅
**Description**: Students examine lists with inconsistent data and mark entries needing fixing.
**Dependencies**:
- T25.G3.03 [3]
- T25.G3.04.01 [3]

### T25.G3.06.01 - Create a simple table in CreatiCode ✅
**Description**: Students create two-column tables, add rows, and display tables.
**Dependencies**:
- T25.G3.02 [3]
- T25.G2.04 [2]

### T25.G3.06.02 - Access table items by row and column ✅
**Description**: Students retrieve specific values from tables using row/column blocks.
**Dependencies**:
- T25.G3.06.01 [3]
- T10.G3.01 [3] (cross-topic: loops)

---

## GRADE 4 (6 skills)

### T25.G4.01 - Build schema diagrams for simple apps ✅
**Description**: Students diagram app data needs showing column names and types before coding.
**Dependencies**:
- T25.G3.02 [3]
- T25.G2.04 [2]

### T25.G4.02 - Encode the same fact in decimal, fraction, and percentage ✅
**Description**: Students represent same numerical fact in three formats using CreatiCode.
**Dependencies**:
- T25.G3.01.02 [3]
- T25.G2.02 [2]

### T25.G4.03 - Compare dense vs sparse representations ⚠️
**Description**: Students compare dense (all values) vs sparse (non-empty only) and implement both in CreatiCode.
**Dependencies**:
- T25.G3.02 [3]
- T25.G2.03 [2]

**Issue**: Requires both understanding AND implementing both approaches - too much for one skill

### T25.G4.04 - Document special rules in a data key ✅
**Description**: Learners create legend for mini-map with exceptions documented.
**Dependencies**:
- T25.G3.02 [3]
- T25.G2.01 [2]

### T25.G4.05 - Distinguish between raw data and computed values ✅
**Description**: Students identify stored values vs computed values in game scoreboard.
**Dependencies**:
- T25.G3.02 [3]
- T25.G4.01 [4]

### T25.G4.06 - Populate tables from list data ✅
**Description**: Students loop through lists and build tables from list data.
**Dependencies**:
- T25.G3.06.01 [3]
- T10.G3.01 [3] (cross-topic: loops)

---

## GRADE 5 (10 skills)

### T25.G5.01.01 - Design multi-type data structures on paper ✅
**Description**: Students design "player" data structure showing different data types on paper.
**Dependencies**:
- T25.G3.02 [3]
- T25.G4.01 [4]

### T25.G5.01.02 - Implement multi-type game state in CreatiCode ⚠️
**Description**: Students implement player data using variables AND lists with coordinated updates.
**Dependencies**:
- T25.G5.01.01 [5]
- T09.G3.01.04 [3] (cross-topic)

**Issue**: Combines multiple variable types, lists, AND coordinated updates - 3+ concepts

### T25.G5.02.01 - Normalize text input using join and replace ✅
**Description**: Students use text operations to standardize inconsistent inputs.
**Dependencies**:
- T25.G3.01.02 [3]
- T25.G3.04.02 [3]

### T25.G5.02.02 - Build a data validation and cleaning project ⚠️
**Description**: Students build complete survey normalization with multiple cleaning techniques, validation, and storage.
**Dependencies**:
- T25.G5.02.01 [5]
- T25.G3.05 [3]

**Issue**: Full project combining multiple techniques - should be 4-5 separate skills

### T25.G5.03 - Decide when to upgrade from list to table ✅
**Description**: Students examine scenarios and decide between lists vs tables.
**Dependencies**:
- T25.G3.01.02 [3]
- T25.G4.03 [4]

### T25.G5.04 - Encode categorical values with numeric codes ✅
**Description**: Students map categorical text to numeric codes with legend.
**Dependencies**:
- T25.G4.04 [4]
- T25.G3.02 [3]

### T25.G5.05 - Add meaningful default values to data fields ✅
**Description**: Students design profiles with appropriate default values for empty fields.
**Dependencies**:
- T25.G4.01 [4]
- T25.G3.02 [3]

### T25.G5.06.01 - Create multi-column tables with varied data ✅
**Description**: Students build 3+ column tables with different column types.
**Dependencies**:
- T25.G3.06.02 [3]
- T25.G5.03 [5]

### T25.G5.06.02 - Query tables by value ✅
**Description**: Students search tables to find specific rows by value.
**Dependencies**:
- T25.G5.06.01 [5]

### T25.G5.06.03 - Filter and delete table rows ✅
**Description**: Students remove rows from tables using delete blocks.
**Dependencies**:
- T25.G5.06.02 [5]

### T25.G5.07 - Validate data types and ranges before storage ✅
**Description**: Students write validation scripts checking user input before storing.
**Dependencies**:
- T25.G3.02 [3]
- T08.G4.01 [4] (cross-topic: if/else)

---

## GRADE 6 (12 skills)

### T25.G6.01 - Document metadata for datasets ⚠️
**Description**: Students create metadata tables with FieldName, Description, DataType, Units, ValidRange columns.
**Dependencies**:
- T25.G5.01.01 [5]
- T25.G4.04 [4] ⚠️ **X-2 borderline**
- T25.G4.01 [4] ⚠️ **X-2 borderline**

**Issue**: 5 different column types - too complex for single skill

### T25.G6.02 - Explain lossy vs lossless representation ⚠️
**Description**: Students compare lossless (every frame) vs lossy (key checkpoints) and implement both.
**Dependencies**:
- T25.G5.03 [5]
- T25.G4.03 [4] ⚠️ **X-2 borderline**

**Issue**: Conceptual understanding + 2 implementations + tradeoff analysis - too much

### T25.G6.03 - Nest tables and lists within each other ⚠️
**Description**: Students design and implement nested data structures (tables with list columns).
**Dependencies**:
- T25.G5.01.02 [5]
- T25.G5.03 [5]

**Issue**: Design + implementation + accessing nested data - 3 concepts

### T25.G6.04 - Trace AI prompt inputs to structured slots ✅
**Description**: Students map variables to template placeholders for AI prompts.
**Dependencies**:
- T25.G5.04 [5]
- T25.G5.02.02 [5]

### T25.G6.05.01 - Search and filter table data with conditions ⚠️
**Description**: Students find rows matching conditions, collect to new list, display results.
**Dependencies**:
- T25.G5.06.03 [5]
- T25.G4.06 [4]

**Issue**: Finding + collecting + displaying - multiple operations

### T25.G6.05.02 - Aggregate table data using built-in blocks ✅
**Description**: Students use sum/average/median/max/min blocks on table columns.
**Dependencies**:
- T25.G6.05.01 [6]

### T25.G6.05.03 - Sort table data by column ✅
**Description**: Students sort tables by different columns in ascending/descending order.
**Dependencies**:
- T25.G6.05.01 [6]

### T25.G6.06.01 - Save data to server storage ✅
**Description**: Students save individual values using server storage blocks.
**Dependencies**:
- T25.G5.01.02 [5]

### T25.G6.06.02 - Load data from server storage ✅
**Description**: Students retrieve saved data and handle missing data cases.
**Dependencies**:
- T25.G6.06.01 [6]

### T25.G6.07.01 - Export table data as CSV ✅
**Description**: Students export tables to CSV and examine raw file format.
**Dependencies**:
- T25.G5.06.01 [5]

### T25.G6.07.02 - Import CSV data into tables ✅
**Description**: Students import CSV files into CreatiCode tables.
**Dependencies**:
- T25.G6.07.01 [6]

### T25.G6.07.03 - Debug and verify imported table structure ⚠️
**Description**: Students debug and fix common CSV import problems.
**Dependencies**:
- T25.G6.07.02 [6]

**Issue**: Debugging + verification + fixing - should be 2 skills

---

## GRADE 7 (10 skills)

### T25.G7.01 - Normalize repeating data into separate tables ⚠️
**Description**: Students examine redundancy, design normalized schema, implement two linked tables, and query across them.
**Dependencies**:
- T25.G5.01.02 [5] ⚠️ **X-2 borderline**
- T25.G5.03 [5] ⚠️ **X-2 borderline**
- T25.G6.03 [6]

**Issue**: Database normalization is complex - 4+ concepts (identify, design, implement, query)

### T25.G7.02 - Identify bias introduced by representation choices ✅
**Description**: Students critique schemas that collapse categories and redesign to better represent all groups.
**Dependencies**:
- T25.G5.01.02 [5]
- T25.G5.04 [5]
- T25.G6.01 [6]

### T25.G7.03.01 - Save tables using CSV and server storage ✅
**Description**: Students export table to CSV, then save CSV text using server storage.
**Dependencies**:
- T25.G6.07.02 [6]
- T25.G6.06.02 [6]

### T25.G7.03.02 - Restore tables from CSV and server storage ✅
**Description**: Students load CSV from server storage and import into table.
**Dependencies**:
- T25.G7.03.01 [7]

### T25.G7.03.03 - Use direct table storage methods ✅
**Description**: Students use built-in table save/load blocks for direct persistence.
**Dependencies**:
- T25.G6.03 [6]
- T25.G6.06.02 [6]

### T25.G7.04 - Evaluate storage vs performance tradeoffs ⚠️
**Description**: Students build two versions (pre-calculated vs computed) and compare tradeoffs.
**Dependencies**:
- T25.G5.01.02 [5] ⚠️ **X-2 borderline**
- T25.G6.01 [6]
- T25.G6.02 [6]

**Issue**: Building 2 implementations + comparison - should be 3 skills

### T25.G7.05.01 - Fetch data from database collections ✅
**Description**: Students fetch all documents from shared multi-user collections.
**Dependencies**:
- T25.G6.05.01 [6]
- T25.G6.06.02 [6]

### T25.G7.05.02 - Query database collections with conditions ✅
**Description**: Students fetch filtered data using query conditions.
**Dependencies**:
- T25.G7.05.01 [7]

### T25.G7.05.03 - Update and delete collection documents ✅
**Description**: Students modify shared database collections.
**Dependencies**:
- T25.G7.05.02 [7]

### T25.G7.06.01 - Set up Google Sheets integration ✅
**Description**: Students connect CreatiCode to Google Sheets.
**Dependencies**:
- T25.G6.05.01 [6]

### T25.G7.06.02 - Read and write Google Sheets data ✅
**Description**: Students import from and export to Google Sheets.
**Dependencies**:
- T25.G7.06.01 [7]

### T25.G7.06.03 - Append and modify Google Sheets rows ✅
**Description**: Students add rows and update cells in Google Sheets.
**Dependencies**:
- T25.G7.06.02 [7]

---

## GRADE 8 (4 skills)

### T25.G8.01 - Design schemas for multi-modal apps ⚠️🔴
**Description**: Students design data for apps combining vision AI + audio AI + conversation history with relationships.
**Dependencies**:
- T06.G6.01 [6] ⚠️ **X-2 borderline** (cross-topic)
- T25.G6.01 [6] ⚠️ **X-2 borderline**
- T25.G6.03 [6] ⚠️ **X-2 borderline**
- T25.G7.01 [7]

**Issue**: EXTREMELY BROAD - essentially a capstone project covering 5+ concepts

### T25.G8.02 - Document versioning and lineage metadata ✅
**Description**: Students create enhanced metadata with source, timestamp, transformation history, versions.
**Dependencies**:
- T25.G6.01 [6] ⚠️ **X-2 borderline**
- T25.G7.02 [7]

### T25.G8.03 - Evaluate compression strategies for large datasets ⚠️
**Description**: Students compare storage approaches, calculate memory usage, implement compression.
**Dependencies**:
- T06.G6.01 [6] ⚠️ **X-2 borderline** (cross-topic)
- T09.G6.01 [6] ⚠️ **X-2 borderline** (cross-topic)
- T25.G6.02 [6] ⚠️ **X-2 borderline**
- T25.G7.04 [7]

**Issue**: Multiple examples + calculations + discussion + implementation - 4+ concepts

### T25.G8.04 - Document data formats for project collaboration ⚠️
**Description**: Students create comprehensive spec for inputs, outputs, formatting rules, then implement sample project.
**Dependencies**:
- T25.G6.01 [6] ⚠️ **X-2 borderline**
- T25.G7.03.02 [7]
- T25.G7.01 [7]

**Issue**: Comprehensive documentation + implementation - should be 4 skills

---

## SUMMARY STATISTICS

**Total Skills**: 65
- Kindergarten: 3
- Grade 1: 3
- Grade 2: 4
- Grade 3: 11
- Grade 4: 6
- Grade 5: 10
- Grade 6: 12 (most skills)
- Grade 7: 10
- Grade 8: 4 (but all overly broad)

**Issues Identified**:
- ✅ No issues: 50 skills (77%)
- ⚠️ Overly broad: 15 skills (23%)
- 🔴 Critical (circular dependency): 1 skill
- X-2 borderline: 8 skills (12%)

**Cross-Topic Dependencies**:
- T01 (Sequencing): 1 dependency
- T06 (Events): 3 dependencies
- T08 (Conditionals): 4 dependencies
- T09 (Variables): 7 dependencies (includes circular)
- T10 (Loops): 3 dependencies

**Recommended Splits**:
- Priority 1 (must do): 5 skills → 20 skills
- Priority 2 (should do): 7 skills → 22 skills
- Priority 3 (nice to have): 3 skills → 8 skills
- **Total impact**: 65 current → 95-100 after splits

