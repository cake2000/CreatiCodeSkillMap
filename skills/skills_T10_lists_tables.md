# T10 – Lists, Tables & Structured Data in Programs: K–8 Skill List (Draft v1)

Topic reference: `T10 Lists, Tables & Structured Data in Programs` in `domains_topics_overview.md`
Domain: Programming (D2) & Data and Analysis (D3) · CSTA focus: PRO‑DH, DAA‑DF, DAA‑DP, DAA‑DI (with links to PRO‑PF, PRO‑TR)

Each skill below has:

- a stable **ID** (`T10.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Grade K introduces the concept of sequences and simple collections of objects in a concrete, hands‑on way—no formal lists yet, but building the foundation for understanding "a group of things."

### T10.GK.01 – Sort objects by a property

- **Short name:** Sort items into groups
- **Description:** Students arrange physical objects (or pictures) by a visible property (e.g., color, size, shape) and describe what makes each group the same. This builds the idea that data can be organized and categorized.
- **Challenge format:** Concept, interactive activity. A CreatiCode project displays or presents pictures of items (e.g., fruits, toys); students drag them into labeled groups (color baskets, size piles) or choose which group an item belongs to. Auto‑grading checks correct category assignments.
- **CSTA:** EK‑DAA‑DF‑01 (understanding data collection and organization).

### T10.GK.02 – Count items in a collection

- **Short name:** Count how many items are in a group
- **Description:** Students count members of a simple set (e.g., "how many red apples?" or "how many animals?") and communicate the total, connecting counting with basic data aggregation.
- **Challenge format:** Concept, interactive item. A CreatiCode project shows a collection of objects on screen; students count and enter or select the number. Auto‑grading validates the count against the displayed items.
- **CSTA:** EK‑DAA‑DF‑01.

### T10.GK.03 – Recognize a sequence of items

- **Short name:** Find the pattern in a list
- **Description:** Students identify a repeating or ordered sequence of items (e.g., red-blue-red-blue or Monday-Tuesday-Wednesday-Monday) and describe or continue the pattern, building awareness that ordered collections follow rules.
- **Challenge format:** Concept, pattern continuation. A row of picture tiles shows a sequence; students identify the pattern type or drag the next item(s) to complete it. Auto‑grading compares chosen/extended sequence to correct continuation.
- **CSTA:** EK‑ALG‑AF‑01 (pattern recognition, early step toward list structure).

---

## Grade 1

Grade 1 extends sequence awareness and introduces the notion of "a list of things to do" or simple inventories, still primarily through concrete examples.

### T10.G1.01 – Record items in a shopping list or checklist

- **Short name:** Write down a list of items
- **Description:** Students create a simple list (e.g., "things to buy," "tasks to do") in a structured way, recognizing that a list is a collection of items in a chosen order.
- **Challenge format:** Concept and light coding, guided construction. A CreatiCode project has a label or text field where students type or are given sentence stems to record 3–4 items, one per line or in a simple table. Auto‑grading checks that at least the required number of items are recorded and formatted consistently.
- **CSTA:** E1‑DAA‑DF‑01 (understanding different data types and collections).

### T10.G1.02 – Arrange items in order (sorting)

- **Short name:** Put items in order
- **Description:** Students take a scrambled list or set of items and reorder them by a rule (e.g., alphabetically, by size, by date) and explain the ordering criterion.
- **Challenge format:** Concept, drag-to-order or multiple choice. CreatiCode displays items (pictures or text) out of order; students drag them into the correct sequence or select the correctly ordered list. Auto‑grading validates the order against the specified criterion.
- **CSTA:** E1‑DAA‑DF‑01, E1‑DAA‑DP (early data organization).

### T10.G1.03 – Find an item in a list

- **Short name:** Look for an item in a list
- **Description:** Students are given a list and search for a specific item (e.g., "Find 'apple' in the shopping list") or count how many times it appears, building the idea of querying or searching a collection.
- **Challenge format:** Concept, search task. CreatiCode displays a short list (e.g., grocery items, names); students identify the position or count occurrences of a target item. Auto‑grading checks the answer against the list.
- **CSTA:** E1‑DAA‑DI‑02 (data investigation and pattern recognition).

---

## Grade 2

Grade 2 introduces the formal *list* variable in CreatiCode, allowing students to create, add to, and remove items from structured data collections.

### T10.G2.01 – Create and add items to a list

- **Short name:** Build a list with code
- **Description:** Students create an empty list variable and add items to it one at a time (or in a loop) using the `add [item] to [list]` block, understanding lists as dynamic, growable containers.
- **Challenge format:** Coding, starter project. Provided: empty list and sprite with a `when green flag clicked` block. Students add 5–6 specific items to the list (e.g., fruits, colors, names). Auto‑grading checks that the correct items exist in the list after execution and that the add block is used correctly.
- **CSTA:** E2‑DAA‑DF‑01 (collecting and organizing data), E2‑PRO‑DH‑02.

### T10.G2.02 – Access and display items from a list

- **Short name:** Get an item from a list
- **Description:** Students retrieve a specific item from a list (e.g., the first item, a random item, the item at position 3) using `item [#] of [list]` and display or use it (e.g., have the sprite say it).
- **Challenge format:** Coding, starter project. Provided: a pre‑filled list. Students use `item [#] of [list]` to get and display items. Auto‑grading checks that the correct items are retrieved and displayed based on the indices used.
- **CSTA:** E2‑DAA‑DP (data processing and retrieval), E2‑PRO‑DH‑02.

### T10.G2.03 – Remove or replace items in a list

- **Short name:** Remove or change list items
- **Description:** Students modify a list by deleting an item at a position or replacing it with a new value, understanding that lists are mutable.
- **Challenge format:** Coding, starter project. Provided: a list with several items. Prompt: "Remove the item at position 2" or "Replace the color 'red' with 'blue'." Students use `delete [#] of [list]` or `replace item [#] of [list] with [value]`. Auto‑grading checks the final list contents.
- **CSTA:** E2‑DAA‑DP (modifying data), E2‑PRO‑DH‑02.

### T10.G2.04 – Check if a list contains an item

- **Short name:** Does the list have this item?
- **Description:** Students use the `[list] contains [item]?` reporter to check if an item is in a list and respond accordingly (e.g., with a conditional or by saying "found it" or "not found").
- **Challenge format:** Coding, starter project. Provided: a list and a target item. Students use the contains block in an `if` statement to report whether the item exists. Auto‑grading runs test cases with different lists and items and checks the conditional behavior.
- **CSTA:** E2‑DAA‑DI‑02 (investigating data with simple queries).

---

## Grade 3

Grade 3 deepens list manipulation with iteration and conditions, connecting lists to the looping concepts introduced in T07.

### T10.G3.01 – Loop through and process each item in a list

- **Short name:** Do something with each item in a list
- **Description:** Students use a `repeat` or `for each [item] in [list]` loop to iterate over all items in a list and perform an action on each (e.g., say each item, add them up, count specific ones).
- **Challenge format:** Coding, starter project. Provided: a list of numbers or words and a loop block stub. Students fill in the loop to perform a task (e.g., "Say each fruit in the list"). Auto‑grading checks that the loop iterates the correct number of times and that the action occurs for each item.
- **CSTA:** E3‑PRO‑PF‑01 (using loops), E3‑DAA‑DP (processing data via iteration).

### T10.G3.02 – Find and count items in a list with a condition

- **Short name:** Count items that match a rule
- **Description:** Students loop through a list and count items that satisfy a condition (e.g., "count how many numbers are greater than 5" or "count red items"), using a counter variable inside the loop.
- **Challenge format:** Coding, starter project. Provided: a list and a target condition. Students initialize a counter, loop through the list, check the condition for each item, and increment the counter if true. Auto‑grading checks the final count value.
- **CSTA:** E3‑DAA‑DP (processing and filtering data), E3‑DAA‑DI (investigating data patterns).

### T10.G3.03 – Sort a list by swapping items

- **Short name:** Arrange a list in order
- **Description:** Students implement a simple sorting algorithm (e.g., bubble sort or selection sort intuition) by repeatedly comparing adjacent items and swapping them if out of order, or by selecting the smallest/largest and moving it. This introduces algorithmic thinking about data organization.
- **Challenge format:** Coding, starter project or guided challenge. Provided: an unsorted list and pseudocode or block hints. Students implement swaps or comparisons to sort in ascending or descending order. Auto‑grading checks the final sorted order and may verify the number of comparisons (within reasonable bounds).
- **CSTA:** E3‑ALG‑AF‑01 (recognizing and implementing algorithms), E3‑DAA‑DP.

### T10.G3.04 – Search a list for a specific item (linear search)

- **Short name:** Find an item's position in a list
- **Description:** Students implement a simple linear search: loop through a list, compare each item to a target, and report the position or index when found (or "not found" if the loop completes).
- **Challenge format:** Coding, starter project. Provided: a list and a target value. Students use a loop with a counter to find the position. Auto‑grading runs test cases (item present at various positions, item not present) and checks the returned position.
- **CSTA:** E3‑DAA‑DI (investigating and finding patterns in data), MS‑PRO‑PF‑01 (loop-based algorithms).

---

## Grade 4

Grade 4 introduces nested loops and more complex list operations, including the early concept of parallel lists or structured data via multiple variables.

### T10.G4.01 – Use nested loops to process a 2D arrangement (rows and columns)

- **Short name:** Nested loops for a grid of items
- **Description:** Students use two nested loops to process a conceptual 2D arrangement represented as a list of lists (e.g., a seating chart or a simple game grid) or multiple parallel lists. They loop through rows (outer loop) and columns (inner loop) to access or modify items.
- **Challenge format:** Coding, starter project. Provided: a list representation of a grid (e.g., list of lists or a single flattened list with a width value). Prompt: "Mark all items in row 2" or "Count items in the left column." Students implement two nested loops with appropriate index math. Auto‑grading checks the final state or the count.
- **CSTA:** E4‑PRO‑PF‑01 (nested loops), E4‑DAA‑DP (processing 2D data).

### T10.G4.02 – Store and retrieve parallel list data

- **Short name:** Use multiple lists for related data
- **Description:** Students use two or more lists in parallel (e.g., names in one list, scores in another) and keep them synchronized by index. For example, "the player at index 2 in the names list has the score at index 2 in the scores list."
- **Challenge format:** Coding, starter project. Provided: two or more pre‑filled parallel lists. Students retrieve data by matching indices (e.g., "What score does Alice have?" requires finding her index in names and using it in scores). Auto‑grading validates the correct output by checking against reference data.
- **CSTA:** E4‑DAA‑DF (organizing data via multiple variables), E4‑PRO‑DH‑02.

### T10.G4.03 – Build a high score or leaderboard list

- **Short name:** Create a ranked list of scores
- **Description:** Students create a list of scores or rankings (possibly with names), insert new scores in the appropriate position to keep the list sorted, or use loops and conditionals to find the highest/lowest score.
- **Challenge format:** Coding, guided project. Starter code has a list of scores and a new score to add. Students either insert the new score in the correct position or re‑sort the list after adding. Auto‑grading checks the final sorted order.
- **CSTA:** E4‑DAA‑DP (organizing and processing data), E4‑DAA‑DI (analyzing and ranking data).

### T10.G4.04 – Filter or remove items from a list based on a condition

- **Short name:** Remove items that don't match a rule
- **Description:** Students loop through a list and delete items that don't satisfy a condition (e.g., "keep only items > 10" or "remove all 'broken' tools"), either by building a new filtered list or by modifying the original.
- **Challenge format:** Coding, starter project. Provided: a list of mixed items and a filter criterion. Students iterate and either add matching items to a new list or delete non‑matching items from the original. Auto‑grading checks the final filtered list.
- **CSTA:** E4‑DAA‑DP (filtering and cleaning data), E4‑PRO‑PF‑01.

---

## Grade 5

Grade 5 introduces the **CreatiCode table variable**, a structured 2D data type that can store rows and columns of diverse data. Lists are extended and used more creatively in algorithms and simulations.

### T10.G5.01 – Create and populate a table variable

- **Short name:** Build a table with rows and columns
- **Description:** Students create an empty table variable and add rows with multiple columns (e.g., using a "make table" or "add row" block), understanding that a table is a 2D structure where each row can have multiple attributes (like a spreadsheet or database record).
- **Challenge format:** Coding, starter project. Provided: an empty table. Prompt: "Create a table of student records with columns: Name, Grade, Score." Students add rows using a block that accepts a row data structure (or multiple add operations for each column). Auto‑grading checks the table dimensions and data.
- **CSTA:** E5‑DAA‑DF‑01 (collecting structured data), E5‑PRO‑DH‑02.

### T10.G5.02 – Access table cells by row and column

- **Short name:** Read data from a table cell
- **Description:** Students retrieve a value from a table using row and column indices (e.g., `item [row 2, column 3] of [table]` or equivalent) and use or display that value.
- **Challenge format:** Coding, starter project. Provided: a pre‑populated table. Prompt: "Get the score of the student in row 3." Students use the appropriate block to access `[row][column]` and store or say the value. Auto‑grading validates correct cell access.
- **CSTA:** E5‑DAA‑DP (processing structured data), E5‑PRO‑DH‑02.

### T10.G5.03 – Update or insert rows in a table

- **Short name:** Add or change rows in a table
- **Description:** Students modify a table by adding a new row (e.g., a new student record) or updating values in an existing row, maintaining the table structure.
- **Challenge format:** Coding, starter project. Provided: an existing table and new data to insert. Students add a row with all required columns or update specific cells in a row. Auto‑grading checks the final table state.
- **CSTA:** E5‑DAA‑DP (updating and managing structured data), E5‑PRO‑DH‑02.

### T10.G5.04 – Loop through table rows to compute aggregates

- **Short name:** Sum or average data from a table
- **Description:** Students use a loop to iterate through all rows of a table, accessing a specific column, and computing a total (sum), average, count, or max/min value.
- **Challenge format:** Coding, starter project with a table of numbers. Prompt: "Calculate the sum of all scores" or "Find the highest grade." Students loop through rows, access the target column, and update an accumulator. Auto‑grading checks the computed result.
- **CSTA:** E5‑DAA‑DP (aggregating data via loops), E5‑DAA‑DI (analyzing structured data).

### T10.G5.05 – Search and filter table data

- **Short name:** Find rows matching a condition
- **Description:** Students search a table for rows where a specific column matches a value or condition (e.g., "find all students with Grade = 'A'" or "find all scores > 80"), and return the matching row(s).
- **Challenge format:** Coding, starter project. Provided: a table and a search criterion. Students loop through rows, check the condition, and either display matching rows or collect them in a results list/table. Auto‑grading validates the search results on multiple test cases.
- **CSTA:** E5‑DAA‑DI (investigating and filtering structured data), E5‑DAA‑DP.

---

## Grade 6

Grade 6 deepens table usage for real-world data analysis and introduces sorting and joining operations on structured datasets.

### T10.G6.01 – Sort a table by a column

- **Short name:** Arrange table rows by a column value
- **Description:** Students implement sorting logic that rearranges table rows based on values in a specified column (e.g., sort students by name or by score), preserving row integrity (all columns in a row stay together).
- **Challenge format:** Coding, starter project. Provided: a table and a column to sort by. Students implement a sort algorithm (using nested loops or a helper list of indices) that reorders rows by the target column. Auto‑grading checks the final row order.
- **CSTA:** MS‑DAA‑DP‑05 (organizing and processing data), MS‑PRO‑PF‑01 (using loops and comparisons).

### T10.G6.02 – Join or merge data from two tables

- **Short name:** Combine two related tables
- **Description:** Students combine data from two tables based on a matching key (e.g., matching student IDs to combine a scores table with a demographics table), or simply append rows from one table to another.
- **Challenge format:** Coding, starter project. Provided: two tables with a common column (e.g., student_id). Students use nested loops to find matching rows and copy data into a combined table or display combined results. Auto‑grading checks the result for correctness and integrity.
- **CSTA:** MS‑DAA‑DP (organizing and processing data), MS‑DAA‑DI (analyzing relationships in data).

### T10.G6.03 – Pivot or reshape table data

- **Short name:** Reorganize table structure
- **Description:** Students restructure table data (e.g., converting from "tall" format with many rows to "wide" format with fewer rows but more columns, or vice versa) to prepare for analysis or visualization.
- **Challenge format:** Coding, guided challenge. Provided: a table in one format and a description of the target format. Students write code to create a new table with the restructured layout. Auto‑grading checks the dimensions and values of the result.
- **CSTA:** MS‑DAA‑DP‑05 (reshaping data), MS‑DAA‑DF (organizing data).

### T10.G6.04 – Count, group, or aggregate data from a table

- **Short name:** Group rows and compute summaries
- **Description:** Students group table rows by a category column (e.g., grade level) and compute a summary statistic (count, sum, average) for each group, creating a summary table or report.
- **Challenge format:** Coding, starter project. Provided: a table with mixed data. Prompt: "Count how many students are in each grade" or "Sum sales by product type." Students loop, group by a key column, and accumulate counts or sums for each group. Auto‑grading validates group counts and summary values.
- **CSTA:** MS‑DAA‑DP‑05 (grouping and aggregating data), MS‑DAA‑DI‑08 (analyzing data relationships).

---

## Grade 7

Grade 7 uses tables and list-based data structures for realistic simulations, real-world data analysis, and algorithmic problem-solving involving complex data.

### T10.G7.01 – Design and populate a table for a real-world inventory or database

- **Short name:** Create a data model for real-world data
- **Description:** Students design the structure of a table (columns and data types) to model a real-world domain (e.g., a library catalog, game inventory, sports statistics) and populate it with realistic data.
- **Challenge format:** Design and coding. Prompt: "Design a table to store information about books in a library. Include at least: ISBN, Title, Author, Year, Available Copies." Students determine columns, create the table, and add sample rows. Auto‑grading checks column names/types (via description or data) and validates that several rows are present.
- **CSTA:** MS‑DAA‑DF‑04 (creating metadata and data structures), MS‑PRO‑DH‑04.

### T10.G7.02 – Analyze a dataset to find patterns or outliers

- **Short name:** Investigate table data for insights
- **Description:** Students examine a table of data and use code to find patterns (e.g., the most common value, a trend over time) or identify outliers (unusual values). They may create summary statistics or visualizations.
- **Challenge format:** Coding, data analysis project. Provided: a table with real or realistic data. Prompt: "Find the highest and lowest values in the Score column" or "Identify any scores that are much higher than average." Students loop, compare, and report findings. Auto‑grading validates the identified patterns or outliers.
- **CSTA:** MS‑DAA‑DI‑08 (identifying relationships in data), MS‑DAA‑DI‑09 (making classifications from data patterns).

### T10.G7.03 – Transform or clean data in a table using loops and conditions

- **Short name:** Clean and preprocess table data
- **Description:** Students perform data cleaning operations: remove rows with missing values, standardize formats (e.g., uppercase names), fix errors, or handle special cases—preparing raw data for analysis.
- **Challenge format:** Coding, data preprocessing task. Provided: a "messy" table with inconsistencies (missing values, varied case, obvious errors). Students write code to iterate and fix issues, creating a clean version. Auto‑grading compares the cleaned result to a reference dataset.
- **CSTA:** MS‑DAA‑DP‑07 (identifying and fixing errors in data), MS‑DAA‑DP‑06 (manipulating data).

### T10.G7.04 – Use nested loops to analyze relationships between two datasets

- **Short name:** Compare data from multiple tables
- **Description:** Students write nested loops to compare or correlate data from two tables (e.g., matching purchases to customer profiles, checking for correlations in sensor readings), identifying connections or anomalies.
- **Challenge format:** Coding, analytical challenge. Provided: two related tables. Prompt: "For each customer, show their total purchases" or "Find any products that appear in both tables." Students use nested loops to match and analyze. Auto‑grading validates the results.
- **CSTA:** MS‑DAA‑DP (processing structured data), MS‑DAA‑DI‑09 (analyzing relationships).

---

## Grade 8

Grade 8 applies lists and tables to complex algorithms, simulations, and data-driven decision-making—bridging toward high school computer science.

### T10.G8.01 – Implement a data structure using lists (simple version of array of records)

- **Short name:** Build a data structure with lists
- **Description:** Students implement a simple record or struct-like behavior using multiple parallel lists or a list of lists, simulating how professional code organizes complex data.
- **Challenge format:** Coding, algorithmic challenge. Prompt: "Create a character system for a game where each character has a name, health, and level. Use lists to store this data." Students use parallel lists or nested lists and write accessor functions to get character stats. Auto‑grading validates data integrity and accessor correctness.
- **CSTA:** MS‑PRO‑DH‑04 (using appropriate data structures).

### T10.G8.02 – Implement a sorting algorithm (bubble sort or selection sort)

- **Short name:** Write a sorting algorithm
- **Description:** Students implement a complete sorting algorithm (not just swap intuition, but the full loop logic) to sort a list or table by a numeric or alphabetic criterion, understanding algorithmic complexity informally (e.g., "this takes many comparisons").
- **Challenge format:** Coding, algorithmic challenge. Provided: an unsorted list and pseudocode or algorithm description. Students implement the full algorithm with nested loops and comparisons. Auto‑grading checks the final sorted result and runs tests on various input sizes to verify correctness.
- **CSTA:** MS‑ALG‑AF‑02 (analyzing and designing algorithms), MS‑PRO‑PF‑01.

### T10.G8.03 – Build a simulation using list-based state

- **Short name:** Simulate a system with list data
- **Description:** Students create a simulation (e.g., a game, a population model, a traffic system) where entities and their properties are stored in lists or tables, and the simulation loop reads/updates this data each frame.
- **Challenge format:** Coding, creative project with auto-checks. Prompt: "Build a simple ecosystem simulation where creatures are stored in a list, each with x, y position and energy. Move and update creatures each frame." Students maintain the data structure and implement update logic. Auto‑grading checks that entities are updated, moved, or behave over multiple frames.
- **CSTA:** MS‑PRO‑PF‑01 (implementing algorithms and simulations), MS‑DAA‑DP (processing state data).

### T10.G8.04 – Query and report statistics from a complex dataset

- **Short name:** Analyze a real dataset with code
- **Description:** Students load or are provided a realistic multi-column table (e.g., weather data, sports statistics, survey results) and write code to compute requested statistics: means, medians, percentiles, counts by category, trends, or comparisons.
- **Challenge format:** Coding, data analysis project. Provided: a real-world dataset in a table. Prompt: "Calculate the average temperature by month" or "Find the percentile rank of each student's score." Students write loops and accumulator logic to compute results. Auto‑grading validates computed statistics.
- **CSTA:** MS‑DAA‑DI‑08 (analyzing data to identify patterns), MS‑DAA‑DP‑05 (processing and aggregating data).

### T10.G8.05 – Model real-world relationships using table joins or lookups

- **Short name:** Manage related data in a program
- **Description:** Students use lists or tables to model entities and relationships (e.g., students with associated grades, orders with associated items), and write code to perform lookups or join operations to answer queries (e.g., "What grades does student X have?").
- **Challenge format:** Coding, data modeling project. Provided: two or more related tables. Prompt: "Build a system that allows looking up a student by ID and returning all their grades." Students implement lookup/join logic to retrieve related data. Auto‑grading runs queries and checks the results.
- **CSTA:** MS‑PRO‑DH‑04 (using data structures to represent relationships), MS‑DAA‑DI‑09 (analyzing complex datasets).

