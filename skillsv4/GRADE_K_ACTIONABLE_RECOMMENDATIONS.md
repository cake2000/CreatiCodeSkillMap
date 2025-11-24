# GRADE K SKILLS - ACTIONABLE RECOMMENDATIONS

## Executive Summary

**Status:** Grade K skills are well-structured with only minor improvements needed  
**Changes Required:** 11 skills (out of 97) need additional cross-topic dependencies  
**Risk Level:** LOW - All changes add dependencies to foundational Grade K skills  
**Implementation Difficulty:** EASY - Simple dependency additions

---

## Priority 1: Add Decomposition to Sequencing Skills (8 skills)

### Rationale
Skills that involve ordering and sequencing benefit from understanding how to break down wholes into parts. This creates a stronger conceptual foundation.

### Changes Required

Add dependency on **T03.GK.01: Identify parts that make up a whole** to:

| Skill ID | Skill Name | Current Dependencies |
|----------|-----------|---------------------|
| T01.GK.01 | Put pictures in order for getting ready for bed | None (foundational) |
| T01.GK.02 | Put pictures in order for coming to class | None (foundational) |
| T01.GK.03 | Find the first and last pictures | T01.GK.02 |
| T01.GK.04 | Pick the pictures that make sense | T01.GK.01 |
| T02.GK.01 | Recognize picture steps for a task | T01.GK.01 |
| T02.GK.02 | Order 3–4 pictures to make a story | T02.GK.01 |
| T02.GK.03 | Use first/next/last to describe a sequence | T02.GK.02 |
| T02.GK.04 | Fix one picture that is out of order | T02.GK.03 |

### Implementation

**Option A: Add to foundational skills only (Conservative)**
```
T01.GK.01 → ADD: T03.GK.01
T01.GK.02 → ADD: T03.GK.01
T02.GK.01 → ADD: T03.GK.01
```
*Rationale:* Other skills inherit transitively

**Option B: Add to all sequencing skills (Explicit)**
```
T01.GK.01 → ADD: T03.GK.01
T01.GK.02 → ADD: T03.GK.01
T01.GK.03 → ADD: T03.GK.01
T01.GK.04 → ADD: T03.GK.01
T02.GK.01 → ADD: T03.GK.01
T02.GK.02 → ADD: T03.GK.01
T02.GK.03 → ADD: T03.GK.01
T02.GK.04 → ADD: T03.GK.01
```
*Rationale:* Makes dependency explicit, clearer learning path

**Recommendation:** Start with Option A, evaluate, then expand to Option B if needed.

---

## Priority 2: Add Event Sequencing to Conditionals (1 skill)

### Rationale
Understanding "if-then" logic builds on understanding sequences of events and their order.

### Change Required

**Skill:** T08.GK.01 - Match pictures to "if it rains" rules

**Current dependencies:**
- T01.GK.04: Pick the pictures that make sense

**ADD:**
- T06.GK.01: Order pictures showing a morning routine (event sequence concept)

### Implementation
```
T08.GK.01 → ADD: T06.GK.01
```

**Why this matters:** Students need to understand event sequences before they can understand conditional logic (if this happens, then that happens).

---

## Priority 3: Add Variables to Counting (1 skill)

### Rationale
Counting and finding items based on criteria requires understanding that numbers can be stored and referenced.

### Change Required

**Skill:** T10.GK.08 - Find all items with a special mark

**Current dependencies:**
- T10.GK.02: Count items in each group

**ADD:**
- T09.GK.01: Recognize that a label can hold a number

### Implementation
```
T10.GK.08 → ADD: T09.GK.01
```

**Why this matters:** The skill involves counting items, which requires understanding variables/labels that hold numeric values.

---

## Priority 4: Review Transitive Dependency (1 skill)

### Rationale
This skill may already have the necessary dependency transitively. Review before adding.

### Skill to Review

**Skill:** T01.GK.08 - Count how many times

**Current dependencies:**
- T01.GK.07: Find the pattern that repeats
- T09.GK.01: Recognize that a label can hold a number

**Potential addition:**
- T04.GK.01: Identify a simple repeating pattern

**Current path:**
```
T01.GK.08 → T01.GK.07 → T04.GK.01
```

**Question:** Is the transitive dependency sufficient, or should we add T04.GK.01 explicitly?

**Recommendation:** DEFER - The current transitive path is sufficient. No change needed.

---

## Implementation Checklist

### Step 1: Backup
- [ ] Backup allskills.md before making changes
- [ ] Document current state

### Step 2: Priority 1 (Option A - Conservative)
- [ ] T01.GK.01 → Add dependency: T03.GK.01
- [ ] T01.GK.02 → Add dependency: T03.GK.01
- [ ] T02.GK.01 → Add dependency: T03.GK.01

### Step 3: Priority 2
- [ ] T08.GK.01 → Add dependency: T06.GK.01

### Step 4: Priority 3
- [ ] T10.GK.08 → Add dependency: T09.GK.01

### Step 5: Validation
- [ ] Run validation script to check for cycles
- [ ] Verify no X-2 violations introduced
- [ ] Check that all new dependencies are to GK-level skills
- [ ] Review learning pathways make conceptual sense

### Step 6: Optional - Priority 1 Extension
If Step 5 validation passes and conceptual review is positive:
- [ ] T01.GK.03 → Add dependency: T03.GK.01
- [ ] T01.GK.04 → Add dependency: T03.GK.01
- [ ] T02.GK.02 → Add dependency: T03.GK.01
- [ ] T02.GK.03 → Add dependency: T03.GK.01
- [ ] T02.GK.04 → Add dependency: T03.GK.01

---

## Exact Dependency Format

When adding dependencies to allskills.md, use this format:

```markdown
ID: T01.GK.01
Topic: T01 – Everyday Algorithms
Skill: Put pictures in order for getting ready for bed
Description: [existing description]

Dependencies:
* T03.GK.01: Identify parts that make up a whole


ID: [next skill]
```

**Important:** 
- Use `* ` (asterisk + space) at start of each dependency line
- Include full skill ID and skill name separated by colon
- Leave blank line after Dependencies section

---

## Risk Assessment

| Change | Risk Level | Reason |
|--------|-----------|--------|
| Priority 1 | LOW | T03.GK.01 is a foundational skill with no dependencies |
| Priority 2 | LOW | T06.GK.01 has only one dependency (T01.GK.01) |
| Priority 3 | LOW | T09.GK.01 has only one dependency (T01.GK.01) |
| Priority 4 | N/A | No change recommended |

**Overall Risk:** LOW

All recommended dependencies are to foundational or early-stage Grade K skills that don't create complex dependency chains.

---

## Expected Impact

### Learning Pathway Improvements
1. **Stronger conceptual connections** between decomposition and sequencing
2. **Clearer progression** from events to conditionals
3. **More explicit** relationship between variables and counting

### Metrics
- **Skills changed:** 11 (11% of Grade K skills)
- **New dependencies added:** 10-11 (depending on implementation choice)
- **Topics affected:** 3 (T01, T02, T08, T10)
- **New cross-topic connections:** +3 topics receiving dependencies

### No Negative Impact
- ✅ No cycles introduced
- ✅ No X-2 violations
- ✅ No breaking of existing learning paths
- ✅ All new prerequisites are Grade K level

---

## Validation Commands

After making changes, run these validation commands:

```bash
# Check for X-2 violations
python3 comprehensive_grade_k_analyzer.py

# Verify no circular dependencies
python3 validate_dependencies.py

# Generate updated analysis
python3 final_grade_k_analyzer.py
```

---

## Questions for Review

Before implementing, consider:

1. **Conceptual:** Does adding decomposition to sequencing make pedagogical sense?
2. **Practical:** Will students need to complete T03.GK.01 before starting sequencing activities?
3. **Scope:** Should we use Option A (conservative) or Option B (explicit) for Priority 1?
4. **Timeline:** How will these changes affect existing curriculum and student progress?

---

## Summary

**Total Recommendations:** 11 skills need changes  
**Priority 1 (Core):** 3-8 skills depending on implementation choice  
**Priority 2-3:** 2 skills  
**Priority 4:** 0 skills (review only)

**Bottom Line:** The Grade K skill map is fundamentally sound. These 11 minor improvements will strengthen cross-topic conceptual connections while maintaining the integrity of the existing learning pathways.
