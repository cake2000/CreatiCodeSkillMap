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

- **Short name:** Pick the right physics method
- **Description:** Students compare CreatiCode project briefs (platformer, UI animation, top-down maze, pinball machine) and, drawing on prior simulation planning (T05.G2.03, T05.G4.05), choose whether to stick with manual velocity variables or enable the physics extension. They explain the decision for each brief so later T14 skills inherit the correct dependency.
- **Challenge format:** Concept, drag-and-sort. Students drag each brief into “Manual physics” or “2D physics engine”
  bins and type a short justification. Auto-grading checks placement and keywords.
- **CSTA:** E5‑PRO‑PF‑01, SAS‑IM.

### T17.G5.02 – Track gravity with velocity variables

- **Short name:** Update y-velocity each frame
- **Description:** Students build a loop that stores a sprite’s y-velocity in a variable, subtracts gravity, then adds it
  to the sprite’s position. This manual approach mirrors classic Scratch tutorials and prepares students for physics
  debugging even without the extension.
- **Challenge format:** Coding, starter project. Prompt: “Make the hero fall by updating a `y velocity` variable every
  frame.” Auto-grading checks the variable math and resulting motion.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.03 – Use horizontal speed and friction variables

- **Short name:** Slide with vx and friction
- **Description:** Students add an `x velocity` variable, respond to arrow keys to change it, and multiply by a friction
  factor each tick so motion glides to a stop. This mirrors T14 platformer expectations before physics bodies are added.
- **Challenge format:** Coding, starter project. Students implement horizontal movement with adjustable friction slider.
  Auto-grading inspects code and checks that motion slows when the slider is increased.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.04 – Code a manual bounce with energy loss

- **Short name:** Bounce by flipping velocity
- **Description:** Students write a conditional that checks for ground contact, multiplies the y-velocity by a negative
  damping factor (e.g., ‑0.6), and sends the sprite back up with reduced height. This cements the physics vocabulary in
  block form before using the engine’s restitution settings.
- **Challenge format:** Coding, debugging prompt. Students receive a partially working script and complete the bounce
  logic. Auto-grading runs three drops to verify decreasing bounce heights.
- **CSTA:** E5‑PRO‑PF‑01, PRO‑TR.

### T17.G5.05 – Initialize a 2D physics world

- **Short name:** Start gravity for the scene
- **Description:** Students add the Initialize 2D Physics block, set gravity (e.g., X: 0, Y: -100), and confirm the debug
  overlay shows the world running. They understand that no physics behavior occurs until this block executes.
- **Challenge format:** Coding, guided setup. Starter project has sprites but no physics. Students add the init block,
  choose gravity, and run a provided test button. Auto-grading inspects the script.
- **CSTA:** E5‑PRO‑PF‑01, SAS‑IM.

### T17.G5.06 – Attach a dynamic body to a sprite

- **Short name:** Give a sprite a physics body
- **Description:** Students convert a sprite to a dynamic physics body (selecting density/mass options) so the sprite
  responds to gravity without manual loops. They observe the sprite fall and stop when it hits the stage floor.
- **Challenge format:** Coding, starter project. Prompt: “Add a dynamic body to the hero sprite and press the gravity test
  button.” Auto-grading checks that the sprite’s body type and parameters are correct.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.07 – Build static boundaries for floors and walls

- **Short name:** Create static walls to stop sprites
- **Description:** Students add static physics bodies to floor or wall sprites so falling or sliding objects stop on
  contact. They learn to use static bodies for geometry that should not move.
- **Challenge format:** Coding, starter project. Students configure boundary sprites as static bodies and rerun the gravity
  test to ensure the player lands and cannot exit the screen. Auto-grading checks collision behavior.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.08 – Apply an impulse to jump or push

- **Short name:** Tap to jump with impulse
- **Description:** Students apply an upward impulse or horizontal shove to a dynamic sprite in response to input (e.g.,
  space key or on-screen button). They control how strong the impulse is so the sprite clears a target platform.
- **Challenge format:** Coding, starter project. Prompt: “When SPACE is pressed, apply an impulse that lets the hero clear
  the first platform.” Auto-grading checks for the impulse block and resulting jump height.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.09 – **[Engine Skill]** Configure gravity and mass parameters

- **Short name:** Set precise physics values (technical)
- **Description:** Students adjust gravity strength and sprite mass using numeric inputs to achieve specific physics behaviors (exact fall time, bounce height). They learn to read physics specifications and translate them into parameter values.
- **Challenge format:** Coding, parameter lab. Students use sliders and numeric inputs to achieve target measurements. Auto-grading checks parameter values and physics measurements.
- **CSTA:** E5‑PRO‑PF‑01.

### T17.G5.09b – **[Creative Skill]** Tune physics feel for player experience

- **Short name:** Adjust physics for game feel (creative)
- **Description:** Students, informed by simulation planning (T05.G5.06, T05.G6.06), adjust gravity and mass to create desired player emotions (heavy/floaty, challenging/forgiving). They explain how physics parameters support gameplay goals.
- **Challenge format:** Creative iteration challenge. Students adjust parameters to match creative briefs ("make jumping feel heroic" vs "create realistic falling"). Auto-grading evaluates alignment between settings and creative goals.
- **CSTA:** E5‑PRO‑PF‑01.
- **Dependencies:** T05.G5.06, T05.G6.06 (simulation planning).

### T17.G5.10 – Trace simple 2D physics motion

- **Short name:** Predict landing spot from settings
- **Description:** Students read a small table showing gravity, mass, starting height, and time elapsed, then choose the
  correct statement about where the sprite will be (e.g., “lands on the platform,” “still in the air,” “passed through
  the floor”).
- **Challenge format:** Concept, interactive trace. A visualization panel shows the parameters; students select from
  multiple conclusions. Auto-grading compares answers to a hidden simulation.
- **CSTA:** E5‑PRO‑PF‑01, PRO‑TR.

### T17.G5.11 – Debug missing physics setup

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

- **Short name:** Set friction values (technical)
- **Description:** Students adjust the friction property numerically and measure how far objects travel on different surfaces. They learn to map friction coefficients to sliding distances through systematic testing.
- **Challenge format:** Coding, measurement lab. Students set specific friction values, measure results, and record the relationship between parameters and physics outcomes. Auto-grading checks numerical accuracy.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.01b – **[Creative Skill]** Design surface feel for game environments

- **Short name:** Choose friction for story/gameplay (creative)
- **Description:** Students select friction values to create desired environmental storytelling (ice, wood, carpet) and gameplay experiences. They explain how surface properties enhance narrative and player challenge.
- **Challenge format:** Creative implementation. Students choose friction settings to support environmental themes and explain the connection between physics properties and story/gameplay goals.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.02 – **[Engine Skill]** Control restitution parameters

- **Short name:** Set bounce coefficients (technical)
- **Description:** Students modify the restitution property numerically and measure bounce heights. They learn the relationship between restitution values (0.0-1.0) and energy conservation in collisions.
- **Challenge format:** Coding, measurement lab. Students use sliders to test restitution values and record bounce height data. Auto-grading checks correlation between restitution and measured bounce.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.02b – **[Creative Skill]** Design bounce feel for game mechanics

- **Short name:** Choose bounce for gameplay (creative)
- **Description:** Students select restitution values to create specific gameplay experiences (lively pinball bumpers, soft landing zones). They explain how bounce properties enhance game mechanics and player feel.
- **Challenge format:** Creative implementation. Students design bounce behaviors to support game mechanics and justify choices based on player experience goals.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.03 – Build a kinematic moving platform

- **Short name:** Move platforms without gravity
- **Description:** Students convert a sprite to a kinematic body so it ignores gravity but still collides with the player.
  They script its left-right motion and ensure the player rides it safely.
- **Challenge format:** Coding, starter project. Prompt: “Create a kinematic moving platform that carries the player
  across a gap.” Auto-grading checks for kinematic status and reliable transport.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.04 – Detect collisions for scoring or triggers

- **Short name:** Score points when physics sprites meet
- **Description:** Students listen for collision events between named sprites (player hits coin, ball hits bumper) and run
  scoring or state-change scripts in response.
- **Challenge format:** Coding, starter project. Provided sensors emit messages on collision; students hook them to a
  scoreboard. Auto-grading checks scoring accuracy and reset conditions.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑DH.

### T17.G6.05 – Use collision groups to filter interactions

- **Short name:** Choose who collides
- **Description:** Students assign collision groups or masks so the player can pass through collectibles but still hit
  hazards. They reason about selective interactions in crowded levels.
- **Challenge format:** Coding, puzzle scene. Students set group numbers according to a table. Auto-grading simulates
  collisions and confirms only allowed pairs interact.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G6.06 – Blend manual and engine sprites in a level

- **Short name:** Mix manual movers with physics bodies
- **Description:** Students keep manual scripts (e.g., scrolling backgrounds, UI-driven particles) running alongside
  physics bodies in the same T14 level without conflicts. They ensure manual sprites do not accidentally inherit physics
  forces and vice versa.
- **Challenge format:** Coding, integration task. Students toggle physics on/off for selected sprites and write comments
  documenting why. Auto-grading checks sprite settings and script separation.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PM.

### T17.G6.07 – Debug unstable physics behavior

- **Short name:** Fix jittery or sinking sprites
- **Description:** Students diagnose why a sprite jitters, sinks through a platform, or flies off-screen (e.g., mass too
  low, time step too large, conflicting impulses) and adjust parameters to stabilize the scene.
- **Challenge format:** Coding, debugging lab. Students tweak gravity, density, or damping based on clues. Auto-grading
  checks that the sprite stays within tolerances after the fix.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T17.G6.08 – Compare simulations to real-world motion

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

- **Short name:** Set angle and speed for projectiles
- **Description:** Students create a launcher where users set angle/speed sliders. The projectile receives an initial
  impulse that produces a parabolic arc, and targets are placed at measurable distances.
- **Challenge format:** Coding, design challenge. Students wire sliders to the impulse block and verify hits on given
  targets. Auto-grading checks for correct parameter math and hit detection.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T17.G7.02 – Combine multiple forces simultaneously

- **Short name:** Mix gravity, thrust, and wind
- **Description:** Students apply two or more forces in the same update loop (gravity + constant wind, gravity + player
  thrust). They predict and observe the resulting curved motion.
- **Challenge format:** Coding, starter project. Prompt: “Add a wind force so the falling glider drifts 50 pixels to the
  right before landing.” Auto-grading checks final position.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G7.03 – Simulate drag or resistance

- **Short name:** Slow motion with drag
- **Description:** Students implement drag forces for different media (air, water, honey) by applying a force opposite to
  the sprite’s velocity. They compare how quickly each case comes to rest.
- **Challenge format:** Coding, comparative lab. Students log velocity over time for three drag coefficients.
  Auto-grading checks monotonic decreases and ordering.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DI.

### T17.G7.04 – Build chains or stacks of physics objects

- **Short name:** Create multi-object systems
- **Description:** Students create stacks of boxes, a rope of linked sprites, or domino lines and explore how forces
  propagate through the system when one element is pushed.
- **Challenge format:** Coding, creative challenge. Students follow constraints (at least five bodies) and record video
  evidence. Auto-grading inspects scripts for multiple bodies and interactions.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G7.05 – Instrument and graph motion data

- **Short name:** Log position, velocity, and acceleration
- **Description:** Students record motion data from a selected sprite every few frames, store it in lists, and create a
  quick graph widget. They use the graph to confirm constant acceleration or to spot errors.
- **Challenge format:** Coding + data visualization. Auto-grading checks list contents and that graph trends match the
  scenario (e.g., parabolic position vs linear velocity).
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP/DI.

### T17.G7.06 – Model a real-world physics scenario

- **Short name:** Simulate a pendulum, orbit, or rolling cart
- **Description:** Students choose a real phenomenon, and based on assumptions and plans from T05.G5.03 and T05.G5.04, build a CreatiCode simulation that approximates it. They explain which physics properties they tuned to mimic reality.
- **Challenge format:** Coding, design project. Students submit both the project link and a short rationale. Auto-grading
  checks for required documentation fields plus reasonable parameter choices.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T17.G7.07 – Evaluate whether a simulation meets requirements

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

- **Short name:** Build a polished physics arcade level
- **Description:** Students design a launcher + target loop (Angry Birds–style) with multiple levels of difficulty. They
  test and adjust physics parameters to make each shot feel fair but challenging.
- **Challenge format:** Coding, project brief. Students submit a project and a balancing checklist (easy/medium/hard
  targets). Auto-grading runs scripted tests to confirm clear win conditions.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PD.

### T17.G8.02 – Implement advanced joints or constraints

- **Short name:** Connect sprites with hinges or ropes
- **Description:** Students use physics constraint blocks (hinge, distance, weld) to link sprites so they rotate or move
  together. Example: building a drawbridge or swinging wrecking ball.
- **Challenge format:** Coding, starter project. Prompt: “Attach the bridge plank to the tower with a hinge so it lowers
  smoothly when tapped.” Auto-grading checks that the joint behaves as expected.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G8.03 – Build automated physics regression tests

- **Short name:** Auto-test physics behaviors
- **Description:** Students create scripts that spawn test objects, run the simulation for a set time, and assert that
  positions, velocities, or collision counts stay within tolerances. This guards against regressions when sharing code.
- **Challenge format:** Coding, testing challenge. Students write a loop that fires multiple projectiles and logs pass/
  fail counts. Auto-grading checks that diagnostics catch intentional bugs.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR, linkage to T13.

### T17.G8.04 – Optimize a physics scene for performance

- **Short name:** Improve simulation efficiency
- **Description:** Students profile a busy physics scene (many objects) and implement optimizations such as sleeping
  inactive bodies, lowering collision checks, culling off-screen objects, or reducing update frequency.
- **Challenge format:** Coding, optimization lab. Auto-grading measures frame rate before/after and checks for required
  optimization techniques.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T17.G8.05a – **[Engine Skill]** Implement multiple physics parameter sets

- **Short name:** Build physics mode system (technical)
- **Description:** Students implement a system to toggle between different physics parameter sets (realistic vs arcade). They create data structures to store parameter configurations and switching mechanisms.
- **Challenge format:** Coding, systems implementation. Students build parameter management system with mode switching. Auto-grading verifies technical implementation of multiple physics modes.
- **CSTA:** MS‑PRO‑PF‑01.

### T17.G8.05b – **[Creative Skill]** Design physics modes for player experience

- **Short name:** Choose physics for game feel (creative)
- **Description:** Students design realistic and stylized physics modes to create different player experiences. They document how each mode affects gameplay emotion, difficulty, and accessibility.
- **Challenge format:** Creative design + reflection. Students create modes with distinct feels and explain when each improves player experience. Auto-grading evaluates design rationale and player experience analysis.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T17.G8.06 – Use instrumentation data to tune difficulty

- **Short name:** Adjust physics using playtest data
- **Description:** Students log player attempts (launch angle, power, success/fail) and analyze the dataset to retune
  gravity, impulse strength, or target size for a desired win rate. They connect physics tweaks to analytics.
- **Challenge format:** Coding + data analysis. Students export a CSV, run a quick summary (mean, min, max), and use the
  stats to justify parameter changes. Auto-grading checks calculations and updated physics values.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DP/DI.
