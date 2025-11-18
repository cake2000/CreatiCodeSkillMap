# CreatiCode Block Coverage Matrix

## Visual Gap Analysis: What's Taught vs. What's Missing

---

## MOTION BLOCKS

| Block | Exists? | Where Taught | Grade | Notes |
|-------|---------|--------------|-------|-------|
| Move [n] steps | ✅ | T01.G3.01 | 3 | "move 10 steps" |
| Turn [n] degrees | ✅ | T01.G3.01 | 3 | "turn 90 degrees" |
| Point in direction | ❌ | - | - | **GAP** |
| Point towards | ❌ | - | - | **GAP** |
| Go to x/y | ❌ | - | - | **GAP** |
| Go to sprite/mouse | ❌ | - | - | **GAP** |
| Glide to x/y | ❌ | - | - | **GAP** |
| Change x by | ❌ | - | - | **GAP** |
| Set x to | ❌ | - | - | **GAP** |
| Change y by | ❌ | - | - | **GAP** |
| Set y to | ❌ | - | - | **GAP** |
| Bounce on edge | ❌ | - | - | **GAP** |
| Set rotation style | ❌ | - | - | **GAP** |

**Coverage: 2/13 (15%)**

---

## LOOKS BLOCKS

| Block | Exists? | Where Taught | Grade | Notes |
|-------|---------|--------------|-------|-------|
| Say [text] | ⚠️ | T01.G3.01 | 3 | "say 'Done!'" only mentioned |
| Think [text] | ❌ | - | - | **GAP** |
| Show | ❌ | - | - | **GAP** |
| Hide | ❌ | - | - | **GAP** |
| Switch costume | ❌ | - | - | **GAP** - Used in T15.G3.01 |
| Next costume | ❌ | - | - | **GAP** |
| Change size by | ❌ | - | - | **GAP** - Used in T20.G4.03 |
| Set size to | ❌ | - | - | **GAP** |
| Change color effect | ❌ | - | - | **GAP** - Used in T20.G4.03 |
| Set color effect | ❌ | - | - | **GAP** |
| Change ghost effect | ❌ | - | - | **GAP** |
| Set ghost effect | ❌ | - | - | **GAP** |
| Clear graphic effects | ❌ | - | - | **GAP** |
| Go to front/back | ❌ | - | - | **GAP** |
| Go forward/backward layers | ❌ | - | - | **GAP** |

**Coverage: 1/15 (7%)**

---

## SOUND BLOCKS

| Block | Exists? | Where Taught | Grade | Notes |
|-------|---------|--------------|-------|-------|
| Play sound until done | ❌ | - | - | **GAP** - Used in T15.G3.04 |
| Start sound | ❌ | - | - | **GAP** |
| Stop all sounds | ❌ | - | - | **GAP** |
| Change volume by | ❌ | - | - | **GAP** |
| Set volume to | ❌ | - | - | **GAP** |
| Change tempo by | ❌ | - | - | **GAP** |
| Set tempo to | ❌ | - | - | **GAP** |
| Play note/drum | ❌ | - | - | **GAP** |

**Coverage: 0/8 (0%)**

---

## EVENT BLOCKS

| Block | Exists? | Where Taught | Grade | Notes |
|-------|---------|--------------|-------|-------|
| When green flag clicked | ✅ | T06.G3.01, T01.G3.01 | 3 | Well covered |
| When key pressed | ✅ | T06.G3.01 | 3 | "different events" |
| When sprite clicked | ✅ | T06.G3.01 | 3 | "different events" |
| When backdrop switches | ⚠️ | T06.G3.01 | 3 | Implied in "events" |
| When loudness/timer | ⚠️ | T06.G4.01 | 4 | "timing events" |
| Broadcast | ✅ | T06.G3.02 | 3 | Explicitly taught |
| When I receive | ✅ | T06.G3.02 | 3 | With broadcasts |

**Coverage: 7/7 (100%)**

---

## CONTROL BLOCKS

| Block | Exists? | Where Taught | Grade | Notes |
|-------|---------|--------------|-------|-------|
| Wait [n] seconds | ✅ | T06.G4.01 | 4 | "timing events" |
| Repeat [n] | ✅ | T07.G3.01+ | 3-5 | Multiple skills |
| Forever | ✅ | T07.G3.02 | 3 | Explicitly taught |
| If / If-else | ✅ | T08.G3.01 | 3 | Explicitly taught |
| Wait until | ⚠️ | T07.G3.01 | 3 | Implied in repeat-until |
| Repeat until | ✅ | T07.G3.01 | 3 | Explicitly taught |
| Stop all/script/other | ❌ | - | - | **GAP** |
| Clone sprite | ❌ | - | - | **GAP** - Used in T14.G3.03 |
| Delete clone | ❌ | - | - | **GAP** |

**Coverage: 7/9 (78%)**

---

## SENSING BLOCKS

| Block | Exists? | Where Taught | Grade | Notes |
|-------|---------|--------------|-------|-------|
| Touching sprite/color | ⚠️ | T07.G3.01 | 3 | "touching goal" in repeat-until |
| Touching edge | ❌ | - | - | **GAP** |
| Color touching color | ❌ | - | - | **GAP** |
| Distance to | ❌ | - | - | **GAP** |
| Ask and wait | ⚠️ | T09.G4.01 | 4 | "user input" likely uses this |
| Answer | ⚠️ | T09.G4.01 | 4 | Goes with "ask" |
| Key pressed? | ❌ | - | - | **GAP** |
| Mouse down? | ❌ | - | - | **GAP** |
| Mouse x/y | ❌ | - | - | **GAP** |
| Loudness | ❌ | - | - | **GAP** |
| Timer | ⚠️ | T06.G4.01 | 4 | "timer blocks" |
| Reset timer | ⚠️ | T06.G4.01 | 4 | "timer blocks" |
| X/Y position of sprite | ❌ | - | - | **GAP** |

**Coverage: 3/13 (23%)**

---

## OPERATORS

| Block | Exists? | Where Taught | Grade | Notes |
|-------|---------|--------------|-------|-------|
| + - * / | ✅ | T09.G3.03 | 3 | "multiplication and division" |
| Pick random | ⚠️ | T20.G3.03 | 3 | "Use randomness" |
| < > = | ✅ | T09.G4.03 | 4 | "comparison operators" |
| And / Or / Not | ✅ | T08.G3.02-03, G5.04 | 3-5 | Explicitly taught |
| Join (concatenate) | ✅ | T09.G5.02 | 5 | "string concatenation" |
| Letter of | ✅ | T29.G3.01 | 3 | "first letter of word" |
| Length of | ⚠️ | T29.G3.02 | 3 | Implied in "substring" |
| Contains | ✅ | T29.G3.02 | 3 | "contains substring" |
| Mod | ✅ | T09.G5.03 | 5 | Explicitly taught |
| Round | ❌ | - | - | **GAP** |
| Math function (abs, sqrt, etc) | ❌ | - | - | **GAP** |

**Coverage: 8/11 (73%)**

---

## VARIABLES

| Block | Exists? | Where Taught | Grade | Notes |
|-------|---------|--------------|-------|-------|
| Set variable to | ✅ | T09.G3.01 | 3 | Explicitly taught |
| Change variable by | ✅ | T09.G3.01 | 3 | Explicitly taught |
| Show/hide variable | ⚠️ | T16.G3.02 | 3 | "label to display info" |

**Coverage: 3/3 (100%)**

---

## LISTS

| Block | Exists? | Where Taught | Grade | Notes |
|-------|---------|--------------|-------|-------|
| Add item to list | ✅ | T10.G3.01 | 3 | Implied in "loop through" |
| Delete item from list | ✅ | T10.G4.04 | 4 | "remove items" |
| Insert at position | ⚠️ | T10.G5.03 | 5 | "insert rows in table" |
| Replace item | ✅ | T10.G3.03 | 3 | "sort by swapping" |
| Item # of list | ✅ | T10.G3.01 | 3 | "process each item" |
| Length of list | ⚠️ | T10.G3.02 | 3 | Implied in "count items" |
| Contains item | ✅ | T10.G3.04 | 3 | "search for item" |
| Show/hide list | ❌ | - | - | **GAP** |

**Coverage: 7/8 (88%)**

---

## PEN BLOCKS

| Block | Exists? | Where Taught | Grade | Notes |
|-------|---------|--------------|-------|-------|
| Clear | ❌ | - | - | **GAP** - Used in T20 |
| Stamp | ⚠️ | T20.G3.02 | 3 | "stamp placement" |
| Pen down | ❌ | - | - | **GAP** - Used in T20 |
| Pen up | ❌ | - | - | **GAP** |
| Set pen color | ❌ | - | - | **GAP** |
| Change pen color | ❌ | - | - | **GAP** |
| Set pen size | ❌ | - | - | **GAP** |
| Change pen size | ❌ | - | - | **GAP** |

**Coverage: 1/8 (13%)**

---

## CUSTOM BLOCKS (MY BLOCKS)

| Capability | Exists? | Where Taught | Grade | Notes |
|------------|---------|--------------|-------|-------|
| Make a block | ✅ | T11.G3.02 | 3 | Explicitly taught |
| Add input (parameter) | ✅ | T11.G3.02 | 3 | "multiple parameters" |
| Add label (text) | ⚠️ | T11.G3.02 | 3 | Implied |
| Run without screen refresh | ❌ | - | - | **GAP** - Advanced |

**Coverage: 3/4 (75%)**

---

## OVERALL COVERAGE SUMMARY

| Category | Covered | Total | % | Status |
|----------|---------|-------|---|--------|
| **Motion** | 2 | 13 | 15% | 🔴 Critical Gap |
| **Looks** | 1 | 15 | 7% | 🔴 Critical Gap |
| **Sound** | 0 | 8 | 0% | 🔴 Critical Gap |
| **Events** | 7 | 7 | 100% | 🟢 Complete |
| **Control** | 7 | 9 | 78% | 🟡 Good |
| **Sensing** | 3 | 13 | 23% | 🔴 Critical Gap |
| **Operators** | 8 | 11 | 73% | 🟡 Good |
| **Variables** | 3 | 3 | 100% | 🟢 Complete |
| **Lists** | 7 | 8 | 88% | 🟢 Excellent |
| **Pen** | 1 | 8 | 13% | 🔴 Critical Gap |
| **Custom Blocks** | 3 | 4 | 75% | 🟡 Good |

**TOTAL BLOCK COVERAGE: 42/99 (42%)**

---

## CRITICAL GAPS TO FILL

### Priority 1: Motion (11 missing blocks)
Most commonly used category for beginners. Only "move" and "turn" are taught.

**Missing:**
- Glide, Go to, Point in direction, X/Y manipulation, Bounce on edge

**Impact:** Students can't create smooth animations or precise positioning.

---

### Priority 2: Looks (14 missing blocks)
Second most common category. Only "say" is mentioned once.

**Missing:**
- Costumes, Size, Show/Hide, Effects, Layers

**Impact:** Students can't create visual variety or animation.

---

### Priority 3: Sensing (10 missing blocks)
Critical for interactivity. Only "touching" is taught via repeat-until.

**Missing:**
- Key detection, Mouse position/click, Distance, Color sensing

**Impact:** Students can't build truly interactive programs.

---

### Priority 4: Sound (8 missing blocks)
Completely untaught at foundational level.

**Missing:**
- All sound blocks (play, volume, tempo, notes)

**Impact:** Students can't add audio to projects without trial-and-error.

---

### Priority 5: Pen (7 missing blocks)
Used in creative coding (T20) but never taught.

**Missing:**
- Pen up/down, Clear, Color/Size controls

**Impact:** Students in T20 (Algorithmic Art) don't know how to use pen blocks.

---

## RECOMMENDED NEW SKILLS

### Grade 2 (Introduce Blocks)

**T37.G2.01: Move Your Sprite**
- Teach: move [n] steps, turn [n] degrees
- Activity: Move sprite in a square pattern

**T37.G2.02: Sprite Speech Bubbles**
- Teach: say [text], think [text]
- Activity: Create a conversation between sprites

**T37.G2.03: Play a Sound**
- Teach: play sound [name] until done
- Activity: Add sound effects to actions

**T37.G2.04: Change How Your Sprite Looks**
- Teach: switch costume, next costume
- Activity: Animate a character walking

**T37.G2.05: Show and Hide**
- Teach: show, hide
- Activity: Make sprite appear/disappear on click

**T37.G2.06: Make Sprites Bigger and Smaller**
- Teach: set size to [%], change size by [%]
- Activity: Growing/shrinking animation

**T37.G2.07: Detect Clicks and Keys**
- Teach: when [sprite] clicked, when [key] pressed
- Activity: Interactive control practice

**T37.G2.08: Touch and Detect**
- Teach: touching [sprite/color]?, touching edge?
- Activity: Simple collision detection

---

### Grade 3 (Expand Blocks)

**T37.G3.01: Smooth Gliding Motion**
- Teach: glide [n] secs to x: [x] y: [y]
- Activity: Create smooth sprite paths

**T37.G3.02: Go To Positions**
- Teach: go to [sprite/mouse/x:y], go to random position
- Activity: Teleporting sprite game

**T37.G3.03: Point and Rotate**
- Teach: point in direction [degrees], point towards [sprite/mouse]
- Activity: Sprite follows mouse smoothly

**T37.G3.04: Control Position with Numbers**
- Teach: change x by [n], set x to [n], change y by [n], set y to [n]
- Activity: Precise sprite movement

**T37.G3.05: Graphic Effects**
- Teach: set/change [color/ghost/brightness] effect
- Activity: Fading and color-shifting animations

**T37.G3.06: Sound Volume and Speed**
- Teach: set/change volume, set/change tempo
- Activity: Dynamic audio control

**T37.G3.07: Ask Questions**
- Teach: ask [question] and wait, answer
- Activity: Interactive quiz or name input

**T37.G3.08: Measure Distance**
- Teach: distance to [sprite/mouse]
- Activity: Proximity-based interactions

**T37.G3.09: Drawing with the Pen**
- Teach: pen down, pen up, clear, set pen color/size
- Activity: Simple drawing program

**T37.G3.10: Random Numbers and Math**
- Teach: pick random [min] to [max], round, abs
- Activity: Random sprite placement and movement

---

## INTEGRATION INTO EXISTING CURRICULUM

### Current Dependency Chain (BROKEN):
```
T01.G3.01 (teaches "move, turn, say")
  ↓
T14.G3.01 (expects full Motion/Looks/Sound knowledge)
```

### Fixed Dependency Chain:
```
T37.G2.01-08 (Grade 2 block basics)
  ↓
T01.G3.01 (first algorithm using blocks)
  ↓
T37.G3.01-10 (Grade 3 block expansion)
  ↓
T14.G3.01+ (project-based learning assumes all blocks)
```

---

## FILES IN THIS VERIFICATION

1. **EXISTING_FOUNDATION_VERIFICATION.md** - Detailed 8,000-word analysis
2. **FOUNDATION_SKILLS_BY_CATEGORY.md** - Skills grouped by topic with IDs
3. **VERIFICATION_QUICK_SUMMARY.md** - Executive summary
4. **BLOCK_COVERAGE_MATRIX.md** - This visual gap analysis

---

**Analysis Complete:** 2025-11-17  
**Block Coverage:** 42/99 blocks (42%)  
**Critical Gaps:** 57 blocks need foundational skills  
**Recommended New Skills:** 18-20 for Grades 2-3
