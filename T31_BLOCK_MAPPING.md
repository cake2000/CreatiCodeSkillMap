# T31 Block-to-Skill Mapping Reference

## Cloud Category Blocks - Where They Should Be

### Web Fetch
| Block | Current Coverage | Should Be In | Recommended Skill |
|-------|-----------------|--------------|-------------------|
| fetch web page as [FORMAT] from URL [URL] | T31.G5.03 ❌ | T33.G6.02 ✅ | Already exists in T33 |

### Google Sheets - Read Operations
| Block | Current Coverage | Should Be In | Recommended Skill |
|-------|-----------------|--------------|-------------------|
| read from google sheet: url [...] into table | T31.G6.02 ❌ | T33.G6.03 ✅ | Already exists in T33 |
| value at row (ROW) column (COL) of sheet | T31.G6.02 ❌ | T33.G7.02 ✅ | Already exists in T33 |

### Google Sheets - Write Operations
| Block | Current Coverage | Should Be In | Recommended Skill |
|-------|-----------------|--------------|-------------------|
| write into google sheet [...] from table | T31.G6.03 ❌ | T33.G6.04 ✅ | Already exists in T33 |
| set value to [...] at row column | T31.G6.03 ❌ | T33.G7.02 ✅ | Already exists in T33 |
| append row [...] from table to sheet | T31.G6.03.01 ❌ | T33.G7.03 ✅ | Already exists in T33 |

### Google Sheets - Structure Management
| Block | Current Coverage | Should Be In | Recommended Skill |
|-------|-----------------|--------------|-------------------|
| list all sheets in google sheet | T31.G6.03.02 ❌ | T33.G7.01 ✅ | Already exists in T33 |
| add sheet [...] to google sheet | T31.G6.03.02 ❌ | T33.G7.01 ✅ | Already exists in T33 |
| remove sheet [...] from google sheet | T31.G6.03.02 ❌ | T33.G7.01 ✅ | Already exists in T33 |
| clear sheet [...] in Google Sheet | NOT COVERED | T33.G6.05 ✅ | Already exists in T33 |
| insert [COUNT] rows at row | NOT COVERED | T33.G8.01 ✅ | Already exists in T33 |
| insert [COUNT] columns at column | NOT COVERED | T33.G8.01 ✅ | Already exists in T33 |
| remove rows [FROM] to [TO] | NOT COVERED | T33.G8.01 ✅ | Already exists in T33 |
| remove columns [FROM] to [TO] | NOT COVERED | T33.G8.01 ✅ | Already exists in T33 |

### Google Drive
| Block | Current Coverage | Should Be In | Recommended Skill |
|-------|-----------------|--------------|-------------------|
| list content of Google Drive folder | NOT COVERED | T33.G7.04 ✅ | Already exists in T33 |

---

## Multiplayer Category Blocks - Where They Should Be

### Session Management
| Block | Current Coverage | Should Be In | Notes |
|-------|-----------------|--------------|-------|
| create game named [...] | T31.G5.04 ❌ | T19 ✅ | Need to verify T19 exists |
| join multiplayer game [...] | T31.G5.04 ❌ | T19 ✅ | Need to verify T19 exists |
| list multiplayer games [...] | T31.G5.04 ❌ | T19 ✅ | Need to verify T19 exists |
| list players in game [...] | T31.G5.04 ❌ | T19 ✅ | Need to verify T19 exists |
| connected to game (boolean) | T31.G5.05 ❌ | T19 ✅ | Need to verify T19 exists |
| reset game world | NOT COVERED | T19 ✅ | Need to verify T19 exists |

### Sprite Management in Multiplayer
| Block | Current Coverage | Should Be In | Notes |
|-------|-----------------|--------------|-------|
| add this sprite to game as [...] | T31.G6.06 ❌ | T19 ✅ | Need to verify T19 exists |
| when added to game (hat block) | T31.G6.06 ❌ | T19 ✅ | Need to verify T19 exists |
| remove this sprite from game | T31.G6.06 ❌ | T19 ✅ | Need to verify T19 exists |

### Movement Synchronization
| Block | Current Coverage | Should Be In | Notes |
|-------|-----------------|--------------|-------|
| synchronously set speed x (X) y (Y) | T31.G7.02 ❌ | T19 ✅ | Need to verify T19 exists |
| synchronously set speed (SPEED) dir (DIR) | T31.G7.02 ❌ | T19 ✅ | Need to verify T19 exists |

### Communication & Interaction
| Block | Current Coverage | Should Be In | Notes |
|-------|-----------------|--------------|-------|
| broadcast [MESSAGE] with parameter [...] | T31.G7.02.01 ❌ | T19 ✅ | Need to verify T19 exists |
| when touching [...] will [...] and trigger [...] | T31.G7.02.02 ❌ | T19 ✅ | Need to verify T19 exists |

---

## Database Category Blocks - Where They Should Be

### CRUD Operations
| Block | Current Coverage | Should Be In | Recommended Skill |
|-------|-----------------|--------------|-------------------|
| insert from table [...] into collection | T31.G7.02.03 ❌ | T33 ✅ | Need new T33 skill |
| fetch from collection [...] where | T31.G7.02.04 ❌ | T33 ✅ | Need new T33 skill |
| update collection [...] from table | T31.G7.02.05 ❌ | T33 ✅ | Need new T33 skill |
| update collection [...] in-place where | T31.G7.02.05 ❌ | T33 ✅ | Need new T33 skill |
| remove all documents from collection | T31.G7.02.05 ❌ | T33 ✅ | Need new T33 skill |

### Query Helpers
| Block | Current Coverage | Should Be In | Notes |
|-------|-----------------|--------------|-------|
| collection [COLLECTIONNAME] | T31.G7.02.03-05 ❌ | T33 ✅ | Helper block |
| field [FIELDNAME] | T31.G7.02.03-05 ❌ | T33 ✅ | Helper block |
| <cond [...] [COMPARATOR] [...]> | T31.G7.02.04-05 ❌ | T33 ✅ | Query condition |
| <cond (field [...]) contains [...]?> | T31.G7.02.04-05 ❌ | T33 ✅ | Query condition |
| <cond not <>> | T31.G7.02.04-05 ❌ | T33 ✅ | Query operator |
| <cond <> and <>> | T31.G7.02.04-05 ❌ | T33 ✅ | Query operator |
| <cond <> or <>> | T31.G7.02.04-05 ❌ | T33 ✅ | Query operator |
| op [...] [OPERATOR] [...] | T31.G7.02.05 ❌ | T33 ✅ | Field operator |

---

## Game Category - Persistent Data Blocks

### Leaderboard
| Block | Current Coverage | Should Be In | Priority |
|-------|-----------------|--------------|----------|
| record player score (VALUE) | NOT COVERED ❌ | T31.G6 NEW ✅ | HIGH - Add this |
| show game leaderboard [...] | NOT COVERED ❌ | T31.G6 NEW ✅ | HIGH - Add this |
| hide game leaderboard | NOT COVERED ❌ | T31.G6 NEW ✅ | HIGH - Add this |
| clear scores for [WHO] | NOT COVERED ❌ | T31.G6 NEW ✅ | HIGH - Add this |

### User Data Storage
| Block | Current Coverage | Should Be In | Priority |
|-------|-----------------|--------------|----------|
| store user data key [...] value [...] | NOT COVERED ❌ | T31.G5 NEW ✅ | HIGH - Add this |
| read user data key [...] | NOT COVERED ❌ | T31.G5 NEW ✅ | HIGH - Add this |

---

## Other Network-Related Blocks

### Sensing Category
| Block | Current Coverage | Should Be In | Priority |
|-------|-----------------|--------------|----------|
| read URL parameter [PARAMETER] | NOT COVERED ❌ | T31.G5 NEW ✅ | HIGH - Add this |

### Looks Category
| Block | Current Coverage | Should Be In | Priority |
|-------|-----------------|--------------|----------|
| add costume named [...] from URL | NOT COVERED | Could add to T31.G6 | LOW - Optional |

---

## Conceptual Skills (No Specific Blocks)

These T31 skills teach concepts without specific CreatiCode blocks:

### Good Conceptual Skills (Keep)
- **T31.GK.01**: Recognize internet devices
- **T31.G1.01**: Connected vs disconnected
- **T31.G2.01**: Internet connects computers
- **T31.G2.02**: Safe online behavior (consider T32)
- **T31.G3.01**: Trace device-to-website path
- **T31.G3.02**: Types of online sharing
- **T31.G4.01**: How data travels (packets)
- **T31.G4.02**: Secure websites (consider T32)
- **T31.G5.01**: Trace device to service
- **T31.G5.02**: Internet vs offline apps
- **T31.G6.01**: HTTP/HTTPS request steps
- **T31.G7.03**: Network topologies
- **T31.G7.04**: Client-server vs P2P
- **T31.G7.05**: Societal impacts

### Vague Conceptual Skills (Need Clarification)
- **T31.G6.04**: Latency effects on AI
  - **Fix**: Use timer blocks to measure response time
- **T31.G6.05**: Privacy of AI data
  - **Consider**: Move to T32 (Cybersecurity)
- **T31.G7.01**: Distributed multiplayer server
  - **Fix**: Make generic (not multiplayer-specific) or move to T19
- **T31.G8.01**: Edge vs cloud processing
  - **Fix**: Mark as design/diagramming activity
- **T31.G8.02**: AI service network requirements
  - **Fix**: Add measurable metrics (bandwidth, latency)
- **T31.G8.03**: Secure AI cloud systems
  - **Consider**: Move to T32
- **T31.G8.04**: Privacy protection for AI data
  - **Consider**: Move to T32
- **T31.G8.05**: AI service resilience
  - **Fix**: Add specific error handling patterns
- **T31.G8.06**: AI monitoring dashboards
  - **Fix**: Simplify or mark as advanced capstone

---

## Summary Tables

### Blocks Currently in T31 That Should Move

| Category | Count | Destination |
|----------|-------|-------------|
| Cloud (Google Sheets/Drive/Web Fetch) | 15 blocks | T33 |
| Multiplayer | 13 blocks | T19 |
| Database | 12 blocks | T33 |
| **Total Moving Out** | **40 blocks** | - |

### Blocks NOT in T31 That Should Be Added

| Category | Count | New Skills Needed |
|----------|-------|-------------------|
| Game - User Data | 2 blocks | T31.G5.06 (NEW) |
| Game - Leaderboard | 4 blocks | T31.G6.07 (NEW) |
| Sensing - URL Params | 1 block | T31.G5.03 (NEW) |
| **Total Adding** | **7 blocks** | **3 new skills** |

### Final T31 Block Count

| Type | Count |
|------|-------|
| Conceptual skills (no blocks) | ~14 skills |
| Hands-on skills (with blocks) | ~7 skills |
| Total measurement/analysis skills | ~4 skills |
| **Total T31 Skills** | **~25 skills** |

---

## Action Plan for Block Coverage

### Phase 1: Remove Incorrect Skills
1. Move all Google Sheets skills (7 skills) → T33
2. Move all Multiplayer skills (8 skills) → T19
3. Move all Database skills (3 skills) → T33

### Phase 2: Add Missing Skills
4. Add T31.G5.03 (NEW): Read URL parameters
5. Add T31.G5.06 (NEW): Store/retrieve user data
6. Add T31.G6.07 (NEW): Game leaderboards

### Phase 3: Fix Vague Skills
7. Clarify T31.G6.04: Add timer block usage
8. Clarify T31.G8.01-06: Add specific implementation or mark as conceptual

### Phase 4: Review Cross-Topic
9. Review T31.G2.02, G4.02, G6.05, G8.03, G8.04 for T32 movement
10. Verify all T33 skills properly cover moved blocks
11. Verify T19 exists and accepts multiplayer skills
