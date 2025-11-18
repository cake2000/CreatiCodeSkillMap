# Foundational Skills Recommendations - Grade 3 Minimal Viable Curriculum

**Date:** 2025-11-17
**Purpose:** Detailed specifications for creating Grade 3 foundational block skills
**Target:** 41 skills in 3 weeks (Minimum Viable Curriculum)

---

## Overview

This document provides detailed specifications for the **41 critical Grade 3 skills** that must be created to enable coding instruction in CreatiCode.

These skills teach the foundational blocks that students need before they can progress to grades 4-8.

---

## Skill Creation Principles

### 1. One Block, One Skill

Each skill should focus on teaching ONE specific block or ONE specific combination of blocks.

**Good Example:**
- T06.G3.01: Use "when green flag clicked" to start a program

**Bad Example:**
- T06.G3.01: Use events to start programs and respond to clicks (too broad)

### 2. Clear Success Criteria

Every skill must have objective, auto-gradable success criteria.

**Good Example:**
- Success: Sprite moves 10 steps when green flag clicked
- Auto-grade: Check if sprite x position changed by 10

**Bad Example:**
- Success: Make the sprite do something interesting (subjective)

### 3. Minimal Dependencies

Grade 3 skills should have minimal or zero dependencies (students are just starting coding).

**Good Progression:**
- T06.G3.01: when flag clicked (0 dependencies)
- T07.G3.01: wait block (depends on T06.G3.01)
- T07.G3.02: repeat block (depends on T06.G3.01)

### 4. Scaffolding and Support

Provide:
- Starter code (when appropriate)
- Clear instructions
- Visual examples
- Hints for common errors
- XO assistant prompts

### 5. Engagement and Relevance

Use contexts that are:
- Age-appropriate (8-9 year olds)
- Culturally responsive
- Immediately satisfying (visible results)
- Relatable (games, stories, animations)

---

## Week 1: Basic Operations (20 skills)

### Events Block Skills (5 skills)

#### T06.G3.01: Start a Program with Green Flag (GATEWAY SKILL)

**Title:** Make the Cat Move When You Click the Flag

**Learning Objective:** Use "when green flag clicked" to start a program

**Description:**
Students add a "when green flag clicked" event block and make the cat sprite move forward 10 steps.

**Starter Code:**
- Cat sprite on stage at center (0, 0)

**Instructions:**
1. Drag the "when green flag clicked" block to your code area
2. Snap a "move 10 steps" block underneath it
3. Click the green flag to test

**Success Criteria:**
- Code has "when green flag clicked" block
- Code has "move 10 steps" block connected below it
- When flag clicked, sprite x position increases by 10

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "event_whenflagclicked", "required": true},
    {"block": "motion_movesteps", "required": true, "parent": "event_whenflagclicked"}
  ],
  "runtime_checks": [
    {"type": "position_change", "sprite": "Cat", "axis": "x", "min_change": 8, "max_change": 12}
  ]
}
```

**Common Errors & Hints:**
- Blocks not connected: "Make sure the green flag block is on top and the move block is snapped underneath"
- Wrong block: "Look for the green flag block in the Events category (yellow)"

**Dependencies:** None (entry point)

**Estimated Time:** 5-10 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.02: Make a Sprite Respond to Clicks

**Title:** Make the Cat Meow When You Click It

**Learning Objective:** Use "when this sprite clicked" to respond to mouse clicks

**Description:**
Students add a "when this sprite clicked" event and make the cat play a meow sound.

**Starter Code:**
- Cat sprite on stage at center

**Instructions:**
1. Drag the "when this sprite clicked" block to your code area
2. Snap a "play sound meow" block underneath it
3. Click on the cat to test

**Success Criteria:**
- Code has "when this sprite clicked" block
- Code has "play sound" block connected below it
- When sprite clicked, sound plays

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "event_whenthisspriteclicked", "required": true},
    {"block": "sound_play", "required": true, "parent": "event_whenthisspriteclicked"}
  ],
  "runtime_checks": [
    {"type": "sound_played", "trigger": "click_sprite", "sound_name": "meow"}
  ]
}
```

**Dependencies:** T06.G3.01

**Estimated Time:** 5-10 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.03: Use Two Different Events in One Project

**Title:** Flag Makes Cat Move, Click Makes Cat Say Hello

**Learning Objective:** Use multiple event handlers in the same program

**Description:**
Students create a program with two event handlers: clicking the flag makes the cat move, clicking the cat makes it say "Hello!"

**Starter Code:**
- Cat sprite on stage

**Instructions:**
1. Add "when green flag clicked" and make cat move 10 steps
2. Add "when this sprite clicked" and make cat say "Hello!" for 2 seconds
3. Test both events

**Success Criteria:**
- Code has both "when green flag clicked" and "when this sprite clicked"
- Flag click causes movement
- Sprite click causes speech

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "event_whenflagclicked", "required": true},
    {"block": "event_whenthisspriteclicked", "required": true},
    {"block": "motion_movesteps", "required": true},
    {"block": "looks_sayforsecs", "required": true}
  ],
  "runtime_checks": [
    {"type": "position_change", "trigger": "flag_click"},
    {"type": "speech_bubble", "trigger": "sprite_click", "text": "Hello"}
  ]
}
```

**Dependencies:** T06.G3.01, T06.G3.02

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.04: Respond to Arrow Key Presses

**Title:** Make the Cat Walk with Arrow Keys

**Learning Objective:** Use "when key pressed" to respond to arrow key input

**Description:**
Students create four event handlers that move the cat in different directions using arrow keys.

**Starter Code:**
- Cat sprite on stage at center
- Reminder: up arrow changes y, left/right arrows change x

**Instructions:**
1. Add "when right arrow key pressed" → move 10 steps
2. Add "when left arrow key pressed" → move -10 steps
3. Add "when up arrow key pressed" → change y by 10
4. Add "when down arrow key pressed" → change y by -10
5. Test all four arrows

**Success Criteria:**
- Four "when key pressed" blocks (up, down, left, right)
- Each key moves sprite in correct direction
- Sprite position changes correctly for all four keys

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "event_whenkeypressed", "required": 4}
  ],
  "runtime_checks": [
    {"type": "key_movement", "key": "right", "axis": "x", "direction": "positive"},
    {"type": "key_movement", "key": "left", "axis": "x", "direction": "negative"},
    {"type": "key_movement", "key": "up", "axis": "y", "direction": "positive"},
    {"type": "key_movement", "key": "down", "axis": "y", "direction": "negative"}
  ]
}
```

**Dependencies:** T06.G3.01, T06.G3.03

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.05: Respond to Space Bar Press

**Title:** Make the Cat Jump When You Press Space

**Learning Objective:** Use "when space key pressed" event

**Description:**
Students make the cat jump up and down when the space bar is pressed.

**Starter Code:**
- Cat sprite on stage at y=0

**Instructions:**
1. Add "when space key pressed"
2. Make cat change y by 50 (jump up)
3. Wait 0.5 seconds
4. Make cat change y by -50 (fall down)
5. Test with space bar

**Success Criteria:**
- "when space key pressed" event exists
- Sprite moves up then down
- Uses wait for timing

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "event_whenkeypressed", "key": "space", "required": true},
    {"block": "motion_changeyby", "required": 2},
    {"block": "control_wait", "required": true}
  ],
  "runtime_checks": [
    {"type": "jump_motion", "trigger": "space", "up_amount": 50, "down_amount": -50}
  ]
}
```

**Dependencies:** T06.G3.04, T07.G3.01 (wait block)

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

### Control Block Skills - Basics (4 skills)

#### T07.G3.01: Use Wait to Create Timing

**Title:** Make the Cat Walk Slowly Across the Stage

**Learning Objective:** Use "wait" block to control timing between actions

**Description:**
Students make the cat take four slow steps across the stage by adding wait blocks between move blocks.

**Starter Code:**
- Cat sprite on stage at x=-200

**Instructions:**
1. When green flag clicked
2. Move 25 steps
3. Wait 0.5 seconds
4. Repeat steps 2-3 three more times
5. Watch the cat walk slowly

**Success Criteria:**
- Uses wait blocks between movements
- Total movement is ~100 steps
- Takes ~2 seconds to complete

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_wait", "required": true, "min_count": 3}
  ],
  "runtime_checks": [
    {"type": "timed_movement", "duration_min": 1.5, "duration_max": 2.5, "distance": 100}
  ]
}
```

**Dependencies:** T06.G3.01

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-11

---

#### T07.G3.02: Use Repeat to Create Patterns (GATEWAY SKILL)

**Title:** Make the Cat Draw a Square Path

**Learning Objective:** Use "repeat" block to avoid repeating code

**Description:**
Students use a repeat block to make the cat draw a square by moving and turning four times.

**Starter Code:**
- Cat sprite on stage
- Pen extension enabled (or use motion to trace)

**Instructions:**
1. When green flag clicked
2. Use "repeat 4" block
3. Inside repeat: move 50 steps, turn 90 degrees
4. Watch the cat draw a square

**Success Criteria:**
- Uses "repeat 4" block
- Contains move and turn inside repeat
- Cat returns close to starting position

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_repeat", "required": true, "times": 4},
    {"block": "motion_movesteps", "required": true, "parent": "control_repeat"},
    {"block": "motion_turnright", "required": true, "parent": "control_repeat"}
  ],
  "runtime_checks": [
    {"type": "path_pattern", "shape": "square", "tolerance": 10}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.01

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-11

---

#### T07.G3.03: Use Forever for Continuous Motion (GATEWAY SKILL)

**Title:** Make the Cat Spin Forever

**Learning Objective:** Use "forever" block to create continuous behavior

**Description:**
Students make the cat spin continuously using a forever block.

**Starter Code:**
- Cat sprite on stage at center

**Instructions:**
1. When green flag clicked
2. Use "forever" block
3. Inside forever: turn 5 degrees
4. Click flag and watch the cat spin

**Success Criteria:**
- Uses "forever" block
- Contains turn block inside forever
- Cat continues spinning until stopped

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_forever", "required": true},
    {"block": "motion_turnright", "required": true, "parent": "control_forever"}
  ],
  "runtime_checks": [
    {"type": "continuous_rotation", "duration": 3}
  ]
}
```

**Dependencies:** T06.G3.01

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-11

---

#### T07.G3.04: Combine Repeat with Motion

**Title:** Make the Cat Do a Dance Pattern

**Learning Objective:** Combine repeat blocks with multiple motion blocks

**Description:**
Students create a dance by combining repeat with multiple move and turn blocks.

**Starter Code:**
- Cat sprite on stage at center

**Instructions:**
1. When green flag clicked
2. Repeat 4 times:
   - Move 20 steps forward
   - Turn 90 degrees right
   - Move 20 steps backward
   - Turn 90 degrees left
3. Watch the dance

**Success Criteria:**
- Uses repeat block
- Contains multiple motion blocks inside repeat
- Creates a visible pattern

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_repeat", "required": true},
    {"block": "motion_movesteps", "required": true, "min_count": 2, "parent": "control_repeat"},
    {"block": "motion_turnright", "required": true, "parent": "control_repeat"}
  ]
}
```

**Dependencies:** T07.G3.02

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-11

---

### Control Block Skills - Conditionals (4 skills)

#### T08.G3.01: Use If-Then to Check Conditions (GATEWAY SKILL)

**Title:** Make the Cat Meow Only If Touching the Edge

**Learning Objective:** Use "if-then" block to make decisions

**Description:**
Students use an if-then block to check if the cat is touching the edge and make it meow if true.

**Starter Code:**
- Cat sprite on stage
- Event: when green flag clicked, forever

**Instructions:**
1. Inside the forever loop, add "if touching edge"
2. Inside the if: play sound meow
3. Also inside forever (after if): move 5 steps
4. Watch what happens when cat reaches edge

**Success Criteria:**
- Uses "if-then" block
- Uses "touching edge" condition
- Sound plays only when touching edge

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_if", "required": true},
    {"block": "sensing_touchingedge", "required": true, "parent": "control_if"},
    {"block": "sound_play", "required": true, "parent": "control_if"}
  ],
  "runtime_checks": [
    {"type": "conditional_sound", "condition": "touching_edge", "sound": "meow"}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.03 (forever)

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-11

---

#### T08.G3.02: Use If-Then-Else for Two Outcomes

**Title:** Make the Cat Say "Edge!" or "Safe!" Based on Position

**Learning Objective:** Use "if-then-else" for two different outcomes

**Description:**
Students use if-then-else to make the cat say different things based on whether it's near the edge.

**Starter Code:**
- Cat sprite on stage
- Event: when green flag clicked, forever

**Instructions:**
1. Inside forever: if touching edge
2. Then: say "Edge!" for 1 second
3. Else: say "Safe!" for 1 second
4. Also add: move 5 steps
5. Watch the messages change

**Success Criteria:**
- Uses "if-then-else" block
- Different output for true and false branches
- Both messages appear at different times

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_if_else", "required": true},
    {"block": "looks_sayforsecs", "required": 2}
  ],
  "runtime_checks": [
    {"type": "conditional_output", "condition": "touching_edge", "true_output": "Edge", "false_output": "Safe"}
  ]
}
```

**Dependencies:** T08.G3.01

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-11

---

#### T08.G3.03: Use Comparison Operators in Conditionals

**Title:** Make the Cat Say "Big!" When Size is Over 100

**Learning Objective:** Use comparison operators (>, <, =) in if-then blocks

**Description:**
Students use a comparison operator to check if the cat's size is greater than 100.

**Starter Code:**
- Cat sprite on stage at size 50
- Event: when green flag clicked, forever

**Instructions:**
1. Inside forever: change size by 5
2. Add if block: if size > 100
3. Then: say "Big!" for 1 second
4. After if: wait 0.1 seconds
5. Watch the cat grow and announce when big

**Success Criteria:**
- Uses "if-then" with comparison operator (>)
- Compares sprite size to 100
- Message appears only when condition is true

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_if", "required": true},
    {"block": "operator_gt", "required": true, "parent": "control_if"},
    {"block": "looks_size", "required": true},
    {"block": "looks_sayforsecs", "required": true, "parent": "control_if"}
  ],
  "runtime_checks": [
    {"type": "conditional_by_property", "property": "size", "operator": ">", "value": 100}
  ]
}
```

**Dependencies:** T08.G3.01

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-11

---

#### T08.G3.04: Detect Collisions with If-Touching

**Title:** Make the Cat Say "Got You!" When Touching the Ball

**Learning Objective:** Use "if touching sprite" to detect collisions

**Description:**
Students make the cat detect when it touches a ball sprite.

**Starter Code:**
- Cat sprite on stage
- Ball sprite moving across stage
- Event: when green flag clicked, forever for cat

**Instructions:**
1. For cat, inside forever: if touching Ball
2. Then: say "Got you!" for 1 second
3. Also inside forever: make cat follow mouse pointer
4. Try to make the cat catch the ball

**Success Criteria:**
- Uses "if touching sprite" block
- Correctly detects collision with ball
- Message appears only on collision

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_if", "required": true},
    {"block": "sensing_touchingobject", "required": true, "parent": "control_if"},
    {"block": "looks_sayforsecs", "required": true, "parent": "control_if"}
  ],
  "runtime_checks": [
    {"type": "collision_detection", "sprite1": "Cat", "sprite2": "Ball"}
  ]
}
```

**Dependencies:** T08.G3.01

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-11

---

### Operator Block Skills (5 skills)

#### T09.G3.10: Use Addition and Subtraction in Programs

**Title:** Make the Cat Move Forward and Backward by Math

**Learning Objective:** Use + and - operators in motion blocks

**Description:**
Students use math operators to calculate how far the cat should move.

**Starter Code:**
- Cat sprite on stage

**Instructions:**
1. When green flag clicked
2. Move (10 + 5) steps
3. Wait 1 second
4. Move (20 - 5) steps
5. Watch the cat move different amounts

**Success Criteria:**
- Uses + operator in move block
- Uses - operator in move block
- Cat moves correct distances

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "operator_add", "required": true},
    {"block": "operator_subtract", "required": true},
    {"block": "motion_movesteps", "required": 2}
  ],
  "runtime_checks": [
    {"type": "calculated_movement", "first_move": 15, "second_move": 15}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.01

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-12

---

#### T09.G3.11: Use Multiplication and Division

**Title:** Make the Cat Jump High Using Multiplication

**Learning Objective:** Use * and / operators for calculations

**Description:**
Students use multiplication to make the cat jump higher.

**Starter Code:**
- Cat sprite on stage at y=0

**Instructions:**
1. When space key pressed
2. Change y by (10 * 5) - cat jumps up
3. Wait 0.3 seconds
4. Change y by (50 / 1) with negative - cat falls
5. Test the jump

**Success Criteria:**
- Uses * operator
- Uses / operator
- Cat jumps and falls correctly

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "operator_multiply", "required": true},
    {"block": "motion_changeyby", "required": 2}
  ]
}
```

**Dependencies:** T09.G3.10

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-12

---

#### T09.G3.12: Use Pick Random for Unpredictability

**Title:** Make the Cat Move a Random Distance

**Learning Objective:** Use "pick random" to generate random numbers

**Description:**
Students use pick random to make the cat move unpredictable distances.

**Starter Code:**
- Cat sprite on stage

**Instructions:**
1. When green flag clicked
2. Repeat 5 times:
3. Move (pick random 10 to 50) steps
4. Wait 0.5 seconds
5. Watch the cat move different amounts each time

**Success Criteria:**
- Uses "pick random" block
- Random values used in motion
- Movement varies each run

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "operator_random", "required": true},
    {"block": "motion_movesteps", "required": true}
  ],
  "runtime_checks": [
    {"type": "randomized_behavior", "iterations": 5, "varies": true}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.02

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-12

---

#### T09.G3.13: Use Comparison Operators in Conditionals

**Title:** Make the Cat Say "Far!" If x Position > 100

**Learning Objective:** Use >, <, = in if-then blocks

**Description:**
Students use comparison operators to check the cat's position.

**Starter Code:**
- Cat sprite on stage at x=-200
- Event: when green flag clicked, forever

**Instructions:**
1. Inside forever: move 5 steps
2. Add if: if x position > 100
3. Then: say "Far!" for 1 second
4. Else: say "Not far yet" for 1 second
5. Watch messages change as cat moves

**Success Criteria:**
- Uses comparison operator (>)
- Compares x position to 100
- Different messages based on position

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_if", "required": true},
    {"block": "operator_gt", "required": true},
    {"block": "motion_xposition", "required": true}
  ],
  "runtime_checks": [
    {"type": "position_based_output", "axis": "x", "threshold": 100}
  ]
}
```

**Dependencies:** T08.G3.01, T09.G3.10

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-12

---

#### T09.G3.14: Combine Multiple Operators

**Title:** Calculate the Cat's Final Position Using Math

**Learning Objective:** Combine multiple operators in one expression

**Description:**
Students use multiple operators to calculate a final position.

**Starter Code:**
- Cat sprite on stage at x=0

**Instructions:**
1. When green flag clicked
2. Set x to ((10 + 5) * 2) - this calculates 30
3. Wait 1 second
4. Set x to ((50 - 10) / 2) - this calculates 20
5. Watch the cat jump to calculated positions

**Success Criteria:**
- Uses multiple operators in one expression
- Parentheses used for order of operations
- Cat moves to correct calculated positions

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "operator_add", "required": true},
    {"block": "operator_multiply", "required": true},
    {"block": "motion_setx", "required": 2}
  ],
  "runtime_checks": [
    {"type": "calculated_positions", "first_x": 30, "second_x": 20}
  ]
}
```

**Dependencies:** T09.G3.10, T09.G3.11

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-12

---

### Motion Block Skills (2 skills for Week 1)

#### T06.G3.10: Move Sprite Forward with Move Block

**Title:** Make the Cat Walk Across the Stage

**Learning Objective:** Use "move steps" block to move a sprite

**Description:**
Students use the move block to make the cat walk from left to right across the stage.

**Starter Code:**
- Cat sprite on stage at x=-200

**Instructions:**
1. When green flag clicked
2. Repeat 10 times:
3. Move 20 steps
4. Wait 0.2 seconds
5. Watch the cat walk across

**Success Criteria:**
- Uses "move steps" block
- Cat moves from left to right
- Movement is visible and smooth

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "motion_movesteps", "required": true}
  ],
  "runtime_checks": [
    {"type": "horizontal_movement", "direction": "right", "min_distance": 150}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.02

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.11: Turn Sprite with Turn Block

**Title:** Make the Cat Spin in a Circle

**Learning Objective:** Use "turn degrees" block to rotate a sprite

**Description:**
Students use the turn block to make the cat spin.

**Starter Code:**
- Cat sprite on stage at center

**Instructions:**
1. When green flag clicked
2. Repeat 36 times:
3. Turn 10 degrees right
4. Wait 0.05 seconds
5. Watch the cat spin slowly

**Success Criteria:**
- Uses "turn degrees" block
- Cat completes full rotation (360 degrees)
- Rotation is smooth

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "motion_turnright", "required": true}
  ],
  "runtime_checks": [
    {"type": "full_rotation", "degrees": 360, "tolerance": 10}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.02

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

## Week 2: Visual Feedback & Interaction (13 skills)

### Motion Block Skills - Continued (5 skills)

#### T06.G3.12: Move in Four Directions

**Title:** Make the Cat Move Up, Down, Left, and Right

**Learning Objective:** Use "change x by" and "change y by" to move in all directions

**Description:**
Students learn the difference between moving (forward) and changing x/y (directional).

**Starter Code:**
- Cat sprite on stage at center (0, 0)

**Instructions:**
1. When green flag clicked
2. Change x by 50 (move right)
3. Wait 1 second
4. Change y by 50 (move up)
5. Wait 1 second
6. Change x by -50 (move left)
7. Wait 1 second
8. Change y by -50 (move down)
9. Watch the cat make a square path

**Success Criteria:**
- Uses "change x by" for horizontal movement
- Uses "change y by" for vertical movement
- Cat returns close to starting position

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "motion_changexby", "required": 2},
    {"block": "motion_changeyby", "required": 2}
  ],
  "runtime_checks": [
    {"type": "square_path", "tolerance": 5}
  ]
}
```

**Dependencies:** T06.G3.10, T06.G3.11

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.13: Return to Starting Position

**Title:** Make the Cat Return Home After Walking

**Learning Objective:** Use "go to x:y" to position sprite at specific coordinates

**Description:**
Students make the cat walk around and then return to center.

**Starter Code:**
- Cat sprite on stage at center (0, 0)

**Instructions:**
1. When green flag clicked
2. Move 100 steps (cat walks off)
3. Wait 1 second
4. Go to x:0 y:0 (cat returns home)
5. Test multiple times

**Success Criteria:**
- Uses "go to x:y" block
- Cat returns to (0, 0) after moving
- Position is accurate

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "motion_gotoxy", "required": true}
  ],
  "runtime_checks": [
    {"type": "return_to_origin", "final_x": 0, "final_y": 0, "tolerance": 5}
  ]
}
```

**Dependencies:** T06.G3.10, T06.G3.12

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.14: Create Circular Motion

**Title:** Make the Cat Walk in a Circle

**Learning Objective:** Combine move and turn to create circular paths

**Description:**
Students learn that moving + turning creates curves.

**Starter Code:**
- Cat sprite on stage at center

**Instructions:**
1. When green flag clicked
2. Repeat 36 times:
3. Move 5 steps
4. Turn 10 degrees
5. Watch the cat walk in a circle

**Success Criteria:**
- Uses both move and turn in a loop
- Cat traces a circular path
- Returns close to starting point

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_repeat", "required": true},
    {"block": "motion_movesteps", "required": true, "parent": "control_repeat"},
    {"block": "motion_turnright", "required": true, "parent": "control_repeat"}
  ],
  "runtime_checks": [
    {"type": "circular_path", "tolerance": 20}
  ]
}
```

**Dependencies:** T06.G3.10, T06.G3.11, T07.G3.02

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.15: Bounce Off Edges

**Title:** Make the Cat Bounce Back When It Hits the Edge

**Learning Objective:** Use "if on edge, bounce" block

**Description:**
Students make the cat bounce back when it reaches the edge of the stage.

**Starter Code:**
- Cat sprite on stage at center
- Cat facing 0 degrees (right)

**Instructions:**
1. When green flag clicked
2. Forever:
3. Move 5 steps
4. If on edge, bounce
5. Watch the cat bounce back and forth

**Success Criteria:**
- Uses "if on edge, bounce" block
- Cat changes direction when hitting edge
- Cat stays on screen

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "motion_ifonedgebounce", "required": true},
    {"block": "control_forever", "required": true}
  ],
  "runtime_checks": [
    {"type": "bouncing_behavior", "duration": 5, "stays_on_stage": true}
  ]
}
```

**Dependencies:** T06.G3.10, T07.G3.03, T08.G3.01

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.16: Use Glide for Smooth Animation

**Title:** Make the Cat Glide Smoothly Across the Stage

**Learning Objective:** Use "glide to" block for smooth motion

**Description:**
Students compare regular move (instant) with glide (smooth).

**Starter Code:**
- Cat sprite on stage at x=-200

**Instructions:**
1. When green flag clicked
2. Glide 2 seconds to x:200 y:0
3. Wait 1 second
4. Glide 2 seconds back to x:-200 y:0
5. Watch the smooth gliding motion

**Success Criteria:**
- Uses "glide to" block
- Cat moves smoothly (not instantly)
- Correct timing (2 seconds per glide)

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "motion_glideto", "required": 2}
  ],
  "runtime_checks": [
    {"type": "glide_motion", "duration": 2, "smooth": true}
  ]
}
```

**Dependencies:** T06.G3.10, T06.G3.13, T07.G3.01

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

### Looks Block Skills (6 skills)

#### T06.G3.20: Show and Hide Sprites

**Title:** Make the Cat Appear and Disappear

**Learning Objective:** Use "show" and "hide" blocks

**Description:**
Students make the cat disappear and reappear.

**Starter Code:**
- Cat sprite on stage (visible)

**Instructions:**
1. When green flag clicked
2. Wait 1 second
3. Hide
4. Wait 2 seconds
5. Show
6. Say "Surprise!" for 1 second
7. Watch the cat disappear and reappear

**Success Criteria:**
- Uses "hide" block
- Uses "show" block
- Correct timing between hide and show

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "looks_hide", "required": true},
    {"block": "looks_show", "required": true}
  ],
  "runtime_checks": [
    {"type": "visibility_change", "sequence": ["visible", "hidden", "visible"]}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.01

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.21: Make Sprite Say Messages

**Title:** Make the Cat Tell a Story with Speech Bubbles

**Learning Objective:** Use "say for seconds" block

**Description:**
Students make the cat tell a three-part story using say blocks.

**Starter Code:**
- Cat sprite on stage

**Instructions:**
1. When green flag clicked
2. Say "Once upon a time..." for 2 seconds
3. Say "...there was a cat..." for 2 seconds
4. Say "...who loved to code!" for 2 seconds
5. Read the story

**Success Criteria:**
- Uses "say for seconds" block at least 3 times
- Different messages
- Correct timing

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "looks_sayforsecs", "required": 3}
  ],
  "runtime_checks": [
    {"type": "sequential_speech", "messages": 3}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.01

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.22: Switch Costumes to Animate

**Title:** Make the Cat Change Appearance

**Learning Objective:** Use "switch costume" block

**Description:**
Students make the cat switch between different costumes.

**Starter Code:**
- Cat sprite with multiple costumes (cat-a, cat-b)

**Instructions:**
1. When green flag clicked
2. Repeat 5 times:
3. Switch costume to cat-a
4. Wait 0.5 seconds
5. Switch costume to cat-b
6. Wait 0.5 seconds
7. Watch the cat change appearance

**Success Criteria:**
- Uses "switch costume" block
- Switches between at least 2 costumes
- Creates visible animation

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "looks_switchcostumeto", "required": 2}
  ],
  "runtime_checks": [
    {"type": "costume_animation", "costume_changes": 10}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.02

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.23: Use Next Costume for Walking Animation

**Title:** Make the Cat Walk with Animation

**Learning Objective:** Use "next costume" block

**Description:**
Students create a walking animation using next costume.

**Starter Code:**
- Cat sprite with walking costumes

**Instructions:**
1. When green flag clicked
2. Repeat 20 times:
3. Move 10 steps
4. Next costume
5. Wait 0.1 seconds
6. Watch the cat walk with animation

**Success Criteria:**
- Uses "next costume" block
- Combines with movement
- Creates smooth walking animation

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "looks_nextcostume", "required": true},
    {"block": "motion_movesteps", "required": true}
  ],
  "runtime_checks": [
    {"type": "walking_animation", "movement": true, "costume_changes": true}
  ]
}
```

**Dependencies:** T06.G3.22, T06.G3.10

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.24: Change Sprite Size

**Title:** Make the Cat Grow and Shrink

**Learning Objective:** Use "set size" and "change size by" blocks

**Description:**
Students make the cat grow larger and then shrink back.

**Starter Code:**
- Cat sprite on stage at size 100%

**Instructions:**
1. When green flag clicked
2. Repeat 10 times:
3. Change size by 10
4. Wait 0.2 seconds
5. Wait 1 second
6. Set size to 100%
7. Watch the cat grow and reset

**Success Criteria:**
- Uses "change size by" block
- Uses "set size to" block
- Size changes are visible

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "looks_changesizeby", "required": true},
    {"block": "looks_setsizeto", "required": true}
  ],
  "runtime_checks": [
    {"type": "size_animation", "max_size": 200, "reset_size": 100}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.02

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-10

---

#### T06.G3.25: Create Pulsing Effect with Size

**Title:** Make the Cat Pulse Like a Heartbeat

**Learning Objective:** Combine forever and size changes for effects

**Description:**
Students create a pulsing animation using size changes in a loop.

**Starter Code:**
- Cat sprite on stage at size 100%

**Instructions:**
1. When green flag clicked
2. Forever:
3. Repeat 5 times: change size by 5, wait 0.1 seconds
4. Repeat 5 times: change size by -5, wait 0.1 seconds
5. Watch the pulsing effect

**Success Criteria:**
- Uses forever with size changes
- Creates grow-shrink cycle
- Smooth pulsing effect

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_forever", "required": true},
    {"block": "looks_changesizeby", "required": 2}
  ],
  "runtime_checks": [
    {"type": "pulsing_effect", "duration": 3}
  ]
}
```

**Dependencies:** T06.G3.24, T07.G3.03

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-10

---

### Sensing Block Skills (2 skills)

#### T08.G3.10: Detect Sprite Touching Sprite

**Title:** Make the Cat Say "Caught!" When Touching the Ball

**Learning Objective:** Use "touching sprite" block to detect collisions

**Description:**
Students use the touching block to detect when two sprites collide.

**Starter Code:**
- Cat sprite (player controls)
- Ball sprite (moves automatically)

**Instructions:**
1. For Cat: when green flag clicked, forever
2. Follow mouse pointer (go to mouse-pointer)
3. If touching Ball, say "Caught!" for 1 second
4. Try to touch the ball

**Success Criteria:**
- Uses "touching sprite" block
- Correctly detects collision
- Message appears on collision only

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "sensing_touchingobject", "required": true},
    {"block": "control_if", "required": true}
  ],
  "runtime_checks": [
    {"type": "collision_detection", "sprite1": "Cat", "sprite2": "Ball"}
  ]
}
```

**Dependencies:** T08.G3.01, T07.G3.03

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-11

---

#### T08.G3.11: Detect Sprite Touching Edge

**Title:** Make the Cat Stop at the Edge

**Learning Objective:** Use "touching edge" block

**Description:**
Students make the cat stop moving when it reaches the edge.

**Starter Code:**
- Cat sprite on stage

**Instructions:**
1. When green flag clicked, forever
2. If NOT touching edge, then move 5 steps
3. Else say "Edge!" for 1 second
4. Watch what happens at the edge

**Success Criteria:**
- Uses "touching edge" block
- Uses NOT operator
- Cat stops at edge

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "sensing_touchingedge", "required": true},
    {"block": "operator_not", "required": true}
  ],
  "runtime_checks": [
    {"type": "edge_detection", "stops_at_edge": true}
  ]
}
```

**Dependencies:** T08.G3.01, T08.G3.02

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-11

---

## Week 3: Data & Debugging (8 skills)

### Variable Block Skills (5 skills)

#### T09.G3.01: Create and Use a Variable to Track Score (GATEWAY SKILL)

**Title:** Make a Score Counter for the Game

**Learning Objective:** Create a variable and use it to track data

**Description:**
Students create their first variable and use it to count how many times they click the cat.

**Starter Code:**
- Cat sprite on stage

**Instructions:**
1. Create a variable named "score"
2. When green flag clicked: set score to 0
3. When this sprite clicked: change score by 1
4. Click the cat multiple times and watch score increase

**Success Criteria:**
- Variable named "score" exists
- Score starts at 0 when flag clicked
- Score increases by 1 each click
- Score is visible on stage

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"type": "variable_exists", "name": "score", "required": true},
    {"block": "data_setvariableto", "variable": "score", "value": 0, "required": true},
    {"block": "data_changevariableby", "variable": "score", "value": 1, "required": true}
  ],
  "runtime_checks": [
    {"type": "variable_tracking", "variable": "score", "starts_at": 0, "increases": true}
  ]
}
```

**Dependencies:** T06.G3.01, T06.G3.02

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-09

**NOTE:** This is the MOST CRITICAL gateway skill with 297 dependent skills.

---

#### T09.G3.02: Change Variable to Count Events

**Title:** Count How Many Times the Cat Reaches the Edge

**Learning Objective:** Use "change variable by" to count occurrences

**Description:**
Students count how many times an event happens.

**Starter Code:**
- Cat sprite on stage
- Variable "edge count" created

**Instructions:**
1. When green flag clicked: set edge count to 0
2. Forever:
3. Move 5 steps
4. If on edge, bounce
5. If touching edge: change edge count by 1
6. Watch the counter increase

**Success Criteria:**
- Uses "change variable by" block
- Correctly counts edge touches
- Variable increases each time condition is met

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "data_changevariableby", "required": true},
    {"block": "control_if", "required": true}
  ],
  "runtime_checks": [
    {"type": "event_counting", "variable": "edge count", "event": "edge_touch"}
  ]
}
```

**Dependencies:** T09.G3.01, T08.G3.01

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-09

---

#### T09.G3.03: Display Variable on Stage

**Title:** Show and Hide the Score Display

**Learning Objective:** Use "show variable" and "hide variable" blocks

**Description:**
Students control whether variables are visible.

**Starter Code:**
- Cat sprite
- Variable "score" exists

**Instructions:**
1. When green flag clicked: hide variable score, set score to 0
2. Wait 2 seconds
3. Say "Get ready..." for 1 second
4. Show variable score
5. Start counting clicks
6. Watch the score appear after countdown

**Success Criteria:**
- Uses "show variable" block
- Uses "hide variable" block
- Variable visibility changes correctly

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "data_showvariable", "required": true},
    {"block": "data_hidevariable", "required": true}
  ],
  "runtime_checks": [
    {"type": "variable_visibility", "starts_hidden": true, "becomes_visible": true}
  ]
}
```

**Dependencies:** T09.G3.01

**Estimated Time:** 10-15 minutes

**CSTA Code:** 1B-AP-09

---

#### T09.G3.04: Use Variable in Motion

**Title:** Make the Cat Move as Far as the Score

**Learning Objective:** Use variable values in other blocks

**Description:**
Students learn that variables can be used as inputs to other blocks.

**Starter Code:**
- Cat sprite
- Variable "distance" exists

**Instructions:**
1. Create variable "distance"
2. When green flag clicked: set distance to (pick random 10 to 50)
3. Move (distance) steps
4. Say (join "I moved " distance) for 2 seconds
5. Click flag multiple times and see different distances

**Success Criteria:**
- Variable used in move block
- Variable used in say block (with join)
- Distance varies each run

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "motion_movesteps", "uses_variable": true, "required": true},
    {"block": "operator_join", "required": true}
  ],
  "runtime_checks": [
    {"type": "variable_driven_motion", "randomized": true}
  ]
}
```

**Dependencies:** T09.G3.01, T09.G3.12

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-09

---

#### T09.G3.05: Reset Variable at Start

**Title:** Make a Game That Starts Fresh Each Time

**Learning Objective:** Initialize variables at the start of programs

**Description:**
Students learn to reset game state at the beginning.

**Starter Code:**
- Cat sprite
- Variables: "score", "lives", "level"

**Instructions:**
1. Create three variables: score, lives, level
2. When green flag clicked:
3. Set score to 0
4. Set lives to 3
5. Set level to 1
6. Say "Game starting!" for 1 second
7. Test multiple times to see reset

**Success Criteria:**
- All variables reset when flag clicked
- Same starting values each run
- Good initialization practice

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "data_setvariableto", "required": 3},
    {"event": "event_whenflagclicked", "has_initialization": true}
  ],
  "runtime_checks": [
    {"type": "consistent_initialization", "variables": ["score", "lives", "level"]}
  ]
}
```

**Dependencies:** T09.G3.01

**Estimated Time:** 15-20 minutes

**CSTA Code:** 1B-AP-09

---

### Debugging Block Skills (3 skills)

#### T13.G3.01: Use Say Blocks to Debug (GATEWAY SKILL)

**Title:** Find Out Why the Cat Isn't Moving Right

**Learning Objective:** Use say blocks to show variable values and debug

**Description:**
Students are given broken code and must add say blocks to figure out what's wrong.

**Starter Code:**
- Cat sprite
- Code: when flag clicked, set x to 100 (but x never changes due to bug)
- Variable "target x" exists but isn't used

**Instructions:**
1. This code is supposed to move the cat, but it doesn't work
2. Add say blocks to show:
   - What "target x" value is
   - What cat's actual x position is
3. Figure out the bug (target x is set but not used)
4. Fix it by adding: set x to (target x)
5. Explain what was wrong

**Success Criteria:**
- Adds say blocks to show values
- Identifies that variable wasn't being used
- Fixes the code correctly
- Can explain the bug

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "looks_say", "required": 2, "context": "debugging"},
    {"block": "motion_setx", "uses_variable": true, "required": true}
  ],
  "runtime_checks": [
    {"type": "bug_fixed", "original_bug": "unused_variable", "fixed": true}
  ]
}
```

**Dependencies:** T06.G3.01, T06.G3.21, T09.G3.01

**Estimated Time:** 20-25 minutes

**CSTA Code:** 1B-AP-15

**NOTE:** Gateway debugging skill

---

#### T13.G3.02: Test Code Incrementally

**Title:** Build and Test a Program Step by Step

**Learning Objective:** Test each part of code before adding more

**Description:**
Students build a complex program by testing each block before adding the next.

**Starter Code:**
- Cat sprite on stage

**Instructions:**
1. Step 1: Add "when flag clicked", test it (nothing happens - OK)
2. Step 2: Add "move 10 steps", test it (cat moves - OK)
3. Step 3: Add "repeat 5" around the move, test it (cat moves 50 - OK)
4. Step 4: Add "turn 72 degrees" after move, test it (cat draws pentagon - OK)
5. Step 5: Add "say Done!" at end, test it (cat says done - OK)
6. Explain why testing each step helps

**Success Criteria:**
- Builds program incrementally
- Tests after each addition
- Final program works correctly
- Can explain benefit of incremental testing

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"block": "control_repeat", "required": true},
    {"block": "motion_movesteps", "required": true},
    {"block": "motion_turnright", "required": true}
  ],
  "runtime_checks": [
    {"type": "incremental_development", "tested_steps": 5}
  ]
}
```

**Dependencies:** T06.G3.01, T07.G3.02

**Estimated Time:** 20-25 minutes

**CSTA Code:** 1B-AP-15

---

#### T13.G3.03: Fix Common Errors

**Title:** Debugging Challenge - Fix Three Broken Programs

**Learning Objective:** Identify and fix common coding errors

**Description:**
Students are given three broken programs and must fix each one.

**Starter Code:**
- Three sprites with broken code:
  1. Cat: Move block not connected to event
  2. Dog: Repeat 10 times but only moves 1 step total (should be inside repeat)
  3. Bird: Forever loop without if-then causes continuous speech (annoying)

**Instructions:**
1. Test each sprite's code
2. Identify what's wrong
3. Fix each bug
4. Test again to confirm fix
5. Explain each error

**Success Criteria:**
- Correctly identifies all 3 bugs
- Fixes all 3 bugs
- All programs work after fixes
- Can explain what was wrong

**Auto-Grade Rules:**
```json
{
  "structure_checks": [
    {"type": "connection_error_fixed", "sprite": "Cat"},
    {"type": "scope_error_fixed", "sprite": "Dog"},
    {"type": "logic_error_fixed", "sprite": "Bird"}
  ],
  "runtime_checks": [
    {"type": "all_sprites_functional", "count": 3}
  ]
}
```

**Dependencies:** T13.G3.01, T13.G3.02

**Estimated Time:** 25-30 minutes

**CSTA Code:** 1B-AP-15

---

## Week 4+: Integration & Expansion

### Integration Projects (5-10 skills recommended)

After completing the 41 foundational skills, students should complete integration projects that combine multiple block types. These reinforce learning and build confidence.

**Suggested Integration Projects:**

1. **Simple Catch Game**
   - Combines: Motion, Events, Variables, Sensing, Control
   - Player controls one sprite to catch falling objects
   - Score increases when caught
   - Game ends after time limit

2. **Interactive Story**
   - Combines: Events, Looks, Sound, Control
   - Multiple sprites tell a story
   - User clicks to advance story
   - Backdrop changes between scenes

3. **Animation Showcase**
   - Combines: Looks, Control, Motion
   - Create 3 different animations (grow/shrink, spin, walk)
   - User presses keys to trigger each animation
   - Smooth transitions

4. **Simple Chase Game**
   - Combines: Motion, Events, Sensing, Control, Variables
   - One sprite chases another
   - Player controls the chased sprite with arrow keys
   - Score tracks how long player survives

5. **Pattern Generator**
   - Combines: Motion, Control, Operators, Looks
   - Use repeat and random to create visual patterns
   - Change colors and sizes
   - Different patterns with different keys

---

## Implementation Timeline

### Week 1: Core Foundation
- **Days 1-2:** Events (5 skills)
- **Days 3-5:** Control basics & conditionals (8 skills)
- **Throughout:** Operators (5 skills)
- **Day 5:** Motion basics (2 skills)
- **Total:** 20 skills

### Week 2: Visual & Interactive
- **Days 1-2:** Motion advanced (5 skills)
- **Days 3-5:** Looks (6 skills)
- **Day 5:** Sensing (2 skills)
- **Total:** 13 skills

### Week 3: Data & Debugging
- **Days 1-3:** Variables (5 skills)
- **Days 4-5:** Debugging (3 skills)
- **Total:** 8 skills

### Week 4: Integration
- Integration projects (5-10 skills)
- Testing with students
- Iteration based on feedback

---

## Quality Assurance Checklist

For each skill created, verify:

- [ ] Clear learning objective (one block or concept)
- [ ] Age-appropriate (8-9 year olds)
- [ ] Starter code provided (when needed)
- [ ] Step-by-step instructions
- [ ] Objective success criteria
- [ ] Auto-gradable rules defined
- [ ] Common errors anticipated
- [ ] Hints provided
- [ ] Correct dependencies listed
- [ ] CSTA code assigned
- [ ] Estimated time reasonable (10-30 minutes)
- [ ] Engaging context/theme
- [ ] Tested with at least 3 students

---

## Success Metrics

The Minimal Viable Curriculum (41 skills) will be successful if:

1. **Completion Rate:** 80%+ of Grade 3 students complete all 41 skills
2. **Time on Task:** Average 15 minutes per skill (range 10-30)
3. **Engagement:** <10% abandon rate per skill
4. **Auto-Grade Accuracy:** >95% accurate grading
5. **Mastery:** 80%+ students can create simple projects combining 3+ block types
6. **Teacher Satisfaction:** 85%+ teachers rate skills as "clear and appropriate"

---

## Next Steps

1. **Review & Approve:** Curriculum team reviews these 41 skill specifications
2. **Create First 5:** Start with Events skills (highest priority)
3. **Test Early:** Test first 5 skills with 5-10 students
4. **Iterate:** Refine based on feedback
5. **Scale Production:** Create remaining 36 skills
6. **Full Testing:** Test complete MVC with 30-50 students
7. **Launch:** Deploy to Grade 3 classrooms

---

## Conclusion

These 41 foundational skills represent the **absolute minimum** needed to enable coding instruction in Grade 3. They teach students the core blocks they need before progressing to more complex projects and concepts in grades 4-8.

**Without these 41 skills, students cannot code in CreatiCode.**

Priority 1 is creating these skills as quickly as possible while maintaining quality. The spec provides detailed guidance for each skill, but implementers should feel free to adjust contexts, themes, and exact parameters while keeping the core learning objectives intact.

The goal is to get students coding successfully within 3 weeks of starting Grade 3, building on the strong conceptual foundation from K-2.

---

**For detailed implementation guidance, see:**
- `FOUNDATIONAL_BLOCKS_ANALYSIS.md` - Complete analysis of gaps
- `FOUNDATIONAL_GAPS_CRITICAL.md` - Prioritized list of critical gaps
- `spec_v2_updated.md` - Overall curriculum framework
