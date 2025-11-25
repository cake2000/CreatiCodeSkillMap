# T28 Issues Quick Reference
**Generated**: 2025-11-25

## Skills That Need Breaking Down

| Skill ID | Current Name | Issue | Suggested Split |
|----------|--------------|-------|-----------------|
| T28.G3.05 | Describe randomness in games | 3 tasks in one | .01 Identify randomness, .02 Simulate element, .03 Skill vs luck |
| T28.G7.06.01 | Multi-agent simulation (5-10) | Too steep jump | .01 3-4 agents, .02 Different behaviors, .03 Scale to 5-10 |
| T28.G7.06.02 | Aggregate metrics | Depends on .01 | Becomes .04 after breakdown |
| T28.G8.01 | Chain sim→analysis→dashboard | Massive capstone | .01 Manual params, .02 Auto sweep, .03 Static dashboard, .04 User selection, .05 Auto-refresh |

---

## Critical Missing Skills

| Insert After | New Skill ID | Purpose |
|--------------|--------------|---------|
| T28.G3.07 | T28.G3.08 | 4-6 outcome random generator (bridge to if-statements) |
| T28.G3.09 | T28.G3.09 | Why simulations are useful (foundational concept) |
| T28.G4.01 | T28.G4.01.05 | Manual trial logging (bridge to automated) |
| T28.G4.07 | T28.G4.08 | Paired random values (bridge to compound events) |
| T28.G4.06 | Reorganize | Move G5.05 (calculate prob) before G4.06 (interpret prob) |
| T28.G5.11 | T28.G5.12 | Observe run-to-run variation (sets up seeded random) |
| T28.G7.08 | T28.G7.09 | Noise function for procedural generation |

---

## Dependencies to REMOVE (Bloat)

### T28.G4.01
❌ Remove: T02.G2.01, T02.G2.02, T04.G2.01, T04.G2.02, T04.G2.03, T06.G2.01, T06.G2.02
✓ Keep: T06.G2.03, T08.G3.01, T09.G3.05, T28.G3.07

### T28.G4.02.01
❌ Remove: T05.G3.01, T05.G3.02
✓ Keep: T07.G3.01, T10.G3.03, T28.G4.01

### T28.G4.02.02
❌ Remove: T05.G3.01, T05.G3.02
✓ Keep: T09.G3.05, T28.G4.02.01

---

## Dependencies to ADD

| Skill | Add Dependency | Reason |
|-------|----------------|--------|
| T28.G4.05 | T28.G3.02 | Uses pick random for coordinates |
| T28.G4.07 | T28.G4.01 | Needs basic random understanding |
| T28.G4.07 | T10.G4.17 | Uses insert random items block |
| T28.G5.02 | T28.G4.02.01 | Logs assignments to lists |
| T28.G5.08 | T28.G5.05 or .06 | Probabilistic simulations need prob concepts |
| T28.G6.10 | T10.G4.x | List manipulation for sampling |
| T28.G7.04 | T10.G4.15 | Uses reshuffle block |

---

## Skills Needing Better Descriptions

| Skill | Issue | Fix |
|-------|-------|-----|
| T28.G3.01 | Vague "simulation" | Specify: "3-color spinner simulation" |
| T28.G4.04 | Missing example | Add: "pick random 1-5 for 4 colors = unfair" |
| T28.G5.08 | Vague requirements | Provide specific scenario: "foraging ant with has_food variable" |
| T28.G6.04 | Unclear purpose | Clarify random data generation vs AI testing |
| T28.G6.11 | No implementation | Add: "run simulation 1000x, count conditional cases" |

---

## Skills Needing Block References

| Skill | Current | Add Block Reference |
|-------|---------|---------------------|
| T28.G4.02.01 | "appending to list" | `add (result) to [trials]` |
| T28.G4.02.02 | "count frequencies" | `if (item) = (color)` + `change [count] by (1)` |
| T28.G4.05 | "random coordinates" | `pick random (MIN) to (MAX)` twice |
| T28.G4.07 | "without repetition" | `insert (N) [random] items from [list1] into [list2]` |
| T28.G5.08 | "tracks position" | `set [x] to`, `set [y] to`, `change [x] by` |
| T28.G6.05 | "grid position" | `set [gridX] to`, `set [direction] to` |
| T28.G7.04 | "shuffle randomly" | `reshuffle [list] randomly` |

---

## Overlapping Skills to Clarify

| Pair | Issue | Resolution |
|------|-------|------------|
| T28.G5.08 vs T28.G6.05 | Both track agent position | G5.08 = continuous coords, G6.05 = discrete grid |
| T28.G4.02.03 vs T28.G4.06 | Both use percentages | G4.02.03 = experimental, G4.06 = theoretical |

---

## Missing Block Coverage

| Block | Syntax | Status |
|-------|--------|--------|
| Random list | `set [list] to (N) random whole numbers...` | ⚠️ T10 teaches, T28 never uses |
| Reshuffle | `reshuffle [list] randomly` | ⚠️ Used (G7.04) but not taught in T28 |
| Insert random | `insert (N) [random] items from [list1] into [list2]` | ⚠️ Available but not used |
| Noise | `noise at x (X) y (Y) seed (SEED)` | ❌ Never taught or used |
| Reshuffle table | `reshuffle table [table] randomly` | ❌ Never used in T28 |

### Recommendations
- Add T28.G4.09: Use reshuffle for probability experiments
- Update T28.G4.07: Reference insert random items block
- Add T28.G7.09: Teach noise function for procedural generation

---

## X-2 Rule Check

✓ **All dependencies pass X-2 rule**
- No circular dependencies found
- No forward dependencies found
- All cross-topic dependencies within X, X-1, or X-2 grades

---

## Grade Level Appropriateness

✓ **K-2 skills** (T28.G2.01-04): All use physical manipulatives or pictures ✓
✓ **G3+ skills**: All use CreatiCode blocks ✓
⚠️ **Some G3+ skills** lack specific block syntax (see "Needing Block References" above)

---

## Implementation Priority

### Phase 1: Critical Fixes (Do First)
1. Break down T28.G8.01 (5 sub-skills)
2. Break down T28.G3.05 (2-3 sub-skills)
3. Break down T28.G7.06.01/.02 (4 sub-skills)
4. Clean dependencies (remove T02, T05 from G4 skills)

### Phase 2: Fill Gaps (Do Next)
5. Add T28.G3.08 (bridge to if-statements)
6. Add T28.G4.01.05 (manual logging)
7. Add T28.G4.08 (paired random values)
8. Reorganize G4.06/G5.05 (calc before interpret)

### Phase 3: Quality (Do Soon)
9. Add specific examples to vague skills
10. Add block syntax to all coding skills
11. Clarify G5.08 vs G6.05 distinction
12. Update T28.G4.07 block reference

### Phase 4: Enhancement (Do Later)
13. Add T28.G3.09 (why simulate)
14. Add T28.G5.12 (run variation)
15. Add T28.G7.09 (noise function)
16. Add T28.G4.09 (reshuffle)
17. Create T28 Block Reference Guide

---

## Quick Stats

- **Total T28 Skills**: 48 (G2: 4, G3: 7, G4: 7, G5: 11, G6: 11, G7: 6, G8: 5)
- **Need Breakdown**: 4 skills
- **Need Better Descriptions**: 5 skills
- **Need Block References**: 7 skills
- **Missing Skills to Add**: 7 skills
- **Dependencies to Remove**: 12 dependencies
- **Dependencies to Add**: 7 dependencies

---

## Testing Checklist

After fixes, verify:
- [ ] No skill depends on a later skill in same topic
- [ ] All G4 skills depend only on G2-G4 skills (X-2 rule)
- [ ] All G5 skills depend only on G3-G5 skills
- [ ] All G6 skills depend only on G4-G6 skills
- [ ] All skills reference specific CreatiCode blocks
- [ ] No skill tries to teach 3+ distinct concepts
- [ ] All skills have concrete examples
- [ ] Progression from simple → complex is smooth (no big jumps)
