# T19 - Multiplayer Apps: Optimized Complete Skills

## GRADE 5 SKILLS (Conceptual Foundation)

---

ID: T19.G5.01
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Create a local 2-player game on one keyboard
Description: Students create a simple game where two players use different keys on the same keyboard (e.g., Player 1 uses arrow keys, Player 2 uses WASD). They implement separate controls for each player using key press conditionals. They use variables to track each player's state independently. They use broadcasts to coordinate actions between player sprites (e.g., "Player 1 scored" message). This introduces the concept of multiple agents before teaching networked multiplayer.

Dependencies:
* T06.G4.01: Use broadcast to coordinate sprite actions
* T08.G4.01: Use conditionals with multiple outcomes
* T14.G5.01: Detect when sprites touch or overlap
* T09.G3.01.01: Create a new variable with a descriptive name
* T10.G3.01.01: Create a new list variable


---

ID: T19.G5.02
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand what the internet is
Description: Students learn that the internet is a network of computers that can send messages to each other. They understand that multiplayer games work by sending messages over the internet between players' computers. They identify real-world examples of internet communication (websites, email, video chat, online games). They explain the difference between local programs (running on one computer) and networked programs (connecting multiple computers).

Dependencies:
None (foundational)


---

ID: T19.G5.03
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand what "multiplayer" means
Description: Students learn that "multiplayer" means multiple people playing the same game simultaneously, interacting with each other in real-time. They compare local multiplayer (same screen/keyboard) to online multiplayer (different computers connected over internet). They identify examples of multiplayer games and explain how players interact (competing, cooperating, chatting). They understand that multiplayer requires synchronizing game state so all players see the same world.

Dependencies:
* T19.G5.01: Create a local 2-player game on one keyboard
* T19.G5.02: Understand what the internet is


---

ID: T19.G5.04
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand host and client roles
Description: Students learn that in CreatiCode multiplayer, one player creates the game (the "host") and others join (the "clients"). They understand that the host's computer runs the authoritative game state and clients synchronize with it. They compare this to real-world examples (host of a party, server at restaurant, teacher in classroom). They explain why having one authoritative source prevents conflicts when multiple players make changes simultaneously.

Dependencies:
* T19.G5.03: Understand what "multiplayer" means


---

ID: T19.G5.05
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand synchronization basics
Description: Students learn that "synchronization" means keeping game state consistent across all players' screens. They understand that when one player moves, that movement must be sent to all other players so everyone sees the same position. They identify what needs synchronization (player positions, scores, game events) versus what doesn't (local UI, sound effects on individual machines). They explain why network delay means synchronization isn't instant.

Dependencies:
* T19.G5.04: Understand host and client roles


---

## GRADE 6 SKILLS (Core Implementation)

### Conceptual Foundation (G6.00X)

---

ID: T19.G6.00A
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand what "multiplayer" means in CreatiCode games (deeper dive)
Description: Students learn the technical details of how CreatiCode multiplayer works. They understand that game rooms exist on servers, the host creates the authoritative game state, and clients connect and synchronize. They compare single-player (one instance) to multiplayer (multiple instances connected). They diagram the flow: player actions → network messages → synchronization → all players see changes. They explain why some games work better as multiplayer (competitive, cooperative) than others (story-driven, puzzle).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G5.03: Understand what "multiplayer" means
* T19.G5.04: Understand host and client roles


---

ID: T19.G6.00B
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand the host-client model and game rooms in multiplayer games
Description: Students learn the detailed responsibilities of hosts versus clients. The host creates the game room, runs the authoritative game logic, validates actions, and broadcasts updates. Clients send input requests and receive state updates. They understand that game rooms are containers that hold connected players and shared game state. They explain why the host must validate actions (prevent cheating) and why clients can't directly modify game state. They identify which parts of their game should run on host versus all clients.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G5.04: Understand host and client roles
* T19.G6.00A: Understand what "multiplayer" means in CreatiCode games (deeper dive)


---

ID: T19.G6.00C
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand sprite replication in multiplayer games
Description: Students learn that when a sprite is registered with the multiplayer game, it appears on all connected players' screens automatically. The "original" sprite exists on the player who registered it, and "replicate" sprites appear on other players' screens. They understand that position updates on the original automatically synchronize to replicates. They explain why replication is necessary (so all players see the same game world) and how it works (network messages broadcast position/state changes).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00B: Understand the host-client model and game rooms in multiplayer games


---

ID: T19.G6.00C2
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand how code runs on original vs replicate sprites
Description: Students learn that code blocks run only on the original sprite by default, not on replicate sprites. Input controls (arrow keys) should only affect the local player's sprite (the original), not remote players' replicates. They test this by adding print statements and observing which window shows output. They understand this prevents conflicts (multiple players trying to control the same sprite) and allows each player to control only their own sprite while seeing others' sprites as replicates.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00C: Understand sprite replication in multiplayer games


---

ID: T19.G6.00D
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand Dynamic vs Static sprites in multiplayer games
Description: Students learn the difference between Dynamic and Static sprites in multiplayer. Dynamic sprites are for moving objects (players, enemies, projectiles) and their positions synchronize continuously. Static sprites are for fixed objects (walls, platforms, obstacles) and their positions never change, using less network bandwidth. They categorize at least 10 game objects as Dynamic or Static. They explain the performance trade-off: Dynamic sprites synchronize smoothly but use more network traffic, Static sprites are efficient but can't move.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00B: Understand the host-client model in multiplayer games


---

ID: T19.G6.00E
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand collision shapes (Rectangle vs Circle) in multiplayer games
Description: Students learn that multiplayer sprites need collision shapes for hit detection: Rectangle for box-shaped objects (walls, crates, platforms) and Circle for round objects (balls, circular players). They understand that collision shapes must match sprite appearance for accurate gameplay. They test collision detection with both shapes and observe differences. They explain why choosing the right shape matters: better accuracy, smoother gameplay, and fair collision detection across all players.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T14.G5.01: Detect when sprites touch or overlap
* T19.G6.00B: Understand the host-client model in multiplayer games


---

ID: T19.G6.00F
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand synchronization mechanisms in depth
Description: Students learn the technical details of how CreatiCode synchronizes game state. They understand that synchronized movement blocks automatically send position updates through the network. Broadcasting messages explicitly synchronizes events (player scored, game started). They compare automatic synchronization (positions of Dynamic sprites) to manual synchronization (broadcasts for custom events). They explain when to use each: continuous data (movement) uses synchronized blocks, discrete events (scoring, collecting) use broadcasts.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G5.05: Understand synchronization basics
* T19.G6.00C: Understand sprite replication in multiplayer games


---

ID: T19.G6.00G
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand what lag and latency mean in multiplayer games
Description: Students learn that "lag" or "latency" is the delay between an action and seeing it on other players' screens. They understand this delay is caused by network message travel time (physical distance, internet speed). They identify how lag affects gameplay: high lag makes games feel unresponsive, low lag feels smooth and immediate. They test games on different server locations and observe lag differences. They explain why some games are more affected by lag than others (fast-paced action games vs turn-based strategy).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00F: Understand synchronization mechanisms in depth


---

ID: T19.G6.00H
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand what servers are in multiplayer games
Description: Students learn that servers are computers that relay messages between players and store game rooms. CreatiCode provides servers in different geographic locations (US-East, US-West, Europe, Asia). They understand that all players must connect to the same server to play together. They explain why server location matters (closer servers = lower lag) and why servers are necessary (relay messages, maintain game room, validate actions). They identify which server location is best for their geography and play group.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00B: Understand the host-client model and game rooms in multiplayer games


---

ID: T19.G6.00I
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand what roles are in multiplayer games
Description: Students learn that "roles" are labels assigned to players (e.g., "red team", "builder", "seeker", "guard") that can be used to give different behaviors or responsibilities. They understand that roles are optional text labels that don't automatically change behavior - developers must write code to check roles and act accordingly. They identify examples of role-based games (asymmetric games, team games, job-based games). They explain how roles enable game variety: players can have different abilities, objectives, or team assignments.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00B: Understand the host-client model and game rooms in multiplayer games


---

ID: T19.G6.00J
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand display names and game names
Description: Students learn the difference between account names (private, for login), display names (public, shown to other players), and game names (identifies the game room). They understand that display names let players identify each other without revealing personal information. Game names let players find and join specific games. They choose clear, appropriate display names and unique game names. They explain why these distinctions matter for privacy and usability.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00B: Understand the host-client model and game rooms in multiplayer games


---

ID: T19.G6.00K
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Distinguish multiplayer games from cloud variables
Description: Students compare two ways to share data online: multiplayer games (real-time synchronization, game rooms, multiple players see changes instantly) versus cloud variables (persistent storage, slower updates, no game rooms). They understand when to use each: multiplayer for interactive real-time games with simultaneous players, cloud variables for leaderboards, saved progress, or asynchronous sharing. They explain the technical differences: multiplayer uses game servers and rooms, cloud variables use database storage.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T09.G5.01: Store and retrieve game state using variables
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00B: Understand the host-client model and game rooms in multiplayer games


---

### Room Management (G6.01X)

---

ID: T19.G6.01A
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Create a basic multiplayer game room
Description: Students use the create game block to host a multiplayer room. They enter a unique game name that other players will use to find their game. They choose whether to set a password (private game) or leave it empty (public game). They verify the game was created by checking the connected to game reporter. They understand that they are now the host and their computer runs the authoritative game state. They test by confirming they can see their created game in the game list.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G4.01: Use conditionals with multiple outcomes
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00B: Understand the host-client model and game rooms in multiplayer games
* T19.G6.00J: Understand display names and game names


---

ID: T19.G6.01A.01
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Set display name when creating a game
Description: Students configure their display name (what other players will see) when creating a multiplayer game using the create game block. They understand the difference between account name (private, for login) and display name (public, shown to other players). They choose clear, appropriate display names that help other players identify them. They test with two windows to verify the display name appears correctly in the player list. They explain why display names matter for player identity and communication.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00J: Understand display names and game names
* T19.G6.01A: Create a basic multiplayer game room


---

ID: T19.G6.01A.02
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Choose a role when creating a game
Description: Students choose a role for themselves when creating a multiplayer game. They understand that roles are optional text labels (like "red team", "builder", "seeker") that can be used to assign different behaviors. They learn that choosing a role at creation time doesn't automatically change behavior; they must write code to check roles and act accordingly. They test by verifying their chosen role appears in the player list. They explain scenarios where roles are useful (teams, asymmetric games, job assignments).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00I: Understand what roles are in multiplayer games
* T19.G6.01A.01: Set display name when creating a game


---

ID: T19.G6.01A.03
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Select server location when creating a game
Description: Students select an appropriate server location (US-East, US-West, Europe, Asia, etc.) when creating a multiplayer game using the create game block. They understand that all players must connect to the same server, so the host's choice affects everyone. They consider where most players will be located geographically and choose the closest server to minimize lag. They test games on different servers and observe lag differences. They explain why server location matters for gameplay quality.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00H: Understand what servers are in multiplayer games
* T19.G6.01A.02: Choose a role when creating a game


---

ID: T19.G6.01B
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Join a basic multiplayer game room
Description: Students use the join game block to connect to an existing multiplayer room. They enter the game name and select the same server location the host chose. They enter the password if required (or leave empty for public games). They verify connection using the connected to game reporter. They understand that they are now a client connecting to someone else's hosted game. They must know the game name and server location from the host to join successfully.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00H: Understand what servers are in multiplayer games
* T19.G6.01A: Create a basic multiplayer game room


---

ID: T19.G6.01B.01
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Set display name when joining a game
Description: Students set their display name (what other players will see) when joining a multiplayer game using the join game block. They choose clear, appropriate names that help other players identify them. They test with two windows to verify their display name appears correctly in the player list visible to all players. They understand that display names are public and visible to everyone in the game. They explain why consistent display names help with player recognition across sessions.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00J: Understand display names and game names
* T19.G6.01B: Join a basic multiplayer game room


---

ID: T19.G6.01B.02
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Choose a role when joining a game
Description: Students choose a role for themselves when joining a multiplayer game. They understand that the host may have designed the game with specific roles in mind (teams, job assignments, character types). They select a role that fits the game design or leave it empty if roles aren't used. They verify their role appears correctly in the player list. They coordinate with other players to choose complementary roles (different teams, different jobs). They explain how role selection affects their gameplay experience.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00I: Understand what roles are in multiplayer games
* T19.G6.01B.01: Set display name when joining a game


---

ID: T19.G6.01C
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Configure game capacity (maximum players)
Description: Students learn to set the maximum number of players (capacity) when creating a multiplayer game room using the create game block. They understand that capacity limits how many clients can join their hosted game. They test different capacity values (2, 4, 6, 8, etc.) and observe what happens when capacity is reached (additional players cannot join). They choose appropriate capacity based on game type (2 for head-to-head, 4-8 for party games) and explain how capacity affects gameplay experience and server resources.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00B: Understand the host-client model and game rooms in multiplayer games
* T19.G6.01A.03: Select server location when creating a game


---

ID: T19.G6.01C2
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Configure multiplayer world dimensions (width and height)
Description: Students set world width and height when creating a multiplayer game room using the create game block. They understand that world dimensions define the boundaries of the shared game space. They test different sizes and observe how it affects gameplay (small worlds feel cramped, large worlds feel spacious). They choose dimensions appropriate for their game type (racing games need longer tracks, battle arenas may be square). They explain how world size affects player interaction and game pacing.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00B: Understand the host-client model and game rooms in multiplayer games
* T19.G6.01C: Configure game capacity (maximum players)


---

ID: T19.G6.01C3
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Handle capacity limits and "game full" scenarios
Description: Students detect when a game has reached capacity and display appropriate messages to players trying to join. They use the game list user count to identify full games. They implement UI feedback ("Game Full - Please Try Another") when join attempts fail. They test by filling a game to capacity and attempting additional joins. They explain why capacity limits exist (performance, game balance, server resources) and how to communicate them clearly to players.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.01C: Configure game capacity (maximum players)
* T19.G6.01D: List available multiplayer games in a table


---

ID: T19.G6.01D
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: List available multiplayer games in a table
Description: Students use the list multiplayer games on server block to display all active game rooms in a table. They read the table columns: "Host Name" (who created the game), "Game Name" (the room's identifier), and "User Count" (how many players are connected). They use this information to find games to join. They filter games by server location to see only games on their chosen server. They understand that this list updates to show currently active games, not past or deleted games.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T09.G5.01: Store and retrieve game state using variables
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00B: Understand the host-client model and game rooms in multiplayer games
* T19.G6.00H: Understand what servers are in multiplayer games


---

ID: T19.G6.01E
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: List players in a game room
Description: Students use the list players in game block to display who is in a specific game. They read the table columns: "Player Name" (display names) and "Role" (assigned roles). They use this to verify who has joined their game or to check if friends are in a game before joining. They understand that tables organize player data in rows (one per player) and columns (attributes). They test by joining games and verifying all connected players appear in the list.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T09.G5.01: Store and retrieve game state using variables
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.01B: Join a basic multiplayer game room


---

ID: T19.G6.01F
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Check connection status and display feedback
Description: Students use the connected to game boolean reporter to check whether they are properly connected to a multiplayer game. They display appropriate messages ("Connected!", "Connecting...", "Disconnected") based on connection state. They disable game controls when disconnected to prevent errors. They test by observing connection status during normal gameplay and simulated disconnections. They understand that connection can drop due to network issues and the game should handle this gracefully with clear user feedback.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G4.01: Use conditionals with multiple outcomes
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.01B: Join a basic multiplayer game room


---

ID: T19.G6.01G
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Test a multiplayer game with two browser windows
Description: Students open two browser windows or tabs to test their multiplayer game by creating and joining as two separate players. They verify that actions in one window appear in the other window (movement, messages, score changes). They use this testing method throughout development to catch synchronization issues early. They understand that two-window testing simulates real multiplayer but both instances run on the same computer, so network lag is minimal. They explain why testing with actual network delay (different computers) is also important.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.01B: Join a basic multiplayer game room


---

### Sprite Registration (G6.02X)

---

ID: T19.G6.02A
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand sprite registration purpose
Description: Students learn that sprites must be "registered" with the multiplayer game server to become visible to other players. Unregistered sprites exist only locally and other players cannot see them. Registration creates replicate copies on all other players' screens that automatically synchronize position and appearance. They identify which sprites should be registered (players, enemies, shared objects) versus which should stay local (UI elements, local effects, background decorations). They explain why registration is necessary for multiplayer gameplay.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00C: Understand sprite replication in multiplayer games
* T19.G6.00D: Understand Dynamic vs Static sprites in multiplayer games
* T19.G6.00E: Understand collision shapes (Rectangle vs Circle) in multiplayer games


---

ID: T19.G6.02B.01
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Add a Dynamic sprite to the multiplayer game
Description: Students use the add this sprite to game block with Dynamic mode to register moving sprites (players, enemies, projectiles) with the multiplayer game server. They understand that Dynamic sprites continuously synchronize their positions across all players. They test with two windows to verify that when a Dynamic sprite moves in one window, its position updates in the other window automatically. They explain when to use Dynamic mode (any sprite that will move during gameplay) and its trade-off (smooth synchronization but higher network usage).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00D: Understand Dynamic vs Static sprites in multiplayer games
* T19.G6.01B: Join a basic multiplayer game room
* T19.G6.02A: Understand sprite registration purpose


---

ID: T19.G6.02B.02
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Add a Static sprite to the multiplayer game
Description: Students use the add this sprite to game block with Static mode to register non-moving sprites (walls, platforms, obstacles) with the multiplayer game server. They understand that Static sprites do not synchronize position updates, saving network bandwidth. They test with two windows to verify that Static sprites appear in both windows but do not send position updates when moved. They explain when to use Static mode (sprites that never move) and its benefit (efficient, low network usage). They identify the limitation: Static sprites cannot move during gameplay.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00D: Understand Dynamic vs Static sprites in multiplayer games
* T19.G6.02B.01: Add a Dynamic sprite to the multiplayer game


---

ID: T19.G6.02B.03
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Choose Rectangle collision shape when registering sprites
Description: Students use the add this sprite to game block with Rectangle collision shape for box-shaped sprites (walls, crates, platforms, rectangular players). They understand that Rectangle collision detection checks if rectangular bounding boxes overlap. They test collision accuracy by colliding rectangular sprites with Rectangle shape versus Circle shape. They observe that Rectangle shape provides accurate collision for box-shaped sprites but less accurate for round sprites. They categorize their game sprites and choose Rectangle for appropriate objects.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00E: Understand collision shapes (Rectangle vs Circle) in multiplayer games
* T19.G6.02B.02: Add a Static sprite to the multiplayer game


---

ID: T19.G6.02B.04
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Choose Circle collision shape when registering sprites
Description: Students use the add this sprite to game block with Circle collision shape for round sprites (balls, circular players, round obstacles). They understand that Circle collision detection checks if circular bounding circles overlap. They test collision accuracy by colliding round sprites with Circle shape versus Rectangle shape. They observe that Circle shape provides accurate collision for round sprites but less accurate for rectangular sprites. They explain why choosing the correct collision shape improves gameplay (accurate hit detection, fair gameplay, better player experience).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00E: Understand collision shapes (Rectangle vs Circle) in multiplayer games
* T19.G6.02B.03: Choose Rectangle collision shape when registering sprites


---

ID: T19.G6.02C
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Initialize sprites when they join using "when added to game"
Description: Students use the when added to game hat block to run initialization code after a sprite is successfully registered with the multiplayer game server. They set starting positions, display names, or announce arrivals to other players. They understand this event fires after the add sprite block completes and the server confirms registration. They test with two windows to verify initialization runs at the right time. They explain why this event is important (ensures sprite is registered before initializing) versus running code immediately after the add block (might run before server confirms).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.02B.04: Choose Circle collision shape when registering sprites


---

### Project-Based Learning (G6.03X)

---

ID: T19.G6.03A.01
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Set up multiplayer racing game structure
Description: Students create the foundation for a 2-player racing game. They set up a game room with appropriate capacity (2 players), create a race track with a clear starting line and finish line, and register player sprites as Dynamic Circles. They position both players at the starting line when they join using the when added to game event. They test with two windows to verify both players appear at the starting positions. This establishes the game world structure before adding movement and win conditions.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.01G: Test a multiplayer game with two browser windows
* T19.G6.02B.01: Add a Dynamic sprite to the multiplayer game
* T19.G6.02C: Initialize sprites when they join using "when added to game"


---

ID: T19.G6.03A.02
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Implement synchronized racing controls
Description: Students add keyboard-controlled movement to their racing game using synchronized speed blocks. They implement arrow key controls (up/down/left/right) that update speed x and y values to move players around the track. They test with two windows to verify that when one player moves, both windows show the same movement. They ensure controls are responsive and movement feels smooth for racing gameplay. They understand that synchronized blocks automatically send position updates to all players.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.03A.01: Set up multiplayer racing game structure
* T19.G6.05A: Use synchronized speed x/y blocks for movement


---

ID: T19.G6.03A.03
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Add finish line and collision detection
Description: Students implement finish line collision detection in their racing game. They create a finish line sprite or zone and use collision detection to identify when a player crosses it. They configure appropriate collision behavior (continue, not stop, so players can cross the line). They test with two windows to verify that crossing the finish line is detected correctly for both players. They prepare to broadcast a message when collision occurs to announce the winner.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T14.G5.01: Detect when sprites touch or overlap
* T19.G6.03A.02: Implement synchronized racing controls


---

ID: T19.G6.03A.04
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Determine and display race winner
Description: Students implement win detection by broadcasting a message when the first player crosses the finish line. They display the winner's name on all players' screens and stop the race. They handle edge cases (simultaneous finish, disconnections during race). They test with two windows by racing to the finish and verifying the correct winner is announced on both screens. They understand that broadcasting ensures all players see the same winner announcement simultaneously.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.03A.03: Add finish line and collision detection
* T19.G6.04C: Broadcast multiplayer messages with parameters


---

ID: T19.G6.03B.01
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Design cooperative puzzle objectives
Description: Students design a multiplayer puzzle where players must work together to achieve a shared goal. They identify objectives that require coordination (both players press switches simultaneously, one player holds door while other passes through, players pass items between each other). They create simple prototypes of cooperative mechanics. They explain why cooperation is required (single player cannot complete alone) and how it encourages teamwork and communication.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.01G: Test a multiplayer game with two browser windows


---

ID: T19.G6.03B.02
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Implement shared progress tracking
Description: Students create variables to track shared progress in their cooperative game (switches pressed, items collected, objectives completed). They update these variables when players complete tasks. They display progress to all players using a shared UI or scoreboard. They test with two windows to verify that when one player completes a task, both players see the progress update. They understand that shared state must be synchronized across all players.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T09.G5.01: Store and retrieve game state using variables
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.03B.01: Design cooperative puzzle objectives


---

ID: T19.G6.03B.03
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Broadcast cooperative events
Description: Students use broadcast blocks to synchronize cooperative events (switch pressed, item delivered, door opened). They broadcast messages with parameters to include event details (which switch, which player). They handle these messages on all clients to update game state consistently. They test with two windows to verify that events triggered by one player are seen by all players. They explain why broadcasting is necessary for cooperative gameplay (all players must know about shared events).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.03B.02: Implement shared progress tracking
* T19.G6.04C: Broadcast multiplayer messages with parameters


---

ID: T19.G6.03B.04
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Implement cooperative win condition
Description: Students implement a win condition that requires all players to complete their objectives (all switches pressed, all items delivered, all players reach exit). They check that all required tasks are completed before declaring victory. They broadcast a win message and display celebration on all players' screens. They test with two windows to verify that partial completion doesn't trigger win and full completion does. They understand that cooperative win conditions encourage teamwork and shared success.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.03B.03: Broadcast cooperative events
* T19.G6.04C: Broadcast multiplayer messages with parameters


---

ID: T19.G6.03C.01
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Design tag game roles and rules
Description: Students design a tag game with clear roles (tagger, runners) and rules (how tagging works, what happens when tagged, how roles change). They plan the game flow: initial role assignment, tagging mechanic, role swap after tag, win/end conditions. They sketch the game layout and identify required sprites (players, boundaries, safe zones). They explain how their design creates engaging gameplay through role asymmetry and chase mechanics.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00I: Understand what roles are in multiplayer games
* T19.G6.01G: Test a multiplayer game with two browser windows


---

ID: T19.G6.03C.02
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Implement role-based tag behaviors
Description: Students implement different behaviors for taggers versus runners using role conditionals. Taggers can tag others (trigger collision events), runners try to avoid taggers. They use the player's role to determine which behavior to execute. They test with two windows by assigning different roles and verifying each role behaves correctly. They understand that role-based conditionals create asymmetric gameplay where different players have different objectives.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00I: Understand what roles are in multiplayer games
* T19.G6.03C.01: Design tag game roles and rules


---

ID: T19.G6.03C.03
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Use collision messages for tagging
Description: Students configure multiplayer collision blocks to detect when the tagger touches a runner. They set collision behavior to "continue" (players pass through each other, not stop) and trigger a "tagged" message. They attach parameters to identify which player was tagged. They test with two windows by moving players into collision and verifying the message fires. They explain why "continue" mode works better than "stop" for tag games (allows smooth gameplay, no getting stuck).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T14.G5.01: Detect when sprites touch or overlap
* T19.G6.03C.02: Implement role-based tag behaviors
* T19.G6.06: Configure stop vs continue collision behavior


---

ID: T19.G6.03C.04
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Swap roles after tagging
Description: Students implement role swapping when a tag occurs: the tagged runner becomes the tagger, and the tagger becomes a runner. They broadcast a role change message to all players when a tag happens. They update player roles and behaviors immediately after the swap. They test with two windows by tagging and verifying roles swap correctly and both players' behaviors change. They handle edge cases (simultaneous tags, disconnections). They explain how role swapping maintains game dynamics and prevents one player from being "it" forever.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.03C.03: Use collision messages for tagging
* T19.G6.04C: Broadcast multiplayer messages with parameters
* T19.G6.07: Handle multiplayer collisions with triggered messages


---

### Messaging (G6.04X)

---

ID: T19.G6.04A
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Choose between "All Sprites" and "Exclude Replicate" broadcast modes
Description: Students learn the two broadcast modes in multiplayer games. "All Sprites" mode sends the message to all sprites on all clients (originals and replicates). "Exclude Replicate" mode sends only to original sprites (skips replicates). They test both modes and observe the difference: "All Sprites" may cause duplicate actions if replicates also respond, "Exclude Replicate" ensures each player's code runs only once. They choose the appropriate mode based on whether they want actions to run on all sprites or only on original/controlling sprites.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00C: Understand sprite replication in multiplayer games
* T19.G6.00C2: Understand how code runs on original vs replicate sprites


---

ID: T19.G6.04B
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Receive and handle multiplayer broadcast messages
Description: Students use when I receive blocks to handle multiplayer broadcasts. They understand that broadcasted messages are sent to all connected players and all sprites that listen for that message. They implement handlers that run when specific messages arrive (game started, player scored, item collected). They test with two windows to verify that when one player broadcasts, all players receive and handle the message. They explain why message handling is necessary for synchronized game events.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T06.G4.01: Use broadcast to coordinate sprite actions
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.04A: Choose between "All Sprites" and "Exclude Replicate" broadcast modes


---

ID: T19.G6.04C
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Broadcast multiplayer messages with parameters
Description: Students use the broadcast message to all block with parameters to send data along with messages (player name, score change, item ID). They attach parameters to messages so receiving code knows the details (who scored, how many points, which item). They access parameters in the when I receive handler. They test with two windows by broadcasting messages with different parameters and verifying receivers get the correct data. They explain why parameters are essential for meaningful multiplayer communication.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.04B: Receive and handle multiplayer broadcast messages


---

ID: T19.G6.04D
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Access and use broadcast message parameters
Description: Students use the message parameter reporter block to retrieve data attached to multiplayer broadcasts. They extract parameter values and use them in game logic (display player name, update score by amount, spawn item at location). They handle different parameter types (text, numbers, lists). They test with two windows by sending various parameters and verifying receivers correctly extract and use the values. They explain how parameters enable complex multiplayer interactions beyond simple notifications.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T09.G5.01: Store and retrieve game state using variables
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.04C: Broadcast multiplayer messages with parameters


---

### Movement (G6.05X)

---

ID: T19.G6.05A
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Use synchronized speed x/y blocks for movement
Description: Students use the set synchronized speed x and y blocks to move Dynamic sprites in multiplayer games. They understand that these blocks automatically synchronize sprite positions across all players. They implement keyboard controls (arrow keys, WASD) that set speed x/y values to move sprites in 4 or 8 directions. They test with two windows to verify that movement in one window appears in the other window smoothly. They explain when to use x/y movement (grid-based, platformer-style, or 4-direction movement).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00F: Understand synchronization mechanisms in depth
* T19.G6.02B.01: Add a Dynamic sprite to the multiplayer game


---

ID: T19.G6.05B
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Use synchronized speed/direction blocks for movement
Description: Students use the set synchronized speed and direction blocks to move Dynamic sprites in multiplayer games. They understand that these blocks use polar coordinates (speed magnitude and angle) instead of x/y components. They implement rotation-based controls (turn left/right, move forward) suitable for vehicles, spaceships, or top-down rotational movement. They test with two windows to verify smooth synchronized movement. They compare to x/y movement and explain when speed/direction is more intuitive (rotation-based movement, vehicles, orbital mechanics).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.00F: Understand synchronization mechanisms in depth
* T19.G6.05A: Use synchronized speed x/y blocks for movement


---

### Collisions (G6.06X, G6.07)

---

ID: T19.G6.06
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Configure stop vs continue collision behavior
Description: Students learn the two basic collision behaviors in multiplayer collision blocks. "Stop" makes both sprites stop moving when they collide (solid collision for walls, obstacles). "Continue" lets sprites pass through each other (trigger zones, collectibles, pass-through collisions). They test both behaviors and observe differences. They choose appropriate behavior based on game design: solid objects use "stop", triggers and pass-through objects use "continue". They explain how collision behavior affects gameplay feel and mechanics.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T14.G5.01: Detect when sprites touch or overlap
* T19.G6.02B.01: Add a Dynamic sprite to the multiplayer game


---

ID: T19.G6.06B
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Configure collision deletion (stop and delete, continue and delete)
Description: Students learn the "delete" collision modes that remove sprites after collision. "Stop and delete" creates solid collectibles (coin blocks, solid items that stop you and disappear). "Continue and delete" creates pass-through collectibles (coins you run through, power-ups). They test both deletion modes and observe when sprites are removed. They choose based on game design: solid collectibles use "stop and delete", pass-through collectibles use "continue and delete". They explain how deletion affects gameplay (resource collection, consumables, destructible objects).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.06: Configure stop vs continue collision behavior


---

ID: T19.G6.07
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Handle multiplayer collisions with triggered messages
Description: Students configure multiplayer collision blocks to trigger broadcast messages when collisions occur. They attach parameters to include collision details (which sprites collided, collision location). They handle these messages to implement game logic (scoring, damage, collectibles, triggers). They test with two windows to verify that collisions detected on one client trigger messages received by all clients. They explain why collision messages are necessary (synchronize game events, ensure all players know about collisions, coordinate responses).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.04C: Broadcast multiplayer messages with parameters
* T19.G6.06B: Configure collision deletion (stop and delete, continue and delete)


---

### Game Management (G6.08-G6.12)

---

ID: T19.G6.08
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Create shared world objects that stay synchronized
Description: Students create game objects that persist and synchronize across all players (platforms, obstacles, collectibles). They register these sprites with the game and ensure they appear identically on all clients. They test with two windows to verify that world objects appear in the same positions on both screens. They understand that shared world objects create a consistent game environment for all players. They choose Dynamic vs Static based on whether objects move (falling platforms vs fixed walls).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.02B.01: Add a Dynamic sprite to the multiplayer game
* T19.G6.02B.02: Add a Static sprite to the multiplayer game


---

ID: T19.G6.09
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Display a synchronized scoreboard for multiplayer sessions
Description: Students create a scoreboard that displays all players' scores and synchronizes across all clients. They update scores using broadcast messages so all players see the same values. They use variables or tables to store multiple players' scores. They display the scoreboard visually (text, table, or UI widget). They test with two windows to verify that score changes in one window appear in the other window. They explain why score synchronization is important for fair gameplay and competitive awareness.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T09.G5.01: Store and retrieve game state using variables
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.04C: Broadcast multiplayer messages with parameters


---

ID: T19.G6.10A
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Detect when players join or leave the game
Description: Students implement event handlers to detect when new players join or existing players leave the multiplayer game. They use player list changes to trigger announcements or UI updates ("Player joined!", "Player left"). They update game state to account for player count changes (reassign teams, adjust difficulty, update player list display). They test with two windows by joining and leaving to verify detection works. They explain why join/leave detection is important for game flow and player awareness.

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.01E: List players in a game room


---

ID: T19.G6.10B
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Announce player join and leave events
Description: Students broadcast messages when players join or leave to notify all connected players. They display announcements visually ("[Player Name] joined the game", "[Player Name] left the game") on all players' screens. They include player names and roles in announcements for context. They test with two windows by joining and leaving to verify announcements appear correctly on all screens. They explain why announcements improve multiplayer experience (player awareness, social presence, game state transparency).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.04C: Broadcast multiplayer messages with parameters
* T19.G6.10A: Detect when players join or leave the game


---

ID: T19.G6.10C
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Remove sprites and clean up when players leave
Description: Students implement cleanup logic when players leave the game. They remove disconnected players' sprites from the game world, remove them from scoreboards and player lists, and clean up any resources associated with that player. They test with two windows by disconnecting and verifying the disconnected player's sprites disappear on the remaining player's screen. They explain why cleanup is important (prevents ghost sprites, maintains accurate game state, manages resources efficiently).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.10B: Announce player join and leave events
* T19.G6.11: Remove sprites from the multiplayer game world


---

ID: T19.G6.11
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Remove sprites from the multiplayer game world
Description: Students use the remove this sprite from game block to unregister sprites from the multiplayer game server. They understand that removed sprites disappear from all players' screens. They use this for game mechanics (destroying objects, removing collectibles after collection, cleaning up when players leave). They test with two windows to verify that removing a sprite in one window makes it disappear in the other window. They explain when to remove sprites (object destruction, player leaving, resetting game state).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.02B.01: Add a Dynamic sprite to the multiplayer game


---

ID: T19.G6.12
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Reset the game world for new rounds
Description: Students use the reset multiplayer game block to clean up the current game state and start fresh for a new round. They understand this removes all registered sprites and resets game variables. They implement new-round logic that resets scores, repositions players, and reinitializes game objects. They test with two windows by resetting and verifying all players see the fresh game state. They explain when to reset (new round, game restart, major state change) and why it's better than manual cleanup (atomic operation, ensures consistency).

Dependencies:
* T05.G5.01: Write clear user needs and requirements for a small app
* T08.G5.01: Design multi-branch decision logic
* T10.G5.01: Understand table structure (rows, columns, cells)
* T19.G6.11: Remove sprites from the multiplayer game world


---

## GRADE 7 SKILLS (Advanced Techniques)

---

ID: T19.G7.00A
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Implement different behaviors for different roles
Description: Students implement role-based conditional logic so players with different roles have different behaviors, abilities, or objectives. They check player roles using conditionals and execute role-specific code (red team attacks blue base, builder places blocks, seeker finds hiders). They test with multiple players assigned to different roles to verify each role behaves correctly. They explain how role-based gameplay creates strategic depth, asymmetric game modes, and diverse player experiences.

Dependencies:
* T19.G6.00I: Understand what roles are in multiplayer games
* T19.G6.01E: List players in a game room
* T08.G5.01: Design multi-branch decision logic
* T08.G6.01: Use conditionals to control simulation steps


---

ID: T19.G7.00B
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Choose appropriate server locations to minimize lag
Description: Students learn to select server locations strategically based on where players are located geographically. They test games on different servers (US-East, US-West, Europe, Asia) and measure lag differences. They understand that players closer to the server experience lower lag. They make informed decisions about which server to use based on player distribution (choose central location, or closest to majority of players). They explain the trade-offs when players are geographically distributed.

Dependencies:
* T19.G6.00G: Understand what lag and latency mean in multiplayer games
* T19.G6.00H: Understand what servers are in multiplayer games


---

ID: T19.G7.00C
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand network delay and its impact on gameplay
Description: Students learn that network delay causes actions to appear delayed on other players' screens. They understand that fast-paced games are more affected by delay than slow-paced games. They test their games with players in different locations and observe delay effects. They design gameplay that accounts for delay (avoid requiring frame-perfect timing, provide visual feedback for actions, use prediction/compensation techniques). They explain how network architecture choices affect delay tolerance.

Dependencies:
* T19.G6.00G: Understand what lag and latency mean in multiplayer games
* T19.G7.00B: Choose appropriate server locations to minimize lag


---

ID: T19.G7.01
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Build a cooperative puzzle with shared progress counters
Description: Students design a multiplayer task where players must work together toward shared goals (e.g., both press switches simultaneously, collect items together). They maintain progress counters that all players can see and update. They broadcast progress updates and check win conditions cooperatively. They test with two players to verify cooperation is required and progress synchronizes correctly. They explain how cooperative mechanics encourage communication and teamwork.

Dependencies:
* T19.G6.08: Create shared world objects that stay synchronized
* T19.G6.09: Display a synchronized scoreboard for multiplayer sessions


---

ID: T19.G7.02
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Implement a ready-up system before the game starts
Description: Students create a lobby where players click a "Ready" button that broadcasts their status. The host monitors the player list and starts the game only when all connected players have marked themselves ready. They use player count and ready status to control game start. They test with two windows by marking players ready and verifying the game doesn't start until all are ready. They explain why ready-up systems improve multiplayer experience (ensures everyone is prepared, prevents unfair starts, gives time to join).

Dependencies:
* T19.G6.10A: Detect when players join or leave the game
* T19.G6.04C: Broadcast multiplayer messages with parameters


---

ID: T19.G7.03
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Choose what data to synchronize versus keep local
Description: Students decide which variables should sync across all clients (scores, positions, game state) versus stay local (UI state, sounds, visual effects). They use broadcasts for event-driven sync and synchronized blocks for continuous updates. They understand that over-synchronizing causes network lag while under-synchronizing causes inconsistent game states. They test by deliberately over/under-synchronizing and observing problems. They develop judgment about synchronization trade-offs based on game requirements.

Dependencies:
* T19.G6.05A: Use synchronized speed x/y blocks for movement
* T19.G6.04C: Broadcast multiplayer messages with parameters
* T09.G5.01: Store and retrieve game state using variables


---

ID: T19.G7.04
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Scale game logic to handle variable player counts
Description: Students refactor scripts to work correctly with any number of players (2, 3, 4, or more). They loop over the player list when creating sprites, updating displays, or distributing objectives. They use the player list length to determine actual player count and adjust accordingly. They test with different player counts to verify the game adapts correctly. They explain why scalable design is important (reusability, flexibility, better player experience across different group sizes).

Dependencies:
* T19.G6.10A: Detect when players join or leave the game
* T07.G5.01: Use a loop to repeat a task an exact number of times
* T09.G5.01: Store and retrieve game state using variables


---

ID: T19.G7.05
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Balance starting conditions and scoring for fairness
Description: Students audit spawn points, turn order, and scoring rules to identify and eliminate built-in advantages. They test with multiple players and document how changes improve game balance. They understand that fair games give all players equal opportunities to win (spawn positions equidistant from objectives, alternating turn order, symmetric scoring). They iteratively test and refine balance. They explain why fairness is important for competitive multiplayer (player satisfaction, replay value, perceived legitimacy).

Dependencies:
* T19.G6.09: Display a synchronized scoreboard for multiplayer sessions
* T19.G6.10A: Detect when players join or leave the game


---

ID: T19.G7.06
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Choose when to use passwords vs public games
Description: Students learn when to use passwords (private games with friends, controlled access, teaching environments) versus empty passwords (public games open to anyone, matchmaking, open lobbies). They understand trade-offs: passwords keep games private but require coordination (sharing passwords), public games are easier to join but may have unwanted players. They implement both types and discuss use cases. They explain password security basics (don't broadcast publicly, share through private channels, change if compromised).

Dependencies:
* T19.G6.01A: Create a basic multiplayer game room


---

ID: T19.G7.07
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Debug why sprites aren't synchronizing
Description: Students identify and fix common synchronization problems. They check if they used synchronized movement blocks instead of regular movement blocks. They verify that sprites were registered with add sprite to game. They use print statements to trace execution on both clients and compare outputs. They test changes with two windows to verify fixes work. They develop a systematic debugging approach for multiplayer synchronization issues.

Dependencies:
* T19.G6.01G: Test a multiplayer game with two browser windows
* T19.G6.05A: Use synchronized speed x/y blocks for movement
* T13.G6.01: Trace complex code with multiple variables


---

ID: T19.G7.08
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Test multiplayer games with 3+ players
Description: Students test their games with three or more players to identify issues that only appear at scale (unbalanced gameplay, confusing UI, performance problems, edge cases in player management). They recruit additional testers or use multiple devices/windows. They document bugs and balance issues discovered during multi-player testing. They understand that 2-player testing is insufficient for games designed for larger groups. They explain why comprehensive testing improves game quality.

Dependencies:
* T19.G6.01G: Test a multiplayer game with two browser windows
* T19.G7.04: Scale game logic to handle variable player counts


---

ID: T19.G7.09
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Design fair starting conditions for variable player counts
Description: Students design spawn systems that maintain fairness regardless of how many players join (2, 3, 4, or more). They implement dynamic spawn point distribution (evenly space players, rotate through spawn zones, randomize fairly). They ensure no player has a systematic advantage based on join order or spawn location. They test with different player counts and verify fairness. They explain the relationship between player count, spawn distribution, and competitive balance.

Dependencies:
* T19.G7.04: Scale game logic to handle variable player counts
* T19.G7.05: Balance starting conditions and scoring for fairness
* T09.G5.01: Store and retrieve game state using variables


---

## GRADE 8 SKILLS (Expert/Architecture)

---

ID: T19.G8.01
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Implement team assignment or simple matchmaking
Description: Students automatically assign players to teams based on join order, player count, or role selection. They ensure teams are balanced in size and update assignments when players join or leave. They use loops and conditionals to distribute players evenly across teams. They display team assignments to all players. They test with variable player counts to verify balanced distribution. They explain how matchmaking algorithms improve multiplayer experience (fair teams, reduced setup time, better matches).

Dependencies:
* T19.G7.04: Scale game logic to handle variable player counts
* T19.G7.00A: Implement different behaviors for different roles
* T07.G6.01: Trace nested loops with variable bounds


---

ID: T19.G8.02
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Implement host-authoritative validation to prevent cheating
Description: Students restructure their game so clients request actions (score increase, movement, item collection) but only the host validates and applies them. The host rejects impossible actions (teleporting, instant score, invalid moves) to maintain fair play. They understand that client-side validation can be bypassed but host validation cannot. They test by attempting to cheat and verifying the host blocks invalid actions. They explain the security benefits of host-authoritative architecture.

Dependencies:
* T19.G7.03: Choose what data to synchronize versus keep local
* T19.G7.04: Scale game logic to handle variable player counts
* T08.G6.01: Use conditionals to control simulation steps


---

ID: T19.G8.03
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Implement reconnection handling
Description: Students detect when a player's connection drops and implement reconnection logic. They save player state before disconnection, allow the player to rejoin the same game, and restore their state (score, position, role) upon reconnection. They test by simulating disconnections and verifying smooth reconnection. They explain why reconnection handling improves player experience (network issues are common, prevents losing progress, maintains game flow).

Dependencies:
* T19.G6.01F: Check connection status and display feedback
* T19.G6.10C: Remove sprites and clean up when players leave
* T19.G8.02: Implement host-authoritative validation to prevent cheating


---

ID: T19.G8.04
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Debug message delivery timing issues
Description: Students identify when messages arrive in different orders on different clients, causing state divergence. They understand that network messages have variable delays. They add sequence numbers or timestamps to broadcasts to debug ordering. They implement acknowledgement systems to ensure critical messages are received. They test by observing message timing with print statements across multiple clients. They develop strategies to handle out-of-order messages (ignore duplicates, re-order based on timestamps).

Dependencies:
* T19.G7.07: Debug why sprites aren't synchronizing
* T19.G7.03: Choose what data to synchronize versus keep local
* T06.G6.01: Trace event execution paths in a multi-event program
* T13.G6.01: Trace complex code with multiple variables


---

ID: T19.G8.05.01
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Diagram client-server message flow
Description: Students create diagrams showing how messages flow between clients and the server in their multiplayer game. They map specific game actions (player moves, scores, collides) to message exchanges (client sends input → server processes → server broadcasts update → clients receive and display). They identify synchronization points where all clients must agree on state. They use their diagrams to explain game architecture to others. They understand that visualizing message flow helps identify bottlenecks and bugs.

Dependencies:
* T19.G7.03: Choose what data to synchronize versus keep local
* T19.G7.04: Scale game logic to handle variable player counts


---

ID: T19.G8.05.02
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Identify synchronization points in your game
Description: Students analyze their game to identify all points where synchronization is required (game start, score changes, player actions, collisions, game end). They categorize synchronization by type (continuous position updates, discrete events, state transitions). They document which blocks/messages handle each synchronization point. They verify that all critical game events are properly synchronized by testing with two windows. They explain why identifying synchronization points is important for debugging and optimization.

Dependencies:
* T19.G8.05.01: Diagram client-server message flow
* T19.G7.03: Choose what data to synchronize versus keep local


---

ID: T19.G8.05.03
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Trace a single game action through the system
Description: Students select one game action (player scores, collects item, wins round) and trace its complete execution path: (1) user input triggers local code, (2) message broadcast to all clients, (3) all clients receive and process message, (4) all clients update their displays. They use print statements at each stage to verify execution order and data values. They create execution diagrams showing the complete flow. They explain how tracing improves understanding of system behavior and helps identify bugs.

Dependencies:
* T19.G8.05.02: Identify synchronization points in your game
* T06.G6.01: Trace event execution paths in a multi-event program
* T13.G6.01: Trace complex code with multiple variables


---

ID: T19.G8.05.04
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Identify and explain performance bottlenecks
Description: Students identify parts of their multiplayer game that cause lag or slow performance. They recognize common bottlenecks: broadcasting every frame, too many Dynamic sprites, large broadcast parameters, inefficient loops. They use timing and observation to measure performance. They propose optimizations (reduce broadcast frequency, use Static sprites, minimize parameter size). They test before and after optimizations to verify improvements. They explain the relationship between network traffic, game complexity, and performance.

Dependencies:
* T19.G8.05.03: Trace a single game action through the system
* T19.G7.03: Choose what data to synchronize versus keep local


---

ID: T19.G8.06
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Understand what information is shared in multiplayer games
Description: Students learn what data is shared with other players in CreatiCode multiplayer: display names, roles, positions, broadcast messages, but NOT account credentials, passwords, or personal information. They understand that game room passwords protect the room, not individual players. They learn that all players in a room can see all public game data. They design games that don't expose private information accidentally. They explain privacy implications of data sharing in multiplayer contexts.

Dependencies:
* T19.G6.01B: Join a basic multiplayer game room
* T19.G6.04C: Broadcast multiplayer messages with parameters


---

ID: T19.G8.07
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Optimize network traffic in multiplayer games
Description: Students learn that excessive broadcasts or too many Dynamic sprites cause network lag. They identify performance bottlenecks: broadcasting every frame, synchronizing unnecessary data, too many moving objects. They optimize by reducing broadcast frequency (broadcast on change, not every frame), using Static sprites where possible (walls, platforms), and only synchronizing essential data. They test before and after optimization to measure improvements. They explain the relationship between network traffic and game performance.

Dependencies:
* T19.G6.00D: Understand Dynamic vs Static sprites in multiplayer games
* T19.G7.03: Choose what data to synchronize versus keep local
* T19.G6.04C: Broadcast multiplayer messages with parameters


---

ID: T19.G8.08
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Profile and measure multiplayer performance
Description: Students use timing and counting techniques to measure multiplayer performance metrics. They measure latency (time from broadcast to receive), frame rate, and network message count. They collect performance data during gameplay. They identify performance bottlenecks using measured data (not guessing). They compare performance before and after optimizations to verify improvements. They explain why measurement is essential for optimization (intuition is often wrong, data reveals true bottlenecks).

Dependencies:
* T19.G8.07: Optimize network traffic in multiplayer games
* T09.G6.01: Model real-world quantities using variables and formulas


---

ID: T19.G8.09
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Handle error cases in multiplayer games
Description: Students identify common multiplayer error cases: connection failures, full games, invalid passwords, player disconnections mid-game, host leaving. They implement error handling for each case: display clear error messages, provide retry options, clean up properly, prevent game corruption. They test error cases deliberately and verify handling works correctly. They explain why robust error handling improves player experience (reduces frustration, provides clarity, maintains game stability).

Dependencies:
* T19.G6.01F: Check connection status and display feedback
* T08.G6.01: Use conditionals to control simulation steps


---

ID: T19.G8.10
Topic: T19 – Multiplayer Apps: Grade 6–8 Skill List
Skill: Compare peer-to-peer vs client-server architectures
Description: Students learn the differences between peer-to-peer (all players equal, no central authority) and client-server (one host, multiple clients) architectures. They understand that CreatiCode uses client-server with the host as the authoritative server. They compare advantages (client-server prevents cheating, peer-to-peer has no single point of failure) and disadvantages (host leaving breaks client-server, peer-to-peer harder to synchronize). They explain why client-server is common for games requiring fairness and consistency.

Dependencies:
* T19.G6.00B: Understand the host-client model and game rooms in multiplayer games
* T19.G8.05.04: Identify and explain performance bottlenecks


---
