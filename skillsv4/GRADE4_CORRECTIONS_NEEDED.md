# Grade 4 Corrections Needed

This document lists the specific corrections needed to complete the Grade 4 dependency validation.

## Invalid Dependency IDs (6 issues)

These dependencies reference skills that don't exist. The correct IDs are listed below:

### 1. T16.G4.03 -> T10.G3.01
**Issue:** T10.G3.01 doesn't exist (has sub-skills)
**Suggested fix:** Replace with T10.G3.01.01 and/or T10.G3.01.02 (both exist)

### 2. T18.G4.01.01 -> T09.G3.01
**Issue:** T09.G3.01 doesn't exist (has sub-skills)
**Suggested fix:** Replace with one or more of:
- T09.G3.01.01
- T09.G3.01.02
- T09.G3.01.03
- T09.G3.01.04
- T09.G3.01.05

### 3. T18.G4.01.01 -> T14.G3.01
**Issue:** T14.G3.01 doesn't exist (has sub-skills)
**Suggested fix:** Replace with T14.G3.01.01 and/or T14.G3.01.02

### 4. T25.G4.06 -> T10.G3.01
**Issue:** T10.G3.01 doesn't exist (has sub-skills)
**Suggested fix:** Replace with T10.G3.01.01 and/or T10.G3.01.02

### 5. T26.G4.06 -> T26.G4.02
**Issue:** T26.G4.02 doesn't exist (has sub-skills)
**Suggested fix:** Replace with T26.G4.02.01 and/or T26.G4.02.02

### 6. T27.G4.01 -> T26.G3.04
**Issue:** T26.G3.04 doesn't exist (has sub-skills)
**Suggested fix:** Replace with T26.G3.04.01 and/or T26.G3.04.02

## Self-Referential Dependencies (6 issues)

These skills list themselves as dependencies, which creates circular references:

### 1. T08.G4.00 depends on T08.G4.00
**Fix:** Remove T08.G4.00 from its own dependencies list

### 2. T08.G4.01 depends on T08.G4.01
**Fix:** Remove T08.G4.01 from its own dependencies list

### 3. T08.G4.03 depends on T08.G4.03
**Fix:** Remove T08.G4.03 from its own dependencies list

### 4. T08.G4.05 depends on T08.G4.05
**Fix:** Remove T08.G4.05 from its own dependencies list

### 5. T09.G4.02.01 depends on T09.G4.02.01
**Fix:** Remove T09.G4.02.01 from its own dependencies list

### 6. T27.G4.03 depends on T27.G4.03
**Fix:** Remove T27.G4.03 from its own dependencies list

## Root Cause Analysis

All 6 invalid dependency issues are caused by the same problem: **referencing parent skills that have been subdivided into sub-skills.**

When a skill like T10.G3.01 has sub-skills (T10.G3.01.01, T10.G3.01.02), the parent ID (T10.G3.01) no longer exists as a standalone skill. Dependencies must reference the specific sub-skill(s) needed.

## Recommended Approach

For each invalid reference, replace with the **first sub-skill** (the most foundational one):
- T09.G3.01 → T09.G3.01.01
- T10.G3.01 → T10.G3.01.01
- T14.G3.01 → T14.G3.01.01
- T26.G3.04 → T26.G3.04.01
- T26.G4.02 → T26.G4.02.01

Alternatively, if multiple sub-skills are needed, include all relevant sub-skills in the dependency list.

## Priority

**High Priority (can be automated):**
- Self-referential dependencies - simple deletions
- Parent skill references - replace with .01 sub-skill

**All 12 corrections can be done with find-and-replace operations.**

---
*Generated: 2025-11-24*
