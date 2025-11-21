# T17 – 2D Motion & Physics: Grades 5–8 Skill List (Draft v3)

Topic reference: `T17 – 2D Motion & Physics` in `domains_topics_overview.md`
Domain: Programming Core & Applications (D2) · CSTA focus: PRO‑PF, PRO‑TR, SAS‑IM

CreatiCode supports **two complementary ways** to model physics:

1. **Manual motion scripts** that store speed, direction, and gravity in variables/lists and update sprite positions
   frame-by-frame (classic Scratch style).  
2. The **CreatiCode 2D Physics extension** (Rapier.js wrapper blocks) that automatically handles gravity, collisions,
   joints, and accurate impulses once sprites have physics bodies.

T17 deliberately teaches **both approaches** so students can decide which fits a particular 2D game prototype (T14) or
simulation before they graduate to 3D physics in T18. CSTA’s draft standards do not call out physics by name, but they
expect students to model program state, predict behavior, and evaluate trade-offs (PRO‑PF, PRO‑TR, SAS‑IM). These skills
fulfill that requirement for motion-heavy projects.

Design commitments:

- **Grades 5–8 only:** Students in Grades K–4 focus on conceptual motion inside T01–T05 and create non-physics games in
  T14. T17 begins at Grade 5, immediately before the T14 G5 skills that depend on realistic collisions and gravity.
- **IXL-style microsteps:** Each skill is a tiny, engaging action (plan → implement → trace → debug) with contexts such as
  pinball tables, slingshot puzzles, or platformers.
- **Explicit dependencies:** Grade introductions and skill blurbs reference prerequisite topics so pathway tools can wire
  T17 nodes before 2D Games (T14) and 3D Worlds (T18).
- **Planning bridge:** Simulation goals, measurements, and fairness checks are planned in **T05 Human‑Centered Design**
  (e.g., T05.G3/T05.G5). T17 focuses on **implementation and debugging** of those plans rather than re-teaching planning.

---

**Grades K–4:** _Intentionally unassigned in this topic._ Students at these levels build sequencing, loops, and motion
intuition via T01–T05, T07, and T14 (non-physics). They meet 2D physics for the first time in Grade 5.

---

## Grade 5

Grade 5 establishes the vocabulary for manual physics scripts **and** introduces the CreatiCode 2D physics engine.
Students decide which approach to use, wire up variables, and then move into physics-body workflows that T14 relies on.

Strands: **G5‑A Manual motion variables**, **G5‑B Physics engine setup**, **G5‑C Trace & debug**

### T17.G5.01 – Choose manual vs engine-based physics

_Dependency:_
  * T01.G3.01: Complete a simple script with missing blocks
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Pick the right physics method
- **Description:** Students compare CreatiCode project briefs (platformer, UI animation, top-down maze, pinball machine) and, drawing on prior simulation planning (T05.G2.03, T05.G4.05), choose whether to stick with manual velocity variables or enable the physics extension. They explain the decision for each brief so later T14 skills inherit the correct dependency.
- **Challenge format:** Concept, drag-and-sort. Students drag each brief into “Manual physics” or “2D physics engine”
  bins and type a short justification. Auto-grading checks placement and keywords.
- **CSTA:** E5‑PRO‑PF‑01, SAS‑IM.

### T17.G5.02 – Track gravity with velocity variables

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Update y-velocity each frame
- **Description:** Students build a loop that stores a sprite’s y-velocity in a variable, subtracts gravity, then adds it
  to the sprite’s position. This manual approach mirrors classic Scratch tutorials and prepares students for physics
  debugging even without the extension.
- **Challenge format:** Coding, starter project. Prompt: “Make the hero fall by updating a `y velocity` variable every
  frame.” Auto-grading checks the variable math and resulting motion.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.03 – Use horizontal speed and friction variables

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Slide with vx and friction
- **Description:** Students add an `x velocity` variable, respond to arrow keys to change it, and multiply by a friction
  factor each tick so motion glides to a stop. This mirrors T14 platformer expectations before physics bodies are added.
- **Challenge format:** Coding, starter project. Students implement horizontal movement with adjustable friction slider.
  Auto-grading inspects code and checks that motion slows when the slider is increased.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.04 – Code a manual bounce with energy loss

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator


- **Short name:** Bounce by flipping velocity
- **Description:** Students write a conditional that checks for ground contact, multiplies the y-velocity by a negative
  damping factor (e.g., ‑0.6), and sends the sprite back up with reduced height. This cements the physics vocabulary in
  block form before using the engine’s restitution settings.
- **Challenge format:** Coding, debugging prompt. Students receive a partially working script and complete the bounce
  logic. Auto-grading runs three drops to verify decreasing bounce heights.
- **CSTA:** E5‑PRO‑PF‑01, PRO‑TR.

### T17.G5.05 – Initialize a 2D physics world

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Start gravity for the scene
- **Description:** Students add the Initialize 2D Physics block, set gravity (e.g., X: 0, Y: -100), and confirm the debug
  overlay shows the world running. They understand that no physics behavior occurs until this block executes.
- **Challenge format:** Coding, guided setup. Starter project has sprites but no physics. Students add the init block,
  choose gravity, and run a provided test button. Auto-grading inspects the script.
- **CSTA:** E5‑PRO‑PF‑01, SAS‑IM.

### T17.G5.06 – Attach a dynamic body to a sprite

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator


- **Short name:** Give a sprite a physics body
- **Description:** Students convert a sprite to a dynamic physics body (selecting density/mass options) so the sprite
  responds to gravity without manual loops. They observe the sprite fall and stop when it hits the stage floor.
- **Challenge format:** Coding, starter project. Prompt: “Add a dynamic body to the hero sprite and press the gravity test
  button.” Auto-grading checks that the sprite’s body type and parameters are correct.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.06.01 – Select appropriate body shapes

_Dependency:_
  * T17.G5.06: Attach a dynamic body to a sprite

- **Short name:** Choose box, circle, or convex hull
- **Description:** Students select the appropriate shape type (Box, Circle, ConvexHull, Capsule) when creating physics bodies. They understand that simpler shapes run faster, while convex hulls match irregular sprites more closely.
- **Challenge format:** Coding, shape matching. Students assign shapes to different sprites and test that collisions feel accurate. Auto-grading checks shape selections match sprite outlines.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.06.02 – Create sensor bodies for trigger zones

_Dependency:_
  * T17.G5.06: Attach a dynamic body to a sprite

- **Short name:** Make a non-solid trigger zone
- **Description:** Students create sensor bodies that detect collisions but do not physically block other sprites. Sensors are used for collectibles, checkpoints, and invisible trigger zones that start events.
- **Challenge format:** Coding, trigger setup. Students configure a sensor body that broadcasts a message when the player enters. Auto-grading verifies the player passes through without bouncing.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.06.03 – Create compound shapes for complex sprites

_Dependency:_
  * T17.G5.06.01: Select appropriate body shapes

- **Short name:** Combine shapes for concave sprites
- **Description:** Students use the compound shape block to create physics bodies for sprites that cannot be represented by a single convex shape (L-shapes, characters with arms). They combine multiple simple shapes into one body.
- **Challenge format:** Coding, compound body. Students build a compound shape for an irregular sprite and test that collisions work correctly. Auto-grading checks the compound body setup.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.07 – Build static boundaries for floors and walls

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Create static walls to stop sprites
- **Description:** Students add static physics bodies to floor or wall sprites so falling or sliding objects stop on
  contact. They learn to use static bodies for geometry that should not move.
- **Challenge format:** Coding, starter project. Students configure boundary sprites as static bodies and rerun the gravity
  test to ensure the player lands and cannot exit the screen. Auto-grading checks collision behavior.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.08 – Apply an impulse to jump or push

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Tap to jump with impulse
- **Description:** Students apply an upward impulse or horizontal shove to a dynamic sprite in response to input (e.g.,
  space key or on-screen button). They control how strong the impulse is so the sprite clears a target platform.
- **Challenge format:** Coding, starter project. Prompt: “When SPACE is pressed, apply an impulse that lets the hero clear
  the first platform.” Auto-grading checks for the impulse block and resulting jump height.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.08.01 – Distinguish forces from impulses

_Dependency:_
  * T17.G5.08: Apply an impulse to jump or push

- **Short name:** Know when to use force vs impulse
- **Description:** Students understand the difference between continuous forces (applied every frame for thrust, wind) and one-time impulses (instant kick for jumps, hits). They choose the correct block for different scenarios.
- **Challenge format:** Concept + coding. Students match scenarios to force/impulse and implement both in a test scene. Auto-grading checks correct block selection for each mechanic.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.08.02 – Apply force at a position for rotation effects

_Dependency:_
  * T17.G5.08.01: Distinguish forces from impulses

- **Short name:** Push off-center to spin
- **Description:** Students apply forces or impulses at positions other than the center of a physics body to create rotation. They understand that off-center forces produce torque in addition to linear motion.
- **Challenge format:** Coding, rotation lab. Students push a box at different positions and observe the resulting spin. Auto-grading checks for force-at-position block usage.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.09 – **[Engine Skill]** Configure gravity and mass parameters

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Set precise physics values (technical)
- **Description:** Students adjust gravity strength and sprite mass using numeric inputs to achieve specific physics behaviors (exact fall time, bounce height). They learn to read physics specifications and translate them into parameter values.
- **Challenge format:** Coding, parameter lab. Students use sliders and numeric inputs to achieve target measurements. Auto-grading checks parameter values and physics measurements.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.09b – **[Creative Skill]** Tune physics feel for player experience

_Dependency:_
  * T17.G5.09: Configure gravity and mass parameters
  * T05.G5.06: Plan simulations with specific requirements

- **Short name:** Adjust physics for game feel (creative)
- **Description:** Students, informed by simulation planning, adjust gravity and mass to create desired player emotions (heavy/floaty, challenging/forgiving). They explain how physics parameters support gameplay goals.
- **Challenge format:** Creative iteration challenge. Students adjust parameters to match creative briefs ("make jumping feel heroic" vs "create realistic falling"). Auto-grading evaluates alignment between settings and creative goals.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.10 – Trace simple 2D physics motion

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Predict landing spot from settings
- **Description:** Students read a small table showing gravity, mass, starting height, and time elapsed, then choose the
  correct statement about where the sprite will be (e.g., “lands on the platform,” “still in the air,” “passed through
  the floor”).
- **Challenge format:** Concept, interactive trace. A visualization panel shows the parameters; students select from
  multiple conclusions. Auto-grading compares answers to a hidden simulation.
- **CSTA:** E5‑PRO‑PF‑01, PRO‑TR.

### T17.G5.10.01 – Remove physics body from a sprite

_Dependency:_
  * T17.G5.06: Attach a dynamic body to a sprite

- **Short name:** Turn off physics for a sprite
- **Description:** Students use the remove physics behavior block to disconnect a sprite from the physics engine. This is essential for destroying objects, transitioning sprites to manual control, or resetting game states.
- **Challenge format:** Coding, removal task. Students remove a physics body when a sprite is collected or leaves the screen. Auto-grading verifies the sprite no longer responds to physics forces.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.11 – Debug missing physics setup

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator


- **Short name:** Fix a sprite that ignores gravity
- **Description:** Students open a buggy project where the player never falls because the physics world was not
  initialized or the body was left as static/manual. They inspect the scripts, correct the setup, and re-test.
- **Challenge format:** Coding, debugging challenge. Students identify the missing block or wrong body type and fix it.
  Auto-grading confirms that the sprite now falls and collides properly.
- **CSTA:** E5‑PRO‑PF‑01, PRO‑TR.

---

## Grade 6

Grade 6 layers in surface properties, interactions, and hybrid scenes where manual and engine-based sprites coexist in
T14 games. Students refine collisions, scoring, and stability while comparing engine output to real-world motion.

Strands: **G6‑A Control surfaces**, **G6‑B Manage interactions**, **G6‑C Blend & evaluate**

### T17.G6.01 – **[Engine Skill]** Configure surface friction parameters

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T17.G5.10: Trace simple 2D physics motion


- **Short name:** Set friction values (technical)
- **Description:** Students adjust the friction property numerically and measure how far objects travel on different surfaces. They learn to map friction coefficients to sliding distances through systematic testing.
- **Challenge format:** Coding, measurement lab. Students set specific friction values, measure results, and record the relationship between parameters and physics outcomes. Auto-grading checks numerical accuracy.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.01b – **[Creative Skill]** Design surface feel for game environments

_Dependency:_
  * T17.G6.01: Configure surface friction parameters

- **Short name:** Choose friction for story/gameplay (creative)
- **Description:** Students select friction values to create desired environmental storytelling (ice, wood, carpet) and gameplay experiences. They explain how surface properties enhance narrative and player challenge.
- **Challenge format:** Creative implementation. Students choose friction settings to support environmental themes and explain the connection between physics properties and story/gameplay goals.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.02 – **[Engine Skill]** Control restitution parameters

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes


- **Short name:** Set bounce coefficients (technical)
- **Description:** Students modify the restitution property numerically and measure bounce heights. They learn the relationship between restitution values (0.0-1.0) and energy conservation in collisions.
- **Challenge format:** Coding, measurement lab. Students use sliders to test restitution values and record bounce height data. Auto-grading checks correlation between restitution and measured bounce.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.02b – **[Creative Skill]** Design bounce feel for game mechanics

_Dependency:_
  * T17.G6.02: Control restitution parameters

- **Short name:** Choose bounce for gameplay (creative)
- **Description:** Students select restitution values to create specific gameplay experiences (lively pinball bumpers, soft landing zones). They explain how bounce properties enhance game mechanics and player feel.
- **Challenge format:** Creative implementation. Students design bounce behaviors to support game mechanics and justify choices based on player experience goals.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.02.01 – Set velocity directly for physics bodies

_Dependency:_
  * T17.G5.06: Attach a dynamic body to a sprite
  * T17.G6.02: Control restitution parameters

- **Short name:** Set x/y speed directly
- **Description:** Students use the set x speed and set y speed blocks to directly control a physics body's velocity without applying forces or impulses. This is useful for instant speed changes, velocity limits, or resetting motion.
- **Challenge format:** Coding, velocity control. Students set velocity limits so a falling object never exceeds a terminal velocity. Auto-grading checks the velocity clamping behavior.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.03 – Build a kinematic moving platform

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.04: Trace code with variables to predict outcomes
  * T17.G5.10: Trace simple 2D physics motion


- **Short name:** Move platforms without gravity
- **Description:** Students convert a sprite to a kinematic body so it ignores gravity but still collides with the player.
  They script its left-right motion and ensure the player rides it safely.
- **Challenge format:** Coding, starter project. Prompt: “Create a kinematic moving platform that carries the player
  across a gap.” Auto-grading checks for kinematic status and reliable transport.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.04 – Detect collisions for scoring or triggers

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.04: Trace code with variables to predict outcomes
  * T17.G5.10: Trace simple 2D physics motion


- **Short name:** Score points when physics sprites meet
- **Description:** Students listen for collision events between named sprites (player hits coin, ball hits bumper) and run
  scoring or state-change scripts in response.
- **Challenge format:** Coding, starter project. Provided sensors emit messages on collision; students hook them to a
  scoreboard. Auto-grading checks scoring accuracy and reset conditions.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑DH.

### T17.G6.04.01 – Detect collision end events

_Dependency:_
  * T17.G6.04: Detect collisions for scoring or triggers

- **Short name:** React when sprites stop touching
- **Description:** Students use the collision end broadcast block to detect when two physics bodies stop colliding. This enables behaviors like resetting states after leaving a zone or ending power-up effects.
- **Challenge format:** Coding, exit detection. Students implement a speed boost zone that activates on entry and deactivates on exit. Auto-grading checks both collision start and end handling.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.04.02 – Use ground detection for platformer jumping

_Dependency:_
  * T17.G6.04: Detect collisions for scoring or triggers

- **Short name:** Check if sprite is on ground
- **Description:** Students enable raycast-based ground detection to determine if a character is standing on a surface. They use the "in collision below" reporter to allow jumping only when grounded, preventing infinite air jumps.
- **Challenge format:** Coding, platformer jump. Students implement grounded jumping that only works when the player is touching the floor. Auto-grading tests for proper ground detection usage.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.05 – Use collision groups to filter interactions

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes


- **Short name:** Choose who collides
- **Description:** Students assign collision groups or masks so the player can pass through collectibles but still hit
  hazards. They reason about selective interactions in crowded levels.
- **Challenge format:** Coding, puzzle scene. Students set group numbers according to a table. Auto-grading simulates
  collisions and confirms only allowed pairs interact.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.05.01 – Use dominance groups for one-way interactions

_Dependency:_
  * T17.G6.05: Use collision groups to filter interactions

- **Short name:** Make heavy objects push light ones
- **Description:** Students set dominance groups so that higher-dominance bodies push lower-dominance bodies without being pushed back. This creates one-way platforms, bulldozer effects, or immovable player characters.
- **Challenge format:** Coding, dominance setup. Students configure dominance so the player can push boxes but boxes cannot push the player. Auto-grading tests collision asymmetry.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.06 – Blend manual and engine sprites in a level

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.04: Trace code with variables to predict outcomes
  * T17.G5.10: Trace simple 2D physics motion


- **Short name:** Mix manual movers with physics bodies
- **Description:** Students keep manual scripts (e.g., scrolling backgrounds, UI-driven particles) running alongside
  physics bodies in the same T14 level without conflicts. They ensure manual sprites do not accidentally inherit physics
  forces and vice versa.
- **Challenge format:** Coding, integration task. Students toggle physics on/off for selected sprites and write comments
  documenting why. Auto-grading checks sprite settings and script separation.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PM.

### T17.G6.06.01 – Lock movement or rotation of physics bodies

_Dependency:_
  * T17.G5.06: Attach a dynamic body to a sprite
  * T17.G6.06: Blend manual and engine sprites in a level

- **Short name:** Prevent unwanted motion or spin
- **Description:** Students use the prevent body movement and prevent body rotation blocks to lock specific degrees of freedom. This keeps platformer characters upright, creates objects that only slide horizontally, or prevents rotation on stacked items.
- **Challenge format:** Coding, lock constraints. Students lock a character's rotation so it stays upright while being pushed. Auto-grading checks the locking behavior works correctly.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.07 – Debug unstable physics behavior

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T09.G3.04: Trace code with variables to predict outcomes


- **Short name:** Fix jittery or sinking sprites
- **Description:** Students diagnose why a sprite jitters, sinks through a platform, or flies off-screen (e.g., mass too
  low, time step too large, conflicting impulses) and adjust parameters to stabilize the scene.
- **Challenge format:** Coding, debugging lab. Students tweak gravity, density, or damping based on clues. Auto-grading
  checks that the sprite stays within tolerances after the fix.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T17.G6.07.01 – Configure world border properties

_Dependency:_
  * T17.G5.05: Initialize a 2D physics world
  * T17.G6.07: Debug unstable physics behavior

- **Short name:** Set stage wall friction and bounce
- **Description:** Students configure the friction and restitution of the four invisible world border walls created during physics initialization. They adjust these properties to control how sprites interact with stage boundaries.
- **Challenge format:** Coding, border setup. Students make the left wall bouncy and the floor sticky, then test ball behavior against each. Auto-grading checks different border properties are applied.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.08 – Compare simulations to real-world motion

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.04: Trace code with variables to predict outcomes
  * T17.G5.10: Trace simple 2D physics motion


- **Short name:** Test if the simulation feels real
- **Description:** Students record bounce heights or slide distances in both CreatiCode and a quick classroom demo, then
  compare graphs to discuss how closely the simulation matches reality and what simplifications exist.
- **Challenge format:** Concept + reflection. Students upload measurements, overlay two line graphs, and answer prompts
  about similarities/differences. Auto-grading looks for specific comparisons.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

---

## Grade 7

Grade 7 pushes 2D physics into multi-force systems, drag, stacks/chains, and instrumentation to verify whether a
simulation satisfies constraints. Students are ready to connect these experiences directly to T14 boss levels and to
T18’s spatial reasoning.

Strands: **G7‑A Advanced motion**, **G7‑B Multi-body systems**, **G7‑C Measure & justify**

### T17.G7.01 – Launch a configurable projectile

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T17.G6.08: Compare simulations to real-world motion


- **Short name:** Set angle and speed for projectiles
- **Description:** Students create a launcher where users set angle/speed sliders. The projectile receives an initial
  impulse that produces a parabolic arc, and targets are placed at measurable distances.
- **Challenge format:** Coding, design challenge. Students wire sliders to the impulse block and verify hits on given
  targets. Auto-grading checks for correct parameter math and hit detection.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T17.G7.01.01 – Point sprite in movement direction

_Dependency:_
  * T17.G7.01: Launch a configurable projectile

- **Short name:** Face the direction of travel
- **Description:** Students use the point in direction of speed block to automatically rotate a sprite to face its current movement direction. This is essential for arrows, rockets, birds, and other projectiles that should visually align with their trajectory.
- **Challenge format:** Coding, projectile orientation. Students create an arrow that always points forward as it follows a parabolic arc. Auto-grading checks the sprite rotation matches velocity direction.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G7.02 – Combine multiple forces simultaneously

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T17.G6.07: Debug unstable physics behavior
  * T17.G6.08: Compare simulations to real-world motion


- **Short name:** Mix gravity, thrust, and wind
- **Description:** Students apply two or more forces in the same update loop (gravity + constant wind, gravity + player
  thrust). They predict and observe the resulting curved motion.
- **Challenge format:** Coding, starter project. Prompt: “Add a wind force so the falling glider drifts 50 pixels to the
  right before landing.” Auto-grading checks final position.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G7.02.01 – Clear forces and torques from physics bodies

_Dependency:_
  * T17.G7.02: Combine multiple forces simultaneously

- **Short name:** Remove all applied forces
- **Description:** Students use the remove all forces and remove all torques blocks to stop continuous force application. This is essential for switching between different force modes, stopping thrust engines, or resetting physics states.
- **Challenge format:** Coding, force management. Students implement a jetpack that applies thrust while a key is held and clears forces when released. Auto-grading checks force clearing behavior.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G7.03 – Simulate drag or resistance

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T17.G6.07: Debug unstable physics behavior
  * T17.G6.08: Compare simulations to real-world motion


- **Short name:** Slow motion with drag
- **Description:** Students implement drag forces for different media (air, water, honey) by applying a force opposite to
  the sprite’s velocity. They compare how quickly each case comes to rest.
- **Challenge format:** Coding, comparative lab. Students log velocity over time for three drag coefficients.
  Auto-grading checks monotonic decreases and ordering.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T17.G7.03.01 – Use built-in damping for drag effects

_Dependency:_
  * T17.G7.03: Simulate drag or resistance

- **Short name:** Set movement and rotation damping
- **Description:** Students use the set damping factor block to apply automatic velocity reduction without manually calculating drag forces. They set separate damping values for linear and angular motion to simulate air resistance or underwater movement.
- **Challenge format:** Coding, damping comparison. Students compare custom drag code to built-in damping and achieve matching behavior with less code. Auto-grading checks damping parameter usage and equivalent motion.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G7.04 – Build chains or stacks of physics objects

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T17.G6.07: Debug unstable physics behavior
  * T17.G6.08: Compare simulations to real-world motion


- **Short name:** Create multi-object systems
- **Description:** Students create stacks of boxes, a rope of linked sprites, or domino lines and explore how forces
  propagate through the system when one element is pushed.
- **Challenge format:** Coding, creative challenge. Students follow constraints (at least five bodies) and record video
  evidence. Auto-grading inspects scripts for multiple bodies and interactions.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G7.04.01 – Use rotation speed and torque

_Dependency:_
  * T17.G7.04: Build chains or stacks of physics objects

- **Short name:** Control spinning physics objects
- **Description:** Students set rotation speed directly and apply torques to create spinning objects. They understand the relationship between torque (rotational force) and angular velocity, and use the angular speed reporter to monitor rotation.
- **Challenge format:** Coding, spinner mechanics. Students create a spinning wheel that maintains constant angular velocity or responds to torque inputs. Auto-grading checks rotation speed and torque usage.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G7.05 – Instrument and graph motion data

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T17.G6.07: Debug unstable physics behavior
  * T17.G6.08: Compare simulations to real-world motion


- **Short name:** Log position, velocity, and acceleration
- **Description:** Students record motion data from a selected sprite every few frames, store it in lists, and create a
  quick graph widget. They use the graph to confirm constant acceleration or to spot errors.
- **Challenge format:** Coding + data visualization. Auto-grading checks list contents and that graph trends match the
  scenario (e.g., parabolic position vs linear velocity).
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP/DI.

### T17.G7.05.01 – Read velocity and mass reporters

_Dependency:_
  * T17.G7.05: Instrument and graph motion data

- **Short name:** Get speed and mass values from physics
- **Description:** Students use the x speed, y speed, mass, and angular speed reporter blocks to read physics body properties at runtime. They display these values or use them in calculations for adaptive gameplay or data logging.
- **Challenge format:** Coding, physics dashboard. Students create a HUD that displays real-time velocity and mass of the player sprite. Auto-grading checks reporter block usage and displayed values.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G7.06 – Model a real-world physics scenario

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T17.G6.08: Compare simulations to real-world motion


- **Short name:** Simulate a pendulum, orbit, or rolling cart
- **Description:** Students choose a real phenomenon, and based on assumptions and plans from T05.G5.03 and T05.G5.04, build a CreatiCode simulation that approximates it. They explain which physics properties they tuned to mimic reality.
- **Challenge format:** Coding, design project. Students submit both the project link and a short rationale. Auto-grading
  checks for required documentation fields plus reasonable parameter choices.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T17.G7.07 – Evaluate whether a simulation meets requirements

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T17.G6.07: Debug unstable physics behavior
  * T17.G6.08: Compare simulations to real-world motion


- **Short name:** Check physics against constraints
- **Description:** Students are given target requirements (e.g., “ball must clear the second bumper but stop before the third”) and, drawing on test plans from T05.G5.05 and T05.G5.06, inspect a recorded run, examine logged data, and decide if the requirements were met, citing evidence.
- **Challenge format:** Concept + analysis. Students review playback and motion logs, then answer MCQ plus short
  justification prompts. Auto-grading looks for correct verdicts and referenced data points.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

---

## Grade 8

Grade 8 treats physics simulations as full systems to be balanced, optimized, and tested like professional games. These
skills close the loop with T14 capstones and prepare for the spatial thinking in T18 3D Worlds.

Strands: **G8‑A Design & balance**, **G8‑B Advanced systems**, **G8‑C Optimize & evaluate**

### T17.G8.01 – Design and balance a physics-based arcade game

_Dependency:_
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T17.G7.06: Model a real-world physics scenario


- **Short name:** Build a polished physics arcade level
- **Description:** Students design a launcher + target loop (Angry Birds–style) with multiple levels of difficulty. They
  test and adjust physics parameters to make each shot feel fair but challenging.
- **Challenge format:** Coding, project brief. Students submit a project and a balancing checklist (easy/medium/hard
  targets). Auto-grading runs scripted tests to confirm clear win conditions.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PD.

### T17.G8.02 – Implement fixed joints for connected objects

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T17.G7.06: Model a real-world physics scenario

- **Short name:** Weld sprites together as one body
- **Description:** Students use fixed joint blocks to lock the relative position between two physics bodies, creating compound objects that move as one unit. They can also remove constraints to break objects apart during gameplay.
- **Challenge format:** Coding, construction task. Students build a vehicle from multiple sprites connected with fixed joints. Auto-grading checks that connected parts move together.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G8.02.01 – Implement revolute joints for hinges

_Dependency:_
  * T17.G8.02: Implement fixed joints for connected objects

- **Short name:** Create rotating hinges between sprites
- **Description:** Students use revolute joint blocks to create hinge connections where one body rotates around another. They can add motors to control rotation speed and damping. Examples include doors, drawbridges, and swinging pendulums.
- **Challenge format:** Coding, hinge mechanics. Students create a swinging door that opens when the player approaches and closes automatically. Auto-grading checks revolute joint setup and motor behavior.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G8.02.02 – Implement prismatic joints for sliding

_Dependency:_
  * T17.G8.02: Implement fixed joints for connected objects

- **Short name:** Create sliding constraints between sprites
- **Description:** Students use prismatic joint blocks to constrain one body to slide along an axis relative to another body, with optional distance limits. Examples include pistons, sliding platforms, and elevator mechanics.
- **Challenge format:** Coding, slider mechanics. Students create an elevator platform that slides vertically within set limits. Auto-grading checks prismatic joint setup and distance constraints.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G8.03 – Build automated physics regression tests

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Auto-test physics behaviors
- **Description:** Students create scripts that spawn test objects, run the simulation for a set time, and assert that
  positions, velocities, or collision counts stay within tolerances. This guards against regressions when sharing code.
- **Challenge format:** Coding, testing challenge. Students write a loop that fires multiple projectiles and logs pass/
  fail counts. Auto-grading checks that diagnostics catch intentional bugs.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR, linkage to T13.

### T17.G8.04 – Optimize a physics scene for performance

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T17.G7.06: Model a real-world physics scenario
  * T17.G7.07: Evaluate whether a simulation meets requirements


- **Short name:** Improve simulation efficiency
- **Description:** Students profile a busy physics scene (many objects) and implement optimizations such as sleeping
  inactive bodies, lowering collision checks, culling off-screen objects, or reducing update frequency.
- **Challenge format:** Coding, optimization lab. Auto-grading measures frame rate before/after and checks for required
  optimization techniques.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T17.G8.04.01 – Enable CCD for fast-moving objects

_Dependency:_
  * T17.G8.04: Optimize a physics scene for performance

- **Short name:** Prevent bullets from tunneling through walls
- **Description:** Students enable continuous collision detection (CCD) for fast-moving physics bodies like bullets, small balls, or fast projectiles. They understand that without CCD, thin objects can pass through walls between physics steps.
- **Challenge format:** Coding, tunneling fix. Students fire a fast projectile that tunnels through a wall, then enable CCD to fix it. Auto-grading checks CCD is enabled and collision is detected.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G8.05 – Control gravity scale and time speed

_Dependency:_
  * T17.G7.06: Model a real-world physics scenario

- **Short name:** Adjust per-body gravity and simulation speed
- **Description:** Students use the gravity scale block to give individual sprites different gravity (floating balloons, heavy rocks, underwater objects) and the physics time speed block to create slow-motion or fast-forward effects for dramatic moments.
- **Challenge format:** Coding, physics variety. Students create a scene with objects of different gravity scales and a slow-motion trigger. Auto-grading checks gravity scale and time speed usage.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G8.05a – **[Engine Skill]** Implement multiple physics parameter sets

_Dependency:_
  * T17.G7.06: Model a real-world physics scenario
  * T17.G7.07: Evaluate whether a simulation meets requirements

- **Short name:** Build physics mode system (technical)
- **Description:** Students implement a system to toggle between different physics parameter sets (realistic vs arcade). They create data structures to store parameter configurations and switching mechanisms.
- **Challenge format:** Coding, systems implementation. Students build parameter management system with mode switching. Auto-grading verifies technical implementation of multiple physics modes.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G8.05b – **[Creative Skill]** Design physics modes for player experience

_Dependency:_
  * T17.G8.05a: Implement multiple physics parameter sets

- **Short name:** Choose physics for game feel (creative)
- **Description:** Students design realistic and stylized physics modes to create different player experiences. They document how each mode affects gameplay emotion, difficulty, and accessibility.
- **Challenge format:** Creative design + reflection. Students create modes with distinct feels and explain when each improves player experience. Auto-grading evaluates design rationale and player experience analysis.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T17.G8.06 – Use instrumentation data to tune difficulty

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.05: Fix a condition that uses the wrong operator
  * T09.G3.01: Create and use a numeric variable for score or count
  * T17.G7.06: Model a real-world physics scenario


- **Short name:** Adjust physics using playtest data
- **Description:** Students log player attempts (launch angle, power, success/fail) and analyze the dataset to retune
  gravity, impulse strength, or target size for a desired win rate. They connect physics tweaks to analytics.
- **Challenge format:** Coding + data analysis. Students export a CSV, run a quick summary (mean, min, max), and use the
  stats to justify parameter changes. Auto-grading checks calculations and updated physics values.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP/DI.
