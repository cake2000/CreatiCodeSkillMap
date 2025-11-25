# Grade 7 Fixes - Quick Reference Guide

## Common Replacements (X-2 Rule Fixes)

Use this table for quick lookup when applying X-2 fixes:

| Old (Grade 2-4) | New (Grade 5-7) | Use For |
|----------------|----------------|---------|
| T04.G2.01 | T04.G5.01 | Pattern recognition in algorithms |
| T09.G3.01.04 | T09.G5.01 | Variable usage and monitoring |
| T09.G3.05 | T09.G5.01 or T09.G5.02 | Variable manipulation |
| T06.G3.01 | T06.G5.01 | Event-driven programming |
| T07.G3.01 | T07.G5.01 | Loop concepts |
| T08.G4.01 | T08.G5.01 | Conditional logic |
| T10.G4.01 | T10.G5.01 | List operations |
| T10.G4.02 | T10.G5.01 | List operations |
| T10.G4.08 | T10.G5.03 | List searching/filtering |
| T14.G4.06 | T14.G5.01 | Game mechanics |
| T14.G4.09 | T14.G5.01 | Game mechanics |
| T14.G4.10 | T14.G5.02 | Game mechanics |
| T16.G4.03 | T16.G5.01 | Multimedia |
| T29.G4.05.02 | T29.G5.01 | AI literacy |
| T30.G4.05 | T30.G5.01 | Platform concepts |
| T36.G4.03 | T36.G5.01 | Collaboration |

## Topic-Specific Additions

### When to Add Topic 8 (Conditions) - T08.G5.01
Add when skill involves:
- ✅ Algorithm comparison or analysis
- ✅ Search algorithms
- ✅ Edge case testing
- ✅ Decision-making in design
- ✅ Pathfinding
- ✅ Defensive programming
- ✅ Role-based behaviors
- ✅ Data filtering or validation

### When to Add Topic 9 (Variables) - T09.G5.01
Add when skill involves:
- ✅ Debugging and inspection
- ✅ State tracking
- ✅ Performance monitoring
- ✅ Game state management
- ✅ Data synchronization
- ✅ Dynamic systems
- ✅ Encapsulation concepts

### When to Add Topic 10 (Lists/Tables) - T10.G5.01 or T10.G5.03
Add when skill involves:
- ✅ Test case collections
- ✅ Checklists
- ✅ Search algorithms (use T10.G5.03)
- ✅ Data structures
- ✅ Grid-based systems
- ✅ Template libraries
- ✅ Conversation history
- ✅ Data analysis

### When to Add Topic 7 (Loops) - T07.G5.01
Add when skill involves:
- ✅ Iteration through collections
- ✅ Time-based simulations
- ✅ Data processing/cleaning
- ✅ Grid pattern generation
- ✅ Repeated operations
- ✅ Algorithm implementation

### When to Add Topic 6 (Events) - T06.G5.01
Add when skill involves:
- ✅ Event-driven systems
- ✅ Game state transitions
- ✅ Scene management
- ✅ Multiplayer coordination
- ✅ User interaction handling
- ✅ Broadcast coordination

### When to Add Topic 11 (Functions) - T11.G5.01
Add when skill involves:
- ✅ Modular design
- ✅ Code reusability
- ✅ Decomposition
- ✅ Template libraries
- ✅ Architectural patterns

## Redundant Dependencies to Remove

Simply delete these from the respective skills:

1. T05.G7.07 ← remove T05.G6.04
2. T20.G7.06 ← remove T20.G7.03
3. T21.G7.09d ← remove T08.G5.01
4. T24.G7.05 ← remove T24.G6.06 AND T09.G5.01
5. T24.G7.06 ← remove T10.G5.03
6. T24.G7.07.03 ← remove T08.G5.01
7. T24.G7.08.04 ← remove T07.G5.01
8. T24.G7.13 ← remove T09.G5.01

## Skills Requiring Multiple Changes

These skills need several fixes applied:

### T01.G7.03.01 (Write pseudocode for "find max")
- Replace T04.G2.01 → T04.G5.01
- Replace T09.G3.01.04 → T09.G5.01
- Add T10.G5.03 (list searching)

### T01.G7.03.02 (Write pseudocode for "count matches")
- Replace T04.G2.01 → T04.G5.01
- Replace T09.G3.01.04 → T09.G5.01
- Add T08.G5.01 (conditional logic)

### T03.G7.02 (Map functional modules to architecture)
- Replace T06.G3.01 → T06.G5.01
- Replace T09.G3.01.04 → T09.G5.01
- Add T08.G5.01 (conditional logic)
- Add T11.G5.01 (modular design)

### T03.G7.04 (Redesign project structure)
- Replace T06.G3.01 → T06.G5.01
- Replace T09.G3.01.04 → T09.G5.01
- Add T08.G5.01 (conditional logic)

### T04.G7.05 (Implement combined pattern solution)
- Replace T06.G3.01 → T06.G5.01
- Replace T09.G3.01.04 → T09.G5.01
- Add T07.G5.01 (loops)

### T14.G7.06 (Advanced level management system)
- Replace T14.G4.09 → T14.G5.01
- Replace T14.G4.10 → T14.G5.02
- Add T08.G5.01 (conditional logic)
- Add T06.G5.01 (events)

### T24.G7.05 (Use XO to coach peers)
- Remove T24.G6.06 (redundant)
- Remove T09.G5.01 (redundant)

### T26.G7.02 (Monitor data quality in real time)
- Replace T09.G3.01.04 → T09.G5.01
- Replace T09.G3.05 → T09.G5.02

## Implementation Checklist

For each skill being modified:

- [ ] Locate skill block in allskills.md (search for "ID: SKILL_ID")
- [ ] Find Dependencies section
- [ ] Apply replacements (change dependency line)
- [ ] Apply removals (delete dependency line)
- [ ] Apply additions (add new dependency line with format: `* SKILL_ID: description`)
- [ ] Verify no duplicate dependencies created
- [ ] Mark skill as complete in tracking sheet

## Validation Commands

After applying fixes, run these checks:

```bash
# Check for remaining X-2 violations (should return 0)
grep -A 5 "^ID: T.*\.G7\." allskills.md | grep "^\*.*\.G[234]\." | wc -l

# Count dependencies (should increase from ~500 to ~570)
grep "^Dependencies:" -A 50 allskills.md | grep "^\* T" | wc -l

# Check for circular dependencies (manual review needed)
# Run dependency analysis script
```

## Priority Order

1. **FIRST:** Apply all X-2 replacements (39 fixes)
2. **SECOND:** Remove redundant dependencies (9 removals)
3. **THIRD:** Add Topic 8/9 dependencies (40 additions)
4. **FOURTH:** Add Topic 10/7/6/11 dependencies (37 additions)
5. **FIFTH:** Review complex skills (3 skills)

## Common Pitfalls to Avoid

❌ **Don't** add a dependency that's already there
❌ **Don't** remove a dependency before adding its replacement
❌ **Don't** create circular dependencies (A depends on B depends on A)
❌ **Don't** skip validation after each batch
❌ **Don't** add same dependency to a skill twice

✅ **Do** verify replacement skill exists before applying
✅ **Do** check skill descriptions match the justification
✅ **Do** apply changes in order (replace, remove, add)
✅ **Do** run validation after each phase
✅ **Do** keep backup of original allskills.md

## Estimated Time

- X-2 fixes: ~2 hours (39 skills)
- Redundant removals: ~15 minutes (9 skills)
- Missing T8/T9 additions: ~1.5 hours (40 skills)
- Missing T10/T7/T6/T11 additions: ~1.5 hours (37 skills)
- Validation: ~30 minutes

**Total:** ~6 hours of careful work

## Support Files

- `GRADE7_FIXES_PLAN.json` - Full machine-readable fix plan
- `GRADE7_FIXES_SUMMARY.md` - Detailed human-readable summary
- `GRADE7_DEPENDENCY_ANALYSIS.md` - Original analysis
- `GRADE7_MISSING_CROSS_DEPS.md` - Missing dependencies analysis
