# Foundational Skills Implementation Guide

**Purpose:** Comprehensive guide for teaching the 41 Grade 3 foundational block skills
**Audience:** Teachers, curriculum designers, platform developers
**Last Updated:** 2025-11-17

---

## Table of Contents

1. [Overview](#overview)
2. [Teaching Philosophy](#teaching-philosophy)
3. [Weekly Breakdown](#weekly-breakdown)
4. [Teaching Strategies](#teaching-strategies)
5. [Common Student Errors](#common-student-errors)
6. [Assessment & Progress Monitoring](#assessment--progress-monitoring)
7. [Differentiation Strategies](#differentiation-strategies)
8. [Platform Implementation Notes](#platform-implementation-notes)
9. [Sample Lesson Plans](#sample-lesson-plans)
10. [Resources & Materials](#resources--materials)

---

## Overview

### What Are Foundational Skills?

The 41 foundational block skills represent THE MINIMUM skills students need to begin productive coding in CreatiCode. Without these skills, students cannot:
- Build games
- Create animations
- Make interactive stories
- Progress to Grades 4-8 content

### Critical Statistics

- **Total Skills:** 41
- **Gateway Skills:** 6 (T06.G3.01, T07.G3.01, T07.G3.02, T07.G3.03, T08.G3.01, T09.G3.01)
- **Most Critical Gateway:** T09.G3.01 (Variables) - unlocks 297 dependent skills
- **Estimated Time:** 12-15 hours of instruction across 3 weeks
- **Success Target:** 80%+ of students master all 41 skills

### Why Grade 3?

Grade 3 is empirically the **critical transition year**:
- **K-2:** Picture-based conceptual foundations (206 skills)
- **Grade 3:** THE BRIDGE → Block coding begins (41 foundational skills)
- **Grades 4-8:** Progressive coding proficiency (900+ advanced skills)

Dependencies jump 154% from Grade 2 to Grade 3, making this the make-or-break year for CS education.

---

## Teaching Philosophy

### Core Principles

**1. One Block, One Skill**
Each skill focuses on ONE specific block or ONE specific combination. Don't teach too much at once.

**Good:** "Today we learn the 'move steps' block"
**Bad:** "Today we learn motion" (too broad)

**2. Immediate Success**
Students should see results within 30 seconds of trying a new block.

**Example:** First use of "move 10 steps" should make the cat visibly move immediately.

**3. Scaffolding & Support**
- Provide starter code to reduce cognitive load
- Break complex skills into micro-steps
- Use visual examples and demonstrations
- Offer hint cards and reference materials

**4. Test Early, Test Often**
Students should test their code after EVERY block added (incremental testing).

**Not:** Write all code → Test → Everything's broken
**Yes:** Add one block → Test → Add next block → Test

**5. Debugging Is Part of Learning**
Errors are learning opportunities, not failures. Teach debugging from Day 1.

**6. Gateway Skills Get Extra Time**
Allocate 40-50% of instructional time to the 6 gateway skills. These are THAT important.

---

## Weekly Breakdown

### Week 1: Core Blocks (20 skills)

**Focus:** Events, Loops, Conditionals, Operators, Basic Motion

**Day 1 (2 hours):**
- **Morning:** T06.G3.01 (green flag) ⭐ GATEWAY
  - Why this first? Foundation of all programs
  - Activity: Make cat walk when flag clicked
- **Afternoon:** T06.G3.02-T06.G3.03 (sprite clicked, keyboard)
  - Activity: Multi-event program

**Day 2 (2 hours):**
- **Morning:** T07.G3.01 (wait) ⭐ GATEWAY
  - Timing and sequencing
  - Activity: Slow-motion cat walk
- **Afternoon:** T07.G3.02 (repeat) ⭐ GATEWAY
  - Introduction to loops
  - Activity: Draw a square

**Day 3 (2 hours):**
- **Morning:** T07.G3.03 (forever) ⭐ GATEWAY
  - Continuous behavior
  - Activity: Spinning sprite
- **Afternoon:** T08.G3.01 (if-then) ⭐ GATEWAY
  - Decisions in code
  - Activity: Edge detection

**Day 4 (2 hours):**
- **Morning:** T08.G3.02-T08.G3.04 (conditionals)
  - If-then-else, comparisons, collisions
- **Afternoon:** T10.G3.01-T10.G3.05 (operators)
  - Math and text operations

**Day 5 (1 hour):**
- **Consolidation:** T05.G3.01-T05.G3.02 (basic motion)
  - Practice and integration
  - Mini-project: Simple interactive program

**Week 1 Success Criteria:**
- Students can start programs with events
- Students can create loops and patterns
- Students can make basic decisions with if-then
- Students can use math in their code

### Week 2: Visual & Interactive (13 skills)

**Focus:** Advanced Motion, Looks, Sensing

**Day 1 (2 hours):**
- **Morning:** T05.G3.03-T05.G3.05 (glide, go to, change x/y)
  - Coordinate system mastery
- **Afternoon:** T05.G3.06-T05.G3.07 (bounce, point towards)
  - Advanced motion techniques

**Day 2 (2 hours):**
- **Morning:** T11.G3.01-T11.G3.03 (show/hide, say/think, costumes)
  - Visual feedback
- **Afternoon:** T11.G3.04-T11.G3.06 (size, effects, layers)
  - Visual effects mastery

**Day 3 (1 hour):**
- **Consolidation:** T12.G3.01-T12.G3.02 (sensing)
  - Collision detection
  - Integration practice

**Week 2 Success Criteria:**
- Students can position sprites precisely
- Students can create smooth animations
- Students can detect collisions
- Students can create visually appealing projects

### Week 3: Data & Polish (8 skills)

**Focus:** Variables and Debugging

**Day 1 (2 hours):**
- **Full Focus:** T09.G3.01 (create variable) ⭐ MOST CRITICAL
  - This is THE gateway skill (297 dependents)
  - Multiple examples and practice
  - Activity: Score counter

**Day 2 (2 hours):**
- **Morning:** T09.G3.02-T09.G3.03 (set, change)
  - Working with variables
- **Afternoon:** T09.G3.04-T09.G3.05 (show/hide, use in code)
  - Dynamic behavior with variables

**Day 3 (2 hours):**
- **Morning:** T13.G3.01-T13.G3.03 (debugging)
  - Debug with say blocks
  - Incremental testing
  - Fix common errors
- **Afternoon:** Integration project
  - Combine all 41 skills

**Week 3 Success Criteria:**
- Students can create and use variables
- Students can track scores and data
- Students can debug their own code
- Students can build complete projects independently

---

## Teaching Strategies

### Strategy 1: I Do, We Do, You Do

**I Do (5 minutes):**
- Teacher demonstrates the skill
- Think-aloud: "Now I'm going to add the move block..."
- Show the result
- Explain why it works

**We Do (10 minutes):**
- Teacher and students do together
- Call on students for next steps
- Guide through any errors
- Celebrate when it works

**You Do (10-15 minutes):**
- Students work independently
- Teacher circulates and helps
- Students help each other (pair programming)
- Early finishers get extension challenges

### Strategy 2: Worked Examples

Provide complete working examples with annotations:

```
When green flag clicked    ← This starts the program
  Set score to 0           ← Initialize the variable
  Forever:                 ← Keep doing this forever
    If touching Mouse?     ← Check if mouse is touching
      Change score by 1    ← Add one point
      Play sound Pop       ← Give feedback
```

### Strategy 3: Error Analysis

Show broken code and have students find the error:

**Broken Code:**
```
Move 10 steps              ← What's wrong?
When green flag clicked
```

**Fixed Code:**
```
When green flag clicked    ← Event must be first!
  Move 10 steps
```

### Strategy 4: Pair Programming

Students work in pairs:
- **Driver:** Uses the keyboard/mouse
- **Navigator:** Reads instructions, checks for errors
- **Switch** every 5-10 minutes

Benefits:
- Reduces frustration
- Builds collaboration
- Improves debugging
- More voices in problem-solving

### Strategy 5: Scaffolding Gradual Release

**High Scaffolding (Beginning):**
- Complete starter code provided
- Step-by-step instructions
- Visual guides
- Teacher check-ins every 2 minutes

**Medium Scaffolding (Middle):**
- Partial starter code
- Hint cards available
- Students ask for help when needed
- Teacher check-ins every 5 minutes

**Low Scaffolding (End):**
- Just the goal, no starter code
- Self-guided learning
- Peer helpers
- Teacher available but students more independent

### Strategy 6: Metacognition & Reflection

After each skill, ask:
- "What did you learn?"
- "What was tricky?"
- "How could you use this in a project?"
- "What do you want to try next?"

Use exit tickets:
- 🟢 I got it! (can explain to others)
- 🟡 I mostly got it (need a little more practice)
- 🔴 I'm stuck (need help)

---

## Common Student Errors

### Category 1: Connection Errors

**Error:** Blocks floating (not connected)
**Why:** Students drag blocks but don't "snap" them together
**Fix:**
- Teach the "click sound" when blocks connect
- Visual: "Look for the white line that appears"
- Practice: Have students connect/disconnect blocks repeatedly

**Error:** Wrong order (move before event)
**Why:** Students don't understand execution flow
**Fix:**
- Use "traffic light" analogy: Green flag is the green light to GO
- Show: "Code runs from top to bottom"

### Category 2: Event Confusion

**Error:** Using "sprite clicked" when they mean "flag clicked"
**Why:** All event blocks look similar
**Fix:**
- Color-code event types
- Chant: "Green flag starts the program"
- Post reference chart on wall

**Error:** Multiple start events (two flag clicked blocks doing different things)
**Why:** Don't understand events trigger independently
**Fix:**
- Demo with two sprites
- Show: Flag clicked makes EVERYTHING with flag clicked run at once

### Category 3: Loop Misunderstandings

**Error:** Putting repeat inside forever (or vice versa)
**Why:** Don't understand loop purposes
**Fix:**
- Repeat = "Do this X times then STOP"
- Forever = "Do this FOREVER, never stop"
- Visual chart showing loop types

**Error:** Not putting blocks INSIDE the loop
**Why:** Visual confusion about what "inside" means
**Fix:**
- Highlight the C-shape gap
- Practice dragging blocks into the gap
- Use highlighter to show "inside" vs "outside"

### Category 4: Variable Challenges

**Error:** Using variable before setting it
**Why:** Don't understand initialization
**Fix:**
- Analogy: "Empty box has nothing in it - put something in first!"
- Rule: "Always SET before CHANGE or USE"

**Error:** Wrong variable name (typo or wrong variable)
**Why:** Multiple variables look similar
**Fix:**
- Use descriptive names (score not s)
- Color-code variables (not possible in Scratch but can annotate)
- Checklist: "Did I use the RIGHT variable?"

**Error:** Setting when they mean changing (or vice versa)
**Why:** Confusing SET vs CHANGE
**Fix:**
- SET = "Put this exact number in the box"
- CHANGE = "Add this amount to what's already there"
- Practice both with physical counters

### Category 5: Sensing & Collision

**Error:** Collision not detected
**Why:** Sprites not actually overlapping, or wrong sprite name
**Fix:**
- Make sprites BIGGER (easier to touch)
- Debug: Add "say touching Ball?" to see true/false
- Check spelling of sprite names EXACTLY

**Error:** "Touching edge" when they mean "touching sprite"
**Why:** Dropdown confusion
**Fix:**
- Practice reading dropdowns carefully
- Color-code: Edge detection (green), sprite detection (blue)

### Category 6: Coordinate Confusion

**Error:** Mixing up x and y
**Why:** Abstract concept for 8-9 year olds
**Fix:**
- X = "Cross" (left-right)
- Y = "Up" (up-down)
- Physical grid on floor for walking through coordinates

**Error:** Negative numbers confusing
**Why:** New math concept for many
**Fix:**
- Number line on wall
- "Negative means OPPOSITE direction"
- Practice with temperature (below zero)

---

## Assessment & Progress Monitoring

### Formative Assessment (Daily)

**1. Observation Checklist:**
```
Student: _______________ Date: _______

Skill: T06.G3.01 (Green Flag Event)

Observations:
☐ Finds green flag block independently
☐ Connects blocks correctly
☐ Tests code by clicking flag
☐ Troubleshoots when not working
☐ Can explain what green flag does

Level:
☐ Mastered (can teach others)
☐ Proficient (independent)
☐ Developing (needs hints)
☐ Beginning (needs support)

Notes: ________________________
```

**2. Exit Tickets:**
- 3-2-1: 3 things learned, 2 things to practice, 1 question
- Code snippet: "Write code to make sprite move and turn"
- Self-assessment: Traffic light (red/yellow/green)

**3. Quick Checks:**
- "Show me the repeat block"
- "Point to the event block in your code"
- "What does this code do?" (code reading)

### Summative Assessment (Weekly/End of Unit)

**Week 1 Assessment: Basic Controls**
```
Task: Create a program that:
1. Starts with green flag
2. Makes sprite move in a square (using repeat)
3. Has sprite respond to space bar with a jump
4. Uses wait blocks for timing

Rubric:
4 = All working perfectly, extra features
3 = All working correctly
2 = Most working, minor errors
1 = Some working, needs support
0 = Not working, start over
```

**Week 2 Assessment: Visual & Interactive**
```
Task: Create an animation that:
1. Sprite glides to 3 different positions
2. Changes costumes while moving
3. Changes size or color
4. Detects when it touches the edge

Rubric: Same 0-4 scale
```

**Week 3 Assessment: Complete Project**
```
Task: Create a simple clicker game:
1. Score variable starts at 0
2. Clicking sprite increases score
3. Score is displayed on screen
4. Uses at least 5 different block categories
5. Code is organized and tested

Rubric:
5 = Exceeds (added creative features)
4 = Proficient (all requirements met)
3 = Developing (most requirements met)
2 = Beginning (some requirements met)
1 = Needs support
```

### Gateway Skill Assessments

For the 6 gateway skills, use more thorough assessment:

**T09.G3.01 (Variables) - Extended Assessment:**
```
Part 1: Create a variable named "lives"
Part 2: Set lives to 3 when program starts
Part 3: Make lives decrease when sprite touches edge
Part 4: Show "Game Over" when lives reach 0
Part 5: Explain what a variable is in your own words

Criteria:
- Technical mastery (does it work?)
- Conceptual understanding (can they explain?)
- Application (can they use it in new contexts?)
```

### Progress Tracking Dashboard

Track class progress on all 41 skills:

```
Skill Status Dashboard
=======================
T06.G3.01: ████████████████░░░░  80% mastered
T06.G3.02: █████████████████░░░  85% mastered
T06.G3.03: ██████████████░░░░░░  70% mastered
...

Gateway Skills:
T09.G3.01: ██████████████░░░░░░  70% mastered ⚠️ FOCUS HERE

Students Needing Support:
- Alice: T07.G3.02 (repeat loops)
- Bob: T08.G3.01 (if-then)
- Carol: T09.G3.01 (variables) ⚠️
```

---

## Differentiation Strategies

### For Struggling Students

**Strategy 1: Break It Down Further**
- Instead of 1 skill in 15 minutes, break into 3 micro-skills
- Use physical manipulatives (block cards to arrange)
- Provide video tutorials to watch and re-watch
- Allow extra time (double period if needed)

**Strategy 2: Peer Tutoring**
- Pair with successful student
- Use "expert groups" - students who master a skill teach others
- Create buddy system for help requests

**Strategy 3: Simplified Versions**
- Start with fewer steps
- Remove optional features
- Focus on core concept only
- Add complexity only after mastery

**Strategy 4: Multi-Sensory**
- Kinesthetic: Walk through code (physical movement)
- Visual: Color-coded reference sheets
- Auditory: Explain code out loud
- Tactile: Use block manipulatives

**Example - Variables for Struggling Students:**
```
Lesson 1: What is a variable? (just concept, no code)
Lesson 2: Create a variable (just creation)
Lesson 3: Set a variable (just setting to 0)
Lesson 4: Show variable on screen (just visibility)
Lesson 5: Change variable (just increment)
Lesson 6: Use variable (combine all skills)
```

### For Advanced Students

**Strategy 1: Extension Challenges**
- "Can you make it do X?"
- Add optional features
- Combine multiple skills creatively
- Optimize code (fewer blocks)

**Strategy 2: Creative Freedom**
- Open-ended projects
- "Build whatever you want using these blocks"
- Design challenges for other students
- Help struggling peers (teaching reinforces learning)

**Strategy 3: Advanced Concepts Preview**
- Introduce functions early
- Show lists and cloning
- Explore custom blocks
- Preview Boolean logic

**Strategy 4: Competition Preparation**
- ACSL problems
- Scratch Olympiad projects
- Mini-hackathons
- Code challenges

**Example - Variables for Advanced Students:**
```
Challenge 1: Create a two-variable system (score AND lives)
Challenge 2: Make variables interact (lives decrease, score bonus changes)
Challenge 3: Create a level system (score thresholds unlock levels)
Challenge 4: Build a high score system (compare to best score)
Challenge 5: Create a complete game using 5+ variables
```

### For English Language Learners (ELL)

**Strategy 1: Visual Supports**
- Picture-based instructions
- Video demonstrations (can watch multiple times)
- Minimal text, maximum visuals
- Symbol/icon reference sheets

**Strategy 2: Bilingual Resources**
- Instructions in home language + English
- Bilingual peer buddies
- Translate key vocabulary
- Allow code comments in home language

**Strategy 3: Reduced Language Load**
- Simplified instructions
- Key word only (not full sentences)
- Demonstrate rather than explain verbally
- Use consistent, repeated phrases

**Key Vocabulary to Pre-Teach:**
- Event, loop, repeat, forever, if-then, variable
- Coordinate, position, motion, costume, effect
- Set, change, increase, decrease
- Touch, detect, sense, collision

---

## Platform Implementation Notes

### Auto-Grading Requirements

For each skill, the platform should check:

**1. Structure Checks (Code Analysis):**
```javascript
{
  "skill_id": "T06.G3.01",
  "checks": [
    {
      "type": "block_exists",
      "block": "event_whenflagclicked",
      "required": true
    },
    {
      "type": "block_exists",
      "block": "motion_movesteps",
      "required": true
    },
    {
      "type": "block_connection",
      "parent": "event_whenflagclicked",
      "child": "motion_movesteps"
    }
  ]
}
```

**2. Runtime Checks (Execution Analysis):**
```javascript
{
  "skill_id": "T06.G3.01",
  "runtime_checks": [
    {
      "type": "position_change",
      "axis": "x",
      "min_change": 8,
      "max_change": 12,
      "trigger": "flag_click"
    }
  ]
}
```

**3. Behavior Checks (Interaction Analysis):**
```javascript
{
  "skill_id": "T08.G3.04",
  "behavior_checks": [
    {
      "type": "collision_response",
      "sprite_a": "Cat",
      "sprite_b": "Ball",
      "expected_action": "sound_or_message"
    }
  ]
}
```

### Hint System

Three-tier hint system for each skill:

**Tier 1 Hint (Gentle Nudge):**
"Remember to use a block from the Events category."

**Tier 2 Hint (More Specific):**
"Look for the block with a green flag picture. It's in the Events category (yellow blocks)."

**Tier 3 Hint (Show Solution):**
[Video demonstration] or [Step-by-step with screenshots]

### Unlock Logic

```javascript
skill_unlocked = (
  all_dependencies_completed() AND
  minimum_grade_level_met() AND
  (not is_gateway() OR teacher_override)
)
```

### Progress Visualization

Show students:
- Skills completed (green checkmarks)
- Skills available (blue, clickable)
- Skills locked (gray, with lock icon)
- Gateway skills (star icon)
- Dependency paths (connecting lines)

### Teacher Dashboard Requirements

Teachers need to see:
1. **Class Progress:** % of students who mastered each skill
2. **Individual Progress:** Which skills each student has mastered
3. **Gateway Focus:** Special alerts for gateway skills <70% mastery
4. **Time on Task:** How long students spend on each skill
5. **Error Patterns:** Common mistakes students are making
6. **Intervention Needed:** Students falling behind

---

## Sample Lesson Plans

### Sample Lesson 1: T06.G3.01 (Green Flag Event)

**Duration:** 45 minutes
**Objective:** Students will use "when green flag clicked" to start a program

**Materials:**
- CreatiCode playground access
- Projector for demonstration
- Reference chart (laminated, 1 per student)

**Lesson Flow:**

**0:00-0:05 - Hook (5 min)**
"Have you ever seen a race? What starts the race? (Flag!) In coding, we also use a flag to start our programs. Let me show you..."

**0:05-0:10 - I Do (5 min)**
Teacher demonstrates:
1. Open CreatiCode
2. Find Events category
3. Drag "when green flag clicked"
4. Add "move 10 steps" underneath
5. Click green flag
6. Cat moves!

**0:10-0:20 - We Do (10 min)**
Students follow along:
1. "Everyone find the Events category - it's yellow!"
2. "Find the block with the green flag"
3. "Drag it to your workspace"
4. "Now let's add movement..."
5. "Click the green flag above the stage"
6. "Did your cat move? Give me thumbs up!"

**0:20-0:35 - You Do (15 min)**
Independent practice:
- Task: Make cat move 10 steps when flag clicked
- Extension: Make cat move AND turn
- Super extension: Make cat move in a square

Teacher circulates, helps struggling students

**0:35-0:40 - Share (5 min)**
2-3 students share their code on projector
Class discusses what worked

**0:40-0:45 - Closure (5 min)**
- Exit ticket: "What does the green flag do?"
- Preview next skill: "Tomorrow we'll learn clicking on sprites!"
- Save work

**Assessment:**
☐ All students have green flag block
☐ All students have move block connected
☐ All students successfully clicked flag and saw movement

---

### Sample Lesson 2: T09.G3.01 (Create Variable) ⭐

**Duration:** 90 minutes (THIS IS CRITICAL - TAKE EXTRA TIME)
**Objective:** Students will create a variable and understand what variables are

**Materials:**
- CreatiCode access
- Physical variable boxes (labeled shoe boxes)
- Index cards with numbers
- Variable reference poster

**Lesson Flow:**

**0:00-0:15 - Hook & Concrete Understanding (15 min)**

**Physical Variable Activity:**
1. Show shoe box labeled "score"
2. "This box is a VARIABLE. A variable is like a labeled box that stores information."
3. Put card with "0" in the box
4. "Right now, score = 0"
5. Add card with "10"
6. "Now score = 10"
7. Remove "10", add "20"
8. "Now score = 20"
9. "The number changes, but the box stays the same!"

**Multiple Examples:**
- Box labeled "lives" with "3"
- Box labeled "level" with "1"
- Box labeled "playerName" with "Alice"

**0:15-0:25 - I Do (10 min)**

Teacher demonstrates in CreatiCode:
1. "Now let's make a variable in code!"
2. Click Variables category
3. "Click 'Make a Variable'"
4. Type "score"
5. Click OK
6. "Look! New blocks appeared!"
7. Check the checkbox to show variable
8. "See it on the stage? That's our variable box!"

**0:25-0:40 - We Do (15 min)**

Students create their first variable:
1. "Everyone, find the Variables category - it's orange"
2. "Click the 'Make a Variable' button"
3. "Type the word: score" (write on board)
4. "Click OK"
5. "Check the box next to 'score' to show it"
6. "Do you see 'score: 0' on your stage?"
7. Check in with each student

**0:40-0:60 - You Do Part 1 (20 min)**

Practice creating variables:
- Create "score" variable ✓
- Create "lives" variable
- Create "level" variable
- Make all three visible

Teacher circulates intensively (this is hard!)

**0:60-0:75 - You Do Part 2 (15 min)**

Simple use:
- Set score to 0 when flag clicked
- Set lives to 3 when flag clicked
- Set level to 1 when flag clicked
- Test by clicking flag multiple times

**0:75-0:85 - Share & Discuss (10 min)**

Gallery walk:
- Students visit 3 other computers
- Check: Do they have all three variables?
- Help anyone who's stuck

Whole class discussion:
- "What is a variable?"
- "Why are variables useful?"
- "What could you use variables for?"

**0:85-0:90 - Assessment & Closure (5 min)**

Exit ticket (written):
1. What is a variable?
2. Draw a picture of a variable storing the number 10
3. Name three things you could track with variables

Preview: "Tomorrow we'll make our variables CHANGE!"

**Special Notes for This Lesson:**

This is THE most important lesson in the entire unit. Variables unlock everything. Common issues:

1. **Students can't find "Make a Variable"**
   - Show multiple times
   - Have students point to button before clicking
   - Use projector + highlight

2. **Variable doesn't appear**
   - Check checkbox!
   - This trips up 50% of students
   - Practice checking/unchecking multiple times

3. **Confusion about variable blocks**
   - "Now you have 5 new blocks - all for THIS variable"
   - Label each block on reference sheet

4. **Naming variables poorly**
   - Pre-approve variable names
   - Write good examples on board
   - Emphasize: Names should tell you what's stored

**Success Criteria:**
- 100% of students create at least one variable
- 90% of students create three variables
- 80% can explain what a variable is
- 70% can use variables in code (tomorrow's lesson)

---

## Resources & Materials

### Printable Materials

**1. Block Reference Cards (1 per category)**
- Events (yellow)
- Control (orange)
- Motion (blue)
- Looks (purple)
- Sensing (light blue)
- Operators (green)
- Variables (orange)

Each card shows:
- Block name
- Block picture
- What it does
- Example use

**2. Skill Checklist Poster**
Large poster showing all 41 skills:
```
Week 1: Core Blocks
☐ T06.G3.01 Green flag starts program ⭐
☐ T06.G3.02 Sprite clicked event
☐ T06.G3.03 Keyboard controls
...

Week 2: Visual & Interactive
☐ T05.G3.03 Glide smoothly
...

Week 3: Data & Polish
☐ T09.G3.01 Create variable ⭐⭐⭐
...
```

Students check off as they complete.

**3. Debugging Checklist Laminated Card**
```
My code isn't working! Check:
☐ Green flag at the top?
☐ All blocks connected? (no floating blocks?)
☐ Right blocks? (check colors)
☐ Variables set before used?
☐ Did I click the green flag to test?
☐ Ask a friend for help?
☐ Ask the teacher?
```

**4. Gateway Skills Poster**
```
GATEWAY SKILLS - The Most Important!

⭐ T06.G3.01 - Start with green flag
⭐ T07.G3.01 - Use wait for timing
⭐ T07.G3.02 - Use repeat for patterns
⭐ T07.G3.03 - Use forever for continuous
⭐ T08.G3.01 - Use if-then for decisions
⭐⭐⭐ T09.G3.01 - Create variables (MOST IMPORTANT!)
```

### Digital Resources

**1. Video Tutorials (2-3 minutes each)**
- One video per skill
- Screen recording with narration
- Shows common errors and fixes
- Closed captions for ELL students

**2. Interactive Examples**
- Remix-able projects for each skill
- Students can see working code
- Modify and experiment
- Save their own versions

**3. Practice Projects**
- 5-10 practice projects per week
- Increasing difficulty
- Auto-graded
- Instant feedback

**4. Extension Challenges**
- For fast finishers
- Creative open-ended projects
- Competition-prep problems
- Advanced skill previews

### Physical Materials

**1. Coding Unplugged**
- Block cards (paper/cardstock)
- Magnetic blocks for whiteboard
- Grid floor mat for coordinates
- Variable boxes (as described above)

**2. Bulletin Board**
- Student work showcase
- "Coder of the Week"
- Project gallery
- Skill progress chart

**3. Help System**
- Red/yellow/green cups (signal for help)
- Help request board
- Peer helper roster
- Office hours signup

### Parent Communication

**1. Welcome Letter**
```
Dear Families,

This month, your child will learn the 41 foundational blocks
of coding in CreatiCode. These skills are the building blocks
for all future computer science learning.

What you can do at home:
- Ask your child to show you their projects
- Encourage persistence when code doesn't work
- Celebrate small victories
- No computer science knowledge needed from you!

Gateway Skills to Watch:
Week 1: Events and Loops
Week 2: Visual Effects
Week 3: VARIABLES (the big one!)

Questions? Contact me at: _______
```

**2. Weekly Progress Reports**
```
Week 1 Progress: Alex

Skills Mastered: 18/20 ✓
Skills in Progress: 2/20
Skills Not Started: 0/20

Strengths:
- Great at loops!
- Creative problem solver
- Helps other students

Areas to Practice:
- If-then conditionals (need more practice)

Next Week: Visual effects and animation!
```

**3. At-Home Activities (Optional)**
```
Help your child practice this week's skills!

Activity 1: Real-Life Events
Look for "events" in daily life:
- Doorbell rings → Answer the door
- Timer beeps → Take out cookies
- Alarm goes off → Wake up

Activity 2: Patterns & Loops
Find repeating patterns:
- Tile floors
- Wallpaper
- Music beats
- Dance moves

Activity 3: If-Then Decisions
Practice conditional thinking:
- IF it's raining THEN bring umbrella
- IF homework is done THEN play games
- IF hungry THEN eat snack
```

---

## Troubleshooting Guide

### Platform Technical Issues

**Issue:** "I can't find the block!"
**Solution:**
1. Check correct category (color)
2. Scroll down in category
3. Use search function
4. Show reference card

**Issue:** "My code deleted!"
**Solution:**
1. Check undo button
2. Check "My Projects" (might have saved earlier version)
3. Use auto-save/restore feature
4. Rebuild (good practice!)

**Issue:** "Green flag doesn't work"
**Solution:**
1. Check blocks connected
2. Check event block at top
3. Click flag above STAGE not in code
4. Refresh page if broken

### Classroom Management

**Issue:** Students off-task
**Solution:**
- Set timer (15 minutes)
- Frequent check-ins
- Show student work (positive attention)
- Extension challenges ready

**Issue:** Wide range of abilities
**Solution:**
- Fast finishers → Extension challenges
- Struggling students → Peer helpers
- Use differentiation strategies (see above)
- Small group pullouts

**Issue:** Students copying each other
**Solution:**
- "Inspiration is okay, copying is not"
- Require personal variations
- Explain understanding > completion
- Pair programming is allowed

---

## Success Metrics

### Student Success Metrics

**Mastery:**
- 80%+ of students master all 41 skills
- 90%+ of students master 6 gateway skills
- 100% of students can create a simple working program

**Engagement:**
- <10% abandon rate per skill
- >70% request additional challenges
- >80% positive attitude towards coding

**Understanding:**
- >75% can explain what their code does
- >70% can debug simple errors independently
- >60% can help peers

### Teacher Success Metrics

**Preparation:**
- All materials ready before class
- Video tutorials available
- Extension activities prepared
- Assessment tools created

**Instruction:**
- Clear demonstrations
- Frequent checks for understanding
- Responsive to student needs
- Positive, encouraging environment

**Outcomes:**
- >80% student mastery
- <5% students significantly behind
- Gateway skills prioritized
- Differentiation implemented

---

## Conclusion

The 41 foundational block skills are the gateway to all future learning in CreatiCode. By following this implementation guide, teachers can ensure that ALL students master these critical skills and are prepared for advanced coding in Grades 4-8.

**Key Takeaways:**

1. **Gateway skills matter most** - Allocate extra time to the 6 gateway skills
2. **Variables are critical** - T09.G3.01 unlocks 297+ dependent skills
3. **Incremental testing** - Test after every block added
4. **Scaffolding** - Start with high support, gradually release
5. **Differentiation** - Meet all learners where they are
6. **Assessment** - Monitor progress daily, adjust instruction

**Remember:** These aren't just "coding skills" - they're problem-solving skills, critical thinking skills, and perseverance skills that will serve students far beyond computer science.

Good luck, and happy coding! 🚀

---

**Document Version:** 1.0
**Last Updated:** 2025-11-17
**Next Review:** 2026-01-15
