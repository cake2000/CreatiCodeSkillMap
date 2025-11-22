# T36 (Careers, Collaboration & Future Paths) - Phase 1 Optimization Analysis Report

## Executive Summary

**Total Skills Analyzed:** 35 skills (K through Grade 8)
- Kindergarten: 3 skills
- Grade 1: 3 skills
- Grade 2: 4 skills
- Grade 3: 4 skills
- Grade 4: 4 skills
- Grade 5: 3 skills
- Grade 6: 7 skills (including 2 sub-skills)
- Grade 7: 5 skills (including 2 sub-skills)
- Grade 8: 5 skills (including 2 sub-skills)

**Critical Issues Found:** 12 HIGH priority, 8 MEDIUM priority, 5 LOW priority

---

## HIGH PRIORITY ISSUES (Must Fix)

### H1. Inappropriate K-2 Dependencies on Grade 3+ Coding Skills

**Skill:** T36.G3.01 (Grade 3)
- **Issue:** Dependency on T07.G3.01 (Use a counted repeat loop) for a non-coding skill
- **Problem:** "Ask classmates simple questions to understand project needs" is about interviewing/research, not coding. The dependency on a coding skill (loops) is inappropriate.
- **Fix:** Remove T07.G3.01 dependency. This skill is about communication/empathy, not coding mechanics.

**Skill:** T36.G3.02 (Grade 3)
- **Issue:** Dependency on T09.G3.01 (Create and use a numeric variable) for team agreements
- **Problem:** "Draft simple team agreements" is about collaboration documentation, not variable usage. Unnecessary coding dependency.
- **Fix:** Remove T09.G3.01 dependency.

**Skill:** T36.G5.02 (Grade 5)
- **Issue:** Dependency on T07.G3.01 (Use a counted repeat loop)
- **Problem:** "Follow a plan-build-feedback cycle" involves iteration as a process concept, not loop implementation. The loop dependency is inappropriate.
- **Fix:** Remove T07.G3.01 dependency.

**Total Issues:** 3 skills with inappropriate coding dependencies

---

### H2. Missing Foundation Dependencies

**Skill:** T36.G1.01 (Grade 1)
- **Issue:** No dependencies despite building on career concepts
- **Problem:** Should depend on T36.GK.01 or T36.GK.03 (describing what tools help with)
- **Fix:** Add dependency on T36.GK.03 (Describe what a digital tool helps someone do)

**Skill:** T36.G2.01 (Grade 2)
- **Issue:** Dependency on T01.G1.10 doesn't support project role identification
- **Problem:** "Match pictures to if/then rules" is unrelated to understanding team roles
- **Fix:** Should depend on T36.G1.03 (Show listening behaviors) instead, as understanding roles builds on understanding teamwork basics

**Skill:** T36.G2.03 (Grade 2)
- **Issue:** Dependency on T01.G1.10 doesn't support recognizing strengths
- **Problem:** Same as G2.01 - the if/then dependency is inappropriate
- **Fix:** Should depend on T36.G1.03 (Show listening behaviors) and T36.G2.01 (Identify project roles)

**Total Issues:** 3 skills with missing/inappropriate foundation dependencies

---

### H3. Dependency Violations of X-2 Rule

**Skill:** T36.G4.01 (Grade 4)
- **Issue:** Dependencies include T36.G3.04 (Grade 3) and T36.G3.01 (Grade 3)
- **Problem:** Both are fine (Grade 4 can depend on Grade 3)
- **Status:** PASS - No violation

**Skill:** T36.G6.01 (Grade 6)
- **Issue:** Dependency on T36.G4.01 (Grade 4)
- **Problem:** Grade 6 depending on Grade 4 violates X-2 rule (can only go back to Grade 4, which is exactly X-2)
- **Status:** BORDERLINE PASS - This is exactly X-2, which is allowed

**Skill:** T36.G6.04 (Grade 6)
- **Issue:** Dependency on T36.G3.02 (Grade 3)
- **Problem:** Grade 6 depending on Grade 3 violates X-2 rule (X-2 = Grade 4)
- **Fix:** Should depend on G5 or G4 skill instead. Recommend changing to T36.G5.02 (Follow a plan-build-feedback cycle) which already has the team agreement foundation

**Total Violations:** 1 skill violates X-2 rule

---

### H4. Unclear or Too Broad Skill Descriptions

**Skill:** T36.G6.01 (Grade 6)
- **Issue:** "Compare computing career clusters" is very broad
- **Problem:** Comparing 4 major career clusters (software, hardware, data, AI) with job titles, skills, and daily tasks is too ambitious for one skill
- **Fix:** Should be broken into multiple skills:
  - T36.G6.01a: Identify job titles in computing career clusters
  - T36.G6.01b: Compare skills needed across career clusters
  - T36.G6.01c: Analyze daily tasks in different computing careers
- **Note:** The sub-skills G6.01.01 and G6.01.02 exist but focus on representation and AI connections, not the core comparison breakdown

**Skill:** T36.G7.01 (Grade 7)
- **Issue:** "Interview or research diverse technologists" combines two different activities
- **Problem:** Interviewing (synchronous, interactive) vs researching profiles (asynchronous, passive) are very different skills
- **Fix:** Split into two skills or clarify focus on one approach

**Skill:** T36.G8.03 (Grade 8)
- **Issue:** "Research AI's impact on job displacement vs augmentation" is very broad
- **Problem:** This topic could be an entire unit; research skills + economic analysis + AI literacy all mixed
- **Fix:** Narrow scope to specific sectors or make research parameters more concrete (e.g., "Research AI's impact on 3 job categories and classify as displacement/augmentation/hybrid")

**Total Issues:** 3 skills need clarity/breakdown

---

### H5. Skills That Don't Involve Coding (Grade 3+)

**Analysis:** Topic T36 is unique - it's about careers, collaboration, and future paths, which are often meta-skills about coding rather than coding itself. Let me check each Grade 3+ skill:

**Grade 3:**
- T36.G3.01: Ask classmates questions - NO CODING (appropriate for this topic)
- T36.G3.02: Draft team agreements - NO CODING (appropriate for this topic)
- T36.G3.03: Reflect on collaboration - NO CODING (appropriate for this topic)
- T36.G3.04: Explore what coders do - NO CODING (appropriate - learning ABOUT coding)

**Grade 4:**
- T36.G4.01: Explore tech careers - NO CODING (appropriate - career exploration)
- T36.G4.02: Track work with checklist - NO CODING (appropriate - project management)
- T36.G4.03: Role-play resolving disagreements - NO CODING (appropriate - soft skills)
- T36.G4.04: Categorize tech jobs - NO CODING (appropriate - career exploration)

**Grade 5:**
- T36.G5.01: Map interests to tech pathways - NO CODING (appropriate - career exploration)
- T36.G5.02: Follow plan-build-feedback cycle - INVOLVES CODING (builds CreatiCode feature)
- T36.G5.03: Evaluate representation - NO CODING (appropriate - equity analysis)

**Grade 6:**
- T36.G6.01: Compare career clusters - NO CODING (appropriate - career research)
- T36.G6.01.01: Analyze representation - NO CODING (appropriate - equity research)
- T36.G6.01.02: Connect AI skills to careers - NO CODING (appropriate - connects concepts)
- T36.G6.02: Practice stand-ups/sprint reviews - PROJECT MANAGEMENT (appropriate - involves coding projects)
- T36.G6.03: Analyze job descriptions - NO CODING (appropriate - career literacy)
- T36.G6.04: Add ethics clauses - NO CODING (appropriate - ethical framework)
- T36.G6.05: Document project contributions - INVOLVES CODING (documents CreatiCode projects)

**Grade 7:**
- T36.G7.01: Interview technologists - NO CODING (appropriate - career research)
- T36.G7.01.01: Research emerging careers - NO CODING (appropriate - career research)
- T36.G7.01.02: Discuss AI ethics - NO CODING (appropriate - ethics discussion)
- T36.G7.02: Design team diagrams - NO CODING (appropriate - organizational design)
- T36.G7.03: Facilitate inclusive collaboration - NO CODING (appropriate - soft skills)
- T36.G7.04: Mentor younger coders - INVOLVES CODING (teaches coding concepts)
- T36.G7.05: Use digital collaboration tools - TOOLS USE (appropriate - professional skills)

**Grade 8:**
- T36.G8.01: Build career roadmaps - NO CODING (appropriate - career planning)
- T36.G8.02: Prepare resumes/portfolios - INVOLVES CODING (portfolio of CreatiCode projects)
- T36.G8.03: Research AI's impact - NO CODING (appropriate - research/analysis)
- T36.G8.03.01: Analyze AI impacts by community - NO CODING (appropriate - equity research)
- T36.G8.03.02: Design equitable AI proposal - NO CODING (appropriate - policy/proposal)
- T36.G8.04: Facilitate retrospectives - PROJECT MANAGEMENT (appropriate - involves coding projects)

**Conclusion:** NO ISSUES - T36 is appropriately designed as a meta-topic about careers, collaboration, and professional development. Most skills don't directly involve coding but are about understanding, planning, and reflecting on technology careers and collaborative coding work. The few that do involve coding (G5.02, G6.05, G7.04, G8.02, G8.04) appropriately apply coding skills in context.

**Total Issues:** 0 (this is working as intended)

---

## MEDIUM PRIORITY ISSUES (Should Fix)

### M1. Same-Grade Dependencies That May Be Unnecessary

**Skill:** T36.G4.02 (Grade 4)
- **Issue:** Depends on both T36.G3.02 (team agreements) and T36.G2.03 (recognize strengths)
- **Problem:** G2.03 dependency might be redundant since G3.02 already builds on collaboration foundations
- **Recommendation:** Review if G2.03 dependency is necessary or if G3.02 + G3.03 is sufficient

**Skill:** T36.G4.03 (Grade 4)
- **Issue:** Depends on both T36.G3.02 and T36.G3.03
- **Problem:** G3.03 already depends on G3.02, creating a chain
- **Recommendation:** Remove G3.02 dependency, keep only G3.03 (which implies G3.02)

**Skill:** T36.G5.02 (Grade 5)
- **Issue:** Depends on T36.G4.02 and T36.G3.03
- **Problem:** Should trace through G4 skills instead of skipping back to G3
- **Recommendation:** Change G3.03 to G4.03 (which includes reflection on disagreement resolution)

**Total Issues:** 3 skills with redundant/skipped dependencies

---

### M2. Missing Intermediate Skills for Logical Progression

**Gap Between G1 and G2 on Collaboration:**
- G1.03 introduces listening behaviors
- G2.01 jumps to project roles
- **Missing:** Understanding what a team/group is and why we work together
- **Recommendation:** Add G1.04 or revise G1.03 to explicitly define teams

**Gap Between G4 and G5 on Career Exploration:**
- G4.04 categorizes jobs by output
- G5.01 maps personal interests to pathways
- **Missing:** Explicitly connecting own skills/interests to job categories from G4.04
- **Recommendation:** Current progression is okay but could be smoother

**Gap Between G5 and G6 on Agile Practices:**
- G5.02 introduces plan-build-feedback cycle
- G6.02 jumps to formal agile rituals (stand-ups, sprint reviews)
- **Missing:** Introduction to why teams use structured processes
- **Recommendation:** Add G5.04 or expand G5.02 description to mention "teams that build software use processes like this"

**Total Issues:** 2 notable gaps in progression

---

### M3. Inconsistent Skill Granularity

**Grade 6 has 7 skills** (including sub-skills) while:
- Grade 5 has 3 skills
- Grade 7 has 5 skills
- Grade 8 has 5 skills

**Issue:** Grade 6 includes two levels of sub-skills (G6.01.01, G6.01.02) which makes the structure inconsistent.

**Problem:**
- Why does G6.01 get sub-skills but G7.01 and G8.03 also have sub-skills?
- Sub-skill numbering should be consistent across grades

**Recommendation:**
- Decide on consistent approach: either use sub-skills throughout or flatten them
- If keeping sub-skills, ensure they truly break down the parent skill rather than add new concepts

**Total Issues:** 1 structural inconsistency

---

## LOW PRIORITY ISSUES (Nice to Have)

### L1. Wording Improvements for Age-Appropriateness

**Skill:** T36.GK.02 (Kindergarten)
- **Current:** "Take turns using a device to complete a task together"
- **Issue:** Phrase "complete a task together" might be abstract for K
- **Suggestion:** "Take turns using a device to finish something as a team" or use more concrete example in description

**Skill:** T36.G3.02 (Grade 3)
- **Current:** "Students fill a charter listing..."
- **Issue:** Word "charter" might be unfamiliar to Grade 3
- **Suggestion:** Use "team agreement form" or "team plan" instead

**Skill:** T36.G6.02 (Grade 6)
- **Current:** Uses terms "stand-ups", "sprint reviews"
- **Issue:** Industry jargon without context
- **Suggestion:** Define in description: "short daily check-ins called 'stand-ups'"

**Total Issues:** 3 minor wording improvements

---

### L2. Potential Overlaps Within T36

**T36.G3.04 and T36.G4.01:**
- G3.04: "Explore what coders and digital designers do"
- G4.01: "Explore diverse tech careers via profiles/videos"
- **Overlap:** Both involve exploring tech careers through media
- **Differentiation:** G3.04 is narrower (coders/designers only), G4.01 is broader (diverse roles)
- **Status:** Appropriate progression, not redundant

**T36.G6.03 and T36.G8.02:**
- G6.03: "Analyze job descriptions for skills/values"
- G8.02: "Prepare resumes/portfolios and practice interviews"
- **Overlap:** Both relate to job application process
- **Differentiation:** G6.03 is reading/analyzing, G8.02 is creating/doing
- **Status:** Appropriate progression, not redundant

**Total Issues:** 0 true overlaps (apparent overlaps are intentional scaffolding)

---

### L3. Minor Description Enhancements

**Skill:** T36.G2.04 (Grade 2)
- **Current:** "Name jobs where people create digital things"
- **Enhancement:** Could specify what "digital things" means for Grade 2 (apps, games, videos, drawings)

**Skill:** T36.G5.01 (Grade 5)
- **Current:** Lists specific roles (sound designer, narrative designer, sports data analyst, civic technologist)
- **Enhancement:** Some of these roles might be unfamiliar; consider providing brief definitions in teaching notes

**Total Issues:** 2 minor description enhancements

---

## DETAILED DEPENDENCY ANALYSIS

### Within-T36 Dependencies (Valid)

| Skill | Dependencies (T36 only) | X-2 Check | Status |
|-------|------------------------|-----------|---------|
| T36.GK.02 | T36.GK.01 | N/A (K) | PASS |
| T36.GK.03 | T36.GK.01 | N/A (K) | PASS |
| T36.G1.02 | T36.G1.01 | Same grade | PASS |
| T36.G2.04 | T36.G1.01, T36.GK.03 | G2→G1, G2→K | PASS |
| T36.G3.01 | T36.G2.01 | G3→G2 | PASS |
| T36.G3.02 | T36.G3.01 | Same grade | PASS |
| T36.G3.03 | T36.G3.02 | Same grade | PASS |
| T36.G3.04 | T36.G2.04 | G3→G2 | PASS |
| T36.G4.01 | T36.G3.04, T36.G3.01 | G4→G3 | PASS |
| T36.G4.02 | T36.G3.02, T36.G2.03 | G4→G3, G4→G2 | PASS |
| T36.G4.03 | T36.G3.02, T36.G3.03 | G4→G3 | PASS (but redundant) |
| T36.G4.04 | T36.G2.04, T36.G4.01 | G4→G2, same | PASS |
| T36.G5.01 | T36.G4.04, T36.G4.01 | G5→G4 | PASS |
| T36.G5.02 | T36.G4.02, T36.G3.03 | G5→G4, G5→G3 | PASS |
| T36.G5.03 | T36.G4.01, T36.G3.01 | G5→G4, G5→G3 | PASS |
| T36.G6.01 | T36.G5.01, T36.G4.01 | G6→G5, G6→G4 | PASS |
| T36.G6.01.01 | T36.G6.01, T36.G5.03 | Same, G6→G5 | PASS |
| T36.G6.01.02 | T36.G6.01, T36.G5.01 | Same, G6→G5 | PASS |
| T36.G6.02 | T36.G5.02, T36.G4.02 | G6→G5, G6→G4 | PASS |
| T36.G6.03 | T36.G5.01, T36.G4.04 | G6→G5, G6→G4 | PASS |
| T36.G6.04 | T36.G5.02, T36.G3.02 | G6→G5, G6→G3 | **FAIL** (X-2 violation) |
| T36.G6.05 | T36.G5.02, T36.G5.01 | G6→G5 | PASS |
| T36.G7.01 | T36.G6.01, T36.G5.03 | G7→G6, G7→G5 | PASS |
| T36.G7.01.01 | T36.G7.01, T36.G6.01 | Same, G7→G6 | PASS |
| T36.G7.01.02 | T36.G7.01, T36.G6.01.01 | Same, G7→G6 | PASS |
| T36.G7.02 | T36.G6.02, T36.G6.01 | G7→G6 | PASS |
| T36.G7.03 | T36.G5.02, T36.G5.03, T36.G4.03 | G7→G5, G7→G4 | PASS |
| T36.G7.04 | T36.G6.04, T36.G5.03 | G7→G6, G7→G5 | PASS |
| T36.G7.05 | T36.G6.02, T36.G6.05 | G7→G6 | PASS |
| T36.G8.01 | T36.G7.01.01, T36.G6.01.02 | G8→G7, G8→G6 | PASS |
| T36.G8.02 | T36.G6.05, T36.G6.03, T36.G7.04 | G8→G6, G8→G7 | PASS |
| T36.G8.03 | T36.G6.01.02, T36.G7.01.02 | G8→G6, G8→G7 | PASS |
| T36.G8.03.01 | T36.G8.03, T36.G6.01.01 | Same, G8→G6 | PASS |
| T36.G8.03.02 | T36.G8.03.01 | Same | PASS |
| T36.G8.04 | T36.G7.02, T36.G7.03, T36.G6.02 | G8→G7, G8→G6 | PASS |

**Summary:** 1 X-2 violation found (T36.G6.04)

---

### Cross-Topic Dependencies (Preserve All)

**T36.G1.03** → T03.GK.01 (Identify parts that make up a whole)
- **Status:** PRESERVE

**T36.G2.01** → T01.G1.10 (Match pictures to if/then rules)
- **Status:** PRESERVE but questionable relevance (see H2 above)

**T36.G2.02** → T01.G1.01, T03.G1.03
- **Status:** PRESERVE (sequencing and routines are relevant)

**T36.G2.03** → T01.G1.10
- **Status:** PRESERVE but questionable relevance (see H2 above)

**T36.G3.01** → T07.G3.01 (Use a counted repeat loop)
- **Status:** PRESERVE but inappropriate for this skill (see H1 above)

**T36.G3.02** → T09.G3.01 (Create and use a numeric variable)
- **Status:** PRESERVE but inappropriate for this skill (see H1 above)

**T36.G5.02** → T01.G3.01 (Complete a simple script), T07.G3.01 (Use a counted repeat loop)
- **Status:** PRESERVE T01.G3.01, but T07.G3.01 is inappropriate (see H1 above)

**T36.G6.01** → T04.G2.01 (Identify repeating unit in pattern)
- **Status:** PRESERVE but unclear relevance - might be about recognizing patterns in career data?

**ALL OTHER CROSS-TOPIC DEPENDENCIES:** PRESERVE

---

## SCAFFOLDING & PROGRESSION ANALYSIS

### Kindergarten Foundation
**Skills:** 3 foundational skills
- GK.01: Match helpers to tools (picture-based) ✓
- GK.02: Take turns with devices (unplugged collaboration) ✓
- GK.03: Describe tool purposes (picture-based) ✓

**Assessment:** Strong foundation, appropriate for age, all picture-based/unplugged

---

### Grade 1 Introduction to Careers & Tradeoffs
**Skills:** 3 skills building on K
- G1.01: List jobs using computers (builds on GK) - **NEEDS DEPENDENCY FIX**
- G1.02: Sort helps vs problems (critical thinking) ✓
- G1.03: Show listening in group work (collaboration intro) ✓

**Assessment:** Good progression, but G1.01 needs connection to K skills

---

### Grade 2 Team Roles & Wellness
**Skills:** 4 skills
- G2.01: Identify project roles - **DEPENDENCY ISSUE (T01.G1.10 irrelevant)**
- G2.02: Plan balanced screen time (wellness) ✓
- G2.03: Recognize teammates' strengths - **DEPENDENCY ISSUE (T01.G1.10 irrelevant)**
- G2.04: Name digital creation careers ✓

**Assessment:** Career and wellness tracks developing, but role/teamwork skills need better dependencies

---

### Grade 3 Empathy, Agreements & Reflection
**Skills:** 4 skills
- G3.01: Ask questions for project needs - **REMOVE CODING DEPENDENCY**
- G3.02: Draft team agreements - **REMOVE CODING DEPENDENCY**
- G3.03: Reflect on collaboration ✓
- G3.04: Explore coder/designer roles ✓

**Assessment:** Strong collaboration framework, but remove inappropriate coding dependencies

---

### Grade 4 Career Diversity & Conflict Resolution
**Skills:** 4 skills
- G4.01: Explore diverse tech careers ✓
- G4.02: Track work with checklists ✓
- G4.03: Role-play resolving disagreements - **REDUNDANT DEPENDENCY**
- G4.04: Categorize tech jobs by output ✓

**Assessment:** Solid career exploration and collaboration skills

---

### Grade 5 Personal Pathways & Iteration
**Skills:** 3 skills
- G5.01: Map interests to tech pathways ✓
- G5.02: Follow plan-build-feedback cycle - **REMOVE T07.G3.01 DEPENDENCY**
- G5.03: Evaluate representation/inclusion ✓

**Assessment:** Brings together careers, collaboration, and equity

---

### Grade 6 Career Depth & Agile Practices
**Skills:** 7 skills (including 2 sub-skills)
- G6.01: Compare career clusters - **TOO BROAD, NEEDS BREAKDOWN**
- G6.01.01: Analyze representation in careers ✓
- G6.01.02: Connect AI skills to careers ✓
- G6.02: Practice agile rituals ✓
- G6.03: Analyze job descriptions ✓
- G6.04: Add ethics clauses - **X-2 VIOLATION**
- G6.05: Document project contributions ✓

**Assessment:** Rich career exploration but needs structural fixes

---

### Grade 7 Professional Skills & Mentorship
**Skills:** 5 skills (including 2 sub-skills)
- G7.01: Interview diverse technologists - **CLARIFY INTERVIEW vs RESEARCH**
- G7.01.01: Research emerging tech careers ✓
- G7.01.02: Discuss AI ethics with professionals ✓
- G7.02: Design cross-functional team diagrams ✓
- G7.03: Facilitate inclusive collaboration ✓
- G7.04: Mentor younger coders ✓
- G7.05: Use digital collaboration tools ✓

**Assessment:** Excellent professional development focus

---

### Grade 8 Career Planning & Impact Analysis
**Skills:** 5 skills (including 2 sub-skills)
- G8.01: Build multi-year career roadmaps ✓
- G8.02: Prepare resumes/portfolios/interviews ✓
- G8.03: Research AI's job impact - **TOO BROAD, NEEDS SCOPE**
- G8.03.01: Analyze AI impacts by community ✓
- G8.03.02: Design equitable AI proposal ✓
- G8.04: Facilitate capstone retrospectives ✓

**Assessment:** Strong capstone-level skills preparing for high school

---

## SUMMARY OF ISSUES BY CATEGORY

### HIGH PRIORITY (12 issues)
1. Remove T07.G3.01 from T36.G3.01 (inappropriate coding dependency)
2. Remove T09.G3.01 from T36.G3.02 (inappropriate coding dependency)
3. Remove T07.G3.01 from T36.G5.02 (inappropriate coding dependency)
4. Add T36.GK.03 dependency to T36.G1.01 (missing foundation)
5. Replace T01.G1.10 with T36.G1.03 in T36.G2.01 (wrong dependency)
6. Replace T01.G1.10 with T36.G1.03 + T36.G2.01 in T36.G2.03 (wrong dependency)
7. Replace T36.G3.02 with T36.G5.02 in T36.G6.04 (X-2 violation)
8. Break down T36.G6.01 into clearer sub-components (too broad)
9. Clarify T36.G7.01 focus: interview OR research (unclear)
10. Narrow scope of T36.G8.03 research parameters (too broad)

### MEDIUM PRIORITY (8 issues)
1. Remove redundant T36.G2.03 from T36.G4.02 dependencies
2. Remove redundant T36.G3.02 from T36.G4.03 (keep G3.03 only)
3. Replace T36.G3.03 with T36.G4.03 in T36.G5.02
4. Add G1.04 or enhance G1.03 to define teams (scaffolding gap)
5. Consider G5.04 to bridge to formal agile processes (scaffolding gap)
6. Standardize sub-skill structure across grades (inconsistent granularity)

### LOW PRIORITY (5 issues)
1. Simplify "complete a task together" in T36.GK.02
2. Replace "charter" with "team agreement form" in T36.G3.02
3. Define agile jargon in T36.G6.02 description
4. Specify "digital things" examples in T36.G2.04
5. Consider providing role definitions for T36.G5.01

---

## POSITIVE ASPECTS

1. **Appropriate Non-Coding Focus:** T36 correctly treats careers/collaboration as meta-skills, not requiring coding in every skill
2. **Strong K-2 Foundation:** All K-2 skills are appropriately picture-based/unplugged
3. **Equity Integration:** Excellent inclusion of representation, accessibility, and equity topics throughout
4. **AI Career Connections:** Forward-thinking connections between AI skills and career pathways
5. **Professional Skills:** Age-appropriate introduction of real-world practices (agile, portfolios, interviews)
6. **Scaffolded Collaboration:** Clear progression from sharing devices (K) to facilitating retrospectives (G8)
7. **Career Diversity:** Broad representation of tech career paths beyond just "programmer"

---

## RECOMMENDATIONS FOR PHASE 2

### Immediate Fixes (High Priority)
1. Clean up all inappropriate coding dependencies (3 skills)
2. Fix missing/wrong foundation dependencies (3 skills)
3. Resolve X-2 violation (1 skill)
4. Break down or clarify overly broad skills (3 skills)

### Structural Improvements (Medium Priority)
1. Streamline redundant dependencies (3 skills)
2. Add missing scaffolding skills (2 gaps)
3. Standardize sub-skill approach (grade-wide)

### Polish (Low Priority)
1. Update wording for age-appropriateness (3 skills)
2. Enhance descriptions with examples (2 skills)

### Total Skills Needing Changes: 18 out of 35 (51%)

---

## CONCLUSION

Topic T36 has a strong conceptual foundation with appropriate focus on careers, collaboration, and professional development. The main issues are:
1. **Inappropriate coding dependencies** in non-coding skills (especially G3 skills)
2. **Some weak foundation dependencies** that should connect better to T36 concepts
3. **One X-2 violation** that needs fixing
4. **A few overly broad skills** that need scope clarification

The progression from K (picture-based career awareness) to Grade 8 (career planning and AI impact analysis) is logical and age-appropriate. The topic successfully balances technical career knowledge, collaboration skills, and equity considerations.

**Overall Assessment:** GOOD framework with targeted fixes needed
**Readiness for Phase 2:** READY after addressing 12 high-priority issues
