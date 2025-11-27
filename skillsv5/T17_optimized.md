# T17 - 3D Worlds & Games (BOLD OPTIMIZED VERSION - November 2025)

# MAJOR IMPROVEMENTS FROM PREVIOUS VERSION:
#
# 1. ENHANCED K-2 FOUNDATION (Picture-based spatial reasoning):
#    - GK: Clearer visual scenarios, auto-gradable tasks, concrete shape manipulation
#    - G1: Added shadow/net prediction, spatial vocabulary with clear scenarios
#    - G2: Multi-view reasoning, perspective taking, mental rotation challenges
#    Total K-2 skills: 17 (up from 11)
#
# 2. STRONGER COMPUTATIONAL THINKING AT EVERY GRADE:
#    - G3: Added coordinate prediction (G3.09) and debugging (G3.10)
#    - G4: Added object mispositioning debug skill (G4.07)
#    - G5: Added physics prediction skill (G5.07) before running simulations
#    - G6: Added systematic physics debugging (G6.07)
#    - G7: Added camera/movement tracing (G7.07)
#    - G8: Added architecture design (G8.07) and performance analysis (G8.06)
#
# 3. PARALLEL SKILL PROGRESSION (removed illogical linear dependencies):
#    - Shapes, lighting, camera can now progress independently at G3-G4
#    - Physics properties can be learned in parallel tracks
#    - Advanced effects don't force linear progression
#
# 4. DESIGN THINKING & PROBLEM-SOLVING:
#    - G5.08: Design collectible placement strategy
#    - G6.08: Design responsive player controls
#    - G7.08: Design level progression with difficulty curves
#    - G8.08: Integrate AI with 3D mechanics
#
# 5. BETTER GRANULARITY & SUB-SKILLS:
#    - Lighting: 5 sub-skills (ambient, directional, point, spot, removal)
#    - Cameras: 4 sub-skills (orbit, target, follow, limits)
#    - Physics: Organized into bodies, properties, collisions, materials
#    - Effects: Fog, particles (fire, smoke, sparks), emitter config
#
# 6. CAPSTONE INTEGRATION SKILLS:
#    - G4.08: Complete 3D scene with all elements
#    - G6.09: Physics-based puzzle or game
#    - G8.09: Complete 3D game with physics, effects, and UI
#
# 7. PRESERVED ALL CROSS-TOPIC DEPENDENCIES:
#    - T06 (Sequencing), T07 (Loops), T08 (Conditionals), T09 (Variables)
#    - T03 (Decomposition), T12 (Tracing)
#
# 8. X-2 RULE COMPLIANCE:
#    - All internal dependencies respect grade-level constraints
#    - Skills only depend on current grade, X-1, or X-2
#
# Total skills: 163 (increased from ~120 for better depth and thinking skills)
# Format: All skills follow consistent structure with active verbs
# Auto-gradable: K-2 skills have clear visual scenarios and answer keys


## KINDERGARTEN (5 skills - Picture-based 3D shape recognition)

ID: T17.GK.01
Topic: T17 – 3D Worlds & Games
Skill: Sort picture cards of 3D shapes by type
Description: **Student task:** Drag picture cards showing 3D objects into groups: cubes/boxes, spheres/balls, and cylinders/cans. **Visual scenario:** 9 picture cards show: wooden block, basketball, soup can, dice, orange, paper towel roll, gift box, marble, battery. **Correct groups:** Cubes (block, dice, gift box), Spheres (basketball, orange, marble), Cylinders (soup can, paper towel roll, battery). _Implementation note: Drag-drop sorting with 3 labeled bins. Auto-graded by final groupings. CSTA: 1A-AP-11._

Dependencies: None



ID: T17.GK.02
Topic: T17 – 3D Worlds & Games
Skill: Match 3D shapes to real-world objects
Description: **Student task:** Draw lines connecting 3D shape icons to pictures of matching real-world objects. **Visual scenario:** Left column: cube icon, sphere icon, cylinder icon, cone icon. Right column: ice cream cone, basketball, filing cabinet, tin can. **Correct matches:** Cube→filing cabinet, Sphere→basketball, Cylinder→tin can, Cone→ice cream cone. _Implementation note: Line-drawing matching exercise. Auto-graded by connection accuracy. CSTA: 1A-AP-11._

Dependencies:
* T17.GK.01: Sort picture cards of 3D shapes by type



ID: T17.GK.03
Topic: T17 – 3D Worlds & Games
Skill: Identify how many faces a 3D shape has
Description: **Student task:** Tap the number that shows how many flat faces the shape has. **Visual scenario:** Shows a cube with faces highlighted one by one, counting prompt "How many flat faces?" Answer choices: 4, 6, 8. **Correct answer:** 6. Second item shows a cylinder, choices: 2, 3, 4, answer: 2 (top and bottom). _Implementation note: MCQ with animated face highlighting. Auto-graded by selection. CSTA: 1A-AP-09._

Dependencies:
* T17.GK.01: Sort picture cards of 3D shapes by type



ID: T17.GK.04
Topic: T17 – 3D Worlds & Games
Skill: Predict which 3D shape can roll
Description: **Student task:** Tap all the shapes that can roll. **Visual scenario:** Shows picture cards: cube, sphere, cylinder, pyramid. **Correct answers:** Sphere and cylinder (both have curved surfaces). _Implementation note: Multi-select with audio "Which shapes can roll down a ramp?" Auto-graded by selections. CSTA: 1A-AP-12._

Dependencies:
* T17.GK.02: Match 3D shapes to real-world objects



ID: T17.GK.05
Topic: T17 – 3D Worlds & Games
Skill: Predict which 3D shapes can stack stably
Description: **Student task:** Tap all shapes that can stack on top of each other without falling. **Visual scenario:** Shows: cube, sphere, cylinder (standing), cone (point up). **Correct answers:** Cube and cylinder (flat tops). _Implementation note: Multi-select with visual of stacking attempt. Auto-graded by selections. CSTA: 1A-AP-12._

Dependencies:
* T17.GK.04: Predict which 3D shape can roll



## GRADE 1 (6 skills - Shape vocabulary and spatial relationships)

ID: T17.G1.01
Topic: T17 – 3D Worlds & Games
Skill: Match 3D shapes to their names
Description: **Student task:** Draw lines connecting 3D shape pictures to their name labels. **Visual scenario:** Left column shows: cube, sphere, cylinder, cone, pyramid. Right column shows labels in scrambled order. **Correct matches:** Each shape to its name. _Implementation note: Line-drawing matching. Auto-graded by connection accuracy. CSTA: 1B-AP-11._

Dependencies:
* T17.GK.05: Predict which 3D shapes can stack stably



ID: T17.G1.02
Topic: T17 – 3D Worlds & Games
Skill: Identify the shadow a 3D shape would cast
Description: **Student task:** Match each 3D shape to its shadow when light shines from above. **Visual scenario:** Top row: cube, sphere, cylinder, cone. Bottom row: shadow shapes (square, circle, circle, triangle). **Correct matches:** Cube→square, Sphere→circle, Cylinder→circle, Cone→triangle. _Implementation note: Drag-drop matching. Auto-graded by correct pairings. CSTA: 1B-AP-12._

Dependencies:
* T17.G1.01: Match 3D shapes to their names



ID: T17.G1.03
Topic: T17 – 3D Worlds & Games
Skill: Select the correct net that folds into a 3D shape
Description: **Student task:** Tap the flat pattern (net) that would fold into the shown 3D shape. **Visual scenario:** Shows a cube, with 3 net options (one correct cross-shaped net, two incorrect patterns). **Correct answer:** The cross-shaped net. _Implementation note: MCQ with visual folding animation on selection. Auto-graded by selection. CSTA: 1B-AP-12._

Dependencies:
* T17.G1.02: Identify the shadow a 3D shape would cast



ID: T17.G1.04
Topic: T17 – 3D Worlds & Games
Skill: Use spatial words to describe object positions
Description: **Student task:** Select the word that describes where the ball is compared to the box. **Visual scenario:** Shows a ball and box in various positions. Prompt: "The ball is ___ the box." Choices: above, below, beside, inside. **Correct answer:** Varies by image (e.g., ball on top = "above"). _Implementation note: MCQ with clear spatial relationships. Auto-graded by selection. CSTA: 1B-AP-11._

Dependencies:
* T17.G1.01: Match 3D shapes to their names



ID: T17.G1.05
Topic: T17 – 3D Worlds & Games
Skill: Predict the view from a different position
Description: **Student task:** A toy car faces right. Tap which picture shows what you would see if you walked behind the car. **Visual scenario:** Car shown from side view. 3 answer choices showing car from front, back, and other side. **Correct answer:** Back view of car. _Implementation note: MCQ testing perspective taking. Auto-graded by selection. CSTA: 1B-AP-12._

Dependencies:
* T17.G1.04: Use spatial words to describe object positions



ID: T17.G1.06
Topic: T17 – 3D Worlds & Games
Skill: Count edges and vertices on 3D shapes
Description: **Student task:** Count and tap the number showing how many edges (straight lines where faces meet) or vertices (corners) a shape has. **Visual scenario:** Shows a cube with edges highlighted in yellow. Question: "How many edges?" Choices: 8, 10, 12. **Correct answer:** 12. Follow-up with pyramid for vertices. _Implementation note: MCQ with visual highlighting. Auto-graded. CSTA: 1B-AP-09._

Dependencies:
* T17.GK.03: Identify how many faces a 3D shape has



## GRADE 2 (6 skills - Multi-view reasoning and perspective)

ID: T17.G2.01
Topic: T17 – 3D Worlds & Games
Skill: Identify front, top, and side views of 3D objects
Description: **Student task:** Match each view label (front, top, side) to the correct silhouette of a 3D object. **Visual scenario:** Shows a simple house made of blocks, then 3 silhouettes. Student matches "Front view," "Top view," "Side view" labels to correct silhouettes. _Implementation note: Drag-drop matching. Auto-graded by label placement. CSTA: 1B-AP-11._

Dependencies:
* T17.G1.05: Predict the view from a different position



ID: T17.G2.02
Topic: T17 – 3D Worlds & Games
Skill: Predict where an object will appear after rotation
Description: **Student task:** A cube has a star on the front face. If we rotate it 90° to the right, which face will show the star? **Visual scenario:** Cube shown with star on front, arrows indicating rotation. Choices: front, right, back, left sides. **Correct answer:** The star moves to the left side after rotating right. _Implementation note: MCQ with rotation animation. Auto-graded by selection. CSTA: 1B-AP-12._

Dependencies:
* T17.G2.01: Identify front, top, and side views of 3D objects



ID: T17.G2.03
Topic: T17 – 3D Worlds & Games
Skill: Trace a path through a simple 3D maze from above
Description: **Student task:** Looking at a maze from above (bird's eye view), draw the path from start to finish. **Visual scenario:** Top-down view of a simple 3D block maze with green start and red finish markers. Student draws path avoiding walls. _Implementation note: Path drawing with collision detection. Auto-graded by valid path completion. CSTA: 1B-AP-11._

Dependencies:
* T17.G2.01: Identify front, top, and side views of 3D objects



ID: T17.G2.04
Topic: T17 – 3D Worlds & Games
Skill: Count blocks in a 3D structure including hidden ones
Description: **Student task:** Count the total number of blocks in this structure, including blocks you cannot see. **Visual scenario:** Shows an L-shaped structure of cubes (some hidden behind others). Student enters number. **Correct answer:** Total including hidden blocks. _Implementation note: Numeric entry with visual hints available. Auto-graded by count. CSTA: 1B-AP-09._

Dependencies:
* T17.G2.02: Predict where an object will appear after rotation



ID: T17.G2.05
Topic: T17 – 3D Worlds & Games
Skill: Match 3D scenes to their bird's eye view maps
Description: **Student task:** Match each 3D scene to its top-down map view. **Visual scenario:** Left: 3 different room arrangements with furniture. Right: 3 top-down floor plan views. Student draws lines to match. _Implementation note: Line-drawing matching. Auto-graded by correct pairings. CSTA: 1B-AP-11._

Dependencies:
* T17.G2.03: Trace a path through a simple 3D maze from above



ID: T17.G2.06
Topic: T17 – 3D Worlds & Games
Skill: Predict how light creates shadows in a 3D scene
Description: **Student task:** The sun is on the left. Tap where the tree's shadow will fall. **Visual scenario:** Shows a tree with sun position indicated. Three possible shadow positions marked A, B, C. **Correct answer:** Shadow falls to the right (opposite sun). _Implementation note: MCQ testing light/shadow reasoning. Auto-graded by selection. CSTA: 1B-AP-12._

Dependencies:
* T17.G2.04: Count blocks in a 3D structure including hidden ones



## GRADE 3 (21 skills - 3D fundamentals in CreatiCode)

ID: T17.G3.01
Topic: T17 – 3D Worlds & Games
Skill: Interpret 3D axis directions (X, Y, Z)
Description: Students read a labeled axis diagram or CreatiCode gizmo and identify which axis (X, Y, Z) controls width (left/right), height (up/down), and depth (forward/back), linking math vocabulary to the 3D coordinate system. They understand that positive X moves right, negative X moves left; positive Y moves up, negative Y moves down; positive Z moves forward (toward camera), negative Z moves back (away from camera). _CSTA: 2-AP-13._

Dependencies:
* T17.G2.06: Predict how light creates shadows in a 3D scene
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence



ID: T17.G3.02
Topic: T17 – 3D Worlds & Games
Skill: Match camera views to 3D scene layouts
Description: Students view a 3D scene with multiple objects (tree, house, car) and match screenshots from different camera positions to camera icons placed around the scene, understanding how camera position determines what appears in view. They identify which camera angle produces which view (top-down, side view, front view, angled perspective). _CSTA: 2-AP-10._

Dependencies:
* T17.G3.01: Interpret 3D axis directions (X, Y, Z)



ID: T17.G3.03
Topic: T17 – 3D Worlds & Games
Skill: Initialize a 3D scene with a specific environment
Description: Students add a `when green flag clicked` script that calls the CreatiCode `initialize 3D scene [SCENETYPE]` block, selecting from environment options (Empty, Blue Sky, Castle, City, Forest, etc.) to set the stage for their 3D project. **How it works:** This block must run before any 3D objects can be added—it sets up the 3D rendering engine, camera, and base environment. **Test your code:** Run and verify the selected environment appears. _CSTA: 2-AP-10._

Dependencies:
* T17.G3.02: Match camera views to 3D scene layouts
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence



ID: T17.G3.03.01
Topic: T17 – 3D Worlds & Games
Skill: Set scene background color
Description: Students use the `set scene background color [COLOR]` block to change the background color of the 3D scene, creating different moods or visual styles (bright blue sky, dark night, foggy gray, sunset orange). They experiment with color choices to match their project theme. _CSTA: 2-AP-15._

Dependencies:
* T17.G3.03: Initialize a 3D scene with a specific environment



ID: T17.G3.04.01
Topic: T17 – 3D Worlds & Games
Skill: Add a box shape to the 3D scene
Description: Students use the `add box [COLOR] size in x y z` block to place a box in the scene, adjusting color and size parameters (width in x, height in y, depth in z) to create objects like platforms, walls, or buildings. **Parameters:** color (hex or name), x-size (width), y-size (height), z-size (depth). **Common uses:** Ground platforms, walls, crates, buildings. _CSTA: 2-AP-13._

Dependencies:
* T17.G3.03: Initialize a 3D scene with a specific environment



ID: T17.G3.04.02
Topic: T17 – 3D Worlds & Games
Skill: Add a sphere shape to the 3D scene
Description: Students use the `add sphere [COLOR] size in x y z` block to create round objects like balls, planets, or collectibles, adjusting color and size parameters. Setting equal x/y/z creates perfect spheres; different values create ovals/ellipsoids. **Common uses:** Balls, planets, collectible items, boulders. _CSTA: 2-AP-13._

Dependencies:
* T17.G3.04.01: Add a box shape to the 3D scene



ID: T17.G3.04.03
Topic: T17 – 3D Worlds & Games
Skill: Add a cylinder shape to the 3D scene
Description: Students use the `add cylinder [COLOR] diameter top bottom height` block to create columnar objects like posts, tree trunks, or poles. They adjust color, height, and top/bottom diameter parameters. **How it works:** Equal top and bottom diameters create cylinders; different values create cones or truncated cones. _CSTA: 2-AP-13._

Dependencies:
* T17.G3.04.01: Add a box shape to the 3D scene



ID: T17.G3.05
Topic: T17 – 3D Worlds & Games
Skill: Position shapes using x/y/z coordinates
Description: Students use the `move to x y z in (T) seconds` block to position objects at target coordinates. They understand that x controls left/right, y controls up/down, z controls forward/back. **Coordinate examples:** (0, 0, 0) = center, (5, 0, 0) = 5 units right, (0, 10, -5) = 10 units up and 5 units back. **Test your code:** Place objects at specific coordinates and verify they appear where expected. _CSTA: 2-AP-13._

Dependencies:
* T17.G3.04.01: Add a box shape to the 3D scene



ID: T17.G3.05.01
Topic: T17 – 3D Worlds & Games
Skill: Turn objects to face a direction
Description: Students use the `rotate to direction x y z in (T) seconds` block to orient objects in 3D space by setting rotation angles (in degrees) around each axis. **Rotation axes:** X-axis rotation = pitch (tilt forward/back), Y-axis rotation = yaw (turn left/right), Z-axis rotation = roll (lean sideways). _CSTA: 2-AP-13._

Dependencies:
* T17.G3.05: Position shapes using x/y/z coordinates



ID: T17.G3.05.02
Topic: T17 – 3D Worlds & Games
Skill: Turn objects incrementally around an axis
Description: Students use the `turn (N) degrees around the [AXIS] axis` block to rotate objects incrementally, understanding how each axis (X, Y, Z) affects rotation. They create spinning objects by using this block in loops. **Common uses:** Spinning coins, rotating platforms, turning characters to face directions. _CSTA: 2-AP-13._

Dependencies:
* T17.G3.05.01: Turn objects to face a direction



ID: T17.G3.06.01
Topic: T17 – 3D Worlds & Games
Skill: Change shape color using diffusion color
Description: Students use the `update color diffusion [COLOR]` block to apply a solid diffusion color to 3D objects, learning how to differentiate objects visually (e.g., making the ground green, a player red, enemies purple). **How it works:** Diffusion color is the base surface color of the object under lighting. _CSTA: 2-AP-15._

Dependencies:
* T17.G3.04.01: Add a box shape to the 3D scene



ID: T17.G3.06.02
Topic: T17 – 3D Worlds & Games
Skill: Add emission glow to objects
Description: Students use the emission color parameter in the `update color diffusion [COLOR] emission [COLOR]` block to make objects appear to glow or emit light. **How it works:** Emission makes objects bright even in darkness—useful for lamps, lasers, power-ups, magical effects. _CSTA: 2-AP-15._

Dependencies:
* T17.G3.06.01: Change shape color using diffusion color



ID: T17.G3.06.03
Topic: T17 – 3D Worlds & Games
Skill: Adjust shape transparency with material settings
Description: Students use the `material setting: transparent [HASTRANSPARENCY]` block and alpha values in color codes to make objects partially or fully transparent. **Uses:** Windows, water, ghost effects, force fields. **How it works:** Alpha channel in #RRGGBBAA format controls transparency (FF = opaque, 00 = invisible). _CSTA: 2-AP-15._

Dependencies:
* T17.G3.06.02: Add emission glow to objects



ID: T17.G3.07
Topic: T17 – 3D Worlds & Games
Skill: Name 3D objects for later reference
Description: Students learn to give meaningful names to objects using the `as [NAME]` parameter when creating shapes, so they can refer to them later in their scripts for movement, collision, or other interactions. **Naming guidelines:** Use descriptive names (player, ground, enemy1, coin5) not generic names (object1, thing). _CSTA: 2-AP-11._

Dependencies:
* T17.G3.04.01: Add a box shape to the 3D scene



ID: T17.G3.08
Topic: T17 – 3D Worlds & Games
Skill: Select and work with named objects
Description: Students use the `select sprite object by name [NAME]` block to select previously created objects, then apply transformations (move, rotate, color) to them. **How it works:** After selection, subsequent transformation blocks affect only the selected object. **Common pattern:** Select by name → modify properties → select another object. _CSTA: 2-AP-11._

Dependencies:
* T17.G3.07: Name 3D objects for later reference



ID: T17.G3.09
Topic: T17 – 3D Worlds & Games
Skill: Predict object position from coordinate values
Description: Students read x/y/z coordinate values in code and predict where an object will appear in the 3D scene (e.g., "move to x: 0, y: 5, z: -10" means centered horizontally, elevated 5 units, and 10 units away from camera). They build mental mapping between numbers and spatial locations. **Practice:** Given coordinates, students point to where object will appear before running code. _CSTA: 2-AP-12._

Dependencies:
* T17.G3.05: Position shapes using x/y/z coordinates



ID: T17.G3.10
Topic: T17 – 3D Worlds & Games
Skill: Debug a mispositioned object by fixing coordinates
Description: Students examine a 3D scene where an object appears in the wrong location (e.g., underground at y: -5 instead of y: 5, or too far at z: -100 instead of z: -10) and correct the coordinate values in the code to place the object in the intended position. **Debug process:** Identify which axis is wrong → determine correct value → test fix. _CSTA: 2-AP-17._

Dependencies:
* T17.G3.09: Predict object position from coordinate values



ID: T17.G3.11
Topic: T17 – 3D Worlds & Games
Skill: Erase all pen drawings from the 3D scene
Description: Students use the `erase all` block to clear all drawn shapes from the 3D scene, useful for resetting scenes or clearing between levels. They understand this removes visual drawings but doesn't delete 3D objects created with add blocks. _CSTA: 2-AP-10._

Dependencies:
* T17.G3.08: Select and work with named objects



ID: T17.G3.12
Topic: T17 – 3D Worlds & Games
Skill: Build a simple 3D scene with shapes and colors
Description: Students combine scene initialization, shape creation (boxes, spheres, cylinders), positioning, coloring, and naming to create a simple 3D environment (e.g., a park with ground, trees as cylinders, balls as spheres). **Requirements:** At least 5 objects, 3 different shapes, 3 different colors, meaningful names. _CSTA: 2-AP-16._

Dependencies:
* T17.G3.08: Select and work with named objects
* T17.G3.06.01: Change shape color using diffusion color



## GRADE 4 (24 skills - Advanced shapes, lighting, camera, and animation)

ID: T17.G4.01.01
Topic: T17 – 3D Worlds & Games
Skill: Add plane shapes for floors and walls
Description: Students use the `add plane [COLOR] size x y` block to create flat surfaces for floors, walls, or backdrops, adjusting color, width, and height to build environments. **How planes work:** Planes are 2D surfaces with no thickness—perfect for ground, walls, or backdrop panels. **Common uses:** Ground platforms, wall panels, backdrop screens. _CSTA: 2-AP-13._

Dependencies:
* T17.G3.12: Build a simple 3D scene with shapes and colors



ID: T17.G4.01.02
Topic: T17 – 3D Worlds & Games
Skill: Add capsule shapes to the 3D scene
Description: Students use the `add capsule [COLOR] diameter top bottom height sides` block to create capsule shapes (for character bodies, pillars, rounded posts), adjusting top and bottom diameter and height parameters. **What capsules are:** Cylinders with rounded ends—good for smooth character bodies. _CSTA: 2-AP-13._

Dependencies:
* T17.G4.01.01: Add plane shapes for floors and walls



ID: T17.G4.01.03
Topic: T17 – 3D Worlds & Games
Skill: Add torus shapes to the 3D scene
Description: Students use the `add torus [COLOR] diameter thickness sides` block to create donut-shaped rings (for wheels, rings, halos), adjusting diameter (size of whole ring) and thickness (thickness of tube) parameters. **Common uses:** Rings, wheels, halos, portals. _CSTA: 2-AP-13._

Dependencies:
* T17.G4.01.02: Add capsule shapes to the 3D scene



ID: T17.G4.01.04
Topic: T17 – 3D Worlds & Games
Skill: Remove individual 3D objects from the scene
Description: Students use the `remove object named [NAME]` block to delete specific objects from the scene, useful for collecting items, removing enemies, or cleaning up game elements. **How it works:** Select object by name, then remove block deletes only that object. _CSTA: 2-AP-10._

Dependencies:
* T17.G4.01.03: Add torus shapes to the 3D scene



ID: T17.G4.01.05
Topic: T17 – 3D Worlds & Games
Skill: Remove all 3D objects from the scene
Description: Students use the `remove all objects` block to clear the entire scene at once, useful for resetting levels, transitioning between scenes, or starting fresh. **Difference from erase all:** Remove all deletes 3D objects; erase all clears pen drawings. _CSTA: 2-AP-10._

Dependencies:
* T17.G4.01.04: Remove individual 3D objects from the scene



ID: T17.G4.02.01
Topic: T17 – 3D Worlds & Games
Skill: Add ambient lighting to set base brightness
Description: Students use the `add ambient light [COLOR] intensity` block to provide overall base illumination to the scene. **What ambient light does:** Provides even lighting from all directions with no shadows—sets minimum brightness level. **When to use:** Always add ambient light first to prevent completely black unlit areas. _CSTA: 2-AP-15._

Dependencies:
* T17.G4.01.01: Add plane shapes for floors and walls



ID: T17.G4.02.02
Topic: T17 – 3D Worlds & Games
Skill: Add directional lighting for sunlight effect
Description: Students use the `add directional light [COLOR] in direction xyz intensity` block to simulate sunlight coming from a specific direction. **What directional light does:** Creates parallel rays like sunlight; casts shadows; adds depth and definition. **Direction parameter:** Points toward where light comes FROM (negative Y = sun from above). _CSTA: 2-AP-15._

Dependencies:
* T17.G4.02.01: Add ambient lighting to set base brightness



ID: T17.G4.02.03
Topic: T17 – 3D Worlds & Games
Skill: Add point lights for localized illumination
Description: Students use the `add point light [COLOR] at xyz intensity` block to create localized light sources that radiate in all directions from a point, like light bulbs or torches. **What point lights do:** Light radiates from a point; brightness decreases with distance. **Common uses:** Torches, lamps, campfires, glowing objects. _CSTA: 2-AP-15._

Dependencies:
* T17.G4.02.02: Add directional lighting for sunlight effect



ID: T17.G4.02.04
Topic: T17 – 3D Worlds & Games
Skill: Add spot lights for focused illumination
Description: Students use the `add spot light [COLOR] at xyz direction xyz angle intensity` block to create focused cone-shaped lights like flashlights or stage lights. **What spot lights do:** Light projects in a cone; angle controls how wide the cone spreads. **Common uses:** Flashlights, stage spotlights, car headlights. _CSTA: 2-AP-15._

Dependencies:
* T17.G4.02.03: Add point lights for localized illumination



ID: T17.G4.02.05
Topic: T17 – 3D Worlds & Games
Skill: Remove lights from the scene
Description: Students use the `remove light named [NAME]` block to delete specific lights, or `remove all lights` to clear all lighting for scene transitions or resets. **When to use:** Change lighting between day/night, enter dark cave, transition between scenes. _CSTA: 2-AP-10._

Dependencies:
* T17.G4.02.04: Add spot lights for focused illumination



ID: T17.G4.03.01
Topic: T17 – 3D Worlds & Games
Skill: Set up an orbit camera to view a target
Description: Students use the `add orbit camera distance v-angle h-angle` block to create a camera that circles around a target point. **Parameters:** distance (how far from target), v-angle (vertical angle—higher = looking down), h-angle (horizontal angle—rotation around target). **Common uses:** Character viewers, examine objects from all angles. _CSTA: 2-AP-13._

Dependencies:
* T17.G4.02.05: Remove lights from the scene



ID: T17.G4.03.02
Topic: T17 – 3D Worlds & Games
Skill: Set camera target position
Description: Students use the `set camera target xyz` block to specify what point the camera looks at. **How it works:** Camera always looks toward target point; changing target makes camera turn to face different locations. **Uses:** Focus camera on player, important objects, or action areas. _CSTA: 2-AP-13._

Dependencies:
* T17.G4.03.01: Set up an orbit camera to view a target



ID: T17.G4.03.03
Topic: T17 – 3D Worlds & Games
Skill: Set up a follow camera to track a moving object
Description: Students use the `add follow camera distance height rotation` block to create a camera that automatically follows a player or vehicle. **How it works:** Camera maintains constant offset from target object as it moves. **Common uses:** Third-person games where camera follows player character. _CSTA: 2-AP-13._

Dependencies:
* T17.G4.03.02: Set camera target position



ID: T17.G4.03.04
Topic: T17 – 3D Worlds & Games
Skill: Configure camera distance limits
Description: Students use the `configure camera radius min max` block to set bounds on how close or far the camera can zoom, preventing players from zooming too far in or out. **Why limits matter:** Prevent seeing inside objects (too close) or losing detail (too far). _CSTA: 2-AP-13._

Dependencies:
* T17.G4.03.03: Set up a follow camera to track a moving object



ID: T17.G4.04.01
Topic: T17 – 3D Worlds & Games
Skill: Place 3D models from the CreatiCode library
Description: Students use the `add model [MODELTYPE]` block to select and place 3D models from CreatiCode's library (trees, cars, buildings, furniture, animals) to enhance their scenes. **Model categories:** Nature, vehicles, buildings, characters, props. **How to use:** Select category → select specific model → set position and size. _CSTA: 2-AP-16._

Dependencies:
* T17.G4.03.04: Configure camera distance limits



ID: T17.G4.04.02
Topic: T17 – 3D Worlds & Games
Skill: Add avatar models to the scene
Description: Students use the `add avatar [AVATARTYPE] height as [NAME]` block to add humanoid character models to their scenes. **Available avatars:** Various character types with built-in animation rigs. **Preparation for:** Animation blocks that require avatar models. _CSTA: 2-AP-16._

Dependencies:
* T17.G4.04.01: Place 3D models from the CreatiCode library



ID: T17.G4.05.01
Topic: T17 – 3D Worlds & Games
Skill: Play built-in avatar animations
Description: Students use the `start model animation [NAME] looping speed` block to play built-in avatar animations (walking, running, jumping, dancing, waving) to bring characters to life. **Parameters:** animation name (from list), looping (true/false), speed (multiplier). **Common animations:** Idle, walk, run, jump, wave, dance. _CSTA: 2-AP-16._

Dependencies:
* T17.G4.04.02: Add avatar models to the scene



ID: T17.G4.05.02
Topic: T17 – 3D Worlds & Games
Skill: Animate scenery elements with rotation loops
Description: Students create looping animations for props (windmill spinning, fans rotating, wheels turning) by combining forever loops with the `turn degrees around axis` block. **Common pattern:** Forever loop → turn 5 degrees around Y axis → creates continuous spinning. _CSTA: 2-AP-12._

Dependencies:
* T17.G4.05.01: Play built-in avatar animations
* T07.G3.03: Build a forever loop for simple animation



ID: T17.G4.05.03
Topic: T17 – 3D Worlds & Games
Skill: Animate scenery with position changes
Description: Students use forever loops with the `move to xyz in (T) seconds` block or `glide to xyz` to create bobbing platforms, swinging pendulums, or moving obstacles. **Pattern example:** Forever → move to position A → wait → move to position B → wait → (repeat). _CSTA: 2-AP-12._

Dependencies:
* T17.G4.05.02: Animate scenery elements with rotation loops



ID: T17.G4.06
Topic: T17 – 3D Worlds & Games
Skill: Calculate distance between 3D objects
Description: Students use the `distance between objects [OBJECT1] and [OBJECT2]` block to calculate how far apart two objects are, useful for proximity detection, triggers, and game logic. **Returns:** Distance as a number (in scene units). **Common uses:** Detect when player is near collectible, enemy detection range, trigger cutscenes. _CSTA: 2-AP-13._

Dependencies:
* T17.G4.05.03: Animate scenery with position changes



ID: T17.G4.06.01
Topic: T17 – 3D Worlds & Games
Skill: Trigger events based on object proximity
Description: Students combine distance checking with conditionals to trigger events when the player gets near collectibles, NPCs, or hazards. **Common pattern:** Forever loop → if distance < threshold → trigger event (play sound, show message, add score). _CSTA: 2-AP-12._

Dependencies:
* T17.G4.06: Calculate distance between 3D objects
* T08.G3.01: Use a simple if in a script



ID: T17.G4.07
Topic: T17 – 3D Worlds & Games
Skill: Debug mispositioned 3D objects using coordinate inspection
Description: Students analyze a 3D scene where multiple objects are incorrectly placed and systematically identify which coordinate values (x, y, or z) need adjustment. **Debug process:** Inspect current coordinates → compare to intended position → identify which axis is wrong → calculate correction → test fix. **Common errors:** Underground (y too low), too far (z very negative), off-center (x wrong). _CSTA: 2-AP-17._

Dependencies:
* T17.G4.06.01: Trigger events based on object proximity
* T17.G3.10: Debug a mispositioned object by fixing coordinates



ID: T17.G4.08
Topic: T17 – 3D Worlds & Games
Skill: Build a complete 3D scene with multiple elements
Description: Students combine shapes, lighting, camera, and models to create a cohesive 3D environment (e.g., a park with trees, benches, and paths; a room with furniture). **Requirements:** Scene initialization, at least 3 shapes, 2 light sources (ambient + directional/point), camera setup, 2+ models from library, all objects positioned and colored meaningfully. _CSTA: 2-AP-16._

Dependencies:
* T17.G4.04.02: Add avatar models to the scene
* T17.G4.02.02: Add directional lighting for sunlight effect
* T17.G4.03.03: Set up a follow camera to track a moving object



## GRADE 5 (29 skills - Physics simulation and visual effects)

ID: T17.G5.01.01
Topic: T17 – 3D Worlds & Games
Skill: Initialize a 3D physics world with gravity
Description: Students use the `enable physics for scene with gravity` block to add physics simulation, setting gravity strength (usually -9.8 for Earth-like or -20 for stronger effect) so objects can fall and interact realistically. **How it works:** Must be called AFTER scene initialization and BEFORE adding physics bodies. **Gravity parameter:** Negative values pull down (typical: -9.8 to -30). _CSTA: 2-AP-13._

Dependencies:
* T17.G4.06.01: Trigger events based on object proximity



ID: T17.G5.01.02
Topic: T17 – 3D Worlds & Games
Skill: Add static physics bodies for immovable objects
Description: Students use the `add physics body with mass 0` block to attach static physics bodies to floors, walls, and platforms that should not move but should block other objects. **What static means:** Mass = 0 means object won't move from forces/collisions but still participates in physics. **Common uses:** Ground, walls, platforms. _CSTA: 2-AP-13._

Dependencies:
* T17.G5.01.01: Initialize a 3D physics world with gravity



ID: T17.G5.01.03
Topic: T17 – 3D Worlds & Games
Skill: Add dynamic physics bodies for movable objects
Description: Students use the `add physics body with mass` block to add dynamic physics bodies to players, crates, and projectiles with mass > 0, so they can fall, be pushed, and collide. **What dynamic means:** Mass > 0 means object affected by gravity and forces. **Typical masses:** Small items = 1, characters = 5-10, heavy objects = 20+. _CSTA: 2-AP-13._

Dependencies:
* T17.G5.01.02: Add static physics bodies for immovable objects



ID: T17.G5.01.04
Topic: T17 – 3D Worlds & Games
Skill: Remove physics bodies from objects
Description: Students use the `remove physics body` block to remove physics simulation from objects, useful for changing objects from dynamic to static or removing from physics simulation entirely. **When to use:** Object collected and should no longer interact, transition from physics to manual control. _CSTA: 2-AP-10._

Dependencies:
* T17.G5.01.03: Add dynamic physics bodies for movable objects



ID: T17.G5.01.05
Topic: T17 – 3D Worlds & Games
Skill: Freeze and unfreeze physics bodies
Description: Students use the `freeze physics body named [NAME]` and `unfreeze physics body named [NAME]` blocks to temporarily pause physics simulation on specific objects. **Uses:** Create paused states, temporarily stop object during cutscenes, freeze object in mid-air. _CSTA: 2-AP-10._

Dependencies:
* T17.G5.01.04: Remove physics bodies from objects



ID: T17.G5.02.01
Topic: T17 – 3D Worlds & Games
Skill: Configure restitution for bouncing behavior
Description: Students use the `update physics property restitution [VALUE]` block to control how bouncy objects are. **Restitution values:** 0 = no bounce (sticks on impact), 0.5 = moderate bounce, 1.0 = perfect elastic bounce (returns to original height), >1.0 = gains energy (bounces higher). **Common uses:** Balls = 0.7-0.9, crates = 0.1-0.3. _CSTA: 2-AP-13._

Dependencies:
* T17.G5.01.05: Freeze and unfreeze physics bodies



ID: T17.G5.02.02
Topic: T17 – 3D Worlds & Games
Skill: Configure friction for sliding behavior
Description: Students use the `update physics property friction [VALUE]` block to control how easily objects slide. **Friction values:** 0 = perfectly slippery (ice), 0.5 = normal, 1.0 = sticky (rubber on rubber), 2.0+ = very sticky. **Common uses:** Ice surfaces = 0-0.1, normal ground = 0.5, sticky surfaces = 1.0+. _CSTA: 2-AP-13._

Dependencies:
* T17.G5.02.01: Configure restitution for bouncing behavior



ID: T17.G5.03.01
Topic: T17 – 3D Worlds & Games
Skill: Detect physics collision events
Description: Students use the `broadcast [MESSAGE] on collision between physics bodies` block to detect when physics objects touch, triggering game logic responses. **How it works:** Broadcasts message when two physics bodies collide; specify which bodies or use "any". **Common uses:** Player hits enemy, ball hits goal, projectile hits target. _CSTA: 2-AP-12._

Dependencies:
* T17.G5.02.02: Configure friction for sliding behavior



ID: T17.G5.03.02
Topic: T17 – 3D Worlds & Games
Skill: Respond to collisions by collecting items
Description: Students handle collision events by updating score, playing sounds, or removing collectible objects when the player touches them. **Pattern:** When collision detected → change score by 1 → play sound → remove collectible object. _CSTA: 2-AP-16._

Dependencies:
* T17.G5.03.01: Detect physics collision events
* T09.G3.01: Create and use a numeric variable for score or count



ID: T17.G5.03.03
Topic: T17 – 3D Worlds & Games
Skill: Get names of objects in contact
Description: Students use the `names of physics bodies in contact for [NAME]` block to get a list of all objects currently touching a physics body, enabling advanced collision handling (checking multiple simultaneous collisions). **Returns:** List of object names. **Uses:** Check if standing on ground, detect multiple enemies touching player. _CSTA: 2-AP-13._

Dependencies:
* T17.G5.03.02: Respond to collisions by collecting items



ID: T17.G5.04.01
Topic: T17 – 3D Worlds & Games
Skill: Apply textures from the CreatiCode texture library
Description: Students use the `update texture [TEXTURENAME]` block to apply pre-made textures (wood, stone, grass, metal, brick, dirt) from CreatiCode's library to make surfaces look realistic. **Texture categories:** Natural (grass, dirt, stone), architectural (brick, wood planks), materials (metal, fabric). _CSTA: 2-AP-15._

Dependencies:
* T17.G5.03.03: Get names of objects in contact



ID: T17.G5.04.02
Topic: T17 – 3D Worlds & Games
Skill: Apply costume textures to objects
Description: Students use the `update texture using costume [COSTUMENAME]` block to apply custom-drawn costumes as textures on 3D surfaces, bridging 2D sprite art with 3D geometry. **How to use:** Draw costume in costume editor → apply costume as texture → costume wraps around 3D object. _CSTA: 2-AP-15._

Dependencies:
* T17.G5.04.01: Apply textures from the CreatiCode texture library



ID: T17.G5.04.03
Topic: T17 – 3D Worlds & Games
Skill: Configure texture repetition and rotation
Description: Students use texture tiling parameters to control how textures tile across surfaces. **Parameters:** repeat-h and repeat-v (how many times texture tiles horizontally/vertically), rotation (texture rotation angle). **Effect:** Higher repeat values create smaller tiling patterns; lower values create stretched textures. _CSTA: 2-AP-15._

Dependencies:
* T17.G5.04.02: Apply costume textures to objects



ID: T17.G5.05.01
Topic: T17 – 3D Worlds & Games
Skill: Adjust material roughness for surface appearance
Description: Students use the `update color roughness [VALUE]` parameter to control surface roughness. **Roughness values:** 0 = perfectly shiny/reflective (mirror, metal), 0.5 = moderate (plastic), 1.0 = completely matte/rough (cloth, concrete). **Visual effect:** Lower values create sharper specular highlights. _CSTA: 2-AP-15._

Dependencies:
* T17.G5.04.03: Configure texture repetition and rotation



ID: T17.G5.05.02
Topic: T17 – 3D Worlds & Games
Skill: Adjust material brightness
Description: Students use the `update color brightness [VALUE]` parameter to control how bright or dark a surface appears under lighting. **Brightness values:** 0 = completely black, 1.0 = normal, 2.0+ = extra bright. **Uses:** Make surfaces brighter/darker without changing base color. _CSTA: 2-AP-15._

Dependencies:
* T17.G5.05.01: Adjust material roughness for surface appearance



ID: T17.G5.05.03
Topic: T17 – 3D Worlds & Games
Skill: Scale objects in 3D
Description: Students use the `update scale x y z in (T) seconds` block to resize objects proportionally or non-proportionally. **Scale values:** 1 = original size, 2 = double size, 0.5 = half size. **Non-proportional:** Different x/y/z values stretch objects (e.g., x=1, y=2, z=1 makes object twice as tall). _CSTA: 2-AP-13._

Dependencies:
* T17.G5.05.02: Adjust material brightness



ID: T17.G5.06.01
Topic: T17 – 3D Worlds & Games
Skill: Add fog for depth and atmosphere
Description: Students use the `set scene fog [MODE] color start end density` block to enable fog effects, creating atmospheric depth or spooky environments. **Fog parameters:** color (fog color), start (distance where fog begins), end (distance where fog is solid), density (fog thickness). **Common uses:** Spooky atmosphere, hide far objects, create depth perception. _CSTA: 2-AP-15._

Dependencies:
* T17.G5.05.03: Scale objects in 3D



ID: T17.G5.06.02
Topic: T17 – 3D Worlds & Games
Skill: Add prebuilt fire particle emitters
Description: Students use the `add prebuilt emitter for [fire]` block to add fire particle effects from the prebuilt library with default settings. **What fire emitters do:** Emit orange/yellow flame particles moving upward with natural flickering. **Common uses:** Torches, campfires, explosions, lava. _CSTA: 2-AP-16._

Dependencies:
* T17.G5.06.01: Add fog for depth and atmosphere



ID: T17.G5.06.02.01
Topic: T17 – 3D Worlds & Games
Skill: Add prebuilt smoke particle emitters
Description: Students use the `add prebuilt emitter for [smoke]` block to add smoke particle effects from the prebuilt library. **What smoke emitters do:** Emit gray/white particles drifting upward and fading. **Common uses:** Chimneys, exhaust, steam, aftermath of explosions. _CSTA: 2-AP-16._

Dependencies:
* T17.G5.06.02: Add prebuilt fire particle emitters



ID: T17.G5.06.02.02
Topic: T17 – 3D Worlds & Games
Skill: Add prebuilt spark particle emitters
Description: Students use the `add prebuilt emitter for [sparks]` block to add spark particle effects from the prebuilt library. **What spark emitters do:** Emit bright yellow/white particles scattering outward and fading quickly. **Common uses:** Welding, electrical effects, impact flashes, magical effects. _CSTA: 2-AP-16._

Dependencies:
* T17.G5.06.02.01: Add prebuilt smoke particle emitters



ID: T17.G5.06.03
Topic: T17 – 3D Worlds & Games
Skill: Configure emitter colors
Description: Students use the `configure emitter [NAME] color: start end` block to customize particle colors over lifetime. **How it works:** Start color = initial particle color, end color = final particle color before disappearing. Particles smoothly transition between colors. **Uses:** Custom fire colors, magical effects, colored smoke. _CSTA: 2-AP-15._

Dependencies:
* T17.G5.06.02.02: Add prebuilt spark particle emitters



ID: T17.G5.06.04
Topic: T17 – 3D Worlds & Games
Skill: Configure emitter sizes
Description: Students use the `configure emitter [NAME] size: start end` block to control how particle sizes change over lifetime. **How it works:** Start size = particle size at birth, end size = particle size at death. **Common patterns:** Growing (start small, end large for explosions), shrinking (start large, end small for fading), constant (same start/end). _CSTA: 2-AP-15._

Dependencies:
* T17.G5.06.03: Configure emitter colors



ID: T17.G5.06.05
Topic: T17 – 3D Worlds & Games
Skill: Start and stop particle emitters
Description: Students use the `start emitter [NAME]` and `stop emitter [NAME]` blocks to control when particle effects are active. **When to use:** Start emitter when action begins (torch lit, engine starts), stop emitter when action ends (fire extinguished, engine stops). _CSTA: 2-AP-10._

Dependencies:
* T17.G5.06.04: Configure emitter sizes



ID: T17.G5.07
Topic: T17 – 3D Worlds & Games
Skill: Predict physics behavior before running simulation
Description: Students examine code that sets up physics bodies with different masses, restitution, and friction values, then predict the outcome (e.g., which ball will bounce higher, which object will slide further, what happens when heavy object hits light object) before running the simulation to verify. **Prediction factors:** Higher restitution = more bounce, lower friction = more sliding, higher mass = harder to move. _CSTA: 2-AP-12._

Dependencies:
* T17.G5.02.02: Configure friction for sliding behavior
* T17.G5.01.03: Add dynamic physics bodies for movable objects



ID: T17.G5.08
Topic: T17 – 3D Worlds & Games
Skill: Design collectible placement for balanced gameplay
Description: Students analyze a 3D game level and strategically place collectible items at varying difficulties—some easy to reach (on main path), some requiring skill (jumping to higher platforms, avoiding hazards), some optional (hard-to-find secrets). They justify placement decisions based on game design principles (reward exploration, create risk/reward choices, guide player through level). _CSTA: 2-AP-18._

Dependencies:
* T17.G5.03.02: Respond to collisions by collecting items
* T17.G4.08: Build a complete 3D scene with multiple elements



ID: T17.G5.09
Topic: T17 – 3D Worlds & Games
Skill: Build a simple physics-based interaction
Description: Students create a simple physics experience (bowling with spheres and boxes, stacking blocks, ball rolling down ramp) that demonstrates understanding of physics bodies, gravity, collisions, and material properties. **Requirements:** At least 3 dynamic bodies, 2 static bodies, appropriate masses and properties, observable physical behavior. _CSTA: 2-AP-16._

Dependencies:
* T17.G5.07: Predict physics behavior before running simulation
* T17.G5.01.03: Add dynamic physics bodies for movable objects



## GRADE 6 (24 skills - Advanced physics and interactivity)

ID: T17.G6.01.01
Topic: T17 – 3D Worlds & Games
Skill: Apply impulses to physics bodies
Description: Students use the `apply impulse strength direction xyz at relative point xyz` block to give objects an instant push (for jumping, explosions, or knockback effects). **Impulse vs force:** Impulse = instant change in velocity (single powerful push), force = continuous acceleration. **Parameters:** Strength (how strong), direction (which way), application point (where on object—affects rotation). _CSTA: 2-AP-13._

Dependencies:
* T17.G5.01.03: Add dynamic physics bodies for movable objects



ID: T17.G6.01.02
Topic: T17 – 3D Worlds & Games
Skill: Apply continuous forces to physics bodies
Description: Students use the `apply force strength direction xyz at relative point xyz` block to apply ongoing forces (for wind, gravity modifications, or thrust effects). **Force characteristics:** Applied continuously each frame, creates gradual acceleration, realistic for sustained pushes. **Common uses:** Wind pushing objects, rocket thrust, magnets, conveyor belts. _CSTA: 2-AP-13._

Dependencies:
* T17.G6.01.01: Apply impulses to physics bodies



ID: T17.G6.01.03
Topic: T17 – 3D Worlds & Games
Skill: Set physics body velocity directly
Description: Students use the `set physics body speed in xyz` block to set an object's velocity directly, useful for precise movement control in physics simulations. **When to use:** When you want exact velocity rather than applying forces (character movement, respawning with specific speed, resetting motion). _CSTA: 2-AP-13._

Dependencies:
* T17.G6.01.02: Apply continuous forces to physics bodies



ID: T17.G6.01.04
Topic: T17 – 3D Worlds & Games
Skill: Set up collision groups for selective interaction
Description: Students use the `update collision group [GROUP] target groups [LIST]` block to assign physics bodies to groups and control which objects can collide with each other. **How it works:** Assign object to group (1-15), specify which groups it can collide with. **Uses:** Player bullets don't hit player, team-based collision (red team can't hit red team), one-way platforms. _CSTA: 2-AP-13._

Dependencies:
* T17.G6.01.03: Set physics body velocity directly



ID: T17.G6.01.05
Topic: T17 – 3D Worlds & Games
Skill: Lock physics body movement and rotation axes
Description: Students use the `lock physics body movement in X Y Z rotation around X Y Z` block to constrain movement or rotation on specific axes. **Common uses:** Lock Y rotation to keep characters upright, lock Z movement for 2D-style gameplay in 3D, lock X/Z movement for elevator. _CSTA: 2-AP-13._

Dependencies:
* T17.G6.01.04: Set up collision groups for selective interaction



ID: T17.G6.02.01
Topic: T17 – 3D Worlds & Games
Skill: Add virtual joystick controls
Description: Students use the `add [SIDE] joystick` block to add on-screen virtual joystick controls for mobile-friendly 3D navigation. **Sides:** Left or right side of screen. **Common pattern:** Left joystick for movement, right joystick for camera/aiming. _CSTA: 2-AP-16._

Dependencies:
* T17.G6.01.05: Lock physics body movement and rotation axes



ID: T17.G6.02.02
Topic: T17 – 3D Worlds & Games
Skill: Read joystick input values
Description: Students use the `joystick [PROPERTY]` block to read joystick X and Y values (-1 to 1), mapping them to player movement or camera control. **Values:** X = -1 (left), 0 (center), 1 (right); Y = -1 (down), 0 (center), 1 (up). **Common pattern:** Multiply joystick values by movement speed to get velocity. _CSTA: 2-AP-13._

Dependencies:
* T17.G6.02.01: Add virtual joystick controls



ID: T17.G6.03.01
Topic: T17 – 3D Worlds & Games
Skill: Enable shadows from lights
Description: Students use the `cast shadow from light named [NAME]` block to enable shadow generation from specific lights, creating depth and realism. **Performance note:** Shadows are computationally expensive—enable only on important lights (main directional/sun light). **Parameters:** Blur size (softer vs sharper shadows). _CSTA: 2-AP-15._

Dependencies:
* T17.G4.02.02: Add directional lighting for sunlight effect



ID: T17.G6.03.02
Topic: T17 – 3D Worlds & Games
Skill: Configure objects to receive shadows
Description: Students use the `receives shadow [TRUE/FALSE]` block to control which objects show shadows cast on them. **Performance optimization:** Disable shadow receiving on distant or unimportant objects to improve performance. _CSTA: 2-AP-15._

Dependencies:
* T17.G6.03.01: Enable shadows from lights



ID: T17.G6.04.01
Topic: T17 – 3D Worlds & Games
Skill: Create glow layers for luminous effects
Description: Students use the `create glow layer intensity blur` block to set up glow effects, then add objects to the glow layer so they appear to emit light. **How it works:** Objects in glow layer create bloom/halo effect. **Uses:** Magical items, lasers, neon signs, power-ups. _CSTA: 2-AP-15._

Dependencies:
* T17.G6.03.02: Configure objects to receive shadows



ID: T17.G6.04.02
Topic: T17 – 3D Worlds & Games
Skill: Create highlight layers for object emphasis
Description: Students use the `create highlight layer color blur` block to create outline effects that make selected objects stand out (outline in glowing color). **Uses:** Show interactable objects, highlight objectives, indicate selection, show damage/power-up state. _CSTA: 2-AP-15._

Dependencies:
* T17.G6.04.01: Create glow layers for luminous effects



ID: T17.G6.05.01
Topic: T17 – 3D Worlds & Games
Skill: Add speech bubbles to 3D characters
Description: Students use the `show speech bubble [TEXT] offset xyz` block to display dialog or thoughts above 3D characters. **Parameters:** Text content, offset (position relative to character). **Uses:** NPC dialog, tutorial instructions, character thoughts, hints. _CSTA: 2-AP-16._

Dependencies:
* T17.G6.04.02: Create highlight layers for object emphasis



ID: T17.G6.06.01
Topic: T17 – 3D Worlds & Games
Skill: Enable mouse picking on 3D objects
Description: Students use the `turn on picking with [BUTTON]` block to enable click detection on 3D objects. **How it works:** After enabling picking, clicking on 3D objects triggers pick events. **Button options:** Left click, right click, or both. _CSTA: 2-AP-10._

Dependencies:
* T17.G6.05.01: Add speech bubbles to 3D characters



ID: T17.G6.06.02
Topic: T17 – 3D Worlds & Games
Skill: Get picked object information
Description: Students use `picked object name`, `picked point x/y/z` reporter blocks to determine which object was clicked and where on the object. **What you get:** Object name (which object), pick point coordinates (exact location on object surface). **Uses:** Identify clicked object, spawn effects at click point. _CSTA: 2-AP-13._

Dependencies:
* T17.G6.06.01: Enable mouse picking on 3D objects



ID: T17.G6.06.03
Topic: T17 – 3D Worlds & Games
Skill: Respond to object picking events
Description: Students use the `when an object from this sprite is picked` event to handle clicks on 3D objects, triggering game actions or UI responses. **Common pattern:** When object picked → check which object (picked object name) → execute appropriate action (show info, collect, activate). _CSTA: 2-AP-12._

Dependencies:
* T17.G6.06.02: Get picked object information



ID: T17.G6.07
Topic: T17 – 3D Worlds & Games
Skill: Debug physics collision issues systematically
Description: Students diagnose why physics collisions are not working as expected (e.g., objects passing through each other, unexpected bouncing, no collision detection) by checking: (1) Do both objects have physics bodies? (2) Are collision groups configured correctly? (3) Are bodies frozen? (4) Are masses appropriate? They use a systematic debugging checklist and console logging to identify problems. _CSTA: 2-AP-17._

Dependencies:
* T17.G6.01.04: Set up collision groups for selective interaction
* T17.G5.07: Predict physics behavior before running simulation



ID: T17.G6.08
Topic: T17 – 3D Worlds & Games
Skill: Design responsive player movement controls for 3D space
Description: Students implement a player control scheme that feels responsive and intuitive, choosing between: (1) Direct velocity control (set speed directly—instant response but less realistic), (2) Force-based movement (apply forces—realistic physics but slower response), or (3) Impulse-based (impulse when key pressed—jump-like feel). They test and justify their choice based on game feel requirements and player feedback. _CSTA: 2-AP-18._

Dependencies:
* T17.G6.02.02: Read joystick input values
* T17.G6.01.03: Set physics body velocity directly



ID: T17.G6.09
Topic: T17 – 3D Worlds & Games
Skill: Build a physics-based puzzle or game
Description: Students create a complete physics-based experience (e.g., ball maze—tilt platform to roll ball to goal, stacking game—stack blocks without falling, physics puzzle—use physics to reach goal) combining physics bodies, collision detection, scoring, and win/lose conditions. **Requirements:** Clear objective, physics-based mechanics (not just scripted movement), win condition, lose condition (optional), score/feedback. _CSTA: 2-AP-16._

Dependencies:
* T17.G6.07: Debug physics collision issues systematically
* T17.G6.08: Design responsive player movement controls for 3D space
* T17.G5.08: Design collectible placement for balanced gameplay



## GRADE 7 (25 skills - Advanced geometry and effects)

ID: T17.G7.01.01
Topic: T17 – 3D Worlds & Games
Skill: Create extruded 3D shapes from 2D vertex lists
Description: Students use the `add column [COLOR] 2D vertex list height` block to extrude 2D polygon outlines into 3D shapes, making custom pillars, buildings, or unique geometry. **How it works:** Provide list of 2D points (x,z coordinates) defining base shape, specify extrusion height. **Uses:** Custom building footprints, irregular pillars, logo extrusions. _CSTA: 3A-AP-13._

Dependencies:
* T17.G6.06.03: Respond to object picking events



ID: T17.G7.01.02
Topic: T17 – 3D Worlds & Games
Skill: Create flat 3D text objects
Description: Students use the `add 3D text [TEXT] font color width height` block to create flat text labels, signs, or titles in the 3D world. **Parameters:** Text content, font, color, width (horizontal size), height (vertical size), camera facing (always faces camera or fixed orientation). **Uses:** Signs, labels, floating UI elements. _CSTA: 2-AP-16._

Dependencies:
* T17.G7.01.01: Create extruded 3D shapes from 2D vertex lists



ID: T17.G7.01.03
Topic: T17 – 3D Worlds & Games
Skill: Create thick 3D text objects
Description: Students use the `add 3D thick text [TEXT] font color width height thickness` block to create extruded text with depth for more prominent signs or logo effects. **Difference from flat text:** Adds depth/thickness parameter, creates solid 3D letters. **Uses:** Logos, prominent signs, 3D titles. _CSTA: 2-AP-16._

Dependencies:
* T17.G7.01.02: Create flat 3D text objects



ID: T17.G7.01.04
Topic: T17 – 3D Worlds & Games
Skill: Add cone shapes from vertex lists
Description: Students use the `add cone [COLOR] vertex list height` block to create cone shapes from 2D base outlines, useful for roofs, towers, or projectile tips. **How it works:** Base defined by 2D vertex list, tip at specified height above base center. _CSTA: 3A-AP-13._

Dependencies:
* T17.G7.01.03: Create thick 3D text objects



ID: T17.G7.01.05
Topic: T17 – 3D Worlds & Games
Skill: Add tube shapes to the 3D scene
Description: Students use the `add tube [COLOR] diameter-top diameter-bottom height arc sides thickness` block to create hollow tubes for pipes, tunnels, or architectural elements. **Parameters:** Top/bottom diameters (different = tapered), arc (full circle = 360°, half = 180°), thickness (wall thickness). _CSTA: 3A-AP-13._

Dependencies:
* T17.G7.01.04: Add cone shapes from vertex lists



ID: T17.G7.01.06
Topic: T17 – 3D Worlds & Games
Skill: Add rectangle tube shapes
Description: Students use the `add rectangle tube [COLOR] size-X size-Y height thickness` block to create hollow rectangular tubes for ducts, channels, or frames. **Uses:** Rectangular pipes, architectural frames, ductwork. _CSTA: 3A-AP-13._

Dependencies:
* T17.G7.01.05: Add tube shapes to the 3D scene



ID: T17.G7.01.07
Topic: T17 – 3D Worlds & Games
Skill: Add stair shapes to the 3D scene
Description: Students use the `add stairs [COLOR] width depth height step-count` block to create staircase structures for platformers or architectural scenes. **Parameters:** Width (how wide), depth (how deep each step), height (total rise), step count (number of steps). _CSTA: 2-AP-16._

Dependencies:
* T17.G7.01.06: Add rectangle tube shapes



ID: T17.G7.02.01
Topic: T17 – 3D Worlds & Games
Skill: Copy objects using grid matrix patterns
Description: Students use the `copy by matrix count-x count-y count-z spacing-x spacing-y spacing-z` block to efficiently duplicate objects in 3D arrays without manual loops. **Uses:** Create forests (grid of trees), building blocks, fences, arrays of collectibles. **How it works:** Copies selected object in 3D grid pattern with specified spacing. _CSTA: 3A-AP-17._

Dependencies:
* T17.G7.01.07: Add stair shapes to the 3D scene



ID: T17.G7.02.02
Topic: T17 – 3D Worlds & Games
Skill: Copy objects using mirror symmetry
Description: Students use the `copy to mirror position [PLANE]` block to create symmetrical designs across planes (XY, XZ, YZ). **Uses:** Symmetrical buildings, vehicles (left/right mirror), decorative patterns. **How it works:** Creates mirrored copy across specified plane. _CSTA: 3A-AP-17._

Dependencies:
* T17.G7.02.01: Copy objects using grid matrix patterns



ID: T17.G7.02.03
Topic: T17 – 3D Worlds & Games
Skill: Copy objects using rotational symmetry
Description: Students use the `copy to rotated position around [AXIS] count degrees` block to duplicate objects in circular patterns (like petals, spokes, columns around a center). **Parameters:** Axis of rotation (X, Y, or Z), count (how many copies), degree step (angle between copies—360/count for even distribution). _CSTA: 3A-AP-17._

Dependencies:
* T17.G7.02.02: Copy objects using mirror symmetry



ID: T17.G7.03.01
Topic: T17 – 3D Worlds & Games
Skill: Add distance constraints between physics bodies
Description: Students use the `add distance constraint between [BODY1] and [BODY2] distance` block to keep two physics bodies at a fixed or maximum distance, creating ropes, chains, or pendulums. **How it works:** Constraint maintains specified distance between bodies as they move. **Uses:** Ropes, chains, swinging objects, tethers. _CSTA: 3A-AP-13._

Dependencies:
* T17.G7.02.03: Copy objects using rotational symmetry



ID: T17.G7.03.02
Topic: T17 – 3D Worlds & Games
Skill: Add hinge constraints for rotating joints
Description: Students use the `add hinge constraint between [BODY1] and [BODY2] at point axis` block to create rotating joints like doors, gates, or mechanical arms that pivot around an axis. **Parameters:** Hinge point (where joint is), axis (which axis to rotate around). **Uses:** Doors, gates, swinging bridges, mechanical arms. _CSTA: 3A-AP-13._

Dependencies:
* T17.G7.03.01: Add distance constraints between physics bodies



ID: T17.G7.03.03
Topic: T17 – 3D Worlds & Games
Skill: Configure hinge constraint limits and motors
Description: Students use the `set limits for hinge constraint min max` to control how far hinges can rotate (door that only opens 90°) and `set motor for hinge constraint speed` to add motorized rotation (automatic opening door). **Limits:** Prevent over-rotation. **Motors:** Create automatic movement. _CSTA: 3A-AP-13._

Dependencies:
* T17.G7.03.02: Add hinge constraints for rotating joints



ID: T17.G7.03.04
Topic: T17 – 3D Worlds & Games
Skill: Add fixed constraints for rigid connections
Description: Students use the `add fixed constraint between [BODY1] and [BODY2]` block to weld physics bodies together rigidly, creating compound objects like connected train cars or attached weapons. **How it works:** Bodies locked together, move as single unit. **Uses:** Multi-part objects, attached weapons/tools. _CSTA: 3A-AP-13._

Dependencies:
* T17.G7.03.03: Configure hinge constraint limits and motors



ID: T17.G7.03.05
Topic: T17 – 3D Worlds & Games
Skill: Remove physics constraints
Description: Students use the `remove constraint named [NAME]` block to disconnect previously linked physics bodies, useful for detaching objects or breaking connections (breaking rope, opening lock, separating train cars). _CSTA: 2-AP-10._

Dependencies:
* T17.G7.03.04: Add fixed constraints for rigid connections



ID: T17.G7.04.01
Topic: T17 – 3D Worlds & Games
Skill: Move objects along their current direction
Description: Students use the `move [DISTANCE] along current direction in [T] seconds` block to move objects forward based on their facing direction, useful for projectiles or AI movement that should move "forward" relative to rotation. _CSTA: 2-AP-13._

Dependencies:
* T17.G7.03.05: Remove physics constraints



ID: T17.G7.04.02
Topic: T17 – 3D Worlds & Games
Skill: Point objects toward a target position
Description: Students use the `point to position xyz in [T] seconds` block to orient objects toward a target location, useful for NPCs looking at players or turrets aiming. **How it works:** Smoothly rotates object to face target position over specified time. _CSTA: 2-AP-13._

Dependencies:
* T17.G7.04.01: Move objects along their current direction



ID: T17.G7.05.01
Topic: T17 – 3D Worlds & Games
Skill: Merge multiple meshes into one
Description: Students use the `merge [OBJECT1] into [OBJECT2]` block to combine multiple 3D objects into a single mesh for optimization or to create complex shapes. **Benefits:** Better performance (one object instead of many), enable compound physics shapes. **Use case:** Merge building parts, combine decorative elements. _CSTA: 3A-AP-17._

Dependencies:
* T17.G7.04.02: Point objects toward a target position



ID: T17.G7.05.02
Topic: T17 – 3D Worlds & Games
Skill: Create compound physics bodies
Description: Students use the `add physics bodies into compound [NAME]` block to attach compound physics bodies to merged meshes for complex collision shapes like vehicles (multiple collision shapes for different parts). _CSTA: 3A-AP-17._

Dependencies:
* T17.G7.05.01: Merge multiple meshes into one



ID: T17.G7.05.03
Topic: T17 – 3D Worlds & Games
Skill: Use carve operations for boolean geometry
Description: Students use the `carve [OBJECT1] with [OBJECT2]` block to subtract one mesh from another, creating windows, doorways, or hollowed objects (boolean subtraction). **How it works:** Object2's volume removed from Object1. **Uses:** Cut windows in walls, create tunnels, hollow out objects. _CSTA: 3A-AP-13._

Dependencies:
* T17.G7.05.02: Create compound physics bodies



ID: T17.G7.06.01
Topic: T17 – 3D Worlds & Games
Skill: Animate camera position transitions
Description: Students use the `set camera distance v-angle h-angle target xyz in [T] seconds` block to choreograph smooth camera movements for cutscenes or transitions. **Parameters:** All camera parameters can be smoothly animated over time. **Uses:** Cinematic cutscenes, camera reveals, dramatic angles. _CSTA: 2-AP-16._

Dependencies:
* T17.G7.05.03: Use carve operations for boolean geometry



ID: T17.G7.06.02
Topic: T17 – 3D Worlds & Games
Skill: Add trails to moving objects
Description: Students use the `add trail color width segments` block to attach trail effects to moving objects, showing motion paths for projectiles, vehicles, or characters. **Parameters:** Color (trail color), width (trail thickness), segments (how many trail segments to track). _CSTA: 2-AP-16._

Dependencies:
* T17.G7.06.01: Animate camera position transitions



ID: T17.G7.06.03
Topic: T17 – 3D Worlds & Games
Skill: Create custom particle emitters
Description: Students use the `add particle emitter [CONFIG]` block to create custom particle systems with full control over appearance, movement, lifetime, and behavior. **Parameters:** Emission rate, particle lifetime, initial velocity, colors, sizes, textures. **Uses:** Custom effects beyond prebuilt options. _CSTA: 3A-AP-17._

Dependencies:
* T17.G7.06.02: Add trails to moving objects



ID: T17.G7.07
Topic: T17 – 3D Worlds & Games
Skill: Trace camera and object movement in complex scenes
Description: Students analyze a multi-object 3D animation sequence with camera transitions, predicting the visual result at each keyframe by mentally tracing: (1) Object positions and rotations through time, (2) Camera position and target, (3) What appears in frame at each moment. They document predictions then run to verify. _CSTA: 3A-AP-23._

Dependencies:
* T17.G7.06.01: Animate camera position transitions
* T17.G7.04.02: Point objects toward a target position



ID: T17.G7.08
Topic: T17 – 3D Worlds & Games
Skill: Design level progression with increasing difficulty
Description: Students create a multi-level 3D game where each level introduces new challenges, obstacles, or mechanics progressively. They balance difficulty curves ensuring: (1) Early levels teach mechanics, (2) Mid levels challenge mastery, (3) Late levels require combining skills. They test with players and adjust pacing based on feedback. _CSTA: 3A-AP-18._

Dependencies:
* T17.G6.09: Build a physics-based puzzle or game
* T17.G7.02.01: Copy objects using grid matrix patterns



## GRADE 8 (24 skills - Professional techniques and integration)

ID: T17.G8.01.01
Topic: T17 – 3D Worlds & Games
Skill: Enable car physics simulation
Description: Students use the `enable car simulation mass restitution friction tire-friction suspension` block to enable car physics on a vehicle model. **Parameters:** Mass (vehicle weight), restitution (bounciness), friction (body friction), tire friction (grip), suspension (spring stiffness). _CSTA: 3A-AP-13._

Dependencies:
* T17.G7.06.03: Create custom particle emitters
* T08.G6.01: Use conditionals in physics simulations



ID: T17.G8.01.02
Topic: T17 – 3D Worlds & Games
Skill: Control car engine and brakes
Description: Students use the `set car engine force [FORCE] brake [LEVEL]` block to control acceleration and braking of physics-enabled vehicles. **Engine force:** Positive = accelerate, 0 = coast, negative = reverse. **Brake level:** 0 = no brakes, 1 = full brakes. _CSTA: 3A-AP-13._

Dependencies:
* T17.G8.01.01: Enable car physics simulation



ID: T17.G8.01.03
Topic: T17 – 3D Worlds & Games
Skill: Steer car to an angle
Description: Students use the `steer car to angle [DEGREES]` block to control wheel steering angle for turning physics-enabled vehicles. **Angle:** 0 = straight, positive = turn right, negative = turn left. **Typical range:** -30 to 30 degrees. _CSTA: 3A-AP-13._

Dependencies:
* T17.G8.01.02: Control car engine and brakes



ID: T17.G8.02.01
Topic: T17 – 3D Worlds & Games
Skill: Set up multiple camera display regions
Description: Students use the `set display region bottom-left width height border` block to create split-screen views or picture-in-picture displays for multiple camera feeds (two-player split-screen, rear-view mirrors, mini-map cameras). **Parameters:** Position (where region appears), size (region dimensions), border (frame visibility). _CSTA: 3A-AP-17._

Dependencies:
* T17.G8.01.03: Steer car to an angle



ID: T17.G8.02.02
Topic: T17 – 3D Worlds & Games
Skill: Add skybox textures to scenes
Description: Students use the `set sky [SKYTYPE]` block to add skybox textures for 360-degree background environments (space, mountains, city skylines, fantasy worlds). **What skyboxes are:** Cube-mapped textures creating illusion of distant environment. **Available options:** Various preset skyboxes from library. _CSTA: 2-AP-15._

Dependencies:
* T17.G8.02.01: Set up multiple camera display regions



ID: T17.G8.02.03
Topic: T17 – 3D Worlds & Games
Skill: Add post-processing pipeline effects
Description: Students use the `add pipeline vignette bloom antialiasing sharpening contrast exposure` block to enhance visual quality with post-processing effects. **Effects:** Vignette (darkened edges), bloom (glow on bright areas), antialiasing (smooth edges), sharpening (detail enhancement), contrast (light/dark separation), exposure (overall brightness). _CSTA: 3A-AP-17._

Dependencies:
* T17.G8.02.02: Add skybox textures to scenes
* T03.G6.01: Propose a module hierarchy for a medium project



ID: T17.G8.03.01
Topic: T17 – 3D Worlds & Games
Skill: Export 3D models as GLB files
Description: Students use the `export object [NAME] as GLB file` block to save created 3D geometry for use in other applications or sharing. **GLB format:** Standard 3D model format supported by many applications (Blender, Unity, web viewers). **Uses:** Share creations, use in other software, 3D printing preparation. _CSTA: 3A-AP-21._

Dependencies:
* T17.G8.02.03: Add post-processing pipeline effects



ID: T17.G8.03.02
Topic: T17 – 3D Worlds & Games
Skill: Export 3D models as STL files for 3D printing
Description: Students use the `export object [NAME] as STL file` block to export 3D geometry suitable for 3D printing, bridging digital creation with physical fabrication. **STL format:** Standard for 3D printing. **Preparation needed:** Ensure mesh is closed (no holes), appropriate scale, manifold geometry. _CSTA: 3A-AP-21._

Dependencies:
* T17.G8.03.01: Export 3D models as GLB files



ID: T17.G8.04.01
Topic: T17 – 3D Worlds & Games
Skill: Enable AR world camera mode
Description: Students use the `switch to AR world camera` block to enable augmented reality, placing 3D objects in real-world environments using the device camera. **How it works:** Device camera becomes background, 3D objects appear anchored in real world. **Uses:** AR games, educational AR visualizations, virtual furniture placement. _CSTA: 3B-AP-16._

Dependencies:
* T17.G8.03.02: Export 3D models as STL files for 3D printing



ID: T17.G8.04.02
Topic: T17 – 3D Worlds & Games
Skill: Enable AR face tracking mode
Description: Students use the `switch to AR face camera` block to enable face tracking that can attach 3D objects to detected faces for filters or effects. **How it works:** Detects face landmarks, tracks face movement, anchors objects to face position. **Uses:** Face filters, virtual makeup, educational face anatomy. _CSTA: 3B-AP-16._

Dependencies:
* T17.G8.04.01: Enable AR world camera mode



ID: T17.G8.04.03
Topic: T17 – 3D Worlds & Games
Skill: Enable AR image/logo tracking mode
Description: Students use the `switch to AR image tracking` block to display 3D content when specific images or logos are detected by the camera. **How it works:** Upload target image, camera detects image, 3D content appears anchored to image. **Uses:** Interactive posters, educational cards, marketing AR. _CSTA: 3B-AP-16._

Dependencies:
* T17.G8.04.02: Enable AR face tracking mode



ID: T17.G8.05.01
Topic: T17 – 3D Worlds & Games
Skill: Build mirrors for reflective surfaces
Description: Students use the `build mirror brightness using object [NAME]` block to create reflective surfaces showing other objects, useful for water, windows, or polished floors. **Parameters:** Brightness (reflection intensity), object (which object becomes mirror surface). _CSTA: 3A-AP-17._

Dependencies:
* T17.G8.04.03: Enable AR image/logo tracking mode



ID: T17.G8.05.02
Topic: T17 – 3D Worlds & Games
Skill: Create geometry points in 3D space
Description: Students use the `geometry: add point at xyz color size` block to define vertices in 3D space as the foundation for custom procedural geometry. **Uses:** Building custom meshes from scratch, visualizing data points, creating custom shapes. _CSTA: 3A-AP-13._

Dependencies:
* T17.G8.05.01: Build mirrors for reflective surfaces



ID: T17.G8.05.03
Topic: T17 – 3D Worlds & Games
Skill: Create geometry lines between points
Description: Students use the `geometry: add line between points` block to create line segments between defined points for wireframe or structural visualization. **Uses:** Visualize connections, create wireframe models, show relationships between data points. _CSTA: 3A-AP-13._

Dependencies:
* T17.G8.05.02: Create geometry points in 3D space



ID: T17.G8.05.04
Topic: T17 – 3D Worlds & Games
Skill: Create geometry triangles from points
Description: Students use the `geometry: add triangle from points color` block to create triangular faces from three points, building custom meshes from vertices programmatically. **How it works:** Three points define triangle, normal direction determines which side is visible. **Uses:** Procedural mesh generation, terrain, custom models. _CSTA: 3A-AP-13._

Dependencies:
* T17.G8.05.03: Create geometry lines between points



ID: T17.G8.06.01
Topic: T17 – 3D Worlds & Games
Skill: Analyze and optimize 3D scene performance
Description: Students profile a sluggish 3D project, identify bottlenecks (too many objects, excessive physics bodies, inefficient loops, too many dynamic objects, large textures, many lights with shadows), and refactor using: object pooling (reuse instead of create/delete), culling (remove off-screen objects), merged meshes, optimized textures, fewer lights. They measure before/after performance. _CSTA: 3B-AP-11._

Dependencies:
* T17.G8.05.04: Create geometry triangles from points
* T12.G6.01: Trace complex code with multiple variables



ID: T17.G8.06.02
Topic: T17 – 3D Worlds & Games
Skill: Analyze trade-offs in 3D design decisions
Description: Students review a completed 3D project and explain design choices with justifications: (1) Physics vs manual motion (realism vs control), (2) Camera placement (gameplay clarity vs cinematic feel), (3) Effect usage (visual appeal vs performance), (4) Lighting approach (realism vs performance). They cite pros and cons relative to project requirements and constraints. _CSTA: 3B-AP-22._

Dependencies:
* T17.G8.06.01: Analyze and optimize 3D scene performance
* T03.G6.01: Propose a module hierarchy for a medium project



ID: T17.G8.07
Topic: T17 – 3D Worlds & Games
Skill: Design and document a 3D game architecture
Description: Students plan a complex 3D game by creating a comprehensive design document outlining: (1) Game mechanics (core gameplay loop, controls, win/lose conditions), (2) Level structure (how levels progress, difficulty curve), (3) Object hierarchy (what objects exist, how they interact), (4) Physics requirements (what uses physics, collision rules), (5) Visual effects (particles, lighting, post-processing), (6) Control schemes (keyboard/joystick mapping). They justify technical choices and identify potential challenges with mitigation strategies. _CSTA: 3B-AP-14._

Dependencies:
* T17.G8.06.02: Analyze trade-offs in 3D design decisions
* T17.G7.08: Design level progression with increasing difficulty



ID: T17.G8.08
Topic: T17 – 3D Worlds & Games
Skill: Integrate AI behaviors with 3D game mechanics
Description: Students combine AI-driven behaviors (pathfinding, decision-making, state machines, targeting) with 3D physics and animation to create intelligent NPCs or enemies that respond dynamically to player actions in 3D space. **Requirements:** AI selects targets in 3D, navigates around obstacles, responds to player position, uses appropriate animations, interacts with physics (avoids falling, responds to collisions). _CSTA: 3B-AP-16._

Dependencies:
* T17.G8.01.03: Steer car to an angle
* T17.G7.04.02: Point objects toward a target position



ID: T17.G8.09
Topic: T17 – 3D Worlds & Games
Skill: Build a complete 3D game with physics, effects, and UI
Description: Students create a polished 3D game integrating multiple systems: (1) 3D scene with environment, lighting, and effects (fog, particles, shadows), (2) Physics-based gameplay (player physics, collisions, physics puzzles), (3) Player controls (responsive input, camera control), (4) Scoring/UI (HUD, menus, feedback), (5) Multiple levels or progressive difficulty, (6) Visual and audio feedback (effects, sounds). **This is the capstone skill demonstrating mastery of 3D game development.** _CSTA: 3B-AP-16._

Dependencies:
* T17.G8.07: Design and document a 3D game architecture
* T17.G8.04.01: Enable AR world camera mode
* T17.G8.02.03: Add post-processing pipeline effects
