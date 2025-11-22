# T19 - Multiplayer Apps: Complete Skill Extraction

## Grade 6-8 Skills

### ID: T19.G6.00A
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Understand what "multiplayer" means in CreatiCode games
**Description:** Students learn that multiplayer games let multiple people play together by connecting over the internet. They understand that one person "hosts" the game (creates it) and others "join" it. They identify examples of multiplayer vs single-player games and explain why multiplayer games need internet connections. They understand that all players see the same game world and can interact with each other.

**Dependencies:**
* T06.G3.09: Fix a behavior that runs at the wrong time
* T09.G3.05: Trace code with variables to predict outcomes

---

### ID: T19.G6.00B
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Understand the host-client model in multiplayer games
**Description:** Students learn that in CreatiCode multiplayer, one player is the "host" who creates the game, and other players are "clients" who join. They understand that the game only exists as long as the host is connected - if the host leaves, the game ends for everyone. They explain why this matters for game design (host should be reliable). They identify which player is the host in a running game.

**Dependencies:**
* T19.G6.00A: Understand what "multiplayer" means in CreatiCode games

---

### ID: T19.G6.00C
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Understand sprite replication in multiplayer games
**Description:** Students learn that when they add a sprite to a multiplayer game, other players see a "replicate" copy of that sprite on their screens. They understand that the "original" sprite (on your screen) runs your code, while "replicate" sprites (on other screens) show what you're doing. They identify which sprites are originals vs replicates when testing with two windows. They explain why replication is necessary (each player needs to see all other players).

**Dependencies:**
* T19.G6.00B: Understand the host-client model in multiplayer games

---

### ID: T19.G6.00D
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Understand Dynamic vs Static sprites in multiplayer games
**Description:** Students learn that Dynamic sprites can move and have physics (gravity, collisions), while Static sprites stay in place and act as fixed obstacles (walls, platforms). They understand that Static sprites use less network bandwidth because they don't send position updates. They choose appropriate sprite types for different game objects: players are Dynamic, walls are Static, collectible coins might be either.

**Dependencies:**
* T19.G6.00C: Understand sprite replication in multiplayer games
* T14.G4.01: Compare position, velocity, and acceleration

---

### ID: T19.G6.00E
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Understand collision shapes (Rectangle vs Circle) in multiplayer games
**Description:** Students learn that sprites can have Rectangle or Circle collision shapes. They understand that Rectangle is better for square/rectangular objects (walls, boxes) and Circle is better for round objects (balls, players). They test different shapes and observe how collision detection changes - circles collide smoothly at edges, rectangles have corner detection. They choose appropriate shapes for their game objects.

**Dependencies:**
* T19.G6.00D: Understand Dynamic vs Static sprites in multiplayer games
* T14.G5.01: Detect when sprites touch or overlap

---

### ID: T19.G6.00F
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Understand what "synchronization" means in multiplayer games
**Description:** Students learn that "synchronization" means keeping all players' screens showing the same thing. They understand that normal movement blocks (like "change x by 10") only affect their own screen, but synchronized blocks (like "synchronously set speed x 10 y 0") affect everyone's screen. They compare both approaches and observe the difference. They explain why synchronization is necessary for fair multiplayer games.

**Dependencies:**
* T19.G6.00C: Understand sprite replication in multiplayer games

---

### ID: T19.G6.01A
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Create a simple multiplayer game room
**Description:** Students use the `create game` block with a game name and password to host a room. They use default values for server (US-East), capacity (4), and world dimensions (480x360). They verify the game was created by checking the `connected to game` boolean reporter. They understand that their computer is now the "host" and others can join.

**Dependencies:**
* T19.G6.00B: Understand the host-client model in multiplayer games
* T08.G3.01: Use a simple if in a script

---

### ID: T19.G6.01B
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Join a multiplayer game room
**Description:** Students use the `join game` block with a game name, host name, and password to join an existing room. They provide a display name (what other players see). They verify connection using the `connected to game` reporter. They understand that they are a "client" connecting to someone else's hosted game.

**Dependencies:**
* T19.G6.01A: Create a simple multiplayer game room

---

### ID: T19.G6.01C
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Configure game capacity and world dimensions
**Description:** Students learn to set capacity (max players) and world width/height when creating a game. They understand that capacity limits how many players can join (e.g., capacity 2 for 1v1 games, capacity 8 for party games). They understand that world dimensions define the playable area - sprites outside these bounds may wrap around or be hidden. They test how capacity limits affect who can join.

**Dependencies:**
* T19.G6.01A: Create a simple multiplayer game room

---

### ID: T19.G6.01D
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** List available multiplayer games in a table
**Description:** Students use `list multiplayer games in server` to display all active games in a table. They read the Host Name, Game Name, and User Count columns to see which games are available and how many players are in each. They use this information to decide which game to join. They understand that this only shows games on the selected server.

**Dependencies:**
* T19.G6.01A: Create a simple multiplayer game room
* T10.G4.01: Find an item's position in a list (linear search)

---

### ID: T19.G6.01E
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** List players in a game room
**Description:** Students use `list players in game` to display who is in a specific game. They read the Player Name and Role columns to see all connected players and their assigned roles. They use this to verify who has joined their game or to check if friends are in a game before joining.

**Dependencies:**
* T19.G6.01B: Join a multiplayer game room
* T10.G4.01: Find an item's position in a list (linear search)

---

### ID: T19.G6.01F
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Check connection status and display feedback
**Description:** Students use the `connected to game` boolean reporter to check whether they are properly connected. They display appropriate messages (e.g., "Connected!" or "Reconnecting...") based on connection state. They disable game controls when disconnected to prevent errors. They understand that connection can drop due to network issues and the game should handle this gracefully.

**Dependencies:**
* T19.G6.01B: Join a multiplayer game room
* T08.G3.01: Use a simple if in a script

---

### ID: T19.G6.02A
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Test a multiplayer game with two browser windows
**Description:** Students learn to open two browser windows (or tabs) to test their multiplayer game locally. They create a game in one window (host) and join it in another (client). They verify that changes in one window appear in the other window. They understand that this simulates two players without needing a second person.

**Dependencies:**
* T19.G6.01B: Join a multiplayer game room

---

### ID: T19.G6.02B
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Register sprites with the game server
**Description:** Students use the `add this sprite to game as a [Dynamic/Static] [Rectangle/Circle]` block to register a sprite with the game server. They understand that this makes the sprite visible to other players. They choose Dynamic for moving sprites and Static for fixed obstacles. They choose Rectangle or Circle collision shape based on the sprite's appearance. They understand that only registered sprites appear in the multiplayer world.

**Dependencies:**
* T19.G6.00C: Understand sprite replication in multiplayer games
* T19.G6.00D: Understand Dynamic vs Static sprites in multiplayer games
* T19.G6.00E: Understand collision shapes (Rectangle vs Circle) in multiplayer games
* T19.G6.01B: Join a multiplayer game room

---

### ID: T19.G6.02C
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Initialize sprites when they join using "when added to game"
**Description:** Students use the `when added to game` hat block to run initialization code when a sprite is confirmed registered by the server. They set starting positions, display names, or announce arrivals to other players. They understand this event fires after the sprite is successfully added to the multiplayer game.

**Dependencies:**
* T19.G6.02B: Register sprites with the game server

---

### ID: T19.G6.03A
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Create a simple 2-player tag game
**Description:** Students create a simple multiplayer tag game where players chase each other. When one player touches another, that player becomes "it" (the chaser). They use synchronized movement so both players see the same positions. They use collision detection to detect touches. They broadcast "you're it!" messages to change roles. They test with two windows.

**Dependencies:**
* T19.G6.02B: Register sprites with the game server
* T19.G6.02C: Initialize sprites when they join using "when added to game"

---

### ID: T19.G6.04A
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Choose between "All Sprites" and "Exclude Replicate" broadcast modes
**Description:** Students learn when to broadcast to "All Sprites" (including replicates) vs "Exclude Replicate" (originals only). They understand that "All Sprites" makes all copies of all sprites run the handler, while "Exclude Replicate" makes only original sprites (one per player) run it. They test both modes and observe the difference. They choose "Exclude Replicate" when each player should do something once (like scoring), and "All Sprites" when every visible sprite should react (like playing animation).

**Dependencies:**
* T19.G6.00C: Understand sprite replication in multiplayer games
* T19.G6.02C: Initialize sprites when they join using "when added to game"

---

### ID: T19.G6.04B
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Broadcast multiplayer messages with parameters
**Description:** Students use the `broadcast [MESSAGE] with parameter [PARAMETER] mode [MODE]` block to send messages to all players with data attached. They understand that this is different from regular broadcast - it sends across the network to all connected clients. They use parameters to send scores, player names, or other data. They receive the parameter in the message handler and use it.

**Dependencies:**
* T19.G6.04A: Choose between "All Sprites" and "Exclude Replicate" broadcast modes

---

### ID: T19.G6.05
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Synchronize player movement using synchronized speed blocks
**Description:** Students use the `synchronously set speed x (X) y (Y)` or `synchronously set speed (SPEED) dir (DIR)` blocks to move sprites so that all players see the same motion. They understand that the server coordinates movement across all connected clients. They compare synchronized movement to regular movement blocks and observe that only synchronized blocks update all clients.

**Dependencies:**
* T19.G6.00F: Understand what "synchronization" means in multiplayer games
* T19.G6.02C: Initialize sprites when they join using "when added to game"
* T19.G6.01F: Check connection status and display feedback

---

### ID: T19.G6.06
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Configure stop vs pass collision behavior
**Description:** Students learn that collision events can make sprites "stop" (bounce off each other) or "pass" (go through each other). They configure this in the `when touching` collision trigger block. They test both behaviors and choose appropriate ones for different game objects: walls should stop, collectible items should pass.

**Dependencies:**
* T19.G6.02B: Register sprites with the game server
* T14.G5.01: Detect when sprites touch or overlap

---

### ID: T19.G6.07
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Handle multiplayer collisions with triggered messages
**Description:** Students use the `when touching [SPRITENAME] will [stop/pass] and trigger [MESSAGE] with parameter [PARAMETER]` block to detect collisions between multiplayer sprites. They configure whether sprites should stop or pass through on contact and handle the triggered message. They understand that collision events are synchronized across all clients.

**Dependencies:**
* T19.G6.05: Synchronize player movement using synchronized speed blocks
* T19.G6.06: Configure stop vs pass collision behavior

---

### ID: T19.G6.08
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Create shared world objects that stay synchronized
**Description:** Students add static sprites (coins, doors, obstacles) to the game world and track their state. When a player interacts with an object, they broadcast the change so all clients show the same world state. They understand that shared objects need synchronization to work correctly in multiplayer.

**Dependencies:**
* T19.G6.02B: Register sprites with the game server
* T19.G6.04B: Broadcast multiplayer messages with parameters

---

### ID: T19.G6.09
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Display a synchronized scoreboard for multiplayer sessions
**Description:** Students maintain score variables that update across all clients when any player earns points. They use broadcasts with parameters to send score updates. They ensure all players see the same scoreboard by broadcasting score changes and handling received messages.

**Dependencies:**
* T19.G6.04B: Broadcast multiplayer messages with parameters

---

### ID: T19.G6.10
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Handle player join and leave events
**Description:** Students use the `list players in game` block periodically to detect when new players join or existing players leave. They spawn or remove sprites accordingly and send welcome messages or update the player list display. They understand that monitoring the player list is necessary for dynamic lobbies.

**Dependencies:**
* T19.G6.02C: Initialize sprites when they join using "when added to game"
* T19.G6.01E: List players in a game room
* T19.G6.04B: Broadcast multiplayer messages with parameters

---

### ID: T19.G6.11
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Remove sprites from the multiplayer game world
**Description:** Students use the `remove this sprite from game` block to remove sprites when players disconnect, objects are collected, or enemies are defeated. They ensure the removal is synchronized by broadcasting removal events so all clients update their display. They understand that proper cleanup prevents ghost sprites.

**Dependencies:**
* T19.G6.02B: Register sprites with the game server
* T19.G6.07: Handle multiplayer collisions with triggered messages

---

### ID: T19.G6.12
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Reset the game world for new rounds
**Description:** Students use the `reset game world` block to clean up all synchronized objects when starting a new round or resetting the game. They re-initialize game state and respawn sprites for all players. They understand that resetting ensures a clean slate for new rounds.

**Dependencies:**
* T19.G6.08: Create shared world objects that stay synchronized
* T19.G6.04B: Broadcast multiplayer messages with parameters

---

## Grade 7-8 Skills

### ID: T19.G7.00A
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Use roles to identify player types
**Description:** Students learn that roles let them assign different responsibilities to players (like "seeker" vs "hider" in hide-and-seek, or "red team" vs "blue team"). They assign roles when creating or joining a game. They read a player's role from the player list table and use conditionals to run different code for different roles. They understand that roles are just labels - they don't automatically change behavior, you must code the differences.

**Dependencies:**
* T19.G6.01E: List players in a game room
* T08.G4.01: Use conditionals with multiple outcomes

---

### ID: T19.G7.00B
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Choose appropriate server locations to minimize lag
**Description:** Students learn that server location affects how fast messages travel between players (latency/lag). They understand that players should choose servers close to most players geographically - US-East for East Coast players, US-West for West Coast, etc. They test games with different server locations and observe latency differences. They understand that further distance equals more lag.

**Dependencies:**
* T19.G6.00F: Understand what "synchronization" means in multiplayer games

---

### ID: T19.G7.01
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Build a cooperative puzzle with shared progress counters
**Description:** Students design a multiplayer task where players must work together toward shared goals (e.g., both press switches simultaneously). They maintain progress counters that all players can see and update. They broadcast progress updates and check win conditions cooperatively.

**Dependencies:**
* T19.G6.08: Create shared world objects that stay synchronized
* T19.G6.09: Display a synchronized scoreboard for multiplayer sessions

---

### ID: T19.G7.02
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Implement a ready-up system before the game starts
**Description:** Students create a lobby where players click a "Ready" button that broadcasts their status. The host monitors the player list and starts the game only when all connected players have marked themselves ready. They use player count and ready status to control game start.

**Dependencies:**
* T19.G6.10: Handle player join and leave events
* T19.G6.04B: Broadcast multiplayer messages with parameters

---

### ID: T19.G7.03
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Choose what data to synchronize versus keep local
**Description:** Students decide which variables should sync across all clients (scores, positions) versus stay local (UI state, sounds). They use broadcasts for event-driven sync and synchronized blocks for continuous updates. They understand that over-synchronizing causes network lag while under-synchronizing causes inconsistent game states.

**Dependencies:**
* T19.G6.05: Synchronize player movement using synchronized speed blocks
* T19.G6.04B: Broadcast multiplayer messages with parameters

---

### ID: T19.G7.04
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Scale game logic to handle variable player counts
**Description:** Students refactor scripts to loop over the player list when creating sprites, updating displays, or distributing game objectives. The game works correctly whether 2, 4, or more players are connected. They use the player list length to determine actual player count and adjust accordingly.

**Dependencies:**
* T19.G6.10: Handle player join and leave events
* T07.G5.01: Use a loop to repeat a task an exact number of times

---

### ID: T19.G7.05
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Balance starting conditions and scoring for fairness
**Description:** Students audit spawn points, turn order, and scoring rules to identify and eliminate built-in advantages. They test with multiple players and document how changes improve game balance. They understand that fair games give all players equal opportunities to win.

**Dependencies:**
* T19.G6.09: Display a synchronized scoreboard for multiplayer sessions
* T19.G6.10: Handle player join and leave events

---

### ID: T19.G7.06
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Choose when to use passwords vs public games
**Description:** Students learn when to use passwords (private games with friends) vs empty passwords (public games open to anyone). They understand trade-offs: passwords keep games private but require coordination, public games are easier to join but may have unwanted players. They implement both types and discuss use cases.

**Dependencies:**
* T19.G6.01A: Create a simple multiplayer game room

---

### ID: T19.G7.07
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Debug why sprites aren't synchronizing
**Description:** Students identify when sprites move on one client but not another. They check if they used synchronized movement blocks instead of regular movement blocks. They verify that sprites were added to the game. They use print statements to trace execution on both clients. They fix synchronization issues by using the correct blocks.

**Dependencies:**
* T19.G6.02A: Test a multiplayer game with two browser windows
* T19.G6.05: Synchronize player movement using synchronized speed blocks
* T13.G6.01: Add print statements to trace variable changes

---

## Grade 8 Skills

### ID: T19.G8.01
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Implement team assignment or simple matchmaking
**Description:** Students automatically assign players to teams based on join order, player count, or role selection. They ensure teams are balanced in size and update assignments when players join or leave. They use loops and conditionals to distribute players evenly across teams.

**Dependencies:**
* T19.G7.04: Scale game logic to handle variable player counts
* T19.G7.00A: Use roles to identify player types
* T07.G6.01: Trace nested loops with variable bounds

---

### ID: T19.G8.02
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Implement host-authoritative validation to prevent cheating
**Description:** Students restructure their game so clients request score changes or moves, but only the host validates and applies them. The host rejects impossible actions (teleporting, instant kills) to maintain fair play. They understand that client-side validation can be bypassed but host validation cannot.

**Dependencies:**
* T19.G7.03: Choose what data to synchronize versus keep local
* T19.G7.04: Scale game logic to handle variable player counts
* T08.G6.01: Use conditionals to control simulation steps

---

### ID: T19.G8.03
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Persist match data to CreatiCode cloud storage
**Description:** Students use cloud variables or cloud lists to store final scores, achievements, or unlocks that persist across sessions. They load saved data when players return to show long-term progress. They understand the difference between session data (temporary) and persistent data (saved).

**Dependencies:**
* T19.G6.09: Display a synchronized scoreboard for multiplayer sessions
* T09.G6.01: Model real-world quantities using variables and formulas

---

### ID: T19.G8.04
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Debug message delivery timing issues
**Description:** Students identify when messages arrive in different orders on different clients, causing state divergence. They understand that network messages have variable delays. They add sequence numbers or timestamps to broadcasts to debug ordering. They implement acknowledgement systems to ensure critical messages are received.

**Dependencies:**
* T19.G7.07: Debug why sprites aren't synchronizing
* T19.G7.03: Choose what data to synchronize versus keep local
* T06.G6.01: Trace event execution paths in a multi‑event program
* T13.G6.01: Add print statements to trace variable changes

---

### ID: T19.G8.05
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Explain the architecture of a multiplayer game system
**Description:** Students create a diagram showing how their multiplayer game works: player input, host/server processing, message broadcast, and screen updates. They identify potential bottlenecks (too many messages, slow hosts) and propose solutions. They understand the data flow in client-server architecture.

**Dependencies:**
* T19.G7.03: Choose what data to synchronize versus keep local
* T19.G7.04: Scale game logic to handle variable player counts
* T02.G6.01: Design a flowchart for a simple guessing game
* T06.G6.01: Trace event execution paths in a multi‑event program

---

### ID: T19.G8.06
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Understand what information is shared in multiplayer games
**Description:** Students learn what data is shared with other players: display name, position, messages, but NOT account credentials or personal info. They understand that passwords protect game rooms, not individual players. They learn that all players can see all public game data. They explain why this matters for privacy and design games accordingly.

**Dependencies:**
* T19.G6.01B: Join a multiplayer game room
* T19.G6.04B: Broadcast multiplayer messages with parameters

---

### ID: T19.G8.07
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Optimize network traffic in multiplayer games
**Description:** Students learn that too many broadcasts or too many Dynamic sprites cause network lag. They identify performance bottlenecks: broadcasting every frame, synchronizing unnecessary data, too many moving objects. They optimize by reducing broadcast frequency, using Static sprites where possible, and only synchronizing essential data.

**Dependencies:**
* T19.G6.00D: Understand Dynamic vs Static sprites in multiplayer games
* T19.G7.03: Choose what data to synchronize versus keep local
* T19.G6.04B: Broadcast multiplayer messages with parameters

---

### ID: T19.G8.08
**Topic:** T19 – Multiplayer Apps: Grade 6–8 Skill List
**Skill:** Profile and measure multiplayer performance
**Description:** Students use timing and counting techniques to measure multiplayer performance. They measure latency (time from broadcast to receive), frame rate, and network message count. They identify performance bottlenecks using data. They compare performance before and after optimizations.

**Dependencies:**
* T19.G8.07: Optimize network traffic in multiplayer games
* T09.G6.01: Model real-world quantities using variables and formulas

---

## Summary

**Total T19 Skills: 47**
- Grade 6 Skills: 18 (T19.G6.00A - T19.G6.12)
- Grade 7 Skills: 8 (T19.G7.00A - T19.G7.07)
- Grade 8 Skills: 8 (T19.G8.01 - T19.G8.08)

All skills are from the "Grade 6–8 Skill List" for the T19 – Multiplayer Apps topic.
