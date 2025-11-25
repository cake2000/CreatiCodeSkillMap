# Grade 8 X-2 Rule Violations - ACTION LIST

## PRIORITY: IMMEDIATE ATTENTION REQUIRED

This document lists all 18 Grade 8 skills with X-2 rule violations.
Each needs scaffolding skills from Grades 6-8 to replace too-distant dependencies.

---

## X-2 Rule Reminder

**Rule:** A Grade 8 skill can ONLY depend on grades: 6, 7, and 8
- ✅ G8 → G8: OK
- ✅ G8 → G7: OK
- ✅ G8 → G6: OK
- ❌ G8 → G5: VIOLATION (3 grades below)
- ❌ G8 → G4: VIOLATION (4 grades below)
- ❌ G8 → G3: VIOLATION (5 grades below)

---

## CRITICAL VIOLATIONS (Multiple Dependencies)

### 1. T01.G8.01 - Design one-step update rules for a simple simulation
**Topic:** T01 - Everyday Algorithms
**Severity:** HIGH (3 violations)

**Current Problematic Dependencies:**
- ❌ T07.G3.01: Use a counted repeat loop (GRADE 3 - 5 levels below)
- ❌ T08.G3.01: Use a simple if in a script (GRADE 3 - 5 levels below)
- ❌ T09.G3.01.04: Display variable value on stage (GRADE 3 - 5 levels below)

**Recommended Action:**
- Find T07.G6-G8 equivalent for loops (e.g., T07.G6.01: Trace nested loops)
- Find T08.G6-G8 equivalent for conditionals (e.g., T08.G6.01: List operations)
- Find T09.G6-G8 equivalent for variable display (e.g., T09.G6.01: Model with variables)

---

### 2. T29.G8.06 - Parse and use complex API responses
**Topic:** T29 - APIs
**Severity:** HIGH (3 violations)

**Current Problematic Dependencies:**
- ❌ T29.G5.04.02: (GRADE 5 - 3 levels below)
- ❌ T09.G3.05: (GRADE 3 - 5 levels below)
- ❌ T10.G5.03: (GRADE 5 - 3 levels below)

**Recommended Action:**
- Upgrade to T29.G6+ API skills
- Upgrade to T09.G6.01 or higher for custom blocks
- Upgrade to T10.G6+ for conditional logic

---

### 3. T01.G8.04 - Multi-step algorithm design
**Topic:** T01 - Everyday Algorithms
**Severity:** MEDIUM (2 violations)

**Current Problematic Dependencies:**
- ❌ T06.G3.01: (GRADE 3 - 5 levels below)
- ❌ T09.G3.01.04: (GRADE 3 - 5 levels below)

**Recommended Action:**
- Upgrade to T06.G6.01: Trace event execution paths
- Upgrade to T09.G6.01: Model with variables

---

### 4. T01.G8.08 - Complex simulation parameters
**Topic:** T01 - Everyday Algorithms
**Severity:** MEDIUM (2 violations)

**Current Problematic Dependencies:**
- ❌ T06.G3.01: (GRADE 3 - 5 levels below)
- ❌ T09.G3.01.04: (GRADE 3 - 5 levels below)

**Recommended Action:**
- Upgrade to T06.G6+ loop skills
- Upgrade to T09.G6+ variable skills

---

### 5. T29.G8.05 - Parse JSON API response
**Topic:** T29 - APIs
**Severity:** MEDIUM (2 violations)

**Current Problematic Dependencies:**
- ❌ T29.G5.03.02: Build stop-word filter (GRADE 5 - 3 levels below)
- ❌ T29.G5.06: Parse sentence parts of speech (GRADE 5 - 3 levels below)

**Recommended Action:**
- Find T29.G6-G7 text processing skills
- Consider T15.G6+ string manipulation as alternative

---

## SINGLE VIOLATIONS (Easier to Fix)

### 6. T01.G8.02
**Violation:** T09.G3.01.04 (Grade 3)
**Fix:** Upgrade to T09.G6.01 or T09.G7+

### 7. T01.G8.05
**Violation:** T09.G3.01.04 (Grade 3)
**Fix:** Upgrade to T09.G6.01 or T09.G7+

### 8. T01.G8.09
**Violation:** T07.G3.01 (Grade 3)
**Fix:** Upgrade to T07.G6.01 or T07.G7+

### 9. T06.G8.06.01 - Advanced loop patterns
**Violation:** T06.G4.08.01 (Grade 4 - 4 levels below)
**Fix:** Use T06.G6+ or T06.G7+ loop skills

### 10. T06.G8.06.05 - Complex iteration
**Violation:** T06.G4.09 (Grade 4 - 4 levels below)
**Fix:** Use T06.G6+ or T06.G7+ loop skills

### 11. T10.G8.01 - Advanced conditionals
**Violation:** T07.G5.01 (Grade 5 - 3 levels below)
**Fix:** Use T07.G6.01 or T07.G7+

### 12. T10.G8.02 - Complex boolean logic
**Violation:** T10.G4.10 (Grade 4 - 4 levels below)
**Fix:** Use T10.G6+ or T10.G7+

### 13. T10.G8.03 - Nested conditionals
**Violation:** T10.G4.07 (Grade 4 - 4 levels below)
**Fix:** Use T10.G6+ or T10.G7+

### 14. T10.G8.04 - State machines
**Violation:** T10.G5.07 (Grade 5 - 3 levels below)
**Fix:** Use T10.G6+ or T10.G7+

### 15. T10.G8.07 - Complex decision trees
**Violation:** T10.G4.02 (Grade 4 - 4 levels below)
**Fix:** Use T10.G6+ or T10.G7+

### 16. T13.G8.05 - Advanced pen drawing
**Violation:** T11.G5.01 (Grade 5 - 3 levels below)
**Fix:** Use T11.G6.01 or T11.G7+

### 17. T18.G8.01.02 - Physics simulation
**Violation:** T09.G3.01 (Grade 3 - 5 levels below)
**Fix:** Use T09.G6.01 or T09.G7+

### 18. T26.G8.01.01 - Advanced UI design
**Violation:** T26.G5.08.02 (Grade 5 - 3 levels below)
**Fix:** Use T26.G6+ or T26.G7+

---

## SUMMARY BY TOPIC

### T01 (Everyday Algorithms) - 6 violations
- T01.G8.01 (3 violations) ⚠️ CRITICAL
- T01.G8.02 (1 violation)
- T01.G8.04 (2 violations)
- T01.G8.05 (1 violation)
- T01.G8.08 (2 violations)
- T01.G8.09 (1 violation)

**Pattern:** Heavy reliance on Grade 3 basics (loops, conditions, variables)
**Solution:** Create/identify Grade 6-7 intermediate algorithm skills

### T10 (Conditionals) - 5 violations
- T10.G8.01 (1 violation)
- T10.G8.02 (1 violation)
- T10.G8.03 (1 violation)
- T10.G8.04 (1 violation)
- T10.G8.07 (1 violation)

**Pattern:** Jumping from Grade 4-5 to Grade 8
**Solution:** Ensure T10.G6 and T10.G7 have comprehensive conditional skills

### T29 (APIs) - 2 violations
- T29.G8.05 (2 violations)
- T29.G8.06 (3 violations) ⚠️ CRITICAL

**Pattern:** Grade 5 text processing to Grade 8 API integration
**Solution:** Create Grade 6-7 data parsing and API foundation skills

### Other Topics - 5 violations
- T06 (Loops): 2 violations
- T13 (Pen): 1 violation
- T18 (Physics): 1 violation
- T26 (UI): 1 violation

---

## VIOLATION BREAKDOWN BY GRADE

### Grade 3 Dependencies (5 levels below) - MOST SEVERE
**Count:** 10 violations

**Affected Skills:**
- T01.G8.01 (3 violations from G3)
- T01.G8.02 (1 violation)
- T01.G8.04 (2 violations from G3)
- T01.G8.05 (1 violation)
- T01.G8.08 (2 violations from G3)
- T01.G8.09 (1 violation)
- T18.G8.01.02 (1 violation)
- T29.G8.06 (1 violation)

### Grade 4 Dependencies (4 levels below)
**Count:** 5 violations

**Affected Skills:**
- T06.G8.06.01
- T06.G8.06.05
- T10.G8.02
- T10.G8.03
- T10.G8.07

### Grade 5 Dependencies (3 levels below)
**Count:** 7 violations

**Affected Skills:**
- T10.G8.01
- T10.G8.04
- T13.G8.05
- T26.G8.01.01
- T29.G8.05 (2 violations from G5)
- T29.G8.06 (2 violations from G5)

---

## ACTION PLAN

### Step 1: Audit Existing Skills (2-3 hours)
For each violating dependency:
1. Search for equivalent skill in Grades 6-8
2. If exists, note the ID
3. If not, mark for creation

### Step 2: Create Missing Skills (Variable time)
Based on audit, create necessary scaffolding:
- Priority: T01, T10, T29 (most violations)
- Focus on Grades 6-7
- Ensure proper progression

### Step 3: Update Dependencies (1 hour)
- Replace violating dependencies with G6-8 equivalents
- Verify X-2 compliance
- Test learning progression

### Step 4: Validate (1 hour)
- Check all 18 skills
- Ensure no new violations created
- Verify pedagogical coherence

---

## QUICK REFERENCE TABLE

| Skill ID | Topic | Violations | Severity | Priority |
|----------|-------|------------|----------|----------|
| T01.G8.01 | Algorithms | 3 (G3) | HIGH | 1 |
| T29.G8.06 | APIs | 3 (G3,G5) | HIGH | 2 |
| T01.G8.04 | Algorithms | 2 (G3) | MEDIUM | 3 |
| T01.G8.08 | Algorithms | 2 (G3) | MEDIUM | 4 |
| T29.G8.05 | APIs | 2 (G5) | MEDIUM | 5 |
| T01.G8.02 | Algorithms | 1 (G3) | LOW | 6 |
| T01.G8.05 | Algorithms | 1 (G3) | LOW | 7 |
| T01.G8.09 | Algorithms | 1 (G3) | LOW | 8 |
| T06.G8.06.01 | Loops | 1 (G4) | LOW | 9 |
| T06.G8.06.05 | Loops | 1 (G4) | LOW | 10 |
| T10.G8.01 | Conditionals | 1 (G5) | LOW | 11 |
| T10.G8.02 | Conditionals | 1 (G4) | LOW | 12 |
| T10.G8.03 | Conditionals | 1 (G4) | LOW | 13 |
| T10.G8.04 | Conditionals | 1 (G5) | LOW | 14 |
| T10.G8.07 | Conditionals | 1 (G4) | LOW | 15 |
| T13.G8.05 | Pen | 1 (G5) | LOW | 16 |
| T18.G8.01.02 | Physics | 1 (G3) | LOW | 17 |
| T26.G8.01.01 | UI | 1 (G5) | LOW | 18 |

---

## ESTIMATED EFFORT

**Total Time:** 8-12 hours
- Audit: 2-3 hours
- Skill creation: 3-6 hours (depends on gaps)
- Updates: 1-2 hours
- Validation: 1-2 hours
- Documentation: 1 hour

**Complexity:** MEDIUM
- Clear identification of issues
- Systematic replacement approach
- May require new skill creation

**Impact:** HIGH
- Ensures grade-appropriate progression
- Maintains pedagogical integrity
- Complies with X-2 rule

---

## SUCCESS CRITERIA

✅ All 18 skills have dependencies from G6-G8 only
✅ No new X-2 violations introduced
✅ Learning progression maintained
✅ Skill content alignment verified
✅ Documentation updated

---

**Document Created:** 2025-11-24
**Total Violations:** 18 skills, 26 dependency violations
**Critical:** 2 skills (3 violations each)
**Status:** READY FOR ACTION
