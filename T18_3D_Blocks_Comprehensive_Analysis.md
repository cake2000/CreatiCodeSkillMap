# COMPREHENSIVE 3D BLOCKS ANALYSIS FOR CREATICODE PLATFORM

## EXECUTIVE SUMMARY
Total 3D-related blocks found: **239 blocks**

### Distribution by Category:
- **3D Scene**: 47 blocks (Scene setup, camera, lighting, environment)
- **3D Object**: 50 blocks (Object creation, primitives, models, avatars)
- **3D Action**: 51 blocks (Movement, rotation, collision, interaction)
- **3D Tools**: 32 blocks (Materials, textures, transformations, utilities)
- **3D Physics**: 36 blocks (Physics simulation, forces, constraints)
- **3D Effect**: 18 blocks (Particle systems, trails, emitters)
- **3D AR/VR**: 5 blocks (Augmented reality features)

---

## DETAILED BREAKDOWN BY FUNCTIONAL AREA

### 1. SCENE SETUP & INITIALIZATION (3D Scene)

#### Scene Management:
- `initialize 3D scene [SCENETYPE] as hidden [ISHIDDEN]` - Initialize 3D scene with Babylon.js engine
- `show 3D scene [ISVISIBLE]` - Toggle scene visibility
- `when 3D scene is initialized` - Event trigger when scene ready
- `set scene background color [COLOR]` - Set background color

#### Environment Effects:
- `set scene fog [MODE] [COLOR] start (DISTANCE) end (DISTANCE) density (DENSITY)` - Linear/exponential fog
- `set sky [SKYTYPE]` - Multiple skybox textures (Blue Sky, HDR, Starfield 1-9, Above Earth 1-3, Mars Surface, etc.)
- `remove sky` - Remove skybox
- `set clipping plane [ID] direction xyz (X) (Y) (Z) offset (OFFSET)` - Add clipping planes (up to 4)
- `remove clipping plane [ID]` - Remove clipping plane

#### Post-Processing Pipeline:
- `add pipeline vignette (RADIUS) [COLOR] bloom strength (STRENGTH) threshold (%)  kernel (KERNEL) antialiasing [YES/NO] sharpening [YES/NO] camera contrast (C) exposure (E)` - Advanced post-processing effects
- `remove pipeline` - Remove pipeline

#### Display & Viewport:
- `set display region bottom (%)  left (%)  width (%)  height (%)  border width (W) color [COLOR] for camera [NAME]` - Multi-camera viewport setup
- `switch to full screen [BORDERTYPE]` - Fullscreen mode
- `lock pointer [YES/NO]` - Pointer lock for FPS-style controls

#### Virtual Controls:
- `add [SIDE] joystick [COLOR1] [COLOR2] scale [SCALE]` - Virtual joystick for mobile
- `[SIDE] joystick [PROPERTY]` - Read joystick values
- `remove all joysticks` - Remove joysticks

#### Debug & Utilities:
- `show 3D axis [SHOW] length (LENGTH)` - Show world coordinate system
- `show inspector [SHOW]` - Babylon.js inspector
- `GPU Available` - Check GPU support

---

### 2. CAMERA SYSTEM (3D Scene)

#### Camera Types:
- `add orbit camera distance (D) v-angle (V) h-angle (H) panning speed ratio (S) inputs key [KEY] pointer [POINTER] active [ACTIVE] as [NAME]` - Arc-rotate/orbit camera
- `add follow camera distance (D) z offset (Z) v-angle (V) h-angle (H) direction lock [TYPE] see-through (%)  active [YES/NO] as [NAME]` - Third-person follow camera

#### Camera Control:
- `set camera target xyz (X) (Y) (Z)` - Set camera look-at point
- `set camera target object [NAME] offset xyz (X) (Y) (Z)` - Target specific object
- `set camera distance (D) v-angle (V) h-angle (H) z offset (Z) target xyz (X) (Y) (Z) in (T) seconds` - Animate camera properties
- `set camera distance (D) [N/S] (°) (') (") [E/W] (°) (') (") in (T) seconds` - Geographic positioning on globe
- `configure camera radius min (MIN) max (MAX) visible range min (MIN) max (MAX) v-angle min (MIN) max (MAX) speed ratio panning (RATIO) angular (RATIO)` - Camera constraints and limits

#### Camera Hierarchy:
- `set [OBJECTNAME] as parent of camera` - Attach camera to object
- `set camera as parent` (in 3D Object category) - Attach object to camera

#### Camera Queries:
- `camera [PROPERTY]` - Read camera properties
- `get camera direction [FACE]` - Get view direction
- `get camera view position for xyz (X) (Y) (Z)` - Project 3D to screen coordinates

---

### 3. LIGHTING SYSTEM (3D Scene)

#### Light Types:
- `add ambient light [COLOR] sky direction xyz (X) (Y) (Z) intensity (I) as [NAME]` - Hemispheric/ambient light
- `add directional light [COLOR] in direction xyz (X) (Y) (Z) at xyz (X) (Y) (Z) intensity (I) as [NAME]` - Directional light (sunlight)
- `add point light [COLOR] at xyz (X) (Y) (Z) intensity (I) show position [YES/NO] as [NAME]` - Point light source
- `add spot light [COLOR] at xyz (X) (Y) (Z) open angle (A) intensity (I) blur (B) show position [YES/NO] as [NAME]` - Spotlight

#### Light Management:
- `remove all lights` - Remove all lights
- `remove light named [NAME]` - Remove specific light
- `switch [ON/OFF] light named [NAME]` - Toggle light
- `exclude object [OBJNAME] from light named [LIGHTNAME]` - Selective lighting

#### Shadow System:
- `cast shadow [YES/NO] from light named [NAME] blur size (B)` - Enable shadow casting
- `receives shadow [YES/NO]` - Enable shadow receiving

#### Glow & Highlight Effects:
- `create glow layer intensity (I) blur size (B) as [NAME]` - Glow layer
- `add to glow layer named [NAME]` - Add object to glow
- `remove from glow layer named [NAME]` - Remove from glow
- `create highlight layer blur size (B) as [NAME]` - Highlight layer
- `add highlight in [COLOR] to layer named [NAME]` - Add colored highlight
- `remove from highlight layer named [NAME]` - Remove highlight

---

### 4. OBJECT CREATION (3D Object)

#### Primitive Shapes:
- `add box [COLOR] size in x (X) y (Y) z (Z) edge radius (R) as [NAME]` - Box/cube
- `add 6-colored box [C1] [C2] [C3] [C4] [C5] [C6] size in x (X) y (Y) z (Z) as [NAME]` - Multi-colored box
- `add sphere [COLOR] size in x (X) y (Y) z (Z) arc (ARC) slice (SLICE) sides (S) as [NAME]` - Sphere/ellipsoid
- `add cylinder [COLOR] diameter top (T) bottom (B) height (H) arc (ARC) closed section [YES/NO] cap type [TYPE] sides (S) as [NAME]` - Cylinder/cone
- `add tube [COLOR] diameter top (T) bottom (B) height (H) arc (ARC) closed section [TYPE] cap type [TYPE] sides (S) thickness (T) as [NAME]` - Hollow tube
- `add rectangle tube [COLOR] size in X (X) Y (Y) height (H) cap type [TYPE] thickness (T) sides [COUNT] as [NAME]` - Rectangular tube
- `add capsule [COLOR] diameter top (T) bottom (B) height (H) sides (S) as [NAME]` - Capsule shape
- `add torus [COLOR] diameter (D) thickness (T) sides (S) as [NAME]` - Torus/donut
- `add plane [COLOR] size x (X) y (Y) as [NAME]` - Plane
- `add plane [COLOR] width (W) height (H) coefficients abcd (A) (B) (C) (D) as [NAME]` - Plane from equation

#### Complex Shapes:
- `add stairs [COLOR] width (W) depth (D) height (H) count (COUNT) thickness (T) type [TYPE] as [NAME]` - Stairs
- `add column [COLOR] 2D vertex list [LIST] height (H) cap type [TYPE] as [NAME]` - Extruded polygon
- `add cone [COLOR] vertex list [LIST] height (H) as [NAME]` - Cone from base polygon

#### Lines & Curves:
- `add line [COLOR] diameter (D) cap [CAP] arrow [ARROW] sides (S) xyz from (X1) (Y1) (Z1) to (X2) (Y2) (Z2) segments (S) as [NAME]` - Solid line
- `add dotted line [COLOR] diameter (D) segment length (L) gap length (G) cap [CAP] arrow [ARROW] sides (S) from xyz (X1) (Y1) (Z1) to xyz (X2) (Y2) (Z2) as [NAME]` - Dotted line
- `generate arc points from (X1) (Y1) (Z1) via (X2) (Y2) (Z2) to (X3) (Y3) (Z3) into list [LIST] count (N)` - Generate arc points
- `add curve [COLOR] diameter (D) cap [CAP] arrow [ARROW] sides (S) using list [LIST] from (START) to (END) segments (S) as [NAME]` - Curve from points
- `add moving line between [OBJ1] and [OBJ2] [COLOR] diameter (D) sides (S) as [NAME]` - Dynamic line

#### Text Objects:
- `add 3D text [TEXT] font [FONT] color [COLOR] width (W) height (H) diameter (D) camera facing [YES/NO] as [NAME]` - Flat 3D text
- `add 3D thick text [TEXT] font [FONT] color [COLOR] width (W) height (H) thickness (T) diameter (D) camera facing [YES/NO] as [NAME]` - Extruded text

#### Models & Assets:
- `add model [TYPE] target height (H) origin offset x (X) y (Y) z (Z) rotation x (RX) y (RY) z (RZ) hidden [YES/NO] as [NAME]` - Prebuilt models
- `add public object at URL [URL] as [TYPE] target height (H) rotation (RX) (RY) (RZ) origin offset (X) (Y) (Z) as [NAME]` - Load GLTF/GLB from URL
- `add community model [NAME] target height (H) rotation (RX) (RY) (RZ) origin offset (X) (Y) (Z) as [NAME]` - Community-shared models

#### Avatars:
- `add avatar [TYPE] height (H) as [NAME] hidden [YES/NO]` - Built-in avatars
- `add avatar [NAME] for user [USERNAME] height (H) as [NAME] hidden [YES/NO]` - User's uploaded avatars
- `add user avatar [NAME] height (H) as [NAME]` - Community avatars

#### Advanced Geometry:
- `geometry: add point at xyz (X) (Y) (Z) color [COLOR] size (S) on [PARENT] as [NAME]` - Point object
- `geometry: add point between points [P1] [P2] at (%)  color [COLOR] size (S) as [NAME]` - Interpolated point
- `geometry: add line between points [P1] [P2] color [COLOR] diameter (D) arrow [TYPE] sides (S) segments (S) as [NAME]` - Line between points
- `geometry: add triangle from points [P1] [P2] [P3] color [COLOR] as [NAME]` - Triangle
- `geometry: add frame box color [COLOR] size in x (X) y (Y) z (Z) thickness (T) labels [YES/NO] as [NAME]` - Wireframe box
- `geometry: add angle mark [P1] [P2] [P3] size (S) color [COLOR] diameter (D) arrow [TYPE] sides (S) label [TEXT] as [NAME]` - Angle visualization

#### Chemistry/Molecular:
- `chemistry: add atom [TYPE] as [NAME] connect hole [HOLES] to atom [NAME] hole [HOLES] distance (D)` - Predefined atoms
- `chemistry: add custom atom [COLOR] size (S) holes [HOLES] label [LABEL] angle [ANGLE] as [NAME] connect hole [HOLES] to atom [NAME] hole [HOLES] distance (D)` - Custom atoms

#### Special Objects:
- `add transformer as [NAME]` - Transform node for hierarchies
- `add voxel size in xyz (X) (Y) (Z) with costumes top [C] bottom [C] front [C] back [C] left [C] right [C] texture size (T) sampling [METHOD] as [NAME]` - Textured voxel
- `extrude costume [COSTUME] thickness (T) scaling factor (S) side color [COLOR] granularity (G) as [NAME]` - Extrude 2D image to 3D

#### Particle Systems (SPS):
- `convert to sps at xyz from list [LIST] updatable [YES/NO]` - Convert to solid particle system
- `add to sps [NAME] at xyz from list [LIST]` - Add instances to SPS

#### Object Management:
- `remove object named [NAME]` - Remove specific object
- `remove all objects` - Clear all objects
- `object [NAME] exists` - Check if object exists
- `show local axis [SHOW] length (L)` - Show object's local axes

---

### 5. POSITION, ROTATION & SCALE (3D Action & 3D Tools)

#### Position Control:
- `move to x (X) y (Y) z (Z) in (T) seconds [BLOCKING]` - Move to absolute position
- `move (DISTANCE) along current direction in (T) seconds [BLOCKING]` - Move forward/backward
- `copy position from camera` - Copy camera position
- `copy position from object [NAME]` - Copy object position
- `x position`, `y position`, `z position` (Motion category) - Read position

#### Rotation Control:
- `rotate to angle (A) around the [AXIS] axis in (T) seconds [BLOCKING]` - Rotate to absolute angle
- `rotate to direction x (X) y (Y) z (Z) in (T) seconds [BLOCKING]` - Set all rotation angles
- `turn (N) degrees around the [AXIS] axis in (T) seconds [BLOCKING]` - Relative rotation
- `point to position x (X) y (Y) z (Z) in (T) seconds [BLOCKING]` - Point toward position
- `copy direction from camera` - Copy camera orientation
- `copy direction from object [NAME]` - Copy object orientation
- `direction` (Motion category) - Read rotation angle

#### Scale Control:
- `update scale x (X)% y (Y)% z (Z)% in (T) seconds [BLOCKING]` - Animated scaling
- `update size x (X) y (Y) z (Z)` - Direct size change
- `set size to (N)%` (Looks category) - Uniform scaling
- `change size by (N)` (Looks category) - Relative scaling
- `size` (Looks category) - Read current scale

#### Speed-Based Movement:
- `set speed [TYPE] to (N)` - Set forward/backward/rotation speed
- Speed types: Forward Speed, Backward Speed, Left Rotation Speed, Right Rotation Speed

---

### 6. MATERIALS & TEXTURES (3D Tools)

#### Color & Material Properties:
- `update color diffusion [COLOR] emission [COLOR] roughness (R) brightness (B) remove texture [YES/NO] area [AREA]` - PBR material properties
- `get [COLORTYPE] color of object named [NAME]` - Read color values

#### Texture Mapping:
- `update texture [TEXTURENAME] unit size (SIZE) non-box repeat h (H) v (V) rotation (R) area [AREA]` - Apply built-in texture
- `update texture using costume [COSTUME] unit size (SIZE) non-box repeat h (H) v (V) rotation (R) area [AREA]` - Use costume as texture
- `add texture with shared file [URL] box unit size (SIZE) non-box repeat h (H) v (V) rotation (R) area [AREA]` - Load texture from URL

#### Special Materials:
- `apply grid material face [COLOR] line [COLOR] density (D) minor line visibility (V) line offset xyz (X) (Y) (Z)` - Grid material
- `material setting: wireframe mode [YES/NO] draw back face [YES/NO] z-offset (Z) log depth [YES/NO] transparent [YES/NO]` - Material settings
- `convert to flat shading` - Flat shading mode

#### Mirror/Reflection:
- `build mirror brightness (B) using object named [NAME]` - Create mirror
- `reflect in mirror [NAME]` - Add object to mirror
- `remove all reflections in mirror [NAME]` - Clear mirror

---

### 7. HIERARCHIES & PARENTING (3D Object)

#### Parent-Child Relationships:
- `set object [NAME] from sprite [SPRITE] as parent and update position/scale [YES/NO]` - Set parent object
- `unlink parent` - Remove parent
- `unlink all children` - Remove all children
- `set camera as parent` - Attach to camera
- `set [NAME] as parent of camera` (3D Scene) - Attach camera to object

#### Avatar Attachments:
- `attach to body part [PART] of [AVATAR] from sprite [SPRITE] target height (H)` - Attach to avatar skeleton
- `detach from body` - Detach from avatar

---

### 8. ANIMATION (3D Action)

#### Avatar Animations:
- `add animations [LIST]` - Add animations to avatar (animation library)
- `start animation [NAME] looping [YES/NO] progress from (START) to (END) speed ratio (RATIO) [BLOCKING] offset x (X) y (Y) z (Z) broadcast [MESSAGES] at progress [POINTS]` - Play avatar animation

#### Model Animations:
- `start model animation [NAME] looping [YES/NO] progress from (START) to (END) speed ratio (RATIO) [BLOCKING] offset x (X) y (Y) z (Z) broadcast [MESSAGES] at progress [POINTS]` - Play model animation

#### Skeletal Control:
- `update bone [BONE] move in x (X) y (Y) z (Z) rotate in x (RX) y (RY) z (RZ)` - Direct bone manipulation

---

### 9. INTERACTION & PICKING (3D Action)

#### Object Picking (Click):
- `turn on picking with [BUTTON] for objects created in sprites [LIST] on [ACTION]` - Enable picking
- `turn off picking for objects created in sprites [LIST]` - Disable picking
- `when an object from this sprite is picked` - Event trigger
- `picked object name` - Get picked object name
- `picked point x pos`, `y pos`, `z pos` - Get picked 3D coordinates

#### Hovering:
- `turn on hovering for objects created in sprites [LIST]` - Enable hover detection
- `turn off hovering for objects created in sprites [LIST]` - Disable hovering
- `hovered object name` - Get hovered object
- `hovered point x pos`, `y pos`, `z pos` - Get hover position

#### Dragging:
- `set dragging mode [MODE] direction X (X) Y (Y) z (Z)` - Configure drag behavior
- `set dragging limits min xyz (X) (Y) (Z) max xyz (X) (Y) (Z)` - Constrain dragging
- `when an object from this sprite starts to be dragged` - Drag start event
- `when an object from this sprite is being dragged` - During drag event
- `when an object from this sprite stops being dragged` - Drag end event
- `dragged object name` - Get dragged object

#### Screen-to-3D Mapping:
- `map screen XY (X) (Y) to XYZ position on object [NAME]` - Project 2D to 3D surface

---

### 10. COLLISION DETECTION (3D Action)

#### Raycast-Based Collision:
- `turn on [BLOCKING/NON-BLOCKING] collision with [SPRITE] collider z offset (Z) precision [TYPE] debug [YES/NO]` - Enable collision
- `when colliding with [SPRITE]` - Collision event
- `sprite object blocked [DIRECTION]` - Check if blocked
- `update collider dimension x (X) y (Y) z (Z) collider z offset (Z) sensing range x (X) y (Y) z (Z) color [COLOR]` - Configure collider

#### Mesh Collision Events:
- `broadcast [MESSAGE] on collision between [OBJ1] from [SPRITE1] and [OBJ2] from [SPRITE2]` - Mesh collision event

#### Overlap Detection:
- `broadcast [MESSAGE] when [OBJ1] from [SPRITE1] and [OBJ2] from [SPRITE2] overlap` - Bounding box overlap
- `objects [OBJ1] and [OBJ2] are overlapping` - Check overlap

#### Distance Sensing:
- `set distance sensor front [ON/OFF] back [ON/OFF] left [ON/OFF] right [ON/OFF] down [ON/OFF] up [ON/OFF] max distance (D) count [COUNT] visible [YES/NO]` - Configure distance sensors
- `distance to nearest obstacle in the [DIRECTION] direction for [NAME]` - Get distance
- `name of nearest obstacle in the [DIRECTION] direction for [NAME]` - Get obstacle name
- `broadcast [MESSAGE] when [DIMENSION] distance <= (D) between [OBJ1] from [SPRITE1] and [OBJ2] from [SPRITE2]` - Distance threshold event
- `distance between objects [OBJ1] and [OBJ2]` - Get distance

---

### 11. PHYSICS SIMULATION (3D Physics)

#### Physics World:
- `enable physics for scene with gravity (G)` - Initialize physics engine
- `update gravity for scene to (G)` - Change gravity
- `set physics frame rate [RATE]` - Set simulation rate
- `get physics frame rate` - Get frame rate

#### Physics Bodies:
- `add [SHAPE] physics body with mass (M) restitution (R)% friction (F)% frozen [YES/NO] debug [YES/NO] [COLOR]` - Add physics body
- Shapes: Box, Sphere, Cylinder, Mesh, Convex Hull, Compound
- `remove physics body` - Remove physics
- `freeze physics body named [NAME] [YES/NO]` - Freeze/unfreeze
- `freeze all physics bodys [YES/NO]` - Freeze all

#### Physics Properties:
- `update physics property restitution (R)% friction (F)%` - Update material
- `set physics body damping for movement (M)% rotation (R)% for [NAME]` - Damping
- `get physics body [PROPERTY] for [NAME]` - Query properties

#### Forces & Motion:
- `apply force strength (S) direction xyz (X) (Y) (Z) at relative point xyz (X) (Y) (Z) to [NAME]` - Apply force
- `apply impulse strength (S) direction xyz (X) (Y) (Z) at relative point xyz (X) (Y) (Z) to [NAME]` - Apply impulse
- `set physics body speed in xyz (X) (Y) (Z) for [NAME]` - Set linear velocity
- `set physics body rotation speed around xyz axes (RX) (RY) (RZ) for [NAME]` - Set angular velocity
- `set physics body speed in facing direction (S) for [NAME]` - Speed in forward direction
- `set physics body speed (S) towards target xyz (X) (Y) (Z) for [NAME]` - Speed toward point
- `set physics body speed (S) for [NAME] towards object [TARGET] from sprite [SPRITE]` - Speed toward object

#### Movement & Rotation Constraints:
- `set physics body movement speed limit (L) allow direction X [YES/NO] Y [YES/NO] Z [YES/NO] for [NAME]` - Limit linear motion
- `set physics body rotation speed limit (L) allow axis X [YES/NO] Y [YES/NO] Z [YES/NO] for [NAME]` - Limit angular motion
- `lock physics body speed in X (X) Y (Y) Z (Z) rotation around X (RX) Y (RY) Z (RZ) for [NAME]` - Lock axes

#### Collision Detection:
- `broadcast [MESSAGE] on collision between physics bodies of [NAME1] from [SPRITE1] and [NAME2] from [SPRITE2]` - Collision event
- `names of physics bodies in contact for [NAME]` - Get colliding bodies
- `update collision group [GROUP] target groups [GROUPS] for [NAME]` - Collision filtering

#### Constraints/Joints:
- `add fixed constraint between bodies of [OBJ1] from [SPRITE1] and [OBJ2] from [SPRITE2] named [NAME]` - Fixed joint
- `add distance constraint between bodies of [OBJ1] from [SPRITE1] and [OBJ2] from [SPRITE2] named [NAME]` - Distance joint
- `add hinge constraint between bodies of [OBJ1] from [SPRITE1] at point x (X) y (Y) z (Z) axis x (X) y (Y) z (Z) and [OBJ2] from [SPRITE2] at point x (X) y (Y) z (Z) axis x (X) y (Y) z (Z) named [NAME]` - Hinge joint
- `set limits for hinge constraint named [NAME] angle between (LOW) and (HIGH) softness (S) bias factor (B) relaxation (R)` - Hinge limits
- `set speed (S) for hinge constraint named [NAME]` - Motor speed
- `remove constraint named [NAME]` - Remove joint

#### Compound Bodies:
- `add physics bodies of [CHILDREN] into compound [NAME] keep object [YES/NO]` - Merge bodies

#### Car Physics:
- `enable car simulation mass (M) restitution (R)% friction (BF)% tire friction (TF)% suspension (S) for [NAME]` - Car physics
- `set car engine force (F) brake level (B)% for [NAME]` - Engine/brake
- `steer car to angle (A) for [NAME]` - Steering
- `set car wheel angle LF (LF) RF (RF) LB (LB) RB (RB) for [NAME]` - Individual wheel angles
- `set car wheel engine force LF (LF) RF (RF) LB (LB) RB (RB) brake level (B)% for [NAME]` - Individual wheel forces

---

### 12. PARTICLE EFFECTS (3D Effect)

#### Prebuilt Emitters:
- `add prebuilt emitter for [TYPE] [COLOR1] [COLOR2] capacity (C) texture size (T) source size (S) speed (S) max life (L) as [NAME]` - Quick emitters
- Types: Smoke, Fire, Explosion, Fountain, Rain, Snow, Firework, etc.

#### Custom Emitters:
- `add particle emitter shape [SHAPE] texture [TEXTURE] facing camera [YES/NO] life min (MIN) max (MAX) capacity (C) GPU [YES/NO] time ratio (%)  as [NAME]` - Create emitter
- Shapes: Point, Box, Sphere, Hemisphere, Cylinder, Cone, Mesh

#### Emitter Shape Configuration:
- `configure box emitter [NAME]: min xyz (X) (Y) (Z) max xyz (X) (Y) (Z)` - Box emitter
- `configure sphere emitter [NAME]: radius (R) range (R)` - Sphere emitter
- `configure hemispheric emitter [NAME]: radius (R) range (R)` - Hemisphere emitter
- `configure cylinder emitter [NAME]: radius (R) range (R) height (H) direction randomness (R)%` - Cylinder emitter
- `configure cone emitter [NAME]: radius (R) angle (A) radius range (R) height range (H)` - Cone emitter
- `configure mesh emitter [NAME]: use mesh normal direction [YES/NO]` - Mesh emitter

#### Particle Properties:
- `configure emitter [NAME] color: start [C1] to [C2] end [C3] to [C4] at progress (%)  [C5] to [C6]` - Color animation
- `configure emitter [NAME] size: start (S1) to (S2) end (S3) to (S4) at progress (%)  (S5) to (S6)` - Size animation
- `configure emitter [NAME] scale: x min (X)% max (X)% y min (Y)% max (Y)%` - Scale range
- `configure emitter [NAME] rotation speed: start (S1) to (S2) end (S3) to (S4) at progress (%)  (S5) to (S6)` - Rotation animation
- `configure emitter [NAME] initial rotation: min (MIN) max (MAX)` - Initial rotation
- `configure emitter [NAME] movement: speed min (MIN) max (MAX) direction 1 (X) (Y) (Z) direction 2 (X) (Y) (Z)` - Particle motion
- `configure emitter [NAME] blend mode [MODE]` - Blending mode

#### Emitter Control:
- `start emitter [NAME] [RATE/COUNT] of (N)` - Start emission
- `[ACTION] emitter [NAME]` - Start/stop/pause/dispose
- Actions: Start, Stop, Pause, Dispose

#### Trails:
- `add trail diffusion [COLOR] emission [COLOR] width (W) segments (N) as [NAME]` - Motion trail effect

---

### 13. ADVANCED TOOLS & UTILITIES (3D Tools)

#### Object Operations:
- `copy object share data [YES/NO] as [NAME]` - Clone object
- `merge [OBJ1] into [OBJ2]` - Boolean union
- `carve [OBJ1] with [OBJ2]` - Boolean subtraction
- `bake current transformations` - Apply transformations to mesh

#### Instancing & Arrays:
- `copy by matrix count in xyz (X) (Y) (Z) spacing in xyz (X) (Y) (Z) random ratio in spacing (%)  scale (%)  z-rotation (%)  [SUBSET] object [OBJ]` - Matrix array
- `copy by matrix from center count in xyz (X) (Y) (Z) spacing in xyz (X) (Y) (Z) random ratio in spacing (%)  scale (%)  z-rotation (%)  [SUBSET] object [OBJ]` - Centered matrix
- `copy to mirror position [TYPE]` - Mirror copies (XY, YZ, ZX planes)
- `copy to rotated position around the [AXIS] axis count (N) degree step (STEP) shift XYZ (X) (Y) (Z)` - Radial array
- `for each 3D object named [VARIABLE]` - Iterate through copies

#### Mesh Editing:
- `subdivide faces by (N)` - Mesh subdivision
- `update vertices scale xyz (X) (Y) (Z) move xyz (X) (Y) (Z) position min xyz (X) (Y) (Z) max xyz (X) (Y) (Z)` - Transform vertices

#### Visibility & Rendering:
- `show bounding box [YES/NO]` - Show bounds
- `show edges [YES/NO] color [COLOR] thickness (T)` - Show wireframe edges
- `show skeleton [YES/NO]` - Show armature
- `set rendering layer [ID]` - Rendering order
- `set camera facing mode [MODE]` - Billboard mode

#### Export:
- `export object [NAME] as a GLB file` - Export to GLB
- `export object [NAME] as an STL file` - Export to STL

#### Object Properties:
- `[PROPERTY] of object [NAME] from sprite [SPRITE]` - Read property
- `property [PROPERTY] of [NAME]` - Read property (alternate)
- `set property [PROPERTY] to [VALUE] for [NAME]` - Write property

#### Object Selection:
- `select sprite object by name [NAME]` - Switch current object
- `sprite object name` - Get current object name

---

### 14. AR/VR FEATURES (3D AR/VR)

#### AR Cameras:
- `switch to AR world camera scale (S) emulation mode [YES/NO]` - World-scale AR with back camera
- `switch to AR face camera show marker [YES/NO] scale (S) emulation mode [YES/NO] data table [TABLE] with mesh of face [YES/NO] eyes [YES/NO] mouth [YES/NO] lips [YES/NO]` - Face tracking AR
- `switch to AR LOGO as [TYPE] camera [CAMTYPE] marker [YES/NO] scale (S) emulation [YES/NO]` - Logo-based AR anchor

#### AR Utilities:
- `convert to transparent occlusion` - Create occlusion mesh

#### Debug:
- `show inspector [YES/NO]` - Babylon.js inspector

---

### 15. ADDITIONAL FEATURES

#### Speech Bubbles (3D Action):
- `show speech bubble [TEXT] offset xyz (X) (Y) (Z) max width (W) text font [FONT] size (SIZE) color [COLOR] background [COLOR] for [T] seconds camera facing [YES/NO] ID [ID]` - 3D speech bubble

#### Webcam Integration (3D Scene):
- `turn [ON/OFF] webcam background [FRONT/BACK] in [FLIP] mode` - AR webcam background

#### Distance Calculation (Operator):
- `distance between (X1) (Y1) (Z1) and (X2) (Y2) (Z2) method [DIRECT/MANHATTAN]` - 3D distance function

#### Visibility (Looks):
- `show` - Show sprite object (works in 3D)
- `hide` - Hide sprite object (works in 3D)

#### Sensing (Sensing):
- `[ATTRIBUTE] of [SPRITE]` - Extended for 3D (x/y/z position, direction)

---

## SUMMARY OF COVERAGE

### Core 3D Features (All Present):
✅ Scene initialization and management
✅ Multiple camera types (orbit, follow, free)
✅ Comprehensive lighting (ambient, directional, point, spot)
✅ Shadow casting and receiving
✅ Extensive primitive shapes (box, sphere, cylinder, tube, capsule, torus, plane, etc.)
✅ Line and curve creation
✅ 3D text (flat and extruded)
✅ Model loading (GLTF/GLB from library, URL, community)
✅ Avatar system with animations
✅ Position, rotation, scale transformations
✅ Material system (color, texture, roughness, emission)
✅ Texture mapping (built-in, costume, URL)
✅ Parent-child hierarchies
✅ Object picking/clicking
✅ Hover detection
✅ Drag-and-drop
✅ Collision detection (raycast-based)
✅ Distance sensing
✅ Full physics engine (Babylon.js physics)
✅ Physics bodies (box, sphere, mesh, convex hull)
✅ Forces and impulses
✅ Constraints/joints (fixed, distance, hinge)
✅ Particle systems (extensive customization)
✅ Visual effects (fog, skybox, glow, highlight, bloom, vignette)
✅ Post-processing pipeline
✅ AR features (world, face, image tracking)

### Advanced Features:
✅ Geometry tools (points, lines, triangles, angle marks)
✅ Chemistry/molecular structures
✅ Skeletal animation and bone manipulation
✅ Car physics simulation
✅ Solid particle systems (SPS) for optimization
✅ Mesh operations (merge, carve, subdivide)
✅ Instancing and arrays (matrix, radial, mirror)
✅ Export to GLB/STL
✅ Mirror/reflection effects
✅ Trails and motion blur
✅ Grid material
✅ Clipping planes
✅ Multi-camera viewports
✅ Virtual joysticks for mobile
✅ Webcam integration
✅ 3D coordinate system visualization

### Notable Capabilities:
- **239 total 3D blocks** across 7 categories
- **Babylon.js engine** - Professional 3D engine
- **Full PBR materials** - Physically-based rendering
- **GPU particle systems** - High-performance effects
- **Skeletal animation** - Avatar and model animations
- **Physics simulation** - Realistic physics with constraints
- **AR support** - Face tracking, world tracking, image anchors
- **Advanced geometry** - Constructive solid geometry, extrusion
- **Optimization** - SPS, instancing, LOD support implied

---

## VERIFICATION NOTES

This analysis is based on extracting ALL blocks from `/media/binyu/USB2/ScratchCopilot/blockdes8.txt` with:
- `Category: 3D Scene` - 47 blocks
- `Category: 3D Object` - 50 blocks  
- `Category: 3D Action` - 51 blocks
- `Category: 3D Tools` - 32 blocks
- `Category: 3D Physics` - 36 blocks
- `Category: 3D Effect` - 18 blocks
- `Category: 3D AR/VR` - 5 blocks

Total: **239 blocks**

Additional blocks marked as "Can be used for 3D: true" in other categories (Motion, Looks, Sensing, Operators) provide extended 3D functionality for position, visibility, attributes, and distance calculations.

---

## RECOMMENDATIONS FOR T18 SKILL VERIFICATION

When verifying T18 (3D Graphics & Visualization) skills, ensure coverage of:

1. **Scene Setup**: Scene initialization, cameras, lighting, environment
2. **Object Creation**: Primitives, models, avatars, text, lines
3. **Transformations**: Position, rotation, scale with animation
4. **Materials**: Colors, textures, PBR properties
5. **Interaction**: Picking, hovering, dragging
6. **Collision**: Raycast collision, distance sensing, overlap detection  
7. **Physics**: Bodies, forces, constraints, car simulation
8. **Effects**: Particles, trails, post-processing, glow/highlight
9. **Advanced**: Hierarchies, bone animation, arrays, mesh operations
10. **AR/VR**: Face tracking, world tracking, image anchors

The platform has **extensive** 3D capabilities that go far beyond basic visualization, including professional-grade features like:
- Full physics simulation
- Skeletal animation
- AR integration
- Advanced particle systems
- Mesh CSG operations
- Export functionality

