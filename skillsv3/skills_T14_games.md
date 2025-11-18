# T14 – 2D Games: K–8 Skill List (Draft v2)

Topic reference: `T14 2D Games` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, PRO‑PD (with links to ALG‑AF, ALG‑PS, DAA‑DF, DAA‑DP)

Each skill below has:

- a stable **ID** (`T14.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Games and interactive experiences are introduced through simple cause‑and‑effect patterns and basic game ideas (players, goals, score, start and end), using picture‑based, unplugged activities.

### T14.GK.01 – Match controls to character actions

- **Short name:** Connect a button to an action
- **Description:** Students see pictures of simple controls (e.g., arrow cards, a big “jump” button) and pictures of a character moving or reacting. They match each control to the action it causes (e.g., left arrow → move left), building the idea that input leads to game action.
- **Challenge format:** Concept, picture matching. Drag control cards to matching action pictures.
- **CSTA:** EK‑PRO‑DH‑03

### T14.GK.02 – Recognize a score in simple games

- **Short name:** Tell when points go up
- **Description:** Students look at pictures from simple games that show a score or counter. They notice when the score increases (e.g., after collecting a star) and what it means to “have more points.”
- **Challenge format:** Concept, picture‑based questions. Show before/after pictures: “Who has more points?” or “Did the score go up?”
- **CSTA:** EK‑PRO‑DH‑03

### T14.GK.03 – Recognize a game starting and ending

- **Short name:** Spot start and game over
- **Description:** Students observe a simple game story with a clear beginning (Start screen) and ending (Game Over). They identify which pictures show the start and end of the game.
- **Challenge format:** Concept, sequencing. Order 3 pictures: Start Screen -> Gameplay -> Game Over.
- **CSTA:** EK‑ALG‑AF‑01

---

## Grade 1

Grade 1 students reason about simple game structure: players, goals, obstacles, score, and what makes games easier or harder, all through pictures and stories.

### T14.G1.01 – Identify the player, goal, and obstacles

- **Short name:** Find the player, goal, and dangers
- **Description:** In a picture of a game level (e.g., a maze or platformer), students identify which character is the player, which item is the goal (e.g., a flag or treasure), and which items are hazards (e.g., spikes or enemies).
- **Challenge format:** Concept, hotspot clicking. “Click on the player.” “Click on the thing that makes you lose.”
- **CSTA:** 1A‑AP‑08

### T14.G1.02 – Apply simple game rules

- **Short name:** Follow the game rules
- **Description:** Students are given a simple rule (e.g., “Collect all coins to open the door”) and a sequence of pictures. They decide if the player followed the rule or not.
- **Challenge format:** Concept, True/False. Show a sequence where player skips coins and tries to open door. “Did they follow the rule?”
- **CSTA:** 1A‑AP‑08

### T14.G1.03 – Compare game difficulty

- **Short name:** Which game is harder?
- **Description:** Students compare two pictures of the same game level—one with more obstacles or fewer platforms—and identify which one would be harder to play.
- **Challenge format:** Concept, comparison. Show two levels side-by-side. “Which level is harder?”
- **CSTA:** 1A‑AP‑08

---

## Grade 2

Grade 2 students explore game flow concepts like turns, lives, and levels, and begin to think about game design choices, still without writing code.

### T14.G2.01 – Understand turns and rounds

- **Short name:** Whose turn is it?
- **Description:** Students look at a game situation involving multiple players or a turn-based system. They determine whose turn it is or what happens when a turn ends.
- **Challenge format:** Concept, prediction. “Player 1 just moved. Who moves next?”
- **CSTA:** 1A‑AP‑08

### T14.G2.02 – Track lives and game over conditions

- **Short name:** Count lives and game over
- **Description:** Students track a player’s “lives” through a short picture story. They identify when a life is lost (e.g., touching a hazard) and when the game is over (lives reach zero).
- **Challenge format:** Concept, tracking. Show a sequence of 3 events. “How many lives are left?”
- **CSTA:** 1A‑AP‑10

### T14.G2.03 – Recognize level progression

- **Short name:** Moving to the next level
- **Description:** Students identify the condition for moving to the next level (e.g., “When the goal is reached”) and recognize that the next level is usually different or harder.
- **Challenge format:** Concept, logic. “What must happen to go to Level 2?” (Select from images).
- **CSTA:** 1A‑AP‑10

---

## Grade 3

Grade 3 is the **gateway to coding** for games. Students move from concepts to building the core components of a 2D game: moving a character, interacting with objects, and managing basic flow.

### Strand A: Player Control

#### T14.G3.01 – Move a sprite with arrow keys (4 directions)
- **Short name:** Code 4-way movement
- **Description:** Create a script where pressing up/down/left/right arrow keys changes the sprite’s x or y position.
- **Challenge format:** Build/Parsons. Assemble `when [up arrow] key pressed` -> `change y by (10)`.
- **CSTA:** 1B‑AP‑10

#### T14.G3.02 – Move a sprite with keys (2 directions)
- **Short name:** Code left-right movement
- **Description:** Create a script for a platformer or paddle game where only left/right keys control the sprite.
- **Challenge format:** Build. Connect `when [right arrow] key pressed` -> `change x by (10)`.
- **CSTA:** 1B‑AP‑10

#### T14.G3.03 – Keep sprite on screen
- **Short name:** Stop at the edge
- **Description:** Add logic to prevent the player from moving off the stage (e.g., `if on edge, bounce` or simple coordinate checks).
- **Challenge format:** Debug/Modify. “The player walks off the screen. Fix it.”
- **CSTA:** 1B‑AP‑10

### Strand B: Interaction

#### T14.G3.04 – Detect touching a goal
- **Short name:** Code winning touch
- **Description:** Use a `touching [Sprite]?` block inside a loop to detect when the player reaches the goal.
- **Challenge format:** Build. Create `forever` -> `if <touching [Goal]> then` -> `say [You Win!]`.
- **CSTA:** 1B‑AP‑10

#### T14.G3.05 – Detect touching a hazard
- **Short name:** Code danger touch
- **Description:** Use a `touching [Color]?` or `touching [Sprite]?` block to detect hazards (spikes, enemies) and reset the player.
- **Challenge format:** Build. Create `if <touching [Spike]> then` -> `go to x: start y: start`.
- **CSTA:** 1B‑AP‑10

### Strand C: Game Flow

#### T14.G3.06 – Create a start screen
- **Short name:** Make a start button
- **Description:** Program a “Start” button sprite that hides itself and broadcasts a “Start Game” message when clicked.
- **Challenge format:** Build. `when this sprite clicked` -> `hide` -> `broadcast [Start Game]`.
- **CSTA:** 1B‑AP‑15

#### T14.G3.07 – Switch to game mode
- **Short name:** Start game on signal
- **Description:** Program game objects (player, enemies) to show themselves and start moving only when they receive the “Start Game” message.
- **Challenge format:** Modify. Change `when green flag clicked` to `when I receive [Start Game]`.
- **CSTA:** 1B‑AP‑15

#### T14.G3.08 – Trigger Game Over
- **Short name:** Broadcast game over
- **Description:** Broadcast a “Game Over” message when a losing condition is met, and have other sprites stop or hide.
- **Challenge format:** Build. `broadcast [Game Over]` -> `stop [all]`.
- **CSTA:** 1B‑AP‑15

### Strand D: Feedback

#### T14.G3.09 – Add sound effects to actions
- **Short name:** Play jump or collect sounds
- **Description:** Insert `start sound` blocks into movement or interaction scripts to provide audio feedback.
- **Challenge format:** Modify. “Add a ‘pop’ sound when the player touches the coin.”
- **CSTA:** 1B‑AP‑10

#### T14.G3.10 – Visual effects on interaction
- **Short name:** Flash or change color
- **Description:** Use graphic effects (color, brightness, ghost) to show when a player is hit or collects an item.
- **Challenge format:** Build. `change [color] effect by (25)` inside an interaction check.
- **CSTA:** 1B‑AP‑10

---

## Grade 4

Grade 4 expands into **mechanics and state**. Students build dynamic systems like projectiles and enemies, and track game state using variables.

### Strand A: Projectiles & Shooting

#### T14.G4.01 – Spawn a projectile
- **Short name:** Create a bullet clone
- **Description:** Use `create clone of [myself]` or another sprite to spawn a projectile when a key is pressed.
- **Challenge format:** Build. `when [space] key pressed` -> `create clone of [Bullet]`.
- **CSTA:** 1B‑AP‑11

#### T14.G4.02 – Move a projectile
- **Short name:** Make bullets fly
- **Description:** Program the projectile clone to move forward (change x or y, or move steps) continuously until it hits something.
- **Challenge format:** Build. `when I start as a clone` -> `repeat until <touching [edge]>` -> `move (10) steps`.
- **CSTA:** 1B‑AP‑11

#### T14.G4.03 – Clean up projectiles
- **Short name:** Delete bullets at edge
- **Description:** Ensure clones are deleted when they touch the edge or a target to prevent lag and bugs.
- **Challenge format:** Debug. “The game gets slow because bullets never disappear. Fix it.”
- **CSTA:** 1B‑AP‑11

### Strand B: Enemy Behavior

#### T14.G4.04 – Simple enemy movement
- **Short name:** Patrol back and forth
- **Description:** Program an enemy to move back and forth between two points or bounce off edges.
- **Challenge format:** Build. `forever` -> `move (5) steps` -> `if on edge, bounce`.
- **CSTA:** 1B‑AP‑10

#### T14.G4.05 – Chase the player
- **Short name:** Enemy follows player
- **Description:** Use `point towards [Player]` and `move` blocks to create a simple chasing enemy.
- **Challenge format:** Build. `forever` -> `point towards [Player]` -> `move (2) steps`.
- **CSTA:** 1B‑AP‑10

### Strand C: State Tracking

#### T14.G4.06 – Create a Score variable
- **Short name:** Make a score keeper
- **Description:** Create a global variable named “Score”, initialize it to 0, and change it when an event occurs.
- **Challenge format:** Build. `set [Score] to (0)` -> `change [Score] by (1)`.
- **CSTA:** 1B‑AP‑09

#### T14.G4.07 – Create a Lives variable
- **Short name:** Make a life counter
- **Description:** Create a variable for “Lives”, decrease it upon damage, and check if it reaches zero.
- **Challenge format:** Build. `change [Lives] by (-1)` -> `if <(Lives) < (1)> then` -> `broadcast [Game Over]`.
- **CSTA:** 1B‑AP‑09

#### T14.G4.08 – Create a Timer
- **Short name:** Make a countdown timer
- **Description:** Use a variable and a loop with `wait (1) seconds` to create a countdown timer.
- **Challenge format:** Build. `repeat until <(Time) = (0)>` -> `wait (1) secs` -> `change [Time] by (-1)`.
- **CSTA:** 1B‑AP‑09

### Strand D: Level Progression

#### T14.G4.09 – Detect level complete
- **Short name:** Check win condition
- **Description:** Check if a condition (Score > 10, or touching door) is met to trigger the next level.
- **Challenge format:** Logic/Build. `if <(Score) > (9)> then` -> `broadcast [Next Level]`.
- **CSTA:** 1B‑AP‑10

#### T14.G4.10 – Switch backdrops for levels
- **Short name:** Change the level background
- **Description:** When “Next Level” is received, switch the backdrop and reset player position.
- **Challenge format:** Build. `when I receive [Next Level]` -> `next backdrop` -> `go to x: start y: start`.
- **CSTA:** 1B‑AP‑10

---

## Grade 5

Grade 5 introduces **advanced 2D mechanics** like physics (gravity), scrolling, and more complex data handling, preparing students for full game engines.

### Strand A: Physics Basics

#### T14.G5.01 – Simulate gravity
- **Short name:** Make it fall
- **Description:** Create a `y velocity` variable. Change y by `y velocity` and change `y velocity` by a negative number (gravity) every frame.
- **Challenge format:** Build. `change [y velocity] by (-1)` -> `change y by (y velocity)`.
- **CSTA:** 1B‑AP‑10

#### T14.G5.02 – Jump with velocity
- **Short name:** Velocity jump
- **Description:** Set `y velocity` to a positive number when the jump key is pressed, but only if touching the ground.
- **Challenge format:** Build. `if <key [up arrow] pressed?> and <touching [Ground]?>` -> `set [y velocity] to (10)`.
- **CSTA:** 1B‑AP‑10

#### T14.G5.03 – Ground collision
- **Short name:** Stop on the ground
- **Description:** Prevent falling through the floor by moving the sprite up until it’s no longer touching the ground if it sinks in.
- **Challenge format:** Debug/Refine. “The player falls through the floor. Add a ground check.”
- **CSTA:** 1B‑AP‑10

### Strand B: Scrolling

#### T14.G5.04 – Camera variables
- **Short name:** Track camera position
- **Description:** Create `Scroll X` and `Scroll Y` variables to track the “camera” position based on the player’s movement.
- **Challenge format:** Build. `set [Scroll X] to (Player X)`.
- **CSTA:** 1B‑AP‑10

#### T14.G5.05 – Move background relative to camera
- **Short name:** Scroll the world
- **Description:** Position background or platform sprites based on their world position minus `Scroll X`.
- **Challenge format:** Build. `go to x: ((World X) - (Scroll X)) y: (World Y)`.
- **CSTA:** 1B‑AP‑10

### Strand C: Spawning & Waves

#### T14.G5.06 – Random spawn positions
- **Short name:** Spawn at random spots
- **Description:** When creating clones (enemies/items), set their position to a random x/y within bounds.
- **Challenge format:** Build. `go to x: (pick random -200 to 200) y: (150)`.
- **CSTA:** 1B‑AP‑11

#### T14.G5.07 – Timed waves
- **Short name:** Enemy waves
- **Description:** Use a loop to spawn a group of enemies every few seconds.
- **Challenge format:** Build. `forever` -> `repeat (5)` -> `create clone`, `wait (3) secs`.
- **CSTA:** 1B‑AP‑11

### Strand D: Data

#### T14.G5.08 – High score list
- **Short name:** Save high scores
- **Description:** Use a list to store the top 5 scores. Insert new scores in the correct position.
- **Challenge format:** Build/Modify. `add (Score) to [High Scores]`.
- **CSTA:** 1B‑AP‑09

#### T14.G5.09 – Inventory system
- **Short name:** Collect items in a list
- **Description:** Use a list to track items collected (e.g., “Key”, “Potion”). Check if an item is in the list before allowing an action.
- **Challenge format:** Build. `if <[Inventory] contains [Key]?>` -> `broadcast [Open Door]`.
- **CSTA:** 1B‑AP‑09

---

## Grade 6–8 (Middle School)

In middle school, the focus shifts to **architecture, optimization, and systems**. Students build robust engines rather than just scripts.

### Grade 6: Systems & State Machines

#### T14.G6.01 – Character State Machine
- **Short name:** State machine (Idle/Run/Jump)
- **Description:** Use a variable `State` (Idle, Run, Jump) to control animation and behavior, preventing conflicting actions (e.g., jumping while already jumping).
- **Challenge format:** Refactor. Convert spaghetti code into a clean state machine structure.
- **CSTA:** 2‑AP‑10

#### T14.G6.02 – Hitbox separation
- **Short name:** Separate hitbox and art
- **Description:** Use a simple rectangular sprite for collision detection (hitbox) and a separate sprite for animation, linking them by position.
- **Challenge format:** Build. Program the Art sprite to always `go to [Hitbox]`.
- **CSTA:** 2‑AP‑13

### Grade 7: Efficiency & Advanced Mechanics

#### T14.G7.01 – Spatial Partitioning (Grid)
- **Short name:** Grid-based movement
- **Description:** Implement movement that snaps to a grid (tile-based), useful for RPGs or puzzle games.
- **Challenge format:** Build. Round coordinates to nearest multiple of 32.
- **CSTA:** 2‑AP‑13

#### T14.G7.02 – Basic Pathfinding
- **Short name:** Move towards target intelligently
- **Description:** Create an enemy that moves towards the player but stops at walls, rather than getting stuck trying to move through them.
- **Challenge format:** Debug/Refine. Improve a “point towards” script to slide along walls.
- **CSTA:** 2‑AP‑13

### Grade 8: Engine Design

#### T14.G8.01 – Modular Level Loader
- **Short name:** Load levels from data
- **Description:** Create a system that reads a list of strings (e.g., “111000111”) to generate a level layout using clones.
- **Challenge format:** Build. Parse a string and stamp/clone tiles at correct coordinates.
- **CSTA:** 2‑AP‑14

#### T14.G8.02 – Particle System
- **Short name:** Particle effects engine
- **Description:** Create a flexible particle system (for explosions, smoke) where one sprite manages many clones with varying properties (life, speed, color).
- **Challenge format:** Build. Create a generic “Spawn Particle” custom block with parameters.
- **CSTA:** 2‑AP‑14
