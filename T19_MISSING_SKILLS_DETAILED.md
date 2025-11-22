# T19 Multiplayer Apps - Detailed Missing Skills Specifications

This document provides complete specifications for all recommended new skills.

---

## FOUNDATIONAL CONCEPT SKILLS (G6.00A-F)

### T19.G6.00A: Understand what "multiplayer" means
**Skill:** Understand what "multiplayer" means in CreatiCode games

**Description:** Students learn that multiplayer games let multiple people play together by connecting over the internet. They understand that one person "hosts" the game (creates it) and others "join" it. They identify examples of multiplayer vs single-player games and explain why multiplayer games need internet connections. They understand that all players see the same game world and can interact with each other.

**Implementation Examples:**
- Watch a demo video showing two players in the same CreatiCode game
- List 5 games and identify which are multiplayer vs single-player
- Explain in writing: "Why do multiplayer games need the internet?"
- Identify what makes a game "multiplayer": (a) multiple characters, (b) multiple people controlling different characters, (c) multiple levels

**CSTA Alignment:** IC-20-01 (Compare computing technologies)

**Dependencies:** None (this is the foundation)

**Leads to:** T19.G6.00B

---

### T19.G6.00B: Understand the host-client model
**Skill:** Understand the host-client model in multiplayer games

**Description:** Students learn that in CreatiCode multiplayer, one player is the "host" who creates the game, and other players are "clients" who join. They understand that the game only exists as long as the host is connected - if the host leaves, the game ends for everyone. They explain why this matters for game design (host should be reliable). They identify which player is the host in a running game.

**Implementation Examples:**
- Diagram showing: Host creates game → Clients join → Host leaves → Game ends
- Watch what happens when host disconnects
- Explain: "Why does the game end when the host leaves?"
- Role-play: Teacher is host, students are clients, act out joining/leaving

**CSTA Alignment:** NI-04-01 (Model how information is broken down and transmitted)

**Dependencies:**
- T19.G6.00A (multiplayer concept)

**Leads to:** T19.G6.01A (creating games), T19.G6.01B (joining games)

---

### T19.G6.00C: Understand sprite replication in multiplayer games
**Skill:** Understand sprite replication in multiplayer games

**Description:** Students learn that when they add a sprite to a multiplayer game, other players see a "replicate" copy of that sprite on their screens. They understand that the "original" sprite (on your screen) runs your code, while "replicate" sprites (on other screens) show what you're doing. They identify which sprites are originals vs replicates when testing with two windows. They explain why replication is necessary (each player needs to see all other players).

**Implementation Examples:**
- Open two browser windows, add sprite in Window 1, observe replicate in Window 2
- Label diagram: "Original sprite (runs my code)" vs "Replicate sprite (shows their actions)"
- Test: Add print statement to original, verify it doesn't print on replicate
- Explain: "Why do I see two copies of my sprite when I test with two windows?"

**CSTA Alignment:** NI-04-01, AP-13-01 (Create prototypes that use algorithms)

**Dependencies:**
- T19.G6.00B (host-client model)

**Leads to:** T19.G6.02B (adding sprites), T19.G6.04A (broadcast modes)

---

### T19.G6.00D: Understand Dynamic vs Static sprites
**Skill:** Understand Dynamic vs Static sprites in multiplayer games

**Description:** Students learn that Dynamic sprites can move and have physics (gravity, collisions), while Static sprites stay in place and act as fixed obstacles (walls, platforms). They understand that Static sprites use less network bandwidth because they don't send position updates. They choose appropriate sprite types for different game objects: players are Dynamic, walls are Static, collectible coins might be either.

**Implementation Examples:**
- Create two sprites: one Dynamic (player), one Static (wall)
- Test: Try to move Static sprite, observe it doesn't work
- Compare network traffic: game with all Dynamic vs some Static sprites
- Decision tree: "When to use Dynamic vs Static?"
- Build simple platformer: player (Dynamic), platforms (Static), moving enemies (Dynamic)

**CSTA Alignment:** AP-13-01, AP-16-02 (Incorporate existing code)

**Dependencies:**
- T19.G6.00C (replication)
- T14.G4.01 (basic physics concepts)

**Leads to:** T19.G6.02B (adding sprites)

---

### T19.G6.00E: Understand collision shapes (Rectangle vs Circle)
**Skill:** Understand collision shapes (Rectangle vs Circle) in multiplayer games

**Description:** Students learn that sprites can have Rectangle or Circle collision shapes. They understand that Rectangle is better for square/rectangular objects (walls, boxes) and Circle is better for round objects (balls, players). They test different shapes and observe how collision detection changes - circles collide smoothly at edges, rectangles have corner detection. They choose appropriate shapes for their game objects.

**Implementation Examples:**
- Add sprite as Rectangle, test collision with corners
- Change same sprite to Circle, test collision difference
- Visual diagram: Rectangle collision (corners collide) vs Circle collision (smooth)
- Match game objects to shapes: Ball→Circle, Box→Rectangle, Player→either
- Build test scene with mixed shapes, observe which collisions feel "right"

**CSTA Alignment:** AP-13-01 (Create prototypes)

**Dependencies:**
- T19.G6.00D (Dynamic/Static)
- T14.G5.01 (collision concepts)

**Leads to:** T19.G6.02B (adding sprites), T19.G6.06 (collision events)

---

### T19.G6.00F: Understand what "synchronization" means
**Skill:** Understand what "synchronization" means in multiplayer games

**Description:** Students learn that "synchronization" means keeping all players' screens showing the same thing. They understand that normal movement blocks (like "change x by 10") only affect their own screen, but synchronized blocks (like "synchronously set speed x 10 y 0") affect everyone's screen. They compare both approaches and observe the difference. They explain why synchronization is necessary for fair multiplayer games.

**Implementation Examples:**
- Test 1: Use regular "change x by 10" block, observe sprite only moves on local screen
- Test 2: Use "synchronously set speed x 10 y 0", observe sprite moves on all screens
- Open two windows, compare synchronized vs unsynchronized movement
- Explain: "What happens if we don't synchronize player movement?"
- Identify which game elements need synchronization: player positions (yes), background music (no), UI buttons (no)

**CSTA Alignment:** NI-04-01, AP-13-01

**Dependencies:**
- T19.G6.00C (replication)

**Leads to:** T19.G6.05 (synchronized movement), T19.G7.03 (choosing what to sync)

---

## SPLIT/REVISED HOSTING SKILLS (G6.01A-F)

### T19.G6.01A: Create a simple multiplayer game room
**Skill:** Create a simple multiplayer game room

**Description:** Students use the `create game` block with a game name and password to host a room. They use default values for server (US-East), capacity (4), and world dimensions (480x360). They verify the game was created by checking the `connected to game` boolean reporter. They understand that their computer is now the "host" and others can join.

**Block Used:**
```
create game named [game 1] password [123] my name [host] role [player 1] server [US-East v] capacity (4) world width (480) height (360)
```

**Implementation Examples:**
- Create game with name "MyGame" and password "secret123"
- Add conditional: if `connected to game` then say "Game created!" else say "Failed to create"
- Test: Try to create two games with same name, observe what happens
- Troubleshoot: Check internet connection if game creation fails

**CSTA Alignment:** NI-04-01, AP-13-01

**Dependencies:**
- T19.G6.00B (host-client model)
- T06.G3.09 (event timing)
- T09.G3.05 (variables for game name, password)

**Leads to:** T19.G6.01B (joining), T19.G6.01C (configuring)

---

### T19.G6.01B: Join a multiplayer game room
**Skill:** Join a multiplayer game room

**Description:** Students use the `join game` block with a game name, host name, and password to join an existing room. They provide a display name (what other players see). They verify connection using the `connected to game` reporter. They understand that they are a "client" connecting to someone else's hosted game.

**Block Used:**
```
join multiplayer game named [game 1] by host [host] from server [US-East v] with password [123] my name [player 2] role [player 2]
```

**Implementation Examples:**
- Join a game created by partner/teacher
- Add conditional: if `connected to game` then say "Joined!" else say "Failed"
- Troubleshoot common errors: wrong password, wrong host name, wrong server
- Practice: Student A hosts, Student B joins

**CSTA Alignment:** NI-04-01, AP-13-01

**Dependencies:**
- T19.G6.01A (creating games)

**Leads to:** T19.G6.02A (testing with two windows), T19.G6.05 (synchronized movement)

---

### T19.G6.01C: Configure game capacity and world dimensions
**Skill:** Configure game capacity and world dimensions

**Description:** Students learn to set capacity (max players) and world width/height when creating a game. They understand that capacity limits how many players can join (e.g., capacity 2 for 1v1 games, capacity 8 for party games). They understand that world dimensions define the playable area - sprites outside these bounds may wrap around or be hidden. They test how capacity limits affect who can join.

**Block Used:**
```
create game named [game] password [] my name [host] role [] server [US-East v] capacity (8) world width (960) height (720)
```

**Implementation Examples:**
- Create game with capacity 2, try to join with third player, observe rejection
- Compare world dimensions 480x360 (small) vs 1920x1080 (large)
- Set world width to 480, move sprite to x=500, observe wrapping/hiding behavior
- Design decisions: "How many players should my game support?"

**CSTA Alignment:** AP-13-01, AP-14-01 (Use procedures with parameters)

**Dependencies:**
- T19.G6.01A (creating games)

**Leads to:** T19.G7.04 (variable player counts)

---

### T19.G6.01D: List available multiplayer games in a table
**Skill:** List available multiplayer games in a table

**Description:** Students use `list multiplayer games in server` to display all active games in a table. They read the Host Name, Game Name, and User Count columns to see which games are available and how many players are in each. They use this information to decide which game to join. They understand that this only shows games on the selected server.

**Block Used:**
```
list multiplayer games in server [US-East v] in table [games v]
```

**Table Columns:** Host Name, Game Name, User Count

**Implementation Examples:**
- List games in US-East server, display table on screen
- Find row where User Count < capacity (game has space)
- Read Host Name and Game Name from selected row
- Use these values to join that game
- Build lobby UI: list games, click to join

**CSTA Alignment:** AP-13-01, DA-07-01 (Store, access, retrieve data)

**Dependencies:**
- T19.G6.01A (creating games)
- T10.G4.01 (reading tables/lists)

**Leads to:** T19.G6.01B (joining selected game)

---

### T19.G6.01E: List players in a game room
**Skill:** List players in a game room

**Description:** Students use `list players in game` to display who is in a specific game. They read the Player Name and Role columns to see all connected players and their assigned roles. They use this to verify who has joined their game or to check if friends are in a game before joining.

**Block Used:**
```
list players in game [game 1] hosted by [host] from server [US-East v] in table [players v]
```

**Table Columns:** Player Name, Role

**Implementation Examples:**
- After creating game, list players to see yourself
- When someone joins, list players again to see them appear
- Display player count: length of players table
- Show player roster on screen during game
- Use roles column to identify player types (explained in T19.G7.00A)

**CSTA Alignment:** AP-13-01, DA-07-01

**Dependencies:**
- T19.G6.01B (joining games)
- T10.G4.01 (reading tables/lists)

**Leads to:** T19.G6.05 (handling join/leave events)

---

### T19.G6.01F: Check connection status and display feedback
**Skill:** Check connection status and display feedback

**Description:** Students use the `connected to game` boolean reporter to check whether they are properly connected. They display appropriate messages (e.g., "Connected!" or "Reconnecting...") based on connection state. They disable game controls when disconnected to prevent errors. They understand that connection can drop due to network issues and the game should handle this gracefully.

**Block Used:**
```
connected to game
```

**Implementation Examples:**
- Forever loop: if `connected to game` show green indicator, else show red
- Say "Reconnecting..." when connection drops
- Disable movement controls when not connected: if `not connected to game` then don't run movement
- Use as precondition: "only run this code if connected"
- Test: Turn off WiFi, observe connection status change

**CSTA Alignment:** AP-13-01, AP-15-01 (Test and debug)

**Dependencies:**
- T19.G6.01A (creating/joining games)
- T08.G3.01 (conditionals)

**Leads to:** T19.G6.05 (synchronized movement with connection check)

---

## SPRITE MANAGEMENT SKILLS (G6.02A-B)

### T19.G6.02A: Test a multiplayer game with two browser windows
**Skill:** Test a multiplayer game with two browser windows

**Description:** Students learn to open two browser windows (or tabs) to test their multiplayer game locally. They create a game in one window (host) and join it in another (client). They verify that changes in one window appear in the other window. They understand that this simulates two players without needing a second person.

**Implementation Examples:**
- Open two windows side-by-side
- Window 1: Create game "test", password "123"
- Window 2: Join game "test" by host (your username), password "123"
- Add sprite in Window 1, verify replicate appears in Window 2
- Move sprite in Window 1, verify replicate moves in Window 2
- Test broadcast: send message from Window 1, receive in Window 2

**CSTA Alignment:** AP-15-01 (Test and debug)

**Dependencies:**
- T19.G6.01B (joining games)

**Leads to:** T19.G7.04A (debugging sync issues)

---

### T19.G6.02B: Register sprites with the game server
**Skill:** Register sprites with the game server

**Description:** Students use the `add this sprite to game as a [Dynamic/Static] [Rectangle/Circle]` block to register a sprite with the game server. They understand that this makes the sprite visible to other players. They choose Dynamic for moving sprites and Static for fixed obstacles. They choose Rectangle or Circle collision shape based on the sprite's appearance. They understand that only registered sprites appear in the multiplayer world.

**Block Used:**
```
add this sprite to game as a [Dynamic v] [Rectangle v]
```

**Implementation Examples:**
- Add player sprite as Dynamic Rectangle
- Add wall sprite as Static Rectangle
- Add ball sprite as Dynamic Circle
- Test: Don't add sprite to game, observe it's invisible to other players
- Add sprite to game, verify replicate appears in other window

**CSTA Alignment:** AP-13-01, AP-16-02

**Dependencies:**
- T19.G6.00C (replication)
- T19.G6.00D (Dynamic/Static)
- T19.G6.00E (collision shapes)
- T19.G6.01B (joining games)

**Leads to:** T19.G5.03 (when added event), T19.G6.05 (synchronized movement)

---

### T19.G6.02C: Configure stop vs pass collision behavior
**Skill:** Configure stop vs pass collision behavior

**Description:** Students learn that collision events can make sprites "stop" (bounce off each other) or "pass" (go through each other). They configure this in the `when touching` collision trigger block. They test both behaviors and choose appropriate ones for different game objects: walls should stop, collectible items should pass.

**Block Used:**
```
when touching [Sprite1 v] will [stop v] and trigger [message1 v] with parameter [hit]
when touching [Coin v] will [pass v] and trigger [collect v] with parameter [10]
```

**Implementation Examples:**
- Player touching Wall: will "stop" (blocks movement)
- Player touching Coin: will "pass" (collect but don't block)
- Player touching Enemy: will "stop" (both bounce)
- Test both behaviors, observe difference in gameplay feel

**CSTA Alignment:** AP-13-01

**Dependencies:**
- T19.G6.02B (adding sprites)
- T14.G5.01 (collision concepts)

**Leads to:** T19.G6.06 (collision events)

---

## BROADCAST MODE SKILLS (G6.04A-B)

### T19.G6.04A: Choose between "All Sprites" and "Exclude Replicate" broadcast modes
**Skill:** Choose between "All Sprites" and "Exclude Replicate" broadcast modes

**Description:** Students learn when to broadcast to "All Sprites" (including replicates) vs "Exclude Replicate" (originals only). They understand that "All Sprites" makes all copies of all sprites run the handler, while "Exclude Replicate" makes only original sprites (one per player) run it. They test both modes and observe the difference. They choose "Exclude Replicate" when each player should do something once (like scoring), and "All Sprites" when every visible sprite should react (like playing animation).

**Block Used:**
```
broadcast [score v] with parameter [10] mode [Exclude Replicate v]
broadcast [explode v] with parameter [] mode [All Sprites v]
```

**Implementation Examples:**
- Test with "All Sprites": Send message, observe both original AND replicate run handler (action happens twice)
- Test with "Exclude Replicate": Send message, observe only original runs handler (action happens once)
- Use case: Score points → "Exclude Replicate" (don't double-score)
- Use case: Play animation → "All Sprites" (all visible sprites should animate)
- Build decision tree: "When should I use each mode?"

**CSTA Alignment:** AP-13-01, AP-14-01

**Dependencies:**
- T19.G6.00C (replication concept)
- T19.G5.04 (basic broadcast)

**Leads to:** T19.G6.04B (broadcast with parameters), T19.G7.03 (choosing what to sync)

---

### T19.G6.04B: Broadcast multiplayer messages with parameters
**Skill:** Broadcast multiplayer messages with parameters

**Description:** Students use the `broadcast [MESSAGE] with parameter [PARAMETER] mode [MODE]` block to send messages to all players with data attached. They understand that this is different from regular broadcast - it sends across the network to all connected clients. They use parameters to send scores, player names, or other data. They receive the parameter in the message handler and use it.

**Block Used:**
```
broadcast [heal v] with parameter [20] mode [All Sprites v]

when I receive [heal v] with parameter [amount]
  change variable [health] by (amount)
```

**Implementation Examples:**
- Broadcast "playerJoined" with parameter = player name
- Broadcast "scoreChanged" with parameter = new score value
- Broadcast "chatMessage" with parameter = message text
- Receive and display: when receive "chatMessage" say (parameter)
- Compare: multiplayer broadcast vs regular Scratch broadcast

**CSTA Alignment:** AP-13-01, AP-14-01, NI-04-01

**Dependencies:**
- T19.G6.04A (broadcast modes)
- T19.G5.03 (message handlers)

**Leads to:** T19.G6.04 (synchronized scoreboard), T19.G6.03 (shared world objects)

---

## ROLES AND SERVERS (G7.00A-B)

### T19.G7.00A: Use roles to identify player types
**Skill:** Use roles to identify player types

**Description:** Students learn that roles let them assign different responsibilities to players (like "seeker" vs "hider" in hide-and-seek, or "red team" vs "blue team"). They assign roles when creating or joining a game. They read a player's role from the player list table and use conditionals to run different code for different roles. They understand that roles are just labels - they don't automatically change behavior, you must code the differences.

**Block Used:**
```
create game ... role [seeker]
join game ... role [hider]

list players in game ... in table [players v]
// Read Role column from table
if (my role) = [seeker] then
  // Seeker behavior
else
  // Hider behavior
end
```

**Implementation Examples:**
- Hide and seek: role "seeker" sees all players, role "hider" starts hidden
- Team game: role "red" scores at red goal, role "blue" scores at blue goal
- Read own role from players table, store in variable
- Use conditional: if role = "attacker" then enable attack button
- Build role selection screen: player chooses role before joining

**CSTA Alignment:** AP-13-01, AP-14-01

**Dependencies:**
- T19.G6.01E (player list)
- T08.G4.01 (conditionals with strings)

**Leads to:** T19.G8.01 (team assignment)

---

### T19.G7.00B: Choose appropriate server locations to minimize lag
**Skill:** Choose appropriate server locations to minimize lag

**Description:** Students learn that server location affects how fast messages travel between players (latency/lag). They understand that players should choose servers close to most players geographically - US-East for East Coast players, US-West for West Coast, etc. They test games with different server locations and observe latency differences. They understand that further distance = more lag.

**Server Options:** US-East, US-West, Europe, Asia

**Implementation Examples:**
- Test: All players in California → use US-West (low lag)
- Test: All players in New York → use US-East (low lag)
- Test: California players on US-East → observe higher lag
- Measure: Time between button press and action appearing (latency)
- Best practice: Ask where players are located before choosing server

**CSTA Alignment:** NI-04-01, IC-20-01

**Dependencies:**
- T19.G6.00F (synchronization concept)
- (Optional context: T31.G5.01 - networking basics)

**Leads to:** T19.G8.04 (debugging latency issues)

---

## DEBUGGING SKILLS (G7.04A-B)

### T19.G7.04A: Debug why sprites aren't synchronizing
**Skill:** Debug why sprites aren't synchronizing

**Description:** Students identify when sprites move on one client but not another. They check if they used synchronized movement blocks (`synchronously set speed`) instead of regular movement (`change x by`). They verify that sprites were added to the game with `add sprite to game`. They use print statements to trace execution on both clients. They fix synchronization issues by using the correct blocks.

**Common Problems:**
1. Used `change x by 10` instead of `synchronously set speed x`
2. Forgot to add sprite to game
3. Not connected to game
4. Movement code only runs on one sprite

**Debugging Process:**
1. Check `connected to game` on both clients
2. Verify sprite was added to game on both clients
3. Add print statement before movement block
4. Check if using synchronized movement blocks
5. Test in two windows

**Implementation Examples:**
- Problem: Player moves in Window 1 but not Window 2
- Debug: Print "moving" before movement block
- Observe: Print appears only in Window 1 → code only running on original
- Solution: Use synchronized movement block
- Verify: Test again, movement appears in both windows

**CSTA Alignment:** AP-15-01 (Test and debug), AP-17-01 (Develop systematic tests)

**Dependencies:**
- T19.G6.02A (testing with two windows)
- T13.G6.01 (print debugging)
- T19.G6.05 (synchronized movement)

**Leads to:** T19.G7.04B (message ordering)

---

### T19.G7.04B: Debug message delivery timing issues
**Skill:** Debug message delivery timing issues

**Description:** Students identify when messages arrive in different orders on different clients, causing state divergence. They understand that network messages have variable delays (some fast, some slow). They add sequence numbers or timestamps to broadcasts to debug ordering. They implement acknowledgement systems to ensure critical messages are received. They understand that multiplayer games must handle out-of-order messages.

**Common Problems:**
1. Messages arrive in different orders on different clients
2. Fast messages overtake slow messages
3. Game state diverges between clients

**Debugging Techniques:**
1. Add sequence numbers: broadcast "move" with parameter = message counter
2. Add timestamps: broadcast "action" with parameter = timer value
3. Print message arrival order on both clients
4. Implement acknowledgement: client confirms receipt

**Implementation Examples:**
- Problem: Player A shoots, Player B moves, but Player B sees move first then shoot
- Debug: Add counter to each broadcast, print counter when received
- Observe: Client 1 receives [1,2,3], Client 2 receives [1,3,2]
- Solution: Add sequence numbers, sort messages before processing
- Advanced: Implement "snapshot interpolation" for smooth playback

**CSTA Alignment:** AP-15-01, AP-17-01, NI-04-01

**Dependencies:**
- T19.G7.04A (debugging sync issues)
- T19.G6.04B (broadcast with parameters)

**Leads to:** T19.G8.04 (advanced debugging)

---

## PRACTICE/APPLICATION SKILLS (G6.03A-B, G7.01A)

### T19.G6.03A: Create a 2-player tag game
**Skill:** Create a 2-player tag game

**Description:** Students create a simple multiplayer tag game where players chase each other. When one player touches another, that player becomes "it" (the chaser). They use synchronized movement so both players see the same positions. They use collision detection to detect touches. They broadcast "you're it!" messages to change roles. They test with two windows.

**Requirements:**
- Two player sprites
- Synchronized movement (arrow keys)
- Collision detection (when touching other player)
- Role switching (who is "it")
- Visual indicator (different color/costume when "it")

**Implementation Examples:**
- Player 1: Use WASD keys for movement
- Player 2: Use arrow keys for movement
- Both: `synchronously set speed x/y` for movement
- When Player1 touching Player2: broadcast "tag" with parameter "Player1"
- When receive "tag": if parameter = my name, then I'm it

**CSTA Alignment:** AP-13-01, AP-16-03 (Systematically test and refine)

**Dependencies:**
- T19.G6.02B (add sprites)
- T19.G6.05 (synchronized movement)
- T19.G6.06 (collision detection)

**Leads to:** T19.G7.01 (cooperative puzzle)

---

### T19.G6.03B: Create a multiplayer drawing canvas
**Skill:** Create a multiplayer drawing canvas

**Description:** Students create an app where multiple players can draw together on a shared canvas. Each player's pen strokes appear on all screens in real-time. They use broadcasts to share drawing data (pen x/y positions). They understand this is a "cooperative" multiplayer app, not a competitive game.

**Requirements:**
- Pen drawing (stamp or pen blocks)
- Synchronized pen position
- Broadcast drawing data
- Different colors per player
- Clear button (broadcasts to all)

**Implementation Examples:**
- When mouse down: start drawing
- Every frame: broadcast "draw" with parameter = "x,y,color"
- When receive "draw": parse parameter, stamp at x,y with color
- Clear button: broadcast "clear", all clients clear canvas
- Optional: Undo button (need to store drawing history)

**CSTA Alignment:** AP-13-01, AP-16-03

**Dependencies:**
- T19.G6.01B (joining games)
- T19.G6.04B (broadcast with parameters)

**Leads to:** T19.G7.01A (cooperative puzzle)

---

### T19.G7.01A: Create a cooperative button puzzle
**Skill:** Create a cooperative button puzzle

**Description:** Students create a puzzle where multiple buttons must be pressed simultaneously to open a door. They use shared variables to track which buttons are pressed. They broadcast button states to all players. They check if all buttons are pressed before opening the door. They understand "cooperation" means players must work together.

**Requirements:**
- Multiple button sprites (Static)
- Door sprite (opens when all pressed)
- Shared state tracking (which buttons pressed)
- Synchronized state updates
- Visual feedback (button color changes)

**Implementation Examples:**
- 4 buttons, each player stands on one
- When touching button: broadcast "buttonPressed" with parameter = button number
- When receive "buttonPressed": set button X to pressed
- Forever check: if all buttons pressed, open door
- Door opens: broadcast "doorOpen", all clients show open door

**CSTA Alignment:** AP-13-01, AP-16-03, IC-20-03 (Collaborate)

**Dependencies:**
- T19.G6.03 (shared world objects)
- T19.G6.04B (broadcast with parameters)

**Leads to:** T19.G7.01 (cooperative puzzle with counters)

---

## BEST PRACTICES SKILLS (G7.06-07 - NEW)

### T19.G7.06: Choose when to use passwords vs public games
**Skill:** Choose when to use passwords vs public games

**Description:** Students learn when to use passwords (private games with friends) vs empty passwords (public games open to anyone). They understand trade-offs: passwords keep games private but require coordination, public games are easier to join but may have unwanted players. They implement both types and discuss use cases.

**Use Cases:**
- **Use Password:** Playing with specific friends, tournament/league games, testing/development
- **No Password:** Public lobbies, casual matchmaking, demo games, community events

**Implementation Examples:**
- Create private game: password = "secret123", share with friends only
- Create public game: password = "", appears in game list for anyone
- Best practice: Use specific passwords (not "123"), share via chat/DM
- Best practice: Public games need moderation/kick features

**CSTA Alignment:** IC-20-03 (Collaborate), IC-19-05 (Explain privacy)

**Dependencies:**
- T19.G6.01A (creating games with passwords)

**Leads to:** T19.G8.06 (security skills)

---

### T19.G7.07: Design games for variable player counts
**Skill:** Design games for variable player counts

**Description:** Students design games that work well with different numbers of players (2, 4, 6, 8). They avoid hard-coding assumptions like "there are always 4 players". They use the player list length to determine actual player count. They adjust game rules, map size, or objectives based on player count. They test with different numbers of players.

**Design Patterns:**
- **Free-for-all:** Works with any player count (tag, racing)
- **Teams:** Require even numbers (2v2, 3v3, 4v4)
- **Cooperative:** Scale difficulty with player count
- **Turn-based:** Use player list to determine turn order

**Implementation Examples:**
- Get player count: length of (player list table)
- Adjust spawn points: loop over player count, place spawn for each
- Adjust difficulty: if player count > 4, spawn more enemies
- Team assignment: divide player count by 2 for team size
- Validate: if player count is odd and game needs teams, show error

**CSTA Alignment:** AP-13-01, AP-14-01, AP-16-03

**Dependencies:**
- T19.G7.04 (scale game logic skill)
- T19.G6.01E (player list)

**Leads to:** T19.G8.01 (team assignment)

---

## SECURITY/PERFORMANCE SKILLS (G8.06-08 - NEW)

### T19.G8.06: Understand multiplayer security basics
**Skill:** Understand what information is shared in multiplayer games

**Description:** Students learn what data is shared with other players: display name, position, messages, but NOT account credentials or personal info. They understand that passwords protect game rooms, not individual players. They learn that all players can see all public game data. They explain why this matters for privacy and design games accordingly.

**What's Shared:**
- ✅ Display name (what you enter in join block)
- ✅ Sprite positions and movements
- ✅ Broadcast messages and parameters
- ✅ Game state (scores, objects)
- ❌ Account username (unless you use it as display name)
- ❌ Password (only used for authentication)
- ❌ Personal information (unless you broadcast it)

**Implementation Examples:**
- Don't use real names as display names if you want privacy
- Don't broadcast personal information (address, phone, etc.)
- Understand that any data you broadcast is visible to all players
- Use generic names: "Player1", "RedTeam", etc.
- Host can see all connected clients

**CSTA Alignment:** IC-19-05 (Explain privacy/security), IC-20-06 (Digital footprint)

**Dependencies:**
- T19.G6.01B (joining games with display names)
- T19.G6.04B (broadcasting)

**Leads to:** None (terminal skill)

---

### T19.G8.07: Optimize network traffic in multiplayer games
**Skill:** Optimize network traffic in multiplayer games

**Description:** Students learn that too many broadcasts or too many Dynamic sprites cause network lag. They identify performance bottlenecks: broadcasting every frame, synchronizing unnecessary data, too many moving objects. They optimize by reducing broadcast frequency, using Static sprites where possible, and only synchronizing essential data.

**Performance Problems:**
1. Broadcasting every frame (60 times/second) → network overload
2. Too many Dynamic sprites → too much position data
3. Synchronizing UI elements (don't need to sync local UI)
4. Large broadcast parameters (sending big strings/lists)

**Optimization Techniques:**
1. Throttle broadcasts: only send every 0.1 seconds, not every frame
2. Use Static sprites for non-moving objects (walls, decorations)
3. Keep UI local (health bars, buttons don't need sync)
4. Send deltas (only changes) not full state
5. Limit max sprites/players

**Implementation Examples:**
- Problem: Game lags with 50 sprites
- Solution: Change decorative sprites from Dynamic to Static → only 10 moving sprites
- Problem: Sending player position every frame
- Solution: Only send when position changes significantly (> 5 pixels)
- Problem: Broadcast entire player list every update
- Solution: Only broadcast when player joins/leaves

**CSTA Alignment:** AP-17-01 (Systematically test), AP-18-01 (Design algorithms with efficiency)

**Dependencies:**
- T19.G6.00D (Dynamic vs Static)
- T19.G6.04B (broadcasting)
- T19.G7.03 (choosing what to sync)

**Leads to:** None (terminal skill)

---

### T19.G8.08: Profile and measure multiplayer performance
**Skill:** Profile and measure multiplayer performance

**Description:** Students use timing and counting techniques to measure multiplayer performance. They measure latency (time from broadcast to receive), frame rate (sprites per second), and network message count. They identify performance bottlenecks using data. They compare performance before and after optimizations.

**Metrics to Measure:**
1. **Latency:** Time from send to receive (broadcast with timestamp)
2. **Frame rate:** Sprites moving smoothly or stuttering?
3. **Message count:** How many broadcasts per second?
4. **Sprite count:** How many Dynamic sprites?

**Measurement Techniques:**
1. Latency: Broadcast message with timer value, receive and subtract = latency
2. Message count: Increment counter on each broadcast, display per second
3. Frame rate: Use "turbo mode" indicator or measure render time
4. Profile: Run game, record metrics, optimize, re-measure

**Implementation Examples:**
- Measure latency: `broadcast [ping] with parameter (timer)`
  - On receive: `set latency to (timer - parameter)`
- Count broadcasts: variable `msgCount`, increment on send, reset every second
- Before optimization: 120 messages/second, 200ms latency
- After optimization: 30 messages/second, 50ms latency
- Document: "Reduced broadcasts by 75%, latency improved 4x"

**CSTA Alignment:** AP-17-01, AP-18-01, DA-08-01 (Collect and analyze data)

**Dependencies:**
- T19.G8.07 (optimization techniques)
- T09.G6.01 (variables and formulas)

**Leads to:** None (terminal skill)

---

## SUMMARY OF NEW SKILLS

### Grade 6: 12 new skills
- T19.G6.00A-F: Foundation concepts (6)
- T19.G6.01A-F: Hosting/joining/listing (6)

### Grade 6 continued: 6 new skills
- T19.G6.02A: Testing with two windows
- T19.G6.02B: Add sprites (revised)
- T19.G6.02C: Stop vs pass collisions
- T19.G6.03A-B: Practice games (tag, drawing)
- T19.G6.04A: Broadcast modes

### Grade 7: 6 new skills
- T19.G7.00A-B: Roles and servers
- T19.G7.01A: Cooperative puzzle
- T19.G7.04A-B: Debugging skills
- T19.G7.06-07: Best practices

### Grade 8: 3 new skills
- T19.G8.06: Security awareness
- T19.G8.07: Performance optimization
- T19.G8.08: Performance profiling

### TOTAL: 27 new skills + ~8 revised skills = 35 total changes

This brings T19 from 25 skills to approximately 42-45 skills, with complete coverage of all blocks and proper scaffolding.
