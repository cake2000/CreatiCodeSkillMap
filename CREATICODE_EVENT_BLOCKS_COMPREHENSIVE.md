# COMPREHENSIVE EVENT BLOCKS IN CREATICODE

Source: /media/binyu/USB2/ScratchCopilot/blockdes8.txt
Date: 2025-11-23

## CATEGORY: Events (Core Event Blocks)

### Message Broadcasting & Receiving
1. **when I receive [MESSAGE v] with parameter [VARIABLE v]**
   - Block ID: event_whenbroadcastreceivedwithparam
   - Description: Hat block triggered when MESSAGE is received with optional parameter stored in VARIABLE

2. **broadcast [MESSAGE v] with parameter [P]**
   - Block ID: event_broadcastwithparam
   - Description: Broadcast message to all sprites with optional parameter

3. **broadcast [MESSAGE v] with parameter [P] and wait**
   - Block ID: event_broadcastwithparamandwait
   - Description: Broadcast message with parameter and wait for processing

4. **send [MESSAGE v] to sprite [SPRITENAME v]**
   - Block ID: event_sendmessage
   - Description: Send message to specific sprite only

5. **send [MESSAGE v] with parameter [P] to sprite [SPRITENAME v]**
   - Block ID: event_sendmessagewithparam
   - Description: Send message with parameter to specific sprite

6. **send [MESSAGE v] to sprite [SPRITENAME v] and wait**
   - Block ID: event_sendmessageandwait
   - Description: Send message to sprite and wait for processing

7. **send [MESSAGE v] with parameter [P] to sprite [SPRITENAME v] and wait**
   - Block ID: event_sendmessagewithparamandwait
   - Description: Send message with parameter to sprite and wait

### Touch/Collision Events
8. **when touching [SPRITENAME v]**
   - Block ID: event_whenspritetouchingobject
   - Description: Triggered when sprite touches another sprite

9. **when touching color [TARGETCOLOR]**
   - Block ID: event_whenspritetouchingcolor
   - Description: Triggered when sprite touches specific color

### Drag Events (2D Sprites)
10. **when dragging starts**
    - Block ID: event_whenspritedraggingstarts
    - Description: Triggered when sprite dragging begins

11. **when being dragged**
    - Block ID: event_whenspritebeingdragged
    - Description: Triggered continuously while sprite is being dragged

12. **when dragging stops**
    - Block ID: event_whenspritedraggingstops
    - Description: Triggered when sprite dragging ends

### Mouse Events
13. **when [BUTTON v] mouse button is released at x [XVAR v] y [YVAR v]**
    - Block ID: event_whenleftrightmousebuttonclick
    - Description: Triggered on mouse button release, stores coordinates

14. **when [BUTTON v] mouse button is pressed at x [XVAR v] y [YVAR v]**
    - Block ID: event_whenleftrightmousebuttonpress
    - Description: Triggered on mouse button press, stores coordinates

15. **when [BUTTON v] mouse pointer is dragged to x [XVAR v] y [YVAR v]**
    - Block ID: event_whenleftrightmousebuttonmove
    - Description: Triggered when mouse is dragged, stores coordinates

16. **when mouse wheel scroll by [NVAR v]**
    - Block ID: event_whenmousewheel
    - Description: Triggered on mouse wheel scroll, stores scroll amount

### Keyboard Events
17. **when key [KVAR v] pressed**
    - Block ID: event_whenkeyvariablepressed
    - Description: Triggered when key (stored in variable) is pressed

18. **when key [KVAR v] released**
    - Block ID: event_whenkeyvariablereleased
    - Description: Triggered when key (stored in variable) is released

19. **when [KEY v] key released**
    - Block ID: event_whenkeyreleased
    - Description: Triggered when specific key is released

### Conditional Events
20. **when <CONDITION>**
    - Block ID: event_whenboolean
    - Description: Triggered when boolean condition becomes true

### Variable Events
21. **when variable [VARIABLENAME v] changed**
    - Block ID: event_whenvariablechanged
    - Category: Event (singular)
    - Description: Triggered when variable value changes (works with cloud variables)

### Setup Events
22. **prepare for green flag click**
    - Block ID: event_preparewhenflagclicked
    - Description: Preparation block for green flag click event

---

## CATEGORY: 3D Scene

23. **when 3D scene is initialized**
    - Block ID: d3scene_d3_when3dsceneisready
    - Description: Triggered when 3D scene has been initialized

---

## CATEGORY: 2D Physics

24. **broadcast [MESSAGE] when colliding with [SPRITENAME v]**
    - Block ID: physics_broadcastcollisioneventmessage
    - Description: Broadcast message when 2D physics body starts colliding

25. **broadcast [MESSAGE] when finish colliding with [SPRITENAME v]**
    - Block ID: physics_broadcastcollisioneventmessage2
    - Description: Broadcast message when 2D physics body finishes colliding

---

## CATEGORY: 3D Action

26. **when colliding with [SPRITENAME v]**
    - Block ID: d3action_d3_whenincollision
    - Description: Triggered when 3D object collides with sprite

27. **broadcast [MESSAGE v] when [OBJECTNAME1] from [SPRITENAME1 v] and [OBJECTNAME2] from [SPRITENAME2 v] overlap**
    - Block ID: d3action_d3_broadcastoverlapmessage
    - Description: Broadcast when two 3D objects' bounding boxes overlap

28. **broadcast [MESSAGE v] when [DIMENSION v] distance dlte (D) between [OBJECTNAME1] from [SPRITENAME1 v] and [OBJECTNAME2] from [SPRITENAME2 v]**
    - Block ID: d3action_d3_broadcasdistmessage
    - Description: Broadcast when distance between 3D objects is <= threshold

### 3D Object Picking/Dragging Events
29. **when an object from this sprite is picked**
    - Block ID: d3action_d3_whenobjectpicked
    - Description: Triggered when 3D object is picked/selected

30. **when an object from this sprite is being dragged**
    - Block ID: d3action_d3_whenobjectbeingdragged
    - Description: Triggered continuously while 3D object is dragged

31. **when an object from this sprite stops being dragged**
    - Block ID: d3action_d3_whenobjectenddragged
    - Description: Triggered when 3D object dragging ends

32. **when an object from this sprite starts to be dragged**
    - Block ID: d3action_d3_whenobjectstartdragged
    - Description: Triggered when 3D object dragging begins

---

## CATEGORY: Widgets

### Widget Interaction Events
33. **when widget [NAME v] clicked**
    - Block ID: widget_whenwidgetclicked
    - Description: Triggered when widget is clicked

34. **when widget [NAME v] changes**
    - Block ID: widget_whenwidgetchanges
    - Description: Triggered when widget value/state changes

35. **when any button named [BUTTONNAME v] clicked**
    - Block ID: widget_whenanybuttonnamedclicked
    - Description: Triggered when any button with specified name is clicked

36. **when pointer enters widget named [WIDGETNAME v]**
    - Block ID: widget_whenmouseenter
    - Description: Triggered when mouse pointer enters widget area

37. **when pointer leaves widget named [WIDGETNAME v]**
    - Block ID: widget_whenmouseleave
    - Description: Triggered when mouse pointer leaves widget area

38. **when tab [TABNAME v] selected**
    - Block ID: widget_whentabselected
    - Description: Triggered when tab is selected

### Video Widget Events
39. **when video time is (T) seconds for [VIDEONAME v]**
    - Block ID: widget_whenvideotimeis
    - Description: Triggered when video reaches specific time

40. **when video [VIDEONAME v] paused**
    - Block ID: widget_whenvideoispaused
    - Description: Triggered when video is paused

41. **when video [VIDEONAME v] stopped**
    - Block ID: widget_whenvideoisstopped
    - Description: Triggered when video is stopped

42. **when video [VIDEONAME v] start**
    - Block ID: widget_whenvideostart
    - Description: Triggered when video starts playing

---

## CATEGORY: Multiplayer

43. **when added to game**
    - Block ID: mp_whenaddedtogame
    - Description: Triggered when sprite is added to multiplayer game

44. **when touching [SPRITENAME v] will [STOPTYPE v] and trigger [MESSAGE v] with parameter [PARAMETER]**
    - Block ID: mp_broadcasttouchmessage
    - Description: Specifies behavior and message when sprite touches another in multiplayer

---

## SUMMARY BY CATEGORY

**Events Category**: 22 blocks
- Message/broadcast: 7 blocks
- Touch/collision: 2 blocks
- Drag events (2D): 3 blocks
- Mouse events: 4 blocks
- Keyboard events: 3 blocks
- Conditional: 1 block
- Variable: 1 block
- Setup: 1 block

**3D Scene**: 1 block
**2D Physics**: 2 blocks
**3D Action**: 7 blocks
- Collision: 3 blocks
- Picking/dragging: 4 blocks

**Widgets**: 10 blocks
- Widget interaction: 6 blocks
- Video events: 4 blocks

**Multiplayer**: 2 blocks

**TOTAL EVENT BLOCKS**: 44

---

## NOTES ON STANDARD SCRATCH EVENTS

The following standard Scratch event blocks appear to be built-in and are not explicitly listed in blockdes8.txt:
- when green flag clicked
- when this sprite clicked
- when stage clicked
- when [space] key pressed (standard dropdown version)
- when backdrop switches to [backdrop]
- when timer > [value]
- when loudness > [value]

CreatiCode extends standard Scratch events with advanced features:
- Message parameters for passing data
- Targeted message sending to specific sprites
- Variable-based key events for dynamic key handling
- 3D-specific events (scene initialization, 3D collision, 3D object picking)
- Widget events (UI interaction, video playback)
- Multiplayer events (game joining, collision handling)
- Physics collision events (2D and 3D)
- Advanced mouse events (button differentiation, coordinate tracking)
- Variable change detection (including cloud variables)

---

## KEY DIFFERENCES FROM STANDARD SCRATCH

1. **Enhanced Messaging**: Standard Scratch has basic broadcast/receive. CreatiCode adds:
   - Message parameters
   - Targeted sending to specific sprites
   - Wait variants for synchronization

2. **3D Support**: Extensive 3D event system not in standard Scratch:
   - 3D scene initialization
   - 3D collision detection
   - 3D object picking and dragging
   - Distance-based triggers

3. **Advanced Input**: More sophisticated input handling:
   - Left/right mouse button differentiation
   - Mouse wheel support
   - Coordinate capture on mouse events
   - Variable-based key detection

4. **Widget System**: Complete UI event system:
   - Button/widget clicks
   - Widget value changes
   - Mouse enter/leave events
   - Video playback events
   - Tab selection

5. **Physics Integration**: Dedicated physics events:
   - Collision start/end detection
   - 2D physics body interactions

6. **Multiplayer Support**: Network game events:
   - Player joining
   - Touch with collision behavior

7. **Variable Watching**: Cloud-variable-aware change detection
