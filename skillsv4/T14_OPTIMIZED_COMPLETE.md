# T14 (2D Games) - Complete Optimized Skills List

## Summary of Changes
- **Original skills**: 66
- **New skills added**: 8 (5 from sub-IDs + 3 standalone)
- **Skills modified**: 23
- **Skills with sub-IDs**: 4 families (8 total sub-skills)
- **Total optimized skills**: 74
- **Dependencies fixed**: 2 X-2 rule violations

---

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


ID: T14.G2.01
Topic: T14 – 2D Games
Skill: Understand turns and rounds
Description: Students look at a turn-based scene with multiple players or timers and determine whose turn it is or what happens next when a turn ends.

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


ID: T14.G3.01.01
Topic: T14 – 2D Games
Skill: Move a sprite left and right with keys
Description: **NEW:** Create scripts where pressing left arrow decreases x position and right arrow increases x position by a fixed amount (e.g., 10 steps). Test that the sprite moves the same distance each time. This simpler 2-direction control prepares students for 4-direction movement.

Dependencies:
* T14.G2.04: Sequence a safe route
* T01.G3.05: Replace repeated blocks with a repeat loop




ID: T14.G3.01.02
Topic: T14 – 2D Games
Skill: Move a sprite with arrow keys (4 directions)
Description: **MODIFIED (from T14.G3.01):** Extend 2-direction movement to add up arrow (increase y) and down arrow (decrease y). Test that the sprite moves smoothly in all four directions without getting stuck at edges.

Dependencies:
* T14.G3.01.01: Move a sprite left and right with keys




ID: T14.G3.02
Topic: T14 – 2D Games
Skill: Move a sprite with keys (2 directions)
Description: Create scripts for platformer/paddle games where only left/right keys control the sprite and ensure speeds match on both sides.

Dependencies:
* T07.G3.02: Trace a script with a simple loop
* T14.G2.04: Sequence a safe route


ID: T14.G3.03
Topic: T14 – 2D Games
Skill: Keep sprite on screen with edge bounce
Description: **MODIFIED:** Add an `if on edge, bounce` block to your movement script so the sprite bounces back when it reaches the stage boundary. Test that the sprite never disappears off-screen.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T14.G3.01.01: Move a sprite left and right with keys




ID: T14.G3.04
Topic: T14 – 2D Games
Skill: Detect touching a goal
Description: Use `touching [Sprite]?` or `touching [Color]?` inside a forever loop to continuously check when the player reaches the goal. When collision is detected, broadcast a 'You Win' message and display a victory sprite or backdrop.

Dependencies:
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T14.G2.03: Recognize level progression


ID: T14.G3.05
Topic: T14 – 2D Games
Skill: Detect touching a hazard
Description: Use collision checks with hazards (spikes, enemies) to reset the player to a safe position or broadcast a warning.

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
Description: Program game objects to show and begin moving only after receiving `Start Game`, separating setup from play.

Dependencies:
* T10.G3.01: Loop through and process each item in a list
* T11.G3.01: Understand when to use custom blocks vs loops
* T14.G3.06: Create a start screen


ID: T14.G3.08
Topic: T14 – 2D Games
Skill: Trigger Game Over
Description: Broadcast `Game Over` when losing conditions occur (lives reach zero, time runs out). Program all game sprites to stop their scripts and either hide or show a 'Game Over' message when they receive this broadcast.

Dependencies:
* T12.G3.01: Write a comment explaining a complex block
* T08.G3.03: Pick the right conditional block for a scenario


ID: T14.G3.09
Topic: T14 – 2D Games
Skill: Add sound effects to movement and collision
Description: **MODIFIED:** Insert `start sound` blocks when the player moves (footstep sounds), jumps (whoosh sound), or touches collectibles (coin sound) to provide audio feedback for key actions.

Dependencies:
* T09.G3.04: Debug a single missing or wrong variable block
* T07.G3.04: Use repeat‑until to reach a simple goal


ID: T14.G3.10
Topic: T14 – 2D Games
Skill: Visual effects on interaction
Description: Use graphic effects (color, brightness, ghost) to show when a player is hit or collects an item.

Dependencies:
* T11.G3.02: Use a pre-made custom block with parameters
* T08.G3.04: Trace code with a single if/else


ID: T14.G3.11
Topic: T14 – 2D Games
Skill: Create collectible items
Description: Make items (coins, gems, stars) that disappear when the player touches them. Use clones to place multiple collectibles around the level, and delete each clone when touched. This foundational skill prepares for tracking scores and inventory.

Dependencies:
* T14.G3.04: Detect touching a goal
* T07.G3.03: Build a forever loop for simple animation
* T08.G3.01: Use a simple if in a script


ID: T14.G3.12
Topic: T14 – 2D Games
Skill: Make sprite jump with a key press
Description: **NEW:** Create a script where pressing the space key changes the sprite's y position upward by a larger amount (e.g., 50 pixels), then use a repeat loop to gradually move it back down. This simple jump mechanic introduces the concept of upward/downward motion before learning physics-based gravity.

Dependencies:
* T14.G3.01.02: Move a sprite with arrow keys (4 directions)
* T07.G3.01: Use a counted repeat loop




ID: T14.G4.01
Topic: T14 – 2D Games
Skill: Spawn a projectile
Description: Use `create clone of [Bullet]` (or `myself`) to spawn a projectile when an input occurs.

Dependencies:
* T14.G3.01.02: Move a sprite with arrow keys (4 directions)
* T06.G3.02: Build a key‑press script that controls a sprite
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G4.02
Topic: T14 – 2D Games
Skill: Move a projectile
Description: Program projectile clones to move forward continuously in their current direction until they hit a target (using touching detection) or reach the edge of the screen. Include logic to trigger an effect when collision occurs.

Dependencies:
* T14.G3.01.02: Move a sprite with arrow keys (4 directions)
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G4.03
Topic: T14 – 2D Games
Skill: Clean up projectiles
Description: Delete clones when they touch an edge or target using `delete this clone` to prevent lag and bugs. Test that old projectiles don't pile up off-screen.

Dependencies:
* T14.G4.02: Move a projectile
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G4.04
Topic: T14 – 2D Games
Skill: Simple enemy patrol movement
Description: **MODIFIED:** Program an enemy to move back and forth horizontally between two x positions (e.g., x=-100 to x=100) using glide blocks or by checking x position and reversing direction. Students should be able to predict where the enemy will be at any given time.

Dependencies:
* T14.G3.01.02: Move a sprite with arrow keys (4 directions)
* T14.G3.03: Keep sprite on screen with edge bounce
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G4.05.01
Topic: T14 – 2D Games
Skill: Point sprite towards a target
Description: **NEW:** Use the `point towards [Sprite]` block to make one sprite always face another sprite (like an arrow pointing at the player). Test that the sprite rotates correctly as the target moves around the stage.

Dependencies:
* T14.G3.01.02: Move a sprite with arrow keys (4 directions)
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count




ID: T14.G4.05.02
Topic: T14 – 2D Games
Skill: Chase the player
Description: **MODIFIED (from T14.G4.05):** Combine `point towards [Player]` and `move` blocks inside a forever loop to create an enemy that chases the player continuously. Test that the enemy follows the player wherever they go.

Dependencies:
* T14.G4.05.01: Point sprite towards a target
* T08.G3.01: Use a simple if in a script




ID: T14.G4.06
Topic: T14 – 2D Games
Skill: Create a Score variable
Description: Create a global `Score` variable, initialize it to 0, and increase it when the player collects items or defeats enemies. Display the score on stage and reset it when the game restarts.

Dependencies:
* T14.G3.11: Create collectible items
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.07
Topic: T14 – 2D Games
Skill: Create a Lives variable
Description: Create a `Lives` variable, decrease it upon damage, and check for zero to trigger Game Over.

Dependencies:
* T14.G3.08: Trigger Game Over
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T08.G3.05: Fix a condition that uses the wrong operator
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.08
Topic: T14 – 2D Games
Skill: Create a Timer
Description: Use a variable and a loop with `wait (1) seconds` to create a countdown that drives win/loss conditions.

Dependencies:
* T14.G3.08: Trigger Game Over
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.01: Use a counted repeat loop
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.09
Topic: T14 – 2D Games
Skill: Detect level complete
Description: Check if a condition (Score threshold, touch door) is met to trigger the next level.

Dependencies:
* T14.G3.08: Trigger Game Over
* T14.G3.04: Detect touching a goal
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T08.G3.05: Fix a condition that uses the wrong operator
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.10
Topic: T14 – 2D Games
Skill: Switch backdrops for levels
Description: When `Next Level` is received, switch the backdrop and reset player position.

Dependencies:
* T14.G3.01.02: Move a sprite with arrow keys (4 directions)
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G4.11
Topic: T14 – 2D Games
Skill: Add checkpoints
Description: Store the player's last checkpoint coordinates in variables and restore them after hazards instead of warping all the way back.

Dependencies:
* T14.G3.08: Trigger Game Over
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T08.G3.05: Fix a condition that uses the wrong operator
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.12
Topic: T14 – 2D Games
Skill: Temporary power-ups
Description: Give the player a temporary effect (speed boost, shield) by toggling a variable and using a timer to turn it off.

Dependencies:
* T14.G3.01.02: Move a sprite with arrow keys (4 directions)
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.13
Topic: T14 – 2D Games
Skill: Pause and resume the game
Description: Create a Pause button that broadcasts `Pause Game`, stops motion scripts, and resumes when `Resume Game` arrives.

Dependencies:
* T14.G3.08: Trigger Game Over
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G4.14
Topic: T14 – 2D Games
Skill: Reset on restart messages
Description: Use `when I receive [Restart]` (or `Game Over`) to send every sprite back to a known costume, position, and visibility so repeats are consistent.

Dependencies:
* T14.G3.08: Trigger Game Over
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.01: Use a counted repeat loop
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G4.15
Topic: T14 – 2D Games
Skill: Show damage feedback
Description: When the player takes damage (loses a life), show visual feedback by flashing the sprite (using repeat with ghost effect or color change), playing a hurt sound, and briefly making the player invincible. Use a variable to track invincibility time so the player cannot be hit again immediately.

Dependencies:
* T14.G3.10: Visual effects on interaction
* T14.G4.07: Create a Lives variable
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.01: Use a simple if in a script


ID: T14.G5.01.01
Topic: T14 – 2D Games
Skill: Understand velocity variables for movement
Description: **NEW:** Create a `y velocity` variable to control how fast a sprite moves up or down. In a forever loop, change the sprite's y position by the velocity value. Test changing the velocity to different positive and negative numbers to see how it affects movement speed and direction.

Dependencies:
* T14.G3.12: Make sprite jump with a key press
* T09.G3.01.04: Display variable value on stage using the variable monitor




ID: T14.G5.01.02
Topic: T14 – 2D Games
Skill: Apply gravity with velocity
Description: **NEW:** Inside a forever loop, decrease the `y velocity` variable by a small constant value (e.g., -0.5) each frame to simulate gravity pulling the sprite down. When the sprite touches the ground, reset velocity to 0 to stop falling.

Dependencies:
* T14.G5.01.01: Understand velocity variables for movement
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator




ID: T14.G5.01.03
Topic: T14 – 2D Games
Skill: Configure gravity and weight parameters
Description: **MODIFIED (from T14.G5.01):** Test different gravity values to see how they affect jump height and fall speed: smaller values (like -0.3) create floaty moon-like jumps, larger values (like -1.5) create fast snappy movement. Find the right balance for your game's feel.

Dependencies:
* T14.G5.01.02: Apply gravity with velocity




ID: T14.G5.02
Topic: T14 – 2D Games
Skill: Control jump timing with ground detection
Description: **MODIFIED:** Allow jumping only when the player is touching the ground color or platform sprite. Use an if-statement to check `touching color [ground]?` before setting `y velocity` to a positive jump value (e.g., 15). This prevents double-jumping in mid-air.

Dependencies:
* T14.G5.01.02: Apply gravity with velocity
* T06.G3.02: Build a key‑press script that controls a sprite
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G5.03
Topic: T14 – 2D Games
Skill: Fix ground collisions
Description: Prevent falling through floors by nudging the sprite up until it is no longer intersecting the ground or by snapping to the floor after a fall.

Dependencies:
* T14.G4.03: Clean up projectiles
* T14.G5.01.02: Apply gravity with velocity
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G5.04
Topic: T14 – 2D Games
Skill: Position viewport at level start
Description: **MODIFIED:** Use `move viewport to x (XPOS) y (YPOS)` at the beginning of each level to center the camera on the starting area. This ensures players see the right part of large maps when the level begins.

Dependencies:
* T14.G4.10: Switch backdrops for levels
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G5.05
Topic: T14 – 2D Games
Skill: Lock viewport to the player
Description: Call `lock viewport to sprite [Player]` so the stage follows the player automatically, noting how edges behave when the player reaches the map boundary.

Dependencies:
* T14.G4.10: Switch backdrops for levels
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G5.06
Topic: T14 – 2D Games
Skill: Pin HUD to the screen
Description: Use `attach to viewport at x (XPOS) y (YPOS)` to place score, lives, and buttons relative to the viewport so they stay in the same spot even while the world scrolls.

Dependencies:
* T14.G4.10: Switch backdrops for levels
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G5.07
Topic: T14 – 2D Games
Skill: Spawn near the viewport
Description: Combine `viewport x`/`viewport y` reporters with random offsets to spawn enemies just outside the camera so they enter smoothly instead of popping on the player.

Dependencies:
* T14.G4.10: Switch backdrops for levels
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G5.08
Topic: T14 – 2D Games
Skill: Timed waves
Description: Use a repeat loop or custom block to spawn a set number of enemies every few seconds (using wait blocks). Track wave numbers in a variable and increase spawn count or enemy speed with each new wave to create escalating difficulty.

Dependencies:
* T14.G4.08: Create a Timer
* T14.G4.02: Move a projectile
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G5.09
Topic: T14 – 2D Games
Skill: High score list
Description: Use a list to store the top scores, insert new scores in order, and display the list in a viewport-attached HUD sprite.

Dependencies:
* T14.G4.06: Create a Score variable
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G5.10
Topic: T14 – 2D Games
Skill: Inventory system
Description: Track collected items ("Key", "Potion") in a list, check membership before allowing actions, and show collected icons near the HUD.

Dependencies:
* T14.G4.12: Temporary power-ups
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G6.01.01
Topic: T14 – 2D Games
Skill: Track game state with a variable
Description: **NEW:** Create a `Game State` variable with values like "Menu", "Playing", and "GameOver". Use if-statements to check the state before running certain scripts - for example, only allow movement when state = "Playing". Change the state when events happen (clicking Start button sets state to "Playing").

Dependencies:
* T14.G4.13: Pause and resume the game
* T09.G3.01.04: Display variable value on stage using the variable monitor




ID: T14.G6.01.02
Topic: T14 – 2D Games
Skill: Character state machine
Description: **MODIFIED (from T14.G6.01):** Create a `Character State` variable with values (Idle, Run, Jump, Fall). Use if-statements to check the current state before allowing actions - for example, only allow jumping when State = 'Idle' or 'Run', preventing double-jumps. Change the state variable and costume based on player actions and physics.

Dependencies:
* T14.G6.01.01: Track game state with a variable
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator




ID: T14.G6.02
Topic: T14 – 2D Games
Skill: Hitbox separation
Description: Create a simple rectangular sprite (called a 'collision box' or 'hitbox') that is hidden during gameplay. Use this sprite for detecting when the player touches walls or enemies, while a separate art sprite follows it and shows the visual character. This technique makes collision detection more accurate and easier to debug.

Dependencies:
* T14.G5.03: Fix ground collisions
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G6.03
Topic: T14 – 2D Games
Skill: Multi-layer HUD with viewport attachments
Description: Attach multiple sprites to the viewport (score, minimap, buttons) and manage their layering so UI always sits above gameplay while remaining interactive.

Dependencies:
* T14.G5.06: Pin HUD to the screen
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G6.04
Topic: T14 – 2D Games
Skill: Stream level chunks with viewport reporters
Description: Use `viewport x` and `viewport y` to track where the camera is positioned. Write scripts that create new game objects (platforms, enemies) when the camera gets close to them, and delete objects that are far behind the camera. This keeps your game running smoothly even with large levels.

Dependencies:
* T14.G5.04: Position viewport at level start
* T14.G5.05: Lock viewport to the player
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G6.05
Topic: T14 – 2D Games
Skill: Cinematic camera rails
Description: Call `detach from viewport`, run scripted `move viewport` sequences for intro/outro scenes, then relock to the player once the cutscene ends.

Dependencies:
* T14.G5.04: Position viewport at level start
* T14.G5.05: Lock viewport to the player
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator


ID: T14.G6.06
Topic: T14 – 2D Games
Skill: Mode and pause manager
Description: Maintain a `Game Mode` variable and gate scripts so physics, UI, and spawns only run in the appropriate mode (Play, Pause, Shop, Cutscene).

Dependencies:
* T14.G6.01.02: Character state machine
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.05: Fix a simple repeat loop count
* T08.G3.05: Fix a condition that uses the wrong operator
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G6.07
Topic: T14 – 2D Games
Skill: Monitor and optimize clone count
Description: **NEW (fixes G7.04 dependency):** Create a variable to count active clones. When creating a clone, increment the counter; when deleting, decrement it. Display this counter and observe during gameplay. If clone count gets too high (e.g., over 50), implement limits: reuse existing clones, delete off-screen clones immediately, or cap maximum spawns.

Dependencies:
* T14.G4.01: Spawn a projectile
* T14.G4.03: Clean up projectiles
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T12.G5.01: Explain code changes to a peer




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
Skill: Basic pathfinding around obstacles
Description: **MODIFIED:** Create an enemy that moves toward the player using `point towards [Player]`, but when it hits a wall, add logic to try moving in alternative directions (up, down, left, right) in sequence until it finds a path that doesn't collide with walls. This basic pathfinding prevents enemies from getting stuck on corners.

Dependencies:
* T14.G6.01.02: Character state machine
* T07.G6.05: Fix a loop that runs too many or too few times
* T08.G5.01: Fix a condition that uses the wrong operator
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G7.03
Topic: T14 – 2D Games
Skill: Balanced enemy spawning
Description: Create a list of enemy types with numbers representing how often each should appear (e.g., 'Grunt:70', 'Tank:30'). Write a script that randomly selects from this list, using the numbers to make common enemies appear more often than rare ones. Adjust the ratios as the level increases to change difficulty.

Dependencies:
* T10.G5.01: Store and retrieve named data with a list
* T07.G5.01: Loop over a list or range
* T08.G5.01: Fix a condition that uses the wrong operator
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T14.G5.08: Timed waves



ID: T14.G7.04
Topic: T14 – 2D Games
Skill: Profile clone performance and implement optimization strategies
Description: **MODIFIED (dependency fixed):** Use the clone counter from G6.07 to track performance during complex gameplay. Test your game with many clones and identify lag points. Learn and apply optimization strategies: object pooling (reusing clones instead of creating new ones), spatial culling (deleting clones far from viewport), and spawn throttling (limiting clones per frame).

Dependencies:
* T14.G6.07: Monitor and optimize clone count
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps




ID: T14.G7.05
Topic: T14 – 2D Games
Skill: Implement difficulty progression curves
Description: **MODIFIED (dependency fixed):** Store difficulty targets in a list (speed, damage, spawn interval by level) and apply them when the player advances. Design a balanced difficulty curve: early levels should be easy to learn, middle levels gradually harder, and late levels challenging but fair. Test and adjust based on player feedback.

Dependencies:
* T10.G5.01: Store and retrieve named data with a list
* T14.G5.08: Timed waves
* T14.G4.09: Detect level complete
* T14.G4.10: Switch backdrops for levels
* T09.G3.01.04: Display variable value on stage using the variable monitor




ID: T14.G7.06
Topic: T14 – 2D Games
Skill: Advanced level management system
Description: **NEW (bridge G5→G7.05):** Create a `Current Level` variable and level configuration list. When level changes, read the configuration for that level (backdrop name, enemy count, timer length) and apply all settings. Implement level unlocking so players must complete Level 1 before accessing Level 2. Save progress using cloud variables or lists.

Dependencies:
* T14.G5.08: Timed waves
* T14.G4.09: Detect level complete
* T14.G4.10: Switch backdrops for levels
* T10.G5.01: Store and retrieve named data with a list
* T09.G3.01.04: Display variable value on stage using the variable monitor




ID: T14.G8.01
Topic: T14 – 2D Games
Skill: Modular level loader
Description: Create a system that reads a list of strings or table rows (e.g., "111000111" where 1=wall, 0=empty) to generate level layouts using clones. Each character in the string creates a specific tile type at the corresponding grid position.

Dependencies:
* T14.G7.01: Spatial partitioning (grid)
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas


ID: T14.G8.02
Topic: T14 – 2D Games
Skill: Particle system
Description: Create a flexible particle system (explosions, smoke) where one sprite manages many short-lived clones, each with properties like lifetime, speed, direction, and color that change over time.

Dependencies:
* T14.G7.04: Profile clone performance and implement optimization strategies
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps


ID: T14.G8.03
Topic: T14 – 2D Games
Skill: Component-based entity system
Description: **MODIFIED:** Design a flexible entity system where each sprite has a list of component tags (text values like 'CanTakeDamage', 'CanShoot', 'IsShopkeeper'). In your scripts, use if-statements to check if a sprite's component list contains specific tags before activating behaviors. For example, only run damage logic if the list contains 'CanTakeDamage'. This modular approach lets you create many different game objects by mixing and matching components.

Dependencies:
* T14.G6.01.02: Character state machine
* T06.G6.01: Trace event execution paths in a multi‑event program
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps
* T09.G6.01: Model real-world quantities using variables and formulas


ID: T14.G8.04
Topic: T14 – 2D Games
Skill: Automated gameplay tests
Description: Build a testing system that plays your game automatically using scripted inputs (simulate arrow key presses in sequence). Program it to check if win/lose conditions trigger correctly (e.g., 'Does game end when lives reach 0?'). Use broadcast messages to log what happened during the test and compare it to expected results before releasing your game to players.

Dependencies:
* T14.G7.05: Implement difficulty progression curves
* T06.G6.01: Trace event execution paths in a multi‑event program
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


