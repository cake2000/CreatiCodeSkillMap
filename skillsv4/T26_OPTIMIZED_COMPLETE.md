ID: T26.GK.01
Topic: T26 – Data Collection & Logging
Skill: Identify countable things in a picture
Description: Students scan a picture of a classroom and point to objects they could count (books, chairs, students), building awareness that we can collect information by counting things we see.

Dependencies:
* T09.GK.01: Notice when things are different
* T01.GK.08: Count objects in a set (1–10)

ID: T26.GK.02
Topic: T26 – Data Collection & Logging
Skill: Use tokens to log repeated events
Description: Learners watch a simple animation and slide a bead/token each time an event occurs, then count tokens at the end. This is their first "log."

Dependencies:
* T26.GK.01: Identify countable things in a picture
* T01.GK.07: Group objects by one attribute




ID: T26.GK.03
Topic: T26 – Data Collection & Logging
Skill: Capture yes/no answers with smile/frown cards
Description: Students ask a peer a yes/no question and place the response card into the correct bin, making a physical tally.

Dependencies:
* T26.GK.01: Identify countable things in a picture


ID: T26.G1.01
Topic: T26 – Data Collection & Logging
Skill: Run a three-option picture survey
Description: Students pick a topic (favorite snack) and provide three picture choices. They ask five peers and place stickers on a mini poster to record answers.

Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed
* T26.GK.03: Capture yes/no answers with smile/frown cards

ID: T26.G1.02
Topic: T26 – Data Collection & Logging
Skill: Keep observation logs over time
Description: Learners observe a daily attribute twice (morning vs afternoon temperature icon) for a week, emphasizing longitudinal collection.

Dependencies:
* T26.G1.01: Run a three-option picture survey


ID: T26.G1.03
Topic: T26 – Data Collection & Logging
Skill: Follow a simple data-collection checklist
Description: Students learn to (1) introduce themselves, (2) ask the question the same way, (3) record the answer immediately. They practice on classmates and reflect on why following steps matters.

Dependencies:
* T26.G1.01: Run a three-option picture survey


ID: T26.G2.01
Topic: T26 – Data Collection & Logging
Skill: Distinguish observational vs survey data
Description: Students categorize example data statements as "observed" (counting birds) or "asked" (favorite color), reinforcing method selection.

Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T26.G1.02: Keep observation logs over time


ID: T26.G2.02
Topic: T26 – Data Collection & Logging
Skill: Build a two-column record sheet
Description: Learners create a simple table to log respondents' names and answers, showing why we store identifiers alongside data.

Dependencies:
* T26.G1.01: Run a three-option picture survey
* T25.G1.02: Design a picture table


ID: T26.G2.03
Topic: T26 – Data Collection & Logging
Skill: Use timers to collect duration data
Description: Students run a simple experiment (spin a top) and record each trial's duration using a timer, highlighting measurement precision.

Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T26.G1.02: Keep observation logs over time


ID: T26.G2.04
Topic: T26 – Data Collection & Logging
Skill: Explain why sample size matters
Description: Learners see two surveys (3 responses vs 10) and explain why the larger one may be more reliable.

Dependencies:
* T26.G1.01: Run a three-option picture survey
* T26.G2.02: Build a two-column record sheet


ID: T26.G2.05
Topic: T26 – Data Collection & Logging
Skill: Conduct a multi-response tally survey
Description: Students run an unplugged survey with four or more answer choices (e.g., "What's your favorite season?"), practicing tally marks and organizing more complex response categories before learning coded surveys.

Dependencies:
* T26.G2.04: Explain why sample size matters
* T01.G1.01: Put pictures in order to plant a seed


ID: T26.G3.01
Topic: T26 – Data Collection & Logging
Skill: Script a CreatiCode survey loop
Description: Students write a script that repeats `ask` five times, storing each answer in a list variable (linking T26 to T25 representations).

Dependencies:
* T26.G2.01: Distinguish observational vs survey data
* T07.G3.01: Use a counted repeat loop

Blocks: ask and wait, repeat, add item to list


ID: T26.G3.02
Topic: T26 – Data Collection & Logging
Skill: Write fair survey questions
Description: Learners compare two survey questions—one that suggests an answer ("Don't you love cats?") and one that is neutral ("What is your favorite pet?")—then practice writing their own fair survey question and implement it in CreatiCode using the ask block with multiple-choice buttons, ensuring all response options are equally valid.

Dependencies:
* T26.G3.01: Script a CreatiCode survey loop
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor

Blocks: ask and wait, answer, if-then


ID: T26.G3.03
Topic: T26 – Data Collection & Logging
Skill: Log sensor-style events with counters
Description: Students build a script where a sprite increments a counter variable each time a key is pressed, simulating basic telemetry collection for tracking user interactions.

Dependencies:
* T26.G3.01: Script a CreatiCode survey loop
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor

Blocks: when key pressed, change variable by 1, variable monitor


ID: T26.G3.04.01
Topic: T26 – Data Collection & Logging
Skill: Store raw data in lists
Description: Students create a list to store all raw survey answers without any processing (e.g., 'red', 'blue', 'red', 'blue', 'red'), learning to preserve original data exactly as collected before any aggregation or transformation.

Dependencies:
* T26.G3.03: Log sensor-style events with counters
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor

Blocks: create list, add to list


ID: T26.G3.04.02
Topic: T26 – Data Collection & Logging
Skill: Generate summary data from raw data
Description: Students create a separate list that processes raw data to generate summary counts (e.g., 'red: 2', 'blue: 1'), demonstrating how to aggregate data while keeping the original data intact.

Dependencies:
* T26.G3.04.01: Store raw data in lists
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor

Blocks: create list, add to list, join (for summary formatting), length of list


ID: T26.G3.05
Topic: T26 – Data Collection & Logging
Skill: Spot common data collection mistakes
Description: Students review sample data sets containing common mistakes (missing entries, inconsistent spelling, duplicate records) and identify what went wrong, preparing them to track invalid data in G4.

Dependencies:
* T26.G3.04.02: Generate summary data from raw data
* T08.G3.01: Use a simple if in a script


ID: T26.G3.06
Topic: T26 – Data Collection & Logging
Grade: Grade 3
Skill: Implement basic consent before data collection
Description: Students create a consent workflow that uses an ask block to get user permission ('Do you want to share your answer? yes/no') before collecting and saving any data. They use an if-then block to only store the response if the user agrees, learning to implement privacy-by-design.

Dependencies:
* T26.G3.01: Script a CreatiCode survey loop
* T08.G3.01: Use a simple if in a script

Blocks: ask and wait, if-then, add to list


ID: T26.G4.01
Topic: T26 – Data Collection & Logging
Skill: Create written data collection protocols for teammates
Description: Students draft multi-step written protocols (who to ask, how many people, what to say) so teammates can collect consistent data. This is a planning/documentation activity that applies knowledge from coding skills to organize real-world data collection processes.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Get the length of a list
* T26.G3.04.02: Generate summary data from raw data


ID: T26.G4.02.01
Topic: T26 – Data Collection & Logging
Skill: Create basic tables for logging
Description: Students create simple tables with columns (time, event) to log basic gameplay events. They practice adding rows to tables and understand table structure for organizing multi-attribute data.

Dependencies:
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Get the length of a list
* T26.G3.04.01: Store raw data in lists

Blocks: create table, add row to table


ID: T26.G4.02.02
Topic: T26 – Data Collection & Logging
Skill: Log structured events with multiple attributes
Description: Students extend their tables to capture complex events with multiple attributes (time, event, player, score, level), creating comprehensive telemetry logs that mirror professional game logging systems.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G3.04.02: Generate summary data from raw data
* T26.G4.02.01: Create basic tables for logging

Blocks: create table, add row to table, set cell in table, get cell from table


ID: T26.G4.03
Topic: T26 – Data Collection & Logging
Skill: Track missing/invalid data with flags
Description: Students add a column to note when data is missing or suspect, preparing them for cleaning in T27.

Dependencies:
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G2.01: Create a simple cause-and-effect chain with picture cards
* T06.G2.02: Match multiple triggers to the same action
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Get the length of a list
* T26.G4.02.02: Log structured events with multiple attributes

Blocks: create table, add row to table, set cell in table, if-then


ID: T26.G4.04
Topic: T26 – Data Collection & Logging
Skill: Reflect on privacy in collection
Description: Learners evaluate a proposed survey (asking for full names + addresses) and suggest safer alternatives, aligning with AI4K12 ethics.

Dependencies:
* T04.G2.03: Compare a long explicit description vs a compressed "repeat" description
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Get the length of a list
* T26.G4.01: Create written data collection protocols for teammates


ID: T26.G4.05
Topic: T26 – Data Collection & Logging
Skill: Practice simple file export and import
Description: Students export a simple list variable to a file (downloading it), then import it back into a new project, learning the basics of data persistence through files before moving to databases.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T05.G3.01: Put human‑centered design steps in order
* T05.G3.02: Identify user needs from a short interview transcript
* T10.G3.03: Get the length of a list
* T26.G4.02.01: Create basic tables for logging

Blocks: export variable to file, import variable from file


ID: T26.G4.06.01
Topic: T26 – Data Collection & Logging
Grade: Grade 4
Skill: Use timer and loops for periodic data collection
Description: Students use a counted loop (repeat 10) with timer reset and wait blocks to collect data at regular intervals, understanding the mechanics of time-based data gathering.

Dependencies:
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T07.G3.01: Use a counted repeat loop
* T10.G3.03: Get the length of a list

Blocks: repeat, reset timer, wait seconds, timer


ID: T26.G4.06
Topic: T26 – Data Collection & Logging
Skill: Collect data from one AI sensor
Description: Students practice with a single AI sensor (like microphone volume or mouse position) by logging its values to a list ten times using a counted loop, building familiarity with continuous data collection before combining multiple sensors.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T05.G3.01: Put human‑centered design steps in order
* T05.G3.02: Identify user needs from a short interview transcript
* T07.G2.01: Identify when to use "repeat" vs "do once"
* T10.G3.03: Get the length of a list
* T26.G4.02.01: Create basic tables for logging
* T26.G4.06.01: Use timer and loops for periodic data collection

Blocks: loudness of microphone, mouse x, mouse y, add item to list, repeat


ID: T26.G4.07
Topic: T26 – Data Collection & Logging
Skill: Use list statistics blocks to summarize collected data
Description: Students apply list statistics blocks (min, max, sum, average) to analyze collected data, learning to compute basic statistical summaries that reveal patterns in their datasets.

Dependencies:
* T04.G2.01: Identify the repeating unit in a longer pattern
* T04.G2.02: Spot repeated step sequences in everyday algorithms
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Get the length of a list
* T26.G3.04.01: Store raw data in lists

Blocks: min of list, max of list, sum of list, average of list, length of list


ID: T26.G5.01.01
Topic: T26 – Data Collection & Logging
Grade: Grade 5
Skill: Use basic print to console block
Description: Students use the print to console block to display simple messages, learning the fundamental mechanism for outputting information to the console for debugging and logging.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list

Blocks: print to console


ID: T26.G5.01.02
Topic: T26 – Data Collection & Logging
Grade: Grade 5
Skill: Print variable values for debugging
Description: Students insert print statements that display variable values at key points in their code, learning to track how data changes during program execution.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G5.01.01: Use basic print to console block

Blocks: print to console, join, variables


ID: T26.G5.01.03
Topic: T26 – Data Collection & Logging
Grade: Grade 5
Skill: Use color-coded console messages for different event types
Description: Students use console blocks with different colors (red for errors, green for success, yellow for warnings) to create more informative logging systems that make it easier to identify event types at a glance.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G5.01.02: Print variable values for debugging

Blocks: print to console with color, variables


ID: T26.G5.01
Topic: T26 – Data Collection & Logging
Skill: Add print statements to track events during execution
Description: Students insert print blocks at key points in their code to display messages to the console when specific events occur (level start, player hit, score update), creating a chronological log of what happened during gameplay for debugging and later analysis.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G4.02.02: Log structured events with multiple attributes
* T26.G5.01.03: Use color-coded console messages for different event types

Blocks: print to console, variables


ID: T26.G5.02
Topic: T26 – Data Collection & Logging
Skill: Plan sampling strategies
Description: Learners compare convenience sampling (asking the first 5 classmates they see) vs random sampling (using a random number generator to select student IDs) for a class poll. They plan and document which sampling strategy they'll use and why, explaining the trade-offs between ease of collection and representativeness. They implement their chosen strategy in CreatiCode.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G3.01: Script a CreatiCode survey loop

Blocks: ask and wait, pick random from list


ID: T26.G5.03
Topic: T26 – Data Collection & Logging
Skill: Validate data entry with error checks
Description: Students add checks (e.g., reject scores <0 or >100) during collection to ensure data quality upstream.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G4.03: Track missing/invalid data with flags

Blocks: if-then, comparison operators, add to list, print to console


ID: T26.G5.04.01
Topic: T26 – Data Collection & Logging
Grade: Grade 5
Skill: Create tables with named columns
Description: Students create a table variable with specific column names (e.g., "time", "event", "player") and understand column organization before adding data rows.

Dependencies:
* T10.G4.02: Read and modify cells in a table

Blocks: create table, set column names


ID: T26.G5.04
Topic: T26 – Data Collection & Logging
Skill: Store logs in CreatiCode tables for export
Description: Learners push collected events into table variables with named columns, prepping for CSV export to T27.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.01: Add print statements to track events during execution
* T26.G5.04.01: Create tables with named columns

Blocks: create table, add row to table, get cell from table, set cell in table


ID: T26.G5.05.01
Topic: T26 – Data Collection & Logging
Grade: Grade 5
Skill: Insert table data into cloud database collection
Description: Students insert a simple data table (3-5 rows, 2-3 columns) into a database collection using the "insert from table into collection" block, learning to persist data to cloud storage.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: insert from table into collection, collection name reporter, set database URL and key


ID: T26.G5.05.02
Topic: T26 – Data Collection & Logging
Grade: Grade 5
Skill: Fetch data from cloud collection into table
Description: Students retrieve previously stored data from a database collection into a table variable using "fetch from collection into table" block, understanding data retrieval basics.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.05.01: Insert table data into cloud database collection

Blocks: fetch from collection into table, collection name reporter


ID: T26.G5.06.01
Topic: T26 – Data Collection & Logging
Grade: Grade 5
Skill: Record player scores to leaderboard
Description: Students use leaderboard blocks to save player names and scores to persistent cloud storage, learning the basics of competitive game data tracking.

Dependencies:
* T09.G4.01: Create and use a numeric variable for score or count
* T10.G4.02: Read and modify cells in a table
* T26.G5.05.01: Insert table data into cloud database collection

Blocks: record score to leaderboard


ID: T26.G5.06.02
Topic: T26 – Data Collection & Logging
Grade: Grade 5
Skill: Retrieve and display leaderboard rankings
Description: Students fetch top scores from the leaderboard and display them on stage, understanding how to retrieve and present ranked data.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.06.01: Record player scores to leaderboard

Blocks: show leaderboard, hide leaderboard


ID: T26.G5.07
Topic: T26 – Data Collection & Logging
Skill: Collect face detection data into tables
Description: Students use CreatiCode face detection blocks to capture facial landmark data (position, expression, orientation) into tables with timestamps, learning to collect and organize real-time sensor data for analysis.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T23.G4.01: Detect faces and show bounding boxes
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: detect faces, get face data, add row to table, timer


ID: T26.G5.08.01
Topic: T26 – Data Collection & Logging
Grade: Grade 5
Skill: Export and import list variables to/from files
Description: Students export a list variable to a downloadable JSON file and import it back in a new project, understanding basic file I/O for list data persistence.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G4.05: Practice simple file export and import

Blocks: export variable to file, import variable from file


ID: T26.G5.08.02
Topic: T26 – Data Collection & Logging
Grade: Grade 5
Skill: Export and import tables to/from files
Description: Students export table variables to downloadable files and import them back, understanding table file persistence and backup strategies.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export
* T26.G5.08.01: Export and import list variables to/from files

Blocks: export table to file, import table from file


ID: T26.G5.09
Topic: T26 – Data Collection & Logging
Skill: Collect data from two synchronized sensors
Description: Students log data from two different sensors simultaneously (e.g., mouse position and microphone volume) in the same row of a table, recording them together so the values stay synchronized for later analysis.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G4.06: Collect data from one AI sensor
* T26.G5.04: Store logs in CreatiCode tables for export
* T26.G5.04.01: Create tables with named columns

Blocks: loudness of microphone, mouse x, mouse y, add row to table, timer


ID: T26.G5.10
Topic: T26 – Data Collection & Logging
Skill: Save key-value data to server storage
Description: Students use server storage blocks to save simple key-value pairs (like player preferences or game settings) to persistent cloud storage, learning the basics of data persistence beyond local variables.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G5.05.01: Insert table data into cloud database collection

Blocks: set server value for key, get server value for key


ID: T26.G5.11
Topic: T26 – Data Collection & Logging
Skill: Read key-value data from server storage
Description: Students retrieve previously stored key-value data from server storage, learning to access persistent data across sessions and use it to restore application state.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T10.G3.03: Add and remove items from a list
* T26.G5.10: Save key-value data to server storage

Blocks: get server value for key, set variable to


ID: T26.G6.01
Topic: T26 – Data Collection & Logging
Skill: Map stakeholder questions to data requirements
Description: Students receive stakeholder questions ("Which level is hardest?") and specify what data to collect (attempt count, completion time), aligning collection with analysis goals.

Dependencies:
* T08.G4.01: Use a simple if in a script
* T09.G4.01: Create and use a numeric variable for score or count
* T09.G4.04: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export


ID: T26.G6.02.01
Topic: T26 – Data Collection & Logging
Grade: Grade 6
Skill: Log hand tracking data to table
Description: Students use hand tracking blocks to capture hand landmark data (position, gesture) into tables with timestamps, learning to collect real-time body tracking sensor data.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T23.G5.01: Detect hands and show hand landmarks
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: detect hands, get hand data, add row to table, timer


ID: T26.G6.02.02
Topic: T26 – Data Collection & Logging
Grade: Grade 6
Skill: Combine face and hand tracking data in one table
Description: Students log data from both face detection and hand tracking simultaneously into a unified table, learning to synchronize multiple AI sensor streams with matching timestamps.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.07: Collect face detection data into tables
* T26.G6.02.01: Log hand tracking data to table

Blocks: detect faces, detect hands, get face data, get hand data, add row to table, timer


ID: T26.G6.02
Topic: T26 – Data Collection & Logging
Skill: Automate logging from three different sensors
Description: Learners combine blocks to record data from three different sensor types (face detection, hand tracking, microphone level) simultaneously into a unified table, ensuring all data streams are captured with matching timestamps for synchronized analysis.

Dependencies:
* T06.G4.01: Build a green-flag script that runs a 3-5 block sequence
* T09.G4.04: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export
* T26.G6.02.02: Combine face and hand tracking data in one table

Blocks: detect faces, detect hands, loudness of microphone, add row to table, timer


ID: T26.G6.03
Topic: T26 – Data Collection & Logging
Skill: Create consent and opt-out workflows with widget dialogs
Description: Students implement dialog widget blocks that explain what will be collected, gather explicit user consent, and disable logging when declined, following privacy-by-design principles.

Dependencies:
* T08.G4.01: Use a simple if in a script
* T09.G4.04: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G4.04: Reflect on privacy in collection
* T26.G6.01: Map stakeholder questions to data requirements

Blocks: show dialog, ask and wait, if-then-else, add row to table


ID: T26.G6.04
Topic: T26 – Data Collection & Logging
Skill: Note when measurements might be inaccurate
Description: Learners add a "data quality" column to their measurement tables using descriptive flags like "verified," "estimated," or "uncertain." For example, when recording game scores, they mark auto-recorded scores as "verified" but manually entered scores as "estimated," teaching them to document measurement reliability alongside the data itself.

Dependencies:
* T08.G4.01: Use a simple if in a script
* T09.G4.01: Create and use a numeric variable for score or count
* T09.G4.04: Trace code with variables to predict outcomes
* T10.G4.02: Read and modify cells in a table
* T26.G5.03: Validate data entry with error checks

Blocks: create table, add row to table, set cell in table, if-then-else


ID: T26.G6.05.01
Topic: T26 – Data Collection & Logging
Grade: Grade 6
Skill: Understand document structure for database collections
Description: Students examine how table rows (with column names as fields) map to database documents with field-value pairs, understanding the data structure transformation between tables and NoSQL documents.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.05.01: Insert table data into cloud database collection


ID: T26.G6.05
Topic: T26 – Data Collection & Logging
Skill: Insert data from tables into database collections
Description: Students use CreatiCode database blocks to insert rows from their data tables into cloud database collections, learning the basics of database operations and structured data storage for larger-scale data management.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.05.01: Insert table data into cloud database collection
* T26.G6.01: Map stakeholder questions to data requirements
* T26.G6.05.01: Understand document structure for database collections

Blocks: insert from table into collection, set database URL and key


ID: T26.G6.06.01
Topic: T26 – Data Collection & Logging
Grade: Grade 6
Skill: Build simple database filter conditions
Description: Students create basic filter conditions using comparison operators (=, >, <, ≥, ≤, ≠) and field reporters to query specific records from a collection.

Dependencies:
* T08.G5.02: Use compound conditions (and, or, not)
* T10.G4.02: Read and modify cells in a table

Blocks: cond [comparison operators], field [fieldname] reporter


ID: T26.G6.06.01.01
Topic: T26 – Data Collection & Logging
Grade: Grade 6
Skill: Build compound database conditions with AND/OR
Description: Students create compound filter conditions by combining multiple simple conditions with AND/OR logic (e.g., "score > 50 AND level = 3"), learning to express complex query requirements.

Dependencies:
* T26.G6.06.01: Build simple database filter conditions
* T08.G5.02: Use compound conditions (and, or, not)

Blocks: cond and, cond or, cond not, cond field [comparison], field reporter


ID: T26.G6.06.02
Topic: T26 – Data Collection & Logging
Grade: Grade 6
Skill: Query database collections with filters
Description: Students use the fetch block with where conditions to retrieve filtered subsets of data (e.g., "score > 50"), understanding how to efficiently access relevant records from larger collections.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G6.06.01: Build simple database filter conditions
* T26.G5.05.02: Fetch data from cloud collection into table

Blocks: fetch from collection into table, where condition, limit


ID: T26.G6.06.03
Topic: T26 – Data Collection & Logging
Grade: Grade 6
Skill: Sort database query results
Description: Students add sorting criteria to their database queries to retrieve data in specific order (ascending/descending by field), learning to organize query results for analysis.

Dependencies:
* T10.G6.01: Sort a table by a column

* T26.G6.06.02: Query database collections with filters

Blocks: fetch from collection into table, sort by field, ascending/descending


ID: T26.G6.07
Topic: T26 – Data Collection & Logging
Skill: Import data from Google Sheets into tables
Description: Students use Google Sheets integration blocks to pull data from shared spreadsheets into CreatiCode tables, enabling collaboration and data collection from external sources.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: read from Google Sheets into table, set Google Sheets credentials


ID: T26.G6.08
Topic: T26 – Data Collection & Logging
Skill: Export tables to Google Sheets
Description: Learners push their collected data tables to Google Sheets for sharing with teammates or further analysis in spreadsheet tools, understanding data export workflows.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export
* T26.G6.07: Import data from Google Sheets into tables

Blocks: write into Google Sheets from table, set Google Sheets credentials


ID: T26.G6.09
Topic: T26 – Data Collection & Logging
Skill: Log multiplayer game session data
Description: Students implement data collection in multiplayer games to track player interactions, scores, and events across multiple connected users, learning to handle concurrent data streams and player identification.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.06.01: Record player scores to leaderboard
* T26.G6.01: Map stakeholder questions to data requirements

Blocks: multiplayer blocks, add row to table, get player ID, timer


ID: T26.G6.10
Topic: T26 – Data Collection & Logging
Skill: Delete rows from tables by index
Description: Students learn to remove specific rows from tables using row index, understanding how to clean up or correct collected data by removing individual records.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G5.04: Store logs in CreatiCode tables for export

Blocks: delete row from table at index, number of rows in table


ID: T26.G6.11
Topic: T26 – Data Collection & Logging
Skill: Clear all rows from a table
Description: Students use blocks to remove all rows from a table while preserving the column structure, learning to reset data collection tables for new sessions or experiments.

Dependencies:
* T10.G4.02: Read and modify cells in a table
* T26.G6.10: Delete rows from tables by index

Blocks: clear all rows from table, create table


ID: T26.G7.01
Topic: T26 – Data Collection & Logging
Skill: Build reusable data collection modules
Description: Students wrap logging behavior into custom blocks (e.g., `logEvent type message data`) so multiple sprites can call the same routine.

Dependencies:
* T06.G5.01: Build a green-flag script that runs a 3-5 block sequence
* T09.G5.01: Trace code with variables to predict outcomes
* T10.G5.03: Add and remove items from a list
* T11.G5.02: Define a custom block with one parameter
* T26.G6.01: Map stakeholder questions to data requirements

Blocks: define custom block, call custom block, add row to table


ID: T26.G7.02
Topic: T26 – Data Collection & Logging
Skill: Monitor data quality in real time
Description: Learners build HUD widgets indicating percentage of responses collected, number of nulls, or out-of-range counts to catch issues while collecting.

Dependencies:
* T09.G5.01: Display variable value on stage using the variable monitor
* T09.G5.02: Trace code with variables to predict outcomes
* T10.G5.03: Add and remove items from a list
* T26.G6.04: Note when measurements might be inaccurate
* T26.G7.01: Build reusable data collection modules

Blocks: variable monitor, count items in list, if-then, operators


ID: T26.G7.03.01
Topic: T26 – Data Collection & Logging
Grade: Grade 7
Skill: Import CSV data files into tables
Description: Students use file import blocks to load CSV datasets (weather data, public statistics) into CreatiCode tables, learning to work with external data sources in standard formats.

Dependencies:
* T10.G5.03: Add and remove items from a list
* T26.G5.04: Store logs in CreatiCode tables for export
* T26.G5.08.02: Export and import tables to/from files

Blocks: import table from file, read CSV into table


ID: T26.G7.03.02
Topic: T26 – Data Collection & Logging
Grade: Grade 7
Skill: Create metadata table for data sources
Description: Students create a separate metadata table that documents information about their datasets (source URL, license, date downloaded, refresh date), learning to track data provenance systematically.

Dependencies:
* T10.G5.03: Add and remove items from a list
* T26.G5.04: Store logs in CreatiCode tables for export
* T26.G7.03.01: Import CSV data files into tables

Blocks: create table, add row to table, set cell in table


ID: T26.G7.03
Topic: T26 – Data Collection & Logging
Skill: Document provenance for external CSV datasets
Description: Students import an open dataset from CSV files (weather data, public statistics) using file import blocks, then log metadata (source URL, license, date downloaded, when to refresh), reinforcing responsible data use and proper citation practices.

Dependencies:
* T08.G5.01: Use a simple if in a script
* T09.G5.01: Trace code with variables to predict outcomes
* T10.G5.03: Add and remove items from a list
* T26.G5.04: Store logs in CreatiCode tables for export
* T26.G6.03: Create consent and opt-out workflows with widget dialogs
* T26.G7.03.02: Create metadata table for data sources

Blocks: import table from file, create table, add row to table


ID: T26.G7.04
Topic: T26 – Data Collection & Logging
Skill: Evaluate bias risks introduced during collection
Description: Learners compare planned participants vs actual participants and highlight underrepresented groups, proposing corrective actions.

Dependencies:
* T08.G5.01: Use a simple if in a script
* T09.G5.01: Trace code with variables to predict outcomes
* T10.G5.03: Add and remove items from a list
* T26.G5.02: Plan sampling strategies
* T26.G7.02: Monitor data quality in real time


ID: T26.G7.05
Topic: T26 – Data Collection & Logging
Grade: Grade 7
Skill: Debug data collection scripts using print statements
Description: Students debug data collection issues by strategically placing print statements to track variable values, loop iterations, and data transformations. They identify where data gets corrupted or lost in their collection pipeline.

Dependencies:
* T26.G5.01: Add print statements to track events during execution
* T26.G5.04: Store logs in CreatiCode tables for export
* T07.G5.01: Use a repeat loop in a script

Blocks: print to console, variables, lists, tables


ID: T26.G7.06
Topic: T26 – Data Collection & Logging
Skill: Update and append data to Google Sheets
Description: Students use Google Sheets blocks to append new rows to existing spreadsheets or update specific cells based on conditions, enabling continuous data collection and collaborative data management.

Dependencies:
* T10.G5.03: Add and remove items from a list
* T26.G6.07: Import data from Google Sheets into tables
* T26.G6.08: Export tables to Google Sheets

Blocks: append row from table to sheet, set value at row/column in sheet


ID: T26.G7.07.01
Topic: T26 – Data Collection & Logging
Grade: Grade 7
Skill: Update existing documents in database collections
Description: Students modify specific fields in existing database documents using update operations with where conditions, learning to maintain and correct stored data.

Dependencies:
* T10.G5.03: Add and remove items from a list
* T26.G6.06.02: Query database collections with filters
* T26.G6.06.01.01: Build compound database conditions with AND/OR

Blocks: update collection from table, update collection in-place where, set fields, cond expressions


ID: T26.G7.07.02
Topic: T26 – Data Collection & Logging
Grade: Grade 7
Skill: Delete documents from database collections
Description: Students remove obsolete or unwanted documents from collections using delete operations with where conditions, understanding data lifecycle management.

Dependencies:
* T10.G5.03: Add and remove items from a list
* T26.G7.07.01: Update existing documents in database collections
* T26.G6.06.01.01: Build compound database conditions with AND/OR

Blocks: remove all documents from collection where, cond expressions


ID: T26.G8.01
Topic: T26 – Data Collection & Logging
Skill: Design end-to-end telemetry pipelines with cloud integration
Description: Students design a complete data pipeline diagram for a multi-level game, mapping the flow: (1) in-game events → (2) validation checks → (3) table storage → (4) database insert → (5) query/retrieval → (6) file export. They identify what data transformations happen at each stage and why, understanding how professional games track player behavior for analytics.

Dependencies:
* T01.G6.01: Count comparisons in linear and binary search
* T06.G6.01: Trace event execution paths in a multi-event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column

* T26.G7.01: Build reusable data collection modules
* T04.G6.01: Group snippets by underlying algorithm pattern
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T07.G6.01: Trace nested loops with variable bounds


ID: T26.G8.01.01
Topic: T26 – Data Collection & Logging
Grade: Grade 8
Skill: Implement end-to-end telemetry pipeline
Description: Students build a complete working telemetry system that collects game events, validates them, stores in tables, saves to database, and exports to file, implementing the pipeline they designed in T26.G8.01.


Blocks: All telemetry blocks (events, validation, tables, database insert/fetch/update, file export)

Dependencies:
* T26.G8.01: Design end-to-end telemetry pipelines with cloud integration
* T26.G7.07.01: Update existing documents in database collections
* T26.G6.06.02: Query database collections with filters
* T26.G5.08.02: Export and import tables to/from files
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T07.G6.01: Trace nested loops with variable bounds
* T13.G6.01: Trace complex code with multiple variables


ID: T26.G8.02
Topic: T26 – Data Collection & Logging
Skill: Implement scheduled data exports and resets
Description: Learners script timed routines that export a table to file (or display) and then clear/reset logs, mirroring production data rotation.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi-event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column

* T26.G7.01: Build reusable data collection modules
* T26.G8.01: Design end-to-end telemetry pipelines with cloud integration
* T04.G6.01: Group snippets by underlying algorithm pattern
* T07.G6.01: Trace nested loops with variable bounds
* T25.G6.01: Document metadata for datasets

Blocks: timer, export table to file, clear all rows from table, custom block


ID: T26.G8.03
Topic: T26 – Data Collection & Logging
Skill: Use AI assistant to review data collection protocols
Description: Students send their data collection protocol to the XO AI assistant for review, then document which suggestions they accepted or rejected, demonstrating human oversight of AI recommendations.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi-event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column

* T24.G6.01: Use XO to generate code snippets
* T26.G8.01: Design end-to-end telemetry pipelines with cloud integration
* T07.G6.01: Trace nested loops with variable bounds
* T22.G6.01.01: Make a basic ChatGPT request with one parameter
* T36.G6.01: Compare computing career clusters (software, hardware, data, AI)

Blocks: XO chat, ask and wait, variables


ID: T26.G8.04
Topic: T26 – Data Collection & Logging
Skill: Publish data privacy agreements for peers
Description: Learners author a short agreement describing what data will be collected, how it's stored, who can access it, and deletion timelines, tying back to AI4K12's societal-impact focus.

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column

* T26.G6.03: Create consent and opt-out workflows with widget dialogs
* T26.G7.04: Evaluate bias risks introduced during collection
* T07.G6.01: Trace nested loops with variable bounds
* T13.G6.01: Trace complex code with multiple variables
* T22.G6.01.01: Make a basic ChatGPT request with one parameter


ID: T26.G8.05
Topic: T26 – Data Collection & Logging
Skill: Create and search semantic databases for AI-powered data retrieval
Description: Students use CreatiCode semantic database blocks to store text documents with AI-generated embeddings, then perform natural language searches (e.g., 'find articles about space exploration') to retrieve semantically similar records, understanding how AI enables meaning-based search beyond exact keyword matching.


Blocks: semantic database insert, semantic search, embeddings

Dependencies:
* T10.G6.01: Sort a table by a column

* T24.G7.01: Generate text or ideas with AI prompts
* T26.G6.05: Insert data from tables into database collections
* T26.G6.06.02: Query database collections with filters
* T07.G6.01: Trace nested loops with variable bounds
* T09.G6.01: Model real-world quantities using variables and formulas
* T12.G6.01: Analyze a program's structure using a checklist and suggest specific improvements


