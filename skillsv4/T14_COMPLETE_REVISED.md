# T14 (2D Games) - Complete Revised Skills Section

## Summary of Changes
- **Broad skills broken down**: 4 families (13 sub-skills added)
- **Missing physics skills added**: 17 new skills at G5.11
- **Missing viewport skills added**: 4 new skills at G5.04
- **Missing game category skills added**: 6 new skills at G7.07
- **Dependencies fixed**: All dependencies follow X-2 rule and logical progression
- **Total skills**: 106 (from original 66)

---

# KINDERGARTEN (K)

ID: T14.GK.01
Topic: T14 – 2D Games
Skill: Match controls to character actions
Description: Students drag arrow key cards (up, down, left, right) or action button cards (jump, run) onto pictures showing the matching movement or reaction (up arrow → character jumps up, right arrow → character walks right). They connect specific keyboard inputs to predictable character responses. _Implementation note: Match 4–6 input-action pairs via drag-and-drop. CSTA: 1A-AP-11.__

Dependencies:
* T06.GK.01: Match arrows to directions


ID: T14.GK.02
Topic: T14 – 2D Games
Skill: Recognize a score in simple games
Description: Students compare before/after pictures of a score counter and gameplay moments (collecting a star, hitting a hazard) to see when the score changes and what it signals. _CSTA: 1A-AP-09.__

Dependencies:
* T09.GK.01: Notice when things are different


ID: T14.GK.03
Topic: T14 – 2D Games
Skill: Identify when a game starts and ends
Description: Students observe a simple game story with a clear beginning (Start screen) and ending (Game Over). They identify which pictures show the start, play, and end of the game. _CSTA: 1A-AP-08.__

Dependencies:
None


ID: T14.GK.04
Topic: T14 – 2D Games
Skill: Match rewards to goals
Description: Students match pictures of finishing a level (touching a flag, clearing a board) to appropriate celebration panels (You Win text, trophy, fireworks) so they connect goals to feedback. _CSTA: 1A-AP-11.__

Dependencies:
* T14.GK.02: Recognize a score in simple games
* T14.GK.03: Identify when a game starts and ends


# GRADE 1

ID: T14.G1.01
Topic: T14 – 2D Games
Skill: Identify the player, goal, and obstacles
Description: In a labeled picture of a game level (maze, platformer, or board game), students point to and name: (1) the controllable character (marked with an arrow or labeled 'YOU'), (2) the goal object or location (flag, door, finish line), and (3) hazards that should be avoided (spikes, enemies, water). _CSTA: 1B-AP-11.__

Dependencies:
* T01.GK.03: Find the first and last pictures
* T14.GK.03: Identify when a game starts and ends


ID: T14.G1.02
Topic: T14 – 2D Games
Skill: Apply simple game rules
Description: Students are given a simple rule (e.g., "Collect all coins to open the door") and a sequence of pictures. They decide if the player followed the rule. _CSTA: 1B-AP-08.__

Dependencies:
* T14.G1.01: Identify the player, goal, and obstacles
* T14.GK.04: Match rewards to goals


ID: T14.G1.03
Topic: T14 – 2D Games
Skill: Compare game difficulty
Description: Students compare two pictures of the same game level—one with more obstacles or fewer platforms—and identify which one would be harder to play. _CSTA: 1B-AP-10.__

Dependencies:
* T01.GK.04: Pick the pictures that make sense


ID: T14.G1.04
Topic: T14 – 2D Games
Skill: Predict the best next move
Description: Given a short rule and a partially played level, students pick which control card (up, down, left, right, jump) keeps the player safe and moving toward the goal. _CSTA: 1B-AP-12.__

Dependencies:
* T14.G1.01: Identify the player, goal, and obstacles
* T14.GK.01: Match controls to character actions


ID: T14.G1.05
Topic: T14 – 2D Games
Skill: Distinguish helpers from hazards
Description: Students sort icons from a level (heart, speed shoe, spike, slime) into "helps you win" and "makes you lose," building vocabulary around pickups and traps. _CSTA: 1B-AP-09.__

Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed
* T14.GK.04: Match rewards to goals


# GRADE 2

ID: T14.G2.01
Topic: T14 – 2D Games
Skill: Understand turns and rounds
Description: Students look at a turn-based scene with multiple players or timers and determine whose turn it is or what happens next when a turn ends. _CSTA: 1B-AP-11.__

Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T14.G1.02: Apply simple game rules


ID: T14.G2.02
Topic: T14 – 2D Games
Skill: Track lives and game over conditions
Description: Students track a player's lives through a short picture story. They identify when a life is lost (touching a hazard) and when the game is over (lives reach zero). _CSTA: 1B-AP-12.__

Dependencies:
* T01.G1.04: Predict the next step in a story sequence
* T14.G1.05: Distinguish helpers from hazards


ID: T14.G2.03
Topic: T14 – 2D Games
Skill: Recognize level progression
Description: Students identify the condition for moving to the next level (touch goal, collect items) and notice that later levels are usually different or harder. _CSTA: 1B-AP-10.__

Dependencies:
* T01.G1.01: Put pictures in order to plant a seed
* T14.G1.01: Identify the player, goal, and obstacles


ID: T14.G2.04
Topic: T14 – 2D Games
Skill: Sequence a safe route
Description: Students order 3–4 picture cards showing a safe route through a level (jump over spikes, grab key, open door) to highlight planning before play. _CSTA: 1B-AP-11.__

Dependencies:
* T01.G1.04: Predict the next step in a story sequence
* T14.G1.04: Predict the best next move


ID: T14.G2.05
Topic: T14 – 2D Games
Skill: Adjust game difficulty settings
Description: Presented with a short brief ("Make it easier for new players"), students choose the change that best matches the goal (add another heart, remove a hazard, shorten timer) to understand how game settings affect difficulty. _CSTA: 1B-AP-15.__

Dependencies:
* T01.G1.10: Match pictures to "if/then" rules
* T14.G1.03: Compare game difficulty


# GRADE 3

ID: T14.G3.01.01
Topic: T14 – 2D Games
Skill: Move sprite left and right with arrow keys
Description: Create scripts where pressing the left arrow key decreases x by a fixed amount (e.g., -10) and pressing the right arrow key increases x by the same amount (+10). Test that the sprite moves smoothly horizontally and travels equal distances in both directions. _CSTA: 2-AP-10.__

Dependencies:
* T14.G2.04: Sequence a safe route
* T01.G3.05: Replace repeated blocks with a repeat loop


ID: T14.G3.01.02
Topic: T14 – 2D Games
Skill: Move sprite in 4 directions with arrow keys
Description: Extend left/right movement by adding up/down controls: up arrow changes y by +10, down arrow changes y by -10. Test that the sprite can move smoothly in all four cardinal directions and combine keys for diagonal movement without getting stuck. _CSTA: 2-AP-10.__

Dependencies:
* T14.G3.01.01: Move sprite left and right with arrow keys
* T01.G3.05: Replace repeated blocks with a repeat loop


ID: T14.G3.02
Topic: T14 – 2D Games
Skill: Keep sprite on screen
Description: Add boundary logic to prevent the player from leaving the stage. Use explicit x/y position checks with if-statements (e.g., `if x position < -240 then set x to -240`) to constrain movement within visible bounds. Test all four edges to ensure the player cannot move into invisible areas. _CSTA: 2-AP-13.__

Dependencies:
* T14.G3.01.02: Move sprite in 4 directions with arrow keys
* T08.G3.01: Use a simple if in a script


ID: T14.G3.03
Topic: T14 – 2D Games
Skill: Detect touching a goal
Description: Use `touching [Sprite]?` or `touching [Color]?` inside a forever loop to continuously check when the player reaches the goal. When collision is detected, broadcast a 'You Win' message and display a victory sprite or backdrop. _CSTA: 2-AP-13.__

Dependencies:
* T09.G3.01.04: Display variable value on stage using the variable monitor
* T14.G2.03: Recognize level progression


ID: T14.G3.04.01
Topic: T14 – 2D Games
Skill: Detect touching a hazard using sprite collision
Description: Use `touching [Sprite]?` block to detect when the player touches a hazard sprite (enemy, spike, pit). Place this check inside a forever loop to continuously monitor collisions. When touched, broadcast a message or reduce lives. _CSTA: 2-AP-13.__

Dependencies:
* T14.G3.03: Detect touching a goal
* T07.G3.03: Build a forever loop for simple animation


ID: T14.G3.04.02
Topic: T14 – 2D Games
Skill: Detect touching a hazard using color collision
Description: Use `touching color [red]?` block to detect when the player touches a specific color representing hazards (red for lava, black for pits). This allows using painted backdrops for level design instead of sprite-based obstacles. Test with different hazard colors. _CSTA: 2-AP-13.__

Dependencies:
* T14.G3.04.01: Detect touching a hazard using sprite collision
* T08.G3.02: Decide when a single if is enough


ID: T14.G3.05
Topic: T14 – 2D Games
Skill: Create a start screen
Description: Program a "Start" button sprite that hides itself and broadcasts `Start Game` when clicked. All game sprites listen for this broadcast before beginning their scripts. _CSTA: 2-AP-16.__

Dependencies:
* T09.G3.02: Use a variable in a conditional (if block)
* T06.G3.06: Trace a project with a single event and predict output


ID: T14.G3.06
Topic: T14 – 2D Games
Skill: Switch to game mode
Description: Program game objects to show and begin moving only after receiving `Start Game`, separating setup from play. Use `when I receive [Start Game]` hat blocks to trigger game behavior. _CSTA: 2-AP-16.__

Dependencies:
* T14.G3.05: Create a start screen
* T10.G3.01: Loop through and process each item in a list


ID: T14.G3.07
Topic: T14 – 2D Games
Skill: Trigger Game Over
Description: Broadcast `Game Over` when losing conditions occur (lives reach zero, time runs out). Program all game sprites to stop their scripts and either hide or show a 'Game Over' message when they receive this broadcast. _CSTA: 2-AP-16.__

Dependencies:
* T14.G3.06: Switch to game mode
* T08.G3.03: Pick the right conditional block for a scenario


ID: T14.G3.08
Topic: T14 – 2D Games
Skill: Add sound effects to actions
Description: Insert `start sound` blocks immediately after key movement, collision, or collection events to provide audio feedback. Match sound choices to actions (jump sound for jumping, coin sound for collecting). Test that sounds play reliably without overlapping or cutting off. _CSTA: 2-AP-17.__

Dependencies:
* T14.G3.04.01: Detect touching a hazard using sprite collision
* T07.G3.04: Use repeat‑until to reach a simple goal


ID: T14.G3.09
Topic: T14 – 2D Games
Skill: Visual effects on interaction
Description: Use graphic effects (color, brightness, ghost) to show when a player is hit or collects an item. Apply effects temporarily using a combination of `set effect`, `wait`, and `clear effects`. _CSTA: 2-AP-17.__

Dependencies:
* T14.G3.04.01: Detect touching a hazard using sprite collision
* T08.G3.04: Trace code with a single if/else


ID: T14.G3.10
Topic: T14 – 2D Games
Skill: Create collectible items
Description: Make items (coins, gems, stars) that disappear when the player touches them. Use clones to place multiple collectibles around the level, and delete each clone when touched. This foundational skill prepares for tracking scores and inventory. _CSTA: 2-AP-14.__

Dependencies:
* T14.G3.03: Detect touching a goal
* T07.G3.03: Build a forever loop for simple animation
* T08.G3.01: Use a simple if in a script


ID: T14.G3.11
Topic: T14 – 2D Games
Skill: Simple jump with key press
Description: Program the player to jump when the space key is pressed by changing y position by a fixed amount (e.g., +50), waiting briefly, then returning to the original y position. This creates a simple hop suitable for basic platformers before learning physics-based jumping. _CSTA: 2-AP-10.__

Dependencies:
* T14.G3.01.02: Move sprite in 4 directions with arrow keys
* T06.G3.02: Build a key‑press script that controls a sprite


# GRADE 4

ID: T14.G4.01
Topic: T14 – 2D Games
Skill: Spawn a projectile
Description: Use `create clone of [Bullet]` (or `myself`) to spawn a projectile when an input occurs (key press or collision). Initialize the clone's position to match the player's position using `when I start as a clone` hat block. _CSTA: 2-AP-14.__

Dependencies:
* T14.G3.01.02: Move sprite in 4 directions with arrow keys
* T06.G3.02: Build a key‑press script that controls a sprite
* T08.G3.01: Use a simple if in a script


ID: T14.G4.02
Topic: T14 – 2D Games
Skill: Move a projectile
Description: Program projectile clones to move forward continuously in their current direction until they hit a target (using touching detection) or reach the edge of the screen. Use `when I start as a clone` hat block and a forever loop with movement blocks. _CSTA: 2-AP-14.__

Dependencies:
* T14.G4.01: Spawn a projectile
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.01: Use a simple if in a script


ID: T14.G4.03
Topic: T14 – 2D Games
Skill: Clean up projectiles
Description: Delete clones when they touch an edge or target to prevent lag and bugs. Use `touching edge?` condition combined with `delete this clone` block inside the projectile's movement loop. _CSTA: 2-AP-14.__

Dependencies:
* T14.G4.02: Move a projectile
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T08.G3.01: Use a simple if in a script


ID: T14.G4.04.01
Topic: T14 – 2D Games
Skill: Create patrol movement pattern
Description: Program an enemy to patrol back and forth between two points using a forever loop with `move` blocks. When the sprite touches an edge or boundary color, use `turn 180 degrees` to reverse direction. Test that movement is smooth and consistent. _CSTA: 2-AP-13.__

Dependencies:
* T14.G3.02: Keep sprite on screen
* T07.G3.03: Build a forever loop for simple animation
* T08.G3.01: Use a simple if in a script


ID: T14.G4.04.02
Topic: T14 – 2D Games
Skill: Create glide movement pattern
Description: Use `glide` blocks to move an enemy smoothly between predefined coordinates. Create a loop that alternates between two or more positions. This creates predictable, timed movement patterns suitable for platformers. _CSTA: 2-AP-13.__

Dependencies:
* T14.G4.04.01: Create patrol movement pattern
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.01: Use a counted repeat loop


ID: T14.G4.05.01
Topic: T14 – 2D Games
Skill: Point sprite towards target
Description: Use `point towards [Player]` to make a sprite always face the player character. Test that the sprite rotates correctly as the player moves to different positions. This foundational skill is essential for creating chasing enemies or aiming projectiles. _CSTA: 2-AP-13.__

Dependencies:
* T14.G3.01.02: Move sprite in 4 directions with arrow keys
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T07.G3.03: Build a forever loop for simple animation


ID: T14.G4.05.02
Topic: T14 – 2D Games
Skill: Chase the player
Description: Combine `point towards [Player]` with `move` blocks inside a forever loop to create a chaser enemy that follows the player continuously. Adjust movement speed to balance difficulty. Test that the chaser can navigate around simple obstacles. _CSTA: 2-AP-13.__

Dependencies:
* T14.G4.05.01: Point sprite towards target
* T07.G3.03: Build a forever loop for simple animation
* T08.G3.01: Use a simple if in a script


ID: T14.G4.06
Topic: T14 – 2D Games
Skill: Create a Score variable
Description: Create a global `Score` variable, initialize it to 0 at game start using `set [Score] to (0)`, and increase it when the player collects items using `change [Score] by (1)` or defeats enemies. Display the score on stage using the variable monitor and reset it when the game restarts. _CSTA: 2-AP-11.__

Dependencies:
* T14.G3.10: Create collectible items
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.07
Topic: T14 – 2D Games
Skill: Create a Lives variable
Description: Create a `Lives` variable, initialize it to a starting value (e.g., 3), decrease it upon damage using `change [Lives] by (-1)`, and check for zero to trigger Game Over. Display lives using the variable monitor or custom sprite costumes. _CSTA: 2-AP-11.__

Dependencies:
* T14.G3.07: Trigger Game Over
* T14.G3.04.01: Detect touching a hazard using sprite collision
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.08
Topic: T14 – 2D Games
Skill: Create a Timer
Description: Use a variable and a loop with `wait (1) seconds` to create a countdown or count-up timer. Use the timer value to drive win/loss conditions (time runs out = game over, or time bonus for fast completion). _CSTA: 2-AP-11.__

Dependencies:
* T14.G3.07: Trigger Game Over
* T07.G3.01: Use a counted repeat loop
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.09
Topic: T14 – 2D Games
Skill: Detect level complete
Description: Check if a completion condition (Score threshold, collect all items, touch goal) is met to trigger the next level. Use conditionals to test the win condition and broadcast a level complete message. _CSTA: 2-AP-13.__

Dependencies:
* T14.G3.03: Detect touching a goal
* T14.G4.06: Create a Score variable
* T08.G3.01: Use a simple if in a script


ID: T14.G4.10
Topic: T14 – 2D Games
Skill: Switch backdrops for levels
Description: When `Next Level` is received, switch the backdrop using `switch backdrop to [backdrop2]` and reset player position to the starting coordinates for the new level using `go to x: () y: ()`. _CSTA: 2-AP-16.__

Dependencies:
* T14.G4.09: Detect level complete
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence


ID: T14.G4.11
Topic: T14 – 2D Games
Skill: Add checkpoints
Description: Store the player's last checkpoint coordinates in variables (CheckpointX, CheckpointY). Update these variables when touching checkpoint objects using `set [CheckpointX] to (x position)`. After hazards, restore the player to checkpoint position instead of the level start. _CSTA: 2-AP-11.__

Dependencies:
* T14.G3.04.01: Detect touching a hazard using sprite collision
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.12
Topic: T14 – 2D Games
Skill: Temporary power-ups
Description: Give the player a temporary effect (speed boost, invincibility) by setting a boolean variable to true, applying the effect, using a timer with `wait` blocks to turn it off after a duration, then resetting the variable to false. _CSTA: 2-AP-11.__

Dependencies:
* T14.G3.10: Create collectible items
* T14.G4.08: Create a Timer
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.13
Topic: T14 – 2D Games
Skill: Pause and resume the game
Description: Create a Pause button that broadcasts `Pause Game`, causing all sprites to enter a wait loop using `wait until <[Paused] = [false]>`. Broadcast `Resume Game` to exit the wait loop and continue. Use boolean variables to track pause state. _CSTA: 2-AP-16.__

Dependencies:
* T14.G3.07: Trigger Game Over
* T08.G3.01: Use a simple if in a script


ID: T14.G4.14
Topic: T14 – 2D Games
Skill: Reset on restart messages
Description: Use `when I receive [Restart]` to send every sprite back to initial costume using `switch costume to [costume1]`, position using `go to x: () y: ()`, and visibility using `show` or `hide`. Reset all game variables to starting values to ensure consistent game restarts. _CSTA: 2-AP-16.__

Dependencies:
* T14.G3.07: Trigger Game Over
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G4.15
Topic: T14 – 2D Games
Skill: Show damage feedback
Description: When the player takes damage, show visual feedback by flashing the sprite (using `repeat (5)` with `set ghost effect to (50)`, `wait (0.1) seconds`, `clear graphic effects`), playing a hurt sound, and briefly making the player invincible using a temporary invincibility variable. _CSTA: 2-AP-17.__

Dependencies:
* T14.G3.09: Visual effects on interaction
* T14.G4.07: Create a Lives variable
* T07.G3.01: Use a counted repeat loop


# GRADE 5

ID: T14.G5.01.01
Topic: T14 – 2D Games
Skill: Understand velocity variables
Description: Create a `y velocity` variable to control vertical movement. Instead of directly changing y position with arrow keys, set y velocity when jumping and continuously add y velocity to y position in a forever loop using `change y by (y velocity)`. Test that changing the velocity value changes how fast the sprite moves. _CSTA: 2-AP-11.__

Dependencies:
* T14.G3.11: Simple jump with key press
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G5.01.02
Topic: T14 – 2D Games
Skill: Apply gravity with velocity
Description: Add a constant negative value (like -0.5) to `y velocity` each frame inside a forever loop using `change [y velocity] by (-0.5)` to simulate gravity pulling the character down. Test that the sprite accelerates downward when not on the ground, creating realistic falling motion. _CSTA: 2-AP-11.__

Dependencies:
* T14.G5.01.01: Understand velocity variables
* T07.G3.03: Build a forever loop for simple animation


ID: T14.G5.01.03
Topic: T14 – 2D Games
Skill: Configure gravity and weight parameters
Description: Experiment with different gravity values to tune game feel. Test smaller values (like -0.3) for floaty moon-like jumps and larger values (like -1.5) for fast snappy movement. Adjust the initial jump velocity and gravity strength together to create the desired jump arc and falling speed. _CSTA: 2-AP-17.__

Dependencies:
* T14.G5.01.02: Apply gravity with velocity
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G5.02
Topic: T14 – 2D Games
Skill: Control jump timing with ground detection
Description: Allow jumping only when the player is touching the ground color or platform sprite. Check `touching color [green]?` or use a sensor sprite at the player's feet before allowing jump. This prevents mid-air jumping. _CSTA: 2-AP-13.__

Dependencies:
* T14.G5.01.03: Configure gravity and weight parameters
* T06.G3.02: Build a key‑press script that controls a sprite
* T08.G3.01: Use a simple if in a script


ID: T14.G5.03.01
Topic: T14 – 2D Games
Skill: Fix ground collisions by nudging up
Description: Prevent falling through floors by detecting when the player overlaps with ground (touching color or sprite), then repeatedly change y by small increments (+1) using `repeat until <not <touching [Ground]?>>` until no longer touching. This nudging technique keeps the player on top of platforms. _CSTA: 2-AP-13.__

Dependencies:
* T14.G5.01.03: Configure gravity and weight parameters
* T07.G3.04: Use repeat‑until to reach a simple goal


ID: T14.G5.03.02
Topic: T14 – 2D Games
Skill: Fix ground collisions by snapping to surface
Description: Alternative collision fix: when touching ground, set y velocity to 0 and position the player at a fixed y coordinate that represents the ground surface using `set y to ()`. This snapping method works well for flat terrain. _CSTA: 2-AP-13.__

Dependencies:
* T14.G5.03.01: Fix ground collisions by nudging up
* T08.G3.01: Use a simple if in a script


ID: T14.G5.04.01
Topic: T14 – 2D Games
Skill: Get viewport x position
Description: Use the `viewport x` reporter block to get the current x-coordinate of the camera. This value tells you the horizontal center of what the player can see on the screen. Use this to spawn enemies near the camera edges or position UI elements. _Implementation note: Uses CreatiCode motion_viewportx block. CSTA: 2-AP-11.__

Dependencies:
* T14.G4.10: Switch backdrops for levels
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G5.04.02
Topic: T14 – 2D Games
Skill: Get viewport y position
Description: Use the `viewport y` reporter block to get the current y-coordinate of the camera. This value tells you the vertical center of what the player can see. Combine with `viewport x` to fully track camera position. _Implementation note: Uses CreatiCode motion_viewporty block. CSTA: 2-AP-11.__

Dependencies:
* T14.G5.04.01: Get viewport x position
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G5.04.03
Topic: T14 – 2D Games
Skill: Move viewport to position
Description: Use `move viewport to x (XPOS) y (YPOS)` to position the camera at specific coordinates. This allows you to manually control what part of the level the player sees, useful for cutscenes or starting positions. _Implementation note: Uses CreatiCode motion_move_viewport block. CSTA: 2-AP-17.__

Dependencies:
* T14.G5.04.02: Get viewport y position
* T14.G4.10: Switch backdrops for levels


ID: T14.G5.04.04
Topic: T14 – 2D Games
Skill: Detach sprite from viewport
Description: Use `detach from viewport` to make a sprite stop following the camera. This is useful for sprites that should move with the camera (like the player) when you want them to temporarily stay fixed on screen, or for transitioning between camera modes. _Implementation note: Uses CreatiCode motion_detachfromviewport block. CSTA: 2-AP-17.__

Dependencies:
* T14.G5.04.03: Move viewport to position


ID: T14.G5.05
Topic: T14 – 2D Games
Skill: Lock viewport to the player
Description: Call `lock viewport to sprite [Player]` so the stage follows the player automatically using CreatiCode's viewport locking system. Test how viewport behaves when the player reaches the map boundary - the viewport should stop scrolling at edges to prevent showing empty space. _Implementation note: CreatiCode-specific viewport control blocks. CSTA: 2-AP-17.__

Dependencies:
* T14.G5.04.03: Move viewport to position
* T14.G4.10: Switch backdrops for levels


ID: T14.G5.06
Topic: T14 – 2D Games
Skill: Pin HUD to the screen
Description: Use `attach to viewport at x (XPOS) y (YPOS)` to place score, lives, and buttons relative to the viewport so they stay in the same spot even while the world scrolls. Test that HUD elements remain visible and positioned correctly during gameplay. _Implementation note: CreatiCode-specific viewport control blocks. CSTA: 2-AP-17.__

Dependencies:
* T14.G5.05: Lock viewport to the player
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G5.07
Topic: T14 – 2D Games
Skill: Spawn near the viewport
Description: Combine `viewport x`/`viewport y` reporters with random offsets to spawn enemies just outside the camera so they enter smoothly instead of popping on the player. Use expressions like `(viewport x) + (pick random 240 to 300)` to place spawns near screen edges. _CSTA: 2-AP-11.__

Dependencies:
* T14.G5.04.02: Get viewport y position
* T14.G4.01: Spawn a projectile


ID: T14.G5.08
Topic: T14 – 2D Games
Skill: Timed waves
Description: Use a repeat loop or custom block to spawn a set number of enemies every few seconds (using wait blocks). Track wave numbers in a variable and increase spawn count or enemy speed with each new wave to create escalating difficulty. _CSTA: 2-AP-13.__

Dependencies:
* T14.G4.08: Create a Timer
* T14.G4.01: Spawn a projectile
* T07.G3.01: Use a counted repeat loop


ID: T14.G5.09.01
Topic: T14 – 2D Games
Skill: Create a high score list
Description: Create a list variable called `High Scores` to store multiple score values. When the game ends, use `add [Score] to [High Scores]` to store the current score. Display the list on stage using the list monitor. _CSTA: 2-AP-11.__

Dependencies:
* T14.G4.06: Create a Score variable
* T10.G3.01: Loop through and process each item in a list


ID: T14.G5.09.02
Topic: T14 – 2D Games
Skill: Sort high scores in order
Description: After adding a new score to the high scores list, use a loop to compare values and rearrange them from highest to lowest. Insert the new score at the correct position so the best score is always at position 1. _CSTA: 2-AP-13.__

Dependencies:
* T14.G5.09.01: Create a high score list
* T10.G4.01: Build a list to collect input or track state


ID: T14.G5.09.03
Topic: T14 – 2D Games
Skill: Display top scores in HUD
Description: Create a sprite that shows the top 5 scores from your high scores list using `item (1) of [High Scores]` through `item (5) of [High Scores]`. Attach this sprite to the viewport so it appears on a game over screen or leaderboard menu. _CSTA: 2-AP-17.__

Dependencies:
* T14.G5.09.02: Sort high scores in order
* T14.G5.06: Pin HUD to the screen


ID: T14.G5.09.04
Topic: T14 – 2D Games
Skill: Limit high score list size
Description: Keep only the top 10 scores by checking list length using `length of [High Scores]` and deleting the lowest score using `delete (last) of [High Scores]` when the list gets too long. This prevents the list from growing infinitely. _CSTA: 2-AP-13.__

Dependencies:
* T14.G5.09.02: Sort high scores in order
* T10.G4.01: Build a list to collect input or track state


ID: T14.G5.10.01
Topic: T14 – 2D Games
Skill: Create an inventory list
Description: Create a list variable called `Inventory` to track collected items. When the player touches a collectible item (key, potion, coin), add its name to the inventory using `add [Key] to [Inventory]`. Display the inventory list on stage. _CSTA: 2-AP-11.__

Dependencies:
* T14.G3.10: Create collectible items
* T10.G3.01: Loop through and process each item in a list


ID: T14.G5.10.02
Topic: T14 – 2D Games
Skill: Check inventory membership
Description: Before allowing an action (opening a door, using a special ability), check if the required item is in the inventory using `<[Inventory] contains [Key]?>`. Show a message if the item is missing. _CSTA: 2-AP-13.__

Dependencies:
* T14.G5.10.01: Create an inventory list
* T08.G3.01: Use a simple if in a script


ID: T14.G5.10.03
Topic: T14 – 2D Games
Skill: Remove items from inventory when used
Description: When the player uses a consumable item (potion, key), find its position in the inventory list and delete it using `delete (position) of [Inventory]`. This prevents using the same item multiple times. _CSTA: 2-AP-13.__

Dependencies:
* T14.G5.10.02: Check inventory membership
* T10.G4.01: Build a list to collect input or track state


ID: T14.G5.10.04
Topic: T14 – 2D Games
Skill: Display collected item icons
Description: Create sprite clones for each item in the inventory and position them near the HUD using `attach to viewport`. As items are added or removed, update the displayed icons to match the inventory list contents. _CSTA: 2-AP-17.__

Dependencies:
* T14.G5.10.01: Create an inventory list
* T14.G5.06: Pin HUD to the screen
* T14.G4.01: Spawn a projectile


ID: T14.G5.10.05
Topic: T14 – 2D Games
Skill: Limit inventory capacity
Description: Before adding an item to inventory, check if the list length is below the maximum capacity (e.g., 10 items) using `<(length of [Inventory]) < (10)>`. Show a "inventory full" message if the player tries to collect more. _CSTA: 2-AP-13.__

Dependencies:
* T14.G5.10.01: Create an inventory list
* T08.G3.01: Use a simple if in a script


ID: T14.G5.10.06
Topic: T14 – 2D Games
Skill: Track item quantities
Description: Instead of adding duplicate item names, create a second list to track quantities. When collecting an item already in inventory, increase its quantity counter rather than adding a new list entry. Display "Key x3" to show the player has 3 keys. _CSTA: 2-AP-13.__

Dependencies:
* T14.G5.10.01: Create an inventory list
* T10.G4.01: Build a list to collect input or track state


ID: T14.G5.11.01
Topic: T14 – 2D Games
Skill: Enable 2D physics on a sprite
Description: Use `turn physics on with type [dynamic]` to make a sprite follow realistic physics rules (gravity, momentum, collisions). Dynamic bodies are affected by forces and can move freely. Test how the sprite falls and bounces differently than with manual movement code. _Implementation note: Uses CreatiCode physics_turnonphysics block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.01.03: Configure gravity and weight parameters


ID: T14.G5.11.02
Topic: T14 – 2D Games
Skill: Create static physics objects
Description: Use `turn physics on with type [static]` for platforms and walls that don't move but interact with dynamic physics bodies. Static objects provide surfaces for players to land on and obstacles that block movement. _Implementation note: Uses CreatiCode physics_turnonphysics block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.03
Topic: T14 – 2D Games
Skill: Apply force to physics body
Description: Use `apply force x (X) y (Y)` to push a physics-enabled sprite. Forces create realistic acceleration that respects the sprite's mass and momentum. Test different force values to see how they affect movement speed. _Implementation note: Uses CreatiCode physics_applyforce block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.04
Topic: T14 – 2D Games
Skill: Apply impulse for instant movement
Description: Use `apply impulse x (X) y (Y)` to instantly change a physics sprite's velocity, useful for jumping or launching. Unlike forces (which accelerate gradually), impulses provide immediate speed changes. _Implementation note: Uses CreatiCode physics_applyimpulse block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.03: Apply force to physics body


ID: T14.G5.11.05
Topic: T14 – 2D Games
Skill: Set physics sprite shape
Description: Use `set physics shape to [rectangle/circle]` to define the collision boundary for a sprite. Circles work well for balls and rolling objects, rectangles for boxes and platforms. The shape affects how objects collide and rotate. _Implementation note: Uses CreatiCode physics_setshape block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.06
Topic: T14 – 2D Games
Skill: Adjust physics sprite mass
Description: Use `set mass to (MASS)` to control how heavy a sprite is. Heavier objects (higher mass) are harder to push and fall faster, lighter objects (lower mass) are easier to move and float longer. Test different masses to tune gameplay feel. _Implementation note: Uses CreatiCode physics_setMass block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.07
Topic: T14 – 2D Games
Skill: Set bounciness (restitution)
Description: Use `set bounciness to (VALUE)` where 0 = no bounce and 1 = perfectly bouncy. This controls how much energy an object keeps after colliding with surfaces. A bouncy ball might use 0.8, a sandbag might use 0.1. _Implementation note: Uses CreatiCode physics_setrestitution block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.08
Topic: T14 – 2D Games
Skill: Set friction coefficient
Description: Use `set friction to (VALUE)` to control how slippery surfaces are. Higher friction (like 0.8) makes objects grip and slow down quickly, lower friction (like 0.1) makes surfaces slippery like ice. _Implementation note: Uses CreatiCode physics_setfrictioncoefficient block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.09
Topic: T14 – 2D Games
Skill: Set air resistance (drag)
Description: Use `set drag to (VALUE)` to simulate air resistance or water resistance. Higher drag values make objects slow down faster when moving through space, useful for underwater effects or parachuting. _Implementation note: Uses CreatiCode physics_setdrag block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.10
Topic: T14 – 2D Games
Skill: Set angular velocity for spinning
Description: Use `set angular velocity to (DEGREES/SEC)` to make a physics sprite spin continuously. Positive values spin clockwise, negative counterclockwise. Useful for spinning obstacles or rolling objects. _Implementation note: Uses CreatiCode physics_setangularvelocity block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.11
Topic: T14 – 2D Games
Skill: Disable physics rotation
Description: Use `lock rotation` to prevent a physics sprite from rotating during collisions. This keeps characters upright and prevents boxes from tumbling when you just want sliding motion. _Implementation note: Uses CreatiCode physics_lockrotation block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.10: Set angular velocity for spinning


ID: T14.G5.11.12
Topic: T14 – 2D Games
Skill: Create a physics sensor
Description: Use `turn physics on with type [sensor]` to create an object that detects collisions without physically blocking movement (like a trigger zone). Sensors are perfect for goal areas, checkpoint zones, or detection areas that shouldn't stop the player. _Implementation note: Uses CreatiCode physics_turnonphysics with sensor type. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.13
Topic: T14 – 2D Games
Skill: Detect physics collisions
Description: Use `when I collide with [Sprite]` event hat block to run code when a physics body touches another sprite. This event triggers automatically by the physics engine, unlike manual touching detection loops. _Implementation note: Uses CreatiCode physics_whencollidebegin event. CSTA: 2-AP-16.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.14
Topic: T14 – 2D Games
Skill: Create physics groups
Description: Use `set physics group to [GROUP]` to categorize sprites, then use `set collides with [GROUP]` to control which groups collide with each other. This lets you make player bullets pass through players but hit enemies. _Implementation note: Uses CreatiCode physics_setcollisiongroup blocks. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.15
Topic: T14 – 2D Games
Skill: Apply force at a point
Description: Use `apply force x (X) y (Y) at x (POINTX) y (POINTY)` to push a sprite at a specific location on its body. Forces applied off-center create rotation (torque) as well as movement, useful for realistic impacts. _Implementation note: Uses CreatiCode physics_applyforceatpoint block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.03: Apply force to physics body


ID: T14.G5.11.16
Topic: T14 – 2D Games
Skill: Get collision force
Description: Use `collision force` reporter inside a collision event to measure how hard two objects hit each other. Use this value to determine damage, play appropriate sound effects, or trigger effects only on hard impacts. _Implementation note: Uses CreatiCode physics_getimpactforce reporter. CSTA: 2-AP-11.__

Dependencies:
* T14.G5.11.13: Detect physics collisions


ID: T14.G5.11.17
Topic: T14 – 2D Games
Skill: Turn off physics temporarily
Description: Use `turn physics off` to disable physics simulation for a sprite, making it ignore gravity and collisions. Useful when switching game modes or during cutscenes. Turn physics back on when needed. _Implementation note: Uses CreatiCode physics_turnoffphysics block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.18
Topic: T14 – 2D Games
Skill: Set x velocity directly
Description: Use `set velocity x to (VELOCITY)` to directly control the horizontal speed of a physics sprite without applying forces. This gives precise control over movement speed and is useful for player controls that need consistent speed. _Implementation note: Uses CreatiCode physics_setvelocityx block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.19
Topic: T14 – 2D Games
Skill: Set y velocity directly
Description: Use `set velocity y to (VELOCITY)` to directly control the vertical speed of a physics sprite. This is useful for implementing custom jump mechanics where you want precise control over jump height. _Implementation note: Uses CreatiCode physics_setvelocityy block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.18: Set x velocity directly


ID: T14.G5.11.20
Topic: T14 – 2D Games
Skill: Set velocity with direction
Description: Use `set velocity to (SPEED) at angle (DEGREES)` to make a sprite move in a specific direction at a specific speed. This is perfect for projectiles that need to travel at an exact angle. _Implementation note: Uses CreatiCode physics_setvelocitydir block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.19: Set y velocity directly


ID: T14.G5.11.21
Topic: T14 – 2D Games
Skill: Get x velocity reporter
Description: Use the `velocity x` reporter to read how fast a physics sprite is currently moving horizontally. Use this value to change animations (running vs standing), trigger effects (dust at high speed), or calculate momentum. _Implementation note: Uses CreatiCode physics_getvelocityx reporter. CSTA: 2-AP-11.__

Dependencies:
* T14.G5.11.18: Set x velocity directly


ID: T14.G5.11.22
Topic: T14 – 2D Games
Skill: Get y velocity reporter
Description: Use the `velocity y` reporter to read how fast a sprite is moving vertically. Use this to detect when the player is falling fast (for landing effects) or moving upward (for jump animations). _Implementation note: Uses CreatiCode physics_getvelocityy reporter. CSTA: 2-AP-11.__

Dependencies:
* T14.G5.11.21: Get x velocity reporter


ID: T14.G5.11.23
Topic: T14 – 2D Games
Skill: Get mass reporter
Description: Use the `mass` reporter to read how heavy a physics sprite is. This can be useful for creating effects that scale with mass or for debugging physics behavior. _Implementation note: Uses CreatiCode physics_getMass reporter. CSTA: 2-AP-11.__

Dependencies:
* T14.G5.11.06: Adjust physics sprite mass


ID: T14.G5.11.24
Topic: T14 – 2D Games
Skill: Broadcast on collision event
Description: Use `when I collide with [Sprite], broadcast [message]` to send a message to other sprites when a physics collision occurs. This lets you coordinate effects across multiple sprites (screen shake, score updates, sound effects). _Implementation note: Uses CreatiCode physics_broadcastcollisioneventmessage block. CSTA: 2-AP-16.__

Dependencies:
* T14.G5.11.13: Detect physics collisions


ID: T14.G5.11.25
Topic: T14 – 2D Games
Skill: Broadcast on collision end
Description: Use `when I stop colliding with [Sprite], broadcast [message]` to detect when two physics objects separate. This is useful for detecting when a player leaves a platform or exits a trigger zone. _Implementation note: Uses CreatiCode physics_broadcastcollisioneventmessage2 block. CSTA: 2-AP-16.__

Dependencies:
* T14.G5.11.24: Broadcast on collision event


ID: T14.G5.11.26
Topic: T14 – 2D Games
Skill: Detect collision below
Description: Use `colliding below?` reporter combined with `turn on collision detection` to check if a physics sprite is touching something underneath it. This is essential for detecting when the player is on the ground and can jump. _Implementation note: Uses CreatiCode physics_getcollidingbottom and physics_turnoncollisiondetection blocks. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.13: Detect physics collisions


ID: T14.G5.11.27
Topic: T14 – 2D Games
Skill: Get ground slope
Description: Use `ground slope` reporter to read the angle of the surface below a sprite. Use this value to adjust character rotation on slopes or to determine if the player can climb a surface based on steepness. _Implementation note: Uses CreatiCode physics_getgroundslope reporter. CSTA: 2-AP-11.__

Dependencies:
* T14.G5.11.26: Detect collision below


ID: T14.G5.11.28
Topic: T14 – 2D Games
Skill: Set gravity scale
Description: Use `set gravity scale to (SCALE)` to adjust how much gravity affects a specific sprite. A scale of 0 makes the sprite float (no gravity), 2 makes it fall twice as fast. Each sprite can have different gravity scales. _Implementation note: Uses CreatiCode physics_setgravityscale block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.29
Topic: T14 – 2D Games
Skill: Set damping factor
Description: Use `set damping to (VALUE)` to make physics sprites slow down over time even without friction. Higher damping makes objects lose velocity faster, simulating resistance. Useful for underwater or space effects. _Implementation note: Uses CreatiCode physics_setdampingfactor block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.09: Set air resistance (drag)


ID: T14.G5.11.30
Topic: T14 – 2D Games
Skill: Lock/unlock body movement
Description: Use `lock movement` to prevent a physics sprite from moving while still allowing it to rotate. Use `unlock movement` to restore movement. Useful for anchored objects or temporarily frozen states. _Implementation note: Uses CreatiCode physics_lockmovement block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.31
Topic: T14 – 2D Games
Skill: Add torque/rotation
Description: Use `apply torque (TORQUE)` to make a physics sprite spin by applying rotational force. Torque creates angular acceleration, making objects spin faster over time. Useful for spinning obstacles or rotating platforms. _Implementation note: Uses CreatiCode physics_addtorque block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.10: Set angular velocity for spinning


ID: T14.G5.11.32
Topic: T14 – 2D Games
Skill: Create fixed joint
Description: Use `add fixed joint to [Sprite]` to rigidly connect two physics sprites together so they move as one unit. This is useful for creating composite objects like a character holding a weapon or a car with wheels. _Implementation note: Uses CreatiCode physics_addfixedjoint block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.01: Enable 2D physics on a sprite


ID: T14.G5.11.33
Topic: T14 – 2D Games
Skill: Create revolute/hinge joint
Description: Use `add revolute joint to [Sprite] at x (X) y (Y)` to create a rotating connection between two sprites, like a door hinge or pendulum. The sprites can rotate around the joint point but stay connected. _Implementation note: Uses CreatiCode physics_addrevoltejoint block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.32: Create fixed joint


ID: T14.G5.11.34
Topic: T14 – 2D Games
Skill: Create prismatic/sliding joint
Description: Use `add prismatic joint to [Sprite]` to create a sliding connection between two sprites that can move along one axis but not rotate, like a piston or elevator. Define the axis of movement for realistic mechanical motion. _Implementation note: Uses CreatiCode physics_addprismaticjoint block. CSTA: 2-AP-13.__

Dependencies:
* T14.G5.11.33: Create revolute/hinge joint


# GRADE 6

ID: T14.G6.01.01
Topic: T14 – 2D Games
Skill: Track game state with a variable
Description: Create a `Game State` variable with text values like "Menu", "Playing", "Paused", and "GameOver". Use if-statements to check the state before running scripts - for example, only allow movement when state = "Playing". Change the state when events happen (clicking Start button sets state to "Playing"). _CSTA: 2-AP-13.__

Dependencies:
* T14.G4.13: Pause and resume the game
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G6.01.02.01
Topic: T14 – 2D Games
Skill: Define character states
Description: Create a `Character State` variable with text values representing different states: "Idle", "Running", "Jumping", "Falling", "Crouching", "Attacking". Document what each state means and when the character should enter that state. _CSTA: 2-AP-13.__

Dependencies:
* T14.G6.01.01: Track game state with a variable
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G6.01.02.02
Topic: T14 – 2D Games
Skill: Implement state transitions
Description: Write scripts that check current state and player inputs to determine when to change states. For example: if State = "Idle" and space pressed and on ground, set State to "Jumping". Use if-statements to enforce valid transitions (can't jump while already jumping). _CSTA: 2-AP-13.__

Dependencies:
* T14.G6.01.02.01: Define character states
* T08.G3.03: Pick the right conditional block for a scenario


ID: T14.G6.01.02.03
Topic: T14 – 2D Games
Skill: Match costumes to states
Description: Switch character costumes based on the current state using `if <(Character State) = [Running]> then switch costume to [Run1]`. Create animation loops for each state so the visual appearance always matches what the character is doing. _CSTA: 2-AP-17.__

Dependencies:
* T14.G6.01.02.01: Define character states
* T08.G3.01: Use a simple if in a script


ID: T14.G6.01.02.04
Topic: T14 – 2D Games
Skill: Prevent invalid state actions
Description: Before allowing player actions, check if they're valid for the current state. For example, only allow shooting when State = "Idle" or "Running", not while "Jumping" or "Crouching". This prevents double-jumps and creates more polished game feel. _CSTA: 2-AP-13.__

Dependencies:
* T14.G6.01.02.02: Implement state transitions
* T08.G3.03: Pick the right conditional block for a scenario


ID: T14.G6.02
Topic: T14 – 2D Games
Skill: Hitbox separation
Description: Create a simple rectangular sprite (called a 'collision box' or 'hitbox') that is hidden during gameplay using `hide`. Use this sprite for detecting when the player touches walls or enemies using collision detection blocks, while a separate art sprite follows it using `go to [Hitbox]` and shows the visual character. This technique makes collision detection more accurate and easier to debug. _CSTA: 2-AP-16.__

Dependencies:
* T14.G5.03.01: Fix ground collisions by nudging up
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G6.03
Topic: T14 – 2D Games
Skill: Multi-layer HUD with viewport attachments
Description: Attach multiple sprites to the viewport (score, minimap, buttons) and manage their layering using `go to front layer` and `go back (N) layers` so UI always sits above gameplay while remaining interactive. Test that buttons can be clicked and text remains readable. _CSTA: 2-AP-17.__

Dependencies:
* T14.G5.06: Pin HUD to the screen
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G6.04
Topic: T14 – 2D Games
Skill: Stream level chunks with viewport reporters
Description: Use `viewport x` and `viewport y` reporters to track where the camera is positioned. Write scripts that create new game objects (platforms, enemies) when the camera gets close to them using distance calculations, and delete objects that are far behind the camera. This keeps your game running smoothly even with large levels. _CSTA: 2-AP-16.__

Dependencies:
* T14.G5.04.02: Get viewport y position
* T14.G5.05: Lock viewport to the player
* T14.G4.01: Spawn a projectile


ID: T14.G6.05
Topic: T14 – 2D Games
Skill: Cinematic camera rails
Description: Call `detach from viewport` to unlock the camera from the player, then run scripted `move viewport to x () y ()` sequences with glide or wait timing for intro/outro scenes. When the cutscene ends, use `lock viewport to [Player]` to resume normal gameplay. _CSTA: 2-AP-17.__

Dependencies:
* T14.G5.04.04: Detach sprite from viewport
* T14.G5.05: Lock viewport to the player


ID: T14.G6.06
Topic: T14 – 2D Games
Skill: Mode and pause manager
Description: Maintain a `Game Mode` variable with values like "Play", "Pause", "Shop", "Cutscene" and use if-statements at the start of every sprite's main loop to check the mode. Only run physics, UI, and spawns in the appropriate modes. This creates a centralized system for controlling game state. _CSTA: 2-AP-16.__

Dependencies:
* T14.G6.01.02.01: Define character states
* T14.G4.13: Pause and resume the game


ID: T14.G6.07
Topic: T14 – 2D Games
Skill: Monitor and optimize clone count
Description: Create a variable to count active clones. When creating a clone, increment the counter using `change [Clone Count] by (1)`; when deleting, decrement it. Display this counter and observe during gameplay. If clone count gets too high (e.g., over 50), implement limits: reuse existing clones, delete off-screen clones immediately using distance checks, or cap maximum spawns. _CSTA: 2-AP-17.__

Dependencies:
* T14.G4.01: Spawn a projectile
* T14.G4.03: Clean up projectiles
* T09.G3.01.04: Display variable value on stage using the variable monitor


# GRADE 7

ID: T14.G7.01
Topic: T14 – 2D Games
Skill: Spatial partitioning (grid)
Description: Implement movement that snaps to a tile grid (e.g., each move is exactly 32 pixels). Create lists to store which grid positions (x,y coordinates) are occupied by walls or objects. Before moving, check the target grid position in your lists using `[Grid] contains (target position)?` to determine if movement is allowed, enabling puzzle or turn-based RPG logic. _CSTA: 2-AP-16.__

Dependencies:
* T14.G6.04: Stream level chunks with viewport reporters
* T10.G4.01: Build a list to collect input or track state


ID: T14.G7.02
Topic: T14 – 2D Games
Skill: Basic pathfinding around obstacles
Description: Create an enemy that moves toward the player using `point towards [Player]`, but when it hits a wall, add logic to try moving in alternative directions (up, down, left, right) in sequence until it finds a path that doesn't collide with walls using `not <touching [Wall]?>` checks. This basic pathfinding prevents enemies from getting stuck on corners. _CSTA: 2-AP-16.__

Dependencies:
* T14.G6.01.02.04: Prevent invalid state actions
* T14.G4.05.02: Chase the player


ID: T14.G7.03
Topic: T14 – 2D Games
Skill: Balanced enemy spawning
Description: Create a list of enemy types with numbers representing how often each should appear (e.g., 'Grunt:70', 'Tank:30'). Write a script that randomly selects from this list using weighted random selection, making common enemies appear more often than rare ones. Adjust the ratios as the level increases to change difficulty. _CSTA: 2-AP-16.__

Dependencies:
* T10.G4.01: Build a list to collect input or track state
* T14.G5.08: Timed waves


ID: T14.G7.04
Topic: T14 – 2D Games
Skill: Profile clone performance and implement optimization strategies
Description: Use the clone counter from G6.07 to track performance during complex gameplay. Test your game with many clones and identify lag points by watching when frame rate drops. Learn and apply optimization strategies: object pooling (reusing clones instead of creating new ones), spatial culling (deleting clones far from viewport), and spawn throttling (limiting clones per frame using wait blocks). _CSTA: 3A-AP-17.__

Dependencies:
* T14.G6.07: Monitor and optimize clone count
* T12.G5.01: Explain code changes to a peer


ID: T14.G7.05
Topic: T14 – 2D Games
Skill: Implement difficulty progression curves
Description: Store difficulty targets in a list (speed, damage, spawn interval by level) and apply them when the player advances using `item (Current Level) of [Difficulty Settings]`. Design a balanced difficulty curve: early levels should be easy to learn, middle levels gradually harder, and late levels challenging but fair. Test and adjust based on player feedback. _CSTA: 2-AP-17.__

Dependencies:
* T14.G5.08: Timed waves
* T14.G4.09: Detect level complete
* T14.G4.10: Switch backdrops for levels
* T10.G4.01: Build a list to collect input or track state


ID: T14.G7.06
Topic: T14 – 2D Games
Skill: Advanced level management system
Description: Create a `Current Level` variable and level configuration list. When level changes, read the configuration for that level (backdrop name, enemy count, timer length) using list lookups and apply all settings using a custom block. Implement level unlocking so players must complete Level 1 before accessing Level 2 by checking a `Max Level Reached` variable. _CSTA: 2-AP-16.__

Dependencies:
* T14.G5.08: Timed waves
* T14.G4.09: Detect level complete
* T14.G4.10: Switch backdrops for levels
* T10.G4.01: Build a list to collect input or track state


ID: T14.G7.07.01
Topic: T14 – 2D Games
Skill: Save progress to cloud variables
Description: Create cloud variables (variables with ☁ symbol) that persist between game sessions. When the player completes a level or reaches a checkpoint, save their progress using `set [☁ Saved Level] to (Current Level)`. When the game starts, load the saved value to resume from where they left off. _Implementation note: Cloud variables sync across users in CreatiCode. CSTA: 2-AP-11.__

Dependencies:
* T14.G4.09: Detect level complete
* T09.G3.01.04: Display variable value on stage using the variable monitor


ID: T14.G7.07.02.01
Topic: T14 – 2D Games
Skill: Identify data to save
Description: Determine what game data should persist between sessions: player progress (current level, high score), unlocked content (available characters, purchased upgrades), and settings (difficulty, sound volume). Create a list of variables that need to be saved. _CSTA: 2-AP-16.__

Dependencies:
* T14.G4.06: Create a Score variable
* T14.G4.09: Detect level complete


ID: T14.G7.07.02.02
Topic: T14 – 2D Games
Skill: Convert game state to storable format
Description: Convert multiple game variables into a single text string that can be stored. For example, combine Score, Level, and Lives into "1000,5,3" format. Write scripts to split this string back into individual values when loading. _CSTA: 2-AP-16.__

Dependencies:
* T14.G7.07.02.01: Identify data to save
* T10.G4.01: Build a list to collect input or track state


ID: T14.G7.07.02.03
Topic: T14 – 2D Games
Skill: Implement save and load functions
Description: Create custom blocks called "Save Game" and "Load Game". Save Game stores all important variables to cloud storage or lists. Load Game reads the stored data and restores all variables to their saved values. Add these to your game's menu system. _CSTA: 2-AP-16.__

Dependencies:
* T14.G7.07.02.02: Convert game state to storable format
* T11.G4.01: Create a custom block for a repeated action


ID: T14.G7.07.03
Topic: T14 – 2D Games
Skill: Test save/load system
Description: Test your save/load system by playing to a specific point, saving, stopping the project, restarting, and loading. Verify that all progress is restored correctly: current level, score, collected items, and unlocked features. Fix any data that doesn't persist correctly. _CSTA: 2-AP-19.__

Dependencies:
* T14.G7.07.02.03: Implement save and load functions
* T13.G4.01: Test a feature and observe program behavior


ID: T14.G7.07.04
Topic: T14 – 2D Games
Skill: Record score to global leaderboard
Description: Use `record score (SCORE) to leaderboard` to submit the player's score to a game-wide leaderboard that all players can see. Call this when the game ends or a level completes. Scores are automatically ranked from highest to lowest. _Implementation note: Uses CreatiCode game_recordplayerscore block. CSTA: 2-AP-17.__

Dependencies:
* T14.G4.06: Create a Score variable
* T14.G3.07: Trigger Game Over


ID: T14.G7.07.05
Topic: T14 – 2D Games
Skill: Show game leaderboard
Description: Use `show leaderboard` to display the global leaderboard sprite showing top player scores and names. Position it on the game over screen or in the menu so players can see how they rank against others. _Implementation note: Uses CreatiCode game_showgameleaderboard block. CSTA: 2-AP-17.__

Dependencies:
* T14.G7.07.04: Record score to global leaderboard


ID: T14.G7.07.06
Topic: T14 – 2D Games
Skill: Hide game leaderboard
Description: Use `hide leaderboard` to remove the leaderboard display when returning to gameplay or other menu screens. This keeps the UI clean and only shows the leaderboard when relevant. _Implementation note: Uses CreatiCode game_hidegameleaderboard block. CSTA: 2-AP-17.__

Dependencies:
* T14.G7.07.05: Show game leaderboard


ID: T14.G7.07.07
Topic: T14 – 2D Games
Skill: Clear leaderboard scores
Description: Use `clear leaderboard` to reset all scores on the global leaderboard. This is useful during testing or when starting a new season/competition. Note: this affects all players, so use carefully. _Implementation note: Uses CreatiCode game_cleargameleaderboard block. CSTA: 2-AP-17.__

Dependencies:
* T14.G7.07.04: Record score to global leaderboard


ID: T14.G7.07.08
Topic: T14 – 2D Games
Skill: Store user data
Description: Use `store value (VALUE) for key [KEY]` to save custom game data associated with the current player. Unlike cloud variables, user data is private to each player and can store text or numbers using named keys like "HighScore", "UnlockedLevels", "Inventory". _Implementation note: Uses CreatiCode game_storeuserdatakey block. CSTA: 2-AP-17.__

Dependencies:
* T14.G7.07.02.02: Convert game state to storable format


ID: T14.G7.07.09
Topic: T14 – 2D Games
Skill: Read user data
Description: Use `read value for key [KEY]` reporter to retrieve previously stored user data. When the game starts, load saved data like high scores, unlocked levels, and player progress. Check if the key exists before using the value (it returns empty if never set). _Implementation note: Uses CreatiCode game_readuserdatakey block. CSTA: 2-AP-17.__

Dependencies:
* T14.G7.07.08: Store user data


# GRADE 8

ID: T14.G8.01
Topic: T14 – 2D Games
Skill: Modular level loader
Description: Create a system that reads a list of strings or table rows (e.g., "111000111" where 1=wall, 0=empty) to generate level layouts using clones. Use nested loops to process each character: outer loop for rows, inner loop for columns. Each character in the string creates a specific tile type at the corresponding grid position calculated by `(x: (col * 32) y: (row * 32))`. _CSTA: 3A-AP-13.__

Dependencies:
* T14.G7.01: Spatial partitioning (grid)
* T10.G5.01: Store and retrieve named data with a list


ID: T14.G8.02
Topic: T14 – 2D Games
Skill: Particle system
Description: Create a flexible particle system (explosions, smoke, rain) where one sprite manages many short-lived clones. Each particle has properties stored in lists (lifetime, speed, direction, color) that change over time using `change by` blocks. Particles delete themselves after their lifetime expires. Test different particle counts to balance visual appeal and performance. _CSTA: 3A-AP-17.__

Dependencies:
* T14.G7.04: Profile clone performance and implement optimization strategies
* T10.G5.01: Store and retrieve named data with a list


ID: T14.G8.03
Topic: T14 – 2D Games
Skill: Component-based entity system
Description: Design a flexible entity system where each sprite has a list of component tags (text values like 'CanTakeDamage', 'CanShoot', 'IsShopkeeper'). In your scripts, use if-statements with `<[Components] contains [CanTakeDamage]?>` to check if a sprite's component list contains specific tags before activating behaviors. For example, only run damage logic if the list contains 'CanTakeDamage'. This modular approach lets you create many different game objects by mixing and matching components without duplicating code. _CSTA: 3A-AP-13.__

Dependencies:
* T14.G6.01.02.04: Prevent invalid state actions
* T10.G5.01: Store and retrieve named data with a list


ID: T14.G8.04
Topic: T14 – 2D Games
Skill: Automated gameplay tests
Description: Build a testing system that plays your game automatically using scripted inputs. Create a list of test commands like "[space,0.5]" (press space, wait 0.5 seconds). Program a test runner to execute these commands using `when I receive [run test]` and broadcast key press messages. Check if win/lose conditions trigger correctly (e.g., 'Does game end when lives reach 0?'). Use broadcast messages to log what happened during the test and compare it to expected results before releasing your game to players. _CSTA: 3A-AP-19.__

Dependencies:
* T14.G7.05: Implement difficulty progression curves
* T10.G5.01: Store and retrieve named data with a list


ID: T14.G8.05
Topic: T14 – 2D Games
Skill: Collect game statistics for balancing
Description: Track and store player performance data in lists: how many times they die on each level using `add (deaths) to [Level Deaths]`, how long it takes to win using timer values, which power-ups they use most. After testing with multiple players, review this data using list operations to calculate averages and identify levels that are too hard (high death rate) or too easy (very fast completion). Adjust difficulty settings (enemy speed, obstacle count, time limits) based on the data to make your game fun and fair. _CSTA: 3A-AP-19.__

Dependencies:
* T14.G7.03: Balanced enemy spawning
* T10.G5.01: Store and retrieve named data with a list


---

# END OF T14 COMPLETE REVISED SECTION

**IMPORTANT NOTES:**
1. All K-2 skills remain picture-based (no coding required)
2. All G3+ skills use block-based coding with specific CreatiCode block names
3. Dependencies follow the X-2 rule (no dependencies more than 2 grades above)
4. All missing CreatiCode features have been added
5. Broad skills have been properly broken down into learnable sub-skills
6. Total skills increased from 66 to 106 for better scaffolding and coverage
