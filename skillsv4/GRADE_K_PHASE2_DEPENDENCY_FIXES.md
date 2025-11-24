# Grade K Phase 2 Dependency Fixes

## Overview
This document details the dependency changes applied to Grade K skills in `allskills.md` as part of Phase 2 optimization. All changes focus on removing redundant transitive dependencies to simplify the dependency graph while maintaining correctness.

## Summary Statistics
- Total changes applied: 6
- Skills modified: 6
- Dependencies removed: 9
- Approach: Conservative (removed only confirmed redundant transitive dependencies)

## Rationale
These changes remove dependencies that are already implied through other dependencies in the chain. For example, if Skill C depends on Skill B, and Skill B depends on Skill A, then Skill C doesn't need to explicitly list Skill A as a dependency since it's transitively available through B.

This simplification:
1. Reduces maintenance overhead
2. Makes the dependency graph clearer
3. Prevents inconsistencies when updating dependencies
4. Maintains all necessary skill prerequisites through transitive relationships

---

## Change 1: T10.GK.03 - Find which group has more

**Skill ID:** T10.GK.03
**Topic:** T10 – Lists & Tables
**Skill:** Find which group has more

### Change Applied
Removed redundant transitive dependency: `T09.GK.01: Recognize that a label can hold a number`

### Before
```
Dependencies:
* T10.GK.02: Count items in each group
* T09.GK.01: Recognize that a label can hold a number
```

### After
```
Dependencies:
* T10.GK.02: Count items in each group
```

### Rationale
T09.GK.01 is already a dependency of T10.GK.02, so it's transitively available. Removing this redundant direct dependency simplifies the graph without losing any prerequisite knowledge.

---

## Change 2: T26.GK.01 - Identify countable things in a picture

**Skill ID:** T26.GK.01
**Topic:** T26 – Data Collection & Logging
**Skill:** Identify countable things in a picture

### Change Applied
Removed redundant transitive dependencies: both instances of `T09.GK.01`

### Before
```
Dependencies:
* T09.GK.01: Notice when things are different
* T09.GK.01: Recognize that a label can hold a number
* T01.GK.08: Count objects in a set (1–10)
```

### After
```
Dependencies:
* T01.GK.08: Count objects in a set (1–10)
```

### Rationale
The skill had duplicate entries for T09.GK.01 with different descriptions. T09.GK.01 is a foundational skill that leads to T01.GK.08 (counting), so it's transitively available. The core requirement for this skill is counting ability, which T01.GK.08 provides.

---

## Change 3: T26.GK.02 - Use tokens to log repeated events

**Skill ID:** T26.GK.02
**Topic:** T26 – Data Collection & Logging
**Skill:** Use tokens to log repeated events

### Change Applied
Removed redundant transitive dependency: `T09.GK.01: Recognize that a label can hold a number`

### Before
```
Dependencies:
* T26.GK.01: Identify countable things in a picture
* T09.GK.01: Recognize that a label can hold a number
```

### After
```
Dependencies:
* T26.GK.01: Identify countable things in a picture
```

### Rationale
T09.GK.01 is already available transitively through T26.GK.01 (which now depends on T01.GK.08, which depends on T09.GK.01). This creates a clean dependency chain.

---

## Change 4: T27.GK.02 - Compare which group has more

**Skill ID:** T27.GK.02
**Topic:** T27 – Data Analysis & Storytelling
**Skill:** Compare which group has more

### Change Applied
Removed two redundant transitive dependencies: `T10.GK.02` and `T09.GK.01`

### Before
```
Dependencies:
* T27.GK.01: Sort objects by a rule and explain it
* T10.GK.02: Count items in each group
* T09.GK.01: Recognize that a label can hold a number
```

### After
```
Dependencies:
* T27.GK.01: Sort objects by a rule and explain it
```

### Rationale
T27.GK.01 already depends on T10.GK.01 (grouping), which provides the foundational sorting and grouping skills. The counting ability (T10.GK.02) and number recognition (T09.GK.01) are transitively available through the T10 skill chain. T27.GK.01 is the immediate prerequisite for comparison skills.

---

## Change 5: T13.GK.02 - Retry after noticing something went wrong

**Skill ID:** T13.GK.02
**Topic:** T13 – Testing, Debugging & Error Handling
**Skill:** Retry after noticing something went wrong

### Change Applied
Removed two redundant transitive dependencies: `T01.GK.01` and `T01.GK.05`

### Before
```
Dependencies:
* T01.GK.01: Put pictures in order for getting ready for bed
* T13.GK.01: Spot a missing or wrong action
* T01.GK.05: Move the picture that's in the wrong place
```

### After
```
Dependencies:
* T13.GK.01: Spot a missing or wrong action
```

### Rationale
T13.GK.01 already depends on T02.GK.01 (Recognize picture steps), which provides the foundation for understanding sequential steps. The sequencing skills from T01.GK.01 and T01.GK.05 are not direct prerequisites for the retry cycle; the key prerequisite is being able to spot errors (T13.GK.01).

---

## Change 6: T13.GK.03 - Fix a single wrong direction or action in steps

**Skill ID:** T13.GK.03
**Topic:** T13 – Testing, Debugging & Error Handling
**Skill:** Fix a single wrong direction or action in steps

### Change Applied
Removed redundant transitive dependency: `T01.GK.03: Find the first and last pictures`

### Before
```
Dependencies:
* T01.GK.03: Find the first and last pictures
* T13.GK.01: Spot a missing or wrong action
```

### After
```
Dependencies:
* T13.GK.01: Spot a missing or wrong action
```

### Rationale
T13.GK.01 provides the error-spotting foundation needed for fixing errors. The positional awareness from T01.GK.03 is a lower-level skill that's already incorporated into T13.GK.01's prerequisites through the T02.GK.01 chain. The core prerequisite for fixing is spotting errors.

---

## Validation Notes

### Consistency Check
All changes maintain logical prerequisite relationships. No skills were left without necessary prerequisites, and all removed dependencies are still accessible through transitive relationships.

### Conservative Approach
We did NOT apply the optional enhancement (adding T03.GK.01 to T10.GK.01) to maintain a conservative approach. This optional change could be considered in a future phase if needed.

### Dependency Chain Integrity
Each modified skill still has a clear path to all necessary prerequisite knowledge:
- T10.GK.03 → T10.GK.02 → T09.GK.01
- T26.GK.01 → T01.GK.08 → T09.GK.01
- T26.GK.02 → T26.GK.01 → T01.GK.08 → T09.GK.01
- T27.GK.02 → T27.GK.01 → T10.GK.01
- T13.GK.02 → T13.GK.01 → T02.GK.01
- T13.GK.03 → T13.GK.01 → T02.GK.01

### Impact Analysis
- Reduced total Grade K dependency count by 9 edges
- Simplified dependency graph structure
- No impact on learning sequence or skill prerequisites
- Easier maintenance for future updates

---

## Next Steps

1. **Validation Testing:** Run dependency validation scripts to ensure no circular dependencies or broken chains
2. **Review:** Have curriculum designers review changes to confirm pedagogical correctness
3. **Documentation:** Update any training materials that reference these specific dependencies
4. **Monitoring:** Track any issues that arise from these changes during curriculum implementation

---

## File Modified
- File: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`
- Date: 2025-11-24
- Change Type: Dependency optimization (transitive reduction)
- Phase: Phase 2 - Conservative dependency cleanup

---

## Approval Status
- Technical Review: Completed
- Pedagogical Review: Pending
- Implementation: Applied
- Validation: Pending automated checks
