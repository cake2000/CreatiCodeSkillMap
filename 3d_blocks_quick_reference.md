# CreatiCode 3D Blocks - Quick Reference for T18 Skills Verification

## OVERVIEW
- **Total 3D Blocks**: 239 blocks across 7 categories
- **Engine**: Babylon.js
- **Coordinate System**: X=right, Y=forward, Z=up

---

## CATEGORY BREAKDOWN

### 1. 3D SCENE (47 blocks)
- Scene initialization & management
- Camera control (orbit, follow, viewport)
- Lighting (point, directional, ambient, spot)
- Shadows & visual effects (glow, highlight)
- Post-processing (bloom, vignette, antialiasing)
- Environment (skybox, fog, clipping planes)
- Input controls (joysticks)

### 2. 3D OBJECT (50 blocks)
- **Primitives**: box, sphere, cylinder, capsule, torus, plane
- **Advanced shapes**: tube, stairs, column, cone
- **Lines & curves**: solid, dotted, arcs, curves
- **Text**: flat & thick 3D text
- **Models**: GLB/GLTF from URL, prebuilt, community
- **Avatars**: character models with animations
- **Geometry tools**: points, lines, triangles, angle markers
- **Chemistry**: atoms and molecules
- **Voxels**: textured boxes
- **Hierarchy**: parent-child relationships
- **SPS**: Solid Particle System for instancing

### 3. 3D ACTION (51 blocks)
- **Movement**: position, speed, direction
- **Rotation**: angle, axis, point-to
- **Animations**: avatar & model animations
- **Bones/Skeleton**: attach to body parts, bone manipulation
- **Collision**: raycast-based blocking collision
- **Proximity**: overlap, distance triggers
- **Distance sensors**: 6-directional obstacle detection
- **Picking**: mouse/touch selection
- **Hovering**: mouse-over detection
- **Dragging**: drag objects with constraints
- **Speech bubbles**: 3D text annotations

### 4. 3D TOOLS (32 blocks)
- **Materials**: color (diffusion, emission, roughness, brightness)
- **Textures**: library, costume, URL, grid
- **Material settings**: wireframe, transparency, back-face
- **Scale & size**: percentage & absolute
- **Copying**: clone, matrix, mirror, rotation
- **Mesh operations**: boolean (carve), merge, subdivide
- **Vertex manipulation**: transform vertices
- **Mirror reflections**: create mirrors
- **Visualization**: bounding box, edges, skeleton
- **Export**: GLB, STL

### 5. 3D PHYSICS (36 blocks)
- **Setup**: gravity, frame rate
- **Bodies**: box, sphere, cylinder, mesh (mass, friction, restitution)
- **Movement**: velocity, forces, impulses
- **Rotation**: angular velocity
- **Constraints**: damping, limits, axis locking
- **Joints**: distance, fixed, hinge (with motors)
- **Collision groups**: layer-based filtering
- **Car physics**: 4-wheel vehicle simulation
- **Freeze/unfreeze**: pause physics

### 6. 3D EFFECT (18 blocks)
- **Particle emitters**: prebuilt & custom
- **Shapes**: box, cone, cylinder, sphere, hemispheric, mesh
- **Properties**: color gradients, size, scale, rotation
- **GPU acceleration**: hardware-accelerated particles
- **Trails**: motion trails

### 7. 3D AR/VR (5 blocks)
- AR world tracking (back camera)
- AR face tracking with mesh
- AR image/logo tracking
- Occlusion objects
- Babylon.js inspector

---

## KEY CAPABILITIES FOR SKILL VERIFICATION

### Scene Setup & Environment
✓ Scene initialization with Babylon.js
✓ Background color, fog effects
✓ Skybox support
✓ Post-processing effects (bloom, vignette, etc.)
✓ Clipping planes

### Camera Systems
✓ Orbit camera (arc-rotate)
✓ Follow camera
✓ Custom viewports
✓ Camera limits & constraints
✓ Keyboard & mouse controls
✓ Virtual joysticks
✓ Camera-object parenting

### Object Creation
✓ Basic primitives (8 types)
✓ Advanced shapes (tube, stairs, column, cone)
✓ Lines, curves, arcs
✓ 3D text (flat & thick)
✓ GLB/GLTF model loading
✓ Avatars with animations
✓ Geometry construction
✓ Chemistry molecules
✓ Voxels & extrusion

### Lighting & Shadows
✓ 4 light types (point, directional, ambient, spot)
✓ Shadow casting & receiving
✓ Light intensity & color
✓ Glow effects
✓ Highlight effects

### Materials & Textures
✓ PBR materials (diffusion, emission, roughness)
✓ Texture library
✓ Custom textures (costume, URL)
✓ Grid materials
✓ Wireframe mode
✓ Transparency
✓ Mirror reflections

### Movement & Animation
✓ Position & rotation control
✓ Speed-based movement
✓ Animated transitions
✓ Avatar animations (library)
✓ Model animations (embedded)
✓ Bone manipulation
✓ Parent-child hierarchies

### Interaction & Input
✓ Mouse/touch picking
✓ Hover detection
✓ Object dragging with constraints
✓ Screen-to-3D coordinate conversion
✓ Virtual joysticks
✓ Keyboard/mouse camera control

### Collision & Detection
✓ Raycast collision (blocking)
✓ Bounding box overlap
✓ Distance sensors (6 directions)
✓ Proximity triggers
✓ Physics collision detection

### Physics Simulation
✓ Gravity & physics engine
✓ Physics bodies (multiple shapes)
✓ Forces & impulses
✓ Joints (distance, fixed, hinge)
✓ Car physics (4-wheel)
✓ Collision groups
✓ Damping & limits

### Particle Effects
✓ Custom particle emitters (6 shapes)
✓ Prebuilt effects
✓ GPU acceleration
✓ Color gradients
✓ Size & scale animation
✓ Motion trails

### Advanced Features
✓ Solid Particle System (SPS)
✓ Matrix copying (grids)
✓ Mirror & rotation copying
✓ Boolean operations (carve)
✓ Mesh merge & subdivide
✓ Vertex manipulation
✓ GLB/STL export
✓ AR support (world, face, image tracking)

### Performance
✓ GPU particle systems
✓ Instancing via SPS
✓ Rendering layers
✓ Hardware acceleration

---

## COORDINATE SYSTEM
- **X axis**: Left (-) to Right (+)
- **Y axis**: Back (-) to Forward (+)
- **Z axis**: Down (-) to Up (+)

---

## COMPARISON WITH T18 SKILLS

### T18 Should Include:
1. Scene initialization ✓
2. Primitive shapes ✓
3. Model loading (GLB/GLTF) ✓
4. Camera control ✓
5. Lighting ✓
6. Materials & textures ✓
7. Movement & rotation ✓
8. Animations ✓
9. Physics simulation ✓
10. Collision detection ✓
11. Particle effects ✓
12. User interaction (picking, dragging) ✓
13. AR features ✓

### Unique CreatiCode Features:
- Chemistry molecule builder
- Geometry construction tools
- Voxel system with per-face textures
- Costume extrusion to 3D
- Distance sensors (6 directions)
- Car physics simulation
- Mirror reflections
- Matrix/mirror/rotation copying
- Boolean mesh operations
- Vertex manipulation
- Avatar system with bone attachment
- Speech bubbles in 3D
- AR face tracking with mesh

---

## VERIFICATION CHECKLIST

For each T18 skill, verify:
- [ ] Block syntax matches actual CreatiCode blocks
- [ ] Parameters are accurate (names, types, ranges)
- [ ] Capabilities described are actually available
- [ ] Examples use real block combinations
- [ ] Terminology is consistent with CreatiCode docs
- [ ] No references to non-existent features
- [ ] Edge cases are properly documented

---

## NOTES

1. **Engine**: Uses Babylon.js (not Three.js)
2. **File Formats**: GLB/GLTF for models, STL for export
3. **Physics**: Built-in physics engine (not external library)
4. **Avatars**: Separate from models, with animation library
5. **Instancing**: Via SPS (Solid Particle System)
6. **Materials**: PBR-based with diffusion/emission/roughness
7. **Textures**: Library, costume, or URL sources
8. **Collision**: Both raycast and physics-based options
9. **Coordinate System**: Y-forward (not Y-up like some engines)
