# T30 Internet & Cloud: Comprehensive Redistribution Plan

## Current State Analysis

### Skill Count by Grade
- **GK**: 4 skills (picture-based foundational concepts)
- **G1**: 4 skills (picture-based connectivity awareness)
- **G2**: 5 skills (picture-based cloud storage intro)
- **G3**: 5 skills (network components, URLs, cloud save/load)
- **G4**: 6 skills (packets, HTTPS, storage trade-offs, debugging)
- **G5**: 10 skills (request-response, multiplayer basics, web fetch, user identity)
- **G6**: 25 skills ⚠️ **OVERLOADED**
- **G7**: 25 skills ⚠️ **OVERLOADED**
- **G8**: 16 skills ⚠️ **UNDERUTILIZED**

### G6 Current Skills by Category (25 total)
**Google Sheets (9 skills):**
- G6.02: Read from Google Sheet
- G6.02.01: Debug Google Sheets connection
- G6.03: Write to Google Sheet
- G6.04: Set individual cell values
- G6.05: Read individual cell values
- G6.06: Append rows
- G6.07: Manage sheets (list/add/remove)
- G6.08: Clear sheet data
- G6.09: Modify sheet structure (insert/remove rows/columns)

**Multiplayer (4 skills):**
- G6.12: Add sprite to game
- G6.13: Remove sprite from game
- G6.14: "when added to game" event
- G6.15: List players in game

**Cloud Sessions (4 skills):**
- G6.16: Create cloud session
- G6.17: Join cloud session
- G6.18: Save cloud data (public/private)
- G6.19: Load cloud data

**UI/UX (3 skills):**
- G6.10.01: Implement loading indicators
- G6.22: Design cloud-connected UIs
- G6.23: Handle asynchronous responses

**Miscellaneous (5 skills):**
- G6.01: Trace HTTP/HTTPS request
- G6.10: Measure network latency
- G6.11: Classify data privacy risks
- G6.20: Access Google Drive folder contents
- G6.21: Read URL parameters

### G7 Current Skills by Category (25 total)
**Database (13 skills):**
- G7.06: Insert into database collection
- G7.07: Query/retrieve from collections
- G7.07.01: Debug database queries
- G7.08: Build query conditions (comparison)
- G7.09: Build query conditions (text search, logical)
- G7.09.01: Design efficient queries
- G7.10: Update database records
- G7.11: Remove database documents
- G7.11.01: Handle concurrent updates
- G7.12: Use field/collection reporter blocks
- G7.17: Create semantic database
- G7.18: Search semantic database (basic)
- G7.19: Search semantic database (with conditions)

**Multiplayer Advanced (5 skills):**
- G7.01: Diagram client-server communication
- G7.02: Synchronize sprite movement
- G7.03: Broadcast multiplayer messages
- G7.04: Handle sprite collisions
- G7.05: Reset game world

**Leaderboard (3 skills):**
- G7.13: Record player score
- G7.14: Display game leaderboard
- G7.15: Manage leaderboard (hide/clear/remove)

**User Data (1 skill):**
- G7.16: Store and read user data

**Network Architecture (3 skills):**
- G7.20: Analyze network topologies
- G7.21: Client-server vs peer-to-peer
- G7.22: Analyze societal impacts

### G8 Current Skills (16 total)
All skills are architectural/conceptual analysis:
- G8.01: Edge vs cloud processing
- G8.02: Bandwidth and latency requirements
- G8.03: Security measures for cloud data
- G8.04: Data anonymization
- G8.05: Fallback strategies for failures
- G8.06: Cloud service monitoring dashboards
- G8.07: API request patterns
- G8.08: Data synchronization conflict resolution
- G8.09: Scalable data structures
- G8.10: Rate limiting and quota management
- G8.11: Cloud deployment regions
- G8.12: Event-driven cloud architectures
- G8.13: Cloud-first application architectures
- G8.14: Real-world cloud service trade-offs
- G8.15: Retry logic with exponential backoff
- G8.16: Debug multi-user scenarios

---

## Key Issues Identified

### 1. Grade Imbalance
- **G6 overload**: 25 skills (target: 12-15)
- **G7 overload**: 25 skills (target: 12-15)
- **G8 underutilized**: 16 skills (target: 15-18)

### 2. Missing Security/Privacy Skills
- **G3**: No explicit security/privacy skill
- **G5**: No explicit security/privacy skill
- **G7**: No explicit security/privacy skill (only privacy risks mentioned in G6.11)

### 3. Logical Progression Issues
- Google Sheets skills (9 total) too concentrated in G6
- Multiplayer basics split across G5/G6/G7 without clear progression
- Database skills (13) dominating G7
- Leaderboard separated from database when they're closely related

### 4. Tool-Focused vs Concept-Focused Balance
- Too many granular tool skills (individual blocks)
- Need more computational thinking: design, analyze, debug, predict

---

## Redistribution Strategy

### Goals
1. **Balance skill counts**: G5 (10→12), G6 (25→14), G7 (25→15), G8 (16→18)
2. **Add security/privacy**: G3, G5, G7 each get explicit security skills
3. **Improve progression**: Group related skills, create clearer learning paths
4. **Enhance CT focus**: Add design/analyze/debug/predict skills at all levels

---

## DETAILED REDISTRIBUTION PLAN

### GRADE 3 (Currently 5, Target: 6)

**ADD NEW:**
- **T30.G3.06** - Recognize when to keep passwords and personal info private in cloud apps
  - Description: Students identify scenarios where personal information should NOT be shared in cloud applications (entering passwords, full name, address, phone). They explain why keeping information private protects them online and practice identifying safe vs unsafe sharing situations in cloud contexts.
  - CSTA: E3-SAS-SC-02
  - Dependencies: T30.G2.03, T30.G3.04

**Result: 6 skills total** ✓

---

### GRADE 4 (Currently 6, Target: 6)

**NO CHANGES** - Already well-balanced

**Result: 6 skills total** ✓

---

### GRADE 5 (Currently 10, Target: 12)

**MOVE FROM G6 TO G5:**
- **T30.G6.21** → **T30.G5.10**: Read URL parameters using "read URL parameter" block
  - Rationale: Basic block usage, fits with G5's introduction to web concepts
  - Update dependencies to reference G3.02 (URLs)

**ADD NEW:**
- **T30.G5.11** - Identify security indicators when using cloud blocks (new)
  - Description: Students recognize security features in CreatiCode cloud blocks: password protection for games, public vs private data options, user authentication. They explain why each feature matters and choose appropriate security settings for different scenarios.
  - CSTA: MS-SAS-SC-09
  - Dependencies: T30.G5.04 (user identity), T30.G4.02 (HTTPS)

**Result: 12 skills total** ✓

---

### GRADE 6 (Currently 25, Target: 14)

**MOVE TO G5:**
- T30.G6.21 → T30.G5.10 (URL parameters)

**MOVE TO G7:**
- T30.G6.01 → T30.G7.00 (HTTP/HTTPS request tracing - becomes foundation for G7 architecture)
- T30.G6.10 → T30.G7.00.01 (Measure latency - becomes sub-skill of HTTP tracing)
- T30.G6.10.01 → T30.G7.00.02 (Loading indicators - UI response to latency)

**CONSOLIDATE Google Sheets skills:**
- **KEEP in G6 (Core CRUD - 5 skills):**
  - G6.02: Read from Google Sheet
  - G6.02.01: Debug Google Sheets connection
  - G6.03: Write to Google Sheet
  - G6.05: Read individual cell values
  - G6.06: Append rows

- **MOVE to G7 (Advanced manipulation - 4 skills):**
  - G6.04 → G7.05.01: Set individual cell values (advanced update)
  - G6.07 → G7.05.02: Manage sheets (list/add/remove)
  - G6.08 → G7.05.03: Clear sheet data
  - G6.09 → G7.05.04: Modify sheet structure (insert/remove rows/columns)

**KEEP in G6 (14 skills):**
1. G6.02: Read from Google Sheet
2. G6.02.01: Debug Google Sheets connection
3. G6.03: Write to Google Sheet
4. G6.05: Read individual cell values
5. G6.06: Append rows
6. G6.11: Classify data privacy risks (important G6 security skill)
7. G6.12: Add sprite to multiplayer game
8. G6.13: Remove sprite from game
9. G6.14: "when added to game" event
10. G6.15: List players in game
11. G6.16: Create cloud session
12. G6.17: Join cloud session
13. G6.18: Save cloud data (public/private)
14. G6.19: Load cloud data

**MOVE to G7:**
- G6.20 → G7.05.05: Access Google Drive folder contents (advanced integration)
- G6.22 → G7.24: Design cloud-connected UIs (design skill for G7)
- G6.23 → G7.25: Handle asynchronous responses (architectural understanding)

**Result: 14 skills total** ✓

---

### GRADE 7 (Currently 25, Target: 15)

**RECEIVE FROM G6:**
- G6.01 → **T30.G7.00**: Trace HTTP/HTTPS request steps (new G7 foundation)
- G6.10 → **T30.G7.00.01**: Measure and compare network latency effects
- G6.10.01 → **T30.G7.00.02**: Implement loading indicators for slow responses
- G6.04 → **T30.G7.05.01**: Set individual cell values in Google Sheet
- G6.07 → **T30.G7.05.02**: Manage Google Sheets structure
- G6.08 → **T30.G7.05.03**: Clear Google Sheet data
- G6.09 → **T30.G7.05.04**: Modify Google Sheet structure
- G6.20 → **T30.G7.05.05**: Access Google Drive folder contents
- G6.22 → **T30.G7.24**: Design cloud-connected UIs
- G6.23 → **T30.G7.25**: Handle asynchronous responses

**MOVE TO G8:**
- G7.06 → G8.17: Insert data into database collection (implementation detail)
- G7.08 → G8.18: Build query conditions (comparison)
- G7.09 → G8.19: Build query conditions (text/logical)
- G7.10 → G8.20: Update database records
- G7.11 → G8.21: Remove database documents
- G7.12 → G8.22: Use field/collection reporter blocks
- G7.17 → G8.23: Create semantic database
- G7.18 → G8.24: Search semantic database (basic)
- G7.19 → G8.25: Search semantic database (conditions)

**CONSOLIDATE Leaderboard into Database section (move to G8):**
- G7.13 → G8.26: Record player score
- G7.14 → G8.27: Display game leaderboard
- G7.15 → G8.28: Manage leaderboard

**ADD NEW SECURITY SKILL:**
- **T30.G7.26** - Implement access control for cloud data (new)
  - Description: Students design and implement access control mechanisms: who can read/write data, password protection for sessions, role-based permissions in multiplayer games. They create projects with different user roles (admin, player, viewer) and enforce appropriate permissions.
  - CSTA: MS-SAS-SC-09
  - Dependencies: G7.16 (user data), G6.18 (cloud data)

**KEEP in G7 (15 skills):**
1. **G7.00**: Trace HTTP/HTTPS request steps (from G6.01)
2. **G7.00.01**: Measure network latency (from G6.10)
3. **G7.00.02**: Implement loading indicators (from G6.10.01)
4. G7.01: Diagram client-server communication
5. G7.02: Synchronize sprite movement
6. G7.03: Broadcast multiplayer messages
7. G7.04: Handle sprite collisions
8. G7.05: Reset game world
9. **G7.05.01-05**: Google Sheets advanced (5 skills from G6)
10. G7.07: Query and retrieve from database collections (CONCEPT - keep)
11. G7.07.01: Debug database queries (CONCEPT - keep)
12. G7.09.01: Design efficient queries (CONCEPT - keep)
13. G7.11.01: Handle concurrent updates (CONCEPT - keep)
14. G7.16: Store and read user data
15. G7.20: Analyze network topologies
16. G7.21: Client-server vs peer-to-peer
17. G7.22: Analyze societal impacts
18. **G7.24**: Design cloud-connected UIs (from G6.22)
19. **G7.25**: Handle asynchronous responses (from G6.23)
20. **G7.26**: Implement access control for cloud data (NEW)

**Wait, that's 20 skills. Let me recount and consolidate further...**

**REVISED G7 (15 skills):**
1. **G7.00**: Trace HTTP/HTTPS request steps (from G6.01)
2. **G7.01**: Diagram client-server communication (KEEP)
3. **G7.02**: Synchronize sprite movement (KEEP)
4. **G7.03**: Broadcast multiplayer messages (KEEP)
5. **G7.04**: Handle sprite collisions (KEEP)
6. **G7.05**: Reset game world (KEEP)
7. **G7.06** (renumbered): Query and retrieve from database collections (KEEP - high-level concept)
8. **G7.07** (renumbered): Debug database queries (KEEP - CT skill)
9. **G7.08** (renumbered): Design efficient queries (KEEP - from G7.09.01)
10. **G7.09** (renumbered): Handle concurrent database updates (KEEP - from G7.11.01)
11. **G7.10** (renumbered): Store and read user data (KEEP - from G7.16)
12. **G7.11** (renumbered): Analyze network topologies (KEEP - from G7.20)
13. **G7.12** (renumbered): Client-server vs peer-to-peer (KEEP - from G7.21)
14. **G7.13** (renumbered): Analyze societal impacts of networked systems (KEEP - from G7.22)
15. **G7.14** (renumbered): Implement access control for cloud data (NEW security skill)

**MOVE to G8 (Advanced implementation skills):**
- G6.10 → G8.00.01: Measure network latency
- G6.10.01 → G8.00.02: Implement loading indicators
- G6.04, G6.07-09, G6.20 → G8 (Google Sheets advanced - 5 skills)
- G6.22 → G8: Design cloud-connected UIs
- G6.23 → G8: Handle asynchronous responses
- All detailed database blocks (G7.06, 08, 09, 10, 11, 12, 17, 18, 19) → G8 (9 skills)
- All leaderboard blocks (G7.13, 14, 15) → G8 (3 skills)

**Result: 15 skills total** ✓

---

### GRADE 8 (Currently 16, Target: 18-20)

**RECEIVE FROM G7 (Implementation-focused database & tool skills):**
- **G8.17**: Insert data into database collection (from G7.06)
- **G8.18**: Build query conditions with comparison operators (from G7.08)
- **G8.19**: Build query conditions with text search and logical operators (from G7.09)
- **G8.20**: Update database records (from G7.10)
- **G8.21**: Remove database documents (from G7.11)
- **G8.22**: Use field/collection reporter blocks (from G7.12)
- **G8.23**: Create semantic database (from G7.17)
- **G8.24**: Search semantic database (basic) (from G7.18)
- **G8.25**: Search semantic database with conditions (from G7.19)
- **G8.26**: Record player score to leaderboard (from G7.13)
- **G8.27**: Display game leaderboard (from G7.14)
- **G8.28**: Manage leaderboard (from G7.15)

**RECEIVE FROM G6 (Advanced tool manipulation):**
- **G8.29**: Measure and compare network latency effects (from G6.10)
- **G8.30**: Implement loading indicators (from G6.10.01)
- **G8.31**: Set individual cell values in Google Sheet (from G6.04)
- **G8.32**: Manage Google Sheets structure (list/add/remove) (from G6.07)
- **G8.33**: Clear Google Sheet data (from G6.08)
- **G8.34**: Modify Google Sheet structure (from G6.09)
- **G8.35**: Access Google Drive folder contents (from G6.20)
- **G8.36**: Design cloud-connected UIs (from G6.22)
- **G8.37**: Handle asynchronous responses (from G6.23)

**REORGANIZE G8 by themes:**

**Theme 1: Architecture & Design (5 skills - KEEP):**
- G8.01: Edge vs cloud processing pipelines
- G8.02: Bandwidth and latency requirements
- G8.11: Cloud deployment regions
- G8.12: Event-driven cloud architectures
- G8.13: Cloud-first application architectures

**Theme 2: Security & Privacy (2 skills - KEEP):**
- G8.03: Security measures for cloud data
- G8.04: Data anonymization

**Theme 3: Reliability & Performance (4 skills - KEEP):**
- G8.05: Fallback strategies for failures
- G8.07: API request patterns
- G8.10: Rate limiting and quota management
- G8.15: Retry logic with exponential backoff

**Theme 4: Advanced Debugging & Analysis (3 skills - KEEP):**
- G8.06: Cloud service monitoring dashboards
- G8.14: Real-world cloud service trade-offs
- G8.16: Debug multi-user scenarios

**Theme 5: Data Management (3 skills - KEEP):**
- G8.08: Data synchronization conflict resolution
- G8.09: Scalable data structures

**Theme 6: Database Implementation (9 skills - FROM G7):**
- G8.17: Insert data into database collection
- G8.18: Build query conditions (comparison)
- G8.19: Build query conditions (text/logical)
- G8.20: Update database records
- G8.21: Remove database documents
- G8.22: Use field/collection reporter blocks
- G8.23: Create semantic database
- G8.24: Search semantic database (basic)
- G8.25: Search semantic database (conditions)

**Theme 7: Leaderboard System (3 skills - FROM G7):**
- G8.26: Record player score
- G8.27: Display game leaderboard
- G8.28: Manage leaderboard

**Theme 8: Advanced Google Sheets (5 skills - FROM G6):**
- G8.31: Set individual cell values
- G8.32: Manage sheets structure
- G8.33: Clear sheet data
- G8.34: Modify sheet structure
- G8.35: Access Google Drive folder contents

**Theme 9: UI & UX Implementation (3 skills - FROM G6):**
- G8.29: Measure network latency
- G8.30: Implement loading indicators
- G8.36: Design cloud-connected UIs
- G8.37: Handle asynchronous responses

**Total G8: 16 (original) + 20 (from G6/G7) = 36 skills** ⚠️ **TOO MANY!**

**REVISED APPROACH - Keep G8 focused on ARCHITECTURE and CONCEPTS, not tools:**

---

## REVISED REDISTRIBUTION (Final)

### Core Principle
- **G5-G6**: Introduction to cloud BLOCKS (hands-on tool usage)
- **G7**: Integration and PATTERNS (combining blocks, conceptual understanding)
- **G8**: Architecture and SYSTEMS THINKING (design, analysis, trade-offs)

---

### GRADE 5: Introduction to Cloud Blocks (Target: 12 skills)

**CURRENT (10 skills):**
1. G5.01: Request-response cycle
2. G5.02: Evaluate when apps need internet
3. G5.03: Fetch web content
4. G5.04: User identity blocks
5. G5.05: Create multiplayer game
6. G5.06: Join multiplayer game
7. G5.07: List multiplayer games
8. G5.08: Check connection status
9. G5.09: Debug multiplayer connection

**ADD FROM G6:**
10. **G5.10**: Read URL parameters (from G6.21)

**ADD NEW:**
11. **G5.11**: Identify security indicators in cloud blocks (NEW - privacy/security for G5)
12. **G5.12**: Predict outcomes when cloud operations fail (NEW - CT skill)

**Result: 12 skills** ✓

---

### GRADE 6: Cloud Data & Collaboration Tools (Target: 14 skills)

**Google Sheets Core (5 skills):**
1. G6.01: Trace HTTP/HTTPS requests (moved from old G6.01)
2. G6.02: Read from Google Sheet
3. G6.03: Write to Google Sheet
4. G6.04: Read individual cell values
5. G6.05: Append rows to Google Sheet
6. G6.06: Debug Google Sheets connections (from old G6.02.01)

**Cloud Sessions (4 skills):**
7. G6.07: Create cloud session (from old G6.16)
8. G6.08: Join cloud session (from old G6.17)
9. G6.09: Save cloud data public/private (from old G6.18)
10. G6.10: Load cloud data (from old G6.19)

**Multiplayer Sprites (4 skills):**
11. G6.11: Add sprite to multiplayer game (from old G6.12)
12. G6.12: Remove sprite from game (from old G6.13)
13. G6.13: Use "when added to game" event (from old G6.14)
14. G6.14: List players in game (from old G6.15)

**MOVE to G7:**
- Old G6.11 (privacy risks) → G7 (better fit with security analysis)
- Old G6.04, 07, 08, 09, 20 (advanced Sheets) → G7
- Old G6.10, 10.01 (latency) → G7
- Old G6.22, 23 (UI/async) → G7

**Result: 14 skills** ✓

---

### GRADE 7: Integration & Patterns (Target: 16 skills)

**Network Analysis (3 skills):**
1. **G7.01**: Measure and compare network latency (from old G6.10)
2. **G7.02**: Analyze network topologies (from old G7.20)
3. **G7.03**: Client-server vs peer-to-peer architecture (from old G7.21)

**Multiplayer Patterns (5 skills):**
4. **G7.04**: Diagram client-server communication for multiplayer (from old G7.01)
5. **G7.05**: Synchronize sprite movement (from old G7.02)
6. **G7.06**: Broadcast multiplayer messages (from old G7.03)
7. **G7.07**: Handle sprite collisions (from old G7.04)
8. **G7.08**: Reset multiplayer game world (from old G7.05)

**Database Concepts (4 skills - high-level only):**
9. **G7.09**: Query and retrieve database data (from old G7.07 - concept only)
10. **G7.10**: Debug database queries (from old G7.07.01)
11. **G7.11**: Design efficient database queries (from old G7.09.01)
12. **G7.12**: Handle concurrent database updates (from old G7.11.01)

**Advanced Integration (4 skills):**
13. **G7.13**: Store and read user-specific data (from old G7.16)
14. **G7.14**: Classify data privacy risks when sharing cloud data (from old G6.11)
15. **G7.15**: Design cloud-connected user interfaces (from old G6.22)
16. **G7.16**: Analyze societal impacts of networked systems (from old G7.22)

**MOVE to G8 (all detailed implementation blocks):**
- All specific database operation blocks (insert, update, delete, query conditions, semantic search)
- All leaderboard blocks
- All advanced Google Sheets blocks
- Async response handling (old G6.23)

**Result: 16 skills** ✓

---

### GRADE 8: Architecture & Systems (Target: 20 skills)

**Architecture & Design (5 skills - EXISTING):**
1. G8.01: Edge vs cloud processing pipelines
2. G8.02: Bandwidth and latency requirements
3. G8.11: Cloud deployment regions
4. G8.12: Event-driven architectures
5. G8.13: Cloud-first application architectures

**Security & Privacy (3 skills):**
6. G8.03: Security measures for cloud data
7. G8.04: Data anonymization
8. **G8.17**: Implement access control patterns (NEW)

**Reliability & Performance (5 skills):**
9. G8.05: Fallback strategies for failures
10. G8.07: API request patterns
11. G8.10: Rate limiting and quota management
12. G8.15: Retry logic with exponential backoff
13. **G8.18**: Implement loading indicators and async response handling (from G6.10.01 + G6.23 combined)

**Advanced Data & Debugging (4 skills):**
14. G8.06: Cloud service monitoring dashboards
15. G8.08: Data synchronization conflict resolution
16. G8.09: Scalable data structures
17. G8.16: Debug multi-user scenarios

**Real-World Analysis (3 skills):**
18. G8.14: Real-world cloud service trade-offs
19. **G8.19**: Implement complete database CRUD operations (NEW - combines all G7 database blocks into one comprehensive skill)
20. **G8.20**: Build complete cloud application with multiple services (NEW - capstone integration project)

**ABSORBED from G7 (reconceptualized as high-level skills):**
- Database implementation details → consolidated into G8.19 (comprehensive CRUD)
- Leaderboard blocks → part of G8.19 (database applications)
- Google Sheets advanced → part of G8.20 (cloud application integration)
- Semantic database → part of G8.20 (advanced cloud services)

**Result: 20 skills** ✓

---

## NEW SKILLS TO ADD

### G3.06: Recognize when to keep information private in cloud apps
- **Category**: Security & Privacy
- **Description**: Students identify scenarios where personal information should NOT be shared in cloud applications (passwords, full address, phone). They explain why privacy matters in cloud contexts.
- **CSTA**: E3-SAS-SC-02
- **Dependencies**: T30.G2.03, T30.G3.04
- **Rationale**: Fills security gap in G3, age-appropriate privacy awareness

### G5.11: Identify security indicators in cloud blocks
- **Category**: Security & Privacy
- **Description**: Students recognize security features in CreatiCode cloud blocks: password protection for games, public vs private data options, user authentication. They choose appropriate settings for different scenarios.
- **CSTA**: MS-SAS-SC-09
- **Dependencies**: T30.G5.04, T30.G4.02
- **Rationale**: Fills security gap in G5, practical application of security concepts

### G5.12: Predict outcomes when cloud operations fail
- **Category**: Computational Thinking (Predict)
- **Description**: Students predict what happens when cloud operations fail (network timeout, server error, wrong credentials). They identify which operations will succeed/fail in different failure scenarios.
- **CSTA**: MS-SAS-HW-03
- **Dependencies**: T30.G5.03, T30.G5.08
- **Rationale**: Adds CT predict skill, builds resilience thinking

### G8.17: Implement access control patterns
- **Category**: Security & Privacy
- **Description**: Students design and implement access control: role-based permissions, password protection, public/private data separation. They create projects with different user roles (admin, player, viewer) and enforce permissions.
- **CSTA**: MS-SAS-SC-09
- **Dependencies**: T30.G8.03, T30.G7.13
- **Rationale**: Advanced security implementation for G8

### G8.18: Implement loading indicators and async response handling
- **Category**: UI/UX & Performance
- **Description**: Students build complete async handling systems: loading indicators during operations, success/error messages, preventing duplicate requests, maintaining responsive UI. They handle slow networks gracefully.
- **CSTA**: MS-SAS-NW-06
- **Dependencies**: T30.G8.07, T30.G7.01
- **Rationale**: Consolidates G6.10.01 + G6.23, comprehensive UX skill

### G8.19: Implement complete database CRUD operations
- **Category**: Database Systems (Comprehensive)
- **Description**: Students implement full database lifecycle: insert, query with complex conditions, update, delete. They build a complete application using database collections with proper error handling, efficient queries, and concurrent update management. Includes semantic search integration.
- **CSTA**: MS-SAS-NW-06
- **Dependencies**: T30.G7.09, T30.G7.10, T30.G7.11, T30.G7.12
- **Rationale**: Consolidates 12+ G7 database blocks into comprehensive implementation skill

### G8.20: Build complete cloud application with multiple services
- **Category**: Integration & Systems (Capstone)
- **Description**: Students design and build a complete cloud-connected application integrating multiple services: database for persistence, Google Sheets for data export, multiplayer for collaboration, user authentication, and leaderboard. They create architecture diagrams, implement all components, and handle errors gracefully.
- **CSTA**: MS-SAS-NW-06
- **Dependencies**: T30.G8.13, T30.G8.19, T30.G8.18
- **Rationale**: Capstone project bringing together all G8 skills, demonstrates mastery

---

## SKILLS TO CONSOLIDATE

### Consolidation 1: Database Implementation Skills (G7 → G8.19)
**Combine these G7 skills into ONE comprehensive G8 skill:**
- G7.06: Insert into database
- G7.08: Query conditions (comparison)
- G7.09: Query conditions (text/logical)
- G7.10: Update database records
- G7.11: Remove database documents
- G7.12: Field/collection reporter blocks
- G7.17: Create semantic database
- G7.18: Search semantic database (basic)
- G7.19: Search semantic database (conditions)

**New G8.19** teaches all these as integrated CRUD operations in one comprehensive skill.

### Consolidation 2: Leaderboard System (G7 → part of G8.19)
**Integrate these into G8.19 (database applications):**
- G7.13: Record player score
- G7.14: Display leaderboard
- G7.15: Manage leaderboard

**Rationale**: Leaderboards are database applications, teach together.

### Consolidation 3: Advanced Google Sheets (G6 → part of G8.20)
**Integrate these into G8.20 (cloud application):**
- G6.04: Set individual cell values
- G6.07: Manage sheets structure
- G6.08: Clear sheet data
- G6.09: Modify sheet structure
- G6.20: Google Drive folder contents

**Rationale**: Advanced Sheets features used in complete applications, not standalone.

### Consolidation 4: Async UX (G6 → G8.18)
**Combine these into ONE comprehensive UX skill:**
- G6.10.01: Implement loading indicators
- G6.23: Handle asynchronous responses

**Rationale**: These are two sides of same UX challenge - handling async operations.

---

## SKILLS TO SPLIT

### None Required
All current skills are appropriately granular. The issue was over-granularity at the block level, which is addressed through consolidation rather than splitting.

---

## FINAL SKILL COUNT SUMMARY

| Grade | Current | Target | Final | Change |
|-------|---------|--------|-------|--------|
| GK    | 4       | 4      | 4     | 0      |
| G1    | 4       | 4      | 4     | 0      |
| G2    | 5       | 5      | 5     | 0      |
| G3    | 5       | 6      | 6     | +1     |
| G4    | 6       | 6      | 6     | 0      |
| G5    | 10      | 12     | 12    | +2     |
| G6    | 25      | 14     | 14    | -11    |
| G7    | 25      | 16     | 16    | -9     |
| G8    | 16      | 20     | 20    | +4     |
| **Total** | **100** | **87** | **87** | **-13** |

**Note**: Total reduced by 13 skills through consolidation of redundant/overly-granular skills.

---

## DEPENDENCY UPDATES REQUIRED

### Skills Moved - Update Dependencies

**T30.G5.10** (from G6.21 - URL parameters):
- Update deps: T30.G5.01, T30.G3.02

**T30.G7.01** (from G6.10 - latency):
- Update deps: T30.G6.01 (HTTP), T30.G5.02

**T30.G7.14** (from G6.11 - privacy risks):
- Update deps: T30.G6.01, T30.G4.02

**T30.G7.15** (from G6.22 - cloud UIs):
- Update deps: T30.G7.01 (latency), T30.G5.08

**All G8 database skills** (from G7):
- Update deps to reference G7.09-G7.12 (concept skills)

---

## IMPLEMENTATION CHECKLIST

### Phase 1: Add New Skills
- [ ] Add T30.G3.06 (privacy awareness)
- [ ] Add T30.G5.11 (security indicators)
- [ ] Add T30.G5.12 (predict failures)
- [ ] Add T30.G8.17 (access control)
- [ ] Add T30.G8.18 (async UX - consolidation of G6.10.01 + G6.23)
- [ ] Add T30.G8.19 (comprehensive CRUD - consolidation of 12 G7 database skills)
- [ ] Add T30.G8.20 (capstone cloud application)

### Phase 2: Renumber/Reorganize G6
- [ ] G6.01: Keep HTTP/HTTPS trace
- [ ] G6.02: Keep Read Google Sheet
- [ ] G6.03: Keep Write Google Sheet
- [ ] G6.04: Keep Read cell values
- [ ] G6.05: Keep Append rows
- [ ] G6.06: Rename from G6.02.01 (Debug Sheets)
- [ ] G6.07: Rename from G6.16 (Create session)
- [ ] G6.08: Rename from G6.17 (Join session)
- [ ] G6.09: Rename from G6.18 (Save data)
- [ ] G6.10: Rename from G6.19 (Load data)
- [ ] G6.11: Rename from G6.12 (Add sprite)
- [ ] G6.12: Rename from G6.13 (Remove sprite)
- [ ] G6.13: Rename from G6.14 (When added event)
- [ ] G6.14: Rename from G6.15 (List players)

### Phase 3: Renumber/Reorganize G7
- [ ] G7.01: Rename from G6.10 (Measure latency)
- [ ] G7.02: Rename from G7.20 (Network topologies)
- [ ] G7.03: Rename from G7.21 (Client-server vs P2P)
- [ ] G7.04: Rename from G7.01 (Diagram multiplayer)
- [ ] G7.05: Keep from G7.02 (Sync movement)
- [ ] G7.06: Keep from G7.03 (Broadcast messages)
- [ ] G7.07: Keep from G7.04 (Sprite collisions)
- [ ] G7.08: Keep from G7.05 (Reset world)
- [ ] G7.09: Rename from G7.07 (Query database - concept)
- [ ] G7.10: Rename from G7.07.01 (Debug queries)
- [ ] G7.11: Rename from G7.09.01 (Efficient queries)
- [ ] G7.12: Rename from G7.11.01 (Concurrent updates)
- [ ] G7.13: Rename from G7.16 (User data)
- [ ] G7.14: Rename from G6.11 (Privacy risks)
- [ ] G7.15: Rename from G6.22 (Cloud UIs)
- [ ] G7.16: Rename from G7.22 (Societal impacts)

### Phase 4: Reorganize G8
- [ ] G8.01-16: Keep existing architecture skills
- [ ] G8.17: Add access control (NEW)
- [ ] G8.18: Add async UX (consolidation)
- [ ] G8.19: Add comprehensive CRUD (consolidation)
- [ ] G8.20: Add capstone project (NEW)

### Phase 5: Remove Consolidated Skills
- [ ] Remove old G6.04, 07, 08, 09, 10, 10.01, 20, 21, 22, 23
- [ ] Remove old G7.06, 08, 09, 10, 11, 12, 13, 14, 15, 17, 18, 19

### Phase 6: Update All Dependencies
- [ ] Update all skills that referenced moved skills
- [ ] Verify dependency chains are intact
- [ ] Check for circular dependencies

### Phase 7: Verification
- [ ] Verify skill counts match targets
- [ ] Verify progression makes sense K-8
- [ ] Verify all security/privacy gaps filled
- [ ] Verify CT focus improved
- [ ] Verify block coverage complete

---

## RATIONALE SUMMARY

### Why This Redistribution Works

1. **Balanced Progression**:
   - G5: Introduction to cloud blocks (hands-on)
   - G6: Core cloud tools (CRUD operations)
   - G7: Integration patterns (combining tools)
   - G8: Architecture & systems (design thinking)

2. **Security Coverage**:
   - G3: Privacy awareness (age-appropriate)
   - G5: Security features in tools (practical)
   - G7: Privacy risks analysis (evaluation)
   - G8: Access control implementation (advanced)

3. **Reduced Redundancy**:
   - 12 granular database blocks → 1 comprehensive CRUD skill
   - 5 advanced Sheets blocks → integrated into capstone
   - 2 async UX blocks → 1 comprehensive UX skill

4. **CT Focus Enhanced**:
   - G5.12: Predict (failure scenarios)
   - G7.10: Debug (database queries)
   - G7.11: Design (efficient queries)
   - G8.19: Implement (comprehensive systems)

5. **Realistic Skill Counts**:
   - G5-G6: 12-14 skills (appropriate for introduction)
   - G7: 16 skills (integration level)
   - G8: 20 skills (mastery + capstone)

---

## APPENDIX: Detailed Skill Mapping

### FROM G6 → G5
- G6.21 → G5.10 (URL parameters)

### FROM G6 → G7
- G6.01 → (stays G6.01 but recontextualized)
- G6.10 → G7.01 (latency measurement)
- G6.11 → G7.14 (privacy risks)
- G6.22 → G7.15 (cloud UIs)

### FROM G6 → G8 (via consolidation)
- G6.04, 07, 08, 09, 20 → G8.20 (capstone integration)
- G6.10.01, G6.23 → G8.18 (async UX)

### FROM G7 → G8
- G7.06, 08, 09, 10, 11, 12 → G8.19 (CRUD operations)
- G7.13, 14, 15 → G8.19 (leaderboard as database app)
- G7.17, 18, 19 → G8.19 (semantic search as advanced DB)

### REMOVED (consolidated)
- 23 skills consolidated into 4 comprehensive skills
- Net reduction: 19 skills

---

## NEXT STEPS

1. **Review this plan** with stakeholders
2. **Validate** CreatiCode block coverage against skill descriptions
3. **Implement Phase 1**: Add new skills with proper IDs
4. **Implement Phases 2-4**: Renumber existing skills
5. **Implement Phase 5**: Remove consolidated skills
6. **Implement Phase 6**: Update all dependencies
7. **Implement Phase 7**: Final verification

---

**Document Version**: 1.0
**Date**: 2025-11-29
**Status**: DRAFT - Awaiting Review
