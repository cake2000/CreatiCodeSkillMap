# G7 Skills - Top Issues Quick Fix Guide

## Transitive Dependencies to Remove

These dependencies can be safely removed because they're already implied by other dependencies:

### Pattern 1: T01.GK.08 implies T01.GK.07
**Affected Skills (8):** T01.G7.01, T01.G7.02, T01.G7.03, T01.G7.04, T01.G7.05, T01.G7.06, T01.G7.07, T01.G7.08

**Fix:** Remove `T01.GK.07` from dependencies (keep `T01.GK.08`)

### Pattern 2: T02.GK.04 implies T02.GK.03
**Affected Skills (6):** T02.G7.01, T02.G7.02, T02.G7.03, T02.G7.04, T02.G7.05, T02.G7.06

**Fix:** Remove `T02.GK.03` from dependencies (keep `T02.GK.04`)

### Pattern 3: T03.GK.04 implies T03.GK.03
**Affected Skills (6):** T03.G7.01, T03.G7.02, T03.G7.03, T03.G7.04, T03.G7.05, T03.G7.06

**Fix:** Remove `T03.GK.03` from dependencies (keep `T03.GK.04`)

### Pattern 4: T19.G6.04/T19.G6.05 implies T31.G5.01
**Affected Skills (4):** T19.G7.01, T19.G7.02, T19.G7.03, T19.G7.05

**Fix:** Remove `T31.G5.01` from dependencies (keep the G6 dependencies)

### Pattern 5: Various other transitive chains
Many other skills have transitive dependencies to clean up. See full analysis for details.

---

## Missing Dependencies to Add

### Skills Missing T10 (Lists & Tables) Dependencies

These skills mention lists/tables in descriptions but lack T10 dependencies:

1. **T01.G7.05** - Design a set of edge‑case tests for an algorithm
   - Mentions: "algorithm" (likely processes lists)
   - **Add:** T10.G3.01 or T10.G3.02

2. **T02.G7.02** - Extend a simulation trace and predict future behavior
   - Mentions: "trace table"
   - **Add:** T10.G3.01

3. **T02.G7.03** - Create a flowchart for linear search or "find max"
   - Mentions: "scan a list"
   - **Add:** T10.G3.01

4. **T02.G7.04** - Read a flowchart for a simple sort and trace one pass
   - Mentions: "short list"
   - **Add:** T10.G3.01

5. **T17.G7.05** - Tune parameters for realistic motion
   - Mentions: "trial‑and‑error table"
   - **Add:** T10.G3.01 or similar

6. **T23.G7.05** - Build a privacy‑aware voice/vision capture system
   - Mentions: "data is captured"
   - **Add:** T10.G3.01 or T10.G6.04

And 9 more... (see full list in comprehensive analysis)

### Skills Missing T07 (Loops) Dependencies

1. **T16.G7.01** - Build a data collection interface
   - Mentions: likely needs loops to process inputs
   - **Add:** T07.G3.01

2. **T18.G7.01** - Plan a level with interconnected rooms or zones
   - Mentions: may need loops for room processing
   - **Add:** T07.G3.01 (verify if actually needed)

And 6 more...

### Skills Missing T09 (Variables) Dependencies

1. **T16.G7.03** - Design an accessible interface for users with different abilities
   - Mentions: likely needs state variables
   - **Add:** T09.G3.01

2. **T18.G7.05** - Script camera transitions for cutscenes
   - Mentions: camera state
   - **Add:** T09.G3.01

And 3 more...

### Skills Missing T08 (Conditions) Dependencies

1. **T02.G7.06** - Trace an algorithm to find a bug or edge case
   - Mentions: "incorrect condition"
   - **Add:** T08.G3.01 or T08.G6.03

2. **T28.G7.05** - Validate model outputs against known data
   - Mentions: conditional logic for validation
   - **Add:** T08.G3.01

And 1 more...

---

## Overly Broad Skills to Review

### 1. T02.G7.01 - Trace a step‑by‑step simulation algorithm
**Issue:** Uses "several timesteps" (vague quantity)

**Recommendation:** Either:
- Specify: "trace 3-5 timesteps" or "trace until stable state"
- Or accept as is if flexibility is intentional

### 2. T28.G7.01 - Design a simple climate model
**Issue:** Uses "various factors"

**Recommendation:** Either:
- Specify: "2-3 factors such as temperature and precipitation"
- Or break into sub-skills for different complexity levels

### 3. T28.G7.02 - Model interconnected system components
**Issue:** Uses "multiple components"

**Recommendation:** Either:
- Specify: "2-4 components with clear interactions"
- Or provide examples of what "interconnected" means

---

## Quick Win: Automated Transitive Dependency Cleanup

The most common issue (116 occurrences) could be addressed with a script:

```python
# Pseudo-code for automated cleanup
for skill in g7_skills:
    for dep_a in skill.dependencies:
        for dep_b in skill.dependencies:
            if dep_b in get_dependencies(dep_a):
                # dep_b is implied by dep_a, can remove
                skill.dependencies.remove(dep_b)
```

This would clean up ~77% of all issues automatically.

---

## Manual Review Needed

The following require human judgment:

1. **Missing dependencies** - Need to verify if the skill actually requires the missing topic
2. **Overly broad skills** - Need to decide if specificity is needed or flexibility is intentional
3. **Cross-topic dependencies** - Verify that dependencies like T19→T31 make logical sense

---

## Impact Analysis

**If all transitive dependencies are removed:**
- 116 skills become cleaner and easier to understand
- Average dependencies per skill drops from ~4.5 to ~3.2
- Dependency graph becomes easier to visualize and maintain

**If missing dependencies are added:**
- 31 skills gain more accurate prerequisite information
- Skill paths become clearer for learners
- Potential for better prerequisite checking in implementation

**If overly broad skills are clarified:**
- 3 skills become more measurable and testable
- Assessment design becomes easier
- Learning objectives become more precise

---

## Priority Order for Fixes

1. **First:** Remove transitive dependencies (low risk, high impact, can automate)
2. **Second:** Review and add missing loop/variable/condition dependencies (medium effort, medium impact)
3. **Third:** Review and add missing list dependencies (requires more domain knowledge)
4. **Last:** Clarify overly broad skills (lowest priority, highest subjectivity)

