# T06 – Events & Sequencing in Programs: K–8 Skill List (v2, IXL‑Style Microsteps)

Topic reference: `T06 Events & Sequencing in Programs` in `domains_topics_overview.md`  
Domain: Programming Core (D2) · Primary CSTA focus: PRO‑PF (with links to ALG‑AF, PRO‑PD)

This v2 version refines the original draft (`skills_T06_events.md`) into an **IXL‑style microstep design**:

- **Role of T06:** Core **event** and **sequence** gateway topic: how programs start, how scripts are triggered, and how actions run in order and in response to inputs or messages.  
- **Microsteps:** Each skill focuses on a small idea (recognize triggers, build tiny event scripts, trace order of actions, coordinate multiple events, design broadcasts, state machines) instead of broad “build a full game” tasks.  
- **Uneven density:** The heaviest concentration is in **Grade 3–5**, matching the spec that G3 events are a gateway skill; K–2 are conceptual, 6–8 focus on architecture, refactoring, and debugging.  
- **Implementability:** All skills are CreatiCode‑friendly: small code snippets, starter projects, and auto‑graders for behavior and structure.

IDs follow `T06.G<grade>.<nn>`. v1 IDs are preserved conceptually; new microsteps use higher `<nn>` values.

---

## Grade K (PreK–K) – “When I Click, It Starts”

Strands: **K‑A Recognize triggers**, **K‑B Simple sequences**

### K‑A: Recognize triggers

**T06.GK.01 – Spot what starts the program**  
Students identify the green flag or start button as the control that makes the project run.  
_Format:_ Picture of the stage and UI; students click the start control. · _CSTA:_ EK‑PRO‑PF‑01.

**T06.GK.02 – Match everyday “when” events to actions**  
Students match simple everyday events (“when door opens,” “when bell rings”) to what happens next.  
_Format:_ Drag event cards to action cards; auto‑graded. · _CSTA:_ EK‑PRO‑PF‑01, EK‑ALG‑AF‑01.

### K‑B: Simple sequences

**T06.GK.03 – Order 3 sprite actions to match a story**  
Students arrange 3 action pictures (move, say, jump) to match a simple story about a sprite.  
_Format:_ Drag‑drop ordering; auto‑graded. · _CSTA:_ EK‑PRO‑PF‑01.

**T06.GK.04 – Match a tiny script to a picture sequence**  
Students match a 2–3 block script (start → move → say) to a 3‑panel picture.  
_Format:_ Picture + 2–3 scripts; MCQ. · _CSTA:_ EK‑PRO‑PF‑01, EK‑ALG‑AF‑01.

---

## Grade 1 – Build and Trace Single‑Event Sequences

Strands: **1‑A Build green‑flag scripts**, **1‑B Trace & predict**

### 1‑A: Build green‑flag scripts

**T06.G1.01 – Build a 3–4 block script that runs on green flag**  
Students create a short script starting with green flag and add movement/say/wait blocks in order.  
_Format:_ Coding in a starter project; auto‑graded by blocks and behavior. · _CSTA:_ E1‑PRO‑PF‑01.

**T06.G1.02 – Extend a script with one more action**  
Students add one specified action (e.g., “then say bye”) at the correct place in an existing green‑flag script.  
_Format:_ Edit script; auto‑graded. · _CSTA:_ E1‑PRO‑PF‑01.

### 1‑B: Trace & predict

**T06.G1.03 – Trace a 3–4 block script and pick the final picture**  
Students read a short script and choose which picture shows the final sprite state.  
_Format:_ Code‑reading + image MCQ; auto‑graded. · _CSTA:_ E1‑PRO‑PF‑01, E1‑ALG‑AF‑01.

**T06.G1.04 – Number blocks to show execution order**  
Students see a small script and drag numbers 1, 2, 3… onto blocks to show top‑to‑bottom order.  
_Format:_ Numbering interaction; auto‑graded. · _CSTA:_ E1‑PRO‑PF‑01.

---

## Grade 2 – More Triggers and Multi‑Script Projects (Conceptual Bridge)

Strands: **2‑A Different kinds of events**, **2‑B Multiple scripts in one sprite**

> Note: Grade 2 is primarily conceptual; heavy code building starts in Grade 3.

### 2‑A: Different kinds of events

**T06.G2.01 – Match event blocks to user actions**  
Students match event blocks like “when green flag clicked,” “when space key pressed,” “when this sprite clicked” to pictures of those actions.  
_Format:_ Drag‑match; auto‑graded. · _CSTA:_ E2‑PRO‑PF‑01.

**T06.G2.02 – Decide which event fits a scenario**  
Students read simple scenarios (“start game,” “jump when space pressed”) and choose the correct event block.  
_Format:_ Scenario + MCQ; auto‑graded. · _CSTA:_ E2‑PRO‑PF‑01.

### 2‑B: Multiple scripts in one sprite

**T06.G2.03 – Recognize that one sprite can have multiple scripts**  
Students see a sprite with two scripts (green‑flag, key press) and answer questions like “what happens when we press space vs click green flag?”  
_Format:_ Code‑reading + MCQ; auto‑graded. · _CSTA:_ E2‑PRO‑PF‑01.

**T06.G2.04 – Match each event to its outcome in a simple project**  
Students match listed events (green flag, key, click) to short descriptions of what happens when each occurs.  
_Format:_ Match events → descriptions; auto‑graded. · _CSTA:_ E2‑PRO‑PF‑01.

---

## Grade 3 – Gateway: Core Event‑Driven Coding

Strands: **3‑A Build basic event‑driven scripts**, **3‑B Coordinate events and sequences**, **3‑C Debug simple event issues**

### 3‑A: Build basic event‑driven scripts

**T06.G3.01 – Build a green‑flag script that runs a 3–5 block sequence**  
Students create a simple script triggered by green flag that performs a short sequence (movement, say, costume change).  
_Format:_ Coding, starter project; auto‑graded on structure and behavior. · _CSTA:_ E3‑PRO‑PF‑01. ⭐ Gateway

**T06.G3.02 – Build a key‑press script that controls a sprite**  
Students make a “when key pressed” script that moves a sprite in one direction.  
_Format:_ Coding; auto‑graded by behavior when pressing the key. · _CSTA:_ E3‑PRO‑PF‑01.

### 3‑B: Coordinate events and sequences

**T06.G3.03 – Decide which event type to use for a behavior**  
Students choose between green flag, key press, and sprite‑click events for simple tasks (“start game,” “jump,” “open door”).  
_Format:_ Scenario + MCQ; auto‑graded. · _CSTA:_ E3‑PRO‑PF‑01.

**T06.G3.04 – Trace a project with two events and predict outputs**  
Students see a program with green‑flag and key‑press scripts, then answer what happens if you only click green flag, only press key, and do both.  
_Format:_ Code‑reading + multiple questions; auto‑graded. · _CSTA:_ E3‑PRO‑PF‑01, E3‑ALG‑AF‑01.

### 3‑C: Debug simple event issues

**T06.G3.05 – Fix a script that is missing an event block**  
Students correct a script that has the right actions but no event head by adding the appropriate event block.  
_Format:_ Coding fix; auto‑graded by presence and behavior. · _CSTA:_ E3‑PRO‑PF‑01, E3‑PRO‑TR‑02.

**T06.G3.06 – Fix a behavior that runs at the wrong time**  
Students adjust which event triggers a script (e.g., move from green flag to key press) to match a story description.  
_Format:_ Edit event block; auto‑graded by observed behavior. · _CSTA:_ E3‑PRO‑PF‑01, E3‑PRO‑TR‑02.

---

## Grade 4 – Multiple Events per Sprite and Simple Broadcasts

Strands: **4‑A Multi‑script sprites**, **4‑B Intro to broadcasts**, **4‑C Debug multi‑event interactions**

### 4‑A: Multi‑script sprites

**T06.G4.01 – Build a sprite with several event handlers (green flag + keys)**  
Students create multiple scripts for the same sprite to respond to different keys and to the green flag.  
_Format:_ Coding in a starter project; auto‑graded by event set and behavior. · _CSTA:_ E4‑PRO‑PF‑01.

**T06.G4.02 – Trace which scripts run for different inputs**  
Students see multiple event scripts and determine which ones run when specific events happen.  
_Format:_ Code‑reading + MCQ; auto‑graded. · _CSTA:_ E4‑PRO‑PF‑01, E4‑ALG‑AF‑01.

### 4‑B: Intro to broadcasts

**T06.G4.03 – Recognize when a broadcast could connect sprites**  
Students see a project idea requiring coordination between sprites (e.g., “when player reaches goal, show next level”) and choose that a broadcast is appropriate.  
_Format:_ Scenario + MCQ; auto‑graded. · _CSTA:_ E4‑PRO‑PF‑01.

**T06.G4.04 – Match a broadcast send to its receivers**  
Students match `broadcast` blocks to `when I receive` scripts that respond to the same message.  
_Format:_ Matching interaction; auto‑graded. · _CSTA:_ E4‑PRO‑PF‑01.

### 4‑C: Debug multi‑event interactions

**T06.G4.05 – Fix a sprite that doesn’t respond because the event is wrong**  
Students change an event block so a sprite responds to the intended key/click.  
_Format:_ Coding fix; auto‑graded. · _CSTA:_ E4‑PRO‑TR‑02.

**T06.G4.06 – Fix a missing receiver for a broadcast**  
Students add a `when I receive` block to make a sprite react to a broadcast that is already sent.  
_Format:_ Coding fix; auto‑graded. · _CSTA:_ E4‑PRO‑TR‑02.

---

## Grade 5 – Coordinated Event‑Driven Systems

Strands: **5‑A Event patterns in games**, **5‑B Broadcast‑driven coordination**, **5‑C Event debugging & organization**

### 5‑A: Event patterns in games

**T06.G5.01 – Identify standard event patterns in a small game**  
Students label patterns like “start game,” “reset level,” “on collision,” “on score change” as specific event handlers in code.  
_Format:_ Code‑reading + labeling; auto‑graded. · _CSTA:_ E5‑PRO‑PF‑01.

**T06.G5.02 – Add a new event‑triggered behavior to an existing game**  
Students add a new key or click event that triggers a simple new action without breaking existing ones.  
_Format:_ Coding in existing project; auto‑graded. · _CSTA:_ E5‑PRO‑PF‑01.

### 5‑B: Broadcast‑driven coordination

**T06.G5.03 – Design a simple broadcast sequence for level start/end**  
Students configure broadcasts like “level‑start” and “level‑end” and connect them to sprites that show/hide or reset positions.  
_Format:_ Coding; auto‑graded by message names and responses. · _CSTA:_ E5‑PRO‑PF‑01.

**T06.G5.04 – Trace event and broadcast order for a scenario**  
Students follow a sequence of player actions and predict which scripts (events + broadcasts) run and in what rough order.  
_Format:_ Code‑reading with timeline; auto‑graded. · _CSTA:_ E5‑PRO‑PF‑01, E5‑ALG‑AF‑01.

### 5‑C: Event debugging & organization

**T06.G5.05 – Find and fix conflicting event scripts**  
Students debug a project where two event handlers interfere (e.g., two keys both move sprite at once) by changing events or conditions.  
_Format:_ Coding debugging challenge; auto‑graded. · _CSTA:_ E5‑PRO‑TR‑02.

**T06.G5.06 – Group scripts by event type to improve organization**  
Students reorganize scripts in a project (e.g., grouping movement events, UI events) and add comments describing each group.  
_Format:_ Refactor; auto‑graded by structure and comments. · _CSTA:_ E5‑PRO‑PF‑01, E5‑PRO‑PD‑02.

---

## Grade 6 – Analyze and Refactor Event‑Driven Control Flow

Strands: **6‑A Control‑flow analysis**, **6‑B Event refactoring & custom broadcasts**

### 6‑A: Control‑flow analysis

**T06.G6.01 – Trace event execution paths in a multi‑event program**  
Students analyze a program with several event handlers and broadcasts and determine which scripts run in response to different input sequences.  
_Format:_ Code‑reading with scenarios; auto‑graded. · _CSTA:_ MS‑PRO‑PF‑01.

**T06.G6.02 – Identify parallel vs sequential event behaviors**  
Students decide which scripts run “at the same time” vs one after another when events and broadcasts occur.  
_Format:_ MCQ based on code and timelines; auto‑graded. · _CSTA:_ MS‑PRO‑PF‑01.

### 6‑B: Event refactoring & custom broadcasts

**T06.G6.03 – Refactor event handlers for clarity and grouping**  
Students reorganize an existing project’s event scripts into clearer groups (movement, UI, scoring), adding comments and simplifying logic.  
_Format:_ Coding refactor; auto‑graded by structure and behavior equivalence. · _CSTA:_ MS‑PRO‑PF‑01, PRO‑PD‑02.

**T06.G6.04 – Design meaningful custom broadcasts and document them**  
Students replace generic “message1/message2” with semantic broadcasts (e.g., “player‑hit,” “game‑over”) and update listeners; they also fill in a small “event dictionary” describing each broadcast.  
_Format:_ Coding + template; auto‑graded. · _CSTA:_ MS‑PRO‑PF‑01, PRO‑PD‑02.

---

## Grade 7 – Event‑Driven Architecture and State Machines

Strands: **7‑A State machine patterns**, **7‑B Decoupled architectures & event protocols**

### 7‑A: State machine patterns

**T06.G7.01 – Model program states and transitions using events**  
Students sketch and implement states (menu, playing, paused, game‑over) and the events/broadcasts that move between them.  
_Format:_ Diagram + coding; auto‑graded by state definitions and transitions. · _CSTA:_ MS‑PRO‑PF‑01, PRO‑PD‑02.

**T06.G7.02 – Trace state changes in event‑driven code**  
Students read code that manages a state variable and events, then trace how state changes in response to inputs.  
_Format:_ Code‑reading + table; auto‑graded. · _CSTA:_ MS‑PRO‑PF‑01.

### 7‑B: Decoupled architectures & event protocols

**T06.G7.03 – Design a broadcast protocol to decouple components**  
Students plan which broadcasts communicate between subsystems (player, enemies, UI, score) and implement them.  
_Format:_ Planning table + coding; auto‑graded. · _CSTA:_ MS‑PRO‑PF‑01, PRO‑PD‑02.

**T06.G7.04 – Compare tightly coupled vs broadcast‑based designs**  
Students compare two designs and decide which is more modular and easier to change, explaining in terms of events vs direct references.  
_Format:_ MCQ + explanation; auto‑graded. · _CSTA:_ MS‑PRO‑PF‑01, PRO‑PD‑02.

---

## Grade 8 – Robust Event Systems, Edge Cases, and Documentation

Strands: **8‑A Robust event handling & edge cases**, **8‑B Event‑system documentation and review**

### 8‑A: Robust event handling & edge cases

**T06.G8.01 – Debug subtle event ordering and race conditions**  
Students debug projects where order of broadcasts or overlapping events leads to intermittent bugs and propose targeted fixes.  
_Format:_ Coding debugging challenge; auto‑graded with test cases. · _CSTA:_ MS‑PRO‑PF‑01, PRO‑TR‑14.

**T06.G8.02 – Design fallback behaviors for missed or repeated events**  
Students add guards or checks so programs behave reasonably even if events fire in unexpected ways (e.g., double clicks, missed start).  
_Format:_ Coding + explanation; auto‑graded by added conditions and behavior. · _CSTA:_ MS‑PRO‑PF‑01, PRO‑TR‑14.

### 8‑B: Event‑system documentation and review

**T06.G8.03 – Document the event protocol of a project**  
Students create a concise table or diagram listing events/broadcasts, senders, receivers, and purpose.  
_Format:_ Template completion; auto‑graded by coverage. · _CSTA:_ MS‑PRO‑PD‑02.

**T06.G8.04 – Review and critique an event design for clarity and maintainability**  
Students evaluate a project’s event structure, identifying confusing names, unnecessary events, or tight coupling, and suggest improvements.  
_Format:_ Checklist + short comments; auto‑graded by key issues found. · _CSTA:_ MS‑PRO‑PD‑02.

---

### Notes on Dependencies and Alignment

- K–2: T06 skills rely mainly on picture‑based understanding of sequence and basic program start (green flag); they connect to T01/T02 sequences and are conceptual pre‑coding.  
- G3–5: T06 is a **gateway** programming topic; dependencies should ensure core T06.G3 event skills unlock many later skills in loops (T07), conditionals (T08), and variables (T09). Within T06, microsteps progress from single events to coordination and broadcasts.  
- G6–8: T06 skills assume solid use of events and focus on analyzing, refactoring, and architecting event‑driven systems; they support project‑level topics (T14–T19) and debugging (T13) without blocking basic construct learning.  
- This design aligns with CSTA PRO‑PF and PRO‑PD expectations while keeping skills small, progressive, and CreatiCode‑implementable.

