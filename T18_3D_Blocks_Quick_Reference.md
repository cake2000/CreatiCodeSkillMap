# T18 3D BLOCKS QUICK REFERENCE TABLE

## Block Count by Category
| Category | Block Count | Primary Purpose |
|----------|------------|-----------------|
| 3D Scene | 47 | Scene setup, camera, lighting, environment |
| 3D Object | 50 | Object creation, primitives, models, avatars |
| 3D Action | 51 | Movement, rotation, collision, interaction |
| 3D Tools | 32 | Materials, textures, transformations |
| 3D Physics | 36 | Physics simulation, forces, constraints |
| 3D Effect | 18 | Particle systems, trails, emitters |
| 3D AR/VR | 5 | Augmented reality features |
| **TOTAL** | **239** | **Complete 3D system** |

## Functional Area Coverage

### 1. Scene & Environment (47 blocks)
- ✅ Scene initialization (Empty, City, Grass Land, etc.)
- ✅ Background color
- ✅ Fog (Linear, Exponential)
- ✅ Skybox (15+ presets: Blue Sky, HDR, Starfield, Mars, etc.)
- ✅ Post-processing (Bloom, Vignette, Antialiasing, Sharpening)
- ✅ Clipping planes (up to 4)
- ✅ Multi-viewport support
- ✅ Virtual joysticks
- ✅ Fullscreen mode
- ✅ Webcam background (AR)

### 2. Camera System (15 blocks)
- ✅ Orbit camera (arc-rotate)
- ✅ Follow camera (third-person)
- ✅ Camera positioning (distance, angles, target)
- ✅ Camera animation
- ✅ Geographic positioning (lat/lon)
- ✅ Camera constraints (min/max radius, angles)
- ✅ Parent-child camera attachment
- ✅ Camera property queries

### 3. Lighting (16 blocks)
- ✅ Ambient/Hemispheric light
- ✅ Directional light (sunlight)
- ✅ Point light
- ✅ Spot light
- ✅ Shadow casting/receiving
- ✅ Glow layers
- ✅ Highlight layers
- ✅ Light exclusion
- ✅ Light management (add/remove/toggle)

### 4. Primitives & Objects (50 blocks)
**Basic Shapes (10):**
- Box, Sphere, Cylinder, Tube, Capsule, Torus, Plane

**Complex Shapes (5):**
- Stairs, Column (extruded polygon), Cone (from base), 6-colored box, Rectangle tube

**Lines & Curves (5):**
- Solid line, Dotted line, Arc points, Curve from list, Moving line

**Text (2):**
- Flat 3D text, Extruded thick text

**Models & Avatars (6):**
- Prebuilt models, GLTF/GLB from URL, Community models
- Built-in avatars, User avatars, Community avatars

**Geometry Tools (6):**
- Points, Lines between points, Triangles, Frame boxes, Angle marks

**Special (8):**
- Transformer nodes, Voxels, Extrusion from costume, Chemistry atoms, SPS

**Management (8):**
- Add/remove objects, Object existence check, Local axes display

### 5. Transformations (20 blocks)
**Position (5):**
- Move to XYZ, Move along direction, Copy position (camera/object)

**Rotation (7):**
- Rotate to angle (per axis), Rotate to direction (XYZ), Turn degrees, Point to position
- Copy direction (camera/object)

**Scale (4):**
- Update scale (animated), Update size (direct), Set/change size

**Speed (4):**
- Forward/Backward/Left/Right rotation speeds

### 6. Materials & Textures (11 blocks)
**Materials (5):**
- PBR color (diffusion, emission, roughness, brightness)
- Grid material, Flat shading, Wireframe mode, Material settings

**Textures (4):**
- Built-in textures, Costume textures, URL textures, Texture properties

**Mirrors (3):**
- Create mirror, Add reflection, Remove reflections

### 7. Interaction (23 blocks)
**Picking (6):**
- Enable/disable picking, Pick events, Picked object/position

**Hovering (5):**
- Enable/disable hovering, Hovered object/position

**Dragging (7):**
- Drag mode, Drag limits, Drag events (start/during/end), Dragged object

**Mapping (1):**
- Screen XY to 3D position

**Speech (1):**
- 3D speech bubbles

**Object Selection (2):**
- Select object by name, Get current object

**Distance (1):**
- 3D distance calculation

### 8. Collision Detection (10 blocks)
**Raycast (4):**
- Enable collision, Collision events, Blocked direction, Collider configuration

**Mesh Collision (1):**
- Mesh collision events

**Overlap (2):**
- Overlap events, Overlap check

**Distance Sensing (4):**
- Configure sensors, Distance queries, Name queries, Distance events

**Distance Between (1):**
- Object distance calculation

### 9. Physics Simulation (36 blocks)
**World Setup (4):**
- Enable physics, Set/update gravity, Frame rate

**Bodies (7):**
- Add body (Box, Sphere, Cylinder, Mesh, Convex Hull)
- Remove body, Freeze/unfreeze bodies

**Properties (4):**
- Restitution, Friction, Damping, Property queries

**Forces (7):**
- Apply force, Apply impulse, Set linear velocity, Set angular velocity
- Speed in direction, Speed toward point/object

**Constraints (7):**
- Lock axes (linear/angular), Speed limits (linear/angular)

**Collision (3):**
- Collision events, Contact queries, Collision groups

**Joints (6):**
- Fixed constraint, Distance constraint, Hinge constraint
- Hinge limits, Motor speed, Remove constraint

**Compound (1):**
- Merge bodies

**Car Physics (7):**
- Enable car, Engine/brake, Steering, Wheel angles, Wheel forces

### 10. Particle Effects (18 blocks)
**Emitters (2):**
- Prebuilt emitters (Smoke, Fire, Explosion, Fountain, Rain, Snow, Firework)
- Custom emitters (Point, Box, Sphere, Hemisphere, Cylinder, Cone, Mesh)

**Configuration (6):**
- Box, Sphere, Hemisphere, Cylinder, Cone, Mesh emitter shapes

**Properties (6):**
- Color animation, Size animation, Scale range, Rotation animation
- Initial rotation, Movement direction, Blend mode

**Control (2):**
- Start emission (rate/count), Actions (start/stop/pause/dispose)

**Trails (1):**
- Motion trail effect

**GPU Support (1):**
- GPU acceleration option

### 11. Advanced Tools (32 blocks)
**Object Ops (4):**
- Clone, Merge (union), Carve (subtraction), Bake transformations

**Instancing (5):**
- Matrix array, Centered matrix, Mirror copies, Radial array, Iterator

**Mesh Edit (2):**
- Subdivide faces, Transform vertices

**Rendering (6):**
- Bounding box, Edges, Skeleton, Rendering layer, Camera facing, Properties

**Export (2):**
- Export GLB, Export STL

**Hierarchies (6):**
- Set parent, Unlink parent/children, Camera parenting

**Avatar (2):**
- Attach to bone, Detach from body

**Animation (3):**
- Add animations, Play animation (avatar), Play animation (model)

**Skeletal (1):**
- Update bone transform

**Properties (1):**
- Get/set object properties

### 12. AR/VR (5 blocks)
- ✅ World camera (back camera AR)
- ✅ Face camera (face tracking with mesh)
- ✅ Logo-based AR anchor
- ✅ Transparent occlusion
- ✅ Inspector debug

## Key Capabilities Summary

### What CreatiCode 3D CAN Do:
1. ✅ Professional 3D rendering (Babylon.js engine)
2. ✅ Full PBR materials (Physically-Based Rendering)
3. ✅ Multiple camera types with animation
4. ✅ Comprehensive lighting with shadows
5. ✅ Extensive primitive library (10+ shapes)
6. ✅ Model loading (GLTF/GLB) from URL/library
7. ✅ Avatar system with skeletal animation
8. ✅ Physics simulation (forces, constraints, car physics)
9. ✅ Particle systems (GPU-accelerated)
10. ✅ Post-processing effects (bloom, vignette, etc.)
11. ✅ Object picking, hovering, dragging
12. ✅ Collision detection (raycast + distance sensors)
13. ✅ Hierarchies and parenting
14. ✅ Texture mapping (built-in, costume, URL)
15. ✅ Mesh operations (merge, carve, subdivide)
16. ✅ Instancing and arrays
17. ✅ AR features (face/world/image tracking)
18. ✅ Export to GLB/STL
19. ✅ Chemistry/geometry visualization tools
20. ✅ 3D text rendering

### Advanced Features:
- Bone-level animation control
- Compound physics bodies
- Hinge constraints with motors
- GPU particle systems
- Multi-camera viewports
- Clipping planes
- Mirror/reflection effects
- Trails and motion blur
- Virtual joysticks
- Geographic camera positioning
- Voxel creation
- SPS optimization
- Custom emitter shapes
- Blend modes

### What Makes It Professional-Grade:
1. **Babylon.js Engine** - Industry-standard WebGL engine
2. **PBR Materials** - Professional rendering quality
3. **Physics Engine** - Full rigid body dynamics
4. **Skeletal Animation** - Avatar and model animation
5. **AR Integration** - Face/world tracking
6. **Export Capability** - GLB/STL file export
7. **GPU Acceleration** - Particle systems
8. **Optimization** - SPS, instancing
9. **Advanced Lighting** - Shadows, glow, highlights
10. **Post-Processing** - Image effects pipeline

## Comparison with T18 Skills

The platform's 3D capabilities **significantly exceed** what might be expected from an educational block-based system. It provides:

- **239 dedicated 3D blocks** (more than most professional 3D engines expose)
- **Full scene graph** with hierarchies
- **Complete physics simulation** (not just simple collision)
- **AR integration** (cutting-edge feature)
- **Professional rendering** (PBR, shadows, post-processing)
- **Export capability** (GLB/STL for 3D printing/sharing)

This is a **production-ready 3D system**, not a toy or educational simplification.

## Files Generated
1. `/media/binyu/USB2/dev/CreatiCodeSkillMap/T18_3D_Blocks_Comprehensive_Analysis.md` - Full detailed analysis
2. `/media/binyu/USB2/dev/CreatiCodeSkillMap/T18_3D_Blocks_Quick_Reference.md` - This quick reference

## Source
Extracted from `/media/binyu/USB2/ScratchCopilot/blockdes8.txt` (2025-11-23)
All blocks with `Category: 3D *` prefix (7 categories, 239 total blocks)
