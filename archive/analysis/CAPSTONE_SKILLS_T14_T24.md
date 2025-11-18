# Capstone Skills: T14-T24 Applications Domain

Generated: 2025-11-17

## Overview

Capstone skills are complex skills that integrate **5 or more prerequisites from 3 or more topics**. These skills demonstrate mastery and are excellent opportunities for performance assessment.

**Total Capstones:** 256 of 346 skills (74.0%)

## Capstones by Topic

### T14: 2D Games & Interactive Simulations

**Capstones:** 23

#### T14.G3.01: Create a title screen and a start button

- **Grade:** 3
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students design a title screen that appears when the game loads and is replaced by gameplay when a button is clicked. This introduces simple state management: the game switches from a "start" state to a "play" state.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T14.G3.02: End the game with a game over screen

- **Grade:** 3
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** When a win or loss condition is met, students switch to a "game over" state: gameplay pauses, a screen appears showing the final score or outcome, and the game no longer responds to player input for gameplay (though a "restart" option may be available).
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T14.G3.03: Use a loop to repeatedly spawn enemies

- **Grade:** 3
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Instead of manually placing each enemy sprite, students use a loop to create multiple enemy clones or reset their positions repeatedly, building in a pattern or at intervals. This reduces code duplication and introduces spawning logic.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T14.G3.04: Check multiple win/loss conditions

- **Grade:** 3
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students add multiple conditional branches to check different game‑ending scenarios (e.g., "win if score ≥ 10 OR lose if lives = 0 OR lose if time runs out"). This teaches compound logic in a game context.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T14.G4.01: Detect different types of collisions

- **Grade:** 4
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students expand beyond simple "touching" checks to distinguish between collisions with different object types (e.g., `if touching coin` vs `if touching enemy` vs `if touching wall`), each triggering a different outcome. This mirrors real game architecture.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T07.G3.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01

#### T14.G4.02: Implement simple AI movement for enemies

- **Grade:** 4
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students create a simple AI: enemies move in a pattern (e.g., patrol left‑right) or follow a basic rule (e.g., move toward the player if closer than a distance threshold, otherwise patrol). This introduces algorithmic decision‑making in game design.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T07.G3.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01

#### T14.G4.03: Use a timer or counter for paced events

- **Grade:** 4
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students implement a timer variable that increments each frame/loop iteration and triggers events when the timer reaches a threshold (e.g., spawn an enemy every 30 frames, or show a warning when time is low). This teaches event pacing.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T07.G3.01
  - T07.G4.01
  - T08.G3.01
  - T09.G3.01
  - T09.G4.01
  - T10.G3.01

#### T14.G4.04: Refactor game code for clarity

- **Grade:** 4
- **Total Dependencies:** 14
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students review their game code and identify repeated patterns (e.g., multiple similar collision checks or movement sequences) and refactor them using custom blocks or loops to reduce duplication and improve readability.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T07.G3.01
  - T07.G4.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T10.G3.01

#### T14.G5.01: Implement a scrolling camera for larger worlds

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students implement a simple camera/viewport system where the player remains roughly centered on screen and the background scrolls to simulate movement through a larger world. This introduces coordinate transformation concepts.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T14.G5.02: Create enemy waves or spawning patterns

- **Grade:** 5
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students implement more complex enemy spawning: enemies spawn in waves (groups), with varying patterns, timings, and behaviors. This moves beyond simple looping to conditional spawning.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T07.G3.01
  - T07.G5.01
  - T08.G3.01
  - T08.G5.01
  - T09.G3.01
  - T10.G3.01

#### T14.G5.03: Track game statistics (kills, time, accuracy)

- **Grade:** 5
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students add variables to track gameplay metrics beyond score (e.g., enemies defeated, accuracy percentage, time elapsed, distance traveled) and display or save these statistics for analysis or post‑game summary.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T09.G5.01
  - T10.G3.01
  - T11.G3.01

#### T14.G6.01: Design a game state machine

- **Grade:** 6
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students explicitly design and implement a state machine (e.g., using a `game state` variable) to manage transitions between title, menu, playing, paused, and game over states. This formalizes the concept of game states introduced in Grade 3.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T09.G6.01
  - T10.G3.01
  - T11.G3.01

#### T14.G6.02: Implement pixel‑perfect or grid‑based collision

- **Grade:** 6
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students move beyond simple rectangular collision boxes to implement more precise detection: pixel‑perfect collision (checking if visible pixels overlap) or grid‑based collision (checking tile occupancy). This improves game feel and fairness.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T08.G6.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01

#### T14.G6.03: Use data structures to manage game objects

- **Grade:** 6
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Instead of hardcoding individual enemy sprites, students use a list to dynamically store game object data (positions, states, velocities). This scales the game architecture: adding more enemies becomes adding to a list rather than duplicating code.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T09.G6.01
  - T10.G3.01
  - T10.G6.01

#### T14.G6.04: Debug game logic systematically

- **Grade:** 6
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students apply debugging techniques to game‑specific issues: a sprite moves unexpectedly, collisions trigger at wrong times, or scoring is incorrect. They use print/say blocks, trace execution, and isolate failures.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T08.G6.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01

#### T14.G7.01: Simulate physics: gravity and jumping

- **Grade:** 7
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T12, T13 (4 topics)
- **Description:** Students implement a simple physics system: a character has velocity in the y‑direction, gravity continuously increases downward velocity, and jumping (pressing a key) sets upward velocity if the character is on the ground. This introduces continuous numerical simulation.
- **Key Prerequisites:**
  - T06.G7.01
  - T08.G7.01
  - T12.G7.01
  - T13.G7.01

#### T14.G7.02: Implement simple pathfinding (waypoints or A*)

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students implement a pathfinding system where enemies move toward a goal or follow a predetermined path. Simple variants use waypoints; more advanced variants approximate A‑star behavior by moving toward the player while avoiding obstacles.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T14.G7.03: Optimize collision checking to avoid lag

- **Grade:** 7
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** When a game has many objects, checking all pairs can lag. Students learn to optimize: only check collisions for nearby objects (using quadtrees or spatial hashing concepts), cache results, or reduce check frequency. Even a conceptual understanding of the problem builds algorithmic thinking.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T07.G3.01
  - T08.G3.01
  - T08.G7.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01

#### T14.G7.04: Analyze and balance game difficulty

- **Grade:** 7
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students play and analyze their game, identifying difficulty parameters (enemy speed, health, respawn rate, reward amounts), and deliberately adjust them to achieve a specific difficulty curve. They might gather data on success rates or time to completion and use it to guide balance.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T07.G3.01
  - T08.G3.01
  - T08.G7.01
  - T09.G3.01
  - T09.G7.01
  - T10.G3.01

#### T14.G8.01: Architect a game using modular custom blocks

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students deliberately design their game architecture using custom blocks (procedures/functions) to encapsulate game systems: collision handler, spawn system, update physics, render, etc. This introduces software engineering principles.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T11.G8.01

#### T14.G8.02: Implement a particle system (visual effects)

- **Grade:** 8
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students implement a simple particle system: many small visual elements (e.g., sparks, smoke) that emit, move, fade, and disappear, creating visual feedback for events (explosions, hits). This combines loops, timing, and array/list management.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T07.G3.01
  - T07.G8.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T10.G8.01

#### T14.G8.03: Design game levels using data structures

- **Grade:** 8
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Instead of manually placing each game object, students define levels using data structures (lists of lists, or a string representing a tile map) and a parser that converts the data into actual game objects. This teaches data‑driven design and scales level creation.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T09.G8.01
  - T10.G3.01
  - T10.G8.01

#### T14.G8.04: Document and analyze a complete game system

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students document their game: architecture diagram showing how systems connect, pseudocode or flowcharts for key algorithms, and written explanations of design choices (why they chose certain collision detection, what difficulty parameters they used, how enemy AI works). This reinforces reflection and communication of complex ideas.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T08.G8.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01


---

### T15: Stories, Animation & Digital Media

**Capstones:** 24

#### T15.G3.01: Animate on command (click or key)

- **Grade:** 3
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students create a script where a sprite performs a sequence of animations (costume cycle, movement, sound) triggered by a click, key press, or other event, introducing interactivity to stories.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T15.G3.02: Dialogue with branching (simple choice)

- **Grade:** 3
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students implement a simple branching dialogue where the user or another sprite's action determines which speech the character says (e.g., if key "A" is pressed, character says one thing; if key "B," another).
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T15.G3.03: Multi‑character scene with interactions

- **Grade:** 3
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students coordinate behavior between two or more sprites in the same scene: one sprite moves or speaks, and another sprite responds based on proximity, overlap, or message. This introduces simple communication between sprites.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T15.G3.04: Sound effects and background music layer

- **Grade:** 3
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students layer multiple sounds: a background music track that plays continuously alongside sound effects triggered by sprite actions, building a richer audio narrative.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T15.G4.01: State-based character animation

- **Grade:** 4
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students use variables or backdrop changes to track a character's emotional or physical state (e.g., "happy" vs. "sad," "tired" vs. "awake") and play different animation loops accordingly. This connects variable logic to visual storytelling.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T07.G3.01
  - T07.G4.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T09.G4.01

#### T15.G4.02: Multi‑scene narrative with transitions

- **Grade:** 4
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students build a 3–4 scene story where scenes transition smoothly (fade, wipe, or timed switch) and sprite state carries across scenes (e.g., character remains "happy" or injured status persists). Introduces narrative continuity and polish.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T15.G4.03: Lip-sync or timed gesture animations

- **Grade:** 4
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students synchronize costume changes or simple animations to dialogue, creating the illusion that the character's mouth moves when speaking or gestures during specific words ("waving" when saying goodbye).
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T07.G3.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01

#### T15.G4.04: Complex dialogue tree with variables

- **Grade:** 4
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students build a branching dialogue where user choices are tracked in variables, affecting later plot points or character responses (e.g., if the user chooses "friendly" the character trusts you; if "mean," the character is wary).
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T07.G3.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T09.G4.01
  - T10.G3.01

#### T15.G5.01: Complex character state machine

- **Grade:** 5
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students implement a character that cycles through many states (idle, walking, running, jumping, celebrating, resting) with different animation loops, triggered by different events or conditions. This introduces state-machine thinking for animation.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T07.G3.01
  - T07.G5.01
  - T08.G3.01
  - T08.G5.01
  - T09.G3.01
  - T10.G3.01

#### T15.G5.02: Multi‑subplot story with branching paths

- **Grade:** 5
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students write a branching narrative where early choices lead to different scene sequences, sub‑stories, or endings. Multiple characters may have parallel story arcs.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T07.G3.01
  - T08.G3.01
  - T08.G5.01
  - T09.G3.01
  - T10.G3.01
  - T10.G5.01

#### T15.G5.03: Cinematic panning and zoom effects

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students simulate cinematic effects: "zooming in" on a character (enlarging a sprite or changing scale) or "panning" the camera by moving the stage's visible region (using CreatiCode's pan/focus or sprite positioning) to follow action or emphasize a story moment.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T15.G5.04: Layered audio design (music, ambiance, effects)

- **Grade:** 5
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students compose a scene with multiple simultaneous audio layers: background ambiance (e.g., wind, crowd murmur), a music track, and triggered sound effects. They may implement fade-in/fade-out or audio transitions using volume changes or timed overlaps.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T09.G5.01
  - T10.G3.01
  - T10.G5.01

#### T15.G6.01: Design and trace character state diagrams

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students create or analyze a diagram showing all possible states a character can be in and the transitions between them (e.g., Idle → Walking → Running, or Happy → Angry → Sad). This develops their ability to reason about and design complex animation systems.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T15.G6.02: Optimize animation with shared costume libraries

- **Grade:** 6
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students manage animation efficiently by creating shared costume assets that multiple sprites can use (e.g., a "happy face" costume set used by multiple characters) or by organizing costume numbers systematically to reduce redundancy.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T10.G6.01
  - T11.G3.01

#### T15.G6.03: Branching narrative with data persistence

- **Grade:** 6
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students maintain a data structure (e.g., a list or table of choices, or multiple variables) that remembers which decisions the player has made throughout the story. Later scenes reference this data to adapt dialogue, NPC reactions, or available options.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T09.G6.01
  - T10.G3.01
  - T10.G6.01

#### T15.G6.04: Narrative design principles: pacing and user feedback

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students analyze or design a story, reasoning about pacing (when dialogue happens relative to action), visual feedback (does the player know what to do?), and audio cues (does music change to signal important moments?). They articulate design choices using design principles.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T15.G7.01: Implement a scene graph or scene manager

- **Grade:** 7
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students design or implement a "scene manager" that tracks which scene is active, transitions between scenes automatically or on command, and maintains state across scene changes. This models real game and interactive media architecture.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T09.G7.01
  - T10.G3.01
  - T11.G3.01

#### T15.G7.02: Animate using sprite sheets and frame indices

- **Grade:** 7
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students work with a single sprite image containing multiple animation frames in a grid (a sprite sheet), and write code that displays the correct frame by setting costume index based on calculations (e.g., frame = walk_start + loop_counter).
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T07.G3.01
  - T07.G7.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T10.G7.01

#### T15.G7.03: Implement and compare branching narrative algorithms

- **Grade:** 7
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students implement or analyze two different methods for handling branching stories (e.g., nested if/else vs. a data-driven approach with choice tables) and reason about which is more maintainable, readable, or efficient as the story grows.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T07.G3.01
  - T08.G3.01
  - T08.G7.01
  - T09.G3.01
  - T09.G7.01
  - T10.G3.01

#### T15.G7.04: Evaluate narrative fairness and accessibility

- **Grade:** 7
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students play a story-game and critique it for narrative representation, accessibility (readability of text, clarity of instructions), and fairness (do all player paths feel equally rewarding?). They identify potential improvements.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T07.G3.01
  - T08.G3.01
  - T08.G7.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01

#### T15.G8.01: Implement a narrative engine with state and dialogue data

- **Grade:** 8
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students design and code a simple narrative engine that separates story data (dialogue, choices, state changes) from the presentation logic. For example, a "dialogue table" holds character lines and conditions; the engine checks conditions, displays the right line, and updates state.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T08.G8.01
  - T09.G3.01
  - T09.G8.01
  - T10.G3.01

#### T15.G8.02: Optimize animation performance with costume pooling

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students implement or describe techniques to reduce the number of costumes needed for smooth animation, such as reusing a single sprite and manipulating its size/rotation instead of swapping costumes, or implementing procedural animation using geometry.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T15.G8.03: Implement input handling and player agency

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students design a narrative experience where player input (keyboard, mouse, speech, gesture if available) meaningfully affects the story. They consider latency, feedback clarity, and fairness (does every path feel rewarded?).
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T08.G8.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01

#### T15.G8.04: Analyze narrative impacts: representation and bias

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students analyze an interactive story (or their own) for representation of diverse characters, stereotypes, narrative bias (e.g., do all endings favor one choice or character type?), and fairness. They propose revisions.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01


---

### T16: User Interfaces & Widgets

**Capstones:** 24

#### T16.G3.01: Create a start/stop button interface

- **Grade:** 3
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12 (7 topics)
- **Description:** Students design a simple state machine where clicking a "Start" button begins a game loop (sprite moves, score counts) and clicking a "Stop" button ends it. They learn to use a variable to track game state.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G3.02: Use a label to display changing information

- **Grade:** 3
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T08, T09, T10, T11, T12 (6 topics)
- **Description:** Students create a label that continuously updates to show dynamic information (e.g., a timer counting down, the current level, or the player's name input). The label text changes based on a variable or computation.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G3.03: Add a button to reset or restart the game

- **Grade:** 3
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T08, T09, T10, T11, T12 (6 topics)
- **Description:** Students add a "Reset" button that, when clicked, clears variables (e.g., sets score to 0, returns sprite to start position), updates all relevant labels, and prepares the game to be played again.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G3.04: Create a menu with button options

- **Grade:** 3
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T08, T09, T10, T11, T12 (6 topics)
- **Description:** Students design a menu screen with multiple buttons (e.g., "Play Game," "Instructions," "Quit") and labels, and connect each button to a different scene or action. This introduces the concept of navigation in an interface.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G4.01: Add a text input widget and use the entered text

- **Grade:** 4
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T08, T09, T10, T11, T12 (6 topics)
- **Description:** Students add a text input widget (also called a text box or input field) and use blocks to read the text the user types. For example, "Ask the player for their name and then display 'Welcome, [name]!' on a label."
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G4.02: Validate input and provide feedback

- **Grade:** 4
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T08, T09, T10, T11, T12 (6 topics)
- **Description:** Students use conditionals to validate user input (e.g., "Check if the name field is empty; if so, show an error message") and provide user feedback via a label. This builds understanding of error handling in user interfaces.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G4.03: Create a dropdown menu widget

- **Grade:** 4
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T08, T09, T10, T11, T12 (6 topics)
- **Description:** Students add a dropdown widget that displays a list of choices (e.g., "Easy," "Medium," "Hard") and use a block to read the selected option. They might use the selection to set a game difficulty or change colors.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T10.G3.01
  - T10.G4.01
  - T11.G3.01

#### T16.G4.04: Build a settings panel with multiple controls

- **Grade:** 4
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12 (6 topics)
- **Description:** Students create a settings or options screen with multiple widgets (buttons, labels, sliders, dropdowns) to control game features (e.g., volume, difficulty, graphics quality). They learn to organize widgets logically and respond to changes.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T10.G3.01
  - T10.G4.01
  - T11.G3.01

#### T16.G5.01: Create a multi‑screen app with a navigation interface

- **Grade:** 5
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students build an app with multiple screens (e.g., home screen, game screen, results screen) and use buttons and labels to navigate between them. They manage widget visibility to show/hide different screens.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T08.G3.01
  - T08.G5.01
  - T09.G3.01
  - T10.G3.01
  - T10.G5.01
  - T11.G3.01

#### T16.G5.02: Design a form with multiple inputs and validation

- **Grade:** 5
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students create a form interface with multiple text input fields, dropdowns, or checkboxes, validate all inputs for completeness and correctness, and display a summary or confirmation message. This teaches form design and validation patterns.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T08.G3.01
  - T08.G5.01
  - T09.G3.01
  - T10.G3.01
  - T10.G5.01
  - T11.G3.01

#### T16.G5.03: Build a leaderboard or high‑score display

- **Grade:** 5
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students create a label or series of labels that display high scores or player rankings. They use lists or variables to store scores and update the display dynamically. This introduces the concept of showing structured data in a UI.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T08.G3.01
  - T09.G3.01
  - T09.G5.01
  - T10.G3.01
  - T10.G5.01
  - T11.G3.01

#### T16.G5.04: Implement a responsive HUD that reacts to game state

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students design a "heads-up display" (HUD)—on-screen UI elements that show real-time game information (health bar, ammo count, mini-map indicator, status text). The HUD updates dynamically as game variables change.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T08.G3.01
  - T09.G3.01
  - T09.G5.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G6.01: Evaluate an interface for usability

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students examine an existing interface (a simple app screenshot) and identify issues or strengths: Are buttons clearly labeled? Is the layout intuitive? Are colors accessible for colorblind users? They learn to think like a UX designer and consider diverse users.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T08.G3.01
  - T08.G6.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G6.02: Design an interface based on user feedback

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students design an initial interface (buttons, labels, layout), ask peers or a teacher to try it, gather feedback on usability, and then modify the design to address the feedback. This introduces the iterative design process.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T08.G3.01
  - T08.G6.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G6.03: Use color and contrast to improve readability

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students apply color theory to interface design: choosing high-contrast text and backgrounds for readability, avoiding color combinations that are difficult for colorblind users, and using color to highlight important elements (e.g., a red button for "Stop").
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T08.G3.01
  - T08.G6.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G6.04: Create an interface that works on different screen sizes

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students learn that interfaces may be viewed on different devices (tablets, phones, computers) and adjust their layouts to be flexible. They position buttons and labels using percentages or relative sizing rather than fixed positions.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T08.G3.01
  - T08.G6.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G7.01: Build a data collection interface (survey or questionnaire)

- **Grade:** 7
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students design an interface for a survey or questionnaire with text inputs, dropdowns, checkboxes, or radio buttons; validate responses; and collect the data. They learn how interfaces are used to gather information.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T08.G3.01
  - T08.G7.01
  - T09.G3.01
  - T09.G7.01
  - T10.G3.01
  - T10.G7.01

#### T16.G7.02: Implement a search or filter interface

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students create a text input field where users can type a query, and the interface filters or searches a list of items (e.g., a player inventory, a menu of options) to show only matching results. This is a real-world UI pattern.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T10.G7.01
  - T11.G3.01
  - T12.G3.01

#### T16.G7.03: Design an accessible interface for users with different abilities

- **Grade:** 7
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students consider accessibility needs (e.g., text size for low vision, keyboard controls for mobility challenges, colorblind-friendly palettes) and redesign an interface to accommodate multiple ability types. They learn to design inclusively from the start.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T08.G3.01
  - T08.G7.01
  - T09.G3.01
  - T10.G3.01
  - T10.G7.01
  - T11.G3.01

#### T16.G7.04: Create a help or tutorial interface

- **Grade:** 7
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students design a help or tutorial interface within a game, including explanatory labels, step-by-step instructions, images/animations, and a "Next" button to guide the player through mechanics or controls.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01
  - T12.G7.01

#### T16.G8.01: Design a wizard or step-by-step interface

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students build a "wizard" interface that guides users through a multi-step process (e.g., character creation, game setup, checkout) with Previous/Next buttons, progress indicators, and validation at each step. They manage state across multiple screens.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T08.G3.01
  - T08.G8.01
  - T09.G3.01
  - T10.G3.01
  - T10.G8.01
  - T11.G3.01

#### T16.G8.02: Implement dynamic content loading in a UI

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students design an interface where selecting an option dynamically loads and displays related content (e.g., clicking a character name displays their stats, clicking a level number shows the level preview). Content is retrieved from lists or variables.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T08.G3.01
  - T09.G3.01
  - T09.G8.01
  - T10.G3.01
  - T10.G8.01
  - T11.G3.01

#### T16.G8.03: Analyze UI design patterns and their effectiveness

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students examine two different interface designs for the same task (e.g., two layouts for a settings menu, two ways to input a number) and evaluate which is more effective based on clarity, ease of use, and aesthetics. They write a brief analysis.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T08.G3.01
  - T08.G8.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T16.G8.04: Document and refine a UI design based on usability testing

- **Grade:** 8
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13 (7 topics)
- **Description:** Students conduct user testing of their interface (having peers try to complete a task using their interface, noting where they struggle), document observations, and refactor the interface to resolve usability issues. This reinforces the human-centered design cycle.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01
  - T12.G8.01


---

### T17: Physics-Based Motion & Simulation

**Capstones:** 24

#### T17.G3.01: Initialize a 2D physics world

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T07, T08, T09 (4 topics)
- **Description:** Students use the "Initialize 2D Physics" block from CreatiCode's physics category to set up a physics-enabled world with gravity. They learn the concept of a physics world and adjustable gravity.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01

#### T17.G3.02: Add a physics body to a sprite (gravity effect)

- **Grade:** 3
- **Total Dependencies:** 6
- **Integrates Topics:** T06, T07, T08, T09, T10 (5 topics)
- **Description:** Students attach a physics body to a sprite (setting it to dynamic and optionally specifying mass), so that gravity automatically pulls it downward. They observe realistic falling motion without manually coding position changes.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T17.G3.03: Create a platform using a static physics body

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T07, T08, T09 (4 topics)
- **Description:** Students use a static physics body (one that doesn't move) to create a floor or platform. The sprite's dynamic body stops when it hits the static body, learning about collision stopping.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01

#### T17.G3.04: Apply a force to jump (impulse)

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T07, T08, T09 (4 topics)
- **Description:** Students apply an upward impulse or force to a physics-enabled sprite (e.g., in response to a key press) to make it jump. This introduces the concept of applying forces to change motion.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01

#### T17.G4.01: Adjust friction for realistic motion

- **Grade:** 4
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T07, T08, T09, T10, T14 (6 topics)
- **Description:** Students set the friction property on a physics body so that a sliding sprite gradually slows down due to friction, rather than moving at constant speed or decreasing manually.
- **Key Prerequisites:**
  - T06.G4.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G4.01
  - T14.G3.01

#### T17.G4.02: Control bounciness (restitution)

- **Grade:** 4
- **Total Dependencies:** 6
- **Integrates Topics:** T06, T07, T08, T09, T14 (5 topics)
- **Description:** Students adjust the restitution (bounciness) property of a physics body to control how much a sprite bounces when it hits a surface. Higher restitution means more bounce.
- **Key Prerequisites:**
  - T06.G4.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T14.G3.01

#### T17.G4.03: Detect collisions between physics bodies

- **Grade:** 4
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T07, T08, T09, T14 (5 topics)
- **Description:** Students use a collision detection block or condition to determine when two physics-enabled sprites touch. This can trigger events like scoring or sprite removal.
- **Key Prerequisites:**
  - T06.G4.01
  - T07.G3.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T14.G3.01

#### T17.G4.04: Build a simple pendulum or swinging motion

- **Grade:** 4
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T07, T08, T09, T14 (5 topics)
- **Description:** Students create a sprite that swings back and forth using forces or by updating its angle in a loop. This explores circular/rotational motion with physics concepts.
- **Key Prerequisites:**
  - T06.G4.01
  - T07.G3.01
  - T07.G4.01
  - T08.G3.01
  - T09.G3.01
  - T14.G3.01

#### T17.G5.01: Simulate a projectile (gravity + initial velocity)

- **Grade:** 5
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T07, T08, T09, T13, T14 (6 topics)
- **Description:** Students create a sprite that starts with an initial velocity at an angle and follows a parabolic path under gravity. This is the classic projectile motion simulation.
- **Key Prerequisites:**
  - T06.G5.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T13.G5.01
  - T14.G4.01

#### T17.G5.02: Create a multi-object system (chain or stack)

- **Grade:** 5
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T12, T13, T14 (7 topics)
- **Description:** Students create a system of several physics-enabled sprites (e.g., stacked boxes, a chain of connected objects) and observe how forces propagate through the system.
- **Key Prerequisites:**
  - T06.G5.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T12.G5.01
  - T13.G5.01
  - T14.G4.01

#### T17.G5.03: Simulate air resistance or drag

- **Grade:** 5
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T13, T14 (6 topics)
- **Description:** Students approximate air resistance by applying a velocity-dependent force (or by decreasing velocity each step) as a sprite falls, making heavier objects fall faster than light ones (in a simplified model).
- **Key Prerequisites:**
  - T06.G5.01
  - T07.G3.01
  - T08.G3.01
  - T08.G5.01
  - T09.G3.01
  - T13.G5.01
  - T14.G4.01

#### T17.G5.04: Collision groups for selective interactions

- **Grade:** 5
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T07, T08, T09, T13, T14 (6 topics)
- **Description:** Students set collision groups on physics bodies so that certain sprites collide with some objects but not others (e.g., player passes through powerups but collides with enemies).
- **Key Prerequisites:**
  - T06.G5.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T13.G5.01
  - T14.G4.01

#### T17.G6.01: Design a platformer with physics

- **Grade:** 6
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T12, T13, T14 (7 topics)
- **Description:** Students create a simple platformer game with physics-enabled player, platforms, gravity, and jumping. They design a level layout and test the physics feel.
- **Key Prerequisites:**
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T12.G6.01
  - T13.G6.01
  - T14.G5.01

#### T17.G6.02: Trace physics simulation logic

- **Grade:** 6
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T12, T13, T14 (7 topics)
- **Description:** Given a set of physics values (gravity, mass, velocity, friction) for a sprite, students trace what will happen over several steps and predict the final position or behavior.
- **Key Prerequisites:**
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T12.G6.01
  - T13.G6.01
  - T14.G5.01

#### T17.G6.03: Debug physics simulation (unexpected motion)

- **Grade:** 6
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T07, T08, T09, T12, T13, T14 (7 topics)
- **Description:** Students are given a physics simulation that behaves unexpectedly (e.g., sprite falls too fast, bounces too high, doesn't stop) and modify physics properties to fix it.
- **Key Prerequisites:**
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T08.G6.01
  - T09.G3.01
  - T12.G6.01
  - T13.G6.01
  - T14.G5.01

#### T17.G6.04: Compare physics engine behavior to real-world motion

- **Grade:** 6
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T07, T08, T09, T12, T13, T14 (7 topics)
- **Description:** Students compare a physics simulation to real-world observations (e.g., dropping a ball, bouncing a ball) and discuss whether the simulation matches reality or where it simplifies.
- **Key Prerequisites:**
  - T06.G6.01
  - T07.G3.01
  - T08.G3.01
  - T08.G6.01
  - T09.G3.01
  - T12.G6.01
  - T13.G6.01
  - T14.G5.01

#### T17.G7.01: Simulate friction in different media (water, air, ground)

- **Grade:** 7
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T08, T10, T12, T13, T14 (6 topics)
- **Description:** Students create multiple sprites sliding on surfaces with different friction values (high friction ground, low friction ice, medium friction carpet) and observe how each behaves differently.
- **Key Prerequisites:**
  - T06.G7.01
  - T08.G7.01
  - T10.G7.01
  - T12.G7.01
  - T13.G7.01
  - T14.G6.01

#### T17.G7.02: Apply multiple forces simultaneously

- **Grade:** 7
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T07, T08, T09, T10, T12, T13, T14 (8 topics)
- **Description:** Students apply more than one force to a sprite (e.g., gravity and wind, or gravity and a player-applied thrust) and observe the resulting motion as the vector sum of forces.
- **Key Prerequisites:**
  - T06.G7.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G7.01
  - T12.G7.01
  - T13.G7.01
  - T14.G6.01

#### T17.G7.03: Model a real physics scenario (pendulum, orbit, rolling object)

- **Grade:** 7
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T12, T13, T14 (7 topics)
- **Description:** Students choose a real physics phenomenon (e.g., a pendulum, a ball rolling downhill, a satellite orbiting) and create a CreatiCode simulation that reasonably approximates the physics.
- **Key Prerequisites:**
  - T06.G7.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T12.G7.01
  - T13.G7.01
  - T14.G6.01

#### T17.G7.04: Measure and analyze motion data (position, velocity, acceleration)

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T07, T08, T09, T10, T12, T13, T14 (8 topics)
- **Description:** Students log position, velocity, and/or acceleration of a physics-simulated sprite to a list or table, then analyze the data to verify expected physics patterns (e.g., constant acceleration under gravity).
- **Key Prerequisites:**
  - T06.G7.01
  - T07.G3.01
  - T08.G3.01
  - T08.G7.01
  - T09.G3.01
  - T09.G7.01
  - T10.G7.01
  - T12.G7.01

#### T17.G8.01: Design and balance a physics-based arcade game

- **Grade:** 8
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T12, T13, T14 (7 topics)
- **Description:** Students design a physics-based arcade game (similar to Angry Birds, a catapult puzzle, or a gravity-assisted platformer) where projectiles, gravity, and collisions are core mechanics.
- **Key Prerequisites:**
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T12.G8.01
  - T13.G8.01
  - T14.G7.01

#### T17.G8.02: Optimize a physics simulation for performance

- **Grade:** 8
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T07, T08, T09, T12, T13, T14 (7 topics)
- **Description:** Students work with a physics simulation that has many objects and optimize it by adjusting gravity updates, reducing collision checks, or culling off-screen objects to maintain smooth performance.
- **Key Prerequisites:**
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T08.G8.01
  - T09.G3.01
  - T12.G8.01
  - T13.G8.01
  - T14.G7.01

#### T17.G8.03: Implement a physics constraint or joint

- **Grade:** 8
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T07, T08, T09, T12, T13, T14 (7 topics)
- **Description:** Students use advanced physics features (e.g., a weld joint, hinge joint, or distance constraint) to connect two sprites so they move together or rotate around a pivot.
- **Key Prerequisites:**
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T12.G8.01
  - T13.G8.01
  - T14.G7.01

#### T17.G8.04: Design a realistic vs stylized physics feel

- **Grade:** 8
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T07, T08, T09, T10, T12, T13, T14 (8 topics)
- **Description:** Students design a game (e.g., platformer) with two variants: one with realistic physics and one with stylized (unrealistic but fun) physics. They compare and justify design choices.
- **Key Prerequisites:**
  - T06.G8.01
  - T07.G3.01
  - T08.G3.01
  - T08.G8.01
  - T09.G3.01
  - T10.G8.01
  - T12.G8.01
  - T13.G8.01


---

### T18: 3D Worlds & Games

**Capstones:** 21

#### T18.G3.01: Implement a forever loop for continuous 3D control

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T07, T08, T09 (4 topics)
- **Description:** Students use a `forever` loop with conditional key checks inside to enable smooth, continuous control of a 3D character (player-controlled avatar that responds to held keys).
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01

#### T18.G3.02: Create a 3D platformer with a visible ground

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T12 (4 topics)
- **Description:** Students create a 3D scene with a ground plane (a large flat 3D box) and one or more floating platforms, establishing the foundation for a platformer game.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T12.G3.01

#### T18.G4.01: Implement jumping with physics

- **Grade:** 4
- **Total Dependencies:** 6
- **Integrates Topics:** T06, T08, T09, T14 (4 topics)
- **Description:** Students apply an upward impulse or force to a 3D character with physics enabled, allowing it to jump off the ground and fall back due to gravity.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T08.G3.01
  - T09.G3.01
  - T14.G3.01

#### T18.G4.02: Use a variable to track score in a 3D game

- **Grade:** 4
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T08, T09, T14 (4 topics)
- **Description:** Students create a numeric variable to count collected items or points in a 3D game, incrementing it when the player touches a collectible object.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T08.G3.01
  - T09.G3.01
  - T09.G4.01
  - T14.G3.01

#### T18.G4.04: Clone 3D objects to create multiple instances

- **Grade:** 4
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T08, T09, T10, T12, T14 (6 topics)
- **Description:** Students use the clone block to create multiple instances of a 3D object (e.g., a collectible or enemy) at different positions within a game scene.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G4.01
  - T08.G3.01
  - T08.G4.01
  - T09.G3.01
  - T10.G4.01
  - T12.G4.01
  - T14.G3.01

#### T18.G5.01: Use a 3D follow camera attached to the player

- **Grade:** 5
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T08, T09, T13, T14 (5 topics)
- **Description:** Students attach a follow camera to the player character so the camera tracks the character's position and rotation, maintaining a fixed offset (e.g., behind-and-above). This is a standard game camera mechanic.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T08.G3.01
  - T09.G3.01
  - T09.G5.01
  - T13.G5.01
  - T14.G4.01

#### T18.G5.02: Create a multi-level 3D platformer

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T08, T09, T10, T12, T13, T14 (7 topics)
- **Description:** Students build or design a 3D platformer with 2–3 levels, each with its own platforms, collectibles, and enemies. They may use lists or variables to track current level or use separate sections of the scene.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T08.G3.01
  - T09.G3.01
  - T09.G5.01
  - T10.G5.01
  - T12.G5.01
  - T13.G5.01

#### T18.G5.03: Simulate falling water or rolling ball physics

- **Grade:** 5
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T08, T09, T10, T13, T14 (6 topics)
- **Description:** Students use the 3D physics engine to simulate realistic behavior of objects: e.g., a ball rolling down a slope, water falling and bouncing off surfaces, or a block sliding with friction.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T08.G3.01
  - T09.G3.01
  - T10.G5.01
  - T13.G5.01
  - T14.G4.01

#### T18.G5.04: Use nested loops to arrange 3D objects in a grid

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T07, T08, T09, T10, T13, T14 (7 topics)
- **Description:** Students use nested loops to create a grid of 3D objects (e.g., a checkerboard of platforms, a wall of blocks, or an array of collectibles).
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G5.01
  - T07.G5.01
  - T08.G3.01
  - T08.G5.01
  - T09.G3.01
  - T10.G5.01
  - T13.G5.01

#### T18.G6.01: Set up collision groups for selective interaction

- **Grade:** 6
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T08, T09, T12, T13, T14 (6 topics)
- **Description:** Students use the 3D physics engine's collision groups to define which objects collide with which. For example, the player collides with platforms and coins but passes through walls that look like obstacles, or enemies collide with each other but not the player.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T08.G3.01
  - T09.G3.01
  - T12.G6.01
  - T13.G6.01
  - T14.G5.01

#### T18.G6.02: Trace a 3D project to predict object positions

- **Grade:** 6
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T08, T09, T12, T13, T14 (6 topics)
- **Description:** Students read a 3D script with movement and rotation blocks and predict the final position and orientation of an object without running the code.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T08.G3.01
  - T09.G3.01
  - T12.G6.01
  - T13.G6.01
  - T14.G5.01

#### T18.G6.03: Refactor repeated 3D object creation into a loop or function

- **Grade:** 6
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T07, T08, T09, T11, T12, T13, T14 (8 topics)
- **Description:** Students are given a project with many repeated "add object, set position, set properties" blocks and rewrite it using a loop or custom function to reduce duplication.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T07.G6.01
  - T08.G3.01
  - T09.G3.01
  - T11.G6.01
  - T12.G6.01
  - T13.G6.01

#### T18.G6.04: Implement a camera with mouse look (rotate by mouse movement)

- **Grade:** 6
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T08, T09, T12, T13, T14 (6 topics)
- **Description:** Students implement a camera that rotates its view based on mouse movement, allowing the player to look around smoothly (common in first-person games).
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G6.01
  - T08.G3.01
  - T09.G3.01
  - T12.G6.01
  - T13.G6.01
  - T14.G5.01

#### T18.G7.01: Implement pathfinding or waypoint-based NPC movement

- **Grade:** 7
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T12, T13, T14 (4 topics)
- **Description:** Students create a non-player character (NPC) that moves between waypoints or toward a target position (player or goal) using distance calculations or a simple patrolling behavior.
- **Key Prerequisites:**
  - T06.G7.01
  - T12.G7.01
  - T13.G7.01
  - T14.G6.01

#### T18.G7.02: Design collision response for bouncing or sliding

- **Grade:** 7
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T08, T09, T12, T13, T14 (6 topics)
- **Description:** Students use the 3D physics engine's properties (restitution, friction) to tune how objects respond to collisions: e.g., creating a bouncy ball, a sliding block, or a sticky object.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T08.G3.01
  - T09.G3.01
  - T12.G7.01
  - T13.G7.01
  - T14.G6.01

#### T18.G7.03: Use 3D coordinates and distance calculations for game mechanics

- **Grade:** 7
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T08, T09, T12, T13, T14 (6 topics)
- **Description:** Students use distance formulas or conditional checks based on 3D positions (e.g., "if player within 5 units of this object") to trigger events or game logic, reinforcing spatial reasoning with numbers.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G7.01
  - T08.G3.01
  - T08.G7.01
  - T09.G3.01
  - T12.G7.01
  - T13.G7.01
  - T14.G6.01

#### T18.G7.04: Implement a physics-based puzzle mechanic

- **Grade:** 7
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T12, T13, T14 (4 topics)
- **Description:** Students design a simple puzzle that requires using physics-based manipulation: e.g., rolling a ball into a goal, stacking blocks to reach an object, or using gravity to guide an object.
- **Key Prerequisites:**
  - T06.G7.01
  - T12.G7.01
  - T13.G7.01
  - T14.G6.01

#### T18.G8.01: Implement a level editor or dynamic level loading

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T12, T13, T14 (7 topics)
- **Description:** Students use variables or lists to store level data (e.g., object types, positions, properties) and implement code to load different levels dynamically, enabling replay value and multiple game worlds.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T08.G3.01
  - T08.G8.01
  - T09.G3.01
  - T09.G8.01
  - T10.G8.01
  - T12.G8.01

#### T18.G8.02: Use multiple cameras to implement split-screen or UI view

- **Grade:** 8
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T08, T09, T10, T12, T13, T14 (7 topics)
- **Description:** Students create a project with two cameras: one for the main 3D game view and one for a UI overlay (e.g., inventory, minimap, or score display), or split-screen for two players.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T08.G3.01
  - T09.G3.01
  - T09.G8.01
  - T10.G8.01
  - T12.G8.01
  - T13.G8.01

#### T18.G8.03: Analyze and optimize a 3D game for performance

- **Grade:** 8
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T08, T09, T12, T13, T14 (6 topics)
- **Description:** Students examine a 3D project that runs slowly (e.g., many clones or physics objects), identify the bottleneck (e.g., too many draw calls, excessive physics calculations), and refactor to improve frame rate.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T08.G3.01
  - T08.G8.01
  - T09.G3.01
  - T12.G8.01
  - T13.G8.01
  - T14.G7.01

#### T18.G8.04: Analyze trade-offs in 3D game design decisions

- **Grade:** 8
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T08, T09, T12, T13, T14 (6 topics)
- **Description:** Students review a 3D game project and explain design decisions: e.g., "Why did I use physics for the player instead of manual movement?" or "Why is the camera positioned this way?" reflecting on alternatives and trade-offs.
- **Key Prerequisites:**
  - T06.G3.01
  - T06.G8.01
  - T08.G3.01
  - T09.G3.01
  - T12.G8.01
  - T13.G8.01
  - T14.G7.01


---

### T19: Multiplayer & Connected Apps

**Capstones:** 24

#### T19.G3.01: Create a multiplayer game room with a name and password

- **Grade:** 3
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T08, T09, T10, T11, T12 (6 topics)
- **Description:** Students use the "create game" block to start a multiplayer game session, providing a game name, an optional password, and their player name. They understand the role of the host in setting up the game for others to join.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T19.G3.02: Filter the game list to find and join a specific game

- **Grade:** 3
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T08, T09, T10, T11, T12 (6 topics)
- **Description:** Students use a "list games" block to see available multiplayer games, then filter or choose the correct game based on its name, and join it using the join game block with matching parameters (game name, password).
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T19.G3.03: Assign roles to players and check a player's role

- **Grade:** 3
- **Total Dependencies:** 6
- **Integrates Topics:** T06, T08, T09, T10, T11 (5 topics)
- **Description:** Students specify a role when creating or joining a game (e.g., "Red team", "Goalie", "Catcher") and use a "get player role" reporter block to check what role other players have, allowing role‑specific game logic.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01

#### T19.G3.04: Synchronize a position variable across multiplayer instances

- **Grade:** 3
- **Total Dependencies:** 7
- **Integrates Topics:** T06, T08, T09, T10, T11, T12 (6 topics)
- **Description:** Students use a multiplayer variable (or understand how sending/receiving networked values works) to keep one player's x/y position synchronized across all instances so all players see the sprite in the same location.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01
  - T11.G3.01
  - T12.G3.01

#### T19.G4.01: Sync multiple variables (position, score, state) in a multiplayer game

- **Grade:** 4
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T14, T18 (8 topics)
- **Description:** Students extend synchronization to multiple game variables: each player's position (x/y), score, health, or animation state. They use separate multiplayer sends or understand how a shared data structure keeps all these in sync.
- **Key Prerequisites:**
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T11.G4.01
  - T12.G4.01
  - T14.G3.01
  - T18.G3.01

#### T19.G4.02: Respond to a player joining or leaving the game

- **Grade:** 4
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T08, T09, T10, T11, T14, T18 (7 topics)
- **Description:** Students use event blocks like "when [player] joins game" or "when [player] leaves game" to trigger actions (e.g., starting a countdown, removing a player's sprite, showing a welcome message).
- **Key Prerequisites:**
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T11.G4.01
  - T14.G3.01
  - T18.G3.01

#### T19.G4.03: Implement a simple turn-taking mechanism

- **Grade:** 4
- **Total Dependencies:** 8
- **Integrates Topics:** T06, T08, T09, T10, T11, T14, T18 (7 topics)
- **Description:** Students use a shared variable (e.g., "current_turn") and conditionals to ensure only one player can act at a time. They may track turns with a counter or flag, advancing it when one player finishes their action.
- **Key Prerequisites:**
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T11.G4.01
  - T14.G3.01
  - T18.G3.01

#### T19.G4.04: Trace a multiplayer game script to predict final states

- **Grade:** 4
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T14, T18 (8 topics)
- **Description:** Students read a simple multiplayer script (with position syncs, score updates, and joins) and predict the final state of the game (both players' positions, shared score, player list) after a sequence of actions.
- **Key Prerequisites:**
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T11.G4.01
  - T12.G4.01
  - T14.G3.01
  - T18.G3.01

#### T19.G5.01: Build a shared lobby or chat interface with message display

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T08, T09, T10, T11, T13, T14, T18 (8 topics)
- **Description:** Students build a simple chat or message log system where one player sends a message (via ask and wait), the message is broadcast to all players, and all players see an updated list or log of messages on screen.
- **Key Prerequisites:**
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G5.01
  - T11.G4.01
  - T13.G5.01
  - T14.G4.01

#### T19.G5.02: Maintain and display a list of connected players

- **Grade:** 5
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T13, T14, T18 (8 topics)
- **Description:** Students use a "get players in game" or "list players" block to retrieve all connected players and display their names and roles (e.g., in a label widget or variable). They may update this list dynamically as players join/leave.
- **Key Prerequisites:**
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T09.G5.01
  - T10.G4.01
  - T10.G5.01
  - T11.G4.01
  - T13.G5.01

#### T19.G5.03: Detect and respond to collision between synced player sprites

- **Grade:** 5
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T08, T09, T10, T11, T13, T14, T18 (8 topics)
- **Description:** Students use the "touching [sprite]" block or equivalent to detect when their sprite collides with another player's synced sprite. They respond with actions like scoring a point, changing state, or broadcasting an event.
- **Key Prerequisites:**
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T11.G4.01
  - T13.G5.01
  - T14.G4.01
  - T18.G4.01

#### T19.G5.04: Implement a simple scoring system with a shared leaderboard

- **Grade:** 5
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T13, T14, T18 (8 topics)
- **Description:** Students maintain individual scores for each player (via separate variables or a table) and display them in a leaderboard format. Scores update in real time as players perform actions, and all players see the same leaderboard.
- **Key Prerequisites:**
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T09.G5.01
  - T10.G4.01
  - T10.G5.01
  - T11.G4.01
  - T13.G5.01

#### T19.G6.01: Design a multiplayer game world with persistent state (coins, obstacles, etc.)

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13, T14, T18 (9 topics)
- **Description:** Students design a game where the world (stage) has persistent, shared objects (coins, platforms, enemies) that all players interact with. When one player collects a coin, it disappears for both players. All players see the same world state.
- **Key Prerequisites:**
  - T06.G6.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G6.01
  - T11.G4.01
  - T12.G6.01
  - T13.G6.01

#### T19.G6.02: Handle network latency with buffering or prediction

- **Grade:** 6
- **Total Dependencies:** 10
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13, T14, T18 (9 topics)
- **Description:** Students learn that network messages take time to arrive and implement simple strategies like buffering recent position updates or predicting a player's next position. They understand that a brief delay is normal and design games that tolerate or mitigate this.
- **Key Prerequisites:**
  - T06.G6.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T11.G4.01
  - T12.G6.01
  - T13.G6.01
  - T14.G5.01

#### T19.G6.03: Implement a collaborative puzzle or challenge with shared objectives

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13, T14, T18 (9 topics)
- **Description:** Students create a game where both players must work together toward a common goal (e.g., gathering items, reaching a location, solving a puzzle together). Progress is shared and visible to both players.
- **Key Prerequisites:**
  - T06.G6.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G6.01
  - T11.G4.01
  - T12.G6.01
  - T13.G6.01

#### T19.G6.04: Trace a networked game's state changes across multiple broadcast events

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13, T14, T18 (9 topics)
- **Description:** Students read a multiplayer script where several broadcast events are sent in sequence (e.g., "Game Starting" → all sprites move to center → "Ready?" → players can move). They predict the final state and behavior of the game.
- **Key Prerequisites:**
  - T06.G6.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G6.01
  - T11.G4.01
  - T12.G6.01
  - T13.G6.01

#### T19.G7.01: Design multiplayer game balance and fairness mechanisms

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13, T14, T18 (9 topics)
- **Description:** Students analyze or design multiplayer games with fairness in mind: equal starting positions, identical rules for all players, avoiding advantages from network latency, and balanced scoring systems. They discuss why fairness matters in multiplayer games.
- **Key Prerequisites:**
  - T06.G7.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G7.01
  - T11.G4.01
  - T12.G7.01
  - T13.G7.01

#### T19.G7.02: Implement dynamic player matching or team assignment

- **Grade:** 7
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13, T14, T18 (9 topics)
- **Description:** Students use logic to automatically assign players to teams or matches based on criteria (e.g., first two players to join are a team, or random assignment). They may track team membership in a variable or list and ensure fair distribution.
- **Key Prerequisites:**
  - T06.G7.01
  - T08.G4.01
  - T09.G4.01
  - T09.G7.01
  - T10.G4.01
  - T10.G7.01
  - T11.G4.01
  - T12.G7.01

#### T19.G7.03: Evaluate network efficiency: which data must be synced vs. local-only

- **Grade:** 7
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13, T14, T18 (9 topics)
- **Description:** Students analyze a multiplayer game and determine which variables should be synchronized across players (e.g., positions, shared score) and which can be local-only (e.g., individual power-up effects, temporary animations). They understand trade-offs between consistency and bandwidth.
- **Key Prerequisites:**
  - T06.G7.01
  - T08.G4.01
  - T09.G4.01
  - T09.G7.01
  - T10.G4.01
  - T10.G7.01
  - T11.G4.01
  - T12.G7.01

#### T19.G7.04: Handle variable numbers of players (2, 3, 4, or more) in a single game

- **Grade:** 7
- **Total Dependencies:** 13
- **Integrates Topics:** T06, T07, T08, T09, T10, T11, T12, T13, T14, T18 (10 topics)
- **Description:** Students design a multiplayer game that can accommodate more than two players. They use loops and lists to manage a variable number of player sprites, score entries, and positions, ensuring all players are treated fairly regardless of count.
- **Key Prerequisites:**
  - T06.G7.01
  - T07.G7.01
  - T08.G4.01
  - T09.G4.01
  - T09.G7.01
  - T10.G4.01
  - T10.G7.01
  - T11.G4.01

#### T19.G8.01: Implement anti-cheat validation (server-side or consensus checking)

- **Grade:** 8
- **Total Dependencies:** 9
- **Integrates Topics:** T06, T08, T09, T10, T12, T13, T14, T18 (8 topics)
- **Description:** Students implement basic anti-cheat measures: a shared validation rule (e.g., "score can only increase by 1 per coin collection, not arbitrary amounts") or a server-mediated authority (e.g., the host validates coin collection before updating the score). They understand the concept that trusted authorities prevent cheating.
- **Key Prerequisites:**
  - T06.G8.01
  - T08.G8.01
  - T09.G8.01
  - T10.G8.01
  - T12.G8.01
  - T13.G8.01
  - T14.G7.01
  - T18.G7.01

#### T19.G8.02: Trace a message exchange to verify game state consistency

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13, T14, T18 (9 topics)
- **Description:** Students trace the sending and receiving of multiplayer messages (broadcasts, role-based sends) to ensure all players end up with consistent game state. They identify potential inconsistency bugs (e.g., message received out of order, or one player doesn't receive an update).
- **Key Prerequisites:**
  - T06.G8.01
  - T08.G4.01
  - T08.G8.01
  - T09.G4.01
  - T10.G4.01
  - T10.G8.01
  - T11.G4.01
  - T12.G8.01

#### T19.G8.03: Design a multiplayer game with a persistent server/database for high scores or player data

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13, T14, T18 (9 topics)
- **Description:** Students connect a multiplayer game to cloud storage or a database backend (using CreatiCode's cloud blocks or equivalent) to save and retrieve player data (high scores, achievements, player profiles) across sessions and matches. They understand that persistent data lives beyond a single game session.
- **Key Prerequisites:**
  - T06.G8.01
  - T08.G4.01
  - T09.G4.01
  - T09.G8.01
  - T10.G4.01
  - T11.G4.01
  - T12.G8.01
  - T13.G8.01

#### T19.G8.04: Analyze the architecture and data flow of a multiplayer system

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T06, T08, T09, T10, T11, T12, T13, T14, T18 (9 topics)
- **Description:** Students examine the architecture of a multiplayer game system: client (player's game instance), server (shared authority), and network. They trace how a message flows from one client to the server, is processed, and broadcast back. They identify potential bottlenecks or failure points.
- **Key Prerequisites:**
  - T06.G8.01
  - T08.G4.01
  - T08.G8.01
  - T09.G4.01
  - T09.G8.01
  - T10.G4.01
  - T11.G4.01
  - T12.G8.01


---

### T20: Algorithmic Art & Creative Coding

**Capstones:** 23

#### T20.G3.01: Use nested loops to draw a grid pattern

- **Grade:** 3
- **Total Dependencies:** 6
- **Integrates Topics:** T04, T06, T07, T09, T11 (5 topics)
- **Description:** Students use an outer loop (rows) and an inner loop (columns) to create a grid of stamps or shapes. This is a key skill for algorithmic art, introducing two-dimensional design thinking.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G3.01
  - T07.G3.01
  - T09.G3.01
  - T11.G3.01

#### T20.G3.03: Use randomness to create generative patterns

- **Grade:** 3
- **Total Dependencies:** 7
- **Integrates Topics:** T04, T06, T07, T08, T09, T11 (6 topics)
- **Description:** Students add `pick random` to a loop-based drawing script to vary colors, positions, or stamp sizes. This introduces generative art: each run produces a slightly different design.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T11.G3.01

#### T20.G3.04: Trace nested loops and predict output

- **Grade:** 3
- **Total Dependencies:** 6
- **Integrates Topics:** T04, T06, T07, T09, T11 (5 topics)
- **Description:** Students read code with nested loops and predict or count how many stamps will appear or describe the final pattern structure.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G3.01
  - T07.G3.01
  - T09.G3.01
  - T11.G3.01

#### T20.G4.01: Draw a spiral using a loop with changing distance

- **Grade:** 4
- **Total Dependencies:** 8
- **Integrates Topics:** T04, T06, T07, T09, T11 (5 topics)
- **Description:** Students write a loop where the move distance or angle increases on each iteration, creating a spiral or expanding geometric pattern. This combines loops with variables.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G4.01
  - T07.G3.01
  - T07.G4.01
  - T09.G3.01
  - T09.G4.01
  - T11.G3.01

#### T20.G4.02: Create a tessellation or tiling pattern

- **Grade:** 4
- **Total Dependencies:** 7
- **Integrates Topics:** T04, T06, T07, T09, T11 (5 topics)
- **Description:** Students design a repeating tile (e.g., a hexagon or square with internal pattern) and then use nested loops to tile it across the screen, creating a seamless tessellation.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G4.01
  - T07.G3.01
  - T07.G4.01
  - T09.G3.01
  - T11.G3.01

#### T20.G4.03: Use variables to parametrize art (size, color, rotation)

- **Grade:** 4
- **Total Dependencies:** 7
- **Integrates Topics:** T04, T06, T07, T09, T11 (5 topics)
- **Description:** Students create a script where variables control the visual design (e.g., a variable for number of sides, pen size, or rotation angle). Changing the variable changes the whole design.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G4.01
  - T07.G3.01
  - T09.G3.01
  - T09.G4.01
  - T11.G3.01

#### T20.G4.04: Analyze and modify a complex art script

- **Grade:** 4
- **Total Dependencies:** 9
- **Integrates Topics:** T04, T06, T07, T08, T09, T11, T13 (7 topics)
- **Description:** Students are given a script that draws a pattern but has an issue (e.g., too many loops causing clutter, wrong colors, or incorrect spacing). They modify it to fix or improve the design.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G4.01
  - T07.G3.01
  - T07.G4.01
  - T08.G4.01
  - T09.G3.01
  - T11.G3.01
  - T13.G4.01

#### T20.G5.01: Create a bar chart or simple data visualization

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T04, T06, T07, T09, T10, T11, T13 (7 topics)
- **Description:** Students use loops to draw rectangles or lines of varying heights based on a list of numeric values, creating a visual representation of data. This bridges algorithmic art with data visualization.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G5.01
  - T07.G3.01
  - T07.G5.01
  - T09.G3.01
  - T09.G5.01
  - T10.G5.01
  - T11.G3.01

#### T20.G5.02: Animate a pattern based on a variable

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T04, T06, T07, T08, T09, T11, T13 (7 topics)
- **Description:** Students create a script that draws or modifies a pattern in response to a counter variable that changes over time (e.g., a spiral that grows with each frame, or a pattern that rotates).
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G5.01
  - T07.G3.01
  - T07.G5.01
  - T08.G5.01
  - T09.G3.01
  - T09.G5.01
  - T11.G3.01

#### T20.G5.03: Create interactive art that responds to mouse or keyboard

- **Grade:** 5
- **Total Dependencies:** 7
- **Integrates Topics:** T04, T06, T07, T09, T11, T13 (6 topics)
- **Description:** Students build a script where user input (mouse position, key press) drives the algorithmic drawing. For example, the art style or pattern changes based on where the user clicks.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G5.01
  - T07.G3.01
  - T09.G3.01
  - T11.G3.01
  - T13.G5.01

#### T20.G5.04: Design a recursive-like pattern (fractal preview)

- **Grade:** 5
- **Total Dependencies:** 8
- **Integrates Topics:** T04, T06, T07, T09, T11, T13 (6 topics)
- **Description:** Students create patterns where a shape is drawn, and then smaller copies of the same shape are drawn inside or around it, mimicking fractal-like structure (without full recursion, using nested loops instead).
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G5.01
  - T07.G3.01
  - T07.G5.01
  - T09.G3.01
  - T11.G3.01
  - T13.G5.01

#### T20.G6.01: Analyze and describe an algorithmic art script

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T04, T06, T07, T08, T09, T11, T12, T13 (8 topics)
- **Description:** Students examine a script that produces an interesting pattern and explain what the loops, variables, and conditionals do and how they combine to create the visual effect.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G6.01
  - T07.G3.01
  - T07.G6.01
  - T08.G6.01
  - T09.G3.01
  - T09.G6.01
  - T11.G3.01

#### T20.G6.02: Refactor repetitive art code into loops and functions

- **Grade:** 6
- **Total Dependencies:** 10
- **Integrates Topics:** T04, T06, T07, T09, T11, T12, T13 (7 topics)
- **Description:** Students take a lengthy, repetitive art script and refactor it to use loops and/or custom blocks, reducing duplication while maintaining the visual output.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G6.01
  - T07.G3.01
  - T07.G6.01
  - T09.G3.01
  - T11.G3.01
  - T11.G6.01
  - T12.G6.01

#### T20.G6.03: Use variables and conditional logic in art

- **Grade:** 6
- **Total Dependencies:** 10
- **Integrates Topics:** T04, T06, T07, T08, T09, T11, T12, T13 (8 topics)
- **Description:** Students write an algorithm where the visual design branches based on variable values or conditions (e.g., draw a different tile pattern depending on a value, or alternate colors based on a counter).
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G6.01
  - T07.G3.01
  - T08.G6.01
  - T09.G3.01
  - T09.G6.01
  - T11.G3.01
  - T12.G6.01

#### T20.G6.04: Create data-driven visualizations

- **Grade:** 6
- **Total Dependencies:** 10
- **Integrates Topics:** T04, T06, T07, T09, T10, T11, T12, T13 (8 topics)
- **Description:** Students design a script that reads data from a list or table and creates a visualization (bar chart, scatter plot, or abstract artistic representation). This connects data analysis with creative expression.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G6.01
  - T07.G3.01
  - T09.G3.01
  - T09.G6.01
  - T10.G6.01
  - T11.G3.01
  - T12.G6.01

#### T20.G7.01: Optimize an art algorithm for efficiency

- **Grade:** 7
- **Total Dependencies:** 10
- **Integrates Topics:** T04, T06, T07, T08, T09, T11, T12, T13 (8 topics)
- **Description:** Students compare two algorithms that produce similar art but differ in efficiency (e.g., one uses nested loops, another uses conditionals and single loop). They analyze which is faster and explain why.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G7.01
  - T07.G3.01
  - T07.G7.01
  - T08.G7.01
  - T09.G3.01
  - T11.G3.01
  - T12.G7.01

#### T20.G7.02: Use advanced control flow in art (while, repeat-until)

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T04, T06, T07, T08, T09, T11, T12, T13 (8 topics)
- **Description:** Students use a `repeat until` loop (e.g., draw until reaching screen edge) or a `while` condition in an art algorithm, introducing data-dependent looping rather than fixed-count repetition.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G7.01
  - T07.G3.01
  - T07.G7.01
  - T08.G7.01
  - T09.G3.01
  - T09.G7.01
  - T11.G3.01

#### T20.G7.03: Understand how parameters change visual aesthetics

- **Grade:** 7
- **Total Dependencies:** 8
- **Integrates Topics:** T04, T06, T07, T09, T11, T12, T13 (7 topics)
- **Description:** Students investigate how varying a parameter (pen size, angle increment, randomness level) changes the visual result and explain the relationship between the mathematical parameter and the aesthetic effect.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G7.01
  - T07.G3.01
  - T09.G3.01
  - T11.G3.01
  - T12.G7.01
  - T13.G7.01

#### T20.G7.04: Recognize patterns in real-world algorithmic art and design

- **Grade:** 7
- **Total Dependencies:** 9
- **Integrates Topics:** T04, T06, T07, T08, T09, T11, T12, T13 (8 topics)
- **Description:** Students study examples of algorithmic art or generative design from artists or nature (fractals, Penrose tilings, algorithmic music visualizers) and identify the underlying algorithmic principles.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G7.01
  - T07.G3.01
  - T08.G7.01
  - T09.G3.01
  - T11.G3.01
  - T12.G7.01
  - T13.G7.01

#### T20.G8.01: Design and implement a complex data visualization

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T04, T06, T07, T08, T09, T10, T11, T12, T13 (9 topics)
- **Description:** Students design a script that visualizes a larger or more complex dataset (multiple variables, time series) in an artistic way. They choose how to represent data dimensions (color, size, position, animation) and justify their choices.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G8.01
  - T07.G3.01
  - T08.G8.01
  - T09.G3.01
  - T09.G8.01
  - T10.G8.01
  - T11.G3.01

#### T20.G8.02: Create generative or randomized art with constrained variation

- **Grade:** 8
- **Total Dependencies:** 9
- **Integrates Topics:** T04, T06, T07, T09, T11, T12, T13 (7 topics)
- **Description:** Students build an algorithm that uses randomness and loops to generate unique artwork on each run, but with constraints (e.g., a color palette, size limits, or symmetry rules) to maintain aesthetic quality.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G8.01
  - T07.G3.01
  - T07.G8.01
  - T09.G3.01
  - T11.G3.01
  - T12.G8.01
  - T13.G8.01

#### T20.G8.03: Analyze social and creative implications of algorithms in art

- **Grade:** 8
- **Total Dependencies:** 8
- **Integrates Topics:** T04, T06, T07, T09, T11, T12, T13 (7 topics)
- **Description:** Students explore how algorithmic choices affect the artistic result and discuss ethical/creative questions: Does algorithmic art count as "real" art? How do algorithm parameters influence what is created? Can algorithms replicate human creativity?
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G8.01
  - T07.G3.01
  - T09.G3.01
  - T11.G3.01
  - T12.G8.01
  - T13.G8.01

#### T20.G8.04: Optimize art rendering for performance

- **Grade:** 8
- **Total Dependencies:** 9
- **Integrates Topics:** T04, T06, T07, T08, T09, T11, T12, T13 (8 topics)
- **Description:** Students profile or analyze an art script and identify bottlenecks (e.g., too many draw calls, redundant calculations). They refactor to improve performance while maintaining visual output.
- **Key Prerequisites:**
  - T04.G3.01
  - T06.G8.01
  - T07.G3.01
  - T08.G8.01
  - T09.G3.01
  - T11.G3.01
  - T12.G8.01
  - T13.G8.01


---

### T21: AI Media Tools & Creative Assets

**Capstones:** 24

#### T21.G3.01: Write detailed prompts with style and mood words

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students expand their prompt vocabulary to include style descriptors ("watercolor," "cartoon," "realistic," "pixel art") and mood words ("spooky," "joyful," "mysterious"). They learn that these words significantly influence the generated image's aesthetic.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T21.G3.02: Understand that AI training data affects what it can create

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students learn that AI image generators are trained on many examples of images, so they can only make pictures of things they've "seen" in training. They understand that biases in training data can affect what the AI creates, introducing early ethical thinking.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T21.G3.03: Search for and remix existing community AI art

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students search the CreatiCode AI Image Library for existing community-generated images that suit their project. They use library images as starting points, selecting and adapting them for their story or game.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T21.G3.04: Give credit when using AI images (attribution)

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students understand that when they use AI-generated images in a project, they should acknowledge that AI was used to create them. They practice adding comments or credits in their projects (e.g., "Backdrop made with CreatiCode AI") to be honest and transparent.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T21.G4.01: Edit an AI image with the pen tool

- **Grade:** 4
- **Total Dependencies:** 8
- **Integrates Topics:** T05, T06, T08, T09, T10, T15, T16 (7 topics)
- **Description:** Students take an AI-generated image (used as a backdrop costume) and use CreatiCode's pen or drawing tools to add their own marks, details, or corrections. This blends human and AI creativity in a concrete way.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T15.G3.01
  - T16.G3.01

#### T21.G4.02: Compare AI-generated vs. hand-drawn versions of the same idea

- **Grade:** 4
- **Total Dependencies:** 8
- **Integrates Topics:** T05, T06, T08, T09, T10, T15, T16 (7 topics)
- **Description:** Students generate an AI image for a given prompt, then observe or attempt a hand-drawn version (or compare to a reference image). They discuss which better suits the project's needs, mood, or artistic goals. This develops critical thinking about tool selection.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T15.G3.01
  - T16.G3.01

#### T21.G4.03: Evaluate an AI image for bias or appropriateness

- **Grade:** 4
- **Total Dependencies:** 8
- **Integrates Topics:** T05, T06, T08, T09, T10, T15, T16 (7 topics)
- **Description:** Students examine AI-generated images to identify potential biases (e.g., whether certain character types are represented fairly) or appropriateness issues (violence, stereotypes). They practice critical evaluation of AI outputs before using them.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T15.G3.01
  - T16.G3.01

#### T21.G4.04: Write clear, unbiased prompts for AI image generation

- **Grade:** 4
- **Total Dependencies:** 8
- **Integrates Topics:** T05, T06, T08, T09, T10, T15, T16 (7 topics)
- **Description:** Students learn to write prompts that don't reinforce stereotypes or biases. For example, instead of "a doctor" (which may unconsciously bias toward certain demographics), they might write "a diverse team of doctors" or just "a person in medical clothing." This practices ethical AI use.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T15.G3.01
  - T16.G3.01

#### T21.G5.01: Write a detailed visual specification as a prompt

- **Grade:** 5
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T13, T15, T16 (8 topics)
- **Description:** Students write longer, more precise prompts (15–20+ words) that specify composition, colors, lighting, perspective, and emotional tone. For example: "A sunny day in a forest clearing, with tall pine trees, a small wooden cabin in the distance, soft golden light filtering through leaves, warm and peaceful mood." This represents advanced prompt engineering.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T08.G5.01
  - T09.G4.01
  - T10.G4.01
  - T13.G5.01

#### T21.G5.02: Experiment with prompt variations to understand AI responses

- **Grade:** 5
- **Total Dependencies:** 13
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students systematically generate multiple images from slight prompt variations (e.g., changing adjectives, adding/removing details) to understand how specific words influence output. This develops scientific thinking about AI behavior.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T08.G5.01
  - T09.G4.01
  - T10.G4.01
  - T10.G5.01

#### T21.G5.03: Document and explain AI art choices in a project

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T05, T06, T08, T09, T10, T13, T15, T16 (8 topics)
- **Description:** Students create a written or recorded reflection explaining which images they generated, why, what prompts they used, and how the AI images fit their creative vision. This develops metacognition and documentation skills.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T13.G5.01
  - T15.G4.01

#### T21.G5.04: Understand copyright and responsible use of AI-generated art

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T05, T06, T08, T09, T10, T13, T15, T16 (8 topics)
- **Description:** Students learn that CreatiCode-generated images are owned by the platform and can only be used in CreatiCode projects. They understand that they should not claim AI images as their own and should credit the tool. This introduces intellectual property and digital citizenship.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T13.G5.01
  - T15.G4.01

#### T21.G6.01: Plan a project that uses AI-generated, hand-drawn, and remix assets

- **Grade:** 6
- **Total Dependencies:** 12
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students plan which assets (sprite costumes, backdrops, animations) will be AI-generated, which will be hand-drawn, and which will use existing/remixed Scratch library elements. They justify each choice based on efficiency, artistic goals, and project scope.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G6.01
  - T08.G4.01
  - T08.G6.01
  - T09.G4.01
  - T10.G4.01
  - T12.G6.01

#### T21.G6.02: Use AI-generated images with prompt variations to create animation

- **Grade:** 6
- **Total Dependencies:** 12
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students generate multiple AI images by varying prompts slightly (e.g., "person standing," "person running," "person jumping") and use them as animation frames. They understand how AI can speed up asset creation for animation.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G6.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G6.01
  - T12.G6.01

#### T21.G6.03: Analyze the impact of AI-generated assets on game/story authenticity

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students examine games or stories that use AI-generated art and discuss: Does the AI art fit the style? Does it feel authentic to the creator's vision? Would hand-drawn art change the feeling? This develops critical media literacy.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G6.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G6.01
  - T13.G6.01

#### T21.G6.04: Troubleshoot a failed AI generation and revise the prompt

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students are shown a failed or unsuitable AI-generated image and asked to diagnose the problem by analyzing the original prompt. They revise and regenerate, practicing debugging and iteration in a creative context.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G6.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G6.01
  - T13.G6.01

#### T21.G7.01: Explain why AI struggles with certain image types

- **Grade:** 7
- **Total Dependencies:** 13
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students learn that AI image generators struggle with specific subjects: hands (often distorted), text (misspelled), complex mathematical patterns, or specific cultural imagery. They understand these limitations are due to training data gaps and model architecture, not lack of intelligence.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T08.G7.01
  - T09.G4.01
  - T09.G7.01
  - T10.G4.01

#### T21.G7.02: Examine bias in AI-generated images and discuss causes

- **Grade:** 7
- **Total Dependencies:** 12
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students systematically test AI image generators with prompts that should yield diverse results (e.g., "a doctor," "a teacher," "a CEO"). They observe whether the AI perpetuates stereotypes based on gender, race, age, or other factors, and discuss why training data bias causes this.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T09.G4.01
  - T09.G7.01
  - T10.G4.01
  - T12.G7.01

#### T21.G7.03: Plan and execute an AI-heavy creative project with intentional choices

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students design and build a substantial game or multimedia story (8+ screens/scenes) where AI-generated images are a primary asset source. They make intentional decisions about prompts, style consistency, and ethical considerations throughout the project.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G7.01
  - T13.G7.01

#### T21.G7.04: Compare creative workflows with and without AI tools

- **Grade:** 7
- **Total Dependencies:** 12
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students complete two similar creative tasks—one using only hand-drawn/remix assets and one using AI generation—and reflect on differences in time, effort, quality, and artistic satisfaction. This builds nuanced thinking about tool tradeoffs.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T08.G7.01
  - T09.G4.01
  - T10.G4.01
  - T12.G7.01

#### T21.G8.01: Investigate questions of authorship and credit in AI-assisted art

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students explore the philosophical question: When a human writes an AI prompt and the AI generates an image, who is the "artist"? They research real-world debates (e.g., AI art competitions, copyright disputes) and form informed opinions on credit and ownership.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G8.01
  - T13.G8.01

#### T21.G8.02: Analyze how AI image generation might change creative industries

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students examine how professional game studios, animators, and illustrators are (or might) adopt AI tools. They consider both opportunities (faster prototyping, accessibility) and concerns (job displacement, cultural homogenization). This develops systems thinking about technology and society.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G8.01
  - T13.G8.01

#### T21.G8.03: Design an AI-assisted creative workflow for a realistic scenario

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students design a realistic workflow for a small indie game or animation team using AI image generation for concept art, backgrounds, or character variations. They consider quality, consistency, revision cycles, and team roles. This applies AI tool knowledge to authentic professional contexts.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G8.01
  - T12.G8.01

#### T21.G8.04: Evaluate the ethical implications of large-scale AI deployment in creative fields

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T15, T16 (9 topics)
- **Description:** Students evaluate multi-faceted ethical questions: Should creators be required to disclose AI use? Does AI democratize creativity or homogenize it? What happens to artists whose work was used to train AI? They form nuanced positions informed by multiple perspectives.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G8.01
  - T12.G8.01


---

### T22: AI Chatbots & Information Apps

**Capstones:** 24

#### T22.G3.01: Write a clear prompt for ChatGPT

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students learn that how you write a prompt affects the quality of the AI's response, and they practice writing clear, specific prompts rather than vague ones.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T22.G3.02: Maintain conversation context with ChatGPT

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students understand that using the same ChatGPT session allows the AI to remember prior messages in a conversation, enabling follow-up questions and maintaining context, versus starting fresh each time.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T22.G3.03: Create a character chatbot with personality

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students design a chatbot that embodies a specific character or personality (e.g., a pirate, a teacher, a detective) by giving ChatGPT a system prompt or context that shapes its responses to match that character.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T22.G3.04: Handle invalid or off-topic user input gracefully

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students add conditional logic to detect when a user input is off-topic or unclear and respond politely with a redirection, improving the chatbot's user experience.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T22.G4.01: Summarize text using ChatGPT

- **Grade:** 4
- **Total Dependencies:** 7
- **Integrates Topics:** T05, T06, T08, T09, T10, T16 (6 topics)
- **Description:** Students ask ChatGPT to take a longer text and produce a concise summary, understanding that AI can transform content in useful ways.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T16.G3.01

#### T22.G4.02: Translate text using ChatGPT

- **Grade:** 4
- **Total Dependencies:** 7
- **Integrates Topics:** T05, T06, T08, T09, T10, T16 (6 topics)
- **Description:** Students use ChatGPT to translate user input into another language, expanding the idea of content transformation and showing practical AI applications.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T16.G3.01

#### T22.G4.03: Build a multi-turn Q&A chatbot with context

- **Grade:** 4
- **Total Dependencies:** 8
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T16 (7 topics)
- **Description:** Students create a chatbot that maintains conversation history across multiple turns, so the AI can reference earlier messages and provide coherent, context-aware replies.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G4.01
  - T16.G3.01

#### T22.G4.04: Identify and discuss responsible AI use

- **Grade:** 4
- **Total Dependencies:** 7
- **Integrates Topics:** T05, T06, T08, T09, T10, T16 (6 topics)
- **Description:** Students reflect on how to use ChatGPT responsibly (e.g., not claiming AI output as their own, fact-checking AI answers, respecting privacy in conversations) and discuss ethical concerns.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T16.G3.01

#### T22.G5.01: Build a virtual tutor chatbot

- **Grade:** 5
- **Total Dependencies:** 9
- **Integrates Topics:** T05, T06, T08, T09, T10, T13, T16 (7 topics)
- **Description:** Students design a tutoring chatbot that helps users learn a topic by asking guiding questions, providing hints, and adapting responses based on user answers.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T13.G5.01
  - T16.G4.01

#### T22.G5.02: Handle multiple chatbot sessions simultaneously

- **Grade:** 5
- **Total Dependencies:** 13
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students use multiple session variables to track separate conversations with the chatbot on different topics, understanding that sessions isolate context.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T08.G5.01
  - T09.G4.01
  - T09.G5.01
  - T10.G4.01

#### T22.G5.03: Create a FAQ chatbot that stores Q&A pairs

- **Grade:** 5
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T13, T16 (7 topics)
- **Description:** Students build a chatbot that stores frequently asked questions and answers in a list or table, and responds by searching the list before asking ChatGPT, improving efficiency and consistency.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T09.G5.01
  - T10.G4.01
  - T10.G5.01

#### T22.G5.04: Evaluate chatbot responses for accuracy and quality

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T05, T06, T08, T09, T10, T13, T16 (7 topics)
- **Description:** Students learn to critically evaluate chatbot responses, checking for accuracy, clarity, bias, and appropriateness, and making notes on when the chatbot performed well or poorly.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T08.G5.01
  - T09.G4.01
  - T10.G4.01
  - T13.G5.01

#### T22.G6.01: Design a chatbot for a specific audience

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students consider who will use their chatbot (e.g., young learners, people with disabilities, non-native speakers) and design its language, tone, and features accordingly, applying human-centered design.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G6.01
  - T08.G4.01
  - T08.G6.01
  - T09.G4.01
  - T10.G4.01
  - T12.G6.01

#### T22.G6.02: Use a table to store chatbot knowledge

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students structure a chatbot's knowledge base as a table, where each row contains a question, category, and answer, enabling efficient searching and scalable information management.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G6.01
  - T08.G4.01
  - T09.G4.01
  - T09.G6.01
  - T10.G4.01
  - T12.G6.01

#### T22.G6.03: Combine ChatGPT with pre-trained knowledge

- **Grade:** 6
- **Total Dependencies:** 12
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students build a chatbot that first checks a local knowledge base (list/table) and only uses ChatGPT if an answer is not found, balancing efficiency and flexibility.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G6.01
  - T08.G4.01
  - T08.G6.01
  - T09.G4.01
  - T10.G4.01
  - T10.G6.01

#### T22.G6.04: Discuss bias and fairness in chatbot responses

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students ask a chatbot questions that might elicit biased responses (e.g., about gender roles, cultural stereotypes) and analyze whether the responses are fair and inclusive, or if they reflect stereotypes.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G6.01
  - T08.G4.01
  - T08.G6.01
  - T09.G4.01
  - T10.G4.01
  - T12.G6.01

#### T22.G7.01: Design a multi-intent chatbot

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students design and build a chatbot that can recognize when a user wants different things (e.g., get information, ask for help, provide feedback) and respond appropriately to each intent.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T08.G7.01
  - T09.G4.01
  - T10.G4.01
  - T12.G7.01

#### T22.G7.02: Build a chatbot that learns from user feedback

- **Grade:** 7
- **Total Dependencies:** 12
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students implement a chatbot that logs user interactions and feedback, using the data to identify common questions or problematic responses to improve future versions.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T08.G7.01
  - T09.G4.01
  - T09.G7.01
  - T10.G4.01

#### T22.G7.03: Integrate external data into chatbot responses

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students enhance a chatbot by fetching or referencing external data sources (e.g., a spreadsheet, an API call simulation, or sensor data) to provide current or dynamic information.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T09.G4.01
  - T09.G7.01
  - T10.G4.01
  - T12.G7.01

#### T22.G7.04: Analyze societal impacts of chatbot misinformation

- **Grade:** 7
- **Total Dependencies:** 10
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students investigate how chatbots can spread misinformation or false information, discuss the societal consequences, and brainstorm safeguards.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G7.01
  - T13.G7.01

#### T22.G8.01: Extract key information from user input

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students implement logic to identify key entities or keywords in user questions (e.g., "Book by Roald Dahl" → extract "Roald Dahl" as author) to improve chatbot responses or data lookups.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T08.G8.01
  - T09.G4.01
  - T09.G8.01
  - T10.G4.01

#### T22.G8.02: Design and run chatbot performance tests

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students create test cases for a chatbot (predefined questions with expected answers) and run them to measure accuracy, identifying which types of questions the chatbot handles well or poorly.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T08.G8.01
  - T09.G4.01
  - T10.G4.01
  - T12.G8.01

#### T22.G8.03: Compare different chatbot designs for a task

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students implement two different approaches to the same chatbot task (e.g., rule-based lookup vs. ChatGPT-only, or different prompt strategies) and compare them on metrics like accuracy, speed, and user satisfaction.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T08.G8.01
  - T09.G4.01
  - T10.G4.01
  - T12.G8.01

#### T22.G8.04: Discuss ethical design and deployment of information bots

- **Grade:** 8
- **Total Dependencies:** 10
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students engage in structured discussion or written reflection about ethical responsibilities when deploying chatbots (e.g., transparency about AI use, managing user expectations, preventing harm, protecting privacy).
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G8.01
  - T13.G8.01


---

### T23: AI Voice, Vision & Gesture Interfaces

**Capstones:** 23

#### T23.G3.01: Repeat until spoken confirmation

- **Grade:** 3
- **Total Dependencies:** 6
- **Integrates Topics:** T06, T07, T08, T09, T10 (5 topics)
- **Description:** Students use a `repeat until` loop with speech input: the loop keeps prompting and listening for "yes" (or a target word) and stops when that word is recognized.
- **Key Prerequisites:**
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T23.G3.02: Use gesture to score points in a game

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students build a simple game where detecting a specific hand gesture (e.g., fist, thumbs-up, or hand at a certain position) increases the player's score. This combines pose/gesture detection with game state (a score variable).
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T23.G3.03: Build a voice-controlled menu

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students create a simple menu where speech input selects between options (e.g., "Say 1, 2, or 3 to pick a game"). The recognized number/word is matched to an action.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T23.G3.04: Create a gesture-based dance (pose detection)

- **Grade:** 3
- **Total Dependencies:** 5
- **Integrates Topics:** T06, T08, T09, T10 (4 topics)
- **Description:** Students use body pose detection to trigger different animations or sprite movements based on their body position. For example, when they stand with arms up, the sprite dances one way; arms down, a different way.
- **Key Prerequisites:**
  - T06.G3.01
  - T08.G3.01
  - T09.G3.01
  - T10.G3.01

#### T23.G4.02: Track hand movement across the screen

- **Grade:** 4
- **Total Dependencies:** 6
- **Integrates Topics:** T05, T06, T09, T10, T16 (5 topics)
- **Description:** Students collect hand position data over time (storing x, y coordinates in a list) as the hand moves on screen. They then visualize or analyze the movement pattern (e.g., a line or path trace).
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T09.G4.01
  - T10.G4.01
  - T16.G3.01

#### T23.G4.03: Count people in the camera view

- **Grade:** 4
- **Total Dependencies:** 8
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T16 (7 topics)
- **Description:** Students use hand or pose detection to estimate the number of distinct people in frame (e.g., if multiple hand detection results appear, each likely represents one person). They maintain a counter of detected individuals.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G4.01
  - T16.G3.01

#### T23.G4.04: Build an accessibility feature (voice commands)

- **Grade:** 4
- **Total Dependencies:** 7
- **Integrates Topics:** T05, T06, T08, T09, T10, T16 (6 topics)
- **Description:** Students design a game or application where voice commands fully control the experience (no keyboard/mouse required). For example, a player says "jump," "left," or "right" to move and interact, promoting accessibility.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T16.G3.01

#### T23.G5.01: Build a chatbot that responds to voice and speaks back

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T05, T06, T08, T09, T10, T13, T16 (7 topics)
- **Description:** Students create a chatbot that listens (speech recognition), sends the recognized text to ChatGPT, receives a reply, and speaks it aloud (text-to-speech). This is a complete voice conversation cycle.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G5.01
  - T13.G5.01

#### T23.G5.02: Detect and respond to exercise/fitness movements

- **Grade:** 5
- **Total Dependencies:** 6
- **Integrates Topics:** T05, T06, T08, T13, T16 (5 topics)
- **Description:** Students use pose detection to identify when the player is doing a specific exercise (e.g., squat, jump, arm raise) and award points for correct form or repetitions. This combines movement detection with game scoring.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G5.01
  - T08.G5.01
  - T13.G5.01
  - T16.G4.01

#### T23.G5.03: Log and analyze gesture data from a session

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T05, T06, T08, T09, T10, T13, T16 (7 topics)
- **Description:** Students collect gesture/hand/pose data over time (position, finger angles, etc.) into a table during a gameplay or interaction session. They then analyze this data to answer questions (e.g., "What was the most common gesture?", "How much did the hand move?").
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T09.G5.01
  - T10.G4.01
  - T13.G5.01

#### T23.G5.04: Design an interactive art piece controlled by voice and movement

- **Grade:** 5
- **Total Dependencies:** 9
- **Integrates Topics:** T05, T06, T08, T09, T10, T13, T16 (7 topics)
- **Description:** Students create an artistic project where speech input (e.g., words or emotions) and hand/body movements drive visual changes (colors, shapes, animations). The project is expressive and combines both modalities.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G5.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T13.G5.01
  - T16.G4.01

#### T23.G6.01: Handle speech recognition misheard words gracefully

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students implement error handling for speech recognition failures (e.g., when the system doesn't understand the word clearly). They add a confidence check or allow the user to retry if a word isn't recognized.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G6.01
  - T08.G4.01
  - T08.G6.01
  - T09.G4.01
  - T10.G4.01
  - T12.G6.01

#### T23.G6.02: Evaluate fairness and bias in pose detection

- **Grade:** 6
- **Total Dependencies:** 7
- **Integrates Topics:** T05, T06, T08, T12, T13, T16 (6 topics)
- **Description:** Students test pose detection on people with different body types, heights, abilities, and dress (e.g., loose vs tight clothing). They document whether the detection works equally well for everyone and reflect on potential bias.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G6.01
  - T08.G6.01
  - T12.G6.01
  - T13.G6.01
  - T16.G5.01

#### T23.G6.03: Improve speech recognition with feedback loop

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T07, T08, T09, T10, T12, T13, T16 (9 topics)
- **Description:** Students design a system that allows users to correct misheard words. Each correction is logged, helping the system (conceptually) improve over time. This introduces the idea of feedback-driven AI improvement.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G6.01
  - T07.G6.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G6.01

#### T23.G6.04: Trace and understand hand detection data

- **Grade:** 6
- **Total Dependencies:** 8
- **Integrates Topics:** T05, T06, T08, T09, T12, T13, T16 (7 topics)
- **Description:** Students trace through the hand detection data table, understanding that each row represents a keypoint (finger joint) with coordinates, and each column is an attribute (x, y, z, angle). They select and use specific rows to answer questions about hand position and posture.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G6.01
  - T08.G6.01
  - T09.G6.01
  - T12.G6.01
  - T13.G6.01
  - T16.G5.01

#### T23.G7.01: Design and test a hands-free app interface

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students design a small application (e.g., a quiz, a music player, a story reader) where all controls are voice-based. They test the interface with multiple users to evaluate how well voice commands are understood.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G7.01
  - T12.G7.01

#### T23.G7.02: Combine multiple AI modalities (voice + vision) in one project

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students create a project that meaningfully uses both voice and vision (or gesture) at the same time, where each modality contributes distinct information (e.g., voice gives commands, vision confirms who is speaking or detects a pose to enable the command).
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T10.G7.01
  - T12.G7.01

#### T23.G7.03: Measure and optimize gesture recognition accuracy

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students design a gesture (e.g., a thumbs-up, a specific hand shape, or pose) and test how consistently the system detects it. They measure accuracy (number of correct detections / total attempts) and try to improve it by refining the detection logic or providing clearer instructions to users.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T08.G7.01
  - T09.G4.01
  - T10.G4.01
  - T12.G7.01

#### T23.G7.04: Explain how AI voice/vision features affect user experience

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students reflect on how voice and vision recognition technologies enable or restrict access for different user groups (e.g., voice helps non-typists, but fails for those who are non-verbal; gesture recognition may miss people with limited mobility). They identify potential improvements.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G7.01
  - T08.G4.01
  - T08.G7.01
  - T09.G4.01
  - T10.G4.01
  - T12.G7.01

#### T23.G8.01: Implement a complete voice-to-action pipeline with error handling

- **Grade:** 8
- **Total Dependencies:** 10
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students build a voice application that includes speech recognition, command parsing/matching, error handling for misheard words, and feedback to the user. The system is robust enough to handle real-world speech variations (e.g., "go left" vs "turn left").
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T09.G4.01
  - T10.G4.01
  - T12.G8.01
  - T13.G8.01

#### T23.G8.02: Analyze pose data to classify or predict movement patterns

- **Grade:** 8
- **Total Dependencies:** 8
- **Integrates Topics:** T05, T06, T08, T09, T12, T13, T16 (7 topics)
- **Description:** Students collect pose data while a person performs different movements (e.g., walking, jumping, standing still) and use a table to organize and analyze the data. They look for patterns (e.g., differences in keypoint velocities, distances, or angles) that distinguish one movement from another.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G8.01
  - T08.G8.01
  - T09.G8.01
  - T12.G8.01
  - T13.G8.01
  - T16.G7.01

#### T23.G8.03: Design and justify a voice/vision accessibility feature

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students design a feature of an existing game or app that uses voice or vision to improve accessibility for a specific user group (e.g., a text-to-speech narrator for a reading game, hand-gesture controls for a player with limited fine motor control). They justify their design with evidence from user testing or accessibility research.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T08.G8.01
  - T09.G4.01
  - T10.G4.01
  - T12.G8.01

#### T23.G8.04: Evaluate and mitigate bias in AI detection systems

- **Grade:** 8
- **Total Dependencies:** 11
- **Integrates Topics:** T05, T06, T08, T09, T10, T12, T13, T16 (8 topics)
- **Description:** Students build or use a pose/gesture/speech detection system and systematically test it across different demographic groups, lighting conditions, accents, etc. They measure and document disparities in accuracy and propose mitigations.
- **Key Prerequisites:**
  - T05.G4.01
  - T06.G4.01
  - T06.G8.01
  - T08.G4.01
  - T08.G8.01
  - T09.G4.01
  - T10.G4.01
  - T12.G8.01


---

### T24: XO & AI-Supported Coding Practices

**Capstones:** 22

#### T24.G3.01: Ask XO to review your code idea

- **Grade:** 3
- **Total Dependencies:** 9
- **Integrates Topics:** T01, T02, T03, T06, T07, T08, T11, T13 (8 topics)
- **Description:** Before coding, a student describes their algorithm or plan to XO (e.g., "My plan is to repeat moving the sprite forward 10 times and then turn. Will this make a square?") and asks XO to spot issues or confirm it will work. This shifts XO use from brainstorming to validation.
- **Key Prerequisites:**
  - T01.G3.01
  - T02.G3.01
  - T03.G3.01
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T11.G3.01
  - T13.G3.01

#### T24.G3.02: Get improvement suggestions from XO, then decide

- **Grade:** 3
- **Total Dependencies:** 7
- **Integrates Topics:** T01, T02, T03, T06, T11, T13 (6 topics)
- **Description:** After completing a simple project or feature, a student asks XO "What could I improve?" and receives suggestions (e.g., "You could add sound," "You could make the movement smoother," "You could add a title screen"). The student picks one improvement they want to make, reinforcing their agency.
- **Key Prerequisites:**
  - T01.G3.01
  - T02.G3.01
  - T03.G3.01
  - T06.G3.01
  - T11.G3.01
  - T13.G3.01

#### T24.G3.03: Describe a bug to XO; try XO's suggestions before fixing it yourself

- **Grade:** 3
- **Total Dependencies:** 9
- **Integrates Topics:** T01, T02, T03, T06, T07, T08, T11, T13 (8 topics)
- **Description:** When a student encounters a bug (e.g., "My sprite is stuck in a corner"), they describe it to XO (not paste full code, just explain) and ask for hints on what to check. XO might suggest "Check if you're resetting the position" or "Look at your loop condition." The student tries these hints. If a hint doesn't work, they continue debugging independently, learning that XO is a guide, not a solution.
- **Key Prerequisites:**
  - T01.G3.01
  - T02.G3.01
  - T03.G3.01
  - T06.G3.01
  - T07.G3.01
  - T08.G3.01
  - T11.G3.01
  - T13.G3.01

#### T24.G4.01: Ask XO if your code is well-organized

- **Grade:** 4
- **Total Dependencies:** 10
- **Integrates Topics:** T01, T02, T03, T05, T06, T08, T11, T12, T13 (9 topics)
- **Description:** A student writes or pastes a short script and asks XO "Is this organized well?" or "Could I use a custom block here?" XO suggests refactoring opportunities. The student decides whether to adopt the suggestion based on understanding (not blind acceptance).
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T11.G4.01
  - T12.G4.01

#### T24.G4.02: Discuss design choices with XO, then justify your decision

- **Grade:** 4
- **Total Dependencies:** 10
- **Integrates Topics:** T01, T02, T03, T05, T06, T07, T08, T11, T13 (9 topics)
- **Description:** After completing a project, a student asks XO "Why is my solution good?" or "Are there trade-offs I should know about?" XO explains pros and cons of the student's approach. The student then articulates their reasoning: "I used a loop because it's shorter" or "I used if/else because it's clearer to me." This reinforces that coding decisions involve values (clarity, efficiency, simplicity) and that the student's voice matters.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G4.01
  - T07.G4.01
  - T08.G4.01
  - T11.G4.01

#### T24.G4.03: Recognize when XO doesn't know the answer

- **Grade:** 4
- **Total Dependencies:** 9
- **Integrates Topics:** T01, T02, T03, T05, T06, T08, T11, T13 (8 topics)
- **Description:** Students learn that XO sometimes gives generic answers or slightly incorrect suggestions, especially for CreatiCode-specific features or edge cases. They practice saying "That suggestion doesn't fit my project" or asking a peer/teacher instead. This builds critical thinking and prevents over-reliance on AI.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G4.01
  - T08.G4.01
  - T11.G4.01
  - T13.G4.01

#### T24.G5.01: Ask XO about algorithm efficiency

- **Grade:** 5
- **Total Dependencies:** 14
- **Integrates Topics:** T01, T02, T03, T05, T06, T07, T08, T09, T10, T11, T12, T13 (12 topics)
- **Description:** Given multiple ways to solve a problem (e.g., two different loop structures, two different variable organizations), a student asks XO "Which is better and why?" XO explains trade-offs (clarity vs. speed, etc.). The student then decides based on their project needs.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G5.01
  - T07.G5.01
  - T08.G5.01
  - T09.G5.01

#### T24.G5.02: Create a project plan with XO, then document your decisions

- **Grade:** 5
- **Total Dependencies:** 10
- **Integrates Topics:** T01, T02, T03, T05, T06, T08, T11, T13 (8 topics)
- **Description:** A student asks XO for a detailed project plan (e.g., all steps to make a platformer game), receives the outline, follows it while taking notes on why they chose each step or what they changed. They then write a brief project report documenting their decisions and how they differ from XO's suggestion.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G5.01
  - T08.G5.01
  - T11.G4.01
  - T13.G4.01

#### T24.G5.03: Combine feedback from XO, peer, and your own testing

- **Grade:** 5
- **Total Dependencies:** 9
- **Integrates Topics:** T01, T02, T03, T05, T06, T11, T13 (7 topics)
- **Description:** After completing a feature or project, a student gathers feedback from XO ("What do you think of this?"), a peer ("Does it work well?"), and their own testing ("Does it do what I want?"). They analyze all three inputs and decide what to change based on their priorities.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G5.01
  - T11.G4.01
  - T13.G4.01
  - T13.G5.01

#### T24.G5.04: Recognize bias or limitations in XO's suggestions

- **Grade:** 5
- **Total Dependencies:** 11
- **Integrates Topics:** T01, T02, T03, T05, T06, T07, T08, T11, T13 (9 topics)
- **Description:** Students learn that XO may favor certain approaches (e.g., always suggest a loop even when if/else is simpler, or not know about CreatiCode-specific blocks). They practice saying "This suggestion doesn't fit my project" and explaining why. This builds metacognitive awareness.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G5.01
  - T07.G5.01
  - T08.G5.01
  - T11.G4.01

#### T24.G6.01: Ask XO for algorithm design help

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T01, T02, T03, T05, T06, T10, T11, T12, T13 (9 topics)
- **Description:** Given a complex task (e.g., "How do I search a list for a value?"), a student asks XO for a conceptual outline or pseudocode, not full code. XO provides steps. The student implements it and documents where their code came from. This combines AI assistance with student problem-solving.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G6.01
  - T10.G6.01
  - T11.G4.01
  - T12.G6.01

#### T24.G6.02: Cross-check XO advice with documentation or peers

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T01, T02, T03, T05, T06, T08, T11, T12, T13 (9 topics)
- **Description:** When XO suggests a solution, a student learns to verify it: "Does the CreatiCode docs say this is right?" or "Does this match what my peer said?" This prevents adopting incorrect or outdated advice.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G6.01
  - T08.G6.01
  - T11.G4.01
  - T12.G6.01

#### T24.G6.03: Ask XO to explain code and assess the explanation

- **Grade:** 6
- **Total Dependencies:** 11
- **Integrates Topics:** T01, T02, T03, T05, T06, T08, T11, T12, T13 (9 topics)
- **Description:** A student pastes a short script (their own or a peer's) and asks XO "What does this do?" XO explains the logic. The student assesses: "Is that right?" by tracing the code or testing it. If there's a mismatch, they ask a follow-up question or correct XO.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G6.01
  - T08.G6.01
  - T11.G4.01
  - T12.G6.01

#### T24.G6.04: Balance XO assistance with peer collaboration and independent work

- **Grade:** 6
- **Total Dependencies:** 10
- **Integrates Topics:** T01, T02, T03, T05, T06, T11, T12, T13 (8 topics)
- **Description:** Students learn that a healthy project workflow includes asking XO (for big ideas), collaborating with peers (for diverse perspectives), and working alone (for deep understanding). They practice deciding which mode to use when.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G6.01
  - T11.G4.01
  - T12.G6.01
  - T13.G4.01

#### T24.G7.01: Ask XO about edge cases and robustness

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T01, T02, T03, T05, T06, T10, T11, T12, T13 (9 topics)
- **Description:** Before or after implementing a solution, a student asks XO "What edge cases might break my code?" or "How do I make my solution more robust?" XO suggests cases (negative numbers, empty lists, etc.). The student tests or implements guards against them.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G7.01
  - T10.G7.01
  - T11.G4.01
  - T12.G7.01

#### T24.G7.02: Discuss trade-offs: speed vs. clarity with XO

- **Grade:** 7
- **Total Dependencies:** 13
- **Integrates Topics:** T01, T02, T03, T05, T06, T07, T09, T11, T12, T13 (10 topics)
- **Description:** Students understand that many coding decisions involve trade-offs (a loop is faster but a function call is clearer; a variable is flexible but a constant is predictable). They ask XO "Which is better for my goal?" and make informed choices based on their priorities.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G7.01
  - T07.G7.01
  - T09.G7.01
  - T11.G4.01

#### T24.G7.03: Use XO to refactor and improve existing code

- **Grade:** 7
- **Total Dependencies:** 13
- **Integrates Topics:** T01, T02, T03, T05, T06, T08, T09, T11, T12, T13 (10 topics)
- **Description:** After completing a working solution, a student shows it to XO and asks "How could I make this better?" XO suggests refactoring (extract a function, use a data structure, simplify a condition). The student implements one or two suggestions and documents why.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G7.01
  - T08.G7.01
  - T09.G7.01
  - T11.G4.01

#### T24.G7.04: Critique XO's suggestions against your priorities

- **Grade:** 7
- **Total Dependencies:** 11
- **Integrates Topics:** T01, T02, T03, T05, T06, T10, T11, T12, T13 (9 topics)
- **Description:** XO might suggest a sophisticated optimization or feature that's technically sound but doesn't align with a student's project goals (e.g., XO suggests a complex sorting algorithm when the student's list is tiny, or XO suggests a 3D feature when the project is 2D). Students learn to say "That's smart, but not what I need for this project" and explain why.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G7.01
  - T10.G7.01
  - T11.G4.01
  - T12.G7.01

#### T24.G8.01: Use XO to help document a complex project

- **Grade:** 8
- **Total Dependencies:** 10
- **Integrates Topics:** T01, T02, T03, T05, T06, T11, T12, T13 (8 topics)
- **Description:** After completing a multi-feature project, a student shows XO the code and asks "Help me write clear documentation for a peer to understand this." XO provides a structured outline (overview, features, code breakdown). The student refines it with their own details and perspective, creating a hybrid human-AI document.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G8.01
  - T11.G4.01
  - T12.G8.01
  - T13.G4.01

#### T24.G8.02: Reflect on your coding decisions with XO's help

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T01, T02, T03, T05, T06, T07, T08, T11, T12, T13 (10 topics)
- **Description:** A student completes a project and asks XO "What strengths do you see in my code?" or "What would I improve if I had more time?" XO provides feedback. The student integrates this with their own self-assessment ("I was proud that I used a loop to reduce repetition. Next time, I'd…").
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G8.01
  - T07.G8.01
  - T08.G8.01
  - T11.G4.01

#### T24.G8.03: Ask XO to help debug by explaining your hypothesis

- **Grade:** 8
- **Total Dependencies:** 12
- **Integrates Topics:** T01, T02, T03, T05, T06, T07, T08, T11, T12, T13 (10 topics)
- **Description:** Before diving into code, a student tells XO their hypothesis about a bug ("I think the sprite is stuck because the loop never ends"). XO helps them design a test (add a print statement, add a timer, etc.). The student tests and reports back. This combines logical reasoning with AI-assisted verification.
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G8.01
  - T07.G8.01
  - T08.G8.01
  - T11.G4.01

#### T24.G8.04: Recognize and mitigate limitations of XO-assisted code

- **Grade:** 8
- **Total Dependencies:** 10
- **Integrates Topics:** T01, T02, T03, T05, T06, T11, T12, T13 (8 topics)
- **Description:** Sometimes XO-generated code or suggestions work but aren't ideal (inefficient, unclear, not fully correct). Grade 8 students learn to review code XO suggests, test it thoroughly, and either adopt it with understanding or revise it. They practice the principle: "AI is a tool, not an authority."
- **Key Prerequisites:**
  - T01.G4.01
  - T02.G4.01
  - T03.G4.01
  - T05.G4.01
  - T06.G8.01
  - T11.G4.01
  - T12.G8.01
  - T13.G4.01


---

## Capstones by Grade Level

### Grade 3 (40 capstones)

- **T14.G3.01**: Create a title screen and a start button (8 deps)
- **T14.G3.02**: End the game with a game over screen (8 deps)
- **T14.G3.03**: Use a loop to repeatedly spawn enemies (8 deps)
- **T14.G3.04**: Check multiple win/loss conditions (8 deps)
- **T15.G3.01**: Animate on command (click or key) (8 deps)
- ... and 35 more

### Grade 4 (41 capstones)

- **T14.G4.01**: Detect different types of collisions (10 deps)
- **T14.G4.02**: Implement simple AI movement for enemies (10 deps)
- **T14.G4.03**: Use a timer or counter for paced events (11 deps)
- **T14.G4.04**: Refactor game code for clarity (14 deps)
- **T15.G4.01**: State-based character animation (12 deps)
- ... and 36 more

### Grade 5 (43 capstones)

- **T14.G5.01**: Implement a scrolling camera for larger worlds (10 deps)
- **T14.G5.02**: Create enemy waves or spawning patterns (12 deps)
- **T14.G5.03**: Track game statistics (kills, time, accuracy) (11 deps)
- **T15.G5.01**: Complex character state machine (12 deps)
- **T15.G5.02**: Multi‑subplot story with branching paths (13 deps)
- ... and 38 more

### Grade 6 (44 capstones)

- **T14.G6.01**: Design a game state machine (12 deps)
- **T14.G6.02**: Implement pixel‑perfect or grid‑based collision (12 deps)
- **T14.G6.03**: Use data structures to manage game objects (13 deps)
- **T14.G6.04**: Debug game logic systematically (12 deps)
- **T15.G6.01**: Design and trace character state diagrams (11 deps)
- ... and 39 more

### Grade 7 (44 capstones)

- **T14.G7.01**: Simulate physics: gravity and jumping (5 deps)
- **T14.G7.02**: Implement simple pathfinding (waypoints or A*) (11 deps)
- **T14.G7.03**: Optimize collision checking to avoid lag (12 deps)
- **T14.G7.04**: Analyze and balance game difficulty (13 deps)
- **T15.G7.01**: Implement a scene graph or scene manager (12 deps)
- ... and 39 more

### Grade 8 (44 capstones)

- **T14.G8.01**: Architect a game using modular custom blocks (12 deps)
- **T14.G8.02**: Implement a particle system (visual effects) (13 deps)
- **T14.G8.03**: Design game levels using data structures (13 deps)
- **T14.G8.04**: Document and analyze a complete game system (12 deps)
- **T15.G8.01**: Implement a narrative engine with state and dialogue data (13 deps)
- ... and 39 more

## Assessment Recommendations

### Using Capstone Skills for Assessment

1. **Project-Based Assessment:** Capstone skills naturally lend themselves to project-based evaluation
2. **Rubric Development:** Create rubrics that assess integration of prerequisite skills
3. **Portfolio Evidence:** Students can demonstrate mastery through completed projects
4. **Peer Review:** Complex projects benefit from collaborative critique

### Sample Assessment Framework

For each capstone skill:

1. **Planning Phase:**
   - Can student identify required skills?
   - Do they decompose the problem effectively?
   - Is the project plan realistic?

2. **Implementation Phase:**
   - Do they apply prerequisite skills correctly?
   - Is code organized and maintainable?
   - Do they debug systematically?

3. **Refinement Phase:**
   - Do they test comprehensively?
   - Can they iterate based on feedback?
   - Is the final product polished?

4. **Reflection Phase:**
   - Can they explain their design choices?
   - Do they identify areas for improvement?
   - Can they connect to broader concepts?

### Suggested Capstone Projects by Grade

**Grade 5:**
- Multi-level 2D game with scoring and collision detection
- Interactive story with branching narratives
- Simple UI app with form validation

**Grade 6:**
- Physics simulation demonstrating scientific concepts
- AI-powered media generation tool
- Multi-scene animation with custom transitions

**Grade 7:**
- 3D world exploration game
- Multiplayer turn-based strategy game
- AI chatbot with context awareness

**Grade 8:**
- Complete game with AI opponents
- Voice/vision interface for accessibility
- Meta-project using XO for code generation and optimization

---

**Total capstone skills:** 256
