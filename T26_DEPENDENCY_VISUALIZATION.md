# T26 Dependency Visualization

## Within-Topic Dependency Map

This shows ONLY dependencies within T26 (excludes T01-T25, T27+ dependencies for clarity).

```
KINDERGARTEN
┌─────────┐
│ GK.01   │ Identify countable things
│(base)   │
└────┬────┘
     ├──────────────────┐
     │                  │
     ▼                  ▼
┌─────────┐        ┌─────────┐
│ GK.02   │        │ GK.03   │
│ Tokens  │        │Yes/No   │
└─────────┘        └────┬────┘
                        │
                        │
GRADE 1                 │
                        ▼
                   ┌─────────┐
                   │ G1.01   │ Three-option survey
                   │ Survey  │
                   └────┬────┘
                        ├──────────────────┐
                        │                  │
                        ▼                  ▼
                   ┌─────────┐        ┌─────────┐
                   │ G1.02   │        │ G1.03   │
                   │Obs Logs │        │Checklist│
                   └────┬────┘        └─────────┘
                        │
                        │
GRADE 2                 │
     ┌──────────────────┼──────────────────┐
     │                  │                  │
     ▼                  ▼                  ▼
┌─────────┐        ┌─────────┐        ┌─────────┐
│ G2.01   │        │ G2.02   │        │ G2.03   │
│Obs vs   │        │Two-col  │        │ Timers  │
│Survey   │        │ Sheet   │        │         │
└────┬────┘        └────┬────┘        └─────────┘
     │                  │
     │                  ├──────────────────┐
     │                  ▼                  │
     │             ┌─────────┐             │
     │             │ G2.04   │             │
     │             │ Sample  │             │
     │             │  Size   │             │
     │             └────┬────┘             │
     │                  │                  │
     │                  ▼                  │
     │             ┌─────────┐             │
     │             │ G2.05   │             │
     │             │Multi-   │             │
     │             │Response │             │
     │             └─────────┘             │
     │                                     │
GRADE 3 (CODING BEGINS)                  │
     │                                     │
     ▼                                     │
┌─────────┐                               │
│ G3.01   │ Survey loop (KEY TRANSITION) │
│ Survey  │                               │
│  Loop   │                               │
└────┬────┘                               │
     ├──────────────────┐                 │
     │                  │                 │
     ▼                  ▼                 │
┌─────────┐        ┌─────────┐           │
│ G3.02   │        │ G3.03   │           │
│  Fair   │        │ Sensor  │           │
│Question │        │Counters │           │
└─────────┘        └────┬────┘           │
                        │                │
                        ▼                │
                   ┌─────────┐           │
                   │ G3.04   │ Raw vs Summary (KEY CONCEPT)
                   │ Raw vs  │           │
                   │ Summary │           │
                   └────┬────┘           │
                        ├────────────────┘
                        ▼
                   ┌─────────┐
                   │ G3.05   │
                   │  Spot   │
                   │ Mistakes│
                   └─────────┘

GRADE 4 (TABLE OPERATIONS BEGIN)
     ┌──────────────────┼──────────────────┐
     │                  │                  │
     ▼                  ▼                  ▼
┌─────────┐        ┌─────────┐        ┌─────────┐
│ G4.01   │        │ G4.02   │────────│ G4.03   │
│Protocol │        │ Tables  │        │Invalid  │
│         │        │         │        │  Flags  │
└────┬────┘        └────┬────┘        └─────────┘
     │                  │
     │                  │
     ▼                  │
┌─────────┐             │
│ G4.04   │             │
│ Privacy │             │
│         │             │
└─────────┘             │
                        │
GRADE 5                 │
     ┌──────────────────┼──────────────────┐
     │                  │                  │
     ▼                  ▼                  ▼
┌─────────┐        ┌─────────┐        ┌─────────┐
│ G5.01   │        │ G5.02   │        │ G5.03   │
│ Print   │        │Sampling │        │Validate │
│  Log    │        │Strategy │        │  Entry  │
└────┬────┘        └─────────┘        └─────────┘
     │                   │
     │                   │(removed K deps)
     ▼                   │
┌─────────┐              │
│ G5.04   │              │
│ Store   │              │
│ Tables  │              │
└────┬────┘              │
     │                   │
     │                   │
GRADE 6                  │
     ├───────────────────┼──────────────────┐
     │                   │                  │
     ▼                   ▼                  ▼
┌─────────┐        ┌─────────┐        ┌─────────┐
│ G6.01   │────────│ G6.03   │        │ G6.04   │
│Stakehold│        │ Consent │        │ Note    │
│  Map    │        │Workflow │        │Inaccur  │
└────┬────┘        └─────────┘        └─────────┘
     │
     │             ┌─────────┐
     │             │ G6.02   │
     │             │Multi-In │
     │             └─────────┘
     │
GRADE 7
     │
     ├──────────────────┬──────────────────┐
     │                  │                  │
     ▼                  ▼                  ▼
┌─────────┐        ┌─────────┐        ┌─────────┐
│ G7.01   │────────│ G7.02   │        │ G7.03   │
│Reusable │        │ Monitor │        │Document │
│ Modules │        │ Quality │        │Provenanc│
└────┬────┘        └─────────┘        └─────────┘
     │
     │             ┌─────────┐
     │             │ G7.04   │
     │             │Evaluate │
     │             │  Bias   │
     │             └─────────┘
     │
GRADE 8
     │
     ├──────────────────┬──────────────────┐
     │                  │                  │
     ▼                  ▼                  ▼
┌─────────┐        ┌─────────┐        ┌─────────┐
│ G8.01   │────────│ G8.02   │        │ G8.03   │
│Telemetry│        │Scheduled│        │AI Review│
│ Pipeline│        │ Exports │        │         │
└─────────┘        └─────────┘        └─────────┘

                   ┌─────────┐
                   │ G8.04   │
                   │ Privacy │
                   │Agreement│
                   └─────────┘
```

---

## Key Dependency Chains

### Chain 1: Survey Evolution (Unplugged → Coding)
```
GK.01 → GK.03 → G1.01 → G2.02 → G2.04 → G3.01
(count)  (yes/no) (3-opt) (2-col)  (size)  (loop)
```

### Chain 2: Observation/Logging
```
GK.01 → GK.02 → G1.02 → G2.01 → G3.01
(count) (tokens) (obs)   (obs/sur) (loop)
```

### Chain 3: Sensor → Tables → Export
```
G3.03 → G3.04 → G4.02 → G5.01 → G5.04
(sensor) (raw/sum) (tables) (print) (export)
```

### Chain 4: Data Quality
```
G3.04 → G4.03 → G5.03 → G6.04 → G7.02
(raw/sum) (flags) (validate) (note)  (monitor)
```

### Chain 5: Privacy/Ethics Thread
```
G4.04 → G6.03 → G7.03 → G8.04
(privacy) (consent) (provenance) (agreement)
```

### Chain 6: Reusability/Pipelines
```
G5.04 → G6.01 → G7.01 → G8.01 → G8.02
(export) (stakehld) (modules) (pipeline) (scheduled)
```

---

## Dependency Statistics

### Within-Topic Dependencies by Grade

| Grade | Skills | With T26 Deps | Without T26 Deps | Avg T26 Deps per Skill |
|-------|--------|---------------|------------------|------------------------|
| K | 3 | 2 (67%) | 1 (33%) | 0.67 |
| G1 | 3 | 3 (100%) | 0 (0%) | 1.00 |
| G2 | 5 | 4 (80%) | 1 (20%) | 0.80 |
| G3 | 5 | 4 (80%) | 1 (20%) | 0.80 |
| G4 | 4 | 4 (100%) | 0 (0%) | 1.25 |
| G5 | 4 | 4 (100%) | 0 (0%) | 1.25 |
| G6 | 4 | 3 (75%) | 1 (25%) | 1.00 |
| G7 | 4 | 3 (75%) | 1 (25%) | 1.00 |
| G8 | 4 | 3 (75%) | 1 (25%) | 0.75 |
| **Total** | **36** | **30 (83%)** | **6 (17%)** | **0.97** |

**Key Insight:** Most skills (83%) depend on at least one prior T26 skill, showing strong cumulative learning within the topic.

---

## Cross-Topic Dependencies by Grade

| Grade | T01 | T06 | T07 | T08 | T09 | T10 | T11 | T23 | T24 | T25 | Total |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-------|
| K | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| G1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| G2 | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 4 |
| G3 | 0 | 0 | 1 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 9 |
| G4 | 0 | 4 | 0 | 3 | 4 | 4 | 0 | 0 | 0 | 0 | 15 |
| G5 | 0 | 0 | 0 | 2 | 4 | 4 | 0 | 0 | 0 | 0 | 10 |
| G6 | 0 | 1 | 0 | 3 | 4 | 4 | 0 | 1 | 0 | 0 | 13 |
| G7 | 0 | 1 | 0 | 2 | 2 | 3 | 1 | 0 | 0 | 0 | 9 |
| G8 | 1 | 2 | 0 | 0 | 3 | 3 | 0 | 0 | 1 | 0 | 10 |
| **Total** | **5** | **8** | **1** | **14** | **25** | **22** | **1** | **1** | **1** | **1** | **79** |

**Key Insight:** T09 (Variables) and T10 (Lists/Tables) are the most critical prerequisites for T26, followed by T08 (Conditionals).

---

## Isolated vs Connected Skills

### Base Skills (No T26 Dependencies)
- **T26.GK.01** - First skill in topic
- **T26.G2.01** - Depends only on T01.G1.01 and T26.G1.02
- **T26.G3.01** - Transition to coding (depends on T26.G2.01, T07.G3.01)
- **T26.G6.02** - Multi-input logging (depends on external topics + T26.G5.04)
- **T26.G7.03** - Provenance (depends on external topics + T26.G5.04 + T26.G6.03)
- **T26.G8.04** - Privacy agreement (depends on T26.G6.03 + T26.G7.04)

### Highly Connected Skills (3+ T26 Dependencies)
None found - longest chain is 2 direct T26 dependencies.

**This is GOOD:** Shows skills are modular and don't create deep dependency nesting.

---

## Dependency Types

### Sequential Dependencies (Skill N → N+1)
- G1.01 → G1.02 (survey → observation)
- G2.02 → G2.04 (sheet → sample size)
- G3.03 → G3.04 (counters → raw/summary)
- G4.02 → G4.03 (tables → flags)
- G5.01 → G5.04 (print → store)
- G7.01 → G7.02 (modules → monitor)
- G8.01 → G8.02 (pipeline → scheduled)

### Branching Dependencies (Skill N → M, P)
- GK.01 → GK.02, GK.03 (count → both collection methods)
- G1.01 → G1.02, G1.03 (survey → both obs and checklist)
- G3.01 → G3.02, G3.03 (loop → both fair questions and sensors)
- G3.04 → G4.01, G4.02 (raw/summary → both protocols and tables)
- G5.04 → G6.01, G6.02, G7.03 (export → multiple G6-G7 uses)

### Convergent Dependencies (Skills M, P → N)
- G2.02, G2.04 → G2.05 (sheet + size → multi-response)
- T26.G4.01, T26.G4.04 dependencies both use G4.01
- T26.G6.03, T26.G7.04 → G8.04 (consent + bias → privacy agreement)

---

## Grade Transition Analysis

### K→G1 Transition
- **Carries forward:** GK.03 (yes/no) → G1.01 (three-option survey)
- **New concepts:** Longitudinal observation (G1.02), checklists (G1.03)
- **Pedagogical note:** Expansion from binary to multi-choice

### G1→G2 Transition
- **Carries forward:** G1.01 → multiple G2 skills
- **New concepts:** Distinguish methods (G2.01), structured tables (G2.02), timers (G2.03)
- **Pedagogical note:** Adding rigor and structure

### G2→G3 Transition (CRITICAL: Unplugged → Coding)
- **Carries forward:** G2.01 → G3.01 (concepts to code)
- **New concepts:** All coding-based (loops, variables, lists)
- **Pedagogical note:** Biggest conceptual leap; well-scaffolded by G2.01 bridge

### G3→G4 Transition
- **Carries forward:** G3.04 → G4.01, G4.02 (raw/summary → protocols and tables)
- **New concepts:** Tables (vs lists), multi-attribute logging, team protocols
- **Pedagogical note:** Shift from individual to collaborative, lists to tables

### G4→G5 Transition
- **Carries forward:** G4.02 → G5.01 (tables → print logging), G4.03 → G5.03 (flags → validation)
- **New concepts:** Export/persistence (G5.04), sampling strategies (G5.02)
- **Pedagogical note:** Making data portable

### G5→G6 Transition
- **Carries forward:** G5.04 → G6.01, G6.02 (export → stakeholder mapping and multi-input)
- **New concepts:** Requirements gathering (G6.01), consent workflows (G6.03)
- **Pedagogical note:** Professional practices

### G6→G7 Transition
- **Carries forward:** G6.01 → G7.01 (stakeholder → reusable modules)
- **New concepts:** Modularity (G7.01), real-time monitoring (G7.02), provenance (G7.03)
- **Pedagogical note:** Engineering maturity

### G7→G8 Transition
- **Carries forward:** G7.01 → G8.01, G8.02 (modules → pipelines)
- **New concepts:** End-to-end systems (G8.01), AI assistance (G8.03)
- **Pedagogical note:** Systems thinking

---

## Recommendations Based on Dependencies

### Strengthen G2→G3 Bridge
Currently G2.01 → G3.01 is the only unplugged-to-coding bridge. Consider:
- Add transition skill or
- Add more unplugged reflection in G2 about "what would code need to do this?"

### Consider G5.02 Dependencies
Currently reaches back to Kindergarten (X-2 violation). FIXED in recommendations.

### Evaluate G4 Dependencies
Three G4 skills depend on G3 versions of T06, T09, T10. Should check if G4 equivalents exist.

---

**Document Version:** 1.0
**Created:** 2025-11-21
**See Also:**
- T26_COMPREHENSIVE_ANALYSIS.md (full details)
- T26_QUICK_REFERENCE.md (summary)
