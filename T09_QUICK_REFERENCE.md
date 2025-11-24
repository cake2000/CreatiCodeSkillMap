# T09 Variables & Expressions - Quick Action Reference

**Date:** November 23, 2025

## Executive Summary

- **Total T09 Skills Analyzed:** 62 (GK.01 to G8.06)
- **Skills with Critical Issues:** 8 (13% - must split)
- **Skills Needing Clarification:** 23 (37% - add block references, fix dependencies, clarify)
- **Total Recommended Changes:** 37 actionable items
- **Resulting Skill Count After Changes:** ~76 skills (+14 net increase)

## Critical Issues Requiring Immediate Action

### 1. OVERLY BROAD SKILLS (MUST SPLIT - 8 skills)

| Skill ID | Current Description | Issue | Action |
|----------|-------------------|--------|---------|
| **T09.G3.02** | Use change and reduce blocks | Covers 2 blocks | Split into G3.02 (change) + G3.02.01 (reduce) |
| **T09.G4.01** | Use addition and subtraction | Covers 2 operators | Split into G4.01 (+) + G4.01.01 (-) |
| **T09.G4.02** | Use multiplication and division | Covers 2 operators | Split into G4.02 (*) + G4.02.01 (/) |
| **T09.G4.06** | Use all 6 comparison operators | Covers 6 operators! | Split into 4 skills: G4.06 (=,<), G4.06.01 (>), G4.06.02 (≠), G4.06.03 (≥,≤) |
| **T09.G6.04** | String length and case conversion | Covers 2+ blocks | Split into G6.04 (length) + G6.04.01 (case) |
| **T09.G6.05** | Substring and position operations | Covers 2+ blocks | Split into G6.05 (position) + G6.05.01 (substring) |
| **T09.G7.01.01** | Use 5 math functions | Covers 5 functions | Split into G7.01.01 (round/floor/ceil) + G7.01.02 (abs) + G7.01.03 (sqrt) |
| **T09.G6.01** | Model real-world quantities | Too abstract | Clarify with specific examples or split into formula types |

**Impact:** Splitting these 8 skills will create 13 new sub-skills.

---

## Top 10 Priority Fixes

### Priority 1: Break Down Overly Broad Skills
1. Split T09.G4.06 (comparison operators) - HIGHEST IMPACT (6 operators → 4 skills)
2. Split T09.G7.01.01 (math functions) - HIGH IMPACT (5 functions → 3 skills)
3. Split T09.G4.01 and G4.02 (arithmetic operators) - 4 operators → 4 skills

### Priority 2: Fix Dependencies
4. Move T09.G3.06 earlier (copy variable) - should come after G3.01.02, not G3.02
5. Add intra-topic dependencies to T09.G4.05 (loop counter needs G3.01.04, G3.02)

### Priority 3: Add Missing Block References
6. Add block references to G3.01.01, G3.01.02, G3.01.03 (basic variable blocks)
7. Add block references to G6.03, G6.03.01, G7.05 (exponent, mod, export/import)
8. Add block references to G8.02.01, G8.02.02, G8.03 (min/max, trig, cloud)

### Priority 4: Add Missing Scaffolding
9. Add T09.G3.01.05 - Use variable reporter blocks (missing fundamental skill)
10. Clarify T09.G4.04 - ask/answer blocks (currently confusing)

---

## Issues by Grade Level

### Grade 3 (2 issues)
- Split G3.02 (change vs reduce blocks)
- Move G3.06 earlier in sequence

### Grade 4 (6 issues)
- Split G4.01 (+ and -)
- Split G4.02 (* and /)
- Clarify G4.04 (ask/answer)
- Add dependencies to G4.05
- **Split G4.06 (6 comparison operators!) - CRITICAL**
- Add block ref to G4.08

### Grade 5 (3 issues)
- Clarify G5.02 (string variables)
- Add block ref to G5.02.01 (boolean)
- Clarify G5.03 (join block)

### Grade 6 (5 issues)
- Clarify G6.01 (too broad)
- Add block refs to G6.03, G6.03.01
- Split G6.04 (length and case)
- Split G6.05 (position and substring)

### Grade 7 (3 issues)
- Clarify G7.01 (dynamic systems)
- **Split G7.01.01 (5 math functions) - CRITICAL**
- Add block ref to G7.05

### Grade 8 (4 issues)
- Simplify/remove G8.01.03 (too advanced)
- Add block refs to G8.02.01, G8.02.02, G8.03

---

## Block Reference Checklist

### Blocks Needing References Added:

**Grade 3:**
- [ ] T09.G3.01.01: "Make a Variable" UI button
- [ ] T09.G3.01.02: `set [variable] to (value)`
- [ ] T09.G3.01.03: `change [variable] by (1)`

**Grade 4:**
- [ ] T09.G4.04: `ask [question] and wait`, `(answer)`
- [ ] T09.G4.08: `pick random (min) to (max)`

**Grade 5:**
- [ ] T09.G5.02.01: `<true>`, `<false>` (operator_true, operator_false)
- [ ] T09.G5.03: `join (A) (B)` (standard Scratch)

**Grade 6:**
- [ ] T09.G6.03: `(BASE) ^ (P)` (operator_pow)
- [ ] T09.G6.03.01: `(A) mod (B)` - VERIFY EXISTS
- [ ] T09.G6.04: `length of [string]`, `[CASE v] of text [T]`
- [ ] T09.G6.05: `position of [T1] in [T2]`, `substring of [TEXT] from (P1) to (P2)`

**Grade 7:**
- [ ] T09.G7.05: `export variable [VAR]`, `import variable [VAR]`
- [ ] T09.G7.01.01: Math functions (abs, round, floor, ceiling, sqrt) - VERIFY HOW ACCESSED

**Grade 8:**
- [ ] T09.G8.02.01: min(), max() - VERIFY HOW ACCESSED
- [ ] T09.G8.02.02: sin(), cos(), tan() - VERIFY HOW ACCESSED
- [ ] T09.G8.03: `save [VISIBILITY v] data [VALUE] with name [KEY]` (data_savedata)

---

## New Skills to Add

1. **T09.G3.01.05** - Use variable reporter blocks in other blocks
   - Location: After G3.01.04
   - Block: [variable] round reporter
   - Purpose: Teach that variables can be dragged into say, move, etc.

2. **T09.G5.03.01** - Use multi-input join with separator
   - Location: After G5.03
   - Block: `join [T1] [T2] [T3] [T4] [T5] [T6] with [SEPARATOR]`
   - Purpose: Advanced string joining (CSV, formatted lists)

---

## Dependency Fixes Needed

### Fix 1: T09.G3.06 (Copy variable value)
**Current:** Depends on T09.G3.02 (change/reduce blocks)
**Problem:** Copying uses "set", not "change"
**Fix:** Change dependency to T09.G3.01.02 (set block)
**Move:** Place G3.06 immediately after G3.01.02

### Fix 2: T09.G4.05 (Loop counter)
**Current:** Only depends on T07.G3.01 (loops)
**Problem:** Missing intra-topic dependencies on variable basics
**Fix:** Add dependencies:
- T09.G3.01.04 (display variable)
- T09.G3.02 (change variable)

---

## Skills to Clarify or Simplify

| Skill | Issue | Recommended Fix |
|-------|-------|-----------------|
| T09.G5.02 | "Use string variables" too vague | Add: "Store text values and display them" |
| T09.G7.01 | "Dynamic systems" too abstract | Change to: "Update variables each frame for animation" |
| T09.G8.01.03 | Newton's method too advanced | Remove or simplify to "guess-and-check algorithms" |

---

## Implementation Roadmap

### Phase 1: Critical Splits (Week 1)
1. Split T09.G4.06 (6 comparison operators)
2. Split T09.G7.01.01 (5 math functions)
3. Split T09.G4.01, G4.02 (arithmetic operators)

### Phase 2: Dependencies and Moves (Week 1)
4. Move T09.G3.06 earlier
5. Fix dependencies for T09.G4.05

### Phase 3: Block References (Week 2)
6. Add block references to all 13 skills missing them
7. Verify mod operator and math functions in CreatiCode

### Phase 4: Add New Skills (Week 2)
8. Add T09.G3.01.05 (variable reporter)
9. Add T09.G5.03.01 (multi-join)

### Phase 5: Clarifications (Week 3)
10. Clarify G5.02, G7.01, G8.01.03
11. Review and test all changes

---

## Validation Checklist

Before finalizing changes:
- [ ] Verify all mentioned blocks exist in blockdes8.txt
- [ ] Check mod operator exists in CreatiCode
- [ ] Verify how math functions (abs, round, sqrt) are accessed
- [ ] Verify min/max functions exist
- [ ] Check trig functions (sin, cos, tan) availability
- [ ] Confirm cloud variables work as described
- [ ] Test all new skill progressions for logical flow
- [ ] Ensure no circular dependencies created
- [ ] Verify X-2 rule compliance for all new dependencies

---

## Success Metrics

After implementing all changes:
- ✅ No single skill should cover more than 2 closely-related blocks
- ✅ All skills should have explicit block references where applicable
- ✅ All intra-topic dependencies should be logical and necessary
- ✅ Progression should be smooth with no large gaps
- ✅ K-2 skills remain unplugged/visual (already good)
- ✅ Grade 3+ skills use concrete CreatiCode blocks
- ✅ Skills increase from ~62 to ~76 (22% increase for better granularity)

---

## Contact for Questions

See full analysis in: `/media/binyu/USB2/dev/CreatiCodeSkillMap/T09_COMPREHENSIVE_ANALYSIS.md`
