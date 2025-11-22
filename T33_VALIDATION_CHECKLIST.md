# T33 Validation Checklist

Use this checklist to verify T33 optimization is complete and correct.

## Pre-Implementation Verification

### Current State Analysis ✓
- [x] Extracted all 27 T33 skills from allskills.md
- [x] Extracted all 15 Cloud blocks from blockdes8.txt
- [x] Identified 2 missing cloud session blocks (Variables category)
- [x] Analyzed all dependencies for X-2 compliance
- [x] Identified all quality issues (H, M, L priority)
- [x] Created renumbering map
- [x] Created new skill definition for cloud sessions

## Implementation Checklist

### Phase 1: Critical Fixes

#### Fix 1: Renumber Grade 6 Skills
- [ ] Rename T33.G6.04.01 to T33.G6.05
  - [ ] Update skill ID in header
  - [ ] Verify description unchanged
  - [ ] Verify block reference unchanged (p2p_clearsheet)
- [ ] Rename T33.G6.05 to T33.G6.06
  - [ ] Update skill ID in header
  - [ ] Verify description unchanged
  - [ ] Update dependency from T33.G6.02 (unchanged)
- [ ] Rename T33.G6.06 to T33.G6.07
  - [ ] Update skill ID in header
  - [ ] Verify description unchanged
  - [ ] Update dependency reference: T33.G6.05 → T33.G6.06

#### Fix 2: Renumber Grade 7 Skills
- [ ] Rename T33.G7.02.01 to T33.G7.03
  - [ ] Update skill ID in header
  - [ ] Verify description unchanged
  - [ ] Verify block reference unchanged (p2p_appendrow)
- [ ] Rename T33.G7.03 to T33.G7.04
  - [ ] Update skill ID in header
  - [ ] Verify description unchanged
  - [ ] Verify block reference unchanged (p2p_getgooglefoldercontent)
  - [ ] Update dependency reference: T33.G6.05 → T33.G6.06
- [ ] Rename T33.G7.04 to T33.G7.06
  - [ ] Update skill ID in header
  - [ ] Verify description unchanged
  - [ ] Verify dependencies unchanged (T08.G5.01, T31.G5.01, T33.G6.03, T33.G6.04)
- [ ] Rename T33.G7.05 to T33.G7.07
  - [ ] Update skill ID in header
  - [ ] Verify description unchanged
  - [ ] Update dependency reference: T33.G6.06 → T33.G6.07
- [ ] Rename T33.G7.06 to T33.G7.08
  - [ ] Update skill ID in header
  - [ ] Verify description unchanged
  - [ ] Update dependency references: T33.G6.05 → T33.G6.06, T33.G6.06 → T33.G6.07
- [ ] Rename T33.G7.07 to T33.G7.09
  - [ ] Update skill ID in header
  - [ ] Verify description unchanged
  - [ ] Update dependency reference: T33.G6.05 → T33.G6.06

#### Fix 3: Add New Cloud Session Skill
- [ ] Insert new skill T33.G7.05 after T33.G7.04 (formerly T33.G7.03)
- [ ] Copy text from T33_COMPLETE_SKILLS_EXTRACT.md
- [ ] Verify skill components:
  - [ ] ID: T33.G7.05
  - [ ] Topic: T33 – Connected Services & Tool Wrappers
  - [ ] Skill: Create and join cloud sessions for real-time collaboration
  - [ ] Description includes all required elements
  - [ ] Block references: data_createcloudsession, data_joincloudsession
  - [ ] Dependencies: T08.G5.01, T09.G5.01, T31.G5.01, T33.G6.03, T33.G6.04

#### Fix 4: Update Grade 8 Dependencies
- [ ] Update T33.G8.02 dependency: T33.G7.06 → T33.G7.08
- [ ] Update T33.G8.03 dependency: T33.G7.06 → T33.G7.08
- [ ] Update T33.G8.04 dependency: T33.G7.06 → T33.G7.08
- [ ] Update T33.G8.05 dependency: T33.G7.06 → T33.G7.08
- [ ] Update T33.G8.06 dependency: T33.G7.05 → T33.G7.07

### Phase 2: Medium Priority Fixes

#### Improvement 1: Revise T33.G6.01
- [ ] Update skill title to: "Identify Cloud blocks and their internet dependencies"
- [ ] Update description to focus specifically on Cloud category blocks
- [ ] Suggested description:
  ```
  Students explore CreatiCode's Cloud category blocks and test each to identify
  which require internet connectivity. They create a reference chart showing which
  blocks need external services (Google Sheets blocks need Google account access,
  fetch URL needs internet, etc.). They test behavior when offline versus online
  and categorize blocks by their service dependencies. They understand that some
  blocks work with local data (tables) while others connect to external services.
  ```
- [ ] Verify dependencies unchanged

#### Improvement 2: Remove Redundant Clear Sheet Reference
- [ ] Locate T33.G7.01 description
- [ ] Remove mention of `clear sheet` block from the description
- [ ] Update description to focus only on: `list all sheets`, `add sheet`, `remove sheet`
- [ ] Keep block reference to p2p_clearsheet in T33.G6.05 only
- [ ] Verify T33.G7.01 still makes sense without clear sheet mention

#### Improvement 3: Add Block References to G8 Skills
- [ ] Update T33.G8.02 description to add: "Uses blocks learned in G6-G7 to analyze terms of service requirements"
- [ ] Update T33.G8.03 description to add: "Uses error handling patterns from T33.G6.06 to simulate failures"
- [ ] Update T33.G8.04 description to add: "Uses data validation techniques with blocks from G6-G7"
- [ ] Update T33.G8.05 description to add: "Compares Cloud blocks (G6-G7) with local alternatives"

#### Improvement 4: Reorder Security Skill (Optional)
- [ ] DECISION: Keep T33.G7.06 (security) where it is, OR move to after T33.G7.08
- [ ] If moving: Renumber T33.G7.07, T33.G7.08 up by one
- [ ] If moving: Place security as T33.G7.09 (last in G7)
- [ ] Update all affected dependencies

### Phase 3: Polish

#### Polish 1: Add Modern App Examples to K-2
- [ ] Update T33.GK.01 description with specific examples:
  - [ ] Add: "YouTube Kids, Google Maps, Alexa" as internet-dependent
  - [ ] Add: "Calculator, Camera, Offline Drawing App" as offline
- [ ] Update T33.G1.01 description with sorting examples:
  - [ ] Add: "YouTube needs internet, Clock works alone"
- [ ] Update T33.G2.01 description with loading examples:
  - [ ] Add: "spinning circle on YouTube while loading videos"

#### Polish 2: Standardize Terminology
- [ ] Search and replace: "service blocks" → "Cloud blocks" (if not in quote)
- [ ] Search and replace: "network connectivity" → "internet connectivity"
- [ ] Search and replace: "google sheet" → "Google Sheets" (when referring to service)
- [ ] Verify "google sheet" (lowercase) only used when referring to specific spreadsheet instance
- [ ] Create terminology note at top of T33 section

#### Polish 3: Add AI Cross-References
- [ ] Search for all mentions of "AI blocks" in T33
- [ ] Add note after each: "(See Topic T34 for AI-specific skills)"
- [ ] Or add general note at beginning of G6: "Note: AI blocks are covered in Topic T34"
- [ ] Affected skills: T33.G6.01, T33.G6.05, T33.G6.06, T33.G7.05 (multi-service), T33.G8.06 (pipeline)

## Post-Implementation Verification

### Skill Count Verification
- [ ] Total skills in T33: 28 (was 27)
  - [ ] K: 1 skill
  - [ ] G1: 1 skill
  - [ ] G2: 1 skill
  - [ ] G3: 1 skill
  - [ ] G4: 1 skill
  - [ ] G5: 1 skill
  - [ ] G6: 7 skills (was 6 + 1 with .01 suffix = 7, now all sequential)
  - [ ] G7: 9 skills (was 7 + 1 with .01 suffix = 8, now 9 with new cloud session)
  - [ ] G8: 6 skills

### ID Sequence Verification
- [ ] No gaps in K-5: GK.01, G1.01, G2.01, G3.01, G4.01, G5.01 ✓
- [ ] No gaps in G6: G6.01, G6.02, G6.03, G6.04, G6.05, G6.06, G6.07
- [ ] No .01 suffixes in G6: All sequential ✓
- [ ] No gaps in G7: G7.01, G7.02, G7.03, G7.04, G7.05, G7.06, G7.07, G7.08, G7.09
- [ ] No .01 suffixes in G7: All sequential ✓
- [ ] No gaps in G8: G8.01, G8.02, G8.03, G8.04, G8.05, G8.06
- [ ] TOTAL: 28 skills, all sequential within each grade ✓

### Block Coverage Verification
- [ ] All 15 Cloud category blocks covered:
  - [ ] p2p_fetchfromurl → T33.G6.02 ✓
  - [ ] p2p_removecolumnsfromsheet → T33.G8.01 ✓
  - [ ] p2p_removerowsfromsheet → T33.G8.01 ✓
  - [ ] p2p_insertcolumnsinsheet → T33.G8.01 ✓
  - [ ] p2p_insertrowsinsheet → T33.G8.01 ✓
  - [ ] p2p_clearsheet → T33.G6.05 ✓
  - [ ] p2p_readfromgooglesheet → T33.G6.03 ✓
  - [ ] p2p_writeintogooglesheet → T33.G6.04 ✓
  - [ ] p2p_listSheetsInGoogleSheet → T33.G7.01 ✓
  - [ ] p2p_addsheet → T33.G7.01 ✓
  - [ ] p2p_removesheet → T33.G7.01 ✓
  - [ ] p2p_appendrow → T33.G7.03 ✓
  - [ ] p2p_setvalue → T33.G7.02 ✓
  - [ ] p2p_getvalue → T33.G7.02 ✓
  - [ ] p2p_getgooglefoldercontent → T33.G7.04 ✓

- [ ] Both cloud session blocks covered:
  - [ ] data_createcloudsession → T33.G7.05 ✓
  - [ ] data_joincloudsession → T33.G7.05 ✓

- [ ] **TOTAL: 17/17 blocks = 100% coverage** ✓

### Dependency Verification

#### X-2 Rule Compliance
- [ ] All G6 skills depend only on G4-G6 skills (max 2 grade gap) ✓
- [ ] All G7 skills depend only on G5-G7 skills (max 2 grade gap) ✓
- [ ] All G8 skills depend only on G6-G8 skills (max 2 grade gap) ✓

#### No Forward References
- [ ] All dependencies point to earlier or same-grade skills ✓
- [ ] No skill depends on a skill that comes after it ✓

#### Cross-Topic Dependencies Valid
- [ ] All T08 dependencies exist in Topic T08 (Conditionals)
- [ ] All T09 dependencies exist in Topic T09 (Variables)
- [ ] All T10 dependencies exist in Topic T10 (Data Structures)
- [ ] All T31 dependencies exist in Topic T31 (Networks)

#### Within-Topic Dependencies Valid
- [ ] All T33.GX.YY dependencies exist in current skill list
- [ ] All dependency IDs match new numbering scheme
- [ ] No dependencies on old IDs (e.g., T33.G6.04.01, T33.G7.02.01)

### Grade Appropriateness Verification
- [ ] K-2 skills are picture-based, no coding ✓
- [ ] G3-5 skills are conceptual, exploring apps/services ✓
- [ ] G6+ skills use block coding ✓
- [ ] Block complexity increases by grade:
  - [ ] G6: Basic read/write operations ✓
  - [ ] G7: Advanced operations, multi-service workflows ✓
  - [ ] G8: Data pipelines, validation, professional practices ✓

### Description Quality Verification
- [ ] All skills have clear, actionable descriptions ✓
- [ ] All skills that teach specific blocks mention block names ✓
- [ ] All skills explain what students will build/create ✓
- [ ] All skills explain the learning objective ✓

### Progression Verification
- [ ] Each grade builds on previous grade's knowledge ✓
- [ ] No skill teaches the same content as another ✓
- [ ] Skills within a grade have logical sequence ✓
- [ ] G8.06 capstone integrates earlier skills ✓

## Final Sign-Off

### Quality Metrics
- [ ] Block coverage: 100% (17/17) ✓
- [ ] ID consistency: 100% (no .01 suffixes) ✓
- [ ] Dependency compliance: 100% (X-2 rule) ✓
- [ ] Grade appropriateness: 100% ✓
- [ ] **Overall Grade: A-** ✓

### Documentation
- [ ] T33_ANALYSIS_REPORT.md created ✓
- [ ] T33_OPTIMIZATION_SUMMARY.md created ✓
- [ ] T33_COMPLETE_SKILLS_EXTRACT.md created ✓
- [ ] T33_VALIDATION_CHECKLIST.md created ✓

### Git Tracking
- [ ] Add T33_ANALYSIS_REPORT.md to git
- [ ] Add T33_OPTIMIZATION_SUMMARY.md to git
- [ ] Add T33_COMPLETE_SKILLS_EXTRACT.md to git
- [ ] Add T33_VALIDATION_CHECKLIST.md to git
- [ ] Update skillsv4/allskills.md with changes
- [ ] Create T33_changes_summary.md for git tracking

### Final Review
- [ ] All checklist items completed
- [ ] All files reviewed by human
- [ ] All changes tested (if applicable)
- [ ] Ready for integration into main skills file

---

## Notes and Issues Encountered

(Add any notes, issues, or deviations from the plan here)

---

## Completion Date
- [ ] Analysis completed: ________________
- [ ] Implementation completed: ________________
- [ ] Validation completed: ________________
- [ ] Sign-off: ________________
