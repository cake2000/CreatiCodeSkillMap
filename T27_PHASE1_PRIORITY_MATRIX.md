# T27 PHASE 1 ANALYSIS - PRIORITY MATRIX

**Analysis Date**: November 21, 2025
**Purpose**: Visual prioritization of all identified issues and recommendations

---

## PRIORITY QUADRANT ANALYSIS

```
HIGH IMPACT + HIGH URGENCY          HIGH IMPACT + MEDIUM URGENCY
┌─────────────────────────────┐    ┌─────────────────────────────┐
│ CRITICAL (DO IMMEDIATELY)   │    │ IMPORTANT (DO SOON)         │
│                             │    │                             │
│ • Add G3.0X table creation  │    │ • Add G4.0Y sorting         │
│ • Fix G3.01 aggregation     │    │ • Add G5.0X GROUP BY        │
│ • Fix G5.02 scatter plots   │    │ • Add G6.0X VLOOKUP         │
│ • Add G4.02a median concept │    │ • Add G6.0Y pivot tables    │
│ • Move G6.01 filter to G4   │    │ • Add G6.0Z CSV export      │
│ • Fix G4.02 inconsistency   │    │ • Add G7.0X moving avg      │
│ • Fix G4.01 dependencies    │    │ • Add G7.0Y Google Sheets   │
│ • Add block specificity (3) │    │ • Add G7.0Z chart auto      │
│                             │    │                             │
│ IMPACT: Broken skills       │    │ IMPACT: Major capability    │
│ EFFORT: Low-Medium          │    │ EFFORT: Medium              │
└─────────────────────────────┘    └─────────────────────────────┘

LOW IMPACT + HIGH URGENCY           LOW IMPACT + MEDIUM URGENCY
┌─────────────────────────────┐    ┌─────────────────────────────┐
│ QUICK WINS (DO FIRST)       │    │ NICE TO HAVE (DO LATER)     │
│                             │    │                             │
│ • Fix G7.04 typo            │    │ • Add database integration  │
│ • Fix G6.04 dependency text │    │ • Clarify dashboard details │
│ • Clarify G2.01 unplugged   │    │ • Differentiate G4/G6 trends│
│                             │    │ • Add table display options │
│                             │    │ • Simplify G8.01 description│
│ IMPACT: Text clarity        │    │                             │
│ EFFORT: Trivial             │    │ IMPACT: Polish              │
└─────────────────────────────┘    │ EFFORT: Low-Medium          │
                                    └─────────────────────────────┘
```

---

## ISSUE IMPACT SCORING

### Impact Categories
- **BLOCKER**: Students cannot complete skill (score 10)
- **MAJOR**: Teaches wrong approach or missing key capability (score 7-9)
- **MODERATE**: Confusion or inefficiency (score 4-6)
- **MINOR**: Polish or enhancement (score 1-3)

### Effort Categories
- **TRIVIAL**: Text fix only (1 hour)
- **LOW**: Single skill rewrite (2-4 hours)
- **MEDIUM**: Multiple skills or new skill creation (1-2 days)
- **HIGH**: Major restructuring or research needed (3+ days)

---

## RANKED ISSUE LIST (BY ROI)

| Rank | Issue | Impact | Effort | ROI | Category |
|------|-------|--------|--------|-----|----------|
| 1 | Fix G7.04 typo | 2 | Trivial | 🟢 99 | Quick Win |
| 2 | Fix G6.04 dep text | 2 | Trivial | 🟢 99 | Quick Win |
| 3 | Fix G4.01 dependencies | 6 | Low | 🟢 95 | Critical |
| 4 | Fix G3.01 aggregation | 8 | Low | 🟢 95 | Critical |
| 5 | Fix G5.02 scatter plots | 10 | Low | 🟢 95 | Critical |
| 6 | Clarify G2.01 unplugged | 3 | Trivial | 🟢 90 | Quick Win |
| 7 | Add G4.02a median concept | 9 | Medium | 🟡 85 | Critical |
| 8 | Add block specs (G3.03/04) | 7 | Low | 🟡 85 | Critical |
| 9 | Add G3.0X table creation | 10 | Medium | 🟡 80 | Critical |
| 10 | Fix G4.02 inconsistency | 8 | Medium | 🟡 75 | Critical |
| 11 | Add G4.0X filtering | 9 | Medium | 🟡 75 | Critical |
| 12 | Add G4.0Y sorting | 7 | Low | 🟡 80 | Important |
| 13 | Add G5.0X GROUP BY | 8 | Medium | 🟡 70 | Important |
| 14 | Add G6.0Z CSV export | 7 | Medium | 🟡 65 | Important |
| 15 | Add G7.0Y Google Sheets | 7 | Medium | 🟡 65 | Important |
| 16 | Add G6.0X VLOOKUP | 6 | Medium | 🟡 60 | Important |
| 17 | Add G6.0Y pivot tables | 8 | Medium | 🟡 70 | Important |
| 18 | Add G7.0X moving avg | 6 | Medium | 🟡 60 | Important |
| 19 | Add G7.0Z chart auto | 7 | Medium | 🟡 65 | Important |
| 20 | Clarify dashboard (G5.01) | 5 | Low | 🟡 70 | Quality |
| 21 | Specify comparison (G6.02) | 4 | Low | 🟡 65 | Quality |
| 22 | Differentiate trends | 5 | Medium | 🟢 55 | Quality |
| 23 | Simplify G8.01 | 4 | Low | 🟢 65 | Quality |
| 24 | Add database skills | 6 | High | 🔴 40 | Future |
| 25 | Add display options | 3 | Low | 🟢 60 | Nice to Have |

**ROI Legend**: 🟢 High ROI (>80) | 🟡 Medium ROI (50-80) | 🔴 Low ROI (<50)

---

## IMPLEMENTATION WAVES

### WAVE 1: Quick Wins + Critical Blockers (Week 1)
**Goal**: Unblock students, fix broken skills
**Time**: 2-3 days

✅ **Text Fixes** (4 hours)
1. Fix G7.04 typo
2. Fix G6.04 dependency text
3. Clarify G2.01 unplugged
4. Fix G4.01 dependencies

✅ **Skill Rewrites** (1 day)
5. Fix G3.01 aggregation approach
6. Fix G5.02 scatter plots
7. Add block specificity (G3.03, G3.04, G5.01)

✅ **Critical New Skill** (1 day)
8. Add G3.0X table creation

**Deliverable**: 8 fixes, students can complete G3-G5

---

### WAVE 2: Foundation Skills (Week 2)
**Goal**: Complete scaffolding, add missing prerequisites
**Time**: 3-4 days

✅ **Concept vs Code** (1 day)
1. Add G4.02a median/mode concept
2. Reconcile G4.02 inconsistency (add G4.05 percentage)

✅ **Essential Operations** (2 days)
3. Add G4.0X filtering (move from G6.01)
4. Add G4.0Y sorting
5. Update dependencies for affected skills

**Deliverable**: 5 new/fixed skills, complete G3-G5 scaffolding

---

### WAVE 3: Advanced Capabilities (Week 3-4)
**Goal**: Add professional-level analysis skills
**Time**: 5-7 days

✅ **Data Manipulation** (2 days)
1. Add G5.0X GROUP BY aggregation
2. Add G6.0X VLOOKUP operations
3. Add G6.0Y pivot tables

✅ **Data Exchange** (2 days)
4. Add G6.0Z CSV export/import
5. Add G7.0Y Google Sheets integration

✅ **Advanced Analysis** (2 days)
6. Add G7.0X moving averages
7. Add G7.0Z chart automation

**Deliverable**: 7 new skills, 44-50% platform coverage

---

### WAVE 4: Quality & Polish (Week 4+)
**Goal**: Improve clarity and completeness
**Time**: 3-4 days

✅ **Specification Enhancement** (1 day)
1. Clarify dashboard implementation (G5.01, G7.01)
2. Specify comparison methods (G6.02)
3. Simplify statistical test (G8.01)

✅ **Skill Differentiation** (1 day)
4. Differentiate trend analysis (G4.01 vs G6.03)
5. Add chart type progression

✅ **Documentation** (1 day)
6. Update all dependency lists
7. Synchronize skills_T27 and allskills.md
8. Create implementation examples

**Deliverable**: Polished, production-ready skill set

---

## RESOURCE ALLOCATION

### Staffing Needs

**Content Designer** (20-24 hours)
- Write 10 new skill descriptions
- Rewrite 8 existing skills
- Fix dependencies and text issues

**Platform Expert** (8-12 hours)
- Validate block references
- Create implementation examples
- Test skill sequences

**Curriculum Reviewer** (8-10 hours)
- Review progression logic
- Validate age-appropriateness
- Check CSTA alignment

**Total Effort**: 36-46 hours (roughly 1 week for small team)

---

## RISK ASSESSMENT

### HIGH RISK if NOT Fixed
🔴 **Missing table creation (G3.0X)**
- Impact: 70%+ of G3+ skills cannot be completed
- Probability: 100% (guaranteed failure)
- Mitigation: MUST add before any G3+ implementation

🔴 **Scatter plot reference (G5.02)**
- Impact: Skill impossible to implement
- Probability: 100% (platform limitation)
- Mitigation: MUST rewrite immediately

🔴 **Loop-based aggregation (G3.01)**
- Impact: Students learn inefficient/wrong approach
- Probability: 100% (pedagogical error)
- Mitigation: MUST rewrite to use built-in blocks

### MEDIUM RISK if NOT Fixed
🟡 **Missing filtering prerequisite (G4)**
- Impact: G5 dashboard skill difficult
- Probability: 80% (workaround possible but awkward)
- Mitigation: Should move from G6 to G4

🟡 **Vague block references (multiple skills)**
- Impact: Teacher confusion, implementation variance
- Probability: 60% (teachers can figure out but takes time)
- Mitigation: Should add specific block names

### LOW RISK if NOT Fixed
🟢 **Missing advanced skills (GROUP BY, pivot, etc.)**
- Impact: Reduced capability, but core skills work
- Probability: 40% (students notice gap in advanced grades)
- Mitigation: Can add in future versions

---

## SUCCESS METRICS

### Phase 1 Completion Criteria

**Must Have** (Required for launch):
- ✅ All CRITICAL issues fixed (12 total)
- ✅ Table creation skill added (G3.0X)
- ✅ Aggregation approach fixed (G3.01)
- ✅ Scatter plot issue resolved (G5.02)
- ✅ Filtering moved to G4
- ✅ Median/mode scaffolding complete (G4.02a/b)

**Should Have** (Strongly recommended):
- ✅ All MEDIUM issues addressed (8 total)
- ✅ Essential operations added (sorting, GROUP BY)
- ✅ Dependencies validated and corrected
- ✅ Block specificity added

**Nice to Have** (Quality improvements):
- ✅ Advanced skills added (pivot, VLOOKUP, CSV, Sheets)
- ✅ All LOW issues polished (5 total)
- ✅ Complete platform coverage (44-50%)

### Validation Tests

1. **Skill Implementability**: Can teacher create working example for each skill?
2. **Progression Smoothness**: Can student complete each grade without knowledge gaps?
3. **Platform Alignment**: Does every skill use actual CreatiCode blocks?
4. **Dependency Integrity**: Do all T27→T27 dependencies follow correct order?
5. **Coverage Completeness**: Are major block categories represented?

**Target**: 100% pass rate on tests 1-4, >80% pass on test 5

---

## DECISION FRAMEWORK

### When to Add New Skill
**YES if**:
- ✅ Fills critical gap (prerequisite missing)
- ✅ Major platform capability unused
- ✅ CSTA standard not covered
- ✅ Essential real-world workflow

**NO if**:
- ❌ Minor variation of existing skill
- ❌ Platform doesn't support well
- ❌ Too advanced for grade level
- ❌ Belongs in different topic (T25/T26)

### When to Rewrite Existing Skill
**YES if**:
- ✅ Platform mismatch (teaches wrong thing)
- ✅ Blocker for other skills
- ✅ Violates scaffolding principles
- ✅ Confusing to teachers

**NO if**:
- ❌ Minor wording improvement only
- ❌ Low priority enhancement
- ❌ Risk breaking other dependencies
- ❌ Core concept correct (just polish needed)

### When to Delete Skill
**Phase 1 Rule**: NEVER delete (only add/improve)
**Phase 2+**: Only if duplicative AND low value

---

## TRACKING DASHBOARD

### Issues by Status

| Status | Critical | Important | Quality | Total |
|--------|----------|-----------|---------|-------|
| 🔴 Not Started | 12 | 8 | 5 | 25 |
| 🟡 In Progress | 0 | 0 | 0 | 0 |
| 🟢 Complete | 0 | 0 | 0 | 0 |

### Skills by Status

| Grade | Current | Target | Added | Status |
|-------|---------|--------|-------|--------|
| K | 3 | 3 | 0 | ✅ Complete |
| 1 | 3 | 3 | 0 | ✅ Complete |
| 2 | 4 | 4 | 0 | ⚠️ 1 minor fix |
| 3 | 4 | 5 | +1 | 🔴 Needs work |
| 4 | 4 | 7 | +3 | 🔴 Needs work |
| 5 | 4 | 5 | +1 | 🔴 Needs work |
| 6 | 4 | 7 | +3 | 🔴 Needs work |
| 7 | 4 | 7 | +3 | ⚠️ Needs additions |
| 8 | 4 | 4 | 0 | ⚠️ 2 fixes |
| **Total** | **28** | **38** | **+10** | **62% ready** |

### Platform Coverage

| Category | Blocks | Used Now | Used After | Coverage |
|----------|--------|----------|------------|----------|
| Widgets | 4 | 2 | 4 | 50% → 100% |
| Tables | 30+ | 8 | 20 | 27% → 67% |
| Database | 13 | 0 | 2 | 0% → 15% |
| Cloud | 14 | 0 | 2 | 0% → 14% |
| Operators | 1 | 0 | 1 | 0% → 100% |
| **Total** | **62+** | **10** | **29** | **16% → 47%** |

---

## NEXT ACTIONS

### This Week
1. ⏳ Stakeholder review of this analysis
2. ⏳ Prioritize critical vs important fixes
3. ⏳ Assign resources (content, platform, review)
4. ⏳ Start Wave 1 implementation

### Next Week
5. ⏳ Complete Wave 1 (quick wins + blockers)
6. ⏳ Begin Wave 2 (foundation skills)
7. ⏳ Validate with sample implementations
8. ⏳ Update documentation

### Weeks 3-4
9. ⏳ Complete Wave 2 and Wave 3
10. ⏳ Quality review and testing
11. ⏳ Synchronize all files
12. ⏳ Prepare for Phase 2 (cross-topic)

---

**Status**: READY FOR DECISION-MAKING
**Owner**: Awaiting stakeholder prioritization
**Next Update**: After Wave 1 completion
