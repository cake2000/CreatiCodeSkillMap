# Grade 3 Foundational Block Skills - Week 2: Visual & Interactive

**Week Focus:** Motion Advanced, Looks, Sensing
**Total Skills:** 13
**Estimated Time:** 4-6 hours of instruction

---

## T05: Motion Advanced (5 skills)

### T05.G3.03 - Glide smoothly to a position

**Learning Objective:** Use "glide to" block for smooth motion

**Description:**
Students use the glide block to make a sprite move smoothly from one position to another over time. The sprite must glide (not jump instantly) to the target position.

**Why Glide Matters:**
Glide creates smooth, professional-looking animations. Without it, sprites just teleport! This is essential for polished projects.

**Starter Code:**
- Cat sprite at x=-200, y=0 (left side of stage)

**Step-by-Step Instructions:**
1. When green flag clicked
2. Glide 2 seconds to x:200 y:0
3. Wait 1 second
4. Glide 2 seconds to x:-200 y:0
5. Watch the smooth back-and-forth motion!

**Success Criteria (Auto-Grade):**
- ✅ Uses "glide to" block (not "go to")
- ✅ Sprite moves smoothly (visible motion, not instant)
- ✅ Takes specified amount of time (2 seconds)
- ✅ Reaches target position accurately

**Common Errors & Hints:**
- **Instant movement:** "Make sure you're using GLIDE (which takes time) not GO TO (which is instant)"
- **Wrong block:** "Glide is in Motion (blue blocks) - it has a clock icon"
- **Too fast/slow:** "The first number in glide is the time in seconds"

**Glide vs Go To:**
- **Go To:** Instant teleport (good for resetting)
- **Glide:** Smooth movement over time (good for animations)

**Extension Activity:**
Make the cat glide to 5 different positions to create a tour of the stage!

**Dependencies:** T05.G3.01

**Time:** 15 minutes

---

### T05.G3.04 - Go to specific positions

**Learning Objective:** Use "go to x:y" to position sprites at coordinates

**Description:**
Students use the 'go to x:y' block to position sprites at specific coordinates on the stage. The sprite must move to the exact x and y coordinates specified in the block.

**Understanding the Stage:**
```
        y: 180 (top)
            |
x: -240 ---0--- x: 240
(left)      |      (right)
        y: -180 (bottom)
```

**Starter Code:**
- Cat sprite at center (0, 0)
- Corner markers visible to help students see coordinates

**Step-by-Step Instructions:**
1. When green flag clicked
2. Go to x:0 y:0 (center - starting position)
3. Wait 1 second
4. Go to x:200 y:150 (top right corner)
5. Say "Top right!" for 1 second
6. Wait 1 second
7. Go to x:-200 y:-150 (bottom left corner)
8. Say "Bottom left!" for 1 second
9. Wait 1 second
10. Go to x:0 y:0 (back to center)

**Success Criteria (Auto-Grade):**
- ✅ Uses "go to x:y" block
- ✅ Sprite moves to exact coordinates
- ✅ Visits multiple positions correctly
- ✅ Understands coordinate system

**Common Errors & Hints:**
- **Not at exact spot:** "Check your x and y numbers - they need to match exactly"
- **Confused about negative:** "Negative x is LEFT, negative y is DOWN"
- **Off stage:** "Stay within x: -240 to 240, y: -180 to 180"

**Memory Trick:**
- **X-axis:** "X is cross - LEFT and RIGHT"
- **Y-axis:** "Y is up - UP and DOWN"

**Coordinate Examples:**
- (0, 0) = Center
- (240, 180) = Top-right corner
- (-240, -180) = Bottom-left corner
- (0, 180) = Top center
- (240, 0) = Right center

**Dependencies:** T05.G3.01

**Time:** 15 minutes

---

### T05.G3.05 - Change x and y coordinates

**Learning Objective:** Use "change x by" and "change y by" for relative movement

**Description:**
Students use 'change x by' and 'change y by' blocks to move sprites horizontally and vertically. The code must use both blocks to move a sprite in a specific pattern demonstrating understanding of coordinate system.

**Change vs Go To:**
- **Go to x:100** → Jump to exactly x=100
- **Change x by 100** → Move 100 from wherever you are now

**Starter Code:**
- Cat sprite at center (0, 0)
- Goal: Make a square path using change x and change y

**Step-by-Step Instructions:**
1. When green flag clicked
2. Change x by 100 (move right)
3. Wait 0.5 seconds
4. Change y by 100 (move up)
5. Wait 0.5 seconds
6. Change x by -100 (move left)
7. Wait 0.5 seconds
8. Change y by -100 (move down)
9. Watch the square path!

**Success Criteria (Auto-Grade):**
- ✅ Uses "change x by" for horizontal movement
- ✅ Uses "change y by" for vertical movement
- ✅ Sprite moves in correct directions
- ✅ Returns close to starting position
- ✅ Creates clear path pattern

**Common Errors & Hints:**
- **Wrong direction:** "Positive x = right, negative x = left. Positive y = up, negative y = down"
- **Using go to instead:** "Use CHANGE (relative movement) not GO TO (absolute position)"
- **Not a square:** "Make sure your positive and negative numbers match (like +100 and -100)"

**Change X by:**
- Positive number → moves RIGHT
- Negative number → moves LEFT
- Amount is how far to move

**Change Y by:**
- Positive number → moves UP
- Negative number → moves DOWN
- Amount is how far to move

**Pattern Challenge:**
Can you use change x and change y to make:
- A plus sign (+)?
- A zig-zag pattern?
- The letter "Z"?

**Dependencies:** T05.G3.04

**Time:** 20 minutes

---

### T05.G3.06 - Bounce at the edge of screen

**Learning Objective:** Use "if on edge, bounce" block

**Description:**
Students use the 'if on edge, bounce' block to make a sprite change direction when it hits the edge of the stage. The sprite must bounce off edges and stay within the stage boundaries.

**Why Bouncing Matters:**
This is how balls bounce, characters stay on screen, and games feel natural. Without this, sprites disappear off-screen!

**Starter Code:**
- Cat sprite at center, pointing right (direction = 0)

**Step-by-Step Instructions:**
1. When green flag clicked
2. Point in direction 0 (face right)
3. Forever:
   - Move 5 steps
   - If on edge, bounce
4. Watch the cat bounce back and forth!
5. To stop: Click the red stop button

**Success Criteria (Auto-Grade):**
- ✅ Uses "if on edge, bounce" block
- ✅ Sprite changes direction when hitting edge
- ✅ Sprite stays on screen (doesn't disappear)
- ✅ Bouncing happens smoothly
- ✅ Works with forever loop

**Common Errors & Hints:**
- **Disappears off edge:** "Did you put 'if on edge, bounce' INSIDE the forever loop?"
- **Doesn't bounce:** "Make sure move and bounce are both inside forever"
- **Upside down:** "Click the 'i' on sprite, set rotation style to 'left-right' not 'all around'"

**Rotation Styles:**
- **All around:** Sprite rotates fully (can be upside down)
- **Left-right:** Sprite only flips horizontally
- **Don't rotate:** Sprite never rotates

**How Bouncing Works:**
```
Moving right (0°) + hits right edge = now moving left (180°)
Moving left (180°) + hits left edge = now moving right (0°)
```

**Try These Variations:**
- Change move speed (move 10 steps = faster bounce)
- Add "change color by 5" for rainbow bouncing
- Use "pick random 3 to 8" for variable speed

**Dependencies:** T05.G3.01, T07.G3.03

**Time:** 20 minutes

---

### T05.G3.07 - Point towards another sprite

**Learning Objective:** Use "point towards" block

**Description:**
Students use the 'point towards' block to make one sprite always face another sprite or the mouse pointer. The sprite must rotate to point toward the target.

**Real-World Uses:**
- Enemies chasing the player
- Turrets aiming at targets
- Characters looking at each other
- Arrows pointing to goals

**Starter Code:**
- Cat sprite (stays at center)
- Ball sprite (player can drag around)

**Step-by-Step Instructions:**
1. For Cat sprite:
2. When green flag clicked
3. Forever:
   - Point towards [Ball]
   - (Cat now always faces the ball!)
4. Drag the ball around the stage
5. Watch cat rotate to follow it!

**Success Criteria (Auto-Grade):**
- ✅ Uses "point towards" block
- ✅ Sprite rotates to face target
- ✅ Updates continuously (in forever loop)
- ✅ Points accurately at target

**Common Errors & Hints:**
- **Doesn't follow:** "Make sure 'point towards' is inside a forever loop to keep updating"
- **Wrong target:** "Select the right sprite name from the dropdown menu"
- **Jerky movement:** "This is normal - it updates each frame"

**Point Towards Options:**
- **Mouse-pointer:** Follows your cursor
- **Another sprite:** Follows that sprite
- **Random position:** (use variables for x,y)

**Extension - Make it Chase:**
```
Forever:
  Point towards Ball
  Move 2 steps        ← Add this to make cat chase ball!
  If on edge, bounce
```

**Creative Challenge:**
Make a "two sprite dance" where:
- Cat points towards Ball
- Ball points towards Cat
- Both move slowly
- They spiral around each other!

**Dependencies:** T05.G3.02

**Time:** 20 minutes

---

## T11: Looks (6 skills)

### T11.G3.01 - Show and hide sprites

**Learning Objective:** Use "show" and "hide" blocks

**Description:**
Students use the show and hide blocks to make sprites appear and disappear. The sprite must become invisible when hide is used and visible when show is used.

**Why Show/Hide is Important:**
- Make things disappear when collected
- Create surprise appearances
- Build games with invisible enemies
- Control what's visible on screen

**Starter Code:**
- Cat sprite (visible on stage)

**Step-by-Step Instructions:**
1. When green flag clicked
2. Wait 1 second
3. Hide (cat disappears!)
4. Wait 2 seconds
5. Show (cat reappears!)
6. Say "Boo!" for 1 second

**Success Criteria (Auto-Grade):**
- ✅ Uses "hide" block
- ✅ Uses "show" block
- ✅ Sprite becomes invisible when hidden
- ✅ Sprite becomes visible when shown
- ✅ Timing is correct

**Common Errors & Hints:**
- **Still visible:** "Make sure you're clicking the green flag to run the code"
- **Can't see it come back:** "Did you add 'show' after the wait?"
- **Stuck invisible:** "Always start with 'show' when green flag clicked to reset"

**Best Practice - Always Reset:**
```
When green flag clicked
  Show           ← Always start visible
  Go to x:0 y:0  ← Reset position
  Set size to 100 ← Reset size
  ... then your code ...
```

**Creative Uses:**
- Hide sprite when "caught" in tag game
- Show power-up after timer
- Blinking effect (hide, wait 0.1, show, wait 0.1, repeat)
- Invisible maze (show walls briefly then hide)

**Try This Pattern:**
```
Repeat 10:
  Hide
  Wait 0.2 seconds
  Show
  Wait 0.2 seconds
= Blinking sprite!
```

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

### T11.G3.02 - Make sprites say and think

**Learning Objective:** Use "say" and "think" blocks

**Description:**
Students use the say and think blocks to display text in speech bubbles and thought bubbles. The sprite must display messages using both types of bubbles.

**Say vs Think:**
- **Say:** Speech bubble (white, rounded, spoken words)
- **Think:** Thought bubble (white, with small circles, inner thoughts)

**Starter Code:**
- Cat sprite on stage

**Step-by-Step Instructions:**
1. When green flag clicked
2. Say "Hello! I'm a cat!" for 2 seconds
3. Wait 0.5 seconds
4. Think "I wonder what's for lunch..." for 2 seconds
5. Wait 0.5 seconds
6. Say "Thanks for coding with me!" for 2 seconds

**Success Criteria (Auto-Grade):**
- ✅ Uses "say for ___ seconds" block
- ✅ Uses "think for ___ seconds" block
- ✅ Speech bubble appears with say
- ✅ Thought bubble appears with think
- ✅ Messages display for correct duration

**Common Errors & Hints:**
- **Bubbles overlap:** "Use 'say for seconds' not just 'say' - the timed version waits before continuing"
- **Can't see difference:** "Look closely - speech is rounder, thoughts have little circles"
- **Too fast:** "Use at least 2 seconds so people can read the message"

**Say For vs Say:**
- **Say for 2 seconds:** Shows message, waits 2 seconds, then continues code
- **Say "hello":** Shows message forever (until something else replaces it)

**Good Message Timing:**
- Short message (1-3 words): 1 second
- Normal message (4-8 words): 2 seconds
- Long message (9+ words): 3-4 seconds

**Storytelling with Say/Think:**
```
Say "It's a beautiful day!" for 2 secs
Think "But I'm feeling sleepy..." for 2 secs
Say "I know! I'll take a nap!" for 2 secs
Hide (cat goes to sleep)
```

**Extension - Interactive Dialog:**
```
Say "What's your name?" for 2 secs
Set [name] to (ask "Your name?" and wait)
Say (join "Nice to meet you, " name) for 2 secs
```

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

### T11.G3.03 - Switch costumes for animation

**Learning Objective:** Use "switch costume" and "next costume" blocks

**Description:**
Students use the 'switch costume' or 'next costume' blocks to animate a sprite by changing its appearance. The sprite must cycle through at least 2 different costumes to create animation.

**What Are Costumes?**
Costumes are different pictures/poses for the same sprite. By switching between them quickly, you create animation!

**Starter Code:**
- Cat sprite (has two costumes: cat-a and cat-b)
- Both costumes show cat in different walking positions

**Step-by-Step Instructions:**
1. When green flag clicked
2. Repeat 10 times:
   - Next costume (switches to next costume in list)
   - Wait 0.3 seconds
3. Watch the walking animation!

**Success Criteria (Auto-Grade):**
- ✅ Uses "switch costume" or "next costume" block
- ✅ Switches between at least 2 costumes
- ✅ Creates visible animation effect
- ✅ Timing creates smooth motion

**Common Errors & Hints:**
- **Too fast to see:** "Make wait time longer like 0.3 or 0.5 seconds"
- **Only shows one:** "Make sure you're using 'next costume' not 'switch costume to cat-a' (which stays on one)"
- **Doesn't loop:** "Next costume automatically goes back to first costume after last one"

**Switch Costume vs Next Costume:**
- **Switch costume to [cat-a]:** Always goes to that specific costume
- **Next costume:** Goes to next costume in list (and loops back to first)

**Animation = Quick Costume Changes:**
```
Next costume
Wait 0.1 seconds   ← Fast = smooth animation
Next costume
Wait 0.1 seconds
= Walking, flying, swimming, etc.
```

**Try This Walking Animation:**
```
When green flag clicked
Forever:
  Next costume
  Move 2 steps     ← Combines animation with movement!
  Wait 0.1 seconds
```

**Finding Sprites with Good Costumes:**
- Ballerina (4 dancing poses)
- Butterfly (2 flapping wings)
- Cat (2 walking poses)
- All sprites with "costume1" and "costume2"

**Dependencies:** T06.G3.01, T07.G3.02

**Time:** 20 minutes

---

### T11.G3.04 - Change sprite size

**Learning Objective:** Use "set size" and "change size by" blocks

**Description:**
Students use the 'set size to' and 'change size by' blocks to make sprites grow or shrink. The sprite must visibly change size when the blocks are used.

**Understanding Size:**
- 100% = Normal size (default)
- 200% = Double size (twice as big)
- 50% = Half size
- Can go up to 1000%+ (very big!)
- Can't go below 0% (invisible at 0%)

**Starter Code:**
- Cat sprite at size 100%

**Step-by-Step Instructions:**
1. When green flag clicked
2. Set size to 100% (start at normal)
3. Repeat 10 times:
   - Change size by 10
   - Wait 0.2 seconds
4. Wait 1 second
5. Set size to 100% (back to normal)

**Success Criteria (Auto-Grade):**
- ✅ Uses "change size by" block
- ✅ Uses "set size to" block
- ✅ Size changes are visible
- ✅ Grows then resets to normal

**Common Errors & Hints:**
- **Doesn't change:** "Make sure the blocks are in the right order and connected"
- **Too big/small:** "Stay between 50% and 200% for readable sizes"
- **Can't reset:** "Use 'set size to 100%' to return to normal"

**Change Size vs Set Size:**
- **Change size by 10:** Add 10 to current size (100 → 110 → 120 → ...)
- **Set size to 100:** Jump to exactly 100% (no matter what it was before)

**Size Effects:**
```
Growing:                    Shrinking:
Repeat 20                   Repeat 20
  Change size by 5            Change size by -5
  Wait 0.1 secs               Wait 0.1 secs
= Gets bigger!              = Gets smaller!
```

**Creative Uses:**
- Power-up makes character bigger
- Collecting coins makes you grow
- Losing life makes you shrink
- Pulsing heartbeat effect
- Zoom in/out on important items

**Advanced - Pulsing Animation:**
```
Forever:
  Repeat 10: change size by 5, wait 0.05 secs
  Repeat 10: change size by -5, wait 0.05 secs
= Continuous pulse!
```

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

### T11.G3.05 - Change color effects

**Learning Objective:** Use "change color effect" and "set color effect" blocks

**Description:**
Students use the 'change color effect' or 'set color effect' blocks to alter sprite appearance. The sprite must change color or visual effect in a visible way.

**Graphic Effects Available:**
- **Color:** Changes hue (red → orange → yellow → green → blue → purple → red)
- **Fisheye:** Bulges the sprite
- **Whirl:** Swirls the sprite
- **Pixelate:** Makes it blocky
- **Mosaic:** Duplicates it
- **Brightness:** Lighter/darker
- **Ghost:** Transparency (100 = invisible)

**Starter Code:**
- Cat sprite (normal appearance)

**Step-by-Step Instructions:**
1. When green flag clicked
2. Clear graphic effects (start fresh)
3. Repeat 36 times:
   - Change color effect by 10
   - Wait 0.1 seconds
4. Watch the rainbow!

**Success Criteria (Auto-Grade):**
- ✅ Uses "change ___ effect by" or "set ___ effect to"
- ✅ Sprite appearance changes visibly
- ✅ Creates smooth effect transition
- ✅ Uses appropriate effect values

**Common Errors & Hints:**
- **No change:** "Make sure you're changing by a big enough number (like 10 or 25)"
- **Stuck on effect:** "Use 'clear graphic effects' at the start to reset"
- **Too extreme:** "For color, change by 10-25. For ghost, stay under 50 (or it's invisible!)"

**Change Effect vs Set Effect:**
- **Change color by 10:** Add 10 to current value (keeps changing)
- **Set color to 100:** Jump to exactly 100 (fixed value)

**Color Effect Rainbow:**
```
0 = Original color
50 = Different hue
100 = More different
150 = Even more
200 = Back to original (it loops!)
```

**Effect Experiments:**
```
Forever:
  Change fisheye by 10      = Growing bulge
  Change whirl by 5         = Spinning distortion
  Change brightness by -1   = Fading to dark
  Change ghost by 1         = Slowly disappearing
```

**Creative Combinations:**
```
When sprite clicked
  Set ghost to 50          = Half transparent
  Set color to 100         = Different color
  Set size to 150          = Bigger
= Magical transformation!
```

**Pro Tip - Always Reset:**
```
When green flag clicked
  Clear graphic effects    ← Always start fresh!
  Set size to 100
  Show
```

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

### T11.G3.06 - Move sprites to front or back

**Learning Objective:** Use layer blocks to control sprite stacking

**Description:**
Students use 'go to front layer' and 'go to back layer' blocks to control which sprite appears on top. The sprite layering must change when these blocks are used.

**What Are Layers?**
Sprites stack like pieces of paper. Front layer = on top (visible), back layer = on bottom (can be hidden behind others).

**Starter Code:**
- Two sprites: Cat and Ball
- Both overlapping at center

**Step-by-Step Instructions:**
1. For Cat:
   - When green flag clicked
   - Go to front layer
2. For Ball:
   - When this sprite clicked
   - Go to front layer
3. Try clicking each sprite to bring it to front!

**Success Criteria (Auto-Grade):**
- ✅ Uses layer control blocks
- ✅ Sprite moves to front when specified
- ✅ Sprite moves to back when specified
- ✅ Layering changes are visible

**Common Errors & Hints:**
- **Can't see change:** "Make sure sprites are overlapping so you can see which is on top"
- **Wrong layer:** "Front layer = on top, back layer = on bottom"

**Layer Commands:**
- **Go to front layer:** Puts sprite on top of all others
- **Go to back layer:** Puts sprite behind all others
- **Go forward 1 layer:** Move up one level
- **Go backward 1 layer:** Move down one level

**Real-World Uses:**
- Character walks in front of trees
- UI elements always on top
- Background stays in back
- Click to bring to front

**Extension - Interactive Stacking:**
```
When this sprite clicked
  Go to front layer
  Say "I'm on top!" for 1 second
```

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

## T12: Sensing (2 skills)

### T12.G3.01 - Detect when touching a sprite

**Learning Objective:** Use "touching sprite?" sensing block

**Description:**
Students use the 'touching [sprite]?' sensing block to detect when sprites collide. The code must respond differently when the sprites are touching versus not touching.

**Why Collision Detection Matters:**
This is THE most important skill for games:
- Catching coins
- Hitting enemies
- Picking up items
- Reaching the goal
- Dodging obstacles

**Starter Code:**
- Cat sprite (controlled by player)
- Ball sprite (moving around)
- Pre-built Ball code: forever → move + turn + bounce

**Step-by-Step Instructions:**
1. For Cat sprite:
2. When green flag clicked
3. Forever:
   - Go to mouse-pointer
   - If **touching Ball?** then:
     - Say "Caught it!" for 0.5 seconds
4. Try to touch the ball with the cat!

**Success Criteria (Auto-Grade):**
- ✅ Uses "touching [sprite]?" block
- ✅ Correctly detects collision
- ✅ Action happens only when touching
- ✅ No action when not touching
- ✅ Works reliably and consistently

**Common Errors & Hints:**
- **Always detecting:** "Make sure you're checking INSIDE a forever loop with if-then"
- **Never detects:** "Are the sprites actually touching? They need to overlap!"
- **Wrong sprite:** "Select the correct sprite name from the dropdown"

**Touching Options:**
- **Touching [sprite name]?** → Specific sprite
- **Touching mouse-pointer?** → Mouse cursor
- **Touching edge?** → Stage edge
- **Touching color?** → Specific color

**Game Example - Coin Collector:**
```
For Coin sprite:
When green flag clicked
Forever:
  If touching Player? then
    Hide                    ← Coin disappears
    Change [score] by 1     ← Score increases
    Play sound "collect"    ← Audio feedback
```

**Debugging Collision:**
If collision isn't working:
1. Make sprites bigger (easier to touch)
2. Add "say touching Ball?" to see true/false
3. Make ball move slower
4. Check sprite names match exactly

**Dependencies:** T08.G3.04

**Time:** 20 minutes

---

### T12.G3.02 - Detect when touching the edge

**Learning Objective:** Use "touching edge?" sensing block

**Description:**
Students use the 'touching edge?' sensing block to detect when a sprite reaches the stage boundary. The code must react when the sprite touches the edge of the stage.

**Why Edge Detection Matters:**
- Keep characters on screen
- Trigger events at boundaries
- Create borders
- Change direction at edges

**Starter Code:**
- Cat sprite at center

**Step-by-Step Instructions:**
1. When green flag clicked
2. Forever:
   - If **NOT touching edge?** then:
     - Move 5 steps
   - Else:
     - Say "At the edge!" for 1 second
3. Watch cat stop at edge!

**Success Criteria (Auto-Grade):**
- ✅ Uses "touching edge?" block
- ✅ Uses NOT operator with touching edge
- ✅ Sprite stops or reacts at edge
- ✅ Different behavior at edge vs. not at edge

**Common Errors & Hints:**
- **Falls off edge:** "Use NOT touching edge? to move - this moves only when NOT touching"
- **Can't find NOT:** "NOT is in Operators (green) - it's a hexagon shape"
- **Never reaches edge:** "Make sure move is inside the forever loop"

**Edge Detection Patterns:**

**Pattern 1 - Stop at Edge:**
```
Forever:
  If NOT touching edge? then
    Move 5 steps
```

**Pattern 2 - Say Message at Edge:**
```
Forever:
  Move 5 steps
  If touching edge? then
    Say "Edge!" for 1 second
```

**Pattern 3 - Reverse at Edge:**
```
Forever:
  Move 5 steps
  If touching edge? then
    Point in direction (180 - direction)  ← Turn around!
```

**Combining with Bounce:**
```
Forever:
  Move 5 steps
  If on edge, bounce       ← Built-in bounce
  If touching edge? then
    Play sound "boing"     ← Sound effect
```

**NOT Operator:**
- **NOT touching edge?** → true when away from edge
- Useful for "do this while NOT at edge"

**Dependencies:** T08.G3.01

**Time:** 20 minutes

---

## Week 2 Summary

**Total Skills Completed This Week:** 13
**Cumulative Skills:** 33/41

**Motion Skills Mastered:**
- Glide for smooth animation
- Go to coordinates for precise positioning
- Change x/y for relative movement
- Bounce at edges
- Point towards targets

**Looks Skills Mastered:**
- Show and hide sprites
- Say and think bubbles
- Costume animation
- Size changes and effects
- Color and visual effects
- Layer control

**Sensing Skills Mastered:**
- Sprite collision detection
- Edge detection

**Students Can Now:**
- Create smooth animations with glide
- Position sprites anywhere using coordinates
- Make sprites bounce and stay on screen
- Point sprites at moving targets
- Show/hide sprites for effects
- Display messages with speech/thought bubbles
- Animate sprites by switching costumes
- Change size and color for effects
- Control which sprites appear on top
- Detect when sprites touch each other or edges

**Ready for Week 3:** Variables and Debugging

**Project Ideas Using Week 1+2 Skills:**
1. **Catch the Star Game** - Move sprite with keys, collect falling stars
2. **Color Change Animation** - Sprite changes colors while gliding around
3. **Follow the Leader** - One sprite points towards and follows another
4. **Bouncing Rainbow Ball** - Ball bounces and changes colors
5. **Hide and Seek** - Sprites hide and appear at random positions
