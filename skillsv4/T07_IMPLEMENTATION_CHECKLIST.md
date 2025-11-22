# T07 (Loops) Implementation Checklist
**Analysis Date**: 2025-11-22
**Use this checklist to track implementation progress**

---

## PHASE 1: CRITICAL FIXES ⏰ Estimated: 3-4 hours

### ☐ Task H1: Add K-2 Foundation Skills (4 new skills)

#### ☐ H1.1: Create T07.K.01
- [ ] Write skill definition (see Action Plan for template)
- [ ] Add to allskills.md at beginning of T07 section
- [ ] Verify dependency on T04.K.01 exists
- [ ] Create sample assessment questions
- [ ] Update topic skill count: K (0→1)

#### ☐ H1.2: Create T07.G1.01
- [ ] Write skill definition (see Action Plan)
- [ ] Add to allskills.md after T07.K.01
- [ ] Verify dependencies: T07.K.01, T04.G1.01
- [ ] Create sample assessment questions
- [ ] Update topic skill count: G1 (0→1)

#### ☐ H1.3: Create T07.G1.02
- [ ] Write skill definition (see Action Plan)
- [ ] Add to allskills.md after T07.G1.01
- [ ] Verify dependency: T07.G1.01
- [ ] Create sample assessment questions
- [ ] Update topic skill count: G1 (1→2)

#### ☐ H1.4: Create T07.G2.01
- [ ] Write skill definition (see Action Plan)
- [ ] Add to allskills.md after T07.G1.02
- [ ] Verify dependencies: T07.G1.02, T04.G2.01
- [ ] Create sample assessment questions
- [ ] Update topic skill count: G2 (0→1)

#### ☐ H1.5: Update T07.G3.01 Dependencies
- [ ] Add T07.G2.01 to dependency list
- [ ] Keep existing T04.G1.01, T04.G2.01, T01.G2.05 dependencies
- [ ] Verify no circular dependencies created
- [ ] Update any cross-references in other topics

**Completion Criteria**: 4 new K-2 skills added, G3.01 updated, no dependency errors

---

### ☐ Task H2: Verify and Fix T07.G6.08 (break/continue blocks)

#### ☐ H2.1: Verify Block Names in CreatiCode
- [ ] Check if "break out of loop" block exists
- [ ] Check if "continue to next iteration" block exists
- [ ] Document exact block names found
- [ ] Screenshot blocks for reference

#### ☐ H2.2: Update Skill Description
**If blocks exist:**
- [ ] Update description with exact block names
- [ ] Verify examples use correct syntax
- [ ] Test that skill is implementable

**If blocks DON'T exist:**
- [ ] Rewrite skill to use flag variables + conditionals
- [ ] Use alternative description from Action Plan
- [ ] Add T09.G4.01 dependency (flag variables)
- [ ] Update examples to match new approach
- [ ] Rename skill if needed: "Exit loops early using flag variables"

**Completion Criteria**: T07.G6.08 verified implementable with CreatiCode blocks

---

### ☐ Task H3: Clarify T07.G6.05 and T07.G6.06 Distinction

#### ☐ H3.1: Update T07.G6.05 Description
- [ ] Replace description with version from Action Plan
- [ ] Emphasize trace table as GENERAL METHODOLOGY
- [ ] Note it works for any nested loop scenario
- [ ] Keep existing dependencies unchanged

#### ☐ H3.2: Update T07.G6.06 Description
- [ ] Replace description with version from Action Plan
- [ ] Emphasize VISUAL PATTERN APPLICATION
- [ ] Add note that trace table from G6.05 can be used
- [ ] Add T07.G6.05 to dependency list
- [ ] Verify new dependency doesn't create cycle

#### ☐ H3.3: Verify Progression
- [ ] Confirm G6.05 teaches technique
- [ ] Confirm G6.06 applies technique to visual context
- [ ] Check that dependency G6.06→G6.05 makes sense
- [ ] Update any cross-references in other topics

**Completion Criteria**: Clear distinction between methodology (G6.05) and application (G6.06), proper dependency flow

---

### ☐ Task H4: Rewrite T07.G8.02 for Specificity

#### ☐ H4.1: Update Description
- [ ] Replace vague description with specific version from Action Plan
- [ ] Include 3-component framework: (1) initial state, (2) update rule, (3) stopping condition
- [ ] Add concrete examples: GCD, primes, Fibonacci
- [ ] Make assessable: "identify when iteration is needed"
- [ ] Keep dependencies unchanged

#### ☐ H4.2: Verify Sub-Skills Align
- [ ] Review T07.G8.02.01 (GCD) - still fits parent?
- [ ] Review T07.G8.02.02 (primes) - still fits parent?
- [ ] Review T07.G8.02.03 (Fibonacci) - still fits parent?
- [ ] Update sub-skill descriptions if needed
- [ ] No dependency changes needed

#### ☐ H4.3: Create Sample Assessment
- [ ] Write 2-3 sample problems testing new description
- [ ] Verify problems assess "identify when iteration needed"
- [ ] Verify problems assess 3-component framework
- [ ] Test with target grade level

**Completion Criteria**: T07.G8.02 is specific, assessable, and sub-skills align

---

### ☐ Task H5: Add T07.G6.09 (For-Each Loops)

#### ☐ H5.1: Create Skill Definition
- [ ] Write skill definition (see Action Plan for template)
- [ ] Cover `for each item [var] in [list]` block
- [ ] Cover `for each index [var] in [list]` block
- [ ] Explain when to use vs manual indexing
- [ ] Add dependencies: T07.G5.02, T07.G6.03, T09.G4.01

#### ☐ H5.2: Insert Into Skill List
- [ ] Add after T07.G6.08 in allskills.md
- [ ] Update topic skill count: G6 (8→9)
- [ ] Renumber if using sequential numbering
- [ ] Verify placement between list skills and G7

#### ☐ H5.3: Verify Block Availability
- [ ] Confirm `for each item in` block exists in CreatiCode
- [ ] Confirm `for each index in` block exists in CreatiCode
- [ ] Document exact syntax
- [ ] Create example implementations

#### ☐ H5.4: Update Cross-References
- [ ] Check if any G7-G8 skills should reference G6.09
- [ ] Check if list-processing skills need updates
- [ ] Update documentation to mention for-each pattern

**Completion Criteria**: G6.09 added, blocks verified, proper placement in progression

---

## PHASE 1 COMPLETION CHECKLIST
- [ ] All 5 High Priority tasks completed (H1-H5)
- [ ] Total new skills added: 5 (4 K-2 + 1 G6)
- [ ] Total skills updated: 5 (G3.01, G6.05, G6.06, G6.08, G8.02)
- [ ] No broken dependencies
- [ ] All new skills have sample assessments
- [ ] Documentation updated
- [ ] Skill counts updated: K(1), G1(2), G2(1), G3(5), G4(8), G5(4), G6(9), G7(4), G8(7)
- [ ] Total T07 skills: 36→41

---

## PHASE 2: RECOMMENDED IMPROVEMENTS ⏰ Estimated: 2-3 hours

### ☐ Task M1: Clarify T07.G4.07 Description
- [ ] Add sentence explaining why G4.03 dependency helps
- [ ] Use enhanced description from Action Plan
- [ ] No dependency changes
- [ ] No structural changes

**Estimated Time**: 15 minutes

---

### ☐ Task M2: Update T07.G3.01 Dependencies (After H1)
- [ ] Verify H1 completed first
- [ ] Add T07.G2.01 to dependencies
- [ ] Keep T04.G1.01, T04.G2.01, T01.G2.05
- [ ] Verify no circular refs
- [ ] Test dependency graph

**Estimated Time**: 15 minutes

---

### ☐ Task M3: Document G4 Skill Sequencing
- [ ] Create instructor guide (see Action Plan for template)
- [ ] Show Tier 1 (parallel) vs Tier 2 (sequential) skills
- [ ] Explain G4.07 requires G4.03 + G4.06 first
- [ ] Add to teacher documentation
- [ ] No skill changes needed

**Estimated Time**: 30 minutes

---

### ☐ Task M4: Consider Adding G5 Skills (OPTIONAL)

#### ☐ M4.1: Decide on G5 Expansion
- [ ] Review current G5: only 4 skills
- [ ] Compare to G4 (8) and G6 (9)
- [ ] Decide if smoother progression needed
- [ ] Approve/reject expansion

**If approved:**

#### ☐ M4.2: Add T07.G5.05 (Input Loops)
- [ ] Write skill definition from Action Plan
- [ ] Verify T10.G4.01 dependency exists
- [ ] Create examples: sum until -1, build list from input
- [ ] Add to allskills.md after G5.04
- [ ] Update skill count: G5 (4→5)

#### ☐ M4.3: Add T07.G5.06 (List Modification)
- [ ] Write skill definition from Action Plan
- [ ] Create examples: double all values, add 10 to each
- [ ] Add to allskills.md after G5.05
- [ ] Update skill count: G5 (5→6)
- [ ] Bridge to G6.03 list searching

**Estimated Time**: 1 hour (if approved)

---

### ☐ Task M5: Split T07.G4.03 Into Two Skills (OPTIONAL)

#### ☐ M5.1: Decide on Split
- [ ] Review current G4.03: teaches 2 concepts
- [ ] Assess if granularity improvement worth effort
- [ ] Approve/reject split

**If approved:**

#### ☐ M5.2: Create T07.G4.03 (Manual Counter)
- [ ] Write new description focusing on manual counter pattern
- [ ] Keep existing dependencies
- [ ] Create examples: "Step 1, Step 2, Step 3"
- [ ] Replace in allskills.md

#### ☐ M5.3: Create T07.G4.03.01 (For-Loop Block)
- [ ] Write description focusing on for-loop block
- [ ] Add T07.G4.03 as dependency
- [ ] Create examples: count by 2s, count down
- [ ] Add after T07.G4.03 in allskills.md

#### ☐ M5.4: Update Downstream Dependencies
- [ ] Review T07.G4.07, G6.01, G6.02, G7.04
- [ ] Determine which need manual counter (G4.03)
- [ ] Determine which need for-loop (G4.03.01)
- [ ] Update dependencies accordingly

**Estimated Time**: 1-1.5 hours (if approved)

---

### ☐ Task M6: Enhance T07.G7.01 Description
- [ ] Add bridging context connecting to G6.07
- [ ] Explain time-step concept
- [ ] Add physics examples
- [ ] Use enhanced description from Action Plan
- [ ] No dependency changes

**Estimated Time**: 15 minutes

---

### ☐ Task M7: Add Loop Efficiency Skill (OPTIONAL)

#### ☐ M7.1: Decide on Efficiency Skill
- [ ] Review if optimization explicit teaching needed
- [ ] Check if G8.02.02 (primes) covers enough
- [ ] Approve/reject new skill

**If approved:**

#### ☐ M7.2: Create T07.G7.05
- [ ] Write skill definition from Action Plan
- [ ] Examples: √n for primes, break for early exit
- [ ] Add dependencies: G6.08, G7.03, G7.04
- [ ] Insert before current G7.05 or renumber
- [ ] Update skill count: G7 (4→5)

#### ☐ M7.3: Update T07.G8.02.02
- [ ] Consider adding G7.05 as dependency
- [ ] Reference optimization concept
- [ ] Verify alignment

**Estimated Time**: 45 minutes (if approved)

---

### ☐ Task M8: Verify Sub-Skill Dependencies (After H4)
- [ ] Verify H4 (G8.02 rewrite) completed first
- [ ] Review T07.G8.02.01 (GCD) alignment
- [ ] Review T07.G8.02.02 (primes) alignment
- [ ] Review T07.G8.02.03 (Fibonacci) alignment
- [ ] Consider adding T07.G7.04 as shared dependency
- [ ] Update dependencies if needed

**Estimated Time**: 30 minutes

---

## PHASE 2 COMPLETION CHECKLIST
- [ ] All required M tasks completed (M1, M2, M3, M6, M8)
- [ ] Optional M tasks decided (M4, M5, M7)
- [ ] If all optional approved: +5 more skills
- [ ] Documentation updated
- [ ] Instructor guides created
- [ ] No broken dependencies

---

## PHASE 3: OPTIONAL ENHANCEMENTS ⏰ Estimated: 1-2 hours

### ☐ Task O1: Add 3D Object Iteration Skill (OPTIONAL)

#### ☐ O1.1: Assess 3D Curriculum Importance
- [ ] Determine if 3D programming is major focus
- [ ] Check if `for each 3D object` block is heavily used
- [ ] Approve/reject skill

**If approved:**

#### ☐ O1.2: Create T07.G7.06
- [ ] Write skill definition from Action Plan
- [ ] Find 3D topic dependency
- [ ] Add dependency on G6.09 (for-each pattern)
- [ ] Create 3D examples
- [ ] Insert in G7 section

**Estimated Time**: 45 minutes (if approved)

---

### ☐ Task O2: Add Concurrent Loops Skill (OPTIONAL)

#### ☐ O2.1: Assess Parallel Execution Teaching
- [ ] Determine if concurrent loops are taught
- [ ] Check if multi-sprite games use this pattern
- [ ] Approve/reject skill

**If approved:**

#### ☐ O2.2: Create T07.G6.10
- [ ] Write skill definition from Action Plan
- [ ] Add dependencies: G4.01, T06 broadcast, T09 variables
- [ ] Create multi-sprite examples
- [ ] Insert in G6 section

**Estimated Time**: 45 minutes (if approved)

---

## PHASE 3 COMPLETION CHECKLIST
- [ ] Optional enhancements decided
- [ ] If approved: skills added and tested
- [ ] Documentation complete
- [ ] Final skill count determined

---

## FINAL VALIDATION ✅

### ☐ Dependency Graph Validation
- [ ] Run dependency checker on all T07 skills
- [ ] Verify no circular dependencies
- [ ] Verify all X-2 rule compliance (no G8→K deps)
- [ ] Check cross-topic dependencies still valid

### ☐ Skill Count Validation
- [ ] Count all K-2 skills: Expected 4
- [ ] Count all G3-8 skills: Expected 36+ (depending on optional)
- [ ] Verify total matches documentation
- [ ] Update topic overview with final counts

### ☐ Block Coverage Validation
- [ ] `repeat (N)` - covered ✓
- [ ] `forever` - covered ✓
- [ ] `repeat until` - covered ✓
- [ ] `for [var] from...to...step` - covered ✓
- [ ] `repeat N times at intervals` - covered ✓
- [ ] `for each item in [list]` - NOW covered (G6.09) ✓
- [ ] `for each index in [list]` - NOW covered (G6.09) ✓
- [ ] `break`/`continue` - verified or revised (G6.08) ✓

### ☐ Spec Compliance Validation
- [ ] K-2 picture-based skills: NOW 4 ✓
- [ ] G3+ block-based skills: YES ✓
- [ ] X-2 dependency rule: YES ✓
- [ ] IXL-style clear/assessable: NOW YES (G8.02 fixed) ✓
- [ ] CreatiCode block accuracy: NOW verified ✓
- [ ] No skill deletion: YES ✓
- [ ] Cross-topic deps preserved: YES ✓

**Target**: 7/7 spec requirements met = 100% compliance

### ☐ Documentation Validation
- [ ] All skill descriptions are clear
- [ ] All dependencies are documented
- [ ] Sample assessments created for new skills
- [ ] Instructor guides completed
- [ ] Cross-references updated

### ☐ Quality Assurance
- [ ] Each new skill has 2-3 sample problems
- [ ] Each updated skill tested for clarity
- [ ] Progression flows logically K→G8
- [ ] No gaps in critical concepts
- [ ] Competition readiness maintained

---

## FINAL SIGN-OFF

**Phase 1 Completed**: ☐ Date: ____________ By: ____________
- 5 critical fixes implemented
- K-2 foundation established
- For-each loops added
- Vague descriptions fixed
- Block verification complete

**Phase 2 Completed**: ☐ Date: ____________ By: ____________
- Recommended improvements implemented
- Optional expansions decided
- Documentation complete

**Phase 3 Completed**: ☐ Date: ____________ By: ____________
- Optional enhancements decided/implemented
- Final validation passed

**T07 Optimization 100% Complete**: ☐ Date: ____________ By: ____________

---

## METRICS SUMMARY

### Before Optimization:
- Total Skills: 36
- K-2 Skills: 0 ❌
- Spec Compliance: 5/7 (71%)
- Quality Rating: ⭐⭐⭐⭐ (4/5)

### After Phase 1:
- Total Skills: 41
- K-2 Skills: 4 ✅
- Spec Compliance: 7/7 (100%)
- Quality Rating: ⭐⭐⭐⭐⭐ (5/5)

### After All Phases (Max):
- Total Skills: 48-50
- K-2 Skills: 4 ✅
- G5 Skills: 6 (expanded)
- G7 Skills: 5-6 (efficiency + optional 3D)
- Spec Compliance: 7/7 (100%)
- Quality Rating: ⭐⭐⭐⭐⭐ (5/5)

---

## REFERENCES

- **T07_COMPREHENSIVE_ANALYSIS.md** - Detailed issue analysis
- **T07_ACTION_PLAN.md** - Implementation guide with skill definitions
- **T07_EXECUTIVE_SUMMARY.md** - High-level overview
- **T07_VISUAL_PROGRESSION.md** - Visual skill progression map
- **T07_IMPLEMENTATION_CHECKLIST.md** - This document

---

**Last Updated**: 2025-11-22
**Status**: Ready for implementation
