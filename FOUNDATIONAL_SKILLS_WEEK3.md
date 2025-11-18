# Grade 3 Foundational Block Skills - Week 3: Data & Polish

**Week Focus:** Variables and Debugging
**Total Skills:** 8
**Estimated Time:** 3-4 hours of instruction

---

## T09: Variables (5 skills)

### T09.G3.01 - Create and name a variable ⭐ CRITICAL GATEWAY

**Learning Objective:** Create a variable and give it a meaningful name

**Description:**
Students create a new variable and give it a meaningful name. The variable must be created through the variables palette and named appropriately for its purpose.

**Why This Is THE Most Critical Skill:**
Variables are THE gateway to advanced programming. This single skill unlocks 297 dependent skills - more than any other skill in the entire curriculum. Without variables, students cannot:
- Track scores or progress
- Store player data
- Make complex games
- Process information
- Use lists or advanced features

**What Is a Variable?**
A variable is like a labeled box that stores information. You can:
- Put a value IN the box (set variable)
- Change what's IN the box (change variable)
- Look at what's IN the box (use variable)
- Show the box on screen (show variable)

**Starter Code:**
- Cat sprite on stage
- Empty variable palette

**Step-by-Step Instructions:**
1. Click on "Variables" category (orange blocks)
2. Click "Make a Variable" button
3. Type a good name: **score** (not "var1" or "x")
4. Click OK
5. You'll see new blocks appear for your variable!
6. Check the box next to "score" to show it on stage

**Success Criteria (Auto-Grade):**
- ✅ Variable is created successfully
- ✅ Variable has a meaningful name (score, lives, level, etc.)
- ✅ Variable appears in the variables palette
- ✅ Variable is visible on stage (checkbox checked)

**Good Variable Names:**
- ✅ score (tracks points)
- ✅ lives (tracks health)
- ✅ level (tracks game level)
- ✅ speed (tracks how fast something moves)
- ✅ playerName (stores name)

**Bad Variable Names:**
- ❌ var1 (meaningless)
- ❌ x (too short, unclear)
- ❌ asdfasdf (random letters)
- ❌ thing (too vague)

**Common Errors & Hints:**
- **Can't find "Make a Variable":** "Look in the Variables category (orange) - the button is at the top"
- **Variable doesn't appear:** "After creating it, you'll see new blocks. Check the box to show it on stage"
- **Named it wrong:** "You can delete it and make a new one with a better name"

**Naming Rules:**
- Use letters and numbers (score1, player2)
- No spaces (use playerScore not "player score")
- Make it descriptive (what does it store?)
- Keep it short but clear

**What Happens When You Create a Variable:**
You get 5 new blocks:
1. **set [score] to (0)** - Put a value in the box
2. **change [score] by (1)** - Add to what's in the box
3. **show variable [score]** - Display the box on screen
4. **hide variable [score]** - Hide the box
5. **score** (reporter) - The value inside the box

**Try This After Creating:**
1. Drag the "score" reporter block (oval shape) to the stage
2. Click it a few times
3. Watch it show the current value (0 at first)

**Real-World Connection:**
Variables are everywhere:
- Game score counter
- Lives remaining
- Timer countdown
- Money in your bank account
- Temperature reading
- Speed of a car

**Dependencies:** T06.G3.01

**Time:** 15 minutes

---

### T09.G3.02 - Set a variable's value

**Learning Objective:** Use "set variable to" block to assign a value

**Description:**
Students use the 'set variable to' block to assign a value to a variable. The variable must be set to a specific value when the green flag is clicked.

**What Does "Set" Do?**
"Set" puts a new value in the variable box, replacing whatever was there before.

**Starter Code:**
- Cat sprite on stage
- Variable "score" already created

**Step-by-Step Instructions:**
1. When green flag clicked
2. Set score to **0** (start at zero)
3. Wait 1 second
4. Set score to **10** (now it's 10)
5. Wait 1 second
6. Set score to **50** (now it's 50)
7. Watch the score change on screen!

**Success Criteria (Auto-Grade):**
- ✅ Uses "set variable to" block
- ✅ Variable is set to specified value
- ✅ Value appears on stage display
- ✅ Set happens at correct time (when flag clicked)

**Common Errors & Hints:**
- **Score doesn't change:** "Make sure the variable is visible (checkbox checked)"
- **Wrong value:** "Check the number you typed in the 'set' block"
- **Doesn't reset:** "Always 'set to 0' at the start to reset the game"

**Set vs Change:**
- **Set to 10:** Makes it exactly 10 (no matter what it was before)
- **Change by 10:** Adds 10 to current value (if it was 5, now it's 15)

**Best Practice - Always Reset:**
```
When green flag clicked
  Set score to 0        ← Always start fresh!
  Set lives to 3
  Set level to 1
```

**What Can You Set?**
- Numbers: set score to 100
- Text: set name to "Player 1"
- Results of math: set score to (10 + 5)
- Random values: set score to (pick random 1 to 100)
- Other variables: set scoreBackup to score

**Common Pattern - Initialize Variables:**
```
When green flag clicked
  Set score to 0        ← Reset score
  Set lives to 3        ← Set starting lives
  Set gameOver to "no"  ← Set game state
  Show                  ← Reset sprite
  Go to x:0 y:0        ← Reset position
```

**Try These:**
1. Set score to 999 (see big number!)
2. Set score to -50 (negative numbers work!)
3. Set score to (pick random 1 to 100) (random starting score!)

**Dependencies:** T09.G3.01

**Time:** 15 minutes

---

### T09.G3.03 - Change a variable by an amount

**Learning Objective:** Use "change variable by" block to increase/decrease values

**Description:**
Students use the 'change variable by' block to increase or decrease a variable's value. The variable must increase by at least 1 when a specific event occurs (like clicking a sprite).

**What Does "Change By" Do?**
"Change by" adds to (or subtracts from) the current value.
- If score is 10 and you change by 5, score becomes 15
- If score is 10 and you change by -3, score becomes 7

**Starter Code:**
- Cat sprite on stage
- Variable "score" created and set to 0

**Step-by-Step Instructions:**
1. When green flag clicked:
   - Set score to 0
2. When this sprite clicked:
   - Change score by 1
   - Play sound "pop"
3. Click the cat many times!
4. Watch the score increase!

**Success Criteria (Auto-Grade):**
- ✅ Uses "change variable by" block
- ✅ Variable increases each time event occurs
- ✅ Change amount is appropriate (1 for counting clicks)
- ✅ Counter works reliably

**Common Errors & Hints:**
- **Score doesn't go up:** "Make sure you're using CHANGE not SET"
- **Goes up too much:** "Check the number - for counting clicks use 1"
- **Doesn't reset:** "Use 'set to 0' when green flag clicked to start fresh"

**Change By Uses:**
- **Change by 1:** Count one more (clicks, coins collected, etc.)
- **Change by 10:** Add points (scored a goal, caught item)
- **Change by -1:** Subtract one (lose a life, spend money)
- **Change by (pick random 1 to 10):** Random amount

**Change By vs Set To:**
```
Starting: score = 10

Set score to 5
Result: score = 5 (replaced old value)

Change score by 5
Result: score = 15 (added to old value)
```

**Common Game Patterns:**

**Pattern 1 - Click Counter:**
```
When sprite clicked
  Change score by 1      ← Count clicks
  Play sound "pop"
```

**Pattern 2 - Coin Collector:**
```
Forever:
  If touching Coin? then
    Change score by 10   ← 10 points per coin
    Hide (Coin)          ← Coin disappears
```

**Pattern 3 - Timer Countdown:**
```
Set timer to 30
Repeat 30:
  Wait 1 second
  Change timer by -1     ← Countdown!
  If timer < 1 then
    Say "Time's up!"
```

**Pattern 4 - Damage System:**
```
If touching Enemy? then
  Change lives by -1     ← Lose one life
  Play sound "ouch"
  If lives < 1 then
    Say "Game Over"
```

**Advanced - Multipliers:**
```
If powerUp = "yes" then
  Change score by (10 * 2)  ← Double points!
Else
  Change score by 10         ← Normal points
```

**Debugging Change By:**
Add a say block to see what's happening:
```
Change score by 10
Say (join "Score is now " score) for 1 sec
```

**Dependencies:** T09.G3.02

**Time:** 15 minutes

---

### T09.G3.04 - Display a variable on screen

**Learning Objective:** Use "show variable" and "hide variable" blocks

**Description:**
Students use the 'show variable' and 'hide variable' blocks to control whether a variable's value is visible on the stage. The variable must appear and disappear at appropriate times.

**Why Control Variable Display?**
- Hide during setup/countdown
- Show during gameplay
- Hide secret values
- Reduce screen clutter
- Create reveals and surprises

**Starter Code:**
- Cat sprite
- Variable "score" created and visible

**Step-by-Step Instructions:**
1. When green flag clicked:
   - Hide variable score
   - Set score to 0
   - Say "Get ready..." for 1 second
   - Wait 1 second
   - Say "GO!" for 1 second
   - Show variable score
2. When this sprite clicked:
   - Change score by 1
3. Test: Score hidden at start, appears after countdown!

**Success Criteria (Auto-Grade):**
- ✅ Uses "show variable" block
- ✅ Uses "hide variable" block
- ✅ Variable visibility changes correctly
- ✅ Timing of show/hide is appropriate

**Common Errors & Hints:**
- **Always visible:** "Use 'hide variable' at the start"
- **Never appears:** "Did you add 'show variable' before the game starts?"
- **Can still see it:** "Make sure you're using the BLOCK not just unchecking the checkbox"

**Show/Hide vs Checkbox:**
- **Checkbox:** Manual control (for testing)
- **Show/Hide blocks:** Code control (for games)

**Variable Display Styles:**
You can right-click the variable on stage and choose:
- **Normal readout:** "score: 42"
- **Large readout:** Just "42" (bigger)
- **Slider:** Can drag to change value

**Game Flow Pattern:**
```
When green flag clicked
  Hide all variables     ← Start clean
  Set score to 0
  Set lives to 3

  Say "3..." for 1 sec   ← Countdown
  Say "2..." for 1 sec
  Say "1..." for 1 sec
  Say "GO!" for 1 sec

  Show variable score    ← Now show variables
  Show variable lives

  ... game starts ...
```

**Advanced - Toggle Visibility:**
```
When [space] key pressed
  If score visible? then     ← Need to track this
    Hide variable score
  Else
    Show variable score
```

**Positioning Variables:**
- Drag variable display to different screen positions
- Top-left: Common for score
- Top-right: Common for lives/time
- Bottom: Common for status messages

**Multiple Variables:**
```
Hide variable score        ← Hide each one
Hide variable lives
Hide variable timer

... countdown ...

Show variable score        ← Show each one
Show variable lives
Show variable timer
```

**Dependencies:** T09.G3.01

**Time:** 15 minutes

---

### T09.G3.05 - Use variables in your code

**Learning Objective:** Insert variable blocks into other blocks to use values

**Description:**
Students insert variable blocks into other blocks (like move, say, or if-then) to use variable values. The code must use a variable's value to control sprite behavior (e.g., move by the value stored in a variable).

**Why This Is Powerful:**
Variables can control ANYTHING:
- How far to move
- What to say
- How long to wait
- When to do something
- Everything becomes dynamic!

**Starter Code:**
- Cat sprite
- Variable "speed" created

**Step-by-Step Instructions:**
1. When green flag clicked:
   - Set speed to **(pick random 3 to 10)**
   - Say (join "My speed is " speed) for 2 seconds
2. Forever:
   - Move **speed** steps ← Use the variable!
   - If on edge, bounce
3. Test multiple times - different speed each time!

**Success Criteria (Auto-Grade):**
- ✅ Variable block (oval) used inside another block
- ✅ Variable value controls sprite behavior
- ✅ Behavior changes based on variable value
- ✅ Multiple uses of variables in different ways

**Common Errors & Hints:**
- **Using numbers instead:** "Drag the VARIABLE oval block (score) not a number!"
- **Doesn't change:** "Make sure you SET the variable to different values"
- **Wrong variable:** "Check you're using the right variable name"

**How to Insert Variables:**
1. Find the block you want to use (like "move ___ steps")
2. Find the variable reporter (oval shape)
3. Drag the variable INTO the blank spot
4. Now it uses the variable's value!

**Variable Uses - The Power List:**

**1. Variables in Motion:**
```
Move (speed) steps            ← Dynamic movement
Change y by (jumpHeight)      ← Variable jumping
Go to x:(targetX) y:(targetY) ← Variable positions
Glide (time) secs to x:0 y:0  ← Variable timing
```

**2. Variables in Looks:**
```
Say (score) for 2 seconds     ← Show the value
Say (join "Score: " score)    ← Better formatting
Set size to (playerSize)      ← Variable size
Change color by (colorSpeed)  ← Variable effects
```

**3. Variables in Control:**
```
Wait (delayTime) seconds      ← Variable timing
Repeat (numberOfTimes)        ← Variable loops
If x position > (boundary)    ← Variable conditions
```

**4. Variables in Operators:**
```
If score > (winScore) then    ← Compare to variable
Set total to (score + bonus)  ← Math with variables
Pick random 1 to (maxValue)   ← Variable range
```

**Real Game Example - Difficulty Scaling:**
```
When green flag clicked
  Set level to 1
  Set enemySpeed to 3

When [space] pressed
  Change level by 1
  Set enemySpeed to (level + 2)  ← Speed increases with level!

For Enemy sprite:
Forever:
  Move (enemySpeed) steps        ← Uses variable speed!
  If on edge, bounce
```

**Advanced Pattern - Variable-Controlled Animation:**
```
Set animationSpeed to 0.1      ← Fast animation
Repeat 10:
  Next costume
  Wait (animationSpeed) seconds ← Variable timing!

Set animationSpeed to 0.5      ← Slow animation
Repeat 10:
  Next costume
  Wait (animationSpeed) seconds ← Same code, different speed!
```

**Join for Better Messages:**
Instead of just saying the number:
```
Say (score)                         = "42"

Say (join "Score: " score)          = "Score: 42"

Say (join "You have " lives " lives!") = "You have 3 lives!"
```

**Common Pattern - Dynamic Difficulty:**
```
When green flag clicked
  Set difficulty to "easy"

  If difficulty = "easy" then
    Set enemySpeed to 3
    Set maxEnemies to 5

  If difficulty = "hard" then
    Set enemySpeed to 8
    Set maxEnemies to 15
```

**Teaching Point:**
Without variables, every value would be fixed. With variables, your entire program becomes flexible and powerful!

**Dependencies:** T09.G3.02

**Time:** 20 minutes

---

## T13: Debugging (3 skills)

### T13.G3.01 - Use say blocks to see what's happening

**Learning Objective:** Use say blocks to display variable values and debug code

**Description:**
Students add 'say' blocks to their code to display variable values or check if certain parts of code are running. The debugging technique must help identify why code isn't working as expected.

**What Is Debugging?**
Finding and fixing problems (bugs) in your code. Say blocks are like X-ray vision into your program!

**Why Say Blocks for Debugging?**
- See what value variables have
- Check if code is running
- Find where code stops working
- Understand what's happening

**Starter Code:**
- Cat sprite
- Broken code provided:
```
When green flag clicked
  Set score to 10
  Change score by (speed)  ← But speed isn't set!
  Move (score) steps
```

**Step-by-Step Instructions:**
1. Read the broken code
2. Before "change score by", add:
   - Say (join "Score before: " score) for 1 sec
3. Before "change score by", add:
   - Say (join "Speed is: " speed) for 1 sec
4. After "change score by", add:
   - Say (join "Score after: " score) for 1 sec
5. Run the code and watch the messages
6. Figure out the bug: speed is never set!
7. Fix: Add "set speed to 5" at the start

**Success Criteria (Auto-Grade):**
- ✅ Adds say blocks to show variable values
- ✅ Say blocks help identify the problem
- ✅ Finds the bug (speed not initialized)
- ✅ Fixes the bug correctly
- ✅ Explains what was wrong

**Common Debugging Say Patterns:**

**Pattern 1 - Show Variable Values:**
```
Say (join "Score: " score) for 1 sec
Say (join "Lives: " lives) for 1 sec
Say (join "x: " x position) for 1 sec
```

**Pattern 2 - Check If Code Runs:**
```
When green flag clicked
  Say "Started!" for 1 sec        ← Check start

  Repeat 10:
    Say "Inside loop!" for 0.5 sec ← Check loop runs
    Move 10 steps

  Say "Loop done!" for 1 sec      ← Check completion
```

**Pattern 3 - Check Conditions:**
```
If score > 50 then
  Say "TRUE - score is high" for 1 sec
Else
  Say "FALSE - score is low" for 1 sec
```

**Pattern 4 - Track Changes:**
```
Say (join "Before: " score) for 1 sec
Change score by 10
Say (join "After: " score) for 1 sec
← See if change worked!
```

**Common Bugs to Find with Say:**

**Bug 1 - Variable Not Set:**
```
Change score by (bonus)
← Error: bonus is not set!

Fix: Set bonus to 10 first
```

**Bug 2 - Wrong Variable:**
```
If lives > 0 then...
← But you're changing "health" not "lives"

Fix: Use same variable everywhere
```

**Bug 3 - Math Errors:**
```
Say (join "Result: " (10 + 5 * 2))
← Check if math is right (20 not 30)
```

**Bug 4 - Code Not Running:**
```
When green flag clicked
  Say "Step 1" for 1 sec
  Move 100 steps
  Say "Step 2" for 1 sec

← If "Step 2" never shows, code crashed at Move
```

**Real Debugging Session:**
```
Problem: Score isn't increasing when I collect coins

Debug:
1. Add: Say "Coin touched!" when touching coin
   → Message appears! (touching works)

2. Add: Say (join "Before: " score) before change
   → Shows "Before: 0"

3. Add: Say (join "After: " score) after change
   → Shows "After: 0" (score didn't change!)

4. Check change block
   → Found bug: "change score by score" (should be by 10!)

Fix: Change score by 10
```

**Advanced - Debugging Forever Loops:**
```
Forever:
  Say (join "Loop running, score=" score) for 0.1 sec
  Move 5 steps
  If touching edge then...

← Shows loop is running and score value each frame
```

**Pro Tips:**
- Use short wait times (0.5-1 sec) to keep debugging fast
- Use "join" to show what you're checking
- Add say blocks before AND after problem area
- Remove debug says when finished (or comment them out)

**Common Errors & Hints:**
- **Too many messages:** "Use shorter wait times or fewer say blocks"
- **Can't see message:** "Make wait time longer (2 seconds)"
- **Message wrong:** "Check spelling of variable name exactly"

**Dependencies:** T09.G3.02, T11.G3.02

**Time:** 20 minutes

---

### T13.G3.02 - Test your code step by step

**Learning Objective:** Build and test code incrementally, one block at a time

**Description:**
Students build code gradually, testing each new block before adding the next one. They must demonstrate adding code in small steps and verifying each step works before proceeding.

**What Is Incremental Testing?**
Add a little bit of code → Test it → If it works, add more
NOT: Write all code → Test → Everything's broken → Don't know why

**Why Test Step by Step?**
- Find bugs immediately
- Know exactly what's wrong
- Less overwhelming
- Faster debugging
- Build confidence

**Challenge Activity:**
Build this program step by step, testing after EACH step:

**Goal: Make a spinning, growing, color-changing sprite**

**Step-by-Step Building:**

**Step 1:**
```
When green flag clicked
← Test: Nothing happens (but no errors!)
```
✅ Works? Add Step 2

**Step 2:**
```
When green flag clicked
  Set size to 50
← Test: Sprite shrinks to 50%
```
✅ Works? Add Step 3

**Step 3:**
```
When green flag clicked
  Set size to 50
  Repeat 10:
    (empty)
← Test: Still works, sprite at 50%
```
✅ Works? Add Step 4

**Step 4:**
```
When green flag clicked
  Set size to 50
  Repeat 10:
    Change size by 10
← Test: Sprite grows from 50 to 150
```
✅ Works? Add Step 5

**Step 5:**
```
When green flag clicked
  Set size to 50
  Repeat 10:
    Change size by 10
    Wait 0.2 seconds
← Test: Sprite grows slowly
```
✅ Works? Add Step 6

**Step 6:**
```
When green flag clicked
  Set size to 50
  Repeat 10:
    Change size by 10
    Turn 36 degrees
    Wait 0.2 seconds
← Test: Sprite grows and spins
```
✅ Works? Add Step 7

**Step 7:**
```
When green flag clicked
  Set size to 50
  Repeat 10:
    Change size by 10
    Turn 36 degrees
    Change color effect by 10
    Wait 0.2 seconds
← Test: Sprite grows, spins, changes colors!
```
✅ Perfect!

**Success Criteria (Auto-Grade):**
- ✅ Builds program in small steps
- ✅ Tests after each addition
- ✅ Final program works correctly
- ✅ Can explain the step-by-step process
- ✅ Identifies which step caused any problems

**Common Errors & Hints:**
- **Adds too much at once:** "Add ONE block, test it, then add the next"
- **Doesn't test:** "Click the green flag after EVERY step"
- **Gives up when stuck:** "Go back to last working step and try again"

**Incremental Testing Process:**
1. Start with event block
2. Add ONE block
3. Test
4. If it works → Add next block
5. If it breaks → Remove block and try differently
6. Repeat until done

**What to Test At Each Step:**
- Does code run without errors?
- Does sprite do what you expect?
- Are variables changing correctly?
- Are movements smooth?
- Do conditions work?

**Example - Building a Game Step by Step:**

**Step 1: Make sprite appear**
```
When green flag clicked
  Show
  Go to x:0 y:0
← Test: Sprite appears at center
```

**Step 2: Add movement**
```
... previous code ...
Forever:
  Move 5 steps
← Test: Sprite moves right
```

**Step 3: Add bouncing**
```
... previous code ...
Forever:
  Move 5 steps
  If on edge, bounce
← Test: Sprite bounces
```

**Step 4: Add score**
```
... previous code ...
When this sprite clicked
  Change score by 1
← Test: Clicking increases score
```

**Each step works = Easy debugging!**

**What If a Step Breaks?**

**Problem at Step 4:**
- Remove Step 4
- Program works again (back to Step 3)
- Try Step 4 differently
- Maybe use "if touching mouse pointer" instead

**Teaching Moment:**
Professional programmers ALWAYS test step by step. No one writes 100 lines of code and runs it for the first time hoping it works!

**Common Patterns:**
- **Start simple:** Get basic structure working
- **Add features:** One at a time
- **Test constantly:** After every change
- **Build confidence:** Small wins add up

**Dependencies:** T06.G3.01

**Time:** 20 minutes

---

### T13.G3.03 - Find and fix common errors

**Learning Objective:** Identify and fix common coding errors

**Description:**
Students identify and fix common coding errors like blocks not connected, wrong event block, or blocks in wrong order. They must successfully debug provided code with at least 2 errors.

**Common Coding Errors (The Big 5):**

**Error 1: Blocks Not Connected**
```
When green flag clicked
Move 10 steps               ← Floating! Not connected!
```
Fix: Snap it underneath the event block

**Error 2: Wrong Event Block**
```
When this sprite clicked    ← Wrong event!
  Forever:
    Move 5 steps
    If on edge, bounce
```
Should be: "When green flag clicked" for continuous motion

**Error 3: Blocks in Wrong Order**
```
When green flag clicked
  Change score by 1         ← Used before set!
  Set score to 0            ← Should be first!
```
Fix: Set must come before change

**Error 4: Wrong Block Type**
```
Forever:
  Repeat 10:               ← Loop inside loop = confusing
    Move 5 steps
```
Should be: Just forever OR just repeat, not both

**Error 5: Missing Blocks**
```
Forever:
  Move 5 steps
  ← Missing "if on edge, bounce"!
```
Sprite goes off-screen forever!

**Debugging Challenge - Fix These Broken Programs:**

**Broken Program 1: Cat That Won't Move**
```
Move 10 steps               ← Floating block!
When green flag clicked     ← Nothing under it!
```
Errors:
1. Blocks not connected
2. Wrong order

Fix:
```
When green flag clicked
  Move 10 steps             ← Connected and under event
```

**Broken Program 2: Score That Won't Increase**
```
When green flag clicked
  Change score by 1         ← Score not set first!

When this sprite clicked
  Say "Click me!"
```
Errors:
1. Score not initialized
2. Wrong event for changing score

Fix:
```
When green flag clicked
  Set score to 0            ← Initialize!

When this sprite clicked
  Change score by 1         ← Right event!
  Say "Click me!"
```

**Broken Program 3: Forever Loop Gone Wrong**
```
When green flag clicked
Forever:                    ← Not connected!
  Say "Hello!" for 1 second
  Wait 2 seconds
```
Error:
1. Forever not connected to event

Fix:
```
When green flag clicked
  Forever:                  ← Connected!
    Say "Hello!" for 1 second
    Wait 2 seconds
```

**Broken Program 4: Bouncing Sprite Stuck**
```
When green flag clicked
  Forever:
    If on edge, bounce      ← No movement!
```
Error:
1. Missing move block

Fix:
```
When green flag clicked
  Forever:
    Move 5 steps            ← Added movement!
    If on edge, bounce
```

**Success Criteria (Auto-Grade):**
- ✅ Identifies all errors in broken code
- ✅ Fixes all errors correctly
- ✅ Fixed program works as intended
- ✅ Can explain what was wrong
- ✅ Can explain the fix

**Debugging Checklist:**

**When code doesn't work, check:**
- [ ] Are all blocks connected?
- [ ] Is the right event block at the top?
- [ ] Are blocks in the right order?
- [ ] Are variables set before being used?
- [ ] Are loops and ifs in the right places?
- [ ] Are there any floating blocks?
- [ ] Did you click the green flag to test?

**Visual Debugging - Look For:**
- **Floating blocks:** Blocks not touching others
- **Wrong colors:** Event color on wrong type of block
- **Missing pieces:** Gaps in the code
- **Too much nesting:** Loops inside loops inside loops
- **Backwards logic:** IF touching THEN move away (should be towards)

**Advanced Error - Logic Bugs:**
```
If score < 10 then
  Say "You win!"           ← Backwards! Should be > not <
```

**Advanced Error - Variable Name Typo:**
```
Set scor to 0              ← Typo! "scor" not "score"
Change score by 1          ← Using different variable!
```

**Debugging Strategy:**
1. **Read the code** - What should it do?
2. **Run the code** - What does it actually do?
3. **Find the difference** - What's wrong?
4. **Check connections** - All blocks attached?
5. **Check order** - Right sequence?
6. **Check values** - Right numbers/variables?
7. **Fix and test** - Make one fix, test it
8. **Repeat** - Until it works!

**Common Student Mistakes:**

**Mistake 1: "It doesn't work!"**
Better: "When I click the sprite, the score doesn't increase"
(Specific problem = easier to fix)

**Mistake 2: Changing everything at once**
Better: Fix one thing, test, then fix next thing

**Mistake 3: Not reading error messages**
Better: Read carefully - CreatiCode often shows what's wrong

**Real Debugging Story:**
```
Problem: "My sprite won't bounce!"

Code:
Forever:
  Move 5 steps
  If on edge bounce         ← Missing comma!

Debug process:
1. Check connection - Connected ✓
2. Check event - Right event ✓
3. Check blocks - Found it! Wrong block name!
4. Fix: Use "if on edge, bounce" (with comma)
5. Test - Works! ✓
```

**Pro Debugging Tips:**
- Start from the event block and read down
- Check one block at a time
- Use say blocks to see what's happening
- Remove blocks until it works, then add back
- Ask: "What did I change last?"

**Dependencies:** T13.G3.02

**Time:** 25 minutes

---

## Week 3 Summary

**Total Skills Completed This Week:** 8
**TOTAL FOUNDATIONAL SKILLS COMPLETED:** 41/41 ✅

**Variables Skills Mastered:**
- Create and name variables
- Set variable values
- Change variables (increment/decrement)
- Show and hide variable displays
- Use variables in code (dynamic behavior)

**Debugging Skills Mastered:**
- Use say blocks to debug
- Test code incrementally
- Find and fix common errors

**Students Can Now:**
- Store and track information with variables
- Create dynamic programs that change behavior
- Build counters, scores, and game stats
- Debug their own code effectively
- Build programs step-by-step
- Find and fix common errors
- Read and understand code

**Congratulations!**
Students have mastered all 41 foundational block skills!

**They are now ready for:**
- Building complete games
- Creating interactive stories
- Making advanced projects
- Learning advanced blocks (functions, lists, cloning)
- Competition preparation (ACSL, Scratch Olympiad)
- Independent creative projects

**Gateway Skills Mastered:**
1. T06.G3.01 - Events (green flag)
2. T07.G3.01 - Wait blocks
3. T07.G3.02 - Repeat loops
4. T07.G3.03 - Forever loops
5. T08.G3.01 - If-then conditionals
6. T09.G3.01 - Variables (THE BIG ONE - 297 dependents!)

**Complete Skill Coverage:**
- **Events:** 5 skills
- **Loops:** 4 skills
- **Conditionals:** 4 skills
- **Operators:** 5 skills
- **Motion:** 7 skills
- **Looks:** 6 skills
- **Sensing:** 2 skills
- **Variables:** 5 skills
- **Debugging:** 3 skills

**Next Steps:**
1. Integration projects (combine all skills)
2. Game development track
3. Storytelling track
4. Data visualization track
5. AI integration track

**Integration Project Ideas:**
1. **Clicker Game** - Use all variables, events, looks
2. **Maze Game** - Use motion, sensing, conditionals
3. **Catch Game** - Use motion, variables, collision
4. **Story Adventure** - Use events, looks, variables
5. **Race Game** - Use all motion, loops, variables

**Assessment Ideas:**
- Can student build a complete working game?
- Can student debug broken code independently?
- Can student explain their code?
- Can student use variables effectively?
- Can student combine multiple skills?

**The Foundation Is Complete!**
These 41 skills unlock all future learning in CreatiCode. Every advanced skill in Grades 4-8 builds on these foundations.
