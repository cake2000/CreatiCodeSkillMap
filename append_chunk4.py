
with open('t09_content.txt', 'a') as f:
    f.write(r'''ID: T09.G7.01
Topic: T09 – Variables & Expressions
Skill: Model dynamic systems where variables change over time
Description: **Student task:** Students create simulations where variables represent quantities that change each frame or time step. Examples: position updated by velocity, population growing by percentage, temperature cooling. They set up update rules (e.g., "change position by speed") and observe how repeated updates create realistic animations.

Dependencies:
* T07.G5.01: Simulate repeated experiments with a loop
* T09.G6.09: Use temporary variables for multi-step calculations

ID: T09.G7.02
Topic: T09 – Variables & Expressions
Skill: Use rounding and absolute value functions
Description: **Student task:** Students use rounding functions to convert decimals to integers: round() rounds to nearest, floor() rounds down, ceiling() rounds up. They also use abs() to get magnitude without regard to sign. They understand when each is appropriate. Examples: "set rounded_score to round(score)" for display, "set pages to ceiling(items / 10)" for pagination, "set distance to abs(x1 - x2)" for magnitude.

Dependencies:
* T09.G6.04: Use exponents (^) and modulo (%) operators

ID: T09.G7.03
Topic: T09 – Variables & Expressions
Skill: Use square root and distance functions
Description: **Student task:** Students use the sqrt() function to find square roots and distance 2D block to calculate Euclidean distance between points. They apply these for distance formulas (Pythagorean theorem), collision detection ranges, or proximity checks. Examples: "set distance to sqrt((x2-x1)^2 + (y2-y1)^2)" or using the built-in distance block for simplified calculations.

Dependencies:
* T09.G7.02: Use rounding and absolute value functions

ID: T09.G7.04
Topic: T09 – Variables & Expressions
Skill: Use min, max, and direction functions
Description: **Student task:** Students use min() and max() functions to keep variable values within bounds and the direction block to calculate angles between points. Examples: "set x to max(0, min(480, x))" to keep x between 0 and 480, "set health to max(0, health)" to prevent negative health, or calculate angle toward moving target for aiming mechanics. These are essential for game boundaries, clamping values, and trajectory calculations.

Dependencies:
* T09.G7.03: Use square root and distance functions

ID: T09.G7.05
Topic: T09 – Variables & Expressions
Skill: Compute average using sum and count variables
Description: **Student task:** Students implement average calculation: maintain a sum variable (accumulating values) and a count variable (tracking how many), then compute average by dividing sum by count. This combines multiple variable patterns and connects to data analysis.

Dependencies:
* T09.G5.08: Use the accumulator pattern to compute running totals
* T09.G6.09: Use temporary variables for multi-step calculations

ID: T09.G7.06
Topic: T09 – Variables & Expressions
Skill: Use compound conditions (AND, OR, NOT) with variables
Description: **Student task:** Students create conditional expressions using logical operators (AND, OR, NOT) to combine multiple variable comparisons. Example: "if score > 10 AND lives > 0" or "if NOT game_over". This enables more nuanced decision logic.

Dependencies:
* T09.G5.11: Track high score using variable comparison
* T09.G6.11: Debug off-by-one and comparison operator errors

ID: T09.G7.07
Topic: T09 – Variables & Expressions
Skill: Choose and apply correct variable scope (for-this-sprite vs for-all-sprites)
Description: **Student task:** Students choose the appropriate scope when creating variables: for-this-sprite for private data each sprite clone needs separately (e.g., individual clone's speed, health), and for-all-sprites for shared data like game score that all sprites can read and update. They debug scope-related bugs where a variable unexpectedly shows the same value across all clones, or where sprites can't access needed data. They demonstrate sharing data between sprites using for-all-sprites variables.

Dependencies:
* T09.G5.07: Use variables as settings to control program behavior
* T09.G6.01: Model real-world quantities using variables and formulas

ID: T09.G7.08
Topic: T09 – Variables & Expressions
Skill: Save and load variables from files (import/export)
Description: **Student task:** Students use file export operations to save variable values to a file and file import operations to load them back. This enables persistent storage of game state, settings, or high scores that survives beyond program execution. They understand how to format data for export/import and create complete save/load functionality.

Dependencies:
* T09.G7.07: Choose and apply correct variable scope (for-this-sprite vs for-all-sprites)

ID: T09.G7.09
Topic: T09 – Variables & Expressions
Skill: Predict behavior changes from modifying variable values
Description: **Student task:** Students analyze existing code and predict how behavior changes when variable initialization values, update amounts, or conditions are modified. Example: "If speed changes from 5 to 10, what happens?" This is analytical reasoning about code without running it.

Dependencies:
* T09.G6.11: Debug off-by-one and comparison operator errors
* T09.G7.01: Model dynamic systems where variables change over time

ID: T09.G7.10
Topic: T09 – Variables & Expressions
Skill: Use regex test to validate text patterns
Description: **Student task:** Students use the regex test operation to check if a text string matches a regular expression pattern, returning true or false. They apply this for input validation (e.g., checking if email format is valid, if password meets requirements). Example: test if text matches pattern "^[A-Za-z]+$" for letters only.

Dependencies:
* T09.G6.08: Transform text with replace, split, and case operators

ID: T09.G7.11
Topic: T09 – Variables & Expressions
Skill: Use regex match to find pattern occurrences
Description: **Student task:** Students use the regex match operation to find all occurrences of a pattern in text, returning a list of matches. They apply this for extracting data (e.g., finding all numbers in text, extracting hashtags from messages). Example: match all words starting with capital letters.

Dependencies:
* T09.G7.10: Use regex test to validate text patterns

ID: T09.G7.12
Topic: T09 – Variables & Expressions
Skill: Use regex replace and split for pattern-based text processing
Description: **Student task:** Students use regex replace to substitute text matching a pattern with replacement text, and regex split to break text into parts based on a pattern delimiter (not just fixed strings). They apply these for advanced text processing: removing all digits, normalizing whitespace, flexible parsing. Examples: replace all sequences of spaces with single space, split by any whitespace using pattern "\s+".

Dependencies:
* T09.G7.11: Use regex match to find pattern occurrences

ID: T09.G7.13
Topic: T09 – Variables & Expressions
Skill: Debug variable scope and update timing errors
Description: **Student task:** Students identify and fix bugs related to variable scope (using for-this-sprite when for-all-sprites was needed, or vice versa) and update timing (variable read before being set in another script). They trace variable values across multiple sprites and event handlers to diagnose why a variable has an unexpected value. This prepares them for G8 concurrent update debugging.

Dependencies:
* T09.G7.07: Choose and apply correct variable scope (for-this-sprite vs for-all-sprites)
* T09.G7.09: Predict behavior changes from modifying variable values

ID: T09.G7.14
Topic: T09 – Variables & Expressions
Skill: Design variable naming conventions for maintainability
Description: **Student task:** Students establish and follow consistent variable naming conventions (e.g., camelCase, snake_case, descriptive names) for their projects. They understand how good naming improves code readability and maintainability. They refactor existing code to use better variable names and explain why certain names are clearer than others. Examples: "playerSpeed" vs "ps", "highScore" vs "hs", "isGameOver" vs "flag1".

Dependencies:
* T09.G6.10: Trace variable values across multiple event handlers
* T09.G7.07: Choose and apply correct variable scope (for-this-sprite vs for-all-sprites)

ID: T09.G7.15
Topic: T09 – Variables & Expressions
Skill: Design multi-variable reactive systems with change events
Description: **Student task:** Students design complex reactive systems where multiple variable-changed events coordinate behavior. Building on G5.29's basic variable-changed event, they now: (1) Chain variable changes (when scoreChanged triggers levelCheck, which may trigger levelChanged), (2) Prevent infinite loops from circular dependencies, (3) Coordinate multiple sprites responding to the same variable change, (4) Debug unexpected cascade effects. Example: score change triggers UI update, achievement check, AND sound effect - students ensure all handlers complete without conflicts.

Dependencies:
* T09.G5.29: React to variable changes with when-variable-changed event
* T09.G6.10: Trace variable values across multiple event handlers
* T09.G7.07: Choose and apply correct variable scope (for-this-sprite vs for-all-sprites)

ID: T09.G7.16
Topic: T09 – Variables & Expressions
Skill: Store and process AI model outputs in variables
Description: **Student task:** Students use variables to capture outputs from AI blocks (ChatGPT responses, image recognition results, speech-to-text transcriptions) and process them for further use. They understand that AI blocks store their results in specified variables, then use string operations or conditionals to extract meaning from the responses. Example: "ChatGPT request [question] result [aiResponse]", then "if aiResponse includes yes then do action". This connects AI capabilities to programmatic decision-making.

Dependencies:
* T09.G5.12: Apply basic text formatting using string operations
* T09.G6.12: Use variables to parameterize AI prompts dynamically
* T09.G7.10: Use regex test to validate text patterns

ID: T09.G7.17
Topic: T09 – Variables & Expressions
Skill: Create multiplayer game state with shared variables
Description: **Student task:** Students design variable structures for multiplayer games where multiple players need access to shared state. They use for-all-sprites variables for global game state (game_phase, current_turn), and consider how cloud variables can synchronize state across connected players. Example: create turn-based game with "currentPlayer" variable that all sprites check, or shared "gameOver" flag that affects all players. Students plan variable scoping to ensure appropriate data sharing vs privacy.

Dependencies:
* T09.G7.07: Choose and apply correct variable scope (for-this-sprite vs for-all-sprites)
* T09.G7.13: Debug variable scope and update timing errors

ID: T09.G7.18
Topic: T09 – Variables & Expressions
Skill: Debug race conditions in concurrent variable updates
Description: **Student task:** Students identify and fix race conditions where multiple scripts attempt to update the same variable simultaneously, causing unpredictable results. They trace scenarios like: two "when I receive" handlers both trying to update score, or collision handler running while another script reads the same variable. They apply fixes such as using flags to prevent concurrent access, ordering operations carefully, or using atomic update patterns. Example: two clones both increment a shared counter at the same time, causing some increments to be lost.

Dependencies:
* T09.G7.13: Debug variable scope and update timing errors
* T09.G7.17: Create multiplayer game state with shared variables

ID: T09.G7.19
Topic: T09 – Variables & Expressions
Skill: Implement linear interpolation for smooth animations (tweening)
Description: **Student task:** Students implement linear interpolation (lerp) to create smooth transitions between values. The lerp formula is: result = start + (end - start) * t, where t goes from 0 to 1. They use this for smooth movement, color fading, size transitions, and easing animations. Example: smoothly move a sprite from position A to position B by updating "set x to startX + (endX - startX) * progress" where progress increases from 0 to 1. Students understand that tweening creates professional-quality animations compared to abrupt changes.

Dependencies:
* T09.G7.01: Model dynamic systems where variables change over time
* T09.G7.04: Use min, max, and direction functions

ID: T09.G7.20
Topic: T09 – Variables & Expressions
Skill: Extract structured data from text using split and part-of operators
Description: **Student task:** Students use the `split [text] by [delimiter]` block to break structured text into parts, and `part (index) of [text] by [separator]` to extract specific fields. They apply this to parse CSV data, extract fields from formatted strings, or process structured input. Examples: split "apple,banana,cherry" by "," to get individual fruits, extract username from "user:password" format, parse coordinates from "x:100,y:200" string. This connects string manipulation to data processing workflows.

Dependencies:
* T09.G6.08: Transform text with replace, split, and case operators
* T09.G7.10: Use regex test to validate text patterns

ID: T09.G7.21
Topic: T09 – Variables & Expressions
Skill: Use AI to generate variable-based code from natural language
Description: **Student task:** Students use CreatiCode's AI assistant (XO) or ChatGPT blocks to generate code snippets involving variables from natural language descriptions. They describe what they want: "Create a score variable that starts at 0 and increases by 10 when touching a coin", then evaluate, test, and potentially modify the AI-generated code. They learn to: (1) write clear prompts that specify variable names and behaviors, (2) verify the generated code works correctly, (3) identify and fix any issues in AI-generated variable logic. This skill prepares students for AI-assisted programming workflows.

Dependencies:
* T09.G6.12: Use variables to parameterize AI prompts dynamically
* T09.G7.16: Store and process AI model outputs in variables

ID: T09.G7.22
Topic: T09 – Variables & Expressions
Skill: Implement performance-aware variable update patterns
Description: **Student task:** Students identify performance issues where variables are updated too frequently or unnecessarily, causing lag. They apply optimization patterns: (1) throttling (update at most once per N frames), (2) change detection (only update if value actually changed), (3) caching (store expensive calculations). Example: instead of recalculating distance to target every frame, cache the value and only recalculate when positions change. They measure performance before/after optimization using frame rate or timing variables.

Dependencies:
* T09.G7.01: Model dynamic systems where variables change over time
* T09.G7.09: Predict behavior changes from modifying variable values

ID: T09.G7.23
Topic: T09 – Variables & Expressions
Skill: Design variable state for AI conversation memory
Description: **Student task:** Students design variable structures to enable AI systems to "remember" conversation context across multiple interactions. They create variables for: user preferences mentioned earlier, conversation topics discussed, follow-up questions, interaction count. Example: AI tutor remembers student's favorite subject (stored in variable) and references it in later explanations. They implement: (1) detecting key information from AI responses using string operations, (2) storing extracted info in variables, (3) injecting stored context into future prompts.

Dependencies:
* T09.G6.12: Use variables to parameterize AI prompts dynamically
* T09.G7.16: Store and process AI model outputs in variables
* T09.G7.20: Extract structured data from text using split and part-of operators

ID: T09.G7.24
Topic: T09 – Variables & Expressions
Skill: Use AI to explain what variable code does
Description: **Student task:** Students use AI tools (XO assistant or ChatGPT blocks) to analyze and explain existing variable code. They paste code and ask: "What does this code do?", "What will the variable 'score' equal after this runs?", "What happens if 'lives' starts at 0 instead of 3?" They critically evaluate AI explanations: (1) Is it correct? (2) Did it miss anything? (3) Can it explain edge cases? This develops AI-assisted learning skills and builds ability to verify AI-generated explanations through reasoning.

Dependencies:
* T09.G7.09: Predict behavior changes from modifying variable values
* T09.G7.21: Use AI to generate variable-based code from natural language

ID: T09.G7.25
Topic: T09 – Variables & Expressions
Skill: Implement exponential backoff using variables
Description: **Student task:** Students implement the exponential backoff pattern: a delay that doubles after each failed attempt. They create variables for: currentDelay (starts at 1), attemptCount, maxDelay. Pattern: on failure, "set currentDelay to currentDelay * 2", cap with "if currentDelay > maxDelay then set currentDelay to maxDelay". Applications: retry logic for network requests, rate limiting, progressive difficulty. This algorithmic pattern teaches geometric growth and practical resilience strategies.

Dependencies:
* T09.G7.01: Model dynamic systems where variables change over time
* T09.G7.04: Use min, max, and direction functions

ID: T09.G7.26
Topic: T09 – Variables & Expressions
Skill: Debug state inconsistencies across event handlers
Description: **Student task:** Students identify and fix bugs where multiple event handlers leave variables in inconsistent states. Example: "when key pressed" and "when clicked" both modify playerState but assume different starting values. They trace event sequences that cause problems: (1) identify which handlers access shared variables, (2) trace what happens if events fire in different orders, (3) add state validation or synchronization to ensure consistency. This prepares for G8 concurrent programming challenges.

Dependencies:
* T09.G7.13: Debug variable scope and update timing errors
* T09.G7.18: Debug race conditions in concurrent variable updates

ID: T09.G7.27
Topic: T09 – Variables & Expressions
Skill: Verify invariants during debugging
Description: **Student task:** Students use invariant checking as a debugging technique. They: (1) Identify the invariants that should hold (from G5.24/G6.25), (2) Add console logs that display invariant conditions at key points, (3) Run code and watch for invariant violations, (4) Trace back to find what operation broke the invariant. Example: For a game with "health invariant: 0 <= health <= maxHealth", add "console log [health >= 0 AND health <= maxHealth]" after every health update. When it logs "false", they found the bug. This systematic debugging approach catches bugs earlier.

Dependencies:
* T09.G6.25: Write preconditions and postconditions for variable updates
* T09.G7.13: Debug variable scope and update timing errors

ID: T09.G7.28
Topic: T09 – Variables & Expressions
Skill: Implement observer pattern for variable change notifications
Description: **Student task:** Students implement a basic observer pattern where changes to key variables automatically trigger notification to other parts of the program. They use CreatiCode's "when variable changed" event block to create reactive systems. Examples: UI automatically updates when score changes, sound plays when health drops below threshold, save system triggers when game state changes. They design: (1) Which variables are "observable", (2) What reactions should occur on changes, (3) How to prevent infinite update loops. This pattern is fundamental to modern reactive programming.

Dependencies:
* T09.G7.15: Design multi-variable reactive systems with change events
* T09.G7.17: Create multiplayer game state with shared variables

ID: T09.G7.29
Topic: T09 – Variables & Expressions
Skill: Use bisection to isolate variable bugs in large programs
Description: **Student task:** Students apply binary search thinking to debugging: systematically divide the program in half to find which section contains the bug. For variable bugs: (1) Add console log at middle of program, (2) Check if variable is correct at that point, (3) If correct, bug is in second half; if wrong, bug is in first half, (4) Repeat with smaller sections. This O(log n) approach finds bugs faster than linear searching through code. Example: Variable shows wrong value at end of 100-block program; bisection finds the bug in 7 checks instead of 100.

Dependencies:
* T09.G5.26: Create minimal reproducible examples for variable bugs
* T09.G7.26: Debug state inconsistencies across event handlers

ID: T09.G7.30
Topic: T09 – Variables & Expressions
Skill: Design prompts that correctly describe variable state
Description: **Student task:** Students learn to write AI prompts that accurately communicate variable state for debugging or code generation. They practice: (1) Describing current variable values clearly, (2) Explaining the expected vs actual behavior, (3) Providing context about variable types and purposes, (4) Structuring prompts so AI understands the data model. Example: Instead of "my score is broken", write "I have a variable 'score' (number, starts at 0, increments by 10 on coin touch). Expected: 30 after 3 coins. Actual: 10. Here's my code..." This prompt engineering skill maximizes AI assistance effectiveness.

Dependencies:
* T09.G6.20: Trace AI prompt variables to debug unexpected AI outputs
* T09.G7.24: Use AI to explain what variable code does

ID: T09.G8.01
Topic: T09 – Variables & Expressions
Skill: Use variables to track index position in linear search
Description: **Student task:** Students implement a linear search algorithm that uses a variable to track the current index position while searching through values. They initialize an index variable, update it in each iteration, and use it to check each position until finding the target value or reaching the end.

Dependencies:
* T02.G6.02: Use the pseudocode generation block
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds
* T09.G7.06: Use compound conditions (AND, OR, NOT) with variables
* T09.G7.09: Predict behavior changes from modifying variable values

ID: T09.G8.02
Topic: T09 – Variables & Expressions
Skill: Use flag variables in search algorithms to track found status
Description: **Student task:** Students use a boolean flag variable (e.g., "found") to remember whether a search has succeeded. They set the flag to false initially, update it to true when the target is found, and check it to determine next actions. This pattern helps control loop termination and post-search behavior.

Dependencies:
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds
* T09.G8.01: Use variables to track index position in linear search

ID: T09.G8.03
Topic: T09 – Variables & Expressions
Skill: Use variables in iterative approximation algorithms
Description: **Student task:** Students implement iterative approximation algorithms (e.g., Newton's method for square roots, binary search for values) that use variables to track and refine estimates across multiple iterations. They understand convergence criteria and when to stop iterating.

Dependencies:
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T07.G6.01: Trace nested loops with variable bounds
* T09.G8.02: Use flag variables in search algorithms to track found status

ID: T09.G8.04
Topic: T09 – Variables & Expressions
Skill: Simplify and optimize variable expressions
Description: **Student task:** Students identify opportunities to simplify expressions: replacing "x + x + x" with "x * 3", factoring common subexpressions, or replacing a counting loop with a direct formula. They evaluate trade-offs between readability and efficiency.

Dependencies:
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds
* T09.G6.04: Use exponents (^) and modulo (%) operators
* T09.G7.09: Predict behavior changes from modifying variable values
* T10.G6.01: Sort a table by a column

ID: T09.G8.05
Topic: T09 – Variables & Expressions
Skill: Use trigonometric functions in expressions
Description: **Student task:** Students use sine, cosine, tangent, and their inverse functions (asin, acos, atan) to calculate angles and circular motion. They apply these to create circular paths, calculate trajectory angles, or convert between polar and Cartesian coordinates. Examples: "set x to radius * cos(angle)", "set angle to atan2(dy, dx)" for direction to target.

Dependencies:
* T02.G6.02: Use the pseudocode generation block
* T07.G6.01: Trace nested loops with variable bounds
* T09.G7.03: Use square root and distance functions
* T11.G6.16: Analyze a program's structure using a checklist and suggest specific improvements

ID: T09.G8.06
Topic: T09 – Variables & Expressions
Skill: Use logarithmic and exponential functions in expressions
Description: **Student task:** Students use natural logarithm (ln), base-10 logarithm (log), and exponential functions (e^x, 10^x) in calculations. They apply these for exponential growth/decay models, compound interest, scientific calculations, or data transformations. Examples: modeling population growth, radioactive decay, pH calculations, or converting between logarithmic and linear scales.

Dependencies:
* T09.G8.05: Use trigonometric functions in expressions

ID: T09.G8.07
Topic: T09 – Variables & Expressions
Skill: Use cloud variables for persistent data storage
Description: **Student task:** Students use cloud variables to save data that persists across sessions and is shared between users. They understand that cloud variables are stored on a server and updated in real-time, enabling high scores, user preferences, or multiplayer data sharing.

Dependencies:
* T04.G6.01: Group snippets by underlying algorithm pattern
* T07.G6.01: Trace nested loops with variable bounds
* T09.G7.07: Choose and apply correct variable scope (for-this-sprite vs for-all-sprites)
* T09.G7.08: Save and load variables from files (import/export)
* T15.G6.01: Evaluate an interface for usability

ID: T09.G8.08
Topic: T09 – Variables & Expressions
Skill: Debug variable scope and concurrent update errors
Description: **Student task:** Students identify and fix bugs in programs with multiple sprites sharing variables: scope confusion (for-this-sprite vs for-all-sprites), race conditions when multiple scripts update the same variable, or initialization order dependencies. They trace variable states across concurrent scripts.

Dependencies:
* T02.G6.02: Use the pseudocode generation block
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T07.G6.01: Trace nested loops with variable bounds
* T09.G7.13: Debug variable scope and update timing errors

ID: T09.G8.09
Topic: T09 – Variables & Expressions
Skill: Use variables to manage state in multi-turn AI conversations
Description: **Student task:** Students use variables to track conversation context across multiple AI interactions. Examples: storing user preferences mentioned earlier, tracking conversation topics, maintaining dialogue history, or counting interaction rounds. They understand how variables enable AI systems to "remember" previous interactions and provide contextually relevant responses. Example: "set userFavoriteColor to [answer]", then later "generate poem about [userFavoriteColor]".

Dependencies:
* T09.G6.10: Trace variable values across multiple event handlers
* T09.G6.12: Use variables to parameterize AI prompts dynamically
* T09.G7.07: Choose and apply correct variable scope (for-this-sprite vs for-all-sprites)

ID: T09.G8.10
Topic: T09 – Variables & Expressions
Skill: Analyze variable usage patterns for code optimization
Description: **Student task:** Students analyze their code to identify variable usage patterns and optimization opportunities: variables that are set but never read (dead code), variables updated unnecessarily, or calculations that could be cached in variables instead of recomputed. They refactor code to eliminate redundant variable operations and improve efficiency while maintaining correctness.

Dependencies:
* T09.G7.09: Predict behavior changes from modifying variable values
* T09.G7.14: Design variable naming conventions for maintainability
* T09.G8.04: Simplify and optimize variable expressions

ID: T09.G8.11
Topic: T09 – Variables & Expressions
Skill: Translate mathematical formulas into code expressions
Description: **Student task:** Students translate real-world formulas (distance = speed × time, area = π × r², compound interest) into variable assignments and expressions. They handle operator precedence, multi-step calculations, and unit considerations. This capstone skill demonstrates mastery of variables and expressions.

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T09.G6.03: Use parentheses to override operator precedence
* T09.G7.05: Compute average using sum and count variables

ID: T09.G8.12
Topic: T09 – Variables & Expressions
Skill: Use fast-updating cloud variables for real-time synchronization
Description: **Student task:** Students use CreatiCode's cloud variable system to create real-time multiplayer experiences. They join or create cloud sessions with `join cloud session` or `create cloud session named`, then use cloud variables that automatically sync across all connected players. They understand the difference between regular cloud variables (for persistence) and fast-updating cloud variables (for real-time gameplay). Example: sync player positions in a multiplayer racing game, or create a collaborative drawing canvas where strokes appear for all users in real-time.

Dependencies:
* T09.G7.17: Create multiplayer game state with shared variables
* T09.G8.07: Use cloud variables for persistent data storage

ID: T09.G8.13
Topic: T09 – Variables & Expressions
Skill: Use variables with web search and semantic database results
Description: **Student task:** Students use variables to work with CreatiCode's web search and semantic database blocks. They store search results (from `web search [query] store top (K) in table`) and semantic query results in table variables, then extract and process specific fields. Example: search for information about a topic, store results in a table variable, extract the first result's summary, and display it to the user. This connects AI-powered information retrieval to variable-based data processing.

Dependencies:
* T09.G7.16: Store and process AI model outputs in variables
* T09.G8.09: Use variables to manage state in multi-turn AI conversations

ID: T09.G8.14
Topic: T09 – Variables & Expressions
Skill: Build adaptive AI systems using variable-based context
Description: **Student task:** Students design AI interactions that adapt based on accumulated variable state. They track user preferences, interaction history, and conversation context in variables, then use this context to modify AI prompts and responses. Example: build a personalized tutor that tracks which topics the user struggles with (stored in variables), adjusts difficulty based on success rate, and provides targeted help. This represents advanced integration of variables with AI capabilities for intelligent, context-aware applications.

Dependencies:
* T09.G7.16: Store and process AI model outputs in variables
* T09.G8.09: Use variables to manage state in multi-turn AI conversations
* T09.G8.10: Analyze variable usage patterns for code optimization

ID: T09.G8.15
Topic: T09 – Variables & Expressions
Skill: Use variables for memoization and caching
Description: **Student task:** Students implement memoization by storing computed results in variables to avoid redundant calculations. They create cache variables that store previously computed values and check the cache before recalculating. Example: caching Fibonacci numbers, storing collision detection results that are reused in the same frame, or caching expensive AI query results. Students measure performance improvement from caching and understand trade-offs between memory usage and computation time.

Dependencies:
* T09.G8.04: Simplify and optimize variable expressions
* T09.G8.10: Analyze variable usage patterns for code optimization

ID: T09.G8.16
Topic: T09 – Variables & Expressions
Skill: Design variable schemas for complex state management
Description: **Student task:** Students design organized variable naming schemes and structures for managing complex application state. They create variable hierarchies using naming conventions (e.g., player_health, player_x, player_y for player state), document their variable schemas, and plan how different parts of the program will read and update shared state. Example: designing the variable structure for a game with multiple levels, inventory system, and save/load functionality. This capstone skill demonstrates mastery of variables for large-scale applications.

Dependencies:
* T09.G7.14: Design variable naming conventions for maintainability
* T09.G8.10: Analyze variable usage patterns for code optimization
* T09.G8.14: Build adaptive AI systems using variable-based context

ID: T09.G8.17
Topic: T09 – Variables & Expressions
Skill: Generate procedural content using noise functions
Description: **Student task:** Students use CreatiCode's `noise at x (x) y (y) seed (seed)` function to generate smooth, random-looking values for procedural content generation. They understand that noise functions produce consistent values for the same inputs (unlike random), creating coherent patterns. Applications include: terrain generation (height maps), texture variations, natural movement patterns, and organic shapes. Example: use noise to create a rolling hills landscape where y-position varies smoothly based on x-position, or generate random-looking but reproducible tree positions for a forest.

Dependencies:
* T09.G7.01: Model dynamic systems where variables change over time
* T09.G8.05: Use trigonometric functions in expressions

ID: T09.G8.18
Topic: T09 – Variables & Expressions
Skill: Solve equations dynamically with the solve equation block
Description: **Student task:** Students use CreatiCode's `solve equation [equation]` block to solve mathematical equations at runtime. The block takes an equation string and returns variable values (e.g., "solve equation [x + y = 10, x + 2y = 12]" returns "x,8,y,2"). They parse the returned values into separate variables using split operations. Applications include: physics simulations (solving for unknown forces), game mechanics (calculating required speeds to reach targets), and educational tools (checking student equation solutions). This advanced skill combines string handling with mathematical problem-solving.

Dependencies:
* T09.G6.13: Use the expression calculator block for complex formulas
* T09.G7.20: Extract structured data from text using split and part-of operators

ID: T09.G8.19
Topic: T09 – Variables & Expressions
Skill: Debug variable bugs with AI-assisted analysis
Description: **Student task:** Students use AI tools to help diagnose and fix variable-related bugs. They describe the bug symptoms to an AI ("My score variable stays at 0 even when I collect coins") and provide relevant code. They learn to: (1) write effective bug descriptions that include expected vs actual behavior, (2) evaluate AI debugging suggestions critically, (3) verify that suggested fixes actually work, (4) understand WHY the fix works rather than just applying it blindly. This skill develops meta-cognitive debugging abilities enhanced by AI collaboration.

Dependencies:
* T09.G7.13: Debug variable scope and update timing errors
* T09.G7.21: Use AI to generate variable-based code from natural language
* T09.G8.08: Debug variable scope and concurrent update errors

ID: T09.G8.20
Topic: T09 – Variables & Expressions
Skill: Design variable structures for AI training data collection
Description: **Student task:** Students design and implement variable structures to collect training data for AI systems. They create variables and lists to store: user interactions (clicks, answers, times), game play patterns (moves, scores, strategies), or sensor data (positions, velocities). They understand how this data can train AI models to make predictions or adapt behavior. Example: collect player movement patterns in a game to train an AI opponent, or store user preferences to personalize content. This connects variables to machine learning data pipelines.

Dependencies:
* T09.G8.14: Build adaptive AI systems using variable-based context
* T09.G8.16: Design variable schemas for complex state management

ID: T09.G8.21
Topic: T09 – Variables & Expressions
Skill: Analyze variable memory usage and optimize for large-scale applications
Description: **Student task:** Students analyze how many variables their program uses and estimate memory consumption. They identify opportunities to reduce memory usage: (1) reusing temporary variables instead of creating new ones, (2) clearing large string/data variables when no longer needed, (3) using efficient data types (numbers instead of strings where possible). They compare memory-efficient vs memory-wasteful implementations and justify trade-offs between memory and code clarity.

Dependencies:
* T09.G8.10: Analyze variable usage patterns for code optimization
* T09.G8.15: Use variables for memoization and caching
* T09.G8.16: Design variable schemas for complex state management

ID: T09.G8.22
Topic: T09 – Variables & Expressions
Skill: Build table-integrated variable systems for complex data workflows
Description: **Student task:** Students design systems that combine table variables (for structured collections) with regular variables (for processing). They implement complete workflows: (1) load data from tables into variables for filtering/sorting, (2) perform calculations using variables, (3) store results back in tables. Example: load product inventory from table, calculate discounted prices using variables, update price column in table. They use table blocks with variable-driven row/column access for dynamic data processing.

Dependencies:
* T09.G5.19: Integrate table variables with regular variables for structured data
* T09.G8.16: Design variable schemas for complex state management

ID: T09.G8.23
Topic: T09 – Variables & Expressions
Skill: Design end-to-end AI application with complete variable state management
Description: **Student task:** Students design and implement a complete AI-enhanced application demonstrating mastery of variables with AI: (1) user input captured in variables, (2) variables used to construct dynamic AI prompts, (3) AI outputs stored in variables, (4) extracted data processed with expressions, (5) results displayed using variable-bound UI elements, (6) conversation state persists across interactions. Example: AI-powered quiz app that tracks user name, score, difficulty preference, generates personalized questions, evaluates answers, and adapts difficulty. This capstone skill synthesizes variables, expressions, AI integration, and state management.

Dependencies:
* T09.G8.09: Use variables to manage state in multi-turn AI conversations
* T09.G8.14: Build adaptive AI systems using variable-based context
* T09.G8.19: Debug variable bugs with AI-assisted analysis

''')