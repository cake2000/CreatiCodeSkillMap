# T33 Connected Services - Fix Implementation Checklist

**Priority-Ordered Action Items**

---

## 🔴 CRITICAL PRIORITY (Do First)

### Issue #1: Missing Cloud Database Category
- [ ] **Write T33.G6.XX** - Introduction to cloud collections
  - Blocks: database_collection, database_find_from_collection (basic)
  - Create collection, insert documents, find all documents
  - Dependencies: T08.G4.01, T10.G5.01, T31.G5.01, T33.G6.01

- [ ] **Write T33.G7.XX** - Query collections with conditions
  - Blocks: database_query, database_operator, database_collectionfield
  - WHERE clauses, comparison operators, field references
  - Dependencies: T08.G5.01, T33.G6.XX (collections intro)

- [ ] **Write T33.G7.YY** - Update and delete documents
  - Blocks: database_update_collection, database_remove_all_document
  - Modify existing documents, delete by condition
  - Dependencies: T08.G5.01, T33.G7.XX (queries)

- [ ] **Write T33.G8.XX** - Advanced query logic
  - Blocks: database_and, database_or, database_not, database_contains
  - Complex conditions, boolean logic, text searching
  - Dependencies: T08.G6.01, T33.G7.XX, T33.G7.YY

- [ ] **Write T33.G8.YY** - Collection design and optimization
  - Blocks: database_update_collection_in_place
  - Schema planning, efficient queries, data modeling
  - Dependencies: T09.G6.01, T33.G8.XX

### Issue #2: Cloud Sessions vs Multiplayer Confusion
- [ ] **Rewrite T33.G5.02** - Cloud variables vs local variables
  - Change from "real-time apps" to cloud variable concepts
  - Remove multiplayer game references
  - Add explicit contrast with local variables
  - Keep dependency on T33.G5.01

- [ ] **Rewrite T33.G7.05** - Cloud sessions for variable sync
  - Emphasize "VARIABLES ONLY" throughout
  - Remove "multiplayer experiences" language
  - Add "not sprites, not physics, not game logic" clarifications
  - Strengthen note distinguishing from T19 Multiplayer
  - Keep blocks: data_createcloudsession, data_joincloudsession

### Issue #3: Missing URL-Based Media Loading
- [ ] **Write T33.G6.XX** - Load media from URLs
  - Loading images from URLs as costumes/backdrops
  - Loading sounds from URLs as audio clips
  - URL requirements (public, format compatibility)
  - Error handling for failed loads
  - Dependencies: T31.G5.01, T33.G6.01

---

## 🟠 HIGH PRIORITY (Do Second)

### Issue #4: T33.G6.01 Too Broad
- [ ] **Rewrite T33.G6.01** - Narrow to Cloud category only
  - Remove AI blocks references (keep in note only)
  - Remove Multiplayer references (keep in note only)
  - Add database operations to list
  - Simplify data flow categorization
  - Keep dependencies: T08.G4.01, T09.G4.04, T31.G5.01, T33.G5.01

### Issue #5: Privacy Skill Too Late
- [ ] **Write T33.G5.03** (NEW) - Privacy in shared online data
  - Understand URLs = access for anyone
  - Create safe test datasets
  - Identify data never to share online
  - Broad scope (applies to all cloud services)
  - Dependencies: T31.G5.01, T33.G5.01

- [ ] **Update T33.G6.08** - Apply privacy to Google Sheets
  - Add dependency on T33.G5.03
  - Focus on Google Sheets-specific practices
  - Remove redundant general privacy content (now in G5.03)
  - Keep specific practices (test data, sheet permissions)

### Issue #6: "Tool Wrappers" Terminology
- [ ] **Rename topic title** throughout allskills.md
  - Find: "T33 – Connected Services & Tool Wrappers"
  - Replace: "T33 – Connected Services"
  - Update all 30 skills (K-8)

### Issue #7: Cell Operations Missing Context
- [ ] **Update T33.G7.02** - Add tradeoff analysis
  - Explain when to use cell operations vs bulk operations
  - Add performance considerations
  - Provide concrete examples (high score vs leaderboard)
  - Keep blocks: p2p_getvalue, p2p_setvalue

### Issue #8: Multi-Service Workflow Gap
- [ ] **Write T33.G7.06A** (NEW) - Chain two services
  - Insert before current G7.07 (which becomes G7.08)
  - 2-step workflows only (fetch → display, sheets → save)
  - Intermediate variable storage
  - Sequential execution (wait for step 1)
  - Dependencies: T08.G5.01, T09.G5.01, T31.G5.01, T33.G6.02, T33.G6.04, T33.G6.06

- [ ] **Update T33.G7.07** → Renumber to **T33.G7.08**
  - Add dependency on new T33.G7.06A
  - Update to focus on 3+ step workflows (not 2-step)
  - Keep multi-service orchestration content

- [ ] **Renumber subsequent G7 skills:**
  - Current G7.08 → G7.09
  - Current G7.09 → G7.10

### Issue #9: G8 Skills Too Technical
- [ ] **Simplify T33.G8.03** - Service failure fallbacks
  - Remove "simulate outages" (just test with invalid inputs)
  - Remove "incident response procedures"
  - Focus on Plan B behaviors (show sample data, retry button)
  - Age-appropriate activities

- [ ] **Simplify T33.G8.04** - Data validation
  - Remove "logging validation failures"
  - Remove "sanitize" terminology
  - Focus on basic checks (empty? expected columns?)
  - Simple error messages

- [ ] **Simplify T33.G8.05** - Service vs local comparison
  - Remove "measure and compare" (no profiling tools)
  - Focus on qualitative comparison (works offline? updatable?)
  - Remove "decision framework" (just explain tradeoffs)

### Issue #10: G8.02 Legal Analysis Vague
- [ ] **Rewrite T33.G8.02** - Service usage policies
  - Specify where students get policy info (teacher/knowledge base)
  - Concrete activities (create checklist, count API calls)
  - Focus on actionable rules (rate limits, content filters)
  - Add teacher note about providing simplified policies

### Issue #11: Google Drive Read-Only Unclear
- [ ] **Update T33.G7.04** - Clarify read-only access
  - Add "read-only" to title and description
  - Explain what CAN'T be done (download, modify, delete)
  - Explain what CAN be done (see files, get URLs)
  - Use cases for file URLs with other blocks
  - Keep block: p2p_getgooglefoldercontent

---

## 🟡 MEDIUM PRIORITY (Do Third)

### Issue #12: Missing Table Practice Before DB
- [ ] **Write T33.G6.XX** - Cloud service results in tables
  - Store multiple fetch results in table
  - Combine data from multiple sheets
  - Practice table operations with cloud data
  - Dependencies: T10.G5.01, T33.G6.02, T33.G6.03

### Issue #13: G7.06 Authorization Unclear
- [ ] **Decision:** Revise or remove T33.G7.06
  - **Option A:** Remove (consolidate into G6.08)
  - **Option B:** Refocus on authorization model (how CreatiCode handles auth)
  - **Choose option and implement**

### Issue #14: G7.08 Service Comparison Vague
- [ ] **Update T33.G7.08** (renumbered from G7.07) - Add decision framework
  - Provide specific comparison criteria
  - Add service strengths/limitations table
  - Concrete examples of when to use each service
  - Clear justification format

### Issue #15: Web Fetch Result Processing Missing
- [ ] **Update T33.G6.02** - Expand to cover display/parsing
  - Add how to display markdown content
  - Add basic string extraction (substring, find)
  - Explain markdown rendering (or lack thereof)
  - Add note about using string operators

### Issue #16: G7.09 Caching Too Advanced
- [ ] **Simplify T33.G7.09** - Remove timestamp complexity
  - Remove "cache expiration by timestamps"
  - Remove time calculations
  - Keep basic lookup-before-call pattern
  - Add manual cache clear button
  - Add note about advanced caching as extension

### Issue #17: G6.05 Sheet Clearing Weak
- [ ] **Update T33.G6.05** - Remove premature delete comparison
  - Remove "vs deleting" (students haven't learned delete yet)
  - Focus on clearing use cases (reset features)
  - Explain what clearing does vs doesn't do
  - Keep block: p2p_clearsheet

### Issue #18: Missing Quota Explanation
- [ ] **Write T33.G5.04** (NEW) - Why services have limits
  - Services cost money (servers, processing, storage)
  - Free tiers have quotas
  - Exceeding quotas = blocked or payment
  - Shared quotas affect all users
  - Dependencies: T31.G5.01, T33.G5.01

- [ ] **Update T33.G6.07** - Add dependency on T33.G5.04
  - Reference quota concept from G5.04
  - Focus on implementation (counters, cooldowns)
  - Add quota status feedback examples

---

## 🔵 DEPENDENCY FIXES (Do Fourth)

### Issue #23: Missing Table Dependencies
- [ ] **Update T33.G6.03** - Add T10.G5.01 dependency
  - Reading sheets requires table understanding
  - Add: T10.G5.01 (Understand table structure)

- [ ] **Update T33.G6.04** - Add T10.G5.01 dependency
  - Writing tables requires table understanding
  - Add: T10.G5.01 (Understand table structure)

### Issue #24: Missing Variable Tracing
- [ ] **Update T33.G6.06** - Add T09.G4.04 dependency
  - Error handling requires variable state understanding
  - Add: T09.G4.04 (Trace code with variables)

- [ ] **Update T33.G6.07** - Add T09.G4.04 dependency
  - Rate limiting counters require variable understanding
  - Add: T09.G4.04 (Trace code with variables)

### Issue #21: G8.06 Missing Dependencies
- [ ] **Update T33.G8.06** - Add cloud database and sessions
  - Add dependency on cloud database skills (when added)
  - Add dependency on T33.G7.05 (cloud sessions)
  - Update description to include database and sessions in pipeline
  - Make this a true comprehensive cloud integration capstone

### Issue #25: G7.09 Missing Lookup Dependency
- [ ] **Check T10 for lookup/search skills**
  - If exists: Add to T33.G7.09 dependencies
  - If not exists: Consider adding to T10 or teaching inline in G7.09

---

## 📋 VALIDATION CHECKS

After all fixes are complete:

- [ ] **Block Coverage Validation**
  - [ ] All 13 Google Sheets blocks mapped? (p2p_*)
  - [ ] All 13 Database blocks mapped? (database_*)
  - [ ] Cloud Sessions blocks mapped? (data_createcloudsession, data_joincloudsession)
  - [ ] Web fetch block mapped? (p2p_fetchfromurl)
  - [ ] Google Drive block mapped? (p2p_getgooglefoldercontent)
  - [ ] URL media loading blocks mapped? (verify if separate blocks exist)

- [ ] **Dependency Validation**
  - [ ] No circular dependencies within T33
  - [ ] All X-2 rule compliant (max 2 grades back)
  - [ ] Same-grade dependencies documented with sequence
  - [ ] All T10 table skills as prerequisites where needed
  - [ ] All T09 variable skills as prerequisites where needed
  - [ ] All T31 networking skills as prerequisites where needed

- [ ] **Progression Validation**
  - [ ] K-2: Conceptual only (no blocks) ✓
  - [ ] G3-5: Conceptual transitions to concrete
  - [ ] G6: Individual service blocks introduced
  - [ ] G7: Multi-service workflows
  - [ ] G8: Advanced techniques and capstone
  - [ ] Privacy before data sharing (G5.03 before G6.03)
  - [ ] Quotas before rate limiting (G5.04 before G6.07)

- [ ] **Age Appropriateness**
  - [ ] K-2 use familiar apps and simple language ✓
  - [ ] G3-5 connect concepts to student experiences
  - [ ] G6-8 balance technical accuracy with accessibility
  - [ ] No professional engineering terminology (DevOps, SRE, etc.)
  - [ ] Activities match cognitive development stage

- [ ] **Clarity & Completeness**
  - [ ] All skill descriptions actionable
  - [ ] All block references correct
  - [ ] All dependencies listed
  - [ ] All notes/warnings included
  - [ ] Topic title consistent throughout

---

## 📊 PROGRESS TRACKING

### Skills to Add (10 total):
- [ ] T33.G5.03 - Privacy foundation
- [ ] T33.G5.04 - Service quotas
- [ ] T33.G6.XX - URL media loading
- [ ] T33.G6.YY - Cloud results in tables
- [ ] T33.G6.ZZ - Database intro
- [ ] T33.G7.06A - 2-service workflows
- [ ] T33.G7.XX - Database queries
- [ ] T33.G7.YY - Database update/delete
- [ ] T33.G8.XX - Advanced database queries
- [ ] T33.G8.YY - Database design

### Skills to Rewrite (13 total):
- [ ] T33.G5.02 - Cloud variables
- [ ] T33.G6.01 - Cloud blocks intro
- [ ] T33.G6.02 - Web fetch
- [ ] T33.G6.05 - Clear sheets
- [ ] T33.G6.08 - Privacy practices
- [ ] T33.G7.02 - Cell operations
- [ ] T33.G7.04 - Google Drive
- [ ] T33.G7.05 - Cloud sessions
- [ ] T33.G7.06 - Authorization
- [ ] T33.G7.08 - Service comparison (renumbered)
- [ ] T33.G8.02 - Usage policies
- [ ] T33.G8.03 - Fallbacks
- [ ] T33.G8.04 - Validation
- [ ] T33.G8.05 - Service vs local

### Skills to Update (8 dependencies):
- [ ] T33.G6.03 - Add table dependency
- [ ] T33.G6.04 - Add table dependency
- [ ] T33.G6.06 - Add variable dependency
- [ ] T33.G6.07 - Add quota dependency
- [ ] T33.G7.09 - Simplify and check lookup dependency
- [ ] T33.G8.06 - Add database and session dependencies

### Skills to Renumber (3 total):
- [ ] T33.G7.07 → T33.G7.08
- [ ] T33.G7.08 → T33.G7.09
- [ ] T33.G7.09 → T33.G7.10

### Global Changes (1 total):
- [ ] Rename topic title (all 30 skills)

---

## ESTIMATED EFFORT

| Phase | Tasks | Est. Hours | Priority |
|-------|-------|-----------|----------|
| Phase 1: Critical (Database, Sessions, Privacy) | 10 skills | 12-15 hrs | 🔴 Critical |
| Phase 2: High Priority (Simplify, Clarify) | 13 skills | 8-10 hrs | 🟠 High |
| Phase 3: Medium Priority (Enhancements) | 8 skills | 5-6 hrs | 🟡 Medium |
| Phase 4: Dependencies & Validation | 8 updates + checks | 3-4 hrs | 🔵 Low |
| **TOTAL** | **39 items** | **28-35 hrs** | — |

---

## COMPLETION CRITERIA

✅ **Analysis Complete** when:
- All 26 issues documented
- All recommendations provided
- All affected skills identified

✅ **Implementation Complete** when:
- All new skills written (10)
- All skills rewritten (13)
- All dependencies updated (8)
- All skills renumbered (3)
- Topic title updated (30 skills)
- All blocks mapped to skills (30+ blocks)

✅ **Validation Complete** when:
- 100% block coverage confirmed
- All dependencies verified
- Progression validated
- Age appropriateness checked
- No circular dependencies
- Documentation updated

---

**Next Action:** Begin Phase 1 - Write cloud database skills (highest priority)
