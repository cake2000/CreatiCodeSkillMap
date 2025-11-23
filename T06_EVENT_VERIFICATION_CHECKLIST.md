# T06 Event Skills Verification Checklist

This document helps verify that T06 skills in the skill map accurately cover all CreatiCode event capabilities.

## Event Categories Found in CreatiCode (44 total)

### 1. Core Events Category (22 blocks)

#### Message/Broadcasting (7 blocks)
- [ ] when I receive [MESSAGE] with parameter
- [ ] broadcast [MESSAGE] with parameter
- [ ] broadcast [MESSAGE] with parameter and wait
- [ ] send [MESSAGE] to sprite
- [ ] send [MESSAGE] with parameter to sprite
- [ ] send [MESSAGE] to sprite and wait
- [ ] send [MESSAGE] with parameter to sprite and wait

#### Touch/Collision (2 blocks)
- [ ] when touching [SPRITENAME]
- [ ] when touching color

#### Drag Events - 2D (3 blocks)
- [ ] when dragging starts
- [ ] when being dragged
- [ ] when dragging stops

#### Mouse Events (4 blocks)
- [ ] when [left/right] mouse button released (with x,y capture)
- [ ] when [left/right] mouse button pressed (with x,y capture)
- [ ] when [left/right] mouse pointer dragged (with x,y capture)
- [ ] when mouse wheel scroll

#### Keyboard Events (3 blocks)
- [ ] when key [variable] pressed
- [ ] when key [variable] released
- [ ] when [KEY] key released

#### Conditional Events (1 block)
- [ ] when <CONDITION> (boolean condition trigger)

#### Variable Events (1 block)
- [ ] when variable [VARIABLENAME] changed (including cloud variables)

#### Setup Events (1 block)
- [ ] prepare for green flag click

### 2. 3D Scene Events (1 block)
- [ ] when 3D scene is initialized

### 3. 2D Physics Events (2 blocks)
- [ ] broadcast [MESSAGE] when colliding with [SPRITENAME]
- [ ] broadcast [MESSAGE] when finish colliding with [SPRITENAME]

### 4. 3D Action Events (7 blocks)

#### 3D Collision (3 blocks)
- [ ] when colliding with [SPRITENAME] (3D version)
- [ ] broadcast when [OBJECT1] and [OBJECT2] overlap (bounding box)
- [ ] broadcast when distance <= D between objects

#### 3D Picking/Dragging (4 blocks)
- [ ] when an object from this sprite is picked
- [ ] when an object from this sprite is being dragged
- [ ] when an object from this sprite stops being dragged
- [ ] when an object from this sprite starts to be dragged

### 5. Widget Events (10 blocks)

#### Widget Interaction (6 blocks)
- [ ] when widget [NAME] clicked
- [ ] when widget [NAME] changes
- [ ] when any button named [BUTTONNAME] clicked
- [ ] when pointer enters widget named [WIDGETNAME]
- [ ] when pointer leaves widget named [WIDGETNAME]
- [ ] when tab [TABNAME] selected

#### Video Widget Events (4 blocks)
- [ ] when video time is (T) seconds for [VIDEONAME]
- [ ] when video [VIDEONAME] paused
- [ ] when video [VIDEONAME] stopped
- [ ] when video [VIDEONAME] start

### 6. Multiplayer Events (2 blocks)
- [ ] when added to game
- [ ] when touching [SPRITENAME] will [STOPTYPE] and trigger [MESSAGE]

---

## Standard Scratch Events (Assumed Built-in)

These are standard Scratch events not explicitly listed in blockdes8.txt but likely supported:
- when green flag clicked
- when this sprite clicked
- when stage clicked
- when [space] key pressed (standard dropdown)
- when backdrop switches to [backdrop]
- when timer > [value]
- when loudness > [value]

---

## T06 Skills Coverage Analysis

### What T06 Skills Should Cover:

1. **Basic Event Handling**
   - Green flag, sprite clicks, key presses
   - Mouse events (basic)
   - Timer and backdrop switches

2. **Message Broadcasting**
   - Basic broadcast/receive
   - Advanced: parameters, targeted sending, wait variants

3. **Collision Detection**
   - 2D sprite collision
   - Color collision
   - 2D physics collision (start/end)
   - 3D collision
   - 3D bounding box overlap
   - 3D distance-based triggers

4. **User Interaction**
   - Keyboard input (standard and variable-based)
   - Mouse input (buttons, wheel, coordinates)
   - Drag and drop (2D sprites)
   - 3D object picking and dragging
   - Widget interactions (buttons, tabs, etc.)

5. **Conditional/Dynamic Events**
   - when <CONDITION> (boolean triggers)
   - Variable change detection
   - Video playback events

6. **3D-Specific Events**
   - Scene initialization
   - 3D collision
   - 3D object interaction

7. **Advanced Features**
   - Multiplayer events
   - Physics events
   - Widget system events
   - Cloud variable watching

---

## Verification Questions for T06 Skills:

1. Does T06 cover message parameters? (Not in standard Scratch)
2. Does T06 cover targeted message sending to specific sprites?
3. Does T06 distinguish between 2D and 3D collision events?
4. Does T06 cover 3D object picking/dragging separately from 2D?
5. Does T06 cover advanced mouse events (button differentiation, coordinate capture)?
6. Does T06 cover widget events?
7. Does T06 cover video playback events?
8. Does T06 cover multiplayer-specific events?
9. Does T06 cover variable change detection?
10. Does T06 cover conditional event triggers (when <CONDITION>)?
11. Does T06 cover 3D scene initialization?
12. Does T06 distinguish between physics collision and basic collision?

---

## Key Enhancements Over Standard Scratch:

### CreatiCode-Specific Features NOT in Standard Scratch:
1. Message parameters (passing data with broadcasts)
2. Targeted messaging (send to specific sprite)
3. Variable-based key detection
4. Mouse button differentiation (left/right)
5. Coordinate capture on mouse events
6. Mouse wheel support
7. All 3D events (initialization, collision, picking, dragging)
8. Widget events (UI system)
9. Video playback events
10. Multiplayer events
11. Physics-specific collision events (separate from basic collision)
12. Distance-based triggers
13. Bounding box overlap detection
14. Variable change watching (especially cloud variables)
15. Conditional event triggers (when <CONDITION>)
16. Sprite dragging events (start, during, stop)

---

## Recommended T06 Skill Structure:

### Phase 1: Basic Events
- Standard Scratch events (green flag, clicks, keys)
- Basic message broadcasting
- Simple collision detection

### Phase 2: Advanced Input
- Mouse events with coordinates
- Variable-based keyboard
- Mouse wheel
- Drag and drop

### Phase 3: 3D Events
- 3D scene initialization
- 3D collision detection
- 3D object picking/dragging

### Phase 4: Advanced Features
- Message parameters
- Targeted messaging
- Widget events
- Video events
- Physics events
- Multiplayer events
- Variable watching
- Conditional triggers

---

## File Reference:
- Source: /media/binyu/USB2/ScratchCopilot/blockdes8.txt
- Full documentation: /media/binyu/USB2/dev/CreatiCodeSkillMap/CREATICODE_EVENT_BLOCKS_COMPREHENSIVE.md
