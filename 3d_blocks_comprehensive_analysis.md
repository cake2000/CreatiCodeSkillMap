# CreatiCode 3D Blocks - Comprehensive Analysis

## Summary Statistics
- **Total 3D Categories**: 7
- **Total 3D Blocks**: 239

### Breakdown by Category:
- 3D Scene: 47 blocks
- 3D Object: 50 blocks
- 3D Action: 51 blocks
- 3D Tools: 32 blocks
- 3D Physics: 36 blocks
- 3D Effect: 18 blocks
- 3D AR/VR: 5 blocks

---

## 1. 3D SCENE INITIALIZATION & SETUP (47 blocks)

### Scene Management
- `initialize 3D scene [SCENETYPE] as hidden [ISHIDDEN]` - Initialize 3D scene using Babylon JS engine
- `show 3D scene [ISVISIBLE]` - Toggle 3D scene visibility
- `when 3D scene is initialized` - Hat block triggered when scene is ready
- `set scene background color [COLOR]` - Set background color
- `set scene fog [MODE] [COLOR] start (STARTDISTANCE) end (FULLDISTANCE) density (DENSITY)` - Add fog effects

### Camera Controls
- `add orbit camera distance (D) v-angle (V) h-angle (H) panning speed ratio (S) inputs key [KEY] pointer [POINTER] active [ACTIVE] as [NAME]` - Add arc-rotate camera
- `add follow camera distance (D) z offset (ZOFFSET) v-angle (V) h-angle (H) direction lock [LOCKTYPE] see-through (SEETHROUGH)% active [ISACTIVE] as [NAME]` - Add camera that follows target
- `set camera distance (D) v-angle (V) h-angle (H) z offset (OFFSET) target xyz (X) (Y) (Z) in (T) seconds` - Update camera properties
- `set camera distance (D) [NORS] (0)° (0)' (0)" [EORW] (0)° (0)' (0)" in (T) seconds` - Position camera on globe
- `configure camera radius min (MINRADIUS) max (MAXRADIUS) visible range min (MINRANGE) max (MAXRANGE) v-angle min (MINVANGLE) max (MAXVANGLE) speed ratio panning (PANNINGSPEEDRATIO) angular (ANGULARSPEEDRATIO)` - Configure camera limits
- `set camera target xyz (X) (Y) (Z)` - Set camera target position
- `set camera target object [OBJECTNAME] offset xyz (OFFSETX) (OFFSETY) (OFFSETZ)` - Target camera at object
- `set [OBJECTNAME] as parent of camera` - Set object as camera parent
- `camera [PROPERTY]` - Get camera property
- `get camera direction [FACE]` - Get camera direction
- `get camera view position for xyz (X) (Y) (Z)` - Convert 3D to screen position
- `lock pointer [DOLOCK]` - Lock/unlock mouse pointer
- `set display region bottom (B)% left (L)% width (W)% height (H)% border width (BORDERWIDTH) color [BORDERCOLOR] for camera [NAME]` - Set viewport region

### Lighting
- `add point light [COLOR] at xyz (X) (Y) (Z) intensity (INTENSITY) show position [SHOW] as [NAME]` - Add point light
- `add directional light [COLOR] in direction xyz (DIRX) (DIRY) (DIRZ) at xyz (POSX) (POSY) (POSZ) intensity (INTENSITY) as [NAME]` - Add directional/sun light
- `add ambient light [COLOR] sky direction xyz (DIRX) (DIRY) (DIRZ) intensity (INTENSITY) as [NAME]` - Add hemispheric ambient light
- `add spot light [COLOR] at xyz (X) (Y) (Z) open angle (ANGLE) intensity (INTENSITY) blur (BLUE) show position [SHOW] as [NAME]` - Add spotlight
- `remove all lights` - Remove all lights
- `remove light named [NAME]` - Remove specific light
- `switch [ONOFF] light named [NAME]` - Toggle light on/off
- `exclude object [OBJNAME] from light named [LIGHTNAME]` - Exclude object from lighting

### Shadows & Effects
- `cast shadow [DOCAST] from light named [NAME] blur size (BLUE)` - Configure shadow casting
- `receives shadow [DORECEIVE]` - Enable shadow receiving
- `create glow layer intensity (INTENSITY) blur size (BLUR) as [NAME]` - Create glow effect layer
- `add to glow layer named [NAME]` - Add object to glow layer
- `remove from glow layer named [NAME]` - Remove from glow layer
- `create highlight layer blur size (BLUR) as [NAME]` - Create highlight layer
- `add highlight in [COLOR] to layer named [NAME]` - Add highlight to object
- `remove from highlight layer named [NAME]` - Remove highlight

### Post-Processing
- `add pipeline vignette (VRADIUS) [COLOR] bloom strength (BSTRENGTH) threshold (BTHRESHOLD)% kernel (BKERNEL) antialiasing [ISANTIALIASING] sharpening [ISSHARPENING] camera contrast (C) exposure (E)` - Add post-processing effects
- `remove pipeline` - Remove post-processing

### Environment & Sky
- `set sky [SKYTYPE]` - Set skybox
- `remove sky` - Remove skybox
- `set clipping plane [PLANEID] direction xyz (X) (Y) (Z) offset (OFFSET)` - Set clipping plane
- `remove clipping plane [PLANEID]` - Remove clipping plane

### Input Controls
- `add [SIDE] joystick [COLOR1] [COLOR2] scale [SCALE]` - Add virtual joystick
- `[SIDE] joystick [PROPERTY]` - Read joystick property
- `remove all joysticks` - Remove joysticks

### Utilities
- `show 3D axis [SHOW] length (LENGTH)` - Show/hide 3D axis
- `turn [ONOFF] webcam background [WHICHCAMERA] in [FLIPMODE] mode` - Use webcam as background
- `GPU Available` - Check GPU support
- `switch to full screen [BORDERTYPE]` - Enter fullscreen mode

---

## 2. 3D OBJECTS - PRIMITIVES & SHAPES (50 blocks)

### Basic Shapes
- `add box [COLOR] size in x (SIZEX) y (SIZEY) z (SIZEZ) edge radius (R) as [NAME]` - Add box
- `add 6-colored box [COLOR1] [COLOR2] [COLOR3] [COLOR4] [COLOR5] [COLOR6] size in x (SIZEX) y (SIZEY) z (SIZEZ) as [NAME]` - Add box with colored faces
- `add sphere [COLOR] size in x (SIZEX) y (SIZEY) z (SIZEZ) arc (ARC) slice (SLICE) sides (SIDES) as [NAME]` - Add sphere
- `add cylinder [COLOR] diameter top (DIAMETERTOP) bottom (DIAMETERBOTTOM) height (HEIGHT) arc (ARC) closed section [CLOSEDSECTION] cap type [CAPTYPE] sides (SIDES) as [NAME]` - Add cylinder
- `add capsule [COLOR] diameter top (TOPD) bottom (BOTTOMD) height (H) sides (SIDES) as [NAME]` - Add capsule
- `add torus [COLOR] diameter (D) thickness (THICKNESS) sides (SIDES) as [NAME]` - Add torus
- `add plane [COLOR] size x (SIZEX) y (SIZEY) as [NAME]` - Add plane
- `add plane [COLOR] width (W) height (H) coefficients abcd (A) (B) (C) (D) as [NAME]` - Add plane from equation

### Advanced Shapes
- `add tube [COLOR] diameter top (TOPD) bottom (BOTTOMD) height (H) arc (ARC) closed section [SECTIONTYPE] cap type [CAPTYPE] sides (SIDES) thickness (THICKNESS) as [NAME]` - Add tube
- `add rectangle tube [COLOR] size in X (SIZEX) Y (SIZEY) height (H) cap type [CAPTYPE] thickness (THICKNESS) sides [SIDECOUNT] as [NAME]` - Add rectangular tube
- `add stairs [COLOR] width (W) depth (D) height (H) count (COUNT) thickness (THICKNESS) type [TYPE] as [NAME]` - Add stairs
- `add column [COLOR] 2D vertex list [LISTNAME] height (H) cap type [CAPTYPE] as [NAME]` - Extrude 2D shape vertically
- `add cone [COLOR] vertex list [LISTNAME] height (H) as [NAME]` - Add cone from vertex list

### Lines & Curves
- `add line [COLOR] diameter (DIAMETER) cap [CAP] arrow [ARROW] sides (SIDES) xyz from (X1) (Y1) (Z1) to (X2) (Y2) (Z2) segments (SEGMENTS) as [NAME]` - Add line
- `add dotted line [COLOR] diameter (DIAMETER) segment length (SEGMENTLENGTH) gap length (GAPLENGTH) cap [CAP] arrow [ARROW] sides (SIDES) from xyz (X1) (Y1) (Z1) to xyz (X2) (Y2) (Z2) as [NAME]` - Add dotted line
- `generate arc points from (X1) (Y1) (Z1) via (X2) (Y2) (Z2) to (X3) (Y3) (Z3) into list [LISTNAME] count (N)` - Generate arc points
- `add curve [COLOR] diameter (D) cap [CAPTYPE] arrow [ARROWTYPE] sides (S) using list [LISTNAME] from (STARTINDEX) to (ENDINDEX) segments (SEGMENTCOUNT) as [NAME]` - Add curve from points
- `add moving line between [OBJECT1] and [OBJECT2] [COLOR] diameter (D) sides (SIDES) as [NAME]` - Add line between moving objects

### Text
- `add 3D text [TEXT] font [FONT] color [COLOR] width (WIDTH) height (HEIGHT) diameter (DIAMETER) camera facing [CAMERAFACING] as [NAME]` - Add flat 3D text
- `add 3D thick text [TEXT] font [FONT] color [COLOR] width (WIDTH) height (HEIGHT) thickness (THICKNESS) diameter (DIAMETER) camera facing [CAMERAFACING] as [NAME]` - Add thick 3D text

### Models & Avatars
- `add model [MODELTYPE] target height (H) origin offset x (OFFSETX) y (OFFSETY) z (OFFSETZ) rotation x (RX) y (RY) z (RZ) hidden [HIDDEN] as [NAME]` - Add prebuilt model
- `add public object at URL [OBJECTURL] as [TYPE] target height (H) rotation (RX) (RY) (RZ) origin offset (OFFSETX) (OFFSETY) (OFFSETZ) as [NAME]` - Load model from URL (GLB/GLTF)
- `add community model [MODELNAME] target height (H) rotation (RX) (RY) (RZ) origin offset (OFFSETX) (OFFSETY) (OFFSETZ) as [NAME]` - Add community-shared model
- `add avatar [AVATARTYPE] height (H) as [NAME] hidden [ISHIDDEN]` - Add avatar
- `add avatar [AVATARNAME] for user [USERNAME] height (H) as [NAME] hidden [ISHIDDEN]` - Add user's avatar
- `add user avatar [AVATARNAME] height (HEIGHT) as [NAME]` - Add community avatar

### Geometry Tools
- `geometry: add point at xyz (X) (Y) (Z) color [COLOR] size (SIZE) on [PARENTNAME] as [NAME]` - Add point
- `geometry: add point between points [POINT1NAME] [POINT2NAME] at (RATIO)% color [COLOR] size (SIZE) as [NAME]` - Add point on line
- `geometry: add line between points [POINT1NAME] [POINT2NAME] color [COLOR] diameter (D) arrow [ARROWTYPE] sides (SIDES) segments (SEGMENTS) as [NAME]` - Add geometric line
- `geometry: add triangle from points [POINT1] [POINT2] [POINT3] color [COLOR] as [NAME]` - Add triangle
- `geometry: add frame box color [COLOR] size in x (X) y (Y) z (Z) thickness (T) labels [SHOWLABELS] as [NAME]` - Add wireframe box
- `geometry: add angle mark [POINT1NAME] [POINT2NAME] [POINT3NAME] size (S) color [COLOR] diameter (D) arrow [ARROWTYPE] sides (SIDES) label [LABELTEXT] as [NAME]` - Add angle marker

### Chemistry
- `chemistry: add atom [ATOMTYPE] as [MYNAME] connect hole [MYHOLELIST] to atom [OTHERNAME] hole [OTHERHOLELIST] distance (D)` - Add atom
- `chemistry: add custom atom [COLOR] size (S) holes [HOLELIST] label [LABEL] angle [LABELANGLE] as [MYNAME] connect hole [MYHOLELIST] to atom [OTHERATOM] hole [OTHERHOLELIST] distance (D)` - Add custom atom

### Special Objects
- `add voxel size in xyz (SX) (SY) (SZ) with costumes top [CTOP] bottom (CBOTTOM) front (CFRONT) back (CBACK) left (CLEFT) right (CRIGHT) texture size (T) sampling [METHOD] as [NAME]` - Add voxel/textured box
- `extrude costume [COSTUMENAME] thickness (T) scaling factor (SCALE) side color [COLOR] granularity (G) as [NAME]` - Extrude 2D costume
- `add transformer as [NAME]` - Add transform node (parent container)

### Object Management
- `remove object named [NAME]` - Remove object
- `remove all objects` - Remove all objects
- `object [NAME] exists` - Check if object exists
- `show local axis [SHOW] length (LENGTH)` - Show object's local coordinate axis

### Hierarchy
- `set object [OBJECTNAME] from sprite [SPRITENAME] as parent and update position/scale [DOUPDATE]` - Set parent object
- `set camera as parent` - Make camera the parent
- `unlink all children` - Remove all children
- `unlink parent` - Remove parent relationship

### Advanced
- `convert to sps at xyz from list [LISTNAME] updatable [ISUPDATABLE]` - Convert to solid particle system
- `add to sps [NAME] at xyz from list [LIST]` - Add instances to SPS
- `[PROPERTY] of object [OBJECTNAME] from sprite [SPRITENAME]` - Get object property
- `set property [PROPERTYNAME] to [VALUE] for [OBJNECTNAME]` - Set object property
- `property [PROPERTYNAME] of [OBJECTNAME]` - Get property value

---

## 3. 3D ACTIONS - MOVEMENT & INTERACTION (51 blocks)

### Position & Movement
- `move to x (X) y (Y) z (Z) in (T) seconds [ISBLOCKING]` - Move to position
- `move (DISTANCE) along current direction in (T) seconds [ISBLOCKING]` - Move forward
- `set speed [SPEEDTYPE] to (N)` - Set movement speed
- `copy position from camera` - Copy camera position
- `copy position from object [NAME]` - Copy object position

### Rotation
- `rotate to angle (A) around the [AXIS] axis in (T) seconds [ISBLOCKING]` - Rotate to angle
- `rotate to direction x (ANGLEX) y (ANGLEY) z (ANGLEZ) in (T) seconds [ISBLOCKING]` - Rotate to direction
- `turn (N) degrees around the [AXIS] axis in (T) seconds [ISBLOCKING]` - Turn by degrees
- `point to position x (PX) y (PY) z (PZ) in (T) seconds [ISBLOCKING]` - Point to position
- `copy direction from camera` - Copy camera direction
- `copy direction from object [NAME]` - Copy object direction

### Object Selection
- `select sprite object by name [NAME]` - Select object to work with
- `sprite object name` - Get current sprite object name

### Animations (Models & Avatars)
- `add animations [ANIMATIONLIST]` - Add animations to avatar
- `start animation [NAME] looping [ISLOOPING] progress from (PSTART) to (PEND) speed ratio (SPEEDRATIO) [BLOCKINGMODE] offset x (OFFSETX) y (OFFSETY) z (OFFSETZ) broadcast [MESSAGELIST] at progress [PROGRESSPOINTLIST]` - Start avatar animation
- `start model animation [NAME] looping [ISLOOPING] progress from (PSTART) to (PEND) speed ratio (SPEEDRATIO) [BLOCKINGMODE] offset x (OFFSETX) y (OFFSETY) z (OFFSETZ) broadcast [MESSAGELIST] at progress [PROGRESSPOINTLIST]` - Start model animation

### Skeleton/Bones
- `attach to body part [PARTNAME] of [AVATARNAME] from sprite [SPRITENAME] target height (H)` - Attach to avatar bone
- `detach from body` - Detach from bone
- `update bone [BONENAME] move in x (MOVEX) y (MOVEY) z (MOVEZ) rotate in x (ROTATEX) y (ROTATEY) z (ROTATEZ)` - Update bone transformation

### Collision Detection (Raycast)
- `turn on [ISBLOCKING] collision with [SPRITENAME] collider z offset (ZOFFSET) precision [PRECISIONTYPE] debug [ISDEBUG]` - Enable collision detection
- `broadcast [MESSAGE] on collision between [OBJECTNAME1] from [SPRITENAME1] and [OBJECTNAME2] from [SPRITENAME2]` - Broadcast on collision
- `when colliding with [SPRITENAME]` - Hat block for collision
- `update collider dimension x (SIZEX) y (SIZEY) z (SIZEZ) collider z offset (ZOFFSET) sensing range x (RANGEX) y (RANGEY) z (RANGEZ) color [COLOR]` - Update collider box
- `sprite object blocked [DIRECTION]` - Check if blocked

### Proximity Detection
- `broadcast [MESSAGE] when [OBJECTNAME1] from [SPRITENAME1] and [OBJECTNAME2] from [SPRITENAME2] overlap` - Broadcast on overlap
- `broadcast [MESSAGE] when [DIMENSION] distance dlte (D) between [OBJECTNAME1] from [SPRITENAME1] and [OBJECTNAME2] from [SPRITENAME2]` - Broadcast when distance threshold met
- `distance between objects [OBJECT1] and [OBJECT2]` - Get distance between objects

### Distance Sensors
- `set distance sensor front [ONOFFFRONT] back [ONOFFBACK] left [ONOFFLEFT] right [ONOFFRIGHT] down [ONOFFDOWN] up [ONOFFUP] max distance (MAXD) count [COUNT] visible [ISVISIBLE]` - Configure distance sensors
- `name of nearest obstacle in the [DIRECTION] direction for [OBJECTNAME]` - Get nearest obstacle name
- `distance to nearest obstacle in the [DIRECTION] direction for [OBJECTNAME]` - Get distance to obstacle

### Picking (Mouse/Touch Interaction)
- `turn on picking with [BUTTON] for objects created in sprites [SPRITELIST] on [POINTERACTION]` - Enable object picking
- `turn off picking for objects created in sprites [SPRITELIST]` - Disable picking
- `when an object from this sprite is picked` - Hat block for picking
- `picked object name` - Get picked object name
- `picked point x pos` - Get picked X position
- `picked point y pos` - Get picked Y position
- `picked point z pos` - Get picked Z position

### Hovering
- `turn on hovering for objects created in sprites [SPRITELIST]` - Enable hover detection
- `turn off hovering for objects created in sprites [SPRITELIST]` - Disable hovering
- `hovered object name` - Get hovered object
- `hovered point x pos` - Get hover X position
- `hovered point y pos` - Get hover Y position
- `hovered point z pos` - Get hover Z position

### Dragging
- `set dragging mode [DRAGGINGMODE] direction X (DX) Y (DY) z (DZ)` - Configure drag mode
- `set dragging limits min xyz (MINX) (MINY) (MINZ) max xyz (MAXX) (MAXY) (MAXZ)` - Set drag limits
- `when an object from this sprite is being dragged` - Hat block during drag
- `when an object from this sprite stops being dragged` - Hat block on drag end
- `when an object from this sprite starts to be dragged` - Hat block on drag start
- `dragged object name` - Get dragged object name

### Utilities
- `show speech bubble [TEXT] offset xyz (X) (Y) (Z) max width (W) text font [FONTNAME] size (FONTSIZE) color [FONTCOLOR] background [BGCOLOR] for [T] seconds camera facing [ISCAMERAFACING] ID [BUBBLEID]` - Display speech bubble
- `map screen XY (X) (Y) to XYZ position on object [OBJECTNAME]` - Convert 2D to 3D position

---

## 4. 3D TOOLS - MATERIALS & UTILITIES (32 blocks)

### Materials - Color & Texture
- `update color diffusion [DIFFUSIONCOLOR] emission [EMISSIONCOLOR] roughness (R) brightness (B) remove texture [DOREMOVE] area [AREATYPE]` - Update material colors
- `update texture [TEXTURENAME] unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [All]` - Apply texture from library
- `update texture using costume [COSTUMENAME] unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [AREATYPE]` - Apply costume as texture
- `add texture with shared file [IMAGEURL] box unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [AREATYPE]` - Apply texture from URL
- `apply grid material face [FACECOLOR] line [LINECOLOR] density (D) minor line visibility (V) line offset xyz (OFFSETX) (OFFSETY) (OFFSETZ)` - Apply grid material
- `get [COLORTYPE] color of object named [NAME]` - Get object color

### Material Settings
- `material setting: wireframe mode [ISWIREMODE] draw back face [DODRAW] z-offset (OFFSETZ) log depth [ISLOG] transparent [HASTRANSPARENCY]` - Configure material properties
- `set rendering layer [ID]` - Set rendering order

### Scale & Size
- `update scale x (SX)% y (SY)% z (SZ)% in (T) seconds [BLOCKINGTYPE]` - Scale object (percentage)
- `update size x (SX) y (SY) z (SZ)` - Set absolute size

### Object Copying
- `copy object share data [ISSHARING] as [NAME]` - Clone object
- `copy by matrix count in xyz (COUNTX) (COUNTY) (COUNTZ) spacing in xyz (SPACINGX) (SPACINGY) (SPACINGZ) random ratio in spacing (SPACINGR)% scale (SCALINGR)% z-rotation (ZROTATIONR)% [SUBSET] object [SUBSETOBJECT]` - Create matrix of copies
- `copy by matrix from center count in xyz (COUNTX) (COUNTY) (COUNTZ) spacing in xyz (SPACINGX) (SPACINGY) (SPACINGZ) random ratio in spacing (SPACINGR)% scale (SCALINGR)% z-rotation (ZROTATIONR)% [SUBSET] object [SUBSETOBJECT]` - Create centered matrix
- `copy to mirror position [TYPE]` - Mirror copy
- `copy to rotated position around the [AXISNAME] axis count (N) degree step (STEP) shift XYZ (SHIFTX) (SHIFTY) (SHIFTZ)` - Rotational copy
- `for each 3D object named [VARIABLENAME]` - Iterate through copies

### Mesh Operations
- `carve [STARTINGOBJECT] with [CARVINGOBJECT]` - Boolean subtraction
- `merge [OBJECTNAME1] into [OBJECTNAME2]` - Merge objects
- `convert to flat shading` - Convert to flat shading
- `subdivide faces by (N)` - Subdivide mesh
- `update vertices scale xyz (SX) (SY) (SZ) move xyz (MX) (MY) (MZ) position min xyz (MINX) (MINY) (MINZ) max xyz (MAXX) (MAXY) (MAXZ)` - Transform vertices
- `bake current transformations` - Bake transformations

### Mirror Reflections
- `build mirror brightness (B) using object named [NAME]` - Convert object to mirror
- `reflect in mirror [NAME]` - Make object visible in mirror
- `remove all reflections in mirror [NAME]` - Clear mirror reflections

### Camera Facing
- `set camera facing mode [MODE]` - Set billboard mode

### Visualization
- `show bounding box [ISSHOWN]` - Show/hide bounding box
- `show edges [ISSHOWN] color [COLOR] thickness (THICKNESS)` - Show/hide edges
- `show skeleton [ISSHOWN]` - Show/hide skeleton

### Export
- `export object [NAME] as a GLB file` - Export as GLB
- `export object [NAME] as an STL file` - Export as STL

---

## 5. 3D PHYSICS (36 blocks)

### Physics Setup
- `enable physics for scene with gravity (GRAVITY)` - Initialize physics engine
- `update gravity for scene to (GRAVITY)` - Change gravity
- `set physics frame rate [RATE]` - Set physics update rate
- `get physics frame rate` - Get physics frame rate

### Physics Bodies
- `add [SHAPE] physics body with mass (MASS) restitution (RESTITUTION)% friction (FRICTION)% frozen [ISFROZEN] debug [ISDEBUG] [COLOR]` - Add physics body
- `update physics property restitution (RESTITUTION)% friction (FRICTION)%` - Update physics properties
- `remove physics body` - Remove physics body
- `freeze physics body named [NAME] [ISFROZEN]` - Freeze/unfreeze body
- `freeze all physics bodys [ISFROZEN]` - Freeze/unfreeze all
- `add physics bodies of [CHILDRENNAMELIST] into compound [NAME] keep object [KEEPOBJ]` - Create compound body

### Movement & Forces
- `set physics body speed in facing direction (SPEED) for [NAME]` - Set forward speed
- `set physics body speed (SPEED) towards target xyz (X) (Y) (Z) for [NAME]` - Set speed toward position
- `set physics body speed (SPEED) for [NAME] towards object [TARGETNAME] from sprite [SPRITENAME]` - Set speed toward object
- `set physics body speed in xyz (MX) (MY) (MZ) for [NAME]` - Set linear velocity
- `apply force strength (SIZE) direction xyz (X) (Y) (Z) at relative point xyz (X2) (Y2) (Z2) to [NAME]` - Apply force
- `apply impulse strength (SIZE) direction xyz (X) (Y) (Z) at relative point xyz (X2) (Y2) (Z2) to [NAME]` - Apply impulse

### Rotation
- `set physics body rotation speed around xyz axes (RX) (RY) (RZ) for [NAME]` - Set angular velocity

### Constraints & Limits
- `set physics body damping for movement (MD)% rotation (RD)% for [NAME]` - Set damping
- `set physics body movement speed limit (LIMIT) allow direction X [ALLOWX] Y [ALLOWY] Z [ALLOWZ] for [NAME]` - Limit linear velocity
- `set physics body rotation speed limit (LIMIT) allow axis X [ALLOWX] Y [ALLOWY] Z [ALLOWZ] for [NAME]` - Limit angular velocity
- `lock physics body speed in X (MX) Y (MY) Z (MZ) rotation around X (RX) Y (RY) Z (RZ) for [NAME]` - Lock axes

### Joints/Constraints
- `add distance constraint between bodies of [OBJECTNAME] from [SPRITENAME] and [OBJECTNAME2] from [SPRITENAME2] named [JOINTNAME]` - Fixed distance joint
- `add fixed constraint between bodies of [OBJECTNAME] from [SPRITENAME] and [OBJECTNAME2] from [SPRITENAME2] named [JOINTNAME]` - Fixed position joint
- `add hinge constraint between bodies of [OBJECTNAME] from [SPRITENAME] at point x (X2) y (Y2) z (Z2) axis x (X) y (Y) z (Z) and [OBJECTNAME2] from [SPRITENAME2] at point x (X4) y (Y4) z (Z4) axis x (X3) y (Y3) z (Z3) named [JOINTNAME]` - Hinge joint
- `set limits for hinge constraint named [NAME] angle between (LOW) and (HIGH) softness (SOFT) bias factor (BIAS) relaxation (RELAX)` - Configure hinge limits
- `set speed (SPEED) for hinge constraint named [NAME]` - Set hinge motor speed
- `remove constraint named [JOINTNAME]` - Remove joint

### Collision Groups
- `update collision group [COLLISIONGROUP] target groups [TARGETGROUPS] for [NAME]` - Set collision groups
- `broadcast [BROADCASTMESSAGE] on collision between physics bodies of [NAME] from [SPRITENAME] and [NAME2] from [SPRITENAME2]` - Broadcast on physics collision
- `names of physics bodies in contact for [NAME]` - Get colliding bodies

### Car Physics
- `enable car simulation mass (MASS) restitution (RESTITUTION)% friction (BODYFRICTION)% tire friction (FRICTION)% suspension (SUSPENSION) for [NAME]` - Convert to car
- `set car engine force (ENGINEFORCE) brake level (BRAKEFORCE) % for [NAME]` - Control car engine
- `steer car to angle (A) for [NAME]` - Steer car
- `set car wheel angle LF (LF) RF (RF) LB (LB) RB (RB) for [NAME]` - Set individual wheel angles
- `set car wheel engine force LF (LF) RF (RF) LB (LB) RB (RB) brake level (BRAKE)% for [NAME]` - Control individual wheels

### Data
- `get physics body [PROPERTY] for [NAME]` - Get physics property

---

## 6. 3D EFFECTS - PARTICLES & TRAILS (18 blocks)

### Particle Emitters - Prebuilt
- `add prebuilt emitter for [TYPE] [COLOR1] [COLOR2] capacity (C) texture size (TEXTURESIZE) source size (SOURCESIZE) speed (SPEED) max life (MAXLIFE) as [NAME]` - Add prebuilt particle system

### Particle Emitters - Custom
- `add particle emitter shape [SHAPETYPE] texture [TEXTURE] facing camera [FACINGCAM] life min (MINLIFE) max (MAXLIFE) capacity (C) GPU [USEGPU] time ratio (TIMERATIO)% as [NAME]` - Create custom emitter

### Emitter Shape Configuration
- `configure box emitter [NAME]: min xyz (MINX) (MINY) (MINZ) max xyz (MAXX) (MAXY) (MAXZ)` - Configure box emitter
- `configure cone emitter [NAME]: radius (R) angle (A) radius range (RR) height range (HR)` - Configure cone emitter
- `configure cylinder emitter [NAME]: radius (RADIUS) range (RANGE) height (H) direction randomness (R)%` - Configure cylinder emitter
- `configure hemispheric emitter [NAME]: radius (RADIUS) range (RANGE)` - Configure hemispheric emitter
- `configure sphere emitter [NAME]: radius (RADIUS) range (RANGE)` - Configure sphere emitter
- `configure mesh emitter [NAME]: use mesh normal direction [USENORMAL]` - Configure mesh emitter

### Emitter Properties
- `configure emitter [NAME] color: start [STARTCOLOR1] to [STARTCOLOR2] end [ENDCOLOR1] to [ENDCOLOR2] at progress (MIDDLE)% [MIDDLECOLOR1] to [MIDDLECOLOR2]` - Set particle colors
- `configure emitter [NAME] size: start (STARTS1) to (STARTS2) end (ENDS1) to (ENDS2) at progress (MIDDLE)% (MIDDLES1) to (MIDDLES2)` - Set particle size
- `configure emitter [NAME] scale: x min (MINX)% max (MAXX)% y min (MINY)% max (MAXY)%` - Set particle scale
- `configure emitter [NAME] movement: speed min (MINS) max (MAXS) direction 1 (X1) (Y1) (Z1) direction 2 (X2) (Y2) (Z2)` - Set particle movement
- `configure emitter [NAME] rotation speed: start (STARTS1) to (STARTS2) end (ENDS1) to (ENDS2) at progress (MIDDLE)% (MIDDLES1) to (MIDDLES2)` - Set rotation speed
- `configure emitter [NAME] initial rotation: min (MINR) max (MAXR)` - Set initial rotation
- `configure emitter [NAME] blend mode [MODE]` - Set blend mode

### Emitter Control
- `start emitter [NAME] [RATETYPE] of (N)` - Start particle emission
- `[ACTION] emitter [NAME]` - Control emitter (start/stop/pause/etc.)

### Trails
- `add trail diffusion [DIFFUSECOLOR] emission [EMISSIONCOLOR] width (W) segments (N) as [NAME]` - Add motion trail

---

## 7. 3D AR/VR (5 blocks)

### AR Camera Modes
- `switch to AR world camera scale (S) emulation mode [ISEMULATION]` - AR with back camera (world tracking)
- `switch to AR face camera show marker [SHOW] scale (S) emulation mode [ISEMULATION] data table [TABLENAME] with mesh of face [SHOWFACE] eyes [SHOWEYE] mouth [SHOWMOUTH] lips [SHOWLIP]` - AR with face tracking
- `switch to AR LOGO as [TYPE] camera [CAMTYPE] marker [SHOW] scale (S) emulation [ISEMULATION]` - AR with logo/image tracking

### AR Features
- `convert to transparent occlusion` - Make object occlude AR but invisible

### Developer Tools
- `show inspector [SHOW]` - Show Babylon.js inspector

---

## KEY FEATURES SUMMARY

### Scene Management
- Babylon.js-based 3D engine
- Scene initialization, visibility control
- Background color, fog effects
- Skybox, clipping planes
- Post-processing pipeline (bloom, vignette, antialiasing, etc.)

### Objects & Shapes
- **Primitives**: Box, Sphere, Cylinder, Capsule, Torus, Plane
- **Advanced**: Tube, Stairs, Column (extrusion), Cone
- **Lines**: Solid, dotted, curves, arcs
- **Text**: Flat and thick 3D text
- **Models**: GLB/GLTF loading, prebuilt models, community models
- **Avatars**: Character models with animations
- **Geometry**: Points, lines, triangles, angle markers
- **Chemistry**: Molecular structures
- **Voxels**: Textured boxes with per-face costumes
- **Extrusion**: Convert 2D costumes to 3D

### Camera System
- **Types**: Orbit (arc-rotate), Follow, Custom viewports
- **Controls**: Keyboard, mouse, joystick
- **Properties**: Distance, angles, target, limits
- **Parent**: Can follow objects or have objects follow it

### Lighting
- **Types**: Point, Directional, Ambient (hemispheric), Spot
- **Features**: Intensity, color, shadows, exclusion
- **Effects**: Glow layers, highlight layers

### Materials & Textures
- Color (diffusion, emission, roughness, brightness)
- Texture library, costume textures, URL textures
- Grid materials
- Wireframe, transparency, back-face culling
- Mirror reflections

### Movement & Transformation
- Position (x, y, z coordinates)
- Rotation (individual axes or combined)
- Scale (percentage or absolute)
- Animated transitions with duration
- Speed-based movement
- Parent-child hierarchies

### Animations
- Avatar animations (library)
- Model animations (embedded in GLB/GLTF)
- Animation control (loop, speed, progress range)
- Broadcast messages at animation points

### Interaction
- **Picking**: Click/tap to select objects
- **Hovering**: Mouse-over detection
- **Dragging**: Drag objects with constraints
- **Screen-to-3D**: Convert screen coordinates to 3D positions

### Collision & Detection
- **Raycast collision**: Blocking collision with sprites
- **Overlap detection**: Bounding box overlap
- **Distance sensors**: Detect obstacles in 6 directions
- **Proximity**: Distance-based triggers
- **Physics collision**: Physics-based collision detection

### Physics Engine
- **Bodies**: Box, sphere, cylinder, mesh shapes
- **Properties**: Mass, friction, restitution
- **Forces**: Apply force, impulse
- **Constraints**: Fixed, distance, hinge joints
- **Car simulation**: 4-wheel vehicle physics
- **Collision groups**: Layer-based collision filtering

### Particle Effects
- **Shapes**: Box, cone, cylinder, sphere, hemispheric, mesh
- **Properties**: Color gradient, size, scale, rotation
- **GPU particles**: Hardware acceleration
- **Prebuilt effects**: Fire, smoke, etc.
- **Trails**: Motion trails

### Advanced Features
- **Bone/Skeleton**: Attach to avatar body parts, bone manipulation
- **SPS**: Solid Particle System for many instances
- **Matrix copying**: Create grids of objects
- **Mirror/Rotation copying**: Symmetrical arrangements
- **Mesh operations**: Boolean (carve), merge, subdivide
- **Vertex manipulation**: Direct vertex transformation
- **Export**: GLB, STL file export

### AR/VR
- AR world tracking (device camera)
- AR face tracking with mesh
- AR image/logo tracking
- Occlusion objects
- Babylon.js inspector

### Input & Controls
- Virtual joysticks (left/right)
- Keyboard input
- Mouse/pointer input
- Pointer lock
- Webcam background

### Coordinate System
- X: Left/Right (right is positive)
- Y: Forward/Backward (forward is positive)
- Z: Up/Down (up is positive)

### Performance
- GPU particle systems
- Instancing for copies
- Level of detail (rendering layers)
- Frustum culling
- Hardware acceleration check

---

## CONCLUSION

CreatiCode provides **239 3D blocks** across **7 categories**, offering comprehensive 3D development capabilities including:

1. **Scene Management** - Full control over scene setup, cameras, lighting, and environment
2. **Rich Object Library** - Primitives, complex shapes, models, avatars, text, geometry, chemistry
3. **Advanced Materials** - Colors, textures, grid materials, reflections, wireframe
4. **Robust Physics** - Full physics engine with bodies, forces, constraints, car simulation
5. **Particle Systems** - Custom and prebuilt particle emitters with extensive configuration
6. **Interaction System** - Picking, hovering, dragging, collision detection, distance sensors
7. **Animation Support** - Avatar animations, model animations, bone manipulation
8. **AR Features** - World tracking, face tracking, image tracking
9. **Export Capabilities** - GLB and STL export
10. **Performance Tools** - GPU particles, instancing, rendering layers

This is a **production-ready 3D engine** built on Babylon.js, suitable for games, simulations, visualizations, AR experiences, and educational projects.
