# T26 Optimization Quick Reference

**Analysis Date:** 2025-11-25

---

## AT A GLANCE

**Current Skills:** 66
**Recommended Skills:** ~105
**New Skills to Add:** 21
**Skills to Break Down:** 8 (→ 18 sub-skills)
**Dependencies to Fix:** 2
**Descriptions to Improve:** 3

---

## PRIORITY 1: CRITICAL FIXES

### 1. Fix Misplaced Skill ID
```
MOVE: T26.G6.01.01 (compound database conditions)
TO:   T26.G6.06.04

REASON: G6.01 is about stakeholder mapping, not database queries
```

### 2. Fix Phantom Dependency
```
CHANGE: T26.G5.01 depends on "T26.G4.02"
TO:     T26.G5.01 depends on "T26.G4.02.02"

REASON: T26.G4.02 parent skill doesn't exist (only .01 and .02)
```

### 3. Add Missing Console Logging Sub-Skills
```
ADD: T26.G5.01.01 - Log messages to console with colors
ADD: T26.G5.01.02 - Retrieve console log history

REASON: G5.01 is too broad, blocks exist but not taught systematically
```

---

## PRIORITY 2: MISSING BLOCK COVERAGE (21 NEW SKILLS)

### G4: List Text Operations (3 skills)
```
T26.G4.07.01: Export list data to text format (join)
T26.G4.07.02: Parse text data into lists (split)
T26.G4.07.03: Search for items in collected data (contains, item #)
```

### G5: Statistics & Advanced Operations (10 skills)
```
T26.G5.10.01: Calculate basic statistics (min/max/sum/average)
T26.G5.10.02: Calculate median of collected data

T26.G5.11.01: Extract column data as lists
T26.G5.11.02: Add columns to existing tables
T26.G5.11.03: Remove columns from tables

T26.G5.12.01: Save single values to server
T26.G5.12.02: Load saved data from server
T26.G5.12.03: Understand public vs private visibility

T26.G5.13.01: Export table data as CSV files
```

### G6: Table Queries & Transformations (8 skills)
```
T26.G6.10.01: Find specific records in tables
T26.G6.10.02: Filter table data by conditions
T26.G6.10.03: Calculate column statistics

T26.G6.11.01: Import CSV files into tables

T26.G6.12.01: Sort collected data by columns
T26.G6.12.02: Copy and merge data tables
T26.G6.12.03: Group data by categories
```

---

## PRIORITY 3: BREAK DOWN BROAD SKILLS (8 SKILLS → 18 SUB-SKILLS)

### 1. T26.G5.02 - Sampling (2 sub-skills)
```
T26.G5.02.01: Compare sampling methods (convenience vs random)
T26.G5.02.02: Implement random sampling with code
```

### 2. T26.G5.04 - Table Logging (2 sub-skills)
```
Keep: T26.G5.04.01 (create tables with columns)
ADD:  T26.G5.04.02 (add rows with event data)
ADD:  T26.G5.04.03 (read specific cells)
```

### 3. T26.G6.01 - Stakeholder Mapping (2 sub-skills)
```
T26.G6.01.01: Identify measurable variables from questions (REPLACE current)
T26.G6.01.02: Design data schema for stakeholder needs
```

### 4. T26.G6.02 - Multi-Sensor (1 sub-skill)
```
T26.G6.02.01: Add timestamps to sensor data
T26.G6.02.02: Collect from three sensors (rename current)
```

### 5. T26.G7.03 - Provenance (3 sub-skills)
```
T26.G7.03.01: Import external CSV datasets
T26.G7.03.02: Document dataset metadata
T26.G7.03.03: Practice citation and attribution
```

### 6. T26.G8.01 - Telemetry Design (6 sub-skills)
```
T26.G8.01.01: Design event capture layer (REPLACE current)
T26.G8.01.02: Design validation rules
T26.G8.01.03: Design storage schema
T26.G8.01.04: Plan database persistence
T26.G8.01.05: Design query and export workflows
T26.G8.01.06: Implement complete pipeline (MOVE from current G8.01.01)
```

### 7. T26.G8.04 - Privacy (2 sub-skills)
```
T26.G8.04.01: List data types and storage locations
T26.G8.04.02: Define access controls and deletion timelines
```

### 8. T26.G4.02 - Tables (FIX)
```
DELETE: T26.G4.02 (phantom parent)
KEEP:   T26.G4.02.01 (create basic tables)
KEEP:   T26.G4.02.02 (log multi-attribute events)
```

---

## PRIORITY 4: DESCRIPTION IMPROVEMENTS

### 1. T26.G3.02 - Remove Non-Existent Block Reference
```
CURRENT: "...using the ask block with multiple-choice buttons..."
PROBLEM: CreatiCode doesn't have multiple-choice buttons in ask block
FIX:     "...using the ask block with conditional logic..."
```

### 2. T26.G4.06 - Clarify "AI Sensor"
```
CURRENT: "Collect data from one AI sensor (like microphone volume...)"
PROBLEM: Microphone isn't an AI sensor
FIX:     "Collect data from one sensor (microphone volume, mouse position...)"
```

### 3. T26.G8.05 - Clarify Data Collection Context
```
ADD: "Students collect text data (user comments, survey responses) into a
      semantic database..."
REASON: Makes collection aspect clearer
```

---

## BLOCK COVERAGE MAP

### Fully Covered ✅
- Basic list operations (add, remove, length)
- Basic table operations (create, add row, read cell)
- Database CRUD (insert, query, update, delete)
- Google Sheets (read, write, sync)
- Leaderboard (basic record/display)

### Partially Covered ⚠️
- List statistics (blocks exist, no skills) → ADD G5.10.01-02
- List text operations (join/split blocks exist) → ADD G4.07.01-02
- Table columns (blocks exist, no skills) → ADD G5.11.01-03
- Table queries (blocks exist, no skills) → ADD G6.10.01-03
- Server storage (blocks exist, no skills) → ADD G5.12.01-03
- Console logging (blocks exist, minimal skills) → ADD G5.01.01-02

### Not Covered (OK) ✅
- Table transformation (pivot, reshuffle) → Belongs in T27 (Analysis)
- Advanced list operations (reverse, shuffle) → Optional/T27
- Google Sheets admin (add/remove sheets) → Administrative

---

## GRADE DISTRIBUTION

### Current (66 skills)
```
GK: 3   G1: 3   G2: 5   G3: 6   G4: 7   G5: 9   G6: 13   G7: 7   G8: 5
```

### Recommended (~105 skills)
```
GK: 3   G1: 3   G2: 5   G3: 6   G4: 11   G5: 29   G6: 26   G7: 11   G8: 11
```

### Growth Areas
- **G4:** +4 skills (list text operations, clarifications)
- **G5:** +20 skills (statistics, columns, server storage, console)
- **G6:** +13 skills (table queries, CSV import, transformations)
- **G7:** +4 skills (provenance sub-skills)
- **G8:** +6 skills (pipeline decomposition)

---

## IMPLEMENTATION PHASES

### Phase 1: Fixes (1-2 hours)
- Fix G6.01.01 misplacement
- Fix G5.01 dependency
- Add G5.01.01-02 console skills
- Add G5.12.01-03 server storage

### Phase 2: Block Coverage (3-4 hours)
- Add G4.07 list text skills (3)
- Add G5.10 statistics skills (2)
- Add G5.11 column skills (3)
- Add G6.10 table query skills (3)

### Phase 3: Decomposition (2-3 hours)
- Break down G8.01 (6 sub-skills)
- Break down G6.01 (2 sub-skills)
- Break down G7.03 (3 sub-skills)
- Add G6.02.01 timestamp skill

### Phase 4: Polish (1-2 hours)
- Improve 3 descriptions
- Review all dependencies
- Add optional capstone skills

**Total Estimated Time:** 7-11 hours

---

## DEPENDENCY FIXES

### Critical
1. **G6.01.01** → Rename to G6.06.04
2. **G5.01** → Change dependency from G4.02 to G4.02.02

### Recommended
3. Review all G6.01 dependencies (11 total) after restructuring
4. Update G8.01 dependency chain after decomposition

---

## PEDAGOGICAL FLOW

### Current Flow ✅ GOOD
```
K-G2: Unplugged (counting, surveys, logs)
G3:   Basic coding (loops, lists, ask)
G4:   Tables (multi-attribute data)
G5:   Persistence (files, server, stats)
G6:   Cloud (database, sheets, multi-sensor)
G7:   Modules (reusable, provenance, ethics)
G8:   Pipelines (end-to-end, AI integration)
```

### Recommended Enhancements
```
G4: Add list text operations (export/parse)
G5: Add statistics & column operations
G6: Add table queries & transformations
G7: Add provenance sub-steps
G8: Add pipeline design stages
```

---

## ALIGNMENT WITH AI4K12

### Strong ✅
- Ethics & Privacy (consent, bias, privacy agreements)
- Data Representation (schemas, tables, databases)
- Computing Systems (files, server, cloud, databases)

### Could Improve ⚠️
- Learning from Data (add ML training data collection in G8)
- Natural Interaction (semantic search is good, could expand)

---

## CROSS-TOPIC DEPENDENCIES

### Depends Heavily On:
- **T09** (Variables) - counters, monitors
- **T10** (Lists & Tables) - basic CRUD
- **T25** (Data Representation) - advanced operations

### Provides To:
- **T27** (Data Analysis) - collected datasets
- **T24** (AI Integration) - training data
- **T28** (Visualization) - data to visualize

### Check:
- Ensure T26 skills don't overlap with T27 (analysis)
- Clarify boundary between collection and transformation

---

## SUMMARY METRICS

| Metric | Current | Recommended | Change |
|--------|---------|-------------|--------|
| Total Skills | 66 | ~105 | +39 (+59%) |
| K-G2 Skills | 11 | 11 | +0 |
| G3-G4 Skills | 13 | 17 | +4 |
| G5-G6 Skills | 22 | 55 | +33 |
| G7-G8 Skills | 12 | 22 | +10 |
| Skills with Blocks | 45 | 78 | +33 |
| Conceptual Skills | 21 | 27 | +6 |

---

## NEXT STEPS

1. ✅ Review this analysis
2. ⬜ Prioritize which recommendations to implement
3. ⬜ Create detailed skill definitions for Phase 1
4. ⬜ Update allskills.md with fixes
5. ⬜ Generate dependency graphs
6. ⬜ Create visual skill maps
7. ⬜ Write assessment items for new skills

---

**For detailed analysis, see:** T26_OPTIMIZATION_ANALYSIS_COMPLETE.md
