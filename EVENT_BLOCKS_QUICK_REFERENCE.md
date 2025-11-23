# CreatiCode Event Blocks - Quick Reference

## Total: 44 Event Blocks

### Events Category (22 blocks)
**Messaging (7)**
- when I receive [MSG] with parameter [VAR]
- broadcast [MSG] with parameter [P]
- broadcast [MSG] with parameter [P] and wait
- send [MSG] to sprite [SPRITE]
- send [MSG] with parameter [P] to sprite [SPRITE]
- send [MSG] to sprite [SPRITE] and wait
- send [MSG] with parameter [P] to sprite [SPRITE] and wait

**Touch (2)**
- when touching [SPRITE]
- when touching color [COLOR]

**Drag - 2D (3)**
- when dragging starts
- when being dragged
- when dragging stops

**Mouse (4)**
- when [button] mouse button released at x [X] y [Y]
- when [button] mouse button pressed at x [X] y [Y]
- when [button] mouse pointer dragged to x [X] y [Y]
- when mouse wheel scroll by [N]

**Keyboard (3)**
- when key [var] pressed
- when key [var] released
- when [KEY] key released

**Other (3)**
- when <CONDITION>
- when variable [VAR] changed
- prepare for green flag click

### 3D Scene (1 block)
- when 3D scene is initialized

### 2D Physics (2 blocks)
- broadcast [MSG] when colliding with [SPRITE]
- broadcast [MSG] when finish colliding with [SPRITE]

### 3D Action (7 blocks)
**Collision (3)**
- when colliding with [SPRITE]
- broadcast [MSG] when [OBJ1] and [OBJ2] overlap
- broadcast [MSG] when distance <= D between [OBJ1] and [OBJ2]

**Picking/Dragging (4)**
- when an object from this sprite is picked
- when an object from this sprite is being dragged
- when an object from this sprite stops being dragged
- when an object from this sprite starts to be dragged

### Widgets (10 blocks)
**Interaction (6)**
- when widget [NAME] clicked
- when widget [NAME] changes
- when any button named [NAME] clicked
- when pointer enters widget named [NAME]
- when pointer leaves widget named [NAME]
- when tab [NAME] selected

**Video (4)**
- when video time is (T) seconds for [VIDEO]
- when video [VIDEO] paused
- when video [VIDEO] stopped
- when video [VIDEO] start

### Multiplayer (2 blocks)
- when added to game
- when touching [SPRITE] will [ACTION] and trigger [MSG]

---

## Key CreatiCode Extensions

### Beyond Standard Scratch:
1. Message parameters
2. Targeted message sending
3. Variable-based keyboard
4. Left/right mouse button differentiation
5. Coordinate capture on mouse events
6. Mouse wheel
7. All 3D events
8. Widget system
9. Video events
10. Multiplayer events
11. Physics collision events
12. Distance-based triggers
13. Variable change watching
14. Conditional triggers
15. Sprite dragging lifecycle

### Standard Scratch Events (assumed built-in):
- when green flag clicked
- when this sprite clicked
- when stage clicked
- when [space] key pressed
- when backdrop switches to
- when timer > value
- when loudness > value

---

## Categories by Use Case

### Game Development
- All collision detection (2D touch, 3D collision, physics, distance)
- Input handling (keyboard, mouse, drag)
- Game state (green flag, messages, variables)

### 3D Applications
- Scene initialization
- 3D collision/overlap
- 3D object picking/dragging
- Distance triggers

### UI/Interactive Apps
- Widget events (clicks, changes, hover)
- Video playback
- Tab selection
- Mouse enter/leave

### Multiplayer
- Player joining
- Collision with actions

### Advanced Programming
- Conditional triggers
- Variable watching
- Message parameters
- Targeted messaging

---

Source: /media/binyu/USB2/ScratchCopilot/blockdes8.txt
Full details: CREATICODE_EVENT_BLOCKS_COMPREHENSIVE.md
