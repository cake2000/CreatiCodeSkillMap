# T19 Multiplayer Apps - Block to Skill Mapping

This document maps every CreatiCode multiplayer block to existing and proposed skills.

---

## Block Coverage Matrix

| # | Block | Parameters | Current Coverage | Gaps | Proposed Skills |
|---|-------|-----------|------------------|------|----------------|
| 1 | `create game` | name, password, host name, role, server, capacity, world w/h | ⚠️ Partial: T19.G5.01 | Missing: capacity, world dimensions, roles, servers | T19.G6.01A (basic), T19.G6.01C (capacity/dimensions), T19.G7.00A (roles), T19.G7.00B (servers) |
| 2 | `join game` | name, host, server, password, display name, role | ⚠️ Partial: T19.G5.01 | Missing: roles, display names | T19.G6.01B (basic), T19.G7.00A (roles) |
| 3 | `list games` | server, table | ⚠️ Conflated: T19.G5.06 | Needs separate skill | T19.G6.01D (separate) |
| 4 | `list players` | game, host, server, table | ⚠️ Conflated: T19.G5.06 | Needs separate skill | T19.G6.01E (separate) |
| 5 | `reset game world` | none | ✅ Full: T19.G6.07 | None | Keep as-is |
| 6 | `connected to game` | none (reporter) | ✅ Full: T19.G5.05 | None | Move to T19.G6.01F |
| 7 | `add sprite to game` | mode (Dynamic/Static), shape (Rectangle/Circle) | ⚠️ Partial: T19.G5.02 | Missing: mode/shape explanation | T19.G6.02B (revised), T19.G6.00D (Dynamic/Static), T19.G6.00E (shapes) |
| 8 | `remove sprite` | none | ✅ Full: T19.G6.06 | None | Keep as-is |
| 9 | `when added to game` | none (hat block) | ✅ Full: T19.G5.03 | None | Keep but improve description |
| 10 | `sync speed x/y` | x, y | ⚠️ No concepts: T19.G6.01 | Missing: what "sync" means | T19.G6.05 (revised), T19.G6.00F (sync concept) |
| 11 | `sync speed/dir` | speed, direction | ⚠️ No concepts: T19.G6.01 | Missing: what "sync" means | T19.G6.05 (revised), T19.G6.00F (sync concept) |
| 12 | `broadcast with param` | message, parameter, mode (All/Exclude) | ⚠️ Partial: T19.G5.04 | Missing: mode explanation | T19.G6.04B (revised), T19.G6.04A (modes) |
| 13 | `when touching (collision)` | sprite, stop/pass, message, parameter | ⚠️ Partial: T19.G6.02 | Missing: stop/pass behavior | T19.G6.06 (revised), T19.G6.02C (stop/pass) |

**Summary:**
- ✅ **3 blocks fully covered** (23%)
- ⚠️ **10 blocks partially covered** (77%)
- ❌ **0 blocks completely missing** (0%)

**But many features/parameters are missing:**
- Capacity, world dimensions
- Roles
- Server locations
- Dynamic/Static modes
- Collision shapes
- Stop/pass behavior
- Broadcast modes
- Synchronization concept

---

## Feature Coverage Analysis

### Game Management Features

| Feature | Block | Current Coverage | Status |
|---------|-------|------------------|--------|
| Create game (basic) | `create game` | T19.G5.01 | ⚠️ Too complex |
| Join game (basic) | `join game` | T19.G5.01 | ⚠️ Too complex |
| Game name | `create/join` | T19.G5.01 | ✅ Covered |
| Password | `create/join` | T19.G5.01 | ✅ Covered |
| Host name | `create/join` | T19.G5.01 | ✅ Covered |
| Display name | `join` | ❌ Not covered | ❌ MISSING |
| **Roles** | `create/join` | ❌ Not covered | ❌ MISSING |
| **Server location** | `create/join/list` | ❌ Not covered | ❌ MISSING |
| **Capacity** | `create` | ❌ Not covered | ❌ MISSING |
| **World dimensions** | `create` | ❌ Not covered | ❌ MISSING |
| List games | `list games` | T19.G5.06 | ⚠️ Conflated |
| List players | `list players` | T19.G5.06 | ⚠️ Conflated |
| Reset world | `reset` | T19.G6.07 | ✅ Covered |
| Connection status | `connected to game` | T19.G5.05 | ✅ Covered |

**Missing: 6 features**

---

### Sprite Management Features

| Feature | Block | Current Coverage | Status |
|---------|-------|------------------|--------|
| Add sprite (basic) | `add sprite` | T19.G5.02 | ✅ Covered |
| **Dynamic vs Static** | `add sprite` | ❌ Not covered | ❌ MISSING |
| **Rectangle vs Circle** | `add sprite` | ❌ Not covered | ❌ MISSING |
| Remove sprite | `remove sprite` | T19.G6.06 | ✅ Covered |
| When added event | `when added` | T19.G5.03 | ✅ Covered |
| **Replication concept** | implicit | ❌ Not covered | ❌ MISSING |

**Missing: 3 features + 1 concept**

---

### Movement Features

| Feature | Block | Current Coverage | Status |
|---------|-------|------------------|--------|
| Sync speed xy | `sync speed x/y` | T19.G6.01 | ⚠️ No concept |
| Sync speed/dir | `sync speed/dir` | T19.G6.01 | ⚠️ No concept |
| **Synchronization concept** | implicit | ❌ Not covered | ❌ MISSING |

**Missing: 1 concept**

---

### Communication Features

| Feature | Block | Current Coverage | Status |
|---------|-------|------------------|--------|
| Broadcast (basic) | `broadcast` | T19.G5.04 | ✅ Covered |
| Broadcast with parameter | `broadcast` | T19.G5.04 | ✅ Covered |
| **All Sprites mode** | `broadcast` | ❌ Not covered | ❌ MISSING |
| **Exclude Replicate mode** | `broadcast` | ❌ Not covered | ❌ MISSING |
| Collision detection | `when touching` | T19.G6.02 | ✅ Covered |
| Collision trigger message | `when touching` | T19.G6.02 | ✅ Covered |
| **Stop behavior** | `when touching` | ❌ Not covered | ❌ MISSING |
| **Pass behavior** | `when touching` | ❌ Not covered | ❌ MISSING |

**Missing: 4 features**

---

## Conceptual Foundation Coverage

| Concept | Importance | Current Coverage | Status |
|---------|-----------|------------------|--------|
| What is multiplayer? | CRITICAL | ❌ Not covered | ❌ MISSING |
| Host-client model | CRITICAL | ❌ Not covered | ❌ MISSING |
| Sprite replication | CRITICAL | ❌ Not covered | ❌ MISSING |
| Synchronization | CRITICAL | ❌ Not covered | ❌ MISSING |
| Dynamic vs Static | HIGH | ❌ Not covered | ❌ MISSING |
| Collision shapes | HIGH | ❌ Not covered | ❌ MISSING |
| Roles system | MEDIUM | ❌ Not covered | ❌ MISSING |
| Server locations | MEDIUM | ❌ Not covered | ❌ MISSING |
| Network latency | MEDIUM | ❌ Not covered | ❌ MISSING |
| Message ordering | LOW | ❌ Not covered | ❌ MISSING |

**Missing: 10 foundational concepts (0% coverage)**

---

## Block Parameters: Complete Coverage Matrix

### Block 1: `create game`

| Parameter | Type | Options | Current Skill | Status |
|-----------|------|---------|---------------|--------|
| GAMENAME | text | any string | T19.G5.01 | ✅ Covered |
| PASSWORD | text | any string | T19.G5.01 | ✅ Covered |
| HOSTNAME | text | any string | T19.G5.01 | ✅ Covered |
| ROLE | text | any string | ❌ Not covered | ❌ MISSING |
| LOCATION | menu | US-East, US-West, Europe, Asia | ❌ Not covered | ❌ MISSING |
| CAPACITY | number | 1-50 | ❌ Not covered | ❌ MISSING |
| W (width) | number | pixels | ❌ Not covered | ❌ MISSING |
| H (height) | number | pixels | ❌ Not covered | ❌ MISSING |

**Coverage: 3/8 = 37.5%**

---

### Block 2: `join game`

| Parameter | Type | Options | Current Skill | Status |
|-----------|------|---------|---------------|--------|
| GAMENAME | text | any string | T19.G5.01 | ✅ Covered |
| HOSTNAME | text | any string | T19.G5.01 | ✅ Covered |
| LOCATION | menu | US-East, US-West, Europe, Asia | ❌ Not covered | ❌ MISSING |
| PASSWORD | text | any string | T19.G5.01 | ✅ Covered |
| DISPLAYNAME | text | any string | ❌ Not covered | ❌ MISSING |
| ROLE | text | any string | ❌ Not covered | ❌ MISSING |

**Coverage: 3/6 = 50%**

---

### Block 3: `list games`

| Parameter | Type | Options | Current Skill | Status |
|-----------|------|---------|---------------|--------|
| LOCATION | menu | US-East, US-West, Europe, Asia | ❌ Not covered | ❌ MISSING |
| TABLE | menu | table variable names | T19.G5.06 | ✅ Covered |

**Returns:** Host Name, Game Name, User Count

**Coverage: 1/2 = 50% (plus return values covered)**

---

### Block 4: `list players`

| Parameter | Type | Options | Current Skill | Status |
|-----------|------|---------|---------------|--------|
| GAMENAME | text | any string | T19.G5.06 | ✅ Covered |
| HOSTNAME | text | any string | T19.G5.06 | ✅ Covered |
| LOCATION | menu | US-East, US-West, Europe, Asia | ❌ Not covered | ❌ MISSING |
| TABLE | menu | table variable names | T19.G5.06 | ✅ Covered |

**Returns:** Player Name, Role

**Coverage: 3/4 = 75% (plus return values covered)**

---

### Block 7: `add sprite to game`

| Parameter | Type | Options | Current Skill | Status |
|-----------|------|---------|---------------|--------|
| MODE | menu | Dynamic, Static | ❌ Not covered | ❌ MISSING |
| SHAPE | menu | Rectangle, Circle | ❌ Not covered | ❌ MISSING |

**Coverage: 0/2 = 0%**

---

### Block 12: `broadcast with parameter`

| Parameter | Type | Options | Current Skill | Status |
|-----------|------|---------|---------------|--------|
| MESSAGE | menu | message names | T19.G5.04 | ✅ Covered |
| PARAMETER | any | any value | T19.G5.04 | ✅ Covered |
| MODE | menu | All Sprites, Exclude Replicate | ❌ Not covered | ❌ MISSING |

**Coverage: 2/3 = 67%**

---

### Block 13: `when touching (collision)`

| Parameter | Type | Options | Current Skill | Status |
|-----------|------|---------|---------------|--------|
| SPRITENAME | menu | sprite names | T19.G6.02 | ✅ Covered |
| STOPTYPE | menu | stop, pass | ❌ Not covered | ❌ MISSING |
| MESSAGE | menu | message names | T19.G6.02 | ✅ Covered |
| PARAMETER | any | any value | T19.G6.02 | ✅ Covered |

**Coverage: 3/4 = 75%**

---

## Overall Parameter Coverage

**Total Parameters: 33**
- ✅ Covered: 18 (54.5%)
- ❌ Missing: 15 (45.5%)

**Most Critical Missing Parameters:**
1. **MODE** (Dynamic/Static) - Block 7
2. **SHAPE** (Rectangle/Circle) - Block 7
3. **MODE** (All Sprites/Exclude Replicate) - Block 12
4. **STOPTYPE** (stop/pass) - Block 13
5. **ROLE** - Blocks 1, 2, 4
6. **LOCATION** (server) - Blocks 1, 2, 3, 4
7. **CAPACITY** - Block 1
8. **World dimensions (W, H)** - Block 1
9. **DISPLAYNAME** - Block 2

---

## Proposed Skill Mapping

### Foundation (NEW - Grade 6)
- **T19.G6.00A:** Multiplayer concept → Covers: What is multiplayer
- **T19.G6.00B:** Host-client model → Covers: HOSTNAME, host/client roles
- **T19.G6.00C:** Replication → Covers: Original vs replicate sprites
- **T19.G6.00D:** Dynamic/Static → Covers: MODE parameter (Block 7)
- **T19.G6.00E:** Collision shapes → Covers: SHAPE parameter (Block 7)
- **T19.G6.00F:** Synchronization → Covers: "synchronously" concept (Blocks 10-11)

### Core Mechanics (REVISED - Grade 6)
- **T19.G6.01A:** Create game (basic) → Covers: Blocks 1 (partial)
- **T19.G6.01B:** Join game (basic) → Covers: Block 2 (partial)
- **T19.G6.01C:** Capacity/dimensions → Covers: CAPACITY, W, H (Block 1)
- **T19.G6.01D:** List games → Covers: Block 3
- **T19.G6.01E:** List players → Covers: Block 4
- **T19.G6.01F:** Connection status → Covers: Block 6
- **T19.G6.02A:** Testing with two windows → Covers: Testing methodology
- **T19.G6.02B:** Add sprites → Covers: Block 7 (with T19.G6.00D/E)
- **T19.G6.02C:** Stop/pass collisions → Covers: STOPTYPE (Block 13)
- **T19.G6.04A:** Broadcast modes → Covers: MODE (Block 12)
- **T19.G6.04B:** Broadcast with param → Covers: Block 12 (with T19.G6.04A)
- **T19.G6.05:** Sync movement → Covers: Blocks 10-11 (with T19.G6.00F)
- **T19.G6.06:** Collisions → Covers: Block 13 (with T19.G6.02C)

### Advanced Topics (NEW/REVISED - Grade 7-8)
- **T19.G7.00A:** Roles → Covers: ROLE parameter (Blocks 1, 2, 4)
- **T19.G7.00B:** Server locations → Covers: LOCATION parameter (Blocks 1-4)
- **T19.G7.00C:** Display names → Covers: DISPLAYNAME (Block 2)

### Result
**All 13 blocks fully covered**
**All 33 parameters covered**
**All 10 foundational concepts covered**

---

## Coverage Improvement

### Current State
- Blocks fully covered: 3/13 (23%)
- Parameters covered: 18/33 (54.5%)
- Concepts covered: 0/10 (0%)

### After Proposed Changes
- Blocks fully covered: 13/13 (100%)
- Parameters covered: 33/33 (100%)
- Concepts covered: 10/10 (100%)

**Total improvement: 77 percentage points**

---

## File Locations

- **This analysis:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T19_BLOCK_MAPPING.md`
- **Full analysis:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T19_MULTIPLAYER_ANALYSIS.md`
- **Summary:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T19_ANALYSIS_SUMMARY.md`
- **Detailed skills:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T19_MISSING_SKILLS_DETAILED.md`
- **Action plan:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/T19_ACTION_PLAN.md`
- **Block code:** `/media/binyu/USB2/scratch-workspace/scratch-gui/src/components/python-editor/blocks/multiplayer-blocks.js`

---

## Quick Reference: What's Missing

### Critical Gaps (Must Fix)
1. ❌ No foundational concepts (multiplayer, host-client, replication, sync)
2. ❌ Dynamic/Static not explained
3. ❌ Collision shapes not explained
4. ❌ Broadcast modes not explained
5. ❌ Stop/pass collisions not explained

### Major Gaps (Should Fix)
6. ❌ Roles not explained
7. ❌ Server locations not explained
8. ❌ Capacity not explained
9. ❌ World dimensions not explained
10. ❌ Display names not explained

### Process Gaps (Should Add)
11. ❌ No testing methodology
12. ❌ Insufficient debugging skills
13. ❌ No practice/application skills
14. ❌ Grade level too low (G5 → G6)

**Total Issues: 14 critical problems requiring ~27 new skills + 8 revised skills**
