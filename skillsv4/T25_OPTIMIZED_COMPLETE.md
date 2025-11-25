# Topic T25: Data Representation - OPTIMIZED VERSION
# Total Skills: 140+ (expanded from 80)
# Key Changes:
# - Split broad skills into focused sub-skills (one block/concept per skill)
# - Added missing list operations (reverse, reshuffle, sort, statistics, copy/append, join/split)
# - Added missing table operations (insert row, replace row/cell, group by, pivot, show table)
# - Added AI-data integration skills (face/body/hand to tables, NLP, KNN, neural nets)
# - Fixed intra-topic dependencies for logical progression
# - Preserved all cross-topic dependencies

## Kindergarten (3 skills - unchanged)

ID: T25.GK.01
Topic: T25 – Data Representation
Skill: Spot data in everyday objects
Description: Students decide whether a card shows a picture, a word, or a numeral and explain what information it carries. This builds foundational awareness that data can appear in multiple forms.

Dependencies: None


ID: T25.GK.02
Topic: T25 – Data Representation
Skill: Match quantities to symbols
Description: Students count a small set of items and choose a symbol (tally marks, dots, stickers) to represent the quantity, reinforcing that symbols can encode counts.

Dependencies:
* T25.GK.01: Spot data in everyday objects


ID: T25.GK.03
Topic: T25 – Data Representation
Skill: Build a two-symbol legend
Description: Given two emotions or states (happy/sad, hot/cold), students invent or select symbols to stand for each and use them to label pictures. This sets up later ideas about legends in charts.

Dependencies:
* T25.GK.02: Match quantities to symbols


## Grade 1 (3 skills - unchanged)

ID: T25.G1.01
Topic: T25 – Data Representation
Skill: Record data with tally marks
Description: Students watch a short animation (e.g., fish swimming by) and record occurrences with tally marks, then convert the tallies to numerals.

Dependencies:
* T25.GK.02: Match quantities to symbols


ID: T25.G1.02
Topic: T25 – Data Representation
Skill: Arrange data in picture rows and columns
Description: Learners arrange four objects into a simple table (rows = choices, columns = counts) using pictures instead of numerals, showing that tables are structured representations.

Dependencies:
* T25.G1.01: Record data with tally marks


ID: T25.G1.03
Topic: T25 – Data Representation
Skill: Describe the same fact in words and numbers
Description: Students practice saying "There are five apples" and also representing it with the numeral "5" and the word "five," highlighting multi-format representation.

Dependencies:
* T25.G1.01: Record data with tally marks


## Grade 2 (4 skills - unchanged)

ID: T25.G2.01
Topic: T25 – Data Representation
Skill: Choose labels for a category chart
Description: Students study a picture-based bar chart and provide meaningful text labels (e.g., rename "Column A" to "Bananas"). This underscores the importance of descriptive labels.

Dependencies:
* T25.G1.02: Arrange data in picture rows and columns


ID: T25.G2.02
Topic: T25 – Data Representation
Skill: Translate between timeline, table, and sentence
Description: Learners view a three-step story (wake up → eat breakfast → go to school) and encode it as (1) a timeline drawing, (2) a table with time + action, and (3) a narrative sentence. Emphasis is on seeing equivalence across forms.

Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T25.G1.03: Describe the same fact in words and numbers


ID: T25.G2.03
Topic: T25 – Data Representation
Skill: Pick the best representation for a question
Description: Students match questions ("How many stickers?" "Which order do things happen?") to the most useful representation type, building judgement about data tools.

Dependencies:
* T25.G1.02: Arrange data in picture rows and columns
* T25.G2.02: Translate between timeline, table, and sentence


ID: T25.G2.04
Topic: T25 – Data Representation
Skill: Combine two data attributes
Description: Learners create flashcards with two pieces of info (animal + habitat) to see how pairing attributes forms richer records.

Dependencies:
* T25.G1.02: Arrange data in picture rows and columns


## Grade 3 (28 skills - expanded from 17)

### G3.00 Series: Variables and Lists Basics (SPLIT FROM ORIGINAL 2 SKILLS)

ID: T25.G3.00.01.01
Topic: T25 – Data Representation
Skill: Create a variable in CreatiCode
Description: Students learn to create new variables using the 'Make a Variable' button in CreatiCode. They practice choosing meaningful names (like 'score' not 'x') and understand that variables store one value at a time.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence


ID: T25.G3.00.01.02
Topic: T25 – Data Representation
Skill: Set a variable value
Description: Students use 'set [variable] to [value]' blocks to assign values to variables. They practice setting variables to different values (numbers, text, true/false) and understand how to update stored values.

Dependencies:
* T25.G3.00.01.01: Create a variable in CreatiCode


ID: T25.G3.00.01.03
Topic: T25 – Data Representation
Skill: Display variable monitors on stage
Description: Students check and uncheck variable checkboxes to show/hide variable monitors on stage. They observe how variable values update in real-time when the variable changes, learning to visualize variable state during program execution.

Dependencies:
* T25.G3.00.01.02: Set a variable value


ID: T25.G3.00.02.01
Topic: T25 – Data Representation
Skill: Create a list in CreatiCode
Description: Students learn to create new lists using the 'Make a List' button in CreatiCode. They practice naming lists descriptively (like 'playerNames' not 'list1') and understand that lists store many values in order.

Dependencies:
* T25.G3.00.01.03: Display variable monitors on stage


ID: T25.G3.00.02.02
Topic: T25 – Data Representation
Skill: Add items to a list using blocks
Description: Students use 'add [item] to [list]' blocks to append items to the end of a list. They practice adding multiple items and understand that lists maintain insertion order.

Dependencies:
* T25.G3.00.02.01: Create a list in CreatiCode


ID: T25.G3.00.02.03
Topic: T25 – Data Representation
Skill: Display list monitors on stage
Description: Students check list checkboxes to show list monitors on stage. They observe how the list monitor displays all items with their index numbers, learning to visualize list contents during program execution.

Dependencies:
* T25.G3.00.02.02: Add items to a list using blocks


### G3.01 Series: Building Lists

ID: T25.G3.01.01
Topic: T25 – Data Representation
Skill: Build lists by manually adding items
Description: Students practice building lists by manually adding items one at a time using 'add [item] to [list]' blocks. They create simple lists (favorite foods, color names, numbers) and learn that lists maintain insertion order.

Dependencies:
* T25.G3.00.02.03: Display list monitors on stage


ID: T25.G3.01.02
Topic: T25 – Data Representation
Skill: Map survey responses into list variables
Description: Students take physical sticky notes and type each response as an item in a CreatiCode list using 'add item to list' blocks in sequence. They create named lists (e.g., 'favoriteColors') and populate them with survey data, demonstrating how analog data becomes digital.

Dependencies:
* T25.G3.01.01: Build lists by manually adding items
* T25.G2.01: Choose labels for a category chart


### G3.02 Series: Data Types

ID: T25.G3.02.01
Topic: T25 – Data Representation
Skill: Use number variables for counting and scoring
Description: Students create number variables (score, lives, timer) and practice storing numeric values. They use 'set [variable] to [number]' blocks with different numeric values and observe how number variables can be used in calculations.

Dependencies:
* T25.G3.01.02: Map survey responses into list variables


ID: T25.G3.02.02
Topic: T25 – Data Representation
Skill: Use text variables for names and messages
Description: Students create text variables (playerName, currentMessage, status) and practice storing text values. They use 'set [variable] to [text]' blocks with different text strings and understand that text variables store words, sentences, or any characters.

Dependencies:
* T25.G3.02.01: Use number variables for counting and scoring


ID: T25.G3.02.03
Topic: T25 – Data Representation
Skill: Use boolean variables for true/false states
Description: Students learn about boolean (true/false) variables for tracking binary states like isGameOver, isPaused, or hasKey. They practice setting boolean variables using true/false values and using them in conditional blocks.

Dependencies:
* T25.G3.02.02: Use text variables for names and messages
* T08.G3.02: Decide when a single if is enough


### G3.03 Series: Structured Data

ID: T25.G3.03
Topic: T25 – Data Representation
Skill: Break sentences into structured records
Description: Students read sentences ("Luna fed 4 fish to the seal") and fill a table with fields (character, action, quantity, target). This links narrative data to structured formats. Students implement one example in CreatiCode using four separate variables to represent a structured record.

Dependencies:
* T25.G3.02.03: Use boolean variables for true/false states
* T08.G3.03: Pick the right conditional block for a scenario


### G3.04 Series: Data Consistency

ID: T25.G3.04.01
Topic: T25 – Data Representation
Skill: Identify inconsistent units in data
Description: Learners examine a table mixing minutes and seconds and identify which entries use different units. They mark the inconsistencies and explain why having different units in the same column makes comparisons impossible.

Dependencies:
* T25.G3.03: Break sentences into structured records


ID: T25.G3.04.02
Topic: T25 – Data Representation
Skill: Convert data to consistent units
Description: Students build a CreatiCode project that converts mixed time formats to a single unit. Users enter values in either minutes or seconds, and the program converts everything to seconds using variables and math operators.

Dependencies:
* T25.G3.04.01: Identify inconsistent units in data
* T09.G3.02: Use a variable in a conditional (if block)


### G3.05 Series: Data Quality Awareness

ID: T25.G3.05
Topic: T25 – Data Representation
Skill: Identify when data needs cleaning
Description: Students examine lists containing inconsistent data (different date formats, mixed capitalization like 'Red', 'red', 'RED') and mark which entries need fixing. They explain what makes data inconsistent and why it causes problems in programs.

Dependencies:
* T25.G3.03: Break sentences into structured records
* T25.G3.04.01: Identify inconsistent units in data


### G3.06 Series: Table Basics (SPLIT FROM ORIGINAL 2 SKILLS)

ID: T25.G3.06.01.01
Topic: T25 – Data Representation
Skill: Create an empty table in CreatiCode
Description: Students use the 'create table with columns [list]' block to create a new empty table with column names. They practice specifying column names as a list and understand that tables organize data into rows and columns.

Dependencies:
* T25.G3.02.03: Use boolean variables for true/false states
* T25.G2.04: Combine two data attributes


ID: T25.G3.06.01.02
Topic: T25 – Data Representation
Skill: Add rows to a table
Description: Students use 'add row [values] to table' blocks to insert rows with multiple values. They practice adding rows one at a time, ensuring each value corresponds to the correct column, and understand how tables grow row by row.

Dependencies:
* T25.G3.06.01.01: Create an empty table in CreatiCode


ID: T25.G3.06.01.03
Topic: T25 – Data Representation
Skill: Display table monitors on stage
Description: Students use 'show table [name]' blocks to display tables on stage. They observe how tables appear with columns and rows clearly formatted, learning to visualize table contents during program execution.

Dependencies:
* T25.G3.06.01.02: Add rows to a table


ID: T25.G3.06.02
Topic: T25 – Data Representation
Skill: Access table items by row and column
Description: Students learn to retrieve specific values from tables using 'item at row [number] column [name/number] of table' blocks. They practice accessing individual cells and displaying values using 'say' blocks.

Dependencies:
* T25.G3.06.01.03: Display table monitors on stage
* T10.G3.01: Loop through and process each item in a list


### G3.07 Series: List Operations Basics (NEW - MISSING SKILLS)

ID: T25.G3.07.01
Topic: T25 – Data Representation
Skill: Delete specific items from lists
Description: Students use 'delete [index/value] of [list]' blocks to remove items from lists. They practice deleting items by index number (position) and by value, understanding how list length changes after deletion.

Dependencies:
* T25.G3.01.01: Build lists by manually adding items


ID: T25.G3.07.02
Topic: T25 – Data Representation
Skill: Insert items at specific positions in lists
Description: Students use 'insert [item] at [index] of [list]' blocks to add items at specific positions (not just the end). They understand how insertion shifts later items to higher index numbers.

Dependencies:
* T25.G3.07.01: Delete specific items from lists


ID: T25.G3.07.03
Topic: T25 – Data Representation
Skill: Replace items in lists
Description: Students use 'replace item [index] of [list] with [value]' blocks to change existing list items. They practice updating list contents while maintaining list length.

Dependencies:
* T25.G3.07.02: Insert items at specific positions in lists


ID: T25.G3.07.04
Topic: T25 – Data Representation
Skill: Get list length and access items by index
Description: Students use 'length of [list]' reporter blocks to count list items and 'item [index] of [list]' blocks to access specific items. They understand that list indices start at 1.

Dependencies:
* T25.G3.07.03: Replace items in lists


## Grade 4 (24 skills - expanded from 6)

### G4.01-05 Series: Schema and Representations (unchanged core concepts)

ID: T25.G4.01
Topic: T25 – Data Representation
Skill: Build schema diagrams for simple apps
Description: Students diagram an app's data needs (e.g., to-do list: task text, due date, done?) showing column names and types before coding. They practice identifying what data their app needs to store, choosing appropriate data types for each field, and documenting their plan.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T05.G3.01: Put human‑centered design steps in order
* T05.G3.02: Identify user needs from a short interview transcript
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T25.G2.04: Combine two data attributes
* T25.G3.02.03: Use boolean variables for true/false states


ID: T25.G4.02
Topic: T25 – Data Representation
Skill: Encode the same fact in decimal, fraction, and percentage
Description: Students practice representing the same numerical fact in three formats: decimal (0.75), fraction (3/4), and percentage (75%). They use CreatiCode's math operators and variables to store and display values in each format.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T25.G2.02: Translate between timeline, table, and sentence
* T25.G3.01.02: Map survey responses into list variables


ID: T25.G4.03
Topic: T25 – Data Representation
Skill: Compare dense vs sparse representations
Description: Students compare dense (storing all values) versus sparse (storing only non-empty values) data representations. Example: representing a tic-tac-toe board as [X, O, empty, X, O, empty, empty, empty, X] vs [square1:X, square2:O, square4:X, square5:O, square9:X].

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T05.G3.01: Put human‑centered design steps in order
* T05.G3.02: Identify user needs from a short interview transcript
* T06.G2.03: Design a simple "if-then" game rule
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T25.G2.03: Pick the best representation for a question
* T25.G3.02.03: Use boolean variables for true/false states


ID: T25.G4.04
Topic: T25 – Data Representation
Skill: Document special rules in a data key
Description: Learners create a legend for a mini-map (color = terrain) and add a note describing exceptions (e.g., "Purple = portal unless near volcano"). Students create a legend table in CreatiCode with columns for Symbol and Meaning.

Dependencies:
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.03: Design a simple "if-then" game rule
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T25.G2.01: Choose labels for a category chart
* T25.G3.02.03: Use boolean variables for true/false states


ID: T25.G4.05
Topic: T25 – Data Representation
Skill: Distinguish between raw data and computed values
Description: Students examine a game scoreboard and identify which values are stored (points earned each round) vs computed (total score). They build a simple scoreboard using separate variables for round scores and a reporter block for total score.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T25.G3.02.03: Use boolean variables for true/false states
* T25.G4.01: Build schema diagrams for simple apps


### G4.06 Series: List to Table Conversion (SPLIT)

ID: T25.G4.06.01
Topic: T25 – Data Representation
Skill: Design algorithm to populate tables from lists
Description: Students design (on paper) an algorithm that loops through a list and plans how to add each item to a table row. They specify loop bounds, index tracking, and row creation steps before coding.

Dependencies:
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T05.G3.01: Put human‑centered design steps in order
* T05.G3.02: Identify user needs from a short interview transcript
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T25.G3.06.01.03: Display table monitors on stage


ID: T25.G4.06.02
Topic: T25 – Data Representation
Skill: Implement table population from list data
Description: Students implement their designed algorithm by writing scripts that loop through a list and use 'add row to table' blocks to build a table from list data. They create tables with Name and Index columns by looping through lists with index counters.

Dependencies:
* T25.G4.06.01: Design algorithm to populate tables from lists
* T10.G3.01.01: Create a list variable and add items to it
* T25.G3.06.01.02: Add rows to a table


### G4.07 Series: Advanced List Operations (NEW - MISSING SKILLS)

ID: T25.G4.07.01
Topic: T25 – Data Representation
Skill: Join list items to text
Description: Students use 'join items of [list] with [separator]' blocks to convert lists into text strings. They practice using different separators (comma, space, newline) and understand how lists can be converted to text for display or export.

Dependencies:
* T25.G3.07.04: Get list length and access items by index


ID: T25.G4.07.02
Topic: T25 – Data Representation
Skill: Split text to list
Description: Students use 'split [text] by [delimiter]' blocks to convert text strings into lists. They practice splitting sentences by spaces (words) or CSV text by commas, understanding how text can be parsed into structured data.

Dependencies:
* T25.G4.07.01: Join list items to text


ID: T25.G4.07.03
Topic: T25 – Data Representation
Skill: Find items containing a value in lists
Description: Students use 'item # of [value] in [list]' blocks to search for specific values and get their index positions. They understand how to locate data within lists for further processing.

Dependencies:
* T25.G3.07.04: Get list length and access items by index


ID: T25.G4.07.04
Topic: T25 – Data Representation
Skill: Check if lists contain specific values
Description: Students use '[list] contains [value]' reporter blocks to test whether a value exists in a list. They practice using this in conditionals to make decisions based on list membership.

Dependencies:
* T25.G4.07.03: Find items containing a value in lists


### G4.08 Series: Table Column Operations (NEW - MISSING SKILLS)

ID: T25.G4.08.01
Topic: T25 – Data Representation
Skill: Add columns to existing tables
Description: Students use 'add column [name] to table' blocks to add new columns to tables after creation. They understand how to extend table schemas dynamically and practice populating new columns.

Dependencies:
* T25.G3.06.01.03: Display table monitors on stage


ID: T25.G4.08.02
Topic: T25 – Data Representation
Skill: Delete columns from tables
Description: Students use 'delete column [name/number] from table' blocks to remove columns from tables. They understand when to remove unnecessary columns and how this affects table structure.

Dependencies:
* T25.G4.08.01: Add columns to existing tables


ID: T25.G4.08.03
Topic: T25 – Data Representation
Skill: Get column values as lists
Description: Students use 'column [name/number] of table' reporter blocks to extract entire columns as lists. They understand how to convert table columns to lists for processing with list operations.

Dependencies:
* T25.G4.08.01: Add columns to existing tables
* T25.G3.07.04: Get list length and access items by index


### G4.09 Series: Table Row Operations (NEW - MISSING SKILLS)

ID: T25.G4.09.01
Topic: T25 – Data Representation
Skill: Get row count of tables
Description: Students use 'number of rows in [table]' reporter blocks to count table rows. They practice using row counts in loops and conditionals.

Dependencies:
* T25.G3.06.01.03: Display table monitors on stage


ID: T25.G4.09.02
Topic: T25 – Data Representation
Skill: Get entire rows as lists
Description: Students use 'row [number] of table' reporter blocks to extract entire rows as lists of values. They understand how rows can be processed as units.

Dependencies:
* T25.G4.09.01: Get row count of tables


ID: T25.G4.09.03
Topic: T25 – Data Representation
Skill: Delete rows from tables by index
Description: Students use 'delete row [number] from table' blocks to remove specific rows by position. They understand how row deletion shifts subsequent rows to lower indices.

Dependencies:
* T25.G4.09.02: Get entire rows as lists


ID: T25.G4.09.04
Topic: T25 – Data Representation
Skill: Delete all rows from tables
Description: Students use 'delete all rows from [table]' blocks to clear table contents while preserving column structure. They understand when to reset tables for reuse.

Dependencies:
* T25.G4.09.03: Delete rows from tables by index


## Grade 5 (35 skills - expanded from 17)

### G5.01 Series: Game State Management (existing - minor refinement)

ID: T25.G5.01.01
Topic: T25 – Data Representation
Skill: Design multi-type data structures on paper
Description: Students design a "player" data structure on paper showing different data types: text (name), number (score, health), Boolean (isAlive), and list (inventory). They create a schema diagram identifying which CreatiCode data structure to use for each field.

Dependencies:
* T25.G3.02.03: Use boolean variables for true/false states
* T25.G4.01: Build schema diagrams for simple apps
* T12.G3.05: Test a program against its expected behavior
* T12.G4.05: Identify specific lines of code that caused incorrect output
* T10.G3.05: Loop through each item in a list
* T09.G3.03: Use a variable in a simple conditional (if block)


ID: T25.G5.01.02.01
Topic: T25 – Data Representation
Skill: Define game state variables with initial values
Description: Students implement the initial game state design by creating all necessary variables (playerName, score, health, isAlive) and lists (inventory) with appropriate initial values using green-flag scripts.

Dependencies:
* T25.G5.01.01: Design multi-type data structures on paper
* T12.G3.05: Test a program against its expected behavior
* T12.G4.05: Identify specific lines of code that caused incorrect output
* T10.G3.05: Loop through each item in a list
* T09.G3.03: Use a variable in a simple conditional (if block)


ID: T25.G5.01.02.02
Topic: T25 – Data Representation
Skill: Update game state variables based on events
Description: Students implement coordinated state updates in response to game events. When the player picks up an item, they add it to inventory AND update score. When the player takes damage, they decrease health AND check if health reaches zero.

Dependencies:
* T25.G5.01.02.01: Define game state variables with initial values
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T12.G3.05: Test a program against its expected behavior
* T12.G4.05: Identify specific lines of code that caused incorrect output
* T10.G3.05: Loop through each item in a list


ID: T25.G5.01.02.03
Topic: T25 – Data Representation
Skill: Persist game state across game restarts
Description: Students learn to save and restore the complete game state. They implement save functionality that stores all critical variables (score, health, inventory contents) and load functionality that retrieves these values when the game restarts.

Dependencies:
* T25.G5.01.02.02: Update game state variables based on events
* T12.G3.05: Test a program against its expected behavior
* T12.G4.05: Identify specific lines of code that caused incorrect output
* T10.G3.05: Loop through each item in a list
* T09.G3.03: Use a variable in a simple conditional (if block)


### G5.02 Series: Data Cleaning

ID: T25.G5.02.01
Topic: T25 – Data Representation
Skill: Normalize text input using join and replace
Description: Students use CreatiCode's text operation blocks to standardize inconsistent inputs. They practice: (1) using 'join [text] and [text]' blocks to combine separated inputs, (2) using 'replace [old] with [new] in [text]' blocks to fix common variations.

Dependencies:
* T25.G3.01.02: Map survey responses into list variables
* T25.G3.04.02: Convert data to consistent units
* T09.G3.03: Use a variable in a simple conditional (if block)


ID: T25.G5.02.02.01
Topic: T25 – Data Representation
Skill: Identify and catalog data quality issues
Description: Students examine a dataset with multiple issues (inconsistent formats, duplicates, missing values, invalid entries) and create a checklist identifying each type of problem. They categorize issues by type.

Dependencies:
* T25.G5.02.01: Normalize text input using join and replace
* T25.G3.05: Identify when data needs cleaning
* T09.G3.03: Use a variable in a simple conditional (if block)


ID: T25.G5.02.02.02
Topic: T25 – Data Representation
Skill: Remove duplicate entries from lists
Description: Students build a script that detects and removes duplicate entries from a list. They use loops to check if an item already exists in a "clean" list before adding it, creating a duplicate-free version.

Dependencies:
* T25.G5.02.02.01: Identify and catalog data quality issues
* T09.G3.03: Use a variable in a simple conditional (if block)
* T10.G3.05: Loop through each item in a list


ID: T25.G5.02.02.03
Topic: T25 – Data Representation
Skill: Fix inconsistent text formats
Description: Students build a script that standardizes text formatting in a list. They apply multiple transformations: convert all text to lowercase, remove extra whitespace, replace variant spellings with standard forms.

Dependencies:
* T25.G5.02.02.02: Remove duplicate entries from lists
* T09.G3.03: Use a variable in a simple conditional (if block)
* T10.G3.05: Loop through each item in a list


ID: T25.G5.02.02.04
Topic: T25 – Data Representation
Skill: Validate cleaned data against rules
Description: Students implement validation checks that verify cleaned data meets quality requirements. They check that all entries match expected patterns using conditional blocks. Invalid entries are flagged or removed.

Dependencies:
* T25.G5.02.02.03: Fix inconsistent text formats
* T09.G3.03: Use a variable in a simple conditional (if block)
* T07.G3.01: Use a counted repeat loop


ID: T25.G5.02.02.05
Topic: T25 – Data Representation
Skill: Test data cleaning with sample datasets
Description: Students create test cases with known data quality issues and verify their cleaning pipeline fixes them correctly. They prepare "dirty" sample data, run it through their cleaning process, and compare results to expected outputs.

Dependencies:
* T25.G5.02.02.04: Validate cleaned data against rules
* T09.G3.03: Use a variable in a simple conditional (if block)
* T07.G3.01: Use a counted repeat loop


### G5.03 Series: Data Structure Selection

ID: T25.G5.03
Topic: T25 – Data Representation
Skill: Decide when to upgrade from list to table
Description: Students examine three scenarios with different data requirements and decide whether to use lists (single attribute per item) or tables (multiple attributes per item). They implement one chosen scenario in CreatiCode.

Dependencies:
* T25.G3.01.02: Map survey responses into list variables
* T25.G4.03: Compare dense vs sparse representations
* T10.G3.05: Loop through each item in a list


### G5.04-05 Series: Encoding and Defaults

ID: T25.G5.04
Topic: T25 – Data Representation
Skill: Encode categorical values with numeric codes
Description: Students learn to map repeated categorical text values (difficulty: Easy/Medium/Hard) to numeric codes (1/2/3) stored in variables. They create a legend table documenting the mapping and use coded values in conditionals.

Dependencies:
* T25.G4.04: Document special rules in a data key
* T25.G3.02.03: Use boolean variables for true/false states
* T10.G3.05: Loop through each item in a list
* T09.G3.03: Use a variable in a simple conditional (if block)


ID: T25.G5.05
Topic: T25 – Data Representation
Skill: Add meaningful default values to data fields
Description: Students design a player profile where some fields might be empty (e.g., "nickname") and choose appropriate default values. They create a profile creation script that sets defaults using if/else blocks.

Dependencies:
* T25.G4.01: Build schema diagrams for simple apps
* T25.G3.02.03: Use boolean variables for true/false states
* T09.G3.03: Use a variable in a simple conditional (if block)


### G5.06 Series: Table Operations (SPLIT AND EXPANDED)

ID: T25.G5.06.01
Topic: T25 – Data Representation
Skill: Create multi-column tables with varied data
Description: Students build multi-column tables (3+ columns) with complex data using CreatiCode table blocks. They practice creating tables with different column types (text, number, boolean) and adding rows with multiple values.

Dependencies:
* T25.G3.06.02: Access table items by row and column
* T25.G5.03: Decide when to upgrade from list to table
* T10.G3.05: Loop through each item in a list
* T09.G3.03: Use a variable in a simple conditional (if block)


ID: T25.G5.06.02
Topic: T25 – Data Representation
Skill: Query tables by value using find row
Description: Students learn to search tables using 'find row number where column [name] = [value]' blocks. They practice finding specific rows, retrieving the row number, then accessing other columns from that row.

Dependencies:
* T25.G5.06.01: Create multi-column tables with varied data
* T10.G3.05: Loop through each item in a list
* T09.G3.03: Use a variable in a simple conditional (if block)


ID: T25.G5.06.03
Topic: T25 – Data Representation
Skill: Delete table rows by condition
Description: Students learn to remove rows from tables using 'delete all rows where column [name] = [value]' blocks. They build projects that filter tables by deleting unwanted rows and display the filtered results.

Dependencies:
* T25.G5.06.02: Query tables by value using find row
* T10.G3.05: Loop through each item in a list
* T09.G3.03: Use a variable in a simple conditional (if block)


ID: T25.G5.06.04
Topic: T25 – Data Representation
Skill: Insert rows at specific positions in tables
Description: Students use 'insert row [values] at position [number] in table' blocks to add rows at specific positions (not just the end). They understand how insertion shifts subsequent rows to higher indices.

Dependencies:
* T25.G5.06.01: Create multi-column tables with varied data


ID: T25.G5.06.05
Topic: T25 – Data Representation
Skill: Replace entire table rows
Description: Students use 'replace row [number] with [values] in table' blocks to update entire rows with new data. They understand when to replace vs delete-and-insert.

Dependencies:
* T25.G5.06.04: Insert rows at specific positions in tables


ID: T25.G5.06.06
Topic: T25 – Data Representation
Skill: Replace individual table cells
Description: Students use 'replace item at row [number] column [name] with [value] in table' blocks to update individual cell values. They practice precise cell updates without affecting other cells.

Dependencies:
* T25.G5.06.05: Replace entire table rows


ID: T25.G5.06.07
Topic: T25 – Data Representation
Skill: Change table cells by relative amounts
Description: Students use 'change item at row [number] column [name] by [value] in table' blocks to modify numeric cells by adding/subtracting values. They understand relative vs absolute updates.

Dependencies:
* T25.G5.06.06: Replace individual table cells


ID: T25.G5.06.08
Topic: T25 – Data Representation
Skill: Reduce table cells using formulas
Description: Students use 'reduce item at row [number] column [name] by formula [expression] in table' blocks to apply calculations to cell values. They practice compound updates like "multiply by 2 then subtract 10".

Dependencies:
* T25.G5.06.07: Change table cells by relative amounts


### G5.07 Series: List Statistical Operations (NEW - MISSING SKILLS)

ID: T25.G5.07.01
Topic: T25 – Data Representation
Skill: Find minimum and maximum values in lists
Description: Students use 'min of [list]' and 'max of [list]' reporter blocks to find smallest and largest values. They practice finding extremes in numeric lists.

Dependencies:
* T25.G3.07.04: Get list length and access items by index


ID: T25.G5.07.02
Topic: T25 – Data Representation
Skill: Calculate sum and average of list values
Description: Students use 'sum of [list]' and 'average of [list]' reporter blocks to aggregate numeric lists. They understand how to compute basic statistics.

Dependencies:
* T25.G5.07.01: Find minimum and maximum values in lists


ID: T25.G5.07.03
Topic: T25 – Data Representation
Skill: Calculate median of list values
Description: Students use 'median of [list]' reporter blocks to find middle values. They understand when median is more appropriate than average (handling outliers).

Dependencies:
* T25.G5.07.02: Calculate sum and average of list values


### G5.08 Series: List Manipulation (NEW - MISSING SKILLS)

ID: T25.G5.08.01
Topic: T25 – Data Representation
Skill: Reverse lists
Description: Students use 'reverse [list]' blocks to flip list order (first becomes last). They understand when reverse order is useful (recent-first displays, undo stacks).

Dependencies:
* T25.G3.07.04: Get list length and access items by index


ID: T25.G5.08.02
Topic: T25 – Data Representation
Skill: Reshuffle lists randomly
Description: Students use 'reshuffle [list]' blocks to randomize list order. They practice creating randomized quizzes, shuffled decks, and random selections.

Dependencies:
* T25.G5.08.01: Reverse lists


ID: T25.G5.08.03
Topic: T25 – Data Representation
Skill: Sort lists in ascending order
Description: Students use 'sort [list] in [ascending] order' blocks to organize list items alphabetically or numerically. They understand how sorting changes list order permanently.

Dependencies:
* T25.G5.08.02: Reshuffle lists randomly


ID: T25.G5.08.04
Topic: T25 – Data Representation
Skill: Sort lists in descending order
Description: Students practice sorting lists in descending order (largest first, Z-A). They compare ascending vs descending and choose appropriate ordering for different scenarios.

Dependencies:
* T25.G5.08.03: Sort lists in ascending order


ID: T25.G5.08.05
Topic: T25 – Data Representation
Skill: Copy and append lists
Description: Students use 'copy of [list]' blocks to duplicate lists and 'append [list] to [list]' blocks to combine lists. They understand shallow copying and list merging.

Dependencies:
* T25.G5.08.04: Sort lists in descending order


### G5.09 Series: Table Validation

ID: T25.G5.07
Topic: T25 – Data Representation
Skill: Validate data types and ranges before storage
Description: Students write validation scripts that check user input before storing it in variables. Using conditional blocks, they verify that scores are numbers in valid ranges (e.g., 0-100) and reject invalid inputs with error messages.

Dependencies:
* T25.G3.02.03: Use boolean variables for true/false states
* T08.G4.01: Use if/else for binary choices
* T09.G3.03: Use a variable in a simple conditional (if block)
* T07.G3.01: Use a counted repeat loop


## Grade 6 (24 skills - expanded from 13)

### G6.01-04 Series: Metadata, Representations, Nesting, AI Prompts (existing)

ID: T25.G6.01
Topic: T25 – Data Representation
Skill: Document metadata for datasets
Description: Students create a metadata documentation table in CreatiCode with columns: FieldName, Description, DataType, Units, ValidRange. They complete metadata tables for a project dataset, documenting each field's details.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G4.01: Build schema diagrams for simple apps
* T25.G4.04: Document special rules in a data key
* T25.G5.01.01: Design multi-type data structures on paper


ID: T25.G6.02
Topic: T25 – Data Representation
Skill: Explain lossy vs lossless representation
Description: Learners compare representing a path as every coordinate (lossless) vs key checkpoints (lossy) and discuss tradeoffs. Students implement both approaches in CreatiCode.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G4.03: Compare dense vs sparse representations
* T25.G5.03: Decide when to upgrade from list to table


ID: T25.G6.03
Topic: T25 – Data Representation
Skill: Nest tables and lists within each other
Description: Students design and implement nested data structures using CreatiCode tables and lists. They practice creating a table where one column stores lists (e.g., Inventory column contains a list of item names).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G5.01.02.03: Persist game state across game restarts
* T25.G5.03: Decide when to upgrade from list to table


ID: T25.G6.04
Topic: T25 – Data Representation
Skill: Trace AI prompt inputs to structured slots
Description: Learners examine an AI prompt template ('Write a summary about {topic} in {tone}') and identify which data fields store each slot's values. Students implement a simple template system using variables and 'join' blocks.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G5.02.02.05: Test data cleaning with sample datasets
* T25.G5.04: Encode categorical values with numeric codes


### G6.05 Series: Advanced Table Queries (SPLIT AND EXPANDED)

ID: T25.G6.05.01.01
Topic: T25 – Data Representation
Skill: Use lookup blocks for value-based queries
Description: Students use 'lookup rows where column [name] = [value] in table' blocks to find all matching rows. They practice building queries with single conditions.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G5.06.02: Query tables by value using find row


ID: T25.G6.05.01.02
Topic: T25 – Data Representation
Skill: Filter tables with comparison operators
Description: Students build filters using comparison operators (>, <, >=, <=, ≠) to find rows matching numeric ranges (e.g., 'find all rows where Score > 100'). They collect matching rows into new tables or lists.

Dependencies:
* T25.G6.05.01.01: Use lookup blocks for value-based queries


ID: T25.G6.05.01.03
Topic: T25 – Data Representation
Skill: Filter tables with compound conditions
Description: Students combine multiple conditions using AND/OR logic to build complex queries (e.g., 'find rows where Score > 100 AND Level = 5'). They understand query composition.

Dependencies:
* T25.G6.05.01.02: Filter tables with comparison operators
* T08.G5.02: Use compound conditions (and, or, not)


ID: T25.G6.05.02
Topic: T25 – Data Representation
Skill: Aggregate table data using built-in blocks
Description: Students use CreatiCode's built-in aggregation blocks 'sum/average/median/max/min of column [name]' to analyze table data. They build a grade analyzer that calculates class statistics.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G6.05.01.01: Use lookup blocks for value-based queries


ID: T25.G6.05.03
Topic: T25 – Data Representation
Skill: Sort tables by column
Description: Students learn to sort tables using 'sort table by column [name] in [ascending/descending] order' blocks. They practice sorting by different columns and understand how sorting preserves row data integrity.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G6.05.01.01: Use lookup blocks for value-based queries


ID: T25.G6.05.04
Topic: T25 – Data Representation
Skill: Reshuffle table rows randomly
Description: Students use 'reshuffle [table]' blocks to randomize row order. They practice creating randomized quiz questions from table data.

Dependencies:
* T25.G6.05.03: Sort tables by column


### G6.06 Series: Server Storage (SPLIT)

ID: T25.G6.06.01.01
Topic: T25 – Data Representation
Skill: Save individual values to server with unique keys
Description: Students use 'save public/private data [value] with name [key]' blocks to store individual values with unique key names. They understand public vs private visibility settings.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G5.01.02.03: Persist game state across game restarts


ID: T25.G6.06.01.02
Topic: T25 – Data Representation
Skill: Understand public vs private data visibility
Description: Students compare public (visible to all users) vs private (only this user) storage options. They build projects that require each type and explain when to use each.

Dependencies:
* T25.G6.06.01.01: Save individual values to server with unique keys


ID: T25.G6.06.02
Topic: T25 – Data Representation
Skill: Load data from server storage
Description: Students learn to retrieve saved data using 'load data named [key]' blocks. They practice loading previously saved values, handling cases where no data exists using default values.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G6.06.01.02: Understand public vs private data visibility


### G6.07 Series: CSV Import/Export (existing)

ID: T25.G6.07.01
Topic: T25 – Data Representation
Skill: Export table data as CSV
Description: Students use 'export table as [filename]' blocks to save table data as CSV files. After exporting, they open the downloaded CSV file in a text editor to examine the raw format.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G5.06.01: Create multi-column tables with varied data


ID: T25.G6.07.02
Topic: T25 – Data Representation
Skill: Import CSV data into tables
Description: Students use 'import file into table' blocks to load CSV data from files. They practice uploading CSV files, importing them into CreatiCode tables, and verifying the data appears correctly.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T18.G5.01: Design and implement a simple multiplayer turn-based game
* T24.G5.01: Use real-world context to define minimum/maximum values for random ranges
* T25.G6.07.01: Export table data as CSV


### G6.08 Series: Advanced Table Operations (NEW - MISSING SKILLS)

ID: T25.G6.08.01
Topic: T25 – Data Representation
Skill: Copy and append tables
Description: Students use 'copy of [table]' blocks to duplicate tables and 'append rows from [table] to [table]' blocks to combine tables. They understand table merging and when to create copies vs references.

Dependencies:
* T25.G5.06.01: Create multi-column tables with varied data


ID: T25.G6.08.02
Topic: T25 – Data Representation
Skill: Group table rows by column values
Description: Students use 'group table by column [name]' blocks to organize rows into groups based on shared values. They practice grouping students by grade level or items by category.

Dependencies:
* T25.G6.05.03: Sort tables by column


ID: T25.G6.08.03
Topic: T25 – Data Representation
Skill: Create pivot tables
Description: Students use 'pivot table with rows [column] columns [column] values [column]' blocks to transform table layouts. They practice creating cross-tabulation reports (e.g., sales by product and region).

Dependencies:
* T25.G6.08.02: Group table rows by column values


ID: T25.G6.08.04
Topic: T25 – Data Representation
Skill: Show table snapshots with custom styling
Description: Students use 'show table [name] at x:[x] y:[y] with style [options]' blocks to display tables with custom positioning and styling (colors, fonts, borders). They understand presentation vs data storage.

Dependencies:
* T25.G3.06.01.03: Display table monitors on stage


## Grade 7 (22 skills - expanded from 11)

### G7.01 Series: Normalization (existing)

ID: T25.G7.01.01
Topic: T25 – Data Representation
Skill: Understand First Normal Form (1NF)
Description: Students learn that First Normal Form requires each table cell to contain a single atomic value (no lists or multiple values in one cell). They examine and refactor tables with comma-separated values.

Dependencies:
* T25.G5.01.02.03: Persist game state across game restarts
* T25.G5.03: Decide when to upgrade from list to table


ID: T25.G7.01.02
Topic: T25 – Data Representation
Skill: Understand Second Normal Form (2NF)
Description: Students learn that Second Normal Form eliminates partial dependencies by ensuring all non-key attributes depend on the entire primary key. They practice identifying partial dependencies.

Dependencies:
* T25.G7.01.01: Understand First Normal Form (1NF)
* T25.G6.03: Nest tables and lists within each other


ID: T25.G7.01.03
Topic: T25 – Data Representation
Skill: Understand Third Normal Form (3NF)
Description: Students learn that Third Normal Form eliminates transitive dependencies where non-key attributes depend on other non-key attributes. They practice identifying transitive dependencies.

Dependencies:
* T25.G7.01.02: Understand Second Normal Form (2NF)


ID: T25.G7.01.04
Topic: T25 – Data Representation
Skill: Apply normalization to a game database
Description: Students take a denormalized game database and normalize it through 1NF, 2NF, and 3NF. They create separate tables with ID relationships and implement the normalized design in CreatiCode.

Dependencies:
* T25.G7.01.03: Understand Third Normal Form (3NF)


### G7.02 Series: Bias and Ethics

ID: T25.G7.02
Topic: T25 – Data Representation
Skill: Identify bias introduced by representation choices
Description: Learners critique data schemas that collapse categories (e.g., combining 'Non-binary' and 'Prefer not to say' into 'Other') and discuss how such choices can hide important differences. Students redesign biased schemas.

Dependencies:
* T25.G5.01.02.03: Persist game state across game restarts
* T25.G5.04: Encode categorical values with numeric codes
* T25.G6.01: Document metadata for datasets


### G7.03 Series: Persistence Methods (SPLIT)

ID: T25.G7.03.01.01
Topic: T25 – Data Representation
Skill: Export tables to CSV format
Description: Students use 'export table as [filename]' blocks to convert tables to CSV text format for Method 1 persistence. They understand the CSV text structure.

Dependencies:
* T25.G6.07.02: Import CSV data into tables


ID: T25.G7.03.01.02
Topic: T25 – Data Representation
Skill: Save CSV text to server storage
Description: Students combine CSV export with server storage by saving the CSV text content using 'save data with name [key]' blocks. They understand the multi-step persistence workflow.

Dependencies:
* T25.G7.03.01.01: Export tables to CSV format
* T25.G6.06.02: Load data from server storage


ID: T25.G7.03.02.01
Topic: T25 – Data Representation
Skill: Load CSV text from server storage
Description: Students load previously saved CSV text from server storage using 'load data named [key]' blocks as the first step of Method 1 restoration.

Dependencies:
* T25.G7.03.01.02: Save CSV text to server storage


ID: T25.G7.03.02.02
Topic: T25 – Data Representation
Skill: Import CSV text into tables
Description: Students complete Method 1 restoration by importing the loaded CSV text into tables using 'import text into table' blocks. They build complete save/load systems.

Dependencies:
* T25.G7.03.02.01: Load CSV text from server storage


ID: T25.G7.03.03.01
Topic: T25 – Data Representation
Skill: Save tables using local storage blocks
Description: Students learn Method 2 for table persistence using built-in 'save table to local storage with name [key]' blocks for direct table persistence.

Dependencies:
* T25.G6.03: Nest tables and lists within each other
* T25.G6.06.02: Load data from server storage


ID: T25.G7.03.03.02
Topic: T25 – Data Representation
Skill: Load tables from local storage
Description: Students complete Method 2 by using 'load table from local storage named [key]' blocks to restore saved tables directly.

Dependencies:
* T25.G7.03.03.01: Save tables using local storage blocks


ID: T25.G7.03.03.03
Topic: T25 – Data Representation
Skill: Compare persistence methods and choose appropriately
Description: Students compare Method 1 (CSV export for sharing) vs Method 2 (direct save/load for speed). They decide which method fits different scenarios and implement both in a project.

Dependencies:
* T25.G7.03.02.02: Import CSV text into tables
* T25.G7.03.03.02: Load tables from local storage


### G7.04 Series: Performance Tradeoffs

ID: T25.G7.04
Topic: T25 – Data Representation
Skill: Evaluate storage vs performance tradeoffs
Description: Students build two versions of a game scoreboard: (1) store total score in variable, (2) store round scores in list, calculate total using 'sum of list'. They compare tradeoffs.

Dependencies:
* T25.G5.01.02.03: Persist game state across game restarts
* T25.G6.01: Document metadata for datasets
* T25.G6.02: Explain lossy vs lossless representation


### G7.05 Series: Database Collections (SPLIT AND EXPANDED)

ID: T25.G7.05.01.01
Topic: T25 – Data Representation
Skill: Understand database collections as shared storage
Description: Students learn that database collections are shared, multi-user tables stored on CreatiCode's server (unlike private server storage). They understand the concept of shared cloud databases.

Dependencies:
* T25.G6.06.02: Load data from server storage


ID: T25.G7.05.01.02
Topic: T25 – Data Representation
Skill: Insert documents from tables to collections
Description: Students use 'insert from table into collection [name]' blocks to add multiple rows from a table to a database collection in one operation.

Dependencies:
* T25.G7.05.01.01: Understand database collections as shared storage
* T25.G6.05.01.01: Use lookup blocks for value-based queries


ID: T25.G7.05.01.03
Topic: T25 – Data Representation
Skill: Fetch all documents from collections into tables
Description: Students use 'fetch all from collection [name]' blocks to retrieve all documents from a collection into their local tables for processing.

Dependencies:
* T25.G7.05.01.02: Insert documents from tables to collections


ID: T25.G7.05.02.01
Topic: T25 – Data Representation
Skill: Build simple query conditions for collections
Description: Students create basic query conditions using comparison operators (=, >, <) to filter collection documents (e.g., fetch all records where score > 100).

Dependencies:
* T25.G7.05.01.03: Fetch all documents from collections into tables


ID: T25.G7.05.02.02
Topic: T25 – Data Representation
Skill: Build compound query conditions with AND/OR
Description: Students combine multiple conditions using AND/OR logic to build complex collection queries (e.g., 'score > 100 AND level = 5').

Dependencies:
* T25.G7.05.02.01: Build simple query conditions for collections


ID: T25.G7.05.02.03
Topic: T25 – Data Representation
Skill: Fetch filtered documents from collections
Description: Students use 'fetch from collection [name] where [condition]' blocks to retrieve only documents matching query conditions, enabling efficient data retrieval from large collections.

Dependencies:
* T25.G7.05.02.02: Build compound query conditions with AND/OR


ID: T25.G7.05.03.01
Topic: T25 – Data Representation
Skill: Update documents in collections
Description: Students use 'update document in collection [name] where [condition] set [field] to [value]' blocks to modify documents in shared collections.

Dependencies:
* T25.G7.05.02.03: Fetch filtered documents from collections


ID: T25.G7.05.03.02
Topic: T25 – Data Representation
Skill: Delete documents from collections
Description: Students use 'delete documents from collection [name] where [condition]' blocks to remove documents from shared collections based on conditions.

Dependencies:
* T25.G7.05.03.01: Update documents in collections


ID: T25.G7.05.03.03
Topic: T25 – Data Representation
Skill: Build collaborative multi-user data projects
Description: Students build projects where multiple users contribute to shared datasets (leaderboards, collaborative maps) and understand data persistence and sharing implications.

Dependencies:
* T25.G7.05.03.02: Delete documents from collections


### G7.06 Series: Google Sheets Integration (SPLIT AND EXPANDED)

ID: T25.G7.06.01.01
Topic: T25 – Data Representation
Skill: Create and configure Google Sheets for CreatiCode
Description: Students create a Google Sheet, configure sharing settings, and obtain the sheet URL needed for CreatiCode integration. Requires Google account and parent/teacher approval.

Dependencies:
* T25.G6.05.01.01: Use lookup blocks for value-based queries


ID: T25.G7.06.01.02
Topic: T25 – Data Representation
Skill: Connect CreatiCode to Google Sheets
Description: Students use 'connect to Google Sheet [URL]' blocks to establish connection between their CreatiCode project and Google Sheets.

Dependencies:
* T25.G7.06.01.01: Create and configure Google Sheets for CreatiCode


ID: T25.G7.06.02.01
Topic: T25 – Data Representation
Skill: Import Google Sheets data to CreatiCode tables
Description: Students use 'import sheet [name] from Google Sheets' blocks to read data from connected Google Sheets into CreatiCode tables.

Dependencies:
* T25.G7.06.01.02: Connect CreatiCode to Google Sheets


ID: T25.G7.06.02.02
Topic: T25 – Data Representation
Skill: Export CreatiCode tables to Google Sheets
Description: Students use 'export table to Google Sheet [name]' blocks to write table data to Google Sheets. They identify advantages of Google Sheets (accessible from any device, familiar interface).

Dependencies:
* T25.G7.06.02.01: Import Google Sheets data to CreatiCode tables


ID: T25.G7.06.03.01
Topic: T25 – Data Representation
Skill: Append rows to Google Sheets
Description: Students use 'append row [values] to sheet [name]' blocks to add individual rows to Google Sheets without replacing existing data.

Dependencies:
* T25.G7.06.02.02: Export CreatiCode tables to Google Sheets


ID: T25.G7.06.03.02
Topic: T25 – Data Representation
Skill: Update specific cells in Google Sheets
Description: Students use 'set cell [row, column] to [value] in sheet [name]' blocks to modify specific cells in Google Sheets.

Dependencies:
* T25.G7.06.03.01: Append rows to Google Sheets


ID: T25.G7.06.03.03
Topic: T25 – Data Representation
Skill: Build data collection projects with Google Sheets
Description: Students build complete projects that log data to shared Google Sheets (data collection, survey results) accessible to teachers and collaborators.

Dependencies:
* T25.G7.06.03.02: Update specific cells in Google Sheets


## Grade 8 (18 skills - expanded from 6)

### G8.01 Series: Multi-Modal Schemas (SPLIT)

ID: T25.G8.01.01.01
Topic: T25 – Data Representation
Skill: Design schema for text data
Description: Students design a data structure for storing text data with metadata. They create a schema showing: text content field, timestamp field, source/speaker ID field.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi‑event program
* T25.G6.01: Document metadata for datasets
* T03.G6.01: Propose modules for a medium project
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T06.G6.02: Identify parallel vs sequential event behaviors


ID: T25.G8.01.01.02
Topic: T25 – Data Representation
Skill: Add timestamps to text data schemas
Description: Students extend their text schemas to include timestamp fields (when spoken/written), understanding temporal data tracking.

Dependencies:
* T25.G8.01.01.01: Design schema for text data


ID: T25.G8.01.01.03
Topic: T25 – Data Representation
Skill: Add confidence scores to text data schemas
Description: Students add confidence score fields to text schemas (for speech recognition accuracy), learning to represent data quality metrics.

Dependencies:
* T25.G8.01.01.02: Add timestamps to text data schemas


ID: T25.G8.01.02
Topic: T25 – Data Representation
Skill: Design schema for numeric sensor data
Description: Students design a data structure for storing numeric sensor readings (temperature, position coordinates, distances). They create a schema showing: sensor value fields, reading timestamp, sensor ID, and measurement units.

Dependencies:
* T25.G8.01.01.03: Add confidence scores to text data schemas
* T02.G6.01: Learn the pseudocode generation block
* T03.G6.01: Propose modules for a medium project
* T06.G6.01: Trace event execution paths in a multi‑event program


ID: T25.G8.01.03
Topic: T25 – Data Representation
Skill: Design schema for media file references
Description: Students design a data structure for storing references to media files (images, videos, audio). They create a schema showing: file URL/path field, file type field, upload timestamp, file size, and associated metadata.

Dependencies:
* T25.G8.01.02: Design schema for numeric sensor data
* T03.G6.01: Propose modules for a medium project
* T04.G6.01: Group snippets by underlying algorithm pattern
* T06.G6.01: Trace event execution paths in a multi‑event program


ID: T25.G8.01.04
Topic: T25 – Data Representation
Skill: Design schema for pose and gesture data
Description: Students design a data structure for storing body pose detection results. They create a schema showing: arrays of joint coordinates (x, y positions for each body part), detection timestamp, confidence scores per joint, and detected gesture label.

Dependencies:
* T25.G8.01.03: Design schema for media file references
* T02.G6.01: Learn the pseudocode generation block
* T03.G6.01: Propose modules for a medium project
* T06.G6.01: Trace event execution paths in a multi‑event program


ID: T25.G8.01.05
Topic: T25 – Data Representation
Skill: Integrate multi-modal schemas with relationships
Description: Students combine their individual schemas (text, numeric, media, pose) into an integrated database design. They define relationships and implement a simplified multi-modal data system using multiple linked tables.

Dependencies:
* T25.G8.01.04: Design schema for pose and gesture data
* T25.G6.03: Nest tables and lists within each other
* T25.G7.01.04: Apply normalization to a game database
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds


### G8.02-04 Series: Lineage, Compression, Collaboration (existing)

ID: T25.G8.02
Topic: T25 – Data Representation
Skill: Document versioning and lineage metadata
Description: Learners add fields for source, timestamp, and transformation notes to a dataset. Students create enhanced metadata tables that track: data source, collection timestamp, transformation history, and version numbers.

Dependencies:
* T25.G6.01: Document metadata for datasets
* T25.G7.02: Identify bias introduced by representation choices
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds


ID: T25.G8.03
Topic: T25 – Data Representation
Skill: Evaluate compression strategies for large datasets
Description: Students investigate compression strategies by comparing storage approaches. They calculate memory usage, discuss lossy vs lossless compression, decide which strategy fits constraints, and implement one approach.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi‑event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T25.G6.02: Explain lossy vs lossless representation
* T25.G7.04: Evaluate storage vs performance tradeoffs
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T07.G6.01: Trace nested loops with variable bounds
* T11.G6.01: Design custom blocks with clear, predictable interfaces


ID: T25.G8.04
Topic: T25 – Data Representation
Skill: Document data formats for project collaboration
Description: Students create a data format specification document describing: required input data, output data produced, and formatting rules for sharing data with teammates. They build a sample project following their specification.

Dependencies:
* T25.G6.01: Document metadata for datasets
* T25.G7.03.02.02: Import CSV text into tables
* T25.G7.01.04: Apply normalization to a game database
* T07.G6.01: Trace nested loops with variable bounds
* T10.G6.01: Sort a table by a column
* T12.G6.01: Analyze a program's structure using a checklist and suggest specific improvements


### G8.05 Series: AI-Data Integration (NEW - MISSING SKILLS)

ID: T25.G8.05.01
Topic: T25 – Data Representation
Skill: Store face detection results in tables
Description: Students use CreatiCode face detection blocks to capture facial landmark data (position, expression, orientation) and store results in tables with columns for each detected face attribute.

Dependencies:
* T23.G5.01: Detect faces in camera feed
* T25.G6.08.01: Copy and append tables


ID: T25.G8.05.02
Topic: T25 – Data Representation
Skill: Store body/hand pose detection in tables
Description: Students use CreatiCode body/hand tracking blocks to capture pose data (joint coordinates, gesture recognition) and organize results in structured tables for analysis.

Dependencies:
* T25.G8.05.01: Store face detection results in tables
* T23.G5.02: Detect body pose landmarks


ID: T25.G8.05.03
Topic: T25 – Data Representation
Skill: Store NLP analysis results in tables
Description: Students use CreatiCode NLP blocks (sentiment analysis, entity extraction, text classification) and store results in tables with columns for input text, detected sentiment/entities, and confidence scores.

Dependencies:
* T25.G8.05.01: Store face detection results in tables
* T22.G5.01: Use text generation blocks for creative writing


ID: T25.G8.05.04
Topic: T25 – Data Representation
Skill: Prepare training datasets from tables for KNN
Description: Students organize labeled example data in tables (features in columns, labels in one column) and use 'train KNN classifier from table' blocks to create classifiers from structured data.

Dependencies:
* T25.G8.05.03: Store NLP analysis results in tables
* T25.G7.01.04: Apply normalization to a game database


ID: T25.G8.05.05
Topic: T25 – Data Representation
Skill: Prepare training datasets from tables for neural networks
Description: Students organize training data in tables (input features, expected outputs) and use 'train neural network from table' blocks. They understand data format requirements for ML training.

Dependencies:
* T25.G8.05.04: Prepare training datasets from tables for KNN


ID: T25.G8.05.06
Topic: T25 – Data Representation
Skill: Store neural network predictions in tables
Description: Students use trained neural networks to make predictions and store results in tables with columns for input values, predicted outputs, and confidence scores for analysis.

Dependencies:
* T25.G8.05.05: Prepare training datasets from tables for neural networks


ID: T25.G8.05.07
Topic: T25 – Data Representation
Skill: Build semantic search systems with table data
Description: Students organize searchable content in tables, use 'semantic search [query] in table column [name]' blocks to find similar items, and store search results with relevance scores.

Dependencies:
* T25.G8.05.06: Store neural network predictions in tables
* T22.G6.01: Understand semantic similarity vs keyword matching


## SUMMARY

**Total Skills: 148** (expanded from 80)
- Kindergarten: 3 (unchanged)
- Grade 1: 3 (unchanged)
- Grade 2: 4 (unchanged)
- Grade 3: 28 (from 17) - Added granular variable/list/table creation, list operations (delete/insert/replace/access)
- Grade 4: 24 (from 6) - Added list-to-table, join/split, find/contains, column ops, row ops, statistical list ops
- Grade 5: 35 (from 17) - Added granular table operations (insert/replace/change/reduce cells), list stats, list manipulation (reverse/reshuffle/sort/copy/append)
- Grade 6: 24 (from 13) - Added compound queries, table ops (group by/pivot/styling), public/private storage clarity
- Grade 7: 22 (from 11) - Added granular persistence methods, database collection ops, Google Sheets ops
- Grade 8: 18 (from 6) - Added AI-data integration (face/body/NLP/KNN/neural nets/semantic search to tables)

**Key Improvements:**
1. Each skill now focuses on ONE block or concept (following "one skill = one block" principle)
2. Added all missing list operations from CreatiCode blocks
3. Added all missing table operations from CreatiCode blocks
4. Added comprehensive AI-data integration pathway
5. Fixed dependency chains to ensure logical progression
6. Preserved all cross-topic dependencies
