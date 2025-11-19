# T09 – Variables & Expressions: K–8 Skill List (Draft v1)

Topic reference: `T09 Variables & Expressions` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, Data and Analysis (DAA‑DF)

Each skill below has:

- a stable **ID** (`T09.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Variables are treated as intuitive objects or containers whose values change over time. Students recognize changing attributes (position, score, count) without naming them formally as variables.

### T09.GK.01 – Notice a value that keeps changing

- **Short name:** Spot changing values in pictures
- **Description:** Students recognize that certain aspects of a scene or animation change (e.g., a number growing, a sprite moving, a color changing) and can point out what is changing and roughly what direction it changes (more/less, higher/lower). This builds the intuitive notion that things in programs can have values that are not fixed.
- **Challenge format:** Concept, interactive animation. A short animation or sequence of pictures shows an attribute changing (e.g., a score counter incrementing, a sprite getting taller, a timer counting down). Students are asked "What is changing?" and choose from picture/word options. Auto‑grading checks the selected answer.
- **CSTA:** EK‑PRO‑DH‑03 (identify symbols and data in daily life).

### T09.GK.02 – Count repeated actions to track a total

- **Short name:** Count things that happen
- **Description:** Students manually track or count repeated events (e.g., how many times the sprite bounced, how many turns in a game) by observing an animation or story. This connects the informal idea of "counting up" to the notion of accumulating a total over time.
- **Challenge format:** Concept, guided observation. An animation plays and shows a sprite performing an action multiple times. Students count and report the final total with picture‑based or number answers. Auto‑grading checks the numeric answer against the animation.
- **CSTA:** EK‑PRO‑DH‑03.

### T09.GK.03 – Use "more," "less," or "same" to compare values

- **Short name:** Compare bigger and smaller numbers
- **Description:** Students compare two quantities or displayed numbers using everyday language ("more," "less," "same") to recognize that expressions can result in different values and that comparing values is meaningful.
- **Challenge format:** Concept, multiple choice. Show two sets of items or two numbers on screen; ask "Which has more?" or "Are they the same?" Students select the correct comparison. Auto‑grading matches the selection.
- **CSTA:** EK‑PRO‑DH‑03.

---

## Grade 1

Variables are recognized as named containers with values; students see values change and can label them informally. Simple expressions involving counting and addition appear.

### T09.G1.01 – Identify values that change in a program

- **Short name:** Find things that change in code
- **Description:** Students observe a short running program and identify which on‑screen values or attributes change when the green flag is clicked or after an event (e.g., position, color, displayed number), distinguishing them from fixed values. This builds awareness that variables hold mutable data.
- **Challenge format:** Concept, multiple choice. Show a small script with a sprite and ask "What changes when the green flag is clicked?" with options like "position," "color," "costume," or "none." Students select the correct changing element. Auto‑grading checks the answer.
- **CSTA:** E1‑PRO‑DH‑02 (identify terms for values that change over time).

### T09.G1.02 – Use a simple counter that increments

- **Short name:** Add to a counter
- **Description:** Students create or modify a simple program where a variable (often labeled "score" or "count") starts at 0 and increases by 1 each time an event occurs (e.g., each click, each time a sprite touches something). This is their first explicit use of a variable to track a running total.
- **Challenge format:** Coding, starter project. Provided: a sprite, a displayed variable, and partial script with an event block. Students add or complete blocks that "change [variable] by 1" when triggered. Auto‑grading checks that the variable initializes correctly and increments on each trigger.
- **CSTA:** E1‑PRO‑DH‑02.

### T09.G1.03 – Recognize a simple expression (add/subtract numbers)

- **Short name:** Understand simple math in code
- **Description:** Students read simple arithmetic expressions (e.g., 5 + 3, 10 − 2) embedded in code or as displayed values, and predict or report the result. This is the first exposure to expressions combining operators and numbers.
- **Challenge format:** Concept, code‑reading item. Show a short script that sets a variable to an expression like "set score to 3 + 7" or "change count by 2 − 1" and ask "What is the value?" with numeric choices. Auto‑grading compares to the correct result.
- **CSTA:** E1‑PRO‑DH‑02, E1‑PRO‑PF‑01.

### T09.G1.04 – Display a variable value on screen

- **Short name:** Show a variable in the program
- **Description:** Students use a "say" or "display" block to show the value of a variable on screen, connecting the abstract idea of a stored value to visible output.
- **Challenge format:** Coding, starter project. Provided: a sprite with a variable already created. Students add a "say [variable]" or display block to show its value. Auto‑grading checks that the correct variable is displayed and appears on screen when run.
- **CSTA:** E1‑PRO‑DH‑02.

---

## Grade 2

Students use variables to store and modify numeric values; simple arithmetic expressions are part of program logic. Timers and counters appear in realistic contexts (scoring, keeping time).

### T09.G2.01 – Initialize a variable and use it in code

- **Short name:** Set a variable to start a program
- **Description:** Students create a variable, initialize it with a starting value (e.g., "set score to 0"), and then use it in subsequent blocks to display it or modify it. This builds the formal pattern of declaring and initializing variables before use.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable called 'score'. Set it to 0 when the green flag is clicked. Make it show on the screen." Students build the script. Auto‑grading checks variable creation, initialization, and display blocks.
- **CSTA:** E2‑PRO‑DH‑02.

### T09.G2.02 – Use expressions with variables to set a value

- **Short name:** Set a variable using math
- **Description:** Students write code that sets a variable to the result of an expression combining two numbers or variables, such as "set total to 5 + 3" or "set result to [var1] + [var2]." This demonstrates that expressions can be stored in variables.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable called 'sum'. Set it to 7 + 8 when the green flag is clicked." Students build this. Auto‑grading checks that the variable is set to the correct result (15).
- **CSTA:** E2‑PRO‑DH‑02.

### T09.G2.03 – Change a variable by an amount (increment/decrement)

- **Short name:** Add or subtract from a variable
- **Description:** Students use "change [variable] by [number]" blocks to modify the value of a variable by a fixed or computed amount, supporting the idea that variables can be updated incrementally. Both positive (increment) and negative (decrement) changes are explored.
- **Challenge format:** Coding, starter project. A game scene shows a score starting at 100. Prompt: "Each time the sprite collects a coin, add 10 to the score. When it hits an enemy, subtract 5." Students implement these change blocks. Auto‑grading checks the score after a sequence of events.
- **CSTA:** E2‑PRO‑DH‑02.

### T09.G2.04 – Use a timer variable to track elapsed time

- **Short name:** Make a timer in code
- **Description:** Students create a variable (often named "timer" or "time") that increments by 1 in a loop or on each frame/tick, using it to measure how long the program has been running or to trigger time‑based events. This connects variables to temporal logic.
- **Challenge format:** Coding, starter project with a loop or repeated event. Provided: a variable and a loop that runs repeatedly. Students add "change timer by 1" inside the loop. Auto‑grading checks that the timer value increases correctly and can trigger a condition (e.g., stop at 30 seconds).
- **CSTA:** E2‑PRO‑DH‑02, E2‑PRO‑PF‑01.

### T09.G2.05 – Predict the result of an expression with variables

- **Short name:** Calculate expressions in code
- **Description:** Students read code with variable names and expressions (e.g., "change score by lives * 10") and predict the final value after execution given starting values. This strengthens mental models of how expressions work.
- **Challenge format:** Concept, code‑reading item. Show a script with variable initialization and expressions, then ask "What is the final value of [variable]?" with numeric options. Auto‑grading compares to the computed result.
- **CSTA:** E2‑PRO‑DH‑02.

---

## Grade 3

Variables hold different data types; expressions combine operators (+, −, *, /, mod) with variables and inputs. Students use variables in conditions and loops.

### T09.G3.01 – Use different variable types (number, text, boolean)

- **Short name:** Create different kinds of variables
- **Description:** Students create variables of different types—number, text, and boolean—and assign appropriate values to each. This introduces the concept of variable types and when each is appropriate.
- **Challenge format:** Coding, guided construction. Prompt: "Create a variable called 'name' for text, 'score' for a number, and 'is_ready' for true/false." Students create each variable type and optionally assign sample values. Auto‑grading checks that each variable has the correct type.
- **CSTA:** E3‑PRO‑DH‑02.

### T09.G3.02 – Use a variable in a conditional (if block)

- **Short name:** Check a variable in an if statement
- **Description:** Students write conditionals that read a variable's value and branch based on it, such as "if score > 10 then..." This connects variables to control flow and decision logic.
- **Challenge format:** Coding, starter project. A sprite or game mechanic is set up with a score variable. Prompt: "If the score is greater than 50, say 'You win!'" Students add an if block comparing the variable. Auto‑grading checks the condition and response.
- **CSTA:** E3‑PRO‑DH‑02, E3‑PRO‑PF‑01.

### T09.G3.03 – Use multiplication and division in expressions

- **Short name:** Multiply or divide in expressions
- **Description:** Students use * and / operators in expressions to set or change variables, such as "set total to lives * 100" or "set average to sum / count." This extends arithmetic to include multiplicative operations.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable 'total_points' equal to the number of coins collected multiplied by 5." Students set up the expression. Auto‑grading checks that multiplication is used and the final value is correct.
- **CSTA:** E3‑PRO‑DH‑02.

### T09.G3.04 – Combine operators and variables in complex expressions

- **Short name:** Build multi‑step expressions
- **Description:** Students write expressions that combine two or more operators and variables, such as "(a + b) * 2" or "x + y − z", with attention to operator precedence or explicit grouping.
- **Challenge format:** Coding, starter project. Given variables a, b, c with starting values, prompt: "Set result to (a + b) * c." Students build the expression. Auto‑grading checks the final value.
- **CSTA:** E3‑PRO‑DH‑02.

### T09.G3.05 – Trace code with variables to predict outcomes

- **Short name:** Follow variable changes through code
- **Description:** Students trace a short script step‑by‑step, recording the value of a variable at each stage, and predict the final result. This reinforces understanding of how variables are modified.
- **Challenge format:** Concept, code‑reading with step‑through or table. Show a script with a variable that changes several times; ask "What is the value of [variable] after line X?" or "In the end?" with options. Auto‑grading checks selected answers.
- **CSTA:** E3‑PRO‑DH‑02.

---

## Grade 4

Students use variables across events and loops; expressions incorporate user input and sensor data. Multiple variables are coordinated in more complex programs.

### T09.G4.01 – Store and use user input in a variable

- **Short name:** Save the player's answer
- **Description:** Students use an "ask and wait" or input block to capture user input (a number or text), store it in a variable, and then use that variable in later blocks or conditionals.
- **Challenge format:** Coding, starter project. Prompt: "Ask the player for their name and store it. Then say 'Hello [name]!'" Students implement input capture and variable storage. Auto‑grading checks that input is stored and used correctly.
- **CSTA:** E4‑PRO‑DH‑02.

### T09.G4.02 – Use variables in a loop counter pattern

- **Short name:** Use a variable inside a loop
- **Description:** Students combine a loop with a variable that increments or decrements each iteration, often displaying intermediate values. This is a for‑loop-like pattern using repeated assignment.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable 'step'. Use a repeat loop and inside it, change 'step' by 1. Say the step number each time (e.g., 1, 2, 3, 4, 5)." Students build this. Auto‑grading checks loop count and variable updates.
- **CSTA:** E4‑PRO‑DH‑02, E4‑PRO‑PF‑01.

### T09.G4.03 – Use comparison operators in expressions

- **Short name:** Compare values with ==, >, <
- **Description:** Students use comparison operators (equal, not equal, greater than, less than) in conditionals and understand that comparisons evaluate to true/false, enabling more nuanced program logic.
- **Challenge format:** Coding, concept and practice. Prompt: "Create an if statement: if score >= 100, say 'High score!'" Students use the comparison operator. Auto‑grading checks the condition logic.
- **CSTA:** E4‑PRO‑DH‑02.

### T09.G4.04 – Use boolean variables to track states

- **Short name:** Use true/false variables
- **Description:** Students create boolean variables (e.g., "is_jumping", "has_key") to track on/off or yes/no states in a program, and use them in conditionals to control behavior.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable 'has_key' set to false. When the sprite collects a key, change it to true. If 'has_key' is true, let the player open a door." Students build this. Auto‑grading checks state tracking and conditional logic.
- **CSTA:** E4‑PRO‑DH‑02.

### T09.G4.05 – Modify a variable based on sensor or random input

- **Short name:** Change variables with sensors or randomness
- **Description:** Students set or modify a variable based on the result of a "pick random" block, sensor reading (e.g., volume, tilt), or other external input. This shows that variable updates can depend on dynamic sources.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable 'health'. When a random number is rolled, if it's > 50, add 10 to health; else subtract 5." Students implement the logic. Auto‑grading checks variable updates.
- **CSTA:** E4‑PRO‑DH‑02.

### T09.G4.06 – Debug incorrect variable updates in code

- **Short name:** Fix variable bugs
- **Description:** Students examine a program where a variable is initialized, modified, or used incorrectly (e.g., not initialized, updated too many times, used in the wrong place) and fix it to achieve the intended behavior.
- **Challenge format:** Coding, debugging. A starter project shows a game where the score does not update correctly. Students adjust the variable blocks to fix it. Auto‑grading checks the final behavior.
- **CSTA:** E4‑PRO‑DH‑02, E4‑PRO‑TR‑03.

---

## Grade 5

Students use multiple coordinated variables in complex expressions; variables support data collection and analysis within programs. Expressions use function‑like blocks and string operations.

### T09.G5.01 – Use multiple variables together in expressions

- **Short name:** Combine many variables in math
- **Description:** Students write expressions that use three or more variables together, such as "total = width * height * depth" or updating one variable based on others, demonstrating coordination of multiple data values.
- **Challenge format:** Coding, starter project. Prompt: "Calculate the area of a rectangle using width and height variables. Store the result in 'area'." Students build and test. Auto‑grading checks the expression and final value.
- **CSTA:** E5‑PRO‑DH‑02.

### T09.G5.02 – Use string variables and concatenation

- **Short name:** Join text strings together
- **Description:** Students use variables holding text and combine them using concatenation (e.g., "say [first_name] [last_name]" or "set message to 'Hello ' + name") to build dynamic messages.
- **Challenge format:** Coding, starter project. Prompt: "Ask the player for their first and last name. Create a greeting: 'Welcome, [first] [last]!'" Students implement text variable assignment and concatenation. Auto‑grading checks the output string.
- **CSTA:** E5‑PRO‑DH‑02.

### T09.G5.03 – Use mod (remainder) operator in expressions

- **Short name:** Use the mod operator
- **Description:** Students use the modulo operator (remainder after division) in expressions, such as "if (score mod 10) == 0" to detect patterns or trigger events at regular intervals.
- **Challenge format:** Coding, starter project. Prompt: "Every time the score increases by 10 (i.e., score mod 10 == 0), play a sound." Students use the mod operator. Auto‑grading checks the condition logic and timing.
- **CSTA:** E5‑PRO‑DH‑02.

### T09.G5.04 – Use variables to accumulate data in a loop

- **Short name:** Collect data with loop variables
- **Description:** Students use variables (accumulators) inside loops to collect totals, counts, or sums. This bridges toward data collection and analysis, where program state reflects gathered information.
- **Challenge format:** Coding, starter project. Prompt: "Ask the player for 5 numbers. Use a loop and a variable to add them all together. Display the total." Students build the accumulator pattern. Auto‑grading checks the sum after loop execution.
- **CSTA:** E5‑PRO‑DH‑02, E5‑PRO‑PF‑01, DAA‑DF.

### T09.G5.05 – Create and use a list variable (basic)

- **Short name:** Store multiple values in a list
- **Description:** Students create a list (array) variable, add items to it, and access items by index, recognizing that a list is a special kind of variable holding multiple values.
- **Challenge format:** Coding, starter project. Prompt: "Create a list called 'colors'. Add 'red', 'blue', 'green' to it. Display the first color." Students create and manipulate the list. Auto‑grading checks list content and indexed access.
- **CSTA:** E5‑PRO‑DH‑02, DAA‑DF.

### T09.G5.06 – Trace complex variable assignments and expressions

- **Short name:** Trace multi‑step variable code
- **Description:** Students trace code with multiple variables and expressions, recording values at each step and predicting final outcomes. This reinforces mental models of variable scope and order of operations.
- **Challenge format:** Concept, code‑reading with trace table. Show a script with several variable assignments and expressions; provide a table to fill in values at each step, or ask for the final value. Auto‑grading checks completed table or final answer.
- **CSTA:** E5‑PRO‑DH‑02.

---

## Grade 6

In middle school, variables are used in structured algorithms and data processing. Students understand scope, use variables to represent real‑world quantities, and create expressions for more abstract problem‑solving.

### T09.G6.01 – Use variables to represent real‑world quantities

- **Short name:** Model real quantities with variables
- **Description:** Students create variables that represent tangible quantities in a simulation or modeling context (e.g., temperature, distance, population, budget) and update them according to rules or formulas to simulate processes.
- **Challenge format:** Coding, project or simulation. Prompt: "Model the population of a creature. Start with 10. Each cycle, multiply by 1.1 to show growth. Stop when it exceeds 100." Students create variables and update logic. Auto‑grading checks growth rates and stopping condition.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑PF‑02.

### T09.G6.02 – Use expressions with mixed operators and precedence

- **Short name:** Build expressions with multiple operators
- **Description:** Students write and evaluate expressions using a mix of arithmetic operators, understanding or using parentheses to control order of operations, such as "(a + b) * c" vs "a + b * c".
- **Challenge format:** Coding, concept and practice. Prompt: "Calculate the cost: base_price + (base_price * tax_rate)." or show expressions and ask to predict the value. Auto‑grading checks expression evaluation.
- **CSTA:** MS‑PRO‑DH‑05.

### T09.G6.03 – Use variables in algorithms that include selection and iteration

- **Short name:** Use variables in complex algorithms
- **Description:** Students write algorithms (loops and conditionals) that rely on variables being initialized, updated, and checked at each iteration, such as a search loop maintaining a found variable or a counter in a nested loop context.
- **Challenge format:** Coding, starter project. Prompt: "Write a loop that counts how many numbers from 1 to 50 are divisible by 3. Store the count in a variable." Students implement. Auto‑grading checks the final count.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑PF‑01.

### T09.G6.04 – Trace and debug variable-dependent logic

- **Short name:** Find bugs in variable code
- **Description:** Students analyze a script with variable assignments and expressions, identify where a variable has an incorrect value or is used wrong, and fix the issue to achieve intended behavior.
- **Challenge format:** Coding, debugging. A project has a variable that is not initialized, incremented wrong, or used in an incorrect expression. Students fix it. Auto‑grading checks that the program behaves correctly after the fix.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑TR‑11.

### T09.G6.05 – Use variables to store intermediate results

- **Short name:** Save calculated results
- **Description:** Students recognize when to create temporary variables to store intermediate results of calculations, improving code readability and reducing redundant computation.
- **Challenge format:** Coding, refactor challenge. Given code that computes a complex expression inline, students refactor it to use helper variables to break down the calculation. Auto‑grading checks that intermediate results are stored and used correctly.
- **CSTA:** MS‑PRO‑DH‑04.

---

## Grade 7

Students use variables in simulations and data‑driven programs. Expressions are used to compute statistics, model physics, and drive decision logic in game and simulation contexts.

### T09.G7.01 – Use variables to store and update state in simulations

- **Short name:** Variables in simulations
- **Description:** Students create simulations (e.g., population, weather, particle motion) where variables represent state (position, velocity, count) and expressions update them each time step, demonstrating how variables enable temporal processes.
- **Challenge format:** Coding, project. Prompt: "Simulate a ball falling. Create variables for position and velocity. Each frame, apply gravity: velocity += 9.8, position += velocity." Students implement. Auto‑grading checks realistic falling motion.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑PF‑01, DAA‑DP.

### T09.G7.02 – Use aggregate expressions (sum, average, min, max)

- **Short name:** Calculate aggregate statistics
- **Description:** Students write expressions or use blocks to compute aggregate statistics (sum, average, minimum, maximum) over variables or lists, connecting expressions to data analysis.
- **Challenge format:** Coding, project. Prompt: "Store test scores in a list. Calculate and display the average score." Students create the list and write the averaging expression. Auto‑grading checks the result.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑DH‑06, DAA‑DP.

### T09.G7.03 – Use variables in conditional logic with compound conditions

- **Short name:** Use AND/OR in complex conditions
- **Description:** Students create conditional expressions using logical operators (AND, OR, NOT) to combine multiple variable comparisons, enabling more nuanced decision logic.
- **Challenge format:** Coding, starter project. Prompt: "If the player's health is > 0 AND they have a key, let them proceed. If health <= 0 OR they have no key, block them." Students use AND/OR operators. Auto‑grading checks the logic.
- **CSTA:** MS‑PRO‑DH‑05, MS‑PRO‑PF‑01.

### T09.G7.04 – Analyze how variable updates affect program behavior

- **Short name:** Understand variable impact on behavior
- **Description:** Students reason about how changing variable initialization values, update rates, or expressions changes the program's output or behavior, supporting algorithmic analysis.
- **Challenge format:** Concept, analysis and explanation. Show code with a variable and ask "If we change this initialization from 0 to 100, what happens?" or "Why does this need to be multiplied by 2?" Students explain or predict. Auto‑grading checks explanation quality.
- **CSTA:** MS‑PRO‑DH‑04, MS‑ALG‑AF‑01.

---

## Grade 8

Students use variables and expressions in complex algorithms and data processing; they analyze how expressions and variable choices affect efficiency and correctness.

### T09.G8.01 – Use variables in iterative algorithms

- **Short name:** Variables in complex algorithms
- **Description:** Students implement algorithms (e.g., searching, sorting, iterative numerical methods) that rely on variables to track state across many iterations, such as a variable tracking the index in a search or the accumulator in a repeated approximation.
- **Challenge format:** Coding, algorithmic challenge. Prompt: "Implement a linear search: given a list and a target, use variables to track the index and found status. Return the index if found, else -1." Students implement. Auto‑grading checks correctness on test cases.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑PF‑02.

### T09.G8.02 – Analyze expressions for efficiency and correctness

- **Short name:** Evaluate expression design
- **Description:** Students compare different expressions or variable strategies that solve the same problem (e.g., computing a sum by repeated addition vs direct formula) and reason about correctness, readability, and efficiency.
- **Challenge format:** Concept, comparison and explanation. Show two versions of code computing the same result using different expressions; ask which is better and why. Auto‑grading scores explanation quality.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑DH‑05, MS‑ALG‑AF‑02.

### T09.G8.03 – Use variables in data collection and statistical analysis

- **Short name:** Variables for data-driven programs
- **Description:** Students use variables (or lists of variables) to collect data from user input or sensors, compute statistics on the data, and use those statistics in expressions to make decisions or report findings.
- **Challenge format:** Coding, project. Prompt: "Collect 10 temperature readings. Calculate the average, min, and max. If the average > 30, display 'Hot!'." Students implement data collection and analysis. Auto‑grading checks calculations.
- **CSTA:** MS‑PRO‑DH‑04, MS‑DAA‑DP‑05, MS‑DAA‑DP‑06.

### T09.G8.04 – Debug variable-related logical errors

- **Short name:** Fix complex variable bugs
- **Description:** Students identify and fix bugs related to variable scope, initialization order, incorrect update expressions, or misuse of variables in conditionals. Debugging is more sophisticated, involving tracing across multiple blocks or loops.
- **Challenge format:** Coding, debugging challenge. A project has a variable that is not initialized before use, or an expression that produces wrong results due to order of operations or scope issues. Students fix it. Auto‑grading checks correctness.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑TR‑11.

### T09.G8.05 – Use expressions to implement mathematical or logical rules

- **Short name:** Implement formulas in code
- **Description:** Students take mathematical formulas or logical rules (e.g., distance = speed × time, tax = price × rate, is_valid = age >= 18 AND has_id) and translate them into variable assignments and expressions in code.
- **Challenge format:** Coding, project. Prompt: "Implement the quadratic formula: x = (-b ± sqrt(b² - 4ac)) / 2a. Create variables for a, b, c and compute both roots." Students implement the expressions. Auto‑grading checks correct output for test cases.
- **CSTA:** MS‑PRO‑DH‑05, MS‑ALG‑AF‑02.

