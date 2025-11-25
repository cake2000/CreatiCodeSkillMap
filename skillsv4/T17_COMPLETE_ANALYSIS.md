# T17 – 2D Motion & Physics: Complete Analysis

## Overview
This document provides a comprehensive analysis of all T17 (2D Motion & Physics) skills extracted from the allskills.md file, organized by grade level from GK through G8.

---

## GRADE K (Kindergarten)

### T17.K.01
**Skill:** Observe sprite position changes (picture-based)
**Description:** Students watch animations of sprites moving and identify which sprite moved, matching before/after pictures. They recognize that "motion" means a sprite's position changes on the stage.
**Dependencies:** None

### T17.K.02
**Skill:** Match sprite to position after motion (picture-based)
**Description:** Students see a motion block sequence and choose which picture shows where the sprite will end up. They develop spatial reasoning by predicting final positions from simple motion sequences.
**Dependencies:**
* T17.K.01: Observe sprite position changes (picture-based)

---

## GRADE 1

### T17.G1.01
**Skill:** Identify fast vs slow motion (picture-based)
**Description:** Students watch two sprite animations and identify which sprite moves faster. They compare motion speeds visually and describe motion using "fast" and "slow" vocabulary.
**Dependencies:**
* T17.K.02: Match sprite to position after motion (picture-based)

---

## GRADE 2

### T17.G2.01
**Skill:** Predict sprite direction from motion blocks (picture choices)
**Description:** Students look at motion blocks (move 10 steps, turn right, move 10 steps) and choose from picture options showing which direction the sprite will move. They build directional intuition before coding.
**Dependencies:**
* T17.G1.01: Identify fast vs slow motion (picture-based)

---

## GRADE 3

### T17.G3.01
**Skill:** Observe position changes from motion blocks
**Description:** Students observe how motion blocks (move, glide) change a sprite's position over time. They describe motion as "changing position" and predict where a sprite will be after motion blocks run.
**Dependencies:**
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T17.G2.01: Predict sprite direction from motion blocks (picture choices)

### T17.G3.02
**Skill:** Predict direction and distance of sprite motion
**Description:** Students predict which direction a sprite will move and approximately how far, given a sequence of motion blocks. They develop intuition for motion before variables are introduced.
**Dependencies:**
* T17.G3.01: Observe position changes from motion blocks

---

## GRADE 4

### T17.G4.01
**Skill:** Simulate falling with repeated motion
**Description:** Students create a simple falling animation by repeatedly moving a sprite down in a loop. They observe that the sprite appears to "fall" due to gravity conceptually, preparing them for velocity-based motion.
**Dependencies:**
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T07.G3.01: Use a counted repeat loop
* T17.G3.02: Predict direction and distance of sprite motion

### T17.G4.02
**Skill:** Explain speed as position change over time
**Description:** Students explain that speed means "how much position changes each time the loop runs." They compare fast vs slow motion by changing the step size in a loop.
**Dependencies:**
* T01.G2.01: Find actions that repeat in everyday tasks
* T02.G2.01: Turn a picture routine into labeled boxes
* T02.G2.02: Read a box diagram and choose the matching pictures
* T06.G2.03: Design a simple "if-then" game rule
* T09.G3.05: Trace code with variables to predict outcomes
* T17.G4.01: Simulate falling with repeated motion

---

## GRADE 5

### T17.G5.02
**Skill:** Track gravity with velocity variables
**Description:** Students build a loop that stores a sprite's y-velocity in a variable, subtracts a gravity constant each frame, then adds the velocity to the sprite's y-position. This manual approach mirrors classic Scratch tutorials and prepares students for physics debugging.
**Dependencies:**
* T07.G3.05: Fix a simple repeat loop count
* T09.G3.05: Trace code with variables to predict outcomes
* T17.G4.02: Explain speed as position change over time
* T08.G3.00: Identify if blocks in existing code

### T17.G5.03
**Skill:** Use horizontal speed and friction variables
**Description:** Students add an x-velocity variable, respond to arrow keys to change it, and multiply by a friction factor (e.g., 0.9) each tick so motion glides to a stop. This prepares students for platformer mechanics.
**Dependencies:**
* T09.G4.03: Use multiple variables in a single script
* T17.G5.02: Track gravity with velocity variables
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code

### T17.G5.03.01
**Skill:** Build a top-down vehicle with manual friction control
**Description:** Create a top-down car or spaceship game using manual friction variables to control movement
**Dependencies:**
* T17.G5.03: Use horizontal speed and friction variables
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.04
**Skill:** Code a manual bounce with energy loss
**Description:** Students write a conditional that checks for ground contact, multiplies the y-velocity by a negative damping factor (e.g., -0.6), and sends the sprite back up with reduced height. This cements physics vocabulary before using the engine's restitution.
**Dependencies:**
* T08.G3.01: Use a simple if in a script
* T17.G5.02: Track gravity with velocity variables
* T07.G3.01: Use a counted repeat loop
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.04.01
**Skill:** Create a simple platformer using manual gravity
**Description:** Build a basic platformer game using manual gravity and bounce calculations with velocity variables
**Dependencies:**
* T17.G5.04: Code a manual bounce with energy loss
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.05
**Skill:** Initialize a 2D physics world
**Description:** Students add the `initialize 2D physics world with gravity x [0] y [-100]` block, set appropriate gravity values, and confirm the debug overlay shows the world running. They understand that no physics behavior occurs until this block executes. Note: Running this block again resets the entire physics world, useful for level transitions or game resets.
**Dependencies:**
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T17.G4.02: Explain speed as position change over time
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.06
**Skill:** Attach a dynamic body to a sprite
**Description:** Students convert a sprite to a dynamic physics body using `behave as a [dynamic] [object] shape [Box] debug [Yes]`. They observe the sprite fall and stop when it hits the stage floor, confirming the physics world affects it.
**Dependencies:**
* T17.G5.05: Initialize a 2D physics world
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.06.A
**Skill:** Practice creating multiple dynamic bodies
**Description:** Students create 2-3 different sprites and convert each to dynamic physics bodies. They experiment with different starting positions and observe how all bodies fall and interact, building fluency with the basic dynamic body setup before exploring shape options.
**Dependencies:**
* T17.G5.06: Attach a dynamic body to a sprite
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.06.A.01
**Skill:** Use debug mode to visualize collision shapes
**Description:** Enable debug mode in the 2D physics world to see invisible collision shape outlines overlaid on sprites. Students learn that debug mode helps understand why collisions happen or don't happen, by showing the actual physics boundaries independent of sprite appearance.
**Dependencies:**
* T17.G5.06.A: Practice creating multiple dynamic bodies
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.06.01
**Skill:** Choose Box vs Circle collision shapes
**Description:** Choose between Box and Circle collision shapes based on sprite appearance and desired physics behavior
**Dependencies:**
* T17.G5.06.A: Practice creating multiple dynamic bodies
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.06.01.01
**Skill:** Use Capsule shapes for elongated objects
**Description:** Use Capsule collision shapes for elongated sprites like characters or vehicles
**Dependencies:**
* T17.G5.06.01: Choose Box vs Circle collision shapes
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.06.01.02
**Skill:** Use Convex Hull for sprite-fitted collision
**Description:** Use Convex Hull collision shapes for automatic sprite-fitted collision detection
**Dependencies:**
* T17.G5.06.01: Choose Box vs Circle collision shapes
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.06.02
**Skill:** Create sensor bodies for trigger zones
**Description:** Students create sensor bodies using `behave as a [dynamic] [sensor]` that detect overlaps without causing physical collisions. They use sensors for trigger zones, collectible detection areas, and checkpoint markers.
**Dependencies:**
* T17.G5.06.01: Choose Box vs Circle collision shapes
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.06.03
**Skill:** Create compound shapes for complex sprites
**Description:** Students use `behave as a [dynamic] [object] in compound shape with curve tolerance [value] point distance [value]` to create physics bodies that match complex or concave sprite outlines. They understand the trade-off between accuracy and performance.
**Dependencies:**
* T17.G5.06.01: Choose Box vs Circle collision shapes
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.07
**Skill:** Build fixed boundaries for floors and walls
**Description:** Students add fixed physics bodies to floor or wall sprites using `behave as a [fixed] [object]` so falling or sliding objects stop on contact. They learn to use fixed bodies for geometry that should not move.
**Dependencies:**
* T17.G5.05: Initialize a 2D physics world
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.08
**Skill:** Apply an impulse to jump or push
**Description:** Students use `apply impulse [force] in direction [angle]` to make a dynamic sprite jump in response to input (e.g., direction 90 for upward jump). They control impulse strength so the sprite clears a target platform height.
**Dependencies:**
* T06.G4.01: Use multiple event handlers in the same sprite
* T17.G5.06: Attach a dynamic body to a sprite
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.08.01
**Skill:** Distinguish forces from impulses
**Description:** Students compare `add force [force] in direction [angle]` (applied continuously each frame) with `apply impulse [force] in direction [angle]` (applied once instantly). They use forces for sustained thrust (jetpack) and impulses for sudden actions (jump, kick).
**Dependencies:**
* T17.G5.08: Apply an impulse to jump or push
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.08.02
**Skill:** Apply impulse at a position for rotation
**Description:** Students use `apply impulse [force] in direction [angle] at position x [X] y [Y]` to apply off-center impulses. They observe how impulses applied away from center create instant rotation (torque), useful for hitting objects at an angle or creating spin effects.
**Dependencies:**
* T17.G5.08.01: Distinguish forces from impulses
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.09
**Skill:** Configure density for mass control
**Description:** Students adjust density using `update density [value] friction % restitution %` to control how heavy a sprite feels. They understand that density × area = mass and experiment with light vs heavy objects in collisions.
**Dependencies:**
* T17.G5.06: Attach a dynamic body to a sprite
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.10
**Skill:** Trace simple 2D physics motion
**Description:** Students experiment with a physics simulation by adjusting gravity, density, and starting height values, then predict and verify where the sprite lands. They run the simulation, observe outcomes, and choose the correct statement about where the sprite ends up (e.g., "lands on the platform," "still in the air," "passed through the floor"). This hands-on prediction and testing builds physics intuition.
**Dependencies:**
* T09.G3.05: Trace code with variables to predict outcomes
* T17.G5.06: Attach a dynamic body to a sprite
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code

### T17.G5.10.01
**Skill:** Remove physics body from a sprite
**Description:** Students use `remove physics-based behavior` to detach a sprite from the physics engine so it no longer responds to gravity or collisions. They use this for collected items, destroyed enemies, or transitioning between physics and non-physics modes.
**Dependencies:**
* T17.G5.06: Attach a dynamic body to a sprite
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.11
**Skill:** Debug missing physics setup
**Description:** Students open a buggy project where the player never falls because the physics world was not initialized or the body was left as fixed. They inspect the scripts, identify the missing setup, and re-test.
**Dependencies:**
* T17.G5.06: Attach a dynamic body to a sprite
* T17.G5.07: Build fixed boundaries for floors and walls
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

### T17.G5.12
**Skill:** Choose manual vs engine-based physics
**Description:** After experiencing both manual velocity variables (G5.02-G5.04) and the physics engine (G5.05-G5.11), students compare CreatiCode project briefs (platformer, UI animation, top-down maze, pinball machine) and choose the most appropriate approach for each. They justify their decision based on project requirements and their hands-on experience with both methods.
**Dependencies:**
* T05.G4.05: Plan a simulation with defined inputs and outputs
* T17.G5.04: Code a manual bounce with energy loss
* T17.G5.11: Debug missing physics setup
* T07.G3.01: Use a counted repeat loop
* T08.G3.00: Identify if blocks in existing code
* T09.G3.01.01: Create a new variable with a descriptive name

---

## GRADE 6

### T17.G6.01
**Skill:** Configure surface friction parameters
**Description:** Students adjust the friction percentage using `update density [value] friction [value]% restitution [value]%` and measure how far objects slide on different surfaces. They learn to map friction values to sliding distances through systematic testing.
**Dependencies:**
* T17.G5.09: Configure density for mass control
* T17.G5.10: Trace simple 2D physics motion

### T17.G6.02
**Skill:** Control restitution (bounce) parameters
**Description:** Students modify the restitution percentage and measure bounce heights. They learn the relationship between restitution values (0-100%) and energy conservation in collisions: 0% = no bounce, 100% = full bounce.
**Dependencies:**
* T17.G6.01: Configure surface friction parameters

### T17.G6.02.01
**Skill:** Set velocity directly for physics bodies
**Description:** Students use `set x speed [value]`, `set y speed [value]`, and `set speed [value] in direction [angle]` to directly control physics body velocity. They compare direct velocity setting to impulses and understand when each approach is appropriate.
**Dependencies:**
* T17.G5.06: Attach a dynamic body to a sprite
* T17.G5.08: Apply an impulse to jump or push

### T17.G6.02.01.02
**Skill:** Read velocity reporters for verification
**Description:** Use velocity reporter blocks (x speed, y speed, speed) to read and verify the current velocity of a physics body. Students learn to check if velocity changes worked as expected, essential for debugging motion issues.
**Dependencies:**
* T17.G6.02.01: Set velocity directly for physics bodies

### T17.G6.02.01.03
**Skill:** Set rotation speed directly
**Description:** Use 'physics set rotation speed' to directly control how fast a physics body spins (degrees per second). Students learn this gives immediate rotation control, parallel to setting linear velocity.
**Dependencies:**
* T17.G6.02.01: Set velocity directly for physics bodies

### T17.G6.02.01.01
**Skill:** Maintain constant speed in current direction
**Description:** Students use `set speed [value] in moving direction` to regulate an object's speed without changing its trajectory. This is useful for maintaining constant character movement speed, limiting maximum velocity, or normalizing physics-driven velocities while preserving direction changes from collisions or forces.
**Dependencies:**
* T17.G6.02.01: Set velocity directly for physics bodies

### T17.G6.02.02
**Skill:** Compare dynamic vs movable body types
**Description:** Students compare dynamic bodies (affected by forces and gravity) with movable (kinematic) bodies (move via velocity but don't respond to forces). They identify scenarios where each type is appropriate: dynamic for player characters and falling objects, movable for moving platforms and elevators.
**Dependencies:**
* T17.G5.06: Attach a dynamic body to a sprite
* T17.G6.02.01: Set velocity directly for physics bodies

### T17.G6.03
**Skill:** Build a movable (kinematic) moving platform
**Description:** Students create a platform using `behave as a [movable] [object]` that moves on a fixed path while still colliding with players. They use `set x speed` and `set y speed` to control platform motion directly rather than relying on physics forces.
**Dependencies:**
* T07.G3.05: Fix a simple repeat loop count
* T17.G6.02.02: Compare dynamic vs movable body types

### T17.G6.04
**Skill:** Detect collisions for scoring or triggers
**Description:** Students use `broadcast [message] when colliding with [sprite]` to listen for collision events between sprites. They run scoring or state-change scripts in response to collisions (player hits coin, ball hits bumper).
**Dependencies:**
* T06.G4.01: Use multiple event handlers in the same sprite
* T17.G5.10: Trace simple 2D physics motion

### T17.G6.04.01
**Skill:** Detect collision end events
**Description:** Students use `broadcast [message] when finish colliding with [sprite]` to trigger actions when objects stop touching. Students learn collision end events are essential for: stopping lava damage when leaving fire, releasing pressed buttons, tracking exit from trigger zones, and any scenario needing 'when objects separate' detection.
**Dependencies:**
* T17.G6.04: Detect collisions for scoring or triggers

### T17.G6.04.02
**Skill:** Enable ground detection for jump control
**Description:** Enable ground detection and use the 'in collision below' reporter to control platformer jumping
**Dependencies:**
* T17.G6.04: Detect collisions for scoring or triggers

### T17.G6.04.02.01
**Skill:** Use ground slope reporter for inclined surfaces
**Description:** Use the ground slope reporter to adjust sprite behavior on slopes and ramps
**Dependencies:**
* T17.G6.04.02: Enable ground detection for jump control

### T17.G6.04.03
**Skill:** Identify collision management needs
**Description:** Students analyze a game design (with multiple object types like players, enemies, collectibles, hazards, and platforms) and identify which objects should collide with each other and which should pass through. They plan collision filtering strategy before implementing collision groups.
**Dependencies:**
* T17.G6.04: Detect collisions for scoring or triggers

### T17.G6.04.04
**Skill:** Build trigger zones and collectibles with sensor bodies
**Description:** Use sensor bodies to create trigger zones, checkpoints, and collectible items that detect without physical collision
**Dependencies:**
* T17.G5.06.02: Create sensor bodies for trigger zones
* T17.G6.04: Detect collisions for scoring or triggers

### T17.G6.05
**Skill:** Set up static collision groups for filtering
**Description:** Set up collision groups to filter which objects can interact with each other. Students learn the 3-step process: (1) Assign group numbers to sprites using 'physics collision groups', (2) Configure filters on BOTH sprites using 'physics add collision filter' (filters are directional), (3) Test that objects not in any group collide with everything by default. Example: Group 1 (players) filters out Group 2 (power-ups) so players pass through collectibles.
**Dependencies:**
* T08.G4.01: Write a condition that uses and/or
* T17.G6.04.03: Identify collision management needs

### T17.G6.05.01
**Skill:** Dynamically modify collision groups at runtime
**Description:** Dynamically add or remove collision group memberships during gameplay (e.g., for invincibility, phasing)
**Dependencies:**
* T17.G6.05: Set up static collision groups for filtering

### T17.G6.05.02
**Skill:** Use dominance groups for one-way pushing
**Description:** Use dominance groups to create one-way interactions where stronger objects push weaker ones
**Dependencies:**
* T17.G6.05: Set up static collision groups for filtering

### T17.G6.06
**Skill:** Blend manual and engine sprites in a level
**Description:** Students create a project that combines manual motion (scrolling backgrounds, UI elements, non-physics objects) with physics bodies (falling objects, player characters) running simultaneously. Success criteria: manual sprites move smoothly without physics interference, physics sprites respond to gravity and collisions correctly, and no unintended physics bodies are created.
**Dependencies:**
* T17.G5.10: Trace simple 2D physics motion
* T17.G5.11: Debug missing physics setup

### T17.G6.06.01
**Skill:** Lock movement or rotation of physics bodies
**Description:** Students use `prevent body movement from forces [Yes]` and `prevent body rotation from forces [Yes]` to constrain physics objects. They create characters that stay upright, platforms that resist being pushed, or objects that only rotate without moving.
**Dependencies:**
* T17.G5.06: Attach a dynamic body to a sprite

### T17.G6.07
**Skill:** Debug unstable physics behavior
**Description:** Students diagnose why a sprite jitters, sinks through a platform, or flies off-screen (e.g., density too low, conflicting impulses, missing collision groups) and adjust parameters to stabilize the scene.
**Dependencies:**
* T17.G6.01: Configure surface friction parameters
* T17.G6.02: Control restitution (bounce) parameters

### T17.G6.07.01
**Skill:** Configure world border properties
**Description:** Set physics world border properties (friction and restitution). Students use 'physics world border friction' and 'physics world border restitution' blocks to control how sprites bounce and slide when hitting stage edges, creating realistic boundary behavior without manual edge detection.
**Dependencies:**
* T17.G5.05: Initialize a 2D physics world
* T17.G6.01: Configure surface friction parameters

### T17.G6.07.02
**Skill:** Configure world borders for wrap-around or open-edge levels
**Description:** Set physics world border collision groups. Students use 'physics world border collision groups' block to configure whether certain sprites or groups can collide with stage borders, enabling scenarios where some objects pass through edges while others bounce.
**Dependencies:**
* T17.G6.07.01: Configure world border properties

### T17.G6.08
**Skill:** Compare simulations to real-world motion
**Description:** Students record bounce heights or slide distances in CreatiCode, compare them to expected real-world results, and discuss how closely the simulation matches reality and what simplifications the physics engine makes.
**Dependencies:**
* T17.G5.10: Trace simple 2D physics motion

---

## GRADE 7

### T17.G7.01
**Skill:** Launch a configurable projectile
**Description:** Students create a launcher where users set angle and power using sliders. The projectile receives an initial impulse using `apply impulse [force] in direction [angle]` that produces a parabolic arc toward targets.
**Dependencies:**
* T08.G5.01: Fix a condition that uses the wrong operator
* T09.G5.01: Display variable value on stage using the variable monitor
* T17.G5.08: Apply an impulse to jump or push
* T17.G6.04: Detect collisions for scoring or triggers

### T17.G7.01.01
**Skill:** Point sprite in movement direction
**Description:** Students use `point in direction of speed` to automatically rotate a sprite to face its current movement direction. This is essential for arrows, rockets, and birds that should visually align with their trajectory as they fly along parabolic arcs.
**Dependencies:**
* T17.G7.01: Launch a configurable projectile

### T17.G7.01.02
**Skill:** Enable CCD for fast projectiles
**Description:** Enable Continuous Collision Detection (CCD) to prevent fast-moving objects from tunneling through walls. Students observe that very fast physics bodies sometimes pass through thin obstacles (called 'tunneling'), then learn CCD solves this by detecting collisions between frames, ensuring no missed collisions at high speeds.
**Dependencies:**
* T17.G7.01: Launch a configurable projectile

### T17.G7.02
**Skill:** Combine multiple forces simultaneously
**Description:** Students use `add force [force] in direction [angle]` to apply two or more forces in the same frame (gravity + constant wind, gravity + player thrust). They predict and observe the resulting curved motion paths.
**Dependencies:**
* T17.G5.08.01: Distinguish forces from impulses
* T17.G6.07: Debug unstable physics behavior
* T17.G6.08: Compare simulations to real-world motion

### T17.G7.02.01
**Skill:** Clear forces and torques from physics bodies
**Description:** Students use `remove all forces` and `remove all torques` to reset accumulated forces on physics bodies. They use this for game resets, mode transitions, or when switching from force-driven to velocity-driven control.
**Dependencies:**
* T17.G7.02: Combine multiple forces simultaneously

### T17.G7.02.02
**Skill:** Apply force at a position for continuous rotation
**Description:** Students use `add force [force] in direction [angle] at position x [X] y [Y]` to apply continuous off-center forces. They observe how sustained forces applied away from center create continuous rotation (torque), useful for thrusters, spinning mechanisms, or torque-based controls.
**Dependencies:**
* T17.G5.08.02: Apply impulse at a position for rotation
* T17.G7.02: Combine multiple forces simultaneously

### T17.G7.03
**Skill:** Simulate drag with manual force calculations
**Description:** Students manually implement drag effects by calculating forces opposite to velocity (applying force proportional to speed in the reverse direction). They experiment with different drag coefficients and observe how they affect motion through different media (air, water, honey). This manual approach builds understanding before using built-in damping.
**Dependencies:**
* T17.G5.08.01: Distinguish forces from impulses
* T17.G6.07: Debug unstable physics behavior

### T17.G7.03.01
**Skill:** Use built-in damping as alternative to manual drag
**Description:** Students use the built-in `set damping factor for movement [M]% rotation [R]%` block to simulate air resistance or water friction as an easier alternative to manual force calculations. They compare results with their manual implementation and tune damping percentages for desired slowdown behavior.
**Dependencies:**
* T17.G7.03: Simulate drag with manual force calculations

### T17.G7.04
**Skill:** Build chains or stacks of physics objects
**Description:** Students create stacks of boxes or chains of linked sprites and explore how forces propagate through the system when one element is pushed. They observe how density affects collision outcomes.
**Dependencies:**
* T17.G6.07: Debug unstable physics behavior
* T17.G6.08: Compare simulations to real-world motion

### T17.G7.04.01
**Skill:** Use continuous torque to rotate bodies
**Description:** Use 'physics add torque' to apply continuous rotational force to a physics body. Students learn that torque (like force for linear motion) accumulates over time, respecting the body's rotational mass and creating smooth, physics-based rotation. Compare to direct rotation speed control.
**Dependencies:**
* T17.G6.02.01.03: Set rotation speed directly
* T17.G7.02: Combine multiple forces simultaneously

### T17.G7.04.01.01
**Skill:** Apply torque impulse for instant rotation
**Description:** Use 'physics apply torque impulse' to apply an instant rotational "kick" to a physics body. Students learn that torque impulse (like linear impulse) applies immediately regardless of mass, perfect for one-time rotation events like hitting a spinning obstacle.
**Dependencies:**
* T17.G7.04.01: Use continuous torque to rotate bodies
* T17.G5.08.02: Apply impulse at a position for rotation

### T17.G7.05
**Skill:** Read velocity and mass reporters
**Description:** Students use the reporter blocks `(x speed)`, `(y speed)`, `(mass)`, `(angular speed)`, and `(ground slope)` to display real-time physics data on screen. They use this data for UI displays, conditional logic, and debugging.
**Dependencies:**
* T17.G6.07: Debug unstable physics behavior
* T17.G6.08: Compare simulations to real-world motion

### T17.G7.05.01
**Skill:** Instrument and graph motion data
**Description:** Students record motion data from a sprite every few frames using velocity reporters, store values in lists, and create a graph. They use the graph to confirm constant acceleration or spot errors.
**Dependencies:**
* T10.G5.01: Add and remove items from a list
* T17.G7.05: Read velocity and mass reporters

### T17.G7.05.02
**Skill:** Use velocity reporters for UI speedometers and HUDs
**Description:** Read velocity and angular speed reporters to display speedometers, tachometers, and other HUD elements
**Dependencies:**
* T17.G7.05: Read velocity and mass reporters

### T17.G7.06
**Skill:** Model a real-world physics scenario
**Description:** Students choose a real phenomenon (bouncing ball, swinging pendulum, sliding object) and build a CreatiCode simulation that approximates it. They explain which physics properties (gravity, friction, restitution) they tuned to mimic reality.
**Dependencies:**
* T08.G5.01: Fix a condition that uses the wrong operator
* T09.G5.01: Display variable value on stage using the variable monitor
* T17.G6.08: Compare simulations to real-world motion

### T17.G7.07
**Skill:** Evaluate whether a simulation meets requirements
**Description:** Students are given target requirements (e.g., "ball must clear the second bumper but stop before the third") and test a simulation against them. They examine logged data and decide if requirements were met, citing evidence.
**Dependencies:**
* T17.G6.07: Debug unstable physics behavior
* T17.G6.08: Compare simulations to real-world motion

---

## GRADE 8

### T17.G8.01
**Skill:** Design and balance a physics-based arcade game
**Description:** Students design a launcher + target game (Angry Birds–style) with multiple levels of difficulty. They test and adjust physics parameters (gravity, impulse strength, object density) to make gameplay fair but challenging.
**Dependencies:**
* T07.G6.01: Trace nested loops with variable bounds
* T08.G6.01: Use conditionals to control simulation steps
* T17.G7.06: Model a real-world physics scenario
* T04.G6.01: Group snippets by underlying algorithm pattern
* T10.G6.01: Sort a table by a column
* T18.G6.01.01: Apply forces and impulses to physics bodies

### T17.G8.02
**Skill:** Implement fixed joints for connected objects
**Description:** Students use `fix relative position to [sprite]` to weld sprites together so they move as a single rigid unit, and `remove relative position constraint` to break the connection. Examples: compound objects, multi-part characters, towed vehicles that can be detached.
**Dependencies:**
* T09.G6.01: Model real-world quantities using variables and formulas
* T17.G7.06: Model a real-world physics scenario
* T02.G6.01: Learn the pseudocode generation block
* T16.G6.01: Evaluate an interface for usability
* T22.G6.01.01: Make a basic ChatGPT request with one parameter

### T17.G8.02.01
**Skill:** Implement revolute joints for hinges
**Description:** Students use `set [sprite] as rotation axis with offset x [X] y [Y]` to create hinged objects like doors, seesaws, and pendulums. They configure rotation behavior with `set rotation axis speed [S] damping factor [D]%`, and use `remove rotation axis` to disconnect hinges. Examples: breakable doors, detachable rotating parts.
**Dependencies:**
* T17.G8.02: Implement fixed joints for connected objects
* T02.G6.01: Learn the pseudocode generation block
* T07.G6.01: Trace nested loops with variable bounds
* T12.G6.01: Analyze a program's structure using a checklist and suggest specific improvements

### T17.G8.02.01.01
**Skill:** Control revolute joint motors with speed and damping
**Description:** Control revolute joint motors using speed and damping parameters to create powered rotations like fans or wheels
**Dependencies:**
* T17.G8.02.01: Implement revolute joints for hinges
* T12.G6.01: Analyze a program's structure using a checklist and suggest specific improvements
* T25.G6.01: Document metadata for datasets
* T33.G6.01: Identify and test Cloud blocks for network dependencies

### T17.G8.02.02
**Skill:** Implement prismatic joints for sliding
**Description:** Students use `allow [Horizontal/Vertical] sliding relative to [sprite] range from [min] to [max]` to create pistons, sliding doors, and spring-loaded platforms with configurable movement limits. Note: Prismatic joints are permanent once created; plan constraint usage during the design phase.
**Dependencies:**
* T17.G8.02.01: Implement revolute joints for hinges
* T02.G6.01: Learn the pseudocode generation block
* T12.G6.01: Analyze a program's structure using a checklist and suggest specific improvements
* T16.G6.01: Evaluate an interface for usability

### T17.G8.03
**Skill:** Build automated physics regression tests
**Description:** Students create scripts that spawn test objects, run the simulation for a set time, and assert that positions, velocities, or collision counts stay within tolerances. This guards against regressions when modifying physics code.
**Dependencies:**
* T08.G6.01: Use conditionals to control simulation steps
* T17.G7.07: Evaluate whether a simulation meets requirements
* T02.G6.01: Learn the pseudocode generation block
* T05.G6.01: Apply empathy, needs, and accessibility checklist to a design
* T07.G6.01: Trace nested loops with variable bounds

### T17.G8.04
**Skill:** Identify physics performance bottlenecks
**Description:** Students identify performance bottlenecks in a busy physics scene by observing frame rate and lag during playtesting. They diagnose issues like too many active objects, complex collision shapes, or unnecessary collision checks.
**Dependencies:**
* T07.G6.01: Trace nested loops with variable bounds
* T17.G7.06: Model a real-world physics scenario
* T17.G7.07: Evaluate whether a simulation meets requirements
* T04.G6.01: Group snippets by underlying algorithm pattern
* T10.G6.01: Sort a table by a column
* T11.G6.01: Design custom blocks with clear, predictable interfaces

### T17.G8.04.01
**Skill:** Optimize collision shapes for performance
**Description:** Students implement shape optimizations by using simpler collision shapes (Box instead of Convex Hull), reducing active object count, using compound shapes sparingly, disabling unnecessary collision groups, and hiding debug overlays. They verify improvements through repeated playtesting.
**Dependencies:**
* T17.G8.04: Identify physics performance bottlenecks
* T04.G6.01: Group snippets by underlying algorithm pattern
* T06.G6.01: Trace event execution paths in a multi‑event program
* T10.G6.01: Sort a table by a column

### T17.G8.05
**Skill:** Control gravity scale and time speed
**Description:** Students use `set gravity scale [value]%` to create floaty zones or reverse gravity areas, and `set physics time speed [value]%` to create slow-motion or fast-forward effects for dramatic game moments.
**Dependencies:**
* T17.G7.06: Model a real-world physics scenario
* T02.G6.01: Learn the pseudocode generation block
* T03.G6.01: Propose modules for a medium project
* T07.G6.01: Trace nested loops with variable bounds

### T17.G8.06
**Skill:** Use instrumentation data to tune difficulty
**Description:** Students log player attempts (launch angle, power, success/fail), analyze the dataset, and retune physics parameters (gravity, impulse strength, target size) to achieve a desired win rate. They connect physics tweaks to game analytics.
**Dependencies:**
* T09.G6.01: Model real-world quantities using variables and formulas
* T17.G7.06: Model a real-world physics scenario
* T03.G6.01: Propose modules for a medium project
* T04.G6.01: Group snippets by underlying algorithm pattern
* T07.G6.01: Trace nested loops with variable bounds

### T17.G8.07
**Skill:** Build a physics-based puzzle game
**Description:** Design and implement a physics-based puzzle game (e.g., pulleys, seesaws, Rube Goldberg machines)
**Dependencies:**
* T17.G8.02: Implement fixed joints for connected objects
* T17.G7.06: Model a real-world physics scenario
* T18.G6.01.01: Apply forces and impulses to physics bodies
* T26.G6.01: Map stakeholder questions to data requirements
* T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)

---

## ANALYSIS SECTION

### 1. SKILLS THAT SEEM TOO BROAD AND NEED BREAKING DOWN

**T17.G5.12 - Choose manual vs engine-based physics**
- This is a comparative decision-making skill that spans a huge conceptual space
- Should potentially be broken into: (a) Identify project requirements, (b) Match requirements to physics approach, (c) Justify physics approach selection

**T17.G6.06 - Blend manual and engine sprites in a level**
- This skill combines multiple complex concepts (manual motion, physics bodies, debugging)
- Could be broken into: (a) Identify which sprites need physics, (b) Implement mixed-mode sprites, (c) Debug physics/non-physics interactions

**T17.G7.06 - Model a real-world physics scenario**
- Very open-ended and could encompass many different types of scenarios
- Should potentially have sub-skills for different scenario types (projectile, pendulum, collision, etc.)

**T17.G8.01 - Design and balance a physics-based arcade game**
- This is a capstone project that combines design, implementation, and tuning
- Could benefit from scaffolding skills for: (a) Design game mechanics, (b) Implement core physics, (c) Balance parameters through testing

**T17.G8.07 - Build a physics-based puzzle game**
- Another broad capstone project
- Similar to G8.01, needs more scaffolding

### 2. POTENTIAL DUPLICATES OR OVERLAPS

**T17.G6.02.01 vs T17.G6.02.01.02**
- "Set velocity directly for physics bodies" vs "Read velocity reporters for verification"
- These are complementary (write vs read) but the naming/organization could be clearer

**T17.G5.08.01 vs T17.G7.02**
- "Distinguish forces from impulses" (G5) vs "Combine multiple forces simultaneously" (G7)
- Good progression but T17.G7.02 should explicitly reference the distinction made in G5

**T17.G7.03 vs T17.G7.03.01**
- "Simulate drag with manual force calculations" vs "Use built-in damping as alternative"
- These present two approaches to the same problem - organization is good

**T17.G5.06.02 vs T17.G6.04.04**
- "Create sensor bodies for trigger zones" (G5) vs "Build trigger zones and collectibles with sensor bodies" (G6)
- The G5 skill introduces the concept, G6 applies it - good scaffolding but could be clearer

### 3. MISSING SCAFFOLDING GAPS

**Gap between K and G1:**
- No Grade K to Grade 1 transition - single skill in G1 (T17.G1.01)
- Need more K-level skills or early G1 skills to bridge basic motion understanding

**Gap in G4 (Missing T17.G5.01):**
- Notice the jump from T17.G4.02 directly to T17.G5.02
- There's a note in the original that "G5.01 is missing" which references applying gravity
- The curriculum jumps from conceptual gravity (G4) to velocity variables (G5.02) without a bridge

**Gap between manual physics (G5.02-G5.04) and engine physics (G5.05-G5.12):**
- T17.G5.12 attempts to bridge this but comes at the END
- Would benefit from a mid-point skill around G5.06-G5.07 that explicitly compares approaches

**Gap in collision detection progression:**
- T17.G6.04 introduces collision detection
- T17.G6.04.02 jumps to ground detection (specialized)
- Missing: basic collision filtering before specialized applications

**Gap in force/impulse progression:**
- T17.G5.08: Apply impulse
- T17.G5.08.01: Distinguish forces from impulses
- T17.G7.02: Combine multiple forces
- Missing: Apply a single continuous force (between G5.08.01 and G7.02)

**Gap in joints:**
- T17.G8.02: Fixed joints
- T17.G8.02.01: Revolute joints
- T17.G8.02.02: Prismatic joints
- Missing: Joint debugging skills, joint limit testing, joint breaking mechanics

### 4. DEPENDENCY ISSUES WITHIN T17

**Circular or confusing dependencies:**

**T17.G5.05 dependencies include T09.G3.01.01**
- "Initialize a 2D physics world" depends on "Create a new variable with a descriptive name"
- This seems unnecessary - you don't need variables to initialize physics world
- Likely copy-paste error in dependency list

**T17.G5.06.A has same dependencies as T17.G5.06**
- Both have identical T07, T08, T09 dependencies
- G5.06.A should only depend on G5.06, not repeat all its dependencies

**Multiple skills have identical 4-dependency sets:**
- T07.G3.01, T08.G3.00, T09.G3.01.01 appear together in many G5 skills
- This suggests these are copied template dependencies rather than carefully considered
- Many of these are likely unnecessary (e.g., why does choosing collision shapes need variable creation?)

**Cross-topic dependency gaps:**
- T17.G8.01 depends on T18.G6.01.01 (from Topic 18: 3D Worlds)
- This creates a forward dependency on 3D physics before mastering 2D
- Should be T17.G7.02 or similar 2D force skill instead

**Missing internal dependencies:**

**T17.G6.02.01.01, .02, .03 are siblings but could have linear progression**
- All three depend only on T17.G6.02.01
- But .03 (rotation speed) could depend on .02 (read velocity) for verification pattern

**T17.G7.01.01 and .02 are independent but could sequence**
- Both depend on T17.G7.01
- But "Enable CCD" (.02) should probably come after "Point sprite in movement direction" (.01)

**T17.G8.02.01.01 has excessive dependencies**
- Depends on T25.G6.01 (Document metadata for datasets) and T33.G6.01 (Cloud blocks)
- These seem completely unrelated to revolute joint motors
- Likely copy-paste error

**Missing prerequisite for complex shapes:**
- T17.G5.06.03 (compound shapes) depends on T17.G5.06.01 (Box vs Circle)
- Should also depend on T17.G5.06.01.02 (Convex Hull) since compound shapes are more advanced

**Grade-level inconsistencies:**

**T17.G5.12 capstone comes too early**
- "Choose manual vs engine-based physics" requires experience with both
- But many engine features (friction, restitution, collision groups) come in G6
- Should be moved to G6 or G7

**T17.G6.04.02 ground detection seems early**
- Platformer-specific skill but general collision groups come later (G6.05)
- Order might be reversed

### 5. ADDITIONAL OBSERVATIONS

**Excellent progression in many areas:**
- The manual velocity skills (G5.02-G5.04) provide strong conceptual foundation
- The physics engine introduction (G5.05-G5.12) is well-scaffolded
- Shape progression (Box/Circle → Capsule → Convex Hull → Compound) is logical

**Strong sub-skill organization:**
- The .01, .02, .03 numbering helps show related concepts
- The .A practice skills are a good pattern (e.g., G5.06.A)

**Good real-world connections:**
- Skills like G6.08 (Compare simulations to real-world motion) and G7.06 (Model a real-world physics scenario) connect theory to practice

**Performance and optimization addressed:**
- G8.04 and G8.04.01 cover performance considerations
- This is often missing in physics curricula

**Missing topics that could be added:**
- Raycasting for line-of-sight or laser beams
- Physics materials (predefined surface property sets)
- Collision masks/categories (more advanced than groups)
- Springs and distance joints
- Rope/chain joints
- Particle systems with physics
- Camera following physics objects
- Physics-based sound effects (collision intensity → volume)

---

## SUMMARY STATISTICS

- **Total T17 Skills:** 105 skills
- **Grade K:** 2 skills
- **Grade 1:** 1 skill
- **Grade 2:** 1 skill
- **Grade 3:** 2 skills
- **Grade 4:** 2 skills
- **Grade 5:** 28 skills (largest grade level)
- **Grade 6:** 33 skills (largest grade level)
- **Grade 7:** 17 skills
- **Grade 8:** 19 skills

**Skill Distribution Pattern:**
- Early grades (K-4): Conceptual understanding with 8 skills
- Middle grades (5-6): Heavy technical implementation with 61 skills (58% of total)
- Upper grades (7-8): Application and advanced features with 36 skills

**Dependency Patterns:**
- Most G5 skills have 4-5 dependencies (includes repeated T07/T08/T09 dependencies)
- G6-G8 skills have more selective dependencies focused on prior physics skills
- Cross-topic dependencies increase in G6-G8 (connecting to variables, conditionals, lists, etc.)

---

## RECOMMENDATIONS

1. **Add T17.G5.01** - The missing "Apply gravity to a sprite using 2D physics" skill that's referenced in dependencies
2. **Clean up template dependencies** - Remove unnecessary T07/T08/T09 dependencies that appear copied across many skills
3. **Fix cross-topic dependencies** - Replace T18 dependency in T17.G8.01 with appropriate T17 skill
4. **Add force application skill** - Bridge between impulses (G5.08) and combining forces (G7.02)
5. **Move T17.G5.12** - Relocate "Choose manual vs engine-based physics" to G6 after more experience
6. **Add joint debugging** - Include skills for troubleshooting joint constraints (G8 level)
7. **Clarify sensor vs collision skills** - Better distinguish T17.G5.06.02 from T17.G6.04.04
8. **Add raycasting** - Consider adding physics raycast skills for line-of-sight detection (G7-G8)
9. **Review G8.02.01.01 dependencies** - Remove unrelated T25 and T33 dependencies
10. **Add bridge skills in early grades** - More K-G1 transition skills for motion concepts
