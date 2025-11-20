# Grade 5 Skills - Comprehensive Fix Plan

**Generated:** 2025-11-20
**Total Skills to Fix:** 28
**Source:** Based on G5 comprehensive analysis reports
**Status:** Ready for implementation

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Detailed Fix Specifications by Topic](#detailed-fix-specifications-by-topic)
   - [T03 - Problem Decomposition](#t03-3-skills)
   - [T05 - Design & Modeling](#t05-6-skills)
   - [T12 - Documentation](#t12-1-skills)
   - [T13 - Testing & Debugging](#t13-1-skills)
   - [T25 - Data Structures](#t25-3-skills)
   - [T30 - Hardware](#t30-4-skills)
   - [T31 - Internet & Cloud](#t31-1-skills)
   - [T32 - Security](#t32-3-skills)
   - [T34 - History of Computing](#t34-2-skills)
   - [T35 - Impacts of Computing](#t35-3-skills)
   - [T36 - Inclusion & Diversity](#t36-1-skills)
3. [Implementation Guide](#implementation-guide)
4. [Validation Checklist](#validation-checklist)
5. [Replacement Mappings](#replacement-mappings)
6. [Machine-Readable Fix Data](#machine-readable-fix-data)

---

## Executive Summary

This document provides a complete, implementable fix plan for all 28 Grade 5 skills
with dependency issues. Each fix has been validated to:

- Replace G1/G2 dependencies with G3/G4 equivalents
- Remove transitive dependencies
- Fix same-grade dependencies
- Maintain pedagogical coherence

### Change Summary

- **Total Dependency Removals:** 52
- **Total Dependency Additions:** 26
- **Net Change:** -26 dependencies (cleaner dependency graph)

### Issues Addressed

- **38 HIGH Priority Issues:** Invalid grade dependencies (G5 depending on G1/G2)
- **25 MEDIUM Priority Issues:** Transitive dependencies
- **1 MEDIUM Priority Issue:** Same-grade dependency (T31.G5.02)

### Impact by Topic

| Topic | Skills Fixed | Replacements | Removals | Net Change |
|-------|--------------|--------------|----------|------------|
| T03 | 3 | 3 | 3 | 0 |
| T05 | 6 | 7 | 11 | -4 |
| T12 | 1 | 1 | 1 | 0 |
| T13 | 1 | 1 | 1 | 0 |
| T25 | 3 | 3 | 7 | -4 |
| T30 | 4 | 3 | 10 | -7 |
| T31 | 1 | 0 | 1 | -1 |
| T32 | 3 | 3 | 6 | -3 |
| T34 | 2 | 2 | 4 | -2 |
| T35 | 3 | 4 | 6 | -2 |
| T36 | 1 | 1 | 2 | -1 |
| **Total** | **28** | **26** | **52** | **-26** |

### Key Findings

1. **Most G1/G2 dependencies have G3 equivalents** in the same topic
2. **T30 (Hardware) most affected** - 4 skills, 10 dependency removals
3. **T05 (Design & Modeling)** - All 6 G5 skills had issues
4. **Only 1 skill needs manual review** (T31.G5.02 - same-grade dependency)

---

## Detailed Fix Specifications by Topic

### T03 (3 skills)

#### T03.G5.01 - Create a feature list and subtask breakdown

**Current Dependencies:**
- T03.G1.02 (G1)
- T03.GK.04 (GK)
- T06.G3.01 (G3)

**Issues Found:**
- Invalid grade: T03.G1.02

**Proposed Dependencies:**
- T03.G3.01 (G3) - Identify features in a small game description
- T03.GK.04 (GK) - Choose the missing middle step in a routine
- T06.G3.01 (G3) - Build a green‑flag script that runs a 3–5 block sequence

**Dependencies to Remove:**
- T03.G1.02

**Dependencies to Add:**
- T03.G3.01 - Identify features in a small game description

**Rationale:**
- Replace T03.G1.02 with T03.G3.01: Same topic (T03) G3 skill replacing G1 skill

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 1
- Dependencies added: 1

---

#### T03.G5.03 - Identify task dependencies in a project plan

**Current Dependencies:**
- T03.G1.02 (G1)
- T03.GK.04 (GK)

**Issues Found:**
- Invalid grade: T03.G1.02

**Proposed Dependencies:**
- T03.G3.01 (G3) - Identify features in a small game description
- T03.GK.04 (GK) - Choose the missing middle step in a routine

**Dependencies to Remove:**
- T03.G1.02

**Dependencies to Add:**
- T03.G3.01 - Identify features in a small game description

**Rationale:**
- Replace T03.G1.02 with T03.G3.01: Same topic (T03) G3 skill replacing G1 skill

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 1
- Dependencies added: 1

---

#### T03.G5.04 - Flag high‑risk or unclear tasks

**Current Dependencies:**
- T03.G1.02 (G1)
- T03.GK.04 (GK)

**Issues Found:**
- Invalid grade: T03.G1.02

**Proposed Dependencies:**
- T03.G3.01 (G3) - Identify features in a small game description
- T03.GK.04 (GK) - Choose the missing middle step in a routine

**Dependencies to Remove:**
- T03.G1.02

**Dependencies to Add:**
- T03.G3.01 - Identify features in a small game description

**Rationale:**
- Replace T03.G1.02 with T03.G3.01: Same topic (T03) G3 skill replacing G1 skill

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 1
- Dependencies added: 1

---

### T05 (6 skills)

#### T05.G5.01 - Write clear user needs and requirements for a small app

**Current Dependencies:**
- T05.G1.02 (G1)
- T05.GK.03 (GK)
- T05.GK.04 (GK)
- T06.G3.01 (G3)

**Issues Found:**
- Invalid grade: T05.G1.02
- Transitive dependencies: T05.GK.03

**Proposed Dependencies:**
- T05.G3.01 (G3) - Put human‑centered design steps in order
- T05.GK.04 (GK) - Choose a change that makes something easier
- T06.G3.01 (G3) - Build a green‑flag script that runs a 3–5 block sequence

**Dependencies to Remove:**
- T05.G1.02
- T05.GK.03

**Dependencies to Add:**
- T05.G3.01 - Put human‑centered design steps in order

**Rationale:**
- Replace T05.G1.02 with T05.G3.01: Same topic (T05) G3 skill replacing G1 skill
- Remove T05.GK.03: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

#### T05.G5.02 - Create a low‑fidelity sketch for a user story

**Current Dependencies:**
- T05.G1.02 (G1)
- T05.GK.03 (GK)
- T05.GK.04 (GK)
- T06.G3.01 (G3)

**Issues Found:**
- Invalid grade: T05.G1.02
- Transitive dependencies: T05.GK.03

**Proposed Dependencies:**
- T05.G3.01 (G3) - Put human‑centered design steps in order
- T05.GK.04 (GK) - Choose a change that makes something easier
- T06.G3.01 (G3) - Build a green‑flag script that runs a 3–5 block sequence

**Dependencies to Remove:**
- T05.G1.02
- T05.GK.03

**Dependencies to Add:**
- T05.G3.01 - Put human‑centered design steps in order

**Rationale:**
- Replace T05.G1.02 with T05.G3.01: Same topic (T05) G3 skill replacing G1 skill
- Remove T05.GK.03: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

#### T05.G5.03 - Identify variables and initial values for a simulation

**Current Dependencies:**
- T01.G3.01 (G3)
- T05.GK.03 (GK)
- T05.GK.04 (GK)
- T09.G3.01 (G3)

**Issues Found:**
- Transitive dependencies: T05.GK.03

**Proposed Dependencies:**
- T01.G3.01 (G3) - Complete a simple script with missing blocks
- T05.GK.04 (GK) - Choose a change that makes something easier
- T09.G3.01 (G3) - Create and use a numeric variable for score or count

**Dependencies to Remove:**
- T05.GK.03

**Rationale:**
- Remove T05.GK.03: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 1
- Dependencies added: 0

---

#### T05.G5.04 - Draft simple update rules for a simulation

**Current Dependencies:**
- T05.GK.03 (GK)
- T05.GK.04 (GK)
- T09.G3.01 (G3)

**Issues Found:**
- Transitive dependencies: T05.GK.03

**Proposed Dependencies:**
- T05.GK.04 (GK) - Choose a change that makes something easier
- T09.G3.01 (G3) - Create and use a numeric variable for score or count

**Dependencies to Remove:**
- T05.GK.03

**Rationale:**
- Remove T05.GK.03: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 1
- Dependencies added: 0

---

#### T05.G5.05 - Plan how to test whether a design meets user needs

**Current Dependencies:**
- T04.G2.01 (G2)
- T05.G1.01 (G1)
- T05.GK.03 (GK)
- T05.GK.04 (GK)
- T06.G3.01 (G3)

**Issues Found:**
- Invalid grade: T04.G2.01
- Invalid grade: T05.G1.01
- Transitive dependencies: T05.GK.03

**Proposed Dependencies:**
- T04.G3.01 (G3) - Identify where a loop could replace repeated blocks
- T05.G3.01 (G3) - Put human‑centered design steps in order
- T05.GK.04 (GK) - Choose a change that makes something easier
- T06.G3.01 (G3) - Build a green‑flag script that runs a 3–5 block sequence

**Dependencies to Remove:**
- T04.G2.01
- T05.G1.01
- T05.GK.03

**Dependencies to Add:**
- T04.G3.01 - Identify where a loop could replace repeated blocks
- T05.G3.01 - Put human‑centered design steps in order

**Rationale:**
- Replace T04.G2.01 with T04.G3.01: Same topic (T04) G3 skill replacing G2 skill
- Replace T05.G1.01 with T05.G3.01: Same topic (T05) G3 skill replacing G1 skill
- Remove T05.GK.03: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 3
- Dependencies added: 2

---

#### T05.G5.06 - Plan what to measure in a simulation experiment

**Current Dependencies:**
- T05.G1.02 (G1)
- T05.GK.03 (GK)
- T05.GK.04 (GK)

**Issues Found:**
- Invalid grade: T05.G1.02
- Transitive dependencies: T05.GK.03

**Proposed Dependencies:**
- T05.G3.01 (G3) - Put human‑centered design steps in order
- T05.GK.04 (GK) - Choose a change that makes something easier

**Dependencies to Remove:**
- T05.G1.02
- T05.GK.03

**Dependencies to Add:**
- T05.G3.01 - Put human‑centered design steps in order

**Rationale:**
- Replace T05.G1.02 with T05.G3.01: Same topic (T05) G3 skill replacing G1 skill
- Remove T05.GK.03: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

### T12 (1 skills)

#### T12.G5.02 - Document code functionality and choices

**Current Dependencies:**
- T12.G1.01 (G1)
- T12.G4.03 (G4)
- T12.G4.04 (G4)

**Issues Found:**
- Invalid grade: T12.G1.01

**Proposed Dependencies:**
- T12.G3.01 (G3) - Write a comment explaining a complex block
- T12.G4.03 (G4) - Refactor repeated blocks into a custom block for clarity
- T12.G4.04 (G4) - Analyze and improve variable scope and naming

**Dependencies to Remove:**
- T12.G1.01

**Dependencies to Add:**
- T12.G3.01 - Write a comment explaining a complex block

**Rationale:**
- Replace T12.G1.01 with T12.G3.01: Same topic (T12) G3 skill replacing G1 skill

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 1
- Dependencies added: 1

---

### T13 (1 skills)

#### T13.G5.04 - Modify a program to improve reliability and correctness

**Current Dependencies:**
- T06.G3.01 (G3)
- T13.G1.01 (G1)
- T13.GK.02 (GK)
- T13.GK.03 (GK)

**Issues Found:**
- Invalid grade: T13.G1.01

**Proposed Dependencies:**
- T06.G3.01 (G3) - Build a green‑flag script that runs a 3–5 block sequence
- T13.G4.01 (G4) - Debug a conditional inside a loop
- T13.GK.02 (GK) - Try again when the steps don't work
- T13.GK.03 (GK) - Fix a single wrong direction or action in steps

**Dependencies to Remove:**
- T13.G1.01

**Dependencies to Add:**
- T13.G4.01 - Debug a conditional inside a loop

**Rationale:**
- Replace T13.G1.01 with T13.G4.01: Same topic (T13) G4 skill replacing G1 skill

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 1
- Dependencies added: 1

---

### T25 (3 skills)

#### T25.G5.01 - Model multi-type game state

**Current Dependencies:**
- T09.G3.01 (G3)
- T25.G1.01 (G1)
- T25.GK.02 (GK)
- T25.GK.03 (GK)

**Issues Found:**
- Invalid grade: T25.G1.01
- Transitive dependencies: T25.GK.02

**Proposed Dependencies:**
- T09.G3.01 (G3) - Create and use a numeric variable for score or count
- T25.G3.01 (G3) - Map survey responses into list variables
- T25.GK.03 (GK) - Build a two-symbol legend

**Dependencies to Remove:**
- T25.G1.01
- T25.GK.02

**Dependencies to Add:**
- T25.G3.01 - Map survey responses into list variables

**Rationale:**
- Replace T25.G1.01 with T25.G3.01: Same topic (T25) G3 skill replacing G1 skill
- Remove T25.GK.02: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

#### T25.G5.02 - Convert messy inputs into canonical formats

**Current Dependencies:**
- T06.G3.01 (G3)
- T25.G1.01 (G1)
- T25.GK.02 (GK)
- T25.GK.03 (GK)

**Issues Found:**
- Invalid grade: T25.G1.01
- Transitive dependencies: T25.GK.02

**Proposed Dependencies:**
- T06.G3.01 (G3) - Build a green‑flag script that runs a 3–5 block sequence
- T25.G3.01 (G3) - Map survey responses into list variables
- T25.GK.03 (GK) - Build a two-symbol legend

**Dependencies to Remove:**
- T25.G1.01
- T25.GK.02

**Dependencies to Add:**
- T25.G3.01 - Map survey responses into list variables

**Rationale:**
- Replace T25.G1.01 with T25.G3.01: Same topic (T25) G3 skill replacing G1 skill
- Remove T25.GK.02: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

#### T25.G5.03 - Decide when to upgrade from list to table

**Current Dependencies:**
- T25.G1.01 (G1)
- T25.G1.02 (G1)
- T25.GK.02 (GK)
- T25.GK.03 (GK)

**Issues Found:**
- Invalid grade: T25.G1.01
- Invalid grade: T25.G1.02
- Transitive dependencies: T25.G1.01, T25.GK.02

**Proposed Dependencies:**
- T25.G3.01 (G3) - Map survey responses into list variables
- T25.GK.03 (GK) - Build a two-symbol legend

**Dependencies to Remove:**
- T25.G1.01
- T25.G1.02
- T25.GK.02

**Dependencies to Add:**
- T25.G3.01 - Map survey responses into list variables

**Rationale:**
- Replace T25.G1.01 with T25.G3.01: Same topic (T25) G3 skill replacing G1 skill
- Remove T25.G1.01: transitive dependency already covered
- Remove T25.GK.02: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 3
- Dependencies added: 1

---

### T30 (4 skills)

#### T30.G5.01 - Match CreatiCode AI features to hardware requirements

**Current Dependencies:**
- T30.G1.01 (G1)
- T30.G1.02 (G1)
- T30.GK.02 (GK)
- T30.GK.03 (GK)

**Issues Found:**
- Invalid grade: T30.G1.01
- Invalid grade: T30.G1.02
- Transitive dependencies: T30.G1.01, T30.GK.02

**Proposed Dependencies:**
- T30.G3.01 (G3) - Connect project ideas to required sensors/actuators
- T30.GK.03 (GK) - Recognize input vs output examples

**Dependencies to Remove:**
- T30.G1.01
- T30.G1.02
- T30.GK.02

**Dependencies to Add:**
- T30.G3.01 - Connect project ideas to required sensors/actuators

**Rationale:**
- Replace T30.G1.01 with T30.G3.01: Same topic (T30) G3 skill replacing G1 skill
- Remove T30.G1.01: transitive dependency already covered
- Remove T30.GK.02: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 3
- Dependencies added: 1

---

#### T30.G5.02 - Plan safe device-handling procedures for group work

**Current Dependencies:**
- T30.G1.01 (G1)
- T30.G1.02 (G1)
- T30.GK.02 (GK)
- T30.GK.03 (GK)

**Issues Found:**
- Invalid grade: T30.G1.01
- Invalid grade: T30.G1.02
- Transitive dependencies: T30.G1.01, T30.GK.02

**Proposed Dependencies:**
- T30.G3.01 (G3) - Connect project ideas to required sensors/actuators
- T30.GK.03 (GK) - Recognize input vs output examples

**Dependencies to Remove:**
- T30.G1.01
- T30.G1.02
- T30.GK.02

**Dependencies to Add:**
- T30.G3.01 - Connect project ideas to required sensors/actuators

**Rationale:**
- Replace T30.G1.01 with T30.G3.01: Same topic (T30) G3 skill replacing G1 skill
- Remove T30.G1.01: transitive dependency already covered
- Remove T30.GK.02: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 3
- Dependencies added: 1

---

#### T30.G5.03 - Explain how different sensors collect data

**Current Dependencies:**
- T09.G3.01 (G3)
- T30.GK.02 (GK)
- T30.GK.03 (GK)

**Issues Found:**
- Transitive dependencies: T30.GK.02

**Proposed Dependencies:**
- T09.G3.01 (G3) - Create and use a numeric variable for score or count
- T30.GK.03 (GK) - Recognize input vs output examples

**Dependencies to Remove:**
- T30.GK.02

**Rationale:**
- Remove T30.GK.02: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 1
- Dependencies added: 0

---

#### T30.G5.04 - Relate hardware choices to accessibility outcomes

**Current Dependencies:**
- T30.G1.01 (G1)
- T30.G1.02 (G1)
- T30.GK.02 (GK)
- T30.GK.03 (GK)

**Issues Found:**
- Invalid grade: T30.G1.01
- Invalid grade: T30.G1.02
- Transitive dependencies: T30.G1.01, T30.GK.02

**Proposed Dependencies:**
- T30.G3.01 (G3) - Connect project ideas to required sensors/actuators
- T30.GK.03 (GK) - Recognize input vs output examples

**Dependencies to Remove:**
- T30.G1.01
- T30.G1.02
- T30.GK.02

**Dependencies to Add:**
- T30.G3.01 - Connect project ideas to required sensors/actuators

**Rationale:**
- Replace T30.G1.01 with T30.G3.01: Same topic (T30) G3 skill replacing G1 skill
- Remove T30.G1.01: transitive dependency already covered
- Remove T30.GK.02: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 3
- Dependencies added: 1

---

### T31 (1 skills)

#### T31.G5.02 - Decide when apps need the internet vs work offline

**Current Dependencies:**
- T01.G3.01 (G3)
- T30.G3.01 (G3)
- T31.G5.01 (G5)

**Issues Found:**
- Same-grade dependency: T31.G5.01

**Proposed Dependencies:**
- T01.G3.01 (G3) - Complete a simple script with missing blocks
- T30.G3.01 (G3) - Connect project ideas to required sensors/actuators

**Dependencies to Remove:**
- T31.G5.01

**Rationale:**
- WARNING: No G3/G4 replacement found for T31.G5.01 - manual review needed

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 1
- Dependencies added: 0

---

### T32 (3 skills)

#### T32.G5.01 - Analyze social engineering tactics

**Current Dependencies:**
- T32.G1.01 (G1)
- T32.G1.02 (G1)
- T32.GK.02 (GK)
- T32.GK.03 (GK)

**Issues Found:**
- Invalid grade: T32.G1.01
- Invalid grade: T32.G1.02
- Transitive dependencies: T32.G1.01

**Proposed Dependencies:**
- T32.G3.01 (G3) - Explain multi-factor authentication (MFA) with analogies
- T32.GK.02 (GK) - Recognize when to ask for help online
- T32.GK.03 (GK) - Understand that passwords keep things safe

**Dependencies to Remove:**
- T32.G1.01
- T32.G1.02

**Dependencies to Add:**
- T32.G3.01 - Explain multi-factor authentication (MFA) with analogies

**Rationale:**
- Replace T32.G1.01 with T32.G3.01: Same topic (T32) G3 skill replacing G1 skill
- Remove T32.G1.01: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

#### T32.G5.02 - Evaluate terms of service/privacy policies (kid-friendly summaries)

**Current Dependencies:**
- T32.G1.01 (G1)
- T32.G1.02 (G1)
- T32.GK.02 (GK)
- T32.GK.03 (GK)

**Issues Found:**
- Invalid grade: T32.G1.01
- Invalid grade: T32.G1.02
- Transitive dependencies: T32.G1.01

**Proposed Dependencies:**
- T32.G3.01 (G3) - Explain multi-factor authentication (MFA) with analogies
- T32.GK.02 (GK) - Recognize when to ask for help online
- T32.GK.03 (GK) - Understand that passwords keep things safe

**Dependencies to Remove:**
- T32.G1.01
- T32.G1.02

**Dependencies to Add:**
- T32.G3.01 - Explain multi-factor authentication (MFA) with analogies

**Rationale:**
- Replace T32.G1.01 with T32.G3.01: Same topic (T32) G3 skill replacing G1 skill
- Remove T32.G1.01: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

#### T32.G5.03 - Secure AI training data and outputs

**Current Dependencies:**
- T32.G1.01 (G1)
- T32.G1.02 (G1)
- T32.GK.02 (GK)
- T32.GK.03 (GK)

**Issues Found:**
- Invalid grade: T32.G1.01
- Invalid grade: T32.G1.02
- Transitive dependencies: T32.G1.01

**Proposed Dependencies:**
- T32.G3.01 (G3) - Explain multi-factor authentication (MFA) with analogies
- T32.GK.02 (GK) - Recognize when to ask for help online
- T32.GK.03 (GK) - Understand that passwords keep things safe

**Dependencies to Remove:**
- T32.G1.01
- T32.G1.02

**Dependencies to Add:**
- T32.G3.01 - Explain multi-factor authentication (MFA) with analogies

**Rationale:**
- Replace T32.G1.01 with T32.G3.01: Same topic (T32) G3 skill replacing G1 skill
- Remove T32.G1.01: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

### T34 (2 skills)

#### T34.G5.02 - Compare invention timelines in multiple industries

**Current Dependencies:**
- T34.G1.01 (G1)
- T34.G1.02 (G1)
- T34.GK.02 (GK)
- T34.GK.03 (GK)

**Issues Found:**
- Invalid grade: T34.G1.01
- Invalid grade: T34.G1.02
- Transitive dependencies: T34.G1.01

**Proposed Dependencies:**
- T34.G3.01 (G3) - Sequence milestones on a timeline
- T34.GK.02 (GK) - Match old vs new versions of tech
- T34.GK.03 (GK) - Name a person who uses computers in their job

**Dependencies to Remove:**
- T34.G1.01
- T34.G1.02

**Dependencies to Add:**
- T34.G3.01 - Sequence milestones on a timeline

**Rationale:**
- Replace T34.G1.01 with T34.G3.01: Same topic (T34) G3 skill replacing G1 skill
- Remove T34.G1.01: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

#### T34.G5.03 - Conduct interviews with tech users

**Current Dependencies:**
- T34.G1.01 (G1)
- T34.G1.02 (G1)
- T34.GK.02 (GK)
- T34.GK.03 (GK)

**Issues Found:**
- Invalid grade: T34.G1.01
- Invalid grade: T34.G1.02
- Transitive dependencies: T34.G1.01

**Proposed Dependencies:**
- T34.G3.01 (G3) - Sequence milestones on a timeline
- T34.GK.02 (GK) - Match old vs new versions of tech
- T34.GK.03 (GK) - Name a person who uses computers in their job

**Dependencies to Remove:**
- T34.G1.01
- T34.G1.02

**Dependencies to Add:**
- T34.G3.01 - Sequence milestones on a timeline

**Rationale:**
- Replace T34.G1.01 with T34.G3.01: Same topic (T34) G3 skill replacing G1 skill
- Remove T34.G1.01: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

### T35 (3 skills)

#### T35.G5.01 - Examine global impacts of technology

**Current Dependencies:**
- T35.G1.01 (G1)
- T35.G1.02 (G1)
- T35.GK.02 (GK)
- T35.GK.03 (GK)

**Issues Found:**
- Invalid grade: T35.G1.01
- Invalid grade: T35.G1.02
- Transitive dependencies: T35.G1.01

**Proposed Dependencies:**
- T35.G3.01 (G3) - Evaluate digital footprints
- T35.GK.02 (GK) - Recognize signs of too much screen time
- T35.GK.03 (GK) - Practice device sharing etiquette

**Dependencies to Remove:**
- T35.G1.01
- T35.G1.02

**Dependencies to Add:**
- T35.G3.01 - Evaluate digital footprints

**Rationale:**
- Replace T35.G1.01 with T35.G3.01: Same topic (T35) G3 skill replacing G1 skill
- Remove T35.G1.01: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

#### T35.G5.02 - Debate digital well-being scenarios

**Current Dependencies:**
- T35.G1.01 (G1)
- T35.G1.02 (G1)
- T35.GK.02 (GK)
- T35.GK.03 (GK)

**Issues Found:**
- Invalid grade: T35.G1.01
- Invalid grade: T35.G1.02
- Transitive dependencies: T35.G1.01

**Proposed Dependencies:**
- T35.G3.01 (G3) - Evaluate digital footprints
- T35.GK.02 (GK) - Recognize signs of too much screen time
- T35.GK.03 (GK) - Practice device sharing etiquette

**Dependencies to Remove:**
- T35.G1.01
- T35.G1.02

**Dependencies to Add:**
- T35.G3.01 - Evaluate digital footprints

**Rationale:**
- Replace T35.G1.01 with T35.G3.01: Same topic (T35) G3 skill replacing G1 skill
- Remove T35.G1.01: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

#### T35.G5.03 - Analyze AI's differential impacts on workers and communities

**Current Dependencies:**
- T04.G2.01 (G2)
- T35.G1.01 (G1)
- T35.GK.02 (GK)
- T35.GK.03 (GK)

**Issues Found:**
- Invalid grade: T04.G2.01
- Invalid grade: T35.G1.01

**Proposed Dependencies:**
- T04.G3.01 (G3) - Identify where a loop could replace repeated blocks
- T35.G3.01 (G3) - Evaluate digital footprints
- T35.GK.02 (GK) - Recognize signs of too much screen time
- T35.GK.03 (GK) - Practice device sharing etiquette

**Dependencies to Remove:**
- T04.G2.01
- T35.G1.01

**Dependencies to Add:**
- T04.G3.01 - Identify where a loop could replace repeated blocks
- T35.G3.01 - Evaluate digital footprints

**Rationale:**
- Replace T04.G2.01 with T04.G3.01: Same topic (T04) G3 skill replacing G2 skill
- Replace T35.G1.01 with T35.G3.01: Same topic (T35) G3 skill replacing G1 skill

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 2

---

### T36 (1 skills)

#### T36.G5.03 - Evaluate inclusion in tech stories

**Current Dependencies:**
- T36.G1.01 (G1)
- T36.G1.02 (G1)
- T36.GK.02 (GK)
- T36.GK.03 (GK)

**Issues Found:**
- Invalid grade: T36.G1.01
- Invalid grade: T36.G1.02
- Transitive dependencies: T36.G1.01

**Proposed Dependencies:**
- T36.G3.01 (G3) - Conduct empathy interviews for project ideas (ties to T05)
- T36.GK.02 (GK) - Practice sharing and turn-taking with devices
- T36.GK.03 (GK) - Describe what a digital tool helps someone do

**Dependencies to Remove:**
- T36.G1.01
- T36.G1.02

**Dependencies to Add:**
- T36.G3.01 - Conduct empathy interviews for project ideas (ties to T05)

**Rationale:**
- Replace T36.G1.01 with T36.G3.01: Same topic (T36) G3 skill replacing G1 skill
- Remove T36.G1.01: transitive dependency already covered

**Validation:**
- Only valid grades (G3/G4/G5/GK): ✓
- Dependencies removed: 2
- Dependencies added: 1

---

## Implementation Guide

### Phase 1: Simple Fixes (No replacements needed)

Skills where we only remove transitive or same-grade dependencies:

- **T05.G5.03**: Remove T05.GK.03
- **T05.G5.04**: Remove T05.GK.03
- **T30.G5.03**: Remove T30.GK.02
- **T31.G5.02**: Remove T31.G5.01

### Phase 2: Replacement Fixes

Skills where we replace G1/G2 dependencies with G3/G4:

- **T03.G5.01**:
  - Remove: T03.G1.02
  - Add: T03.G3.01
- **T03.G5.03**:
  - Remove: T03.G1.02
  - Add: T03.G3.01
- **T03.G5.04**:
  - Remove: T03.G1.02
  - Add: T03.G3.01
- **T05.G5.01**:
  - Remove: T05.G1.02, T05.GK.03
  - Add: T05.G3.01
- **T05.G5.02**:
  - Remove: T05.G1.02, T05.GK.03
  - Add: T05.G3.01
- **T05.G5.05**:
  - Remove: T04.G2.01, T05.G1.01, T05.GK.03
  - Add: T04.G3.01, T05.G3.01
- **T05.G5.06**:
  - Remove: T05.G1.02, T05.GK.03
  - Add: T05.G3.01
- **T12.G5.02**:
  - Remove: T12.G1.01
  - Add: T12.G3.01
- **T13.G5.04**:
  - Remove: T13.G1.01
  - Add: T13.G4.01
- **T25.G5.01**:
  - Remove: T25.G1.01, T25.GK.02
  - Add: T25.G3.01
- **T25.G5.02**:
  - Remove: T25.G1.01, T25.GK.02
  - Add: T25.G3.01
- **T25.G5.03**:
  - Remove: T25.G1.01, T25.G1.02, T25.GK.02
  - Add: T25.G3.01
- **T30.G5.01**:
  - Remove: T30.G1.01, T30.G1.02, T30.GK.02
  - Add: T30.G3.01
- **T30.G5.02**:
  - Remove: T30.G1.01, T30.G1.02, T30.GK.02
  - Add: T30.G3.01
- **T30.G5.04**:
  - Remove: T30.G1.01, T30.G1.02, T30.GK.02
  - Add: T30.G3.01
- **T32.G5.01**:
  - Remove: T32.G1.01, T32.G1.02
  - Add: T32.G3.01
- **T32.G5.02**:
  - Remove: T32.G1.01, T32.G1.02
  - Add: T32.G3.01
- **T32.G5.03**:
  - Remove: T32.G1.01, T32.G1.02
  - Add: T32.G3.01
- **T34.G5.02**:
  - Remove: T34.G1.01, T34.G1.02
  - Add: T34.G3.01
- **T34.G5.03**:
  - Remove: T34.G1.01, T34.G1.02
  - Add: T34.G3.01
- **T35.G5.01**:
  - Remove: T35.G1.01, T35.G1.02
  - Add: T35.G3.01
- **T35.G5.02**:
  - Remove: T35.G1.01, T35.G1.02
  - Add: T35.G3.01
- **T35.G5.03**:
  - Remove: T04.G2.01, T35.G1.01
  - Add: T04.G3.01, T35.G3.01
- **T36.G5.03**:
  - Remove: T36.G1.01, T36.G1.02
  - Add: T36.G3.01

### Phase 3: Manual Review Required

Skills that may need additional review:

- **T31.G5.02**: Decide when apps need the internet vs work offline
  - WARNING: No G3/G4 replacement found for T31.G5.01 - manual review needed

---

## Validation Checklist

After implementing these fixes, validate the following:

### Automated Checks
- [ ] Re-run `analyze_g5_comprehensive.py` to verify all issues are resolved
- [ ] Verify no new circular dependencies were introduced
- [ ] Verify no new transitive dependencies were created
- [ ] Confirm all G5 skills only depend on G3/G4/G5/GK skills
- [ ] Check that dependency counts match expected values (26 additions, 52 removals)

### Manual Review
- [ ] Review T31.G5.02 - confirm removing T31.G5.01 is pedagogically sound
- [ ] Spot-check 5 random fixed skills to verify replacements make sense
- [ ] Verify G3 replacements provide appropriate prerequisite knowledge
- [ ] Check that cross-topic dependencies (T04, T05, T06, T09, T30) are still valid
- [ ] Confirm no skills are left with zero dependencies that should have some

### Pedagogical Review
- [ ] Review all T05 fixes (6 skills) - major topic with many changes
- [ ] Review all T30 fixes (4 skills) - most dependency removals
- [ ] Verify replacement skills align with curriculum learning progression
- [ ] Confirm G3 skills provide adequate foundation for G5 complexity

---

## Replacement Mappings

This section summarizes which G1/G2 skills are being replaced by which G3/G4 skills.

### Most Common Replacements

| Original G1/G2 Skill | Replacement G3/G4 Skill | Used In | Topics |
|---------------------|------------------------|---------|---------|
| T03.G1.02 | T03.G3.01 | 3 skills | T03 |
| T05.G1.02 | T05.G3.01 | 4 skills | T05 |
| T25.G1.01 | T25.G3.01 | 3 skills | T25 |
| T30.G1.01 | T30.G3.01 | 3 skills | T30 |
| T32.G1.01 | T32.G3.01 | 3 skills | T32 |
| T34.G1.01 | T34.G3.01 | 2 skills | T34 |
| T35.G1.01 | T35.G3.01 | 3 skills | T35 |
| T36.G1.01 | T36.G3.01 | 1 skill | T36 |
| T04.G2.01 | T04.G3.01 | 2 skills | T05, T35 |
| T05.G1.01 | T05.G3.01 | 1 skill | T05 |
| T12.G1.01 | T12.G3.01 | 1 skill | T12 |
| T13.G1.01 | T13.G4.01 | 1 skill | T13 |

### Cross-Topic Replacements

Only 2 skills have cross-topic G2 dependencies that need replacement:

1. **T05.G5.05** depends on **T04.G2.01** → Replace with **T04.G3.01**
2. **T35.G5.03** depends on **T04.G2.01** → Replace with **T04.G3.01**

Both are reasonable as they involve understanding loops (T04) for design and impact analysis.

### Transitive Dependencies to Remove

| Skill Pattern | Transitive to Remove | Via Parent | Count |
|--------------|---------------------|------------|-------|
| T05.G5.* | T05.GK.03 | T05.GK.04 | 6 skills |
| T25.G5.* | T25.GK.02 | T25.GK.03 | 3 skills |
| T30.G5.* | T30.GK.02 | T30.GK.03 | 4 skills |
| T30.G5.* | T30.G1.01 | T30.G1.02 | 3 skills |
| T32.G5.* | T32.G1.01 | T32.G1.02 | 3 skills |
| T34.G5.* | T34.G1.01 | T34.G1.02 | 2 skills |
| T35.G5.* | T35.G1.01 | T35.G1.02 | 2 skills |
| T36.G5.03 | T36.G1.01 | T36.G1.02 | 1 skill |

---

## Implementation Notes

### Recommended Implementation Order

**Week 1: Simple Fixes (4 skills)**
- Day 1: T05.G5.03, T05.G5.04, T30.G5.03 (transitive removals only)
- Day 2: T31.G5.02 (same-grade removal + review)

**Week 2: Single-Topic Replacements (15 skills)**
- Day 1: T03.G5.01, T03.G5.03, T03.G5.04 (all T03.G1.02 → T03.G3.01)
- Day 2: T12.G5.02, T13.G5.04 (simple 1:1 replacements)
- Day 3: T32.G5.01, T32.G5.02, T32.G5.03 (security - all T32.G1.* → T32.G3.01)
- Day 4: T34.G5.02, T34.G5.03 (history)
- Day 5: T36.G5.03 (inclusion)

**Week 3: Complex Fixes (9 skills)**
- Day 1: T25.G5.01, T25.G5.02 (2 changes each)
- Day 2: T25.G5.03 (3 changes)
- Day 3: T30.G5.01, T30.G5.02 (3 changes each)
- Day 4: T30.G5.04 (3 changes)
- Day 5: T35.G5.01, T35.G5.02, T35.G5.03

**Week 4: T05 Topic (6 skills)**
- Day 1: T05.G5.01, T05.G5.02 (2 changes each)
- Day 2: T05.G5.06 (2 changes)
- Day 3: T05.G5.05 (3 changes, cross-topic)
- Day 4-5: Full validation and testing

### Risk Assessment

**Low Risk (17 skills):** Simple 1:1 replacements or transitive removals
- T03.G5.01, T03.G5.03, T03.G5.04
- T05.G5.01, T05.G5.02, T05.G5.03, T05.G5.04, T05.G5.06
- T12.G5.02
- T13.G5.04
- T25.G5.01, T25.G5.02
- T30.G5.03
- T31.G5.02
- T34.G5.02, T34.G5.03
- T36.G5.03

**Medium Risk (9 skills):** Multiple changes or cross-topic dependencies
- T05.G5.05 (3 changes, cross-topic)
- T25.G5.03 (3 changes)
- T30.G5.01, T30.G5.02, T30.G5.04 (3 changes each)
- T32.G5.01, T32.G5.02, T32.G5.03 (multiple changes)
- T35.G5.01, T35.G5.02

**High Risk (2 skills):** Cross-topic G2 dependencies
- T05.G5.05 (depends on T04.G2.01)
- T35.G5.03 (depends on T04.G2.01)

### Expected Outcomes

After implementing all fixes:
- **0 HIGH priority issues** (all G1/G2 dependencies replaced)
- **0 MEDIUM priority issues** (all transitives and same-grade removed)
- **0 LOW priority issues** (none found in original analysis)
- **Total issues:** 0 (down from 64)

---

## Machine-Readable Fix Data

See accompanying `G5_FIX_PLAN.json` for complete machine-readable fix data.

### JSON Structure

```json
{
  "SKILL_ID": {
    "skill_id": "T##.G5.##",
    "skill_name": "Skill name",
    "topic": "T##",
    "current_dependencies": ["list", "of", "current", "deps"],
    "issues": ["list of issues found"],
    "transitive_deps_to_remove": ["list of transitives"],
    "proposed_dependencies": ["final", "dependency", "list"],
    "dependencies_to_remove": ["deps", "to", "remove"],
    "dependencies_to_add": ["deps", "to", "add"],
    "rationale": ["explanation", "of", "changes"],
    "validation": {
      "no_circular_deps": true,
      "no_new_transitives": true,
      "only_valid_grades": true,
      "replacement_count": 1,
      "removal_count": 1
    }
  }
}
```

---

## Appendix: Source Analysis Reports

This fix plan was generated from the following analysis reports:

1. **G5_COMPREHENSIVE_ANALYSIS_REPORT.txt** - Complete technical analysis of all 64 issues
2. **G5_ANALYSIS_EXECUTIVE_SUMMARY.md** - High-level overview and recommendations
3. **G5_AFFECTED_SKILLS_LIST.md** - Complete list of 28 affected skills with details
4. **G5_ANALYSIS_README.md** - Overview of analysis methodology and findings

All source reports are available in: `/media/binyu/USB2/dev/CreatiCodeSkillMap/`

---

## Questions or Issues?

**Generated by:** `generate_g5_fix_plan.py`
**Date:** 2025-11-20
**Skills Database:** `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md` (1204 total skills)

For questions about specific fixes or to report issues with the fix plan, review the detailed specifications for each skill above or consult the machine-readable JSON data.
