# Grade 6 Dependency Fixes - Change Log

**Generated:** 2025-11-24

## Summary

- **Circular dependency fixes:** 2
- **Missing cross-topic dependencies added:** 192
- **Total skills modified:** 194

## Part 1: Circular Dependency Fixes (CRITICAL)

### CIRC-001: T07.G6.09

**Action:** Remove circular dependency

**Dependency removed:** `T07.G6.03`

**Rationale:** For-each loops are a foundational looping construct. Loop-based search is an application of loops. Students should learn for-each loops BEFORE applying them to search tasks.

**Dependencies before:**
- `T07.G5.02`
- `T07.G6.03`
- `T10.G5.01`

**Dependencies after:**
- `T07.G5.02`
- `T10.G5.01`

---

### CIRC-002: T07.G6.08

**Action:** Remove circular dependency

**Dependency removed:** `T07.G6.04`

**Rationale:** Students need to understand the problem (infinite loops) before learning the solution (break/continue). Understanding infinite loops doesn't require knowing about break/continue.

**Dependencies before:**
- `T07.G5.02`
- `T07.G6.03`
- `T07.G6.04`

**Dependencies after:**
- `T07.G5.02`
- `T07.G6.03`

---

## Part 2: Missing Cross-Topic Dependencies

### Topic T19 (55 skills)

#### T19.G6.00A: Understand what "multiplayer" means in CreatiCode games (deeper dive)

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G5.03`, `T19.G5.04`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T19.G5.03`, `T19.G5.04`

---

#### T19.G6.00B: Understand the host-client model and game rooms in depth

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G5.04`, `T19.G6.00A`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T19.G5.04`, `T19.G6.00A`

---

#### T19.G6.00C: Understand sprite replication in multiplayer games

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G6.00B`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T19.G6.00B`

---

#### T19.G6.00C2: Understand how code runs on original vs replicate sprites

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G6.00C`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T19.G6.00C`

---

#### T19.G6.00D: Understand Dynamic vs Static sprites in multiplayer games

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G6.00B`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T19.G6.00B`

---

#### T19.G6.00E: Understand collision shapes (Rectangle vs Circle) in multiplayer games

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G6.00B`, `T14.G5.01`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T14.G5.01`, `T19.G6.00B`

---

#### T19.G6.00F: Understand synchronization mechanisms in depth

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G5.05`, `T19.G6.00C`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T19.G5.05`, `T19.G6.00C`

---

#### T19.G6.00G: Understand what lag and latency mean in multiplayer games

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G6.00F`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T19.G6.00F`

---

#### T19.G6.00H: Understand what servers are in multiplayer games

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G6.00B`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T19.G6.00B`

---

#### T19.G6.00I: Understand what roles are in multiplayer games

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G6.00B`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T19.G6.00B`

---

#### T19.G6.00J: Understand display names and game names

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G6.00B`

**Dependencies after:** `T05.G5.01`, `T10.G5.01`, `T19.G6.00B`

---

#### T19.G6.00K: Distinguish multiplayer games from cloud variables

**Dependencies added:** `T05.G5.01`, `T10.G5.01`

**Rationale:** Multiplayer concepts require understanding variables (for state) and events (for networking)

**Dependencies before:** `T19.G6.00B`, `T09.G5.01`

**Dependencies after:** `T05.G5.01`, `T09.G5.01`, `T10.G5.01`, `T19.G6.00B`

---

#### T19.G6.01A: Create a simple multiplayer game room

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.00B`, `T19.G6.00H`, `T19.G6.00I`, `T19.G6.00J`, `T08.G4.01`

**Dependencies after:** `T05.G5.01`, `T08.G4.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.00B`, `T19.G6.00H`, `T19.G6.00I` ... (9 total)

---

#### T19.G6.01B: Join a multiplayer game room

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.01A`, `T19.G6.00H`, `T19.G6.00I`, `T19.G6.00J`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.00H`, `T19.G6.00I`, `T19.G6.00J`, `T19.G6.01A`

---

#### T19.G6.01C: Configure game capacity (maximum players)

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.00B`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.00B`

---

#### T19.G6.01C2: Configure multiplayer world dimensions (width and height)

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.00B`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.00B`

---

#### T19.G6.01C3: Handle capacity limits and "game full" scenarios

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.01C`, `T19.G6.01D`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.01C`, `T19.G6.01D`

---

#### T19.G6.01D: List available multiplayer games in a table

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.00B`, `T19.G6.00H`, `T09.G5.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T09.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.00B`, `T19.G6.00H`

---

#### T19.G6.01E: List players in a game room

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.01B`, `T09.G5.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T09.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.01B`

---

#### T19.G6.01F: Check connection status and display feedback

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.01B`, `T08.G4.01`

**Dependencies after:** `T05.G5.01`, `T08.G4.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.01B`

---

#### T19.G6.01G: Test a multiplayer game with two browser windows

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.01B`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.01B`

---

#### T19.G6.02A: Understand sprite registration purpose

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.00C`, `T19.G6.00D`, `T19.G6.00E`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.00C`, `T19.G6.00D`, `T19.G6.00E`

---

#### T19.G6.02B: Register sprites with the game server

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.02A`, `T19.G6.01B`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.01B`, `T19.G6.02A`

---

#### T19.G6.02C: Initialize sprites when they join using "when added to game"

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.02B`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.02B`

---

#### T19.G6.03A: Create a simple 2-player racing game (DEPRECATED - use sub-skills)

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03A.04`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03A.04`

---

#### T19.G6.03A.01: Set up multiplayer racing game structure

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.01G`, `T19.G6.02B`, `T19.G6.02C`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.01G`, `T19.G6.02B`, `T19.G6.02C`

---

#### T19.G6.03A.02: Implement synchronized racing controls

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03A.01`, `T19.G6.05A`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03A.01`, `T19.G6.05A`

---

#### T19.G6.03A.03: Add finish line and collision detection

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03A.02`, `T19.G6.06`, `T19.G6.07`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03A.02`, `T19.G6.06`, `T19.G6.07`

---

#### T19.G6.03A.04: Determine and display race winner

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03A.03`, `T19.G6.04C`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03A.03`, `T19.G6.04C`

---

#### T19.G6.03B: Create a 2-player cooperative game (DEPRECATED - use sub-skills)

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03B.04`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03B.04`

---

#### T19.G6.03B.01: Design cooperative game objective

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.03A.04`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.03A.04`

---

#### T19.G6.03B.02: Implement individual player actions

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03B.01`, `T19.G6.02B`, `T19.G6.05A`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.02B`, `T19.G6.03B.01`, `T19.G6.05A`

---

#### T19.G6.03B.03: Add shared progress tracking

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03B.02`, `T19.G6.08`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03B.02`, `T19.G6.08`

---

#### T19.G6.03B.04: Broadcast cooperation events and check win condition

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03B.03`, `T19.G6.04C`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03B.03`, `T19.G6.04C`

---

#### T19.G6.03C: Add collision-based tag game mechanic (DEPRECATED - use sub-skills)

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03C.04`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03C.04`

---

#### T19.G6.03C.01: Detect player-to-player collisions

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.03A.04`, `T19.G6.06`, `T19.G6.07`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.03A.04`, `T19.G6.06`, `T19.G6.07`

---

#### T19.G6.03C.02: Track and broadcast "it" status

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03C.01`, `T19.G6.04C`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03C.01`, `T19.G6.04C`

---

#### T19.G6.03C.03: Add visual indicators for "it" status

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03C.02`, `T19.G6.04B`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03C.02`, `T19.G6.04B`

---

#### T19.G6.03C.04: Polish and test tag game mechanics

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Player interactions need variables for state, events for actions, lists for multiple players

**Dependencies before:** `T19.G6.03C.03`, `T19.G6.12`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.03C.03`, `T19.G6.12`

---

#### T19.G6.04A: Choose between "All Sprites" and "Exclude Replicate" broadcast modes

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Synchronization requires variables for shared state, events for updates, lists for data

**Dependencies before:** `T19.G6.00C`, `T06.G4.01`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.00C`

---

#### T19.G6.04B: Receive and handle multiplayer broadcast messages

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Synchronization requires variables for shared state, events for updates, lists for data

**Dependencies before:** `T06.G4.01`, `T19.G6.02C`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.02C`

---

#### T19.G6.04C: Broadcast multiplayer messages with parameters

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Synchronization requires variables for shared state, events for updates, lists for data

**Dependencies before:** `T19.G6.04A`, `T19.G6.04B`, `T11.G5.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T11.G5.01`, `T19.G6.04A`, `T19.G6.04B`

---

#### T19.G6.04D: Access and use broadcast message parameters

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Synchronization requires variables for shared state, events for updates, lists for data

**Dependencies before:** `T19.G6.04C`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.04C`

---

#### T19.G6.05A: Use synchronized speed x/y blocks for movement

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Synchronization requires variables for shared state, events for updates, lists for data

**Dependencies before:** `T19.G6.00F`, `T19.G6.02C`, `T14.G4.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T14.G4.01`, `T19.G6.00F`, `T19.G6.02C`

---

#### T19.G6.05B: Use synchronized speed/direction blocks for movement

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T08.G5.01`

**Rationale:** Synchronization requires variables for shared state, events for updates, lists for data

**Dependencies before:** `T19.G6.05A`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T19.G6.05A`

---

#### T19.G6.06: Configure stop vs continue collision behavior

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.02B`, `T14.G5.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T14.G5.01`, `T18.G5.01`, `T19.G6.02B`

---

#### T19.G6.06B: Configure collision deletion (delete sprite on touch)

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.06`, `T19.G6.07`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.06`, `T19.G6.07`

---

#### T19.G6.07: Handle multiplayer collisions with triggered messages

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.06`, `T06.G4.01`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.06`

---

#### T19.G6.08: Create shared world objects that stay synchronized

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.02B`, `T19.G6.04C`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.02B`, `T19.G6.04C`

---

#### T19.G6.09: Display a synchronized scoreboard for multiplayer sessions

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.04C`, `T09.G5.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T09.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.04C`

---

#### T19.G6.10A: Detect when players join or leave the game

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.01E`, `T19.G6.01F`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.01E`, `T19.G6.01F`

---

#### T19.G6.10B: Spawn sprites for new players who join

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.10A`, `T19.G6.02B`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.02B`, `T19.G6.10A`

---

#### T19.G6.10C: Remove sprites and clean up when players leave

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.10A`, `T19.G6.11`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.10A`, `T19.G6.11`

---

#### T19.G6.11: Remove sprites from the multiplayer game world

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.02B`, `T19.G6.07`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.02B`, `T19.G6.07`

---

#### T19.G6.12: Reset the game world for new rounds

**Dependencies added:** `T05.G5.01`, `T10.G5.01`, `T18.G5.01`, `T08.G5.01`

**Rationale:** Room management needs variables, events, UI for room displays, and lists for player management

**Dependencies before:** `T19.G6.08`, `T19.G6.04C`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T10.G5.01`, `T18.G5.01`, `T19.G6.04C`, `T19.G6.08`

---

### Topic T20 (8 skills)

#### T20.G6.01: Trace and explain an art algorithm

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T07.G5.01`, `T09.G5.01`, `T20.G5.04`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T20.G5.04`

---

#### T20.G6.02: Refactor repetitive art into loops/custom blocks

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T07.G5.01`, `T11.G5.01`, `T20.G5.04`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T11.G5.01`, `T20.G5.04`

---

#### T20.G6.03: Use variables and conditionals to branch designs

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T07.G5.01`, `T08.G5.01`, `T09.G5.01`, `T20.G5.02`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T08.G5.01`, `T09.G5.01`, `T20.G5.02`

---

#### T20.G6.04: **[Technical Skill]** Implement multi-field data visualization

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T07.G5.01`, `T08.G5.01`, `T10.G5.01`, `T20.G5.01`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T08.G5.01`, `T10.G5.01`, `T20.G5.01`

---

#### T20.G6.05: Apply math transformations to art

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T07.G5.01`, `T09.G5.01`, `T20.G5.04`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T20.G5.04`

---

#### T20.G6.05.01: Apply materials and textures to 3D art

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T20.G5.10`, `T20.G6.05`

**Dependencies after:** `T05.G5.01`, `T20.G5.10`, `T20.G6.05`

---

#### T20.G6.05.02: Create 3D curve and line art

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T20.G5.10`, `T20.G6.05`

**Dependencies after:** `T05.G5.01`, `T20.G5.10`, `T20.G6.05`

---

#### T20.G6.05.03: Create interactive 3D generative art

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T20.G5.03`, `T20.G5.10`

**Dependencies after:** `T05.G5.01`, `T20.G5.03`, `T20.G5.10`

---

### Topic T21 (19 skills)

#### T21.G6.01: Plan a mixed-source asset kit for a game or story project

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T21.G4.01`, `T21.G5.01`

**Dependencies after:** `T05.G5.01`, `T21.G4.01`, `T21.G5.01`

---

#### T21.G6.02: Write structured prompts to maintain consistent visual style

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T21.G5.01`, `T21.G5.02`

**Dependencies after:** `T05.G5.01`, `T21.G5.01`, `T21.G5.02`

---

#### T21.G6.03: Build a prompt test bench inside CreatiCode

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T06.G4.01`, `T09.G3.01.04`, `T10.G5.03`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T09.G3.01.04`, `T10.G5.03`

---

#### T21.G6.04: Iterate when an AI output fails requirements

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T10.G5.03`

**Dependencies after:** `T05.G5.01`, `T10.G5.03`

---

#### T21.G6.05: Use Azure speech recognition (ai_startspeech block)

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T06.G4.01`, `T21.G5.04`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T21.G5.04`

---

#### T21.G6.05a: Use OpenAI Whisper speech recognition (ai_startopenaispeech block)

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T06.G4.01`, `T21.G6.05`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T21.G6.05`

---

#### T21.G6.06: Check user input with AI content moderation

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T08.G4.01`, `T21.G5.05`

**Dependencies after:** `T05.G5.01`, `T08.G4.01`, `T21.G5.05`

---

#### T21.G6.07: Use image moderation to check visual content

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T21.G5.02`, `T21.G6.06`

**Dependencies after:** `T05.G5.01`, `T21.G5.02`, `T21.G6.06`

---

#### T21.G6.08: Use ChatGPT to generate story text or dialogue

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T21.G5.06`, `T21.G5.07`

**Dependencies after:** `T05.G5.01`, `T21.G5.06`, `T21.G5.07`

---

#### T21.G6.09: Compare ChatGPT responses with different temperatures

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T21.G5.07`

**Dependencies after:** `T05.G5.01`, `T21.G5.07`

---

#### T21.G6.10: Use system instructions to guide ChatGPT behavior

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T21.G5.06`

**Dependencies after:** `T05.G5.01`, `T21.G5.06`

---

#### T21.G6.11: Detect faces in camera video (basic detection setup)

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T06.G4.01`, `T10.G5.03`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T10.G5.03`

---

#### T21.G6.11a: Read facial feature coordinates from detection table

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T10.G5.03`, `T21.G6.11`

**Dependencies after:** `T05.G5.01`, `T10.G5.03`, `T21.G6.11`

---

#### T21.G6.11b: Use head tilt angle for face orientation detection

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T08.G4.01`, `T21.G6.11a`

**Dependencies after:** `T05.G5.01`, `T08.G4.01`, `T21.G6.11a`

---

#### T21.G6.12: Track 2D body parts in camera video (basic setup)

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T06.G4.01`, `T10.G4.01`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T10.G4.01`

---

#### T21.G6.12a: Read body part positions from detection table

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T10.G4.01`, `T21.G6.12`

**Dependencies after:** `T05.G5.01`, `T10.G4.01`, `T21.G6.12`

---

#### T21.G6.12b: Use curl and direction values for arm/leg gestures

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T08.G4.01`, `T21.G6.12a`

**Dependencies after:** `T05.G5.01`, `T08.G4.01`, `T21.G6.12a`

---

#### T21.G6.12c: Detect specific poses using body part combinations

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T08.G4.01`, `T21.G6.12b`

**Dependencies after:** `T05.G5.01`, `T08.G4.01`, `T21.G6.12b`

---

#### T21.G6.13: Stop camera-based AI detection to manage resources

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T21.G6.11`, `T21.G6.12`

**Dependencies after:** `T05.G5.01`, `T21.G6.11`, `T21.G6.12`

---

### Topic T22 (13 skills)

#### T22.G6.01.01: Make a basic ChatGPT request with one parameter

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T06.G4.01`, `T09.G4.01`, `T22.G5.01`, `T22.G5.05`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T07.G5.01`, `T09.G4.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`, `T22.G5.01` ... (9 total)

---

#### T22.G6.01.02: Configure multiple ChatGPT parameters and conversation flow

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T06.G4.01`, `T08.G4.01`, `T09.G4.04`, `T22.G6.01.01`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T07.G5.01`, `T08.G4.01`, `T09.G4.04`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01` ... (9 total)

---

#### T22.G6.01.03: Manage chat history and user input capture

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T08.G4.01`, `T09.G4.01`, `T09.G4.04`, `T22.G6.01.02`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T08.G4.01`, `T09.G4.01`, `T09.G4.04`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01` ... (9 total)

---

#### T22.G6.02: Adjust temperature for response creativity

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T06.G4.01`, `T08.G4.01`, `T09.G4.04`, `T22.G5.01`, `T22.G6.01.01`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T07.G5.01`, `T08.G4.01`, `T09.G4.04`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01` ... (10 total)

---

#### T22.G6.03: Handle streaming mode and long requests

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T06.G4.01`, `T08.G4.01`, `T09.G4.04`, `T22.G5.01`, `T22.G6.01.01`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T07.G5.01`, `T08.G4.01`, `T09.G4.04`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01` ... (10 total)

---

#### T22.G6.04.01: Add input widgets for user messages

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T16.G3.01`, `T16.G3.05`, `T22.G5.04`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`, `T16.G3.01`, `T16.G3.05`, `T22.G5.04`

---

#### T22.G6.04.02: Build a conversation log with dynamic updates

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T16.G3.03`, `T22.G6.02`, `T22.G6.03`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`, `T16.G3.03`, `T22.G6.02`, `T22.G6.03`

---

#### T22.G6.05: Implement session management for multi-turn conversations

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T22.G6.01.02`, `T22.G6.01.03`, `T22.G6.02`, `T22.G6.03`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`, `T22.G6.01.02`, `T22.G6.01.03`, `T22.G6.02` ... (9 total)

---

#### T22.G6.06.01: Create and configure a pre-built chat window

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T22.G6.01.02`, `T22.G6.02`, `T22.G6.03`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`, `T22.G6.01.02`, `T22.G6.02`, `T22.G6.03`

---

#### T22.G6.06.02: Manage chat messages with append and update blocks

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T22.G6.02`, `T22.G6.03`, `T22.G6.06.01`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`, `T22.G6.02`, `T22.G6.03`, `T22.G6.06.01`

---

#### T22.G6.06.03: Display streaming responses in real-time

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T22.G6.02`, `T22.G6.03`, `T22.G6.06.02`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`, `T22.G6.02`, `T22.G6.03`, `T22.G6.06.02`

---

#### T22.G6.07: Debug off-topic responses by rewriting prompts

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T06.G4.08`, `T08.G4.01`, `T09.G4.04`, `T22.G4.01`, `T22.G5.01` ... (6 total)

**Dependencies after:** `T05.G5.01`, `T06.G4.08`, `T07.G5.01`, `T08.G4.01`, `T09.G4.04`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01` ... (11 total)

---

#### T22.G6.08: Use multiple chatbot sessions with the select chatbot block

**Dependencies added:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`

**Rationale:** Game mechanics need variables (state), conditionals (logic), loops (updates), events (input), motion (movement)

**Dependencies before:** `T22.G6.01.02`, `T22.G6.01.03`, `T22.G6.04.02`

**Dependencies after:** `T05.G5.01`, `T07.G5.01`, `T09.G5.01`, `T10.G5.01`, `T11.G5.01`, `T22.G6.01.02`, `T22.G6.01.03`, `T22.G6.04.02`

---

### Topic T23 (31 skills)

#### T23.G6.01.01: Capture a single spoken phrase with basic speech recognition

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G5.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G5.02`

---

#### T23.G6.01.02: Select speech recognition language and observe accuracy differences

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G6.01.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G6.01.01`

---

#### T23.G6.01.03: Use continuous speech recognition for real-time transcription

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G6.01.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G6.01.02`

---

#### T23.G6.01.04: Handle speech recognition errors and implement retry logic

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G6.01.03`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G6.01.03`

---

#### T23.G6.02.01: Convert text to speech with basic settings

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G5.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G5.02`

---

#### T23.G6.02.02: Control TTS playback using the stop speaking block

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G6.02.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G6.02.01`

---

#### T23.G6.02.03: Save and reuse text-to-speech audio recordings

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G6.02.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G6.02.02`

---

#### T23.G6.03.01: Build a two-way voice chatbot loop

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T22.G6.01`, `T23.G6.01.02`, `T23.G6.02.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T22.G6.01` ... (10 total)

---

#### T23.G6.03.02: Use OpenAI Whisper for advanced speech transcription

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T22.G6.01`, `T23.G6.01.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T22.G6.01` ... (9 total)

---

#### T23.G6.04.01: Set up hand detection and view debug output

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G5.05`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G5.05`

---

#### T23.G6.04.02: Read and display finger curl angles from hand detection

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T09.G3.01.04`, `T23.G6.04.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01` ... (9 total)

---

#### T23.G6.04.03: Read finger direction data for advanced gesture recognition

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T09.G3.01.04`, `T23.G6.04.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01` ... (9 total)

---

#### T23.G6.04.04: Recognize basic gestures from hand detection data

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T23.G6.04.03`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G6.04.03`

---

#### T23.G6.04.05: Drive UI elements with live hand detection

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T23.G6.04.04`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01`, `T23.G6.04.04`

---

#### T23.G6.04.06: Detect and differentiate between left and right hands

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T23.G6.04.04`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01`, `T23.G6.04.04`

---

#### T23.G6.04.07: Track multiple hands simultaneously

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T23.G6.04.06`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01`, `T23.G6.04.06`

---

#### T23.G6.06.01: Apply moving average to smooth noisy sensor data

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G5.05`, `T23.G6.04.02`, `T23.G4.03`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G5.01`, `T09.G5.05`, `T11.G5.01`, `T15.G5.01`, `T23.G4.03` ... (9 total)

---

#### T23.G6.06.02: Use clamping to limit sensor values to valid ranges

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G6.04.02`, `T23.G4.03`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G4.03` ... (9 total)

---

#### T23.G6.06.03: Implement debouncing to filter rapid fluctuations

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G6.04.02`, `T23.G4.03`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G4.03` ... (9 total)

---

#### T23.G6.06.04: Create watchdog timers to detect and recover from sensor dropouts

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G6.04.02`, `T23.G4.03`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G4.03` ... (9 total)

---

#### T23.G6.07: Choose continuous vs. event-driven detection patterns

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T23.G6.04.04`, `T23.G6.06.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G6.04.04`, `T23.G6.06.01`

---

#### T23.G6.08: Add consent and privacy controls for sensor use

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T16.G6.01`, `T08.G3.01`, `T09.G3.01.04`, `T23.G5.03`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T16.G6.01` ... (9 total)

---

#### T23.G6.09.01: Set up 2D body pose detection and read keypoint positions

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T09.G3.01.04`, `T23.G6.04.02`, `T23.G5.05`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01` ... (10 total)

---

#### T23.G6.09.02: Detect body poses and trigger actions

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T09.G3.01.04`, `T23.G6.09.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01` ... (9 total)

---

#### T23.G6.09.03: Use 3D pose detection for depth-aware body tracking

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T09.G3.01.04`, `T23.G6.09.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01` ... (9 total)

---

#### T23.G6.10.01: Set up face detection and view detected faces

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T09.G3.01.04`, `T23.G5.05`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01` ... (9 total)

---

#### T23.G6.10.02: Read face data and trigger actions based on detection

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T09.G3.01.04`, `T23.G6.10.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01` ... (9 total)

---

#### T23.G6.10.03: Detect facial expressions and emotions from face data

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T23.G6.10.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01`, `T23.G6.10.02`

---

#### T23.G6.10.04: Track face attributes like age, gender, and accessories

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T10.G5.04`, `T08.G3.01`, `T23.G6.10.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G5.01`, `T10.G5.04`, `T11.G5.01`, `T15.G5.01`, `T23.G6.10.02`

---

#### T23.G6.11: Use NLP sentence analysis to extract parts of speech

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G6.01.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G6.01.02`

---

#### T23.G6.12: Compare Azure vs OpenAI Whisper speech recognition performance

**Dependencies added:** `T11.G5.01`, `T06.G5.01`, `T15.G5.01`, `T05.G5.01`, `T09.G5.01`

**Rationale:** Physics needs motion (movement), operators (calculations), sensing (collisions), variables (physics values), loops (updates)

**Dependencies before:** `T08.G3.01`, `T09.G3.01.04`, `T23.G6.03.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G3.01`, `T09.G3.01.04`, `T09.G5.01`, `T11.G5.01`, `T15.G5.01`, `T23.G6.03.02`

---

### Topic T24 (22 skills)

#### T24.G6.01: Provide complete context when asking XO to debug

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T06.G4.01`, `T09.G4.04`, `T24.G5.03`, `T24.G5.05`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T06.G5.01`, `T08.G5.01`, `T09.G4.04`, `T18.G5.01`, `T24.G5.03`, `T24.G5.05`

---

#### T24.G6.02: Verify XO's explanation against the project

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T06.G4.01`, `T07.G4.01`, `T08.G4.01`, `T09.G4.01`, `T24.G5.03` ... (6 total)

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T06.G5.01`, `T07.G4.01`, `T08.G4.01`, `T08.G5.01`, `T09.G4.01`, `T18.G5.01` ... (10 total)

---

#### T24.G6.03: Generate and deliver a quiz using XO

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T06.G4.01`, `T09.G4.04`, `T24.G5.05`, `T24.G6.02`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T06.G5.01`, `T08.G5.01`, `T09.G4.04`, `T18.G5.01`, `T24.G5.05`, `T24.G6.02`

---

#### T24.G6.04: Iterate AI images using feedback from XO

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T09.G4.04`, `T24.G5.04`, `T24.G5.05`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T09.G4.04`, `T18.G5.01`, `T24.G5.04`, `T24.G5.05`

---

#### T24.G6.04A: Generate custom images with the DALL-E block

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T24.G4.02`, `T24.G5.04`, `T24.G5.11`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G4.02`, `T24.G5.04`, `T24.G5.11`

---

#### T24.G6.05: Maintain a prompt/response lab notebook using lists

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T06.G4.01`, `T09.G4.01`, `T10.G4.03`, `T24.G5.05`, `T24.G6.04`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T06.G5.01`, `T08.G5.01`, `T09.G4.01`, `T10.G4.03`, `T18.G5.01`, `T24.G5.05` ... (9 total)

---

#### T24.G6.05A: Use AI sentence analysis to identify parts of speech

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T24.G4.02`, `T24.G4.06`, `T24.G5.05.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G4.02`, `T24.G4.06`, `T24.G5.05.01`

---

#### T24.G6.06: Label risky prompts and rewrite them safely

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T08.G4.01`, `T09.G4.04`, `T24.G5.05`, `T24.G6.05`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G4.01`, `T08.G5.01`, `T09.G4.04`, `T18.G5.01`, `T24.G5.05`, `T24.G6.05`

---

#### T24.G6.07.01: Use moderation blocks for text filtering

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T06.G4.01`, `T08.G4.01`, `T24.G4.05`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T06.G5.01`, `T08.G4.01`, `T08.G5.01`, `T18.G5.01`, `T24.G4.05`

---

#### T24.G6.07.02: Use moderation blocks for image filtering (costumes)

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T06.G4.01`, `T08.G4.01`, `T24.G4.05`, `T24.G6.07.01`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T06.G5.01`, `T08.G4.01`, `T08.G5.01`, `T18.G5.01`, `T24.G4.05`, `T24.G6.07.01`

---

#### T24.G6.07.03: Use moderation blocks for URL images

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T08.G4.01`, `T24.G4.05`, `T24.G6.07.01`, `T24.G6.07.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G4.01`, `T08.G5.01`, `T18.G5.01`, `T24.G4.05`, `T24.G6.07.01`, `T24.G6.07.02`

---

#### T24.G6.08.01: Manage ChatGPT sessions explicitly

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T24.G5.07.03`, `T08.G4.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G4.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.07.03`

---

#### T24.G6.08: Build a multi-turn chatbot using LLM sessions

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T07.G4.01`, `T08.G4.01`, `T24.G6.08.01`, `T24.G6.05`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T07.G4.01`, `T08.G4.01`, `T08.G5.01`, `T18.G5.01`, `T24.G6.05`, `T24.G6.08.01`

---

#### T24.G6.09: Attach stage snapshots to XO for visual debugging

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T24.G6.04`, `T09.G4.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T09.G4.01`, `T18.G5.01`, `T24.G6.04`

---

#### T24.G6.10.01: Understand hand detection table structure (47 rows)

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T06.G4.01`, `T24.G5.09`, `T24.G5.05.01`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.05.01`, `T24.G5.09`

---

#### T24.G6.10.02: Read curl and direction values for gesture recognition

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T24.G6.10.01`, `T09.G4.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T09.G4.01`, `T18.G5.01`, `T24.G6.10.01`

---

#### T24.G6.10.03: Build basic hand gesture controls

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T08.G4.01`, `T24.G6.10.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G4.01`, `T08.G5.01`, `T18.G5.01`, `T24.G6.10.02`

---

#### T24.G6.11.01: Understand 2D body detection table structure

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T06.G4.01`, `T24.G6.10.01`, `T24.G5.05.01`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.05.01`, `T24.G6.10.01`

---

#### T24.G6.11.02: Read body part positions and detect movements

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T09.G4.01`, `T24.G6.11.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T09.G4.01`, `T18.G5.01`, `T24.G6.11.01`

---

#### T24.G6.11.03: Build interactive games with body tracking

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T08.G4.01`, `T24.G6.11.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G4.01`, `T08.G5.01`, `T18.G5.01`, `T24.G6.11.02`

---

#### T24.G6.12: Use ChatGPT vision with costume attachment

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T06.G4.01`, `T24.G5.07.01`, `T24.G6.09`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.07.01`, `T24.G6.09`

---

#### T24.G6.13: Use web search blocks for real-time information

**Dependencies added:** `T08.G5.01`, `T06.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** Data handling needs lists (collections), operators (statistics), UI (visualization), variables (values)

**Dependencies before:** `T06.G4.01`, `T09.G4.01`, `T24.G4.06`, `T24.G6.05`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T06.G5.01`, `T08.G5.01`, `T09.G4.01`, `T18.G5.01`, `T24.G4.06`, `T24.G6.05`

---

### Topic T25 (11 skills)

#### T25.G6.01: Document metadata for datasets

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G5.01.01`, `T25.G4.04`, `T25.G4.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G4.01`, `T25.G4.04`, `T25.G5.01.01`

---

#### T25.G6.02: Explain lossy vs lossless representation

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G5.03`, `T25.G4.03`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G4.03`, `T25.G5.03`

---

#### T25.G6.03: Nest tables and lists within each other

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G5.01.02.03`, `T25.G5.03`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G5.01.02.03`, `T25.G5.03`

---

#### T25.G6.04: Trace AI prompt inputs to structured slots

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G5.04`, `T25.G5.02.02.05`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G5.02.02.05`, `T25.G5.04`

---

#### T25.G6.05.01: Search and filter table data with conditions

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G5.06.03`, `T25.G4.06`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G4.06`, `T25.G5.06.03`

---

#### T25.G6.05.02: Aggregate table data using built-in blocks

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G6.05.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G6.05.01`

---

#### T25.G6.05.03: Sort table data by column

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G6.05.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G6.05.01`

---

#### T25.G6.06.01: Save data to server storage

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G5.01.02.03`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G5.01.02.03`

---

#### T25.G6.06.02: Load data from server storage

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G6.06.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G6.06.01`

---

#### T25.G6.07.01: Export table data as CSV

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G5.06.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G5.06.01`

---

#### T25.G6.07.02: Import CSV data into tables

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T18.G5.01`, `T05.G5.01`

**Rationale:** AI needs data concepts, lists (datasets), UI (interaction), variables (model state)

**Dependencies before:** `T25.G6.07.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T25.G6.07.01`

---

### Topic T29 (9 skills)

#### T29.G6.01: Compare characters, words, and token counts

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T29.G5.10`, `T29.G5.03.02`, `T29.G4.03`, `T08.G4.01`, `T09.G4.04` ... (6 total)

**Dependencies after:** `T05.G5.01`, `T08.G4.01`, `T09.G4.04`, `T10.G4.03`, `T29.G4.03`, `T29.G5.03.02`, `T29.G5.10`

---

#### T29.G6.02: Compute n-gram (bigram) frequencies

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T29.G5.03.02`, `T11.G5.01`, `T07.G4.01`, `T09.G4.04`, `T10.G4.03`

**Dependencies after:** `T05.G5.01`, `T07.G4.01`, `T09.G4.04`, `T10.G4.03`, `T11.G5.01`, `T29.G5.03.02`

---

#### T29.G6.03: Create autocomplete suggestions from bigrams

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T29.G6.02`, `T06.G4.01`, `T09.G4.04`, `T10.G4.03`

**Dependencies after:** `T05.G5.01`, `T06.G4.01`, `T09.G4.04`, `T10.G4.03`, `T29.G6.02`

---

#### T29.G6.04: Log AI prompts/responses with ratings and timestamps

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T29.G5.02`, `T29.G5.05`, `T11.G5.01`, `T07.G4.01`, `T09.G4.04` ... (6 total)

**Dependencies after:** `T05.G5.01`, `T07.G4.01`, `T09.G4.04`, `T10.G4.03`, `T11.G5.01`, `T29.G5.02`, `T29.G5.05`

---

#### T29.G6.06: Convert speech to text using voice recognition

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T29.G5.02`, `T29.G5.07`

**Dependencies after:** `T05.G5.01`, `T29.G5.02`, `T29.G5.07`

---

#### T29.G6.07: Convert text to speech with voice selection

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T29.G4.01`

**Dependencies after:** `T05.G5.01`, `T29.G4.01`

---

#### T29.G6.08: Compare text similarity using edit distance

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T29.G4.03`, `T29.G6.01`

**Dependencies after:** `T05.G5.01`, `T29.G4.03`, `T29.G6.01`

---

#### T29.G6.09: Handle text length limits and truncation

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T29.G6.01`, `T08.G5.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T29.G6.01`

---

#### T29.G6.10: Validate text input and handle errors

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T29.G6.01`, `T08.G5.01`

**Dependencies after:** `T05.G5.01`, `T08.G5.01`, `T29.G6.01`

---

### Topic T30 (9 skills)

#### T30.G6.01: Analyze sensor specifications for CreatiCode projects

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T30.G5.03`, `T30.G5.01`

**Dependencies after:** `T05.G5.01`, `T30.G5.01`, `T30.G5.03`

---

#### T30.G6.02: Compare browser storage options for CreatiCode projects

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T30.G5.01`, `T30.G3.03`

**Dependencies after:** `T05.G5.01`, `T30.G3.03`, `T30.G5.01`

---

#### T30.G6.03: Explain camera and microphone privacy permissions

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T30.G5.02`, `T30.G3.05`, `T30.G3.06`

**Dependencies after:** `T05.G5.01`, `T30.G3.05`, `T30.G3.06`, `T30.G5.02`

---

#### T30.G6.04: Plan device capability checklists for CreatiCode AI projects

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T30.G5.01`, `T30.G5.03`

**Dependencies after:** `T05.G5.01`, `T30.G5.01`, `T30.G5.03`

---

#### T30.G6.05: Use speech recognition in voice-controlled CreatiCode projects

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T30.G3.06`, `T30.G5.01`

**Dependencies after:** `T05.G5.01`, `T30.G3.06`, `T30.G5.01`

---

#### T30.G6.05.01: Use webcam as 3D scene background for AR effects

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T30.G5.05`, `T30.G6.04`

**Dependencies after:** `T05.G5.01`, `T30.G5.05`, `T30.G6.04`

---

#### T30.G6.06: Implement hand and 2D body tracking in CreatiCode projects

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T30.G5.06`, `T30.G4.05`

**Dependencies after:** `T05.G5.01`, `T30.G4.05`, `T30.G5.06`

---

#### T30.G6.06.01: Use 3D pose detection for depth-aware body tracking

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T30.G6.06`, `T30.G5.05`

**Dependencies after:** `T05.G5.01`, `T30.G5.05`, `T30.G6.06`

---

#### T30.G6.06.02: Implement 3D object dragging with mouse

**Dependencies added:** `T05.G5.01`

**Rationale:** Basic variables skill as foundation

**Dependencies before:** `T30.G5.05.01`, `T30.G4.05`

**Dependencies after:** `T05.G5.01`, `T30.G4.05`, `T30.G5.05.01`

---

### Topic T35 (8 skills)

#### T35.G6.01: Apply ethics lenses (beneficence, fairness, autonomy)

**Dependencies added:** `T24.G5.01`, `T25.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`

**Rationale:** ML needs data skills, AI foundations, lists (training data), variables, operators (calculations)

**Dependencies before:** `T16.G6.01`, `T35.G5.01`, `T35.G4.01`, `T22.G6.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T16.G6.01`, `T22.G6.01`, `T24.G5.01`, `T25.G5.01`, `T35.G4.01` ... (9 total)

---

#### T35.G6.02: Analyze data privacy tradeoffs

**Dependencies added:** `T24.G5.01`, `T25.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`

**Rationale:** ML needs data skills, AI foundations, lists (training data), variables, operators (calculations)

**Dependencies before:** `T35.G5.01`, `T35.G4.02`, `T16.G6.01`, `T19.G6.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T16.G6.01`, `T19.G6.01`, `T24.G5.01`, `T25.G5.01`, `T35.G4.02` ... (9 total)

---

#### T35.G6.05.01: Build consent form and data collection

**Dependencies added:** `T24.G5.01`, `T25.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`

**Rationale:** ML needs data skills, AI foundations, lists (training data), variables, operators (calculations)

**Dependencies before:** `T35.G6.02`, `T16.G6.01`, `T19.G6.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T16.G6.01`, `T19.G6.01`, `T24.G5.01`, `T25.G5.01`, `T35.G6.02`

---

#### T35.G6.05.02: Implement data viewing and deletion controls

**Dependencies added:** `T24.G5.01`, `T25.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`

**Rationale:** ML needs data skills, AI foundations, lists (training data), variables, operators (calculations)

**Dependencies before:** `T35.G6.05.01`, `T16.G6.01`, `T19.G6.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T16.G6.01`, `T19.G6.01`, `T24.G5.01`, `T25.G5.01`, `T35.G6.05.01`

---

#### T35.G6.03.01: Test AI content generation tools (T21-T22)

**Dependencies added:** `T24.G5.01`, `T25.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`

**Rationale:** ML needs data skills, AI foundations, lists (training data), variables, operators (calculations)

**Dependencies before:** `T35.G5.03`, `T35.G4.03.01`, `T21.G6.01`, `T22.G6.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T21.G6.01`, `T22.G6.01`, `T24.G5.01`, `T25.G5.01`, `T35.G4.03.01` ... (9 total)

---

#### T35.G6.03.02: Synthesize comprehensive AI ethics guidelines

**Dependencies added:** `T24.G5.01`, `T25.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`

**Rationale:** ML needs data skills, AI foundations, lists (training data), variables, operators (calculations)

**Dependencies before:** `T35.G6.03.01`, `T16.G6.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T16.G6.01`, `T24.G5.01`, `T25.G5.01`, `T35.G6.03.01`

---

#### T35.G6.03.03: Develop ethics guidelines for AI perception and assistance (T23-T24)

**Dependencies added:** `T24.G5.01`, `T25.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`

**Rationale:** ML needs data skills, AI foundations, lists (training data), variables, operators (calculations)

**Dependencies before:** `T35.G5.03`, `T23.G6.01`, `T24.G6.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T23.G6.01`, `T24.G5.01`, `T24.G6.01`, `T25.G5.01`, `T35.G5.03`

---

#### T35.G6.04: Examine digital divide data

**Dependencies added:** `T24.G5.01`, `T25.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`

**Rationale:** ML needs data skills, AI foundations, lists (training data), variables, operators (calculations)

**Dependencies before:** `T35.G5.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T24.G5.01`, `T25.G5.01`, `T35.G5.01`

---

### Topic T36 (7 skills)

#### T36.G6.01: Compare computing career clusters (software, hardware, data, AI)

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`, `T18.G5.01`

**Rationale:** Data science needs data handling, lists, variables, operators, UI (visualization)

**Dependencies before:** `T36.G5.01`, `T36.G4.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T36.G4.01`, `T36.G5.01`

---

#### T36.G6.01.01: Analyze representation in computing careers

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`, `T18.G5.01`

**Rationale:** Data science needs data handling, lists, variables, operators, UI (visualization)

**Dependencies before:** `T36.G5.03`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T36.G5.03`

---

#### T36.G6.01.02: Connect AI skills to career pathways

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`, `T18.G5.01`

**Rationale:** Data science needs data handling, lists, variables, operators, UI (visualization)

**Dependencies before:** `T36.G5.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T36.G5.01`

---

#### T36.G6.02: Practice stand-ups, task boards, and sprint reviews in team projects

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`, `T18.G5.01`

**Rationale:** Data science needs data handling, lists, variables, operators, UI (visualization)

**Dependencies before:** `T36.G5.02`, `T36.G4.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T36.G4.02`, `T36.G5.02`

---

#### T36.G6.03: Analyze job descriptions for skills/values

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`, `T18.G5.01`

**Rationale:** Data science needs data handling, lists, variables, operators, UI (visualization)

**Dependencies before:** `T36.G5.01`, `T36.G4.04`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T36.G4.04`, `T36.G5.01`

---

#### T36.G6.04: Add ethics clauses to team charters

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`, `T18.G5.01`

**Rationale:** Data science needs data handling, lists, variables, operators, UI (visualization)

**Dependencies before:** `T36.G5.02`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T36.G5.02`

---

#### T36.G6.05: Document project contributions for a portfolio

**Dependencies added:** `T24.G5.01`, `T08.G5.01`, `T05.G5.01`, `T06.G5.01`, `T18.G5.01`

**Rationale:** Data science needs data handling, lists, variables, operators, UI (visualization)

**Dependencies before:** `T36.G5.02`, `T36.G5.01`

**Dependencies after:** `T05.G5.01`, `T06.G5.01`, `T08.G5.01`, `T18.G5.01`, `T24.G5.01`, `T36.G5.01`, `T36.G5.02`

---

