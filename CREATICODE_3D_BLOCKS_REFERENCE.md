# CreatiCode 3D Blocks - Complete Reference

Based on analysis of `/media/binyu/USB2/ScratchCopilot/blockdes8.txt`

## Summary
- **Total 3D Blocks**: 239
- **Categories**: 7

---

## Category Breakdown

### 1. 3D Scene (47 blocks)
Scene initialization, camera controls, lighting, environment effects, and scene-wide settings.

**Scene Setup:**
- initialize 3D scene [SCENETYPE] as hidden [ISHIDDEN v]
- show 3D scene [ISVISIBLE]
- when 3D scene is initialized
- set scene background color [COLOR]
- set scene fog [MODE v] [COLOR] start (STARTDISTANCE) end (FULLDISTANCE) density (DENSITY)
- set sky [SKYTYPE]
- remove sky
- set clipping plane [PLANEID v] direction xyz (X) (Y) (Z) offset (OFFSET)
- remove clipping plane [PLANEID v]
- add pipeline vignette (VRADIUS) [COLOR] bloom strength (BSTRENGTH) threshold (BTHRESHOLD)% kernel (BKERNEL) antialiasing [ISANTIALIASING] sharpening [ISSHARPENING] camera contrast (C) exposure (E)
- remove pipeline
- lock pointer [DOLOCK]
- show 3D axis [SHOW v] length (LENGTH)
- turn [ONOFF v] webcam background [WHICHCAMERA v] in [FLIPMODE v] mode
- switch to full screen [BORDERTYPE v]
- GPU Available

**Camera Controls:**
- set [OBJECTNAME] as parent of camera
- set camera target xyz (X) (Y) (Z)
- set camera target object [OBJECTNAME] offset xyz (OFFSETX) (OFFSETY) (OFFSETZ)
- set display region bottom (B)% left (L)% width (W)% height (H)% border width (BORDERWIDTH) color [BORDERCOLOR] for camera [NAME]
- add orbit camera distance (D) v-angle (V) h-angle (H) panning speed ratio (S) inputs key [KEY] pointer [POINTER] active [ACTIVE] as [NAME]
- set camera distance (D) v-angle (V) h-angle (H) z offset (OFFSET) target xyz (X) (Y) (Z) in (T) seconds
- set camera distance (D) [NORS] (0)° (0)' (0)" [EORW] (0)° (0)' (0)" in (T) seconds
- configure camera radius min (MINRADIUS) max (MAXRADIUS) visible range min (MINRANGE) max (MAXRANGE) v-angle min (MINVANGLE) max (MAXVANGLE) speed ratio panning (PANNINGSPEEDRATIO) angular (ANGULARSPEEDRATIO)
- add follow camera distance (D) z offset (ZOFFSET) v-angle (V) h-angle (H) direction lock [LOCKTYPE v] see-through (SEETHROUGH)% active [ISACTIVE v] as [NAME]
- camera [PROPERTY v]
- get camera direction [FACE v]
- get camera view position for xyz (X) (Y) (Z)

**Lighting:**
- add point light [COLOR] at xyz (X) (Y) (Z) intensity (INTENSITY) show position [SHOW v] as [NAME]
- add directional light [COLOR] in direction xyz (DIRX) (DIRY) (DIRZ) at xyz (POSX) (POSY) (POSZ) intensity (INTENSITY) as [NAME]
- add ambient light [COLOR] sky direction xyz (DIRX) (DIRY) (DIRZ) intensity (INTENSITY) as [NAME]
- add spot light [COLOR] at xyz (X) (Y) (Z) open angle (ANGLE) intensity (INTENSITY) blur (BLUE) show position [SHOW v] as [NAME]
- cast shadow [DOCAST v] from light named [NAME] blur size (BLUE)
- receives shadow [DORECEIVE v]
- remove all lights
- remove light named [NAME]
- switch [ONOFF] light named [NAME]
- exclude object [OBJNAME] from light named [LIGHTNAME]

**Glow & Highlight Effects:**
- create glow layer intensity (INTENSITY) blur size (BLUR) as [NAME]
- add to glow layer named [NAME]
- remove from glow layer named [NAME]
- create highlight layer blur size (BLUR) as [NAME]
- add highlight in [COLOR] to layer named [NAME]
- remove from highlight layer named [NAME]

**Joystick Controls:**
- add [SIDE] joystick [COLOR1] [COLOR2] scale [SCALE]
- [SIDE] joystick [PROPERTY]
- remove all joysticks

---

### 2. 3D Object (50 blocks)
Creating, managing, and manipulating 3D objects and their hierarchies.

**Basic Shapes:**
- add box [COLOR] size in x (SIZEX) y (SIZEY) z (SIZEZ) edge radius (R) as [NAME]
- add 6-colored box [COLOR1] [COLOR2] [COLOR3] [COLOR4] [COLOR5] [COLOR6] size in x (SIZEX) y (SIZEY) z (SIZEZ) as [NAME]
- add sphere [COLOR] size in x (SIZEX) y (SIZEY) z (SIZEZ) arc (ARC) slice (SLICE) sides (SIDES) as [NAME]
- add cylinder [COLOR] diameter top (DIAMETERTOP) bottom (DIAMETERBOTTOM) height (HEIGHT) arc (ARC) closed section [CLOSEDSECTION v] cap type [CAPTYPE v] sides (SIDES) as [NAME]
- add tube [COLOR] diameter top (TOPD) bottom (BOTTOMD) height (H) arc (ARC) closed section [SECTIONTYPE v] cap type [CAPTYPE v] sides (SIDES) thickness (THICKNESS) as [NAME]
- add rectangle tube [COLOR] size in X (SIZEX) Y (SIZEY) height (H) cap type [CAPTYPE v] thickness (THICKNESS) sides [SIDECOUNT v] as [NAME]
- add capsule [COLOR] diameter top (TOPD) bottom (BOTTOMD) height (H) sides (SIDES) as [NAME]
- add torus [COLOR] diameter (D) thickness (THICKNESS) sides (SIDES) as [NAME]
- add cone [COLOR] vertex list [LISTNAME v] height (H) as [NAME]
- add column [COLOR] 2D vertex list [LISTNAME v] height (H) cap type [CAPTYPE v] as [NAME]

**Lines & Curves:**
- add line [COLOR] diameter (DIAMETER) cap [CAP v] arrow [ARROW v] sides (SIDES) xyz from (X1) (Y1) (Z1) to (X2) (Y2) (Z2) segments (SEGMENTS) as [NAME]
- add dotted line [COLOR] diameter (DIAMETER) segment length (SEGMENTLENGTH) gap length (GAPLENGTH) cap [CAP v] arrow [ARROW v] sides (SIDES) from xyz (X1) (Y1) (Z1) to xyz (X2) (Y2) (Z2) as [NAME]
- add curve [COLOR] diameter (D) cap [CAPTYPE v] arrow [ARROWTYPE v] sides (S) using list [LISTNAME v] from (STARTINDEX) to (ENDINDEX) segments (SEGMENTCOUNT) as [NAME]
- generate arc points from (X1) (Y1) (Z1) via (X2) (Y2) (Z2) to (X3) (Y3) (Z3) into list [LISTNAME v] count (N)
- add moving line between [OBJECT1] and [OBJECT2] [COLOR] diameter (D) sides (SIDES) as [NAME]

**Text Objects:**
- add 3D text [TEXT] font [FONT v] color [COLOR] width (WIDTH) height (HEIGHT) diameter (DIAMETER) camera facing [CAMERAFACING v] as [NAME]
- add 3D thick text [TEXT] font [FONT v] color [COLOR] width (WIDTH) height (HEIGHT) thickness (THICKNESS) diameter (DIAMETER) camera facing [CAMERAFACING v] as [NAME]

**Planes:**
- add plane [COLOR] size x (SIZEX) y (SIZEY) as [NAME]
- add plane [COLOR] width (W) height (H) coefficients abcd (A) (B) (C) (D) as [NAME]

**Complex Objects:**
- add stairs [COLOR] width (W) depth (D) height (H) count (COUNT) thickness (THICKNESS) type [TYPE v] as [NAME]
- add model [MODELTYPE] target height (H) origin offset x (OFFSETX) y (OFFSETY) z (OFFSETZ) rotation x (RX) y (RY) z (RZ) hidden [HIDDEN v] as [NAME]
- add public object at URL [OBJECTURL] as [TYPE v] target height (H) rotation (RX) (RY) (RZ) origin offset (OFFSETX) (OFFSETY) (OFFSETZ) as [NAME]
- add community model [MODELNAME] target height (H) rotation (RX) (RY) (RZ) origin offset (OFFSETX) (OFFSETY) (OFFSETZ) as [NAME]
- add voxel size in xyz (SX) (SY) (SZ) with costumes top [CTOP v] bottom (CBOTTOM v) front (CFRONT v) back (CBACK v) left (CLEFT v) right (CRIGHT v) texture size (T) sampling [METHOD v] as [NAME]
- extrude costume [COSTUMENAME v] thickness (T) scaling factor (SCALE) side color [COLOR] granularity (G) as [NAME]

**Avatars:**
- add avatar [AVATARTYPE] height (H) as [NAME] hidden [ISHIDDEN v]
- add avatar [AVATARNAME] for user [USERNAME] height (H) as [NAME] hidden [ISHIDDEN v]
- add user avatar [AVATARNAME] height (HEIGHT) as [NAME]

**Geometry Tools:**
- geometry: add point at xyz (X) (Y) (Z) color [COLOR] size (SIZE) on [PARENTNAME] as [NAME]
- geometry: add point between points [POINT1NAME] [POINT2NAME] at (RATIO)% color [COLOR] size (SIZE) as [NAME]
- geometry: add line between points [POINT1NAME] [POINT2NAME] color [COLOR] diameter (D) arrow [ARROWTYPE v] sides (SIDES) segments (SEGMENTS) as [NAME]
- geometry: add triangle from points [POINT1] [POINT2] [POINT3] color [COLOR] as [NAME]
- geometry: add frame box color [COLOR] size in x (X) y (Y) z (Z) thickness (T) labels [SHOWLABELS v] as [NAME]
- geometry: add angle mark [POINT1NAME] [POINT2NAME] [POINT3NAME] size (S) color [COLOR] diameter (D) arrow [ARROWTYPE v] sides (SIDES) label [LABELTEXT] as [NAME]

**Chemistry:**
- chemistry: add atom [ATOMTYPE v] as [MYNAME] connect hole [MYHOLELIST] to atom [OTHERNAME] hole [OTHERHOLELIST] distance (D)
- chemistry: add custom atom [COLOR] size (S) holes [HOLELIST] label [LABEL] angle [LABELANGLE] as [MYNAME] connect hole [MYHOLELIST] to atom [OTHERATOM] hole [OTHERHOLELIST] distance (D)

**Object Management:**
- remove object named [NAME]
- remove all objects
- add transformer as [NAME]
- set object [OBJECTNAME] from sprite [SPRITENAME v] as parent and update position/scale [DOUPDATE v]
- unlink all children
- unlink parent
- set camera as parent
- show local axis [SHOW v] length (LENGTH)
- object [NAME] exists
- convert to sps at xyz from list [LISTNAME v] updatable [ISUPDATABLE v]
- add to sps [NAME] at xyz from list [LIST v]

**Properties:**
- [PROPERTY v] of object [OBJECTNAME] from sprite [SPRITENAME]
- set property [PROPERTYNAME] to [VALUE] for [OBJNECTNAME]
- property [PROPERTYNAME] of [OBJECTNAME]

---

### 3. 3D Action (51 blocks)
Movement, rotation, interaction, collision detection, and object behaviors.

**Movement & Rotation:**
- move to x (X) y (Y) z (Z) in (T) seconds [ISBLOCKING v]
- rotate to angle (A) around the [AXIS v] axis in (T) seconds [ISBLOCKING v]
- rotate to direction x (ANGLEX) y (ANGLEY) z (ANGLEZ) in (T) seconds [ISBLOCKING v]
- turn (N) degrees around the [AXIS v] axis in (T) seconds [ISBLOCKING v]
- move (DISTANCE) along current direction in (T) seconds [ISBLOCKING v]
- point to position x (PX) y (PY) z (PZ) in (T) seconds [ISBLOCKING v]
- set speed [SPEEDTYPE v] to (N)
- distance between objects [OBJECT1] and [OBJECT2]

**Position & Direction Copying:**
- copy direction from camera
- copy position from camera
- copy position from object [NAME]
- copy direction from object [NAME]

**Speech Bubbles:**
- show speech bubble [TEXT] offset xyz (X) (Y) (Z) max width (W) text font [FONTNAME v] size (FONTSIZE) color [FONTCOLOR] background [BGCOLOR] for [T] seconds camera facing [ISCAMERAFACING v] ID [BUBBLEID v]

**Object Selection:**
- select sprite object by name [NAME]
- sprite object name

**Animations:**
- start model animation [NAME] looping [ISLOOPING v] progress from (PSTART) to (PEND) speed ratio (SPEEDRATIO) [BLOCKINGMODE v] offset x (OFFSETX) y (OFFSETY) z (OFFSETZ) broadcast [MESSAGELIST] at progress [PROGRESSPOINTLIST]
- add animations [ANIMATIONLIST]
- start animation [NAME] looping [ISLOOPING v] progress from (PSTART) to (PEND) speed ratio (SPEEDRATIO) [BLOCKINGMODE v] offset x (OFFSETX) y (OFFSETY) z (OFFSETZ) broadcast [MESSAGELIST] at progress [PROGRESSPOINTLIST]
- update bone [BONENAME v] move in x (MOVEX) y (MOVEY) z (MOVEZ) rotate in x (ROTATEX) y (ROTATEY) z (ROTATEZ)

**Avatar Attachment:**
- attach to body part [PARTNAME v] of [AVATARNAME] from sprite [SPRITENAME v] target height (H)
- detach from body

**Collision Detection:**
- turn on [ISBLOCKING v] collision with [SPRITENAME v] collider z offset (ZOFFSET) precision [PRECISIONTYPE v] debug [ISDEBUG v]
- broadcast [MESSAGE v] on collision between [OBJECTNAME1] from [SPRITENAME1 v] and [OBJECTNAME2] from [SPRITENAME2 v]
- when colliding with [SPRITENAME v]
- update collider dimension x (SIZEX) y (SIZEY) z (SIZEZ) collider z offset (ZOFFSET) sensing range x (RANGEX) y (RANGEY) z (RANGEZ) color [COLOR]
- sprite object blocked [DIRECTION v]
- broadcast [MESSAGE v] when [OBJECTNAME1] from [SPRITENAME1 v] and [OBJECTNAME2] from [SPRITENAME2 v] overlap
- broadcast [MESSAGE v] when [DIMENSION v] distance dlte (D) between [OBJECTNAME1] from [SPRITENAME1 v] and [OBJECTNAME2] from [SPRITENAME2 v]

**Distance Sensors:**
- set distance sensor front [ONOFFFRONT v] back [ONOFFBACK v] left [ONOFFLEFT v] right [ONOFFRIGHT v] down [ONOFFDOWN v] up [ONOFFUP v] max distance (MAXD) count [COUNT v] visible [ISVISIBLE v]
- name of nearest obstacle in the [DIRECTION v] direction for [OBJECTNAME]
- distance to nearest obstacle in the [DIRECTION v] direction for [OBJECTNAME]

**Picking (Selection):**
- turn on picking with [BUTTON v] for objects created in sprites [SPRITELIST] on [POINTERACTION v]
- turn off picking for objects created in sprites [SPRITELIST]
- picked point x pos
- picked point y pos
- picked point z pos
- picked object name
- when an object from this sprite is picked

**Hovering:**
- turn on hovering for objects created in sprites [SPRITELIST]
- turn off hovering for objects created in sprites [SPRITELIST]
- hovered object name
- hovered point x pos
- hovered point y pos
- hovered point z pos

**Dragging:**
- set dragging limits min xyz (MINX) (MINY) (MINZ) max xyz (MAXX) (MAXY) (MAXZ)
- set dragging mode [DRAGGINGMODE v] direction X (DX) Y (DY) z (DZ)
- dragged object name
- when an object from this sprite is being dragged
- when an object from this sprite stops being dragged
- when an object from this sprite starts to be dragged

**Utilities:**
- map screen XY (X) (Y) to XYZ position on object [OBJECTNAME]

---

### 4. 3D Tools (32 blocks)
Material properties, textures, scaling, transformations, and advanced rendering options.

**Colors & Textures:**
- update color diffusion [DIFFUSIONCOLOR] emission [EMISSIONCOLOR] roughness (R) brightness (B) remove texture [DOREMOVE v] area [AREATYPE v]
- update texture [TEXTURENAME] unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [All v]
- update texture using costume [COSTUMENAME v] unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [AREATYPE v]
- add texture with shared file [IMAGEURL] box unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [AREATYPE v]
- get [COLORTYPE v] color of object named [NAME]

**Scaling & Size:**
- update scale x (SX)% y (SY)% z (SZ)% in (T) seconds [BLOCKINGTYPE v]
- update size x (SX) y (SY) z (SZ)

**Material Settings:**
- apply grid material face [FACECOLOR] line [LINECOLOR] density (D) minor line visibility (V) line offset xyz (OFFSETX) (OFFSETY) (OFFSETZ)
- material setting: wireframe mode [ISWIREMODE v] draw back face [DODRAW v] z-offset (OFFSETZ) log depth [ISLOG v] transparent [HASTRANSPARENCY v]
- convert to flat shading
- set camera facing mode [MODE v]
- set rendering layer [ID v]

**Export:**
- export object [NAME] as a GLB file
- export object [NAME] as an STL file

**Object Operations:**
- objects [OBJECTNAME1] and [OBJECTNAME2] are overlapping
- bake current transformations
- carve [STARTINGOBJECT] with [CARVINGOBJECT]
- merge [OBJECTNAME1] into [OBJECTNAME2]
- copy object share data [ISSHARING v] as [NAME]

**Mirroring:**
- remove all reflections in mirror [NAME]
- reflect in mirror [NAME]
- build mirror brightness (B) using object named [NAME]
- copy to mirror position [TYPE v]

**Matrix Copying:**
- copy by matrix count in xyz (COUNTX) (COUNTY) (COUNTZ) spacing in xyz (SPACINGX) (SPACINGY) (SPACINGZ) random ratio in spacing (SPACINGR)% scale (SCALINGR)% z-rotation (ZROTATIONR)% [SUBSET v] object [SUBSETOBJECT]
- copy by matrix from center count in xyz (COUNTX) (COUNTY) (COUNTZ) spacing in xyz (SPACINGX) (SPACINGY) (SPACINGZ) random ratio in spacing (SPACINGR)% scale (SCALINGR)% z-rotation (ZROTATIONR)% [SUBSET v] object [SUBSETOBJECT]
- copy to rotated position around the [AXISNAME v] axis count (N) degree step (STEP) shift XYZ (SHIFTX) (SHIFTY) (SHIFTZ)

**Iteration:**
- for each 3D object named [VARIABLENAME v]

**Vertices & Geometry:**
- update vertices scale xyz (SX) (SY) (SZ) move xyz (MX) (MY) (MZ) position min xyz (MINX) (MINY) (MINZ) max xyz (MAXX) (MAXY) (MAXZ)
- subdivide faces by (N)

**Visual Aids:**
- show bounding box [ISSHOWN v]
- show edges [ISSHOWN v] color [COLOR] thickness (THICKNESS)
- show skeleton [ISSHOWN v]

---

### 5. 3D Physics (36 blocks)
Physics simulation, rigid bodies, constraints, collisions, and vehicle simulation.

**Physics Setup:**
- enable physics for scene with gravity (GRAVITY)
- update gravity for scene to (GRAVITY)
- set physics frame rate [RATE]
- get physics frame rate for [NAME]

**Physics Bodies:**
- add [SHAPE v] physics body with mass (MASS) restitution (RESTITUTION)% friction (FRICTION)% frozen [ISFROZEN v] debug [ISDEBUG v] [COLOR]
- update physics property restitution (RESTITUTION)% friction (FRICTION)%
- freeze physics body named [NAME] [ISFROZEN v]
- freeze all physics bodys [ISFROZEN v]
- add physics bodies of [CHILDRENNAMELIST] into compound [NAME] keep object [KEEPOBJ v]
- remove physics body
- get physics body [PROPERTY v] for [NAME]

**Movement & Speed:**
- set physics body speed in facing direction (SPEED) for [NAME]
- set physics body speed (SPEED) towards target xyz (X) (Y) (Z) for [NAME]
- set physics body speed (SPEED) for [NAME] towards object [TARGETNAME] from sprite [SPRITENAME v]
- set physics body speed in xyz (MX) (MY) (MZ) for [NAME]
- set physics body rotation speed around xyz axes (RX) (RY) (RZ) for [NAME]

**Forces & Impulses:**
- apply force strength (SIZE) direction xyz (X) (Y) (Z) at relative point xyz (X2) (Y2) (Z2) to [NAME]
- apply impulse strength (SIZE) direction xyz (X) (Y) (Z) at relative point xyz (X2) (Y2) (Z2) to [NAME]

**Constraints & Limits:**
- lock physics body speed in X (MX) Y (MY) Z (MZ) rotation around X (RX) Y (RY) Z (RZ) for [NAME]
- set physics body damping for movement (MD)% rotation (RD)% for [NAME]
- set physics body rotation speed limit (LIMIT) allow axis X [ALLOWX v] Y [ALLOWY v] Z [ALLOWZ v] for [NAME]
- set physics body movement speed limit (LIMIT) allow direction X [ALLOWX v] Y [ALLOWY v] Z [ALLOWZ v] for [NAME]

**Joints/Constraints:**
- add distance constraint between bodies of [OBJECTNAME] from [SPRITENAME v] and [OBJECTNAME2] from [SPRITENAME2 v] named [JOINTNAME]
- add fixed constraint between bodies of [OBJECTNAME] from [SPRITENAME v] and [OBJECTNAME2] from [SPRITENAME2 v] named [JOINTNAME]
- add hinge constraint between bodies of [OBJECTNAME] from [SPRITENAME v] at point x (X2) y (Y2) z (Z2) axis x (X) y (Y) z (Z) and [OBJECTNAME2] from [SPRITENAME2 v] at point x (X4) y (Y4) z (Z4) axis x (X3) y (Y3) z (Z3) named [JOINTNAME]
- set limits for hinge constraint named [NAME] angle between (LOW) and (HIGH) softness (SOFT) bias factor (BIAS) relaxation (RELAX)
- set speed (SPEED) for hinge constraint named [NAME]
- remove constraint named [JOINTNAME]

**Collisions:**
- names of physics bodies in contact for [NAME]
- update collision group [COLLISIONGROUP v] target groups [TARGETGROUPS] for [NAME]
- broadcast [BROADCASTMESSAGE] on collision between physics bodies of [NAME] from [SPRITENAME v] and [NAME2] from [SPRITENAME2 v]

**Car Physics:**
- enable car simulation mass (MASS) restitution (RESTITUTION)% friction (BODYFRICTION)% tire friction (FRICTION)% suspension (SUSPENSION) for [NAME]
- set car engine force (ENGINEFORCE) brake level (BRAKEFORCE) % for [NAME]
- set car wheel angle LF (LF) RF (RF) LB (LB) RB (RB) for [NAME]
- steer car to angle (A) for [NAME]
- set car wheel engine force LF (LF) RF (RF) LB (LB) RB (RB) brake level (BRAKE)% for [NAME]

---

### 6. 3D Effect (18 blocks)
Particle systems, emitters, trails, and visual effects.

**Prebuilt Emitters:**
- add prebuilt emitter for [TYPE v] [COLOR1] [COLOR2] capacity (C) texture size (TEXTURESIZE) source size (SOURCESIZE) speed (SPEED) max life (MAXLIFE) as [NAME]

**Custom Particle Emitters:**
- add particle emitter shape [SHAPETYPE v] texture [TEXTURE] facing camera [FACINGCAM v] life min (MINLIFE) max (MAXLIFE) capacity (C) GPU [USEGPU v] time ratio (TIMERATIO)% as [NAME]

**Emitter Shapes:**
- configure box emitter [NAME]: min xyz (MINX) (MINY) (MINZ) max xyz (MAXX) (MAXY) (MAXZ)
- configure cone emitter [NAME]: radius (R) angle (A) radius range (RR) height range (HR)
- configure cylinder emitter [NAME]: radius (RADIUS) range (RANGE) height (H) direction randomness (R)%
- configure hemispheric emitter [NAME]: radius (RADIUS) range (RANGE)
- configure mesh emitter [NAME]: use mesh normal direction [USENORMAL v]
- configure sphere emitter [NAME]: radius (RADIUS) range (RANGE)

**Emitter Properties:**
- configure emitter [NAME] blend mode [MODE v]
- configure emitter [NAME] color: start [STARTCOLOR1] to [STARTCOLOR2] end [ENDCOLOR1] to [ENDCOLOR2] at progress (MIDDLE)% [MIDDLECOLOR1] to [MIDDLECOLOR2]
- configure emitter [NAME] initial rotation: min (MINR) max (MAXR)
- configure emitter [NAME] movement: speed min (MINS) max (MAXS) direction 1 (X1) (Y1) (Z1) direction 2 (X2) (Y2) (Z2)
- configure emitter [NAME] rotation speed: start (STARTS1) to (STARTS2) end (ENDS1) to (ENDS2) at progress (MIDDLE)% (MIDDLES1) to (MIDDLES2)
- configure emitter [NAME] scale: x min (MINX)% max (MAXX)% y min (MINY)% max (MAXY)%
- configure emitter [NAME] size: start (STARTS1) to (STARTS2) end (ENDS1) to (ENDS2) at progress (MIDDLE)% (MIDDLES1) to (MIDDLES2)

**Emitter Control:**
- [ACTION v] emitter [NAME]
- start emitter [NAME] [RATETYPE v] of (N)

**Trails:**
- add trail diffusion [DIFFUSECOLOR] emission [EMISSIONCOLOR] width (W) segments (N) as [NAME]

---

### 7. 3D AR/VR (5 blocks)
Augmented reality and virtual reality features.

**AR Modes:**
- switch to AR world camera scale (S) emulation mode [ISEMULATION v]
- switch to AR face camera show marker [SHOW v] scale (S) emulation mode [ISEMULATION v] data table [TABLENAME v] with mesh of face [SHOWFACE v] eyes [SHOWEYE v] mouth [SHOWMOUTH v] lips [SHOWLIP v]
- switch to AR LOGO as [TYPE v] camera [CAMTYPE v] marker [SHOW v] scale (S) emulation [ISEMULATION v]

**AR Tools:**
- convert to transparent occlusion
- show inspector [SHOW v]

---

## Key Findings

1. **No separate "Camera", "Avatar", "Model", or "Terrain" categories** - these are integrated into the main categories:
   - Camera controls are in **3D Scene**
   - Avatars are in **3D Object**
   - Models are in **3D Object**
   - Terrain is not explicitly categorized (may be built using planes/geometry)

2. **Comprehensive 3D Support**: CreatiCode has extensive 3D capabilities including:
   - Full physics simulation
   - Particle effects
   - AR/VR support
   - Advanced lighting and materials
   - Geometry and chemistry tools
   - Animation support

3. **Skills Should Map to These 7 Categories**:
   - T03: 3D Scene
   - T04: 3D Objects
   - T05: 3D Motion (maps to "3D Action")
   - T06: 3D Look (maps to "3D Tools" for appearance)
   - T07: 3D Physics
   - T08: 3D Effects (maps to "3D Effect")
   - AR/VR could be part of advanced 3D Scene or separate

4. **Block Naming Patterns**:
   - Most blocks use explicit syntax with parameters in parentheses () or brackets []
   - [v] indicates dropdown menus
   - (PARAM) indicates numeric/text inputs
   - Many blocks support gradual transitions with "in (T) seconds"

---

## Block Count by Subcategory

### 3D Scene (47 blocks breakdown):
- Scene Setup: 16 blocks
- Camera Controls: 13 blocks
- Lighting: 10 blocks
- Glow & Highlight Effects: 6 blocks
- Joystick Controls: 3 blocks

### 3D Object (50 blocks breakdown):
- Basic Shapes: 10 blocks
- Lines & Curves: 5 blocks
- Text Objects: 2 blocks
- Planes: 2 blocks
- Complex Objects: 6 blocks
- Avatars: 3 blocks
- Geometry Tools: 6 blocks
- Chemistry: 2 blocks
- Object Management: 11 blocks
- Properties: 3 blocks

### 3D Action (51 blocks breakdown):
- Movement & Rotation: 8 blocks
- Position & Direction Copying: 4 blocks
- Speech Bubbles: 1 block
- Object Selection: 2 blocks
- Animations: 4 blocks
- Avatar Attachment: 2 blocks
- Collision Detection: 7 blocks
- Distance Sensors: 3 blocks
- Picking (Selection): 7 blocks
- Hovering: 6 blocks
- Dragging: 7 blocks
- Utilities: 1 block

### 3D Tools (32 blocks breakdown):
- Colors & Textures: 5 blocks
- Scaling & Size: 2 blocks
- Material Settings: 5 blocks
- Export: 2 blocks
- Object Operations: 5 blocks
- Mirroring: 4 blocks
- Matrix Copying: 3 blocks
- Iteration: 1 block
- Vertices & Geometry: 2 blocks
- Visual Aids: 3 blocks

### 3D Physics (36 blocks breakdown):
- Physics Setup: 4 blocks
- Physics Bodies: 7 blocks
- Movement & Speed: 5 blocks
- Forces & Impulses: 2 blocks
- Constraints & Limits: 4 blocks
- Joints/Constraints: 6 blocks
- Collisions: 3 blocks
- Car Physics: 5 blocks

### 3D Effect (18 blocks breakdown):
- Prebuilt Emitters: 1 block
- Custom Particle Emitters: 1 block
- Emitter Shapes: 6 blocks
- Emitter Properties: 7 blocks
- Emitter Control: 2 blocks
- Trails: 1 block

### 3D AR/VR (5 blocks breakdown):
- AR Modes: 3 blocks
- AR Tools: 2 blocks

---

## Mapping to Current Skills Structure

Based on this analysis, the skill tree structure should be:

**T03: 3D Scene** (47 blocks)
- Scene initialization and configuration
- Camera controls (orbit, follow, positioning)
- Lighting (point, directional, ambient, spot)
- Environment (background, fog, sky, pipeline effects)
- Joystick controls

**T04: 3D Objects** (50 blocks)
- Creating primitive shapes (box, sphere, cylinder, etc.)
- Lines, curves, and paths
- 3D text
- Loading models and avatars
- Geometry and chemistry tools
- Object hierarchy and parenting

**T05: 3D Motion** (maps to "3D Action" - 51 blocks)
- Movement and rotation
- Animations
- Speed and direction
- Avatar attachment
- Speech bubbles
- Object selection

**T06: 3D Look** (maps to "3D Tools" - 32 blocks)
- Materials and textures
- Colors and appearance
- Scaling and transformations
- Export capabilities
- Visual debugging aids

**T07: 3D Physics** (36 blocks)
- Physics simulation setup
- Rigid bodies
- Constraints and joints
- Forces and impulses
- Car physics
- Collision detection (physics-based)

**T08: 3D Effects** (maps to "3D Effect" - 18 blocks)
- Particle systems
- Emitters (various shapes)
- Trails
- Visual effects

**T09: 3D Interaction** (subset of "3D Action" - ~21 blocks)
- Picking/clicking objects
- Hovering detection
- Dragging objects
- Collision detection (non-physics)
- Distance sensors

**T10: 3D AR/VR** (5 blocks)
- AR world mode
- AR face tracking
- AR marker recognition
- Inspector tools

