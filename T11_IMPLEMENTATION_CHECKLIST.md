# T11 Implementation Checklist

**Purpose:** Step-by-step checklist for implementing T11 optimizations

---

## PRE-IMPLEMENTATION

### 1. Review & Approval
- [ ] Review T11_OPTIMIZATION_SUMMARY.md
- [ ] Review T11_PHASE1_ANALYSIS_REPORT.md for detailed rationale
- [ ] Review T11_QUICK_FIX_GUIDE.md for specific changes
- [ ] Get stakeholder approval for HIGH priority changes
- [ ] Decide whether to implement MEDIUM priority changes now or later

### 2. Backup
- [ ] Create backup of /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
- [ ] Note current git commit hash: `git rev-parse HEAD`
- [ ] Consider creating a branch: `git checkout -b optimize-t11-phase1`

---

## HIGH PRIORITY CHANGES (MUST DO)

### Dependency Fixes (10 skills)

#### T11.G4.02 - Add T11.G4.01, clean up

- [ ] **Find:** T11.G4.02 Dependencies section
- [ ] **Remove:** T06.G3.01, T08.G3.01
- [ ] **Add:** T11.G4.01 (as first dependency)
- [ ] **Keep:** T11.G3.03, T09.G3.01
- [ ] **Verify:** Dependencies are now: T11.G4.01, T11.G3.03, T09.G3.01

#### T11.G5.02 - Add T11.G4.01, remove T11.G4.04

- [ ] **Find:** T11.G5.02 Dependencies section
- [ ] **Remove:** T11.G4.04
- [ ] **Add:** T11.G4.01 (as first dependency)
- [ ] **Keep:** T11.G4.05
- [ ] **Verify:** Dependencies are now: T11.G4.01, T11.G4.05

#### T11.G6.01 - Remove G3 cross-topic dependencies

- [ ] **Find:** T11.G6.01 Dependencies section
- [ ] **Remove:** T08.G3.01, T09.G3.01
- [ ] **Keep:** T11.G5.03, T11.G5.04
- [ ] **Verify:** Dependencies are now: T11.G5.03, T11.G5.04

#### T11.G6.02 - Remove old dependencies

- [ ] **Find:** T11.G6.02 Dependencies section
- [ ] **Remove:** T06.G3.01, T11.G3.01
- [ ] **Keep:** T11.G5.03, T11.G5.04
- [ ] **Verify:** Dependencies are now: T11.G5.03, T11.G5.04

#### T11.G6.03 - Remove old dependencies

- [ ] **Find:** T11.G6.03 Dependencies section
- [ ] **Remove:** T06.G3.01, T08.G3.01
- [ ] **Keep:** T11.G5.03, T11.G5.04
- [ ] **Verify:** Dependencies are now: T11.G5.03, T11.G5.04

#### T11.G6.04 - Remove old dependencies

- [ ] **Find:** T11.G6.04 Dependencies section
- [ ] **Remove:** T06.G3.01, T09.G3.01
- [ ] **Keep:** T11.G5.03, T11.G5.04
- [ ] **Verify:** Dependencies are now: T11.G5.03, T11.G5.04

#### T11.G7.01 - Remove old dependency

- [ ] **Find:** T11.G7.01 Dependencies section
- [ ] **Remove:** T01.G5.01
- [ ] **Keep:** T09.G5.01, T11.G6.03, T11.G6.04
- [ ] **Verify:** Dependencies are now: T09.G5.01, T11.G6.03, T11.G6.04

#### T11.G7.02 - Remove old dependencies

- [ ] **Find:** T11.G7.02 Dependencies section
- [ ] **Remove:** T06.G3.01, T09.G5.01
- [ ] **Keep:** T11.G6.03, T11.G6.04
- [ ] **Verify:** Dependencies are now: T11.G6.03, T11.G6.04

#### T11.G7.03 - Fix data error and remove old dependencies

- [ ] **Find:** T11.G7.03 Dependencies section
- [ ] **Remove:** T09.G5.01, T11.G5.01 (NOTE: This has wrong skill name!)
- [ ] **Keep:** T11.G6.03, T11.G6.04
- [ ] **Verify:** Dependencies are now: T11.G6.03, T11.G6.04
- [ ] **Double-check:** No reference to T11.G5.01 remains

#### T11.G7.04 - Remove old dependencies

- [ ] **Find:** T11.G7.04 Dependencies section
- [ ] **Remove:** T06.G3.01, T08.G5.01
- [ ] **Keep:** T11.G6.03, T11.G6.04
- [ ] **Verify:** Dependencies are now: T11.G6.03, T11.G6.04

### Post-Dependency Fix Validation

- [ ] Count total T11 dependencies: should be ~40 (down from ~71)
- [ ] Search for "T06.G3.01" in T11 skills: should find 0 matches in dependencies
- [ ] Search for "T08.G3.01" in T11 skills: should find 0 matches in dependencies
- [ ] Search for "T09.G3.01" in T11 G6+ skills: should find 0 matches
- [ ] Verify T11.G4.01 appears in: T11.G4.02, T11.G5.02 dependencies
- [ ] Run X-2 validation (see validation section below)

---

## MEDIUM PRIORITY CHANGES (RECOMMENDED)

### Description Updates (7 skills)

#### T11.G3.01 - Clarify assessment

- [ ] **Find:** T11.G3.01 Description
- [ ] **Replace:** Current description
- [ ] **With:** New description from Quick Fix Guide (section 11)
- [ ] **Verify:** Includes concrete assessment example

#### T11.G3.03 - Clarify "highlight"

- [ ] **Find:** T11.G3.03 Description
- [ ] **Replace:** Current description
- [ ] **With:** New description from Quick Fix Guide (section 12)
- [ ] **Verify:** Specifies "drawing boxes and labeling"

#### T11.G4.02 - Use standard terminology

- [ ] **Find:** T11.G4.02 Skill name and Description
- [ ] **Replace:** "action blocks" with "command blocks"
- [ ] **Update:** Description per Quick Fix Guide (section 13)
- [ ] **Verify:** Uses "command blocks" and "reporter blocks" consistently

#### T11.G4.04 - Clarify high-level vs low-level

- [ ] **Find:** T11.G4.04 Description
- [ ] **Replace:** Current description
- [ ] **With:** New description from Quick Fix Guide (section 14)
- [ ] **Verify:** Emphasizes "WHAT" (purpose) not "HOW" (implementation)

#### T11.G4.05 - Clarify tracing vs describing

- [ ] **Find:** T11.G4.05 Description
- [ ] **Replace:** Current description
- [ ] **With:** New description from Quick Fix Guide (section 14)
- [ ] **Verify:** Emphasizes "LOW-LEVEL tracing" and distinguishes from G4.04

#### T11.G6.01 - Explain interface-first

- [ ] **Find:** T11.G6.01 Description
- [ ] **Replace:** Current description
- [ ] **With:** New description from Quick Fix Guide (section 15)
- [ ] **Verify:** Explains "interface-first thinking" in K-8 terms

#### T11.G7.03 - K-8 friendly language

- [ ] **Find:** T11.G7.03 Description
- [ ] **Replace:** Current description
- [ ] **With:** New description from Quick Fix Guide (section 16)
- [ ] **Verify:** Uses "black box" metaphor and explains encapsulation clearly

#### T11.G8.03 - Clarify "objects"

- [ ] **Find:** T11.G8.03 Description
- [ ] **Replace:** "objects with multiple attributes"
- [ ] **With:** Updated description from Quick Fix Guide (section 17)
- [ ] **Verify:** Clarifies how to represent structured data in Scratch

---

## LOW PRIORITY CHANGES (OPTIONAL)

### Polish (2 skills)

#### T11.G3.04 - Active voice

- [ ] **Find:** T11.G3.04 Description
- [ ] **Replace:** "Students are introduced to the idea"
- [ ] **With:** "Students learn that"
- [ ] **Update:** Full description per Quick Fix Guide (section 18)

#### T11.G4.03 - Better examples

- [ ] **Find:** T11.G4.03 Description
- [ ] **Update:** Examples per Quick Fix Guide (section 19)
- [ ] **Verify:** Examples clearly show reporter blocks in expressions

---

## VALIDATION

### Automated Checks

Run these commands to validate changes:

#### Check no skills deleted
```bash
grep -c "^ID: T11\." /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md
# Should return: 26
```

#### Check cross-topic dependencies preserved
```bash
grep -A 10 "^ID: T14.G3.07" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T11.G3.01"
grep -A 10 "^ID: T14.G3.10" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T11.G3.02"
grep -A 10 "^ID: T15.G3.07" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T11.G3.01"
grep -A 10 "^ID: T15.G3.09" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T11.G3.02"
grep -A 10 "^ID: T18.G3.08" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T11.G3.01"
# All should find matches
```

#### Check no X-2 violations from G3 to G6+
```bash
# Should find NO matches in G6+ skills:
grep -A 10 "^ID: T11.G6" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T06.G3.01"
grep -A 10 "^ID: T11.G6" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T08.G3.01"
grep -A 10 "^ID: T11.G6" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T09.G3.01"
grep -A 10 "^ID: T11.G6" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T11.G3.01"

grep -A 10 "^ID: T11.G7" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T06.G3.01"
grep -A 10 "^ID: T11.G7" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T11.G5.01"
# All should return NO matches
```

#### Check critical T11.G4.01 added
```bash
grep -A 10 "^ID: T11.G4.02" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T11.G4.01"
grep -A 10 "^ID: T11.G5.02" /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md | grep "T11.G4.01"
# Both should find matches
```

### Manual X-2 Rule Validation

For each T11 skill, verify dependencies are at most 2 grades back:

- [ ] **G3 skills:** Check dependencies (should be from other topics or none)
- [ ] **G4 skills:** Verify dependencies from G3-G4 only (max 1 grade back)
- [ ] **G5 skills:** Verify dependencies from G3-G5 only (max 2 grades back)
- [ ] **G6 skills:** Verify dependencies from G4-G6 only (max 2 grades back)
- [ ] **G7 skills:** Verify dependencies from G5-G7 only (max 2 grades back)
- [ ] **G8 skills:** Verify dependencies from G6-G8 only (max 2 grades back)

### Logical Progression Validation

- [ ] **G3 → G4:** All G4 skills have at least one G3 prerequisite
- [ ] **Creation before parameters:** T11.G5.02 depends on T11.G4.01
- [ ] **Understanding before creation:** T11.G4.01 depends on T11.G3.04
- [ ] **Analysis before design:** All G6 skills depend on G5 analysis skills
- [ ] **Design before advanced:** All G7 skills depend on G6 design skills
- [ ] **Advanced before architecture:** All G8 skills depend on G7 skills

---

## POST-IMPLEMENTATION

### Documentation

- [ ] Update changelog or version notes
- [ ] Document date of changes
- [ ] Note any deviations from recommended changes
- [ ] Save these analysis files for future reference

### Git Workflow

- [ ] Stage changes: `git add skillsv4/allskills.md`
- [ ] Commit with descriptive message:
  ```bash
  git commit -m "Optimize T11 (Functions & Procedures) - Phase 1

  - Remove 31 dependencies (18 within-T11, 13 cross-topic)
  - Add 2 critical dependencies (T11.G4.01 prerequisites)
  - Fix X-2 violations (15 → 0)
  - Update 7 skill descriptions for clarity
  - Fix data integrity error in T11.G7.03

  No skills deleted. All cross-topic dependencies preserved.
  See T11_OPTIMIZATION_SUMMARY.md for details."
  ```
- [ ] Push to branch or merge to main as appropriate

### Testing & Validation (if applicable)

- [ ] Pilot with small group of students (if possible)
- [ ] Verify assessment materials align with updated descriptions
- [ ] Test CreatiCode features mentioned in skills
- [ ] Gather feedback from educators

### Follow-up

- [ ] Schedule review after 1-2 weeks of use
- [ ] Note any issues or improvements needed
- [ ] Consider Phase 2 optimization for other topics
- [ ] Review whether other topics should depend on optimized T11 skills

---

## ROLLBACK PLAN

If issues are discovered:

### Quick Rollback (Git)
```bash
git checkout [previous-commit-hash] -- skillsv4/allskills.md
git commit -m "Rollback T11 optimization - found issue: [describe issue]"
```

### Partial Rollback

If only specific changes cause issues:
1. Identify problematic change from T11_QUICK_FIX_GUIDE.md
2. Reverse that specific change only
3. Document why the change was reverted
4. Consider alternative fix

---

## COMPLETION CHECKLIST

### Minimum (HIGH Priority Only)
- [ ] All 10 HIGH priority dependency changes implemented
- [ ] All automated validation checks pass
- [ ] Manual X-2 validation complete
- [ ] Git commit created
- [ ] Documentation updated

### Recommended (HIGH + MEDIUM Priority)
- [ ] All HIGH priority changes implemented ✓
- [ ] 7 MEDIUM priority description updates implemented
- [ ] All validation checks pass
- [ ] Terminology standardized across T11
- [ ] Git commit created
- [ ] Documentation updated

### Complete (ALL Priorities)
- [ ] All HIGH + MEDIUM changes implemented ✓
- [ ] 2 LOW priority polish changes implemented
- [ ] All validation checks pass
- [ ] Testing completed (if applicable)
- [ ] Feedback gathered
- [ ] Follow-up scheduled
- [ ] Git commit created
- [ ] Documentation complete

---

## NOTES

**Estimated time:**
- HIGH priority only: 1-2 hours (mostly find/replace)
- HIGH + MEDIUM: 2-3 hours (includes description updates)
- ALL priorities: 3-4 hours (includes testing and documentation)

**Best practices:**
- Work on one skill at a time
- Verify each change before moving to next
- Use search/replace carefully (skill IDs look similar)
- Test automated checks frequently
- Commit frequently if making many changes

**Common pitfalls:**
- Accidentally modifying skills from other topics
- Missing a dependency in a multi-line dependency list
- Copying wrong skill ID (T11.G3.01 vs T11.G5.01)
- Removing cross-topic dependencies that should be preserved

---

## REFERENCE

**Analysis files:**
- Summary: T11_OPTIMIZATION_SUMMARY.md
- Full report: T11_PHASE1_ANALYSIS_REPORT.md
- Change guide: T11_QUICK_FIX_GUIDE.md
- Dependency viz: T11_DEPENDENCY_VISUALIZATION.md
- This checklist: T11_IMPLEMENTATION_CHECKLIST.md

**Working directory:**
- /media/binyu/USB2/dev/CreatiCodeSkillMap

**Main file:**
- /media/binyu/USB2/dev/CreatiCodeSkillMap/skillsv4/allskills.md

**Analysis date:** 2025-11-20
