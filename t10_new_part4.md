## GRADE 7 (33 skills)

ID: T10.G7.01
Topic: T10 – Lists & Tables
Skill: Design data flow for external data (import → validate → transform → use)
Description: Students learn to design a systematic data processing workflow when working with external data sources (CSV files, Google Sheets, APIs). They map out the four-stage pipeline: (1) Import: load data into a table using import blocks, (2) Validate: check for missing values, correct data types, reasonable ranges, (3) Transform: clean text (trim, standardize case), convert formats, compute derived columns, (4) Use: filter, sort, aggregate, or visualize the cleaned data. Students sketch this flow on paper before coding, identifying what validation checks are needed (e.g., ages should be 0-120, dates should match format) and what transformations are required (e.g., convert state abbreviations to full names). This pipeline thinking skill prepares students for real-world data work where raw data is messy and must be processed systematically before use, preventing "garbage in, garbage out" problems.
Dependencies:
* T10.G6.02: Filter table rows based on a condition
* T10.G5.06: Update a cell value in a table
* T10.G5.31: Verify table operations produce expected results

ID: T10.G7.02
Topic: T10 – Lists & Tables
Skill: Pivot or reshape table data
Description: Students use CreatiCode's `pivot [source] into [result] row groups [cols] columns [values] methods [methods]` block to reshape data from "long" format (many rows, few columns) to "wide" format (fewer rows, more columns) or vice versa, preparing data for different types of analysis.
Dependencies:
* T10.G6.05: Group data and compute aggregates per group

ID: T10.G7.03
Topic: T10 – Lists & Tables
Skill: Import external data into a table
Description: Students use the `import file into table [table]` block to load data from an external CSV file into a table. They understand file formats, handle the imported structure, and verify the data loaded correctly.
Dependencies:
* T10.G5.03: Create a table and add columns
* T10.G5.05: Read a cell value from a table

ID: T10.G7.04
Topic: T10 – Lists & Tables
Skill: Design a table schema for a real-world scenario
Description: Students design the structure of a table (what columns to include, what data types they hold) to model a real-world domain. They create a table with appropriate column names, justify their design choices (why these columns? what data type?), and demonstrate by populating the table with sample data that validates their design. Example domains: Library catalog (columns: title, author, ISBN, genre, available_copies); Game inventory (item_name, item_type, quantity, value, rarity); Sports statistics (player_name, team, position, points, assists).
Dependencies:
* T10.G5.03: Create a table and add columns

ID: T10.G7.05
Topic: T10 – Lists & Tables
Skill: Visualize table data with charts
Description: Students use CreatiCode's chart blocks like `draw [line/bar/pie] chart using columns [...] from table [table]` to create visual representations of their data. They also use `draw [type] chart using category column [col1] value column [col2] from table [table]` for categorical data visualization (e.g., bar chart of sales by region, pie chart of votes by candidate). They choose appropriate chart types: line charts for trends over time, bar charts for comparing categories, and pie charts for showing proportions of a whole.
Dependencies:
* T10.G5.10: Use built-in table aggregate blocks
* T10.G6.05: Group data and compute aggregates per group

ID: T10.G7.06
Topic: T10 – Lists & Tables
Skill: Clean and transform table data
Description: Students apply data cleaning transformations to improve data quality. Techniques include: trimming whitespace from text, standardizing text case (uppercase/lowercase), removing or replacing invalid characters, and standardizing formats (date formats, phone numbers). Students write loops to process each row and apply these transformations, verifying improvements by spot-checking cleaned values.
Dependencies:
* T10.G5.06: Update a cell value in a table
* T10.G5.09: Loop through table rows to compute aggregates
* T08.G5.02: Use compound conditions with and/or/not

ID: T10.G7.07
Topic: T10 – Lists & Tables
Skill: Validate and handle missing data in tables
Description: Students detect data quality issues: missing values (empty cells), out-of-range values (e.g., age > 150), and invalid data types (text in numeric columns). They implement validation rules and handle issues by replacing missing values with defaults (e.g., 0 or "N/A"), deleting invalid rows, or marking rows for manual review. Students report the count of issues found and fixed.
Dependencies:
* T10.G7.06: Clean and transform table data
* T10.G5.11: Delete a single row by index
* T08.G5.02: Use compound conditions with and/or/not

ID: T10.G7.08
Topic: T10 – Lists & Tables
Skill: Analyze a dataset to find patterns or outliers
Description: Students examine a table of data and write code to find patterns (most frequent value, trends over time) or identify outliers (values much larger/smaller than typical). They combine aggregates, sorting, and conditionals to discover insights and report their findings with supporting evidence from the data.
Dependencies:
* T10.G6.05: Group data and compute aggregates per group
* T10.G6.01: Sort a table by a column
* T08.G5.02: Use compound conditions with and/or/not

ID: T10.G7.09
Topic: T10 – Lists & Tables
Skill: Use regex patterns to find items in lists
Description: Students use regular expression patterns to find items in lists that match complex text patterns (e.g., "find all emails," "find all phone numbers," "find all codes starting with A"). They use CreatiCode's regex blocks to extract matching items into a new list and verify the pattern matches only intended items.
Dependencies:
* T10.G4.07: Filter items from a list based on a condition

ID: T10.G7.10
Topic: T10 – Lists & Tables
Skill: Read and write data with Google Sheets
Description: Students use `read from google sheet: url [url] sheet name [name] range [range] into table [table]` and `write into google sheet: url [url] sheet name [name] start cell [cell] from table [table]` to sync data with Google Sheets. They also use `list all sheets in google sheet at URL [url] into list [list]` to get names of all sheets in a spreadsheet for dynamic sheet selection. They learn to set up sharing, use proper URLs, and handle authentication.
Dependencies:
* T10.G7.03: Import external data into a table
* T10.G5.04: Add rows of data to a table

ID: T10.G7.11
Topic: T10 – Lists & Tables
Skill: Manage Google Sheets structure
Description: Students use `add sheet [name] to google sheet at URL [url]`, `remove sheet [name]`, `insert [n] columns/rows in sheet [name]`, `remove [n] columns/rows from sheet [name]`, and `clear sheet [name] in google sheet at URL [url]` to programmatically manage spreadsheet structure. They understand when to modify structure vs. data.
Dependencies:
* T10.G7.10: Read and write data with Google Sheets
* T10.G5.15: Add a column at a specific position

ID: T10.G7.12
Topic: T10 – Lists & Tables
Skill: Display formatted table snapshots
Description: Students use `show snapshot of table [table] from row (start) to (end) with style [style] [color]` to create professionally formatted table displays with styling and color themes. They use this for presenting data in projects, creating reports, or showing partial table views.
Dependencies:
* T10.G5.24: Show and hide table monitors
* T10.G7.05: Visualize table data with charts

ID: T10.G7.13
Topic: T10 – Lists & Tables
Skill: Export table data to a file
Description: Students use `export table [table] as [filename]` to save table data as a downloadable CSV file. They understand CSV format (comma-separated values), when to export data (sharing results, backup, analysis in other tools), and how file export complements data import.
Dependencies:
* T10.G7.03: Import external data into a table
* T10.G5.03: Create a table and add columns

ID: T10.G7.14
Topic: T10 – Lists & Tables
Skill: Save and load data to the cloud
Description: Students use `save table [table] to server as [dataname]` and `load [dataname] from server into table [table]` to store and retrieve table data on CreatiCode's cloud server. They understand this enables data persistence (save progress, reload later), multi-session projects, and simple data sharing without Google Sheets integration.
Dependencies:
* T10.G7.03: Import external data into a table
* T10.G7.10: Read and write data with Google Sheets

ID: T10.G7.15
Topic: T10 – Lists & Tables
Skill: Use AI to analyze table data
Description: Students use CreatiCode's AI blocks to ask questions about table data (e.g., "What are the key insights from this sales data?" or "Summarize the trends in this dataset"). Students formulate clear questions, interpret AI responses, and verify AI suggestions against actual data.
Dependencies:
* T10.G7.08: Analyze a dataset to find patterns or outliers
* T10.G5.10: Use built-in table aggregate blocks

ID: T10.G7.16
Topic: T10 – Lists & Tables
Skill: Implement stack operations (push and pop)
Description: Students implement stack behavior using a list: push (add to end), pop (remove and return last item), and peek (read first item without removing). They use `add [item] to [stack]` for push, `item (length of [stack]) of [stack]` with `delete (length of [stack]) of [stack]` for pop, and recognize LIFO (Last-In-First-Out) behavior. Applications include undo functionality (push each action, pop to undo), expression evaluation, and backtracking algorithms. Students trace through a sequence of push/pop operations and predict the stack state after each.
Dependencies:
* T10.G6.13: Implement queue operations (enqueue and dequeue)

ID: T10.G7.17
Topic: T10 – Lists & Tables
Skill: Use KNN classification with table data
Description: Students use CreatiCode's KNN (K-Nearest Neighbors) blocks to classify new data points based on existing labeled data stored in a table. They prepare training data in a table with feature columns and a label column, use the `add training data from table [table] features [cols] labels [col]` block, then classify new inputs using the trained model. Students experiment with different k values and observe how it affects classification accuracy. This introduces supervised machine learning concepts using familiar table data.
Dependencies:
* T10.G7.04: Design a table schema for a real-world scenario
* T10.G5.10: Use built-in table aggregate blocks

ID: T10.G7.18
Topic: T10 – Lists & Tables
Skill: Build a simple recommendation system using tables
Description: Students create a basic recommendation system using table data and similarity calculations. Given a table of users and their ratings/preferences (e.g., movie ratings, product reviews), students find similar users by comparing their ratings, then recommend items that similar users liked but the target user hasn't seen. They implement a simple similarity measure (count of matching ratings) and use table lookups to generate recommendations. This practical application combines table operations with real-world data analysis.
Dependencies:
* T10.G6.04: Use table lookup to find related data
* T10.G6.05: Group data and compute aggregates per group
* T10.G5.09: Loop through table rows to compute aggregates

ID: T10.G7.19
Topic: T10 – Lists & Tables
Skill: Debug table operations by logging intermediate states
Description: Students develop systematic debugging strategies for table programs: logging row/column values during loops using console output, checking boundary conditions (first row, last row, empty table), verifying column values match expected types, and using table snapshots to compare before/after states. Given a buggy table program, students add logging statements to trace execution, identify where values diverge from expectations, and fix the issue. This skill builds on list debugging (T10.G3.17) but addresses table-specific challenges like multi-column access patterns and row counting errors.
Dependencies:
* T10.G5.27: Debug table programs by tracing row and column access
* T10.G7.07: Validate and handle missing data in tables

ID: T10.G7.20
Topic: T10 – Lists & Tables
Skill: Insert and update database records from table data
Description: Students use CreatiCode's database blocks to persist table data beyond individual sessions. They use `insert from table [table] row from (start) to (end) into collection [collection]` to add records to a database collection, and `update collection [collection] from table [table]` to modify existing records. Students understand the difference between local tables (temporary, in memory) and database collections (persistent, shared), and design programs that sync data between tables and databases appropriately.
Dependencies:
* T10.G7.10: Read and write data with Google Sheets
* T10.G7.04: Design a table schema for a real-world scenario

ID: T10.G7.21
Topic: T10 – Lists & Tables
Skill: Query and filter database collections into tables
Description: Students use `fetch from collection [collection] into table [table] where <condition> limit (n) sort by (field) [order]` to retrieve database records matching specific criteria. They construct filter conditions, apply sorting, limit result counts for performance, and process the fetched data using table operations. This skill bridges the gap between simple table operations and real database querying, preparing students for SQL concepts.
Dependencies:
* T10.G7.20: Insert and update database records from table data
* T10.G6.02: Filter table rows based on a condition

ID: T10.G7.22
Topic: T10 – Lists & Tables
Skill: Document data schema decisions for future readers
Description: Students write documentation explaining their data schema design choices. For a table they've created, they document: (1) Purpose of each column and what values it can contain, (2) Relationships between columns if any, (3) Why they chose this structure over alternatives, (4) Example queries the table is designed to support. This communication skill is essential for team projects—others need to understand your data design to work with it. Students practice writing clear, concise documentation and review each other's documentation for clarity.
Dependencies:
* T10.G7.04: Design a table schema for a real-world scenario
* T10.G5.29: Compare tables vs parallel lists and justify choice

ID: T10.G7.23
Topic: T10 – Lists & Tables
Skill: Analyze static AI vision data in tables
Description: Students process static datasets captured from AI vision blocks (e.g., "run hand detection table"). Unlike real-time interaction, this skill focuses on post-processing: identifying specific gestures from recorded frames, calculating average positions, or detecting sequences. Students understand the table structure output by AI (rows for keypoints, columns for x/y/z/confidence) and write code to extract meaning from this raw geometric data.
Dependencies:
* T10.G7.04: Design a table schema for a real-world scenario
* T10.G5.09: Loop through table rows to compute aggregates
* T10.G6.02: Filter table rows based on a condition

ID: T10.G7.24
Topic: T10 – Lists & Tables
Skill: Build a data-driven quiz or flashcard system using tables
Description: Students design and implement a complete quiz or flashcard application using table data. They design a table with columns for questions, correct answers, optional wrong answers (for multiple choice), and possibly difficulty/category. They implement: (1) Loading questions from the table, (2) Randomly selecting questions, (3) Checking user answers against correct answers, (4) Tracking score, (5) Optionally tracking which questions were missed for review. This project integrates many table skills into a practical, reusable application. Students can extend it by importing their own question sets from CSV files.
Dependencies:
* T10.G7.03: Import external data into a table
* T10.G6.19: Select a random item from a list
* T10.G6.04: Use table lookup to find related data

ID: T10.G7.25
Topic: T10 – Lists & Tables
Skill: Optimize table operations for large datasets
Description: Students learn strategies to make table operations faster on larger datasets (100+ rows). Techniques: (1) Filter early to reduce rows before processing, (2) Use built-in aggregate blocks instead of manual loops when possible, (3) Avoid repeated lookups by caching results, (4) Limit display operations (don't show all 500 rows at once). Students compare performance of optimized vs. naive approaches using timer blocks and understand that algorithmic choices matter more as data grows. This prepares students for thinking about scalability in real-world applications.
Dependencies:
* T10.G7.08: Analyze a dataset to find patterns or outliers
* T10.G6.23: Implement a simple lookup cache with lists

ID: T10.G7.26
Topic: T10 – Lists & Tables
Skill: Debug data import errors and mismatched schemas
Description: Students learn to systematically troubleshoot problems when importing external data. Common issues include: file not found (check file path and sharing permissions), wrong delimiter (CSV uses commas, but file might use tabs or semicolons), column count mismatch (some rows have more/fewer columns than expected), encoding issues (special characters display wrong), and header row problems (data includes header row as first data row). Students use debugging strategies: (1) examine first few rows with table monitor to see what actually imported, (2) check column count and names, (3) verify expected data appears in correct columns, (4) test with small sample file first, (5) use text blocks to preview file contents before import. They practice with deliberately problematic files (wrong delimiter, missing columns, extra whitespace) and fix import settings or pre-process the data. This practical troubleshooting skill builds resilience when working with real external data.
Dependencies:
* T10.G7.03: Import external data into a table
* T10.G7.07: Validate and handle missing data in tables
* T10.G5.27: Debug table programs by tracing row and column access

ID: T10.G7.27
Topic: T10 – Lists & Tables
Skill: Store and retrieve AI conversation history in table
Description: Students use a table to store AI chatbot conversation history, enabling context-aware conversations and conversation review. Table structure: columns "Role" (user/assistant), "Message" (the text), and optionally "Timestamp." When the user sends a message, add a row with role="user". When AI responds, add a row with role="assistant". Students implement: (1) Display conversation history by looping through table rows, (2) Clear history to start a new conversation, (3) Export history for later review, (4) Optionally limit history length by deleting oldest rows when the table grows too large. This pattern is essential for building AI applications where context matters, and teaches students how professional chatbots maintain conversation state.
Dependencies:
* T10.G7.04: Design a table schema for a real-world scenario
* T10.G5.04: Add rows of data to a table
* T10.G5.11: Delete a single row by index

ID: T10.G7.28
Topic: T10 – Lists & Tables
Skill: Process streaming AI data updates into table
Description: Students learn to handle AI data that arrives continuously over time, updating a table with new information rather than replacing it. Examples: hand tracking updates hand position coordinates multiple times per second; body pose detection continuously provides joint positions; speech recognition might provide partial results before final text. Students implement: (1) Update existing rows when data changes (e.g., update hand position row), (2) Add new rows for new detections (e.g., a second hand appears), (3) Remove stale rows when data is no longer detected (e.g., hand leaves frame), (4) Handle the "update vs. add" decision by checking if a row for that entity exists. They use table operations within event loops to maintain real-time data tables. This streaming data pattern is essential for interactive AI applications.
Dependencies:
* T10.G7.23: Analyze static AI vision data in tables
* T10.G5.06: Update a cell value in a table
* T10.G5.08: Find which row contains a value

ID: T10.G7.29
Topic: T10 – Lists & Tables
Skill: Build data pipelines that feed into AI models
Description: Students design and implement complete data pipelines that prepare and feed data into AI models for analysis or prediction. The pipeline includes: (1) Data collection—gather data from user input, sensors, or imports into tables; (2) Data cleaning—remove invalid entries, fill missing values, standardize formats; (3) Feature preparation—extract or compute the specific columns/values the AI model needs; (4) AI invocation—pass prepared data to AI blocks (KNN classifier, semantic search, AI analysis); (5) Result processing—interpret AI output and take action. Students build a complete pipeline for one scenario, such as: collecting flower measurements into a table, cleaning the data, extracting features, running KNN classification, and displaying the predicted species. They document each pipeline stage and explain why each step is necessary. This end-to-end skill connects data structures with AI capabilities.
Dependencies:
* T10.G6.28: Design table schemas optimized for AI processing
* T10.G7.07: Validate and handle missing data in tables
* T10.G7.17: Use KNN classification with table data

ID: T10.G7.30
Topic: T10 – Lists & Tables
Skill: Implement circular buffer for streaming data
Description: Students implement a circular buffer (ring buffer) using a list to store a fixed-size window of recent data, which is essential for processing streaming data efficiently. Implementation: Create a list with fixed size (e.g., 10 elements), use a position variable that wraps around using modulo (when position > size, position = 1), overwrite the oldest data when adding new data. Operations: (1) Add new item at current position, advance position (wrapping), (2) Read recent N items by traversing backwards from position, (3) Calculate statistics on the buffer (moving average, recent max/min). Applications: storing last 10 sensor readings, keeping recent chat messages in memory, tracking last N mouse positions for smoothing. Students implement a circular buffer that stores the last 5 values, displaying them and computing their average. They compare this to the naive approach (delete oldest, add newest) which is slower. This advanced pattern is used in real systems for efficient streaming data handling.
Dependencies:
* T10.G7.28: Process streaming AI data updates into table
* T10.G3.28: Replace an item in a list
* T10.G4.19: Loop through list indices

ID: T10.G7.31
Topic: T10 – Lists & Tables
Skill: Trace insertion sort algorithm on paper before implementing
Description: Students trace the insertion sort algorithm on paper with a small list (5-6 items) before writing code. The algorithm works by building a sorted portion from left to right: start with the first item as the "sorted portion," take the next item from the unsorted portion, find where it belongs in the sorted portion, insert it there by shifting larger items right. Given [5, 2, 8, 1, 9], students trace: (1) Start: sorted=[5], unsorted=[2,8,1,9]; (2) Take 2, insert before 5: sorted=[2,5], unsorted=[8,1,9]; (3) Take 8, insert after 5: sorted=[2,5,8], unsorted=[1,9]; (4) Take 1, insert at start: sorted=[1,2,5,8], unsorted=[9]; (5) Take 9, insert at end: sorted=[1,2,5,8,9]. Students create a trace table showing the sorted/unsorted portions after each step and count how many shifts (item moves) were needed. They compare insertion sort to bubble sort: insertion sort builds sorted portion from left, bubble sort pushes largest items to right. Key insight: insertion sort performs well on nearly-sorted data because few shifts are needed. This prepares for G8 implementation.
Dependencies:
* T10.G4.31: Trace bubble sort algorithm on paper before implementing
* T10.G4.10: Swap two items in a list
* T10.G3.27: Insert an item at a specific position in a list

ID: T10.G7.32
Topic: T10 – Lists & Tables
Skill: Apply map operation to transform all list items (Functional Pattern)
Description: Students implement the "map" pattern—applying a transformation function to every item in a list, producing a new list with transformed values. Implementation: create a result list, loop through source list, apply transformation to each item, add transformed item to result. Examples: (1) Double all numbers: [1, 2, 3] → [2, 4, 6], (2) Convert names to uppercase: ["sam", "lia"] → ["SAM", "LIA"]. Students recognize the common pattern: "for each item, compute something and save it." This functional programming pattern is fundamental in modern languages and data processing pipelines. Students compare map to filter: map transforms all items (same count), filter selects some items (fewer count).
Dependencies:
* T10.G6.07: Remove duplicate items from a list
* T10.G3.09: Loop through each item in a list
* T10.G4.07: Filter items from a list based on a condition

ID: T10.G7.33
Topic: T10 – Lists & Tables
Skill: Apply reduce operation to aggregate list into single value (Functional Pattern)
Description: Students implement the "reduce" pattern—combining all list items into a single value using an accumulator. Implementation: initialize an accumulator, loop through list, combine each item with accumulator, return final accumulator value. Examples: (1) Sum: accumulator starts at 0, add each item → total, (2) Product: accumulator starts at 1, multiply each item → product, (3) Concatenate: accumulator starts at "", append each item → combined string. Students recognize the pattern: "start with initial value, combine each item, get final result." This functional programming pattern is powerful for aggregation. Students compare reduce to map: map produces a list, reduce produces a single value.
Dependencies:
* T10.G7.32: Apply map operation to transform all list items (Functional Pattern)
* T10.G5.10: Use built-in table aggregate blocks
* T10.G3.11: Count items in a list that match a condition

## GRADE 8 (33 skills)

ID: T10.G8.01
Topic: T10 – Lists & Tables
Skill: Use nested loops to compare data across two tables
Description: Students write nested loops to analyze relationships between two tables (e.g., matching orders to customers, finding common elements). The outer loop iterates through one table while the inner loop searches the other table for matches.
Dependencies:
* T07.G6.01: Trace nested loops with variable bounds
* T10.G6.04: Use table lookup to find related data

ID: T10.G8.02
Topic: T10 – Lists & Tables
Skill: Implement bubble sort algorithm step by step
Description: Students implement bubble sort by writing nested loops: the outer loop controls passes, the inner loop compares adjacent items and swaps if out of order. They trace through the algorithm to understand how items "bubble" to their correct positions.
Dependencies:
* T10.G6.16: Swap adjacent items based on comparison
* T07.G6.01: Trace nested loops with variable bounds

ID: T10.G8.03
Topic: T10 – Lists & Tables
Skill: Implement selection sort algorithm step by step
Description: Students implement selection sort by writing nested loops: the outer loop selects each position, the inner loop finds the minimum remaining element. They understand that selection sort makes fewer swaps than bubble sort.
Dependencies:
* T10.G8.02: Implement bubble sort algorithm step by step
* T10.G6.17: Find maximum in a sublist range

ID: T10.G8.04
Topic: T10 – Lists & Tables
Skill: Build a simulation using table-based state
Description: Students create a simulation (e.g., a game with multiple entities, a population model, an ecosystem) where entities and their properties are stored in a table. Each simulation step loops through rows to update values based on rules.
Dependencies:
* T10.G7.04: Design a table schema for a real-world scenario
* T10.G5.09: Loop through table rows to compute aggregates

ID: T10.G8.05
Topic: T10 – Lists & Tables
Skill: Query and report statistics from a complex dataset
Description: Students work with a realistic multi-column table (e.g., weather data, sports statistics, survey results) and write code to answer analytical questions: compute means, find percentiles, compare groups, identify trends, and format results as a report.
Dependencies:
* T10.G7.08: Analyze a dataset to find patterns or outliers
* T10.G6.01: Sort a table by a column

ID: T10.G8.06
Topic: T10 – Lists & Tables
Skill: Model relationships using multiple linked tables
Description: Students design and use multiple tables that reference each other (e.g., a Students table and a Grades table linked by student ID). They write code to perform lookups across tables to answer queries like "What are all grades for student X?"
Dependencies:
* T10.G8.01: Use nested loops to compare data across two tables
* T10.G7.04: Design a table schema for a real-world scenario

ID: T10.G8.07
Topic: T10 – Lists & Tables
Skill: Implement a hash table lookup using lists
Description: Students simulate a simple hash table by using a list where each position corresponds to a hash value computed using modulo operation (e.g., hash(key) = key mod list_length for numbers, or sum of character codes mod list_length for strings). They handle collisions using linear probing (check next positions) or chaining (store multiple items at one position using lists within lists). Implementation pattern: Use a list as the hash table, create a hash function using math operators and string blocks, use linear search as fallback for collisions, and compare performance to linear search to demonstrate the principle of constant-time lookup.
Dependencies:
* T10.G8.03: Implement selection sort algorithm step by step
* T10.G6.14: Use frequency counting with lists
* T09.G7.01: Compare computational efficiency of different approaches

ID: T10.G8.08
Topic: T10 – Lists & Tables
Skill: Trace binary search step by step before implementing
Description: Before implementing binary search, students trace through the algorithm manually to understand the divide-and-conquer strategy. Given a sorted list [2, 5, 8, 12, 15, 20, 25, 30, 35, 40] and target 20, they trace each step: (1) calculate middle position (length ÷ 2), (2) compare target to middle value, (3) eliminate half the search space (if target < middle, search left half; if target > middle, search right half; if equal, found), (4) repeat with new boundaries until found or search space is empty. Students track the changing search boundaries (low, high) and middle position at each iteration, counting how many steps binary search takes vs. linear search (which would check every item). This hands-on tracing reveals why binary search is O(log n) efficient and builds understanding before managing the complex nested conditional and loop structure in code.
Dependencies:
* T10.G6.30: Compare algorithm speed with different list sizes
* T10.G8.02: Implement bubble sort algorithm step by step

ID: T10.G8.09
Topic: T10 – Lists & Tables
Skill: Implement binary search on sorted lists
Description: Students implement binary search algorithm to find items in O(log n) time instead of O(n) linear search. They repeatedly divide the sorted list's search space in half: compare the middle element to the target, then search either the left half (if target is smaller) or right half (if target is larger). Students trace through the algorithm step-by-step, counting comparisons, and compare performance to linear search to demonstrate logarithmic efficiency gains. This introduces divide-and-conquer algorithmic thinking.
Dependencies:
* T10.G8.08: Trace binary search step by step before implementing
* T09.G7.01: Compare computational efficiency of different approaches

ID: T10.G8.10
Topic: T10 – Lists & Tables
Skill: Use two-pointer technique for list problems
Description: Students apply two-pointer techniques where pointers move from both ends toward the center to solve problems efficiently. Common patterns: Finding pairs that sum to a target value (one pointer at start, one at end, move based on comparison), removing duplicates from sorted lists (slow and fast pointers), or checking palindromes (compare from both ends). Students implement at least one two-pointer algorithm, trace pointer movements, and understand how this technique avoids nested loops for certain problems.
Dependencies:
* T10.G8.09: Implement binary search on sorted lists
* T09.G7.01: Compare computational efficiency of different approaches

ID: T10.G8.11
Topic: T10 – Lists & Tables
Skill: Apply sliding window algorithms
Description: Students use sliding window algorithms to efficiently process contiguous subarrays by maintaining a window that slides through the data. Common applications: finding maximum sum of k consecutive elements, longest substring without repeating characters, or moving averages. Implementation pattern: Initialize window with first k elements, slide window right by adding next element and removing leftmost element, track window state (sum, max, set of unique items), update result after each slide. Students understand how sliding window reduces O(n*k) to O(n) by reusing previous computations.
Dependencies:
* T10.G8.10: Use two-pointer technique for list problems
* T09.G7.01: Compare computational efficiency of different approaches

ID: T10.G8.12
Topic: T10 – Lists & Tables
Skill: Implement a priority queue using sorted insertion
Description: Students implement a priority queue where items are always retrieved in priority order (highest or lowest first). They maintain a sorted list by inserting new items at the correct position (binary search for position, then insert) rather than sorting after each insertion. Students compare this O(n) insertion with O(1) removal to naive approaches (O(1) insertion with O(n) search for removal). Applications include task schedulers, event-driven simulations, and Dijkstra's algorithm foundations.
Dependencies:
* T10.G8.09: Implement binary search on sorted lists
* T10.G6.13: Implement queue operations (enqueue and dequeue)

ID: T10.G8.13
Topic: T10 – Lists & Tables
Skill: Parse and process structured text into tables
Description: Students write programs to parse structured text data (log files, configuration files, semi-structured reports) into tables for analysis. They use string operations (split, find, substring) to extract fields from each line, handle variations in format, skip header/footer lines, and build a clean table from messy input. This real-world skill prepares students for data engineering tasks where raw data must be cleaned and structured before analysis.
Dependencies:
* T10.G7.06: Clean and transform table data
* T10.G6.18: Parse text into structured list data
* T10.G5.04: Add rows of data to a table

ID: T10.G8.14
Topic: T10 – Lists & Tables
Skill: Design and implement a data pipeline with multiple transformations
Description: Students design a multi-step data processing pipeline: import raw data → clean/validate → transform → aggregate → visualize/export. They chain together table operations learned throughout T10 to build an end-to-end solution for a realistic scenario (e.g., process survey data, analyze game statistics, generate a report from transaction logs). Students document their pipeline design before implementing, handle errors gracefully, and verify output quality at each stage.
Dependencies:
* T10.G8.05: Query and report statistics from a complex dataset
* T10.G7.03: Import external data into a table
* T10.G7.13: Export table data to a file
* T10.G7.07: Validate and handle missing data in tables

ID: T10.G8.15
Topic: T10 – Lists & Tables
Skill: Build a semantic search database from table data
Description: Students use CreatiCode's `create semantic database from table [table]` block to build a searchable database where queries find results by meaning rather than exact keyword matching. They prepare a table with a required 'key' column and additional data columns, understand that the semantic database uses AI embeddings to find similar content, and test queries to verify relevant results are returned. Applications include building a FAQ search system, finding similar products, or creating a knowledge base that users can query in natural language.
Dependencies:
* T10.G8.06: Model relationships using multiple linked tables
* T10.G7.15: Use AI to analyze table data

ID: T10.G8.16
Topic: T10 – Lists & Tables
Skill: Query semantic databases with natural language and filters
Description: Students use `search semantic database with [query] store top (K) in table [result]` and `search semantic database with [query] where [condition] store top (K) in table [result]` to find relevant data using natural language queries. They experiment with different queries to understand how semantic similarity works, apply filters to narrow results, and compare semantic search to exact-match lookups. Students build a practical application (e.g., a smart assistant that answers questions from a knowledge base).
Dependencies:
* T10.G8.15: Build a semantic search database from table data
* T10.G6.02: Filter table rows based on a condition

ID: T10.G8.17
Topic: T10 – Lists & Tables
Skill: Use moving averages to analyze time-series data in lists
Description: Students use `value from [simple/exponential] moving average window [length] of list [list]` to smooth noisy data and identify trends. They understand that moving averages calculate the average over a sliding window, compare simple vs. exponential methods (exponential gives more weight to recent values), and apply this to real scenarios: smoothing sensor readings, analyzing stock prices, or detecting trends in game metrics. Students visualize raw vs. smoothed data to see the difference.
Dependencies:
* T10.G8.03: Implement selection sort algorithm step by step
* T10.G7.08: Analyze a dataset to find patterns or outliers

ID: T10.G8.18
Topic: T10 – Lists & Tables
Skill: Real-time AI vision interaction with table data
Description: Students build real-time applications that react to streaming AI vision data stored in tables. Unlike static analysis (G7.23), this skill focuses on immediate response loops: reading the current hand/body position from the table every frame, detecting changes (e.g., a sudden jump in coordinates signifying a fast movement), and triggering game actions. Students optimize their loops to handle high-frequency updates and prevent lag, ensuring the application feels responsive.
Dependencies:
* T10.G8.04: Build a simulation using table-based state
* T10.G7.28: Process streaming AI data updates into table

ID: T10.G8.19
Topic: T10 – Lists & Tables
Skill: Parse and analyze AI-generated structured data
Description: Students process structured data returned by AI services: web search results stored in tables (`web search [query] store top (K) in table [table]`), NLP sentence analysis (`analyze sentence [text] and write into table [table]` which outputs word, lemma, part-of-speech, etc.), and geographic data (`get geo info for latitude (lat) longitude (lon) and write into table [table]`). Students write code to extract insights from these AI-generated tables: find the most relevant search result, identify verbs in a sentence, or determine the country for coordinates. This skill bridges AI capabilities with data processing skills.
Dependencies:
* T10.G8.13: Parse and process structured text into tables
* T10.G7.23: Analyze static AI vision data in tables

ID: T10.G8.20
Topic: T10 – Lists & Tables
Skill: Design and test data validation rules for tables
Description: Students create comprehensive validation rules for table data and write code to enforce them. Validation types: (1) Type validation (numeric columns should contain numbers), (2) Range validation (age should be 0-150, percentage 0-100), (3) Format validation (email should contain @, date in correct format), (4) Referential validation (foreign key exists in related table), (5) Uniqueness validation (no duplicate IDs). Students implement validation as a function that checks all rows and returns a list of errors with row numbers and descriptions. They test validation rules with intentionally bad data to verify rules catch all issues.
Dependencies:
* T10.G7.07: Validate and handle missing data in tables
* T10.G8.06: Model relationships using multiple linked tables

ID: T10.G8.21
Topic: T10 – Lists & Tables
Skill: Compare algorithmic efficiency for list operations
Description: Students analyze and compare the efficiency of different approaches to the same problem. Case studies: (1) Linear search O(n) vs binary search O(log n) - measure time with 100 vs 1000 items, (2) Naive duplicate removal O(n²) vs sort-then-remove O(n log n), (3) Repeated single lookups vs batch lookup with caching. Students use timer blocks to measure actual performance, create data visualizations showing how time grows with input size, and articulate why some algorithms scale better. This introduces Big-O thinking without formal notation, preparing students for computer science studies.
Dependencies:
* T10.G8.09: Implement binary search on sorted lists
* T10.G8.02: Implement bubble sort algorithm step by step
* T10.G7.25: Optimize table operations for large datasets

ID: T10.G8.22
Topic: T10 – Lists & Tables
Skill: Build a complete AI-enhanced data application
Description: Students design and implement a comprehensive application that combines AI capabilities with data structures. Project options: (1) Smart FAQ system: import questions into table, create semantic search database, accept natural language queries, return relevant answers; (2) Gesture-controlled data browser: use hand detection table to navigate through data displays; (3) Automated data summarizer: import data, use AI to generate insights, display visualizations; (4) Multi-source data aggregator: pull data from web searches into tables, combine and analyze. Students document their design, implement the application, test with real data, and present their solution explaining how AI and data structures work together.
Dependencies:
* T10.G8.15: Build a semantic search database from table data
* T10.G8.19: Parse and analyze AI-generated structured data
* T10.G8.14: Design and implement a data pipeline with multiple transformations

ID: T10.G8.23
Topic: T10 – Lists & Tables
Skill: Implement merge sort algorithm with recursion concept
Description: Students implement merge sort by breaking a list into halves, sorting each half, then merging the sorted halves. While full recursion may be beyond block-based programming, students simulate the divide-and-conquer approach: manually split the list, sort the sublists (using built-in sort or bubble sort), then use the merge algorithm from G6. Students trace through the algorithm on paper showing how a list of 8 items is split into 4 pairs, sorted, merged into 2 sorted halves, then merged into the final sorted list. They compare merge sort's O(n log n) efficiency to bubble sort's O(n²) and understand why divide-and-conquer is powerful.
Dependencies:
* T10.G6.15: Merge two sorted lists into one sorted list
* T10.G8.03: Implement selection sort algorithm step by step
* T10.G8.21: Compare algorithmic efficiency for list operations

ID: T10.G8.24
Topic: T10 – Lists & Tables
Skill: Design a complete data solution for a complex scenario
Description: Students synthesize all T10 skills by designing and implementing a complete data solution for a realistic, multi-faceted scenario (e.g., "Build a school library management system," "Create a sports tournament tracker," "Design a personal budget analyzer"). The solution must include: (1) schema design (choose appropriate data structures, design tables with proper columns), (2) data input/import (collect user input or import external data), (3) data validation and cleaning (handle errors and missing data), (4) core operations (search, filter, sort, aggregate), (5) data transformation or analysis (compute statistics, identify patterns), and (6) output/export (display results, save to file, or visualize). Students document their design decisions, justify data structure choices, implement the system modularly (one feature at a time), test with realistic data, and debug systematically. This capstone skill demonstrates mastery by integrating data structures, algorithms, and software design principles into a coherent solution.
Dependencies:
* T10.G8.14: Design and implement a data pipeline with multiple transformations
* T10.G8.06: Model relationships using multiple linked tables
* T10.G8.05: Query and report statistics from a complex dataset
* T10.G7.04: Design a table schema for a real-world scenario

ID: T10.G8.25
Topic: T10 – Lists & Tables
Skill: Implement LRU (Least Recently Used) cache with lists
Description: Students implement an LRU cache—a data structure that stores recently used items and automatically evicts the least recently used item when capacity is exceeded. Implementation uses two parallel lists: one for keys, one for values, with a maximum size limit. Operations: (1) Get: if key exists, return value AND move item to end (most recent); (2) Put: if key exists, update value and move to end; if key doesn't exist and at capacity, delete first item (least recent) then add new item at end; if under capacity, just add. Students trace through cache operations: put(A,1), put(B,2), put(C,3), get(A), put(D,4) with capacity=3 shows how A moves to end after get, then B (least recent) is evicted when D is added. This advanced pattern appears in web browsers (recently visited), operating systems (memory pages), and databases (query results), teaching both algorithm design and practical systems thinking.
Dependencies:
* T10.G6.23: Implement a simple lookup cache with lists
* T10.G3.29: Delete an item from a list by value
* T10.G3.27: Insert an item at a specific position in a list

ID: T10.G8.26
Topic: T10 – Lists & Tables
Skill: Design data validation rules for AI-generated outputs
Description: Students create validation rules specifically for data that comes from AI services, which can be unpredictable or incorrectly formatted. AI-specific challenges: (1) AI might return empty responses or error messages instead of data, (2) AI might return more or fewer fields than expected, (3) AI confidence scores might indicate uncertain data, (4) AI might hallucinate plausible-looking but incorrect data. Students implement validation layers: check if response is empty, verify expected structure exists, validate data types and ranges, check confidence thresholds, and flag suspicious patterns (e.g., all values identical, values outside realistic bounds). They apply these validations to CreatiCode AI outputs like web search results, NLP analysis, or semantic search and design fallback behaviors when validation fails. This critical thinking skill is essential as AI becomes more integrated into applications.
Dependencies:
* T10.G8.19: Parse and analyze AI-generated structured data
* T10.G8.20: Design and test data validation rules for tables
* T10.G7.07: Validate and handle missing data in tables

ID: T10.G8.27
Topic: T10 – Lists & Tables
Skill: Model tree structure using table with parent references
Description: Students learn to represent hierarchical (tree) data using a table where each row has a "ParentID" column pointing to its parent row. Example: file system where folders contain subfolders and files. Table structure: columns "ID", "Name", "Type" (folder/file), "ParentID" (null for root, or ID of parent folder). Students implement: (1) Find all items in a folder (filter by ParentID), (2) Find the path to an item (follow ParentID chain up to root), (3) Find all descendants (recursive-like traversal using a work queue), (4) Move an item to a different folder (update ParentID). They understand that this "adjacency list" representation is how databases store trees, and compare it to nested structures (which would require complex nesting operations). Applications: organizational charts, category hierarchies, folder structures, comment threads with replies.
Dependencies:
* T10.G6.25: Model simple graph relationships using table as adjacency list
* T10.G8.06: Model relationships using multiple linked tables
* T10.G6.13: Implement queue operations (enqueue and dequeue)

ID: T10.G8.28
Topic: T10 – Lists & Tables
Skill: Compare space-time tradeoffs in data structure choice
Description: Students analyze and articulate the space-time tradeoffs when choosing between data structures or algorithms. Case studies: (1) Storing computed results vs recomputing (cache uses memory to save time), (2) Sorted list enables fast binary search but insert/delete are slow vs unsorted list has fast insert but slow search, (3) Hash table (simulated) has fast lookup but uses more memory than sorted list, (4) Storing redundant data in multiple tables for fast queries vs normalizing to save space but requiring joins. Students create comparison tables showing: operation, structure A time, structure B time, structure A space, structure B space. They articulate decisions like: "I'd use a cache because lookups happen 100x more than updates, so trading memory for lookup speed makes sense." This analytical skill is foundational for algorithm design and system architecture, preparing students for advanced computer science.
Dependencies:
* T10.G8.21: Compare algorithmic efficiency for list operations
* T10.G8.25: Implement LRU (Least Recently Used) cache with lists
* T10.G8.07: Implement a hash table lookup using lists

ID: T10.G8.29
Topic: T10 – Lists & Tables
Skill: Design state machines using table-driven logic
Description: Students implement a state machine where state transitions are stored in a table rather than hardcoded in if-statements. Table structure: columns "CurrentState", "Event", "NextState", "Action". For a vending machine: rows like (Idle, CoinInserted, HasCredit, ShowBalance), (HasCredit, SelectItem, Dispensing, DispenseItem), (Dispensing, ItemDispensed, Idle, Reset). The main program reads the current state and event, looks up the matching row in the table, executes the action, and updates to the next state. Students implement a simple game menu system or traffic light controller using this pattern. Benefits: (1) All state logic is visible in one table, (2) Adding states doesn't require code changes—just add table rows, (3) Easy to debug by logging state transitions. This pattern is widely used in game development, UI systems, and embedded systems, teaching students to externalize logic into data structures.
Dependencies:
* T10.G8.06: Model relationships using multiple linked tables
* T10.G6.04: Use table lookup to find related data
* T10.G8.04: Build a simulation using table-based state

ID: T10.G8.30
Topic: T10 – Lists & Tables
Skill: Implement graph traversal (BFS) using queue and table
Description: Students implement Breadth-First Search (BFS) traversal using a queue (list) for nodes to visit and a table for graph edges (adjacency list from T10.G6.25). BFS algorithm: (1) Start with initial node in queue, mark as visited, (2) While queue not empty: dequeue front node, process it, find all neighbors in edge table, enqueue unvisited neighbors and mark as visited, (3) Continue until queue is empty. Students build a "find all reachable nodes" function for a social network or map, or implement "shortest path" by tracking distances. They trace through BFS on paper first, showing queue state and visit order, then implement in code. Key insight: BFS explores level-by-level (all nodes 1 step away, then all 2 steps away, etc.), which is why it finds shortest paths. This fundamental algorithm connects queue data structure with graph representation, preparing students for more advanced CS concepts.
Dependencies:
* T10.G6.25: Model simple graph relationships using table as adjacency list
* T10.G6.13: Implement queue operations (enqueue and dequeue)
* T10.G8.27: Model tree structure using table with parent references

ID: T10.G8.31
Topic: T10 – Lists & Tables
Skill: Build a complete data-driven game using tables
Description: Students design and implement a complete game where game content is stored in tables rather than hardcoded, demonstrating data-driven development. Game elements stored in tables: (1) Item table—all collectible items with properties (name, value, effect, sprite), (2) Level table—level configurations (difficulty, spawn rate, goal), (3) Enemy table—enemy types with behaviors (speed, damage, health), (4) Dialog table—NPC conversations with branching options. Students build a complete mini-game (dungeon crawler, quiz game, or trading simulator) where: new items can be added by editing a table without changing code, difficulty can be adjusted through level table parameters, game content can be imported from CSV files. They document how the data-driven approach makes the game extensible. This capstone skill synthesizes all table operations into a professional game development pattern used by real game studios.
Dependencies:
* T10.G8.04: Build a simulation using table-based state
* T10.G8.24: Design a complete data solution for a complex scenario
* T10.G7.03: Import external data into a table

ID: T10.G8.32
Topic: T10 – Lists & Tables
Skill: Implement insertion sort algorithm step by step
Description: Students implement insertion sort using nested loops: the outer loop iterates through the unsorted portion (starting at position 2), and for each element, the inner loop finds the correct position in the sorted portion by comparing and shifting elements right to make room. Implementation pattern: (1) For each position i from 2 to length, (2) Store the current item as "key," (3) Search backwards through sorted portion to find where key belongs, (4) Shift larger items right one position, (5) Insert key in the correct spot. Students implement this step by step, first writing the outer loop structure, then the inner comparison/shift logic. They trace through execution on a 5-item list to verify correctness. Comparison to other sorts: Insertion sort is O(n²) worst case like bubble sort, but performs much better on nearly-sorted data because few shifts are needed. Students test their implementation on different inputs: random order, nearly sorted, and reverse sorted, observing performance differences. This completes the basic sorting algorithm trilogy (bubble, selection, insertion).
Dependencies:
* T10.G7.31: Trace insertion sort algorithm on paper before implementing
* T10.G8.02: Implement bubble sort algorithm step by step
* T10.G8.03: Implement selection sort algorithm step by step

ID: T10.G8.33
Topic: T10 – Lists & Tables
Skill: Analyze and compare sorting algorithms for different input patterns
Description: Students conduct systematic experiments to compare bubble sort, selection sort, and insertion sort on different input patterns. Test scenarios: (1) Random order - all three are similar, (2) Nearly sorted (1-2 items out of place) - insertion sort is fastest, (3) Reverse sorted - bubble sort is slowest, (4) Already sorted - insertion sort completes instantly. For each scenario, students count the number of comparisons and swaps/shifts, create a comparison table, and draw conclusions about when each algorithm performs best. Key insights: (1) No single algorithm is best for all situations, (2) Knowing your data patterns helps choose the right algorithm, (3) Real-world data is often partially sorted, favoring insertion sort, (4) Built-in sort functions use more advanced algorithms that outperform all three. Students write a recommendation guide: "Use insertion sort when data is likely already partially sorted. Use selection sort when minimizing swaps is important. Use built-in sort for general purposes." This analytical skill demonstrates that algorithmic choice is context-dependent—preparing students for algorithm design thinking.
Dependencies:
* T10.G8.32: Implement insertion sort algorithm step by step
* T10.G8.21: Compare algorithmic efficiency for list operations
* T10.G6.30: Compare algorithm speed with different list sizes

