ID: T17.K.01
Topic: T17 – 2D Motion & Physics
Skill: Observe sprite position changes (picture-based)
Description: Students watch animations of sprites moving and identify which sprite moved, matching before/after pictures. They recognize that "motion" means a sprite's position changes on the stage.

Dependencies:
None


ID: T17.K.02
Topic: T17 – 2D Motion & Physics
Skill: Match sprite to position after motion (picture-based)
Description: Students see a motion block sequence and choose which picture shows where the sprite will end up. They develop spatial reasoning by predicting final positions from simple motion sequences.

Dependencies:
* T17.K.01: Observe sprite position changes (picture-based)


ID: T17.G1.01
Topic: T17 – 2D Motion & Physics
Skill: Identify fast vs slow motion (picture-based)
Description: Students watch two sprite animations and identify which sprite moves faster. They compare motion speeds visually and describe motion using "fast" and "slow" vocabulary.

Dependencies:
* T17.K.02: Match sprite to position after motion (picture-based)


ID: T17.G2.01
Topic: T17 – 2D Motion & Physics
Skill: Predict sprite direction from motion blocks (picture choices)
Description: Students look at motion blocks (move 10 steps, turn right, move 10 steps) and choose from picture options showing which direction the sprite will move. They build directional intuition before coding.

Dependencies:
* T17.G1.01: Identify fast vs slow motion (picture-based)


ID: T17.G3.01
Topic: T17 – 2D Motion & Physics
Skill: Observe position changes from motion blocks
Description: Students observe how motion blocks (move, glide) change a sprite's position over time. They describe motion as "changing position" and predict where a sprite will be after motion blocks run.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T17.G2.01: Predict sprite direction from motion blocks (picture choices)


ID: T17.G3.02
Topic: T17 – 2D Motion & Physics
Skill: Predict direction and distance of sprite motion
Description: Students predict which direction a sprite will move and approximately how far, given a sequence of motion blocks. They develop intuition for motion before variables are introduced.

Dependencies:
* T17.G3.01: Observe position changes from motion blocks


ID: T17.G4.01
Topic: T17 – 2D Motion & Physics
Skill: Simulate falling with repeated motion
Description: Students create a simple falling animation by repeatedly moving a sprite down in a loop. They observe that the sprite appears to "fall" due to gravity conceptually, preparing them for velocity-based motion.

Dependencies:
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T07.G3.01: Use a counted repeat loop
* T17.G3.02: Predict direction and distance of sprite motion


ID: T17.G4.02
Topic: T17 – 2D Motion & Physics
Skill: Explain speed as position change over time
Description: Students explain that speed means "how much position changes each time the loop runs." They compare fast vs slow motion by changing the step size in a loop.

Dependencies:
* T01.G2.01: Find actions that repeat in everyday tasks
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T06.G2.03: Design a simple "if-then" game rule
* T09.G3.05: Trace code with variables to predict outcomes
* T17.G4.01: Simulate falling with repeated motion


ID: T17.G5.01
Topic: T17 – 2D Motion & Physics
Skill: Apply gravity to a sprite using 2D physics
Description: Students use the physics engine to apply gravity forces to a sprite, observing how it falls and accelerates naturally. They understand that gravity is a constant downward force that affects all dynamic physics bodies in the scene.

Dependencies:
* T17.G4.02: Explain speed as position change over time


ID: T17.G5.02
Topic: T17 – 2D Motion & Physics
Skill: Track gravity with velocity variables
Description: Students build a loop that stores a sprite's y-velocity in a variable, subtracts a gravity constant each frame, then adds the velocity to the sprite's y-position. This manual approach mirrors classic Scratch tutorials and prepares students for physics debugging.

Dependencies:
* T07.G3.05: Fix a simple repeat loop count
* T09.G3.05: Trace code with variables to predict outcomes
* T17.G5.01: Apply gravity to a sprite using 2D physics
* T08.G3.00: Identify if blocks in existing code


ID: T17.G5.03
Topic: T17 – 2D Motion & Physics
Skill: Use horizontal speed and friction variables
Description: Students add an x-velocity variable, respond to arrow keys to change it, and multiply by a friction factor (e.g., 0.9) each tick so motion glides to a stop. This prepares students for platformer mechanics.

Dependencies:
* T09.G4.03: Use multiple variables in a single script
* T17.G5.02: Track gravity with velocity variables
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code


ID: T17.G5.03.01
Topic: T17 – 2D Motion & Physics
Skill: Build a top-down vehicle with manual friction control
Description: Create a top-down car or spaceship game using manual friction variables to control movement

Dependencies:
* T17.G5.03: Use horizontal speed and friction variables


ID: T17.G5.04
Topic: T17 – 2D Motion & Physics
Skill: Code a manual bounce with energy loss
Description: Students write a conditional that checks for ground contact, multiplies the y-velocity by a negative damping factor (e.g., -0.6), and sends the sprite back up with reduced height. This cements physics vocabulary before using the engine's restitution.

Dependencies:
* T08.G3.01: Use a simple if in a script
* T17.G5.02: Track gravity with velocity variables


ID: T17.G5.04.01
Topic: T17 – 2D Motion & Physics
Skill: Create a simple platformer using manual gravity
Description: Build a basic platformer game using manual gravity and bounce calculations with velocity variables

Dependencies:
* T17.G5.04: Code a manual bounce with energy loss


ID: T17.G5.05
Topic: T17 – 2D Motion & Physics
Skill: Initialize a 2D physics world
Description: Students add the `initialize 2D physics world with gravity x [0] y [-100]` block, set appropriate gravity values, and confirm the debug overlay shows the world running. They understand that no physics behavior occurs until this block executes. Note: Running this block again resets the entire physics world, useful for level transitions or game resets.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T17.G4.02: Explain speed as position change over time
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name


ID: T17.G5.06
Topic: T17 – 2D Motion & Physics
Skill: Attach a dynamic body to a sprite
Description: Students convert a sprite to a dynamic physics body using `behave as a [dynamic] [object] shape [Box] debug [Yes]`. They observe the sprite fall and stop when it hits the stage floor, confirming the physics world affects it.

Dependencies:
* T17.G5.05: Initialize a 2D physics world


ID: T17.G5.06.A
Topic: T17 – 2D Motion & Physics
Skill: Practice creating multiple dynamic bodies
Description: Students create 2-3 different sprites and convert each to dynamic physics bodies. They experiment with different starting positions and observe how all bodies fall and interact, building fluency with the basic dynamic body setup before exploring shape options.

Dependencies:
* T17.G5.06: Attach a dynamic body to a sprite


ID: T17.G5.06.A.01
Topic: T17 – 2D Motion & Physics
Skill: Use debug mode to visualize collision shapes
Description: Enable debug mode in the 2D physics world to see invisible collision shape outlines overlaid on sprites. Students learn that debug mode helps understand why collisions happen or don't happen, by showing the actual physics boundaries independent of sprite appearance.

Dependencies:
* T17.G5.06.A: Practice creating multiple dynamic bodies


ID: T17.G5.06.01
Topic: T17 – 2D Motion & Physics
Skill: Choose Box vs Circle collision shapes
Description: Choose between Box and Circle collision shapes based on sprite appearance and desired physics behavior

Dependencies:
* T17.G5.06.A: Practice creating multiple dynamic bodies


ID: T17.G5.06.01.01
Topic: T17 – 2D Motion & Physics
Skill: Use Capsule shapes for elongated objects
Description: Students select Capsule collision shapes for elongated sprites (characters, vehicles, rods). They observe how Capsules provide smoother rolling and better collision response for pill-shaped objects compared to boxes, useful for character physics that should roll over obstacles without catching on edges.

Dependencies:
* T17.G5.06.01: Choose Box vs Circle collision shapes


ID: T17.G5.06.01.02
Topic: T17 – 2D Motion & Physics
Skill: Use Convex Hull for sprite-fitted collision
Description: Students apply Convex Hull collision shapes to create automatic collision boundaries that closely match sprite outlines. They understand that Convex Hull wraps the sprite's visible pixels with the smallest convex polygon, providing better visual accuracy than basic shapes but using more computational resources.

Dependencies:
* T17.G5.06.01: Choose Box vs Circle collision shapes


ID: T17.G5.06.02
Topic: T17 – 2D Motion & Physics
Skill: Create sensor bodies for trigger zones
Description: Students create sensor bodies using `behave as a [dynamic] [sensor]` that detect overlaps without causing physical collisions. They use sensors for trigger zones, collectible detection areas, and checkpoint markers.

Dependencies:
* T17.G5.06.01: Choose Box vs Circle collision shapes


ID: T17.G5.06.03
Topic: T17 – 2D Motion & Physics
Skill: Create compound shapes for complex sprites
Description: Students use `behave as a [dynamic] [object] in compound shape with curve tolerance [value] point distance [value]` to create physics bodies that match complex or concave sprite outlines. They understand the trade-off between accuracy and performance.

Dependencies:
* T17.G5.06.01: Choose Box vs Circle collision shapes


ID: T17.G5.07
Topic: T17 – 2D Motion & Physics
Skill: Build fixed boundaries for floors and walls
Description: Students add fixed physics bodies to floor or wall sprites using `behave as a [fixed] [object]` so falling or sliding objects stop on contact. They learn to use fixed bodies for geometry that should not move.

Dependencies:
* T17.G5.05: Initialize a 2D physics world


ID: T17.G5.08
Topic: T17 – 2D Motion & Physics
Skill: Apply an impulse to jump or push
Description: Students use `apply impulse [force] in direction [angle]` to make a dynamic sprite jump in response to input (e.g., direction 90 for upward jump). They control impulse strength so the sprite clears a target platform height.

Dependencies:
* T06.G4.01: Use multiple event handlers in the same sprite
* T17.G5.06: Attach a dynamic body to a sprite


ID: T17.G5.08.01
Topic: T17 – 2D Motion & Physics
Skill: Distinguish forces from impulses
Description: Students compare `add force [force] in direction [angle]` (applied continuously each frame) with `apply impulse [force] in direction [angle]` (applied once instantly). They use forces for sustained thrust (jetpack) and impulses for sudden actions (jump, kick).

Dependencies:
* T17.G5.08: Apply an impulse to jump or push


ID: T17.G5.08.02
Topic: T17 – 2D Motion & Physics
Skill: Apply impulse at a position for rotation
Description: Students use `apply impulse [force] in direction [angle] at position x [X] y [Y]` to apply off-center impulses. They observe how impulses applied away from center create instant rotation (torque), useful for hitting objects at an angle or creating spin effects.

Dependencies:
* T17.G5.08.01: Distinguish forces from impulses


ID: T17.G5.08.03
Topic: T17 – 2D Motion & Physics
Skill: Apply a single continuous force
Description: Students use `add force [force] in direction [angle]` to apply a single continuous force to a physics body (e.g., constant wind, jetpack thrust). They observe how continuous forces create sustained acceleration unlike one-time impulses, preparing them for combining multiple forces.

Dependencies:
* T17.G5.08.01: Distinguish forces from impulses


ID: T17.G5.09
Topic: T17 – 2D Motion & Physics
Skill: Configure density for mass control
Description: Students adjust density using `update density [value]` to control how heavy a sprite feels. They understand that density × area = mass and experiment with light vs heavy objects in collisions.

Dependencies:
* T17.G5.06: Attach a dynamic body to a sprite


ID: T17.G5.09.01
Topic: T17 – 2D Motion & Physics
Skill: Introduce friction percentage
Description: Students adjust the friction percentage parameter using `update density [value] friction [value]%` to control surface stickiness. They observe how friction affects sliding behavior and prepare for detailed friction experiments in G6.

Dependencies:
* T17.G5.09: Configure density for mass control


ID: T17.G5.09.02
Topic: T17 – 2D Motion & Physics
Skill: Introduce restitution percentage
Description: Students adjust the restitution percentage parameter using `update density [value] friction [value]% restitution [value]%` to control bounciness. They observe basic bounce behavior and prepare for systematic bounce height measurements in G6.

Dependencies:
* T17.G5.09.01: Introduce friction percentage


ID: T17.G5.10
Topic: T17 – 2D Motion & Physics
Skill: Trace simple 2D physics motion
Description: Students experiment with a physics simulation by adjusting gravity, density, and starting height values, then predict and verify where the sprite lands. They run the simulation, observe outcomes, and choose the correct statement about where the sprite ends up (e.g., "lands on the platform," "still in the air," "passed through the floor"). This hands-on prediction and testing builds physics intuition.

Dependencies:
* T09.G3.05: Trace code with variables to predict outcomes
* T17.G5.06: Attach a dynamic body to a sprite


ID: T17.G5.10.01
Topic: T17 – 2D Motion & Physics
Skill: Remove physics body from a sprite
Description: Students use `remove physics-based behavior` to detach a sprite from the physics engine so it no longer responds to gravity or collisions. They use this for collected items, destroyed enemies, or transitioning between physics and non-physics modes.

Dependencies:
* T17.G5.06: Attach a dynamic body to a sprite


ID: T17.G5.11
Topic: T17 – 2D Motion & Physics
Skill: Debug missing physics setup
Description: Students open a buggy project where the player never falls because the physics world was not initialized or the body was left as fixed. They inspect the scripts, identify the missing setup, and re-test.

Dependencies:
* T17.G5.06: Attach a dynamic body to a sprite
* T17.G5.07: Build fixed boundaries for floors and walls


ID: T17.G5.12
Topic: T17 – 2D Motion & Physics
Skill: Choose manual vs engine-based physics
Description: After experiencing both manual velocity variables (G5.02-G5.04) and the physics engine (G5.05-G5.11), students compare CreatiCode project briefs (platformer, UI animation, top-down maze, pinball machine) and choose the most appropriate approach for each. They justify their decision based on project requirements and their hands-on experience with both methods.

Dependencies:
* T05.G4.05: Plan a simulation with defined inputs and outputs
* T17.G5.04: Code a manual bounce with energy loss
* T17.G5.11: Debug missing physics setup


<!-- X-2 VIOLATION NOTE: Several G6-G7 skills below have cross-topic dependencies on T07/T08/T09.G3 skills,
     creating 3-4 grade gaps. This is acceptable since they are cross-topic dependencies (not within-topic)
     and will be addressed in Phase 2 cross-topic dependency optimization. The skills are properly scaffolded
     within T17 itself. -->

ID: T17.G6.01
Topic: T17 – 2D Motion & Physics
Skill: Configure surface friction parameters
Description: Students adjust the friction percentage using `update density [value] friction [value]% restitution [value]%` and measure how far objects slide on different surfaces. They learn to map friction values to sliding distances through systematic testing.

Dependencies:
* T17.G5.09.01: Introduce friction percentage
* T17.G5.10: Trace simple 2D physics motion


ID: T17.G6.02
Topic: T17 – 2D Motion & Physics
Skill: Control restitution (bounce) parameters
Description: Students modify the restitution percentage and measure bounce heights. They learn the relationship between restitution values (0-100%) and energy conservation in collisions: 0% = no bounce, 100% = full bounce.

Dependencies:
* T17.G5.09.02: Introduce restitution percentage
* T17.G6.01: Configure surface friction parameters


ID: T17.G6.02.01
Topic: T17 – 2D Motion & Physics
Skill: Set velocity directly for physics bodies
Description: Students use `set x speed [value]`, `set y speed [value]`, and `set speed [value] in direction [angle]` to directly control physics body velocity. They compare direct velocity setting to impulses and understand when each approach is appropriate.

Dependencies:
* T17.G5.06: Attach a dynamic body to a sprite
* T17.G5.08: Apply an impulse to jump or push


ID: T17.G6.02.01.02
Topic: T17 – 2D Motion & Physics
Skill: Read velocity reporters for verification
Description: Use velocity reporter blocks (x speed, y speed, speed) to read and verify the current velocity of a physics body. Students learn to check if velocity changes worked as expected, essential for debugging motion issues.

Dependencies:
* T17.G6.02.01: Set velocity directly for physics bodies


ID: T17.G6.02.01.03
Topic: T17 – 2D Motion & Physics
Skill: Set rotation speed directly
Description: Use 'physics set rotation speed' to directly control how fast a physics body spins (degrees per second). Students learn this gives immediate rotation control, parallel to setting linear velocity.

Dependencies:
* T17.G6.02.01: Set velocity directly for physics bodies


ID: T17.G6.02.01.01
Topic: T17 – 2D Motion & Physics
Skill: Maintain constant speed in current direction
Description: Students use `set speed [value] in moving direction` to regulate an object's speed without changing its trajectory. This is useful for maintaining constant character movement speed, limiting maximum velocity, or normalizing physics-driven velocities while preserving direction changes from collisions or forces.

Dependencies:
* T17.G6.02.01: Set velocity directly for physics bodies


ID: T17.G6.02.02
Topic: T17 – 2D Motion & Physics
Skill: Compare dynamic vs movable body types
Description: Students compare dynamic bodies (affected by forces and gravity) with movable (kinematic) bodies (move via velocity but don't respond to forces). They identify scenarios where each type is appropriate: dynamic for player characters and falling objects, movable for moving platforms and elevators.

Dependencies:
* T17.G5.06: Attach a dynamic body to a sprite
* T17.G6.02.01: Set velocity directly for physics bodies


ID: T17.G6.03
Topic: T17 – 2D Motion & Physics
Skill: Build a movable (kinematic) moving platform
Description: Students create a platform using `behave as a [movable] [object]` that moves on a fixed path while still colliding with players. They use `set x speed` and `set y speed` to control platform motion directly rather than relying on physics forces.

Dependencies:
* T07.G3.05: Fix a simple repeat loop count
* T17.G6.02.02: Compare dynamic vs movable body types


ID: T17.G6.04
Topic: T17 – 2D Motion & Physics
Skill: Detect collisions for scoring or triggers
Description: Students use `broadcast [message] when colliding with [sprite]` to listen for collision events between sprites. They run scoring or state-change scripts in response to collisions (player hits coin, ball hits bumper).

Dependencies:
* T06.G4.01: Use multiple event handlers in the same sprite
* T17.G5.10: Trace simple 2D physics motion


ID: T17.G6.04.01
Topic: T17 – 2D Motion & Physics
Skill: Detect collision end events
Description: Students use `broadcast [message] when finish colliding with [sprite]` to trigger actions when objects stop touching. Students learn collision end events are essential for: stopping lava damage when leaving fire, releasing pressed buttons, tracking exit from trigger zones, and any scenario needing 'when objects separate' detection.

Dependencies:
* T17.G6.04: Detect collisions for scoring or triggers


ID: T17.G6.04.02
Topic: T17 – 2D Motion & Physics
Skill: Enable ground detection for jump control
Description: Students enable ground detection using `enable ground detection [Yes]` and use the `(in collision below)` reporter in conditionals to allow jumping only when the sprite is standing on ground. This prevents mid-air double jumps and creates responsive platformer controls.

Dependencies:
* T17.G6.04: Detect collisions for scoring or triggers


ID: T17.G6.04.02.01
Topic: T17 – 2D Motion & Physics
Skill: Use ground slope reporter for inclined surfaces
Description: Students use the `(ground slope)` reporter to read the angle of the surface beneath a sprite. They adjust sprite behavior on slopes and ramps by detecting whether the character is on flat ground (0 degrees), uphill (positive), or downhill (negative), enabling features like sliding down steep slopes or adjusting movement speed on inclines.

Dependencies:
* T17.G6.04.02: Enable ground detection for jump control


ID: T17.G6.04.03
Topic: T17 – 2D Motion & Physics
Skill: Identify collision management needs
Description: Students analyze a game design (with multiple object types like players, enemies, collectibles, hazards, and platforms) and identify which objects should collide with each other and which should pass through. They plan collision filtering strategy before implementing collision groups.

Dependencies:
* T17.G6.04: Detect collisions for scoring or triggers


ID: T17.G6.04.04
Topic: T17 – 2D Motion & Physics
Skill: Build trigger zones and collectibles with sensor bodies
Description: Use sensor bodies to create trigger zones, checkpoints, and collectible items that detect without physical collision

Dependencies:
* T17.G5.06.02: Create sensor bodies for trigger zones
* T17.G6.04: Detect collisions for scoring or triggers


ID: T17.G6.05
Topic: T17 – 2D Motion & Physics
Skill: Add sprites to collision groups
Description: Students assign group numbers to sprites using `physics collision groups [group1, group2, ...]` to categorize physics objects. They understand that collision groups are the foundation for collision filtering and that sprites can belong to multiple groups simultaneously.

Dependencies:
* T17.G6.04.03: Identify collision management needs


ID: T17.G6.05.01
Topic: T17 – 2D Motion & Physics
Skill: Enable collision filtering with other groups
Description: Students configure collision filters using `physics add collision filter [group1, group2, ...]` to specify which groups a sprite should NOT collide with. They understand that filters are directional and must be set on BOTH sprites for mutual pass-through behavior.

Dependencies:
* T17.G6.05: Add sprites to collision groups


ID: T17.G6.05.02
Topic: T17 – 2D Motion & Physics
Skill: Test collision group filtering behavior
Description: Students test collision group setups by running the game and verifying that objects pass through or collide as expected. They debug filtering issues by checking that groups are assigned correctly, filters are bidirectional, and objects without group assignments collide with everything by default.

Dependencies:
* T17.G6.05.01: Enable collision filtering with other groups


ID: T17.G6.05.03
Topic: T17 – 2D Motion & Physics
Skill: Dynamically modify collision groups at runtime
Description: Dynamically add or remove collision group memberships during gameplay (e.g., for invincibility, phasing)

Dependencies:
* T17.G6.05.02: Test collision group filtering behavior


ID: T17.G6.05.04
Topic: T17 – 2D Motion & Physics
Skill: Use dominance groups for one-way pushing
Description: Students use dominance groups to create one-way physical interactions where higher-dominance objects push lower-dominance objects without being pushed back. They apply this to create boss characters that can't be knocked back by players, heavy objects that push light ones, or unstoppable moving hazards.

Dependencies:
* T17.G6.05.02: Test collision group filtering behavior


ID: T17.G6.06
Topic: T17 – 2D Motion & Physics
Skill: Blend manual and engine sprites in a level
Description: Students create a project that combines manual motion (scrolling backgrounds, UI elements, non-physics objects) with physics bodies (falling objects, player characters) running simultaneously. Success criteria: manual sprites move smoothly without physics interference, physics sprites respond to gravity and collisions correctly, and no unintended physics bodies are created.

Dependencies:
* T17.G5.10: Trace simple 2D physics motion
* T17.G5.11: Debug missing physics setup


ID: T17.G6.06.01
Topic: T17 – 2D Motion & Physics
Skill: Lock movement or rotation of physics bodies
Description: Students use `prevent body movement from forces [Yes]` and `prevent body rotation from forces [Yes]` to constrain physics objects. They create characters that stay upright, platforms that resist being pushed, or objects that only rotate without moving.

Dependencies:
* T17.G5.06: Attach a dynamic body to a sprite


ID: T17.G6.07
Topic: T17 – 2D Motion & Physics
Skill: Debug unstable physics behavior
Description: Students diagnose why a sprite jitters, sinks through a platform, or flies off-screen (e.g., density too low, conflicting impulses, missing collision groups) and adjust parameters to stabilize the scene.

Dependencies:
* T17.G6.01: Configure surface friction parameters
* T17.G6.02: Control restitution (bounce) parameters


ID: T17.G6.07.01
Topic: T17 – 2D Motion & Physics
Skill: Configure world border properties
Description: Set physics world border properties (friction and restitution). Students use 'physics world border friction' and 'physics world border restitution' blocks to control how sprites bounce and slide when hitting stage edges, creating realistic boundary behavior without manual edge detection.

Dependencies:
* T17.G5.05: Initialize a 2D physics world
* T17.G6.01: Configure surface friction parameters


ID: T17.G6.07.02
Topic: T17 – 2D Motion & Physics
Skill: Configure world borders for wrap-around or open-edge levels
Description: Set physics world border collision groups. Students use 'physics world border collision groups' block to configure whether certain sprites or groups can collide with stage borders, enabling scenarios where some objects pass through edges while others bounce.

Dependencies:
* T17.G6.07.01: Configure world border properties


ID: T17.G6.08
Topic: T17 – 2D Motion & Physics
Skill: Compare simulations to real-world motion
Description: Students record bounce heights or slide distances in CreatiCode, compare them to expected real-world results, and discuss how closely the simulation matches reality and what simplifications the physics engine makes.

Dependencies:
* T17.G5.10: Trace simple 2D physics motion


ID: T17.G7.01
Topic: T17 – 2D Motion & Physics
Skill: Launch a configurable projectile
Description: Students create a launcher where users set angle and power using sliders. The projectile receives an initial impulse using `apply impulse [force] in direction [angle]` that produces a parabolic arc toward targets.

Dependencies:
* T08.G5.01: Fix a condition that uses the wrong operator
* T09.G5.01: Display variable value on stage using the variable monitor
* T17.G5.08: Apply an impulse to jump or push
* T17.G6.04: Detect collisions for scoring or triggers


ID: T17.G7.01.01
Topic: T17 – 2D Motion & Physics
Skill: Point sprite in movement direction
Description: Students use `point in direction of speed` to automatically rotate a sprite to face its current movement direction. This is essential for arrows, rockets, and birds that should visually align with their trajectory as they fly along parabolic arcs.

Dependencies:
* T17.G7.01: Launch a configurable projectile


ID: T17.G7.01.02
Topic: T17 – 2D Motion & Physics
Skill: Enable CCD for fast projectiles
Description: Enable Continuous Collision Detection (CCD) to prevent fast-moving objects from tunneling through walls. Students observe that very fast physics bodies sometimes pass through thin obstacles (called 'tunneling'), then learn CCD solves this by detecting collisions between frames, ensuring no missed collisions at high speeds.

Dependencies:
* T17.G7.01: Launch a configurable projectile


ID: T17.G7.02
Topic: T17 – 2D Motion & Physics
Skill: Combine multiple forces simultaneously
Description: Students use `add force [force] in direction [angle]` to apply two or more forces in the same frame (gravity + constant wind, gravity + player thrust). They predict and observe the resulting curved motion paths.

Dependencies:
* T17.G5.08.03: Apply a single continuous force
* T17.G6.07: Debug unstable physics behavior
* T17.G6.08: Compare simulations to real-world motion


ID: T17.G7.02.01
Topic: T17 – 2D Motion & Physics
Skill: Clear forces and torques from physics bodies
Description: Students use `remove all forces` and `remove all torques` to reset accumulated forces on physics bodies. They use this for game resets, mode transitions, or when switching from force-driven to velocity-driven control.

Dependencies:
* T17.G7.02: Combine multiple forces simultaneously


ID: T17.G7.02.02
Topic: T17 – 2D Motion & Physics
Skill: Apply force at a position for continuous rotation
Description: Students use `add force [force] in direction [angle] at position x [X] y [Y]` to apply continuous off-center forces. They observe how sustained forces applied away from center create continuous rotation (torque), useful for thrusters, spinning mechanisms, or torque-based controls.

Dependencies:
* T17.G5.08.02: Apply impulse at a position for rotation
* T17.G7.02: Combine multiple forces simultaneously


ID: T17.G7.03
Topic: T17 – 2D Motion & Physics
Skill: Simulate drag with manual force calculations
Description: Students manually implement drag effects by calculating forces opposite to velocity (applying force proportional to speed in the reverse direction). They experiment with different drag coefficients and observe how they affect motion through different media (air, water, honey). This manual approach builds understanding before using built-in damping.

Dependencies:
* T17.G5.08.01: Distinguish forces from impulses
* T17.G6.07: Debug unstable physics behavior


ID: T17.G7.03.01
Topic: T17 – 2D Motion & Physics
Skill: Use built-in damping as alternative to manual drag
Description: Students use the built-in `set damping factor for movement [M]% rotation [R]%` block to simulate air resistance or water friction as an easier alternative to manual force calculations. They compare results with their manual implementation and tune damping percentages for desired slowdown behavior.

Dependencies:
* T17.G7.03: Simulate drag with manual force calculations


ID: T17.G7.04
Topic: T17 – 2D Motion & Physics
Skill: Build chains or stacks of physics objects
Description: Students create stacks of boxes or chains of linked sprites and explore how forces propagate through the system when one element is pushed. They observe how density affects collision outcomes.

Dependencies:
* T17.G6.07: Debug unstable physics behavior
* T17.G6.08: Compare simulations to real-world motion


ID: T17.G7.04.01
Topic: T17 – 2D Motion & Physics
Skill: Use continuous torque to rotate bodies
Description: Use 'physics add torque' to apply continuous rotational force to a physics body. Students learn that torque (like force for linear motion) accumulates over time, respecting the body's rotational mass and creating smooth, physics-based rotation. Compare to direct rotation speed control.

Dependencies:
* T17.G6.02.01.03: Set rotation speed directly
* T17.G7.02: Combine multiple forces simultaneously


ID: T17.G7.04.01.01
Topic: T17 – 2D Motion & Physics
Skill: Apply torque impulse for instant rotation
Description: Use 'physics apply torque impulse' to apply an instant rotational "kick" to a physics body. Students learn that torque impulse (like linear impulse) applies immediately regardless of mass, perfect for one-time rotation events like hitting a spinning obstacle.

Dependencies:
* T17.G7.04.01: Use continuous torque to rotate bodies
* T17.G5.08.02: Apply impulse at a position for rotation


ID: T17.G7.05
Topic: T17 – 2D Motion & Physics
Skill: Read velocity and mass reporters
Description: Students use the reporter blocks `(x speed)`, `(y speed)`, `(mass)`, `(angular speed)`, and `(ground slope)` to display real-time physics data on screen. They use this data for UI displays, conditional logic, and debugging.

Dependencies:
* T17.G6.07: Debug unstable physics behavior
* T17.G6.08: Compare simulations to real-world motion


ID: T17.G7.05.01
Topic: T17 – 2D Motion & Physics
Skill: Instrument and graph motion data
Description: Students record motion data from a sprite every few frames using velocity reporters, store values in lists, and create a graph. They use the graph to confirm constant acceleration or spot errors.

Dependencies:
* T10.G5.01: Add and remove items from a list
* T17.G7.05: Read velocity and mass reporters


ID: T17.G7.05.02
Topic: T17 – 2D Motion & Physics
Skill: Use velocity reporters for UI speedometers and HUDs
Description: Read velocity and angular speed reporters to display speedometers, tachometers, and other HUD elements

Dependencies:
* T17.G7.05: Read velocity and mass reporters


ID: T17.G7.06
Topic: T17 – 2D Motion & Physics
Skill: Model a real-world physics scenario
Description: Students choose a real phenomenon (bouncing ball, swinging pendulum, sliding object) and build a CreatiCode simulation that approximates it. They explain which physics properties (gravity, friction, restitution) they tuned to mimic reality.

Dependencies:
* T08.G5.01: Fix a condition that uses the wrong operator
* T09.G5.01: Display variable value on stage using the variable monitor
* T17.G6.08: Compare simulations to real-world motion


ID: T17.G7.07
Topic: T17 – 2D Motion & Physics
Skill: Evaluate whether a simulation meets requirements
Description: Students are given target requirements (e.g., "ball must clear the second bumper but stop before the third") and test a simulation against them. They examine logged data and decide if requirements were met, citing evidence.

Dependencies:
* T17.G6.07: Debug unstable physics behavior
* T17.G6.08: Compare simulations to real-world motion


ID: T17.G8.01
Topic: T17 – 2D Motion & Physics
Skill: Design a physics-based arcade game concept
Description: Students design a launcher + target game (Angry Birds–style) by planning level layouts, identifying required physics objects (projectiles, targets, obstacles), and sketching game mechanics. They create design documents that specify win conditions and challenge progression before implementation.

Dependencies:
* T17.G7.06: Model a real-world physics scenario


ID: T17.G8.01.01
Topic: T17 – 2D Motion & Physics
Skill: Implement physics arcade game mechanics
Description: Students implement the game design from T17.G8.01 by creating sprites, setting up physics bodies, configuring collision detection, and scripting game logic. They translate design specifications into working code using physics blocks.

Dependencies:
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps
* T17.G8.01: Design a physics-based arcade game concept
* T04.G6.01: Group snippets by underlying algorithm pattern
* T10.G6.01: Sort a table by a column


ID: T17.G8.01.02
Topic: T17 – 2D Motion & Physics
Skill: Balance and tune physics game difficulty
Description: Students playtest their physics game and adjust physics parameters (gravity, impulse strength, object density, friction, restitution) to balance difficulty. They iterate on parameter values to make gameplay fair but challenging, ensuring levels are neither too easy nor frustratingly hard.

Dependencies:
* T17.G8.01.01: Implement physics arcade game mechanics


ID: T17.G8.02
Topic: T17 – 2D Motion & Physics
Skill: Implement fixed joints for connected objects
Description: Students use `fix relative position to [sprite]` to weld sprites together so they move as a single rigid unit, and `remove relative position constraint` to break the connection. Examples: compound objects, multi-part characters, towed vehicles that can be detached.

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T17.G7.06: Model a real-world physics scenario
* T02.G6.01: Learn the pseudocode generation block
* T16.G6.01: Evaluate an interface for usability
* T22.G6.01.01: Make a basic ChatGPT request with one parameter


ID: T17.G8.02.01
Topic: T17 – 2D Motion & Physics
Skill: Implement revolute joints for hinges
Description: Students use `set [sprite] as rotation axis with offset x [X] y [Y]` to create hinged objects like doors, seesaws, and pendulums. They configure rotation behavior with `set rotation axis speed [S] damping factor [D]%`, and use `remove rotation axis` to disconnect hinges. Examples: breakable doors, detachable rotating parts.

Dependencies:
* T17.G8.02: Implement fixed joints for connected objects
* T02.G6.01: Learn the pseudocode generation block
* T07.G6.01: Trace nested loops with variable bounds
* T12.G6.01: Analyze a program's structure using a checklist and suggest specific improvements


ID: T17.G8.02.01.01
Topic: T17 – 2D Motion & Physics
Skill: Control revolute joint motors with speed and damping
Description: Control revolute joint motors using speed and damping parameters to create powered rotations like fans or wheels

Dependencies:
* T17.G8.02.01: Implement revolute joints for hinges
* T12.G6.01: Analyze a program's structure using a checklist and suggest specific improvements


ID: T17.G8.02.02
Topic: T17 – 2D Motion & Physics
Skill: Implement prismatic joints for sliding
Description: Students use `allow [Horizontal/Vertical] sliding relative to [sprite] range from [min] to [max]` to create pistons, sliding doors, and spring-loaded platforms with configurable movement limits. Note: Prismatic joints are permanent once created; plan constraint usage during the design phase.

Dependencies:
* T17.G8.02.01: Implement revolute joints for hinges
* T02.G6.01: Learn the pseudocode generation block
* T12.G6.01: Analyze a program's structure using a checklist and suggest specific improvements
* T16.G6.01: Evaluate an interface for usability


ID: T17.G8.02.03
Topic: T17 – 2D Motion & Physics
Skill: Debug joint constraint issues
Description: Students diagnose and fix common joint problems such as joints separating under force, rotation limits not working correctly, or motors behaving unpredictably. They learn to adjust joint parameters, verify anchor positions, and test constraint behavior systematically.

Dependencies:
* T17.G8.02.01: Implement revolute joints for hinges
* T17.G8.02.02: Implement prismatic joints for sliding


ID: T17.G8.03
Topic: T17 – 2D Motion & Physics
Skill: Build automated physics regression tests
Description: Students create scripts that spawn test objects, run the simulation for a set time, and assert that positions, velocities, or collision counts stay within tolerances. This guards against regressions when modifying physics code.

Dependencies:
* T08.G6.01: Use conditionals to control simulation steps
* T17.G7.07: Evaluate whether a simulation meets requirements
* T02.G6.01: Learn the pseudocode generation block
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T07.G6.01: Trace nested loops with variable bounds


ID: T17.G8.04
Topic: T17 – 2D Motion & Physics
Skill: Identify physics performance bottlenecks
Description: Students identify performance bottlenecks in a busy physics scene by observing frame rate and lag during playtesting. They diagnose issues like too many active objects, complex collision shapes, or unnecessary collision checks.

Dependencies:
* T07.G6.01: Trace nested loops with variable bounds
* T17.G7.06: Model a real-world physics scenario
* T17.G7.07: Evaluate whether a simulation meets requirements
* T04.G6.01: Group snippets by underlying algorithm pattern
* T10.G6.01: Sort a table by a column
* T11.G6.01: Design custom blocks with clear, predictable interfaces


ID: T17.G8.04.01
Topic: T17 – 2D Motion & Physics
Skill: Optimize collision shapes for performance
Description: Students implement shape optimizations by using simpler collision shapes (Box instead of Convex Hull), reducing active object count, using compound shapes sparingly, disabling unnecessary collision groups, and hiding debug overlays. They verify improvements through repeated playtesting.

Dependencies:
* T17.G8.04: Identify physics performance bottlenecks
* T04.G6.01: Group snippets by underlying algorithm pattern
* T06.G6.01: Trace event execution paths in a multi‑event program
* T10.G6.01: Sort a table by a column


ID: T17.G8.05
Topic: T17 – 2D Motion & Physics
Skill: Control gravity scale and time speed
Description: Students use `set gravity scale [value]%` to create floaty zones or reverse gravity areas, and `set physics time speed [value]%` to create slow-motion or fast-forward effects for dramatic game moments.

Dependencies:
* T17.G7.06: Model a real-world physics scenario
* T02.G6.01: Learn the pseudocode generation block
* T03.G6.01: Propose modules for a medium project
* T07.G6.01: Trace nested loops with variable bounds


ID: T17.G8.06
Topic: T17 – 2D Motion & Physics
Skill: Use instrumentation data to tune difficulty
Description: Students log player attempts (launch angle, power, success/fail), analyze the dataset, and retune physics parameters (gravity, impulse strength, target size) to achieve a desired win rate. They connect physics tweaks to game analytics.

Dependencies:
* T09.G6.01: Model real-world quantities using variables and formulas
* T17.G7.06: Model a real-world physics scenario
* T03.G6.01: Propose modules for a medium project
* T04.G6.01: Group snippets by underlying algorithm pattern
* T07.G6.01: Trace nested loops with variable bounds


ID: T17.G8.07
Topic: T17 – 2D Motion & Physics
Skill: Plan a physics-based puzzle game
Description: Students plan a physics puzzle game (pulleys, seesaws, Rube Goldberg machines) by identifying required physics mechanics, sketching level layouts, and defining puzzle solutions. They create design documents specifying which joints and physics properties each puzzle requires.

Dependencies:
* T17.G8.02: Implement fixed joints for connected objects
* T17.G7.06: Model a real-world physics scenario


ID: T17.G8.07.01
Topic: T17 – 2D Motion & Physics
Skill: Select appropriate joints for puzzle mechanics
Description: Students analyze their puzzle game design and select the appropriate joint types (fixed, revolute, prismatic) for each puzzle element. They justify joint choices based on desired mechanical behavior and puzzle challenge design.

Dependencies:
* T17.G8.07: Plan a physics-based puzzle game
* T17.G8.02.01: Implement revolute joints for hinges
* T17.G8.02.02: Implement prismatic joints for sliding


ID: T17.G8.07.02
Topic: T17 – 2D Motion & Physics
Skill: Implement and test physics puzzle game
Description: Students implement their physics puzzle game by creating joints, configuring physics parameters, and scripting win conditions. They playtest puzzles to ensure solutions are discoverable and mechanics work as intended, iterating on joint parameters and object properties to achieve desired difficulty.

Dependencies:
* T17.G8.07.01: Select appropriate joints for puzzle mechanics
* T26.G6.01: Map stakeholder questions to data requirements
* T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)


