## T10 – Lists & Tables

# PHASE 16 MAJOR OPTIMIZATION - List & Table Mastery (December 2025)
#
# KEY CHANGES IN PHASE 16:
# 1. REBALANCED PROGRESSION (G3/G4):
#    - Moved basic list operations (Insert, Replace, Find Position) from G4 to G3.
#    - G3 now covers all fundamental list manipulations.
#    - G4 focuses on algorithms, parallel lists, and data patterns.
#
# 2. CONSOLIDATED STATISTICS (G4):
#    - Merged individual Sum/Avg/Min/Max skills into one "Built-in Statistics" skill.
#    - Added manual algorithm versions as distinct skills for CS depth.
#
# 3. CLARIFIED FUNCTIONAL PATTERNS (G4 vs G7):
#    - G4: Imperative loops ("Update all items", "Accumulate total").
#    - G7: Functional abstractions ("Map", "Reduce", "Filter").
#
# 4. AI & DATA SCIENCE INTEGRATION (G7/G8):
#    - Refined AI data skills to distinguish between processing (G7) and real-time interaction (G8).
#    - Added explicit streaming data patterns.
#
# 5. STRICT DEPENDENCY MANAGEMENT:
#    - Enforced X-2 rule for advanced G8 algorithms (linking to G6/G7 structures).
#    - Ensured no gaps in K-8 progression.
#
# SKILL COUNTS:
#    - GK: 13 skills (Foundational sorting/classifying)
#    - G1: 13 skills (Multi-condition filtering)
#    - G2: 14 skills (Picture tables & logic)
#    - G3: 29 skills (+4 from G4: Insert, Replace, Find, Delete-by-val)
#    - G4: 38 skills (Optimized from 48)
#    - G5: 40 skills (Table mastery)
#    - G6: 31 skills (Nested lists & advanced tables)
#    - G7: 33 skills (Data science & AI pipelines)
#    - G8: 33 skills (Advanced CS algorithms)
#
---

## GRADE K (13 skills)

ID: T10.GK.01
Topic: T10 – Lists & Tables
Skill: Classify picture cards into two groups by attribute
Description: **Student task:** Drag 4-6 picture cards into 2 colored boxes based on a visible attribute (color, shape, or type). **Visual scenario:** Picture cards show: red ball, blue car, red apple, blue block. Two boxes labeled "Red things" and "Blue things." **Correct answer:** Red ball and red apple go in "Red things" box; blue car and blue block go in "Blue things" box. **Why this matters:** Sorting is the first step in organizing data—computers store related items together in lists. _Implementation note: Drag-drop sorting with visual feedback. Auto-graded by final card positions in boxes. CSTA: EK-ALG-AF-01._

ID: T10.GK.02
Topic: T10 – Lists & Tables
Skill: Count items in each sorted group
Description: **Student task:** After sorting picture cards into groups, count how many items are in each group and tap the correct count from picture choices. **Visual scenario:** Two boxes after sorting: "Pets" box has 3 animals (cat, dog, fish), "Wild animals" box has 2 animals (lion, bear). Question: "How many pets?" **Correct answer:** Tap the picture showing 3 dots. **Why this matters:** Counting items in a group is like finding the "length" of a list—a key operation programmers use constantly. _Implementation note: Multi-choice with dot representations (1-4 dots). Audio reads numbers on tap. CSTA: EK-ALG-AF-01._
Dependencies:
* T10.GK.01: Classify picture cards into two groups by attribute

ID: T10.GK.03
Topic: T10 – Lists & Tables
Skill: Compare group sizes to find which has more
Description: **Student task:** Look at two groups of sorted items and tap the group that has more items. **Visual scenario:** Two boxes after sorting: "Circles" box has 4 shapes, "Triangles" box has 2 shapes. Question: "Which group has more?" **Correct answer:** Tap the "Circles" box. **Why this matters:** Comparing group sizes helps us make decisions about data—like finding which team has more players or which category is most popular. _Implementation note: Visual comparison activity with highlighting on selection. CSTA: EK-ALG-AF-01._
Dependencies:
* T10.GK.02: Count items in each sorted group

ID: T10.GK.04
Topic: T10 – Lists & Tables
Skill: Add a new item to the correct group
Description: **Student task:** Look at two boxes with sorted picture cards. A new picture card appears. Drag it to the correct box. **Visual scenario:** "Animals" box has dog and cat pictures. "Foods" box has apple and banana pictures. New card shows a bird. **Correct answer:** Drag the bird card to the "Animals" box. **Why this matters:** This is like the "add to list" operation—putting a new item where it belongs. _Implementation note: Drag-drop with snap-to-box feedback. CSTA: EK-ALG-AF-01._
Dependencies:
* T10.GK.01: Classify picture cards into two groups by attribute

ID: T10.GK.05
Topic: T10 – Lists & Tables
Skill: Find the first and last item in a row
Description: **Student task:** Look at a row of 3-5 picture cards arranged from left to right. Tap the first item, then tap the last item. **Visual scenario:** Five picture cards in a row: apple, banana, orange, grape, watermelon. **Correct answer:** Tap apple (first), then tap watermelon (last). _Implementation note: Sequential tap activity with visual order indicators. CSTA: EK-ALG-AF-01._
Dependencies:
* T01.GK.04: Find the first and last pictures

ID: T10.GK.06
Topic: T10 – Lists & Tables
Skill: Read information from a simple picture table
Description: **Student task:** Look at a picture table showing which child likes which fruit. Answer questions by tapping the correct cell. **Visual scenario:** 2x3 table with rows for "Sam" and "Lia", columns for "Fruit" showing apple and banana icons. Question: "What does Sam like?" **Correct answer:** Tap the cell showing Sam's fruit (apple). **Why this matters:** Tables organize information in rows and columns—just like your teacher's attendance chart that shows who is here each day, or a restaurant menu that shows food names and prices! This is how databases and spreadsheets store data. _Implementation note: Interactive table with cell highlighting on tap. CSTA: EK-ALG-AF-01._
Dependencies:
* T10.GK.01: Classify picture cards into two groups by attribute

ID: T10.GK.07
Topic: T10 – Lists & Tables
Skill: Match related items by drawing lines
Description: **Student task:** Draw lines or drag to match pairs of related items. **Visual scenario:** Left column shows 3 animals (dog, fish, bird). Right column shows 3 homes (doghouse, fishbowl, nest). **Correct answer:** Dog→doghouse, fish→fishbowl, bird→nest. **Why this matters:** Matching pairs is like a lookup operation—finding related information across two lists. _Implementation note: Line-drawing or drag-drop matching with visual connection feedback. CSTA: EK-ALG-AF-01._
Dependencies:
* T10.GK.01: Classify picture cards into two groups by attribute

ID: T10.GK.08
Topic: T10 – Lists & Tables
Skill: Filter items by a special mark and count them
Description: **Student task:** Look at a collection of picture cards. Some have a star mark. Tap all cards with stars, then count how many you found. **Visual scenario:** 6 picture cards showing toys. 3 cards have gold stars on them (teddy bear, ball, puzzle). **Correct answer:** Tap the 3 starred cards, then tap "3" from the number choices. **Why this matters:** This is filtering—selecting only the items that match a condition, a core data operation. _Implementation note: Multi-tap selection with counter display. CSTA: EK-ALG-AF-01._
Dependencies:
* T10.GK.02: Count items in each sorted group

ID: T10.GK.09
Topic: T10 – Lists & Tables
Skill: Explain why we group things together using picture cards
Description: **Student task:** After sorting picture cards into groups, explain WHY you put certain cards together. Point to each group and say what makes those cards belong together. **Visual scenario:** Student has sorted 6 animal cards into "Pets" (dog, cat, fish) and "Farm animals" (cow, pig, chicken). Student records or tells a partner: "I put dog, cat, and fish together because they live in people's homes. I put cow, pig, and chicken together because they live on farms." **Why this matters:** Explaining your grouping helps others understand your thinking and is the first step toward explaining data structure choices in programming. _Implementation note: Voice recording or partner activity. Teacher/AI evaluates explanation for clear reasoning about shared attributes. CSTA: EK-CS-PC-01._
Dependencies:
* T10.GK.01: Classify picture cards into two groups by attribute
* T10.GK.04: Add a new item to the correct group

ID: T10.GK.10
Topic: T10 – Lists & Tables
Skill: Find lists and tables in everyday life (picture examples)
Description: **Student task:** Look at pictures of real-world items and tap which ones are lists or tables. **Visual scenario:** Four pictures: (A) a grocery shopping list on paper, (B) a single apple, (C) a class schedule showing days and subjects in a grid, (D) a photograph of a dog. **Correct answer:** Tap A (shopping list is a list!) and C (class schedule is a table!). B and D are single items, not collections. **Why this matters:** Lists and tables are everywhere—once you recognize them, you can organize information like a computer does! _Implementation note: Multi-select with picture recognition. Audio explains "A list is a collection of items in order. A table organizes information in rows and columns." CSTA: EK-ALG-AF-01._
Dependencies:
* T10.GK.06: Read information from a simple picture table

ID: T10.GK.11
Topic: T10 – Lists & Tables
Skill: Predict what changes when an item is removed from a sorted group
Description: **Student task:** Look at a sorted group of picture cards, then predict what the group will look like after one item is removed. **Visual scenario:** A "Pets" group has 4 cards: cat, dog, fish, bird. The fish card is crossed out. Question: "How many pets are left? Which ones?" **Correct answer:** 3 pets left: cat, dog, bird. **Why this matters:** When we remove something from a collection, the collection changes—programmers call this "deleting" from a list. _Implementation note: Prediction activity where students tap remaining items and select the new count. Audio: "What happens to our group when we take one away?" CSTA: EK-ALG-AF-01._
Dependencies:
* T10.GK.04: Add a new item to the correct group
* T10.GK.02: Count items in each sorted group

ID: T10.GK.12
Topic: T10 – Lists & Tables
Skill: Trace through a simple sorting plan step by step
Description: **Student task:** Watch a sorting animation and predict what happens at each step, then verify by tapping "next." **Visual scenario:** 4 mixed fruit cards need to be sorted into 2 boxes (Apples, Oranges). Animation shows: Step 1: Pick up first card (red apple). Question: "Which box?" Student taps "Apples" box. Step 2: Pick up second card (orange). Question: "Which box?" Continue until all 4 cards are sorted. **Correct answer:** Students correctly predict each placement before it happens. **Why this matters:** Tracing step-by-step is how programmers check if their sorting works correctly—following the process one item at a time. _Implementation note: Step-by-step animation with prediction prompts. Audio: "Where does this card go? Tap to guess, then watch!" CSTA: EK-ALG-AF-02._
Dependencies:
* T10.GK.04: Add a new item to the correct group
* T10.GK.01: Classify picture cards into two groups by attribute

ID: T10.GK.13
Topic: T10 – Lists & Tables
Skill: Predict what happens when we reverse a row of items
Description: **Student task:** Look at a row of 4 picture cards in order, then predict what order they will be in after reversing (flipping the row). **Visual scenario:** Row shows: apple → banana → orange → grape. Question: "If we flip the row around, what will be first? What will be last?" **Correct answer:** Grape will be first, apple will be last. The new order is: grape → orange → banana → apple. **Why this matters:** Reversing is a common list operation—like "undo" in a game or playing a video backwards. Programmers use `reverse [list]` to flip data order. _Implementation note: Visual animation showing row being flipped; students tap predictions before seeing result. Audio: "Let's turn this row around! What will be at the front now?" CSTA: EK-ALG-AF-02._
Dependencies:
* T10.GK.05: Find the first and last item in a row
* T10.GK.12: Trace through a simple sorting plan step by step

## GRADE 1 (13 skills)

ID: T10.G1.01
Topic: T10 – Lists & Tables
Skill: Classify items using two combined rules (AND condition)
Description: **Student task:** Drag 6-8 items into groups where each item must match TWO rules (e.g., must be both "big" AND "red"). **Visual scenario:** 8 shape cards: big red circle, small red square, big blue triangle, small blue circle, big red square, small red triangle, big blue square, small blue square. Two boxes: "Big AND Red" and "Other." **Correct answer:** Only big red circle and big red square go in "Big AND Red" box; all others go in "Other" box. **Why this matters:** Filtering data often requires checking multiple conditions at once—this is the AND logic computers use. _Implementation note: Two-attribute classification with visual rule indicators. CSTA: E1-ALG-AF-01._
Dependencies:
* T10.GK.01: Classify picture cards into two groups by attribute
* T10.GK.04: Add a new item to the correct group

ID: T10.G1.02
Topic: T10 – Lists & Tables
Skill: Build a picture tally chart from data
Description: **Student task:** Count items in categories and add tally marks or picture icons to show the count. **Visual scenario:** Picture shows 5 students' snack choices: 2 chose apple, 2 chose banana, 1 chose orange. Empty chart has rows for each snack. **Correct answer:** Add 2 tally marks (or 2 apple icons) in apple row, 2 in banana row, 1 in orange row. **Why this matters:** Tally charts are how we count votes and choices—like the voting boards on game shows when audiences vote, or your classroom's "favorite book" choice board! This is the foundation of data tables. _Implementation note: Interactive chart builder with drag-drop tally marks or icons. CSTA: E1-ALG-AF-01._
Dependencies:
* T10.GK.02: Count items in each sorted group
* T10.GK.06: Read information from a simple picture table

ID: T10.G1.03
Topic: T10 – Lists & Tables
Skill: Locate specific values in a picture table
Description: **Student task:** Answer questions by finding and tapping specific cells in a picture table with 3-4 rows and 3-4 columns. **Visual scenario:** 3x3 table showing 3 students (rows) and what they have: pencils, crayons, erasers (columns with number icons). Question: "How many pencils does Lia have?" **Correct answer:** Tap the cell at Lia's row, pencils column showing "5." **Why this matters:** Finding a specific value by row and column is exactly how computers look up data in tables. _Implementation note: Interactive table with question-guided cell selection. CSTA: E1-ALG-AF-01._
Dependencies:
* T10.GK.06: Read information from a simple picture table

ID: T10.G1.04
Topic: T10 – Lists & Tables
Skill: Identify the row or column with the maximum value
Description: **Student task:** Look at a picture table and tap the row or column that has the most items in total. **Visual scenario:** 3x2 table showing students and their points. Row 1 (Sam): 5 stars. Row 2 (Lia): 8 stars. Row 3 (Max): 3 stars. Question: "Which student has the most stars?" **Correct answer:** Tap Lia's row (8 stars). **Why this matters:** Finding the maximum is a key aggregation—like finding the high score or the most popular item. _Implementation note: Visual comparison with highlighting on tap. CSTA: E1-ALG-AF-01._
Dependencies:
* T10.G1.03: Locate specific values in a picture table
* T10.GK.03: Compare group sizes to find which has more

ID: T10.G1.05
Topic: T10 – Lists & Tables
Skill: Predict and fill missing values in a table pattern
Description: **Student task:** Look at a table with a pattern in rows or columns. Some cells are empty. Drag the correct picture or number to fill the missing cells. **Visual scenario:** 3x3 table with alternating colors: Red, Blue, ?, Red, Blue, ?, Red, Blue, ?. **Correct answer:** Fill each ? with Red to continue the Red-Blue-Red pattern. **Why this matters:** Recognizing patterns in data helps predict missing values—a common task in data analysis. _Implementation note: Drag-drop pattern completion with visual feedback. CSTA: E1-ALG-AF-01._
Dependencies:
* T10.G1.03: Locate specific values in a picture table
* T01.GK.08: Find the pattern that repeats

ID: T10.G1.06
Topic: T10 – Lists & Tables
Skill: Select items matching multiple conditions (intersection)
Description: **Student task:** Look at a collection of picture cards. Find and tap all items that match TWO conditions at the same time (e.g., items that are both red AND round). **Visual scenario:** 8 cards showing shapes: red circle, blue circle, red square, green triangle, red triangle, blue square, green circle, red oval. Question: "Find all things that are both RED and ROUND." **Correct answer:** Tap only the red circle. **Why this matters:** This is the intersection of two groups—items that are in BOTH groups at once. _Implementation note: Multi-select activity with AND logic indicator. CSTA: E1-ALG-AF-01._
Dependencies:
* T10.G1.01: Classify items using two combined rules (AND condition)

ID: T10.G1.07
Topic: T10 – Lists & Tables
Skill: Select items matching either of two conditions (union)
Description: **Student task:** Look at a collection of picture cards. Find and tap all items that match EITHER one condition OR another (e.g., items that are red OR round). **Visual scenario:** 8 cards showing shapes: red circle, blue circle, red square, green triangle, red triangle, blue square, green circle, red oval. Question: "Find all things that are RED or ROUND (or both)." **Correct answer:** Tap red circle, blue circle, red square, red triangle, green circle, red oval (6 cards total—anything red OR anything round). **Why this matters:** This is the union of two groups—items that are in EITHER group. Sometimes we want anything that matches at least one rule, not both rules. _Implementation note: Multi-select activity with OR logic indicator. Compare to T10.G1.06 to distinguish AND vs OR. CSTA: E1-ALG-AF-01._
Dependencies:
* T10.G1.06: Select items matching multiple conditions (intersection)

ID: T10.G1.08
Topic: T10 – Lists & Tables
Skill: Decide whether to use one group or two groups for sorting
Description: **Student task:** Look at a collection of picture cards and decide: should we sort into ONE group (keep/discard) or TWO groups (category A/category B)? Choose the best sorting strategy. **Visual scenario:** Scenario 1: "We want to find all the red toys." → One group is best (red toys vs. not-red toys). Scenario 2: "We want to organize toys by type." → Two groups make sense (dolls vs. cars). **Correct answer:** Match each scenario to the right sorting approach. **Why this matters:** Choosing the right way to organize data is an important decision programmers make—sometimes one category is enough, sometimes you need multiple categories. _Implementation note: Matching activity connecting scenarios to strategies. CSTA: E1-ALG-AF-01._
Dependencies:
* T10.G1.01: Classify items using two combined rules (AND condition)
* T10.GK.08: Filter items by a special mark and count them

ID: T10.G1.09
Topic: T10 – Lists & Tables
Skill: Predict table cell value after a change scenario
Description: **Student task:** Look at a simple picture table, then predict what a cell will show after something changes. **Visual scenario:** Table shows 3 students and their star counts: Sam has 3 stars, Lia has 5 stars, Max has 2 stars. Story: "Max earns 2 more stars!" Question: "How many stars does Max have now?" **Correct answer:** 4 stars. **Why this matters:** Tables store information that can change—predicting the result of changes is how we check our work before making updates. _Implementation note: Story-based table update prediction; students tap the new value. CSTA: E1-ALG-AF-01._
Dependencies:
* T10.G1.03: Locate specific values in a picture table
* T10.GK.02: Count items in each sorted group

ID: T10.G1.10
Topic: T10 – Lists & Tables
Skill: Debug a picture sorting by finding misplaced items
Description: **Student task:** Look at a sorted collection and find items that are in the wrong group. **Visual scenario:** Two boxes labeled "Things with wheels" and "Things without wheels." Contents: Wheels box has: car, bicycle, apple (wrong!), skateboard. No-wheels box has: book, ball, wagon (wrong!), pencil. **Correct answer:** Tap apple (should be in no-wheels) and wagon (should be in wheels). **Why this matters:** Finding mistakes in sorted data is debugging—a skill programmers use every day to fix errors in their programs. _Implementation note: Error-detection activity with tap-to-mark incorrect items. Audio: "Oops! Someone made mistakes. Can you find the items in the wrong box?" CSTA: E1-AP-DB-01._
Dependencies:
* T10.GK.12: Trace through a simple sorting plan step by step
* T10.GK.04: Add a new item to the correct group

ID: T10.G1.11
Topic: T10 – Lists & Tables
Skill: Predict table results after multiple changes
Description: **Student task:** Track multiple changes to a picture table and predict the final state. **Visual scenario:** Starting table shows 3 students with star counts: Sam=2, Lia=3, Max=1. Story: "First, everyone gets 1 more star. Then Sam gives 1 star to Max." Questions: "How many stars does Sam have now? Lia? Max?" **Correct answer:** Sam=2 (had 3 after first change, gave 1 away), Lia=4, Max=3. **Why this matters:** Tracking multiple changes helps you predict what data will look like after running a program—essential for understanding how code affects information. _Implementation note: Multi-step prediction with running tally option. Students can use scratch paper or track mentally. CSTA: E1-ALG-AF-02._
Dependencies:
* T10.G1.09: Predict table cell value after a change scenario
* T10.G1.03: Locate specific values in a picture table

ID: T10.G1.12
Topic: T10 – Lists & Tables
Skill: Compare two groups using a simple picture chart
Description: **Student task:** Look at a picture chart with two bars made of stacked icons and answer comparison questions. **Visual scenario:** A "Favorite Pets" picture chart shows Cat bar (5 cat icons stacked) and Dog bar (3 dog icons stacked). Questions: "Which pet is more popular?" "How many more cats than dogs?" **Correct answer:** Cats are more popular (5 > 3); 2 more cats than dogs. **Why this matters:** Picture charts are how we show data visually—you see them in news, apps, and school reports. Reading them is the first step before creating them. _Implementation note: Interactive chart where students tap to count icons, then select answers. Audio: "Count the icons to compare!" CSTA: 1A-DA-07._
Dependencies:
* T10.GK.03: Compare group sizes to find which has more
* T10.G1.02: Build a picture tally chart from data

ID: T10.G1.13
Topic: T10 – Lists & Tables
Skill: Create a simple two-column table from picture pairs
Description: **Student task:** Look at matching pairs of pictures and organize them into a 2-column table. **Visual scenario:** 4 picture pairs scattered: (dog, bone), (cat, fish), (bird, seeds), (rabbit, carrot). Empty table with columns: "Animal" and "Food." **Correct answer:** Create 4 rows matching each animal to its food. **Why this matters:** Tables show relationships between things—like which pet eats which food, or which student has which backpack. Creating tables is how we organize paired information. _Implementation note: Drag-and-drop table builder. Students drag animal to first column, then drag matching food to second column in same row. Audio: "Match each animal with what it eats!" CSTA: 1A-DA-06._
Dependencies:
* T10.G1.02: Build a picture tally chart from data
* T10.GK.07: Match related items by drawing lines

## GRADE 2 (14 skills)

ID: T10.G2.01
Topic: T10 – Lists & Tables
Skill: Convert a written list into a structured table
Description: **Student task:** Read a list of information and fill in a table with labeled rows and columns. **Visual scenario:** Text list: "Sam has 3 apples, Lia has 2 oranges, Max has 5 bananas." Empty table with columns: Name, Fruit, Count. **Correct answer:** Fill 3 rows: (Sam, apples, 3), (Lia, oranges, 2), (Max, bananas, 5). **Why this matters:** Converting unstructured information into organized tables is a key data entry skill. _Implementation note: Interactive table builder with drag-drop or type-in fields. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G1.03: Locate specific values in a picture table

ID: T10.G2.02
Topic: T10 – Lists & Tables
Skill: Append a new row to an existing table
Description: **Student task:** Look at an existing picture table. You're given new information for a new student. Add a new row by filling in all the column values. **Visual scenario:** Table has 2 students with columns: Name, Favorite Color. You get: "Add Tom who likes Green." **Correct answer:** Add row 3: (Tom, Green). **Why this matters:** Adding rows is how tables grow—like adding new entries to a database or spreadsheet. _Implementation note: Interactive row addition with column-guided input. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G2.01: Convert a written list into a structured table

ID: T10.G2.03
Topic: T10 – Lists & Tables
Skill: Compare values across two rows in a table
Description: **Student task:** Look at two different rows in a table and answer questions about differences or similarities. **Visual scenario:** Table with columns: Student, Math Score, Reading Score. Row 1: (Sam, 85, 90). Row 2: (Lia, 80, 95). Question: "Who has a higher Math score?" **Correct answer:** Sam. "Who has a higher Reading score?" **Correct answer:** Lia. **Why this matters:** Comparing rows helps answer questions like "who performed better?" or "which product costs more?" _Implementation note: Guided comparison questions with row highlighting. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G2.01: Convert a written list into a structured table

ID: T10.G2.04
Topic: T10 – Lists & Tables
Skill: Reorder table rows by a column value (manual sorting)
Description: **Student task:** Rearrange rows in a simple table to put them in order by one column (e.g., from most to least points). **Visual scenario:** 3-row table: (Sam, 5 points), (Lia, 9 points), (Max, 3 points). Instruction: "Arrange from most to least points." **Correct answer:** Lia (9), Sam (5), Max (3). **Why this matters:** Sorting makes data easier to analyze—finding the top performer or lowest value becomes instant. _Implementation note: Drag-drop row reordering with visual order indicators. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G2.01: Convert a written list into a structured table
* T01.G1.02: Put pictures in order to plant a seed

ID: T10.G2.05
Topic: T10 – Lists & Tables
Skill: Filter table rows by marking those matching a condition
Description: **Student task:** Look at a table and mark all rows where a specific column matches a condition. **Visual scenario:** 5-row table with student scores. Question: "Mark all students with 10 or more points." Rows: (Sam, 8), (Lia, 12), (Max, 15), (Eva, 6), (Tom, 10). **Correct answer:** Mark Lia, Max, and Tom rows. **Why this matters:** Filtering is how we find relevant data—like finding all orders over $100 or all students who passed. _Implementation note: Multi-select row marking with condition indicator. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G2.01: Convert a written list into a structured table

ID: T10.G2.06
Topic: T10 – Lists & Tables
Skill: Count filtered rows that satisfy a condition
Description: **Student task:** Look at a table and count how many rows satisfy a condition. **Visual scenario:** 5-row table with student scores: (Sam, 8), (Lia, 12), (Max, 15), (Eva, 6), (Tom, 10). Question: "How many students scored more than 5?" **Correct answer:** 5 students (all of them: Sam 8, Lia 12, Max 15, Eva 6, Tom 10 are all greater than 5). **Why this matters:** Counting filtered results answers questions like "how many people registered?" or "how many errors occurred?" _Implementation note: Count-focused activity with condition highlighting. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G2.05: Filter table rows by marking those matching a condition

ID: T10.G2.07
Topic: T10 – Lists & Tables
Skill: Recognize real-world examples of lists and tables
Description: Students transition from picture tables to recognizing that code can have "lists" - ordered collections of items that the computer stores and uses. **Student task:** Look at picture scenarios and tap which ones represent "lists" (ordered collections). **Visual scenario:** Four pictures: (A) shopping list on paper, (B) single ball, (C) music playlist on phone, (D) leaderboard with ranked players. **Correct answer:** Tap A, C, and D (all are ordered collections). **Why this matters:** Lists are everywhere in computing—playlists, contact lists, high scores, search results. Recognizing them prepares you for programming. _Implementation note: Multi-select concept recognition activity. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G2.01: Convert a written list into a structured table

ID: T10.G2.08
Topic: T10 – Lists & Tables
Skill: Trace through a table lookup step by step
Description: **Student task:** Given a picture table and a lookup question, show the step-by-step process to find the answer. **Visual scenario:** Table shows 4 students (rows) with columns: Name, Pet, Favorite Color. Question: "What pet does Sam have?" Step 1: Find the Name column. Step 2: Go down to find "Sam" row. Step 3: Stay in that row, move to Pet column. Step 4: Read the answer: "Dog." Student taps cells in order to show the lookup path. **Correct answer:** Tap Name header → Sam cell → Pet cell in Sam's row → Say "Dog." **Why this matters:** Tracing step-by-step is how we debug and verify our work—an essential computational thinking skill. _Implementation note: Sequential tap activity showing lookup path with visual trail. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G2.01: Convert a written list into a structured table
* T10.G1.03: Locate specific values in a picture table

ID: T10.G2.09
Topic: T10 – Lists & Tables
Skill: Connect picture tables to real-world apps
Description: **Student task:** Match picture tables to real-world applications that use similar data organization. **Visual scenario:** Three mini-tables: (1) Name-Phone Number table, (2) Day-Subject-Time table, (3) Item-Price table. Three apps: Contacts app, Calendar app, Shopping app. **Correct answer:** Match Name-Phone to Contacts, Day-Subject-Time to Calendar, Item-Price to Shopping. **Why this matters:** The tables you see in apps work just like the picture tables you're learning! YouTube playlists are tables (video name, length, thumbnail). App store search results are tables (app name, rating, price). Game leaderboards are tables (player name, score, rank). Same rows and columns, just on a screen! _Implementation note: Drag-and-drop matching with real app screenshots. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G2.07: Recognize real-world examples of lists and tables
* T10.G2.01: Convert a written list into a structured table

ID: T10.G2.10
Topic: T10 – Lists & Tables
Skill: Predict and verify table changes after adding or removing rows
Description: **Student task:** Look at a table, then predict what it will look like after adding or removing a row. Verify your prediction. **Visual scenario:** Table has 3 students: (Sam, 10 points), (Lia, 8 points), (Max, 12 points). Instruction: "We add a new student: Tom with 7 points." Student draws/selects the new table with 4 rows. Then: "Sam leaves the class." Student shows the table now has 3 rows without Sam. **Correct answer:** After add: 4-row table with Tom at bottom. After remove: 3-row table without Sam, others shift up. **Why this matters:** Predicting changes before making them helps catch mistakes—this is how programmers think before they code! _Implementation note: Table prediction with before/after comparison. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G2.02: Append a new row to an existing table

ID: T10.G2.11
Topic: T10 – Lists & Tables
Skill: Trace step-by-step through a multi-condition filter on picture table
Description: **Student task:** Look at a picture table and follow a two-step filtering process to find specific rows. **Visual scenario:** Table shows 6 students with columns: Name, Grade, Sport. Step 1: "Circle all students in Grade 2." Step 2: "Of those circled, put a star on students who play Soccer." **Correct answer:** Students trace through both conditions sequentially, first identifying all Grade 2 students (filter 1), then among those, identifying Soccer players (filter 2). **Why this matters:** Real data searches often use multiple filters—this step-by-step tracing builds the mental model for complex queries. _Implementation note: Two-phase marking activity on table; visual shows narrowing of results. CSTA: E2-ALG-AF-01._
Dependencies:
* T10.G2.05: Filter table rows by marking those matching a condition
* T10.G1.06: Select items matching multiple conditions (intersection)

ID: T10.G2.12
Topic: T10 – Lists & Tables
Skill: Design a simple classification system for new items
Description: **Student task:** Given a collection of new items, design your own classification groups and sort the items. **Visual scenario:** 8 new toy picture cards that haven't been sorted before (robot, doll, puzzle, ball, car, blocks, stuffed animal, board game). Students create 2-3 group labels and sort all items. **Correct answer:** Multiple valid solutions exist (e.g., "Indoor/Outdoor," "With batteries/Without batteries," "Play alone/Play together"). Students must: (1) create clear group names, (2) sort all items consistently, (3) explain their classification rule. **Why this matters:** Designing your own categories is how database designers think—they decide HOW to organize data before storing it. This is the first step toward designing data structures. _Implementation note: Open-ended sorting with student-created labels. Teacher/AI evaluates for consistency (all items follow the rule) and clarity (rule is understandable). CSTA: E2-ALG-AB-01._
Dependencies:
* T10.G2.01: Convert a written list into a structured table
* T10.G1.08: Decide whether to use one group or two groups for sorting

ID: T10.G2.13
Topic: T10 – Lists & Tables
Skill: Read and answer questions from a bar chart or picture graph
Description: **Student task:** Look at a bar chart or picture graph with 3-4 categories and answer questions about the data. **Visual scenario:** A horizontal bar chart shows "Books Read This Month": Sam (4 books), Lia (7 books), Max (3 books), Eva (5 books). Questions: "Who read the most books?" "How many books did everyone read in total?" "Who read more than 4 books?" **Correct answer:** Lia read the most (7); total is 19 books; Lia (7) and Eva (5) read more than 4. **Why this matters:** Bar charts are everywhere—weather apps, game leaderboards, YouTube video stats. Being able to read them quickly helps you understand information at a glance. _Implementation note: Interactive chart with tap-to-highlight bars; students select answers from multiple choice. CSTA: 1A-DA-07._
Dependencies:
* T10.G1.12: Compare two groups using a simple picture chart
* T10.G2.06: Count filtered rows that satisfy a condition

ID: T10.G2.14
Topic: T10 – Lists & Tables
Skill: Design a sorting rule and explain it to a partner
Description: **Student task:** Create your own sorting rule for a set of items, sort them, and explain your rule clearly to a partner. **Visual scenario:** 8 picture cards showing different foods (pizza, salad, apple, ice cream, sandwich, banana, cookie, broccoli). Students choose a sorting rule (e.g., "healthy vs treat," "hot vs cold," "fruit vs not fruit"), sort the cards, then explain: "My rule is ___. I put ___ in this group because ___." **Correct answer:** Multiple valid rules exist. Success is measured by: (1) all items sorted consistently, (2) partner can understand the rule, (3) partner can correctly predict where a new item would go. **Why this matters:** Explaining sorting rules is the first step toward writing code comments and documentation—others need to understand YOUR logic. Real programmers always explain why they organized data a certain way. _Implementation note: Partner activity or AI partner simulation. Students speak or type their rule explanation. CSTA: 1A-CS-PC-01._
Dependencies:
* T10.G2.12: Design a simple classification system for new items
* T10.GK.09: Explain why we group things together using picture cards

