# T19 – Multiplayer Apps: Grade 5–8 Skill List (Draft v3)

Topic reference: `T19 Multiplayer Apps` in `domains_topics_overview.md`
Domain: Applications & AI (D3) · CSTA focus: PRO‑PD, SAS‑NW (with links to PRO‑PF, ALG‑AF, CAS‑ET)

Each skill below includes:

- a stable **ID** (`T19.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (the targeted understanding/behavior),
- a **challenge format** (typical assessment interaction).

Where relevant, a primary **CSTA code** is noted.

> **Note:** Multiplayer implementation details are intentionally deferred until Grade 5 so that students have sufficient coding fluency and conceptual maturity. Grades K–4 focus on foundational CS ideas in other topics.

---

## Grade 5 – Multiplayer Basics (Lobby, Communication, Shared Goals)

### T19.G5.01 – Host or join a CreatiCode multiplayer lobby

- **Short name:** Create or join a lobby
- **Description:** Students use the `create game` and `join game` blocks to host a named room or connect to one by entering the game ID, password, and their player name. They read the status returned by each block (success, waiting for host, wrong password).
- **Challenge format:** Coding, guided practice. Starter project prints lobby status to a label. Prompt: “Host `SkyDash` with password `blue` as `Player1`, then join from a second instance.” Auto-grading confirms the exact lobby metadata and that the join succeeds only when parameters match.
- **CSTA:** PRO‑PD (Program development: using multiplayer APIs).

### T19.G5.02 – Build a ready-up indicator before the game starts

- **Short name:** Everyone clicks “Ready”
- **Description:** Students implement a button that broadcasts “ready” and adds the player’s name to a shared list. The host starts the game when all connected players have marked themselves ready.
- **Challenge format:** Coding, coordination task. Starter project tracks players but lacks ready logic. Auto-grading simulates three players toggling ready status and verifies the game only starts when the ready count equals the player count.
- **CSTA:** PRO‑PD (synchronization and control flow).

### T19.G5.03 – Implement shared quick chat or emote buttons

- **Short name:** Send chat or emotes to all players
- **Description:** Students add UI buttons (text presets or emotes) that broadcast a message to everyone and display it above each sprite or inside a chat log.
- **Challenge format:** Coding, feature build. Starter project includes blank buttons and a shared list. Auto-grading triggers button presses from multiple clients and checks that the same messages appear in every instance.
- **CSTA:** PRO‑PD (communication features in networked systems).

### T19.G5.04 – Display a synchronized scoreboard for the current session

- **Short name:** Shared score HUD
- **Description:** Students maintain a cloud or multiplayer variable that stores each player’s score. Whenever any player earns points, the scoreboard updates on every client within the same session ID.
- **Challenge format:** Coding, data task. Starter includes a list of `{player, score}` pairs but no update logic. Auto-grading awards points to different players and verifies that the HUD updates everywhere and resets when the session ID changes.
- **CSTA:** PRO‑PD (shared data management); SAS‑NW.

### T19.G5.05 – Diagnose and respond to connection status changes

- **Short name:** Handle waiting and error states
- **Description:** Students interpret the multiplayer status output (connecting, waiting for host, disconnected) and display appropriate guidance (e.g., “Waiting for host… please stay on this screen”). They retry joins or disable controls until a connection is restored.
- **Challenge format:** Coding + reasoning. Auto-grading injects status codes; students must update UI text and logic accordingly. Checks ensure controls remain disabled during disconnects.
- **CSTA:** PRO‑PD (robustness in interactive systems).

---

## Grade 6 – Shared Worlds, Synchronization, and Latency Awareness

### T19.G6.01 – Synchronize player movement and orientation

- **Short name:** Keep avatars aligned online
- **Description:** Students publish their sprite’s x, y, and facing direction whenever it changes and update remote clones when new data arrives. They ensure motion feels identical on all screens.
- **Challenge format:** Coding, movement sync challenge. Auto-grading moves a sprite in one client and confirms the second client mirrors position and direction within a tolerance.
- **CSTA:** PRO‑PD (state synchronization).

### T19.G6.02 – Maintain shared world objects with persistent state

- **Short name:** Shared objects stay collected
- **Description:** Students track world objects (coins, doors, hazards) using a stage-level structure (list/dictionary). When a player interacts with an object, they update the shared structure and broadcast the change so all clients agree, including late joiners.
- **Challenge format:** Coding, systems build. Auto-grading collects objects in one client and ensures they disappear everywhere, including for a newly joined spectator.
- **CSTA:** PRO‑PD (shared world state management).

### T19.G6.03 – Build a cooperative puzzle with shared progress counters

- **Short name:** Solve it together
- **Description:** Students design a task where multiple players must contribute to shared goals (e.g., both press switches). They maintain counters and display progress for all players.
- **Challenge format:** Coding, co-op design. Auto-grading simulates players activating switches and validates that the shared counter unlocks the win state.
- **CSTA:** PRO‑PD (collaborative mechanics).

### T19.G6.04 – Handle player join/leave events and late joiners

- **Short name:** Welcome new players and clean up
- **Description:** Students respond to join/leave events to spawn or remove sprites, send welcome messages, and replay recent game state so late joiners catch up quickly.
- **Challenge format:** Coding, event handling. Auto-grading simulates players joining mid-round and disconnecting; checks ensure UI updates and cleanup occur consistently.
- **CSTA:** PRO‑PD (event-driven multiplayer).

### T19.G6.05 – Smooth latency with buffering or interpolation

- **Short name:** Reduce jitter from delayed packets
- **Description:** Students measure the delay between updates and implement interpolation or short buffers so remote sprites glide smoothly even when packets arrive late.
- **Challenge format:** Coding + concept. Auto-grading injects artificial latency and inspects whether motion remains smooth while students explain their approach in a short response.
- **CSTA:** PRO‑PD (robust real-time systems); SAS‑NW.

---

## Grade 7 – Fairness, Scaling, and Network Efficiency

### T19.G7.01 – Balance starting conditions and scoring

- **Short name:** Make the game fair
- **Description:** Students audit spawn points, turn order, and scoring rules to eliminate built-in advantages. They document how each change improves fairness.
- **Challenge format:** Coding + reflection. Auto-grading checks code for randomized spawns or alternating turns and reviews a short justification.
- **CSTA:** PRO‑PD; CAS‑ET (ethical design).

### T19.G7.02 – Implement dynamic team assignment or matchmaking

- **Short name:** Auto-build balanced teams
- **Description:** Students automatically assign players to teams or lobbies based on join order, rank, or availability, ensuring balanced team sizes.
- **Challenge format:** Coding, algorithmic. Auto-grading simulates multiple join sequences and checks resulting team lists.
- **CSTA:** PRO‑PD (algorithmic player management).

### T19.G7.03 – Decide what data syncs vs stays local

- **Short name:** Optimize network traffic
- **Description:** Students label project variables as “sync every frame,” “sync on event,” or “local only,” and adjust scripts accordingly to reduce bandwidth without hurting gameplay.
- **Challenge format:** Concept + coding. Auto-grading checks tagging accuracy and that unnecessary sync messages were removed.
- **CSTA:** PRO‑PD; SAS‑NW (systems optimization).

### T19.G7.04 – Scale logic to handle variable player counts

- **Short name:** Works with 2–8 players
- **Description:** Students refactor scripts to loop over the player list when instantiating sprites, updating HUDs, or distributing objectives so the game behaves consistently regardless of player count.
- **Challenge format:** Coding, scalability task. Auto-grading runs the project with random player counts and verifies correct behavior.
- **CSTA:** PRO‑PD (scalable systems).

### T19.G7.05 – Display connection quality and apply fallbacks

- **Short name:** Show when the connection is weak
- **Description:** Students calculate basic latency (if supported) or detect delayed messages, display an indicator (e.g., Wi-Fi bars), and slow gameplay or pause when conditions deteriorate.
- **Challenge format:** Coding, resilience feature. Auto-grading injects lag and checks that indicators appear and fallback logic runs.
- **CSTA:** PRO‑PD; SAS‑NW.

---

## Grade 8 – Security, Persistence, and Architecture Choices

### T19.G8.01 – Implement host-authoritative validation to prevent cheating

- **Short name:** Host confirms every score
- **Description:** Students restructure scoring so clients request changes but only the host (or server role) validates and applies them, rejecting impossible moves or rapid repeats.
- **Challenge format:** Coding, security feature. Auto-grading attempts to cheat by sending fake updates and verifies that the host rejects them.
- **CSTA:** PRO‑PD (secure program design); SAS‑NW.

### T19.G8.02 – Trace message ordering and resolve inconsistencies

- **Short name:** Fix out-of-order updates
- **Description:** Students analyze logs containing timestamps and sequence IDs from multiple clients, identify where state diverged, and add ordering checks (sequence numbers, acknowledgements) to prevent issues.
- **Challenge format:** Concept + coding. Auto-grading checks the explanation plus whether new ordering checks prevent the logged issue from recurring.
- **CSTA:** PRO‑PD (reasoning about concurrency and distributed state).

### T19.G8.03 – Persist match data to CreatiCode cloud storage

- **Short name:** Save match history
- **Description:** Students store final scores, MVP stats, or unlocks using persistent cloud variables/lists, then load them in the next session to show long-term progress.
- **Challenge format:** Coding, integration. Auto-grading plays two matches and verifies that the second run shows prior results.
- **CSTA:** PRO‑PD; DAA‑DI (data persistence).

### T19.G8.04 – Explain the architecture of their multiplayer system

- **Short name:** Diagram client/server flow
- **Description:** Students create an architecture diagram showing input capture, host/server processing, message broadcast, and UI updates. They identify potential bottlenecks and propose mitigations (sharding, simplified messages).
- **Challenge format:** Concept, architecture write-up. Auto-grading uses a rubric for completeness and accuracy.
- **CSTA:** PRO‑PD; SAS‑NW.

### T19.G8.05 – Compare CreatiCode multiplayer (`mp`) and peer-to-peer (`p2p`) extensions

- **Short name:** Pick the right multiplayer mode
- **Description:** Students experiment with both the standard multiplayer extension and the peer-to-peer (`p2p`) extension (message-only, Nengi/3D modes). They document trade-offs such as latency, authority, and scalability, and recommend which extension fits a given game concept.
- **Challenge format:** Concept + coding exploration. Auto-grading checks for evidence (logs/screenshots) from both modes and evaluates the written comparison.
- **CSTA:** PRO‑PD; SAS‑NW (architecture evaluation).

---

## Summary

By delaying multiplayer specifics until Grade 5, students arrive with foundational programming skills and can concentrate on the nuanced behaviors required for reliable multiplayer games. Grades 5–6 introduce lobby flow, shared state, and latency mitigation; Grades 7–8 emphasize fairness, scalability, security, persistence, and architectural reasoning—mirroring the increasing sophistication expected in CreatiCode projects and competitions.
