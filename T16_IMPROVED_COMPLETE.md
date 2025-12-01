# T16 - 2D Motion & Physics (COMPLETE IMPROVED VERSION)

# MAJOR IMPROVEMENTS IMPLEMENTED:
#
# 1. ENHANCED K-2 FOUNDATION (Added 4 new picture-based skills):
#    - T16.K.05: Identify relative motion between objects
#    - T16.G1.04: Predict acceleration effects
#    - T16.G2.05: Trace energy transfer in collision chains
#    - T16.G2.06: Identify friction effects on motion
#
# 2. STRENGTHENED G3-G4 BRIDGE (Added 4 new skills):
#    - T16.G3.04: Use motion blocks to draw shapes
#    - T16.G4.04: Debug a broken motion animation
#    - T16.G4.05: Create smooth motion using glide blocks
#    - T16.G4.06: Build a simple racing game
#
# 3. PARALLEL TRACK STRUCTURE FOR G5:
#    - Track A (G5.01-G5.04): Manual physics with variables
#    - Track B (G5.05-G5.13): Engine-based physics
#    - T16.G5.14: Compare manual vs engine approaches (capstone)
#
# 4. COMPUTATIONAL THINKING SKILLS G6-G7:
#    - T16.G6.10: Predict collision outcomes
#    - T16.G6.11: Debug sprites passing through walls
#    - T16.G7.09: Trace physics simulation frame-by-frame
#    - T16.G7.10: Design physics experiment
#
# 5. AI INTEGRATION SKILLS G8:
#    - T16.G8.12: Create AI-controlled physics objects
#    - T16.G8.13: Use ML to optimize physics parameters
#    - T16.G8.14: Implement procedural level generation
#    - T16.G8.15: Build adaptive difficulty using physics telemetry
#
# 6. FIXED DEPENDENCY ISSUES:
#    - T16.G6.01 and G6.02 now reference correct skill names
#
# 7. ADDED SUB-SKILLS FOR DEPTH:
#    - T16.G5.06.04: Match collision shape to sprite artwork
#    - T16.G6.04.05: Create one-way platforms
#    - T16.G7.01.03: Calculate optimal launch angle


ID: T16.K.01
Topic: T16 – 2D Motion & Physics
Skill: Identify which sprite moved (picture-based)
Description: **Student task:** Look at two "before" and "after" picture cards showing a stage with multiple sprites. Tap the sprite that changed position. **Visual scenario:** Before card shows cat, dog, and ball in a row. After card shows dog moved to the right. Student taps the dog. **Vocabulary:** "moved," "same spot," "different spot." _Introduces the concept that motion = change in position._ Auto-graded by correct selection.

Dependencies:
None




ID: T16.K.02
Topic: T16 – 2D Motion & Physics
Skill: Match sprite to position after motion (picture-based)
Description: **Student task:** See a simple motion instruction (arrow or "move right") and choose which picture shows where the sprite will end up. **Visual scenario:** A bird is shown with a right-pointing arrow. Three pictures show the bird in different positions. Student taps the picture with the bird moved right. _Develops spatial reasoning for predicting motion._ Auto-graded by correct selection.

Dependencies:
* T16.K.01: Identify which sprite moved (picture-based)


ID: T16.K.02.01
Topic: T16 – 2D Motion & Physics
Skill: Identify direction of motion from trail marks (picture-based)
Description: **Student task:** Look at pictures showing sprites with trail marks (footprints, tire tracks, dotted lines) and identify which direction each sprite moved. **Visual scenario:** A duck picture shows footprints going from left to right. Student drags an arrow pointing right. A car shows tire marks curving upward. Student drags an arrow pointing up. **Vocabulary:** "trail," "path," "footprints," "tracks," "direction." _Introduces visual tracing as motion evidence._ Auto-graded by correct arrow placement.

Dependencies:
* T16.K.02: Match sprite to position after motion (picture-based)


ID: T16.K.03
Topic: T16 – 2D Motion & Physics
Skill: Identify objects that fall down (picture-based)
Description: **Student task:** Sort picture cards of objects into "falls down" and "stays up" piles. **Visual scenario:** Cards show: apple on table edge, balloon tied to string, ball in the air, bird flying, rock on a hill. Students sort based on everyday experience. **Discussion:** What makes things fall? (Gravity pulls things down.) _First introduction to gravity concept._ Auto-graded by correct sorting.

Dependencies:
* T16.K.01: Identify which sprite moved (picture-based)


ID: T16.K.04
Topic: T16 – 2D Motion & Physics
Skill: Sequence two motion steps (picture-based)
Description: **Student task:** Look at picture cards showing two motion steps (arrow right, then arrow up) and choose which final position picture is correct. **Visual scenario:** Cat starts in bottom-left. Card 1 shows "right arrow," Card 2 shows "up arrow." Four choices show cat in different corners. Student picks cat in top-right (moved right then up). **Vocabulary:** "first," "then," "after that." _Builds sequential motion thinking before coding._ Auto-graded by correct selection.

Dependencies:
* T16.K.02: Match sprite to position after motion (picture-based)


ID: T16.K.05
Topic: T16 – 2D Motion & Physics
Skill: Identify relative motion between objects (picture-based)
Description: **Student task:** Look at two animations playing side-by-side and identify which sprite moves faster relative to the other. **Visual scenario:** Two cars drive from left to right. Car A takes 5 seconds to cross the screen, Car B takes 3 seconds. Student taps Car B as "faster." Another scenario shows both cars moving but one appears faster because the background is also moving. **Vocabulary:** "faster than," "slower than," "same speed," "relative to." _Introduces comparative motion before variables._ Auto-graded by correct selection.

Dependencies:
* T16.K.02: Match sprite to position after motion (picture-based)




ID: T16.G1.01
Topic: T16 – 2D Motion & Physics
Skill: Identify fast vs slow motion (picture-based)
Description: **Student task:** Watch two sprite animations side by side and tap which sprite moves faster. **Visual scenario:** Two cats walk across the screen—one takes small slow steps, one takes big fast leaps. Student taps the fast cat. **Vocabulary:** Students describe motion using "fast," "slow," "quick," and "gentle." _Auto-graded by correct selection._

Dependencies:
* T16.K.02: Match sprite to position after motion (picture-based)


ID: T16.G1.02
Topic: T16 – 2D Motion & Physics
Skill: Predict motion direction from arrow pictures (picture-based)
Description: **Student task:** Look at a sprite with an arrow showing its direction, then tap where the sprite will be after it moves. **Visual scenario:** A car sprite has a green arrow pointing right. Three position choices show the car left, center, or right. Student taps the right position. _This builds directional intuition for motion prediction._ Auto-graded by correct position selection.

Dependencies:
* T16.G1.01: Identify fast vs slow motion (picture-based)


ID: T16.G1.02.01
Topic: T16 – 2D Motion & Physics
Skill: Predict final position after multiple arrow moves (picture-based)
Description: **Student task:** Look at a sequence of 3 arrow cards (right, right, up) and choose which final position picture is correct. **Visual scenario:** Robot starts in bottom-left corner. Cards show: arrow right, arrow right, arrow up. Four picture choices show robot in different positions. Student picks robot in top-middle (moved right twice, then up once). **Vocabulary:** "first move," "second move," "third move," "final position." _Builds multi-step motion prediction before loops._ Auto-graded by correct picture selection.

Dependencies:
* T16.G1.02: Predict motion direction from arrow pictures (picture-based)


ID: T16.G1.03
Topic: T16 – 2D Motion & Physics
Skill: Sort objects by how they fall (picture-based)
Description: **Student task:** Sort picture cards of objects into "falls fast" and "falls slow" piles. **Visual scenario:** Cards show feather, rock, balloon, ball, leaf, brick. Students sort based on everyday experience with gravity. **Discussion:** Teacher asks why some things fall faster (heavier, less air). _Builds intuition for gravity before coding._ Auto-graded by correct sorting.

Dependencies:
* T16.K.03: Identify objects that fall down (picture-based)
* T16.G1.01: Identify fast vs slow motion (picture-based)


ID: T16.G1.04
Topic: T16 – 2D Motion & Physics
Skill: Predict acceleration effects (picture-based)
Description: **Student task:** Look at two side-by-side animations showing a car. Animation A shows the car moving at constant speed (equal spacing between position markers). Animation B shows the car speeding up (increasing spacing between markers). Student identifies which car is "speeding up" and which is "staying the same speed." **Visual scenario:** Picture cards show position snapshots at equal time intervals with spacing markers. **Vocabulary:** "speeding up," "slowing down," "constant speed," "acceleration." _Introduces acceleration concept before variables._ Auto-graded by correct identification.

Dependencies:
* T16.G1.01: Identify fast vs slow motion (picture-based)
* T16.K.05: Identify relative motion between objects (picture-based)




ID: T16.G2.01
Topic: T16 – 2D Motion & Physics
Skill: Predict sprite direction from motion blocks (picture choices)
Description: **Student task:** Look at motion blocks (move 10 steps, turn right, move 10 steps) shown as picture cards and choose which picture shows where the sprite ends up. **Visual scenario:** A cat starts facing right. Blocks show: turn left, move forward. Four picture choices show cat in different positions. Student picks the cat that moved up. _Builds directional intuition before coding._ Auto-graded by correct picture selection.

Dependencies:
* T16.G1.02: Predict motion direction from arrow pictures (picture-based)




ID: T16.G2.02
Topic: T16 – 2D Motion & Physics
Skill: Identify bouncing vs sliding motion (picture-based)
Description: **Student task:** Watch two animations and identify which shows bouncing and which shows sliding. **Visual scenario:** Animation A shows a ball hitting a wall and bouncing back. Animation B shows a box sliding along the floor and stopping. Student labels each correctly. **Vocabulary:** "bounce," "slide," "stop," "reverse direction." _Builds intuition for friction and restitution concepts._ Auto-graded by correct labeling.

Dependencies:
* T16.G2.01: Predict sprite direction from motion blocks (picture choices)


ID: T16.G2.02.01
Topic: T16 – 2D Motion & Physics
Skill: Predict which object will fall faster (picture-based)
Description: **Student task:** Look at two side-by-side animations showing objects starting to fall, then predict which will hit the ground first. **Visual scenario:** Animation setup shows a feather and a rock both released from the same height. Student selects "rock will fall faster" before animations run. After selection, animations play to confirm. **Discussion:** Why does the rock fall faster? (Heavier, less air pushes it.) _Builds gravity and mass intuition._ Auto-graded by reasonable prediction.

Dependencies:
* T16.G2.01: Predict sprite direction from motion blocks (picture choices)


ID: T16.G2.03
Topic: T16 – 2D Motion & Physics
Skill: Predict collision outcomes (picture-based)
Description: **Student task:** Look at a picture showing two objects about to collide, then choose what happens next. **Visual scenario:** A rolling ball approaches a stationary block. Choices: (A) ball stops, block moves, (B) ball bounces back, block stays, (C) both move right. Student picks based on intuition about heavy/light objects. _Reveals physics intuition about mass and momentum._ Auto-graded by reasonable selection with explanation prompt.

Dependencies:
* T16.G2.02: Identify bouncing vs sliding motion (picture-based)


ID: T16.G2.03.01
Topic: T16 – 2D Motion & Physics
Skill: Sequence collision events in order (picture-based)
Description: **Student task:** Look at 4 picture cards showing different moments of a collision (before touch, touching, bouncing apart, after bounce) and drag them into the correct time order. **Visual scenario:** Cards show: (A) ball approaching wall, (B) ball touching wall, (C) ball bouncing away from wall, (D) ball far from wall after bounce. Student arranges as A-B-C-D. **Vocabulary:** "before," "during," "after," "collision," "bounce." _Develops cause-effect physics sequencing._ Auto-graded by correct ordering.

Dependencies:
* T16.G2.03: Predict collision outcomes (picture-based)


ID: T16.G2.04
Topic: T16 – 2D Motion & Physics
Skill: Compare speeds of two moving objects (picture-based)
Description: **Student task:** Watch two sprites race across the screen at different speeds, then answer: "Which one is faster?" and "Which one is slower?" **Visual scenario:** A rabbit hops quickly across the top, a turtle walks slowly across the bottom. Student identifies rabbit as faster, turtle as slower. **Extension:** Students estimate how much faster (e.g., "twice as fast," "a little faster"). _Builds quantitative speed comparison before variables._ Auto-graded by correct identification.

Dependencies:
* T16.G1.01: Identify fast vs slow motion (picture-based)


ID: T16.G2.05
Topic: T16 – 2D Motion & Physics
Skill: Trace energy transfer in collision chains (picture-based)
Description: **Student task:** Watch a Newton's cradle-style animation where one ball hits a line of balls, and the energy transfers through to make the last ball swing out. Student traces the energy path by tapping balls in order. **Visual scenario:** Five balls hang in a row. Left ball swings and hits the line. Middle balls stay still. Right ball swings out. Student taps: left ball → middle balls → right ball. **Vocabulary:** "energy," "transfer," "through," "chain reaction." _Introduces energy conservation concept visually._ Auto-graded by correct sequence.

Dependencies:
* T16.G2.03.01: Sequence collision events in order (picture-based)


ID: T16.G2.06
Topic: T16 – 2D Motion & Physics
Skill: Identify friction effects on motion (picture-based)
Description: **Student task:** Watch two animations showing a block sliding on different surfaces (ice vs carpet) and identify which surface has more friction. **Visual scenario:** Animation A shows block sliding far on ice before stopping. Animation B shows block stopping quickly on carpet. Student identifies carpet as "more friction" and ice as "less friction." **Discussion:** What makes things slow down when sliding? (Friction between surfaces.) **Vocabulary:** "friction," "smooth," "rough," "slow down." _Introduces friction concept before physics engine._ Auto-graded by correct labeling.

Dependencies:
* T16.G2.02: Identify bouncing vs sliding motion (picture-based)




ID: T16.G3.01
Topic: T16 – 2D Motion & Physics
Skill: Trace how motion blocks change sprite position
Description: Trace through motion blocks (`move`, `glide`) to determine how a sprite's position changes. Predict the sprite's final position after running a sequence of motion blocks, explaining reasoning step by step. **Example:** Given `go to x: 0 y: 0`, `move 50 steps`, `turn right 90 degrees`, `move 30 steps`, trace position changes to predict final x,y coordinates. **Acceptance criteria:** Correctly calculate final position with step-by-step work shown.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T16.G2.03: Predict collision outcomes (picture-based)




ID: T16.G3.02
Topic: T16 – 2D Motion & Physics
Skill: Predict direction and distance of sprite motion
Description: Predict which direction a sprite will move and approximately how far, given a sequence of motion blocks. Develop intuition for motion before variables are introduced. **Example:** Given `point in direction 90`, `move 100 steps`, predict sprite moves straight up approximately 100 units. **Acceptance criteria:** Correct direction and reasonable distance estimate.

Dependencies:
* T16.G3.01: Trace how motion blocks change sprite position


ID: T16.G3.02.01
Topic: T16 – 2D Motion & Physics
Skill: Calculate position after motion with given starting point
Description: Trace through motion blocks to calculate exact final x,y coordinates when given specific starting coordinates. **Example:** Start at (50, -30). Run blocks: `change x by 20`, `change y by 40`. Calculate final position: (70, 10). Show work step-by-step with coordinate pairs after each block. **Acceptance criteria:** All intermediate positions calculated correctly, final coordinates exact, work shown clearly.

Dependencies:
* T16.G3.02: Predict direction and distance of sprite motion


ID: T16.G3.03
Topic: T16 – 2D Motion & Physics
Skill: Debug why sprite doesn't move as expected (picture-based debugging intro)
Description: Examine a buggy motion script shown as picture blocks and identify why the sprite doesn't reach the expected position. **Visual scenario:** Script shows `point in direction 0`, `move 50 steps` but sprite should face right (90 degrees). Student identifies wrong direction value. **Common bugs:** wrong direction, wrong step count, missing turn block. _Introduces debugging thinking before text code._ **Acceptance criteria:** Correctly identify the bug and suggest fix.

Dependencies:
* T16.G3.02: Predict direction and distance of sprite motion


ID: T16.G3.04
Topic: T16 – 2D Motion & Physics
Skill: Use motion blocks to draw shapes (square, triangle)
Description: Create scripts that use motion and turn blocks to draw geometric shapes on the stage. **Implementation:** (1) For square: repeat 4 times [move 100 steps, turn right 90 degrees], (2) for triangle: repeat 3 times [move 100 steps, turn right 120 degrees]. Use pen down/up to create visible trails. **Acceptance criteria:** Both square and triangle drawn correctly using loops and calculated turn angles.

Dependencies:
* T07.G3.01: Use a counted repeat loop
* T16.G3.02: Predict direction and distance of sprite motion




ID: T16.G4.01
Topic: T16 – 2D Motion & Physics
Skill: Simulate falling with repeated motion
Description: Create a simple falling animation by repeatedly moving a sprite down in a loop. Observe that the sprite appears to "fall" due to gravity conceptually, preparing for velocity-based motion. **Implementation:** Use `repeat` loop with `change y by -5` to simulate falling. **Acceptance criteria:** Sprite falls smoothly from top to bottom of stage.

Dependencies:
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T07.G3.01: Use a counted repeat loop
* T16.G3.02: Predict direction and distance of sprite motion


ID: T16.G4.01.01
Topic: T16 – 2D Motion & Physics
Skill: Compare different fall speeds in simulation
Description: Create two falling sprites with different step sizes in their repeat loops (`change y by -3` vs `change y by -8`) and observe which reaches the bottom first. Record timing and explain the relationship between step size and fall duration. **Implementation:** Two sprites start at y=150, loop until y<-150, time how many loop iterations each takes. **Acceptance criteria:** Correctly predict and verify that larger step size = faster fall = fewer iterations.

Dependencies:
* T16.G4.01: Simulate falling with repeated motion


ID: T16.G4.02
Topic: T16 – 2D Motion & Physics
Skill: Explain speed as position change over time
Description: Explain that speed means "how much position changes each time the loop runs." Compare fast vs slow motion by changing the step size in a loop. **Example:** `change y by -2` creates slow falling, `change y by -10` creates fast falling. **Acceptance criteria:** Correctly explain relationship between step size and perceived speed.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T06.G2.03: Design a simple "if-then" game rule
* T09.G3.05: Trace code with variables to predict outcomes
* T16.G4.01: Simulate falling with repeated motion


ID: T16.G4.02.01
Topic: T16 – 2D Motion & Physics
Skill: Trace velocity changes during repeated motion
Description: Build a script that displays the current `change y by` value on screen during falling motion. Start with `change y by -2`, show the value updating each loop, then modify to decrease by -1 each frame to simulate acceleration. Trace how velocity changes create acceleration. **Implementation:** Create velocity variable, display it, change it each frame, observe acceleration effect. **Acceptance criteria:** Velocity variable tracked correctly, acceleration effect demonstrated, relationship explained.

Dependencies:
* T16.G4.02: Explain speed as position change over time


ID: T16.G4.03
Topic: T16 – 2D Motion & Physics
Skill: Build a simple bounce animation without physics engine
Description: Create a bouncing ball animation using loops and conditionals without the physics engine. **Implementation:** (1) Move ball down in loop, (2) when touching floor (y < -150), reverse direction, (3) ball moves up, (4) when touching top, reverse again. **Acceptance criteria:** Ball bounces continuously between top and bottom without physics blocks. _This manual approach builds understanding before using restitution parameters._

Dependencies:
* T08.G3.01: Use a simple if in a script
* T16.G4.02: Explain speed as position change over time


ID: T16.G4.04
Topic: T16 – 2D Motion & Physics
Skill: Debug a broken motion animation (sprite moves wrong direction)
Description: Given a buggy project where a sprite is supposed to move right but moves left instead, identify and fix the error. **Common bugs:** wrong direction value (270 instead of 90), negative step count, incorrect x/y axis. **Implementation:** Examine motion blocks, identify incorrect parameter, correct it, verify sprite moves as intended. **Acceptance criteria:** Bug identified correctly, fix applied, sprite motion verified.

Dependencies:
* T16.G3.03: Debug why sprite doesn't move as expected (picture-based debugging intro)
* T16.G4.01: Simulate falling with repeated motion


ID: T16.G4.05
Topic: T16 – 2D Motion & Physics
Skill: Create smooth motion using glide blocks vs step-based motion
Description: Compare two motion approaches: (1) step-based motion using `repeat` loop with `move 5 steps`, (2) smooth motion using `glide 2 secs to x: 200 y: 100`. Observe that glide creates smoother animation and simpler code for straight-line movement. **Acceptance criteria:** Both approaches implemented, differences explained, appropriate use cases identified.

Dependencies:
* T16.G4.01: Simulate falling with repeated motion


ID: T16.G4.06
Topic: T16 – 2D Motion & Physics
Skill: Build a simple racing game with keyboard-controlled sprite
Description: Create a basic racing game where arrow keys control a sprite's movement across the stage. **Implementation:** (1) Use `when [up arrow] key pressed` to move sprite up, (2) similar handlers for down/left/right arrows, (3) add finish line sprite, (4) detect when player reaches finish using `touching [finish line]`, (5) display "You Win!" message. **Acceptance criteria:** All four directions work, finish detection works, game is playable.

Dependencies:
* T06.G4.01: Use multiple event handlers in the same sprite
* T08.G3.01: Use a simple if in a script
* T16.G4.02: Explain speed as position change over time




ID: T16.G5.01
Topic: T16 – 2D Motion & Physics
Skill: Apply gravity to a sprite using 2D physics
Description: Use the physics engine to apply gravity forces to a sprite, observing how it falls and accelerates naturally. Understand that gravity is a constant downward force that affects all dynamic physics bodies in the scene. **Implementation:** Initialize physics world with gravity, attach dynamic body to sprite. **Acceptance criteria:** Sprite falls and accelerates smoothly.

Dependencies:
* T16.G4.02: Explain speed as position change over time




ID: T16.G5.02
Topic: T16 – 2D Motion & Physics
Skill: Track gravity with velocity variables
Description: Build a loop that stores a sprite's y-velocity in a variable, subtracts a gravity constant each frame, then adds the velocity to the sprite's y-position. This manual approach mirrors classic Scratch tutorials and prepares for physics debugging. **Implementation:** Create `yVelocity` variable, each frame: `change yVelocity by -1`, `change y by yVelocity`. **Acceptance criteria:** Manual gravity produces smooth acceleration matching physics engine behavior.

Dependencies:
* T07.G3.05: Fix a simple repeat loop count
* T09.G3.05: Trace code with variables to predict outcomes
* T16.G5.01: Apply gravity to a sprite using 2D physics
* T08.G3.00: Identify if blocks in existing code




ID: T16.G5.03
Topic: T16 – 2D Motion & Physics
Skill: Use horizontal speed and friction variables
Description: Add an x-velocity variable, respond to arrow keys to change it, and multiply by a friction factor (e.g., 0.9) each tick so motion glides to a stop. This prepares for platformer mechanics. **Implementation:** Create `xVelocity` variable, arrow keys: `change xVelocity by 2`, each frame: `set xVelocity to (xVelocity * 0.9)`, `change x by xVelocity`. **Acceptance criteria:** Sprite accelerates when keys pressed, glides to stop when released.

Dependencies:
* T09.G4.03: Use multiple variables in a single script
* T16.G5.02: Track gravity with velocity variables
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code


ID: T16.G5.03.01
Topic: T16 – 2D Motion & Physics
Skill: Build a top-down vehicle with manual friction control
Description: Create a top-down car or spaceship game using manual friction variables. **Implementation:** (1) Add xVelocity and yVelocity variables, (2) respond to arrow keys to adjust velocities, (3) multiply both velocities by friction factor (0.95) each frame so vehicle drifts to a stop, (4) update sprite position using velocities. **Acceptance criteria:** Vehicle feels responsive but gradually slows down when keys are released, creating realistic drift mechanics.

Dependencies:
* T16.G5.03: Use horizontal speed and friction variables




ID: T16.G5.04
Topic: T16 – 2D Motion & Physics
Skill: Code a manual bounce with energy loss
Description: Write a conditional that checks for ground contact, multiplies the y-velocity by a negative damping factor (e.g., -0.6), and sends the sprite back up with reduced height. This cements physics vocabulary before using the engine's restitution. **Implementation:** `if <y position < -150>`, `set yVelocity to (yVelocity * -0.6)`. **Acceptance criteria:** Ball bounces with decreasing height until stopping.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T16.G5.02: Track gravity with velocity variables


ID: T16.G5.04.01
Topic: T16 – 2D Motion & Physics
Skill: Create a simple platformer using manual gravity
Description: Build a basic platformer game combining manual gravity, horizontal friction, and ground detection. **Features:** (1) Character falls with gravity (yVelocity decreases each frame), (2) pressing jump key adds upward velocity only when touching ground, (3) left/right keys control horizontal movement with friction, (4) character stops at floor level. **Acceptance criteria:** All features work correctly, character can jump and move smoothly. This integrates all manual physics concepts before using the engine.

Dependencies:
* T16.G5.04: Code a manual bounce with energy loss
* T16.G5.03: Use horizontal speed and friction variables




ID: T16.G5.05
Topic: T16 – 2D Motion & Physics
Skill: Initialize a 2D physics world
Description: Add the `initialize 2D physics world with gravity x [0] y [-100]` block, set appropriate gravity values, and confirm the debug overlay shows the world running. Understand that no physics behavior occurs until this block executes. **Note:** Running this block again resets the entire physics world, useful for level transitions or game resets. **Acceptance criteria:** Physics world initializes successfully, debug overlay visible.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T16.G4.02: Explain speed as position change over time
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name




ID: T16.G5.06
Topic: T16 – 2D Motion & Physics
Skill: Attach a dynamic body to a sprite
Description: Convert a sprite to a dynamic physics body using `behave as a [dynamic] [object] shape [Box] debug [Yes]`. Observe the sprite fall and stop when it hits the stage floor, confirming the physics world affects it. **Acceptance criteria:** Sprite falls under gravity and collides with stage boundaries correctly.

Dependencies:
* T16.G5.05: Initialize a 2D physics world


ID: T16.G5.06.00
Topic: T16 – 2D Motion & Physics
Skill: Practice creating multiple dynamic bodies
Description: Create 2-3 different sprites and convert each to dynamic physics bodies. Experiment with different starting positions and observe how all bodies fall and interact, building fluency with the basic dynamic body setup before exploring shape options. **Acceptance criteria:** All sprites fall independently and collide with each other realistically.

Dependencies:
* T16.G5.06: Attach a dynamic body to a sprite


ID: T16.G5.06.00.01
Topic: T16 – 2D Motion & Physics
Skill: Use debug mode to visualize collision shapes
Description: Enable debug mode in the 2D physics world to see invisible collision shape outlines overlaid on sprites. Understand that debug mode helps understand why collisions happen or don't happen, by showing the actual physics boundaries independent of sprite appearance. **Acceptance criteria:** Debug outlines visible, correctly identify shape boundaries vs sprite visuals.

Dependencies:
* T16.G5.06.00: Practice creating multiple dynamic bodies


ID: T16.G5.06.01
Topic: T16 – 2D Motion & Physics
Skill: Choose Box vs Circle collision shapes
Description: Select between Box and Circle collision shapes based on sprite appearance and desired physics behavior. **Guidelines:** Use Box for rectangular sprites (platforms, crates, walls) that should stack stably. Use Circle for round sprites (balls, wheels, coins) that should roll smoothly. Test both shapes on the same sprite to observe behavioral differences. **Acceptance criteria:** Correctly justify shape choice for given sprites.

Dependencies:
* T16.G5.06.00: Practice creating multiple dynamic bodies


ID: T16.G5.06.01.01
Topic: T16 – 2D Motion & Physics
Skill: Use Capsule shapes for elongated objects
Description: Select Capsule collision shapes for elongated sprites (characters, vehicles, rods). Observe how Capsules provide smoother rolling and better collision response for pill-shaped objects compared to boxes, useful for character physics that should roll over obstacles without catching on edges. **Acceptance criteria:** Capsule shape selected for appropriate sprites, smooth obstacle traversal demonstrated.

Dependencies:
* T16.G5.06.01: Choose Box vs Circle collision shapes


ID: T16.G5.06.01.02
Topic: T16 – 2D Motion & Physics
Skill: Use Convex Hull for sprite-fitted collision
Description: Apply Convex Hull collision shapes to create automatic collision boundaries that closely match sprite outlines. Understand that Convex Hull wraps the sprite's visible pixels with the smallest convex polygon, providing better visual accuracy than basic shapes but using more computational resources. **Acceptance criteria:** Convex Hull applied correctly, trade-offs understood.

Dependencies:
* T16.G5.06.01: Choose Box vs Circle collision shapes


ID: T16.G5.06.02
Topic: T16 – 2D Motion & Physics
Skill: Create sensor bodies for trigger zones
Description: Create sensor bodies using `behave as a [dynamic] [sensor]` that detect overlaps without causing physical collisions. Use sensors for trigger zones, collectible detection areas, and checkpoint markers. **Acceptance criteria:** Sensor detects overlaps but doesn't physically block movement.

Dependencies:
* T16.G5.06.01: Choose Box vs Circle collision shapes


ID: T16.G5.06.03
Topic: T16 – 2D Motion & Physics
Skill: Create compound shapes for complex sprites
Description: Use `behave as a [dynamic] [object] in compound shape with curve tolerance [value] point distance [value]` to create physics bodies that match complex or concave sprite outlines. Understand the trade-off between accuracy and performance. **Acceptance criteria:** Compound shape created for complex sprite, performance impact considered.

Dependencies:
* T16.G5.06.01: Choose Box vs Circle collision shapes


ID: T16.G5.06.04
Topic: T16 – 2D Motion & Physics
Skill: Match collision shape to sprite artwork
Description: Given a sprite with specific artwork (star, crescent moon, car, character), select the most appropriate collision shape that balances visual accuracy and performance. **Process:** (1) Examine sprite outline, (2) consider gameplay needs (does it need to roll? stack?), (3) test multiple shapes, (4) select best match justifying trade-offs. **Acceptance criteria:** Shape choice justified for 3+ different sprite types, visual accuracy vs performance trade-off explained.

Dependencies:
* T16.G5.06.01: Choose Box vs Circle collision shapes
* T16.G5.06.01.02: Use Convex Hull for sprite-fitted collision




ID: T16.G5.07
Topic: T16 – 2D Motion & Physics
Skill: Build fixed boundaries for floors and walls
Description: Add fixed physics bodies to floor or wall sprites using `behave as a [fixed] [object]` so falling or sliding objects stop on contact. Learn to use fixed bodies for geometry that should not move. **Acceptance criteria:** Fixed boundaries stop dynamic objects correctly, fixed bodies don't move under force.

Dependencies:
* T16.G5.05: Initialize a 2D physics world




ID: T16.G5.08
Topic: T16 – 2D Motion & Physics
Skill: Apply an impulse to jump or push
Description: Use `apply impulse [force] in direction [angle]` to make a dynamic sprite jump in response to input (e.g., direction 90 for upward jump). Control impulse strength so the sprite clears a target platform height. **Acceptance criteria:** Impulse produces consistent jump height, sprite lands on target platform.

Dependencies:
* T06.G4.01: Use multiple event handlers in the same sprite
* T16.G5.06: Attach a dynamic body to a sprite


ID: T16.G5.08.01
Topic: T16 – 2D Motion & Physics
Skill: Distinguish forces from impulses
Description: Compare `add force [force] in direction [angle]` (applied continuously each frame) with `apply impulse [force] in direction [angle]` (applied once instantly). Use forces for sustained thrust (jetpack) and impulses for sudden actions (jump, kick). **Acceptance criteria:** Correctly explain difference, select appropriate method for given scenarios.

Dependencies:
* T16.G5.08: Apply an impulse to jump or push


ID: T16.G5.08.02
Topic: T16 – 2D Motion & Physics
Skill: Apply impulse at a position for rotation
Description: Use `apply impulse [force] in direction [angle] at position x [X] y [Y]` to apply off-center impulses. Observe how impulses applied away from center create instant rotation (torque), useful for hitting objects at an angle or creating spin effects. **Acceptance criteria:** Off-center impulse produces rotation, effect understood and controlled.

Dependencies:
* T16.G5.08.01: Distinguish forces from impulses


ID: T16.G5.08.03
Topic: T16 – 2D Motion & Physics
Skill: Apply a single continuous force
Description: Use `add force [force] in direction [angle]` to apply a single continuous force to a physics body (e.g., constant wind, jetpack thrust). Observe how continuous forces create sustained acceleration unlike one-time impulses, preparing for combining multiple forces. **Acceptance criteria:** Continuous force creates sustained acceleration, difference from impulse clear.

Dependencies:
* T16.G5.08.01: Distinguish forces from impulses




ID: T16.G5.09
Topic: T16 – 2D Motion & Physics
Skill: Configure density for mass control
Description: Adjust density using `update density [value]` to control how heavy a sprite feels. Understand that density × area = mass and experiment with light vs heavy objects in collisions. **Acceptance criteria:** Demonstrate density's effect on collision outcomes, heavier objects push lighter ones.

Dependencies:
* T16.G5.06: Attach a dynamic body to a sprite


ID: T16.G5.09.01
Topic: T16 – 2D Motion & Physics
Skill: Configure friction percentage for sliding control
Description: Adjust the friction percentage parameter using `update density [value] friction [value]%` to control surface stickiness. Configure different friction values (0%, 50%, 100%) and observe how friction affects sliding distance. Prepare for detailed friction experiments in G6. **Acceptance criteria:** Friction changes sliding distance measurably, relationship between friction and sliding understood, three different friction values tested.

Dependencies:
* T16.G5.09: Configure density for mass control


ID: T16.G5.09.02
Topic: T16 – 2D Motion & Physics
Skill: Configure restitution percentage for bounce control
Description: Adjust the restitution percentage parameter using `update density [value] friction [value]% restitution [value]%` to control bounciness. Configure different restitution values (0%, 50%, 100%) and observe bounce behavior systematically. Prepare for bounce height measurements in G6. **Acceptance criteria:** Restitution changes bounce height predictably, 0%=no bounce and 100%=full bounce verified, three different restitution values tested.

Dependencies:
* T16.G5.09.01: Configure friction percentage for sliding control




ID: T16.G5.10
Topic: T16 – 2D Motion & Physics
Skill: Trace simple 2D physics motion
Description: Experiment with a physics simulation by adjusting gravity, density, and starting height values, then predict and verify where the sprite lands. Run the simulation, observe outcomes, and choose the correct statement about where the sprite ends up (e.g., "lands on the platform," "still in the air," "passed through the floor"). This hands-on prediction and testing builds physics intuition. **Acceptance criteria:** Correctly predict landing position based on physics parameters.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T16.G5.06: Attach a dynamic body to a sprite


ID: T16.G5.10.01
Topic: T16 – 2D Motion & Physics
Skill: Remove physics body from a sprite
Description: Use `remove physics-based behavior` to detach a sprite from the physics engine so it no longer responds to gravity or collisions. Use this for collected items, destroyed enemies, or transitioning between physics and non-physics modes. **Acceptance criteria:** Sprite stops responding to physics after removal, useful for collectibles demonstrated.

Dependencies:
* T16.G5.06: Attach a dynamic body to a sprite




ID: T16.G5.11
Topic: T16 – 2D Motion & Physics
Skill: Debug missing physics setup
Description: Open a buggy project where the player never falls because the physics world was not initialized or the body was left as fixed. Inspect the scripts, identify the missing setup, and re-test. **Acceptance criteria:** Correctly identify missing initialization or incorrect body type, fix implemented successfully.

Dependencies:
* T16.G5.06: Attach a dynamic body to a sprite
* T16.G5.07: Build fixed boundaries for floors and walls




ID: T16.G5.12
Topic: T16 – 2D Motion & Physics
Skill: Choose manual vs engine-based physics
Description: After experiencing both manual velocity variables (G5.02-G5.04) and the physics engine (G5.05-G5.11), compare CreatiCode project briefs (platformer, UI animation, top-down maze, pinball machine) and choose the most appropriate approach for each. Justify decisions based on project requirements and hands-on experience with both methods. **Acceptance criteria:** Correct method chosen for each scenario with clear justification.

Dependencies:
* T05.G4.05: Plan a simulation with defined inputs and outputs
* T16.G5.04: Code a manual bounce with energy loss
* T16.G5.11: Debug missing physics setup


ID: T16.G5.13
Topic: T16 – 2D Motion & Physics
Skill: Use (speed) reporter to display total speed
Description: Use the `(speed)` reporter block to read and display a physics body's total velocity magnitude (combining x and y components). Understand that `(speed)` returns the scalar speed value while `(x speed)` and `(y speed)` return directional components. **Example use cases:** Display speedometer in racing game, check if object has stopped moving, trigger effects at high speeds. **Acceptance criteria:** Correctly display total speed, explain difference from x/y speed components.

Dependencies:
* T16.G5.06: Attach a dynamic body to a sprite
* T16.G5.08: Apply an impulse to jump or push


ID: T16.G5.14
Topic: T16 – 2D Motion & Physics
Skill: Compare manual vs engine approaches side-by-side (capstone)
Description: Build two versions of the same simple physics behavior (bouncing ball or platformer jump): one using manual velocity variables (Track A approach) and one using the physics engine (Track B approach). Compare code complexity, performance, realism, and control for each approach. **Deliverable:** Side-by-side demonstration with written comparison explaining strengths and weaknesses of each approach. **Acceptance criteria:** Both versions implemented correctly, comparison covers 4+ dimensions, recommendations for when to use each approach provided.

Dependencies:
* T16.G5.04: Code a manual bounce with energy loss
* T16.G5.12: Choose manual vs engine-based physics
* T16.G5.10: Trace simple 2D physics motion


<!-- X-2 VIOLATION NOTE: Several G6-G7 skills below have cross-topic dependencies on T07/T08/T09.G3 skills,
     creating 3-4 grade gaps. This is acceptable since they are cross-topic dependencies (not within-topic)
     and will be addressed in Phase 2 cross-topic dependency optimization. The skills are properly scaffolded
     within T16 itself. -->




ID: T16.G6.01
Topic: T16 – 2D Motion & Physics
Skill: Configure surface friction parameters
Description: Adjust the friction percentage using `update density [value] friction [value]% restitution [value]%` and measure how far objects slide on different surfaces. Map friction values to sliding distances through systematic testing. **Acceptance criteria:** Friction experiment completed, data table shows friction vs distance relationship.

Dependencies:
* T16.G5.09.01: Configure friction percentage for sliding control
* T16.G5.10: Trace simple 2D physics motion




ID: T16.G6.02
Topic: T16 – 2D Motion & Physics
Skill: Control restitution (bounce) parameters
Description: Modify the restitution percentage and measure bounce heights. Learn the relationship between restitution values (0-100%) and energy conservation in collisions: 0% = no bounce, 100% = full bounce. **Acceptance criteria:** Restitution experiment completed, bounce height graph shows linear relationship.

Dependencies:
* T16.G5.09.02: Configure restitution percentage for bounce control
* T16.G6.01: Configure surface friction parameters


ID: T16.G6.02.01
Topic: T16 – 2D Motion & Physics
Skill: Set velocity directly for physics bodies
Description: Use `set x speed [value]`, `set y speed [value]`, and `set speed [value] in direction [angle]` to directly control physics body velocity. Compare direct velocity setting to impulses and understand when each approach is appropriate. **Guidelines:** Use direct velocity for instant speed changes, teleports, or capping max speed. Use impulses for physics-realistic acceleration. **Acceptance criteria:** Demonstrate both methods, explain appropriate use cases.

Dependencies:
* T16.G5.06: Attach a dynamic body to a sprite
* T16.G5.08: Apply an impulse to jump or push


ID: T16.G6.02.01.01
Topic: T16 – 2D Motion & Physics
Skill: Maintain constant speed in current direction
Description: Use `set speed [value] in moving direction` to regulate an object's speed without changing its trajectory. This is useful for maintaining constant character movement speed, limiting maximum velocity, or normalizing physics-driven velocities while preserving direction changes from collisions or forces. **Acceptance criteria:** Speed clamped successfully, direction preserved through collisions.

Dependencies:
* T16.G6.02.01: Set velocity directly for physics bodies


ID: T16.G6.02.01.02
Topic: T16 – 2D Motion & Physics
Skill: Read velocity reporters for verification
Description: Use velocity reporter blocks (`(x speed)`, `(y speed)`, `(speed)`) to read and verify the current velocity of a physics body. Learn to check if velocity changes worked as expected, essential for debugging motion issues. **Acceptance criteria:** Velocity values read correctly, used to verify expected behavior in script.

Dependencies:
* T16.G6.02.01: Set velocity directly for physics bodies


ID: T16.G6.02.01.03
Topic: T16 – 2D Motion & Physics
Skill: Set rotation speed directly
Description: Use `set rotation speed [value]` to directly control how fast a physics body spins (degrees per second). Understand this gives immediate rotation control, parallel to setting linear velocity. **Acceptance criteria:** Rotation speed set correctly, predictable spinning behavior demonstrated.

Dependencies:
* T16.G6.02.01: Set velocity directly for physics bodies


ID: T16.G6.02.02
Topic: T16 – 2D Motion & Physics
Skill: Compare dynamic vs movable body types
Description: Compare dynamic bodies (affected by forces and gravity) with movable (kinematic) bodies (move via velocity but don't respond to forces). Identify scenarios where each type is appropriate: dynamic for player characters and falling objects, movable for moving platforms and elevators. **Acceptance criteria:** Correctly identify body type for 5+ scenarios, explain reasoning.

Dependencies:
* T16.G5.06: Attach a dynamic body to a sprite
* T16.G6.02.01: Set velocity directly for physics bodies




ID: T16.G6.03
Topic: T16 – 2D Motion & Physics
Skill: Build a movable (kinematic) moving platform
Description: Create a platform using `behave as a [movable] [object]` that moves on a fixed path while still colliding with players. Use `set x speed` and `set y speed` to control platform motion directly rather than relying on physics forces. **Acceptance criteria:** Platform moves on path, carries player correctly, doesn't respond to gravity or impulses.

Dependencies:
* T07.G3.05: Fix a simple repeat loop count
* T16.G6.02.02: Compare dynamic vs movable body types




ID: T16.G6.04
Topic: T16 – 2D Motion & Physics
Skill: Detect collisions for scoring or triggers
Description: Use `broadcast [message] when colliding with [sprite]` to listen for collision events between sprites. Run scoring or state-change scripts in response to collisions (player hits coin, ball hits bumper). **Acceptance criteria:** Collision detection triggers score change or state transition correctly.

Dependencies:
* T06.G4.01: Use multiple event handlers in the same sprite
* T16.G5.10: Trace simple 2D physics motion


ID: T16.G6.04.01
Topic: T16 – 2D Motion & Physics
Skill: Detect collision end events
Description: Use `broadcast [message] when finish colliding with [sprite]` to trigger actions when objects stop touching. Understand collision end events are essential for: stopping lava damage when leaving fire, releasing pressed buttons, tracking exit from trigger zones, and any scenario needing 'when objects separate' detection. **Acceptance criteria:** End-collision event triggers action correctly, difference from start-collision understood.

Dependencies:
* T16.G6.04: Detect collisions for scoring or triggers


ID: T16.G6.04.02
Topic: T16 – 2D Motion & Physics
Skill: Enable ground detection for jump control
Description: Enable ground detection using `turn on ground detection within distance [value] debug [Yes/No]` and use the `<in collision below>` reporter in conditionals to allow jumping only when the sprite is standing on ground. This prevents mid-air double jumps and creates responsive platformer controls. **Acceptance criteria:** Jump only works when grounded, no double-jumping possible.

Dependencies:
* T16.G6.04: Detect collisions for scoring or triggers


ID: T16.G6.04.02.01
Topic: T16 – 2D Motion & Physics
Skill: Use ground slope reporter for inclined surfaces
Description: Use the `(ground slope)` reporter to read the angle of the surface beneath a sprite. Adjust sprite behavior on slopes and ramps by detecting whether the character is on flat ground (0 degrees), uphill (positive), or downhill (negative), enabling features like sliding down steep slopes or adjusting movement speed on inclines. **Acceptance criteria:** Slope angle read correctly, behavior changes based on slope angle.

Dependencies:
* T16.G6.04.02: Enable ground detection for jump control


ID: T16.G6.04.03
Topic: T16 – 2D Motion & Physics
Skill: Identify collision management needs
Description: Analyze a game design (with multiple object types like players, enemies, collectibles, hazards, and platforms) and identify which objects should collide with each other and which should pass through. Plan collision filtering strategy before implementing collision groups. **Acceptance criteria:** Collision matrix created showing all object type pairs, pass-through vs collide decision for each.

Dependencies:
* T16.G6.04: Detect collisions for scoring or triggers


ID: T16.G6.04.04
Topic: T16 – 2D Motion & Physics
Skill: Build trigger zones and collectibles with sensor bodies
Description: Combine sensor bodies with collision events to create functional game elements. **Examples:** (1) Checkpoint zone that saves player progress when entered, (2) collectible coins that add score and hide when touched, (3) danger zone that triggers damage without blocking movement. The sensor detects entry but doesn't physically block the player. **Acceptance criteria:** All three example types implemented and working correctly.

Dependencies:
* T16.G5.06.02: Create sensor bodies for trigger zones
* T16.G6.04: Detect collisions for scoring or triggers


ID: T16.G6.04.05
Topic: T16 – 2D Motion & Physics
Skill: Create one-way platforms using collision filtering
Description: Build platforms that players can jump through from below but land on from above. **Implementation:** (1) Create platform as movable/fixed body, (2) use ground detection to check if player is above platform, (3) disable collision when player below, enable when player above and falling. **Alternative approach:** Use collision groups to selectively enable/disable platform collision based on player position. **Acceptance criteria:** One-way platform works correctly, player can jump through from below and land from above.

Dependencies:
* T16.G6.04.02: Enable ground detection for jump control
* T16.G6.04: Detect collisions for scoring or triggers




ID: T16.G6.05
Topic: T16 – 2D Motion & Physics
Skill: Add sprites to collision groups
Description: Assign group numbers to sprites using `add to collision group [G]` to categorize physics objects. Understand that collision groups are the foundation for collision filtering and that sprites can belong to multiple groups simultaneously. **Acceptance criteria:** Sprites assigned to groups correctly, multiple group membership understood.

Dependencies:
* T16.G6.04.03: Identify collision management needs


ID: T16.G6.05.01
Topic: T16 – 2D Motion & Physics
Skill: Enable collision filtering with other groups
Description: Configure collision filters using `enable collision with group [G]` and `disable collision with group [G]` to specify which groups a sprite should collide with. Understand that filters are directional and must be set on BOTH sprites for mutual pass-through behavior. **Acceptance criteria:** Collision filtering works correctly, bidirectional requirement understood.

Dependencies:
* T16.G6.05: Add sprites to collision groups


ID: T16.G6.05.02
Topic: T16 – 2D Motion & Physics
Skill: Test collision group filtering behavior
Description: Test collision group setups by running the game and verifying that objects pass through or collide as expected. Debug filtering issues by checking that groups are assigned correctly, filters are bidirectional, and objects without group assignments collide with everything by default. **Acceptance criteria:** All collision behaviors match design, filtering bugs identified and fixed.

Dependencies:
* T16.G6.05.01: Enable collision filtering with other groups


ID: T16.G6.05.03
Topic: T16 – 2D Motion & Physics
Skill: Dynamically modify collision groups at runtime
Description: Dynamically add or remove collision group memberships during gameplay (e.g., for invincibility, phasing) using `add to collision group [G]` and `remove from collision group [G]`. **Example use cases:** Player invincibility after hit, ghost mode power-up, phase-shifting mechanics. **Acceptance criteria:** Runtime group changes work correctly, gameplay uses demonstrated.

Dependencies:
* T16.G6.05.02: Test collision group filtering behavior


ID: T16.G6.05.04
Topic: T16 – 2D Motion & Physics
Skill: Use dominance groups for one-way pushing
Description: Use `set dominance group to [G]` to create one-way physical interactions where higher-dominance objects push lower-dominance objects without being pushed back. Apply this to create boss characters that can't be knocked back by players, heavy objects that push light ones, or unstoppable moving hazards. **Acceptance criteria:** Dominance demonstrated with boss that pushes player without being pushed.

Dependencies:
* T16.G6.05.02: Test collision group filtering behavior




ID: T16.G6.06
Topic: T16 – 2D Motion & Physics
Skill: Blend manual and engine sprites in a level
Description: Create a project that combines manual motion (scrolling backgrounds, UI elements, non-physics objects) with physics bodies (falling objects, player characters) running simultaneously. **Success criteria:** Manual sprites move smoothly without physics interference, physics sprites respond to gravity and collisions correctly, and no unintended physics bodies are created. **Acceptance criteria:** Mixed project works correctly, no interference between systems.

Dependencies:
* T16.G5.10: Trace simple 2D physics motion
* T16.G5.11: Debug missing physics setup


ID: T16.G6.06.01
Topic: T16 – 2D Motion & Physics
Skill: Lock movement or rotation of physics bodies
Description: Use `prevent body movement from forces [Yes]` and `prevent body rotation from forces [Yes]` to constrain physics objects. Create characters that stay upright, platforms that resist being pushed, or objects that only rotate without moving. **Acceptance criteria:** Constraints applied correctly, constrained bodies behave as expected under forces.

Dependencies:
* T16.G5.06: Attach a dynamic body to a sprite




ID: T16.G6.07
Topic: T16 – 2D Motion & Physics
Skill: Debug unstable physics behavior
Description: Diagnose why a sprite jitters, sinks through a platform, or flies off-screen (e.g., density too low, conflicting impulses, missing collision groups) and adjust parameters to stabilize the scene. **Common causes:** too-high forces, too-small collision shapes, missing fixed bodies, tunneling (solved with CCD). **Acceptance criteria:** Unstable behavior identified, root cause diagnosed, fix applied successfully.

Dependencies:
* T16.G6.01: Configure surface friction parameters
* T16.G6.02: Control restitution (bounce) parameters


ID: T16.G6.07.01
Topic: T16 – 2D Motion & Physics
Skill: Configure world border properties
Description: Set physics world border properties (friction and restitution). Use `set world border collider friction [value]% restitution [value]%` to control how sprites bounce and slide when hitting stage edges, creating realistic boundary behavior without manual edge detection. **Acceptance criteria:** Border friction and restitution configured, edge behavior matches design intent.

Dependencies:
* T16.G5.05: Initialize a 2D physics world
* T16.G6.01: Configure surface friction parameters


ID: T16.G6.07.02
Topic: T16 – 2D Motion & Physics
Skill: Configure world borders for wrap-around or open-edge levels
Description: Set physics world border collision groups. Use `set world border collision group [G] colliding with group [G]` to configure whether certain sprites or groups can collide with stage borders, enabling scenarios where some objects pass through edges while others bounce. **Acceptance criteria:** Group-based border collision works, pass-through and bounce behaviors configured correctly.

Dependencies:
* T16.G6.07.01: Configure world border properties




ID: T16.G6.08
Topic: T16 – 2D Motion & Physics
Skill: Compare simulations to real-world motion
Description: Record bounce heights or slide distances in CreatiCode, compare them to expected real-world results, and discuss how closely the simulation matches reality and what simplifications the physics engine makes. **Acceptance criteria:** Real vs simulated comparison completed, engine limitations identified and explained.

Dependencies:
* T16.G5.10: Trace simple 2D physics motion


ID: T16.G6.08.01
Topic: T16 – 2D Motion & Physics
Skill: Build a pinball-style bumper using collision and impulse response
Description: Create a bumper sprite that detects collisions with a ball and applies an outward impulse to push the ball away. **Implementation:** (1) Create fixed bumper body, (2) use `broadcast [bounce] when colliding with [Ball]`, (3) in Ball sprite, receive broadcast and `apply impulse [150] in direction [away from bumper]`, (4) add visual/sound feedback. **Acceptance criteria:** Bumper pushes ball away realistically, impulse direction calculated from bumper position, visual/sound effects added.

Dependencies:
* T16.G6.04: Detect collisions for scoring or triggers
* T16.G5.08: Apply an impulse to jump or push


ID: T16.G6.09
Topic: T16 – 2D Motion & Physics
Skill: Use screen shake for collision impact effects
Description: Implement screen shake effects when high-speed collisions occur to enhance impact feedback. **Implementation:** (1) Detect collision events, (2) check collision velocity using velocity reporters, (3) if speed > threshold, apply random camera offset for several frames, (4) gradually reduce shake intensity. **Example use cases:** Ball hitting wall at high speed, car crashes, explosions. **Acceptance criteria:** Screen shake triggers on hard impacts, intensity scales with collision force, effect feels satisfying.

Dependencies:
* T16.G6.04: Detect collisions for scoring or triggers
* T16.G6.02.01.02: Read velocity reporters for verification


ID: T16.G6.09.01
Topic: T16 – 2D Motion & Physics
Skill: Create particle burst effect on high-speed collision
Description: Create a visual particle burst effect that triggers when collision velocity exceeds a threshold. **Implementation:** (1) Use velocity reporters `(x speed)` and `(y speed)` to calculate collision speed, (2) when speed > threshold, spawn 5-10 particle clones, (3) apply random impulses to particles, (4) fade particles out. **Acceptance criteria:** Particle effect triggers only on high-speed collisions, particles scatter realistically, effect enhances visual feedback.

Dependencies:
* T16.G6.08: Compare simulations to real-world motion
* T16.G5.08: Apply an impulse to jump or push


ID: T16.G6.10
Topic: T16 – 2D Motion & Physics
Skill: Predict collision outcomes before running simulation
Description: Given a physics scenario setup (two objects with known mass, velocity, and collision angle), predict the outcome before running the simulation. **Process:** (1) Analyze initial conditions (which is heavier? which is faster?), (2) predict post-collision velocities and directions using physics intuition, (3) run simulation, (4) compare prediction to actual outcome, (5) explain any differences. **Acceptance criteria:** Predictions made for 3+ scenarios, reasoning explained, simulation results compared to predictions.

Dependencies:
* T16.G5.09: Configure density for mass control
* T16.G6.02.01.02: Read velocity reporters for verification


ID: T16.G6.11
Topic: T16 – 2D Motion & Physics
Skill: Debug sprites passing through walls (tunneling diagnosis)
Description: Diagnose and fix "tunneling" where fast-moving sprites pass through thin walls. **Diagnostic process:** (1) Identify symptoms (sprite appears on other side of wall), (2) check sprite speed using velocity reporters, (3) check wall thickness vs sprite speed, (4) apply fixes: enable CCD, increase wall thickness, or reduce max speed. **Acceptance criteria:** Tunneling bug identified, root cause explained (speed vs wall thickness), appropriate fix applied.

Dependencies:
* T16.G6.07: Debug unstable physics behavior
* T16.G6.02.01.02: Read velocity reporters for verification




ID: T16.G7.01
Topic: T16 – 2D Motion & Physics
Skill: Launch a configurable projectile
Description: Create a launcher where users set angle and power using sliders. The projectile receives an initial impulse using `apply impulse [force] in direction [angle]` that produces a parabolic arc toward targets. **Acceptance criteria:** Sliders control launch angle and power, projectile follows realistic arc, targets hittable with correct settings.

Dependencies:
* T08.G5.01: Fix a condition that uses the wrong operator
* T04.G5.02: Identify accumulator patterns in code (sum/concatenate)
* T16.G5.08: Apply an impulse to jump or push
* T16.G6.04: Detect collisions for scoring or triggers


ID: T16.G7.01.01
Topic: T16 – 2D Motion & Physics
Skill: Point sprite in movement direction
Description: Use `point in direction of speed` to automatically rotate a sprite to face its current movement direction. This is essential for arrows, rockets, and birds that should visually align with their trajectory as they fly along parabolic arcs. **Acceptance criteria:** Sprite rotates to match velocity direction throughout flight.

Dependencies:
* T16.G7.01: Launch a configurable projectile


ID: T16.G7.01.02
Topic: T16 – 2D Motion & Physics
Skill: Enable CCD for fast projectiles
Description: Enable Continuous Collision Detection (CCD) using `enable collision detection as a fast object [Yes]` to prevent fast-moving objects from tunneling through walls. Observe that very fast physics bodies sometimes pass through thin obstacles (called 'tunneling'), then learn CCD solves this by detecting collisions between frames, ensuring no missed collisions at high speeds. **Acceptance criteria:** CCD enabled, fast projectile no longer tunnels through thin walls.

Dependencies:
* T16.G7.01: Launch a configurable projectile


ID: T16.G7.01.03
Topic: T16 – 2D Motion & Physics
Skill: Calculate optimal launch angle for target distance
Description: Experiment with different launch angles to find the optimal angle for maximum distance or hitting a specific target. **Process:** (1) Set up target at known distance, (2) test angles from 15° to 75° in 15° increments, (3) record which angle hits target or goes farthest, (4) refine angle in smaller increments near optimal, (5) explain why 45° is often optimal for maximum range. **Acceptance criteria:** Data collected for 5+ angles, optimal angle identified, relationship between angle and distance explained.

Dependencies:
* T16.G7.01: Launch a configurable projectile




ID: T16.G7.02
Topic: T16 – 2D Motion & Physics
Skill: Combine multiple forces simultaneously
Description: Use `add force [force] in direction [angle]` to apply two or more forces in the same frame (gravity + constant wind, gravity + player thrust). Predict and observe the resulting curved motion paths. **Acceptance criteria:** Multiple forces combined correctly, resulting trajectory matches prediction, force vectors understood.

Dependencies:
* T16.G5.08.03: Apply a single continuous force
* T16.G6.07: Debug unstable physics behavior
* T16.G6.08: Compare simulations to real-world motion


ID: T16.G7.02.01
Topic: T16 – 2D Motion & Physics
Skill: Clear forces and torques from physics bodies
Description: Use `remove all forces` and `remove all torques` to reset accumulated forces on physics bodies. Use this for game resets, mode transitions, or when switching from force-driven to velocity-driven control. **Acceptance criteria:** Forces cleared successfully, clean state transitions demonstrated.

Dependencies:
* T16.G7.02: Combine multiple forces simultaneously


ID: T16.G7.02.02
Topic: T16 – 2D Motion & Physics
Skill: Apply force at a position for continuous rotation
Description: Use `add force [force] in direction [angle] at position x [X] y [Y]` to apply continuous off-center forces. Observe how sustained forces applied away from center create continuous rotation (torque), useful for thrusters, spinning mechanisms, or torque-based controls. **Acceptance criteria:** Off-center force creates rotation, torque effect controlled and predictable.

Dependencies:
* T16.G5.08.02: Apply impulse at a position for rotation
* T16.G7.02: Combine multiple forces simultaneously




ID: T16.G7.03
Topic: T16 – 2D Motion & Physics
Skill: Simulate drag with manual force calculations
Description: Manually implement drag effects by calculating forces opposite to velocity (applying force proportional to speed in the reverse direction). Experiment with different drag coefficients and observe how they affect motion through different media (air, water, honey). This manual approach builds understanding before using built-in damping. **Acceptance criteria:** Manual drag implemented, different media simulated, drag coefficient effect understood.

Dependencies:
* T16.G5.08.01: Distinguish forces from impulses
* T16.G6.07: Debug unstable physics behavior


ID: T16.G7.03.01
Topic: T16 – 2D Motion & Physics
Skill: Use built-in damping as alternative to manual drag
Description: Use the built-in `set damping factor for movement [M]% rotation [R]%` block to simulate air resistance or water friction as an easier alternative to manual force calculations. Compare results with manual implementation and tune damping percentages for desired slowdown behavior. **Acceptance criteria:** Damping configured correctly, comparison with manual drag completed, trade-offs understood.

Dependencies:
* T16.G7.03: Simulate drag with manual force calculations




ID: T16.G7.04
Topic: T16 – 2D Motion & Physics
Skill: Build chains or stacks of physics objects
Description: Create stacks of boxes or chains of linked sprites and explore how forces propagate through the system when one element is pushed. Observe how density affects collision outcomes. **Acceptance criteria:** Stack or chain built successfully, force propagation observed, density effects demonstrated.

Dependencies:
* T16.G6.07: Debug unstable physics behavior
* T16.G6.08: Compare simulations to real-world motion


ID: T16.G7.04.01
Topic: T16 – 2D Motion & Physics
Skill: Use continuous torque to rotate bodies
Description: Use `add torque [value]` to apply continuous rotational force to a physics body. Understand that torque (like force for linear motion) accumulates over time, respecting the body's rotational mass and creating smooth, physics-based rotation. Compare to direct rotation speed control. **Acceptance criteria:** Torque applied correctly, difference from direct rotation speed understood.

Dependencies:
* T16.G6.02.01.03: Set rotation speed directly
* T16.G7.02: Combine multiple forces simultaneously


ID: T16.G7.04.01.01
Topic: T16 – 2D Motion & Physics
Skill: Apply torque impulse for instant rotation
Description: Use `apply torque impulse [value]` to apply an instant rotational "kick" to a physics body. Understand that torque impulse (like linear impulse) applies immediately regardless of mass, perfect for one-time rotation events like hitting a spinning obstacle. **Acceptance criteria:** Torque impulse applied correctly, instant rotation vs continuous torque distinguished.

Dependencies:
* T16.G7.04.01: Use continuous torque to rotate bodies
* T16.G5.08.02: Apply impulse at a position for rotation




ID: T16.G7.05
Topic: T16 – 2D Motion & Physics
Skill: Read velocity and mass reporters
Description: Use the reporter blocks `(x speed)`, `(y speed)`, `(mass)`, `(angular speed)`, and `(ground slope)` to display real-time physics data on screen. Use this data for UI displays, conditional logic, and debugging. **Acceptance criteria:** All reporter types used correctly, data displayed in HUD or used in logic.

Dependencies:
* T16.G6.07: Debug unstable physics behavior
* T16.G6.08: Compare simulations to real-world motion


ID: T16.G7.05.01
Topic: T16 – 2D Motion & Physics
Skill: Instrument and graph motion data
Description: Record motion data from a sprite every few frames using velocity reporters, store values in lists, and create a graph. Use the graph to confirm constant acceleration or spot errors. **Acceptance criteria:** Data logged to list successfully, graph created, acceleration pattern confirmed or debugged.

Dependencies:
* T10.G5.01: Add and remove items from a list
* T16.G7.05: Read velocity and mass reporters


ID: T16.G7.05.02
Topic: T16 – 2D Motion & Physics
Skill: Use velocity reporters for UI speedometers and HUDs
Description: Create visual HUD elements that display real-time physics data. **Examples:** (1) Speedometer that shows `(speed)` as a number or visual gauge, (2) tachometer showing `(angular speed)` for rotating objects, (3) velocity indicator arrows pointing in direction of movement. Update HUD elements each frame to reflect current physics state. **Acceptance criteria:** All three HUD types implemented and updating correctly.

Dependencies:
* T16.G7.05: Read velocity and mass reporters




ID: T16.G7.06
Topic: T16 – 2D Motion & Physics
Skill: Model a real-world physics scenario
Description: Choose a real phenomenon (bouncing ball, swinging pendulum, sliding object) and build a CreatiCode simulation that approximates it. Explain which physics properties (gravity, friction, restitution) were tuned to mimic reality. **Acceptance criteria:** Simulation matches real-world behavior qualitatively, physics parameters justified.

Dependencies:
* T08.G5.01: Fix a condition that uses the wrong operator
* T04.G5.02: Identify accumulator patterns in code (sum/concatenate)
* T16.G6.08: Compare simulations to real-world motion


ID: T16.G7.06.01
Topic: T16 – 2D Motion & Physics
Skill: Validate simulation accuracy with known physics formulas
Description: Compare CreatiCode simulation results to predictions from known physics formulas (d=½gt², v=at, etc.). **Process:** (1) Choose a simple scenario (free fall), (2) predict results using formula, (3) measure actual simulation results, (4) calculate percent error, (5) explain any differences (frame rate, air resistance, rounding). **Acceptance criteria:** Formula prediction calculated correctly, simulation measured accurately, percent error calculated, differences explained.

Dependencies:
* T16.G7.06: Model a real-world physics scenario


ID: T16.G7.07
Topic: T16 – 2D Motion & Physics
Skill: Evaluate whether a simulation meets requirements
Description: Given target requirements (e.g., "ball must clear the second bumper but stop before the third"), test a simulation against them. Examine logged data and decide if requirements were met, citing evidence. **Acceptance criteria:** All requirements tested, pass/fail determined correctly, evidence cited from logs or observations.

Dependencies:
* T16.G6.07: Debug unstable physics behavior
* T16.G6.08: Compare simulations to real-world motion


ID: T16.G7.07.01
Topic: T16 – 2D Motion & Physics
Skill: Create acceptance test cases for physics requirements
Description: Given physics-based game requirements, write specific test cases with pass/fail criteria. **Example requirement:** "Player must be able to jump over a 100-unit wall." **Test case:** (1) Place player at wall base, (2) trigger jump with max power, (3) measure max height reached, (4) pass if height > 100. Create 5+ test cases for a game feature. **Acceptance criteria:** Test cases are specific and measurable, cover normal and edge cases, include pass/fail criteria.

Dependencies:
* T16.G7.07: Evaluate whether a simulation meets requirements


ID: T16.G7.08
Topic: T16 – 2D Motion & Physics
Skill: Create a physics-based sports game
Description: Design and implement a sports game (basketball, golf, soccer) using physics mechanics. **Implementation:** (1) Configure gravity and restitution for sport ball, (2) implement launch/kick mechanics with angle and power control, (3) create goal/target with collision detection, (4) add scoring system based on successful shots. **Examples:** Basketball with arc shots and backboard bounces, mini-golf with putting power control, soccer with kicked ball physics. **Acceptance criteria:** Sport mechanics feel realistic, scoring works correctly, game is playable and fun.

Dependencies:
* T16.G7.01: Launch a configurable projectile
* T16.G6.04: Detect collisions for scoring or triggers
* T16.G6.02: Control restitution (bounce) parameters


ID: T16.G7.09
Topic: T16 – 2D Motion & Physics
Skill: Trace physics simulation frame-by-frame
Description: Build a physics scenario and step through it frame-by-frame, recording position, velocity, and forces at each step. **Process:** (1) Set up simple physics scenario (falling ball), (2) pause simulation after each frame, (3) record current values in table, (4) manually predict next frame values, (5) step forward and verify predictions. **Purpose:** Understand that physics engines update in discrete steps, not continuous motion. **Acceptance criteria:** Frame-by-frame data recorded for 10+ frames, predictions made and verified, discrete time-step concept explained.

Dependencies:
* T16.G7.05: Read velocity and mass reporters
* T16.G6.07: Debug unstable physics behavior


ID: T16.G7.10
Topic: T16 – 2D Motion & Physics
Skill: Design a physics experiment to test a hypothesis
Description: Formulate a physics hypothesis (e.g., "doubling density doubles collision force"), design an experiment to test it, collect data, and conclude whether hypothesis is supported. **Process:** (1) State clear hypothesis, (2) design controlled experiment with independent/dependent variables, (3) run 5+ trials, (4) record data in table, (5) analyze results and draw conclusion. **Acceptance criteria:** Complete experimental design with hypothesis, controlled variables, data collection, and conclusion.

Dependencies:
* T16.G7.06: Model a real-world physics scenario
* T16.G7.05.01: Instrument and graph motion data




ID: T16.G8.01
Topic: T16 – 2D Motion & Physics
Skill: Design a physics-based arcade game concept
Description: Design a launcher + target game (Angry Birds–style) by planning level layouts, identifying required physics objects (projectiles, targets, obstacles), and sketching game mechanics. Create design documents that specify win conditions and challenge progression before implementation. **Acceptance criteria:** Complete design document with sketches, object list, mechanics description, and win conditions.

Dependencies:
* T16.G7.06: Model a real-world physics scenario


ID: T16.G8.01.01
Topic: T16 – 2D Motion & Physics
Skill: Implement physics arcade game mechanics
Description: Implement the game design from T16.G8.01 by creating sprites, setting up physics bodies, configuring collision detection, and scripting game logic. Translate design specifications into working code using physics blocks. **Acceptance criteria:** All designed mechanics implemented, game playable from start to win condition.

Dependencies:
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps
* T16.G8.01: Design a physics-based arcade game concept
* T04.G6.01: Group snippets by underlying algorithm pattern
* T10.G6.01: Sort a table by a column


ID: T16.G8.01.02
Topic: T16 – 2D Motion & Physics
Skill: Balance and tune physics game difficulty
Description: Playtest physics game and adjust physics parameters (gravity, impulse strength, object density, friction, restitution) to balance difficulty. Iterate on parameter values to make gameplay fair but challenging, ensuring levels are neither too easy nor frustratingly hard. **Acceptance criteria:** Game difficulty balanced through playtesting, parameter changes justified, target win rate achieved.

Dependencies:
* T16.G8.01.01: Implement physics arcade game mechanics




ID: T16.G8.02
Topic: T16 – 2D Motion & Physics
Skill: Implement fixed joints for connected objects
Description: Use `fix relative position to [sprite]` to weld sprites together so they move as a single rigid unit, and `remove relative position constraint` to break the connection. **Examples:** compound objects (car with wheels), multi-part characters (robot with detachable arms), towed vehicles that can be detached mid-game. Fixed joints are useful when objects should move as one rigid body. **Acceptance criteria:** Fixed joint created, compound object behaves as single unit, detachment works.

Dependencies:
* T16.G7.06: Model a real-world physics scenario
* T16.G7.04: Build chains or stacks of physics objects


ID: T16.G8.02.01
Topic: T16 – 2D Motion & Physics
Skill: Implement revolute joints for hinges
Description: Use `set [sprite] as rotation axis with offset x [X] y [Y]` to create hinged objects like doors, seesaws, and pendulums. Configure rotation behavior with `set rotation axis speed [S] damping factor [D]%`, and use `remove rotation axis` to disconnect hinges. **Examples:** swinging doors, seesaw balance puzzles, pendulum clocks, catapult arms. Revolute joints allow rotation around a fixed point. **Acceptance criteria:** Hinge joint created, rotation constrained to axis, motor control demonstrated if applicable.

Dependencies:
* T16.G8.02: Implement fixed joints for connected objects
* T16.G7.04.01: Use continuous torque to rotate bodies


ID: T16.G8.02.01.01
Topic: T16 – 2D Motion & Physics
Skill: Control revolute joint motors with speed and damping
Description: Control revolute joint motors using `set rotation axis speed [S] damping factor [D]%` to create powered rotations like fans or wheels. Balance speed for rotation rate and damping for resistance, creating smooth or snappy rotation behaviors. **Examples:** motorized windmill, spinning platform, rotating obstacle in a game. **Acceptance criteria:** Motor speed and damping configured, rotation behavior controllable and predictable.

Dependencies:
* T16.G8.02.01: Implement revolute joints for hinges


ID: T16.G8.02.02
Topic: T16 – 2D Motion & Physics
Skill: Implement prismatic joints for sliding
Description: Use `allow [Horizontal/Vertical] sliding relative to [sprite] range from [min] to [max]` to create pistons, sliding doors, and spring-loaded platforms with configurable movement limits. **Examples:** elevator platform that slides vertically, piston in a machine, sliding puzzle pieces. **Note:** Prismatic joints are permanent once created; plan constraint usage during the design phase. **Acceptance criteria:** Sliding joint created, movement constrained to range, sliding behavior smooth.

Dependencies:
* T16.G8.02: Implement fixed joints for connected objects


ID: T16.G8.02.03
Topic: T16 – 2D Motion & Physics
Skill: Debug joint constraint issues
Description: Diagnose and fix common joint problems such as joints separating under force, rotation limits not working correctly, or motors behaving unpredictably. Adjust joint parameters, verify anchor positions, and test constraint behavior systematically. **Acceptance criteria:** Joint bug identified, root cause diagnosed, fix applied successfully.

Dependencies:
* T16.G8.02.01: Implement revolute joints for hinges
* T16.G8.02.02: Implement prismatic joints for sliding




ID: T16.G8.03
Topic: T16 – 2D Motion & Physics
Skill: Build automated physics regression tests
Description: Create scripts that spawn test objects, run the simulation for a set time, and assert that positions, velocities, or collision counts stay within tolerances. **Process:** (1) Set up known initial conditions, (2) run physics for fixed frames, (3) check final state against expected values, (4) report pass/fail. This guards against regressions when modifying physics code. **Acceptance criteria:** Test script created, passes for correct physics, fails for broken physics.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T16.G7.07: Evaluate whether a simulation meets requirements
* T16.G7.05.01: Instrument and graph motion data




ID: T16.G8.04
Topic: T16 – 2D Motion & Physics
Skill: Identify physics performance bottlenecks
Description: Identify performance bottlenecks in a busy physics scene by observing frame rate and lag during playtesting. **Diagnostic process:** (1) Observe where lag occurs, (2) count active physics bodies, (3) check collision shape complexity, (4) review collision group settings. Physics performance depends on body count, shape complexity, and collision pair counts. **Acceptance criteria:** Bottleneck identified, contributing factors explained, measurement data provided.

Dependencies:
* T16.G7.06: Model a real-world physics scenario
* T16.G7.07: Evaluate whether a simulation meets requirements
* T16.G6.05.02: Test collision group filtering behavior


ID: T16.G8.04.01
Topic: T16 – 2D Motion & Physics
Skill: Optimize collision shapes for performance
Description: Implement shape optimizations by using simpler collision shapes (Box instead of Convex Hull), reducing active object count, using compound shapes sparingly, disabling unnecessary collision groups, and hiding debug overlays. **Optimization checklist:** (1) Use Box/Circle over Convex Hull, (2) limit active bodies to <50, (3) use collision groups to reduce pair checks, (4) disable debug mode in production. Verify improvements through repeated playtesting. **Acceptance criteria:** Optimizations applied, performance improvement measured, checklist completed.

Dependencies:
* T16.G8.04: Identify physics performance bottlenecks
* T16.G5.06.01.02: Use Convex Hull for sprite-fitted collision




ID: T16.G8.05
Topic: T16 – 2D Motion & Physics
Skill: Control gravity scale and time speed
Description: Use `set gravity scale [value]%` to create floaty zones (low gravity), reverse gravity areas (negative values), or heavy gravity zones. Use `set physics time speed [value]%` to create slow-motion effects (50%) or fast-forward (200%) for dramatic game moments. **Examples:** moon-gravity platformer levels, bullet-time effects, time-manipulation puzzles. **Acceptance criteria:** Gravity scale zones created, time speed effects implemented, gameplay enhanced by effects.

Dependencies:
* T16.G7.06: Model a real-world physics scenario
* T16.G5.05: Initialize a 2D physics world


ID: T16.G8.05.01
Topic: T16 – 2D Motion & Physics
Skill: Create gravity transition zones between areas
Description: Build zones that smoothly transition gravity between different values (normal gravity zone → low gravity zone → zero gravity zone). **Implementation:** (1) Create invisible sensor zones, (2) detect when player enters zone with collision broadcasts, (3) gradually change `set gravity scale` over 30-60 frames using interpolation, (4) test smooth transitions without jarring jumps. **Acceptance criteria:** Smooth gravity transitions implemented, no sudden physics jerks, player movement feels natural through transitions.

Dependencies:
* T16.G8.05: Control gravity scale and time speed
* T16.G5.06.02: Create sensor bodies for trigger zones


ID: T16.G8.06
Topic: T16 – 2D Motion & Physics
Skill: Use instrumentation data to tune difficulty
Description: Log player attempts (launch angle, power, success/fail), analyze the dataset, and retune physics parameters (gravity, impulse strength, target size) to achieve a desired win rate. **Process:** (1) Add logging for player actions, (2) collect 10+ playtests, (3) calculate success rate, (4) adjust physics parameters to reach target difficulty (e.g., 60% win rate), (5) re-test. Connect physics tweaks to game analytics. **Acceptance criteria:** Data logged successfully, analysis completed, parameters tuned to target win rate.

Dependencies:
* T16.G7.05.01: Instrument and graph motion data
* T16.G8.01.02: Balance and tune physics game difficulty




ID: T16.G8.07
Topic: T16 – 2D Motion & Physics
Skill: Plan a physics-based puzzle game
Description: Plan a physics puzzle game (pulleys, seesaws, Rube Goldberg machines) by identifying required physics mechanics, sketching level layouts, and defining puzzle solutions. Create design documents specifying which joints and physics properties each puzzle requires. **Acceptance criteria:** Complete puzzle game design document with mechanics list, level sketches, and solution descriptions.

Dependencies:
* T16.G8.02: Implement fixed joints for connected objects
* T16.G7.06: Model a real-world physics scenario


ID: T16.G8.07.01
Topic: T16 – 2D Motion & Physics
Skill: Select appropriate joints for puzzle mechanics
Description: Analyze puzzle game design and select the appropriate joint types (fixed, revolute, prismatic) for each puzzle element. Justify joint choices based on desired mechanical behavior and puzzle challenge design. **Acceptance criteria:** Joint types selected for all puzzle elements, choices justified clearly.

Dependencies:
* T16.G8.07: Plan a physics-based puzzle game
* T16.G8.02.01: Implement revolute joints for hinges
* T16.G8.02.02: Implement prismatic joints for sliding


ID: T16.G8.07.02
Topic: T16 – 2D Motion & Physics
Skill: Implement and test physics puzzle game
Description: Implement physics puzzle game by creating joints, configuring physics parameters, and scripting win conditions. **Development cycle:** (1) Build first puzzle with joints, (2) playtest for solvability, (3) adjust physics parameters, (4) add visual feedback for puzzle state, (5) iterate until solutions are discoverable. Good physics puzzles have clear mechanics and fair difficulty curves. **Acceptance criteria:** Puzzle game implemented, all puzzles solvable, difficulty curve appropriate.

Dependencies:
* T16.G8.07.01: Select appropriate joints for puzzle mechanics
* T16.G8.01.02: Balance and tune physics game difficulty


ID: T16.G8.08
Topic: T16 – 2D Motion & Physics
Skill: Design multi-level physics game with level progression
Description: Design a multi-level physics game with increasing difficulty and new mechanics introduced gradually. **Design process:** (1) Create level progression plan (easy→medium→hard), (2) introduce one new mechanic per 2-3 levels, (3) design tutorial levels for new mechanics, (4) plan difficulty curve using playtesting data, (5) create level transition system with save/load. **Acceptance criteria:** Complete level progression document with 8+ levels, difficulty curve planned, mechanics introduction schedule defined.

Dependencies:
* T16.G8.01.02: Balance and tune physics game difficulty
* T16.G8.07.02: Implement and test physics puzzle game


ID: T16.G8.09
Topic: T16 – 2D Motion & Physics
Skill: Implement object pooling for spawning many physics objects
Description: Implement object pooling to efficiently spawn and recycle many physics objects (projectiles, particles, collectibles) without performance degradation. **Implementation:** (1) Create pool of hidden clones at start, (2) when spawning needed, show and position a hidden clone, (3) when object destroyed, hide and return to pool instead of deleting, (4) reuse pooled objects for new spawns. **Benefits:** Avoids constant create/delete overhead, maintains stable frame rate with many objects. **Acceptance criteria:** Pool created with 20+ objects, spawn/recycle working correctly, performance stable with many active objects.

Dependencies:
* T16.G8.04.01: Optimize collision shapes for performance
* T16.G7.01: Launch a configurable projectile


ID: T16.G8.10
Topic: T16 – 2D Motion & Physics
Skill: Decompose complex physics behavior into testable sub-components
Description: Decompose complex physics behavior (e.g., vehicle physics, character controller, chain reaction puzzle) into independent testable sub-components. **Process:** (1) Identify core behaviors (movement, jumping, collision response), (2) create isolated test scene for each behavior, (3) verify each component works independently, (4) integrate components and test interactions, (5) debug integration issues. **Example:** Character controller decomposed into: ground detection test, jump force test, friction test, slope climbing test. **Acceptance criteria:** Complex behavior decomposed into 4+ testable components, each tested independently, integration completed successfully.

Dependencies:
* T16.G8.03: Build automated physics regression tests
* T16.G8.02.03: Debug joint constraint issues


ID: T16.G8.11
Topic: T16 – 2D Motion & Physics
Skill: Apply physics patterns to new game genres
Description: Identify physics patterns from existing games (launcher, platformer, puzzle, sports) and apply them to create a new game in a different genre. **Process:** (1) Analyze mechanics from 2+ existing physics games, (2) identify reusable patterns (projectile launch, collision scoring, force accumulation, joint constraints), (3) combine patterns in novel way for new genre, (4) prototype and playtest new combination. **Example:** Combine golf launch mechanics with puzzle game chain reactions to create golf-puzzle hybrid. **Acceptance criteria:** New game genre created using 3+ physics patterns from different sources, prototype demonstrates novel combination, gameplay is cohesive.

Dependencies:
* T16.G8.01.02: Balance and tune physics game difficulty
* T16.G8.07.02: Implement and test physics puzzle game
* T16.G7.08: Create a physics-based sports game


ID: T16.G8.11.01
Topic: T16 – 2D Motion & Physics
Skill: Document physics patterns as reusable templates
Description: Create documentation templates for common physics patterns that can be reused across projects. **Patterns to document:** (1) platformer character setup (body type, shape, density, friction), (2) bouncing ball configuration, (3) kinematic platform movement, (4) collision group setup for multi-layer games. **Template format:** Purpose, required blocks, parameter recommendations, common pitfalls. **Acceptance criteria:** 3+ physics patterns documented, templates include all necessary configuration details, tested by implementing pattern from template alone.

Dependencies:
* T16.G8.11: Apply physics patterns to new game genres


ID: T16.G8.12
Topic: T16 – 2D Motion & Physics
Skill: Create AI-controlled physics objects (enemy that aims projectiles)
Description: Build AI-controlled enemies that use physics to aim and launch projectiles at the player. **Implementation:** (1) Calculate angle from enemy to player position, (2) predict player movement trajectory, (3) calculate launch angle accounting for gravity and distance, (4) apply impulse in calculated direction, (5) add variation to make aiming imperfect but fair. **Acceptance criteria:** AI enemy aims at player, projectiles have realistic trajectories, aiming difficulty tunable, gameplay feels fair.

Dependencies:
* T16.G7.01: Launch a configurable projectile
* T16.G8.01.02: Balance and tune physics game difficulty


ID: T16.G8.13
Topic: T16 – 2D Motion & Physics
Skill: Use machine learning to optimize physics parameters
Description: Use iterative playtesting data to automatically tune physics parameters for target difficulty. **Process:** (1) Define target metrics (60% win rate, average 3 attempts), (2) run automated playtests with different parameter sets, (3) record success rates for each parameter combination, (4) identify parameter values that achieve target metrics, (5) verify through human playtesting. **Note:** This is simplified ML—systematically testing parameter space and selecting best performers. **Acceptance criteria:** Parameter optimization process completed, target metrics achieved, improvement over manual tuning demonstrated.

Dependencies:
* T16.G8.06: Use instrumentation data to tune difficulty
* T16.G8.03: Build automated physics regression tests


ID: T16.G8.14
Topic: T16 – 2D Motion & Physics
Skill: Implement procedural level generation with physics constraints
Description: Create a system that procedurally generates physics-based levels while ensuring they remain solvable. **Implementation:** (1) Define level template with variable positions, (2) randomly place platforms/obstacles within constraints, (3) verify path exists from start to goal using physics simulation, (4) if unsolvable, regenerate or adjust, (5) test generated levels for fairness. **Acceptance criteria:** Level generator creates 5+ unique solvable levels, physics constraints maintained, all levels playable and fair.

Dependencies:
* T16.G8.07.02: Implement and test physics puzzle game
* T16.G8.10: Decompose complex physics behavior into testable sub-components


ID: T16.G8.15
Topic: T16 – 2D Motion & Physics
Skill: Build adaptive difficulty using physics telemetry
Description: Implement adaptive difficulty that adjusts physics parameters based on player performance. **Implementation:** (1) Track player success rate over last 5 attempts, (2) if success rate < 40%, reduce difficulty (weaker gravity, larger targets, more impulse force), (3) if success rate > 80%, increase difficulty (stronger gravity, smaller targets, less force), (4) adjust gradually to avoid noticeable jumps, (5) display difficulty adjustments transparently. **Acceptance criteria:** Adaptive difficulty system working, adjustments based on data, player experience improved, difficulty changes feel fair.

Dependencies:
* T16.G8.06: Use instrumentation data to tune difficulty
* T16.G8.01.02: Balance and tune physics game difficulty
