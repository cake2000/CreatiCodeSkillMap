# T14 – 2D Games & Interactive Simulations: K–8 Skill List (Draft v1)

Topic reference: `T14 2D Games & Interactive Simulations` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, PRO‑PD (with links to ALG‑AF, ALG‑PS, DAA‑DF, DAA‑DP)

Each skill below has:

- a stable **ID** (`T14.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Games and interactive experiences are introduced through simple cause‑and‑effect patterns: pressing a key or clicking makes a character move or react.

### T14.GK.01 – Press a key to make a sprite move

- **Short name:** Make a character move with a key press
- **Description:** Students create their first interactive game mechanic: pressing a key (arrow, space, or letter) triggers a sprite's movement. They recognize the connection between input (key press) and output (sprite motion) as a foundational game mechanic.
- **Challenge format:** Coding, starter project. Provided: a sprite and one `on key pressed` event block outline. Students drag a move block into the event handler and specify a direction or distance. Auto‑grading checks that a `move` block is inside the `on key pressed` handler and that the sprite moves when the key is pressed.
- **CSTA:** EK‑PRO‑PF‑02 (Create programs that include a sequence to complete a task).

### T14.GK.02 – Recognize a scoring variable

- **Short name:** Understand what a score is
- **Description:** Students see a variable displayed on screen (labeled "Score") and observe that it changes when certain events happen (e.g., touching an object). This is purely observational; they do not yet modify the code. The goal is familiarity with the concept that games track numbers.
- **Challenge format:** Concept, interactive viewing. A pre‑built project shows a sprite and a score variable on screen. When the sprite touches an object (e.g., a coin), the score increases visually. Students answer simple questions like "What happens to the score when you touch the coin?" Auto‑grading checks multiple‑choice answers.
- **CSTA:** EK‑PRO‑DH‑03 (Identify gestures and symbols in everyday life that represent information).

### T14.GK.03 – Recognize a game starting and ending

- **Short name:** Spot when a game starts and stops
- **Description:** Students observe a simple game with a clear beginning (e.g., "Click the green flag to start") and ending (e.g., "Game Over when lives reach zero"). They describe or identify which actions mark the start and end, building intuition for game states.
- **Challenge format:** Concept, interactive or picture‑based. Show a 3‑4 frame storyboard of a simple game: (1) title screen, (2) gameplay, (3) game over screen. Ask students to identify which is the "start" and which is the "end," or ask which button they would click to begin. Auto‑grading checks selected sequence or short text responses.
- **CSTA:** EK‑ALG‑AF‑01 (Identify algorithms in daily activities).

---

## Grade 1

Grade 1 students build simple games with basic movement and object interaction, still within fairly rigid templates.

### T14.G1.01 – Move a character in four directions

- **Short name:** Control movement left, right, up, down
- **Description:** Students create separate `on key pressed` handlers for multiple keys (e.g., arrow keys or WASD) so that a sprite can move in any direction. This moves beyond a single‑key movement and introduces the idea of responsive, multi‑directional control.
- **Challenge format:** Coding, starter project. Provided: a sprite and four outline `on key pressed` blocks (for up, down, left, right). Students fill in move blocks for each direction. Auto‑grading confirms that all four keys trigger movement in the correct direction and that the sprite responds immediately.
- **CSTA:** E1‑PRO‑PF‑01 (Create code from an algorithm that includes sequence and events).

### T14.G1.02 – Detect when a sprite touches a target

- **Short name:** Check if the player touches a goal
- **Description:** Students use a simple collision detection block (e.g., `if touching [object name]`) to recognize when the player sprite touches a target sprite. The collision triggers a response like a sound, message, or variable change—but students only observe or build the detection, not yet the full consequence logic.
- **Challenge format:** Coding, guided construction. Starter project includes a player sprite, a target sprite (e.g., a coin), and a movement handler. Students add an `if touching` block and a simple action (e.g., `play sound` or `say "Found it!"`). Auto‑grading checks that the `if touching` condition is present and triggers when sprites overlap.
- **CSTA:** E1‑PRO‑PF‑01.

### T14.G1.03 – Count points when collecting objects

- **Short name:** Add to a score when touching an object
- **Description:** Students combine movement, collision detection, and variable updates: the player moves, touches an object, and the score increases by a fixed amount (e.g., `change score by 1`). This simple version reinforces that game scoring is driven by events.
- **Challenge format:** Coding, starter project. Provided: a player sprite, a collectible sprite, a score variable, and movement and collision blocks partially filled. Students add `change score by 1` inside the collision handler. Auto‑grading simulates gameplay and confirms that the score increases correctly each time a collectible is touched.
- **CSTA:** E1‑PRO‑PF‑01, E1‑PRO‑DH‑02 (Identify terms that refer to values that change over time).

### T14.G1.04 – Bounce a sprite off the edge

- **Short name:** Make a sprite bounce when it hits a screen edge
- **Description:** Students add edge detection (e.g., `if on edge, bounce`) to a moving sprite, creating a simple animation that stays visible and repeats. This builds the concept of screen boundaries and sprite containment.
- **Challenge format:** Coding, starter project. Provided: a sprite with a repeated move block (either inside a `forever` loop or a simple starter script). Students add an `if on edge, bounce` block. Auto‑grading confirms that the sprite bounces and stays within the visible screen across multiple movements.
- **CSTA:** E1‑PRO‑PF‑01.

---

## Grade 2

Grade 2 introduces loops in games, more complex scoring logic, and simple turn‑based or state‑like behavior.

### T14.G2.01 – Use a forever loop for continuous game input

- **Short name:** Keep checking for key presses in a loop
- **Description:** Students wrap movement and collision checks inside a `forever` loop (triggered by `when green flag clicked`), so that the game continuously responds to input instead of responding only once. This is the foundation of a real‑time game loop.
- **Challenge format:** Coding, refactor/guided construction. Starter project has movement and collision blocks outside any loop. Students identify that the game should respond continuously and wrap the logic in a `forever` loop. Auto‑grading checks that the `forever` block is present and that the game handles repeated key presses smoothly.
- **CSTA:** E2‑PRO‑PF‑01 (Create code from an algorithm that includes sequence, events, and iteration).

### T14.G2.02 – Respawn a collectible after it is touched

- **Short name:** Make a coin reappear after collection
- **Description:** When the player collects an object, instead of the object disappearing permanently, students reset it to a new position (e.g., random coordinates or a fixed spawn point). This introduces recycling and respawning patterns common in games.
- **Challenge format:** Coding, starter project. Provided: a collectible sprite, collision detection, and score update. Students add blocks to move the collectible to a new position (e.g., `go to random position`) when touched. Auto‑grading simulates multiple collections and verifies that the collectible appears in new locations.
- **CSTA:** E2‑PRO‑PF‑01.

### T14.G2.03 – Track lives or health and end the game

- **Short name:** Lose a life and end when health is zero
- **Description:** Students add a "lives" or "health" variable, decrease it when a bad event occurs (e.g., enemy touch), and stop the game (or show a "Game Over" message) when the variable reaches zero. This introduces a simple fail condition and game state transition.
- **Challenge format:** Coding, starter project. Provided: a player sprite, an enemy sprite, movement, and a lives variable initialized to 3. Students add collision detection with the enemy that decreases lives and checks `if lives = 0 then stop` (or show a game over screen). Auto‑grading simulates collisions and confirms that lives decrease and the game ends correctly.
- **CSTA:** E2‑PRO‑PF‑01, E2‑PRO‑DH‑02 (Label different representations of information with a name and whether its value is constant or changes).

### T14.G2.04 – Add simple obstacles or hazards

- **Short name:** Create an obstacle that the player must avoid
- **Description:** Students place one or more non‑player sprites as obstacles (e.g., walls, enemies) and use collision detection to handle contact (e.g., stop movement, lose a life, bounce back). This teaches spatial reasoning and basic enemy/hazard interaction.
- **Challenge format:** Coding, guided construction. Starter project includes a player, movement controls, and a static obstacle sprite. Students add an `if touching obstacle` block that stops the player or decreases health. Auto‑grading checks that the collision handler activates when the player touches the obstacle.
- **CSTA:** E2‑PRO‑PF‑01.

---

## Grade 3

Grade 3 expands to multi‑state games (title, play, game over), more complex collision logic, and refinement of game mechanics.

### T14.G3.01 – Create a title screen and a start button

- **Short name:** Build a game start screen
- **Description:** Students design a title screen that appears when the game loads and is replaced by gameplay when a button is clicked. This introduces simple state management: the game switches from a "start" state to a "play" state.
- **Challenge format:** Coding, guided construction. Starter project includes a backdrop for the title and a button sprite. When the game starts, the button is shown; when clicked, it broadcasts a message (e.g., `game start`) that hides the button and triggers gameplay. Auto‑grading checks that the title screen displays initially and gameplay begins correctly after the button is clicked.
- **CSTA:** E3‑PRO‑PF‑01 (Develop code from a student‑created algorithm that includes sequence, events, iteration, and selection).

### T14.G3.02 – End the game with a game over screen

- **Short name:** Display a game over screen with a message
- **Description:** When a win or loss condition is met, students switch to a "game over" state: gameplay pauses, a screen appears showing the final score or outcome, and the game no longer responds to player input for gameplay (though a "restart" option may be available).
- **Challenge format:** Coding, guided construction. Starter project includes a game over backdrop and a restart button. When `game over` is triggered (e.g., lives reach 0 or goal is reached), students switch the backdrop and broadcast `game over`, which disables gameplay loops. Auto‑grading simulates win/loss conditions and confirms proper state transitions.
- **CSTA:** E3‑PRO‑PF‑01.

### T14.G3.03 – Use a loop to repeatedly spawn enemies

- **Short name:** Create multiple enemies in a loop
- **Description:** Instead of manually placing each enemy sprite, students use a loop to create multiple enemy clones or reset their positions repeatedly, building in a pattern or at intervals. This reduces code duplication and introduces spawning logic.
- **Challenge format:** Coding, guided construction with cloning or list creation. Starter project provides an enemy sprite and a loop outline. Students fill in the loop to create or respawn enemies at intervals (e.g., `repeat 5 { create clone }`). Auto‑grading verifies that the correct number of enemies appear.
- **CSTA:** E3‑PRO‑PF‑01, E3‑ALG‑AF‑01 (Write the steps in algorithms that include sequence, events, iteration, and selection).

### T14.G3.04 – Check multiple win/loss conditions

- **Short name:** End game based on several conditions
- **Description:** Students add multiple conditional branches to check different game‑ending scenarios (e.g., "win if score ≥ 10 OR lose if lives = 0 OR lose if time runs out"). This teaches compound logic in a game context.
- **Challenge format:** Coding, starter project with partial conditions. Students complete the logic using `if`, `else if`, or multiple `if` blocks with compound conditions (e.g., `if score ≥ 10 then set state to win`). Auto‑grading tests various game states and confirms correct transitions.
- **CSTA:** E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 deepens game mechanics with more sophisticated collision handling, variable timing, and refinement of game behavior.

### T14.G4.01 – Detect different types of collisions

- **Short name:** Handle multiple collision types
- **Description:** Students expand beyond simple "touching" checks to distinguish between collisions with different object types (e.g., `if touching coin` vs `if touching enemy` vs `if touching wall`), each triggering a different outcome. This mirrors real game architecture.
- **Challenge format:** Coding, starter project with multiple sprite types (coins, enemies, obstacles). Students add separate collision checks for each type, each with its own handler (e.g., coins increase score, enemies decrease lives). Auto‑grading simulates multiple collisions and confirms appropriate responses for each type.
- **CSTA:** E4‑PRO‑PF‑01 (Develop code from a student‑created algorithm that includes sequence, events, iteration, and selection).

### T14.G4.02 – Implement simple AI movement for enemies

- **Short name:** Make an enemy move toward or away from the player
- **Description:** Students create a simple AI: enemies move in a pattern (e.g., patrol left‑right) or follow a basic rule (e.g., move toward the player if closer than a distance threshold, otherwise patrol). This introduces algorithmic decision‑making in game design.
- **Challenge format:** Coding, guided construction. Starter project provides an enemy sprite and a player sprite. Students implement a loop that checks the distance or position relationship and moves the enemy accordingly (e.g., `if player x > enemy x then move right`). Auto‑grading verifies that the enemy exhibits the intended behavior.
- **CSTA:** E4‑PRO‑PF‑01.

### T14.G4.03 – Use a timer or counter for paced events

- **Short name:** Trigger events at timed intervals
- **Description:** Students implement a timer variable that increments each frame/loop iteration and triggers events when the timer reaches a threshold (e.g., spawn an enemy every 30 frames, or show a warning when time is low). This teaches event pacing.
- **Challenge format:** Coding, guided construction. Starter project includes a forever loop, a timer variable, and event triggers. Students increment the timer, check if it exceeds a threshold, and reset it. Auto‑grading verifies that events occur at the correct intervals.
- **CSTA:** E4‑PRO‑PF‑01, E4‑PRO‑DH‑02 (Trace how data flows through and alters values in an existing program, using variables).

### T14.G4.04 – Refactor game code for clarity

- **Short name:** Clean up game code and remove duplication
- **Description:** Students review their game code and identify repeated patterns (e.g., multiple similar collision checks or movement sequences) and refactor them using custom blocks or loops to reduce duplication and improve readability.
- **Challenge format:** Coding, refactor challenge. Starter project contains a working game with redundant code (e.g., four nearly identical collision handlers). Students consolidate logic using loops, custom blocks, or conditionals, preserving all functionality. Auto‑grading checks that the refactored code behaves identically and uses fewer lines.
- **CSTA:** E4‑PRO‑PF‑01, E4‑PRO‑PM‑05 (Document a program, using embedded or external comments).

---

## Grade 5

Grade 5 emphasizes game design patterns: camera systems, more complex AI, physics‑like behavior, and data collection in games.

### T14.G5.01 – Implement a scrolling camera for larger worlds

- **Short name:** Make the camera follow the player
- **Description:** Students implement a simple camera/viewport system where the player remains roughly centered on screen and the background scrolls to simulate movement through a larger world. This introduces coordinate transformation concepts.
- **Challenge format:** Coding, guided construction. Starter project includes a player sprite, a wide backdrop, and outline camera logic. Students implement: `camera x = player x - center offset` to track the player. Auto‑grading verifies that the player stays roughly centered and that the world shifts appropriately.
- **CSTA:** E5‑PRO‑PF‑01 (Develop code from student‑created algorithms that include sequence, events, iteration, selection, and variables).

### T14.G5.02 – Create enemy waves or spawning patterns

- **Short name:** Spawn waves of enemies
- **Description:** Students implement more complex enemy spawning: enemies spawn in waves (groups), with varying patterns, timings, and behaviors. This moves beyond simple looping to conditional spawning.
- **Challenge format:** Coding, guided construction. Starter project includes a spawner variable tracking the current wave and a list or counter for enemies. Students implement logic to spawn enemy groups at intervals, increase difficulty (e.g., more enemies in later waves), and detect when all enemies are defeated. Auto‑grading verifies wave progression and enemy counts.
- **CSTA:** E5‑PRO‑PF‑01, E5‑ALG‑AF‑01 (Create visual or textual representations of algorithms that include sequence, events, iteration, selection, and variables).

### T14.G5.03 – Track game statistics (kills, time, accuracy)

- **Short name:** Collect data during gameplay
- **Description:** Students add variables to track gameplay metrics beyond score (e.g., enemies defeated, accuracy percentage, time elapsed, distance traveled) and display or save these statistics for analysis or post‑game summary.
- **Challenge format:** Coding, guided construction. Starter project includes game loop and collision detection. Students add variables for each metric, update them appropriately during gameplay, and display them at the end. Auto‑grading verifies that metrics are calculated correctly and displayed accurately.
- **CSTA:** E5‑PRO‑PF‑01, E5‑PRO‑DH‑02 (Use different types of variables to store, compare, and modify data).

### T14.G5.04 – Implement power‑ups and temporary effects

- **Short name:** Add collectible power‑ups
- **Description:** Students create collectible items that grant temporary bonuses (e.g., invincibility, speed boost, rapid fire), using a timer or flag to track when the effect expires. This teaches state management and timed effects.
- **Challenge format:** Coding, guided construction. Starter project includes a player, a power‑up sprite, and a movement loop. Students add a `power up active` variable and timer; when a power‑up is collected, set the timer and modify player behavior (e.g., `if power up active, speed = 10` else `speed = 5`). Auto‑grading simulates power‑up collection and verifies timed effects.
- **CSTA:** E5‑PRO‑PF‑01.

---

## Grade 6

In middle school, games become more architecturally complex; students focus on designing and implementing systems rather than simple mechanics.

### T14.G6.01 – Design a game state machine

- **Short name:** Manage multiple game states
- **Description:** Students explicitly design and implement a state machine (e.g., using a `game state` variable) to manage transitions between title, menu, playing, paused, and game over states. This formalizes the concept of game states introduced in Grade 3.
- **Challenge format:** Coding, guided design challenge. Students draw or pseudo‑code the state diagram, then implement it using a variable and a main script that dispatches to different behavior based on the state value. Auto‑grading checks that states transition correctly and that state‑specific behaviors execute in the right state.
- **CSTA:** MS‑PRO‑PF‑01 (Analyze how a segment of code works by identifying and describing the roles of key components).

### T14.G6.02 – Implement pixel‑perfect or grid‑based collision

- **Short name:** Refine collision detection accuracy
- **Description:** Students move beyond simple rectangular collision boxes to implement more precise detection: pixel‑perfect collision (checking if visible pixels overlap) or grid‑based collision (checking tile occupancy). This improves game feel and fairness.
- **Challenge format:** Coding, guided construction. Starter project includes collision detection using a custom algorithm (e.g., checking distance thresholds or a collision list/grid). Students refine the logic to improve accuracy. Auto‑grading tests edge cases and verifies that collisions are detected at the correct boundaries.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑DH‑04 (Represent data, using appropriate data structures, including variables and collection types).

### T14.G6.03 – Use data structures to manage game objects

- **Short name:** Store and update game objects in a list
- **Description:** Instead of hardcoding individual enemy sprites, students use a list to dynamically store game object data (positions, states, velocities). This scales the game architecture: adding more enemies becomes adding to a list rather than duplicating code.
- **Challenge format:** Coding, guided construction. Starter project includes a list structure and loop outline. Students populate the list with object data (e.g., positions), then implement a loop to update and render all objects. Auto‑grading verifies that the list correctly stores and updates game object state.
- **CSTA:** MS‑PRO‑PF‑01, MS‑PRO‑DH‑04.

### T14.G6.04 – Debug game logic systematically

- **Short name:** Find and fix game behavior bugs
- **Description:** Students apply debugging techniques to game‑specific issues: a sprite moves unexpectedly, collisions trigger at wrong times, or scoring is incorrect. They use print/say blocks, trace execution, and isolate failures.
- **Challenge format:** Coding, debugging challenge. Starter project includes a game with one or two intentional bugs (e.g., collision condition is inverted, or enemy spawning loop has off‑by‑one error). Students identify the issue and fix it, with auto‑grading verifying that the corrected behavior matches the specification.
- **CSTA:** MS‑PRO‑TR‑11 (Use standard practices to test, debug, document, and peer‑review code).

---

## Grade 7

Grade 7 emphasizes algorithmic efficiency and advanced mechanics: physics approximation, pathfinding, and large‑scale game data.

### T14.G7.01 – Simulate physics: gravity and jumping

- **Short name:** Add gravity and jumping to platformer
- **Description:** Students implement a simple physics system: a character has velocity in the y‑direction, gravity continuously increases downward velocity, and jumping (pressing a key) sets upward velocity if the character is on the ground. This introduces continuous numerical simulation.
- **Challenge format:** Coding, guided construction. Starter project includes a player sprite and ground sprite. Students implement variables for `velocity y` and `gravity`, update them each frame inside the game loop, and detect ground collision to reset `jumping` state. Auto‑grading simulates gameplay and verifies realistic jump and fall behavior.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑01 (Optimize visual representations of algorithms).

### T14.G7.02 – Implement simple pathfinding (waypoints or A*)

- **Short name:** Make an enemy navigate intelligently
- **Description:** Students implement a pathfinding system where enemies move toward a goal or follow a predetermined path. Simple variants use waypoints; more advanced variants approximate A‑star behavior by moving toward the player while avoiding obstacles.
- **Challenge format:** Coding, guided construction. Starter project includes enemy and player sprites, and a waypoints list or grid. Students implement a loop that calculates the next position to move toward (waypoint or player) and updates the enemy position. Auto‑grading verifies that the enemy reaches goals or follows paths correctly.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑01.

### T14.G7.03 – Optimize collision checking to avoid lag

- **Short name:** Make collision detection efficient
- **Description:** When a game has many objects, checking all pairs can lag. Students learn to optimize: only check collisions for nearby objects (using quadtrees or spatial hashing concepts), cache results, or reduce check frequency. Even a conceptual understanding of the problem builds algorithmic thinking.
- **Challenge format:** Mixed coding and concept. Starter project includes a game with many objects and noticeable lag. Students implement an optimization (e.g., only check collisions for enemies within a distance of the player, or check every other frame). Auto‑grading measures performance improvement and verifies correctness.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑PS‑05 (Demonstrate the correctness of algorithms for given inputs).

### T14.G7.04 – Analyze and balance game difficulty

- **Short name:** Tune game difficulty parameters
- **Description:** Students play and analyze their game, identifying difficulty parameters (enemy speed, health, respawn rate, reward amounts), and deliberately adjust them to achieve a specific difficulty curve. They might gather data on success rates or time to completion and use it to guide balance.
- **Challenge format:** Concept and coding. Students build or modify a game, then document difficulty parameters and test outcomes. They write a short reflection explaining their balancing choices. Auto‑grading checks that parameters are adjusted coherently and documentation is clear.
- **CSTA:** MS‑PRO‑TR‑11, MS‑ALG‑PS‑07 (Hypothesize about internal processes and functions of opaque systems).

---

## Grade 8

Grade 8 prepares students for advanced game development by focusing on modularity, data management, and understanding game engine concepts.

### T14.G8.01 – Architect a game using modular custom blocks

- **Short name:** Design game code with reusable functions
- **Description:** Students deliberately design their game architecture using custom blocks (procedures/functions) to encapsulate game systems: collision handler, spawn system, update physics, render, etc. This introduces software engineering principles.
- **Challenge format:** Coding, architectural challenge. Students build a game by defining custom blocks for each system, with clear parameters and separation of concerns. Auto‑grading checks code structure (presence of relevant custom blocks), modularity (each block has a focused purpose), and behavior correctness.
- **CSTA:** MS‑PRO‑PD‑08 (Create modular programs that incorporate sequence, selection, and iteration).

### T14.G8.02 – Implement a particle system (visual effects)

- **Short name:** Create visual feedback with particles
- **Description:** Students implement a simple particle system: many small visual elements (e.g., sparks, smoke) that emit, move, fade, and disappear, creating visual feedback for events (explosions, hits). This combines loops, timing, and array/list management.
- **Challenge format:** Coding, guided construction. Starter project includes particle data (position, velocity, lifetime) and a loop to create and update particles. Students fill in the emission logic (when/how many particles spawn) and the update loop (move particles, decrease lifetime, remove dead ones). Auto‑grading verifies that particles emit on events and behave correctly.
- **CSTA:** MS‑PRO‑PD‑08, MS‑PRO‑DH‑04 (Represent data, using appropriate data structures).

### T14.G8.03 – Design game levels using data structures

- **Short name:** Create levels from tile maps or data
- **Description:** Instead of manually placing each game object, students define levels using data structures (lists of lists, or a string representing a tile map) and a parser that converts the data into actual game objects. This teaches data‑driven design and scales level creation.
- **Challenge format:** Coding, guided construction. Starter project includes a level data structure (e.g., a 2D array of tile IDs) and an outline parser. Students implement the parser to create platforms, obstacles, and collectibles based on the data. Auto‑grading verifies that levels are created correctly and multiple levels can be defined separately.
- **CSTA:** MS‑PRO‑DH‑04, MS‑PRO‑DH‑06 (Use iteration to access, update, and process elements in a collection).

### T14.G8.04 – Document and analyze a complete game system

- **Short name:** Explain game architecture and design choices
- **Description:** Students document their game: architecture diagram showing how systems connect, pseudocode or flowcharts for key algorithms, and written explanations of design choices (why they chose certain collision detection, what difficulty parameters they used, how enemy AI works). This reinforces reflection and communication of complex ideas.
- **Challenge format:** Documentation and reflection. Students create a design document or project report that includes architecture overview, system descriptions, and analysis of design decisions. Auto‑grading checks completeness, clarity, and alignment with the actual code.
- **CSTA:** MS‑PRO‑PM‑16 (Document a program, using comments, descriptive names, and structured guides).

---
