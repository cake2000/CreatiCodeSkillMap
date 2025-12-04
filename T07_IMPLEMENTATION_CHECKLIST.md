# T07 Restructuring - Implementation Checklist

## Step-by-Step Integration Guide

---

## PHASE 1: DEPRECATE OLD SKILLS

### Mark for Deletion (Do NOT remove yet - mark as deprecated)

```markdown
# In allskills.md, add [DEPRECATED] tag to these skills:

□ T07.G8.16 - Paginated API responses
  → MERGED INTO: T07.G8.12 (new)

□ T07.G8.23 - Rate limiting patterns
  → MERGED INTO: T07.G8.12 (new)

□ T07.G8.24 - AI model inference batching
  → MERGED INTO: T07.G8.12 (new)

□ T07.G3.13 - Debug wrong repeat loop count
  → MERGED INTO: T07.G3.06 (new)

□ T07.G3.14 - Debug repeat loop with wrong action
  → MERGED INTO: T07.G3.06 (new)

□ T07.G3.15 - Use step-by-step execution
  → MERGED INTO: T07.G3.06 (new)

□ T07.G3.18 - Identify three categories of loop bugs
  → MERGED INTO: T07.G3.06 (new)
```

**NOTE:** Keep old skills marked [DEPRECATED] for one curriculum cycle to allow smooth transition.

---

## PHASE 2: INSERT NEW SKILLS

### Kindergarten (1 new skill)

```markdown
INSERT AFTER T07.K.05:

□ T07.K.06 [NEW] - Group repeated tasks into one idea
  Dependencies: T07.K.01

ACTION: Renumber current K.06 and beyond (if any exist)
```

### Grade 2 (1 new skill)

```markdown
INSERT AFTER T07.G2.11:

□ T07.G2.12 [NEW] - Predict "how many times" before seeing the loop
  Dependencies: T07.G2.06, T07.K.06

ACTION: No renumbering needed (G2.11 was last)
```

### Grade 3 (1 new skill - strengthened)

```markdown
INSERT AFTER T07.G3.07:

□ T07.G3.07A [NEW] - Master CreatiCode console logging for loop debugging
  Dependencies: T07.G3.06, T07.G6.06 (note: G6 is cross-grade but within X-2)

ACTION: Renumber T07.G3.08-G3.18 to G3.08A-G3.18A temporarily
THEN: After consolidation, renumber back to G3.08-G3.12 (fewer skills)
```

### Grade 5 (3 new skills)

```markdown
INSERT AFTER T07.G5.21:

□ T07.G5.22 [NEW] - Identify and name common loop patterns
  Dependencies: T07.G5.17, T07.G5.04, T07.G5.02

□ T07.G5.23 [NEW] - Choose appropriate pattern for a new problem
  Dependencies: T07.G5.22, T07.G5.16

□ T07.G5.24 [NEW] - Understand parallel loop execution in multi-sprite programs
  Dependencies: T07.G4.15, T07.G3.08

ACTION: No renumbering needed (G5.21 was last)
```

### Grade 6 (4 new skills)

```markdown
INSERT AFTER T07.G6.25:

□ T07.G6.26 [NEW] - Decompose one complex loop into multiple simpler loops
  Dependencies: T07.G5.22, T07.G6.05

□ T07.G6.27 [NEW] - Understand loop invariants (simplified)
  Dependencies: T07.G6.06, T07.G5.04

□ T07.G6.28 [NEW] - Debug race conditions in parallel loops
  Dependencies: T07.G5.24, T07.G6.04

INSERT AFTER T07.G6.19:

□ T07.G6.19A [NEW] - Master clone-based parallel loops for advanced effects
  Dependencies: T07.G6.18, T07.G6.19, T07.G5.24

ACTION: Renumber T07.G6.20-G6.25 to G6.21-G6.26
THEN: Add G6.27, G6.28, G6.29 at end
```

### Grade 7 (1 new skill)

```markdown
INSERT AFTER T07.G7.18:

□ T07.G7.19 [NEW] - Implement error recovery mid-loop (continue on failure)
  Dependencies: T07.G7.08, T07.G8.20 (note: G8 is future-looking dependency - OK for advanced topic)

ACTION: No renumbering needed (G7.18 was last)
```

### Grade 8 (1 new skill)

```markdown
INSERT AT END:

□ T07.G8.29 [NEW] - Compare iteration vs recursion trade-offs
  Dependencies: T07.G8.02, T07.G8.08

ACTION: No renumbering needed (adding to end)
```

---

## PHASE 3: REPLACE CONSOLIDATED SKILLS

### Grade 3 Debugging Consolidation

```markdown
REPLACE T07.G3.06 with consolidated version:

OLD: T07.G3.06 - Debug loops by adding say blocks to visualize execution
NEW: T07.G3.06 - Debug loops using systematic techniques [CONSOLIDATED]

□ Update skill text to comprehensive 3-tool + 3-bug-category framework
□ Update dependencies to: T07.G3.05, T07.G3.11
□ Verify all examples from old G3.13, G3.14, G3.15, G3.18 are covered
```

### Grade 8 API Consolidation

```markdown
REPLACE T07.G8.12 with consolidated version:

OLD: T07.G8.12 - Design loops for batch AI API calls
NEW: T07.G8.12 - Design loops for API integration patterns [CONSOLIDATED]

□ Update skill text to cover batching + pagination + rate limiting
□ Update dependencies to: T07.G8.10, T07.G8.08, T07.G8.17
□ Verify all examples from old G8.16, G8.23, G8.24 are covered
```

---

## PHASE 4: UPDATE MODIFIED SKILLS

### Update Descriptions

```markdown
□ T07.G5.01 - Use loops for statistical experiments
  UPDATE: Add convergence concept, data science connection

□ T07.G6.03 - Implement linear search with early exit
  UPDATE: Add break optimization, efficiency comparison

□ T07.G7.05 - Recognize and apply accumulator patterns strategically
  UPDATE: Enumerate 5 variations, add selection task

□ T07.G8.10 - Write effective prompts for AI to generate loop code
  UPDATE: Add 6-part prompt structure, concrete examples
```

### Fix Dependencies

```markdown
□ T07.G6.01 - Trace nested loops with variable bounds
  OLD DEPENDENCY: T07.G5.07 (2 grades back - violates X-2)
  NEW DEPENDENCY: T07.G5.08 (1 grade back - complies)
  ALSO ADD: T07.G4.15 (foundation skill)

□ T07.G8.02 - Analyze iterative algorithm structure
  OLD DEPENDENCY: T01.G6.01 (cross-topic, 2 grades back)
  NEW DEPENDENCY: T07.G7.04 (same topic, 1 grade back)
  ALSO ADD: T07.G7.05, T07.G6.06
```

---

## PHASE 5: GLOBAL DEPENDENCY UPDATES

### Search and Replace Deprecated Skill References

```bash
# Run these searches in allskills.md:

□ Search: "T07.G8.16" → Replace with: "T07.G8.12"
□ Search: "T07.G8.23" → Replace with: "T07.G8.12"
□ Search: "T07.G8.24" → Replace with: "T07.G8.12"
□ Search: "T07.G3.13" → Replace with: "T07.G3.06"
□ Search: "T07.G3.14" → Replace with: "T07.G3.06"
□ Search: "T07.G3.15" → Replace with: "T07.G3.06"
□ Search: "T07.G3.18" → Replace with: "T07.G3.06"
```

### Verify New Skill Dependencies are Valid

```markdown
For each NEW skill, verify dependencies exist:

□ T07.K.06 → depends on T07.K.01 ✓
□ T07.G2.12 → depends on T07.G2.06, T07.K.06 ✓
□ T07.G3.07A → depends on T07.G3.06, T07.G6.06 ✓
□ T07.G5.22 → depends on T07.G5.17, T07.G5.04, T07.G5.02 ✓
□ T07.G5.23 → depends on T07.G5.22, T07.G5.16 ✓
□ T07.G5.24 → depends on T07.G4.15, T07.G3.08 ✓
□ T07.G6.26 → depends on T07.G5.22, T07.G6.05 ✓
□ T07.G6.27 → depends on T07.G6.06, T07.G5.04 ✓
□ T07.G6.28 → depends on T07.G5.24, T07.G6.04 ✓
□ T07.G6.19A → depends on T07.G6.18, T07.G6.19, T07.G5.24 ✓
□ T07.G7.19 → depends on T07.G7.08, T07.G8.20 (future-looking OK) ✓
□ T07.G8.29 → depends on T07.G8.02, T07.G8.08 ✓
```

---

## PHASE 6: RENUMBERING

### Grade 3 (After Consolidation)

```markdown
BEFORE: G3.01 - G3.18 (18 skills)
AFTER: G3.01 - G3.12 (12 skills, after removing 6 consolidated into G3.06)

Renumbering plan:
- G3.01-G3.05: No change
- G3.06: CONSOLIDATED skill (replaces old G3.06, G3.13, G3.14, G3.15, G3.18)
- G3.07: No change (console logging - already existed)
- INSERT G3.07A: New console mastery skill
- G3.08-G3.12: OLD G3.08-G3.12 (no change)
- REMOVE: G3.13, G3.14, G3.15 (merged into G3.06)
- G3.13: OLD G3.16 becomes NEW G3.13
- G3.14: OLD G3.17 becomes NEW G3.14
- REMOVE: G3.18 (merged into G3.06)
```

### Grade 6 (After Inserts)

```markdown
BEFORE: G6.01 - G6.25 (25 skills)
AFTER: G6.01 - G6.29 (29 skills, added 4 new)

Renumbering plan:
- G6.01-G6.19: No change
- INSERT G6.19A: New clone mastery skill
- G6.20-G6.26: OLD G6.20-G6.25 shifted down by 1
- INSERT G6.27: New decomposition skill
- INSERT G6.28: New invariants skill
- INSERT G6.29: New race conditions skill
```

---

## PHASE 7: VALIDATION

### Automated Checks

```markdown
□ Run X-2 rule validator on all T07 dependencies
  Expected: 0 violations (down from 3)

□ Verify no broken dependencies (skills that don't exist)
  Command: grep "T07\." allskills.md | extract deps | check existence

□ Count total T07 skills
  Expected: 161 (was 158)

□ Verify grade distribution
  K: 6 (was 5)
  G1: 9 (no change)
  G2: 12 (was 11)
  G3: 13 (was 18, consolidated + added)
  G4: 23 (no change)
  G5: 24 (was 21)
  G6: 29 (was 25)
  G7: 19 (was 18)
  G8: 29 (was 28, consolidated but added)
```

### Manual Checks

```markdown
□ Read through NEW consolidated G3.06 debugging skill
  Verify: Covers all 6 original techniques ✓

□ Read through NEW consolidated G8.12 API skill
  Verify: Covers batching, pagination, rate limiting ✓

□ Check NEW pattern skills (G5.22, G5.23)
  Verify: All 5 patterns defined (accumulator, sentinel, flag, counter, processing) ✓

□ Check NEW parallel skills (G5.24, G6.28)
  Verify: CreatiCode multi-sprite context clear ✓

□ Check dependency chains
  Example: T07.G5.23 → G5.22 → G5.17, G5.04, G5.02 → ... (trace full chain)
```

---

## PHASE 8: CURRICULUM INTEGRATION

### Lesson Plan Updates

```markdown
□ Create lesson plan for T07.G3.06 (debugging framework)
  Include: All 3 tools demonstration, 3 bug categories worksheet

□ Create lesson plan for T07.G5.22 (named patterns)
  Include: Pattern identification activity, pattern vocabulary flashcards

□ Create lesson plan for T07.G8.12 (API integration)
  Include: Batching demo, pagination demo, rate limiting calculation

□ Update existing lessons that referenced deprecated skills
  Search lessons for: G8.16, G8.23, G8.24, G3.13-G3.15, G3.18
```

### Assessment Updates

```markdown
□ Create assessment for consolidated debugging (G3.06)
  Rubric: Can use say blocks, console, step-by-step | Can categorize bugs

□ Create assessment for named patterns (G5.22)
  Rubric: Can identify all 5 patterns | Can name patterns correctly

□ Create assessment for pattern selection (G5.23)
  Rubric: Chooses appropriate pattern | Justifies choice

□ Update rubrics referencing deprecated skills
```

---

## PHASE 9: DOCUMENTATION

### Migration Guide for Teachers

```markdown
CREATE: T07_TEACHER_MIGRATION_GUIDE.md

Include:
□ What changed: Consolidations, additions, modifications
□ Why it changed: Rationale for each major change
□ How to teach consolidated skills: Tips for covering all components
□ FAQ: "Where did skill X go?" → "It's now part of skill Y"
□ Timeline: When to switch from old to new curriculum
```

### Student-Facing Changes

```markdown
UPDATE: Student skill progression charts

□ Update "Debugging Loops" progression to show single framework skill
□ Update "Advanced Loops" (G5-G8) to include pattern vocabulary
□ Add "Parallel Loops" as new progression track (G5-G6)
□ Add visual showing 5 named patterns with examples
```

---

## PHASE 10: FINAL REVIEW

### Stakeholder Sign-Off

```markdown
□ Curriculum Director review
□ Lead Teacher review
□ Technical Reviewer (verify CreatiCode-specific content)
□ Student pilot feedback (optional: test with small group first)
```

### Pre-Launch Checklist

```markdown
□ All deprecated skills marked [DEPRECATED]
□ All NEW skills inserted with correct numbering
□ All CONSOLIDATED skills updated with comprehensive content
□ All MODIFIED skills have improved descriptions
□ All dependencies verified and X-2 compliant
□ All lesson plans updated
□ All assessments updated
□ Migration guide published
□ Teacher training scheduled (if needed)
```

---

## ROLLBACK PLAN (If Issues Arise)

```markdown
In case of critical issues discovered after deployment:

□ Keep backup of old allskills.md as allskills_phase13_backup.md
□ Keep deprecated skills in file (marked but not deleted) for one cycle
□ Document any issues in T07_RESTRUCTURING_ISSUES.md
□ If major problems: Revert to Phase 13, schedule Phase 14v2
□ If minor problems: Hot-fix specific skills, document in errata
```

---

## SUCCESS CRITERIA

### Metrics to Track Post-Implementation

```markdown
After 1 semester:

□ Teacher survey: Is debugging framework (G3.06) clearer than old fragmented approach?
□ Student assessment: Can students name and apply 5 loop patterns? (Target: 80%+)
□ Code review: Do students use systematic debugging? (Target: 70%+)
□ Bug reports: Fewer parallel loop race condition bugs? (Target: 30% reduction)
□ AI usage: Do students write better prompts for loop generation? (Target: measurable improvement)
```

---

## TIMELINE ESTIMATE

| Phase | Tasks | Duration | Responsible |
|-------|-------|----------|-------------|
| 1. Deprecate | Mark 8 skills | 1 hour | Curriculum Lead |
| 2. Insert NEW | Add 11 skills | 3 hours | Curriculum Lead |
| 3. Consolidate | Update 2 skills | 2 hours | Curriculum Lead |
| 4. Modify | Update 5 skills | 2 hours | Curriculum Lead |
| 5. Dependencies | Global updates | 2 hours | Tech Lead |
| 6. Renumber | Fix numbering | 2 hours | Curriculum Lead |
| 7. Validate | Run checks | 2 hours | Tech Lead |
| 8. Curriculum | Update lessons | 1 week | Teacher Team |
| 9. Documentation | Create guides | 3 days | Documentation Team |
| 10. Review | Sign-offs | 1 week | All Stakeholders |

**TOTAL ESTIMATED TIME:** 3 weeks (with parallel workstreams)

---

## QUESTIONS FOR IMPLEMENTER

Before starting:

```markdown
□ Do we have automated tools for X-2 validation?
□ Do we have backup/version control for allskills.md?
□ Who owns lesson plan updates?
□ Who owns assessment updates?
□ Is there a teacher training budget if needed?
□ What's the deadline for Phase 14 launch?
□ Should we pilot with a subset of classes first?
```

---

## CONTACT FOR ISSUES

During implementation, contact:

- **Skill content questions:** [Curriculum Lead]
- **Technical issues (dependencies, numbering):** [Tech Lead]
- **Lesson plan questions:** [Teacher Team Lead]
- **Timeline concerns:** [Project Manager]

---

**Checklist Version:** 1.0
**Date:** 2024-12-04
**Status:** Ready for Implementation

---

## APPENDIX: Quick Command Reference

### Useful grep commands for verification:

```bash
# Count T07 skills by grade
grep "^ID: T07\.K\." allskills.md | wc -l  # Kindergarten count
grep "^ID: T07\.G1\." allskills.md | wc -l # Grade 1 count
# ... repeat for G2-G8

# Find all dependencies on a specific skill
grep "T07.G8.16" allskills.md  # Find references to deprecated skill

# Verify no broken dependencies
grep "Dependencies:" -A 5 allskills.md | grep "T07\." | sort | uniq > deps.txt
# Then check each ID in deps.txt exists in the file

# Find X-2 violations
# (Manual process: for each skill, check if dependencies are within 2 grades)
```

---

END OF CHECKLIST
