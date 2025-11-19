# T09 – Variables & Expressions: K–8 Skill List (Draft v1)

Topic reference: `T09 Variables & Expressions` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, Data and Analysis (DAA‑DF)

Each skill below has:

- a stable **ID** (`T09.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

**Scope in v3:** Variables & expressions as coding constructs are the focus from **Grade 3–8** in this topic. K–2 numeric and “changing value” intuitions are primarily built in T01/T04 (repeats, counters) and T25 (data representation); T09 assumes those foundations and begins when students start block‑based coding.

---

## Grade 3

Variables represent changing quantities; expressions combine operators (+, −, *, /, mod) with variables and inputs. Students begin by using single numeric variables in simple programs, then connect them to conditions and loops.

### T09.G3.01 – Create and use a numeric variable for score or count

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T03.G2.01: Choose subtasks for a simple project idea


- **Short name:** Create a variable to track score
- **Description:** Students create their first numeric variable with a simple name (e.g., `score`), set it to 0 at the start, and update it by 1 when something obvious happens (like touching a star). This gateway skill introduces the fundamental concept that programs can remember and change numbers. Focus on the create-set-change pattern with very simple increments.
- **Challenge format:** Coding, highly scaffolded starter project with step-by-step guidance. Prompt: "Create a variable called 'score'. Set it to 0 when the green flag is clicked. When the sprite touches a star, change 'score' by 1." Students follow guided steps to create, initialize, and update the variable. Auto‑grading checks variable creation, initialization, and simple increment behavior.
- **CSTA:** E3‑PRO‑DH‑02. ⭐ Gateway

### T09.G3.02 – Use a variable in a conditional (if block)

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T03.G3.03: Create a 3‑panel storyboard for a project
  * T07.G3.02: Trace a script with a simple loop
  * T08.G3.02: Decide when a single if is enough


- **Short name:** Check a variable in an if statement
- **Description:** Students write their first conditional that reads a variable's value using very simple comparisons (e.g., "if score > 3 then say 'Great!'"). This connects the variable concept to conditional logic with small, easy-to-test numbers. Focus on understanding that variables can be checked in conditions.
- **Challenge format:** Coding, scaffolded starter project. A sprite and score variable are set up. Prompt: "If the score is greater than 3, say 'Good job!'" with guided condition building. Students add an if block comparing the variable to a small number. Auto‑grading checks the condition logic and response.
- **CSTA:** E3‑PRO‑DH‑02, E3‑PRO‑PF‑01.

### T09.G3.03 – Debug missing or wrong variable updates

_Dependency:_
  * T09.G3.02: Use a variable in a conditional (if block)
  * T07.G3.03: Build a forever loop for simple animation
  * T08.G3.03: Pick the right conditional block for a scenario


- **Short name:** Fix a variable that never changes
- **Description:** Students inspect a very simple script where a variable obviously doesn't work right (e.g., `score` stays at 0 even after touching stars). The missing piece should be clear (missing "set score to 0" or missing "change score by 1"). This contextualized debugging skill teaches debugging as a natural part of learning variables, with obvious problems and straightforward fixes.  
- **Challenge format:** Coding, scaffolded debugging. Starter project shows clear expected behavior vs. actual behavior; students identify what's missing and add the missing variable block with guided options. Auto‑grading checks that the variable is properly initialized and updated.  
- **CSTA:** E3‑PRO‑DH‑02, E3‑PRO‑TR‑01.

### T09.G3.04 – Trace code with variables to predict outcomes

_Dependency:_
  * T09.G3.03: Debug missing or wrong variable updates
  * T07.G3.04: Use repeat‑until to reach a simple goal
  * T08.G3.04: Trace code with a single if/else


- **Short name:** Follow variable changes through code
- **Description:** Students trace a very short script (3-4 steps) where a variable changes in simple ways (set to 0, change by 1, change by 1 again), and predict the final value. Use small numbers and obvious changes. Focus on the basic concept of following how variables change step by step.
- **Challenge format:** Concept, simple code‑reading with visual support. Show a script like "set score to 0, change score by 1, change score by 2" and ask "What is score at the end?" with multiple choice answers. Auto‑grading checks selected answers.
- **CSTA:** E3‑PRO‑DH‑02.

---

## Grade 4

Students use variables across events and loops; expressions incorporate user input and sensor data. Multiple variables are coordinated in more complex programs.

### T09.G4.01 – Use multiplication and division in expressions

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.03: Debug missing or wrong variable updates
  * T09.G3.04: Trace code with variables to predict outcomes


- **Short name:** Multiply or divide in expressions
- **Description:** Students use * and / operators in expressions to set or change variables, such as "set total to lives * 100" or "set average to sum / count." This extends arithmetic to include multiplicative operations.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable 'total_points' equal to the number of coins collected multiplied by 5." Students set up the expression. Auto‑grading checks that multiplication is used and the final value is correct.
- **CSTA:** E4‑PRO‑DH‑02.

### T09.G4.02 – Combine operators and variables in complex expressions

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.03: Debug missing or wrong variable updates
  * T09.G3.04: Trace code with variables to predict outcomes


- **Short name:** Build multi‑step expressions
- **Description:** Students write expressions that combine two or more operators and variables, such as "(a + b) * 2" or "x + y − z", with attention to operator precedence or explicit grouping.
- **Challenge format:** Coding, starter project. Given variables a, b, c with starting values, prompt: "Set result to (a + b) * c." Students build the expression. Auto‑grading checks the final value.
- **CSTA:** E4‑PRO‑DH‑02.

### T09.G4.03 – Store and use user input in a variable

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes


- **Short name:** Save the player's answer
- **Description:** Students use an "ask and wait" or input block to capture user input (a number or text), store it in a variable, and then use that variable in later blocks or conditionals.
- **Challenge format:** Coding, starter project. Prompt: "Ask the player for their name and store it. Then say 'Hello [name]!'". Students implement input capture and variable storage. Auto‑grading checks that input is stored and used correctly.
- **CSTA:** E4‑PRO‑DH‑02.

### T09.G4.04 – Use variables in a loop counter pattern

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes


- **Short name:** Use a variable inside a loop
- **Description:** Students combine a loop with a variable that increments or decrements each iteration, often displaying intermediate values. This is a for‑loop–like pattern using repeated assignment.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable 'step'. Use a repeat loop and inside it, change 'step' by 1. Say the step number each time (e.g., 1, 2, 3, 4, 5)." Students build this. Auto‑grading checks loop count and variable updates.
- **CSTA:** E4‑PRO‑DH‑02, E4‑PRO‑PF‑01.

### T09.G4.05 – Use comparison operators in expressions

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes


- **Short name:** Compare values with ==, >, <
- **Description:** Students use comparison operators (equal, not equal, greater than, less than) in conditionals and understand that comparisons evaluate to true/false, enabling more nuanced program logic.
- **Challenge format:** Coding, concept and practice. Prompt: "Create an if statement: if score >= 100, say 'High score!'." Students use the comparison operator. Auto‑grading checks the condition logic.
- **CSTA:** E4‑PRO‑DH‑02.

### T09.G4.06 – Use boolean variables to track states

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.03: Debug missing or wrong variable updates


- **Short name:** Use true/false variables
- **Description:** Students create boolean variables (e.g., "is_jumping", "has_key") to track on/off or yes/no states in a program, and use them in conditionals to control behavior.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable 'has_key' set to false. When the sprite collects a key, change it to true. If 'has_key' is true, let the player open a door." Students build this. Auto‑grading checks state tracking and conditional logic.
- **CSTA:** E4‑PRO‑DH‑02.

### T09.G4.07 – Modify a variable based on sensor or random input

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes


- **Short name:** Change variables with sensors or randomness
- **Description:** Students set or modify a variable based on the result of a "pick random" block, sensor reading (e.g., volume, tilt), or other external input. This shows that variable updates can depend on dynamic sources.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable 'health'. When a random number is rolled, if it's > 50, add 10 to health; else subtract 5." Students implement the logic. Auto‑grading checks variable updates.
- **CSTA:** E4‑PRO‑DH‑02.

### T09.G4.08 – Debug incorrect variable updates in code

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.03: Debug missing or wrong variable updates


- **Short name:** Fix variable bugs
- **Description:** Students examine a program where a variable is initialized, modified, or used incorrectly (e.g., not initialized, updated too many times, used in the wrong place) and fix it to achieve the intended behavior.
- **Challenge format:** Coding, debugging. A starter project shows a game where the score does not update correctly. Students adjust the variable blocks to fix it. Auto‑grading checks the final behavior.
- **CSTA:** E4‑PRO‑DH‑02, E4‑PRO‑TR‑03.

---

## Grade 5

Students use multiple coordinated variables in complex expressions; variables support data collection and analysis within programs. Expressions use function‑like blocks and string operations.

### T09.G5.01 – Use multiple variables together in expressions

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.02: Use a variable in a conditional (if block)
  * T09.G4.07: Modify a variable based on sensor or random input
  * T09.G4.08: Debug incorrect variable updates in code


- **Short name:** Combine many variables in math
- **Description:** Students write expressions that use three or more variables together, such as "total = width * height * depth" or updating one variable based on others, demonstrating coordination of multiple data values.
- **Challenge format:** Coding, starter project. Prompt: "Calculate the area of a rectangle using width and height variables. Store the result in 'area'." Students build and test. Auto‑grading checks the expression and final value.
- **CSTA:** E5‑PRO‑DH‑02.

### T09.G5.02 – Use string variables and concatenation

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.02: Use a variable in a conditional (if block)
  * T09.G4.07: Modify a variable based on sensor or random input
  * T09.G4.08: Debug incorrect variable updates in code


- **Short name:** Join text in variables
- **Description:** Students store text in variables and use concatenation (e.g., joining "Hello " + name) to build messages and labels.
- **Challenge format:** Coding, starter project. Prompt: "Ask for the player's name. Store it in a variable. Then say 'Welcome, [name]!'." Auto‑grading checks that text is stored and concatenated correctly.
- **CSTA:** E5‑PRO‑DH‑02.

### T09.G5.03 – Use variables to configure behavior (parameters without functions)

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G4.08: Debug incorrect variable updates in code


- **Short name:** Tune behavior with variables
- **Description:** Students create variables that configure behavior (e.g., speed, difficulty, number of lives) and use them in expressions to control program settings, introducing the idea of parameterization.
- **Challenge format:** Coding, starter project. Prompt: "Create a variable 'speed'. Use it to control how far the sprite moves on each key press." Auto‑grading checks that behavior changes when the variable's value changes.
- **CSTA:** E5‑PRO‑DH‑02.

### T09.G5.04 – Use expressions involving lists (length, indexing)

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.02: Use a variable in a conditional (if block)
  * T09.G4.07: Modify a variable based on sensor or random input
  * T09.G4.08: Debug incorrect variable updates in code


- **Short name:** Use list properties in expressions
- **Description:** Students use expressions like "length of [list]" or "item (index) of [list]" and combine them with numeric variables (e.g., index variables) to work with list data.
- **Challenge format:** Coding, starter project. Prompt: "Use a variable 'i' and a list of names. Say each name with its position (e.g., '1: Alice')." Auto‑grading checks that indexing is correct.
- **CSTA:** E5‑PRO‑DH‑02, DAA‑DF.

### T09.G5.05 – Use variables to track cumulative statistics

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G4.07: Modify a variable based on sensor or random input
  * T09.G4.08: Debug incorrect variable updates in code


- **Short name:** Track statistics with variables
- **Description:** Students maintain variables such as "total_score", "games_played", and "high_score" across multiple rounds or sessions, using expressions to update and compare these values.
- **Challenge format:** Coding, project. Prompt: "Track the total score over 5 rounds and display the average at the end." Auto‑grading checks that totals and averages are computed correctly.
- **CSTA:** E5‑PRO‑DH‑02, DAA‑DP.

### T09.G5.06 – Trace complex variable assignments and expressions

_Dependency:_
  * T01.G3.01: Complete a simple script with missing blocks
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G4.07: Modify a variable based on sensor or random input
  * T09.G4.08: Debug incorrect variable updates in code


- **Short name:** Trace multi‑step variable code
- **Description:** Students trace code with multiple variables and expressions, recording values at each step and predicting final outcomes. This reinforces mental models of variable scope and order of operations.
- **Challenge format:** Concept, code‑reading with trace table. Show a script with several variable assignments and expressions; provide a table to fill in values at each step, or ask for the final value. Auto‑grading checks completed table or final answer.
- **CSTA:** E5‑PRO‑DH‑02.

### T09.G5.07 – Trace a counter variable in a loop

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G4.08: Debug incorrect variable updates in code


- **Short name:** Trace loop counter  
- **Description:** Students trace a script where a variable starts at a value and changes inside a loop, predicting its final value.  
- **Challenge format:** Code‑reading with table or MCQ; checked by simulation.  
- **CSTA:** E5‑ALG‑AF‑01.

### T09.G5.08 – Trace an accumulator that sums values

_Dependency:_
  * T01.G3.01: Complete a simple script with missing blocks
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G4.07: Modify a variable based on sensor or random input
  * T09.G4.08: Debug incorrect variable updates in code


- **Short name:** Trace accumulator  
- **Description:** Students trace code that adds values to a running total and determine the final sum.  
- **Challenge format:** Code‑reading + numeric answer; auto‑graded.  
- **CSTA:** E5‑ALG‑AF‑01, E5‑ALG‑PS‑03.

---

## Grade 6

In middle school, variables are used in structured algorithms and data processing. Students understand scope, use variables to represent real‑world quantities, and create expressions for more abstract problem‑solving.

### T09.G6.01 – Use variables to represent real‑world quantities

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.02: Use a variable in a conditional (if block)
  * T09.G5.07: Trace a counter variable in a loop
  * T09.G5.08: Trace an accumulator that sums values


- **Short name:** Model real quantities with variables
- **Description:** Students create variables that represent tangible quantities in a simulation or modeling context (e.g., temperature, distance, population, budget) and update them according to rules or formulas to simulate processes.
- **Challenge format:** Coding, project or simulation. Prompt: "Model the population of a creature. Start with 10. Each cycle, multiply by 1.1 to show growth. Stop when it exceeds 100." Students create variables and update logic. Auto‑grading checks growth rates and stopping condition.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑PF‑02.

### T09.G6.02 – Use expressions with mixed operators and precedence

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G5.07: Trace a counter variable in a loop
  * T09.G5.08: Trace an accumulator that sums values


- **Short name:** Build expressions with multiple operators
- **Description:** Students write and evaluate expressions using a mix of arithmetic operators, understanding or using parentheses to control order of operations, such as "(a + b) * c" vs "a + b * c".
- **Challenge format:** Coding, concept and practice. Prompt: "Calculate the cost: base_price + (base_price * tax_rate)." or show expressions and ask to predict the value. Auto‑grading checks expression evaluation.
- **CSTA:** MS‑PRO‑DH‑05.

### T09.G6.03 – Use variables in algorithms that include selection and iteration

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G5.08: Trace an accumulator that sums values


- **Short name:** Use variables in complex algorithms
- **Description:** Students write algorithms (loops and conditionals) that rely on variables being initialized, updated, and checked at each iteration, such as a search loop maintaining a found variable or a counter in a nested loop context.
- **Challenge format:** Coding, starter project. Prompt: "Write a loop that counts how many numbers from 1 to 50 are divisible by 3. Store the count in a variable." Students implement. Auto‑grading checks the final count.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑PF‑01.

### T09.G6.04 – Trace and debug variable-dependent logic

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G5.08: Trace an accumulator that sums values


- **Short name:** Find bugs in variable code
- **Description:** Students analyze a script with variable assignments and expressions, identify where a variable has an incorrect value or is used wrong, and fix the issue to achieve intended behavior.
- **Challenge format:** Coding, debugging. A project has a variable that is not initialized, incremented wrong, or used in an incorrect expression. Students fix it. Auto‑grading checks that the program behaves correctly after the fix.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑TR‑11.

### T09.G6.05 – Use variables to store intermediate results

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G5.07: Trace a counter variable in a loop
  * T09.G5.08: Trace an accumulator that sums values


- **Short name:** Save calculated results
- **Description:** Students recognize when to create temporary variables to store intermediate results of calculations, improving code readability and reducing redundant computation.
- **Challenge format:** Coding, refactor challenge. Given code that computes a complex expression inline, students refactor it to use helper variables to break down the calculation. Auto‑grading checks that intermediate results are stored and used correctly.
- **CSTA:** MS‑PRO‑DH‑04.

---

## Grade 7

Students use variables in simulations and data‑driven programs. Expressions are used to compute statistics, model physics, and drive decision logic in game and simulation contexts.

### T09.G7.01 – Use variables to store and update state in simulations

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.02: Use a variable in a conditional (if block)
  * T09.G6.04: Trace and debug variable-dependent logic
  * T09.G6.05: Use variables to store intermediate results


- **Short name:** Variables in simulations
- **Description:** Students create simulations (e.g., population, weather, particle motion) where variables represent state (position, velocity, count) and expressions update them each time step, demonstrating how variables enable temporal processes.
- **Challenge format:** Coding, project. Prompt: "Simulate a ball falling. Create variables for position and velocity. Each frame, apply gravity: velocity += 9.8, position += velocity." Students implement. Auto‑grading checks realistic falling motion.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑PF‑01, DAA‑DP.

### T09.G7.02 – Use aggregate expressions (sum, average, min, max)

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.02: Use a variable in a conditional (if block)
  * T09.G6.04: Trace and debug variable-dependent logic
  * T09.G6.05: Use variables to store intermediate results


- **Short name:** Calculate aggregate statistics
- **Description:** Students write expressions or use blocks to compute aggregate statistics (sum, average, minimum, maximum) over variables or lists, connecting expressions to data analysis.
- **Challenge format:** Coding, project. Prompt: "Store test scores in a list. Calculate and display the average score." Students create the list and write the averaging expression. Auto‑grading checks the result.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑DH‑06, DAA‑DP.

### T09.G7.03 – Use variables in conditional logic with compound conditions

_Dependency:_
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G6.04: Trace and debug variable-dependent logic
  * T09.G6.05: Use variables to store intermediate results


- **Short name:** Use AND/OR in complex conditions
- **Description:** Students create conditional expressions using logical operators (AND, OR, NOT) to combine multiple variable comparisons, enabling more nuanced decision logic.
- **Challenge format:** Coding, starter project. Prompt: "If the player's health is > 0 AND they have a key, let them proceed. If health <= 0 OR they have no key, block them." Students use AND/OR operators. Auto‑grading checks the logic.
- **CSTA:** MS‑PRO‑DH‑05, MS‑PRO‑PF‑01.

### T09.G7.04 – Analyze how variable updates affect program behavior

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G6.04: Trace and debug variable-dependent logic
  * T09.G6.05: Use variables to store intermediate results


- **Short name:** Understand variable impact on behavior
- **Description:** Students reason about how changing variable initialization values, update rates, or expressions changes the program's output or behavior, supporting algorithmic analysis.
- **Challenge format:** Concept, analysis and explanation. Show code with a variable and ask "If we change this initialization from 0 to 100, what happens?" or "Why does this need to be multiplied by 2?" Students explain or predict. Auto‑grading checks explanation quality.
- **CSTA:** MS‑PRO‑DH‑04, MS‑ALG‑AF‑01.

---

## Grade 8

Students use variables and expressions in complex algorithms and data processing; they analyze how expressions and variable choices affect efficiency and correctness.

### T09.G8.01 – Use variables in iterative algorithms

_Dependency:_
  * T01.G3.01: Complete a simple script with missing blocks
  * T07.G3.01: Use a counted repeat loop
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G7.03: Use variables in conditional logic with compound conditions
  * T09.G7.04: Analyze how variable updates affect program behavior


- **Short name:** Variables in complex algorithms
- **Description:** Students implement algorithms (e.g., searching, sorting, iterative numerical methods) that rely on variables to track state across many iterations, such as a variable tracking the index in a search or the accumulator in a repeated approximation.
- **Challenge format:** Coding, algorithmic challenge. Prompt: "Implement a linear search: given a list and a target, use variables to track the index and found status. Return the index if found, else -1." Students implement. Auto‑grading checks correctness on test cases.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑PF‑02.

### T09.G8.02 – Analyze expressions for efficiency and correctness

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G7.03: Use variables in conditional logic with compound conditions
  * T09.G7.04: Analyze how variable updates affect program behavior


- **Short name:** Evaluate expression design
- **Description:** Students compare different expressions or variable strategies that solve the same problem (e.g., computing a sum by repeated addition vs direct formula) and reason about correctness, readability, and efficiency.
- **Challenge format:** Concept, comparison and explanation. Show two versions of code computing the same result using different expressions; ask which is better and why. Auto‑grading scores explanation quality.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑DH‑05, MS‑ALG‑AF‑02.

### T09.G8.03 – Use variables in data collection and statistical analysis

_Dependency:_
  * T04.G2.01: Identify the repeating unit in a longer pattern
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G7.03: Use variables in conditional logic with compound conditions
  * T09.G7.04: Analyze how variable updates affect program behavior


- **Short name:** Variables for data-driven programs
- **Description:** Students use variables (or lists of variables) to collect data from user input or sensors, compute statistics on the data, and use those statistics in expressions to make decisions or report findings.
- **Challenge format:** Coding, project. Prompt: "Collect 10 temperature readings. Calculate the average, min, and max. If the average > 30, display 'Hot!'." Students implement data collection and analysis. Auto‑grading checks calculations.
- **CSTA:** MS‑PRO‑DH‑04, MS‑DAA‑DP‑05, MS‑DAA‑DP‑06.

### T09.G8.04 – Debug variable-related logical errors

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G7.03: Use variables in conditional logic with compound conditions
  * T09.G7.04: Analyze how variable updates affect program behavior


- **Short name:** Fix complex variable bugs
- **Description:** Students identify and fix bugs related to variable scope, initialization order, incorrect update expressions, or misuse of variables in conditionals. Debugging is more sophisticated, involving tracing across multiple blocks or loops.
- **Challenge format:** Coding, debugging challenge. A project has a variable that is not initialized before use, or an expression that produces wrong results due to order of operations or scope issues. Students fix it. Auto‑grading checks correctness.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑TR‑11.

### T09.G8.05 – Use expressions to implement mathematical or logical rules

_Dependency:_
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.02: Use a variable in a conditional (if block)
  * T09.G3.03: Debug missing or wrong variable updates
  * T09.G7.03: Use variables in conditional logic with compound conditions
  * T09.G7.04: Analyze how variable updates affect program behavior


- **Short name:** Implement formulas in code
- **Description:** Students take mathematical formulas or logical rules (e.g., distance = speed × time, tax = price × rate, is_valid = age >= 18 AND has_id) and translate them into variable assignments and expressions in code.
- **Challenge format:** Coding, project. Prompt: "Implement the quadratic formula: x = (-b ± sqrt(b² - 4ac)) / 2a. Create variables for a, b, c and compute both roots." Students implement the expressions. Auto‑grading checks correct output for test cases.
- **CSTA:** MS‑PRO‑DH‑05, MS‑ALG‑AF‑02.

---

### Notes on Dependencies and Alignment

**Editor Notes:**
- K–2 foundations: Conceptual work on numeric and "changing value" intuitions lives in T01/T04 (repeats, counters) and T25 (data representation) and is picture‑based/non‑coding. T09 assumes these foundations.
- G3–5: T09 is a gateway programming topic that follows the progression: create/use simple variables → use in conditions → debug missing updates → trace changes. Complex expressions involving multiplication/division are appropriately placed in G4.
- G6–8: T09 skills assume solid use of basic variables and focus on complex expressions, real‑world modeling, and algorithm implementation.
- The G3 debugging skill (T09.G3.03) is an excellent example of contextualized debugging that teaches debugging as a natural part of learning variables.
- This design manages G3 cognitive load effectively and aligns with CSTA PRO‑DH expectations while keeping skills small, progressive, and CreatiCode‑implementable.
