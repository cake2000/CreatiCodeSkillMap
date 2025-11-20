# T06 Dependency Analysis for Grade 4 Skills

## Executive Summary

Analyzed 59 Grade 4 skills that currently lack T06 (Events & Sequences) dependencies.

**Findings:**
- **42 skills** should have T06 added (List A)
- **17 skills** do NOT need T06 (List B)

**Rationale:** T06 teaches foundational event handling (green flag, key press, sprite click) which is essential for writing any executable code. Skills that involve building or implementing programs need T06 as a prerequisite. Skills focused purely on analysis, tracing, or debugging existing code do not require T06.

---

## LIST A: Skills That SHOULD Have T06 Added (42 Skills)

### T07 (Loops) - 4 skills need T06

#### T07.G4.01: Create a forever game loop for controls
**Why T06 is needed:** Students must write a script that runs continuously. This requires an event trigger (green flag) to start the forever loop.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T07.G4.02: Loop with a condition inside
**Why T06 is needed:** Students write a loop with conditionals - this is executable code that needs an event to trigger it.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T07.G4.03: Use a loop counter variable
**Why T06 is needed:** Students implement a loop that maintains a counter - this is working code that needs an event trigger to run.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T07.G4.04: Convert repeated blocks with conditions into loops
**Why T06 is needed:** Students rewrite code using loops - they need to build scripts that can be triggered and run.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

---

### T08 (Conditions & Logic) - 5 skills need T06

#### T08.G4.01: Combine two conditions with AND
**Why T06 is needed:** Students use compound conditions in executable code - needs event triggers to run the conditional logic.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T08.G4.02: Combine two conditions with OR
**Why T06 is needed:** Students write conditional logic with OR - this is executable code that needs event triggers.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T08.G4.04: Nest if/else statements
**Why T06 is needed:** Students build nested conditional structures - working code that needs event triggers to execute.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T08.G4.05: Convert nested if to cleaner logic
**Why T06 is needed:** Students refactor conditional code - they need to write scripts with event triggers.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T08.G4.06: Use if to control state changes
**Why T06 is needed:** Students manage game states with conditionals - needs events to respond to game triggers and user input.
**Add dependency:**
```
* T06.G3.02: Build a key-press script that controls a sprite
```

---

### T09 (Variables) - 7 skills need T06

#### T09.G4.01: Use multiplication and division in expressions
**Why T06 is needed:** Students use expressions in working programs - needs event triggers to execute the code.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T09.G4.02: Combine operators and variables in complex expressions
**Why T06 is needed:** Students write code with complex expressions - needs event triggers to run.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T09.G4.03: Store and use user input in a variable
**Why T06 is needed:** Students capture and use user input - this interactive feature needs event triggers.
**Add dependency:**
```
* T06.G3.02: Build a key-press script that controls a sprite
```

#### T09.G4.04: Use variables in a loop counter pattern
**Why T06 is needed:** Students combine loops and variables - needs event triggers to start the loop.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T09.G4.05: Use comparison operators in expressions
**Why T06 is needed:** Students use comparisons in conditionals - executable code needs event triggers.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T09.G4.06: Use boolean variables to track states
**Why T06 is needed:** Students use boolean variables in game logic - needs event triggers to respond to state changes.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T09.G4.07: Modify a variable based on sensor or random input
**Why T06 is needed:** Students use external inputs - interactive programs need event triggers.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

---

### T10 (Lists & Tables) - 6 skills need T06

#### T10.G4.01: Use nested loops to process a 2D arrangement
**Why T06 is needed:** Students implement nested loops - executable code needs event triggers to run.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T10.G4.02: Store and retrieve parallel list data
**Why T06 is needed:** Students work with parallel lists in programs - needs event triggers to execute list operations.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T10.G4.03: Build a high score or leaderboard list
**Why T06 is needed:** Students create interactive leaderboard systems - needs event triggers to update scores.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T10.G4.04: Sort a list by swapping items
**Why T06 is needed:** Students implement sorting algorithms - executable code needs event triggers.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T10.G4.05: Search a list for a specific item
**Why T06 is needed:** Students implement linear search - executable code needs event triggers.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T10.G4.06: Filter or remove items from a list
**Why T06 is needed:** Students loop through lists with conditionals - executable code needs event triggers.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

---

### T11 (Functions) - 2 skills need T06

#### T11.G4.01: Define and call a simple helper
**Why T06 is needed:** Students create and call custom blocks - needs event triggers to test the helper blocks.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T11.G4.03: Use a block's result in a calculation
**Why T06 is needed:** Students use reporter functions in working code - needs event triggers to execute.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

---

### T12 (Organizing Programs) - 2 skills need T06

#### T12.G4.02: Choose descriptive names for custom blocks
**Why T06 is needed:** Students create custom blocks - needs event triggers to build and test them.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T12.G4.03: Refactor repeated blocks into a custom block
**Why T06 is needed:** Students extract code into custom blocks - needs event triggers to build working scripts.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

---

### T13 (Testing/Debugging) - 2 skills need T06

#### T13.G4.03: Create an alternative solution
**Why T06 is needed:** Students build working programs with different approaches - needs event triggers.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T13.G4.05: Use systematic testing with multiple test cases
**Why T06 is needed:** Students test programs with different inputs - needs event triggers to run test cases.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

---

### T14 (2D Games) - 14 skills need T06

#### T14.G4.01: Spawn a projectile
**Why T06 is needed:** Students create projectiles triggered by user input - needs key-press event handling.
**Add dependency:**
```
* T06.G3.02: Build a key-press script that controls a sprite
```

#### T14.G4.02: Move a projectile
**Why T06 is needed:** Projectile clones need "when I start as a clone" events to move - requires event understanding.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.03: Clean up projectiles
**Why T06 is needed:** Projectiles need event-driven cleanup logic - requires event handling.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.04: Simple enemy movement
**Why T06 is needed:** Enemy behaviors run continuously using forever loops - needs event triggers.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.05: Chase the player
**Why T06 is needed:** Enemy AI needs continuous event-driven behavior - requires event handling.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.06: Create a Score variable
**Why T06 is needed:** Score updates happen in response to game events - needs event handling.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.07: Create a Lives variable
**Why T06 is needed:** Lives decrease on collision events and trigger game over - needs event handling.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.08: Create a Timer
**Why T06 is needed:** Timer runs continuously using loops and checks conditions - needs event triggers.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.09: Detect level complete
**Why T06 is needed:** Level completion checks run continuously and trigger next level - needs event handling.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.10: Switch backdrops for levels
**Why T06 is needed:** Level switching responds to broadcast messages - needs event handling (when I receive).
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.11: Add checkpoints
**Why T06 is needed:** Checkpoints store and restore player state on events - needs event handling.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.12: Temporary power-ups
**Why T06 is needed:** Power-ups toggle states and use timers - event-driven behavior needs event handling.
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.13: Pause and resume the game
**Why T06 is needed:** Pause functionality uses broadcast messages - needs event handling (when I receive).
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

#### T14.G4.14: Reset on restart messages
**Why T06 is needed:** Reset uses broadcast messages to coordinate sprites - needs event handling (when I receive).
**Add dependency:**
```
* T06.G3.01: Build a green-flag script that runs a 3-5 block sequence
```

---

## LIST B: Skills That DON'T Need T06 (17 Skills)

These skills focus on analyzing, tracing, debugging, or understanding existing code rather than writing new executable programs. They don't require students to know how to trigger scripts.

### T07 (Loops) - 2 skills

- **T07.G4.05:** Analyze and fix a loop bug - Students read and debug existing code
- **T07.G4.06:** Trace code that combines a loop and a condition - Students trace existing code

### T08 (Conditions & Logic) - 3 skills

- **T08.G4.03:** Trace code with compound conditionals - Students trace existing code
- **T08.G4.07:** Analyze and fix a logic bug - Students debug existing code
- **T08.G4.08:** Trace code with a sequence of if/else blocks - Students trace existing code

### T09 (Variables) - 1 skill

- **T09.G4.08:** Debug incorrect variable updates in code - Students debug existing code

### T11 (Functions) - 3 skills

- **T11.G4.02:** Distinguish action blocks from reporter functions - Conceptual understanding, not coding
- **T11.G4.04:** Describe what each helper does in a script - Students read and explain existing code
- **T11.G4.05:** Trace through a script with helpers and reporters - Students trace existing code

### T12 (Organizing Programs) - 2 skills

- **T12.G4.01:** Document a program with embedded comments - Adding comments to existing code
- **T12.G4.04:** Analyze and improve variable scope and naming - Code review of existing code

### T13 (Testing/Debugging) - 6 skills

- **T13.G4.01:** Debug a conditional inside a loop - Students debug existing code
- **T13.G4.02:** Test edge cases in a simple condition - Testing existing programs
- **T13.G4.04:** Identify and fix an infinite loop - Students debug existing code
- **T13.G4.06:** Compare two programs solving the same task - Students compare existing programs
- **T13.G4.07:** Debug a complex loop with nested structures - Students debug existing code
- **T13.G4.08:** Document the steps you took to find and fix a bug - Writing about debugging

---

## Implementation Summary

### Quick Reference by Topic

| Topic | Skills Needing T06 | Skill IDs |
|-------|-------------------|-----------|
| T07 (Loops) | 4 | T07.G4.01-04 |
| T08 (Conditions) | 5 | T08.G4.01-02, 04-06 |
| T09 (Variables) | 7 | T09.G4.01-07 |
| T10 (Lists) | 6 | T10.G4.01-06 |
| T11 (Functions) | 2 | T11.G4.01, 03 |
| T12 (Program Org) | 2 | T12.G4.02-03 |
| T13 (Testing) | 2 | T13.G4.03, 05 |
| T14 (Games) | 14 | T14.G4.01-14 |
| **TOTAL** | **42** | |

### Dependency Distribution

- **39 skills** should add `T06.G3.01` (Build a green-flag script)
- **3 skills** should add `T06.G3.02` (Build a key-press script):
  - T08.G4.06 (Use if to control state changes)
  - T09.G4.03 (Store and use user input)
  - T14.G4.01 (Spawn a projectile)

---

## Rationale for Decision Criteria

### Skills Requiring T06
Programming skills where students:
- **Build or create** new programs
- **Implement or use** programming constructs in executable code
- **Write scripts** that need event triggers to run
- Work with **interactive features** (user input, game controls)
- Create **continuous behaviors** (loops, timers, animations)

### Skills NOT Requiring T06
Analysis and comprehension skills where students:
- **Trace or read** existing code
- **Analyze or debug** provided programs
- **Compare or describe** code written by others
- Focus on **conceptual understanding** without writing executable code
- Add **documentation** to existing programs

---

## Recommendation

**Proceed with adding T06 dependencies to the 42 skills identified in List A.** This will ensure students have foundational event-handling knowledge before writing programs that require triggering scripts, which is essential for all coding tasks in block-based programming environments like Scratch.
