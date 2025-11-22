# T31 Phase 1 Optimization - Quick Reference

## At a Glance
- **Current Skills:** 37 (K-8)
- **High Priority Issues:** 18
- **Medium Priority Issues:** 12
- **Low Priority Issues:** 7
- **Proposed Final Count:** ~25 skills

## Critical Finding
**Major topic confusion between T31 and T33:**
- 15+ skills currently in T31 should be in T33 (Connected Services)
- 8+ skills currently in T31 should be in T19 (Multiplayer)
- Several skills might belong in T32 (Cybersecurity)

## High Priority Actions

### 1. Move to T33 (Connected Services) - 7 skills
- T31.G5.03 → Web fetch block usage
- T31.G6.02 → Read Google Sheets cell
- T31.G6.03 → Write Google Sheets cell
- T31.G6.03.01 → Update Google Sheets rows
- T31.G6.03.02 → Manage multiple sheets
- T31.G7.02.03 → Database insert
- T31.G7.02.04 → Database fetch
- T31.G7.02.05 → Database update/remove

### 2. Move to T19 (Multiplayer) - 8 skills
- T31.G5.04 → Create/join multiplayer game
- T31.G5.05 → Check connection status
- T31.G6.06 → Add sprites to game
- T31.G7.01 → Model multiplayer server
- T31.G7.02 → Sync sprite movement
- T31.G7.02.01 → Broadcast messages
- T31.G7.02.02 → Handle collisions

### 3. Fix ID Numbering Violations - 7 skills
Invalid format (using 3-level numbering):
- T31.G6.03.01 → Renumber
- T31.G6.03.02 → Renumber
- T31.G7.02.01 → Renumber
- T31.G7.02.02 → Renumber
- T31.G7.02.03 → Renumber
- T31.G7.02.04 → Renumber
- T31.G7.02.05 → Renumber

### 4. Add Missing Skills - 4 new skills
- **G5.03** (new): Read URL parameters
- **G5.06** (new): Store/retrieve user data
- **G6.07** (new): Game leaderboards
- **G7.06** (new): Handle network errors

### 5. Clarify Vague Skills - 4 skills
- T31.G6.04: Add specific timer block usage
- T31.G8.01: Mark as design/diagramming
- T31.G8.02: Add measurable metrics
- T31.G8.05: Add error handling patterns

### 6. Review for T32 Move - 5 skills
- T31.G2.02: Safe online behavior
- T31.G4.02: Secure websites
- T31.G6.05: Privacy of AI data
- T31.G8.03: Secure cloud systems
- T31.G8.04: Privacy protection

## What T31 SHOULD Focus On
✅ Networking concepts (how internet works)
✅ Protocols (HTTP/HTTPS)
✅ Network architecture (client-server, P2P, topologies)
✅ Latency, bandwidth, connectivity
✅ General cloud computing concepts
✅ Societal impacts

❌ NOT specific service implementations (Google Sheets, Database)
❌ NOT multiplayer game mechanics
❌ NOT detailed security/privacy (that's T32)

## What T33 SHOULD Focus On
✅ Google Sheets blocks
✅ Database blocks
✅ Web fetch blocks
✅ Google Drive blocks
✅ Service error handling
✅ API rate limiting
✅ Persistent game data (leaderboards, user data)

## CreatiCode Blocks Found

### Cloud Category (15 blocks)
- fetch web page as markdown
- 13 Google Sheets operations (read, write, cell ops, sheet management, insert/remove rows/cols)
- 1 Google Drive operation (list folder)

### Multiplayer Category (13 blocks)
- create/join game, list games/players
- add/remove sprite from game
- sync movement (2 variants)
- broadcast messages
- collision detection
- connection status check
- reset world

### Database Category (12 blocks)
- insert, fetch, update, remove
- query conditions (6 operator blocks)
- field and collection reporters

### Game Category - Persistent Data (5 blocks)
- record score
- show/hide/clear leaderboard
- store/read user data

### Other Network Blocks
- read URL parameter (Sensing)
- add costume from URL (Looks)

## Skills That Are Good (Keep As-Is)

### K-4: All conceptual skills are appropriate
- T31.GK.01: Recognize internet devices ✅
- T31.G1.01: Connected vs disconnected ✅
- T31.G2.01: Internet connects computers ✅
- T31.G3.01: Trace device to website path ✅
- T31.G3.02: Types of online sharing ✅
- T31.G4.01: How data travels (packets) ✅

### Grade 5-8: Core networking concepts
- T31.G5.01: Trace device to service ✅
- T31.G5.02: Internet vs offline apps ✅
- T31.G6.01: HTTP/HTTPS request steps ✅
- T31.G7.03: Network topologies ✅
- T31.G7.04: Client-server vs P2P ✅
- T31.G7.05: Societal impacts ✅

## Blocks NOT Covered Anywhere
❌ read URL parameter (Sensing) - SHOULD ADD to T31.G5.03
❌ store/read user data (Game) - SHOULD ADD to T31.G5.06
❌ record score, leaderboard blocks (Game) - SHOULD ADD to T31.G6.07
❌ Google Drive blocks - Currently in T33.G7.04
❌ All Cloud category blocks - Wrongly scattered in T31, should be in T33

## Next Steps
1. ✅ Get approval on T31/T33 scope separation
2. ✅ Confirm T19 topic exists for multiplayer
3. Execute moves:
   - 15 skills to T33
   - 8 skills to T19
4. Add 4 missing skills to T31
5. Fix 7 ID numbering violations
6. Clarify 4 vague G8 skills
7. Update ~20 cross-topic dependencies
