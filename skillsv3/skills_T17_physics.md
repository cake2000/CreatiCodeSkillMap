# T17 – Motion & Physics: K–8 Skill List (Draft v1)

Topic reference: `T17 Motion & Physics` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, Systems and Security (SAS‑IM)

Each skill below has:

- a stable **ID** (`T17.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Physics in early grades is about informal motion and pattern observation rather than formal physics.

### T17.GK.01 – Spot moving objects (observation)

- **Short name:** Identify things that move in pictures
- **Description:** Students recognize and point out objects in motion (e.g., a ball rolling, a person jumping) and distinguish moving things from still things. This establishes foundational awareness of motion.
- **Challenge format:** Concept, multiple choice or matching. Show 3–4 picture scenes; students identify which objects are moving or which direction something moves. Auto‑grading checks selections.
- **CSTA:** EK‑SAS‑IM‑03 (categorizing computing tools and their impacts).

### T17.GK.02 – Act out gravity (unplugged motion)

- **Short name:** Gravity makes things fall
- **Description:** Students understand through physical experience (dropping objects, rolling balls down slopes) that gravity pulls things downward. They use simple language like "falls down" and observe patterns.
- **Challenge format:** Concept and hands-on. Drop different small objects and observe where they land; compare heavy and light items. Discuss results. Auto‑grading uses teacher observation notes or simple video check.
- **CSTA:** EK‑SAS‑IM‑03.

### T17.GK.03 – Describe bouncing and falling

- **Short name:** Tell what a bouncing ball does
- **Description:** Students watch a short animation or video of a bouncing ball or falling object and describe in their own words what they see: "it goes down," "it bounces," etc. This builds vocabulary and observation skills.
- **Challenge format:** Concept, open‑ended response with sentence stems. A CreatiCode project shows a bouncing animation. Students complete a sentence: "The ball _____ down and _____ back up." Auto‑grading uses keyword matching.
- **CSTA:** EK‑SAS‑IM‑03.

---

## Grade 1

Grade 1 introduces simple motion logic and the beginnings of physics concepts through Scratch blocks, not yet as a formal physics engine.

### T17.G1.01 – Move a sprite down (manual gravity)

- **Short name:** Make a sprite fall down
- **Description:** Students create a simple script where a sprite moves downward repeatedly (e.g., `move 5 steps down` in a loop or repeated blocks), simulating a basic falling motion without using physics blocks.
- **Challenge format:** Coding, starter project. Provided: a sprite above the stage. Prompt: "Make the sprite fall by moving it down. Use move blocks." Students build the script. Auto‑grading checks that the sprite moves downward and reaches the bottom.
- **CSTA:** E1‑PRO‑PF‑01, E1‑ALG‑AF‑01.

### T17.G1.02 – Bounce off the floor (bounce block)

- **Short name:** Bounce when touching the edge
- **Description:** Students use the "if on edge, bounce" block to make a sprite that moves bounce off the stage edges. This introduces the concept of a boundary and simple collision.
- **Challenge format:** Coding, starter project. Provided: a sprite with a move block. Students add "if on edge, bounce" to the script. Auto‑grading verifies the sprite bounces off edges when run.
- **CSTA:** E1‑PRO‑PF‑01.

### T17.G1.03 – Predict where a falling sprite lands

- **Short name:** Where will the sprite land?
- **Description:** Given a short script where a sprite moves downward for a fixed number of steps, students predict where on the stage it will end up, relating motion distance to final position.
- **Challenge format:** Concept, interactive visualization. A tiny script is shown (e.g., `repeat 8 { move 10 steps down }`). Students choose the correct final y-position from options. Auto‑grading compares answer to simulation.
- **CSTA:** E1‑PRO‑PF‑01.

### T17.G1.04 – Simulate a jump (temporary y-position change)

- **Short name:** Make a sprite jump
- **Description:** Students manually code a jump by moving a sprite up a few steps, waiting, then moving it back down. This builds intuition for motion sequences and is a precursor to physics-based jumping.
- **Challenge format:** Coding, guided construction. Starter project has a sprite and example blocks. Prompt: "Make the sprite jump up and come back down." Students arrange move, turn, and wait blocks. Auto‑grading checks sequence and that sprite returns to starting position.
- **CSTA:** E1‑PRO‑PF‑01.

---

## Grade 2

Grade 2 continues manual motion simulation and introduces the first elements of physics thinking (friction, resistance).

### T17.G2.01 – Slow down a falling sprite (simple friction)

- **Short name:** Slow the fall with smaller steps
- **Description:** Students modify a falling sprite script so that the sprite's downward motion gradually slows (by decreasing the distance moved each step). This mimics friction or air resistance.
- **Challenge format:** Coding, refactor challenge. Starter script has a sprite moving down with constant speed. Prompt: "Make the sprite slow down as it falls." Students modify the move distance in a loop. Auto‑grading checks that step sizes decrease.
- **CSTA:** E2‑PRO‑PF‑01.

### T17.G2.02 – Make a bouncing ball reduce bounce height

- **Short name:** Ball bounces lower each time
- **Description:** Students create a script where a sprite bounces multiple times, with each bounce being smaller than the previous one. This simulates energy loss in real bounces.
- **Challenge format:** Coding, starter project. Provided: a sprite with a bounce animation. Prompt: "Make the ball bounce 3 times, getting smaller each time." Students use move and scale blocks, or repeated bounce sequences with decreasing amounts. Auto‑grading checks for decreasing bounce amplitudes.
- **CSTA:** E2‑PRO‑PF‑01.

### T17.G2.03 – Create a rolling motion (horizontal sliding)

- **Short name:** Make a sprite roll or slide across the stage
- **Description:** Students build a script where a sprite moves horizontally (side to side) and gradually slows down, simulating rolling with friction.
- **Challenge format:** Coding, starter project. Provided: a sprite. Prompt: "Make the sprite roll across the stage and slow down." Students use horizontal move blocks, optionally with costume changes to simulate rolling. Auto‑grading checks horizontal motion and deceleration.
- **CSTA:** E2‑PRO‑PF‑01.

### T17.G2.04 – Identify motion variables

- **Short name:** What changes about the moving sprite?
- **Description:** Given a simple falling or bouncing animation, students identify which properties change (position, speed, direction) and which stay the same (size, color unless changed).
- **Challenge format:** Concept, multiple choice checklist. A sprite animation plays. Students select which properties change: position, speed, direction, size, etc. Auto‑grading checks correct selections.
- **CSTA:** E2‑PRO‑PF‑01, E2‑PRO‑DH‑02.

---

## Grade 3

Grade 3 introduces the CreatiCode 2D physics engine and structured approaches to gravity and forces.

### T17.G3.01 – Initialize a 2D physics world

- **Short name:** Set up the physics engine
- **Description:** Students use the "Initialize 2D Physics" block from CreatiCode's physics category to set up a physics-enabled world with gravity. They learn the concept of a physics world and adjustable gravity.
- **Challenge format:** Coding, guided setup. Starter project has an empty script. Prompt: "Add a physics initialization block to set gravity to -100 in Y." Students add the block and run it. Auto‑grading checks for the block's presence and parameter value.
- **CSTA:** E3‑PRO‑PF‑01, SAS‑IM (understanding systems).

### T17.G3.02 – Add a physics body to a sprite (gravity effect)

- **Short name:** Make a sprite fall with physics
- **Description:** Students attach a physics body to a sprite (setting it to dynamic and optionally specifying mass), so that gravity automatically pulls it downward. They observe realistic falling motion without manually coding position changes.
- **Challenge format:** Coding, starter project. Provided: physics world initialized, a sprite in the upper stage. Prompt: "Add a physics body to the sprite so it falls due to gravity." Students use the "add physics body to [sprite]" block. Auto‑grading checks sprite falls and doesn't go below stage.
- **CSTA:** E3‑PRO‑PF‑01.

### T17.G3.03 – Create a platform using a static physics body

- **Short name:** Build a static floor
- **Description:** Students use a static physics body (one that doesn't move) to create a floor or platform. The sprite's dynamic body stops when it hits the static body, learning about collision stopping.
- **Challenge format:** Coding, starter project. Provided: physics world, a falling sprite with dynamic body, an empty floor sprite. Prompt: "Add a physics body to the floor (make it static) so the falling sprite stops." Auto‑grading checks that sprite stops on contact.
- **CSTA:** E3‑PRO‑PF‑01.

### T17.G3.04 – Apply a force to jump (impulse)

- **Short name:** Use a force to make the sprite jump
- **Description:** Students apply an upward impulse or force to a physics-enabled sprite (e.g., in response to a key press) to make it jump. This introduces the concept of applying forces to change motion.
- **Challenge format:** Coding, starter project. Provided: physics world, a sprite with dynamic body standing on a platform. Prompt: "When the space key is pressed, apply an upward force to make the sprite jump." Students use "apply impulse" or "apply force" blocks. Auto‑grading checks that sprite jumps on key press.
- **CSTA:** E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 develops more complex physics simulations, combining forces, friction, and collisions.

### T17.G4.01 – Adjust friction for realistic motion

- **Short name:** Add friction to slow sliding
- **Description:** Students set the friction property on a physics body so that a sliding sprite gradually slows down due to friction, rather than moving at constant speed or decreasing manually.
- **Challenge format:** Coding, comparative challenge. Provided: two sprites side-by-side, both given a horizontal impulse, one with high friction and one with low. Prompt: "Adjust the friction values so one slides farther than the other." Students modify friction values. Auto‑grading compares final positions.
- **CSTA:** E4‑PRO‑PF‑01.

### T17.G4.02 – Control bounciness (restitution)

- **Short name:** Make a bouncy or non-bouncy ball
- **Description:** Students adjust the restitution (bounciness) property of a physics body to control how much a sprite bounces when it hits a surface. Higher restitution means more bounce.
- **Challenge format:** Coding, guided experiment. Starter project: a sprite with physics body above a floor, with a slider widget or variable to control restitution. Prompt: "Change the restitution value and observe how the ball bounces." Students test values. Auto‑grading checks that different restitution values yield different bounce heights.
- **CSTA:** E4‑PRO‑PF‑01.

### T17.G4.03 – Detect collisions between physics bodies

- **Short name:** Check when two sprites collide
- **Description:** Students use a collision detection block or condition to determine when two physics-enabled sprites touch. This can trigger events like scoring or sprite removal.
- **Challenge format:** Coding, starter project. Provided: a player sprite, a collectible sprite, both with physics bodies. Prompt: "When the player touches the collectible, increase the score." Students use a collision condition inside a loop. Auto‑grading checks that score increases on collision.
- **CSTA:** E4‑PRO‑PF‑01.

### T17.G4.04 – Build a simple pendulum or swinging motion

- **Short name:** Create a swinging object
- **Description:** Students create a sprite that swings back and forth using forces or by updating its angle in a loop. This explores circular/rotational motion with physics concepts.
- **Challenge format:** Coding, starter project. Prompt: "Create a pendulum by making a sprite swing back and forth." Students can use forces and torque, or simple angle changes in a loop. Auto‑grading checks for oscillating motion pattern.
- **CSTA:** E4‑PRO‑PF‑01.

---

## Grade 5

Grade 5 combines multiple physics concepts into more complex simulations and introduces multi-body systems.

### T17.G5.01 – Simulate a projectile (gravity + initial velocity)

- **Short name:** Launch a projectile with angle and speed
- **Description:** Students create a sprite that starts with an initial velocity at an angle and follows a parabolic path under gravity. This is the classic projectile motion simulation.
- **Challenge format:** Coding, starter project with parameters. Provided: a physics world, a sprite with dynamic body, input sliders for launch angle and speed. Prompt: "Apply an initial force at the given angle so the sprite follows a curved path." Students use force/impulse blocks and trigonometry or preset angle values. Auto‑grading checks that trajectory is parabolic.
- **CSTA:** E5‑PRO‑PF‑01, DAA‑DI.

### T17.G5.02 – Create a multi-object system (chain or stack)

- **Short name:** Stack or chain multiple physics objects
- **Description:** Students create a system of several physics-enabled sprites (e.g., stacked boxes, a chain of connected objects) and observe how forces propagate through the system.
- **Challenge format:** Coding, creative challenge. Prompt: "Create a stack of at least 3 boxes with physics bodies. Apply a force to the bottom box and observe what happens." Students build the stack and apply forces. Auto‑grading checks code structure and that the system responds to forces.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.03 – Simulate air resistance or drag

- **Short name:** Air resistance slows falling objects
- **Description:** Students approximate air resistance by applying a velocity-dependent force (or by decreasing velocity each step) as a sprite falls, making heavier objects fall faster than light ones (in a simplified model).
- **Challenge format:** Coding, comparative project. Prompt: "Create two falling sprites with different masses. The heavier one should accelerate faster." Students create two sprites, each with appropriate physics properties. Auto‑grading compares falling speeds.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.04 – Collision groups for selective interactions

- **Short name:** Use collision groups to control what collides
- **Description:** Students set collision groups on physics bodies so that certain sprites collide with some objects but not others (e.g., player passes through powerups but collides with enemies).
- **Challenge format:** Coding, game scenario. Provided: player, enemies, and powerups, each with physics bodies. Prompt: "Set collision groups so the player collides with enemies but passes through powerups." Auto‑grading checks that collisions happen only as specified.
- **CSTA:** E5‑PRO‑PF‑01.

---

## Grade 6

Grade 6 applies physics to game design and more complex simulations, emphasizing systems thinking.

### T17.G6.01 – Design a platformer with physics

- **Short name:** Build a physics-based platformer level
- **Description:** Students create a simple platformer game with physics-enabled player, platforms, gravity, and jumping. They design a level layout and test the physics feel.
- **Challenge format:** Coding, design challenge. Prompt: "Create a small platformer level (5–6 platforms) where the player can jump between them. Test and refine the feel." Students build platforms with static bodies, player with dynamic body, jump controls. Auto‑grading checks code structure and that the level is playable.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.02 – Trace physics simulation logic

- **Short name:** Predict motion from physics values
- **Description:** Given a set of physics values (gravity, mass, velocity, friction) for a sprite, students trace what will happen over several steps and predict the final position or behavior.
- **Challenge format:** Concept, code‑reading item. Show a script with initial conditions and physics blocks. Ask: "If gravity is -100, initial velocity is +50 up, and mass is 10, where will the sprite be after 5 seconds?" with choices. Auto‑grading compares to simulation.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.03 – Debug physics simulation (unexpected motion)

- **Short name:** Fix strange physics behavior
- **Description:** Students are given a physics simulation that behaves unexpectedly (e.g., sprite falls too fast, bounces too high, doesn't stop) and modify physics properties to fix it.
- **Challenge format:** Coding, debugging challenge. Starter project: a sprite that falls off-screen immediately or behaves oddly. Prompt: "The sprite is falling too fast. Adjust gravity or mass to fix it." Students modify values. Auto‑grading checks that behavior matches specification.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T17.G6.04 – Compare physics engine behavior to real-world motion

- **Short name:** Evaluate realism of simulated motion
- **Description:** Students compare a physics simulation to real-world observations (e.g., dropping a ball, bouncing a ball) and discuss whether the simulation matches reality or where it simplifies.
- **Challenge format:** Concept and reflection. Prompt: "Compare your simulated bouncing ball to a real ball. Is the bounce pattern similar? What's different?" Students run simulation, test real ball, answer comparison questions. Auto‑grading scores responses for thoughtful observation.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

---

## Grade 7

Grade 7 explores advanced physics simulations, including more realistic forces and multi-body interactions.

### T17.G7.01 – Simulate friction in different media (water, air, ground)

- **Short name:** Different surfaces have different friction
- **Description:** Students create multiple sprites sliding on surfaces with different friction values (high friction ground, low friction ice, medium friction carpet) and observe how each behaves differently.
- **Challenge format:** Coding, comparative simulation. Prompt: "Create three platforms with different friction values. Apply the same impulse to three sprites and compare how far each slides." Students build and observe. Auto‑grading checks that friction values differ and sprites stop at different distances.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T17.G7.02 – Apply multiple forces simultaneously

- **Short name:** Combine forces for complex motion
- **Description:** Students apply more than one force to a sprite (e.g., gravity and wind, or gravity and a player-applied thrust) and observe the resulting motion as the vector sum of forces.
- **Challenge format:** Coding, starter project. Prompt: "Make a sprite fall due to gravity, but also apply a horizontal wind force. Observe the combined motion." Students use two force blocks. Auto‑grading checks that motion reflects combined forces (parabolic path, drift).
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G7.03 – Model a real physics scenario (pendulum, orbit, rolling object)

- **Short name:** Simulate a real-world physics scenario
- **Description:** Students choose a real physics phenomenon (e.g., a pendulum, a ball rolling downhill, a satellite orbiting) and create a CreatiCode simulation that reasonably approximates the physics.
- **Challenge format:** Coding, design and simulation challenge. Prompt: "Choose a physics scenario (pendulum, orbit, rolling ball, etc.) and build a simulation. Document what physics properties you used." Students implement simulation. Auto‑grading checks code structure and that behavior is plausible for the chosen scenario.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T17.G7.04 – Measure and analyze motion data (position, velocity, acceleration)

- **Short name:** Track sprite motion data over time
- **Description:** Students log position, velocity, and/or acceleration of a physics-simulated sprite to a list or table, then analyze the data to verify expected physics patterns (e.g., constant acceleration under gravity).
- **Challenge format:** Coding, data analysis project. Prompt: "Log the y-position of a falling sprite every frame for 3 seconds. Create a graph and verify that acceleration is constant." Students use a data-logging loop. Auto‑grading checks data structure and analysis process.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP/DI.

---

## Grade 8

Grade 8 applies physics to complex game and simulation projects, emphasizing design trade-offs and system optimization.

### T17.G8.01 – Design and balance a physics-based arcade game

- **Short name:** Create a physics arcade game (Angry Birds style)
- **Description:** Students design a physics-based arcade game (similar to Angry Birds, a catapult puzzle, or a gravity-assisted platformer) where projectiles, gravity, and collisions are core mechanics.
- **Challenge format:** Coding, design and implementation project. Prompt: "Design a simple physics-based arcade game: (1) a launcher, (2) projectiles, (3) target objects, and (4) gravity. Test balance and adjust difficulty." Students implement full game. Auto‑grading checks code structure, physics implementation, and playability.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PD.

### T17.G8.02 – Optimize a physics simulation for performance

- **Short name:** Improve simulation efficiency
- **Description:** Students work with a physics simulation that has many objects and optimize it by adjusting gravity updates, reducing collision checks, or culling off-screen objects to maintain smooth performance.
- **Challenge format:** Coding, optimization challenge. Provided: a simulation with 10+ physics objects that runs slowly. Prompt: "Optimize this simulation to run smoothly. What changes did you make?" Students profile performance and modify code. Auto‑grading measures frame rate improvement.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T17.G8.03 – Implement a physics constraint or joint

- **Short name:** Connect objects with a physics joint
- **Description:** Students use advanced physics features (e.g., a weld joint, hinge joint, or distance constraint) to connect two sprites so they move together or rotate around a pivot.
- **Challenge format:** Coding, starter project. Prompt: "Create a two-sprite system: a rod and a hanging weight. Use a physics constraint to connect them so the weight swings like a pendulum." Students use joint blocks. Auto‑grading checks constraint function.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G8.04 – Design a realistic vs stylized physics feel

- **Short name:** Choose physics parameters for game feel
- **Description:** Students design a game (e.g., platformer) with two variants: one with realistic physics and one with stylized (unrealistic but fun) physics. They compare and justify design choices.
- **Challenge format:** Coding and reflection. Prompt: "Build two versions of a small platformer: (A) realistic physics (gravity ~-100, normal friction), (B) stylized physics (floaty gravity, less friction). Write pros/cons of each." Students implement both. Auto‑grading checks design differences and reflection depth.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM (understanding impact of system design).
