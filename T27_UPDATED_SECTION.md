# T27 - DATA ANALYSIS & STORYTELLING
# COMPLETE UPDATED SECTION WITH ALL PHASE 1 FIXES IMPLEMENTED
# Generated: November 21, 2025

---

ID: T27.GK.01
Topic: T27 – Data Analysis & Storytelling
Skill: Sort objects by a rule and explain it
Description: In this picture-based activity, students group objects (shapes, animals) and state the rule ("all red things"), reinforcing that analysis starts with describing criteria.



ID: T27.GK.02
Topic: T27 – Data Analysis & Storytelling
Skill: Compare which group has more
Description: Learners count two piles (≤5 each) and state which is larger or if they match, building comparative reasoning.

Dependencies:
* T27.GK.01: Sort objects by a rule and explain it




ID: T27.GK.03
Topic: T27 – Data Analysis & Storytelling
Skill: Read a two-column picture chart
Description: Students interpret which category wins using a pictograph (one icon per item), establishing the basic concept of visual comparisons.

Dependencies:
* T27.GK.02: Compare which group has more




ID: T27.G1.01
Topic: T27 – Data Analysis & Storytelling
Skill: Build a pictograph from tallies
Description: Students convert tally marks collected in T26 into stacked icons using manipulatives or drawing tools, linking collection to analysis visuals.

Dependencies:
* T27.GK.03: Read a two-column picture chart

ID: T27.G1.02
Topic: T27 – Data Analysis & Storytelling
Skill: Answer "how many more?" questions
Description: Learners compute the difference between two categories using picture charts.

Dependencies:
* T27.G1.01: Build a pictograph from tallies


ID: T27.G1.03
Topic: T27 – Data Analysis & Storytelling
Skill: Tell a one-sentence story with data
Description: Students describe what the chart shows ("Most kids chose apples") using comparative language.

Dependencies:
* T27.G1.01: Build a pictograph from tallies


ID: T27.G2.01
Topic: T27 – Data Analysis & Storytelling
Skill: Create bar charts with axes labels
Description: Learners build a bar chart using paper, crayons, or simple drag-and-drop drawing tools (no coding) with labeled axes, reinforcing representation clarity. This is an unplugged/pre-coding activity focused on understanding chart structure.

Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T27.G1.01: Build a pictograph from tallies


ID: T27.G2.02
Topic: T27 – Data Analysis & Storytelling
Skill: Interpret simple line plots
Description: Students analyze a small line plot (temperature across 5 days) and answer what increased/decreased.

Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T27.G1.01: Build a pictograph from tallies


ID: T27.G2.03
Topic: T27 – Data Analysis & Storytelling
Skill: Identify outliers visually in small data sets
Description: Learners look at illustrated lists like [3, 4, 3, 12] represented as pictures or bars and point out which value looks different, explaining why 12 is unusual compared to the others.

Dependencies:
* T01.G1.10: Match pictures to "if/then" rules
* T27.G2.01: Create bar charts with axes labels


ID: T27.G2.04
Topic: T27 – Data Analysis & Storytelling
Skill: Decide if data answers the question asked
Description: Students read a question ("Which snack is most popular?") and determine if the provided chart answers it or if more data is needed.

Dependencies:
* T27.G1.03: Tell a one-sentence story with data
* T27.G2.02: Interpret simple line plots


ID: T27.G3.01b
Topic: T27 – Data Analysis & Storytelling
Skill: Create and populate data tables in CreatiCode
Description: Students learn to create table structure by adding columns (using 'add column [name] at position (1) to table [table1 v]'), populate rows with data (using 'add to table [table1 v]: [value1] [value2] [value3]'), and display tables to verify contents (using 'show table [table1 v]'). This builds the foundation for all data analysis activities in G3 and beyond.

Dependencies:
* T27.G2.01: Create bar charts with axes labels
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.01: Create and use a numeric variable for score or count


ID: T27.G3.01
Topic: T27 – Data Analysis & Storytelling
Skill: Compute totals and averages from data tables
Description: Students use CreatiCode's built-in aggregation blocks ([sum v] of column [scores] in table [data v] and [average v] of column [scores] in table [data v]) to quickly compute totals and means from data tables, learning to use powerful analysis tools efficiently without manual loops.

Dependencies:
* T27.G3.01b: Create and populate data tables in CreatiCode
* T07.G3.01: Use a counted repeat loop


ID: T27.G3.02
Topic: T27 – Data Analysis & Storytelling
Skill: Build comparison statements with evidence
Description: Learners write comparison statements like "X has more than Y because 15 vs 10" displayed in sprite speech bubbles, reinforcing evidence-based claims using computed data from their analysis.

Dependencies:
* T27.G3.01: Compute totals and averages from data tables
* T09.G3.01: Create and use a numeric variable for score or count


ID: T27.G3.03
Topic: T27 – Data Analysis & Storytelling
Skill: Use CreatiCode data tables to group and count
Description: Students use CreatiCode table blocks to filter rows by category (e.g., using 'delete rows with column [type] of value [desert]' to keep only forest levels) and count how many rows match (using 'row count of table [data v]'), learning simple data grouping and filtering operations.

Dependencies:
* T27.G3.01b: Create and populate data tables in CreatiCode
* T27.G3.02: Build comparison statements with evidence


ID: T27.G3.04
Topic: T27 – Data Analysis & Storytelling
Skill: Create side-by-side bar charts for two groups
Description: Learners use CreatiCode's 'draw [bar v] chart using columns [classA,classB] from table [scores v]' block to generate multi-series bar charts comparing two categories (e.g., Class A vs Class B scores), reinforcing comparative visualization skills.

Dependencies:
* T27.G3.03: Use CreatiCode data tables to group and count


ID: T27.G4.01
Topic: T27 – Data Analysis & Storytelling
Skill: Analyze change over time using line graphs
Description: Students read game data (such as scores over 10 rounds) and use line graphs to identify segments where values rise, fall, or stay flat, building temporal analysis skills.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T09.G3.01: Create and use a numeric variable for score or count
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G3.04: Separate raw data from summary data
* T27.G3.04: Create side-by-side bar charts for two groups


ID: T27.G4.02b
Topic: T27 – Data Analysis & Storytelling
Skill: Understand median and mode concepts
Description: Students examine small, pre-sorted datasets and identify the median (middle value) and mode (most frequent value) through visual inspection and counting. They explain why these statistics differ from the mean and when each is most useful (e.g., median is less affected by outliers). This is a conceptual data literacy skill preparing for computational implementation.

Dependencies:
* T27.G3.01: Compute totals and averages from data tables
* T27.G2.03: Identify outliers visually in small data sets


ID: T27.G4.02c
Topic: T27 – Data Analysis & Storytelling
Skill: Calculate median and mode using code
Description: Students implement median calculation by sorting a list and finding the middle value, and mode calculation by counting frequencies. They use CreatiCode's aggregation blocks ([median v] of column [scores] in table [data v]) along with sorting and conditional blocks to compute these statistics, connecting statistical concepts to code implementation.

Dependencies:
* T27.G4.02b: Understand median and mode concepts
* T08.G3.01: Use a simple if in a script


ID: T27.G4.02
Topic: T27 – Data Analysis & Storytelling
Skill: Calculate percentages from grouped data
Description: Students compute percentage breakdowns (e.g., 15 out of 50 = 30%) from categorized tables using division and the percentage chart block, connecting raw counts to relative comparisons for interpretive analysis.

Dependencies:
* T27.G4.02b: Understand median and mode concepts
* T27.G3.03: Use CreatiCode data tables to group and count
* T09.G3.01: Create and use a numeric variable for score or count


ID: T27.G4.02d
Topic: T27 – Data Analysis & Storytelling
Skill: Filter table rows by condition
Description: Students use CreatiCode filtering blocks to keep or remove rows matching specific criteria (e.g., 'delete rows with column [score] of value [0]' to remove incomplete data, or 'keep rows with column [level] > [5]' to analyze advanced levels only). This prepares for dashboard filtering and data quality control.

Dependencies:
* T27.G4.03: Check data quality before analysis
* T08.G3.01: Use a simple if in a script
* T09.G3.01: Create and use a numeric variable for score or count


ID: T27.G4.03
Topic: T27 – Data Analysis & Storytelling
Skill: Check data quality before analysis
Description: Students inspect a table for specific issues: missing entries, duplicate rows, or invalid numbers (e.g., negative ages), and decide how to handle each (ignore row, replace with average, flag for review). They use visual inspection and simple conditional checks to identify problematic data.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G3.04: Separate raw data from summary data
* T27.G3.03: Use CreatiCode data tables to group and count


ID: T27.G4.04
Topic: T27 – Data Analysis & Storytelling
Skill: Create narrative captions for charts
Description: Learners write 2–3 sentence captions summarizing key findings, audience, and implications for their visualizations.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G3.04: Separate raw data from summary data
* T27.G4.01: Analyze change over time using line graphs


ID: T27.G4.04b
Topic: T27 – Data Analysis & Storytelling
Skill: Sort tables to organize data
Description: Students use 'sort table [data v] by column [score] [large to small v]' to organize data for analysis, understanding ascending vs descending order and how sorting reveals patterns (top performers, lowest values, alphabetical order). Sorting is essential for finding medians and identifying extremes.

Dependencies:
* T27.G4.02d: Filter table rows by condition
* T09.G3.01: Create and use a numeric variable for score or count


ID: T27.G5.01
Topic: T27 – Data Analysis & Storytelling
Skill: Build a simple interactive dashboard with filter widgets
Description: Students connect 2-3 CreatiCode widgets (dropdown menus or buttons created with widget blocks) to data tables so viewers can filter by one category (e.g., clicking "Forest" button shows only forest level data) and watch a single chart update dynamically. This introduces interactive data exploration.

Dependencies:
* T27.G4.02d: Filter table rows by condition
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G3.04: Separate raw data from summary data
* T27.G4.04: Create narrative captions for charts


ID: T27.G5.01b
Topic: T27 – Data Analysis & Storytelling
Skill: Group data by category and compute statistics (GROUP BY)
Description: Students use 'set table [summary v] to [average v] of column [score] in table [data v] by column [grade]' to create summary tables showing statistics per group (e.g., average score per grade level, total sales per region). This enables powerful comparative analysis across categories and is a foundational database operation.

Dependencies:
* T27.G4.04b: Sort tables to organize data
* T27.G3.01: Compute totals and averages from data tables
* T09.G4.01: Read multiple inputs via ask blocks and apply them in conditions


ID: T27.G5.02
Topic: T27 – Data Analysis & Storytelling
Skill: Correlate two variables visually
Description: Students create dual bar charts or overlaid line charts (using multi-column chart blocks) to explore relationships (e.g., comparing time played vs high score using side-by-side bars) and describe patterns they observe, such as positive correlation, negative correlation, or no clear relationship.

Dependencies:
* T27.G4.01: Analyze change over time using line graphs
* T27.G4.02: Calculate percentages from grouped data
* T09.G4.01: Read multiple inputs via ask blocks and apply them in conditions


ID: T27.G5.03
Topic: T27 – Data Analysis & Storytelling
Skill: Compare data from two sensors or sources
Description: Students analyze two logs (voice commands vs actual actions) to spot mismatches and hypothesize causes. They use side-by-side table comparison or manual inspection to identify discrepancies between expected and actual data.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G3.04: Separate raw data from summary data
* T27.G5.02: Correlate two variables visually


ID: T27.G5.04
Topic: T27 – Data Analysis & Storytelling
Skill: Present findings using slides or mini reports
Description: Learners assemble one chart + one key insight + one recommendation in a short presentation, practicing clear data-driven communication for specific audiences.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G3.04: Separate raw data from summary data
* T27.G5.01: Build a simple interactive dashboard with filter widgets


ID: T27.G6.01
Topic: T27 – Data Analysis & Storytelling
Skill: Filter table rows using multiple conditions
Description: Students use CreatiCode table blocks to filter rows by compound conditions (e.g., keep rows where score > 50 AND level = "Forest") before computing summaries or drawing charts, enabling more sophisticated data subset analysis.

Dependencies:
* T27.G4.02d: Filter table rows by condition
* T09.G4.01: Read multiple inputs via ask blocks and apply them in conditions
* T09.G4.04: Trace code with variables to predict outcomes
* T26.G4.04: Plan a one-week observation schedule for a variable
* T27.G5.03: Compare data from two sensors or sources


ID: T27.G6.01b
Topic: T27 – Data Analysis & Storytelling
Skill: Look up values across tables (VLOOKUP)
Description: Students use 'item in column [age] of [students v] where column [name] equals [John]' to retrieve related information from tables, similar to spreadsheet VLOOKUP operations. This enables cross-referencing data from different sources (e.g., looking up student scores by matching names across two tables).

Dependencies:
* T27.G5.01b: Group data by category and compute statistics (GROUP BY)
* T09.G4.04: Trace code with variables to predict outcomes


ID: T27.G6.02
Topic: T27 – Data Analysis & Storytelling
Skill: Compare two groups using data
Description: Learners split data into two groups (Version A vs Version B) and evaluate which performs better by comparing averages using aggregation blocks, calculating the difference between group means, and stating conclusions about whether differences are large or small relative to the data range.

Dependencies:
* T08.G4.01: Use an if-else block with compound conditions
* T09.G4.04: Trace code with variables to predict outcomes
* T26.G4.04: Plan a one-week observation schedule for a variable
* T27.G6.01: Filter table rows using multiple conditions


ID: T27.G6.02b
Topic: T27 – Data Analysis & Storytelling
Skill: Create pivot tables for multi-dimensional analysis
Description: Students use 'pivot [data v] into [summary v] row groups [grade,gender] columns [score] methods [average]' to create multi-dimensional summaries (e.g., average scores broken down by both grade AND gender). This enables complex comparative analysis across multiple grouping variables simultaneously.

Dependencies:
* T27.G5.01b: Group data by category and compute statistics (GROUP BY)
* T10.G4.01: Use list length and item access in expressions


ID: T27.G6.03
Topic: T27 – Data Analysis & Storytelling
Skill: Identify trends and patterns in time-series data
Description: Students analyze multi-week data to identify trends (increasing, decreasing, cyclical patterns) and articulate patterns with supporting evidence from the data. They distinguish between short-term fluctuations and long-term trends.

Dependencies:
* T27.G5.02: Correlate two variables visually
* T27.G6.01: Filter table rows using multiple conditions
* T09.G4.04: Trace code with variables to predict outcomes


ID: T27.G6.03b
Topic: T27 – Data Analysis & Storytelling
Skill: Export and import data using CSV files
Description: Students use 'export table [data v] as [analysis_results]' to save analysis results as CSV files for sharing, and 'import file into table [imported v]' to load external data. This enables real-world data exchange and collaboration beyond CreatiCode.

Dependencies:
* T27.G6.01: Filter table rows using multiple conditions
* T06.G4.01: Sequence multiple sprite events


ID: T27.G6.04
Topic: T27 – Data Analysis & Storytelling
Skill: Create structured summaries for AI input
Description: Learners condense findings into structured text formats (key metric, insight, recommended action) that can be copied into AI assistants like XO for further analysis or to generate reports, bridging data analysis with AI prompt engineering.

Dependencies:
* T06.G4.01: Sequence multiple sprite events
* T09.G4.01: Read multiple inputs via ask blocks and apply them in conditions
* T09.G4.04: Trace code with variables to predict outcomes
* T26.G4.04: Plan a one-week observation schedule for a variable
* T27.G6.02: Compare two groups using data


ID: T27.G7.01
Topic: T27 – Data Analysis & Storytelling
Skill: Build multi-chart dashboards with linked filters
Description: Students create dashboards with multiple charts (bar + line) that respond to the same filter variable (using shared variables and event broadcasting), providing cohesive analysis for complex apps. When one filter changes, all charts update together.

Dependencies:
* T10.G4.01: Use list length and item access in expressions
* T26.G5.04: Separate raw data from summary data
* T27.G6.03: Identify trends and patterns in time-series data
* T27.G6.04: Create structured summaries for AI input


ID: T27.G7.01b
Topic: T27 – Data Analysis & Storytelling
Skill: Integrate Google Sheets for cloud collaboration
Description: Students use 'read from google sheet: url [...] into table [data v]' to import shared data and 'write into google sheet: ... from table [results v]' to publish findings. This enables real-time collaboration and data sharing beyond CreatiCode, connecting to professional cloud workflows.

Dependencies:
* T27.G6.03b: Export and import data using CSV files
* T06.G5.01: Broadcast a custom message and respond in another sprite


ID: T27.G7.02
Topic: T27 – Data Analysis & Storytelling
Skill: Compare predictions to actual outcomes
Description: Learners compare predicted values versus actual outcomes (e.g., XO's time estimate vs actual time), calculate the difference (residual) for each prediction, and identify patterns in errors to detect systematic over- or under-prediction.

Dependencies:
* T08.G5.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G5.04: Separate raw data from summary data
* T27.G7.01: Build multi-chart dashboards with linked filters


ID: T27.G7.02b
Topic: T27 – Data Analysis & Storytelling
Skill: Calculate moving averages for trend smoothing
Description: Students use 'value from [simple v] moving average window [7] of list [daily_scores v]' to calculate rolling averages that reveal underlying trends by reducing noise in time-series data. They compare raw vs smoothed charts to interpret patterns more clearly.

Dependencies:
* T27.G6.03: Identify trends and patterns in time-series data
* T27.G7.01: Build multi-chart dashboards with linked filters
* T10.G4.01: Use list length and item access in expressions


ID: T27.G7.02c
Topic: T27 – Data Analysis & Storytelling
Skill: Automate chart updates with variables
Description: Students learn to connect chart blocks to table variables so that when data changes (via widget interaction, new imports, or computed updates), charts automatically redraw without manual regeneration. This prepares for automated reporting and dynamic dashboards.

Dependencies:
* T27.G7.01: Build multi-chart dashboards with linked filters
* T09.G6.01: Model real-world quantities using variables and formulas


ID: T27.G7.03
Topic: T27 – Data Analysis & Storytelling
Skill: Evaluate fairness metrics across user groups
Description: Students compute simple success rates or accuracy metrics separately for different user groups (e.g., by age or region), compare the results, and discuss any disparities found, tying to AI4K12's ethical lens for fairness evaluation.

Dependencies:
* T08.G5.01: Use a simple if in a script
* T09.G3.05: Trace code with variables to predict outcomes
* T26.G5.04: Separate raw data from summary data
* T27.G7.02: Compare predictions to actual outcomes


ID: T27.G7.04
Topic: T27 – Data Analysis & Storytelling
Skill: Write findings reports for an audience
Description: Learners prepare a short report with "Finding, Evidence, Recommendation" sections aimed at teachers or peers, practicing clear data-driven communication tailored to their audience.

Dependencies:
* T06.G5.01: Broadcast a custom message and respond in another sprite
* T10.G4.01: Use list length and item access in expressions
* T26.G5.04: Separate raw data from summary data
* T27.G7.03: Evaluate fairness metrics across user groups


ID: T27.G8.01
Topic: T27 – Data Analysis & Storytelling
Skill: Determine if differences are statistically meaningful
Description: Students use simple statistical reasoning (e.g., comparing differences to typical variation, or simulating many samples to see if patterns persist) to judge whether observed differences are likely real or due to chance, documenting their assumptions and methods.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T26.G6.01: Map stakeholder questions to data requirements
* T27.G7.03: Evaluate fairness metrics across user groups


ID: T27.G8.02
Topic: T27 – Data Analysis & Storytelling
Skill: Automate report generation
Description: Learners build scripts that assemble updated charts and textual findings (using variables to populate text templates) at the press of a button, supporting repeatable reporting workflows for ongoing data monitoring.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds
* T09.G6.01: Model real-world quantities using variables and formulas
* T10.G6.01: Sort a table by a column
* T26.G6.01: Map stakeholder questions to data requirements
* T27.G7.02c: Automate chart updates with variables
* T27.G8.01: Determine if differences are statistically meaningful


ID: T27.G8.03
Topic: T27 – Data Analysis & Storytelling
Skill: Integrate data analysis into AI prompt engineering
Description: Students extract key statistics from their analysis, construct prompts that include these metrics (e.g., "Given average score=75 and 20% drop-off at level 3, suggest improvements"), send to XO, and critically evaluate whether the AI's recommendations align with the data.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi‑event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T26.G6.01: Map stakeholder questions to data requirements
* T27.G8.02: Automate report generation


ID: T27.G8.04
Topic: T27 – Data Analysis & Storytelling
Skill: Publish data stories to a shared platform
Description: Learners create polished data stories with charts, written context, ethical considerations, and calls to action, then publish to CreatiCode's sharing feature or export as a web page for others to view and learn from.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi‑event program
* T09.G6.01: Model real-world quantities using variables and formulas
* T26.G6.01: Map stakeholder questions to data requirements
* T27.G8.03: Integrate data analysis into AI prompt engineering


---
# END OF T27 UPDATED SECTION
