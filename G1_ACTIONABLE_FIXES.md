# Grade 1 Dependency Fixes - Actionable Items

**Date:** 2024-11-24
**Total Issues:** 3
**Priority:** LOW (transitive redundancy cleanup)

---

## Quick Fix Summary

| Skill ID | Current Deps | Remove | Keep | Reason |
|----------|--------------|--------|------|---------|
| T10.G1.01 | T10.GK.01, T10.GK.04 | T10.GK.01 | T10.GK.04 | GK.01 → GK.04 (transitive) |
| T24.G1.02 | T24.GK.01, T24.GK.03 | T24.GK.01 | T24.GK.03 | GK.01 → GK.03 (transitive) |
| T24.G1.03 | T24.GK.03, T24.G1.02 | T24.GK.03 | T24.G1.02 | GK.03 → G1.02 (transitive) |

---

## Detailed Fixes

### Fix 1: T10.G1.01

**Location:** Topic T10 – Lists & Tables
**Skill:** Sort items using two rules

**Current:**
```markdown
ID: T10.G1.01
Topic: T10 – Lists & Tables
Skill: Sort items using two rules
Description: Students sort 6-8 items into groups using two attributes (e.g., "big red shapes" vs "small blue shapes"), understanding that items can belong to groups based on multiple properties.

Dependencies:
* T10.GK.01: Sort picture cards into groups
* T10.GK.04: Add an item to the right group
```

**Fixed:**
```markdown
ID: T10.G1.01
Topic: T10 – Lists & Tables
Skill: Sort items using two rules
Description: Students sort 6-8 items into groups using two attributes (e.g., "big red shapes" vs "small blue shapes"), understanding that items can belong to groups based on multiple properties.

Dependencies:
* T10.GK.04: Add an item to the right group
```

**Change:** Remove line `* T10.GK.01: Sort picture cards into groups`

**Verification:** Check that T10.GK.04 has T10.GK.01 as dependency:
```
T10.GK.04 depends on T10.GK.01 → T10.GK.03 → T10.GK.01
```

---

### Fix 2: T24.G1.02

**Location:** Topic T24 – XO & Generative AI Practices
**Skill:** Compare AI answers to expected answers

**Current:**
```markdown
ID: T24.G1.02
Topic: T24 – XO & Generative AI Practices
Skill: Compare AI answers to expected answers
Description: Students ask a simple question (e.g., "What color is the sky?") and compare the AI's answer to what they know. They discuss when AI gives good answers and when it might be wrong.

Dependencies:
* T24.GK.01: Identify AI as a computer helper
* T24.GK.03: Give simple instructions to an AI helper
```

**Fixed:**
```markdown
ID: T24.G1.02
Topic: T24 – XO & Generative AI Practices
Skill: Compare AI answers to expected answers
Description: Students ask a simple question (e.g., "What color is the sky?") and compare the AI's answer to what they know. They discuss when AI gives good answers and when it might be wrong.

Dependencies:
* T24.GK.03: Give simple instructions to an AI helper
```

**Change:** Remove line `* T24.GK.01: Identify AI as a computer helper`

**Verification:** Check that T24.GK.03 has T24.GK.01 as dependency:
```
T24.GK.03 depends on T24.GK.01
```

---

### Fix 3: T24.G1.03

**Location:** Topic T24 – XO & Generative AI Practices
**Skill:** Understand AI needs clear instructions

**Current:**
```markdown
ID: T24.G1.03
Topic: T24 – XO & Generative AI Practices
Skill: Understand AI needs clear instructions
Description: Students see examples of unclear instructions and their confusing results. They practice making instructions clearer by adding details like color, size, or action.

Dependencies:
* T24.GK.03: Give simple instructions to an AI helper
* T24.G1.02: Compare AI answers to expected answers
```

**Fixed:**
```markdown
ID: T24.G1.03
Topic: T24 – XO & Generative AI Practices
Skill: Understand AI needs clear instructions
Description: Students see examples of unclear instructions and their confusing results. They practice making instructions clearer by adding details like color, size, or action.

Dependencies:
* T24.G1.02: Compare AI answers to expected answers
```

**Change:** Remove line `* T24.GK.03: Give simple instructions to an AI helper`

**Verification:** Check that T24.G1.02 has T24.GK.03 as dependency:
```
T24.G1.02 depends on T24.GK.03
```

---

## Implementation Checklist

- [ ] **T10.G1.01:** Remove T10.GK.01 dependency
- [ ] **T24.G1.02:** Remove T24.GK.01 dependency
- [ ] **T24.G1.03:** Remove T24.GK.03 dependency
- [ ] Verify each transitive dependency chain is correct
- [ ] Update any dependent documentation
- [ ] Run validation checks after changes

---

## Validation Queries

After making changes, verify with these checks:

```bash
# Check T10.G1.01 only has GK.04
grep -A 5 "ID: T10.G1.01" skillsv4/allskills.md | grep "Dependencies:" -A 2

# Check T24.G1.02 only has GK.03
grep -A 5 "ID: T24.G1.02" skillsv4/allskills.md | grep "Dependencies:" -A 2

# Check T24.G1.03 only has G1.02
grep -A 5 "ID: T24.G1.03" skillsv4/allskills.md | grep "Dependencies:" -A 2
```

---

## Impact Assessment

**Risk Level:** LOW

**Affected Skills:** 3 out of 112 Grade 1 skills (2.7%)

**Dependency Graph Changes:**
- Cleaner, more maintainable dependency structure
- No functional impact on learning progression
- Easier to understand skill prerequisites

**Testing Required:**
- Verify dependency chains are complete
- Confirm no circular dependencies introduced
- Check that all skills remain reachable from K

**Rollback Plan:**
If issues arise, simply restore the removed dependency lines. No Grade 2 or later skills are affected.

---

## Rationale for Changes

### Why Remove Transitive Dependencies?

1. **Maintenance:** When updating a transitive dependency, only one reference needs updating
2. **Clarity:** Direct prerequisites are more obvious
3. **Graph complexity:** Reduces edge count in dependency graph
4. **Documentation:** Easier to explain skill relationships
5. **Tooling:** Simpler for automated dependency checking

### Why These Were Flagged

All three issues involve same-topic dependencies with clear linear progression:

- **T10:** GK.01 → GK.04 → G1.01 (sorting progression)
- **T24:** GK.01 → GK.03 → G1.02 → G1.03 (AI understanding progression)

These are textbook cases of transitive redundancy where the intermediate skill clearly encompasses the earlier one.

### Pedagogical Impact

**None.** Students still learn skills in the same order:
- The transitive dependency is still there, just implicit
- The learning sequence is unchanged
- Assessment requirements are identical

---

## Additional Observations

### Grade 1 Dependency Health

**Overall Health: EXCELLENT**

- ✓ Zero X-2 rule violations
- ✓ Appropriate cross-topic dependencies
- ✓ No missing critical dependencies
- ✓ Only 3 minor cleanup items
- ✓ Clear topic progressions
- ✓ Proper distinction between unplugged and programming activities

### Future Considerations

As Grade 2 skills are developed, maintain this level of quality by:

1. **Regular dependency audits** after major changes
2. **Automated X-2 rule checking** in CI/CD
3. **Transitive dependency detection** in validation scripts
4. **Cross-topic dependency reviews** for advanced topics

---

**End of Actionable Fixes Document**
