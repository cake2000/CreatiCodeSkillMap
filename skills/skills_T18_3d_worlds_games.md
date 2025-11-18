# T18 – 3D Worlds & Games: K–8 Skill List (Draft v1)

Topic reference: `T18 3D Worlds & Games` in `domains_topics_overview.md`
Domain: CreatiCode-specific, Coding-heavy · CSTA focus: PRO‑PF, DAA‑DF, SAS‑IM

Each skill below has:

- a stable **ID** (`T18.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

3D awareness is developed through intuitive exploration of spatial concepts and directional understanding. Students learn basic 3D vocabulary and recognize depth in visual media.

### T18.GK.01 – Recognize depth in pictures (2D to 3D thinking)

- **Short name:** See depth in flat pictures
- **Description:** Students view a 2D image or video (e.g., a photograph or simple 3D animation) and identify which objects appear closer or farther away. They begin developing spatial vocabulary ("in front," "behind," "above," "below") and recognize that pictures can show 3D scenes.
- **Challenge format:** Concept, interactive visual. Show an image of a simple 3D scene (a landscape with houses and trees at different distances). Ask multiple-choice questions like "Which tree is closer to you?" or "What is behind the house?" Auto‑grading checks selected answers.
- **CSTA:** EK‑SAS‑IM‑03 (recognize computing tools for understanding the world).

### T18.GK.02 – Follow directions in a 3D space (left, right, forward, back)

- **Short name:** Understand 3D directions
- **Description:** Students watch an animated character or object move in 3D space and identify the direction of movement using basic directional language. They learn that 3D has more directions than 2D (forward/back in addition to left/right).
- **Challenge format:** Concept, interactive animation. A simple 3D object or character moves, and students select the direction (left, right, forward, backward, up, down). Prompt: "Which way did the character move?" Auto‑grading compares the chosen direction to the observed movement.
- **CSTA:** EK‑PRO‑PF‑01 (recognize sequence in actions).

### T18.GK.03 – Count objects in a 3D scene

- **Short name:** Count items in a 3D world
- **Description:** Students view a simple 3D scene in CreatiCode (e.g., a few boxes or spheres) and count visible objects, distinguishing between occluded (hidden) and visible items based on the camera angle.
- **Challenge format:** Concept, interactive scene. A CreatiCode 3D project displays a simple scene with several distinct 3D objects. Students are asked "How many boxes do you see?" or "How many red balls?" with picture‑based or numeric answer choices. Auto‑grading checks the count.
- **CSTA:** EK‑DAA‑DF‑01 (collect and interpret data about the world).

---

## Grade 1

Grade 1 students begin to interact with 3D scenes by moving a basic character or camera and positioning simple objects. They understand cause and effect in 3D movement.

### T18.G1.01 – Move a character forward/backward in 3D

- **Short name:** Move a character in 3D space
- **Description:** Students write code to move a 3D character (sprite with a 3D model) forward and backward along the Z-axis, observing how the character's distance from the camera changes.
- **Challenge format:** Coding, starter project. Provided: a 3D scene with a character model and a "when green flag clicked" block. Students add blocks to move the character forward (e.g., `change z by -10` to move closer to camera or away). Auto‑grading checks that the character moves along the Z-axis the correct direction and distance.
- **CSTA:** E1‑PRO‑PF‑01 (create code with sequence and events).

### T18.G1.02 – Rotate a 3D object

- **Short name:** Spin a 3D object
- **Description:** Students write code to rotate a 3D object (e.g., a cube or sphere) around one axis (X, Y, or Z), causing it to spin or turn.
- **Challenge format:** Coding, starter project. Provided: a 3D object and a "when green flag clicked" block. Students add blocks like `change rotation y by 30` to make the object rotate. Auto‑grading checks that rotation occurs on the specified axis and by the correct amount.
- **CSTA:** E1‑PRO‑PF‑01.

### T18.G1.03 – Place objects at specific X, Y, Z coordinates

- **Short name:** Position objects in 3D space
- **Description:** Students use code to set the position of a 3D object at specific coordinates (x, y, z), understanding how coordinates map to location in 3D space.
- **Challenge format:** Coding, guided construction. A 3D scene shows a grid or reference points. Students are instructed to place an object at a specific location (e.g., "Put the box at coordinates (50, 0, -100)") by setting x, y, z values. Auto‑grading compares the final position to the target.
- **CSTA:** E1‑DAA‑DF‑01 (collect and organize numeric data).

### T18.G1.04 – Predict object visibility based on camera angle

- **Short name:** Understand what the camera can see
- **Description:** Students predict which objects will be visible from a given camera angle. They learn that objects behind other objects or outside the camera's view are hidden.
- **Challenge format:** Concept, interactive visualization. Show a 3D scene from one camera angle and ask "Which ball can the camera see?" or "Is the box visible from this angle?" with visual answer choices. Auto‑grading checks selected answer.
- **CSTA:** E1‑SAS‑IM‑03 (describe benefits/harms of computing tools).

---

## Grade 2

Grade 2 students create simple 3D scenes and implement camera control. They use loops to create animated movement in 3D.

### T18.G2.01 – Use a loop to animate 3D movement

- **Short name:** Loop for 3D animation
- **Description:** Students use a `repeat` loop to move a 3D object multiple times or continuously, creating smooth animated movement rather than instantaneous jumps.
- **Challenge format:** Coding, starter project. Provided: a 3D object in an empty scene. Students create a `repeat` loop (e.g., `repeat 10 { change z by 5 }`) to make the object glide smoothly. Auto‑grading checks loop structure and that movement is smooth over multiple iterations.
- **CSTA:** E2‑PRO‑PF‑01 (create code with iteration).

### T18.G2.02 – Create a 3D scene with multiple objects

- **Short name:** Build a 3D scene
- **Description:** Students use blocks to add multiple 3D primitives (boxes, spheres, cylinders) to an empty 3D scene, positioning each one in different locations, creating a small world.
- **Challenge format:** Coding, guided construction. Prompt: "Create a 3D scene with 1 red box on the ground and 2 blue spheres floating above it." Provided: blocks to initialize 3D, add shapes, and set positions. Auto‑grading checks that the correct number and types of objects exist at approximately correct positions.
- **CSTA:** E2‑PRO‑PF‑01.

### T18.G2.03 – Control the camera with keyboard input

- **Short name:** Move the camera with arrow keys
- **Description:** Students add event blocks (key pressed) to control camera position or angle, enabling the player to look around a 3D scene.
- **Challenge format:** Coding, starter project. Provided: a 3D scene and `when key pressed` event blocks. Students add code to change the camera's position (x, y, z) or rotation when keys are pressed. Auto‑grading runs the project and checks that keyboard controls move the camera.
- **CSTA:** E2‑PRO‑PF‑01.

### T18.G2.04 – Distinguish between absolute and relative movement in 3D

- **Short name:** Absolute vs. relative position
- **Description:** Students understand the difference between setting an object to an absolute position (`set z to 50`) versus changing it by a relative amount (`change z by 10`).
- **Challenge format:** Concept, code‑reading item. Show two short scripts: one using `set` and one using `change`. Ask "Which script starts the object in the same place each time?" or "Which script moves the object further away each time it runs?" Auto‑grading checks the answer.
- **CSTA:** E2‑PRO‑PF‑01.

---

## Grade 3

Grade 3 students implement interactive 3D games with keyboard control, simple physics, and event handling in 3D environments.

### T18.G3.01 – Implement a forever loop for continuous 3D control

- **Short name:** Forever loop for 3D player control
- **Description:** Students use a `forever` loop with conditional key checks inside to enable smooth, continuous control of a 3D character (player-controlled avatar that responds to held keys).
- **Challenge format:** Coding, starter project. Provided: a 3D character and a `when green flag clicked` block. Students create a `forever` loop that checks for multiple key presses (e.g., WASD or arrow keys) and updates character position inside the loop. Auto‑grading runs the project and verifies that holding keys produces continuous movement.
- **CSTA:** E3‑PRO‑PF‑01 (develop code with iteration and selection).

### T18.G3.02 – Create a 3D platformer with a visible ground

- **Short name:** Build a 3D platform level
- **Description:** Students create a 3D scene with a ground plane (a large flat 3D box) and one or more floating platforms, establishing the foundation for a platformer game.
- **Challenge format:** Coding, guided construction. Prompt: "Create a 3D scene with a ground plane and 2 floating platforms at different heights." Provided: blocks to add large boxes/planes and position them. Auto‑grading checks that platforms exist and are positioned at different heights.
- **CSTA:** E3‑PRO‑PF‑01.

### T18.G3.03 – Detect collision between objects in 3D

- **Short name:** Detect 3D collisions
- **Description:** Students use collision detection blocks to check if a 3D player character is touching a platform, wall, or collectible object, enabling game logic like landing, blocking, or scoring.
- **Challenge format:** Coding, starter project. Provided: a player sprite with a 3D model and a platform. Students add an `if touching` block (or equivalent 3D collision block) to detect when the player lands on the platform. Auto‑grading runs the project and checks that collision is detected when positions overlap.
- **CSTA:** E3‑PRO‑PF‑01.

### T18.G3.04 – Apply gravity to a 3D object

- **Short name:** Add gravity in 3D
- **Description:** Students enable the 3D physics engine and apply gravity to a character or object, making it fall downward (along the Y-axis) until it collides with a surface.
- **Challenge format:** Coding, starter project. Provided: a 3D scene with physics initialized, a character, and a ground plane. Students use a block to add a physics body to the character and/or enable gravity. Auto‑grading runs the project and checks that the character falls and stops on the ground.
- **CSTA:** E3‑PRO‑PF‑01.

---

## Grade 4

Grade 4 students refine 3D game mechanics, implement jumping and collision response, and use variables to track game state in 3D worlds.

### T18.G4.01 – Implement jumping with physics

- **Short name:** Make a character jump
- **Description:** Students apply an upward impulse or force to a 3D character with physics enabled, allowing it to jump off the ground and fall back due to gravity.
- **Challenge format:** Coding, starter project. Provided: a character with physics body and gravity enabled, a ground plane. Students add an event (key space pressed) that applies an upward impulse when the player presses space. Auto‑grading runs the project and checks that the character jumps upward and falls back to the ground.
- **CSTA:** E4‑PRO‑PF‑01 (develop code from student-created algorithm).

### T18.G4.02 – Use a variable to track score in a 3D game

- **Short name:** Track game score
- **Description:** Students create a numeric variable to count collected items or points in a 3D game, incrementing it when the player touches a collectible object.
- **Challenge format:** Coding, starter project. Provided: a player character, a collectible 3D object (e.g., a coin), and collision detection. Students create a `score` variable, increment it when the player touches the coin, and display it. Auto‑grading checks variable initialization, increment logic, and final score after test gameplay.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.03 – Rotate a character to face movement direction

- **Short name:** Orient character based on input
- **Description:** Students modify character rotation based on the direction of movement, so the character "looks" in the direction it's moving (e.g., rotating around the Y-axis).
- **Challenge format:** Coding, starter project. Provided: a character and keyboard controls. Students add code to change the rotation when movement keys are pressed (e.g., `if key w pressed then change rotation y by -5`). Auto‑grading runs the project and verifies character rotation matches movement direction.
- **CSTA:** E4‑PRO‑PF‑01.

### T18.G4.04 – Clone 3D objects to create multiple instances

- **Short name:** Duplicate objects with cloning
- **Description:** Students use the clone block to create multiple instances of a 3D object (e.g., a collectible or enemy) at different positions within a game scene.
- **Challenge format:** Coding, starter project. Provided: a sprite with a 3D model and initial positioning code. Students use a loop and the `create clone` block to spawn multiple copies at different locations. Auto‑grading checks that the correct number of clones are created.
- **CSTA:** E4‑PRO‑PF‑01.

---

## Grade 5

Grade 5 students build complete 3D games with multiple levels, interactive cameras, and simulation of 3D physics phenomena. They use data structures to manage game state.

### T18.G5.01 – Use a 3D follow camera attached to the player

- **Short name:** Implement a follow camera
- **Description:** Students attach a follow camera to the player character so the camera tracks the character's position and rotation, maintaining a fixed offset (e.g., behind-and-above). This is a standard game camera mechanic.
- **Challenge format:** Coding, starter project. Provided: a 3D scene, a player character, and a follow-camera block. Students configure camera offset or use a block to attach the camera to the player. Auto‑grading runs the project and checks that the camera stays relative to the player and doesn't lose focus.
- **CSTA:** E5‑PRO‑PF‑01 (develop code from student-created algorithms).

### T18.G5.02 – Create a multi-level 3D platformer

- **Short name:** Design multi-level platformer
- **Description:** Students build or design a 3D platformer with 2–3 levels, each with its own platforms, collectibles, and enemies. They may use lists or variables to track current level or use separate sections of the scene.
- **Challenge format:** Coding, creative challenge with structure check. Prompt: "Create a 3D platformer with at least 2 playable levels, each with platforms and at least 1 collectible." Students design the geometry and gameplay. Auto‑grading inspects the code for level management (e.g., changing scenes, loading objects) and verifies that multiple playable areas exist.
- **CSTA:** E5‑PRO‑PF‑01.

### T18.G5.03 – Simulate falling water or rolling ball physics

- **Short name:** Simulate physics phenomena
- **Description:** Students use the 3D physics engine to simulate realistic behavior of objects: e.g., a ball rolling down a slope, water falling and bouncing off surfaces, or a block sliding with friction.
- **Challenge format:** Coding, starter project. Provided: physics initialized, objects with appropriate mass/friction/restitution. Prompt: "Use the physics engine to simulate a ball rolling down a slope and bouncing." Students add or adjust physics properties and create the slope geometry. Auto‑grading runs a simulation and checks that behavior is physically plausible.
- **CSTA:** E5‑DAA‑DF‑01 (collect and use multiple data types).

### T18.G5.04 – Use nested loops to arrange 3D objects in a grid

- **Short name:** Arrange objects in 3D grids
- **Description:** Students use nested loops to create a grid of 3D objects (e.g., a checkerboard of platforms, a wall of blocks, or an array of collectibles).
- **Challenge format:** Coding, starter project. Prompt: "Use nested loops to create a 4×3 grid of platforms." Students implement two nested loops to position objects at grid coordinates. Auto‑grading checks that objects are arranged in the correct pattern and counts.
- **CSTA:** E5‑PRO‑PF‑01.

---

## Grade 6

In middle school, students design and analyze 3D game mechanics, implement collision groups, and explore advanced camera and rendering concepts. They refine code for efficiency and clarity.

### T18.G6.01 – Set up collision groups for selective interaction

- **Short name:** Collision groups for game logic
- **Description:** Students use the 3D physics engine's collision groups to define which objects collide with which. For example, the player collides with platforms and coins but passes through walls that look like obstacles, or enemies collide with each other but not the player.
- **Challenge format:** Coding, starter project. Provided: multiple 3D objects (player, platforms, coins, walls) with physics bodies. Students assign collision groups and/or set collision flags so that specific pairs collide and others don't. Auto‑grading tests collision behavior by placing objects and checking which pairs interact.
- **CSTA:** MS‑PRO‑PF‑01 (analyze code and identify roles of components).

### T18.G6.02 – Trace a 3D project to predict object positions

- **Short name:** Trace 3D code and predict positions
- **Description:** Students read a 3D script with movement and rotation blocks and predict the final position and orientation of an object without running the code.
- **Challenge format:** Concept, code‑reading item. Show a script like `set x to 50, set y to 10, change z by 20, change rotation y by 90`. Ask "What is the object's final position?" or "Which way is the object facing?" with numeric or directional answer choices. Auto‑grading compares answers to simulation results.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G6.03 – Refactor repeated 3D object creation into a loop or function

- **Short name:** Refactor 3D object creation
- **Description:** Students are given a project with many repeated "add object, set position, set properties" blocks and rewrite it using a loop or custom function to reduce duplication.
- **Challenge format:** Coding, refactor challenge. Starter script manually creates and positions 5 platforms one by one. Students rewrite it to use a loop (and possibly a list of position data) to create and position all platforms with far less code. Auto‑grading checks code structure (loop or function present) and behavioral equivalence.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T18.G6.04 – Implement a camera with mouse look (rotate by mouse movement)

- **Short name:** Mouse-look camera control
- **Description:** Students implement a camera that rotates its view based on mouse movement, allowing the player to look around smoothly (common in first-person games).
- **Challenge format:** Coding, starter project. Provided: a 3D scene and blocks for mouse position input. Students use `mouse x` and `mouse y` reporters to update camera rotation angles. Auto‑grading runs the project and checks that moving the mouse rotates the camera view.
- **CSTA:** MS‑PRO‑PF‑01.

---

## Grade 7

Grade 7 students implement sophisticated 3D game mechanics, including NPC (non-player character) behavior, advanced collision response, and physics-based puzzles.

### T18.G7.01 – Implement pathfinding or waypoint-based NPC movement

- **Short name:** NPC navigation in 3D
- **Description:** Students create a non-player character (NPC) that moves between waypoints or toward a target position (player or goal) using distance calculations or a simple patrolling behavior.
- **Challenge format:** Coding, starter project. Provided: an NPC sprite with 3D model, player, and waypoint positions. Students implement code that moves the NPC toward waypoints or the player (e.g., using `if distance to [player] > 1 then move towards [player]`). Auto‑grading runs the project and checks that the NPC moves plausibly toward targets.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.02 – Design collision response for bouncing or sliding

- **Short name:** Custom collision response
- **Description:** Students use the 3D physics engine's properties (restitution, friction) to tune how objects respond to collisions: e.g., creating a bouncy ball, a sliding block, or a sticky object.
- **Challenge format:** Coding, starter project. Provided: multiple objects with physics bodies and a test scene. Students adjust restitution and friction values on objects to achieve desired behavior (bouncing, sliding, or sticking). Auto‑grading simulates collisions and checks that behavior matches the intended response.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G7.03 – Use 3D coordinates and distance calculations for game mechanics

- **Short name:** Distance and coordinate calculations in 3D
- **Description:** Students use distance formulas or conditional checks based on 3D positions (e.g., "if player within 5 units of this object") to trigger events or game logic, reinforcing spatial reasoning with numbers.
- **Challenge format:** Coding, starter project. Prompt: "Make an enemy spawn when the player gets within 10 units." Students calculate distance (possibly using `distance to` if available, or `sqrt(dx² + dy² + dz²)`) and trigger spawning. Auto‑grading places the player at known distances and checks if the event fires correctly.
- **CSTA:** MS‑DAA‑DF‑01 (examine relationships in data).

### T18.G7.04 – Implement a physics-based puzzle mechanic

- **Short name:** Physics-based puzzle
- **Description:** Students design a simple puzzle that requires using physics-based manipulation: e.g., rolling a ball into a goal, stacking blocks to reach an object, or using gravity to guide an object.
- **Challenge format:** Coding, creative challenge with structure check. Prompt: "Create a puzzle where the player must push a ball with gravity to roll it into a target area." Students design the environment and implement the physics and collision detection. Auto‑grading checks that the physics engine is active and the solution is playable.
- **CSTA:** MS‑PRO‑PF‑01.

---

## Grade 8

Grade 8 students build polished 3D games with advanced features: multiple cameras, UI overlays, networked gameplay, and optimization awareness. They reflect on their design choices.

### T18.G8.01 – Implement a level editor or dynamic level loading

- **Short name:** Load and switch between 3D levels
- **Description:** Students use variables or lists to store level data (e.g., object types, positions, properties) and implement code to load different levels dynamically, enabling replay value and multiple game worlds.
- **Challenge format:** Coding, starter project. Provided: a structure for level data (e.g., a list of objects with positions, or level numbers). Students implement code to initialize a level at startup and switch to a new level on user input or when a goal is reached. Auto‑grading checks that at least 2 distinct levels exist and can be loaded.
- **CSTA:** MS‑PRO‑PF‑01, DAA‑DF.

### T18.G8.02 – Use multiple cameras to implement split-screen or UI view

- **Short name:** Multiple camera systems
- **Description:** Students create a project with two cameras: one for the main 3D game view and one for a UI overlay (e.g., inventory, minimap, or score display), or split-screen for two players.
- **Challenge format:** Coding, guided construction. Prompt: "Create a 3D game with a main camera and a second camera for a minimap." Provided: blocks to create and switch cameras. Students add both camera types and script the switching or simultaneous rendering. Auto‑grading checks that two distinct camera views are rendered.
- **CSTA:** MS‑PRO‑PF‑01.

### T18.G8.03 – Analyze and optimize a 3D game for performance

- **Short name:** Optimize 3D performance
- **Description:** Students examine a 3D project that runs slowly (e.g., many clones or physics objects), identify the bottleneck (e.g., too many draw calls, excessive physics calculations), and refactor to improve frame rate.
- **Challenge format:** Concept and coding, debugging/optimization challenge. Provide a slow project and tell students: "This game drops frames when there are many enemies. Identify why and optimize." Students might reduce clone count, disable physics on non-essential objects, or use pooling. Auto‑grading runs timing tests and checks that frame rate improves.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T18.G8.04 – Analyze trade-offs in 3D game design decisions

- **Short name:** Justify 3D design choices
- **Description:** Students review a 3D game project and explain design decisions: e.g., "Why did I use physics for the player instead of manual movement?" or "Why is the camera positioned this way?" reflecting on alternatives and trade-offs.
- **Challenge format:** Concept, explanation plus selection. Show a 3D game with annotated code sections (e.g., camera setup, physics configuration). Ask: "Why use gravity instead of manual Y-movement?" with answer choices that include trade-offs (simplicity vs. control, realism vs. performance). Students choose the best explanation and optionally write a short justification. Auto‑grading scores selected answers and key reasoning.
- **CSTA:** MS‑PRO‑PF‑01, SAS‑IM.

---

## Notes on Progression

- **K–1:** Spatial intuition and basic 3D vocabulary; simple movement and observation.
- **2–3:** Interactive 3D scenes; keyboard control; basic physics (gravity, collision).
- **4–5:** Complete small games; camera control; physics refinement; organized scene building.
- **6–7:** Polished mechanics (NPCs, advanced physics, collision tuning); algorithmic thinking about 3D.
- **8:** Complex systems (level loading, multi-camera, optimization); design reflection.

All challenges emphasize the **CreatiCode 3D blocks** (initialize 3D, add shape, set position/rotation, attach physics, detect collisions, follow camera, etc.) and integrate with CreatiCode's Babylon.js backend. Students build concrete, auto-gradable, and visually rewarding 3D worlds and games.
