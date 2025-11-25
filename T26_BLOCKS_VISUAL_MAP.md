# T26 Data Collection & Logging - Visual Block Map

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CREATICODE BLOCKS FOR T26                         │
│                Data Collection & Logging (105+ Blocks)               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────┬─────────────────┬─────────────────┬──────────────┐
│   VARIABLES     │    DATABASE     │     CLOUD       │   CONTROL    │
│   (60 blocks)   │   (15 blocks)   │   (16 blocks)   │  (3 blocks)  │
├─────────────────┼─────────────────┼─────────────────┼──────────────┤
│ • Lists (25)    │ • Collections   │ • Google Sheets │ • Console    │
│   - Basic CRUD  │   - Insert      │   (15 blocks)   │   Logging    │
│   - Sort/Shuffle│   - Fetch       │   - Read/Write  │ • Get Logs   │
│   - Statistics  │   - Update      │   - CRUD Sheets │              │
│   - Iteration   │   - Delete      │   - Cell Access │              │
│   - Text Ops    │   - Query (8)   │ • Drive (1)     │              │
│                 │     - Conditions│   - List Files  │              │
│ • Tables (25)   │     - Fields    │                 │              │
│   - Row Ops     │     - Operators │                 │              │
│   - Column Ops  │                 │                 │              │
│   - Cell Access │                 │                 │              │
│   - Stats       │                 │                 │              │
│   - Sort/Pivot  │                 │                 │              │
│   - CSV I/O     │                 │                 │              │
│                 │                 │                 │              │
│ • Persistence   │                 │                 │              │
│   - Export (4)  │                 │                 │              │
│   - Server (4)  │                 │                 │              │
│   - Import (2)  │                 │                 │              │
└─────────────────┴─────────────────┴─────────────────┴──────────────┘

┌─────────────────┬─────────────────┐
│  MULTIPLAYER    │    AI & OTHER   │
│   (5 blocks)    │   (7 blocks)    │
├─────────────────┼─────────────────┤
│ • Game Mgmt (3) │ • Semantic DB   │
│   - Create      │   - Create      │
│   - List        │   - Search (2)  │
│   - Reset       │ • Web Search    │
│ • Sync (2)      │ • Regex (4)     │
│   - Speed       │   - Match       │
│   - Direction   │   - Split       │
└─────────────────┴─────────────────┘


═══════════════════════════════════════════════════════════════════
                        GRADE-LEVEL PROGRESSION
═══════════════════════════════════════════════════════════════════

K-G2 (Unplugged)
┌────────────────────────────────────────────┐
│ No blocks needed - Physical activities     │
│ • Counting tokens                          │
│ • Picture surveys                          │
│ • Paper record sheets                      │
└────────────────────────────────────────────┘

G3: Introduction to Digital Collection
┌────────────────────────────────────────────┐
│ LISTS + EVENTS + VARIABLES                 │
│ ┌────────────┬──────────────┬────────────┐│
│ │ ask/answer │ add to list  │ counters   ││
│ │ repeat     │ item of list │ timers     ││
│ └────────────┴──────────────┴────────────┘│
└────────────────────────────────────────────┘

G4: Structured Data
┌────────────────────────────────────────────┐
│ TABLES + LISTS + CONDITIONALS              │
│ ┌──────────────────┬──────────────────────┐│
│ │ add to table     │ if/else              ││
│ │ item at row/col  │ validation           ││
│ │ sort table       │ privacy checks       ││
│ └──────────────────┴──────────────────────┘│
└────────────────────────────────────────────┘

G5: Persistence & Monitoring
┌────────────────────────────────────────────┐
│ EXPORT + LOGGING + VALIDATION              │
│ ┌──────────────┬───────────┬─────────────┐│
│ │ export table │ print log │ repeat until││
│ │ CSV files    │ console   │ sampling    ││
│ └──────────────┴───────────┴─────────────┘│
└────────────────────────────────────────────┘

G6: Cloud & Collaboration
┌────────────────────────────────────────────┐
│ GOOGLE SHEETS + MULTI-INPUT + CONSENT      │
│ ┌────────────────┬────────────────────────┐│
│ │ read/write     │ stakeholder tables     ││
│ │ sheets         │ opt-in/opt-out         ││
│ │ sync data      │ video/voice/pose       ││
│ └────────────────┴────────────────────────┘│
└────────────────────────────────────────────┘

G7: Professional Practices
┌────────────────────────────────────────────┐
│ CUSTOM BLOCKS + DATABASE + MONITORING      │
│ ┌─────────────┬────────────┬─────────────┐│
│ │ define      │ collections│ provenance  ││
│ │ parameters  │ queries    │ quality     ││
│ │ reusable    │ conditions │ tracking    ││
│ └─────────────┴────────────┴─────────────┘│
└────────────────────────────────────────────┘

G8: End-to-End Pipelines
┌────────────────────────────────────────────┐
│ DATABASE + SHEETS + AI + AUTOMATION        │
│ ┌──────────────────────────────────────────┐│
│ │ fetch → process → store → export        ││
│ │ telemetry → database → Google Sheets    ││
│ │ scheduled exports + AI quality review   ││
│ └──────────────────────────────────────────┘│
└────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════
                           DATA FLOW PATTERNS
═══════════════════════════════════════════════════════════════════

PATTERN 1: Simple Collection (G3)
┌──────┐     ┌──────┐     ┌──────┐
│ ask  │ ──> │ list │ ──> │ show │
└──────┘     └──────┘     └──────┘

PATTERN 2: Structured Logging (G4-G5)
┌──────┐     ┌───────┐     ┌────────┐     ┌──────┐
│event │ ──> │ table │ ──> │validate│ ──> │ CSV  │
└──────┘     └───────┘     └────────┘     └──────┘

PATTERN 3: Cloud Pipeline (G6-G7)
┌──────┐     ┌───────┐     ┌──────────┐     ┌────────┐
│inputs│ ──> │ table │ ──> │ database │ ──> │ Sheets │
└──────┘     └───────┘     └──────────┘     └────────┘
               │                                 ^
               └─────────────────────────────────┘
                     (bidirectional sync)

PATTERN 4: Telemetry (G8)
┌─────────┐     ┌─────────┐     ┌──────────┐
│ sensors │ ──> │ process │ ──> │ database │
└─────────┘     └─────────┘     └──────────┘
                      │               │
                      v               v
                 ┌─────────┐     ┌────────┐
                 │ console │     │ Sheets │
                 │   log   │     │ export │
                 └─────────┘     └────────┘


═══════════════════════════════════════════════════════════════════
                        STORAGE DECISION TREE
═══════════════════════════════════════════════════════════════════

Need to save data?
    │
    ├─ NO ──> Use variables/lists (session only)
    │
    └─ YES
        │
        ├─ Just for this user?
        │   │
        │   ├─ On their computer? ──> export/import
        │   └─ On server? ──> save data (private)
        │
        └─ Share with others?
            │
            ├─ Within project? ──> save data (public) or database
            │
            └─ External access?
                │
                ├─ Collaboration? ──> Google Sheets
                └─ Real-time game? ──> Multiplayer


═══════════════════════════════════════════════════════════════════
                      BLOCK COMPLEXITY LEVELS
═══════════════════════════════════════════════════════════════════

BASIC (G3-G4)
┌──────────────────────────────────────────────────────┐
│ • add to [list v] item []                            │
│ • delete () of [list v]                              │
│ • item () of [list v]                                │
│ • add to table []: [] [] []                          │
│ • print [] in [console v] color []                   │
└──────────────────────────────────────────────────────┘

INTERMEDIATE (G5-G6)
┌──────────────────────────────────────────────────────┐
│ • export table [] as []                              │
│ • sort list [] from [method v]                       │
│ • for each item [] in []                             │
│ • read from google sheet: url [] ... into table []   │
│ • save [visibility v] data [] with name []           │
└──────────────────────────────────────────────────────┘

ADVANCED (G7-G8)
┌──────────────────────────────────────────────────────┐
│ • define collect_data (param1) (param2)              │
│ • fetch from collection [] into table []             │
│   where <cond (field []) [op] []>                    │
│ • update collection [] in-place where <cond>         │
│   set () to () set () to ()                          │
│ • create semantic database from table []             │
└──────────────────────────────────────────────────────┘


═══════════════════════════════════════════════════════════════════
                    COMMON BLOCK COMBINATIONS
═══════════════════════════════════════════════════════════════════

SURVEY LOOP
┌────────────────────────────────┐
│ repeat (n)                     │
│   ask [question] and wait      │
│   add (answer) to [list v]     │
│ end                            │
└────────────────────────────────┘

EVENT COUNTER
┌────────────────────────────────┐
│ when [space v] key pressed     │
│ change [counter v] by (1)      │
│ add to table [log v]:          │
│   (timer) [jump] (counter) []  │
└────────────────────────────────┘

VALIDATED INPUT
┌────────────────────────────────┐
│ repeat until <(answer) > [0]>  │
│   ask [Enter positive:] & wait │
│   if <(answer) < [1]> then     │
│     print [Invalid!] in ...    │
│   end                          │
│ end                            │
│ add (answer) to [data v]       │
└────────────────────────────────┘

CONSENT WORKFLOW
┌────────────────────────────────┐
│ ask [Share age? y/n] and wait  │
│ if <(answer) = [y]> then       │
│   ask [Age?] and wait          │
│   add (answer) to [ages v]     │
│ else                           │
│   print [Opted out] in ...     │
│ end                            │
└────────────────────────────────┘

CSV EXPORT
┌────────────────────────────────┐
│ // Collect data in table       │
│ add to table [data v]: ...     │
│ ...                            │
│ // Export when done            │
│ export table [data v] as       │
│   [experiment_results]         │
└────────────────────────────────┘

GOOGLE SHEETS SYNC
┌────────────────────────────────┐
│ write into google sheet:       │
│   url [https://docs.google...] │
│   sheet name [Data]            │
│   start cell [A1]              │
│   from table [collected v]     │
└────────────────────────────────┘


═══════════════════════════════════════════════════════════════════
                      FEATURE COMPARISON MATRIX
═══════════════════════════════════════════════════════════════════

Feature                 | Scratch | CreatiCode | Advantage
────────────────────────┼─────────┼────────────┼──────────────────
Lists                   |    ✓    |     ✓✓     | +18 extended ops
Tables                  |    ✗    |     ✓      | Native support
CSV Export              |    ✗    |     ✓      | One-block export
Server Storage          |  Cloud  |   ✓✓✓      | Key-val+table+DB
Google Sheets           | Extension|    ✓      | Native integration
Console Logging         |    ✗    |     ✓      | Color-coded
Database                |    ✗    |     ✓      | Full CRUD
Multiplayer Sync        |    ✗    |     ✓      | Built-in
Statistical Functions   |    ✗    |     ✓      | Min/max/avg/etc
Regex Operations        |    ✗    |     ✓      | Match/split
Pivot Tables            |    ✗    |     ✓      | Native support

Legend: ✓ = Basic, ✓✓ = Enhanced, ✓✓✓ = Advanced, ✗ = Not available


═══════════════════════════════════════════════════════════════════
                           QUICK STATS
═══════════════════════════════════════════════════════════════════

Total Blocks for T26:    105+
Total Categories:        10
File Formats Supported:  4 (TXT, CSV, JSON, Google Sheets)
Persistence Methods:     5
Storage Scopes:          6 (local, session, project, user, external, game)
Grade Levels Supported:  K-G8 (100%)
Skills Fully Covered:    45/45
Platform Blockers:       0

Documentation Generated:
• T26_DATA_BLOCKS_ANALYSIS.md:    20 KB (technical reference)
• T26_BLOCKS_QUICK_REF.md:        12 KB (lookup tables)
• T26_BLOCKS_SUMMARY.md:          14 KB (analysis & pedagogy)
• T26_BLOCKS_INDEX.md:            6 KB (navigation guide)
• T26_BLOCKS_VISUAL_MAP.md:       This file

Total Documentation:              ~52 KB


═══════════════════════════════════════════════════════════════════
                          NAVIGATION GUIDE
═══════════════════════════════════════════════════════════════════

For detailed block syntax:        → T26_DATA_BLOCKS_ANALYSIS.md
For quick block lookup:           → T26_BLOCKS_QUICK_REF.md
For platform analysis:            → T26_BLOCKS_SUMMARY.md
For document overview:            → T26_BLOCKS_INDEX.md
For visual understanding:         → You are here!

Analysis Date: 2025-11-25
Source: /media/binyu/USB2/ScratchCopilot/blockdes8.txt
