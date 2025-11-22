# T36 Phase 1 Optimization Analysis
**Topic:** Careers, Collaboration & Future Paths
**Domain:** Computing & Society (D5)
**Analysis Date:** 2025-11-22
**Scope:** Internal T36 issues only (cross-topic dependencies preserved)

---

## HIGH PRIORITY ISSUES

### H1: Grade 4 Dependencies All Point to K Skills (Poor Scaffolding)
**Issue Type:** Dependency & Scaffolding Problem
**Affected Skills:** T36.G4.01, T36.G4.02, T36.G4.03
**Problem:**
All three Grade 4 skills have identical dependencies pointing ONLY to kindergarten skills:
- T36.GK.02 (Take turns kindly)
- T36.GK.03 (How does this tool help?)
- T36.G1.01 (List jobs that rely on computers)

This creates a 3-year gap with no intermediate scaffolding through Grades 2-3. Grade 4 students exploring careers should build on Grade 3 collaboration skills (empathy interviews, team charters, reflection) not just kindergarten turn-taking.

**Recommended Fix:**
- T36.G4.01 (Career snapshot) should depend on T36.G1.01 (jobs use tech) + T36.G3.01 (empathy interviews) - connecting career exploration to user research
- T36.G4.02 (Shared checklist) should depend on T36.G3.02 (team charter) - evolving from charter to tracking
- T36.G4.03 (Resolving disagreements) should depend on T36.G2.03 (recognizing strengths) + T36.G1.03 (listening) - building on collaboration foundations

---

### H2: Grade 5 Illogical Dependencies Mix Coding & Kindergarten Skills
**Issue Type:** Dependency Logic Problem
**Affected Skills:** T36.G5.01, T36.G5.02, T36.G5.03
**Problem:**
Grade 5 skills have inconsistent dependency patterns:
- T36.G5.01 depends on coding skills (T06.G3.01, T09.G3.01) + kindergarten sharing (T36.GK.02, T36.GK.03) - Why would mapping interests to careers require variables and green-flag scripts but skip all Grade 1-4 career exploration?
- T36.G5.02 depends on T01.G3.01, T07.G3.01 + kindergarten skills - iteration cycles should build on G4 project tracking, not coding blocks
- T36.G5.03 depends on G1 jobs/pros-cons + kindergarten - evaluating inclusion should build on G4 career profiles

The kindergarten dependencies (GK.02, GK.03) are too foundational for Grade 5 social/career skills. The coding dependencies (T06, T07, T09) are irrelevant to career exploration.

**Recommended Fix:**
- T36.G5.01 should depend on T36.G4.01 (career profiles provide foundation for interest mapping)
- T36.G5.02 should depend on T36.G4.02 (evolving from checklists to feedback cycles)
- T36.G5.03 should depend on T36.G4.01 (analyzing inclusion builds on career exposure) + T36.G1.02 (pros/cons thinking)
- Remove coding block dependencies (T06, T07, T09, T01) - they're not prerequisites for collaboration/career skills
- Remove kindergarten dependencies - they're too distant

---

### H3: Grades 6-8 Over-Rely on Kindergarten Skills
**Issue Type:** Dependency & Scaffolding Problem
**Affected Skills:** T36.G6.01, G6.02, G6.03, G6.04, G7.01, G7.02, G7.03, G7.04, G8.01, G8.02, G8.03, G8.04
**Problem:**
Nearly EVERY middle school skill (Grades 6-8) includes T36.GK.02 and/or T36.GK.03 as dependencies. These are kindergarten skills about sharing devices and describing tool purposes - far too basic for 6th-8th graders analyzing career equity, running agile rituals, or building roadmaps.

Examples:
- T36.G6.01 (Career equity analysis across computing clusters) depends on kindergarten "describe what a tool helps someone do"
- T36.G7.01 (Interview AI ethics practitioners) depends on kindergarten turn-taking
- T36.G8.03 (AI's differential impact on work) depends on kindergarten device sharing

This violates the X-2 rule (should only depend on grades X, X-1, X-2) and suggests poor scaffolding design.

**Recommended Fix:**
Replace kindergarten dependencies with Grade 3-5 career/collaboration skills:
- For career analysis skills (G6.01, G6.03, G7.01, G8.01, G8.02, G8.03): Use T36.G4.01 (career profiles) and/or T36.G5.01 (interest mapping) as foundations
- For collaboration/teamwork skills (G6.02, G6.04, G7.02, G7.03, G7.04, G8.04): Use T36.G3.02 (team charter), T36.G3.03 (reflection), T36.G4.02 (tracking), T36.G4.03 (compromise)
- Preserve T36.G1.01 and T36.G1.02 where relevant (these are foundational but not as distant as kindergarten)

---

### H4: Grade 6-8 Skills Depend on Irrelevant Coding/Pattern Skills
**Issue Type:** Dependency Logic Problem
**Affected Skills:** T36.G6.01, G6.02, G7.02, G8.01, G8.02, G8.03
**Problem:**
Several middle school career/collaboration skills depend on unrelated coding prerequisites:
- T36.G6.01, G8.01, G8.03 depend on T04.G2.01 (Identify repeating unit in pattern) - pattern recognition is not a prerequisite for career equity analysis or roadmap planning
- T36.G6.02, G7.02, G8.02 depend on T08.G3.01 (simple if) and T09.G3.01 (numeric variable) - running agile check-ins or creating org charts doesn't require conditionals or variables

These dependencies appear to be artificial attempts to tie social skills to coding, but they don't make logical sense.

**Recommended Fix:**
Remove pattern/coding dependencies (T04.G2.01, T08.G3.01, T09.G3.01, T06.G3.01) unless there's a clear pedagogical rationale. Career analysis, teamwork, and professional skills should scaffold from earlier career/collaboration work, not from unrelated coding mechanics.

Keep T06.G3.01 or T09.G3.01 ONLY if the skill explicitly involves building a CreatiCode project (e.g., T36.G5.02 plan-build-feedback could reasonably require basic scripting).

---

## MEDIUM PRIORITY ISSUES

### M1: Grade 3 Circular Dependency Chain
**Issue Type:** Dependency Logic Problem
**Affected Skills:** T36.G3.01, T36.G3.02, T36.G3.03
**Problem:**
Grade 3 skills form a sequential chain:
- T36.G3.01 (empathy interviews) → feeds into →
- T36.G3.02 (team charter) depends on G3.01 → feeds into →
- T36.G3.03 (reflection) depends on G3.02

While this progression is logical (interview → charter → reflect), it means all three skills must be taught in strict sequence with no flexibility. This is overly rigid for same-grade dependencies.

**Recommended Fix:**
Consider whether G3.02 and G3.03 truly REQUIRE their predecessors or if they could stand alone:
- T36.G3.02 (team charter) could be done independently of empathy interviews - teams can create charters without user research
- T36.G3.03 (reflection) could follow ANY group activity, not just charter creation

**Suggested Change:**
- Keep G3.01 independent (or depend only on G2.01 project roles)
- G3.02 depends on G2.01 (roles) or G2.03 (recognizing strengths) - not G3.01
- G3.03 depends on G2.01 or any Grade 2 collaboration skill - reflection doesn't require charter work

---

### M2: T36.G3.01 Depends on Coding Blocks (Questionable Logic)
**Issue Type:** Dependency Logic Problem
**Affected Skills:** T36.G3.01
**Problem:**
T36.G3.01 (Conduct empathy interviews) depends on:
- T06.G3.01 (Build green-flag script with 3-5 blocks)
- T07.G3.01 (Use a counted repeat loop)

Why would interviewing classmates about app needs require knowing loops? The description says "interview classmates/family and summarize insights" - this is a research/communication skill, not a coding skill. The dependency seems forced.

**Recommended Fix:**
Remove T06.G3.01 and T07.G3.01 dependencies. Empathy interviews should depend on prior collaboration/communication skills:
- T36.G2.01 (project roles) - understanding roles helps frame interview questions
- T36.G1.03 (listening behaviors) - essential for interviews
- Possibly T01.G2.01 or T03 sequencing skills if organizing interview data

---

### M3: T36.G7.04 Depends on T01 Sequencing (Weak Connection)
**Issue Type:** Dependency Logic Problem
**Affected Skills:** T36.G7.04
**Problem:**
T36.G7.04 (Mentor younger coders) depends on:
- T01.G3.01 (Complete a simple script with missing blocks)
- T01.G3.02 (Match story to code sequence)

These are Grade 3 T01 sequencing/storytelling skills. While mentoring might involve teaching sequencing, the dependency is 4 years old (G3→G7) and feels weak. Mentoring should build on Grade 6-7 collaboration and leadership skills.

**Recommended Fix:**
Replace T01 dependencies with T36 collaboration skills:
- T36.G5.02 (plan-build-feedback cycle) - mentors need to understand iterative teaching
- T36.G6.02 (agile rituals) or T36.G4.02 (tracking) - managing a workshop requires organization
- T36.G4.03 (compromise) or T36.G3.03 (reflection) - adjusting based on feedback

The current T01 dependencies suggest mentoring is about teaching sequencing, but the description says "debugging, AI safety" - broader topics requiring mature collaboration skills.

---

### M4: Inconsistent Terminology for Similar Skills Across Grades
**Issue Type:** Clarity & Consistency
**Affected Skills:** T36.G3.02, G6.04
**Problem:**
- T36.G3.02: "Draft simple team agreements" (short name: "Project team charter")
- T36.G6.04: "Add ethics clauses to team charters" (short name: "Responsible-use agreements")

Both involve "team charters" but G6.04 doesn't depend on G3.02. Students are amending charters in Grade 6 without having created basic charters in Grade 3? The progression is unclear.

**Recommended Fix:**
Make the relationship explicit:
- T36.G6.04 should depend on T36.G3.02 (or a Grade 4-5 evolution of charter work)
- Consider adding a Grade 5 skill bridging basic charters (G3) to ethics-enhanced charters (G6)
- Alternatively, clarify that G6.04 is creating NEW charters with ethics focus, not amending old ones

---

### M5: T36.GK.01 Has No Dependencies (Outlier)
**Issue Type:** Consistency
**Affected Skills:** T36.GK.01
**Problem:**
T36.GK.01 is the ONLY kindergarten skill in T36 with zero dependencies. All other K-G2 skills depend on at least one T01 or T03 sequencing/decomposition skill. This is inconsistent.

While "match community helpers to tools" is indeed foundational, every other T36 skill assumes some prior sequencing/organizing ability from T01.

**Recommended Fix:**
Add a minimal dependency:
- T01.GK.01 (Put pictures in order for bedtime) - shows ability to sequence/organize, relevant for organizing worker-tool matches
- OR leave as-is but document why this is an exception (truly foundational social awareness)

---

## LOW PRIORITY ISSUES

### L1: T36.G2.01 Depends on T01.G1.10 (If/Then) - Weak Relevance
**Issue Type:** Dependency Logic
**Affected Skills:** T36.G2.01
**Problem:**
T36.G2.01 (Identify project roles) depends on T01.G1.10 (Match pictures to if/then rules). The connection is unclear - identifying roles (planner, builder, tester) doesn't inherently require conditional thinking.

**Recommended Fix:**
Replace with T03.G1.03 (List steps for classroom routine) - role identification is closer to decomposing tasks than conditional logic. OR depend on T36.G1.03 (listening behaviors) since teamwork requires listening.

---

### L2: T36.G2.02 Has Overlapping Dependencies
**Issue Type:** Dependency Redundancy
**Affected Skills:** T36.G2.02
**Problem:**
T36.G2.02 (Plan balanced routines) depends on:
- T01.G1.01 (Put pictures in order to plant seed)
- T03.G1.03 (List steps for classroom routine)

Both are Grade 1 sequencing skills - redundant. Sequencing a routine (T03.G1.03) already implies ability to order steps (T01.G1.01).

**Recommended Fix:**
Keep T03.G1.03 only (more directly relevant to routines). Drop T01.G1.01 to reduce clutter.

---

### L3: Grade 8 Skills All Depend on T04.G2.01 (Pattern Recognition) - Weak Relevance
**Issue Type:** Dependency Logic
**Affected Skills:** T36.G8.01, G8.03
**Problem:**
Building career roadmaps (G8.01) and analyzing AI's impact on work (G8.03) both depend on T04.G2.01 (Identify repeating unit in a pattern). The rationale is unclear - career planning isn't about finding repeating units.

If the intent is to recognize patterns in career progression or societal trends, it's too abstract and not explicitly stated in skill descriptions.

**Recommended Fix:**
Remove T04.G2.01 unless there's clear documentation of why pattern recognition is essential. Career/futures skills should build on prior career exploration (T36.G4.01, G5.01, G6.01) and analysis skills (T36.G1.02 pros/cons, G5.03 inclusion analysis).

---

### L4: T36.G6.01 and G8.03 Are Potentially Too Broad/Complex
**Issue Type:** Skill Scope & Complexity
**Affected Skills:** T36.G6.01, T36.G8.03
**Problem:**
- **T36.G6.01** (Grade 6): "Analyze career equity across computing clusters (software, hardware, data, AI)" requires researching skill/tool needs, demographics, salary equity, accessibility barriers, geographic distribution, AND connecting T21-T24 AI skills to careers. This is 5+ distinct research tasks in one skill.

- **T36.G8.03** (Grade 8): "Analyze AI's differential impact on future work and equity" requires researching displacement vs augmentation, impacts by education/income/geography, policy recommendations, AND connecting T21-T24 experiences. Again, 4+ distinct analytical tasks.

Both skills might overwhelm students with too many research dimensions at once.

**Recommended Fix:**
**Option A (Preferred):** Break into smaller skills:
- G6.01a: Research computing career clusters (software, hardware, data, AI) and required skills/tools
- G6.01b: Analyze representation and equity in computing careers
- G8.03a: Research AI's impact on different job types (displacement vs augmentation)
- G8.03b: Analyze equity dimensions of AI in the workplace

**Option B:** Simplify expectations - require analysis of 2-3 dimensions (not all) and scaffold more gradually.

---

### L5: Missing Explicit Skill for "Version Control Collaboration"
**Issue Type:** Potential Gap
**Affected Skills:** None (gap)
**Problem:**
T36 covers team charters, check-ins, retros, org charts, and mentoring, but never explicitly addresses collaborative coding practices like:
- Using shared workspaces (CreatiCode projects)
- Merging work from multiple contributors
- Resolving conflicts when two students edit the same sprite/script
- Commenting code for teammates

These are practical collaboration skills relevant to CreatiCode environments.

**Recommended Fix:**
Consider adding a Grade 4-5 skill:
- **T36.G4.04:** "Collaborate on shared CreatiCode projects" - students practice dividing work across sprites, using comments to communicate, and combining contributions
- OR expand T36.G4.02 (shared checklist) to include division of coding work

This might overlap with T32 (project management in CreatiCode Studio), so check cross-topic alignment before adding.

---

### L6: No Explicit "Digital Citizenship in Teams" Skill
**Issue Type:** Potential Gap
**Affected Skills:** None (gap)
**Problem:**
T36 covers general collaboration (listening, compromise, inclusion) but doesn't explicitly address online collaboration etiquette:
- Respectful communication in shared workspaces/comments
- Handling asynchronous collaboration (not everyone online at once)
- Digital communication tone (text can seem rude without tone of voice)

These are increasingly relevant as CreatiCode projects may involve remote or asynchronous teamwork.

**Recommended Fix:**
Consider adding a Grade 5-6 skill:
- **T36.G5.04:** "Practice respectful digital communication" - students write comments, give feedback, or collaborate asynchronously, reflecting on tone and clarity
- OR expand T36.G4.03 (resolving disagreements) to include digital communication challenges

Check if this overlaps with T24 (XO policies) or T32 (community norms) before adding.

---

## POSITIVE OBSERVATIONS

1. **Clear K-2 Picture-Based Design:** Skills like T36.GK.01 (match helpers to tools), T36.G1.02 (sort helps vs problems), T36.G2.01 (match roles to tasks) appropriately use matching/sorting formats for young learners.

2. **Good Grade 3+ Block Coding Integration (when logical):** T36.G5.02 (plan-build-feedback cycle) correctly ties collaboration to CreatiCode project iteration.

3. **Strong Career Progression:** K (helpers use tech) → G1 (jobs need computers) → G4 (career profiles) → G5 (interests to pathways) → G6 (career clusters + equity) → G7 (interview practitioners) → G8 (roadmaps + resumes) shows logical scaffolding in the career exploration strand.

4. **Good Collaboration Progression:** G1 (listening) → G2 (roles, strengths) → G3 (interviews, charters, reflection) → G4 (tracking, compromise) → G5 (feedback cycles) → G6 (agile rituals, ethics clauses) → G7 (inclusion, mentoring) → G8 (retrospectives) is well-structured.

5. **AI Ethics Integration:** G6.01 (AI career pathways), G7.01 (AI ethics interviews), G8.03 (AI's impact on work) appropriately connect T21-T24 AI skills to career/societal context.

---

## SUMMARY OF RECOMMENDED ACTIONS

### High Priority (Must Fix):
1. **Fix Grade 4 dependencies:** Replace kindergarten-only dependencies with Grade 2-3 scaffolding (H1)
2. **Fix Grade 5 dependencies:** Remove illogical coding dependencies, replace kindergarten skills with Grade 4 career/collaboration skills (H2)
3. **Fix Grades 6-8 kindergarten over-reliance:** Replace GK.02/GK.03 dependencies with Grade 3-5 skills per X-2 rule (H3)
4. **Remove irrelevant coding/pattern dependencies:** Strip out T04.G2.01, T06.G3.01, T07.G3.01, T08.G3.01, T09.G3.01 from career/collaboration skills unless logically justified (H4)

### Medium Priority (Should Fix):
5. **Loosen Grade 3 chain:** Allow G3.02 and G3.03 to be more independent (M1)
6. **Remove coding from empathy interviews:** T36.G3.01 shouldn't require loops (M2)
7. **Update mentoring dependencies:** T36.G7.04 should build on collaboration, not old sequencing skills (M3)
8. **Clarify charter progression:** Connect G3.02 and G6.04 explicitly (M4)
9. **Standardize kindergarten dependencies:** Add dependency to T36.GK.01 or document exception (M5)

### Low Priority (Nice to Have):
10. **Refine minor dependency choices:** Clean up T36.G2.01, G2.02, G8.01, G8.03 dependencies (L1, L2, L3)
11. **Consider breaking up complex skills:** Split G6.01 and G8.03 if they're too broad (L4)
12. **Evaluate gaps:** Consider adding collaborative coding (L5) and digital citizenship (L6) skills

---

## CONCLUSION

T36 has strong conceptual progression in both career exploration and collaboration strands, but **dependency design is problematic**. The over-reliance on kindergarten skills in Grades 4-8 violates scaffolding principles, and the insertion of irrelevant coding/pattern dependencies (T04, T06, T07, T08, T09) weakens logical coherence.

**Primary fixes:** Rebuild Grade 4-8 dependencies to respect the X-2 rule, connect career skills to prior career skills (not kindergarten sharing), and remove coding prerequisites that don't support the learning goals.

Once dependencies are corrected, T36 will provide a clear, age-appropriate path through collaboration and career readiness aligned with CSTA standards.
