# T19 Quick Reference - Optimized Skills

## Skill Count by Grade

- **Grade 5:** 5 skills (Conceptual foundation)
- **Grade 6:** 69 skills (Core implementation - was 60, +9 new)
- **Grade 7:** 9 skills (Advanced techniques)
- **Grade 8:** 12 skills (Expert/Architecture)
- **Total:** 95 skills

---

## Key Changes at a Glance

### NEW SKILLS (9 total):

**Create Game Parameters (3):**
- T19.G6.01A.01 - Set display name when creating
- T19.G6.01A.02 - Choose role when creating
- T19.G6.01A.03 - Select server location when creating

**Join Game Parameters (2):**
- T19.G6.01B.01 - Set display name when joining
- T19.G6.01B.02 - Choose role when joining

**Sprite Registration (4):**
- T19.G6.02B.01 - Add Dynamic sprite
- T19.G6.02B.02 - Add Static sprite
- T19.G6.02B.03 - Choose Rectangle collision shape
- T19.G6.02B.04 - Choose Circle collision shape

### REVISED SKILLS (3):

1. **T19.G6.01A** - Now only game name + password (narrowed from 8 parameters)
2. **T19.G6.01B** - Now only game name + server + password (narrowed from 6 parameters)
3. **T19.G6.02B** - DEPRECATED, use .01-.04 instead

### FIXED:
- Removed phantom T18.G5.01 dependency from 20+ skills
- Cleaned up excessive T02/T03/T04/T05 cross-topic dependencies
- Fixed circular dependencies in deprecated project skills

---

## Learning Sequence: Create and Join Games

### Path 1: Creating Games (Host)

1. **T19.G6.01A** - Basic create (name + password)
2. **T19.G6.01A.01** - Add display name
3. **T19.G6.01A.02** - Add role selection
4. **T19.G6.01A.03** - Add server selection
5. **T19.G6.01C** - Add capacity setting
6. **T19.G6.01C2** - Add world dimensions

### Path 2: Joining Games (Client)

1. **T19.G6.01B** - Basic join (name + server + password)
2. **T19.G6.01B.01** - Add display name
3. **T19.G6.01B.02** - Add role selection

### Path 3: Game Discovery

- **T19.G6.01D** - List available games
- **T19.G6.01E** - List players in game
- **T19.G6.01C3** - Handle capacity limits

---

## Learning Sequence: Sprite Registration

### Sequential Path:

1. **T19.G6.02A** - Understand registration purpose (conceptual)
2. **T19.G6.02B.01** - Add Dynamic sprite (moving objects)
3. **T19.G6.02B.02** - Add Static sprite (fixed objects)
4. **T19.G6.02B.03** - Choose Rectangle shape (box sprites)
5. **T19.G6.02B.04** - Choose Circle shape (round sprites)
6. **T19.G6.02C** - Initialize with "when added to game"

---

## Block-to-Skills Mapping

### mp_createmultiplayergame (Create Game)
**6 skills cover all parameters:**
1. T19.G6.01A - game name, password
2. T19.G6.01A.01 - display name (host)
3. T19.G6.01A.02 - role
4. T19.G6.01A.03 - server location
5. T19.G6.01C - capacity
6. T19.G6.01C2 - width, height

### mp_joinmultiplayergame (Join Game)
**3 skills cover all parameters:**
1. T19.G6.01B - game name, host name, server, password
2. T19.G6.01B.01 - display name
3. T19.G6.01B.02 - role

### mp_addspritetogame (Add Sprite)
**4 skills cover both parameters:**
1. T19.G6.02B.01 - Dynamic mode
2. T19.G6.02B.02 - Static mode
3. T19.G6.02B.03 - Rectangle shape
4. T19.G6.02B.04 - Circle shape

### mp_listmultiplayergames (List Games)
**1 skill:**
- T19.G6.01D

### mp_listmultiplayergameusers (List Players)
**1 skill:**
- T19.G6.01E

### mp_whenaddedtogame (When Added Event)
**1 skill:**
- T19.G6.02C

### mp_removespritefromgame (Remove Sprite)
**1 skill:**
- T19.G6.11

### mp_setsyncmovement (Sync Speed X/Y)
**1 skill:**
- T19.G6.05A

### mp_setsyncmovement2 (Sync Speed/Direction)
**1 skill:**
- T19.G6.05B

### mp_broadcastmessagetoall (Broadcast Message)
**4 skills cover all aspects:**
1. T19.G6.04A - Choose broadcast mode
2. T19.G6.04B - Receive messages
3. T19.G6.04C - Send with parameters
4. T19.G6.04D - Access parameters

### mp_broadcasttouchmessage (Collision Message)
**3 skills cover 4 modes:**
1. T19.G6.06 - Stop vs continue
2. T19.G6.06B - Delete modes
3. T19.G6.07 - Handle collision messages

### mp_resetmultiplayergame (Reset Game)
**1 skill:**
- T19.G6.12

### mp_isconnectedtogame (Connection Status)
**1 skill:**
- T19.G6.01F

---

## Project Skills Structure

### Racing Game (T19.G6.03A.01-.04)
1. Set up structure (room + track + sprites)
2. Implement controls (synchronized movement)
3. Add collision detection (finish line)
4. Determine winner (broadcast + display)

### Cooperative Game (T19.G6.03B.01-.04)
1. Design objectives (cooperative mechanics)
2. Track progress (shared variables)
3. Broadcast events (coordination)
4. Implement win condition (all objectives complete)

### Tag Game (T19.G6.03C.01-.04)
1. Design roles and rules (tagger vs runner)
2. Implement behaviors (role-based conditionals)
3. Use collision messages (tagging detection)
4. Swap roles (role change after tag)

---

## Common Dependency Patterns

### Conceptual Foundation (All G6 Skills Need):
- T05.G5.01 (user needs and requirements)
- T10.G5.01 (table structure)
- T08.G5.01 (multi-branch decision logic)

### Room Management Skills Need:
- T19.G6.00B (host-client model)
- T19.G6.00H (servers)
- T19.G6.00J (display names)

### Sprite Skills Need:
- T19.G6.00C (sprite replication)
- T19.G6.00D (Dynamic vs Static)
- T19.G6.00E (collision shapes)

### Movement Skills Need:
- T19.G6.00F (synchronization mechanisms)
- T19.G6.02B.01 (Dynamic sprite registration)

### Messaging Skills Need:
- T19.G6.00C2 (code on originals vs replicates)
- T06.G4.01 (basic broadcasts)

---

## Grade 7 Focus Areas

**Roles & Strategy:**
- T19.G7.00A - Role-based behaviors
- T19.G7.00B - Server location selection
- T19.G7.00C - Network delay understanding

**Implementation:**
- T19.G7.01 - Cooperative puzzles
- T19.G7.02 - Ready-up systems
- T19.G7.03 - Data synchronization choices
- T19.G7.04 - Variable player counts

**Quality:**
- T19.G7.05 - Balance and fairness
- T19.G7.06 - Passwords vs public games
- T19.G7.07 - Debug synchronization
- T19.G7.08 - Test with 3+ players
- T19.G7.09 - Fair starting conditions

---

## Grade 8 Focus Areas

**Advanced Systems:**
- T19.G8.01 - Team assignment/matchmaking
- T19.G8.02 - Host-authoritative validation
- T19.G8.03 - Reconnection handling
- T19.G8.04 - Message timing debugging

**Architecture:**
- T19.G8.05.01 - Diagram message flow
- T19.G8.05.02 - Identify sync points
- T19.G8.05.03 - Trace game actions
- T19.G8.05.04 - Identify bottlenecks

**Optimization:**
- T19.G8.06 - Data privacy understanding
- T19.G8.07 - Optimize network traffic
- T19.G8.08 - Profile performance
- T19.G8.09 - Error handling
- T19.G8.10 - Compare architectures

---

## Testing Progression

### Two-Window Testing (G6):
- T19.G6.01G - Test with 2 windows
- Required for all basic multiplayer testing

### Multi-Player Testing (G7):
- T19.G7.08 - Test with 3+ players
- Required for scaling and balance

### Systematic Testing (G8):
- T19.G8.08 - Performance profiling
- T19.G8.09 - Error case testing

---

## Prerequisite Knowledge (Before Starting T19)

### From Other Topics:
- **T06.G4.01** - Basic broadcasts (for multiplayer messages)
- **T08.G4.01** - Conditionals (for game logic)
- **T09.G3.01.01** - Variables (for game state)
- **T10.G3.01.01** - Lists (for player data)
- **T14.G5.01** - Collision detection (for multiplayer collisions)

### Within T19:
- **Complete G5** before starting G6
- **Master G6.00X** (conceptual) before G6.01X (implementation)
- **Learn room management** (G6.01X) before sprites (G6.02X)
- **Learn sprites** (G6.02X) before messaging (G6.04X)
- **Complete basic G6** before attempting projects (G6.03X)

---

## Assessment Checkpoints

### Checkpoint 1: Basic Multiplayer (After G6.01X)
- Can create and join games
- Can use game lists
- Can verify connection status

### Checkpoint 2: Sprite Synchronization (After G6.02X)
- Can register Dynamic and Static sprites
- Understands collision shapes
- Can initialize sprites

### Checkpoint 3: Communication (After G6.04X + G6.05X)
- Can broadcast messages
- Can synchronize movement
- Can pass parameters

### Checkpoint 4: Complete Game (After G6.03X or G6.06-12)
- Has built at least one complete multiplayer game
- Uses collisions and game management
- Demonstrates understanding of all core concepts

### Checkpoint 5: Advanced Techniques (After G7)
- Implements roles
- Handles variable player counts
- Tests and debugs systematically

### Checkpoint 6: Expert Systems (After G8)
- Understands architecture
- Optimizes performance
- Handles edge cases

---

## Common Pitfalls & Solutions

### Pitfall 1: Trying to teach G6.01A all at once
**Solution:** Use new 6-skill sequence (A → A.01 → A.02 → A.03 → C → C2)

### Pitfall 2: Not testing with two windows
**Solution:** Require T19.G6.01G early and use throughout

### Pitfall 3: Using regular movement instead of synchronized
**Solution:** Emphasize T19.G6.05A/B and debug with T19.G7.07

### Pitfall 4: Not understanding originals vs replicates
**Solution:** Spend time on T19.G6.00C2 before attempting control logic

### Pitfall 5: Over-synchronizing or under-synchronizing
**Solution:** Teach T19.G7.03 to develop judgment about sync decisions

---

## Implementation Timeline (Suggested)

### Week 1-2: Foundation
- G5.01-05 (conceptual understanding)
- G6.00A-K (deeper concepts)

### Week 3-4: Room Management
- G6.01A through G6.01G (create, join, list, test)

### Week 5-6: Sprites & Movement
- G6.02A-C (sprite registration)
- G6.05A-B (synchronized movement)

### Week 7-8: Communication & Collisions
- G6.04A-D (messaging)
- G6.06-07 (collisions)

### Week 9-10: Complete Projects
- G6.03A.01-04 (racing game)
- OR G6.03B.01-04 (cooperative)
- OR G6.03C.01-04 (tag)

### Week 11-12: Game Management & Polish
- G6.08-12 (world objects, scoreboard, player management)

### Week 13-14: Advanced Techniques (G7)
- Roles, scaling, testing, debugging

### Week 15-16: Expert Topics (G8)
- Architecture, optimization, error handling

---

## Resources Needed

### Development Tools:
- Two browser windows (minimum)
- Multiple devices for real network testing (optional but recommended)

### Testing Partners:
- At least one other person for two-player testing
- 2+ people for multi-player testing (G7.08)

### Reference Materials:
- CreatiCode multiplayer blocks documentation
- This skill map
- T19_optimized_complete.md (full skill descriptions)

---

## Success Metrics

### Students Should Be Able To:
- ✓ Create and join multiplayer games independently
- ✓ Register sprites with appropriate Dynamic/Static and shape settings
- ✓ Implement synchronized movement
- ✓ Send and receive broadcast messages with parameters
- ✓ Handle collisions with appropriate behaviors
- ✓ Build complete multiplayer games from scratch
- ✓ Test systematically with multiple windows/players
- ✓ Debug synchronization issues
- ✓ Optimize network performance
- ✓ Explain multiplayer architecture

### Observable Behaviors:
- Uses two-window testing without prompting
- Chooses appropriate Dynamic/Static and collision shapes
- Structures code to separate original vs replicate logic
- Makes informed sync decisions (what to sync, when, how)
- Debugs methodically using print statements across clients
- Considers fairness and balance in game design
- Optimizes based on measurement, not guessing

---

## Quick FAQ

**Q: Why split G6.01A into 6 skills?**
A: Teaching 8 parameters at once was overwhelming and not assessable. Now each parameter is a focused learning objective.

**Q: What happened to T19.G6.02B?**
A: Split into 4 skills (Dynamic, Static, Rectangle, Circle) for better scaffolding.

**Q: Why remove T18.G5.01 dependency?**
A: It doesn't exist (only T18.G5.01.01-.05 exist) and 3D physics isn't relevant to networking.

**Q: Can students skip conceptual skills (G6.00X)?**
A: Not recommended. Conceptual understanding prevents common mistakes and enables better design.

**Q: What's the minimum to build a working multiplayer game?**
A: G6.01A, G6.01B, G6.02B.01, G6.05A, G6.01G (create, join, register sprite, move, test).

**Q: When should students learn about roles?**
A: Concept at G6.00I, parameters at G6.01A.02/B.02, implementation at G7.00A.

**Q: How long does T19 take to complete?**
A: Full mastery: 12-16 weeks. Basic competency: 4-6 weeks. First multiplayer game: 2-3 weeks.

---

## Version Information

- **Document Version:** 1.0
- **Optimization Date:** 2025-11-25
- **Total Skills:** 95 (5 G5, 69 G6, 9 G7, 12 G8)
- **Skills Added:** 9
- **Skills Revised:** 3 major, ~30 minor
- **Dependencies Fixed:** 20+ phantom dependencies removed
