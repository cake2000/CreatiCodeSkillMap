# CreatiCode Drawing Blocks - Quick Reference for T20 Skills

## CRITICAL FINDING: CreatiCode Drawing Model is Different from Scratch!

### What CreatiCode HAS:
- **Looks category drawing**: Direct drawing of shapes (rectangle, oval, line, curve, text) at specific x,y positions
- **Pen category**: Only 4 blocks - mainly for drawing shapes centered at sprite position
- **Position-based drawing**: Draw shapes at calculated positions, not continuous tracing

### What CreatiCode DOES NOT HAVE:
- ❌ NO "pen up" / "pen down"
- ❌ NO "set pen color to"
- ❌ NO "set pen size to"
- ❌ NO continuous line drawing while sprite moves
- ❌ NO "stamp" block
- ❌ NO traditional Scratch-style pen drawing

---

## PRIMARY DRAWING BLOCKS (All in Looks Category)

### 1. Rectangle Drawing
```
draw rectangle at x (X) y (Y)
  width (W) height (H)
  fill [COLOR]
  border [COLOR] width (W)
  corner radius (R)
  rotation (ANGLE)
```

### 2. Oval/Circle Drawing
```
draw oval at x (X) y (Y)
  width (W) height (H)
  fill [COLOR]
  border [COLOR] width (W)
  rotation (ANGLE)
```

### 3. Line Drawing
```
draw line in [COLOR]
  from x (X1) y (Y1)
  to x (X2) y (Y2)
  thickness (T)
```

### 4. Bezier Curve Drawing
```
draw curve in [COLOR]
  from x (X1) y (Y1)
  to x (X2) y (Y2)
  control 1 x (CX1) y (CY1)
  control 2 x (CX2) y (CY2)
  thickness (T)
```

### 5. Text Drawing
```
draw text [TEXT]
  at x (X) y (Y)
  size (SIZE)
  color (COLOR)
  rotation (ANGLE)
```

### 6. Dynamic Color Generation
```
color (hue) saturation (sat) brightness (bright) transparency (trans)
```
Returns: "#RRGGBBAA" format color string

### 7. Clear Drawings
```
clear all drawings          // Clear this sprite's drawings
clear all prints            // Clear all sprites' drawings
```

---

## PATTERN CREATION STRATEGIES

### Strategy 1: LOOP + POSITION + DRAW
```
for [i v] from (1) to (100) at step (1)
  set x to ((i) * (10))
  set y to ((sin of (i)) * (50))
  draw oval at x (x position) y (y position) width (5) height (5) fill [#FF0000FF]
```

### Strategy 2: RADIAL PATTERNS
```
for [angle v] from (0) to (360) at step (10)
  set x to (((cos of (angle)) * (100)))
  set y to (((sin of (angle)) * (100)))
  draw rectangle at x (x position) y (y position) width (20) height (20) ...
```

### Strategy 3: GRID PATTERNS
```
for [x v] from (-240) to (240) at step (50)
  for [y v] from (-180) to (180) at step (50)
    draw oval at x (x) y (y) width (40) height (40) ...
```

### Strategy 4: SPIRAL
```
for [i v] from (0) to (360) at step (5)
  set x to ((((cos of (i)) * (i)) / (3)))
  set y to ((((sin of (i)) * (i)) / (3)))
  draw oval at x (x) y (y) width (10) height (10) ...
```

### Strategy 5: CONNECTING LINES
```
set [x1 v] to (x position)
set [y1 v] to (y position)
// move or calculate new position
set [x2 v] to (x position)
set [y2 v] to (y position)
draw line in [#0000FFFF] from x (x1) y (y1) to x (x2) y (y2) thickness (2)
```

---

## KEY MOTION BLOCKS FOR POSITIONING

```
go to x: (X) y: (Y)              // Direct positioning
set x to (X)                      // Set x only
set y to (Y)                      // Set y only
change x by (DX)                  // Relative movement
change y by (DY)                  // Relative movement
(x position)                      // Get current x
(y position)                      // Get current y

point in direction (ANGLE)        // Set direction
turn cw (DEGREES) degrees         // Rotate clockwise
turn ccw (DEGREES) degrees        // Rotate counterclockwise
(direction)                       // Get current direction
```

---

## ESSENTIAL MATH BLOCKS

```
(pick random (1) to (100))                        // Random numbers
((A) + (B))   ((A) - (B))   ((A) * (B))  ((A) / (B))  // Arithmetic
([sqrt v] of (N))                                  // Square root
((A) ^ (B))                                        // Power
([sin v] of (ANGLE))                               // Sine
([cos v] of (ANGLE))                               // Cosine
([tan v] of (ANGLE))                               // Tangent
([floor v] of (N))                                 // Round down
([ceiling v] of (N))                               // Round up
((A) mod (B))                                      // Modulo

distance between x (X1) y (Y1) and x (X2) y (Y2) [direct v]   // Vector distance
direction from x (X1) y (Y1) to x (X2) y (Y2)                 // Vector angle
```

---

## CONTROL BLOCKS FOR PATTERNS

```
repeat (N)                                    // Simple repeat
for [var v] from (START) to (END) at step (S) // For loop with variable
forever                                       // Infinite loop
if <condition> then ... else ...              // Conditional
wait (T) [seconds v]                          // Delay
```

---

## 3D GENERATIVE ART BLOCKS

### Basic 3D Shapes
```
add box [COLOR] size in x (X) y (Y) z (Z) edge radius (R) as [NAME]
add sphere [COLOR] size in x (X) y (Y) z (Z) arc (A) slice (S) sides (N) as [NAME]
add cylinder [COLOR] diameter top (D1) bottom (D2) height (H) ... as [NAME]
add torus [COLOR] diameter (D) thickness (T) sides (N) as [NAME]
```

### 3D Lines and Curves
```
add line [COLOR] diameter (D) ... xyz from (X1) (Y1) (Z1) to (X2) (Y2) (Z2) ... as [NAME]
add curve [COLOR] diameter (D) ... using list [points v] ... as [NAME]
```

### 3D Positioning
```
set z to (Z)
change z by (DZ)
(z position)
```

---

## COMMON ALGORITHMIC ART PATTERNS

### 1. CIRCULAR MANDALA
```
repeat (12)
  for [r v] from (20) to (100) at step (20)
    set x to (((cos of (direction)) * (r)))
    set y to (((sin of (direction)) * (r)))
    draw oval at x (x) y (y) width (30) height (30) ...
  turn cw (30) degrees
```

### 2. SPIRAL
```
for [angle v] from (0) to (720) at step (5)
  set x to ((((cos of (angle)) * (angle)) / (4)))
  set y to ((((sin of (angle)) * (angle)) / (4)))
  draw oval at x (x) y (y) width (8) height (8) ...
```

### 3. GRADIENT CIRCLES
```
for [i v] from (0) to (100) at step (5)
  set [hue v] to ((i) * (3.6))
  draw oval at x (0) y (0)
    width ((200) - ((i) * (2)))
    height ((200) - ((i) * (2)))
    fill (color (hue) saturation (100) brightness (100) transparency (0))
```

### 4. FRACTAL TREE (using recursive custom block)
```
define draw-tree (length) (angle)
if <(length) > (10)> then
  set [x1 v] to (x position)
  set [y1 v] to (y position)
  change y by (length)
  draw line from x (x1) y (y1) to x (x position) y (y position) thickness (2)

  turn cw (angle) degrees
  draw-tree ((length) * (0.7)) (angle)
  turn ccw ((angle) * (2)) degrees
  draw-tree ((length) * (0.7)) (angle)
  turn cw (angle) degrees

  set x to (x1)
  set y to (y1)
```

### 5. RANDOM COMPOSITION
```
repeat (100)
  set x to (pick random (-240) to (240))
  set y to (pick random (-180) to (180))
  set [h v] to (pick random (0) to (100))
  set [s v] to (pick random (50) to (100))
  set [b v] to (pick random (50) to (100))
  set [size v] to (pick random (10) to (50))
  draw oval at x (x) y (y)
    width (size) height (size)
    fill (color (h) saturation (s) brightness (b) transparency (20))
```

### 6. PARAMETRIC CURVE (Lissajous)
```
clear all drawings
for [t v] from (0) to (360) at step (2)
  set [x1 v] to (x)
  set [y1 v] to (y)
  set x to ((((sin of ((t) * (3))) * (100)))
  set y to ((((cos of ((t) * (2))) * (100)))
  if <(t) > (0)> then
    draw line from x (x1) y (y1) to x (x) y (y) thickness (1)
```

---

## COLOR STRATEGIES

### Rainbow Gradient
```
for [i v] from (0) to (360) at step (10)
  color (i) saturation (100) brightness (100) transparency (0)
```

### Complementary Colors
```
color (hue) saturation (100) brightness (100) transparency (0)
color ((hue) + (180)) saturation (100) brightness (100) transparency (0)
```

### Monochromatic Variations
```
for [b v] from (20) to (100) at step (20)
  color (220) saturation (80) brightness (b) transparency (0)
```

### Random Pastels
```
color (pick random (0) to (100))
      saturation (pick random (30) to (60))
      brightness (pick random (80) to (100))
      transparency (0)
```

---

## IMPORTANT NOTES FOR T20 SKILLS

1. **Always calculate positions first**, then draw
2. **Use variables** to store previous positions for connecting lines
3. **Combine loops** with trigonometry for circular/radial patterns
4. **Use for-loops** with variables for mathematical progressions
5. **Dynamic colors** with color() function for vibrant patterns
6. **Clear drawings** before starting new patterns
7. **3D art** requires different coordinate system (x right, y forward, z up)
8. **No stamp block**: To repeat a complex shape, use custom blocks with drawing code
9. **Bezier curves** enable organic, flowing designs
10. **Think in coordinates**: CreatiCode drawing is position-based, not path-based

---

## SKILL PROGRESSION

### Level 1: Basic Shape Drawing
- Draw shapes at fixed positions
- Use loops to repeat shapes
- Change colors systematically

### Level 2: Pattern Creation
- Grid patterns with nested loops
- Radial patterns with angles
- Simple spirals

### Level 3: Mathematical Art
- Parametric curves
- Trigonometric patterns
- Dynamic color gradients

### Level 4: Advanced Generative Art
- Recursive fractals
- Complex spirals and roses
- Random generative compositions
- Interactive art with sensing

### Level 5: 3D Generative Art
- 3D object patterns
- Particle systems
- 3D fractals and sculptures
