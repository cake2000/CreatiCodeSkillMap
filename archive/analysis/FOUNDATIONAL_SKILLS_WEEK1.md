# Grade 3 Foundational Block Skills - Week 1: Core Blocks

**Week Focus:** Events, Loops, Conditionals, Operators, Motion Basics
**Total Skills:** 20
**Estimated Time:** 5-7 hours of instruction

---

## T06: Events (5 skills)

### T06.G3.01 - Start your program with the green flag ⭐ GATEWAY

**Learning Objective:** Use "when green flag clicked" to start a program

**Description:**
Students use the 'when green flag clicked' event block to start a program that makes a sprite move forward 10 steps. The sprite must visibly move when the green flag is clicked, demonstrating understanding of event-driven programming basics.

**Why This Is Gateway:**
This is THE entry point to all block-based coding. Without understanding event handlers, students cannot create any functional program. 190+ skills depend on this foundational concept.

**Starter Code:**
- Cat sprite on stage at center (0, 0)
- Empty script area

**Step-by-Step Instructions:**
1. Look in the Events category (yellow blocks)
2. Drag the "when green flag clicked" block to your script area
3. Look in the Motion category (blue blocks)
4. Find the "move 10 steps" block
5. Snap it underneath the green flag block (you'll hear a click)
6. Click the green flag above the stage to test

**Success Criteria (Auto-Grade):**
- ✅ Code has "when green flag clicked" block
- ✅ Code has "move 10 steps" block connected below it
- ✅ When flag clicked, sprite x position increases by approximately 10
- ✅ Blocks are properly connected (no floating blocks)

**Common Errors & Hints:**
- **Blocks not connected:** "Make sure the green flag block is on top and the move block is snapped underneath. You should hear a click when they connect!"
- **Wrong block:** "Look for the block with a green flag picture in the Events category (yellow)"
- **Nothing happens:** "Did you click the green flag above the stage (not the block in your code)?"

**Assessment Questions:**
- What does the green flag event do?
- Why do we need event blocks?
- What happens if you click the flag multiple times?

**Extension Activity:**
Try changing the number in "move ___ steps" to make the cat move further or backward (use negative numbers).

**Time:** 15 minutes

---

### T06.G3.02 - Make a sprite respond to clicks

**Learning Objective:** Use "when this sprite clicked" to respond to mouse clicks

**Description:**
Students add a 'when this sprite clicked' event that makes the sprite play a sound when clicked. The code must use the event block correctly and produce audio output when the sprite is clicked.

**Starter Code:**
- Cat sprite on stage at center
- Sound library available (meow sound)

**Step-by-Step Instructions:**
1. Find "when this sprite clicked" in Events
2. Drag it to your script area
3. Go to Sound category (pink blocks)
4. Find "play sound [meow]" block
5. Snap it under the sprite clicked event
6. Click on the cat sprite on the stage to test

**Success Criteria (Auto-Grade):**
- ✅ Code has "when this sprite clicked" block
- ✅ Code has "play sound" block connected below it
- ✅ When sprite clicked, sound plays
- ✅ Sound plays each time sprite is clicked

**Common Errors & Hints:**
- **Can't hear sound:** "Check your volume! Also make sure the sound name matches (meow)"
- **Wrong event:** "Make sure you're using 'when this SPRITE clicked' not 'when green flag clicked'"
- **Sound plays but not from clicking:** "Did you connect the sound to the sprite clicked event?"

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

### T06.G3.03 - Use keyboard controls (arrow keys)

**Learning Objective:** Use "when key pressed" to respond to arrow key input

**Description:**
Students create four 'when key pressed' event handlers for the arrow keys that move a sprite in different directions. The sprite must respond to all four arrow keys (up, down, left, right) and move in the correct direction for each key.

**Starter Code:**
- Cat sprite on stage at center
- Hint card showing:
  - Right arrow → move 10 steps
  - Left arrow → move -10 steps
  - Up arrow → change y by 10
  - Down arrow → change y by -10

**Step-by-Step Instructions:**
1. Add "when [right arrow] key pressed" event
2. Connect "move 10 steps" below it
3. Add "when [left arrow] key pressed" event
4. Connect "move -10 steps" below it
5. Add "when [up arrow] key pressed" event
6. Connect "change y by 10" below it
7. Add "when [down arrow] key pressed" event
8. Connect "change y by -10" below it
9. Test all four arrow keys!

**Success Criteria (Auto-Grade):**
- ✅ Four "when key pressed" blocks (one for each arrow)
- ✅ Right arrow moves sprite to the right
- ✅ Left arrow moves sprite to the left
- ✅ Up arrow moves sprite up
- ✅ Down arrow moves sprite down

**Common Errors & Hints:**
- **Up/down not working:** "Remember: up and down use 'change y by' not 'move steps'!"
- **Left goes right:** "For left arrow, use a negative number like -10"
- **Mixed up directions:** "Test each key one at a time. Does the sprite go the right way?"

**Why This Matters:**
Arrow key controls are used in almost every game and interactive project. This is essential for game development.

**Dependencies:** T06.G3.01

**Time:** 20 minutes

---

### T06.G3.04 - Use the space bar for jumping/actions

**Learning Objective:** Use "when space key pressed" event

**Description:**
Students use the 'when space key pressed' event to make a sprite jump by changing y position up then down with a wait block between. The sprite must move up by at least 30 pixels, wait briefly, then return to original position.

**Starter Code:**
- Cat sprite on stage at y=0 (on the ground)
- Hint: A jump has three parts - go up, pause, come down

**Step-by-Step Instructions:**
1. Add "when [space] key pressed" event
2. Add "change y by 50" (jump up)
3. Add "wait 0.5 seconds"
4. Add "change y by -50" (fall down)
5. Press space bar to test the jump

**Success Criteria (Auto-Grade):**
- ✅ Uses "when space key pressed" event
- ✅ Sprite y position increases (jumps up)
- ✅ Wait block creates pause at top of jump
- ✅ Sprite y position decreases back to start (lands)
- ✅ Jump is smooth and visible

**Common Errors & Hints:**
- **Sprite goes up and never comes down:** "Did you forget the second 'change y by' with a negative number?"
- **Too fast to see:** "Make your wait time longer, like 0.5 or 1 second"
- **Goes down instead of up:** "First change should be positive (+50), second should be negative (-50)"

**Real-World Connection:**
The space bar is the most common jump button in games like Mario, Sonic, and many platformers!

**Dependencies:** T06.G3.03

**Time:** 20 minutes

---

### T06.G3.05 - Use multiple events in one project

**Learning Objective:** Use multiple event handlers in the same program

**Description:**
Students create a program with at least two different event handlers (e.g., green flag makes sprite move, clicking sprite makes it speak). Each event must trigger a different action, demonstrating understanding of multiple independent event handlers.

**Starter Code:**
- Cat sprite on stage
- Challenge: Make the cat respond to 3 different things

**Step-by-Step Instructions:**
1. Add "when green flag clicked"
2. Make cat move 20 steps
3. Add "when this sprite clicked"
4. Make cat say "Hello!" for 2 seconds
5. Add "when [space] key pressed"
6. Make cat play a sound
7. Test all three events!

**Success Criteria (Auto-Grade):**
- ✅ Code has at least 2 different event types
- ✅ Each event triggers different action
- ✅ Green flag event works independently
- ✅ Other events work independently
- ✅ Events don't interfere with each other

**Common Errors & Hints:**
- **All actions happen together:** "Make sure each action is connected to its own separate event block"
- **Only one works:** "Each event block should be separate - don't connect them all together"

**Creative Extension:**
Can you make the cat respond to 5 different things? Try adding more keys!

**Dependencies:** T06.G3.01, T06.G3.02

**Time:** 20 minutes

---

## T07: Loops - Basics (4 skills)

### T07.G3.01 - Use wait to create timing ⭐ GATEWAY

**Learning Objective:** Use "wait" block to control timing between actions

**Description:**
Students use the wait block to create pauses between actions, making a sprite take slow steps across the stage. The code must include at least 3 wait blocks between movement commands to create visible delays.

**Why This Is Gateway:**
Timing control is essential for animations, games, and storytelling. This unlocks 205+ dependent skills including all animation and game mechanics.

**Starter Code:**
- Cat sprite at x=-200 (left side of stage)
- Goal: Make cat walk slowly (not teleport!)

**Step-by-Step Instructions:**
1. When green flag clicked
2. Move 25 steps
3. **Wait 0.5 seconds** ← This creates the slow walk!
4. Move 25 steps
5. **Wait 0.5 seconds**
6. Move 25 steps
7. **Wait 0.5 seconds**
8. Move 25 steps
9. Watch the cat walk slowly across!

**Success Criteria (Auto-Grade):**
- ✅ Uses wait blocks between movements
- ✅ At least 3 wait blocks present
- ✅ Total movement is ~100 steps
- ✅ Takes at least 1.5 seconds to complete
- ✅ Visible slow movement (not instant)

**Common Errors & Hints:**
- **Cat moves instantly:** "Did you add wait blocks BETWEEN each move?"
- **Too slow/too fast:** "Try changing the wait time - 0.5 seconds is good for walking"
- **Wait before first move:** "The first move should happen right away - wait goes BETWEEN moves"

**Explore Time:**
- What happens with wait 0.1 seconds? (faster)
- What happens with wait 2 seconds? (very slow)
- Can you make the cat walk in slow motion?

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

### T07.G3.02 - Use repeat to make patterns ⭐ GATEWAY

**Learning Objective:** Use "repeat" block to avoid repeating code

**Description:**
Students use a repeat block to draw a square by moving and turning four times. The code must use 'repeat 4' with move and turn blocks inside to create a closed square shape.

**Why This Is Gateway:**
The repeat block is fundamental to all programming. Understanding repetition unlocks loops, patterns, and efficiency. This is one of the most important skills in all of coding.

**Starter Code:**
- Cat sprite on stage
- Pen extension enabled
- Hint: A square has 4 equal sides and 4 right angles (90 degrees)

**Step-by-Step Instructions:**
1. When green flag clicked
2. Add "pen down" (so we can see the path)
3. Add "repeat 4" block (from Control category - orange)
4. **Inside the repeat**, add:
   - Move 100 steps
   - Turn right 90 degrees
5. Click the flag and watch the square form!

**Success Criteria (Auto-Grade):**
- ✅ Uses "repeat 4" block
- ✅ Move block is inside repeat
- ✅ Turn block is inside repeat
- ✅ Cat returns close to starting position
- ✅ Path forms a square shape

**Common Errors & Hints:**
- **Not a square:** "Check your turn amount - 90 degrees for right angles"
- **Blocks outside repeat:** "Make sure move and turn are INSIDE the repeat block (you'll see a gap to drop them in)"
- **Too small/big:** "Change the move steps number (100 is a good size)"

**Teaching Point:**
Without repeat, you'd need to write the same code 4 times! Imagine if you wanted to make a shape with 100 sides!

**Before/After Comparison:**
```
WITHOUT REPEAT (12 blocks):        WITH REPEAT (3 blocks):
move 100 steps                     repeat 4
turn 90 degrees                      move 100 steps
move 100 steps                       turn 90 degrees
turn 90 degrees
move 100 steps
turn 90 degrees
move 100 steps
turn 90 degrees
```

**Dependencies:** T06.G3.01

**Time:** 20 minutes

---

### T07.G3.03 - Use forever for continuous actions ⭐ GATEWAY

**Learning Objective:** Use "forever" block to create continuous behavior

**Description:**
Students use a forever block to make a sprite continuously perform an action (like spinning or moving). The sprite must continue the action indefinitely until the program is stopped.

**Why This Is Gateway:**
Forever loops are the heartbeat of games and interactive programs. They enable continuous checking, animation, and game loops.

**Starter Code:**
- Cat sprite on stage at center
- Goal: Make the cat spin forever!

**Step-by-Step Instructions:**
1. When green flag clicked
2. Add "forever" block (Control category)
3. **Inside forever**, add:
   - Turn right 5 degrees
4. Click the green flag
5. Watch the cat spin continuously!
6. Click the stop button (red octagon) to stop it

**Success Criteria (Auto-Grade):**
- ✅ Uses "forever" block
- ✅ Turn block is inside forever
- ✅ Cat continues spinning until stopped
- ✅ Rotation is smooth and continuous

**Common Errors & Hints:**
- **Spins once and stops:** "Make sure turn is INSIDE the forever block"
- **Spins too fast:** "Use a smaller number like 5 degrees, or add 'wait 0.01 seconds'"
- **Can't stop it:** "Click the red stop button above the stage"

**Forever vs Repeat:**
- **Repeat 10**: Does something 10 times, then stops
- **Forever**: Does something over and over FOREVER until you stop it

**Try These:**
- Forever + move 1 step + if on edge bounce (bouncing sprite!)
- Forever + change color by 1 (rainbow effect!)

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

### T07.G3.04 - Combine repeat with motion

**Learning Objective:** Combine repeat blocks with multiple motion blocks

**Description:**
Students use a repeat block with multiple motion commands inside to create a dance pattern. The code must have at least two different motion blocks (move, turn) inside a repeat loop.

**Starter Code:**
- Cat sprite on stage at center
- Challenge: Make the cat do a cool dance!

**Step-by-Step Instructions:**
1. When green flag clicked
2. Add "repeat 4"
3. **Inside repeat**, add:
   - Move 30 steps
   - Turn 90 degrees right
   - Move -20 steps (backward!)
   - Turn 90 degrees left
4. Watch the dance!

**Success Criteria (Auto-Grade):**
- ✅ Uses repeat block
- ✅ At least 2 different motion blocks inside repeat
- ✅ Creates a visible movement pattern
- ✅ Pattern repeats correctly

**Common Errors & Hints:**
- **Looks random:** "Make sure all blocks are INSIDE the repeat"
- **Too simple:** "Try adding more moves - forward, backward, turns!"
- **Gets stuck off-screen:** "Use smaller move numbers or add turns to keep cat on stage"

**Creative Challenge:**
Can you make the cat:
- Dance in a star shape?
- Zig-zag across the stage?
- Do a spinning jump?

**Dependencies:** T07.G3.02

**Time:** 20 minutes

---

## T08: Conditionals (4 skills)

### T08.G3.01 - Use if-then to check conditions ⭐ GATEWAY

**Learning Objective:** Use "if-then" block to make decisions

**Description:**
Students use an if-then block to check if a sprite is touching the edge and perform an action only when true. The code must use an if-then block with a sensing condition that executes code only when the condition is met.

**Why This Is Gateway:**
Conditionals (if-then) are how computers make decisions. This is one of the most fundamental concepts in ALL programming. 183+ skills depend on this.

**Starter Code:**
- Cat sprite on stage
- Pre-built code: when green flag clicked → forever → move 5 steps
- Student adds: if-then inside the forever

**Step-by-Step Instructions:**
1. Your code already has: forever → move 5 steps
2. **Inside the forever**, AFTER move 5 steps, add:
3. "If-then" block (Control category)
4. In the hexagon (the condition), add: "touching edge?"
5. Inside the "then" part, add: "play sound meow"
6. Test: Cat meows only when it hits the edge!

**Success Criteria (Auto-Grade):**
- ✅ Uses "if-then" block
- ✅ Uses "touching edge?" condition
- ✅ Sound plays only when touching edge
- ✅ Sound does NOT play when not touching edge
- ✅ If-then is inside forever loop

**Common Errors & Hints:**
- **Sound plays all the time:** "Make sure the sound block is INSIDE the if-then, not just after it"
- **Never plays sound:** "Is the if-then inside the forever loop? The cat needs to keep checking"
- **Wrong condition:** "Use 'touching edge?' from the Sensing category (light blue)"

**How If-Then Works:**
```
IF (condition is true) THEN
  do this action
ELSE
  skip it and keep going
```

**Real-World Example:**
- IF (it's raining) THEN (bring umbrella)
- IF (sprite touching edge) THEN (play sound)

**Dependencies:** T06.G3.01, T07.G3.03

**Time:** 20 minutes

---

### T08.G3.02 - Use if-then-else for two paths

**Learning Objective:** Use "if-then-else" for two different outcomes

**Description:**
Students use an if-then-else block to make a sprite say different messages based on a condition. The code must have different actions in both the 'then' and 'else' branches that execute based on the condition.

**Starter Code:**
- Cat sprite on stage
- Code: when green flag clicked → forever → move 5 steps
- Student adds: if-then-else

**Step-by-Step Instructions:**
1. After move 5 steps, add "if-then-else" (NOT just if-then!)
2. Condition: "touching edge?"
3. In the "then" section: say "Edge!" for 1 second
4. In the "else" section: say "Safe!" for 1 second
5. Watch the messages change as cat moves!

**Success Criteria (Auto-Grade):**
- ✅ Uses "if-then-else" block
- ✅ Different actions in "then" and "else"
- ✅ Shows "Edge!" when touching edge
- ✅ Shows "Safe!" when NOT touching edge
- ✅ Both messages appear at appropriate times

**Common Errors & Hints:**
- **Only one message:** "Make sure you're using if-then-ELSE, not just if-then"
- **Wrong messages:** "Put the edge message in 'then', the safe message in 'else'"
- **Messages overlap:** "Use 'say for 1 second' not just 'say'"

**If-Then vs If-Then-Else:**
- **If-Then**: Does something IF true, otherwise does nothing
- **If-Then-Else**: Does one thing IF true, does DIFFERENT thing if false

**Extension:**
Try checking if the cat is touching a different sprite, and say different things for "touching" vs "not touching"!

**Dependencies:** T08.G3.01

**Time:** 20 minutes

---

### T08.G3.03 - Use comparison operators (>, <, =)

**Learning Objective:** Use comparison operators (greater than, less than, equals) in if-then blocks

**Description:**
Students use comparison operators (greater than, less than, equals) in an if-then block to compare sprite properties like size or position. The code must use at least one comparison operator to make a decision.

**Starter Code:**
- Cat sprite at size 50
- Code: when green flag clicked → forever → change size by 5

**Step-by-Step Instructions:**
1. After change size by 5, add "if-then"
2. In the condition, add ">" (greater than) operator
3. Put "size" reporter on left side of >
4. Put number 100 on right side of >
5. Inside then: say "Big!" for 1 second
6. Test: Message appears when size goes over 100!

**Success Criteria (Auto-Grade):**
- ✅ Uses "if-then" with comparison operator
- ✅ Uses > or < or = operator
- ✅ Compares sprite property to a number
- ✅ Action only happens when condition is true

**Common Errors & Hints:**
- **Backwards comparison:** "size > 100 means 'size is greater than 100'"
- **Can't find operators:** "Look in Operators category (green blocks)"
- **Always true/false:** "Check your number - 100 is a good threshold for size"

**Comparison Operators:**
- **>** greater than (5 > 3 is TRUE)
- **<** less than (3 < 5 is TRUE)
- **=** equals (5 = 5 is TRUE)

**Try These:**
- If x position > 100 then say "Far right!"
- If y position < -50 then say "Down low!"
- If size = 100 then say "Perfect size!"

**Dependencies:** T08.G3.01

**Time:** 20 minutes

---

### T08.G3.04 - Detect when sprites touch

**Learning Objective:** Use "if touching sprite" to detect collisions

**Description:**
Students use the 'touching sprite' sensing block in an if-then to detect when two sprites collide. The code must respond differently when sprites are touching versus not touching.

**Starter Code:**
- Cat sprite (player controlled)
- Ball sprite (moving automatically)
- Cat code: when green flag clicked → forever → go to mouse-pointer

**Step-by-Step Instructions:**
1. In cat's forever loop (after go to mouse), add "if-then"
2. Condition: "touching [Ball]?"
3. Inside then: say "Got you!" for 1 second
4. Make ball move around stage (repeat → move + turn + if on edge bounce)
5. Try to make cat touch ball!

**Success Criteria (Auto-Grade):**
- ✅ Uses "if touching sprite" block
- ✅ Correctly detects collision with specific sprite
- ✅ Action happens only when touching
- ✅ No action when not touching
- ✅ Works reliably

**Common Errors & Hints:**
- **Always says "Got you":** "The if-then must be checking 'touching [Ball]?' not 'touching edge'"
- **Never says it:** "Make sure cat and ball can actually touch - are they both moving?"
- **Wrong sprite:** "Make sure you select the right sprite name from the dropdown"

**Real-World Use:**
This is how games detect:
- Catching coins
- Hitting enemies
- Picking up power-ups
- Touching the goal

**Dependencies:** T08.G3.01

**Time:** 20 minutes

---

## T10: Operators (5 skills)

### T10.G3.01 - Use addition and subtraction in code

**Learning Objective:** Use + and - operators in motion blocks

**Description:**
Students use addition and subtraction operators in code to calculate movement distances or other values. The code must use both + and - operators to perform calculations that affect sprite behavior.

**Starter Code:**
- Cat sprite on stage

**Step-by-Step Instructions:**
1. When green flag clicked
2. Move **(10 + 5)** steps ← Use + operator!
3. Wait 1 second
4. Move **(20 - 5)** steps ← Use - operator!
5. See how math changes the movement!

**Success Criteria (Auto-Grade):**
- ✅ Uses + operator in code
- ✅ Uses - operator in code
- ✅ Math is inside another block (like move)
- ✅ Calculations work correctly (10+5=15, 20-5=15)

**Common Errors & Hints:**
- **No operators visible:** "You need to put the green operator blocks INSIDE the move block"
- **Doesn't calculate:** "Make sure you're using + and - from Operators (green), not just typing"

**Why Use Math in Code?**
Instead of typing 15, you can write 10+5. This is useful when:
- Calculations change based on variables
- You want to show your thinking
- Math makes the code clearer

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

### T10.G3.02 - Use multiplication and division

**Learning Objective:** Use * and / operators for calculations

**Description:**
Students use multiplication and division operators to calculate values in their code. The code must use the * or / operator to perform calculations.

**Starter Code:**
- Cat sprite on stage at y=0

**Step-by-Step Instructions:**
1. When space key pressed
2. Change y by **(10 * 5)** ← Multiply!
3. Wait 0.3 seconds
4. Change y by **(-50 / 1)** ← Divide!
5. Test the super jump!

**Success Criteria (Auto-Grade):**
- ✅ Uses * (multiply) operator
- ✅ Uses / (divide) operator
- ✅ Calculations affect sprite behavior
- ✅ Math works correctly (10*5=50, -50/1=-50)

**Common Errors & Hints:**
- **Can't find operators:** "* is multiply, / is divide - both in Operators (green)"
- **Jump doesn't work:** "First change should be positive (up), second negative (down)"

**Math Operators:**
- **+** add (5 + 3 = 8)
- **-** subtract (5 - 3 = 2)
- ***** multiply (5 * 3 = 15)
- **/** divide (15 / 3 = 5)

**Dependencies:** T10.G3.01

**Time:** 15 minutes

---

### T10.G3.03 - Use random numbers for variety

**Learning Objective:** Use "pick random" to generate random numbers

**Description:**
Students use the 'pick random' block to generate random numbers that make their program unpredictable. The code must use random numbers in a way that creates different outcomes each time the program runs.

**Starter Code:**
- Cat sprite on stage

**Step-by-Step Instructions:**
1. When green flag clicked
2. Repeat 5 times:
3. Move **(pick random 10 to 50)** steps
4. Wait 0.5 seconds
5. Watch different distances each time!

**Success Criteria (Auto-Grade):**
- ✅ Uses "pick random" block
- ✅ Random values used in motion or other blocks
- ✅ Behavior varies each time program runs
- ✅ Random range makes sense (10 to 50, not 1 to 1000)

**Common Errors & Hints:**
- **Same every time:** "Make sure you're using 'pick random' from Operators (green), not just a number"
- **Too random:** "Choose a good range - 10 to 50 gives variety without being crazy"
- **Can't see difference:** "Run the program multiple times to see different results"

**Random is Everywhere:**
- Dice rolling (1 to 6)
- Where enemies appear
- What color something changes to
- Surprise elements in games

**Try These Random Ideas:**
- pick random 1 to 360 → point in direction (random spin!)
- pick random -200 to 200 → go to x: (random position!)
- pick random 50 to 150 → set size (random size!)

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

### T10.G3.04 - Compare numbers (greater, less, equal)

**Learning Objective:** Use comparison operators to compare two numbers or values

**Description:**
Students use comparison operators to compare two numbers or values. The code must use >, <, or = to make comparisons that affect program behavior.

**Starter Code:**
- Cat sprite
- Variable "score" created and set to 0

**Step-by-Step Instructions:**
1. When green flag clicked
2. Set score to (pick random 1 to 100)
3. If **(score > 50)** then
4. Say "High score!" for 2 seconds
5. Run multiple times to see different results!

**Success Criteria (Auto-Grade):**
- ✅ Uses comparison operator (>, <, or =)
- ✅ Compares two values
- ✅ Comparison affects what code does
- ✅ Logic is correct (message appears when it should)

**Common Errors & Hints:**
- **Backwards:** "score > 50 means 'score is greater than 50'"
- **Always true/never true:** "Test with different values to check your comparison"

**Comparisons in Real Life:**
- If score > 100 → You win!
- If lives < 1 → Game over!
- If size = 100 → Perfect!

**Dependencies:** T08.G3.03

**Time:** 15 minutes

---

### T10.G3.05 - Join text together

**Learning Objective:** Use the join operator to combine text strings

**Description:**
Students use the join operator to combine text strings together. The code must use the join block to create a message from multiple text pieces.

**Starter Code:**
- Cat sprite
- Variable "name" created

**Step-by-Step Instructions:**
1. When green flag clicked
2. Set name to "Scratchy"
3. Say **(join "Hello " name)** for 2 seconds
4. See the message "Hello Scratchy"!
5. Try changing the name!

**Success Criteria (Auto-Grade):**
- ✅ Uses "join" block
- ✅ Combines at least 2 text pieces
- ✅ Creates readable message
- ✅ Uses variable or multiple text strings

**Common Errors & Hints:**
- **Smashed together:** "Add a space in your text like 'Hello ' (with space after)"
- **Can't find join:** "It's in Operators (green) - looks like two puzzle pieces"
- **Not working:** "Make sure you put the join block INSIDE the say block"

**Join is Powerful:**
```
join "I am " → "10" → " years old"
= "I am 10 years old"

join "Score: " → score variable
= "Score: 42"
```

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

## T05: Motion Basics (2 skills)

### T05.G3.01 - Move sprites with move and turn blocks

**Learning Objective:** Use "move steps" and "turn degrees" blocks

**Description:**
Students use the move steps and turn degrees blocks to control sprite motion. The sprite must move forward and rotate using these basic motion commands.

**Success Criteria:**
- ✅ Uses "move steps" block
- ✅ Uses "turn degrees" block
- ✅ Sprite moves forward
- ✅ Sprite rotates correctly

**Time:** 15 minutes

---

### T05.G3.02 - Make sprites point in directions

**Learning Objective:** Use "point in direction" block

**Description:**
Students use the 'point in direction' block to make sprites face specific directions (0=right, 90=up, 180=left, -90=down). The sprite must face the correct direction when the code runs.

**Key Directions:**
- 0° = right
- 90° = up
- 180° = left
- -90° = down

**Success Criteria:**
- ✅ Uses "point in direction" block
- ✅ Sprite faces correct direction
- ✅ Understands direction numbers

**Time:** 15 minutes

---

## Week 1 Summary

**Total Skills Completed:** 20
**Gateway Skills Mastered:** 5 (T06.G3.01, T07.G3.01, T07.G3.02, T07.G3.03, T08.G3.01)
**Essential Blocks Learned:**
- Events: when flag clicked, when sprite clicked, when key pressed
- Loops: wait, repeat, forever
- Conditionals: if-then, if-then-else
- Operators: +, -, *, /, pick random, comparison, join
- Motion: move, turn, point in direction

**Students Can Now:**
- Start programs with events
- Create timed sequences
- Make patterns with repeat loops
- Make programs run continuously
- Make decisions with if-then
- Use math in their code
- Control sprite movement

**Ready for Week 2:** Motion Advanced, Looks, Sensing
