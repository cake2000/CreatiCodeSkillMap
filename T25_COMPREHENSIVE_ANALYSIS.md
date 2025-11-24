# T25 Data Representation - Comprehensive Analysis

## Executive Summary

Topic T25 (Data Representation) contains **65 skills** across grades K-8, making it one of the largest topics in the skill map. The topic shows excellent progression from unplugged data awareness (K-2) through basic variables and lists (Grade 3) to advanced database operations and multi-modal data structures (Grades 7-8).

**Key Findings:**
- **Grade appropriateness**: Generally good, with K-2 being picture-based/unplugged and Grade 3+ involving block-based coding
- **Overly broad skills**: 15+ skills identified that need breakdown
- **Dependency issues**: Several X-2 rule violations and circular dependencies found
- **Topic coherence**: Strong overall progression with some gaps in middle grades

---

## 1. Complete List of T25 Skills by Grade

### Kindergarten (3 skills)
1. **T25.GK.01** - Spot data in everyday objects
2. **T25.GK.02** - Match quantities to symbols
3. **T25.GK.03** - Build a two-symbol legend

### Grade 1 (3 skills)
4. **T25.G1.01** - Record data with tally marks
5. **T25.G1.02** - Arrange data in picture rows and columns
6. **T25.G1.03** - Describe the same fact in words and numbers

### Grade 2 (4 skills)
7. **T25.G2.01** - Choose labels for a category chart
8. **T25.G2.02** - Translate between timeline, table, and sentence
9. **T25.G2.03** - Pick the best representation for a question
10. **T25.G2.04** - Combine two data attributes

### Grade 3 (11 skills)
11. **T25.G3.00.01** - Create and name variables in CreatiCode
12. **T25.G3.00.02** - Create and name lists in CreatiCode
13. **T25.G3.01.01** - Add items to a list manually
14. **T25.G3.01.02** - Map survey responses into list variables
15. **T25.G3.02** - Choose the right variable type ⚠️ **OVERLY BROAD**
16. **T25.G3.03** - Break sentences into structured records
17. **T25.G3.04.01** - Identify inconsistent units in data
18. **T25.G3.04.02** - Convert data to consistent units
19. **T25.G3.05** - Identify when data needs cleaning
20. **T25.G3.06.01** - Create a simple table in CreatiCode
21. **T25.G3.06.02** - Access table items by row and column

### Grade 4 (6 skills)
22. **T25.G4.01** - Build schema diagrams for simple apps
23. **T25.G4.02** - Encode the same fact in decimal, fraction, and percentage
24. **T25.G4.03** - Compare dense vs sparse representations ⚠️ **OVERLY BROAD**
25. **T25.G4.04** - Document special rules in a data key
26. **T25.G4.05** - Distinguish between raw data and computed values
27. **T25.G4.06** - Populate tables from list data

### Grade 5 (10 skills)
28. **T25.G5.01.01** - Design multi-type data structures on paper
29. **T25.G5.01.02** - Implement multi-type game state in CreatiCode ⚠️ **OVERLY BROAD**
30. **T25.G5.02.01** - Normalize text input using join and replace
31. **T25.G5.02.02** - Build a data validation and cleaning project ⚠️ **OVERLY BROAD**
32. **T25.G5.03** - Decide when to upgrade from list to table
33. **T25.G5.04** - Encode categorical values with numeric codes
34. **T25.G5.05** - Add meaningful default values to data fields
35. **T25.G5.06.01** - Create multi-column tables with varied data
36. **T25.G5.06.02** - Query tables by value
37. **T25.G5.06.03** - Filter and delete table rows
38. **T25.G5.07** - Validate data types and ranges before storage

### Grade 6 (12 skills)
39. **T25.G6.01** - Document metadata for datasets ⚠️ **OVERLY BROAD**
40. **T25.G6.02** - Explain lossy vs lossless representation ⚠️ **OVERLY BROAD**
41. **T25.G6.03** - Nest tables and lists within each other
42. **T25.G6.04** - Trace AI prompt inputs to structured slots
43. **T25.G6.05.01** - Search and filter table data with conditions
44. **T25.G6.05.02** - Aggregate table data using built-in blocks
45. **T25.G6.05.03** - Sort table data by column
46. **T25.G6.06.01** - Save data to server storage
47. **T25.G6.06.02** - Load data from server storage
48. **T25.G6.07.01** - Export table data as CSV
49. **T25.G6.07.02** - Import CSV data into tables
50. **T25.G6.07.03** - Debug and verify imported table structure ⚠️ **OVERLY BROAD**

### Grade 7 (10 skills)
51. **T25.G7.01** - Normalize repeating data into separate tables ⚠️ **OVERLY BROAD**
52. **T25.G7.02** - Identify bias introduced by representation choices
53. **T25.G7.03.01** - Save tables using CSV and server storage
54. **T25.G7.03.02** - Restore tables from CSV and server storage
55. **T25.G7.03.03** - Use direct table storage methods
56. **T25.G7.04** - Evaluate storage vs performance tradeoffs ⚠️ **OVERLY BROAD**
57. **T25.G7.05.01** - Fetch data from database collections
58. **T25.G7.05.02** - Query database collections with conditions
59. **T25.G7.05.03** - Update and delete collection documents
60. **T25.G7.06.01** - Set up Google Sheets integration
61. **T25.G7.06.02** - Read and write Google Sheets data
62. **T25.G7.06.03** - Append and modify Google Sheets rows

### Grade 8 (4 skills)
63. **T25.G8.01** - Design schemas for multi-modal apps ⚠️ **OVERLY BROAD**
64. **T25.G8.02** - Document versioning and lineage metadata
65. **T25.G8.03** - Evaluate compression strategies for large datasets ⚠️ **OVERLY BROAD**
66. **T25.G8.04** - Document data formats for project collaboration ⚠️ **OVERLY BROAD**

---

## 2. Specific Issues Found

### 2.1 Overly Broad Skills (15 identified)

#### **T25.G3.02 - Choose the right variable type**
**Issue**: Covers 3 distinct decisions in one skill:
1. Number vs text variables
2. Boolean values for game states
3. Single variables vs lists

**Recommendation**: Break into 3 skills:
- T25.G3.02.01: Distinguish number variables from text variables
- T25.G3.02.02: Use boolean variables for true/false states
- T25.G3.02.03: Decide between single variables and lists

---

#### **T25.G3.06.02 - Access table items by row and column**
**Issue**: Combines understanding table structure with accessing cells

**Recommendation**: Break into 2 skills:
- T25.G3.06.02: Understand table row and column indexing
- T25.G3.06.03: Retrieve specific values from tables using blocks

---

#### **T25.G4.03 - Compare dense vs sparse representations**
**Issue**: Requires both understanding the concepts AND implementing both approaches - too much for one skill

**Recommendation**: Break into 2 skills:
- T25.G4.03.01: Identify differences between dense and sparse data storage
- T25.G4.03.02: Implement and compare both representation methods

---

#### **T25.G5.01.02 - Implement multi-type game state in CreatiCode**
**Issue**: Combines multiple variable types, lists, AND coordinated updates across data structures

**Recommendation**: Break into 3 skills:
- T25.G5.01.02: Implement game state using multiple variable types
- T25.G5.01.03: Maintain synchronized updates across related variables
- T25.G5.01.04: Combine variables and lists in game state management

---

#### **T25.G5.02.02 - Build a data validation and cleaning project**
**Issue**: "Complete survey response normalization project" combining multiple cleaning techniques, validation, and storage - this is a full project, not a single skill

**Recommendation**: Break into 4 skills:
- T25.G5.02.02: Apply multiple text normalization operations in sequence
- T25.G5.02.03: Validate cleaned data against expected formats
- T25.G5.02.04: Store validated data with error handling
- T25.G5.02.05: Build complete data cleaning pipeline (capstone skill)

---

#### **T25.G6.01 - Document metadata for datasets**
**Issue**: Creating metadata tables with 5 different column types (FieldName, Description, DataType, Units, ValidRange) - too complex for single skill

**Recommendation**: Break into 3 skills:
- T25.G6.01.01: Identify essential metadata fields for data documentation
- T25.G6.01.02: Create metadata tables with basic field descriptions
- T25.G6.01.03: Add data type, unit, and range specifications to metadata

---

#### **T25.G6.02 - Explain lossy vs lossless representation**
**Issue**: Combines conceptual understanding, implementation of BOTH approaches, AND tradeoff analysis

**Recommendation**: Break into 3 skills:
- T25.G6.02.01: Distinguish lossy from lossless data representation
- T25.G6.02.02: Implement lossless path recording (every frame)
- T25.G6.02.03: Implement lossy path recording and compare tradeoffs

---

#### **T25.G6.03 - Nest tables and lists within each other**
**Issue**: Covers design, implementation, AND accessing nested data structures

**Recommendation**: Break into 3 skills:
- T25.G6.03.01: Design nested data structures on paper
- T25.G6.03.02: Create tables with list-type columns
- T25.G6.03.03: Access nested data using combined operations

---

#### **T25.G6.05.01 - Search and filter table data with conditions**
**Issue**: Finding rows, collecting to new list, AND displaying - multiple operations

**Recommendation**: Break into 3 skills:
- T25.G6.05.01: Find single rows matching conditions
- T25.G6.05.02: Collect multiple matching rows into new structures
- T25.G6.05.03: Display filtered results effectively

---

#### **T25.G6.07.03 - Debug and verify imported table structure**
**Issue**: Combines debugging, verification, and fixing import issues

**Recommendation**: Break into 2 skills:
- T25.G6.07.03: Verify imported table structure matches expectations
- T25.G6.07.04: Debug and fix common CSV import problems

---

#### **T25.G7.01 - Normalize repeating data into separate tables**
**Issue**: Examining redundancy, designing normalized schema, implementing TWO tables, AND querying across tables - database normalization is complex

**Recommendation**: Break into 4 skills:
- T25.G7.01.01: Identify redundant data in single tables
- T25.G7.01.02: Design normalized multi-table schemas with ID linking
- T25.G7.01.03: Implement linked tables in CreatiCode
- T25.G7.01.04: Query across linked tables using ID relationships

---

#### **T25.G7.04 - Evaluate storage vs performance tradeoffs**
**Issue**: Building TWO different implementations AND comparing tradeoffs

**Recommendation**: Break into 3 skills:
- T25.G7.04.01: Implement pre-calculated stored totals
- T25.G7.04.02: Implement computed-on-demand totals
- T25.G7.04.03: Compare storage and performance tradeoffs

---

#### **T25.G8.01 - Design schemas for multi-modal apps**
**Issue**: Extremely broad - combines vision AI, audio AI, multiple data types, AND relationships. This is essentially a capstone project.

**Recommendation**: Break into 5 skills:
- T25.G8.01.01: Design data structures for vision AI outputs
- T25.G8.01.02: Design data structures for audio AI outputs
- T25.G8.01.03: Design conversation history storage
- T25.G8.01.04: Map relationships between different data modalities
- T25.G8.01.05: Create unified multi-modal schema (capstone)

---

#### **T25.G8.03 - Evaluate compression strategies for large datasets**
**Issue**: Multiple compression examples, calculating memory usage, discussing lossy vs lossless, AND implementing

**Recommendation**: Break into 4 skills:
- T25.G8.03.01: Identify opportunities for data compression
- T25.G8.03.02: Implement delta-based compression (store changes only)
- T25.G8.03.03: Calculate and compare storage requirements
- T25.G8.03.04: Choose appropriate compression strategy for constraints

---

#### **T25.G8.04 - Document data formats for project collaboration**
**Issue**: Creating comprehensive spec with inputs, outputs, AND formatting rules, PLUS implementing sample project

**Recommendation**: Break into 4 skills:
- T25.G8.04.01: Document required input data specifications
- T25.G8.04.02: Document output data formats and structure
- T25.G8.04.03: Define data sharing and formatting rules
- T25.G8.04.04: Implement project following data specifications

---

### 2.2 Grade Appropriateness Issues

#### **Correct Grade Placement** ✅
- **K-2**: All skills are picture-based or unplugged - EXCELLENT
  - Kindergarten: Spotting data, matching symbols, simple legends
  - Grade 1: Tally marks, picture tables, word/number equivalence
  - Grade 2: Chart labels, translations between formats, combining attributes

- **Grade 3+**: All involve block-based coding in CreatiCode - CORRECT

#### **Potential Grade Level Concerns**

**T25.G3.00.01 - Create and name variables (Grade 3)**
- **Issue**: Has dependency on T09.G3.01.04 (Display variable value on stage) which creates a circular dependency issue
- **Concern**: Displaying variables should come AFTER creating them, not as a prerequisite
- **Fix**: Remove T09.G3.01.04 from dependencies OR make T25.G3.00.01 the .00 skill with no dependencies

**T25.G3.06.01/02 - Tables in Grade 3**
- **Concern**: Introducing tables alongside variables and lists might be too much
- **Assessment**: Actually OK - they're simple 2-column tables, appropriate for Grade 3
- **Keep as is**

**T25.G6.04 - AI prompt templates (Grade 6)**
- **Concern**: Feels advanced for Grade 6
- **Assessment**: It's just variable substitution into text templates using join blocks - appropriate
- **Keep as is**

**T25.G7.06.01-03 - Google Sheets (Grade 7)**
- **Concern**: Requires Google accounts and parent/teacher approval
- **Assessment**: Documented in description, appropriate for Grade 7
- **Keep as is but ensure clear prerequisites**

---

### 2.3 Duplicates and Overlaps Within T25

#### **Significant Overlap Found:**

**T25.G6.05.01 vs T25.G5.06.02**
- G5.06.02: Query tables by value - "find row number where column = value"
- G6.05.01: Search and filter table data - "find all rows where Score > 100"
- **Overlap**: Both search tables, but G6 version is more advanced (conditions vs exact match, multiple results vs single)
- **Assessment**: NOT duplicate - appropriate progression
- **Keep both**

**T25.G6.06.01-02 (server storage) vs T25.G7.03.03 (table storage)**
- G6.06: Individual values to server storage
- G7.03.03: Direct table storage methods
- **Overlap**: Both use storage, but different data types
- **Assessment**: NOT duplicate - appropriate progression
- **Keep both**

**T25.G6.07.01-02 (CSV) vs T25.G7.03.01-02 (CSV + server storage)**
- G6.07: CSV export/import as files
- G7.03: CSV text combined with server storage
- **Overlap**: Both use CSV format
- **Assessment**: NOT duplicate - G7 adds server persistence layer
- **Keep both but clarify relationship**

#### **No True Duplicates Found** ✅
All apparent overlaps represent intentional skill progression from simpler to more complex versions.

---

### 2.4 Intra-Topic Dependency Analysis

#### **X-2 Rule Violations** (Dependencies more than 2 grades back)

**T25.G6.01 - Document metadata for datasets (Grade 6)**
- Depends on: T25.G4.01 (Build schema diagrams) - Grade 4 ❌ **2 GRADES BACK** (borderline acceptable)
- Depends on: T25.G4.04 (Document special rules) - Grade 4 ❌ **2 GRADES BACK** (borderline acceptable)
- **Assessment**: Exactly at X-2 limit, acceptable but review if intermediate skill needed

**T25.G6.02 - Explain lossy vs lossless (Grade 6)**
- Depends on: T25.G4.03 (Compare dense vs sparse) - Grade 4 ❌ **2 GRADES BACK** (borderline acceptable)
- **Assessment**: At X-2 limit, acceptable

**T25.G7.01 - Normalize repeating data (Grade 7)**
- Depends on: T25.G5.03 (Decide when to upgrade from list to table) - Grade 5 ❌ **2 GRADES BACK** (borderline acceptable)
- **Assessment**: At X-2 limit, acceptable

**T25.G8.01 - Design schemas for multi-modal apps (Grade 8)**
- Depends on: T25.G6.03 (Nest tables and lists) - Grade 6 ❌ **2 GRADES BACK** (borderline acceptable)
- Depends on: T25.G7.01 (Normalize repeating data) - Grade 7 ✅ **1 GRADE BACK** (good)
- **Assessment**: Mix of X-2 and X-1, acceptable

**T25.G8.03 - Evaluate compression strategies (Grade 8)**
- Depends on: T25.G6.02 (Lossy vs lossless) - Grade 6 ❌ **2 GRADES BACK** (borderline acceptable)
- Depends on: T25.G7.04 (Storage vs performance) - Grade 7 ✅ **1 GRADE BACK** (good)
- **Assessment**: Mix acceptable

#### **Cross-Grade Dependencies Beyond X-2** ⚠️

**T25.G7.04 - Evaluate storage vs performance tradeoffs (Grade 7)**
- Depends on: T25.G6.02 (Lossy vs lossless) - Grade 6 ✅
- Depends on: T25.G6.01 (Document metadata) - Grade 6 ✅
- BUT T25.G6.01 depends on T25.G4.01 (Grade 4)
- **Transitive violation**: G7 → G6 → G4 = **3 GRADES BACK** ❌
- **Fix**: Add Grade 5 intermediate skill OR remove G4 dependency from G6.01

#### **Dependencies on Later Skills in Same Topic** ⚠️

**T25.G3.00.01 - Create and name variables**
- Depends on: T09.G3.01.04 (Display variable value) from Topic T09
- **Issue**: T09.G3.01.04 probably depends on T25.G3.00.01 (can't display variables without creating them)
- **Likely circular dependency across topics**
- **Fix**: T25.G3.00.01 should have NO T25 dependencies (it's foundational)

**T25.G3.00.02 - Create and name lists**
- Depends on: T25.G3.00.01 (Create variables) ✅ GOOD
- Depends on: T09.G3.01.04 (Display variable) from T09
- **Same circular dependency issue**
- **Fix**: Remove T09 dependency or make T09.G3.01.04 depend on T25.G3.00.01

#### **Unnecessary Same-Grade Dependencies**

**T25.G3.04.01 and T25.G3.05** (both Grade 3)
- G3.04.01: Identify inconsistent units
- G3.05: Identify when data needs cleaning
- **Both depend on G3.03** (Break sentences into structured records)
- **Issue**: Why does unit consistency require structured records?
- **Assessment**: Dependency makes sense for G3.04.01 (units appear in record fields) but questionable
- **Recommendation**: Review if G3.04.01 could be standalone

**T25.G5.06.01, .02, .03** (all Grade 5)
- Sequential chain: .01 → .02 → .03
- **Assessment**: Good progressive sequence
- **Keep as is**

---

### 2.5 Logical Progression Analysis

#### **Strong Progressions** ✅

**Variables and Lists (Grades 3-5)**
- G3.00.01: Create variables →
- G3.00.02: Create lists →
- G3.01.01: Add items manually →
- G3.01.02: Map real data to lists →
- G3.02: Choose variable types →
- G4-5: More complex variable/list operations
- **Assessment**: EXCELLENT progression

**Tables (Grades 3-7)**
- G3.06.01: Create simple tables →
- G3.06.02: Access table items →
- G4.06: Populate tables from lists →
- G5.06.01-03: Multi-column tables, querying, filtering →
- G6.05.01-03: Advanced search, aggregation, sorting →
- G6.07.01-02: CSV export/import →
- G7.01: Normalize to multiple tables →
- G7.05.01-03: Database collections
- **Assessment**: EXCELLENT progression

**Data Persistence (Grades 6-7)**
- G6.06.01: Save to server storage →
- G6.06.02: Load from server storage →
- G6.07.01: Export CSV →
- G6.07.02: Import CSV →
- G7.03.01-03: Combined CSV + server storage
- **Assessment**: GOOD progression

**Metadata and Documentation (Grades 4-8)**
- G4.01: Build schema diagrams →
- G4.04: Document data keys →
- G6.01: Document metadata →
- G8.02: Document versioning/lineage →
- G8.04: Document for collaboration
- **Assessment**: GOOD progression

#### **Weak Progressions / Gaps** ⚠️

**Grade 5 → Grade 6 Jump**
- Grade 5 ends with: validation, multi-column tables, filtering
- Grade 6 starts with: metadata documentation, lossy/lossless, nesting
- **Gap**: No skills bridging advanced table operations to conceptual understanding of data tradeoffs
- **Recommendation**: Consider adding Grade 5 skill on data structure tradeoffs introduction

**Grade 7 → Grade 8 Jump**
- Grade 7: Database collections, Google Sheets, normalization
- Grade 8: Multi-modal schemas, compression, collaboration docs
- **Gap**: Grade 8 assumes multi-modal AI knowledge (vision T23, audio T24)
- **Assessment**: Acceptable if dependencies on T23/T24 are explicit (they are in T25.G8.01)

**Data Cleaning Sequence**
- G3.05: Identify when cleaning needed →
- G5.02.01: Normalize text →
- G5.02.02: Build cleaning project
- **Gap**: Nothing in Grade 4 about data quality
- **Recommendation**: Consider Grade 4 skill on data quality checking

---

## 3. CreatiCode Data Representation Features

### 3.1 Variables (Category: Variables)

**Basic Operations:**
- Create variables (Make a Variable button)
- Set variable value: `set [variable] to [value]`
- Change variable: `change [variable] by [N]`
- Reduce variable: `reduce [variable] by [N]` (for young learners)
- Display variable monitors on stage
- Export variable: `export variable [variable]` (to txt file)
- Import variable: `import variable [variable]` (from txt/csv file)

**Variable Types Supported:**
- Number variables
- Text variables
- Boolean (implicit through comparison operators)

### 3.2 Lists (Category: Variables)

**Basic List Operations:**
- Create lists (Make a List button)
- Add item: `add [item] to [list]`
- Delete item: `delete [index] of [list]`
- Delete value: `delete value [V] from [list]`
- Insert item: `insert [item] at [index] of [list]`
- Replace item: `replace item [index] of [list] with [item]`
- Change item value: `change item [index] of [list] by [N]`
- Reduce item: `reduce item [index] of [list] by [N]`

**List Queries:**
- Item at index: `item [index] of [list]`
- Item number: `# of item [value] in [list]`
- Item containing: `# of item containing [TEXT] in [list]`
- Length: `length of [list]`
- Contains: `[list] contains [item]`

**List Transformations:**
- Join list: `join [list] into text with [SEPARATOR]`
- Split text: `set [list] to split of [TEXT] with splitter [SEPARATOR]`
- Copy list: `copy [list1] to [list2]`
- Append list: `append [list1] to [list2]`
- Insert items from list: `insert [N] [selector] items from [list1] into [list2]`

**List Manipulation:**
- Reverse: `reverse [list]`
- Shuffle: `reshuffle [list] randomly`
- Sort: `sort list [list] from [large to small / small to large]`
- Delete all: `delete all of [list]`

**List Generation:**
- Random list: `set [list] to [N] random whole numbers between [MIN] and [MAX] [no repetition / allow repetition]`
- Seeded random: `set [list] to [N] random numbers with seed [SEED]`

**List Analytics:**
- Smallest/Largest/Sum/Average/Median: `[method] of list [list]`

**List Iteration:**
- For each: `for each [variable] in [list]` (C-block)
- For each index: `for each index [variable] in [list]` (C-block)

### 3.3 Tables (Category: Variables)

**Table Creation:**
- Create table: `create table [name]`
- Add row: `add row to table [name]` with values
- Insert row: `insert row at [index] to table [name]`
- Replace row: `replace row [index] of table [name]`

**Table Access:**
- Item at row/column: `item at row [number] column [name/number] of table [name]`
- Row at index: `row at index [number] of table [name]`
- Row count: `row count of table [name]`

**Table Manipulation:**
- Delete row: `delete row [index] from table [name]`
- Delete all rows: `delete all rows of table [name]`
- Delete column: `delete column [name] from table [name]`
- Remove all columns: `remove all columns from table [name]`

**Table Transformations:**
- Copy table: `copy table [table1] into table [table2]`
- Append table: `append table [table1] into table [table2]`
- Pivot table: `pivot table [table1] into table [table2]`
- Compute table: `set table [table] to computed [...]`

**Table Analysis:**
- Sort table: `sort table by column [name] in [ascending/descending] order`
- Shuffle table: `reshuffle table [name]`
- Lookup table: `lookup in table [name]`

**Table Display:**
- Show table: `show table [name]`
- Hide table: `hide table [name]`
- Show snapshot: `show snapshot of table [name]`

**Table Import/Export:**
- Export table: `export table [name]` (as CSV file)
- Import table: `import table [name]` (from CSV file)
- Save table: `save table [name]` (to local storage with name)
- Load table: `load table [name]` (from local storage)

### 3.4 Server Storage & Database

**Server Storage (Individual Values):**
- Save data: `save public/private data [value] with name [key]`
- Load data: `load data named [key]`
- Public vs private visibility settings

**Database Collections (Multi-user Tables):**
- Fetch all: `fetch all from collection [name]`
- Fetch with conditions: `fetch from collection [name] where [field] [operator] [value]`
- Insert from table: `insert rows from table [table] into collection [name]`
- Update documents: `update document in collection [name] where [condition]`
- Delete documents: `delete documents from collection [name] where [condition]`

**Semantic Database (Pinecone):**
- Search by query embedding: searches semantic database using query converted to embedding vector
- Filter by metadata field/value

### 3.5 External Integrations

**Google Sheets:**
- Connect: `connect to Google Sheet [URL]`
- Import sheet: `import sheet [name] from Google Sheets`
- Export table: `export table to Google Sheet [name]`
- Append row: `append row [values] to sheet [name]`
- Set cell: `set cell [row, column] to [value] in sheet [name]`

**File Operations:**
- Export variable to txt file
- Import variable from txt/csv file
- Export table as CSV download
- Import file into table

### 3.6 Advanced Features

**AI Integration:**
- Tables can store AI outputs (face detection, hand tracking with 47 rows per hand)
- KNN classifier: predict labels and write to table
- Geo info lookup: `get geo info for latitude (LAT) longitude (LON) and write into table`

**Data Structures:**
- Nested tables and lists (tables with list-type columns)
- Multi-column tables with mixed data types (text, number, boolean)
- Computed columns vs stored columns

---

## 4. Recommendations for Breaking Down Broad Skills

### Priority 1: Critical Splits (Must Do)

**1. T25.G3.02 - Choose the right variable type**
```
T25.G3.02.01: Distinguish number variables from text variables
T25.G3.02.02: Use boolean variables for true/false states
T25.G3.02.03: Decide between single variables and lists
```

**2. T25.G5.01.02 - Implement multi-type game state**
```
T25.G5.01.02: Implement game state using multiple variable types
T25.G5.01.03: Maintain synchronized updates across related variables
T25.G5.01.04: Combine variables and lists in game state management
```

**3. T25.G5.02.02 - Build data validation and cleaning project**
```
T25.G5.02.02: Apply multiple text normalization operations in sequence
T25.G5.02.03: Validate cleaned data against expected formats
T25.G5.02.04: Store validated data with error handling
T25.G5.02.05: Build complete data cleaning pipeline (capstone)
```

**4. T25.G7.01 - Normalize repeating data**
```
T25.G7.01.01: Identify redundant data in single tables
T25.G7.01.02: Design normalized multi-table schemas with ID linking
T25.G7.01.03: Implement linked tables in CreatiCode
T25.G7.01.04: Query across linked tables using ID relationships
```

**5. T25.G8.01 - Design schemas for multi-modal apps**
```
T25.G8.01.01: Design data structures for vision AI outputs
T25.G8.01.02: Design data structures for audio AI outputs
T25.G8.01.03: Design conversation history storage
T25.G8.01.04: Map relationships between different data modalities
T25.G8.01.05: Create unified multi-modal schema (capstone)
```

### Priority 2: Important Splits (Should Do)

**6. T25.G4.03 - Compare dense vs sparse**
```
T25.G4.03.01: Identify differences between dense and sparse data storage
T25.G4.03.02: Implement and compare both representation methods
```

**7. T25.G6.01 - Document metadata**
```
T25.G6.01.01: Identify essential metadata fields for data documentation
T25.G6.01.02: Create metadata tables with basic field descriptions
T25.G6.01.03: Add data type, unit, and range specifications
```

**8. T25.G6.02 - Explain lossy vs lossless**
```
T25.G6.02.01: Distinguish lossy from lossless data representation
T25.G6.02.02: Implement lossless path recording (every frame)
T25.G6.02.03: Implement lossy path recording and compare tradeoffs
```

**9. T25.G6.03 - Nest tables and lists**
```
T25.G6.03.01: Design nested data structures on paper
T25.G6.03.02: Create tables with list-type columns
T25.G6.03.03: Access nested data using combined operations
```

**10. T25.G7.04 - Evaluate storage vs performance**
```
T25.G7.04.01: Implement pre-calculated stored totals
T25.G7.04.02: Implement computed-on-demand totals
T25.G7.04.03: Compare storage and performance tradeoffs
```

**11. T25.G8.03 - Evaluate compression strategies**
```
T25.G8.03.01: Identify opportunities for data compression
T25.G8.03.02: Implement delta-based compression (store changes only)
T25.G8.03.03: Calculate and compare storage requirements
T25.G8.03.04: Choose appropriate compression strategy
```

### Priority 3: Optional Splits (Nice to Have)

**12. T25.G6.05.01 - Search and filter table data**
```
T25.G6.05.01: Find single rows matching conditions
T25.G6.05.02: Collect multiple matching rows into new structures
T25.G6.05.03: Display filtered results effectively
(Note: This creates ID conflict with existing G6.05.02/03 - would need renumbering)
```

**13. T25.G8.04 - Document data formats**
```
T25.G8.04.01: Document required input data specifications
T25.G8.04.02: Document output data formats and structure
T25.G8.04.03: Define data sharing and formatting rules
T25.G8.04.04: Implement project following specifications
```

---

## 5. Overall Assessment

### Strengths ✅

1. **Excellent K-2 unplugged foundation**: Picture-based data awareness, symbols, legends
2. **Smooth Grade 3 transition**: Variables and lists introduced appropriately
3. **Progressive table complexity**: From 2-column tables (G3) to normalized multi-table databases (G7)
4. **Strong persistence progression**: Local variables → server storage → database collections → Google Sheets
5. **Good conceptual scaffolding**: Dense/sparse → lossy/lossless → compression
6. **Real-world applications**: Survey data, game states, metadata, collaboration
7. **Comprehensive coverage**: Variables, lists, tables, databases, external integrations

### Weaknesses ⚠️

1. **Too many overly broad skills**: 15+ skills need breakdown (23% of topic)
2. **Some X-2 borderline violations**: Several dependencies exactly at 2-grade limit
3. **Circular dependency issue**: T25.G3.00.01 ↔ T09.G3.01.04 needs resolution
4. **Grade 4 gap**: No data quality/cleaning skills between G3 identification and G5 implementation
5. **Grade 5→6 conceptual jump**: From operations to tradeoff analysis needs bridging
6. **Heavy Grade 8**: Only 4 skills but all are extremely broad capstone projects

### Topic Coherence Score: 8/10

**Justification:**
- Strong logical progression from concrete to abstract
- Good integration of CreatiCode features
- Age-appropriate skill sequencing
- Some skills too broad, reducing granularity
- Minor dependency issues
- Overall excellent topic design with room for refinement

---

## 6. Action Items

### Immediate Fixes Required:

1. **Break down 15 overly broad skills** (see Priority 1-3 recommendations)
2. **Resolve T25.G3.00.01 circular dependency** with T09.G3.01.04
3. **Add Grade 4 data quality skill** to bridge G3→G5 gap
4. **Review all X-2 borderline dependencies** for potential Grade 5 intermediate skills
5. **Renumber skills after splits** to maintain ID consistency

### Optional Improvements:

6. Add Grade 5 skill on "Introduction to data structure tradeoffs"
7. Add Grade 6 skill on "Data quality metrics" before G7 normalization
8. Consider splitting Grade 8 into more granular skills to reduce capstone overload
9. Add explicit cross-references between CSV skills (G6.07 vs G7.03)
10. Create skill dependency visualization to identify hidden transitive violations

---

## Appendix A: Full Dependency Map

(See separate visualization - dependencies too complex for text format)

**Key Patterns:**
- Linear progressions: G3.00.01 → G3.00.02 → G3.01.01 → G3.01.02
- Branching: G3.02 splits to multiple G4/G5 paths
- Convergence: Multiple G5/G6 skills converge to G7.01 normalization
- Cross-topic: T06, T08, T09, T10 dependencies throughout

---

## Appendix B: CreatiCode Block Coverage Analysis

**Variables**: ✅ Fully covered (G3-G8)
**Lists**: ✅ Fully covered (G3-G8)
**Tables**: ✅ Well covered (G3-G7)
- Missing: Pivot tables (mentioned in blocks but no skill)
- Missing: Computed tables (mentioned but not explicitly taught)
- Missing: Lookup tables (block exists, no dedicated skill)

**Server Storage**: ✅ Covered (G6-G7)
**Database Collections**: ✅ Covered (G7)
**Google Sheets**: ✅ Covered (G7)
**CSV**: ✅ Covered (G6-G7)

**Advanced Features**:
- ⚠️ AI table outputs (face/hand detection) - mentioned in T23/T24 but not T25
- ⚠️ KNN classifier tables - not covered in T25
- ⚠️ Geo info tables - not covered in T25
- ⚠️ Regex match into list - not covered

**Recommendation**: Consider adding Grade 7-8 skills for advanced table integrations with AI/ML outputs.

---

## End of Analysis

**Document prepared**: 2025-11-23
**Total skills analyzed**: 65
**Issues identified**: 28
**Recommendations made**: 45+
**Next steps**: Review with curriculum team, implement Priority 1 splits, resolve circular dependencies
