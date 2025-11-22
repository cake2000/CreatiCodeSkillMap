## Topic 14: 2D Games (UPDATED - Phase 1 Optimization)

---

### KINDERGARTEN (K)

ID: T14.GK.01
Topic: T14 – 2D Games
Skill: Match controls to character actions
Description: Students drag arrow key cards (up, down, left, right) or action button cards (jump, run) onto pictures showing the matching movement or reaction (up arrow → character jumps up, right arrow → character walks right). They learn that specific inputs lead to predictable actions in games.



ID: T14.GK.02
Topic: T14 – 2D Games
Skill: Recognize a score in simple games
Description: Students compare before/after pictures of a score counter and gameplay moments (collecting a star, hitting a hazard) to see when the score changes and what it signals.




ID: T14.GK.03
Topic: T14 – 2D Games
Skill: Identify when a game starts and ends
Description: Students observe a simple game story with a clear beginning (Start screen) and ending (Game Over). They identify which pictures show the start, play, and end of the game.




ID: T14.GK.04
Topic: T14 – 2D Games
Skill: Match rewards to goals
Description: Students match pictures of finishing a level (touching a flag, clearing a board) to appropriate celebration panels (You Win text, trophy, fireworks) so they connect goals to feedback.

Dependencies:
* T14.GK.02: Recognize a score in simple games
* T14.GK.03: Identify when a game starts and ends




---

### GRADE 1

ID: T14.G1.01
Topic: T14 – 2D Games
Skill: Identify the player, goal, and obstacles
Description: In a labeled picture of a game level (maze, platformer, or board game), students point to and name: (1) the controllable character (marked with an arrow or labeled 'YOU'), (2) the goal object or location (flag, door, finish line), and (3) hazards that should be avoided (spikes, enemies, water).

Dependencies:
* T01.GK.03: Find the first and last pictures
* T14.GK.03: Identify when a game starts and ends


ID: T14.G1.02
Topic: T14 – 2D Games
Skill: Apply simple game rules
Description: Students are given a simple rule (e.g., "Collect all coins to open the door") and a sequence of pictures. They decide if the player followed the rule.

Dependencies:
* T14.G1.01: Identify the player, goal, and obstacles
* T14.GK.04: Match rewards to goals


ID: T14.G1.03
Topic: T14 – 2D Games
Skill: Compare game difficulty
Description: Students compare two pictures of the same game level—one with more obstacles or fewer platforms—and identify which one would be harder to play.

Dependencies:
* T01.GK.04: Pick the pictures that make sense


ID: T14.G1.04
Topic: T14 – 2D Games
Skill: Predict the best next move
Description: Given a short rule and a partially played level, students pick which control card (up, down, left, right, jump) keeps the player safe and moving toward the goal.

Dependencies:
* T14.G1.01: Identify the player, goal, and obstacles
* T14.GK.01: Match controls to character actions


ID: T14.G1.05
Topic: T14 – 2D Games
Skill: Distinguish helpers from hazards
Description: Students sort icons from a level (heart, speed shoe, spike, slime) into "helps you win" and "makes you lose," building vocabulary around pickups and traps.

Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed
* T14.GK.04: Match rewards to goals


---

### GRADE 2

ID: T14.G2.01
Topic: T14 – 2D Games
Skill: Identify turns and rounds in games
Description: Students look at a turn-based scene with multiple players or timers and identify whose turn it is or what happens next when a turn ends.

Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T14.G1.02: Apply simple game rules


ID: T14.G2.02
Topic: T14 – 2D Games
Skill: Track lives and game over conditions
Description: Students track a player's lives through a short picture story. They identify when a life is lost (touching a hazard) and when the game is over (lives reach zero).

Dependencies:
* T01.G1.04: Predict the next step in a story sequence
* T14.G1.05: Distinguish helpers from hazards


ID: T14.G2.03
Topic: T14 – 2D Games
Skill: Recognize level progression
Description: Students identify the condition for moving to the next level (touch goal, collect items) and notice that later levels are usually different or harder.

Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T14.G1.01: Identify the player, goal, and obstacles


ID: T14.G2.04
Topic: T14 – 2D Games
Skill: Sequence a safe route
Description: Students order 3–4 picture cards showing a safe route through a level (jump over spikes, grab key, open door) to highlight planning before play.

Dependencies:
* T01.G1.04: Predict the next step in a story sequence
* T14.G1.04: Predict the best next move


ID: T14.G2.05
Topic: T14 – 2D Games
Skill: Adjust game difficulty settings
Description: Presented with a short brief ("Make it easier for new players"), students choose the change that best matches the goal (add another heart, remove a hazard, shorten timer) to understand how game settings affect difficulty.

Dependencies:
* T01.G1.10: Match pictures to "if/then" rules
* T14.G1.03: Compare game difficulty


---

### GRADE 3

ID: T14.G3.01
Topic: T14 – 2D Games
Skill: Move a sprite with arrow keys (4 directions)
Description: Create scripts where pressing each arrow key (up/down/left/right) changes the sprite's x or y position by a consistent amount (e.g., 10 steps). Test that the sprite moves the same distance each time a key is pressed and can move smoothly in all four directions without getting stuck.

Dependencies:
* T14.G2.04: Sequence a safe route
* T01.G3.05: Replace repeated blocks with a repeat loop


ID: T14.G3.02
Topic: T14 – 2D Games
Skill: Move a sprite with keys (2 directions)
Description: Create scripts for platformer/paddle games where only left/right keys control the sprite and ensure speeds match on both sides.

Dependencies:
* T07.G3.02: Trace a script with a simple loop
* T14.G2.04: Sequence a safe route


ID: T14.G3.03
Topic: T14 – 2D Games
Skill: Keep sprite on screen
Description: Add boundary checking logic to prevent the player from leaving the stage. Use `if on edge, bounce` block for simple games or explicit x/y coordinate checks (if x > 240, set x to 240) for precise control. This ensures the player never disappears off-screen.

Dependencies:
* T08.G3.01: Use a simple if in a script


ID: T14.G3.04
Topic: T14 – 2D Games
Skill: Detect touching a goal
Description: Use `touching [Sprite]?` or `touching [Color]?` inside a forever loop to continuously check when the player reaches the goal. When collision is detected, broadcast a 'You Win' message and display a victory sprite or backdrop.

Dependencies:
* T09.G3.01: Create and use a numeric variable for score or count
* T14.G2.03: Recognize level progression


ID: T14.G3.05
Topic: T14 – 2D Games
Skill: Detect touching a hazard
Description: Use collision detection blocks (`touching [Enemy]?` or `touching [red color]?`) inside a forever loop to check when the player touches hazards like spikes or enemies. When detected, reset the player to a safe starting position or checkpoint, or broadcast a 'Hit' message to trigger damage effects.

Dependencies:
* T07.G3.03: Build a forever loop for simple animation
* T08.G3.02: Decide when a single if is enough


ID: T14.G3.06
Topic: T14 – 2D Games
Skill: Create a start screen
Description: Program a "Start" button sprite that hides itself and broadcasts `Start Game` when clicked.

Dependencies:
* T09.G3.02: Use a variable in a conditional (if block)
* T06.G3.06: Trace a project with a single event and predict output


ID: T14.G3.07
Topic: T14 – 2D Games
Skill: Switch to game mode
Description: Program game objects (player, enemies, collectibles) to show and begin their movement scripts only after receiving the `Start Game` broadcast message. This separates the setup phase (where sprites are hidden or idle) from active gameplay.

Dependencies:
* T14.G3.06: Create a start screen
* T06.G3.05: Trace a script with multiple events


ID: T14.G3.08
Topic: T14 – 2D Games
Skill: Trigger Game Over
Description: Broadcast `Game Over` when losing conditions occur (lives reach zero, time runs out). Program all game sprites to stop their scripts and either hide or show a 'Game Over' message when they receive this broadcast.

Dependencies:
* T12.G3.01: Write a comment explaining a complex block
* T08.G3.03: Pick the right conditional block for a scenario


ID: T14.G3.09
Topic: T14 – 2D Games
Skill: Add sound effects to actions
Description: Add sound effect blocks (`play sound [jump]` or `start sound [coin]`) to movement and collision scripts to provide audio feedback when the player jumps, collects items, or gets hit.

Dependencies:
* T09.G3.04: Debug a single missing or wrong variable block
* T07.G3.04: Use repeat-until to reach a simple goal


ID: T14.G3.10
Topic: T14 – 2D Games
Skill: Visual effects on interaction
Description: Use graphic effects (color, brightness, ghost) to show when a player is hit or collects an item.

Dependencies:
* T11.G3.02: Use a pre-made custom block with parameters
* T08.G3.04: Trace code with a single if/else


ID: T14.G3.10.01
Topic: T14 – 2D Games
Skill: Create and delete a single clone
Description: Practice the fundamentals of cloning by creating one clone of a sprite when green flag is clicked, making the clone move or change costume, then deleting it after 3 seconds. This builds understanding of the clone lifecycle before using clones for collectibles or enemies.

Dependencies:
* T14.G3.04: Detect touching a goal
* T07.G3.01: Use a counted repeat loop


ID: T14.G3.11
Topic: T14 – 2D Games
Skill: Create collectible items
Description: Make items (coins, gems, stars) that disappear when the player touches them. Use clones to place multiple collectibles around the level, and delete each clone when touched. This foundational skill prepares for tracking scores and inventory.

Dependencies:
* T14.G3.10.01: Create and delete a single clone
* T14.G3.04: Detect touching a goal
* T07.G3.03: Build a forever loop for simple animation
* T08.G3.01: Use a simple if in a script


---

### GRADE 4

ID: T14.G4.01
Topic: T14 – 2D Games
Skill: Spawn a projectile
Description: Use `create clone of [Bullet]` (or `myself`) to spawn a projectile when a key is pressed or when a timer triggers. Program the projectile to appear at the player's or enemy's current position and point in the correct direction.

Dependencies:
* T14.G3.01: Move a sprite with arrow keys (4 directions)
* T07.G3.01: Use a counted repeat loop
* T08.G3.01: Use a simple if in a script


ID: T14.G4.02
Topic: T14 – 2D Games
Skill: Move a projectile
Description: Program projectile clones to move forward continuously in their current direction until they hit a target (using touching detection) or reach the edge of the screen. Include logic to delete the clone or trigger an effect when collision occurs.

Dependencies:
* T14.G3.01: Move a sprite with arrow keys (4 directions)
* T07.G3.05: Fix a simple repeat loop count


ID: T14.G4.03
Topic: T14 – 2D Games
Skill: Clean up projectiles
Description: Delete clones when they touch an edge/target to prevent lag and bugs.

Dependencies:
* T14.G4.02: Move a projectile
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script


ID: T14.G4.04.01
Topic: T14 – 2D Games
Skill: Enemy patrol movement
Description: Program an enemy to move back and forth between two specific points. Use glide blocks to move between coordinates, or use movement blocks with direction changes. The enemy should reverse direction when reaching each endpoint, creating a predictable patrol pattern.

Dependencies:
* T14.G3.01: Move a sprite with arrow keys (4 directions)
* T07.G3.03: Build a forever loop for simple animation


ID: T14.G4.04.02
Topic: T14 – 2D Games
Skill: Enemy bounce movement
Description: Program an enemy to move continuously in one direction and bounce off the edges of the stage using `if on edge, bounce`. Students should be able to control the enemy's speed and predict where it will be at any time.

Dependencies:
* T14.G3.03: Keep sprite on screen
* T07.G3.03: Build a forever loop for simple animation


ID: T14.G4.05
Topic: T14 – 2D Games
Skill: Chase the player
Description: Use `point towards [Player]` and `move` blocks inside a forever loop to create a chaser enemy. Optionally add an if-statement to reduce movement speed when the distance to the player is less than a threshold, creating more challenging gameplay.

Dependencies:
* T14.G3.01: Move a sprite with arrow keys (4 directions)
* T07.G3.01: Use a counted repeat loop
* T08.G3.01: Use a simple if in a script


ID: T14.G4.06
Topic: T14 – 2D Games
Skill: Create a Score variable
Description: Create a global `Score` variable, initialize it to 0 at game start, and increase it when the player collects items or defeats enemies. Display the score on stage and reset it when the game restarts.

Dependencies:
* T14.G3.11: Create collectible items
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G4.07
Topic: T14 – 2D Games
Skill: Create a Lives variable
Description: Create a `Lives` variable, initialize it to a starting value (like 3), and decrease it when the player touches hazards. Check if lives reach zero to trigger Game Over using an if-statement.

Dependencies:
* T14.G3.08: Trigger Game Over
* T14.G3.05: Detect touching a hazard
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G4.08
Topic: T14 – 2D Games
Skill: Create a Timer
Description: Use a variable and a loop with `wait (1) seconds` to create a countdown that drives win/loss conditions.

Dependencies:
* T14.G3.08: Trigger Game Over
* T07.G3.01: Use a counted repeat loop
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G4.09
Topic: T14 – 2D Games
Skill: Detect level complete
Description: Check if a win condition (Score threshold reached, all coins collected, or touching the exit door) is met to trigger the next level. Use an if-statement inside a forever loop to continuously check the condition.

Dependencies:
* T14.G3.08: Trigger Game Over
* T14.G3.04: Detect touching a goal
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G4.10
Topic: T14 – 2D Games
Skill: Switch backdrops for levels
Description: When `Next Level` message is received, switch the backdrop to represent the new level and reset the player's position to the starting point.

Dependencies:
* T14.G3.01: Move a sprite with arrow keys (4 directions)
* T08.G3.01: Use a simple if in a script


ID: T14.G4.11
Topic: T14 – 2D Games
Skill: Add checkpoints
Description: Store the player's last checkpoint coordinates in variables and restore them after hazards instead of warping all the way back to the start.

Dependencies:
* T14.G3.08: Trigger Game Over
* T14.G3.05: Detect touching a hazard
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G4.12
Topic: T14 – 2D Games
Skill: Temporary power-ups
Description: Give the player a temporary effect (speed boost, shield) by toggling a variable and using a timer to turn it off.

Dependencies:
* T14.G3.01: Move a sprite with arrow keys (4 directions)
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G4.13
Topic: T14 – 2D Games
Skill: Pause and resume the game
Description: Create a Pause button that broadcasts `Pause Game`, stops motion scripts, and resumes when `Resume Game` arrives.

Dependencies:
* T14.G3.08: Trigger Game Over
* T08.G3.01: Use a simple if in a script


ID: T14.G4.14
Topic: T14 – 2D Games
Skill: Reset on restart messages
Description: Use `when I receive [Restart]` (or `Game Over`) to send every sprite back to a known costume, position, and visibility so repeats are consistent.

Dependencies:
* T14.G3.08: Trigger Game Over
* T07.G3.01: Use a counted repeat loop


ID: T14.G4.15
Topic: T14 – 2D Games
Skill: Show damage feedback
Description: When the player takes damage (loses a life), show visual feedback by flashing the sprite (using repeat with ghost effect or color change), playing a hurt sound, and briefly making the player invincible. Use a variable to track invincibility time so the player cannot be hit again immediately.

Dependencies:
* T14.G3.10: Visual effects on interaction
* T14.G4.07: Create a Lives variable
* T14.G3.05: Detect touching a hazard
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script


---

### GRADE 5

ID: T14.G5.01
Topic: T14 – 2D Games
Skill: Configure gravity and weight parameters
Description: Implement simple platformer physics by creating a `y velocity` variable that changes each frame. Add a small negative value (like -0.5 or -1) to simulate gravity pulling the character down. Test different gravity values to see how they affect jump height and fall speed: smaller values create floaty moon-like jumps, larger values create fast snappy movement.

Dependencies:
* T14.G3.01: Move a sprite with arrow keys (4 directions)
* T07.G3.05: Fix a simple repeat loop count


ID: T14.G5.02
Topic: T14 – 2D Games
Skill: Control jump timing
Description: Allow jumping only when the player is touching the ground (or within a short "coyote time") by checking sensors before setting `y velocity`.

Dependencies:
* T14.G4.07: Create a Lives variable
* T14.G5.01: Configure gravity and weight parameters
* T06.G3.02: Build a key-press script that controls a sprite


ID: T14.G5.03
Topic: T14 – 2D Games
Skill: Fix ground collisions
Description: Prevent falling through floors by nudging the sprite up until it is no longer intersecting the ground or by snapping to the floor after a fall.

Dependencies:
* T14.G4.03: Clean up projectiles
* T14.G5.01: Configure gravity and weight parameters


ID: T14.G5.04
Topic: T14 – 2D Games
Skill: Script viewport pans
Description: Use `move viewport to x (XPOS) y (YPOS)` to position the camera at the start of a level or to smoothly slide the view during a non-playable intro sequence before gameplay begins. Students learn to control what the player sees.

Dependencies:
* T14.G4.10: Switch backdrops for levels


ID: T14.G5.05
Topic: T14 – 2D Games
Skill: Lock viewport to the player
Description: Call `lock viewport to sprite [Player]` so the stage follows the player automatically, noting how edges behave when the player reaches the map boundary.

Dependencies:
* T14.G4.10: Switch backdrops for levels


ID: T14.G5.06
Topic: T14 – 2D Games
Skill: Pin HUD to the screen
Description: Use `attach to viewport at x (XPOS) y (YPOS)` to place score, lives, and buttons relative to the viewport so they stay in the same spot even while the world scrolls.

Dependencies:
* T14.G4.10: Switch backdrops for levels


ID: T14.G5.07
Topic: T14 – 2D Games
Skill: Spawn enemies near viewport
Description: Combine `viewport x` and `viewport y` reporters with random offsets to spawn enemies just outside the camera view so they enter smoothly instead of suddenly appearing on top of the player.

Dependencies:
* T14.G4.10: Switch backdrops for levels


ID: T14.G5.08.01
Topic: T14 – 2D Games
Skill: Spawn enemies at timed intervals
Description: Use a repeat loop with wait blocks to spawn a set number of enemies every few seconds. For example, create 5 enemies with a 2-second wait between each spawn. This creates predictable enemy waves.

Dependencies:
* T14.G4.08: Create a Timer
* T14.G4.02: Move a projectile


ID: T14.G5.08.02
Topic: T14 – 2D Games
Skill: Track wave numbers
Description: Create a `Wave` variable that increments each time all enemies in a wave are defeated or when a time period ends. Display the wave number on screen to show player progress.

Dependencies:
* T14.G5.08.01: Spawn enemies at timed intervals
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G5.08.03
Topic: T14 – 2D Games
Skill: Scale difficulty per wave
Description: Use the wave number variable to increase challenge: spawn more enemies, make them faster, or reduce spawn delays as waves increase. For example: `wait (3 - (Wave / 2)) seconds` makes spawns faster each wave.

Dependencies:
* T14.G5.08.02: Track wave numbers


ID: T14.G5.09
Topic: T14 – 2D Games
Skill: High score list
Description: Use a list to store the top scores, insert new scores in sorted order, and display the list in a viewport-attached HUD sprite. Note: CreatiCode also provides built-in `record player score` and `show game leaderboard` blocks for persistent online leaderboards shared across all players.

Dependencies:
* T14.G4.06: Create a Score variable
* T10.G3.01: Loop through and process each item in a list


ID: T14.G5.10
Topic: T14 – 2D Games
Skill: Inventory system
Description: Track collected items ("Key", "Potion") in a list, check membership before allowing actions, and show collected icons near the HUD.

Dependencies:
* T14.G4.12: Temporary power-ups
* T10.G3.01: Loop through and process each item in a list


---

### GRADE 6

ID: T14.G6.01
Topic: T14 – 2D Games
Skill: Character state machine
Description: Create a `State` variable with text values (Idle, Run, Jump, Fall). Use if-statements to check the current state before allowing actions - for example, only allow jumping when State = 'Idle' or 'Run', preventing double-jumps. Change the state variable and costume based on player actions.

Dependencies:
* T14.G4.13: Pause and resume the game
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G6.02
Topic: T14 – 2D Games
Skill: Hitbox separation
Description: Create a simple rectangular sprite (called a 'collision box' or 'hitbox') that is hidden during gameplay. Use this sprite for detecting when the player touches walls or enemies, while a separate art sprite follows it and shows the visual character. This technique makes collision detection more accurate and easier to debug.

Dependencies:
* T14.G5.03: Fix ground collisions
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G6.03
Topic: T14 – 2D Games
Skill: Multi-layer HUD with viewport attachments
Description: Attach multiple sprites to the viewport (score, minimap, buttons) and manage their layering so UI always sits above gameplay while remaining interactive.

Dependencies:
* T14.G5.06: Pin HUD to the screen
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G6.04
Topic: T14 – 2D Games
Skill: Stream level chunks with viewport reporters
Description: Use `viewport x` and `viewport y` to track where the camera is positioned. Write scripts that create new game objects (platforms, enemies) when the camera gets close to them, and delete objects that are far behind the camera. This keeps your game running smoothly even with large levels.

Dependencies:
* T14.G5.04: Script viewport pans
* T14.G5.05: Lock viewport to the player
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G6.05
Topic: T14 – 2D Games
Skill: Cinematic camera rails
Description: Call `detach from viewport`, run scripted `move viewport` sequences for intro/outro scenes, then relock to the player once the cutscene ends.

Dependencies:
* T14.G5.04: Script viewport pans
* T14.G5.05: Lock viewport to the player


ID: T14.G6.06
Topic: T14 – 2D Games
Skill: Mode and pause manager
Description: Maintain a `Game Mode` variable and gate scripts so physics, UI, and spawns only run in the appropriate mode (Play, Pause, Shop, Cutscene).

Dependencies:
* T14.G6.01: Character state machine
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G6.07
Topic: T14 – 2D Games
Skill: Save and load game progress
Description: Use CreatiCode's `store user data key [KEY] value [VALUE]` and `read user data key [KEY]` blocks to save player progress (level reached, items collected, high score) to the cloud. Load this data when the game starts so players can resume where they left off.

Dependencies:
* T14.G4.06: Create a Score variable
* T14.G4.10: Switch backdrops for levels
* T10.G3.01: Loop through and process each item in a list


---

### GRADE 7

ID: T14.G7.01
Topic: T14 – 2D Games
Skill: Spatial partitioning (grid)
Description: Implement movement that snaps to a tile grid (e.g., each move is exactly 32 pixels). Create lists to store which grid positions (x,y coordinates) are occupied by walls or objects. Before moving, check the target grid position in your lists to determine if movement is allowed, enabling puzzle or turn-based RPG logic.

Dependencies:
* T14.G6.04: Stream level chunks with viewport reporters
* T07.G6.05: Fix a loop that runs too many or too few times
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas


ID: T14.G7.02
Topic: T14 – 2D Games
Skill: Basic pathfinding
Description: Create an enemy that moves toward the player using `point towards [Player]`, but when it hits a wall, add logic to try moving in alternative directions (up, down, left, right) until it finds a path around the obstacle. This basic pathfinding prevents enemies from getting stuck on corners.

Dependencies:
* T14.G6.01: Character state machine
* T07.G6.05: Fix a loop that runs too many or too few times
* T08.G5.01: Fix a condition that uses the wrong operator
* T09.G3.01: Create and use a numeric variable for score or count


ID: T14.G7.03
Topic: T14 – 2D Games
Skill: Balanced enemy spawning
Description: Create a list of enemy types with numbers representing how often each should appear (e.g., 'Grunt:70', 'Tank:30'). Write a script that randomly selects from this list, using the numbers to make common enemies appear more often than rare ones. Adjust the ratios as the level increases to change difficulty.

Dependencies:
* T10.G5.01: Store and retrieve named data with a list
* T07.G5.01: Loop over a list or range
* T08.G5.01: Fix a condition that uses the wrong operator
* T09.G3.01: Create and use a numeric variable for score or count
* T14.G5.08.03: Scale difficulty per wave



ID: T14.G7.04
Topic: T14 – 2D Games
Skill: Monitor clone performance
Description: Create a watcher to track how many clones exist at once. Test your game and observe if too many clones make it run slowly. Learn strategies to reduce clone count: reuse clones instead of creating new ones, delete clones that move off-screen, or limit how many can exist at once using a counter variable.

Dependencies:
* T14.G4.01: Spawn a projectile
* T14.G4.03: Clean up projectiles
* T09.G3.01: Create and use a numeric variable for score or count
* T12.G5.01: Explain code changes to a peer



ID: T14.G7.05
Topic: T14 – 2D Games
Skill: Difficulty curves
Description: Store difficulty targets in a list (speed, damage, spawn interval by level) and apply them when the player advances, ensuring ramped but fair gameplay.

Dependencies:
* T10.G5.01: Store and retrieve named data with a list
* T14.G4.09: Detect level complete
* T14.G4.10: Switch backdrops for levels
* T09.G3.01: Create and use a numeric variable for score or count



---

### GRADE 8

ID: T14.G8.01
Topic: T14 – 2D Games
Skill: Modular level loader
Description: Create a system that reads a list of strings or table rows (e.g., "111000111") to generate level layouts via clones.

Dependencies:
* T14.G7.01: Spatial partitioning (grid)
* T06.G6.01: Trace event execution paths in a multi-event program
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas


ID: T14.G8.02
Topic: T14 – 2D Games
Skill: Particle system
Description: Create a flexible particle system (explosions, smoke) where one sprite manages many clones with properties like life, speed, and color.

Dependencies:
* T14.G7.04: Monitor clone performance
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps


ID: T14.G8.03
Topic: T14 – 2D Games
Skill: Component-based entities (Advanced)
Description: Design a flexible entity system where each sprite has a list of component tags (text values like 'CanTakeDamage', 'CanShoot', 'IsShopkeeper'). In your scripts, use if-statements to check if a sprite's list contains specific tags before activating behaviors. For example, only run damage logic if 'CanTakeDamage' is in the list. This enables modular, reusable game objects. (Challenge skill for advanced students)

Dependencies:
* T14.G6.01: Character state machine
* T06.G6.01: Trace event execution paths in a multi-event program
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas


ID: T14.G8.04
Topic: T14 – 2D Games
Skill: Automated gameplay tests
Description: Build a testing system that plays your game automatically using scripted inputs (simulate arrow key presses in sequence). Program it to check if win/lose conditions trigger correctly (e.g., 'Does game end when lives reach 0?'). Use broadcast messages to log what happened during the test and compare it to expected results before releasing your game to players.

Dependencies:
* T14.G7.05: Difficulty curves
* T06.G6.01: Trace event execution paths in a multi-event program
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps


ID: T14.G8.05
Topic: T14 – 2D Games
Skill: Collect game statistics for balancing
Description: Track and store player performance data in lists: how many times they die on each level, how long it takes to win, which power-ups they use most. After testing with multiple players, review this data to identify levels that are too hard or too easy. Adjust difficulty settings (enemy speed, obstacle count, time limits) based on the data to make your game fun and fair.

Dependencies:
* T14.G7.03: Balanced enemy spawning
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps


---

## END OF T14 UPDATED SECTION
