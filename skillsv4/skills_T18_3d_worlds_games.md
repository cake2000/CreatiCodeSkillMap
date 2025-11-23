# T18 – 3D Worlds & Games: K–8 Skill List (Draft v2)

Topic reference: `T18 3D Worlds` in `domains_topics_overview.md`
Domain: CreatiCode-specific, Coding-heavy · CSTA focus: PRO‑PF, DAA‑DF, SAS‑IM

T18 is the CreatiCode home for Babylon.js-based scenes, models, and gameplay. Conceptual spatial reasoning for K–2 occurs inside T01–T05 (sequencing, patterns, directions), so this topic **begins at Grade 3**. Grade 3 students first tackle short conceptual checks about axes and camera views before easing into CreatiCode's 3D extension; Grades 4–8 then scale into full 3D games.

The topic strands cover all CreatiCode 3D block families:
- **3D scene:** initializing the world, camera placement, sky, and lighting.
- **3D objects:** primitives, imported models, and grouped assemblies.
- **3D tools:** color, texture, materials, and hierarchy for organization.
- **3D actions:** movement, animation loops, controls, and scripted cameras.
- **3D physics:** gravity, collisions, and behaviors that coordinate with T17 (2D Motion & Physics).
- **3D effects:** fog, glow, particles, and UI overlays that reinforce mood or feedback.

Grade 3 is the on-ramp to 3D blocks after students complete core programming topics (T01–T09); Grade 5+ assumes familiarity with T17 physics decision-making before enabling 3D rigid bodies.
- **Planning bridge:** User needs, accessibility, and simulation goals are planned in **T05 Human‑Centered Design**; T18 focuses on implementing and debugging 3D behaviors from those plans.

---

## Grade 3

Grade 3 starts with lightweight conceptual checks (axes, camera views) and quickly transitions into initializing CreatiCode's 3D stage, adding primitives, styling them, and building simple movement scripts. Strands: **G3-A Spatial concepts**, **G3-B Scene setup & objects**, **G3-C Movement & tracing**.

### T18.G3.01 – Interpret 3D axis directions

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T03.G2.01: Choose subtasks for a simple project idea


- **Short name:** Interpret x/y/z directions
- **Description:** Students read a labeled axis diagram or CreatiCode gizmo and identify which axis controls width, height, and depth, linking math vocabulary to the 3D stage.
- **Challenge format:** Concept, diagram interpretation. Auto-grading checks the selected axis labels.
- **CSTA:** E3‑DAA‑DF‑01.

### T18.G3.02 – Match camera views to 3D layouts

_Dependency:_
  * T18.G3.01: Interpret 3D axis directions
  * T07.G3.01: Use a counted repeat loop


- **Short name:** Match camera views in 3D
- **Description:** Students compare front/top/side snapshots of the same object arrangement and match each snapshot to the correct camera icon, understanding how viewpoint affects what they see before coding cameras.
- **Challenge format:** Concept, drag-and-match. Auto-grading validates matches.
- **CSTA:** E3‑SAS‑IM‑01.

### T18.G3.03 – Initialize a 3D scene with a specific environment

_Dependency:_
  * T18.G3.02: Match camera views to 3D layouts
  * T09.G3.01: Create and use a numeric variable for score or count
  * T07.G3.02: Trace a script with a simple loop
  * T03.G3.03: Create a 3‑panel storyboard for a project


- **Short name:** Start a 3D scene with environment
- **Description:** Students add a `when green flag clicked` script that calls the CreatiCode `initialize 3D world` block, selecting from environment options (Empty, Blue Sky, Castle, City, etc.) to set the stage for their project.
- **Challenge format:** Coding, guided setup. Auto-grading checks that the initialization block runs at start-up with the specified environment.
- **CSTA:** E3‑PRO‑PF‑01.

### T18.G3.04.01 – Add a box shape to the 3D scene

_Dependency:_
  * T18.G3.03: Initialize a 3D scene with a specific environment
  * T08.G3.01: Use a simple if in a script


- **Short name:** Add box with dimensions
- **Description:** Students use the `add box` block to place a box in the scene, adjusting width, height, and depth parameters to create objects like platforms, walls, or buildings.
- **Challenge format:** Coding, starter project. Auto-grading verifies that a box exists with correct dimensions.
- **CSTA:** E3‑PRO‑PF‑01.

### T18.G3.04.02 – Add a sphere shape to the 3D scene

_Dependency:_
  * T18.G3.04.01: Add a box shape to the 3D scene


- **Short name:** Add sphere with diameter
- **Description:** Students use the `add sphere` block to create round objects like balls, planets, or collectibles, setting diameter and segments for smoothness.
- **Challenge format:** Coding, starter project. Auto-grading verifies that a sphere exists with correct dimensions.
- **CSTA:** E3‑PRO‑PF‑01.

### T18.G3.04.03 – Add a cylinder shape to the 3D scene

_Dependency:_
  * T18.G3.04.02: Add a sphere shape to the 3D scene


- **Short name:** Add cylinder shape
- **Description:** Students use the `add cylinder` block to create columnar objects like posts, trees, or poles, adjusting height and diameter parameters.
- **Challenge format:** Coding, starter project. Auto-grading verifies that a cylinder exists with correct dimensions.
- **CSTA:** E3‑PRO‑PF‑01.

### T18.G3.05 – Position shapes using x/y/z coordinates

_Dependency:_
  * T18.G3.04.03: Add a cylinder shape to the 3D scene
  * T09.G3.02: Use a variable in a conditional (if block)
  * T08.G3.02: Decide when a single if is enough


- **Short name:** Place shapes with coordinates
- **Description:** Students set `x`, `y`, and `z` values (or use `go to x:y:z`) to move an object to a target location, connecting coordinate plans from earlier math/diagram skills (T02/T25) to actual blocks.
- **Challenge format:** Coding, starter project with coordinate target markers. Auto-grading compares the final position to the expected coordinates.
- **CSTA:** E3‑DAA‑DF‑01.

### T18.G3.06.01 – Change shape color using basic color picker

_Dependency:_
  * T18.G3.05: Position shapes using x/y/z coordinates
  * T07.G3.03: Build a forever loop for simple animation
  * T03.G3.04: Match storyboard panels to project scenes


- **Short name:** Set basic shape color
- **Description:** Students use the `set color` block to apply a solid color to 3D objects, learning how to differentiate objects visually (e.g., making the ground green, a player red).
- **Challenge format:** Coding, starter project. Auto-grading inspects the object color property to confirm color was set correctly.
- **CSTA:** E3‑SAS‑IM‑01.

### T18.G3.06.02 – Adjust shape transparency

_Dependency:_
  * T18.G3.06.01: Change shape color using basic color picker


- **Short name:** Set transparency
- **Description:** Students use opacity or alpha blocks to make objects partially or fully transparent, useful for windows, water, or ghost effects.
- **Challenge format:** Coding, starter project. Auto-grading checks the opacity value of specified objects.
- **CSTA:** E3‑SAS‑IM‑01.

### T18.G3.07 – Move a 3D player with keyboard input

_Dependency:_
  * T18.G3.06.02: Adjust shape transparency
  * T08.G3.03: Pick the right conditional block for a scenario
  * T09.G3.03: Debug missing or wrong variable updates


- **Short name:** Move a 3D player with keys
- **Description:** Students build a `forever` loop that checks arrow keys (or WASD) and `change x/z` so a player cube can walk around the scene.
- **Challenge format:** Coding, starter project. Auto-grading runs scripted key presses to confirm the cube moves correctly along both axes.
- **CSTA:** E3‑PRO‑PF‑01.

### T18.G3.08 – Trace a short 3D script to predict positions

_Dependency:_
  * T18.G3.07: Move a 3D player with keyboard input
  * T11.G3.01: Understand when to use custom blocks vs loops
  * T07.G3.04: Use repeat‑until to reach a simple goal


- **Short name:** Trace simple 3D scripts
- **Description:** Students read a short 3D script that changes `x`, `y`, and rotation values and predict the final position/orientation without running it, reinforcing spatial reasoning.
- **Challenge format:** Concept/code-reading. Students type the final coordinates or pick from multiple choices; auto-grading compares to simulated output.
- **CSTA:** E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 scales up to full scenes with lighting, cameras, imported models, and ambient animation. Strands: **G4-A Scene & lighting**, **G4-B Objects & models**, **G4-C Interactivity**.

### T18.G4.01.01 – Add plane shapes for floors and walls

_Dependency:_
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.G3.01: Move a sprite with arrow keys (4 directions)
  * T18.G3.08: Trace a short 3D script to predict positions


- **Short name:** Create floors with plane shapes
- **Description:** Students use the `add plane` block to create flat surfaces for floors, walls, or backdrops, adjusting width and height to build environments.
- **Challenge format:** Coding, starter project. Auto-grading verifies that plane objects exist with correct dimensions.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.01.02 – Add capsule and torus shapes

_Dependency:_
  * T18.G4.01.01: Add plane shapes for floors and walls


- **Short name:** Use capsule and torus shapes
- **Description:** Students add capsule shapes (for character bodies, pillars) and torus shapes (for rings, wheels) to expand their shape vocabulary beyond basic primitives.
- **Challenge format:** Coding, starter project. Auto-grading checks for the presence of capsule and torus shapes.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.01.03 – Compose a multi-part 3D scene with multiple primitives

_Dependency:_
  * T18.G4.01.02: Add capsule and torus shapes


- **Short name:** Compose 3D set pieces
- **Description:** Students create a complex environment using multiple primitive types (boxes, spheres, cylinders, planes, etc.), aligning them precisely to build a room, park, or racetrack.
- **Challenge format:** Coding, creative build with auto-check. Auto-grading inspects that required objects exist with correct spacing and heights.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.02.01 – Add ambient lighting to set base brightness

_Dependency:_
  * T18.G4.01.03: Compose a multi-part 3D scene with multiple primitives


- **Short name:** Set ambient light
- **Description:** Students add an ambient light to provide overall base illumination to the scene, adjusting color and intensity for the desired mood.
- **Challenge format:** Coding, starter project. Auto-grading verifies the presence of ambient light with correct parameters.
- **CSTA:** E4‑SAS‑IM‑01.

### T18.G4.02.02 – Add directional lighting for sunlight effect

_Dependency:_
  * T18.G4.02.01: Add ambient lighting to set base brightness


- **Short name:** Add directional sunlight
- **Description:** Students place a directional light to simulate sunlight, adjusting direction, color, and intensity to create shadows and depth.
- **Challenge format:** Coding, starter project. Auto-grading verifies the presence of directional light with correct direction and intensity.
- **CSTA:** E4‑SAS‑IM‑01.

### T18.G4.02.03 – Add point lights for localized illumination

_Dependency:_
  * T18.G4.02.02: Add directional lighting for sunlight effect


- **Short name:** Use point lights
- **Description:** Students add point lights (like light bulbs or torches) that radiate in all directions, setting position, range, and intensity for localized lighting effects.
- **Challenge format:** Coding, starter project. Auto-grading verifies point light placement and properties.
- **CSTA:** E4‑SAS‑IM‑01.

### T18.G4.03.01 – Set up an orbit camera to view a target

_Dependency:_
  * T18.G4.02.03: Add point lights for localized illumination


- **Short name:** Create orbit camera
- **Description:** Students use orbit camera blocks to circle around a target object or point, adjusting radius, height, and rotation speed for a strategic or cinematic view.
- **Challenge format:** Coding, starter project with a central target. Auto-grading verifies camera orbits correctly around the target.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.03.02 – Set up a follow camera to track a moving object

_Dependency:_
  * T18.G4.03.01: Set up an orbit camera to view a target


- **Short name:** Create follow camera
- **Description:** Students attach the camera to follow a player or vehicle, adjusting offset and height for a smooth third-person view that moves with the target.
- **Challenge format:** Coding, starter project with a moving player. Auto-grading simulates movement and checks that the camera follows smoothly.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.04.01 – Place 3D models from the CreatiCode library

_Dependency:_
  * T18.G4.03.02: Set up a follow camera to track a moving object


- **Short name:** Add library 3D models
- **Description:** Students select and place 3D models from CreatiCode's 1000+ model library (trees, cars, buildings, furniture) to enhance their scenes with detailed assets.
- **Challenge format:** Coding, starter project with asset selector. Auto-grading confirms the correct model is added and positioned.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.04.02 – Add avatar models to the scene

_Dependency:_
  * T18.G4.04.01: Place 3D models from the CreatiCode library


- **Short name:** Place avatar models
- **Description:** Students add avatar models (humanoid characters) to their scenes, distinguishing avatars from static models and preparing for character animation.
- **Challenge format:** Coding, starter project. Auto-grading confirms an avatar is present in the scene.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.05.01 – Play built-in avatar animations

_Dependency:_
  * T18.G4.04.02: Add avatar models to the scene
  * T07.G3.01: Use a counted repeat loop


- **Short name:** Trigger avatar animations
- **Description:** Students use animation blocks to play one of 100+ built-in avatar animations (walking, running, jumping, dancing, waving) to bring characters to life.
- **Challenge format:** Coding, starter project with avatar. Auto-grading watches for the correct animation to play.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.05.02 – Animate scenery elements with rotation loops

_Dependency:_
  * T18.G4.05.01: Play built-in avatar animations


- **Short name:** Rotate scenery continuously
- **Description:** Students create looping animations for props (windmill spinning, fans rotating, wheels turning) by combining `forever` loops with rotation changes.
- **Challenge format:** Coding, starter project. Auto-grading watches the animation for correct rotation axis and speed.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.05.03 – Animate scenery with position changes

_Dependency:_
  * T18.G4.05.02: Animate scenery elements with rotation loops


- **Short name:** Animate object positions
- **Description:** Students use loops to create bobbing platforms, swinging pendulums, or moving obstacles by smoothly changing position coordinates over time.
- **Challenge format:** Coding, starter project. Auto-grading verifies position changes occur correctly.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.06 – Detect when 3D objects are close or touching

_Dependency:_
  * T18.G4.05.03: Animate scenery with position changes
  * T08.G3.01: Use a simple if in a script


- **Short name:** Detect 3D proximity
- **Description:** Students use distance checking or proximity detection to trigger events when the player gets near tokens, NPCs, or hazards, then respond with sound, score changes, or dialog.
- **Challenge format:** Coding, starter project. Auto-grading runs scripted movements to ensure the trigger fires at the correct distance.
- **CSTA:** E4‑PRO‑PF‑01.

---

## Grade 5

Grade 5 brings in 3D physics, repeated level layout, and scene polish. These skills depend on T17 (2D Motion & Physics) decision making so students can compare manual vs engine-based motion. Strands: **G5-A Physics setup**, **G5-B Structured building**, **G5-C Materials & effects**.

### T18.G5.01.01 – Initialize a 3D physics world with gravity

_Dependency:_
  * T18.G4.06: Detect when 3D objects are close or touching
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Enable 3D physics
- **Description:** Students add the CreatiCode 3D physics initialization block and set gravity direction and strength (X/Y/Z vectors) so objects can fall and interact realistically.
- **Challenge format:** Coding, guided setup. Auto-grading checks that physics initializes with the specified gravity vector.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.01.02 – Add static physics bodies for immovable objects

_Dependency:_
  * T18.G5.01.01: Initialize a 3D physics world with gravity


- **Short name:** Create static physics bodies
- **Description:** Students attach static (mass=0) physics bodies to floors, walls, and platforms that should not move but should block other objects.
- **Challenge format:** Coding, starter project. Auto-grading verifies static bodies are configured and do not move when hit.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.01.03 – Add dynamic physics bodies for movable objects

_Dependency:_
  * T18.G5.01.02: Add static physics bodies for immovable objects


- **Short name:** Create dynamic physics bodies
- **Description:** Students add dynamic physics bodies to players, crates, and projectiles, setting mass, restitution (bounciness), and friction so objects fall and collide realistically.
- **Challenge format:** Coding, starter project. Auto-grading tests that dynamic bodies fall with gravity and bounce correctly.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.02.01 – Configure restitution for bouncing behavior

_Dependency:_
  * T18.G5.01.03: Add dynamic physics bodies for movable objects


- **Short name:** Set object bounciness
- **Description:** Students adjust the restitution parameter on physics bodies to control how bouncy objects are (0 = no bounce, 1 = perfect bounce), useful for balls, projectiles, or platforms.
- **Challenge format:** Coding, starter project. Auto-grading measures bounce height to verify restitution settings.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.02.02 – Configure friction for sliding behavior

_Dependency:_
  * T18.G5.02.01: Configure restitution for bouncing behavior


- **Short name:** Set object friction
- **Description:** Students adjust friction parameters to create slippery ice surfaces or sticky floors, controlling how easily objects slide across surfaces.
- **Challenge format:** Coding, starter project. Auto-grading tests sliding distance to verify friction settings.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.03.01 – Detect physics collision events

_Dependency:_
  * T18.G5.02.02: Configure friction for sliding behavior
  * T08.G3.01: Use a simple if in a script


- **Short name:** Listen for collision events
- **Description:** Students use `when body A collides with body B` event blocks to detect when physics objects touch, preparing to respond with game logic.
- **Challenge format:** Coding, starter project. Auto-grading simulates collisions and verifies events fire correctly.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.03.02 – Respond to collisions by collecting items

_Dependency:_
  * T18.G5.03.01: Detect physics collision events


- **Short name:** Collect items on collision
- **Description:** Students respond to collision events by updating score, playing sounds, or removing collectible objects when the player touches them.
- **Challenge format:** Coding, starter project. Auto-grading checks that score updates and objects disappear on collision.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.04.01 – Use nested loops to create 3D grids of objects

_Dependency:_
  * T18.G5.03.02: Respond to collisions by collecting items
  * T07.G3.01: Use a counted repeat loop


- **Short name:** Generate 3D grids with loops
- **Description:** Students apply nested loops to stamp or spawn objects at evenly spaced coordinates in X and Z directions, creating grids of platforms, trees, or tiles.
- **Challenge format:** Coding, starter project. Auto-grading inspects code for nested loops and counts placed objects.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.04.02 – Add vertical variation to grid layouts

_Dependency:_
  * T18.G5.04.01: Use nested loops to create 3D grids of objects


- **Short name:** Create stepped terrain
- **Description:** Students extend grid generation to vary Y coordinates, creating stepped platforms, hills, or terraced landscapes by modifying height in loops.
- **Challenge format:** Coding, starter project. Auto-grading verifies height variation across grid positions.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.05.01 – Apply textures from the CreatiCode texture library

_Dependency:_
  * T18.G5.04.02: Add vertical variation to grid layouts


- **Short name:** Use texture library
- **Description:** Students select and apply textures from CreatiCode's 200+ texture library (wood, stone, grass, metal, etc.) to make surfaces look realistic.
- **Challenge format:** Coding, starter project. Auto-grading checks that specified objects have the requested texture applied.
- **CSTA:** E5‑SAS‑IM‑01.

### T18.G5.05.02 – Apply costume textures to objects

_Dependency:_
  * T18.G5.05.01: Apply textures from the CreatiCode texture library


- **Short name:** Use custom costume textures
- **Description:** Students apply custom-drawn costumes as textures on 3D surfaces, bridging 2D sprite art with 3D geometry.
- **Challenge format:** Coding, starter project. Auto-grading verifies costume texture is applied to 3D object.
- **CSTA:** E5‑SAS‑IM‑01.

### T18.G5.05.03 – Adjust material properties for metallic and roughness

_Dependency:_
  * T18.G5.05.02: Apply costume textures to objects


- **Short name:** Set material properties
- **Description:** Students adjust material blocks to control metallic sheen and surface roughness, creating different looks (shiny metal, matte plastic, rough stone).
- **Challenge format:** Coding, starter project. Auto-grading checks material property values.
- **CSTA:** E5‑SAS‑IM‑01.

### T18.G5.06.01 – Add fog for depth and atmosphere

_Dependency:_
  * T18.G5.05.03: Adjust material properties for metallic and roughness


- **Short name:** Enable fog effect
- **Description:** Students enable fog in the scene, adjusting color, density, and start/end distance to create atmospheric depth or spooky environments.
- **Challenge format:** Coding, starter project. Auto-grading inspects scene for fog with correct parameters.
- **CSTA:** E5‑PRO‑PF‑01, SAS‑IM.

### T18.G5.06.02 – Add particle emitters for fire and smoke

_Dependency:_
  * T18.G5.06.01: Add fog for depth and atmosphere


- **Short name:** Create fire and smoke particles
- **Description:** Students add particle emitter blocks (fire, smoke types) and position them to create torches, campfires, or explosions.
- **Challenge format:** Coding, starter project. Auto-grading verifies particle emitter exists with correct type and position.
- **CSTA:** E5‑PRO‑PF‑01, SAS‑IM.

### T18.G5.06.03 – Configure particle emitter colors and sizes

_Dependency:_
  * T18.G5.06.02: Add particle emitters for fire and smoke


- **Short name:** Customize particle appearance
- **Description:** Students adjust emitter configuration blocks to change particle colors, sizes, emission rates, and lifespans for custom visual effects.
- **Challenge format:** Coding, starter project. Auto-grading checks emitter configuration parameters.
- **CSTA:** E5‑PRO‑PF‑01, SAS‑IM.

---

## Grade 6

Grade 6 focuses on systems thinking: selective collisions, code quality, advanced controls, and triggered effects. Strands: **G6-A Physics systems**, **G6-B Code quality & controls**, **G6-C Effects & analytics**.

### T18.G6.01.01 – Apply forces and impulses to physics bodies

_Dependency:_
  * T18.G5.06.03: Configure particle emitter colors and sizes
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence


- **Short name:** Use forces on physics objects
- **Description:** Students apply forces or impulses to physics bodies to create jumps, launches, or wind effects, understanding the difference between continuous forces and instant impulses.
- **Challenge format:** Coding, starter project. Auto-grading tests that objects move correctly when forces are applied.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G6.01.02 – Set up collision groups for selective interaction

_Dependency:_
  * T18.G6.01.01: Apply forces and impulses to physics bodies


- **Short name:** Use collision groups
- **Description:** Students assign 3D physics bodies to collision groups or masks so only certain pairs collide (player with platforms/coins, enemies avoiding one another, projectiles passing through decorations).
- **Challenge format:** Coding, starter project with multiple body types. Auto-grading spawns test objects to confirm only requested collisions occur.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G6.01.03 – Freeze physics body axes for constrained movement

_Dependency:_
  * T18.G6.01.02: Set up collision groups for selective interaction


- **Short name:** Freeze physics axes
- **Description:** Students use freeze blocks to lock rotation or movement on specific axes, preventing unwanted spinning or movement (like keeping a character upright).
- **Challenge format:** Coding, starter project. Auto-grading verifies objects cannot rotate/move on frozen axes.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G6.02 – Trace multi-step 3D scripts with transforms

_Dependency:_
  * T18.G6.01.03: Freeze physics body axes for constrained movement


- **Short name:** Trace complex 3D scripts
- **Description:** Students read longer scripts that mix coordinate changes, rotations, and camera commands (orbit, zoom) and predict final object positions or camera headings without running it.
- **Challenge format:** Concept/code-reading. Auto-grading compares student predictions to simulated output.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G6.03 – Refactor repeated object creation with loops

_Dependency:_
  * T18.G6.02: Trace multi-step 3D scripts with transforms
  * T07.G3.01: Use a counted repeat loop
  * T11.G3.01: Understand when to use custom blocks vs loops


- **Short name:** Refactor 3D object creation
- **Description:** Students rewrite scripts that manually duplicate "add object / set transform" blocks into loops or custom functions, reducing duplication when spawning many props.
- **Challenge format:** Coding, refactor challenge. Auto-grading checks that a loop/function is used and scene output matches the original.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T18.G6.04.01 – Implement camera rotation with mouse input

_Dependency:_
  * T18.G6.03: Refactor repeated object creation with loops


- **Short name:** Create mouse-look camera
- **Description:** Students map mouse movement to camera yaw and pitch to build a smooth first-person or free-look camera, including clamping pitch to avoid flipping.
- **Challenge format:** Coding, starter project. Auto-grading simulates mouse motion and verifies camera rotates correctly.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G6.04.02 – Add virtual joystick controls

_Dependency:_
  * T18.G6.04.01: Implement camera rotation with mouse input


- **Short name:** Use virtual joystick
- **Description:** Students add on-screen virtual joystick controls for mobile-friendly 3D navigation, mapping joystick input to player movement.
- **Challenge format:** Coding, starter project. Auto-grading tests joystick input handling.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G6.05.01 – Add spot lights for focused illumination

_Dependency:_
  * T18.G6.04.02: Add virtual joystick controls


- **Short name:** Create spot light effects
- **Description:** Students add spot lights (like flashlights or stage lights) with configurable direction, cone angle, and intensity for dramatic focused lighting.
- **Challenge format:** Coding, starter project. Auto-grading verifies spot light properties.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G6.05.02 – Enable shadows for realistic lighting

_Dependency:_
  * T18.G6.05.01: Add spot lights for focused illumination


- **Short name:** Add shadow casting
- **Description:** Students enable shadow generation from lights, configuring which lights cast shadows and which objects receive them for depth and realism.
- **Challenge format:** Coding, starter project. Auto-grading checks shadow settings on lights and objects.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G6.05.03 – Add glow and highlight layers

_Dependency:_
  * T18.G6.05.02: Enable shadows for realistic lighting


- **Short name:** Use glow effects
- **Description:** Students add objects to glow or highlight layers to make them emit light or stand out, useful for power-ups, UI elements, or magical items.
- **Challenge format:** Coding, starter project. Auto-grading verifies objects are on glow layer.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G6.06.01 – Add speech bubbles to 3D characters

_Dependency:_
  * T18.G6.05.03: Add glow and highlight layers


- **Short name:** Display 3D speech bubbles
- **Description:** Students use speech bubble blocks to show dialog or thoughts above 3D characters, creating narrative or tutorial moments.
- **Challenge format:** Coding, starter project. Auto-grading checks speech bubble appears with correct text.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G6.06.02 – Detect mouse picking and clicking on 3D objects

_Dependency:_
  * T18.G6.06.01: Add speech bubbles to 3D characters


- **Short name:** Handle 3D object clicks
- **Description:** Students use mouse picking blocks to detect when users click on specific 3D objects, enabling interactive menus, selectable items, or clickable NPCs.
- **Challenge format:** Coding, starter project. Auto-grading simulates clicks and verifies events fire on correct objects.
- **CSTA:** MS‑PRO‑PF‑01.

---

## Grade 7

Grade 7 builds sophisticated mechanics: AI navigation, advanced copying, physics constraints, and cinematic storytelling. Strands: **G7-A Advanced geometry**, **G7-B Physics constraints**, **G7-C Cinematics & interaction**.

### T18.G7.01.01 – Create extruded 3D shapes from 2D polygons

_Dependency:_
  * T18.G6.06.02: Detect mouse picking and clicking on 3D objects


- **Short name:** Extrude 2D to 3D columns
- **Description:** Students use the column (extrude) block to create 3D shapes from 2D polygon outlines, making custom pillars, buildings, or unique geometry.
- **Challenge format:** Coding, starter project. Auto-grading verifies extruded shapes exist with correct parameters.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.01.02 – Create 3D text objects

_Dependency:_
  * T18.G7.01.01: Create extruded 3D shapes from 2D polygons


- **Short name:** Add 3D text to scenes
- **Description:** Students add flat or thick 3D text blocks to create signs, titles, or labels in the 3D world, adjusting font, size, and depth.
- **Challenge format:** Coding, starter project. Auto-grading checks for 3D text with specified content.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.01.03 – Use advanced shapes (cone, tube, stairs)

_Dependency:_
  * T18.G7.01.02: Create 3D text objects


- **Short name:** Add complex geometric shapes
- **Description:** Students add cone, tube, rectangle tube, and stair shapes to expand their building vocabulary for more complex architecture and level design.
- **Challenge format:** Coding, starter project. Auto-grading verifies presence of advanced shapes.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.02.01 – Copy objects using grid matrix patterns

_Dependency:_
  * T18.G7.01.03: Use advanced shapes (cone, tube, stairs)


- **Short name:** Use matrix copy
- **Description:** Students use grid matrix copying to efficiently duplicate objects in 3D arrays (like building blocks, trees in a forest) without manual loops.
- **Challenge format:** Coding, starter project. Auto-grading checks for matrix-copied objects.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.02.02 – Copy objects using mirror symmetry

_Dependency:_
  * T18.G7.02.01: Copy objects using grid matrix patterns


- **Short name:** Use mirror copy
- **Description:** Students use mirror copy blocks to create symmetrical designs across planes, useful for buildings, vehicles, or decorative patterns.
- **Challenge format:** Coding, starter project. Auto-grading verifies mirror symmetry in object placement.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.02.03 – Copy objects using rotational symmetry

_Dependency:_
  * T18.G7.02.02: Copy objects using mirror symmetry


- **Short name:** Use rotational copy
- **Description:** Students use rotational copy to duplicate objects in circular patterns (like petals, spokes, columns around a center), creating radial designs.
- **Challenge format:** Coding, starter project. Auto-grading checks for rotational pattern.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.03.01 – Add distance constraints between physics bodies

_Dependency:_
  * T18.G7.02.03: Copy objects using rotational symmetry


- **Short name:** Use distance constraints
- **Description:** Students add distance constraints to keep two physics bodies at a fixed or maximum distance, creating ropes, chains, or pendulums.
- **Challenge format:** Coding, starter project. Auto-grading tests constraint behavior.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.03.02 – Add hinge constraints for rotating joints

_Dependency:_
  * T18.G7.03.01: Add distance constraints between physics bodies


- **Short name:** Use hinge constraints
- **Description:** Students add hinge constraints to create rotating joints like doors, gates, or mechanical arms that pivot around an axis.
- **Challenge format:** Coding, starter project. Auto-grading verifies hinge rotation behavior.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.03.03 – Add fixed constraints for rigid connections

_Dependency:_
  * T18.G7.03.02: Add hinge constraints for rotating joints


- **Short name:** Use fixed constraints
- **Description:** Students use fixed constraints to weld physics bodies together, creating compound objects like connected train cars or attached weapons.
- **Challenge format:** Coding, starter project. Auto-grading checks bodies move together as one unit.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.04.01 – Implement waypoint-based NPC movement

_Dependency:_
  * T18.G7.03.03: Add fixed constraints for rigid connections


- **Short name:** Create waypoint patrol paths
- **Description:** Students code NPCs to follow a list of waypoint positions, pausing at each point or smoothly transitioning between them for patrol routes.
- **Challenge format:** Coding, starter project. Auto-grading measures NPC path against expected waypoints.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.04.02 – Implement distance-based chase AI

_Dependency:_
  * T18.G7.04.01: Implement waypoint-based NPC movement


- **Short name:** Create chase behavior
- **Description:** Students code NPCs to detect player distance, then compute direction vectors and adjust movement speed to chase or flee from the player.
- **Challenge format:** Coding, starter project. Auto-grading tests NPC response to player position.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.05.01 – Create compound physics bodies from merged meshes

_Dependency:_
  * T18.G7.04.02: Implement distance-based chase AI


- **Short name:** Merge and create compound bodies
- **Description:** Students use merge blocks to combine multiple meshes, then attach compound physics bodies for complex collision shapes like vehicles or multi-part objects.
- **Challenge format:** Coding, starter project. Auto-grading verifies compound body behavior.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.05.02 – Use carve operations for boolean geometry

_Dependency:_
  * T18.G7.05.01: Create compound physics bodies from merged meshes


- **Short name:** Carve shapes from meshes
- **Description:** Students use carve blocks to subtract one mesh from another, creating windows, doorways, or hollowed objects.
- **Challenge format:** Coding, starter project. Auto-grading checks carved geometry.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.06.01 – Script camera position transitions for cutscenes

_Dependency:_
  * T18.G7.05.02: Use carve operations for boolean geometry


- **Short name:** Animate camera paths
- **Description:** Students choreograph camera movements through position/target waypoints, blending easing functions to create smooth cinematic transitions for intros or cutscenes.
- **Challenge format:** Coding, starter project. Auto-grading watches camera timeline to ensure it hits all required points.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G7.06.02 – Add particle trails to moving objects

_Dependency:_
  * T18.G7.06.01: Script camera position transitions for cutscenes


- **Short name:** Create motion trails
- **Description:** Students attach trail effects to moving objects (projectiles, vehicles, characters) to show motion paths and add visual polish.
- **Challenge format:** Coding, starter project. Auto-grading verifies trail appears on moving object.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G7.06.03 – Configure advanced particle emitters with custom shapes

_Dependency:_
  * T18.G7.06.02: Add particle trails to moving objects


- **Short name:** Use shaped particle emitters
- **Description:** Students configure particle emitters to use box, sphere, cone, or mesh emitter shapes, controlling emission direction and area for complex effects.
- **Challenge format:** Coding, starter project. Auto-grading checks emitter shape configuration.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

---

## Grade 8

Grade 8 focuses on systems integration, scalability, and reflective design choices that mirror professional workflows. Strands: **G8-A Advanced systems**, **G8-B Export & VR/AR**, **G8-C Performance & critique**.

### T18.G8.01.01 – Create car simulations with physics

_Dependency:_
  * T18.G7.06.03: Configure advanced particle emitters with custom shapes


- **Short name:** Build physics car controls
- **Description:** Students use car simulation blocks to create drivable vehicles with realistic steering, acceleration, and suspension physics.
- **Challenge format:** Coding, starter project. Auto-grading tests car control response.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G8.01.02 – Implement dynamic level loading from data structures

_Dependency:_
  * T18.G8.01.01: Create car simulations with physics
  * T09.G3.01: Create and use a numeric variable for score or count


- **Short name:** Load levels from data
- **Description:** Students store level data in lists or records and write code to spawn objects per level, supporting editing, replay, and difficulty scaling.
- **Challenge format:** Coding, starter project. Auto-grading ensures at least two levels load correctly from data structures.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DF.

### T18.G8.01.03 – Create and manage multiple 3D camera views

_Dependency:_
  * T18.G8.01.02: Implement dynamic level loading from data structures


- **Short name:** Use multiple cameras
- **Description:** Students create two camera feeds (main gameplay plus minimap/UI view or split-screen for multiplayer) and manage when each renders.
- **Challenge format:** Coding, guided construction. Auto-grading confirms two distinct camera views refresh as specified.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G8.02.01 – Add skybox textures to scenes

_Dependency:_
  * T18.G8.01.03: Create and manage multiple 3D camera views


- **Short name:** Apply skybox backgrounds
- **Description:** Students add skybox textures to create 360-degree background environments (space, mountains, city skylines) for immersive scenes.
- **Challenge format:** Coding, starter project. Auto-grading verifies skybox is applied.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G8.02.02 – Add post-processing effects to scenes

_Dependency:_
  * T18.G8.02.01: Add skybox textures to scenes


- **Short name:** Use post-processing
- **Description:** Students enable post-processing effects (bloom, color grading, depth of field) to enhance visual quality and mood of entire scenes.
- **Challenge format:** Coding, starter project. Auto-grading checks post-processing settings.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G8.03.01 – Export 3D models as GLB files

_Dependency:_
  * T18.G8.02.02: Add post-processing effects to scenes


- **Short name:** Export GLB models
- **Description:** Students use export blocks to save created 3D geometry as GLB files for use in other applications or sharing.
- **Challenge format:** Coding, starter project. Auto-grading verifies export function is called.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G8.03.02 – Export 3D models as STL files for 3D printing

_Dependency:_
  * T18.G8.03.01: Export 3D models as GLB files


- **Short name:** Export STL for printing
- **Description:** Students export 3D geometry as STL files suitable for 3D printing, bridging digital creation with physical fabrication.
- **Challenge format:** Coding, starter project. Auto-grading verifies export function is called.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G8.04.01 – Implement AR world camera tracking

_Dependency:_
  * T18.G8.03.02: Export 3D models as STL files for 3D printing


- **Short name:** Use AR world camera
- **Description:** Students enable AR world camera to place 3D objects in real-world environments using device camera, creating augmented reality experiences.
- **Challenge format:** Coding, guided setup. Auto-grading checks AR initialization (simulation mode).
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G8.04.02 – Implement AR face tracking

_Dependency:_
  * T18.G8.04.01: Implement AR world camera tracking


- **Short name:** Use AR face tracking
- **Description:** Students use face tracking blocks to attach 3D objects to detected faces, creating filters or interactive AR effects.
- **Challenge format:** Coding, guided setup. Auto-grading checks face tracking initialization (simulation mode).
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G8.04.03 – Implement AR image tracking

_Dependency:_
  * T18.G8.04.02: Implement AR face tracking


- **Short name:** Use AR image markers
- **Description:** Students configure AR image tracking to display 3D content when specific images are detected by the camera, creating marker-based AR.
- **Challenge format:** Coding, guided setup. Auto-grading checks image tracking configuration.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G8.05.01 – Use mirrors for reflective surfaces

_Dependency:_
  * T18.G8.04.03: Implement AR image tracking


- **Short name:** Add mirror reflections
- **Description:** Students add mirror blocks to create reflective surfaces that show other objects in the scene, useful for water, windows, or polished floors.
- **Challenge format:** Coding, starter project. Auto-grading verifies mirror surface exists.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

### T18.G8.05.02 – Create custom geometry with points, lines, and triangles

_Dependency:_
  * T18.G8.05.01: Use mirrors for reflective surfaces


- **Short name:** Build custom meshes
- **Description:** Students use geometry blocks to define custom meshes from vertices, edges, and faces, creating unique shapes not available as primitives.
- **Challenge format:** Coding, guided construction. Auto-grading verifies custom geometry exists.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G8.06.01 – Analyze and optimize 3D scene performance

_Dependency:_
  * T18.G8.05.02: Create custom geometry with points, lines, and triangles


- **Short name:** Optimize 3D performance
- **Description:** Students profile a sluggish 3D project, identify bottlenecks (too many objects, physics bodies, or draw calls), and refactor using pooling, culling, or simplified meshes.
- **Challenge format:** Coding/debugging. Auto-grading measures frame time before/after and checks for required optimizations.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T18.G8.06.02 – Analyze trade-offs in 3D design decisions

_Dependency:_
  * T18.G8.06.01: Analyze and optimize 3D scene performance


- **Short name:** Justify 3D design choices
- **Description:** Students review a completed 3D project and explain design choices (physics vs manual motion, camera placement, effect usage), citing pros and cons relative to requirements.
- **Challenge format:** Concept, explanation + selection. Auto-grading scores selected answers and rubric-tagged justification.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

---

## Notes on Progression

- **Grade 3:** Blend conceptual microsteps (axes, camera views) with first CreatiCode scene setup, primitives broken down by shape type (box, sphere, cylinder, plane, capsule, torus), basic styling (color, transparency), and simple player controls.
- **Grade 4:** Expand to full scenes with all primitive shapes, progressive lighting types (ambient, directional, point), camera types (orbit, follow), imported models and avatars, avatar animations, scenery animation (rotation, position), and proximity detection.
- **Grade 5:** Layer in 3D physics with detailed body types (static, dynamic), physics properties (restitution, friction), collision events, structured scene generation with loops, comprehensive texture/material system, and particle effects.
- **Grade 6:** Emphasize systems thinking—forces/impulses, collision groups, axis freezing, refactoring, advanced camera controls (mouse-look, virtual joystick), advanced lighting (spot lights, shadows, glow), and interaction (speech bubbles, object picking).
- **Grade 7:** Build sophisticated mechanics—advanced geometry (extrude, text, complex shapes), copying techniques (grid matrix, mirror, rotational), physics constraints (distance, hinge, fixed), AI navigation (waypoints, chase), compound bodies, boolean operations, cinematic cameras, trails, and shaped emitters.
- **Grade 8:** Focus on production concerns—car physics, level loading, multiple cameras, skyboxes, post-processing, export capabilities (GLB, STL), AR/VR features (world camera, face tracking, image tracking), advanced rendering (mirrors, custom geometry), performance optimization, and reflective design analysis.
- **All grades:** Every skill intentionally maps to specific CreatiCode 3D blocks (scene, object, action, tool, physics, effect) with proper scaffolding. Dependencies into T14 (Games) and T17 (Physics) remain explicit. No same-grade dependencies within T18 (they're assumed). Cross-topic dependencies follow X-2 rule.
