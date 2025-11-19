# T14 – 2D Games: K–8 Skill List (Draft v3)

Topic reference: `T14 2D Games` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, PRO‑PD (links to ALG‑AF, ALG‑PS, DAA‑DF, DAA‑DP, SAS‑IM)

This v3 refresh tightens the microstep ladder, keeps Grades K–2 unplugged/picture-based, aligns Grades 3–8 with adjacent topics (T06 Events, T07 Loops, T09 Variables, T12 Organizing Programs, T15 Stories & Animation, T17 Physics), and adds CreatiCode's viewport blocks (`move viewport`, `lock viewport to sprite`, `attach/detach to viewport`, `viewport x/y`). Students now learn camera, HUD, and streaming patterns without duplicating learning targets elsewhere.

Each skill below has:

- a stable **ID** (`T14.G<grade>.<nn>`),
- an IXL-style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Games and interactive experiences are introduced through simple cause-and-effect patterns and basic game ideas (players, goals, score, start/end), using picture-based, unplugged activities.

### T14.GK.01 – Match controls to character actions

- **Short name:** Connect a button to an action
- **Description:** Students drag arrow or button cards onto pictures showing the matching movement or reaction (tap jump button → character hops). They learn that inputs lead to predictable actions in games.
- **Challenge format:** Concept, picture matching. Drag control cards to the actions they trigger.
- **CSTA:** EK‑PRO‑DH‑03

### T14.GK.02 – Recognize a score in simple games

_Dependency:_
  * T01.GK.03: Find the first and last pictures


- **Short name:** Tell when points go up
- **Description:** Students compare before/after pictures of a score counter and gameplay moments (collecting a star, hitting a hazard) to see when the score changes and what it signals.
- **Challenge format:** Concept, picture-based questions. “Did the score go up?” “Who has more points?”
- **CSTA:** EK‑PRO‑DH‑03

### T14.GK.03 – Recognize a game starting and ending

_Dependency:_
  * T01.GK.03: Find the first and last pictures


- **Short name:** Spot start and game over
- **Description:** Students observe a simple game story with a clear beginning (Start screen) and ending (Game Over). They identify which pictures show the start, play, and end of the game.
- **Challenge format:** Concept, sequencing. Order pictures: Start Screen → Gameplay → Game Over.
- **CSTA:** EK‑ALG‑AF‑01

### T14.GK.04 – Match rewards to goals

- **Short name:** Pick the prize for winning
- **Description:** Students match pictures of finishing a level (touching a flag, clearing a board) to appropriate celebration panels (You Win text, trophy, fireworks) so they connect goals to feedback.
- **Challenge format:** Concept, drag-and-drop or pairing. Connect the goal picture to the reward picture.
- **CSTA:** EK‑PRO‑DH‑03

---

## Grade 1

Grade 1 students reason about simple game structure—players, goals, helpers, hazards, score, and fairness—through pictures and stories.

### T14.G1.01 – Identify the player, goal, and obstacles

_Dependency:_
  * T01.GK.03: Find the first and last pictures


- **Short name:** Find the player, goal, and dangers
- **Description:** In a picture of a game level (maze, platformer, board), students identify the controllable character, the goal, and the hazards that should be avoided.
- **Challenge format:** Concept, hotspot clicking. “Click on the player.” “Click on the danger.”
- **CSTA:** 1A‑AP‑08

### T14.G1.02 – Apply simple game rules

_Dependency:_
  * T01.GK.01: Put pictures in order for getting ready for bed


- **Short name:** Follow the game rules
- **Description:** Students are given a simple rule (e.g., “Collect all coins to open the door”) and a sequence of pictures. They decide if the player followed the rule.
- **Challenge format:** Concept, True/False. “Did the player follow the rule?”
- **CSTA:** 1A‑AP‑08

### T14.G1.03 – Compare game difficulty

_Dependency:_
  * T01.GK.04: Pick the pictures that make sense


- **Short name:** Which game is harder?
- **Description:** Students compare two pictures of the same game level—one with more obstacles or fewer platforms—and identify which one would be harder to play.
- **Challenge format:** Concept, comparison. “Which level is harder?”
- **CSTA:** 1A‑AP‑08

### T14.G1.04 – Predict the best next move

_Dependency:_
  * T01.GK.01: Put pictures in order for getting ready for bed


- **Short name:** Choose the next move
- **Description:** Given a short rule and a partially played level, students pick which control card (up, down, left, right, jump) keeps the player safe and moving toward the goal.
- **Challenge format:** Concept, multiple choice. “Which button should the player press next?”
- **CSTA:** 1A‑AP‑08

### T14.G1.05 – Distinguish helpers from hazards

_Dependency:_
  * T01.GK.01: Put pictures in order for getting ready for bed


- **Short name:** Spot helpful items
- **Description:** Students sort icons from a level (heart, speed shoe, spike, slime) into “helps you win” and “makes you lose,” building vocabulary around pickups and traps.
- **Challenge format:** Concept, sorting. Drag each icon into the helper or hazard bin.
- **CSTA:** 1A‑AP‑08

---

## Grade 2

Grade 2 students explore game flow concepts like turns, lives, levels, and balance without writing code.

### T14.G2.01 – Understand turns and rounds

_Dependency:_
  * T01.G1.01: Put pictures in order to plant a seed


- **Short name:** Whose turn is it?
- **Description:** Students look at a turn-based scene with multiple players or timers and determine whose turn it is or what happens next when a turn ends.
- **Challenge format:** Concept, prediction. “Player 1 just moved. Who moves next?”
- **CSTA:** 1A‑AP‑08

### T14.G2.02 – Track lives and game over conditions

_Dependency:_
  * T01.G1.01: Put pictures in order to plant a seed
  * T01.G1.04: Predict the next step in a story sequence


- **Short name:** Count lives and game over
- **Description:** Students track a player’s lives through a short picture story. They identify when a life is lost (touching a hazard) and when the game is over (lives reach zero).
- **Challenge format:** Concept, tracking. “After these events, how many lives remain?”
- **CSTA:** 1A‑AP‑10

### T14.G2.03 – Recognize level progression

_Dependency:_
  * T01.G1.01: Put pictures in order to plant a seed


- **Short name:** Moving to the next level
- **Description:** Students identify the condition for moving to the next level (touch goal, collect items) and notice that later levels are usually different or harder.
- **Challenge format:** Concept, multiple choice. “What must happen to go to Level 2?”
- **CSTA:** 1A‑AP‑10

### T14.G2.04 – Sequence a safe route

_Dependency:_
  * T01.G1.01: Put pictures in order to plant a seed
  * T01.G1.04: Predict the next step in a story sequence


- **Short name:** Plan how to reach the goal
- **Description:** Students order 3–4 picture cards showing a safe route through a level (jump over spikes, grab key, open door) to highlight planning before play.
- **Challenge format:** Concept, sequencing. Arrange the moves into a safe plan.
- **CSTA:** 1A‑AP‑08

### T14.G2.05 – Adjust difficulty knobs

_Dependency:_
  * T01.G1.10: Match pictures to "if/then" rules


- **Short name:** Make the level fair
- **Description:** Presented with a short brief (“Make it easier for new players”), students choose the change that best matches the goal (add another heart, remove a hazard, shorten timer) to understand balancing.
- **Challenge format:** Concept, choose-a-change. Drag the best change into the brief.
- **CSTA:** 1A‑AP‑10

---

## Grade 3

Grade 3 is the **gateway to coding** for games. Students move from concepts to building core components: player movement, interactions, flow, and feedback built on T06 (events) and T07 (loops).

### Strand A: Player Control

#### T14.G3.01 – Move a sprite with arrow keys (4 directions)

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.01: Use a counted repeat loop
  * T14.G2.01: Understand turns and rounds
  * T01.G3.05: Replace repeated blocks with a repeat loop

- **Short name:** Code 4-way movement
- **Description:** Create scripts where pressing up/down/left/right arrow keys changes the sprite’s x or y position, keeping motion smooth and repeatable.
- **Challenge format:** Build/Parsons. Assemble `when [up arrow] key pressed` → `change y by (10)` style scripts.
- **CSTA:** 1B‑AP‑10

#### T14.G3.02 – Move a sprite with keys (2 directions)

_Dependency:_
  * T14.G3.01: Move a sprite with arrow keys (4 directions)
  * T07.G3.02: Trace a script with a simple loop
  * T14.G2.02: Track lives and game over conditions

- **Short name:** Code left-right movement
- **Description:** Create scripts for platformer/paddle games where only left/right keys control the sprite and ensure speeds match on both sides.
- **Challenge format:** Build. Connect `when [right arrow] key pressed` → `change x by (10)` and mirror for left.
- **CSTA:** 1B‑AP‑10

#### T14.G3.03 – Keep sprite on screen

_Dependency:_
  * T14.G3.02: Move a sprite with keys (2 directions)
  * T08.G3.01: Use a simple if in a script
  * T14.G2.03: Recognize level progression

- **Short name:** Stop at the edge
- **Description:** Add logic to prevent the player from leaving the stage (use `if on edge, bounce` or explicit x/y checks) so losing never results from invisible space.
- **Challenge format:** Debug/Modify. “The player walks off the screen. Add a guard to keep them visible.”
- **CSTA:** 1B‑AP‑10

### Strand B: Interaction

#### T14.G3.04 – Detect touching a goal

_Dependency:_
  * T14.G3.03: Keep sprite on screen
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.G2.04: Sequence a safe route

- **Short name:** Code winning touch
- **Description:** Use `touching [Sprite]?` or `touching [Color]?` inside a loop to detect when the player reaches the goal and trigger a win message.
- **Challenge format:** Build. `forever` → `if <touching [Goal]> then` → `say [You Win!]`.
- **CSTA:** 1B‑AP‑10

#### T14.G3.05 – Detect touching a hazard

_Dependency:_
  * T14.G3.04: Detect touching a goal
  * T07.G3.03: Build a forever loop for simple animation
  * T08.G3.02: Decide when a single if is enough

- **Short name:** Code danger touch
- **Description:** Use collision checks with hazards (spikes, enemies) to reset the player to a safe position or broadcast a warning.
- **Challenge format:** Build. `if <touching [Spike]> then` → `go to x: start y: start`.
- **CSTA:** 1B‑AP‑10

### Strand C: Game Flow

#### T14.G3.06 – Create a start screen

_Dependency:_
  * T14.G3.05: Detect touching a hazard
  * T09.G3.02: Use a variable in a conditional (if block)
  * T06.G3.05: Trace a project with a single event and predict output

- **Short name:** Make a start button
- **Description:** Program a “Start” button sprite that hides itself and broadcasts `Start Game` when clicked.
- **Challenge format:** Build. `when this sprite clicked` → `hide` → `broadcast [Start Game]`.
- **CSTA:** 1B‑AP‑15

#### T14.G3.07 – Switch to game mode

_Dependency:_
  * T14.G3.06: Create a start screen
  * T10.G3.01: Loop through and process each item in a list
  * T11.G3.01: Understand when to use custom blocks vs loops

- **Short name:** Start game on signal
- **Description:** Program game objects to show and begin moving only after receiving `Start Game`, separating setup from play.
- **Challenge format:** Modify. Replace `when green flag clicked` with `when I receive [Start Game]` for sprites.
- **CSTA:** 1B‑AP‑15

#### T14.G3.08 – Trigger Game Over

_Dependency:_
  * T14.G3.07: Switch to game mode
  * T12.G3.01: Write a comment explaining a complex block
  * T08.G3.03: Pick the right conditional block for a scenario

- **Short name:** Broadcast game over
- **Description:** Broadcast `Game Over` when losing conditions occur and have other sprites stop/hide when they get that message.
- **Challenge format:** Build. `broadcast [Game Over]` → `stop [all]` plus listener scripts.
- **CSTA:** 1B‑AP‑15

### Strand D: Feedback

#### T14.G3.09 – Add sound effects to actions

_Dependency:_
  * T14.G3.08: Trigger Game Over
  * T09.G3.03: Debug missing or wrong variable updates
  * T07.G3.04: Use repeat‑until to reach a simple goal

- **Short name:** Play jump or collect sounds
- **Description:** Insert `start sound` blocks into movement/interaction scripts to provide audio feedback.
- **Challenge format:** Modify. “Add a ‘pop’ sound when the player touches the coin.”
- **CSTA:** 1B‑AP‑10

#### T14.G3.10 – Visual effects on interaction

_Dependency:_
  * T14.G3.09: Add sound effects to actions
  * T11.G3.02: Use a pre‑made helper block with parameters
  * T08.G3.04: Trace code with a single if/else

- **Short name:** Flash or change color
- **Description:** Use graphic effects (color, brightness, ghost) to show when a player is hit or collects an item.
- **Challenge format:** Build. `change [color] effect by (25)` inside interaction checks.
- **CSTA:** 1B‑AP‑10

---

## Grade 4

Grade 4 expands into mechanics and state. Students build projectiles, enemies, timers, and level transitions, preparing data structures for later grades.

### Strand A: Projectiles & Shooting

#### T14.G4.01 – Spawn a projectile

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.04: Match rewards to goals

- **Short name:** Create a bullet clone
- **Description:** Use `create clone of [Bullet]` (or `myself`) to spawn a projectile when an input occurs.
- **Challenge format:** Build. `when [space] key pressed` → `create clone of [Bullet]`.
- **CSTA:** 1B‑AP‑11

#### T14.G4.02 – Move a projectile

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.04: Match rewards to goals

- **Short name:** Make bullets fly
- **Description:** Program projectile clones to move forward continuously until they hit something.
- **Challenge format:** Build. `when I start as a clone` → `repeat until <touching [edge]>` → `move (10) steps`.
- **CSTA:** 1B‑AP‑11

#### T14.G4.03 – Clean up projectiles

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Delete bullets at edge
- **Description:** Delete clones when they touch an edge/target to prevent lag and bugs.
- **Challenge format:** Debug. “Bullets never disappear. Add cleanup logic.”
- **CSTA:** 1B‑AP‑11

### Strand B: Enemy Behavior

#### T14.G4.04 – Simple enemy movement

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.04: Match rewards to goals

- **Short name:** Patrol back and forth
- **Description:** Program an enemy to move between points or bounce off edges for predictable patrols.
- **Challenge format:** Build. `forever` → `move (5) steps` → `if on edge, bounce`.
- **CSTA:** 1B‑AP‑10

#### T14.G4.05 – Chase the player

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.04: Match rewards to goals

- **Short name:** Enemy follows player
- **Description:** Use `point towards [Player]` and `move` to create a simple chaser that slows when close.
- **Challenge format:** Build. `forever` → `point towards [Player]` → `move (2) steps`.
- **CSTA:** 1B‑AP‑10

### Strand C: State Tracking

#### T14.G4.06 – Create a Score variable

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Make a score keeper
- **Description:** Create a global `Score` variable, initialize it, and change it when events happen.
- **Challenge format:** Build. `set [Score] to (0)` → `change [Score] by (1)`.
- **CSTA:** 1B‑AP‑09

#### T14.G4.07 – Create a Lives variable

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Make a life counter
- **Description:** Create a `Lives` variable, decrease it upon damage, and check for zero to trigger Game Over.
- **Challenge format:** Build. `change [Lives] by (-1)` → `if <(Lives) < (1)> then` → `broadcast [Game Over]`.
- **CSTA:** 1B‑AP‑09

#### T14.G4.08 – Create a Timer

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Make a countdown timer
- **Description:** Use a variable and a loop with `wait (1) seconds` to create a countdown that drives win/loss conditions.
- **Challenge format:** Build. `repeat until <(Time) = (0)>` → `wait (1) secs` → `change [Time] by (-1)`.
- **CSTA:** 1B‑AP‑09

### Strand D: Level Progression

#### T14.G4.09 – Detect level complete

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Check win condition
- **Description:** Check if a condition (Score threshold, touch door) is met to trigger the next level.
- **Challenge format:** Logic/Build. `if <(Score) > (9)> then` → `broadcast [Next Level]`.
- **CSTA:** 1B‑AP‑10

#### T14.G4.10 – Switch backdrops for levels

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.04: Match rewards to goals

- **Short name:** Change the level background
- **Description:** When `Next Level` is received, switch the backdrop and reset player position.
- **Challenge format:** Build. `when I receive [Next Level]` → `next backdrop` → `go to x: start y: start`.
- **CSTA:** 1B‑AP‑10

### Strand E: Power-Ups & Flow

#### T14.G4.11 – Add checkpoints

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Save the last safe spot
- **Description:** Store the player’s last checkpoint coordinates in variables and restore them after hazards instead of warping all the way back.
- **Challenge format:** Build. When touching a checkpoint flag, `set [Checkpoint X] to (x position)` and later `go to x: (Checkpoint X) y: (Checkpoint Y)`.
- **CSTA:** 1B‑AP‑09

#### T14.G4.12 – Temporary power-ups

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.04: Match rewards to goals

- **Short name:** Time-limited boosts
- **Description:** Give the player a temporary effect (speed boost, shield) by toggling a variable and using a timer to turn it off.
- **Challenge format:** Build. `when I receive [Boost]` → `set [Speed Boost?] to [true]` → `wait (5)` → `set [Speed Boost?] to [false]`.
- **CSTA:** 1B‑AP‑09

#### T14.G4.13 – Pause and resume the game

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Pause with a broadcast
- **Description:** Create a Pause button that broadcasts `Pause Game`, stops motion scripts, and resumes when `Resume Game` arrives.
- **Challenge format:** Build. `when this sprite clicked` → `broadcast [Pause Game]`; listening sprites use `wait until <(State) = [Play]>` patterns.
- **CSTA:** 1B‑AP‑15

### Strand F: Reset & Replay

#### T14.G4.14 – Reset on restart messages

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Reset everything when told
- **Description:** Use `when I receive [Restart]` (or `Game Over`) to send every sprite back to a known costume, position, and visibility so repeats are consistent.
- **Challenge format:** Debug. “Some enemies stay hidden after a restart. Add a listener that resets them.”
- **CSTA:** 1B‑AP‑15

---

## Grade 5

Grade 5 introduces advanced 2D mechanics like gravity feel, scrolling via CreatiCode’s viewport blocks, spawning systems, and richer data handling, preparing students for engine thinking. Detailed physics formulas stay in T17; T14 focuses on tuning them for gameplay.

### Strand A: Feel & Fairness

#### T14.G5.01 – **[Engine Skill]** Configure gravity and weight parameters

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Set gravity values (technical)
- **Description:** Adjust the amount added to a `y velocity` variable each frame using specific numeric values. Students learn to map gravity constants to measurable jump heights and movement behaviors.
- **Challenge format:** Build/test. Students implement specific gravity values and measure the resulting physics behavior. Auto-grading checks parameter accuracy.
- **CSTA:** 1B‑AP‑10

#### T14.G5.01b – **[Creative Skill]** Design gravity feel for game experience
- **Short name:** Choose gravity for game feel (creative)
- **Description:** Select gravity values to match design briefs (floaty balloon vs. heavy robot) and explain how the choice supports player emotion and gameplay goals.
- **Challenge format:** Creative implementation. Students choose gravity settings to achieve specific player experiences and justify design decisions.
- **CSTA:** 1B‑AP‑10

#### T14.G5.02 – Control jump timing

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Add grounded checks
- **Description:** Allow jumping only when the player is touching the ground (or within a short “coyote time”) by checking sensors before setting `y velocity`.
- **Challenge format:** Build. `if <key [up arrow] pressed?> and <touching [Ground]?> then` → `set [y velocity] to (10)`.
- **CSTA:** 1B‑AP‑10

#### T14.G5.03 – Fix ground collisions

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Stop on the ground
- **Description:** Prevent falling through floors by nudging the sprite up until it is no longer intersecting the ground or by snapping to the floor after a fall.
- **Challenge format:** Debug/Refine. “The player sinks into the platform. Add a correction loop.”
- **CSTA:** 1B‑AP‑10

### Strand B: Camera & HUD (Viewport Blocks)

#### T14.G5.04 – Script viewport pans

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Move the camera window
- **Description:** Use `move viewport to x (XPOS) y (YPOS)` to place the camera at the start of a level or slide it during a cutscene before gameplay begins.
- **Challenge format:** Build. Add a short `repeat` loop that increments XPOS and calls `move viewport` for a pan.
- **CSTA:** 1B‑AP‑15

#### T14.G5.05 – Lock viewport to the player

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Follow the hero
- **Description:** Call `lock viewport to sprite [Player]` so the stage follows the player automatically, noting how edges behave when the player reaches the map boundary.
- **Challenge format:** Build. Insert the lock block after setup and test how the camera follows the sprite.
- **CSTA:** 1B‑AP‑10

#### T14.G5.06 – Pin HUD to the screen

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Attach score to viewport
- **Description:** Use `attach to viewport at x (XPOS) y (YPOS)` to place score, lives, and buttons relative to the viewport so they stay in the same spot even while the world scrolls.
- **Challenge format:** Build. Attach a score sprite at (‑200, 150) relative to the viewport and verify it stays fixed.
- **CSTA:** 1B‑AP‑09

### Strand C: Spawning & Waves

#### T14.G5.07 – Spawn near the viewport

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Spawn off-screen safely
- **Description:** Combine `viewport x`/`viewport y` reporters with random offsets to spawn enemies just outside the camera so they enter smoothly instead of popping on the player.
- **Challenge format:** Build. Set enemy position to `((viewport x) + (250))` with random Y and show it when ready.
- **CSTA:** 1B‑AP‑11

#### T14.G5.08 – Timed waves

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator

- **Short name:** Enemy waves
- **Description:** Use a loop or custom block to spawn a set number of enemies every few seconds, optionally adjusting difficulty each wave.
- **Challenge format:** Build. `forever` → `repeat (5)` → `create clone` → `wait (0.5)`; after the wave `wait (3)`.
- **CSTA:** 1B‑AP‑11

### Strand D: Data & Progression

#### T14.G5.09 – High score list

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Save high scores
- **Description:** Use a list to store the top scores, insert new scores in order, and display the list in a viewport-attached HUD sprite.
- **Challenge format:** Build/Modify. `add (Score) to [High Scores]`, sort, then draw the list on screen.
- **CSTA:** 1B‑AP‑09

#### T14.G5.10 – Inventory system

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Collect items in a list
- **Description:** Track collected items (“Key”, “Potion”) in a list, check membership before allowing actions, and show collected icons near the HUD.
- **Challenge format:** Build. `add [Key] to [Inventory]`; later `if <[Inventory] contains [Key]?> then` → `broadcast [Open Door]`.
- **CSTA:** 1B‑AP‑09

---

## Grade 6 (Middle School)

Grade 6 shifts toward architecture: state machines, clean collisions, layered HUDs, and viewport streaming/cutscenes that hand off between scripted cameras and player-controlled views.

### T14.G6.01 – Character state machine

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** State machine (Idle/Run/Jump)
- **Description:** Use a `State` variable (Idle, Run, Jump) to control animation and input handling, preventing conflicting actions such as double jumps.
- **Challenge format:** Refactor. Convert spaghetti code into a `State`-driven structure.
- **CSTA:** 2‑AP‑10

### T14.G6.02 – Hitbox separation

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Separate hitbox and art
- **Description:** Use a simple rectangular sprite or clone for collision detection (hitbox) and have the art sprite follow it, enabling readable collisions.
- **Challenge format:** Build. Program the art sprite to `go to [Hitbox]` each frame while the hitbox handles physics.
- **CSTA:** 2‑AP‑13

### T14.G6.03 – Multi-layer HUD with viewport attachments

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Stack HUD panels
- **Description:** Attach multiple sprites to the viewport (score, minimap, buttons) and manage their layering so UI always sits above gameplay while remaining interactive.
- **Challenge format:** Build. Use `attach to viewport at x/y`, `go to front layer`, and verify hit detection still works.
- **CSTA:** 2‑AP‑13

### T14.G6.04 – Stream level chunks with viewport reporters

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Load areas near the camera
- **Description:** Use `viewport x`/`viewport y` to determine which tiles or enemy sets should exist. Spawn new chunks just ahead of the camera and delete ones far behind to keep performance steady.
- **Challenge format:** Build. Given tile data, write logic that compares `(viewport x)` to chunk boundaries and creates/deletes clones accordingly.
- **CSTA:** 2‑AP‑17

### T14.G6.05 – Cinematic camera rails

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Detach for cutscenes
- **Description:** Call `detach from viewport`, run scripted `move viewport` sequences for intro/outro scenes, then relock to the player once the cutscene ends.
- **Challenge format:** Build. Add a `when I receive [Intro]` script that detaches, pans across landmarks, waits, then `lock viewport to sprite [Player]` again.
- **CSTA:** 2‑AP‑15

### T14.G6.06 – Mode and pause manager

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Manage Play/Pause/Shop states
- **Description:** Maintain a `Game Mode` variable and gate scripts so physics, UI, and spawns only run in the appropriate mode (Play, Pause, Shop, Cutscene).
- **Challenge format:** Build. Wrap loops with `wait until <(Game Mode) = [Play]>` and broadcast when switching modes.
- **CSTA:** 2‑AP‑10

---

## Grade 7 (Middle School)

Grade 7 focuses on efficiency and advanced mechanics: grid systems, smarter enemies, scalable spawning, and performance profiling.

### T14.G7.01 – Spatial partitioning (grid)

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.03: Recognize a game starting and ending
  * T14.GK.04: Match rewards to goals

- **Short name:** Grid-based movement
- **Description:** Implement movement that snaps to a tile grid (e.g., 32 px) and uses lists/tables to track which tiles are occupied, enabling puzzle/RPG logic.
- **Challenge format:** Build. Round coordinates to the nearest multiple of grid size after each move.
- **CSTA:** 2‑AP‑13

### T14.G7.02 – Basic pathfinding

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.04: Match rewards to goals

- **Short name:** Move toward target intelligently
- **Description:** Create an enemy that moves toward the player but slides along walls instead of getting stuck, using simple pathfinding or steering logic.
- **Challenge format:** Debug/Refine. Improve a “point towards” script to handle walls correctly.
- **CSTA:** 2‑AP‑13

### T14.G7.03 – Weighted spawn scheduler

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending
  * T14.GK.04: Match rewards to goals

- **Short name:** Data-driven spawns
- **Description:** Use a table/list of enemy types with weights and iterate through it to spawn diverse waves (e.g., 70% small, 30% tank) based on difficulty level.
- **Challenge format:** Build. Given a data table, script `repeat (wave size)` picking a random weighted entry before creating clones.
- **CSTA:** 2‑AP‑14

### T14.G7.04 – Clone budget profiler

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.04: Match rewards to goals

- **Short name:** Keep FPS stable
- **Description:** Track clone counts with watchers, measure frame rate, and refactor to reuse clones or throttle spawns when counts exceed a threshold.
- **Challenge format:** Debug. Instrument a project with a `Clone Count` variable and add guards that delay spawns when the count is high.
- **CSTA:** 2‑AP‑17

### T14.G7.05 – Difficulty curves

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.04: Match rewards to goals

- **Short name:** Scale challenge across levels
- **Description:** Store difficulty targets in a list (speed, damage, spawn interval by level) and apply them when the player advances, ensuring ramped but fair gameplay.
- **Challenge format:** Build. On `Next Level`, read the next row of a table and update enemy parameters.
- **CSTA:** 2‑AP‑14

---

## Grade 8 (Middle School)

Grade 8 students build reusable engines: modular loaders, component systems, effects, automated tests, and telemetry to balance play.

### T14.G8.01 – Modular level loader

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Load levels from data
- **Description:** Create a system that reads a list of strings or table rows (e.g., “111000111”) to generate level layouts via clones.
- **Challenge format:** Build. Parse a string and stamp/clone tiles at correct coordinates.
- **CSTA:** 2‑AP‑14

### T14.G8.02 – Particle system

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending
  * T14.GK.04: Match rewards to goals

- **Short name:** Particle effects engine
- **Description:** Create a flexible particle system (explosions, smoke) where one sprite manages many clones with properties like life, speed, and color.
- **Challenge format:** Build. Create a generic `spawn particle` custom block with parameters.
- **CSTA:** 2‑AP‑14

### T14.G8.03 – Component-based entities

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Attach behaviors by list
- **Description:** Store component tags (e.g., “CanTakeDamage”, “Shops”) in lists or tables per sprite and have scripts activate behaviors only when tags are present, enabling modularity.
- **Challenge format:** Build. Given a table of entities and components, write logic that iterates over tags to decide which scripts run.
- **CSTA:** 2‑AP‑14

### T14.G8.04 – Automated gameplay tests

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending

- **Short name:** Simulate runs to catch bugs
- **Description:** Build a test harness that moves the player via scripted inputs, logs outcomes, and asserts that win/lose conditions trigger correctly before releasing a level.
- **Challenge format:** Build. Create a `when I receive [Test Run]` script that plays a level hands-free and records pass/fail in a list.
- **CSTA:** 2‑AP‑17

### T14.G8.05 – Telemetry and balancing

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T14.GK.03: Recognize a game starting and ending
  * T14.GK.04: Match rewards to goals

- **Short name:** Log data to tune the game
- **Description:** Collect runtime stats (deaths per level, time-to-win) in lists, visualize them, and adjust difficulty knobs based on the data to keep the game fair.
- **Challenge format:** Build. Append data to a list after each round, then analyze and recommend a change (e.g., lower enemy speed) based on the numbers.
- **CSTA:** 2‑DA‑08
