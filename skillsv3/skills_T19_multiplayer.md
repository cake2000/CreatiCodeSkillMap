# T19 – Multiplayer Apps: K–8 Skill List (Draft v1)

Topic reference: `T19 Multiplayer Apps` in `domains_topics_overview.md`
Domain: Programming (D2) · CSTA focus: PRO‑PD, SAS‑NW (with links to PRO‑PF, ALG‑AF, CAS‑ET)

Each skill below has:

- a stable **ID** (`T19.G<grade>.<nn>`),
- an IXL‑style **short name**,
- a **description** (what understanding/behavior it targets),
- a **challenge format** (the typical problem type to assess it).

Where relevant, a primary **CSTA code** is noted.

---

## Grade K (PreK–K)

Multiplayer and connected apps are introduced through intuitive ideas about sharing, taking turns, and basic networked concepts—not yet as code.

### T19.GK.01 – Understand that computers connect to share messages

- **Short name:** Computers send messages to each other
- **Description:** Students recognize that computers and devices can send information to each other over networks. They explore the idea that when you play a game online or send a message, your device talks to another person's device far away.
- **Challenge format:** Concept, interactive activity. A simple animation shows two characters on different screens sending a message or emoji to each other. Students identify what happens when one character sends something. Auto‑grading checks understanding of the basic connection idea.
- **CSTA:** SAS‑NW (Networks: basic connection awareness).

### T19.GK.02 – Recognize turn‑taking in game rules

- **Short name:** Notice when games take turns
- **Description:** Students observe or play a very simple sequential game (e.g., a guessing game, a pass‑the‑message game) and identify that players must wait for others to move or respond. This lays groundwork for understanding synchronization in multiplayer games.
- **Challenge format:** Concept, guided observation. Show a picture or short video of two players playing a turn‑based game (like tic‑tac‑toe). Ask students "Whose turn is it?" or "What happens after Player 1 moves?" Auto‑grading checks selection of the correct turn or action sequence.
- **CSTA:** SAS‑NW (Networks: basic communication order).

### T19.GK.03 – Describe how sharing screens lets friends play together

- **Short name:** Understand screen sharing for games
- **Description:** Students learn that when multiple people look at the same screen or device, they can play together. They understand the concept that all players see the same thing (e.g., a shared game board) and that changes one player makes appear for everyone.
- **Challenge format:** Concept, picture-based activity. Show pictures of children gathered around a tablet or screen playing a game. Students explain what they see and why they think everyone can play together. Auto‑grading checks understanding that the shared screen shows the game state to all players.
- **CSTA:** SAS‑NW (Networks: shared resources).

---

## Grade 1

Grade 1 focuses on recognizing basic networked communication and simple game hosting/joining concepts without coding.

### T19.G1.01 – Identify who the host and guest are in a simple game

- **Short name:** Spot the host and guest in a game
- **Description:** Students examine a simple multiplayer game scenario (picture or short animation) and identify which player set up the game (host) and which player joined it (guest). This builds awareness of different player roles.
- **Challenge format:** Concept, multiple choice. Show a scenario: "Alex opens a new game room and invites friends to join. Taylor sees a list of games and clicks on Alex's game to play." Students choose: "Who is the host?" and "Who is the guest?" Auto‑grading checks both role identifications.
- **CSTA:** SAS‑NW (Networks: roles in communication).

### T19.G1.02 – Understand that both players see the same game state

- **Short name:** Both players see the same board
- **Description:** Students understand that in a multiplayer game, if one player moves their character or piece, the other player's screen also updates to show the same change. This is the foundation for synchronized games.
- **Challenge format:** Concept, traced scenario. Show a simple 2D grid-based game where Player 1 moves left. Students identify what Player 2 sees on their screen and select the matching picture (showing the same updated position). Auto‑grading compares to the correct synchronized view.
- **CSTA:** SAS‑NW (Networks: data synchronization concept).

### T19.G1.03 – Match a networked game description to the term "multiplayer"

- **Short name:** Recognize multiplayer games
- **Description:** Students read or hear simple descriptions of games (e.g., "Two friends play tag on different computers at home") and identify which ones are "multiplayer" (multiple people playing together over a network).
- **Challenge format:** Concept, multiple choice or drag‑match. Present 3–4 game scenarios; students mark which ones are multiplayer games. Auto‑grading checks correct identification.
- **CSTA:** SAS‑NW (Networks: basic understanding).

---

## Grade 2

Grade 2 introduces simple block‑based actions related to multiplayer games (joining, basic data sharing) and explores the idea of synchronized state.

### T19.G2.01 – Join a game in a CreatiCode project

- **Short name:** Click to join a multiplayer game
- **Description:** Students use a pre-built CreatiCode project where they can click a "Join Game" button (or similar UI element) and see their name and sprite appear in a shared game room. They experience being a guest joining an existing multiplayer session.
- **Challenge format:** Coding, interactive guided task. Provided: a CreatiCode project with a button labeled "Join Game" (already set up to join a specific test room). Students click the button, see the join confirmation, and view the list of players. Auto‑grading checks that the student successfully joined the room (verified by the game state or player list updating).
- **CSTA:** PRO‑PD (Program Development: using multiplayer blocks).

### T19.G2.02 – Observe your sprite move on another player's screen

- **Short name:** See your move appear for others
- **Description:** In a two‑player setup, students control their sprite and notice that when they move it, the other player (controlled by the teacher or AI) also sees it move in real time. This builds intuitive understanding of state synchronization.
- **Challenge format:** Coding, interactive observation. Starter project: a simple game where the student controls a sprite with arrow keys. A test "opponent" sprite (cloud‑controlled) also moves randomly. The student can observe both their sprite and the opponent's sprite updating live. Auto‑grading runs the project with a test opponent and verifies that both sprites update correctly when either player's script triggers movement.
- **CSTA:** SAS‑NW (Networks: observing synchronized data).

### T19.G2.03 – Broadcast a simple message to all players

- **Short name:** Send a message to everyone
- **Description:** Students use a multiplayer broadcast block (e.g., "broadcast [message] to all players") to send a simple signal (like "Jump!" or "Turn red!") and observe that all players' sprites respond to that message.
- **Challenge format:** Coding, starter project. Provided: a multiplayer project with sprites for each player and a broadcast block. Prompt: "Use the broadcast message block to make all sprites say 'Ready?' at the same time." Students fill in the message and click a button to broadcast. Auto‑grading checks that (1) the broadcast block is used correctly, (2) all sprites respond with the message, and (3) the message is displayed or spoken.
- **CSTA:** PRO‑PD (Program Development: using broadcast blocks).

### T19.G2.04 – Trace what happens when a shared variable changes

- **Short name:** Trace a shared score update
- **Description:** Students read a simple multiplayer script where a shared variable (like "score") changes when a player collects a coin. They predict what value both players' screens will show after the collection.
- **Challenge format:** Concept, code‑reading item. Show a small script: "When sprite touches coin, change score by 10." Students are asked "If Player 1 collects a coin, what will Player 2's score display show?" with numeric answer choices. Auto‑grading compares the selected score to the correct calculated value.
- **CSTA:** PRO‑PD (Program Development: understanding shared state).

---

## Grade 3

Grade 3 introduces more complex multiplayer game mechanics: creating/hosting games, role assignment, and conditional responses to networked events.

### T19.G3.01 – Create a multiplayer game room with a name and password

- **Short name:** Set up a multiplayer game to host
- **Description:** Students use the "create game" block to start a multiplayer game session, providing a game name, an optional password, and their player name. They understand the role of the host in setting up the game for others to join.
- **Challenge format:** Coding, starter project. Provided: a CreatiCode project with the "create game" block partially filled in. Prompt: "Create a new game called 'DodgeGame' with password '2023' and your name 'Player1'." Students complete the block parameters. Auto‑grading verifies that (1) the game was created with correct parameters, (2) the game appears in the game list with the right name, and (3) the hosting player is listed correctly.
- **CSTA:** PRO‑PD (Program Development: game server interaction).

### T19.G3.02 – Filter the game list to find and join a specific game

- **Short name:** Search and join a game from a list
- **Description:** Students use a "list games" block to see available multiplayer games, then filter or choose the correct game based on its name, and join it using the join game block with matching parameters (game name, password).
- **Challenge format:** Coding, starter project. Provided: a project with a "list games" block that displays available games (populated with test games like "Pong Room", "Tag Arena", "Chase Game"). Prompt: "Find the game named 'Pong Room' and join it with password 'abc'." Students use the join block with the correct parameters. Auto‑grading checks (1) correct game selection, (2) correct password entry, (3) successful join confirmed in the game state.
- **CSTA:** PRO‑PD (Program Development: networking API usage).

### T19.G3.03 – Assign roles to players and check a player's role

- **Short name:** Set and check player roles
- **Description:** Students specify a role when creating or joining a game (e.g., "Red team", "Goalie", "Catcher") and use a "get player role" reporter block to check what role other players have, allowing role‑specific game logic.
- **Challenge format:** Coding, starter project. Provided: a multiplayer project where the student creates a game with role "Seeker" and invites a test player with role "Hider". Prompt: "Use a block to check the other player's role. If they are 'Hider', say 'I'm seeking you!' otherwise say 'We are teammates!'." Students add a conditional that reads the other player's role and responds appropriately. Auto‑grading simulates both role assignments and checks that the correct speech output occurs.
- **CSTA:** PRO‑PD (Program Development: role‑based logic).

### T19.G3.04 – Synchronize a position variable across multiplayer instances

- **Short name:** Sync position across players
- **Description:** Students use a multiplayer variable (or understand how sending/receiving networked values works) to keep one player's x/y position synchronized across all instances so all players see the sprite in the same location.
- **Challenge format:** Coding, starter project. Provided: a two‑player project where the student controls a sprite. Prompt: "Use the multiplayer feature to keep your sprite's x position the same on both players' screens. When you move right, the other player should see you move right too." Students use blocks to send or sync the x position variable. Auto‑grading runs both instances, moves the student's sprite, and verifies that the opponent's view updates to reflect the correct x position.
- **CSTA:** PRO‑PD (Program Development: data synchronization).

---

## Grade 4

Grade 4 builds multiplayer games with more sophisticated synchronization: handling multiple synced variables, responding to player join/leave events, and simple turn mechanics.

### T19.G4.01 – Sync multiple variables (position, score, state) in a multiplayer game

- **Short name:** Sync position, score, and state
- **Description:** Students extend synchronization to multiple game variables: each player's position (x/y), score, health, or animation state. They use separate multiplayer sends or understand how a shared data structure keeps all these in sync.
- **Challenge format:** Coding, starter project. Provided: a 2D multiplayer game where each sprite has x, y, score, and costume (alive/dead state). Prompt: "Make sure both players see the same score and both sprite positions. When Player 1 collects a coin, Player 2 should see the score increase." Students add blocks to sync score changes and position updates. Auto‑grading runs multiple test cases: one player moves (position syncs), one player collects a coin (score syncs), and verifies that both instances reflect all changes correctly.
- **CSTA:** PRO‑PD (Program Development: complex state management).

### T19.G4.02 – Respond to a player joining or leaving the game

- **Short name:** Handle player join/leave events
- **Description:** Students use event blocks like "when [player] joins game" or "when [player] leaves game" to trigger actions (e.g., starting a countdown, removing a player's sprite, showing a welcome message).
- **Challenge format:** Coding, starter project. Provided: a multiplayer project with a lobby screen. Prompt: "When a guest player joins, send a broadcast message 'Game Starting!' and make all sprites move to the center of the stage. When a player leaves, display 'Player Left—Waiting for new player'." Students add the join/leave event blocks and appropriate responses. Auto‑grading simulates a player joining and leaving, verifying that the correct broadcasts and sprite movements occur.
- **CSTA:** PRO‑PD (Program Development: event handling in networked systems).

### T19.G4.03 – Implement a simple turn-taking mechanism

- **Short name:** Create turn‑based multiplayer logic
- **Description:** Students use a shared variable (e.g., "current_turn") and conditionals to ensure only one player can act at a time. They may track turns with a counter or flag, advancing it when one player finishes their action.
- **Challenge format:** Coding, starter project. Provided: a turn‑based game (like checkers or tic‑tac‑toe simulator) with a "current_turn" variable initialized to 1. Prompt: "Make it so Player 1 can only move when current_turn equals 1. After they move, set current_turn to 2 so Player 2 can move." Students add conditionals around move blocks and update the turn variable. Auto‑grading runs the game, verifies that moves are only allowed on a player's turn, and that turn changes work correctly.
- **CSTA:** PRO‑PD (Program Development: turn‑based synchronization).

### T19.G4.04 – Trace a multiplayer game script to predict final states

- **Short name:** Trace multiplayer game logic
- **Description:** Students read a simple multiplayer script (with position syncs, score updates, and joins) and predict the final state of the game (both players' positions, shared score, player list) after a sequence of actions.
- **Challenge format:** Concept, code‑reading item. Show a short multiplayer script and a sequence of actions: "Player 1 joins game 'Test', moves to (50, 50). Player 2 joins with a different role. Player 1 collects a coin (score +5)." Students predict: "What is Player 1's x position on Player 2's screen?" or "What is the shared score?" with numeric/text answer choices. Auto‑grading compares to the correct traced values.
- **CSTA:** PRO‑PD (Program Development: understanding networked state transitions).

---

## Grade 5

Grade 5 explores more complex networked mechanics: shared game worlds, player list management, real‑time chat/messaging, and collision/interaction detection across networked players.

### T19.G5.01 – Build a shared lobby or chat interface with message display

- **Short name:** Create a shared message board
- **Description:** Students build a simple chat or message log system where one player sends a message (via ask and wait), the message is broadcast to all players, and all players see an updated list or log of messages on screen.
- **Challenge format:** Coding, starter project. Provided: a multiplayer project with a label widget area for displaying messages and an input field. Prompt: "Create a chat feature: when a player types a message and presses 'Send', broadcast it to all players. All players should see the new message added to a displayed list." Students add send/receive logic and update a list or label with incoming messages. Auto‑grading runs multiple players, sends test messages, and verifies that all instances receive and display messages correctly.
- **CSTA:** PRO‑PD (Program Development: real‑time communication systems).

### T19.G5.02 – Maintain and display a list of connected players

- **Short name:** Show all connected players
- **Description:** Students use a "get players in game" or "list players" block to retrieve all connected players and display their names and roles (e.g., in a label widget or variable). They may update this list dynamically as players join/leave.
- **Challenge format:** Coding, starter project. Provided: a multiplayer project with a label widget and a "get players" block. Prompt: "Display a list of all players currently in the game, showing each player's name and role." Students loop through the player list and format the display. Auto‑grading verifies (1) the correct number of players is displayed, (2) names and roles are accurate, and (3) the list updates when players join/leave.
- **CSTA:** PRO‑PD (Program Development: handling collections of networked data).

### T19.G5.03 – Detect and respond to collision between synced player sprites

- **Short name:** Detect collision with other players
- **Description:** Students use the "touching [sprite]" block or equivalent to detect when their sprite collides with another player's synced sprite. They respond with actions like scoring a point, changing state, or broadcasting an event.
- **Challenge format:** Coding, starter project. Provided: a multiplayer tag or chase game with two sprites (player and opponent) synced across instances. Prompt: "When your sprite touches the other player's sprite, increase your score by 1 and broadcast 'Tagged!' to all players." Students add a touching check inside a loop and appropriate response blocks. Auto‑grading simulates movement that causes collision and verifies that the score increments and broadcast occurs.
- **CSTA:** PRO‑PD (Program Development: interaction detection in networked systems).

### T19.G5.04 – Implement a simple scoring system with a shared leaderboard

- **Short name:** Build a shared leaderboard
- **Description:** Students maintain individual scores for each player (via separate variables or a table) and display them in a leaderboard format. Scores update in real time as players perform actions, and all players see the same leaderboard.
- **Challenge format:** Coding, starter project. Provided: a multiplayer project with player data structure and a label widget area. Prompt: "Create a leaderboard that shows each player's name and score. Update scores when players collect coins, and display the leaderboard sorted by highest score first." Students manage score variables, maintain a sorted list, and display it. Auto‑grading runs the game, awards points to different players, and verifies that the leaderboard displays correctly and is visible to all players.
- **CSTA:** PRO‑PD (Program Development: shared data management and presentation).

---

## Grade 6

In middle school, multiplayer games become more sophisticated, incorporating world state management, latency awareness, and collaborative problem-solving in networked environments.

### T19.G6.01 – Design a multiplayer game world with persistent state (coins, obstacles, etc.)

- **Short name:** Manage world state in multiplayer
- **Description:** Students design a game where the world (stage) has persistent, shared objects (coins, platforms, enemies) that all players interact with. When one player collects a coin, it disappears for both players. All players see the same world state.
- **Challenge format:** Coding, design and implementation challenge. Prompt: "Design a multiplayer game where coins are placed on the stage. When any player collects a coin, it should disappear for everyone and add 1 to the global score. The same coins must be available to all players." Students create a system to spawn coins, sync their collection, and remove them. Auto‑grading verifies (1) coins are shared (same positions for all players), (2) collection updates global state correctly, and (3) coins disappear across all instances after collection.
- **CSTA:** PRO‑PD (Program Development: managing shared game world state).

### T19.G6.02 – Handle network latency with buffering or prediction

- **Short name:** Manage latency in real-time games
- **Description:** Students learn that network messages take time to arrive and implement simple strategies like buffering recent position updates or predicting a player's next position. They understand that a brief delay is normal and design games that tolerate or mitigate this.
- **Challenge format:** Concept and coding, mixed. Concept part: explain why a player's sprite on another player's screen might be slightly "behind." Coding part: Provided a multiplayer project with intentional delay blocks, students use a position buffer or "glide toward" to smooth out the visual appearance of synced movement. Auto‑grading checks that the student explains latency and that the smoothing mechanism reduces visual jitter.
- **CSTA:** PRO‑PD (Program Development: robust networked game design).

### T19.G6.03 – Implement a collaborative puzzle or challenge with shared objectives

- **Short name:** Build a cooperative multiplayer game
- **Description:** Students create a game where both players must work together toward a common goal (e.g., gathering items, reaching a location, solving a puzzle together). Progress is shared and visible to both players.
- **Challenge format:** Coding, collaborative design challenge. Prompt: "Create a cooperative game where two players must each collect 5 items and bring them to a shared goal location. Display a shared progress counter showing total items collected by both players." Students design the item spawning, collection logic, shared progress tracking, and win condition. Auto‑grading simulates both players collecting items, verifies the shared counter updates correctly, and detects when the shared goal is met.
- **CSTA:** PRO‑PD (Program Development: collaborative game mechanics).

### T19.G6.04 – Trace a networked game's state changes across multiple broadcast events

- **Short name:** Trace multicast message chain reactions
- **Description:** Students read a multiplayer script where several broadcast events are sent in sequence (e.g., "Game Starting" → all sprites move to center → "Ready?" → players can move). They predict the final state and behavior of the game.
- **Challenge format:** Concept, code‑reading item with trace. Show a multiplayer script with several broadcast blocks and listeners. Provide a sequence of simulated player actions and broadcasts. Students trace through and predict: "After these broadcasts and player actions, what will both players' sprites be doing?" Auto‑grading compares the trace to the correct predicted behavior.
- **CSTA:** PRO‑PD (Program Development: event-driven networked systems).

---

## Grade 7

Grade 7 emphasizes algorithmic multiplayer game mechanics and scalability: handling variable numbers of players, implementing algorithms for matchmaking or game balancing, and understanding performance implications of network synchronization.

### T19.G7.01 – Design multiplayer game balance and fairness mechanisms

- **Short name:** Build fair game mechanics for multiplayer
- **Description:** Students analyze or design multiplayer games with fairness in mind: equal starting positions, identical rules for all players, avoiding advantages from network latency, and balanced scoring systems. They discuss why fairness matters in multiplayer games.
- **Challenge format:** Coding and concept. Coding part: Provided a basic competitive multiplayer game, students identify and fix an unfairness (e.g., one player always moves first, or position syncing favors one player). They implement a fair initialization or turn system. Concept part: students explain why the change improves fairness. Auto‑grading checks (1) the fairness fix is implemented, (2) all players have equal opportunities under the new rules, and (3) the student's explanation addresses equity.
- **CSTA:** PRO‑PD (Program Development: ethical game design in networked systems).

### T19.G7.02 – Implement dynamic player matching or team assignment

- **Short name:** Matchmake players into teams
- **Description:** Students use logic to automatically assign players to teams or matches based on criteria (e.g., first two players to join are a team, or random assignment). They may track team membership in a variable or list and ensure fair distribution.
- **Challenge format:** Coding, starter project. Provided: a multiplayer project with multiple players joining a game. Prompt: "Assign the first two players to Team Red and the next two to Team Blue. Display each player's team on screen." Students implement a counter or list to track player joins and assign teams dynamically. Auto‑grading simulates four players joining in sequence and verifies correct team assignments and display.
- **CSTA:** PRO‑PD (Program Development: algorithmic player management).

### T19.G7.03 – Evaluate network efficiency: which data must be synced vs. local-only

- **Short name:** Optimize what data is networked
- **Description:** Students analyze a multiplayer game and determine which variables should be synchronized across players (e.g., positions, shared score) and which can be local-only (e.g., individual power-up effects, temporary animations). They understand trade-offs between consistency and bandwidth.
- **Challenge format:** Concept, multiple choice with explanation. Present a multiplayer game scenario (e.g., a co-op action game) with 8 variables. For each, students choose "Must sync", "Local only", or "Optional". They explain one or two choices (e.g., "Player position must sync so both players see where they are, but my health can be local because only I need to know"). Auto‑grading checks selections against a reference answer and evaluates explanations for reasonable logic.
- **CSTA:** PRO‑PD (Program Development: systems optimization).

### T19.G7.04 – Handle variable numbers of players (2, 3, 4, or more) in a single game

- **Short name:** Scale multiplayer game for many players
- **Description:** Students design a multiplayer game that can accommodate more than two players. They use loops and lists to manage a variable number of player sprites, score entries, and positions, ensuring all players are treated fairly regardless of count.
- **Challenge format:** Coding, algorithmic challenge. Provided: a multiplayer project framework that supports up to 6 players. Prompt: "Write a script that works for any number of players (2–6): initialize a sprite and score display for each connected player, and display all scores on a leaderboard." Students use loops over the player list and create dynamic sprite/label instances. Auto‑grading tests with 2, 3, 4, and 6 players, verifying that all are initialized, synced, and displayed correctly.
- **CSTA:** PRO‑PD (Program Development: scalable networked systems).

---

## Grade 8

Grade 8 builds toward high school by introducing advanced multiplayer concepts: message reliability and ordering, state validation, anti-cheating measures, and understanding the architecture of multiplayer systems.

### T19.G8.01 – Implement anti-cheat validation (server-side or consensus checking)

- **Short name:** Prevent cheating in multiplayer games
- **Description:** Students implement basic anti-cheat measures: a shared validation rule (e.g., "score can only increase by 1 per coin collection, not arbitrary amounts") or a server-mediated authority (e.g., the host validates coin collection before updating the score). They understand the concept that trusted authorities prevent cheating.
- **Challenge format:** Coding, security challenge. Provided: a multiplayer game where players collect coins to gain points. Currently, any player can change the score directly (bad). Prompt: "Modify the game so only the host can validate coin collection and award points. Guests send a 'coin collected' message, and the host decides if it's valid before updating the score." Students implement a validation scheme. Auto‑grading tests attempts to cheat (e.g., directly modifying score) and verifies that cheating is prevented or detected.
- **CSTA:** PRO‑PD (Program Development: security in networked systems).

### T19.G8.02 – Trace a message exchange to verify game state consistency

- **Short name:** Verify game state across network messages
- **Description:** Students trace the sending and receiving of multiplayer messages (broadcasts, role-based sends) to ensure all players end up with consistent game state. They identify potential inconsistency bugs (e.g., message received out of order, or one player doesn't receive an update).
- **Challenge format:** Concept, message sequence trace. Present a scenario: Player 1 collects a coin (sends "coin_collected" message). Player 2 moves (sends "position" update). Both messages are received by both players, but in different orders. Students trace the final state on each player's side and identify if the game state is consistent. They identify which variables could become inconsistent. Auto‑grading checks the trace and consistency analysis.
- **CSTA:** PRO‑PD (Program Development: understanding message ordering and consistency).

### T19.G8.03 – Design a multiplayer game with a persistent server/database for high scores or player data

- **Short name:** Save multiplayer game data persistently
- **Description:** Students connect a multiplayer game to cloud storage or a database backend (using CreatiCode's cloud blocks or equivalent) to save and retrieve player data (high scores, achievements, player profiles) across sessions and matches. They understand that persistent data lives beyond a single game session.
- **Challenge format:** Coding, integration challenge. Provided: a multiplayer game with a leaderboard. Prompt: "After the game ends, save the final scores to a cloud database. When a new game starts, load and display the all-time leaderboard from the database." Students add cloud save/load blocks around the score data. Auto‑grading runs a game, checks that scores are saved to cloud, closes the game, starts a new session, and verifies that the leaderboard is restored correctly.
- **CSTA:** PRO‑PD (Program Development: persistence in networked systems).

### T19.G8.04 – Analyze the architecture and data flow of a multiplayer system

- **Short name:** Understand multiplayer system design
- **Description:** Students examine the architecture of a multiplayer game system: client (player's game instance), server (shared authority), and network. They trace how a message flows from one client to the server, is processed, and broadcast back. They identify potential bottlenecks or failure points.
- **Challenge format:** Concept, design analysis. Present a diagram or description of a multiplayer system. Ask: "How does the game ensure Player 1's coin collection is seen by Player 2?" Students explain the message flow (Player 1 sends "coin" → Server validates → Server broadcasts update → Player 2 receives and updates UI). They identify one potential issue (e.g., network delay, server overload). Auto‑grading evaluates the explanation for correctness and identification of at least one realistic architectural concern.
- **CSTA:** PRO‑PD (Program Development: systems architecture); SAS‑NW (Networks: understanding system design).

---

## Summary

This T19 skills progression builds from kindergarten's intuitive understanding of networked connection and turn-taking through grade 8's advanced concepts of anti-cheating, message consistency, and system architecture. Students progress from observing multiplayer games to designing complex networked systems, with each grade adding more sophisticated synchronization, scalability, and reliability concerns. The skills are anchored in CreatiCode's multiplayer blocks and align with CSTA's PRO-PD (Program Development) and SAS-NW (Networks) standards, with connections to broader programming and computational thinking competencies.
