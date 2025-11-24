# T31 Internet & Cloud - Visual Breakdown

## Topic Distribution

```
T31 Internet & Cloud (67 skills)
│
├─ K-4: Foundation (10 skills)
│  ├─ Kindergarten (1): Internet device recognition
│  ├─ Grade 1 (1): Connection status
│  ├─ Grade 2 (2): Networks, safety
│  ├─ Grade 3 (2): Data paths, sharing types
│  └─ Grade 4 (2): Packets, security
│
├─ Grade 5: Introduction (8 skills)
│  ├─ Concepts (2): Device-to-service, online/offline
│  ├─ Web (1): Fetch web page
│  └─ Multiplayer Basics (5): Create, join, list, status
│
├─ Grade 6: Cloud Services (18 skills)
│  ├─ HTTP/HTTPS (1): Request tracing
│  ├─ Google Sheets (10): Read, write, manage
│  ├─ AI Impact (2): Latency, privacy
│  └─ Multiplayer Sprites (4): Add, remove, list, reset
│
├─ Grade 7: Advanced Systems (20 skills)
│  ├─ Multiplayer Advanced (7): Movement, broadcast, collisions, server
│  ├─ Database (9): Insert, query, update, remove
│  └─ Architecture (4): Topology, client-server, impacts
│
└─ Grade 8: AI Integration (7 skills)
   ├─ AI Cloud (4): Edge/cloud, requirements, security, privacy
   ├─ Drive (1): Folder access
   └─ Resilience (2): Fallbacks, monitoring
```

---

## Feature Coverage Map

### DATABASE BLOCKS (13) ✓ Complete

```
Database Operations
│
├─ Basic Operations (3 blocks → 3 skills)
│  ├─ T31.G7.03: Insert from table
│  ├─ T31.G7.03.07: Update collection
│  └─ T31.G7.03.08: Remove from collection
│
├─ Query Operators (7 blocks → 6 skills)
│  ├─ T31.G7.03.01: Equals
│  ├─ T31.G7.03.02: Greater than / Less than
│  ├─ T31.G7.03.03: Contains
│  ├─ T31.G7.03.04: AND logic
│  ├─ T31.G7.03.05: OR logic
│  └─ T31.G7.03.06: NOT logic
│
└─ Extended Operators (3 blocks - covered above)
   ├─ Not equals (in .01)
   ├─ Greater than or equal (in .02)
   └─ Less than or equal (in .02)
```

### MULTIPLAYER BLOCKS (13) ✓ Complete

```
Multiplayer System
│
├─ Session Management (4 blocks → 4 skills)
│  ├─ T31.G5.04: Create game
│  ├─ T31.G5.04.01: Join game
│  ├─ T31.G5.04.02: List games
│  └─ T31.G5.05: Connection status
│
├─ Sprite Management (4 blocks → 4 skills)
│  ├─ T31.G6.06: Add sprite
│  ├─ T31.G6.06.01: Remove sprite
│  ├─ T31.G6.06.02: List players
│  └─ T31.G6.06.03: Reset game
│
├─ Movement Sync (3 blocks → 3 skills)
│  ├─ T31.G7.02: Set speed x/y
│  ├─ T31.G7.02.01: Set speed/direction
│  └─ T31.G7.02.02: Broadcast message
│
└─ Collision Handling (2 blocks → 3 skills)
   ├─ T31.G7.02.03: Stop mode
   ├─ T31.G7.02.04: Delete mode
   └─ T31.G7.02.05: Continue mode
```

### CLOUD/SHEETS BLOCKS (15) ✓ Complete

```
Cloud Operations
│
├─ Web Fetching (1 block → 1 skill)
│  └─ T31.G5.03: Fetch web page
│
├─ Read Operations (2 blocks → 2 skills)
│  ├─ T31.G6.02: Read range
│  └─ T31.G6.02.01: Get cell value
│
├─ Write Operations (3 blocks → 3 skills)
│  ├─ T31.G6.03: Write range
│  ├─ T31.G6.03.01: Set cell value
│  └─ T31.G6.03.02: Append rows
│
├─ Structure Operations (5 blocks → 4 skills)
│  ├─ T31.G6.03.03: Insert rows/columns
│  ├─ T31.G6.03.04: Remove rows/columns
│  ├─ T31.G6.03.05: Clear sheet
│  └─ T31.G6.03.06: List sheets
│
├─ Sheet Management (2 blocks → 1 skill)
│  └─ T31.G6.03.07: Add/remove sheets
│
└─ Drive Operations (2 blocks → 1 skill)
   └─ T31.G8.04.01: List Drive folders
```

---

## Dependency Flow Diagram

### Grade 5 Foundation
```
T31.G5.01 (Trace device to service)
    │
    ├──→ T31.G5.02 (Online/offline)
    │        └──→ T31.G6.04 (AI latency)
    │        └──→ T31.G6.05 (AI privacy)
    │
    ├──→ T31.G5.03 (Fetch web)
    │        └──→ T31.G6.02 (Read Sheets)
    │
    └──→ T31.G5.04 (Create game)
             └──→ T31.G5.04.01 (Join game)
                      └──→ T31.G5.05 (Status)
                           └──→ T31.G6.06 (Add sprite)
```

### Grade 6 Expansion
```
T31.G6.02 (Read range)
    ├──→ T31.G6.02.01 (Get cell)
    └──→ T31.G6.03 (Write range)
             ├──→ T31.G6.03.01 (Set cell)
             ├──→ T31.G6.03.02 (Append)
             │        └──→ T31.G6.03.03 (Insert)
             │                 └──→ T31.G6.03.04 (Remove)
             ├──→ T31.G6.03.05 (Clear)
             ├──→ T31.G6.03.06 (List sheets)
             │        └──→ T31.G6.03.07 (Add/remove sheets)
             └──→ (feeds to G8.04.01 via G8.04)

T31.G6.06 (Add sprite)
    ├──→ T31.G6.06.01 (Remove sprite)
    ├──→ T31.G6.06.02 (List players)
    ├──→ T31.G6.06.03 (Reset game)
    └──→ T31.G7.01 (Model server)
    └──→ T31.G7.02 (Movement sync)
             ├──→ T31.G7.02.01 (Polar)
             ├──→ T31.G7.02.02 (Broadcast)
             └──→ T31.G7.02.03 (Collision stop)
                      ├──→ T31.G7.02.04 (Delete)
                      └──→ T31.G7.02.05 (Continue)
```

### Grade 7 Database
```
T31.G7.03 (Insert data)
    └──→ T31.G7.03.01 (Equals)
             ├──→ T31.G7.03.02 (Comparisons)
             │        └──→ T31.G7.03.04 (AND)
             │                 ├──→ T31.G7.03.05 (OR)
             │                 └──→ T31.G7.03.06 (NOT)
             ├──→ T31.G7.03.03 (Contains)
             │        └──→ T31.G7.03.04 (AND)
             ├──→ T31.G7.03.07 (Update)
             └──→ T31.G7.03.08 (Remove)
```

### Grade 7 Architecture
```
T31.G6.01 (HTTP/HTTPS)
    └──→ T31.G7.04 (Topology)
             └──→ T31.G7.05 (Client-server)
                      └──→ T31.G7.06 (Societal impacts)
                               └──→ T31.G8.01 (Edge/cloud)
                                        ├──→ T31.G8.02 (Requirements)
                                        │        └──→ T31.G8.05 (Resilience)
                                        └──→ T31.G8.03 (Security)
                                                 └──→ T31.G8.04 (Privacy)
```

---

## Before vs After Comparison

### Skill Structure Changes

#### BEFORE: Broad Skills (Example)
```
T31.G6.02-03: Google Sheets Read/Write (2 skills)
    ↓
Covered ~15 blocks with vague descriptions
Students unclear which block to use when
```

#### AFTER: Specific Skills (Example)
```
T31.G6.02: Read range (1 block)
T31.G6.02.01: Get cell (1 block)
T31.G6.03: Write range (1 block)
T31.G6.03.01: Set cell (1 block)
T31.G6.03.02: Append rows (1 block)
T31.G6.03.03: Insert rows/columns (2 blocks)
T31.G6.03.04: Remove rows/columns (2 blocks)
T31.G6.03.05: Clear sheet (1 block)
T31.G6.03.06: List sheets (1 block)
T31.G6.03.07: Add/remove sheets (2 blocks)
    ↓
10 focused skills, each teaching specific operation
Clear when to use each block
```

---

## Complexity Progression

### Kindergarten → Grade 4: Conceptual
```
Visual/Unplugged → Understanding → Recognition
No coding, picture-based activities
Building mental models of internet
```

### Grade 5: First Implementation
```
Conceptual → Practical
First hands-on coding with blocks
Simple operations (fetch, create, join)
```

### Grade 6: Feature Expansion
```
Single Operations → Multiple Features
Google Sheets: 10 operations
Multiplayer: Sprite management
AI: Understanding impacts
```

### Grade 7: System Understanding
```
Features → Systems
Database: Complete CRUD + queries
Multiplayer: Full synchronization
Architecture: Topology, client-server
```

### Grade 8: Integration & Ethics
```
Systems → Integration + Ethics
AI cloud architecture
Security and privacy
Monitoring and resilience
```

---

## Assessment Clarity

### BEFORE
```
Skill: "Use Google Sheets"
Question: "Can student use Google Sheets?"
Problem: Which operations? Read? Write? Manage?
```

### AFTER
```
Skill: "Append rows to Google Sheets"
Question: "Can student use 'append rows' block to add data?"
Assessment: Show student a leaderboard scenario
Expected: Student selects 'append rows' (not write range)
```

---

## Learning Path Examples

### Path 1: Building a Multiplayer Game
```
1. T31.G5.04: Create game session
2. T31.G5.04.01: Join from second device
3. T31.G5.05: Check connection status
4. T31.G6.06: Add player sprites
5. T31.G7.02: Synchronize movement
6. T31.G7.02.02: Broadcast game events
7. T31.G7.02.03: Handle collisions
```

### Path 2: Building a Cloud Leaderboard
```
1. T31.G5.03: Understand web fetching
2. T31.G6.02: Read existing scores
3. T31.G6.03: Write new scores
4. T31.G6.03.02: Append new entries
5. T31.G6.03.03: Insert rows for structure
6. T31.G6.03.06: List multiple sheets
7. T31.G6.03.07: Manage game levels as sheets
```

### Path 3: Building a Database App
```
1. T31.G7.03: Insert player profiles
2. T31.G7.03.01: Fetch by username
3. T31.G7.03.02: Find high scores
4. T31.G7.03.04: Complex queries (AND)
5. T31.G7.03.07: Update player stats
6. T31.G7.03.08: Remove inactive players
```

---

## Grade-Level Intensity

```
Skills per Grade:
K    ■ (1)
1    ■ (1)
2    ■■ (2)
3    ■■ (2)
4    ■■ (2)
5    ■■■■■■■■ (8)
6    ■■■■■■■■■■■■■■■■■■ (18)
7    ■■■■■■■■■■■■■■■■■■■■ (20)
8    ■■■■■■■ (7)

K-4: Foundation building (picture-based, conceptual)
5-6: Feature learning (hands-on, practical)
7-8: System mastery (advanced, integrated)
```

---

## Block-to-Skill Ratio

```
Database:     13 blocks → 9 skills  (1.4:1) ✓
Multiplayer:  13 blocks → 13 skills (1:1)   ✓
Sheets/Cloud: 15 blocks → 11 skills (1.4:1) ✓

Overall:      41 blocks → 67 skills (1:1.6)

Plus 33 conceptual/integration skills
Total: 67 skills covering all features
```

---

## Success Metrics

### Coverage
- ✓ 100% of database blocks covered
- ✓ 100% of multiplayer blocks covered
- ✓ 100% of cloud/sheets blocks covered

### Quality
- ✓ Each skill focuses on ONE specific block/feature
- ✓ Clear descriptions with examples
- ✓ Grade-appropriate complexity
- ✓ Proper scaffolding and dependencies

### Usability
- ✓ Teachers know exactly what to teach
- ✓ Students know exactly what to learn
- ✓ Assessments can measure specific skills
- ✓ Projects naturally combine multiple skills

---

*Visual breakdown generated: 2024-11-24*
