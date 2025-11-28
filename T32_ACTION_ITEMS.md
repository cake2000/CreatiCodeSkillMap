# T32 Digital Citizenship - Prioritized Action Items

## Phase 1: Quick Wins (1-2 weeks, ~20-30 hours)

### A. Consolidations (Reduce 135 → 122-125 skills)

#### 1. Consolidate Career Clusters (G6) [-3 skills]
**DELETE:**
- T32.G6.15: Identify hardware engineering careers
- T32.G6.16: Identify data science careers
- T32.G6.17: Identify AI and machine learning careers

**MODIFY:**
- T32.G6.14: Identify software development careers
  → **NEW:** Identify and compare computing career clusters (software, hardware, data, AI/ML)

**New Description:**
```
Students research four computing career clusters: software development, hardware
engineering, data science, and AI/ML. For each cluster, they identify 2-3 example
job titles, key skills needed, and typical tools used. Students create a comparison
chart showing similarities and differences across clusters.
```

---

#### 2. Consolidate AI Displacement (G8) [-2 skills]
**DELETE:**
- T32.G8.18: Identify jobs augmented by AI
- T32.G8.19: Compare AI displacement vs augmentation patterns

**MODIFY:**
- T32.G8.17: Identify jobs at risk of AI displacement
  → **NEW:** Analyze AI impacts on employment (displacement vs augmentation)

**New Description:**
```
Students research how AI affects different jobs, identifying at least 3 job categories
at risk of displacement and 3 where AI augments human workers. They create a comparison
chart showing patterns: which tasks are at risk, which skills remain valuable, and how
workers can prepare. Students examine how impacts vary across communities based on
education, income, and geography.
```

**Dependencies:** Add T32.G8.20 to dependencies

---

#### 3. Consolidate Ethics Lenses (G6) [-2 skills]
**DELETE:**
- T32.G6.05: Apply fairness lens
- T32.G6.06: Apply autonomy lens

**MODIFY:**
- T32.G6.04: Apply beneficence lens
  → **NEW:** Apply ethics lenses (beneficence, fairness, autonomy)

**New Description:**
```
Students learn three ethics lenses for evaluating technology:
(1) Beneficence: Does it help? Who benefits? Who might be harmed?
(2) Fairness: Can everyone use it equally? Are there accessibility barriers?
(3) Autonomy: Do users have control and informed choice?
Students apply each lens to CreatiCode projects using ChatGPT blocks to analyze
project purpose and document evaluations in a table variable.
```

**Update T32.G6.07 dependencies:** Change from G6.05-06 to just G6.04 (modified)

---

#### 4. Consolidate Workshops (G7-G8) [-2-3 skills]
**MERGE:**
- T32.G7.24 + T32.G7.25 → T32.G7.24 (Plan and deliver lesson to younger coders)
- T32.G8.04.01 + G8.04.02 + G8.04.03 → T32.G8.04 (Design and deliver workshop)

**T32.G7.24 New Description:**
```
Students plan a short lesson (10-15 minutes) to teach younger students a coding
concept or tech safety topic. After delivering the lesson, they reflect on what
went well, what was challenging, and what they would change next time.
```

**T32.G8.04 New Description:**
```
Students design a workshop on a responsible tech topic (screen balance, kindness,
privacy, AI ethics). They build interactive teaching tools using widgets and blocks,
pilot the workshop with younger grades, collect feedback using surveys, and iterate
based on results.
```

**Decision needed:** Keep or merge T32.G8.10 (Lead peer workshops)?

---

#### 5. Fix Vague Verb (1 skill)
**MODIFY:**
- T32.G3.05: Interview classmates to **understand** project needs
  → Interview classmates to **identify** project needs

---

### B. Grade Redistributions (Balance G6-G7)

#### Move from G6 to G5 [-1 from G6]
- T32.G6.14 (consolidated career clusters) → Move to G5 after consolidation
  - Rationale: Builds naturally on G5.09 (map interests to pathways)
  - New ID: T32.G5.14

#### Move from G6 to G8 [-2 from G6]
- T32.G6.24: Analyze job descriptions for technical skills → T32.G8.24
- T32.G6.25: Analyze job descriptions for soft skills → T32.G8.25
  - Rationale: These fit better with G8 resume/career prep (G8.15-16)

---

### C. Description Simplification (32 skills, prioritize top 10)

**Priority 1 (Longest):**
1. T32.G8.09 (1107 chars) → Reduce to ~350 chars
2. T32.G7.14 (1157 chars) → Reduce to ~400 chars
3. T32.G7.13 (977 chars) → Reduce to ~400 chars
4. T32.G8.10 (928 chars) → Reduce to ~350 chars
5. T32.G8.08 (862 chars) → Reduce to ~400 chars

**Priority 2:**
6. T32.G7.12 (874 chars)
7. T32.G6.09 (848 chars)
8. T32.G6.13 (784 chars)
9. T32.G4.05 (743 chars)
10. T32.G4.06 (678 chars)

**Guideline:** Reduce to 200-400 chars. Remove excessive parentheticals. Move implementation details to teacher guides.

---

**Phase 1 Results:**
- Skills: 135 → 122-125
- G6: 27 → 20
- G7: 27 → 22
- G8: 22 → 21
- Balanced distribution achieved ✅

---

## Phase 2: Add Modern Topics (2-3 weeks, ~30-40 hours)

### Critical Additions (Must add)

#### 1. Algorithmic Influence (G5)
```
ID: T32.G5.XX (assign next available number after redistributions)
Skill: Explain how algorithms shape online experiences
Description: Students research how algorithms determine what they see online
(search results, social media feeds, video recommendations, ads). They identify
3+ types of data algorithms use and explain how this creates personalized experiences.
Students discuss benefits (relevant content) and concerns (filter bubbles, manipulation).

Dependencies: T32.G3.02, T32.G4.03
```

---

#### 2. Filter Bubbles (G6)
```
ID: T32.G6.XX
Skill: Analyze filter bubbles and echo chambers
Description: Students investigate how recommendation algorithms can create filter
bubbles (limited exposure to diverse viewpoints). They conduct an experiment searching
for a controversial topic using different persona profiles and document how results
differ. Using widgets and table variables, they build a comparison tool showing how
different users see different information. Students propose strategies to break out
of filter bubbles.

Dependencies: T32.G3.02, T32.G5.08, T32.G5.XX (new algorithmic influence skill)
```

---

#### 3. AI Content Attribution (G7)
```
ID: T32.G7.XX
Skill: Analyze AI content attribution and copyright
Description: Students investigate copyright questions around AI-generated content:
Should AI art be copyrightable? Should training data sources be credited? When must
AI generation be disclosed? Students research legal cases and stakeholder perspectives,
conduct structured debates using a widget-based debate tool, and draft policy proposals
with specific recommendations.

Dependencies: T32.G7.06 (AI art gallery), T32.G5.08 (credibility evaluation)
```

**Note:** This may overlap with T32.G7.14. Consider merging or making this the focus of G7.14.

---

#### 4. Digital Footprint Management (G5)
```
ID: T32.G5.XX
Skill: Manage and minimize digital footprints
Description: Students learn strategies for managing their digital footprint: audit
(search for themselves online), minimize (privacy settings, limit sharing), curate
(build positive presence), and delete (right to be forgotten, data removal). Students
create a personal digital footprint management plan with specific actions and discuss
why footprint management is harder for some groups.

Dependencies: T32.G3.01, T32.G2.04
```

---

#### 5. AI-Generated Content Detection (G8)
```
ID: T32.G8.XX
Skill: Evaluate AI-generated content across media types
Description: Students learn to identify AI-generated content across formats: text
(ChatGPT essays, fake reviews), images (DALL-E), audio (voice clones), video (deepfakes).
They build a detection checklist tool using widgets with criteria for each media type,
test the tool on mixed human/AI content, and document detection accuracy and limitations.
Students discuss implications for trust, attribution, and authentication.

Dependencies: T32.G7.17 (deepfakes), T32.G6.03
```

---

### High Priority Additions (Strongly recommended)

#### 6. Algorithmic Transparency (G7)
```
ID: T32.G7.XX
Skill: Analyze algorithmic transparency and accountability
Description: Students compare transparent vs. opaque algorithms using case studies.
They evaluate when algorithms should explain decisions, who should challenge them,
and what happens when algorithms err. Students build a widget-based tool simulating
algorithmic decision-making with varying transparency levels, showing impact on trust
and fairness.

Dependencies: T32.G7.09 (transparency tradeoffs), T32.G6.11
```

---

#### 7. Expand Dark Patterns (G4)
**MODIFY existing T32.G4.04:**

**Current:** Compare persuasive vs informative design patterns

**New:** Identify dark patterns and manipulative design

**Expanded description:**
```
Students analyze persuasive design patterns in apps and websites, distinguishing
informative design from "dark patterns" (manipulative tactics). They identify examples:
fake urgency, hidden costs, hard-to-cancel subscriptions, misleading defaults, and
confirmshaming. Students create two versions of the same app (e.g., game invitation):
one using persuasive/dark patterns and one that's neutral. Using widget blocks, they
build both interfaces, have peers compare them, and document which tactics they notice.
```

---

### Medium Priority (Consider adding if time)

#### 8. Cyberbullying Bystander (G4)
```
ID: T32.G4.XX
Skill: Respond to cyberbullying as a bystander
Description: Students learn bystander strategies for responding to online meanness:
support the target, report to trusted adult, don't share mean content, counter with
kindness. Students role-play scenarios using CreatiCode chat simulation and practice
choosing helpful responses. They discuss why bystanders matter and barriers to intervention.

Dependencies: T32.G2.03 (online kindness)
```

---

#### 9. Respectful Disagreement (G6)
```
ID: T32.G6.XX
Skill: Practice respectful disagreement online
Description: Students learn techniques for disagreeing respectfully: assume good intent,
ask clarifying questions, focus on ideas not people, acknowledge valid points, know when
to disengage. Students build a discussion simulator using widgets where they practice
responding to controversial statements. They compare respectful vs. hostile responses
and analyze how tone affects outcomes.

Dependencies: T32.G3.03 (respectful communication)
```

---

#### 10. Compulsive Tech Use (G5)
```
ID: T32.G5.XX
Skill: Recognize compulsive technology use patterns
Description: Students learn warning signs of compulsive tech use: checking phone despite
no notification, feeling anxious without device, neglecting responsibilities, sleep loss.
They analyze fictional case studies and identify healthy vs. concerning patterns. Students
design a self-monitoring tool (daily tracker using widgets) to log tech use and feelings,
identifying personal triggers.

Dependencies: T32.G2.02 (balanced schedules), T32.G5.04 (well-being debates)
```

---

**Phase 2 Results:**
- Add 5 critical + 2 high priority = 7 new skills minimum
- Add 3 medium priority = 10 new skills maximum
- Skills: 122-125 → 129-135 (net neutral to slight reduction)
- Modern, relevant content ✅

---

## Phase 3: Refinement (1-2 weeks, ~10-15 hours)

### A. Add Bridge Skills (Smooth progression)

#### Digital Footprint Bridge (G3)
```
ID: T32.G3.0X (insert before G3.01)
Skill: Trace a sample digital footprint
Description: Students trace a fictional character's digital footprint using picture
cards showing online activities (creating account → sharing photo → posting comment).
They map what information gets collected at each step and who can see it, practicing
concepts before building the T32.G3.01 coding project.

Dependencies: T32.G2.04
```

---

#### AI Ethics Bridge (G5)
```
ID: T32.G5.XX
Skill: Apply ethics questions to AI tools
Description: Students apply the simple ethics framework from T32.G5.07 specifically
to AI tools they've used (ChatGPT blocks, image generation). For 3+ AI tools, they
evaluate: Does it help? Is it fair? Do users have control? Students document findings
and identify which ethical question is hardest to answer for AI.

Dependencies: T32.G5.07, T21.G5.01
```

---

### B. Dependency Chain Review
- Check all dependencies after consolidations
- Ensure no broken links
- Update skills that depended on consolidated/moved skills

---

### C. Pilot & Iterate
- Share revised skills with 3-5 teachers
- Collect feedback on feasibility
- Adjust based on teacher input
- Finalize skill descriptions

---

**Phase 3 Results:**
- 2 bridge skills added
- All dependencies verified
- Teacher-tested and approved
- Final count: ~128-132 skills ✅

---

## Success Metrics

| Metric | Before | After | Target | Status |
|--------|--------|-------|--------|--------|
| Total skills | 135 | ~128-132 | 120-135 | ✅ |
| G6 skills | 27 | 20 | 18-22 | ✅ |
| G7 skills | 27 | 22 | 18-22 | ✅ |
| G8 skills | 22 | 21 | 18-22 | ✅ |
| Vague verbs | 1 | 0 | 0 | ✅ |
| X-2 violations | 0 | 0 | 0 | ✅ |
| Long descriptions (600+) | 32 | 0 | <5 | ✅ |
| Algorithmic literacy skills | 0 | 2 | 2+ | ✅ |
| Filter bubble skills | 0 | 1 | 1+ | ✅ |
| AI attribution skills | 0 | 1 | 1+ | ✅ |
| Career skill % | 23% | 15-17% | <20% | ✅ |

---

## Timeline

**Week 1-2:** Phase 1 (Consolidations, redistributions, description cleanup)
**Week 3-4:** Phase 2 (Add 5-7 critical modern topics)
**Week 5-6:** Phase 3 (Bridge skills, dependency review, pilot)

**Total:** 6 weeks

---

## Resources Needed

**Writing:** 60-85 hours total
- 20-30h: Consolidation and editing (Phase 1)
- 30-40h: New skill development (Phase 2)
- 10-15h: Refinement and testing (Phase 3)

**Review:** 10-15 hours
- Curriculum team review of consolidations
- Teacher pilot feedback sessions

**Testing:** 3-5 teacher volunteers for Phase 3 pilot

---

## Dependencies & Risks

**Low Risk:**
- All consolidations (clear redundancy, no content loss)
- Description simplification (quality improvement only)
- Grade rebalancing (teachers will appreciate)

**Medium Risk:**
- New modern topics (requires content development, but high value)
- Bridge skills (need to fit smoothly in sequence)

**No High Risks Identified**

---

## Next Steps

1. ✅ Review this action plan with curriculum team
2. ✅ Approve consolidation list (Phase 1A)
3. ✅ Assign writer to description simplification (Phase 1C)
4. ✅ Assign writers to new skills (Phase 2)
5. ✅ Recruit 3-5 teachers for Phase 3 pilot
6. ✅ Schedule weekly check-ins during 6-week implementation

**Start date:** [TBD]
**Target completion:** [Start date + 6 weeks]
