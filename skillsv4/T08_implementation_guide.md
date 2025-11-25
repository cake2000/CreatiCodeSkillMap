# T08 Implementation Guide - Quick Reference

## Executive Summary
- **Total issues found**: 7 critical/high priority
- **Skills affected**: 15 skills need updates
- **New skills to add**: 4 essential + 1 optional
- **Skills to remove**: 2 (merge into one)
- **Dependencies to remove**: 45 redundant dependencies
- **Estimated time**: 3 hours
- **Risk level**: LOW (all changes within T08)

---

## Phase 1: Critical Fixes (Do First - 90 minutes)

### 1.1 Add Missing G3 Bridge Skill (15 min)
**Location**: Between T08.G2.03 and T08.G3.00

**Action**: INSERT new skill
```
ID: T08.G3.00-pre
Skill: Match scenarios to if-block descriptions
Dependencies: T08.G2.03
```

**Update**: T08.G3.00 dependencies
```
Change: T07.G3.01, T08.G2.03
To: T07.G3.01, T08.G3.00-pre
```

---

### 1.2 Fix T08.G4.00 Dependencies (5 min)
```
Remove:
* T06.G2.01
* T06.G2.02
* T07.G2.01

Keep:
* T08.G3.05
```

---

### 1.3 Fix T08.G4.01 Dependencies (5 min)
```
Remove:
* T04.G2.03
* T06.G2.01
* T06.G2.02
* T06.G3.01
* T07.G2.01
* T08.G4.00

Keep:
* T08.G4.00b
* T08.G3.05
```

---

### 1.4 Fix T08.G4.02 Dependencies (5 min)
```
Remove (7 deps):
* T04.G2.01
* T04.G2.02
* T06.G2.01
* T06.G2.02
* T06.G2.03
* T06.G3.01
* T07.G2.01
* T08.G4.01

Keep:
* T08.G4.01c (will rename from G4.01b)
* T09.G3.01.04
```

---

### 1.5 Fix T08.G4.03 Dependencies (5 min)
```
Remove (5 deps):
* T01.G2.01
* T06.G2.01
* T06.G2.02
* T06.G3.01
* T07.G2.01
* T08.G4.01

Keep:
* T08.G4.02
* T13.G3.01
```

---

### 1.6 Fix T08.G4.04 Dependencies (5 min)
```
Remove (4 deps):
* T06.G2.01
* T06.G2.02
* T06.G3.01
* T07.G2.01
* T08.G4.03

Keep:
* T08.G4.03b
```

---

### 1.7 Fix T08.G4.05 Dependencies (5 min)
```
Remove (7 deps):
* T04.G2.01
* T04.G2.02
* T06.G2.01
* T06.G2.02
* T06.G2.03
* T07.G2.01
* T08.G4.03

Keep:
* T08.G4.04
```

---

### 1.8 Fix T08.G4.06 Dependencies (10 min) **CRITICAL BUG FIX**
```
Remove (3 deps):
* T06.G2.01
* T06.G2.02
* T07.G2.01
* T08.G4.01
* T08.G4.02
* T08.G4.05

Add (was missing!):
* T08.G4.04

New dependencies:
* T08.G4.04 [ADDED]
* T08.G4.05
* T08.G4.05b
```

---

### 1.9 Fix T08.G4.07 Dependencies (5 min)
```
Remove (3 deps):
* T06.G2.01
* T06.G2.02
* T07.G2.01

Keep:
* T08.G3.05
* T06.G3.02
* T09.G3.01.04
```

---

### 1.10 Fix T08.G4.08 Dependencies (5 min)
```
Remove (6 deps):
* T04.G2.03
* T06.G2.01
* T06.G2.02
* T07.G2.01
* T08.G4.01
* T08.G4.02
* T08.G4.05

Keep:
* T08.G4.05b
* T08.G4.03
* T13.G3.01
```

---

### 1.11 Fix T08.G4.09 Dependencies (5 min)
```
Remove (3 deps):
* T06.G2.01
* T06.G2.02
* T07.G2.01

Keep:
* T08.G3.04
* T13.G3.01
```

---

### 1.12 Fix T08.G5.00 Dependencies (5 min) **CRITICAL BUG FIX**
```
Change:
* T02.G2.01 (WRONG - sequential diagrams)

To:
* T08.G2.01 (CORRECT - branching paths)
```

---

### 1.13 Fix T08.G5.03 Dependencies (5 min)
```
Remove (2 deps):
* T09.G3.03
* T02.G5.01

Keep:
* T08.G4.05b
* T08.G4.08
```

---

## Phase 2: Structural Improvements (Do Second - 60 minutes)

### 2.1 Reorganize Boolean Operator Skills (30 min)

**Step 1**: RENAME existing skills
```
T08.G4.01a → T08.G4.00c (Understand OR truth table)
T08.G4.05a → T08.G4.00d (Understand NOT truth table)
T08.G4.01b → T08.G4.01c (Distinguish AND vs OR scenarios)
```

**Step 2**: ADD new skill T08.G4.01b
```
ID: T08.G4.01b
Skill: Identify situations requiring OR
Dependencies: T08.G4.01, T08.G4.00c
[Insert after T08.G4.01]
```

**Step 3**: Update all dependencies that referenced old IDs
- T08.G4.01a → T08.G4.00c (check G4 skills)
- T08.G4.01b → T08.G4.01c (check G4 skills)
- T08.G4.05a → T08.G4.00d (check G4 skills)

**Step 4**: Update T08.G4.00c dependencies
```
Old (when it was G4.01a):
* T08.G4.01

New:
* T08.G4.00 (parallel to AND truth table)
```

**Step 5**: Update T08.G4.00d dependencies
```
Old (when it was G4.05a):
* T08.G4.05

New:
* T08.G4.00c (after OR truth table)
```

**New G4 sequence**:
```
T08.G4.00  - AND truth table
T08.G4.00b - Identify AND situations
T08.G4.00c - OR truth table [moved]
T08.G4.00d - NOT truth table [moved]
T08.G4.01  - Combine AND
T08.G4.01b - Identify OR situations [new]
T08.G4.01c - Distinguish AND vs OR [renamed]
T08.G4.02  - Combine OR
T08.G4.02b - Choose AND vs OR in code [optional, see Phase 3]
T08.G4.03  - Trace compound conditionals
T08.G4.03a - Read nested if/else
T08.G4.03b - Identify nesting levels
T08.G4.04  - Nest if/else
T08.G4.05  - Use else-if
T08.G4.05b - Use NOT [keep here]
T08.G4.06  - Convert nested to cleaner
T08.G4.07  - Use if for state changes
T08.G4.08  - Fix compound logic bug
T08.G4.09  - Trace sequence of if/else
```

---

### 2.2 Merge G6 Simulation Skills (15 min)

**Step 1**: DELETE skills
```
T08.G6.01a - Use conditionals in physics simulations
T08.G6.01b - Use conditionals in population models
```

**Step 2**: UPDATE T08.G6.01
```
ID: T08.G6.01
Skill: Use conditionals to control simulation steps

Description: Students write conditionals that control simulation behavior across various domains: physics (collision detection "if sprite touching wall then reverse direction", boundary checking "if y < 0 then set y to 0"), biology (population dynamics "if population > carrying capacity then increase death rate", resource limits "if food < threshold then reduce birth rate"), or games (state transitions, win/loss conditions). Students complete projects in at least one domain. This applies conditional logic to scientific and mathematical modeling contexts.

Dependencies:
* T08.G5.03
* T08.G5.04

CSTA: E6-ALG-AF-01, E6-PRO-PF-01
```

---

### 2.3 Add G7 Bridge Skill (15 min)

**Step 1**: INSERT new skill after T08.G7.02
```
ID: T08.G7.03
Skill: Simplify complex boolean expressions

Description: Students apply boolean algebra rules (De Morgan's laws, distributive property, elimination of double negation) to simplify complex conditional expressions. For example, simplify "NOT(A OR B)" to "NOT A AND NOT B", or "if (A AND B) OR (A AND C)" to "if A AND (B OR C)". This develops formal logic skills and prepares students for analyzing logical equivalence in G8.

Dependencies:
* T08.G4.05b
* T08.G6.03

CSTA: E7-ALG-AF-01
```

**Step 2**: Update T08.G8.01 dependencies
```
Add to existing dependencies:
* T08.G7.03
```

---

## Phase 3: Optional Enhancements (30 minutes)

### 3.1 Add G4 Practice Skill (Optional)
**Location**: After T08.G4.02

```
ID: T08.G4.02b
Skill: Choose between AND and OR for coding scenarios

Description: Given scenario descriptions, students determine whether to use AND or OR and implement the correct compound condition. For example, "Alert if score is low OR time is running out" vs "Unlock door if player has key AND puzzle is solved". This applies conceptual understanding of boolean operators to practical coding decisions. Students complete 3-4 scenarios.

Dependencies:
* T08.G4.02
* T08.G4.01c

CSTA: E4-ALG-AF-01, E4-PRO-PF-01
```

---

## Validation Checklist

After implementing all changes, verify:

### ✅ Dependency Validation
- [ ] No T08 skill depends on a later T08 skill
- [ ] All G4 skills only depend on G2-G4 (X-2 rule)
- [ ] All G5 skills only depend on G3-G5 (X-2 rule)
- [ ] All G6 skills only depend on G4-G6 (X-2 rule)
- [ ] All G7 skills only depend on G5-G7 (X-2 rule)
- [ ] All G8 skills only depend on G6-G8 (X-2 rule)
- [ ] No circular dependencies within T08

### ✅ Content Validation
- [ ] K-2 skills are picture-based/unplugged (no coding)
- [ ] Grade 3+ skills involve block-based coding
- [ ] Each new concept introduced in one skill at a time
- [ ] Skill descriptions are clear and actionable

### ✅ Structural Validation
- [ ] All renamed skills updated everywhere
- [ ] All deleted skills removed from dependencies
- [ ] All new skills have complete descriptions
- [ ] CSTA standards included for all skills

### ✅ Cross-Topic Dependencies Preserved
- [ ] T06 (Events) dependencies unchanged
- [ ] T07 (Loops) dependencies unchanged
- [ ] T09 (Variables) dependencies unchanged
- [ ] T13 (Testing) dependencies unchanged
- [ ] Other cross-topic dependencies unchanged

---

## Files to Update

1. **Primary file**: `/media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md`
   - Lines 5534-6211 (T08 section)

2. **Backup**: Create backup before changes
   ```bash
   cp allskills.md allskills_backup_before_T08_phase1_$(date +%s).md
   ```

3. **Documentation**: Create optimization summary
   - `T08_optimization_summary.md`

---

## Testing After Implementation

### Test 1: Dependency Graph
Run dependency graph validator to check for:
- Circular dependencies
- Forward references
- X-2 rule violations

### Test 2: Skill Count
Verify skill counts by grade:
```
Grade K: 2 skills
Grade 1: 3 skills
Grade 2: 3 skills
Grade 3: 15 skills (was 14, added G3.00-pre)
Grade 4: 21 skills (was 19, added 00c, 00d, 01b, 02b [optional])
Grade 5: 6 skills (unchanged)
Grade 6: 3 skills (was 5, merged 01a and 01b into 01)
Grade 7: 3 skills (was 2, added G7.03)
Grade 8: 2 skills (unchanged)

Total: 58 skills (was 55, net +3)
[Or 57 if skipping optional G4.02b]
```

### Test 3: Cross-Topic Dependencies
Verify no cross-topic dependencies were accidentally removed:
```bash
grep "T06\|T07\|T09\|T13" T08_section.md | wc -l
# Should match original count
```

---

## Rollback Plan

If issues are discovered:

1. **Immediate rollback**: Restore from backup
   ```bash
   cp allskills_backup_before_T08_phase1_*.md allskills.md
   ```

2. **Partial rollback**: Revert specific phases
   - Phase 1 only: Keep new skills, restore old dependencies
   - Phase 2 only: Restore old skill numbers, keep dependency fixes
   - Phase 3 only: Remove optional skills

3. **Issue tracking**: Document any problems in `T08_issues_found.md`

---

## Success Metrics

### Quantitative:
- ✅ G4 dependencies reduced from 65 → 20 (69% reduction)
- ✅ X-2 violations reduced from 8 → 0 (100% elimination)
- ✅ Critical bugs fixed: 2 (G4.06 missing dep, G5.00 wrong dep)
- ✅ Missing skills added: 4 essential

### Qualitative:
- ✅ Improved learning progression (truth tables grouped)
- ✅ Better conceptual scaffolding (G3 and G7 bridges)
- ✅ Reduced maintenance burden (fewer dependencies)
- ✅ Clearer skill organization (operators logically sequenced)

---

## Timeline Estimate

| Phase | Task | Time | Cumulative |
|-------|------|------|------------|
| 1.1 | Add G3.00-pre | 15 min | 15 min |
| 1.2-1.13 | Fix 12 skill dependencies | 60 min | 75 min |
| 2.1 | Reorganize boolean operators | 30 min | 105 min |
| 2.2 | Merge G6 simulations | 15 min | 120 min |
| 2.3 | Add G7.03 bridge | 15 min | 135 min |
| Validation | Test and verify | 30 min | 165 min |
| **Total** | | **2h 45min** | |

Add 30 min buffer for Phase 3 optional skill: **3h 15min total**

---

## Contact for Questions

Review the following documents for details:
- **Full analysis**: `T08_comprehensive_analysis.md`
- **Proposed changes**: `T08_proposed_changes.md`
- **Issues summary**: `T08_issues_summary.md`
- **This guide**: `T08_implementation_guide.md`

---

## Quick Command Reference

### Create backup:
```bash
cd /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4
cp allskills.md allskills_backup_before_T08_phase1_$(date +%s).md
```

### Extract T08 section:
```bash
sed -n '5534,6211p' allskills.md > T08_current.md
```

### Count T08 skills:
```bash
grep "^ID: T08\." allskills.md | wc -l
```

### Count dependencies by skill:
```bash
grep -A 20 "^ID: T08\.G4\.01$" allskills.md | grep "^\* " | wc -l
```

### Verify no circular deps:
```bash
# (Use your dependency graph tool)
```

---

## Notes

- All changes are contained within T08 - no cross-topic impacts
- Dependency removals are conservative (only remove clear redundancies)
- New skills fill genuine gaps in progression
- Risk level is LOW - changes simplify rather than complicate
- Backward compatible - students who completed old G4 skills have all prerequisites for new sequence

**Recommendation**: Implement Phase 1 + Phase 2 now, defer Phase 3 to next iteration.
