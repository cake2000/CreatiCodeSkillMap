# Creative Skills + ACSL Cleanup Integration Plan

**Date:** 2025-11-17
**Purpose:** Step-by-step guide for integrating 3 new creative skills and 9 modified ACSL cleanup skills into the main curriculum

---

## Overview

This document provides a complete integration plan for:

### Part A: 3 New Creative Skills
- T20.G7.05 - Design a Visual Theme for Your Project
- T16.G7.06 - Add Delightful Details to Your Interface
- T05.G6.07 - Brainstorm Creative Solutions with Ideation Techniques

### Part B: 9 Modified Skills (ACSL Cleanup)
- 3 skills marked as competition-only
- 6 skills reframed with better language

---

## Section 1: Integration Steps

### Step 1: Backup Current Data

**Before making any changes:**

```bash
# Create backup of main skills file
cp skills_k8_ai_complete_WEEK2.json skills_k8_ai_complete_WEEK2.BACKUP_$(date +%Y%m%d).json

# Verify backup created successfully
ls -lh skills_k8_ai_complete_WEEK2.BACKUP_*.json
```

**Purpose:** Safety net in case we need to revert changes

---

### Step 2: Add 3 New Creative Skills

**Source File:** `CREATIVE_SKILLS_3.json`

**Integration Method:** Append to main skills array

```python
import json

# Load existing skills
with open('skills_k8_ai_complete_WEEK2.json', 'r') as f:
    skills = json.load(f)

# Load new creative skills
with open('CREATIVE_SKILLS_3.json', 'r') as f:
    new_creative_skills = json.load(f)

# Find insertion points (maintain sorted order by topic and grade)
# T05.G6.07 goes after T05.G6.06
# T16.G7.06 goes after T16.G7.05
# T20.G7.05 goes after T20.G7.04

# Insert skills in appropriate positions
# (Implementation details below)
```

**Insertion Points:**

1. **T05.G6.07** → Insert after T05.G6.06 (index based on current position)
2. **T16.G7.06** → Insert after T16.G7.05
3. **T20.G7.05** → Insert after T20.G7.04

**Validation After Insertion:**
- Verify 3 new skills present
- Verify IDs are unique (no duplicates)
- Verify JSON structure is valid

---

### Step 3: Modify 3 Competition-Only Skills

**Skills to Modify:**
- T02.G7.03
- T01.G6.01
- T04.G6.04

**Changes to Apply:**

```python
competition_only_updates = {
    'T02.G7.03': {
        'difficulty_track': 'competition',
        'competition_tags': ['ACSL Junior'],
        'optional': True,
        'theoretical_cs': True
    },
    'T01.G6.01': {
        'difficulty_track': 'competition',
        'competition_tags': ['ACSL Junior'],
        'optional': True,
        'theoretical_cs': True
    },
    'T04.G6.04': {
        'difficulty_track': 'competition',
        'competition_tags': ['ACSL Junior'],
        'optional': True,
        'theoretical_cs': True
    }
}

# Apply updates to each skill
for skill in skills:
    if skill['id'] in competition_only_updates:
        skill.update(competition_only_updates[skill['id']])
```

**Validation:**
- All 3 skills have `difficulty_track: "competition"`
- All 3 have `ACSL Junior` competition tag
- All 3 marked as optional
- New field `theoretical_cs: true` added

---

### Step 4: Reframe 6 Skills with Better Language

**Skills to Modify:**

| Skill ID | New Title | Terminology Change |
|----------|-----------|-------------------|
| T02.G4.03 | Plan step-by-step before coding | pseudocode → planning |
| T02.G5.03 | Plan your code with steps | pseudocode → planning |
| T02.G6.03 | Plan complex code with multiple steps | nested structures → complex logic |
| T01.G7.02 | Choose the right approach for your problem | algorithms → approaches |
| T01.G7.04 | Test your code with unusual inputs | analyze correctness → testing |
| T02.G7.04 | Debug by following your code step-by-step | trace algorithm → debugging |

**Implementation:**

```python
reframed_updates = {
    'T02.G4.03': {
        'title': 'Plan step-by-step before coding',
        'description': 'Given a real-world process (e.g., "make a peanut butter sandwich") or a task description, students write out the steps in simple, clear language before turning it into code. This planning helps students think through the logic before they start coding. Example: "1. Get two slices of bread. 2. Spread peanut butter on one slice. 3. Put slices together." This skill teaches that clear planning makes coding easier and helps catch mistakes before they happen.',
        'terminology_simplified': 'pseudocode → step-by-step planning'
    },
    'T02.G5.03': {
        'title': 'Plan your code with steps',
        'description': 'Before coding a complex feature (like a game level or animation sequence), students write out the steps in plain English with structure that shows loops and decisions. Example: "For each enemy: Check if player is nearby. If yes, move toward player. If no, keep patrolling." This teaches students to plan complex logic before coding, making it easier to translate their thinking into actual code blocks.',
        'terminology_simplified': 'pseudocode → planning steps'
    },
    'T02.G6.03': {
        'title': 'Plan complex code with multiple steps',
        'description': 'For complex game or app logic with nested patterns, students plan out the structure before coding. Example: "For each row in the grid: For each column in that row: Check if there\'s a match. If match found: Add to score and remove item." Planning nested logic on paper first helps students visualize the structure before building it in code blocks. This is especially useful for grid-based games, nested menus, or complex animations.',
        'terminology_simplified': 'nested pseudocode → planning complex logic'
    },
    'T01.G7.02': {
        'title': 'Choose the right approach for your problem',
        'description': 'When solving a coding problem, students learn to consider multiple approaches and choose the best one for their situation. Example: Should I use a loop or make a custom block? Should I store this in a variable or a list? Should I use broadcast messages or direct sprite interactions? Students justify their choice based on what makes the code clearer, easier to maintain, or better suited to their specific project. This develops practical decision-making about code structure.',
        'terminology_simplified': 'algorithms → coding approaches'
    },
    'T01.G7.04': {
        'title': 'Test your code with unusual inputs',
        'description': 'Students learn to test their code with edge cases - unusual situations that might break their program. Examples: What happens if the player has 0 lives? 1000 enemies? An empty username? Maximum score? Students run their code with these extreme cases to find bugs before users do. This teaches thorough testing: if your code works with weird inputs, it\'ll definitely work with normal ones. This is how professional developers ensure their apps don\'t crash.',
        'terminology_simplified': 'algorithm analysis → code testing'
    },
    'T02.G7.04': {
        'title': 'Debug by following your code step-by-step',
        'description': 'When code doesn\'t work as expected, students learn to trace through it step-by-step to find the bug. They follow the logic: "First this variable is set to 5. Then the loop runs 3 times. On the third time, wait - that\'s wrong!" This step-by-step debugging helps students find exactly where their logic breaks. It\'s like being a detective following clues to find where the problem happened. This is a fundamental debugging skill used by all programmers.',
        'terminology_simplified': 'algorithm tracing → step-by-step debugging'
    }
}

# Apply updates
for skill in skills:
    if skill['id'] in reframed_updates:
        skill.update(reframed_updates[skill['id']])
```

**Validation:**
- All 6 skills have updated titles
- All 6 have updated descriptions with practical language
- All 6 have `terminology_simplified` field documenting change

---

### Step 5: Update Dependency Counts

After adding new skills, some dependency counts may need updating:

**Skills that now have new dependents:**

- **T16.G7.05** → New dependent: T16.G7.06
- **T20.G7.04** → May be referenced by T20.G7.05 (check dependencies)
- **T05.G6.06** → May be near T05.G6.07 (check dependencies)

**Recalculate dependency counts:**

```python
# For each skill, count how many other skills list it as a dependency
for skill in skills:
    skill['dependency_count'] = len(skill.get('dependencies', []))
```

---

### Step 6: Save Integrated File

```python
# Save updated skills
with open('skills_k8_ai_complete_WEEK2_INTEGRATED.json', 'w') as f:
    json.dump(skills, f, indent=2, ensure_ascii=False)

# Verify file is valid JSON
import json
with open('skills_k8_ai_complete_WEEK2_INTEGRATED.json', 'r') as f:
    test_load = json.load(f)
    print(f"Successfully loaded {len(test_load)} skills")
```

---

## Section 2: Validation Checklist

### Pre-Integration Validation

- [ ] Backup created successfully
- [ ] All source files present (CREATIVE_SKILLS_3.json, ACSL_CLEANUP_APPLIED.json)
- [ ] Current skill count documented

### Post-Integration Validation

**Skill Count:**
- [ ] Total skills increased by 3 (new creative skills added)
- [ ] No skills deleted (competition skills still present, just marked differently)

**New Skills Validation:**
- [ ] T05.G6.07 present with all required fields
- [ ] T16.G7.06 present with all required fields
- [ ] T20.G7.05 present with all required fields
- [ ] All 3 have complete auto_grade_rules
- [ ] All 3 have accessibility configuration
- [ ] All 3 have proper CSTA codes

**Competition-Only Skills Validation:**
- [ ] T02.G7.03 has `difficulty_track: "competition"`
- [ ] T01.G6.01 has `difficulty_track: "competition"`
- [ ] T04.G6.04 has `difficulty_track: "competition"`
- [ ] All 3 have `competition_tags: ["ACSL Junior"]`
- [ ] All 3 have `optional: true`
- [ ] All 3 have `theoretical_cs: true`

**Reframed Skills Validation:**
- [ ] T02.G4.03 title updated, has `terminology_simplified`
- [ ] T02.G5.03 title updated, has `terminology_simplified`
- [ ] T02.G6.03 title updated, has `terminology_simplified`
- [ ] T01.G7.02 title updated, has `terminology_simplified`
- [ ] T01.G7.04 title updated, has `terminology_simplified`
- [ ] T02.G7.04 title updated, has `terminology_simplified`

**Dependency Validation:**
- [ ] No broken dependencies (all referenced skill IDs exist)
- [ ] Dependency counts accurate
- [ ] No circular dependencies

**JSON Structure Validation:**
- [ ] File is valid JSON (parses without errors)
- [ ] All required fields present on all skills
- [ ] No duplicate skill IDs
- [ ] Grade values consistent (K or 1-8)

---

## Section 3: Dependency Analysis

### New Skills Dependencies

**T05.G6.07 (Ideation Techniques):**
- Dependencies: [] (none - foundational skill)
- Impact: Can be taught early, before any project skills

**T16.G7.06 (Delightful Details):**
- Dependencies: ['T16.G7.05', 'T16.G6.01']
- Impact: Requires UI mockup skills before adding polish

**T20.G7.05 (Visual Theme):**
- Dependencies: ['T16.G6.05', 'T20.G6.01']
- Impact: Requires basic design and art skills

### Modified Skills Dependencies

**Competition-Only Skills:**

All 3 competition-only skills keep their existing dependencies. Students who choose to take them will still need prerequisites, but standard track students don't need to take them at all.

**Reframed Skills:**

Dependencies unchanged - only language improved, not skill structure.

### Reverse Dependencies (Who depends on modified skills?)

**Important:** Check if any standard track skills depend on the 3 competition-only skills:

```python
# Check reverse dependencies
competition_only_ids = ['T02.G7.03', 'T01.G6.01', 'T04.G6.04']

for comp_id in competition_only_ids:
    dependents = [s['id'] for s in skills if comp_id in s.get('dependencies', [])]
    print(f"{comp_id} is depended on by: {dependents}")
```

**Expected Results:**
- T02.G7.03: No standard track dependents
- T01.G6.01: Only T02.G7.03 (also competition-only)
- T04.G6.04: No standard track dependents

If any standard track skills depend on competition-only skills, those dependencies must be removed or those skills must also be marked competition-only.

---

## Section 4: Testing Plan

### Automated Tests

**Test 1: JSON Validity**
```python
import json
with open('skills_k8_ai_complete_WEEK2_INTEGRATED.json', 'r') as f:
    skills = json.load(f)
    assert len(skills) > 0, "Skills loaded successfully"
```

**Test 2: No Duplicate IDs**
```python
skill_ids = [s['id'] for s in skills]
assert len(skill_ids) == len(set(skill_ids)), "No duplicate IDs"
```

**Test 3: All Required Fields Present**
```python
required_fields = ['id', 'title', 'topic_id', 'grade', 'description',
                   'dependencies', 'csta_code', 'difficulty_track']

for skill in skills:
    for field in required_fields:
        assert field in skill, f"Skill {skill['id']} missing {field}"
```

**Test 4: Dependency Validity**
```python
valid_ids = set([s['id'] for s in skills])

for skill in skills:
    for dep in skill.get('dependencies', []):
        assert dep in valid_ids, f"Skill {skill['id']} has invalid dependency: {dep}"
```

**Test 5: New Skills Present**
```python
new_skill_ids = ['T05.G6.07', 'T16.G7.06', 'T20.G7.05']
existing_ids = set([s['id'] for s in skills])

for new_id in new_skill_ids:
    assert new_id in existing_ids, f"New skill {new_id} not found"
```

**Test 6: Competition Skills Properly Tagged**
```python
competition_ids = ['T02.G7.03', 'T01.G6.01', 'T04.G6.04']

for skill in skills:
    if skill['id'] in competition_ids:
        assert skill['difficulty_track'] == 'competition', f"{skill['id']} not marked competition"
        assert 'ACSL Junior' in skill['competition_tags'], f"{skill['id']} missing ACSL tag"
        assert skill.get('optional') == True, f"{skill['id']} not marked optional"
```

### Manual Testing

**Teacher Review:**
1. Read through reframed skill descriptions
2. Confirm language is clearer and more practical
3. Verify examples are relevant to students' projects

**Student Pilot:**
1. Show new creative skill prompts to students
2. Observe if they understand what to do
3. Gather feedback on clarity

---

## Section 5: Rollout Strategy

### Phase 1: Internal Testing (Week 1)
- Apply integration to test database
- Run all automated validation tests
- Manual review by curriculum team
- Fix any issues found

### Phase 2: Teacher Preview (Week 2)
- Share integrated curriculum with 3-5 pilot teachers
- Provide CREATIVE_SKILLS_SPECS.md for new skills
- Provide ACSL_CLEANUP_REPORT.md for language changes
- Gather feedback on clarity and usefulness

### Phase 3: Limited Rollout (Week 3-4)
- Deploy to 1-2 classrooms
- Monitor student engagement with new creative skills
- Track: Do students understand reframed language better?
- Adjust based on feedback

### Phase 4: Full Deployment (Week 5+)
- Deploy to all classrooms
- Update teacher documentation
- Update student-facing curriculum guides
- Monitor metrics

---

## Section 6: Documentation Updates

### Files to Update

**1. competition_paths.md**
- Add section explaining ACSL Junior optional track
- List 3 competition-only skills clearly
- Clarify: standard track students don't need these

**2. DELIVERABLES_INDEX.md**
- Add entries for new creative skills
- Add entry for ACSL cleanup
- Update statistics (total skills, creative skills count)

**3. README.md (if exists)**
- Update skill count
- Mention creative skills enhancement
- Mention ACSL cleanup for accessibility

**4. WEEK2_CREATIVITY_ANALYSIS.md**
- Add note that gaps have been filled
- Reference new creative skills
- Mark analysis as "ADDRESSED"

---

## Section 7: Metrics to Track

### Success Metrics

**For New Creative Skills:**
- Student engagement: Do students spend more time on visual design?
- Project quality: Do final projects show more visual consistency?
- Competition success: Do projects submitted to contests show stronger design?

**For ACSL Cleanup:**
- Comprehension: Do students understand reframed language better?
- Completion rate: Do more students complete reframed skills?
- Teacher feedback: Do teachers report clearer instruction with new language?

### Data to Collect

**Week 1 Baseline (Before Integration):**
- % students completing theoretical skills (T02.G7.03, etc.)
- Time spent on planning/pseudocode skills
- Teacher reports on student confusion

**Week 4-8 Post-Integration:**
- % students completing reframed skills (should increase)
- % students choosing competition track (should be small subset)
- Student feedback: "Is the language clearer?"
- Project visual quality scores

**Week 12+ Long-term:**
- Competition submission quality
- Student retention in creative vs competition tracks
- Teacher satisfaction with curriculum clarity

---

## Section 8: Rollback Plan

If integration causes issues:

### Quick Rollback (Emergency)
```bash
# Restore from backup
cp skills_k8_ai_complete_WEEK2.BACKUP_20251117.json skills_k8_ai_complete_WEEK2.json

# Verify restoration
python -c "import json; print(len(json.load(open('skills_k8_ai_complete_WEEK2.json'))))"
```

### Partial Rollback (Specific Skills)

If only certain skills cause issues:

**Option 1: Remove problematic new skill**
- Filter out T20.G7.05 (or whichever is problematic)
- Restore from integrated version

**Option 2: Revert language changes**
- Keep competition-only changes
- Restore original language for reframed skills

**Option 3: Keep skills, adjust difficulty**
- Keep all changes
- Add more scaffolding for challenging skills

---

## Section 9: Communication Plan

### Stakeholder Communication

**To Teachers:**

**Subject:** New Creative Skills + Clearer Language in Curriculum

**Message:**
> We've added 3 new creative skills to enhance visual design and ideation instruction:
> - Design a Visual Theme (G7) - Color theory and typography
> - Add Delightful Details (G7) - Microinteractions and polish
> - Brainstorm Creative Solutions (G6) - Ideation techniques
>
> We've also improved language in 6 planning/debugging skills, removing CS jargon and adding practical examples.
>
> Additionally, 3 theoretical algorithm analysis skills are now optional (ACSL competition track only).
>
> Full documentation: CREATIVE_SKILLS_SPECS.md and ACSL_CLEANUP_REPORT.md

**To Students:**

**Message:**
> We've added new activities to help you make your projects look amazing and help you brainstorm creative ideas! We've also made some instructions clearer and easier to understand.

**To Parents/Administrators:**

**Message:**
> Curriculum enhanced with explicit creative design instruction and more accessible language. Standard curriculum focuses on creative project development; theoretical computer science content now optional for students interested in competitions.

---

## Section 10: Implementation Checklist

### Pre-Integration
- [ ] Read all documentation (CREATIVE_SKILLS_3.json, ACSL_CLEANUP_APPLIED.json, reports)
- [ ] Create backup of current skills file
- [ ] Set up testing environment
- [ ] Prepare rollback plan

### Integration
- [ ] Run integration script
- [ ] Verify 3 new skills added
- [ ] Verify 3 skills marked competition-only
- [ ] Verify 6 skills reframed
- [ ] Run all automated tests
- [ ] Manual review of changes

### Post-Integration
- [ ] Update documentation files
- [ ] Update competition pathways guide
- [ ] Prepare teacher training materials
- [ ] Set up metrics tracking
- [ ] Deploy to test environment

### Rollout
- [ ] Phase 1: Internal testing complete
- [ ] Phase 2: Teacher preview complete
- [ ] Phase 3: Limited rollout complete
- [ ] Phase 4: Full deployment
- [ ] Monitor metrics
- [ ] Gather feedback

---

## Section 11: Expected Outcomes

### Immediate Outcomes (Week 1-2)

**From New Creative Skills:**
- Students explicitly learn color theory and typography
- Students practice structured ideation before jumping to code
- Students add polish and personality to interfaces

**From ACSL Cleanup:**
- 3 fewer theoretical skills required for standard track
- 6 skills have clearer, more practical language
- Students understand planning/debugging skills better

### Medium-term Outcomes (Month 1-3)

**Creative Skills:**
- Final projects show more visual consistency
- Projects have more personality and delightful details
- Students can articulate design decisions

**ACSL Cleanup:**
- Higher completion rates for reframed skills
- Fewer teacher questions about "what is pseudocode?"
- Competition track students clearly separated

### Long-term Outcomes (6+ months)

**Creative Skills:**
- Competition submissions show stronger design
- Student portfolios demonstrate design thinking
- Increased student engagement with visual aspects

**ACSL Cleanup:**
- Curriculum perceived as more accessible
- Clear pathways for both creative and competition students
- Teacher satisfaction with curriculum clarity

---

## Conclusion

This integration plan provides:

1. **Step-by-step integration instructions** for adding 3 creative skills
2. **Clear modification process** for 9 ACSL cleanup skills
3. **Comprehensive validation** to ensure no broken dependencies
4. **Testing strategy** for quality assurance
5. **Rollout plan** for careful deployment
6. **Rollback procedures** for safety
7. **Success metrics** for evaluation

**Timeline:**
- Integration: 1 day
- Testing: 1 week
- Teacher preview: 1 week
- Limited rollout: 2 weeks
- Full deployment: Week 5+

**Risk Level:** LOW
- All changes are additive or clarifying
- No skills removed
- No broken dependencies
- Easy rollback available

**Expected Impact:** HIGH
- Fills critical creative skills gaps
- Removes theoretical barriers for standard track
- Improves language accessibility
- Maintains rigor for competition students

---

**Document Status:** Ready for implementation
**Next Action:** Execute Step 1 (Create Backup)
**Questions?** Refer to CREATIVE_SKILLS_SPECS.md and ACSL_CLEANUP_REPORT.md for details
