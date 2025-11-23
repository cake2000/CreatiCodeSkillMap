# T18 – 3D Worlds & Games (Phase 1 Optimized)

## Grade K

ID: T18.GK.01
Topic: T18 – 3D Worlds & Games
Skill: Explore 3D shapes in the real world
Description: Students identify and describe common 3D shapes (boxes/cubes, balls/spheres, cylinders/cans) in their classroom and daily life, building spatial awareness by feeling, drawing, and comparing these shapes before encountering them digitally.

Dependencies: None


## Grade 1

ID: T18.G1.01
Topic: T18 – 3D Worlds & Games
Skill: Match 3D shapes to their names
Description: Students view pictures or physical models of common 3D shapes (cube, sphere, cylinder, cone, pyramid) and match them to their correct names, learning vocabulary for basic 3D geometry through sorting and labeling activities.

Dependencies:
* T18.GK.01: Explore 3D shapes in the real world


## Grade 2

ID: T18.G2.01
Topic: T18 – 3D Worlds & Games
Skill: Identify front, top, and side views of 3D objects
Description: Students look at simple 3D objects (toy car, block tower, etc.) from different angles and draw or select the correct front, top, and side view silhouettes, developing spatial reasoning about how viewpoint changes appearance.

Dependencies:
* T18.G1.01: Match 3D shapes to their names


## Grade 3

ID: T18.G3.01
Topic: T18 – 3D Worlds & Games
Skill: Interpret 3D axis directions
Description: Students read a labeled axis diagram or CreatiCode gizmo and identify which axis controls width, height, and depth, linking math vocabulary to the 3D stage.

Dependencies:
* T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
* T03.G2.01: Choose subtasks for a simple project idea


ID: T18.G3.02
Topic: T18 – 3D Worlds & Games
Skill: Match camera views to 3D layouts
Description: Students compare front/top/side snapshots of the same object arrangement and match each snapshot to the correct camera icon, understanding how viewpoint affects what they see before coding cameras.

Dependencies:
* T18.G3.01: Interpret 3D axis directions


ID: T18.G3.03
Topic: T18 – 3D Worlds & Games
Skill: Initialize a 3D scene with default lighting and basic setup
Description: Students add a `when green flag clicked` script that calls the CreatiCode `initialize 3D scene [SCENETYPE] as hidden [ISHIDDEN v]` block (choosing a scene type like Empty, Grass Land, or City) so every run begins with a clean scene including default camera and lighting. They can optionally use `show axis` to visualize the x/y/z directions for learning purposes, and set basic scene properties like background color. The `as hidden` parameter controls whether the scene starts visible or off-screen (advanced usage).

Dependencies:
* T18.G3.02: Match camera views to 3D layouts
* T07.G3.02: Trace a script with a simple loop
* T03.G3.03: Create a 3‑panel storyboard for a project


ID: T18.G3.04
Topic: T18 – 3D Worlds & Games
Skill: Add box shapes with size parameters
Description: Students use the `add box [COLOR] size in x (SIZEX) y (SIZEY) z (SIZEZ) edge radius (R) as [NAME]` block to place rectangular box objects in the scene, learning to set color, dimensions in all three axes (x, y, z), optional edge radius for rounded corners, and giving each object a unique name. This is the foundation primitive shape for building 3D environments.

Dependencies:
* T18.G3.03: Initialize a 3D scene with default lighting and basic setup


ID: T18.G3.04.01
Topic: T18 – 3D Worlds & Games
Skill: Add sphere shapes with arc and slice parameters
Description: Students use the `add sphere [COLOR] size in x (SIZEX) y (SIZEY) z (SIZEZ) arc (ARC) slice (SLICE) sides (SIDES) as [NAME]` block to create spherical objects, learning to control the size in each dimension to create perfect spheres or ellipsoids. The arc and slice parameters allow creating partial spheres (hemispheres, wedges), and sides controls the smoothness of the sphere surface.

Dependencies:
* T18.G3.04: Add box shapes with size parameters


ID: T18.G3.04.02
Topic: T18 – 3D Worlds & Games
Skill: Add cylinder shapes with diameter and height parameters
Description: Students use the `add cylinder [COLOR] diameter top (DIAMETERTOP) bottom (DIAMETERBOTTOM) height (HEIGHT) arc (ARC) closed section [CLOSEDSECTION v] cap type [CAPTYPE v] sides (SIDES) as [NAME]` block to create cylindrical objects. They learn that different top and bottom diameters create cones or truncated cones, the arc parameter creates partial cylinders, and closed section/cap type control the cylinder ends.

Dependencies:
* T18.G3.04.01: Add sphere shapes with arc and slice parameters


ID: T18.G3.05
Topic: T18 – 3D Worlds & Games
Skill: Rotate objects around axes
Description: Students use the `rotate to angle (A) around the [AXIS v] axis in (T) seconds [ISBLOCKING v]` and `turn (N) degrees around the [AXIS v] axis in (T) seconds [ISBLOCKING v]` blocks to orient objects in 3D space, learning to rotate around x, y, and z axes to face different directions.

Dependencies:
* T18.G3.04.02: Add cylinder shapes with diameter and height parameters


ID: T18.G3.06
Topic: T18 – 3D Worlds & Games
Skill: Position shapes using x/y/z coordinates
Description: Students use the `move to x (X) y (Y) z (Z) in (T) seconds [ISBLOCKING v]` block to move an object to a specific location in 3D space, connecting coordinate concepts from earlier math/diagram skills (T02/T25) to actual 3D positioning. They learn that in CreatiCode's default camera view: X controls left-right, Y controls forward-backward, and Z controls up-down placement. They position objects and observe how changing each coordinate affects placement.

Dependencies:
* T18.G3.04: Add box shapes with size parameters


ID: T18.G3.07
Topic: T18 – 3D Worlds & Games
Skill: Change object colors
Description: Students use the `update color diffusion [COLOR] emission [COLOR] roughness (R) brightness (B) remove texture [DOREMOVE v] area [AREATYPE v]` block to change object colors, making simple adjustments to differentiate objects such as making the ground green or a sphere blue. They focus on the color parameters and basic usage, not advanced material properties.

Dependencies:
* T18.G3.06: Position shapes using x/y/z coordinates


ID: T18.G3.08
Topic: T18 – 3D Worlds & Games
Skill: Move a 3D player with keyboard input
Description: Students build a `forever` loop that checks arrow keys (or WASD) using `if key [KEY v] pressed` blocks and moves the player using `set speed [SPEEDTYPE v] to (N)` to move along the current direction, or incrementally adjusts position with `move to x y z` so a player cube can walk around the scene in all four directions.

Dependencies:
* T18.G3.06: Position shapes using x/y/z coordinates
* T07.G3.03: Build a forever loop for simple animation


ID: T18.G3.09
Topic: T18 – 3D Worlds & Games
Skill: Trace a short 3D script to predict positions
Description: Students read a 3-5 block script using `move to x y z`, `rotate to angle`, and `turn N degrees` blocks and predict the final position/orientation by drawing or describing the result without running it, reinforcing spatial reasoning and understanding of 3D transformations.

Dependencies:
* T18.G3.08: Move a 3D player with keyboard input
* T07.G3.04: Use repeat‑until to reach a simple goal


## Grade 4

ID: T18.G4.01
Topic: T18 – 3D Worlds & Games
Skill: Compose a multi-part 3D scene with basic primitives
Description: Students create a floor, obstacles, and backdrop objects using the three basic primitives (boxes, spheres, cylinders) learned in G3, aligning them precisely using position and rotation blocks to build a cohesive environment such as a room, park, or simple racetrack. They practice combining multiple objects into a unified scene.

Dependencies:
* T18.G3.09: Trace a short 3D script to predict positions


ID: T18.G4.01.01
Topic: T18 – 3D Worlds & Games
Skill: Add plane shapes for floors and walls
Description: Students use the `add plane [COLOR] width (WIDTH) height (HEIGHT) as [NAME]` block to create flat rectangular surfaces, typically for floors, walls, ceilings, or large flat platforms. They learn that planes are more efficient than thin boxes for flat surfaces and can be oriented using rotation to serve as vertical walls or angled ramps.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G4.01.02
Topic: T18 – 3D Worlds & Games
Skill: Add torus shapes for rings and wheels
Description: Students use the `add torus [COLOR] diameter (DIAMETER) thickness (THICKNESS) arc (ARC) sides (SIDES) as [NAME]` block to create donut-shaped ring objects, useful for wheels, portals, hoops, or decorative elements. The arc parameter allows creating partial rings (arcs), and sides controls the smoothness.

Dependencies:
* T18.G4.01.01: Add plane shapes for floors and walls


ID: T18.G4.01.03
Topic: T18 – 3D Worlds & Games
Skill: Add cone shapes for pointed objects
Description: Students use the `add cone [COLOR] diameter bottom (DIAMETERBOTTOM) height (HEIGHT) as [NAME]` block to create cone-shaped objects with a circular base tapering to a point, useful for traffic cones, mountain peaks, pointed roofs, or arrows. They understand cones are similar to cylinders but with zero top diameter.

Dependencies:
* T18.G4.01.02: Add torus shapes for rings and wheels


ID: T18.G4.01.04
Topic: T18 – 3D Worlds & Games
Skill: Add capsule shapes for rounded columns
Description: Students use the `add capsule [COLOR] diameter (DIAMETER) height (HEIGHT) as [NAME]` block to create pill-shaped objects (cylinders with hemispherical caps), useful for characters, poles, rounded pillars, or obstacles. Capsules are smoother than cylinders for objects that need soft rounded ends.

Dependencies:
* T18.G4.01.03: Add cone shapes for pointed objects


ID: T18.G4.01.05
Topic: T18 – 3D Worlds & Games
Skill: Add tube shapes for pipes and tunnels
Description: Students use the `add tube [COLOR] diameter (DIAMETER) height (HEIGHT) thickness (THICKNESS) arc (ARC) as [NAME]` block to create hollow cylindrical tubes, useful for pipes, tunnels, rings, or structural elements. The thickness parameter controls the wall thickness, and arc allows creating partial tubes.

Dependencies:
* T18.G4.01.04: Add capsule shapes for rounded columns


ID: T18.G4.01.06
Topic: T18 – 3D Worlds & Games
Skill: Add stair shapes for platforming
Description: Students use the `add stairs [COLOR] width (WIDTH) height (HEIGHT) depth (DEPTH) steps (STEPS) as [NAME]` block to create staircase objects with multiple steps, useful for platforming games or multi-level environments. They adjust width, height, depth, and number of steps to create stairs of different scales and proportions.

Dependencies:
* T18.G4.01.05: Add tube shapes for pipes and tunnels


ID: T18.G4.01.07
Topic: T18 – 3D Worlds & Games
Skill: Understand camera position and orientation
Description: Students learn that the camera is the viewpoint from which they see the 3D scene. They use `show axis` to visualize how the camera looks at the scene and understand basic camera concepts like position (where the camera is) and what it's looking at (target). They experiment with simple camera adjustments to see how viewpoint changes what appears on screen.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G4.02
Topic: T18 – 3D Worlds & Games
Skill: Add ambient light for general illumination
Description: Students use `add ambient light [COLOR] sky direction xyz (DIRX) (DIRY) (DIRZ) intensity (INTENSITY) as [NAME]` (hemispheric light) to create general illumination that comes from the sky direction, providing overall lighting for their scene and learning to adjust color and intensity for different atmospheres.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G4.02.01
Topic: T18 – 3D Worlds & Games
Skill: Add directional light for focused sun-like lighting
Description: Students use `add directional light [COLOR] in direction xyz (DIRX) (DIRY) (DIRZ) at xyz (POSX) (POSY) (POSZ) intensity (INTENSITY) as [NAME]` to create focused sun-like lighting from a specific direction, learning to position and aim lights to illuminate parts of their scene. They understand directional lights simulate distant light sources like the sun.

Dependencies:
* T18.G4.02: Add ambient light for general illumination


ID: T18.G4.02.02
Topic: T18 – 3D Worlds & Games
Skill: Add point lights to illuminate objects
Description: Students use `add point light [COLOR] at xyz (X) (Y) (Z) intensity (INTENSITY) show position [SHOW v] as [NAME]` to create localized light sources that radiate in all directions from a single point, learning to position lights near objects to highlight them, choosing colors and intensities for different effects like warm lamplight or bright stars.

Dependencies:
* T18.G4.02.01: Add directional light for focused sun-like lighting


ID: T18.G4.02.03
Topic: T18 – 3D Worlds & Games
Skill: Add spot lights for cone-shaped lighting
Description: Students use `add spot light [COLOR] at xyz (X) (Y) (Z) open angle (ANGLE) intensity (INTENSITY) blur (BLUR) show position [SHOW v] as [NAME]` to create cone-shaped lighting effects like flashlights or stage spotlights, tuning angle and intensity to achieve focused lighting effects. They learn spotlights combine position and direction.

Dependencies:
* T18.G4.02.02: Add point lights to illuminate objects


ID: T18.G4.02.04
Topic: T18 – 3D Worlds & Games
Skill: Manage lights dynamically (add, remove, switch on/off)
Description: Students use `remove light named [NAME]`, `remove all lights`, and `switch [ONOFF v] light named [NAME]` blocks to dynamically control lighting during gameplay, such as turning lights on/off when entering rooms or removing lights when changing levels.

Dependencies:
* T18.G4.02.01: Add directional light for focused sun-like lighting


ID: T18.G4.03
Topic: T18 – 3D Worlds & Games
Skill: Create a following camera
Description: Students use `add follow camera distance (D) z offset (ZOFFSET) v-angle (V) h-angle (H) direction lock [LOCKTYPE v] see-through (SEETHROUGH)% active [ISACTIVE v] as [NAME]` to create a camera that follows the player with an over-the-shoulder or third-person view, adjusting distance, vertical angle, horizontal angle, and direction lock for smooth following behavior. This is the most common camera type for games.

Dependencies:
* T18.G4.01.07: Understand camera position and orientation
* T18.G3.08: Move a 3D player with keyboard input


ID: T18.G4.03.01
Topic: T18 – 3D Worlds & Games
Skill: Create an orbiting camera
Description: Students use `add orbit camera distance (D) v-angle (V) h-angle (H) panning speed ratio (S) inputs key [KEY v] pointer [POINTER v] active [ACTIVE v] as [NAME]` for a camera that orbits around a target point, adjusting distance, vertical/horizontal angles, and panning speed. They enable keyboard or mouse controls for user-controlled orbiting, useful for exploring scenes or viewing objects from all angles.

Dependencies:
* T18.G4.03: Create a following camera


ID: T18.G4.04
Topic: T18 – 3D Worlds & Games
Skill: Use CreatiCode prebuilt 3D models
Description: Students use `add model [MODELTYPE] target height (H) origin offset x (OFFSETX) y (OFFSETY) z (OFFSETZ) rotation x (RX) y (RY) z (RZ) hidden [ISHIDDEN v] as [NAME]` to insert prebuilt CreatiCode models from the library (tree, car, character), then align them with primitives using position and rotation blocks to enhance their scenes with detailed assets.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G4.04.01
Topic: T18 – 3D Worlds & Games
Skill: Scale and resize objects
Description: Students use `update scale x (SX)% y (SY)% z (SZ)% in (T) seconds [BLOCKINGTYPE v]` to proportionally grow or shrink objects, or `update size x (SX) y (SY) z (SZ)` to set absolute dimensions, learning to make objects larger or smaller to fit their scene design. This works on all objects including primitives and models.

Dependencies:
* T18.G3.04: Add box shapes with size parameters


ID: T18.G4.04.02
Topic: T18 – 3D Worlds & Games
Skill: Apply textures to objects
Description: Students use the `update texture [TEXTURENAME] unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [AREATYPE v]` block to apply textures from the library to objects, making surfaces look like brick, wood, grass, or other materials. They learn basic texture application without advanced material properties.

Dependencies:
* T18.G3.07: Change object colors


ID: T18.G4.05
Topic: T18 – 3D Worlds & Games
Skill: Animate a 3D object with simple movement
Description: Students create simple animations by using `move to x y z in (T) seconds` or `rotate to angle (A) around the [AXIS v] axis in (T) seconds` to make a single object move or rotate over time, learning basic 3D animation concepts before applying loops.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives
* T07.G3.01: Use a counted repeat loop


ID: T18.G4.05.01
Topic: T18 – 3D Worlds & Games
Skill: Animate scenery elements with loops
Description: Students create looping animations for props (windmill spinning, lights pulsing, platforms bobbing) by combining `forever` loops with `rotate to angle (A) around the [AXIS v] axis in (T) seconds [ISBLOCKING v]` or `turn (N) degrees around the [AXIS v] axis` for rotation, or `move to x y z in (T) seconds` for position changes, creating continuous motion effects.

Dependencies:
* T18.G4.05: Animate a 3D object with simple movement


ID: T18.G4.06
Topic: T18 – 3D Worlds & Games
Skill: Detect when objects overlap
Description: Students use `broadcast [MESSAGE] when [DIMENSIONTYPE v] objects overlap [OBJECTNAME1] from [SPRITENAME1 v] and [OBJECTNAME2] from [SPRITENAME2 v]` to detect when bounding boxes intersect, creating simple trigger zones for collecting items or entering areas without complex collision physics.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives
* T08.G3.01: Use a simple if in a script


ID: T18.G4.06.01
Topic: T18 – 3D Worlds & Games
Skill: Use distance sensors to detect obstacles
Description: Students use `set distance sensor front [ONOFFFRONT v] back [ONOFFBACK v] left [ONOFFLEFT v] right [ONOFFRIGHT v] down [ONOFFDOWN v] up [ONOFFUP v] max distance (MAXD) count [COUNT] visible [ISVISIBLE v]` to enable distance sensors in six directions, then use `distance to nearest obstacle in the [DIRECTION v] direction for [OBJECTNAME]` and `name of nearest obstacle in the [DIRECTION v] direction for [OBJECTNAME]` to detect nearby objects without physical collision.

Dependencies:
* T18.G4.06: Detect when objects overlap


ID: T18.G4.06.02
Topic: T18 – 3D Worlds & Games
Skill: Understand collision detection types (raycast vs overlap vs physics)
Description: Students learn the three collision detection methods in CreatiCode 3D: (1) Raycast collision using `turn on collision with` for blocking movement when objects touch, (2) Overlap detection using `broadcast when objects overlap` for trigger zones that detect when bounding boxes intersect (already learned in G4.06), and (3) Physics collision using `broadcast on collision between physics bodies` for realistic impacts with the physics engine (to be learned in G5). They identify at least 3 game mechanics and choose the appropriate collision method for each: walls should use raycast to block movement, collectibles should use overlap to trigger pickup, and bouncing balls should use physics for realistic impacts.

Dependencies:
* T18.G4.06: Detect when objects overlap


ID: T18.G4.07
Topic: T18 – 3D Worlds & Games
Skill: Trigger events when 3D objects touch (raycast collision)
Description: Students use `turn on [ISBLOCKING v] collision with [SPRITENAME v] collider z offset (ZOFFSET) precision [PRECISIONTYPE v] debug [ISDEBUG v]` to enable collision detection, then use the `when colliding with [SPRITENAME v]` hat block or `broadcast [MESSAGE] on collision between [OBJECTNAME1] and [OBJECTNAME2]` to detect when the player touches tokens or obstacles, responding by playing sounds, updating score, or showing dialog.

Dependencies:
* T18.G4.06.02: Understand collision detection types (raycast vs overlap vs physics)


ID: T18.G4.08
Topic: T18 – 3D Worlds & Games
Skill: Control model animations
Description: Students use `start model animation [NAME] looping [ISLOOPING v] progress from (PSTART) to (PEND) speed ratio (SPEEDRATIO)` to play built-in animations embedded in imported GLB/GLTF models (e.g., animated props, vehicles), controlling whether the animation loops and at what speed it plays.

Dependencies:
* T18.G4.04: Use CreatiCode prebuilt 3D models


ID: T18.G4.08.01
Topic: T18 – 3D Worlds & Games
Skill: Add and control avatar animations
Description: Students use `add avatar [AVATARTYPE v] height (H) as [NAME]` to place a humanoid character, then `add animations [ANIMATIONLIST]` to load animation clips from the library (walk, idle, jump, dance), and `start animation [NAME] looping [ISLOOPING v] progress from (PSTART) to (PEND) speed ratio (SPEEDRATIO)` to play animations, syncing animations with user input or game events.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G4.09
Topic: T18 – 3D Worlds & Games
Skill: Add 3D text for labels and signs
Description: Students use `add 3D text [TEXT] font [FONT v] color [COLOR] width (WIDTH) height (HEIGHT) diameter (DIAMETER) camera facing [CAMERAFACING v] as [NAME]` to create flat text objects for signs and labels, or `add 3D thick text [TEXT] font [FONT v] color [COLOR] width (WIDTH) height (HEIGHT) thickness (THICKNESS) diameter (DIAMETER) camera facing [CAMERAFACING v] as [NAME]` for solid lettering, choosing fonts, sizes, and whether text always faces the camera for readability.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G4.10
Topic: T18 – 3D Worlds & Games
Skill: Pick 3D objects with mouse or touch
Description: Students use `turn on picking with [BUTTON] for objects created in sprites [SPRITELIST] on [POINTERACTION v]` to enable object picking, then use the `when an object from this sprite is picked` hat block along with `picked object name` and `picked point x/y/z pos` reporters to respond to clicks or taps on 3D objects, creating interactive selections.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G4.10.01
Topic: T18 – 3D Worlds & Games
Skill: Drag 3D objects with mouse or touch
Description: Students enable picking and use `set dragging mode [DRAGGINGMODE v] direction X (DX) Y (DY) z (DZ)` to configure drag behavior, then use hat blocks `when an object starts to be dragged`, `when an object is being dragged`, and `when an object stops being dragged` to move objects interactively. They optionally set drag limits with `set dragging limits min/max xyz` to constrain movement.

Dependencies:
* T18.G4.10: Pick 3D objects with mouse or touch


ID: T18.G4.11
Topic: T18 – 3D Worlds & Games
Skill: Add fog effects for atmosphere
Description: Students use `set scene fog [MODE v] [COLOR] start (STARTDISTANCE) end (FULLDISTANCE) density (DENSITY)` with mode options (linear or exponential), configure start/end distances for linear fog or density for exponential fog, and choose fog color to create atmospheric depth such as misty forests, underwater scenes, or spooky environments.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G4.11.01
Topic: T18 – 3D Worlds & Games
Skill: Change sky background
Description: Students use `set sky [SKYTYPE]` to change the scene background from a solid color to realistic sky textures (Blue Sky, Night Sky, Sunset, etc.) or remove the sky with `remove sky`, creating atmospheric environments that match their game's setting or mood.

Dependencies:
* T18.G3.03: Initialize a 3D scene with default lighting and basic setup


ID: T18.G4.12
Topic: T18 – 3D Worlds & Games
Skill: Add on-screen joystick controls
Description: Students use `add [SIDE v] joystick [COLOR1] [COLOR2] scale [SCALE]` to add left or right virtual joysticks to the screen for touchscreen devices, then read joystick input with `[SIDE v] joystick [PROPERTY v]` reporters to control player movement or camera rotation, making games playable on tablets and phones.

Dependencies:
* T18.G3.08: Move a 3D player with keyboard input


## Grade 5

ID: T18.G5.01
Topic: T18 – 3D Worlds & Games
Skill: Initialize a 3D physics world
Description: Students add the `enable physics for scene with gravity (GRAVITY)` block to initialize the physics engine, typically setting gravity to -100 for realistic downward pull on the Z-axis. They verify objects respond to physics by enabling debug visualization with the debug parameter when adding physics bodies, seeing collision shapes overlaid on objects.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G5.02
Topic: T18 – 3D Worlds & Games
Skill: Attach static physics bodies
Description: Students use `add [SHAPE v] physics body with mass (MASS) restitution (RESTITUTION)% friction (FRICTION)% frozen [ISFROZEN v] debug [ISDEBUG v] [COLOR]` to add static physics bodies (mass = 0) to objects like floors, walls, and platforms that don't move. They learn that static bodies provide collision surfaces for dynamic objects to interact with, and adjust restitution (bounciness) and friction (surface grip) to create different surface properties.

Dependencies:
* T18.G5.01: Initialize a 3D physics world


ID: T18.G5.02.01
Topic: T18 – 3D Worlds & Games
Skill: Attach dynamic physics bodies
Description: Students use `add [SHAPE v] physics body with mass (MASS) restitution (RESTITUTION)% friction (FRICTION)% frozen [ISFROZEN v] debug [ISDEBUG v] [COLOR]` to add dynamic physics bodies (mass > 0) to objects like players, crates, or balls that react to gravity and forces. They experiment with different mass values to see how heavier objects behave differently from lighter ones, and adjust restitution for bounciness and friction for surface grip.

Dependencies:
* T18.G5.02: Attach static physics bodies


ID: T18.G5.03
Topic: T18 – 3D Worlds & Games
Skill: Detect physics collisions to collect items
Description: Students use `broadcast [BROADCASTMESSAGE] on collision between physics bodies of [NAME] from [SPRITENAME v] and [NAME2] from [SPRITENAME2 v]` or check `names of physics bodies in contact for [NAME]` to detect when physics-enabled objects collide, then respond by changing score, removing collectible objects with `remove object named [NAME]`, or playing sounds when the player touches items.

Dependencies:
* T18.G5.02.01: Attach dynamic physics bodies


ID: T18.G5.04
Topic: T18 – 3D Worlds & Games
Skill: Use repeat loops to create multiple objects
Description: Students apply a simple `repeat (N)` loop to create multiple copies of objects at different positions, incrementing x, y, or z coordinates in each iteration to stamp or spawn objects in a row or column, learning to apply loop concepts from T07 to 3D object creation.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives
* T07.G3.01: Use a counted repeat loop


ID: T18.G5.04.01
Topic: T18 – 3D Worlds & Games
Skill: Use nested loops to arrange 3D objects in grids
Description: Students apply nested loops (loop inside a loop) to stamp or spawn platforms, trees, or tiles at evenly spaced coordinates by incrementing x and y (or other combinations) values in each iteration, creating 2D grids or 3D arrays. They optionally vary height or add random offsets for stepped terrain or natural-looking layouts. This builds on loop programming skills from T04.G3+ or T07.G4+.

Dependencies:
* T18.G5.04: Use repeat loops to create multiple objects
* T07.G4.01: Use nested loops to create complex patterns


ID: T18.G5.04.02
Topic: T18 – 3D Worlds & Games
Skill: Use copy by matrix for object arrays
Description: Students use `copy by matrix count in xyz (COUNTX) (COUNTY) (COUNTZ) spacing in xyz (SPACINGX) (SPACINGY) (SPACINGZ)` to automatically create grids, rows, or 3D arrays of objects with a single block, optionally adding random variation with spacing/scale/rotation randomness parameters for more efficient object duplication than manual loops.

Dependencies:
* T18.G5.04.01: Use nested loops to arrange 3D objects in grids


ID: T18.G5.04.03
Topic: T18 – 3D Worlds & Games
Skill: Use mirror and rotation copying
Description: Students use `copy to mirror position [TYPE v]` to create symmetrical copies across X, Y, or Z planes, and `copy to rotated position around the [AXISNAME v] axis count (N) degree step (STEP)` to create radial arrangements like flower petals, pillars around a center, or rotating platforms.

Dependencies:
* T18.G5.04.02: Use copy by matrix for object arrays


ID: T18.G5.05
Topic: T18 – 3D Worlds & Games
Skill: Apply detailed textures with PBR materials
Description: Students use `update texture [TEXTURENAME] unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [AREATYPE v]` to apply tileable textures with advanced UV scaling, `update texture using costume [COSTUMENAME v] unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [AREATYPE v]` to use custom images, and `update color diffusion [COLOR] emission [COLOR] roughness (R) brightness (B) remove texture [DOREMOVE v] area [AREATYPE v]` to adjust PBR (Physically Based Rendering) material properties including roughness and emission, making surfaces like walls, roads, or floors look realistic with proper material behavior.

Dependencies:
* T18.G4.04.02: Apply textures to objects


ID: T18.G5.06
Topic: T18 – 3D Worlds & Games
Skill: Enable shadows from lights
Description: Students use `cast shadow [DOCAST v] from light named [NAME] blur size (BLUR)` to make objects cast shadows from directional or point lights, and `receive shadow [DORECEIVE v]` to make surfaces show shadows, adjusting blur for soft or sharp shadow edges to enhance realism.

Dependencies:
* T18.G4.02.02: Add point lights to illuminate objects
* T18.G4.02.01: Add directional light for focused sun-like lighting


ID: T18.G5.07
Topic: T18 – 3D Worlds & Games
Skill: Add prebuilt particle emitters
Description: Students use `add prebuilt emitter for [TYPE v] [COLOR1] [COLOR2] capacity (C) texture size (TEXTURESIZE) source size (SOURCESIZE) speed (SPEED) max life (MAXLIFE) as [NAME]` to add fire, smoke, rain, snow, or sparks effects with simple configuration, and `start emitter [NAME] [RATETYPE v] of (N)` to activate the effects, enhancing scenes with dynamic visual feedback.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G5.08
Topic: T18 – 3D Worlds & Games
Skill: Apply forces and impulses to physics bodies
Description: Students use `apply force strength (SIZE) direction xyz (X) (Y) (Z) at relative point xyz (X2) (Y2) (Z2) to [NAME]` and `apply impulse strength (SIZE) direction xyz (X) (Y) (Z) at relative point xyz (X2) (Y2) (Z2) to [NAME]` to push or launch physics bodies in a direction. They differentiate between continuous forces (for sustained movement like wind) and impulses (for instant kicks like jumping, shooting, or explosions). NAME can be left empty to target the current sprite object.

Dependencies:
* T18.G5.02.01: Attach dynamic physics bodies


ID: T18.G5.08.01
Topic: T18 – 3D Worlds & Games
Skill: Remove objects and reset scenes
Description: Students use `remove object named [NAME]` to delete specific objects (collected items, defeated enemies), `remove all objects` to clear the scene, and combine these with scene reinitialization to implement level resets or transitions between game states.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G5.09
Topic: T18 – 3D Worlds & Games
Skill: Adjust camera distance and angles dynamically
Description: Students use `set camera distance (D) v-angle (V) h-angle (H) z offset (OFFSET) target xyz (X) (Y) (Z) in (T) seconds` to smoothly animate the camera view during gameplay, such as zooming in when aiming or pulling back for a wide view of the level, creating cinematic transitions or responsive camera behavior based on game events.

Dependencies:
* T18.G4.01.07: Understand camera position and orientation


ID: T18.G5.10
Topic: T18 – 3D Worlds & Games
Skill: Import external 3D models from URLs
Description: Students use `add public object at URL [OBJECTURL] as [TYPE] target height (H) as [NAME]` to load GLB/GLTF models from external URLs, learning to import custom 3D assets from online sources and integrate them with library models and primitives in their scenes.

Dependencies:
* T18.G4.04: Use CreatiCode prebuilt 3D models


## Grade 6

ID: T18.G6.01
Topic: T18 – 3D Worlds & Games
Skill: Set up collision groups for selective interaction
Description: Students use `update collision group [COLLISIONGROUP v] target groups [TARGETGROUPS] for [NAME]` to assign physics bodies to collision groups (1-8) and specify which target groups they can collide with, creating selective interactions where players collide with platforms and coins but not decorations, enemies avoid each other, or projectiles pass through certain objects.

Dependencies:
* T18.G5.03: Detect physics collisions to collect items
* T18.G5.08: Apply forces and impulses to physics bodies


ID: T18.G6.02
Topic: T18 – 3D Worlds & Games
Skill: Debug simple 3D scripts with visualization tools
Description: Students identify and fix bugs in basic 3D projects by using debugging tools: `show axis` to visualize X/Y/Z directions and verify coordinate systems, `show bounding box` to see object boundaries and check sizing/positioning, and enabling debug parameters in collision blocks to visualize collision shapes. They follow a process: identify the bug, form a hypothesis about the cause, use debugging tools to gather evidence, trace script execution with console/say blocks, fix the issue, and verify the solution works.

Dependencies:
* T18.G4.01: Compose a multi-part 3D scene with basic primitives


ID: T18.G6.03
Topic: T18 – 3D Worlds & Games
Skill: Refactor simple repeated object creation into loops
Description: Students identify scripts that manually duplicate "add object / set position" blocks multiple times and rewrite them using simple `repeat (N)` loops, reducing code duplication when spawning basic props or creating simple object patterns.

Dependencies:
* T18.G5.04: Use repeat loops to create multiple objects


ID: T18.G6.04
Topic: T18 – 3D Worlds & Games
Skill: Refactor complex 3D object creation into loops or functions
Description: Students rewrite scripts that manually duplicate complex object creation patterns into nested loops or custom blocks (functions), reducing duplication when spawning many props with variations or creating parametric scenes. They use custom blocks with inputs to create reusable object creation functions.

Dependencies:
* T18.G5.04.01: Use nested loops to arrange 3D objects in grids
* T11.G4.01: Create a custom block with inputs


ID: T18.G6.05
Topic: T18 – 3D Worlds & Games
Skill: Debug complex 3D scenes with nested loops and physics
Description: Students debug advanced 3D projects with nested loops, physics interactions, and complex script flow by tracing execution order, checking object naming in loops, verifying coordinate systems, using `show bounding box` for object boundaries, and enabling physics debug visualization to see invisible collision shapes and forces. They apply systematic debugging to multi-layered problems.

Dependencies:
* T18.G5.04.01: Use nested loops to arrange 3D objects in grids
* T18.G6.02: Debug simple 3D scripts with visualization tools


ID: T18.G6.06
Topic: T18 – 3D Worlds & Games
Skill: Capture mouse movement for camera control
Description: Students use the `lock pointer [DOLOCK v]` block to lock the mouse pointer to the screen center and capture raw mouse movement, then read pointer delta X and Y values to detect mouse movement. This is the foundation for implementing mouse-look camera controls in first-person or free-look games.

Dependencies:
* T18.G4.03: Create a following camera
* T09.G4.01: Capture user text or number input into a variable


ID: T18.G6.06.01
Topic: T18 – 3D Worlds & Games
Skill: Implement a camera with mouse look
Description: Students build on pointer locking to map mouse movement delta values to camera h-angle (horizontal rotation) and v-angle (vertical rotation), creating smooth first-person or free-look camera control. They implement vertical angle clamping to prevent the camera from flipping upside-down, typically limiting v-angle between -90 and +90 degrees.

Dependencies:
* T18.G6.06: Capture mouse movement for camera control


ID: T18.G6.07
Topic: T18 – 3D Worlds & Games
Skill: Trigger advanced visual effects on events
Description: Students enable or disable advanced effects (bloom via `add pipeline vignette (VRADIUS) [COLOR] bloom strength (BSTRENGTH) threshold (BTHRESHOLD)% kernel (BKERNEL) antialiasing [ISANTIALIASING v] sharpening [ISSHARPENING v] camera contrast (C) exposure (E)`, spotlight cones, burst particles via `start emitter by burst`) in response to events such as power-ups or low health, coordinating visuals with game state.

Dependencies:
* T18.G5.07: Add prebuilt particle emitters
* T08.G4.01: Use if‑else or else‑if chains


ID: T18.G6.08
Topic: T18 – 3D Worlds & Games
Skill: Create custom particle emitters with advanced configuration
Description: Students create custom emitters with `add particle emitter shape [SHAPETYPE v] texture [TEXTURE] facing camera [FACINGCAM v] life min (MINLIFE) max (MAXLIFE) capacity (C) GPU [USEGPU v] time ratio (TIMERATIO)% as [NAME]`, then configure detailed properties with blocks like `configure emitter [NAME] color`, `configure emitter [NAME] size`, `configure emitter [NAME] movement` to create unique visual effects beyond the prebuilt options.

Dependencies:
* T18.G5.07: Add prebuilt particle emitters


ID: T18.G6.09
Topic: T18 – 3D Worlds & Games
Skill: Add fixed constraints to connect physics bodies
Description: Students use `add fixed constraint between bodies of [OBJECTNAME] from [SPRITENAME v] and [OBJECTNAME2] from [SPRITENAME2 v] named [JOINTNAME]` to create rigid connections between physics objects, making them move together as one unit (e.g., attaching decorations to moving platforms, connecting pieces of a compound object).

Dependencies:
* T18.G5.08: Apply forces and impulses to physics bodies
* T18.G6.01: Set up collision groups for selective interaction


ID: T18.G6.10
Topic: T18 – 3D Worlds & Games
Skill: Create object hierarchies with parent-child relationships
Description: Students use `set object [OBJECTNAME] from sprite [SPRITENAME v] as parent and update position/scale [DOUPDATE v]` to attach child objects to parent objects, so when the parent moves or rotates, all children move with it (e.g., wheels attached to a car, decorations on a platform), then use `unlink parent` or `unlink all children` to break relationships when needed.

Dependencies:
* T18.G5.04.01: Use nested loops to arrange 3D objects in grids


## Grade 7

ID: T18.G7.01
Topic: T18 – 3D Worlds & Games
Skill: Implement waypoint-based NPC movement
Description: Students code an NPC (non-player character) that follows a sequence of waypoints (target positions) stored in a list, moving smoothly between each position using `move to x (X) y (Y) z (Z) in (T) seconds [ISBLOCKING v]` blocks and list iteration. They create patrol patterns where NPCs move through a set path repeatedly, or chase behavior where NPCs move toward the player by computing direction vectors with `point to position x (PX) y (PY) z (PZ)` or `rotate to direction x y z`.

Dependencies:
* T10.G5.01: Use a list to store multiple values
* T18.G3.08: Move a 3D player with keyboard input


ID: T18.G7.02
Topic: T18 – 3D Worlds & Games
Skill: Design collision response for bouncing or sliding
Description: Students use `update physics property restitution (RESTITUTION)% friction (FRICTION)%` to tweak bounciness and friction values on physics bodies, and apply impulses with `apply impulse` on collision events to achieve different behaviors such as bouncy projectiles (high restitution), sliding ice blocks (low friction), or sticky platforms (high friction, low restitution).

Dependencies:
* T18.G5.08: Apply forces and impulses to physics bodies
* T18.G6.09: Add fixed constraints to connect physics bodies


ID: T18.G7.03
Topic: T18 – 3D Worlds & Games
Skill: Use 3D distance calculations for game mechanics
Description: Students use `distance between objects [OBJECT1] and [OBJECT2]` or `broadcast [MESSAGE] when [DIMENSION v] distance less than or equal to (D) between [OBJECTNAME1] from [SPRITENAME1 v] and [OBJECTNAME2] from [SPRITENAME2 v]` to trigger events based on proximity, implementing mechanics such as proximity mines, aggro ranges for enemies, safe zones, or camera shakes when objects approach each other.

Dependencies:
* T18.G7.01: Implement waypoint-based NPC movement
* T09.G5.02: Use arithmetic expressions with multiple operations


ID: T18.G7.04
Topic: T18 – 3D Worlds & Games
Skill: Implement a physics-based puzzle mechanic
Description: Students combine physics bodies, collision triggers, constraints, and environmental interactions to design a solvable puzzle (e.g., push blocks onto pressure plates, roll a ball through ramps, or chain swinging platforms).

Dependencies:
* T18.G7.02: Design collision response for bouncing or sliding
* T18.G6.09: Add fixed constraints to connect physics bodies


ID: T18.G7.05
Topic: T18 – 3D Worlds & Games
Skill: Script camera transitions for cutscenes
Description: Students choreograph mini-cutscenes by sequencing `set camera target xyz (X) (Y) (Z)` and `set camera distance (D) v-angle (V) h-angle (H) z offset (OFFSET) target xyz (X) (Y) (Z) in (T) seconds` blocks to smoothly move the camera through key positions, creating cinematic introductions, dramatic reveals, or level transitions with timed camera movements.

Dependencies:
* T18.G5.09: Adjust camera distance and angles dynamically
* T10.G5.01: Use a list to store multiple values


ID: T18.G7.06
Topic: T18 – 3D Worlds & Games
Skill: Add hinge constraints with motors
Description: Students use `add hinge constraint between bodies of [OBJECTNAME] from [SPRITENAME v] at point xyz and [OBJECTNAME2] at point xyz named [JOINTNAME]` to create rotating joints for mechanisms like swinging doors or rotating wheels, then configure hinge motors with `set speed (SPEED) for hinge constraint named [NAME]` to create powered articulated mechanisms.

Dependencies:
* T18.G6.09: Add fixed constraints to connect physics bodies


ID: T18.G7.07
Topic: T18 – 3D Worlds & Games
Skill: Control avatar animations with state-based logic
Description: Students use `add avatar [AVATARTYPE v] height (H) as [NAME]` to place a humanoid character, `add animations [ANIMATIONLIST]` to load multiple animation clips from the library, and `start animation [NAME] looping [ISLOOPING v] speed ratio (SPEEDRATIO)` to switch between animations (walk, idle, jump, dance) based on game state using if-else chains, creating a simple animation state machine that syncs character movement with visual animation.

Dependencies:
* T18.G4.08.01: Add and control avatar animations
* T08.G5.01: Use if‑else to handle two cases


## Grade 8

ID: T18.G8.01
Topic: T18 – 3D Worlds & Games
Skill: Load level layouts from list data
Description: Students store level layouts (object types, positions, properties) in lists or nested lists and write code to loop through the data and spawn 3D objects dynamically, enabling multiple levels, difficulty scaling, or player-created content.

Dependencies:
* T18.G5.04.01: Use nested loops to arrange 3D objects in grids
* T10.G6.02: Use 2D lists (lists of lists)


ID: T18.G8.02
Topic: T18 – 3D Worlds & Games
Skill: Use multiple cameras for split-screen or UI views
Description: Students use `set display region bottom (B)% left (L)% width (W)% height (H)% border width (BORDERWIDTH) color [BORDERCOLOR] for camera [NAME]` to divide the screen into multiple viewports, creating split-screen gameplay for local multiplayer or picture-in-picture views such as main gameplay plus minimap, managing which camera renders to each region.

Dependencies:
* T18.G4.03: Create a following camera
* T18.G5.09: Adjust camera distance and angles dynamically


ID: T18.G8.03
Topic: T18 – 3D Worlds & Games
Skill: Analyze and optimize a 3D game for performance
Description: Students profile a sluggish 3D project by observing frame rate and visual glitches, identify bottlenecks (too many physics bodies, complex meshes, excessive particles, unoptimized loops), and refactor by reducing object counts with `remove object named`, using simpler collision shapes, limiting particle capacity, or using GPU-accelerated particles.

Dependencies:
* T18.G8.01: Load level layouts from list data
* T18.G6.07: Trigger advanced visual effects on events


ID: T18.G8.04
Topic: T18 – 3D Worlds & Games
Skill: Analyze trade-offs between visual quality and performance
Description: Students review a completed 3D project and identify at least 3 design choices (physics on/off for objects, texture resolution, particle count, shadow quality, mesh complexity) and explain the trade-off for each: why it was chosen, what was sacrificed, and the impact on frame rate performance. They demonstrate understanding by explaining specific examples from their project (e.g., "I disabled physics for decorative objects to improve frame rate, sacrificing realism but gaining 10+ FPS").

Dependencies:
* T18.G8.03: Analyze and optimize a 3D game for performance
* T18.G7.04: Implement a physics-based puzzle mechanic


ID: T18.G8.05
Topic: T18 – 3D Worlds & Games
Skill: Use car physics for vehicle simulation
Description: Students use `enable car simulation mass (MASS) restitution (RESTITUTION)% friction (BODYFRICTION)% tire friction (FRICTION)% suspension (SUSPENSION) for [NAME]` to convert an object into a physics-based car, then control it with `set car engine force (ENGINEFORCE) brake level (BRAKEFORCE)%` and `steer car to angle (A)` to drive vehicles with realistic wheel physics, suspension, and handling through 3D environments.

Dependencies:
* T18.G7.02: Design collision response for bouncing or sliding
* T18.G7.06: Add hinge constraints with motors
