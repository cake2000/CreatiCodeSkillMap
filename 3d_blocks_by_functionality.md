# CreatiCode 3D Blocks - Organized by Functionality

This document organizes all 239 3D blocks by their primary function to help verify T18 skills.

---

## SCENE INITIALIZATION (2 blocks)
- `initialize 3D scene [SCENETYPE] as hidden [ISHIDDEN]`
- `show 3D scene [ISVISIBLE]`

## SCENE EVENTS (1 block)
- `when 3D scene is initialized`

## SCENE APPEARANCE (5 blocks)
- `set scene background color [COLOR]`
- `set scene fog [MODE] [COLOR] start (STARTDISTANCE) end (FULLDISTANCE) density (DENSITY)`
- `set sky [SKYTYPE]`
- `remove sky`
- `turn [ONOFF] webcam background [WHICHCAMERA] in [FLIPMODE] mode`

## SCENE UTILITIES (4 blocks)
- `show 3D axis [SHOW] length (LENGTH)`
- `GPU Available`
- `switch to full screen [BORDERTYPE]`
- `set clipping plane [PLANEID] direction xyz (X) (Y) (Z) offset (OFFSET)`
- `remove clipping plane [PLANEID]`

## POST-PROCESSING (2 blocks)
- `add pipeline vignette (VRADIUS) [COLOR] bloom strength (BSTRENGTH) threshold (BTHRESHOLD)% kernel (BKERNEL) antialiasing [ISANTIALIASING] sharpening [ISSHARPENING] camera contrast (C) exposure (E)`
- `remove pipeline`

---

## CAMERA - CREATION (2 blocks)
- `add orbit camera distance (D) v-angle (V) h-angle (H) panning speed ratio (S) inputs key [KEY] pointer [POINTER] active [ACTIVE] as [NAME]`
- `add follow camera distance (D) z offset (ZOFFSET) v-angle (V) h-angle (H) direction lock [LOCKTYPE] see-through (SEETHROUGH)% active [ISACTIVE] as [NAME]`

## CAMERA - POSITION & TARGET (6 blocks)
- `set camera distance (D) v-angle (V) h-angle (H) z offset (OFFSET) target xyz (X) (Y) (Z) in (T) seconds`
- `set camera distance (D) [NORS] (0)° (0)' (0)" [EORW] (0)° (0)' (0)" in (T) seconds`
- `set camera target xyz (X) (Y) (Z)`
- `set camera target object [OBJECTNAME] offset xyz (OFFSETX) (OFFSETY) (OFFSETZ)`
- `set [OBJECTNAME] as parent of camera`
- `lock pointer [DOLOCK]`

## CAMERA - CONFIGURATION (2 blocks)
- `configure camera radius min (MINRADIUS) max (MAXRADIUS) visible range min (MINRANGE) max (MAXRANGE) v-angle min (MINVANGLE) max (MAXVANGLE) speed ratio panning (PANNINGSPEEDRATIO) angular (ANGULARSPEEDRATIO)`
- `set display region bottom (B)% left (L)% width (W)% height (H)% border width (BORDERWIDTH) color [BORDERCOLOR] for camera [NAME]`

## CAMERA - DATA (3 blocks)
- `camera [PROPERTY]`
- `get camera direction [FACE]`
- `get camera view position for xyz (X) (Y) (Z)`

---

## LIGHTING - CREATION (4 blocks)
- `add point light [COLOR] at xyz (X) (Y) (Z) intensity (INTENSITY) show position [SHOW] as [NAME]`
- `add directional light [COLOR] in direction xyz (DIRX) (DIRY) (DIRZ) at xyz (POSX) (POSY) (POSZ) intensity (INTENSITY) as [NAME]`
- `add ambient light [COLOR] sky direction xyz (DIRX) (DIRY) (DIRZ) intensity (INTENSITY) as [NAME]`
- `add spot light [COLOR] at xyz (X) (Y) (Z) open angle (ANGLE) intensity (INTENSITY) blur (BLUE) show position [SHOW] as [NAME]`

## LIGHTING - MANAGEMENT (4 blocks)
- `remove all lights`
- `remove light named [NAME]`
- `switch [ONOFF] light named [NAME]`
- `exclude object [OBJNAME] from light named [LIGHTNAME]`

## SHADOWS (2 blocks)
- `cast shadow [DOCAST] from light named [NAME] blur size (BLUE)`
- `receives shadow [DORECEIVE]`

## GLOW EFFECTS (3 blocks)
- `create glow layer intensity (INTENSITY) blur size (BLUR) as [NAME]`
- `add to glow layer named [NAME]`
- `remove from glow layer named [NAME]`

## HIGHLIGHT EFFECTS (3 blocks)
- `create highlight layer blur size (BLUR) as [NAME]`
- `add highlight in [COLOR] to layer named [NAME]`
- `remove from highlight layer named [NAME]`

---

## SHAPES - BASIC PRIMITIVES (8 blocks)
- `add box [COLOR] size in x (SIZEX) y (SIZEY) z (SIZEZ) edge radius (R) as [NAME]`
- `add 6-colored box [COLOR1] [COLOR2] [COLOR3] [COLOR4] [COLOR5] [COLOR6] size in x (SIZEX) y (SIZEY) z (SIZEZ) as [NAME]`
- `add sphere [COLOR] size in x (SIZEX) y (SIZEY) z (SIZEZ) arc (ARC) slice (SLICE) sides (SIDES) as [NAME]`
- `add cylinder [COLOR] diameter top (DIAMETERTOP) bottom (DIAMETERBOTTOM) height (HEIGHT) arc (ARC) closed section [CLOSEDSECTION] cap type [CAPTYPE] sides (SIDES) as [NAME]`
- `add capsule [COLOR] diameter top (TOPD) bottom (BOTTOMD) height (H) sides (SIDES) as [NAME]`
- `add torus [COLOR] diameter (D) thickness (THICKNESS) sides (SIDES) as [NAME]`
- `add plane [COLOR] size x (SIZEX) y (SIZEY) as [NAME]`
- `add plane [COLOR] width (W) height (H) coefficients abcd (A) (B) (C) (D) as [NAME]`

## SHAPES - ADVANCED (4 blocks)
- `add tube [COLOR] diameter top (TOPD) bottom (BOTTOMD) height (H) arc (ARC) closed section [SECTIONTYPE] cap type [CAPTYPE] sides (SIDES) thickness (THICKNESS) as [NAME]`
- `add rectangle tube [COLOR] size in X (SIZEX) Y (SIZEY) height (H) cap type [CAPTYPE] thickness (THICKNESS) sides [SIDECOUNT] as [NAME]`
- `add stairs [COLOR] width (W) depth (D) height (H) count (COUNT) thickness (THICKNESS) type [TYPE] as [NAME]`
- `add voxel size in xyz (SX) (SY) (SZ) with costumes top [CTOP] bottom (CBOTTOM) front (CFRONT) back (CBACK) left (CLEFT) right (CRIGHT) texture size (T) sampling [METHOD] as [NAME]`

## SHAPES - EXTRUSION (2 blocks)
- `add column [COLOR] 2D vertex list [LISTNAME] height (H) cap type [CAPTYPE] as [NAME]`
- `add cone [COLOR] vertex list [LISTNAME] height (H) as [NAME]`
- `extrude costume [COSTUMENAME] thickness (T) scaling factor (SCALE) side color [COLOR] granularity (G) as [NAME]`

## LINES & CURVES (5 blocks)
- `add line [COLOR] diameter (DIAMETER) cap [CAP] arrow [ARROW] sides (SIDES) xyz from (X1) (Y1) (Z1) to (X2) (Y2) (Z2) segments (SEGMENTS) as [NAME]`
- `add dotted line [COLOR] diameter (DIAMETER) segment length (SEGMENTLENGTH) gap length (GAPLENGTH) cap [CAP] arrow [ARROW] sides (SIDES) from xyz (X1) (Y1) (Z1) to xyz (X2) (Y2) (Z2) as [NAME]`
- `generate arc points from (X1) (Y1) (Z1) via (X2) (Y2) (Z2) to (X3) (Y3) (Z3) into list [LISTNAME] count (N)`
- `add curve [COLOR] diameter (D) cap [CAPTYPE] arrow [ARROWTYPE] sides (S) using list [LISTNAME] from (STARTINDEX) to (ENDINDEX) segments (SEGMENTCOUNT) as [NAME]`
- `add moving line between [OBJECT1] and [OBJECT2] [COLOR] diameter (D) sides (SIDES) as [NAME]`

## TEXT (2 blocks)
- `add 3D text [TEXT] font [FONT] color [COLOR] width (WIDTH) height (HEIGHT) diameter (DIAMETER) camera facing [CAMERAFACING] as [NAME]`
- `add 3D thick text [TEXT] font [FONT] color [COLOR] width (WIDTH) height (HEIGHT) thickness (THICKNESS) diameter (DIAMETER) camera facing [CAMERAFACING] as [NAME]`

## MODELS (3 blocks)
- `add model [MODELTYPE] target height (H) origin offset x (OFFSETX) y (OFFSETY) z (OFFSETZ) rotation x (RX) y (RY) z (RZ) hidden [HIDDEN] as [NAME]`
- `add public object at URL [OBJECTURL] as [TYPE] target height (H) rotation (RX) (RY) (RZ) origin offset (OFFSETX) (OFFSETY) (OFFSETZ) as [NAME]`
- `add community model [MODELNAME] target height (H) rotation (RX) (RY) (RZ) origin offset (OFFSETX) (OFFSETY) (OFFSETZ) as [NAME]`

## AVATARS (3 blocks)
- `add avatar [AVATARTYPE] height (H) as [NAME] hidden [ISHIDDEN]`
- `add avatar [AVATARNAME] for user [USERNAME] height (H) as [NAME] hidden [ISHIDDEN]`
- `add user avatar [AVATARNAME] height (HEIGHT) as [NAME]`

## GEOMETRY TOOLS (6 blocks)
- `geometry: add point at xyz (X) (Y) (Z) color [COLOR] size (SIZE) on [PARENTNAME] as [NAME]`
- `geometry: add point between points [POINT1NAME] [POINT2NAME] at (RATIO)% color [COLOR] size (SIZE) as [NAME]`
- `geometry: add line between points [POINT1NAME] [POINT2NAME] color [COLOR] diameter (D) arrow [ARROWTYPE] sides (SIDES) segments (SEGMENTS) as [NAME]`
- `geometry: add triangle from points [POINT1] [POINT2] [POINT3] color [COLOR] as [NAME]`
- `geometry: add frame box color [COLOR] size in x (X) y (Y) z (Z) thickness (T) labels [SHOWLABELS] as [NAME]`
- `geometry: add angle mark [POINT1NAME] [POINT2NAME] [POINT3NAME] size (S) color [COLOR] diameter (D) arrow [ARROWTYPE] sides (SIDES) label [LABELTEXT] as [NAME]`

## CHEMISTRY (2 blocks)
- `chemistry: add atom [ATOMTYPE] as [MYNAME] connect hole [MYHOLELIST] to atom [OTHERNAME] hole [OTHERHOLELIST] distance (D)`
- `chemistry: add custom atom [COLOR] size (S) holes [HOLELIST] label [LABEL] angle [LABELANGLE] as [MYNAME] connect hole [MYHOLELIST] to atom [OTHERATOM] hole [OTHERHOLELIST] distance (D)`

## OBJECT MANAGEMENT (4 blocks)
- `remove object named [NAME]`
- `remove all objects`
- `object [NAME] exists`
- `add transformer as [NAME]`

## OBJECT HIERARCHY (5 blocks)
- `set object [OBJECTNAME] from sprite [SPRITENAME] as parent and update position/scale [DOUPDATE]`
- `set camera as parent`
- `unlink all children`
- `unlink parent`
- `show local axis [SHOW] length (LENGTH)`

## OBJECT PROPERTIES (3 blocks)
- `[PROPERTY] of object [OBJECTNAME] from sprite [SPRITENAME]`
- `set property [PROPERTYNAME] to [VALUE] for [OBJNECTNAME]`
- `property [PROPERTYNAME] of [OBJECTNAME]`

## SOLID PARTICLE SYSTEM (2 blocks)
- `convert to sps at xyz from list [LISTNAME] updatable [ISUPDATABLE]`
- `add to sps [NAME] at xyz from list [LIST]`

---

## MOVEMENT - POSITION (5 blocks)
- `move to x (X) y (Y) z (Z) in (T) seconds [ISBLOCKING]`
- `move (DISTANCE) along current direction in (T) seconds [ISBLOCKING]`
- `set speed [SPEEDTYPE] to (N)`
- `copy position from camera`
- `copy position from object [NAME]`

## MOVEMENT - ROTATION (6 blocks)
- `rotate to angle (A) around the [AXIS] axis in (T) seconds [ISBLOCKING]`
- `rotate to direction x (ANGLEX) y (ANGLEY) z (ANGLEZ) in (T) seconds [ISBLOCKING]`
- `turn (N) degrees around the [AXIS] axis in (T) seconds [ISBLOCKING]`
- `point to position x (PX) y (PY) z (PZ) in (T) seconds [ISBLOCKING]`
- `copy direction from camera`
- `copy direction from object [NAME]`

## OBJECT SELECTION (2 blocks)
- `select sprite object by name [NAME]`
- `sprite object name`

## DISTANCE & PROXIMITY (3 blocks)
- `distance between objects [OBJECT1] and [OBJECT2]`
- `broadcast [MESSAGE] when [OBJECTNAME1] from [SPRITENAME1] and [OBJECTNAME2] from [SPRITENAME2] overlap`
- `broadcast [MESSAGE] when [DIMENSION] distance dlte (D) between [OBJECTNAME1] from [SPRITENAME1] and [OBJECTNAME2] from [SPRITENAME2]`

---

## ANIMATIONS - AVATAR (2 blocks)
- `add animations [ANIMATIONLIST]`
- `start animation [NAME] looping [ISLOOPING] progress from (PSTART) to (PEND) speed ratio (SPEEDRATIO) [BLOCKINGMODE] offset x (OFFSETX) y (OFFSETY) z (OFFSETZ) broadcast [MESSAGELIST] at progress [PROGRESSPOINTLIST]`

## ANIMATIONS - MODEL (1 block)
- `start model animation [NAME] looping [ISLOOPING] progress from (PSTART) to (PEND) speed ratio (SPEEDRATIO) [BLOCKINGMODE] offset x (OFFSETX) y (OFFSETY) z (OFFSETZ) broadcast [MESSAGELIST] at progress [PROGRESSPOINTLIST]`

## SKELETON & BONES (3 blocks)
- `attach to body part [PARTNAME] of [AVATARNAME] from sprite [SPRITENAME] target height (H)`
- `detach from body`
- `update bone [BONENAME] move in x (MOVEX) y (MOVEY) z (MOVEZ) rotate in x (ROTATEX) y (ROTATEY) z (ROTATEZ)`

---

## COLLISION - RAYCAST (5 blocks)
- `turn on [ISBLOCKING] collision with [SPRITENAME] collider z offset (ZOFFSET) precision [PRECISIONTYPE] debug [ISDEBUG]`
- `broadcast [MESSAGE] on collision between [OBJECTNAME1] from [SPRITENAME1] and [OBJECTNAME2] from [SPRITENAME2]`
- `when colliding with [SPRITENAME]`
- `update collider dimension x (SIZEX) y (SIZEY) z (SIZEZ) collider z offset (ZOFFSET) sensing range x (RANGEX) y (RANGEY) z (RANGEZ) color [COLOR]`
- `sprite object blocked [DIRECTION]`

## COLLISION - OVERLAP (2 blocks)
- `broadcast [MESSAGE] when [OBJECTNAME1] from [SPRITENAME1] and [OBJECTNAME2] from [SPRITENAME2] overlap`
- `objects [OBJECTNAME1] and [OBJECTNAME2] are overlapping`

## DISTANCE SENSORS (3 blocks)
- `set distance sensor front [ONOFFFRONT] back [ONOFFBACK] left [ONOFFLEFT] right [ONOFFRIGHT] down [ONOFFDOWN] up [ONOFFUP] max distance (MAXD) count [COUNT] visible [ISVISIBLE]`
- `name of nearest obstacle in the [DIRECTION] direction for [OBJECTNAME]`
- `distance to nearest obstacle in the [DIRECTION] direction for [OBJECTNAME]`

---

## PICKING (7 blocks)
- `turn on picking with [BUTTON] for objects created in sprites [SPRITELIST] on [POINTERACTION]`
- `turn off picking for objects created in sprites [SPRITELIST]`
- `when an object from this sprite is picked`
- `picked object name`
- `picked point x pos`
- `picked point y pos`
- `picked point z pos`

## HOVERING (6 blocks)
- `turn on hovering for objects created in sprites [SPRITELIST]`
- `turn off hovering for objects created in sprites [SPRITELIST]`
- `hovered object name`
- `hovered point x pos`
- `hovered point y pos`
- `hovered point z pos`

## DRAGGING (6 blocks)
- `set dragging mode [DRAGGINGMODE] direction X (DX) Y (DY) z (DZ)`
- `set dragging limits min xyz (MINX) (MINY) (MINZ) max xyz (MAXX) (MAXY) (MAXZ)`
- `when an object from this sprite is being dragged`
- `when an object from this sprite stops being dragged`
- `when an object from this sprite starts to be dragged`
- `dragged object name`

## INTERACTION UTILITIES (2 blocks)
- `show speech bubble [TEXT] offset xyz (X) (Y) (Z) max width (W) text font [FONTNAME] size (FONTSIZE) color [FONTCOLOR] background [BGCOLOR] for [T] seconds camera facing [ISCAMERAFACING] ID [BUBBLEID]`
- `map screen XY (X) (Y) to XYZ position on object [OBJECTNAME]`

---

## MATERIALS - COLOR (2 blocks)
- `update color diffusion [DIFFUSIONCOLOR] emission [EMISSIONCOLOR] roughness (R) brightness (B) remove texture [DOREMOVE] area [AREATYPE]`
- `get [COLORTYPE] color of object named [NAME]`

## MATERIALS - TEXTURE (4 blocks)
- `update texture [TEXTURENAME] unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [All]`
- `update texture using costume [COSTUMENAME] unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [AREATYPE]`
- `add texture with shared file [IMAGEURL] box unit size (UNITSIZE) non-box repeat h (H) v (V) rotation (R) area [AREATYPE]`
- `apply grid material face [FACECOLOR] line [LINECOLOR] density (D) minor line visibility (V) line offset xyz (OFFSETX) (OFFSETY) (OFFSETZ)`

## MATERIALS - SETTINGS (2 blocks)
- `material setting: wireframe mode [ISWIREMODE] draw back face [DODRAW] z-offset (OFFSETZ) log depth [ISLOG] transparent [HASTRANSPARENCY]`
- `set rendering layer [ID]`
- `set camera facing mode [MODE]`

## SCALE & SIZE (2 blocks)
- `update scale x (SX)% y (SY)% z (SZ)% in (T) seconds [BLOCKINGTYPE]`
- `update size x (SX) y (SY) z (SZ)`

---

## OBJECT COPYING (5 blocks)
- `copy object share data [ISSHARING] as [NAME]`
- `copy by matrix count in xyz (COUNTX) (COUNTY) (COUNTZ) spacing in xyz (SPACINGX) (SPACINGY) (SPACINGZ) random ratio in spacing (SPACINGR)% scale (SCALINGR)% z-rotation (ZROTATIONR)% [SUBSET] object [SUBSETOBJECT]`
- `copy by matrix from center count in xyz (COUNTX) (COUNTY) (COUNTZ) spacing in xyz (SPACINGX) (SPACINGY) (SPACINGZ) random ratio in spacing (SPACINGR)% scale (SCALINGR)% z-rotation (ZROTATIONR)% [SUBSET] object [SUBSETOBJECT]`
- `copy to mirror position [TYPE]`
- `copy to rotated position around the [AXISNAME] axis count (N) degree step (STEP) shift XYZ (SHIFTX) (SHIFTY) (SHIFTZ)`
- `for each 3D object named [VARIABLENAME]`

## MESH OPERATIONS (6 blocks)
- `carve [STARTINGOBJECT] with [CARVINGOBJECT]`
- `merge [OBJECTNAME1] into [OBJECTNAME2]`
- `convert to flat shading`
- `subdivide faces by (N)`
- `update vertices scale xyz (SX) (SY) (SZ) move xyz (MX) (MY) (MZ) position min xyz (MINX) (MINY) (MINZ) max xyz (MAXX) (MAXY) (MAXZ)`
- `bake current transformations`

## MIRROR REFLECTIONS (3 blocks)
- `build mirror brightness (B) using object named [NAME]`
- `reflect in mirror [NAME]`
- `remove all reflections in mirror [NAME]`

## VISUALIZATION (3 blocks)
- `show bounding box [ISSHOWN]`
- `show edges [ISSHOWN] color [COLOR] thickness (THICKNESS)`
- `show skeleton [ISSHOWN]`

## EXPORT (2 blocks)
- `export object [NAME] as a GLB file`
- `export object [NAME] as an STL file`

---

## PHYSICS - SETUP (4 blocks)
- `enable physics for scene with gravity (GRAVITY)`
- `update gravity for scene to (GRAVITY)`
- `set physics frame rate [RATE]`
- `get physics frame rate`

## PHYSICS - BODIES (6 blocks)
- `add [SHAPE] physics body with mass (MASS) restitution (RESTITUTION)% friction (FRICTION)% frozen [ISFROZEN] debug [ISDEBUG] [COLOR]`
- `update physics property restitution (RESTITUTION)% friction (FRICTION)%`
- `remove physics body`
- `freeze physics body named [NAME] [ISFROZEN]`
- `freeze all physics bodys [ISFROZEN]`
- `add physics bodies of [CHILDRENNAMELIST] into compound [NAME] keep object [KEEPOBJ]`

## PHYSICS - MOVEMENT (6 blocks)
- `set physics body speed in facing direction (SPEED) for [NAME]`
- `set physics body speed (SPEED) towards target xyz (X) (Y) (Z) for [NAME]`
- `set physics body speed (SPEED) for [NAME] towards object [TARGETNAME] from sprite [SPRITENAME]`
- `set physics body speed in xyz (MX) (MY) (MZ) for [NAME]`
- `apply force strength (SIZE) direction xyz (X) (Y) (Z) at relative point xyz (X2) (Y2) (Z2) to [NAME]`
- `apply impulse strength (SIZE) direction xyz (X) (Y) (Z) at relative point xyz (X2) (Y2) (Z2) to [NAME]`

## PHYSICS - ROTATION (1 block)
- `set physics body rotation speed around xyz axes (RX) (RY) (RZ) for [NAME]`

## PHYSICS - CONSTRAINTS (4 blocks)
- `set physics body damping for movement (MD)% rotation (RD)% for [NAME]`
- `set physics body movement speed limit (LIMIT) allow direction X [ALLOWX] Y [ALLOWY] Z [ALLOWZ] for [NAME]`
- `set physics body rotation speed limit (LIMIT) allow axis X [ALLOWX] Y [ALLOWY] Z [ALLOWZ] for [NAME]`
- `lock physics body speed in X (MX) Y (MY) Z (MZ) rotation around X (RX) Y (RY) Z (RZ) for [NAME]`

## PHYSICS - JOINTS (6 blocks)
- `add distance constraint between bodies of [OBJECTNAME] from [SPRITENAME] and [OBJECTNAME2] from [SPRITENAME2] named [JOINTNAME]`
- `add fixed constraint between bodies of [OBJECTNAME] from [SPRITENAME] and [OBJECTNAME2] from [SPRITENAME2] named [JOINTNAME]`
- `add hinge constraint between bodies of [OBJECTNAME] from [SPRITENAME] at point x (X2) y (Y2) z (Z2) axis x (X) y (Y) z (Z) and [OBJECTNAME2] from [SPRITENAME2] at point x (X4) y (Y4) z (Z4) axis x (X3) y (Y3) z (Z3) named [JOINTNAME]`
- `set limits for hinge constraint named [NAME] angle between (LOW) and (HIGH) softness (SOFT) bias factor (BIAS) relaxation (RELAX)`
- `set speed (SPEED) for hinge constraint named [NAME]`
- `remove constraint named [JOINTNAME]`

## PHYSICS - COLLISION (3 blocks)
- `update collision group [COLLISIONGROUP] target groups [TARGETGROUPS] for [NAME]`
- `broadcast [BROADCASTMESSAGE] on collision between physics bodies of [NAME] from [SPRITENAME] and [NAME2] from [SPRITENAME2]`
- `names of physics bodies in contact for [NAME]`

## PHYSICS - CAR (5 blocks)
- `enable car simulation mass (MASS) restitution (RESTITUTION)% friction (BODYFRICTION)% tire friction (FRICTION)% suspension (SUSPENSION) for [NAME]`
- `set car engine force (ENGINEFORCE) brake level (BRAKEFORCE) % for [NAME]`
- `steer car to angle (A) for [NAME]`
- `set car wheel angle LF (LF) RF (RF) LB (LB) RB (RB) for [NAME]`
- `set car wheel engine force LF (LF) RF (RF) LB (LB) RB (RB) brake level (BRAKE)% for [NAME]`

## PHYSICS - DATA (1 block)
- `get physics body [PROPERTY] for [NAME]`

---

## PARTICLES - CREATION (2 blocks)
- `add prebuilt emitter for [TYPE] [COLOR1] [COLOR2] capacity (C) texture size (TEXTURESIZE) source size (SOURCESIZE) speed (SPEED) max life (MAXLIFE) as [NAME]`
- `add particle emitter shape [SHAPETYPE] texture [TEXTURE] facing camera [FACINGCAM] life min (MINLIFE) max (MAXLIFE) capacity (C) GPU [USEGPU] time ratio (TIMERATIO)% as [NAME]`

## PARTICLES - SHAPE CONFIG (6 blocks)
- `configure box emitter [NAME]: min xyz (MINX) (MINY) (MINZ) max xyz (MAXX) (MAXY) (MAXZ)`
- `configure cone emitter [NAME]: radius (R) angle (A) radius range (RR) height range (HR)`
- `configure cylinder emitter [NAME]: radius (RADIUS) range (RANGE) height (H) direction randomness (R)%`
- `configure hemispheric emitter [NAME]: radius (RADIUS) range (RANGE)`
- `configure sphere emitter [NAME]: radius (RADIUS) range (RANGE)`
- `configure mesh emitter [NAME]: use mesh normal direction [USENORMAL]`

## PARTICLES - PROPERTIES (7 blocks)
- `configure emitter [NAME] color: start [STARTCOLOR1] to [STARTCOLOR2] end [ENDCOLOR1] to [ENDCOLOR2] at progress (MIDDLE)% [MIDDLECOLOR1] to [MIDDLECOLOR2]`
- `configure emitter [NAME] size: start (STARTS1) to (STARTS2) end (ENDS1) to (ENDS2) at progress (MIDDLE)% (MIDDLES1) to (MIDDLES2)`
- `configure emitter [NAME] scale: x min (MINX)% max (MAXX)% y min (MINY)% max (MAXY)%`
- `configure emitter [NAME] movement: speed min (MINS) max (MAXS) direction 1 (X1) (Y1) (Z1) direction 2 (X2) (Y2) (Z2)`
- `configure emitter [NAME] rotation speed: start (STARTS1) to (STARTS2) end (ENDS1) to (ENDS2) at progress (MIDDLE)% (MIDDLES1) to (MIDDLES2)`
- `configure emitter [NAME] initial rotation: min (MINR) max (MAXR)`
- `configure emitter [NAME] blend mode [MODE]`

## PARTICLES - CONTROL (2 blocks)
- `start emitter [NAME] [RATETYPE] of (N)`
- `[ACTION] emitter [NAME]`

## TRAILS (1 block)
- `add trail diffusion [DIFFUSECOLOR] emission [EMISSIONCOLOR] width (W) segments (N) as [NAME]`

---

## AR/VR (5 blocks)
- `switch to AR world camera scale (S) emulation mode [ISEMULATION]`
- `switch to AR face camera show marker [SHOW] scale (S) emulation mode [ISEMULATION] data table [TABLENAME] with mesh of face [SHOWFACE] eyes [SHOWEYE] mouth [SHOWMOUTH] lips [SHOWLIP]`
- `switch to AR LOGO as [TYPE] camera [CAMTYPE] marker [SHOW] scale (S) emulation [ISEMULATION]`
- `convert to transparent occlusion`
- `show inspector [SHOW]`

---

## INPUT CONTROLS (3 blocks)
- `add [SIDE] joystick [COLOR1] [COLOR2] scale [SCALE]`
- `[SIDE] joystick [PROPERTY]`
- `remove all joysticks`

---

## TOTAL: 239 blocks
