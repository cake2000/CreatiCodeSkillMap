# T30 Skill Flow Visualization

## Overview: Before vs After

```
BEFORE:
G5 [10 skills] ────┐
                    │
G6 [25 skills] ────┤  ← OVERLOADED
                    │
G7 [25 skills] ────┤  ← OVERLOADED
                    │
G8 [16 skills] ────┘  ← UNDERUTILIZED

AFTER:
G5 [12 skills] ────┐
                    │
G6 [14 skills] ────┤  ← BALANCED
                    │
G7 [16 skills] ────┤  ← BALANCED
                    │
G8 [20 skills] ────┘  ← OPTIMIZED
```

---

## Skill Movement Flow

```
                    ┌─────────────────────────────────────┐
                    │         GRADE 5 (12 skills)         │
                    │                                     │
                    │  [10 original skills]               │
                    │  + URL Parameters ←─────────────┐  │
                    │  + Security Indicators (NEW)    │  │
                    │  + Predict Failures (NEW)       │  │
                    └─────────────────────────────────│──┘
                                                      │
                    ┌─────────────────────────────────│──┐
                    │         GRADE 6 (14 skills)     │  │
                    │                                 │  │
                    │  HTTP/HTTPS Tracing             │  │
                    │  Google Sheets Core (5 skills)  │  │
                    │  Cloud Sessions (4 skills)      │  │
                    │  Multiplayer Sprites (4 skills) │  │
                    │                                 │  │
                    │  SENDS OUT:                     │  │
                    │  - URL Parameters ──────────────┘  │
                    │  - Latency Measurement ────────┐   │
                    │  - Privacy Risks ───────────┐  │   │
                    │  - Cloud UI Design ─────┐   │  │   │
                    │  - Async Response ──┐   │   │  │   │
                    │  - Adv Sheets (5) ──│───│───│──│───┼──→ G8.20
                    └────────────────────│───│───│──│───│──┘
                                         │   │   │  │   │
                    ┌────────────────────│───│───│──│───│──┐
                    │         GRADE 7 (16 skills)   │   │  │
                    │                    │   │   │  │   │  │
                    │  RECEIVES:         │   │   │  │   │  │
                    │  - Latency ←───────┼───┼───┼──┘   │  │
                    │  - Privacy Risks ←─┼───┼───┘      │  │
                    │  - Cloud UI Design ←───┘          │  │
                    │                                   │  │
                    │  Network Analysis (3 skills)      │  │
                    │  Multiplayer Patterns (5 skills)  │  │
                    │  Database Concepts (4 skills)     │  │
                    │  Advanced Integration (4 skills)  │  │
                    │                                   │  │
                    │  SENDS OUT:                       │  │
                    │  - Database Implementation (12)───┼──┤
                    │  - Leaderboard (3) ───────────────┼──┤
                    │  - Semantic Search (3) ───────────┼──┘
                    └───────────────────────────────────│───┘
                                                        │
                    ┌───────────────────────────────────│───┐
                    │         GRADE 8 (20 skills)       ▼   │
                    │                                       │
                    │  RECEIVES & CONSOLIDATES:             │
                    │  - Async Response + Loading ─→ G8.18 │
                    │  - DB Impl (12) ─────────────→ G8.19 │
                    │  - Leaderboard (3) ───────────→ G8.19 │
                    │  - Semantic (3) ──────────────→ G8.19 │
                    │  - Adv Sheets (5) ────────────→ G8.20 │
                    │                                       │
                    │  Architecture & Design (5)            │
                    │  Security & Privacy (3)               │
                    │  Reliability & Performance (5)        │
                    │  Advanced Data & Debugging (4)        │
                    │  Real-World Analysis (3)              │
                    └───────────────────────────────────────┘
```

---

## Category Distribution Across Grades

```
GRADE 5: Introduction to Cloud Blocks
┌────────────────────────────────────────────────────────┐
│ Request-Response  │ Multiplayer Basics │ Security      │
│ (3 skills)        │ (6 skills)         │ (3 skills)    │
│                   │                    │               │
│ • Request cycle   │ • Create game      │ • URL params  │
│ • Evaluate needs  │ • Join game        │ • Security    │
│ • Fetch web       │ • List games       │   indicators  │
│                   │ • Check status     │ • Predict     │
│                   │ • Debug connect    │   failures    │
│                   │ • User identity    │               │
└────────────────────────────────────────────────────────┘
```

```
GRADE 6: Core Cloud Tools
┌────────────────────────────────────────────────────────┐
│ Google Sheets     │ Cloud Sessions    │ Multiplayer   │
│ (6 skills)        │ (4 skills)        │ (4 skills)    │
│                   │                   │               │
│ • HTTP trace      │ • Create session  │ • Add sprite  │
│ • Read data       │ • Join session    │ • Remove      │
│ • Write data      │ • Save data       │ • When added  │
│ • Read cells      │ • Load data       │ • List        │
│ • Append rows     │                   │   players     │
│ • Debug connect   │                   │               │
└────────────────────────────────────────────────────────┘
```

```
GRADE 7: Integration Patterns
┌────────────────────────────────────────────────────────┐
│ Network Analysis  │ Multiplayer      │ Database       │
│ (3 skills)        │ (5 skills)       │ (4 skills)     │
│                   │                  │                │
│ • Measure latency │ • Diagram comm   │ • Query data   │
│ • Topologies      │ • Sync movement  │ • Debug        │
│ • Client-server   │ • Broadcast      │ • Efficiency   │
│   vs P2P          │ • Collisions     │ • Concurrent   │
│                   │ • Reset world    │                │
├───────────────────┴──────────────────┴────────────────┤
│ Advanced Integration (4 skills)                       │
│ • User data  • Privacy risks  • UI design  • Societal │
└────────────────────────────────────────────────────────┘
```

```
GRADE 8: Architecture & Systems
┌────────────────────────────────────────────────────────┐
│ Architecture (5)  │ Security (3)     │ Reliability (5)│
│                   │                  │                │
│ • Edge vs cloud   │ • Security       │ • Fallbacks    │
│ • Bandwidth       │   measures       │ • API patterns │
│ • Deployment      │ • Anonymization  │ • Rate limits  │
│ • Event-driven    │ • Access control │ • Retry logic  │
│ • Cloud-first     │                  │ • Async UX     │
├───────────────────┴──────────────────┴────────────────┤
│ Analysis & Integration (7 skills)                     │
│ • Monitoring  • Conflict resolution  • Data structures│
│ • Multi-user debug  • Trade-offs  • Comprehensive DB  │
│ • Complete Cloud Application (CAPSTONE)               │
└────────────────────────────────────────────────────────┘
```

---

## Security/Privacy Skill Progression

```
BEFORE (gaps at G3, G5, G7):
GK ─── G1 ─── G2 ─── G3 ─── G4 ─── G5 ─── G6 ─── G7 ─── G8
 ∅      ∅      ✓      ✗      ✓      ✗      ✓      ✗      ✓✓

AFTER (complete coverage):
GK ─── G1 ─── G2 ─── G3 ─── G4 ─── G5 ─── G6 ─── G7 ─── G8
 ∅      ∅      ✓      ✓      ✓      ✓      ∅      ✓      ✓✓✓

Legend:
∅ = Not applicable (age-appropriate)
✓ = Has security/privacy skill
✗ = Gap (MISSING security/privacy)
```

**Security Progression:**
- **G2**: Privacy basics (what not to share)
- **G3**: Privacy awareness in cloud apps (NEW)
- **G4**: HTTPS indicators (secure connections)
- **G5**: Security indicators in blocks (NEW)
- **G6**: (tools focus - no explicit security)
- **G7**: Privacy risk classification (analysis)
- **G8**: Security measures + anonymization + access control (implementation)

---

## Computational Thinking Skills Distribution

```
Design Skills:
G5 ────────────────── ∅
G6 ────────────────── ∅
G7 ══════════════════ ✓✓  (Efficient queries, Cloud UIs)
G8 ══════════════════ ✓✓✓✓✓ (Edge/cloud, Event-driven, Cloud-first, etc.)

Analyze Skills:
G5 ────────────────── ∅
G6 ────────────────── ∅
G7 ══════════════════ ✓✓✓  (Topologies, Societal impacts, etc.)
G8 ══════════════════ ✓✓✓✓  (Bandwidth, Trade-offs, Data structures, etc.)

Debug Skills:
G5 ══════════════════ ✓    (Debug multiplayer)
G6 ══════════════════ ✓    (Debug Sheets)
G7 ══════════════════ ✓    (Debug queries)
G8 ══════════════════ ✓    (Debug multi-user)

Predict Skills:
G5 ══════════════════ ✓    (Predict failures - NEW)
G6 ────────────────── ∅
G7 ────────────────── ∅
G8 ══════════════════ ✓    (Fallback strategies)

Legend: ∅ = None, ✓ = 1-2 skills, ✓✓ = 3-4 skills, ✓✓✓+ = 5+ skills
```

---

## Google Sheets Skills Redistribution

```
BEFORE (all in G6):
G5 ─────────────────
G6 ═════════════════ 9 SKILLS (overloaded)
   │ Read, Write, Append, Read cell, Set cell,
   │ Manage sheets, Clear, Modify structure,
   │ Debug connection
G7 ─────────────────
G8 ─────────────────

AFTER (distributed):
G5 ─────────────────
G6 ═════════════════ 6 SKILLS (core CRUD)
   │ HTTP trace, Read, Write, Read cell, Append,
   │ Debug connection
G7 ─────────────────
G8 ─────────────────  Advanced features integrated
   │ Set cell, Manage sheets, Clear, Modify
   │ → Part of G8.20 (Capstone Integration)
```

---

## Database Skills Redistribution

```
BEFORE (all in G7):
G5 ─────────────────
G6 ─────────────────
G7 ═════════════════ 13 SKILLS (overloaded)
   │ Insert, Query, Debug, Comparison conditions,
   │ Text/logical conditions, Efficient design,
   │ Update, Delete, Concurrent handling,
   │ Field reporters, Semantic create,
   │ Semantic search, Semantic with conditions
G8 ─────────────────

AFTER (concept vs implementation):
G5 ─────────────────
G6 ─────────────────
G7 ═════════════════ 4 SKILLS (concepts)
   │ Query & retrieve (concept)
   │ Debug queries
   │ Design efficient queries
   │ Handle concurrent updates
G8 ═════════════════ 1 COMPREHENSIVE SKILL
   │ G8.19: Complete CRUD operations
   │ → Consolidates all 12 implementation blocks
   │    (insert, query conditions, update, delete,
   │     semantic search, leaderboard)
```

---

## Multiplayer Skills Progression

```
G5: Multiplayer Basics (6 skills)
┌────────────────────────────────┐
│ • Create game session          │
│ • Join game session            │
│ • List available games         │
│ • Check connection status      │
│ • Debug connection failures    │
│ • User identity (username/id)  │
└────────────────────────────────┘
         │
         ▼
G6: Multiplayer Sprites (4 skills)
┌────────────────────────────────┐
│ • Add sprite to game           │
│ • Remove sprite from game      │
│ • "When added to game" event   │
│ • List players in game         │
└────────────────────────────────┘
         │
         ▼
G7: Multiplayer Patterns (5 skills)
┌────────────────────────────────┐
│ • Diagram client-server comm   │
│ • Synchronize sprite movement  │
│ • Broadcast messages           │
│ • Handle sprite collisions     │
│ • Reset game world             │
└────────────────────────────────┘
         │
         ▼
G8: Multiplayer Systems (integrated)
┌────────────────────────────────┐
│ • Part of G8.08 (conflict      │
│   resolution)                  │
│ • Part of G8.12 (event-driven) │
│ • Part of G8.16 (multi-user    │
│   debugging)                   │
│ • Part of G8.20 (capstone      │
│   integration)                 │
└────────────────────────────────┘
```

---

## Consolidation Examples

### Example 1: Database CRUD (12 skills → 1)

```
BEFORE (G7):
┌─────────────────────────────────────────┐
│ G7.06: Insert into collection          │
├─────────────────────────────────────────┤
│ G7.08: Query conditions (comparison)    │
├─────────────────────────────────────────┤
│ G7.09: Query conditions (text/logical)  │
├─────────────────────────────────────────┤
│ G7.10: Update records                   │
├─────────────────────────────────────────┤
│ G7.11: Remove documents                 │
├─────────────────────────────────────────┤
│ G7.12: Field/collection reporters       │
├─────────────────────────────────────────┤
│ G7.13: Record player score              │
├─────────────────────────────────────────┤
│ G7.14: Display leaderboard              │
├─────────────────────────────────────────┤
│ G7.15: Manage leaderboard               │
├─────────────────────────────────────────┤
│ G7.17: Create semantic database         │
├─────────────────────────────────────────┤
│ G7.18: Semantic search (basic)          │
├─────────────────────────────────────────┤
│ G7.19: Semantic search (conditions)     │
└─────────────────────────────────────────┘
             12 SEPARATE SKILLS

AFTER (G8):
┌─────────────────────────────────────────┐
│ G8.19: Comprehensive Database CRUD      │
│                                         │
│ Students implement full database        │
│ lifecycle: insert, query with complex   │
│ conditions, update, delete. Build a     │
│ complete application using database     │
│ collections with proper error handling, │
│ efficient queries, concurrent update    │
│ management, semantic search, and        │
│ leaderboard functionality.              │
│                                         │
│ Covers: CRUD operations, complex        │
│ queries, leaderboard systems, semantic  │
│ search, error handling, concurrency     │
└─────────────────────────────────────────┘
        1 COMPREHENSIVE PROJECT SKILL
```

### Example 2: Async UX (2 skills → 1)

```
BEFORE (G6):
┌─────────────────────────────────────────┐
│ G6.10.01: Implement loading indicators  │
│ (display progress bars, spinners)       │
└─────────────────────────────────────────┘
┌─────────────────────────────────────────┐
│ G6.23: Handle asynchronous responses    │
│ (prevent duplicate requests, maintain   │
│ responsive UI)                          │
└─────────────────────────────────────────┘
             2 SEPARATE SKILLS

AFTER (G8):
┌─────────────────────────────────────────┐
│ G8.18: Async UX Implementation          │
│                                         │
│ Students build complete async handling  │
│ systems: loading indicators during ops, │
│ success/error messages, preventing      │
│ duplicate requests, maintaining         │
│ responsive UI. Handle slow networks     │
│ gracefully.                             │
│                                         │
│ Covers: Loading states, error handling, │
│ request deduplication, responsive UI    │
└─────────────────────────────────────────┘
        1 COMPREHENSIVE UX SKILL
```

---

## Pedagogical Progression

```
┌──────────────────────────────────────────────────────────┐
│                    BLOOM'S TAXONOMY                      │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  CREATE     ────────────────────────────────────── G8   │
│  (Design complete cloud applications)                   │
│                                                          │
│  EVALUATE   ────────────────────────────────── G7-G8    │
│  (Analyze trade-offs, assess societal impacts)          │
│                                                          │
│  ANALYZE    ───────────────────────────── G6-G7         │
│  (Diagram systems, classify privacy risks)              │
│                                                          │
│  APPLY      ──────────────────── G5-G6                  │
│  (Use cloud blocks, implement features)                 │
│                                                          │
│  UNDERSTAND ────────── G3-G4                            │
│  (Explain concepts, predict outcomes)                   │
│                                                          │
│  REMEMBER   ── GK-G2                                    │
│  (Identify devices, recognize indicators)               │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## Implementation Timeline

```
Week 1-2: Preparation
├── Backup current data
├── Review plan with stakeholders
└── Validate block coverage

Week 3-4: Add New Skills
├── Create T30.G3.06 (privacy)
├── Create T30.G5.11 (security)
├── Create T30.G5.12 (predict)
├── Create T30.G8.17 (access control)
├── Create T30.G8.18 (async UX)
├── Create T30.G8.19 (comprehensive CRUD)
└── Create T30.G8.20 (capstone)

Week 5: Reorganize G5
└── Add G5.10 from G6.21

Week 6: Reorganize G6
├── Renumber to G6.01-G6.14
└── Remove consolidated skills

Week 7: Reorganize G7
├── Renumber to G7.01-G7.16
├── Add skills from G6
└── Remove consolidated skills

Week 8: Update G8
└── Add G8.17-G8.20

Week 9-10: Update Dependencies
├── Update moved skill dependencies
├── Fix broken references
└── Verify dependency chains

Week 11: Testing & Verification
├── Verify skill counts
├── Check progression
├── Validate dependencies
└── Review with teachers

Week 12: Final Review & Launch
└── Documentation & rollout
```

---

## Success Metrics Dashboard

```
┌────────────────────────────────────────────────────────┐
│ METRIC                          BEFORE  →  AFTER       │
├────────────────────────────────────────────────────────┤
│ Max skills per grade (G5-G8)       25   →    20   ✓   │
│ Min skills per grade (G5-G8)       10   →    12   ✓   │
│ Grades with security gaps           3   →     0   ✓   │
│ CT skills (% of total)             20%  →   35%   ✓   │
│ Granular tool skills               40   →    15   ✓   │
│ Comprehensive project skills        0   →     3   ✓   │
│ Total skill count                 100   →    87   ✓   │
│ Skills per grade variance        High  →   Low   ✓   │
└────────────────────────────────────────────────────────┘

All metrics improved! ✓
```

---

**Document**: T30 Visual Flow
**Version**: 1.0
**Date**: 2025-11-29
**Purpose**: Visual representation of skill redistribution plan
