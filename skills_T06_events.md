# T06 – Events & Sequencing in Programs: K–8 Skill List (Draft v1)

Topic reference: `T06 Events & Sequencing in Programs` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PF (with links to ALG‑AF, PRO‑PD)

Each skill below has:

- a stable **ID** (`T06.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Events are introduced through concrete, physical actions: clicking a button, pressing a key, or waiting for something to happen. Sequencing is about ordering simple actions in time.

### T06.GK.01 – Recognize what starts a program

- **Short name:** Spot the green flag button
- **Description:** Students identify that programs in CreatiCode start with a specific trigger, like clicking the green flag, and understand that this is how you "run" a project. They recognize the green flag as a clear start signal.
- **Challenge format:** Concept, interactive. A CreatiCode project interface is shown; students click on or point to the green flag button to indicate what starts the program. Auto‑grading confirms correct identification.
- **CSTA:** EK‑PRO‑PF‑01, EK‑ALG‑AF‑01.

### T06.GK.02 – Order actions in a simple sequence

- **Short name:** Put actions in order
- **Description:** Students arrange or recognize the correct order of simple sprite actions (e.g., move, say, jump) to match a given story or direction. They understand that order matters: doing something "first, then, then."
- **Challenge format:** Concept, drag‑and‑drop. Show 3–4 action tiles (pictures or words) out of order. Students drag them into the sequence that matches a simple storyboard or verbal direction (e.g., "The cat says hello, then jumps, then walks away"). Auto‑grading checks the final order.
- **CSTA:** EK‑PRO‑PF‑01.

### T06.GK.03 – Match a simple script to a sequence

- **Short name:** Match code to a picture story
- **Description:** Students connect a short block script (e.g., green flag, move, say, wait) to a matching 3-frame story or animation, building the concept that code produces behavior in order.
- **Challenge format:** Concept, multiple choice. Show a picture story (three panels with a sprite moving and speaking) and two or three short code scripts. Students select the script that creates the shown behavior.
- **CSTA:** EK‑PRO‑PF‑01, EK‑ALG‑AF‑01.

### T06.GK.04 – Predict what happens when you click green flag

- **Short name:** What happens when you click go?
- **Description:** Given a short CreatiCode script, students predict the visual outcome (sprite moves, changes, speaks) that occurs when the program runs. This builds mental models of code execution.
- **Challenge format:** Concept, multiple choice or interactive trace. Students view a script and a set of possible outcomes (picture tiles or sprite positions); they select what will happen. Auto‑grading compares to simulation.
- **CSTA:** EK‑PRO‑PF‑01.

---

## Grade 1

Grade 1 focuses on creating and tracing simple sequences with green-flag events, introducing the idea that scripts are ordered lists of actions.

### T06.G1.01 – Build a simple sequence with green flag

- **Short name:** Build a short script with green flag
- **Description:** Students create a short script triggered by the green flag (e.g., move 10 steps, say "Hi", wait 1 sec, move 10 steps again) and observe the sprite's behavior, connecting code blocks to actions.
- **Challenge format:** Coding, starter project. Provided: a sprite and the green-flag event block. Prompt: "Make the cat move forward, say hello, and wait 2 seconds." Students add movement and speech blocks in order. Auto‑grading checks (1) green flag is present, (2) blocks are in sequence, and (3) behavior matches when the flag is clicked.
- **CSTA:** E1‑PRO‑PF‑01.

### T06.G1.02 – Trace a script and predict the output

- **Short name:** Trace code to find the result
- **Description:** Students read a short script (2–4 blocks) starting with green flag and predict the sequence of actions, or select which picture shows the final result after the script runs.
- **Challenge format:** Concept, code‑reading item. Show a script with say, move, and turn blocks. Ask "In what order do these happen?" or show multiple final states and have students choose the correct one. Auto‑grading uses simulation or manual key checks.
- **CSTA:** E1‑PRO‑PF‑01, E1‑ALG‑AF‑01.

### T06.G1.03 – Identify the sequence in a given script

- **Short name:** Find the order of blocks
- **Description:** Students are shown a complete script and asked to identify or number the order in which blocks execute, reinforcing the idea that execution is top‑to‑bottom and sequential.
- **Challenge format:** Concept, multiple choice or matching. A script is displayed; students answer "Which block runs first?" or number the blocks 1, 2, 3. Auto‑grading checks selections against expected order.
- **CSTA:** E1‑PRO‑PF‑01.

### T06.G1.04 – Insert a block into an existing sequence

- **Short name:** Add a block to a script
- **Description:** Students are given a starter script (e.g., move, say, wait) and add one missing block to complete a behavior (e.g., insert a turn block between move and say to make the cat turn before speaking). This reinforces sequencing and editing.
- **Challenge format:** Coding, guided construction. Starter project has a script with one or two missing blocks represented as blanks or labeled placeholders. Prompt: "Insert a [jump] block after the cat says hello." Auto‑grading verifies the correct block is added in the correct position.
- **CSTA:** E1‑PRO‑PF‑01, E1‑PRO‑PM‑04.

---

## Grade 2

Grade 2 introduces awareness of events beyond green flag (key presses) and reinforces that multiple sequences can exist in one program.

### T06.G2.01 – Respond to a key event

- **Short name:** Make a sprite respond to a key
- **Description:** Students create a script with a `when [key] pressed` event block (e.g., when right arrow pressed, move right). They understand that this event is separate from green flag and runs when triggered by the key.
- **Challenge format:** Coding, starter project. Provided: a sprite and one or two event blocks (green flag and a key event) with partial scripts. Prompt: "When the right arrow is pressed, make the cat move right 10 steps." Students add a move block inside the key event. Auto‑grading checks that the event block is correct and the movement block is inside it.
- **CSTA:** E2‑PRO‑PF‑01.

### T06.G2.02 – Distinguish green flag from key events

- **Short name:** Know the difference between events
- **Description:** Students recognize that a green flag event runs when the program starts, while a key event only runs when that key is pressed. They understand these are different triggers for different scripts.
- **Challenge format:** Concept, multiple choice. Scenario: "The cat has a green flag script to say hello and a space key script to jump. What happens?" Options: (A) cat says hello and jumps on startup, (B) cat says hello on startup; jumps only when space is pressed, (C) nothing happens. Auto‑grading checks the answer and understanding of event timing.
- **CSTA:** E2‑PRO‑PF‑01.

### T06.G2.03 – Sequence actions in a key-triggered script

- **Short name:** Order actions in a key event
- **Description:** Students build or trace a script attached to a key event (e.g., when left arrow, turn left then move forward), ensuring actions are in the correct sequence within that event.
- **Challenge format:** Coding, drag‑and‑drop or starter project. Show a key event block and 3–4 action blocks; students order them correctly (or build from scratch in a starter). Prompt: "When the up arrow is pressed, the cat should turn to face up, then move forward." Auto‑grading checks block order within the event.
- **CSTA:** E2‑PRO‑PF‑01.

### T06.G2.04 – Match scripts to game controls

- **Short name:** Assign controls to sprite movements
- **Description:** Students create or match key event scripts for a simple game control scheme (e.g., left/right arrows for horizontal movement, up arrow for jump), associating each key with a meaningful action.
- **Challenge format:** Coding, scaffolded construction. Prompt: "Set up the keyboard controls so the player can move left, right, and jump." Provided: empty event blocks for each key and movement blocks. Students drag movement blocks into the correct events. Auto‑grading checks that all three controls are assigned and the correct blocks are in each event.
- **CSTA:** E2‑PRO‑PF‑01.

---

## Grade 3

Grade 3 extends event handling with multiple independent scripts and introduces simple broadcast (message) events, allowing scripts to trigger one another.

### T06.G3.01 – Create independent scripts with different events

- **Short name:** Multiple scripts in one project
- **Description:** Students build a program with two or more separate scripts (e.g., one green flag script and one or two key scripts) that work together, each responding to its own event without interfering with the others.
- **Challenge format:** Coding, starter project. Prompt: "Add a green flag script that makes the cat walk continuously. Also add a space key script that makes the cat jump while walking." Provided: sprite and empty event blocks. Auto‑grading checks (1) two scripts are present with correct events, (2) both run without conflict, and (3) behaviors are as expected.
- **CSTA:** E3‑PRO‑PF‑01.

### T06.G3.02 – Introduce broadcasts to sequence events

- **Short name:** Use broadcasts to trigger other scripts
- **Description:** Students use a `broadcast [message]` block in one script and a `when I receive [message]` block in another script to make scripts communicate. This enables one script to trigger another.
- **Challenge format:** Coding, guided construction. Prompt: "When the green flag is clicked, the cat moves to the center. When the cat reaches the center, send a 'start' message. Add another script that listens for 'start' and makes the cat dance." Starter includes partial broadcast blocks. Auto‑grading checks (1) broadcast is sent, (2) listener is correct, and (3) sequence of actions occurs as intended.
- **CSTA:** E3‑PRO‑PF‑01.

### T06.G3.03 – Understand event priority and concurrency

- **Short name:** Multiple events running at the same time
- **Description:** Students recognize that when a program runs, a green flag script, key scripts, and other event handlers can respond simultaneously or near-simultaneously, and that this can create interesting emergent behaviors.
- **Challenge format:** Concept, interactive exploration. Project: a sprite with a green flag script making it walk continuously and a key script making it jump. Students click the key while the sprite is walking and see that both happen together (concurrency). Prompt: "Can the cat jump and walk at the same time?" Auto‑grading assesses understanding through observation or multiple choice.
- **CSTA:** E3‑PRO‑PF‑01.

### T06.G3.04 – Debug event-handling code

- **Short name:** Find and fix event problems
- **Description:** Students examine a script where an event is not triggered correctly (e.g., wrong key, wrong event type, missing broadcast) and modify it to work as intended.
- **Challenge format:** Coding, debugging challenge. Starter project: a script with an error, e.g., the jump key doesn't work because it's in the green flag script instead of a key event. Prompt: "Fix this so jumping responds to the space key, not the green flag." Auto‑grading checks the corrected event structure and tests behavior.
- **CSTA:** E3‑PRO‑PF‑01, E3‑PRO‑TR‑03.

---

## Grade 4

Grade 4 deepens understanding of event-driven programs with more complex scenarios, timing events, and refactored designs.

### T06.G4.01 – Use timing events (wait and timer blocks)

- **Short name:** Sequence with delays and timing
- **Description:** Students use `wait` blocks and/or timer events to add delays between actions or to trigger scripts after a certain amount of time, introducing temporal control of events.
- **Challenge format:** Coding, starter project. Prompt: "Make the cat move, wait 2 seconds, then turn and move again. Also, set a timer so that every 5 seconds the cat changes color." Provided: sprite, wait and timer blocks. Auto‑grading checks correct timing in the sequence and behavior.
- **CSTA:** E4‑PRO‑PF‑01.

### T06.G4.02 – Refactor repeated event scripts into loops

- **Short name:** Use loops inside event handlers
- **Description:** Students recognize that a key event script might contain repeated actions and replace them with a loop (e.g., change "jump 3 times" from three separate jump blocks to one `repeat 3` loop inside a key event).
- **Challenge format:** Coding, refactor challenge. Starter project: a key event with three identical `jump` blocks. Prompt: "Refactor this so the jump repeats 3 times using a loop." Auto‑grading checks that a loop is present, count is correct, and behavior is unchanged.
- **CSTA:** E4‑PRO‑PF‑01, ALG‑AF.

### T06.G4.03 – Create event sequences with branching

- **Short name:** Events with conditional outcomes
- **Description:** Students add conditional logic inside event handlers (e.g., `when clicked, if score > 10 then win, else show try again`) so that events trigger different behaviors based on program state.
- **Challenge format:** Coding, starter project. Prompt: "When the space key is pressed, if the sprite is touching the goal, display 'You win!' Otherwise, say 'Keep trying.'" Provided: key event block and if/else blocks. Auto‑grading checks structure and tests both branches.
- **CSTA:** E4‑PRO‑PF‑01.

### T06.G4.04 – Analyze event flow in a multi-event program

- **Short name:** Trace event sequences in complex projects
- **Description:** Students read a program with multiple events and scripts and predict the order and outcomes of events, understanding which scripts run first, when broadcasts trigger other scripts, and how events interact.
- **Challenge format:** Concept, code‑reading item. Show a program with a green flag script, a key event, and two broadcast/receive pairs. Prompt: "If you click the green flag and then press a key, in what order do scripts run?" or "Which script runs after the 'go' broadcast is sent?" Auto‑grading checks answers using simulation or key phrases.
- **CSTA:** E4‑PRO‑PF‑01.

---

## Grade 5

Grade 5 emphasizes event handling in game and simulation contexts, with multiple simultaneous events and state management through events.

### T06.G5.01 – Design event-driven game flow

- **Short name:** Structure a game with events
- **Description:** Students organize a game using events to manage different game states: green flag for setup/start, key events for player controls, broadcasts for level changes or game over, building a coherent game loop through events.
- **Challenge format:** Coding, project design. Prompt: "Create a simple game where the green flag starts the game, arrow keys move the player, touching a coin triggers a 'score' broadcast, and collecting 5 coins sends an 'end' broadcast." Provided: starter with scenes/sprites. Auto‑grading checks event structure, state transitions, and win/lose conditions.
- **CSTA:** E5‑PRO‑PF‑01, PRO‑PD.

### T06.G5.02 – Coordinate multiple simultaneous events

- **Short name:** Many events happening together
- **Description:** Students build programs where several independent events (green flag, multiple key presses, broadcasts) are active at the same time, requiring careful design to avoid conflicts and unintended interference.
- **Challenge format:** Coding, simulation/game. Prompt: "The sprite walks continuously (green flag), can jump when space is pressed, can turn with arrow keys, and shows 'level up' when a broadcast arrives. Make sure all events work together smoothly." Auto‑grading checks that events don't interfere and all behaviors work.
- **CSTA:** E5‑PRO‑PF‑01.

### T06.G5.03 – Use broadcasts to decouple scripts

- **Short name:** Send and receive broadcasts
- **Description:** Students design programs where one script broadcasts an event (e.g., enemy hit) and multiple other scripts listen and respond (e.g., player loses health, score updates, sound plays), allowing modular, loosely-coupled behavior.
- **Challenge format:** Coding, starter project with multiple sprites/objects. Prompt: "When the player touches an enemy, send a 'hit' broadcast. Create separate scripts that respond by (1) reducing player health, (2) playing a sound, (3) moving the enemy away." Provided: sprites and empty scripts. Auto‑grading checks broadcast/receive structure and all three responses occur.
- **CSTA:** E5‑PRO‑PF‑01, PRO‑PD.

### T06.G5.04 – Sequence complex animations with events

- **Short name:** Choreograph animations with events
- **Description:** Students synchronize multiple sprite animations using green flag, broadcasts, and timing to create coordinated scenes (e.g., character walks on stage, broadcasts "start dance", multiple dancers begin choreographed movements together).
- **Challenge format:** Coding, creative/performance project. Prompt: "Create an animated scene where a main character enters, then sends a 'start' broadcast. Three background dancers receive this and perform a synchronized dance routine." Provided: multiple sprites, empty event/animation scripts. Auto‑grading checks broadcast/receive structure and approximate timing/synchronization.
- **CSTA:** E5‑PRO‑PF‑01.

---

## Grade 6

In middle school, event-driven programming becomes more abstract and integrated into algorithm design; students analyze and optimize event handling strategies.

### T06.G6.01 – Analyze event-driven control flow

- **Short name:** Trace event execution paths
- **Description:** Students analyze a multi-event program and describe the order in which scripts execute given various inputs (key presses, mouse clicks, broadcasts), constructing a mental model of event dispatch and execution order.
- **Challenge format:** Concept, code‑reading item. Show a program with multiple events, broadcasts, and conditional branches. Prompt: "List the order of scripts that run when [sequence of inputs occurs]" or "Which scripts run in parallel?" Auto‑grading checks answers using static analysis or simulation.
- **CSTA:** MS‑PRO‑PF‑01.

### T06.G6.02 – Refactor event handling for clarity

- **Short name:** Improve event script organization
- **Description:** Students review event-based code and restructure it (e.g., consolidate related key events, clarify broadcast purposes, add comments) to improve readability and maintainability without changing behavior.
- **Challenge format:** Coding, refactor challenge. Provided: a working but poorly organized program with scattered events and unclear broadcasts. Prompt: "Reorganize the scripts to group movement controls, then separate game logic and animation." Auto‑grading checks code structure, comments, and behavior equivalence.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PD.

### T06.G6.03 – Design custom events using broadcasts

- **Short name:** Create meaningful broadcast messages
- **Description:** Students name and design broadcasts that represent domain-specific events (e.g., "player-jumped", "goal-reached", "level-complete") rather than generic names, treating broadcasts as part of the program's communication protocol.
- **Challenge format:** Coding, design challenge. Prompt: "Design a game where scoring, level transitions, and game over are all coordinated through custom broadcasts. Choose clear names and document what each broadcast means." Provided: partial game structure. Auto‑grading checks broadcast names (clarity/meaningfulness) and that corresponding receivers are correctly implemented.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PD.

### T06.G6.04 – Handle edge cases in event scripts

- **Short name:** Debug unexpected event behavior
- **Description:** Students identify and fix subtle event-handling bugs, such as a broadcast sent before a listener is ready, a key event that interferes with game logic, or events that fire in an unexpected order.
- **Challenge format:** Coding, debugging challenge. Starter project has a subtle event bug (e.g., "level up" broadcast is sent before the game-over listener is set up, or key events cause sprite to move off-screen incorrectly). Prompt: "Fix this so the game doesn't crash and events happen in the right order." Auto‑grading tests the fixed code.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

---

## Grade 7

Grade 7 focuses on event-driven architecture in simulations and games, emphasizing state machines and signal-based coordination.

### T06.G7.01 – Design state machines using events

- **Short name:** Use events to manage game states
- **Description:** Students model a program using state machines where each state (menu, playing, paused, game-over) is a distinct set of event handlers, and broadcasts or events trigger transitions between states.
- **Challenge format:** Coding, architecture challenge. Prompt: "Design a game with distinct states: (1) Menu (waiting for key), (2) Playing (responding to controls), (3) Game Over (showing score). Use broadcasts to transition between states." Provided: partial state structure. Auto‑grading checks that states are distinct, transitions use broadcasts, and only appropriate events are active in each state.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PD.

### T06.G7.02 – Use event broadcasting for loose coupling

- **Short name:** Decouple systems with broadcasts
- **Description:** Students design large programs (e.g., games with multiple enemies, items, UI) where components communicate only through broadcasts rather than direct references, reducing complexity and improving modularity.
- **Challenge format:** Coding, system design. Prompt: "Design a game system where enemies, items, and the player don't directly reference each other. Instead, they broadcast events (enemy-hit, item-collected, score-changed) that others listen for." Provided: partial structure with multiple sprite types. Auto‑grading checks that systems are decoupled and communication uses broadcasts.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PD.

### T06.G7.03 – Trace and optimize event handling order

- **Short name:** Analyze event priorities and timing
- **Description:** Students examine event-driven code and reason about which scripts should run first, how timing affects behavior, and whether the order of broadcasts and receivers could be improved for correctness or performance.
- **Challenge format:** Concept, analysis. Prompt: "Two sprites broadcast 'collision' simultaneously. Three listeners update score, play sound, and check win condition. What's the ideal order and why?" Auto‑grading scores the answer based on correctness and reasoning.
- **CSTA:** MS‑PRO‑PF‑01, ALG‑AF.

### T06.G7.04 – Implement complex event sequences in projects

- **Short name:** Multi-stage event sequences
- **Description:** Students build projects where events follow complex, conditional sequences: initial triggers lead to broadcasts, which themselves broadcast further events, and the final outcomes depend on program state.
- **Challenge format:** Coding, scenario-based. Prompt: "When the player presses 'start', broadcast 'game-begin'. This triggers enemy spawning and music. When an enemy is hit, broadcast 'enemy-defeated', which updates score and checks if all enemies are gone. If so, broadcast 'level-complete'." Provided: partial sprite/event structure. Auto‑grading checks the entire event chain works.
- **CSTA:** MS‑PRO‑PF‑01.

---

## Grade 8

Grade 8 applies event-driven programming to sophisticated interactive systems and games, emphasizing real-world event architectures.

### T06.G8.01 – Design responsive multiplayer event handling

- **Short name:** Coordinate events across players
- **Description:** Students program a multiplayer or networked scenario where events from multiple players (e.g., broadcasts or input streams) must be received and processed correctly, handling race conditions and ensuring fair, synchronized behavior.
- **Challenge format:** Coding, multiplayer game or simulation. Prompt: "In a two-player game, each player's key presses are handled independently, but they can't occupy the same space. Use broadcasts to handle collisions and keep both players synchronized." Provided: multiplayer sprites and partial scripts. Auto‑grading tests that both players can play simultaneously without interference or crashes.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PD.

### T06.G8.02 – Implement custom event listeners and handlers

- **Short name:** Create reusable event-handling patterns
- **Description:** Students design custom blocks or scripts that encapsulate event-handling logic (e.g., a reusable "on-click-handler" or "collision-detector") so that events can be managed consistently across multiple objects.
- **Challenge format:** Coding, abstraction challenge. Prompt: "Create a custom block called 'handle-click' that can be used by multiple buttons in your game. Each button broadcasts its own event when clicked." Provided: multiple button sprites, empty custom block. Auto‑grading checks that the block is reusable and that each button correctly broadcasts its event.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑PD.

### T06.G8.03 – Analyze and optimize event-driven architecture

- **Short name:** Evaluate event system design
- **Description:** Students review an existing event-driven program (e.g., a complex game), identify inefficiencies or coupling issues, and propose or implement improvements to the event architecture.
- **Challenge format:** Concept and coding. Prompt: "This game has many scripts all listening to a 'tick' broadcast. Suggest how to reorganize to reduce the number of listeners and improve clarity. Implement at least one improvement." Provided: a complex program. Auto‑grading evaluates the refactoring for feasibility and improvement.
- **CSTA:** MS‑PRO‑PF‑01, PRO‑TR.

### T06.G8.04 – Justify event-handling choices for different scenarios

- **Short name:** Explain event design decisions
- **Description:** Students compare different event architectures (e.g., polling vs. broadcast-based, green flag + key events vs. a game loop) and explain when each is appropriate and why, considering clarity, efficiency, and maintainability.
- **Challenge format:** Concept, structured explanation. Prompt: "Compare a polling approach (forever loop checking if key pressed) to a broadcast approach (key event triggers broadcast). When would you use each and why?" Auto‑grading scores the explanation based on understanding of trade-offs.
- **CSTA:** MS‑PRO‑PF‑01, MS‑ALG‑AF‑02.

