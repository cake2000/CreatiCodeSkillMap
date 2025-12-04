## GRADE 3 (29 skills)

ID: T10.G3.01
Topic: T10 – Lists & Tables
Skill: Create a new list variable
Description: Students create a new list variable in the Variables palette by clicking "Make a List" and giving it a descriptive name (e.g., "fruits", "scores", "inventory"). Lists are containers that can hold multiple values, unlike regular variables which hold only one value. Students recognize that this is the first step before any list operations can be performed, and verify the empty list appears in the Variables palette.
Dependencies:
* T09.G3.01: Create a new variable

ID: T10.G3.02
Topic: T10 – Lists & Tables
Skill: Add an item to the end of a list
Description: Students use the `add [item] to [list]` block to add items one at a time to the end of a list. They observe how each item is added in sequence (1, 2, 3...) and note that lists grow dynamically as items are added. Students practice adding 3-4 items and use the list monitor to verify the growing list.
Dependencies:
* T10.G3.01: Create a new list variable

ID: T10.G3.03
Topic: T10 – Lists & Tables
Skill: Trace list index access step by step
Description: Before reading items from lists, students practice tracing through the relationship between list positions and items. Given a small list displayed on screen (e.g., ["apple", "banana", "cherry"]), students identify what item is at position 1, position 2, etc., understanding that CreatiCode lists start counting at 1 (not 0 like many programming languages). They predict what `item (2) of [fruits]` will return before running the code, then verify their prediction. This foundational tracing skill prevents common errors like expecting position 0 to work or confusing the item value with its position number. Students practice with 3-4 item lists using the list monitor for visual feedback.
Dependencies:
* T10.G3.02: Add an item to the end of a list
* T10.G3.15: Display a list monitor on the stage

ID: T10.G3.04
Topic: T10 – Lists & Tables
Skill: Read items from a list by position (index starts at 1)
Description: Students use the `item (1) of [list]` block to retrieve specific items from a list by their position number (index). The first item is at position 1, second at position 2, etc. Students practice reading different positions and displaying or using the retrieved values, verifying the correct item is returned.
Dependencies:
* T10.G3.03: Trace list index access step by step

ID: T10.G3.05
Topic: T10 – Lists & Tables
Skill: Get the length of a list
Description: Students use the `length of [list]` block to find how many items are in a list. They observe that as items are added or removed, the length changes accordingly. This is essential for knowing the bounds when accessing list items and avoiding out-of-range errors.
Dependencies:
* T10.G3.02: Add an item to the end of a list

ID: T10.G3.06
Topic: T10 – Lists & Tables
Skill: Delete an item at a specific position
Description: Students use the `delete (position) of [list]` block to remove an item from a specific position in the list. They observe how items after the deleted position shift down (e.g., item 3 becomes item 2) and verify that the list length decreases by 1. Students practice deleting items from different positions (beginning, middle, end) and predict the resulting list state.
Dependencies:
* T10.G3.04: Read items from a list by position (index starts at 1)
* T10.G3.05: Get the length of a list

ID: T10.G3.07
Topic: T10 – Lists & Tables
Skill: Clear all items from a list
Description: Students use the `delete all of [list]` block to remove every item from a list at once, returning it to empty. Clearing is useful for starting fresh or resetting for a new game. Students observe that after clearing, the list length becomes 0 and verify the list monitor shows an empty list.
Dependencies:
* T10.G3.06: Delete an item at a specific position
* T10.G3.05: Get the length of a list

ID: T10.G3.08
Topic: T10 – Lists & Tables
Skill: Predict list state after delete operations
Description: Students develop mental models of how lists change when items are deleted. Given a starting list shown in the monitor (e.g., [10, 20, 30, 40, 50]), they predict the resulting list after operations like "delete (2) of list" or "delete (4) of list". They draw or write out the expected result, paying special attention to how items shift positions: when item 2 is deleted, what was item 3 becomes the new item 2. Students verify predictions by running the code and comparing actual vs. expected results. This predictive skill builds debugging ability and prevents confusion about why items "moved" after deletion. Practice includes deleting from beginning (position 1), middle, and end positions.
Dependencies:
* T10.G3.06: Delete an item at a specific position
* T10.G3.16: Predict and trace list changes step by step

ID: T10.G3.09
Topic: T10 – Lists & Tables
Skill: Loop through each item in a list
Description: Students use the `for each [item] in [list]` block to automatically visit every item in sequence. Unlike counted repeat loops where you specify a number of repetitions, this block iterates through all items regardless of list length. Students perform simple actions on each item (e.g., say each fruit name) and observe that every item is processed exactly once. Keep the list short (3-4 items) and actions simple.
Dependencies:
* T07.G3.01: Use a counted repeat loop
* T10.G3.02: Add an item to the end of a list
* T10.G3.04: Read items from a list by position (index starts at 1)

ID: T10.G3.10
Topic: T10 – Lists & Tables
Skill: Check if a list contains a specific item
Description: Students use the `[list] contains [item]?` block to check whether a value exists in a list. They combine this with conditionals to make decisions based on list membership (e.g., "if my fruits list contains 'apple' then say 'I have an apple!'"). Students test with items that are in the list and items that are not.
Dependencies:
* T10.G3.02: Add an item to the end of a list
* T08.G3.04: Use a simple if in a script

ID: T10.G3.11
Topic: T10 – Lists & Tables
Skill: Count items in a list that match a condition
Description: Students loop through a short list and count items that match a simple condition (e.g., "count numbers greater than 5" or "count items equal to 'apple'"). They use a counter variable that increments inside a conditional inside a loop. Students predict the count before running and verify their prediction matches the result. Real-world applications: count how many classmates chose pizza in a lunch survey, count scores above the passing grade of 60, count items in stock that are below the reorder level, count how many days had temperature above 80°F.
Dependencies:
* T10.G3.09: Loop through each item in a list
* T08.G3.04: Use a simple if in a script
* T09.G3.01: Increment and decrement a variable

ID: T10.G3.12
Topic: T10 – Lists & Tables
Skill: Check if a list is empty before accessing
Description: Students check whether a list is empty (has zero items) before trying to read from it, to avoid errors. They use the `length of [list] = 0` condition in an if-statement to guard list access. This defensive programming pattern prevents crashes when dealing with lists that might be empty.
Dependencies:
* T10.G3.05: Get the length of a list
* T08.G3.04: Use a simple if in a script

ID: T10.G3.13
Topic: T10 – Lists & Tables
Skill: Trace empty list edge cases
Description: Students learn to identify and handle the empty list scenario through tracing exercises. They trace through code that attempts to read from an empty list (length = 0) and predict what will happen: trying to access `item (1) of [emptyList]` causes an error because there is no position 1. Students practice checking "is the list empty?" BEFORE accessing items using the pattern: `if <(length of [list]) = (0)> then say "List is empty!" else say (item (1) of [list])`. They trace through programs with different starting conditions (empty list, 1-item list, multi-item list) to understand when guards are necessary. This defensive programming pattern prevents crashes and teaches edge-case thinking early.
Dependencies:
* T10.G3.12: Check if a list is empty before accessing
* T10.G3.16: Predict and trace list changes step by step

ID: T10.G3.14
Topic: T10 – Lists & Tables
Skill: Increment or decrement a list item's value
Description: Students use the `change item (position) of [list] by (amount)` block to modify numeric values in a list arithmetically (e.g., increase a player's score by 10, decrease health by 5). This block changes the value in place without needing to manually get-calculate-replace, making score updates and counters much simpler. For young learners who don't know negative numbers, the `reduce item (position) of [list] by (amount)` block provides a simpler way to decrease values. Students verify the change by reading the item before and after modification.
Dependencies:
* T10.G3.04: Read items from a list by position (index starts at 1)
* T09.G3.01: Increment and decrement a variable

ID: T10.G3.15
Topic: T10 – Lists & Tables
Skill: Display a list monitor on the stage
Description: Students enable the list monitor by checking the checkbox next to the list name in the Variables palette. The monitor displays all items with their positions (1, 2, 3...) and updates in real-time as items are added, removed, or changed. Students use visual feedback to verify list state and debug their programs by watching the monitor while running code.
Dependencies:
* T10.G3.02: Add an item to the end of a list

ID: T10.G3.16
Topic: T10 – Lists & Tables
Skill: Predict and trace list changes step by step
Description: Students trace through a short sequence of list operations (3-5 blocks) and predict the final state of the list. Given blocks like: create list → add "apple" → add "banana" → delete item 1 → add "cherry", students write down what the list contains after each step and predict the final result ["banana", "cherry"]. This builds mental models of how lists work and prepares students for debugging. Students verify predictions by running the code and comparing actual vs expected results.
Dependencies:
* T10.G3.02: Add an item to the end of a list
* T10.G3.06: Delete an item at a specific position
* T10.G3.15: Display a list monitor on the stage

ID: T10.G3.17
Topic: T10 – Lists & Tables
Skill: Debug a list program by identifying wrong positions
Description: Students identify and fix bugs in list programs where items are accessed, inserted, or deleted at wrong positions. Given a buggy program that should add items to a shopping cart but produces incorrect results, students use step-by-step execution and list monitors to find where positions are off-by-one or incorrect. They practice common debugging patterns: verifying list contents after each operation, checking that indices are within bounds (1 to length), and understanding how deletions shift subsequent items.
Dependencies:
* T10.G3.16: Predict and trace list changes step by step
* T10.G3.04: Read items from a list by position (index starts at 1)

ID: T10.G3.18
Topic: T10 – Lists & Tables
Skill: Use a list to store user inputs
Description: Students create interactive programs that collect multiple inputs from users and store them in a list. They use the `ask and wait` block inside a loop to gather several responses (e.g., "Enter 3 favorite foods"), adding each answer to a list. After collection, they display or process the collected data, such as saying all items back to the user. This introduces the practical pattern of building lists dynamically from user interaction rather than hardcoding values. Real-world applications: build a birthday wish list, collect friend names for party invitations, store high scores from different players, gather survey responses from classmates.
Dependencies:
* T10.G3.02: Add an item to the end of a list
* T07.G3.01: Use a counted repeat loop

ID: T10.G3.19
Topic: T10 – Lists & Tables
Skill: Validate user input before adding to list
Description: Students learn to check user inputs before adding them to a list, preventing invalid or unwanted data from being stored. They use simple conditionals to validate inputs: check if answer is not empty, check if answer is a number (when expecting numbers), or check if answer matches expected values (e.g., "yes" or "no"). For example, when collecting ages, students verify the input is greater than 0 and less than 150 before adding to the ages list. If validation fails, they ask the user to try again or skip that entry. This introduces data quality concepts early and prevents "garbage in, garbage out" problems. Students verify their validation works by intentionally entering invalid data and confirming it's rejected.
Dependencies:
* T10.G3.18: Use a list to store user inputs
* T08.G3.04: Use a simple if in a script

ID: T10.G3.20
Topic: T10 – Lists & Tables
Skill: Explain to a partner why a list is useful for a problem
Description: Students explain their choice to use a list rather than separate variables. Given a scenario (e.g., "store 5 quiz scores"), they articulate to a partner or record: "I used a list because I have MANY similar items, and with a list I can add more items easily, loop through all items, and keep them organized together. If I used 5 separate variables, I couldn't easily add a 6th score or loop through them." Students practice explaining trade-offs: lists are better for collections of similar items, but single variables are fine for one or two distinct values. This communication skill is essential for collaborative programming and code reviews.
Dependencies:
* T10.G3.02: Add an item to the end of a list
* T10.G3.09: Loop through each item in a list

ID: T10.G3.21
Topic: T10 – Lists & Tables
Skill: Choose list or variables for a simple data storage problem
Description: Students analyze a data storage scenario and decide whether to use a list or separate variables. Scenarios include: (A) "Store a player's name, score, and level" → 3 separate variables (different types of data), (B) "Store the names of 10 students" → list (many similar items), (C) "Store whether sound is on or off" → single variable (just one value). Students justify their choice and recognize patterns: lists are for "many of the same kind," variables are for "few different things." This decision-making skill prepares students for designing more complex data solutions.
Dependencies:
* T10.G3.01: Create a new list variable
* T09.G3.01: Create a new variable

ID: T10.G3.22
Topic: T10 – Lists & Tables
Skill: Compare list efficiency vs separate variables for 5+ similar items
Description: Students compare managing 5+ similar items using a list versus using separate variables, noticing practical advantages. Given a scenario like "track scores for 10 players," they first attempt to write code using 10 separate variables (score1, score2, ... score10) to find the highest score. Then they write the same logic using a list with a loop. Students observe: (1) the list version has fewer lines of code, (2) changing from 10 to 20 players is easy with a list but requires rewriting with variables, (3) finding the highest score with a loop works for ANY number of items. Students articulate: "A list is better when I have many similar items because I can use loops instead of writing the same code over and over." This practical comparison reinforces when to choose lists.
Dependencies:
* T10.G3.21: Choose list or variables for a simple data storage problem
* T10.G3.09: Loop through each item in a list
* T10.G3.11: Count items in a list that match a condition

ID: T10.G3.23
Topic: T10 – Lists & Tables
Skill: Debug list programs using console logging
Description: Students use CreatiCode's console panel to debug list programs by adding `log [message]` blocks that print the current state of list operations. When a program isn't working correctly (e.g., items aren't being added as expected, or counts are wrong), students add log statements showing: (1) list contents at key points, (2) index values during loops, (3) values being compared or added. For example, inside a loop they add `log (join "Checking item at position: " (position))` and `log (join "Item value is: " (item (position) of [myList]))`. Students compare the logged output to their expected values to find where the program diverges from expectations. This systematic debugging skill is essential for fixing more complex programs. Students practice with a buggy "count items > 10" program and use logs to find why the count is wrong.
Dependencies:
* T10.G3.17: Debug a list program by identifying wrong positions
* T10.G3.09: Loop through each item in a list

ID: T10.G3.24
Topic: T10 – Lists & Tables
Skill: Check if all list items are in expected range (min/max validation)
Description: Students learn to validate entire collections by checking if all values fall within expected bounds. After building a list from user input (like collecting ages or scores), they loop through and verify each value is within range (e.g., ages between 5-18, scores between 0-100). If any value is out of range, they report which position has the problem. Example: collecting test scores → loop through list → for each score, check if it's ≥ 0 AND ≤ 100 → if not, say "Score at position X is invalid!" This teaches defensive programming with collections: "Before using the data, make sure it makes sense." Real-world applications: checking all prices are positive before calculating total, verifying all ages are reasonable before computing average age.
Dependencies:
* T10.G3.19: Validate user input before adding to list
* T10.G3.09: Loop through each item in a list
* T10.G3.11: Count items in a list that match a condition

ID: T10.G3.25
Topic: T10 – Lists & Tables
Skill: Create a simple bar chart from list data
Description: Students use CreatiCode's chart blocks to visualize list data as a simple bar chart. Given a list of numbers (e.g., scores: [85, 72, 90, 68, 95] for 5 students), students use chart blocks to display a vertical bar chart where each bar represents one list item. They learn to: (1) prepare list data for visualization, (2) use the chart block to create a display, (3) interpret the visual output to verify it matches the data. Students practice with a class poll (votes for favorite colors) by first collecting votes into a list, then creating a bar chart to see which color won. This bridges the gap between reading charts (G2) and the full chart creation with tables (G7), giving students their first hands-on chart creation experience. Real-world connection: "This is how apps show your step counts each day or your game scores over time."
Dependencies:
* T10.G3.05: Get the length of a list
* T10.G3.09: Loop through each item in a list
* T10.G2.13: Read and answer questions from a bar chart or picture graph

ID: T10.G3.26
Topic: T10 – Lists & Tables
Skill: Find an item's position using built-in block
Description: Students use the `item # of [value] in [list]` block to find the position of a value in a list. They understand this returns the index of the first occurrence (or 0 if not found) and practice searching for items in different lists.
Dependencies:
* T10.G3.04: Read items from a list by position (index starts at 1)

ID: T10.G3.27
Topic: T10 – Lists & Tables
Skill: Insert an item at a specific position in a list
Description: Students use the `insert [item] at (position) of [list]` block to add items at the beginning, middle, or end of a list. They observe how existing items shift to higher indices to make room and verify the new item appears at the correct position. Students practice inserting at position 1 (prepend), at length+1 (append), and at middle positions.
Dependencies:
* T10.G3.04: Read items from a list by position (index starts at 1)
* T10.G3.05: Get the length of a list

ID: T10.G3.28
Topic: T10 – Lists & Tables
Skill: Replace an item in a list
Description: Students use the `replace item (position) of [list] with [value]` block to update an existing item without changing the list length. They practice replacing items based on position and recognize the difference between replacing (overwrites in place, same length) and inserting (shifts existing items, length increases).
Dependencies:
* T10.G3.04: Read items from a list by position (index starts at 1)

ID: T10.G3.29
Topic: T10 – Lists & Tables
Skill: Delete an item from a list by value
Description: Students use the `delete value [item] from [list]` block to remove the first occurrence of a specific value (e.g., delete "apple" from the fruits list). This finds and removes the item without needing to know its position, which differs from deleting by index. Students test with items that exist (removes first match) and items that don't exist (no change).
Dependencies:
* T10.G3.06: Delete an item at a specific position
* T10.G3.10: Check if a list contains a specific item

## GRADE 4 (38 skills)

ID: T10.G4.01
Topic: T10 – Lists & Tables
Skill: Trace the off-by-one error pattern
Description: Students learn to recognize and debug one of the most common list errors: off-by-one mistakes. They trace through code that has typical off-by-one errors, such as looping from 0 instead of 1 (causing an error since lists start at 1), looping to length+1 (trying to access a position that doesn't exist), or deleting from position 0 (invalid). Students identify the error symptoms (program crashes, wrong item accessed, unexpected behavior), locate the incorrect boundary in the code (start/end of loop or position access), and correct it. They practice with examples like `repeat (length of [list])` with counter starting at 0 vs. 1, and `item ((length of [list]) + (1)) of [list]` which accesses beyond the list. This debugging pattern skill builds awareness of list boundaries and index arithmetic.
Dependencies:
* T10.G3.04: Read items from a list by position (index starts at 1)
* T10.G3.05: Get the length of a list
* T10.G3.17: Debug a list program by identifying wrong positions

ID: T10.G4.02
Topic: T10 – Lists & Tables
Skill: Implement manual linear search with loop
Description: Students implement a simple linear search algorithm by looping through a list, comparing each item to a target value, and reporting the position when found (or "not found" if the loop completes). They use a counter variable for the position and a conditional to check each item. This foundational algorithm skill teaches sequential searching and how the built-in block works internally.
Dependencies:
* T10.G3.09: Loop through each item in a list
* T08.G3.04: Use a simple if in a script
* T09.G3.01: Increment and decrement a variable

ID: T10.G4.03
Topic: T10 – Lists & Tables
Skill: Store and retrieve parallel list data
Description: Students use two lists in parallel (e.g., "playerNames" and "playerScores") where items at the same index are related. They add items to both lists together and use the same index to retrieve matching data (e.g., "the player at index 2 in names has the score at index 2 in scores"). Students recognize that keeping parallel lists synchronized is critical—adding to one requires adding to the other at the same position.
Dependencies:
* T10.G3.02: Add an item to the end of a list
* T10.G3.04: Read items from a list by position (index starts at 1)

ID: T10.G4.04
Topic: T10 – Lists & Tables
Skill: Use built-in blocks to sort a list
Description: Students use CreatiCode's `sort list [list] from [large to small/small to large]` block to sort numeric or alphabetic lists. They observe how the order changes and note that sorting rearranges items by value. Students verify the sort by reading the first and last items to confirm the order direction.
Dependencies:
* T10.G3.02: Add an item to the end of a list

ID: T10.G4.05
Topic: T10 – Lists & Tables
Skill: Use built-in list statistics (Sum, Average, Min, Max)
Description: Students use built-in blocks `[sum/average/smallest/largest] of list [list]` to compute aggregate values. They understand when to use each statistic: Sum for totals, Average for typical value, Min/Max for extremes (best/worst scores). This skill replaces writing manual loops for common statistical operations.
Dependencies:
* T10.G3.05: Get the length of a list

ID: T10.G4.06
Topic: T10 – Lists & Tables
Skill: Find the maximum or minimum item in a list manually
Description: Students write a loop to find the largest or smallest item in a numeric list without using built-in blocks. They initialize a "best so far" variable with the first item, loop through remaining items comparing each to the current best, and update the best when a better value is found. Students trace through a 5-item list and track how the "best so far" variable changes. This manual algorithm builds algorithmic thinking for aggregation operations.
Dependencies:
* T10.G3.09: Loop through each item in a list
* T08.G3.04: Use a simple if in a script
* T09.G3.01: Increment and decrement a variable

ID: T10.G4.07
Topic: T10 – Lists & Tables
Skill: Filter items from a list based on a condition
Description: Students loop through a list and build a new filtered list containing only items that satisfy a condition (e.g., "keep only scores > 50"). They create an empty result list, use conditionals inside a loop to check each item, and add matching items to the result list. Students verify the filtered list contains exactly the items that match the condition.
Dependencies:
* T10.G3.09: Loop through each item in a list
* T08.G3.04: Use a simple if in a script
* T10.G3.02: Add an item to the end of a list

ID: T10.G4.08
Topic: T10 – Lists & Tables
Skill: Trace filter algorithm step by step before implementing
Description: Before writing filter code, students practice tracing through the filter algorithm with a paper-and-pencil exercise. Given a source list [5, 12, 8, 15, 3, 20] and a condition "keep only numbers > 10", they manually step through the process: start with empty result list, examine each item, ask "does it match the condition?", if yes add to result, if no skip it, continue to next item. Students track both the source list position and the growing result list at each step. This explicit tracing builds algorithmic thinking and reveals the pattern: initialize empty result → loop through source → conditional check → add to result if match. After tracing on paper, students implement the algorithm in code with confidence, understanding each block's purpose. This tracing-first approach reduces cognitive load and prevents common mistakes like filtering in-place or forgetting the conditional.
Dependencies:
* T10.G3.11: Count items in a list that match a condition
* T10.G3.16: Predict and trace list changes step by step

ID: T10.G4.09
Topic: T10 – Lists & Tables
Skill: Build a high score list with parallel lists
Description: Students create a leaderboard using two parallel lists (names and scores). When a new score is added, they find the correct position to insert it (to keep scores sorted in descending order) and insert both the name and score at matching positions. Students verify that the leaderboard remains sorted after each insertion.
Dependencies:
* T10.G4.02: Implement manual linear search with loop
* T10.G4.03: Store and retrieve parallel list data
* T10.G3.27: Insert an item at a specific position in a list
* T10.G4.04: Use built-in blocks to sort a list

ID: T10.G4.10
Topic: T10 – Lists & Tables
Skill: Swap two items in a list
Description: Students swap the positions of two items in a list using a temporary variable. They store one item in the temp variable, replace it with the other item, then put the temp value in the second position. Students trace through the three-step swap process and verify both items exchange positions correctly. This pattern is a building block for sorting algorithms.
Dependencies:
* T10.G3.28: Replace an item in a list
* T09.G3.01: Increment and decrement a variable

ID: T10.G4.11
Topic: T10 – Lists & Tables
Skill: Copy one list to another (replacing contents)
Description: Students use the `copy [list1] to [list2]` block to duplicate a list. This REPLACES all items in list2 with items from list1, so list2's original contents are lost. After copying, both lists have identical items but remain separate (changing one doesn't affect the other). Students verify independence by modifying one list and confirming the other remains unchanged.
Dependencies:
* T10.G3.02: Add an item to the end of a list
* T10.G3.09: Loop through each item in a list

ID: T10.G4.12
Topic: T10 – Lists & Tables
Skill: Append one list to another (adding to end)
Description: Students use the `append [list1] to [list2]` block to add all items from list1 to the END of list2. This PRESERVES list2's original items and adds list1's items below them. Students compare append vs. copy and identify when each is appropriate: copy for backup/duplication, append for combining datasets.
Dependencies:
* T10.G4.11: Copy one list to another (replacing contents)

ID: T10.G4.13
Topic: T10 – Lists & Tables
Skill: Split a text string into a list
Description: Students use the `set [list] to split of [text] with splitter [delimiter]` block to convert text into a list of items (e.g., split "apple,banana,orange" by "," to get a list of three fruits). Students experiment with different delimiters (comma, space, newline) and verify the resulting list contains the expected items. This introduces text processing and list creation from external data.
Dependencies:
* T10.G3.02: Add an item to the end of a list
* T09.G4.01: Use addition (+) in variable expressions

ID: T10.G4.14
Topic: T10 – Lists & Tables
Skill: Join list items into a text string
Description: Students use the `join [list] into text with [delimiter]` block to combine list items into a single text string (e.g., join ["red", "green", "blue"] with ", " to get "red, green, blue"). This is the inverse of split and is useful for displaying list contents or saving list data as text.
Dependencies:
* T10.G4.13: Split a text string into a list
* T09.G4.01: Use addition (+) in variable expressions

ID: T10.G4.15
Topic: T10 – Lists & Tables
Skill: Reverse the order of items in a list
Description: Students use the `reverse [list]` block to flip item order (first becomes last, last becomes first). They observe the list monitor to see position changes. Reversing is useful for converting ascending to descending order, reversing time sequences, or inverting rankings.
Dependencies:
* T10.G3.02: Add an item to the end of a list
* T10.G3.04: Read items from a list by position (index starts at 1)

ID: T10.G4.16
Topic: T10 – Lists & Tables
Skill: Randomly shuffle items in a list
Description: Students use the `reshuffle [list] randomly` block to randomly rearrange all items. Each shuffle produces a different random order. Applications include shuffling cards, randomizing quiz questions, or creating random starting positions. Students note that reshuffling destroys the original order (make a copy first if needed).
Dependencies:
* T10.G3.02: Add an item to the end of a list

ID: T10.G4.17
Topic: T10 – Lists & Tables
Skill: Generate a list of random numbers with options
Description: Students use the `set [list] to (N) random whole numbers between (min) and (max) [no repetition/allow repetition]` block to populate a list with random values. They select whether to allow duplicate numbers and apply this for generating test data, simulating dice rolls, or creating random scores.
Dependencies:
* T10.G3.02: Add an item to the end of a list
* T10.G3.05: Get the length of a list

ID: T10.G4.18
Topic: T10 – Lists & Tables
Skill: Generate seeded random list
Description: Students use the seeded random block `set [list] to (N) random numbers with seed (SEED)` which generates the same sequence when using the same seed. This enables reproducible randomness for games (same level layout with same seed) and testing scenarios requiring consistent random data. Students verify that the same seed always produces the same list.
Dependencies:
* T10.G4.17: Generate a list of random numbers with options

ID: T10.G4.19
Topic: T10 – Lists & Tables
Skill: Loop through list indices
Description: Students use the `for each index [i] in [list]` block to iterate through list positions (1, 2, 3...) instead of values. This is necessary when they need to know both the position and the value, or when they need to modify items while looping. Students compare index-based iteration to value-based iteration and identify use cases for each.
Dependencies:
* T10.G3.04: Read items from a list by position (index starts at 1)
* T10.G3.09: Loop through each item in a list

ID: T10.G4.20
Topic: T10 – Lists & Tables
Skill: Find an item containing a substring
Description: Students use the `# of item containing [substring] in [list]` block to find the first list item that includes a partial match (e.g., find first name containing "son" in a names list). Students compare exact matching to partial matching and identify when each is appropriate.
Dependencies:
* T10.G3.26: Find an item's position using built-in block
* T09.G4.01: Use addition (+) in variable expressions

ID: T10.G4.21
Topic: T10 – Lists & Tables
Skill: Select multiple items from a list by criteria
Description: Students use the `insert (N) [largest/smallest/random] items from [list1] into [list2]` block to extract top/bottom/random items efficiently. Applications include leaderboards (top 10 scores), random sampling (pick 5 random quiz questions), or filtering extremes (3 coldest days). Students verify results by checking that list2 contains exactly N items matching the specified criteria.
Dependencies:
* T10.G4.04: Use built-in blocks to sort a list
* T10.G4.06: Find the maximum or minimum item in a list manually
* T10.G4.12: Append one list to another (adding to end)

ID: T10.G4.22
Topic: T10 – Lists & Tables
Skill: Extract a sublist from a range of positions
Description: Students create a new list containing items from a specific range within an existing list. Using a loop from start position to end position, they read each item from the source list and add it to a new result list. For example, to extract items 3-5 from a 10-item list, they loop from 3 to 5, reading and adding each item. This pattern is useful for pagination (show items 11-20), processing chunks of data, or splitting a list into smaller pieces.
Dependencies:
* T10.G3.04: Read items from a list by position (index starts at 1)
* T10.G3.02: Add an item to the end of a list
* T07.G3.01: Use a counted repeat loop

ID: T10.G4.23
Topic: T10 – Lists & Tables
Skill: Transform each item in a list using a loop
Description: Students iterate through a list and apply a transformation to each item (e.g., double all numbers, convert all text to uppercase, add a prefix to each name). They use a loop with index access to read each item, transform it, and replace it in the same position. This pattern introduces the "map" concept where every element is processed uniformly. Students trace through a 4-item list showing the before and after state.
Dependencies:
* T10.G4.19: Loop through list indices
* T10.G3.28: Replace an item in a list

ID: T10.G4.24
Topic: T10 – Lists & Tables
Skill: Accumulate a single value from a list
Description: Students implement the accumulator pattern to reduce a list to a single result: start with an initial value (0 for sum, 1 for product, empty string for concatenation), loop through all items, and combine each item with the accumulator. Beyond sum (already covered), students apply this pattern to compute products of all numbers, concatenate all strings, or find the longest string. This introduces the "reduce" concept foundational to functional programming.
Dependencies:
* T10.G3.09: Loop through each item in a list
* T10.G4.05: Use built-in list statistics (Sum, Average, Min, Max)

ID: T10.G4.25
Topic: T10 – Lists & Tables
Skill: Predict list state after a sequence of operations
Description: Students read a sequence of 5-7 list operations (add, delete, insert, replace) and predict the final list contents without running the code. They trace through each operation step by step, writing the list state after each step, then verify their prediction by running the code. This skill emphasizes understanding how each operation modifies the list and develops mental execution abilities critical for debugging and algorithm design.
Dependencies:
* T10.G3.16: Predict and trace list changes step by step
* T10.G3.27: Insert an item at a specific position in a list
* T10.G3.28: Replace an item in a list

ID: T10.G4.26
Topic: T10 – Lists & Tables
Skill: Predict parallel list synchronization issues
Description: Students learn to identify and prevent synchronization errors in parallel lists through prediction and tracing exercises. Given two parallel lists (e.g., names and scores), they examine code that adds to one list but not the other, or deletes from one list but not the other, and predict what problems will occur: mismatched data (wrong score paired with wrong name), mismatched lengths (lists become different sizes), or index errors (trying to access position that exists in one list but not the other). Students trace through problematic code step-by-step, tracking the length and contents of both lists to see when they fall out of sync. They then fix the code by ensuring all operations (add, delete, replace) happen to both lists at the same position. This critical skill prevents data corruption in parallel list patterns.
Dependencies:
* T10.G4.03: Store and retrieve parallel list data
* T10.G3.16: Predict and trace list changes step by step
* T10.G3.17: Debug a list program by identifying wrong positions

ID: T10.G4.27
Topic: T10 – Lists & Tables
Skill: Debug parallel list synchronization errors
Description: Students identify and fix bugs where parallel lists become out of sync—a common error when working with related data in separate lists. Given buggy code where names and scores lists don't match up correctly (e.g., inserting into one list but not the other, or deleting at different positions), students trace through to find where synchronization breaks and fix the code. They develop the rule: "When modifying parallel lists, ALWAYS modify both at the same position." Students practice debugging scenarios: (1) adding to only one list, (2) deleting from wrong positions, (3) inserting at mismatched indices.
Dependencies:
* T10.G4.03: Store and retrieve parallel list data
* T10.G3.27: Insert an item at a specific position in a list
* T10.G3.17: Debug a list program by identifying wrong positions

ID: T10.G4.28
Topic: T10 – Lists & Tables
Skill: Design a list structure for a game inventory system
Description: Students design and implement a simple inventory system using lists. They identify what data needs to be stored (item names, quantities, maybe categories), decide between one list vs. parallel lists vs. list of formatted strings, and implement add/remove/display operations. Example: A simple game where the player collects items. Students design: items list ["sword", "shield", "potion"], quantities list [1, 1, 3]. They implement: add item (check if exists, increment or add new), remove item (decrement or remove if zero), display inventory (loop through and show). This project-based skill applies list concepts to a real game scenario.
Dependencies:
* T10.G4.03: Store and retrieve parallel list data
* T10.G3.26: Find an item's position using built-in block
* T10.G3.14: Increment or decrement a list item's value

ID: T10.G4.29
Topic: T10 – Lists & Tables
Skill: Compare two lists for equality
Description: Students write code to check if two lists contain the same items in the same order. They first check if lengths match, then loop through comparing each position. If any position differs, the lists are not equal. Students trace through comparisons and understand this is different from checking if lists have the same items in ANY order (which would require sorting or more complex checking). Applications include: verifying a copy was made correctly, checking if a shuffle changed anything, or validating user input matches expected sequence.
Dependencies:
* T10.G4.19: Loop through list indices
* T10.G3.05: Get the length of a list
* T08.G3.04: Use a simple if in a script

ID: T10.G4.30
Topic: T10 – Lists & Tables
Skill: Design data structure for a simple scenario (list vs multiple variables)
Description: Students analyze a given scenario and make a justified decision about data structure choice: should they use a list, multiple separate variables, or parallel lists? For example, storing 3 high scores could be done with variables (score1, score2, score3) or a list [scores]; tracking player name, level, and lives could use 3 separate variables or parallel lists if there are multiple players. Students consider factors: How many items? Will the number change? Do items need to be processed together (loop)? Are items all the same type? They sketch their design choice, explain the tradeoffs (variables are simpler for fixed small amounts; lists are flexible for variable amounts), and implement their design. This design thinking skill bridges concrete list operations to abstract data structure decision-making.
Dependencies:
* T10.G3.21: Choose list or variables for a simple data storage problem
* T10.G4.03: Store and retrieve parallel list data
* T10.G4.02: Implement manual linear search with loop

ID: T10.G4.31
Topic: T10 – Lists & Tables
Skill: Trace bubble sort algorithm on paper before implementing
Description: Students trace through the bubble sort algorithm on paper with a small list (5-6 items) before writing code. Given an unsorted list like [5, 2, 8, 1, 9], they manually perform each pass: compare adjacent pairs, swap if out of order, track how many swaps occurred per pass, and continue until no swaps are needed. Students create a trace table showing the list state after each pass and count total comparisons and swaps. Key observations: (1) largest items "bubble up" to the end first, (2) each pass places at least one more item in its final position, (3) worst case requires many passes for nearly-reversed lists. This tracing-first approach builds understanding of the algorithm's behavior before managing the complexity of nested loops in code, directly preparing for T10.G8.02.
Dependencies:
* T10.G4.10: Swap two items in a list
* T10.G4.04: Use built-in blocks to sort a list
* T10.G3.16: Predict and trace list changes step by step

ID: T10.G4.32
Topic: T10 – Lists & Tables
Skill: Recognize when sorting helps vs when it's unnecessary
Description: Students analyze scenarios to decide whether sorting a list is helpful, unnecessary, or potentially wasteful. Scenarios: (1) "Find if 'apple' is in the grocery list" → sorting first doesn't help for a small list; just search directly. (2) "Display students in alphabetical order" → sorting is exactly what's needed. (3) "Find the maximum value" → sorting works but is overkill; use the max block or a single loop instead. (4) "Find items over $10 from a shopping list" → sorting by price could help, OR just filter directly. Students learn that sorting takes time and isn't always the right tool. They articulate: "I would sort first because..." or "I wouldn't sort because..." AI-era insight: When sending data to AI for analysis or classification, the AI doesn't care about order—sorting wastes time. But when displaying results to users, sorting by relevance or date helps them find what they need. This early algorithmic reasoning prepares students for efficiency thinking in later grades.
Dependencies:
* T10.G4.04: Use built-in blocks to sort a list
* T10.G4.06: Find the maximum or minimum item in a list manually
* T10.G4.07: Filter items from a list based on a condition

ID: T10.G4.33
Topic: T10 – Lists & Tables
Skill: Use step-by-step execution to trace list algorithms
Description: Students use CreatiCode's step-by-step execution feature (debugger) to trace through list algorithms one block at a time, observing how list contents change with each operation. They set breakpoints before critical operations, step through the code, and watch the list monitor update in real-time. This helps understand exactly when items are added, deleted, or modified. Students practice with algorithms like: filtering (watch which items get added to result), finding maximum (watch tracker variable update), and reversing (watch items swap positions). For each algorithm, they predict what will happen on the next step, execute it, and compare their prediction to the actual result. This active tracing builds deep understanding of list manipulation patterns and is essential for debugging complex code. Students complete a guided worksheet tracking list state through a 10-step algorithm.
Dependencies:
* T10.G3.23: Debug list programs using console logging
* T10.G4.06: Find the maximum or minimum item in a list manually
* T10.G4.07: Filter items from a list based on a condition

ID: T10.G4.34
Topic: T10 – Lists & Tables
Skill: Analyze when to use built-in blocks vs manual algorithms
Description: Students compare using CreatiCode's built-in list blocks (like `sort list`, `[sum] of list`, `[largest] of list`) versus implementing the same operation manually with loops. They analyze trade-offs: Built-in blocks are (1) faster to write, (2) less error-prone, (3) often more efficient; Manual algorithms are better when (1) you need custom behavior (sort by second character), (2) you need to track additional information (which position had the max), (3) you're learning how the algorithm works. Students practice making justified decisions: given "find the 3 largest items," they might use built-in sort then take first 3 items, OR implement a manual algorithm that's more efficient. They articulate their choice and reasoning. This meta-cognitive skill—choosing the right tool for the job—is essential for efficient programming.
Dependencies:
* T10.G4.04: Use built-in blocks to sort a list
* T10.G4.05: Use built-in list statistics (Sum, Average, Min, Max)
* T10.G4.06: Find the maximum or minimum item in a list manually

ID: T10.G4.35
Topic: T10 – Lists & Tables
Skill: Check for duplicate entries before adding to list
Description: Students implement a common data quality pattern: before adding a new item to a list, check if it already exists using `[list] contains [item]?`. If the item is already in the list, skip adding it (or show a message); if not, add it. Applications: prevent duplicate usernames in a registration list, avoid re-adding the same item to a shopping cart, ensure unique vote entries in a poll. Implementation pattern: `if <not <[myList] contains (newItem)?>> then add [newItem] to [myList] else say "Already in list!"`. Students test their validation by trying to add duplicates and verifying they're rejected. This practical pattern prepares students for database concepts where unique constraints prevent duplicate records.
Dependencies:
* T10.G3.10: Check if a list contains a specific item
* T10.G3.19: Validate user input before adding to list
* T08.G3.04: Use a simple if in a script

ID: T10.G4.36
Topic: T10 – Lists & Tables
Skill: Store and access items in a list of lists (basic 2D introduction)
Description: Students create a simple nested list structure (2-3 rows, 2-3 items each) to represent basic grid data like a mini tic-tac-toe board or a small seating chart. They learn the two-step access pattern: first get the row using `item (row) of [grid]`, then get the cell using `item (column) of (the row)`. Full syntax: `item (column) of (item (row) of [grid])`. Example: A 3x3 grid stored as [[X, O, X], [O, X, O], [X, X, O]]; to read position (2,3), use `item (3) of (item (2) of [grid])` which returns O. Students practice: (1) creating a nested list structure manually by adding lists to a list, (2) reading values at specific row/column positions, (3) understanding why row comes before column in the access pattern. This foundational skill prepares for full 2D array work in G6.
Dependencies:
* T10.G4.03: Store and retrieve parallel list data
* T10.G3.28: Replace an item in a list

ID: T10.G4.37
Topic: T10 – Lists & Tables
Skill: Create a grouped bar chart comparing two data sets
Description: Students extend their chart skills to compare two related lists using grouped or stacked bar charts. Given two parallel lists (e.g., monthlyScoresTeamA: [85, 78, 92] and monthlyScoresTeamB: [80, 88, 85] for Jan/Feb/Mar), students create a chart showing both data sets side by side. They learn to: (1) ensure both lists have the same length, (2) use chart blocks with multiple data sources, (3) interpret the comparison (which team did better each month?). Real-world connections: comparing sales between two stores, tracking two players' scores over a season, or showing test scores before vs. after studying. This skill bridges single-list charts (G3.25) to full table-based charts (G7.05).
Dependencies:
* T10.G3.25: Create a simple bar chart from list data
* T10.G4.03: Store and retrieve parallel list data

ID: T10.G4.38
Topic: T10 – Lists & Tables
Skill: Identify sensitive data that should not be shared
Description: Students learn to recognize personally identifiable information (PII) and sensitive data that requires careful handling. Given a sample table with various columns (Name, Age, Favorite Color, Home Address, Phone Number, Birthday, High Score), students identify which columns contain sensitive data that shouldn't be shared publicly. Categories of sensitive data: (1) Contact info (address, phone, email), (2) Personal identifiers (full name + birthday combination, student ID), (3) Private information (health data, passwords). Students classify each column as "OK to share," "Ask permission first," or "Never share publicly." They discuss why: address could help someone find you; birthday + name together could enable identity theft; high scores are generally safe to share. This data ethics foundation skill prepares students for responsible data handling in the AI era where data is constantly collected and shared.
Dependencies:
* T10.G4.03: Store and retrieve parallel list data
* T10.G3.21: Choose list or variables for a simple data storage problem

