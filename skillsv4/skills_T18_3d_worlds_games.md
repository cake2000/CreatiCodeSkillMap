# T18 – 3D Worlds & Games: K–8 Skill List (Draft v2)

Topic reference: `T18 3D Worlds` in `domains_topics_overview.md`
Domain: CreatiCode-specific, Coding-heavy · CSTA focus: PRO‑PF, DAA‑DF, SAS‑IM

T18 is the CreatiCode home for Babylon.js-based scenes, models, and gameplay. Conceptual spatial reasoning for K–2 occurs inside T01–T05 (sequencing, patterns, directions), so this topic **begins at Grade 3**. Grade 3 students first tackle short conceptual checks about axes and camera views before easing into CreatiCode’s 3D extension; Grades 4–8 then scale into full 3D games.

The topic strands cover all CreatiCode 3D block families:
- **3D scene:** initializing the world, camera placement, sky, and lighting.
- **3D objects:** primitives, imported models, and grouped assemblies.
- **3D tools:** color, texture, materials, and hierarchy for organization.
- **3D actions:** movement, animation loops, controls, and scripted cameras.
- **3D physics:** gravity, collisions, and behaviors that coordinate with T17 (2D Motion & Physics).
- **3D effects:** fog, glow, particles, and UI overlays that reinforce mood or feedback.

Grade 3 is the on-ramp to 3D blocks after students complete core programming topics (T01–T09); Grade 5+ assumes familiarity with T17 physics decision-making before enabling 3D rigid bodies.

---

## Grade 3

Grade 3 starts with lightweight conceptual checks (axes, camera views) and quickly transitions into initializing CreatiCode’s 3D stage, adding primitives, styling them, and building simple movement scripts. Strands: **G3-A Spatial concepts**, **G3-B Scene setup & objects**, **G3-C Movement & tracing**.

### T18.G3.01 – Interpret 3D axis directions

- **Short name:** Interpret x/y/z directions
- **Description:** Students read a labeled axis diagram or CreatiCode gizmo and identify which axis controls width, height, and depth, linking math vocabulary to the 3D stage.
- **Challenge format:** Concept, diagram interpretation. Auto-grading checks the selected axis labels.
- **CSTA:** E3‑DAA‑DF‑01.

### T18.G3.02 – Match camera views to 3D layouts

- **Short name:** Match camera views in 3D
- **Description:** Students compare front/top/side snapshots of the same object arrangement and match each snapshot to the correct camera icon, understanding how viewpoint affects what they see before coding cameras.
- **Challenge format:** Concept, drag-and-match. Auto-grading validates matches.
- **CSTA:** E3‑SAS‑IM‑01.

### T18.G3.03 – Initialize a 3D scene with default lighting

- **Short name:** Start a 3D scene
- **Description:** Students add a `when green flag clicked` script that calls the CreatiCode `initialize 3D world` block (choosing stage size, sky color, default light) so every run begins with a clean scene.
- **Challenge format:** Coding, guided setup. Auto-grading checks that the initialization block runs at start-up and that camera and lighting reset.
- **CSTA:** E3‑PRO‑PF‑01.

### T18.G3.04 – Add primitive shapes with 3D blocks

- **Short name:** Add 3D shapes with blocks
- **Description:** Students use the `add box/sphere/cylinder` blocks to place primitives in the scene and adjust their size parameters.
- **Challenge format:** Coding, starter project. Auto-grading verifies that the requested shapes exist with correct dimensions.
- **CSTA:** E3‑PRO‑PF‑01.

### T18.G3.05 – Position shapes using x/y/z coordinates

- **Short name:** Place shapes with coordinates
- **Description:** Students set `x`, `y`, and `z` values (or use `go to x:y:z`) to move an object to a target location, connecting coordinate plans from earlier math/diagram skills (T02/T25) to actual blocks.
- **Challenge format:** Coding, starter project with coordinate target markers. Auto-grading compares the final position to the expected coordinates.
- **CSTA:** E3‑DAA‑DF‑01.

### T18.G3.06 – Change shape colors or textures

- **Short name:** Color or texture shapes
- **Description:** Students use 3D styling blocks (set color, set texture, adjust opacity) to differentiate objects such as making the ground green and a sphere metallic.
- **Challenge format:** Coding, starter project. Auto-grading inspects the object properties or renders to confirm colors/textures were updated.
- **CSTA:** E3‑SAS‑IM‑01.

### T18.G3.07 – Move a 3D player with keyboard input

- **Short name:** Move a 3D player with keys
- **Description:** Students build a `forever` loop that checks arrow keys (or WASD) and `change x/z` so a player cube can walk around the scene.
- **Challenge format:** Coding, starter project. Auto-grading runs scripted key presses to confirm the cube moves correctly along both axes.
- **CSTA:** E3‑PRO‑PF‑01.

### T18.G3.08 – Trace a short 3D script to predict positions

- **Short name:** Trace simple 3D scripts
- **Description:** Students read a short 3D script that changes `x`, `y`, and rotation values and predict the final position/orientation without running it, reinforcing spatial reasoning.
- **Challenge format:** Concept/code-reading. Students type the final coordinates or pick from multiple choices; auto-grading compares to simulated output.
- **CSTA:** E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 scales up to full scenes with lighting, cameras, imported models, and ambient animation. Strands: **G4-A Scene & lighting**, **G4-B Objects & models**, **G4-C Interactivity**.

### T18.G4.01 – Compose a multi-part 3D scene with primitives

- **Short name:** Compose 3D set pieces
- **Description:** Students create a floor, obstacles, and backdrop objects using multiple primitives, aligning them precisely to build a room, park, or racetrack.
- **Challenge format:** Coding, creative build with auto-check. Auto-grading inspects that required objects exist with correct spacing and heights.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.02 – Configure ambient and directional lighting

- **Short name:** Set ambient and directional lights
- **Description:** Students place an ambient light plus at least one directional light (sunlight/spotlight) and tune color/intensity to achieve the requested mood.
- **Challenge format:** Coding, starter project. Auto-grading verifies the presence of both light types and checks color/intensity ranges.
- **CSTA:** E4‑SAS‑IM‑01.

### T18.G4.03 – Create a following or orbiting camera

- **Short name:** Add follow/orbit camera controls
- **Description:** Students use camera blocks to attach the camera to a player or orbit around a point, adjusting offsets for a smooth third-person or fly-around view.
- **Challenge format:** Coding, starter project with a moving target. Auto-grading simulates movement and checks that the camera follows/orbits as specified.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.04 – Place imported or premade 3D models

- **Short name:** Place 3D model assets
- **Description:** Students insert a prebuilt CreatiCode model (e.g., tree, car, character) and align it with primitives, learning how to mix asset types in one scene.
- **Challenge format:** Coding, starter project with asset selector. Auto-grading confirms the correct model is added and positioned accurately.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.05 – Animate scenery elements with loops

- **Short name:** Animate scenery loops
- **Description:** Students create looping animations for props (windmill spinning, lights pulsing, platforms bobbing) by combining `forever` loops with rotation/position changes.
- **Challenge format:** Coding, starter project. Auto-grading watches the animation for correct speed, axis, and repetition.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.06 – Trigger events when 3D objects touch

- **Short name:** Trigger events on 3D contact
- **Description:** Students detect when the player touches a token or when two objects get within a distance threshold and respond by playing a sound, updating score, or showing dialog.
- **Challenge format:** Coding, starter project. Auto-grading runs scripted movements to ensure the trigger fires exactly when contact occurs.
- **CSTA:** E4‑PRO‑PF‑01.

---

## Grade 5

Grade 5 brings in 3D physics, repeated level layout, and scene polish. These skills depend on T17 (2D Motion & Physics) decision making so students can compare manual vs engine-based motion. Strands: **G5-A Physics setup**, **G5-B Structured building**, **G5-C Materials & effects**.

### T18.G5.01 – Initialize a 3D physics world

- **Short name:** Start 3D physics
- **Description:** Students add the CreatiCode 3D physics initialization block, set gravity for X/Y/Z, and confirm the debug overlay shows the physics world running before gameplay starts.
- **Challenge format:** Coding, guided setup. Auto-grading checks that physics initializes exactly once with the specified gravity vector.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.02 – Attach static and dynamic physics bodies

- **Short name:** Give objects 3D physics bodies
- **Description:** Students configure which shapes are static (floors, walls) and which are dynamic (player, crates) by setting mass, restitution, and body type so objects react to gravity.
- **Challenge format:** Coding, starter project. Auto-grading tests collisions to confirm the correct body types and parameters were applied.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.03 – Detect physics collisions to collect items

- **Short name:** Collect items with physics collisions
- **Description:** Students use collision event blocks (e.g., `when body A hits body B`) to change score, remove coins, or play sounds when the player touches collectibles.
- **Challenge format:** Coding, starter project. Auto-grading simulates collisions and checks that the event fires once per contact and updates state correctly.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.04 – Use nested loops to arrange 3D objects in grids

- **Short name:** Arrange objects in 3D grids
- **Description:** Students apply nested loops to stamp or spawn platforms, trees, or tiles at evenly spaced coordinates, optionally varying height for stepped terrain.
- **Challenge format:** Coding, starter project. Auto-grading inspects code for nested loops and counts the placed objects to ensure the grid dimensions match the prompt.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.05 – Apply detailed textures or materials to surfaces

- **Short name:** Texture large surfaces
- **Description:** Students use material blocks to apply tileable textures, adjust UV scaling, or mix colors and normal maps so surfaces like walls or roads look realistic.
- **Challenge format:** Coding, starter project. Auto-grading checks that specified objects have the requested texture/material settings.
- **CSTA:** E5‑SAS‑IM‑01.

### T18.G5.06 – Add global fog or particle effects for atmosphere

- **Short name:** Add simple 3D effects
- **Description:** Students enable fog, glow, or particle emitters (e.g., falling snow, magical sparks) and tune their color, density, and bounds so the effect supports gameplay feedback.
- **Challenge format:** Coding, starter project. Auto-grading inspects the scene for the selected effect and validates parameter ranges.
- **CSTA:** E5‑PRO‑PF‑01, SAS‑IM.

---

## Grade 6

Grade 6 focuses on systems thinking: selective collisions, code quality, advanced controls, and triggered effects. Strands: **G6-A Physics systems**, **G6-B Code quality & controls**, **G6-C Effects & analytics**.

### T18.G6.01 – Set up collision groups for selective interaction

- **Short name:** Collision groups for game logic
- **Description:** Students assign 3D physics bodies to collision groups or masks so only certain pairs collide (player with platforms/coins, enemies avoiding one another, projectiles passing through decorations) to fine-tune game logic.
- **Challenge format:** Coding, starter project with multiple body types. Auto-grading spawns test objects to confirm only the requested collisions occur.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G6.02 – Trace a multi-step 3D script to predict positions

- **Short name:** Trace complex 3D scripts
- **Description:** Students read a longer script that mixes coordinate changes, rotations, and camera commands (e.g., orbit, zoom) and predict final object positions or camera headings without running it.
- **Challenge format:** Concept/code-reading. Auto-grading compares the student’s prediction to simulated output.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G6.03 – Refactor repeated 3D object creation into a loop or function

- **Short name:** Refactor 3D object creation
- **Description:** Students rewrite scripts that manually duplicate “add object / set transform” blocks into loops or custom functions, reducing duplication when spawning many props.
- **Challenge format:** Coding, refactor challenge. Auto-grading checks that a loop/function is used and scene output matches the original.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T18.G6.04 – Implement a camera with mouse look

- **Short name:** Mouse-look camera control
- **Description:** Students map mouse movement to camera yaw/pitch to build a smooth first-person or free-look camera, including clamping pitch to avoid flipping.
- **Challenge format:** Coding, starter project. Auto-grading simulates mouse motion and verifies the camera rotates correctly.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G6.05 – Trigger advanced visual effects on events

- **Short name:** Trigger advanced 3D effects
- **Description:** Students enable or disable advanced effects (bloom, spotlight cones, burst particles) in response to events such as power-ups or low health, coordinating visuals with game state.
- **Challenge format:** Coding, starter project. Auto-grading triggers events to ensure the effect toggles correctly and uses the requested parameters.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

---

## Grade 7

Grade 7 builds sophisticated mechanics: AI navigation, tuned physics responses, puzzles, and cinematic storytelling. Strands: **G7-A Game AI**, **G7-B Physics puzzles**, **G7-C Cinematics & UX**.

### T18.G7.01 – Implement pathfinding or waypoint-based NPC movement

- **Short name:** NPC navigation in 3D
- **Description:** Students code an NPC that follows waypoints, patrols, or chases the player by computing direction vectors and adjusting movement speed smoothly.
- **Challenge format:** Coding, starter project. Auto-grading measures NPC paths against expected routes or ensures it catches up to the player.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.02 – Design collision response for bouncing or sliding

- **Short name:** Custom collision response
- **Description:** Students tweak restitution, friction, or apply impulses on collision to achieve different results (bouncy projectiles, sliding ice blocks, sticky platforms).
- **Challenge format:** Coding, starter project. Auto-grading simulates collisions to check for correct responses.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.03 – Use 3D coordinates and distance calculations for game mechanics

- **Short name:** Distance and coordinate calculations in 3D
- **Description:** Students compute 3D distances (using built-in `distance to` or math) to trigger events such as proximity mines, safe zones, or camera shakes.
- **Challenge format:** Coding, starter project. Auto-grading positions the player at various distances and checks whether events fire correctly.
- **CSTA:** MS‑DAA‑DF‑01.

### T18.G7.04 – Implement a physics-based puzzle mechanic

- **Short name:** Physics-based puzzle
- **Description:** Students combine physics bodies, triggers, and environmental interactions to design a solvable puzzle (e.g., push blocks onto switches, roll a ball through ramps).
- **Challenge format:** Coding, creative challenge with rubric + auto-check. Auto-grading confirms required mechanics (physics enabled, win condition detected) exist.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.05 – Script camera transitions for cutscenes

- **Short name:** Scripted 3D camera moments
- **Description:** Students choreograph mini-cutscenes by moving the camera through a list of positions/targets, blending easing functions to introduce or conclude levels.
- **Challenge format:** Coding, starter project. Auto-grading watches the camera timeline to ensure it hits all required points in order and timing.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

---

## Grade 8

Grade 8 focuses on systems integration, scalability, and reflective design choices that mirror professional workflows. Strands: **G8-A Systems & tooling**, **G8-B Performance & critique**.

### T18.G8.01 – Implement a level editor or dynamic level loading

- **Short name:** Load and switch between 3D levels
- **Description:** Students store level data in lists or records and write code to spawn objects per level, supporting editing, replay, and difficulty scaling.
- **Challenge format:** Coding, starter project. Auto-grading ensures at least two levels load correctly and data structures contain requested entries.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DF.

### T18.G8.02 – Use multiple cameras to implement split-screen or UI view

- **Short name:** Multiple camera systems
- **Description:** Students create two camera feeds (main gameplay plus minimap/UI or split-screen for multiplayer) and manage when each renders.
- **Challenge format:** Coding, guided construction. Auto-grading confirms two distinct camera views refresh as specified.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G8.03 – Analyze and optimize a 3D game for performance

- **Short name:** Optimize 3D performance
- **Description:** Students profile a sluggish 3D project, identify bottlenecks (too many clones, physics bodies, or draw calls), and refactor using pooling, culling, or simplified meshes to improve frame rate.
- **Challenge format:** Coding/debugging. Auto-grading measures frame time before/after and checks for required optimizations.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T18.G8.04 – Analyze trade-offs in 3D game design decisions

- **Short name:** Justify 3D design choices
- **Description:** Students review a completed 3D project and explain design choices (physics vs manual motion, camera placement, effect usage), citing pros and cons relative to requirements.
- **Challenge format:** Concept, explanation + selection. Auto-grading scores selected answers and rubric-tagged justification.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

---

## Notes on Progression

- **Grade 3:** Blend conceptual microsteps (axes, camera views) with first CreatiCode scene setup, primitives, styling, and simple player controls.
- **Grade 4:** Expand to full scenes with lighting, multi-camera setups, imported models, ambient animation, and basic event handling.
- **Grade 5:** Layer in 3D physics, structured scene generation, and atmospheric effects, building on T17’s decision rules.
- **Grades 6–7:** Emphasize systems thinking—collision groups, refactoring, mouse-look controls, AI navigation, physics puzzles, and cinematics.
- **Grade 8:** Focus on production concerns such as level loading, split views, performance optimization, and reflective design choices.
- **All grades:** Every strand intentionally maps to CreatiCode’s 3D scene/object/tool/action/physics/effect blocks so dependencies into T14 (Games) and T17 (Physics) remain explicit and scaffolded.
