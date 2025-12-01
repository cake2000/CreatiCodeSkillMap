# T30 Skill ID Mapping Table

## Quick Reference: Old ID → New ID

This table shows how existing T30 skills map to the new structure.

---

## GRADE 5 MAPPING

| Old ID | Old Skill Name | New ID | New Skill Name | Action |
|--------|----------------|--------|----------------|--------|
| T30.G5.01 | Request-response cycle | T30.G5.01 | Request-response cycle | KEEP |
| T30.G5.02 | Evaluate internet needs | T30.G5.02 | Evaluate internet needs | KEEP |
| T30.G5.03 | Fetch web content | T30.G5.03 | Fetch web content | KEEP |
| T30.G5.04 | User identity blocks | T30.G5.04 | User identity blocks | KEEP |
| T30.G5.05 | Create multiplayer game | T30.G5.05 | Create multiplayer game | KEEP |
| T30.G5.06 | Join multiplayer game | T30.G5.06 | Join multiplayer game | KEEP |
| T30.G5.07 | List multiplayer games | T30.G5.07 | List multiplayer games | KEEP |
| T30.G5.08 | Check connection status | T30.G5.08 | Check connection status | KEEP |
| T30.G5.09 | Debug multiplayer connection | T30.G5.09 | Debug multiplayer connection | KEEP |
| T30.G6.21 | Read URL parameters | **T30.G5.10** | Read URL parameters | **MOVED FROM G6** |
| - | - | **T30.G5.11** | Security indicators in cloud blocks | **NEW** |
| - | - | **T30.G5.12** | Predict cloud operation failures | **NEW** |

**G5 Total**: 10 → 12 skills (+2)

---

## GRADE 6 MAPPING

| Old ID | Old Skill Name | New ID | New Skill Name | Action |
|--------|----------------|--------|----------------|--------|
| T30.G6.01 | Trace HTTP/HTTPS request | T30.G6.01 | Trace HTTP/HTTPS request | KEEP (recontextualized) |
| T30.G6.02 | Read from Google Sheet | T30.G6.02 | Read from Google Sheet | KEEP |
| T30.G6.03 | Write to Google Sheet | T30.G6.03 | Write to Google Sheet | KEEP |
| T30.G6.05 | Read individual cell values | T30.G6.04 | Read individual cell values | RENUMBER |
| T30.G6.06 | Append rows | T30.G6.05 | Append rows | RENUMBER |
| T30.G6.02.01 | Debug Sheets connection | T30.G6.06 | Debug Sheets connection | RENUMBER |
| T30.G6.16 | Create cloud session | T30.G6.07 | Create cloud session | RENUMBER |
| T30.G6.17 | Join cloud session | T30.G6.08 | Join cloud session | RENUMBER |
| T30.G6.18 | Save cloud data | T30.G6.09 | Save cloud data (public/private) | RENUMBER |
| T30.G6.19 | Load cloud data | T30.G6.10 | Load cloud data | RENUMBER |
| T30.G6.12 | Add sprite to game | T30.G6.11 | Add sprite to game | RENUMBER |
| T30.G6.13 | Remove sprite from game | T30.G6.12 | Remove sprite from game | RENUMBER |
| T30.G6.14 | "when added to game" event | T30.G6.13 | "when added to game" event | RENUMBER |
| T30.G6.15 | List players in game | T30.G6.14 | List players in game | RENUMBER |

### G6 Skills REMOVED (moved to other grades)

| Old ID | Old Skill Name | New Location | Reason |
|--------|----------------|--------------|--------|
| T30.G6.04 | Set individual cell values | → G8.20 (capstone) | Advanced Sheets integration |
| T30.G6.07 | Manage sheets structure | → G8.20 (capstone) | Advanced Sheets integration |
| T30.G6.08 | Clear sheet data | → G8.20 (capstone) | Advanced Sheets integration |
| T30.G6.09 | Modify sheet structure | → G8.20 (capstone) | Advanced Sheets integration |
| T30.G6.10 | Measure network latency | → T30.G7.01 | Network analysis skill |
| T30.G6.10.01 | Implement loading indicators | → T30.G8.18 | Consolidated into async UX |
| T30.G6.11 | Classify privacy risks | → T30.G7.14 | Privacy analysis for G7 |
| T30.G6.20 | Google Drive folder access | → G8.20 (capstone) | Advanced integration |
| T30.G6.21 | Read URL parameters | → T30.G5.10 | Basic block usage for G5 |
| T30.G6.22 | Design cloud-connected UIs | → T30.G7.15 | Design skill for G7 |
| T30.G6.23 | Handle async responses | → T30.G8.18 | Consolidated into async UX |

**G6 Total**: 25 → 14 skills (-11)

---

## GRADE 7 MAPPING

| Old ID | Old Skill Name | New ID | New Skill Name | Action |
|--------|----------------|--------|----------------|--------|
| T30.G6.10 | Measure network latency | **T30.G7.01** | Measure and compare network latency | **FROM G6** |
| T30.G7.20 | Analyze network topologies | T30.G7.02 | Analyze network topologies | RENUMBER |
| T30.G7.21 | Client-server vs P2P | T30.G7.03 | Client-server vs peer-to-peer | RENUMBER |
| T30.G7.01 | Diagram multiplayer communication | T30.G7.04 | Diagram client-server multiplayer | RENUMBER |
| T30.G7.02 | Synchronize sprite movement | T30.G7.05 | Synchronize sprite movement | RENUMBER |
| T30.G7.03 | Broadcast multiplayer messages | T30.G7.06 | Broadcast multiplayer messages | RENUMBER |
| T30.G7.04 | Handle sprite collisions | T30.G7.07 | Handle sprite collisions | RENUMBER |
| T30.G7.05 | Reset game world | T30.G7.08 | Reset multiplayer game world | RENUMBER |
| T30.G7.07 | Query database collections | T30.G7.09 | Query and retrieve database data | RENUMBER (concept only) |
| T30.G7.07.01 | Debug database queries | T30.G7.10 | Debug database queries | RENUMBER |
| T30.G7.09.01 | Design efficient queries | T30.G7.11 | Design efficient database queries | RENUMBER |
| T30.G7.11.01 | Handle concurrent updates | T30.G7.12 | Handle concurrent database updates | RENUMBER |
| T30.G7.16 | Store/read user data | T30.G7.13 | Store and read user-specific data | RENUMBER |
| T30.G6.11 | Classify privacy risks | **T30.G7.14** | Classify data privacy risks | **FROM G6** |
| T30.G6.22 | Design cloud UIs | **T30.G7.15** | Design cloud-connected UIs | **FROM G6** |
| T30.G7.22 | Analyze societal impacts | T30.G7.16 | Analyze societal impacts of networks | RENUMBER |

### G7 Skills REMOVED (moved to G8)

| Old ID | Old Skill Name | New Location | Reason |
|--------|----------------|--------------|--------|
| T30.G7.06 | Insert into database collection | → T30.G8.19 | Consolidated into comprehensive CRUD |
| T30.G7.08 | Query conditions (comparison) | → T30.G8.19 | Consolidated into comprehensive CRUD |
| T30.G7.09 | Query conditions (text/logical) | → T30.G8.19 | Consolidated into comprehensive CRUD |
| T30.G7.10 | Update database records | → T30.G8.19 | Consolidated into comprehensive CRUD |
| T30.G7.11 | Remove database documents | → T30.G8.19 | Consolidated into comprehensive CRUD |
| T30.G7.12 | Field/collection reporters | → T30.G8.19 | Consolidated into comprehensive CRUD |
| T30.G7.13 | Record player score | → T30.G8.19 | Leaderboard as database application |
| T30.G7.14 | Display game leaderboard | → T30.G8.19 | Leaderboard as database application |
| T30.G7.15 | Manage leaderboard | → T30.G8.19 | Leaderboard as database application |
| T30.G7.17 | Create semantic database | → T30.G8.19 | Consolidated into comprehensive CRUD |
| T30.G7.18 | Search semantic database (basic) | → T30.G8.19 | Consolidated into comprehensive CRUD |
| T30.G7.19 | Search semantic database (conditions) | → T30.G8.19 | Consolidated into comprehensive CRUD |

**G7 Total**: 25 → 16 skills (-9)

---

## GRADE 8 MAPPING

| Old ID | Old Skill Name | New ID | New Skill Name | Action |
|--------|----------------|--------|----------------|--------|
| T30.G8.01 | Edge vs cloud processing | T30.G8.01 | Edge vs cloud processing pipelines | KEEP |
| T30.G8.02 | Bandwidth and latency | T30.G8.02 | Bandwidth and latency requirements | KEEP |
| T30.G8.03 | Security measures | T30.G8.03 | Security measures for cloud data | KEEP |
| T30.G8.04 | Data anonymization | T30.G8.04 | Data anonymization implementation | KEEP |
| T30.G8.05 | Fallback strategies | T30.G8.05 | Fallback strategies for failures | KEEP |
| T30.G8.06 | Monitoring dashboards | T30.G8.06 | Cloud service monitoring dashboards | KEEP |
| T30.G8.07 | API request patterns | T30.G8.07 | API request patterns for efficiency | KEEP |
| T30.G8.08 | Conflict resolution | T30.G8.08 | Data synchronization conflict resolution | KEEP |
| T30.G8.09 | Scalable data structures | T30.G8.09 | Scalable data structures for cloud | KEEP |
| T30.G8.10 | Rate limiting | T30.G8.10 | Rate limiting and quota management | KEEP |
| T30.G8.11 | Cloud deployment regions | T30.G8.11 | Cloud deployment regions trade-offs | KEEP |
| T30.G8.12 | Event-driven architectures | T30.G8.12 | Event-driven cloud architectures | KEEP |
| T30.G8.13 | Cloud-first applications | T30.G8.13 | Cloud-first application architectures | KEEP |
| T30.G8.14 | Real-world trade-offs | T30.G8.14 | Real-world cloud service trade-offs | KEEP |
| T30.G8.15 | Retry logic | T30.G8.15 | Retry logic with exponential backoff | KEEP |
| T30.G8.16 | Debug multi-user scenarios | T30.G8.16 | Debug complex multi-user scenarios | KEEP |
| - | - | **T30.G8.17** | Implement access control patterns | **NEW** |
| - | - | **T30.G8.18** | Async UX implementation | **NEW (consolidation)** |
| - | - | **T30.G8.19** | Comprehensive database CRUD | **NEW (consolidation)** |
| - | - | **T30.G8.20** | Cloud application capstone | **NEW (consolidation)** |

**G8 Total**: 16 → 20 skills (+4)

---

## CONSOLIDATION MAPPING

### Consolidation 1: Database CRUD Operations
**Multiple old skills → T30.G8.19**

| Old ID | Old Skill | Integrated Into |
|--------|-----------|-----------------|
| T30.G7.06 | Insert data into collection | T30.G8.19 |
| T30.G7.08 | Query conditions (comparison) | T30.G8.19 |
| T30.G7.09 | Query conditions (text/logical) | T30.G8.19 |
| T30.G7.10 | Update database records | T30.G8.19 |
| T30.G7.11 | Remove database documents | T30.G8.19 |
| T30.G7.12 | Field/collection reporter blocks | T30.G8.19 |
| T30.G7.17 | Create semantic database | T30.G8.19 |
| T30.G7.18 | Search semantic database (basic) | T30.G8.19 |
| T30.G7.19 | Search semantic database (conditions) | T30.G8.19 |
| T30.G7.13 | Record player score | T30.G8.19 |
| T30.G7.14 | Display game leaderboard | T30.G8.19 |
| T30.G7.15 | Manage leaderboard | T30.G8.19 |

**Total**: 12 skills → 1 comprehensive skill

### Consolidation 2: Async UX Implementation
**Multiple old skills → T30.G8.18**

| Old ID | Old Skill | Integrated Into |
|--------|-----------|-----------------|
| T30.G6.10.01 | Implement loading indicators | T30.G8.18 |
| T30.G6.23 | Handle asynchronous responses | T30.G8.18 |

**Total**: 2 skills → 1 comprehensive skill

### Consolidation 3: Cloud Application Capstone
**Multiple old skills → T30.G8.20**

| Old ID | Old Skill | Integrated Into |
|--------|-----------|-----------------|
| T30.G6.04 | Set individual cell values | T30.G8.20 |
| T30.G6.07 | Manage sheets structure | T30.G8.20 |
| T30.G6.08 | Clear sheet data | T30.G8.20 |
| T30.G6.09 | Modify sheet structure | T30.G8.20 |
| T30.G6.20 | Google Drive folder access | T30.G8.20 |

**Total**: 5 skills → integrated into capstone project

---

## NEW SKILLS DETAIL

### T30.G5.11: Security Indicators in Cloud Blocks
- **Type**: NEW
- **Category**: Security & Privacy
- **Description**: Recognize security features in CreatiCode cloud blocks (passwords, public/private data, authentication)
- **Dependencies**: T30.G5.04, T30.G4.02
- **CSTA**: MS-SAS-SC-09

### T30.G5.12: Predict Cloud Operation Failures
- **Type**: NEW
- **Category**: Computational Thinking (Predict)
- **Description**: Predict what happens when cloud operations fail (timeouts, errors, wrong credentials)
- **Dependencies**: T30.G5.03, T30.G5.08
- **CSTA**: MS-SAS-HW-03

### T30.G8.17: Implement Access Control Patterns
- **Type**: NEW
- **Category**: Security & Privacy
- **Description**: Design and implement access control (role-based permissions, password protection)
- **Dependencies**: T30.G8.03, T30.G7.13
- **CSTA**: MS-SAS-SC-09

### T30.G8.18: Async UX Implementation
- **Type**: CONSOLIDATION (G6.10.01 + G6.23)
- **Category**: UI/UX & Performance
- **Description**: Complete async handling: loading indicators, error messages, responsive UI during network ops
- **Dependencies**: T30.G8.07, T30.G7.01
- **CSTA**: MS-SAS-NW-06

### T30.G8.19: Comprehensive Database CRUD
- **Type**: CONSOLIDATION (12 G7 database skills)
- **Category**: Database Systems
- **Description**: Full database lifecycle: insert, query (complex conditions), update, delete, error handling, semantic search
- **Dependencies**: T30.G7.09, T30.G7.10, T30.G7.11, T30.G7.12
- **CSTA**: MS-SAS-NW-06

### T30.G8.20: Cloud Application Capstone
- **Type**: CONSOLIDATION (5 G6 advanced features) + NEW (integration project)
- **Category**: Systems Integration
- **Description**: Complete cloud app integrating database, Sheets, multiplayer, authentication, leaderboard
- **Dependencies**: T30.G8.13, T30.G8.19, T30.G8.18
- **CSTA**: MS-SAS-NW-06

---

## DEPENDENCY UPDATES REQUIRED

### Skills with Updated Dependencies

| Skill ID | Old Dependencies | New Dependencies | Reason |
|----------|------------------|------------------|--------|
| T30.G5.10 | (none in G6.21) | T30.G5.01, T30.G3.02 | Moved from G6 to G5 |
| T30.G7.01 | T30.G6.01, T30.G5.01 | T30.G6.01, T30.G5.02 | Moved from G6 to G7 |
| T30.G7.14 | T30.G6.01, T30.G4.02 | T30.G6.01, T30.G4.02 | Moved from G6 to G7 |
| T30.G7.15 | T30.G6.10.01, T30.G5.08 | T30.G7.01, T30.G5.08 | Moved from G6 to G7, G6.10.01→G7.01 |

### Skills Referencing Removed Skills

Any skill that referenced these OLD IDs must be updated:
- T30.G6.04, G6.07, G6.08, G6.09, G6.10, G6.10.01, G6.11, G6.20, G6.21, G6.22, G6.23
- T30.G7.06, G7.08, G7.09, G7.10, G7.11, G7.12, G7.13, G7.14, G7.15, G7.17, G7.18, G7.19

**Action**: Search entire curriculum for references to these IDs and update to new IDs.

---

## IMPLEMENTATION CHECKLIST

### Step 1: Backup Current Data
- [ ] Create backup of allskills.md
- [ ] Save copy of current T30 section separately
- [ ] Document current state

### Step 2: Add New Skills
- [ ] Add T30.G3.06 (privacy awareness)
- [ ] Add T30.G5.11 (security indicators)
- [ ] Add T30.G5.12 (predict failures)
- [ ] Add T30.G8.17 (access control)
- [ ] Add T30.G8.18 (async UX)
- [ ] Add T30.G8.19 (comprehensive CRUD)
- [ ] Add T30.G8.20 (capstone)

### Step 3: Renumber G5
- [ ] Add G5.10 from G6.21
- [ ] Verify G5.01-G5.12 complete

### Step 4: Renumber G6
- [ ] Reorganize to G6.01-G6.14
- [ ] Remove old G6.04, 07-11, 20-23
- [ ] Update skill descriptions

### Step 5: Renumber G7
- [ ] Reorganize to G7.01-G7.16
- [ ] Remove old G7.06, 08-15, 17-19
- [ ] Add skills from G6 (G6.10, G6.11, G6.22)
- [ ] Update skill descriptions

### Step 6: Update G8
- [ ] Keep G8.01-G8.16
- [ ] Add G8.17-G8.20
- [ ] Update descriptions to reference G7 concepts

### Step 7: Update Dependencies
- [ ] Update T30.G5.10 dependencies
- [ ] Update all G7 dependencies (skills moved from G6)
- [ ] Update all G8 dependencies (skills moved from G7)
- [ ] Search curriculum for broken references

### Step 8: Verification
- [ ] Verify skill counts: G5=12, G6=14, G7=16, G8=20
- [ ] Verify no duplicate skill IDs
- [ ] Verify all dependencies valid
- [ ] Verify progression makes sense
- [ ] Verify all CreatiCode blocks covered

---

**Document**: T30 Skill Mapping Table
**Version**: 1.0
**Date**: 2025-11-29
**Purpose**: Quick reference for implementing skill redistribution
