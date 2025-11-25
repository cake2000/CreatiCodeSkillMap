# T18 Block-to-Skill Mapping

**Date**: 2025-11-25

This document maps each CreatiCode 3D block to its corresponding skill (or identifies missing skills).

**Legend**:
- ✓ = Skill exists and correctly maps to block
- ⚠ = Skill exists but has issues
- ❌ = No skill exists for this block

---

## 3D SCENE BLOCKS (47 blocks)

### Scene Setup (16 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `initialize 3D scene` | T18.G3.03 | ⚠ | Exists but has unnecessary deps |
| `show 3D scene` | ❌ | Missing | |
| `when 3D scene is initialized` | ❌ | Missing | Event block |
| `set scene background color` | ❌ | Missing | **NEW in Phase 2** |
| `set scene fog` | T18.G5.06.01 | ⚠ | Mentioned in description but not dedicated skill |
| `set sky` | T18.G8.02.01 | ⚠ | Only covers skybox textures |
| `remove sky` | ❌ | Missing | |
| `set clipping plane` | ❌ | Missing | |
| `remove clipping plane` | ❌ | Missing | |
| `add pipeline vignette` | T18.G8.02.02 | ⚠ | Post-processing, partial coverage |
| `remove pipeline` | ❌ | Missing | |
| `lock pointer` | ❌ | Missing | |
| `show 3D axis` | ❌ | Missing | **NEW in Phase 2** |
| `turn webcam background` | ❌ | Missing | |
| `switch to full screen` | ❌ | Missing | |
| `GPU Available` | ❌ | Missing | Reporter block |

**Coverage**: 3/16 = 19%

---

### Camera Controls (13 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `set [OBJECT] as parent of camera` | ❌ | Missing | |
| `set camera target xyz` | ❌ | Missing | |
| `set camera target object` | ❌ | Missing | |
| `set display region` | ❌ | Missing | Multi-camera viewports |
| `add orbit camera` | T18.G4.03.01 | ⚠ | Wrong dependency (lights) |
| `set camera distance/angles` | ❌ | Missing | |
| `set camera distance lat/long` | ❌ | Missing | |
| `configure camera` | ❌ | Missing | Radius, range, angle limits |
| `add follow camera` | T18.G4.03.02 | ✓ | Good |
| `camera [PROPERTY]` | ❌ | Missing | Reporter |
| `get camera direction` | ❌ | Missing | Reporter |
| `get camera view position` | ❌ | Missing | Maps 3D to screen |

**Coverage**: 2/13 = 15%

---

### Lighting (10 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add point light` | T18.G4.02.03 | ✓ | Good |
| `add directional light` | T18.G4.02.02 | ✓ | Good |
| `add ambient light` | T18.G4.02.01 | ✓ | Good |
| `add spot light` | T18.G6.05.01 | ⚠ | Should be G4, not G6 |
| `cast shadow` | T18.G6.05.02 | ✓ | Good |
| `receives shadow` | ❌ | Missing | |
| `remove all lights` | ❌ | Missing | **NEW in Phase 2** |
| `remove light named` | ❌ | Missing | **NEW in Phase 2** |
| `switch light on/off` | ❌ | Missing | |
| `exclude object from light` | ❌ | Missing | |

**Coverage**: 5/10 = 50%

---

### Glow & Highlight Effects (6 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `create glow layer` | T18.G6.05.03 | ⚠ | Combined with highlight |
| `add to glow layer` | T18.G6.05.03 | ⚠ | Combined skill |
| `remove from glow layer` | ❌ | Missing | |
| `create highlight layer` | T18.G6.05.03 | ⚠ | Combined with glow |
| `add highlight to layer` | T18.G6.05.03 | ⚠ | Combined skill |
| `remove from highlight layer` | ❌ | Missing | |

**Coverage**: 1/6 = 17% (one skill covers multiple blocks)

---

### Joystick Controls (3 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add joystick` | T18.G6.04.02 | ✓ | Good |
| `joystick [PROPERTY]` | ❌ | Missing | Reporter |
| `remove all joysticks` | ❌ | Missing | |

**Coverage**: 1/3 = 33%

---

## 3D OBJECT BLOCKS (50 blocks)

### Basic Shapes (10 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add box` | T18.G3.04.01 | ⚠ | Has unnecessary conditional dep |
| `add 6-colored box` | ❌ | Missing | Different color per face |
| `add sphere` | T18.G3.04.02 | ✓ | Good |
| `add cylinder` | T18.G3.04.03 | ✓ | Good |
| `add tube` | ❌ | Missing | Different from cylinder (hollow) |
| `add rectangle tube` | ❌ | Missing | |
| `add capsule` | T18.G4.01.02 | ⚠ | **CRITICAL: Combined with torus** |
| `add torus` | T18.G4.01.02 | ⚠ | **CRITICAL: Combined with capsule** |
| `add cone` | T18.G7.01.03 | ⚠ | **CRITICAL: Combined with tube/stairs** |
| `add column` (extrude) | T18.G7.01.01 | ✓ | Good |

**Coverage**: 5/10 = 50% (but 3 are multi-block skills!)

---

### Lines & Curves (5 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add line` | ❌ | Missing | |
| `add dotted line` | ❌ | Missing | |
| `add curve` | ❌ | Missing | |
| `generate arc points` | ❌ | Missing | Helper for curves |
| `add moving line` | ❌ | Missing | Dynamic line between objects |

**Coverage**: 0/5 = 0%

---

### Text Objects (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add 3D text` | T18.G7.01.02 | ✓ | Good |
| `add 3D thick text` | ❌ | Missing | With depth/thickness |

**Coverage**: 1/2 = 50%

---

### Planes (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add plane (size)` | T18.G4.01.01 | ✓ | Good |
| `add plane (equation)` | ❌ | Missing | From plane equation |

**Coverage**: 1/2 = 50%

---

### Complex Objects (6 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add stairs` | T18.G7.01.03 | ⚠ | **CRITICAL: Combined with cone/tube** |
| `add model` | T18.G4.04.01 | ⚠ | Wrong dependency |
| `add public object at URL` | ❌ | Missing | |
| `add community model` | ❌ | Missing | |
| `add voxel` | ❌ | Missing | |
| `extrude costume` | ❌ | Missing | 2D costume → 3D |

**Coverage**: 2/6 = 33%

---

### Avatars (3 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add avatar` (type) | T18.G4.04.02 | ✓ | Good |
| `add avatar` (for user) | ❌ | Missing | Different block signature |
| `add user avatar` | ❌ | Missing | Current user |

**Coverage**: 1/3 = 33%

---

### Geometry Tools (6 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `geometry: add point` | ❌ | Missing | |
| `geometry: add point between` | ❌ | Missing | |
| `geometry: add line` | ❌ | Missing | |
| `geometry: add triangle` | ❌ | Missing | |
| `geometry: add frame box` | ❌ | Missing | |
| `geometry: add angle mark` | ❌ | Missing | |

**Coverage**: 0/6 = 0%

---

### Chemistry (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `chemistry: add atom` | ❌ | Missing | |
| `chemistry: add custom atom` | ❌ | Missing | |

**Coverage**: 0/2 = 0%

---

### Object Management (11 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `remove object named` | ❌ | Missing | **NEW in Phase 2** |
| `remove all objects` | ❌ | Missing | **NEW in Phase 2** |
| `add transformer` | ❌ | Missing | |
| `set object from sprite as parent` | ❌ | Missing | |
| `unlink all children` | ❌ | Missing | |
| `unlink parent` | ❌ | Missing | |
| `set camera as parent` | ❌ | Missing | |
| `show local axis` | ❌ | Missing | |
| `object exists` | ❌ | Missing | Boolean reporter |
| `convert to sps` | ❌ | Missing | Solid Particle System |
| `add to sps` | ❌ | Missing | |

**Coverage**: 0/11 = 0%

---

### Properties (3 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `[PROPERTY] of object` | ❌ | Missing | Reporter |
| `set property to` | ❌ | Missing | |
| `property of` | ❌ | Missing | Reporter |

**Coverage**: 0/3 = 0%

---

## 3D ACTION BLOCKS (51 blocks)

### Movement & Rotation (8 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `move to x y z` | T18.G3.05 | ⚠ | Wrong block name in description |
| `rotate to angle around axis` | ❌ | Missing | |
| `rotate to direction xyz` | ❌ | Missing | |
| `turn degrees around axis` | ❌ | Missing | |
| `move along current direction` | ❌ | Missing | |
| `point to position xyz` | ❌ | Missing | |
| `set speed` | ❌ | Missing | **NEW in Phase 2** |
| `distance between objects` | ❌ | Missing | **NEW in Phase 2** |

**Coverage**: 1/8 = 13%

---

### Position & Direction Copying (4 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `copy direction from camera` | ❌ | Missing | **NEW in Phase 2** |
| `copy position from camera` | ❌ | Missing | **NEW in Phase 2** |
| `copy position from object` | ❌ | Missing | |
| `copy direction from object` | ❌ | Missing | |

**Coverage**: 0/4 = 0%

---

### Speech Bubbles (1 block)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `show speech bubble` | T18.G6.06.01 | ✓ | Good |

**Coverage**: 1/1 = 100%

---

### Object Selection (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `select sprite object by name` | ❌ | Missing | |
| `sprite object name` | ❌ | Missing | Reporter |

**Coverage**: 0/2 = 0%

---

### Animations (4 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `start model animation` | T18.G4.05.01 | ⚠ | Unnecessary loop dep |
| `add animations` | ❌ | Missing | |
| `start animation` | ❌ | Missing | |
| `update bone` | ❌ | Missing | Skeletal animation |

**Coverage**: 1/4 = 25%

---

### Avatar Attachment (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `attach to body part` | ❌ | Missing | |
| `detach from body` | ❌ | Missing | |

**Coverage**: 0/2 = 0%

---

### Collision Detection (7 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `turn on collision` | ❌ | Missing | |
| `broadcast on collision` | ❌ | Missing | |
| `when colliding with` | T18.G4.06 | ⚠ | Unclear if physics or non-physics |
| `update collider dimension` | ❌ | Missing | |
| `sprite object blocked` | ❌ | Missing | Boolean reporter |
| `broadcast when overlap` | ❌ | Missing | |
| `broadcast when distance` | ❌ | Missing | |

**Coverage**: 1/7 = 14%

---

### Distance Sensors (3 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `set distance sensor` | ❌ | Missing | 6 directions |
| `name of nearest obstacle` | ❌ | Missing | Reporter |
| `distance to nearest obstacle` | ❌ | Missing | Reporter |

**Coverage**: 0/3 = 0%

---

### Picking (Selection) (7 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `turn on picking` | T18.G6.06.02 | ⚠ | Unclear if single block or multiple |
| `turn off picking` | ❌ | Missing | |
| `picked point x pos` | T18.G6.06.02 | ⚠ | Maybe covered |
| `picked point y pos` | T18.G6.06.02 | ⚠ | Maybe covered |
| `picked point z pos` | T18.G6.06.02 | ⚠ | Maybe covered |
| `picked object name` | T18.G6.06.02 | ⚠ | Maybe covered |
| `when object is picked` | ❌ | Missing | Event |

**Coverage**: 1/7 = 14% (one skill may cover multiple blocks)

---

### Hovering (6 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `turn on hovering` | ❌ | Missing | |
| `turn off hovering` | ❌ | Missing | |
| `hovered object name` | ❌ | Missing | Reporter |
| `hovered point x pos` | ❌ | Missing | Reporter |
| `hovered point y pos` | ❌ | Missing | Reporter |
| `hovered point z pos` | ❌ | Missing | Reporter |

**Coverage**: 0/6 = 0%

---

### Dragging (7 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `set dragging limits` | ❌ | Missing | |
| `set dragging mode` | ❌ | Missing | |
| `dragged object name` | ❌ | Missing | Reporter |
| `when object is being dragged` | ❌ | Missing | Event |
| `when object stops being dragged` | ❌ | Missing | Event |
| `when object starts to be dragged` | ❌ | Missing | Event |

**Coverage**: 0/7 = 0%

---

### Utilities (1 block)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `map screen XY to XYZ` | ❌ | Missing | |

**Coverage**: 0/1 = 0%

---

## 3D TOOLS BLOCKS (32 blocks)

### Colors & Textures (5 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `update color` | T18.G3.06.01 | ⚠ | Wrong block name |
| `update texture` | T18.G5.05.01 | ✓ | Good |
| `update texture using costume` | T18.G5.05.02 | ✓ | Good |
| `add texture with shared file` | ❌ | Missing | |
| `get color of object` | ❌ | Missing | Reporter |

**Coverage**: 2/5 = 40%

---

### Scaling & Size (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `update scale xyz` | ❌ | Missing | |
| `update size xyz` | ❌ | Missing | |

**Coverage**: 0/2 = 0%

---

### Material Settings (5 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `apply grid material` | ❌ | Missing | |
| `material setting` | ❌ | Missing | Wireframe, backface, etc. |
| `convert to flat shading` | ❌ | Missing | |
| `set camera facing mode` | ❌ | Missing | |
| `set rendering layer` | ❌ | Missing | |

**Coverage**: 0/5 = 0%

---

### Export (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `export object as GLB` | T18.G8.03.01 | ✓ | Good |
| `export object as STL` | T18.G8.03.02 | ✓ | Good |

**Coverage**: 2/2 = 100%

---

### Object Operations (5 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `objects are overlapping` | ❌ | Missing | Boolean reporter |
| `bake current transformations` | ❌ | Missing | |
| `carve [OBJECT] with [OBJECT]` | T18.G7.05.02 | ✓ | Good |
| `merge into` | T18.G7.05.01 | ⚠ | Combined with compound physics |
| `copy object` | ❌ | Missing | |

**Coverage**: 2/5 = 40%

---

### Mirroring (4 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `remove all reflections` | ❌ | Missing | |
| `reflect in mirror` | ❌ | Missing | |
| `build mirror` | T18.G8.05.01 | ✓ | Good |
| `copy to mirror position` | ❌ | Missing | |

**Coverage**: 1/4 = 25%

---

### Matrix Copying (3 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `copy by matrix` | T18.G7.02.01 | ✓ | Good |
| `copy by matrix from center` | ❌ | Missing | |
| `copy to rotated position` | T18.G7.02.03 | ✓ | Rotational symmetry |

**Coverage**: 2/3 = 67%

---

### Iteration (1 block)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `for each 3D object` | ❌ | Missing | Loop block |

**Coverage**: 0/1 = 0%

---

### Vertices & Geometry (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `update vertices` | ❌ | Missing | |
| `subdivide faces` | ❌ | Missing | |

**Coverage**: 0/2 = 0%

---

### Visual Aids (3 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `show bounding box` | ❌ | Missing | |
| `show edges` | ❌ | Missing | |
| `show skeleton` | ❌ | Missing | |

**Coverage**: 0/3 = 0%

---

## 3D PHYSICS BLOCKS (36 blocks)

### Physics Setup (4 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `enable physics for scene` | T18.G5.01.01 | ⚠ | Wrong order (after collision) |
| `update gravity` | ❌ | Missing | |
| `set physics frame rate` | ❌ | Missing | |
| `get physics frame rate` | ❌ | Missing | Reporter |

**Coverage**: 1/4 = 25%

---

### Physics Bodies (7 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add physics body` | T18.G5.01.02 + .03 | ✓ | Good (static + dynamic) |
| `update physics property` | T18.G5.02.01 + .02 | ✓ | Good (restitution + friction) |
| `freeze physics body named` | T18.G6.01.03 | ✓ | Good |
| `freeze all physics bodys` | ❌ | Missing | |
| `add physics bodies into compound` | ❌ | Missing | |
| `remove physics body` | ❌ | Missing | |
| `get physics body [PROPERTY]` | ❌ | Missing | Reporter |

**Coverage**: 4/7 = 57%

---

### Movement & Speed (5 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `set physics body speed in facing` | ❌ | Missing | |
| `set physics body speed towards xyz` | ❌ | Missing | |
| `set physics body speed towards object` | ❌ | Missing | |
| `set physics body speed in xyz` | ❌ | Missing | |
| `set physics body rotation speed` | ❌ | Missing | |

**Coverage**: 0/5 = 0%

---

### Forces & Impulses (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `apply force` | T18.G6.01.01 | ⚠ | Combined with impulse |
| `apply impulse` | T18.G6.01.01 | ⚠ | Combined with force |

**Coverage**: 1/2 = 50% (one skill covers both)

---

### Constraints & Limits (4 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `lock physics body speed` | ❌ | Missing | |
| `set physics body damping` | ❌ | Missing | |
| `set rotation speed limit` | ❌ | Missing | |
| `set movement speed limit` | ❌ | Missing | |

**Coverage**: 0/4 = 0%

---

### Joints/Constraints (6 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add distance constraint` | T18.G7.03.01 | ✓ | Good |
| `add fixed constraint` | T18.G7.03.03 | ✓ | Good |
| `add hinge constraint` | T18.G7.03.02 | ✓ | Good |
| `set limits for hinge` | ❌ | Missing | |
| `set speed for hinge` | ❌ | Missing | Motor |
| `remove constraint` | ❌ | Missing | |

**Coverage**: 3/6 = 50%

---

### Collisions (3 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `names of physics bodies in contact` | ❌ | Missing | Reporter |
| `update collision group` | T18.G6.01.02 | ✓ | Good |
| `broadcast on collision between physics bodies` | T18.G5.03.01 + .02 | ✓ | Good |

**Coverage**: 2/3 = 67%

---

### Car Physics (5 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `enable car simulation` | T18.G8.01.01 | ✓ | Good |
| `set car engine force` | ❌ | Missing | |
| `set car wheel angle` | ❌ | Missing | |
| `steer car to angle` | ❌ | Missing | |
| `set car wheel engine force` | ❌ | Missing | Individual wheel control |

**Coverage**: 1/5 = 20%

---

## 3D EFFECT BLOCKS (18 blocks)

### Prebuilt Emitters (1 block)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add prebuilt emitter` | T18.G5.06.02 | ✓ | Good |

**Coverage**: 1/1 = 100%

---

### Custom Particle Emitters (1 block)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add particle emitter` | ❌ | Missing | Custom from scratch |

**Coverage**: 0/1 = 0%

---

### Emitter Shapes (6 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `configure box emitter` | ❌ | Missing | |
| `configure cone emitter` | ❌ | Missing | |
| `configure cylinder emitter` | ❌ | Missing | |
| `configure hemispheric emitter` | ❌ | Missing | |
| `configure mesh emitter` | ❌ | Missing | |
| `configure sphere emitter` | ❌ | Missing | |

**Coverage**: 0/6 = 0%

---

### Emitter Properties (7 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `configure emitter blend mode` | ❌ | Missing | |
| `configure emitter color` | T18.G5.06.03 | ⚠ | Partial - combined with other configs |
| `configure emitter initial rotation` | ❌ | Missing | |
| `configure emitter movement` | ❌ | Missing | |
| `configure emitter rotation speed` | ❌ | Missing | |
| `configure emitter scale` | ❌ | Missing | |
| `configure emitter size` | T18.G5.06.03 | ⚠ | Partial - combined with color |

**Coverage**: 1/7 = 14%

---

### Emitter Control (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `[ACTION] emitter` | ❌ | Missing | Start/stop/pause |
| `start emitter` | ❌ | Missing | With rate |

**Coverage**: 0/2 = 0%

---

### Trails (1 block)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `add trail` | T18.G7.06.02 | ✓ | Good |

**Coverage**: 1/1 = 100%

---

## 3D AR/VR BLOCKS (5 blocks)

### AR Modes (3 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `switch to AR world camera` | T18.G8.04.01 | ✓ | Good |
| `switch to AR face camera` | T18.G8.04.02 | ✓ | Good |
| `switch to AR LOGO` | T18.G8.04.03 | ✓ | Image tracking |

**Coverage**: 3/3 = 100%

---

### AR Tools (2 blocks)

| Block | Skill ID | Status | Notes |
|-------|----------|--------|-------|
| `convert to transparent occlusion` | ❌ | Missing | |
| `show inspector` | ❌ | Missing | |

**Coverage**: 0/2 = 0%

---

## OVERALL SUMMARY

| Category | Blocks | Skills | Coverage | Status |
|----------|--------|--------|----------|--------|
| 3D Scene | 47 | ~15 | 32% | Poor |
| 3D Object | 50 | ~10 | 20% | Very Poor |
| 3D Action | 51 | ~8 | 16% | Very Poor |
| 3D Tools | 32 | ~5 | 16% | Very Poor |
| 3D Physics | 36 | ~15 | 42% | Fair |
| 3D Effect | 18 | ~3 | 17% | Very Poor |
| 3D AR/VR | 5 | ~3 | 60% | Good |
| **TOTAL** | **239** | **~60** | **25%** | **Poor** |

---

## KEY INSIGHTS

1. **Best Coverage**: AR/VR (60%), Physics (42%)
2. **Worst Coverage**: 3D Action (16%), 3D Tools (16%), 3D Effect (17%)
3. **Most Missing**: Object Management (0/11), Hovering (0/6), Dragging (0/7), Geometry Tools (0/6)
4. **Critical Issues**: 3 multi-block skills violating ONE-BLOCK rule

---

## PRIORITY ADDITIONS NEEDED

### Immediate (Top 20 blocks)
1. Distance between objects
2. Set speed
3. Copy position from camera
4. Copy direction from camera
5. Remove object named
6. Remove all objects
7. Remove light named
8. Remove all lights
9. Set scene background color
10. Show 3D axis
11. Distance sensors (3 blocks)
12. Turn on/off hovering
13. Hovered object/position reporters
14. Turn on/off dragging
15. Dragged object reporter
16. For each 3D object
17. Update scale xyz
18. Update size xyz
19. Objects are overlapping
20. Update gravity

### High Priority (Next 20 blocks)
21-40. See comprehensive analysis document for full priority list

---

**Last Updated**: 2025-11-25
