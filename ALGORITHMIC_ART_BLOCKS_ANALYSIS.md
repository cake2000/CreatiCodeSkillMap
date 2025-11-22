# CreatiCode Blocks for Algorithmic Art and Creative Coding
## Comprehensive Analysis from blockdes8.txt

This document catalogs ALL blocks available in CreatiCode that are relevant for algorithmic art, generative art, patterns, fractals, spirals, and creative coding projects.

---

## 1. DRAWING BLOCKS - Looks Category (27 blocks total, 9 drawing-related)

### Direct Drawing on Stage/Costume

#### looks_draw_rectangle
- **Syntax**: `draw rectangle at x (XPOS) y (YPOS) width (W) height (H) fill [FILLCOLOR] border [BORDERCOLOR] width (BORDERWIDTH) corner radius (CORNERRADIUS) rotation (N)`
- **Description**: Draw a rectangle at the given x and y position with the given width and height. The rectangle can be styled with a FILLCOLOR, BORDERCOLOR, BORDERWIDTH and CORNERRADIUS. The rectangle can be rotated by N degrees clockwise as well. This block can be used to draw a rectangle directly on the sprite's current costume assuming it is in vector format, not draw on the stage.
- **3D Compatible**: false
- **Algorithmic Art Use Cases**:
  - Grid patterns and tessellations
  - Building blocks for geometric art
  - Rotated rectangles for kaleidoscope effects
  - Rounded corners for organic patterns

#### looks_draw_oval
- **Syntax**: `draw oval at x (XPOS) y (YPOS) width (W) height (H) fill [FILLCOLOR] border [BORDERCOLOR] width (BORDERWIDTH) rotation (N)`
- **Description**: Draw an oval at the given x and y positions with the given width and height. The oval can be styled with a FILLCOLOR, BORDERCOLOR and BORDERWIDTH. The oval can be rotated by N degrees clockwise as well. This block can be used to draw an oval directly on the sprite's current costume assuming it is in vector format, not draw on the stage.
- **3D Compatible**: false
- **Algorithmic Art Use Cases**:
  - Circle patterns and mandalas
  - Elliptical spirals
  - Organic, flowing designs
  - Rotated ellipses for petal/flower patterns

#### looks_draw_line
- **Syntax**: `draw line in [LINECOLOR] from x (FROMX) y (FROMY) to x (TOX) y (TOY) thickness (THICKNESS)`
- **Description**: Draw a line between 2 points: (FROMX, FROMY) to (TOX, TOY). The line can be styled with LINECOLOR and THICKNESS. This block can be used to draw a line directly on the sprite's current costume assuming it is in vector format, not draw on the stage.
- **3D Compatible**: false
- **Algorithmic Art Use Cases**:
  - Line art and geometric patterns
  - Connecting points in algorithmic designs
  - Creating polygons by connecting vertices
  - Fractal trees and branches

#### looks_draw_curve
- **Syntax**: `draw curve in [LINECOLOR] from x (FROMX) y (FROMY) to x (TOX) y (TOY) control 1 x (CONTROLX1) y (CONTROLY1) control 2 x (CONTROLX2) y (CONTROLY2) thickness (THICKNESS)`
- **Description**: Draw a bezier curve from the point (FROMX, FROMY) to the point (TOX, TOY), using two control points of (CONTROLX1, CONTROLY1) and (CONTROLX2, CONTROLY2). The curve can be styled with LINECOLOR and THICKNESS. This block can be used to draw a curve directly on the sprite's current costume assuming it is in vector format, not draw on the stage.
- **3D Compatible**: false
- **Algorithmic Art Use Cases**:
  - Smooth, flowing organic patterns
  - Bezier curve art
  - Generative landscapes
  - Abstract wave patterns

#### looks_draw_text
- **Syntax**: `draw text [TEXT] at x (X) y (Y) size (SIZE) color (COLOR) rotation (ROTATION)`
- **Description**: Draw text at the given x and y positions in the given font size and font color. The text can be rotated by the given degrees clockwise. This block can be used to draw text directly on the sprite's current costume assuming it is in vector format, not draw on the stage.
- **3D Compatible**: false
- **Algorithmic Art Use Cases**:
  - Text-based generative art
  - Typography patterns
  - Word clouds
  - Rotated text spirals

#### looks_printtext
- **Syntax**: `print [TEXT] at x (XPOS) y (YPOS) width (W) height (H) color [FONTCOLOR]`
- **Description**: Print text at the given x and y coordinates, and scaled up or down proportionally so that the text fits into the given window of width and height. The text can be styled with a color.
- **3D Compatible**: false
- **Algorithmic Art Use Cases**:
  - Dynamic text sizing in patterns
  - ASCII art generation
  - Text-based compositions

#### looks_printtextforsecs
- **Syntax**: `print [TEXT] at x (XPOS) y (YPOS) width (W) height (H) color [FONTCOLOR] for (T) seconds`
- **Description**: Same as above but with timed display
- **3D Compatible**: false

### Clearing Drawings

#### looks_clearallmyprints
- **Syntax**: `clear all my prints`
- **Description**: Clear all the text and drawing printed by this sprite using the 'print' and 'draw' blocks in the 'Looks' category. Does not affect the drawings done by the 'Pen' blocks.
- **3D Compatible**: false

#### looks_clearallprints
- **Syntax**: `clear all prints`
- **Description**: Clear all the text and drawing printed by all sprites using the 'print' and 'draw' blocks in the 'Looks' category. Does not affect the drawings done by the 'Pen' blocks.
- **3D Compatible**: false

#### looks_clear_drawing
- **Syntax**: `clear all drawings`
- **Description**: Remove all drawings on this sprite's current costume, assuming it is in vector mode, and the drawings are done also using looks blocks, such as rectangle/oval/text/line/curve.
- **3D Compatible**: false

### Color and Visual Effects

#### looks_colour
- **Syntax**: `color (C) saturation (S) brightness (B) transparency (T)`
- **Description**: A reporter block that represents the color composed of the specified color C, saturation S, brightness B and transparency T. Each input value is between 0 and 100. This block allows us to generate colors dynamically, instead of using the color selector sliders manually. Its return value will be a color string in the format of "#RRGGBBAA".
- **3D Compatible**: false
- **Algorithmic Art Use Cases**:
  - Dynamic color generation
  - Color gradients
  - Rainbow effects
  - Color harmonies and palettes

---

## 2. PEN CATEGORY BLOCKS (4 blocks)

**IMPORTANT NOTE**: CreatiCode has only 4 dedicated Pen blocks. Most drawing functionality is in the Looks category above.

#### pen_printtext
- **Syntax**: `draw text [TEXT] width (W) height (H) color [COLOR] for [T] seconds`
- **Description**: Print some text at the current sprite's position on the 2D stage, no matter if the pen is up or down. No need to set pen color or pen size to draw this text. The width W and height H define a rectangle area centered at the sprite's position, and the text will be scaled up to fit into this area while keeping its original aspect ratio. The text will be in the given COLOR. If the number of seconds T is specified, the text will disappear after that many seconds, otherwise it will stay there forever. You need to first move the sprite to the desired position before printing the text.
- **3D Compatible**: false

#### pen_setdrawing
- **Syntax**: `set drawing [WHERE v] costume`
- **Description**: Set the pen's drawing layer to be 'above' or 'below' the costume of the sprite using the WHERE parameter. For example, if we do not want the costume of the sprite to block the drawing of the pen, we should select 'above'. By default the pen's drawing is below the costume of the sprite.
- **3D Compatible**: false

#### pen_drawrectangle
- **Syntax**: `draw rectangle width (W) height (H) fill color [FILL] border width (BORDERWIDTH) color [BORDERCOLOR] corner radius (RADIUS) rotation (ROTATION)`
- **Description**: Draw a rectangle centered at the sprite's position
- **3D Compatible**: false

#### pen_drawoval
- **Syntax**: `draw oval width (W) height (H) fill color [FILL] border width (BORDERWIDTH) color [BORDERCOLOR] rotation (ROTATION)`
- **Description**: Draw an oval centered at the sprite's position, no matter if the pen is up or down. No need to set pen color or pen size to draw this oval. You do need to move the sprite to the desired position before drawing the oval. W and H define the width and height of the oval. The fill color is FILL, the border width is BORDERWIDTH, and border color is BORDERCOLOR. The direction of the oval is determined by the ROTATION parameter and is unrelated to the sprite's orientation, so you need to set the rotation parameter correctly.
- **3D Compatible**: false

**MISSING TRADITIONAL SCRATCH PEN BLOCKS**:
- No "pen up" or "pen down" blocks
- No "set pen color to" block
- No "change pen color by" block
- No "set pen size to" block
- No "stamp" block
- No continuous line drawing while sprite moves

---

## 3. MOTION BLOCKS (38 blocks total)

These blocks are essential for creating algorithmic patterns through movement and positioning.

### Basic Positioning

#### motion_gotoxy
- **Syntax**: `go to x: (XPOS) y: (YPOS)`
- **3D Compatible**: true
- **Use**: Position sprite for drawing at specific coordinates

#### motion_setx / motion_sety
- **Syntax**: `set x to (N)` / `set y to (N)`
- **3D Compatible**: true
- **Use**: Set individual x or y coordinates

#### motion_changexby / motion_changeyby
- **Syntax**: `change x by (N)` / `change y by (N)`
- **3D Compatible**: true
- **Use**: Relative positioning for iterative patterns

#### motion_xposition / motion_yposition
- **Syntax**: `(x position)` / `(y position)`
- **3D Compatible**: true
- **Use**: Reporter blocks to get current position

### Rotation and Direction

#### motion_pointindirection
- **Syntax**: `point in direction (DIR)`
- **3D Compatible**: true
- **Use**: Set sprite direction for radial patterns

#### motion_turnright / motion_turnleft
- **Syntax**: `turn cw (N) degrees` / `turn ccw (N) degrees`
- **3D Compatible**: true
- **Use**: Critical for spirals, stars, polygons

#### motion_direction
- **Syntax**: `(direction)`
- **3D Compatible**: true
- **Use**: Get current direction

#### motion_jrpointright / motion_jrpointleft / motion_jrpointup / motion_jrpointdown
- **Syntax**: `point right` / `point left` / `point up` / `point down`
- **Description**: Point to cardinal directions (90, -90, 0, 180 degrees)
- **3D Compatible**: false

### Movement

#### motion_movesteps
- **Syntax**: `move (N) steps`
- **3D Compatible**: true
- **Use**: Move forward in current direction

#### motion_jrforward_2 / motion_jrbackward_2
- **Syntax**: `move forward` / `move backward`
- **Description**: Move sprite forward/backward by a little bit over a short time period
- **3D Compatible**: false

#### motion_jrup_2 / motion_jrdown_2 / motion_jrleft_2 / motion_jrright_2
- **Syntax**: `move up` / `move down` / `move left` / `move right`
- **Description**: Move sprite in cardinal directions by a little bit
- **3D Compatible**: false

### Smooth Movement

#### motion_glidesecstoxy
- **Syntax**: `glide (T) secs to x: (XPOS) y: (YPOS)`
- **3D Compatible**: true
- **Use**: Smooth animated movement for drawing

#### motion_pointtowards_xy
- **Syntax**: `point towards x (XPOS) y (YPOS) in (T) seconds`
- **3D Compatible**: true

### Advanced Motion

#### motion_turnaroundsprite
- **Syntax**: `turn [DIRECTION v] (N) degrees around [SPRITENAME v] in (T) seconds`
- **Description**: Turn this sprite left or right around another sprite for N degrees smoothly over T seconds
- **3D Compatible**: false
- **Use**: Orbital patterns, rotation around center

#### motion_shakescreen
- **Syntax**: `shake screen duration [DURATION] frame rate [FRAMERATE] magnitude [MAGNITUDE]`
- **Description**: Shake the entire stage with all sprites in it
- **3D Compatible**: true

### Viewport Control (for large canvas art)

#### motion_vpxposition / motion_vpyposition
- **Syntax**: `viewport x` / `viewport y`
- **Description**: Position of viewport over canvas
- **3D Compatible**: false

#### motion_move_viewport
- **Syntax**: `move viewport to x (XPOS) y (YPOS)`
- **3D Compatible**: false

#### motion_attachtoviewport / motion_detachfromviewport
- **3D Compatible**: false
- **Use**: Fix sprite position relative to viewport

### 3D Motion

#### motion_zposition / motion_setz / motion_changezby
- **Syntax**: `(z position)` / `set z to (N)` / `change z by (N)`
- **3D Compatible**: true
- **Use**: 3D positioning for depth effects

---

## 4. OPERATORS FOR MATHEMATICAL ART (30 blocks total)

### Vector and Distance Calculations

#### operator_vector_distance
- **Syntax**: `distance between x (X1) y (Y1) and x (X2) y (Y2) [METHOD v]`
- **Description**: Calculate distance between two points (direct or manhattan)
- **Use**: Spacing calculations, proximity-based patterns

#### operator_vector_distance3d
- **Syntax**: `distance between x (X1) y (Y1) z (Z1) and x (X2) y (Y2) z (Z2) [METHOD v]`
- **3D Compatible**: true

#### operator_vector_direction
- **Syntax**: `direction from x (X1) y (Y1) to x (X2) y (Y2)`
- **Description**: Returns direction in degrees from first point to second
- **Use**: Dynamic direction calculations for generative patterns

### Math Functions (Standard Scratch blocks not shown in detail)
- Addition, subtraction, multiplication, division
- Random number generation
- Trigonometric functions (sin, cos, tan)
- Square root, power, logarithm
- Rounding, floor, ceiling, absolute value
- Modulo operator

---

## 5. 3D OBJECT CREATION (50 blocks total)

For 3D generative art and algorithmic sculptures.

### Basic 3D Shapes

#### d3object_d3_addbox
- **Syntax**: `add box [COLOR] size in x (SIZEX) y (SIZEY) z (SIZEZ) edge radius (R) as [NAME]`
- **Use**: 3D voxel art, architectural patterns

#### d3object_d3_add6box
- **Syntax**: `add 6-colored box [COLOR1] [COLOR2] [COLOR3] [COLOR4] [COLOR5] [COLOR6] size in x (SIZEX) y (SIZEY) z (SIZEZ) as [NAME]`
- **Use**: Colorful 3D patterns

#### d3object_d3_addsphere
- **Syntax**: `add sphere [COLOR] size in x (SIZEX) y (SIZEY) z (SIZEZ) arc (ARC) slice (SLICE) sides (SIDES) as [NAME]`
- **Use**: Sphere packing, bubble patterns

#### d3object_d3_addcylinder
- **Syntax**: `add cylinder [COLOR] diameter top (DIAMETERTOP) bottom (DIAMETERBOTTOM) height (HEIGHT) arc (ARC) closed section [CLOSEDSECTION v] cap type [CAPTYPE v] sides (SIDES) as [NAME]`
- **Use**: Column patterns, cylindrical art

#### d3object_d3_addcapsule
- **Syntax**: `add capsule [COLOR] diameter top (TOPD) bottom (BOTTOMD) height (H) sides (SIDES) as [NAME]`

#### d3object_d3_addtorus
- **Syntax**: `add torus [COLOR] diameter (D) thickness (THICKNESS) sides (SIDES) as [NAME]`
- **Use**: Donut patterns, linked structures

#### d3object_d3_addcone
- **Syntax**: `add cone [COLOR] vertex list [LISTNAME v] height (H) as [NAME]`
- **Use**: Custom-base cones, pyramid patterns

### 3D Lines and Curves

#### d3object_d3_addsolidline
- **Syntax**: `add line [COLOR] diameter (DIAMETER) cap [CAP v] arrow [ARROW v] sides (SIDES) xyz from (X1) (Y1) (Z1) to (X2) (Y2) (Z2) segments (SEGMENTS) as [NAME]`
- **Use**: 3D line art, connecting structures

#### d3object_d3_adddottedline
- **Syntax**: `add dotted line [COLOR] diameter (DIAMETER) segment length (SEGMENTLENGTH) gap length (GAPLENGTH) cap [CAP v] arrow [ARROW v] sides (SIDES) from xyz (X1) (Y1) (Z1) to xyz (X2) (Y2) (Z2) as [NAME]`

#### d3object_d3_addcurveusinglist
- **Syntax**: `add curve [COLOR] diameter (D) cap [CAPTYPE v] arrow [ARROWTYPE v] sides (S) using list [LISTNAME v] from (STARTINDEX) to (ENDINDEX) segments (SEGMENTCOUNT) as [NAME]`
- **Description**: Creates a 3D curve by connecting points given in a list
- **Use**: Parametric curves, 3D spirals

#### d3object_d3_generatearcpoints
- **Syntax**: `generate arc points from (X1) (Y1) (Z1) via (X2) (Y2) (Z2) to (X3) (Y3) (Z3) into list [LISTNAME v] count (N)`
- **Use**: Generate points for smooth curves

### Custom 3D Shapes

#### d3object_d3_addcolumn
- **Syntax**: `add column [COLOR] 2D vertex list [LISTNAME v] height (H) cap type [CAPTYPE v] as [NAME]`
- **Description**: Create a 3D column by extruding a 2D shape vertically
- **Use**: Custom prismatic patterns

#### d3object_d3_addtube / d3object_d3_addrecttube
- **Use**: Hollow structures, tube networks

#### d3object_d3_addstairs
- **Syntax**: `add stairs [COLOR] width (W) depth (D) height (H) count (COUNT) thickness (THICKNESS) type [TYPE v] as [NAME]`
- **Use**: Step patterns, terraced structures

### 3D Text

#### d3object_d3_addtext
- **Syntax**: `add 3D text [TEXT] font [FONT v] color [COLOR] width (WIDTH) height (HEIGHT) diameter (DIAMETER) camera facing [CAMERAFACING v] as [NAME]`
- **Use**: 3D typography art

#### d3object_d3_addtext2
- **Syntax**: `add 3D thick text [TEXT] font [FONT v] color [COLOR] width (WIDTH) height (HEIGHT) thickness (THICKNESS) diameter (DIAMETER) camera facing [CAMERAFACING v] as [NAME]`
- **Use**: Extruded text sculptures

### Object Management

#### d3object_d3_removeobject
- **Syntax**: `remove object named [NAME]`

#### d3object_d3_removeallobjects
- **Syntax**: `remove all objects`

#### d3object_d3_setasparent / d3object_d3_removeparent / d3object_d3_removechildren
- **Use**: Hierarchical object structures

---

## 6. 3D EFFECTS AND PARTICLES (18 blocks)

For generative particle systems and visual effects.

### Particle Emitters

#### d3effect_d3_addgenerator
- **Syntax**: `add prebuilt emitter for [TYPE v] [COLOR1] [COLOR2] capacity (C) texture size (TEXTURESIZE) source size (SOURCESIZE) speed (SPEED) max life (MAXLIFE) as [NAME]`
- **Use**: Fire, smoke, sparkle effects

#### d3effect_d3_createemitter
- **Syntax**: `add particle emitter shape [SHAPETYPE v] texture [TEXTURE] facing camera [FACINGCAM v] life min (MINLIFE) max (MAXLIFE) capacity (C) GPU [USEGPU v] time ratio (TIMERATIO)% as [NAME]`
- **Use**: Custom particle systems

#### d3effect_d3_fireemitter / d3effect_d3_emittercommand
- **Use**: Start/stop particle emission

### Emitter Configuration

Multiple blocks for configuring:
- Box, cone, cylinder, sphere, hemispheric, mesh emitters
- Color gradients over particle lifetime
- Size changes over lifetime
- Rotation speed
- Movement direction and speed
- Initial rotation range
- Scale ratios
- Blend modes

#### d3effect_d3_addtrail
- **Syntax**: `add trail diffusion [DIFFUSECOLOR] emission [EMISSIONCOLOR] width (W) segments (N) as [NAME]`
- **Description**: Add a trail that follows object movement
- **Use**: Motion trails, path visualization

---

## 7. CONTROL BLOCKS FOR ITERATION (14 blocks)

Essential for algorithmic patterns.

### Loops

#### control_set_variable_in_loop
- **Syntax**: `for [VARIABLE v] from (START) to (LIMIT) at step (S)`
- **Description**: For-loop with variable control
- **Use**: Critical for iterative patterns, grids

#### control_repeat_on_every
- **Syntax**: `repeat (N) times at intervals of (T) [TIMEUNIT v]`
- **Use**: Timed repetition for animations

### Standard Scratch Control Blocks (not detailed)
- repeat (N) times
- forever
- if/then/else
- wait
- stop

### Loop Control

#### control_break
- **Syntax**: `break`
- **Description**: Break out of current loop

#### control_continue
- **Syntax**: `continue`
- **Description**: Skip to next iteration

---

## 8. SENSING BLOCKS

### Color Detection

#### sensing_readcolor
- **Syntax**: `read color at x (XPOS) y (YPOS) into variables color [VARIABLE1 v] brightness [VARIABLE2 v] saturation [VARIABLE3 v] transparency [VARIABLE4 v]`
- **Description**: Read color at any point on stage
- **Use**: Interactive art based on existing colors, feedback loops

---

## ALGORITHMIC ART USE CASES BY PATTERN TYPE

### 1. SPIRALS
**Required blocks**:
- `repeat (N) times` or `for [i v] from (1) to (360) at step (10)`
- `move (N) steps` - with N increasing each iteration
- `turn cw (N) degrees` - constant angle
- `draw oval` or drawing blocks

**Example pattern**:
```
for [i v] from (1) to (360) at step (10)
  move (i) steps
  turn cw (10) degrees
  draw oval at x (x position) y (y position) width (20) height (20) fill [#FF0000FF]
```

### 2. FRACTALS
**Required blocks**:
- Recursive custom blocks (My Blocks)
- `draw line` for branches
- `turn cw/ccw` for angle changes
- Scaling factors for size reduction

**Example: Tree fractal**
```
define draw tree (length) (angle)
if <(length) > (5)> then
  draw line from current position forward (length) pixels
  turn cw (angle) degrees
  draw tree ((length) * (0.7)) (angle)
  turn ccw ((angle) * (2)) degrees
  draw tree ((length) * (0.7)) (angle)
  turn cw (angle) degrees
```

### 3. TESSELLATIONS AND GRIDS
**Required blocks**:
- `for [x v] from (-240) to (240) at step (50)`
- `for [y v] from (-180) to (180) at step (50)`
- `draw rectangle` or `draw oval`
- Nested loops for 2D grid

### 4. RADIAL PATTERNS (Mandalas, Flowers)
**Required blocks**:
- `for [angle v] from (0) to (360) at step (N)`
- `point in direction (angle)`
- `go to x: (0) y: (0)` - return to center
- `move (N) steps`
- `draw oval` or other shapes

### 5. PARAMETRIC CURVES
**Required blocks**:
- `for [t v] from (0) to (360) at step (1)`
- Math operators: `sin`, `cos`
- `set x to ((cos of (t)) * (radius))`
- `set y to ((sin of (t)) * (radius))`
- `draw line` between consecutive points

### 6. RANDOM GENERATIVE ART
**Required blocks**:
- `pick random (min) to (max)`
- `draw rectangle/oval/line` with random parameters
- `color (C) saturation (S) brightness (B) transparency (T)` with random values
- Loop many times

### 7. 3D GENERATIVE SCULPTURES
**Required blocks**:
- 3D object creation: `add box`, `add sphere`, `add torus`
- Nested loops for 3D grids
- 3D positioning: `set x/y/z to`
- Rotation calculations

### 8. PARTICLE SYSTEMS
**Required blocks**:
- `add particle emitter`
- Configuration blocks for color, movement, size
- `start emitter` with emission rate
- Can create dynamic, animated generative art

---

## KEY FINDINGS FOR T20 SKILLS

### STRENGTHS:
1. **Excellent 2D drawing tools** in Looks category (rectangle, oval, line, bezier curves, text)
2. **Dynamic color generation** with HSBT values
3. **Comprehensive 3D capabilities** (50+ 3D object blocks, particle systems)
4. **Good motion control** (38 blocks) for positioning and rotation
5. **Mathematical operators** including vector distance and direction
6. **For-loops with variables** for precise iteration control
7. **Bezier curves** for organic shapes
8. **Custom 3D shapes** from vertex lists

### LIMITATIONS:
1. **NO traditional Scratch pen blocks**: No pen up/down, no continuous line drawing while moving, no stamp
2. **Limited pen category**: Only 4 pen blocks (text, rectangle, oval, drawing layer)
3. **Drawing is position-based**: Must position sprite, then draw at that location
4. **No continuous path tracing**: Can't draw while sprite moves like traditional Scratch pen

### RECOMMENDED APPROACH FOR ALGORITHMIC ART SKILLS:
1. Use **Looks category drawing blocks** as primary drawing tools
2. Combine with **Motion blocks** for positioning
3. Use **for-loops** for iteration patterns
4. Leverage **dynamic color generation**
5. For 3D art, use extensive **3D Object** and **3D Effect** blocks
6. Focus on **calculated positioning** rather than continuous drawing

### MISSING FROM TRADITIONAL SCRATCH:
- pen up / pen down
- set pen color to (color)
- change pen color by (amount)
- set pen size to (size)
- change pen size by (amount)
- stamp (create copy of sprite costume at current position)
- These blocks DO NOT exist in CreatiCode

---

## RECOMMENDED SKILL STRUCTURE FOR T20

### Beginner Level:
- Draw shapes at specific positions (rectangle, oval, line)
- Create simple repeating patterns with loops
- Use motion blocks to position drawing
- Generate colors dynamically

### Intermediate Level:
- Create spirals (combining move, turn, draw)
- Build radial patterns (loops with angles)
- Draw grids and tessellations (nested loops)
- Use bezier curves for organic designs
- Generate random art compositions

### Advanced Level:
- Fractals with recursive patterns
- Parametric curves using trigonometry
- Complex mandalas and symmetrical designs
- 3D generative sculptures
- Particle-based generative art
- Interactive art using color sensing

Each skill should include:
1. Required blocks with exact syntax
2. Mathematical concepts (angles, distances, coordinates)
3. Loop structures and iteration patterns
4. Color theory and dynamic color generation
5. Example code pattern
6. Variations and extensions
