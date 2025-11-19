# T15 – Stories & Animation: K–8 Skill List (Draft v2)

Topic reference: `T15 Stories & Animation` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF, ALG‑HD (with links to PRO‑PM, ALG‑PS)

Each skill below has:

- a stable **ID** (`T15.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Stories and animation are introduced through visual sequences, character expressions, and simple narrative structures, using picture‑based, unplugged activities.

### T15.GK.01 – Sequence story pictures
- **Short name:** Put the story in order
- **Description:** Students arrange 3 picture panels to tell a simple story (e.g., Wake up -> Eat -> Play).
- **Challenge format:** Concept, drag‑and‑drop. Order 3 cards.
- **CSTA:** EK‑ALG‑HD‑02

### T15.GK.02 – Match emotions to faces

_Dependency:_
  * T03.GK.01: Identify parts that make up a whole

- **Short name:** How does the character feel?
- **Description:** Students identify the emotion of a character based on their facial expression or pose (Happy, Sad, Surprised).
- **Challenge format:** Concept, matching. Match "Happy" word/icon to the smiling character.
- **CSTA:** EK‑PRO‑PF‑01

### T15.GK.03 – Identify speech bubbles

_Dependency:_
  * T01.GK.03: Find the first and last pictures

- **Short name:** Who is talking?
- **Description:** Students look at a picture with characters and speech bubbles and identify who is speaking or what they are saying.
- **Challenge format:** Concept, hotspot. "Click on the character who is saying 'Hello'."
- **CSTA:** EK‑PRO‑PF‑02

---

## Grade 1

Grade 1 focuses on the components of a story: characters, settings, and dialogue, using pictures and logic puzzles.

### T15.G1.01 – Match setting to story

_Dependency:_
  * T03.GK.02: Match parts to whole objects

- **Short name:** Pick the right background
- **Description:** Given a story prompt (e.g., "The fish swims"), students choose the appropriate background (Ocean vs. Space).
- **Challenge format:** Concept, multiple choice. "Where does this story happen?"
- **CSTA:** 1A‑AP‑08

### T15.G1.02 – Order dialogue

_Dependency:_
  * T01.GK.02: Put pictures in order for coming to class

- **Short name:** Who speaks first?
- **Description:** Students see a comic strip with empty speech bubbles or jumbled order and determine the logical flow of conversation.
- **Challenge format:** Concept, sequencing. Order the lines: "Hello" -> "Hi, how are you?" -> "I am good."
- **CSTA:** 1A‑AP‑08

### T15.G1.03 – Action and consequence

_Dependency:_
  * T01.GK.02: Put pictures in order for coming to class

- **Short name:** What happens next?
- **Description:** Students predict the next frame in a simple animation sequence (e.g., Ball drops -> ? -> Ball hits ground).
- **Challenge format:** Concept, prediction. Select the image that completes the animation.
- **CSTA:** 1A‑AP‑08

---

## Grade 2

Grade 2 explores pacing, timing, and scene changes conceptually, preparing for coding these elements.

### T15.G2.01 – Fast vs. Slow animation

_Dependency:_
  * T01.G1.01: Put pictures in order to plant a seed

- **Short name:** Fast or slow?
- **Description:** Students compare two animation sequences (represented by frame strips) and identify which one represents a faster or slower action based on the gap between positions.
- **Challenge format:** Concept, comparison. "Which ball is moving faster?"
- **CSTA:** 1A‑AP‑08

### T15.G2.02 – Identify scene transitions

_Dependency:_
  * T01.G1.10: Match pictures to "if/then" rules
  * T01.G1.04: Predict the next step in a story sequence

- **Short name:** When does the scene change?
- **Description:** In a story sequence, students identify the point where the location changes (e.g., from House to School).
- **Challenge format:** Concept, hotspot. "Click the picture where the scene changes."
- **CSTA:** 1A‑AP‑10

### T15.G2.03 – Loop patterns in animation

_Dependency:_
  * T01.G1.07: Decide if two algorithms finish with the same result

- **Short name:** Find the repeating action
- **Description:** Students identify the repeating part of an animation (e.g., Left foot, Right foot, Left foot, Right foot).
- **Challenge format:** Concept, pattern recognition. "Which part of the dance repeats?"
- **CSTA:** 1A‑AP‑10

---

## Grade 3

Grade 3 is the **gateway to coding** for stories. Students use code to control characters, create dialogue, and build simple animations.

### Strand A: Basic Animation

#### T15.G3.01 – Switch costume

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T01.G3.01: Complete a simple script with missing blocks
  * T15.G2.01: Fast vs. Slow animation

- **Short name:** Change how it looks
- **Description:** Use `switch costume to [Costume B]` to change a sprite’s appearance.
- **Challenge format:** Build. `when clicked` -> `switch costume to [Happy]`.
- **CSTA:** 1B‑AP‑10

#### T15.G3.02 – Simple animation loop

_Dependency:_
  * T15.G3.01: Switch costume
  * T07.G3.01: Use a counted repeat loop
  * T01.G3.05: Replace repeated blocks with a repeat loop

- **Short name:** Make it move
- **Description:** Use `next costume` inside a `repeat` loop to create a simple animation cycle.
- **Challenge format:** Build. `repeat (10)` -> `next costume`, `wait (0.1) secs`.
- **CSTA:** 1B‑AP‑10

#### T15.G3.03 – Reset appearance

_Dependency:_
  * T15.G3.02: Simple animation loop
  * T08.G3.01: Use a simple if in a script
  * T01.G3.10: Trace a script with a single if/then

- **Short name:** Start fresh
- **Description:** Ensure the sprite starts with the correct costume and position when the green flag is clicked.
- **Challenge format:** Debug/Modify. "The character stays sad when I restart. Fix it."
- **CSTA:** 1B‑AP‑10

### Strand B: Dialogue

#### T15.G3.04 – Say something

_Dependency:_
  * T15.G3.03: Reset appearance
  * T09.G3.01: Create and use a numeric variable for score or count
  * T14.G3.03: Keep sprite on screen
  * T07.G3.02: Trace a script with a simple loop

- **Short name:** Speech bubble
- **Description:** Use the `say [Hello] for (2) seconds` block to display text.
- **Challenge format:** Build. `say [Welcome!] for (2) secs`.
- **CSTA:** 1B‑AP‑10

#### T15.G3.05 – Think bubble

_Dependency:_
  * T15.G3.04: Say something
  * T08.G3.02: Decide when a single if is enough
  * T07.G3.03: Build a forever loop for simple animation

- **Short name:** Thought bubble
- **Description:** Use the `think [Hmm...]` block to show internal monologue.
- **Challenge format:** Modify. Change `say` to `think`.
- **CSTA:** 1B‑AP‑10

### Strand C: Sequencing & Timing

#### T15.G3.06 – Sequence dialogue

_Dependency:_
  * T15.G3.05: Think bubble
  * T09.G3.02: Use a variable in a conditional (if block)
  * T10.G3.01: Loop through and process each item in a list

- **Short name:** Talk in order
- **Description:** Stack multiple `say` blocks to create a monologue.
- **Challenge format:** Build. `say [Hi]`, `say [I am a cat]`.
- **CSTA:** 1B‑AP‑10

#### T15.G3.07 – Wait between actions

_Dependency:_
  * T15.G3.06: Sequence dialogue
  * T11.G3.01: Understand when to use custom blocks vs loops
  * T12.G3.01: Write a comment explaining a complex block

- **Short name:** Pause for effect
- **Description:** Use `wait (1) seconds` to create a pause between an action and a line of dialogue.
- **Challenge format:** Build. `move (10)`, `wait (1)`, `say [Made it!]`.
- **CSTA:** 1B‑AP‑10

### Strand D: Interactive Events

#### T15.G3.08 – Click to talk

_Dependency:_
  * T15.G3.07: Wait between actions
  * T14.G3.05: Detect touching a hazard
  * T09.G3.03: Debug missing or wrong variable updates

- **Short name:** Talk when clicked
- **Description:** Trigger a speech script using `when this sprite clicked`.
- **Challenge format:** Build. `when this sprite clicked` -> `say [You poked me!]`.
- **CSTA:** 1B‑AP‑10

#### T15.G3.09 – Key press animation

_Dependency:_
  * T15.G3.08: Click to talk
  * T11.G3.02: Use a pre‑made helper block with parameters
  * T08.G3.04: Trace code with a single if/else

- **Short name:** Press space to jump
- **Description:** Trigger a costume change or motion using `when [space] key pressed`.
- **Challenge format:** Build. `when [space] key pressed` -> `switch costume to [Jump]`.
- **CSTA:** 1B‑AP‑10

---

## Grade 4

Grade 4 expands into **narrative structure and state**. Students manage scenes, coordinate multiple characters, and create interactive stories.

### Strand A: Advanced Animation

#### T15.G4.01 – Animate with effects

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T15.GK.03: Identify speech bubbles

- **Short name:** Fade or grow
- **Description:** Use `change [ghost] effect` or `change size` to animate appearance (e.g., fading out, growing).
- **Challenge format:** Build. `repeat (10)` -> `change [ghost] effect by (10)`.
- **CSTA:** 1B‑AP‑10

#### T15.G4.02 – Costume number logic

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T15.GK.03: Identify speech bubbles

- **Short name:** Costume by number
- **Description:** Use costume numbers to switch costumes (e.g., `switch costume to (1)`), useful for ordered frames.
- **Challenge format:** Modify. Switch from costume name to number.
- **CSTA:** 1B‑AP‑10

### Strand B: Scene Management

#### T15.G4.03 – Switch backdrop

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T15.GK.03: Identify speech bubbles

- **Short name:** Change the scene
- **Description:** Use `switch backdrop to [Next Scene]` to change the setting.
- **Challenge format:** Build. `say [Let's go outside]`, `switch backdrop to [Outdoors]`.
- **CSTA:** 1B‑AP‑10

#### T15.G4.04 – Hide and Show characters

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T15.GK.03: Identify speech bubbles

- **Short name:** Enter and exit
- **Description:** Use `hide` and `show` to control which characters appear in which scene.
- **Challenge format:** Build. `when backdrop switches to [Scene 2]` -> `show`.
- **CSTA:** 1B‑AP‑10

### Strand C: Interactive Stories

#### T15.G4.05 – Ask and Answer

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T15.GK.03: Identify speech bubbles

- **Short name:** Ask the player
- **Description:** Use `ask [What is your name?] and wait` and use the `answer` block in a response.
- **Challenge format:** Build. `ask [Name?]`, `say (join [Hello ] (answer))`.
- **CSTA:** 1B‑AP‑10

#### T15.G4.06 – Simple branching (Yes/No)

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T15.GK.03: Identify speech bubbles

- **Short name:** Yes or No choice
- **Description:** Use `if <(answer) = [yes]>` to give different responses.
- **Challenge format:** Build. `if <(answer) = [yes]>` -> `say [Great!]` else `say [Oh no.]`.
- **CSTA:** 1B‑AP‑10

### Strand D: Coordination

#### T15.G4.07 – Coordinate two sprites (Wait)

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T15.GK.03: Identify speech bubbles

- **Short name:** Wait for your turn
- **Description:** Coordinate a conversation between two sprites using `wait` blocks (Sprite A speaks for 2s, Sprite B waits 2s then speaks).
- **Challenge format:** Debug. "They talk over each other. Fix the timing."
- **CSTA:** 1B‑AP‑10

#### T15.G4.08 – Parallel actions

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T15.GK.02: Match emotions to faces

- **Short name:** Walk and talk
- **Description:** Use two `when green flag clicked` scripts to make a sprite walk and talk at the same time.
- **Challenge format:** Build. Script 1: `glide...`, Script 2: `say...`.
- **CSTA:** 1B‑AP‑10

---

## Grade 5

Grade 5 introduces **complex narrative systems**. Students use broadcasts for events, variables for story state, and advanced effects.

### Strand A: Broadcasting for Stories

#### T15.G5.01 – Broadcast scene change

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Signal next scene
- **Description:** Use `broadcast [Scene 2]` to trigger backdrop changes and sprite entrances/exits simultaneously.
- **Challenge format:** Build. `broadcast [Start Scene 2]`.
- **CSTA:** 1B‑AP‑15

#### T15.G5.02 – Broadcast specific actions

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T15.GK.02: Match emotions to faces

- **Short name:** Signal an action
- **Description:** Use broadcasts to trigger specific animations (e.g., `broadcast [Dance]`) so multiple sprites dance at once.
- **Challenge format:** Build. `when I receive [Dance]` -> `repeat (10)...`.
- **CSTA:** 1B‑AP‑15

### Strand B: Camera & Polish

#### T15.G5.03 – Simulated Camera Pan

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Pan the camera
- **Description:** Move all sprites in the opposite direction to simulate a camera panning.
- **Challenge format:** Build. `change x by (-10)` (on all world sprites).
- **CSTA:** 1B‑AP‑10

#### T15.G5.04 – Layering logic

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Go to front/back
- **Description:** Use `go to front layer` or `go backward (1) layers` to manage depth in a scene.
- **Challenge format:** Debug. "The tree is in front of the character. Fix it."
- **CSTA:** 1B‑AP‑10

### Strand C: Advanced Text

#### T15.G5.05 – Join text strings

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Combine words
- **Description:** Use `join [Hello ] [World]` to construct dynamic sentences.
- **Challenge format:** Build. `say (join [Score: ] (Score))`.
- **CSTA:** 1B‑AP‑10

#### T15.G5.06 – Text effects (Typewriter)

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Typewriter text
- **Description:** (Conceptual/Simple) Reveal text letter by letter or use a custom block to simulate typing.
- **Challenge format:** Build/Parsons. Loop through string length (advanced) or use a provided custom block.
- **CSTA:** 1B‑AP‑10

### Strand D: Branching & State

#### T15.G5.07 – Track story choices

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Remember choices
- **Description:** Use a variable `(Trust)` to track player decisions (+1 for nice, -1 for mean).
- **Challenge format:** Build. `change [Trust] by (1)`.
- **CSTA:** 1B‑AP‑09

#### T15.G5.08 – Conditional endings

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T08.G3.01: Use a simple if in a script
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Different endings
- **Description:** Check variables at the end of the story to show different backdrops/messages.
- **Challenge format:** Build. `if <(Trust) > (5)>` -> `switch backdrop to [Good End]`.
- **CSTA:** 1B‑AP‑10

---

## Grade 6–8 (Middle School)

Middle school focuses on **narrative architecture, efficiency, and user experience**.

### Grade 6: Narrative Systems

#### T15.G6.01 – State Machine for Animation

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.01: Use a counted repeat loop
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count

- **Short name:** Animation states
- **Description:** Use a `State` variable (Idle, Walk, Talk) to control which animation loop plays.
- **Challenge format:** Refactor. Organize loose scripts into a state machine.
- **CSTA:** 2‑AP‑10

#### T15.G6.02 – List-based Dialogue

_Dependency:_
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T15.GK.02: Match emotions to faces

- **Short name:** Dialogue from a list
- **Description:** Store dialogue lines in a list and iterate through them, rather than using hardcoded `say` blocks.
- **Challenge format:** Build. `say (item (i) of [Dialogue])`.
- **CSTA:** 2‑AP‑10

### Grade 7: Advanced Techniques

#### T15.G7.01 – Scene Graph / Manager

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T15.GK.03: Identify speech bubbles

- **Short name:** Scene manager
- **Description:** Create a dedicated "Manager" sprite that handles all broadcasts and global state changes (Scene 1 -> Scene 2).
- **Challenge format:** Build. Centralize logic in one sprite.
- **CSTA:** 2‑AP‑13

#### T15.G7.02 – Lip Sync Logic

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T15.GK.03: Identify speech bubbles

- **Short name:** Auto-lip sync
- **Description:** Map sound volume to costume changes (mouth open/closed) for automatic lip sync.
- **Challenge format:** Build. `switch costume to (round (loudness / 10))`.
- **CSTA:** 2‑AP‑13

### Grade 8: Engine Design

#### T15.G8.01 – Branching Narrative Engine

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T15.GK.02: Match emotions to faces

- **Short name:** Story engine
- **Description:** Build a system that reads a data structure (JSON-like or list of lists) to determine the next node in a branching story.
- **Challenge format:** Build. Parse a "Node ID" and "Next Node" structure.
- **CSTA:** 2‑AP‑14

#### T15.G8.02 – Accessibility in Media

_Dependency:_
  * T06.G3.01: Build a green‑flag script that runs a 3–5 block sequence
  * T06.G3.08: Fix a behavior that runs at the wrong time
  * T07.G3.05: Fix a loop that runs too many or too few times
  * T09.G3.01: Create and use a numeric variable for score or count
  * T15.GK.02: Match emotions to faces

- **Short name:** Accessible story
- **Description:** Implement features like text-to-speech (for blind users) or subtitles (for sound) to make stories accessible.
- **Challenge format:** Modify. Add TTS blocks to existing text.
- **CSTA:** 2‑AP‑14
